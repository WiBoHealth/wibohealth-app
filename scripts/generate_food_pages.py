"""Generate static, crawlable food pages (pilot batch) in three languages.

    python scripts/generate_food_pages.py

Output (re-running rebuilds everything, nothing is appended twice):
    foods/<slug>.html            Arabic (x-default)
    en/foods/<slug>.html         English
    nl/foods/<slug>.html         Dutch
    js/food-pages.js             id -> slug map used by foods.html / food-details.html
    sitemap.xml                  block between <!-- FOOD-PAGES:START --> and <!-- FOOD-PAGES:END -->

Sources: js/data.js (values, GI provenance), doctor.html (design system: CSS, logo, nav labels).
Per-food text can be overridden in scripts/food_pages_overrides.json (lead, tips, slug).
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://wibohealth.com'
REVIEWED = '2026-10-12'
REVIEWED_TXT = {'ar': '12 أكتوبر 2026', 'en': '12 October 2026', 'nl': '12 oktober 2026'}
LANGS = ('ar', 'en', 'nl')

# --------------------------------------------------------------------------------------------
# Pilot batch: id -> (group, typical portion in grams). Portions are approximate household
# servings pending Dr. Wassim's approval; they only drive the per-portion column and the GL.
# --------------------------------------------------------------------------------------------
PILOT = {
    # measured GI (Atkinson 2021)
    1: ('grain', 150), 14: ('grain', 150), 2: ('grain', 150), 3: ('grain', 50), 4: ('grain', 50), 196: ('grain', 60),
    5: ('grain', 150), 7: ('grain', 250), 17: ('grain', 30), 8: ('grain', 150), 9: ('grain', 150), 10: ('grain', 150),
    11: ('grain', 100), 26: ('tuber', 150), 27: ('tuber', 130), 29: ('tuber', 150), 18: ('legume', 150),
    19: ('legume', 150), 22: ('legume', 150), 48: ('fruit', 150), 49: ('fruit', 120), 50: ('fruit', 130),
    51: ('fruit', 280), 53: ('fruit', 120), 54: ('fruit', 150), 55: ('fruit', 150), 66: ('fruit', 170),
    62: ('dried', 70), 63: ('dried', 40), 68: ('dried', 40), 69: ('dairy_drink', 250), 70: ('dairy_drink', 250),
    79: ('dairy_drink', 250),
    # GI not applicable (< 5 g available carbohydrate / 100 g), high search interest
    101: ('protein', 50), 91: ('protein', 100), 92: ('protein', 100), 93: ('protein', 100), 94: ('protein', 100),
    98: ('protein', 100), 128: ('fat', 14), 59: ('fat', 75), 71: ('dairy_solid', 170), 72: ('dairy_solid', 30),
    74: ('dairy_solid', 30), 77: ('dairy_solid', 30), 30: ('veg', 120), 31: ('veg', 100), 32: ('veg', 120),
    35: ('veg', 90), 36: ('veg', 100), 37: ('veg', 80), 38: ('veg', 100), 39: ('veg', 100), 40: ('veg', 70),
    132: ('drink', 240), 133: ('drink', 240),
}
SLUG_OVERRIDES = {71: 'greek-yogurt'}

GROUPS = {
    'grain': ('الحبوب والنشويات', 'Grains & starches', 'Granen & zetmeel'),
    'tuber': ('البطاطا والدرنيات', 'Potatoes & tubers', 'Aardappelen & knollen'),
    'legume': ('البقوليات', 'Legumes', 'Peulvruchten'),
    'fruit': ('الفواكه', 'Fruit', 'Fruit'),
    'dried': ('التمور والفواكه المجففة', 'Dates & dried fruit', 'Dadels & gedroogd fruit'),
    'dairy_drink': ('الحليب ومشروبات الألبان', 'Milk & dairy drinks', 'Melk & zuiveldranken'),
    'dairy_solid': ('الألبان والأجبان', 'Dairy & cheese', 'Zuivel & kaas'),
    'protein': ('اللحوم والأسماك والبيض', 'Meat, fish & eggs', 'Vlees, vis & eieren'),
    'fat': ('الدهون الصحية', 'Healthy fats', 'Gezonde vetten'),
    'veg': ('الخضار', 'Vegetables', 'Groenten'),
    'drink': ('المشروبات', 'Drinks', 'Dranken'),
}

CARB_NOTE = (
    'لمرضى السكري ومقاومة الإنسولين، يُوصى دائماً بمراعاة الحمل الجلايسيمي (GL) الكلي للوجبة وعدم الاعتماد على المؤشر منفرداً.',
    'For people with diabetes or insulin resistance, it is always recommended to consider the total glycemic load (GL) of the meal rather than relying on the glycemic index alone.',
    'Bij diabetes of insulineresistentie wordt altijd aangeraden rekening te houden met de totale glykemische lading (GL) van de maaltijd, en niet alleen met de glykemische index.')
NA_NOTE = (
    'لا يحتاج هذا الصنف إلى مؤشر جلايسيمي، لكن الأطعمة المرافقة له في الوجبة هي التي تحدد أثرها على سكر الدم.',
    'This food does not need a glycemic index, but the foods eaten with it determine the meal\u2019s effect on blood sugar.',
    'Voor dit product is geen glykemische index nodig, maar de producten die je erbij eet bepalen het effect van de maaltijd op de bloedsuiker.')

# (consumption advice, preparation, important note) per group and language
TIPS = {
    'grain': (
        ('تناوله ضمن وجبة متوازنة وبحصة معتدلة، واجمعه مع مصدر بروتين وخضار غنية بالألياف لإبطاء ارتفاع سكر الدم.',
         'اختر الأصناف الكاملة متى أمكن ولا تُفرط في الطهي؛ فالطهي الطويل يرفع المؤشر الجلايسيمي، وتبريد النشويات المطبوخة ثم إعادة تسخينها قد يخفّض استجابة السكر قليلاً.', CARB_NOTE[0]),
        ('Eat it as part of a balanced meal in a moderate portion, together with a protein source and fibre-rich vegetables to slow the rise in blood sugar.',
         'Choose wholegrain versions when possible and avoid overcooking: longer cooking raises the GI, while cooling cooked starches and reheating them may lower the glucose response slightly.', CARB_NOTE[1]),
        ('Eet het als onderdeel van een evenwichtige maaltijd in een gematigde portie, samen met een eiwitbron en vezelrijke groenten om de bloedsuikerstijging te vertragen.',
         'Kies waar mogelijk volkoren varianten en kook niet te lang: langer koken verhoogt de GI, terwijl afkoelen en opnieuw opwarmen van gekookte zetmeelproducten de glucoserespons iets kan verlagen.', CARB_NOTE[2])),
    'tuber': (
        ('اعتبره مصدر النشويات في الوجبة وليس من الخضار، وقلّل الحصة إذا تناولت معه خبزاً أو أرزاً.',
         'السلق أو الخبز بالقشر أفضل من القلي والهرس؛ فالهرس يرفع المؤشر الجلايسيمي، والقلي يضيف سعرات ودهوناً كثيرة.', CARB_NOTE[0]),
        ('Count it as the starch of the meal rather than as a vegetable, and reduce the portion if you also eat bread or rice.',
         'Boiling or baking with the skin on is better than frying or mashing: mashing raises the GI and frying adds many calories and fat.', CARB_NOTE[1]),
        ('Tel het als zetmeelbron van de maaltijd, niet als groente, en neem een kleinere portie als je er ook brood of rijst bij eet.',
         'Koken of bakken met schil is beter dan frituren of pureren: pureren verhoogt de GI en frituren voegt veel calorieën en vet toe.', CARB_NOTE[2])),
    'legume': (
        ('البقوليات من أفضل مصادر الألياف والبروتين النباتي، ويمكن أن تحل جزئياً محل الأرز أو الخبز في الوجبة.',
         'انقعها جيداً قبل الطهي واطبخها حتى تنضج، واغسل المعلّب منها لتقليل الملح.', CARB_NOTE[0]),
        ('Legumes are among the best sources of fibre and plant protein, and can partly replace rice or bread in a meal.',
         'Soak them well before cooking and cook until tender; rinse canned legumes to reduce the salt.', CARB_NOTE[1]),
        ('Peulvruchten behoren tot de beste bronnen van vezels en plantaardig eiwit en kunnen rijst of brood in een maaltijd deels vervangen.',
         'Week ze goed voor het koken en kook ze gaar; spoel peulvruchten uit blik af om zout te verminderen.', CARB_NOTE[2])),
    'fruit': (
        ('تناول الفاكهة كاملة بقشرها متى أمكن بدلاً من العصير، فالألياف تبطئ امتصاص السكر وتزيد الشبع.',
         'تناولها طازجة وفي موسمها، ويمكن جمعها مع حفنة مكسرات أو لبن لإبطاء الاستجابة السكرية.', CARB_NOTE[0]),
        ('Eat the whole fruit, with the skin where possible, rather than juice: the fibre slows sugar absorption and increases fullness.',
         'Enjoy it fresh and in season; pairing it with a handful of nuts or yoghurt can slow the glucose response.', CARB_NOTE[1]),
        ('Eet het hele fruit, waar mogelijk met schil, in plaats van sap: de vezels vertragen de suikeropname en geven meer verzadiging.',
         'Eet het vers en in het seizoen; combineren met een handje noten of yoghurt kan de glucoserespons vertragen.', CARB_NOTE[2])),
    'dried': (
        ('السكريات فيه مركّزة، لذا التزم بحصة صغيرة واعتبرها جزءاً من سكريات يومك.',
         'اجمعه مع مصدر بروتين أو دهون صحية كالمكسرات أو اللبن لإبطاء ارتفاع سكر الدم.', CARB_NOTE[0]),
        ('Its sugars are concentrated, so keep to a small portion and count it as part of your daily sugar intake.',
         'Combine it with protein or healthy fats such as nuts or yoghurt to slow the rise in blood sugar.', CARB_NOTE[1]),
        ('De suikers zijn geconcentreerd, dus houd het bij een kleine portie en tel het mee als onderdeel van je dagelijkse suikerinname.',
         'Combineer het met eiwit of gezonde vetten zoals noten of yoghurt om de bloedsuikerstijging te vertragen.', CARB_NOTE[2])),
    'dairy_drink': (
        ('مصدر جيد للبروتين والكالسيوم بمؤشر جلايسيمي منخفض؛ اختر الأنواع غير المحلاة.',
         'تجنب إضافة السكر أو العسل أو المنكهات، فهي ترفع الحمل الجلايسيمي للمشروب بشكل كبير.', CARB_NOTE[0]),
        ('A good source of protein and calcium with a low GI; choose unsweetened versions.',
         'Avoid adding sugar, honey or flavourings, which raise the drink\u2019s glycemic load considerably.', CARB_NOTE[1]),
        ('Een goede bron van eiwit en calcium met een lage GI; kies ongezoete varianten.',
         'Voeg geen suiker, honing of smaakstoffen toe; die verhogen de glykemische lading van de drank aanzienlijk.', CARB_NOTE[2])),
    'dairy_solid': (
        ('غني بالبروتين وأثره المباشر على سكر الدم ضئيل، لكنه قد يحتوي دهوناً مشبعة وملحاً، فالتزم بحصة معتدلة.',
         'اختر الأنواع الأقل ملحاً ودهوناً، وقدّمه مع الخضار أو خبز الحبوب الكاملة.', NA_NOTE[0]),
        ('Rich in protein with minimal direct effect on blood sugar, but it can be high in saturated fat and salt, so keep to a moderate portion.',
         'Choose lower-salt, lower-fat versions and serve it with vegetables or wholegrain bread.', NA_NOTE[1]),
        ('Rijk aan eiwit met weinig direct effect op de bloedsuiker, maar het kan veel verzadigd vet en zout bevatten; houd de portie gematigd.',
         'Kies varianten met minder zout en vet en eet het met groenten of volkorenbrood.', NA_NOTE[2])),
    'protein': (
        ('مصدر ممتاز للبروتين الذي يعزز الشبع، ووجوده في الوجبة مع النشويات يساعد على إبطاء ارتفاع سكر الدم.',
         'فضّل الشوي أو السلق أو الطهي بالبخار على القلي العميق، وتجنب التحمير الزائد والتفحّم.', NA_NOTE[0]),
        ('An excellent source of protein, which supports fullness; eating it with starchy foods helps slow the rise in blood sugar.',
         'Prefer grilling, boiling or steaming over deep-frying, and avoid charring.', NA_NOTE[1]),
        ('Een uitstekende eiwitbron die verzadiging bevordert; samen met zetmeelrijke producten helpt het de bloedsuikerstijging te vertragen.',
         'Kies grillen, koken of stomen in plaats van frituren, en vermijd aanbranden.', NA_NOTE[2])),
    'fat': (
        ('غني بالدهون غير المشبعة المفيدة لكنه مرتفع السعرات، فالكمية الصغيرة تكفي.',
         'إضافة كمية معتدلة منه إلى وجبة نشوية قد تبطئ امتصاص السكر؛ استخدمه نيئاً في السلطات متى أمكن.', NA_NOTE[0]),
        ('Rich in healthy unsaturated fats but high in calories, so a small amount is enough.',
         'Adding a moderate amount to a starchy meal can slow sugar absorption; use it raw in salads when possible.', NA_NOTE[1]),
        ('Rijk aan gezonde onverzadigde vetten maar calorierijk, dus een kleine hoeveelheid is genoeg.',
         'Een gematigde hoeveelheid bij een zetmeelrijke maaltijd kan de suikeropname vertragen; gebruik het waar mogelijk rauw in salades.', NA_NOTE[2])),
    'veg': (
        ('خضار منخفضة السعرات وغنية بالماء والألياف، ويمكن أن تملأ نصف الطبق.',
         'تناولها نيئة أو مطهوة قليلاً على البخار للحفاظ على الفيتامينات، وقلّل الزيت عند الطهي.', NA_NOTE[0]),
        ('A low-calorie vegetable rich in water and fibre; it can fill half your plate.',
         'Eat it raw or lightly steamed to preserve vitamins, and use little oil when cooking.', NA_NOTE[1]),
        ('Een caloriearme groente, rijk aan water en vezels; ze kan de helft van je bord vullen.',
         'Eet ze rauw of licht gestoomd om vitamines te behouden, en gebruik weinig olie bij het koken.', NA_NOTE[2])),
    'drink': (
        ('خالٍ تقريباً من السعرات والسكريات عند تناوله دون إضافات.',
         'تجنب السكر والشراب المحلّى والكريمة؛ فهي التي تضيف السعرات والحمل الجلايسيمي.',
         'يحتوي على الكافيين؛ اعتدل في الكمية خاصة في المساء، واستشر طبيبك في حالات الحمل أو عند تناول أدوية تتأثر بالكافيين.'),
        ('Almost free of calories and sugars when taken without additions.',
         'Avoid sugar, syrups and cream, which are what add calories and glycemic load.',
         'Contains caffeine: keep intake moderate, especially in the evening, and ask your doctor if you are pregnant or take medication affected by caffeine.'),
        ('Vrijwel zonder calorieën en suikers als je het zonder toevoegingen drinkt.',
         'Vermijd suiker, siropen en room; die voegen de calorieën en glykemische lading toe.',
         'Bevat cafeïne: drink met mate, vooral \u2019s avonds, en overleg met je arts als je zwanger bent of medicijnen gebruikt die door cafeïne beïnvloed worden.')),
}

UI = {
    'ar': dict(
        dir='rtl', title='{name}: السعرات والمؤشر الجلايسيمي والقيم الغذائية | WiBo Health',
        desc_measured='{name}: {kcal} سعرة لكل 100 غ، المؤشر الجلايسيمي {gi} ({level}) وفق Atkinson 2021، والحمل الجلايسيمي {gl} لحصة {p} غ. قيم غذائية كاملة ونصائح وبدائل.',
        desc_na='{name}: {kcal} سعرة و{protein} غ بروتين لكل 100 غ. المؤشر الجلايسيمي لا ينطبق (أقل من 5 غ كربوهيدرات متاحة). قيم غذائية كاملة ونصائح وبدائل.',
        home='الرئيسية', guide='دليل الأطعمة', gi='المؤشر الجلايسيمي', gl='الحمل الجلايسيمي', kcal='السعرات الحرارية',
        protein='البروتين', per100='لكل 100 غ', per_portion='لحصة {p} غ', na='لا ينطبق',
        levels=('منخفض', 'متوسط', 'مرتفع'), gram='غ', kcal_unit='سعرة',
        tips='💡 الإرشاد الغذائي الذكي', tip_titles=('توصيات الاستهلاك', 'أفضل طرق التحضير', 'ملاحظة غذائية هامة'),
        table='القيم الغذائية', nutrient='العنصر الغذائي', col100='لكل 100 غ', colp='لحصة معتادة ({p} غ)',
        rows=('السعرات الحرارية', 'البروتين', 'الكربوهيدرات', 'الكربوهيدرات المتاحة', 'الدهون', 'الألياف الغذائية'),
        ii_row='مؤشر الإنسولين', ii_tested='مختبر سريرياً (Holt / Bao)',
        compare='مقارنة وبدائل ذكية', alt_lower='بدائل بمؤشر جلايسيمي أقل:', alt_same='أصناف قريبة من نفس العائلة:',
        alt_family='بدائل ذكية من نفس العائلة:',
        lowest_note='هذا من أقل الأصناف مؤشراً في فئته.',
        rank_measured='{ya}أتي في المرتبة {rank} من {m_items} في فئة {group} من حيث المؤشر الجلايسيمي (الأقل أولاً).',
        rank_protein='{ya}وفر {v} غ بروتين لكل 100 سعرة، في المرتبة {rank} من {m} في فئة {group} (الأعلى أولاً).',
        rank_kcal='{ya}حتوي على {v} سعرة لكل 100 غ، في المرتبة {rank} من {m} في فئة {group} (الأقل أولاً).',
        lead_measured='كل 100 غ من {name} تحتوي على {kcal} سعرة حرارية و{avail} غ كربوهيدرات متاحة. مؤشر{h} الجلايسيمي {gi} ({level})، وهو متوسط {studies} في الجداول الدولية (Atkinson 2021). وفي حصة معتادة من {p} غ يبلغ حمل{h} الجلايسيمي {gl} ({gl_level}).',
        lead_na='كل 100 غ من {name} تحتوي على {kcal} سعرة حرارية و{protein} غ بروتين. ولأن{h} {ya}حتوي على أقل من 5 غ كربوهيدرات متاحة لكل 100 غ، فلا ينطبق علي{h} المؤشر الجلايسيمي، ويكون أثر{h} المباشر على سكر الدم ضئيلاً.',
        boodi_title='امسح الباركود في السوبرماركت مع تطبيق بودي 💚',
        boodi_text='يحلل بودي المنتجات المعلّبة فوراً، ويفحص الحلال، ويقترح بدائل أقل سكراً من نفس الرف.',
        boodi_btn='اكتشف تطبيق بودي',
        src_gi='📚 المراجع العلمية المعتمدة: الجداول الدولية للمؤشر الجلايسيمي (Atkinson et al., Am J Clin Nutr 2021) • أبحاث جامعة هارفارد الطبية (Harvard Health).',
        src_value='القيمة المعتمدة: متوسط {studies} (النطاق {lo}–{hi})، درجة الثقة {grade}.',
        src_ii='📚 مراجع مؤشر الإنسولين: Holt SH et al., Am J Clin Nutr 1997;66(5):1264–76 • Bao J et al., Am J Clin Nutr 2009;90(4):986–92.',
        src_link='المنهجية والتفاصيل ←',
        disclaimer='إخلاء مسؤولية: هذه البيانات استرشادية لنمط الحياة وليست جهازاً طبياً تشخيصياً وفق اللائحة الأوروبية EU MDR 2017/745. استشر طبيبك دائماً قبل تعديل نظامك العلاجي.',
        reviewed='راجعه طبياً: <a href="{doctor}">د. وسيم حبيب</a> · آخر مراجعة {date}',
        portion_note='الحصة المعتادة تقريبية لأغراض المقارنة.',
        theme='تبديل المظهر', footer_rights='© 2026 WiBo Health Group. جميع الحقوق محفوظة.',
        nav=('الرئيسية', 'دليل الأطعمة', 'الحاسبات', 'المكملات', 'المقالات', 'تطبيق بودي 💚'), privacy='الخصوصية',
        methodology='المنهجية والمراجع العلمية'),
    'en': dict(
        dir='ltr', title='{name}: Calories, Glycemic Index & Nutrition Facts | WiBo Health',
        desc_measured='{name}: {kcal} kcal per 100 g, glycemic index {gi} ({level}) from Atkinson 2021, glycemic load {gl} per {p} g portion. Full nutrition facts, tips and alternatives.',
        desc_na='{name}: {kcal} kcal and {protein} g protein per 100 g. Glycemic index not applicable (under 5 g available carbohydrate). Full nutrition facts, tips and alternatives.',
        home='Home', guide='Food guide', gi='Glycemic index', gl='Glycemic load', kcal='Calories', protein='Protein',
        per100='per 100 g', per_portion='per {p} g portion', na='Not applicable', levels=('Low', 'Medium', 'High'),
        gram='g', kcal_unit='kcal', tips='💡 Smart Nutritional Guidance',
        tip_titles=('Consumption advice', 'Best preparation methods', 'Important Nutritional Note'),
        table='Nutrition facts', nutrient='Nutrient', col100='Per 100 g', colp='Per typical portion ({p} g)',
        rows=('Calories', 'Protein', 'Carbohydrate', 'Available carbohydrate', 'Fat', 'Dietary fibre'),
        ii_row='Insulin index', ii_tested='clinically tested (Holt / Bao)',
        compare='Comparison & smarter alternatives', alt_lower='Lower-GI alternatives:', alt_same='Related foods from the same family:',
        alt_family='Smart alternatives from the same family:',
        lowest_note='This is one of the lowest-GI foods in its group.',
        rank_measured='It ranks {rank} of {m} measured foods in {group} by glycemic index (lowest first).',
        rank_protein='It provides {v} g of protein per 100 kcal, ranking {rank} of {m} in {group} (highest first).',
        rank_kcal='It has {v} kcal per 100 g, ranking {rank} of {m} in {group} (lowest first).',
        lead_measured='Every 100 g of {name} contains {kcal} kcal and {avail} g of available carbohydrate. Its glycemic index is {gi} ({level}), the average of {studies} in the International GI Tables (Atkinson 2021). A typical {p} g portion has a glycemic load of {gl} ({gl_level}).',
        lead_na='Every 100 g of {name} contains {kcal} kcal and {protein} g of protein. Because it has less than 5 g of available carbohydrate per 100 g, the glycemic index does not apply and its direct effect on blood sugar is minimal.',
        boodi_title='Scan supermarket barcodes with the boodi app 💚',
        boodi_text='boodi analyses packaged products instantly, checks halal status and suggests lower-sugar alternatives from the same shelf.',
        boodi_btn='Discover the boodi app',
        src_gi='📚 Scientific sources: International Tables of Glycemic Index (Atkinson et al., Am J Clin Nutr 2021) • Harvard Health Publishing.',
        src_value='Approved value: average of {studies} (range {lo}–{hi}), confidence grade {grade}.',
        src_ii='📚 Insulin index sources: Holt SH et al., Am J Clin Nutr 1997;66(5):1264–76 • Bao J et al., Am J Clin Nutr 2009;90(4):986–92.',
        src_link='Methodology & details →',
        disclaimer='Disclaimer: This guidance is for nutritional lifestyle orientation and does not constitute a diagnostic medical device under EU Regulation MDR 2017/745.',
        reviewed='Medically reviewed by <a href="{doctor}">Dr. Wassim Habib</a> · Last reviewed {date}',
        portion_note='The typical portion is approximate, for comparison purposes.',
        theme='Toggle theme', footer_rights='© 2026 WiBo Health Group. All rights reserved.',
        nav=('Home', 'Food Guide', 'Calculators', 'Supplements', 'Articles', 'boodi App 💚'), privacy='Privacy',
        methodology='Methodology & scientific references'),
    'nl': dict(
        dir='ltr', title='{name}: calorieën, glykemische index & voedingswaarde | WiBo Health',
        desc_measured='{name}: {kcal} kcal per 100 g, glykemische index {gi} ({level}) volgens Atkinson 2021, glykemische lading {gl} per portie van {p} g. Volledige voedingswaarden, tips en alternatieven.',
        desc_na='{name}: {kcal} kcal en {protein} g eiwit per 100 g. Glykemische index niet van toepassing (minder dan 5 g beschikbare koolhydraten). Volledige voedingswaarden, tips en alternatieven.',
        home='Home', guide='Voedingswijzer', gi='Glykemische index', gl='Glykemische lading', kcal='Calorieën', protein='Eiwit',
        per100='per 100 g', per_portion='per portie van {p} g', na='Niet van toepassing', levels=('Laag', 'Gemiddeld', 'Hoog'),
        gram='g', kcal_unit='kcal', tips='💡 Slimme voedingsbegeleiding',
        tip_titles=('Consumptieadvies', 'Beste bereidingswijzen', 'Belangrijke voedingsnotitie'),
        table='Voedingswaarden', nutrient='Voedingsstof', col100='Per 100 g', colp='Per gangbare portie ({p} g)',
        rows=('Calorieën', 'Eiwit', 'Koolhydraten', 'Beschikbare koolhydraten', 'Vet', 'Voedingsvezels'),
        ii_row='Insuline-index', ii_tested='klinisch getest (Holt / Bao)',
        compare='Vergelijking & slimme alternatieven', alt_lower='Alternatieven met een lagere GI:',
        alt_same='Verwante producten uit dezelfde familie:', alt_family='Slimme alternatieven uit dezelfde familie:', lowest_note='Dit is een van de producten met de laagste GI in zijn groep.',
        rank_measured='Het staat op plaats {rank} van {m} gemeten producten in {group} op glykemische index (laagste eerst).',
        rank_protein='Het levert {v} g eiwit per 100 kcal en staat op plaats {rank} van {m} in {group} (hoogste eerst).',
        rank_kcal='Het bevat {v} kcal per 100 g en staat op plaats {rank} van {m} in {group} (laagste eerst).',
        lead_measured='Elke 100 g {name} bevat {kcal} kcal en {avail} g beschikbare koolhydraten. De glykemische index is {gi} ({level}), het gemiddelde van {studies} in de internationale GI-tabellen (Atkinson 2021). Een gangbare portie van {p} g heeft een glykemische lading van {gl} ({gl_level}).',
        lead_na='Elke 100 g {name} bevat {kcal} kcal en {protein} g eiwit. Omdat het minder dan 5 g beschikbare koolhydraten per 100 g bevat, is de glykemische index niet van toepassing en is het directe effect op de bloedsuiker minimaal.',
        boodi_title='Scan barcodes in de supermarkt met de boodi-app 💚',
        boodi_text='boodi analyseert verpakte producten direct, controleert de halalstatus en stelt suikerarmere alternatieven uit hetzelfde schap voor.',
        boodi_btn='Ontdek de boodi-app',
        src_gi='📚 Wetenschappelijke bronnen: Internationale GI-tabellen (Atkinson et al., Am J Clin Nutr 2021) • Harvard Health Publishing.',
        src_value='Goedgekeurde waarde: gemiddelde van {studies} (bereik {lo}–{hi}), betrouwbaarheidsgraad {grade}.',
        src_ii='📚 Bronnen insuline-index: Holt SH et al., Am J Clin Nutr 1997;66(5):1264–76 • Bao J et al., Am J Clin Nutr 2009;90(4):986–92.',
        src_link='Methodologie & details →',
        disclaimer='Algemene disclaimer: Deze informatie is uitsluitend bedoeld als voedingsadvies en is geen medisch diagnostisch hulpmiddel volgens EU MDR 2017/745.',
        reviewed='Medisch gecontroleerd door <a href="{doctor}">dr. Wassim Habib</a> · Laatst gecontroleerd {date}',
        portion_note='De gangbare portie is een benadering, bedoeld om te vergelijken.',
        theme='Thema wisselen', footer_rights='© 2026 WiBo Health Group. Alle rechten voorbehouden.',
        nav=('Home', 'Voedingswijzer', 'Calculators', 'Supplementen', 'Artikelen', 'boodi App 💚'), privacy='Privacy',
        methodology='Methodologie & wetenschappelijke bronnen'),
}


FAQ = {
    'ar': dict(
        title='أسئلة شائعة',
        q=('هل {ya}ناسب {name} الدايت وإنقاص الوزن؟', 'كيف {ya}ؤثر {name} على سكر الدم؟', 'ما القيمة الغذائية لحصة معتادة من {name}؟'),
        w_high='يحتوي {name} على {kcal} سعرة لكل 100 غ، وهي كمية مرتفعة من السعرات، لذلك يُستحسن استخدام كميات صغيرة ومقاسة من{h} في نظام إنقاص الوزن؛ فحصة {p} غ تعطي {kcal_p} سعرة.',
        w_low='نعم، فسعرات {name} منخفضة جداً ({kcal} سعرة لكل 100 غ)، ويمكن تناول كمية جيدة من{h} لزيادة حجم الوجبة والشعور بالشبع دون سعرات كثيرة.',
        w_protein='يمكن أن {ya}كون جزءاً مفيداً من نظام إنقاص الوزن، لأن{h} {ya}وفر {ppk} غ بروتين لكل 100 سعرة، والبروتين يعزز الشبع. وحصة {p} غ تعطي {kcal_p} سعرة.',
        w_fiber='يمكن إدخال{h} باعتدال، ف{huwa} {ya}حتوي على {fiber} غ ألياف لكل 100 غ تساعد على الشبع، وحصة {p} غ تعطي {kcal_p} سعرة.',
        w_general='يمكن إدخال{h} ضمن نظام متوازن مع التحكم بالحصة: حصة {p} غ تعطي {kcal_p} سعرة، والمهم هو مجموع سعرات اليوم ونوعية بقية الوجبة.',
        s_measured='مؤشر{h} الجلايسيمي {gi} ({level}) وفق Atkinson 2021. وفي حصة معتادة من {p} غ يبلغ حمل{h} الجلايسيمي {gl} ({gl_level}){advice}',
        s_advice=('، لذلك يكون تأثير هذه الحصة على سكر الدم محدوداً.', '، لذلك يُفضّل تناول{h} مع بروتين أو خضار غنية بالألياف.',
                  '، لذلك يُفضّل تقليل الحصة أو تقسيمها وتناول{h} مع البروتين والألياف.'),
        s_na_zero='لا يحتوي {name} تقريباً على كربوهيدرات متاحة، لذلك لا ينطبق علي{h} المؤشر الجلايسيمي، وأثر{h} المباشر على سكر الدم ضئيل. أما أثر الوجبة فتحدده الأطعمة المرافقة ل{h} كالخبز والأرز والصلصات المحلاة.',
        s_na='يحتوي {name} على {avail} غ فقط من الكربوهيدرات المتاحة لكل 100 غ، لذلك لا ينطبق علي{h} المؤشر الجلايسيمي، وأثر{h} المباشر على سكر الدم ضئيل. أما أثر الوجبة فتحدده الأطعمة المرافقة ل{h} كالخبز والأرز والصلصات المحلاة.',
        portion='حصة معتادة من {p} غ من {name} تحتوي تقريباً على {kcal_p} سعرة، و{prot_p} غ بروتين، و{carb_p} غ كربوهيدرات، و{fat_p} غ دهون، و{fib_p} غ ألياف.'),
    'en': dict(
        title='Frequently asked questions',
        q=('{Is_} {name} good for weight loss?', 'How {does} {name} affect blood sugar?', 'What is the nutritional value of a typical portion of {name}?'),
        w_high='{name} {provides} {kcal} kcal per 100 g, so it is high in calories and fits a weight-loss plan only in small, measured amounts; a {p} g portion gives {kcal_p} kcal.',
        w_low='Yes. {name} {is_} very low in calories ({kcal} kcal per 100 g), so you can eat a generous amount to add volume and fullness to a meal without many calories.',
        w_protein='It can be a useful part of a weight-loss plan because it provides {ppk} g of protein per 100 kcal, and protein supports fullness. A {p} g portion gives {kcal_p} kcal.',
        w_fiber='It can be included in moderation: it contains {fiber} g of fibre per 100 g, which supports fullness, and a {p} g portion gives {kcal_p} kcal.',
        w_general='It can fit a balanced plan with portion control: a {p} g portion gives {kcal_p} kcal, and what matters most is your total daily intake and the rest of the meal.',
        s_measured='Its glycemic index is {gi} ({level}) according to Atkinson 2021. A typical {p} g portion has a glycemic load of {gl} ({gl_level}){advice}',
        s_advice=(', so the effect of this portion on blood sugar is limited.', ', so it is best combined with protein or fibre-rich vegetables.',
                  ', so it is best to reduce or split the portion and combine it with protein and fibre.'),
        s_na='{name} {contains} only {avail} g of available carbohydrate per 100 g, so the glycemic index does not apply and its direct effect on blood sugar is minimal. The meal’s effect depends on what you eat with it, such as bread, rice or sweetened sauces.',
        s_na_zero='{name} {contains} virtually no available carbohydrate, so the glycemic index does not apply and its direct effect on blood sugar is minimal. The meal’s effect depends on what you eat with it, such as bread, rice or sweetened sauces.',
        portion='A typical {p} g portion of {name} provides about {kcal_p} kcal, {prot_p} g protein, {carb_p} g carbohydrate, {fat_p} g fat and {fib_p} g fibre.'),
    'nl': dict(
        title='Veelgestelde vragen',
        q=('{Is_} {name} geschikt om af te vallen?', 'Wat is het effect van {name} op de bloedsuiker?', 'Wat is de voedingswaarde van een gangbare portie {name}?'),
        w_high='{name} {levert} {kcal} kcal per 100 g en {is_} dus calorierijk; in een afvalplan past het alleen in kleine, afgemeten hoeveelheden. Een portie van {p} g geeft {kcal_p} kcal.',
        w_low='Ja. {name} {is_} zeer caloriearm ({kcal} kcal per 100 g), dus je kunt er royaal van eten om een maaltijd volume en verzadiging te geven zonder veel calorieën.',
        w_protein='Het kan een nuttig onderdeel zijn van een afvalplan, omdat het {ppk} g eiwit per 100 kcal levert en eiwit de verzadiging bevordert. Een portie van {p} g geeft {kcal_p} kcal.',
        w_fiber='Het past met mate: het bevat {fiber} g vezels per 100 g, wat de verzadiging ondersteunt, en een portie van {p} g geeft {kcal_p} kcal.',
        w_general='Het past in een evenwichtig eetpatroon met aandacht voor de portie: een portie van {p} g geeft {kcal_p} kcal, en het gaat vooral om je totale dagelijkse inname en de rest van de maaltijd.',
        s_measured='De glykemische index is {gi} ({level}) volgens Atkinson 2021. Een gangbare portie van {p} g heeft een glykemische lading van {gl} ({gl_level}){advice}',
        s_advice=(', dus het effect van deze portie op de bloedsuiker is beperkt.', ', dus combineer het bij voorkeur met eiwit of vezelrijke groenten.',
                  ', dus verklein of verdeel de portie bij voorkeur en combineer haar met eiwit en vezels.'),
        s_na='{name} {bevat} slechts {avail} g beschikbare koolhydraten per 100 g, dus de glykemische index is niet van toepassing en het directe effect op de bloedsuiker is minimaal. Het effect van de maaltijd hangt af van wat je erbij eet, zoals brood, rijst of gezoete sauzen.',
        s_na_zero='{name} {bevat} vrijwel geen beschikbare koolhydraten, dus de glykemische index is niet van toepassing en het directe effect op de bloedsuiker is minimaal. Het effect van de maaltijd hangt af van wat je erbij eet, zoals brood, rijst of gezoete sauzen.',
        portion='Een gangbare portie van {p} g {name} levert ongeveer {kcal_p} kcal, {prot_p} g eiwit, {carb_p} g koolhydraten, {fat_p} g vet en {fib_p} g vezels.'),
}


PLURAL = {'en': {18, 19, 22, 53, 62, 63, 68}, 'nl': {17, 18, 19, 22, 40, 53, 62, 63, 68}}
VERBS = {'en': (dict(is_='is', does='does', contains='contains', provides='provides'),
                dict(is_='are', does='do', contains='contain', provides='provide')),
         'nl': (dict(is_='is', bevat='bevat', levert='levert'), dict(is_='zijn', bevat='bevatten', levert='leveren')),
         'ar': (dict(), dict())}


def build_faq(food, lang, name, portion, measured, gi=None, lvl=None, gl=None, glv=None, g=None):
    """Three questions whose answers are computed from the food's own numbers."""
    f, u = FAQ[lang], UI[lang]
    v = dict(VERBS[lang][1 if food['id'] in PLURAL.get(lang, set()) else 0])
    if 'is_' in v:
        v['Is_'] = v['is_'].capitalize()
    v.update(g or {})
    pf = portion / 100.0
    kcal = food['kcal']
    kcal_p = round(kcal * pf)
    ppk = food['protein'] / kcal * 100 if kcal else 0
    if kcal >= 400:
        w = f['w_high']
    elif kcal <= 60:
        w = f['w_low']
    elif ppk >= 8:
        w = f['w_protein']
    elif food['fiber'] >= 3:
        w = f['w_fiber']
    else:
        w = f['w_general']
    a1 = w.format(name=name, kcal=round(kcal), p=portion, kcal_p=kcal_p, ppk=fmt(ppk), fiber=fmt(food['fiber']), **v)
    if measured:
        a2 = f['s_measured'].format(gi=gi, level=u['levels'][lvl], p=portion, gl=fmt(gl), gl_level=u['levels'][glv],
                                    advice=f['s_advice'][glv].format(**v), **v)
    else:
        tmpl = f['s_na_zero'] if food['avail'] < 0.5 else f['s_na']
        a2 = tmpl.format(name=name, avail=fmt(food['avail']), **v)
    a3 = f['portion'].format(**v, p=portion, name=name, kcal_p=kcal_p, prot_p=fmt(food['protein'] * pf),
                             carb_p=fmt(food['carbs'] * pf), fat_p=fmt(food['fat'] * pf), fib_p=fmt(food['fiber'] * pf))
    return [(q.format(name=name, **v), a) for q, a in zip(f['q'], (a1, a2, a3))]


