"""Article content for scripts/generate_article_pages.py (AR / EN / NL).

Body HTML may link foods as {food:<slug>} and site pages as {site:/path}; the generator resolves them per language.
GI figures follow the site's own food pages (GI wording bands: <=55 low, 56-69 medium, >=70 high).
"""

SUGAR_FREE_CEREALS = dict(
    slugs=dict(ar='healthy-sugar-free-breakfast-cereals', en='healthy-sugar-free-breakfast-cereals',
               nl='gezonde-ontbijtgranen-zonder-suiker', sv='frukostflingor-utan-socker'),
    hero='healthy-sugar-free-breakfast-cereal-hero.webp', hero_size=(1400, 781),
    bowl='healthy-whole-grain-cereal-bowl.webp',
    published='2026-10-17', modified='2026-10-17',
    references=[
        'Regulation (EC) No 1924/2006, Annex: nutrition claims "low sugars" (≤5 g/100 g) and "high fibre" (≥6 g/100 g)',
        'EFSA Journal 2010;8(12):1885 (oat beta-glucan and lowering blood cholesterol)',
        'EFSA Journal 2011;9(6):2207 (beta-glucans from oats and barley and normal blood LDL-cholesterol)',
        'Atkinson FS et al. Am J Clin Nutr 2021 (International tables of glycemic index and glycemic load values) — PMID: 34258626',
    ],
    content=dict(
ar=dict(
 title='حبوب الإفطار الصحية الخالية من السكر: دليلك الكامل لبداية يوم نشيطة بدون سكر مضاف | WiBo Health',
 h1='حبوب الإفطار الصحية الخالية من السكر: دليلك الكامل لبداية يوم نشيطة بدون سكر مضاف',
 crumb='حبوب الإفطار الخالية من السكر',
 cat='دليل التسوق الذكي',
 desc='كيف تختار حبوب إفطار صحية بدون سكر مضاف: قراءة الملصق وأسماء السكر المخفية، معايير السكر والألياف، أفضل الخيارات في السوبرماركت، تنبيهات الحساسية، و3 وصفات سريعة.',
 summary='كثير من حبوب الإفطار "الصحية" حلوى مقنعة. تعلّم قراءة الملصق، واكتشف أفضل الخيارات الخالية من السكر المضاف في السوبرماركت.',
 hero_alt='امرأة مبتسمة تتناول وعاء شوفان كامل مع التوت وبذور الشيا على مائدة الإفطار',
 bowl_alt='وعاء حبوب كاملة مع الجوز واللوز والتوت والقرفة يُسكب عليه الحليب',
 about=['Breakfast cereals', 'Added sugar', 'Whole grains', 'Glycemic index'],
 disclaimer='⚖️ إخلاء مسؤولية طبي: المعلومات الواردة في هذا الدليل مقدمة لأغراض التثقيف الصحي والغذائي العام من WiBo Health، بناءً على المراجع والأبحاث المنشورة وتوصيات الهيئة الأوروبية لسلامة الأغذية (EFSA)، ولا تُعتبر تشخيصاً طبياً ولا بديلاً عن استشارة طبيبك أو أخصائي التغذية السريرية.',
 body='''            <h2 class="section-title"><i class="fas fa-store"></i> <span>مقدمة: خديعة "الإفطار الصحي" في السوبرماركت</span></h2>
            <p class="lead">تخيل هذا السيناريو اليومي: تستيقظ بحماس، وتقرر أن تبدأ يوماً صحياً، فتسكب وعاءً من رقائق الإفطار التي تصفها الإعلانات بأنها "غنية بالفيتامينات" و"مصدر للألياف" و"تدعم الرشاقة". لكن بعد ساعتين فقط تنهار طاقتك، وتشعر بخمول وصداع خفيف، ورغبة ملحة في السكريات أو في فنجان قهوة ثانٍ!</p>
            <p>ما الذي حدث؟ كثير من علب حبوب الإفطار المعروضة تحت مسمى "صحي" أو "Fitness" هي في الواقع حلوى مقنعة: بعض الأصناف الشهيرة، خصوصاً الموجهة للأطفال، يصل السكر فيها إلى 30–40% من وزن العبوة؛ أي أن كل ملعقتين تحملان ما يقارب ملعقة من السكر.</p>
            <p>في هذا الدليل العملي المبني على المعايير الأوروبية المعتمدة، ستتعلم كيف تختار حبوب إفطار خالية من السكر المضاف، وكيف تقرأ الملصق الغذائي، وما أفضل الخيارات المتوفرة في السوبرماركت (في هولندا وأوروبا والوطن العربي)، وكيف تحافظ على طاقة مستقرة وذهن صافٍ حتى موعد الغداء.</p>

            <h2 class="section-title"><i class="fas fa-magnifying-glass"></i> <span>1. كيف يختبئ السكر في علب الحبوب؟</span></h2>
            <p>عندما تقرأ قائمة المكونات قد تجد أن كلمة "سكر" (<bdi>Sugar / Suiker</bdi>) ليست المكون الأول، فتظن أن المنتج قليل التحلية. لكن كثيراً من المصنعين يوزعون كمية السكر الكلية على 4 أو 5 مكونات بأسماء مختلفة، فتنزل كل منها إلى أسفل القائمة. إذا رأيت أياً من هذه الأسماء، فاعلم أنها سكر مضاف:</p>
            <ul class="check-list">
                <li><strong>شراب الجلوكوز والفركتوز (Glucose-fructosestroop):</strong> سكر صناعي سريع الامتصاص، والإكثار منه يرتبط بزيادة الدهون في الكبد والبطن.</li>
                <li><strong>المالتوديكسترين (Maltodextrin):</strong> نشاء مصنّع مؤشره الجلايسيمي أعلى من السكر الأبيض نفسه.</li>
                <li><strong>مستخلص شعير المالت (Gerstemoutextract):</strong> يمنح الحبوب لوناً بنياً يوحي بأنها حبوب كاملة، مع حلاوة إضافية.</li>
                <li><strong>أسماء أخرى:</strong> سكر العنب، السكروز، الدكستروز، شراب القيقب، ومركزات عصائر الفواكه.</li>
            </ul>
            <div class="tip"><p><strong>القاعدة الذهبية:</strong> علبة حبوب الإفطار الصحية الحقيقية تتكون غالباً من سطر واحد من المكونات، مثل: "حبوب شوفان كاملة 100%".</p></div>

            <h2 class="section-title"><i class="fas fa-list-check"></i> <span>2. معايير الاختيار: أربعة أرقام تحسم قرارك أمام الرف</span></h2>
            <p>لتتخذ قرارك في ثوانٍ، احفظ هذه الأرقام لكل 100 غرام من المنتج. حدّا السكر والألياف يطابقان شروط الادعاءين الأوروبيين "قليل السكر" و"غني بالألياف":</p>
            <div class="rule-cards">
                <div class="rule-card"><div class="rule-num">&lt; 5 غ</div><h3>السكر (Suikers)</h3><p>إذا كتب على العبوة "بدون سكر مضاف"، فالسكر في الجدول هو السكر الطبيعي الموجود في الحبة نفسها.</p></div>
                <div class="rule-card"><div class="rule-num">≥ 6 غ</div><h3>الألياف (Vezels)</h3><p>والأفضل 8–10 غ. الألياف تبطئ امتصاص السكر وتخفف العبء على البنكرياس.</p></div>
                <div class="rule-card"><div class="rule-num">85–100%</div><h3>الحبوب الكاملة (Volkoren)</h3><p>يجب أن تتصدر الحبوب الكاملة قائمة المكونات.</p></div>
                <div class="rule-card"><div class="rule-num">&lt; 0.5 غ</div><h3>الملح (Zout)</h3><p>كلما قل الملح كان أفضل لضغط الدم.</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-cart-shopping"></i> <span>3. دليل المقارنة والتسوق الذكي</span></h2>
            <p>بدلاً من الحيرة أمام عشرات الماركات، صنّفنا الخيارات الشائعة في ثلاث فئات واضحة:</p>
            <figure class="article-figure">
                <img src="/images/healthy-whole-grain-cereal-bowl.webp" alt="وعاء حبوب كاملة مع الجوز واللوز والتوت والقرفة يُسكب عليه الحليب" width="1100" height="614" loading="lazy" decoding="async">
                <figcaption>وعاء حبوب كاملة بلا سكر مضاف، مع مكسرات نيئة وتوت طازج وقرفة.</figcaption>
            </figure>

            <div class="tier-title tier-gold"><span class="tier-dot"></span> الفئة الأولى: الخيارات الذهبية (أعلى قيمة غذائية وأطول شبع)</div>
            <div class="cereal-cards">
                <div class="cereal-card">
                    <h3>الشوفان الكامل (<bdi>Havermout / Rolled Oats</bdi>)</h3>
                    <div class="chip-row"><span class="chip">370 سعرة</span><span class="chip">سكر مضاف: 0 غ</span><span class="chip">ألياف 10–11 غ</span><span class="chip">بروتين 13 غ</span><span class="chip">GI منخفض (55)</span></div>
                    <p><strong>المكونات:</strong> 100% حبوب شوفان كاملة دون إضافات.</p>
                    <p>يحتوي على ألياف البيتا-جلوكان الذائبة التي تشكل هلاماً في الأمعاء؛ ويساهم بيتا-جلوكان الشوفان في الحفاظ على مستويات الكوليسترول الطبيعية في الدم (ادعاء معتمد من EFSA عند تناول 3 غ يومياً)، ويحرر الطاقة ببطء لساعات.</p>
                    <a class="card-link" href="{food:oatmeal}">القيم الغذائية الكاملة للشوفان ←</a>
                </div>
                <div class="cereal-card">
                    <h3>الموسلي الطبيعي (Muesli zonder suiker)</h3>
                    <div class="chip-row"><span class="chip">سكر مضاف: 0 غ</span><span class="chip">سكر طبيعي 3–4 غ</span><span class="chip">ألياف 9–10 غ</span><span class="chip">GI منخفض (≈45)</span></div>
                    <p><strong>المكونات:</strong> رقائق الشوفان والجاودار والقمح الكامل مع بذور الكتان ومكسرات نيئة.</p>
                    <p><strong>تنبيه:</strong> اختر الموسلي غير المحمص (Ongetoast)، لأن المقرمش غالباً يُحمص بالزيت والسكر.</p>
                    <a class="card-link" href="{food:swiss-muesli-no-sugar}">القيم الغذائية للموسلي ←</a>
                </div>
                <div class="cereal-card">
                    <h3>وسائد القمح المبشور (Shredded Wheat)</h3>
                    <div class="chip-row"><span class="chip">سكر مضاف: 0 غ</span><span class="chip">ألياف ≈12 غ</span><span class="chip">ملح: 0 غ</span><span class="chip hi">GI مرتفع (≈75)</span></div>
                    <p><strong>المكونات:</strong> 100% قمح كامل مبشور ومضغوط بالبخار فقط.</p>
                    <p>غني جداً بالألياف غير الذائبة الداعمة لحركة الأمعاء، وخالٍ من الملح والسكر. مؤشره الجلايسيمي مرتفع نسبياً، لذا أضف إليه بروتيناً ومكسرات.</p>
                </div>
            </div>

            <div class="tier-title tier-ok"><span class="tier-dot"></span> الفئة الثانية: خيارات مقبولة بشروط</div>
            <div class="cereal-cards">
                <div class="cereal-card ok">
                    <h3>رقائق الذرة غير المحلاة (Unsweetened Corn Flakes)</h3>
                    <div class="chip-row"><span class="chip">سكر مضاف: 0 غ</span><span class="chip">ألياف 3–4 غ</span><span class="chip hi">GI مرتفع (≈79)</span></div>
                    <p><strong>المكونات:</strong> ذرة مطحونة مع رشة ملح وفيتامينات مضافة، دون طبقة سكرية.</p>
                    <p><strong>النصيحة:</strong> تُهضم أسرع بكثير من الشوفان، فلا تتناولها وحدها مع حليب خالي الدسم. أضف دائماً بروتيناً ودهوناً صحية (زبادي يوناني مع حفنة جوز أو بذور شيا) لإبطاء ارتفاع السكر.</p>
                    <a class="card-link" href="{food:unsweetened-corn-flakes}">القيم الغذائية لرقائق الذرة ←</a>
                </div>
            </div>

            <div class="tier-title tier-avoid"><span class="tier-dot"></span> الفئة الثالثة: خيارات يُفضل تجنبها</div>
            <div class="cereal-cards">
                <div class="cereal-card avoid">
                    <h3>الجرانولا والكروسلي المقرمشة (<bdi>Cruesli / Crispy Granola</bdi>)</h3>
                    <div class="chip-row"><span class="chip hi">سكر 22–30 غ</span></div>
                    <p>تُخلط الحبوب بزيوت وشراب الجلوكوز ثم تُحمص للحصول على القرمشة، فتقترب في سكرها من قطعة كيك.</p>
                    <a class="card-link" href="{food:granola-honey-nut}">القيم الغذائية للغرانولا ←</a>
                </div>
                <div class="cereal-card avoid">
                    <h3>الحبوب الملونة وحبوب الشوكولاتة للأطفال</h3>
                    <div class="chip-row"><span class="chip hi">سكر 32–42 غ</span><span class="chip hi">ألياف &lt; 1.5 غ</span><span class="chip hi">GI مرتفع</span></div>
                    <p>سكر مرتفع وألياف شبه معدومة، ما يعني ارتفاعاً سريعاً في سكر الدم يتبعه غالباً هبوط في الطاقة والتركيز قبل الظهر.</p>
                </div>
            </div>

            <h2 class="section-title"><i class="fas fa-chart-line"></i> <span>4. لماذا يرتبط الإفطار السكري بتراكم دهون البطن؟</span></h2>
            <p>عندما تبدأ يومك بحبوب محلاة، تحدث سلسلة استجابات سريعة:</p>
            <ol class="steps">
                <li><strong>ارتفاع سريع في الجلوكوز (Glucose Spike):</strong> تصل السكريات البسيطة إلى الدم خلال دقائق، فيرتفع سكر الدم بحدة.</li>
                <li><strong>إفراز كبير للإنسولين:</strong> يفرز البنكرياس كمية كبيرة من الإنسولين لإعادة السكر إلى مستواه.</li>
                <li><strong>تثبيط حرق الدهون:</strong> ما دام الإنسولين مرتفعاً، يتوقف الجسم عن إطلاق الدهون المخزنة لاستخدامها، ويخزن فائض السكر في الكبد والعضلات، والباقي على شكل دهون، منها دهون البطن.</li>
                <li><strong>هبوط ارتدادي (Sugar Crash):</strong> بعد ساعتين أو ثلاث قد ينخفض السكر بسرعة، فتشعر بالتشتت والجوع والرغبة في المعجنات أو الحلويات.</li>
            </ol>
            <p>أما الحبوب الكاملة الخالية من السكر الغنية بالألياف، فتجعل منحنى السكر أهدأ وتبقي الإنسولين أقل، ما يساعد جسمك على الاستمرار في استخدام دهونه مصدراً للطاقة خلال الصباح.</p>

            <h2 class="section-title"><i class="fas fa-seedling"></i> <span>5. إضافات ذكية تحوّل طبقك إلى وجبة مشبعة</span></h2>
            <ul class="check-list">
                <li><strong><a href="{food:walnuts}">عين الجمل (الجوز)</a>:</strong> الحبة الواحدة (نصفان) نحو 26 سعرة من دهون صحية، غنية بحمض ألفا لينولينيك (أوميغا 3 النباتي).</li>
                <li><strong>الكاجو واللوز النيئ:</strong> حفنة صغيرة (10–12 حبة) تمدك بالمغنيسيوم والزنك.</li>
                <li><strong><a href="{food:chia-seeds}">بذور الشيا</a> و<a href="{food:flax-seeds}">الكتان المطحون</a>:</strong> ملعقة طعام من الشيا تضيف نحو 4 غ ألياف، وتمتص الماء فتتحول إلى هلام يمنح شبعاً طويلاً.</li>
                <li><strong><a href="{food:ceylon-cinnamon}">القرفة السيلانية</a>:</strong> مذاق حلو دافئ دون أي سكر، وتشير بعض الدراسات إلى أنها قد تدعم استجابة الجسم للإنسولين.</li>
                <li><strong><a href="{food:blueberry}">التوتيات الطازجة</a>:</strong> مؤشرها الجلايسيمي منخفض، وغنية بالأنثوسيانين المضاد للأكسدة.</li>
            </ul>

            <div class="allergy-box" role="note">
                <h2>⚠️ تنبيه خاص بالحساسية الغذائية</h2>
                <ul>
                    <li><strong>حساسية الجلوتين (الداء البطني - السيلياك):</strong> الشوفان خالٍ من الجلوتين طبيعياً، لكنه غالباً يُحصد ويُطحن في منشآت تُصنّع القمح، فيتلوث به. على مرضى السيلياك شراء الشوفان المعتمد الخالي من الجلوتين فقط (<bdi>Gluten-Free Oats / Glutenvrije haver</bdi>).</li>
                    <li><strong>حساسية المكسرات الشجرية والفول السوداني:</strong> تجنب الجوز والكاجو واللوز وزبدة الفول السوداني، واستبدلها ببذور دوار الشمس أو بذور اليقطين أو بذور الشيا.</li>
                    <li><strong>عدم تحمل اللاكتوز:</strong> استخدم حليباً نباتياً غير محلى (مثل حليب الصويا أو حليب اللوز المدعم بالكالسيوم وفيتامين D) بدل حليب البقر.</li>
                </ul>
            </div>

            <div class="boodi-card">
                <div>
                    <h2>6. افحص علبة الحبوب في ثوانٍ مع تطبيق Boodi</h2>
                    <p>امسح باركود العلبة بكاميرا هاتفك ليكشف لك Boodi السكر الكلي وأسماء السكر المخفية، ودرجة Nutri-Score، وحالة الحلال والمكونات المشبوهة (مثل E471)، ويقترح بدائل أقل سكراً من نفس الرف.</p>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> تعرّف على Boodi</a>
            </div>

            <h2 class="section-title"><i class="fas fa-bowl-food"></i> <span>7. ثلاث وصفات سريعة لإفطار بدون سكر</span></h2>
            <div class="recipe-cards">
                <div class="recipe-card">
                    <h3>الشوفان الليلي (Overnight Oats)</h3>
                    <p><strong>المكونات:</strong> 4 ملاعق كبيرة شوفان كامل + كوب حليب لوز أو شوفان غير محلى + ملعقة صغيرة بذور شيا + رشة قرفة + حفنة توت أزرق.</p>
                    <p><strong>التحضير:</strong> اخلط المكونات في مرطبان، وأغلقه، وضعه في الثلاجة قبل النوم. في الصباح يصبح بقوام بودينغ كريمي جاهز للأكل دون طبخ.</p>
                </div>
                <div class="recipe-card">
                    <h3>وعاء الموسلي مع الزبادي اليوناني</h3>
                    <p><strong>المكونات:</strong> 4 ملاعق موسلي طبيعي بدون سكر + 150 غ <a href="{food:greek-yogurt}">زبادي يوناني</a> كامل الدسم + 4 حبات عين جمل + رشة بذور كتان مطحونة.</p>
                    <p><strong>القيمة:</strong> نحو 15 غ بروتين مع دهون صحية تؤخر الجوع حتى منتصف النهار.</p>
                </div>
                <div class="recipe-card">
                    <h3>طبق الرقائق الدافئ</h3>
                    <p><strong>المكونات:</strong> كوب من رقائق القمح الكامل أو الشوفان + حليب ساخن غير محلى + ملعقة صغيرة <a href="{food:natural-peanut-butter}">زبدة فول سوداني طبيعية 100%</a> (بدون زيت نخيل أو سكر).</p>
                    <p><strong>القيمة:</strong> طاقة دافئة ومريحة للمعدة في الصباحات الباردة. لمن لديهم حساسية الفول السوداني: استخدم زبدة بذور دوار الشمس.</p>
                </div>
            </div>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>8. أسئلة شائعة</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>هل العسل الطبيعي بديل آمن لتحلية الحبوب؟</h3><p>يحتوي العسل على مضادات أكسدة، لكنه أيضياً فركتوز وجلوكوز ويرفع سكر الدم والإنسولين كأي سكر آخر. إن استخدمته فاكتفِ بنصف ملعقة صغيرة، والأفضل تعويد ذائقتك على حلاوة القرفة والفواكه الطازجة.</p></div>
                <div class="faq-item"><h3>هل الحبوب الخالية من السكر مناسبة لمن لديهم مقاومة الإنسولين؟</h3><p>نعم، خصوصاً الشوفان والموسلي الطبيعي، بشرط دمجها دائماً مع بروتين ومكسرات لإبطاء الامتصاص وتجنب الارتفاعات المفاجئة في سكر الدم.</p></div>
                <div class="faq-item"><h3>كيف أعرف أن الموسلي بدون سكر إذا كان الغلاف بلغة أجنبية؟</h3><p>ابحث في جدول القيم الغذائية عن عبارة <em>waarvan suikers</em> (في هولندا)، ويجب ألا تتجاوز 5 غ لكل 100 غ. أو امسح الباركود بتطبيق Boodi ليترجم لك المحتوى ويعطيك تقييماً واضحاً.</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-flag-checkered"></i> <span>الخلاصة</span></h2>
            <p>وجبة الإفطار ليست مجرد طعام لتسكين الجوع، بل هي الإشارة الأولى التي تضبط بها هرمونات جسمك وتركيزك وطاقتك لساعات. استبدال الحبوب السكرية بحبوب كاملة خالية من السكر المضاف من أبسط القرارات الصحية وأكثرها أثراً على قلبك ووزنك ونشاطك اليومي.</p>'''),

en=dict(
 title='Healthy Sugar-Free Breakfast Cereals: The Best Supermarket Choices for Lasting Energy | WiBo Health',
 h1='Healthy Sugar-Free Breakfast Cereals: The Best Supermarket Choices for Lasting Energy',
 crumb='Sugar-free breakfast cereals',
 cat='Smart shopping guide',
 desc='How to choose healthy breakfast cereals with no added sugar: reading the label and hidden sugar names, sugar and fibre thresholds, the best supermarket picks, allergy notes and 3 quick recipes.',
 summary='Many "healthy" breakfast cereals are dessert in disguise. Learn to read the label and find the best cereals with no added sugar in the supermarket.',
 hero_alt='Smiling woman eating a bowl of whole oats with berries and chia seeds at the breakfast table',
 bowl_alt='Bowl of whole-grain cereal with walnuts, almonds, berries and cinnamon as milk is poured in',
 about=['Breakfast cereals', 'Added sugar', 'Whole grains', 'Glycemic index'],
 disclaimer='⚖️ Medical disclaimer: The information in this guide is provided by WiBo Health for general health and nutrition education, based on published research and the recommendations of the European Food Safety Authority (EFSA). It is not a medical diagnosis and does not replace a consultation with your doctor or a clinical dietitian.',
 body='''            <h2 class="section-title"><i class="fas fa-store"></i> <span>Introduction: the "healthy breakfast" trap in the supermarket</span></h2>
            <p class="lead">Picture this everyday scene: you wake up motivated to have a healthy day, so you pour a bowl of cereal that the adverts call "rich in vitamins", "a source of fibre" and "good for your figure". Yet just two hours later your energy crashes, you feel sluggish, maybe a slight headache, and you crave something sweet or a second cup of coffee.</p>
            <p>What happened? Many cereals sold as "healthy" or "fitness" are really dessert in disguise: some popular varieties, especially those aimed at children, contain 30–40% sugar by weight, which means almost one spoonful of sugar in every two spoonfuls of cereal.</p>
            <p>In this practical guide, built on approved European standards, you will learn how to choose breakfast cereals with no added sugar, how to read the nutrition label, which options are actually on the shelves (in the Netherlands, elsewhere in Europe and in the Arab world), and how to keep your energy steady and your mind clear until lunch.</p>

            <h2 class="section-title"><i class="fas fa-magnifying-glass"></i> <span>1. How does sugar hide in cereal boxes?</span></h2>
            <p>When you read the ingredients, "sugar" (suiker) may not be the first item, so the product seems lightly sweetened. But many manufacturers split the total sugar over 4 or 5 ingredients with different names, so each one drops down the list. If you see any of these names, it is added sugar:</p>
            <ul class="check-list">
                <li><strong>Glucose-fructose syrup (glucose-fructosestroop):</strong> a fast-absorbed industrial sugar; eating a lot of it is linked to more fat in the liver and around the belly.</li>
                <li><strong>Maltodextrin:</strong> a processed starch with a glycaemic index higher than white sugar itself.</li>
                <li><strong>Barley malt extract (gerstemoutextract):</strong> gives cereal a brown, "wholegrain" look along with extra sweetness.</li>
                <li><strong>Other names:</strong> grape sugar, sucrose, dextrose, maple syrup and fruit juice concentrates.</li>
            </ul>
            <div class="tip"><p><strong>The golden rule:</strong> a truly healthy cereal usually has a single line of ingredients, such as "100% whole oats".</p></div>

            <h2 class="section-title"><i class="fas fa-list-check"></i> <span>2. Four numbers that decide in front of the shelf</span></h2>
            <p>To decide in seconds, remember these figures per 100 g of product. The sugar and fibre limits match the EU conditions for the claims "low sugar" and "high fibre":</p>
            <div class="rule-cards">
                <div class="rule-card"><div class="rule-num">&lt; 5 g</div><h3>Sugar (suikers)</h3><p>If the pack says "no added sugar", the sugar in the table is the natural sugar of the grain itself.</p></div>
                <div class="rule-card"><div class="rule-num">≥ 6 g</div><h3>Fibre (vezels)</h3><p>Ideally 8–10 g. Fibre slows sugar absorption and eases the load on the pancreas.</p></div>
                <div class="rule-card"><div class="rule-num">85–100%</div><h3>Whole grain (volkoren)</h3><p>Whole grain should be the first ingredient on the list.</p></div>
                <div class="rule-card"><div class="rule-num">&lt; 0.5 g</div><h3>Salt (zout)</h3><p>The less salt, the better for your blood pressure.</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-cart-shopping"></i> <span>3. Comparison and smart shopping guide</span></h2>
            <p>Instead of getting lost among dozens of brands, we sorted the common options into three clear groups:</p>
            <figure class="article-figure">
                <img src="/images/healthy-whole-grain-cereal-bowl.webp" alt="Bowl of whole-grain cereal with walnuts, almonds, berries and cinnamon as milk is poured in" width="1100" height="614" loading="lazy" decoding="async">
                <figcaption>A bowl of whole grains with no added sugar, topped with raw nuts, fresh berries and cinnamon.</figcaption>
            </figure>

            <div class="tier-title tier-gold"><span class="tier-dot"></span> Group 1: the gold choices (most nutrients, longest fullness)</div>
            <div class="cereal-cards">
                <div class="cereal-card">
                    <h3>Whole rolled oats (havermout)</h3>
                    <div class="chip-row"><span class="chip">370 kcal</span><span class="chip">Added sugar: 0 g</span><span class="chip">Fibre 10–11 g</span><span class="chip">Protein 13 g</span><span class="chip">GI low (55)</span></div>
                    <p><strong>Ingredients:</strong> 100% whole oats, nothing added.</p>
                    <p>Oats contain soluble beta-glucan fibre, which forms a gel in the gut; oat beta-glucan contributes to the maintenance of normal blood cholesterol levels (EFSA-authorised claim at 3 g a day), and it releases energy slowly over several hours.</p>
                    <a class="card-link" href="{food:oatmeal}">Full nutrition facts for oats →</a>
                </div>
                <div class="cereal-card">
                    <h3>Natural muesli (muesli zonder suiker)</h3>
                    <div class="chip-row"><span class="chip">Added sugar: 0 g</span><span class="chip">Natural sugar 3–4 g</span><span class="chip">Fibre 9–10 g</span><span class="chip">GI low (≈45)</span></div>
                    <p><strong>Ingredients:</strong> flakes of oats, rye and whole wheat with linseed and raw nuts.</p>
                    <p><strong>Note:</strong> choose untoasted muesli (ongetoast); crunchy muesli is usually baked with oil and sugar.</p>
                    <a class="card-link" href="{food:swiss-muesli-no-sugar}">Nutrition facts for muesli →</a>
                </div>
                <div class="cereal-card">
                    <h3>Shredded wheat (volkoren tarwe)</h3>
                    <div class="chip-row"><span class="chip">Added sugar: 0 g</span><span class="chip">Fibre ≈12 g</span><span class="chip">Salt: 0 g</span><span class="chip hi">GI high (≈75)</span></div>
                    <p><strong>Ingredients:</strong> 100% whole wheat, shredded and steam-pressed.</p>
                    <p>Very rich in insoluble fibre that supports regular bowel movements, and free of salt and sugar. Its glycaemic index is fairly high, so add protein and nuts.</p>
                </div>
            </div>

            <div class="tier-title tier-ok"><span class="tier-dot"></span> Group 2: acceptable, with conditions</div>
            <div class="cereal-cards">
                <div class="cereal-card ok">
                    <h3>Unsweetened corn flakes</h3>
                    <div class="chip-row"><span class="chip">Added sugar: 0 g</span><span class="chip">Fibre 3–4 g</span><span class="chip hi">GI high (≈79)</span></div>
                    <p><strong>Ingredients:</strong> milled corn with a pinch of salt and added vitamins, without a sugar coating.</p>
                    <p><strong>Tip:</strong> they are digested much faster than oats, so do not eat them on their own with skimmed milk. Always add protein and healthy fat (Greek yoghurt with a handful of walnuts or chia seeds) to slow the rise in blood sugar.</p>
                    <a class="card-link" href="{food:unsweetened-corn-flakes}">Nutrition facts for corn flakes →</a>
                </div>
            </div>

            <div class="tier-title tier-avoid"><span class="tier-dot"></span> Group 3: best avoided</div>
            <div class="cereal-cards">
                <div class="cereal-card avoid">
                    <h3>Crunchy granola and cruesli</h3>
                    <div class="chip-row"><span class="chip hi">Sugar 22–30 g</span></div>
                    <p>The grains are mixed with oils and glucose syrup and then baked for crunch, so their sugar content comes close to a slice of cake.</p>
                    <a class="card-link" href="{food:granola-honey-nut}">Nutrition facts for granola →</a>
                </div>
                <div class="cereal-card avoid">
                    <h3>Coloured and chocolate cereals for children</h3>
                    <div class="chip-row"><span class="chip hi">Sugar 32–42 g</span><span class="chip hi">Fibre &lt; 1.5 g</span><span class="chip hi">GI high</span></div>
                    <p>High sugar and almost no fibre mean a fast rise in blood sugar, often followed by a dip in energy and focus before noon.</p>
                </div>
            </div>

            <h2 class="section-title"><i class="fas fa-chart-line"></i> <span>4. Why is a sugary breakfast linked to belly fat?</span></h2>
            <p>When you start the day with sweetened cereal, a quick chain of responses follows:</p>
            <ol class="steps">
                <li><strong>A fast glucose spike:</strong> simple sugars reach the blood within minutes and blood sugar rises sharply.</li>
                <li><strong>A large insulin release:</strong> the pancreas releases a lot of insulin to bring blood sugar back down.</li>
                <li><strong>Fat burning is put on hold:</strong> while insulin is high, the body stops releasing stored fat for fuel and stores the extra sugar in the liver and muscles, and the rest as fat, including belly fat.</li>
                <li><strong>A rebound dip (sugar crash):</strong> two or three hours later blood sugar may drop quickly, leaving you unfocused, hungry and craving pastries or sweets.</li>
            </ol>
            <p>Whole, sugar-free, fibre-rich cereals keep the blood sugar curve calmer and insulin lower, which helps your body keep using its own fat for energy through the morning.</p>

            <h2 class="section-title"><i class="fas fa-seedling"></i> <span>5. Smart toppings that make your bowl filling</span></h2>
            <ul class="check-list">
                <li><strong><a href="{food:walnuts}">Walnuts</a>:</strong> one walnut (two halves) gives about 26 kcal of healthy fat and is rich in alpha-linolenic acid (plant omega-3).</li>
                <li><strong>Raw cashews and almonds:</strong> a small handful (10–12 nuts) provides magnesium and zinc.</li>
                <li><strong><a href="{food:chia-seeds}">Chia seeds</a> and <a href="{food:flax-seeds}">ground linseed</a>:</strong> one tablespoon of chia adds about 4 g of fibre and absorbs water to form a gel that keeps you full for longer.</li>
                <li><strong><a href="{food:ceylon-cinnamon}">Ceylon cinnamon</a>:</strong> a warm, sweet taste without any sugar; some studies suggest it may support the body's response to insulin.</li>
                <li><strong><a href="{food:blueberry}">Fresh berries</a>:</strong> a low glycaemic index and plenty of antioxidant anthocyanins.</li>
            </ul>

            <div class="allergy-box" role="note">
                <h2>⚠️ Food allergy notice</h2>
                <ul>
                    <li><strong>Gluten intolerance (coeliac disease):</strong> oats are naturally gluten-free but are often harvested and milled in facilities that also process wheat, so they get contaminated. People with coeliac disease should only buy certified gluten-free oats (glutenvrije haver).</li>
                    <li><strong>Tree nut and peanut allergy:</strong> avoid walnuts, cashews, almonds and peanut butter, and use sunflower seeds, pumpkin seeds or chia seeds instead.</li>
                    <li><strong>Lactose intolerance:</strong> use an unsweetened plant drink (such as soy or almond drink fortified with calcium and vitamin D) instead of cow's milk.</li>
                </ul>
            </div>

            <div class="boodi-card">
                <div>
                    <h2>6. Check a cereal box in seconds with the Boodi app</h2>
                    <p>Scan the barcode with your phone and Boodi shows the total sugar and hidden sugar names, the Nutri-Score, the halal status and doubtful ingredients (such as E471), and suggests lower-sugar alternatives from the same shelf.</p>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> Discover Boodi</a>
            </div>

            <h2 class="section-title"><i class="fas fa-bowl-food"></i> <span>7. Three quick sugar-free breakfast recipes</span></h2>
            <div class="recipe-cards">
                <div class="recipe-card">
                    <h3>Overnight oats</h3>
                    <p><strong>Ingredients:</strong> 4 tablespoons of whole oats + 1 cup of unsweetened almond or oat drink + 1 teaspoon of chia seeds + a pinch of cinnamon + a handful of blueberries.</p>
                    <p><strong>Method:</strong> mix everything in a jar, close it and put it in the fridge before bed. By morning it has the texture of a creamy pudding, ready to eat without cooking.</p>
                </div>
                <div class="recipe-card">
                    <h3>Muesli bowl with Greek yoghurt</h3>
                    <p><strong>Ingredients:</strong> 4 tablespoons of sugar-free natural muesli + 150 g full-fat <a href="{food:greek-yogurt}">Greek yoghurt</a> + 4 walnuts + a sprinkle of ground linseed.</p>
                    <p><strong>Value:</strong> about 15 g of protein plus healthy fats that keep hunger away until midday.</p>
                </div>
                <div class="recipe-card">
                    <h3>Warm cereal bowl</h3>
                    <p><strong>Ingredients:</strong> 1 cup of whole wheat flakes or oats + hot unsweetened milk + 1 teaspoon of <a href="{food:natural-peanut-butter}">100% natural peanut butter</a> (no palm oil or sugar).</p>
                    <p><strong>Value:</strong> warm, stomach-friendly energy on cold mornings. Peanut allergy? Use sunflower seed butter instead.</p>
                </div>
            </div>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>8. Frequently asked questions</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Is natural honey a safe way to sweeten cereal?</h3><p>Honey contains antioxidants, but metabolically it is fructose and glucose and raises blood sugar and insulin like any other sugar. If you use it, keep it to half a teaspoon; better still, train your taste buds with cinnamon and fresh fruit.</p></div>
                <div class="faq-item"><h3>Are sugar-free cereals suitable for people with insulin resistance?</h3><p>Yes, especially oats and natural muesli, as long as you always combine them with protein and nuts to slow absorption and avoid sudden rises in blood sugar.</p></div>
                <div class="faq-item"><h3>How can I tell muesli is sugar-free if the pack is in another language?</h3><p>Look for <em>waarvan suikers</em> ("of which sugars") in the Dutch nutrition table; it should not exceed 5 g per 100 g. Or scan the barcode with the Boodi app for a translation and a clear rating.</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-flag-checkered"></i> <span>Conclusion</span></h2>
            <p>Breakfast is more than a way to quiet morning hunger: it is the first signal that sets your hormones, focus and energy for hours. Swapping sugary cereals for whole grains with no added sugar is one of the simplest and most effective health decisions for your heart, your weight and your daily energy.</p>'''),

nl=dict(
 title='Gezonde ontbijtgranen zonder suiker: de beste keuzes in de supermarkt | WiBo Health',
 h1='Gezonde ontbijtgranen zonder suiker: de beste keuzes in de supermarkt',
 crumb='Ontbijtgranen zonder suiker',
 cat='Slim boodschappen doen',
 desc='Zo kies je gezonde ontbijtgranen zonder toegevoegde suiker: etiketten en verborgen suikernamen lezen, grenzen voor suiker en vezels, de beste keuzes in de supermarkt, allergietips en 3 snelle recepten.',
 summary='Veel "gezonde" ontbijtgranen zijn eigenlijk vermomde snoep. Leer het etiket lezen en vind de beste ontbijtgranen zonder toegevoegde suiker in de supermarkt.',
 hero_alt='Lachende vrouw die aan de ontbijttafel een kom volkoren havermout met bessen en chiazaad eet',
 bowl_alt='Kom volkoren ontbijtgranen met walnoten, amandelen, bessen en kaneel waarover melk wordt geschonken',
 about=['Breakfast cereals', 'Added sugar', 'Whole grains', 'Glycemic index'],
 disclaimer='⚖️ Medische disclaimer: De informatie in deze gids wordt door WiBo Health verstrekt voor algemene gezondheids- en voedingsvoorlichting, op basis van gepubliceerd onderzoek en de aanbevelingen van de Europese Autoriteit voor Voedselveiligheid (EFSA). Ze vormt geen medische diagnose en vervangt geen consult bij je arts of een klinisch diëtist.',
 body='''            <h2 class="section-title"><i class="fas fa-store"></i> <span>Inleiding: de valkuil van het "gezonde ontbijt" in de supermarkt</span></h2>
            <p class="lead">Herken je dit? Je staat vol goede moed op, wilt gezond beginnen en schenkt een kom ontbijtgranen in die volgens de reclame "rijk aan vitamines", "een bron van vezels" en "goed voor de lijn" zijn. Maar twee uur later zakt je energie in, voel je je loom, misschien met lichte hoofdpijn, en heb je trek in iets zoets of een tweede kop koffie.</p>
            <p>Wat is er gebeurd? Veel ontbijtgranen die als "gezond" of "fitness" worden verkocht, zijn eigenlijk vermomde snoep: sommige populaire soorten, vooral die voor kinderen, bestaan voor 30–40% uit suiker. Bij elke twee lepels ontbijtgranen eet je dan bijna één lepel suiker.</p>
            <p>In deze praktische gids, gebaseerd op erkende Europese normen, leer je hoe je ontbijtgranen zonder toegevoegde suiker kiest, hoe je het voedingsetiket leest, welke opties er echt in de schappen liggen (in Nederland, de rest van Europa en de Arabische wereld) en hoe je energie en focus stabiel blijven tot de lunch.</p>

            <h2 class="section-title"><i class="fas fa-magnifying-glass"></i> <span>1. Hoe verstopt suiker zich in ontbijtgranen?</span></h2>
            <p>Als je de ingrediëntenlijst leest, staat "suiker" misschien niet bovenaan en lijkt het product licht gezoet. Maar veel fabrikanten verdelen de totale hoeveelheid suiker over 4 of 5 ingrediënten met verschillende namen, zodat elk ervan lager op de lijst belandt. Zie je een van deze namen, dan is het toegevoegde suiker:</p>
            <ul class="check-list">
                <li><strong>Glucose-fructosestroop:</strong> een snel opneembare industriële suiker; veel ervan eten hangt samen met meer vet in de lever en rond de buik.</li>
                <li><strong>Maltodextrine:</strong> een bewerkt zetmeel met een hogere glykemische index dan witte suiker zelf.</li>
                <li><strong>Gerstemoutextract:</strong> geeft ontbijtgranen een bruine "volkoren" uitstraling, plus extra zoetheid.</li>
                <li><strong>Andere namen:</strong> druivensuiker, sucrose, dextrose, ahornsiroop en vruchtensapconcentraten.</li>
            </ul>
            <div class="tip"><p><strong>De gouden regel:</strong> echt gezonde ontbijtgranen hebben meestal maar één regel ingrediënten, zoals "100% volkoren haver".</p></div>

            <h2 class="section-title"><i class="fas fa-list-check"></i> <span>2. Vier getallen die beslissen voor het schap</span></h2>
            <p>Onthoud deze waarden per 100 g product om in seconden te kiezen. De grenzen voor suiker en vezels komen overeen met de EU-voorwaarden voor de claims "suikerarm" en "rijk aan vezels":</p>
            <div class="rule-cards">
                <div class="rule-card"><div class="rule-num">&lt; 5 g</div><h3>Suikers</h3><p>Staat er "zonder toegevoegde suiker" op de verpakking, dan is de suiker in de tabel de natuurlijke suiker van de graankorrel zelf.</p></div>
                <div class="rule-card"><div class="rule-num">≥ 6 g</div><h3>Vezels</h3><p>Liefst 8–10 g. Vezels vertragen de opname van suiker en ontlasten de alvleesklier.</p></div>
                <div class="rule-card"><div class="rule-num">85–100%</div><h3>Volkoren</h3><p>Volkoren graan hoort bovenaan de ingrediëntenlijst te staan.</p></div>
                <div class="rule-card"><div class="rule-num">&lt; 0,5 g</div><h3>Zout</h3><p>Hoe minder zout, hoe beter voor je bloeddruk.</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-cart-shopping"></i> <span>3. Vergelijking en slim boodschappen doen</span></h2>
            <p>In plaats van te verdwalen tussen tientallen merken, hebben we de gangbare opties in drie duidelijke groepen ingedeeld:</p>
            <figure class="article-figure">
                <img src="/images/healthy-whole-grain-cereal-bowl.webp" alt="Kom volkoren ontbijtgranen met walnoten, amandelen, bessen en kaneel waarover melk wordt geschonken" width="1100" height="614" loading="lazy" decoding="async">
                <figcaption>Een kom volkoren granen zonder toegevoegde suiker, met ongebrande noten, verse bessen en kaneel.</figcaption>
            </figure>

            <div class="tier-title tier-gold"><span class="tier-dot"></span> Groep 1: de gouden keuzes (meeste voedingsstoffen, langst verzadigd)</div>
            <div class="cereal-cards">
                <div class="cereal-card">
                    <h3>Volkoren havermout (rolled oats)</h3>
                    <div class="chip-row"><span class="chip">370 kcal</span><span class="chip">Toegevoegde suiker: 0 g</span><span class="chip">Vezels 10–11 g</span><span class="chip">Eiwit 13 g</span><span class="chip">GI laag (55)</span></div>
                    <p><strong>Ingrediënten:</strong> 100% volkoren haver, zonder toevoegingen.</p>
                    <p>Haver bevat oplosbare bètaglucaanvezels die in de darm een gel vormen; bètaglucaan uit haver draagt bij tot het behoud van een normaal cholesterolgehalte in het bloed (door EFSA toegestane claim bij 3 g per dag), en het geeft urenlang langzaam energie af.</p>
                    <a class="card-link" href="{food:oatmeal}">Volledige voedingswaarden van havermout →</a>
                </div>
                <div class="cereal-card">
                    <h3>Naturel muesli (muesli zonder suiker)</h3>
                    <div class="chip-row"><span class="chip">Toegevoegde suiker: 0 g</span><span class="chip">Natuurlijke suiker 3–4 g</span><span class="chip">Vezels 9–10 g</span><span class="chip">GI laag (≈45)</span></div>
                    <p><strong>Ingrediënten:</strong> vlokken van haver, rogge en volkoren tarwe met lijnzaad en ongebrande noten.</p>
                    <p><strong>Let op:</strong> kies ongetoaste muesli; krokante muesli wordt meestal met olie en suiker gebakken.</p>
                    <a class="card-link" href="{food:swiss-muesli-no-sugar}">Voedingswaarden van muesli →</a>
                </div>
                <div class="cereal-card">
                    <h3>Shredded wheat (volkoren tarwe)</h3>
                    <div class="chip-row"><span class="chip">Toegevoegde suiker: 0 g</span><span class="chip">Vezels ≈12 g</span><span class="chip">Zout: 0 g</span><span class="chip hi">GI hoog (≈75)</span></div>
                    <p><strong>Ingrediënten:</strong> 100% volkoren tarwe, geraspt en met stoom geperst.</p>
                    <p>Zeer rijk aan onoplosbare vezels die een regelmatige stoelgang ondersteunen, en vrij van zout en suiker. De glykemische index is vrij hoog, dus voeg eiwit en noten toe.</p>
                </div>
            </div>

            <div class="tier-title tier-ok"><span class="tier-dot"></span> Groep 2: acceptabel, onder voorwaarden</div>
            <div class="cereal-cards">
                <div class="cereal-card ok">
                    <h3>Ongezoete cornflakes</h3>
                    <div class="chip-row"><span class="chip">Toegevoegde suiker: 0 g</span><span class="chip">Vezels 3–4 g</span><span class="chip hi">GI hoog (≈79)</span></div>
                    <p><strong>Ingrediënten:</strong> gemalen maïs met een snufje zout en toegevoegde vitamines, zonder suikerlaagje.</p>
                    <p><strong>Tip:</strong> ze worden veel sneller verteerd dan havermout, dus eet ze niet alleen met magere melk. Voeg altijd eiwit en gezond vet toe (Griekse yoghurt met een handje walnoten of chiazaad) om de stijging van de bloedsuiker af te remmen.</p>
                    <a class="card-link" href="{food:unsweetened-corn-flakes}">Voedingswaarden van cornflakes →</a>
                </div>
            </div>

            <div class="tier-title tier-avoid"><span class="tier-dot"></span> Groep 3: liever vermijden</div>
            <div class="cereal-cards">
                <div class="cereal-card avoid">
                    <h3>Krokante granola en cruesli</h3>
                    <div class="chip-row"><span class="chip hi">Suiker 22–30 g</span></div>
                    <p>De granen worden met olie en glucosestroop gemengd en daarna krokant gebakken, waardoor het suikergehalte in de buurt komt van een plak cake.</p>
                    <a class="card-link" href="{food:granola-honey-nut}">Voedingswaarden van granola →</a>
                </div>
                <div class="cereal-card avoid">
                    <h3>Gekleurde en chocolade-ontbijtgranen voor kinderen</h3>
                    <div class="chip-row"><span class="chip hi">Suiker 32–42 g</span><span class="chip hi">Vezels &lt; 1,5 g</span><span class="chip hi">GI hoog</span></div>
                    <p>Veel suiker en bijna geen vezels: de bloedsuiker stijgt snel en daarna volgt vaak een dip in energie en concentratie nog voor de middag.</p>
                </div>
            </div>

            <h2 class="section-title"><i class="fas fa-chart-line"></i> <span>4. Waarom hangt een zoet ontbijt samen met buikvet?</span></h2>
            <p>Begin je de dag met gezoete ontbijtgranen, dan volgt een snelle reeks reacties:</p>
            <ol class="steps">
                <li><strong>Een snelle glucosepiek:</strong> enkelvoudige suikers komen binnen enkele minuten in het bloed en de bloedsuiker stijgt sterk.</li>
                <li><strong>Veel insuline:</strong> de alvleesklier maakt veel insuline aan om de bloedsuiker weer te laten dalen.</li>
                <li><strong>Vetverbranding staat op pauze:</strong> zolang de insuline hoog is, geeft het lichaam geen opgeslagen vet vrij als brandstof en slaat het de extra suiker op in lever en spieren, en de rest als vet, ook als buikvet.</li>
                <li><strong>Een terugslag (suikerdip):</strong> twee à drie uur later kan de bloedsuiker snel dalen, waardoor je je onrustig en hongerig voelt en trek krijgt in gebak of snoep.</li>
            </ol>
            <p>Volkoren, suikervrije en vezelrijke ontbijtgranen houden de bloedsuikercurve rustiger en de insuline lager, zodat je lichaam in de ochtend zijn eigen vet als energiebron kan blijven gebruiken.</p>

            <h2 class="section-title"><i class="fas fa-seedling"></i> <span>5. Slimme toppings voor een verzadigende kom</span></h2>
            <ul class="check-list">
                <li><strong><a href="{food:walnuts}">Walnoten</a>:</strong> één walnoot (twee helften) levert ongeveer 26 kcal aan gezond vet en is rijk aan alfa-linoleenzuur (plantaardig omega-3).</li>
                <li><strong>Ongebrande cashewnoten en amandelen:</strong> een klein handje (10–12 noten) levert magnesium en zink.</li>
                <li><strong><a href="{food:chia-seeds}">Chiazaad</a> en <a href="{food:flax-seeds}">gemalen lijnzaad</a>:</strong> een eetlepel chiazaad geeft ongeveer 4 g extra vezels en neemt water op tot een gel die lang verzadigt.</li>
                <li><strong><a href="{food:ceylon-cinnamon}">Ceylonkaneel</a>:</strong> een warme, zoete smaak zonder suiker; sommige studies wijzen erop dat het de reactie van het lichaam op insuline kan ondersteunen.</li>
                <li><strong><a href="{food:blueberry}">Verse bessen</a>:</strong> een lage glykemische index en veel antioxiderende anthocyanen.</li>
            </ul>

            <div class="allergy-box" role="note">
                <h2>⚠️ Let op bij voedselallergie</h2>
                <ul>
                    <li><strong>Glutenintolerantie (coeliakie):</strong> haver is van nature glutenvrij, maar wordt vaak geoogst en gemalen in bedrijven die ook tarwe verwerken, waardoor het besmet raakt. Mensen met coeliakie kopen alleen gecertificeerde glutenvrije haver.</li>
                    <li><strong>Allergie voor noten en pinda's:</strong> vermijd walnoten, cashewnoten, amandelen en pindakaas, en gebruik in plaats daarvan zonnebloempitten, pompoenpitten of chiazaad.</li>
                    <li><strong>Lactose-intolerantie:</strong> gebruik een ongezoete plantaardige drank (zoals soja- of amandeldrink verrijkt met calcium en vitamine D) in plaats van koemelk.</li>
                </ul>
            </div>

            <div class="boodi-card">
                <div>
                    <h2>6. Check een pak ontbijtgranen in seconden met de Boodi-app</h2>
                    <p>Scan de barcode met je telefoon en Boodi toont de totale suiker en verborgen suikernamen, de Nutri-Score, de halalstatus en twijfelachtige ingrediënten (zoals E471), en stelt suikerarmere alternatieven uit hetzelfde schap voor.</p>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> Ontdek Boodi</a>
            </div>

            <h2 class="section-title"><i class="fas fa-bowl-food"></i> <span>7. Drie snelle suikervrije ontbijtrecepten</span></h2>
            <div class="recipe-cards">
                <div class="recipe-card">
                    <h3>Overnight oats</h3>
                    <p><strong>Ingrediënten:</strong> 4 eetlepels volkoren havermout + 1 kop ongezoete amandel- of haverdrink + 1 theelepel chiazaad + een snufje kaneel + een handje blauwe bessen.</p>
                    <p><strong>Bereiding:</strong> meng alles in een pot, sluit die af en zet hem voor het slapengaan in de koelkast. 's Ochtends heb je een romige pudding die je zonder koken kunt eten.</p>
                </div>
                <div class="recipe-card">
                    <h3>Muesli-bowl met Griekse yoghurt</h3>
                    <p><strong>Ingrediënten:</strong> 4 eetlepels naturel muesli zonder suiker + 150 g volle <a href="{food:greek-yogurt}">Griekse yoghurt</a> + 4 walnoten + een snufje gemalen lijnzaad.</p>
                    <p><strong>Waarde:</strong> ongeveer 15 g eiwit met gezonde vetten die de honger tot de middag uitstellen.</p>
                </div>
                <div class="recipe-card">
                    <h3>Warme ontbijtkom</h3>
                    <p><strong>Ingrediënten:</strong> 1 kop volkoren tarwevlokken of havermout + warme ongezoete melk + 1 theelepel <a href="{food:natural-peanut-butter}">100% natuurlijke pindakaas</a> (zonder palmolie of suiker).</p>
                    <p><strong>Waarde:</strong> warme energie die prettig is voor de maag op koude ochtenden. Pinda-allergie? Gebruik zonnebloempittenpasta.</p>
                </div>
            </div>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>8. Veelgestelde vragen</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Is natuurlijke honing een veilige manier om ontbijtgranen te zoeten?</h3><p>Honing bevat antioxidanten, maar is in de stofwisseling gewoon fructose en glucose en verhoogt de bloedsuiker en insuline zoals elke andere suiker. Gebruik je het toch, houd het dan bij een halve theelepel; beter is het om je smaak te laten wennen aan kaneel en vers fruit.</p></div>
                <div class="faq-item"><h3>Zijn suikervrije ontbijtgranen geschikt bij insulineresistentie?</h3><p>Ja, vooral havermout en naturel muesli, zolang je ze altijd combineert met eiwit en noten om de opname te vertragen en plotselinge bloedsuikerstijgingen te voorkomen.</p></div>
                <div class="faq-item"><h3>Hoe zie ik of muesli suikervrij is?</h3><p>Kijk in de voedingswaardetabel naar <em>waarvan suikers</em>; dat mag niet meer zijn dan 5 g per 100 g. Of scan de barcode met de Boodi-app voor een vertaling en een duidelijke beoordeling.</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-flag-checkered"></i> <span>Conclusie</span></h2>
            <p>Het ontbijt is meer dan een manier om de ochtendhonger te stillen: het is het eerste signaal dat je hormonen, focus en energie voor uren afstemt. Zoete ontbijtgranen vervangen door volkoren granen zonder toegevoegde suiker is een van de eenvoudigste en meest effectieve gezondheidskeuzes voor je hart, je gewicht en je dagelijkse energie.</p>'''),
# Swedish (2026-10-23): Swedish shelf terms (havregryn, müsli, Nyckelhålet, "varav sockerarter"); only EU-authorised
# claims (oat beta-glucan); no cinnamon/insulin claim; neutral scanner wording; signed by Dr. Wassim Habib.
sv=dict(
 named_author=True,
 byline='Av Dr. Wassim Habib',
 title='Frukostflingor utan socker: de bästa valen i butiken för energi som håller | WiBo Health',
 h1='Frukostflingor utan socker: de bästa valen i butiken för energi som håller',
 crumb='Frukostflingor utan socker',
 cat='Smarta inköp',
 desc='Så väljer du frukostflingor utan tillsatt socker: läs näringsdeklarationen och de dolda sockernamnen, gränserna för socker och fiber, de bästa valen i butiken, allergiråd och tre snabba recept.',
 summary='Många ”nyttiga” frukostflingor är efterrätt i förklädnad. Lär dig läsa förpackningen och hitta flingorna utan tillsatt socker.',
 hero_alt='Leende kvinna som äter en skål fullkornshavre med bär och chiafrön vid frukostbordet',
 bowl_alt='Skål med fullkornsflingor, valnötter, mandlar, bär och kanel medan mjölk hälls i',
 about=['Breakfast cereals', 'Added sugar', 'Whole grains', 'Glycemic index'],
 disclaimer='⚖️ Medicinsk ansvarsfriskrivning: informationen i den här guiden är allmän hälso- och kostinformation från WiBo Health, byggd på publicerad forskning och Europeiska livsmedelssäkerhetsmyndighetens (EFSA) bedömningar. Den är ingen medicinsk diagnos och ersätter inte råd från legitimerad hälso- och sjukvårdspersonal, till exempel din läkare eller en legitimerad dietist. Kontakta din vårdcentral eller ring 1177 för sjukvårdsrådgivning.',
 body='''            <h2 class="section-title"><i class="fas fa-store"></i> <span>Inledning: fällan med den ”nyttiga frukosten” i butiken</span></h2>
            <p class="lead">Känner du igen dig? Du vaknar motiverad att leva hälsosamt och häller upp en skål flingor som reklamen kallar ”vitaminrika”, ”en källa till fiber” och ”bra för figuren”. Ändå sjunker energin bara två timmar senare, du blir trög, kanske får lite huvudvärk och längtar efter något sött eller en kopp kaffe till.</p>
            <p>Vad hände? Många flingor som säljs som ”nyttiga” eller ”fitness” är egentligen efterrätt i förklädnad: vissa populära sorter, särskilt de som riktar sig till barn, innehåller 30–40 % socker, alltså nästan en sked socker för varannan sked flingor.</p>
            <p>I den här praktiska guiden, byggd på EU:s regler för näringspåståenden, lär du dig att välja frukostflingor utan tillsatt socker, att läsa näringsdeklarationen, vilka alternativ som faktiskt finns på hyllan och hur du håller energin jämn och huvudet klart ända fram till lunch.</p>

            <h2 class="section-title"><i class="fas fa-magnifying-glass"></i> <span>1. Hur gömmer sig sockret i flingpaketet?</span></h2>
            <p>När du läser ingredienslistan står ”socker” kanske inte först, så produkten verkar bara lätt sötad. Men många tillverkare delar upp sockret på 4–5 ingredienser med olika namn, så att var och en hamnar längre ner i listan. Ser du något av de här namnen är det tillsatt socker:</p>
            <ul class="check-list">
                <li><strong>Glukos-fruktossirap:</strong> ett industriellt socker som tas upp snabbt.</li>
                <li><strong>Maltodextrin:</strong> en bearbetad stärkelse med högt glykemiskt index.</li>
                <li><strong>Kornmaltextrakt:</strong> ger flingorna en brun, ”fullkornsaktig” färg och extra sötma.</li>
                <li><strong>Andra namn:</strong> druvsocker, sackaros, dextros, glukossirap, sirap, lönnsirap och fruktjuicekoncentrat.</li>
            </ul>
            <div class="tip"><p><strong>Den gyllene regeln:</strong> riktigt bra flingor har ofta en enda rad i ingredienslistan, till exempel ”100 % fullkornshavre”.</p></div>

            <h2 class="section-title"><i class="fas fa-list-check"></i> <span>2. Fyra siffror som avgör framför hyllan</span></h2>
            <p>För att bestämma dig på några sekunder, kom ihåg de här värdena per 100 g. Gränserna för socker och fiber är desamma som EU:s villkor för påståendena ”lågt sockerinnehåll” och ”fiberrik”:</p>
            <div class="rule-cards">
                <div class="rule-card"><div class="rule-num">&lt; 5 g</div><h3>Socker (varav sockerarter)</h3><p>Står det ”utan tillsatt socker” på paketet är sockret i tabellen spannmålets eget naturliga socker.</p></div>
                <div class="rule-card"><div class="rule-num">≥ 6 g</div><h3>Fiber</h3><p>Gärna 8–10 g. Fiber gör att sockret tas upp långsammare.</p></div>
                <div class="rule-card"><div class="rule-num">85–100 %</div><h3>Fullkorn</h3><p>Fullkorn ska stå först i ingredienslistan.</p></div>
                <div class="rule-card"><div class="rule-num">&lt; 0,5 g</div><h3>Salt</h3><p>Ju mindre salt, desto bättre.</p></div>
            </div>
            <p>Ett snabbt stöd i svenska butiker är <strong>Nyckelhålet</strong>: symbolen visar att produkten är ett hälsosammare val inom sin grupp, med mer fullkorn och fiber och mindre socker och salt.</p>

            <h2 class="section-title"><i class="fas fa-cart-shopping"></i> <span>3. Jämförelse och smart inköpsguide</span></h2>
            <p>I stället för att gå vilse bland dussintals märken har vi delat in de vanligaste alternativen i tre tydliga grupper (länkarna leder till vår livsmedelsguide, som än så länge finns på engelska):</p>
            <figure class="article-figure">
                <img src="/images/healthy-whole-grain-cereal-bowl.webp" alt="Skål med fullkornsflingor, valnötter, mandlar, bär och kanel medan mjölk hälls i" width="1100" height="614" loading="lazy" decoding="async">
                <figcaption>En skål fullkorn utan tillsatt socker, toppad med naturella nötter, färska bär och kanel.</figcaption>
            </figure>

            <div class="tier-title tier-gold"><span class="tier-dot"></span> Grupp 1: guldvalen (mest näring, längst mättnad)</div>
            <div class="cereal-cards">
                <div class="cereal-card">
                    <h3>Havregryn (fullkornshavre)</h3>
                    <div class="chip-row"><span class="chip">370 kcal</span><span class="chip">Tillsatt socker: 0 g</span><span class="chip">Fiber 10–11 g</span><span class="chip">Protein 13 g</span><span class="chip">GI lågt (55)</span></div>
                    <p><strong>Ingredienser:</strong> 100 % fullkornshavre, inget annat.</p>
                    <p>Havre innehåller den lösliga fibern betaglukan, som bildar en gel i tarmen. Betaglukan från havre bidrar till att upprätthålla normala kolesterolnivåer i blodet (EU-godkänt påstående; den gynnsamma effekten uppnås vid ett dagligt intag av 3 g betaglukan från havre), och havren ger energi som frigörs långsamt under flera timmar.</p>
                    <a class="card-link" href="{food:oatmeal}">Näringsvärden för havre →</a>
                </div>
                <div class="cereal-card">
                    <h3>Müsli utan tillsatt socker</h3>
                    <div class="chip-row"><span class="chip">Tillsatt socker: 0 g</span><span class="chip">Naturligt socker 3–4 g</span><span class="chip">Fiber 9–10 g</span><span class="chip">GI lågt (≈45)</span></div>
                    <p><strong>Ingredienser:</strong> flingor av havre, råg och vete med linfrön och naturella nötter.</p>
                    <p><strong>Tänk på:</strong> välj orostad müsli; knaprig müsli är oftast rostad med olja och socker.</p>
                    <a class="card-link" href="{food:swiss-muesli-no-sugar}">Näringsvärden för müsli →</a>
                </div>
                <div class="cereal-card">
                    <h3>Rågflingor</h3>
                    <div class="chip-row"><span class="chip">Tillsatt socker: 0 g</span><span class="chip">Fiber ≈13 g</span><span class="chip">GI lågt (≈45)</span></div>
                    <p><strong>Ingredienser:</strong> 100 % fullkornsråg, valsad.</p>
                    <p>Ett klassiskt nordiskt val med mycket fiber. Koka som gröt eller blanda med havregryn.</p>
                    <a class="card-link" href="{food:whole-rye-flakes}">Näringsvärden för rågflingor →</a>
                </div>
            </div>

            <div class="tier-title tier-ok"><span class="tier-dot"></span> Grupp 2: godkänt, med villkor</div>
            <div class="cereal-cards">
                <div class="cereal-card ok">
                    <h3>Osötade cornflakes</h3>
                    <div class="chip-row"><span class="chip">Tillsatt socker: 0 g</span><span class="chip">Fiber 3–4 g</span><span class="chip hi">GI högt (≈79)</span></div>
                    <p><strong>Ingredienser:</strong> malen majs med en nypa salt och tillsatta vitaminer, utan sockerglasyr.</p>
                    <p><strong>Tips:</strong> de bryts ner mycket snabbare än havre, så ät dem inte ensamma med lättmjölk. Lägg alltid till protein och nyttigt fett (grekisk yoghurt eller kvarg med en näve valnötter eller chiafrön) så stiger blodsockret långsammare.</p>
                    <a class="card-link" href="{food:unsweetened-corn-flakes}">Näringsvärden för cornflakes →</a>
                </div>
            </div>

            <div class="tier-title tier-avoid"><span class="tier-dot"></span> Grupp 3: bäst att undvika</div>
            <div class="cereal-cards">
                <div class="cereal-card avoid">
                    <h3>Knaprig granola och rostad müsli</h3>
                    <div class="chip-row"><span class="chip hi">Socker 22–30 g</span></div>
                    <p>Flingorna blandas med olja och glukossirap och rostas för att bli knapriga, så sockerhalten närmar sig en bit kaka.</p>
                    <a class="card-link" href="{food:granola-honey-nut}">Näringsvärden för granola →</a>
                </div>
                <div class="cereal-card avoid">
                    <h3>Färgglada flingor och chokladflingor för barn</h3>
                    <div class="chip-row"><span class="chip hi">Socker 32–42 g</span><span class="chip hi">Fiber &lt; 1,5 g</span><span class="chip hi">GI högt</span></div>
                    <p>Mycket socker och nästan ingen fiber ger en snabb blodsockerhöjning, ofta följd av en dipp i energi och koncentration före lunch.</p>
                </div>
            </div>

            <h2 class="section-title"><i class="fas fa-chart-line"></i> <span>4. Vad händer i kroppen efter en söt frukost?</span></h2>
            <p>När du börjar dagen med sötade flingor följer en snabb kedja av reaktioner:</p>
            <ol class="steps">
                <li><strong>En snabb blodsockertopp:</strong> enkla sockerarter når blodet på några minuter och blodsockret stiger kraftigt.</li>
                <li><strong>Mycket insulin frisätts:</strong> bukspottkörteln frisätter mycket insulin för att få ner blodsockret igen.</li>
                <li><strong>Kroppen växlar till lagring:</strong> så länge insulinet är högt använder kroppen mindre av sitt lagrade fett som bränsle och lagrar i stället överskottet av socker.</li>
                <li><strong>En dipp efteråt:</strong> två–tre timmar senare kan blodsockret sjunka snabbt, så att du blir okoncentrerad, hungrig och sugen på bullar eller godis.</li>
            </ol>
            <p>Fullkornsflingor utan socker och med mycket fiber ger en lugnare blodsockerkurva och lägre insulin under förmiddagen.</p>

            <h2 class="section-title"><i class="fas fa-seedling"></i> <span>5. Smarta toppingar som gör skålen mättande</span></h2>
            <ul class="check-list">
                <li><strong><a href="{food:walnuts}">Valnötter</a>:</strong> en valnöt (två halvor) ger ungefär 26 kcal, främst från omättat fett, bland annat växtbaserad omega-3 (alfa-linolensyra).</li>
                <li><strong>Naturella cashewnötter och mandlar:</strong> en liten näve (10–12 nötter) innehåller magnesium och zink.</li>
                <li><strong><a href="{food:chia-seeds}">Chiafrön</a> och <a href="{food:flax-seeds}">krossade linfrön</a>:</strong> en matsked chiafrön ger ungefär 4 g fiber och binder vätska till en gel som mättar länge.</li>
                <li><strong><a href="{food:ceylon-cinnamon}">Ceylonkanel</a>:</strong> en varm, söt smak helt utan socker.</li>
                <li><strong><a href="{food:blueberry}">Färska bär</a>:</strong> lågt glykemiskt index och mycket färgämnen (antocyaniner); blåbär och lingon är klassiska nordiska val.</li>
            </ul>

            <div class="allergy-box" role="note">
                <h2>⚠️ Allergiinformation</h2>
                <ul>
                    <li><strong>Celiaki (glutenintolerans):</strong> havre är naturligt glutenfri men odlas och mals ofta i anläggningar som också hanterar vete och blir då förorenad. Vid celiaki ska du bara köpa havre som är märkt glutenfri.</li>
                    <li><strong>Allergi mot nötter och jordnötter:</strong> undvik valnötter, cashewnötter, mandlar och jordnötssmör, och använd solrosfrön, pumpafrön eller chiafrön i stället.</li>
                    <li><strong>Laktosintolerans:</strong> använd laktosfri mjölk eller en osötad växtdryck (till exempel havre- eller sojadryck berikad med kalcium och D-vitamin).</li>
                </ul>
            </div>

            <div class="boodi-card">
                <div>
                    <h2>6. Granska ett flingpaket på några sekunder med boodi-appen</h2>
                    <p>Skanna streckkoden med mobilen så visar boodi det totala sockerinnehållet och dolda sockernamn, Nutri-Score och tveksamma tillsatser (som E471), och föreslår alternativ med mindre socker från samma hylla.</p>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> Upptäck boodi</a>
            </div>

            <h2 class="section-title"><i class="fas fa-bowl-food"></i> <span>7. Tre snabba frukostrecept utan socker</span></h2>
            <div class="recipe-cards">
                <div class="recipe-card">
                    <h3>Overnight oats</h3>
                    <p><strong>Ingredienser:</strong> 4 matskedar havregryn + 2 dl osötad havre- eller mandeldryck + 1 tesked chiafrön + en nypa kanel + en näve blåbär.</p>
                    <p><strong>Gör så här:</strong> blanda allt i en burk, sätt på locket och ställ in i kylen innan du går och lägger dig. På morgonen har det blivit en krämig pudding som kan ätas direkt.</p>
                </div>
                <div class="recipe-card">
                    <h3>Müsliskål med grekisk yoghurt</h3>
                    <p><strong>Ingredienser:</strong> 4 matskedar müsli utan tillsatt socker + 150 g <a href="{food:greek-yogurt}">grekisk yoghurt</a> eller kvarg + 4 valnötter + ett strö krossade linfrön.</p>
                    <p><strong>Värde:</strong> ungefär 15 g protein och nyttiga fetter som håller hungern borta till lunch.</p>
                </div>
                <div class="recipe-card">
                    <h3>Varm gröt</h3>
                    <p><strong>Ingredienser:</strong> 1 dl havregryn eller rågflingor kokta i mjölk eller vatten + 1 tesked <a href="{food:natural-peanut-butter}">100 % naturligt jordnötssmör</a> (utan palmolja och socker) + färska bär.</p>
                    <p><strong>Värde:</strong> varm och skonsam energi kalla morgnar. Jordnötsallergi? Använd solrosfrösmör i stället.</p>
                </div>
            </div>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>8. Vanliga frågor</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Är honung ett bra sätt att söta flingorna?</h3><p>Honung är i kroppen främst fruktos och glukos och höjer blodsockret och insulinet som annat socker. Om du använder honung, håll dig till en halv tesked; ännu bättre är att vänja smaklökarna vid kanel och färsk frukt.</p></div>
                <div class="faq-item"><h3>Passar flingor utan socker vid insulinresistens?</h3><p>Ja, särskilt havregryn, rågflingor och osötad müsli, så länge du kombinerar dem med protein och nötter så att sockret tas upp långsamt och blodsockret inte stiger plötsligt.</p></div>
                <div class="faq-item"><h3>Hur ser jag att müslin är utan socker?</h3><p>Titta på raden <em>varav sockerarter</em> i näringsdeklarationen; den ska inte vara mer än 5 g per 100 g. Du kan också skanna streckkoden med boodi-appen för en tydlig bedömning.</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-flag-checkered"></i> <span>Sammanfattning</span></h2>
            <p>Frukosten är mer än ett sätt att stilla morgonhungern: den sätter tonen för energin och koncentrationen i flera timmar. Att byta söta flingor mot fullkorn utan tillsatt socker är ett av de enklaste valen du kan göra för din vardagsenergi och din vikt.</p>'''),
    ),
)

# --------------------------------------------------------------------------------------------
# Sections: a hub page (<dir>.html per language) plus a folder for its articles (<dir>/<slug>.html).
# An article joins a section with section='<key>'. draft=True keeps the hub noindex and out of the sitemap.
# --------------------------------------------------------------------------------------------
SECTIONS = dict(
    diabetes=dict(
        dir='diabetes',
        content=dict(
ar=dict(
 title='السكري ومتلازمة الأيض: دليلك الصحي الشامل | WiBo Health',
 h1='السكري ومتلازمة الأيض',
 crumb='السكري ومتلازمة الأيض',
 desc='أدلة WiBo Health المبنية على المراجع العلمية حول السكري ومقاومة الإنسولين ومتلازمة الأيض: التغذية، النشاط البدني، والمتابعة اليومية.',
 intro='أدلة مبسطة ومبنية على المراجع العلمية حول السكري ومقاومة الإنسولين ومتلازمة الأيض، يعدّها فريق WiBo Health لمساعدتك على فهم حالتك والتحدث مع طبيبك بثقة.',
 about=['Diabetes', 'Metabolic syndrome', 'Insulin resistance'],
 disclaimer='⚖️ إخلاء مسؤولية طبي: المحتوى في هذا القسم مقدم لأغراض التثقيف الصحي العام من WiBo Health، ولا يُعتبر تشخيصاً طبياً ولا بديلاً عن استشارة طبيبك أو فريق الرعاية الصحية.'),
en=dict(
 title='Diabetes & Metabolic Health: your complete guide | WiBo Health',
 h1='Diabetes & Metabolic Health',
 crumb='Diabetes & Metabolic Health',
 desc='Evidence-based WiBo Health guides on diabetes, insulin resistance and metabolic syndrome: nutrition, physical activity and day-to-day monitoring.',
 intro='Clear, evidence-based guides on diabetes, insulin resistance and metabolic syndrome, prepared by the WiBo Health team to help you understand your situation and talk to your doctor with confidence.',
 about=['Diabetes', 'Metabolic syndrome', 'Insulin resistance'],
 disclaimer='⚖️ Medical disclaimer: the content in this section is general health education from WiBo Health. It is not a medical diagnosis and does not replace advice from your doctor or care team.'),
nl=dict(
 title='Diabetes & metabole gezondheid: je complete gids | WiBo Health',
 h1='Diabetes & metabole gezondheid',
 crumb='Diabetes & metabole gezondheid',
 desc='Wetenschappelijk onderbouwde gidsen van WiBo Health over diabetes, insulineresistentie en het metabool syndroom: voeding, beweging en dagelijkse controle.',
 intro='Heldere, wetenschappelijk onderbouwde gidsen over diabetes, insulineresistentie en het metabool syndroom, gemaakt door het WiBo Health-team om je situatie beter te begrijpen en met vertrouwen met je arts te praten.',
 about=['Diabetes', 'Metabolic syndrome', 'Insulin resistance'],
 disclaimer='⚖️ Medische disclaimer: de inhoud van deze sectie is algemene gezondheidsvoorlichting van WiBo Health. Het is geen medische diagnose en vervangt geen advies van je arts of zorgteam.'),
# Swedish (2026-10-23): HbA1c in mmol/mol, glucose in mmol/l with a decimal comma; Swedish care pathways (vårdcentral, MVC, 1177)
sv=dict(
 title='Diabetes och metabol hälsa: din kompletta guide | WiBo Health',
 h1='Diabetes och metabol hälsa',
 crumb='Diabetes och metabol hälsa',
 desc='Medicinskt granskade guider från WiBo Health om prediabetes, graviditetsdiabetes och insulinresistens: mat, rörelse, sömn och vad dina provsvar betyder.',
 intro='Tydliga guider, byggda på vetenskapliga källor, om diabetes, insulinresistens och metabolt syndrom. WiBo Health-teamet tar fram dem för att hjälpa dig att förstå din situation och prata tryggt med din vårdcentral eller barnmorska. Blodsockervärden anges i mmol/l och HbA1c i mmol/mol, precis som i svensk vård.',
 about=['Diabetes', 'Metabolic syndrome', 'Insulin resistance'],
 disclaimer='⚖️ Medicinsk ansvarsfriskrivning: innehållet i den här delen är allmän hälsoinformation och utbildning från WiBo Health. Det är ingen medicinsk diagnos och ersätter inte råd, diagnos eller behandling från legitimerad hälso- och sjukvårdspersonal. Kontakta din vårdcentral eller ring 1177 för sjukvårdsrådgivning. Vid akut fara – ring 112.'),
        ),
    ),
)

GESTATIONAL_DIABETES = dict(
    section='diabetes',
    slugs=dict(ar='gestational-diabetes', en='gestational-diabetes', nl='zwangerschapsdiabetes', sv='graviditetsdiabetes'),
    hero='gestational-diabetes-guide-hero.webp', hero_size=(1376, 768),
    thumb='gestational-diabetes-guide-thumb.webp', thumb_size=(640, 357),   # hub card (diabetes.html), 640px copy of the hero
    published='2026-10-20', modified='2026-10-20',
    references=[
        'American Diabetes Association (ADA). Standards of Care in Diabetes—2026, Section 15: Management of Diabetes in Pregnancy. Diabetes Care 2026;49(Suppl 1)',
        'American College of Obstetricians and Gynecologists (ACOG). Practice Bulletin No. 190: Gestational Diabetes Mellitus. Obstet Gynecol 2018;131(2):e49–e64',
        'National Institute for Health and Care Excellence (NICE). Diabetes in pregnancy: management from preconception to the postnatal period (NG3), 2015, updated 2020',
        'International Federation of Gynecology and Obstetrics (FIGO). The FIGO Initiative on gestational diabetes mellitus: a pragmatic guide for diagnosis, management, and care. Int J Gynaecol Obstet 2015;131(Suppl 3):S173–S211',
    ],
    faq_schema=True,                                     # FAQPage JSON-LD built from the body's faq-item blocks
    named_author=True,                                   # user decision 2026-10-20: this guide names Dr. Wassim Habib (byline + schema)
    content=dict(
ar=dict(
 byline='بقلم الدكتور وسيم حبيب',
 title='دليل سكر الحمل الشامل: المعدل الطبيعي بالأرقام، جدول الأكل المسموح والممنوع، وخطة يومك خطوة بخطوة',
 h1='دليل سكر الحمل الشامل: المعدل الطبيعي بالأرقام، جدول الأكل المسموح والممنوع، وخطة يومك خطوة بخطوة',
 crumb='سكر الحمل',
 cat='السكري ومتلازمة الأيض',
 desc='كل ما تحتاجين معرفته عن سكر الحمل: أرقام التحاليل الطبيعية على الريق وبعد الأكل، جدول الأطعمة المسموحة والممنوعة لتسطيح منحنى السكر وحماية جنينك، مع خطة وجبات متوازنة ودليل الأطعمة الشامل من WiBo Health.',
 summary='المعدل الطبيعي بالأرقام، الأطعمة المسموحة والممنوعة، وخطة وجبات يومية متوازنة لتسطيح منحنى السكر.',
 hero_alt='امرأة حامل مبتسمة في مطبخ مشمس تضع حساس قياس السكر على ذراعها وأمامها وعاء توت وأفوكادو',
 about=['Gestational diabetes', 'Pregnancy', 'Blood glucose', 'Glycemic index'],
 disclaimer='⚖️ تنبيه سريري وأمان صحي: هذا الدليل أُعد لأغراض التثقيف الصحي وتعديل نمط الحياة من WiBo Health، وهو مصمم ليتكامل مع خطة الرعاية الطبية التي يقدمها لكِ طبيب النسائية والتوليد المتابع لحملكِ، ولا يُعتبر تشخيصاً طبياً ولا بديلاً عنها.',
 body='''            <h2 class="section-title"><i class="fas fa-heart"></i> <span>اطمئني.. أنتِ وجنينكِ بخير والحل يبدأ بلقمتكِ</span></h2>
            <p class="lead">أول شعور ينتاب الأم عند سماع جملة "سكر الحمل مرتفع" هو الخوف وعتاب النفس: <em>"هل أكلت حلويات كثيرة؟ هل آذيت طفلي؟"</em>.</p>
            <p>الحقيقة الطبية التي نريد أن تطمئني إليها فوراً: <strong>سكر الحمل ليس خطأكِ، ولا يعني أبداً أن طفلكِ مريض بالسكري.</strong> هو ببساطة إشارة من جسمكِ يخبركِ فيها أن هرمونات الحمل القوية تضع عبئاً مؤقتاً على معالجة السكريات، وبخطوات غذائية بسيطة وذكية ستعبرين هذه المرحلة بسلام وصحة فائقة لكِ ولمولودكِ.</p>

            <h2 class="section-title"><i class="fas fa-dna"></i> <span>1. ماذا يحدث في جسمكِ حقاً؟ (السر في هرمونات المشيمة)</span></h2>
            <p>المشيمة ليست مجرد وسيلة لتغذية طفلكِ، بل هي مصنع هرمونات جبار. خلال النصف الثاني من الحمل (خاصة بين الشهرين الخامس والسادس)، تفرز المشيمة هرمونات هدفها الوحيد هو: <em>"تأمين أكبر قدر ممكن من الطاقة والغذاء للجنين ليكبر"</em>.</p>
            <p>لكي تفعل ذلك، تقوم هذه الهرمونات بجعل خلايا جسمكِ أكثر مقاومة للإنسولين (أي تترك السكر في مجرى الدم ليمر للطفل). في الطبيعي، يتدخل البنكرياس ويفرز كميات إضافية مضاعفة من الإنسولين ليوازن الكفة. ولكن عندما يتأخر البنكرياس قليلاً عن مجاراة هذا الطلب الكبير، يرتفع السكر في الدم، ونسمي هذه الحالة <strong>سكر الحمل</strong>.</p>
            <div class="tip"><h3>👶 كيف يتأثر الجنين؟</h3><p>إذا بقي السكر مرتفعاً في دم الأم، يمر هذا السكر الزائد للجنين، فيضطر بنكرياس الجنين الصغير لإفراز إنسولين إضافي ليخزن هذا السكر على شكل دهون، مما قد يجعل وزنه كبيراً عند الولادة. لذلك فإن تحكمكِ في طعامكِ هو أكبر درع حماية لنمو طفلكِ بتناسق وأمان.</p></div>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>2. جدول سكر الحمل: ما هي الأرقام والمعدلات الطبيعية؟</span></h2>
            <p>عند قياس السكر بجهاز الفحص المنزلي، هناك 3 أرقام ذهبية يجب أن تتذكريها دائماً:</p>
            <div class="rule-cards">
                <div class="rule-card"><div class="rule-num"><bdi dir="ltr">&lt; 95 <small>mg/dL</small></bdi></div><h3>على الريق</h3><p>أول ما تستيقظين قبل الإفطار. بالمول (أوروبا): أقل من <bdi>5.3 mmol/L</bdi>.</p></div>
                <div class="rule-card"><div class="rule-num"><bdi dir="ltr">&lt; 140 <small>mg/dL</small></bdi></div><h3>بعد الوجبة بساعة واحدة</h3><p>بالمول (أوروبا): أقل من <bdi>7.8 mmol/L</bdi>.</p></div>
                <div class="rule-card"><div class="rule-num"><bdi dir="ltr">&lt; 120 <small>mg/dL</small></bdi></div><h3>بعد الوجبة بساعتين</h3><p>بالمول (أوروبا): أقل من <bdi>6.7 mmol/L</bdi>.</p></div>
            </div>
            <h3>لماذا يرتفع السكر أحياناً على الريق؟</h3>
            <p>في ساعات الفجر، يفرز الكبد كمية طبيعية من الجلوكوز ليعطيكِ طاقة للاستيقاظ (تسمى ظاهرة الفجر). إذا كان السكر الصباحي يرتفع عندكِ، فالحل ليس تجويع نفسكِ ليلاً، بل تناول وجبة خفيفة ذكية قبل النوم (مثل ملعقة زبدة فول سوداني نقية أو حفنة <a href="{food:walnuts}">جوز</a>) لتثبيت إشارات الكبد، مع إخبار طبيبكِ بأرقامكِ الصباحية.</p>

            <h2 class="section-title"><i class="fas fa-traffic-light"></i> <span>3. جدول الأكل لسكر الحمل: نظام الإشارات المرورية الذكي</span></h2>
            <p>بدلاً من الحرمان القاسي، السر الطبي هو <strong>"تسطيح منحنى السكر"</strong>؛ أي تناول وجبات تُمتص ببطء وهدوء وتمنع القفزات الحادة.</p>

            <div class="tier-title tier-gold"><span class="tier-dot"></span> 🟢 الضوء الأخضر (كلي منها براحة وأمان - أساس طبقكِ)</div>
            <ul class="check-list">
                <li><strong>البروتينات الصافية:</strong> <a href="{food:boiled-egg}">البيض المسلوق</a> أو <a href="{food:egg-omelette}">الأومليت</a>، <a href="{food:grilled-chicken-breast}">صدور الدجاج المشوية</a>، والأسماك الآمنة المطهوة جيداً (كـ<a href="{food:grilled-salmon}">السلمون</a> الغني بدهون أوميغا 3 لبناء دماغ الجنين).</li>
                <li><strong>الدهون الصحية:</strong> <a href="{food:extra-virgin-olive-oil}">زيت الزيتون البكر الممتاز</a>، <a href="{food:avocado}">الأفوكادو</a>، <a href="{food:walnuts}">الجوز (عين الجمل)</a>، واللوز النيء.</li>
                <li><strong>الخضار الورقية والألياف:</strong> <a href="{food:spinach}">السبانخ</a>، <a href="{food:zucchini}">الكوسا</a>، <a href="{food:cucumber}">الخيار</a>، <a href="{food:broccoli}">البروكلي</a>، والخس. (الألياف تعمل مثل الإسفنجة في أمعائكِ، تمتص السكر وتجعله يدخل مجرى الدم ببطء شديد).</li>
            </ul>

            <div class="tier-title tier-ok"><span class="tier-dot"></span> 🟡 الضوء الأصفر (مفيدة ولكن بحساب وذكاء)</div>
            <ul class="check-list">
                <li><strong>الكربوهيدرات المعقدة:</strong> <a href="{food:quinoa}">الكينوا</a>، <a href="{food:oatmeal}">الشوفان الكامل</a> غير السريع، و<a href="{food:sourdough-bread}">خبز الحبة الكاملة المخمر طبيعياً</a> (<bdi>Sourdough</bdi>).</li>
                <li><strong>الفواكه الصديقة للأنسولين:</strong> <a href="{food:blueberry}">التوت الأزرق</a>، <a href="{food:strawberry}">الفراولة</a>، <a href="{food:apple}">التفاح الأخضر</a>. (نصيحة ذهبية: لا تأكلي الفاكهة وحدها أبداً، تناولي معها دائماً بضع حبات لوز أو ملعقة <a href="{food:greek-yogurt}">لبن يوناني</a> لفرملة امتصاص السكر).</li>
            </ul>

            <div class="tier-title tier-avoid"><span class="tier-dot"></span> 🔴 الضوء الأحمر (ابتعدي عنها لحماية استقرار أرقامكِ)</div>
            <ul class="check-list">
                <li><strong>العصائر (حتى الطبيعية والمعصورة طازجة):</strong> العصير عبارة عن سكر مركز مجرد من الألياف، يرفع السكر كالسهم في دقائق معدودة. استبدليه بالفاكهة الكاملة مع شرب الماء.</li>
                <li><strong>المخبوزات والنشويات البيضاء:</strong> الخبز الأبيض، المعجنات، الفطائر، وحبوب الإفطار المحلاة.</li>
                <li><strong>السكريات المقنّعة:</strong> المالتوديكسترين، النشا المعدل، وشراب الذرة، وهي مكونات تُضاف بكثرة لمنتجات "خالية من السكر" لكنها ترفع السكر بشدة!</li>
            </ul>


            <h2 class="section-title"><i class="fas fa-cart-shopping"></i> <span>4. كيف تتسوقين بأمان؟ استعيني بـ "دليل الأطعمة الشامل" في موقعنا</span></h2>
            <p>التسوق في السوبرماركت قد يكون محيراً؛ فكل منتج يكتب عليه <em>"صحي ومناسب للحمية"</em>. لمساعدتكِ في اتخاذ قرار فوري وصحيح:</p>
            <ul class="check-list">
                <li><strong>تصفحي <a href="{site:/foods.html}">دليل الأطعمة في الموقع</a>:</strong> خصصنا لكِ في منصة <strong>WiBo Health</strong> دليلاً سريرياً ضخماً يضم أكثر من 850 صنفاً غذائياً مع تصنيف مؤشرها الجلايسيمي الدقيق وقيمتها الغذائية.</li>
                <li><strong>أضيفي الموقع لشاشة هاتفكِ (تطبيق الويب السريع):</strong> بنقرة واحدة من متصفحكِ (<bdi>Add to Home Screen</bdi>)، يصبح الموقع متاحاً على شاشة هاتفكِ مثل أي تطبيق، لتفتحي الدليل وأنتِ داخل السوبرماركت وتبحثي عن أي منتج قبل وضعه في سلة المشتريات.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>5. خطة يومكِ المتوازن: نموذج وجبات واقعي ومشبع</span></h2>
            <ul class="check-list">
                <li><strong>وجبة الإفطار:</strong> بيضتان مطهوتان بزيت الزيتون مع شرائح أفوكادو وخضار ورقية (جرجير وخيار)، مع ربع رغيف خبز كامل الحبة.</li>
                <li><strong>سناك الصباح:</strong> حفنة صغيرة من عين الجمل (الجوز) مع نصف كوب توت طازج.</li>
                <li><strong>وجبة الغداء:</strong> طبق سلطة ملون كبير بزيت الزيتون والليمون (ابدئي به أولاً)، قطعة سمك أو دجاج مشوي، مع 3 ملاعق كينوا أو <a href="{food:brown-rice}">أرز بني</a> مطبوخ.</li>
                <li><strong>سناك بعد الظهر:</strong> شرائح خيار وجزر مع ملعقتين من <a href="{food:hummus-with-tahini}">الحمص بالطحينة</a> أو <a href="{food:cottage-cheese}">جبنة قريش</a> مبسترة.</li>
                <li><strong>وجبة العشاء:</strong> شوربة بروكلي وكوسا دافئة مع صدر دجاج مقطع، مريحة للمعدة وتمنع حموضة الليل.</li>
                <li><strong>سناك ما قبل النوم:</strong> شريحة تفاح رقيقة مدهونة بملعقة صغيرة من زبدة الفول السوداني الطبيعية 100%.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-lightbulb"></i> <span>6. حيل سريرية ذكية تضبط السكر دون حرمان</span></h2>
            <ol class="steps">
                <li><strong>ترتيب تناول اللقمة في الصحن:</strong> ابدئي بأكل الخضار والسلطة أولاً، ثم البروتين والدهون، واتركي النشويات لآخر الوجبة. هذا الترتيب البسيط يخفف قفزة السكر بعد الوجبة بشكل ملحوظ!</li>
                <li><strong>المشي السحري لمدة 10 دقائق بعد الطعام:</strong> عندما تمشين بخفة بعد وجبتكِ، تفتح عضلات الساقين أبوابها لامتصاص السكر مباشرة من الدم لحرقه كطاقة، دون أن تطلب أي إنسولين إضافي من البنكرياس.</li>
                <li><strong>الماء أفضل صديق لكِ:</strong> اجعلي الماء مشروبكِ الأساسي بدلاً من العصائر والمشروبات المحلاة؛ تحتاج الحامل إلى نحو 2.3 لتر من السوائل يومياً (من الماء والطعام معاً)، وهذا يحافظ على ترطيب جسمكِ دون أي سكر إضافي.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>7. أسئلة تهمكِ وإجاباتها من واقع العيادة</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>هل يعني تشخيصي بسكر الحمل أنني سأحتاج حتماً لإبر الإنسولين؟</h3><p>لا على الإطلاق! نحو 70 إلى 85% من الحوامل يتحكمن في أرقام السكر بنجاح وأمان عبر تنظيم الغذاء والمشي الخفيف فقط. والإنسولين لا يُستخدم إلا إذا كانت الأرقام عنيدة لحماية طفلكِ، وهو دواء آمن جداً ولا يعبر المشيمة إلى الجنين.</p></div>
                <div class="faq-item"><h3>هل سيستمر السكري معي بعد الولادة؟</h3><p>في أكثر من 90% من الحالات، يعود السكر إلى طبيعته تماماً بعد خروج المشيمة والولادة. سيطلب منكِ طبيبكِ فحصاً بسيطاً بعد 4 إلى 12 أسبوعاً من الولادة للتأكد التام، ثم فحصاً دورياً كل 1 إلى 3 سنوات، لأن سكر الحمل يرفع احتمال الإصابة بالسكري من النوع الثاني لاحقاً. والحفاظ على هذه العادات الغذائية الجميلة التي حميتِ بها نفسكِ وطفلكِ هو أفضل وقاية.</p></div>
            </div>'''),
en=dict(
 byline='By Dr. Wassim Habib',
 title='Gestational Diabetes Guide: Normal Blood Sugar Levels, Foods to Eat and Avoid, and Your Day Step by Step',
 h1='Gestational Diabetes Guide: Normal Blood Sugar Levels, Foods to Eat and Avoid, and Your Day Step by Step',
 crumb='Gestational diabetes',
 cat='Diabetes & Metabolic Health',
 desc='Everything you need to know about gestational diabetes: normal fasting and after-meal blood sugar levels, a foods to eat and avoid list to flatten your glucose curve and protect your baby, plus a balanced meal plan and the WiBo Health food guide.',
 summary='Normal levels in numbers, foods to eat and avoid, and a balanced daily meal plan to flatten your glucose curve.',
 hero_alt='Smiling pregnant woman in a sunny kitchen wearing a glucose sensor on her arm, with a bowl of berries and an avocado',
 about=['Gestational diabetes', 'Pregnancy', 'Blood glucose', 'Glycemic index'],
 disclaimer='⚖️ Clinical safety notice: this guide was prepared by WiBo Health for health education and lifestyle support. It is designed to complement the medical care plan from the obstetrician who follows your pregnancy, and it is not a diagnosis or a substitute for that care.',
 body='''            <h2 class="section-title"><i class="fas fa-heart"></i> <span>Take a breath: you and your baby are fine, and the answer starts on your plate</span></h2>
            <p class="lead">The first thing most mothers feel when they hear "your pregnancy blood sugar is high" is fear and guilt: <em>"Did I eat too many sweets? Have I hurt my baby?"</em></p>
            <p>Here is the medical truth we want you to hold on to right away: <strong>gestational diabetes is not your fault, and it does not mean your baby has diabetes.</strong> It is simply your body telling you that the powerful pregnancy hormones are putting a temporary load on how you handle sugar. With a few simple, smart food steps you will get through this stage safely and in great health, for you and for your baby.</p>

            <h2 class="section-title"><i class="fas fa-dna"></i> <span>1. What is really happening in your body? (The secret is in the placenta's hormones)</span></h2>
            <p>The placenta is not just a way to feed your baby; it is a powerful hormone factory. In the second half of pregnancy (especially around the fifth and sixth months), the placenta releases hormones with one goal: <em>"get as much energy and food as possible to the baby so it can grow"</em>.</p>
            <p>To do that, these hormones make your cells more resistant to insulin (they leave sugar in the bloodstream so it can pass to the baby). Normally your pancreas steps in and releases extra insulin to balance things out. But when the pancreas falls a little behind this high demand, blood sugar rises, and that is what we call <strong>gestational diabetes</strong>.</p>
            <div class="tip"><h3>👶 How does it affect the baby?</h3><p>If the mother's blood sugar stays high, the extra sugar passes to the baby. The baby's small pancreas then has to make extra insulin to store that sugar as fat, which can make the baby large at birth. That is why managing what you eat is the strongest shield for your baby's healthy, balanced growth.</p></div>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>2. Gestational diabetes chart: what are the normal levels?</span></h2>
            <p>When you check your sugar with a home meter, there are 3 golden numbers to remember:</p>
            <div class="rule-cards">
                <div class="rule-card"><div class="rule-num">&lt; 95 <small>mg/dL</small></div><h3>Fasting</h3><p>As soon as you wake up, before breakfast. In mmol/L (Europe): below 5.3 mmol/L.</p></div>
                <div class="rule-card"><div class="rule-num">&lt; 140 <small>mg/dL</small></div><h3>1 hour after a meal</h3><p>In mmol/L (Europe): below 7.8 mmol/L.</p></div>
                <div class="rule-card"><div class="rule-num">&lt; 120 <small>mg/dL</small></div><h3>2 hours after a meal</h3><p>In mmol/L (Europe): below 6.7 mmol/L.</p></div>
            </div>
            <h3>Why is fasting sugar sometimes high?</h3>
            <p>In the early morning hours your liver naturally releases glucose to give you energy to wake up (the dawn phenomenon). If your morning sugar runs high, the answer is not to starve yourself at night, but to have a smart bedtime snack (such as a spoon of pure peanut butter or a handful of <a href="{food:walnuts}">walnuts</a>) to steady the liver's signals, and to share your morning numbers with your doctor.</p>

            <h2 class="section-title"><i class="fas fa-traffic-light"></i> <span>3. Gestational diabetes food list: the smart traffic-light system</span></h2>
            <p>Instead of harsh restriction, the medical secret is to <strong>"flatten the glucose curve"</strong>: eat meals that are absorbed slowly and calmly and prevent sharp spikes.</p>

            <div class="tier-title tier-gold"><span class="tier-dot"></span> 🟢 Green light (eat freely and safely: the base of your plate)</div>
            <ul class="check-list">
                <li><strong>Lean proteins:</strong> <a href="{food:boiled-egg}">boiled eggs</a> or an <a href="{food:egg-omelette}">omelette</a>, <a href="{food:grilled-chicken-breast}">grilled chicken breast</a>, and safe, well-cooked fish (such as <a href="{food:grilled-salmon}">salmon</a>, rich in omega-3 fats for your baby's brain).</li>
                <li><strong>Healthy fats:</strong> <a href="{food:extra-virgin-olive-oil}">extra virgin olive oil</a>, <a href="{food:avocado}">avocado</a>, <a href="{food:walnuts}">walnuts</a> and raw almonds.</li>
                <li><strong>Leafy greens and fibre:</strong> <a href="{food:spinach}">spinach</a>, <a href="{food:zucchini}">courgette</a>, <a href="{food:cucumber}">cucumber</a>, <a href="{food:broccoli}">broccoli</a> and lettuce. (Fibre works like a sponge in your gut, soaking up sugar so it enters the bloodstream very slowly.)</li>
            </ul>

            <div class="tier-title tier-ok"><span class="tier-dot"></span> 🟡 Yellow light (helpful, but in smart portions)</div>
            <ul class="check-list">
                <li><strong>Complex carbohydrates:</strong> <a href="{food:quinoa}">quinoa</a>, whole <a href="{food:oatmeal}">rolled oats</a> (not instant), and naturally fermented whole-grain <a href="{food:sourdough-bread}">sourdough bread</a>.</li>
                <li><strong>Insulin-friendly fruit:</strong> <a href="{food:blueberry}">blueberries</a>, <a href="{food:strawberry}">strawberries</a>, <a href="{food:apple}">green apple</a>. (Golden tip: never eat fruit on its own; always add a few almonds or a spoon of <a href="{food:greek-yogurt}">Greek yogurt</a> to put the brakes on sugar absorption.)</li>
            </ul>

            <div class="tier-title tier-avoid"><span class="tier-dot"></span> 🔴 Red light (avoid to keep your numbers stable)</div>
            <ul class="check-list">
                <li><strong>Juices (even natural and freshly squeezed):</strong> juice is concentrated sugar stripped of its fibre and sends blood sugar up like an arrow within minutes. Swap it for whole fruit and a glass of water.</li>
                <li><strong>White bakery products and starches:</strong> white bread, pastries, pies and sweetened breakfast cereals.</li>
                <li><strong>Hidden sugars:</strong> maltodextrin, modified starch and corn syrup, ingredients often added to "sugar-free" products that still raise blood sugar sharply!</li>
            </ul>


            <h2 class="section-title"><i class="fas fa-cart-shopping"></i> <span>4. How to shop safely: use the complete food guide on our site</span></h2>
            <p>Supermarket shopping can be confusing; every product says <em>"healthy and diet-friendly"</em>. To help you make the right decision on the spot:</p>
            <ul class="check-list">
                <li><strong>Browse the <a href="{site:/foods.html}">food guide on our site</a>:</strong> on <strong>WiBo Health</strong> we built a large clinical guide with more than 850 foods, each with its glycemic index rating and nutritional values.</li>
                <li><strong>Add the site to your phone's home screen (quick web app):</strong> with one tap in your browser (Add to Home Screen) the site sits on your phone like any app, so you can open the guide in the supermarket and look up any product before it goes in your basket.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>5. Your balanced day: a realistic, filling meal plan</span></h2>
            <ul class="check-list">
                <li><strong>Breakfast:</strong> two eggs cooked in olive oil with avocado slices and leafy greens (rocket and cucumber), plus a quarter of a whole-grain loaf.</li>
                <li><strong>Morning snack:</strong> a small handful of walnuts with half a cup of fresh berries.</li>
                <li><strong>Lunch:</strong> a big colourful salad with olive oil and lemon (eat it first), a piece of grilled fish or chicken, and 3 tablespoons of cooked quinoa or <a href="{food:brown-rice}">brown rice</a>.</li>
                <li><strong>Afternoon snack:</strong> cucumber and carrot sticks with two tablespoons of <a href="{food:hummus-with-tahini}">hummus with tahini</a> or pasteurised <a href="{food:cottage-cheese}">cottage cheese</a>.</li>
                <li><strong>Dinner:</strong> a warm broccoli and courgette soup with sliced chicken breast, gentle on the stomach and helps prevent night-time heartburn.</li>
                <li><strong>Bedtime snack:</strong> a thin apple slice spread with a teaspoon of 100% natural peanut butter.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-lightbulb"></i> <span>6. Smart clinical tricks that steady your sugar without restriction</span></h2>
            <ol class="steps">
                <li><strong>Eat your plate in order:</strong> start with vegetables and salad, then protein and fat, and leave the starch for last. This simple order noticeably softens the sugar spike after a meal!</li>
                <li><strong>The magic 10-minute walk after eating:</strong> when you walk gently after a meal, your leg muscles open their doors to take sugar straight from the blood and burn it as energy, without asking the pancreas for extra insulin.</li>
                <li><strong>Water is your best friend:</strong> make water your main drink instead of juice and sweetened drinks. In pregnancy you need about 2.3 litres of fluid a day (from water and food together), which keeps you hydrated without any added sugar.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>7. Questions that matter to you, answered from clinical practice</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Does a gestational diabetes diagnosis mean I will definitely need insulin injections?</h3><p>Not at all! About 70 to 85% of pregnant women control their sugar successfully and safely with food changes and light walking alone. Insulin is only used when the numbers stay stubborn, to protect your baby; it is a very safe medicine and does not cross the placenta to the baby.</p></div>
                <div class="faq-item"><h3>Will the diabetes stay after the birth?</h3><p>In more than 90% of cases, blood sugar returns completely to normal once the placenta is delivered. Your doctor will ask for a simple test 4 to 12 weeks after the birth to be sure, and then a check every 1 to 3 years, because gestational diabetes raises the chance of type 2 diabetes later in life. Keeping the healthy eating habits that protected you and your baby is the best prevention.</p></div>
            </div>'''),
nl=dict(
 byline='Door Dr. Wassim Habib',
 title='Zwangerschapsdiabetes: normale bloedsuikerwaarden, wat mag je wel en niet eten, en je dag stap voor stap',
 h1='Zwangerschapsdiabetes: normale bloedsuikerwaarden, wat mag je wel en niet eten, en je dag stap voor stap',
 crumb='Zwangerschapsdiabetes',
 cat='Diabetes & metabole gezondheid',
 desc='Alles over zwangerschapsdiabetes: normale nuchtere waarden en waarden na het eten, een lijst met wat je wel en niet mag eten om je suikercurve af te vlakken en je baby te beschermen, plus een gebalanceerd dagmenu en de voedingswijzer van WiBo Health.',
 summary='Normale waarden in cijfers, wat je wel en niet mag eten, en een gebalanceerd dagmenu om je suikercurve af te vlakken.',
 hero_alt='Lachende zwangere vrouw in een zonnige keuken met een glucosesensor op haar arm, met een kom bessen en een avocado',
 about=['Gestational diabetes', 'Pregnancy', 'Blood glucose', 'Glycemic index'],
 disclaimer='⚖️ Klinische veiligheidsmelding: deze gids is door WiBo Health gemaakt voor gezondheidsvoorlichting en leefstijlondersteuning. Hij is bedoeld als aanvulling op het zorgplan van de gynaecoloog of verloskundige die je zwangerschap begeleidt, en is geen diagnose en geen vervanging van die zorg.',
 body='''            <h2 class="section-title"><i class="fas fa-heart"></i> <span>Rustig maar: met jou en je baby gaat het goed, en de oplossing begint op je bord</span></h2>
            <p class="lead">Het eerste wat de meeste moeders voelen als ze horen "je bloedsuiker is te hoog" is angst en schuldgevoel: <em>"Heb ik te veel zoetigheid gegeten? Heb ik mijn baby iets aangedaan?"</em></p>
            <p>De medische waarheid waar we je meteen gerust mee willen stellen: <strong>zwangerschapsdiabetes is niet jouw schuld, en het betekent niet dat je baby diabetes heeft.</strong> Het is gewoon een signaal van je lichaam dat de sterke zwangerschapshormonen tijdelijk extra druk zetten op de verwerking van suikers. Met een paar eenvoudige, slimme voedingsstappen kom je deze periode veilig en gezond door, voor jou en voor je baby.</p>

            <h2 class="section-title"><i class="fas fa-dna"></i> <span>1. Wat gebeurt er echt in je lichaam? (Het geheim zit in de hormonen van de placenta)</span></h2>
            <p>De placenta voedt niet alleen je baby; het is ook een krachtige hormoonfabriek. In de tweede helft van de zwangerschap (vooral rond de vijfde en zesde maand) maakt de placenta hormonen met één doel: <em>"zoveel mogelijk energie en voeding naar de baby sturen zodat hij kan groeien"</em>.</p>
            <p>Daarvoor maken deze hormonen je cellen minder gevoelig voor insuline (ze laten suiker in het bloed zodat die naar de baby kan). Normaal springt je alvleesklier bij en maakt extra insuline om dat te compenseren. Maar als de alvleesklier die grote vraag net niet bijhoudt, stijgt je bloedsuiker. Dat noemen we <strong>zwangerschapsdiabetes</strong>.</p>
            <div class="tip"><h3>👶 Wat betekent dit voor de baby?</h3><p>Blijft de bloedsuiker van de moeder hoog, dan gaat die extra suiker naar de baby. De kleine alvleesklier van de baby moet dan extra insuline maken om die suiker als vet op te slaan, waardoor de baby bij de geboorte groot kan zijn. Daarom is grip op wat je eet het sterkste schild voor een gezonde, evenwichtige groei van je baby.</p></div>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>2. Zwangerschapsdiabetes waarden: wat zijn normale bloedsuikerwaarden?</span></h2>
            <p>Als je je suiker meet met een thuismeter, zijn er 3 gouden getallen om te onthouden:</p>
            <div class="rule-cards">
                <div class="rule-card"><div class="rule-num">&lt; 5,3 <small>mmol/L</small></div><h3>Nuchter</h3><p>Direct na het opstaan, voor het ontbijt. In mg/dL: onder 95 mg/dL.</p></div>
                <div class="rule-card"><div class="rule-num">&lt; 7,8 <small>mmol/L</small></div><h3>1 uur na de maaltijd</h3><p>In mg/dL: onder 140 mg/dL.</p></div>
                <div class="rule-card"><div class="rule-num">&lt; 6,7 <small>mmol/L</small></div><h3>2 uur na de maaltijd</h3><p>In mg/dL: onder 120 mg/dL.</p></div>
            </div>
            <h3>Waarom is je nuchtere suiker soms hoog?</h3>
            <p>In de vroege ochtend geeft je lever van nature glucose af om je energie te geven om wakker te worden (het dawn-fenomeen). Is je ochtendsuiker vaak hoog, dan is de oplossing niet om 's avonds te gaan vasten, maar een slim tussendoortje voor het slapengaan (zoals een lepel pure pindakaas of een handje <a href="{food:walnuts}">walnoten</a>) om de signalen van je lever te stabiliseren. Bespreek je ochtendwaarden ook met je arts.</p>

            <h2 class="section-title"><i class="fas fa-traffic-light"></i> <span>3. Zwangerschapsdiabetes voedingslijst: het slimme stoplichtsysteem</span></h2>
            <p>In plaats van streng te lijnen is het medische geheim <strong>"je suikercurve afvlakken"</strong>: maaltijden eten die langzaam en rustig worden opgenomen en scherpe pieken voorkomen.</p>

            <div class="tier-title tier-gold"><span class="tier-dot"></span> 🟢 Groen licht (eet gerust: de basis van je bord)</div>
            <ul class="check-list">
                <li><strong>Magere eiwitten:</strong> <a href="{food:boiled-egg}">gekookte eieren</a> of een <a href="{food:egg-omelette}">omelet</a>, <a href="{food:grilled-chicken-breast}">gegrilde kipfilet</a>, en veilige, goed gegaarde vis (zoals <a href="{food:grilled-salmon}">zalm</a>, rijk aan omega-3-vetten voor de hersenen van je baby).</li>
                <li><strong>Gezonde vetten:</strong> <a href="{food:extra-virgin-olive-oil}">extra vierge olijfolie</a>, <a href="{food:avocado}">avocado</a>, <a href="{food:walnuts}">walnoten</a> en ongebrande amandelen.</li>
                <li><strong>Bladgroenten en vezels:</strong> <a href="{food:spinach}">spinazie</a>, <a href="{food:zucchini}">courgette</a>, <a href="{food:cucumber}">komkommer</a>, <a href="{food:broccoli}">broccoli</a> en sla. (Vezels werken als een spons in je darmen: ze nemen suiker op zodat die heel langzaam in je bloed komt.)</li>
            </ul>

            <div class="tier-title tier-ok"><span class="tier-dot"></span> 🟡 Oranje licht (goed, maar met slimme porties)</div>
            <ul class="check-list">
                <li><strong>Complexe koolhydraten:</strong> <a href="{food:quinoa}">quinoa</a>, volkoren <a href="{food:oatmeal}">havermout</a> (geen instant), en natuurlijk gerezen volkoren <a href="{food:sourdough-bread}">zuurdesembrood</a>.</li>
                <li><strong>Insulinevriendelijk fruit:</strong> <a href="{food:blueberry}">blauwe bessen</a>, <a href="{food:strawberry}">aardbeien</a>, <a href="{food:apple}">groene appel</a>. (Gouden tip: eet fruit nooit los; neem er altijd een paar amandelen of een lepel <a href="{food:greek-yogurt}">Griekse yoghurt</a> bij om de suikeropname af te remmen.)</li>
            </ul>

            <div class="tier-title tier-avoid"><span class="tier-dot"></span> 🔴 Rood licht (vermijd dit om je waarden stabiel te houden)</div>
            <ul class="check-list">
                <li><strong>Sappen (ook natuurlijke en versgeperste):</strong> sap is geconcentreerde suiker zonder vezels en laat je bloedsuiker binnen enkele minuten pijlsnel stijgen. Kies liever heel fruit en een glas water.</li>
                <li><strong>Wit brood en witte zetmeelproducten:</strong> wit brood, gebak, taart en gezoete ontbijtgranen.</li>
                <li><strong>Verborgen suikers:</strong> maltodextrine, gemodificeerd zetmeel en glucosestroop, ingrediënten die vaak in "suikervrije" producten zitten maar je bloedsuiker flink laten stijgen!</li>
            </ul>


            <h2 class="section-title"><i class="fas fa-cart-shopping"></i> <span>4. Veilig boodschappen doen: gebruik de complete voedingswijzer op onze site</span></h2>
            <p>Boodschappen doen in de supermarkt kan verwarrend zijn; op elk product staat <em>"gezond en geschikt voor je dieet"</em>. Zo maak je ter plekke de juiste keuze:</p>
            <ul class="check-list">
                <li><strong>Blader door de <a href="{site:/foods.html}">voedingswijzer op onze site</a>:</strong> op <strong>WiBo Health</strong> hebben we een uitgebreide klinische gids gemaakt met meer dan 850 voedingsmiddelen, elk met de glykemische index en voedingswaarden.</li>
                <li><strong>Zet de site op het beginscherm van je telefoon (snelle web-app):</strong> met één tik in je browser (Toevoegen aan beginscherm) staat de site als een app op je telefoon, zodat je de gids in de supermarkt opent en elk product opzoekt voordat het in je mandje gaat.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>5. Je gebalanceerde dag: een realistisch, verzadigend dagmenu</span></h2>
            <ul class="check-list">
                <li><strong>Ontbijt:</strong> twee eieren gebakken in olijfolie met plakjes avocado en bladgroenten (rucola en komkommer), plus een kwart volkorenbrood.</li>
                <li><strong>Tussendoortje 's ochtends:</strong> een klein handje walnoten met een half kopje verse bessen.</li>
                <li><strong>Lunch:</strong> een grote, kleurrijke salade met olijfolie en citroen (eet die eerst), een stuk gegrilde vis of kip, en 3 eetlepels gekookte quinoa of <a href="{food:brown-rice}">zilvervliesrijst</a>.</li>
                <li><strong>Tussendoortje 's middags:</strong> komkommer- en wortelreepjes met twee eetlepels <a href="{food:hummus-with-tahini}">hummus met tahin</a> of gepasteuriseerde <a href="{food:cottage-cheese}">hüttenkäse</a>.</li>
                <li><strong>Avondeten:</strong> warme broccoli-courgettesoep met reepjes kipfilet, licht voor de maag en helpt maagzuur 's nachts te voorkomen.</li>
                <li><strong>Voor het slapengaan:</strong> een dun plakje appel met een theelepel 100% natuurlijke pindakaas.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-lightbulb"></i> <span>6. Slimme klinische trucs die je suiker stabiliseren zonder streng te lijnen</span></h2>
            <ol class="steps">
                <li><strong>Eet je bord in de juiste volgorde:</strong> begin met groenten en salade, dan eiwit en vet, en bewaar het zetmeel voor het laatst. Deze simpele volgorde dempt de suikerpiek na de maaltijd merkbaar!</li>
                <li><strong>De magische wandeling van 10 minuten na het eten:</strong> als je na de maaltijd rustig wandelt, nemen je beenspieren suiker direct uit het bloed op en verbranden die als energie, zonder extra insuline van je alvleesklier te vragen.</li>
                <li><strong>Water is je beste vriend:</strong> maak water je belangrijkste drank in plaats van sap en gezoete dranken. Tijdens de zwangerschap heb je ongeveer 2,3 liter vocht per dag nodig (uit water en voeding samen), zo blijf je gehydrateerd zonder extra suiker.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>7. Vragen die jou bezighouden, beantwoord vanuit de praktijk</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Betekent de diagnose zwangerschapsdiabetes dat ik zeker insuline moet spuiten?</h3><p>Helemaal niet! Ongeveer 70 tot 85% van de zwangere vrouwen houdt de suikerwaarden goed en veilig onder controle met alleen aanpassingen in voeding en rustig wandelen. Insuline wordt alleen gebruikt als de waarden hardnekkig hoog blijven, om je baby te beschermen; het is een zeer veilig medicijn dat niet via de placenta naar de baby gaat.</p></div>
                <div class="faq-item"><h3>Blijft de diabetes na de bevalling?</h3><p>In meer dan 90% van de gevallen wordt de bloedsuiker weer helemaal normaal zodra de placenta geboren is. Je arts vraagt 4 tot 12 weken na de bevalling om een eenvoudige test om zeker te zijn, en daarna om een controle elke 1 tot 3 jaar, omdat zwangerschapsdiabetes de kans op diabetes type 2 later vergroot. De gezonde eetgewoonten waarmee je jezelf en je baby beschermde, vasthouden is de beste preventie.</p></div>
            </div>'''),
# Swedish: glucose only in mmol/l; WHO 2013 diagnostic limits as recommended by Socialstyrelsen (2015); targets are set by the
# maternity team. Food pages are English for now, said once in the text.
sv=dict(
 byline='Av Dr. Wassim Habib',
 title='Graviditetsdiabetes: normala blodsockervärden, vad du kan äta och din dag steg för steg',
 h1='Graviditetsdiabetes: normala blodsockervärden, vad du kan äta och din dag steg för steg',
 crumb='Graviditetsdiabetes',
 cat='Diabetes och metabol hälsa',
 desc='Allt du behöver veta om graviditetsdiabetes: gränsvärden och målvärden i mmol/l, en trafikljuslista över mat som jämnar ut blodsockerkurvan och skyddar ditt barn, ett balanserat dagsschema och WiBo Healths livsmedelsguide.',
 summary='Värdena i mmol/l, vad du kan äta och undvika, och ett balanserat dagsschema som jämnar ut blodsockerkurvan.',
 hero_alt='Leende gravid kvinna i ett soligt kök med en glukossensor på armen, en skål bär och en avokado',
 about=['Gestational diabetes', 'Pregnancy', 'Blood glucose', 'Glycemic index'],
 references=[
     'World Health Organization. Diagnostic criteria and classification of hyperglycaemia first detected in pregnancy. Geneva: WHO; 2013',
     'Socialstyrelsen. Gränsvärden för graviditetsdiabetes – stöd för beslut om behandling. Stockholm: Socialstyrelsen; 2015',
     'American Diabetes Association (ADA). Standards of Care in Diabetes—2026, Section 15: Management of Diabetes in Pregnancy. Diabetes Care 2026;49(Suppl 1)',
     'American College of Obstetricians and Gynecologists (ACOG). Practice Bulletin No. 190: Gestational Diabetes Mellitus. Obstet Gynecol 2018;131(2):e49–e64',
     'National Institute for Health and Care Excellence (NICE). Diabetes in pregnancy: management from preconception to the postnatal period (NG3), 2015, updated 2020',
     'International Federation of Gynecology and Obstetrics (FIGO). The FIGO Initiative on gestational diabetes mellitus: a pragmatic guide for diagnosis, management, and care. Int J Gynaecol Obstet 2015;131(Suppl 3):S173–S211',
 ],
 disclaimer='⚖️ Medicinsk ansvarsfriskrivning: den här guiden har tagits fram av WiBo Health som allmän hälsoinformation och stöd för levnadsvanor. Den kompletterar den vård du får av din barnmorska, mödravårdscentral (MVC) och specialistmödravård, och ersätter inte råd, diagnos eller behandling från legitimerad hälso- och sjukvårdspersonal. Kontakta din barnmorska, din vårdcentral eller ring 1177 för sjukvårdsrådgivning. Vid akut fara – ring 112.',
 body='''            <h2 class="section-title"><i class="fas fa-heart"></i> <span>Andas lugnt: du och ditt barn mår bra, och svaret börjar på tallriken</span></h2>
            <p class="lead">Det första de flesta blivande mammor känner när de hör ”ditt blodsocker är för högt” är oro och skuld: <em>”Har jag ätit för mycket sött? Har jag skadat mitt barn?”</em></p>
            <p>Här är den medicinska sanningen vi vill att du håller fast vid redan nu: <strong>graviditetsdiabetes är inte ditt fel, och det betyder inte att ditt barn har diabetes.</strong> Det är kroppens sätt att berätta att de kraftfulla graviditetshormonerna tillfälligt belastar hur du hanterar socker. Med några enkla och smarta steg kring maten tar du dig tryggt igenom den här perioden, både du och ditt barn.</p>

            <h2 class="section-title"><i class="fas fa-dna"></i> <span>1. Vad händer egentligen i kroppen? (Hemligheten finns i moderkakans hormoner)</span></h2>
            <p>Moderkakan är inte bara barnets matledning, den är också en kraftfull hormonfabrik. Under graviditetens andra halva (särskilt runt femte och sjätte månaden) frisätter den hormoner med ett enda mål: <em>”få fram så mycket energi och näring som möjligt till barnet så att det kan växa”</em>.</p>
            <p>För att lyckas gör hormonerna dina celler mer motståndskraftiga mot insulin (sockret får stanna kvar i blodet så att det kan gå över till barnet). Normalt svarar bukspottkörteln med att frisätta extra insulin. Men när bukspottkörteln inte riktigt hinner med det höga behovet stiger blodsockret, och det är det vi kallar <strong>graviditetsdiabetes</strong>.</p>
            <div class="tip"><h3>👶 Hur påverkas barnet?</h3><p>Om mammans blodsocker är högt under längre tid går det extra sockret över till barnet. Barnets lilla bukspottkörtel får då tillverka extra insulin för att lagra sockret som fett, vilket kan göra barnet stort vid födseln. Därför är maten ditt starkaste skydd för barnets friska och jämna tillväxt.</p></div>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>2. Vilka värden gäller? Gränsvärden och målvärden i mmol/l</span></h2>
            <h3>Så ställs diagnosen i Sverige</h3>
            <p>Diagnosen ställs med en sockerbelastning (OGTT med 75 g glukos). Socialstyrelsen rekommenderar sedan 2015 WHO:s gränsvärden, mätt i venöst plasma: graviditetsdiabetes föreligger om <strong>fasteglukos är 5,1 mmol/l eller högre</strong>, <strong>värdet efter 1 timme är 10,0 mmol/l eller högre</strong> eller <strong>värdet efter 2 timmar är 8,5 mmol/l eller högre</strong>. Det räcker att ett av värdena ligger över gränsen. Hur och när provet tas kan skilja sig något mellan regioner, så din barnmorska berättar hur det går till där du bor.</p>
            <h3>Målvärden när du mäter själv hemma</h3>
            <p>När du mäter med blodsockermätare hemma finns det tre gyllene värden att komma ihåg. Det här är de internationella målvärdena (ADA, ACOG och NICE); <strong>din diabetesbarnmorska eller läkare på specialistmödravården sätter dina egna målvärden</strong>, och de kan skilja sig något mellan regioner:</p>
            <div class="rule-cards">
                <div class="rule-card"><div class="rule-num">&lt; 5,3 <small>mmol/l</small></div><h3>Fastande</h3><p>Direkt när du vaknar, före frukost.</p></div>
                <div class="rule-card"><div class="rule-num">&lt; 7,8 <small>mmol/l</small></div><h3>1 timme efter måltid</h3><p>Räknat från att du började äta.</p></div>
                <div class="rule-card"><div class="rule-num">&lt; 6,7 <small>mmol/l</small></div><h3>2 timmar efter måltid</h3><p>Om din barnmorska ber dig mäta efter 2 timmar i stället.</p></div>
            </div>
            <h3>Varför är fastevärdet ibland högt?</h3>
            <p>Under de tidiga morgontimmarna frisätter levern naturligt glukos för att ge dig energi att vakna (gryningsfenomenet). Om ditt morgonvärde är högt är lösningen inte att svälta dig på kvällen, utan att äta ett smart kvällsmål (till exempel en sked naturligt jordnötssmör eller en näve <a href="{food:walnuts}">valnötter</a>) som lugnar leverns signaler, och att visa dina morgonvärden för din barnmorska.</p>

            <h2 class="section-title"><i class="fas fa-traffic-light"></i> <span>3. Mat vid graviditetsdiabetes: det smarta trafikljussystemet</span></h2>
            <p>I stället för hårda förbud är den medicinska hemligheten att <strong>”platta till blodsockerkurvan”</strong>: att äta måltider som tas upp långsamt och lugnt och som förhindrar kraftiga toppar. (Länkarna till livsmedlen leder till vår livsmedelsguide, som än så länge finns på engelska.)</p>

            <div class="tier-title tier-gold"><span class="tier-dot"></span> 🟢 Grönt ljus (ät fritt och tryggt: basen på din tallrik)</div>
            <ul class="check-list">
                <li><strong>Magert protein:</strong> <a href="{food:boiled-egg}">kokta ägg</a> eller <a href="{food:egg-omelette}">omelett</a>, <a href="{food:grilled-chicken-breast}">grillad kycklingfilé</a> och genomstekt fisk som är säker under graviditeten (till exempel <a href="{food:grilled-salmon}">lax</a>, rik på omega-3-fetter för barnets hjärna).</li>
                <li><strong>Nyttiga fetter:</strong> <a href="{food:extra-virgin-olive-oil}">extra jungfruolivolja</a>, <a href="{food:avocado}">avokado</a>, <a href="{food:walnuts}">valnötter</a> och naturella mandlar.</li>
                <li><strong>Gröna bladgrönsaker och fiber:</strong> <a href="{food:spinach}">spenat</a>, <a href="{food:zucchini}">zucchini</a>, <a href="{food:cucumber}">gurka</a>, <a href="{food:broccoli}">broccoli</a> och sallad. (Fibrer fungerar som en svamp i tarmen som suger upp sockret, så att det når blodet mycket långsamt.)</li>
            </ul>

            <div class="tier-title tier-ok"><span class="tier-dot"></span> 🟡 Gult ljus (bra, men i smarta portioner)</div>
            <ul class="check-list">
                <li><strong>Långsamma kolhydrater:</strong> <a href="{food:quinoa}">quinoa</a>, hela <a href="{food:oatmeal}">havregryn</a> (inte snabbgröt) och naturligt jäst <a href="{food:sourdough-bread}">surdegsbröd</a> av fullkorn.</li>
                <li><strong>Insulinvänlig frukt:</strong> <a href="{food:blueberry}">blåbär</a>, <a href="{food:strawberry}">jordgubbar</a> och <a href="{food:apple}">grönt äpple</a>. (Gyllene tips: ät aldrig frukten ensam, lägg alltid till några mandlar eller en sked <a href="{food:greek-yogurt}">grekisk yoghurt</a> som bromsar sockerupptaget.)</li>
            </ul>

            <div class="tier-title tier-avoid"><span class="tier-dot"></span> 🔴 Rött ljus (undvik för att hålla värdena stabila)</div>
            <ul class="check-list">
                <li><strong>Juice (även naturell och nypressad):</strong> juice är koncentrerat socker utan fibrer och skickar upp blodsockret som en pil på några minuter. Byt till hel frukt och ett glas vatten.</li>
                <li><strong>Vitt bröd och bakverk:</strong> vitt bröd, wienerbröd, kanelbullar, pajer och sötade frukostflingor.</li>
                <li><strong>Dolt socker:</strong> maltodextrin, modifierad stärkelse och glukossirap, ingredienser som ofta finns i ”sockerfria” produkter men ändå höjer blodsockret kraftigt!</li>
            </ul>


            <h2 class="section-title"><i class="fas fa-cart-shopping"></i> <span>4. Handla tryggt: använd livsmedelsguiden på vår webbplats</span></h2>
            <p>Det kan vara förvirrande att handla, när varje produkt kallar sig <em>”nyttig och bra för dig”</em>. För att hjälpa dig att välja rätt direkt i butiken:</p>
            <ul class="check-list">
                <li><strong>Bläddra i <a href="{site:/foods.html}">livsmedelsguiden på vår webbplats</a> (än så länge på engelska):</strong> på <strong>WiBo Health</strong> har vi byggt en stor guide med mer än 850 livsmedel, vart och ett med sitt glykemiska index och sina näringsvärden.</li>
                <li><strong>Lägg webbplatsen på telefonens hemskärm (snabb webbapp):</strong> med ett tryck i webbläsaren (Lägg till på hemskärmen) ligger webbplatsen på telefonen som vilken app som helst, så att du kan slå upp en vara i butiken innan den hamnar i korgen.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>5. Din balanserade dag: ett realistiskt och mättande dagsschema</span></h2>
            <ul class="check-list">
                <li><strong>Frukost:</strong> två ägg stekta i olivolja med avokadoskivor och gröna blad (ruccola och gurka), plus en skiva fullkornsbröd eller ett fullkornsknäckebröd.</li>
                <li><strong>Förmiddagsmellanmål:</strong> en liten näve valnötter och en halv deciliter färska bär.</li>
                <li><strong>Lunch:</strong> en stor färgglad sallad med olivolja och citron (ät den först), en bit grillad fisk eller kyckling och 3 matskedar kokt quinoa eller <a href="{food:brown-rice}">fullkornsris</a>.</li>
                <li><strong>Eftermiddagsmellanmål:</strong> gurk- och morotsstavar med två matskedar <a href="{food:hummus-with-tahini}">hummus med tahini</a> eller pastöriserad <a href="{food:cottage-cheese}">keso</a>.</li>
                <li><strong>Middag:</strong> en varm soppa på broccoli och zucchini med skivad kycklingfilé, skonsam för magen och bra mot halsbränna på kvällen.</li>
                <li><strong>Kvällsmål:</strong> en tunn äppelskiva med en tesked 100 % naturligt jordnötssmör.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-lightbulb"></i> <span>6. Smarta knep som stabiliserar blodsockret utan förbud</span></h2>
            <ol class="steps">
                <li><strong>Ät tallriken i rätt ordning:</strong> börja med grönsaker och sallad, fortsätt med protein och fett och spara stärkelsen till sist. Den enkla ordningen dämpar blodsockertoppen efter maten märkbart!</li>
                <li><strong>Den magiska promenaden på 10 minuter efter maten:</strong> när du promenerar lugnt efter en måltid öppnar benmusklerna sina dörrar och tar socker direkt från blodet som energi, utan att be bukspottkörteln om extra insulin.</li>
                <li><strong>Vatten är din bästa vän:</strong> gör vatten till din huvuddryck i stället för juice och söta drycker. Under graviditeten behöver du ungefär 2,3 liter vätska per dag (från dryck och mat tillsammans), så håller du vätskebalansen utan tillsatt socker.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>7. Frågor som är viktiga för dig, besvarade utifrån klinisk erfarenhet</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Betyder graviditetsdiabetes att jag säkert behöver ta insulin?</h3><p>Inte alls! Ungefär 70–85 % av de gravida klarar att hålla blodsockret på en bra och säker nivå med enbart ändrade matvanor och lugna promenader. Insulin används bara om värdena förblir höga, för att skydda ditt barn; det är ett mycket säkert läkemedel som inte passerar moderkakan till barnet.</p></div>
                <div class="faq-item"><h3>Finns diabetesen kvar efter förlossningen?</h3><p>I mer än 90 % av fallen blir blodsockret helt normalt igen när moderkakan har fötts. Efter förlossningen följs du upp med ett enkelt prov för att vara säker, och sedan rekommenderas regelbundna kontroller på vårdcentralen, eftersom graviditetsdiabetes ökar risken för typ 2-diabetes senare i livet. Din barnmorska berättar hur uppföljningen går till i din region. Att behålla de goda matvanorna som skyddade dig och ditt barn är det bästa du kan göra för din hälsa framåt.</p></div>
            </div>'''),
    ),
)

PREDIABETES = dict(
    section='diabetes',
    slugs=dict(ar='prediabetes', en='prediabetes', nl='prediabetes', sv='prediabetes'),
    # full portrait cover (user decision 2026-10-22: show the whole scene with the breakfast bowl, never a face-only crop)
    hero='prediabetes-healthy-breakfast-lifestyle.webp', hero_size=(896, 1200), hero_portrait=True,
    # 16:9 cards: the whole portrait over a blurred copy of itself (hub card; the 1280px one also feeds the homepage)
    thumb='prediabetes-guide-thumb.webp', thumb_size=(640, 360), thumb_2x=('prediabetes-guide-card.webp', 1280),
    published='2026-10-22', modified='2026-10-22',
    references=[
        'American Diabetes Association Professional Practice Committee. 2. Diagnosis and Classification of Diabetes: Standards of Care in Diabetes—2026. Diabetes Care 2026;49(Suppl 1)',
        'Diabetes Prevention Program Research Group. Reduction in the incidence of type 2 diabetes with lifestyle intervention or metformin. N Engl J Med 2002;346(6):393–403',
        'Diabetes Prevention Program Research Group. Long-term effects of lifestyle intervention or metformin on diabetes development and microvascular complications over 15-year follow-up: the Diabetes Prevention Program Outcomes Study. Lancet Diabetes Endocrinol 2015;3(11):866–875',
        'Shukla AP, Iliescu RG, Thomas CE, Aronne LJ. Food order has a significant impact on postprandial glucose and insulin levels. Diabetes Care 2015;38(7):e98–e99',
        'World Health Organization. Definition and diagnosis of diabetes mellitus and intermediate hyperglycaemia: report of a WHO/IDF consultation. Geneva: WHO; 2006',
    ],
    faq_schema=True,
    named_author=True,                                   # user decision 2026-10-22: second named exception (reviewed by Dr. Wassim Habib)
    content=dict(
ar=dict(
 byline='مراجعة طبية: الدكتور وسيم حبيب',
 title='مرحلة ما قبل السكري: كيف توقف القطار وتنزّل التراكمي قبل ما يتحول لسكري؟',
 h1='مرحلة ما قبل السكري: كيف توقف القطار وتنزّل التراكمي قبل ما يتحول لسكري؟',
 crumb='ما قبل السكري',
 cat='السكري ومتلازمة الأيض',
 desc='سكرك التراكمي بين 5.7% و6.4%؟ افهم مرحلة ما قبل السكري بالأرقام، وأعراضها الخفية، وخطة عملية لـ 12 أسبوعاً بالغذاء والحركة والنوم لخفض التراكمي، مبنية على دراسة DPP ومعايير ADA.',
 summary='معنى أرقام التراكمي والصائم، لماذا تحدث مقاومة الإنسولين، وخطة 12 أسبوعاً بالغذاء والحركة والنوم لإعادة السكر إلى المنطقة الآمنة.',
 hero_alt='فطور صحي متوازن لضبط السكر التراكمي ومقاومة الإنسولين - WiBo Health',
 about=['Prediabetes', 'HbA1c', 'Insulin resistance', 'Type 2 diabetes prevention'],
 disclaimer='⚠️ إخلاء مسؤولية طبي: المحتوى والمعلومات الواردة في هذا المقال مقدمة لأغراض التثقيف الصحي العام ورفع الوعي الغذائي، ولا تُعتبر بأي حال من الأحوال تشخيصاً طبياً، أو خطة علاجية مخصصة، أو بديلاً عن استشارة الطبيب المختص أو مقدم الرعاية الصحية المتابع لحالتك. استشر طبيبك دائماً قبل إجراء تغييرات جذرية في نظامك الغذائي أو أدويتك.',
 body='''            <p class="lead">تخيّل أنك خرجت للتو من باب المختبر أو عيادة الطبيب، ورقة التحليل بيدك، وعيناك مثبتتان على رقم واحد محاط بدائرة حمراء: السكر التراكمي 5.9% أو 6.1%، أو ربما سكر الصائم 112 ملغ/ديسيلتر.</p>
            <p>ربما قال لك الطبيب جملة مقتضبة وهو يودعك: <em>"سكرك على الحافة.. انتبه على حالك وخفف أكل"</em>.</p>
            <p>خرجت إلى الشارع، والأفكار تتزاحم في رأسك كأمواج متلاطمة: هل أصبحت مريض سكري خلاص؟ هل انتهت الأيام التي آكل فيها مع عائلتي براحة؟ هل سأعيش بقية عمري على الأدوية ووخز الإبر؟ من أين أبدأ غداً صباحاً؟</p>
            <p>قبل أن تترك القلق يلتهم يومك، خذ نفساً عميقاً واقرأ هذه الكلمات بقلبك: <strong>أنت لست مريض سكري، هذا الرقم ليس حكماً نهائياً ولا نهايةً لا رجعة فيها، والأهم من ذلك كله: هذا ليس خطأك.</strong></p>
            <p>أنت لست في نهاية الطريق، بل أنت تقف في "محطة الإنذار المبكر". ورقة تحليلك هذه لم تكن خبراً سيئاً، بل كانت في الحقيقة أعظم هدية تنبيهية منحك إياها جسمك. هذا المقال ليس كتاباً طبياً معقداً، بل هو خطتك العملية، خطوة بخطوة، لترجع بالسكر التراكمي إلى بر الأمان وتوقف القطار قبل أن يواصل مسيره.</p>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>1. شو يعني "سكرك على الحافة"؟ فك شيفرة ورقة تحليلك ببساطة</span></h2>
            <p>أول خطوة للتخلص من الخوف هي الفهم؛ فالإنسان عدو ما يجهل. عندما تنظر إلى أرقام تحاليل الدم، ستجد مصطلحين رئيسيين يبحث عنهما آلاف الأشخاص يومياً بلهفة:</p>
            <ul class="check-list">
                <li><strong>السكر التراكمي (<bdi>HbA1c</bdi>):</strong> لا يخبرنا بمقدار السكر في دمك اليوم أو بعد وجبة البارحة، بل هو بمثابة "شريط ذكريات" لكريات الدم الحمراء يوثق متوسط السكر الذي سبح في دمك طوال الـ 90 يوماً الماضية.</li>
                <li><strong>سكر الدم الصائم (<bdi>Fasting Glucose</bdi>):</strong> فحص يقيس تركيز السكر في دمك بعد صيام ليلة كاملة (8 إلى 10 ساعات).</li>
            </ul>
            <figure class="article-figure figure-narrow">
                <img src="/images/hba1c-prediabetes-blood-sugar-chart.webp" alt="مخطط أرقام السكر التراكمي ومرحلة ما قبل السكري بالألوان - WiBo Health" width="1024" height="935" loading="lazy" decoding="async">
                <figcaption>المناطق الثلاث للسكر التراكمي وسكر الصائم وفق معايير الجمعية الأمريكية للسكري (ADA).</figcaption>
            </figure>
            <p>لتوضيح الأرقام بدون أي تعقيد، قسّم الأطباء هذه الأرقام إلى ثلاث مناطق واضحة تماماً:</p>

            <div class="tier-title tier-gold"><span class="tier-dot"></span> 🟢 أولاً: منطقة الأمان الخضراء (الوضع الطبيعي)</div>
            <ul class="check-list">
                <li><strong>السكر التراكمي:</strong> أقل من 5.7%.</li>
                <li><strong>سكر الصائم:</strong> أقل من 100 ملغ/ديسيلتر (أقل من 5.6 مليمول/لتر).</li>
                <li><strong>معناها:</strong> خلاياك حساسة للإنسولين، وبنكرياسك يعمل براحة وهدوء.</li>
            </ul>

            <div class="tier-title tier-ok"><span class="tier-dot"></span> 🟡 ثانياً: منطقة التنبيه والفرصة الذهبية (مرحلة ما قبل السكري)</div>
            <ul class="check-list">
                <li><strong>السكر التراكمي:</strong> يقع بين 5.7% و6.4%.</li>
                <li><strong>سكر الصائم:</strong> يقع بين 100 و125 ملغ/ديسيلتر (بين 5.6 و6.9 مليمول/لتر).</li>
                <li><strong>معناها:</strong> أنت في مرحلة "مقدمات السكري". السكر في دمك أعلى من الطبيعي، لكنه لم يصل بعد إلى عتبة مرض السكري. هنا تكمن نافذة النجاة؛ فالجسم ما زال قادراً على استعادة توازنه إذا رفعت عنه الحمل الزائد.</li>
            </ul>

            <div class="tier-title tier-avoid"><span class="tier-dot"></span> 🔴 ثالثاً: منطقة الإجراء والمتابعة الطبية (السكري من النوع الثاني)</div>
            <ul class="check-list">
                <li><strong>السكر التراكمي:</strong> 6.5% أو أكثر.</li>
                <li><strong>سكر الصائم:</strong> 126 ملغ/ديسيلتر أو أكثر (في فحصين منفصلين).</li>
                <li><strong>معناها:</strong> تجاوز الجسم مرحلة التنبيه وأصبح يحتاج لتدخل دوائي ومتابعة منتظمة لمنع المضاعفات.</li>
            </ul>
            <div class="tip"><h3>💡 قاعدة ذهبية احفظها جيداً</h3><p>إذا كان تراكمي السكر لديك اليوم 5.8، 6.0، أو حتى 6.3.. فهذا يعني أنك في المنطقة الصفراء. القطار لم يصل بعد إلى المحطة الأخيرة؛ القطار يبطئ سرعته الآن، وأنت تملك المفتاح لتوجيهه إلى مسار الأمان.</p></div>

            <h2 class="section-title"><i class="fas fa-key"></i> <span>2. ليش تحرك القطار بهاد الاتجاه أصلاً؟ حكاية الباب والمفتاح</span></h2>
            <p>كثير من الناس يشعرون بالذنب الشديد ويظنون أن ما قبل السكري يحدث فقط لأنهم أكلوا قطعة حلوى إضافية، لكن الحقيقة الفسيولوجية أعمق من ذلك بكثير. لنفهم ما يحدث داخل جسدك، تخيل الآتي:</p>
            <ol class="steps">
                <li>في كل مرة تأكل فيها طعاماً (خصوصاً النشويات والسكريات)، يتحول هذا الطعام إلى جلوكوز (سكر) يسبح في مجرى الدم.</li>
                <li>وجود السكر في الدم يدفع البنكرياس لإفراز هرمون يسمى <strong>الإنسولين</strong>.</li>
                <li>الإنسولين وظيفته مثل "المفتاح"؛ يذهب إلى خلايا جسمك (العضلات، الكبد)، يفتح قفل الخلية، ليدخل السكر وتستخدمه الخلية لإنتاج الطاقة والحركة.</li>
            </ol>
            <h3>أين تكمن المشكلة إذاً؟</h3>
            <p>مع مرور السنين، وتكرار الوجبات المليئة بالنشويات السريعة، وقلة الحركة، والتوتر الدائم، أصبحت الخلايا ممتلئة بالسكر ولا تريد المزيد. أقفال الأبواب أصبحت "صدئة وثقيلة"؛ هذا ما نسميه علمياً <a href="{site:/insulin-resistance.html}">مقاومة الإنسولين</a>.</p>
            <p>صار المفتاح العادي لا يفتح الباب بسهولة، فماذا يفعل البنكرياس المسكين؟ يبدأ بالعمل لساعات إضافية (<bdi>Overtime</bdi>)، ويصنع مفاتيح أكثر وأكثر (يفرز كميات هائلة من الإنسولين) حتى يجبر الخلايا على ابتلاع السكر.</p>
            <p>طالما أن البنكرياس قادر على مضاعفة جهده، يظل سكر دمك طبيعياً لسنوات وأنت لا تدري! ولكن بعد فترة، يبدأ البنكرياس بالتعب والإرهاق، فلا يعود قادراً على مواكبة الطلب الهائل؛ هنا يبدأ السكر بالبقاء في الدم والتراكم تدريجياً، لتبدأ أرقام التحليل بالارتفاع نحو 5.7 و6.0 وما فوقها.</p>

            <h2 class="section-title"><i class="fas fa-user-secret"></i> <span>3. هل كنت تشعر بأعراض ولم تنتبه لها؟</span></h2>
            <p>يُطلق على مرحلة ما قبل السكري اسم "اللص الصامت"، لأن الغالبية الساحقة لا يشعرون بأي ألم مفاجئ. لكن الجسم في الحقيقة يرسل إشارات خفية، إذا راجعت شريط ذكرياتك في الأشهر الأخيرة ستجد أنك عشت بعضها:</p>
            <ul class="check-list">
                <li><strong>غيبوبة الطعام بعد الغداء (<bdi>Food Coma</bdi>):</strong> خمول شديد ورغبة ملحة في النوم فور تناول وجبة غداء غنية بالأرز، الخبز، أو المعكرونة.</li>
                <li><strong>شراهة السكر بعد ساعتين من الأكل:</strong> تشعر بجوع مفاجئ ورغبة عارمة في تناول شيء حلو، رغم أنك تناولت وجبة مشبعة قبل قليل؛ والسبب هبوط حاد في سكر الدم ناتج عن موجة الإنسولين العالية.</li>
                <li><strong>دهون البطن والخصر العنيدة:</strong> زيادة ملحوظة في محيط الخصر لا تتزحزح بسهولة؛ فالإنسولين المرتفع هو هرمون تخزين الدهون الأول في الجسم.</li>
                <li><strong>تغيرات جلدية صغيرة:</strong> ظهور بقع داكنة مخملية خفيفة خلف الرقبة أو تحت الإبط (الشواك الأسود)، أو زوائد جلدية صغيرة حول الرقبة؛ وهي علامات خارجية واضحة لمقاومة الإنسولين.</li>
                <li><strong>العطش الخفيف والاستيقاظ للتبول ليلاً:</strong> الجسم يبدأ بمحاولة التخلص من بواقي السكر الزائد عن طريق الكلى.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-flask"></i> <span>4. الحقيقة المثبتة: كيف نوقف القطار علمياً ونخفض التراكمي؟</span></h2>
            <p>دعنا نتفق على حقيقة قاطعة: لا يوجد شاي سحري، ولا خلطة أعشاب على الإنترنت، ولا وصفة سرية تمسح مرحلة ما قبل السكري في ليلة وضحاها. من يخبرك بذلك يبيعك وهماً رخيصاً قد يؤذي صحتك.</p>
            <p>ولكن، في المقابل، هناك حقيقة طبية أثبتتها أضخم الدراسات العالمية (مثل دراسة برنامج الوقاية من السكري الشهيرة <bdi>DPP</bdi>): خلايا البنكرياس في مرحلة ما قبل السكري لم تمت؛ هي فقط منهكة. وإذا خففت عنها العبء، فإن قدرة الجسم على تجديد حساسية الإنسولين وخفض التراكمي هي قدرة مذهلة وحقيقية!</p>
            <div class="tip"><h3>📊 ماذا أثبتت الدراسة؟</h3><p>أظهرت الأبحاث أن فقدان ما بين 5% إلى 7% فقط من وزنك الحالي (أي حوالي 4 إلى 6 كغ إذا كان وزنك 80 كغ)، مع تعديلات ذكية في الحركة ونوعية الأكل، يقلل من احتمال تطور الحالة إلى سكري بنسبة <strong>58%</strong>، أي قرابة ضعف تأثير دواء الميتفورمين (31%) في الدراسة نفسها!</p></div>
            <p>إليك كيف تفعل ذلك عملياً، خطوة بخطوة، وبدون حرمان.</p>

            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>5. خطة الصحن الذكي: كيف تأكل وتخفض السكر بدون حرمان أو جوع؟</span></h2>
            <p>أكبر خطأ يقع فيه من يسمع بكلمة "ما قبل السكري" هو تجويع النفس أو العيش على الخس والماء؛ هذا طريق مسدود ينتهي دائماً بالانتكاس والشراهة. السر لا يكمن في الحرمان، بل في <strong>"ترتيب الأكل"</strong> و<strong>"نوعية المكونات"</strong>.</p>

            <h3>أ. حيلة "ترتيب الأكل" الذهبية (<bdi>Food Sequencing</bdi>)</h3>
            <p>هل تعلم أن تناول نفس مكونات وجبتك، ولكن بترتيب مختلف، يغير تماماً طريقة تعامل جسمك مع السكر؟ أثبتت الدراسات أن تناول الطعام بهذا الترتيب يخفض ذروة ارتفاع السكر بعد الوجبة بنسبة تصل إلى 40%:</p>
            <ol class="steps">
                <li><strong>ابدأ بالألياف أولاً:</strong> صحن السلطة، الخضار الورقية، <a href="{food:cucumber}">الخيار</a>، أو <a href="{food:broccoli}">البروكلي</a>. الألياف تصنع طبقة شبكية هلامية في أمعائك تبطئ امتصاص السكر القادم بعدها.</li>
                <li><strong>انتقل للبروتين والدهون الصحية ثانياً:</strong> البيض، الدجاج، اللحم، السمك، <a href="{food:avocado}">الأفوكادو</a>، أو الجبن و<a href="{food:extra-virgin-olive-oil}">زيت الزيتون</a>. البروتين يحفز هرمونات الشبع ويبطئ إفراغ المعدة.</li>
                <li><strong>اترك النشويات للنهاية:</strong> الأرز، الخبز، أو البطاطا؛ حين تصل النشويات إلى أمعائك تكون شبكة الألياف والبروتين جاهزة لاستقبالها وامتصاصها ببطء شديد، مما يمنع القفزات الحادة في السكر.</li>
            </ol>

            <h3>ب. وجبة الفطور: النغمة التي تقود سائر يومك</h3>
            <p>إذا بدأت يومك بـ<a href="{food:butter-croissant}">كرواسان</a>، قطعة كيك، حبوب إفطار سكرية (كورن فليكس)، أو شاي محلى بثلاث ملاعق سكر، فأنت تشعل حريقاً في سكر دمك منذ الصباح، وسيبقى الإنسولين مرتفعاً طوال اليوم طلباً للمزيد من الكربوهيدرات.</p>
            <p><strong>الفطور المثالي لتسطيح منحنى السكر:</strong></p>
            <ul class="check-list">
                <li><a href="{food:boiled-egg}">بيض مسلوق</a> أو مقلي بزيت زيتون أو زبدة طبيعية.</li>
                <li>نصف حبة <a href="{food:avocado}">أفوكادو</a> أو حفنة مكسرات نيئة (<a href="{food:raw-almonds}">لوز</a> أو <a href="{food:walnuts}">جوز</a>).</li>
                <li>صحن غني بالورقيات الخضراء (<a href="{food:arugula-rocket}">جرجير</a>، <a href="{food:spinach}">سبانخ</a>، <a href="{food:cucumber}">خيار</a>).</li>
                <li>رشة <a href="{food:chia-seeds}">بذور الشيا</a> أو <a href="{food:flax-seeds}">الكتان</a>.</li>
                <li>كأس ماء مع قطرات ليمون طازج.</li>
            </ul>
            <p>(فطور مشبع، غني بالبروتين والدهون النقية، يعطيك طاقة ثابتة لعدة ساعات دون أي هبوط مفاجئ).</p>

            <h3>ج. أطعمة صديقة للبنكرياس اجعلها أساس مائدتك</h3>
            <ul class="check-list">
                <li><strong>الخضار الصليبية والورقية:</strong> <a href="{food:spinach}">السبانخ</a>، <a href="{food:arugula-rocket}">الجرجير</a>، <a href="{food:broccoli}">البروكلي</a>، و<a href="{food:cauliflower}">الزهرة</a>؛ تمنحك شبعاً هائلاً وفيتامينات بدون رفع السكر.</li>
                <li><strong>البقوليات باعتدال:</strong> <a href="{food:lentils}">العدس</a>، <a href="{food:chickpeas}">الحمص</a>، والفاصولياء؛ غنية بألياف تسمى "النشا المقاوم" التي تغذي بكتيريا الأمعاء النافعة.</li>
                <li><strong>الدهون الصحية النقية:</strong> <a href="{food:extra-virgin-olive-oil}">زيت الزيتون البكر الممتاز</a>، حبات <a href="{food:kalamata-olives}">الزيتون</a>، الطحينة السمسمية، والمكسرات النيئة. الدهون ترفع الإنسولين بدرجة ضئيلة وتمنحك شبعاً مستقراً.</li>
                <li><strong>الفواكه الذكية منخفضة الحمل السكري:</strong> لا تقطع الفاكهة كلياً، بل اختر الذكي منها: التوت بأنواعه (<a href="{food:blueberry}">التوت الأزرق</a> و<a href="{food:raspberry}">توت العليق</a>)، <a href="{food:strawberry}">الفراولة</a>، و<a href="{food:apple}">التفاح</a> الأخضر الصغير، وتناولها دائماً بعد الوجبة كثمرة كاملة بأليافها وتجنب عصرها تماماً.</li>
            </ul>

            <h3>د. حيلة النشويات المبردة</h3>
            <p>إذا كنت تشتهي <a href="{food:white-rice}">الأرز</a> أو <a href="{food:boiled-potato}">البطاطا المسلوقة</a>، اطهها ثم اتركها تبرد في الثلاجة لعدة ساعات قبل تناولها (ويمكنك تسخينها لاحقاً). هذه العملية البسيطة تحول جزءاً من نشوياتها إلى "نشا مقاوم" لا يمتصه الجسم كجلوكوز، بل يمر للأمعاء كغذاء للبكتيريا النافعة، مما يقلل ارتفاع السكر بشكل ملحوظ.</p>

            <h2 class="section-title"><i class="fas fa-person-walking"></i> <span>6. حركة العضلات الذكية: "الإسفنجة" التي تمتص السكر بلا إنسولين</span></h2>
            <p>إذا سألت أي شخص: ما هو العضو الذي يضبط السكر؟ سيقول لك فوراً: البنكرياس. وهذا نصف الجواب فقط! العضو الحقيقي الآخر الذي يتولى نحو 80% من امتصاص السكر بعد الوجبات هو <strong>عضلاتك الهيكلية</strong>.</p>
            <p>وهنا السر المذهل الذي لا يعرفه الكثيرون: عندما تتحرك عضلاتك، فإنها قادرة على فتح بواباتها وامتصاص السكر مباشرة من الدم واستخدامه كوقود بدون الحاجة للإنسولين بتاتاً (عبر نواقل تدعى <bdi>GLUT4</bdi>)! أنت بحركتك تعطي البنكرياس استراحة محارب حقيقية.</p>
            <h3>كيف تستغل هذا السحر يومياً دون الذهاب للجيم؟</h3>
            <ul class="check-list">
                <li><strong>سحر الـ 10 إلى 15 دقيقة بعد الأكل:</strong> لا تجلس فور الانتهاء من الغداء أو العشاء. امشِ في غرفتك، تحرك في الحديقة، أو اغسل الأطباق ورتب المنزل. المشي الخفيف مباشرة بعد الوجبة يسحب قمة السكر قبل أن تتراكم في الدم.</li>
                <li><strong>تمرين عضلة الساق وأنت جالس (<bdi>Soleus Pushups</bdi>):</strong> حتى وأنت جالس على مكتبك أو تشاهد التلفاز، رفع الكعبين وإنزالهما بشكل متكرر يشغل عضلة الساق العميقة، وهي عضلة فريدة تستهلك الجلوكوز بكفاءة استثنائية دون إرهاق جسدي.</li>
                <li><strong>تمارين المقاومة البسيطة مرتين أسبوعياً:</strong> الحفاظ على كتلتك العضلية عبر تمارين القرفصاء (<bdi>Squats</bdi>) في المنزل أو الضغط على الجدار يبني "مستودعات إضافية" لتخزين السكر مستقبلاً.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-moon"></i> <span>7. النوم والتوتر: الجنديان المجهولان خلف فحص الصائم المرتفع</span></h2>
            <p>هل تساءلت يوماً: لماذا أستيقظ صباحاً وسكر الصائم لدي 110 أو 115 ملغ/ديسيلتر رغم أنني لم آكل شيئاً طوال 10 ساعات؟ الجواب يكمن في هرمونات التوتر: <a href="{site:/cortisol-stress.html}">الكورتيزول</a> والأدرينالين.</p>
            <p>عندما تسهر طويلاً أو تعيش تحت ضغط نفسي وقلق مزمن، يفرز جسمك الكورتيزول؛ وهذا الهرمون يرسل إشارة فورية للكبد: <em>"نحن في خطر! أطلق مخزون السكر إلى الدم ليمدنا بالطاقة للهرب!"</em>. لذلك، إذا أصلحت أكلك ولم تصلح نومك، سيبقى سكر الصائم مرتفعاً:</p>
            <ul class="check-list">
                <li><strong>نَم من 7 إلى 8 ساعات ليلاً:</strong> ليلة واحدة من قلة النوم (أقل من 5 ساعات) قادرة على تقليل حساسية خلاياك للإنسولين في اليوم التالي بنسبة 25%!</li>
                <li><strong>أغلق مطبخك قبل 3 ساعات من النوم:</strong> تجنب تناول الطعام في وقت متأخر من الليل حتى تمنح جهازك الهضمي والبنكرياس فرصة لإعادة ضبط النفس وإراحة الكبد أثناء النوم.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-route"></i> <span>8. خارطة طريقك العملية: الأسابيع الـ 12 القادمة</span></h2>
            <p>لأن تغيير الحياة لا يحدث بضربة واحدة، قسّم رحلتك إلى أهداف واقعية صغيرة على مدار 12 أسبوعاً (وهي المدة التي تحتاجها كريات الدم الحمراء لتتجدد وينعكس ذلك على فحص التراكمي القادم):</p>
            <h3>📅 الأسبوع 1 إلى 2: تنظيف السوائل وتثبيت الفطور</h3>
            <ul class="check-list">
                <li>توقف تماماً عن شرب السعرات: العصائر (حتى الطبيعية منها)، المشروبات الغازية، والشاي أو القهوة المحلاة. استبدلها بالماء، شاي الأعشاب، أو القهوة السادة.</li>
                <li>اعتمد الفطور الصباحي المعتمد على البيض، الأفوكادو، والألياف، وودع المعجنات والخبز الأبيض صباحاً.</li>
            </ul>
            <h3>📅 الأسبوع 3 إلى 4: عادة المشي وترتيب الصحن</h3>
            <ul class="check-list">
                <li>طبق قاعدة الـ 10 دقائق مشي بعد وجبتك الرئيسية فوراً.</li>
                <li>درب نفسك على أكل الخضار أولاً، ثم اللحوم والبروتينات، وتناول ما تبقى من النشويات في النهاية.</li>
            </ul>
            <h3>📅 الأسبوع 5 إلى 8: الصيام الليلي الطبيعي والنشويات الكاملة</h3>
            <ul class="check-list">
                <li>أرح جهازك الهضمي بصيام ليلي بسيط: 12 ساعة بين آخر لقمة في العشاء وأول لقمة في فطور الصباح (مثلاً: العشاء الساعة 8 مساءً، والفطور الساعة 8 صباحاً).</li>
                <li>استبدل الخبز الأبيض والرز الأبيض بـ<a href="{food:whole-wheat-bread}">الخبز المصنوع من الحبوب الكاملة</a> مع بذور الكتان، و<a href="{food:oatmeal}">حبوب الشوفان الحقيقية</a> غير المعالجة.</li>
            </ul>
            <h3>📅 الأسبوع 9 إلى 12: الثبات وملاحظة التغيرات</h3>
            <ul class="check-list">
                <li>ستلاحظ هنا انخفاضاً حقيقياً في مقاس بنطالك، نشاطاً متواصلاً بعد الغداء دون رغبة بالنوم، واختفاء نوبات الجوع الشديد.</li>
                <li>حدد موعداً مع طبيبك لإعادة فحص السكر التراكمي في نهاية الشهر الثالث، وشاهد بأم عينيك كيف رجعت الأرقام للوراء!</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>9. أسئلة شائعة وإجابات تهمك</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>هل هذا يعني أنني سأحتاج حتماً لدواء منظم السكر (مثل الميتفورمين / جلوكوفاج)؟</h3><p>ليس بالضرورة على الإطلاق. معظم الأطباء يعطون مراجعيهم في مرحلة ما قبل السكري مهلة من 3 إلى 6 أشهر لتعديل نمط الحياة بالغذاء والحركة قبل التفكير بأي علاج دوائي. في كثير من الحالات، النزول الطفيف في الوزن والتعديل الغذائي يكون كافياً وحده لإعادة التراكمي للوضع الطبيعي. وإذا رأى طبيبك حاجة للميتفورمين في حالتك، فهو دواء آمن ومساعد مؤقت، والقرار النهائي دائماً يعود لتقييم طبيبك المشرف.</p></div>
                <div class="faq-item"><h3>كم من الوقت يحتاج السكر التراكمي حتى ينزل؟</h3><p>عمر كريات الدم الحمراء في جسم الإنسان حوالي 90 إلى 120 يوماً. لذلك، أي تحسن تفعله في طعامك وحركتك اليوم سيبدأ بالتأثير فوراً، لكنك لن ترى النتيجة الرقمية الكاملة والدقيقة على ورقة التحليل المخبري إلا بعد مرور 3 أشهر كاملة. لا تتعجل بإعادة الفحص بعد أسبوعين؛ امنح جسمك وقته الطبيعي للترميم.</p></div>
                <div class="faq-item"><h3>هل يجب أن أقطع الخبز والأرز والفواكه تماماً؟</h3><p>لا! هذا التفكير المتطرف هو سبب فشل معظم الحميات. المطلوب هو "الترشيد والذكاء": تقليل كمية النشويات، استبدال الأبيض منها بالحبوب الكاملة، عدم أكل النشويات وحدها على معدة فارغة، واختيار الفواكه كاملة بأليافها بدلاً من عصرها، وأكلها بعد وجبة دسمة وليس كوجبة خفيفة منفردة.</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-heart"></i> <span>رسالة من القلب لكل من يحمل ورقة تحليله اليوم</span></h2>
            <p>اعتبر هذا اليوم تاريخاً فاصلاً في حياتك، ليس كيوم أصابك فيه مرض، بل كيوم قررت فيه أن تسمع لرسالة جسدك الصادقة وتبدأ بالاهتمام به حقاً.</p>
            <p>القطار لم يتحول لسكري، وأبواب الرجوع مفتوحة على مصراعيها، والحلول في متناول يدك: في صحن خضار ملون، في ربع ساعة مشي هادئ بعد طعامك، وفي نوم مريح يرمم خلاياك. ابدأ اليوم بوجبتك القادمة فقط.. وسترى كيف سيكافئك جسدك بالحيوية والأمان.</p>
            <p class="reviewed">تمت مراجعة المقال من قبل الدكتور وسيم حبيب<br>مجموعة ويبو هيلث 🌿</p>'''),
en=dict(
 byline='Medically reviewed by Dr. Wassim Habib',
 title='Prediabetes: How to Stop the Train and Lower Your HbA1c Before It Turns Into Diabetes',
 h1='Prediabetes: How to Stop the Train and Lower Your HbA1c Before It Turns Into Diabetes',
 crumb='Prediabetes',
 cat='Diabetes & Metabolic Health',
 desc='HbA1c between 5.7% and 6.4%? Understand prediabetes in numbers, its hidden signs, and a practical 12-week plan with food, movement and sleep to bring your HbA1c down, based on the DPP study and ADA standards.',
 summary='What your HbA1c and fasting numbers mean, why insulin resistance happens, and a 12-week food, movement and sleep plan to bring your blood sugar back to the safe zone.',
 hero_alt='Balanced healthy breakfast to support HbA1c control and insulin resistance - WiBo Health',
 about=['Prediabetes', 'HbA1c', 'Insulin resistance', 'Type 2 diabetes prevention'],
 disclaimer='⚠️ Medical disclaimer: the content and information in this article are provided for general health education and nutrition awareness. They are in no way a medical diagnosis, a personal treatment plan, or a substitute for advice from your doctor or the healthcare provider who follows your case. Always talk to your doctor before making major changes to your diet or medication.',
 body='''            <p class="lead">Imagine you have just walked out of the lab or your doctor's office, test results in hand, eyes fixed on one number circled in red: an HbA1c of 5.9% or 6.1%, or maybe a fasting blood sugar of 112 mg/dL.</p>
            <p>Perhaps your doctor said one short sentence as you left: <em>"Your sugar is borderline... take care of yourself and eat less."</em></p>
            <p>You step into the street and the thoughts come crashing in like waves: Do I have diabetes now? Are the days of relaxed family meals over? Will I spend the rest of my life on pills and needles? Where do I even start tomorrow morning?</p>
            <p>Before you let the worry swallow your day, take a deep breath and read these words carefully: <strong>you do not have diabetes, this number is not a final verdict or a point of no return, and most important of all: this is not your fault.</strong></p>
            <p>You are not at the end of the road; you are standing at the "early warning station". That lab report is not bad news. It is actually the greatest wake-up call your body could give you. This article is not a complicated medical textbook. It is your practical plan, step by step, to bring your HbA1c back to safety and stop the train before it goes any further.</p>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>1. What does "borderline sugar" mean? Decoding your lab report simply</span></h2>
            <p>The first step to letting go of fear is understanding; we fear what we do not know. When you look at your blood test results, you will find two key terms that thousands of people search for every day:</p>
            <ul class="check-list">
                <li><strong>HbA1c (glycated haemoglobin):</strong> it does not tell you how much sugar is in your blood today or after yesterday's dinner. It is a kind of "memory tape" of your red blood cells that records the average sugar in your blood over the past 90 days.</li>
                <li><strong>Fasting blood glucose:</strong> a test that measures the sugar concentration in your blood after an overnight fast (8 to 10 hours).</li>
            </ul>
            <figure class="article-figure figure-narrow">
                <img src="/images/hba1c-prediabetes-blood-sugar-chart.webp" alt="Colour-coded chart of HbA1c and fasting glucose ranges, including prediabetes - WiBo Health" width="1024" height="935" loading="lazy" decoding="async">
                <figcaption>The three zones for HbA1c and fasting glucose, according to the American Diabetes Association (ADA).</figcaption>
            </figure>
            <p>To make the numbers easy, doctors divide them into three clear zones:</p>

            <div class="tier-title tier-gold"><span class="tier-dot"></span> 🟢 1. The green safe zone (normal)</div>
            <ul class="check-list">
                <li><strong>HbA1c:</strong> below 5.7%.</li>
                <li><strong>Fasting glucose:</strong> below 100 mg/dL (below 5.6 mmol/L).</li>
                <li><strong>What it means:</strong> your cells respond well to insulin and your pancreas works calmly and comfortably.</li>
            </ul>

            <div class="tier-title tier-ok"><span class="tier-dot"></span> 🟡 2. The warning zone and golden opportunity (prediabetes)</div>
            <ul class="check-list">
                <li><strong>HbA1c:</strong> between 5.7% and 6.4%.</li>
                <li><strong>Fasting glucose:</strong> between 100 and 125 mg/dL (5.6 to 6.9 mmol/L).</li>
                <li><strong>What it means:</strong> you are in the "prediabetes" stage. Your blood sugar is higher than normal but has not reached the diabetes threshold. This is your window of opportunity: the body can still restore its balance once you lift the extra load.</li>
            </ul>

            <div class="tier-title tier-avoid"><span class="tier-dot"></span> 🔴 3. The action zone with medical follow-up (type 2 diabetes)</div>
            <ul class="check-list">
                <li><strong>HbA1c:</strong> 6.5% or higher.</li>
                <li><strong>Fasting glucose:</strong> 126 mg/dL or higher (on two separate tests).</li>
                <li><strong>What it means:</strong> the body has passed the warning stage and needs medication and regular follow-up to prevent complications.</li>
            </ul>
            <div class="tip"><h3>💡 A golden rule to remember</h3><p>If your HbA1c today is 5.8, 6.0 or even 6.3, you are in the yellow zone. The train has not reached the last station; it is slowing down right now, and you hold the key to steer it back onto the safe track.</p></div>

            <h2 class="section-title"><i class="fas fa-key"></i> <span>2. Why did the train head this way in the first place? The story of the lock and the key</span></h2>
            <p>Many people feel deeply guilty and think prediabetes happens only because they ate one sweet too many. The physiology goes much deeper than that. To understand what is happening inside your body, picture this:</p>
            <ol class="steps">
                <li>Every time you eat (especially starches and sugars), the food is turned into glucose (sugar) that travels in your bloodstream.</li>
                <li>Sugar in the blood prompts the pancreas to release a hormone called <strong>insulin</strong>.</li>
                <li>Insulin works like a "key": it goes to your body's cells (muscles, liver), unlocks the door, lets the sugar in, and the cell uses it for energy and movement.</li>
            </ol>
            <h3>So where is the problem?</h3>
            <p>Over the years, with repeated meals full of fast starches, little movement and constant stress, the cells have filled up with sugar and do not want more. The locks have become "rusty and stiff": this is what we call <a href="{site:/insulin-resistance.html}">insulin resistance</a>.</p>
            <p>The normal key no longer opens the door easily, so what does the poor pancreas do? It starts working overtime and makes more and more keys (it releases huge amounts of insulin) to force the cells to take in the sugar.</p>
            <p>As long as the pancreas can keep doubling its effort, your blood sugar stays normal for years without you knowing! But after a while the pancreas gets tired and can no longer keep up with the huge demand. That is when sugar starts staying in the blood and building up, and your lab numbers begin to climb towards 5.7, 6.0 and beyond.</p>

            <h2 class="section-title"><i class="fas fa-user-secret"></i> <span>3. Did you have symptoms without noticing?</span></h2>
            <p>Prediabetes is called the "silent thief" because the vast majority feel no sudden pain. But the body does send subtle signals; if you think back over the past months, you may recognise some of them:</p>
            <ul class="check-list">
                <li><strong>The after-lunch food coma:</strong> heavy tiredness and an urge to sleep right after a lunch rich in rice, bread or pasta.</li>
                <li><strong>Sugar cravings two hours after eating:</strong> sudden hunger and a strong urge for something sweet even though you just had a filling meal, caused by a sharp drop in blood sugar after a big insulin wave.</li>
                <li><strong>Stubborn belly and waist fat:</strong> a noticeable increase in waist size that does not shift easily; high insulin is the body's main fat-storage hormone.</li>
                <li><strong>Small skin changes:</strong> faint dark, velvety patches on the back of the neck or under the arms (acanthosis nigricans), or small skin tags around the neck; clear outward signs of insulin resistance.</li>
                <li><strong>Mild thirst and waking up to urinate at night:</strong> the body starts trying to get rid of excess sugar through the kidneys.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-flask"></i> <span>4. The proven truth: how do we stop the train and lower HbA1c, scientifically?</span></h2>
            <p>Let us agree on one firm fact: there is no magic tea, no herbal mix from the internet and no secret recipe that erases prediabetes overnight. Anyone who tells you otherwise is selling you a cheap illusion that could harm your health.</p>
            <p>On the other hand, there is a medical fact proven by the largest studies in the world (such as the well-known Diabetes Prevention Program, DPP): in prediabetes the pancreatic cells are not dead; they are only exhausted. Lighten their load, and the body's ability to restore insulin sensitivity and lower HbA1c is real and remarkable!</p>
            <div class="tip"><h3>📊 What did the study show?</h3><p>Research showed that losing just 5% to 7% of your current weight (about 4 to 6 kg if you weigh 80 kg), together with smart changes in movement and food quality, lowers the chance of progressing to diabetes by <strong>58%</strong>, nearly twice the effect of metformin (31%) in the same study!</p></div>
            <p>Here is how to do it in practice, step by step, without deprivation.</p>

            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>5. The smart plate plan: how to eat and lower your sugar without deprivation or hunger</span></h2>
            <p>The biggest mistake people make when they hear the word "prediabetes" is starving themselves or living on lettuce and water. That is a dead end that always ends in relapse and binge eating. The secret is not deprivation, but <strong>"food order"</strong> and <strong>"ingredient quality"</strong>.</p>

            <h3>A. The golden "food order" trick (food sequencing)</h3>
            <p>Did you know that eating the same meal in a different order completely changes how your body handles the sugar? Studies have shown that eating in this order lowers the after-meal blood sugar peak by up to 40%:</p>
            <ol class="steps">
                <li><strong>Start with fibre:</strong> a salad, leafy greens, <a href="{food:cucumber}">cucumber</a> or <a href="{food:broccoli}">broccoli</a>. Fibre forms a gel-like mesh in your gut that slows down the absorption of the sugar that follows.</li>
                <li><strong>Then protein and healthy fats:</strong> eggs, chicken, meat, fish, <a href="{food:avocado}">avocado</a>, or cheese and <a href="{food:extra-virgin-olive-oil}">olive oil</a>. Protein triggers fullness hormones and slows stomach emptying.</li>
                <li><strong>Leave the starches for last:</strong> rice, bread or potatoes. By the time the starch reaches your gut, the fibre and protein mesh is ready to absorb it very slowly, preventing sharp sugar spikes.</li>
            </ol>

            <h3>B. Breakfast: the tune that sets the rest of your day</h3>
            <p>If you start your day with a <a href="{food:butter-croissant}">croissant</a>, a piece of cake, sugary breakfast cereal (corn flakes) or tea with three spoons of sugar, you set your blood sugar on fire from the morning, and insulin stays high all day asking for more carbohydrates.</p>
            <p><strong>The ideal breakfast to flatten your glucose curve:</strong></p>
            <ul class="check-list">
                <li><a href="{food:boiled-egg}">Boiled eggs</a>, or eggs fried in olive oil or natural butter.</li>
                <li>Half an <a href="{food:avocado}">avocado</a> or a handful of raw nuts (<a href="{food:raw-almonds}">almonds</a> or <a href="{food:walnuts}">walnuts</a>).</li>
                <li>A plate full of leafy greens (<a href="{food:arugula-rocket}">rocket</a>, <a href="{food:spinach}">spinach</a>, <a href="{food:cucumber}">cucumber</a>).</li>
                <li>A sprinkle of <a href="{food:chia-seeds}">chia</a> or <a href="{food:flax-seeds}">flax seeds</a>.</li>
                <li>A glass of water with a few drops of fresh lemon.</li>
            </ul>
            <p>(A filling breakfast, rich in protein and quality fats, that gives you steady energy for hours without a sudden crash.)</p>

            <h3>C. Pancreas-friendly foods to build your meals around</h3>
            <ul class="check-list">
                <li><strong>Cruciferous and leafy vegetables:</strong> <a href="{food:spinach}">spinach</a>, <a href="{food:arugula-rocket}">rocket</a>, <a href="{food:broccoli}">broccoli</a> and <a href="{food:cauliflower}">cauliflower</a>; very filling and full of vitamins without raising your sugar.</li>
                <li><strong>Legumes in moderation:</strong> <a href="{food:lentils}">lentils</a>, <a href="{food:chickpeas}">chickpeas</a> and beans; rich in a fibre called "resistant starch" that feeds your good gut bacteria.</li>
                <li><strong>Quality healthy fats:</strong> <a href="{food:extra-virgin-olive-oil}">extra virgin olive oil</a>, <a href="{food:kalamata-olives}">olives</a>, tahini and raw nuts. Fats raise insulin only slightly and keep you full for longer.</li>
                <li><strong>Smart low-glycaemic-load fruit:</strong> do not cut out fruit completely; choose the smart ones: berries (<a href="{food:blueberry}">blueberries</a>, <a href="{food:raspberry}">raspberries</a>), <a href="{food:strawberry}">strawberries</a> and small green <a href="{food:apple}">apples</a>. Always eat them after a meal, as whole fruit with their fibre, and avoid juicing them.</li>
            </ul>

            <h3>D. The cooled-starch trick</h3>
            <p>If you crave <a href="{food:white-rice}">rice</a> or <a href="{food:boiled-potato}">boiled potatoes</a>, cook them and let them cool in the fridge for a few hours before eating (you can reheat them later). This simple step turns part of the starch into "resistant starch" that the body does not absorb as glucose; it passes to the gut as food for good bacteria, which noticeably reduces the rise in blood sugar.</p>

            <h2 class="section-title"><i class="fas fa-person-walking"></i> <span>6. Smart muscle movement: the "sponge" that soaks up sugar without insulin</span></h2>
            <p>Ask anyone which organ controls blood sugar and they will say: the pancreas. That is only half the answer! The other key organ, which handles about 80% of the sugar uptake after meals, is your <strong>skeletal muscle</strong>.</p>
            <p>And here is the remarkable secret few people know: when your muscles move, they can open their gates and take sugar straight from the blood to use as fuel, without needing insulin at all (through transporters called GLUT4)! By moving, you give your pancreas a well-earned break.</p>
            <h3>How to use this every day without going to the gym</h3>
            <ul class="check-list">
                <li><strong>The 10-to-15-minute magic after eating:</strong> do not sit down right after lunch or dinner. Walk around your room, move in the garden, or wash the dishes and tidy up. Light walking right after a meal pulls down the sugar peak before it builds up in your blood.</li>
                <li><strong>The seated calf exercise (soleus push-ups):</strong> even at your desk or in front of the TV, repeatedly raising and lowering your heels works the deep calf muscle, a unique muscle that burns glucose very efficiently without tiring you out.</li>
                <li><strong>Simple strength exercises twice a week:</strong> keeping your muscle mass with squats at home or wall push-ups builds "extra storage" for sugar in the future.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-moon"></i> <span>7. Sleep and stress: the unknown soldiers behind a high fasting test</span></h2>
            <p>Have you ever wondered why you wake up with a fasting sugar of 110 or 115 mg/dL even though you have not eaten for 10 hours? The answer lies in the stress hormones: <a href="{site:/cortisol-stress.html}">cortisol</a> and adrenaline.</p>
            <p>When you stay up late or live with ongoing pressure and anxiety, your body releases cortisol, which sends an instant signal to the liver: <em>"We are in danger! Release the sugar stores into the blood so we have energy to run!"</em> That is why, if you fix your food but not your sleep, your fasting sugar will stay high:</p>
            <ul class="check-list">
                <li><strong>Sleep 7 to 8 hours a night:</strong> a single short night (less than 5 hours) can lower your cells' insulin sensitivity by 25% the next day!</li>
                <li><strong>Close your kitchen 3 hours before bed:</strong> avoid late-night eating so your digestive system and pancreas can reset and your liver can rest while you sleep.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-route"></i> <span>8. Your practical roadmap: the next 12 weeks</span></h2>
            <p>Because life changes do not happen in one go, split your journey into small, realistic goals over 12 weeks (the time your red blood cells need to renew, which is what your next HbA1c test will reflect):</p>
            <h3>📅 Weeks 1 to 2: clean up your drinks and settle your breakfast</h3>
            <ul class="check-list">
                <li>Stop drinking calories completely: juices (even natural ones), fizzy drinks, and sweetened tea or coffee. Switch to water, herbal tea or plain coffee.</li>
                <li>Move to a breakfast built on eggs, avocado and fibre, and say goodbye to pastries and white bread in the morning.</li>
            </ul>
            <h3>📅 Weeks 3 to 4: the walking habit and the plate order</h3>
            <ul class="check-list">
                <li>Apply the 10-minute walk rule straight after your main meal.</li>
                <li>Train yourself to eat vegetables first, then meat and protein, and finish with whatever starch is left.</li>
            </ul>
            <h3>📅 Weeks 5 to 8: a natural overnight fast and whole grains</h3>
            <ul class="check-list">
                <li>Rest your digestive system with a simple overnight fast: 12 hours between your last bite at dinner and your first bite at breakfast (for example, dinner at 8 pm and breakfast at 8 am).</li>
                <li>Swap white bread and white rice for <a href="{food:whole-wheat-bread}">whole-grain bread</a> with flax seeds, and <a href="{food:oatmeal}">real, unprocessed oats</a>.</li>
            </ul>
            <h3>📅 Weeks 9 to 12: stay steady and notice the changes</h3>
            <ul class="check-list">
                <li>By now you will notice a real drop in your trouser size, steady energy after lunch without the urge to nap, and fewer intense hunger attacks.</li>
                <li>Book an appointment with your doctor to recheck your HbA1c at the end of the third month, and see with your own eyes how the numbers have gone back down!</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>9. Common questions, clear answers</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Does this mean I will definitely need a blood sugar medicine (such as metformin / Glucophage)?</h3><p>Not necessarily at all. Most doctors give people with prediabetes 3 to 6 months to change their lifestyle with food and movement before considering any medication. In many cases, a modest weight loss and a change in diet are enough on their own to bring HbA1c back to normal. If your doctor feels metformin is needed in your case, it is a safe medicine and a temporary help, and the final decision always rests with your doctor's assessment.</p></div>
                <div class="faq-item"><h3>How long does it take for HbA1c to come down?</h3><p>Red blood cells live about 90 to 120 days. So any improvement you make in your food and movement today starts working right away, but you will only see the full, accurate result on your lab report after a full 3 months. Do not rush to retest after two weeks; give your body its natural time to repair.</p></div>
                <div class="faq-item"><h3>Do I have to cut out bread, rice and fruit completely?</h3><p>No! That all-or-nothing thinking is why most diets fail. What you need is "moderation and smart choices": eat smaller amounts of starch, swap white versions for whole grains, do not eat starch on its own on an empty stomach, and choose whole fruit with its fibre instead of juice, eaten after a full meal rather than as a snack on its own.</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-heart"></i> <span>A heartfelt message to everyone holding their lab report today</span></h2>
            <p>See today as a turning point in your life: not the day you got ill, but the day you decided to listen to your body's honest message and truly start taking care of it.</p>
            <p>The train has not turned into diabetes, the way back is wide open, and the answers are within reach: in a colourful plate of vegetables, in a quiet quarter-hour walk after your meal, and in restful sleep that repairs your cells. Start today, with just your next meal, and see how your body rewards you with energy and peace of mind.</p>
            <p class="reviewed">Reviewed by Dr. Wassim Habib<br>WiBo Health Group 🌿</p>'''),
nl=dict(
 byline='Medisch beoordeeld door Dr. Wassim Habib',
 title='Prediabetes: zo zet je de trein stil en verlaag je je HbA1c voordat het diabetes wordt',
 h1='Prediabetes: zo zet je de trein stil en verlaag je je HbA1c voordat het diabetes wordt',
 crumb='Prediabetes',
 cat='Diabetes & metabole gezondheid',
 desc='HbA1c tussen 5,7% en 6,4%? Begrijp prediabetes in cijfers, de verborgen signalen en een praktisch 12-wekenplan met voeding, beweging en slaap om je HbA1c te verlagen, gebaseerd op de DPP-studie en de ADA-richtlijnen.',
 summary='Wat je HbA1c- en nuchtere waarden betekenen, waarom insulineresistentie ontstaat, en een 12-wekenplan met voeding, beweging en slaap om je bloedsuiker terug in de veilige zone te krijgen.',
 hero_alt='Gebalanceerd, gezond ontbijt voor een stabiele HbA1c en minder insulineresistentie - WiBo Health',
 about=['Prediabetes', 'HbA1c', 'Insulin resistance', 'Type 2 diabetes prevention'],
 disclaimer='⚠️ Medische disclaimer: de inhoud en informatie in dit artikel zijn bedoeld voor algemene gezondheidsvoorlichting en voedingsbewustzijn. Ze zijn op geen enkele manier een medische diagnose, een persoonlijk behandelplan of een vervanging van advies van je arts of de zorgverlener die je volgt. Overleg altijd met je arts voordat je grote veranderingen aanbrengt in je voeding of medicatie.',
 body='''            <p class="lead">Stel je voor: je loopt net het lab of de spreekkamer van je arts uit, de uitslag in je hand, je ogen gericht op één getal met een rode cirkel eromheen: een HbA1c van 5,9% of 6,1%, of misschien een nuchtere bloedsuiker van 112 mg/dL (6,2 mmol/L).</p>
            <p>Misschien zei je arts bij het afscheid één korte zin: <em>"Je suiker zit op het randje... let op jezelf en eet wat minder."</em></p>
            <p>Je staat buiten en de gedachten slaan als golven over je heen: heb ik nu diabetes? Zijn de ontspannen maaltijden met mijn familie voorbij? Moet ik de rest van mijn leven pillen slikken en prikken? Waar begin ik morgenochtend?</p>
            <p>Voordat de zorgen je hele dag opslokken: haal diep adem en lees dit met aandacht. <strong>Je hebt geen diabetes, dit getal is geen eindoordeel en geen punt zonder terugkeer, en het allerbelangrijkste: het is niet jouw schuld.</strong></p>
            <p>Je staat niet aan het einde van de weg, maar bij het "vroegtijdige waarschuwingsstation". Die uitslag is geen slecht nieuws. Het is eigenlijk het grootste wake-upsignaal dat je lichaam je kon geven. Dit artikel is geen ingewikkeld medisch handboek, maar je praktische plan, stap voor stap, om je HbA1c terug naar veilig terrein te brengen en de trein stil te zetten voordat hij verder rijdt.</p>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>1. Wat betekent "suiker op het randje"? Je uitslag eenvoudig ontcijferd</span></h2>
            <p>De eerste stap om angst los te laten is begrijpen; we zijn bang voor wat we niet kennen. In je bloeduitslag vind je twee belangrijke termen waar duizenden mensen elke dag naar zoeken:</p>
            <ul class="check-list">
                <li><strong>HbA1c (geglyceerd hemoglobine):</strong> dit zegt niet hoeveel suiker er vandaag of na het eten van gisteren in je bloed zat. Het is een soort "geheugenband" van je rode bloedcellen die de gemiddelde bloedsuiker van de afgelopen 90 dagen vastlegt.</li>
                <li><strong>Nuchtere bloedglucose:</strong> een test die de suikerconcentratie in je bloed meet na een nacht vasten (8 tot 10 uur).</li>
            </ul>
            <figure class="article-figure figure-narrow">
                <img src="/images/hba1c-prediabetes-blood-sugar-chart.webp" alt="Kleurenschema van HbA1c- en nuchtere glucosewaarden, inclusief prediabetes - WiBo Health" width="1024" height="935" loading="lazy" decoding="async">
                <figcaption>De drie zones voor HbA1c en nuchtere glucose volgens de American Diabetes Association (ADA).</figcaption>
            </figure>
            <p>Om het simpel te houden, delen artsen de waarden in drie duidelijke zones in:</p>

            <div class="tier-title tier-gold"><span class="tier-dot"></span> 🟢 1. De groene, veilige zone (normaal)</div>
            <ul class="check-list">
                <li><strong>HbA1c:</strong> lager dan 5,7% (lager dan 39 mmol/mol).</li>
                <li><strong>Nuchtere glucose:</strong> lager dan 100 mg/dL (lager dan 5,6 mmol/L).</li>
                <li><strong>Wat het betekent:</strong> je cellen reageren goed op insuline en je alvleesklier werkt rustig en ontspannen.</li>
            </ul>

            <div class="tier-title tier-ok"><span class="tier-dot"></span> 🟡 2. De waarschuwingszone en gouden kans (prediabetes)</div>
            <ul class="check-list">
                <li><strong>HbA1c:</strong> tussen 5,7% en 6,4% (39 tot 47 mmol/mol).</li>
                <li><strong>Nuchtere glucose:</strong> tussen 100 en 125 mg/dL (5,6 tot 6,9 mmol/L).</li>
                <li><strong>Wat het betekent:</strong> je zit in de fase "prediabetes". Je bloedsuiker is hoger dan normaal, maar heeft de diabetesgrens nog niet bereikt. Dit is je kans: het lichaam kan zijn balans nog herstellen als je de extra belasting wegneemt.</li>
            </ul>

            <div class="tier-title tier-avoid"><span class="tier-dot"></span> 🔴 3. De actiezone met medische begeleiding (diabetes type 2)</div>
            <ul class="check-list">
                <li><strong>HbA1c:</strong> 6,5% of hoger (48 mmol/mol of hoger).</li>
                <li><strong>Nuchtere glucose:</strong> 126 mg/dL of hoger (7,0 mmol/L, bij twee aparte metingen).</li>
                <li><strong>Wat het betekent:</strong> het lichaam is voorbij de waarschuwingsfase en heeft medicatie en regelmatige controle nodig om complicaties te voorkomen.</li>
            </ul>
            <div class="tip"><h3>💡 Een gouden regel om te onthouden</h3><p>Is je HbA1c vandaag 5,8, 6,0 of zelfs 6,3? Dan zit je in de gele zone. De trein heeft het laatste station nog niet bereikt; hij remt nu af, en jij hebt de sleutel in handen om hem terug op het veilige spoor te zetten.</p></div>

            <h2 class="section-title"><i class="fas fa-key"></i> <span>2. Waarom reed de trein überhaupt deze kant op? Het verhaal van het slot en de sleutel</span></h2>
            <p>Veel mensen voelen zich erg schuldig en denken dat prediabetes alleen ontstaat omdat ze een snoepje te veel aten. De fysiologie gaat veel dieper. Om te begrijpen wat er in je lichaam gebeurt, stel je het volgende voor:</p>
            <ol class="steps">
                <li>Elke keer dat je eet (vooral zetmeel en suikers), wordt het voedsel omgezet in glucose (suiker) die door je bloed stroomt.</li>
                <li>Suiker in het bloed zet de alvleesklier aan om een hormoon af te geven: <strong>insuline</strong>.</li>
                <li>Insuline werkt als een "sleutel": het gaat naar je lichaamscellen (spieren, lever), opent het slot, laat de suiker binnen, en de cel gebruikt die voor energie en beweging.</li>
            </ol>
            <h3>Waar zit het probleem dan?</h3>
            <p>Na jaren van maaltijden vol snelle koolhydraten, weinig beweging en constante stress zitten de cellen vol suiker en willen ze niet meer. De sloten zijn "roestig en stroef" geworden: dat noemen we <a href="{site:/insulin-resistance.html}">insulineresistentie</a>.</p>
            <p>De gewone sleutel opent de deur niet meer makkelijk, dus wat doet de arme alvleesklier? Die gaat overuren draaien en maakt steeds meer sleutels (geeft enorme hoeveelheden insuline af) om de cellen te dwingen de suiker op te nemen.</p>
            <p>Zolang de alvleesklier zijn inspanning kan verdubbelen, blijft je bloedsuiker jarenlang normaal zonder dat je het merkt! Maar na een tijd raakt de alvleesklier vermoeid en kan hij de enorme vraag niet meer bijbenen. Dan blijft er suiker in het bloed hangen, stapelt die zich op, en beginnen je waarden te stijgen richting 5,7, 6,0 en hoger.</p>

            <h2 class="section-title"><i class="fas fa-user-secret"></i> <span>3. Had je klachten zonder het te merken?</span></h2>
            <p>Prediabetes wordt de "stille dief" genoemd, omdat de overgrote meerderheid geen plotselinge pijn voelt. Toch stuurt het lichaam subtiele signalen; als je terugdenkt aan de afgelopen maanden, herken je er misschien een paar:</p>
            <ul class="check-list">
                <li><strong>De middagdip na de lunch (food coma):</strong> zware vermoeidheid en een sterke behoefte aan slaap direct na een lunch met veel rijst, brood of pasta.</li>
                <li><strong>Trek in zoet twee uur na het eten:</strong> plotselinge honger en een sterke zin in iets zoets, terwijl je net een vullende maaltijd hebt gegeten, door een snelle daling van de bloedsuiker na een grote insulinegolf.</li>
                <li><strong>Hardnekkig buik- en buikomvangvet:</strong> een merkbare toename van je middelomtrek die niet makkelijk verdwijnt; een hoge insuline is het belangrijkste vetopslaghormoon van het lichaam.</li>
                <li><strong>Kleine huidveranderingen:</strong> lichte, donkere, fluweelachtige plekken in de nek of onder de oksels (acanthosis nigricans), of kleine huidflapjes rond de nek; duidelijke uiterlijke tekenen van insulineresistentie.</li>
                <li><strong>Lichte dorst en 's nachts plassen:</strong> het lichaam probeert overtollige suiker via de nieren kwijt te raken.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-flask"></i> <span>4. De bewezen waarheid: hoe zetten we de trein wetenschappelijk stil en verlagen we de HbA1c?</span></h2>
            <p>Laten we één ding vaststellen: er bestaat geen wonderthee, geen kruidenmengsel van internet en geen geheim recept dat prediabetes van de ene op de andere dag wegveegt. Wie je dat vertelt, verkoopt je een goedkope illusie die je gezondheid kan schaden.</p>
            <p>Daartegenover staat een medisch feit dat door de grootste studies ter wereld is bewezen (zoals het bekende Diabetes Prevention Program, DPP): bij prediabetes zijn de cellen van de alvleesklier niet dood, alleen uitgeput. Verlicht hun last, en het vermogen van het lichaam om de insulinegevoeligheid te herstellen en de HbA1c te verlagen is echt en indrukwekkend!</p>
            <div class="tip"><h3>📊 Wat liet de studie zien?</h3><p>Onderzoek toonde aan dat slechts 5% tot 7% gewichtsverlies (ongeveer 4 tot 6 kg als je 80 kg weegt), samen met slimme aanpassingen in beweging en voedingskwaliteit, de kans op het ontwikkelen van diabetes met <strong>58%</strong> verlaagt: bijna twee keer het effect van metformine (31%) in dezelfde studie!</p></div>
            <p>Zo pak je het in de praktijk aan, stap voor stap en zonder jezelf iets te ontzeggen.</p>

            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>5. Het slimme bordplan: eten en je suiker verlagen zonder honger of strenge regels</span></h2>
            <p>De grootste fout die mensen maken als ze het woord "prediabetes" horen, is zichzelf uithongeren of leven op sla en water. Dat is een doodlopende weg die altijd eindigt in terugval en eetbuien. Het geheim zit niet in ontbering, maar in <strong>"de volgorde van eten"</strong> en <strong>"de kwaliteit van de ingrediënten"</strong>.</p>

            <h3>A. De gouden truc van de eetvolgorde (food sequencing)</h3>
            <p>Wist je dat dezelfde maaltijd in een andere volgorde eten volledig verandert hoe je lichaam met suiker omgaat? Studies tonen aan dat eten in deze volgorde de bloedsuikerpiek na de maaltijd tot 40% verlaagt:</p>
            <ol class="steps">
                <li><strong>Begin met vezels:</strong> een salade, bladgroenten, <a href="{food:cucumber}">komkommer</a> of <a href="{food:broccoli}">broccoli</a>. Vezels vormen een gelachtig netwerk in je darmen dat de opname van de suiker daarna vertraagt.</li>
                <li><strong>Daarna eiwit en gezonde vetten:</strong> eieren, kip, vlees, vis, <a href="{food:avocado}">avocado</a>, of kaas en <a href="{food:extra-virgin-olive-oil}">olijfolie</a>. Eiwit zet verzadigingshormonen aan en vertraagt het legen van de maag.</li>
                <li><strong>Bewaar het zetmeel voor het laatst:</strong> rijst, brood of aardappelen. Als het zetmeel je darmen bereikt, ligt het netwerk van vezels en eiwit al klaar om het heel langzaam op te nemen, zodat scherpe suikerpieken uitblijven.</li>
            </ol>

            <h3>B. Het ontbijt: de toon voor de rest van je dag</h3>
            <p>Begin je de dag met een <a href="{food:butter-croissant}">croissant</a>, een stuk cake, gezoete ontbijtgranen (cornflakes) of thee met drie scheppen suiker, dan zet je je bloedsuiker 's ochtends al in brand, en blijft je insuline de hele dag hoog en vraagt om meer koolhydraten.</p>
            <p><strong>Het ideale ontbijt om je glucosecurve af te vlakken:</strong></p>
            <ul class="check-list">
                <li><a href="{food:boiled-egg}">Gekookte eieren</a>, of eieren gebakken in olijfolie of natuurlijke boter.</li>
                <li>Een halve <a href="{food:avocado}">avocado</a> of een handje ongebrande noten (<a href="{food:raw-almonds}">amandelen</a> of <a href="{food:walnuts}">walnoten</a>).</li>
                <li>Een bord vol bladgroenten (<a href="{food:arugula-rocket}">rucola</a>, <a href="{food:spinach}">spinazie</a>, <a href="{food:cucumber}">komkommer</a>).</li>
                <li>Een snufje <a href="{food:chia-seeds}">chiazaad</a> of <a href="{food:flax-seeds}">lijnzaad</a>.</li>
                <li>Een glas water met een paar druppels verse citroen.</li>
            </ul>
            <p>(Een vullend ontbijt, rijk aan eiwit en goede vetten, dat je urenlang stabiele energie geeft zonder plotselinge dip.)</p>

            <h3>C. Alvleesklier-vriendelijke voeding als basis van je maaltijden</h3>
            <ul class="check-list">
                <li><strong>Kool- en bladgroenten:</strong> <a href="{food:spinach}">spinazie</a>, <a href="{food:arugula-rocket}">rucola</a>, <a href="{food:broccoli}">broccoli</a> en <a href="{food:cauliflower}">bloemkool</a>; zeer vullend en vol vitamines zonder je suiker te verhogen.</li>
                <li><strong>Peulvruchten met mate:</strong> <a href="{food:lentils}">linzen</a>, <a href="{food:chickpeas}">kikkererwten</a> en bonen; rijk aan een vezel die "resistent zetmeel" heet en je goede darmbacteriën voedt.</li>
                <li><strong>Goede, gezonde vetten:</strong> <a href="{food:extra-virgin-olive-oil}">extra vierge olijfolie</a>, <a href="{food:kalamata-olives}">olijven</a>, tahin en ongebrande noten. Vetten verhogen de insuline maar weinig en houden je langer verzadigd.</li>
                <li><strong>Slim fruit met een lage glykemische lading:</strong> schrap fruit niet helemaal, maar kies slim: bessen (<a href="{food:blueberry}">blauwe bessen</a>, <a href="{food:raspberry}">frambozen</a>), <a href="{food:strawberry}">aardbeien</a> en kleine groene <a href="{food:apple}">appels</a>. Eet ze altijd na een maaltijd, als heel fruit met de vezels, en pers ze niet uit.</li>
            </ul>

            <h3>D. De truc met afgekoeld zetmeel</h3>
            <p>Heb je zin in <a href="{food:white-rice}">rijst</a> of <a href="{food:boiled-potato}">gekookte aardappelen</a>? Kook ze en laat ze een paar uur afkoelen in de koelkast voordat je ze eet (opwarmen mag daarna). Deze simpele stap zet een deel van het zetmeel om in "resistent zetmeel", dat het lichaam niet als glucose opneemt maar als voeding voor goede bacteriën naar de darmen laat gaan. Zo stijgt je bloedsuiker merkbaar minder.</p>

            <h2 class="section-title"><i class="fas fa-person-walking"></i> <span>6. Slim bewegen: de "spons" die suiker opneemt zonder insuline</span></h2>
            <p>Vraag iemand welk orgaan de bloedsuiker regelt en je hoort: de alvleesklier. Dat is maar de helft van het antwoord! Het andere sleutelorgaan, dat na maaltijden ongeveer 80% van de suikeropname voor zijn rekening neemt, zijn je <strong>skeletspieren</strong>.</p>
            <p>En hier is het verrassende geheim dat weinig mensen kennen: als je spieren bewegen, kunnen ze hun poorten openen en suiker direct uit het bloed opnemen als brandstof, zonder dat daar insuline voor nodig is (via transporters die GLUT4 heten)! Door te bewegen geef je je alvleesklier een welverdiende pauze.</p>
            <h3>Zo gebruik je dit elke dag, zonder sportschool</h3>
            <ul class="check-list">
                <li><strong>De magie van 10 tot 15 minuten na het eten:</strong> ga na de lunch of het avondeten niet meteen zitten. Loop wat door je kamer, beweeg in de tuin, of doe de afwas en ruim op. Licht wandelen direct na de maaltijd trekt de suikerpiek omlaag voordat die zich in je bloed opbouwt.</li>
                <li><strong>De kuitoefening terwijl je zit (soleus push-ups):</strong> ook achter je bureau of voor de tv: herhaald je hielen optillen en laten zakken traint de diepe kuitspier, een unieke spier die glucose heel efficiënt verbruikt zonder je uit te putten.</li>
                <li><strong>Eenvoudige krachtoefeningen twee keer per week:</strong> je spiermassa behouden met squats thuis of push-ups tegen de muur bouwt "extra opslag" voor suiker in de toekomst.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-moon"></i> <span>7. Slaap en stress: de onbekende soldaten achter een hoge nuchtere waarde</span></h2>
            <p>Heb je je ooit afgevraagd waarom je 's ochtends wakker wordt met een nuchtere suiker van 110 of 115 mg/dL (6,1 tot 6,4 mmol/L), terwijl je 10 uur niets hebt gegeten? Het antwoord zit in de stresshormonen: <a href="{site:/cortisol-stress.html}">cortisol</a> en adrenaline.</p>
            <p>Als je lang opblijft of onder aanhoudende druk en spanning leeft, maakt je lichaam cortisol aan. Dat stuurt meteen een signaal naar de lever: <em>"We zijn in gevaar! Laat de suikervoorraad los in het bloed, zodat we energie hebben om te vluchten!"</em> Daarom blijft je nuchtere suiker hoog als je wel je eten aanpakt, maar niet je slaap:</p>
            <ul class="check-list">
                <li><strong>Slaap 7 tot 8 uur per nacht:</strong> één korte nacht (minder dan 5 uur) kan de insulinegevoeligheid van je cellen de volgende dag met 25% verlagen!</li>
                <li><strong>Sluit je keuken 3 uur voor het slapen:</strong> vermijd laat op de avond eten, zodat je spijsvertering en alvleesklier kunnen herstellen en je lever tijdens de slaap kan rusten.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-route"></i> <span>8. Je praktische routekaart: de komende 12 weken</span></h2>
            <p>Omdat een leven niet in één klap verandert, verdeel je de reis in kleine, haalbare doelen over 12 weken (de tijd die je rode bloedcellen nodig hebben om te vernieuwen, en dat ziet je volgende HbA1c-test terug):</p>
            <h3>📅 Week 1 tot 2: drankjes opschonen en je ontbijt vastleggen</h3>
            <ul class="check-list">
                <li>Stop helemaal met calorieën drinken: sappen (ook natuurlijke), frisdranken en gezoete thee of koffie. Kies water, kruidenthee of zwarte koffie.</li>
                <li>Stap over op een ontbijt met eieren, avocado en vezels, en neem 's ochtends afscheid van gebak en wit brood.</li>
            </ul>
            <h3>📅 Week 3 tot 4: de wandelgewoonte en de volgorde op je bord</h3>
            <ul class="check-list">
                <li>Pas de 10-minutenregel toe: wandel direct na je hoofdmaaltijd.</li>
                <li>Train jezelf om eerst groenten te eten, dan vlees en eiwit, en eindig met wat er van het zetmeel over is.</li>
            </ul>
            <h3>📅 Week 5 tot 8: een natuurlijke nachtelijke vastenperiode en volkoren producten</h3>
            <ul class="check-list">
                <li>Geef je spijsvertering rust met een simpele nachtvasten: 12 uur tussen je laatste hap bij het avondeten en je eerste hap bij het ontbijt (bijvoorbeeld avondeten om 20.00 uur en ontbijt om 8.00 uur).</li>
                <li>Vervang wit brood en witte rijst door <a href="{food:whole-wheat-bread}">volkorenbrood</a> met lijnzaad, en <a href="{food:oatmeal}">echte, onbewerkte havermout</a>.</li>
            </ul>
            <h3>📅 Week 9 tot 12: volhouden en de veranderingen opmerken</h3>
            <ul class="check-list">
                <li>Nu merk je echt dat je broek ruimer zit, je hebt na de lunch constante energie zonder slaapbehoefte, en de heftige hongeraanvallen nemen af.</li>
                <li>Maak een afspraak met je arts om je HbA1c aan het einde van de derde maand opnieuw te laten meten, en zie met eigen ogen hoe de waarden zijn gedaald!</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>9. Veelgestelde vragen en heldere antwoorden</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Betekent dit dat ik zeker een bloedsuikerverlagend medicijn nodig heb (zoals metformine / Glucophage)?</h3><p>Helemaal niet per se. De meeste artsen geven mensen met prediabetes 3 tot 6 maanden om hun leefstijl met voeding en beweging aan te passen voordat ze aan medicatie denken. In veel gevallen is een beetje gewichtsverlies samen met aangepaste voeding al genoeg om de HbA1c weer normaal te krijgen. Vindt je arts metformine in jouw situatie nodig, dan is het een veilig medicijn en een tijdelijke hulp, en de uiteindelijke beslissing ligt altijd bij de beoordeling van je arts.</p></div>
                <div class="faq-item"><h3>Hoe lang duurt het voordat de HbA1c daalt?</h3><p>Rode bloedcellen leven ongeveer 90 tot 120 dagen. Elke verbetering in je voeding en beweging werkt dus meteen, maar het volledige, nauwkeurige resultaat zie je pas na 3 volle maanden op je labuitslag. Laat je niet na twee weken al opnieuw testen; geef je lichaam de natuurlijke tijd om te herstellen.</p></div>
                <div class="faq-item"><h3>Moet ik brood, rijst en fruit helemaal schrappen?</h3><p>Nee! Dat alles-of-niets-denken is de reden dat de meeste diëten mislukken. Wat je nodig hebt is "mate en slimme keuzes": minder zetmeel, de witte varianten vervangen door volkoren, geen zetmeel alleen op een lege maag, en heel fruit met de vezels in plaats van sap, gegeten na een volwaardige maaltijd en niet als losse snack.</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-heart"></i> <span>Een boodschap uit het hart aan iedereen die vandaag zijn uitslag vasthoudt</span></h2>
            <p>Zie vandaag als een keerpunt in je leven: niet als de dag waarop je ziek werd, maar als de dag waarop je besloot te luisteren naar de eerlijke boodschap van je lichaam en er echt voor te gaan zorgen.</p>
            <p>De trein is geen diabetes geworden, de weg terug ligt wijd open en de oplossingen liggen binnen handbereik: in een kleurrijk bord groenten, in een rustig kwartiertje wandelen na het eten en in een goede nachtrust die je cellen herstelt. Begin vandaag, met alleen je volgende maaltijd, en zie hoe je lichaam je beloont met energie en rust.</p>
            <p class="reviewed">Beoordeeld door Dr. Wassim Habib<br>WiBo Health Group 🌿</p>'''),
# Swedish: HbA1c only in mmol/mol (IFCC), glucose only in mmol/l. Fasting limits per WHO as used in Swedish care (IFG 6,1–6,9),
# with the ADA limit named; IGT from the OGTT explained; the HbA1c 39–47 band is presented as international (ADA), not Swedish.
# The %-based ADA chart image is left out on purpose (the zones below carry the numbers).
sv=dict(
 byline='Medicinskt granskad av Dr. Wassim Habib',
 title='Prediabetes: så bromsar du utvecklingen och sänker ditt HbA1c innan det blir diabetes',
 h1='Prediabetes: så bromsar du utvecklingen och sänker ditt HbA1c innan det blir diabetes',
 crumb='Prediabetes',
 cat='Diabetes och metabol hälsa',
 desc='HbA1c mellan 39 och 47 mmol/mol eller förhöjt fasteglukos? Förstå prediabetes i siffror, de dolda tecknen och en praktisk 12-veckorsplan med mat, rörelse och sömn för att sänka ditt HbA1c, byggd på DPP-studien.',
 summary='Vad ditt HbA1c och fasteglukos betyder, varför insulinresistens uppstår och en 12-veckorsplan med mat, rörelse och sömn för att få tillbaka blodsockret till normala nivåer.',
 hero_alt='Balanserad frukost som stöd för blodsockret och insulinkänsligheten – WiBo Health',
 about=['Prediabetes', 'HbA1c', 'Insulin resistance', 'Type 2 diabetes prevention'],
 disclaimer='⚖️ Medicinsk ansvarsfriskrivning: innehållet i den här artikeln är allmän hälsoinformation och utbildning om kost och levnadsvanor. Det är ingen medicinsk diagnos eller personlig behandlingsplan och ersätter inte råd, diagnos eller behandling från legitimerad hälso- och sjukvårdspersonal. Prata alltid med din läkare innan du gör större förändringar i din kost eller dina läkemedel. Kontakta din vårdcentral eller ring 1177 för sjukvårdsrådgivning. Vid akut fara – ring 112.',
 body='''            <p class="lead">Tänk dig att du just har gått ut från vårdcentralen, med provsvaren i handen och blicken fäst vid ett enda rödmarkerat värde: ett HbA1c på 41 eller 43 mmol/mol, eller kanske ett fasteglukos på 6,2 mmol/l.</p>
            <p>Kanske sa läkaren en kort mening när du gick: <em>”Ditt blodsocker ligger lite högt … ta hand om dig och ät lite mindre.”</em></p>
            <p>Du kommer ut på gatan och tankarna sköljer över dig som vågor: Har jag diabetes nu? Är de avslappnade familjemiddagarna slut? Ska jag leva på tabletter och sprutor resten av livet? Var ska jag ens börja i morgon bitti?</p>
            <p>Innan oron tar över din dag, andas djupt och läs de här orden noga: <strong>du har inte diabetes, värdet är ingen slutgiltig dom och ingen punkt utan återvändo, och viktigast av allt: det är inte ditt fel.</strong></p>
            <p>Du står inte vid vägens slut, du står vid ”förvarningsstationen”. Provsvaret är inga dåliga nyheter. Det är faktiskt den bästa väckarklocka kroppen kan ge dig. Den här artikeln är ingen krånglig medicinsk lärobok, utan din praktiska plan, steg för steg, för att få tillbaka ditt HbA1c till trygga nivåer och bromsa tåget innan det går längre.</p>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>1. Vad betyder ”lite högt blodsocker”? Så läser du dina provsvar</span></h2>
            <p>Det första steget bort från rädslan är att förstå; vi är rädda för det vi inte känner till. I dina provsvar hittar du oftast de här begreppen:</p>
            <ul class="check-list">
                <li><strong>HbA1c (långtidssocker):</strong> visar inte hur mycket socker du har i blodet i dag eller efter gårdagens middag. Det är de röda blodkropparnas ”minne”, som speglar ditt genomsnittliga blodsocker de senaste cirka 90 dagarna. I Sverige anges det i mmol/mol.</li>
                <li><strong>Fasteglukos (fP-glukos):</strong> blodsockret efter en natts fasta (8–10 timmar), angivet i mmol/l.</li>
                <li><strong>Sockerbelastning (OGTT):</strong> du dricker en sockerlösning med 75 g glukos och blodsockret mäts efter 2 timmar. Provet visar hur väl kroppen tar hand om en sockermängd.</li>
            </ul>
            <p>Prediabetes är ett samlingsnamn för två tillstånd som kan förekomma var för sig eller tillsammans: <strong>förhöjt fasteglukos</strong> (IFG, ibland kallat nedsatt fasteglukos), där blodsockret är för högt efter nattens fasta, och <strong>nedsatt glukostolerans</strong> (IGT), där kroppen har svårt att ta hand om sockret vid en sockerbelastning. För att göra siffrorna enkla delas de in i tre tydliga zoner:</p>

            <div class="tier-title tier-gold"><span class="tier-dot"></span> 🟢 1. Den gröna trygga zonen (normalt)</div>
            <ul class="check-list">
                <li><strong>HbA1c:</strong> under 39 mmol/mol.</li>
                <li><strong>Fasteglukos:</strong> under 6,1 mmol/l enligt WHO, som används i svensk vård. (Amerikanska ADA drar gränsen lägre, vid 5,6 mmol/l.)</li>
                <li><strong>Sockerbelastning:</strong> under 7,8 mmol/l efter 2 timmar.</li>
                <li><strong>Vad det betyder:</strong> dina celler svarar bra på insulin och bukspottkörteln arbetar lugnt och bekvämt.</li>
            </ul>

            <div class="tier-title tier-ok"><span class="tier-dot"></span> 🟡 2. Varningszonen och den gyllene möjligheten (prediabetes)</div>
            <ul class="check-list">
                <li><strong>Förhöjt fasteglukos (IFG):</strong> 6,1–6,9 mmol/l (WHO). Enligt ADA räknas redan 5,6–6,9 mmol/l.</li>
                <li><strong>Nedsatt glukostolerans (IGT):</strong> 7,8–11,0 mmol/l två timmar efter sockerbelastning.</li>
                <li><strong>HbA1c:</strong> 39–47 mmol/mol. Det här intervallet kommer från ADA och används internationellt; i svensk vård finns inget officiellt HbA1c-intervall för prediabetes, men ett värde i det här spannet är en tydlig signal att se över levnadsvanorna och följa upp provet.</li>
                <li><strong>Vad det betyder:</strong> ditt blodsocker är högre än normalt men har inte nått gränsen för diabetes. Det här är ditt möjlighetsfönster: kroppen kan fortfarande återfå sin balans när du lättar på den extra belastningen.</li>
            </ul>

            <div class="tier-title tier-avoid"><span class="tier-dot"></span> 🔴 3. Zonen för åtgärd och medicinsk uppföljning (typ 2-diabetes)</div>
            <ul class="check-list">
                <li><strong>HbA1c:</strong> 48 mmol/mol eller högre.</li>
                <li><strong>Fasteglukos:</strong> 7,0 mmol/l eller högre.</li>
                <li><strong>Sockerbelastning:</strong> 11,1 mmol/l eller högre efter 2 timmar.</li>
                <li><strong>Vad det betyder:</strong> diagnosen ställs av läkare, i regel efter två förhöjda prov tagna vid olika tillfällen. Kroppen har då passerat varningsstadiet och behöver regelbunden uppföljning, ofta också läkemedel, för att förebygga komplikationer.</li>
            </ul>
            <div class="tip"><h3>💡 En gyllene regel att komma ihåg</h3><p>Om ditt HbA1c i dag är 40, 42 eller till och med 45 mmol/mol är du i den gula zonen. Tåget har inte nått slutstationen; det saktar in just nu, och du har nyckeln till att styra tillbaka det på rätt spår.</p></div>

            <h2 class="section-title"><i class="fas fa-key"></i> <span>2. Varför tog tåget den här vägen från början? Berättelsen om låset och nyckeln</span></h2>
            <p>Många känner stor skuld och tror att prediabetes bara beror på att de ätit en bulle för mycket. Fysiologin går mycket djupare än så. För att förstå vad som händer i kroppen, föreställ dig det här:</p>
            <ol class="steps">
                <li>Varje gång du äter (särskilt stärkelse och socker) omvandlas maten till glukos (socker) som färdas i blodet.</li>
                <li>Sockret i blodet får bukspottkörteln att frisätta ett hormon som heter <strong>insulin</strong>.</li>
                <li>Insulinet fungerar som en ”nyckel”: det går till kroppens celler (muskler, lever), låser upp dörren, släpper in sockret och cellen använder det som energi.</li>
            </ol>
            <h3>Var ligger då problemet?</h3>
            <p>Med åren, med upprepade måltider fulla av snabb stärkelse, lite rörelse och ständig stress, har cellerna fyllts med socker och vill inte ta emot mer. Låsen har blivit ”rostiga och tröga”: det är det vi kallar <a href="{site:/insulin-resistance.html}">insulinresistens</a>.</p>
            <p>Den vanliga nyckeln öppnar inte längre dörren lika lätt, så vad gör den stackars bukspottkörteln? Den börjar arbeta övertid och tillverkar fler och fler nycklar (den frisätter stora mängder insulin) för att tvinga cellerna att ta in sockret.</p>
            <p>Så länge bukspottkörteln orkar dubbla sin insats håller sig blodsockret normalt i flera år utan att du märker något! Men efter ett tag blir bukspottkörteln trött och hinner inte längre med det stora behovet. Då börjar sockret stanna kvar och samlas i blodet, och dina provsvar börjar klättra mot 39, 42 mmol/mol och uppåt.</p>

            <h2 class="section-title"><i class="fas fa-user-secret"></i> <span>3. Hade du symtom utan att märka det?</span></h2>
            <p>Prediabetes kallas ibland ”den tysta tjuven” eftersom de allra flesta inte känner någon plötslig smärta. Men kroppen skickar diskreta signaler; om du tänker tillbaka på de senaste månaderna känner du kanske igen några av dem:</p>
            <ul class="check-list">
                <li><strong>Matkoman efter lunch:</strong> tung trötthet och sömnighet direkt efter en lunch rik på ris, bröd eller pasta.</li>
                <li><strong>Sötsug två timmar efter maten:</strong> plötslig hunger och starkt sug efter något sött trots att du nyss ätit en mättande måltid, orsakat av ett snabbt blodsockerfall efter en stor insulinvåg.</li>
                <li><strong>Envist fett runt magen och midjan:</strong> ett märkbart större midjemått som är svårt att få bort; högt insulin är kroppens viktigaste fettlagringshormon.</li>
                <li><strong>Små hudförändringar:</strong> svaga mörka, sammetslena fläckar i nacken eller under armarna (acanthosis nigricans), eller små hudflikar runt halsen; tydliga yttre tecken på insulinresistens.</li>
                <li><strong>Lätt törst och nattliga toalettbesök:</strong> kroppen börjar försöka göra sig av med överskottssocker via njurarna.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-flask"></i> <span>4. Den bevisade sanningen: hur bromsar vi tåget och sänker HbA1c vetenskapligt?</span></h2>
            <p>Låt oss vara överens om ett faktum: det finns inget magiskt te, ingen örtblandning från nätet och inget hemligt recept som raderar prediabetes över en natt. Den som påstår något annat säljer en billig illusion som kan skada din hälsa.</p>
            <p>Däremot finns det ett medicinskt faktum som bevisats i några av världens största studier (som den välkända Diabetes Prevention Program, DPP): vid prediabetes är bukspottkörtelns celler inte döda, bara utmattade. Lätta på deras börda, så är kroppens förmåga att återfå insulinkänsligheten och sänka HbA1c verklig och anmärkningsvärd!</p>
            <div class="tip"><h3>📊 Vad visade studien?</h3><p>Forskningen visade att en viktnedgång på bara 5–7 % av din nuvarande vikt (ungefär 4–6 kg om du väger 80 kg), tillsammans med smarta förändringar i rörelse och matkvalitet, minskade risken att utveckla diabetes med <strong>58 %</strong>, nästan dubbelt så mycket som läkemedlet metformin (31 %) i samma studie!</p></div>
            <p>Så här gör du i praktiken, steg för steg, utan att svälta dig. (Länkarna till livsmedlen leder till vår livsmedelsguide, som än så länge finns på engelska.)</p>

            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>5. Den smarta tallriken: så äter du för ett lägre blodsocker utan hunger</span></h2>
            <p>Det vanligaste misstaget när man hör ordet ”prediabetes” är att svälta sig eller leva på sallad och vatten. Det är en återvändsgränd som nästan alltid slutar med återfall och hetsätning. Hemligheten är inte att avstå, utan <strong>”matens ordning”</strong> och <strong>”råvarornas kvalitet”</strong>.</p>

            <h3>A. Det gyllene knepet med matens ordning</h3>
            <p>Visste du att samma måltid, äten i en annan ordning, helt ändrar hur kroppen hanterar sockret? Studier har visat att den här ordningen kan sänka blodsockertoppen efter maten med upp till 40 %:</p>
            <ol class="steps">
                <li><strong>Börja med fibrerna:</strong> sallad, gröna blad, <a href="{food:cucumber}">gurka</a> eller <a href="{food:broccoli}">broccoli</a>. Fibrerna bildar ett geléartat nät i tarmen som bromsar upptaget av sockret som kommer efter.</li>
                <li><strong>Sedan protein och nyttigt fett:</strong> ägg, kyckling, kött, fisk, <a href="{food:avocado}">avokado</a> eller ost och <a href="{food:extra-virgin-olive-oil}">olivolja</a>. Proteinet sätter i gång mättnadshormonerna och gör att magsäcken töms långsammare.</li>
                <li><strong>Spara stärkelsen till sist:</strong> ris, bröd eller potatis. När stärkelsen når tarmen är nätet av fibrer och protein redo att ta upp den mycket långsamt, vilket förhindrar kraftiga sockertoppar.</li>
            </ol>

            <h3>B. Frukosten: tonen för resten av dagen</h3>
            <p>Om du börjar dagen med en <a href="{food:butter-croissant}">croissant</a>, en kanelbulle, sockrade flingor eller te med tre sockerbitar sätter du fart på blodsockret redan på morgonen, och insulinet ligger högt hela dagen och ber om mer kolhydrater.</p>
            <p><strong>Den perfekta frukosten för en jämn blodsockerkurva:</strong></p>
            <ul class="check-list">
                <li><a href="{food:boiled-egg}">Kokta ägg</a>, eller ägg stekta i olivolja eller smör.</li>
                <li>En halv <a href="{food:avocado}">avokado</a> eller en näve naturella nötter (<a href="{food:raw-almonds}">mandlar</a> eller <a href="{food:walnuts}">valnötter</a>).</li>
                <li>En tallrik full av gröna blad (<a href="{food:arugula-rocket}">ruccola</a>, <a href="{food:spinach}">spenat</a>, <a href="{food:cucumber}">gurka</a>).</li>
                <li>Ett strö av <a href="{food:chia-seeds}">chiafrön</a> eller <a href="{food:flax-seeds}">linfrön</a>.</li>
                <li>Ett glas vatten med några droppar färsk citron.</li>
            </ul>
            <p>(En mättande frukost rik på protein och bra fetter, som ger jämn energi i flera timmar utan plötslig dipp.)</p>

            <h3>C. Livsmedel som avlastar bukspottkörteln, att bygga dina måltider kring</h3>
            <ul class="check-list">
                <li><strong>Kål och gröna bladgrönsaker:</strong> <a href="{food:spinach}">spenat</a>, <a href="{food:arugula-rocket}">ruccola</a>, <a href="{food:broccoli}">broccoli</a> och <a href="{food:cauliflower}">blomkål</a>; mycket mättande och fulla av vitaminer utan att höja blodsockret.</li>
                <li><strong>Baljväxter med måtta:</strong> <a href="{food:lentils}">linser</a>, <a href="{food:chickpeas}">kikärter</a> och bönor; rika på en fiber som kallas ”resistent stärkelse” och som ger näring åt de goda tarmbakterierna.</li>
                <li><strong>Nyttiga fetter av god kvalitet:</strong> <a href="{food:extra-virgin-olive-oil}">extra jungfruolivolja</a>, <a href="{food:kalamata-olives}">oliver</a>, tahini och naturella nötter. Fett höjer insulinet bara lite och håller dig mätt längre.</li>
                <li><strong>Smart frukt med låg glykemisk belastning:</strong> uteslut inte frukt helt, välj de smarta: bär (<a href="{food:blueberry}">blåbär</a>, <a href="{food:raspberry}">hallon</a>), <a href="{food:strawberry}">jordgubbar</a> och små gröna <a href="{food:apple}">äpplen</a>. Ät dem efter en måltid, hela och med sina fibrer, och undvik att pressa dem till juice.</li>
            </ul>

            <h3>D. Knepet med avsvalnad stärkelse</h3>
            <p>Om du är sugen på <a href="{food:white-rice}">ris</a> eller <a href="{food:boiled-potato}">kokt potatis</a>, koka dem och låt dem svalna i kylen några timmar innan du äter (du kan värma dem igen). Det enkla steget omvandlar en del av stärkelsen till ”resistent stärkelse” som kroppen inte tar upp som glukos; den går vidare till tarmen som mat åt de goda bakterierna, vilket märkbart dämpar blodsockerhöjningen.</p>

            <h2 class="section-title"><i class="fas fa-person-walking"></i> <span>6. Smart muskelrörelse: ”svampen” som suger upp socker utan insulin</span></h2>
            <p>Fråga vem som helst vilket organ som styr blodsockret så svarar de: bukspottkörteln. Det är bara halva svaret! Det andra nyckelorganet, som står för ungefär 80 % av sockerupptaget efter måltider, är din <strong>skelettmuskulatur</strong>.</p>
            <p>Och här är hemligheten som få känner till: när musklerna rör sig kan de öppna sina portar och ta socker direkt från blodet som bränsle, helt utan insulin (via transportörer som kallas GLUT4)! Genom att röra på dig ger du bukspottkörteln en välförtjänt paus.</p>
            <h3>Så använder du det varje dag utan gym</h3>
            <ul class="check-list">
                <li><strong>De magiska 10–15 minuterna efter maten:</strong> sätt dig inte direkt efter lunch eller middag. Gå runt i rummet, rör dig i trädgården eller diska och plocka undan. En lätt promenad direkt efter maten drar ner sockertoppen innan den byggs upp i blodet.</li>
                <li><strong>Vadövningen sittande (soleus push-ups):</strong> även vid skrivbordet eller framför tv:n kan du upprepade gånger lyfta och sänka hälarna. Det arbetar den djupa vadmuskeln, en unik muskel som förbränner glukos mycket effektivt utan att trötta ut dig.</li>
                <li><strong>Enkla styrkeövningar två gånger i veckan:</strong> att behålla muskelmassan med knäböj hemma eller armhävningar mot väggen bygger ”extra förråd” för socker i framtiden.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-moon"></i> <span>7. Sömn och stress: de okända soldaterna bakom ett högt fastevärde</span></h2>
            <p>Har du undrat varför du vaknar med ett fasteglukos på 6,1 eller 6,4 mmol/l trots att du inte ätit på 10 timmar? Svaret finns i stresshormonerna: <a href="{site:/cortisol-stress.html}">kortisol</a> och adrenalin.</p>
            <p>När du är uppe sent eller lever med ständig press och oro frisätter kroppen kortisol, som skickar en omedelbar signal till levern: <em>”Vi är i fara! Släpp ut sockerförråden i blodet så att vi har energi att fly!”</em> Därför förblir fastevärdet högt om du rättar till maten men inte sömnen:</p>
            <ul class="check-list">
                <li><strong>Sov 7–8 timmar per natt:</strong> redan en enda kort natt (under 5 timmar) kan sänka cellernas insulinkänslighet med 25 % nästa dag!</li>
                <li><strong>Stäng köket 3 timmar före sänggåendet:</strong> undvik sena måltider så att matsmältningen och bukspottkörteln kan återhämta sig och levern får vila medan du sover.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-route"></i> <span>8. Din praktiska färdplan: de kommande 12 veckorna</span></h2>
            <p>Eftersom livsstilsförändringar inte sker på en gång, dela upp resan i små, realistiska mål under 12 veckor (den tid de röda blodkropparna behöver för att förnyas, vilket är det ditt nästa HbA1c-prov speglar):</p>
            <h3>📅 Vecka 1–2: rensa bland dryckerna och lägg om frukosten</h3>
            <ul class="check-list">
                <li>Sluta dricka kalorier helt: juice (även naturell), läsk och sötat te eller kaffe. Byt till vatten, örtte eller svart kaffe.</li>
                <li>Gå över till en frukost byggd på ägg, avokado och fibrer, och säg hej då till wienerbröd och vitt bröd på morgonen.</li>
            </ul>
            <h3>📅 Vecka 3–4: promenadvanan och tallrikens ordning</h3>
            <ul class="check-list">
                <li>Inför regeln om 10 minuters promenad direkt efter huvudmålet.</li>
                <li>Träna dig att äta grönsakerna först, sedan kött och protein, och avsluta med den stärkelse som är kvar.</li>
            </ul>
            <h3>📅 Vecka 5–8: en naturlig nattfasta och fullkorn</h3>
            <ul class="check-list">
                <li>Låt matsmältningen vila med en enkel nattfasta: 12 timmar mellan kvällens sista tugga och frukostens första (till exempel middag kl. 20 och frukost kl. 8).</li>
                <li>Byt vitt bröd och vitt ris mot <a href="{food:whole-wheat-bread}">fullkornsbröd</a> med linfrön, fullkornsknäckebröd och <a href="{food:oatmeal}">riktiga, obearbetade havregryn</a>.</li>
            </ul>
            <h3>📅 Vecka 9–12: håll i och lägg märke till förändringarna</h3>
            <ul class="check-list">
                <li>Nu märker du en verklig skillnad i byxstorleken, jämn energi efter lunch utan behov av tupplur och färre kraftiga hungerattacker.</li>
                <li>Boka tid på vårdcentralen för att ta om ditt HbA1c i slutet av tredje månaden, och se med egna ögon hur värdena har gått ner!</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>9. Vanliga frågor, tydliga svar</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Betyder det här att jag måste ta blodsockersänkande läkemedel (som metformin)?</h3><p>Inte alls nödvändigtvis. Vid prediabetes är ändrade levnadsvanor, mat och rörelse, förstahandsåtgärden, och i Sverige används läkemedel som metformin sällan i det här skedet. I många fall räcker en måttlig viktnedgång och ändrade matvanor för att få tillbaka HbA1c till normala nivåer. Om din läkare bedömer att du behöver läkemedel är metformin ett väl beprövat och säkert läkemedel, och beslutet ligger alltid hos din läkare.</p></div>
                <div class="faq-item"><h3>Hur lång tid tar det innan HbA1c går ner?</h3><p>De röda blodkropparna lever i ungefär 90–120 dagar. Varje förbättring du gör i mat och rörelse i dag börjar verka direkt, men det fullständiga och rättvisande resultatet syns i provsvaren först efter tre hela månader. Ta inte om provet efter två veckor; ge kroppen den tid den naturligt behöver för att återhämta sig.</p></div>
                <div class="faq-item"><h3>Måste jag sluta helt med bröd, ris och frukt?</h3><p>Nej! Det där allt-eller-inget-tänkandet är skälet till att de flesta dieter misslyckas. Det du behöver är ”måttlighet och smarta val”: ät mindre mängder stärkelse, byt vita varianter mot fullkorn, ät inte stärkelse ensam på fastande mage, och välj hel frukt med sina fibrer i stället för juice, gärna efter en måltid i stället för som ett ensamt mellanmål.</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-heart"></i> <span>Ett varmt budskap till dig som håller dina provsvar i handen i dag</span></h2>
            <p>Se dagen i dag som en vändpunkt i ditt liv: inte dagen då du blev sjuk, utan dagen då du bestämde dig för att lyssna på kroppens ärliga budskap och verkligen börja ta hand om den.</p>
            <p>Tåget har inte blivit diabetes, vägen tillbaka är vidöppen och svaren finns nära: i en färgglad tallrik grönsaker, i en lugn kvarts promenad efter maten och i en vilsam sömn som reparerar dina celler. Börja i dag, med bara din nästa måltid, och se hur kroppen belönar dig med energi och sinnesro.</p>
            <p class="reviewed">Granskad av Dr. Wassim Habib<br>Grundare, WiBo Health 🌿</p>'''),
    ),
)

# --------------------------------------------------------------------------------------------
# Swedish versions of the older hand-written articles (decision 2026-10-23). Each has only `sv` content here; `legacy`
# names the existing ?lang page (AR/EN/NL) it translates, which becomes its hreflang ar / x-default partner.
# Rules: HbA1c in mmol/mol, glucose in mmol/l; EU 1924/2006 (no cure/reverse/detox wording, authorised claims only);
# signed "Av Dr. Wassim Habib" (byline and schema, 2026-10-23; role unified 2026-10-30).
# --------------------------------------------------------------------------------------------
SV_BYLINE = 'Av Dr. Wassim Habib'
SV_DISCLAIMER = ('⚖️ Medicinsk ansvarsfriskrivning: innehållet i den här artikeln är allmän hälsoinformation och utbildning från '
                 'WiBo Health. Det är ingen medicinsk diagnos eller personlig behandlingsplan och ersätter inte råd, diagnos eller '
                 'behandling från legitimerad hälso- och sjukvårdspersonal. Prata med din läkare innan du gör större förändringar '
                 'i kost eller läkemedel. Kontakta din vårdcentral eller ring 1177 för sjukvårdsrådgivning. Vid akut fara – ring 112.')

INSULIN_RESISTANCE_SV = dict(
    legacy=dict(ar='/insulin-resistance.html'),
    slugs=dict(sv='insulinresistens-hba1c'),
    hero='exercise-insulin.jpg', hero_size=(1376, 751),
    published='2026-10-23', modified='2026-10-23',
    named_author=True,
    faq_schema=True,
    references=[
        'American Diabetes Association Professional Practice Committee. 2. Diagnosis and Classification of Diabetes: Standards of Care in Diabetes—2026. Diabetes Care 2026;49(Suppl 1)',
        'World Health Organization. Use of glycated haemoglobin (HbA1c) in the diagnosis of diabetes mellitus. Geneva: WHO; 2011',
        'Shukla AP, Iliescu RG, Thomas CE, Aronne LJ. Food order has a significant impact on postprandial glucose and insulin levels. Diabetes Care 2015;38(7):e98–e99',
        'Colberg SR, Sigal RJ, Yardley JE, et al. Physical Activity/Exercise and Diabetes: A Position Statement of the American Diabetes Association. Diabetes Care 2016;39(11):2065–2079',
        'Blomhoff R, Andersen R, Arnesen EK, et al. Nordic Nutrition Recommendations 2023. Copenhagen: Nordic Council of Ministers; 2023',
    ],
    content=dict(
sv=dict(
 byline=SV_BYLINE,
 title='HbA1c och insulinresistens: så förstår du dina värden och vad du kan göra själv | WiBo Health',
 h1='HbA1c och insulinresistens: så förstår du dina värden och vad du kan göra själv',
 crumb='HbA1c och insulinresistens',
 cat='Diabetes och metabol hälsa',
 desc='Vad HbA1c i mmol/mol betyder, hur insulinresistens uppstår, de dolda tecknen och hur mat, måltidsordning och rörelse kan förbättra insulinkänsligheten och sänka HbA1c.',
 summary='Vad ditt HbA1c betyder, de dolda tecknen på insulinresistens och de levnadsvanor som kan förbättra insulinkänsligheten.',
 hero_alt='Leende kvinna som joggar på en grusväg i grönskan – rörelse förbättrar musklernas insulinkänslighet',
 about=['HbA1c', 'Insulin resistance', 'Type 2 diabetes prevention', 'Glycemic index'],
 disclaimer=SV_DISCLAIMER,
 body='''            <p class="lead">Många människor lever nära gränsen till typ 2-diabetes utan att veta om det, eftersom tillståndet utvecklas i det tysta under flera år. Bakom den tysta utvecklingen ligger nästan alltid <strong>insulinresistens</strong>.</p>
            <p>Att regelbundet följa sitt HbA1c gör det möjligt att upptäcka förändringar tidigt, långt innan de hinner påverka blodkärl, nerver, njurar och hjärta. I den här guiden förklarar vi sambandet mellan HbA1c och insulinresistens, och vilka levnadsvanor som enligt forskningen kan förbättra kroppens insulinkänslighet.</p>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>Vad är HbA1c och varför är det viktigt?</span></h2>
            <p>HbA1c (långtidssocker) är ett blodprov som speglar ditt genomsnittliga blodsocker de senaste 2–3 månaderna. Principen är enkel: när det finns mycket glukos i blodet binder en del av det till hemoglobinet, proteinet som bär syre i de röda blodkropparna.</p>
            <p>Eftersom en röd blodkropp lever i ungefär 120 dagar ger HbA1c en stabil bild över lång tid, till skillnad från ett enstaka fasteglukos som kan påverkas av gårdagens middag eller av stress. I Sverige anges HbA1c i <strong>mmol/mol</strong>.</p>

            <h2 class="section-title"><i class="fas fa-chart-simple"></i> <span>Så tolkas HbA1c-värdet</span></h2>
            <div class="rule-cards">
                <div class="rule-card"><div class="rule-num">&lt; 39 <small>mmol/mol</small></div><h3>Normalt</h3><p>Cellerna svarar bra på insulin och ämnesomsättningen fungerar väl.</p></div>
                <div class="rule-card"><div class="rule-num">39–47 <small>mmol/mol</small></div><h3>Förhöjt (prediabetes)</h3><p>En tidig varningssignal: bukspottkörteln arbetar hårdare för att hålla blodsockret i schack. Intervallet kommer från ADA och används internationellt.</p></div>
                <div class="rule-card"><div class="rule-num">≥ 48 <small>mmol/mol</small></div><h3>Diabetes</h3><p>Gränsen för typ 2-diabetes. Diagnosen ställs av läkare, i regel efter två förhöjda prov.</p></div>
            </div>
            <p>Läs mer om gränsvärdena, fasteglukos och sockerbelastning i vår <a href="/sv/diabetes/prediabetes.html">guide om prediabetes</a>.</p>

            <h2 class="section-title"><i class="fas fa-key"></i> <span>Insulinresistens: drivkraften bakom ett stigande HbA1c</span></h2>
            <p>Insulin är ett hormon från bukspottkörteln som fungerar som en nyckel: det öppnar cellernas dörrar (framför allt i muskler, lever och fettväv) så att glukos kan komma in och användas som energi. Vid insulinresistens har ”låsen” blivit tröga och svarar sämre på nyckeln.</p>
            <p>Bukspottkörteln kompenserar då genom att frisätta allt mer insulin. Med tiden orkar betacellerna inte hålla samma takt, insulinproduktionen räcker inte till och glukos blir kvar i blodet, och då börjar HbA1c stiga.</p>

            <h2 class="section-title"><i class="fas fa-user-secret"></i> <span>Dolda tecken på insulinresistens</span></h2>
            <ul class="check-list">
                <li><strong>Acanthosis nigricans:</strong> mörka, sammetslena hudpartier i hudveck, särskilt i nacken, i armhålorna och över knogarna.</li>
                <li><strong>Hudflikar (fibrom):</strong> små ofarliga hudutskott, ofta på halsen och bröstet.</li>
                <li><strong>Bukfetma:</strong> ett ökat midjemått (över 102 cm för män och 88 cm för kvinnor) är ett tydligt tecken på rubbad ämnesomsättning.</li>
                <li><strong>Trötthet efter maten:</strong> stark sömnighet och ”hjärndimma” efter kolhydratrika måltider, på grund av snabba blodsockertoppar och följande dippar.</li>
                <li><strong>Starkt sötsug:</strong> trots att det finns mycket socker i blodet får cellerna inte in det, och hjärnan signalerar hunger efter snabba kolhydrater.</li>
            </ul>
            <p>Har du flera av de här tecknen? Ta upp det med din vårdcentral, som kan ta HbA1c och fasteglukos.</p>

            <div class="boodi-card">
                <div>
                    <h2>📱 Skanna varor i butiken med boodi-appen 💚</h2>
                    <p>Skanna streckkoden för att se sockerinnehåll och dolda sockernamn direkt, och hitta alternativ med mindre socker från samma hylla.</p>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> Upptäck boodi</a>
            </div>

            <h2 class="section-title"><i class="fas fa-route"></i> <span>Levnadsvanor som förbättrar insulinkänsligheten och kan sänka HbA1c</span></h2>
            <p>Det goda beskedet är att insulinkänsligheten ofta kan förbättras påtagligt med ändrade levnadsvanor, och att prediabetes i många fall kan återgå till normala värden. Målet är inte att svälta sig, utan att undvika de stora blodsocker- och insulintopparna efter måltiderna. (Länkarna till livsmedlen leder till vår livsmedelsguide, som än så länge finns på engelska.)</p>

            <h3>1. Välj livsmedel med lågt glykemiskt index (GI)</h3>
            <p>Glykemiskt index rangordnar kolhydratrika livsmedel efter hur snabbt de höjer blodsockret:</p>
            <ul class="check-list">
                <li><strong>Begränsa livsmedel med högt GI:</strong> <a href="{food:white-bread}">vitt bröd</a>, <a href="{food:white-rice}">vitt ris</a>, tillsatt socker, juice och friterad potatis, som ger snabba och höga blodsockertoppar.</li>
                <li><strong>Välj oftare alternativ med lågt GI:</strong> <a href="{food:oatmeal}">havregryn</a>, baljväxter (<a href="{food:lentils}">linser</a>, <a href="{food:chickpeas}">kikärter</a>), <a href="{food:quinoa}">quinoa</a>, fullkornsknäckebröd och naturella nötter, som släpper ut glukos gradvis.</li>
            </ul>

            <h3>2. Ät mer fiber</h3>
            <p>Fiber, särskilt den lösliga, gör att magsäcken töms långsammare och att glukos tas upp i lugnare takt. Sikta på minst 25–35 gram fiber per dag, som de nordiska näringsrekommendationerna anger, från grönsaker, baljväxter, fullkorn, <a href="{food:chia-seeds}">chiafrön</a> och bär.</p>

            <h3>3. Ät i smart ordning</h3>
            <p>Studier visar att måltidens ordning påverkar blodsockret märkbart: börja med fiber (sallad och grönsaker), fortsätt med protein och fett (kyckling, fisk, ägg, olivolja) och ät kolhydraterna sist. Den enkla vanan kan sänka blodsockertoppen efter maten med upp till 40 %.</p>

            <h3>4. Låt musklerna ta hand om sockret</h3>
            <p>Skelettmuskulaturen är kroppens största ”förråd” för glukos. Styrketräning och en rask promenad på 10 minuter efter maten aktiverar transportörer (GLUT4) som för in glukos i muskelcellerna, även utan insulin.</p>
            <p>Minst 150 minuter måttlig fysisk aktivitet i veckan, kombinerat med styrketräning två gånger i veckan, förbättrar insulinkänsligheten och kan ge ett lägre HbA1c vid nästa kontroll.</p>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>Vanliga frågor</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Hur lång tid tar det innan HbA1c sjunker efter ändrade levnadsvanor?</h3><p>Eftersom de röda blodkropparna förnyas på ungefär 90–120 dagar rekommenderas att HbA1c tas om först efter tre månader med nya vanor, för att se den verkliga förändringen.</p></div>
                <div class="faq-item"><h3>Kan insulinkänsligheten förbättras utan läkemedel?</h3><p>Ja, i många fall. När bukspottkörtelns betaceller fortfarande fungerar kan en viktnedgång på 7–10 % och mer muskelmassa förbättra insulinkänsligheten påtagligt. Hur mycket som går att förbättra skiljer sig mellan personer, och din läkare bedömer om du även behöver läkemedel.</p></div>
            </div>'''),
    ),
)

LEPTIN_SV = dict(
    legacy=dict(ar='/leptin-resistance.html'),
    slugs=dict(sv='leptinresistens'),
    hero='leptin-hero.jpeg', hero_size=(1376, 768),
    published='2026-10-23', modified='2026-10-23',
    named_author=True,
    faq_schema=True,
    references=[
        'Friedman JM. Leptin and the endocrine control of energy balance. Nat Metab 2019;1(8):754–764',
        'Banks WA, Coon AB, Robinson SM, et al. Triglycerides induce leptin resistance at the blood-brain barrier. Diabetes 2004;53(5):1253–1260',
        'Spiegel K, Tasali E, Penev P, Van Cauter E. Brief communication: sleep curtailment in healthy young men is associated with decreased leptin levels, elevated ghrelin levels, and increased hunger and appetite. Ann Intern Med 2004;141(11):846–850',
        'Blomhoff R, Andersen R, Arnesen EK, et al. Nordic Nutrition Recommendations 2023. Copenhagen: Nordic Council of Ministers; 2023',
    ],
    content=dict(
sv=dict(
 byline=SV_BYLINE,
 title='Varför äter jag men blir aldrig mätt? Leptin, mättnadshormonet som hjärnan slutar lyssna på | WiBo Health',
 h1='Varför äter jag men blir aldrig mätt? Leptin, mättnadshormonet som hjärnan slutar lyssna på',
 crumb='Leptin och mättnad',
 cat='Hormoner och ämnesomsättning',
 desc='Ständig hunger handlar sällan om dålig karaktär. Så fungerar mättnadshormonet leptin, varför hjärnan kan sluta lyssna på det och vilka vanor kring mat, sömn och måltidsrytm som hjälper.',
 summary='Hur mättnadshormonet leptin fungerar, varför hjärnan kan sluta lyssna på det och vilka vardagsvanor som hjälper mättnaden tillbaka.',
 hero_alt='Kvinna som öppnar kylskåpet sent på kvällen – nattligt sötsug och hunger',
 about=['Leptin', 'Leptin resistance', 'Appetite', 'Satiety'],
 disclaimer=SV_DISCLAIMER,
 body='''            <p class="lead">”Du har ätit upp lunchen, druckit kaffet och satt dig för att vila. Tio minuter senare står du framför kylskåpet och letar. Och någon säger: du har ju ingen viljestyrka!”</p>
            <p>Vänta lite. Ständig hunger handlar i de flesta fall inte om dålig karaktär. Bakom den ligger fysiologi: ett samspel mellan hormoner och hjärnans styrcentrum för hunger och mättnad.</p>

            <h2 class="section-title"><i class="fas fa-brain"></i> <span>1. Vad är leptin?</span></h2>
            <p>Kroppens fettceller frisätter ett hormon som heter <strong>leptin</strong>. Det är ett slags mättnadsbud: leptinet färdas med blodet till hypotalamus, hjärnans styrcentral, och berättar att det finns energi i förråden, så att hungern kan dämpas och kroppen kan använda energin som vanligt.</p>
            <p>När systemet fungerar känner du dig nöjd efter en måltid och kan gå flera timmar utan att tänka på mat.</p>

            <h2 class="section-title"><i class="fas fa-ear-deaf"></i> <span>2. När hjärnan slutar lyssna: leptinresistens</span></h2>
            <p>Vid övervikt är problemet sällan för lite leptin. Tvärtom finns det ofta gott om leptin i blodet, men hjärnan svarar sämre på signalen. Det kallas <strong>leptinresistens</strong>.</p>
            <figure class="article-figure">
                <img src="/images/leptin-brain.jpeg" alt="Illustration av hur leptin når hypotalamus och hur signalen kan blockeras" width="1376" height="768" loading="lazy" decoding="async">
                <figcaption>Leptinsignalen till hjärnans hypotalamus (bildtexter på engelska).</figcaption>
            </figure>
            <p>Forskningen pekar på flera bidragande faktorer. Djurstudier tyder på att höga blodfetter (triglycerider), som bland annat ökar av mycket socker i flytande form, kan försämra leptinets transport in i hjärnan. Även långvarig låggradig inflammation och för lite sömn verkar försämra signalen.</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>3. Hjärnan tror att det är svält</span></h2>
            <p>Tänk dig situationen: kroppen har stora energiförråd, men eftersom mättnadssignalen inte når fram uppfattar hjärnan läget som brist. Den svarar som den alltid gjort vid svält: hungern ökar, suget efter snabba kolhydrater blir starkare och kroppen blir mer sparsam med energi.</p>
            <p>Hungern är alltså verklig, inte inbillning.</p>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>4. Frukt eller juice? En viktig skillnad</span></h2>
            <p>Hel frukt i lagom mängd, som ett äpple eller en näve bär, är bra: fibrerna gör att sockret tas upp långsamt. Problemet är juice, där fibrerna har tagits bort och fem frukter ryms i ett glas som dricks på några sekunder, och tillsatt socker och glukos-fruktossirap i kex, godis och färdigmat.</p>

            <h2 class="section-title"><i class="fas fa-list-check"></i> <span>5. Tecken på att mättnadssignalen inte fungerar</span></h2>
            <ul class="check-list">
                <li>Du blir sugen på något sött eller salt en halvtimme efter en måltid.</li>
                <li>Envist fett runt magen och midjan som inte påverkas av vanlig kaloriräkning.</li>
                <li>Stark trötthet och sömnighet direkt efter maten.</li>
                <li>Plötslig hunger sent på kvällen eller på natten.</li>
            </ul>
            <p>Tecknen är vanliga och kan ha många orsaker, till exempel insulinresistens eller sköldkörtelrubbningar. Prata med din vårdcentral om du är osäker.</p>

            <h2 class="section-title"><i class="fas fa-route"></i> <span>6. Vanor som hjälper mättnaden tillbaka</span></h2>
            <ul class="check-list">
                <li><strong>Välj fettkällorna med omsorg:</strong> använd rapsolja och olivolja i matlagningen och ät gärna fisk, nötter och frön, som de nordiska näringsrekommendationerna anger. Begränsa friterad snabbmat och ultraprocessade produkter.</li>
                <li><strong>Stäng av kranen för flytande socker:</strong> ät frukten hel och undvik juice, läsk och sötade drycker.</li>
                <li><strong>Ge kroppen en paus på natten:</strong> en nattfasta på 12–14 timmar sänker insulinnivån. Läs mer i vår artikel om <a href="{site:/intermittent-fasting.html}">periodisk fasta</a>.</li>
                <li><strong>Sov tillräckligt och i mörker:</strong> redan några nätter med för lite sömn sänker leptinet och höjer hungerhormonet ghrelin, så att aptiten ökar nästa dag. Sikta på 7–9 timmar.</li>
                <li><strong>Ät protein och fiber vid varje måltid:</strong> de mättar längst och dämpar blodsockersvängningarna.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>Vanliga frågor</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Kan jag ta leptin som tillskott?</h3><p>Nej. Leptin är ett protein som inte tas upp från tarmen, och det finns inga kosttillskott som höjer leptinkänsligheten. Det som påverkar signalen är mat, sömn, rörelse och vikt.</p></div>
                <div class="faq-item"><h3>Är ständig hunger ett tecken på sjukdom?</h3><p>Oftast inte, men stark hunger tillsammans med törst, täta toalettbesök eller oförklarlig viktförändring ska alltid kontrolleras. Kontakta din vårdcentral eller ring 1177.</p></div>
            </div>'''),
    ),
)

CORTISOL_SV = dict(
    legacy=dict(ar='/cortisol-stress.html'),
    slugs=dict(sv='kortisol-och-stress'),
    hero='cortisol-lifestyle.jpeg', hero_size=(1024, 1024), hero_portrait=True,
    published='2026-10-23', modified='2026-10-23',
    named_author=True,
    faq_schema=True,
    references=[
        'Chrousos GP. Stress and disorders of the stress system. Nat Rev Endocrinol 2009;5(7):374–381',
        'Epel ES, McEwen B, Seeman T, et al. Stress and body shape: stress-induced cortisol secretion is consistently greater among women with central fat. Psychosom Med 2000;62(5):623–632',
        "Nieman LK, Biller BMK, Findling JW, et al. The diagnosis of Cushing's syndrome: an Endocrine Society clinical practice guideline. J Clin Endocrinol Metab 2008;93(5):1526–1540",
        'Commission Regulation (EU) No 432/2012: authorised health claims (magnesium, vitamin C)',
        'EFSA Scientific Committee on Food. Tolerable upper intake levels for vitamins and minerals. Parma: EFSA; 2006 (magnesium from supplements: 250 mg/day)',
    ],
    content=dict(
sv=dict(
 byline=SV_BYLINE,
 title='Kortisol eller kortison? Stresshormonet och bukfettet | WiBo Health',
 h1='Kortisol eller kortison? Stresshormonet och bukfettet',
 crumb='Kortisol och stress',
 cat='Hormoner och ämnesomsättning',
 desc='Skillnaden mellan kroppens stresshormon kortisol och läkemedlet kortison, hur långvarig stress påverkar bukfett och blodsocker, när du ska söka vård och vardagsvanor som lugnar stressystemet.',
 summary='Skillnaden mellan kortisol och kortison, hur långvarig stress påverkar bukfettet och vardagsvanor som lugnar stressystemet.',
 hero_alt='Kvinna som står stilla i en solig skog – återhämtning och lugn för stressystemet',
 about=['Cortisol', 'Stress', 'Visceral fat', 'Cortisone'],
 disclaimer=SV_DISCLAIMER,
 body='''            <p class="lead">Hur många gånger har du ätit enligt planen och tränat regelbundet, men magen har ändå inte rört sig? Ofta handlar det inte om viljestyrka eller felräknade kalorier, utan om ett hormon som styr mycket av kroppens energi: <strong>kortisol</strong>.</p>
            <p>Kortisol är ett livsviktigt hormon som hjälper oss att klara påfrestningar. Men när stressen aldrig släpper och sömnen blir för kort kan samma hormon bidra till högre blodsocker och mer fett runt magen. I den här guiden förklarar vi hur det hänger ihop, reder ut skillnaden mellan kortisol och kortison och går igenom vardagsvanor som lugnar stressystemet.</p>
            <div class="tip"><h3>Viktig skillnad: kortisol och kortison</h3><p><strong>Kortisol</strong> är kroppens eget stresshormon, som bildas i binjurebarken efter ett dygnsmönster och vid stress. <strong>Kortison</strong> är ett läkemedel (tabletter, sprutor, krämer eller inhalationer) som omvandlas till kortisol i kroppen och används mot bland annat inflammation, astma och reumatiska sjukdomar. Det ena bildar kroppen själv, det andra skrivs ut av läkare.</p></div>

            <h2 class="section-title"><i class="fas fa-chart-line"></i> <span>Hur påverkar långvarig stress bukfettet?</span></h2>
            <p>Vid stress aktiverar hjärnan den så kallade HPA-axeln (hypotalamus–hypofys–binjure), och binjurarna frisätter kortisol. Kortisolets uppgift är att snabbt göra energi tillgänglig, bland annat genom att höja blodsockret.</p>
            <p>I dag är stressen oftast psykisk och långvarig, utan den fysiska ansträngning som skulle använda energin. Blodsockret förblir högre, insulinet stiger, och kombinationen av mycket kortisol och mycket insulin gynnar fettinlagring runt magen och de inre organen. Studier har sett att personer med mer bukfett ofta reagerar med högre kortisol vid stress.</p>
            <figure class="article-figure figure-narrow">
                <img src="/images/cortisol-adrenal-chart.jpeg" alt="Illustration av binjurarna ovanpå njurarna, där kortisol bildas" width="1024" height="1024" loading="lazy" decoding="async">
                <figcaption>Binjurarna sitter ovanpå njurarna och bildar kortisol (bildtexter på engelska).</figcaption>
            </figure>

            <div class="boodi-card">
                <div>
                    <h2>📱 Stress höjer blodsockret – välj maten med boodi-appen 💚</h2>
                    <p>Skanna streckkoden för att se socker och dolda sockernamn direkt, och hitta alternativ som ger ett jämnare blodsocker.</p>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> Upptäck boodi</a>
            </div>

            <h2 class="section-title"><i class="fas fa-wave-square"></i> <span>Kortvarig och långvarig stress</span></h2>
            <ul class="check-list">
                <li><strong>Kortvarig stress:</strong> kortisolet stiger för att hantera en utmaning och sjunker när den är över. Det är normalt och nyttigt.</li>
                <li><strong>Långvarig stress:</strong> kroppen får inte tillräcklig återhämtning, sömnen försämras och suget efter sött och salt ökar. Med tiden kan det påverka blodsocker, vikt och humör.</li>
            </ul>
            <p>”Binjuretrötthet” är ingen erkänd medicinsk diagnos. Har du varit stressad länge och känner dig utmattad, sover dåligt eller har svårt att återhämta dig, kontakta din vårdcentral; långvarig stress kan leda till utmattningssyndrom, som behöver bedömas och behandlas av vården.</p>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>Tecken som ska kontrolleras av läkare</span></h2>
            <p>Vissa tecken beror inte på vardagsstress utan kan tyda på att kroppen bildar för mycket kortisol av andra skäl (Cushings syndrom) eller på biverkningar av kortisonbehandling. Sök vård om du har flera av dem:</p>
            <ul class="check-list">
                <li>Rundare ansikte (”månansikte”) och fett i nacken.</li>
                <li>Tunna armar och ben samtidigt som magen växer.</li>
                <li>Breda, rödlila bristningar på magen.</li>
                <li>Muskelsvaghet, särskilt i lår och höfter.</li>
                <li>Högt blodtryck eller högt blodsocker som är svårt att få ner.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-route"></i> <span>Vardagsvanor som lugnar stressystemet</span></h2>
            <p>Att få ner stressnivån kräver varken svält eller lugnande medel, utan vanor som ger kroppen signalen att den är trygg:</p>
            <h3>1. Dagsljus på morgonen</h3>
            <p>Gå ut i dagsljus 10–15 minuter inom en timme efter att du vaknat. Ljuset hjälper dygnsrytmen, ger mer pigghet på dagen och bättre sömn på kvällen. Under den mörka delen av året räcker även en promenad i dagsljus mitt på dagen.</p>
            <h3>2. Kaffe med eftertanke</h3>
            <p>Koffein höjer kortisolet något. Märker du att du blir orolig eller sover sämre, drick kaffet efter frukosten i stället för på fastande mage och undvik kaffe sent på eftermiddagen.</p>
            <h3>3. Mat först, tillskott sist</h3>
            <p>Det finns inga kosttillskott som är godkända för att sänka kortisol. Regelbundna måltider med protein, fiber och grönsaker ger ett jämnare blodsocker och mindre stressreaktioner. Magnesium (från fullkorn, baljväxter, nötter och gröna bladgrönsaker) <strong>bidrar till normal psykologisk funktion</strong> och C-vitamin (från bär, citrusfrukter, paprika och kål) <strong>bidrar till att minska trötthet och utmattning</strong> (EU-godkända påståenden). Om du tar magnesium som tillskott: högst 250 mg per dag, enligt EFSA:s övre gräns.</p>
            <h3>4. Rörelse som återhämtning</h3>
            <p>Mycket hård konditionsträning ovanpå långvarig stress och sömnbrist kan öka belastningen ytterligare. Satsa hellre på styrketräning några gånger i veckan och dagliga promenader på 30–45 minuter i lugnt tempo, gärna i naturen.</p>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>Vanliga frågor</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Kan jag mäta mitt kortisol för att se om jag är stressad?</h3><p>Kortisolprover (i blod, saliv eller urin) används främst för att utreda hormonsjukdomar, till exempel Cushings syndrom eller binjurebarksvikt, och tolkas av läkare. Vid vardaglig stress säger ett enskilt prov sällan särskilt mycket; hur du sover, återhämtar dig och mår är viktigare.</p></div>
                <div class="faq-item"><h3>Jag tar kortison och har gått upp i vikt. Vad gör jag?</h3><p>Längre kortisonbehandling kan ge ökad aptit, vätskeansamling och att fett lagras om, särskilt runt magen och i ansiktet. Prata med din läkare om dosen och om stöd med mat och rörelse. Sluta aldrig ta kortison på egen hand, eftersom det kan vara farligt.</p></div>
            </div>'''),
    ),
)

INTERMITTENT_FASTING_SV = dict(
    legacy=dict(ar='/intermittent-fasting.html'),
    slugs=dict(sv='periodisk-fasta'),
    hero='fasting-hero.jpeg', hero_size=(1376, 768),
    published='2026-10-23', modified='2026-10-23',
    named_author=True,
    faq_schema=True,
    references=[
        'de Cabo R, Mattson MP. Effects of intermittent fasting on health, aging, and disease. N Engl J Med 2019;381(26):2541–2551',
        'Ho KY, Veldhuis JD, Johnson ML, et al. Fasting enhances growth hormone secretion and amplifies the complex rhythms of growth hormone secretion in man. J Clin Invest 1988;81(4):968–975',
        'Betts JA, Richardson JD, Chowdhury EA, et al. The causal role of breakfast in energy balance and health: a randomized controlled trial in lean adults. Am J Clin Nutr 2014;100(2):539–547',
        'Lowe DA, Wu N, Rohdin-Bibby L, et al. Effects of time-restricted eating on weight loss and other metabolic parameters in women and men with overweight and obesity: the TREAT randomized clinical trial. JAMA Intern Med 2020;180(11):1491–1499',
    ],
    content=dict(
sv=dict(
 byline=SV_BYLINE,
 title='Periodisk fasta och myterna i sociala medier: vad säger forskningen? | WiBo Health',
 h1='Periodisk fasta och myterna i sociala medier: vad säger forskningen?',
 crumb='Periodisk fasta',
 cat='Hormoner och ämnesomsättning',
 desc='Periodisk fasta utan myter: vad som händer med insulin och fettförråd när du fastar, hur du bryter fastan klokt, vad du gör vid huvudvärk och vem som inte ska fasta.',
 summary='Vad som händer i kroppen när du fastar, hur du bryter fastan klokt och vem som inte ska fasta.',
 hero_alt='Leende kvinna med ett glas vatten med citron i ett ljust kök',
 about=['Intermittent fasting', 'Time-restricted eating', 'Insulin', 'Breakfast'],
 disclaimer=SV_DISCLAIMER,
 body='''            <p class="lead">”Svälter du? Rädd att ämnesomsättningen kraschar och musklerna försvinner? Ät var tredje timme och hoppa aldrig över frukosten, dagens viktigaste måltid!”</p>
            <p>Låt oss granska de råden med forskningen i handen. För de flesta friska vuxna är en längre paus mellan måltiderna varken farlig för ämnesomsättningen eller musklerna, och frukosten är inte nödvändig för alla.</p>
            <div class="tip"><h3>Vem ska inte fasta?</h3><p>Fasta passar inte om du är <strong>gravid eller ammar</strong>, har eller har haft en <strong>ätstörning</strong>, är <strong>under 18 år</strong>, är <strong>underviktig</strong> eller har <strong>typ 1-diabetes</strong>. Har du <strong>typ 2-diabetes och tar insulin eller andra blodsockersänkande läkemedel</strong> kan fasta ge för lågt blodsocker; prata alltid med din läkare först.</p></div>

            <h2 class="section-title"><i class="fas fa-toggle-on"></i> <span>1. Fasta handlar inte bara om kalorier, utan om insulin</span></h2>
            <p>Många tror att viktnedgång bara är matematik. Kalorier spelar roll, men hormonet <strong>insulin</strong> styr mycket av hur kroppen använder och lagrar energin.</p>
            <p>När du äter ofta under hela dagen ligger insulinet högt, och då använder kroppen mindre av sitt lagrade fett. Under en längre paus sjunker insulinet, hormonet glukagon tar över och kroppen börjar i högre grad använda sina fettförråd som bränsle.</p>

            <div class="boodi-card">
                <div>
                    <h2>📱 Bryt fastan klokt med boodi-appen 💚</h2>
                    <p>Skanna streckkoden för att se socker och glykemiskt index direkt, och välj ett mål som ger jämnt blodsocker efter fastan.</p>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> Upptäck boodi</a>
            </div>

            <h2 class="section-title"><i class="fas fa-dumbbell"></i> <span>2. Försvinner musklerna?</span></h2>
            <p>Vid kortare fasta ökar kroppens frisättning av tillväxthormon, som bland annat hjälper till att skydda muskelmassan. Studier av tidsbegränsat ätande visar att det viktigaste för musklerna är att du äter tillräckligt med protein under dina måltider och fortsätter att styrketräna.</p>
            <p>Forskning, mest från djur- och cellstudier, visar också att fasta sätter i gång <strong>autofagi</strong>, cellernas eget återvinningssystem. Hur stor betydelse det har för människors hälsa undersöks fortfarande.</p>

            <h2 class="section-title"><i class="fas fa-mug-saucer"></i> <span>3. Är frukosten dagens viktigaste måltid?</span></h2>
            <p>Idén blev populär under 1900-talet, inte minst genom reklam för frukostflingor. Randomiserade studier har inte visat att frukost i sig är nödvändig för en sund vikt; för vissa passar frukost bra, för andra inte. Det som spelar störst roll är vad och hur mycket du äter totalt, och att du inte småäter hela dagen.</p>

            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>4. Det vanligaste misstaget: att bryta fastan fel</span></h2>
            <p>Den som har fastat i många timmar och sedan bryter fastan med smoothies, bullar och vitt bröd får en snabb blodsockertopp, ofta följd av en dipp med trötthet och nytt sötsug. Bryt hellre fastan så här:</p>
            <ul class="check-list">
                <li><strong>Börja med något varmt:</strong> ett glas vatten eller en kopp buljong eller soppa.</li>
                <li><strong>Fiber och nyttigt fett:</strong> en grön sallad med olivolja.</li>
                <li><strong>Protein:</strong> ägg, fisk, kyckling, baljväxter eller magert kött, som mättar utan stora blodsockersvängningar.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-head-side-virus"></i> <span>5. Huvudvärk och trötthet när du fastar</span></h2>
            <p>Många nybörjare får huvudvärk eller känner sig yra under de första dagarna. Det beror ofta på för lite vätska och salt, eftersom njurarna gör sig av med mer vatten och natrium när insulinet sjunker, och ibland på att man saknar sitt vanliga kaffe.</p>
            <p>Drick ordentligt med vatten under dagen. En kopp buljong kan hjälpa vid huvudvärk; har du högt blodtryck eller hjärt- eller njursjukdom, prata med din läkare om salt. Blir du yr, skakig eller mår dåligt: avbryt fastan och ät något.</p>

            <h2 class="section-title"><i class="fas fa-venus"></i> <span>6. Råd till kvinnor</span></h2>
            <p>Kvinnors hormonsystem kan reagera känsligare på långa fastor. Undvik dagliga fastor på 20–24 timmar; ett ätfönster med 12–16 timmars nattfasta brukar räcka. Många mår bättre av att korta fastan och äta mer långsamma kolhydrater, som fullkorn och quinoa, veckan före mensen. Får du oregelbunden mens eller mår sämre, avbryt och prata med vården.</p>
            <p>Kort sagt: en nattfasta på 12–16 timmar, mycket vatten, två eller tre näringsrika måltider med protein och grönsaker, och en rask promenad på 30 minuter varje dag. Det är inte svårare än så.</p>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>Vanliga frågor</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Bryter svart kaffe eller te fastan?</h3><p>Nej. Svart kaffe, osötat te och vatten innehåller nästan inga kalorier och höjer inte insulinet nämnvärt. Mjölk, socker och söta drycker bryter däremot fastan.</p></div>
                <div class="faq-item"><h3>Är periodisk fasta säker för alla?</h3><p>Nej. Den passar de flesta friska vuxna, men inte vid graviditet och amning, ätstörningar, undervikt eller typ 1-diabetes, och vid typ 2-diabetes med blodsockersänkande läkemedel bara i samråd med läkare.</p></div>
            </div>'''),
    ),
)

# Batch 3: nutrient articles. Only authorised health claims, worded as in Commission Regulation (EU) No 432/2012
# (Swedish versions); supplement magnesium max 250 mg/day (EFSA UL); iodised salt and max 6 g salt/day (Livsmedelsverket).
MAGNESIUM_SV = dict(
    legacy=dict(ar='/magnesium-types.html'),
    slugs=dict(sv='magnesiumformer'),
    hero='magnesium-types-chart.jpeg', hero_size=(1024, 1024), hero_portrait=True,
    published='2026-10-23', modified='2026-10-23',
    named_author=True,
    faq_schema=True,
    references=[
        'Commission Regulation (EU) No 432/2012 establishing a list of permitted health claims made on foods (magnesium)',
        'EFSA Scientific Committee on Food. Tolerable upper intake levels for vitamins and minerals. Parma: EFSA; 2006 (magnesium from supplements: 250 mg/day)',
        'Firoz M, Graber M. Bioavailability of US commercial magnesium preparations. Magnes Res 2001;14(4):257–262',
        'Blomhoff R, Andersen R, Arnesen EK, et al. Nordic Nutrition Recommendations 2023. Copenhagen: Nordic Council of Ministers; 2023',
    ],
    content=dict(
sv=dict(
 byline=SV_BYLINE,
 title='Magnesiumformer: citrat, bisglycinat eller oxid – vad är skillnaden? | WiBo Health',
 h1='Magnesiumformer: citrat, bisglycinat eller oxid – vad är skillnaden?',
 crumb='Magnesiumformer',
 cat='Kosttillskott',
 desc='Vad skiljer magnesiumformerna åt, hur mycket som är säkert som tillskott (högst 250 mg per dag), vilka läkemedel magnesium påverkar och när maten räcker.',
 summary='Skillnaden mellan magnesiumformerna, den säkra tillskottsdosen och vilka läkemedel magnesium påverkar.',
 hero_alt='Illustration av en magnesiummolekyl och kapslar',
 about=['Magnesium', 'Dietary supplements', 'Minerals'],
 disclaimer=SV_DISCLAIMER,
 body='''            <p class="lead">Du står på apoteket och möts av burkar med namn som bisglycinat, citrat, malat, oxid och taurat. Vilken ska du välja, och behöver du ens ett tillskott?</p>
            <p>Magnesium är ett mineral som kroppen behöver för hundratals enzymreaktioner. Magnesium <strong>bidrar till normal muskelfunktion</strong>, <strong>till normal funktion i nervsystemet</strong>, <strong>till normal energiomsättning</strong> och <strong>till att minska trötthet och utmattning</strong> (EU-godkända påståenden). I ett tillskott är magnesium alltid bundet till ett annat ämne, och det ämnet påverkar hur väl magnesiumet tas upp och hur magen reagerar.</p>
            <div class="tip"><h3>Börja med maten</h3><p>De flesta friska som äter varierat får tillräckligt med magnesium från maten: fullkorn, havregryn, baljväxter, nötter, frön (till exempel pumpafrön), gröna bladgrönsaker och mörk choklad. Brist är ovanlig hos friska, men vanligare vid till exempel långvarig diarré, hög alkoholkonsumtion och vissa läkemedel.</p></div>

            <h2 class="section-title"><i class="fas fa-flask"></i> <span>Magnesiumoxid: billig men sämre upptag</span></h2>
            <p>Magnesiumoxid är den billigaste och vanligaste formen. Den innehåller mycket magnesium per tablett men tas upp sämre i tarmen än de organiska formerna, och det som inte tas upp kan verka lösande på magen.</p>

            <h2 class="section-title"><i class="fas fa-table-list"></i> <span>De vanligaste formerna</span></h2>
            <ul class="check-list">
                <li><strong>Magnesiumbisglycinat (glycinat):</strong> magnesium bundet till aminosyran glycin. Tas upp väl och brukar vara skonsamt för magen, vilket gör det till ett vanligt val för den som får magbesvär av andra former.</li>
                <li><strong>Magnesiumcitrat:</strong> bundet till citronsyra. Tas upp väl. Vid högre doser verkar det lätt lösande, vilket en del uppskattar och andra vill undvika.</li>
                <li><strong>Magnesiummalat:</strong> bundet till äppelsyra. Tas upp väl; ett alternativ för den som vill ta magnesium till frukost.</li>
                <li><strong>Magnesiumtaurat:</strong> bundet till aminosyran taurin. Mindre studerat än citrat och bisglycinat.</li>
                <li><strong>Magnesiumoxid:</strong> mest magnesium per tablett, men sämst upptag och mest magbesvär.</li>
            </ul>
            <p>Oavsett form gäller samma godkända påståenden för magnesium; det finns inga EU-godkända påståenden om att en viss form skulle hjälpa mot sömnproblem eller oro.</p>

            <div class="boodi-card">
                <div>
                    <h2>📱 Granska innehållet med boodi-appen 💚</h2>
                    <p>Skanna streckkoden för att se ingredienser och näringsinnehåll direkt och jämföra produkter från samma hylla.</p>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> Upptäck boodi</a>
            </div>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>Tecken som kan bero på magnesiumbrist</span></h2>
            <p>Symtomen är ospecifika och har oftast andra orsaker, men vid uttalad brist kan man få:</p>
            <ul class="check-list">
                <li>Muskelkramper och muskelryckningar, till exempel i vaderna eller ögonlocket.</li>
                <li>Trötthet och svaghet.</li>
                <li>Hjärtklappning eller oregelbunden puls.</li>
            </ul>
            <p>Har du hjärtklappning, oregelbunden puls eller kramper som inte går över, kontakta vården i stället för att börja med tillskott på egen hand.</p>

            <h2 class="section-title"><i class="fas fa-prescription-bottle"></i> <span>Om du tar magnesium som tillskott</span></h2>
            <h3>1. Dosen: högst 250 mg per dag</h3>
            <p>EFSA har satt den övre gränsen för magnesium från kosttillskott till <strong>250 mg per dag</strong> för vuxna. Räkna på mängden ren magnesium (”elementärt magnesium”) som står i innehållsdeklarationen, inte på vikten av hela föreningen. Över den gränsen ökar risken för diarré och magbesvär.</p>
            <h3>2. Tidpunkt</h3>
            <p>Ta tillskottet i samband med en måltid om magen är känslig. Citrat, som kan verka lösande, tar många hellre på kvällen.</p>
            <h3>3. Läkemedel som påverkas</h3>
            <p>Magnesium kan minska upptaget av vissa läkemedel. Ta magnesium med minst <strong>2–4 timmars mellanrum</strong> från levotyroxin (sköldkörtelhormon), järn- och kalciumtillskott, vissa antibiotika (tetracykliner och kinoloner) och bisfosfonater mot benskörhet. Fråga på apoteket om du är osäker.</p>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>Vanliga frågor</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Visar ett vanligt blodprov om jag har magnesiumbrist?</h3><p>Det vanliga provet i Sverige är magnesium i blodplasma. Eftersom nästan allt magnesium finns i skelettet och cellerna kan ett normalt värde i vissa fall finnas trots låga förråd, så läkaren väger in symtom och sjukdomshistoria.</p></div>
                <div class="faq-item"><h3>Är det säkert att ta magnesium varje dag länge?</h3><p>För friska vuxna med normal njurfunktion är tillskott upp till 250 mg per dag säkert. Har du nedsatt njurfunktion, hjärtsjukdom eller långsam puls ska du prata med din läkare innan du börjar, eftersom magnesium då kan ansamlas i kroppen.</p></div>
            </div>'''),
    ),
)

BONE_HEALTH_SV = dict(
    legacy=dict(ar='/bone-health-minerals.html'),
    slugs=dict(sv='skeletthalsa-och-mineraler'),
    hero='bone-vitality-lifestyle.jpeg', hero_size=(1024, 1024), hero_portrait=True,
    published='2026-10-23', modified='2026-10-23',
    named_author=True,
    faq_schema=True,
    references=[
        'Kanis JA, Cooper C, Rizzoli R, Reginster JY. European guidance for the diagnosis and management of osteoporosis in postmenopausal women. Osteoporos Int 2019;30(1):3–44',
        'Blomhoff R, Andersen R, Arnesen EK, et al. Nordic Nutrition Recommendations 2023. Copenhagen: Nordic Council of Ministers; 2023',
        'Commission Regulation (EU) No 432/2012 establishing a list of permitted health claims made on foods (calcium, vitamin D, vitamin K, magnesium, protein)',
        'Socialstyrelsen. Nationella riktlinjer för rörelseorganens sjukdomar: osteoporos. Stockholm: Socialstyrelsen; 2021',
    ],
    content=dict(
sv=dict(
 byline=SV_BYLINE,
 title='Skeletthälsa: mer än kalcium – D-vitamin, protein, rörelse och mineraler | WiBo Health',
 h1='Skeletthälsa: mer än kalcium – D-vitamin, protein, rörelse och mineraler',
 crumb='Skeletthälsa och mineraler',
 cat='Kost och mineraler',
 desc='Starka ben bygger på mer än kalcium: D-vitamin, protein, magnesium, rörelse och balansträning. Om benskörhet, vem som bör utredas, jodberikat salt och vad du kan göra själv.',
 summary='Vad skelettet behöver utöver kalcium, vem som bör utredas för benskörhet och vad du kan göra själv.',
 hero_alt='Äldre kvinna som tar en rask promenad i en solig park – rörelse för starka ben',
 about=['Bone health', 'Osteoporosis', 'Calcium', 'Vitamin D'],
 disclaimer=SV_DISCLAIMER,
 body='''            <p class="lead">Värk i knäna, knakande leder, ont i ryggen – och oron för benskörhet. Den första reaktionen är ofta att köpa kalciumtabletter och dricka mer mjölk. Men skelettet är levande vävnad som byggs om hela livet, och det behöver betydligt mer än kalcium.</p>
            <p>Sverige har en av världens högsta förekomster av höftfrakturer, och benmassan minskar naturligt med åldern, särskilt hos kvinnor efter klimakteriet. Det går inte att stoppa åldrandet, men mat, rörelse och livsstil påverkar hur starkt skelettet är och hur snabbt det förändras.</p>

            <h2 class="section-title"><i class="fas fa-bone"></i> <span>Näringsämnen som skelettet behöver</span></h2>
            <ul class="check-list">
                <li><strong>Kalcium:</strong> behövs för att upprätthålla normal benstomme. Finns i mjölk, yoghurt, ost, berikade växtdrycker, gröna bladgrönsaker, mandlar och sesamfrön.</li>
                <li><strong>D-vitamin:</strong> bidrar till normalt upptag och utnyttjande av kalcium och till att upprätthålla normal benstomme. Bildas i huden av solljus på sommaren och finns i fet fisk, ägg samt berikad mjölk och margarin.</li>
                <li><strong>Protein:</strong> bidrar till att upprätthålla normal benstomme. Fisk, ägg, mejeriprodukter, baljväxter och kött.</li>
                <li><strong>Magnesium:</strong> bidrar till att upprätthålla normal benstomme. Fullkorn, nötter, frön och baljväxter.</li>
                <li><strong>K-vitamin:</strong> bidrar till att upprätthålla normal benstomme. Gröna bladgrönsaker, kål och vissa ostar.</li>
            </ul>
            <p>(Formuleringarna ovan är EU-godkända hälsopåståenden.) En varierad kost med grönsaker, fullkorn, baljväxter, fisk och mejeriprodukter eller berikade alternativ ger skelettet det mesta av det det behöver.</p>

            <div class="boodi-card">
                <div>
                    <h2>📱 Jämför mejeri- och växtdrycker med boodi-appen 💚</h2>
                    <p>Skanna streckkoden för att se om en växtdryck är berikad med kalcium och D-vitamin, och hur mycket socker den innehåller.</p>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> Upptäck boodi</a>
            </div>

            <h2 class="section-title"><i class="fas fa-sun"></i> <span>D-vitamin under det svenska vinterhalvåret</span></h2>
            <p>Från oktober till mars är solen i Sverige för svag för att huden ska bilda D-vitamin. Då kommer D-vitaminet från maten. Livsmedelsverket rekommenderar extra D-vitamin som tillskott till vissa grupper, till exempel personer som sällan är ute i dagsljus, som täcker huden, har mörk hudfärg eller är 75 år och äldre. Följ dosen på förpackningen eller din läkares råd; mer är inte bättre, eftersom för mycket D-vitamin kan vara skadligt.</p>
            <p>D-vitamin är fettlösligt, så ta tillskottet tillsammans med en måltid.</p>

            <h2 class="section-title"><i class="fas fa-person-walking"></i> <span>Rörelse som bygger och skyddar skelettet</span></h2>
            <ul class="check-list">
                <li><strong>Belastande träning:</strong> promenader, trappgång, dans och lätta hopp stimulerar benvävnaden.</li>
                <li><strong>Styrketräning</strong> två–tre gånger i veckan stärker både muskler och ben.</li>
                <li><strong>Balansträning:</strong> de flesta frakturer hos äldre orsakas av fall, och balansträning minskar risken att falla.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-ban-smoking"></i> <span>Det som försvagar skelettet</span></h2>
            <ul class="check-list">
                <li>Rökning och hög alkoholkonsumtion.</li>
                <li>Låg kroppsvikt och långvariga, hårda bantningskurer.</li>
                <li>Långvarig behandling med kortison i tablettform.</li>
                <li>Tidigt klimakterium.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-user-doctor"></i> <span>När ska man utredas för benskörhet?</span></h2>
            <p>Prata med din vårdcentral om du har brutit något vid ett lågenergitrauma (till exempel fallit från stående och brutit handleden), har tagit kortison länge, har haft tidigt klimakterium eller har benskörhet i släkten. Risken bedöms ofta med verktyget FRAX och vid behov med bentäthetsmätning (DXA).</p>

            <h2 class="section-title"><i class="fas fa-shaker"></i> <span>Salt: välj jodberikat och ät mindre</span></h2>
            <p>Havssalt och rosa salt är kemiskt i stort sett samma sak som vanligt bordssalt (natriumklorid), och mängden andra mineraler i dem är för liten för att ha betydelse. Livsmedelsverket rekommenderar i stället <strong>jodberikat salt</strong>, eftersom jod behövs och ofta saknas i ojodiserade specialsalter, och att vuxna äter <strong>högst 6 gram salt per dag</strong>, för blodtryckets skull.</p>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>Vanliga frågor</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Räcker det att dricka mjölk för att få starka ben?</h3><p>Mjölk och andra mejeriprodukter är bra kalciumkällor, men skelettet behöver också D-vitamin, protein, rörelse och balansträning. Det är helheten som räknas. Dricker du inte mjölk fungerar växtdrycker berikade med kalcium och D-vitamin.</p></div>
                <div class="faq-item"><h3>Ska jag ta K2-vitamin tillsammans med D-vitamin?</h3><p>De flesta får tillräckligt med K-vitamin från maten. Tar du blodförtunnande läkemedel av typen warfarin ska du inte börja med K-vitamintillskott, eftersom det påverkar läkemedlets effekt; prata alltid med din läkare först.</p></div>
            </div>'''),
    ),
)

THYROID_SV = dict(
    legacy=dict(ar='/thyroid-health.html'),
    slugs=dict(sv='trog-skoldkortel'),
    hero='thyroid-hero.jpeg', hero_size=(1376, 768),
    published='2026-10-23', modified='2026-10-23',
    named_author=True,
    faq_schema=True,
    references=[
        'Chaker L, Razvi S, Bensenor IM, et al. Hypothyroidism. Nat Rev Dis Primers 2022;8(1):30',
        'Jonklaas J, Bianco AC, Bauer AJ, et al. Guidelines for the treatment of hypothyroidism: prepared by the American Thyroid Association task force on thyroid hormone replacement. Thyroid 2014;24(12):1670–1751',
        'EFSA Panel on Nutrition, Novel Foods and Food Allergens. Scientific opinion on the tolerable upper intake level for selenium. EFSA J 2023;21(1):7704',
        'Commission Regulation (EU) No 432/2012 establishing a list of permitted health claims made on foods (selenium, iodine)',
        'Blomhoff R, Andersen R, Arnesen EK, et al. Nordic Nutrition Recommendations 2023. Copenhagen: Nordic Council of Ministers; 2023',
    ],
    content=dict(
sv=dict(
 byline=SV_BYLINE,
 title='Trög sköldkörtel: TSH, T4 och T3 i klartext och vad du kan göra själv | WiBo Health',
 h1='Trög sköldkörtel: TSH, T4 och T3 i klartext och vad du kan göra själv',
 crumb='Trög sköldkörtel',
 cat='Hormoner och ämnesomsättning',
 desc='Äter du lite men går ändå upp i vikt, fryser och är trött? Så fungerar sköldkörteln, vad TSH, T4 och T3 betyder, symtomen på underfunktion, jod och selen i maten och när du ska söka vård.',
 summary='Hur sköldkörteln fungerar, vad proverna betyder, symtomen på underfunktion och när du ska söka vård.',
 hero_alt='Leende kvinna i kavaj i en ljus mottagning',
 about=['Hypothyroidism', 'Thyroid', 'TSH', 'Iodine'],
 disclaimer=SV_DISCLAIMER,
 body='''            <p class="lead">”Du äter knappt något och går ändå inte ner ett gram? Du tappar hår, fryser om händer och fötter mitt i sommaren och är ständigt trött?” Sådana besvär kan ha många orsaker, och en av dem är en sköldkörtel som arbetar för långsamt.</p>
            <p>Underfunktion i sköldkörteln (hypotyreos) är vanlig, särskilt hos kvinnor, och den vanligaste orsaken i Sverige är den autoimmuna sjukdomen Hashimotos tyreoidit. Den goda nyheten är att tillståndet är lätt att upptäcka med blodprov och att behandlingen fungerar bra.</p>

            <h2 class="section-title"><i class="fas fa-dna"></i> <span>1. Vad gör sköldkörteln?</span></h2>
            <p>Sköldkörteln är en liten fjärilsformad körtel nedtill på halsen. Dess hormoner styr tempot i kroppens ämnesomsättning: hur mycket energi cellerna gör av med, hur varm du är, hur fort hjärtat slår och hur magen arbetar.</p>
            <p>När sköldkörteln är trög går allt långsammare: du blir trött, fryser lätt, får förstoppning och kan gå upp i vikt trots att du inte äter mer.</p>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>2. TSH, T4 och T3 – vad betyder proverna?</span></h2>
            <ul class="check-list">
                <li><strong>TSH</strong> bildas i hypofysen i hjärnan och ”beställer” hormon från sköldkörteln. När sköldkörteln arbetar för lite stiger TSH. TSH är därför det första och viktigaste provet.</li>
                <li><strong>Fritt T4 (FT4)</strong> är sköldkörtelns huvudsakliga hormon. Det tas ofta tillsammans med TSH.</li>
                <li><strong>T3</strong> är den mest aktiva formen. Det mesta bildas av T4 ute i kroppens vävnader, bland annat i levern och njurarna.</li>
            </ul>
            <p>Har du kvar tydliga symtom trots normala prover, ta upp det med din läkare: symtomen kan bero på något annat, till exempel järnbrist, D-vitaminbrist, sömnbrist eller depression, som också behöver utredas.</p>

            <h2 class="section-title"><i class="fas fa-list-check"></i> <span>3. Vanliga tecken på underfunktion</span></h2>
            <ul class="check-list">
                <li>Trötthet, orkeslöshet och ökat sömnbehov.</li>
                <li>Frusenhet, torr hud och håravfall.</li>
                <li>Förstoppning.</li>
                <li>Svullnad i ansiktet, särskilt runt ögonen på morgonen.</li>
                <li>Viktuppgång utan att man äter mer.</li>
                <li>Koncentrationssvårigheter, nedstämdhet och sämre minne.</li>
            </ul>
            <p>Känner du igen flera av tecknen, boka tid på vårdcentralen och be om provtagning.</p>

            <div class="boodi-card">
                <div>
                    <h2>📱 Hitta jodberikat salt och jämför varor med boodi-appen 💚</h2>
                    <p>Skanna streckkoden för att se ingredienser och näringsinnehåll direkt och jämföra produkter från samma hylla.</p>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> Upptäck boodi</a>
            </div>

            <h2 class="section-title"><i class="fas fa-seedling"></i> <span>4. Jod och selen – i lagom mängd</span></h2>
            <ul class="check-list">
                <li><strong>Jod</strong> bidrar till normal produktion av sköldkörtelhormon och normal sköldkörtelfunktion. I Sverige kommer det mesta jodet från <strong>jodberikat salt</strong>, mejeriprodukter, ägg och fisk. Havssalt och andra specialsalter innehåller ofta lite eller inget jod. Tillskott med tång och alger kan däremot innehålla alldeles för mycket jod, vilket också kan störa sköldkörteln.</li>
                <li><strong>Selen</strong> bidrar till normal sköldkörtelfunktion. Selen finns i fisk, skaldjur, ägg, kött och mejeriprodukter. <a href="{food:brazil-nuts}">Paranötter</a> innehåller mycket och mycket varierande mängder selen; ät dem bara då och då och kombinera dem inte med selentillskott, eftersom för mycket selen är skadligt (EFSA:s övre gräns är 255 mikrogram per dag för vuxna).</li>
            </ul>
            <p>(Formuleringarna om jod och selen är EU-godkända hälsopåståenden.) Om du redan har en diagnostiserad sköldkörtelsjukdom: ta inte jod- eller selentillskott utan att ha pratat med din läkare.</p>

            <h2 class="section-title"><i class="fas fa-route"></i> <span>5. Vardagsvanor som stöder ämnesomsättningen</span></h2>
            <ul class="check-list">
                <li><strong>Undvik hårda svältdieter:</strong> mycket låga energiintag gör att kroppen sparar energi och sänker ämnesomsättningen. En nattfasta på 12–14 timmar är en mer skonsam rytm.</li>
                <li><strong>Ät protein vid varje måltid</strong> och styrketräna, så att du behåller muskelmassan.</li>
                <li><strong>Sov 7–9 timmar</strong> och hitta sätt att hantera långvarig stress.</li>
                <li><strong>Begränsa söta drycker och tillsatt socker,</strong> som belastar levern.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>Vanliga frågor</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Hur behandlas underfunktion i sköldkörteln?</h3><p>Läkaren skriver ut sköldkörtelhormon (levotyroxin) i tablettform och följer upp dosen med blodprov. Tabletten tas på fastande mage, och järn, kalcium och magnesium ska tas med minst fyra timmars mellanrum. Ta aldrig sköldkörtelhormon utan recept.</p></div>
                <div class="faq-item"><h3>Kan jag få igång en trög sköldkörtel med kost eller tillskott?</h3><p>Vid en sjukdom som Hashimotos tyreoidit kan kost och tillskott inte ersätta behandling. En varierad kost med tillräckligt med jod och selen behövs för att sköldkörteln ska fungera normalt, men extra tillskott hjälper inte den som redan får i sig tillräckligt.</p></div>
            </div>'''),
    ),
)

# --------------------------------------------------------------------------------------------
# Fatty liver and visceral fat (2026-10-27): replaces /fatty-liver.html (ar/en/nl via ?lang) and /sv/articles/fettlever.html,
# which now 301 here (vercel.json). Copy by Dr. Wassim Habib, signed by him (user decision 2026-10-27, third named exception).
# Approved corrections: neutral scanner wording (no halal), milk thistle is not "Swedish", published weight-loss figures
# (5% / 7-10% / >=10%) instead of "7-10% melts >80%", no "80% chance" for waist size, EU-authorised wording for omega-3
# (2 g, blood triglycerides), choline (lipid metabolism, liver function) and magnesium (energy metabolism), "studies
# suggest" for milk thistle, coffee, olive oil and sulforaphane, fasting safety note, recover/regress instead of
# cure/treatment, trans fats and reused frying oil instead of all refined vegetable oils, boodi as "coming soon".
# Also listed on the diabetes hub (hubs=['diabetes']) although it lives in /articles/.
# --------------------------------------------------------------------------------------------
FATTY_LIVER_GUIDE = dict(
    hubs=['diabetes'],
    slugs=dict(ar='fatty-liver-and-visceral-fat', en='fatty-liver-and-visceral-fat', nl='fatty-liver-and-visceral-fat',
               sv='fatty-liver-and-visceral-fat'),
    # square cover shown whole (portrait rule); 16:9 cards = the whole photo over a blurred copy of itself
    hero='fatty-liver-visceral-fat.webp', hero_size=(1024, 1024), hero_portrait=True,
    thumb='fatty-liver-guide-thumb.webp', thumb_size=(640, 360), thumb_2x=('fatty-liver-guide-card.webp', 1280),
    published='2026-10-27', modified='2026-10-27',
    references=[
        'Rinella ME, Lazarus JV, Ratziu V, et al. A multisociety Delphi consensus statement on new fatty liver disease nomenclature. J Hepatol 2023;79(6):1542–1556',
        'European Association for the Study of the Liver (EASL), European Association for the Study of Diabetes (EASD), European Association for the Study of Obesity (EASO). EASL–EASD–EASO Clinical Practice Guidelines on the management of metabolic dysfunction-associated steatotic liver disease (MASLD). J Hepatol 2024;81(3):492–542',
        'Vilar-Gomez E, Martinez-Perez Y, Calzadilla-Bertot L, et al. Weight loss through lifestyle modification significantly reduces features of nonalcoholic steatohepatitis. Gastroenterology 2015;149(2):367–378',
        'Promrat K, Kleiner DE, Niemeier HM, et al. Randomized controlled trial testing the effects of weight loss on nonalcoholic steatohepatitis. Hepatology 2010;51(1):121–129',
        'Kennedy OJ, Roderick P, Buchanan R, Fallowfield JA, Hayes PC, Parkes J. Systematic review with meta-analysis: coffee consumption and the risk of cirrhosis. Aliment Pharmacol Ther 2016;43(5):562–574',
        'Alberti KG, Eckel RH, Grundy SM, et al. Harmonizing the metabolic syndrome. Circulation 2009;120(16):1640–1645 (waist circumference thresholds)',
        'Commission Regulation (EU) No 432/2012: authorised health claims for DHA/EPA (normal blood triglyceride levels, 2 g/day), choline (normal lipid metabolism, normal liver function) and magnesium (normal energy-yielding metabolism)',
    ],
    faq_schema=True,
    named_author=True,                                   # user decision 2026-10-27: signed by Dr. Wassim Habib (byline + schema)
    content=dict(
ar=dict(
 byline='بقلم الدكتور وسيم حبيب',
 title='الكبد الدهني أعراضه وأسبابه .. والخبر السعيد تجده في هذا المقال الشامل',
 h1='الكبد الدهني أعراضه وأسبابه .. والخبر السعيد تجده في هذا المقال الشامل',
 crumb='الكبد الدهني والدهون الحشوية',
 cat='الكبد ومتلازمة الأيض',
 desc='أعراض الكبد الدهني وأسبابه الحقيقية، ولماذا يصيب النحيفين أيضاً، والتحاليل التي تكشفه، وجدول الأطعمة الصديقة والمعادية للكبد، وخطة عملية لـ 12 أسبوعاً لتقليل دهون الكبد والكرش الحشوي.',
 summary='لماذا يتراكم الدهن في الكبد حتى عند النحيفين، وكيف تكشفه التحاليل، وخطة 12 أسبوعاً بالغذاء والحركة لتقليل دهون الكبد والكرش الحشوي.',
 hero_alt='امرأة تضع يدها على بطنها في مطبخ مشرق، في إشارة إلى أعراض الكبد الدهني والدهون الحشوية',
 about=['Fatty liver disease', 'MASLD', 'Visceral fat', 'Insulin resistance'],
 disclaimer='⚖️ إخلاء مسؤولية طبي: هذا المقال مقدم لأغراض التثقيف الصحي وتعديل نمط الحياة من WiBo Health، ولا يُعتبر تشخيصاً طبياً ولا بديلاً عن استشارة طبيبك. استشر طبيبك قبل الصيام المتقطع أو تناول أي مكمل غذائي، خاصة إذا كنت تتناول أدوية أو كنتِ حاملاً أو مرضعاً.',
 body='''            <h2 class="section-title"><i class="fas fa-heart"></i> <span>مقدمة من القلب: رسالة إلى كل من يشعر بتعب غير مفهوم</span></h2>
            <p class="lead">إذا كنت تستيقظ في الصباح بعد ثماني ساعات نوم وتشعر وكأنك لم تنم دقيقة واحدة، أو لاحظت أن محيط خصرك بدأ يتسع تدريجياً وأصبح لديك "كرش صلب" يرفض الزوال مهما خففت طعامك، أو ربما أجريت فحص دم روتينياً ففوجئت بالطبيب يقول لك بنبرة هادئة: "تحاليلك جيدة، لكن لديك القليل من الدهون على الكبد"، فهذا الدليل كُتب خصيصاً من أجلك.</p>
            <p>أول ما أريدك أن تعرفه وتضعه في قلبك كطبيب يتحدث إلى صديق: <strong>لا تقلق، ولست وحدك، والأهم من كل ذلك أن كبدك قادر على التعافي؛ ففي المراحل المبكرة يمكن أن تتراجع دهونه بالكامل خلال أسابيع إلى أشهر قليلة.</strong></p>
            <p>الكبد الدهني ليس حكماً مؤبداً، والدهون الحشوية التي تختبئ خلف عضلات بطنك ليست قدراً محتوماً. في هذا المقال سنضع المصطلحات الطبية المعقدة جانباً، ونتحدث بلغة الحياة اليومية: ما الذي يحدث داخل جسدك بهدوء؟ لماذا يصاب به حتى الأشخاص النحيفون؟ وما الخطة اليومية البسيطة التي تقلل هذه الدهون وتعيد إليك صفاء ذهنك وطاقتك وخفتك؟</p>

            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>1. ما هو الكبد الدهني والكرش الحشوي أصلاً؟ (ولماذا يصيب حتى النحيفين؟)</span></h2>
            <p>لنتخيل معاً أن جسدك منزل أنيق، والكبد هو "المطبخ المركزي ومحطة التصفية" في هذا المنزل. وظيفته الأساسية تحويل الطعام إلى طاقة، وتخزين القليل من المغذيات، وتنقية دمك على مدار الساعة.</p>
            <p>في الحالة الطبيعية يحتوي الكبد على نسبة قليلة جداً من الدهون (أقل من 5% من وزنه). وعندما تتجاوز الدهون المخزنة فيه 5% نصبح أمام حالة نسميها طبياً <strong>الكبد الدهني</strong>، وتحديداً النوع المرتبط بمتلازمة الأيض والإفراط في السكريات والنشويات، واسمه العلمي الحديث <bdi>MASLD</bdi>.</p>
            <h3>أسطورة "الدهون تأتي من أكل الدهون"</h3>
            <p>أكبر خرافة يقع فيها الناس هي الاعتقاد بأن أكل دهون اللحم أو الزيت هو ما يسبب دهون الكبد. الحقيقة السريرية أن العدو الأول للكبد الدهني هو <strong>السكر والنشويات المكررة، وخاصة سكر الفركتوز</strong>.</p>
            <p>عندما تتناول مشروباً غازياً أو عصيراً محلى أو وجبة سريعة غنية بالدقيق الأبيض، يمتص جسدك هذه السكريات بسرعة هائلة. العضلات لا تستوعب كل هذه الطاقة، فيضطر الكبد إلى تحويل السكر الفائض إلى دهون ثلاثية بعملية داخلية سريعة.</p>
            <h3>لغز "النحيف الذي يمتلك كبداً دهنياً" (ظاهرة <bdi>TOFI</bdi>)</h3>
            <p>كثير من الناس يقولون: "يا دكتور، وزني 65 كغ ولا أعاني من سمنة واضحة، كيف يخبرني الطبيب أن عندي كبداً دهنياً؟". هنا يأتي دور <strong>الدهون الحشوية</strong> (<bdi>Visceral Fat</bdi>). الدهون في أجسادنا نوعان:</p>
            <ul class="check-list">
                <li><strong>الدهون تحت الجلد (<bdi>Subcutaneous Fat</bdi>):</strong> الدهون اللينة التي يمكنك الإمساك بها بيدك في البطن أو الفخذين، وهي أقل خطراً من الناحية الصحية.</li>
                <li><strong>الدهون الحشوية العميقة (الكرش الصلب):</strong> دهون تختبئ في عمق التجويف البطني وتلتف حول الكبد والبنكرياس والأمعاء. لا تستطيع مسكها باليد، وهي تتصرف كأنها "غدة صماء" نشطة تضخ مواد التهابية وأحماضاً دهنية مباشرة إلى الكبد عبر الوريد البابي.</li>
            </ul>
            <p>لذلك يمكن أن تكون نحيف الذراعين والساقين، لكنك تحمل كبداً دهنياً متعباً بسبب نمط الأكل غير الصحي وقلة الحركة والإجهاد المستمر.</p>

            <h2 class="section-title"><i class="fas fa-stethoscope"></i> <span>2. كيف يخبرك جسدك؟ علامات دهون الكبد الخفية</span></h2>
            <p>الكبد عضو صبور للغاية؛ فنسيجه الداخلي لا يحتوي على أعصاب لنقل الألم، ولهذا يسميه الأطباء "المرض الصامت". هو لا يصرخ متألماً في بداياته، لكنه يرسل إشارات خفيفة يخلط الناس بينها وبين إرهاق الحياة اليومية:</p>
            <h3>أ) الخمول الشديد وضبابية الدماغ بعد الوجبات</h3>
            <p>إذا تناولت غداء فيه خبز أو أرز وشعرت بعده برغبة ملحة في النوم، أو عجزت عن التركيز وشعرت بأن تفكيرك "مغبش"، فقد تكون هذه إشارة إلى <a href="{site:/insulin-resistance.html}">مقاومة الإنسولين</a> وإلى أن كبدك يجهد في معالجة السكر والدهون.</p>
            <h3>ب) ثقل خفيف في الجانب الأيمن العلوي من البطن</h3>
            <p>يقع الكبد تحت القفص الصدري في الجهة اليمنى. عندما يتضخم بسبب تجمع الدهون يضغط على الغشاء الخارجي المحيط به (محفظة غليسون)، فتشعر بثقل أو "انزعاج خفيف" كأن وسادة صغيرة تضغط على خاصرتك اليمنى، خاصة عند الانحناء أو ارتداء ملابس ضيقة.</p>
            <h3>ج) اتساع محيط الخصر وظهور "الكرش الكبدي"</h3>
            <p>تراكم دهون البطن الصلبة علامة واضحة ترافق الكبد الدهني كثيراً. إذا تجاوز محيط خصرك بالشريط المتري <strong>94 سم للرجال أو 80 سم للنساء</strong>، فهذه إشارة إلى زيادة الدهون الحشوية، وتستحق فحص كبدك. يمكنك أيضاً حساب <a href="{site:/whtr-calculator.html}">نسبة الخصر إلى الطول</a> في ثوانٍ.</p>
            <h3>د) العلامات الجلدية وتصبغات الرقبة</h3>
            <p>هل لاحظت زوائد جلدية صغيرة حول الرقبة أو تحت الإبطين؟ أو خطوطاً داكنة كالمخمل خلف رقبتك؟ هذه ليست أوساخاً ولا مشكلة جلدية سطحية؛ إنها ترتبط غالباً بارتفاع الإنسولين في الدم ومقاومته، وهي حالة كثيراً ما ترافق الكبد الدهني.</p>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>3. الفحوصات والتحاليل: كيف تتأكد من صحة كبدك؟</span></h2>
            <figure class="article-figure figure-narrow">
                <img src="/images/visceral-fat-liver-anatomy.webp" alt="رسم تشريحي يوضح الدهون تحت الجلد والدهون الحشوية حول الكبد والأمعاء، مع خلايا كبد محمّلة بقطرات الدهون" width="1024" height="1024" loading="lazy" decoding="async">
                <figcaption>الدهون تحت الجلد مقابل الدهون الحشوية التي تحيط بالأعضاء، وفي الدائرة خلايا كبد محمّلة بقطرات الدهون (التشحم).</figcaption>
            </figure>
            <p>لا داعي للخوف من التحاليل، ففحص الكبد اليوم أصبح سهلاً ودقيقاً:</p>
            <ul class="check-list">
                <li><strong>إنزيمات الكبد في الدم (<bdi>ALT &amp; AST</bdi>):</strong> عندما تلتهب خلايا الكبد بسبب الدهون، تتسرب هذه الإنزيمات إلى الدم. إنزيم <bdi>ALT</bdi> هو المؤشر الأكثر خصوصية للكبد؛ فإذا وجدته مرتفعاً عن حده الطبيعي فهو دليل على أن الدهون بدأت تُحدث التهاباً خفيفاً.</li>
                <li><strong>الموجات فوق الصوتية (السونار):</strong> فحص غير مؤلم يدوم خمس دقائق. يظهر الكبد السليم بلون رمادي داكن، بينما يظهر الكبد الدهني بلون أبيض ساطع عاكس (يسميه الأطباء "الكبد الساطع" <bdi>Bright Liver</bdi>).</li>
                <li><strong>السكر التراكمي (<bdi>HbA1c</bdi>) ومقاومة الإنسولين (<bdi>HOMA-IR</bdi>):</strong> لأن الكبد الدهني ومتلازمة الأيض و<a href="/diabetes/prediabetes.html">مرحلة ما قبل السكري</a> تسير معاً كثيراً، يخبرك السكر التراكمي هل بدأ هذا العبء الدهني يؤثر على تعامل جسمك مع الجلوكوز.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-champagne-glasses"></i> <span>4. الخبر السعيد الذي يستحق الاحتفال: الكبد قادر على التعافي!</span></h2>
            <p>الكبد هو العضو الوحيد في جسم الإنسان الذي يمتلك قدرة استثنائية على تجديد خلاياه ذاتياً (<bdi>Regeneration</bdi>)؛ فلو استُؤصل جزء من كبد سليم جراحياً، ينمو الباقي ويعود إلى حجمه الطبيعي تقريباً.</p>
            <p>ماذا يعني هذا لك؟ يعني أنه بمجرد أن تتوقف عن إغراقه بالسكريات المكررة والدهون المتحولة، وتبدأ باتباع خطة متوازنة، يبدأ الكبد في استخدام الدهون المخزنة فيه وقوداً.</p>
            <div class="rule-cards">
                <div class="rule-card"><div class="rule-num">5%</div><h3>نزول 5% من الوزن</h3><p>يقلل كمية الدهون في الكبد بوضوح.</p></div>
                <div class="rule-card"><div class="rule-num">7–10%</div><h3>نزول 7 إلى 10%</h3><p>يُنهي الالتهاب الدهني عند كثير من المرضى ويعيد الإنزيمات إلى أرقامها الطبيعية في الغالب.</p></div>
                <div class="rule-card"><div class="rule-num">≥ 10%</div><h3>نزول 10% أو أكثر</h3><p>قد يعكس التليف الكبدي المبكر نفسه.</p></div>
            </div>
            <p>وتظهر هذه النتائج عادة خلال شهرين إلى ثلاثة أشهر (12 أسبوعاً) من الالتزام بالغذاء والحركة، وفق الدراسات السريرية وإرشادات الجمعيات الأوروبية للكبد والسكري والسمنة.</p>

            <h2 class="section-title"><i class="fas fa-traffic-light"></i> <span>5. جدول الأكل المسموح والممنوع: قائمة تنظيف دهون الكبد في المطبخ</span></h2>
            <p>صيدليتك الحقيقية موجودة في ثلاجتك. إليك خريطة الأطعمة المدعومة بالأبحاث:</p>
            <div class="tier-title tier-gold"><span class="tier-dot"></span> 🟢 أطعمة "أصدقاء الكبد"</div>
            <ul class="check-list">
                <li><strong><a href="{food:black-coffee}">القهوة السوداء الصافية</a>:</strong> تشير دراسات رصدية كثيرة إلى أن شرب 2 إلى 3 أكواب يومياً (بدون سكر) يرتبط بانخفاض دهون الكبد وبانخفاض خطر تليفه، ويُعزى ذلك إلى مضادات أكسدة مثل حمض الكلوروجينيك.</li>
                <li><strong>الخضار الصليبية (<a href="{food:broccoli}">البروكلي</a>، <a href="{food:cauliflower}">القرنبيط</a>، الملفوف، <a href="{food:arugula-rocket}">الجرجير</a>):</strong> غنية بمركب كبريتي يسمى السولفورافان (<bdi>Sulforaphane</bdi>)، وتشير دراسات إلى أنه ينشط إنزيمات الكبد المسؤولة عن التخلص من السموم.</li>
                <li><strong><a href="{food:extra-virgin-olive-oil}">زيت الزيتون البكر الممتاز</a>:</strong> يحتوي على حمض الأوليك ومضادات أكسدة؛ وتشير دراسات إلى أن ملعقتين يومياً على السلطة، ضمن النمط المتوسطي، تحسن إنزيمات الكبد وحساسية الإنسولين.</li>
                <li><strong>الأسماك الدهنية (<a href="{food:grilled-salmon}">السلمون</a>، <a href="{food:canned-sardines}">السردين</a>، <a href="{food:mackerel}">الماكريل</a>):</strong> مصدر طبيعي لأوميغا 3 (<bdi>EPA/DHA</bdi>) التي تسهم في الحفاظ على المستوى الطبيعي للدهون الثلاثية في الدم.</li>
                <li><strong><a href="{food:artichoke}">الخرشوف (الأرضي شوكي)</a>:</strong> غني بمادة السينارين (<bdi>Cynarin</bdi>) التي يُعتقد أنها تحفز إفراز العصارة الصفراوية وتساعد الكبد على تصريف الدهون.</li>
            </ul>
            <div class="tier-title tier-avoid"><span class="tier-dot"></span> 🔴 أطعمة "أعداء الكبد" (يجب إيقافها فوراً)</div>
            <ul class="check-list">
                <li><strong>المشروبات الغازية وعصائر الفواكه الجاهزة:</strong> حتى لو كُتب عليها "طبيعية 100%"، فإن شرب 30 غراماً من الفركتوز السائل بدون ألياف بمثابة رصاصة مباشرة على خلايا الكبد.</li>
                <li><strong>الدهون المتحولة وزيوت القلي المعاد تسخينها:</strong> السمن الصناعي المهدرج وزيت المقالي المستخدم مراراً يرفعان الالتهاب ويزيدان تراكم الدهون الحشوية.</li>
                <li><strong>المخبوزات والحلويات المصنوعة من الدقيق الأبيض:</strong> يتحول <a href="{food:white-bread}">الخبز الأبيض</a> إلى سكر في دمك أسرع من ملعقة السكر نفسها.</li>
                <li><strong>المقليات والوجبات فائقة التصنيع (<bdi>Ultra-Processed Foods</bdi>):</strong> مثل <a href="{food:french-fries}">البطاطا المقلية</a>؛ تجمع بين الدهون الضارة والملح والنشويات سريعة الامتصاص، وهي التركيبة التي ترهق الكبد أيضياً.</li>
            </ul>
            <h3>📊 المقارنة السريعة: اختر هذا 🟢 بدلاً من هذا 🔴</h3>
            <div class="rule-cards">
                <div class="rule-card"><h3>المشروبات</h3><p>🟢 قهوة سوداء، <a href="{food:green-tea}">شاي أخضر</a>، ماء بليمون<br>🔴 مشروبات غازية، عصائر، مشروبات طاقة</p></div>
                <div class="rule-card"><h3>الدهون والزيوت</h3><p>🟢 زيت زيتون بكر، <a href="{food:avocado}">أفوكادو</a>، دهن الأسماك<br>🔴 دهون متحولة، زيت قلي معاد، سمن نباتي مهدرج</p></div>
                <div class="rule-card"><h3>البروتين</h3><p>🟢 <a href="{food:boiled-egg}">بيض</a>، سمك سلمون، <a href="{food:grilled-chicken-breast}">صدور دجاج</a>، <a href="{food:lentils}">عدس</a><br>🔴 لحوم مصنعة، هوت دوغ، برغر مقلي</p></div>
                <div class="rule-card"><h3>النشويات</h3><p>🟢 <a href="{food:oatmeal}">شوفان حبة كاملة</a>، <a href="{food:quinoa}">كينوا</a>، عدس، <a href="{food:blueberry}">توت</a><br>🔴 خبز أبيض، معجنات، بسكويت، سكر أبيض</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-capsules"></i> <span>6. المكملات الغذائية الداعمة لصحة الكبد (وفق الأبحاث)</span></h2>
            <p>إذا كنت تبحث عن خطوة إضافية بجانب الأكل الصحي، فهذه أكثر المكملات دراسة. استشر طبيبك أو الصيدلي قبل البدء، خاصة إذا كنت تتناول أدوية:</p>
            <ul class="check-list">
                <li><strong><a href="/supplements/milk-thistle.html">شوك الحليب</a> (<bdi>Milk Thistle – Silymarin</bdi>):</strong> نبات بري استُخدم تقليدياً لدعم الكبد منذ قرون. المادة الفعالة فيه (السيليمارين) مضاد أكسدة، وتشير دراسات إلى أنها تحمي خلايا الكبد، لكن الأدلة على البشر ما زالت محدودة.</li>
                <li><strong><a href="/supplements/omega-3-fish-oil.html">أحماض أوميغا 3</a> (<bdi>EPA/DHA</bdi>):</strong> تناول 2 غرام يومياً من <bdi>EPA</bdi> و<bdi>DHA</bdi> يسهم في الحفاظ على المستوى الطبيعي للدهون الثلاثية في الدم، ولا ينبغي تجاوز 5 غرامات يومياً من المكملات.</li>
                <li><strong><a href="/supplements/choline-bitartrate.html">الكولين</a> (<bdi>Choline</bdi>):</strong> يوجد طبيعياً في صفار البيض و<a href="{food:beef-liver}">الكبدة البقرية</a>، ويسهم في استقلاب الدهون الطبيعي وفي الحفاظ على وظائف الكبد الطبيعية؛ فهو يدخل في تصنيع نواقل الدهون (<bdi>VLDL</bdi>) التي تُخرج الدهون من الكبد، ونقصه الشديد يرتبط بتراكم الدهون فيه.</li>
                <li><strong><a href="/supplements/magnesium.html">المغنيسيوم</a> (<bdi>Glycinate / Malate</bdi>):</strong> يسهم في استقلاب الطاقة الطبيعي، ويرتبط انخفاض مستواه في الدراسات بمقاومة الإنسولين.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-calendar-check"></i> <span>7. خطة الـ 12 أسبوعاً العملية لتقليل دهون الكبد والكرش الحشوي</span></h2>
            <p>كيف تطبق هذا الكلام غداً عندما تستيقظ من نومك؟ إليك الخطة السهلة:</p>
            <h3>الأسبوع 1 إلى 4: إيقاف النزيف الأيضي (وقف السكريات والفركتوز)</h3>
            <ol class="steps">
                <li>الامتناع التام عن كل ما يحتوي على سكر مضاف أو شراب الذرة عالي الفركتوز.</li>
                <li>استبدال الخبز الأبيض بخبز الحبة الكاملة أو الشعير أو الحمص.</li>
                <li>شرب كوبين من الماء فور الاستيقاظ، يليهما فنجان قهوة سوداء سادة.</li>
                <li>المشي السريع 20 دقيقة يومياً؛ فالمشي من ألد أعداء الدهون الحشوية.</li>
            </ol>
            <h3>الأسبوع 5 إلى 8: <a href="{site:/intermittent-fasting.html}">الصيام المتقطع</a> الهادئ (14/10 أو 16/8)</h3>
            <ol class="steps">
                <li>اجعل آخر وجبة في الساعة السابعة مساءً، وأول وجبة في العاشرة أو الحادية عشرة صباح اليوم التالي.</li>
                <li>خلال ساعات الصيام ينفد مخزون الجليكوجين من الكبد، فيضطر إلى حرق دهونه الداخلية لإنتاج الطاقة.</li>
                <li>ركّز على وجبات عالية البروتين والألياف لضمان الشبع ومنع هبوط السكر المفاجئ.</li>
            </ol>
            <div class="tip"><h3>⚠️ تنبيه قبل الصيام</h3><p>إذا كنت تتناول أدوية السكري (خاصة الإنسولين أو أدوية السلفونيل يوريا)، أو كنتِ حاملاً أو مرضعاً، أو لديك تاريخ مع اضطرابات الأكل، فلا تبدأ الصيام المتقطع قبل استشارة طبيبك؛ فقد يلزم تعديل الجرعات لتجنب هبوط السكر.</p></div>
            <h3>الأسبوع 9 إلى 12: حصد الثمار وإعادة الفحص</h3>
            <ol class="steps">
                <li>يلاحظ كثيرون انخفاض محيط الخصر بين 4 و8 سم.</li>
                <li>يتراجع شعور الخمول بعد الأكل بوضوح، وتشعر بخفة في الحركة.</li>
                <li>كرر فحص إنزيمات الكبد (<bdi>ALT/AST</bdi>) والسونار مع طبيبك، وقد تفاجأ أنت وطبيبك بالنتيجة الجديدة.</li>
            </ol>

            <div class="boodi-card">
                <div>
                    <h2>8. كيف سيساعدك تطبيق بودي (Boodi) في هذه الرحلة؟ (قريباً)</h2>
                    <p>تقليل دهون الكبد يحتاج إلى حساب دقيق لعجز السعرات (نحو 500 سعرة يومياً) دون أن تشعر بالحرمان أو تنهار طاقتك. في تطبيق بودي صممنا برنامج الدايت المتوازن وفق معادلة <bdi>Mifflin-St Jeor</bdi> المعتمدة، مع الفحص الفوري للباركود:</p>
                    <ul class="check-list">
                        <li><strong>فاحص المكونات والتفضيلات:</strong> يخبرك فوراً إذا كان المنتج يحتوي على دهون مهدرجة أو سكريات خفية.</li>
                        <li><strong>شجرة البدائل:</strong> إن كنت تحب الأرز أو الخبز أو المعكرونة، يقترح عليك بودي بدائل لا ترفع سكر الدم بسرعة.</li>
                        <li><strong>مطبخ مفتوح من كل مطابخ العالم:</strong> يتيح لك تطبيق خطة الـ 12 أسبوعاً بأكلاتك المحببة دون فرض نمط غربي جاف.</li>
                    </ul>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> تعرّف على Boodi</a>
            </div>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>9. الأسئلة الأكثر بحثاً حول الكبد الدهني</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>هل شرب خل التفاح يذيب دهون الكبد؟</h3><p>خل التفاح الطبيعي (ملعقة صغيرة مخففة في كوب ماء كبير قبل الوجبة) قد يحسن حساسية الإنسولين ويقلل الارتفاع الحاد في السكر بعد الأكل، مما يخفف العبء على الكبد، لكنه ليس حلاً سحرياً بمفرده دون تعديل جودة طعامك.</p></div>
                <div class="faq-item"><h3>كم من الوقت يحتاج الكبد ليتخلص من الدهون؟</h3><p>تبدأ دهون الكبد بالانخفاض خلال أسبوعين تقريباً من قطع السكريات، وتصل النتائج إلى ذروتها بعد 8 إلى 12 أسبوعاً من الالتزام بنظام غذائي منضبط ونشاط بدني منتظم.</p></div>
                <div class="faq-item"><h3>هل الفواكه ممنوعة تماماً لمن يعانون من الكبد الدهني؟</h3><p>لا. الفاكهة الكاملة تحتوي على ألياف وفيتامينات وماء تبطئ امتصاص السكر. المسموح حبة إلى حبتين يومياً من الفواكه منخفضة السكر (مثل التوت و<a href="{food:strawberry}">الفراولة</a> و<a href="{food:apple}">التفاح الأخضر</a> و<a href="{food:kiwi}">الكيوي</a>). أما الممنوع فهو عصير الفواكه، لأنه يجرد الفاكهة من أليافها ويضخ كمية فركتوز مركزة تتجه فوراً إلى الكبد.</p></div>
                <div class="faq-item"><h3>هل الكبد الدهني خطير، وهل يسبب السرطان؟</h3><p>الكبد الدهني في مراحله الأولى قابل للتراجع في أغلب الحالات. الخطورة تحدث إذا أُهمل لسنوات طويلة مع استمرار التدخين والسكري غير المنضبط، فقد يتطور إلى التهاب كبدي دهني (<bdi>MASH</bdi>، المعروف سابقاً بـ <bdi>NASH</bdi>) ثم إلى تليف، ونادراً إلى سرطان الكبد. لهذا فإن اكتشافه اليوم والبدء في التعامل معه الآن هو أعظم هدية تقدمها لجسدك ومستقبلك.</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-flag-checkered"></i> <span>خاتمة: ابدأ اليوم.. كبدك ينتظر خطوتك الأولى</span></h2>
            <p>لست بحاجة إلى تغيير حياتك بالكامل في يوم واحد. ابدأ اليوم بقرار بسيط: استبدل المشروب الغازي بكوب ماء بارد مع شريحة ليمون، وامشِ 20 دقيقة في الهواء الطلق، واستمتع بفنجان قهوتك الصباحية بدون سكر، وتابع إطلاق تطبيق بودي قريباً ليرافقك خطوة بخطوة.</p>
            <p>صحتك أغلى ما تملك، وكبدك يستحق أن تمنحه فرصة ليتنفس ويعود نقياً كما كان.</p>'''),
en=dict(
 byline='By Dr. Wassim Habib',
 title='Fatty Liver: Symptoms, Causes & The Good News in This Complete Guide',
 h1='Fatty Liver: Symptoms, Causes & The Good News in This Complete Guide',
 crumb='Fatty liver and visceral fat',
 cat='Liver & Metabolic Health',
 desc='Fatty liver symptoms and their real causes, why slim people get it too, the tests that find it, liver-friendly and liver-unfriendly foods, and a practical 12-week plan to reduce liver fat and visceral belly fat.',
 summary='Why fat builds up in the liver even in slim people, how tests detect it, and a 12-week food and movement plan to reduce liver fat and visceral belly fat.',
 hero_alt='A woman with her hand on her stomach in a bright kitchen, illustrating the symptoms of fatty liver and visceral fat',
 about=['Fatty liver disease', 'MASLD', 'Visceral fat', 'Insulin resistance'],
 disclaimer='⚖️ Medical disclaimer: this article is health education and lifestyle guidance from WiBo Health. It is not a medical diagnosis and does not replace advice from your doctor. Talk to your doctor before starting intermittent fasting or any food supplement, especially if you take medication or are pregnant or breastfeeding.',
 body='''            <h2 class="section-title"><i class="fas fa-heart"></i> <span>From the heart: a message to anyone who feels tired for no clear reason</span></h2>
            <p class="lead">If you wake up after eight hours of sleep feeling as if you haven't slept a minute, if your waist has slowly been getting wider and you now have a "hard belly" that won't shift however little you eat, or if a routine blood test ended with your doctor calmly saying, "Your results are fine, but there's a little fat on your liver", then this guide was written for you.</p>
            <p>The first thing I want you to know and take to heart, as a doctor talking to a friend: <strong>don't worry, you are not alone, and above all your liver can recover; in the early stages its fat can disappear completely within a few weeks to a few months.</strong></p>
            <p>Fatty liver is not a life sentence, and the visceral fat hiding behind your abdominal muscles is not your destiny. In this article we'll set the complicated medical terms aside and talk in everyday language: what is quietly happening inside your body? Why do even slim people get it? And what simple daily plan reduces this fat and gives you back your clear head, your energy and your lightness?</p>

            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>1. What are fatty liver and visceral belly fat? (And why do slim people get them too?)</span></h2>
            <p>Imagine your body is a well-kept house and the liver is its "central kitchen and filtering station". Its main jobs are turning food into energy, storing a small reserve of nutrients and cleaning your blood around the clock.</p>
            <p>Normally the liver contains very little fat (less than 5% of its weight). When the fat stored in it goes above 5%, we call it <strong>fatty liver</strong>, and in particular the type linked to metabolic syndrome and too much sugar and starch, whose modern scientific name is <bdi>MASLD</bdi>.</p>
            <h3>The myth that "fat comes from eating fat"</h3>
            <p>The biggest myth is that eating meat fat or oil is what causes liver fat. Clinically, the number one enemy of a fatty liver is <strong>sugar and refined starch, especially fructose</strong>.</p>
            <p>When you drink a soft drink or a sweetened juice, or eat a fast-food meal full of white flour, your body absorbs these sugars very quickly. Your muscles can't take up all that energy, so the liver has to turn the surplus sugar into triglycerides in a fast internal process.</p>
            <h3>The puzzle of the "slim person with a fatty liver" (<bdi>TOFI</bdi>)</h3>
            <p>Many people say, "Doctor, I weigh 65 kg and I'm not visibly overweight. How can I have a fatty liver?" This is where <strong>visceral fat</strong> comes in. The fat in our bodies comes in two kinds:</p>
            <ul class="check-list">
                <li><strong>Subcutaneous fat:</strong> the soft fat you can pinch on your belly or thighs. From a health point of view it is the less harmful kind.</li>
                <li><strong>Deep visceral fat (the hard belly):</strong> fat hidden deep in the abdominal cavity, wrapped around the liver, pancreas and intestines. You can't pinch it, and it behaves like an active "endocrine gland", sending inflammatory substances and fatty acids straight to the liver through the portal vein.</li>
            </ul>
            <p>So you can have slim arms and legs and still carry a tired, fatty liver because of unhealthy eating habits, too little movement and constant stress.</p>

            <h2 class="section-title"><i class="fas fa-stethoscope"></i> <span>2. How does your body tell you? The hidden signs of liver fat</span></h2>
            <p>The liver is a very patient organ: its inner tissue has no nerves that carry pain, which is why doctors call fatty liver a "silent disease". It doesn't cry out in the early stages, but it sends quiet signals that people mistake for the tiredness of everyday life:</p>
            <h3>a) Heavy tiredness and brain fog after meals</h3>
            <p>If a lunch with bread or rice leaves you desperate for a nap, or you can't concentrate and your thinking feels "foggy", this may be a sign of <a href="{site:/insulin-resistance.html}">insulin resistance</a> and of a liver struggling to process sugar and fat.</p>
            <h3>b) A mild heaviness in the upper right of the abdomen</h3>
            <p>The liver sits under the ribs on the right. When it swells with fat, it presses on the membrane around it (Glisson's capsule), and you may feel a heaviness or "mild discomfort", as if a small cushion were pressing on your right side, especially when you bend over or wear tight clothes.</p>
            <h3>c) A growing waist and a "liver belly"</h3>
            <p>A build-up of hard belly fat often goes hand in hand with fatty liver. If your waist measures more than <strong>94 cm for men or 80 cm for women</strong>, that points to extra visceral fat and is worth a liver check. You can also work out your <a href="{site:/whtr-calculator.html}">waist-to-height ratio</a> in seconds.</p>
            <h3>d) Skin signs and darker patches on the neck</h3>
            <p>Have you noticed small skin tags around your neck or under your arms, or dark, velvety lines on the back of your neck? This isn't dirt or a surface skin problem; these signs are often linked to high insulin levels and insulin resistance, a condition that frequently goes with fatty liver.</p>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>3. Tests: how can you check your liver?</span></h2>
            <figure class="article-figure figure-narrow">
                <img src="/images/visceral-fat-liver-anatomy.webp" alt="Anatomical illustration of subcutaneous fat and visceral fat around the liver and intestines, with liver cells filled with fat droplets" width="1024" height="1024" loading="lazy" decoding="async">
                <figcaption>Subcutaneous fat versus the visceral fat around the organs; in the circle, liver cells filled with fat droplets (steatosis).</figcaption>
            </figure>
            <p>There's no need to be afraid of the tests; checking the liver is easy and accurate today:</p>
            <ul class="check-list">
                <li><strong>Liver enzymes in the blood (<bdi>ALT &amp; AST</bdi>):</strong> when liver cells become inflamed by fat, these enzymes leak into the blood. <bdi>ALT</bdi> is the most liver-specific marker; if it is above the normal range, the fat has started to cause mild inflammation.</li>
                <li><strong>Ultrasound:</strong> a painless five-minute scan. A healthy liver looks dark grey, while a fatty liver looks bright white and reflective (doctors call it a "bright liver").</li>
                <li><strong>HbA1c and insulin resistance (<bdi>HOMA-IR</bdi>):</strong> fatty liver, metabolic syndrome and <a href="/en/diabetes/prediabetes.html">prediabetes</a> often go together, so your HbA1c shows whether this fat load has started to affect how your body handles glucose.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-champagne-glasses"></i> <span>4. The good news worth celebrating: your liver can recover!</span></h2>
            <p>The liver is the only organ in the human body with an exceptional ability to regenerate its own cells: if part of a healthy liver is removed in surgery, the rest grows back to almost its normal size.</p>
            <p>What does that mean for you? As soon as you stop flooding it with refined sugar and trans fats and start a balanced plan, the liver begins to use its stored fat as fuel.</p>
            <div class="rule-cards">
                <div class="rule-card"><div class="rule-num">5%</div><h3>Losing 5% of your weight</h3><p>Clearly reduces the amount of fat in the liver.</p></div>
                <div class="rule-card"><div class="rule-num">7–10%</div><h3>Losing 7 to 10%</h3><p>Resolves fatty inflammation in many patients and usually brings liver enzymes back to normal.</p></div>
                <div class="rule-card"><div class="rule-num">≥ 10%</div><h3>Losing 10% or more</h3><p>Can even reverse early liver fibrosis.</p></div>
            </div>
            <p>These results usually appear within two to three months (12 weeks) of sticking to better food and more movement, according to clinical studies and the guidelines of the European liver, diabetes and obesity societies.</p>

            <h2 class="section-title"><i class="fas fa-traffic-light"></i> <span>5. Foods to choose and foods to avoid: your kitchen plan for a cleaner liver</span></h2>
            <p>Your real pharmacy is in your fridge. Here is a map of the foods backed by research:</p>
            <div class="tier-title tier-gold"><span class="tier-dot"></span> 🟢 "Liver-friendly" foods</div>
            <ul class="check-list">
                <li><strong><a href="{food:black-coffee}">Plain black coffee</a>:</strong> many observational studies suggest that 2 to 3 cups a day (without sugar) are linked to less liver fat and a lower risk of liver fibrosis, thanks to antioxidants such as chlorogenic acid.</li>
                <li><strong>Cruciferous vegetables (<a href="{food:broccoli}">broccoli</a>, <a href="{food:cauliflower}">cauliflower</a>, cabbage, <a href="{food:arugula-rocket}">rocket</a>):</strong> rich in a sulphur compound called sulforaphane, which studies suggest activates the liver enzymes that clear toxins.</li>
                <li><strong><a href="{food:extra-virgin-olive-oil}">Extra virgin olive oil</a>:</strong> contains oleic acid and antioxidants; studies suggest that two tablespoons a day on salads, as part of a Mediterranean diet, improve liver enzymes and insulin sensitivity.</li>
                <li><strong>Oily fish (<a href="{food:grilled-salmon}">salmon</a>, <a href="{food:canned-sardines}">sardines</a>, <a href="{food:mackerel}">mackerel</a>):</strong> a natural source of omega-3 (<bdi>EPA/DHA</bdi>), which contributes to the maintenance of normal blood triglyceride levels.</li>
                <li><strong><a href="{food:artichoke}">Artichoke</a>:</strong> rich in cynarin, which is thought to stimulate bile flow and help the liver clear fat.</li>
            </ul>
            <div class="tier-title tier-avoid"><span class="tier-dot"></span> 🔴 "Liver-unfriendly" foods (stop these now)</div>
            <ul class="check-list">
                <li><strong>Soft drinks and ready-made fruit juices:</strong> even when the label says "100% natural", drinking 30 g of liquid fructose without fibre is like firing a bullet straight at your liver cells.</li>
                <li><strong>Trans fats and reused frying oil:</strong> hydrogenated margarine and frying oil used over and over raise inflammation and add to visceral fat.</li>
                <li><strong>Baked goods and sweets made with white flour:</strong> <a href="{food:white-bread}">white bread</a> turns into sugar in your blood faster than a spoonful of sugar itself.</li>
                <li><strong>Fried and ultra-processed foods:</strong> such as <a href="{food:french-fries}">French fries</a>; they combine harmful fats, salt and fast-absorbed starch, the mix that strains the liver's metabolism.</li>
            </ul>
            <h3>📊 Quick comparison: choose this 🟢 instead of this 🔴</h3>
            <div class="rule-cards">
                <div class="rule-card"><h3>Drinks</h3><p>🟢 Black coffee, <a href="{food:green-tea}">green tea</a>, water with lemon<br>🔴 Soft drinks, juices, energy drinks</p></div>
                <div class="rule-card"><h3>Fats and oils</h3><p>🟢 Extra virgin olive oil, <a href="{food:avocado}">avocado</a>, oily fish<br>🔴 Trans fats, reused frying oil, hydrogenated margarine</p></div>
                <div class="rule-card"><h3>Protein</h3><p>🟢 <a href="{food:boiled-egg}">Eggs</a>, salmon, <a href="{food:grilled-chicken-breast}">chicken breast</a>, <a href="{food:lentils}">lentils</a><br>🔴 Processed meat, hot dogs, fried burgers</p></div>
                <div class="rule-card"><h3>Starches</h3><p>🟢 <a href="{food:oatmeal}">Whole-grain oats</a>, <a href="{food:quinoa}">quinoa</a>, lentils, <a href="{food:blueberry}">berries</a><br>🔴 White bread, pastries, biscuits, white sugar</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-capsules"></i> <span>6. Food supplements that support liver health (according to research)</span></h2>
            <p>If you want an extra step alongside healthy eating, these are the most studied supplements. Talk to your doctor or pharmacist first, especially if you take medication:</p>
            <ul class="check-list">
                <li><strong><a href="/en/supplements/milk-thistle.html">Milk thistle</a> (silymarin):</strong> a wild plant used traditionally for the liver for centuries. Its active substance, silymarin, is an antioxidant, and studies suggest it protects liver cells, although the evidence in people is still limited.</li>
                <li><strong><a href="/en/supplements/omega-3-fish-oil.html">Omega-3 fatty acids</a> (<bdi>EPA/DHA</bdi>):</strong> 2 g of EPA and DHA a day contributes to the maintenance of normal blood triglyceride levels; supplements should not exceed 5 g a day.</li>
                <li><strong><a href="/en/supplements/choline-bitartrate.html">Choline</a>:</strong> found naturally in egg yolk and <a href="{food:beef-liver}">beef liver</a>, it contributes to normal lipid metabolism and to the maintenance of normal liver function; it is needed to make the fat carriers (<bdi>VLDL</bdi>) that move fat out of the liver, and a severe shortage is linked to fat building up there.</li>
                <li><strong><a href="/en/supplements/magnesium.html">Magnesium</a> (glycinate / malate):</strong> contributes to normal energy-yielding metabolism, and studies link low magnesium levels to insulin resistance.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-calendar-check"></i> <span>7. The practical 12-week plan to reduce liver fat and visceral belly fat</span></h2>
            <p>How do you put all this into practice tomorrow morning? Here is the easy plan:</p>
            <h3>Weeks 1 to 4: stop the metabolic leak (cut sugar and fructose)</h3>
            <ol class="steps">
                <li>Cut out everything with added sugar or high-fructose corn syrup.</li>
                <li>Swap white bread for whole-grain, barley or chickpea bread.</li>
                <li>Drink two glasses of water as soon as you wake up, followed by a cup of plain black coffee.</li>
                <li>Walk briskly for 20 minutes a day; walking is one of visceral fat's worst enemies.</li>
            </ol>
            <h3>Weeks 5 to 8: gentle <a href="{site:/intermittent-fasting.html}">intermittent fasting</a> (14/10 or 16/8)</h3>
            <ol class="steps">
                <li>Have your last meal at 7 pm and your first meal at 10 or 11 am the next day.</li>
                <li>During the fasting hours the liver's glycogen store runs out, so it has to burn its own fat for energy.</li>
                <li>Focus on meals high in protein and fibre to stay full and avoid sudden blood sugar dips.</li>
            </ol>
            <div class="tip"><h3>⚠️ Before you fast</h3><p>If you take diabetes medication (especially insulin or sulfonylureas), are pregnant or breastfeeding, or have a history of eating disorders, don't start intermittent fasting before talking to your doctor; your doses may need adjusting to avoid low blood sugar.</p></div>
            <h3>Weeks 9 to 12: reap the rewards and retest</h3>
            <ol class="steps">
                <li>Many people notice their waist shrinking by 4 to 8 cm.</li>
                <li>The after-meal tiredness clearly fades and you feel lighter on your feet.</li>
                <li>Repeat your liver enzymes (<bdi>ALT/AST</bdi>) and ultrasound with your doctor; you and your doctor may be pleasantly surprised by the new result.</li>
            </ol>

            <div class="boodi-card">
                <div>
                    <h2>8. How will the Boodi app help you on this journey? (Coming soon)</h2>
                    <p>Reducing liver fat takes an accurate calorie deficit (about 500 kcal a day) without feeling deprived or running out of energy. In the Boodi app we built a balanced diet programme on the established <bdi>Mifflin-St Jeor</bdi> equation, together with instant barcode scanning:</p>
                    <ul class="check-list">
                        <li><strong>Ingredient and preference scanner:</strong> tells you straight away whether a product contains hydrogenated fats or hidden sugars.</li>
                        <li><strong>Swap tree:</strong> if you love rice, bread or pasta, Boodi suggests alternatives that don't raise your blood sugar quickly.</li>
                        <li><strong>An open kitchen with all the world's cuisines:</strong> follow the 12-week plan with the dishes you love, without a dry Western diet forced on you.</li>
                    </ul>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> Discover Boodi</a>
            </div>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>9. The most searched questions about fatty liver</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Does apple cider vinegar melt liver fat?</h3><p>Natural apple cider vinegar (a teaspoon diluted in a large glass of water before a meal) may improve insulin sensitivity and soften the sharp rise in blood sugar after eating, which eases the load on the liver. On its own, without improving what you eat, it is not a magic solution.</p></div>
                <div class="faq-item"><h3>How long does it take the liver to get rid of fat?</h3><p>Liver fat starts to fall within about two weeks of cutting out sugar, and the results peak after 8 to 12 weeks of a disciplined diet and regular physical activity.</p></div>
                <div class="faq-item"><h3>Is fruit completely off limits with a fatty liver?</h3><p>No. Whole fruit contains fibre, vitamins and water that slow down sugar absorption. One or two pieces a day of low-sugar fruit (such as berries, <a href="{food:strawberry}">strawberries</a>, <a href="{food:apple}">green apples</a> and <a href="{food:kiwi}">kiwi</a>) are fine. Fruit juice is what to avoid, because it strips the fruit of its fibre and delivers a concentrated dose of fructose that goes straight to the liver.</p></div>
                <div class="faq-item"><h3>Is fatty liver dangerous, and can it cause cancer?</h3><p>In its early stages, fatty liver can be reversed in most cases. The danger comes when it is ignored for many years alongside smoking and poorly controlled diabetes: it can progress to fatty liver inflammation (<bdi>MASH</bdi>, formerly <bdi>NASH</bdi>), then to fibrosis and, rarely, to liver cancer. That is why finding it today and starting to deal with it now is the greatest gift you can give your body and your future.</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-flag-checkered"></i> <span>Conclusion: start today, your liver is waiting for your first step</span></h2>
            <p>You don't need to change your whole life in one day. Start today with one simple decision: swap the soft drink for a glass of cold water with a slice of lemon, walk for 20 minutes outdoors, enjoy your morning coffee without sugar, and keep an eye out for the launch of the Boodi app, coming soon to guide you step by step.</p>
            <p>Your health is the most precious thing you have, and your liver deserves the chance to breathe and become clean again.</p>'''),
nl=dict(
 byline='Door Dr. Wassim Habib',
 title='Leververvetting: Symptomen, oorzaken en het goede nieuws in deze complete gids',
 h1='Leververvetting: Symptomen, oorzaken en het goede nieuws in deze complete gids',
 crumb='Leververvetting en visceraal vet',
 cat='Lever & metabole gezondheid',
 desc='Symptomen van leververvetting en de echte oorzaken, waarom ook slanke mensen het krijgen, welke onderzoeken het aantonen, levervriendelijke en leveronvriendelijke voeding, en een praktisch 12-wekenplan tegen leververvetting en visceraal buikvet.',
 summary='Waarom vet zich ook bij slanke mensen in de lever ophoopt, hoe onderzoek het aantoont, en een 12-wekenplan met voeding en beweging tegen leververvetting en visceraal buikvet.',
 hero_alt='Een vrouw met haar hand op haar buik in een lichte keuken, als beeld voor de symptomen van leververvetting en visceraal vet',
 about=['Fatty liver disease', 'MASLD', 'Visceral fat', 'Insulin resistance'],
 disclaimer='⚖️ Medische disclaimer: dit artikel is gezondheidsvoorlichting en leefstijladvies van WiBo Health. Het is geen medische diagnose en vervangt geen advies van je arts. Overleg met je arts voordat je met intermittent fasting of een voedingssupplement begint, vooral als je medicijnen gebruikt of zwanger bent of borstvoeding geeft.',
 body='''            <h2 class="section-title"><i class="fas fa-heart"></i> <span>Uit het hart: een boodschap voor iedereen die zich moe voelt zonder duidelijke reden</span></h2>
            <p class="lead">Word je na acht uur slaap wakker alsof je geen minuut hebt geslapen? Wordt je taille langzaam breder en heb je een "harde buik" die niet verdwijnt, hoe weinig je ook eet? Of zei je arts na een routinebloedonderzoek rustig: "Je uitslagen zijn goed, maar er zit wat vet op je lever"? Dan is deze gids speciaal voor jou geschreven.</p>
            <p>Het eerste wat ik wil dat je weet en ter harte neemt, als een arts die met een vriend praat: <strong>maak je geen zorgen, je staat er niet alleen voor, en bovenal: je lever kan herstellen. In de vroege fase kan het levervet binnen enkele weken tot een paar maanden helemaal verdwijnen.</strong></p>
            <p>Leververvetting is geen levenslang vonnis, en het viscerale vet dat zich achter je buikspieren verstopt is geen lot. In dit artikel laten we de ingewikkelde medische termen even rusten en praten we in gewone taal: wat gebeurt er stilletjes in je lichaam? Waarom krijgen zelfs slanke mensen het? En welk eenvoudig dagelijks plan vermindert dit vet en geeft je je heldere hoofd, je energie en je lichtheid terug?</p>

            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>1. Wat zijn leververvetting en visceraal buikvet eigenlijk? (En waarom krijgen ook slanke mensen het?)</span></h2>
            <p>Stel je je lichaam voor als een goed onderhouden huis, met de lever als "centrale keuken en zuiveringsstation". De belangrijkste taken van de lever zijn voedsel omzetten in energie, een kleine voorraad voedingsstoffen opslaan en je bloed dag en nacht zuiveren.</p>
            <p>Normaal bevat de lever heel weinig vet (minder dan 5% van zijn gewicht). Komt het opgeslagen vet boven de 5%, dan spreken we van <strong>leververvetting</strong>, en dan vooral de vorm die samenhangt met het metabool syndroom en te veel suiker en zetmeel. De moderne wetenschappelijke naam is <bdi>MASLD</bdi>.</p>
            <h3>De mythe dat "vet van vet eten komt"</h3>
            <p>De grootste mythe is dat vet vlees of olie de oorzaak van levervet is. Klinisch gezien is de grootste vijand van een vervette lever <strong>suiker en geraffineerd zetmeel, vooral fructose</strong>.</p>
            <p>Drink je frisdrank of gezoet sap, of eet je fastfood vol witte bloem, dan neemt je lichaam deze suikers razendsnel op. Je spieren kunnen al die energie niet kwijt, dus moet de lever de overtollige suiker in een snel intern proces omzetten in triglyceriden.</p>
            <h3>Het raadsel van de "slanke persoon met een vervette lever" (<bdi>TOFI</bdi>)</h3>
            <p>Veel mensen zeggen: "Dokter, ik weeg 65 kilo en heb geen zichtbaar overgewicht. Hoe kan ik dan een vervette lever hebben?" Hier speelt <strong>visceraal vet</strong> een rol. Het vet in ons lichaam is er in twee soorten:</p>
            <ul class="check-list">
                <li><strong>Onderhuids vet (subcutaan vet):</strong> het zachte vet dat je op je buik of dijen kunt vastpakken. Voor de gezondheid is dit de minder schadelijke soort.</li>
                <li><strong>Diep visceraal vet (de harde buik):</strong> vet diep in de buikholte, rond de lever, de alvleesklier en de darmen. Je kunt het niet vastpakken, en het gedraagt zich als een actieve "hormoonklier" die ontstekingsstoffen en vetzuren via de poortader rechtstreeks naar de lever stuurt.</li>
            </ul>
            <p>Je kunt dus slanke armen en benen hebben en toch een vermoeide, vervette lever, door ongezonde eetgewoonten, te weinig beweging en aanhoudende stress.</p>

            <h2 class="section-title"><i class="fas fa-stethoscope"></i> <span>2. Hoe vertelt je lichaam het je? De verborgen signalen van levervet</span></h2>
            <p>De lever is een heel geduldig orgaan: het weefsel zelf heeft geen zenuwen die pijn doorgeven. Daarom noemen artsen leververvetting een "stille ziekte". In het begin schreeuwt de lever het niet uit, maar hij geeft zachte signalen die mensen verwarren met de vermoeidheid van het dagelijks leven:</p>
            <h3>a) Zware vermoeidheid en een wazig hoofd na de maaltijd</h3>
            <p>Als je na een lunch met brood of rijst bijna in slaap valt, of je niet kunt concentreren en je denken "mistig" voelt, kan dat een teken zijn van <a href="{site:/insulin-resistance.html}">insulineresistentie</a> en van een lever die moeite heeft met het verwerken van suiker en vet.</p>
            <h3>b) Een licht zwaar gevoel rechtsboven in de buik</h3>
            <p>De lever ligt rechts onder de ribben. Zwelt hij op door vet, dan drukt hij op het vlies eromheen (het kapsel van Glisson). Je kunt dan een zwaar gevoel of "licht ongemak" voelen, alsof er een klein kussen tegen je rechterzij drukt, vooral bij bukken of in strakke kleding.</p>
            <h3>c) Een groeiende taille en een "leverbuik"</h3>
            <p>Een ophoping van hard buikvet gaat vaak samen met leververvetting. Is je middelomtrek meer dan <strong>94 cm bij mannen of 80 cm bij vrouwen</strong>, dan wijst dat op extra visceraal vet en is een levercontrole de moeite waard. Je kunt ook in een paar seconden je <a href="{site:/whtr-calculator.html}">taille-lengteverhouding</a> berekenen.</p>
            <h3>d) Huidsignalen en donkere plekken in de nek</h3>
            <p>Zie je kleine huidaanhangsels rond je nek of onder je oksels, of donkere, fluweelachtige lijnen achter in je nek? Dat is geen vuil en geen oppervlakkig huidprobleem; deze signalen hangen vaak samen met een hoge insulinespiegel en insulineresistentie, een toestand die vaak samengaat met leververvetting.</p>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>3. Onderzoeken: hoe controleer je je lever?</span></h2>
            <figure class="article-figure figure-narrow">
                <img src="/images/visceral-fat-liver-anatomy.webp" alt="Anatomische illustratie van onderhuids vet en visceraal vet rond de lever en darmen, met levercellen vol vetdruppels" width="1024" height="1024" loading="lazy" decoding="async">
                <figcaption>Onderhuids vet tegenover het viscerale vet rond de organen; in de cirkel levercellen vol vetdruppels (steatose).</figcaption>
            </figure>
            <p>Je hoeft niet bang te zijn voor de onderzoeken; de lever controleren is tegenwoordig eenvoudig en nauwkeurig:</p>
            <ul class="check-list">
                <li><strong>Leverenzymen in het bloed (<bdi>ALAT &amp; ASAT</bdi>):</strong> raken levercellen ontstoken door vet, dan lekken deze enzymen naar het bloed. <bdi>ALAT</bdi> is de meest leverspecifieke waarde; ligt die boven de normaalwaarde, dan is het vet een lichte ontsteking gaan veroorzaken.</li>
                <li><strong>Echografie:</strong> een pijnloze scan van vijf minuten. Een gezonde lever ziet er donkergrijs uit, een vervette lever helder wit en reflecterend (artsen spreken van een "heldere lever").</li>
                <li><strong>HbA1c en insulineresistentie (<bdi>HOMA-IR</bdi>):</strong> leververvetting, het metabool syndroom en <a href="/nl/diabetes/prediabetes.html">prediabetes</a> gaan vaak samen. Je HbA1c laat zien of deze vetlast invloed begint te krijgen op hoe je lichaam met glucose omgaat.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-champagne-glasses"></i> <span>4. Het goede nieuws om te vieren: je lever kan herstellen!</span></h2>
            <p>De lever is het enige orgaan in het menselijk lichaam met een uitzonderlijk vermogen om zijn eigen cellen te vernieuwen: wordt een deel van een gezonde lever operatief verwijderd, dan groeit de rest weer tot bijna de normale grootte.</p>
            <p>Wat betekent dat voor jou? Zodra je de lever niet langer overspoelt met geraffineerde suiker en transvetten en met een evenwichtig plan begint, gaat de lever zijn opgeslagen vet als brandstof gebruiken.</p>
            <div class="rule-cards">
                <div class="rule-card"><div class="rule-num">5%</div><h3>5% gewichtsverlies</h3><p>Vermindert de hoeveelheid vet in de lever duidelijk.</p></div>
                <div class="rule-card"><div class="rule-num">7–10%</div><h3>7 tot 10% gewichtsverlies</h3><p>Laat de vettige ontsteking bij veel patiënten verdwijnen en brengt de leverenzymen meestal weer op een normaal niveau.</p></div>
                <div class="rule-card"><div class="rule-num">≥ 10%</div><h3>10% of meer gewichtsverlies</h3><p>Kan zelfs beginnende leverfibrose terugdraaien.</p></div>
            </div>
            <p>Volgens klinische studies en de richtlijnen van de Europese verenigingen voor lever, diabetes en obesitas zie je deze resultaten meestal binnen twee tot drie maanden (12 weken) als je je houdt aan betere voeding en meer beweging.</p>

            <h2 class="section-title"><i class="fas fa-traffic-light"></i> <span>5. Wat je wel en niet eet: je keukenplan voor een schonere lever</span></h2>
            <p>Je echte apotheek staat in je koelkast. Hier is een overzicht van voedingsmiddelen die door onderzoek worden ondersteund:</p>
            <div class="tier-title tier-gold"><span class="tier-dot"></span> 🟢 "Levervriendelijke" voeding</div>
            <ul class="check-list">
                <li><strong><a href="{food:black-coffee}">Zwarte koffie zonder toevoegingen</a>:</strong> veel observationele studies wijzen erop dat 2 tot 3 koppen per dag (zonder suiker) samenhangen met minder levervet en een lager risico op leverfibrose, dankzij antioxidanten zoals chlorogeenzuur.</li>
                <li><strong>Koolsoorten (<a href="{food:broccoli}">broccoli</a>, <a href="{food:cauliflower}">bloemkool</a>, kool, <a href="{food:arugula-rocket}">rucola</a>):</strong> rijk aan de zwavelverbinding sulforafaan, die volgens studies de leverenzymen activeert die afvalstoffen opruimen.</li>
                <li><strong><a href="{food:extra-virgin-olive-oil}">Extra vierge olijfolie</a>:</strong> bevat oliezuur en antioxidanten; studies wijzen erop dat twee eetlepels per dag over de salade, als onderdeel van een mediterraan eetpatroon, de leverenzymen en de insulinegevoeligheid verbeteren.</li>
                <li><strong>Vette vis (<a href="{food:grilled-salmon}">zalm</a>, <a href="{food:canned-sardines}">sardines</a>, <a href="{food:mackerel}">makreel</a>):</strong> een natuurlijke bron van omega-3 (<bdi>EPA/DHA</bdi>), die bijdraagt tot de handhaving van een normaal triglyceridengehalte in het bloed.</li>
                <li><strong><a href="{food:artichoke}">Artisjok</a>:</strong> rijk aan cynarine, waarvan men denkt dat het de galafvoer stimuleert en de lever helpt vet af te voeren.</li>
            </ul>
            <div class="tier-title tier-avoid"><span class="tier-dot"></span> 🔴 "Leveronvriendelijke" voeding (stop hier nu mee)</div>
            <ul class="check-list">
                <li><strong>Frisdrank en kant-en-klare vruchtensappen:</strong> ook als er "100% natuurlijk" op staat, is 30 gram vloeibare fructose zonder vezels als een kogel die rechtstreeks op je levercellen wordt afgevuurd.</li>
                <li><strong>Transvetten en hergebruikte frituurolie:</strong> geharde margarine en frituurolie die steeds opnieuw wordt gebruikt verhogen de ontsteking en vergroten het viscerale vet.</li>
                <li><strong>Gebak en zoetigheid van witte bloem:</strong> <a href="{food:white-bread}">witbrood</a> wordt in je bloed sneller suiker dan een lepel suiker zelf.</li>
                <li><strong>Gefrituurd en ultrabewerkt voedsel:</strong> zoals <a href="{food:french-fries}">patat</a>; het combineert ongezonde vetten, zout en snel opneembaar zetmeel, de mix die de stofwisseling van de lever overbelast.</li>
            </ul>
            <h3>📊 Snel vergelijken: kies dit 🟢 in plaats van dit 🔴</h3>
            <div class="rule-cards">
                <div class="rule-card"><h3>Dranken</h3><p>🟢 Zwarte koffie, <a href="{food:green-tea}">groene thee</a>, water met citroen<br>🔴 Frisdrank, sappen, energiedrankjes</p></div>
                <div class="rule-card"><h3>Vetten en oliën</h3><p>🟢 Extra vierge olijfolie, <a href="{food:avocado}">avocado</a>, vette vis<br>🔴 Transvetten, hergebruikte frituurolie, geharde margarine</p></div>
                <div class="rule-card"><h3>Eiwit</h3><p>🟢 <a href="{food:boiled-egg}">Eieren</a>, zalm, <a href="{food:grilled-chicken-breast}">kipfilet</a>, <a href="{food:lentils}">linzen</a><br>🔴 Bewerkt vlees, hotdogs, gefrituurde burgers</p></div>
                <div class="rule-card"><h3>Zetmeel</h3><p>🟢 <a href="{food:oatmeal}">Volkoren havermout</a>, <a href="{food:quinoa}">quinoa</a>, linzen, <a href="{food:blueberry}">bessen</a><br>🔴 Witbrood, gebak, koekjes, witte suiker</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-capsules"></i> <span>6. Voedingssupplementen die de levergezondheid ondersteunen (volgens onderzoek)</span></h2>
            <p>Wil je naast gezond eten een extra stap zetten, dan zijn dit de best onderzochte supplementen. Overleg eerst met je arts of apotheker, vooral als je medicijnen gebruikt:</p>
            <ul class="check-list">
                <li><strong><a href="/nl/supplements/milk-thistle.html">Mariadistel</a> (silymarine):</strong> een wilde plant die al eeuwen traditioneel voor de lever wordt gebruikt. De werkzame stof silymarine is een antioxidant, en studies wijzen erop dat ze levercellen beschermt, al is het bewijs bij mensen nog beperkt.</li>
                <li><strong><a href="/nl/supplements/omega-3-fish-oil.html">Omega-3-vetzuren</a> (<bdi>EPA/DHA</bdi>):</strong> 2 gram EPA en DHA per dag draagt bij tot de handhaving van een normaal triglyceridengehalte in het bloed; uit supplementen niet meer dan 5 gram per dag.</li>
                <li><strong><a href="/nl/supplements/choline-bitartrate.html">Choline</a>:</strong> zit van nature in eigeel en <a href="{food:beef-liver}">runderlever</a> en draagt bij tot een normaal vetmetabolisme en tot de instandhouding van een normale leverfunctie; het is nodig voor de vettransporteurs (<bdi>VLDL</bdi>) die vet uit de lever afvoeren, en een ernstig tekort hangt samen met vetophoping in de lever.</li>
                <li><strong><a href="/nl/supplements/magnesium.html">Magnesium</a> (glycinaat / malaat):</strong> draagt bij tot een normaal energieleverend metabolisme, en studies verbinden een laag magnesiumgehalte met insulineresistentie.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-calendar-check"></i> <span>7. Het praktische 12-wekenplan tegen levervet en visceraal buikvet</span></h2>
            <p>Hoe breng je dit morgenochtend in praktijk? Dit is het eenvoudige plan:</p>
            <h3>Week 1 tot 4: stop het metabole lek (minder suiker en fructose)</h3>
            <ol class="steps">
                <li>Laat alles staan waar toegevoegde suiker of glucose-fructosestroop in zit.</li>
                <li>Vervang witbrood door volkoren-, gerst- of kikkererwtenbrood.</li>
                <li>Drink direct na het opstaan twee glazen water, gevolgd door een kop zwarte koffie.</li>
                <li>Wandel elke dag 20 minuten stevig door; wandelen is een van de grootste vijanden van visceraal vet.</li>
            </ol>
            <h3>Week 5 tot 8: rustige <a href="{site:/intermittent-fasting.html}">intermittent fasting</a> (14/10 of 16/8)</h3>
            <ol class="steps">
                <li>Eet je laatste maaltijd om 19.00 uur en je eerste maaltijd om 10.00 of 11.00 uur de volgende ochtend.</li>
                <li>Tijdens de vastenuren raakt de glycogeenvoorraad van de lever op, zodat de lever zijn eigen vet moet verbranden voor energie.</li>
                <li>Kies maaltijden met veel eiwit en vezels, zodat je verzadigd blijft en plotselinge bloedsuikerdips voorkomt.</li>
            </ol>
            <div class="tip"><h3>⚠️ Voordat je gaat vasten</h3><p>Gebruik je diabetesmedicatie (vooral insuline of sulfonylureumderivaten), ben je zwanger of geef je borstvoeding, of heb je een eetstoornis gehad? Begin dan niet met intermittent fasting zonder overleg met je arts; je doseringen moeten misschien worden aangepast om een te lage bloedsuiker te voorkomen.</p></div>
            <h3>Week 9 tot 12: de vruchten plukken en opnieuw testen</h3>
            <ol class="steps">
                <li>Veel mensen zien hun taille 4 tot 8 cm slinken.</li>
                <li>De vermoeidheid na het eten neemt duidelijk af en je voelt je lichter.</li>
                <li>Laat je leverenzymen (<bdi>ALAT/ASAT</bdi>) en de echo opnieuw controleren bij je arts; jij en je arts kunnen aangenaam verrast worden door de nieuwe uitslag.</li>
            </ol>

            <div class="boodi-card">
                <div>
                    <h2>8. Hoe gaat de Boodi-app je helpen? (Binnenkort)</h2>
                    <p>Levervet verminderen vraagt om een nauwkeurig calorietekort (ongeveer 500 kcal per dag) zonder dat je je tekortgedaan voelt of je energie instort. In de Boodi-app bouwden we een evenwichtig dieetprogramma op de erkende <bdi>Mifflin-St Jeor</bdi>-formule, samen met een directe barcodescan:</p>
                    <ul class="check-list">
                        <li><strong>Ingrediënten- en voorkeurenscanner:</strong> vertelt je meteen of een product geharde vetten of verborgen suikers bevat.</li>
                        <li><strong>Alternatievenboom:</strong> houd je van rijst, brood of pasta, dan stelt Boodi alternatieven voor die je bloedsuiker niet snel laten stijgen.</li>
                        <li><strong>Een open keuken met alle keukens van de wereld:</strong> volg het 12-wekenplan met de gerechten waar je van houdt, zonder dat je een droog westers dieet opgelegd krijgt.</li>
                    </ul>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> Ontdek Boodi</a>
            </div>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>9. De meest gezochte vragen over leververvetting</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Laat appelazijn levervet smelten?</h3><p>Natuurlijke appelazijn (een theelepel verdund in een groot glas water voor de maaltijd) kan de insulinegevoeligheid verbeteren en de scherpe bloedsuikerstijging na het eten afzwakken, wat de lever ontlast. Zonder betere voeding is het op zich geen wondermiddel.</p></div>
                <div class="faq-item"><h3>Hoe lang duurt het voordat de lever van het vet af is?</h3><p>Het levervet begint binnen ongeveer twee weken na het schrappen van suiker te dalen, en de resultaten bereiken hun hoogtepunt na 8 tot 12 weken met een gedisciplineerd eetpatroon en regelmatige beweging.</p></div>
                <div class="faq-item"><h3>Is fruit helemaal verboden bij leververvetting?</h3><p>Nee. Heel fruit bevat vezels, vitamines en water die de suikeropname vertragen. Eén tot twee stuks per dag van suikerarm fruit (zoals bessen, <a href="{food:strawberry}">aardbeien</a>, <a href="{food:apple}">groene appels</a> en <a href="{food:kiwi}">kiwi</a>) zijn prima. Vruchtensap kun je beter laten staan, omdat het fruit zijn vezels kwijtraakt en je een geconcentreerde dosis fructose krijgt die rechtstreeks naar de lever gaat.</p></div>
                <div class="faq-item"><h3>Is leververvetting gevaarlijk, en kan het kanker veroorzaken?</h3><p>In de vroege fase is leververvetting in de meeste gevallen omkeerbaar. Gevaar ontstaat als het jarenlang wordt genegeerd, samen met roken en slecht geregelde diabetes: het kan dan overgaan in een vettige leverontsteking (<bdi>MASH</bdi>, vroeger <bdi>NASH</bdi>), daarna in fibrose en, zelden, in leverkanker. Daarom is het ontdekken vandaag en er nu mee aan de slag gaan het mooiste cadeau dat je je lichaam en je toekomst kunt geven.</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-flag-checkered"></i> <span>Conclusie: begin vandaag, je lever wacht op je eerste stap</span></h2>
            <p>Je hoeft niet je hele leven in één dag om te gooien. Begin vandaag met één eenvoudige beslissing: ruil de frisdrank in voor een glas koud water met een schijfje citroen, wandel 20 minuten buiten, geniet van je ochtendkoffie zonder suiker, en houd de lancering van de Boodi-app in de gaten, die je binnenkort stap voor stap begeleidt.</p>
            <p>Je gezondheid is het kostbaarste wat je hebt, en je lever verdient de kans om op adem te komen en weer schoon te worden.</p>'''),
# Swedish (2026-10-27): ALAT/ASAT, decimal comma, vårdcentral/1177; replaces /sv/articles/fettlever.html (301)
sv=dict(
 byline=SV_BYLINE,
 title='Fettlever: Symtom, orsaker – och den goda nyheten i denna kompletta guide',
 h1='Fettlever: Symtom, orsaker – och den goda nyheten i denna kompletta guide',
 crumb='Fettlever och visceralt fett',
 cat='Lever och metabol hälsa',
 desc='Symtom på fettlever och de verkliga orsakerna, varför även smala får det, proverna som visar det, mat som levern mår bra och dåligt av, och en praktisk 12-veckorsplan som minskar leverfett och visceralt bukfett.',
 summary='Varför fett lagras i levern även hos smala, hur prover visar det, och en 12-veckorsplan med mat och rörelse som minskar leverfett och visceralt bukfett.',
 hero_alt='En kvinna med handen på magen i ett ljust kök, som en bild av symtomen vid fettlever och visceralt fett',
 about=['Fatty liver disease', 'MASLD', 'Visceral fat', 'Insulin resistance'],
 disclaimer=SV_DISCLAIMER,
 body='''            <h2 class="section-title"><i class="fas fa-heart"></i> <span>Från hjärtat: till dig som känner dig trött utan att förstå varför</span></h2>
            <p class="lead">Vaknar du efter åtta timmars sömn och känner dig som om du inte har sovit en minut? Har midjemåttet sakta ökat och du har fått en "hård mage" som inte försvinner hur lite du än äter? Eller sa läkaren lugnt efter ett rutinprov: "Dina värden ser bra ut, men du har lite fett på levern"? Då är den här guiden skriven just för dig.</p>
            <p>Det första jag vill att du vet och tar till dig, som en läkare som pratar med en vän: <strong>oroa dig inte, du är inte ensam, och framför allt kan din lever återhämta sig. I tidiga stadier kan leverfettet försvinna helt inom några veckor till några månader.</strong></p>
            <p>Fettlever är inget livstidsstraff, och det viscerala fettet som gömmer sig bakom bukmusklerna är inget öde. I den här artikeln lägger vi de krångliga medicinska termerna åt sidan och pratar vardagsspråk: vad händer i det tysta i din kropp? Varför drabbas även smala? Och vilken enkel daglig plan minskar fettet och ger dig tillbaka ett klart huvud, energi och lätthet?</p>

            <h2 class="section-title"><i class="fas fa-circle-info"></i> <span>1. Vad är fettlever och visceralt bukfett? (Och varför drabbas även smala?)</span></h2>
            <p>Tänk dig att kroppen är ett välskött hus och att levern är dess "centralkök och reningsverk". Leverns viktigaste uppgifter är att omvandla mat till energi, lagra en liten reserv av näringsämnen och rena blodet dygnet runt.</p>
            <p>Normalt innehåller levern väldigt lite fett (mindre än 5 % av dess vikt). När det lagrade fettet överstiger 5 % kallas det <strong>fettlever</strong>, särskilt den form som hänger ihop med metabolt syndrom och för mycket socker och stärkelse. Det moderna vetenskapliga namnet är <bdi>MASLD</bdi>.</p>
            <h3>Myten att "fett kommer av att äta fett"</h3>
            <p>Den största myten är att fett kött eller olja är det som orsakar leverfett. Kliniskt är fettleverns största fiende <strong>socker och raffinerad stärkelse, särskilt fruktos</strong>.</p>
            <p>När du dricker läsk eller sötad juice, eller äter snabbmat full av vitt mjöl, tar kroppen upp sockret mycket snabbt. Musklerna kan inte ta hand om all den energin, så levern måste omvandla överskottssockret till triglycerider i en snabb inre process.</p>
            <h3>Gåtan med den "smala personen med fettlever" (<bdi>TOFI</bdi>)</h3>
            <p>Många säger: "Doktorn, jag väger 65 kilo och har ingen synlig övervikt. Hur kan jag ha fettlever?" Här kommer <strong>det viscerala fettet</strong> in. Fettet i kroppen finns i två former:</p>
            <ul class="check-list">
                <li><strong>Underhudsfett (subkutant fett):</strong> det mjuka fettet som du kan nypa tag i på magen eller låren. Hälsomässigt är det den mindre skadliga formen.</li>
                <li><strong>Djupt visceralt fett (den hårda magen):</strong> fett djupt inne i bukhålan, runt levern, bukspottkörteln och tarmarna. Du kan inte nypa tag i det, och det beter sig som en aktiv "hormonkörtel" som skickar inflammatoriska ämnen och fettsyror direkt till levern via portådern.</li>
            </ul>
            <p>Du kan alltså ha smala armar och ben och ändå bära på en trött, fettinlagrad lever på grund av ohälsosamma matvanor, för lite rörelse och ständig stress.</p>

            <h2 class="section-title"><i class="fas fa-stethoscope"></i> <span>2. Hur säger kroppen ifrån? De dolda tecknen på leverfett</span></h2>
            <p>Levern är ett mycket tålmodigt organ: själva levervävnaden saknar nerver som förmedlar smärta, och därför kallar läkare fettlever för en "tyst sjukdom". Den skriker inte i början, men den skickar svaga signaler som många förväxlar med vardagens trötthet:</p>
            <h3>a) Tung trötthet och hjärndimma efter maten</h3>
            <p>Om en lunch med bröd eller ris gör dig desperat efter en tupplur, eller om du inte kan koncentrera dig och tankarna känns "dimmiga", kan det vara ett tecken på <a href="{site:/insulin-resistance.html}">insulinresistens</a> och på en lever som har svårt att hantera socker och fett.</p>
            <h3>b) En lätt tyngdkänsla uppe till höger i magen</h3>
            <p>Levern sitter under revbenen på höger sida. När den sväller av fett trycker den på hinnan runt den (Glissons kapsel), och du kan känna en tyngd eller ett "lätt obehag", som om en liten kudde tryckte mot höger sida, särskilt när du böjer dig eller har åtsittande kläder.</p>
            <h3>c) Ett växande midjemått och en "levermage"</h3>
            <p>En ansamling av hårt bukfett går ofta hand i hand med fettlever. Om ditt midjemått är över <strong>94 cm för män eller 80 cm för kvinnor</strong> tyder det på extra visceralt fett, och då är det värt att kontrollera levern. Du kan också räkna ut din <a href="{site:/whtr-calculator.html}">midja–längdkvot</a> på några sekunder.</p>
            <h3>d) Hudtecken och mörkare partier på halsen</h3>
            <p>Har du fått små hudflikar runt halsen eller under armarna, eller mörka, sammetslika linjer i nacken? Det är inte smuts och inget ytligt hudproblem; tecknen hänger ofta ihop med höga insulinnivåer och insulinresistens, ett tillstånd som ofta följer med fettlever.</p>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>3. Prover: hur kontrollerar du din lever?</span></h2>
            <figure class="article-figure figure-narrow">
                <img src="/images/visceral-fat-liver-anatomy.webp" alt="Anatomisk illustration av underhudsfett och visceralt fett runt levern och tarmarna, med leverceller fyllda av fettdroppar" width="1024" height="1024" loading="lazy" decoding="async">
                <figcaption>Underhudsfett jämfört med det viscerala fettet runt organen; i cirkeln leverceller fyllda av fettdroppar (steatos).</figcaption>
            </figure>
            <p>Du behöver inte vara rädd för proverna; att kontrollera levern är enkelt och säkert i dag:</p>
            <ul class="check-list">
                <li><strong>Levervärden i blodet (<bdi>ALAT och ASAT</bdi>):</strong> när levercellerna blir inflammerade av fett läcker de här enzymerna ut i blodet. <bdi>ALAT</bdi> är det mest leverspecifika värdet; ligger det över referensvärdet har fettet börjat ge en lätt inflammation.</li>
                <li><strong>Ultraljud:</strong> en smärtfri undersökning på fem minuter. En frisk lever ser mörkgrå ut, medan en fettlever ser ljust vit och reflekterande ut (läkare talar om en "ljus lever").</li>
                <li><strong>HbA1c och insulinresistens (<bdi>HOMA-IR</bdi>):</strong> fettlever, metabolt syndrom och <a href="/sv/diabetes/prediabetes.html">prediabetes</a> hänger ofta ihop, så ditt HbA1c visar om fettbelastningen har börjat påverka hur kroppen hanterar glukos.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-champagne-glasses"></i> <span>4. Den goda nyheten att fira: din lever kan återhämta sig!</span></h2>
            <p>Levern är det enda organet i människokroppen med en exceptionell förmåga att förnya sina egna celler: om en del av en frisk lever opereras bort växer resten ut igen till nästan normal storlek.</p>
            <p>Vad betyder det för dig? Så fort du slutar översvämma levern med raffinerat socker och transfetter och börjar med en balanserad plan börjar levern använda sitt lagrade fett som bränsle.</p>
            <div class="rule-cards">
                <div class="rule-card"><div class="rule-num">5 %</div><h3>5 % viktnedgång</h3><p>Minskar mängden fett i levern tydligt.</p></div>
                <div class="rule-card"><div class="rule-num">7–10 %</div><h3>7–10 % viktnedgång</h3><p>Får den fettrelaterade inflammationen att läka ut hos många patienter och normaliserar oftast levervärdena.</p></div>
                <div class="rule-card"><div class="rule-num">≥ 10 %</div><h3>10 % viktnedgång eller mer</h3><p>Kan till och med vända tidig leverfibros.</p></div>
            </div>
            <p>Enligt kliniska studier och riktlinjerna från de europeiska föreningarna för lever, diabetes och fetma syns resultaten oftast inom två till tre månader (12 veckor) om du håller fast vid bättre mat och mer rörelse.</p>

            <h2 class="section-title"><i class="fas fa-traffic-light"></i> <span>5. Vad du ska äta och undvika: ditt köksschema för en renare lever</span></h2>
            <p>Ditt verkliga apotek finns i kylskåpet. Här är en karta över livsmedel som har stöd i forskningen:</p>
            <div class="tier-title tier-gold"><span class="tier-dot"></span> 🟢 Mat som levern mår bra av</div>
            <ul class="check-list">
                <li><strong><a href="{food:black-coffee}">Svart kaffe utan tillsatser</a>:</strong> många observationsstudier tyder på att 2–3 koppar om dagen (utan socker) hänger ihop med mindre leverfett och lägre risk för leverfibros, tack vare antioxidanter som klorogensyra.</li>
                <li><strong>Korsblommiga grönsaker (<a href="{food:broccoli}">broccoli</a>, <a href="{food:cauliflower}">blomkål</a>, vitkål, <a href="{food:arugula-rocket}">ruccola</a>):</strong> rika på svavelföreningen sulforafan, som enligt studier aktiverar de leverenzymer som tar hand om gifter.</li>
                <li><strong><a href="{food:extra-virgin-olive-oil}">Extra jungfruolivolja</a>:</strong> innehåller oljesyra och antioxidanter; studier tyder på att två matskedar om dagen på salladen, som en del av medelhavskost, förbättrar levervärden och insulinkänslighet.</li>
                <li><strong>Fet fisk (<a href="{food:grilled-salmon}">lax</a>, <a href="{food:canned-sardines}">sardiner</a>, <a href="{food:mackerel}">makrill</a>):</strong> en naturlig källa till omega-3 (<bdi>EPA/DHA</bdi>), som bidrar till att bibehålla normala triglyceridnivåer i blodet.</li>
                <li><strong><a href="{food:artichoke}">Kronärtskocka</a>:</strong> rik på cynarin, som anses stimulera gallflödet och hjälpa levern att föra bort fett.</li>
            </ul>
            <div class="tier-title tier-avoid"><span class="tier-dot"></span> 🔴 Mat som levern mår dåligt av (sluta med den nu)</div>
            <ul class="check-list">
                <li><strong>Läsk och färdiga fruktjuicer:</strong> även när det står "100 % naturlig" är 30 gram flytande fruktos utan fibrer som en kula rakt mot levercellerna.</li>
                <li><strong>Transfetter och återanvänd frityrolja:</strong> härdat margarin och frityrolja som används om och om igen ökar inflammationen och bidrar till visceralt fett.</li>
                <li><strong>Bakverk och sötsaker av vitt mjöl:</strong> <a href="{food:white-bread}">vitt bröd</a> blir socker i blodet snabbare än en sked socker.</li>
                <li><strong>Friterad och ultraprocessad mat:</strong> som <a href="{food:french-fries}">pommes frites</a>; den kombinerar ohälsosamma fetter, salt och snabb stärkelse, den blandning som belastar leverns ämnesomsättning.</li>
            </ul>
            <h3>📊 Snabb jämförelse: välj detta 🟢 i stället för detta 🔴</h3>
            <div class="rule-cards">
                <div class="rule-card"><h3>Drycker</h3><p>🟢 Svart kaffe, <a href="{food:green-tea}">grönt te</a>, vatten med citron<br>🔴 Läsk, juice, energidrycker</p></div>
                <div class="rule-card"><h3>Fetter och oljor</h3><p>🟢 Extra jungfruolivolja, <a href="{food:avocado}">avokado</a>, fet fisk<br>🔴 Transfetter, återanvänd frityrolja, härdat margarin</p></div>
                <div class="rule-card"><h3>Protein</h3><p>🟢 <a href="{food:boiled-egg}">Ägg</a>, lax, <a href="{food:grilled-chicken-breast}">kycklingbröst</a>, <a href="{food:lentils}">linser</a><br>🔴 Charkuterier, varmkorv, friterade hamburgare</p></div>
                <div class="rule-card"><h3>Stärkelse</h3><p>🟢 <a href="{food:oatmeal}">Fullkornshavre</a>, <a href="{food:quinoa}">quinoa</a>, linser, <a href="{food:blueberry}">bär</a><br>🔴 Vitt bröd, bakverk, kex, vitt socker</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-capsules"></i> <span>6. Kosttillskott som stöder leverns hälsa (enligt forskningen)</span></h2>
            <p>Vill du ta ett extra steg vid sidan av hälsosam mat är det här de mest studerade tillskotten. Prata först med din läkare eller apotekspersonal, särskilt om du tar läkemedel:</p>
            <ul class="check-list">
                <li><strong><a href="/sv/supplements/milk-thistle.html">Mariatistel</a> (silymarin):</strong> en vild växt som traditionellt har använts för levern i århundraden. Den verksamma substansen silymarin är en antioxidant, och studier tyder på att den skyddar levercellerna, även om bevisen hos människor fortfarande är begränsade.</li>
                <li><strong><a href="/sv/supplements/omega-3-fish-oil.html">Omega-3-fettsyror</a> (<bdi>EPA/DHA</bdi>):</strong> 2 gram EPA och DHA per dag bidrar till att bibehålla normala triglyceridnivåer i blodet; från tillskott högst 5 gram per dag.</li>
                <li><strong><a href="/sv/supplements/choline-bitartrate.html">Kolin</a>:</strong> finns naturligt i äggula och <a href="{food:beef-liver}">nötlever</a> och bidrar till normal fettomsättning och till att bibehålla normal leverfunktion; kolin behövs för att bilda de fettransportörer (<bdi>VLDL</bdi>) som för ut fett ur levern, och en allvarlig brist hänger ihop med fettinlagring där.</li>
                <li><strong><a href="/sv/supplements/magnesium.html">Magnesium</a> (glycinat / malat):</strong> bidrar till normal energiomsättning, och studier kopplar låga magnesiumnivåer till insulinresistens.</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-calendar-check"></i> <span>7. Den praktiska 12-veckorsplanen mot leverfett och visceralt bukfett</span></h2>
            <p>Hur omsätter du det här i praktiken i morgon bitti? Här är den enkla planen:</p>
            <h3>Vecka 1–4: stoppa det metabola läckaget (bort med socker och fruktos)</h3>
            <ol class="steps">
                <li>Avstå helt från allt med tillsatt socker eller glukos-fruktossirap.</li>
                <li>Byt vitt bröd mot fullkorns-, korn- eller kikärtsbröd.</li>
                <li>Drick två glas vatten direkt när du vaknar, följt av en kopp svart kaffe.</li>
                <li>Promenera raskt 20 minuter om dagen; promenader är en av det viscerala fettets värsta fiender.</li>
            </ol>
            <h3>Vecka 5–8: lugn <a href="{site:/intermittent-fasting.html}">periodisk fasta</a> (14/10 eller 16/8)</h3>
            <ol class="steps">
                <li>Ät dagens sista måltid klockan 19 och nästa dags första måltid klockan 10 eller 11.</li>
                <li>Under de fastande timmarna tar leverns glykogenförråd slut, så levern måste bränna sitt eget fett för energi.</li>
                <li>Satsa på måltider med mycket protein och fibrer för att hålla dig mätt och undvika plötsliga blodsockerdippar.</li>
            </ol>
            <div class="tip"><h3>⚠️ Innan du fastar</h3><p>Om du tar diabetesläkemedel (särskilt insulin eller sulfonylureider), är gravid eller ammar, eller har haft en ätstörning, ska du inte börja med periodisk fasta utan att först prata med din läkare eller vårdcentral; doserna kan behöva justeras för att undvika lågt blodsocker.</p></div>
            <h3>Vecka 9–12: skörda frukterna och ta nya prover</h3>
            <ol class="steps">
                <li>Många märker att midjemåttet minskar med 4–8 cm.</li>
                <li>Tröttheten efter maten avtar tydligt och du känner dig lättare i kroppen.</li>
                <li>Ta om levervärdena (<bdi>ALAT/ASAT</bdi>) och ultraljudet hos din läkare; både du och läkaren kan bli positivt överraskade av det nya resultatet.</li>
            </ol>

            <div class="boodi-card">
                <div>
                    <h2>8. Hur kommer boodi-appen att hjälpa dig? (Kommer snart)</h2>
                    <p>Att minska leverfettet kräver ett exakt kaloriunderskott (omkring 500 kcal om dagen) utan att du känner dig snål mot dig själv eller tappar energin. I boodi-appen har vi byggt ett balanserat kostprogram på den etablerade <bdi>Mifflin-St Jeor</bdi>-formeln, tillsammans med direkt streckkodsskanning:</p>
                    <ul class="check-list">
                        <li><strong>Ingrediens- och preferensskanner:</strong> visar direkt om en produkt innehåller härdat fett eller dolt socker.</li>
                        <li><strong>Alternativträd:</strong> älskar du ris, bröd eller pasta föreslår boodi alternativ som inte höjer blodsockret snabbt.</li>
                        <li><strong>Ett öppet kök med alla världens kök:</strong> följ 12-veckorsplanen med rätterna du tycker om, utan att få en torr västerländsk kost påtvingad.</li>
                    </ul>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> Upptäck boodi</a>
            </div>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>9. De vanligaste frågorna om fettlever</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Smälter äppelcidervinäger bort leverfett?</h3><p>Naturlig äppelcidervinäger (en tesked utspädd i ett stort glas vatten före maten) kan förbättra insulinkänsligheten och dämpa den kraftiga blodsockerhöjningen efter maten, vilket avlastar levern. Utan bättre mat är den i sig ingen mirakellösning.</p></div>
                <div class="faq-item"><h3>Hur lång tid tar det för levern att bli av med fettet?</h3><p>Leverfettet börjar minska inom ungefär två veckor efter att du slutat med socker, och resultaten når sin topp efter 8–12 veckor med disciplinerad kost och regelbunden fysisk aktivitet.</p></div>
                <div class="faq-item"><h3>Är frukt helt förbjuden vid fettlever?</h3><p>Nej. Hel frukt innehåller fibrer, vitaminer och vatten som bromsar sockerupptaget. En till två frukter om dagen av sorter med lite socker (som bär, <a href="{food:strawberry}">jordgubbar</a>, <a href="{food:apple}">gröna äpplen</a> och <a href="{food:kiwi}">kiwi</a>) går bra. Det du ska undvika är fruktjuice, eftersom den tar bort fruktens fibrer och ger en koncentrerad dos fruktos som går direkt till levern.</p></div>
                <div class="faq-item"><h3>Är fettlever farligt, och kan det orsaka cancer?</h3><p>I tidiga stadier går fettlever i de flesta fall att vända. Faran uppstår om den lämnas obehandlad i många år tillsammans med rökning och dåligt kontrollerad diabetes: den kan då gå över i fettrelaterad leverinflammation (<bdi>MASH</bdi>, tidigare <bdi>NASH</bdi>), därefter fibros och i sällsynta fall levercancer. Därför är det den största gåvan du kan ge din kropp och din framtid att upptäcka den i dag och börja ta itu med den nu.</p></div>
            </div>

            <h2 class="section-title"><i class="fas fa-flag-checkered"></i> <span>Avslutning: börja i dag – din lever väntar på ditt första steg</span></h2>
            <p>Du behöver inte ändra hela ditt liv på en dag. Börja i dag med ett enkelt beslut: byt läsken mot ett glas kallt vatten med en citronskiva, promenera 20 minuter utomhus, njut av morgonkaffet utan socker, och håll utkik efter lanseringen av boodi-appen, som snart kan följa dig steg för steg.</p>
            <p>Din hälsa är det mest värdefulla du har, och din lever förtjänar en chans att andas och bli ren igen.</p>'''),
    ),
)

# Blood pressure table: a real table on wide screens, one card per row on phones (labels from data-label);
# the to-do checklist uses real checkboxes. Only this article needs these styles.
HYPERTENSION_CSS = """
        .article-subtitle { font-size: 1.12rem; font-weight: 700; color: var(--text-muted); line-height: 1.7; margin: 0 0 12px; }
        .bp-table { width: 100%; border-collapse: separate; border-spacing: 0; margin: 12px 0 6px; font-size: 0.95rem;
            border: 1px solid var(--border-color); border-radius: var(--radius-md); overflow: hidden; }
        .bp-table th, .bp-table td { padding: 12px; text-align: start; vertical-align: top; border-bottom: 1px solid var(--border-color); }
        .bp-table tbody tr:last-child td { border-bottom: 0; }
        .bp-table th { color: var(--primary); font-weight: 800; background: rgba(16, 185, 129, 0.06); }
        .bp-table td.bp-num { font-weight: 800; white-space: nowrap; }
        .bp-table td.bp-op { color: var(--text-muted); font-weight: 700; font-size: 0.85rem; padding-top: 14px; }
        .bp-table td:first-child { font-weight: 800; border-inline-start: 5px solid var(--bp, #10b981); }
        .bp-table td:last-child { color: var(--text-muted); }
        .bp-table td:first-child bdi, .bp-table th bdi { font-weight: 600; color: var(--text-muted); font-size: 0.85em; white-space: nowrap; }
        .article-page h3 bdi { white-space: nowrap; }   /* an English term in brackets never splits across lines */
        .bp-ok { --bp: #10b981; } .bp-elev { --bp: #f1c40f; } .bp-s1 { --bp: #f39c12; } .bp-s2 { --bp: #e74c3c; }
        @media (max-width: 680px) {
            .bp-table, .bp-table tbody, .bp-table tr, .bp-table td { display: block; width: 100%; }
            .bp-table { border: 0; overflow: visible; }
            .bp-table thead { display: none; }
            .bp-table tr { background: var(--bg-input); border: 1px solid var(--border-color); border-inline-start: 5px solid var(--bp, #10b981);
                border-radius: var(--radius-md); padding: 12px 14px; margin-bottom: 12px; display: grid;
                grid-template-columns: 1fr auto 1fr; gap: 6px 10px; align-items: center; }
            .bp-table td { padding: 0; border: 0; }
            .bp-table td:first-child { grid-column: 1 / -1; border: 0; font-size: 1rem; }
            .bp-table td:last-child { grid-column: 1 / -1; font-size: 0.92rem; }
            .bp-table td.bp-num { white-space: normal; }
            .bp-table td.bp-num::before { content: attr(data-label); display: block; font-size: 0.75rem; font-weight: 700; color: var(--text-muted); }
            .bp-table td.bp-op { text-align: center; align-self: end; padding: 0 0 3px; }
        }
        .danger-box { border: 2px solid #e74c3c; background: rgba(231, 76, 60, 0.08); border-radius: var(--radius-md); padding: 18px 20px; margin: 22px 0; }
        .danger-box h3 { margin: 0 0 8px; color: var(--text-main); }
        .danger-box p { margin: 0; }
        .todo-list { list-style: none; padding: 0; margin: 10px 0 24px; display: grid; gap: 10px; }
        .todo-list label { display: flex; gap: 12px; align-items: flex-start; background: var(--bg-input); border: 1px solid var(--border-color);
            border-radius: var(--radius-sm); padding: 12px 16px; cursor: pointer; font-size: 1.04rem; line-height: 1.7; }
        .todo-list input { width: 20px; height: 20px; margin-top: 4px; flex-shrink: 0; accent-color: var(--primary); cursor: pointer; }
        .todo-list input:checked + span { text-decoration: line-through; color: var(--text-muted); }
"""

HYPERTENSION_INSULIN = dict(
    hubs=['diabetes'],                                   # user decision 2026-10-30: a card on the diabetes hubs too
    slugs=dict(ar='high-blood-pressure-sugar-insulin', en='high-blood-pressure-sugar-insulin', nl='hoge-bloeddruk-suiker-insuline',
               sv='hogt-blodtryck-socker-insulin'),
    hero='high-blood-pressure-sugar-hidden-partner-cover.webp', hero_size=(1376, 768),
    thumb='high-blood-pressure-sugar-thumb.webp', thumb_size=(640, 360), thumb_2x=('high-blood-pressure-sugar-card.webp', 1280),
    published='2026-10-30', modified='2026-10-30',
    references=[
        'Whelton PK, Carey RM, Aronow WS, et al. 2017 ACC/AHA Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults. Hypertension 2018;71(6):e13–e115',
        'McEvoy JW, McCarthy CP, Bruno RM, et al. 2024 ESC Guidelines for the management of elevated blood pressure and hypertension. Eur Heart J 2024;45(38):3912–4018',
        'Hall JE, do Carmo JM, da Silva AA, Wang Z, Hall ME. Obesity-induced hypertension: interaction of neurohumoral and renal mechanisms. Circ Res 2015;116(6):991–1006',
        'Sacks FM, Svetkey LP, Vollmer WM, et al. Effects on blood pressure of reduced dietary sodium and the Dietary Approaches to Stop Hypertension (DASH) diet. N Engl J Med 2001;344(1):3–10',
        'Neter JE, Stam BE, Kok FJ, Grobbee DE, Geleijnse JM. Influence of weight reduction on blood pressure: a meta-analysis of randomized controlled trials. Hypertension 2003;42(5):878–884',
        'Edwards JJ, Deenmamode AHP, Griffiths M, et al. Exercise training and resting blood pressure: a large-scale pairwise and network meta-analysis of randomised controlled trials. Br J Sports Med 2023;57(20):1317–1326',
        'World Health Organization. Guideline: Sodium intake for adults and children. Geneva: WHO; 2012',
        'Serban C, Sahebkar A, Ursoniu S, Andrica F, Banach M. Effect of sour tea (Hibiscus sabdariffa L.) on arterial hypertension: a systematic review and meta-analysis of randomized controlled trials. J Hypertens 2015;33(6):1119–1127',
        'Sigurjónsdóttir HA, Franzson L, Manhem K, et al. Liquorice-induced rise in blood pressure: a linear dose-response relationship. J Hum Hypertens 2001;15(8):549–552',
    ],
    named_author=True,                                   # user decision 2026-10-30: «بقلم د. وسيم حبيب» (byline + schema)
    article_schema=True,
    extra_css=HYPERTENSION_CSS,
    content=dict(
ar=dict(
 byline='بقلم د. وسيم حبيب',
 title='ارتفاع ضغط الدم والسكر: العلاقة الخفية اللي لازم تعرفها',
 h1='صدّق أو لا تصدّق: السكر عم يرفع ضغطك… مش بس الملح!',
 subtitle='ارتفاع ضغط الدم، القاتل الصامت: أسبابه، علاقته بالإنسولين، وكيف تحمي شرايينك',
 crumb='ارتفاع ضغط الدم والسكر',
 summary='ضغطك عالي وما بتاكل ملح؟ فتّش عن السكر: كيف الإنسولين بيرفع الضغط، وكيف تقيسه صح بالبيت، وخطة أكل ورياضة ونوم تحمي شرايينك.',
 cat='القلب والأوعية الدموية',
 desc='ليش الملح مش السبب الوحيد لارتفاع ضغط الدم؟ اكتشف كيف الإنسولين بيرفع ضغطك، وشو تاكل وكيف تحمي شرايينك.',
 hero_alt='امرأة قلقة تقيس ضغط دمها بجهاز على الزند، وأمامها مملحة وقهوة مثلجة محلّاة وحلوى شوكولا، وخلفها ظل من مكعبات السكر',
 about=['Hypertension', 'Insulin resistance', 'Blood pressure', 'DASH diet'],
 disclaimer='⚖️ هذا المقال للتوعية والتثقيف الصحي، ولا يغني عن استشارة الطبيب. لا توقف ولا تعدّل أي دواء بدون الرجوع لطبيبك.',
 body='''            <p class="lead">هل تساءلت يوماً لماذا يُطلق عليه الطب الحديث لقب «القاتل الصامت»؟ إن كنت لا تعلم، فدعني أخبرك بالسبب الحقيقي: إنه يتسلل بهدوء إلى شرايينك وأنسجة أعضائك الحيوية ويدمرها خطوة بخطوة، دون أن تشعر بأي ألم، حتى يستفحل الأمر.</p>
            <p>ارتفاع ضغط الدم لا يبدأ كمرض معزول "يتيم الأب والأم"، بل هو في حقيقته انعكاس مباشر لخلل أيضي (<bdi>Metabolic Dysfunction</bdi>) داخل جسمك والتهابات مستمرة في بطانة أوعيتك الدموية.</p>
            <p>تعالوا معاً في هذا المقال لنفكك هذا اللغز بهدوء ودون أي تعقيدات طبية؛ سنحلل هذه الأرقام، ونشرح كيف ترتبط <a href="{site:/insulin-resistance.html}">مقاومة الإنسولين</a> (<bdi>Insulin Resistance</bdi>) ارتباطاً وثيقاً بارتفاع الضغط، ونضع معاً خطة متكاملة لنعيد المرونة والحيوية لشرايينك... ونحمي قلبك الصغير اللي ما بيتحمّل.</p>

            <h2 class="section-title"><i class="fas fa-heart-pulse"></i> <span>ما هو ضغط الدم؟ وماذا تعني الأرقام؟</span></h2>
            <p>عندما ينبض قلبك بوم بوم، فهو يضخ الدم عبر شبكة معقدة من الأوعية الدموية. فخذوا هالمعلومة بخط عريييض: <strong>ضغط الدم هو مقياس قوة دفع الدم ضد جدران الشرايين أثناء جريانه</strong>، يعني بالمختصر هو مقاومة الجدران لقوة جريان الدم.</p>
            <p>هاد الضغط اللي بيصير لحظة ما القلب يضخ، منسميه <strong>الضغط الانقباضي</strong> (<bdi>Systolic Blood Pressure</bdi>). وضحت الفكرة؟ يعني ببساطة هو الرقم الكبير، الرقم اللي فوق. احفظوا اسمه منيح: الضغط الانقباضي.</p>
            <p>هلّق بعد ما ضخ القلب الدم اللي فيه، صار بدو يرتخي ويرتاح ليرجع يتعبى بالدم، فهون بيجي دور <strong>الضغط الانبساطي</strong> (<bdi>Diastolic Blood Pressure</bdi>). وطبعاً الانبساطي ما إلو علاقة بالبسط والفرح والسرور، الانبساطي يعني التمدد والارتخاء، يعني فترة الراحة للقلب بين النبضة والنبضة. بهالفترة بيتقاس الضغط داخل الشرايين، لحتى يمتلئ القلب من جديد ويعيد الكرّة: بوم... بوم... بوم... بوم. سهلة؟</p>
            <h3>كيف منعرف إذا الضغط طبيعي أو بلّش يعطينا إنذارات؟</h3>
            <table class="bp-table">
                <thead><tr><th>التصنيف</th><th>الانقباضي <bdi>(Systolic)</bdi></th><th></th><th>الانبساطي <bdi>(Diastolic)</bdi></th><th>شو يعني؟</th></tr></thead>
                <tbody>
                    <tr class="bp-ok"><td>طبيعي ومثالي <bdi>(Normal)</bdi></td><td class="bp-num" data-label="الانقباضي">أقل من 120</td><td class="bp-op">و</td><td class="bp-num" data-label="الانبساطي">أقل من 80</td><td>أوعية دموية مرنة، وقلب شغّال بأريحية تامة</td></tr>
                    <tr class="bp-elev"><td>ضغط مرتفع، مرحلة الإنذار المبكر <bdi>(Elevated)</bdi></td><td class="bp-num" data-label="الانقباضي"><bdi>120 - 129</bdi></td><td class="bp-op">و</td><td class="bp-num" data-label="الانبساطي">أقل من 80</td><td>بداية تيبّس الأوعية، ووقت التدخل الفوري بنمط الحياة</td></tr>
                    <tr class="bp-s1"><td>ارتفاع الضغط، المرحلة الأولى <bdi>(Stage 1 Hypertension)</bdi></td><td class="bp-num" data-label="الانقباضي"><bdi>130 - 139</bdi></td><td class="bp-op">أو</td><td class="bp-num" data-label="الانبساطي"><bdi>80 - 89</bdi></td><td>صار في تشخيص، والطبيب بيقرر حسب باقي المخاطر</td></tr>
                    <tr class="bp-s2"><td>ارتفاع الضغط، المرحلة الثانية <bdi>(Stage 2 Hypertension)</bdi></td><td class="bp-num" data-label="الانقباضي">140 فأكثر</td><td class="bp-op">أو</td><td class="bp-num" data-label="الانبساطي">90 فأكثر</td><td>بدها متابعة طبية منتظمة وغالباً علاج دوائي</td></tr>
                </tbody>
            </table>
            <p class="table-note">الأرقام كلها بالملّيمتر زئبقي (<bdi>mmHg</bdi>).</p>
            <div class="danger-box">
                <h3>🚨 علامات الإنذار الأحمر (طوارئ فورية)</h3>
                <p>إذا سجّل جهاز القياس قراءة أعلى من <bdi>180 / 120</bdi> ملم زئبق، مترافقة مع صداع شديد ومفاجئ، أو ضبابية بالرؤية، أو ضيق تنفس، أو ألم بالصدر، أو ضعف بطرف من الجسم أو صعوبة بالكلام، فهاي مش حالة منستنى فيها تعديل الأكل. هاي حالة طوارئ طبية (<bdi>Hypertensive Emergency</bdi>) بتستوجب <strong>التوجه الفوري لأقرب مستشفى أو الاتصال بالإسعاف</strong>.</p>
            </div>

            <h2 class="section-title"><i class="fas fa-user-secret"></i> <span>القاتل الصامت إلو شريك سرّي… تعرّف عليه قبل ما يتعرّف عليك 😉</span></h2>
            <p>هون أهم نقطة بموضوعنا اليوم، واللي كتير بتغيب عن البال. ضغطك عالي وما بتاكل ملح؟ فتّش عن السكر! أغلب الناس بتعتقد إنو الضغط بيرتفع بسبب كترة الملح بس. لكن يا أصدقائي، الحقيقة أعمق من هيك بكتير، والمتهم الحقيقي مش اللي بتفكر فيه. خلونا نحكيها عالمكشوف: <strong>السكر بيرفع الإنسولين، والإنسولين هو بطل القصة المخفي.</strong> ويالله، خلّي الإنسولين يكشف المستور:</p>
            <h3>1. احتباس الصوديوم بالكلى (<bdi>Sodium Retention</bdi>)</h3>
            <figure class="article-figure">
                <img src="/images/sodium-water-retention-blood-vessel-hypertension.webp" alt="رسم توضيحي لمقطع في وعاء دموي مليء بكريات الدم الحمراء وأيونات الصوديوم وجزيئات الماء، مع إشارات تصل إلى الكلية لتحبس الصوديوم فيزيد حجم الدم والضغط على جدار الشريان" width="1200" height="896" loading="lazy" decoding="async">
                <figcaption>الإنسولين المرتفع يأمر الكلية بحبس الصوديوم، والصوديوم يسحب الماء معه إلى الدم، فيرتفع الضغط على جدران الشرايين.</figcaption>
            </figure>
            <p>المستويات المرتفعة المزمنة من هرمون الإنسولين بالدم (<bdi>Hyperinsulinemia</bdi>) بتبعت إشارات مباشرة، دايركت، للكليتين لتعيد امتصاص الصوديوم وتمنع خروجه بالبول. والصوديوم وين ما راح بيسحب المي وراه، فبيزيد حجم الدم الكلي داخل الشرايين، وبيزيد الضغط عليها.</p>
            <h3>2. استثارة الجهاز العصبي الودّي (<bdi>Sympathetic Nervous System</bdi>)</h3>
            <p>فرط الإنسولين بيخلي الجهاز العصبي السمبثاوي بحالة تأهّب دائم، كأنو في حرامي بالبيت 24 ساعة. والنتيجة؟ انقباض بالأوعية الدموية (<bdi>Vasoconstriction</bdi>) وتسارع بنبضات قلبك الصغرور.</p>
            <h3>3. بطانة الأوعية بتفقد مرونتها (<bdi>Endothelial Dysfunction</bdi>)</h3>
            <p>بالحالة الطبيعية، بطانة الشرايين بتفرز غاز صغير وسحري اسمه أكسيد النيتريك (<bdi>Nitric Oxide</bdi>)، وهاد شغلته يوسّع الشرايين ويخليها طرية ومرنة. لما تصير عندك مقاومة إنسولين، إنتاج أكسيد النيتريك بيقلّ، والالتهاب المزمن الخفيف (<bdi>Chronic Low-grade Inflammation</bdi>) بيبلّش ياكل بالبطانة. الشريان اللي كان متل المطاط الطري، بيصير متل خرطوم المي القديم اللي قاعد بالشمس من سنين.</p>
            <h3>4. نظام الرينين-أنجيوتنسين-ألدوستيرون (<bdi>RAAS</bdi>)</h3>
            <p>هاد نظام هرموني بيضبط الضغط والسوائل بالجسم. مع مقاومة الإنسولين والدهون الزايدة، هالنظام بيصير شغّال أوفر تايم: الأنجيوتنسين 2 (<bdi>Angiotensin II</bdi>) بيضيّق الشرايين، والألدوستيرون (<bdi>Aldosterone</bdi>) بيحبس صوديوم أكتر. يعني ضربة دبل.</p>
            <h3>5. الدهون الحشوية (<bdi>Visceral Fat</bdi>): مش مجرد كرش</h3>
            <p>الدهون اللي حوالين الأحشاء جوّا البطن مش مخزن طاقة ساكت. هاي نسيج نشيط بيفرز مواد التهابية (<bdi>Cytokines</bdi>) وبيفرز كمان المادة الخام للأنجيوتنسين. لهيك محيط الخصر (<bdi>Waist Circumference</bdi>) أحياناً بيحكيلك عن خطر الضغط أكتر من رقم الوزن على الميزان. (اقرأ أكتر عن <a href="/articles/fatty-liver-and-visceral-fat.html">الدهون الحشوية والكبد الدهني</a>.)</p>
            <h3>طيب، في أسباب تانية؟</h3>
            <p>أكيد. منها الوراثة والعمر، والحساسية للملح (<bdi>Salt Sensitivity</bdi>) اللي بتختلف من شخص لشخص، وانقطاع النفس أثناء النوم (رح نحكي عنه بعدين)، والتدخين، والكحول، وبعض الأدوية متل مسكنات الالتهاب (<bdi>NSAIDs</bdi>)، وبخاخات الأنف المضادة للاحتقان، وحبوب منع الحمل عند بعض السيدات.</p>
            <p>وفي نوع اسمه ارتفاع الضغط الثانوي (<bdi>Secondary Hypertension</bdi>)، يعني في سبب واضح وراه متل أمراض الكلى أو الغدة الدرقية أو الكظر. الطبيب بيفكّر فيه خصوصاً إذا ظهر الضغط بعمر صغير، أو كان عالي كتير وما عم يستجيب للعلاج.</p>

            <h2 class="section-title"><i class="fas fa-stethoscope"></i> <span>طيب، كيف بحس فيه؟ وهون المفاجأة</span></h2>
            <p>بأغلب الحالات، ما بتحس بشي أبداً. ولا وجع ولا إشارة. وهون بالضبط سر لقب «القاتل الصامت». في ناس بتعيش سنين وضغطها 150 وهي مفكرة حالها حديد.</p>
            <p>أحياناً، خصوصاً لما يكون الضغط عالي كتير، ممكن تظهر شغلات متل:</p>
            <ul class="check-list">
                <li>صداع الصبح، غالباً بمؤخرة الراس</li>
                <li>دوخة أو طنين بالأذنين (<bdi>Tinnitus</bdi>)</li>
                <li>خفقان أو إحساس بنبض القلب</li>
                <li>تعب عام وصعوبة بالتركيز</li>
            </ul>
            <p>بس انتبه، هالأعراض مش مقياس. إذا ما عندك أعراض، هاد ما بيعني إنو ضغطك منيح. والجملة الشعبية «ضغطي عالي لأنو راسي عم يوجعني» كتير مرات بتكون معكوسة: الوجع والتوتر هنن اللي رفعوا الضغط مؤقتاً. <strong>الحَكَم الوحيد هو جهاز القياس.</strong></p>

            <h2 class="section-title"><i class="fas fa-house-medical"></i> <span>كيف تقيس ضغطك بالبيت متل الشاطرين</span></h2>
            <p>قراءة وحدة بالعيادة أحياناً بتكذب. في شي اسمه ارتفاع ضغط المعطف الأبيض (<bdi>White Coat Hypertension</bdi>): بمجرد ما تشوف الدكتور، ضغطك بيطلع. وفي العكس كمان، الضغط المقنّع (<bdi>Masked Hypertension</bdi>): بالعيادة تمام، وبالبيت والشغل عالي. لهيك القياس المنزلي (<bdi>Home Blood Pressure Monitoring</bdi>) ذهب.</p>
            <h3>كيف بتعملها صح:</h3>
            <ol class="steps">
                <li>استعمل جهاز عالزند (<bdi>Upper Arm Cuff</bdi>)، مش عالمعصم، وتأكد إنو الكمّ مناسب لحجم إيدك.</li>
                <li>لا قهوة ولا دخان ولا رياضة قبل القياس بنص ساعة، وفضّي مثانتك.</li>
                <li>اقعد على كرسي، ضهرك مسنود، ورجليك عالأرض بدون ما تصلّبهن فوق بعض، وارتاح 5 دقايق.</li>
                <li>حط إيدك على طاولة بمستوى قلبك، والكم على الجلد مباشرة مش فوق الكنزة.</li>
                <li>لا تحكي ولا تشوف موبايلك وقت القياس.</li>
                <li>خود قراءتين بينهن دقيقة، وسجّل المعدّل.</li>
                <li>كرر الشي الصبح والمسا لمدة أسبوع، وخود الجدول معك للدكتور.</li>
            </ol>
            <p>إذا طلع معدّل قراءاتك بالبيت <bdi>130 / 80</bdi> أو أكتر، هاد مؤشر لازم تحكي فيه مع طبيبك. وبالإرشادات الأوروبية (<bdi>ESC 2024</bdi>)، حد القياس بالبيت هو <bdi>135 / 85</bdi>.</p>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>لما تكون على أبواب الضغط: شو منعمل؟</span></h2>
            <p>إذا قراءاتك صارت بين 120 و139، أو الانبساطي عم يلعب حوالين الـ80، فهاد مش وقت الهلع، بس كمان مش وقت «بكرا منشوف». هاي أحلى مرحلة للتدخل، لأنو الشرايين لسا مرنة والجسم بيستجيب بسرعة.</p>
            <h3>الخطوة الأولى: اعرف شو عم يصير جوّا</h3>
            <p>اطلب من طبيبك هالتحاليل، لأنها بتكشف إذا القصة مرتبطة بالإنسولين والأيض:</p>
            <ul class="check-list">
                <li>سكر الصيام (<bdi>Fasting Glucose</bdi>) والسكر التراكمي (<bdi>HbA1c</bdi>)</li>
                <li>إنسولين الصيام (<bdi>Fasting Insulin</bdi>)، ومنه بينحسب مؤشر مقاومة الإنسولين (<bdi>HOMA-IR</bdi>)</li>
                <li>الدهون بالدم (<bdi>Lipid Profile</bdi>)، وخصوصاً الدهون الثلاثية (<bdi>Triglycerides</bdi>) والكوليسترول الجيد (<bdi>HDL</bdi>)</li>
                <li>وظائف الكلى (<bdi>Creatinine, eGFR</bdi>) والألبومين بالبول (<bdi>Urine Albumin</bdi>)</li>
                <li>الصوديوم والبوتاسيوم بالدم، وهرمون الغدة الدرقية (<bdi>TSH</bdi>)</li>
            </ul>
            <p>وقيس محيط خصرك عند مستوى السرّة. بشكل عام، أكتر من <strong>94 سم عند الرجال</strong> وأكتر من <strong>80 سم عند السيدات</strong> هي إشارة للدهون الحشوية. وفيك كمان تحسب <a href="{site:/whtr-calculator.html}">نسبة الخصر إلى الطول</a> بثواني. وإذا تحاليل السكر طلعت على الحفة، اقرأ دليلنا عن <a href="/diabetes/prediabetes.html">مرحلة ما قبل السكري</a>.</p>
            <h3>الخطوة التانية: أعطي نمط حياتك 3 لـ6 أشهر جدية</h3>
            <p>بمرحلة الإنذار المبكر، وبكتير من حالات المرحلة الأولى إذا ما في مخاطر تانية، الطبيب بيبدأ بتعديل نمط الحياة. ولا تستهين فيه: كل كيلو بتنزلو من الوزن الزايد، بينزل الضغط تقريباً 1 ملم زئبق. والأكل الصحي لحالو ممكن ينزّل الانقباضي 8 لـ11 ملم زئبق عند ناس كتير. يعني أحياناً نفس مفعول حبة دوا.</p>
            <div class="tip warn"><p><strong>بس انتبه:</strong> إذا الطبيب وصفلك دوا، لا توقفه من راسك لأنو قريت مقال حلو. التغذية والرياضة بيشتغلوا مع الدوا، والطبيب هو اللي بيقرر إذا فيكن تخففوه مع الوقت.</p></div>

            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>صحنك هو صيدليتك: التغذية اللي بتساعد</span></h2>
            <p>في نظامين غذائيين مدروسين منيح للضغط: نظام داش (<bdi>DASH Diet</bdi>)، يعني حرفياً «المقاربات الغذائية لإيقاف ارتفاع الضغط»، والنظام المتوسطي (<bdi>Mediterranean Diet</bdi>). والخبر الحلو؟ هالنظامين مبنيين على أكل بسيط وطبيعي، قريب كتير من أكل جدّاتنا بكل مكان بالعالم، قبل ما تغزينا الوجبات السريعة.</p>
            <h3>البوتاسيوم (<bdi>Potassium</bdi>): خصم الصوديوم اللدود</h3>
            <p>البوتاسيوم بيساعد الكلى تطرد الصوديوم، وبيرخي جدران الأوعية. لاقيه بـ:</p>
            <ul class="check-list">
                <li><a href="{food:spinach}">السبانخ</a> و<a href="{food:swiss-chard}">السلق</a> و<a href="{food:molokhia}">الملوخية</a> والبقدونس</li>
                <li><a href="{food:avocado}">الأفوكادو</a> و<a href="{food:banana}">الموز</a> و<a href="{food:dried-apricots}">المشمش المجفف</a></li>
                <li>البقوليات: <a href="{food:lentils}">العدس</a> و<a href="{food:white-beans}">الفاصولياء</a> و<a href="{food:chickpeas}">الحمص</a></li>
                <li><a href="{food:sweet-potato}">البطاطا الحلوة</a> و<a href="{food:boiled-potato}">العادية المسلوقة</a> بقشرتها</li>
                <li>اللبن الرائب و<a href="{food:labneh}">اللبنة</a> قليلة الملح</li>
            </ul>
            <div class="tip warn"><p><strong>تنبيه مهم:</strong> إذا عندك مرض كلى، أو عم تاخد أدوية للضغط أو أدوية مدرّة للبول، احكي مع طبيبك قبل ما تكتّر البوتاسيوم أو تستعمل بدائل الملح (<bdi>Salt Substitutes</bdi>).</p></div>
            <h3>المغنيسيوم (<bdi>Magnesium</bdi>): ملك الاسترخاء</h3>
            <p>بيساعد العضلات الملساء بجدران الشرايين ترتخي، وفي دراسات بتربط المغنيسيوم بحساسية أفضل للإنسولين. لاقيه ب<a href="{food:pumpkin-seeds}">بذر اليقطين</a>، واللوز و<a href="{food:cashews}">الكاجو</a>، والخضار الورقية، و<a href="{food:dark-chocolate-85}">الشوكولا الغامقة 85%</a> (مربعين مش لوح كامل، اتفقنا؟).</p>
            <h3>النترات الطبيعية (<bdi>Dietary Nitrates</bdi>): الشمندر والجرجير</h3>
            <p>هون بترجع قصة أكسيد النيتريك. <a href="{food:beetroot}">الشمندر</a> و<a href="{food:arugula-rocket}">الجرجير</a> والسبانخ غنيين بنترات بيحوّلها الجسم لأكسيد النيتريك، فبتتوسّع الشرايين. كاسة عصير شمندر أو صحن سلطة جرجير يومياً عادة حلوة.</p>
            <h3>الألياف وقلة السكر: عشان ننزّل الإنسولين</h3>
            <p>بما إنو الإنسولين هو بطل القصة المخفي، فلازم نهدّيه (وبتلاقي المؤشر الجلايسيمي لكل صنف بـ<a href="{site:/foods.html}">دليل الأطعمة</a>):</p>
            <ul class="check-list">
                <li><a href="{food:oatmeal}">الشوفان</a> و<a href="{food:bulgur}">البرغل</a> و<a href="{food:whole-wheat-bread}">الخبز الأسمر الحقيقي</a> بدل الأبيض</li>
                <li>خضار بكل وجبة، وابدأ أكلك بالسلطة</li>
                <li>بروتين بكل وجبة: <a href="{food:boiled-egg}">بيض</a>، سمك، <a href="{food:grilled-chicken-breast}">دجاج</a>، بقوليات</li>
            </ul>
            <h3>الدهون الصحية</h3>
            <p><a href="{food:extra-virgin-olive-oil}">زيت الزيتون البكر</a>، والسمك الدهني متل <a href="{food:grilled-salmon}">السلمون</a> و<a href="{food:canned-sardines}">السردين</a> و<a href="{food:mackerel}">الماكريل</a> مرتين بالأسبوع لأوميغا 3 (<bdi>Omega-3</bdi>)، و<a href="{food:walnuts}">الجوز</a>.</p>
            <h3>شغلات من المطبخ إلها دعم علمي معقول</h3>
            <ul class="check-list">
                <li><strong>الكركديه (<bdi>Hibiscus Tea</bdi>):</strong> بعض الدراسات لقت إنو بينزّل الضغط شوي، كاستين أو تلاتة باليوم بدون سكر.</li>
                <li><strong><a href="{food:garlic}">الثوم</a>:</strong> إلو تأثير بسيط ومفيد.</li>
            </ul>
            <p>بس ما في عشبة سحرية بتلغي الدوا أو بتصلّح نمط حياة غلط.</p>

            <h2 class="section-title"><i class="fas fa-ban"></i> <span>الأطعمة اللي لازم نعطيها «بلوك»</span></h2>
            <h3>الملح المخفي (<bdi>Hidden Sodium</bdi>): العدو اللي ما بتشوفه</h3>
            <p>طيب، يعني الملح بريء؟ لا أبداً، هو شريك بالجريمة بس مش لحالو. ومنقلكن سر؟ أغلب الملح اللي منآكلو مش من المملحة اللي عالطاولة. أكتر من 70% منو جاي من الأكل الجاهز والمصنّع. الهدف إنو ما تتجاوز <strong>2000 ملغ صوديوم باليوم</strong>، يعني تقريباً معلقة صغيرة ملح (5 غرام) بكل شي.</p>
            <p>انتبه لهدول:</p>
            <ul class="check-list">
                <li>الخبز والمعجنات: ما بتطعم مالح بس فيها كتير</li>
                <li>الأجبان المالحة: متل <a href="{food:halloumi-cheese}">الحلوم</a> و<a href="{food:greek-feta}">الفيتا</a> والبارميزان</li>
                <li><a href="{food:pickled-cucumbers-gherkins}">المخللات</a> والزيتون</li>
                <li>اللحوم المصنّعة: متل السجق والهوت دوغ والبيكون</li>
                <li>مكعبات المرق (<bdi>Stock Cubes</bdi>) والشوربات الجاهزة</li>
                <li>الشيبس والمكسرات المملحة والصوصات متل <a href="{food:naturally-brewed-soy-sauce}">الصويا</a> والكاتشب</li>
                <li>أكل المطاعم والوجبات السريعة</li>
            </ul>
            <div class="tip"><p><strong>حيلة صغيرة بقراءة الملصق:</strong> إذا كاتب صوديوم (<bdi>Sodium</bdi>)، اضربو بـ2.5 بيعطيك كمية الملح. يعني 400 ملغ صوديوم = 1 غرام ملح.</p></div>
            <h3>السكر والنشويات المكررة (<bdi>Refined Carbs</bdi>): الجواب بصحن الحلو، مش بالمملحة</h3>
            <p>بما إنو الإنسولين هو المفتاح، فالمشروبات الغازية، والعصائر المعلّبة، والحلويات، والخبز الأبيض بكترة، كلها بترفع الإنسولين وبتغذّي القصة اللي حكينا عنها. والفركتوز المضاف (<bdi>High-Fructose Corn Syrup</bdi>) بالذات إلو علاقة بارتفاع حمض البول والضغط.</p>
            <h3>عرق السوس (<bdi>Licorice</bdi>): بالمشروبات والحلويات والسكاكر</h3>
            <p>هي معلومة كتير ناس ما بتعرفها. <a href="{food:licorice-drink}">عرق السوس</a> فيه مادة اسمها الغليسيريزين (<bdi>Glycyrrhizin</bdi>)، وهاي بتتصرف متل الألدوستيرون: بتحبس الصوديوم وبتطرد البوتاسيوم، وبترفع الضغط. فإذا ضغطك على الحفة، خفّف مشروبات وسكاكر عرق السوس.</p>
            <h3>الكحول ومشروبات الطاقة</h3>
            <p>الكحول حتى بكميات «اجتماعية» بيرفع الضغط مع الوقت. ومشروبات الطاقة (<bdi>Energy Drinks</bdi>) بكميات كافيين وسكر عالية ممكن ترفعه فجأة. أما <a href="{food:black-coffee}">القهوة العادية</a>، كاسة أو تنتين باليوم، فغالباً ما في مشكلة عند أغلب الناس.</p>

            <h2 class="section-title"><i class="fas fa-person-walking"></i> <span>الرياضة: الدوا اللي ببلاش</span></h2>
            <p>الرياضة بتشتغل على أكتر من جبهة بنفس الوقت: بتحسّن حساسية الإنسولين، وبتهدّي الجهاز السمبثاوي، وبتزيد إفراز أكسيد النيتريك، وبتنزّل الدهون الحشوية. يعني بتضرب القصة من جذورها.</p>
            <h3>التمارين الهوائية (<bdi>Aerobic Exercise</bdi>)</h3>
            <p>مشي سريع، سباحة، بسكليت: <strong>150 دقيقة بالأسبوع</strong>، يعني نص ساعة 5 أيام. هالشي لحالو ممكن ينزّل الانقباضي 5 لـ8 ملم زئبق. ونصيحة ذهبية: مشوار 10 لـ15 دقيقة بعد الأكل بينزّل سكر الدم والإنسولين بشكل ممتاز.</p>
            <h3>تمارين المقاومة (<bdi>Resistance Training</bdi>)</h3>
            <p>أوزان، أو أشرطة مطاطية، أو وزن الجسم: مرتين لـتلات مرات بالأسبوع. العضلات أكبر مستهلك للسكر بالجسم، وكل ما زادت عضلاتك، قلّت حاجتك للإنسولين.</p>
            <h3>المفاجأة: التمارين الثابتة (<bdi>Isometric Exercise</bdi>)</h3>
            <p>تحليل كبير لدراسات نُشر سنة 2023 لقى إنو التمارين الثابتة كانت من أقوى الأنواع لتنزيل الضغط. أشهرها «القعدة عالحيط» (<bdi>Wall Sit</bdi>): بتسند ضهرك عالحيط وبتنزل كأنك قاعد على كرسي وهمي. تقريباً 4 جولات كل وحدة دقيقتين، مع دقيقتين راحة بيناتهن، 3 مرات بالأسبوع. وكمان تمرين الضغط على قبضة اليد (<bdi>Handgrip</bdi>).</p>
            <div class="tip warn"><p><strong>انتبه:</strong> إذا ضغطك <bdi>180 / 110</bdi> أو أكتر، أو عندك مشكلة بالقلب، احكي مع طبيبك قبل ما تبلش. ووقت التمرين لا تحبس نفسك (<bdi>Valsalva Maneuver</bdi>)، كمّل تنفس طبيعي. وبلّش بشوي، لأنو الاستمرارية أهم من الحماس بأول أسبوع.</p></div>

            <h2 class="section-title"><i class="fas fa-moon"></i> <span>النوم: الورشة الليلية لشرايينك</span></h2>
            <p>بالليل، وبالحالة الطبيعية، الضغط بينزل تقريباً 10 لـ20% عن النهار. هالشي اسمه الهبوط الليلي (<bdi>Nocturnal Dipping</bdi>)، وهاي فرصة الشرايين لترتاح وتصلّح حالها. لما تنام قليل أو نومك متقطع، هالورشة بتتسكّر، والجهاز السمبثاوي بيضل شغّال طول الليل.</p>
            <p>الناس اللي بتنام أقل من 6 ساعات بشكل منتظم، خطر الضغط عندها أعلى بشكل واضح. الهدف 7 لـ9 ساعات.</p>
            <h3>انقطاع النفس الانسدادي أثناء النوم (<bdi>Obstructive Sleep Apnea</bdi>)</h3>
            <p>هاد من أهم الأسباب المخفية للضغط، وخصوصاً الضغط اللي ما عم يستجيب للأدوية. القصة إنو مجرى التنفس بيتسكّر لثواني كتير مرات بالليل، الأكسجين بينزل، والجسم بيفيق مرعوب وبيضخ أدرينالين. تخيّل هالشي يصير عشرات المرات بالليل.</p>
            <p>شك فيه إذا:</p>
            <ul class="check-list">
                <li>شخيرك عالي، أو حدا قلّك إنك بتوقف تتنفس وانت نايم</li>
                <li>بتفيق تعبان حتى لو نمت 8 ساعات، وبتغفى بالنهار</li>
                <li>صداع الصبح وجفاف الحلق</li>
            </ul>
            <p>إذا هالكلام بيشبهك، احكي مع طبيبك عن دراسة النوم (<bdi>Sleep Study</bdi>). العلاج بجهاز الضغط الهوائي (<bdi>CPAP</bdi>) ونزول الوزن ممكن يحسّن الضغط بشكل ملحوظ.</p>
            <h3>نصايح سريعة لنوم أحسن</h3>
            <ul class="check-list">
                <li>نام وفيق بنفس الوقت تقريباً كل يوم، حتى بالعطلة</li>
                <li>لا قهوة بعد الساعة 2 الضهر</li>
                <li>شاشات أقل بالساعة الأخيرة قبل النوم، والغرفة عتمة وباردة</li>
                <li>العشا الخفيف وقبل النوم بساعتين لتلاتة</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-spa"></i> <span>الراحة النفسية: لما الأعصاب «تفقع»… الضغط كمان</span></h2>
            <p>التوتر المزمن (<bdi>Chronic Stress</bdi>) بيخلي الجسم يفرز <a href="{site:/cortisol-stress.html}">الكورتيزول</a> (<bdi>Cortisol</bdi>) والأدرينالين (<bdi>Adrenaline</bdi>) بشكل مستمر. الكورتيزول بيرفع السكر وبيزيد مقاومة الإنسولين، والأدرينالين بيضيّق الشرايين وبيسرّع القلب. يعني رجعنا لنفس الحلقة: الجهاز السمبثاوي بحالة طوارئ دائمة.</p>
            <p>الحل إنو نشغّل الفرامل. عندك بالجسم جهاز معاكس اسمه الجهاز العصبي اللاودّي (<bdi>Parasympathetic Nervous System</bdi>)، وأهم كابل فيه هو العصب المبهم (<bdi>Vagus Nerve</bdi>). وفي طرق بسيطة كتير بتشغّلو:</p>
            <h3>التنفس البطيء (<bdi>Slow Breathing</bdi>)</h3>
            <p>شهيق 5 ثواني من الأنف، وزفير 5 ثواني بهدوء. يعني تقريباً 6 أنفاس بالدقيقة، لمدة 5 لـ10 دقايق، مرة أو مرتين باليوم. جرّبها وقيس ضغطك قبل وبعد، رح تحس بالـ«انبساطي»، بس هالمرة من الفرح 😄</p>
            <h3>شغلات تانية بتفرق</h3>
            <ul class="check-list">
                <li>مشوار بالطبيعة أو قعدة بالشمس الصبح</li>
                <li>التأمل (<bdi>Meditation</bdi>) أو الصلاة أو أي ممارسة روحية بتريّحك</li>
                <li>قعدة حلوة مع ناس بتحبهن، لأنو الوحدة لحالها عامل خطر</li>
                <li>تقليل الأخبار والسوشيال ميديا قبل النوم</li>
                <li>إذا التوتر أو القلق صار تقيل وما عم تقدر تحملو، الحكي مع مختص نفسي مش ضعف، هاد جزء من علاج الضغط كمان</li>
            </ul>
            <h3>والتدخين؟</h3>
            <p>كل سيجارة بترفع الضغط لمدة تقريباً نص ساعة بعدها، وبتأذي بطانة الشرايين مباشرة. والأركيلة مش أرحم. <strong>إذا بدك تعمل شي واحد بس لشرايينك، وقّف الدخان.</strong></p>

            <h2 class="section-title"><i class="fas fa-list-check"></i> <span>الخطة باختصار: من بكرا الصبح</span></h2>
            <ul class="todo-list">
                <li><label><input type="checkbox"><span>اشتري جهاز ضغط عالزند وقيس صح لمدة أسبوع</span></label></li>
                <li><label><input type="checkbox"><span>اعمل تحاليل الإنسولين والسكر والدهون والكلى</span></label></li>
                <li><label><input type="checkbox"><span>قيس محيط خصرك</span></label></li>
                <li><label><input type="checkbox"><span>نصّ صحنك خضار، وربعه بروتين، وربعه نشويات كاملة</span></label></li>
                <li><label><input type="checkbox"><span>اقرأ ملصق الصوديوم على كل شي معلّب أو جاهز</span></label></li>
                <li><label><input type="checkbox"><span>امشي نص ساعة 5 أيام بالأسبوع، وزيد عليها «القعدة عالحيط» 3 مرات</span></label></li>
                <li><label><input type="checkbox"><span>نام 7 ساعات عالأقل، وانتبه للشخير</span></label></li>
                <li><label><input type="checkbox"><span>5 دقايق تنفس بطيء كل يوم</span></label></li>
                <li><label><input type="checkbox"><span>راجع طبيبك بالنتايج بعد 3 أشهر</span></label></li>
            </ul>

            <h2 class="section-title"><i class="fas fa-flag-checkered"></i> <span>وبالأخير…</span></h2>
            <p>ارتفاع الضغط مش حكم مؤبد، ومش رقم بيطلع فجأة من العدم. هو رسالة من جسمك إنو في شي بالأيض والشرايين بدو انتباه. والحلو بالموضوع إنو كل خطوة صغيرة، كل مشوار وكل صحن سلطة وكل ليلة نوم منيحة، عم تنقصّ من رقم الضغط وتزيد على عمر شرايينك.</p>
            <p>فما تستنى «القاتل الصامت» يحكي. <strong>إنت احكي أول، وقيس ضغطك اليوم.</strong></p>
            <p>قلبك الصغير رح يشكرك… بوم… بوم… بوم. بس هالمرة بهدوء.</p>'''),
en=dict(
 byline='By Dr. Wassim Habib',
 title='High Blood Pressure and Sugar: The Hidden Insulin Link',
 h1='Believe It or Not: Sugar Is Raising Your Blood Pressure… Not Just Salt!',
 subtitle='High blood pressure, the silent killer: its causes, its link to insulin, and how to protect your arteries',
 crumb='High blood pressure and sugar',
 summary='High blood pressure but you hardly eat salt? Look for the sugar: how insulin raises blood pressure, how to measure it at home, and a food, exercise and sleep plan for your arteries.',
 cat='Heart & blood vessels',
 desc='Salt isn\'t the only cause of high blood pressure. Learn how insulin resistance pushes it up, what to eat, and how to protect your arteries.',
 hero_alt='Worried woman checking her blood pressure with an upper-arm monitor, next to a salt shaker, a sweetened iced coffee and a chocolate dessert, with a shadow made of sugar cubes behind her',
 about=['Hypertension', 'Insulin resistance', 'Blood pressure', 'DASH diet'],
 disclaimer='⚖️ This article is for health awareness and education and does not replace advice from your doctor. Never stop or change any medication without talking to your doctor first.',
 body='''            <p class="lead">Ever wondered why modern medicine calls it "the silent killer"? If not, let me tell you the real reason: it creeps quietly into your arteries and the tissues of your vital organs and damages them step by step, without a single twinge of pain, until the problem is well advanced.</p>
            <p>High blood pressure doesn't start out as some lonely, orphaned disease with no family tree. In reality it is a direct reflection of a metabolic dysfunction inside your body and of ongoing inflammation in the lining of your blood vessels.</p>
            <p>In this article we'll untangle the mystery calmly and without medical jargon: we'll break down the numbers, explain how <a href="{site:/insulin-resistance.html}">insulin resistance</a> is tightly linked to high blood pressure, and put together a complete plan to bring flexibility and life back to your arteries… and to protect that poor little heart of yours, which really can't take much more.</p>

            <h2 class="section-title"><i class="fas fa-heart-pulse"></i> <span>What is blood pressure, and what do the numbers mean?</span></h2>
            <p>Every time your heart goes ba-boom, it pumps blood through a complex network of blood vessels. So write this down in biiig bold letters: <strong>blood pressure is the force of the blood pushing against the walls of your arteries as it flows</strong>. In short, it's how hard the walls are pushing back against the stream.</p>
            <p>The pressure created at the very moment your heart pumps is called the <strong>systolic blood pressure</strong>. Got it? Simply put, it's the big number, the one on top. Remember its name: systolic.</p>
            <p>Once the heart has pushed its blood out, it needs to relax and rest so it can fill up again. That's where the <strong>diastolic blood pressure</strong> comes in. And no, "diastolic" has nothing to do with being ecstatic: it means relaxing and expanding, the heart's little rest between one beat and the next. During this pause we measure the pressure inside the arteries while the heart refills and then does it all over again: ba-boom… ba-boom… ba-boom… ba-boom. Easy, right?</p>
            <h3>How do we know whether blood pressure is normal or starting to flash warning lights?</h3>
            <table class="bp-table">
                <thead><tr><th>Category</th><th>Systolic</th><th></th><th>Diastolic</th><th>What does it mean?</th></tr></thead>
                <tbody>
                    <tr class="bp-ok"><td>Normal and ideal</td><td class="bp-num" data-label="Systolic">below 120</td><td class="bp-op">and</td><td class="bp-num" data-label="Diastolic">below 80</td><td>Flexible blood vessels and a heart working completely at ease</td></tr>
                    <tr class="bp-elev"><td>Elevated: the early-warning stage</td><td class="bp-num" data-label="Systolic">120–129</td><td class="bp-op">and</td><td class="bp-num" data-label="Diastolic">below 80</td><td>Vessels are starting to stiffen: time to change your lifestyle right away</td></tr>
                    <tr class="bp-s1"><td>Stage 1 hypertension</td><td class="bp-num" data-label="Systolic">130–139</td><td class="bp-op">or</td><td class="bp-num" data-label="Diastolic">80–89</td><td>This is now a diagnosis; your doctor decides based on your other risk factors</td></tr>
                    <tr class="bp-s2"><td>Stage 2 hypertension</td><td class="bp-num" data-label="Systolic">140 or higher</td><td class="bp-op">or</td><td class="bp-num" data-label="Diastolic">90 or higher</td><td>Needs regular medical follow-up and often medication</td></tr>
                </tbody>
            </table>
            <p class="table-note">All values in millimetres of mercury (mmHg).</p>
            <div class="danger-box">
                <h3>🚨 Red-flag warning signs (an emergency)</h3>
                <p>If your monitor shows a reading above 180/120 mmHg together with a sudden, severe headache, blurred vision, shortness of breath, chest pain, weakness in an arm or leg, or difficulty speaking, this is not the moment to start tweaking your diet. It is a medical emergency (a hypertensive emergency) and you need to <strong>go to the nearest hospital or call an ambulance immediately</strong>.</p>
            </div>

            <h2 class="section-title"><i class="fas fa-user-secret"></i> <span>The silent killer has a secret accomplice… meet it before it meets you 😉</span></h2>
            <p>This is the most important point of today's topic, and the one people most often miss. High blood pressure, but you hardly touch the salt? Look for the sugar! Most people believe blood pressure goes up only because of too much salt. But, my friends, the truth runs much deeper, and the real culprit isn't who you think it is. Let's put all the cards on the table: <strong>sugar drives up insulin, and insulin is the hidden lead character of this story.</strong> So let's let insulin spill the beans:</p>
            <h3>1. Sodium retention in the kidneys</h3>
            <figure class="article-figure">
                <img src="/images/sodium-water-retention-blood-vessel-hypertension.webp" alt="Illustration of a cross-section of a blood vessel full of red blood cells, sodium ions and water molecules, with signals reaching the kidney to retain sodium, increasing blood volume and pressure on the artery wall" width="1200" height="896" loading="lazy" decoding="async">
                <figcaption>High insulin tells the kidneys to hold on to sodium; sodium pulls water into the blood with it, so the pressure on the artery walls rises.</figcaption>
            </figure>
            <p>Chronically high levels of insulin in the blood (hyperinsulinaemia) send direct signals, straight to the point, telling the kidneys to reabsorb sodium instead of letting it leave in the urine. And wherever sodium goes, water follows. The total volume of blood inside your arteries goes up, and so does the pressure on them.</p>
            <h3>2. An overstimulated sympathetic nervous system</h3>
            <p>Excess insulin keeps the sympathetic nervous system on permanent high alert, as if there were a burglar in the house 24/7. The result? Narrowing of the blood vessels (vasoconstriction) and a faster beat from that sweet little heart of yours.</p>
            <h3>3. The vessel lining loses its flexibility (endothelial dysfunction)</h3>
            <p>Normally the lining of your arteries releases a tiny, magical gas called nitric oxide, whose job is to widen the arteries and keep them soft and supple. Once insulin resistance sets in, nitric oxide production drops and chronic low-grade inflammation starts eating away at the lining. An artery that used to be like soft rubber becomes like an old garden hose that has been baking in the sun for years.</p>
            <h3>4. The renin–angiotensin–aldosterone system (RAAS)</h3>
            <p>This is a hormonal system that regulates blood pressure and fluids in the body. With insulin resistance and excess body fat it starts working overtime: angiotensin II narrows the arteries and aldosterone holds on to even more sodium. A double whammy.</p>
            <h3>5. Visceral fat: not just a belly</h3>
            <p>The fat packed around the organs deep inside your abdomen is not a quiet energy store. It is active tissue that releases inflammatory substances (cytokines) and also produces the raw material for angiotensin. That's why your waist circumference can sometimes tell you more about your blood pressure risk than the number on the scale. (Read more about <a href="/en/articles/fatty-liver-and-visceral-fat.html">visceral fat and fatty liver</a>.)</p>
            <h3>So, are there other causes?</h3>
            <p>Of course. They include genetics and age, salt sensitivity (which varies from person to person), sleep apnoea (more on that later), smoking, alcohol, and some medicines such as anti-inflammatory painkillers (NSAIDs), decongestant nasal sprays and, in some women, the contraceptive pill.</p>
            <p>There is also a type called secondary hypertension, where a clear underlying cause is to blame, such as kidney disease or a thyroid or adrenal problem. Doctors think of it especially when high blood pressure appears at a young age, or when it is very high and isn't responding to treatment.</p>

            <h2 class="section-title"><i class="fas fa-stethoscope"></i> <span>So how would I feel it? Here comes the surprise</span></h2>
            <p>In most cases you feel nothing at all. No pain, no warning. And that is exactly where the nickname "silent killer" comes from. Some people live for years with a blood pressure of 150, convinced they're made of steel.</p>
            <p>Sometimes, especially when blood pressure is very high, you may notice things like:</p>
            <ul class="check-list">
                <li>A morning headache, often at the back of the head</li>
                <li>Dizziness or ringing in the ears (tinnitus)</li>
                <li>Palpitations or being aware of your heartbeat</li>
                <li>General tiredness and trouble concentrating</li>
            </ul>
            <p>But be careful: these symptoms are not a yardstick. Having no symptoms doesn't mean your blood pressure is fine. And the popular line "my blood pressure is up because my head hurts" is often the other way round: the pain and stress pushed the pressure up temporarily. <strong>The only judge is the blood pressure monitor.</strong></p>

            <h2 class="section-title"><i class="fas fa-house-medical"></i> <span>How to measure your blood pressure at home like a pro</span></h2>
            <p>A single reading at the clinic sometimes lies. There's something called white coat hypertension: the moment you see the doctor, your pressure shoots up. And there's the opposite too, masked hypertension: perfectly fine at the clinic, high at home and at work. That's why home blood pressure monitoring is worth its weight in gold.</p>
            <h3>How to do it right:</h3>
            <ol class="steps">
                <li>Use an upper-arm cuff monitor, not a wrist one, and make sure the cuff is the right size for your arm.</li>
                <li>No coffee, smoking or exercise for half an hour before measuring, and empty your bladder.</li>
                <li>Sit on a chair with your back supported and both feet flat on the floor, legs uncrossed, and rest for 5 minutes.</li>
                <li>Rest your arm on a table at heart level, with the cuff directly on your skin, not over your jumper.</li>
                <li>Don't talk or look at your phone while measuring.</li>
                <li>Take two readings one minute apart and write down the average.</li>
                <li>Repeat this morning and evening for a week, and take the log with you to your doctor.</li>
            </ol>
            <p>If your average home reading comes out at 130/80 or higher, that's a sign you should talk to your doctor about it. Under the European guidelines (ESC 2024), the home threshold is 135/85.</p>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>On the edge of high blood pressure: what now?</span></h2>
            <p>If your readings are now between 120 and 139, or your diastolic is hovering around 80, this is no time to panic, but it's not the time for "we'll see tomorrow" either. This is the best possible stage to step in, because your arteries are still flexible and your body responds quickly.</p>
            <h3>Step one: find out what's going on inside</h3>
            <p>Ask your doctor for these tests, because they reveal whether the story is linked to insulin and metabolism:</p>
            <ul class="check-list">
                <li>Fasting glucose and HbA1c</li>
                <li>Fasting insulin, which is used to calculate the insulin resistance index (HOMA-IR)</li>
                <li>A lipid profile, especially triglycerides and "good" HDL cholesterol</li>
                <li>Kidney function (creatinine, eGFR) and urine albumin</li>
                <li>Blood sodium and potassium, and thyroid hormone (TSH)</li>
            </ul>
            <p>Also measure your waist at the level of your belly button. As a general rule, more than <strong>94 cm in men</strong> and more than <strong>80 cm in women</strong> points to visceral fat. You can also work out your <a href="{site:/whtr-calculator.html}">waist-to-height ratio</a> in seconds. And if your blood sugar results are borderline, read our guide to <a href="/en/diabetes/prediabetes.html">prediabetes</a>.</p>
            <h3>Step two: give your lifestyle 3 to 6 months of serious effort</h3>
            <p>In the early-warning stage, and in many stage 1 cases without other risk factors, doctors start with lifestyle changes. Don't underestimate them: every kilo of excess weight you lose lowers blood pressure by about 1 mmHg. Healthy eating alone can bring systolic pressure down by 8 to 11 mmHg in many people. Sometimes that's as much as a pill.</p>
            <div class="tip warn"><p><strong>But careful:</strong> if your doctor has prescribed medication, don't stop it on your own because you read a nice article. Nutrition and exercise work alongside the medicine, and it's your doctor who decides whether you can cut it down over time.</p></div>

            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>Your plate is your pharmacy: the foods that help</span></h2>
            <p>Two eating patterns have been well studied for blood pressure: the DASH diet, literally "Dietary Approaches to Stop Hypertension", and the Mediterranean diet. The good news? Both are built on simple, natural food, very close to what our grandmothers cooked all over the world before fast food invaded our lives.</p>
            <h3>Potassium: sodium's arch-rival</h3>
            <p>Potassium helps the kidneys get rid of sodium and relaxes the walls of the blood vessels. You'll find it in:</p>
            <ul class="check-list">
                <li><a href="{food:spinach}">Spinach</a>, <a href="{food:swiss-chard}">Swiss chard</a>, <a href="{food:molokhia}">molokhia</a> and parsley</li>
                <li><a href="{food:avocado}">Avocado</a>, <a href="{food:banana}">bananas</a> and <a href="{food:dried-apricots}">dried apricots</a></li>
                <li>Pulses: <a href="{food:lentils}">lentils</a>, <a href="{food:white-beans}">beans</a> and <a href="{food:chickpeas}">chickpeas</a></li>
                <li><a href="{food:sweet-potato}">Sweet potatoes</a> and ordinary <a href="{food:boiled-potato}">potatoes boiled</a> in their skins</li>
                <li>Plain yogurt and low-salt <a href="{food:labneh}">labneh</a></li>
            </ul>
            <div class="tip warn"><p><strong>Important:</strong> if you have kidney disease, or you take blood pressure medicines or diuretics, talk to your doctor before you increase your potassium or use salt substitutes.</p></div>
            <h3>Magnesium: the king of relaxation</h3>
            <p>It helps the smooth muscle in the artery walls relax, and studies link magnesium to better insulin sensitivity. Find it in <a href="{food:pumpkin-seeds}">pumpkin seeds</a>, almonds and <a href="{food:cashews}">cashews</a>, leafy greens and <a href="{food:dark-chocolate-85}">85% dark chocolate</a> (two squares, not the whole bar, deal?).</p>
            <h3>Dietary nitrates: beetroot and rocket</h3>
            <p>Here's where the nitric oxide story comes back. <a href="{food:beetroot}">Beetroot</a>, <a href="{food:arugula-rocket}">rocket</a> and spinach are rich in nitrates, which the body turns into nitric oxide, so the arteries widen. A glass of beetroot juice or a plate of rocket salad a day is a lovely habit.</p>
            <h3>Fibre and less sugar: to bring insulin down</h3>
            <p>Since insulin is the hidden lead character of this story, we need to calm it down (you'll find the glycaemic index of every food in our <a href="{site:/foods.html}">food guide</a>):</p>
            <ul class="check-list">
                <li><a href="{food:oatmeal}">Oats</a>, <a href="{food:bulgur}">bulgur</a> and <a href="{food:whole-wheat-bread}">real wholemeal bread</a> instead of white</li>
                <li>Vegetables with every meal, and start your meal with the salad</li>
                <li>Protein with every meal: <a href="{food:boiled-egg}">eggs</a>, fish, <a href="{food:grilled-chicken-breast}">chicken</a>, pulses</li>
            </ul>
            <h3>Healthy fats</h3>
            <p><a href="{food:extra-virgin-olive-oil}">Extra virgin olive oil</a>, oily fish such as <a href="{food:grilled-salmon}">salmon</a>, <a href="{food:canned-sardines}">sardines</a> and <a href="{food:mackerel}">mackerel</a> twice a week for omega-3, and <a href="{food:walnuts}">walnuts</a>.</p>
            <h3>Kitchen staples with reasonable scientific support</h3>
            <ul class="check-list">
                <li><strong>Hibiscus tea:</strong> some studies found it lowers blood pressure slightly; two or three cups a day, without sugar.</li>
                <li><strong><a href="{food:garlic}">Garlic</a>:</strong> has a small but useful effect.</li>
            </ul>
            <p>But there is no magic herb that replaces your medication or fixes an unhealthy lifestyle.</p>

            <h2 class="section-title"><i class="fas fa-ban"></i> <span>The foods we need to put on "block"</span></h2>
            <h3>Hidden sodium: the enemy you can't see</h3>
            <p>So, is salt innocent? Not at all. It's a partner in crime, it just doesn't act alone. Want to know a secret? Most of the salt we eat doesn't come from the salt shaker on the table. More than 70% of it comes from ready-made and processed food. The goal is to stay below <strong>2,000 mg of sodium a day</strong>, roughly one teaspoon of salt (5 grams) from all sources combined.</p>
            <p>Watch out for:</p>
            <ul class="check-list">
                <li>Bread and pastries: they don't taste salty, but they contain plenty</li>
                <li>Salty cheeses such as <a href="{food:halloumi-cheese}">halloumi</a>, <a href="{food:greek-feta}">feta</a> and parmesan</li>
                <li><a href="{food:pickled-cucumbers-gherkins}">Pickles</a> and olives</li>
                <li>Processed meats such as sausages, hot dogs and bacon</li>
                <li>Stock cubes and ready-made soups</li>
                <li>Crisps, salted nuts and sauces such as <a href="{food:naturally-brewed-soy-sauce}">soy sauce</a> and ketchup</li>
                <li>Restaurant food and fast food</li>
            </ul>
            <div class="tip"><p><strong>A little label-reading trick:</strong> if the label lists sodium, multiply it by 2.5 to get the amount of salt. So 400 mg of sodium = 1 gram of salt.</p></div>
            <h3>Sugar and refined carbs: the answer is in the dessert bowl, not the salt shaker</h3>
            <p>Since insulin is the key, soft drinks, packaged juices, sweets and lots of white bread all push insulin up and feed the story we've just told. Added fructose (high-fructose corn syrup) in particular is linked to higher uric acid and higher blood pressure.</p>
            <h3>Liquorice: in drinks, desserts and sweets</h3>
            <p>This is something many people don't know. <a href="{food:licorice-drink}">Liquorice</a> contains a substance called glycyrrhizin, which behaves like aldosterone: it holds on to sodium, flushes out potassium and raises blood pressure. So if your blood pressure is borderline, cut back on liquorice drinks and sweets.</p>
            <h3>Alcohol and energy drinks</h3>
            <p>Alcohol, even in "social" amounts, raises blood pressure over time. Energy drinks, with their high doses of caffeine and sugar, can push it up suddenly. As for regular <a href="{food:black-coffee}">coffee</a>, one or two cups a day is usually not a problem for most people.</p>

            <h2 class="section-title"><i class="fas fa-person-walking"></i> <span>Exercise: the medicine that costs nothing</span></h2>
            <p>Exercise works on several fronts at once: it improves insulin sensitivity, calms the sympathetic nervous system, increases nitric oxide release and reduces visceral fat. In other words, it tackles the story at its roots.</p>
            <h3>Aerobic exercise</h3>
            <p>Brisk walking, swimming, cycling: <strong>150 minutes a week</strong>, that is half an hour on 5 days. That alone can lower systolic pressure by 5 to 8 mmHg. And a golden tip: a 10 to 15-minute walk after a meal brings blood sugar and insulin down beautifully.</p>
            <h3>Resistance training</h3>
            <p>Weights, resistance bands or your own body weight: two to three times a week. Muscles are the body's biggest consumer of sugar, and the more muscle you have, the less insulin you need.</p>
            <h3>The surprise: isometric exercise</h3>
            <p>A large analysis of studies published in 2023 found that isometric (static) exercise was among the most effective types for lowering blood pressure. The best known is the wall sit: lean your back against a wall and slide down as if sitting on an invisible chair. Roughly 4 rounds of 2 minutes each, with two minutes' rest in between, 3 times a week. Handgrip squeezes work too.</p>
            <div class="tip warn"><p><strong>Careful:</strong> if your blood pressure is 180/110 or higher, or you have a heart condition, talk to your doctor before you start. Don't hold your breath while exercising (the Valsalva manoeuvre); keep breathing normally. And start small, because consistency matters more than enthusiasm in week one.</p></div>

            <h2 class="section-title"><i class="fas fa-moon"></i> <span>Sleep: the night-time repair shop for your arteries</span></h2>
            <p>At night, under normal circumstances, blood pressure drops by about 10 to 20% compared with the daytime. This is called nocturnal dipping, and it's your arteries' chance to rest and repair themselves. When you sleep too little or your sleep is broken, the repair shop closes and the sympathetic nervous system stays switched on all night.</p>
            <p>People who regularly sleep less than 6 hours have a clearly higher risk of high blood pressure. The goal is 7 to 9 hours.</p>
            <h3>Obstructive sleep apnoea</h3>
            <p>This is one of the most important hidden causes of high blood pressure, especially blood pressure that won't respond to medication. The airway closes for several seconds, many times a night, oxygen levels drop, and the body wakes up in a panic and pumps out adrenaline. Imagine that happening dozens of times every night.</p>
            <p>Suspect it if:</p>
            <ul class="check-list">
                <li>You snore loudly, or someone has told you that you stop breathing in your sleep</li>
                <li>You wake up tired even after 8 hours of sleep, and nod off during the day</li>
                <li>You have morning headaches and a dry throat</li>
            </ul>
            <p>If this sounds like you, ask your doctor about a sleep study. Treatment with a CPAP machine and weight loss can noticeably improve blood pressure.</p>
            <h3>Quick tips for better sleep</h3>
            <ul class="check-list">
                <li>Go to bed and get up at roughly the same time every day, even at weekends</li>
                <li>No coffee after 2 pm</li>
                <li>Less screen time in the last hour before bed, and keep the room dark and cool</li>
                <li>A light dinner, two to three hours before bedtime</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-spa"></i> <span>Peace of mind: when your nerves snap… so does your blood pressure</span></h2>
            <p>Chronic stress makes the body release <a href="{site:/cortisol-stress.html}">cortisol</a> and adrenaline non-stop. Cortisol raises blood sugar and increases insulin resistance; adrenaline narrows the arteries and speeds up the heart. So we're back in the same loop: a sympathetic nervous system in a permanent state of emergency.</p>
            <p>The solution is to hit the brakes. Your body has an opposing system called the parasympathetic nervous system, and its most important cable is the vagus nerve. There are very simple ways to switch it on:</p>
            <h3>Slow breathing</h3>
            <p>Breathe in through your nose for 5 seconds and out calmly for 5 seconds. That's about 6 breaths a minute, for 5 to 10 minutes, once or twice a day. Try it and measure your blood pressure before and after: you'll feel truly diastolic, relaxed, and this time a little ecstatic too 😄</p>
            <h3>Other things that make a difference</h3>
            <ul class="check-list">
                <li>A walk in nature or sitting in the morning sun</li>
                <li>Meditation, prayer or any spiritual practice that brings you peace</li>
                <li>Quality time with people you love, because loneliness is a risk factor in itself</li>
                <li>Less news and social media before bed</li>
                <li>If stress or anxiety has become too heavy to carry, talking to a mental health professional is not a weakness; it's part of treating blood pressure too</li>
            </ul>
            <h3>And smoking?</h3>
            <p>Every cigarette raises blood pressure for about half an hour afterwards and directly damages the lining of the arteries. And shisha is no kinder. <strong>If you do just one thing for your arteries, stop smoking.</strong></p>

            <h2 class="section-title"><i class="fas fa-list-check"></i> <span>The plan in a nutshell: starting tomorrow morning</span></h2>
            <ul class="todo-list">
                <li><label><input type="checkbox"><span>Buy an upper-arm blood pressure monitor and measure correctly for a week</span></label></li>
                <li><label><input type="checkbox"><span>Get your insulin, blood sugar, lipids and kidney function tested</span></label></li>
                <li><label><input type="checkbox"><span>Measure your waist</span></label></li>
                <li><label><input type="checkbox"><span>Fill half your plate with vegetables, a quarter with protein and a quarter with whole-grain carbs</span></label></li>
                <li><label><input type="checkbox"><span>Read the sodium label on everything canned or ready-made</span></label></li>
                <li><label><input type="checkbox"><span>Walk for half an hour 5 days a week, and add the wall sit 3 times a week</span></label></li>
                <li><label><input type="checkbox"><span>Sleep at least 7 hours, and pay attention to snoring</span></label></li>
                <li><label><input type="checkbox"><span>5 minutes of slow breathing every day</span></label></li>
                <li><label><input type="checkbox"><span>See your doctor with the results after 3 months</span></label></li>
            </ul>

            <h2 class="section-title"><i class="fas fa-flag-checkered"></i> <span>And finally…</span></h2>
            <p>High blood pressure is not a life sentence, and it isn't a number that appears out of nowhere. It's a message from your body that something in your metabolism and arteries needs attention. The good news is that every small step, every walk, every plate of salad and every good night's sleep chips away at your blood pressure and adds years to the life of your arteries.</p>
            <p>So don't wait for the "silent killer" to speak up. <strong>You speak first: measure your blood pressure today.</strong></p>
            <p>Your little heart will thank you… ba-boom… ba-boom… ba-boom. Only this time, nice and calm.</p>'''),
nl=dict(
 byline='Door Dr. Wassim Habib',
 title='Hoge bloeddruk en suiker: het verborgen verband met insuline',
 h1='Geloof het of niet: suiker jaagt je bloeddruk omhoog… niet alleen zout!',
 subtitle='Hoge bloeddruk, de stille moordenaar: de oorzaken, het verband met insuline en hoe je je bloedvaten beschermt',
 crumb='Hoge bloeddruk en suiker',
 summary='Hoge bloeddruk terwijl je bijna geen zout eet? Zoek het bij de suiker: hoe insuline je bloeddruk verhoogt, hoe je thuis goed meet en een plan voor eten, bewegen en slapen.',
 cat='Hart en bloedvaten',
 desc='Zout is niet de enige oorzaak van hoge bloeddruk. Ontdek hoe insuline je bloeddruk verhoogt, wat je beter kunt eten en hoe je je bloedvaten beschermt.',
 hero_alt='Bezorgde vrouw meet haar bloeddruk met een bovenarmmeter, naast een zoutvaatje, een gezoete ijskoffie en een chocoladedessert, met achter haar een schaduw van suikerklontjes',
 about=['Hypertension', 'Insulin resistance', 'Blood pressure', 'DASH diet'],
 disclaimer='⚖️ Dit artikel is bedoeld als gezondheidsvoorlichting en vervangt geen advies van je arts. Stop nooit met een medicijn en pas het niet aan zonder overleg met je arts.',
 body='''            <p class="lead">Heb je je ooit afgevraagd waarom de moderne geneeskunde het "de stille moordenaar" noemt? Weet je het niet, dan vertel ik je de echte reden: het sluipt ongemerkt je slagaders en de weefsels van je vitale organen binnen en beschadigt ze stap voor stap, zonder dat je ook maar iets voelt, tot het probleem al flink gevorderd is.</p>
            <p>Hoge bloeddruk begint niet als een eenzame ziekte zonder vader of moeder. In werkelijkheid is het een directe weerspiegeling van een stofwisselingsstoornis (metabole disfunctie) in je lichaam en van aanhoudende ontsteking in de binnenwand van je bloedvaten.</p>
            <p>In dit artikel ontrafelen we samen dat raadsel, rustig en zonder medisch jargon: we nemen de getallen onder de loep, leggen uit hoe <a href="{site:/insulin-resistance.html}">insulineresistentie</a> nauw samenhangt met hoge bloeddruk, en maken samen een compleet plan om je slagaders weer soepel en vitaal te maken… en om dat kleine hartje van je te beschermen, dat echt niet veel meer aankan.</p>

            <h2 class="section-title"><i class="fas fa-heart-pulse"></i> <span>Wat is bloeddruk, en wat betekenen de getallen?</span></h2>
            <p>Elke keer dat je hart boem-boem doet, pompt het bloed door een ingewikkeld netwerk van bloedvaten. Schrijf dit dus in héééle dikke letters op: <strong>bloeddruk is de kracht waarmee het bloed tegen de wanden van je slagaders duwt terwijl het stroomt</strong>. Kort gezegd: hoe hard de wanden tegendruk geven aan de bloedstroom.</p>
            <p>De druk die ontstaat op het moment dat je hart pompt, noemen we de <strong>systolische bloeddruk</strong>, ook wel de bovendruk. Duidelijk? Simpel gezegd is het het grote getal, het getal bovenaan. Onthoud die naam goed: systolisch.</p>
            <p>Nadat het hart zijn bloed heeft weggepompt, moet het ontspannen en rusten om zich weer te vullen. Daar komt de <strong>diastolische bloeddruk</strong> (de onderdruk) om de hoek kijken. En nee, diastolisch heeft niets met "fantastisch" te maken: het betekent ontspannen en uitzetten, het rustmomentje van het hart tussen twee slagen. In die pauze meten we de druk in de slagaders, terwijl het hart zich opnieuw vult en alles herhaalt: boem… boem… boem… boem. Makkelijk, toch?</p>
            <h3>Hoe weet je of je bloeddruk normaal is of al waarschuwingssignalen geeft?</h3>
            <table class="bp-table">
                <thead><tr><th>Categorie</th><th>Systolisch (bovendruk)</th><th></th><th>Diastolisch (onderdruk)</th><th>Wat betekent het?</th></tr></thead>
                <tbody>
                    <tr class="bp-ok"><td>Normaal en ideaal</td><td class="bp-num" data-label="Systolisch">lager dan 120</td><td class="bp-op">en</td><td class="bp-num" data-label="Diastolisch">lager dan 80</td><td>Soepele bloedvaten en een hart dat helemaal ontspannen werkt</td></tr>
                    <tr class="bp-elev"><td>Verhoogd: de fase van de vroege waarschuwing</td><td class="bp-num" data-label="Systolisch">120–129</td><td class="bp-op">en</td><td class="bp-num" data-label="Diastolisch">lager dan 80</td><td>De vaten beginnen te verstijven: tijd om je leefstijl meteen aan te pakken</td></tr>
                    <tr class="bp-s1"><td>Hypertensie, stadium 1</td><td class="bp-num" data-label="Systolisch">130–139</td><td class="bp-op">of</td><td class="bp-num" data-label="Diastolisch">80–89</td><td>Nu is er een diagnose; je arts beslist op basis van je andere risicofactoren</td></tr>
                    <tr class="bp-s2"><td>Hypertensie, stadium 2</td><td class="bp-num" data-label="Systolisch">140 of hoger</td><td class="bp-op">of</td><td class="bp-num" data-label="Diastolisch">90 of hoger</td><td>Vraagt om regelmatige medische controle en vaak om medicijnen</td></tr>
                </tbody>
            </table>
            <p class="table-note">Alle waarden in millimeter kwik (mmHg).</p>
            <div class="danger-box">
                <h3>🚨 Rode vlaggen (direct spoed)</h3>
                <p>Geeft je meter een waarde boven 180/120 mmHg, samen met plotselinge, hevige hoofdpijn, wazig zien, kortademigheid, pijn op de borst, krachtverlies in een arm of been of moeite met praten? Dan is dit niet het moment om je eten aan te passen. Dit is een medisch spoedgeval (hypertensieve crisis): <strong>ga direct naar de dichtstbijzijnde spoedeisende hulp of bel 112</strong>.</p>
            </div>

            <h2 class="section-title"><i class="fas fa-user-secret"></i> <span>De stille moordenaar heeft een geheime handlanger… leer hem kennen voordat hij jou leert kennen 😉</span></h2>
            <p>Dit is het belangrijkste punt van vandaag, en precies het punt dat vaak over het hoofd wordt gezien. Hoge bloeddruk, terwijl je bijna geen zout eet? Zoek het bij de suiker! De meeste mensen denken dat bloeddruk alleen stijgt door te veel zout. Maar beste vrienden, de waarheid gaat veel dieper, en de echte dader is niet wie je denkt. Laten we open kaart spelen: <strong>suiker drijft je insuline op, en insuline is de verborgen hoofdrolspeler van dit verhaal.</strong> Tijd dus dat insuline eens opbiecht:</p>
            <h3>1. De nieren houden natrium vast (natriumretentie)</h3>
            <figure class="article-figure">
                <img src="/images/sodium-water-retention-blood-vessel-hypertension.webp" alt="Illustratie van een doorsnede van een bloedvat vol rode bloedcellen, natriumionen en watermoleculen, met signalen naar de nier die natrium vasthoudt, waardoor het bloedvolume en de druk op de vaatwand stijgen" width="1200" height="896" loading="lazy" decoding="async">
                <figcaption>Een hoge insulinespiegel zegt de nieren natrium vast te houden; natrium trekt water mee het bloed in, waardoor de druk op de vaatwanden stijgt.</figcaption>
            </figure>
            <p>Een chronisch hoge insulinespiegel in het bloed (hyperinsulinemie) stuurt de nieren rechtstreekse signalen, zonder omwegen, om natrium terug op te nemen in plaats van het via de urine af te voeren. En waar natrium gaat, volgt water. Het totale bloedvolume in je slagaders neemt toe, en daarmee ook de druk erop.</p>
            <h3>2. Een overprikkeld sympathisch zenuwstelsel</h3>
            <p>Te veel insuline houdt het sympathische zenuwstelsel continu in de hoogste staat van paraatheid, alsof er 24 uur per dag een inbreker in huis rondloopt. Het resultaat? Vernauwde bloedvaten (vasoconstrictie) en een sneller kloppend hartje.</p>
            <h3>3. De vaatwand verliest haar soepelheid (endotheeldisfunctie)</h3>
            <p>Normaal gesproken maakt de binnenwand van je slagaders een klein, magisch gas aan: stikstofmonoxide. Dat zorgt ervoor dat je slagaders wijd, zacht en soepel blijven. Bij insulineresistentie daalt de aanmaak van stikstofmonoxide en begint een sluimerende, chronische ontsteking aan de vaatwand te knagen. Een slagader die ooit als zacht rubber was, wordt als een oude tuinslang die al jaren in de zon ligt.</p>
            <h3>4. Het renine-angiotensine-aldosteronsysteem (RAAS)</h3>
            <p>Dit hormoonsysteem regelt de bloeddruk en de vochtbalans in je lichaam. Bij insulineresistentie en overtollig lichaamsvet draait het overuren: angiotensine II vernauwt de slagaders en aldosteron houdt nog meer natrium vast. Een dubbele klap dus.</p>
            <h3>5. Visceraal vet: meer dan alleen een buikje</h3>
            <p>Het vet rond de organen diep in je buik is geen stille energievoorraad. Het is actief weefsel dat ontstekingsstoffen (cytokinen) afgeeft en ook de grondstof voor angiotensine aanmaakt. Daarom zegt je buikomvang soms meer over je risico op hoge bloeddruk dan het getal op de weegschaal. (Lees meer over <a href="/nl/articles/fatty-liver-and-visceral-fat.html">visceraal vet en leververvetting</a>.)</p>
            <h3>Zijn er nog andere oorzaken?</h3>
            <p>Zeker. Denk aan erfelijkheid en leeftijd, zoutgevoeligheid (die van persoon tot persoon verschilt), slaapapneu (daar komen we later op terug), roken, alcohol en sommige medicijnen, zoals ontstekingsremmende pijnstillers (NSAID's), neusspray tegen verstopping en bij sommige vrouwen de anticonceptiepil.</p>
            <p>Er bestaat ook secundaire hypertensie: daarbij zit er een duidelijke oorzaak achter, zoals een nierziekte of een probleem met de schildklier of de bijnieren. Artsen denken daar vooral aan als hoge bloeddruk op jonge leeftijd ontstaat, of als de bloeddruk erg hoog is en niet reageert op behandeling.</p>

            <h2 class="section-title"><i class="fas fa-stethoscope"></i> <span>Hoe merk ik het dan? En nu komt de verrassing</span></h2>
            <p>In de meeste gevallen merk je helemaal niets. Geen pijn, geen signaal. En precies daar komt de bijnaam "stille moordenaar" vandaan. Sommige mensen lopen jarenlang rond met een bovendruk van 150, in de overtuiging dat ze van staal zijn.</p>
            <p>Soms, vooral bij een erg hoge bloeddruk, kun je dingen merken als:</p>
            <ul class="check-list">
                <li>Hoofdpijn in de ochtend, vaak achter in het hoofd</li>
                <li>Duizeligheid of oorsuizen (tinnitus)</li>
                <li>Hartkloppingen of je hartslag voelen</li>
                <li>Algemene vermoeidheid en moeite met concentreren</li>
            </ul>
            <p>Maar let op: deze klachten zijn geen meetlat. Geen klachten betekent niet dat je bloeddruk in orde is. En het bekende "mijn bloeddruk is hoog, want ik heb hoofdpijn" is vaak precies andersom: de pijn en de stress hebben je bloeddruk tijdelijk opgedreven. <strong>De enige scheidsrechter is de bloeddrukmeter.</strong></p>

            <h2 class="section-title"><i class="fas fa-house-medical"></i> <span>Zo meet je je bloeddruk thuis als een pro</span></h2>
            <p>Eén meting in de spreekkamer liegt soms. Er bestaat zoiets als wittejassenhypertensie: zodra je de dokter ziet, schiet je bloeddruk omhoog. En ook het omgekeerde komt voor, gemaskeerde hypertensie: bij de dokter prima, thuis en op het werk te hoog. Daarom is thuis meten goud waard.</p>
            <h3>Zo doe je het goed:</h3>
            <ol class="steps">
                <li>Gebruik een bovenarmmeter, geen polsmeter, en zorg dat de manchet de juiste maat heeft voor je arm.</li>
                <li>Geen koffie, sigaret of sport in het halfuur vóór de meting, en ga eerst even plassen.</li>
                <li>Ga op een stoel zitten met je rug ondersteund en je voeten plat op de grond, benen niet over elkaar, en rust 5 minuten.</li>
                <li>Leg je arm op tafel ter hoogte van je hart, met de manchet direct op je huid en niet over je trui.</li>
                <li>Praat niet en kijk niet op je telefoon tijdens het meten.</li>
                <li>Doe twee metingen met een minuut ertussen en noteer het gemiddelde.</li>
                <li>Herhaal dit een week lang 's ochtends en 's avonds, en neem het overzicht mee naar je arts.</li>
            </ol>
            <p>Komt het gemiddelde van je thuismetingen uit op 130/80 of hoger? Dan is dat een reden om het met je arts te bespreken. Volgens de Europese richtlijnen (ESC 2024) ligt de grens voor thuismetingen op 135/85.</p>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>Op het randje van hoge bloeddruk: wat nu?</span></h2>
            <p>Zitten je metingen tussen 120 en 139, of schommelt je onderdruk rond de 80? Dan is het geen tijd voor paniek, maar ook niet voor "we zien morgen wel". Dit is juist de mooiste fase om in te grijpen, want je slagaders zijn nog soepel en je lichaam reageert snel.</p>
            <h3>Stap één: ontdek wat er vanbinnen gebeurt</h3>
            <p>Vraag je arts om deze bloedtests, want ze laten zien of het verhaal met insuline en je stofwisseling te maken heeft:</p>
            <ul class="check-list">
                <li>Nuchtere glucose en HbA1c</li>
                <li>Nuchtere insuline, waarmee de insulineresistentie-index (HOMA-IR) wordt berekend</li>
                <li>Een lipidenprofiel, vooral triglyceriden en het "goede" HDL-cholesterol</li>
                <li>Nierfunctie (creatinine, eGFR) en albumine in de urine</li>
                <li>Natrium en kalium in het bloed, en het schildklierhormoon TSH</li>
            </ul>
            <p>Meet ook je buikomvang ter hoogte van je navel. In het algemeen wijst meer dan <strong>94 cm bij mannen</strong> en meer dan <strong>80 cm bij vrouwen</strong> op visceraal vet. Je kunt ook in een paar seconden je <a href="{site:/whtr-calculator.html}">taille-lengteverhouding</a> berekenen. En zijn je bloedsuikerwaarden grensgevallen, lees dan onze gids over <a href="/nl/diabetes/prediabetes.html">prediabetes</a>.</p>
            <h3>Stap twee: geef je leefstijl 3 tot 6 maanden serieuze aandacht</h3>
            <p>In de fase van de vroege waarschuwing, en in veel gevallen van stadium 1 zonder andere risicofactoren, begint de arts met leefstijlaanpassingen. Onderschat ze niet: elke kilo overgewicht die je kwijtraakt, verlaagt je bloeddruk met ongeveer 1 mmHg. Gezond eten alleen kan de bovendruk bij veel mensen al 8 tot 11 mmHg laten zakken. Soms is dat net zoveel als een pil.</p>
            <div class="tip warn"><p><strong>Maar let op:</strong> heeft je arts je medicijnen voorgeschreven, stop er dan niet op eigen houtje mee omdat je een mooi artikel hebt gelezen. Voeding en beweging werken samen met de medicijnen, en het is je arts die beslist of je ze na verloop van tijd kunt afbouwen.</p></div>

            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>Je bord is je apotheek: voeding die helpt</span></h2>
            <p>Twee eetpatronen zijn goed onderzocht bij hoge bloeddruk: het DASH-dieet, letterlijk "Dietary Approaches to Stop Hypertension" (voedingsaanpak om hoge bloeddruk te stoppen), en het mediterrane dieet. Het goede nieuws? Beide draaien om eenvoudig, natuurlijk eten, heel dicht bij wat onze grootmoeders overal ter wereld kookten voordat fastfood ons leven binnendrong.</p>
            <h3>Kalium: de aartsrivaal van natrium</h3>
            <p>Kalium helpt de nieren natrium af te voeren en ontspant de wanden van de bloedvaten. Je vindt het in:</p>
            <ul class="check-list">
                <li><a href="{food:spinach}">Spinazie</a>, <a href="{food:swiss-chard}">snijbiet</a>, <a href="{food:molokhia}">molokhia</a> en peterselie</li>
                <li><a href="{food:avocado}">Avocado</a>, <a href="{food:banana}">banaan</a> en <a href="{food:dried-apricots}">gedroogde abrikozen</a></li>
                <li>Peulvruchten: <a href="{food:lentils}">linzen</a>, <a href="{food:white-beans}">bonen</a> en <a href="{food:chickpeas}">kikkererwten</a></li>
                <li><a href="{food:sweet-potato}">Zoete aardappel</a> en gewone <a href="{food:boiled-potato}">aardappel, gekookt</a> in de schil</li>
                <li>Naturel yoghurt en zoutarme <a href="{food:labneh}">labneh</a></li>
            </ul>
            <div class="tip warn"><p><strong>Belangrijk:</strong> heb je een nierziekte, of gebruik je bloeddrukverlagers of plaspillen? Overleg dan met je arts voordat je meer kalium gaat eten of zoutvervangers gebruikt.</p></div>
            <h3>Magnesium: de koning van de ontspanning</h3>
            <p>Het helpt de gladde spieren in de vaatwanden te ontspannen, en studies verbinden magnesium met een betere insulinegevoeligheid. Je vindt het in <a href="{food:pumpkin-seeds}">pompoenpitten</a>, amandelen en <a href="{food:cashews}">cashewnoten</a>, bladgroenten en <a href="{food:dark-chocolate-85}">pure chocolade van 85%</a> (twee blokjes, niet de hele reep, afgesproken?).</p>
            <h3>Natuurlijke nitraten: rode biet en rucola</h3>
            <p>Hier komt het verhaal van stikstofmonoxide terug. <a href="{food:beetroot}">Rode biet</a>, <a href="{food:arugula-rocket}">rucola</a> en spinazie zitten vol nitraten, die je lichaam omzet in stikstofmonoxide, waardoor de slagaders wijder worden. Elke dag een glas bietensap of een bordje rucolasalade is een fijne gewoonte.</p>
            <h3>Vezels en minder suiker: om je insuline omlaag te krijgen</h3>
            <p>Omdat insuline de verborgen hoofdrolspeler is, moeten we die tot rust brengen (de glykemische index van elk product vind je in onze <a href="{site:/foods.html}">voedingsgids</a>):</p>
            <ul class="check-list">
                <li><a href="{food:oatmeal}">Havermout</a>, <a href="{food:bulgur}">bulgur</a> en <a href="{food:whole-wheat-bread}">echt volkorenbrood</a> in plaats van wit</li>
                <li>Groente bij elke maaltijd, en begin je maaltijd met de salade</li>
                <li>Eiwit bij elke maaltijd: <a href="{food:boiled-egg}">eieren</a>, vis, <a href="{food:grilled-chicken-breast}">kip</a>, peulvruchten</li>
            </ul>
            <h3>Gezonde vetten</h3>
            <p><a href="{food:extra-virgin-olive-oil}">Extra vierge olijfolie</a>, twee keer per week vette vis zoals <a href="{food:grilled-salmon}">zalm</a>, <a href="{food:canned-sardines}">sardines</a> en <a href="{food:mackerel}">makreel</a> voor omega-3, en <a href="{food:walnuts}">walnoten</a>.</p>
            <h3>Uit de keuken, met redelijk wetenschappelijk bewijs</h3>
            <ul class="check-list">
                <li><strong>Hibiscusthee:</strong> sommige studies vonden dat het de bloeddruk licht verlaagt; twee à drie koppen per dag, zonder suiker.</li>
                <li><strong><a href="{food:garlic}">Knoflook</a>:</strong> heeft een klein maar nuttig effect.</li>
            </ul>
            <p>Maar er bestaat geen wonderkruid dat je medicijnen vervangt of een ongezonde leefstijl rechtzet.</p>

            <h2 class="section-title"><i class="fas fa-ban"></i> <span>Voedingsmiddelen die we moeten "blokkeren"</span></h2>
            <h3>Verborgen zout: de vijand die je niet ziet</h3>
            <p>Is zout dan onschuldig? Helemaal niet. Het is medeplichtig, alleen niet de enige dader. Zal ik je een geheim verklappen? Het meeste zout dat we binnenkrijgen komt niet uit het zoutvaatje op tafel. Meer dan 70% komt uit kant-en-klaar en bewerkt voedsel. Het doel is onder de <strong>2000 mg natrium per dag</strong> te blijven, ongeveer één theelepel zout (5 gram) uit alles bij elkaar.</p>
            <p>Let op met:</p>
            <ul class="check-list">
                <li>Brood en gebak: smaakt niet zout, maar bevat er veel van</li>
                <li>Zoute kazen zoals <a href="{food:halloumi-cheese}">halloumi</a>, <a href="{food:greek-feta}">feta</a> en parmezaan</li>
                <li><a href="{food:pickled-cucumbers-gherkins}">Augurken</a>, zuur en olijven</li>
                <li>Bewerkt vlees zoals worst, hotdogs en bacon</li>
                <li>Bouillonblokjes en kant-en-klare soepen</li>
                <li>Chips, gezouten noten en sauzen zoals <a href="{food:naturally-brewed-soy-sauce}">sojasaus</a> en ketchup</li>
                <li>Restauranteten en fastfood</li>
            </ul>
            <div class="tip"><p><strong>Handig trucje bij het etiket:</strong> staat er natrium (sodium) op, vermenigvuldig dat dan met 2,5 en je weet hoeveel zout het is. Dus 400 mg natrium = 1 gram zout.</p></div>
            <h3>Suiker en geraffineerde koolhydraten: het antwoord ligt in de dessertschaal, niet in het zoutvaatje</h3>
            <p>Omdat insuline de sleutel is, jagen frisdrank, pakjessap, snoep en zoetigheid en veel wit brood allemaal je insuline omhoog en voeden ze het verhaal dat we net vertelden. Vooral toegevoegde fructose (glucose-fructosestroop) hangt samen met een hoger urinezuur en een hogere bloeddruk.</p>
            <h3>Zoethout (drop): in dranken, desserts en snoep</h3>
            <p>Dit weten veel mensen niet. <a href="{food:licorice-drink}">Zoethout</a>, en dus ook drop, bevat een stof die glycyrrhizine heet. Die gedraagt zich als aldosteron: hij houdt natrium vast, voert kalium af en verhoogt de bloeddruk. Zit je bloeddruk op het randje, beperk dan zoethoutdranken en drop.</p>
            <h3>Alcohol en energiedrankjes</h3>
            <p>Alcohol verhoogt de bloeddruk na verloop van tijd, zelfs in "sociale" hoeveelheden. Energiedrankjes met veel cafeïne en suiker kunnen hem plotseling opdrijven. Gewone <a href="{food:black-coffee}">koffie</a>, één of twee koppen per dag, is voor de meeste mensen meestal geen probleem.</p>

            <h2 class="section-title"><i class="fas fa-person-walking"></i> <span>Bewegen: het medicijn dat niets kost</span></h2>
            <p>Bewegen werkt op meerdere fronten tegelijk: het verbetert de insulinegevoeligheid, kalmeert het sympathische zenuwstelsel, verhoogt de aanmaak van stikstofmonoxide en vermindert visceraal vet. Het pakt het verhaal dus bij de wortel aan.</p>
            <h3>Duurtraining (aerobe training)</h3>
            <p>Stevig wandelen, zwemmen, fietsen: <strong>150 minuten per week</strong>, dus een halfuur op 5 dagen. Dat alleen al kan je bovendruk 5 tot 8 mmHg laten dalen. En een gouden tip: een wandeling van 10 tot 15 minuten na het eten verlaagt je bloedsuiker en insuline prima.</p>
            <h3>Krachttraining</h3>
            <p>Gewichten, weerstandsbanden of je eigen lichaamsgewicht: twee tot drie keer per week. Spieren zijn de grootste suikerverbruikers van je lichaam, en hoe meer spieren je hebt, hoe minder insuline je nodig hebt.</p>
            <h3>De verrassing: isometrische oefeningen</h3>
            <p>Een grote analyse van studies uit 2023 liet zien dat isometrische (statische) oefeningen bij de sterkste vormen hoorden om de bloeddruk te verlagen. De bekendste is de wall sit, oftewel "muurzitten": je leunt met je rug tegen de muur en zakt door alsof je op een onzichtbare stoel zit. Ongeveer 4 rondes van 2 minuten, met telkens twee minuten rust ertussen, 3 keer per week. Ook knijpen in een handknijper (handgrip) werkt.</p>
            <div class="tip warn"><p><strong>Let op:</strong> is je bloeddruk 180/110 of hoger, of heb je een hartprobleem, overleg dan met je arts voordat je begint. Houd tijdens het oefenen je adem niet in (valsalvamanoeuvre), maar blijf gewoon doorademen. En begin rustig, want volhouden is belangrijker dan enthousiasme in de eerste week.</p></div>

            <h2 class="section-title"><i class="fas fa-moon"></i> <span>Slaap: de nachtelijke werkplaats van je slagaders</span></h2>
            <p>'s Nachts daalt je bloeddruk normaal gesproken met zo'n 10 tot 20% ten opzichte van overdag. Dat heet nachtelijke dipping, en dat is het moment waarop je slagaders kunnen rusten en zichzelf herstellen. Slaap je te weinig of word je steeds wakker, dan gaat die werkplaats dicht en blijft het sympathische zenuwstelsel de hele nacht aanstaan.</p>
            <p>Mensen die structureel minder dan 6 uur slapen, hebben een duidelijk hoger risico op hoge bloeddruk. Het doel is 7 tot 9 uur.</p>
            <h3>Obstructieve slaapapneu</h3>
            <p>Dit is een van de belangrijkste verborgen oorzaken van hoge bloeddruk, vooral van bloeddruk die niet reageert op medicijnen. Je luchtweg sluit 's nachts vele keren een aantal seconden af, het zuurstofgehalte daalt en je lichaam schrikt wakker en pompt adrenaline rond. Stel je voor dat dat tientallen keren per nacht gebeurt.</p>
            <p>Denk eraan als:</p>
            <ul class="check-list">
                <li>Je hard snurkt, of iemand je heeft verteld dat je in je slaap stopt met ademen</li>
                <li>Je moe wakker wordt, zelfs na 8 uur slaap, en overdag in slaap sukkelt</li>
                <li>Je 's ochtends hoofdpijn en een droge keel hebt</li>
            </ul>
            <p>Herken je jezelf hierin? Vraag je arts dan naar een slaaponderzoek. Behandeling met een CPAP-apparaat en gewichtsverlies kunnen je bloeddruk merkbaar verbeteren.</p>
            <h3>Snelle tips voor een betere nachtrust</h3>
            <ul class="check-list">
                <li>Ga elke dag rond hetzelfde tijdstip naar bed en sta rond hetzelfde tijdstip op, ook in het weekend</li>
                <li>Geen koffie na 14.00 uur</li>
                <li>Minder schermen in het laatste uur voor het slapen, en een donkere, koele slaapkamer</li>
                <li>Een lichte avondmaaltijd, twee à drie uur voor het slapengaan</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-spa"></i> <span>Innerlijke rust: als je zenuwen knappen… knapt je bloeddruk mee</span></h2>
            <p>Chronische stress laat je lichaam onophoudelijk <a href="{site:/cortisol-stress.html}">cortisol</a> en adrenaline aanmaken. Cortisol verhoogt je bloedsuiker en versterkt insulineresistentie; adrenaline vernauwt de slagaders en laat je hart sneller kloppen. We zijn dus terug in dezelfde vicieuze cirkel: een sympathisch zenuwstelsel in permanente noodtoestand.</p>
            <p>De oplossing: op de rem trappen. Je lichaam heeft een tegenhanger, het parasympathische zenuwstelsel, en de belangrijkste kabel daarvan is de nervus vagus. Er zijn heel eenvoudige manieren om die aan te zetten:</p>
            <h3>Langzaam ademen</h3>
            <p>Adem 5 seconden in door je neus en 5 seconden rustig uit. Dat zijn ongeveer 6 ademhalingen per minuut, 5 tot 10 minuten lang, een- of tweemaal per dag. Probeer het en meet je bloeddruk ervoor en erna: je voelt je heerlijk diastolisch, ontspannen, en deze keer ook gewoon fantastisch 😄</p>
            <h3>Andere dingen die het verschil maken</h3>
            <ul class="check-list">
                <li>Een wandeling in de natuur of even in de ochtendzon zitten</li>
                <li>Meditatie, gebed of elke spirituele bezigheid die je rust geeft</li>
                <li>Gezellige tijd met mensen van wie je houdt, want eenzaamheid is op zichzelf al een risicofactor</li>
                <li>Minder nieuws en sociale media voor het slapengaan</li>
                <li>Zijn stress of angst te zwaar geworden om te dragen, dan is praten met een psycholoog geen zwakte; het hoort net zo goed bij de behandeling van hoge bloeddruk</li>
            </ul>
            <h3>En roken?</h3>
            <p>Elke sigaret verhoogt je bloeddruk voor ongeveer een halfuur en beschadigt direct de binnenwand van je slagaders. En een waterpijp is geen haar beter. <strong>Wil je maar één ding doen voor je slagaders? Stop met roken.</strong></p>

            <h2 class="section-title"><i class="fas fa-list-check"></i> <span>Het plan in het kort: vanaf morgenochtend</span></h2>
            <ul class="todo-list">
                <li><label><input type="checkbox"><span>Koop een bovenarmbloeddrukmeter en meet een week lang op de juiste manier</span></label></li>
                <li><label><input type="checkbox"><span>Laat je insuline, bloedsuiker, bloedvetten en nierfunctie testen</span></label></li>
                <li><label><input type="checkbox"><span>Meet je buikomvang</span></label></li>
                <li><label><input type="checkbox"><span>Vul je bord voor de helft met groente, een kwart met eiwit en een kwart met volkoren koolhydraten</span></label></li>
                <li><label><input type="checkbox"><span>Lees het natriumgehalte op het etiket van alles uit blik of kant-en-klaar</span></label></li>
                <li><label><input type="checkbox"><span>Wandel 5 dagen per week een halfuur, en doe daarbovenop 3 keer per week de wall sit</span></label></li>
                <li><label><input type="checkbox"><span>Slaap minstens 7 uur, en let op snurken</span></label></li>
                <li><label><input type="checkbox"><span>Elke dag 5 minuten langzaam ademen</span></label></li>
                <li><label><input type="checkbox"><span>Bespreek de resultaten na 3 maanden met je arts</span></label></li>
            </ul>

            <h2 class="section-title"><i class="fas fa-flag-checkered"></i> <span>En tot slot…</span></h2>
            <p>Hoge bloeddruk is geen levenslange straf, en het is geen getal dat zomaar uit het niets opduikt. Het is een boodschap van je lichaam dat er iets in je stofwisseling en je slagaders aandacht nodig heeft. Het mooie is dat elke kleine stap, elke wandeling, elk bord salade en elke goede nachtrust iets van je bloeddruk afknabbelt en jaren toevoegt aan het leven van je slagaders.</p>
            <p>Wacht dus niet tot de "stille moordenaar" van zich laat horen. <strong>Jij spreekt als eerste: meet vandaag nog je bloeddruk.</strong></p>
            <p>Je kleine hart zal je dankbaar zijn… boem… boem… boem. Alleen deze keer lekker rustig.</p>'''),
sv=dict(
 byline='Av Dr. Wassim Habib',
 title='Högt blodtryck och socker: det dolda sambandet med insulin',
 h1='Tro det eller ej: sockret höjer ditt blodtryck… inte bara saltet!',
 subtitle='Högt blodtryck, den tysta mördaren: orsakerna, kopplingen till insulin och hur du skyddar dina blodkärl',
 crumb='Högt blodtryck och socker',
 summary='Högt blodtryck fast du knappt äter salt? Leta efter sockret: hur insulin höjer blodtrycket, hur du mäter rätt hemma och en plan för mat, motion och sömn.',
 cat='Hjärta och blodkärl',
 desc='Salt är inte den enda orsaken till högt blodtryck. Så höjer insulin ditt blodtryck, det här ska du äta och så skyddar du dina blodkärl.',
 hero_alt='Orolig kvinna mäter sitt blodtryck med en överarmsmätare, bredvid en saltkar, en sötad iskaffe och en chokladdessert, med en skugga av sockerbitar bakom sig',
 about=['Hypertension', 'Insulin resistance', 'Blood pressure', 'DASH diet'],
 disclaimer='⚖️ Den här artikeln är till för hälsoinformation och utbildning och ersätter inte råd från din läkare. Sluta aldrig med eller ändra ett läkemedel utan att först prata med din läkare.',
 body='''            <p class="lead">Har du någon gång undrat varför den moderna medicinen kallar det "den tysta mördaren"? Om inte, ska jag berätta den verkliga anledningen: det smyger sig tyst in i dina artärer och i vävnaderna i dina livsviktiga organ och skadar dem steg för steg, utan att du känner minsta smärta, tills problemet har gått långt.</p>
            <p>Högt blodtryck börjar inte som en ensam sjukdom utan vare sig mamma eller pappa. I själva verket är det en direkt spegling av en ämnesomsättningsrubbning (metabol dysfunktion) i kroppen och av en pågående inflammation i blodkärlens innerväggar.</p>
            <p>I den här artikeln reder vi ut gåtan i lugn och ro och utan krånglig medicinsk jargong: vi går igenom siffrorna, förklarar hur <a href="{site:/insulin-resistance.html}">insulinresistens</a> hänger tätt ihop med högt blodtryck och gör tillsammans en komplett plan för att ge dina artärer tillbaka deras smidighet och livskraft… och skydda ditt lilla hjärta, som verkligen inte orkar så mycket mer.</p>

            <h2 class="section-title"><i class="fas fa-heart-pulse"></i> <span>Vad är blodtryck, och vad betyder siffrorna?</span></h2>
            <p>Varje gång ditt hjärta slår dunk-dunk pumpar det blod genom ett invecklat nätverk av blodkärl. Så skriv det här med riktigt feeeta bokstäver: <strong>blodtrycket är kraften som blodet trycker med mot artärväggarna medan det strömmar</strong>. Kort sagt: hur hårt kärlväggarna tar emot blodflödet.</p>
            <p>Trycket som uppstår i samma ögonblick som hjärtat pumpar kallas det <strong>systoliska blodtrycket</strong>, eller övertrycket. Hänger du med? Enkelt uttryckt är det den stora siffran, den som står överst. Lägg namnet på minnet: systoliskt.</p>
            <p>När hjärtat har pumpat ut blodet behöver det slappna av och vila för att fyllas på igen. Det är där det <strong>diastoliska blodtrycket</strong> (undertrycket) kommer in. Och nej, diastoliskt har inget med "fantastiskt" att göra: det betyder att hjärtat slappnar av och vidgas, dess lilla vilopaus mellan två slag. Under den pausen mäts trycket i artärerna, medan hjärtat fylls på nytt och gör om alltihop: dunk… dunk… dunk… dunk. Enkelt, eller hur?</p>
            <h3>Hur vet man om blodtrycket är normalt eller har börjat blinka varningslampor?</h3>
            <table class="bp-table">
                <thead><tr><th>Kategori</th><th>Systoliskt (övertryck)</th><th></th><th>Diastoliskt (undertryck)</th><th>Vad betyder det?</th></tr></thead>
                <tbody>
                    <tr class="bp-ok"><td>Normalt och idealiskt</td><td class="bp-num" data-label="Systoliskt">under 120</td><td class="bp-op">och</td><td class="bp-num" data-label="Diastoliskt">under 80</td><td>Smidiga blodkärl och ett hjärta som arbetar helt avslappnat</td></tr>
                    <tr class="bp-elev"><td>Förhöjt: den tidiga varningsfasen</td><td class="bp-num" data-label="Systoliskt">120–129</td><td class="bp-op">och</td><td class="bp-num" data-label="Diastoliskt">under 80</td><td>Kärlen börjar stelna: dags att ändra levnadsvanorna direkt</td></tr>
                    <tr class="bp-s1"><td>Högt blodtryck, steg 1</td><td class="bp-num" data-label="Systoliskt">130–139</td><td class="bp-op">eller</td><td class="bp-num" data-label="Diastoliskt">80–89</td><td>Nu finns en diagnos; läkaren avgör utifrån dina övriga riskfaktorer</td></tr>
                    <tr class="bp-s2"><td>Högt blodtryck, steg 2</td><td class="bp-num" data-label="Systoliskt">140 eller mer</td><td class="bp-op">eller</td><td class="bp-num" data-label="Diastoliskt">90 eller mer</td><td>Kräver regelbunden medicinsk uppföljning och ofta läkemedel</td></tr>
                </tbody>
            </table>
            <p class="table-note">Alla värden anges i millimeter kvicksilver (mmHg).</p>
            <div class="danger-box">
                <h3>🚨 Röda varningssignaler (akut)</h3>
                <p>Visar mätaren ett värde över 180/120 mmHg tillsammans med plötslig, svår huvudvärk, dimsyn, andnöd, bröstsmärta, kraftlöshet i en arm eller ett ben eller svårt att tala? Då är det inte läge att börja justera maten. Det är ett medicinskt akutläge (hypertensiv kris), och du behöver <strong>åka direkt till närmaste akutmottagning eller ringa 112</strong>.</p>
            </div>

            <h2 class="section-title"><i class="fas fa-user-secret"></i> <span>Den tysta mördaren har en hemlig medbrottsling… lär känna den innan den lär känna dig 😉</span></h2>
            <p>Här kommer dagens viktigaste poäng, och den som oftast glöms bort. Högt blodtryck fast du knappt rör saltet? Leta efter sockret! De flesta tror att blodtrycket stiger enbart av för mycket salt. Men, kära vänner, sanningen går mycket djupare, och den verkliga boven är inte den du tror. Låt oss lägga korten på bordet: <strong>socker höjer insulinet, och insulinet är berättelsens dolda huvudperson.</strong> Så nu får insulinet bekänna färg:</p>
            <h3>1. Njurarna håller kvar natrium (natriumretention)</h3>
            <figure class="article-figure">
                <img src="/images/sodium-water-retention-blood-vessel-hypertension.webp" alt="Illustration av ett tvärsnitt av ett blodkärl fullt av röda blodkroppar, natriumjoner och vattenmolekyler, med signaler till njuren som håller kvar natrium, så att blodvolymen och trycket mot kärlväggen ökar" width="1200" height="896" loading="lazy" decoding="async">
                <figcaption>Högt insulin får njurarna att hålla kvar natrium; natriumet drar med sig vatten in i blodet, och trycket mot artärväggarna stiger.</figcaption>
            </figure>
            <p>Långvarigt höga nivåer av hormonet insulin i blodet (hyperinsulinemi) skickar direkta signaler, raka rör, till njurarna om att ta tillbaka natrium i stället för att låta det lämna kroppen med urinen. Och vart natriumet än går följer vattnet med. Den totala blodvolymen i artärerna ökar, och därmed också trycket mot dem.</p>
            <h3>2. Ett överstimulerat sympatiskt nervsystem</h3>
            <p>För mycket insulin håller det sympatiska nervsystemet i ständig högsta beredskap, som om det fanns en inbrottstjuv i huset dygnet runt. Resultatet? Sammandragna blodkärl (vasokonstriktion) och snabbare slag från ditt lilla hjärta.</p>
            <h3>3. Kärlväggen förlorar sin smidighet (endoteldysfunktion)</h3>
            <p>Normalt utsöndrar artärernas innervägg en liten, magisk gas som heter kväveoxid, vars jobb är att vidga artärerna och hålla dem mjuka och smidiga. När insulinresistens uppstår minskar produktionen av kväveoxid, och en kronisk låggradig inflammation börjar nöta på kärlväggen. En artär som förut var som mjukt gummi blir som en gammal trädgårdsslang som legat i solen i åratal.</p>
            <h3>4. Renin-angiotensin-aldosteronsystemet (RAAS)</h3>
            <p>Det här hormonsystemet reglerar blodtrycket och vätskebalansen i kroppen. Vid insulinresistens och för mycket kroppsfett går det på övertid: angiotensin II drar ihop artärerna och aldosteron håller kvar ännu mer natrium. En dubbelsmäll, alltså.</p>
            <h3>5. Visceralt fett: mer än bara en mage</h3>
            <p>Fettet runt organen djupt inne i buken är inget tyst energiförråd. Det är aktiv vävnad som utsöndrar inflammatoriska ämnen (cytokiner) och dessutom tillverkar råmaterialet till angiotensin. Därför kan ditt midjemått ibland säga mer om din risk för högt blodtryck än siffran på vågen. (Läs mer om <a href="/sv/articles/fatty-liver-and-visceral-fat.html">visceralt fett och fettlever</a>.)</p>
            <h3>Finns det fler orsaker?</h3>
            <p>Absolut. Till exempel ärftlighet och ålder, saltkänslighet (som varierar från person till person), sömnapné (mer om det senare), rökning, alkohol och vissa läkemedel som antiinflammatoriska smärtstillande (NSAID), avsvällande nässprayer och, hos en del kvinnor, p-piller.</p>
            <p>Det finns också sekundär hypertoni, där det finns en tydlig bakomliggande orsak som njursjukdom eller problem med sköldkörteln eller binjurarna. Läkaren tänker särskilt på det om högt blodtryck dyker upp i unga år, eller om trycket är mycket högt och inte svarar på behandling.</p>

            <h2 class="section-title"><i class="fas fa-stethoscope"></i> <span>Hur märker jag det då? Här kommer överraskningen</span></h2>
            <p>I de flesta fall märker du ingenting alls. Ingen smärta, ingen signal. Och det är precis därför det kallas "den tysta mördaren". En del lever i åratal med ett övertryck på 150 och tror att de är gjorda av stål.</p>
            <p>Ibland, särskilt när blodtrycket är mycket högt, kan du märka saker som:</p>
            <ul class="check-list">
                <li>Huvudvärk på morgonen, ofta i bakhuvudet</li>
                <li>Yrsel eller öronsus (tinnitus)</li>
                <li>Hjärtklappning eller att du känner hjärtslagen</li>
                <li>Allmän trötthet och svårt att koncentrera dig</li>
            </ul>
            <p>Men se upp: de här symtomen är ingen måttstock. Att du inte har några symtom betyder inte att blodtrycket är bra. Och den klassiska frasen "mitt blodtryck är högt eftersom jag har ont i huvudet" är ofta tvärtom: smärtan och stressen har tillfälligt drivit upp trycket. <strong>Den enda domaren är blodtrycksmätaren.</strong></p>

            <h2 class="section-title"><i class="fas fa-house-medical"></i> <span>Så mäter du blodtrycket hemma som ett proffs</span></h2>
            <p>En enda mätning på mottagningen kan ibland ljuga. Det finns något som kallas vitrockshypertoni: så fort du ser läkaren rusar trycket i höjden. Och det omvända finns också, maskerad hypertoni: helt fint på mottagningen men högt hemma och på jobbet. Därför är hemmamätning av blodtrycket guld värd.</p>
            <h3>Så gör du rätt:</h3>
            <ol class="steps">
                <li>Använd en mätare med manschett runt överarmen, inte runt handleden, och se till att manschetten har rätt storlek för din arm.</li>
                <li>Inget kaffe, ingen cigarett och ingen träning en halvtimme före mätningen, och gå på toaletten först.</li>
                <li>Sitt på en stol med stöd för ryggen och fötterna i golvet, benen okorsade, och vila i 5 minuter.</li>
                <li>Lägg armen på ett bord i hjärthöjd, med manschetten direkt mot huden och inte utanpå tröjan.</li>
                <li>Prata inte och titta inte på mobilen medan du mäter.</li>
                <li>Gör två mätningar med en minuts mellanrum och skriv upp medelvärdet.</li>
                <li>Upprepa morgon och kväll i en vecka, och ta med tabellen till läkaren.</li>
            </ol>
            <p>Hamnar medelvärdet av dina hemmamätningar på 130/80 eller högre är det ett tecken på att du bör prata med din läkare. Enligt de europeiska riktlinjerna (ESC 2024) går gränsen för hemmamätning vid 135/85.</p>

            <h2 class="section-title"><i class="fas fa-vial"></i> <span>På gränsen till högt blodtryck: vad gör vi nu?</span></h2>
            <p>Ligger dina värden mellan 120 och 139, eller pendlar undertrycket runt 80? Då är det inte läge för panik, men inte heller för "vi får se i morgon". Det här är det bästa läget att agera, eftersom artärerna fortfarande är smidiga och kroppen svarar snabbt.</p>
            <h3>Steg ett: ta reda på vad som händer på insidan</h3>
            <p>Be din läkare om de här proverna, eftersom de visar om historien hänger ihop med insulin och ämnesomsättning:</p>
            <ul class="check-list">
                <li>Fasteglukos och HbA1c (långtidsblodsocker)</li>
                <li>Fasteinsulin, som används för att räkna ut insulinresistensindexet HOMA-IR</li>
                <li>Blodfetter (lipidstatus), särskilt triglycerider och det "goda" HDL-kolesterolet</li>
                <li>Njurfunktion (kreatinin, eGFR) och albumin i urinen</li>
                <li>Natrium och kalium i blodet, samt sköldkörtelhormonet TSH</li>
            </ul>
            <p>Mät också midjan i höjd med naveln. Generellt pekar mer än <strong>94 cm hos män</strong> och mer än <strong>80 cm hos kvinnor</strong> på visceralt fett. Du kan också räkna ut din <a href="{site:/whtr-calculator.html}">midja-längdkvot</a> på några sekunder. Och om dina blodsockervärden ligger på gränsen, läs vår guide om <a href="/sv/diabetes/prediabetes.html">prediabetes</a>.</p>
            <h3>Steg två: ge dina levnadsvanor 3 till 6 månader på allvar</h3>
            <p>I den tidiga varningsfasen, och i många fall av steg 1 utan andra riskfaktorer, börjar läkaren med ändrade levnadsvanor. Underskatta dem inte: varje kilo övervikt du går ner sänker blodtrycket med ungefär 1 mmHg. Bara bra mat kan sänka övertrycket med 8 till 11 mmHg hos många. Ibland lika mycket som en tablett.</p>
            <div class="tip warn"><p><strong>Men se upp:</strong> har läkaren skrivit ut läkemedel ska du inte sluta på egen hand för att du läst en bra artikel. Kost och motion verkar tillsammans med läkemedlen, och det är läkaren som avgör om ni kan trappa ner dem med tiden.</p></div>

            <h2 class="section-title"><i class="fas fa-utensils"></i> <span>Din tallrik är ditt apotek: maten som hjälper</span></h2>
            <p>Två kostmönster är väl studerade för blodtrycket: DASH-kosten, ordagrant "Dietary Approaches to Stop Hypertension" (kostråd för att stoppa högt blodtryck), och medelhavskosten. Den goda nyheten? Båda bygger på enkel, naturlig mat, väldigt nära det våra mormödrar och farmödrar lagade över hela världen innan snabbmaten tog över.</p>
            <h3>Kalium: natriumets ärkerival</h3>
            <p>Kalium hjälper njurarna att göra sig av med natrium och får kärlväggarna att slappna av. Du hittar det i:</p>
            <ul class="check-list">
                <li><a href="{food:spinach}">Spenat</a>, <a href="{food:swiss-chard}">mangold</a>, <a href="{food:molokhia}">molokhia</a> och persilja</li>
                <li><a href="{food:avocado}">Avokado</a>, <a href="{food:banana}">banan</a> och <a href="{food:dried-apricots}">torkade aprikoser</a></li>
                <li>Baljväxter: <a href="{food:lentils}">linser</a>, <a href="{food:white-beans}">bönor</a> och <a href="{food:chickpeas}">kikärter</a></li>
                <li><a href="{food:sweet-potato}">Sötpotatis</a> och vanlig <a href="{food:boiled-potato}">potatis, kokt</a> med skalet på</li>
                <li>Naturell yoghurt och saltsnål <a href="{food:labneh}">labneh</a></li>
            </ul>
            <div class="tip warn"><p><strong>Viktigt:</strong> har du en njursjukdom, eller tar du blodtrycksmediciner eller vätskedrivande läkemedel, prata med din läkare innan du ökar kaliumintaget eller använder saltersättning.</p></div>
            <h3>Magnesium: avslappningens kung</h3>
            <p>Det hjälper den glatta muskulaturen i artärväggarna att slappna av, och studier kopplar magnesium till bättre insulinkänslighet. Du hittar det i <a href="{food:pumpkin-seeds}">pumpafrön</a>, mandel och <a href="{food:cashews}">cashewnötter</a>, bladgrönsaker och <a href="{food:dark-chocolate-85}">mörk choklad 85 %</a> (två rutor, inte hela kakan, eller hur?).</p>
            <h3>Naturliga nitrater: rödbetor och ruccola</h3>
            <p>Här kommer historien om kväveoxid tillbaka. <a href="{food:beetroot}">Rödbetor</a>, <a href="{food:arugula-rocket}">ruccola</a> och spenat är rika på nitrater som kroppen omvandlar till kväveoxid, så att artärerna vidgas. Ett glas rödbetsjuice eller en tallrik ruccolasallad om dagen är en fin vana.</p>
            <h3>Fibrer och mindre socker: för att få ner insulinet</h3>
            <p>Eftersom insulinet är berättelsens dolda huvudperson behöver vi lugna ner det (det glykemiska indexet för varje livsmedel hittar du i vår <a href="/sv/foods/index.html">livsmedelsguide</a>):</p>
            <ul class="check-list">
                <li><a href="{food:oatmeal}">Havre</a>, <a href="{food:bulgur}">bulgur</a> och <a href="{food:whole-wheat-bread}">riktigt fullkornsbröd</a> i stället för vitt</li>
                <li>Grönsaker till varje måltid, och börja måltiden med salladen</li>
                <li>Protein till varje måltid: <a href="{food:boiled-egg}">ägg</a>, fisk, <a href="{food:grilled-chicken-breast}">kyckling</a>, baljväxter</li>
            </ul>
            <h3>Nyttiga fetter</h3>
            <p><a href="{food:extra-virgin-olive-oil}">Extra jungfruolivolja</a>, fet fisk som <a href="{food:grilled-salmon}">lax</a>, <a href="{food:canned-sardines}">sardiner</a> och <a href="{food:mackerel}">makrill</a> två gånger i veckan för omega-3, och <a href="{food:walnuts}">valnötter</a>.</p>
            <h3>Från köket, med rimligt vetenskapligt stöd</h3>
            <ul class="check-list">
                <li><strong>Hibiskuste:</strong> vissa studier har funnit att det sänker blodtrycket något; två till tre koppar om dagen, utan socker.</li>
                <li><strong><a href="{food:garlic}">Vitlök</a>:</strong> har en liten men nyttig effekt.</li>
            </ul>
            <p>Men det finns ingen magisk ört som ersätter dina läkemedel eller rättar till ohälsosamma levnadsvanor.</p>

            <h2 class="section-title"><i class="fas fa-ban"></i> <span>Maten vi behöver "blockera"</span></h2>
            <h3>Dolt salt: fienden du inte ser</h3>
            <p>Är saltet alltså oskyldigt? Inte alls. Det är en medbrottsling, den agerar bara inte ensam. Ska jag avslöja en hemlighet? Det mesta saltet vi äter kommer inte från saltkaret på bordet. Över 70 % kommer från färdigmat och processad mat. Målet är att hålla dig under <strong>2 000 mg natrium per dag</strong>, ungefär en tesked salt (5 gram) från allt sammanlagt.</p>
            <p>Se upp med:</p>
            <ul class="check-list">
                <li>Bröd och bakverk: smakar inte salt men innehåller mycket</li>
                <li>Salta ostar som <a href="{food:halloumi-cheese}">halloumi</a>, <a href="{food:greek-feta}">fetaost</a> och parmesan</li>
                <li><a href="{food:pickled-cucumbers-gherkins}">Inlagda grönsaker</a> och oliver</li>
                <li>Charkuterier som korv, varmkorv och bacon</li>
                <li>Buljongtärningar och färdiga soppor</li>
                <li>Chips, saltade nötter och såser som <a href="{food:naturally-brewed-soy-sauce}">soja</a> och ketchup</li>
                <li>Restaurangmat och snabbmat</li>
            </ul>
            <div class="tip"><p><strong>Ett litet knep när du läser etiketten:</strong> står det natrium (sodium), gånga det med 2,5 så får du mängden salt. Alltså 400 mg natrium = 1 gram salt.</p></div>
            <h3>Socker och raffinerade kolhydrater: svaret finns i efterrättsskålen, inte i saltkaret</h3>
            <p>Eftersom insulinet är nyckeln höjer läsk, förpackade juicer, sötsaker och mycket vitt bröd allesammans insulinet och göder historien vi just berättat. Särskilt tillsatt fruktos (glukos-fruktossirap) har koppling till höjd urinsyra och högre blodtryck.</p>
            <h3>Lakrits: i drycker, efterrätter och godis</h3>
            <p>Det här är något många inte känner till. <a href="{food:licorice-drink}">Lakritsrot</a>, och därmed lakrits, innehåller ett ämne som heter glycyrrhizin. Det beter sig som aldosteron: det håller kvar natrium, driver ut kalium och höjer blodtrycket. Ligger ditt blodtryck på gränsen, dra ner på lakritsdrycker och lakritsgodis.</p>
            <h3>Alkohol och energidrycker</h3>
            <p>Alkohol höjer blodtrycket med tiden, även i "sociala" mängder. Energidrycker med höga doser koffein och socker kan driva upp det plötsligt. Vanligt <a href="{food:black-coffee}">kaffe</a>, en eller två koppar om dagen, är däremot oftast inget problem för de flesta.</p>

            <h2 class="section-title"><i class="fas fa-person-walking"></i> <span>Motion: medicinen som är gratis</span></h2>
            <p>Motion verkar på flera fronter samtidigt: den förbättrar insulinkänsligheten, lugnar det sympatiska nervsystemet, ökar frisättningen av kväveoxid och minskar det viscerala fettet. Den angriper alltså historien vid roten.</p>
            <h3>Konditionsträning (aerob träning)</h3>
            <p>Rask promenad, simning, cykling: <strong>150 minuter i veckan</strong>, alltså en halvtimme fem dagar. Bara det kan sänka övertrycket med 5 till 8 mmHg. Och ett guldtips: en promenad på 10 till 15 minuter efter maten sänker blodsockret och insulinet utmärkt.</p>
            <h3>Styrketräning</h3>
            <p>Vikter, gummiband eller kroppsvikt: två till tre gånger i veckan. Musklerna är kroppens största sockerförbrukare, och ju mer muskler du har, desto mindre insulin behöver du.</p>
            <h3>Överraskningen: isometrisk träning</h3>
            <p>En stor analys av studier som publicerades 2023 fann att isometrisk (statisk) träning hörde till de mest effektiva formerna för att sänka blodtrycket. Den mest kända är väggsittning (wall sit): luta ryggen mot väggen och glid ner som om du satt på en osynlig stol. Ungefär 4 omgångar på 2 minuter vardera, med två minuters vila emellan, 3 gånger i veckan. Handgreppsövningar (handgrip) fungerar också.</p>
            <div class="tip warn"><p><strong>Se upp:</strong> är ditt blodtryck 180/110 eller högre, eller har du en hjärtsjukdom, prata med din läkare innan du börjar. Håll inte andan när du tränar (valsalvamanöver), utan fortsätt andas normalt. Och börja försiktigt, för uthållighet är viktigare än entusiasm första veckan.</p></div>

            <h2 class="section-title"><i class="fas fa-moon"></i> <span>Sömn: artärernas nattliga verkstad</span></h2>
            <p>På natten sjunker blodtrycket normalt med ungefär 10 till 20 % jämfört med dagen. Det kallas nattlig dipping, och det är artärernas chans att vila och reparera sig själva. När du sover för lite eller sömnen är avbruten stänger verkstaden, och det sympatiska nervsystemet är igång hela natten.</p>
            <p>Den som regelbundet sover mindre än 6 timmar har en tydligt högre risk för högt blodtryck. Målet är 7 till 9 timmar.</p>
            <h3>Obstruktiv sömnapné</h3>
            <p>Det här är en av de viktigaste dolda orsakerna till högt blodtryck, särskilt blodtryck som inte svarar på läkemedel. Luftvägen stängs i flera sekunder många gånger per natt, syrenivån sjunker och kroppen vaknar i panik och pumpar ut adrenalin. Tänk dig att det händer tiotals gånger varje natt.</p>
            <p>Misstänk det om:</p>
            <ul class="check-list">
                <li>Du snarkar högt, eller någon har sagt att du slutar andas när du sover</li>
                <li>Du vaknar trött även efter 8 timmars sömn och nickar till under dagen</li>
                <li>Du har huvudvärk och torr hals på morgonen</li>
            </ul>
            <p>Känner du igen dig? Prata med din läkare om en sömnregistrering. Behandling med CPAP och viktnedgång kan förbättra blodtrycket märkbart.</p>
            <h3>Snabba tips för bättre sömn</h3>
            <ul class="check-list">
                <li>Lägg dig och vakna ungefär samma tid varje dag, även på helgen</li>
                <li>Inget kaffe efter klockan 14</li>
                <li>Mindre skärmtid den sista timmen före läggdags, och ett mörkt och svalt sovrum</li>
                <li>En lätt middag, två till tre timmar innan du lägger dig</li>
            </ul>

            <h2 class="section-title"><i class="fas fa-spa"></i> <span>Sinnesro: när nerverna brister… brister blodtrycket också</span></h2>
            <p>Kronisk stress får kroppen att utsöndra <a href="{site:/cortisol-stress.html}">kortisol</a> och adrenalin hela tiden. Kortisol höjer blodsockret och ökar insulinresistensen; adrenalin drar ihop artärerna och får hjärtat att slå snabbare. Vi är alltså tillbaka i samma ond cirkel: ett sympatiskt nervsystem i ständigt nödläge.</p>
            <p>Lösningen är att trycka på bromsen. Kroppen har ett motsatt system, det parasympatiska nervsystemet, och dess viktigaste kabel är vagusnerven. Det finns mycket enkla sätt att slå på den:</p>
            <h3>Långsam andning</h3>
            <p>Andas in genom näsan i 5 sekunder och ut lugnt i 5 sekunder. Det blir ungefär 6 andetag i minuten, i 5 till 10 minuter, en eller två gånger om dagen. Prova och mät blodtrycket före och efter: du kommer att känna dig riktigt diastolisk, avslappnad, och den här gången helt fantastisk också 😄</p>
            <h3>Annat som gör skillnad</h3>
            <ul class="check-list">
                <li>En promenad i naturen eller en stund i morgonsolen</li>
                <li>Meditation, bön eller vilken andlig praktik som helst som ger dig ro</li>
                <li>Mysig tid med människor du tycker om, eftersom ensamhet i sig är en riskfaktor</li>
                <li>Mindre nyheter och sociala medier före läggdags</li>
                <li>Har stressen eller oron blivit för tung att bära är det ingen svaghet att prata med en psykolog eller kurator; det är också en del av behandlingen av högt blodtryck</li>
            </ul>
            <h3>Och rökning?</h3>
            <p>Varje cigarett höjer blodtrycket i ungefär en halvtimme efteråt och skadar artärernas innervägg direkt. Och vattenpipa är inte snällare. <strong>Om du bara gör en enda sak för dina artärer: sluta röka.</strong></p>

            <h2 class="section-title"><i class="fas fa-list-check"></i> <span>Planen i korthet: från och med i morgon bitti</span></h2>
            <ul class="todo-list">
                <li><label><input type="checkbox"><span>Köp en blodtrycksmätare för överarmen och mät rätt i en vecka</span></label></li>
                <li><label><input type="checkbox"><span>Ta prover för insulin, blodsocker, blodfetter och njurfunktion</span></label></li>
                <li><label><input type="checkbox"><span>Mät ditt midjemått</span></label></li>
                <li><label><input type="checkbox"><span>Fyll halva tallriken med grönsaker, en fjärdedel med protein och en fjärdedel med fullkornskolhydrater</span></label></li>
                <li><label><input type="checkbox"><span>Läs natriumuppgiften på etiketten på allt konserverat och färdiglagat</span></label></li>
                <li><label><input type="checkbox"><span>Promenera en halvtimme fem dagar i veckan, och lägg till väggsittning tre gånger i veckan</span></label></li>
                <li><label><input type="checkbox"><span>Sov minst 7 timmar, och var uppmärksam på snarkning</span></label></li>
                <li><label><input type="checkbox"><span>5 minuter långsam andning varje dag</span></label></li>
                <li><label><input type="checkbox"><span>Gå igenom resultaten med din läkare efter 3 månader</span></label></li>
            </ul>

            <h2 class="section-title"><i class="fas fa-flag-checkered"></i> <span>Och till sist…</span></h2>
            <p>Högt blodtryck är inget livstidsstraff, och det är ingen siffra som plötsligt dyker upp ur tomma intet. Det är ett meddelande från kroppen om att något i ämnesomsättningen och artärerna behöver uppmärksamhet. Det fina är att varje litet steg, varje promenad, varje salladstallrik och varje god natts sömn nöter ner blodtrycket och lägger till år på dina artärers liv.</p>
            <p>Så vänta inte på att "den tysta mördaren" ska säga något. <strong>Säg du något först: mät ditt blodtryck i dag.</strong></p>
            <p>Ditt lilla hjärta kommer att tacka dig… dunk… dunk… dunk. Fast den här gången i lugn och ro.</p>'''),
    ),
)

FRUCTOSE_CSS = """
        .refs-fold { background: var(--bg-input); border: 1px solid var(--border-color); border-radius: var(--radius-md); margin: 26px 0 14px; }
        .refs-fold summary { cursor: pointer; padding: 12px 16px; font-weight: 800; color: var(--text-muted); list-style: none; }
        .refs-fold summary::-webkit-details-marker { display: none; }
        .refs-fold[open] summary { border-bottom: 1px solid var(--border-color); }
        .refs-fold .ref-list { padding: 12px 16px 6px; padding-inline-start: 34px; }
        .food-links { display: flex; flex-wrap: wrap; gap: 8px; margin: -4px 0 18px; }
        .food-chip { display: inline-flex; align-items: center; gap: 6px; padding: 5px 12px; border-radius: 999px; font-size: 0.88rem; font-weight: 700;
            background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.35); color: var(--primary); text-decoration: none; }
        .food-chip::before { content: "🍽️"; font-size: 0.85em; }
        .food-chip:hover { background: rgba(16, 185, 129, 0.16); }
        .sugar-table { width: 100%; border-collapse: collapse; margin: 12px 0 10px; font-size: 0.95rem; }
        .sugar-table th, .sugar-table td { padding: 10px 12px; border-bottom: 1px solid var(--border-color); text-align: start; vertical-align: top; }
        .sugar-table th { color: var(--primary); font-weight: 800; background: rgba(16, 185, 129, 0.06); }
        .sugar-table td:first-child { font-weight: 800; }
        .sugar-table td:nth-child(2) { white-space: nowrap; }
        .boodi-card { margin: 22px 0 26px; }
"""

# Fifth signed article (31 October 2026): fructose in fruit vs added sugar; copy from fructose-article-ar.md, translated
# faithfully (the copy's translation notes give the replacements for the jokes; the notes themselves are not shown).
# Food links follow the copy's [[link: ...]] markers; «شاي الكركديه» links to 297 (iced hibiscus), user decision 2026-10-31.
FRUCTOSE = dict(
    slugs=dict(ar='fructose-fruit-vs-processed-sugar', en='fructose-fruit-vs-processed-sugar', nl='fructose-fruit-vs-bewerkte-suiker',
               sv='fruktos-frukt-vs-tillsatt-socker'),
    hero='fructose-fruit-vs-processed-sugar-cover.webp', hero_size=(1200, 670),
    published='2026-10-31', modified='2026-10-31',
    references=[
        'World Health Organization. Guideline: Sugars intake for adults and children. Geneva: WHO; 2015.',
        'Tappy L, Lê KA. Metabolic effects of fructose and the worldwide increase in obesity. Physiol Rev. 2010;90(1):23–46.',
        'Stanhope KL et al. Consuming fructose-sweetened, not glucose-sweetened, beverages increases visceral adiposity and lipids and decreases insulin sensitivity in overweight/obese humans. J Clin Invest. 2009;119(5):1322–34.',
        'Jang C et al. The small intestine converts dietary fructose into glucose and organic acids. Cell Metab. 2018;27(2):351–61.',
        'Muraki I et al. Fruit consumption and risk of type 2 diabetes: results from three prospective longitudinal cohort studies. BMJ. 2013;347:f5001.',
        'Atkinson FS, Foster-Powell K, Brand-Miller JC. International tables of glycemic index and glycemic load values: 2008. Diabetes Care. 2008;31(12):2281–3.',
        'Livesey G. Health potential of polyols as sugar replacers, with emphasis on low glycaemic properties. Nutr Res Rev. 2003;16(2):163–91.',
        'EFSA Panel on Food Additives and Flavourings. Re-evaluation of erythritol (E 968) as a food additive. EFSA J. 2023;21(12):e8430.',
        'Witkowski M et al. The artificial sweetener erythritol and cardiovascular event risk. Nat Med. 2023;29(3):710–8.',
        'EFSA Panel on Nutrition, Novel Foods and Food Allergens (NDA). Safety of D-allulose as a novel food pursuant to Regulation (EU) 2015/2283. EFSA J. 2025;23(6):e9468.',
        'Rinella ME et al. A multisociety Delphi consensus statement on new fatty liver disease nomenclature. J Hepatol. 2023;79(6):1542–56.',
        'World Health Organization. Use of non-sugar sweeteners: WHO guideline. Geneva: WHO; 2023.',
    ],
    named_author=True,                                   # medical review line «تمت المراجعة الطبية من قبل د. وسيم حبيب» (Person in schema)
    article_schema=True,
    refs_folded=True,
    extra_css=FRUCTOSE_CSS,
    content=dict(
ar=dict(
 title='الفركتوز: بالفاكهة صديق، وبالعلبة عدو',
 h1='الفركتوز: بالفاكهة صديق، وبالعلبة عدو… شو القصة؟',
 crumb='الفركتوز والسكر المصنّع',
 summary='ليش الفركتوز بالتفاحة ما بيضرك، وبالمشروب الغازي بيروح على كبدك؟ شرح بسيط للسكر المصنّع، والفرق بين البدائل، وكيف تخفف السكر.',
 cat='التغذية',
 desc='ليش الفركتوز بالتفاحة ما بيضرك، وبالمشروب الغازي بيروح على كبدك؟ شرح بسيط للسكر المصنّع، والفرق بين البدائل، وكيف تخفف السكر.',
 hero_alt='شاب وفتاة يختاران بين الفاكهة الطازجة والمشروبات المحلاة والسكر المصنّع',
 about=['Fructose', 'Added sugar', 'Fatty liver disease', 'Sweeteners'],
 refs_label='المصادر ▾',
 disclaimer='<strong>ملاحظة توعية:</strong> هذا المقال للتوعية العامة بالتغذية ونمط الحياة، ولا يغني عن استشارة الطبيب.',
 review='تمت المراجعة الطبية من قبل <a href="{doctor}">د. وسيم حبيب</a> · 31 أكتوبر 2026',
 body='''            <p class="lead"><strong>صدّق أو لا تصدّق:</strong> تفاحة، كاسة عصير تفاح، وعلبة مشروب غازي. التلاتة فيهن فركتوز. بس جسمك بيتعامل مع كل واحد منهن بطريقة مختلفة تماماً… لدرجة إنو واحد منهن صديقك، والتاني ممكن يكون عدوك المخبّى.</p>
            <p>خلّينا نفهم القصة من أولها، بدون تعقيد، وبدون ما نحرم حالنا من كل شي حلو 😄</p>

            <h2 class="section-title"><i class="fas fa-cubes-stacked"></i> <span>شو يعني "سكر مصنّع"؟</span></h2>
            <p>لما منحكي عن السكر المصنّع (<bdi>Added Sugar</bdi>)، ما منقصد السكر الموجود طبيعياً جوّا التفاحة أو الحليب. منقصد السكر اللي <strong>انضاف</strong> للأكل، أو انشرب لحالو:</p>
            <ul class="check-list">
                <li><strong>السكر الأبيض (<bdi>Sucrose</bdi>):</strong> هو اللي بالسكرية عندك. وكل حبة منه هي جزيئة جلوكوز (<bdi>Glucose</bdi>) ماسكة إيد جزيئة فركتوز (<bdi>Fructose</bdi>). يعني <strong>نصه جلوكوز ونصه فركتوز.</strong></li>
                <li><strong>شراب الذرة عالي الفركتوز (<bdi>HFCS</bdi>):</strong> مشهور كتير بأمريكا، وبأوروبا بتلاقيه على العبوات باسم <strong><bdi>glucose-fructose syrup</bdi></strong> (وبالهولندي <strong><bdi>glucose-fructosestroop</bdi></strong>). النوع اللي بيستعملوه بالمشروبات فيه حوالي <strong>55% فركتوز.</strong></li>
                <li><strong>العصير:</strong> حتى العصير الطبيعي 100% بلا سكر مضاف. منظمة الصحة العالمية بتحسب سكره من "السكريات الحرة" (<bdi>Free Sugars</bdi>)، متل السكر المضاف بالظبط. ليش؟ رح نعرف بعد شوي.</li>
            </ul>
            <p><strong>والسكر بيحب يتخبّى بأسماء "بريئة":</strong> دكستروز (<bdi>Dextrose</bdi>)، مالتوز (<bdi>Maltose</bdi>)، شراب الجلوكوز، شراب الأرز، مالتوديكسترين (<bdi>Maltodextrin</bdi>)، سكر محوّل (<bdi>Invert Sugar</bdi>)… وكلهن بالآخر سكر. فإذا لقيت تلات أسماء منهن على نفس العبوة، اعرف إنو المنتج مليان سكر، بس موزّع على كذا اسم لحتى ما يطلع أول المكونات 😏</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>وين الخطورة؟ بالكمية وبالسرعة</span></h2>
            <p>ملعقة سكر بالشاي ما بتعمل شي. المشكلة إنو ملعقة السكر بالشاي ما بتضل وحدة: شاي الصبح، وقهوة الضهر، وعلبة مشروب غازي مع الغدا، وقطعة حلو بالمسا…</p>
            <p>خليني أعطيك رقم بيصدم: <strong>علبة مشروب غازي عادي (330 مل) فيها حوالي 35 غ سكر، يعني حوالي 9 معالق صغيرة.</strong> ومنظمة الصحة العالمية بتنصح إنو السكريات الحرة تكون أقل من 10% من سعراتك اليومية، <strong>والأفضل أقل من 5%، يعني حوالي 25 غ (6 معالق صغيرة) بالنهار كله.</strong> يعني علبة وحدة بتخلّص حصتك ليوم ونص!</p>
            <p><strong>والسكر السائل هو الأخطر</strong>، لسببين:</p>
            <ol class="steps">
                <li><strong>بينشرب بسرعة:</strong> علبة كاملة بدقيقتين، فالسكر كله بيوصل مرة وحدة.</li>
                <li><strong>ما بيشبّع:</strong> جسمك ما بيحسب سعرات المشروبات متل ما بيحسب سعرات الأكل، فبتاكل وجبتك العادية فوقها.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-route"></i> <span>قلب القصة: الجلوكوز والفركتوز… أخين، بس كل واحد بطريق</span></h2>
            <p>بيوصلوا سوا للأمعاء، بس من هونيك كل واحد بياخد طريقه:</p>
            <p><strong>الجلوكوز</strong> هو "الوقود الرسمي" للجسم. بيفوت عالدم، وكل خلية بجسمك بتعرف تستعمله: العضلات، والدماغ، والقلب. ولما يرتفع بالدم، البنكرياس بيفرز الإنسولين، والإنسولين بيفتح أبواب الخلايا لحتى يدخل.</p>
            <p><strong>الفركتوز</strong> قصته مختلفة. تقريباً <strong>ما في غير الكبد بيعرف يتعامل معه.</strong> فبيمشي من الأمعاء على الكبد مباشرة، عبر الوريد البابي (<bdi>Portal Vein</bdi>). وهون بتبلش الحكاية.</p>
            <figure class="article-figure">
                <img src="/images/glucose-vs-fructose-liver-metabolism-pathway.webp" alt="مسار الجلوكوز إلى خلايا الجسم مقابل مسار الفركتوز إلى الكبد وتحوّل الفائض إلى دهون" width="1376" height="768" loading="lazy" decoding="async">
                <figcaption>الطريق الأزرق: الجلوكوز رايح لكل خلايا الجسم. الطريق البرتقالي: الفركتوز رايح على الكبد مباشرة، والزيادة بتتحول لدهون.</figcaption>
            </figure>
            <h3>خليني إحكيلك القصة بطريقة تانية 🍽️</h3>
            <p>تخيّل <strong>كبدك مطعم</strong>، والسكر <strong>زباين</strong> جايين ياكلوا.</p>
            <p><strong>الجلوكوز</strong> أغلبه أصلاً بيروح على "مطاعم تانية" بالجسم: العضلات والدماغ والقلب. واللي بيجي منه على مطعمنا بيفوت من <strong>الباب الرئيسي</strong>، وعليه <strong>بوّاب</strong> (هو إنزيم اسمه <bdi>PFK</bdi>، بس خلّينا نسميه أبو سمير 😄). أبو سمير بيشوف المطعم: إذا في طاولات فاضية، بيفوّت الزبون. وإذا المطعم مليان، بيقلو "استنى برّا شوي".</p>
            <p><strong>الفركتوز</strong> جاي على مطعمنا بالذات، وما بيفوت من الباب الرئيسي. بيفوت من <strong>باب المطبخ</strong>، وهونيك <strong>ما في بوّاب!</strong> وصاحب المطعم (الكبد) ما بيقدر يرجّع حدا، مجبور يستقبل كل زبون فات.</p>
            <ul class="check-list">
                <li><strong>إذا الزباين قلال</strong>، صاحب المطعم بيلاقيلهم طاولات فاضية، وبيمشي الحال. يعني الكبد بيحوّل الفركتوز لجلوكوز، أو بيخزّنه كمخزون سريع (<bdi>Glycogen</bdi>).</li>
                <li><strong>بس إذا المطعم أصلاً مليان</strong>، يعني الجلوكوز اللي جاي مع الفركتوز عبّى المخازن ورفع الإنسولين، فما في ولا كرسي فاضي، والزباين عم يفوتوا ورا بعض من باب المطبخ. فشو بيعمل صاحب المطعم؟ <strong>بيصفّهم بالزوايا وبالممرات… فوق بعضهم</strong> 😅 وهاد بالظبط اللي بيصير: الكبد بيحوّل الفركتوز الزايد <strong>لدهون</strong>، وهالعملية إلها اسم علمي: تصنيع الدهون من جديد (<bdi>De Novo Lipogenesis</bdi>).</li>
            </ul>
            <p>وهون المشكلة الحقيقية: الزباين المكدّسين بالزوايا ما بيطلعوا بسهولة. يعني الدهون اللي بتنصنع بالكبد بتضل متكدّسة فيه، وهيك بيبلش <strong>الكبد الدهني</strong> (<bdi>Fatty Liver</bdi>، واسمه العلمي الجديد <bdi>MASLD</bdi>). وقسم منهم صاحب المطعم بيطلّعهم من الباب الخلفي عالشارع، يعني بيطلعوا عالدم كـ<strong>دهون ثلاثية</strong> (<bdi>Triglycerides</bdi>). وكل هالشي بيمشي إيد بإيد مع <strong>مقاومة الإنسولين</strong> (<bdi>Insulin Resistance</bdi>)، اللي حكينا عنها ب<a href="/articles/high-blood-pressure-sugar-insulin.html">مقال الضغط</a>.</p>
            <h3>هل في دليل على هالحكي؟</h3>
            <p>أكيد. بدراسة مشهورة نُشرت سنة 2009، شرب أشخاص عندهم وزن زايد مشروبات محلاة، ربع سعراتهم اليومية منها، لمدة 10 أسابيع. مجموعة شربت مشروبات محلاة <strong>بالفركتوز</strong>، ومجموعة <strong>بالجلوكوز</strong>. والمفاجأة: الاتنين زادوا وزن تقريباً نفس الشي، <strong>بس مجموعة الفركتوز بس</strong> زادت عندها الدهون حوالي الأعضاء بالبطن (<bdi>Visceral Fat</bdi>)، وطلعت الدهون بدمها، ونقصت حساسيتها للإنسولين.</p>
            <p>يعني <strong>نفس السعرات، بس مش نفس الضرر.</strong></p>
            <h3>لحظة… الفركتوز ما بيرفع السكر؟!</h3>
            <p>إيه، وهون في فخ كبير. <strong>المؤشر الجلايسيمي للفركتوز حوالي 15 بس</strong>، بينما الجلوكوز 100 والسكر الأبيض حوالي 65. ليش؟ لأنه الفركتوز ما بيروح عالدم كتير، بيروح عالكبد. فجهاز السكر ما بيشوفه.</p>
            <p>ولهيك بعض المنتجات المليانة فركتوز، متل <strong>شراب الأغاف (<bdi>Agave</bdi>)</strong>، بتتسوّق إنها "منخفضة المؤشر الجلايسيمي"، وكأنها صحية. بس المؤشر المنخفض هون مش معناه إنو المنتج بريء، معناه إنو الحمل كله رايح عالكبد بدل الدم.</p>
            <p><strong>الدرس:</strong> المؤشر الجلايسيمي أداة مفيدة، بس <strong>مش كل شي منخفض المؤشر صحي.</strong> (وشفنا نفس الشي باللقيمات، اللي مؤشرها منخفض بسبب الدهون!)</p>
            <p class="food-links"><a class="food-chip" href="{food:luqaimat}">لقيمات بدبس التمر</a></p>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>طيب… والفاكهة؟ مش فيها فركتوز كمان؟</span></h2>
            <p>فيها، وهاد السؤال اللي بيخوّف ناس كتير لدرجة إنهم بطّلوا ياكلوا فاكهة. بس خلّيني طمّنك: <strong>الفاكهة الكاملة صديقتك</strong>، والسبب بـ4 كلمات: <strong>الكمية، والسرعة، والألياف، والمي.</strong></p>
            <p><strong>1. الكمية صغيرة.</strong> تفاحة متوسطة فيها حوالي 11 غ فركتوز. علبة المشروب الغازي فيها تقريباً 17 لـ19 غ، وبدون أي شي مفيد معها.</p>
            <p class="food-links"><a class="food-chip" href="{food:apple}">تفاح</a></p>
            <p><strong>2. الأمعاء بتحمي الكبد.</strong> بتجارب على الفئران سنة 2018، لقى العلماء إنو <strong>الأمعاء الدقيقة نفسها بتعالج الكميات الصغيرة من الفركتوز</strong> وبتحوّلها لجلوكوز قبل ما توصل للكبد. بس لما تجي الكمية كبيرة ودفعة وحدة، الأمعاء ما بتلحّق، <strong>فبيفيض الفركتوز عالكبد.</strong> والباحثين بيرجّحوا إنو نفس الشي بيصير عند الإنسان.</p>
            <p><strong>3. الألياف بتبطّئ.</strong> الألياف بالتفاحة بتعمل متل الشبكة، وبتخلي السكر يطلع منها على مهلو.</p>
            <p><strong>4. المي بتعبّي.</strong> جرّب تاكل 4 تفاحات ورا بعض. صعبة، صح؟ بس سكر هالـ4 تفاحات ممكن تشربه بكاسة عصير تفاح بدقيقة!</p>
            <p><strong>وهون بيجي تشبيه المطعم مرة تانية:</strong> التفاحة متل <strong>زبون واحد</strong> فايت من باب المطبخ على مهلو، وصاحب المطعم بيلاقيله طاولة بسهولة. أما المشروب الغازي، فهو <strong>باص سياح كامل</strong> نزل كله دفعة وحدة على باب المطبخ 🚌 والمطعم أصلاً مليان… فخمّن وين رح يحطّهم؟ بالزوايا، فوق بعضهم!</p>
            <p><strong>وشو بتقول الدراسات الكبيرة؟</strong> بدراسة ضخمة تابعت أكتر من 180 ألف شخص لسنين طويلة، اللي أكلوا <strong>فاكهة كاملة</strong> أكتر (خصوصاً التوت الأزرق والعنب والتفاح) كان عندهم خطر أقل للإصابة بالسكري من النوع التاني. أما اللي شربوا <strong>عصير</strong> أكتر، فكان خطرهم أعلى.</p>
            <p>يعني <strong>نفس الفاكهة، بس الشكل بيغيّر كل شي.</strong> ولهيك منظمة الصحة العالمية بتحسب سكر العصير متل السكر المضاف.</p>

            <h2 class="section-title"><i class="fas fa-flask"></i> <span>طيب، شو البدائل؟</span></h2>
            <p>إذا بدك حلاوة بدون الحمل على الكبد، في خيارات كتير. بس كل واحد إلو قصته:</p>
            <h3>🌿 الستيفيا (<bdi>Stevia</bdi>)</h3>
            <p>من أوراق نبتة من أمريكا الجنوبية، وأحلى من السكر بحوالي <strong>200 لـ300 مرة.</strong> <strong>بدون سعرات، وما بترفع السكر.</strong> نقطتين بفنجان القهوة بيكفوا. عيبها الوحيد طعمة مُرّة خفيفة إذا زدت الكمية.</p>
            <p><strong>بأوروبا:</strong> مسموحة، ورمزها <bdi>E960</bdi>.</p>
            <p class="food-links"><a class="food-chip" href="{food:liquid-stevia-drops}">قطرات الستيفيا السائلة</a></p>
            <h3>🧊 الإريثريتول (<bdi>Erythritol</bdi>)</h3>
            <p>من عيلة "الكحوليات السكرية" (<bdi>Sugar Alcohols</bdi>)، وحلاوته حوالي <strong>70% من السكر.</strong> <strong>مؤشره الجلايسيمي صفر، وسعراته صفر تقريباً.</strong> السر إنو الجسم بيمتصه، بس ما بيحرقه، وبيطلعه متل ما هو بالبول. يعني بيمرق بالجسم <strong>متل سايح</strong>: بيتفرّج وبيرجع 😄</p>
            <p class="food-links"><a class="food-chip" href="{food:erythritol}">الإريثريتول</a></p>
            <p><strong>بس انتبه لشغلتين:</strong></p>
            <ul class="check-list">
                <li>الهيئة الأوروبية لسلامة الغذاء (<bdi>EFSA</bdi>) راجعته سنة 2023، وحطّت إلو <strong>حد يومي: نص غرام لكل كيلو من وزنك</strong> (يعني حوالي 35 غ لشخص وزنه 70 كيلو). والسبب الأساسي إنو الكميات الكبيرة بتعمل <strong>إسهال.</strong></li>
                <li>دراسة رصدية سنة 2023 لقت إنو اللي عندهم <strong>مستوى إريثريتول عالي بالدم</strong> كان عندهم خطر أعلى لمشاكل القلب. بس انتبه: الجسم نفسه بيصنع إريثريتول، والدراسة ما بتثبت إنو المحلّي هو السبب. فالموضوع لسا قيد البحث، ومنصحك بالاعتدال متل أي شي تاني.</li>
            </ul>
            <h3>💧 السكرالوز (<bdi>Sucralose</bdi>)</h3>
            <p>مصنوع من السكر نفسه بعد تعديل كيميائي، وأحلى منه بحوالي <strong>600 مرة.</strong> <strong>بدون سعرات، وما بيرفع السكر</strong>، وما بيخرب بالحرارة، فبينفع للطبخ والخبز. وبصراحة؟ أنا شخصياً بستعمل نقطتين منه بفنجان القهوة كل يوم ☕</p>
            <p><strong>بأوروبا:</strong> مسموح، ورمزه <bdi>E955</bdi>.</p>
            <h3>🌲 الزيليتول (<bdi>Xylitol</bdi>)</h3>
            <p>كحول سكري تاني، حلاوته قريبة من السكر، <strong>ومؤشره الجلايسيمي حوالي 13.</strong> مشهور بالعلكة لأنه ما بيأذي الأسنان. بس كمان الكميات الكبيرة منه بتعمل إسهال.</p>
            <p><strong>ومعلومة مهمة جداً:</strong> الزيليتول <strong>سام للكلاب</strong> 🐶 حتى كمية صغيرة منه ممكن تكون خطيرة عليهم. فإذا عندك كلب، خلي علكة الزيليتول بعيدة عنه!</p>
            <h3>🍈 فاكهة الراهب (<bdi>Monk Fruit</bdi>) والألولوز (<bdi>Allulose</bdi>)</h3>
            <p>اتنين بتسمع عنهم كتير بالفيديوهات الأمريكية. بس <strong>بأوروبا وضعهم القانوني مختلف:</strong></p>
            <ul class="check-list">
                <li><strong>الألولوز:</strong> لسا <strong>مش مسموح</strong> بالاتحاد الأوروبي. الهيئة الأوروبية (<bdi>EFSA</bdi>) قالت سنة 2025 إنو الملف ما فيه دراسات أمان كافية.</li>
                <li><strong>فاكهة الراهب:</strong> وضعها بأوروبا محدود ومعقّد، فما رح تلاقيها بسهولة متل الستيفيا.</li>
            </ul>
            <p>يعني إذا بتعيش بأوروبا، الستيفيا والإريثريتول والسكرالوز هنّي الخيارات العملية.</p>
            <p><strong>وكلمة حق:</strong> منظمة الصحة العالمية قالت سنة 2023 إنها ما بتنصح بالمحليات بدون سكر كطريقة لتنزيل الوزن، لأنه الدراسات ما بيّنت فايدة واضحة على المدى الطويل. يعني هالمحليات أداة لتخفيف السكر، مش وصفة رجيم. والهدف الحقيقي إنو لسانك يتعوّد شوي شوي على حلاوة أقل 😉</p>

            <h2 class="section-title"><i class="fas fa-jar"></i> <span>"البدائل الطبيعية"… اللي هي بالآخر سكر 🍯</span></h2>
            <p>هون بدنا نكون صريحين، لأنه في منتجات كتير بتتباع على إنها "صحية":</p>
            <table class="sugar-table">
                <thead><tr><th>البديل</th><th>المؤشر الجلايسيمي</th><th>الحقيقة</th></tr></thead>
                <tbody>
                    <tr><td>العسل</td><td>حوالي 61</td><td>سكر طبيعي، وحوالي نص سكره فركتوز</td></tr>
                    <tr><td>سكر جوز الهند</td><td>حوالي 54</td><td>سكر، وسعراته متل السكر الأبيض</td></tr>
                    <tr><td>دبس التمر</td><td>غير متوفر</td><td>سكر مركّز من التمر</td></tr>
                    <tr><td>السكر الأبيض</td><td>حوالي 65</td><td>للمقارنة</td></tr>
                </tbody>
            </table>
            <p class="food-links"><a class="food-chip" href="{food:coconut-sugar}">سكر جوز الهند</a> <a class="food-chip" href="{food:fenugreek-tea-with-honey}">مغلي الحلبة بالعسل</a></p>
            <p><strong>العسل</strong> فيه شوية مركّبات مفيدة، بس الجسم بيتعامل معه كسكر. و<strong>سكر جوز الهند</strong> مكتوب عليه كتير "منخفض المؤشر الجلايسيمي"، بس جامعة سيدني قاسته وطلع حوالي 54، يعني على حافة المنخفض، ومش بعيد كتير عن السكر الأبيض.</p>
            <p>الخلاصة؟ <strong>سكر "طبيعي"… طبيعي إنو يرفعلك السكر</strong> 😄 الكمية هي اللي بتفرق، مش الاسم اللي على العبوة.</p>

            <h2 class="section-title"><i class="fas fa-list-check"></i> <span>كيف تخفف السكر بدون ما تحس إنك محروم؟</span></h2>
            <p>ما حدا بدو يعيش بدون حلو، وما في داعي. هي خطوات عملية فيك تبلش فيها من بكرة:</p>
            <ol class="steps">
                <li><strong>ابدأ بالمشروبات.</strong> إذا عم تشرب مشروبات غازية أو عصير كل يوم، هون أكبر ربح. فيك تستبدلها بمي فوّارة مع ليمون، أو شاي بارد بدون سكر، أو كركديه مثلّج. <a class="food-chip" href="{food:hibiscus-iced-tea}">شاي كركديه بارد أحمر</a></li>
                <li><strong>كول الفاكهة، ما تشربها.</strong> تفاحة بدل كاسة عصير تفاح.</li>
                <li><strong>خفّف المعالق بالتدريج.</strong> إذا بتحط معلقتين بالشاي، خليها معلقة ونص لأسبوعين، بعدين معلقة. لسانك بيتعوّد أسرع مما بتتوقع.</li>
                <li><strong>اقرأ العبوة.</strong> دوّر على "منها سكريات" (<bdi>Sugars</bdi>) بجدول القيم الغذائية، وعلى الأسماء المخبّاية اللي حكينا عنها. وإذا ما عندك وقت تقرأ كل عبوة بالسوبرماركت، خليها علينا 👇</li>
                <li><strong>استعمل المحليات بذكاء.</strong> نقطتين ستيفيا أو سكرالوز بالقهوة والشاي، وإريثريتول للخبز، بس كلهن باعتدال.</li>
                <li><strong>خلي الحلو بعد الأكل، مش لحالو.</strong> قطعة الحلو بعد وجبة فيها بروتين وألياف أخف على السكر من قطعة على معدة فاضية. <a class="food-chip" href="{food:appeltaart}">كعكة التفاح الهولندية</a></li>
                <li><strong>اختار فطورك صح.</strong> رقائق الشوفان الكبيرة مع فاكهة، بدل حبوب الفطور المحلاة. <a class="food-chip" href="{food:gluten-free-rolled-oats}">رقائق شوفان خالية من الغلوتين</a></li>
            </ol>
            <aside class="boodi-card">
                <div>
                    <h2>📱 امسح الباركود مع تطبيق بودي (<bdi>boodi</bdi>)</h2>
                    <p>بالسوبرماركت، كل منتج بيحكي قصة، بس بخط صغير كتير 😄 تطبيق بودي بيقراها عنك: بتمسح الباركود، وبيطلعلك قديش فيه سكر وكربوهيدرات، ومستوى السكر والمؤشر الجلايسيمي، وبيكشفلك المكونات، وبيقترحلك بدائل أقل سكر من نفس الرف.</p>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> اكتشف تطبيق بودي</a>
            </aside>

            <h2 class="section-title"><i class="fas fa-flag-checkered"></i> <span>الخلاصة بسطرين</span></h2>
            <p><strong>الفركتوز بالفاكهة جاي بكمية صغيرة، ومعه ألياف ومي، والأمعاء بتلحّق عليه، فهو صديقك.</strong> أما الفركتوز بالمشروبات والسكر المصنّع، فجاي بكمية كبيرة ودفعة وحدة، فبيفيض على الكبد، وهون بيتحول لدهون. <strong>فما تخاف من التفاحة… خاف من العلبة!</strong> 🍎🥤</p>'''),
en=dict(
 title='Fructose: A Friend in Fruit, a Foe in the Can',
 h1='Fructose: A Friend in Fruit, a Foe in the Can… What\'s the Story?',
 crumb='Fructose and added sugar',
 summary='Why doesn\'t the fructose in an apple hurt you, while the fructose in a soft drink heads for your liver? A simple guide to added sugar, the alternatives, and cutting down.',
 cat='Nutrition',
 desc='Why doesn\'t the fructose in an apple hurt you, while in a soft drink it heads for your liver? Added sugar, the alternatives, and how to cut down.',
 hero_alt='A young man and woman choosing between fresh fruit, sweetened drinks and added sugar',
 about=['Fructose', 'Added sugar', 'Fatty liver disease', 'Sweeteners'],
 refs_label='Sources ▾',
 disclaimer='<strong>Awareness note:</strong> this article is for general awareness about nutrition and lifestyle and does not replace advice from your doctor.',
 review='Medically reviewed by <a href="{doctor}">Dr. Wassim Habib</a> | Founder, WiBo Health · 31 October 2026',
 body='''            <p class="lead"><strong>Believe it or not:</strong> an apple, a glass of apple juice and a can of soft drink. All three contain fructose. But your body handles each of them in a completely different way… so much so that one of them is your friend, and the other may be your hidden enemy.</p>
            <p>Let's understand the story from the beginning, without complications, and without denying ourselves everything sweet 😄</p>

            <h2 class="section-title"><i class="fas fa-cubes-stacked"></i> <span>What does "added sugar" mean?</span></h2>
            <p>When we talk about added sugar, we don't mean the sugar that occurs naturally inside an apple or in milk. We mean the sugar that has been <strong>added</strong> to food, or that is drunk on its own:</p>
            <ul class="check-list">
                <li><strong>White sugar (sucrose):</strong> the one in your sugar bowl. Every grain of it is a glucose molecule holding hands with a fructose molecule. So it is <strong>half glucose and half fructose.</strong></li>
                <li><strong>High-fructose corn syrup (HFCS):</strong> very common in America; in Europe you find it on labels as <strong>glucose-fructose syrup</strong> (in Dutch <strong>glucose-fructosestroop</strong>). The type used in drinks contains about <strong>55% fructose.</strong></li>
                <li><strong>Juice:</strong> even natural 100% juice with no added sugar. The World Health Organization counts its sugar as "free sugars", exactly like added sugar. Why? We'll find out in a moment.</li>
            </ul>
            <p><strong>And sugar loves to hide behind "innocent" names:</strong> dextrose, maltose, glucose syrup, rice syrup, maltodextrin, invert sugar… and in the end they are all sugar. So if you find three of these names on the same pack, you know the product is full of sugar, just spread over several names so it doesn't come first in the ingredients 😏</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Where is the danger? In the amount and the speed</span></h2>
            <p>A spoon of sugar in your tea does nothing. The problem is that the spoon of sugar in your tea doesn't stay just one: tea in the morning, coffee at noon, a can of soft drink with lunch, a piece of cake in the evening…</p>
            <p>Let me give you a shocking number: <strong>a can of regular soft drink (330 ml) contains about 35 g of sugar, which is about 9 teaspoons.</strong> The World Health Organization recommends keeping free sugars below 10% of your daily calories, <strong>and ideally below 5%, which is about 25 g (6 teaspoons) for the whole day.</strong> So one can uses up your allowance for a day and a half!</p>
            <p><strong>And liquid sugar is the most dangerous</strong>, for two reasons:</p>
            <ol class="steps">
                <li><strong>It is drunk fast:</strong> a whole can in two minutes, so all the sugar arrives at once.</li>
                <li><strong>It doesn't fill you up:</strong> your body doesn't count calories from drinks the way it counts calories from food, so you eat your normal meal on top of it.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-route"></i> <span>The heart of the story: glucose and fructose… brothers, but each on its own road</span></h2>
            <p>They reach the gut together, but from there each takes its own road:</p>
            <p><strong>Glucose</strong> is the body's "official fuel". It enters the blood, and every cell in your body knows how to use it: the muscles, the brain and the heart. When it rises in the blood, the pancreas releases insulin, and insulin opens the doors of the cells so it can get in.</p>
            <p><strong>Fructose</strong> has a different story. Almost <strong>only the liver knows how to handle it.</strong> So it travels from the gut straight to the liver, through the portal vein. And that's where the story begins.</p>
            <figure class="article-figure">
                <img src="/images/glucose-vs-fructose-liver-metabolism-pathway.webp" alt="The path of glucose to the body's cells compared with the path of fructose to the liver, where the excess is turned into fat" width="1376" height="768" loading="lazy" decoding="async">
                <figcaption>The blue road: glucose heads to all the cells of the body. The orange road: fructose heads straight to the liver, and the excess is turned into fat.</figcaption>
            </figure>
            <h3>Let me tell you the story another way 🍽️</h3>
            <p>Imagine <strong>your liver is a restaurant</strong>, and the sugar is <strong>customers</strong> coming in to eat.</p>
            <p>Most of the <strong>glucose</strong> goes to "other restaurants" in the body anyway: the muscles, the brain and the heart. Whatever comes to our restaurant enters through the <strong>main door</strong>, which has a <strong>doorman</strong> (an enzyme called PFK, but let's just call him good old Bob 😄). Good old Bob looks around the restaurant: if there are free tables, he lets the customer in. If the restaurant is full, he tells them "wait outside for a bit".</p>
            <p><strong>Fructose</strong> is coming to our restaurant in particular, and it doesn't come in through the main door. It comes in through the <strong>kitchen door</strong>, and there <strong>there is no doorman!</strong> And the owner of the restaurant (the liver) can't turn anyone away; he has to take in every customer who walks in.</p>
            <ul class="check-list">
                <li><strong>If there are only a few customers</strong>, the owner finds them free tables, and everything is fine. That means the liver turns the fructose into glucose, or stores it as a quick reserve (glycogen).</li>
                <li><strong>But if the restaurant is already full</strong>, meaning the glucose that came with the fructose has filled the stores and raised insulin, there isn't a single free chair, and the customers keep coming in one after another through the kitchen door. So what does the owner do? <strong>He lines them up in the corners and the corridors… piled on top of each other</strong> 😅 And that is exactly what happens: the liver turns the excess fructose <strong>into fat</strong>, and this process has a scientific name: de novo lipogenesis.</li>
            </ul>
            <p>And here's the real problem: customers piled up in the corners don't leave easily. That means the fat made in the liver stays piled up inside it, and that is how <strong>fatty liver</strong> begins (its new scientific name is MASLD). Some of them the owner sends out through the back door onto the street, meaning they go out into the blood as <strong>triglycerides</strong>. And all of this goes hand in hand with <strong>insulin resistance</strong>, which we talked about in the <a href="/en/articles/high-blood-pressure-sugar-insulin.html">blood pressure article</a>.</p>
            <h3>Is there evidence for this?</h3>
            <p>Definitely. In a well-known study published in 2009, people with excess weight drank sweetened drinks that made up a quarter of their daily calories, for 10 weeks. One group drank drinks sweetened <strong>with fructose</strong>, and another <strong>with glucose</strong>. The surprise: both gained about the same weight, <strong>but only the fructose group</strong> gained fat around the organs in the belly (visceral fat), saw the fats in their blood go up, and became less sensitive to insulin.</p>
            <p>So <strong>the same calories, but not the same harm.</strong></p>
            <h3>Wait… fructose doesn't raise blood sugar?!</h3>
            <p>Yes, and here is a big trap. <strong>The glycemic index of fructose is only about 15</strong>, while glucose is 100 and white sugar about 65. Why? Because fructose doesn't go into the blood much; it goes to the liver. So the blood sugar meter doesn't see it.</p>
            <p>That's why some products full of fructose, such as <strong>agave syrup</strong>, are marketed as "low glycemic index", as if they were healthy. But a low index here doesn't mean the product is innocent; it means the whole load is going to the liver instead of the blood.</p>
            <p><strong>The lesson:</strong> the glycemic index is a useful tool, but <strong>not everything with a low index is healthy.</strong> (And we saw the same thing with luqaimat, whose index is low because of the fat!)</p>
            <p class="food-links"><a class="food-chip" href="{food:luqaimat}">Luqaimat with Date Syrup</a></p>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>OK… and fruit? Doesn't it contain fructose too?</span></h2>
            <p>It does, and this is the question that scares so many people that they have stopped eating fruit. But let me reassure you: <strong>whole fruit is your friend</strong>, and the reason comes down to 4 words: <strong>amount, speed, fibre and water.</strong></p>
            <p><strong>1. The amount is small.</strong> A medium apple contains about 11 g of fructose. A can of soft drink contains roughly 17 to 19 g, with nothing useful alongside it.</p>
            <p class="food-links"><a class="food-chip" href="{food:apple}">Apple</a></p>
            <p><strong>2. The gut protects the liver.</strong> In experiments on mice in 2018, scientists found that <strong>the small intestine itself processes small amounts of fructose</strong> and turns them into glucose before they reach the liver. But when a large amount comes all at once, the gut can't keep up, <strong>so the fructose spills over into the liver.</strong> The researchers think the same thing likely happens in humans.</p>
            <p><strong>3. Fibre slows things down.</strong> The fibre in an apple works like a net and lets the sugar out slowly.</p>
            <p><strong>4. Water fills you up.</strong> Try eating 4 apples one after another. Hard, right? But you can drink the sugar of those 4 apples in a glass of apple juice in a minute!</p>
            <p><strong>And here the restaurant comparison comes back:</strong> an apple is like <strong>a single customer</strong> strolling in through the kitchen door, and the owner easily finds him a table. A soft drink, though, is <strong>a whole tour bus</strong> unloading all at once at the kitchen door 🚌 and the restaurant is already full… so guess where he'll put them? In the corners, piled on top of each other!</p>
            <p><strong>And what do the big studies say?</strong> In a huge study that followed more than 180,000 people for many years, those who ate more <strong>whole fruit</strong> (especially blueberries, grapes and apples) had a lower risk of type 2 diabetes. But those who drank more <strong>juice</strong> had a higher risk.</p>
            <p>So <strong>the same fruit, but the form changes everything.</strong> That's why the World Health Organization counts the sugar in juice like added sugar.</p>

            <h2 class="section-title"><i class="fas fa-flask"></i> <span>OK, so what are the alternatives?</span></h2>
            <p>If you want sweetness without the load on your liver, there are plenty of options. But each one has its own story:</p>
            <h3>🌿 Stevia</h3>
            <p>From the leaves of a plant from South America, and about <strong>200 to 300 times sweeter than sugar.</strong> <strong>No calories, and it doesn't raise blood sugar.</strong> Two drops in a cup of coffee are enough. Its only drawback is a light bitter taste if you use more.</p>
            <p><strong>In Europe:</strong> permitted, with the code E960.</p>
            <p class="food-links"><a class="food-chip" href="{food:liquid-stevia-drops}">Liquid Stevia Drops</a></p>
            <h3>🧊 Erythritol</h3>
            <p>From the family of "sugar alcohols", with about <strong>70% of the sweetness of sugar.</strong> <strong>Its glycemic index is zero, and its calories are almost zero.</strong> The secret is that the body absorbs it but doesn't burn it, and passes it out unchanged in the urine. So it goes through the body <strong>just passing through like a tourist</strong>: it looks around and goes back home 😄</p>
            <p class="food-links"><a class="food-chip" href="{food:erythritol}">Erythritol</a></p>
            <p><strong>But watch out for two things:</strong></p>
            <ul class="check-list">
                <li>The European Food Safety Authority (EFSA) reviewed it in 2023 and set <strong>a daily limit: half a gram per kilo of your body weight</strong> (about 35 g for a person weighing 70 kilos). The main reason is that large amounts cause <strong>diarrhoea.</strong></li>
                <li>An observational study in 2023 found that people with <strong>high levels of erythritol in their blood</strong> had a higher risk of heart problems. But note: the body makes erythritol itself, and the study doesn't prove that the sweetener is the cause. So the subject is still being researched, and we advise moderation, as with anything else.</li>
            </ul>
            <h3>💧 Sucralose</h3>
            <p>Made from sugar itself after a chemical modification, and about <strong>600 times sweeter.</strong> <strong>No calories, and it doesn't raise blood sugar</strong>, and heat doesn't spoil it, so it works for cooking and baking. And honestly? I personally use two drops of it in my coffee every day ☕</p>
            <p><strong>In Europe:</strong> permitted, with the code E955.</p>
            <h3>🌲 Xylitol</h3>
            <p>Another sugar alcohol, with a sweetness close to sugar, <strong>and a glycemic index of about 13.</strong> Well known in chewing gum because it doesn't harm the teeth. But large amounts of it also cause diarrhoea.</p>
            <p><strong>And a very important fact:</strong> xylitol is <strong>toxic to dogs</strong> 🐶 even a small amount can be dangerous for them. So if you have a dog, keep xylitol gum away from it!</p>
            <h3>🍈 Monk fruit and allulose</h3>
            <p>Two you hear about a lot in American videos. But <strong>in Europe their legal status is different:</strong></p>
            <ul class="check-list">
                <li><strong>Allulose:</strong> still <strong>not permitted</strong> in the European Union. The European authority (EFSA) said in 2025 that the dossier did not contain enough safety studies.</li>
                <li><strong>Monk fruit:</strong> its status in Europe is limited and complicated, so you won't find it as easily as stevia.</li>
            </ul>
            <p>So if you live in Europe, stevia, erythritol and sucralose are the practical options.</p>
            <p><strong>And in all fairness:</strong> in 2023 the World Health Organization said it does not recommend non-sugar sweeteners as a way to lose weight, because studies have not shown a clear long-term benefit. So these sweeteners are a tool for cutting down on sugar, not a diet prescription. The real goal is for your tongue to get used, little by little, to less sweetness 😉</p>

            <h2 class="section-title"><i class="fas fa-jar"></i> <span>"Natural alternatives"… that are sugar in the end 🍯</span></h2>
            <p>Here we need to be honest, because a lot of products are sold as "healthy":</p>
            <table class="sugar-table">
                <thead><tr><th>Alternative</th><th>Glycemic index</th><th>The truth</th></tr></thead>
                <tbody>
                    <tr><td>Honey</td><td>about 61</td><td>A natural sugar, about half of it fructose</td></tr>
                    <tr><td>Coconut sugar</td><td>about 54</td><td>Sugar, with the same calories as white sugar</td></tr>
                    <tr><td>Date syrup</td><td>not available</td><td>Concentrated sugar from dates</td></tr>
                    <tr><td>White sugar</td><td>about 65</td><td>For comparison</td></tr>
                </tbody>
            </table>
            <p class="food-links"><a class="food-chip" href="{food:coconut-sugar}">Coconut Sugar</a> <a class="food-chip" href="{food:fenugreek-tea-with-honey}">Fenugreek Tea with Honey</a></p>
            <p><strong>Honey</strong> contains a few useful compounds, but the body handles it as sugar. And <strong>coconut sugar</strong> often says "low glycemic index" on the pack, but the University of Sydney measured it at about 54, right on the edge of low, and not very far from white sugar.</p>
            <p>The bottom line? <strong>"Natural" sugar… naturally still raises your sugar</strong> 😄 The amount is what makes the difference, not the name on the pack.</p>

            <h2 class="section-title"><i class="fas fa-list-check"></i> <span>How to cut down on sugar without feeling deprived</span></h2>
            <p>Nobody wants to live without sweet things, and there's no need to. Here are practical steps you can start tomorrow:</p>
            <ol class="steps">
                <li><strong>Start with drinks.</strong> If you drink soft drinks or juice every day, this is the biggest win. You can swap them for sparkling water with lemon, unsweetened iced tea, or iced hibiscus. <a class="food-chip" href="{food:hibiscus-iced-tea}">Hibiscus Iced Tea</a></li>
                <li><strong>Eat your fruit, don't drink it.</strong> An apple instead of a glass of apple juice.</li>
                <li><strong>Cut the spoons gradually.</strong> If you put two spoons in your tea, make it one and a half for two weeks, then one. Your tongue gets used to it faster than you think.</li>
                <li><strong>Read the label.</strong> Look for "of which sugars" in the nutrition table, and for the hidden names we talked about. And if you don't have time to read every pack in the supermarket, leave it to us 👇</li>
                <li><strong>Use sweeteners smartly.</strong> Two drops of stevia or sucralose in coffee and tea, and erythritol for baking, but all in moderation.</li>
                <li><strong>Have something sweet after a meal, not on its own.</strong> A sweet after a meal with protein and fibre is gentler on blood sugar than one on an empty stomach. <a class="food-chip" href="{food:appeltaart}">Dutch Apple Pie (Appeltaart)</a></li>
                <li><strong>Choose your breakfast well.</strong> Large rolled oats with fruit, instead of sweetened breakfast cereal. <a class="food-chip" href="{food:gluten-free-rolled-oats}">Gluten-Free Rolled Oats</a></li>
            </ol>
            <aside class="boodi-card">
                <div>
                    <h2>📱 Scan the barcode with the boodi app</h2>
                    <p>In the supermarket, every product tells a story, but in very small print 😄 The boodi app reads it for you: you scan the barcode, and it shows you how much sugar and carbohydrate it contains, its sugar level and glycemic index, reveals the ingredients, and suggests lower-sugar alternatives from the same shelf.</p>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> Discover the boodi app</a>
            </aside>

            <h2 class="section-title"><i class="fas fa-flag-checkered"></i> <span>The bottom line in two sentences</span></h2>
            <p><strong>The fructose in fruit comes in a small amount, together with fibre and water, and the gut keeps up with it, so it is your friend.</strong> The fructose in drinks and added sugar, though, comes in a large amount all at once, so it spills over into the liver, and there it turns into fat. <strong>So don't be afraid of the apple… be afraid of the can!</strong> 🍎🥤</p>'''),
nl=dict(
 title='Fructose: vriend in fruit, vijand in het blikje',
 h1='Fructose: vriend in fruit, vijand in het blikje… hoe zit dat?',
 crumb='Fructose en toegevoegde suiker',
 summary='Waarom schaadt de fructose in een appel je niet, terwijl die in frisdrank naar je lever gaat? Uitleg over toegevoegde suiker, de alternatieven en minder suiker eten.',
 cat='Voeding',
 desc='Waarom schaadt de fructose in een appel je niet, terwijl die in frisdrank naar je lever gaat? Toegevoegde suiker, alternatieven en minder suiker eten.',
 hero_alt='Een jonge man en vrouw kiezen tussen vers fruit, gezoete dranken en toegevoegde suiker',
 about=['Fructose', 'Added sugar', 'Fatty liver disease', 'Sweeteners'],
 refs_label='Bronnen ▾',
 disclaimer='<strong>Bewustwording:</strong> dit artikel is bedoeld voor algemene bewustwording over voeding en leefstijl en vervangt geen advies van je arts.',
 review='Medisch beoordeeld door <a href="{doctor}">Dr. Wassim Habib</a> | Oprichter, WiBo Health · 31 oktober 2026',
 body='''            <p class="lead"><strong>Geloof het of niet:</strong> een appel, een glas appelsap en een blikje frisdrank. Alle drie bevatten fructose. Maar je lichaam gaat met elk ervan op een totaal andere manier om… zo erg zelfs dat de een je vriend is, en de ander misschien je verborgen vijand.</p>
            <p>Laten we het verhaal vanaf het begin begrijpen, zonder ingewikkeld te doen, en zonder onszelf alles wat zoet is te ontzeggen 😄</p>

            <h2 class="section-title"><i class="fas fa-cubes-stacked"></i> <span>Wat betekent "toegevoegde suiker"?</span></h2>
            <p>Als we het over toegevoegde suiker hebben, bedoelen we niet de suiker die van nature in een appel of in melk zit. We bedoelen de suiker die aan eten is <strong>toegevoegd</strong>, of die je los drinkt:</p>
            <ul class="check-list">
                <li><strong>Witte suiker (sacharose):</strong> die in je suikerpot. Elk korreltje ervan is een glucosemolecuul dat hand in hand gaat met een fructosemolecuul. Het is dus <strong>half glucose en half fructose.</strong></li>
                <li><strong>Glucose-fructosestroop (HFCS):</strong> heel bekend in Amerika; in Europa vind je het op verpakkingen als <strong>glucose-fructose syrup</strong> (in het Nederlands <strong>glucose-fructosestroop</strong>). Het soort dat in dranken wordt gebruikt, bevat ongeveer <strong>55% fructose.</strong></li>
                <li><strong>Sap:</strong> zelfs natuurlijk 100% sap zonder toegevoegde suiker. De Wereldgezondheidsorganisatie rekent de suiker erin tot de "vrije suikers", precies zoals toegevoegde suiker. Waarom? Dat lees je zo meteen.</li>
            </ul>
            <p><strong>En suiker verstopt zich graag achter "onschuldige" namen:</strong> dextrose, maltose, glucosestroop, rijststroop, maltodextrine, invertsuiker… en uiteindelijk zijn ze allemaal suiker. Vind je dus drie van deze namen op dezelfde verpakking, dan weet je dat het product vol suiker zit, alleen verdeeld over meerdere namen zodat het niet als eerste ingrediënt verschijnt 😏</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Waar zit het gevaar? In de hoeveelheid en de snelheid</span></h2>
            <p>Eén lepel suiker in je thee doet niets. Het probleem is dat het niet bij die ene lepel suiker in je thee blijft: thee 's ochtends, koffie 's middags, een blikje frisdrank bij de lunch, een stuk taart 's avonds…</p>
            <p>Ik geef je een schokkend getal: <strong>een blikje gewone frisdrank (330 ml) bevat ongeveer 35 g suiker, dat is ongeveer 9 theelepels.</strong> De Wereldgezondheidsorganisatie raadt aan om vrije suikers onder de 10% van je dagelijkse calorieën te houden, <strong>en liefst onder de 5%, dat is ongeveer 25 g (6 theelepels) voor de hele dag.</strong> Eén blikje gebruikt dus je hele portie voor anderhalve dag op!</p>
            <p><strong>En vloeibare suiker is het gevaarlijkst</strong>, om twee redenen:</p>
            <ol class="steps">
                <li><strong>Het is snel op:</strong> een heel blikje in twee minuten, dus alle suiker komt in één keer binnen.</li>
                <li><strong>Het vult niet:</strong> je lichaam telt calorieën uit dranken niet zoals calorieën uit eten, dus je eet je gewone maaltijd er gewoon bovenop.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-route"></i> <span>De kern van het verhaal: glucose en fructose… broers, maar elk met een eigen weg</span></h2>
            <p>Ze komen samen in de darm aan, maar vanaf daar gaat elk zijn eigen weg:</p>
            <p><strong>Glucose</strong> is de "officiële brandstof" van het lichaam. Het gaat het bloed in, en elke cel in je lichaam weet hoe ze het moet gebruiken: de spieren, de hersenen en het hart. Als het in het bloed stijgt, maakt de alvleesklier insuline aan, en insuline opent de deuren van de cellen zodat het naar binnen kan.</p>
            <p><strong>Fructose</strong> heeft een ander verhaal. Bijna <strong>alleen de lever weet ermee om te gaan.</strong> Het gaat dus van de darm rechtstreeks naar de lever, via de poortader. En daar begint het verhaal.</p>
            <figure class="article-figure">
                <img src="/images/glucose-vs-fructose-liver-metabolism-pathway.webp" alt="De weg van glucose naar de cellen van het lichaam tegenover de weg van fructose naar de lever, waar het overschot in vet wordt omgezet" width="1376" height="768" loading="lazy" decoding="async">
                <figcaption>De blauwe weg: glucose gaat naar alle cellen van het lichaam. De oranje weg: fructose gaat rechtstreeks naar de lever, en het overschot wordt omgezet in vet.</figcaption>
            </figure>
            <h3>Ik vertel je het verhaal nog eens op een andere manier 🍽️</h3>
            <p>Stel je voor dat <strong>je lever een restaurant is</strong>, en de suiker zijn <strong>gasten</strong> die komen eten.</p>
            <p>Het meeste <strong>glucose</strong> gaat sowieso naar "andere restaurants" in het lichaam: de spieren, de hersenen en het hart. Wat naar ons restaurant komt, gaat naar binnen via de <strong>hoofdingang</strong>, en daar staat <strong>een portier</strong> (een enzym dat PFK heet, maar laten we hem gewoon de portier noemen 😄). De portier kijkt rond in het restaurant: zijn er tafels vrij, dan laat hij de gast binnen. Zit het restaurant vol, dan zegt hij "wacht even buiten".</p>
            <p><strong>Fructose</strong> komt juist naar ons restaurant, en komt niet via de hoofdingang binnen. Het komt binnen via de <strong>keukendeur</strong>, en daar <strong>staat geen portier!</strong> En de eigenaar van het restaurant (de lever) kan niemand wegsturen; hij moet elke gast die binnenkomt ontvangen.</p>
            <ul class="check-list">
                <li><strong>Als er maar weinig gasten zijn</strong>, vindt de eigenaar vrije tafels voor ze, en gaat alles goed. Dat betekent dat de lever de fructose omzet in glucose, of opslaat als snelle voorraad (glycogeen).</li>
                <li><strong>Maar als het restaurant al vol zit</strong>, dus als de glucose die met de fructose meekwam de voorraden heeft gevuld en de insuline heeft verhoogd, is er geen enkele stoel meer vrij, en blijven de gasten na elkaar via de keukendeur binnenkomen. Wat doet de eigenaar dan? <strong>Hij zet ze in de hoeken en de gangen… op elkaar gepropt</strong> 😅 En dat is precies wat er gebeurt: de lever zet de overtollige fructose om <strong>in vet</strong>, en dat proces heeft een wetenschappelijke naam: de novo lipogenese.</li>
            </ul>
            <p>En hier zit het echte probleem: gasten die in de hoeken op elkaar gepropt zitten, gaan niet makkelijk weg. Dat betekent dat het vet dat in de lever wordt gemaakt daar opgestapeld blijft, en zo begint <strong>leververvetting</strong> (de nieuwe wetenschappelijke naam is MASLD). Een deel van de gasten stuurt de eigenaar via de achterdeur de straat op, dat wil zeggen dat ze als <strong>triglyceriden</strong> in het bloed terechtkomen. En dit alles gaat hand in hand met <strong>insulineresistentie</strong>, waar we het in het <a href="/nl/articles/hoge-bloeddruk-suiker-insuline.html">artikel over bloeddruk</a> over hadden.</p>
            <h3>Is daar bewijs voor?</h3>
            <p>Zeker. In een bekende studie die in 2009 werd gepubliceerd, dronken mensen met overgewicht 10 weken lang gezoete dranken die een kwart van hun dagelijkse calorieën leverden. De ene groep dronk dranken gezoet <strong>met fructose</strong>, de andere <strong>met glucose</strong>. De verrassing: beide groepen kwamen ongeveer evenveel aan, <strong>maar alleen de fructosegroep</strong> kreeg meer vet rond de organen in de buik (visceraal vet), zag de vetten in het bloed stijgen, en werd minder gevoelig voor insuline.</p>
            <p>Dus <strong>dezelfde calorieën, maar niet dezelfde schade.</strong></p>
            <h3>Wacht even… fructose verhoogt de bloedsuiker niet?!</h3>
            <p>Klopt, en hier zit een grote valkuil. <strong>De glykemische index van fructose is maar ongeveer 15</strong>, terwijl glucose 100 is en witte suiker ongeveer 65. Waarom? Omdat fructose niet veel in het bloed komt; het gaat naar de lever. De bloedsuikermeter ziet het dus niet.</p>
            <p>Daarom worden sommige producten vol fructose, zoals <strong>agavesiroop</strong>, verkocht als "lage glykemische index", alsof ze gezond zijn. Maar een lage index betekent hier niet dat het product onschuldig is; het betekent dat de hele last naar de lever gaat in plaats van naar het bloed.</p>
            <p><strong>De les:</strong> de glykemische index is een handig hulpmiddel, maar <strong>niet alles met een lage index is gezond.</strong> (En dat zagen we ook bij luqaimat, die een lage index hebben door het vet!)</p>
            <p class="food-links"><a class="food-chip" href="{food:luqaimat}">Luqaimat met dadelstroop</a></p>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>Oké… en fruit? Daar zit toch ook fructose in?</span></h2>
            <p>Klopt, en dat is de vraag die zoveel mensen bang maakt dat ze geen fruit meer eten. Maar laat me je geruststellen: <strong>heel fruit is je vriend</strong>, en de reden zit in 4 woorden: <strong>hoeveelheid, snelheid, vezels en water.</strong></p>
            <p><strong>1. De hoeveelheid is klein.</strong> Een middelgrote appel bevat ongeveer 11 g fructose. Een blikje frisdrank bevat ongeveer 17 tot 19 g, zonder iets nuttigs erbij.</p>
            <p class="food-links"><a class="food-chip" href="{food:apple}">Appel</a></p>
            <p><strong>2. De darm beschermt de lever.</strong> In experimenten met muizen in 2018 ontdekten wetenschappers dat <strong>de dunne darm zelf kleine hoeveelheden fructose verwerkt</strong> en omzet in glucose voordat ze de lever bereiken. Maar als er een grote hoeveelheid in één keer komt, kan de darm het niet bijhouden, <strong>en stroomt de fructose door naar de lever.</strong> De onderzoekers denken dat hetzelfde waarschijnlijk bij mensen gebeurt.</p>
            <p><strong>3. Vezels vertragen.</strong> De vezels in een appel werken als een net en laten de suiker er rustig uit.</p>
            <p><strong>4. Water vult.</strong> Probeer eens 4 appels na elkaar te eten. Lastig, toch? Maar de suiker van die 4 appels drink je in een glas appelsap in één minuut!</p>
            <p><strong>En hier komt de vergelijking met het restaurant weer terug:</strong> een appel is als <strong>één gast</strong> die rustig via de keukendeur binnenkomt, en de eigenaar vindt makkelijk een tafel voor hem. Frisdrank daarentegen is <strong>een complete touringbus</strong> die in één keer bij de keukendeur uitstapt 🚌 en het restaurant zit al vol… dus raad eens waar hij ze zet? In de hoeken, op elkaar gepropt!</p>
            <p><strong>En wat zeggen de grote studies?</strong> In een enorme studie die meer dan 180.000 mensen vele jaren volgde, hadden mensen die meer <strong>heel fruit</strong> aten (vooral blauwe bessen, druiven en appels) een lager risico op diabetes type 2. Maar mensen die meer <strong>sap</strong> dronken, hadden een hoger risico.</p>
            <p>Dus <strong>hetzelfde fruit, maar de vorm verandert alles.</strong> Daarom rekent de Wereldgezondheidsorganisatie de suiker in sap net als toegevoegde suiker.</p>

            <h2 class="section-title"><i class="fas fa-flask"></i> <span>Oké, wat zijn dan de alternatieven?</span></h2>
            <p>Wil je zoetheid zonder de last voor je lever, dan zijn er veel opties. Maar elk heeft zijn eigen verhaal:</p>
            <h3>🌿 Stevia</h3>
            <p>Van de bladeren van een plant uit Zuid-Amerika, en ongeveer <strong>200 tot 300 keer zoeter dan suiker.</strong> <strong>Geen calorieën, en het verhoogt de bloedsuiker niet.</strong> Twee druppels in een kop koffie zijn genoeg. Het enige nadeel is een licht bittere smaak als je meer gebruikt.</p>
            <p><strong>In Europa:</strong> toegestaan, met de code E960.</p>
            <p class="food-links"><a class="food-chip" href="{food:liquid-stevia-drops}">Vloeibare steviadruppels</a></p>
            <h3>🧊 Erythritol</h3>
            <p>Uit de familie van de "suikeralcoholen", met ongeveer <strong>70% van de zoetkracht van suiker.</strong> <strong>De glykemische index is nul, en de calorieën zijn bijna nul.</strong> Het geheim is dat het lichaam het opneemt, maar niet verbrandt, en onveranderd met de urine uitscheidt. Het gaat dus door het lichaam en <strong>komt alleen even langs, als een toerist</strong>: het kijkt rond en gaat weer naar huis 😄</p>
            <p class="food-links"><a class="food-chip" href="{food:erythritol}">Erythritol (zoetstof)</a></p>
            <p><strong>Maar let op twee dingen:</strong></p>
            <ul class="check-list">
                <li>De Europese Autoriteit voor Voedselveiligheid (EFSA) heeft het in 2023 opnieuw beoordeeld en <strong>een dagelijkse limiet</strong> vastgesteld: <strong>een halve gram per kilo lichaamsgewicht</strong> (ongeveer 35 g voor iemand van 70 kilo). De belangrijkste reden is dat grote hoeveelheden <strong>diarree</strong> geven.</li>
                <li>Een observationele studie uit 2023 vond dat mensen met <strong>een hoog erythritolgehalte in het bloed</strong> een hoger risico op hartproblemen hadden. Maar let op: het lichaam maakt zelf erythritol, en de studie bewijst niet dat de zoetstof de oorzaak is. Het onderwerp wordt dus nog onderzocht, en we raden aan om het met mate te gebruiken, zoals alles.</li>
            </ul>
            <h3>💧 Sucralose</h3>
            <p>Gemaakt van suiker zelf na een chemische aanpassing, en ongeveer <strong>600 keer zoeter.</strong> <strong>Geen calorieën, en het verhoogt de bloedsuiker niet</strong>, en het kan tegen hitte, dus het is geschikt om mee te koken en te bakken. En eerlijk gezegd? Ik gebruik zelf elke dag twee druppels ervan in mijn koffie ☕</p>
            <p><strong>In Europa:</strong> toegestaan, met de code E955.</p>
            <h3>🌲 Xylitol</h3>
            <p>Nog een suikeralcohol, met een zoetheid die dicht bij suiker ligt, <strong>en een glykemische index van ongeveer 13.</strong> Bekend van kauwgom omdat het de tanden niet beschadigt. Maar ook hiervan geven grote hoeveelheden diarree.</p>
            <p><strong>En een heel belangrijk weetje:</strong> xylitol is <strong>giftig voor honden</strong> 🐶 zelfs een kleine hoeveelheid kan gevaarlijk voor ze zijn. Heb je een hond, houd xylitolkauwgom dan uit zijn buurt!</p>
            <h3>🍈 Monniksvrucht en allulose</h3>
            <p>Twee waar je veel over hoort in Amerikaanse video's. Maar <strong>in Europa is hun wettelijke status anders:</strong></p>
            <ul class="check-list">
                <li><strong>Allulose:</strong> nog <strong>niet toegestaan</strong> in de Europese Unie. De Europese autoriteit (EFSA) zei in 2025 dat het dossier niet genoeg veiligheidsstudies bevatte.</li>
                <li><strong>Monniksvrucht:</strong> de status in Europa is beperkt en ingewikkeld, dus je vindt het niet zo makkelijk als stevia.</li>
            </ul>
            <p>Woon je in Europa, dan zijn stevia, erythritol en sucralose de praktische opties.</p>
            <p><strong>En eerlijk is eerlijk:</strong> de Wereldgezondheidsorganisatie zei in 2023 dat ze zoetstoffen zonder suiker niet aanraadt als manier om af te vallen, omdat studies geen duidelijk voordeel op lange termijn hebben laten zien. Deze zoetstoffen zijn dus een hulpmiddel om minder suiker te gebruiken, geen dieetrecept. Het echte doel is dat je tong stukje bij beetje went aan minder zoetheid 😉</p>

            <h2 class="section-title"><i class="fas fa-jar"></i> <span>"Natuurlijke alternatieven"… die uiteindelijk gewoon suiker zijn 🍯</span></h2>
            <p>Hier moeten we eerlijk zijn, want veel producten worden verkocht als "gezond":</p>
            <table class="sugar-table">
                <thead><tr><th>Alternatief</th><th>Glykemische index</th><th>De waarheid</th></tr></thead>
                <tbody>
                    <tr><td>Honing</td><td>ongeveer 61</td><td>Natuurlijke suiker, ongeveer de helft is fructose</td></tr>
                    <tr><td>Kokossuiker</td><td>ongeveer 54</td><td>Suiker, met evenveel calorieën als witte suiker</td></tr>
                    <tr><td>Dadelstroop</td><td>niet beschikbaar</td><td>Geconcentreerde suiker uit dadels</td></tr>
                    <tr><td>Witte suiker</td><td>ongeveer 65</td><td>Ter vergelijking</td></tr>
                </tbody>
            </table>
            <p class="food-links"><a class="food-chip" href="{food:coconut-sugar}">Kokossuiker</a> <a class="food-chip" href="{food:fenugreek-tea-with-honey}">Fenegriekthee met honing</a></p>
            <p><strong>Honing</strong> bevat een paar nuttige stoffen, maar het lichaam verwerkt het als suiker. En op <strong>kokossuiker</strong> staat vaak "lage glykemische index", maar de Universiteit van Sydney mat het op ongeveer 54, precies op de grens van laag, en niet ver van witte suiker.</p>
            <p>De conclusie? <strong>"Natuurlijke" suiker… verhoogt natuurlijk nog steeds je suiker</strong> 😄 De hoeveelheid maakt het verschil, niet de naam op de verpakking.</p>

            <h2 class="section-title"><i class="fas fa-list-check"></i> <span>Minder suiker zonder je tekort te voelen</span></h2>
            <p>Niemand wil zonder zoetigheid leven, en dat hoeft ook niet. Hier zijn praktische stappen waar je morgen mee kunt beginnen:</p>
            <ol class="steps">
                <li><strong>Begin bij de dranken.</strong> Drink je elke dag frisdrank of sap, dan valt hier de grootste winst te halen. Je kunt ze vervangen door bruisend water met citroen, ijsthee zonder suiker, of ijskoude hibiscusthee. <a class="food-chip" href="{food:hibiscus-iced-tea}">Hibiscusthee koud</a></li>
                <li><strong>Eet je fruit, drink het niet.</strong> Een appel in plaats van een glas appelsap.</li>
                <li><strong>Minder de lepels geleidelijk.</strong> Doe je twee lepels in je thee, maak er dan twee weken lang anderhalve lepel van, daarna één. Je tong went er sneller aan dan je denkt.</li>
                <li><strong>Lees het etiket.</strong> Zoek naar "waarvan suikers" in de voedingswaardetabel, en naar de verborgen namen waar we het over hadden. En heb je geen tijd om elke verpakking in de supermarkt te lezen, laat dat dan aan ons over 👇</li>
                <li><strong>Gebruik zoetstoffen slim.</strong> Twee druppels stevia of sucralose in koffie en thee, en erythritol om te bakken, maar alles met mate.</li>
                <li><strong>Eet iets zoets na de maaltijd, niet los.</strong> Iets zoets na een maaltijd met eiwit en vezels is milder voor de bloedsuiker dan op een lege maag. <a class="food-chip" href="{food:appeltaart}">Hollandse appeltaart</a></li>
                <li><strong>Kies je ontbijt goed.</strong> Grote havervlokken met fruit, in plaats van gezoete ontbijtgranen. <a class="food-chip" href="{food:gluten-free-rolled-oats}">Glutenvrije havervlokken</a></li>
            </ol>
            <aside class="boodi-card">
                <div>
                    <h2>📱 Scan de barcode met de boodi-app</h2>
                    <p>In de supermarkt vertelt elk product een verhaal, maar in heel kleine letters 😄 De boodi-app leest het voor je: je scant de barcode, en de app laat zien hoeveel suiker en koolhydraten erin zitten, het suikerniveau en de glykemische index, onthult de ingrediënten, en stelt alternatieven met minder suiker uit hetzelfde schap voor.</p>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> Ontdek de boodi-app</a>
            </aside>

            <h2 class="section-title"><i class="fas fa-flag-checkered"></i> <span>De conclusie in twee zinnen</span></h2>
            <p><strong>De fructose in fruit komt in een kleine hoeveelheid, samen met vezels en water, en de darm kan het bijhouden, dus het is je vriend.</strong> De fructose in dranken en toegevoegde suiker komt daarentegen in een grote hoeveelheid in één keer, dus het stroomt door naar de lever, en daar wordt het omgezet in vet. <strong>Wees dus niet bang voor de appel… wees bang voor het blikje!</strong> 🍎🥤</p>'''),
sv=dict(
 title='Fruktos: en vän i frukten, en fiende i burken',
 h1='Fruktos: en vän i frukten, en fiende i burken… vad är grejen?',
 crumb='Fruktos och tillsatt socker',
 summary='Varför skadar fruktosen i ett äpple dig inte, medan fruktosen i läsk går till levern? En enkel guide om tillsatt socker, alternativen och hur du drar ner.',
 cat='Kost',
 desc='Varför skadar fruktosen i ett äpple dig inte, medan den i läsk går till levern? Tillsatt socker, alternativen och hur du drar ner på sockret.',
 hero_alt='En ung man och kvinna väljer mellan färsk frukt, sötade drycker och tillsatt socker',
 about=['Fructose', 'Added sugar', 'Fatty liver disease', 'Sweeteners'],
 refs_label='Källor ▾',
 disclaimer='<strong>Upplysning:</strong> den här artikeln är allmän information om kost och livsstil och ersätter inte råd från din läkare.',
 review='Medicinskt granskad av <a href="{doctor}">Dr. Wassim Habib</a> | Grundare, WiBo Health · 31 oktober 2026',
 body='''            <p class="lead"><strong>Tro det eller ej:</strong> ett äpple, ett glas äppeljuice och en burk läsk. Alla tre innehåller fruktos. Men kroppen hanterar var och en av dem på ett helt olika sätt… så mycket att den ena är din vän, och den andra kan vara din dolda fiende.</p>
            <p>Låt oss förstå historien från början, utan krångel, och utan att förneka oss allt som är sött 😄</p>

            <h2 class="section-title"><i class="fas fa-cubes-stacked"></i> <span>Vad betyder "tillsatt socker"?</span></h2>
            <p>När vi pratar om tillsatt socker menar vi inte sockret som finns naturligt i ett äpple eller i mjölk. Vi menar sockret som har <strong>tillsatts</strong> i maten, eller som dricks för sig:</p>
            <ul class="check-list">
                <li><strong>Vitt socker (sackaros):</strong> det i din sockerskål. Varje korn är en glukosmolekyl som håller en fruktosmolekyl i handen. Det är alltså <strong>hälften glukos och hälften fruktos.</strong></li>
                <li><strong>Majssirap med hög fruktoshalt (HFCS):</strong> mycket vanlig i USA; i Europa hittar du den på förpackningar som <strong>glucose-fructose syrup</strong> (på nederländska <strong>glucose-fructosestroop</strong>). Den sort som används i drycker innehåller cirka <strong>55 % fruktos.</strong></li>
                <li><strong>Juice:</strong> även naturlig 100 % juice utan tillsatt socker. Världshälsoorganisationen räknar sockret i den som "fria sockerarter", precis som tillsatt socker. Varför? Det får du veta strax.</li>
            </ul>
            <p><strong>Och socker gömmer sig gärna bakom "oskyldiga" namn:</strong> dextros, maltos, glukossirap, rissirap, maltodextrin, invertsocker… och till sist är de alla socker. Hittar du alltså tre av de här namnen på samma förpackning vet du att produkten är full av socker, bara utspritt på flera namn så att det inte hamnar först bland ingredienserna 😏</p>

            <h2 class="section-title"><i class="fas fa-triangle-exclamation"></i> <span>Var ligger faran? I mängden och hastigheten</span></h2>
            <p>En sked socker i teet gör ingenting. Problemet är att skeden socker i teet inte stannar vid en: te på morgonen, kaffe vid lunch, en burk läsk till maten, en bit kaka på kvällen…</p>
            <p>Här är en chockerande siffra: <strong>en burk vanlig läsk (330 ml) innehåller cirka 35 g socker, ungefär 9 teskedar.</strong> Världshälsoorganisationen rekommenderar att fria sockerarter står för mindre än 10 % av dina dagliga kalorier, <strong>och helst mindre än 5 %, alltså cirka 25 g (6 teskedar) för hela dagen.</strong> En enda burk förbrukar alltså din ranson för en och en halv dag!</p>
            <p><strong>Och flytande socker är farligast</strong>, av två skäl:</p>
            <ol class="steps">
                <li><strong>Det dricks snabbt:</strong> en hel burk på två minuter, så allt socker kommer på en gång.</li>
                <li><strong>Det mättar inte:</strong> kroppen räknar inte kalorier från drycker på samma sätt som kalorier från mat, så du äter din vanliga måltid ovanpå.</li>
            </ol>

            <h2 class="section-title"><i class="fas fa-route"></i> <span>Kärnan i historien: glukos och fruktos… bröder, men var och en på sin egen väg</span></h2>
            <p>De kommer till tarmen tillsammans, men därifrån går var och en sin egen väg:</p>
            <p><strong>Glukos</strong> är kroppens "officiella bränsle". Det går ut i blodet, och varje cell i kroppen vet hur den ska använda det: musklerna, hjärnan och hjärtat. När det stiger i blodet utsöndrar bukspottkörteln insulin, och insulinet öppnar cellernas dörrar så att det kan komma in.</p>
            <p><strong>Fruktos</strong> har en annan historia. Nästan <strong>bara levern vet hur den ska hanteras.</strong> Den går alltså från tarmen direkt till levern, via portådern. Och där börjar historien.</p>
            <figure class="article-figure">
                <img src="/images/glucose-vs-fructose-liver-metabolism-pathway.webp" alt="Glukosens väg till kroppens celler jämfört med fruktosens väg till levern, där överskottet omvandlas till fett" width="1376" height="768" loading="lazy" decoding="async">
                <figcaption>Den blå vägen: glukos går till alla kroppens celler. Den orange vägen: fruktos går direkt till levern, och överskottet omvandlas till fett.</figcaption>
            </figure>
            <h3>Låt mig berätta historien på ett annat sätt 🍽️</h3>
            <p>Föreställ dig att <strong>din lever är en restaurang</strong>, och sockret är <strong>gäster</strong> som kommer för att äta.</p>
            <p>Det mesta av <strong>glukosen</strong> går ändå till "andra restauranger" i kroppen: musklerna, hjärnan och hjärtat. Det som kommer till vår restaurang går in genom <strong>huvudingången</strong>, och där står en <strong>dörrvakt</strong> (ett enzym som heter PFK, men vi kallar honom bara dörrvakten 😄). Dörrvakten ser sig om i restaurangen: finns det lediga bord släpper han in gästen. Är restaurangen full säger han "vänta utanför en stund".</p>
            <p><strong>Fruktosen</strong> kommer just till vår restaurang, och den går inte in genom huvudingången. Den går in genom <strong>köksdörren</strong>, och där <strong>finns ingen dörrvakt!</strong> Och restaurangägaren (levern) kan inte avvisa någon; han måste ta emot varje gäst som kommer in.</p>
            <ul class="check-list">
                <li><strong>Om det bara är några få gäster</strong> hittar ägaren lediga bord åt dem, och allt går bra. Det betyder att levern omvandlar fruktosen till glukos, eller lagrar den som ett snabbt förråd (glykogen).</li>
                <li><strong>Men om restaurangen redan är full</strong>, alltså om glukosen som kom med fruktosen har fyllt förråden och höjt insulinet, finns det inte en enda ledig stol, och gästerna fortsätter att komma in efter varandra genom köksdörren. Vad gör ägaren då? <strong>Han ställer dem i hörnen och korridorerna… staplade på varandra</strong> 😅 Och det är precis det som händer: levern omvandlar överskottet av fruktos <strong>till fett</strong>, och den processen har ett vetenskapligt namn: de novo-lipogenes.</li>
            </ul>
            <p>Och här ligger det verkliga problemet: gäster som staplats i hörnen går inte lätt därifrån. Det betyder att fettet som bildas i levern blir kvar och staplas där, och så börjar <strong>fettlever</strong> (det nya vetenskapliga namnet är MASLD). En del av gästerna skickar ägaren ut genom bakdörren på gatan, alltså går de ut i blodet som <strong>triglycerider</strong>. Och allt detta går hand i hand med <strong>insulinresistens</strong>, som vi pratade om i <a href="/sv/articles/hogt-blodtryck-socker-insulin.html">artikeln om blodtryck</a>.</p>
            <h3>Finns det bevis för det här?</h3>
            <p>Absolut. I en känd studie som publicerades 2009 drack personer med övervikt sötade drycker som stod för en fjärdedel av deras dagliga kalorier, i 10 veckor. En grupp drack drycker sötade <strong>med fruktos</strong>, och en annan <strong>med glukos</strong>. Överraskningen: båda gick upp ungefär lika mycket i vikt, <strong>men bara fruktosgruppen</strong> fick mer fett runt organen i buken (visceralt fett), fick högre blodfetter och blev mindre känslig för insulin.</p>
            <p>Alltså <strong>samma kalorier, men inte samma skada.</strong></p>
            <h3>Vänta… fruktos höjer inte blodsockret?!</h3>
            <p>Just det, och här finns en stor fälla. <strong>Det glykemiska indexet för fruktos är bara cirka 15</strong>, medan glukos är 100 och vitt socker cirka 65. Varför? För att fruktos inte går ut i blodet särskilt mycket; den går till levern. Blodsockermätaren ser den alltså inte.</p>
            <p>Därför marknadsförs vissa produkter fulla av fruktos, som <strong>agavesirap</strong>, som "lågt glykemiskt index", som om de vore nyttiga. Men ett lågt index betyder här inte att produkten är oskyldig; det betyder att hela belastningen går till levern i stället för till blodet.</p>
            <p><strong>Lärdomen:</strong> det glykemiska indexet är ett användbart verktyg, men <strong>allt med lågt index är inte nyttigt.</strong> (Och samma sak såg vi med luqaimat, som har lågt index på grund av fettet!)</p>
            <p class="food-links"><a class="food-chip" href="{food:luqaimat}">Luqaimat med dadelsirap</a></p>

            <h2 class="section-title"><i class="fas fa-apple-whole"></i> <span>Okej… och frukt? Innehåller den inte också fruktos?</span></h2>
            <p>Jo, och det är frågan som skrämmer så många att de har slutat äta frukt. Men låt mig lugna dig: <strong>hel frukt är din vän</strong>, och skälet ryms i 4 ord: <strong>mängd, hastighet, fibrer och vatten.</strong></p>
            <p><strong>1. Mängden är liten.</strong> Ett medelstort äpple innehåller cirka 11 g fruktos. En burk läsk innehåller ungefär 17 till 19 g, och inget nyttigt alls följer med.</p>
            <p class="food-links"><a class="food-chip" href="{food:apple}">Äpple</a></p>
            <p><strong>2. Tarmen skyddar levern.</strong> I försök på möss 2018 upptäckte forskare att <strong>tunntarmen själv tar hand om små mängder fruktos</strong> och omvandlar dem till glukos innan de når levern. Men när en stor mängd kommer på en gång hinner tarmen inte med, <strong>så fruktosen svämmar över till levern.</strong> Forskarna tror att samma sak sannolikt sker hos människor.</p>
            <p><strong>3. Fibrer bromsar.</strong> Fibrerna i ett äpple fungerar som ett nät och släpper ut sockret i lugn takt.</p>
            <p><strong>4. Vatten mättar.</strong> Försök äta 4 äpplen efter varandra. Svårt, eller hur? Men sockret från de 4 äpplena kan du dricka i ett glas äppeljuice på en minut!</p>
            <p><strong>Och här kommer restaurangliknelsen tillbaka:</strong> ett äpple är som <strong>en enda gäst</strong> som lugnt kommer in genom köksdörren, och ägaren hittar lätt ett bord åt honom. Läsk däremot är <strong>en hel turistbuss</strong> som släpper av alla på en gång vid köksdörren 🚌 och restaurangen är redan full… så gissa var han ställer dem? I hörnen, staplade på varandra!</p>
            <p><strong>Och vad säger de stora studierna?</strong> I en jättestudie som följde mer än 180 000 personer i många år hade de som åt mer <strong>hel frukt</strong> (särskilt blåbär, vindruvor och äpplen) lägre risk för typ 2-diabetes. Men de som drack mer <strong>juice</strong> hade högre risk.</p>
            <p>Alltså <strong>samma frukt, men formen ändrar allt.</strong> Därför räknar Världshälsoorganisationen sockret i juice som tillsatt socker.</p>

            <h2 class="section-title"><i class="fas fa-flask"></i> <span>Okej, vilka är alternativen?</span></h2>
            <p>Vill du ha sötma utan belastningen på levern finns det många alternativ. Men vart och ett har sin egen historia:</p>
            <h3>🌿 Stevia</h3>
            <p>Från bladen av en växt från Sydamerika, och cirka <strong>200 till 300 gånger sötare än socker.</strong> <strong>Inga kalorier, och den höjer inte blodsockret.</strong> Två droppar i en kopp kaffe räcker. Den enda nackdelen är en lätt besk smak om du tar mer.</p>
            <p><strong>I Europa:</strong> tillåten, med koden E960.</p>
            <p class="food-links"><a class="food-chip" href="{food:liquid-stevia-drops}">Flytande steviadroppar</a></p>
            <h3>🧊 Erytritol</h3>
            <p>Från familjen "sockeralkoholer", med cirka <strong>70 % av sockrets sötma.</strong> <strong>Dess glykemiska index är noll, och kalorierna nästan noll.</strong> Hemligheten är att kroppen tar upp det men inte förbränner det, och utsöndrar det oförändrat med urinen. Det går alltså genom kroppen <strong>bara på genomresa, som en turist</strong>: det tittar sig omkring och åker hem igen 😄</p>
            <p class="food-links"><a class="food-chip" href="{food:erythritol}">Erytritol (sötningsmedel)</a></p>
            <p><strong>Men se upp med två saker:</strong></p>
            <ul class="check-list">
                <li>Europeiska myndigheten för livsmedelssäkerhet (EFSA) omprövade det 2023 och satte <strong>en daglig gräns: ett halvt gram per kilo kroppsvikt</strong> (cirka 35 g för en person som väger 70 kilo). Huvudskälet är att stora mängder ger <strong>diarré.</strong></li>
                <li>En observationsstudie från 2023 fann att personer med <strong>höga nivåer av erytritol i blodet</strong> hade högre risk för hjärtproblem. Men observera: kroppen bildar själv erytritol, och studien bevisar inte att sötningsmedlet är orsaken. Frågan forskas det alltså fortfarande på, och vi råder dig till måttlighet, som med allt annat.</li>
            </ul>
            <h3>💧 Sukralos</h3>
            <p>Tillverkat av socker självt efter en kemisk förändring, och cirka <strong>600 gånger sötare.</strong> <strong>Inga kalorier, och det höjer inte blodsockret</strong>, och det tål värme, så det fungerar i matlagning och bakning. Och ärligt talat? Själv använder jag två droppar av det i kaffet varje dag ☕</p>
            <p><strong>I Europa:</strong> tillåtet, med koden E955.</p>
            <h3>🌲 Xylitol</h3>
            <p>En annan sockeralkohol, med en sötma nära sockrets, <strong>och ett glykemiskt index på cirka 13.</strong> Känd från tuggummi eftersom det inte skadar tänderna. Men även här ger stora mängder diarré.</p>
            <p><strong>Och en mycket viktig upplysning:</strong> xylitol är <strong>giftigt för hundar</strong> 🐶 även en liten mängd kan vara farlig för dem. Har du hund, håll xylitoltuggummit borta från den!</p>
            <h3>🍈 Munkfrukt och allulos</h3>
            <p>Två som du hör mycket om i amerikanska videor. Men <strong>i Europa är deras rättsliga status en annan:</strong></p>
            <ul class="check-list">
                <li><strong>Allulos:</strong> fortfarande <strong>inte tillåtet</strong> i EU. Den europeiska myndigheten (EFSA) sa 2025 att underlaget inte innehöll tillräckligt med säkerhetsstudier.</li>
                <li><strong>Munkfrukt:</strong> dess status i Europa är begränsad och komplicerad, så du hittar den inte lika lätt som stevia.</li>
            </ul>
            <p>Bor du i Europa är alltså stevia, erytritol och sukralos de praktiska alternativen.</p>
            <p><strong>Och för att vara rättvis:</strong> Världshälsoorganisationen sa 2023 att den inte rekommenderar sötningsmedel utan socker som ett sätt att gå ner i vikt, eftersom studier inte har visat någon tydlig nytta på lång sikt. Sötningsmedlen är alltså ett verktyg för att dra ner på sockret, inte ett bantningsrecept. Det verkliga målet är att tungan steg för steg vänjer sig vid mindre sötma 😉</p>

            <h2 class="section-title"><i class="fas fa-jar"></i> <span>"Naturliga alternativ"… som till sist är socker 🍯</span></h2>
            <p>Här måste vi vara ärliga, för många produkter säljs som "nyttiga":</p>
            <table class="sugar-table">
                <thead><tr><th>Alternativ</th><th>Glykemiskt index</th><th>Sanningen</th></tr></thead>
                <tbody>
                    <tr><td>Honung</td><td>cirka 61</td><td>Naturligt socker, ungefär hälften fruktos</td></tr>
                    <tr><td>Kokossocker</td><td>cirka 54</td><td>Socker, med lika många kalorier som vitt socker</td></tr>
                    <tr><td>Dadelsirap</td><td>inte tillgängligt</td><td>Koncentrerat socker från dadlar</td></tr>
                    <tr><td>Vitt socker</td><td>cirka 65</td><td>Som jämförelse</td></tr>
                </tbody>
            </table>
            <p class="food-links"><a class="food-chip" href="{food:coconut-sugar}">Kokossocker</a> <a class="food-chip" href="{food:fenugreek-tea-with-honey}">Bockhornsklöverte med honung</a></p>
            <p><strong>Honung</strong> innehåller några nyttiga ämnen, men kroppen hanterar den som socker. Och på <strong>kokossocker</strong> står det ofta "lågt glykemiskt index", men University of Sydney mätte det till cirka 54, precis på gränsen till lågt, och inte så långt från vitt socker.</p>
            <p>Slutsatsen? <strong>"Naturligt" socker… höjer naturligtvis fortfarande ditt socker</strong> 😄 Det är mängden som gör skillnaden, inte namnet på förpackningen.</p>

            <h2 class="section-title"><i class="fas fa-list-check"></i> <span>Så drar du ner på sockret utan att känna dig snål mot dig själv</span></h2>
            <p>Ingen vill leva utan sötsaker, och det behövs inte heller. Här är praktiska steg du kan börja med i morgon:</p>
            <ol class="steps">
                <li><strong>Börja med dryckerna.</strong> Dricker du läsk eller juice varje dag är det här den största vinsten. Du kan byta ut dem mot kolsyrat vatten med citron, osötat iste eller iskall hibiskus. <a class="food-chip" href="{food:hibiscus-iced-tea}">Hibiskuste, kallt</a></li>
                <li><strong>Ät frukten, drick den inte.</strong> Ett äpple i stället för ett glas äppeljuice.</li>
                <li><strong>Minska skedarna gradvis.</strong> Tar du två skedar i teet, gör det till en och en halv i två veckor, sedan en. Tungan vänjer sig snabbare än du tror.</li>
                <li><strong>Läs etiketten.</strong> Leta efter "varav sockerarter" i näringsvärdestabellen, och efter de dolda namnen vi pratade om. Och har du inte tid att läsa varje förpackning i mataffären, lämna det åt oss 👇</li>
                <li><strong>Använd sötningsmedel smart.</strong> Två droppar stevia eller sukralos i kaffe och te, och erytritol till bakning, men allt med måtta.</li>
                <li><strong>Ät sött efter maten, inte för sig.</strong> Något sött efter en måltid med protein och fibrer är snällare mot blodsockret än på fastande mage. <a class="food-chip" href="{food:appeltaart}">Holländsk äppelpaj (appeltaart)</a></li>
                <li><strong>Välj rätt frukost.</strong> Storgryn med frukt i stället för sötade frukostflingor. <a class="food-chip" href="{food:gluten-free-rolled-oats}">Glutenfria havregryn</a></li>
            </ol>
            <aside class="boodi-card">
                <div>
                    <h2>📱 Skanna streckkoden med boodi-appen</h2>
                    <p>I mataffären berättar varje produkt en historia, men med väldigt liten text 😄 boodi-appen läser den åt dig: du skannar streckkoden, och den visar hur mycket socker och kolhydrater produkten innehåller, sockernivån och det glykemiska indexet, avslöjar ingredienserna och föreslår alternativ med mindre socker från samma hylla.</p>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> Upptäck boodi-appen</a>
            </aside>

            <h2 class="section-title"><i class="fas fa-flag-checkered"></i> <span>Slutsatsen på två rader</span></h2>
            <p><strong>Fruktosen i frukt kommer i en liten mängd, tillsammans med fibrer och vatten, och tarmen hinner med, så den är din vän.</strong> Fruktosen i drycker och tillsatt socker kommer däremot i en stor mängd på en gång, så den svämmar över till levern, och där omvandlas den till fett. <strong>Så var inte rädd för äpplet… var rädd för burken!</strong> 🍎🥤</p>'''),
    ),
)

ARTICLES = [SUGAR_FREE_CEREALS, PREDIABETES, GESTATIONAL_DIABETES, FATTY_LIVER_GUIDE, HYPERTENSION_INSULIN, FRUCTOSE, INSULIN_RESISTANCE_SV,
            LEPTIN_SV, CORTISOL_SV, INTERMITTENT_FASTING_SV, MAGNESIUM_SV, BONE_HEALTH_SV, THYROID_SV]
