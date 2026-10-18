"""TDEE / BMR calorie calculator content (AR / EN / NL).
Worked example (Mifflin-St Jeor): woman, 34 y, 68 kg, 165 cm, PAL 1.55 -> BMR 1380, TDEE 2139, -20% 1712, +15% 2460;
macros on 1712 kcal: protein 122 g (488 kcal), fat 48 g (428 kcal), carbs 199 g (796 kcal)."""

TDEE = {
    'key': 'tdee',
    'slug': 'tdee-calculator',
    'icon': 'fa-fire-flame-curved',
    'badge': 'Mifflin-St Jeor 1990',
    'published': '2026-10-18',
    'modified': '2026-10-18',
    'references': [
        'Mifflin MD, St Jeor ST, Hill LA, Scott BJ, Daugherty SA, Koh YO. A new predictive equation for resting energy expenditure in healthy individuals. Am J Clin Nutr. 1990;51(2):241-247.',
        'Frankenfield D, Roth-Yousey L, Compher C. Comparison of predictive equations for resting metabolic rate in healthy nonobese and obese adults: a systematic review. J Am Diet Assoc. 2005;105(5):775-789.',
        'FAO/WHO/UNU. Human energy requirements. Report of a Joint FAO/WHO/UNU Expert Consultation. Rome: FAO; 2004.',
        'Hall KD, Sacks G, Chandramohan D, et al. Quantification of the effect of energy imbalance on bodyweight. Lancet. 2011;378(9793):826-837.',
        'Morton RW, Murphy KT, McKellar SR, et al. A systematic review, meta-analysis and meta-regression of the effect of protein supplementation on resistance training-induced gains in muscle mass and strength in healthy adults. Br J Sports Med. 2018;52(6):376-384.',
        'EFSA Panel on Dietetic Products, Nutrition, and Allergies (NDA). Scientific Opinion on Dietary Reference Values for fats. EFSA Journal. 2010;8(3):1461.',
    ],
    'content': {
        'ar': {
            'title': 'حاسبة السعرات الحرارية اليومية TDEE ومعدل الأيض BMR | WiBo Health',
            'desc': 'احسب سعراتك اليومية (TDEE) ومعدل الأيض الأساسي (BMR) بمعادلة ميفلين-سانت جور، مع سعرات خسارة الوزن الآمنة وتوزيع البروتين والدهون والكربوهيدرات.',
            'h1': 'حاسبة السعرات الحرارية اليومية (TDEE) ومعدل الأيض الأساسي (BMR)',
            'crumb': 'حاسبة السعرات TDEE',
            'cat': 'حاسبة طبية · الطاقة والتغذية',
            'short': 'السعرات اليومية TDEE',
            'blurb': 'احتياجك من السعرات للثبات والتنحيف والبناء العضلي.',
            'about': [{'name': 'معدل الأيض الأساسي'}, {'name': 'إجمالي استهلاك الطاقة اليومي'}, {'name': 'السمنة', 'condition': True}],
            'lead': 'كم سعرة حرارية يحتاج جسمك يومياً؟ تحسب هذه الأداة معدل الأيض الأساسي (BMR) بمعادلة ميفلين-سانت جور، وهي الأدق بين معادلات التقدير للبالغين، ثم تضربه في معامل نشاطك لتعطيك إجمالي استهلاك الطاقة اليومي (TDEE)، مع سعرات خسارة الوزن الآمنة وزيادة الكتلة العضلية وتوزيع الماكروز.',
            'ui': {
                'card_title': 'احسب سعراتك اليومية', 'lbl_sex': 'الجنس', 'male': 'ذكر', 'female': 'أنثى',
                'lbl_age': 'العمر (سنوات)', 'lbl_weight': 'الوزن (كغ)', 'lbl_height': 'الطول (سم)',
                'ph_age': 'مثال: 34', 'ph_weight': 'مثال: 68', 'ph_height': 'مثال: 165',
                'lbl_activity': 'مستوى النشاط البدني', 'acts': [
                    'خامل: عمل مكتبي دون تمارين (×1.2)', 'نشاط خفيف: تمارين 1–3 أيام أسبوعياً (×1.375)',
                    'نشاط معتدل: تمارين 3–5 أيام أسبوعياً (×1.55)', 'نشاط عالٍ: تمارين مكثفة 6–7 أيام (×1.725)',
                    'نشاط شاق جداً: رياضي محترف أو عمل بدني شاق (×1.9)'],
                'btn': 'احسب احتياجي من السعرات', 'res_heading': 'إجمالي استهلاك الطاقة اليومي (TDEE)',
                'kcal_day': 'سعرة حرارية يومياً للحفاظ على وزنك الحالي',
                'bmr_label': 'معدل الأيض الأساسي (BMR)', 'bmr_sub': 'ما يحرقه جسمك في الراحة التامة',
                'deficit_label': 'لخسارة الدهون (عجز 20%)', 'deficit_sub': 'لا ينزل عن معدل الأيض الأساسي',
                'surplus_label': 'لبناء العضلات (فائض 15%)', 'surplus_sub': 'مع تمارين المقاومة',
                'macros_header': 'توزيع مقترح للماكروز على سعرات خسارة الدهون',
                'protein': 'البروتين (1.8 غ/كغ)', 'fat': 'الدهون (25% من الطاقة)', 'carbs': 'الكربوهيدرات (الباقي)',
                'tip': 'هذه أرقام تقديرية: راقب وزنك أسبوعين ثم عدّل السعرات بمقدار 100–200 سعرة حسب النتيجة. اختر كربوهيدرات منخفضة المؤشر الجلايسيمي وغنية بالألياف.',
                'tip_lowcarb': 'سعرات العجز منخفضة مقارنة بهدف البروتين، فبقيت حصة صغيرة للكربوهيدرات. لا تنزل أكثر من ذلك دون إشراف أخصائي تغذية، وخاصة إذا كنت تتناول أدوية للسكري.',
            },
            'body': '''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>ما الفرق بين BMR وTDEE؟</span></h2>
            <p><strong>معدل الأيض الأساسي (BMR)</strong> هو الطاقة التي يحتاجها جسمك في الراحة التامة ليبقى حياً: نبض القلب والتنفس وعمل الدماغ والكبد والكلى وتجديد الخلايا والحفاظ على حرارة الجسم. ويمثل عادة الجزء الأكبر من استهلاك الطاقة اليومي لدى معظم الناس قليلي الحركة.</p>
            <p><strong>إجمالي استهلاك الطاقة اليومي (TDEE)</strong> هو كل ما تحرقه خلال 24 ساعة، ويتكون من ثلاثة أجزاء:</p>
            <ul class="check-list">
                <li><strong>معدل الأيض الأساسي:</strong> الحصة الأكبر.</li>
                <li><strong>التأثير الحراري للطعام:</strong> نحو 10% من السعرات، وهي الطاقة اللازمة لهضم الطعام وامتصاصه، وتكون أعلى مع البروتين.</li>
                <li><strong>طاقة النشاط البدني:</strong> التمارين، إضافة إلى الحركة اليومية غير الرياضية كالمشي والوقوف والأعمال المنزلية، وهي الجزء الأكثر تفاوتاً بين الناس.</li>
            </ul>
            <p>إذا أكلت سعرات تساوي TDEE يبقى وزنك ثابتاً تقريباً، وإذا أكلت أقل منها خسرت وزناً، وإذا أكلت أكثر منها زاد وزنك.</p>

            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>معادلة ميفلين-سانت جور: كيف تحسب الأداة سعراتك؟</span></h2>
            <p>نُشرت معادلة ميفلين-سانت جور عام 1990، ووجدت مراجعة منهجية لاحقة للجمعية الأمريكية للتغذية أنها الأكثر قدرة على التنبؤ بمعدل الأيض أثناء الراحة ضمن هامش 10% من القيمة المقاسة فعلياً، لدى البالغين من ذوي الوزن الطبيعي والسمنة على حد سواء:</p>
            <p class="formula-box">للرجال: BMR = (10 × الوزن بالكغ) + (6.25 × الطول بالسم) − (5 × العمر) + 5</p>
            <p class="formula-box">للنساء: BMR = (10 × الوزن بالكغ) + (6.25 × الطول بالسم) − (5 × العمر) − 161</p>
            <p>ثم: <strong>TDEE = BMR × معامل النشاط</strong>.</p>
            <p><strong>مثال عملي:</strong> امرأة عمرها 34 عاماً، وزنها 68 كغ وطولها 165 سم، تتمرن 3–5 أيام أسبوعياً. معدل الأيض الأساسي = 680 + 1031.25 − 170 − 161 = <strong>1380 سعرة</strong>، وإجمالي الاستهلاك = 1380 × 1.55 = <strong>2139 سعرة يومياً</strong>. لخسارة الدهون بعجز 20% تحتاج نحو <strong>1712 سعرة</strong>، ولبناء العضلات بفائض 15% نحو <strong>2460 سعرة</strong>.</p>

            <h2 class="section-title"><i class="fas fa-table"></i> <span>جدول معاملات النشاط البدني</span></h2>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>مستوى النشاط</th><th>الوصف</th><th>المعامل</th></tr></thead>
                <tbody>
                    <tr><td>خامل</td><td>عمل مكتبي، مشي قليل، دون تمارين منتظمة</td><td>1.2</td></tr>
                    <tr><td>نشاط خفيف</td><td>تمارين خفيفة أو مشي سريع 1–3 أيام أسبوعياً</td><td>1.375</td></tr>
                    <tr><td>نشاط معتدل</td><td>تمارين متوسطة الشدة 3–5 أيام أسبوعياً</td><td>1.55</td></tr>
                    <tr><td>نشاط عالٍ</td><td>تمارين مكثفة 6–7 أيام أسبوعياً</td><td>1.725</td></tr>
                    <tr><td>نشاط شاق جداً</td><td>رياضي محترف، تدريب مرتين يومياً، أو عمل بدني شاق</td><td>1.9</td></tr>
                </tbody>
            </table></div>
            <p>نصيحة: يبالغ معظم الناس في تقدير نشاطهم. إذا لم تكن متأكداً فاختر المستوى الأدنى، فالحساب لا يتضمن التمرين مرة أخرى؛ لا تضف السعرات التي تعرضها ساعتك الذكية فوق TDEE.</p>

            <h2 class="section-title"><i class="fas fa-weight-scale"></i> <span>كم سعرة تحتاج لخسارة الوزن بأمان؟</span></h2>
            <p>تقترح الأداة عجزاً معتدلاً بنسبة 20% من TDEE، ولا تنزل أبداً عن معدل الأيض الأساسي. هذا العجز يؤدي غالباً إلى خسارة نحو 0.5 إلى 1 كغ أسبوعياً في البداية، وهو المعدل الذي توصي به معظم الإرشادات الطبية للحفاظ على الكتلة العضلية.</p>
            <p>تذكّر أن القاعدة القديمة «كل 7700 سعرة = 1 كغ دهون» تبسيط مفرط؛ فقد أظهرت نماذج المعاهد الوطنية للصحة الأمريكية أن خسارة الوزن تتباطأ مع الوقت لأن الجسم الأخف يحرق طاقة أقل. لذلك أعد الحساب كلما خسرت 4–5 كغ.</p>
            <ul class="check-list">
                <li><strong>لا تتبع حميات أقل من 800 سعرة يومياً</strong> إلا تحت إشراف طبي مباشر.</li>
                <li><strong>مرضى السكري</strong> الذين يستخدمون الإنسولين أو أدوية السلفونيل يوريا معرضون لهبوط السكر عند تقليل الطعام، فنسّق خطتك مع طبيبك.</li>
                <li><strong>الحامل والمرضع</strong> لا تتبع عجزاً في السعرات إلا بتوجيه طبي.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-chart-pie"></i> <span>توزيع الماكروز: البروتين والدهون والكربوهيدرات</span></h2>
            <p>تحسب الأداة توزيعاً عملياً على سعرات خسارة الدهون:</p>
            <ul class="check-list">
                <li><strong>البروتين 1.8 غ لكل كغ من وزنك:</strong> وجد تحليل جامع منشور في المجلة البريطانية للطب الرياضي أن فائدة البروتين للكتلة العضلية مع تمارين المقاومة تستقر عند نحو 1.6 غ/كغ، مع حد أعلى محتمل يقارب 2.2 غ/كغ. <em>مرضى الكلى المزمنة يحتاجون كميات أقل يحددها الطبيب.</em></li>
                <li><strong>الدهون 25% من الطاقة:</strong> ضمن النطاق الذي توصي به الهيئة الأوروبية لسلامة الأغذية (20–35%)، مع تفضيل زيت الزيتون والمكسرات والأسماك الدهنية.</li>
                <li><strong>الكربوهيدرات الباقي:</strong> من الحبوب الكاملة والبقوليات والخضار والفواكه، ويفضل اختيار الأصناف منخفضة المؤشر الجلايسيمي لاستقرار سكر الدم.</li>
            </ul>
            <p>في المثال السابق (1712 سعرة): بروتين 122 غ، ودهون 48 غ، وكربوهيدرات نحو 199 غ يومياً.</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>حدود الحساب</span></h2>
            <p>كل معادلات تقدير الأيض تعطي متوسطاً للمجموعات، وقد يختلف أيضك الفعلي بنحو 10% صعوداً أو نزولاً. وتقل الدقة لدى الرياضيين ذوي الكتلة العضلية الكبيرة، وكبار السن جداً، ومن يعانون اضطرابات الغدة الدرقية أو يتناولون أدوية تؤثر في الأيض. والمعادلة مصممة للبالغين؛ أما المراهقون فيحتاجون طاقة إضافية للنمو.</p>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>أطعمة تساعدك على بلوغ أهدافك</span></h2>
            <p>مصادر بروتين وألياف من دليلنا الغذائي، مع سعراتها ومؤشرها الجلايسيمي:</p>
            <div class="food-links">
                <a href="{food:grilled-chicken-breast}">صدر الدجاج المشوي</a><a href="{food:boiled-egg}">البيض المسلوق</a>
                <a href="{food:greek-yogurt}">الزبادي اليوناني</a><a href="{food:skyr-naturel}">السكير</a><a href="{food:lentils}">العدس</a>
                <a href="{food:quinoa}">الكينوا</a><a href="{food:brown-rice}">الأرز البني</a><a href="{food:sweet-potato}">البطاطا الحلوة</a>
                <a href="{food:walnuts}">عين الجمل</a><a href="{food:avocado}">الأفوكادو</a>
            </div>
            <p>ولتعرف هل وزنك الحالي ضمن النطاق الصحي أصلاً، ابدأ بـ<a href="{calc:bmi}">حاسبة مؤشر كتلة الجسم</a>، وتابع دهون البطن عبر <a href="{calc:whtr}">حاسبة نسبة الخصر إلى الطول</a>.</p>
''',
            'faq': [
                ('ما الفرق بين معدل الأيض الأساسي (BMR) وTDEE؟', 'معدل الأيض الأساسي هو ما يحرقه جسمك في الراحة التامة، أما TDEE فهو إجمالي ما تحرقه يومياً بعد إضافة هضم الطعام والحركة والتمارين. وتُبنى خطط التنحيف على TDEE لا على BMR.'),
                ('كم سعرة حرارية أحتاج يومياً لخسارة الوزن؟', 'اطرح نحو 20% من TDEE، على ألا تنزل عن معدل الأيض الأساسي. لامرأة TDEE لديها 2139 سعرة، يعني ذلك نحو 1712 سعرة يومياً.'),
                ('هل معادلة ميفلين-سانت جور دقيقة؟', 'هي الأدق بين المعادلات الشائعة للبالغين وفق مراجعة منهجية للجمعية الأمريكية للتغذية، لكنها تبقى تقديراً قد يبتعد عن قياسك الفعلي بنحو 10%. راقب وزنك أسبوعين وعدّل.'),
                ('لماذا توقف نزول وزني رغم أنني آكل أقل من TDEE؟', 'لأن الجسم الأخف يحرق طاقة أقل، ولأن احتباس الماء قد يخفي خسارة الدهون مؤقتاً. أعد الحساب بوزنك الجديد، وتابع محيط الخصر، وتأكد من دقة حساب ما تأكله.'),
                ('كم غراماً من البروتين أحتاج يومياً؟', 'الحد الأدنى للبالغين نحو 0.8 غ لكل كغ، ومع خسارة الوزن وتمارين المقاومة يفيد 1.6 إلى 2.2 غ/كغ للحفاظ على العضلات. مرضى الكلى يتبعون توصية طبيبهم.'),
                ('هل أضيف السعرات التي أحرقها في التمرين إلى TDEE؟', 'لا، فمعامل النشاط يشمل تمارينك المعتادة. إضافتها مرة أخرى تحسبها مرتين وتلغي العجز.'),
            ],
            'disclaimer': 'هذه الحاسبة أداة تقدير تثقيفية للبالغين الأصحاء، ولا تُغني عن خطة غذائية يضعها أخصائي. إذا كنت مصاباً بالسكري أو أمراض الكلى أو القلب، أو حاملاً أو مرضعاً، فاستشر طبيبك قبل تغيير سعراتك.',
        },
        'en': {
            'title': 'TDEE Calculator: Daily Calories & BMR | WiBo Health',
            'desc': 'Calculate your daily calories (TDEE) and BMR with the Mifflin-St Jeor equation, plus safe fat-loss calories and a protein, fat and carb split.',
            'h1': 'TDEE Calculator: Daily Calorie Needs and Basal Metabolic Rate (BMR)',
            'crumb': 'TDEE calculator',
            'cat': 'Medical calculator · Energy and nutrition',
            'short': 'Daily calories (TDEE)',
            'blurb': 'Calories to maintain, lose fat or build muscle.',
            'about': [{'name': 'Basal metabolic rate'}, {'name': 'Total daily energy expenditure'}, {'name': 'Obesity', 'condition': True}],
            'lead': 'How many calories does your body need each day? This tool estimates your basal metabolic rate (BMR) with the Mifflin-St Jeor equation, the most accurate of the common prediction equations for adults, then multiplies it by your activity level to give your total daily energy expenditure (TDEE), plus safe fat-loss and muscle-gain targets and a macro split.',
            'ui': {
                'card_title': 'Calculate your daily calories', 'lbl_sex': 'Sex', 'male': 'Male', 'female': 'Female',
                'lbl_age': 'Age (years)', 'lbl_weight': 'Weight (kg)', 'lbl_height': 'Height (cm)',
                'ph_age': 'e.g. 34', 'ph_weight': 'e.g. 68', 'ph_height': 'e.g. 165',
                'lbl_activity': 'Physical activity level', 'acts': [
                    'Sedentary: desk job, no exercise (×1.2)', 'Lightly active: exercise 1–3 days a week (×1.375)',
                    'Moderately active: exercise 3–5 days a week (×1.55)', 'Very active: hard exercise 6–7 days a week (×1.725)',
                    'Extremely active: athlete or heavy physical work (×1.9)'],
                'btn': 'Calculate my calories', 'res_heading': 'Total daily energy expenditure (TDEE)',
                'kcal_day': 'calories a day to maintain your current weight',
                'bmr_label': 'Basal metabolic rate (BMR)', 'bmr_sub': 'what your body burns at complete rest',
                'deficit_label': 'Fat loss (20% deficit)', 'deficit_sub': 'never below your BMR',
                'surplus_label': 'Muscle gain (15% surplus)', 'surplus_sub': 'with resistance training',
                'macros_header': 'Suggested macro split on your fat-loss calories',
                'protein': 'Protein (1.8 g/kg)', 'fat': 'Fat (25% of energy)', 'carbs': 'Carbohydrates (the rest)',
                'tip': 'These are estimates: track your weight for two weeks, then adjust by 100–200 calories. Choose low-GI, high-fibre carbohydrates.',
                'tip_lowcarb': 'Your deficit calories are low compared with your protein target, so little is left for carbohydrates. Do not go lower without a dietitian, especially if you take diabetes medication.',
            },
            'body': '''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>BMR vs TDEE: what is the difference?</span></h2>
            <p><strong>Basal metabolic rate (BMR)</strong> is the energy your body needs at complete rest just to stay alive: heartbeat, breathing, brain, liver and kidney function, cell renewal and keeping your body warm. For most people who are not very active it is the largest part of daily energy use.</p>
            <p><strong>Total daily energy expenditure (TDEE)</strong> is everything you burn in 24 hours. It has three parts:</p>
            <ul class="check-list">
                <li><strong>Basal metabolic rate:</strong> the largest share.</li>
                <li><strong>Thermic effect of food:</strong> about 10% of calories, the energy needed to digest and absorb food; it is higher for protein.</li>
                <li><strong>Activity energy:</strong> exercise plus everyday non-exercise movement such as walking, standing and housework. This part varies most between people.</li>
            </ul>
            <p>Eat about your TDEE and your weight stays roughly stable; eat less and you lose weight; eat more and you gain.</p>

            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>The Mifflin-St Jeor equation: how the calculator works</span></h2>
            <p>The Mifflin-St Jeor equation was published in 1990. A later systematic review for the American Dietetic Association found it was the equation most likely to predict resting metabolic rate within 10% of the measured value in both non-obese and obese adults:</p>
            <p class="formula-box">Men: BMR = (10 × weight in kg) + (6.25 × height in cm) − (5 × age) + 5</p>
            <p class="formula-box">Women: BMR = (10 × weight in kg) + (6.25 × height in cm) − (5 × age) − 161</p>
            <p>Then: <strong>TDEE = BMR × activity factor</strong>.</p>
            <p><strong>Worked example:</strong> a 34-year-old woman who weighs 68 kg, is 165 cm tall and exercises 3–5 days a week. BMR = 680 + 1031.25 − 170 − 161 = <strong>1,380 kcal</strong>, and TDEE = 1,380 × 1.55 = <strong>2,139 kcal a day</strong>. For fat loss with a 20% deficit she needs about <strong>1,712 kcal</strong>; for muscle gain with a 15% surplus about <strong>2,460 kcal</strong>.</p>

            <h2 class="section-title"><i class="fas fa-table"></i> <span>Activity factor chart</span></h2>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>Activity level</th><th>Description</th><th>Factor</th></tr></thead>
                <tbody>
                    <tr><td>Sedentary</td><td>Desk job, little walking, no regular exercise</td><td>1.2</td></tr>
                    <tr><td>Lightly active</td><td>Light exercise or brisk walking 1–3 days a week</td><td>1.375</td></tr>
                    <tr><td>Moderately active</td><td>Moderate exercise 3–5 days a week</td><td>1.55</td></tr>
                    <tr><td>Very active</td><td>Hard exercise 6–7 days a week</td><td>1.725</td></tr>
                    <tr><td>Extremely active</td><td>Professional athlete, training twice a day, or heavy physical work</td><td>1.9</td></tr>
                </tbody>
            </table></div>
            <p>Tip: most people overestimate their activity. If in doubt, pick the lower level. The factor already includes your training, so do not add the calories your smartwatch shows on top of your TDEE.</p>

            <h2 class="section-title"><i class="fas fa-weight-scale"></i> <span>How many calories to lose weight safely?</span></h2>
            <p>The calculator suggests a moderate 20% deficit below your TDEE and never goes below your BMR. That usually means losing about 0.5 to 1 kg a week at first, the pace most medical guidelines recommend to protect muscle mass.</p>
            <p>The old rule that “7,700 calories = 1 kg of fat” is an oversimplification. Modelling from the US National Institutes of Health showed that weight loss slows over time because a lighter body burns less energy. Recalculate every time you lose 4–5 kg.</p>
            <ul class="check-list">
                <li><strong>Do not follow diets below 800 calories a day</strong> unless under direct medical supervision.</li>
                <li><strong>People with diabetes</strong> on insulin or sulfonylureas can get low blood sugar when they eat less, so plan changes with your doctor.</li>
                <li><strong>During pregnancy and breastfeeding</strong>, do not run a calorie deficit without medical guidance.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-chart-pie"></i> <span>Macro split: protein, fat and carbohydrates</span></h2>
            <p>The calculator applies a practical split to your fat-loss calories:</p>
            <ul class="check-list">
                <li><strong>Protein 1.8 g per kg of body weight:</strong> a meta-analysis in the British Journal of Sports Medicine found that the benefit of protein for muscle gains with resistance training levels off around 1.6 g/kg, with a possible upper value near 2.2 g/kg. <em>People with chronic kidney disease need lower amounts set by their doctor.</em></li>
                <li><strong>Fat 25% of energy:</strong> within the 20–35% range of the European Food Safety Authority, favouring olive oil, nuts and oily fish.</li>
                <li><strong>Carbohydrates the rest:</strong> from whole grains, legumes, vegetables and fruit, preferably low-GI choices for steadier blood sugar.</li>
            </ul>
            <p>In the example above (1,712 kcal): about 122 g protein, 48 g fat and 199 g carbohydrate a day.</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Limits of the calculation</span></h2>
            <p>All metabolic equations predict averages for groups; your real metabolism can be about 10% higher or lower. Accuracy drops in very muscular athletes, the very old, people with thyroid disorders and people taking medicines that affect metabolism. The equation is designed for adults; teenagers need extra energy for growth.</p>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>Foods that help you reach your goals</span></h2>
            <p>Protein and fibre sources from our food guide, with their calories and glycaemic index:</p>
            <div class="food-links">
                <a href="{food:grilled-chicken-breast}">Grilled chicken breast</a><a href="{food:boiled-egg}">Boiled egg</a>
                <a href="{food:greek-yogurt}">Greek yoghurt</a><a href="{food:skyr-naturel}">Skyr</a><a href="{food:lentils}">Lentils</a>
                <a href="{food:quinoa}">Quinoa</a><a href="{food:brown-rice}">Brown rice</a><a href="{food:sweet-potato}">Sweet potato</a>
                <a href="{food:walnuts}">Walnuts</a><a href="{food:avocado}">Avocado</a>
            </div>
            <p>To check whether your current weight is in a healthy range, start with the <a href="{calc:bmi}">BMI calculator</a>, and track belly fat with the <a href="{calc:whtr}">waist-to-height ratio calculator</a>.</p>
''',
            'faq': [
                ('What is the difference between BMR and TDEE?', 'BMR is what your body burns at complete rest; TDEE is your total daily burn once digestion, daily movement and exercise are added. Weight-loss plans are built on TDEE, not BMR.'),
                ('How many calories should I eat to lose weight?', 'Subtract about 20% from your TDEE without going below your BMR. For a woman with a TDEE of 2,139 kcal, that is about 1,712 kcal a day.'),
                ('Is the Mifflin-St Jeor equation accurate?', 'It is the most accurate of the common equations for adults according to a systematic review for the American Dietetic Association, but it is still an estimate that can be about 10% off your measured value. Track your weight for two weeks and adjust.'),
                ('Why has my weight loss stalled even though I eat below my TDEE?', 'A lighter body burns less energy, and water retention can temporarily hide fat loss. Recalculate with your new weight, track your waist and check that your food tracking is accurate.'),
                ('How much protein do I need per day?', 'The adult minimum is about 0.8 g per kg. During weight loss with resistance training, 1.6 to 2.2 g/kg helps protect muscle. People with kidney disease should follow their doctor’s advice.'),
                ('Should I add the calories I burn exercising to my TDEE?', 'No. The activity factor already includes your usual training. Adding it again counts it twice and cancels your deficit.'),
            ],
            'disclaimer': 'This calculator is an educational estimate for healthy adults and does not replace a plan from a dietitian. If you have diabetes, kidney or heart disease, or are pregnant or breastfeeding, talk to your doctor before changing your calorie intake.',
        },
        'nl': {
            'title': 'Calorieën berekenen: TDEE en BMR calculator | WiBo Health',
            'desc': 'Bereken je caloriebehoefte (TDEE) en BMR met Mifflin-St Jeor, inclusief veilige afvalcalorieën en een verdeling van eiwit, vet en koolhydraten.',
            'h1': 'Calorieën berekenen: dagelijkse caloriebehoefte (TDEE) en basaalmetabolisme (BMR)',
            'crumb': 'TDEE-calculator',
            'cat': 'Medische calculator · Energie en voeding',
            'short': 'Caloriebehoefte (TDEE)',
            'blurb': 'Calorieën om op gewicht te blijven, af te vallen of spieren op te bouwen.',
            'about': [{'name': 'Basaalmetabolisme'}, {'name': 'Totale dagelijkse energiebehoefte'}, {'name': 'Obesitas', 'condition': True}],
            'lead': 'Hoeveel calorieën heeft je lichaam per dag nodig? Deze tool schat je basaalmetabolisme (BMR) met de formule van Mifflin-St Jeor, de nauwkeurigste van de gangbare formules voor volwassenen. Daarna vermenigvuldigt hij die met je activiteitsniveau tot je totale dagelijkse energiebehoefte (TDEE), met veilige doelen voor afvallen en spieropbouw en een macroverdeling.',
            'ui': {
                'card_title': 'Bereken je dagelijkse calorieën', 'lbl_sex': 'Geslacht', 'male': 'Man', 'female': 'Vrouw',
                'lbl_age': 'Leeftijd (jaar)', 'lbl_weight': 'Gewicht (kg)', 'lbl_height': 'Lengte (cm)',
                'ph_age': 'bijv. 34', 'ph_weight': 'bijv. 68', 'ph_height': 'bijv. 165',
                'lbl_activity': 'Lichamelijk activiteitsniveau', 'acts': [
                    'Zittend: kantoorwerk, geen sport (×1,2)', 'Licht actief: 1–3 dagen per week sporten (×1,375)',
                    'Matig actief: 3–5 dagen per week sporten (×1,55)', 'Zeer actief: 6–7 dagen per week intensief sporten (×1,725)',
                    'Extreem actief: topsporter of zwaar lichamelijk werk (×1,9)'],
                'btn': 'Bereken mijn calorieën', 'res_heading': 'Totale dagelijkse energiebehoefte (TDEE)',
                'kcal_day': 'calorieën per dag om op je huidige gewicht te blijven',
                'bmr_label': 'Basaalmetabolisme (BMR)', 'bmr_sub': 'wat je lichaam in volledige rust verbrandt',
                'deficit_label': 'Vet verliezen (20% tekort)', 'deficit_sub': 'nooit onder je BMR',
                'surplus_label': 'Spieren opbouwen (15% overschot)', 'surplus_sub': 'met krachttraining',
                'macros_header': 'Voorgestelde macroverdeling op je afvalcalorieën',
                'protein': 'Eiwit (1,8 g/kg)', 'fat': 'Vet (25% van de energie)', 'carbs': 'Koolhydraten (de rest)',
                'tip': 'Dit zijn schattingen: volg je gewicht twee weken en pas dan aan met 100–200 calorieën. Kies koolhydraten met een lage glykemische index en veel vezels.',
                'tip_lowcarb': 'Je afvalcalorieën zijn laag ten opzichte van je eiwitdoel, waardoor er weinig ruimte overblijft voor koolhydraten. Ga niet lager zonder diëtist, zeker niet als je diabetesmedicatie gebruikt.',
            },
            'body': '''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>BMR en TDEE: wat is het verschil?</span></h2>
            <p>Het <strong>basaalmetabolisme (BMR)</strong> is de energie die je lichaam in volledige rust nodig heeft om te blijven functioneren: hartslag, ademhaling, hersenen, lever en nieren, celvernieuwing en het op temperatuur houden van je lichaam. Voor de meeste mensen die weinig bewegen is dit het grootste deel van het dagelijkse energieverbruik.</p>
            <p>De <strong>totale dagelijkse energiebehoefte (TDEE)</strong> is alles wat je in 24 uur verbrandt. Die bestaat uit drie delen:</p>
            <ul class="check-list">
                <li><strong>Basaalmetabolisme:</strong> het grootste deel.</li>
                <li><strong>Thermisch effect van voeding:</strong> ongeveer 10% van de calorieën, de energie die nodig is om voedsel te verteren en op te nemen; hoger bij eiwit.</li>
                <li><strong>Energie voor beweging:</strong> sporten plus dagelijkse niet-sportieve beweging zoals lopen, staan en huishoudelijk werk. Dit deel verschilt het meest tussen mensen.</li>
            </ul>
            <p>Eet je ongeveer je TDEE, dan blijft je gewicht stabiel; eet je minder, dan val je af; eet je meer, dan kom je aan.</p>

            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>De formule van Mifflin-St Jeor: zo rekent de calculator</span></h2>
            <p>De formule van Mifflin-St Jeor verscheen in 1990. Een latere systematische review voor de American Dietetic Association vond dat deze formule het vaakst het rustmetabolisme binnen 10% van de gemeten waarde voorspelde, bij volwassenen met en zonder obesitas:</p>
            <p class="formula-box">Mannen: BMR = (10 × gewicht in kg) + (6,25 × lengte in cm) − (5 × leeftijd) + 5</p>
            <p class="formula-box">Vrouwen: BMR = (10 × gewicht in kg) + (6,25 × lengte in cm) − (5 × leeftijd) − 161</p>
            <p>Daarna: <strong>TDEE = BMR × activiteitsfactor</strong>.</p>
            <p><strong>Rekenvoorbeeld:</strong> een vrouw van 34 jaar die 68 kg weegt, 165 cm lang is en 3–5 dagen per week sport. BMR = 680 + 1031,25 − 170 − 161 = <strong>1380 kcal</strong>, en TDEE = 1380 × 1,55 = <strong>2139 kcal per dag</strong>. Om vet te verliezen met 20% tekort heeft ze ongeveer <strong>1712 kcal</strong> nodig; voor spieropbouw met 15% overschot ongeveer <strong>2460 kcal</strong>.</p>

            <h2 class="section-title"><i class="fas fa-table"></i> <span>Tabel met activiteitsfactoren</span></h2>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>Activiteitsniveau</th><th>Omschrijving</th><th>Factor</th></tr></thead>
                <tbody>
                    <tr><td>Zittend</td><td>Kantoorwerk, weinig lopen, geen vaste sport</td><td>1,2</td></tr>
                    <tr><td>Licht actief</td><td>Lichte training of stevig wandelen 1–3 dagen per week</td><td>1,375</td></tr>
                    <tr><td>Matig actief</td><td>Matig intensief sporten 3–5 dagen per week</td><td>1,55</td></tr>
                    <tr><td>Zeer actief</td><td>Intensief sporten 6–7 dagen per week</td><td>1,725</td></tr>
                    <tr><td>Extreem actief</td><td>Topsporter, twee keer per dag trainen of zwaar lichamelijk werk</td><td>1,9</td></tr>
                </tbody>
            </table></div>
            <p>Tip: de meeste mensen overschatten hoe actief ze zijn. Twijfel je, kies dan het lagere niveau. De factor bevat je training al, dus tel de calorieën van je smartwatch niet nog eens bij je TDEE op.</p>

            <h2 class="section-title"><i class="fas fa-weight-scale"></i> <span>Hoeveel calorieën om veilig af te vallen?</span></h2>
            <p>De calculator stelt een gematigd tekort van 20% onder je TDEE voor en gaat nooit onder je BMR. Daarmee verlies je in het begin meestal 0,5 tot 1 kg per week, het tempo dat de meeste medische richtlijnen aanraden om spiermassa te behouden.</p>
            <p>De oude regel “7700 calorieën = 1 kg vet” is te simpel. Modellen van de Amerikaanse National Institutes of Health lieten zien dat gewichtsverlies na verloop van tijd vertraagt, omdat een lichter lichaam minder energie verbrandt. Reken daarom opnieuw na elke 4–5 kg.</p>
            <ul class="check-list">
                <li><strong>Volg geen diëten onder 800 calorieën per dag</strong> zonder direct medisch toezicht.</li>
                <li><strong>Mensen met diabetes</strong> die insuline of sulfonylureumderivaten gebruiken, kunnen een hypo krijgen als ze minder eten; overleg wijzigingen met je arts.</li>
                <li><strong>Tijdens zwangerschap en borstvoeding</strong> houd je geen calorietekort aan zonder medisch advies.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-chart-pie"></i> <span>Macroverdeling: eiwit, vet en koolhydraten</span></h2>
            <p>De calculator past een praktische verdeling toe op je afvalcalorieën:</p>
            <ul class="check-list">
                <li><strong>Eiwit 1,8 g per kg lichaamsgewicht:</strong> een meta-analyse in het British Journal of Sports Medicine vond dat het effect van eiwit op spiergroei bij krachttraining afvlakt rond 1,6 g/kg, met een mogelijke bovengrens rond 2,2 g/kg. <em>Mensen met chronische nierschade hebben minder nodig, volgens advies van hun arts.</em></li>
                <li><strong>Vet 25% van de energie:</strong> binnen de 20–35% van de Europese voedselveiligheidsautoriteit EFSA, bij voorkeur uit olijfolie, noten en vette vis.</li>
                <li><strong>Koolhydraten de rest:</strong> uit volkoren graan, peulvruchten, groente en fruit, liefst met een lage glykemische index voor een stabielere bloedsuiker.</li>
            </ul>
            <p>In het voorbeeld hierboven (1712 kcal): ongeveer 122 g eiwit, 48 g vet en 199 g koolhydraten per dag.</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Beperkingen van de berekening</span></h2>
            <p>Alle stofwisselingsformules voorspellen een groepsgemiddelde; je werkelijke verbruik kan ongeveer 10% hoger of lager liggen. De nauwkeurigheid is lager bij zeer gespierde sporters, hoogbejaarden, mensen met schildklierproblemen en bij medicijnen die de stofwisseling beïnvloeden. De formule is bedoeld voor volwassenen; tieners hebben extra energie nodig om te groeien.</p>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>Voedingsmiddelen die je helpen je doel te halen</span></h2>
            <p>Bronnen van eiwit en vezels uit onze voedingsgids, met calorieën en glykemische index:</p>
            <div class="food-links">
                <a href="{food:grilled-chicken-breast}">Gegrilde kipfilet</a><a href="{food:boiled-egg}">Gekookt ei</a>
                <a href="{food:greek-yogurt}">Griekse yoghurt</a><a href="{food:skyr-naturel}">Skyr</a><a href="{food:lentils}">Linzen</a>
                <a href="{food:quinoa}">Quinoa</a><a href="{food:brown-rice}">Zilvervliesrijst</a><a href="{food:sweet-potato}">Zoete aardappel</a>
                <a href="{food:walnuts}">Walnoten</a><a href="{food:avocado}">Avocado</a>
            </div>
            <p>Wil je weten of je huidige gewicht gezond is? Begin met de <a href="{calc:bmi}">BMI-calculator</a> en volg je buikvet met de <a href="{calc:whtr}">taille-lengteratio calculator</a>.</p>
''',
            'faq': [
                ('Wat is het verschil tussen BMR en TDEE?', 'De BMR is wat je lichaam in volledige rust verbrandt; de TDEE is je totale dagelijkse verbruik inclusief vertering, dagelijkse beweging en sport. Afvalplannen gaan uit van de TDEE, niet van de BMR.'),
                ('Hoeveel calorieën moet ik eten om af te vallen?', 'Trek ongeveer 20% van je TDEE af zonder onder je BMR te gaan. Voor een vrouw met een TDEE van 2139 kcal is dat ongeveer 1712 kcal per dag.'),
                ('Is de formule van Mifflin-St Jeor nauwkeurig?', 'Volgens een systematische review voor de American Dietetic Association is het de nauwkeurigste van de gangbare formules voor volwassenen, maar het blijft een schatting die ongeveer 10% kan afwijken. Volg je gewicht twee weken en stel bij.'),
                ('Waarom val ik niet meer af terwijl ik onder mijn TDEE eet?', 'Een lichter lichaam verbrandt minder energie, en vochtophoping kan vetverlies tijdelijk verbergen. Reken opnieuw met je nieuwe gewicht, meet je buikomvang en controleer of je eten nauwkeurig bijhoudt.'),
                ('Hoeveel eiwit heb ik per dag nodig?', 'Het minimum voor volwassenen is ongeveer 0,8 g per kg. Bij afvallen met krachttraining helpt 1,6 tot 2,2 g/kg om spieren te behouden. Bij nierziekte volg je het advies van je arts.'),
                ('Moet ik de calorieën van mijn training bij mijn TDEE optellen?', 'Nee. De activiteitsfactor bevat je gebruikelijke training al. Als je ze opnieuw optelt, tel je ze dubbel en verdwijnt je tekort.'),
            ],
            'disclaimer': 'Deze calculator geeft een educatieve schatting voor gezonde volwassenen en vervangt geen plan van een diëtist. Heb je diabetes, een nier- of hartaandoening, of ben je zwanger of geef je borstvoeding? Overleg dan met je arts voordat je je calorie-inname verandert.',
        },
    },
}