# --------------------------------------------------------------------------------------------
# Arabic: definite form (ال التعريف) and grammatical gender of a food name, for use inside sentences
# --------------------------------------------------------------------------------------------
AR_DEFINITE_OVERRIDES = {          # names whose natural definite form does not follow the rules
    'ملوخية ورق خضراء': 'الملوخية الخضراء',
    'لحم بقري ستيك مشوي': 'ستيك اللحم البقري المشوي',
    'بيض مسلوق كامل': 'البيض المسلوق',
    'حليب كامل الدسم 3.5%': 'الحليب كامل الدسم',
    'لبن زبادي يوناني 10%': 'الزبادي اليوناني',
}
AR_IDAFA = {('صدر', 'دجاج'), ('زيت', 'زيتون'), ('سمك', 'سلمون'), ('لحم', 'غنم'), ('خبز', 'قمح'),
            ('جبنة', 'شيدر'), ('جبنة', 'حلوم')}        # construct state: only the second noun takes ال
AR_STOP = {'على', 'في', 'من', 'مع', 'عن', 'إلى', 'أبو', 'بدون'}   # prepositions / proper names: rest stays as is
AR_FEMININE_NOUNS = {'كمثرى', 'بطاطا', 'كوسا', 'مانجو', 'كينوا', 'سبانخ', 'فاصوليا'}
AR_FEMININE_ADJ = {'بيضاء', 'سوداء', 'حمراء', 'خضراء', 'صفراء'}


