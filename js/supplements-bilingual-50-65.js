// Supplements 50-65 - New batch from user
const supplements_50_65 = [
    {
        id: 50,
        name: "هيوبرزين إيه",
        nameEn: "Huperzine A",
        category: "نوم-نفسية",
        categoryEn: "sleep-mental",
        icon: "🌿",
        summary: "مستخلص من نبات صيني - يحسن الذاكرة والتركيز بشكل قوي",
        summaryEn: "Chinese plant extract - powerfully improves memory and focus",
        tags: ["ذاكرة", "تركيز", "نيوتروبيك"],
        tagsEn: ["memory", "focus", "nootropic"],
        benefits: [
            "يثبط إنزيم يكسر الأسيتيل كولين (يزيد الذاكرة)",
            "يحسن الذاكرة والتعلم بشكل ملحوظ",
            "يزيد التركيز واليقظة",
            "يحمي خلايا الدماغ من التلف",
            "مفيد لمرض الزهايمر",
            "تأثير يدوم 6-8 ساعات"
        ],
        benefitsEn: [
            "Inhibits enzyme that breaks down acetylcholine (increases memory)",
            "Significantly improves memory and learning",
            "Increases focus and alertness",
            "Protects brain cells from damage",
            "Beneficial for Alzheimer's disease",
            "Effect lasts 6-8 hours"
        ],
        dosage: {
            recommended: "50-200 ميكروجرام",
            timing: "في الصباح أو قبل المذاكرة",
            frequency: "مرة واحدة يومياً (أو يوم ويوم)"
        },
        dosageEn: {
            recommended: "50-200 mcg",
            timing: "In the morning or before studying",
            frequency: "Once daily (or every other day)"
        },
        warnings: [
            "خذه بحذر - تأثير قوي",
            "لا تستخدمه يومياً - خذ استراحة (2 أيام أون، 1 يوم أوف)",
            "قد يسبب غثيان أو صداع",
            "تجنبه إذا كنت تتناول أدوية للذاكرة"
        ],
        warningsEn: [
            "Use with caution - strong effect",
            "Don't use daily - take breaks (2 days on, 1 day off)",
            "May cause nausea or headache",
            "Avoid if taking memory medications"
        ],
        interactions: "يتفاعل مع أدوية الزهايمر - استشر طبيبك",
        interactionsEn: "Interacts with Alzheimer's medications - consult your doctor",
        naturalSources: "نبات Huperzia serrata الصيني",
        naturalSourcesEn: "Chinese Huperzia serrata plant"
    },
    {
        id: 51,
        name: "حليب الشوك",
        nameEn: "Milk Thistle (Silymarin)",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "🌿",
        summary: "عشبة قوية لحماية وتجديد الكبد - الأفضل لصحة الكبد",
        summaryEn: "Powerful herb for liver protection and regeneration - best for liver health",
        tags: ["كبد", "تطهير", "حماية"],
        tagsEn: ["liver", "cleanse", "protection"],
        benefits: [
            "يحمي الكبد من السموم والأدوية",
            "يساعد في تجديد خلايا الكبد",
            "يحسن وظائف الكبد",
            "مضاد أكسدة قوي",
            "يدعم الهضم والمرارة",
            "مفيد لمن يتناول أدوية أو مكملات كثيرة"
        ],
        benefitsEn: [
            "Protects liver from toxins and medications",
            "Helps regenerate liver cells",
            "Improves liver function",
            "Powerful antioxidant",
            "Supports digestion and gallbladder",
            "Beneficial for those taking many medications or supplements"
        ],
        dosage: {
            recommended: "150-300 ملغ سيليمارين",
            timing: "مع وجبة",
            frequency: "2-3 مرات يومياً"
        },
        dosageEn: {
            recommended: "150-300 mg silymarin",
            timing: "With meal",
            frequency: "2-3 times daily"
        },
        warnings: [
            "النتائج تحتاج 4-8 أسابيع",
            "آمن جداً للاستخدام طويل المدى",
            "قد يسبب إسهال خفيف"
        ],
        warningsEn: [
            "Results take 4-8 weeks",
            "Very safe for long-term use",
            "May cause mild diarrhea"
        ],
        interactions: "قد يتفاعل مع بعض الأدوية - استشر طبيبك",
        interactionsEn: "May interact with some medications - consult your doctor",
        naturalSources: "نبات حليب الشوك (يُستخدم كمكمل)",
        naturalSourcesEn: "Milk thistle plant (used as supplement)"
    },
    {
        id: 52,
        name: "حلبة",
        nameEn: "Fenugreek",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "🌾",
        summary: "بذور عشبية تقليدية - قد تزيد التستوستيرون وتحسن سكر الدم",
        summaryEn: "Traditional herbal seeds - may increase testosterone and improve blood sugar",
        tags: ["تستوستيرون", "سكر دم", "رضاعة"],
        tagsEn: ["testosterone", "blood sugar", "lactation"],
        benefits: [
            "قد تزيد مستوى التستوستيرون لدى الرجال",
            "تحسن حساسية الأنسولين وسكر الدم",
            "تزيد إنتاج الحليب لدى المرضعات",
            "تحسن الرغبة الجنسية",
            "تخفض الكوليسترول",
            "لها خصائص مضادة للالتهاب"
        ],
        benefitsEn: [
            "May increase testosterone levels in men",
            "Improves insulin sensitivity and blood sugar",
            "Increases milk production in nursing mothers",
            "Improves libido",
            "Lowers cholesterol",
            "Has anti-inflammatory properties"
        ],
        dosage: {
            recommended: "500-600 ملغ",
            timing: "مع وجبة",
            frequency: "1-2 مرات يومياً"
        },
        dosageEn: {
            recommended: "500-600 mg",
            timing: "With meal",
            frequency: "1-2 times daily"
        },
        warnings: [
            "النتائج تحتاج 6-12 أسبوع",
            "قد تجعل رائحة الجسم والبول مثل القيقب",
            "تجنبها إذا كنت حاملاً"
        ],
        warningsEn: [
            "Results take 6-12 weeks",
            "May make body and urine smell like maple syrup",
            "Avoid if pregnant"
        ],
        interactions: "قد تتفاعل مع أدوية السكري - استشر طبيبك",
        interactionsEn: "May interact with diabetes medications - consult your doctor",
        naturalSources: "بذور الحلبة الطازجة أو المطحونة",
        naturalSourcesEn: "Fresh or ground fenugreek seeds"
    },
    {
        id: 53,
        name: "تريبولوس",
        nameEn: "Tribulus Terrestris",
        category: "بناء-عضلات",
        categoryEn: "muscle-building",
        icon: "🌿",
        summary: "عشبة تقليدية قد تدعم مستويات التستوستيرون والرغبة الجنسية",
        summaryEn: "Traditional herb may support testosterone levels and libido",
        tags: ["تستوستيرون", "رغبة جنسية", "رياضة"],
        tagsEn: ["testosterone", "libido", "sports"],
        benefits: [
            "قد يدعم مستويات التستوستيرون الطبيعية",
            "يحسن الرغبة الجنسية لدى الرجال والنساء",
            "قد يحسن الأداء الرياضي",
            "يدعم صحة القلب والأوعية الدموية",
            "له خصائص مضادة للالتهاب"
        ],
        benefitsEn: [
            "May support natural testosterone levels",
            "Improves libido in men and women",
            "May improve athletic performance",
            "Supports cardiovascular health",
            "Has anti-inflammatory properties"
        ],
        dosage: {
            recommended: "500-1500 ملغ",
            timing: "مع وجبة",
            frequency: "1-3 مرات يومياً"
        },
        dosageEn: {
            recommended: "500-1500 mg",
            timing: "With meal",
            frequency: "1-3 times daily"
        },
        warnings: [
            "النتائج متضاربة في الأبحاث",
            "أكثر فعالية لمن لديهم تستوستيرون منخفض",
            "قد يسبب اضطراب معدة"
        ],
        warningsEn: [
            "Research results are mixed",
            "More effective for those with low testosterone",
            "May cause stomach upset"
        ],
        interactions: "قد يتفاعل مع أدوية السكري والضغط - استشر طبيبك",
        interactionsEn: "May interact with diabetes and blood pressure medications - consult your doctor",
        naturalSources: "نبات التريبولوس (يُستخدم كمكمل)",
        naturalSourcesEn: "Tribulus plant (used as supplement)"
    },
    {
        id: 54,
        name: "سو بالميتو",
        nameEn: "Saw Palmetto",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "🌴",
        summary: "نبات لصحة البروستاتا - يقلل أعراض تضخم البروستاتا الحميد",
        summaryEn: "Plant for prostate health - reduces benign prostatic hyperplasia symptoms",
        tags: ["بروستاتا", "رجال", "هرمونات"],
        tagsEn: ["prostate", "men", "hormones"],
        benefits: [
            "يحسن أعراض تضخم البروستاتا الحميد (BPH)",
            "يقلل الحاجة للتبول الليلي",
            "قد يمنع تساقط الشعر الهرموني",
            "يدعم صحة المسالك البولية",
            "يثبط تحويل التستوستيرون إلى DHT"
        ],
        benefitsEn: [
            "Improves benign prostatic hyperplasia (BPH) symptoms",
            "Reduces nighttime urination",
            "May prevent hormonal hair loss",
            "Supports urinary tract health",
            "Inhibits conversion of testosterone to DHT"
        ],
        dosage: {
            recommended: "320 ملغ",
            timing: "مع وجبة",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "320 mg",
            timing: "With meal",
            frequency: "Once daily"
        },
        warnings: [
            "النتائج تحتاج 4-6 أسابيع",
            "قد يسبب اضطراب معدة خفيف",
            "استشر طبيبك قبل الاستخدام"
        ],
        warningsEn: [
            "Results take 4-6 weeks",
            "May cause mild stomach upset",
            "Consult your doctor before use"
        ],
        interactions: "قد يتفاعل مع أدوية هرمونية - استشر طبيبك",
        interactionsEn: "May interact with hormonal medications - consult your doctor",
        naturalSources: "ثمار نخيل سو بالميتو",
        naturalSourcesEn: "Saw palmetto palm berries"
    },
    {
        id: 55,
        name: "جذر الماكا",
        nameEn: "Maca Root",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "🥔",
        summary: "جذر بيروفي تقليدي - يزيد الطاقة والرغبة الجنسية والخصوبة",
        summaryEn: "Traditional Peruvian root - increases energy, libido, and fertility",
        tags: ["طاقة", "رغبة جنسية", "خصوبة"],
        tagsEn: ["energy", "libido", "fertility"],
        benefits: [
            "يزيد مستويات الطاقة والتحمل",
            "يحسن الرغبة الجنسية لدى الرجال والنساء",
            "قد يحسن خصوبة الرجال (عدد وحركة الحيوانات المنوية)",
            "يحسن المزاج ويقلل القلق",
            "يوازن الهرمونات",
            "آمن وطبيعي 100%"
        ],
        benefitsEn: [
            "Increases energy levels and endurance",
            "Improves libido in men and women",
            "May improve male fertility (sperm count and motility)",
            "Improves mood and reduces anxiety",
            "Balances hormones",
            "100% safe and natural"
        ],
        dosage: {
            recommended: "1500-3000 ملغ",
            timing: "مع وجبة الإفطار",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "1500-3000 mg",
            timing: "With breakfast",
            frequency: "Once daily"
        },
        warnings: [
            "النتائج تحتاج 6-12 أسبوع",
            "قد يسبب أرق إذا أخذ مساءً",
            "آمن للاستخدام طويل المدى"
        ],
        warningsEn: [
            "Results take 6-12 weeks",
            "May cause insomnia if taken in evening",
            "Safe for long-term use"
        ],
        interactions: "آمن مع معظم الأدوية",
        interactionsEn: "Safe with most medications",
        naturalSources: "جذر الماكا الطازج أو المجفف",
        naturalSourcesEn: "Fresh or dried maca root"
    },
    {
        id: 56,
        name: "فيتامين إي",
        nameEn: "Vitamin E (Tocopherols)",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "🌻",
        summary: "مضاد أكسدة قوي يحمي الخلايا ويدعم صحة البشرة والمناعة",
        summaryEn: "Powerful antioxidant that protects cells and supports skin health and immunity",
        tags: ["مضاد أكسدة", "بشرة", "مناعة"],
        tagsEn: ["antioxidant", "skin", "immunity"],
        benefits: [
            "مضاد أكسدة قوي يحمي الخلايا من التلف",
            "يحسن صحة البشرة ويقلل التجاعيد",
            "يدعم جهاز المناعة",
            "يحمي من أمراض القلب",
            "يحسن صحة العين",
            "قد يقلل خطر السرطان"
        ],
        benefitsEn: [
            "Powerful antioxidant protects cells from damage",
            "Improves skin health and reduces wrinkles",
            "Supports immune system",
            "Protects against heart disease",
            "Improves eye health",
            "May reduce cancer risk"
        ],
        dosage: {
            recommended: "15-400 وحدة دولية",
            timing: "مع وجبة تحتوي على دهون",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "15-400 IU",
            timing: "With meal containing fats",
            frequency: "Once daily"
        },
        warnings: [
            "لا تتجاوز 1000 وحدة يومياً",
            "الجرعات العالية جداً قد تزيد خطر النزيف",
            "اختر الشكل الطبيعي (d-alpha-tocopherol)"
        ],
        warningsEn: [
            "Do not exceed 1000 IU daily",
            "Very high doses may increase bleeding risk",
            "Choose natural form (d-alpha-tocopherol)"
        ],
        interactions: "قد يتفاعل مع مميعات الدم - استشر طبيبك",
        interactionsEn: "May interact with blood thinners - consult your doctor",
        naturalSources: "المكسرات، البذور، السبانخ، البروكلي، الأفوكادو",
        naturalSourcesEn: "Nuts, seeds, spinach, broccoli, avocado"
    },
    {
        id: 57,
        name: "فيتامين كي 2",
        nameEn: "Vitamin K2 (Menaquinone)",
        category: "عظام-مفاصل",
        categoryEn: "bones-joints",
        icon: "🦴",
        summary: "فيتامين أساسي لصحة العظام والقلب - يوجه الكالسيوم للعظام وليس الشرايين",
        summaryEn: "Essential vitamin for bone and heart health - directs calcium to bones not arteries",
        tags: ["عظام", "قلب", "كالسيوم"],
        tagsEn: ["bones", "heart", "calcium"],
        benefits: [
            "يوجه الكالسيوم إلى العظام (يقويها)",
            "يمنع ترسب الكالسيوم في الشرايين (يحمي القلب)",
            "يحسن كثافة العظام ويمنع هشاشتها",
            "يدعم صحة الأسنان",
            "يعمل بشكل ممتاز مع فيتامين د3",
            "مهم جداً وغالباً ناقص"
        ],
        benefitsEn: [
            "Directs calcium to bones (strengthens them)",
            "Prevents calcium deposits in arteries (protects heart)",
            "Improves bone density and prevents osteoporosis",
            "Supports dental health",
            "Works excellently with vitamin D3",
            "Very important and often deficient"
        ],
        dosage: {
            recommended: "100-200 ميكروجرام MK-7",
            timing: "مع فيتامين د3 ووجبة دهنية",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "100-200 mcg MK-7",
            timing: "With vitamin D3 and fatty meal",
            frequency: "Once daily"
        },
        warnings: [
            "خذه مع فيتامين د3 للحصول على أفضل نتيجة",
            "اختر الشكل MK-7 (أفضل من MK-4)",
            "آمن للاستخدام طويل المدى"
        ],
        warningsEn: [
            "Take with vitamin D3 for best results",
            "Choose MK-7 form (better than MK-4)",
            "Safe for long-term use"
        ],
        interactions: "يتفاعل مع مميعات الدم (Warfarin) - لا تجمعهم",
        interactionsEn: "Interacts with blood thinners (Warfarin) - don't combine",
        naturalSources: "الناتو (فول صويا مخمر)، الجبن، صفار البيض، الكبد",
        naturalSourcesEn: "Natto (fermented soybeans), cheese, egg yolks, liver"
    },
    {
        id: 58,
        name: "سيلينيوم",
        nameEn: "Selenium",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "🔬",
        summary: "معدن نادر أساسي لجهاز المناعة والغدة الدرقية ومضاد أكسدة قوي",
        summaryEn: "Trace mineral essential for immune system, thyroid, and powerful antioxidant",
        tags: ["مناعة", "غدة درقية", "مضاد أكسدة"],
        tagsEn: ["immunity", "thyroid", "antioxidant"],
        benefits: [
            "يقوي جهاز المناعة بقوة",
            "ضروري لوظيفة الغدة الدرقية",
            "مضاد أكسدة قوي (جزء من إنزيمات مهمة)",
            "يقلل خطر السرطان",
            "يحسن خصوبة الرجال",
            "يدعم صحة القلب"
        ],
        benefitsEn: [
            "Powerfully strengthens immune system",
            "Essential for thyroid function",
            "Powerful antioxidant (part of important enzymes)",
            "Reduces cancer risk",
            "Improves male fertility",
            "Supports heart health"
        ],
        dosage: {
            recommended: "55-200 ميكروجرام",
            timing: "مع وجبة",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "55-200 mcg",
            timing: "With meal",
            frequency: "Once daily"
        },
        warnings: [
            "لا تتجاوز 400 ميكروجرام يومياً",
            "الجرعات العالية سامة جداً",
            "قد تسبب رائحة ثوم في النفس"
        ],
        warningsEn: [
            "Do not exceed 400 mcg daily",
            "High doses are very toxic",
            "May cause garlic breath"
        ],
        interactions: "قد يتفاعل مع فيتامين سي - خذهم في أوقات منفصلة",
        interactionsEn: "May interact with vitamin C - take at separate times",
        naturalSources: "الجوز البرازيلي (غني جداً!)، الأسماك، اللحوم، البيض",
        naturalSourcesEn: "Brazil nuts (very rich!), fish, meats, eggs"
    },
    {
        id: 59,
        name: "كروميوم",
        nameEn: "Chromium (Picolinate)",
        category: "تخسيس",
        categoryEn: "weight-loss",
        icon: "🔬",
        summary: "معدن نادر يحسن حساسية الأنسولين ويقلل الرغبة في السكر والكربوهيدرات",
        summaryEn: "Trace mineral improves insulin sensitivity and reduces sugar and carb cravings",
        tags: ["أنسولين", "سكر دم", "شهية"],
        tagsEn: ["insulin", "blood sugar", "appetite"],
        benefits: [
            "يحسن حساسية الأنسولين",
            "يساعد في تنظيم سكر الدم",
            "يقلل الرغبة الشديدة في السكر والكربوهيدرات",
            "قد يساعد في إنقاص الوزن",
            "مفيد لمرضى السكري من النوع 2",
            "يحسن الأيض"
        ],
        benefitsEn: [
            "Improves insulin sensitivity",
            "Helps regulate blood sugar",
            "Reduces cravings for sugar and carbs",
            "May help with weight loss",
            "Beneficial for type 2 diabetes",
            "Improves metabolism"
        ],
        dosage: {
            recommended: "200-400 ميكروجرام",
            timing: "مع وجبة",
            frequency: "1-2 مرات يومياً"
        },
        dosageEn: {
            recommended: "200-400 mcg",
            timing: "With meal",
            frequency: "1-2 times daily"
        },
        warnings: [
            "النتائج تحتاج 2-4 أشهر",
            "لا تتجاوز 1000 ميكروجرام يومياً",
            "استشر طبيبك إذا كنت تتناول أدوية السكري"
        ],
        warningsEn: [
            "Results take 2-4 months",
            "Do not exceed 1000 mcg daily",
            "Consult doctor if taking diabetes medications"
        ],
        interactions: "يتفاعل مع أدوية السكري - استشر طبيبك",
        interactionsEn: "Interacts with diabetes medications - consult your doctor",
        naturalSources: "البروكلي، البطاطس، اللحوم، الحبوب الكاملة (بكميات قليلة)",
        naturalSourcesEn: "Broccoli, potatoes, meats, whole grains (in small amounts)"
    },
    {
        id: 60,
        name: "يود",
        nameEn: "Iodine",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "🧂",
        summary: "معدن أساسي للغدة الدرقية - نقصه شائع ويسبب التعب وزيادة الوزن",
        summaryEn: "Essential mineral for thyroid - deficiency is common and causes fatigue and weight gain",
        tags: ["غدة درقية", "أيض", "طاقة"],
        tagsEn: ["thyroid", "metabolism", "energy"],
        benefits: [
            "ضروري لإنتاج هرمونات الغدة الدرقية",
            "ينظم عملية الأيض والطاقة",
            "يدعم النمو والتطور",
            "مهم للحمل والرضاعة",
            "يدعم صحة الدماغ والتركيز",
            "نقصه شائع جداً"
        ],
        benefitsEn: [
            "Essential for thyroid hormone production",
            "Regulates metabolism and energy",
            "Supports growth and development",
            "Important for pregnancy and lactation",
            "Supports brain health and focus",
            "Deficiency is very common"
        ],
        dosage: {
            recommended: "150-300 ميكروجرام",
            timing: "مع وجبة الإفطار",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "150-300 mcg",
            timing: "With breakfast",
            frequency: "Once daily"
        },
        warnings: [
            "لا تتجاوز 1100 ميكروجرام يومياً",
            "الجرعات العالية قد تضر الغدة الدرقية",
            "استشر طبيبك إذا كان لديك مشاكل في الغدة"
        ],
        warningsEn: [
            "Do not exceed 1100 mcg daily",
            "High doses may harm thyroid",
            "Consult doctor if you have thyroid problems"
        ],
        interactions: "يتفاعل مع أدوية الغدة الدرقية - استشر طبيبك",
        interactionsEn: "Interacts with thyroid medications - consult your doctor",
        naturalSources: "الملح المدعم باليود، الأعشاب البحرية، الأسماك، البيض",
        naturalSourcesEn: "Iodized salt, seaweed, fish, eggs"
    },
    {
        id: 61,
        name: "NAC",
        nameEn: "N-Acetyl Cysteine",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "💊",
        summary: "حمض أميني قوي - يزيد الجلوتاثيون ويطهر الكبد والرئتين",
        summaryEn: "Powerful amino acid - increases glutathione and cleanses liver and lungs",
        tags: ["جلوتاثيون", "كبد", "رئتين"],
        tagsEn: ["glutathione", "liver", "lungs"],
        benefits: [
            "يزيد إنتاج الجلوتاثيون (أقوى مضاد أكسدة في الجسم)",
            "يطهر الكبد من السموم",
            "يحسن صحة الرئتين ويذيب المخاط",
            "يدعم جهاز المناعة",
            "يقلل الالتهابات",
            "مفيد للوسواس القهري والإدمان"
        ],
        benefitsEn: [
            "Increases glutathione production (body's most powerful antioxidant)",
            "Cleanses liver from toxins",
            "Improves lung health and dissolves mucus",
            "Supports immune system",
            "Reduces inflammation",
            "Beneficial for OCD and addiction"
        ],
        dosage: {
            recommended: "600-1800 ملغ",
            timing: "على معدة فارغة",
            frequency: "1-2 مرات يومياً"
        },
        dosageEn: {
            recommended: "600-1800 mg",
            timing: "On empty stomach",
            frequency: "1-2 times daily"
        },
        warnings: [
            "قد يسبب رائحة كبريت",
            "قد يسبب غثيان على معدة فارغة",
            "آمن للاستخدام طويل المدى"
        ],
        warningsEn: [
            "May cause sulfur smell",
            "May cause nausea on empty stomach",
            "Safe for long-term use"
        ],
        interactions: "قد يتفاعل مع النيتروجليسرين - استشر طبيبك",
        interactionsEn: "May interact with nitroglycerin - consult your doctor",
        naturalSources: "البروتين (الدجاج، البيض، الثوم، البصل)",
        naturalSourcesEn: "Protein (chicken, eggs, garlic, onions)"
    },
    {
        id: 62,
        name: "MSM",
        nameEn: "Methylsulfonylmethane",
        category: "عظام-مفاصل",
        categoryEn: "bones-joints",
        icon: "💎",
        summary: "مركب كبريت عضوي - يقلل آلام المفاصل والالتهابات ويحسن البشرة",
        summaryEn: "Organic sulfur compound - reduces joint pain, inflammation and improves skin",
        tags: ["كبريت", "مفاصل", "التهاب"],
        tagsEn: ["sulfur", "joints", "inflammation"],
        benefits: [
            "يقلل آلام المفاصل والتهابها",
            "يحسن مرونة المفاصل",
            "يدعم صحة البشرة والشعر والأظافر",
            "له خصائص مضادة للالتهاب",
            "يسرع التعافي بعد التمرين",
            "يقلل أعراض الحساسية"
        ],
        benefitsEn: [
            "Reduces joint pain and inflammation",
            "Improves joint flexibility",
            "Supports skin, hair, and nail health",
            "Has anti-inflammatory properties",
            "Speeds recovery after exercise",
            "Reduces allergy symptoms"
        ],
        dosage: {
            recommended: "1500-3000 ملغ",
            timing: "مع وجبة",
            frequency: "2-3 مرات يومياً"
        },
        dosageEn: {
            recommended: "1500-3000 mg",
            timing: "With meal",
            frequency: "2-3 times daily"
        },
        warnings: [
            "النتائج تحتاج 2-4 أسابيع",
            "قد يسبب اضطراب معدة خفيف",
            "آمن للاستخدام طويل المدى"
        ],
        warningsEn: [
            "Results take 2-4 weeks",
            "May cause mild stomach upset",
            "Safe for long-term use"
        ],
        interactions: "آمن مع معظم الأدوية",
        interactionsEn: "Safe with most medications",
        naturalSources: "الفواكه، الخضروات، الحليب (بكميات قليلة جداً)",
        naturalSourcesEn: "Fruits, vegetables, milk (in very small amounts)"
    },
    {
        id: 63,
        name: "كيرسيتين",
        nameEn: "Quercetin",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "🍎",
        summary: "فلافونويد قوي - مضاد التهاب ومضاد حساسية ومضاد فيروسات",
        summaryEn: "Powerful flavonoid - anti-inflammatory, anti-allergy, and antiviral",
        tags: ["مضاد التهاب", "حساسية", "مناعة"],
        tagsEn: ["anti-inflammatory", "allergy", "immunity"],
        benefits: [
            "مضاد التهاب طبيعي قوي",
            "يقلل أعراض الحساسية بشكل ملحوظ",
            "مضاد أكسدة قوي",
            "له خصائص مضادة للفيروسات",
            "يدعم صحة القلب",
            "قد يحسن الأداء الرياضي"
        ],
        benefitsEn: [
            "Powerful natural anti-inflammatory",
            "Significantly reduces allergy symptoms",
            "Powerful antioxidant",
            "Has antiviral properties",
            "Supports heart health",
            "May improve athletic performance"
        ],
        dosage: {
            recommended: "500-1000 ملغ",
            timing: "مع وجبة",
            frequency: "1-2 مرات يومياً"
        },
        dosageEn: {
            recommended: "500-1000 mg",
            timing: "With meal",
            frequency: "1-2 times daily"
        },
        warnings: [
            "خذه مع فيتامين سي لامتصاص أفضل",
            "قد يسبب صداع خفيف",
            "آمن للاستخدام طويل المدى"
        ],
        warningsEn: [
            "Take with vitamin C for better absorption",
            "May cause mild headache",
            "Safe for long-term use"
        ],
        interactions: "قد يتفاعل مع بعض المضادات الحيوية - استشر طبيبك",
        interactionsEn: "May interact with some antibiotics - consult your doctor",
        naturalSources: "التفاح، البصل، التوت، الشاي الأخضر، العنب الأحمر",
        naturalSourcesEn: "Apples, onions, berries, green tea, red grapes"
    },
    {
        id: 64,
        name: "ريسفيراترول",
        nameEn: "Resveratrol",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "🍇",
        summary: "بوليفينول من العنب الأحمر - مضاد شيخوخة ويحسن صحة القلب",
        summaryEn: "Polyphenol from red grapes - anti-aging and improves heart health",
        tags: ["مضاد شيخوخة", "قلب", "طول عمر"],
        tagsEn: ["anti-aging", "heart", "longevity"],
        benefits: [
            "مضاد شيخوخة قوي (يفعل جينات طول العمر)",
            "يدعم صحة القلب والأوعية الدموية",
            "مضاد أكسدة ومضاد التهاب قوي",
            "قد يحسن حساسية الأنسولين",
            "يحمي الدماغ من التدهور",
            "قد يزيد التحمل الرياضي"
        ],
        benefitsEn: [
            "Powerful anti-aging (activates longevity genes)",
            "Supports cardiovascular health",
            "Powerful antioxidant and anti-inflammatory",
            "May improve insulin sensitivity",
            "Protects brain from decline",
            "May increase athletic endurance"
        ],
        dosage: {
            recommended: "150-500 ملغ",
            timing: "مع وجبة دهنية",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "150-500 mg",
            timing: "With fatty meal",
            frequency: "Once daily"
        },
        warnings: [
            "النتائج طويلة المدى (شهور إلى سنوات)",
            "قد يسبب اضطراب معدة",
            "استشر طبيبك إذا كنت تتناول مميعات الدم"
        ],
        warningsEn: [
            "Long-term results (months to years)",
            "May cause stomach upset",
            "Consult doctor if taking blood thinners"
        ],
        interactions: "قد يتفاعل مع مميعات الدم - استشر طبيبك",
        interactionsEn: "May interact with blood thinners - consult your doctor",
        naturalSources: "العنب الأحمر، النبيذ الأحمر، التوت، الفول السوداني",
        naturalSourcesEn: "Red grapes, red wine, berries, peanuts"
    },
    {
        id: 65,
        name: "بربرين",
        nameEn: "Berberine",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "🟡",
        summary: "قلويد نباتي قوي - يخفض سكر الدم كالميتفورمين ويحسن الأيض",
        summaryEn: "Powerful plant alkaloid - lowers blood sugar like metformin and improves metabolism",
        tags: ["سكر دم", "أيض", "قلب"],
        tagsEn: ["blood sugar", "metabolism", "heart"],
        benefits: [
            "يخفض سكر الدم بقوة (مثل الميتفورمين)",
            "يحسن حساسية الأنسولين",
            "يخفض الكوليسترول والدهون الثلاثية",
            "يساعد في إنقاص الوزن",
            "يدعم صحة الأمعاء",
            "له خصائص مضادة للالتهاب"
        ],
        benefitsEn: [
            "Powerfully lowers blood sugar (like metformin)",
            "Improves insulin sensitivity",
            "Lowers cholesterol and triglycerides",
            "Helps with weight loss",
            "Supports gut health",
            "Has anti-inflammatory properties"
        ],
        dosage: {
            recommended: "500 ملغ",
            timing: "قبل الوجبات بـ 30 دقيقة",
            frequency: "3 مرات يومياً (1500 ملغ total)"
        },
        dosageEn: {
            recommended: "500 mg",
            timing: "30 minutes before meals",
            frequency: "3 times daily (1500 mg total)"
        },
        warnings: [
            "قد يسبب اضطراب معدة وإسهال",
            "ابدأ بجرعة منخفضة",
            "استشر طبيبك إذا كنت تتناول أدوية السكري"
        ],
        warningsEn: [
            "May cause stomach upset and diarrhea",
            "Start with low dose",
            "Consult doctor if taking diabetes medications"
        ],
        interactions: "يتفاعل بقوة مع أدوية السكري - استشر طبيبك",
        interactionsEn: "Strongly interacts with diabetes medications - consult your doctor",
        naturalSources: "نبات البرباريس، الكركم البري، الخيط الذهبي",
        naturalSourcesEn: "Barberry plant, wild turmeric, goldthread"
    }
];

// Export for use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = supplements_50_65;
}
