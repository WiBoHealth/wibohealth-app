"""Nutrition and body tools (batch C, 2026-11-23): calorie deficit + goal date, protein + macros (with a GLP-1 option),
body fat (US Navy) + healthy weight range, meal glycemic load from our food database.
Arabic approved by Dr. Wassim Habib (drafts/batch_c_nutrition_tools_ar.md, decisions of 2026-11-23):
1 floor 1200 kcal women / 1500 men + a gentle note when the calories fall below BMR; 2 protein on the adjusted weight
when BMI >= 30 (weight at BMI 25 + 25% of the difference); 3 GLP-1 1.2-1.6 g/kg, no brand names, kidney note;
4 TDEE page aligned to 1.2-1.6 g/kg; 5 doctor advice below essential fat (men < 5%, women < 13%) with the tape's margin;
6 meal GL compared with the documented daily bands plus an approximate meal guide, stating there is no official meal
cut-off; 7 Gallagher 2000 bands by age and sex, ACE athlete ranges as extra information.
EN/NL/SV are translations of the Arabic. Formulas: js/calc-formulas.js (tested by scripts/test_calc_formulas.js).
"""
from calc_diabetes import SMALL, NEXT, _li
import generate_food_pages as _gfp
import food_sv as _fsv


def _card(lang, links, first=None):
    """'Next steps' card; `first` is a bold line shown before the links (doctor advice, kidney note)."""
    top = f'<p class="next-consult"><strong>{first}</strong></p>' if first else ''
    return f'<h3>{NEXT[lang]}</h3>{top}' + _li(links)


# ------------------------------------------------------------------ protein examples from our food database
_FOODS = _gfp.load_foods()
_EXAMPLES = ((91, 'grilled-chicken-breast'), (98, 'canned-tuna-in-water'), (18, 'lentils'), (101, 'boiled-egg'),
             (76, 'cottage-cheese'))


def _name(fid, lang):
    return _fsv.NAMES[fid][0] if lang == 'sv' else _FOODS[fid][lang]


def protein_examples(lang):
    head = {'ar': ('الطعام', 'الحصة', 'البروتين'), 'en': ('Food', 'Portion', 'Protein'),
            'nl': ('Product', 'Portie', 'Eiwit'), 'sv': ('Livsmedel', 'Portion', 'Protein')}[lang]
    rows = ''
    for fid, slug in _EXAMPLES:
        grams = _gfp.PILOT[fid][1]
        p = _FOODS[fid]['protein'] * grams / 100
        rows += (f'<tr><td><a href="{{food:{slug}}}">{_name(fid, lang)}</a></td><td>{grams} g</td>'
                 f'<td>{round(p)} g</td></tr>')
    return ('<div class="table-scroll"><table class="nutrition-table"><thead><tr>' + ''.join(f'<th>{h}</th>' for h in head) +
            f'</tr></thead><tbody>{rows}</tbody></table></div>')