def _core_words(name):
    name = re.sub(r'\(.*?\)', ' ', name)                     # drop parenthetical alternatives
    return [w for w in name.split() if '/' not in w]          # drop colour variants like أحمر/أخضر


def ar_definite(name):
    """'أرز أبيض مطبوخ' -> 'الأرز الأبيض المطبوخ'; 'صدر دجاج مشوي' -> 'صدر الدجاج المشوي'."""
    if name in AR_DEFINITE_OVERRIDES:
        return AR_DEFINITE_OVERRIDES[name]
    words = _core_words(name)
    out, frozen = [], False
    for i, w in enumerate(words):
        nxt = words[i + 1] if i + 1 < len(words) else ''
        if frozen or w in AR_STOP:
            frozen = True
            out.append(w)
        elif re.match(r'^[\d.%]+$', w) or w.startswith(('ال', 'بال', 'لل', 'وال')):
            out.append(w)
        elif (w, nxt) in AR_IDAFA or nxt.startswith('ال'):    # first noun of a construct stays indefinite
            out.append(w)
        else:
            out.append('ال' + w)
    return ' '.join(out)


def ar_is_feminine(name):
    words = _core_words(name)
    head = words[0] if words else ''
    if head.endswith('ة') or head in AR_FEMININE_NOUNS:
        return True
    return bool(len(words) > 1 and (words[1].endswith('ة') or words[1] in AR_FEMININE_ADJ))


