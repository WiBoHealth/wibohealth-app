"""Article content for scripts/generate_article_pages.py (AR / EN / NL).

Body HTML may link foods as {food:<slug>} and site pages as {site:/path}; the generator resolves them per language.
GI figures follow the site's own food pages (GI wording bands: <=55 low, 56-69 medium, >=70 high).
"""

SUGAR_FREE_CEREALS = dict(
    slugs=dict(ar='healthy-sugar-free-breakfast-cereals', en='healthy-sugar-free-breakfast-cereals',
               nl='gezonde-ontbijtgranen-zonder-suiker'),
    hero='healthy-sugar-free-breakfast-cereal-hero.webp', hero_size=(1400, 781),
    bowl='healthy-whole-grain-cereal-bowl.webp',
    published='2026-10-17', modified='2026-10-17', minutes=9,
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
        ),
    ),
)

GESTATIONAL_DIABETES = dict(
    section='diabetes',
    slugs=dict(ar='gestational-diabetes', en='gestational-diabetes', nl='zwangerschapsdiabetes'),
    hero='gestational-diabetes-guide-hero.webp', hero_size=(1376, 768),
    published='2026-10-20', modified='2026-10-20', minutes=8,
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
 byline='بقلم وتدقيق سريري: د. وسيم حبيب (Dr. Wassim Habib) – مؤسس WiBo Health',
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
 byline='Written & Clinically Reviewed by: Dr. Wassim Habib – Founder of WiBo Health',
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
 byline='Geschreven en klinisch beoordeeld door: Dr. Wassim Habib – Oprichter van WiBo Health',
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
    ),
)

ARTICLES = [SUGAR_FREE_CEREALS, GESTATIONAL_DIABETES]