# ======================================================================================================== deficit
DEFICIT = {
    'key': 'deficit', 'slug': 'calorie-deficit-calculator', 'icon': 'fa-bullseye', 'badge': 'Mifflin-St Jeor · NIH', 'category': 'body',
    'published': '2026-11-23', 'modified': '2026-11-23',
    'references': [
        'Mifflin MD, St Jeor ST, Hill LA, et al. A new predictive equation for resting energy expenditure in healthy individuals. Am J Clin Nutr 1990;51:241-247.',
        'Hall KD, Sacks G, Chandramohan D, et al. Quantification of the effect of energy imbalance on bodyweight. Lancet 2011;378:826-837.',
        'Jensen MD, et al. 2013 AHA/ACC/TOS Guideline for the management of overweight and obesity in adults (500-750 kcal/day deficit; 1200-1500 kcal/day women, 1500-1800 kcal/day men). Circulation 2014;129:S102-S138.',
        'NHS. Losing weight: a safe rate of weight loss of 0.5 to 1 kg a week.',
    ],
    'content': {
        'ar': dict(
            title='حاسبة السعرات لإنقاص الوزن: متى تصل لوزنك المستهدف؟',
            desc='احسب كم سعرة تحتاج يومياً لتخسر وزنك بأمان، وفي أي تاريخ تقريباً ستصل للوزن الذي تريده، مع حد أدنى آمن للسعرات وسرعة نزول مناسبة.',
            h1='حاسبة عجز السعرات وتاريخ الوصول للوزن المستهدف', crumb='حاسبة عجز السعرات', cat='التغذية والجسم',
            short='حاسبة عجز السعرات', blurb='سعراتك لإنقاص الوزن وتاريخ الوصول لهدفك.',
            about=[{'name': 'عجز السعرات'}, {'name': 'إنقاص الوزن'}, {'name': 'السمنة', 'condition': True}],
            lead='لتخسر الوزن يحتاج جسمك أن يأخذ سعرات أقل مما يصرف، وهذا الفرق اسمه «عجز السعرات». اكتب وزنك الحالي والوزن الذي تريده، واختر سرعة النزول، لتعرف كم سعرة تأكل يومياً، وفي أي تاريخ تقريباً ستصل لهدفك.',
            ui=dict(card_title='احسب سعراتك وتاريخ الوصول', lbl_sex='الجنس', male='ذكر', female='أنثى', lbl_age='العمر (سنوات)',
                    lbl_height='الطول (سم)', lbl_weight='الوزن الحالي (كغ)', lbl_target='الوزن المستهدف (كغ)',
                    lbl_activity='مستوى النشاط البدني', lbl_pace='سرعة النزول',
                    paces=['هادئة: 0.25 كغ في الأسبوع', 'معتدلة: 0.5 كغ في الأسبوع (مقترحة)', 'أسرع: 0.75 كغ في الأسبوع'],
                    ph_age='مثال: 40', ph_height='مثال: 165', ph_weight='مثال: 85', ph_target='مثال: 72',
                    btn='احسب', res_heading='سعراتك اليومية المقترحة للنزول', kcal_day='سعرة حرارية يومياً',
                    tdee_label='احتياجك الحالي للحفاظ على وزنك', date_label='التاريخ التقريبي للوصول', lose_label='الوزن الذي ستخسره',
                    weeks_txt='بعد نحو {n} أسبوعاً', kg='كغ',
                    st_plan='خطة تقريبية', st_warn='انتبه للتنبيه أدناه',
                    tip_base='تاريخ تقريبي: نعيد حساب احتياجك كل 5 كغ لأن الجسم الأخف يصرف سعرات أقل. راقب وزنك أسبوعين ثم عدّل السعرات بمقدار 100 إلى 200 سعرة حسب النتيجة.',
                    tip_floor='هذه السعرات منخفضة جداً. اختر سرعة أهدأ، أو زِد حركتك بدل تقليل الأكل أكثر. نعرض لك الحد الأدنى ({floor} سعرة)، ولذلك يصبح النزول أبطأ.',
                    tip_bmr='سعراتك المقترحة أقل من معدل الأيض الأساسي لجسمك ({bmr} سعرة). هذا شائع مع الأوزان الكبيرة، لكن احرص على بروتين كافٍ وأكل متنوع، ولا تنزل أكثر من ذلك.',
                    tip_fast='هذه السرعة عالية لوزنك، والسرعة الأهدأ تحافظ على العضلات أكثر.',
                    tip_lowtarget='هذا الوزن أقل من الطبيعي لطولك. الوزن الصحي لطولك بين {lo} و{hi} كغ.',
                    tip_stall='بهذه السعرات لن تصل لهدفك تقريباً، لأن احتياجك ينخفض مع نزول الوزن. زِد حركتك أو راجع هدفك.',
                    tip_invalid='اكتب وزناً مستهدفاً أقل من وزنك الحالي.',
                    nx_plan=_card('ar', ['اعرف كم بروتين تحتاج أثناء النزول: <a href="{calc:protein}">حاسبة البروتين اليومي</a>.',
                                         'اختر أطعمة مشبعة منخفضة المؤشر الجلايسيمي من <a href="{site:/foods/index.html}">دليل الأطعمة</a>.',
                                         'قِس <a href="{calc:whtr}">نسبة الخصر إلى الطول</a> كل شهر، فهي تتحسن حتى لو تباطأ الميزان.'])),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>كيف تحسب الأداة؟</span></h2>
            <p>نحسب احتياجك اليومي بمعادلة Mifflin-St Jeor مضروبة في مستوى نشاطك، ثم نطرح العجز المناسب لسرعة النزول التي اخترتها: نصف كيلو في الأسبوع يعني نحو 550 سعرة أقل كل يوم. لا ننزل أبداً عن 1200 سعرة للنساء و1500 سعرة للرجال.</p>
            <h2 class="section-title"><i class="fas fa-chart-line"></i> <span>لماذا يتباطأ النزول مع الوقت؟</span></h2>
            <p>كلما نقص وزنك قلّ ما يصرفه جسمك، لذلك نعيد الحساب كل 5 كغ، ونحسب التاريخ أسبوعاً بأسبوع. ومن الطبيعي أن يثبت الميزان أياماً بسبب الماء.</p>
            <h2 class="section-title"><i class="fas fa-gauge"></i> <span>ما السرعة المناسبة؟</span></h2>
            <p>نصف كيلو أسبوعياً تقريباً سرعة مناسبة لأغلب الناس، وتحافظ على العضلات أكثر من الأنظمة القاسية. وإذا كانت السرعة أكثر من 1% من وزنك في الأسبوع ننبهك لذلك.</p>
            <h2 class="section-title"><i class="fas fa-ruler"></i> <span>لا تعتمد على الميزان وحده</span></h2>
            <p>محيط الخصر والطاقة والنوم مؤشرات مهمة أيضاً. قِس خصرك مرة في الشهر بـ<a href="{calc:whtr}">حاسبة نسبة الخصر إلى الطول</a>.</p>
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>لمن لا تصلح الحاسبة؟</span></h2>
            <p>للحامل والمرضع، ولمن عمره أقل من 18 سنة، ولمن لديه اضطراب في الأكل أو تاريخ معه.</p>''',
            faq=[('كم سعرة أنقص لأخسر نصف كيلو في الأسبوع؟', 'حوالي 500 إلى 550 سعرة يومياً أقل من احتياجك.'),
                 ('لماذا لا ينزل وزني رغم العجز؟', 'احتباس الماء، أو تقدير السعرات أقل من الحقيقة، أو انخفاض الحركة اليومية دون أن تشعر.'),
                 ('هل أقل من 1200 سعرة أسرع؟', 'قد يكون أسرع في البداية، لكنه يُصعّب الحصول على البروتين والفيتامينات ويزيد خسارة العضلات، ولا يُنصح به دون إشراف طبي.')],
            disclaimer=SMALL['ar']),
        'en': dict(
            title='Calorie Deficit Calculator: When Will You Reach Your Goal?',
            desc='Work out how many calories a day you need to lose weight safely and roughly when you will reach your goal weight, with a safe calorie minimum and a sensible pace.',
            h1='Calorie deficit calculator and goal weight date', crumb='Calorie deficit calculator', cat='Nutrition and body',
            short='Calorie deficit calculator', blurb='Your weight-loss calories and the date you reach your goal.',
            about=[{'name': 'Calorie deficit'}, {'name': 'Weight loss'}, {'name': 'Obesity', 'condition': True}],
            lead='To lose weight your body needs to take in fewer calories than it uses; that difference is called a "calorie deficit". Enter your current weight and the weight you want, choose a pace, and see how many calories to eat each day and roughly when you will reach your goal.',
            ui=dict(card_title='Calculate your calories and goal date', lbl_sex='Sex', male='Male', female='Female', lbl_age='Age (years)',
                    lbl_height='Height (cm)', lbl_weight='Current weight (kg)', lbl_target='Goal weight (kg)',
                    lbl_activity='Physical activity level', lbl_pace='Pace',
                    paces=['Gentle: 0.25 kg a week', 'Moderate: 0.5 kg a week (suggested)', 'Faster: 0.75 kg a week'],
                    ph_age='e.g. 40', ph_height='e.g. 165', ph_weight='e.g. 85', ph_target='e.g. 72',
                    btn='Calculate', res_heading='Your suggested daily calories for weight loss', kcal_day='calories a day',
                    tdee_label='What you need now to keep your weight', date_label='Approximate goal date', lose_label='Weight to lose',
                    weeks_txt='in about {n} weeks', kg='kg',
                    st_plan='Approximate plan', st_warn='Please read the note below',
                    tip_base='An approximate date: we recalculate your needs every 5 kg because a lighter body uses fewer calories. Watch your weight for two weeks, then adjust your calories by 100 to 200 depending on the result.',
                    tip_floor='These calories are very low. Choose a gentler pace, or move more instead of eating even less. We show you the minimum ({floor} kcal), so weight loss will be slower.',
                    tip_bmr='Your suggested calories are below your basal metabolic rate ({bmr} kcal). This is common at higher body weights, but make sure you get enough protein and varied food, and do not go any lower.',
                    tip_fast='This pace is high for your weight; a gentler pace protects more muscle.',
                    tip_lowtarget='This weight is below the healthy range for your height. A healthy weight for your height is between {lo} and {hi} kg.',
                    tip_stall='With these calories you will hardly reach your goal, because your needs drop as you lose weight. Move more or review your goal.',
                    tip_invalid='Enter a goal weight below your current weight.',
                    nx_plan=_card('en', ['See how much protein you need while losing weight: <a href="{calc:protein}">daily protein calculator</a>.',
                                         'Choose filling, low glycemic index foods in the <a href="{site:/foods/index.html}">food guide</a>.',
                                         'Measure your <a href="{calc:whtr}">waist-to-height ratio</a> every month; it improves even when the scale slows down.'])),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>How does the tool calculate?</span></h2>
            <p>We estimate your daily needs with the Mifflin-St Jeor equation multiplied by your activity level, then subtract the deficit that matches the pace you chose: half a kilo a week means about 550 calories less each day. We never go below 1,200 calories for women and 1,500 calories for men.</p>
            <h2 class="section-title"><i class="fas fa-chart-line"></i> <span>Why does weight loss slow down over time?</span></h2>
            <p>The less you weigh, the fewer calories your body uses, so we recalculate every 5 kg and work out the date week by week. It is also normal for the scale to stand still for a few days because of water.</p>
            <h2 class="section-title"><i class="fas fa-gauge"></i> <span>What is a good pace?</span></h2>
            <p>About half a kilo a week suits most people and protects more muscle than harsh diets. If the pace is more than 1% of your body weight a week, we point that out.</p>
            <h2 class="section-title"><i class="fas fa-ruler"></i> <span>Do not rely on the scale alone</span></h2>
            <p>Waist size, energy and sleep matter too. Measure your waist once a month with the <a href="{calc:whtr}">waist-to-height ratio calculator</a>.</p>
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Who should not use this calculator?</span></h2>
            <p>People who are pregnant or breastfeeding, anyone under 18, and anyone with an eating disorder now or in the past.</p>''',
            faq=[('How many calories should I cut to lose half a kilo a week?', 'About 500 to 550 calories a day below what you need.'),
                 ('Why is my weight not going down despite a deficit?', 'Water retention, underestimating calories, or moving less during the day without noticing.'),
                 ('Is eating under 1,200 calories faster?', 'It may be faster at first, but it makes it hard to get enough protein and vitamins and increases muscle loss; it is not advised without medical supervision.')],
            disclaimer=SMALL['en']),
        'nl': dict(
            title='Calorietekort berekenen: wanneer bereik je je streefgewicht?',
            desc='Bereken hoeveel calorieën per dag je nodig hebt om veilig af te vallen en ongeveer wanneer je je streefgewicht bereikt, met een veilig minimum en een passend tempo.',
            h1='Calorietekort en datum van je streefgewicht berekenen', crumb='Calorietekort berekenen', cat='Voeding en lichaam',
            short='Calorietekort berekenen', blurb='Je calorieën om af te vallen en de datum van je doel.',
            about=[{'name': 'Calorietekort'}, {'name': 'Afvallen'}, {'name': 'Obesitas', 'condition': True}],
            lead='Om af te vallen moet je lichaam minder calorieën binnenkrijgen dan het verbruikt; dat verschil heet een "calorietekort". Vul je huidige gewicht en je streefgewicht in, kies een tempo en zie hoeveel calorieën je per dag eet en ongeveer wanneer je je doel bereikt.',
            ui=dict(card_title='Bereken je calorieën en streefdatum', lbl_sex='Geslacht', male='Man', female='Vrouw', lbl_age='Leeftijd (jaren)',
                    lbl_height='Lengte (cm)', lbl_weight='Huidig gewicht (kg)', lbl_target='Streefgewicht (kg)',
                    lbl_activity='Lichamelijk activiteitsniveau', lbl_pace='Tempo',
                    paces=['Rustig: 0,25 kg per week', 'Gematigd: 0,5 kg per week (aanbevolen)', 'Sneller: 0,75 kg per week'],
                    ph_age='bijv. 40', ph_height='bijv. 165', ph_weight='bijv. 85', ph_target='bijv. 72',
                    btn='Bereken', res_heading='Je aanbevolen calorieën per dag om af te vallen', kcal_day='kcal per dag',
                    tdee_label='Wat je nu nodig hebt om op gewicht te blijven', date_label='Geschatte streefdatum', lose_label='Gewicht om te verliezen',
                    weeks_txt='over ongeveer {n} weken', kg='kg',
                    st_plan='Geschat plan', st_warn='Lees de opmerking hieronder',
                    tip_base='Een geschatte datum: we berekenen je behoefte elke 5 kg opnieuw, omdat een lichter lichaam minder verbruikt. Volg je gewicht twee weken en pas je calorieën dan met 100 tot 200 aan.',
                    tip_floor='Deze calorieën zijn erg laag. Kies een rustiger tempo of beweeg meer in plaats van nog minder te eten. We tonen het minimum ({floor} kcal), waardoor je langzamer afvalt.',
                    tip_bmr='Je aanbevolen calorieën liggen onder je basaal metabolisme ({bmr} kcal). Dat komt vaak voor bij een hoger gewicht, maar zorg voor genoeg eiwit en gevarieerd eten en ga niet lager.',
                    tip_fast='Dit tempo is hoog voor je gewicht; een rustiger tempo beschermt je spieren beter.',
                    tip_lowtarget='Dit gewicht is lager dan gezond voor je lengte. Een gezond gewicht voor jouw lengte ligt tussen {lo} en {hi} kg.',
                    tip_stall='Met deze calorieën bereik je je doel bijna niet, omdat je behoefte daalt naarmate je afvalt. Beweeg meer of bekijk je doel opnieuw.',
                    tip_invalid='Vul een streefgewicht in dat lager is dan je huidige gewicht.',
                    nx_plan=_card('nl', ['Bekijk hoeveel eiwit je nodig hebt tijdens het afvallen: <a href="{calc:protein}">eiwitcalculator</a>.',
                                         'Kies verzadigende producten met een lage glykemische index in de <a href="{site:/foods/index.html}">voedingswijzer</a>.',
                                         'Meet elke maand je <a href="{calc:whtr}">taille-lengteverhouding</a>; die verbetert ook als de weegschaal vertraagt.'])),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Hoe rekent de tool?</span></h2>
            <p>We schatten je dagelijkse behoefte met de formule van Mifflin-St Jeor, vermenigvuldigd met je activiteitsniveau, en trekken daar het tekort van af dat past bij het gekozen tempo: een halve kilo per week betekent ongeveer 550 kcal minder per dag. We gaan nooit onder 1200 kcal voor vrouwen en 1500 kcal voor mannen.</p>
            <h2 class="section-title"><i class="fas fa-chart-line"></i> <span>Waarom gaat afvallen na verloop van tijd langzamer?</span></h2>
            <p>Hoe minder je weegt, hoe minder je lichaam verbruikt. Daarom rekenen we elke 5 kg opnieuw en bepalen we de datum week voor week. Het is ook normaal dat de weegschaal een paar dagen stilstaat door vocht.</p>
            <h2 class="section-title"><i class="fas fa-gauge"></i> <span>Wat is een goed tempo?</span></h2>
            <p>Ongeveer een halve kilo per week past bij de meeste mensen en beschermt je spieren beter dan strenge diëten. Is het tempo meer dan 1% van je lichaamsgewicht per week, dan wijzen we je daarop.</p>
            <h2 class="section-title"><i class="fas fa-ruler"></i> <span>Vertrouw niet alleen op de weegschaal</span></h2>
            <p>Je buikomvang, energie en slaap zijn ook belangrijk. Meet je buik één keer per maand met de <a href="{calc:whtr}">taille-lengteverhouding-calculator</a>.</p>
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Voor wie is de calculator niet geschikt?</span></h2>
            <p>Voor zwangere vrouwen en vrouwen die borstvoeding geven, voor mensen jonger dan 18 en voor mensen met een eetstoornis, nu of in het verleden.</p>''',
            faq=[('Hoeveel calorieën moet ik minder eten om een halve kilo per week af te vallen?', 'Ongeveer 500 tot 550 kcal per dag minder dan je nodig hebt.'),
                 ('Waarom val ik niet af ondanks een tekort?', 'Vochtvasthouden, calorieën te laag inschatten of overdag minder bewegen zonder het te merken.'),
                 ('Is minder dan 1200 kcal sneller?', 'In het begin misschien wel, maar het maakt het moeilijk om genoeg eiwit en vitamines binnen te krijgen en je verliest meer spieren; het wordt zonder medische begeleiding afgeraden.')],
            disclaimer=SMALL['nl']),
        'sv': dict(
            title='Kaloriunderskott: räkna ut när du når din målvikt',
            desc='Räkna ut hur många kalorier per dag du behöver för att gå ner i vikt på ett säkert sätt och ungefär när du når din målvikt, med en säker miniminivå och lagom takt.',
            h1='Räkna ut kaloriunderskott och datum för din målvikt', crumb='Kaloriunderskott', cat='Kost och kropp',
            short='Räkna ut kaloriunderskott', blurb='Dina kalorier för viktnedgång och datum för ditt mål.',
            about=[{'name': 'Kaloriunderskott'}, {'name': 'Viktnedgång'}, {'name': 'Fetma', 'condition': True}],
            lead='För att gå ner i vikt behöver kroppen få i sig färre kalorier än den förbrukar; skillnaden kallas "kaloriunderskott". Skriv in din nuvarande vikt och den vikt du vill nå, välj takt och se hur många kalorier du ska äta per dag och ungefär när du når ditt mål.',
            ui=dict(card_title='Räkna ut kalorier och måldatum', lbl_sex='Kön', male='Man', female='Kvinna', lbl_age='Ålder (år)',
                    lbl_height='Längd (cm)', lbl_weight='Nuvarande vikt (kg)', lbl_target='Målvikt (kg)',
                    lbl_activity='Fysisk aktivitetsnivå', lbl_pace='Takt',
                    paces=['Lugn: 0,25 kg per vecka', 'Måttlig: 0,5 kg per vecka (rekommenderas)', 'Snabbare: 0,75 kg per vecka'],
                    ph_age='t.ex. 40', ph_height='t.ex. 165', ph_weight='t.ex. 85', ph_target='t.ex. 72',
                    btn='Beräkna', res_heading='Dina föreslagna kalorier per dag för viktnedgång', kcal_day='kcal per dag',
                    tdee_label='Det du behöver nu för att behålla vikten', date_label='Ungefärligt måldatum', lose_label='Vikt att gå ner',
                    weeks_txt='om ungefär {n} veckor', kg='kg',
                    st_plan='Ungefärlig plan', st_warn='Läs informationen nedan',
                    tip_base='Ett ungefärligt datum: vi räknar om ditt behov var femte kilo eftersom en lättare kropp förbrukar mindre. Följ vikten i två veckor och justera sedan kalorierna med 100 till 200 beroende på resultatet.',
                    tip_floor='De här kalorierna är mycket låga. Välj en lugnare takt eller rör dig mer i stället för att äta ännu mindre. Vi visar miniminivån ({floor} kcal), så viktnedgången går långsammare.',
                    tip_bmr='Dina föreslagna kalorier ligger under din basalmetabolism ({bmr} kcal). Det är vanligt vid högre kroppsvikt, men se till att få tillräckligt med protein och varierad mat, och gå inte lägre.',
                    tip_fast='Den här takten är hög för din vikt; en lugnare takt skyddar musklerna bättre.',
                    tip_lowtarget='Den här vikten är lägre än normalt för din längd. En hälsosam vikt för din längd ligger mellan {lo} och {hi} kg.',
                    tip_stall='Med de här kalorierna når du knappt ditt mål, eftersom ditt behov minskar när du går ner i vikt. Rör dig mer eller se över ditt mål.',
                    tip_invalid='Skriv in en målvikt som är lägre än din nuvarande vikt.',
                    nx_plan=_card('sv', ['Se hur mycket protein du behöver under viktnedgången: <a href="{calc:protein}">proteinkalkylator</a>.',
                                         'Välj mättande livsmedel med lågt glykemiskt index i <a href="{site:/foods/index.html}">livsmedelsguiden</a>.',
                                         'Mät din <a href="{calc:whtr}">midja-längd-kvot</a> varje månad; den förbättras även när vågen går långsammare.'])),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Hur räknar verktyget?</span></h2>
            <p>Vi uppskattar ditt dagliga behov med Mifflin-St Jeors ekvation multiplicerad med din aktivitetsnivå och drar sedan av det underskott som motsvarar den takt du valt: ett halvt kilo i veckan betyder ungefär 550 kcal mindre per dag. Vi går aldrig under 1 200 kcal för kvinnor och 1 500 kcal för män.</p>
            <h2 class="section-title"><i class="fas fa-chart-line"></i> <span>Varför går viktnedgången långsammare med tiden?</span></h2>
            <p>Ju mindre du väger, desto mindre förbrukar kroppen. Därför räknar vi om var femte kilo och räknar ut datumet vecka för vecka. Det är också normalt att vågen står still några dagar på grund av vätska.</p>
            <h2 class="section-title"><i class="fas fa-gauge"></i> <span>Vilken takt är lagom?</span></h2>
            <p>Ungefär ett halvt kilo i veckan passar de flesta och skyddar musklerna bättre än hårda dieter. Om takten är mer än 1 % av kroppsvikten per vecka påpekar vi det.</p>
            <h2 class="section-title"><i class="fas fa-ruler"></i> <span>Lita inte bara på vågen</span></h2>
            <p>Midjemått, energi och sömn är också viktiga. Mät midjan en gång i månaden med <a href="{calc:whtr}">kalkylatorn för midja-längd-kvot</a>.</p>
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Vem passar kalkylatorn inte för?</span></h2>
            <p>Den passar inte vid graviditet eller amning, för personer under 18 år eller för den som har eller har haft en ätstörning.</p>''',
            faq=[('Hur många kalorier ska jag dra ner för att gå ner ett halvt kilo i veckan?', 'Ungefär 500 till 550 kcal per dag under ditt behov.'),
                 ('Varför går jag inte ner trots underskott?', 'Vätska i kroppen, att man underskattar kalorierna eller att man rör sig mindre under dagen utan att märka det.'),
                 ('Går det snabbare att äta under 1 200 kcal?', 'Kanske i början, men det gör det svårt att få i sig tillräckligt med protein och vitaminer och ökar muskelförlusten; det avråds utan medicinsk uppföljning.')],
            disclaimer=SMALL['sv']),
    },
}

# ======================================================================================================== protein
_KIDNEY = {'ar': 'إذا كان لديك مرض في الكلى فلا تزد البروتين قبل مراجعة طبيبك.',
           'en': 'If you have kidney disease, do not increase your protein before talking to your doctor.',
           'nl': 'Heb je een nierziekte, verhoog je eiwit dan niet voordat je met je arts hebt overlegd.',
           'sv': 'Om du har en njursjukdom ska du inte öka proteinet innan du har pratat med din läkare.'}