def ar_pron(name):
    """Placeholders for Arabic templates: {h} = ه/ها (its), {ya} = ي/ت (verb prefix), {huwa} = هو/هي."""
    fem = ar_is_feminine(name)
    return dict(h='ها' if fem else 'ه', ya='ت' if fem else 'ي', huwa='هي' if fem else 'هو')


# --------------------------------------------------------------------------------------------
# Culinary-aware alternatives: each food's family, in order of preference (curated by hand).
# Measured foods list lower-GI options first; the heading says "lower GI" only when all are lower.
# --------------------------------------------------------------------------------------------
ALTERNATIVES = {
    1: [14, 2, 8], 14: [8, 9, 2], 2: [8, 9, 14], 8: [9, 18, 14], 9: [18, 8, 14], 10: [9, 8, 5], 5: [9, 18, 8],
    3: [4, 7, 17], 196: [4, 7, 17], 4: [7, 17, 8], 7: [17, 4, 8], 17: [7, 4, 8],
    11: [27, 19, 22], 26: [27, 18, 19], 29: [26, 27, 18], 27: [11, 19, 18],
    18: [19, 22, 9], 19: [18, 22, 9], 22: [18, 19, 8],
    54: [48, 66, 50], 51: [66, 48, 50], 49: [48, 66, 50], 53: [48, 66, 50], 55: [48, 66, 50],
    48: [66, 50, 55], 50: [48, 66, 55], 66: [48, 50, 55],
    62: [66, 48, 50], 63: [62, 66, 48], 68: [62, 48, 53],
    69: [70, 79, 71], 70: [69, 79, 71], 79: [69, 70, 72],
    101: [91, 98, 72], 91: [98, 94, 101], 92: [91, 94, 98], 93: [91, 92, 94], 94: [98, 91, 101], 98: [94, 91, 101],
    128: [59], 59: [128],
    71: [72, 79, 69], 72: [71, 77, 74], 74: [77, 72, 71], 77: [72, 74, 71],
    30: [31, 37, 32], 31: [30, 32, 35], 32: [39, 36, 30], 35: [36, 37, 32], 36: [35, 32, 40], 37: [38, 35, 30],
    38: [37, 39, 32], 39: [32, 38, 30], 40: [32, 35, 36],
    132: [133], 133: [132],
}


