"""Waist-to-height ratio (WHtR) calculator content (AR / EN / NL).
Boundaries (NICE 2022, Ashwell/Browning): 0.4-0.49 no increased risk, 0.5-0.59 increased, >= 0.6 further increased.
Worked example: height 175 cm, waist 94 cm -> 0.54 (increased); healthy waist < 87.5 cm, i.e. 6.5 cm to lose."""

WHTR = {
    'key': 'whtr',
    'slug': 'whtr-calculator',
    'icon': 'fa-ruler-combined',
    'badge': 'NICE 2022 · Ashwell',
    'published': '2026-10-18',
    'modified': '2026-10-18',
    'references': [
        'Ashwell M, Gunn P, Gibson S. Waist-to-height ratio is a better screening tool than waist circumference and BMI for adult cardiometabolic risk factors: systematic review and meta-analysis. Obes Rev. 2012;13(3):275-286.',
        'Browning LM, Hsieh SD, Ashwell M. A systematic review of waist-to-height ratio as a screening tool for the prediction of cardiovascular disease and diabetes: 0.5 could be a suitable global boundary value. Nutr Res Rev. 2010;23(2):247-269.',
        'National Institute for Health and Care Excellence (NICE). Obesity: identification, assessment and management (CG189), update on waist-to-height ratio. London: NICE; 2022.',
        'World Health Organization. Waist circumference and waist-hip ratio: report of a WHO expert consultation. Geneva: WHO; 2008.',
        'Ross R, Neeland IJ, Yamashita S, et al. Waist circumference as a vital sign in clinical practice: a Consensus Statement from the IAS and ICCR Working Group on Visceral Obesity. Nat Rev Endocrinol. 2020;16(3):177-189.',
    ],
    'content': {
        'ar': {
            'title': 'حاسبة نسبة الخصر إلى الطول WHtR ودهون البطن الحشوية | WiBo Health',
            'desc': 'احسب نسبة الخصر إلى الطول (WHtR) واعرف خطر دهون البطن الحشوية وفق NICE 2022، مع طريقة قياس الخصر الصحيحة وجدول التصنيف ونصائح لإنقاص الكرش.',
            'h1': 'حاسبة نسبة الخصر إلى الطول (WHtR): هل دهون بطنك في النطاق الآمن؟',
            'crumb': 'حاسبة الخصر إلى الطول',
            'cat': 'حاسبة طبية · دهون البطن',
            'short': 'نسبة الخصر إلى الطول WHtR',
            'blurb': 'مؤشر بسيط لدهون البطن الحشوية وخطرها الأيضي.',
            'about': [{'name': 'نسبة الخصر إلى الطول'}, {'name': 'السمنة البطنية', 'condition': True}, {'name': 'مقاومة الإنسولين', 'condition': True}],
            'lead': 'القاعدة بسيطة: <strong>اجعل محيط خصرك أقل من نصف طولك</strong>. تقيس نسبة الخصر إلى الطول الدهون المتركزة حول البطن، وهي أخطر أنواع الدهون أيضياً، وقد تفوقت في دراسات كثيرة على مؤشر كتلة الجسم في كشف خطر السكري وأمراض القلب. أدخل محيط خصرك وطولك لتعرف موقعك فوراً.',
            'ui': {
                'card_title': 'احسب نسبة خصرك إلى طولك', 'lbl_waist': 'محيط الخصر (سم)', 'lbl_height': 'الطول (سم)',
                'ph_waist': 'مثال: 94', 'ph_height': 'مثال: 175', 'btn': 'قيّم دهون البطن',
                'res_heading': 'نسبة محيط خصرك إلى طولك', 'target_label': 'الحد الصحي لمحيط خصرك (نصف طولك)',
                'diff_label': 'ما تحتاج إلى إنقاصه من خصرك', 'ok_diff': 'ضمن الحد ✓',
                'st_low': 'أقل من 0.4: راجع وزنك', 'st_healthy': 'نطاق صحي', 'st_increased': 'خطر صحي متزايد', 'st_high': 'خطر صحي مرتفع',
                'tip_low': 'النسبة أقل من 0.4 قد تعني نحافة أو كتلة عضلية قليلة. تحقق من مؤشر كتلة الجسم وتغذيتك، خاصة إذا كان وزنك ينقص دون قصد.',
                'tip_healthy': 'دهون البطن ضمن النطاق الصحي. حافظ على ذلك بالنشاط المنتظم وقلة السكريات المضافة، وأعد القياس كل بضعة أشهر.',
                'tip_increased': 'لديك دهون بطنية زائدة ترتبط بمقاومة الإنسولين وارتفاع ضغط الدم والدهون. خسارة بضعة سنتيمترات من الخصر تحسّن هذه المؤشرات؛ راجع سكر الدم في فحصك الدوري.',
                'tip_high': 'النسبة 0.6 أو أكثر تعني خطراً مرتفعاً للسكري من النوع الثاني وأمراض القلب. يُنصح بتقييم طبي (السكر التراكمي، الدهون، ضغط الدم، الكبد الدهني) وخطة منظمة لخسارة الوزن.',
            },
            'body': '''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>ما هي نسبة الخصر إلى الطول؟</span></h2>
            <p>نسبة الخصر إلى الطول (Waist-to-Height Ratio أو WHtR) هي ناتج قسمة محيط الخصر على الطول، بالوحدة نفسها. وتكمن قوتها في أنها تقيس <strong>توزيع الدهون</strong> لا الوزن الكلي فقط: فالدهون الحشوية المتراكمة داخل البطن حول الكبد والأمعاء نشطة أيضياً، وتفرز مواد التهابية، وترتبط بقوة بمقاومة الإنسولين والسكري من النوع الثاني والكبد الدهني وارتفاع ضغط الدم وأمراض القلب.</p>
            <p>ولهذا قد يكون شخصان بمؤشر كتلة الجسم نفسه، لكن أحدهما يحمل دهوناً في الأرداف والآخر «كرشاً»، فيختلف خطرهما الصحي اختلافاً كبيراً. وقد خلص تحليل جامع منشور في مجلة Obesity Reviews إلى أن نسبة الخصر إلى الطول أفضل من محيط الخصر ومن مؤشر كتلة الجسم في كشف عوامل الخطر القلبية الأيضية لدى البالغين.</p>

            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>كيف تُحسب النسبة؟</span></h2>
            <p class="formula-box">نسبة الخصر إلى الطول = محيط الخصر (سم) ÷ الطول (سم)</p>
            <p><strong>مثال عملي:</strong> شخص طوله 175 سم ومحيط خصره 94 سم: 94 ÷ 175 = <strong>0.54</strong>، أي في نطاق الخطر المتزايد. والحد الصحي لخصره نصف طوله: 175 ÷ 2 = <strong>87.5 سم</strong>، فيحتاج إلى إنقاص نحو 6.5 سم من محيط خصره.</p>
            <p>ميزة هذه النسبة أن حدها الصحي واحد تقريباً للرجال والنساء ولمختلف الأعراق والأطوال، كما أوضحت مراجعة منهجية منشورة في مجلة Nutrition Research Reviews اقترحت القيمة 0.5 حداً عالمياً.</p>

            <h2 class="section-title"><i class="fas fa-ruler"></i> <span>كيف تقيس محيط خصرك بدقة؟</span></h2>
            <ol class="steps">
                <li>قف مستقيماً وقدماك متقاربتان، وارفع ملابسك عن البطن ليكون القياس على الجلد مباشرة.</li>
                <li>حدد أسفل آخر ضلع وأعلى عظم الحوض على جانبك، وضع شريط القياس <strong>في منتصف المسافة بينهما</strong>، كما توصي منظمة الصحة العالمية وإرشادات NICE.</li>
                <li>اجعل الشريط أفقياً حول البطن، ملامساً للجلد دون أن يضغطه.</li>
                <li>خذ نفساً طبيعياً ثم أخرجه، واقرأ القياس في نهاية الزفير دون شد البطن.</li>
                <li>كرر القياس مرتين وخذ المتوسط، وقِس في الوقت نفسه من اليوم (صباحاً قبل الأكل) لمتابعة التغيّر.</li>
            </ol>
            <p>إذا تعذّر تحديد العظام، فالقياس عند مستوى السرة بديل عملي شائع، لكن التزم بالطريقة نفسها في كل مرة.</p>

            <h2 class="section-title"><i class="fas fa-table"></i> <span>جدول تصنيف نسبة الخصر إلى الطول للبالغين</span></h2>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>النسبة</th><th>التصنيف (NICE 2022)</th><th>ما يعنيه عملياً</th></tr></thead>
                <tbody>
                    <tr><td>أقل من 0.4</td><td><span class="dot b"></span>غير مصنفة</td><td>قد تشير إلى نحافة؛ قيّمها مع مؤشر كتلة الجسم</td></tr>
                    <tr><td>0.40 – 0.49</td><td><span class="dot g"></span>لا يوجد خطر متزايد</td><td>توزيع دهون صحي؛ حافظ عليه</td></tr>
                    <tr><td>0.50 – 0.59</td><td><span class="dot y"></span>خطر صحي متزايد</td><td>دهون بطنية زائدة؛ ابدأ بتغيير نمط الحياة</td></tr>
                    <tr><td>0.60 فأكثر</td><td><span class="dot r"></span>خطر صحي مرتفع</td><td>يُنصح بتقييم طبي ومتابعة منظمة</td></tr>
                </tbody>
            </table></div>
            <p>وللمقارنة، تستخدم منظمة الصحة العالمية حدوداً لمحيط الخصر وحده: خطر متزايد فوق 94 سم للرجال و80 سم للنساء، وخطر مرتفع فوق 102 سم للرجال و88 سم للنساء. لكن هذه الحدود لا تراعي الطول، فالرجل الطويل والقصير يُقيَّمان بالرقم نفسه، وهنا تتفوق نسبة الخصر إلى الطول.</p>

            <h2 class="section-title"><i class="fas fa-code-compare"></i> <span>WHtR أم WHR أم BMI؟</span></h2>
            <ul class="check-list">
                <li><strong>مؤشر كتلة الجسم (BMI):</strong> يقيس حجم الجسم الكلي ولا يميز مكان الدهون. احسبه عبر <a href="{calc:bmi}">حاسبة BMI</a>.</li>
                <li><strong>نسبة الخصر إلى الورك (WHR):</strong> مقياس مختلف يقسم الخصر على محيط الورك، ويحتاج إلى قياسين وحدوده تختلف بين الرجال والنساء.</li>
                <li><strong>نسبة الخصر إلى الطول (WHtR):</strong> قياس واحد للخصر وحد واحد تقريباً للجميع (0.5)، ولذلك أوصت NICE عام 2022 باستخدامها إلى جانب مؤشر كتلة الجسم لدى البالغين ذوي المؤشر الأقل من 35.</li>
            </ul>
            <p>وقد دعا بيان إجماع دولي منشور في مجلة Nature Reviews Endocrinology عام 2020 إلى اعتبار قياس الخصر «علامة حيوية» تُسجَّل في كل زيارة طبية مثل ضغط الدم.</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>متى لا تكون النسبة دقيقة؟</span></h2>
            <ul class="check-list">
                <li><strong>الحمل:</strong> لا تُستخدم أثناء الحمل.</li>
                <li><strong>الأطفال والمراهقون:</strong> إرشادات NICE تخص البالغين، وتقييم الأطفال يكون مع طبيبهم.</li>
                <li><strong>انتفاخ البطن لأسباب طبية:</strong> مثل الاستسقاء أو الفتق أو الانتفاخ الشديد.</li>
                <li><strong>مؤشر كتلة جسم 35 فأكثر:</strong> الخطر مرتفع أصلاً، والقياس الإضافي لا يغير التصنيف كثيراً.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>كيف تُنقص دهون البطن الحشوية؟ نصائح مبنية على الأدلة</span></h2>
            <p>الخبر الجيد أن الدهون الحشوية تستجيب للعلاج غالباً أسرع من الدهون تحت الجلد. أما تمارين البطن وحدها فتقوّي العضلات لكنها <strong>لا تحرق الدهون من مكان محدد</strong>؛ الحل في الجسم كله:</p>
            <ol class="steps">
                <li><strong>عجز معتدل في السعرات:</strong> احسبه عبر <a href="{calc:tdee}">حاسبة السعرات TDEE</a>. فخسارة 5–10% من الوزن تقلل دهون البطن بوضوح.</li>
                <li><strong>نشاط هوائي منتظم:</strong> 150 إلى 300 دقيقة أسبوعياً من المشي السريع أو السباحة أو الدراجة، مع تمارين مقاومة يومين أسبوعياً.</li>
                <li><strong>قلل السكريات المضافة والمشروبات المحلاة والنشويات المكررة:</strong> واختر بدلها أطعمة منخفضة المؤشر الجلايسيمي وغنية بالألياف.</li>
                <li><strong>البروتين والألياف في كل وجبة:</strong> يزيدان الشبع ويحميان الكتلة العضلية أثناء خسارة الوزن.</li>
                <li><strong>النوم والتوتر:</strong> قلة النوم وارتفاع الكورتيزول المزمن يرتبطان بتراكم دهون البطن؛ اجعل النوم 7 ساعات على الأقل.</li>
                <li><strong>افحص سكر الدم:</strong> إذا كانت نسبتك 0.5 فأكثر، اطلب من طبيبك فحص السكر التراكمي والدهون وإنزيمات الكبد.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>أطعمة تدعم خسارة دهون البطن من دليلنا</span></h2>
            <p>أطعمة غنية بالألياف القابلة للذوبان أو أوميغا 3 أو البروتين، مع مؤشرها الجلايسيمي وقيمها الكاملة:</p>
            <div class="food-links">
                <a href="{food:oatmeal}">الشوفان</a><a href="{food:chia-seeds}">بذور الشيا</a><a href="{food:lentils}">العدس</a>
                <a href="{food:grilled-salmon}">السلمون المشوي</a><a href="{food:walnuts}">عين الجمل</a><a href="{food:apple}">التفاح</a>
                <a href="{food:pear}">الإجاص</a><a href="{food:bulgur}">البرغل</a><a href="{food:broccoli}">البروكلي</a>
            </div>
            <p>ولا تنسَ الترطيب الكافي عبر <a href="{calc:water}">حاسبة الماء اليومية</a>، وتصفّح <a href="{site:/foods.html}">دليل الأطعمة</a> لاختيار بدائل منخفضة المؤشر الجلايسيمي.</p>
''',
            'faq': [
                ('ما هي نسبة الخصر إلى الطول الطبيعية؟', 'من 0.4 إلى 0.49 للبالغين، أي أن يكون محيط الخصر أقل من نصف الطول. من 0.5 إلى 0.59 يعني خطراً صحياً متزايداً، و0.6 فأكثر خطراً مرتفعاً وفق NICE 2022.'),
                ('أين أقيس محيط خصري بالضبط؟', 'في منتصف المسافة بين أسفل آخر ضلع وأعلى عظم الحوض، والشريط أفقي على الجلد، في نهاية زفير طبيعي. القياس عند السرة بديل عملي إذا التزمت به في كل مرة.'),
                ('هل نسبة الخصر إلى الطول أفضل من BMI؟', 'في كشف خطر السكري وأمراض القلب نعم في كثير من الدراسات، لأنها تقيس دهون البطن. والأفضل استخدام الاثنين معاً كما توصي NICE.'),
                ('ما الفرق بين WHtR وWHR؟', 'WHtR تقسم الخصر على الطول وحدها الصحي 0.5 للجميع تقريباً، أما WHR فتقسم الخصر على محيط الورك وتحتاج إلى قياسين وحدودها مختلفة للرجال والنساء.'),
                ('هل تمارين البطن تنقص الكرش؟', 'تقوي عضلات البطن لكنها لا تحرق الدهون من البطن تحديداً. ينقص الكرش بعجز السعرات والنشاط الهوائي وتمارين المقاومة وتحسين النوم والغذاء.'),
                ('هل تصلح هذه الحاسبة للأطفال؟', 'الحدود المعروضة هنا للبالغين وفق NICE. يُقيَّم وزن الأطفال ومحيط خصرهم مع طبيب الأطفال باستخدام معايير مناسبة لأعمارهم.'),
            ],
            'disclaimer': 'هذه الحاسبة أداة فحص تثقيفية للبالغين، ولا تُعد تشخيصاً طبياً، ولا تُستخدم أثناء الحمل. إذا كانت نسبتك 0.5 فأكثر فناقش النتيجة مع طبيبك واطلب الفحوصات المناسبة.',
        },
        'en': {
            'title': 'Waist-to-Height Ratio Calculator (WHtR) | WiBo Health',
            'desc': 'Calculate your waist-to-height ratio and belly-fat risk using NICE 2022 cut-offs. Learn how to measure your waist and how to lose visceral fat.',
            'h1': 'Waist-to-Height Ratio Calculator (WHtR): Is Your Belly Fat in the Safe Range?',
            'crumb': 'Waist-to-height calculator',
            'cat': 'Medical calculator · Belly fat',
            'short': 'Waist-to-height ratio (WHtR)',
            'blurb': 'A simple marker of visceral belly fat and metabolic risk.',
            'about': [{'name': 'Waist-to-height ratio'}, {'name': 'Abdominal obesity', 'condition': True}, {'name': 'Insulin resistance', 'condition': True}],
            'lead': 'The rule is simple: <strong>keep your waist to less than half your height</strong>. Waist-to-height ratio measures fat stored around the abdomen, the most metabolically harmful type of fat, and in many studies it outperformed BMI at flagging diabetes and heart-disease risk. Enter your waist and height to see where you stand.',
            'ui': {
                'card_title': 'Calculate your waist-to-height ratio', 'lbl_waist': 'Waist circumference (cm)', 'lbl_height': 'Height (cm)',
                'ph_waist': 'e.g. 94', 'ph_height': 'e.g. 175', 'btn': 'Assess my belly fat',
                'res_heading': 'Your waist-to-height ratio', 'target_label': 'Healthy waist limit (half your height)',
                'diff_label': 'How much your waist needs to shrink', 'ok_diff': 'Within the limit ✓',
                'st_low': 'Below 0.4: check your weight', 'st_healthy': 'Healthy range', 'st_increased': 'Increased health risk', 'st_high': 'High health risk',
                'tip_low': 'A ratio below 0.4 can mean low body weight or little muscle mass. Check your BMI and nutrition, especially if you are losing weight unintentionally.',
                'tip_healthy': 'Your belly fat is in the healthy range. Keep it there with regular activity and little added sugar, and measure again every few months.',
                'tip_increased': 'You carry extra abdominal fat, which is linked to insulin resistance, high blood pressure and high blood lipids. Losing a few centimetres from your waist improves these markers; check your blood sugar at your next check-up.',
                'tip_high': 'A ratio of 0.6 or more means a high risk of type 2 diabetes and heart disease. A medical assessment (HbA1c, lipids, blood pressure, fatty liver) and a structured weight-loss plan are recommended.',
            },
            'body': '''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>What is waist-to-height ratio?</span></h2>
            <p>Waist-to-height ratio (WHtR) is your waist circumference divided by your height, in the same unit. Its strength is that it measures <strong>where fat is stored</strong>, not just total weight. Visceral fat inside the abdomen, around the liver and intestines, is metabolically active, releases inflammatory substances and is strongly linked to insulin resistance, type 2 diabetes, fatty liver, high blood pressure and heart disease.</p>
            <p>Two people with the same BMI can therefore carry very different risks: one stores fat on the hips, the other around the belly. A meta-analysis in Obesity Reviews concluded that waist-to-height ratio is a better screening tool than waist circumference or BMI for adult cardiometabolic risk factors.</p>

            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>How is the ratio calculated?</span></h2>
            <p class="formula-box">Waist-to-height ratio = waist circumference (cm) ÷ height (cm)</p>
            <p><strong>Worked example:</strong> someone who is 175 cm tall with a 94 cm waist: 94 ÷ 175 = <strong>0.54</strong>, in the increased-risk range. Their healthy waist limit is half their height, 175 ÷ 2 = <strong>87.5 cm</strong>, so they would need to lose about 6.5 cm from their waist.</p>
            <p>A big advantage is that the healthy boundary is roughly the same for men and women, different ethnic groups and different heights, as a systematic review in Nutrition Research Reviews showed when it proposed 0.5 as a global boundary value.</p>

            <h2 class="section-title"><i class="fas fa-ruler"></i> <span>How to measure your waist accurately</span></h2>
            <ol class="steps">
                <li>Stand up straight with your feet close together and lift your clothing so the tape sits directly on your skin.</li>
                <li>Find the bottom of your lowest rib and the top of your hip bone on your side, and place the tape <strong>halfway between them</strong>, as WHO and NICE recommend.</li>
                <li>Keep the tape horizontal around your body, touching the skin without compressing it.</li>
                <li>Breathe in normally, breathe out, and read the measurement at the end of the out-breath without pulling your stomach in.</li>
                <li>Measure twice and take the average. To track change, measure at the same time of day (in the morning before eating).</li>
            </ol>
            <p>If you cannot find the bones, measuring at navel level is a common practical alternative; just use the same method every time.</p>

            <h2 class="section-title"><i class="fas fa-table"></i> <span>Waist-to-height ratio chart for adults</span></h2>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>Ratio</th><th>Classification (NICE 2022)</th><th>What it means in practice</th></tr></thead>
                <tbody>
                    <tr><td>below 0.4</td><td><span class="dot b"></span>Not classified</td><td>May point to low body weight; assess together with BMI</td></tr>
                    <tr><td>0.40 – 0.49</td><td><span class="dot g"></span>No increased risk</td><td>Healthy fat distribution; keep it up</td></tr>
                    <tr><td>0.50 – 0.59</td><td><span class="dot y"></span>Increased health risk</td><td>Excess belly fat; start lifestyle changes</td></tr>
                    <tr><td>0.60 and above</td><td><span class="dot r"></span>Further increased (high) risk</td><td>Medical assessment and structured follow-up advised</td></tr>
                </tbody>
            </table></div>
            <p>For comparison, WHO uses waist circumference alone: increased risk above 94 cm for men and 80 cm for women, and substantially increased risk above 102 cm for men and 88 cm for women. Those cut-offs ignore height, so a tall and a short man are judged by the same number, which is where waist-to-height ratio does better.</p>

            <h2 class="section-title"><i class="fas fa-code-compare"></i> <span>WHtR, WHR or BMI?</span></h2>
            <ul class="check-list">
                <li><strong>Body mass index (BMI):</strong> reflects overall body size but not where fat sits. Calculate it with the <a href="{calc:bmi}">BMI calculator</a>.</li>
                <li><strong>Waist-to-hip ratio (WHR):</strong> a different measure that divides the waist by the hip circumference. It needs two measurements and has different cut-offs for men and women.</li>
                <li><strong>Waist-to-height ratio (WHtR):</strong> one waist measurement and roughly one boundary for everyone (0.5). That is why NICE recommended it in 2022 alongside BMI for adults with a BMI below 35.</li>
            </ul>
            <p>An international consensus statement in Nature Reviews Endocrinology (2020) called for waist circumference to be treated as a “vital sign”, recorded at every clinical visit like blood pressure.</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>When is the ratio less reliable?</span></h2>
            <ul class="check-list">
                <li><strong>Pregnancy:</strong> do not use it during pregnancy.</li>
                <li><strong>Children and teenagers:</strong> the NICE boundaries apply to adults; children are assessed with their doctor.</li>
                <li><strong>Abdominal swelling for medical reasons:</strong> such as ascites, a hernia or severe bloating.</li>
                <li><strong>BMI of 35 or more:</strong> the risk is already high, and the extra measurement changes the classification little.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>How to reduce visceral belly fat: evidence-based tips</span></h2>
            <p>The good news is that visceral fat often responds faster than fat under the skin. Sit-ups alone strengthen the muscles but <strong>do not burn fat from one specific spot</strong>; the answer is whole-body change:</p>
            <ol class="steps">
                <li><strong>A moderate calorie deficit:</strong> work it out with the <a href="{calc:tdee}">TDEE calculator</a>. Losing 5–10% of body weight clearly reduces belly fat.</li>
                <li><strong>Regular aerobic activity:</strong> 150 to 300 minutes a week of brisk walking, swimming or cycling, plus resistance training two days a week.</li>
                <li><strong>Cut added sugar, sugary drinks and refined starches:</strong> choose low-GI, high-fibre foods instead.</li>
                <li><strong>Protein and fibre at every meal:</strong> they keep you full and protect muscle during weight loss.</li>
                <li><strong>Sleep and stress:</strong> short sleep and chronically high cortisol are linked to belly-fat build-up; aim for at least 7 hours of sleep.</li>
                <li><strong>Check your blood sugar:</strong> if your ratio is 0.5 or more, ask your doctor for HbA1c, lipids and liver enzymes.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>Foods that support belly-fat loss</span></h2>
            <p>Foods rich in soluble fibre, omega-3 or protein, with their glycaemic index and full nutrition facts:</p>
            <div class="food-links">
                <a href="{food:oatmeal}">Oatmeal</a><a href="{food:chia-seeds}">Chia seeds</a><a href="{food:lentils}">Lentils</a>
                <a href="{food:grilled-salmon}">Grilled salmon</a><a href="{food:walnuts}">Walnuts</a><a href="{food:apple}">Apple</a>
                <a href="{food:pear}">Pear</a><a href="{food:bulgur}">Bulgur</a><a href="{food:broccoli}">Broccoli</a>
            </div>
            <p>Stay well hydrated with the <a href="{calc:water}">daily water calculator</a>, and browse the <a href="{site:/foods.html}">food guide</a> for low-GI swaps.</p>
''',
            'faq': [
                ('What is a healthy waist-to-height ratio?', '0.4 to 0.49 for adults, meaning your waist is less than half your height. 0.5 to 0.59 means increased health risk, and 0.6 or more means further increased risk according to NICE 2022.'),
                ('Where exactly should I measure my waist?', 'Halfway between the bottom of your lowest rib and the top of your hip bone, with the tape horizontal on bare skin, at the end of a normal out-breath. Measuring at the navel is a practical alternative if you use it consistently.'),
                ('Is waist-to-height ratio better than BMI?', 'For flagging diabetes and heart-disease risk, yes in many studies, because it captures belly fat. Using both together, as NICE recommends, is best.'),
                ('What is the difference between WHtR and WHR?', 'WHtR divides your waist by your height and has a healthy boundary of about 0.5 for everyone. WHR divides your waist by your hip circumference, needs two measurements and has different cut-offs for men and women.'),
                ('Do sit-ups reduce belly fat?', 'They strengthen your abdominal muscles but do not burn fat specifically from your belly. Belly fat goes down with a calorie deficit, aerobic activity, resistance training, better sleep and a better diet.'),
                ('Can children use this calculator?', 'The boundaries shown here are for adults under NICE guidance. Children’s weight and waist are assessed with their doctor using age-appropriate standards.'),
            ],
            'disclaimer': 'This calculator is an educational screening tool for adults. It is not a medical diagnosis and should not be used during pregnancy. If your ratio is 0.5 or more, discuss the result with your doctor and ask about appropriate tests.',
        },
        'nl': {
            'title': 'Taille-lengteratio berekenen (WHtR) | WiBo Health',
            'desc': 'Bereken je taille-lengteratio en je risico op buikvet volgens NICE 2022. Lees hoe je je buikomvang meet en hoe je visceraal vet verliest.',
            'h1': 'Taille-lengteratio berekenen (WHtR): zit je buikvet in het veilige bereik?',
            'crumb': 'Taille-lengteratio',
            'cat': 'Medische calculator · Buikvet',
            'short': 'Taille-lengteratio (WHtR)',
            'blurb': 'Een eenvoudige maat voor buikvet en stofwisselingsrisico.',
            'about': [{'name': 'Taille-lengteratio'}, {'name': 'Abdominale obesitas', 'condition': True}, {'name': 'Insulineresistentie', 'condition': True}],
            'lead': 'De regel is eenvoudig: <strong>houd je buikomvang onder de helft van je lengte</strong>. De taille-lengteratio meet het vet rond je buik, het schadelijkste vet voor je stofwisseling. In veel studies voorspelde hij het risico op diabetes en hartziekten beter dan de BMI. Vul je buikomvang en lengte in en zie direct waar je staat.',
            'ui': {
                'card_title': 'Bereken je taille-lengteratio', 'lbl_waist': 'Buikomvang (cm)', 'lbl_height': 'Lengte (cm)',
                'ph_waist': 'bijv. 94', 'ph_height': 'bijv. 175', 'btn': 'Beoordeel mijn buikvet',
                'res_heading': 'Jouw taille-lengteratio', 'target_label': 'Gezonde grens voor je buikomvang (halve lengte)',
                'diff_label': 'Hoeveel je buikomvang moet afnemen', 'ok_diff': 'Binnen de grens ✓',
                'st_low': 'Onder 0,4: check je gewicht', 'st_healthy': 'Gezond bereik', 'st_increased': 'Verhoogd gezondheidsrisico', 'st_high': 'Hoog gezondheidsrisico',
                'tip_low': 'Een ratio onder 0,4 kan wijzen op een laag gewicht of weinig spiermassa. Check je BMI en voeding, zeker als je onbedoeld afvalt.',
                'tip_healthy': 'Je buikvet ligt in het gezonde bereik. Houd dat zo met regelmatige beweging en weinig toegevoegde suiker, en meet elke paar maanden opnieuw.',
                'tip_increased': 'Je hebt extra buikvet, wat samenhangt met insulineresistentie, hoge bloeddruk en een hoog cholesterol. Een paar centimeter minder buikomvang verbetert deze waarden; laat je bloedsuiker meten bij je volgende controle.',
                'tip_high': 'Een ratio van 0,6 of meer betekent een hoog risico op diabetes type 2 en hart- en vaatziekten. Een medische beoordeling (HbA1c, cholesterol, bloeddruk, leververvetting) en een gestructureerd afvalplan worden aangeraden.',
            },
            'body': '''
            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>Wat is de taille-lengteratio?</span></h2>
            <p>De taille-lengteratio (Waist-to-Height Ratio, WHtR) is je buikomvang gedeeld door je lengte, in dezelfde eenheid. De kracht ervan is dat hij meet <strong>waar het vet zit</strong>, niet alleen hoeveel je weegt. Visceraal vet in de buikholte, rond de lever en darmen, is stofwisselingsactief, geeft ontstekingsstoffen af en hangt sterk samen met insulineresistentie, diabetes type 2, leververvetting, hoge bloeddruk en hart- en vaatziekten.</p>
            <p>Twee mensen met dezelfde BMI kunnen daardoor een heel ander risico hebben: de een slaat vet op rond de heupen, de ander rond de buik. Een meta-analyse in Obesity Reviews concludeerde dat de taille-lengteratio een betere screeningsmaat is dan buikomvang of BMI voor cardiometabole risicofactoren bij volwassenen.</p>

            <h2 class="section-title"><i class="fas fa-square-root-variable"></i> <span>Hoe bereken je de ratio?</span></h2>
            <p class="formula-box">Taille-lengteratio = buikomvang (cm) ÷ lengte (cm)</p>
            <p><strong>Rekenvoorbeeld:</strong> iemand van 175 cm met een buikomvang van 94 cm: 94 ÷ 175 = <strong>0,54</strong>, in het bereik van verhoogd risico. De gezonde grens is de helft van de lengte, 175 ÷ 2 = <strong>87,5 cm</strong>, dus de buikomvang zou ongeveer 6,5 cm moeten afnemen.</p>
            <p>Een groot voordeel is dat de gezonde grens ongeveer gelijk is voor mannen en vrouwen, verschillende etnische groepen en verschillende lengtes. Dat bleek uit een systematische review in Nutrition Research Reviews, die 0,5 voorstelde als wereldwijde grenswaarde.</p>

            <h2 class="section-title"><i class="fas fa-ruler"></i> <span>Zo meet je je buikomvang nauwkeurig</span></h2>
            <ol class="steps">
                <li>Sta rechtop met je voeten dicht bij elkaar en til je kleding op, zodat het meetlint direct op je huid ligt.</li>
                <li>Zoek de onderkant van je onderste rib en de bovenkant van je heupbot aan de zijkant, en leg het meetlint <strong>halverwege daartussen</strong>, zoals de WHO en NICE aanraden.</li>
                <li>Houd het meetlint horizontaal rond je lichaam, tegen de huid zonder in te snoeren.</li>
                <li>Adem normaal in en uit en lees de meting af aan het einde van de uitademing, zonder je buik in te trekken.</li>
                <li>Meet twee keer en neem het gemiddelde. Meet voor het volgen van veranderingen steeds op hetzelfde moment van de dag (’s ochtends voor het eten).</li>
            </ol>
            <p>Kun je de botten niet vinden, dan is meten ter hoogte van de navel een gangbaar praktisch alternatief; gebruik dan wel elke keer dezelfde methode.</p>

            <h2 class="section-title"><i class="fas fa-table"></i> <span>Tabel taille-lengteratio voor volwassenen</span></h2>
            <div class="table-wrap"><table class="data-table">
                <thead><tr><th>Ratio</th><th>Indeling (NICE 2022)</th><th>Wat het in de praktijk betekent</th></tr></thead>
                <tbody>
                    <tr><td>onder 0,4</td><td><span class="dot b"></span>Niet ingedeeld</td><td>Kan wijzen op een laag gewicht; beoordeel samen met de BMI</td></tr>
                    <tr><td>0,40 – 0,49</td><td><span class="dot g"></span>Geen verhoogd risico</td><td>Gezonde vetverdeling; houd dit vast</td></tr>
                    <tr><td>0,50 – 0,59</td><td><span class="dot y"></span>Verhoogd gezondheidsrisico</td><td>Te veel buikvet; begin met leefstijlaanpassingen</td></tr>
                    <tr><td>0,60 en hoger</td><td><span class="dot r"></span>Verder verhoogd (hoog) risico</td><td>Medische beoordeling en gestructureerde begeleiding aangeraden</td></tr>
                </tbody>
            </table></div>
            <p>Ter vergelijking: de WHO gebruikt alleen de buikomvang, met een verhoogd risico boven 94 cm bij mannen en 80 cm bij vrouwen, en een sterk verhoogd risico boven 102 cm bij mannen en 88 cm bij vrouwen. Die grenzen houden geen rekening met lengte, waardoor een lange en een korte man met hetzelfde getal worden beoordeeld. Daar doet de taille-lengteratio het beter.</p>

            <h2 class="section-title"><i class="fas fa-code-compare"></i> <span>WHtR, WHR of BMI?</span></h2>
            <ul class="check-list">
                <li><strong>Body mass index (BMI):</strong> zegt iets over je totale lichaamsomvang, maar niet waar het vet zit. Bereken hem met de <a href="{calc:bmi}">BMI-calculator</a>.</li>
                <li><strong>Taille-heupratio (WHR):</strong> een andere maat die de buikomvang deelt door de heupomvang. Daarvoor zijn twee metingen nodig en de grenzen verschillen voor mannen en vrouwen.</li>
                <li><strong>Taille-lengteratio (WHtR):</strong> één meting van de buik en ongeveer één grens voor iedereen (0,5). Daarom adviseerde NICE hem in 2022 naast de BMI voor volwassenen met een BMI onder 35.</li>
            </ul>
            <p>Een internationale consensusverklaring in Nature Reviews Endocrinology (2020) riep op om de buikomvang te behandelen als een “vitale functie”, die bij elk consult wordt genoteerd, net als de bloeddruk.</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Wanneer is de ratio minder betrouwbaar?</span></h2>
            <ul class="check-list">
                <li><strong>Zwangerschap:</strong> gebruik hem niet tijdens de zwangerschap.</li>
                <li><strong>Kinderen en jongeren:</strong> de NICE-grenzen gelden voor volwassenen; kinderen worden beoordeeld met hun arts.</li>
                <li><strong>Een dikke buik door een medische oorzaak:</strong> zoals ascites, een breuk of ernstige opgeblazenheid.</li>
                <li><strong>BMI van 35 of hoger:</strong> het risico is dan al hoog en de extra meting verandert de indeling weinig.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>Hoe verlies je buikvet? Onderbouwde tips</span></h2>
            <p>Het goede nieuws: visceraal vet reageert vaak sneller dan het vet onder de huid. Buikspieroefeningen alleen versterken de spieren, maar <strong>verbranden geen vet op één specifieke plek</strong>; de oplossing zit in je hele lichaam:</p>
            <ol class="steps">
                <li><strong>Een gematigd calorietekort:</strong> bereken het met de <a href="{calc:tdee}">TDEE-calculator</a>. 5–10% gewichtsverlies vermindert het buikvet duidelijk.</li>
                <li><strong>Regelmatige duurbeweging:</strong> 150 tot 300 minuten per week stevig wandelen, zwemmen of fietsen, plus twee dagen per week krachttraining.</li>
                <li><strong>Minder toegevoegde suiker, frisdrank en geraffineerd zetmeel:</strong> kies in plaats daarvan producten met een lage glykemische index en veel vezels.</li>
                <li><strong>Eiwit en vezels bij elke maaltijd:</strong> ze verzadigen en beschermen je spiermassa tijdens het afvallen.</li>
                <li><strong>Slaap en stress:</strong> kort slapen en langdurig verhoogd cortisol hangen samen met meer buikvet; streef naar minstens 7 uur slaap.</li>
                <li><strong>Laat je bloedsuiker controleren:</strong> is je ratio 0,5 of hoger, vraag je arts dan naar HbA1c, cholesterol en leverwaarden.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>Voeding die helpt bij het verliezen van buikvet</span></h2>
            <p>Producten rijk aan oplosbare vezels, omega-3 of eiwit, met hun glykemische index en alle voedingswaarden:</p>
            <div class="food-links">
                <a href="{food:oatmeal}">Havermout</a><a href="{food:chia-seeds}">Chiazaad</a><a href="{food:lentils}">Linzen</a>
                <a href="{food:grilled-salmon}">Gegrilde zalm</a><a href="{food:walnuts}">Walnoten</a><a href="{food:apple}">Appel</a>
                <a href="{food:pear}">Peer</a><a href="{food:bulgur}">Bulgur</a><a href="{food:broccoli}">Broccoli</a>
            </div>
            <p>Drink voldoende met de <a href="{calc:water}">waterbehoefte-calculator</a> en blader door de <a href="{site:/foods.html}">voedingsgids</a> voor alternatieven met een lage glykemische index.</p>
''',
            'faq': [
                ('Wat is een gezonde taille-lengteratio?', '0,4 tot 0,49 voor volwassenen: je buikomvang is dan minder dan de helft van je lengte. 0,5 tot 0,59 betekent een verhoogd gezondheidsrisico en 0,6 of meer een verder verhoogd risico volgens NICE 2022.'),
                ('Waar moet ik mijn buikomvang precies meten?', 'Halverwege de onderkant van je onderste rib en de bovenkant van je heupbot, met het meetlint horizontaal op de blote huid, aan het einde van een normale uitademing. Meten bij de navel is een praktisch alternatief als je het steeds zo doet.'),
                ('Is de taille-lengteratio beter dan de BMI?', 'Voor het opsporen van risico op diabetes en hartziekten in veel studies wel, omdat hij buikvet meet. Het beste is beide samen te gebruiken, zoals NICE aanraadt.'),
                ('Wat is het verschil tussen WHtR en WHR?', 'WHtR deelt je buikomvang door je lengte en heeft voor iedereen een gezonde grens van ongeveer 0,5. WHR deelt je buikomvang door je heupomvang, vraagt twee metingen en heeft verschillende grenzen voor mannen en vrouwen.'),
                ('Helpen buikspieroefeningen tegen buikvet?', 'Ze versterken je buikspieren, maar verbranden niet specifiek vet op je buik. Buikvet neemt af door een calorietekort, duurbeweging, krachttraining, betere slaap en betere voeding.'),
                ('Kunnen kinderen deze calculator gebruiken?', 'De grenzen hier gelden voor volwassenen volgens NICE. Gewicht en buikomvang van kinderen worden met hun arts beoordeeld met normen die bij hun leeftijd passen.'),
            ],
            'disclaimer': 'Deze calculator is een educatief screeningsmiddel voor volwassenen. Het is geen medische diagnose en is niet bedoeld voor gebruik tijdens de zwangerschap. Is je ratio 0,5 of hoger, bespreek de uitkomst dan met je arts en vraag naar passend onderzoek.',
        },
    },
}