PROTEIN = {
    'key': 'protein', 'slug': 'protein-calculator', 'icon': 'fa-drumstick-bite', 'badge': 'EFSA · PROT-AGE', 'category': 'body',
    'published': '2026-11-23', 'modified': '2026-11-23',
    'references': [
        'EFSA Panel on Dietetic Products, Nutrition and Allergies. Scientific Opinion on Dietary Reference Values for protein. EFSA J 2012;10(2):2557.',
        'Bauer J, Biolo G, Cederholm T, et al. Evidence-based recommendations for optimal dietary protein intake in older people: a position paper from the PROT-AGE Study Group. J Am Med Dir Assoc 2013;14:542-559.',
        'Morton RW, Murphy KT, McKellar SR, et al. A systematic review, meta-analysis and meta-regression of the effect of protein supplementation on resistance training-induced gains in muscle mass and strength in healthy adults. Br J Sports Med 2018;52:376-384.',
        'Mozaffarian D, Agarwal M, Aggarwal M, et al. Nutritional priorities to support GLP-1 therapy for obesity: a joint advisory from the ACLM, ASN, OMA and TOS. Am J Clin Nutr 2025.',
        'EFSA Panel on Dietetic Products, Nutrition and Allergies. Scientific Opinion on Dietary Reference Values for fats and for carbohydrates and dietary fibre. EFSA J 2010;8(3):1461-1462.',
    ],
    'content': {
        'ar': dict(
            title='حاسبة البروتين اليومي: كم غرام بروتين تحتاج؟',
            desc='احسب كم غرام بروتين تحتاج يومياً حسب وزنك وعمرك وهدفك، مع توزيع الماكروز، وخيار خاص لمن يستخدم أدوية GLP-1 لإنقاص الوزن.',
            h1='حاسبة البروتين اليومي وتوزيع الماكروز', crumb='حاسبة البروتين اليومي', cat='التغذية والجسم',
            short='حاسبة البروتين اليومي', blurb='كم غرام بروتين تحتاج حسب هدفك.',
            about=[{'name': 'البروتين'}, {'name': 'الماكروز'}, {'name': 'السمنة', 'condition': True}],
            lead='البروتين يحمي عضلاتك ويُشعرك بالشبع، وتزيد حاجتك له مع العمر، وأثناء إنقاص الوزن، ومع التمارين. اختر هدفك لتعرف كم غراماً تحتاج يومياً، وكيف توزعه على وجباتك.',
            ui=dict(card_title='احسب بروتينك اليومي', lbl_sex='الجنس', male='ذكر', female='أنثى', lbl_age='العمر (سنوات)',
                    lbl_height='الطول (سم)', lbl_weight='الوزن (كغ)', lbl_goal='هدفك',
                    goals=['صحة عامة', 'إنقاص الوزن', 'بناء العضلات (تمارين مقاومة)', 'أستخدم دواء GLP-1 لإنقاص الوزن'],
                    lbl_activity='مستوى النشاط البدني', lbl_kcal='سعراتك اليومية (اختياري)', ph_kcal='اتركها فارغة لنحسبها',
                    ph_age='مثال: 40', ph_height='مثال: 170', ph_weight='مثال: 80',
                    btn='احسب', res_heading='بروتينك اليومي', perkg='{v} غ لكل كغ', meal_label='في كل وجبة (3 وجبات)',
                    basis_label='الوزن المستخدم في الحساب', basis_actual='وزنك الحالي', basis_adj='الوزن المعدّل',
                    macros_header='الماكروز على سعراتك', kcal_label='السعرات', fat_label='الدهون (30%)', carbs_label='الكربوهيدرات (الباقي)',
                    st_ok='تقدير يومي',
                    tip_general='للبالغ السليم يكفي حوالي 0.83 غرام لكل كيلو يومياً.',
                    tip_general65='بعد سن 65 تزيد الحاجة إلى 1.0 إلى 1.2 غرام لكل كيلو للحفاظ على العضلات.',
                    tip_loss='أثناء إنقاص الوزن يساعد 1.2 إلى 1.6 غرام لكل كيلو على حماية العضلات والشعور بالشبع.',
                    tip_muscle='مع تمارين المقاومة تستقر الفائدة عند نحو 1.6 غرام لكل كيلو، والحد الأعلى المفيد نحو 2.2.',
                    tip_glp1='أدوية GLP-1 تقلل الشهية كثيراً، لذلك يسهل أن ينقص البروتين وتُفقد العضلات مع الدهون. حاول أن تبدأ كل وجبة بالبروتين، وأن تقسم الأكل لوجبات صغيرة، وتشرب ماء كافياً، وتمارس تمارين المقاومة مرتين إلى ثلاث أسبوعياً. إذا صعب عليك الأكل أو ظهرت أعراض مزعجة فتحدث مع طبيبك.',
                    tip_adj='مؤشر كتلة جسمك 30 أو أكثر، لذلك حسبنا على «الوزن المعدّل» ({w} كغ) حتى لا تخرج كمية مبالغ فيها.',
                    nx_ok=_card('ar', ['احسب سعراتك وتاريخ الوصول لهدفك: <a href="{calc:deficit}">حاسبة عجز السعرات</a>.',
                                       'ابحث عن أطعمة غنية بالبروتين في <a href="{site:/foods/index.html}">دليل الأطعمة</a>.'], first=_KIDNEY['ar'])),
            body='''
            <h2 class="section-title"><i class="fas fa-table"></i> <span>كم بروتين حسب هدفك؟</span></h2>
            <div class="table-scroll"><table class="nutrition-table"><thead><tr><th>الهدف</th><th>غرام لكل كغ يومياً</th></tr></thead><tbody>
            <tr><td>صحة عامة (18 إلى 64 سنة)</td><td>0.83</td></tr><tr><td>صحة عامة (65 سنة فأكثر)</td><td>1.0 إلى 1.2</td></tr>
            <tr><td>إنقاص الوزن</td><td>1.2 إلى 1.6</td></tr><tr><td>بناء العضلات</td><td>1.6 (حتى 2.2)</td></tr>
            <tr><td>أدوية GLP-1</td><td>1.2 إلى 1.6</td></tr></tbody></table></div>
            <h2 class="section-title"><i class="fas fa-weight-scale"></i> <span>ما هو «الوزن المعدّل»؟</span></h2>
            <p>إذا كان مؤشر كتلة الجسم 30 أو أكثر، فالحساب على الوزن الكامل يعطي كمية مبالغ فيها، لأن الدهون لا تحتاج بروتيناً مثل العضلات. لذلك نأخذ الوزن المقابل لمؤشر 25 لطولك، ونضيف إليه ربع الفرق بينه وبين وزنك الحالي.</p>
            <h2 class="section-title"><i class="fas fa-chart-pie"></i> <span>كيف نوزع الماكروز؟</span></h2>
            <p>البروتين حسب هدفك، والدهون 30% من السعرات (ضمن النطاق الأوروبي 20 إلى 35%)، والكربوهيدرات الباقي. إذا لم تكتب سعراتك نحسبها: احتياجك اليومي للصحة العامة وبناء العضلات، واحتياجك ناقص 550 سعرة لإنقاص الوزن وأدوية GLP-1 (دون النزول عن 1200 للنساء و1500 للرجال).</p>
            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>كم بروتين في أطعمة شائعة؟</span></h2>
            <p>الأرقام من دليل الأطعمة لدينا، للحصة المعتادة:</p>
            {EXAMPLES}
            <p>وزّع البروتين على وجباتك: 25 إلى 40 غراماً في كل وجبة رئيسية أفضل من كمية كبيرة في وجبة واحدة.</p>
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>لمن لا تصلح الحاسبة؟</span></h2>
            <p>للحامل والمرضع (الاحتياج مختلف)، ولمرضى الكلى المزمنة، ولمن عمره أقل من 18 سنة.</p>''',
            faq=[('كم غرام بروتين أحتاج يومياً؟', 'للبالغ السليم حوالي 0.8 غرام لكل كيلو، وتزيد مع العمر والتمارين وإنقاص الوزن.'),
                 ('هل البروتين الكثير يضر الكلى؟', 'عند الأصحاء لا تُظهر الدراسات ضرراً بالكميات المعتادة، أما مرضى الكلى فيحتاجون كمية يحددها الطبيب.'),
                 ('لماذا يحتاج مستخدمو أدوية GLP-1 بروتيناً أكثر؟', 'لأن الأكل يقل كثيراً، والبروتين الكافي مع تمارين المقاومة يساعد على حماية العضلات.')],
            disclaimer=SMALL['ar']),
        'en': dict(
            title='Protein Calculator: How Much Protein Do You Need a Day?',
            desc='Work out how many grams of protein you need a day for your weight, age and goal, with a macro split and a special option for people taking GLP-1 medicines for weight loss.',
            h1='Daily protein and macro calculator', crumb='Protein calculator', cat='Nutrition and body',
            short='Protein calculator', blurb='How many grams of protein you need for your goal.',
            about=[{'name': 'Protein'}, {'name': 'Macronutrients'}, {'name': 'Obesity', 'condition': True}],
            lead='Protein protects your muscles and keeps you full, and you need more of it as you get older, while losing weight and when you train. Choose your goal to see how many grams you need each day and how to spread them over your meals.',
            ui=dict(card_title='Calculate your daily protein', lbl_sex='Sex', male='Male', female='Female', lbl_age='Age (years)',
                    lbl_height='Height (cm)', lbl_weight='Weight (kg)', lbl_goal='Your goal',
                    goals=['General health', 'Weight loss', 'Building muscle (resistance training)', 'I take a GLP-1 medicine for weight loss'],
                    lbl_activity='Physical activity level', lbl_kcal='Your daily calories (optional)', ph_kcal='leave empty and we calculate it',
                    ph_age='e.g. 40', ph_height='e.g. 170', ph_weight='e.g. 80',
                    btn='Calculate', res_heading='Your daily protein', perkg='{v} g per kg', meal_label='Per meal (3 meals)',
                    basis_label='Weight used in the calculation', basis_actual='your current weight', basis_adj='adjusted weight',
                    macros_header='Macros on your calories', kcal_label='Calories', fat_label='Fat (30%)', carbs_label='Carbohydrates (the rest)',
                    st_ok='Daily estimate',
                    tip_general='For a healthy adult, about 0.83 g per kg a day is enough.',
                    tip_general65='From age 65 you need 1.0 to 1.2 g per kg to keep your muscles.',
                    tip_loss='While losing weight, 1.2 to 1.6 g per kg helps protect your muscles and keeps you full.',
                    tip_muscle='With resistance training the benefit levels off around 1.6 g per kg, with a useful upper value near 2.2.',
                    tip_glp1='GLP-1 medicines reduce appetite a lot, so it is easy to eat too little protein and lose muscle along with fat. Try to start each meal with protein, split your food into small meals, drink enough water, and do resistance exercise two to three times a week. If eating is difficult or you have troublesome symptoms, talk to your doctor.',
                    tip_adj='Your BMI is 30 or more, so we used your "adjusted weight" ({w} kg) so the amount is not overstated.',
                    nx_ok=_card('en', ['Work out your calories and goal date: <a href="{calc:deficit}">calorie deficit calculator</a>.',
                                       'Find protein-rich foods in the <a href="{site:/foods/index.html}">food guide</a>.'], first=_KIDNEY['en'])),
            body='''
            <h2 class="section-title"><i class="fas fa-table"></i> <span>How much protein for your goal?</span></h2>
            <div class="table-scroll"><table class="nutrition-table"><thead><tr><th>Goal</th><th>Grams per kg a day</th></tr></thead><tbody>
            <tr><td>General health (18 to 64)</td><td>0.83</td></tr><tr><td>General health (65 and over)</td><td>1.0 to 1.2</td></tr>
            <tr><td>Weight loss</td><td>1.2 to 1.6</td></tr><tr><td>Building muscle</td><td>1.6 (up to 2.2)</td></tr>
            <tr><td>GLP-1 medicines</td><td>1.2 to 1.6</td></tr></tbody></table></div>
            <h2 class="section-title"><i class="fas fa-weight-scale"></i> <span>What is "adjusted weight"?</span></h2>
            <p>If your BMI is 30 or more, using your full weight gives an amount that is too high, because fat tissue does not need protein the way muscle does. So we take the weight that matches a BMI of 25 for your height and add a quarter of the difference between that and your current weight.</p>
            <h2 class="section-title"><i class="fas fa-chart-pie"></i> <span>How are the macros split?</span></h2>
            <p>Protein follows your goal, fat is 30% of calories (within the European range of 20 to 35%), and carbohydrates are the rest. If you do not enter your calories we estimate them: your daily needs for general health and building muscle, and your needs minus 550 calories for weight loss and GLP-1 medicines (never below 1,200 for women and 1,500 for men).</p>
            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>How much protein is in common foods?</span></h2>
            <p>Figures from our food guide, for a usual portion:</p>
            {EXAMPLES}
            <p>Spread your protein over your meals: 25 to 40 grams at each main meal works better than one large amount in a single meal.</p>
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Who should not use this calculator?</span></h2>
            <p>People who are pregnant or breastfeeding (needs are different), people with chronic kidney disease, and anyone under 18.</p>''',
            faq=[('How many grams of protein do I need a day?', 'About 0.8 g per kg for a healthy adult, more with age, training and weight loss.'),
                 ('Does a lot of protein harm the kidneys?', 'In healthy people, studies show no harm at usual amounts; people with kidney disease need an amount set by their doctor.'),
                 ('Why do people on GLP-1 medicines need more protein?', 'Because they eat much less, and enough protein together with resistance exercise helps protect muscle.')],
            disclaimer=SMALL['en']),
        'nl': dict(
            title='Eiwitbehoefte berekenen: hoeveel eiwit heb je per dag nodig?',
            desc='Bereken hoeveel gram eiwit je per dag nodig hebt voor je gewicht, leeftijd en doel, met een macroverdeling en een aparte optie voor wie GLP-1-medicijnen gebruikt om af te vallen.',
            h1='Eiwitbehoefte en macro\'s berekenen', crumb='Eiwitcalculator', cat='Voeding en lichaam',
            short='Eiwitcalculator', blurb='Hoeveel gram eiwit je nodig hebt voor je doel.',
            about=[{'name': 'Eiwit'}, {'name': 'Macronutriënten'}, {'name': 'Obesitas', 'condition': True}],
            lead='Eiwit beschermt je spieren en geeft een vol gevoel. Je hebt er meer van nodig naarmate je ouder wordt, tijdens het afvallen en als je traint. Kies je doel en zie hoeveel gram je per dag nodig hebt en hoe je dat over je maaltijden verdeelt.',
            ui=dict(card_title='Bereken je eiwitbehoefte', lbl_sex='Geslacht', male='Man', female='Vrouw', lbl_age='Leeftijd (jaren)',
                    lbl_height='Lengte (cm)', lbl_weight='Gewicht (kg)', lbl_goal='Je doel',
                    goals=['Algemene gezondheid', 'Afvallen', 'Spieropbouw (krachttraining)', 'Ik gebruik een GLP-1-medicijn om af te vallen'],
                    lbl_activity='Lichamelijk activiteitsniveau', lbl_kcal='Je calorieën per dag (optioneel)', ph_kcal='leeg laten, dan rekenen wij',
                    ph_age='bijv. 40', ph_height='bijv. 170', ph_weight='bijv. 80',
                    btn='Bereken', res_heading='Je eiwit per dag', perkg='{v} g per kg', meal_label='Per maaltijd (3 maaltijden)',
                    basis_label='Gewicht in de berekening', basis_actual='je huidige gewicht', basis_adj='aangepast gewicht',
                    macros_header='Macro\'s op je calorieën', kcal_label='Calorieën', fat_label='Vet (30%)', carbs_label='Koolhydraten (de rest)',
                    st_ok='Schatting per dag',
                    tip_general='Voor een gezonde volwassene is ongeveer 0,83 g per kg per dag genoeg.',
                    tip_general65='Vanaf 65 jaar heb je 1,0 tot 1,2 g per kg nodig om je spieren te behouden.',
                    tip_loss='Tijdens het afvallen helpt 1,2 tot 1,6 g per kg om je spieren te beschermen en geeft het een vol gevoel.',
                    tip_muscle='Bij krachttraining vlakt het effect af rond 1,6 g per kg, met een zinvolle bovengrens rond 2,2.',
                    tip_glp1='GLP-1-medicijnen verminderen de eetlust sterk, waardoor je makkelijk te weinig eiwit eet en naast vet ook spieren verliest. Begin elke maaltijd met eiwit, verdeel je eten over kleine maaltijden, drink genoeg water en doe twee tot drie keer per week krachtoefeningen. Lukt eten moeilijk of heb je vervelende klachten, overleg dan met je arts.',
                    tip_adj='Je BMI is 30 of hoger, dus we rekenden met je "aangepaste gewicht" ({w} kg), zodat de hoeveelheid niet te hoog uitvalt.',
                    nx_ok=_card('nl', ['Bereken je calorieën en streefdatum: <a href="{calc:deficit}">calorietekort berekenen</a>.',
                                       'Zoek eiwitrijke producten in de <a href="{site:/foods/index.html}">voedingswijzer</a>.'], first=_KIDNEY['nl'])),
            body='''
            <h2 class="section-title"><i class="fas fa-table"></i> <span>Hoeveel eiwit bij jouw doel?</span></h2>
            <div class="table-scroll"><table class="nutrition-table"><thead><tr><th>Doel</th><th>Gram per kg per dag</th></tr></thead><tbody>
            <tr><td>Algemene gezondheid (18 tot 64)</td><td>0,83</td></tr><tr><td>Algemene gezondheid (65 en ouder)</td><td>1,0 tot 1,2</td></tr>
            <tr><td>Afvallen</td><td>1,2 tot 1,6</td></tr><tr><td>Spieropbouw</td><td>1,6 (tot 2,2)</td></tr>
            <tr><td>GLP-1-medicijnen</td><td>1,2 tot 1,6</td></tr></tbody></table></div>
            <h2 class="section-title"><i class="fas fa-weight-scale"></i> <span>Wat is "aangepast gewicht"?</span></h2>
            <p>Is je BMI 30 of hoger, dan geeft rekenen met je volledige gewicht een te hoge hoeveelheid, omdat vetweefsel niet zoveel eiwit nodig heeft als spieren. Daarom nemen we het gewicht dat bij een BMI van 25 hoort voor jouw lengte en tellen daar een kwart van het verschil met je huidige gewicht bij op.</p>
            <h2 class="section-title"><i class="fas fa-chart-pie"></i> <span>Hoe worden de macro's verdeeld?</span></h2>
            <p>Eiwit volgt je doel, vet is 30% van de calorieën (binnen het Europese bereik van 20 tot 35%) en koolhydraten vormen de rest. Vul je je calorieën niet in, dan schatten we ze: je dagelijkse behoefte bij algemene gezondheid en spieropbouw, en je behoefte min 550 kcal bij afvallen en GLP-1-medicijnen (nooit onder 1200 voor vrouwen en 1500 voor mannen).</p>
            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>Hoeveel eiwit zit er in veelgegeten producten?</span></h2>
            <p>Cijfers uit onze voedingswijzer, voor een gebruikelijke portie:</p>
            {EXAMPLES}
            <p>Verdeel je eiwit over je maaltijden: 25 tot 40 gram bij elke hoofdmaaltijd werkt beter dan een grote hoeveelheid in één maaltijd.</p>
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Voor wie is de calculator niet geschikt?</span></h2>
            <p>Voor zwangere vrouwen en vrouwen die borstvoeding geven (de behoefte is anders), voor mensen met chronische nierschade en voor mensen jonger dan 18.</p>''',
            faq=[('Hoeveel gram eiwit heb ik per dag nodig?', 'Ongeveer 0,8 g per kg voor een gezonde volwassene, meer naarmate je ouder wordt, traint of afvalt.'),
                 ('Is veel eiwit slecht voor de nieren?', 'Bij gezonde mensen tonen onderzoeken geen schade bij gebruikelijke hoeveelheden; mensen met een nierziekte hebben een hoeveelheid nodig die hun arts bepaalt.'),
                 ('Waarom hebben mensen die GLP-1-medicijnen gebruiken meer eiwit nodig?', 'Omdat ze veel minder eten; genoeg eiwit samen met krachttraining helpt de spieren te beschermen.')],
            disclaimer=SMALL['nl']),
        'sv': dict(
            title='Proteinkalkylator: hur mycket protein behöver du per dag?',
            desc='Räkna ut hur många gram protein du behöver per dag utifrån vikt, ålder och mål, med fördelning av makron och ett särskilt val för dig som tar GLP-1-läkemedel för viktnedgång.',
            h1='Räkna ut ditt proteinbehov och dina makron', crumb='Proteinkalkylator', cat='Kost och kropp',
            short='Proteinkalkylator', blurb='Hur många gram protein du behöver för ditt mål.',
            about=[{'name': 'Protein'}, {'name': 'Makronäringsämnen'}, {'name': 'Fetma', 'condition': True}],
            lead='Protein skyddar musklerna och ger mättnad, och behovet ökar med åldern, under viktnedgång och när du tränar. Välj ditt mål för att se hur många gram du behöver per dag och hur du fördelar dem över måltiderna.',
            ui=dict(card_title='Räkna ut ditt proteinbehov', lbl_sex='Kön', male='Man', female='Kvinna', lbl_age='Ålder (år)',
                    lbl_height='Längd (cm)', lbl_weight='Vikt (kg)', lbl_goal='Ditt mål',
                    goals=['Allmän hälsa', 'Viktnedgång', 'Bygga muskler (styrketräning)', 'Jag tar ett GLP-1-läkemedel för viktnedgång'],
                    lbl_activity='Fysisk aktivitetsnivå', lbl_kcal='Dina kalorier per dag (valfritt)', ph_kcal='lämna tomt så räknar vi',
                    ph_age='t.ex. 40', ph_height='t.ex. 170', ph_weight='t.ex. 80',
                    btn='Beräkna', res_heading='Ditt protein per dag', perkg='{v} g per kg', meal_label='Per måltid (3 måltider)',
                    basis_label='Vikt i beräkningen', basis_actual='din nuvarande vikt', basis_adj='justerad vikt',
                    macros_header='Makron på dina kalorier', kcal_label='Kalorier', fat_label='Fett (30 %)', carbs_label='Kolhydrater (resten)',
                    st_ok='Uppskattning per dag',
                    tip_general='För en frisk vuxen räcker ungefär 0,83 g per kg och dag.',
                    tip_general65='Från 65 år behöver du 1,0 till 1,2 g per kg för att behålla musklerna.',
                    tip_loss='Under viktnedgång hjälper 1,2 till 1,6 g per kg till att skydda musklerna och ger mättnad.',
                    tip_muscle='Vid styrketräning planar nyttan ut runt 1,6 g per kg, med en användbar övre nivå nära 2,2.',
                    tip_glp1='GLP-1-läkemedel minskar aptiten kraftigt, så det är lätt att få i sig för lite protein och förlora muskler tillsammans med fett. Försök börja varje måltid med protein, dela upp maten i små måltider, drick tillräckligt med vatten och styrketräna två till tre gånger i veckan. Om det är svårt att äta eller du får besvärande symtom, prata med din läkare.',
                    tip_adj='Ditt BMI är 30 eller mer, så vi räknade med din "justerade vikt" ({w} kg) så att mängden inte blir för hög.',
                    nx_ok=_card('sv', ['Räkna ut kalorier och måldatum: <a href="{calc:deficit}">räkna ut kaloriunderskott</a>.',
                                       'Hitta proteinrika livsmedel i <a href="{site:/foods/index.html}">livsmedelsguiden</a>.'], first=_KIDNEY['sv'])),
            body='''
            <h2 class="section-title"><i class="fas fa-table"></i> <span>Hur mycket protein för ditt mål?</span></h2>
            <div class="table-scroll"><table class="nutrition-table"><thead><tr><th>Mål</th><th>Gram per kg och dag</th></tr></thead><tbody>
            <tr><td>Allmän hälsa (18 till 64 år)</td><td>0,83</td></tr><tr><td>Allmän hälsa (65 år och äldre)</td><td>1,0 till 1,2</td></tr>
            <tr><td>Viktnedgång</td><td>1,2 till 1,6</td></tr><tr><td>Bygga muskler</td><td>1,6 (upp till 2,2)</td></tr>
            <tr><td>GLP-1-läkemedel</td><td>1,2 till 1,6</td></tr></tbody></table></div>
            <h2 class="section-title"><i class="fas fa-weight-scale"></i> <span>Vad är "justerad vikt"?</span></h2>
            <p>Om ditt BMI är 30 eller mer ger hela vikten en för hög mängd, eftersom fettvävnad inte behöver protein på samma sätt som muskler. Därför tar vi den vikt som motsvarar BMI 25 för din längd och lägger till en fjärdedel av skillnaden mellan den och din nuvarande vikt.</p>
            <h2 class="section-title"><i class="fas fa-chart-pie"></i> <span>Hur fördelas makrona?</span></h2>
            <p>Proteinet följer ditt mål, fettet är 30 % av kalorierna (inom det europeiska intervallet 20 till 35 %) och kolhydraterna är resten. Om du inte skriver in dina kalorier uppskattar vi dem: ditt dagliga behov vid allmän hälsa och muskeluppbyggnad, och behovet minus 550 kcal vid viktnedgång och GLP-1-läkemedel (aldrig under 1 200 för kvinnor och 1 500 för män).</p>
            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>Hur mycket protein finns i vanliga livsmedel?</span></h2>
            <p>Siffror från vår livsmedelsguide, för en vanlig portion:</p>
            {EXAMPLES}
            <p>Fördela proteinet över måltiderna: 25 till 40 gram vid varje huvudmål fungerar bättre än en stor mängd vid ett enda mål.</p>
            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Vem passar kalkylatorn inte för?</span></h2>
            <p>Den passar inte vid graviditet eller amning (behovet är annorlunda), vid kronisk njursjukdom eller för personer under 18 år.</p>''',
            faq=[('Hur många gram protein behöver jag per dag?', 'Ungefär 0,8 g per kg för en frisk vuxen, mer med stigande ålder, träning och viktnedgång.'),
                 ('Skadar mycket protein njurarna?', 'Hos friska personer visar studier ingen skada vid vanliga mängder; personer med njursjukdom behöver en mängd som läkaren bestämmer.'),
                 ('Varför behöver den som tar GLP-1-läkemedel mer protein?', 'Eftersom man äter mycket mindre, och tillräckligt med protein tillsammans med styrketräning hjälper till att skydda musklerna.')],
            disclaimer=SMALL['sv']),
    },
}