def ar_measured_items(n):
    """Arabic counted noun: 3-10 take a plural, 11+ a singular accusative."""
    if n == 1:
        return 'صنف مقاس واحد'
    if n == 2:
        return 'صنفين مقاسين'
    if 3 <= n <= 10:
        return f'{n} أصناف مقاسة'
    return f'{n} صنفاً مقاساً'


def studies_word(n, lang):
    if lang == 'ar':
        return {1: 'دراسة واحدة', 2: 'دراستين'}.get(n, f'{n} دراسات' if 3 <= n <= 10 else f'{n} دراسة')
    if lang == 'en':
        return '1 study' if n == 1 else f'{n} studies'
    return '1 studie' if n == 1 else f'{n} studies'


# --------------------------------------------------------------------------------------------
# Data
# --------------------------------------------------------------------------------------------
def load_foods():
    text = (ROOT / 'js' / 'data.js').read_text(encoding='utf-8')
    foods = {}
    for line in re.findall(r"\{\s*id:\s*\d+,[^\n]*", text):
        def s(k):
            m = re.search(r"\b%s:\s*'((?:[^'\\]|\\.)*)'" % k, line)
            return m.group(1).replace("\\'", "'") if m else ''

        def n(k):
            m = re.search(r"\b%s:\s*(-?[\d.]+|null)" % k, line)
            return None if not m or m.group(1) == 'null' else float(m.group(1))

        def arr(k):
            m = re.search(r"\b%s:\s*\[([^\]]*)\]" % k, line)
            return [float(x) for x in m.group(1).split(',')] if m and m.group(1).strip() else []

        fid = int(re.search(r'id:\s*(\d+)', line).group(1))
        foods[fid] = dict(
            id=fid, ar=s('name'), en=s('nameEn'), nl=s('nameNl'), image=s('image'), icon=s('icon'),
            gi=n('gi'), gi_status=s('gi_status'), gi_grade=s('gi_grade'), gi_n=n('gi_n'), gi_range=arr('gi_range'),
            ii=n('ii'), kcal=n('calories') or 0, protein=n('protein') or 0, carbs=n('carbs') or 0, fat=n('fat') or 0,
            fiber=n('fiber') or 0)
        foods[fid]['avail'] = round(max(0.0, foods[fid]['carbs'] - foods[fid]['fiber']), 1)
    return foods


