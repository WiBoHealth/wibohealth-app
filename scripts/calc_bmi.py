"""BMI calculator page content (AR / EN / NL). Worked example: 78 kg, 175 cm -> 25.5; healthy range 56.7-76.3 kg."""

BMI = {
    'key': 'bmi',
    'slug': 'bmi-calculator',
    'icon': 'fa-weight-scale',
    'badge': 'WHO · NICE 2022',
    'published': '2026-10-18',
    'modified': '2026-10-18',
    'references': [
        'World Health Organization. Obesity: preventing and managing the global epidemic. Report of a WHO Consultation. WHO Technical Report Series 894. Geneva: WHO; 2000.',
        'WHO Expert Consultation. Appropriate body-mass index for Asian populations and its implications for policy and intervention strategies. Lancet. 2004;363(9403):157-163.',
        'National Institute for Health and Care Excellence (NICE). Obesity: identification, assessment and management (CG189), update on BMI thresholds and waist-to-height ratio. London: NICE; 2022.',
        'Knowler WC, Barrett-Connor E, Fowler SE, et al. Reduction in the incidence of type 2 diabetes with lifestyle intervention or metformin. N Engl J Med. 2002;346(6):393-403.',
        'World Health Organization. WHO guidelines on physical activity and sedentary behaviour. Geneva: WHO; 2020.',
    ],
    'content': {
        'ar': {
            'title': 'حاسبة مؤشر كتلة الجسم BMI وحساب الوزن المثالي | WiBo Health',
            'desc': 'احسب مؤشر كتلة الجسم (BMI) مجاناً وفق تصنيف منظمة الصحة العالمية، واعرف نطاق الوزن الصحي لطولك، مع جدول تصنيف النحافة والسمنة وحدود الحساب ونصائح طبية عملية.',
            'h1': 'حاسبة مؤشر كتلة الجسم (BMI) وحساب الوزن المثالي لطولك',
            'crumb': 'حاسبة BMI',
            'cat': 'حاسبة طبية · قياسات الجسم',
            'short': 'مؤشر كتلة الجسم BMI',
            'blurb': 'صنّف وزنك واعرف نطاق الوزن الصحي لطولك.',
            'about': [{'name': 'مؤشر كتلة الجسم'}, {'name': 'السمنة', 'condition': True}, {'name': 'نقص الوزن', 'condition': True}],
            'lead': 'مؤشر كتلة الجسم (Body Mass Index) هو أكثر أدوات الفحص استخداماً في العالم لتقدير ما إذا كان وزنك مناسباً لطولك. أدخل وزنك وطولك لتحصل فوراً على قيمة BMI وتصنيفها وفق منظمة الصحة العالمية، ونطاق الوزن الصحي الخاص بطولك، ثم اقرأ الدليل أدناه لتعرف ما تعنيه النتيجة وما لا تعنيه.',
            'ui': {
                'card_title': 'احسب مؤشر كتلة جسمك', 'lbl_weight': 'الوزن (كغ)', 'lbl_height': 'الطول (سم)',
                'ph_weight': 'مثال: 78', 'ph_height': 'مثال: 175', 'btn': 'احسب مؤشر كتلة الجسم',
                'res_heading': 'مؤشر كتلة جسمك (BMI)', 'ideal_label': 'نطاق الوزن الصحي لطولك (BMI من 18.5 إلى 24.9)',
                'prime_label': 'BMI Prime: نسبتك إلى الحد الأعلى للوزن الطبيعي (25)',
                'st_under': 'نقص الوزن', 'st_normal': 'وزن طبيعي', 'st_over': 'زيادة الوزن',
                'st_ob1': 'سمنة من الدرجة الأولى', 'st_ob2': 'سمنة من الدرجة الثانية', 'st_ob3': 'سمنة من الدرجة الثالثة',
                'tip_under': 'وزنك أقل من النطاق الصحي. ناقش مع طبيبك أسباب النحافة المحتملة (كاضطرابات الغدة الدرقية أو سوء الامتصاص)، وركّز على أطعمة غنية بالطاقة والبروتين بدل الأطعمة الفارغة.',
                'tip_normal': 'وزنك ضمن النطاق الصحي. حافظ عليه بالنشاط المنتظم ونظام غذائي متوازن، وتحقق أيضاً من نسبة الخصر إلى الطول، فالدهون الحشوية قد تزيد حتى مع وزن طبيعي.',
                'tip_over': 'وزنك فوق النطاق الصحي. خسارة 5 إلى 10% فقط من وزنك الحالي تحسّن ضغط الدم وسكر الدم والدهون بشكل ملموس. احسب احتياجك من السعرات وابدأ بعجز معتدل.',
                'tip_obese': 'النتيجة في نطاق السمنة، وهي ترتبط بارتفاع خطر السكري من النوع الثاني وأمراض القلب. يُنصح بتقييم طبي شامل (السكر التراكمي، الدهون، ضغط الدم) ووضع خطة منظمة لخسارة الوزن تحت إشراف مختص.',
            },
            'body': '''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>ما هو مؤشر كتلة الجسم (BMI)؟</span></h2>
            <p>مؤشر كتلة الجسم رقم بسيط يربط وزن الإنسان بطوله، ويُستخدم لتقدير ما إذا كان الوزن ضمن النطاق الصحي أو أقل منه أو أعلى منه. وضع فكرته عالم الرياضيات البلجيكي أدولف كيتليه في القرن التاسع عشر، ثم اعتمدته منظمة الصحة العالمية معياراً دولياً لتصنيف النحافة وزيادة الوزن والسمنة لدى البالغين.</p>
            <p>تكمن قيمة مؤشر كتلة الجسم في أنه سريع ومجاني ولا يحتاج إلا إلى ميزان ومتر قياس، وأنه يرتبط على مستوى المجتمعات بنسبة الدهون في الجسم وبخطر الإصابة بأمراض مزمنة مثل السكري من النوع الثاني وارتفاع ضغط الدم وأمراض القلب والشرايين وبعض أنواع السرطان. لكنه <strong>أداة فحص أولي وليس تشخيصاً</strong>؛ فهو لا يقيس الدهون مباشرة ولا يعرف أين تتوزع في جسمك.</p>

            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>كيف يُحسب مؤشر كتلة الجسم؟</span></h2>
            <p>تقسم الحاسبة وزنك بالكيلوغرام على مربع طولك بالمتر:</p>
            <p class="formula-box">مؤشر كتلة الجسم = الوزن (كغ) ÷ [الطول (م) × الطول (م)]</p>
            <p><strong>مثال عملي:</strong> شخص وزنه 78 كغ وطوله 175 سم. مربع الطول = 1.75 × 1.75 = 3.0625، ثم 78 ÷ 3.0625 = <strong>25.5</strong>، أي في نطاق زيادة الوزن البسيطة. أما نطاق الوزن الصحي لهذا الطول فيُحسب بضرب مربع الطول في حدّي النطاق الطبيعي: 18.5 × 3.0625 = 56.7 كغ، و24.9 × 3.0625 = 76.3 كغ.</p>
            <p>وتعرض الحاسبة أيضاً قيمة <strong>BMI Prime</strong>، وهي ناتج قسمة مؤشرك على 25 (الحد الأعلى للوزن الطبيعي): القيمة 1.00 تعني أنك على الحد تماماً، و1.10 تعني أنك أعلى منه بنحو 10%.</p>

            <h2 class="section-title"><i class="fas fa-table"></i> <span>جدول تصنيف مؤشر كتلة الجسم للبالغين</span></h2>
            <p>يعتمد التصنيف التالي على تقرير منظمة الصحة العالمية، وهو موحد للرجال والنساء من عمر 18 عاماً فأكثر:</p>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>التصنيف</th><th>مؤشر كتلة الجسم (كغ/م²)</th><th>خطر الأمراض المصاحبة</th></tr></thead>
                <tbody>
                    <tr><td><span class="dot b"></span>نقص الوزن</td><td>أقل من 18.5</td><td>منخفض لأمراض السمنة، لكن يرتفع خطر نقص التغذية وهشاشة العظام وضعف المناعة</td></tr>
                    <tr><td><span class="dot g"></span>الوزن الطبيعي</td><td>18.5 – 24.9</td><td>متوسط (المستوى المرجعي)</td></tr>
                    <tr><td><span class="dot y"></span>زيادة الوزن (ما قبل السمنة)</td><td>25.0 – 29.9</td><td>متزايد</td></tr>
                    <tr><td><span class="dot o"></span>سمنة من الدرجة الأولى</td><td>30.0 – 34.9</td><td>معتدل</td></tr>
                    <tr><td><span class="dot r"></span>سمنة من الدرجة الثانية</td><td>35.0 – 39.9</td><td>شديد</td></tr>
                    <tr><td><span class="dot r"></span>سمنة من الدرجة الثالثة</td><td>40 فأكثر</td><td>شديد جداً</td></tr>
                </tbody>
            </table></div>

            <h2 class="section-title"><i class="fas fa-earth-asia"></i> <span>حدود أقل لأصحاب الأصول العربية والآسيوية والأفريقية</span></h2>
            <p>العلاقة بين مؤشر كتلة الجسم ونسبة الدهون ليست واحدة لدى جميع الشعوب. فقد لاحظت منظمة الصحة العالمية أن خطر السكري وأمراض القلب يبدأ بالارتفاع عند قيم أقل لدى سكان آسيا، واقترحت نقطتي تدخل عند 23 و27.5. وفي تحديث عام 2022 أوصى المعهد الوطني البريطاني للصحة والرعاية (NICE) باستخدام هذه الحدود المنخفضة لمن تعود أصوله إلى <strong>الشرق الأوسط</strong> أو جنوب آسيا أو الصين أو باقي آسيا أو أفريقيا السوداء أو الكاريبي الأفريقي:</p>
            <ul class="check-list">
                <li><strong>23 إلى 27.4:</strong> يُعامل كزيادة في الوزن.</li>
                <li><strong>27.5 فأكثر:</strong> يُعامل كسمنة.</li>
            </ul>
            <p>إذا كنت من أصول عربية وكانت نتيجتك بين 23 و25، فلا تكتفِ بتصنيف «وزن طبيعي»، بل قِس محيط خصرك عبر <a href="{calc:whtr}">حاسبة نسبة الخصر إلى الطول</a> وراجع سكر الدم الصائم أو السكر التراكمي في فحصك الدوري.</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>متى لا يكون مؤشر كتلة الجسم دقيقاً؟</span></h2>
            <ul class="check-list">
                <li><strong>الرياضيون وأصحاب الكتلة العضلية الكبيرة:</strong> العضلات أثقل من الدهون، فقد يظهر الرياضي في نطاق «زيادة الوزن» رغم انخفاض دهونه.</li>
                <li><strong>كبار السن:</strong> مع التقدم في العمر تقل الكتلة العضلية وتزيد الدهون، فقد يبدو المؤشر طبيعياً بينما ترتفع نسبة الدهون فعلياً.</li>
                <li><strong>الأطفال والمراهقون (أقل من 18 عاماً):</strong> يُقيَّمون بمنحنيات النمو المئوية حسب العمر والجنس، لا بهذا الجدول.</li>
                <li><strong>الحمل والرضاعة:</strong> يتغير الوزن لأسباب طبيعية، ويُتابَع اكتساب الوزن مع الطبيب.</li>
                <li><strong>احتباس السوائل والوذمة أو بتر الأطراف:</strong> يتأثر الوزن لأسباب لا علاقة لها بالدهون.</li>
                <li><strong>توزيع الدهون:</strong> المؤشر لا يفرّق بين دهون الأرداف ودهون البطن الحشوية الأخطر أيضياً؛ لذلك يُكمَّل دائماً بقياس الخصر.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>كيف تستفيد من نتيجتك؟ نصائح طبية عملية</span></h2>
            <h3>إذا كان وزنك أقل من الطبيعي</h3>
            <p>النحافة غير المقصودة تستحق تقييماً طبياً، خاصة إذا رافقها فقدان وزن سريع أو تعب أو اضطراب في الهضم. زِد السعرات بأطعمة كثيفة غذائياً مثل المكسرات والبقوليات والزبادي ومنتجات الألبان كاملة الدسم، وأضف تمارين المقاومة لبناء العضلات بدل تراكم الدهون.</p>
            <h3>إذا كان وزنك طبيعياً</h3>
            <p>الهدف هو الحفاظ عليه: نشاط بدني معتدل من 150 إلى 300 دقيقة أسبوعياً كما توصي منظمة الصحة العالمية، مع يومين من تمارين القوة، ونوم كافٍ، وطبق يعتمد على الخضار والبروتين الجيد والحبوب الكاملة.</p>
            <h3>إذا كان لديك زيادة في الوزن أو سمنة</h3>
            <p>لا تحتاج إلى الوصول إلى «الوزن المثالي» حتى تتحسن صحتك. ففي دراسة برنامج الوقاية من السكري الأمريكية خفّض فقدانُ نحو 7% من الوزن مع 150 دقيقة نشاط أسبوعياً خطرَ الإصابة بالسكري من النوع الثاني بنسبة 58% لدى أشخاص في مرحلة ما قبل السكري. ابدأ بهذه الخطوات:</p>
            <ol class="steps">
                <li>احسب احتياجك اليومي من السعرات عبر <a href="{calc:tdee}">حاسبة السعرات وTDEE</a>، وابدأ بعجز معتدل نحو 20% بدل الحميات القاسية.</li>
                <li>اجعل نصف طبقك خضاراً، وربعه بروتيناً (دجاج، سمك، بيض، بقوليات)، وربعه نشويات كاملة منخفضة المؤشر الجلايسيمي.</li>
                <li>استبدل المشروبات المحلاة بالماء، واحسب احتياجك عبر <a href="{calc:water}">حاسبة الماء اليومية</a>.</li>
                <li>تابع محيط الخصر شهرياً، فنزوله علامة على خسارة الدهون الحشوية حتى لو تباطأ نزول الميزان.</li>
                <li>إذا كنت تتناول أدوية للسكري أو الضغط، أخبر طبيبك قبل تقليل السعرات بشكل ملحوظ، فقد تحتاج الجرعات إلى تعديل.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>أطعمة تساعد على إدارة الوزن من دليلنا الغذائي</span></h2>
            <p>هذه الأطعمة غنية بالألياف أو البروتين وتمنح شبعاً أطول. افتح صفحة كل طعام لترى سعراته ومؤشره الجلايسيمي وقيمه الغذائية الكاملة:</p>
            <div class="food-links">
                <a href="{food:oatmeal}">الشوفان</a><a href="{food:lentils}">العدس</a><a href="{food:chickpeas}">الحمص</a>
                <a href="{food:greek-yogurt}">الزبادي اليوناني</a><a href="{food:grilled-chicken-breast}">صدر الدجاج المشوي</a>
                <a href="{food:broccoli}">البروكلي</a><a href="{food:apple}">التفاح</a><a href="{food:quinoa}">الكينوا</a>
                <a href="{food:whole-wheat-bread}">خبز القمح الكامل</a>
            </div>
            <p>وتصفّح <a href="{site:/foods.html}">دليل الأطعمة الكامل</a> لمقارنة أكثر من 700 صنف حسب المؤشر الجلايسيمي والسعرات.</p>
''',
            'faq': [
                ('ما هو مؤشر كتلة الجسم الطبيعي للبالغين؟', 'يتراوح مؤشر كتلة الجسم الطبيعي بين 18.5 و24.9 للرجال والنساء من عمر 18 عاماً فأكثر. ولمن تعود أصوله إلى الشرق الأوسط أو آسيا أو أفريقيا، توصي إرشادات NICE باعتبار 23 بداية زيادة الوزن.'),
                ('كيف أعرف وزني المثالي حسب طولي؟', 'اضرب مربع طولك بالمتر في 18.5 ثم في 24.9. فلطول 170 سم (مربعه 2.89): الوزن الصحي بين 53.5 و72 كغ تقريباً. تعرض الحاسبة أعلاه هذا النطاق تلقائياً.'),
                ('هل يختلف حساب BMI بين الرجال والنساء؟', 'المعادلة والحدود واحدة للجنسين لدى البالغين، لكن المرأة تحمل في المتوسط نسبة دهون أعلى من الرجل عند المؤشر نفسه، لذلك يفيد قياس الخصر في استكمال الصورة.'),
                ('هل تصلح حاسبة BMI للأطفال والمراهقين؟', 'لا. يُقيَّم من هم دون 18 عاماً بمنحنيات النمو المئوية حسب العمر والجنس، لأن تركيب الجسم يتغير مع النمو. استشر طبيب الأطفال لتفسير القيم.'),
                ('لماذا يظهر الرياضي في نطاق زيادة الوزن؟', 'لأن المؤشر يعتمد على الوزن الكلي ولا يفرّق بين العضلات والدهون. لدى الرياضيين يكون قياس الخصر أو نسبة الدهون أدق من BMI.'),
                ('ما الفرق بين BMI ونسبة الخصر إلى الطول؟', 'يقيس BMI حجم الجسم الكلي، بينما تقيس نسبة الخصر إلى الطول الدهون المتركزة حول البطن، وهي أقوى ارتباطاً بمقاومة الإنسولين وأمراض القلب. استخدم الاثنين معاً للحصول على تقييم أدق.'),
            ],
            'disclaimer': 'هذه الحاسبة أداة فحص تثقيفية للبالغين (18 عاماً فأكثر)، ولا تُعد تشخيصاً طبياً، ولا تصلح للحوامل أو الأطفال. فسّر نتيجتك مع طبيبك أو أخصائي التغذية ضمن حالتك الصحية الكاملة.',
        },
        'en': {
            'title': 'BMI Calculator: Body Mass Index & Healthy Weight | WiBo Health',
            'desc': 'Free BMI calculator using the WHO chart. See the healthy weight for your height, lower cut-offs for Middle Eastern backgrounds and practical medical advice.',
            'h1': 'BMI Calculator: Body Mass Index and Healthy Weight for Your Height',
            'crumb': 'BMI calculator',
            'cat': 'Medical calculator · Body measurements',
            'short': 'Body mass index (BMI)',
            'blurb': 'Classify your weight and see the healthy range for your height.',
            'about': [{'name': 'Body mass index'}, {'name': 'Obesity', 'condition': True}, {'name': 'Underweight', 'condition': True}],
            'lead': 'Body mass index (BMI) is the most widely used screening tool for checking whether your weight suits your height. Enter your weight and height to get your BMI, its WHO category and the healthy weight range for your height, then read the guide below to understand what the number means and what it does not.',
            'ui': {
                'card_title': 'Calculate your BMI', 'lbl_weight': 'Weight (kg)', 'lbl_height': 'Height (cm)',
                'ph_weight': 'e.g. 78', 'ph_height': 'e.g. 175', 'btn': 'Calculate my BMI',
                'res_heading': 'Your body mass index (BMI)', 'ideal_label': 'Healthy weight range for your height (BMI 18.5 to 24.9)',
                'prime_label': 'BMI Prime: your BMI relative to the upper healthy limit (25)',
                'st_under': 'Underweight', 'st_normal': 'Healthy weight', 'st_over': 'Overweight',
                'st_ob1': 'Obesity class I', 'st_ob2': 'Obesity class II', 'st_ob3': 'Obesity class III',
                'tip_under': 'Your weight is below the healthy range. Ask your doctor about possible causes (such as thyroid problems or malabsorption) and focus on energy- and protein-rich whole foods rather than empty calories.',
                'tip_normal': 'Your weight is in the healthy range. Keep it there with regular activity and a balanced diet, and check your waist-to-height ratio too: visceral fat can rise even at a normal weight.',
                'tip_over': 'Your weight is above the healthy range. Losing just 5 to 10% of your current weight noticeably improves blood pressure, blood glucose and blood lipids. Work out your calorie needs and start with a moderate deficit.',
                'tip_obese': 'Your result is in the obesity range, which is linked to a higher risk of type 2 diabetes and heart disease. A full medical check (HbA1c, lipids, blood pressure) and a structured weight-loss plan with a professional are recommended.',
            },
            'body': '''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>What is body mass index (BMI)?</span></h2>
            <p>Body mass index is a simple number that relates your weight to your height. It is used to estimate whether your weight is in a healthy range, below it or above it. The idea dates back to the Belgian mathematician Adolphe Quetelet in the nineteenth century, and the World Health Organization adopted it as the international standard for classifying underweight, overweight and obesity in adults.</p>
            <p>BMI is quick, free and needs only a scale and a tape measure. At population level it tracks body fat and the risk of chronic conditions such as type 2 diabetes, high blood pressure, cardiovascular disease and some cancers. But it is <strong>a screening tool, not a diagnosis</strong>: it does not measure fat directly and cannot tell where that fat is stored.</p>

            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>How is BMI calculated?</span></h2>
            <p>The calculator divides your weight in kilograms by the square of your height in metres:</p>
            <p class="formula-box">BMI = weight (kg) ÷ [height (m) × height (m)]</p>
            <p><strong>Worked example:</strong> a person who weighs 78 kg and is 175 cm tall. Height squared = 1.75 × 1.75 = 3.0625, and 78 ÷ 3.0625 = <strong>25.5</strong>, which is just into the overweight range. The healthy weight range for this height is found by multiplying height squared by the limits of the normal range: 18.5 × 3.0625 = 56.7 kg and 24.9 × 3.0625 = 76.3 kg.</p>
            <p>The calculator also shows <strong>BMI Prime</strong>: your BMI divided by 25, the upper limit of the healthy range. A value of 1.00 means you are exactly at the limit; 1.10 means you are about 10% above it.</p>

            <h2 class="section-title"><i class="fas fa-table"></i> <span>BMI chart for adults</span></h2>
            <p>The classification below follows the WHO report and is the same for men and women aged 18 and over:</p>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>Category</th><th>BMI (kg/m²)</th><th>Risk of co-morbidities</th></tr></thead>
                <tbody>
                    <tr><td><span class="dot b"></span>Underweight</td><td>below 18.5</td><td>Low for obesity-related disease, but higher risk of undernutrition, osteoporosis and weaker immunity</td></tr>
                    <tr><td><span class="dot g"></span>Healthy weight</td><td>18.5 – 24.9</td><td>Average (reference level)</td></tr>
                    <tr><td><span class="dot y"></span>Overweight (pre-obese)</td><td>25.0 – 29.9</td><td>Increased</td></tr>
                    <tr><td><span class="dot o"></span>Obesity class I</td><td>30.0 – 34.9</td><td>Moderate</td></tr>
                    <tr><td><span class="dot r"></span>Obesity class II</td><td>35.0 – 39.9</td><td>Severe</td></tr>
                    <tr><td><span class="dot r"></span>Obesity class III</td><td>40 and above</td><td>Very severe</td></tr>
                </tbody>
            </table></div>

            <h2 class="section-title"><i class="fas fa-earth-asia"></i> <span>Lower cut-offs for Middle Eastern, Asian and African backgrounds</span></h2>
            <p>The link between BMI and body fat is not the same in every population. WHO observed that diabetes and heart-disease risk starts to rise at lower values in Asian populations and proposed action points at 23 and 27.5. In its 2022 update, the UK National Institute for Health and Care Excellence (NICE) recommended these lower thresholds for people with a <strong>Middle Eastern</strong>, South Asian, Chinese, other Asian, Black African or African-Caribbean family background:</p>
            <ul class="check-list">
                <li><strong>23 to 27.4:</strong> treated as overweight.</li>
                <li><strong>27.5 and above:</strong> treated as obesity.</li>
            </ul>
            <p>If you have such a background and your BMI is between 23 and 25, do not stop at “healthy weight”: measure your waist with the <a href="{calc:whtr}">waist-to-height ratio calculator</a> and check your fasting glucose or HbA1c at your next check-up.</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>When is BMI less accurate?</span></h2>
            <ul class="check-list">
                <li><strong>Athletes and very muscular people:</strong> muscle is denser than fat, so an athlete can land in the “overweight” range with little body fat.</li>
                <li><strong>Older adults:</strong> muscle mass falls and fat rises with age, so BMI can look normal while body fat is actually high.</li>
                <li><strong>Children and teenagers (under 18):</strong> they are assessed with BMI-for-age growth percentiles, not with this chart.</li>
                <li><strong>Pregnancy and breastfeeding:</strong> weight changes for natural reasons; weight gain is monitored with your doctor or midwife.</li>
                <li><strong>Fluid retention, oedema or amputation:</strong> weight changes for reasons unrelated to fat.</li>
                <li><strong>Fat distribution:</strong> BMI cannot tell hip fat from the metabolically riskier visceral fat around the belly, so always pair it with a waist measurement.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>What to do with your result: practical medical advice</span></h2>
            <h3>If you are underweight</h3>
            <p>Unintended thinness deserves a medical check, especially with rapid weight loss, fatigue or digestive symptoms. Add calories with nutrient-dense foods such as nuts, legumes, yoghurt and full-fat dairy, and include resistance training so the extra weight is muscle rather than fat.</p>
            <h3>If your weight is healthy</h3>
            <p>The goal is to stay there: 150 to 300 minutes of moderate activity a week as WHO recommends, two days of strength training, enough sleep and a plate built on vegetables, good protein and whole grains.</p>
            <h3>If you are overweight or living with obesity</h3>
            <p>You do not need to reach an “ideal weight” for your health to improve. In the US Diabetes Prevention Program, losing about 7% of body weight with 150 minutes of activity a week cut the risk of developing type 2 diabetes by 58% in people with prediabetes. Start with these steps:</p>
            <ol class="steps">
                <li>Work out your daily calorie needs with the <a href="{calc:tdee}">TDEE calorie calculator</a> and start with a moderate deficit of about 20% rather than a crash diet.</li>
                <li>Fill half your plate with vegetables, a quarter with protein (chicken, fish, eggs, legumes) and a quarter with low-GI whole-grain starches.</li>
                <li>Swap sugary drinks for water; see how much you need with the <a href="{calc:water}">daily water calculator</a>.</li>
                <li>Measure your waist every month: a shrinking waist shows visceral fat loss even when the scale slows down.</li>
                <li>If you take medication for diabetes or blood pressure, tell your doctor before cutting calories noticeably, as doses may need adjusting.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>Foods that support weight management</span></h2>
            <p>These foods are rich in fibre or protein and keep you full for longer. Open each one to see its calories, glycaemic index and full nutrition facts:</p>
            <div class="food-links">
                <a href="{food:oatmeal}">Oatmeal</a><a href="{food:lentils}">Lentils</a><a href="{food:chickpeas}">Chickpeas</a>
                <a href="{food:greek-yogurt}">Greek yoghurt</a><a href="{food:grilled-chicken-breast}">Grilled chicken breast</a>
                <a href="{food:broccoli}">Broccoli</a><a href="{food:apple}">Apple</a><a href="{food:quinoa}">Quinoa</a>
                <a href="{food:whole-wheat-bread}">Whole-wheat bread</a>
            </div>
            <p>Browse the full <a href="{site:/foods.html}">food guide</a> to compare more than 700 foods by glycaemic index and calories.</p>
''',
            'faq': [
                ('What is a normal BMI for adults?', 'A healthy BMI is 18.5 to 24.9 for men and women aged 18 and over. For people with a Middle Eastern, Asian or African family background, NICE guidance treats 23 as the start of overweight.'),
                ('How do I work out my ideal weight for my height?', 'Multiply your height in metres squared by 18.5 and by 24.9. For a height of 170 cm (2.89 squared), the healthy range is roughly 53.5 to 72 kg. The calculator above shows this range automatically.'),
                ('Is BMI calculated differently for men and women?', 'The formula and cut-offs are the same for adult men and women, but at the same BMI women carry on average more body fat than men, so a waist measurement helps complete the picture.'),
                ('Can I use this BMI calculator for children?', 'No. Under-18s are assessed with BMI-for-age growth percentiles because body composition changes as they grow. Ask your paediatrician to interpret the values.'),
                ('Why does an athlete show up as overweight?', 'BMI uses total body weight and cannot separate muscle from fat. For athletes, waist size or body-fat percentage is more informative than BMI.'),
                ('What is the difference between BMI and waist-to-height ratio?', 'BMI reflects overall body size, while waist-to-height ratio reflects fat stored around the abdomen, which is more strongly linked to insulin resistance and heart disease. Use both for a better assessment.'),
            ],
            'disclaimer': 'This calculator is an educational screening tool for adults (18 and over). It is not a medical diagnosis and is not suitable during pregnancy or for children. Interpret your result with your doctor or dietitian in the context of your overall health.',
        },
        'nl': {
            'title': 'BMI berekenen: calculator en gezond gewicht | WiBo Health',
            'desc': 'Bereken gratis je BMI volgens de WHO-tabel. Zie je gezonde gewicht bij je lengte, lagere grenzen bij een Midden-Oosterse achtergrond en medisch advies.',
            'h1': 'BMI berekenen: body mass index en gezond gewicht bij jouw lengte',
            'crumb': 'BMI-calculator',
            'cat': 'Medische calculator · Lichaamsmaten',
            'short': 'Body mass index (BMI)',
            'blurb': 'Bepaal je gewichtsklasse en het gezonde gewicht bij je lengte.',
            'about': [{'name': 'Body mass index'}, {'name': 'Obesitas', 'condition': True}, {'name': 'Ondergewicht', 'condition': True}],
            'lead': 'De body mass index (BMI) is wereldwijd het meest gebruikte screeningsmiddel om te zien of je gewicht past bij je lengte. Vul je gewicht en lengte in en je krijgt direct je BMI, de WHO-categorie en het gezonde gewicht bij jouw lengte. Lees daarna de gids hieronder om te begrijpen wat het getal wel en niet zegt.',
            'ui': {
                'card_title': 'Bereken je BMI', 'lbl_weight': 'Gewicht (kg)', 'lbl_height': 'Lengte (cm)',
                'ph_weight': 'bijv. 78', 'ph_height': 'bijv. 175', 'btn': 'Bereken mijn BMI',
                'res_heading': 'Jouw body mass index (BMI)', 'ideal_label': 'Gezond gewicht bij jouw lengte (BMI 18,5 tot 24,9)',
                'prime_label': 'BMI Prime: je BMI ten opzichte van de bovengrens (25)',
                'st_under': 'Ondergewicht', 'st_normal': 'Gezond gewicht', 'st_over': 'Overgewicht',
                'st_ob1': 'Obesitas klasse I', 'st_ob2': 'Obesitas klasse II', 'st_ob3': 'Obesitas klasse III',
                'tip_under': 'Je gewicht ligt onder het gezonde bereik. Bespreek mogelijke oorzaken met je huisarts (zoals schildklierproblemen of een slechte opname van voedingsstoffen) en kies energie- en eiwitrijke basisvoeding in plaats van lege calorieën.',
                'tip_normal': 'Je gewicht ligt in het gezonde bereik. Houd dat vast met regelmatige beweging en gevarieerde voeding, en check ook je taille-lengteratio: buikvet kan toenemen, zelfs bij een normaal gewicht.',
                'tip_over': 'Je gewicht ligt boven het gezonde bereik. Al 5 tot 10% afvallen verbetert je bloeddruk, bloedsuiker en cholesterol merkbaar. Bereken je caloriebehoefte en begin met een gematigd tekort.',
                'tip_obese': 'Je uitkomst valt in het obesitasbereik, wat samenhangt met een hoger risico op diabetes type 2 en hart- en vaatziekten. Een volledige medische controle (HbA1c, cholesterol, bloeddruk) en een gestructureerd afvalplan met een professional worden aangeraden.',
            },
            'body': '''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Wat is de body mass index (BMI)?</span></h2>
            <p>De body mass index is een eenvoudig getal dat je gewicht koppelt aan je lengte. Je ziet er snel mee of je gewicht binnen het gezonde bereik valt, eronder of erboven. Het idee gaat terug op de Belgische wiskundige Adolphe Quetelet in de negentiende eeuw. De Wereldgezondheidsorganisatie (WHO) gebruikt de BMI als internationale standaard voor ondergewicht, overgewicht en obesitas bij volwassenen.</p>
            <p>De BMI is snel, gratis en je hebt alleen een weegschaal en een meetlint nodig. Op bevolkingsniveau hangt hij samen met het vetpercentage en het risico op chronische aandoeningen zoals diabetes type 2, hoge bloeddruk, hart- en vaatziekten en sommige vormen van kanker. Maar de BMI is <strong>een screeningsmiddel en geen diagnose</strong>: hij meet vet niet rechtstreeks en zegt niets over waar het vet zit.</p>

            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>Hoe bereken je de BMI?</span></h2>
            <p>De calculator deelt je gewicht in kilogram door het kwadraat van je lengte in meter:</p>
            <p class="formula-box">BMI = gewicht (kg) ÷ [lengte (m) × lengte (m)]</p>
            <p><strong>Rekenvoorbeeld:</strong> iemand weegt 78 kg en is 175 cm lang. Lengte in het kwadraat = 1,75 × 1,75 = 3,0625, en 78 ÷ 3,0625 = <strong>25,5</strong>: net overgewicht. Het gezonde gewicht bij deze lengte vind je door het kwadraat van de lengte te vermenigvuldigen met de grenzen van het normale bereik: 18,5 × 3,0625 = 56,7 kg en 24,9 × 3,0625 = 76,3 kg.</p>
            <p>De calculator toont ook de <strong>BMI Prime</strong>: je BMI gedeeld door 25, de bovengrens van het gezonde bereik. Een waarde van 1,00 betekent precies op de grens; 1,10 betekent ongeveer 10% erboven.</p>

            <h2 class="section-title"><i class="fas fa-table"></i> <span>BMI-tabel voor volwassenen</span></h2>
            <p>De indeling hieronder volgt het WHO-rapport en geldt voor mannen en vrouwen vanaf 18 jaar:</p>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>Categorie</th><th>BMI (kg/m²)</th><th>Risico op bijkomende ziekten</th></tr></thead>
                <tbody>
                    <tr><td><span class="dot b"></span>Ondergewicht</td><td>onder 18,5</td><td>Laag voor obesitasgerelateerde ziekten, maar hoger risico op ondervoeding, botontkalking en verminderde weerstand</td></tr>
                    <tr><td><span class="dot g"></span>Gezond gewicht</td><td>18,5 – 24,9</td><td>Gemiddeld (referentieniveau)</td></tr>
                    <tr><td><span class="dot y"></span>Overgewicht (pre-obesitas)</td><td>25,0 – 29,9</td><td>Verhoogd</td></tr>
                    <tr><td><span class="dot o"></span>Obesitas klasse I</td><td>30,0 – 34,9</td><td>Matig</td></tr>
                    <tr><td><span class="dot r"></span>Obesitas klasse II</td><td>35,0 – 39,9</td><td>Ernstig</td></tr>
                    <tr><td><span class="dot r"></span>Obesitas klasse III</td><td>40 en hoger</td><td>Zeer ernstig</td></tr>
                </tbody>
            </table></div>

            <h2 class="section-title"><i class="fas fa-earth-asia"></i> <span>Lagere grenzen bij een Midden-Oosterse, Aziatische of Afrikaanse achtergrond</span></h2>
            <p>Het verband tussen BMI en lichaamsvet is niet bij iedere bevolkingsgroep gelijk. De WHO zag dat het risico op diabetes en hartziekten bij Aziatische bevolkingsgroepen al bij lagere waarden stijgt en stelde actiepunten voor bij 23 en 27,5. In de update van 2022 adviseert het Britse NICE deze lagere grenzen voor mensen met een <strong>Midden-Oosterse</strong>, Zuid-Aziatische, Chinese, andere Aziatische, Zwart-Afrikaanse of Afro-Caribische familieachtergrond:</p>
            <ul class="check-list">
                <li><strong>23 tot 27,4:</strong> geldt als overgewicht.</li>
                <li><strong>27,5 en hoger:</strong> geldt als obesitas.</li>
            </ul>
            <p>Heb je zo’n achtergrond en ligt je BMI tussen 23 en 25? Stop dan niet bij “gezond gewicht”, maar meet je buikomvang met de <a href="{calc:whtr}">taille-lengteratio calculator</a> en laat bij je volgende controle je nuchtere glucose of HbA1c meten.</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Wanneer is de BMI minder betrouwbaar?</span></h2>
            <ul class="check-list">
                <li><strong>Sporters en mensen met veel spiermassa:</strong> spieren zijn zwaarder dan vet, dus een sporter kan in de categorie “overgewicht” vallen met weinig lichaamsvet.</li>
                <li><strong>Ouderen:</strong> met de leeftijd neemt spiermassa af en vet toe, waardoor de BMI normaal kan lijken terwijl het vetpercentage hoog is.</li>
                <li><strong>Kinderen en jongeren (onder 18):</strong> zij worden beoordeeld met groeicurven naar leeftijd en geslacht, niet met deze tabel.</li>
                <li><strong>Zwangerschap en borstvoeding:</strong> het gewicht verandert om natuurlijke redenen; gewichtstoename volg je met je verloskundige of arts.</li>
                <li><strong>Vochtophoping, oedeem of amputatie:</strong> het gewicht verandert om redenen die niets met vet te maken hebben.</li>
                <li><strong>Vetverdeling:</strong> de BMI ziet geen verschil tussen heupvet en het riskantere buikvet rond de organen; combineer hem daarom altijd met een buikomvangmeting.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>Wat doe je met je uitkomst? Praktisch medisch advies</span></h2>
            <h3>Bij ondergewicht</h3>
            <p>Onbedoeld ondergewicht verdient een medische check, zeker bij snel gewichtsverlies, vermoeidheid of darmklachten. Voeg calorieën toe met voedzame producten zoals noten, peulvruchten, yoghurt en volle zuivel, en doe krachttraining zodat het extra gewicht spier wordt en geen vet.</p>
            <h3>Bij een gezond gewicht</h3>
            <p>Het doel is om daar te blijven: 150 tot 300 minuten matig intensief bewegen per week zoals de WHO aanbeveelt, twee dagen krachttraining, voldoende slaap en een bord met groente, goede eiwitten en volkoren producten.</p>
            <h3>Bij overgewicht of obesitas</h3>
            <p>Je hoeft geen “ideaal gewicht” te bereiken om gezonder te worden. In het Amerikaanse Diabetes Prevention Program verlaagde ongeveer 7% gewichtsverlies met 150 minuten beweging per week het risico op diabetes type 2 met 58% bij mensen met prediabetes. Begin met deze stappen:</p>
            <ol class="steps">
                <li>Bereken je dagelijkse caloriebehoefte met de <a href="{calc:tdee}">TDEE-calorieëncalculator</a> en begin met een gematigd tekort van ongeveer 20% in plaats van een crashdieet.</li>
                <li>Vul je bord voor de helft met groente, een kwart met eiwit (kip, vis, ei, peulvruchten) en een kwart met volkoren zetmeel met een lage glykemische index.</li>
                <li>Vervang suikerhoudende dranken door water; bereken hoeveel je nodig hebt met de <a href="{calc:water}">waterbehoefte-calculator</a>.</li>
                <li>Meet elke maand je buikomvang: een kleinere taille laat verlies van buikvet zien, ook als de weegschaal trager daalt.</li>
                <li>Gebruik je medicijnen tegen diabetes of hoge bloeddruk? Overleg dan met je arts voordat je flink minder gaat eten, want de dosering moet misschien worden aangepast.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>Voedingsmiddelen die helpen bij gewichtsbeheersing</span></h2>
            <p>Deze producten zijn rijk aan vezels of eiwit en geven langer een vol gevoel. Open ze om calorieën, glykemische index en alle voedingswaarden te zien:</p>
            <div class="food-links">
                <a href="{food:oatmeal}">Havermout</a><a href="{food:lentils}">Linzen</a><a href="{food:chickpeas}">Kikkererwten</a>
                <a href="{food:greek-yogurt}">Griekse yoghurt</a><a href="{food:grilled-chicken-breast}">Gegrilde kipfilet</a>
                <a href="{food:broccoli}">Broccoli</a><a href="{food:apple}">Appel</a><a href="{food:quinoa}">Quinoa</a>
                <a href="{food:whole-wheat-bread}">Volkorenbrood</a>
            </div>
            <p>Bekijk de volledige <a href="{site:/foods.html}">voedingsgids</a> om meer dan 700 producten te vergelijken op glykemische index en calorieën.</p>
''',
            'faq': [
                ('Wat is een normale BMI voor volwassenen?', 'Een gezonde BMI ligt tussen 18,5 en 24,9 voor mannen en vrouwen vanaf 18 jaar. Bij een Midden-Oosterse, Aziatische of Afrikaanse familieachtergrond hanteert NICE 23 als begin van overgewicht.'),
                ('Hoe bereken ik mijn ideale gewicht bij mijn lengte?', 'Vermenigvuldig je lengte in meter in het kwadraat met 18,5 en met 24,9. Bij 170 cm (kwadraat 2,89) ligt het gezonde gewicht tussen ongeveer 53,5 en 72 kg. De calculator hierboven toont dit bereik automatisch.'),
                ('Wordt de BMI voor mannen en vrouwen anders berekend?', 'De formule en grenzen zijn voor volwassen mannen en vrouwen gelijk, maar vrouwen hebben bij dezelfde BMI gemiddeld meer lichaamsvet. Een buikomvangmeting maakt het beeld completer.'),
                ('Kan ik deze BMI-calculator voor kinderen gebruiken?', 'Nee. Bij kinderen en jongeren onder 18 jaar wordt de BMI beoordeeld met groeicurven naar leeftijd en geslacht, omdat hun lichaamssamenstelling verandert. Vraag je huisarts of de jeugdarts om uitleg.'),
                ('Waarom heeft een sporter volgens de BMI overgewicht?', 'De BMI rekent met het totale gewicht en ziet geen verschil tussen spieren en vet. Bij sporters zeggen buikomvang of vetpercentage meer dan de BMI.'),
                ('Wat is het verschil tussen BMI en taille-lengteratio?', 'De BMI zegt iets over je totale lichaamsomvang, de taille-lengteratio over vet rond de buik, dat sterker samenhangt met insulineresistentie en hartziekten. Gebruik beide voor een betere inschatting.'),
            ],
            'disclaimer': 'Deze calculator is een educatief screeningsmiddel voor volwassenen (18 jaar en ouder). Het is geen medische diagnose en niet geschikt tijdens de zwangerschap of voor kinderen. Bespreek je uitkomst met je arts of diëtist in het licht van je totale gezondheid.',
        },
    },
}