# ======================================================================================================== body fat
_LOWFAT = {'ar': 'يُنصح بمراجعة طبيبك: نسبة الدهون أقل من الدهون الأساسية التي يحتاجها الجسم، وقد تؤثر على الهرمونات والطاقة. تذكّر أن شريط القياس قد يخطئ بـ 3 إلى 4 نقاط.',
           'en': 'We recommend seeing your doctor: this is below the essential fat the body needs and can affect hormones and energy. Remember that the tape method can be off by 3 to 4 points.',
           'nl': 'We raden aan om naar je arts te gaan: dit ligt onder het essentiële vet dat je lichaam nodig heeft en kan je hormonen en energie beïnvloeden. Houd er rekening mee dat de meetlintmethode 3 tot 4 procentpunten kan afwijken.',
           'sv': 'Vi rekommenderar att du kontaktar din läkare: det här ligger under det livsnödvändiga fett kroppen behöver och kan påverka hormoner och energi. Tänk på att måttbandsmetoden kan slå fel med 3 till 4 procentenheter.'}

BODYFAT = {
    'key': 'bodyfat', 'slug': 'body-fat-calculator', 'icon': 'fa-person', 'badge': 'US Navy · Gallagher', 'category': 'body',
    'published': '2026-11-23', 'modified': '2026-11-23',
    'references': [
        'Hodgdon JA, Beckett MB. Prediction of percent body fat for U.S. Navy men and women from body circumferences and height. Naval Health Research Center, Reports No. 84-11 and 84-29, San Diego, 1984.',
        'Gallagher D, Heymsfield SB, Heo M, et al. Healthy percentage body fat ranges: an approach for developing guidelines based on body mass index. Am J Clin Nutr 2000;72:694-701.',
        'American Council on Exercise (ACE). Percent body fat norms for men and women.',
        'WHO Expert Consultation. Appropriate body-mass index for Asian populations and its implications for policy and intervention strategies. Lancet 2004;363:157-163.',
    ],
    'content': {
        'ar': dict(
            title='حساب نسبة الدهون في الجسم بشريط القياس',
            desc='احسب نسبة الدهون في جسمك بشريط قياس فقط (طريقة البحرية الأمريكية)، واعرف هل هي صحية لعمرك وجنسك، ونطاق الوزن الصحي لطولك.',
            h1='حاسبة نسبة الدهون في الجسم ونطاق الوزن الصحي', crumb='حاسبة نسبة الدهون', cat='التغذية والجسم',
            short='حاسبة نسبة الدهون', blurb='نسبة الدهون بشريط القياس والوزن الصحي لطولك.',
            about=[{'name': 'نسبة الدهون في الجسم'}, {'name': 'السمنة', 'condition': True}],
            lead='الميزان لا يفرّق بين الدهون والعضلات. بشريط قياس عادي وثلاثة قياسات (أربعة للنساء) يمكنك تقدير نسبة الدهون في جسمك، ومعرفة هل هي صحية لعمرك، والوزن الصحي المناسب لطولك.',
            ui=dict(card_title='احسب نسبة الدهون', lbl_sex='الجنس', male='ذكر', female='أنثى', lbl_age='العمر (سنوات)',
                    lbl_height='الطول (سم)', lbl_weight='الوزن (كغ)', lbl_neck='محيط الرقبة (سم)، تحت تفاحة آدم',
                    lbl_waist='محيط الخصر (سم): الرجال عند السرة، النساء عند أضيق نقطة', lbl_hip='محيط الورك (سم)، عند أعرض نقطة (للنساء)',
                    ph_age='مثال: 40', ph_height='مثال: 170', ph_weight='مثال: 80', ph_neck='مثال: 38', ph_waist='مثال: 90', ph_hip='مثال: 100',
                    btn='احسب', res_heading='نسبة الدهون في جسمك',
                    fatkg_label='كتلة الدهون', leankg_label='الكتلة الخالية من الدهون', range_label='النسبة الصحية لعمرك وجنسك',
                    hw_label='نطاق الوزن الصحي لطولك', kg='كغ',
                    st_verylow='منخفضة جداً', st_low='منخفضة', st_healthy='صحية', st_high='مرتفعة', st_veryhigh='مرتفعة جداً',
                    tip_verylow='أقل من الدهون الأساسية (5% للرجال و13% للنساء).',
                    tip_low='أقل من النطاق الصحي لعمرك. حافظ على أكل كافٍ وبروتين جيد.',
                    tip_healthy='ضمن النطاق الصحي لعمرك وجنسك. حافظ على تمارين المقاومة والبروتين الكافي.',
                    tip_high='أعلى من النطاق الصحي لعمرك. نزول بسيط في الوزن مع تمارين المقاومة يحسّن النسبة.',
                    tip_veryhigh='أعلى بوضوح من النطاق الصحي لعمرك. خطة هادئة لإنقاص الوزن مع بروتين كافٍ تساعدك.',
                    tip_invalid='تأكد من القياسات: يجب أن يكون الخصر أكبر من الرقبة.',
                    nx_verylow=_card('ar', ['احسب احتياجك من السعرات: <a href="{calc:tdee}">حاسبة السعرات اليومية</a>.'], first=_LOWFAT['ar']),
                    nx_low=_card('ar', ['احسب احتياجك من السعرات: <a href="{calc:tdee}">حاسبة السعرات اليومية</a>.', 'اعرف كم بروتين تحتاج: <a href="{calc:protein}">حاسبة البروتين اليومي</a>.']),
                    nx_healthy=_card('ar', ['اعرف كم بروتين تحتاج: <a href="{calc:protein}">حاسبة البروتين اليومي</a>.', 'قِس <a href="{calc:whtr}">نسبة الخصر إلى الطول</a>.']),
                    nx_high=_card('ar', ['احسب سعراتك وتاريخ الوصول: <a href="{calc:deficit}">حاسبة عجز السعرات</a>.', 'احمِ عضلاتك أثناء النزول: <a href="{calc:protein}">حاسبة البروتين اليومي</a>.', 'قِس <a href="{calc:whtr}">نسبة الخصر إلى الطول</a>.']),
                    nx_veryhigh=_card('ar', ['احسب سعراتك وتاريخ الوصول: <a href="{calc:deficit}">حاسبة عجز السعرات</a>.', 'احمِ عضلاتك أثناء النزول: <a href="{calc:protein}">حاسبة البروتين اليومي</a>.', 'قِس <a href="{calc:whtr}">نسبة الخصر إلى الطول</a>.'])),
            body='''
            <h2 class="section-title"><i class="fas fa-ruler"></i> <span>كيف تقيس بدقة؟</span></h2>
            <p>صباحاً قبل الأكل، بشريط غير مطاطي، دون شد. قِس كل موضع مرتين وخذ المتوسط. الرقبة تحت تفاحة آدم مباشرة، والخصر عند السرة للرجال وعند أضيق نقطة للنساء، والورك عند أعرض نقطة في الأرداف.</p>
            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>كيف تُحسب النسبة؟</span></h2>
            <p>نستخدم معادلات البحرية الأمريكية (Hodgdon وBeckett، 1984) بالسنتيمتر. للرجال تعتمد على الطول والرقبة والخصر، وللنساء نضيف الورك. كتلة الدهون = الوزن × النسبة، والباقي هو الكتلة الخالية من الدهون (العضلات والعظام والماء).</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>هل نسبتك صحية؟ (Gallagher 2000)</span></h2>
            <div class="table-scroll"><table class="nutrition-table"><thead><tr><th>العمر</th><th>الرجال: صحية</th><th>النساء: صحية</th></tr></thead><tbody>
            <tr><td>20 إلى 39</td><td>8% إلى أقل من 20%</td><td>21% إلى أقل من 33%</td></tr>
            <tr><td>40 إلى 59</td><td>11% إلى أقل من 22%</td><td>23% إلى أقل من 34%</td></tr>
            <tr><td>60 إلى 79</td><td>13% إلى أقل من 25%</td><td>24% إلى أقل من 36%</td></tr></tbody></table></div>
            <p>تحت النطاق تكون النسبة «منخفضة»، وفوقه «مرتفعة» ثم «مرتفعة جداً» (من 25/28/30% للرجال و39/40/42% للنساء حسب العمر). ونعتبرها «منخفضة جداً» تحت الدهون الأساسية: 5% للرجال و13% للنساء.</p>
            <p><strong>للرياضيين (جدول ACE، معلومة إضافية):</strong> 6 إلى 13% للرجال و14 إلى 20% للنساء.</p>
            <h2 class="section-title"><i class="fas fa-bullseye"></i> <span>ما دقة هذه الطريقة؟</span></h2>
            <p>الخطأ عادة بين 3 و4 نقاط مئوية مقارنة بالأجهزة الدقيقة (DEXA)، لكنها ممتازة لمتابعة التغيّر مع الوقت إذا قست بنفس الطريقة.</p>
            <h2 class="section-title"><i class="fas fa-weight-scale"></i> <span>نطاق الوزن الصحي</span></h2>
            <p>نحسبه من مؤشر كتلة الجسم بين 18.5 و24.9 لطولك. تعتبر منظمة الصحة العالمية أن الخطر الصحي لدى الأشخاص من أصول آسيوية يبدأ عند مؤشر أقل (من 23)، لذلك قد يكون الوزن الصحي لديهم أقرب للحد الأدنى من النطاق.</p>''',
            faq=[('ما هي نسبة الدهون الطبيعية؟', 'حسب العمر: للرجال تقريباً 8 إلى 25%، وللنساء 21 إلى 36%. الجدول أعلاه يوضح النطاق لكل عمر.'),
                 ('هل نسبة الدهون أهم من الوزن؟', 'هي تعطي صورة أدق، خاصة لمن يمارس الرياضة. ودهون البطن تحديداً هي الأهم صحياً.'),
                 ('هل أجهزة الميزان الذكي أدق؟', 'تتأثر كثيراً بالماء في الجسم، وطريقة الشريط ليست أقل منها في المتابعة.')],
            disclaimer=SMALL['ar']),
        'en': dict(
            title='Body Fat Calculator: Measure Your Body Fat with a Tape',
            desc='Estimate your body fat percentage with only a tape measure (US Navy method), see whether it is healthy for your age and sex, and find the healthy weight range for your height.',
            h1='Body fat calculator and healthy weight range', crumb='Body fat calculator', cat='Nutrition and body',
            short='Body fat calculator', blurb='Body fat with a tape measure and a healthy weight for your height.',
            about=[{'name': 'Body fat percentage'}, {'name': 'Obesity', 'condition': True}],
            lead='Scales cannot tell fat from muscle. With an ordinary tape measure and three measurements (four for women) you can estimate your body fat percentage, see whether it is healthy for your age, and find the healthy weight for your height.',
            ui=dict(card_title='Calculate your body fat', lbl_sex='Sex', male='Male', female='Female', lbl_age='Age (years)',
                    lbl_height='Height (cm)', lbl_weight='Weight (kg)', lbl_neck='Neck (cm), just below the Adam\'s apple',
                    lbl_waist='Waist (cm): men at the navel, women at the narrowest point', lbl_hip='Hips (cm), at the widest point (women)',
                    ph_age='e.g. 40', ph_height='e.g. 170', ph_weight='e.g. 80', ph_neck='e.g. 38', ph_waist='e.g. 90', ph_hip='e.g. 100',
                    btn='Calculate', res_heading='Your body fat percentage',
                    fatkg_label='Fat mass', leankg_label='Fat-free mass', range_label='Healthy range for your age and sex',
                    hw_label='Healthy weight range for your height', kg='kg',
                    st_verylow='Very low', st_low='Low', st_healthy='Healthy', st_high='High', st_veryhigh='Very high',
                    tip_verylow='Below essential fat (5% for men and 13% for women).',
                    tip_low='Below the healthy range for your age. Make sure you eat enough, with good protein.',
                    tip_healthy='Within the healthy range for your age and sex. Keep up resistance training and enough protein.',
                    tip_high='Above the healthy range for your age. A little weight loss together with resistance training improves it.',
                    tip_veryhigh='Clearly above the healthy range for your age. A gentle weight-loss plan with enough protein will help.',
                    tip_invalid='Please check your measurements: the waist must be larger than the neck.',
                    nx_verylow=_card('en', ['Work out your calorie needs: <a href="{calc:tdee}">daily calorie calculator</a>.'], first=_LOWFAT['en']),
                    nx_low=_card('en', ['Work out your calorie needs: <a href="{calc:tdee}">daily calorie calculator</a>.', 'See how much protein you need: <a href="{calc:protein}">protein calculator</a>.']),
                    nx_healthy=_card('en', ['See how much protein you need: <a href="{calc:protein}">protein calculator</a>.', 'Measure your <a href="{calc:whtr}">waist-to-height ratio</a>.']),
                    nx_high=_card('en', ['Work out your calories and goal date: <a href="{calc:deficit}">calorie deficit calculator</a>.', 'Protect your muscles while losing weight: <a href="{calc:protein}">protein calculator</a>.', 'Measure your <a href="{calc:whtr}">waist-to-height ratio</a>.']),
                    nx_veryhigh=_card('en', ['Work out your calories and goal date: <a href="{calc:deficit}">calorie deficit calculator</a>.', 'Protect your muscles while losing weight: <a href="{calc:protein}">protein calculator</a>.', 'Measure your <a href="{calc:whtr}">waist-to-height ratio</a>.'])),
            body='''
            <h2 class="section-title"><i class="fas fa-ruler"></i> <span>How to measure accurately</span></h2>
            <p>In the morning before eating, with a non-stretch tape, without pulling it tight. Measure each place twice and take the average. The neck just below the Adam's apple, the waist at the navel for men and at the narrowest point for women, and the hips at the widest point of the buttocks.</p>
            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>How is the percentage calculated?</span></h2>
            <p>We use the US Navy equations (Hodgdon and Beckett, 1984) in centimetres. For men they use height, neck and waist; for women we add the hips. Fat mass = weight × percentage, and the rest is fat-free mass (muscle, bone and water).</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>Is your percentage healthy? (Gallagher 2000)</span></h2>
            <div class="table-scroll"><table class="nutrition-table"><thead><tr><th>Age</th><th>Men: healthy</th><th>Women: healthy</th></tr></thead><tbody>
            <tr><td>20 to 39</td><td>8% to under 20%</td><td>21% to under 33%</td></tr>
            <tr><td>40 to 59</td><td>11% to under 22%</td><td>23% to under 34%</td></tr>
            <tr><td>60 to 79</td><td>13% to under 25%</td><td>24% to under 36%</td></tr></tbody></table></div>
            <p>Below the range the percentage is "low"; above it, "high" and then "very high" (from 25/28/30% for men and 39/40/42% for women, depending on age). We call it "very low" below essential fat: 5% for men and 13% for women.</p>
            <p><strong>For athletes (ACE table, extra information):</strong> 6 to 13% for men and 14 to 20% for women.</p>
            <h2 class="section-title"><i class="fas fa-bullseye"></i> <span>How accurate is this method?</span></h2>
            <p>The error is usually 3 to 4 percentage points compared with precise scans (DEXA), but it is excellent for following change over time if you measure the same way.</p>
            <h2 class="section-title"><i class="fas fa-weight-scale"></i> <span>Healthy weight range</span></h2>
            <p>We calculate it from a BMI of 18.5 to 24.9 for your height. The World Health Organization considers that health risk for people of Asian origin starts at a lower BMI (from 23), so their healthy weight may be closer to the lower end of the range.</p>''',
            faq=[('What is a normal body fat percentage?', 'It depends on age: roughly 8 to 25% for men and 21 to 36% for women. The table above shows the range for each age.'),
                 ('Is body fat more important than weight?', 'It gives a more accurate picture, especially if you exercise. Belly fat in particular matters most for health.'),
                 ('Are smart scales more accurate?', 'They are strongly affected by the water in your body; the tape method is no worse for following change.')],
            disclaimer=SMALL['en']),
        'nl': dict(
            title='Vetpercentage berekenen met een meetlint',
            desc='Bereken je vetpercentage met alleen een meetlint (methode van de Amerikaanse marine), zie of het gezond is voor je leeftijd en geslacht en wat een gezond gewicht is voor je lengte.',
            h1='Vetpercentage en gezond gewicht berekenen', crumb='Vetpercentage berekenen', cat='Voeding en lichaam',
            short='Vetpercentage berekenen', blurb='Vetpercentage met een meetlint en een gezond gewicht voor je lengte.',
            about=[{'name': 'Vetpercentage'}, {'name': 'Obesitas', 'condition': True}],
            lead='Een weegschaal ziet geen verschil tussen vet en spieren. Met een gewoon meetlint en drie metingen (vier voor vrouwen) schat je je vetpercentage, zie je of het gezond is voor je leeftijd en wat een gezond gewicht is voor je lengte.',
            ui=dict(card_title='Bereken je vetpercentage', lbl_sex='Geslacht', male='Man', female='Vrouw', lbl_age='Leeftijd (jaren)',
                    lbl_height='Lengte (cm)', lbl_weight='Gewicht (kg)', lbl_neck='Nek (cm), net onder de adamsappel',
                    lbl_waist='Taille (cm): mannen ter hoogte van de navel, vrouwen op het smalste punt', lbl_hip='Heupen (cm), op het breedste punt (vrouwen)',
                    ph_age='bijv. 40', ph_height='bijv. 170', ph_weight='bijv. 80', ph_neck='bijv. 38', ph_waist='bijv. 90', ph_hip='bijv. 100',
                    btn='Bereken', res_heading='Je vetpercentage',
                    fatkg_label='Vetmassa', leankg_label='Vetvrije massa', range_label='Gezond bereik voor je leeftijd en geslacht',
                    hw_label='Gezond gewicht voor je lengte', kg='kg',
                    st_verylow='Zeer laag', st_low='Laag', st_healthy='Gezond', st_high='Hoog', st_veryhigh='Zeer hoog',
                    tip_verylow='Onder het essentiële vet (5% voor mannen en 13% voor vrouwen).',
                    tip_low='Onder het gezonde bereik voor je leeftijd. Zorg dat je genoeg eet, met voldoende eiwit.',
                    tip_healthy='Binnen het gezonde bereik voor je leeftijd en geslacht. Blijf krachttraining doen en genoeg eiwit eten.',
                    tip_high='Boven het gezonde bereik voor je leeftijd. Een beetje afvallen samen met krachttraining verbetert het.',
                    tip_veryhigh='Duidelijk boven het gezonde bereik voor je leeftijd. Een rustig afvalplan met genoeg eiwit helpt je.',
                    tip_invalid='Controleer je metingen: de taille moet groter zijn dan de nek.',
                    nx_verylow=_card('nl', ['Bereken je caloriebehoefte: <a href="{calc:tdee}">calorieën per dag berekenen</a>.'], first=_LOWFAT['nl']),
                    nx_low=_card('nl', ['Bereken je caloriebehoefte: <a href="{calc:tdee}">calorieën per dag berekenen</a>.', 'Bekijk hoeveel eiwit je nodig hebt: <a href="{calc:protein}">eiwitcalculator</a>.']),
                    nx_healthy=_card('nl', ['Bekijk hoeveel eiwit je nodig hebt: <a href="{calc:protein}">eiwitcalculator</a>.', 'Meet je <a href="{calc:whtr}">taille-lengteverhouding</a>.']),
                    nx_high=_card('nl', ['Bereken je calorieën en streefdatum: <a href="{calc:deficit}">calorietekort berekenen</a>.', 'Bescherm je spieren tijdens het afvallen: <a href="{calc:protein}">eiwitcalculator</a>.', 'Meet je <a href="{calc:whtr}">taille-lengteverhouding</a>.']),
                    nx_veryhigh=_card('nl', ['Bereken je calorieën en streefdatum: <a href="{calc:deficit}">calorietekort berekenen</a>.', 'Bescherm je spieren tijdens het afvallen: <a href="{calc:protein}">eiwitcalculator</a>.', 'Meet je <a href="{calc:whtr}">taille-lengteverhouding</a>.'])),
            body='''
            <h2 class="section-title"><i class="fas fa-ruler"></i> <span>Zo meet je nauwkeurig</span></h2>
            <p>'s Ochtends voor het eten, met een meetlint dat niet rekt, zonder aan te trekken. Meet elke plek twee keer en neem het gemiddelde. De nek net onder de adamsappel, de taille bij mannen ter hoogte van de navel en bij vrouwen op het smalste punt, en de heupen op het breedste punt van de billen.</p>
            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>Hoe wordt het percentage berekend?</span></h2>
            <p>We gebruiken de formules van de Amerikaanse marine (Hodgdon en Beckett, 1984) in centimeters. Bij mannen met lengte, nek en taille; bij vrouwen komen de heupen erbij. Vetmassa = gewicht × percentage, de rest is vetvrije massa (spieren, botten en vocht).</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>Is je percentage gezond? (Gallagher 2000)</span></h2>
            <div class="table-scroll"><table class="nutrition-table"><thead><tr><th>Leeftijd</th><th>Mannen: gezond</th><th>Vrouwen: gezond</th></tr></thead><tbody>
            <tr><td>20 tot 39</td><td>8% tot onder 20%</td><td>21% tot onder 33%</td></tr>
            <tr><td>40 tot 59</td><td>11% tot onder 22%</td><td>23% tot onder 34%</td></tr>
            <tr><td>60 tot 79</td><td>13% tot onder 25%</td><td>24% tot onder 36%</td></tr></tbody></table></div>
            <p>Onder het bereik is het percentage "laag", erboven "hoog" en daarna "zeer hoog" (vanaf 25/28/30% voor mannen en 39/40/42% voor vrouwen, afhankelijk van de leeftijd). "Zeer laag" noemen we het onder het essentiële vet: 5% voor mannen en 13% voor vrouwen.</p>
            <p><strong>Voor sporters (ACE-tabel, extra informatie):</strong> 6 tot 13% voor mannen en 14 tot 20% voor vrouwen.</p>
            <h2 class="section-title"><i class="fas fa-bullseye"></i> <span>Hoe nauwkeurig is deze methode?</span></h2>
            <p>De afwijking is meestal 3 tot 4 procentpunten ten opzichte van nauwkeurige scans (DEXA), maar de methode is uitstekend om veranderingen te volgen als je steeds op dezelfde manier meet.</p>
            <h2 class="section-title"><i class="fas fa-weight-scale"></i> <span>Gezond gewicht</span></h2>
            <p>We berekenen het uit een BMI van 18,5 tot 24,9 voor jouw lengte. Volgens de Wereldgezondheidsorganisatie begint het gezondheidsrisico bij mensen van Aziatische afkomst bij een lagere BMI (vanaf 23), dus hun gezonde gewicht ligt mogelijk dichter bij de onderkant van het bereik.</p>''',
            faq=[('Wat is een normaal vetpercentage?', 'Dat hangt af van je leeftijd: ongeveer 8 tot 25% voor mannen en 21 tot 36% voor vrouwen. De tabel hierboven toont het bereik per leeftijd.'),
                 ('Is vetpercentage belangrijker dan gewicht?', 'Het geeft een nauwkeuriger beeld, vooral als je sport. Vooral buikvet is belangrijk voor je gezondheid.'),
                 ('Zijn slimme weegschalen nauwkeuriger?', 'Ze worden sterk beïnvloed door het vocht in je lichaam; de meetlintmethode is niet slechter om veranderingen te volgen.')],
            disclaimer=SMALL['nl']),
        'sv': dict(
            title='Räkna ut fettprocent med måttband',
            desc='Räkna ut din fettprocent med bara ett måttband (amerikanska flottans metod), se om den är hälsosam för din ålder och ditt kön och vilken vikt som är hälsosam för din längd.',
            h1='Räkna ut fettprocent och hälsosam vikt', crumb='Räkna ut fettprocent', cat='Kost och kropp',
            short='Räkna ut fettprocent', blurb='Fettprocent med måttband och hälsosam vikt för din längd.',
            about=[{'name': 'Fettprocent'}, {'name': 'Fetma', 'condition': True}],
            lead='Vågen skiljer inte på fett och muskler. Med ett vanligt måttband och tre mått (fyra för kvinnor) kan du uppskatta din fettprocent, se om den är hälsosam för din ålder och vilken vikt som är hälsosam för din längd.',
            ui=dict(card_title='Räkna ut din fettprocent', lbl_sex='Kön', male='Man', female='Kvinna', lbl_age='Ålder (år)',
                    lbl_height='Längd (cm)', lbl_weight='Vikt (kg)', lbl_neck='Hals (cm), precis under adamsäpplet',
                    lbl_waist='Midja (cm): män i höjd med naveln, kvinnor vid smalaste stället', lbl_hip='Höfter (cm), vid bredaste stället (kvinnor)',
                    ph_age='t.ex. 40', ph_height='t.ex. 170', ph_weight='t.ex. 80', ph_neck='t.ex. 38', ph_waist='t.ex. 90', ph_hip='t.ex. 100',
                    btn='Beräkna', res_heading='Din fettprocent',
                    fatkg_label='Fettmassa', leankg_label='Fettfri massa', range_label='Hälsosamt intervall för din ålder och ditt kön',
                    hw_label='Hälsosam vikt för din längd', kg='kg',
                    st_verylow='Mycket låg', st_low='Låg', st_healthy='Hälsosam', st_high='Hög', st_veryhigh='Mycket hög',
                    tip_verylow='Under det livsnödvändiga fettet (5 % för män och 13 % för kvinnor).',
                    tip_low='Under det hälsosamma intervallet för din ålder. Se till att äta tillräckligt, med bra protein.',
                    tip_healthy='Inom det hälsosamma intervallet för din ålder och ditt kön. Fortsätt med styrketräning och tillräckligt med protein.',
                    tip_high='Över det hälsosamma intervallet för din ålder. Lite viktnedgång tillsammans med styrketräning förbättrar det.',
                    tip_veryhigh='Tydligt över det hälsosamma intervallet för din ålder. En lugn viktnedgångsplan med tillräckligt med protein hjälper dig.',
                    tip_invalid='Kontrollera måtten: midjan måste vara större än halsen.',
                    nx_verylow=_card('sv', ['Räkna ut ditt kaloribehov: <a href="{calc:tdee}">räkna ut kaloribehov</a>.'], first=_LOWFAT['sv']),
                    nx_low=_card('sv', ['Räkna ut ditt kaloribehov: <a href="{calc:tdee}">räkna ut kaloribehov</a>.', 'Se hur mycket protein du behöver: <a href="{calc:protein}">proteinkalkylator</a>.']),
                    nx_healthy=_card('sv', ['Se hur mycket protein du behöver: <a href="{calc:protein}">proteinkalkylator</a>.', 'Mät din <a href="{calc:whtr}">midja-längd-kvot</a>.']),
                    nx_high=_card('sv', ['Räkna ut kalorier och måldatum: <a href="{calc:deficit}">räkna ut kaloriunderskott</a>.', 'Skydda musklerna under viktnedgången: <a href="{calc:protein}">proteinkalkylator</a>.', 'Mät din <a href="{calc:whtr}">midja-längd-kvot</a>.']),
                    nx_veryhigh=_card('sv', ['Räkna ut kalorier och måldatum: <a href="{calc:deficit}">räkna ut kaloriunderskott</a>.', 'Skydda musklerna under viktnedgången: <a href="{calc:protein}">proteinkalkylator</a>.', 'Mät din <a href="{calc:whtr}">midja-längd-kvot</a>.'])),
            body='''
            <h2 class="section-title"><i class="fas fa-ruler"></i> <span>Så mäter du rätt</span></h2>
            <p>På morgonen före frukost, med ett måttband som inte töjer sig, utan att dra åt. Mät varje ställe två gånger och ta medelvärdet. Halsen precis under adamsäpplet, midjan i höjd med naveln för män och vid smalaste stället för kvinnor, och höfterna vid sätets bredaste ställe.</p>
            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>Hur räknas procenten ut?</span></h2>
            <p>Vi använder amerikanska flottans ekvationer (Hodgdon och Beckett, 1984) i centimeter. För män används längd, hals och midja; för kvinnor lägger vi till höfterna. Fettmassa = vikt × procent, och resten är fettfri massa (muskler, skelett och vätska).</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>Är din fettprocent hälsosam? (Gallagher 2000)</span></h2>
            <div class="table-scroll"><table class="nutrition-table"><thead><tr><th>Ålder</th><th>Män: hälsosam</th><th>Kvinnor: hälsosam</th></tr></thead><tbody>
            <tr><td>20 till 39</td><td>8 % till under 20 %</td><td>21 % till under 33 %</td></tr>
            <tr><td>40 till 59</td><td>11 % till under 22 %</td><td>23 % till under 34 %</td></tr>
            <tr><td>60 till 79</td><td>13 % till under 25 %</td><td>24 % till under 36 %</td></tr></tbody></table></div>
            <p>Under intervallet är procenten "låg", över det "hög" och sedan "mycket hög" (från 25/28/30 % för män och 39/40/42 % för kvinnor beroende på ålder). "Mycket låg" kallar vi den under det livsnödvändiga fettet: 5 % för män och 13 % för kvinnor.</p>
            <p><strong>För idrottare (ACE-tabellen, extra information):</strong> 6 till 13 % för män och 14 till 20 % för kvinnor.</p>
            <h2 class="section-title"><i class="fas fa-bullseye"></i> <span>Hur exakt är metoden?</span></h2>
            <p>Felet är oftast 3 till 4 procentenheter jämfört med exakta mätningar (DEXA), men metoden är utmärkt för att följa förändringar över tid om du mäter på samma sätt.</p>
            <h2 class="section-title"><i class="fas fa-weight-scale"></i> <span>Hälsosam vikt</span></h2>
            <p>Vi räknar ut den från ett BMI på 18,5 till 24,9 för din längd. Världshälsoorganisationen anser att hälsorisken för personer med asiatiskt ursprung börjar vid ett lägre BMI (från 23), så deras hälsosamma vikt kan ligga närmare intervallets nedre del.</p>''',
            faq=[('Vad är en normal fettprocent?', 'Det beror på åldern: ungefär 8 till 25 % för män och 21 till 36 % för kvinnor. Tabellen ovan visar intervallet för varje ålder.'),
                 ('Är fettprocent viktigare än vikt?', 'Den ger en mer exakt bild, särskilt om du tränar. Det är främst bukfettet som spelar roll för hälsan.'),
                 ('Är smarta vågar mer exakta?', 'De påverkas mycket av vätskan i kroppen; måttbandsmetoden är inte sämre för att följa förändringar.')],
            disclaimer=SMALL['sv']),
    },
}