def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


def fmt(x):
    x = round(x, 1)
    return str(int(x)) if float(x).is_integer() else str(x)


def gi_level(v):
    return 0 if v <= 55 else (1 if v < 70 else 2)


def gl_level(v):
    return 0 if v <= 10 else (1 if v < 20 else 2)


def esc(s):
    return html.escape(s, quote=True)


# --------------------------------------------------------------------------------------------
# Design system from doctor.html
# --------------------------------------------------------------------------------------------
doctor = (ROOT / 'doctor.html').read_text(encoding='utf-8').replace('\r\n', '\n')
BASE_CSS = re.search(r'    <style>\n(.*?)    </style>\n', doctor, re.S).group(1)
LOGO_SVG = re.search(r'(<svg class="brand-logo-svg".*?</svg>)', doctor, re.S).group(1)

PAGE_CSS = """
        a.lang-btn { text-decoration: none; }
        .food-page h1, .food-page h3, .food-page td, .boodi-card h2, .food-page strong { color: var(--text-main); }
        .food-page { max-width: 980px; }
        .breadcrumb { font-size: 0.85rem; color: var(--text-muted); margin-bottom: 18px; }
        .breadcrumb a { color: var(--text-muted); text-decoration: none; }
        .breadcrumb a:hover { color: var(--primary); }
        .food-hero { display: flex; gap: 24px; align-items: center; flex-wrap: wrap; margin-bottom: 18px; }
        .food-hero img, .food-hero .food-emoji {
            width: 150px; height: 150px; border-radius: 22px; object-fit: cover; flex-shrink: 0;
            border: 3px solid var(--primary-glow); box-shadow: var(--shadow); background: var(--bg-input);
        }
        .food-hero .food-emoji { display: flex; align-items: center; justify-content: center; font-size: 4rem; }
        .food-hero-text { flex: 1; min-width: 220px; }
        .food-hero-text h1 { font-size: 2rem; font-weight: 900; line-height: 1.3; margin-bottom: 4px; }
        .food-subtitle { color: var(--text-muted); font-weight: 600; }
        .group-chip {
            display: inline-block; margin-top: 10px; padding: 4px 14px; border-radius: 999px; font-size: 0.82rem;
            font-weight: 700; color: var(--primary); background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.25);
        }
        .lead { font-size: 1.04rem; margin: 6px 0 22px; }
        .reviewed { font-size: 0.85rem; color: var(--text-muted); margin-top: -12px; margin-bottom: 22px; }
        .reviewed a { color: var(--primary); text-decoration: none; font-weight: 700; }
        .stat-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px; margin-bottom: 26px; }
        .stat-box {
            background: var(--bg-input); border: 1px solid var(--border-color); border-radius: var(--radius-md);
            padding: 16px 12px; text-align: center;
        }
        .stat-box h2 { font-size: 0.82rem; color: var(--text-muted); font-weight: 700; margin-bottom: 6px; }
        .stat-num { font-size: 2rem; font-weight: 900; line-height: 1.2; }
        .stat-num.low { color: #2ecc71; } .stat-num.medium { color: #f39c12; } .stat-num.high { color: #e74c3c; }
        .stat-num.muted { color: var(--text-muted); } .stat-num.kcal { color: #3498db; } .stat-num.protein { color: #9b59b6; }
        .stat-sub { font-size: 0.78rem; color: var(--text-muted); font-weight: 600; }
        .badge {
            display: inline-block; margin-top: 6px; padding: 2px 10px; border-radius: 999px; font-size: 0.72rem;
            font-weight: 700; border: 1px solid transparent;
        }
        .badge.low { background: rgba(46, 204, 113, 0.12); border-color: rgba(46, 204, 113, 0.45); color: #2ecc71; }
        .badge.medium { background: rgba(243, 156, 18, 0.12); border-color: rgba(243, 156, 18, 0.45); color: #f39c12; }
        .badge.high { background: rgba(231, 76, 60, 0.12); border-color: rgba(231, 76, 60, 0.45); color: #e74c3c; }
        .badge.neutral { background: rgba(148, 163, 184, 0.14); border-color: rgba(148, 163, 184, 0.45); color: var(--text-muted); }
        .tip-list { display: grid; gap: 12px; margin: 10px 0 26px; }
        .tip {
            background: var(--bg-input); border: 1px solid var(--border-color); border-inline-start: 4px solid var(--primary);
            border-radius: var(--radius-sm); padding: 14px 18px;
        }
        .tip h3 { font-size: 1rem; font-weight: 800; margin-bottom: 4px; display: flex; gap: 8px; align-items: center; }
        .tip.warn { border-inline-start-color: #f39c12; }
        .tip p { color: var(--text-muted); margin: 0; }
        .nutrition-table { width: 100%; border-collapse: collapse; margin: 10px 0 6px; font-size: 0.95rem; }
        .nutrition-table th, .nutrition-table td { padding: 11px 12px; border-bottom: 1px solid var(--border-color); text-align: start; }
        .nutrition-table th { color: var(--primary); font-weight: 800; background: rgba(16, 185, 129, 0.06); }
        .nutrition-table td:not(:first-child) { font-weight: 700; }
        .table-note { font-size: 0.8rem; color: var(--text-muted); margin-bottom: 26px; }
        .alt-list { list-style: none; display: grid; gap: 10px; margin: 10px 0 26px; padding: 0; }
        .alt-list a {
            display: flex; justify-content: space-between; gap: 12px; padding: 12px 16px; border-radius: var(--radius-sm);
            background: var(--bg-input); border: 1px solid var(--border-color); color: var(--text-main); text-decoration: none; font-weight: 700;
        }
        .alt-list a:hover { border-color: var(--primary); color: var(--primary); }
        .alt-list span { color: var(--text-muted); font-weight: 600; white-space: nowrap; }
        .faq-list { display: grid; gap: 12px; margin: 10px 0 26px; }
        .faq-item { background: var(--bg-input); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 14px 18px; }
        .faq-item h3 { font-size: 1rem; font-weight: 800; margin-bottom: 6px; }
        .faq-item p { color: var(--text-muted); margin: 0; }
        .boodi-card {
            display: flex; gap: 18px; align-items: center; justify-content: space-between; flex-wrap: wrap;
            padding: 22px 24px; border-radius: var(--radius-md); margin-bottom: 26px;
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.16), rgba(6, 182, 212, 0.12));
            border: 1px solid rgba(16, 185, 129, 0.35);
        }
        .boodi-card h2 { font-size: 1.15rem; font-weight: 800; margin-bottom: 4px; }
        .boodi-card p { color: var(--text-muted); margin: 0; }
        .boodi-btn {
            display: inline-flex; align-items: center; gap: 8px; padding: 11px 22px; border-radius: 30px; background: var(--primary);
            color: #ffffff; font-weight: 800; text-decoration: none; white-space: nowrap;
        }
        .boodi-btn:hover { background: var(--primary-hover); }
        .source-strip {
            background: var(--bg-input); border: 1px solid rgba(16, 185, 129, 0.35); border-inline-start: 4px solid var(--primary);
            border-radius: 14px; padding: 12px 16px; margin-bottom: 10px; color: var(--text-muted); font-size: 0.85rem;
            font-weight: 600; overflow-wrap: anywhere;
        }
        .source-strip a { color: var(--primary); font-weight: 800; text-decoration: none; white-space: nowrap; }
        .disclaimer-box {
            margin-top: 18px; padding: 14px 18px; border-radius: 12px; background: rgba(15, 23, 42, 0.62);
            border: 1px solid rgba(226, 232, 240, 0.22); color: #e2e8f0; font-size: 0.85rem; text-align: center;
        }
        html[data-theme="light"] .disclaimer-box { background: #f1f5f9; border-color: rgba(15, 23, 42, 0.12); color: #334155; }
        @media (max-width: 760px) {
            .stat-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            .food-hero { flex-direction: column; text-align: center; }
            .food-hero-text h1 { font-size: 1.6rem; }
        }
"""


def page_url(slug, lang, absolute=True):
    path = f'/foods/{slug}.html' if lang == 'ar' else f'/{lang}/foods/{slug}.html'
    return SITE + path if absolute else path


def site_link(path, lang):
    """Link to a regular site page in the reader's language."""
    return path if lang == 'ar' else f"{path}{'&' if '?' in path else '?'}lang={lang}"


