"""Daily water intake calculator content (AR / EN / NL).
Method: weight-based clinical rule (30-35 ml/kg) + activity add-on (+ pregnancy 300 ml / lactation 700 ml, EFSA),
shown next to the EFSA 2010 adequate intake (women 2.0 L, men 2.5 L total water, ~80% from drinks).
Worked example: man, 75 kg, 30 min activity (+350 ml) -> 2.6-3.0 L, 10-12 cups; EFSA 2.5 L total, ~2.0 L from drinks."""

WATER = {
    'key': 'water',
    'slug': 'water-calculator',
    'icon': 'fa-droplet',
    'badge': 'EFSA 2010 · ACSM',
    'published': '2026-10-18',
    'modified': '2026-10-18',
    'references': [
        'EFSA Panel on Dietetic Products, Nutrition, and Allergies (NDA). Scientific Opinion on Dietary Reference Values for water. EFSA Journal. 2010;8(3):1459.',
        'Popkin BM, D’Anci KE, Rosenberg IH. Water, hydration, and health. Nutr Rev. 2010;68(8):439-458.',
        'American College of Sports Medicine; Sawka MN, Burke LM, Eichner ER, et al. Exercise and fluid replacement. Med Sci Sports Exerc. 2007;39(2):377-390.',
        'Killer SC, Blannin AK, Jeukendrup AE. No evidence of dehydration with moderate daily coffee intake: a counterbalanced cross-over study in a free-living population. PLoS One. 2014;9(1):e84154.',
        'Dennis EA, Dengo AL, Comber DL, et al. Water consumption increases weight loss during a hypocaloric diet intervention in middle-aged and older adults. Obesity. 2010;18(2):300-307.',
    ],
    'content': {
        'ar': {
            'title': 'حاسبة شرب الماء اليومي: كم لتر ماء تحتاج حسب وزنك؟ | WiBo Health',
            'desc': 'احسب كمية الماء التي تحتاجها يومياً حسب وزنك ونشاطك، وقارنها بقيم EFSA المرجعية للرجال والنساء والحامل والمرضع، مع علامات الجفاف ونصائح طبية.',
            'h1': 'حاسبة شرب الماء اليومي: كم لتراً من الماء تحتاج حسب وزنك ونشاطك؟',
            'crumb': 'حاسبة الماء',
            'cat': 'حاسبة طبية · السوائل والترطيب',
            'short': 'احتياج الماء اليومي',
            'blurb': 'كمية السوائل المناسبة لوزنك ونشاطك.',
            'about': [{'name': 'الترطيب'}, {'name': 'الجفاف', 'condition': True}],
            'lead': 'يشكل الماء أكثر من نصف وزن جسم الإنسان البالغ، ويحتاجه كل عضو فيه. تحسب هذه الأداة احتياجك اليومي من السوائل حسب وزنك ومجهودك البدني، وتعرض بجانبه القيم المرجعية الرسمية للهيئة الأوروبية لسلامة الأغذية (EFSA)، لتعرف بالأرقام كم كوباً تحتاج فعلاً.',
            'ui': {
                'card_title': 'احسب احتياجك من الماء', 'lbl_sex': 'الجنس', 'male': 'ذكر', 'female': 'أنثى',
                'lbl_weight': 'الوزن (كغ)', 'ph_weight': 'مثال: 75',
                'lbl_activity': 'التمرين أو المجهود اليومي', 'acts': [
                    'بدون تمرين / عمل مكتبي', '30 دقيقة نشاط معتدل (+350 مل)', '60 دقيقة تمرين نشط (+650 مل)',
                    '90 دقيقة فأكثر أو طقس حار (+1000 مل)'],
                'lbl_status': 'الحمل والرضاعة (للنساء)', 'status_opts': ['لا ينطبق', 'حامل (+300 مل)', 'مرضع (+700 مل)'],
                'btn': 'احسب احتياجي من الماء', 'res_heading': 'احتياجك اليومي التقديري من السوائل',
                'cups': '{a} إلى {b} أكواب (250 مل)',
                'efsa_label': 'مرجع EFSA لإجمالي الماء', 'efsa_sub': 'من المشروبات والطعام معاً',
                'drinks_label': 'منها من المشروبات تقريباً', 'drinks_sub': 'نحو 80% من الإجمالي',
                'tip': 'وزّع شربك على اليوم ولا تنتظر العطش، واجعل لون البول الأصفر الفاتح دليلك. الشاي والقهوة المعتدلان يُحسبان من السوائل، أما المشروبات المحلاة فاستبدلها بالماء.',
                'tip_heavy': 'مع الأوزان المرتفعة تبالغ قاعدة «مل لكل كغ» في التقدير؛ اعتبر الحد الأدنى من النطاق أو مرجع EFSA نقطة البداية، وعدّل حسب العطش ولون البول.',
            },
            'body': '''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>لماذا يحتاج جسمك إلى الماء؟</span></h2>
            <p>يشكل الماء نحو 50 إلى 60% من وزن البالغ، وهو الوسط الذي تجري فيه كل العمليات الحيوية تقريباً: ينقل المغذيات والأكسجين في الدم، وينظم حرارة الجسم بالتعرق، ويطرد الفضلات عبر الكلى، ويرطب المفاصل والأغشية. ولأن الجسم لا يخزن الماء، فإن ما نفقده يومياً بالبول والعرق والتنفس يجب تعويضه باستمرار.</p>
            <p>حتى الجفاف البسيط، أي فقدان نحو 1–2% من وزن الجسم ماءً، قد يرتبط بالصداع والتعب وضعف التركيز وانخفاض الأداء الرياضي، كما ذكرت مراجعة منشورة في مجلة Nutrition Reviews.</p>

            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>كيف تحسب الأداة احتياجك من الماء؟</span></h2>
            <p>تعتمد الحاسبة على طريقتين متكاملتين:</p>
            <ol class="steps">
                <li><strong>القاعدة السريرية حسب الوزن:</strong> من 30 إلى 35 مل لكل كيلوغرام من وزن الجسم، وهي قاعدة شائعة في الممارسة الغذائية، ثم يُضاف ماء التمرين حسب مدته وشدته.</li>
                <li><strong>القيمة المرجعية الأوروبية (EFSA):</strong> وتُعرض للمقارنة؛ فهي «كمية كافية» محددة لإجمالي الماء من المشروبات والطعام معاً.</li>
            </ol>
            <p class="formula-box">احتياج الماء (لتر) = الوزن × (0.030 إلى 0.035) + ماء التمرين + (0.3 للحامل أو 0.7 للمرضع)</p>
            <p><strong>مثال عملي:</strong> رجل وزنه 75 كغ يمارس 30 دقيقة نشاطاً معتدلاً. 75 × 30 = 2250 مل، و75 × 35 = 2625 مل، ومع 350 مل للتمرين يصبح النطاق <strong>2.6 إلى 3.0 لترات يومياً</strong>، أي نحو 10 إلى 12 كوباً. ومرجع EFSA للرجل 2.5 لتر من كل المصادر، منها نحو 2.0 لتر من المشروبات.</p>

            <h2 class="section-title"><i class="fas fa-table"></i> <span>جدول القيم المرجعية للماء حسب EFSA</span></h2>
            <p>حددت الهيئة الأوروبية لسلامة الأغذية عام 2010 «الكمية الكافية» من إجمالي الماء يومياً، ويأتي عادة 20 إلى 30% منها من الطعام والباقي من المشروبات:</p>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>الفئة</th><th>إجمالي الماء يومياً</th><th>من المشروبات تقريباً (80%)</th></tr></thead>
                <tbody>
                    <tr><td>الأطفال 4–8 سنوات</td><td>1.6 لتر</td><td>1.3 لتر</td></tr>
                    <tr><td>الأولاد 9–13 سنة</td><td>2.1 لتر</td><td>1.7 لتر</td></tr>
                    <tr><td>البنات 9–13 سنة</td><td>1.9 لتر</td><td>1.5 لتر</td></tr>
                    <tr><td>النساء (14 عاماً فأكثر)</td><td>2.0 لتر</td><td>1.6 لتر</td></tr>
                    <tr><td>الرجال (14 عاماً فأكثر)</td><td>2.5 لتر</td><td>2.0 لتر</td></tr>
                    <tr><td>الحامل</td><td>2.3 لتر</td><td>1.8 لتر</td></tr>
                    <tr><td>المرضع</td><td>2.7 لتر</td><td>2.2 لتر</td></tr>
                </tbody>
            </table></div>
            <p>هذه القيم لظروف حرارة معتدلة ونشاط متوسط؛ وفي الطقس الحار، كصيف الخليج، أو مع التمارين الطويلة يرتفع الاحتياج بوضوح.</p>

            <h2 class="section-title"><i class="fas fa-person-running"></i> <span>الماء والتمارين الرياضية</span></h2>
            <p>توصي الكلية الأمريكية للطب الرياضي (ACSM) بألا يتجاوز فقدان الوزن بالتعرق 2% من وزن الجسم خلال التمرين. وأبسط طريقة لمعرفة احتياجك أن تزن نفسك قبل التمرين وبعده: كل كيلوغرام تخسره يحتاج إلى نحو <strong>1.5 لتر</strong> من السوائل لتعويضه تدريجياً. وفي التمارين التي تزيد على ساعة مع تعرق غزير، يفيد مشروب يحتوي على الأملاح (الصوديوم).</p>

            <h2 class="section-title"><i class="fas fa-eye"></i> <span>كيف تعرف أنك تشرب كفاية؟ علامات الجفاف</span></h2>
            <ul class="check-list">
                <li><strong>لون البول:</strong> الأصفر الفاتح (لون القش) علامة ترطيب جيد، والأصفر الداكن علامة على الحاجة إلى مزيد من الماء.</li>
                <li><strong>العطش وجفاف الفم:</strong> إشارات متأخرة نسبياً، وتضعف لدى كبار السن، لذلك يحتاجون إلى جدول شرب منتظم.</li>
                <li><strong>الصداع والتعب والدوخة عند الوقوف:</strong> قد تكون من علامات الجفاف، خاصة في الحر.</li>
                <li><strong>قلة التبول:</strong> أقل من 4 مرات يومياً قد يشير إلى نقص السوائل.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>متى يجب الحذر من شرب الماء بكثرة؟</span></h2>
            <p>الإفراط الشديد في شرب الماء خلال وقت قصير قد يخفض صوديوم الدم (نقص صوديوم الدم)، وهي حالة خطيرة تُشاهد أحياناً في سباقات التحمل الطويلة. والأهم أن بعض المرضى يحتاجون إلى <strong>تقييد السوائل</strong> بأمر الطبيب، مثل مرضى قصور القلب، والفشل الكلوي المتقدم وغسيل الكلى، وتليف الكبد، ومتلازمة الإفراز غير الملائم للهرمون المضاد للإدرار. إذا كنت من هؤلاء فاتبع كمية طبيبك لا نتيجة الحاسبة.</p>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>نصائح طبية عملية للترطيب</span></h2>
            <ol class="steps">
                <li>ابدأ يومك بكوب ماء، واجعل زجاجة الماء أمامك في العمل.</li>
                <li><strong>لمرضى السكري:</strong> ارتفاع سكر الدم يزيد التبول والعطش؛ فالماء هو المشروب الأفضل، وتجنب العصائر والمشروبات الغازية المحلاة التي ترفع السكر بسرعة.</li>
                <li><strong>في رمضان:</strong> وزّع الماء على فترات بين الإفطار والسحور بدل شرب كمية كبيرة دفعة واحدة، وقلل الأطعمة شديدة الملوحة والمشروبات الغنية بالكافيين في السحور.</li>
                <li><strong>القهوة والشاي:</strong> تُحسب من السوائل؛ فقد أظهرت دراسة في مجلة PLoS One أن 4 أكواب قهوة معتدلة يومياً رطّبت الجسم بقدر مماثل للماء.</li>
                <li><strong>لإدارة الوزن:</strong> وجدت تجربة عشوائية أن شرب نحو 500 مل من الماء قبل الوجبات مع نظام منخفض السعرات زاد خسارة الوزن بشكل متواضع لدى البالغين في منتصف العمر وكبار السن. احسب سعراتك عبر <a href="{calc:tdee}">حاسبة السعرات TDEE</a>.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>أطعمة غنية بالماء من دليلنا الغذائي</span></h2>
            <p>يأتي جزء من ماء جسمك من الطعام. هذه الأصناف تحتوي على نسبة عالية من الماء مع سعرات قليلة:</p>
            <div class="food-links">
                <a href="{food:watermelon}">البطيخ</a><a href="{food:cucumber}">الخيار</a><a href="{food:strawberry}">الفراولة</a>
                <a href="{food:orange}">البرتقال</a><a href="{food:zucchini}">الكوسا</a><a href="{food:tomato}">الطماطم</a>
                <a href="{food:spinach}">السبانخ</a><a href="{food:kefir}">الكفير</a>
            </div>
            <p>وتابع باقي مؤشراتك الصحية عبر <a href="{calc:bmi}">حاسبة مؤشر كتلة الجسم</a> و<a href="{calc:whtr}">حاسبة نسبة الخصر إلى الطول</a>، أو تصفّح <a href="{site:/foods.html}">دليل الأطعمة</a>.</p>
''',
            'faq': [
                ('كم لتراً من الماء يجب أن أشرب يومياً؟', 'توصي EFSA بـ2.0 لتر يومياً للنساء و2.5 لتر للرجال من كل المصادر، يأتي نحو 80% منها من المشروبات. وحسب الوزن يحتاج البالغ عادة 30 إلى 35 مل لكل كغ، ويزيد الاحتياج مع التمرين والحر.'),
                ('هل يُحسب الشاي والقهوة من شرب الماء؟', 'نعم، فالقهوة والشاي بكميات معتدلة يرطبان الجسم. لكن قلل السكر المضاف، وتجنب الإفراط في الكافيين مساءً.'),
                ('هل شرب الماء يساعد على إنقاص الوزن؟', 'يساعد بشكل متواضع: شرب نحو 500 مل قبل الوجبات مع نظام منخفض السعرات زاد خسارة الوزن في تجربة عشوائية، كما أن استبدال المشروبات المحلاة بالماء يقلل السعرات اليومية.'),
                ('هل يمكن أن أشرب ماء أكثر من اللازم؟', 'نعم، فالإفراط الشديد في وقت قصير قد يخفض صوديوم الدم. ومرضى القلب والكلى والكبد قد يحتاجون إلى تقييد السوائل حسب تعليمات الطبيب.'),
                ('كيف أعرف أنني أشرب كمية كافية من الماء؟', 'أبسط علامة هي لون البول الأصفر الفاتح وتكرار التبول بشكل طبيعي خلال اليوم. البول الداكن والصداع والتعب قد تكون علامات نقص السوائل.'),
                ('هل يحتاج مريض السكري إلى ماء أكثر؟', 'ارتفاع السكر يزيد فقدان الماء بالبول، لذلك يحتاج مريض السكري إلى الانتظام في شرب الماء واختياره بدل المشروبات المحلاة، ما لم يقيد طبيبه السوائل لسبب آخر.'),
            ],
            'disclaimer': 'هذه الحاسبة أداة تقدير تثقيفية للبالغين الأصحاء. إذا كنت مصاباً بقصور القلب أو أمراض الكلى أو الكبد، أو طلب منك طبيبك تقييد السوائل، فاتبع تعليماته لا نتيجة الحاسبة.',
        },
        'en': {
            'title': 'Water Intake Calculator: How Much Water a Day? | WiBo Health',
            'desc': 'How much water should you drink a day? Calculate your needs by weight and activity and compare them with EFSA values for men, women and pregnancy.',
            'h1': 'Water Intake Calculator: How Much Water Do You Need a Day?',
            'crumb': 'Water calculator',
            'cat': 'Medical calculator · Fluids and hydration',
            'short': 'Daily water intake',
            'blurb': 'The right amount of fluid for your weight and activity.',
            'about': [{'name': 'Hydration'}, {'name': 'Dehydration', 'condition': True}],
            'lead': 'Water makes up more than half of an adult’s body weight, and every organ depends on it. This tool estimates your daily fluid needs from your weight and physical activity and shows the official reference values of the European Food Safety Authority (EFSA) alongside, so you know in numbers how many glasses you actually need.',
            'ui': {
                'card_title': 'Calculate your water needs', 'lbl_sex': 'Sex', 'male': 'Male', 'female': 'Female',
                'lbl_weight': 'Weight (kg)', 'ph_weight': 'e.g. 75',
                'lbl_activity': 'Exercise or daily exertion', 'acts': [
                    'No exercise / desk job', '30 minutes of moderate activity (+350 ml)', '60 minutes of active training (+650 ml)',
                    '90+ minutes or hot weather (+1000 ml)'],
                'lbl_status': 'Pregnancy and breastfeeding (women)', 'status_opts': ['Not applicable', 'Pregnant (+300 ml)', 'Breastfeeding (+700 ml)'],
                'btn': 'Calculate my water needs', 'res_heading': 'Your estimated daily fluid needs',
                'cups': '{a} to {b} glasses (250 ml)',
                'efsa_label': 'EFSA reference for total water', 'efsa_sub': 'from drinks and food combined',
                'drinks_label': 'Of which from drinks, approx.', 'drinks_sub': 'about 80% of the total',
                'tip': 'Spread your drinking across the day rather than waiting for thirst, and use pale-yellow urine as your guide. Moderate tea and coffee count as fluid; swap sugary drinks for water.',
                'tip_heavy': 'At higher body weights the “ml per kg” rule overestimates; treat the lower end of the range or the EFSA reference as your starting point and adjust to thirst and urine colour.',
            },
            'body': '''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Why does your body need water?</span></h2>
            <p>Water makes up about 50 to 60% of an adult’s body weight and is the medium for almost every vital process: it carries nutrients and oxygen in the blood, regulates body temperature through sweat, removes waste through the kidneys and lubricates joints and membranes. The body does not store water, so what we lose every day through urine, sweat and breathing has to be replaced continuously.</p>
            <p>Even mild dehydration, losing about 1–2% of body weight as water, can be linked to headache, fatigue, poorer concentration and lower exercise performance, as a review in Nutrition Reviews describes.</p>

            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>How does the calculator estimate your water needs?</span></h2>
            <p>The calculator combines two approaches:</p>
            <ol class="steps">
                <li><strong>The weight-based clinical rule:</strong> 30 to 35 ml per kilogram of body weight, a common rule of thumb in nutrition practice, plus extra water for exercise depending on duration and intensity.</li>
                <li><strong>The European reference value (EFSA):</strong> shown for comparison. It is an “adequate intake” for total water from drinks and food together.</li>
            </ol>
            <p class="formula-box">Water need (L) = weight × (0.030 to 0.035) + exercise water + (0.3 if pregnant or 0.7 if breastfeeding)</p>
            <p><strong>Worked example:</strong> a man who weighs 75 kg and does 30 minutes of moderate activity. 75 × 30 = 2,250 ml and 75 × 35 = 2,625 ml; adding 350 ml for exercise gives a range of <strong>2.6 to 3.0 litres a day</strong>, or about 10 to 12 glasses. The EFSA reference for men is 2.5 litres from all sources, about 2.0 litres of it from drinks.</p>

            <h2 class="section-title"><i class="fas fa-table"></i> <span>EFSA reference values for water</span></h2>
            <p>In 2010 the European Food Safety Authority set an “adequate intake” for total daily water. Usually 20 to 30% comes from food and the rest from drinks:</p>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>Group</th><th>Total water per day</th><th>From drinks, approx. (80%)</th></tr></thead>
                <tbody>
                    <tr><td>Children 4–8 years</td><td>1.6 L</td><td>1.3 L</td></tr>
                    <tr><td>Boys 9–13 years</td><td>2.1 L</td><td>1.7 L</td></tr>
                    <tr><td>Girls 9–13 years</td><td>1.9 L</td><td>1.5 L</td></tr>
                    <tr><td>Women (14 and over)</td><td>2.0 L</td><td>1.6 L</td></tr>
                    <tr><td>Men (14 and over)</td><td>2.5 L</td><td>2.0 L</td></tr>
                    <tr><td>Pregnancy</td><td>2.3 L</td><td>1.8 L</td></tr>
                    <tr><td>Breastfeeding</td><td>2.7 L</td><td>2.2 L</td></tr>
                </tbody>
            </table></div>
            <p>These values apply to moderate temperatures and moderate activity. In hot weather, such as a Gulf summer, or with long training sessions, needs rise clearly.</p>

            <h2 class="section-title"><i class="fas fa-person-running"></i> <span>Water and exercise</span></h2>
            <p>The American College of Sports Medicine (ACSM) advises keeping sweat losses during exercise below 2% of body weight. The simplest way to know your needs is to weigh yourself before and after training: replace each kilogram lost with about <strong>1.5 litres</strong> of fluid, spread over the following hours. For sessions longer than an hour with heavy sweating, a drink containing sodium helps.</p>

            <h2 class="section-title"><i class="fas fa-eye"></i> <span>Are you drinking enough? Signs of dehydration</span></h2>
            <ul class="check-list">
                <li><strong>Urine colour:</strong> pale yellow (straw-coloured) means good hydration; dark yellow means you need more water.</li>
                <li><strong>Thirst and dry mouth:</strong> relatively late signals, and weaker in older adults, who benefit from a regular drinking schedule.</li>
                <li><strong>Headache, fatigue and dizziness on standing:</strong> can be signs of dehydration, especially in the heat.</li>
                <li><strong>Infrequent urination:</strong> fewer than 4 times a day can point to low fluid intake.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>When to be careful with large amounts of water</span></h2>
            <p>Drinking very large amounts in a short time can lower blood sodium (hyponatraemia), a serious condition sometimes seen in long endurance events. More importantly, some patients need <strong>fluid restriction</strong> on medical advice, such as people with heart failure, advanced kidney failure or dialysis, liver cirrhosis or SIADH. If that applies to you, follow your doctor’s amount, not the calculator.</p>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>Practical hydration tips</span></h2>
            <ol class="steps">
                <li>Start your day with a glass of water and keep a bottle in sight at work.</li>
                <li><strong>For people with diabetes:</strong> high blood sugar increases urination and thirst. Water is the best drink; avoid juices and sugary soft drinks that raise blood sugar quickly.</li>
                <li><strong>During Ramadan:</strong> spread water between iftar and suhoor instead of drinking a large amount at once, and limit very salty foods and caffeinated drinks at suhoor.</li>
                <li><strong>Coffee and tea:</strong> they count as fluid. A study in PLoS One found that four moderate cups of coffee a day hydrated people about as well as water.</li>
                <li><strong>For weight management:</strong> a randomised trial found that drinking about 500 ml of water before meals on a low-calorie diet modestly increased weight loss in middle-aged and older adults. Work out your calories with the <a href="{calc:tdee}">TDEE calculator</a>.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>Water-rich foods from our food guide</span></h2>
            <p>Part of your water comes from food. These foods are high in water and low in calories:</p>
            <div class="food-links">
                <a href="{food:watermelon}">Watermelon</a><a href="{food:cucumber}">Cucumber</a><a href="{food:strawberry}">Strawberry</a>
                <a href="{food:orange}">Orange</a><a href="{food:zucchini}">Courgette</a><a href="{food:tomato}">Tomato</a>
                <a href="{food:spinach}">Spinach</a><a href="{food:kefir}">Kefir</a>
            </div>
            <p>Check your other health markers with the <a href="{calc:bmi}">BMI calculator</a> and the <a href="{calc:whtr}">waist-to-height ratio calculator</a>, or browse the <a href="{site:/foods.html}">food guide</a>.</p>
''',
            'faq': [
                ('How many litres of water should I drink a day?', 'EFSA recommends 2.0 litres a day for women and 2.5 litres for men from all sources, about 80% of it from drinks. By body weight, adults usually need 30 to 35 ml per kg, more with exercise and heat.'),
                ('Do tea and coffee count towards my water intake?', 'Yes. Moderate amounts of coffee and tea hydrate the body. Keep added sugar low and avoid too much caffeine in the evening.'),
                ('Does drinking water help with weight loss?', 'Modestly. Drinking about 500 ml before meals on a low-calorie diet increased weight loss in a randomised trial, and replacing sugary drinks with water lowers daily calories.'),
                ('Can I drink too much water?', 'Yes. Very large amounts in a short time can lower blood sodium. People with heart, kidney or liver disease may need to restrict fluids on their doctor’s advice.'),
                ('How do I know if I am drinking enough water?', 'The simplest sign is pale-yellow urine and passing urine normally through the day. Dark urine, headache and fatigue can be signs of low fluid intake.'),
                ('Do people with diabetes need more water?', 'High blood sugar increases water loss through urine, so people with diabetes should drink regularly and choose water over sugary drinks, unless their doctor restricts fluids for another reason.'),
            ],
            'disclaimer': 'This calculator is an educational estimate for healthy adults. If you have heart failure, kidney or liver disease, or your doctor has told you to restrict fluids, follow their instructions rather than the calculator.',
        },
        'nl': {
            'title': 'Waterbehoefte berekenen: hoeveel water per dag? | WiBo Health',
            'desc': 'Hoeveel water moet je per dag drinken? Bereken je behoefte op basis van gewicht en activiteit en vergelijk met de EFSA-waarden voor mannen en vrouwen.',
            'h1': 'Waterbehoefte berekenen: hoeveel water heb je per dag nodig?',
            'crumb': 'Watercalculator',
            'cat': 'Medische calculator · Vocht en hydratatie',
            'short': 'Dagelijkse waterbehoefte',
            'blurb': 'De juiste hoeveelheid vocht voor je gewicht en activiteit.',
            'about': [{'name': 'Hydratatie'}, {'name': 'Uitdroging', 'condition': True}],
            'lead': 'Water vormt meer dan de helft van het lichaamsgewicht van een volwassene, en elk orgaan heeft het nodig. Deze tool schat je dagelijkse vochtbehoefte op basis van je gewicht en lichamelijke activiteit, en toont daarnaast de officiële referentiewaarden van de Europese voedselveiligheidsautoriteit (EFSA). Zo weet je in cijfers hoeveel glazen je echt nodig hebt.',
            'ui': {
                'card_title': 'Bereken je waterbehoefte', 'lbl_sex': 'Geslacht', 'male': 'Man', 'female': 'Vrouw',
                'lbl_weight': 'Gewicht (kg)', 'ph_weight': 'bijv. 75',
                'lbl_activity': 'Sport of dagelijkse inspanning', 'acts': [
                    'Geen sport / kantoorwerk', '30 minuten matige activiteit (+350 ml)', '60 minuten actieve training (+650 ml)',
                    '90+ minuten of warm weer (+1000 ml)'],
                'lbl_status': 'Zwangerschap en borstvoeding (vrouwen)', 'status_opts': ['Niet van toepassing', 'Zwanger (+300 ml)', 'Borstvoeding (+700 ml)'],
                'btn': 'Bereken mijn waterbehoefte', 'res_heading': 'Je geschatte dagelijkse vochtbehoefte',
                'cups': '{a} tot {b} glazen (250 ml)',
                'efsa_label': 'EFSA-referentie voor totaal water', 'efsa_sub': 'uit dranken en voeding samen',
                'drinks_label': 'Waarvan uit dranken, ca.', 'drinks_sub': 'ongeveer 80% van het totaal',
                'tip': 'Verdeel het drinken over de dag in plaats van op dorst te wachten, en gebruik lichtgele urine als richtlijn. Thee en koffie met mate tellen mee als vocht; vervang suikerhoudende dranken door water.',
                'tip_heavy': 'Bij een hoger lichaamsgewicht overschat de regel “ml per kg”; neem de onderkant van het bereik of de EFSA-referentie als vertrekpunt en stem af op dorst en urinekleur.',
            },
            'body': '''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Waarom heeft je lichaam water nodig?</span></h2>
            <p>Water vormt ongeveer 50 tot 60% van het lichaamsgewicht van een volwassene en is het medium voor bijna elk levensproces: het vervoert voedingsstoffen en zuurstof in het bloed, regelt je lichaamstemperatuur via zweet, voert afvalstoffen af via de nieren en houdt gewrichten en slijmvliezen soepel. Het lichaam slaat geen water op, dus wat we dagelijks verliezen via urine, zweet en ademhaling moet steeds worden aangevuld.</p>
            <p>Zelfs lichte uitdroging, een verlies van ongeveer 1–2% van het lichaamsgewicht aan water, kan samengaan met hoofdpijn, vermoeidheid, minder concentratie en lagere sportprestaties, zoals een overzichtsartikel in Nutrition Reviews beschrijft.</p>

            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>Hoe berekent de calculator je waterbehoefte?</span></h2>
            <p>De calculator combineert twee benaderingen:</p>
            <ol class="steps">
                <li><strong>De klinische vuistregel op basis van gewicht:</strong> 30 tot 35 ml per kilogram lichaamsgewicht, een gangbare vuistregel in de voedingspraktijk, plus extra water voor sport afhankelijk van duur en intensiteit.</li>
                <li><strong>De Europese referentiewaarde (EFSA):</strong> ter vergelijking. Dit is een “adequate inname” voor totaal water uit dranken en voeding samen.</li>
            </ol>
            <p class="formula-box">Waterbehoefte (L) = gewicht × (0,030 tot 0,035) + water voor sport + (0,3 bij zwangerschap of 0,7 bij borstvoeding)</p>
            <p><strong>Rekenvoorbeeld:</strong> een man van 75 kg die 30 minuten matig actief is. 75 × 30 = 2250 ml en 75 × 35 = 2625 ml; met 350 ml voor de training wordt het bereik <strong>2,6 tot 3,0 liter per dag</strong>, ongeveer 10 tot 12 glazen. De EFSA-referentie voor mannen is 2,5 liter uit alle bronnen, waarvan ongeveer 2,0 liter uit dranken.</p>

            <h2 class="section-title"><i class="fas fa-table"></i> <span>EFSA-referentiewaarden voor water</span></h2>
            <p>In 2010 stelde de Europese voedselveiligheidsautoriteit een “adequate inname” vast voor de totale dagelijkse hoeveelheid water. Meestal komt 20 tot 30% uit voeding en de rest uit dranken:</p>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>Groep</th><th>Totaal water per dag</th><th>Uit dranken, ca. (80%)</th></tr></thead>
                <tbody>
                    <tr><td>Kinderen 4–8 jaar</td><td>1,6 L</td><td>1,3 L</td></tr>
                    <tr><td>Jongens 9–13 jaar</td><td>2,1 L</td><td>1,7 L</td></tr>
                    <tr><td>Meisjes 9–13 jaar</td><td>1,9 L</td><td>1,5 L</td></tr>
                    <tr><td>Vrouwen (vanaf 14 jaar)</td><td>2,0 L</td><td>1,6 L</td></tr>
                    <tr><td>Mannen (vanaf 14 jaar)</td><td>2,5 L</td><td>2,0 L</td></tr>
                    <tr><td>Zwangerschap</td><td>2,3 L</td><td>1,8 L</td></tr>
                    <tr><td>Borstvoeding</td><td>2,7 L</td><td>2,2 L</td></tr>
                </tbody>
            </table></div>
            <p>Deze waarden gelden bij gematigde temperaturen en gemiddelde activiteit. Bij warm weer of lange trainingen ligt de behoefte duidelijk hoger.</p>

            <h2 class="section-title"><i class="fas fa-person-running"></i> <span>Water en sport</span></h2>
            <p>Het American College of Sports Medicine (ACSM) adviseert om zweetverlies tijdens het sporten onder 2% van het lichaamsgewicht te houden. De eenvoudigste manier om je behoefte te kennen: weeg jezelf voor en na de training en vul elke verloren kilogram aan met ongeveer <strong>1,5 liter</strong> vocht, verspreid over de uren daarna. Bij trainingen langer dan een uur met veel zweten helpt een drank met natrium.</p>

            <h2 class="section-title"><i class="fas fa-eye"></i> <span>Drink je genoeg? Signalen van uitdroging</span></h2>
            <ul class="check-list">
                <li><strong>Kleur van de urine:</strong> lichtgeel (strokleurig) betekent goed gehydrateerd; donkergeel betekent dat je meer water nodig hebt.</li>
                <li><strong>Dorst en een droge mond:</strong> vrij late signalen, en zwakker bij ouderen, die baat hebben bij een vast drinkschema.</li>
                <li><strong>Hoofdpijn, vermoeidheid en duizeligheid bij opstaan:</strong> kunnen wijzen op uitdroging, zeker bij warmte.</li>
                <li><strong>Weinig plassen:</strong> minder dan 4 keer per dag kan wijzen op te weinig vocht.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Wanneer moet je oppassen met veel water?</span></h2>
            <p>Heel veel drinken in korte tijd kan het natriumgehalte in het bloed verlagen (hyponatriëmie), een ernstige aandoening die soms voorkomt bij lange duurwedstrijden. Belangrijker nog: sommige patiënten hebben op medisch advies een <strong>vochtbeperking</strong>, zoals mensen met hartfalen, ernstige nierschade of dialyse, levercirrose of SIADH. Geldt dat voor jou, volg dan de hoeveelheid van je arts en niet die van de calculator.</p>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>Praktische tips voor voldoende vocht</span></h2>
            <ol class="steps">
                <li>Begin de dag met een glas water en houd een fles in zicht op je werk.</li>
                <li><strong>Bij diabetes:</strong> een hoge bloedsuiker zorgt voor meer plassen en dorst. Water is de beste drank; vermijd sappen en frisdranken met suiker die je bloedsuiker snel laten stijgen.</li>
                <li><strong>Tijdens de ramadan:</strong> verdeel het water tussen iftar en suhoor in plaats van veel in één keer te drinken, en beperk erg zout eten en cafeïnehoudende dranken bij de suhoor.</li>
                <li><strong>Koffie en thee:</strong> tellen mee als vocht. Een studie in PLoS One vond dat vier matige koppen koffie per dag ongeveer even goed hydrateerden als water.</li>
                <li><strong>Bij gewichtsbeheersing:</strong> in een gerandomiseerde studie leidde ongeveer 500 ml water voor de maaltijden bij een caloriearm dieet tot iets meer gewichtsverlies bij volwassenen van middelbare en oudere leeftijd. Bereken je calorieën met de <a href="{calc:tdee}">TDEE-calculator</a>.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>Waterrijke voeding uit onze voedingsgids</span></h2>
            <p>Een deel van je water krijg je binnen via voeding. Deze producten bevatten veel water en weinig calorieën:</p>
            <div class="food-links">
                <a href="{food:watermelon}">Watermeloen</a><a href="{food:cucumber}">Komkommer</a><a href="{food:strawberry}">Aardbei</a>
                <a href="{food:orange}">Sinaasappel</a><a href="{food:zucchini}">Courgette</a><a href="{food:tomato}">Tomaat</a>
                <a href="{food:spinach}">Spinazie</a><a href="{food:kefir}">Kefir</a>
            </div>
            <p>Check ook je andere gezondheidswaarden met de <a href="{calc:bmi}">BMI-calculator</a> en de <a href="{calc:whtr}">taille-lengteratio calculator</a>, of blader door de <a href="{site:/foods.html}">voedingsgids</a>.</p>
''',
            'faq': [
                ('Hoeveel liter water moet ik per dag drinken?', 'EFSA adviseert 2,0 liter per dag voor vrouwen en 2,5 liter voor mannen uit alle bronnen, waarvan ongeveer 80% uit dranken. Op basis van gewicht hebben volwassenen meestal 30 tot 35 ml per kg nodig, meer bij sport en warmte.'),
                ('Tellen thee en koffie mee voor mijn waterinname?', 'Ja. Koffie en thee met mate hydrateren het lichaam. Houd toegevoegde suiker laag en vermijd veel cafeïne in de avond.'),
                ('Helpt water drinken bij afvallen?', 'In beperkte mate. Ongeveer 500 ml voor de maaltijden bij een caloriearm dieet gaf in een gerandomiseerde studie meer gewichtsverlies, en suikerhoudende dranken vervangen door water verlaagt je dagelijkse calorieën.'),
                ('Kan ik te veel water drinken?', 'Ja. Heel veel in korte tijd kan het natrium in je bloed verlagen. Mensen met een hart-, nier- of leveraandoening hebben soms een vochtbeperking op advies van hun arts.'),
                ('Hoe weet ik of ik genoeg water drink?', 'Het eenvoudigste signaal is lichtgele urine en normaal plassen over de dag. Donkere urine, hoofdpijn en vermoeidheid kunnen wijzen op te weinig vocht.'),
                ('Hebben mensen met diabetes meer water nodig?', 'Een hoge bloedsuiker verhoogt het waterverlies via de urine. Mensen met diabetes drinken daarom best regelmatig en kiezen water boven suikerhoudende dranken, tenzij hun arts om een andere reden vocht beperkt.'),
            ],
            'disclaimer': 'Deze calculator geeft een educatieve schatting voor gezonde volwassenen. Heb je hartfalen, een nier- of leveraandoening, of heeft je arts je gevraagd vocht te beperken? Volg dan zijn of haar instructies in plaats van de calculator.',
        },
    },
}
