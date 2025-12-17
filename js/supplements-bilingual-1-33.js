/**
 * ============================================================
 * WiBo Health - Bilingual Supplements Database (33 Supplements)
 * قاعدة بيانات المكملات الغذائية ثنائية اللغة (33 مكمل)
 * ============================================================
 * 
 * Version: 3.0 - Extended Build
 * Date: 2025-11-30
 * 
 * Contents:
 * - Supplements 1-16: Translated by AI Assistant
 * - Supplements 17-33: Translated by Helper Chat
 * 
 * Total: 33 Fully Bilingual Supplements
 * ============================================================
 */

const supplementsDataBilingual = [
    // ============================================
    // MUSCLE BUILDING SUPPLEMENTS (بناء العضلات)
    // ============================================
    {
        id: 1,
        name: "واي بروتين",
        nameEn: "Whey Protein",
        category: "بناء-عضلات",
        categoryEn: "muscle-building",
        icon: "💪",
        summary: "أفضل مصدر للبروتين سريع الامتصاص لبناء العضلات والتعافي بعد التمرين",
        summaryEn: "The best fast-absorbing protein source for muscle building and post-workout recovery",
        tags: ["بروتين", "بناء عضلات", "تعافي"],
        tagsEn: ["protein", "muscle building", "recovery"],
        benefits: [
            "يساعد في بناء وإصلاح العضلات بسرعة",
            "يحتوي على جميع الأحماض الأمينية الأساسية",
            "يعزز الشعور بالشبع ويساعد في إدارة الوزن",
            "يدعم جهاز المناعة",
            "سريع الامتصاص (خلال 30-60 دقيقة)"
        ],
        benefitsEn: [
            "Helps build and repair muscles quickly",
            "Contains all essential amino acids",
            "Enhances satiety and helps with weight management",
            "Supports immune system",
            "Fast absorption (within 30-60 minutes)"
        ],
        dosage: {
            recommended: "20-30 جرام",
            timing: "بعد التمرين مباشرة أو بين الوجبات",
            frequency: "1-3 مرات يومياً"
        },
        dosageEn: {
            recommended: "20-30 grams",
            timing: "Immediately after workout or between meals",
            frequency: "1-3 times daily"
        },
        warnings: [
            "قد يسبب اضطرابات هضمية لمن يعانون من حساسية اللاكتوز",
            "تجنبه إذا كان لديك حساسية من الحليب",
            "استشر طبيبك إذا كنت تعاني من مشاكل في الكلى"
        ],
        warningsEn: [
            "May cause digestive issues for those with lactose intolerance",
            "Avoid if you have milk allergy",
            "Consult your doctor if you have kidney problems"
        ],
        interactions: "قد يتفاعل مع أدوية هشاشة العظام (Bisphosphonates) ومضادات الحموضة",
        interactionsEn: "May interact with osteoporosis medications (Bisphosphonates) and antacids",
        naturalSources: "الحليب، الجبن، الزبادي، مصل اللبن الطبيعي",
        naturalSourcesEn: "Milk, cheese, yogurt, natural whey"
    },
    {
        id: 2,
        name: "كازين بروتين",
        nameEn: "Casein Protein",
        category: "بناء-عضلات",
        categoryEn: "muscle-building",
        icon: "🥛",
        summary: "بروتين بطيء الامتصاص يغذي العضلات لساعات طويلة - مثالي قبل النوم",
        summaryEn: "Slow-digesting protein that feeds muscles for hours - ideal before bedtime",
        tags: ["بروتين", "بطيء الامتصاص", "قبل النوم"],
        tagsEn: ["protein", "slow digestion", "bedtime"],
        benefits: [
            "يوفر تدفقاً مستمراً للأحماض الأمينية لمدة 6-8 ساعات",
            "يمنع هدم العضلات أثناء النوم أو الصيام",
            "يزيد الشعور بالشبع لفترة طويلة",
            "يدعم التعافي العضلي البطيء والمستدام"
        ],
        benefitsEn: [
            "Provides steady amino acid flow for 6-8 hours",
            "Prevents muscle breakdown during sleep or fasting",
            "Increases satiety for extended periods",
            "Supports slow and sustained muscle recovery"
        ],
        dosage: {
            recommended: "20-40 جرام",
            timing: "قبل النوم أو بين الوجبات البعيدة",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "20-40 grams",
            timing: "Before bedtime or between distant meals",
            frequency: "Once daily"
        },
        warnings: [
            "تجنبه إذا كان لديك حساسية من الحليب",
            "قد يسبب انتفاخ لدى بعض الأشخاص",
            "استشر طبيبك إذا كنت تعاني من مشاكل في الكلى"
        ],
        warningsEn: [
            "Avoid if you have milk allergy",
            "May cause bloating in some people",
            "Consult your doctor if you have kidney problems"
        ],
        interactions: "قد يتفاعل مع مضادات الحموضة وأدوية هشاشة العظام",
        interactionsEn: "May interact with antacids and osteoporosis medications",
        naturalSources: "الحليب كامل الدسم، الجبن القريش، الزبادي اليوناني",
        naturalSourcesEn: "Whole milk, cottage cheese, Greek yogurt"
    },
    {
        id: 3,
        name: "كرياتين مونوهيدرات",
        nameEn: "Creatine Monohydrate",
        category: "بناء-عضلات",
        categoryEn: "muscle-building",
        icon: "⚡",
        summary: "المكمل رقم 1 المدعوم علمياً لزيادة القوة والكتلة العضلية والأداء الرياضي",
        summaryEn: "The #1 scientifically-backed supplement for increasing strength, muscle mass, and athletic performance",
        tags: ["قوة", "أداء", "كتلة عضلية"],
        tagsEn: ["strength", "performance", "muscle mass"],
        benefits: [
            "يزيد القوة والأداء الرياضي بنسبة 10-15%",
            "يساعد في بناء الكتلة العضلية الصافية",
            "يسرّع التعافي بين التمارين",
            "يحسن الأداء في التمارين عالية الكثافة",
            "يدعم صحة الدماغ والوظائف الإدراكية"
        ],
        benefitsEn: [
            "Increases strength and athletic performance by 10-15%",
            "Helps build lean muscle mass",
            "Accelerates recovery between workouts",
            "Improves performance in high-intensity exercises",
            "Supports brain health and cognitive functions"
        ],
        dosage: {
            recommended: "3-5 جرام",
            timing: "في أي وقت (مع الوجبة أو بعد التمرين)",
            frequency: "يومياً بشكل مستمر"
        },
        dosageEn: {
            recommended: "3-5 grams",
            timing: "Anytime (with meal or post-workout)",
            frequency: "Daily consistently"
        },
        warnings: [
            "قد يسبب احتباس بسيط للماء (1-2 كجم)",
            "اشرب الكثير من الماء (3-4 لتر يومياً)",
            "تجنبه إذا كنت تعاني من مشاكل في الكلى",
            "قد يسبب اضطراب معدة إذا لم تشرب كمية كافية من الماء"
        ],
        warningsEn: [
            "May cause slight water retention (1-2 kg)",
            "Drink plenty of water (3-4 liters daily)",
            "Avoid if you have kidney problems",
            "May cause stomach upset if not drinking enough water"
        ],
        interactions: "آمن مع معظم الأدوية - استشر طبيبك إذا كنت تتناول أدوية للكلى",
        interactionsEn: "Safe with most medications - consult doctor if taking kidney medications",
        naturalSources: "اللحوم الحمراء، الأسماك (بكميات قليلة)",
        naturalSourcesEn: "Red meat, fish (in small amounts)"
    },
    {
        id: 4,
        name: "أحماض أمينية متفرعة BCAA",
        nameEn: "Branched-Chain Amino Acids (BCAA)",
        category: "بناء-عضلات",
        categoryEn: "muscle-building",
        icon: "🔗",
        summary: "ثلاثة أحماض أمينية أساسية تمنع هدم العضلات وتسرع التعافي",
        summaryEn: "Three essential amino acids that prevent muscle breakdown and accelerate recovery",
        tags: ["أحماض أمينية", "تعافي", "منع الهدم"],
        tagsEn: ["amino acids", "recovery", "anti-catabolic"],
        benefits: [
            "يمنع هدم العضلات أثناء التمرين",
            "يقلل ألم العضلات بعد التمرين",
            "يسرع التعافي العضلي",
            "يقلل التعب أثناء التمرين",
            "يحسن تخليق البروتين العضلي"
        ],
        benefitsEn: [
            "Prevents muscle breakdown during exercise",
            "Reduces muscle soreness after workout",
            "Accelerates muscle recovery",
            "Reduces fatigue during exercise",
            "Improves muscle protein synthesis"
        ],
        dosage: {
            recommended: "5-10 جرام",
            timing: "قبل أو أثناء أو بعد التمرين",
            frequency: "1-3 مرات يومياً"
        },
        dosageEn: {
            recommended: "5-10 grams",
            timing: "Before, during, or after workout",
            frequency: "1-3 times daily"
        },
        warnings: [
            "لا حاجة له إذا كنت تتناول كمية كافية من البروتين",
            "قد يكون غير ضروري مع استخدام الواي بروتين",
            "استشر طبيبك إذا كنت تعاني من مرض كبدي"
        ],
        warningsEn: [
            "Not needed if consuming adequate protein",
            "May be unnecessary with whey protein use",
            "Consult doctor if you have liver disease"
        ],
        interactions: "آمن مع معظم الأدوية",
        interactionsEn: "Safe with most medications",
        naturalSources: "اللحوم، الدجاج، الأسماك، البيض، منتجات الألبان",
        naturalSourcesEn: "Meat, chicken, fish, eggs, dairy products"
    },
    {
        id: 5,
        name: "بيتا ألانين",
        nameEn: "Beta-Alanine",
        category: "بناء-عضلات",
        categoryEn: "muscle-building",
        icon: "🔥",
        summary: "يزيد قدرة التحمل العضلي ويؤخر الشعور بالتعب خلال التمارين المكثفة",
        summaryEn: "Increases muscular endurance and delays fatigue during intense workouts",
        tags: ["تحمل عضلي", "أداء", "قوة"],
        tagsEn: ["muscular endurance", "performance", "strength"],
        benefits: [
            "يزيد قدرة التحمل العضلي بنسبة 13-19%",
            "يؤخر الشعور بالتعب والحرقان العضلي",
            "يحسن الأداء في التمارين عالية الكثافة (8-15 دقيقة)",
            "يزيد عدد التكرارات في التمارين",
            "يساعد في بناء الكتلة العضلية الصافية"
        ],
        benefitsEn: [
            "Increases muscular endurance by 13-19%",
            "Delays fatigue and muscle burn sensation",
            "Improves performance in high-intensity exercises (8-15 minutes)",
            "Increases repetitions in workouts",
            "Helps build lean muscle mass"
        ],
        dosage: {
            recommended: "2-5 جرام",
            timing: "قبل التمرين بـ 30-60 دقيقة",
            frequency: "يومياً بشكل مستمر"
        },
        dosageEn: {
            recommended: "2-5 grams",
            timing: "30-60 minutes before workout",
            frequency: "Daily consistently"
        },
        warnings: [
            "قد يسبب وخز أو تنميل مؤقت في الجلد (طبيعي وغير ضار)",
            "الوخز يختفي بعد 60-90 دقيقة",
            "يمكن تقليل الوخز بتقسيم الجرعة على مرتين"
        ],
        warningsEn: [
            "May cause temporary tingling or numbness in skin (normal and harmless)",
            "Tingling disappears after 60-90 minutes",
            "Can reduce tingling by splitting dose into two"
        ],
        interactions: "آمن مع معظم الأدوية والمكملات",
        interactionsEn: "Safe with most medications and supplements",
        naturalSources: "اللحوم الحمراء، الدجاج، الأسماك (بكميات قليلة جداً)",
        naturalSourcesEn: "Red meat, chicken, fish (in very small amounts)"
    },

    // ============================================
    // GENERAL HEALTH SUPPLEMENTS (الصحة العامة)
    // ============================================
    {
        id: 6,
        name: "الفيتامينات المتعددة",
        nameEn: "Multivitamins",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "💊",
        summary: "تأمين صحي شامل يغطي احتياجاتك اليومية من الفيتامينات والمعادن الأساسية",
        summaryEn: "Comprehensive health insurance covering your daily essential vitamins and minerals needs",
        tags: ["فيتامينات", "معادن", "صحة عامة"],
        tagsEn: ["vitamins", "minerals", "general health"],
        benefits: [
            "يسد الفجوات الغذائية في النظام اليومي",
            "يدعم جهاز المناعة والطاقة",
            "يحسن صحة البشرة والشعر والأظافر",
            "يدعم صحة العظام والعضلات",
            "يقلل خطر نقص الفيتامينات والمعادن"
        ],
        benefitsEn: [
            "Fills nutritional gaps in daily diet",
            "Supports immune system and energy",
            "Improves skin, hair, and nail health",
            "Supports bone and muscle health",
            "Reduces risk of vitamin and mineral deficiencies"
        ],
        dosage: {
            recommended: "حبة واحدة",
            timing: "مع وجبة الإفطار",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "One tablet",
            timing: "With breakfast",
            frequency: "Once daily"
        },
        warnings: [
            "لا تتجاوز الجرعة الموصى بها",
            "الجرعات الزائدة من الفيتامينات الذائبة في الدهون (A, D, E, K) قد تكون ضارة",
            "استشر طبيبك إذا كنت حاملاً أو تتناول أدوية"
        ],
        warningsEn: [
            "Do not exceed recommended dose",
            "Excess doses of fat-soluble vitamins (A, D, E, K) may be harmful",
            "Consult doctor if pregnant or taking medications"
        ],
        interactions: "قد يتفاعل مع مميعات الدم (فيتامين K) وأدوية الغدة الدرقية",
        interactionsEn: "May interact with blood thinners (vitamin K) and thyroid medications",
        naturalSources: "الفواكه، الخضروات، اللحوم، الحبوب الكاملة، منتجات الألبان",
        naturalSourcesEn: "Fruits, vegetables, meat, whole grains, dairy products"
    },
    {
        id: 7,
        name: "أوميغا 3 (زيت السمك)",
        nameEn: "Omega-3 Fish Oil",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "🐟",
        summary: "الدهون الصحية الأساسية لصحة القلب والدماغ والمفاصل ومكافحة الالتهابات",
        summaryEn: "Essential healthy fats for heart, brain, joint health and fighting inflammation",
        tags: ["أوميغا 3", "قلب", "دماغ", "مضاد التهاب"],
        tagsEn: ["omega-3", "heart", "brain", "anti-inflammatory"],
        benefits: [
            "يحسن صحة القلب والأوعية الدموية",
            "يخفض الكوليسترول الضار (LDL) ويرفع النافع (HDL)",
            "يدعم صحة الدماغ والذاكرة والتركيز",
            "يقلل الالتهابات وآلام المفاصل",
            "يحسن المزاج ويقلل القلق والاكتئاب",
            "يدعم صحة العين والبشرة"
        ],
        benefitsEn: [
            "Improves heart and cardiovascular health",
            "Lowers bad cholesterol (LDL) and raises good (HDL)",
            "Supports brain health, memory, and focus",
            "Reduces inflammation and joint pain",
            "Improves mood and reduces anxiety and depression",
            "Supports eye and skin health"
        ],
        dosage: {
            recommended: "1000-2000 ملغ EPA+DHA",
            timing: "مع وجبة تحتوي على دهون",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "1000-2000 mg EPA+DHA",
            timing: "With meal containing fats",
            frequency: "Once daily"
        },
        warnings: [
            "قد يسبب طعم سمك أو تجشؤ (اختر كبسولات معوية)",
            "قد يزيد خطر النزيف بجرعات عالية جداً (+3 جرام)",
            "استشر طبيبك إذا كنت تتناول مميعات الدم"
        ],
        warningsEn: [
            "May cause fishy taste or burping (choose enteric capsules)",
            "May increase bleeding risk at very high doses (+3 grams)",
            "Consult doctor if taking blood thinners"
        ],
        interactions: "قد يتفاعل مع مميعات الدم (Aspirin, Warfarin) - استشر طبيبك",
        interactionsEn: "May interact with blood thinners (Aspirin, Warfarin) - consult doctor",
        naturalSources: "السلمون، التونة، الماكريل، السردين، بذور الكتان، الجوز",
        naturalSourcesEn: "Salmon, tuna, mackerel, sardines, flaxseed, walnuts"
    },
    {
        id: 8,
        name: "فيتامين د3",
        nameEn: "Vitamin D3 (Cholecalciferol)",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "☀️",
        summary: "فيتامين الشمس الأساسي لصحة العظام والمناعة والمزاج - يعاني 70% من العرب من نقصه",
        summaryEn: "The essential sunshine vitamin for bone health, immunity, and mood - 70% of Arabs are deficient",
        tags: ["فيتامين د", "عظام", "مناعة", "مزاج"],
        tagsEn: ["vitamin D", "bones", "immunity", "mood"],
        benefits: [
            "يقوي العظام والأسنان ويمنع هشاشة العظام",
            "يدعم جهاز المناعة بقوة",
            "يحسن المزاج ويقلل الاكتئاب",
            "يدعم صحة القلب والعضلات",
            "يقلل خطر الأمراض المزمنة",
            "ضروري لامتصاص الكالسيوم"
        ],
        benefitsEn: [
            "Strengthens bones and teeth, prevents osteoporosis",
            "Strongly supports immune system",
            "Improves mood and reduces depression",
            "Supports heart and muscle health",
            "Reduces risk of chronic diseases",
            "Essential for calcium absorption"
        ],
        dosage: {
            recommended: "1000-4000 وحدة دولية",
            timing: "مع وجبة تحتوي على دهون",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "1000-4000 IU",
            timing: "With meal containing fats",
            frequency: "Once daily"
        },
        warnings: [
            "نقص فيتامين د شائع جداً في العالم العربي",
            "يُنصح بفحص مستوى فيتامين د في الدم",
            "الجرعات العالية جداً (+10,000 وحدة يومياً لفترة طويلة) قد تكون ضارة"
        ],
        warningsEn: [
            "Vitamin D deficiency is very common in Arab world",
            "Blood level testing recommended",
            "Very high doses (+10,000 IU daily long-term) may be harmful"
        ],
        interactions: "قد يتفاعل مع أدوية الكورتيزون وأدوية إنقاص الوزن",
        interactionsEn: "May interact with corticosteroids and weight loss medications",
        naturalSources: "أشعة الشمس (15-30 دقيقة يومياً)، صفار البيض، السلمون، الحليب المدعم",
        naturalSourcesEn: "Sunlight (15-30 minutes daily), egg yolk, salmon, fortified milk"
    },
    {
        id: 9,
        name: "مغنيسيوم",
        nameEn: "Magnesium",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "✨",
        summary: "معدن حيوي مشارك في أكثر من 300 عملية حيوية - للعضلات والطاقة والنوم والمزاج",
        summaryEn: "Vital mineral involved in over 300 bodily processes - for muscles, energy, sleep, and mood",
        tags: ["معادن", "نوم", "عضلات", "طاقة"],
        tagsEn: ["minerals", "sleep", "muscles", "energy"],
        benefits: [
            "يحسن جودة النوم ويقلل الأرق",
            "يمنع تشنجات وتقلصات العضلات",
            "يزيد مستويات الطاقة ويقلل التعب",
            "يحسن المزاج ويقلل القلق والتوتر",
            "يدعم صحة القلب وضغط الدم",
            "يحسن حساسية الأنسولين وصحة العظام"
        ],
        benefitsEn: [
            "Improves sleep quality and reduces insomnia",
            "Prevents muscle cramps and spasms",
            "Increases energy levels and reduces fatigue",
            "Improves mood and reduces anxiety and stress",
            "Supports heart health and blood pressure",
            "Improves insulin sensitivity and bone health"
        ],
        dosage: {
            recommended: "200-400 ملغ",
            timing: "قبل النوم أو مع وجبة العشاء",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "200-400 mg",
            timing: "Before bedtime or with dinner",
            frequency: "Once daily"
        },
        warnings: [
            "قد يسبب إسهال بجرعات عالية",
            "ابدأ بجرعة منخفضة (200 ملغ) ثم زدها تدريجياً",
            "النوع الأفضل: Magnesium Glycinate أو Citrate"
        ],
        warningsEn: [
            "May cause diarrhea at high doses",
            "Start with low dose (200 mg) then increase gradually",
            "Best forms: Magnesium Glycinate or Citrate"
        ],
        interactions: "قد يتفاعل مع مدرات البول وبعض المضادات الحيوية",
        interactionsEn: "May interact with diuretics and some antibiotics",
        naturalSources: "المكسرات، البذور، البقوليات، السبانخ، الموز، الشوكولاتة الداكنة",
        naturalSourcesEn: "Nuts, seeds, legumes, spinach, bananas, dark chocolate"
    },
    {
        id: 10,
        name: "زنك",
        nameEn: "Zinc",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "🛡️",
        summary: "معدن أساسي لجهاز المناعة والهرمونات والتئام الجروح وصحة البشرة",
        summaryEn: "Essential mineral for immune system, hormones, wound healing, and skin health",
        tags: ["معادن", "مناعة", "هرمونات", "بشرة"],
        tagsEn: ["minerals", "immunity", "hormones", "skin"],
        benefits: [
            "يقوي جهاز المناعة ويقلل مدة نزلات البرد",
            "يدعم إنتاج هرمون التستوستيرون لدى الرجال",
            "يحسن صحة البشرة وعلاج حب الشباب",
            "يسرع التئام الجروح",
            "يدعم صحة الشعر ويقلل تساقطه",
            "يحسن حاسة الشم والتذوق"
        ],
        benefitsEn: [
            "Strengthens immune system and reduces cold duration",
            "Supports testosterone production in men",
            "Improves skin health and treats acne",
            "Accelerates wound healing",
            "Supports hair health and reduces hair loss",
            "Improves sense of smell and taste"
        ],
        dosage: {
            recommended: "15-30 ملغ",
            timing: "مع وجبة خفيفة (لتجنب الغثيان)",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "15-30 mg",
            timing: "With light meal (to avoid nausea)",
            frequency: "Once daily"
        },
        warnings: [
            "لا تتجاوز 40 ملغ يومياً لفترة طويلة",
            "الجرعات العالية قد تسبب نقص النحاس",
            "قد يسبب غثيان إذا أخذ على معدة فارغة"
        ],
        warningsEn: [
            "Do not exceed 40 mg daily long-term",
            "High doses may cause copper deficiency",
            "May cause nausea if taken on empty stomach"
        ],
        interactions: "قد يتفاعل مع المضادات الحيوية والكالسيوم والحديد (خذها في أوقات منفصلة)",
        interactionsEn: "May interact with antibiotics, calcium, and iron (take at separate times)",
        naturalSources: "المحار، اللحوم الحمراء، الدجاج، البقوليات، المكسرات، البذور",
        naturalSourcesEn: "Oysters, red meat, chicken, legumes, nuts, seeds"
    },

    // ============================================
    // WEIGHT LOSS SUPPLEMENTS (التخسيس)
    // ============================================
    {
        id: 11,
        name: "مستخلص الشاي الأخضر",
        nameEn: "Green Tea Extract",
        category: "تخسيس",
        categoryEn: "weight-loss",
        icon: "🍵",
        summary: "مضاد أكسدة قوي يسرّع حرق الدهون ويزيد معدل الأيض بشكل طبيعي",
        summaryEn: "Powerful antioxidant that accelerates fat burning and increases metabolism naturally",
        tags: ["حرق دهون", "أيض", "مضاد أكسدة"],
        tagsEn: ["fat burning", "metabolism", "antioxidant"],
        benefits: [
            "يزيد معدل حرق الدهون بنسبة 4-5%",
            "يسرع عملية الأيض ويزيد حرق السعرات",
            "مضاد أكسدة قوي يحمي الخلايا",
            "يحسن صحة القلب ويخفض الكوليسترول",
            "يدعم صحة الدماغ والتركيز",
            "يساعد في تقليل دهون البطن"
        ],
        benefitsEn: [
            "Increases fat burning rate by 4-5%",
            "Accelerates metabolism and increases calorie burn",
            "Powerful antioxidant that protects cells",
            "Improves heart health and lowers cholesterol",
            "Supports brain health and focus",
            "Helps reduce belly fat"
        ],
        dosage: {
            recommended: "250-500 ملغ (EGCG)",
            timing: "قبل الإفطار أو التمرين",
            frequency: "1-2 مرات يومياً"
        },
        dosageEn: {
            recommended: "250-500 mg (EGCG)",
            timing: "Before breakfast or workout",
            frequency: "1-2 times daily"
        },
        warnings: [
            "يحتوي على كافيين (50-100 ملغ لكل جرعة)",
            "تجنبه قبل النوم بـ 6 ساعات",
            "لا تتجاوز 800 ملغ يومياً",
            "استشر طبيبك إذا كنت تعاني من مشاكل في الكبد"
        ],
        warningsEn: [
            "Contains caffeine (50-100 mg per dose)",
            "Avoid 6 hours before bedtime",
            "Do not exceed 800 mg daily",
            "Consult doctor if you have liver problems"
        ],
        interactions: "قد يتفاعل مع مميعات الدم وأدوية ضغط الدم",
        interactionsEn: "May interact with blood thinners and blood pressure medications",
        naturalSources: "الشاي الأخضر الطبيعي (3-5 أكواب يومياً)",
        naturalSourcesEn: "Natural green tea (3-5 cups daily)"
    },
    {
        id: 12,
        name: "حمض اللينوليك المترافق CLA",
        nameEn: "Conjugated Linoleic Acid (CLA)",
        category: "تخسيس",
        categoryEn: "weight-loss",
        icon: "🔻",
        summary: "حمض دهني طبيعي يساعد في تقليل الدهون مع الحفاظ على الكتلة العضلية",
        summaryEn: "Natural fatty acid that helps reduce fat while preserving muscle mass",
        tags: ["حرق دهون", "حفظ عضلات", "تحسين جسم"],
        tagsEn: ["fat burning", "muscle preservation", "body composition"],
        benefits: [
            "يساعد في تقليل دهون الجسم (خاصة البطن)",
            "يحافظ على الكتلة العضلية أثناء التخسيس",
            "يحسن نسبة العضلات إلى الدهون",
            "يدعم صحة القلب والأوعية الدموية",
            "قد يحسن حساسية الأنسولين"
        ],
        benefitsEn: [
            "Helps reduce body fat (especially belly fat)",
            "Preserves muscle mass during weight loss",
            "Improves muscle-to-fat ratio",
            "Supports heart and cardiovascular health",
            "May improve insulin sensitivity"
        ],
        dosage: {
            recommended: "3000-6000 ملغ",
            timing: "مع الوجبات الرئيسية",
            frequency: "مقسمة على 3 مرات يومياً"
        },
        dosageEn: {
            recommended: "3000-6000 mg",
            timing: "With main meals",
            frequency: "Split into 3 times daily"
        },
        warnings: [
            "النتائج تحتاج إلى 3-6 أشهر للظهور",
            "قد يسبب اضطرابات هضمية بسيطة",
            "لا تتوقع نتائج سحرية - يحتاج نظام غذائي سليم"
        ],
        warningsEn: [
            "Results need 3-6 months to appear",
            "May cause mild digestive disturbances",
            "Don't expect magic results - needs proper diet"
        ],
        interactions: "آمن مع معظم الأدوية",
        interactionsEn: "Safe with most medications",
        naturalSources: "منتجات الألبان من الأبقار التي تتغذى على العشب، لحم البقر",
        naturalSourcesEn: "Dairy from grass-fed cows, beef"
    },
    {
        id: 13,
        name: "إل-كارنتين",
        nameEn: "L-Carnitine",
        category: "تخسيس",
        categoryEn: "weight-loss",
        icon: "🚀",
        summary: "ناقل للأحماض الدهنية إلى الخلايا لحرقها وإنتاج الطاقة - مثالي للتخسيس",
        summaryEn: "Transporter of fatty acids to cells for burning and energy production - ideal for weight loss",
        tags: ["حرق دهون", "طاقة", "أداء"],
        tagsEn: ["fat burning", "energy", "performance"],
        benefits: [
            "ينقل الأحماض الدهنية لحرقها وإنتاج طاقة",
            "يزيد حرق الدهون أثناء التمرين",
            "يزيد مستويات الطاقة ويقلل التعب",
            "يحسن الأداء الرياضي والتعافي",
            "يدعم صحة القلب والدماغ"
        ],
        benefitsEn: [
            "Transports fatty acids for burning and energy production",
            "Increases fat burning during exercise",
            "Increases energy levels and reduces fatigue",
            "Improves athletic performance and recovery",
            "Supports heart and brain health"
        ],
        dosage: {
            recommended: "1000-2000 ملغ",
            timing: "قبل التمرين بـ 30-60 دقيقة",
            frequency: "1-2 مرات يومياً"
        },
        dosageEn: {
            recommended: "1000-2000 mg",
            timing: "30-60 minutes before workout",
            frequency: "1-2 times daily"
        },
        warnings: [
            "قد يسبب غثيان أو اضطراب معدة",
            "تجنبه قبل النوم (قد يسبب أرق)",
            "النتائج تحسن مع الوقت (4-12 أسبوع)",
            "النوع الأفضل: Acetyl L-Carnitine"
        ],
        warningsEn: [
            "May cause nausea or stomach upset",
            "Avoid before bedtime (may cause insomnia)",
            "Results improve over time (4-12 weeks)",
            "Best form: Acetyl L-Carnitine"
        ],
        interactions: "قد يتفاعل مع أدوية الغدة الدرقية - استشر طبيبك",
        interactionsEn: "May interact with thyroid medications - consult doctor",
        naturalSources: "اللحوم الحمراء، الدجاج، الأسماك، الحليب (بكميات قليلة)",
        naturalSourcesEn: "Red meat, chicken, fish, milk (in small amounts)"
    },

    // ============================================
    // SLEEP & MENTAL HEALTH (النوم والصحة النفسية)
    // ============================================
    {
        id: 14,
        name: "ميلاتونين",
        nameEn: "Melatonin",
        category: "نوم-نفسية",
        categoryEn: "sleep-mental",
        icon: "😴",
        summary: "هرمون النوم الطبيعي - الحل الأمثل للأرق واضطرابات النوم وتنظيم الساعة البيولوجية",
        summaryEn: "Natural sleep hormone - optimal solution for insomnia, sleep disorders, and circadian rhythm regulation",
        tags: ["نوم", "أرق", "ساعة بيولوجية"],
        tagsEn: ["sleep", "insomnia", "circadian rhythm"],
        benefits: [
            "يسهل النوم ويقلل وقت الاستغراق في النوم",
            "يحسن جودة وعمق النوم",
            "ينظم الساعة البيولوجية (Circadian Rhythm)",
            "مفيد لاضطراب الرحلات الجوية الطويلة (Jet Lag)",
            "مضاد أكسدة قوي",
            "يدعم صحة الدماغ والعين"
        ],
        benefitsEn: [
            "Facilitates sleep and reduces time to fall asleep",
            "Improves sleep quality and depth",
            "Regulates circadian rhythm",
            "Helpful for jet lag",
            "Powerful antioxidant",
            "Supports brain and eye health"
        ],
        dosage: {
            recommended: "0.5-5 ملغ",
            timing: "قبل النوم بـ 30-60 دقيقة",
            frequency: "مرة واحدة يومياً (عند الحاجة)"
        },
        dosageEn: {
            recommended: "0.5-5 mg",
            timing: "30-60 minutes before bedtime",
            frequency: "Once daily (as needed)"
        },
        warnings: [
            "ابدأ بأقل جرعة ممكنة (0.5-1 ملغ)",
            "قد يسبب نعاس صباحي لدى البعض",
            "لا تقود السيارة أو تشغل آلات بعد تناوله",
            "لا يُنصح به للحوامل والمرضعات"
        ],
        warningsEn: [
            "Start with lowest possible dose (0.5-1 mg)",
            "May cause morning drowsiness in some",
            "Do not drive or operate machinery after taking",
            "Not recommended for pregnant or nursing women"
        ],
        interactions: "قد يتفاعل مع مميعات الدم والمهدئات - استشر طبيبك",
        interactionsEn: "May interact with blood thinners and sedatives - consult doctor",
        naturalSources: "الكرز الحامض، الموز، الشوفان، الحليب، الطماطم",
        naturalSourcesEn: "Tart cherries, bananas, oats, milk, tomatoes"
    },
    {
        id: 15,
        name: "أشواغاندا",
        nameEn: "Ashwagandha",
        category: "نوم-نفسية",
        categoryEn: "sleep-mental",
        icon: "🌿",
        summary: "عشبة هندية تقليدية تقلل التوتر والقلق وتحسن المزاج والنوم والطاقة",
        summaryEn: "Traditional Indian herb that reduces stress and anxiety, improves mood, sleep, and energy",
        tags: ["توتر", "قلق", "مزاج", "نوم"],
        tagsEn: ["stress", "anxiety", "mood", "sleep"],
        benefits: [
            "يقلل التوتر والقلق بشكل ملحوظ (يخفض الكورتيزول)",
            "يحسن المزاج ويقلل أعراض الاكتئاب",
            "يحسن جودة النوم ويقلل الأرق",
            "يزيد مستويات الطاقة والتحمل",
            "يدعم إنتاج التستوستيرون لدى الرجال",
            "يحسن التركيز والذاكرة"
        ],
        benefitsEn: [
            "Significantly reduces stress and anxiety (lowers cortisol)",
            "Improves mood and reduces depression symptoms",
            "Improves sleep quality and reduces insomnia",
            "Increases energy levels and endurance",
            "Supports testosterone production in men",
            "Improves focus and memory"
        ],
        dosage: {
            recommended: "300-500 ملغ",
            timing: "مع وجبة العشاء أو قبل النوم",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "300-500 mg",
            timing: "With dinner or before bedtime",
            frequency: "Once daily"
        },
        warnings: [
            "النتائج تحتاج 4-12 أسبوع للظهور",
            "تجنبه إذا كنت حاملاً أو مرضعاً",
            "قد يتفاعل مع أدوية الغدة الدرقية",
            "اختر مستخلص KSM-66 أو Sensoril (الأفضل)"
        ],
        warningsEn: [
            "Results need 4-12 weeks to appear",
            "Avoid if pregnant or nursing",
            "May interact with thyroid medications",
            "Choose KSM-66 or Sensoril extract (best)"
        ],
        interactions: "قد يتفاعل مع أدوية الغدة الدرقية والمهدئات - استشر طبيبك",
        interactionsEn: "May interact with thyroid medications and sedatives - consult doctor",
        naturalSources: "الأشواغاندا نبات هندي تقليدي (يُستخدم كمكمل فقط)",
        naturalSourcesEn: "Ashwagandha is traditional Indian plant (used as supplement only)"
    },
    {
        id: 16,
        name: "5-HTP",
        nameEn: "5-Hydroxytryptophan",
        category: "نوم-نفسية",
        categoryEn: "sleep-mental",
        icon: "😊",
        summary: "يتحول في الجسم إلى سيروتونين (هرمون السعادة) - يحسن المزاج والنوم ويقلل الشهية",
        summaryEn: "Converts in body to serotonin (happiness hormone) - improves mood, sleep, and reduces appetite",
        tags: ["مزاج", "سيروتونين", "نوم", "شهية"],
        tagsEn: ["mood", "serotonin", "sleep", "appetite"],
        benefits: [
            "يزيد إنتاج السيروتونين (هرمون السعادة)",
            "يحسن المزاج ويقلل الاكتئاب والقلق",
            "يحسن جودة النوم وعمقه",
            "يقلل الشهية ويساعد في التحكم بالوزن",
            "يقلل الصداع النصفي"
        ],
        benefitsEn: [
            "Increases serotonin production (happiness hormone)",
            "Improves mood and reduces depression and anxiety",
            "Improves sleep quality and depth",
            "Reduces appetite and helps with weight control",
            "Reduces migraine headaches"
        ],
        dosage: {
            recommended: "50-200 ملغ",
            timing: "قبل النوم أو مع وجبة العشاء",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "50-200 mg",
            timing: "Before bedtime or with dinner",
            frequency: "Once daily"
        },
        warnings: [
            "لا تجمعه مع مضادات الاكتئاب (SSRIs) - خطر",
            "قد يسبب غثيان أو نعاس",
            "ابدأ بجرعة منخفضة (50 ملغ)",
            "استشر طبيبك إذا كنت تتناول أدوية نفسية"
        ],
        warningsEn: [
            "Do not combine with antidepressants (SSRIs) - dangerous",
            "May cause nausea or drowsiness",
            "Start with low dose (50 mg)",
            "Consult doctor if taking psychiatric medications"
        ],
        interactions: "خطير مع مضادات الاكتئاب - لا تجمعهم أبداً - استشر طبيبك",
        interactionsEn: "Dangerous with antidepressants - never combine - consult doctor",
        naturalSources: "يُنتج من بذور نبات Griffonia simplicifolia الأفريقي",
        naturalSourcesEn: "Produced from African Griffonia simplicifolia plant seeds"
    },

    // ============================================
    // ENERGY SUPPLEMENTS (الطاقة)
    // ============================================
    {
        id: 17,
        name: "كافيين",
        nameEn: "Caffeine",
        category: "طاقة",
        categoryEn: "energy",
        icon: "☕",
        summary: "المنشط الطبيعي الأكثر شيوعاً - يزيد الطاقة والتركيز والأداء والتحمل",
        summaryEn: "The most common natural stimulant - increases energy, focus, performance, and endurance",
        tags: ["طاقة", "تركيز", "أداء", "يقظة"],
        tagsEn: ["energy", "focus", "performance", "alertness"],
        benefits: [
            "يزيد اليقظة والتركيز والانتباه",
            "يقلل الشعور بالتعب والإرهاق",
            "يحسن الأداء الرياضي والتحمل",
            "يسرع حرق الدهون ومعدل الأيض",
            "يحسن المزاج والذاكرة قصيرة المدى"
        ],
        benefitsEn: [
            "Increases alertness, focus, and concentration",
            "Reduces fatigue and exhaustion",
            "Improves athletic performance and endurance",
            "Accelerates fat burning and metabolism rate",
            "Enhances mood and short-term memory"
        ],
        dosage: {
            recommended: "100-200 ملغ",
            timing: "صباحاً أو قبل التمرين بـ 30-60 دقيقة",
            frequency: "1-3 مرات يومياً (حسب التحمل)"
        },
        dosageEn: {
            recommended: "100-200 mg",
            timing: "Morning or 30-60 minutes before workout",
            frequency: "1-3 times daily (based on tolerance)"
        },
        warnings: [
            "لا تتجاوز 400 ملغ يومياً (4 أكواب قهوة)",
            "تجنبه بعد الساعة 2 ظهراً (يؤثر على النوم)",
            "قد يسبب قلق وعصبية بجرعات عالية",
            "قد يسبب إدمان بدني خفيف"
        ],
        warningsEn: [
            "Do not exceed 400 mg daily (4 cups of coffee)",
            "Avoid after 2 PM (affects sleep)",
            "May cause anxiety and nervousness at high doses",
            "May cause mild physical dependence"
        ],
        interactions: "قد يتفاعل مع أدوية القلب وضغط الدم - استشر طبيبك",
        interactionsEn: "May interact with heart and blood pressure medications - consult your doctor",
        naturalSources: "القهوة، الشاي الأخضر، الشاي الأسود، الكاكاو، الشوكولاتة الداكنة",
        naturalSourcesEn: "Coffee, green tea, black tea, cocoa, dark chocolate"
    },
    {
        id: 18,
        name: "بري-وورك آوت",
        nameEn: "Pre-Workout",
        category: "طاقة",
        categoryEn: "energy",
        icon: "💥",
        summary: "خلطة متقدمة تفجر الطاقة والقوة والتركيز للحصول على أفضل تمرين في حياتك",
        summaryEn: "Advanced formula that explosively boosts energy, strength, and focus for your best workout ever",
        tags: ["طاقة", "تركيز", "أداء", "قوة"],
        tagsEn: ["energy", "focus", "performance", "strength"],
        benefits: [
            "يزيد الطاقة والقوة بشكل ملحوظ",
            "يحسن التركيز الذهني (Focus) أثناء التمرين",
            "يزيد التحمل العضلي والقدرة على التكرارات",
            "يؤخر التعب ويزيد شدة التمرين",
            "يسرع تدفق الدم والأكسجين للعضلات (Pump)",
            "يسرع حرق الدهون"
        ],
        benefitsEn: [
            "Significantly increases energy and strength",
            "Enhances mental focus (Focus) during workouts",
            "Increases muscular endurance and repetition capacity",
            "Delays fatigue and increases workout intensity",
            "Accelerates blood flow and oxygen to muscles (Pump)",
            "Accelerates fat burning"
        ],
        dosage: {
            recommended: "حسب التعليمات على العبوة",
            timing: "قبل التمرين بـ 20-30 دقيقة",
            frequency: "قبل التمرين فقط (ليس يومياً)"
        },
        dosageEn: {
            recommended: "Follow product instructions",
            timing: "20-30 minutes before workout",
            frequency: "Before workout only (not daily)"
        },
        warnings: [
            "يحتوي على كافيين عالي (150-350 ملغ)",
            "قد يسبب تنميل (Beta-Alanine) - طبيعي",
            "لا تستخدمه يومياً (خذ استراحة أسبوعياً)",
            "ابدأ بنصف جرعة لتقييم التحمل"
        ],
        warningsEn: [
            "Contains high caffeine (150-350 mg)",
            "May cause tingling (Beta-Alanine) - normal",
            "Do not use daily (take weekly breaks)",
            "Start with half dose to assess tolerance"
        ],
        interactions: "لا تجمعه مع قهوة أو كافيين إضافي - قد يسبب قلق",
        interactionsEn: "Do not combine with coffee or additional caffeine - may cause anxiety",
        naturalSources: "لا يوجد - هو خليط من مكملات متعددة (كافيين + بيتا ألانين + كرياتين + سيترولين)",
        naturalSourcesEn: "None - it is a blend of multiple supplements (caffeine + beta-alanine + creatine + citrulline)"
    },

    // ============================================
    // BONES & JOINTS SUPPLEMENTS (العظام والمفاصل)
    // ============================================
    {
        id: 19,
        name: "جلوكوزامين وكوندروتن",
        nameEn: "Glucosamine & Chondroitin",
        category: "عظام-مفاصل",
        categoryEn: "bones-joints",
        icon: "🦴",
        summary: "ثنائي قوي لصحة المفاصل - يقلل آلام التهاب المفاصل ويحمي الغضاريف",
        summaryEn: "Powerful duo for joint health - reduces arthritis pain and protects cartilage",
        tags: ["مفاصل", "غضاريف", "ألم", "التهاب"],
        tagsEn: ["joints", "cartilage", "pain", "inflammation"],
        benefits: [
            "يقلل آلام التهاب المفاصل (Osteoarthritis)",
            "يحمي ويعيد بناء الغضاريف التالفة",
            "يحسن مرونة وحركة المفاصل",
            "يقلل الالتهابات في المفاصل",
            "يؤخر تدهور المفاصل مع التقدم في العمر"
        ],
        benefitsEn: [
            "Reduces osteoarthritis pain",
            "Protects and rebuilds damaged cartilage",
            "Improves joint flexibility and mobility",
            "Reduces joint inflammation",
            "Slows joint deterioration with age"
        ],
        dosage: {
            recommended: "1500 ملغ جلوكوزامين + 1200 ملغ كوندروتن",
            timing: "مع الوجبات",
            frequency: "مقسمة على 2-3 مرات يومياً"
        },
        dosageEn: {
            recommended: "1500 mg glucosamine + 1200 mg chondroitin",
            timing: "With meals",
            frequency: "Divided into 2-3 times daily"
        },
        warnings: [
            "النتائج تحتاج 2-4 أشهر للظهور",
            "استشر طبيبك إذا كنت تعاني من حساسية المحار",
            "قد يؤثر على سكر الدم لدى مرضى السكري",
            "آمن للاستخدام طويل المدى"
        ],
        warningsEn: [
            "Results may take 2-4 months to appear",
            "Consult your doctor if you have shellfish allergy",
            "May affect blood sugar in diabetics",
            "Safe for long-term use"
        ],
        interactions: "قد يتفاعل مع مميعات الدم - استشر طبيبك",
        interactionsEn: "May interact with blood thinners - consult your doctor",
        naturalSources: "أصداف المحار (جلوكوزامين)، غضاريف الحيوانات (كوندروتن)",
        naturalSourcesEn: "Shellfish shells (glucosamine), animal cartilage (chondroitin)"
    },
    {
        id: 20,
        name: "كولاجين",
        nameEn: "Collagen",
        category: "عظام-مفاصل",
        categoryEn: "bones-joints",
        icon: "✨",
        summary: "البروتين الأساسي للبشرة والشعر والأظافر والمفاصل - سر الشباب والحيوية",
        summaryEn: "Essential protein for skin, hair, nails, and joints - secret to youth and vitality",
        tags: ["كولاجين", "بشرة", "شعر", "مفاصل"],
        tagsEn: ["collagen", "skin", "hair", "joints"],
        benefits: [
            "يحسن مرونة ونضارة البشرة ويقلل التجاعيد",
            "يقوي الشعر والأظافر ويقلل التقصف",
            "يدعم صحة المفاصل ويقلل الألم",
            "يحسن صحة العظام والكثافة العظمية",
            "يدعم صحة الأمعاء والجهاز الهضمي",
            "يسرع التئام الجروح"
        ],
        benefitsEn: [
            "Improves skin elasticity and radiance, reduces wrinkles",
            "Strengthens hair and nails, reduces breakage",
            "Supports joint health and reduces pain",
            "Improves bone health and bone density",
            "Supports gut and digestive health",
            "Accelerates wound healing"
        ],
        dosage: {
            recommended: "10-20 جرام",
            timing: "في أي وقت (يفضل على معدة فارغة)",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "10-20 grams",
            timing: "Anytime (preferably on empty stomach)",
            frequency: "Once daily"
        },
        warnings: [
            "النتائج تحتاج 4-12 أسبوع للظهور",
            "اختر النوع 1 و 3 للبشرة والنوع 2 للمفاصل",
            "قد يسبب شعور بالامتلاء",
            "آمن للاستخدام طويل المدى"
        ],
        warningsEn: [
            "Results may take 4-12 weeks to appear",
            "Choose type 1 and 3 for skin, type 2 for joints",
            "May cause feeling of fullness",
            "Safe for long-term use"
        ],
        interactions: "آمن مع معظم الأدوية",
        interactionsEn: "Safe with most medications",
        naturalSources: "مرق العظام، جلد الدجاج، الأسماك الغنية بالجيلاتين",
        naturalSourcesEn: "Bone broth, chicken skin, gelatin-rich fish"
    },
    {
        id: 21,
        name: "سيترولين",
        nameEn: "L-Citrulline",
        category: "طاقة",
        categoryEn: "energy",
        icon: "🍉",
        summary: "حمض أميني يتحول إلى أرجينين ويزيد أكسيد النيتريك - يحسن ضخ الدم والتحمل العضلي",
        summaryEn: "Amino acid that converts to arginine and increases nitric oxide - improves blood pump and muscular endurance",
        tags: ["تحمل", "ضخ دم", "أداء"],
        tagsEn: ["endurance", "blood pump", "performance"],
        benefits: [
            "يزيد تدفق الدم والأكسجين للعضلات (Pump)",
            "يحسن التحمل العضلي ويؤخر التعب",
            "يقلل ألم العضلات بعد التمرين بنسبة 40%",
            "يخفض ضغط الدم بشكل طبيعي",
            "يحسن الأداء في التمارين عالية الكثافة",
            "يدعم صحة القلب والأوعية الدموية"
        ],
        benefitsEn: [
            "Increases blood flow and oxygen to muscles (Pump)",
            "Improves muscular endurance and delays fatigue",
            "Reduces post-workout muscle soreness by 40%",
            "Naturally lowers blood pressure",
            "Improves performance in high-intensity exercises",
            "Supports heart and cardiovascular health"
        ],
        dosage: {
            recommended: "6-8 جرام",
            timing: "قبل التمرين بـ 60 دقيقة",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "6-8 grams",
            timing: "60 minutes before workout",
            frequency: "Once daily"
        },
        warnings: [
            "قد يسبب اضطراب معدة بجرعات عالية",
            "ابدأ بـ 3 جرام ثم زد تدريجياً",
            "آمن للاستخدام طويل المدى"
        ],
        warningsEn: [
            "May cause stomach upset at high doses",
            "Start with 3 grams then gradually increase",
            "Safe for long-term use"
        ],
        interactions: "قد يتفاعل مع أدوية ضغط الدم - استشر طبيبك",
        interactionsEn: "May interact with blood pressure medications - consult your doctor",
        naturalSources: "البطيخ، الخيار، القرع، البقوليات",
        naturalSourcesEn: "Watermelon, cucumber, squash, legumes"
    },
    {
        id: 22,
        name: "تورين",
        nameEn: "Taurine",
        category: "طاقة",
        categoryEn: "energy",
        icon: "⚡",
        summary: "حمض أميني قوي يحسن الأداء الرياضي والتركيز والطاقة - موجود في مشروبات الطاقة",
        summaryEn: "Powerful amino acid that improves athletic performance, focus, and energy - found in energy drinks",
        tags: ["طاقة", "تركيز", "قلب"],
        tagsEn: ["energy", "focus", "heart"],
        benefits: [
            "يحسن الأداء الرياضي والتحمل",
            "يدعم صحة القلب وتنظيم ضرباته",
            "يحسن التركيز واليقظة الذهنية",
            "يساعد في تنظيم مستوى السكر في الدم",
            "يدعم صحة العين والرؤية",
            "له خصائص مضادة للأكسدة"
        ],
        benefitsEn: [
            "Improves athletic performance and endurance",
            "Supports heart health and regulates heartbeat",
            "Enhances focus and mental alertness",
            "Helps regulate blood sugar levels",
            "Supports eye health and vision",
            "Has antioxidant properties"
        ],
        dosage: {
            recommended: "500-2000 ملغ",
            timing: "قبل التمرين أو في الصباح",
            frequency: "1-2 مرات يومياً"
        },
        dosageEn: {
            recommended: "500-2000 mg",
            timing: "Before workout or in the morning",
            frequency: "1-2 times daily"
        },
        warnings: [
            "آمن بجرعات تصل إلى 3000 ملغ يومياً",
            "تجنب الجرعات العالية جداً (+5000 ملغ)",
            "آمن للاستخدام طويل المدى"
        ],
        warningsEn: [
            "Safe at doses up to 3000 mg daily",
            "Avoid very high doses (+5000 mg)",
            "Safe for long-term use"
        ],
        interactions: "آمن مع معظم الأدوية",
        interactionsEn: "Safe with most medications",
        naturalSources: "الأسماك، المحار، اللحوم، منتجات الألبان",
        naturalSourcesEn: "Fish, shellfish, meat, dairy products"
    },

    // ============================================
    // ADDITIONAL SUPPLEMENTS (23-33)
    // ============================================
    {
        id: 23,
        name: "إنزيم Q10",
        nameEn: "Coenzyme Q10 (CoQ10)",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "💓",
        summary: "إنزيم حيوي لإنتاج الطاقة في الخلايا - يدعم صحة القلب ويحارب الشيخوخة",
        summaryEn: "Vital enzyme for cellular energy production - supports heart health and fights aging",
        tags: ["قلب", "طاقة", "مضاد شيخوخة"],
        tagsEn: ["heart", "energy", "anti-aging"],
        benefits: [
            "يدعم صحة القلب بقوة ويحسن وظائفه",
            "يزيد إنتاج الطاقة على مستوى الخلايا",
            "مضاد أكسدة قوي يحارب الشيخوخة",
            "يحسن الأداء الرياضي والتعافي",
            "يقلل آثار أدوية الستاتين الجانبية",
            "يحسن صحة البشرة ويقلل التجاعيد"
        ],
        benefitsEn: [
            "Strongly supports heart health and improves function",
            "Increases cellular energy production",
            "Powerful antioxidant that fights aging",
            "Improves athletic performance and recovery",
            "Reduces statin medication side effects",
            "Improves skin health and reduces wrinkles"
        ],
        dosage: {
            recommended: "100-200 ملغ",
            timing: "مع وجبة تحتوي على دهون",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "100-200 mg",
            timing: "With a meal containing fats",
            frequency: "Once daily"
        },
        warnings: [
            "النتائج تحتاج 4-12 أسبوع للظهور",
            "اختر الشكل Ubiquinol (أفضل امتصاصاً)",
            "استشر طبيبك إذا كنت تتناول أدوية القلب"
        ],
        warningsEn: [
            "Results may take 4-12 weeks to appear",
            "Choose the Ubiquinol form (better absorption)",
            "Consult your doctor if you take heart medications"
        ],
        interactions: "قد يتفاعل مع مميعات الدم وأدوية الضغط - استشر طبيبك",
        interactionsEn: "May interact with blood thinners and blood pressure medications - consult your doctor",
        naturalSources: "اللحوم العضوية (كبد، قلب)، السلمون، السردين، السبانخ",
        naturalSourcesEn: "Organ meats (liver, heart), salmon, sardines, spinach"
    },
    {
        id: 24,
        name: "ثيانين",
        nameEn: "L-Theanine",
        category: "نوم-نفسية",
        categoryEn: "sleep-mental",
        icon: "🍵",
        summary: "حمض أميني من الشاي الأخضر يحسن التركيز ويقلل التوتر بدون نعاس",
        summaryEn: "Amino acid from green tea that improves focus and reduces stress without drowsiness",
        tags: ["تركيز", "استرخاء", "قلق"],
        tagsEn: ["focus", "relaxation", "anxiety"],
        benefits: [
            "يحسن التركيز واليقظة الذهنية بدون نعاس",
            "يقلل التوتر والقلق بشكل طبيعي",
            "يحسن جودة النوم بدون تخدير",
            "يعزز تأثير الكافيين ويقلل عصبيته",
            "يدعم وظائف الدماغ والذاكرة",
            "يساعد في حالات ADHD والتشتت"
        ],
        benefitsEn: [
            "Improves focus and mental alertness without drowsiness",
            "Naturally reduces stress and anxiety",
            "Improves sleep quality without sedation",
            "Enhances caffeine effects and reduces jitteriness",
            "Supports brain function and memory",
            "Helps with ADHD and concentration issues"
        ],
        dosage: {
            recommended: "100-200 ملغ",
            timing: "في الصباح أو مع الكافيين",
            frequency: "1-3 مرات يومياً"
        },
        dosageEn: {
            recommended: "100-200 mg",
            timing: "In the morning or with caffeine",
            frequency: "1-3 times daily"
        },
        warnings: [
            "آمن جداً بجرعات تصل إلى 600 ملغ",
            "قد يسبب صداع خفيف لدى البعض",
            "رائع مع الكافيين (نسبة 1:2)"
        ],
        warningsEn: [
            "Very safe at doses up to 600 mg",
            "May cause mild headaches in some people",
            "Great with caffeine (1:2 ratio)"
        ],
        interactions: "آمن مع معظم الأدوية",
        interactionsEn: "Safe with most medications",
        naturalSources: "الشاي الأخضر، الشاي الأسود (بكميات قليلة)",
        naturalSourcesEn: "Green tea, black tea (in small amounts)"
    },
    {
        id: 25,
        name: "روديولا",
        nameEn: "Rhodiola Rosea",
        category: "نوم-نفسية",
        categoryEn: "sleep-mental",
        icon: "🌸",
        summary: "عشبة سيبيرية تقلل التوتر والإرهاق وتحسن المزاج والأداء الذهني",
        summaryEn: "Siberian herb that reduces stress and fatigue and improves mood and mental performance",
        tags: ["توتر", "طاقة", "مزاج"],
        tagsEn: ["stress", "energy", "mood"],
        benefits: [
            "يقلل التوتر والإرهاق الجسدي والذهني",
            "يحسن المزاج ويقلل أعراض الاكتئاب الخفيف",
            "يزيد الطاقة والقدرة على التحمل",
            "يحسن الأداء الذهني والذاكرة",
            "يساعد في التكيف مع الضغوط (Adaptogen)",
            "يحسن الأداء الرياضي"
        ],
        benefitsEn: [
            "Reduces physical and mental stress and fatigue",
            "Improves mood and reduces mild depression symptoms",
            "Increases energy and endurance capacity",
            "Improves mental performance and memory",
            "Helps adapt to stress (Adaptogen)",
            "Improves athletic performance"
        ],
        dosage: {
            recommended: "200-600 ملغ",
            timing: "في الصباح أو قبل الظهر",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "200-600 mg",
            timing: "In the morning or before noon",
            frequency: "Once daily"
        },
        warnings: [
            "النتائج تحتاج 1-2 أسبوع للظهور",
            "تجنبه قبل النوم (قد يسبب أرق)",
            "اختر مستخلص 3% روزافين و 1% ساليدروسيد"
        ],
        warningsEn: [
            "Results may take 1-2 weeks to appear",
            "Avoid before sleep (may cause insomnia)",
            "Choose extract with 3% rosavins and 1% salidroside"
        ],
        interactions: "قد يتفاعل مع مضادات الاكتئاب - استشر طبيبك",
        interactionsEn: "May interact with antidepressants - consult your doctor",
        naturalSources: "نبات الروديولا (يُستخدم كمكمل فقط)",
        naturalSourcesEn: "Rhodiola plant (used as supplement only)"
    },
    {
        id: 26,
        name: "جنكة بيلوبا",
        nameEn: "Ginkgo Biloba",
        category: "نوم-نفسية",
        categoryEn: "sleep-mental",
        icon: "🍃",
        summary: "عشبة صينية قديمة تحسن الذاكرة والتركيز وتدفق الدم للدماغ",
        summaryEn: "Ancient Chinese herb that improves memory and focus and increases blood flow to the brain",
        tags: ["ذاكرة", "تركيز", "دماغ"],
        tagsEn: ["memory", "focus", "brain"],
        benefits: [
            "يحسن الذاكرة والتركيز والانتباه",
            "يزيد تدفق الدم والأكسجين للدماغ",
            "يدعم صحة الدماغ مع التقدم في العمر",
            "له خصائص مضادة للأكسدة قوية",
            "قد يقلل أعراض القلق",
            "يحسن صحة العين والرؤية"
        ],
        benefitsEn: [
            "Improves memory, focus, and concentration",
            "Increases blood flow and oxygen to the brain",
            "Supports brain health with age",
            "Has strong antioxidant properties",
            "May reduce anxiety symptoms",
            "Improves eye health and vision"
        ],
        dosage: {
            recommended: "120-240 ملغ",
            timing: "مع وجبة الإفطار أو الغداء",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "120-240 mg",
            timing: "With breakfast or lunch",
            frequency: "Once daily"
        },
        warnings: [
            "النتائج تحتاج 4-6 أسابيع للظهور",
            "قد يزيد خطر النزيف بجرعات عالية",
            "استشر طبيبك إذا كنت تتناول مميعات الدم"
        ],
        warningsEn: [
            "Results may take 4-6 weeks to appear",
            "May increase bleeding risk at high doses",
            "Consult your doctor if you take blood thinners"
        ],
        interactions: "يتفاعل مع مميعات الدم وأدوية السكري - استشر طبيبك",
        interactionsEn: "Interacts with blood thinners and diabetes medications - consult your doctor",
        naturalSources: "شجرة الجنكة (يُستخدم كمكمل فقط)",
        naturalSourcesEn: "Ginkgo tree (used as supplement only)"
    },
    {
        id: 27,
        name: "عرف الأسد",
        nameEn: "Lion's Mane Mushroom",
        category: "نوم-نفسية",
        categoryEn: "sleep-mental",
        icon: "🍄",
        summary: "فطر طبي ياباني يدعم صحة الدماغ والذاكرة وقد يساعد في تجديد الخلايا العصبية",
        summaryEn: "Japanese medicinal mushroom that supports brain and memory health and may help regenerate nerve cells",
        tags: ["دماغ", "ذاكرة", "أعصاب"],
        tagsEn: ["brain", "memory", "nerves"],
        benefits: [
            "يدعم صحة الدماغ والجهاز العصبي",
            "قد يحفز نمو الخلايا العصبية (NGF)",
            "يحسن الذاكرة والتركيز",
            "يقلل القلق والاكتئاب الخفيف",
            "يدعم صحة الجهاز الهضمي",
            "له خصائص مضادة للالتهاب"
        ],
        benefitsEn: [
            "Supports brain and nervous system health",
            "May stimulate nerve cell growth (NGF)",
            "Improves memory and focus",
            "Reduces anxiety and mild depression",
            "Supports digestive system health",
            "Has anti-inflammatory properties"
        ],
        dosage: {
            recommended: "500-3000 ملغ",
            timing: "في الصباح أو مع وجبة الإفطار",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "500-3000 mg",
            timing: "In the morning or with breakfast",
            frequency: "Once daily"
        },
        warnings: [
            "النتائج تحتاج 2-8 أسابيع للظهور",
            "آمن للاستخدام طويل المدى",
            "قد يسبب حكة جلدية خفيفة لدى البعض"
        ],
        warningsEn: [
            "Results may take 2-8 weeks to appear",
            "Safe for long-term use",
            "May cause mild skin itching in some people"
        ],
        interactions: "قد يتفاعل مع أدوية السكري - استشر طبيبك",
        interactionsEn: "May interact with diabetes medications - consult your doctor",
        naturalSources: "فطر عرف الأسد الطازج (نادر)",
        naturalSourcesEn: "Fresh Lion's Mane mushroom (rare)"
    },
    {
        id: 28,
        name: "HMB",
        nameEn: "Beta-Hydroxy Beta-Methylbutyrate",
        category: "بناء-عضلات",
        categoryEn: "muscle-building",
        icon: "🔬",
        summary: "مستقلب من الليوسين يمنع هدم العضلات ويسرع التعافي والبناء العضلي",
        summaryEn: "Leucine metabolite that prevents muscle breakdown and accelerates recovery and muscle building",
        tags: ["منع هدم", "تعافي", "عضلات"],
        tagsEn: ["anti-catabolic", "recovery", "muscles"],
        benefits: [
            "يمنع هدم العضلات بقوة (Anti-Catabolic)",
            "يسرع التعافي العضلي بعد التمارين",
            "يزيد القوة والكتلة العضلية الصافية",
            "مفيد جداً لكبار السن والمبتدئين",
            "يقلل ألم العضلات بعد التمرين",
            "يحسن التكيف مع التمارين الشاقة"
        ],
        benefitsEn: [
            "Powerfully prevents muscle breakdown (Anti-Catabolic)",
            "Accelerates muscle recovery after workouts",
            "Increases strength and lean muscle mass",
            "Very beneficial for seniors and beginners",
            "Reduces post-workout muscle soreness",
            "Improves adaptation to intense training"
        ],
        dosage: {
            recommended: "3 جرام",
            timing: "قبل أو بعد التمرين",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "3 grams",
            timing: "Before or after workout",
            frequency: "Once daily"
        },
        warnings: [
            "النتائج تحتاج 2-4 أسابيع للظهور",
            "مكلف نسبياً مقارنة بالكرياتين",
            "آمن للاستخدام طويل المدى"
        ],
        warningsEn: [
            "Results may take 2-4 weeks to appear",
            "Relatively expensive compared to creatine",
            "Safe for long-term use"
        ],
        interactions: "آمن مع معظم الأدوية",
        interactionsEn: "Safe with most medications",
        naturalSources: "يُنتج في الجسم من الليوسين (كميات قليلة)",
        naturalSourcesEn: "Produced in the body from leucine (small amounts)"
    },
    {
        id: 29,
        name: "جلوتامين",
        nameEn: "L-Glutamine",
        category: "بناء-عضلات",
        categoryEn: "muscle-building",
        icon: "🧬",
        summary: "أكثر الأحماض الأمينية وفرة في العضلات - يدعم التعافي والمناعة والأمعاء",
        summaryEn: "Most abundant amino acid in muscles - supports recovery, immunity, and gut health",
        tags: ["تعافي", "مناعة", "أمعاء"],
        tagsEn: ["recovery", "immunity", "gut"],
        benefits: [
            "يسرع التعافي العضلي بعد التمارين",
            "يدعم جهاز المناعة بقوة",
            "يحسن صحة الأمعاء ويعالج التسريب المعوي",
            "يمنع هدم العضلات أثناء الدايت",
            "يقلل الرغبة الشديدة في السكر",
            "يدعم صحة الجهاز الهضمي"
        ],
        benefitsEn: [
            "Accelerates muscle recovery after workouts",
            "Strongly supports immune system",
            "Improves gut health and heals leaky gut",
            "Prevents muscle breakdown during diet",
            "Reduces sugar cravings",
            "Supports digestive system health"
        ],
        dosage: {
            recommended: "5-10 جرام",
            timing: "بعد التمرين أو قبل النوم",
            frequency: "1-2 مرات يومياً"
        },
        dosageEn: {
            recommended: "5-10 grams",
            timing: "After workout or before bed",
            frequency: "1-2 times daily"
        },
        warnings: [
            "قد لا يكون ضرورياً إذا كنت تتناول بروتين كافي",
            "مفيد أكثر للرياضيين المتقدمين",
            "آمن بجرعات تصل إلى 20 جرام"
        ],
        warningsEn: [
            "May not be necessary if you consume enough protein",
            "More beneficial for advanced athletes",
            "Safe at doses up to 20 grams"
        ],
        interactions: "آمن مع معظم الأدوية",
        interactionsEn: "Safe with most medications",
        naturalSources: "اللحوم، الأسماك، البيض، منتجات الألبان، الملفوف",
        naturalSourcesEn: "Meat, fish, eggs, dairy products, cabbage"
    },
    {
        id: 30,
        name: "أرجينين",
        nameEn: "L-Arginine",
        category: "بناء-عضلات",
        categoryEn: "muscle-building",
        icon: "💨",
        summary: "حمض أميني يزيد أكسيد النيتريك ويحسن ضخ الدم والأداء الرياضي",
        summaryEn: "Amino acid that increases nitric oxide and improves blood pump and athletic performance",
        tags: ["ضخ دم", "أداء", "قلب"],
        tagsEn: ["blood pump", "performance", "heart"],
        benefits: [
            "يزيد تدفق الدم والأكسجين للعضلات",
            "يحسن الأداء الرياضي والتحمل",
            "يدعم صحة القلب والأوعية الدموية",
            "يسرع التئام الجروح",
            "يدعم جهاز المناعة",
            "قد يحسن مستويات هرمون النمو"
        ],
        benefitsEn: [
            "Increases blood flow and oxygen to muscles",
            "Improves athletic performance and endurance",
            "Supports heart and cardiovascular health",
            "Accelerates wound healing",
            "Supports immune system",
            "May improve growth hormone levels"
        ],
        dosage: {
            recommended: "3-6 جرام",
            timing: "قبل التمرين بـ 30-60 دقيقة",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "3-6 grams",
            timing: "30-60 minutes before workout",
            frequency: "Once daily"
        },
        warnings: [
            "قد يسبب اضطراب معدة لدى البعض",
            "السيترولين أفضل لزيادة الأرجينين في الدم",
            "تجنبه إذا كان لديك هربس نشط"
        ],
        warningsEn: [
            "May cause stomach upset in some people",
            "Citrulline is better for increasing blood arginine",
            "Avoid if you have active herpes"
        ],
        interactions: "قد يتفاعل مع أدوية ضغط الدم - استشر طبيبك",
        interactionsEn: "May interact with blood pressure medications - consult your doctor",
        naturalSources: "اللحوم الحمراء، الدجاج، الأسماك، المكسرات، البذور",
        naturalSourcesEn: "Red meat, chicken, fish, nuts, seeds"
    },
    {
        id: 31,
        name: "فيتامين سي",
        nameEn: "Vitamin C (Ascorbic Acid)",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "🍊",
        summary: "فيتامين أساسي قوي لجهاز المناعة والبشرة ومضاد أكسدة طبيعي",
        summaryEn: "Essential powerful vitamin for immune system and skin, natural antioxidant",
        tags: ["مناعة", "بشرة", "مضاد أكسدة"],
        tagsEn: ["immunity", "skin", "antioxidant"],
        benefits: [
            "يقوي جهاز المناعة ويقلل مدة نزلات البرد",
            "مضاد أكسدة قوي يحمي الخلايا",
            "يدعم إنتاج الكولاجين للبشرة والمفاصل",
            "يحسن امتصاص الحديد",
            "يدعم صحة القلب والأوعية الدموية",
            "يسرع التئام الجروح"
        ],
        benefitsEn: [
            "Strengthens immune system and reduces cold duration",
            "Powerful antioxidant that protects cells",
            "Supports collagen production for skin and joints",
            "Improves iron absorption",
            "Supports heart and cardiovascular health",
            "Accelerates wound healing"
        ],
        dosage: {
            recommended: "500-1000 ملغ",
            timing: "مع وجبة الإفطار",
            frequency: "1-2 مرات يومياً"
        },
        dosageEn: {
            recommended: "500-1000 mg",
            timing: "With breakfast",
            frequency: "1-2 times daily"
        },
        warnings: [
            "الجرعات العالية جداً (+2000 ملغ) قد تسبب إسهال",
            "آمن للاستخدام طويل المدى",
            "اختر الشكل Buffered أو Liposomal (أفضل)"
        ],
        warningsEn: [
            "Very high doses (+2000 mg) may cause diarrhea",
            "Safe for long-term use",
            "Choose Buffered or Liposomal form (better)"
        ],
        interactions: "آمن مع معظم الأدوية",
        interactionsEn: "Safe with most medications",
        naturalSources: "البرتقال، الليمون، الفلفل الحلو، الفراولة، البروكلي، الكيوي",
        naturalSourcesEn: "Oranges, lemons, bell peppers, strawberries, broccoli, kiwi"
    },
    {
        id: 32,
        name: "فيتامينات ب المركبة",
        nameEn: "Vitamin B Complex",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "⚡",
        summary: "مجموعة من 8 فيتامينات أساسية لإنتاج الطاقة والجهاز العصبي والمزاج",
        summaryEn: "Group of 8 essential vitamins for energy production, nervous system, and mood",
        tags: ["طاقة", "أعصاب", "مزاج"],
        tagsEn: ["energy", "nerves", "mood"],
        benefits: [
            "تدعم إنتاج الطاقة من الطعام",
            "تحسن المزاج وتقلل التوتر",
            "تدعم صحة الجهاز العصبي والدماغ",
            "تحسن صحة البشرة والشعر والأظافر",
            "تدعم تكوين خلايا الدم الحمراء",
            "مهمة لصحة القلب والأوعية الدموية"
        ],
        benefitsEn: [
            "Support energy production from food",
            "Improve mood and reduce stress",
            "Support nervous system and brain health",
            "Improve skin, hair, and nail health",
            "Support red blood cell formation",
            "Important for heart and cardiovascular health"
        ],
        dosage: {
            recommended: "حبة واحدة (B-Complex)",
            timing: "مع وجبة الإفطار",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "One tablet (B-Complex)",
            timing: "With breakfast",
            frequency: "Once daily"
        },
        warnings: [
            "قد يحول لون البول إلى أصفر فاقع (طبيعي)",
            "تجنب الجرعات الضخمة من B6 (+100 ملغ يومياً)",
            "آمن للاستخدام طويل المدى"
        ],
        warningsEn: [
            "May turn urine bright yellow (normal)",
            "Avoid large doses of B6 (+100 mg daily)",
            "Safe for long-term use"
        ],
        interactions: "آمن مع معظم الأدوية",
        interactionsEn: "Safe with most medications",
        naturalSources: "اللحوم، الأسماك، البيض، الحبوب الكاملة، الخضروات الورقية، البقوليات",
        naturalSourcesEn: "Meat, fish, eggs, whole grains, leafy vegetables, legumes"
    },
    {
        id: 33,
        name: "حديد",
        nameEn: "Iron",
        category: "صحة-عامة",
        categoryEn: "general-health",
        icon: "🩸",
        summary: "معدن أساسي لنقل الأكسجين في الدم والطاقة - شائع نقصه لدى النساء",
        summaryEn: "Essential mineral for oxygen transport in blood and energy - commonly deficient in women",
        tags: ["دم", "طاقة", "أكسجين"],
        tagsEn: ["blood", "energy", "oxygen"],
        benefits: [
            "ضروري لإنتاج الهيموجلوبين ونقل الأكسجين",
            "يمنع ويعالج فقر الدم (الأنيميا)",
            "يزيد مستويات الطاقة ويقلل التعب",
            "يدعم جهاز المناعة",
            "يحسن التركيز والأداء الذهني",
            "يدعم صحة الشعر والأظافر"
        ],
        benefitsEn: [
            "Essential for hemoglobin production and oxygen transport",
            "Prevents and treats anemia",
            "Increases energy levels and reduces fatigue",
            "Supports immune system",
            "Improves focus and mental performance",
            "Supports hair and nail health"
        ],
        dosage: {
            recommended: "18-30 ملغ",
            timing: "على معدة فارغة أو مع فيتامين سي",
            frequency: "مرة واحدة يومياً"
        },
        dosageEn: {
            recommended: "18-30 mg",
            timing: "On empty stomach or with vitamin C",
            frequency: "Once daily"
        },
        warnings: [
            "لا تأخذه إلا إذا كان لديك نقص (افحص دمك)",
            "قد يسبب إمساك أو غثيان",
            "تجنب القهوة والشاي قبل/بعد الجرعة بساعتين",
            "الجرعات الزائدة خطيرة جداً"
        ],
        warningsEn: [
            "Only take if you have a deficiency (test blood)",
            "May cause constipation or nausea",
            "Avoid coffee and tea 2 hours before/after dose",
            "Overdoses are very dangerous"
        ],
        interactions: "يتفاعل مع الكالسيوم والشاي والقهوة - خذها منفصلة",
        interactionsEn: "Interacts with calcium, tea, and coffee - take separately",
        naturalSources: "اللحوم الحمراء، الكبد، السبانخ، العدس، الحمص، صفار البيض",
        naturalSourcesEn: "Red meat, liver, spinach, lentils, chickpeas, egg yolks"
    }
];

// Export for use in browser
if (typeof module !== 'undefined' && module.exports) {
    module.exports = supplementsDataBilingual;
}