# --------------------------------------------------------------------------------------------
# Page builder
# --------------------------------------------------------------------------------------------
def build(food, lang, ctx):
    u = UI[lang]
    li = LANGS.index(lang)
    slug, group, portion = ctx['slug'][food['id']], PILOT[food['id']][0], PILOT[food['id']][1]
    name = food[lang] or food['en']
    # inside Arabic sentences the name takes the definite article; headings keep the display name
    sname = ar_definite(name) if lang == 'ar' else name
    g = ar_pron(name) if lang == 'ar' else {}
    subtitle = {'ar': food['en'], 'en': food['nl'], 'nl': food['en']}[lang]
    if subtitle == name:
        subtitle = ''
    group_name = GROUPS[group][li]
    measured = food['gi_status'] == 'measured' and food['gi'] is not None
    p_factor = portion / 100.0
    tips = list(ctx['overrides'].get(str(food['id']), {}).get('tips', {}).get(lang) or TIPS[group][li])
    if len(tips) == 2:                      # food-specific consumption + preparation; keep the approved note
        tips.append(TIPS[group][li][2])

    # -------- numbers
    kcal, protein, avail = round(food['kcal']), fmt(food['protein']), fmt(food['avail'])
    if measured:
        gi = int(food['gi'])
        lvl = gi_level(gi)
        gl = round(gi * food['avail'] * p_factor / 100, 1)
        glv = gl_level(gl)
        studies = studies_word(int(food['gi_n'] or 1), lang)
        lead = u['lead_measured'].format(name=sname, kcal=kcal, avail=avail, gi=gi, level=u['levels'][lvl], studies=studies,
                                         p=portion, gl=fmt(gl), gl_level=u['levels'][glv], **g)
        desc = u['desc_measured'].format(name=name, kcal=kcal, gi=gi, level=u['levels'][lvl], gl=fmt(gl), p=portion)
    else:
        lead = u['lead_na'].format(name=sname, kcal=kcal, protein=protein, **g)
        desc = u['desc_na'].format(name=name, kcal=kcal, protein=protein)
    # a doctor-approved introduction replaces the computed lead (the numbers stay in the cards and table)
    lead = ctx['overrides'].get(str(food['id']), {}).get('lead', {}).get(lang) or lead
    title = u['title'].format(name=name)

    # -------- FAQ (answers computed from the numbers)
    if measured:
        faq = build_faq(food, lang, sname, portion, True, gi=gi, lvl=lvl, gl=gl, glv=glv, g=g)
    else:
        faq = build_faq(food, lang, sname, portion, False, g=g)
    faq_html = ''.join(f'<div class="faq-item"><h3>{esc(q)}</h3><p>{esc(a)}</p></div>' for q, a in faq)
    faq_schema = {
        "@context": "https://schema.org", "@type": "FAQPage", "inLanguage": lang,
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq],
    }

    # -------- comparison & alternatives (within the pilot group)
    peers = [ctx['foods'][i] for i, (g, _) in PILOT.items() if g == group]
    def link_item(f, right):
        return (f'<li><a href="{page_url(ctx["slug"][f["id"]], lang, absolute=False)}">{esc(f[lang] or f["en"])}'
                f'<span>{right}</span></a></li>')
    family = [ctx['foods'][i] for i in ALTERNATIVES.get(food['id'], []) if i in PILOT]
    if measured:
        ranked = sorted([f for f in peers if f['gi_status'] == 'measured'], key=lambda f: f['gi'])
        rank = [f['id'] for f in ranked].index(food['id']) + 1
        compare_txt = u['rank_measured'].format(rank=rank, m=len(ranked), m_items=ar_measured_items(len(ranked)),
                                                group=group_name, **g)
        if rank == 1:
            compare_txt += ' ' + u['lowest_note']
        has_gi = [f for f in family if f['gi_status'] == 'measured']
        lower = sorted([f for f in has_gi if f['gi'] < food['gi']], key=lambda f: f['gi'])
        alts = (lower + [f for f in family if f not in lower])[:3]
        alt_title = u['alt_lower'] if alts and len(lower) == len(alts) else u['alt_family']
        alt_html = ''.join(link_item(f, f"{u['gi']} {int(f['gi'])}" if f['gi_status'] == 'measured'
                                     else f"{round(f['kcal'])} {u['kcal_unit']}") for f in alts)
    else:
        if group in ('protein', 'dairy_solid'):
            key = lambda f: -(f['protein'] / f['kcal'] * 100 if f['kcal'] else 0)
            ranked = sorted(peers, key=key)
            v = fmt(food['protein'] / food['kcal'] * 100) if food['kcal'] else '0'
            tmpl = u['rank_protein']
        else:
            ranked = sorted(peers, key=lambda f: f['kcal'])
            v = str(kcal)
            tmpl = u['rank_kcal']
        rank = [f['id'] for f in ranked].index(food['id']) + 1
        compare_txt = tmpl.format(v=v, rank=rank, m=len(ranked), group=group_name, **g)
        alt_title = u['alt_same']
        alt_html = ''.join(link_item(f, f"{round(f['kcal'])} {u['kcal_unit']}") for f in family[:3])

    # -------- cards
    if measured:
        gi_card = (f'<div class="stat-num {["low", "medium", "high"][lvl]}">{gi}</div>'
                   f'<span class="badge {["low", "medium", "high"][lvl]}">{u["levels"][lvl]}</span>')
        gl_card = (f'<div class="stat-num {["low", "medium", "high"][glv]}">{fmt(gl)}</div>'
                   f'<div class="stat-sub">{u["per_portion"].format(p=portion)}</div>')
    else:
        gi_card = f'<div class="stat-num muted">—</div><span class="badge neutral">{u["na"]}</span>'
        gl_card = f'<div class="stat-num muted">—</div><span class="badge neutral">{u["na"]}</span>'

    # -------- nutrition table
    def row(label, v100, unit):
        return (f'<tr><td>{label}</td><td>{fmt(v100)} {unit}</td><td>{fmt(v100 * p_factor)} {unit}</td></tr>')
    rows = ''.join([
        row(u['rows'][0], food['kcal'], u['kcal_unit']), row(u['rows'][1], food['protein'], u['gram']),
        row(u['rows'][2], food['carbs'], u['gram']), row(u['rows'][3], food['avail'], u['gram']),
        row(u['rows'][4], food['fat'], u['gram']), row(u['rows'][5], food['fiber'], u['gram'])])
    if food['ii'] is not None:
        rows += f'<tr><td>{u["ii_row"]}</td><td colspan="2">{int(food["ii"])} · {u["ii_tested"]}</td></tr>'

    # -------- sources
    method_href = site_link('/methodology.html', lang)
    src = f'<div class="source-strip">{u["src_gi"]} <a href="{method_href}">{u["src_link"]}</a></div>'
    if measured:
        rng = food['gi_range'] or [food['gi'], food['gi']]
        src = (f'<div class="source-strip">{u["src_gi"]}<br>' +
               u['src_value'].format(studies=studies_word(int(food['gi_n'] or 1), lang), lo=int(rng[0]), hi=int(rng[-1]),
                                     grade=food['gi_grade'] or '-') +
               f' <a href="{method_href}">{u["src_link"]}</a></div>')
    if food['ii'] is not None:
        src += f'<div class="source-strip">{u["src_ii"]}</div>'

    # -------- head: SEO
    urls = {l: page_url(slug, l) for l in LANGS}
    image_abs = f'{SITE}/{food["image"]}' if food['image'] else f'{SITE}/images/logo.png'
    hreflang = '\n'.join(f'    <link rel="alternate" hreflang="{l}" href="{urls[l]}">' for l in LANGS)
    schema = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "@id": urls[lang] + '#webpage',
        "url": urls[lang],
        "name": title,
        "description": desc,
        "inLanguage": lang,
        "primaryImageOfPage": {"@type": "ImageObject", "url": image_abs},
        "about": {"@type": "Thing", "name": food['en'], "alternateName": [food['ar'], food['nl']]},
        "isPartOf": {"@type": "WebSite", "name": "WiBo Health", "url": SITE + '/'},
        "reviewedBy": {"@type": "Person", "@id": f"{SITE}/doctor.html#wassim-habib", "name": "Wassim Habib",
                       "url": f"{SITE}/doctor.html"},
        "lastReviewed": REVIEWED,
        "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u['home'], "item": SITE + site_link('/', lang)},
            {"@type": "ListItem", "position": 2, "name": u['guide'], "item": SITE + site_link('/foods.html', lang)},
            {"@type": "ListItem", "position": 3, "name": name, "item": urls[lang]}]},
    }

    nav_paths = ['/', '/foods.html', '/calculators.html', '/supplements.html', '/articles.html', '/boodi.html']
    nav = '\n'.join(f'                <a href="{site_link(p, lang)}" class="nav-link">{label}</a>'
                    for p, label in zip(nav_paths, u['nav']))
    lang_links = '\n'.join(
        f'                    <a class="lang-btn{" active" if l == lang else ""}" href="{page_url(slug, l, absolute=False)}" '
        f'hreflang="{l}" lang="{l}"><span>{flag}</span> <span>{l.upper()}</span></a>'
        for l, flag in (('ar', '🇪🇬'), ('nl', '🇳🇱'), ('en', '🇬🇧')))
    img_html = (f'<img src="/{food["image"]}" alt="{esc(name)}" width="350" height="350">' if food['image']
                else f'<div class="food-emoji" aria-hidden="true">{food["icon"] or "🍽️"}</div>')
    tip_icons = ('fa-check-circle', 'fa-utensils', 'fa-triangle-exclamation')
    tips_html = ''.join(
        f'<div class="tip{" warn" if i == 2 else ""}"><h3><i class="fas {tip_icons[i]}"></i> {u["tip_titles"][i]}</h3>'
        f'<p>{esc(tips[i])}</p></div>' for i in range(3))
    footer_links = ' <span>•</span> '.join(
        f'<a href="{site_link(p, lang)}">{label}</a>' for p, label in
        [('/', u['nav'][0]), ('/foods.html', u['nav'][1]), ('/methodology.html', u['methodology']),
         ('/doctor.html', 'Dr. Wassim Habib' if lang != 'ar' else 'د. وسيم حبيب'), ('/privacy.html', u['privacy'])])

    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{u["dir"]}" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(title)}</title>
    <meta name="description" content="{esc(desc)}">
    <link rel="canonical" href="{urls[lang]}">
{hreflang}
    <link rel="alternate" hreflang="x-default" href="{urls['ar']}">
    <meta property="og:type" content="article">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(desc)}">
    <meta property="og:url" content="{urls[lang]}">
    <meta property="og:image" content="{image_abs}">
    <meta property="og:locale" content="{dict(ar='ar_AR', en='en_US', nl='nl_NL')[lang]}">
    <script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=4)}
    </script>
    <script type="application/ld+json">
{json.dumps(faq_schema, ensure_ascii=False, indent=4)}
    </script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#0f172a">
    <link rel="icon" type="image/png" sizes="192x192" href="/images/icon-192.png">
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
    <script>
        try {{ document.documentElement.setAttribute('data-theme', localStorage.getItem('wibo_theme') || 'dark'); }} catch (e) {{}}
    </script>
    <style>
{BASE_CSS}{PAGE_CSS}    </style>
</head>
<body>
    <header>
        <div class="header-container">
            <a href="{site_link('/', lang)}" class="brand-link">
                {LOGO_SVG}
                <span class="brand-title">WiBo Health</span>
            </a>
            <nav class="nav-links-bar">
{nav}
            </nav>
            <div class="header-actions">
                <button type="button" class="theme-toggle-btn" onclick="toggleTheme()" title="{u["theme"]}" aria-label="{u["theme"]}">
                    <i class="fas fa-sun" id="themeIcon"></i>
                </button>
                <div class="lang-switcher-container">
{lang_links}
                </div>
            </div>
        </div>
    </header>

    <main class="page-wrapper food-page">
        <article class="about-card">
            <nav class="breadcrumb" aria-label="breadcrumb">
                <a href="{site_link('/', lang)}">{u["home"]}</a> › <a href="{site_link('/foods.html', lang)}">{u["guide"]}</a> › <span>{esc(name)}</span>
            </nav>

            <div class="food-hero">
                {img_html}
                <div class="food-hero-text">
                    <h1>{esc(name)}</h1>
                    {f'<div class="food-subtitle">{esc(subtitle)}</div>' if subtitle else ''}
                    <span class="group-chip">{group_name}</span>
                </div>
            </div>

            <p class="lead">{esc(lead)}</p>
            <p class="reviewed">{u["reviewed"].format(doctor=site_link('/doctor.html', lang), date=REVIEWED_TXT[lang])}</p>

            <section class="stat-grid" aria-label="{u["gi"]}">
                <div class="stat-box"><h2>{u["gi"]}</h2>{gi_card}</div>
                <div class="stat-box"><h2>{u["gl"]}</h2>{gl_card}</div>
                <div class="stat-box"><h2>{u["kcal"]}</h2><div class="stat-num kcal">{kcal}</div><div class="stat-sub">{u["kcal_unit"]} {u["per100"]}</div></div>
                <div class="stat-box"><h2>{u["protein"]}</h2><div class="stat-num protein">{protein}</div><div class="stat-sub">{u["gram"]} {u["per100"]}</div></div>
            </section>

            <h2 class="section-title"><span>{u["tips"]}</span></h2>
            <div class="tip-list">{tips_html}</div>

            <h2 class="section-title"><i class="fas fa-table-list"></i> <span>{u["table"]}</span></h2>
            <table class="nutrition-table">
                <thead><tr><th>{u["nutrient"]}</th><th>{u["col100"]}</th><th>{u["colp"].format(p=portion)}</th></tr></thead>
                <tbody>{rows}</tbody>
            </table>
            <p class="table-note">{u["portion_note"]}</p>

            <h2 class="section-title"><i class="fas fa-scale-balanced"></i> <span>{u["compare"]}</span></h2>
            <p>{esc(compare_txt)}</p>
            <p><strong>{alt_title}</strong></p>
            <ul class="alt-list">{alt_html}</ul>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>{FAQ[lang]["title"]}</span></h2>
            <section class="faq-list">{faq_html}</section>

            <aside class="boodi-card">
                <div>
                    <h2>{u["boodi_title"]}</h2>
                    <p>{u["boodi_text"]}</p>
                </div>
                <a class="boodi-btn" href="{site_link('/boodi.html', lang)}"><i class="fas fa-barcode"></i> {u["boodi_btn"]}</a>
            </aside>

            {src}
            <p class="disclaimer-box">{u["disclaimer"]}</p>
        </article>
    </main>

    <footer>
        <div class="footer-links">{footer_links}</div>
        <p>{u["footer_rights"]}</p>
    </footer>

    <script>
        function applyTheme(theme) {{
            document.documentElement.setAttribute('data-theme', theme);
            var icon = document.getElementById('themeIcon');
            if (icon) icon.className = theme === 'light' ? 'fas fa-moon' : 'fas fa-sun';
        }}
        function toggleTheme() {{
            var next = (document.documentElement.getAttribute('data-theme') || 'dark') === 'dark' ? 'light' : 'dark';
            applyTheme(next);
            try {{ localStorage.setItem('wibo_theme', next); }} catch (e) {{}}
        }}
        applyTheme(document.documentElement.getAttribute('data-theme') || 'dark');
        try {{ localStorage.setItem('preferred_language', '{lang}'); localStorage.setItem('wibo_language', '{lang}'); }} catch (e) {{}}
    </script>
