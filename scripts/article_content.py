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
 byline='Dr. Wassim Habib | Grundare och Medicinskt Ansvarig, WiBo Health Group',
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
 byline='Dr. Wassim Habib | Grundare och Medicinskt Ansvarig, WiBo Health Group',
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
 byline='Medicinskt granskad av Dr. Wassim Habib | Grundare och Medicinskt Ansvarig, WiBo Health Group',
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
            <p class="reviewed">Granskad av Dr. Wassim Habib<br>Grundare och medicinskt ansvarig, WiBo Health Group 🌿</p>'''),
    ),
)

# --------------------------------------------------------------------------------------------
# Swedish versions of the older hand-written articles (decision 2026-10-23). Each has only `sv` content here; `legacy`
# names the existing ?lang page (AR/EN/NL) it translates, which becomes its hreflang ar / x-default partner.
# Rules: HbA1c in mmol/mol, glucose in mmol/l; EU 1924/2006 (no cure/reverse/detox wording, authorised claims only);
# signed "Dr. Wassim Habib | Grundare och Medicinskt Ansvarig, WiBo Health Group" (byline and schema, 2026-10-23).
# --------------------------------------------------------------------------------------------
SV_BYLINE = 'Dr. Wassim Habib | Grundare och Medicinskt Ansvarig, WiBo Health Group'
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
                <li><strong>Begränsa livsmedel med högt GI:</strong> vitt bröd, vitt ris, tillsatt socker, juice och friterad potatis, som ger snabba och höga blodsockertoppar.</li>
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

FATTY_LIVER_SV = dict(
    legacy=dict(ar='/fatty-liver.html'),
    slugs=dict(sv='fettlever'),
    hero='fatty-liver-lifestyle.jpeg', hero_size=(1376, 1376), hero_portrait=True,
    published='2026-10-23', modified='2026-10-23',
    named_author=True,
    faq_schema=True,
    references=[
        'European Association for the Study of the Liver (EASL), EASD, EASO. EASL–EASD–EASO Clinical Practice Guidelines on the management of metabolic dysfunction-associated steatotic liver disease (MASLD). J Hepatol 2024;81(3):492–542',
        'Rinella ME, Lazarus JV, Ratziu V, et al. A multisociety Delphi consensus statement on new fatty liver disease nomenclature. J Hepatol 2023;79(6):1542–1556',
        'Vilar-Gomez E, Martinez-Perez Y, Calzadilla-Bertot L, et al. Weight loss through lifestyle modification significantly reduces features of nonalcoholic steatohepatitis. Gastroenterology 2015;149(2):367–378',
        'Schwarz JM, Noworolski SM, Erkin-Cakmak A, et al. Effects of dietary fructose restriction on liver fat, de novo lipogenesis, and insulin kinetics in children with obesity. Gastroenterology 2017;153(3):743–752',
        'Commission Regulation (EU) No 432/2012: authorised health claims (choline and normal liver function)',
    ],
    content=dict(
sv=dict(
 byline=SV_BYLINE,
 title='Fettlever (MASLD): så uppstår den tyst och vad du kan göra för levern | WiBo Health',
 h1='Fettlever (MASLD): så uppstår den tyst och vad du kan göra för levern',
 crumb='Fettlever',
 cat='Diabetes och metabol hälsa',
 desc='Fettlever (MASLD) i klartext: hur fruktos och insulinresistens lagrar fett i levern, stadierna, de dolda tecknen, hur den upptäcks i svensk vård och de levnadsvanor som minskar leverfettet.',
 summary='Hur fettlever uppstår, varför den ofta inte märks, hur den upptäcks och vilka vanor som minskar leverfettet.',
 hero_alt='Kvinna som stretchar på en yogamatta, framför en kopp svart kaffe, bär, avokado och chiafrön – vardagsvanor för levern',
 about=['Fatty liver', 'MASLD', 'Insulin resistance', 'Fructose'],
 disclaimer=SV_DISCLAIMER,
 body='''            <p class="lead">Levern är kroppens kemiska kraftverk med hundratals uppgifter: den bygger proteiner, lagrar energi och tar hand om omsättningen av fett och socker. Ändå har ungefär var fjärde vuxen i världen för mycket fett i levern utan att dricka mycket alkohol, ett tillstånd som i dag kallas <strong>MASLD</strong> (metabolt associerad steatotisk leversjukdom), tidigare NAFLD.</p>
            <p>Det lömska med fettlever är att den oftast inte gör ont: levern saknar smärtnerver, så fettinlagringen kan pågå i många år utan symtom. I den här guiden förklarar vi hur socker, särskilt fruktos, och insulinresistens driver fettinlagringen, och vilka levnadsvanor som enligt forskningen minskar leverfettet.</p>
            <div class="tip"><h3>Viktigt att veta</h3><p>Många med fettlever har helt normala levervärden (ALAT och ASAT). Ett vanligt leverprov räcker därför inte för att utesluta fettlever. I svensk vård används ofta <strong>FIB-4</strong>, ett riskindex som räknas fram från ålder, ALAT, ASAT och trombocyter, och vid behov elastografi (till exempel FibroScan) för att bedöma risken för fibros.</p></div>

            <h2 class="section-title"><i class="fas fa-flask"></i> <span>Fruktos: varför flytande socker belastar levern</span></h2>
            <p>Musklerna, hjärtat och hjärnan använder glukos som bränsle. Fruktos (som finns i glukos-fruktossirap, läsk och juice) tas däremot nästan helt om hand av levern.</p>
            <p>När fruktos kommer i stora mängder, särskilt i flytande form, får levern mer än den hinner använda och omvandlar överskottet till fett, så kallad fettnybildning (de novo-lipogenes).</p>

            <h2 class="section-title"><i class="fas fa-rotate"></i> <span>Insulinresistens och den onda cirkeln</span></h2>
            <p>När fett samlas i leverns celler blir de sämre på att svara på insulin. Normalt bromsar insulinet leverns egen sockerproduktion efter en måltid; vid fettlever fortsätter levern i stället att släppa ut socker i blodet, även när du fastar.</p>
            <p>Det högre blodsockret får bukspottkörteln att frisätta mer insulin, och det höga insulinet driver i sin tur på fettnybildningen i levern. Därför hänger fettlever, insulinresistens och prediabetes ofta ihop.</p>

            <div class="boodi-card">
                <div>
                    <h2>📱 Skydda din lever: granska varor med boodi-appen 💚</h2>
                    <p>Skanna streckkoden för att hitta dolt socker, glukos-fruktossirap och härdade fetter direkt, och se alternativ från samma hylla.</p>
                </div>
                <a class="boodi-btn" href="{site:/boodi.html}"><i class="fas fa-barcode"></i> Upptäck boodi</a>
            </div>

            <h2 class="section-title"><i class="fas fa-layer-group"></i> <span>Fettleverns stadier</span></h2>
            <ul class="check-list">
                <li><strong>1. Enkel fettlever (MASL):</strong> fett utgör mer än 5 % av leverns vikt, utan inflammation. Det här stadiet kan gå tillbaka med viktnedgång och ändrade levnadsvanor.</li>
                <li><strong>2. Fettleverinflammation (MASH):</strong> fettet orsakar inflammation och cellskador. Viktnedgång kan minska inflammationen; följs upp av läkare.</li>
                <li><strong>3. Fibros och cirros:</strong> leverväv ersätts av ärrvävnad. Kräver utredning och uppföljning hos specialist.</li>
            </ul>
            <figure class="article-figure">
                <img src="/images/fatty-liver-chart.jpeg" alt="Jämförelse mellan en frisk lever och en fettlever" width="2816" height="1536" loading="lazy" decoding="async">
                <figcaption>En frisk lever jämfört med en fettlever (bildtexter på engelska).</figcaption>
            </figure>

            <h2 class="section-title"><i class="fas fa-user-secret"></i> <span>Dolda varningstecken</span></h2>
            <p>Fettlever ger oftast inga symtom, men kroppen kan visa vissa tecken:</p>
            <ul class="check-list">
                <li><strong>Trötthet och ”hjärndimma”:</strong> särskilt efter måltider.</li>
                <li><strong>Tyngdkänsla under höger revbensbåge:</strong> en molande känsla när levern blir större.</li>
                <li><strong>Ökat midjemått:</strong> bukfettet speglar ofta hur mycket fett som finns i levern.</li>
                <li><strong>Blodfetter:</strong> höga triglycerider och lågt HDL-kolesterol är vanliga vid fettlever.</li>
            </ul>
            <p>Känner du igen dig, eller har du typ 2-diabetes eller bukfetma? Prata med din vårdcentral om en bedömning av levern.</p>

            <h2 class="section-title"><i class="fas fa-route"></i> <span>Levnadsvanor som minskar leverfettet</span></h2>
            <p>Levercellerna har en god förmåga att återhämta sig. När belastningen minskar börjar fettet i levern minska redan inom några veckor:</p>

            <h3>1. Ta bort söta drycker och tillsatt socker</h3>
            <p>Grunden är att sluta med läsk, juice, söta bakverk och vitt mjöl. En studie visade att leverns fettnybildning och leverfettet minskade redan efter nio dagar när tillsatt fruktos byttes mot stärkelse.</p>

            <h3>2. Ge levern en paus på natten</h3>
            <p>En nattfasta på 12–14 timmar mellan kvällsmat och frukost sänker insulinnivån och ger levern tid att använda sitt lagrade fett. Har du diabetes och tar blodsockersänkande läkemedel, eller är du gravid, prata med din läkare innan du ändrar måltidsrytmen.</p>

            <h3>3. Kaffe kan ingå</h3>
            <p>Svart kaffe utan socker passar bra i en leverfrämjande vardag. Observationsstudier har sett ett samband mellan måttligt kaffedrickande och lägre risk för leverfibros, och EASL:s riktlinjer nämner detta, men ett samband är inte samma sak som ett bevis, och kaffe ersätter inte ändrade levnadsvanor.</p>

            <h3>4. Kolin från ägg och fisk</h3>
            <p>Kolin behövs för att levern ska kunna ”paketera” fett och skicka ut det i blodet. <strong>Kolin bidrar till att upprätthålla normal leverfunktion</strong> (EU-godkänt påstående). Bra källor är ägg och fisk.</p>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>Vanliga frågor</span></h2>
            <div class="faq-list">
                <div class="faq-item"><h3>Måste jag sluta äta frukt om jag har fettlever?</h3><p>Nej. Hel frukt innehåller fiber som gör att fruktosen tas upp långsamt. Välj gärna bär och äpplen, ät frukten hel och undvik juice och smoothies.</p></div>
                <div class="faq-item"><h3>Hur lång tid tar det att minska leverfettet?</h3><p>Vid tidig fettlever minskar en viktnedgång på 7–10 % leverfettet påtagligt och kan normalisera levervärdena inom några månader. Vid en viktnedgång på minst 10 % har studier också sett att inflammation och fibros kan minska. Din läkare följer upp med prover.</p></div>
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
                <li><strong>Selen</strong> bidrar till normal sköldkörtelfunktion. Selen finns i fisk, skaldjur, ägg, kött och mejeriprodukter. Paranötter innehåller mycket och mycket varierande mängder selen; ät dem bara då och då och kombinera dem inte med selentillskott, eftersom för mycket selen är skadligt (EFSA:s övre gräns är 255 mikrogram per dag för vuxna).</li>
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

ARTICLES = [SUGAR_FREE_CEREALS, PREDIABETES, GESTATIONAL_DIABETES, INSULIN_RESISTANCE_SV, FATTY_LIVER_SV,
            LEPTIN_SV, CORTISOL_SV, INTERMITTENT_FASTING_SV, MAGNESIUM_SV, BONE_HEALTH_SV, THYROID_SV]