# ======================================================================================================== glycemic load
GL = {
    'key': 'gl', 'slug': 'glycemic-load-calculator', 'icon': 'fa-bowl-food', 'badge': 'GI · GL · Sydney', 'category': 'body',
    'published': '2026-11-23', 'modified': '2026-11-23',
    'references': [
        'Atkinson FS, Brand-Miller JC, Foster-Powell K, Buyken AE, Goletzke J. International tables of glycemic index and glycemic load values 2021: a systematic review. Am J Clin Nutr 2021;114:1625-1632.',
        'University of Sydney, Glycemic Index Research Service. About glycemic index and glycemic load (GL bands per serving and per day).',
        'Salmerón J, Ascherio A, Rimm EB, et al. Dietary fiber, glycemic load, and risk of NIDDM in men. Diabetes Care 1997;20:545-550.',
    ],
    'content': {
        'ar': dict(
            title='حاسبة الحمل الجلايسيمي: كم ترفع وجبتك السكر؟',
            desc='اختر أطعمة وجبتك من دليلنا واكتب الكمية بالغرام، لتعرف الحمل الجلايسيمي لكل طعام وللوجبة كاملة، وما هي البدائل الأقل رفعاً للسكر.',
            h1='حاسبة الحمل الجلايسيمي للوجبة', crumb='حاسبة الحمل الجلايسيمي', cat='التغذية والجسم',
            short='حاسبة الحمل الجلايسيمي', blurb='كم ترفع وجبتك السكر، من دليل الأطعمة.',
            about=[{'name': 'الحمل الجلايسيمي'}, {'name': 'المؤشر الجلايسيمي'}, {'name': 'السكري', 'condition': True}],
            lead='المؤشر الجلايسيمي يقول لك كم بسرعة يرفع الطعام السكر، أما الحمل الجلايسيمي فيضيف الكمية التي تأكلها، لذلك هو أقرب لما يحدث فعلاً بعد الوجبة. ابحث عن أطعمة وجبتك في دليلنا (أكثر من 970 طعاماً)، واكتب كمية كل طعام بالغرام.',
            ui=dict(card_title='كوّن وجبتك', lbl_search='ابحث عن طعام وأضفه للوجبة', ph_search='مثال: أرز، عدس، خبز',
                    no_match='لا توجد نتيجة. جرّب اسماً آخر.', loading='جارٍ تحميل دليل الأطعمة…', empty='لم تُضف أي طعام بعد.',
                    grams='غرام', remove='احذف', max_items='يمكنك إضافة 8 أطعمة كحد أقصى.',
                    btn='احسب الحمل الجلايسيمي', res_heading='مجموع الحمل الجلايسيمي للوجبة',
                    th_food='الطعام', th_grams='الكمية', th_carbs='كربوهيدرات متاحة', th_gi='المؤشر', th_gl='الحمل',
                    day_label='مقارنة بحدود اليوم كاملاً', day_txt='وجبتك = {p}% من حد اليوم المنخفض (80)',
                    top_label='أعلى طعام رفعاً للسكر في وجبتك', swap_txt='بديل بمؤشر أقل من نفس المجموعة: {b}', no_swap='لا يوجد بديل مناسب في نفس المجموعة.',
                    est_note='يتضمن قيماً تقديرية للمؤشر الجلايسيمي. <a href="{site:/methodology.html}#labels">كيف نقدّرها؟</a>',
                    zero_note='الأطعمة بدون كربوهيدرات تقريباً (مثل اللحوم والزيوت) حملها صفر.',
                    st_low='وجبة منخفضة الحمل', st_medium='وجبة متوسطة الحمل', st_high='وجبة مرتفعة الحمل',
                    bnd_low='منخفض', bnd_medium='متوسط', bnd_high='مرتفع',
                    tip_meal='لا يوجد حد رسمي معتمد للوجبة الواحدة. التصنيف هنا إرشادي تقريبي: أقل من 20 منخفض، و20 إلى 40 متوسط، وأكثر من 40 مرتفع. الحدود الموثّقة هي لليوم كاملاً: أقل من 80 منخفض، و80 إلى 120 متوسط، وأكثر من 120 مرتفع.',
                    nx_meal=_card('ar', ['جرّب تقليل كمية الطعام الأعلى حملاً أو استبداله، وشاهد كيف يتغير المجموع.',
                                         'أضف خضاراً أو بروتيناً للوجبة، فهي تبطئ ارتفاع السكر (لا تغيّر الحساب لكنها تساعد فعلياً).',
                                         'لمرضى السكري: استجابة السكر تختلف من شخص لآخر؛ قِس سكرك بعد الأكل بساعتين لتعرف تأثير وجبتك عليك، و<a href="{calc:glucose}">حوّل القراءة هنا</a>.'])),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>الفرق بين المؤشر والحمل بمثال</span></h2>
            <p>البطيخ مؤشره الجلايسيمي مرتفع (حوالي 72)، لكن شريحة 120 غراماً فيها كربوهيدرات قليلة، فحملها حوالي 6 فقط. أما صحن أرز أبيض 150 غراماً فحمله حوالي 27.</p>
            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>كيف نحسب؟</span></h2>
            <p>الحمل الجلايسيمي = المؤشر الجلايسيمي × الكربوهيدرات المتاحة في الكمية ÷ 100. والكربوهيدرات المتاحة = الكربوهيدرات ناقص الألياف. الأطعمة بدون كربوهيدرات تقريباً (اللحوم والزيوت) حملها صفر.</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>معنى النتيجة</span></h2>
            <div class="table-scroll"><table class="nutrition-table"><thead><tr><th></th><th>منخفض</th><th>متوسط</th><th>مرتفع</th></tr></thead><tbody>
            <tr><td>لكل طعام (حصة)</td><td>10 أو أقل</td><td>11 إلى 19</td><td>20 فأكثر</td></tr>
            <tr><td>لليوم كاملاً (موثّق)</td><td>أقل من 80</td><td>80 إلى 120</td><td>أكثر من 120</td></tr>
            <tr><td>للوجبة (إرشادي تقريبي)</td><td>أقل من 20</td><td>20 إلى 40</td><td>أكثر من 40</td></tr></tbody></table></div>
            <p>لا يوجد حد رسمي معتمد للوجبة الواحدة؛ تصنيف الوجبة هنا تقريبي للمساعدة فقط، ونقارنها أيضاً بحدود اليوم الموثّقة.</p>
            <h2 class="section-title"><i class="fas fa-scale-balanced"></i> <span>لماذا لا يكفي الحمل وحده؟</span></h2>
            <p>طريقة الطبخ، ونضج الفاكهة، والدهون والبروتين في الوجبة، تغيّر الاستجابة الفعلية للسكر.</p>
            <h2 class="section-title"><i class="fas fa-database"></i> <span>من أين تأتي القيم؟</span></h2>
            <p>من <a href="{site:/foods/index.html}">دليل الأطعمة</a> لدينا: القيم المنشورة من جداول المؤشر الجلايسيمي الدولية، والقيم التقديرية موضحة في <a href="{site:/methodology.html}">صفحة المنهجية</a>.</p>''',
            faq=[('ما هو الحمل الجلايسيمي الجيد للوجبة؟', 'لا يوجد حد رسمي للوجبة الواحدة؛ المرجع الشائع لليوم كاملاً أقل من 80 منخفض وأكثر من 120 مرتفع.'),
                 ('هل الطعام عالي المؤشر ممنوع؟', 'لا، الكمية هي الأهم، والحمل يوضح ذلك.'),
                 ('لماذا الحمل صفر للحوم؟', 'لأنها لا تحتوي كربوهيدرات تقريباً، لكن هذا لا يعني أنها بلا تأثير على الصحة.')],
            disclaimer=SMALL['ar']),
        'en': dict(
            title='Glycemic Load Calculator: How Much Does Your Meal Raise Sugar?',
            desc='Pick the foods in your meal from our guide and enter the amount in grams to see the glycemic load of each food and of the whole meal, and which swaps raise blood sugar less.',
            h1='Meal glycemic load calculator', crumb='Glycemic load calculator', cat='Nutrition and body',
            short='Glycemic load calculator', blurb='How much your meal raises blood sugar, from our food guide.',
            about=[{'name': 'Glycemic load'}, {'name': 'Glycemic index'}, {'name': 'Diabetes', 'condition': True}],
            lead='The glycemic index tells you how fast a food raises blood sugar; the glycemic load adds how much of it you eat, so it is closer to what really happens after a meal. Search our guide (more than 970 foods) for the foods in your meal and enter the amount of each in grams.',
            ui=dict(card_title='Build your meal', lbl_search='Search for a food and add it to the meal', ph_search='e.g. rice, lentils, bread',
                    no_match='No result. Try another name.', loading='Loading the food guide…', empty='You have not added any food yet.',
                    grams='grams', remove='Remove', max_items='You can add up to 8 foods.',
                    btn='Calculate glycemic load', res_heading='Total glycemic load of the meal',
                    th_food='Food', th_grams='Amount', th_carbs='Available carbs', th_gi='GI', th_gl='GL',
                    day_label='Compared with the daily limits', day_txt='Your meal = {p}% of the low daily limit (80)',
                    top_label='Food in your meal that raises sugar most', swap_txt='Lower-GI swap from the same group: {b}', no_swap='No suitable swap in the same group.',
                    est_note='Includes estimated glycemic index values. <a href="{site:/methodology.html}#labels">How do we estimate them?</a>',
                    zero_note='Foods with almost no carbohydrate (such as meat and oils) have a load of zero.',
                    st_low='Low-load meal', st_medium='Medium-load meal', st_high='High-load meal',
                    bnd_low='Low', bnd_medium='Medium', bnd_high='High',
                    tip_meal='There is no official cut-off for a single meal. The meal rating here is an approximate guide: under 20 low, 20 to 40 medium, over 40 high. The documented limits are for the whole day: under 80 low, 80 to 120 medium, over 120 high.',
                    nx_meal=_card('en', ['Try a smaller amount of the highest-load food or swap it, and watch the total change.',
                                         'Add vegetables or protein to the meal; they slow the rise in blood sugar (they do not change the calculation, but they help in practice).',
                                         'If you have diabetes: blood sugar responses differ between people; measure your blood sugar two hours after eating to see how your meal affects you, and <a href="{calc:glucose}">convert the reading here</a>.'])),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Index versus load, with an example</span></h2>
            <p>Watermelon has a high glycemic index (about 72), but a 120-gram slice contains little carbohydrate, so its load is only about 6. A 150-gram plate of white rice has a load of about 27.</p>
            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>How do we calculate?</span></h2>
            <p>Glycemic load = glycemic index × available carbohydrate in the amount ÷ 100. Available carbohydrate = carbohydrate minus fibre. Foods with almost no carbohydrate (meat and oils) have a load of zero.</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>What the result means</span></h2>
            <div class="table-scroll"><table class="nutrition-table"><thead><tr><th></th><th>Low</th><th>Medium</th><th>High</th></tr></thead><tbody>
            <tr><td>Per food (portion)</td><td>10 or less</td><td>11 to 19</td><td>20 or more</td></tr>
            <tr><td>Whole day (documented)</td><td>under 80</td><td>80 to 120</td><td>over 120</td></tr>
            <tr><td>Meal (approximate guide)</td><td>under 20</td><td>20 to 40</td><td>over 40</td></tr></tbody></table></div>
            <p>There is no official cut-off for a single meal; the meal rating here is an approximate aid only, and we also compare the meal with the documented daily limits.</p>
            <h2 class="section-title"><i class="fas fa-scale-balanced"></i> <span>Why is the load not enough on its own?</span></h2>
            <p>Cooking method, ripeness of fruit, and the fat and protein in the meal change the actual blood sugar response.</p>
            <h2 class="section-title"><i class="fas fa-database"></i> <span>Where do the values come from?</span></h2>
            <p>From our <a href="{site:/foods/index.html}">food guide</a>: published values come from the international glycemic index tables, and estimated values are explained on the <a href="{site:/methodology.html}">methodology page</a>.</p>''',
            faq=[('What is a good glycemic load for a meal?', 'There is no official cut-off for a single meal; the common reference for the whole day is under 80 low and over 120 high.'),
                 ('Are high-GI foods forbidden?', 'No, the amount matters most, and the load shows this.'),
                 ('Why is the load zero for meat?', 'Because it contains almost no carbohydrate, but that does not mean it has no effect on health.')],
            disclaimer=SMALL['en']),
        'nl': dict(
            title='Glykemische lading berekenen: hoeveel verhoogt je maaltijd je suiker?',
            desc='Kies de producten van je maaltijd uit onze voedingswijzer en vul de hoeveelheid in gram in. Je ziet de glykemische lading per product en voor de hele maaltijd, en welke vervangers je suiker minder verhogen.',
            h1='Glykemische lading van je maaltijd berekenen', crumb='Glykemische lading berekenen', cat='Voeding en lichaam',
            short='Glykemische lading berekenen', blurb='Hoeveel je maaltijd je bloedsuiker verhoogt, uit onze voedingswijzer.',
            about=[{'name': 'Glykemische lading'}, {'name': 'Glykemische index'}, {'name': 'Diabetes', 'condition': True}],
            lead='De glykemische index zegt hoe snel een product je bloedsuiker verhoogt; de glykemische lading telt ook mee hoeveel je ervan eet, en komt daardoor dichter bij wat er na een maaltijd echt gebeurt. Zoek de producten van je maaltijd in onze voedingswijzer (meer dan 970 producten) en vul per product de hoeveelheid in gram in.',
            ui=dict(card_title='Stel je maaltijd samen', lbl_search='Zoek een product en voeg het toe aan de maaltijd', ph_search='bijv. rijst, linzen, brood',
                    no_match='Geen resultaat. Probeer een andere naam.', loading='Voedingswijzer wordt geladen…', empty='Je hebt nog geen product toegevoegd.',
                    grams='gram', remove='Verwijderen', max_items='Je kunt maximaal 8 producten toevoegen.',
                    btn='Bereken de glykemische lading', res_heading='Totale glykemische lading van de maaltijd',
                    th_food='Product', th_grams='Hoeveelheid', th_carbs='Beschikbare koolhydraten', th_gi='GI', th_gl='GL',
                    day_label='Vergeleken met de grenzen per dag', day_txt='Je maaltijd = {p}% van de lage dagelijkse grens (80)',
                    top_label='Product in je maaltijd dat je suiker het meest verhoogt', swap_txt='Vervanger met een lagere GI uit dezelfde groep: {b}', no_swap='Geen geschikte vervanger in dezelfde groep.',
                    est_note='Bevat geschatte waarden voor de glykemische index. <a href="{site:/methodology.html}#labels">Hoe schatten we die?</a>',
                    zero_note='Producten met bijna geen koolhydraten (zoals vlees en olie) hebben een lading van nul.',
                    st_low='Maaltijd met lage lading', st_medium='Maaltijd met middelhoge lading', st_high='Maaltijd met hoge lading',
                    bnd_low='Laag', bnd_medium='Middel', bnd_high='Hoog',
                    tip_meal='Er bestaat geen officiële grens voor één maaltijd. De indeling hier is een benaderende richtlijn: onder 20 laag, 20 tot 40 middel, boven 40 hoog. De vastgelegde grenzen gelden voor de hele dag: onder 80 laag, 80 tot 120 middel, boven 120 hoog.',
                    nx_meal=_card('nl', ['Neem minder van het product met de hoogste lading of vervang het, en zie hoe het totaal verandert.',
                                         'Voeg groente of eiwit toe aan de maaltijd; dat remt de stijging van je bloedsuiker (het verandert de berekening niet, maar helpt in de praktijk).',
                                         'Bij diabetes: de reactie van de bloedsuiker verschilt per persoon; meet je bloedsuiker twee uur na het eten om het effect van je maaltijd te zien, en <a href="{calc:glucose}">reken de waarde hier om</a>.'])),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Index en lading: een voorbeeld</span></h2>
            <p>Watermeloen heeft een hoge glykemische index (ongeveer 72), maar een plak van 120 gram bevat weinig koolhydraten, dus de lading is maar ongeveer 6. Een bord witte rijst van 150 gram heeft een lading van ongeveer 27.</p>
            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>Hoe rekenen we?</span></h2>
            <p>Glykemische lading = glykemische index × beschikbare koolhydraten in de hoeveelheid ÷ 100. Beschikbare koolhydraten = koolhydraten min vezels. Producten met bijna geen koolhydraten (vlees en olie) hebben een lading van nul.</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>Wat betekent de uitkomst?</span></h2>
            <div class="table-scroll"><table class="nutrition-table"><thead><tr><th></th><th>Laag</th><th>Middel</th><th>Hoog</th></tr></thead><tbody>
            <tr><td>Per product (portie)</td><td>10 of minder</td><td>11 tot 19</td><td>20 of meer</td></tr>
            <tr><td>Hele dag (vastgelegd)</td><td>onder 80</td><td>80 tot 120</td><td>boven 120</td></tr>
            <tr><td>Maaltijd (benaderende richtlijn)</td><td>onder 20</td><td>20 tot 40</td><td>boven 40</td></tr></tbody></table></div>
            <p>Er bestaat geen officiële grens voor één maaltijd; de indeling van de maaltijd is hier alleen een benaderend hulpmiddel, en we vergelijken de maaltijd ook met de vastgelegde grenzen per dag.</p>
            <h2 class="section-title"><i class="fas fa-scale-balanced"></i> <span>Waarom is de lading alleen niet genoeg?</span></h2>
            <p>De bereidingswijze, de rijpheid van fruit en het vet en eiwit in de maaltijd veranderen de werkelijke reactie van je bloedsuiker.</p>
            <h2 class="section-title"><i class="fas fa-database"></i> <span>Waar komen de waarden vandaan?</span></h2>
            <p>Uit onze <a href="{site:/foods/index.html}">voedingswijzer</a>: gepubliceerde waarden komen uit de internationale tabellen voor de glykemische index, en geschatte waarden lichten we toe op de <a href="{site:/methodology.html}">pagina over onze werkwijze</a>.</p>''',
            faq=[('Wat is een goede glykemische lading voor een maaltijd?', 'Er bestaat geen officiële grens voor één maaltijd; de gebruikelijke maat voor de hele dag is onder 80 laag en boven 120 hoog.'),
                 ('Zijn producten met een hoge GI verboden?', 'Nee, de hoeveelheid is het belangrijkst, en de lading laat dat zien.'),
                 ('Waarom is de lading van vlees nul?', 'Omdat vlees bijna geen koolhydraten bevat, maar dat betekent niet dat het geen effect op je gezondheid heeft.')],
            disclaimer=SMALL['nl']),
        'sv': dict(
            title='Glykemisk belastning: hur mycket höjer din måltid blodsockret?',
            desc='Välj livsmedlen i din måltid ur vår guide och skriv in mängden i gram, så ser du den glykemiska belastningen för varje livsmedel och hela måltiden och vilka byten som höjer blodsockret mindre.',
            h1='Räkna ut måltidens glykemiska belastning', crumb='Glykemisk belastning', cat='Kost och kropp',
            short='Räkna ut glykemisk belastning', blurb='Hur mycket din måltid höjer blodsockret, från vår livsmedelsguide.',
            about=[{'name': 'Glykemisk belastning'}, {'name': 'Glykemiskt index'}, {'name': 'Diabetes', 'condition': True}],
            lead='Det glykemiska indexet visar hur snabbt ett livsmedel höjer blodsockret; den glykemiska belastningen tar också med hur mycket du äter, och ligger därför närmare det som faktiskt händer efter en måltid. Sök efter livsmedlen i din måltid i vår guide (fler än 970 livsmedel) och skriv in mängden av varje i gram.',
            ui=dict(card_title='Sätt ihop din måltid', lbl_search='Sök ett livsmedel och lägg till det i måltiden', ph_search='t.ex. ris, linser, bröd',
                    no_match='Inget resultat. Prova ett annat namn.', loading='Livsmedelsguiden laddas…', empty='Du har inte lagt till något livsmedel än.',
                    grams='gram', remove='Ta bort', max_items='Du kan lägga till högst 8 livsmedel.',
                    btn='Räkna ut glykemisk belastning', res_heading='Måltidens totala glykemiska belastning',
                    th_food='Livsmedel', th_grams='Mängd', th_carbs='Tillgängliga kolhydrater', th_gi='GI', th_gl='GL',
                    day_label='Jämfört med gränserna för hela dagen', day_txt='Din måltid = {p} % av den låga dagsgränsen (80)',
                    top_label='Livsmedlet i måltiden som höjer blodsockret mest', swap_txt='Byte med lägre GI från samma grupp: {b}', no_swap='Inget lämpligt byte i samma grupp.',
                    est_note='Innehåller uppskattade värden för glykemiskt index. <a href="{site:/methodology.html}#labels">Hur uppskattar vi dem?</a>',
                    zero_note='Livsmedel nästan utan kolhydrater (som kött och oljor) har belastningen noll.',
                    st_low='Måltid med låg belastning', st_medium='Måltid med medelhög belastning', st_high='Måltid med hög belastning',
                    bnd_low='Låg', bnd_medium='Medel', bnd_high='Hög',
                    tip_meal='Det finns ingen officiell gräns för en enskild måltid. Indelningen här är en ungefärlig vägledning: under 20 låg, 20 till 40 medel, över 40 hög. De dokumenterade gränserna gäller hela dagen: under 80 låg, 80 till 120 medel, över 120 hög.',
                    nx_meal=_card('sv', ['Prova en mindre mängd av livsmedlet med högst belastning eller byt ut det, och se hur summan ändras.',
                                         'Lägg till grönsaker eller protein i måltiden; det bromsar blodsockerhöjningen (det ändrar inte beräkningen, men hjälper i praktiken).',
                                         'Vid diabetes: blodsockersvaret skiljer sig mellan personer; mät blodsockret två timmar efter maten för att se hur din måltid påverkar dig, och <a href="{calc:glucose}">omvandla värdet här</a>.'])),
            body='''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Index och belastning, med ett exempel</span></h2>
            <p>Vattenmelon har ett högt glykemiskt index (ungefär 72), men en skiva på 120 gram innehåller lite kolhydrater, så belastningen är bara ungefär 6. En tallrik vitt ris på 150 gram har en belastning på ungefär 27.</p>
            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>Hur räknar vi?</span></h2>
            <p>Glykemisk belastning = glykemiskt index × tillgängliga kolhydrater i mängden ÷ 100. Tillgängliga kolhydrater = kolhydrater minus fibrer. Livsmedel nästan utan kolhydrater (kött och oljor) har belastningen noll.</p>
            <h2 class="section-title"><i class="fas fa-table"></i> <span>Vad betyder resultatet?</span></h2>
            <div class="table-scroll"><table class="nutrition-table"><thead><tr><th></th><th>Låg</th><th>Medel</th><th>Hög</th></tr></thead><tbody>
            <tr><td>Per livsmedel (portion)</td><td>10 eller mindre</td><td>11 till 19</td><td>20 eller mer</td></tr>
            <tr><td>Hela dagen (dokumenterat)</td><td>under 80</td><td>80 till 120</td><td>över 120</td></tr>
            <tr><td>Måltid (ungefärlig vägledning)</td><td>under 20</td><td>20 till 40</td><td>över 40</td></tr></tbody></table></div>
            <p>Det finns ingen officiell gräns för en enskild måltid; indelningen av måltiden är här bara ett ungefärligt hjälpmedel, och vi jämför också måltiden med de dokumenterade gränserna för hela dagen.</p>
            <h2 class="section-title"><i class="fas fa-scale-balanced"></i> <span>Varför räcker inte belastningen ensam?</span></h2>
            <p>Tillagningssätt, fruktens mognad och fettet och proteinet i måltiden ändrar det faktiska blodsockersvaret.</p>
            <h2 class="section-title"><i class="fas fa-database"></i> <span>Varifrån kommer värdena?</span></h2>
            <p>Från vår <a href="{site:/foods/index.html}">livsmedelsguide</a>: publicerade värden kommer från de internationella tabellerna för glykemiskt index, och uppskattade värden förklaras på <a href="{site:/methodology.html}">sidan om vår metod</a>.</p>''',
            faq=[('Vad är en bra glykemisk belastning för en måltid?', 'Det finns ingen officiell gräns för en enskild måltid; den vanliga referensen för hela dagen är under 80 låg och över 120 hög.'),
                 ('Är livsmedel med högt GI förbjudna?', 'Nej, mängden är viktigast, och belastningen visar det.'),
                 ('Varför är belastningen noll för kött?', 'Eftersom kött nästan inte innehåller kolhydrater, men det betyder inte att det saknar betydelse för hälsan.')],
            disclaimer=SMALL['sv']),
    },
}

for _lang, _c in PROTEIN['content'].items():
    _c['body'] = _c['body'].replace('{EXAMPLES}', protein_examples(_lang))

NUTRITION_TOOLS = [DEFICIT, PROTEIN, BODYFAT, GL]


def gl_foods():
    """Compact food list for the glycemic load tool: published foods only, names in 4 languages, slug, GI (null when
    not applicable), estimated flag (anything but a measured, published value), available carbs per 100 g, usual
    portion in grams, food group and food type (PILOT kind, for swaps).
    Columns: id, slug, ar, en, nl, sv, gi, est, avail, portion, group, kind."""
    import json
    ov_path = _gfp.ROOT / 'scripts' / 'food_pages_overrides.json'
    ov = json.loads(ov_path.read_text(encoding='utf-8')).get('foods', {}) if ov_path.exists() else {}
    rows = []
    for fid, (kind, grams) in sorted(_gfp.PILOT.items()):
        f = _FOODS[fid]
        slug = ov.get(str(fid), {}).get('slug') or _gfp.SLUG_OVERRIDES.get(fid) or _gfp.slugify(f['en'])
        gi = int(f['gi']) if f['gi'] is not None else None
        rows.append([fid, slug, f['ar'], f['en'], f['nl'], _fsv.NAMES[fid][0], gi,
                     0 if f['gi_status'] == 'measured' else 1, f['avail'], grams, f['group'], kind])
    return rows