</body>
</html>
'''


# --------------------------------------------------------------------------------------------
def main():
    foods = load_foods()
    overrides_path = ROOT / 'scripts' / 'food_pages_overrides.json'
    overrides = json.loads(overrides_path.read_text(encoding='utf-8')).get('foods', {}) if overrides_path.exists() else {}
    missing = [i for i in PILOT if i not in foods]
    assert not missing, f'unknown food ids: {missing}'
    slugs = {i: overrides.get(str(i), {}).get('slug') or SLUG_OVERRIDES.get(i) or slugify(foods[i]['en']) for i in PILOT}
    assert len(set(slugs.values())) == len(slugs), 'duplicate slugs'
    ctx = dict(foods=foods, slug=slugs, overrides=overrides)

    written = 0
    for fid in PILOT:
        for lang in LANGS:
            out = ROOT / (f'foods/{slugs[fid]}.html' if lang == 'ar' else f'{lang}/foods/{slugs[fid]}.html')
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(build(foods[fid], lang, ctx), encoding='utf-8', newline='\n')
            written += 1

    # id -> slug map for foods.html / food-details.html
    (ROOT / 'js' / 'food-pages.js').write_text(
        '// Generated by scripts/generate_food_pages.py - do not edit by hand.\n'
        '// Food id -> slug of its static page (/foods/<slug>.html, /en/foods/..., /nl/foods/...).\n'
        f'window.FOOD_PAGES = {json.dumps({str(k): v for k, v in sorted(slugs.items())}, separators=(",", ":"))};\n',
        encoding='utf-8', newline='\n')

    # sitemap block with hreflang alternates
    sm_path = ROOT / 'sitemap.xml'
    sm = sm_path.read_text(encoding='utf-8')
    eol = '\r\n' if '\r\n' in sm else '\n'
    if 'xmlns:xhtml' not in sm:
        sm = sm.replace('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
                        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">', 1)
    sm = re.sub(r'\s*<!-- FOOD-PAGES:START -->.*?<!-- FOOD-PAGES:END -->', '', sm, flags=re.S)
    block = ['  <!-- FOOD-PAGES:START -->']
    for fid in PILOT:
        for lang in LANGS:
            block += ['  <url>', f'    <loc>{page_url(slugs[fid], lang)}</loc>', f'    <lastmod>{REVIEWED}</lastmod>',
                      '    <changefreq>monthly</changefreq>', '    <priority>0.7</priority>']
            block += [f'    <xhtml:link rel="alternate" hreflang="{l}" href="{page_url(slugs[fid], l)}"/>' for l in LANGS]
            block += [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{page_url(slugs[fid], "ar")}"/>', '  </url>']
    block.append('  <!-- FOOD-PAGES:END -->')
    sm = sm.replace('</urlset>', eol.join(block) + eol + '</urlset>', 1)
    sm_path.write_text(sm, encoding='utf-8', newline='')

    print(f'pages written: {written} ({len(PILOT)} foods x {len(LANGS)} languages)')
    print('measured:', sum(1 for i in PILOT if foods[i]['gi_status'] == 'measured'),
          '| not applicable:', sum(1 for i in PILOT if foods[i]['gi_status'] == 'not_applicable'))


if __name__ == '__main__':
    main()
