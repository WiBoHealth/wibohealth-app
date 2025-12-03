/**
 * WiBo Health - Bilingual Recipes Database (TEST VERSION)
 * قاعدة بيانات الوصفات الثنائية اللغة (نسخة اختبار)
 * 
 * Contains: 35 Recipes (IDs 1-35)
 * Languages: Arabic & English
 * Status: Testing Phase - Not for Production
 * 
 * Original file (recipes-data.js) remains unchanged!
 */

const recipesDatabase = [
    // === Part 1: Recipes 1-20 ===
    {
        id: 1,
        category: 'فطور صحي',
        categoryEn: 'Healthy Breakfast',
        icon: '🥣',
        title: 'شوفان بالتوت والمكسرات',
        titleEn: 'Oatmeal with Berries and Nuts',
        time: '10 دقائق',
        timeEn: '10 minutes',
        servings: 1,
        calories: 290,
        nutrition: {
            protein: 12,
            carbs: 42,
            fat: 8,
            fiber: 7
        },
        ingredients: [
            'شوفان خام - نصف كوب',
            'حليب خالي الدسم - كوب واحد',
            'توت أزرق - نصف كوب',
            'لوز محمص - 10 حبات',
            'عسل طبيعي - ملعقة صغيرة'
        ],
        ingredientsEn: [
            'Raw oats - 1/2 cup',
            'Skim milk - 1 cup',
            'Blueberries - 1/2 cup',
            'Roasted almonds - 10 pieces',
            'Natural honey - 1 tsp'
        ],
        steps: [
            'ضع الشوفان والحليب في قدر على نار متوسطة',
            'قلّب باستمرار حتى يصبح القوام كريمي (5-7 دقائق)',
            'أضف التوت والعسل وزيّن باللوز المحمص'
        ],
        stepsEn: [
            'Place oats and milk in a pot over medium heat',
            'Stir constantly until creamy (5-7 minutes)',
            'Add berries and honey, garnish with roasted almonds'
        ],
        tips: 'يمكن تحضيره بارداً في الليلة السابقة لتوفير الوقت صباحاً',
        tipsEn: 'Can be prepared cold the night before to save time in the morning'
    },
    {
        id: 2,
        category: 'فطور صحي',
        categoryEn: 'Healthy Breakfast',
        icon: '🍳',
        title: 'أومليت بياض البيض بالخضار',
        titleEn: 'Vegetable Egg White Omelet',
        time: '15 دقيقة',
        timeEn: '15 minutes',
        servings: 1,
        calories: 180,
        nutrition: {
            protein: 18,
            carbs: 12,
            fat: 6,
            fiber: 3
        },
        ingredients: [
            'بياض 3 بيضات',
            'فلفل ألوان مقطع - نصف كوب',
            'بصل أخضر مفروم - ملعقتان',
            'طماطم مقطعة - ربع كوب',
            'زيت زيتون - ملعقة صغيرة'
        ],
        ingredientsEn: [
            'Egg whites from 3 eggs',
            'Mixed bell peppers, chopped - 1/2 cup',
            'Chopped green onion - 2 tbsp',
            'Chopped tomatoes - 1/4 cup',
            'Olive oil - 1 tsp'
        ],
        steps: [
            'سخّن زيت الزيتون في مقلاة غير لاصقة',
            'أضف الخضار وقلّب لمدة 3 دقائق',
            'اخفق بياض البيض واسكبه فوق الخضار',
            'اطهِ حتى ينضج تماماً واطوِه بشكل نصف دائرة'
        ],
        stepsEn: [
            'Heat olive oil in a non-stick pan',
            'Add vegetables and sauté for 3 minutes',
            'Beat egg whites and pour over vegetables',
            'Cook until fully set and fold into half-moon shape'
        ],
        tips: 'يمكن إضافة جبن قريش قليل الدسم لزيادة محتوى البروتين',
        tipsEn: 'Low-fat cottage cheese can be added to increase protein content'
    },
    {
        id: 3,
        category: 'فطور صحي',
        categoryEn: 'Healthy Breakfast',
        icon: '🥑',
        title: 'توست الأفوكادو بالبيض',
        titleEn: 'Avocado Toast with Egg',
        time: '12 دقيقة',
        timeEn: '12 minutes',
        servings: 1,
        calories: 320,
        nutrition: {
            protein: 15,
            carbs: 28,
            fat: 16,
            fiber: 8
        },
        ingredients: [
            'خبز حبوب كاملة - شريحة واحدة',
            'أفوكادو ناضج - نصف حبة',
            'بيضة واحدة',
            'ليمون - عصير نصف حبة',
            'ملح وفلفل أسود - حسب الرغبة'
        ],
        ingredientsEn: [
            'Whole grain bread - 1 slice',
            'Ripe avocado - 1/2 piece',
            'Egg - 1 piece',
            'Lemon juice - 1/2 lemon',
            'Salt and black pepper - to taste'
        ],
        steps: [
            'حمّص شريحة الخبز حتى تصبح ذهبية',
            'اهرس الأفوكادو وأضف عصير الليمون والملح',
            'اسلق أو اقلِ البيضة حسب الرغبة',
            'وزّع الأفوكادو المهروس على التوست وضع البيضة فوقه'
        ],
        stepsEn: [
            'Toast bread slice until golden',
            'Mash avocado and add lemon juice and salt',
            'Boil or fry egg as desired',
            'Spread mashed avocado on toast and place egg on top'
        ],
        tips: 'رش القليل من الفلفل الحار المطحون لنكهة إضافية',
        tipsEn: 'Sprinkle some crushed red pepper for extra flavor'
    },
    {
        id: 4,
        category: 'فطور صحي',
        categoryEn: 'Healthy Breakfast',
        icon: '🥞',
        title: 'بان كيك الموز والشوفان',
        titleEn: 'Banana Oatmeal Pancakes',
        time: '20 دقيقة',
        timeEn: '20 minutes',
        servings: 2,
        calories: 240,
        nutrition: {
            protein: 10,
            carbs: 38,
            fat: 6,
            fiber: 5
        },
        ingredients: [
            'موز ناضج - حبة واحدة',
            'بيضتان',
            'شوفان مطحون - نصف كوب',
            'قرفة مطحونة - ملعقة صغيرة',
            'فانيليا - ربع ملعقة صغيرة'
        ],
        ingredientsEn: [
            'Ripe banana - 1 piece',
            'Eggs - 2 pieces',
            'Ground oats - 1/2 cup',
            'Ground cinnamon - 1 tsp',
            'Vanilla extract - 1/4 tsp'
        ],
        steps: [
            'اهرس الموز في وعاء',
            'أضف البيض والشوفان والقرفة والفانيليا واخلط جيداً',
            'سخّن مقلاة غير لاصقة على نار متوسطة',
            'اسكب الخليط وشكّل دوائر متوسطة الحجم',
            'اقلب البان كيك عندما تظهر فقاعات على السطح'
        ],
        stepsEn: [
            'Mash banana in a bowl',
            'Add eggs, oats, cinnamon and vanilla, mix well',
            'Heat non-stick pan over medium heat',
            'Pour batter to form medium-sized circles',
            'Flip pancakes when bubbles appear on surface'
        ],
        tips: 'قدّمها مع العسل الطبيعي أو زبدة الفول السوداني الطبيعية',
        tipsEn: 'Serve with natural honey or natural peanut butter'
    },
    {
        id: 5,
        category: 'فطور صحي',
        categoryEn: 'Healthy Breakfast',
        icon: '🥤',
        title: 'سموثي البروتين الأخضر',
        titleEn: 'Green Protein Smoothie',
        time: '5 دقائق',
        timeEn: '5 minutes',
        servings: 1,
        calories: 210,
        nutrition: {
            protein: 20,
            carbs: 25,
            fat: 4,
            fiber: 6
        },
        ingredients: [
            'سبانخ طازجة - كوب واحد',
            'موز مجمد - نصف حبة',
            'بروتين مصل الحليب - سكوب واحد',
            'حليب لوز غير محلى - كوب واحد',
            'زبدة لوز - ملعقة صغيرة'
        ],
        ingredientsEn: [
            'Fresh spinach - 1 cup',
            'Frozen banana - 1/2 piece',
            'Whey protein - 1 scoop',
            'Unsweetened almond milk - 1 cup',
            'Almond butter - 1 tsp'
        ],
        steps: [
            'ضع جميع المكونات في الخلاط',
            'اخلط على سرعة عالية حتى يصبح ناعماً تماماً',
            'أضف مكعبات ثلج إذا أردت قواماً أكثر سماكة'
        ],
        stepsEn: [
            'Place all ingredients in blender',
            'Blend on high speed until completely smooth',
            'Add ice cubes if you want a thicker consistency'
        ],
        tips: 'يمكن إضافة بذور الشيا أو الكتان المطحون لزيادة الألياف',
        tipsEn: 'Chia seeds or ground flax can be added to increase fiber'
    },
    {
        id: 6,
        category: 'سلطات صحية',
        categoryEn: 'Healthy Salads',
        icon: '🥗',
        title: 'سلطة الكينوا والأفوكادو',
        titleEn: 'Quinoa Avocado Salad',
        time: '25 دقيقة',
        timeEn: '25 minutes',
        servings: 2,
        calories: 340,
        nutrition: {
            protein: 12,
            carbs: 35,
            fat: 18,
            fiber: 10
        },
        ingredients: [
            'كينوا مطبوخة - كوب واحد',
            'أفوكادو مقطع - حبة واحدة',
            'طماطم كرزية - كوب واحد',
            'خيار مقطع - نصف كوب',
            'عصير ليمون - ملعقتان كبيرتان',
            'زيت زيتون - ملعقة كبيرة'
        ],
        ingredientsEn: [
            'Cooked quinoa - 1 cup',
            'Diced avocado - 1 piece',
            'Cherry tomatoes - 1 cup',
            'Diced cucumber - 1/2 cup',
            'Lemon juice - 2 tbsp',
            'Olive oil - 1 tbsp'
        ],
        steps: [
            'اطبخ الكينوا حسب التعليمات واتركها لتبرد',
            'قطّع الخضار والأفوكادو إلى مكعبات صغيرة',
            'اخلط جميع المكونات في وعاء كبير',
            'أضف عصير الليمون وزيت الزيتون والملح وقلّب'
        ],
        stepsEn: [
            'Cook quinoa according to instructions and let cool',
            'Dice vegetables and avocado into small cubes',
            'Mix all ingredients in a large bowl',
            'Add lemon juice, olive oil and salt, toss well'
        ],
        tips: 'يمكن تحضيرها مسبقاً وحفظها في الثلاجة لمدة 3 أيام',
        tipsEn: 'Can be prepared ahead and stored in refrigerator for 3 days'
    },
    {
        id: 7,
        category: 'سلطات صحية',
        categoryEn: 'Healthy Salads',
        icon: '🥗',
        title: 'سلطة الحمص بالطحينة',
        titleEn: 'Chickpea Tahini Salad',
        time: '15 دقيقة',
        timeEn: '15 minutes',
        servings: 2,
        calories: 280,
        nutrition: {
            protein: 14,
            carbs: 32,
            fat: 12,
            fiber: 9
        },
        ingredients: [
            'حمص مسلوق - كوب ونصف',
            'طحينة - ملعقتان كبيرتان',
            'ثوم مهروس - فص واحد',
            'بقدونس مفروم - ربع كوب',
            'عصير ليمون - ملعقتان',
            'كمون مطحون - نصف ملعقة صغيرة'
        ],
        ingredientsEn: [
            'Cooked chickpeas - 1.5 cups',
            'Tahini - 2 tbsp',
            'Crushed garlic - 1 clove',
            'Chopped parsley - 1/4 cup',
            'Lemon juice - 2 tbsp',
            'Ground cumin - 1/2 tsp'
        ],
        steps: [
            'صفّي الحمص واغسله جيداً',
            'اخلط الطحينة مع عصير الليمون والثوم والكمون',
            'أضف الحمص والبقدونس وقلّب جيداً',
            'تبّل بالملح والفلفل حسب الرغبة'
        ],
        stepsEn: [
            'Drain and rinse chickpeas well',
            'Mix tahini with lemon juice, garlic and cumin',
            'Add chickpeas and parsley, mix well',
            'Season with salt and pepper to taste'
        ],
        tips: 'يمكن إضافة خضار مشكلة حسب الرغبة',
        tipsEn: 'Mixed vegetables can be added as desired'
    },
    {
        id: 8,
        category: 'شوربات صحية',
        categoryEn: 'Healthy Soups',
        icon: '🍲',
        title: 'شوربة العدس بالخضار',
        titleEn: 'Lentil Vegetable Soup',
        time: '35 دقيقة',
        timeEn: '35 minutes',
        servings: 4,
        calories: 220,
        nutrition: {
            protein: 15,
            carbs: 35,
            fat: 3,
            fiber: 12
        },
        ingredients: [
            'عدس أحمر - كوب واحد',
            'جزر مقطع - حبتان',
            'بصل مفروم - حبة واحدة',
            'طماطم مقطعة - حبتان',
            'مرق خضار - 4 أكواب',
            'كمون وكركم - ملعقة صغيرة لكل منهما'
        ],
        ingredientsEn: [
            'Red lentils - 1 cup',
            'Diced carrots - 2 pieces',
            'Chopped onion - 1 piece',
            'Diced tomatoes - 2 pieces',
            'Vegetable broth - 4 cups',
            'Cumin and turmeric - 1 tsp each'
        ],
        steps: [
            'اغسل العدس جيداً وصفّه',
            'سخّن قدر وأضف البصل حتى يذبل',
            'أضف الجزر والطماطم وقلّب لدقيقتين',
            'أضف العدس والمرق والبهارات',
            'اطبخ على نار هادئة لمدة 25-30 دقيقة'
        ],
        stepsEn: [
            'Wash lentils well and drain',
            'Heat pot and add onion until soft',
            'Add carrots and tomatoes, stir for 2 minutes',
            'Add lentils, broth and spices',
            'Simmer for 25-30 minutes'
        ],
        tips: 'يمكن هرس الشوربة جزئياً للحصول على قوام كريمي',
        tipsEn: 'Can partially blend soup for creamy texture'
    },
    {
        id: 9,
        category: 'شوربات صحية',
        categoryEn: 'Healthy Soups',
        icon: '🍲',
        title: 'شوربة الدجاج بالخضار',
        titleEn: 'Chicken Vegetable Soup',
        time: '40 دقيقة',
        timeEn: '40 minutes',
        servings: 4,
        calories: 180,
        nutrition: {
            protein: 22,
            carbs: 15,
            fat: 4,
            fiber: 4
        },
        ingredients: [
            'صدر دجاج - 300 جرام',
            'كوسا - حبة واحدة',
            'جزر - حبتان',
            'كرفس - عودان',
            'بصل - حبة واحدة',
            'مرق دجاج قليل الصوديوم - 5 أكواب'
        ],
        ingredientsEn: [
            'Chicken breast - 300g',
            'Zucchini - 1 piece',
            'Carrots - 2 pieces',
            'Celery - 2 stalks',
            'Onion - 1 piece',
            'Low-sodium chicken broth - 5 cups'
        ],
        steps: [
            'اسلق الدجاج في المرق حتى ينضج',
            'أخرج الدجاج وقطّعه إلى مكعبات',
            'قطّع الخضار وأضفها للمرق',
            'اطبخ لمدة 20 دقيقة حتى تنضج الخضار',
            'أعد الدجاج للقدر وقدّمها ساخنة'
        ],
        stepsEn: [
            'Boil chicken in broth until cooked',
            'Remove chicken and dice it',
            'Dice vegetables and add to broth',
            'Cook for 20 minutes until vegetables are tender',
            'Return chicken to pot and serve hot'
        ],
        tips: 'يمكن إضافة معكرونة حبوب كاملة للمزيد من الإشباع',
        tipsEn: 'Whole grain pasta can be added for more satiety'
    },
    {
        id: 10,
        category: 'أطباق رئيسية - دجاج',
        categoryEn: 'Main Courses - Chicken',
        icon: '🍗',
        title: 'دجاج مشوي بالأعشاب',
        titleEn: 'Herb Grilled Chicken',
        time: '30 دقيقة',
        timeEn: '30 minutes',
        servings: 2,
        calories: 280,
        nutrition: {
            protein: 35,
            carbs: 5,
            fat: 12,
            fiber: 1
        },
        ingredients: [
            'صدر دجاج - قطعتان',
            'زيت زيتون - ملعقتان',
            'ثوم مهروس - 3 فصوص',
            'روزماري وزعتر طازج - ملعقة كبيرة',
            'ليمون - عصير حبة واحدة',
            'ملح وفلفل أسود'
        ],
        ingredientsEn: [
            'Chicken breasts - 2 pieces',
            'Olive oil - 2 tbsp',
            'Crushed garlic - 3 cloves',
            'Fresh rosemary and thyme - 1 tbsp',
            'Lemon juice - 1 piece',
            'Salt and black pepper'
        ],
        steps: [
            'اخلط زيت الزيتون والثوم والأعشاب والليمون',
            'تبّل الدجاج بالخليط واتركه 15 دقيقة',
            'سخّن الشواية أو مقلاة الشوي',
            'اشوِ الدجاج 6-7 دقائق لكل جهة',
            'اتركه يرتاح 5 دقائق قبل التقديم'
        ],
        stepsEn: [
            'Mix olive oil, garlic, herbs and lemon',
            'Season chicken with mixture and marinate for 15 minutes',
            'Heat grill or grill pan',
            'Grill chicken 6-7 minutes per side',
            'Let rest 5 minutes before serving'
        ],
        tips: 'استخدم ترمومتر للتأكد من وصول الحرارة لـ75 درجة مئوية',
        tipsEn: 'Use thermometer to ensure internal temperature reaches 75°C'
    },
    {
        id: 11,
        category: 'أطباق رئيسية - دجاج',
        categoryEn: 'Main Courses - Chicken',
        icon: '🍛',
        title: 'دجاج بالكاري والخضار',
        titleEn: 'Chicken Curry with Vegetables',
        time: '35 دقيقة',
        timeEn: '35 minutes',
        servings: 3,
        calories: 320,
        nutrition: {
            protein: 32,
            carbs: 22,
            fat: 14,
            fiber: 6
        },
        ingredients: [
            'صدر دجاج مقطع - 400 جرام',
            'بروكلي - كوب واحد',
            'فلفل ألوان - كوب واحد',
            'حليب جوز الهند قليل الدسم - نصف كوب',
            'كاري ومسحوق كركم - ملعقتان',
            'بصل وثوم - حسب الرغبة'
        ],
        ingredientsEn: [
            'Diced chicken breast - 400g',
            'Broccoli - 1 cup',
            'Bell peppers - 1 cup',
            'Low-fat coconut milk - 1/2 cup',
            'Curry and turmeric powder - 2 tbsp',
            'Onion and garlic - to taste'
        ],
        steps: [
            'سخّن قليل من الزيت وقلّي البصل والثوم',
            'أضف الدجاج وقلّبه حتى يتغير لونه',
            'أضف البهارات وقلّب لدقيقة',
            'أضف الخضار وحليب جوز الهند',
            'اطبخ لمدة 15-20 دقيقة حتى ينضج'
        ],
        stepsEn: [
            'Heat a little oil and sauté onion and garlic',
            'Add chicken and stir until color changes',
            'Add spices and stir for 1 minute',
            'Add vegetables and coconut milk',
            'Cook for 15-20 minutes until done'
        ],
        tips: 'قدّمه مع أرز بني أو خبز نان للحصول على وجبة متكاملة',
        tipsEn: 'Serve with brown rice or naan bread for a complete meal'
    },
    {
        id: 12,
        category: 'أطباق رئيسية - سمك',
        categoryEn: 'Main Courses - Fish',
        icon: '🐟',
        title: 'سلمون مشوي بصوص الليمون',
        titleEn: 'Grilled Salmon with Lemon Sauce',
        time: '20 دقيقة',
        timeEn: '20 minutes',
        servings: 2,
        calories: 350,
        nutrition: {
            protein: 34,
            carbs: 4,
            fat: 22,
            fiber: 0
        },
        ingredients: [
            'فيليه سلمون - قطعتان (150 جرام لكل)',
            'عصير ليمون - ملعقتان كبيرتان',
            'زيت زيتون - ملعقة كبيرة',
            'ثوم مهروس - فصان',
            'شبت طازج - ملعقة كبيرة',
            'ملح وفلفل'
        ],
        ingredientsEn: [
            'Salmon fillets - 2 pieces (150g each)',
            'Lemon juice - 2 tbsp',
            'Olive oil - 1 tbsp',
            'Crushed garlic - 2 cloves',
            'Fresh dill - 1 tbsp',
            'Salt and pepper'
        ],
        steps: [
            'سخّن الفرن أو الشواية لدرجة 200 مئوية',
            'اخلط الليمون والزيت والثوم والشبت',
            'ضع السلمون في صينية وافرد الخليط عليه',
            'اشوِ لمدة 12-15 دقيقة حتى ينضج',
            'قدّمه ساخناً مع شرائح الليمون'
        ],
        stepsEn: [
            'Preheat oven or grill to 200°C',
            'Mix lemon juice, oil, garlic and dill',
            'Place salmon in baking dish and spread mixture on top',
            'Grill for 12-15 minutes until cooked',
            'Serve hot with lemon slices'
        ],
        tips: 'تأكد من عدم الإفراط في الطهي للحفاظ على رطوبة السلمون',
        tipsEn: 'Avoid overcooking to maintain salmon moisture'
    },
    {
        id: 13,
        category: 'أطباق رئيسية - سمك',
        categoryEn: 'Main Courses - Fish',
        icon: '🍤',
        title: 'جمبري بالثوم والليمون',
        titleEn: 'Garlic Lemon Shrimp',
        time: '15 دقيقة',
        timeEn: '15 minutes',
        servings: 2,
        calories: 240,
        nutrition: {
            protein: 28,
            carbs: 6,
            fat: 10,
            fiber: 1
        },
        ingredients: [
            'جمبري كبير مقشر - 300 جرام',
            'ثوم مفروم - 4 فصوص',
            'زيت زيتون - ملعقتان',
            'عصير ليمون - ملعقتان',
            'بقدونس مفروم - ربع كوب',
            'فلفل حار - حسب الرغبة'
        ],
        ingredientsEn: [
            'Large peeled shrimp - 300g',
            'Minced garlic - 4 cloves',
            'Olive oil - 2 tbsp',
            'Lemon juice - 2 tbsp',
            'Chopped parsley - 1/4 cup',
            'Hot pepper - to taste'
        ],
        steps: [
            'سخّن زيت الزيتون في مقلاة واسعة',
            'أضف الثوم وقلّبه لـ30 ثانية',
            'أضف الجمبري وقلّبه لـ2-3 دقائق',
            'أضف عصير الليمون والبقدونس',
            'قدّمه فوراً وهو ساخن'
        ],
        stepsEn: [
            'Heat olive oil in a wide pan',
            'Add garlic and sauté for 30 seconds',
            'Add shrimp and sauté for 2-3 minutes',
            'Add lemon juice and parsley',
            'Serve immediately while hot'
        ],
        tips: 'لا تطبخ الجمبري أكثر من اللازم لتجنب صلابته',
        tipsEn: 'Do not overcook shrimp to avoid toughness'
    },
    {
        id: 14,
        category: 'أطباق نباتية',
        categoryEn: 'Vegetarian Dishes',
        icon: '🍆',
        title: 'باذنجان مشوي بالطحينة',
        titleEn: 'Grilled Eggplant with Tahini',
        time: '30 دقيقة',
        timeEn: '30 minutes',
        servings: 3,
        calories: 200,
        nutrition: {
            protein: 6,
            carbs: 20,
            fat: 12,
            fiber: 8
        },
        ingredients: [
            'باذنجان كبير - حبتان',
            'طحينة - 3 ملاعق كبيرة',
            'ثوم مهروس - فصان',
            'عصير ليمون - ملعقتان',
            'زيت زيتون - ملعقة كبيرة',
            'كمون - نصف ملعقة صغيرة'
        ],
        ingredientsEn: [
            'Large eggplant - 2 pieces',
            'Tahini - 3 tbsp',
            'Crushed garlic - 2 cloves',
            'Lemon juice - 2 tbsp',
            'Olive oil - 1 tbsp',
            'Cumin - 1/2 tsp'
        ],
        steps: [
            'اشوِ الباذنجان على النار حتى يصبح طرياً',
            'قشّره واهرس اللب في وعاء',
            'أضف الطحينة والثوم والليمون والكمون',
            'اخلط جيداً حتى يصبح كريمياً',
            'زيّنه بزيت الزيتون والبقدونس'
        ],
        stepsEn: [
            'Grill eggplant over fire until soft',
            'Peel and mash pulp in a bowl',
            'Add tahini, garlic, lemon and cumin',
            'Mix well until creamy',
            'Garnish with olive oil and parsley'
        ],
        tips: 'يمكن تقديمه كمقبّل مع الخبز الأسمر',
        tipsEn: 'Can be served as appetizer with brown bread'
    },
    {
        id: 15,
        category: 'أطباق نباتية',
        categoryEn: 'Vegetarian Dishes',
        icon: '🥙',
        title: 'فلافل مشوية',
        titleEn: 'Baked Falafel',
        time: '40 دقيقة',
        timeEn: '40 minutes',
        servings: 4,
        calories: 260,
        nutrition: {
            protein: 12,
            carbs: 34,
            fat: 8,
            fiber: 10
        },
        ingredients: [
            'حمص جاف منقوع - كوبان',
            'بصل مفروم - نصف كوب',
            'ثوم - 3 فصوص',
            'بقدونس وكزبرة - كوب',
            'كمون وكزبرة مطحونة - ملعقة صغيرة لكل',
            'دقيق حمص - ملعقتان'
        ],
        ingredientsEn: [
            'Soaked dry chickpeas - 2 cups',
            'Chopped onion - 1/2 cup',
            'Garlic - 3 cloves',
            'Parsley and cilantro - 1 cup',
            'Ground cumin and coriander - 1 tsp each',
            'Chickpea flour - 2 tbsp'
        ],
        steps: [
            'صفّي الحمص جيداً (لا تسلقه)',
            'اطحن الحمص مع البصل والثوم والأعشاب',
            'أضف البهارات ودقيق الحمص واخلط',
            'شكّل كرات متوسطة الحجم',
            'رصّها في صينية واخبزها لـ25 دقيقة على 180°'
        ],
        stepsEn: [
            'Drain chickpeas well (do not boil)',
            'Grind chickpeas with onion, garlic and herbs',
            'Add spices and chickpea flour, mix',
            'Form medium-sized balls',
            'Arrange in baking dish and bake 25 minutes at 180°C'
        ],
        tips: 'قدّمها في خبز البيتا مع الخضار والطحينة',
        tipsEn: 'Serve in pita bread with vegetables and tahini'
    },
    {
        id: 16,
        category: 'وجبات خفيفة',
        categoryEn: 'Snacks',
        icon: '🥜',
        title: 'كرات الطاقة بالتمر والمكسرات',
        titleEn: 'Date and Nut Energy Balls',
        time: '15 دقيقة',
        timeEn: '15 minutes',
        servings: 10,
        calories: 120,
        nutrition: {
            protein: 4,
            carbs: 16,
            fat: 5,
            fiber: 3
        },
        ingredients: [
            'تمر منزوع النوى - كوب واحد',
            'لوز خام - نصف كوب',
            'جوز - نصف كوب',
            'بذور الشيا - ملعقتان',
            'مسحوق كاكاو - ملعقتان',
            'جوز الهند المبشور - للتزيين'
        ],
        ingredientsEn: [
            'Pitted dates - 1 cup',
            'Raw almonds - 1/2 cup',
            'Walnuts - 1/2 cup',
            'Chia seeds - 2 tbsp',
            'Cocoa powder - 2 tbsp',
            'Shredded coconut - for coating'
        ],
        steps: [
            'ضع التمر والمكسرات في محضر الطعام',
            'اخلط حتى يصبح الخليط متماسكاً',
            'أضف بذور الشيا والكاكاو واخلط',
            'شكّل كرات صغيرة بحجم ملعقة كبيرة',
            'غلّفها بجوز الهند واحفظها في الثلاجة'
        ],
        stepsEn: [
            'Place dates and nuts in food processor',
            'Blend until mixture is cohesive',
            'Add chia seeds and cocoa, blend',
            'Form small balls the size of a tablespoon',
            'Coat with coconut and store in refrigerator'
        ],
        tips: 'يمكن حفظها لمدة أسبوعين في الثلاجة',
        tipsEn: 'Can be stored for two weeks in refrigerator'
    },
    {
        id: 17,
        category: 'وجبات خفيفة',
        categoryEn: 'Snacks',
        icon: '🥒',
        title: 'خضار مقطعة مع حمص',
        titleEn: 'Veggie Sticks with Hummus',
        time: '10 دقائق',
        timeEn: '10 minutes',
        servings: 2,
        calories: 180,
        nutrition: {
            protein: 8,
            carbs: 22,
            fat: 7,
            fiber: 6
        },
        ingredients: [
            'حمص مطحون - نصف كوب',
            'جزر - حبة واحدة',
            'خيار - حبة واحدة',
            'فلفل ألوان - حبة واحدة',
            'كرفس - عودان',
            'طحينة وثوم وليمون - للحمص'
        ],
        ingredientsEn: [
            'Ground hummus - 1/2 cup',
            'Carrots - 1 piece',
            'Cucumber - 1 piece',
            'Bell pepper - 1 piece',
            'Celery - 2 stalks',
            'Tahini, garlic and lemon - for hummus'
        ],
        steps: [
            'قطّع الخضار إلى أصابع طويلة',
            'حضّر الحمص بخلط الحمص المسلوق مع الطحينة',
            'أضف الثوم والليمون والملح',
            'ضع الحمص في وعاء للتغميس',
            'رتّب الخضار حوله وقدّمه'
        ],
        stepsEn: [
            'Cut vegetables into long sticks',
            'Prepare hummus by blending cooked chickpeas with tahini',
            'Add garlic, lemon and salt',
            'Place hummus in a dipping bowl',
            'Arrange vegetables around it and serve'
        ],
        tips: 'وجبة خفيفة مثالية غنية بالألياف والفيتامينات',
        tipsEn: 'Ideal snack rich in fiber and vitamins'
    },
    {
        id: 18,
        category: 'حلويات صحية',
        categoryEn: 'Healthy Desserts',
        icon: '🍌',
        title: 'آيس كريم الموز الصحي',
        titleEn: 'Healthy Banana Ice Cream',
        time: '5 دقائق + تجميد',
        timeEn: '5 minutes + freezing',
        servings: 2,
        calories: 150,
        nutrition: {
            protein: 3,
            carbs: 32,
            fat: 2,
            fiber: 4
        },
        ingredients: [
            'موز مجمد - 3 حبات',
            'حليب لوز - ربع كوب',
            'فانيليا - ربع ملعقة صغيرة',
            'مسحوق كاكاو - اختياري',
            'مكسرات للتزيين - اختياري'
        ],
        ingredientsEn: [
            'Frozen bananas - 3 pieces',
            'Almond milk - 1/4 cup',
            'Vanilla extract - 1/4 tsp',
            'Cocoa powder - optional',
            'Nuts for garnish - optional'
        ],
        steps: [
            'قطّع الموز المجمد إلى قطع صغيرة',
            'ضعه في الخلاط مع حليب اللوز والفانيليا',
            'اخلط حتى يصبح ناعماً وكريمياً',
            'أضف الكاكاو إن أردت نكهة الشوكولاتة',
            'قدّمه فوراً أو أعد تجميده'
        ],
        stepsEn: [
            'Cut frozen bananas into small pieces',
            'Place in blender with almond milk and vanilla',
            'Blend until smooth and creamy',
            'Add cocoa if you want chocolate flavor',
            'Serve immediately or refreeze'
        ],
        tips: 'استخدم موز ناضج جداً للحصول على حلاوة طبيعية',
        tipsEn: 'Use very ripe bananas for natural sweetness'
    },
    {
        id: 19,
        category: 'حلويات صحية',
        categoryEn: 'Healthy Desserts',
        icon: '🍪',
        title: 'كوكيز الشوفان بالموز',
        titleEn: 'Oatmeal Banana Cookies',
        time: '25 دقيقة',
        timeEn: '25 minutes',
        servings: 12,
        calories: 90,
        nutrition: {
            protein: 3,
            carbs: 15,
            fat: 3,
            fiber: 2
        },
        ingredients: [
            'موز ناضج مهروس - حبتان',
            'شوفان - كوب ونصف',
            'زبيب - ربع كوب',
            'قرفة - ملعقة صغيرة',
            'فانيليا - نصف ملعقة صغيرة',
            'رقائق شوكولاتة داكنة - اختياري'
        ],
        ingredientsEn: [
            'Mashed ripe bananas - 2 pieces',
            'Oats - 1.5 cups',
            'Raisins - 1/4 cup',
            'Cinnamon - 1 tsp',
            'Vanilla extract - 1/2 tsp',
            'Dark chocolate chips - optional'
        ],
        steps: [
            'سخّن الفرن لدرجة 180 مئوية',
            'اخلط الموز المهروس مع الشوفان والقرفة',
            'أضف الزبيب والفانيليا',
            'شكّل كرات صغيرة وافردها على صينية',
            'اخبزها لـ15 دقيقة حتى تصبح ذهبية'
        ],
        stepsEn: [
            'Preheat oven to 180°C',
            'Mix mashed bananas with oats and cinnamon',
            'Add raisins and vanilla',
            'Form small balls and flatten on baking sheet',
            'Bake for 15 minutes until golden'
        ],
        tips: 'احفظها في علبة محكمة لمدة 5 أيام',
        tipsEn: 'Store in airtight container for 5 days'
    },
    {
        id: 20,
        category: 'حلويات صحية',
        categoryEn: 'Healthy Desserts',
        icon: '🍫',
        title: 'موس الشوكولاتة بالأفوكادو',
        titleEn: 'Avocado Chocolate Mousse',
        time: '10 دقائق + تبريد',
        timeEn: '10 minutes + cooling',
        servings: 4,
        calories: 180,
        nutrition: {
            protein: 3,
            carbs: 20,
            fat: 11,
            fiber: 5
        },
        ingredients: [
            'أفوكادو ناضج - حبتان',
            'مسحوق كاكاو - ربع كوب',
            'عسل طبيعي - 3 ملاعق كبيرة',
            'حليب لوز - نصف كوب',
            'فانيليا - ملعقة صغيرة',
            'رشة ملح'
        ],
        ingredientsEn: [
            'Ripe avocados - 2 pieces',
            'Cocoa powder - 1/4 cup',
            'Natural honey - 3 tbsp',
            'Almond milk - 1/2 cup',
            'Vanilla extract - 1 tsp',
            'Pinch of salt'
        ],
        steps: [
            'ضع جميع المكونات في الخلاط',
            'اخلط على سرعة عالية حتى يصبح ناعماً تماماً',
            'تذوّق واضبط الحلاوة حسب الرغبة',
            'وزّعه في أكواب صغيرة',
            'ضعه في الثلاجة لمدة ساعتين'
        ],
        stepsEn: [
            'Place all ingredients in blender',
            'Blend on high speed until completely smooth',
            'Taste and adjust sweetness as desired',
            'Divide into small cups',
            'Refrigerate for 2 hours'
        ],
        tips: 'زيّنه بالتوت الطازج أو رقائق جوز الهند',
        tipsEn: 'Garnish with fresh berries or coconut flakes'
    },

    // === Part 2: Recipes 21-35 ===
    {
        id: 21,
        category: 'فطور',
        categoryEn: 'Breakfast',
        icon: '🥐',
        title: 'توست فرنسي صحي',
        titleEn: 'Healthy French Toast',
        time: '15 دقيقة',
        timeEn: '15 minutes',
        servings: 2,
        calories: 260,
        nutrition: {
            protein: 12,
            carbs: 32,
            fat: 9,
            fiber: 4
        },
        ingredients: [
            '4 شرائح خبز أسمر',
            '2 بيضة',
            '¼ كوب حليب قليل الدسم',
            '1 ملعقة صغيرة قرفة',
            '½ ملعقة صغيرة فانيليا',
            '1 ملعقة صغيرة عسل',
            'توت للتزيين'
        ],
        ingredientsEn: [
            '4 slices whole wheat bread',
            '2 eggs',
            '¼ cup low-fat milk',
            '1 teaspoon cinnamon',
            '½ teaspoon vanilla',
            '1 teaspoon honey',
            'Berries for garnish'
        ],
        steps: [
            'اخفق البيض مع الحليب والقرفة والفانيليا',
            'اغمس شرائح الخبز في الخليط',
            'سخّن مقلاة غير لاصقة برذاذ زيت',
            'اقلِ الخبز حتى يتحمر من الجهتين',
            'قدّمه مع العسل والتوت'
        ],
        stepsEn: [
            'Whisk eggs with milk, cinnamon, and vanilla',
            'Dip bread slices into the mixture',
            'Heat non-stick skillet with oil spray',
            'Fry bread until golden on both sides',
            'Serve with honey and berries'
        ],
        tips: 'استخدم خبز أسمر للحصول على ألياف إضافية',
        tipsEn: 'Use whole wheat bread for extra fiber'
    },
    {
        id: 22,
        category: 'سلطات',
        categoryEn: 'Salads',
        icon: '🥗',
        title: 'سلطة الباستا بالخضار',
        titleEn: 'Vegetable Pasta Salad',
        time: '20 دقيقة',
        timeEn: '20 minutes',
        servings: 4,
        calories: 290,
        nutrition: {
            protein: 10,
            carbs: 48,
            fat: 8,
            fiber: 6
        },
        ingredients: [
            '2 كوب باستا حبوب كاملة',
            '1 كوب طماطم كرزية',
            '1 خيار مكعبات',
            '½ كوب زيتون أسود',
            '½ كوب جبن فيتا قليل الدسم',
            '¼ كوب بقدونس',
            '3 ملاعق كبيرة زيت زيتون',
            'عصير ليمونة',
            'ملح وفلفل'
        ],
        ingredientsEn: [
            '2 cups whole wheat pasta',
            '1 cup cherry tomatoes',
            '1 cucumber diced',
            '½ cup black olives',
            '½ cup low-fat feta cheese',
            '¼ cup parsley',
            '3 tablespoons olive oil',
            'Juice of 1 lemon',
            'Salt and pepper'
        ],
        steps: [
            'اسلق الباستا حسب التعليمات',
            'صفّي الباستا واتركها تبرد',
            'قطّع الطماطم إلى نصفين',
            'اخلط الباستا مع جميع الخضار',
            'حضّر الصوص من الزيت والليمون',
            'اسكب الصوص وقلّب',
            'أضف الجبن والبقدونس'
        ],
        stepsEn: [
            'Cook pasta according to instructions',
            'Drain pasta and let it cool',
            'Cut tomatoes in half',
            'Mix pasta with all vegetables',
            'Prepare dressing with oil and lemon',
            'Pour dressing and toss',
            'Add cheese and parsley'
        ],
        tips: 'سلطة مشبعة ومناسبة كوجبة كاملة',
        tipsEn: 'Filling salad perfect as a complete meal'
    },
    {
        id: 23,
        category: 'شوربات',
        categoryEn: 'Soups',
        icon: '🍲',
        title: 'شوربة الدجاج بالخضار',
        titleEn: 'Chicken and Vegetable Soup',
        time: '35 دقيقة',
        timeEn: '35 minutes',
        servings: 6,
        calories: 160,
        nutrition: {
            protein: 18,
            carbs: 12,
            fat: 5,
            fiber: 3
        },
        ingredients: [
            '300 جرام صدر دجاج',
            '2 جزر مقطع',
            '2 كوسة مقطعة',
            '1 بصلة',
            '2 فص ثوم',
            '6 أكواب مرق دجاج',
            '½ كوب شعيرية',
            'ملح وفلفل',
            'بقدونس'
        ],
        ingredientsEn: [
            '300g chicken breast',
            '2 carrots sliced',
            '2 zucchini sliced',
            '1 onion',
            '2 cloves garlic',
            '6 cups chicken broth',
            '½ cup noodles',
            'Salt and pepper',
            'Parsley'
        ],
        steps: [
            'اسلق الدجاج في المرق حتى ينضج',
            'أخرج الدجاج وقطّعه إلى قطع صغيرة',
            'صفِّ المرق وأعده للقدر',
            'أضف البصل والثوم والجزر',
            'اترك يغلي 10 دقائق',
            'أضف الكوسة والشعيرية',
            'اترك 10 دقائق حتى تنضج الشعيرية',
            'أضف الدجاج وتبّل',
            'قدّمها مع البقدونس'
        ],
        stepsEn: [
            'Boil chicken in broth until cooked',
            'Remove chicken and cut into small pieces',
            'Strain broth and return to pot',
            'Add onion, garlic, and carrots',
            'Let boil for 10 minutes',
            'Add zucchini and noodles',
            'Cook for 10 minutes until noodles are done',
            'Add chicken and season',
            'Serve with parsley'
        ],
        tips: 'شوربة دافئة ومغذية مثالية في الشتاء',
        tipsEn: 'Warm and nutritious soup perfect in winter'
    },
    {
        id: 24,
        category: 'أطباق رئيسية',
        categoryEn: 'Main Courses',
        icon: '🥩',
        title: 'ستيك اللحم المشوي',
        titleEn: 'Grilled Beef Steak',
        time: '20 دقيقة',
        timeEn: '20 minutes',
        servings: 2,
        calories: 380,
        nutrition: {
            protein: 45,
            carbs: 2,
            fat: 20,
            fiber: 0
        },
        ingredients: [
            '2 قطعة ستيك لحم (300 جرام)',
            '2 ملعقة كبيرة زيت زيتون',
            '3 فصوص ثوم',
            '1 ملعقة صغيرة روزماري',
            'ملح بحري وفلفل أسود خشن'
        ],
        ingredientsEn: [
            '2 beef steaks (300g)',
            '2 tablespoons olive oil',
            '3 cloves garlic',
            '1 teaspoon rosemary',
            'Sea salt and coarse black pepper'
        ],
        steps: [
            'أخرج اللحم من الثلاجة قبل 30 دقيقة',
            'تبّل اللحم بالملح والفلفل من الجهتين',
            'سخّن مقلاة ثقيلة على نار عالية',
            'أضف الزيت والثوم',
            'اشوِ اللحم 3-4 دقائق لكل جهة (medium)',
            'أضف الروزماري في الدقيقة الأخيرة',
            'اترك اللحم يرتاح 5 دقائق',
            'قطّعه وقدّمه مع خضار مشوية'
        ],
        stepsEn: [
            'Remove meat from fridge 30 minutes before',
            'Season meat with salt and pepper on both sides',
            'Heat heavy skillet over high heat',
            'Add oil and garlic',
            'Grill steak 3-4 minutes per side (medium)',
            'Add rosemary in the last minute',
            'Let meat rest for 5 minutes',
            'Slice and serve with grilled vegetables'
        ],
        tips: 'لا تقلب اللحم كثيراً للحصول على قشرة ذهبية',
        tipsEn: 'Don\'t flip meat too often for golden crust'
    },
    {
        id: 25,
        category: 'أطباق نباتية',
        categoryEn: 'Vegetarian Dishes',
        icon: '🌯',
        title: 'راب الخضار بالحمص',
        titleEn: 'Vegetable and Hummus Wrap',
        time: '15 دقيقة',
        timeEn: '15 minutes',
        servings: 2,
        calories: 320,
        nutrition: {
            protein: 12,
            carbs: 48,
            fat: 10,
            fiber: 10
        },
        ingredients: [
            '2 خبز تورتيلا أسمر',
            '1 كوب حمص مسلوق',
            '1 خيار شرائح',
            '1 طماطم شرائح',
            '½ كوب خس مقطع',
            '¼ كوب جزر مبشور',
            '2 ملعقة كبيرة طحينة',
            'عصير ليمونة'
        ],
        ingredientsEn: [
            '2 whole wheat tortillas',
            '1 cup cooked chickpeas',
            '1 cucumber sliced',
            '1 tomato sliced',
            '½ cup chopped lettuce',
            '¼ cup shredded carrots',
            '2 tablespoons tahini',
            'Juice of 1 lemon'
        ],
        steps: [
            'سخّن التورتيلا قليلاً',
            'اهرس الحمص مع الطحينة والليمون',
            'وزّع الحمص على التورتيلا',
            'رتّب الخضار فوق الحمص',
            'لف التورتيلا بإحكام',
            'قطّعه إلى نصفين وقدّمه'
        ],
        stepsEn: [
            'Warm the tortilla slightly',
            'Mash chickpeas with tahini and lemon',
            'Spread hummus on tortilla',
            'Arrange vegetables over hummus',
            'Wrap tortilla tightly',
            'Cut in half and serve'
        ],
        tips: 'وجبة سريعة ومتوازنة غذائياً',
        tipsEn: 'Quick and nutritionally balanced meal'
    },
    {
        id: 26,
        category: 'وجبات خفيفة',
        categoryEn: 'Snacks',
        icon: '🥤',
        title: 'عصير الفراولة الصحي',
        titleEn: 'Healthy Strawberry Juice',
        time: '5 دقائق',
        timeEn: '5 minutes',
        servings: 2,
        calories: 120,
        nutrition: {
            protein: 8,
            carbs: 22,
            fat: 1,
            fiber: 4
        },
        ingredients: [
            '1 كوب فراولة طازجة',
            '1 موزة',
            '1 كوب زبادي يوناني قليل الدسم',
            '½ كوب حليب لوز',
            '1 ملعقة صغيرة عسل',
            'مكعبات ثلج'
        ],
        ingredientsEn: [
            '1 cup fresh strawberries',
            '1 banana',
            '1 cup low-fat Greek yogurt',
            '½ cup almond milk',
            '1 teaspoon honey',
            'Ice cubes'
        ],
        steps: [
            'اغسل الفراولة وأزل الأوراق',
            'ضع جميع المكونات في الخلاط',
            'اخلط على سرعة عالية حتى يصبح ناعماً',
            'أضف ثلج إضافي إذا أردت قواماً أكثر برودة',
            'اسكبه في أكواب وقدّمه فوراً'
        ],
        stepsEn: [
            'Wash strawberries and remove leaves',
            'Place all ingredients in blender',
            'Blend on high speed until smooth',
            'Add extra ice if you want it colder',
            'Pour into cups and serve immediately'
        ],
        tips: 'غني بفيتامين C والبروتين',
        tipsEn: 'Rich in vitamin C and protein'
    },
    {
        id: 27,
        category: 'حلويات صحية',
        categoryEn: 'Healthy Desserts',
        icon: '🧁',
        title: 'مافن الشوكولاتة الصحي',
        titleEn: 'Healthy Chocolate Muffins',
        time: '30 دقيقة',
        timeEn: '30 minutes',
        servings: 12,
        calories: 140,
        nutrition: {
            protein: 5,
            carbs: 22,
            fat: 4,
            fiber: 3
        },
        ingredients: [
            '1½ كوب طحين شوفان',
            '½ كوب كاكاو خام',
            '2 بيضة',
            '½ كوب موز مهروس',
            '¼ كوب عسل',
            '½ كوب حليب لوز',
            '1 ملعقة صغيرة فانيليا',
            '1 ملعقة صغيرة بيكنج باودر',
            'رشة ملح'
        ],
        ingredientsEn: [
            '1½ cups oat flour',
            '½ cup raw cocoa',
            '2 eggs',
            '½ cup mashed banana',
            '¼ cup honey',
            '½ cup almond milk',
            '1 teaspoon vanilla',
            '1 teaspoon baking powder',
            'Pinch of salt'
        ],
        steps: [
            'سخّن الفرن على 180 درجة',
            'اخلط المكونات الجافة في وعاء',
            'اخفق البيض مع الموز والعسل والحليب والفانيليا',
            'أضف الخليط السائل للجاف وقلّب برفق',
            'وزّع الخليط في قوالب مافن',
            'اخبزها 18-20 دقيقة',
            'اتركها تبرد قبل التقديم'
        ],
        stepsEn: [
            'Preheat oven to 180°C',
            'Mix dry ingredients in a bowl',
            'Whisk eggs with banana, honey, milk, and vanilla',
            'Add liquid mixture to dry and stir gently',
            'Distribute mixture in muffin tins',
            'Bake for 18-20 minutes',
            'Let cool before serving'
        ],
        tips: 'حلى صحي خالي من السكر المكرر',
        tipsEn: 'Healthy dessert free from refined sugar'
    },
    {
        id: 28,
        category: 'فطور',
        categoryEn: 'Breakfast',
        icon: '🥛',
        title: 'بودنغ الشيا بالفانيليا',
        titleEn: 'Vanilla Chia Pudding',
        time: '5 دقائق + 4 ساعات',
        timeEn: '5 minutes + 4 hours',
        servings: 2,
        calories: 180,
        nutrition: {
            protein: 8,
            carbs: 20,
            fat: 8,
            fiber: 10
        },
        ingredients: [
            '4 ملاعق كبيرة بذور شيا',
            '1 كوب حليب لوز',
            '1 ملعقة صغيرة فانيليا',
            '1 ملعقة كبيرة عسل',
            'توت للتزيين',
            'رشة قرفة'
        ],
        ingredientsEn: [
            '4 tablespoons chia seeds',
            '1 cup almond milk',
            '1 teaspoon vanilla',
            '1 tablespoon honey',
            'Berries for garnish',
            'Pinch of cinnamon'
        ],
        steps: [
            'اخلط بذور الشيا مع الحليب والفانيليا والعسل',
            'قلّب جيداً حتى لا تتكتل البذور',
            'غطِّ الوعاء واحفظه في الثلاجة ليلة كاملة',
            'قلّب البودنغ في الصباح',
            'قدّمه مع التوت والقرفة'
        ],
        stepsEn: [
            'Mix chia seeds with milk, vanilla, and honey',
            'Stir well to prevent seed lumping',
            'Cover bowl and refrigerate overnight',
            'Stir pudding in the morning',
            'Serve with berries and cinnamon'
        ],
        tips: 'حضّره في الليلة السابقة لفطور سريع',
        tipsEn: 'Prepare the night before for quick breakfast'
    },
    {
        id: 29,
        category: 'سلطات',
        categoryEn: 'Salads',
        icon: '🥗',
        title: 'سلطة البنجر بالجوز',
        titleEn: 'Beetroot and Walnut Salad',
        time: '50 دقيقة',
        timeEn: '50 minutes',
        servings: 4,
        calories: 220,
        nutrition: {
            protein: 6,
            carbs: 28,
            fat: 10,
            fiber: 6
        },
        ingredients: [
            '3 حبات بنجر متوسطة',
            '2 كوب جرجير',
            '½ كوب جوز محمص',
            '¼ كوب جبن ماعز قليل الدسم',
            '2 ملعقة كبيرة زيت زيتون',
            '1 ملعقة كبيرة خل بلسميك',
            'ملح وفلفل'
        ],
        ingredientsEn: [
            '3 medium beets',
            '2 cups arugula',
            '½ cup roasted walnuts',
            '¼ cup low-fat goat cheese',
            '2 tablespoons olive oil',
            '1 tablespoon balsamic vinegar',
            'Salt and pepper'
        ],
        steps: [
            'اسلق البنجر حتى ينضج (40 دقيقة)',
            'قشّر البنجر وقطّعه إلى مكعبات',
            'رتّب الجرجير في طبق التقديم',
            'أضف البنجر والجوز',
            'اخلط الزيت مع الخل والملح والفلفل',
            'اسكب الصوص على السلطة',
            'فتّت الجبن على الوجه'
        ],
        stepsEn: [
            'Boil beets until cooked (40 minutes)',
            'Peel beets and cut into cubes',
            'Arrange arugula on serving plate',
            'Add beets and walnuts',
            'Mix oil with vinegar, salt, and pepper',
            'Pour dressing over salad',
            'Crumble cheese on top'
        ],
        tips: 'البنجر غني بالحديد ومضادات الأكسدة',
        tipsEn: 'Beets are rich in iron and antioxidants'
    },
    {
        id: 30,
        category: 'شوربات',
        categoryEn: 'Soups',
        icon: '🍲',
        title: 'شوربة البروكلي الكريمية',
        titleEn: 'Creamy Broccoli Soup',
        time: '30 دقيقة',
        timeEn: '30 minutes',
        servings: 4,
        calories: 140,
        nutrition: {
            protein: 8,
            carbs: 16,
            fat: 5,
            fiber: 5
        },
        ingredients: [
            '4 أكواب بروكلي',
            '1 بصلة مفرومة',
            '2 فص ثوم',
            '3 أكواب مرق خضار',
            '½ كوب حليب قليل الدسم',
            '2 ملعقة كبيرة دقيق شوفان',
            'ملح وفلفل',
            '1 ملعقة كبيرة زيت زيتون'
        ],
        ingredientsEn: [
            '4 cups broccoli',
            '1 onion chopped',
            '2 cloves garlic',
            '3 cups vegetable broth',
            '½ cup low-fat milk',
            '2 tablespoons oat flour',
            'Salt and pepper',
            '1 tablespoon olive oil'
        ],
        steps: [
            'سخّن الزيت وقلّب البصل والثوم',
            'أضف البروكلي وقلّب دقيقتين',
            'أضف المرق واترك يغلي',
            'خفّف النار واترك 15 دقيقة',
            'اخلط الشوربة بالخلاط الكهربائي',
            'أضف الحليب ودقيق الشوفان',
            'قلّب حتى تثخن قليلاً',
            'تبّل وقدّمها ساخنة'
        ],
        stepsEn: [
            'Heat oil and sauté onion and garlic',
            'Add broccoli and stir for 2 minutes',
            'Add broth and let boil',
            'Reduce heat and cook for 15 minutes',
            'Blend soup with immersion blender',
            'Add milk and oat flour',
            'Stir until slightly thickened',
            'Season and serve hot'
        ],
        tips: 'شوربة كريمية بدون كريمة ثقيلة',
        tipsEn: 'Creamy soup without heavy cream'
    },
    {
        id: 31,
        category: 'أطباق رئيسية',
        categoryEn: 'Main Courses',
        icon: '🍝',
        title: 'باستا بصوص الطماطم الطازج',
        titleEn: 'Pasta with Fresh Tomato Sauce',
        time: '25 دقيقة',
        timeEn: '25 minutes',
        servings: 4,
        calories: 340,
        nutrition: {
            protein: 14,
            carbs: 58,
            fat: 7,
            fiber: 8
        },
        ingredients: [
            '400 جرام باستا حبوب كاملة',
            '5 طماطم طازجة',
            '4 فصوص ثوم',
            '½ كوب ريحان طازج',
            '2 ملعقة كبيرة زيت زيتون',
            '¼ كوب جبن بارميزان',
            'ملح وفلفل',
            'رشة فلفل أحمر'
        ],
        ingredientsEn: [
            '400g whole wheat pasta',
            '5 fresh tomatoes',
            '4 cloves garlic',
            '½ cup fresh basil',
            '2 tablespoons olive oil',
            '¼ cup Parmesan cheese',
            'Salt and pepper',
            'Pinch of red pepper'
        ],
        steps: [
            'اسلق الباستا حسب التعليمات',
            'قطّع الطماطم إلى مكعبات صغيرة',
            'سخّن الزيت وقلّب الثوم',
            'أضف الطماطم واتركها تتسبّك 15 دقيقة',
            'تبّل بالملح والفلفل والفلفل الأحمر',
            'أضف الريحان المقطع',
            'صفِّ الباستا وأضفها للصوص',
            'قلّب جيداً وقدّمها مع الجبن'
        ],
        stepsEn: [
            'Cook pasta according to instructions',
            'Dice tomatoes into small pieces',
            'Heat oil and sauté garlic',
            'Add tomatoes and let simmer 15 minutes',
            'Season with salt, pepper, and red pepper',
            'Add chopped basil',
            'Drain pasta and add to sauce',
            'Toss well and serve with cheese'
        ],
        tips: 'صوص طماطم طازج أصح من المعلب',
        tipsEn: 'Fresh tomato sauce is healthier than canned'
    },
    {
        id: 32,
        category: 'أطباق نباتية',
        categoryEn: 'Vegetarian Dishes',
        icon: '🥙',
        title: 'بوريتو الفاصوليا السوداء',
        titleEn: 'Black Bean Burrito',
        time: '20 دقيقة',
        timeEn: '20 minutes',
        servings: 4,
        calories: 380,
        nutrition: {
            protein: 16,
            carbs: 58,
            fat: 10,
            fiber: 14
        },
        ingredients: [
            '4 خبز تورتيلا كبير',
            '2 كوب فاصوليا سوداء مسلوقة',
            '1 كوب أرز بني مطبوخ',
            '1 فلفل أحمر مقطع',
            '1 بصلة مقطعة',
            '½ كوب ذرة',
            '½ كوب صلصة طماطم',
            'كمون وبابريكا',
            'كزبرة خضراء'
        ],
        ingredientsEn: [
            '4 large tortillas',
            '2 cups cooked black beans',
            '1 cup cooked brown rice',
            '1 red bell pepper sliced',
            '1 onion sliced',
            '½ cup corn',
            '½ cup tomato sauce',
            'Cumin and paprika',
            'Fresh cilantro'
        ],
        steps: [
            'قلّب البصل والفلفل حتى يذبلا',
            'أضف الفاصوليا والذرة والبهارات',
            'اترك يتسبّك 10 دقائق',
            'سخّن التورتيلا قليلاً',
            'ضع الأرز في منتصف التورتيلا',
            'أضف خليط الفاصوليا',
            'رش الصلصة والكزبرة',
            'لف التورتيلا بإحكام وقدّمه'
        ],
        stepsEn: [
            'Sauté onion and pepper until softened',
            'Add beans, corn, and spices',
            'Let simmer for 10 minutes',
            'Warm tortillas slightly',
            'Place rice in center of tortilla',
            'Add bean mixture',
            'Drizzle sauce and cilantro',
            'Roll tortilla tightly and serve'
        ],
        tips: 'وجبة نباتية كاملة غنية بالبروتين',
        tipsEn: 'Complete vegetarian meal rich in protein'
    },
    {
        id: 33,
        category: 'وجبات خفيفة',
        categoryEn: 'Snacks',
        icon: '🍿',
        title: 'فشار صحي بالتوابل',
        titleEn: 'Healthy Spiced Popcorn',
        time: '10 دقائق',
        timeEn: '10 minutes',
        servings: 4,
        calories: 85,
        nutrition: {
            protein: 3,
            carbs: 17,
            fat: 1,
            fiber: 4
        },
        ingredients: [
            '½ كوب ذرة فشار',
            '1 ملعقة صغيرة زيت زيتون',
            '½ ملعقة صغيرة بابريكا',
            '¼ ملعقة صغيرة ثوم بودرة',
            'رشة ملح بحري'
        ],
        ingredientsEn: [
            '½ cup popcorn kernels',
            '1 teaspoon olive oil',
            '½ teaspoon paprika',
            '¼ teaspoon garlic powder',
            'Pinch of sea salt'
        ],
        steps: [
            'سخّن قدر كبير بغطاء',
            'أضف الزيت والذرة',
            'غطِّ القدر وهز بين الحين والآخر',
            'اترك حتى تنتهي الفرقعات',
            'انقل الفشار لوعاء',
            'رش التوابل وقلّب جيداً'
        ],
        stepsEn: [
            'Heat large pot with lid',
            'Add oil and kernels',
            'Cover pot and shake occasionally',
            'Let pop until sounds slow',
            'Transfer popcorn to bowl',
            'Sprinkle spices and toss well'
        ],
        tips: 'وجبة خفيفة قليلة السعرات وغنية بالألياف',
        tipsEn: 'Low-calorie snack rich in fiber'
    },
    {
        id: 34,
        category: 'حلويات صحية',
        categoryEn: 'Healthy Desserts',
        icon: '🍮',
        title: 'بودنغ الأرز بالحليب',
        titleEn: 'Rice Milk Pudding',
        time: '40 دقيقة',
        timeEn: '40 minutes',
        servings: 6,
        calories: 180,
        nutrition: {
            protein: 6,
            carbs: 32,
            fat: 3,
            fiber: 1
        },
        ingredients: [
            '1 كوب أرز قصير الحبة',
            '4 أكواب حليب قليل الدسم',
            '¼ كوب عسل',
            '1 ملعقة صغيرة فانيليا',
            '½ ملعقة صغيرة هيل',
            'قرفة ومكسرات للتزيين'
        ],
        ingredientsEn: [
            '1 cup short-grain rice',
            '4 cups low-fat milk',
            '¼ cup honey',
            '1 teaspoon vanilla',
            '½ teaspoon cardamom',
            'Cinnamon and nuts for garnish'
        ],
        steps: [
            'اغسل الأرز جيداً',
            'ضع الأرز والحليب في قدر',
            'اترك يغلي ثم خفّف النار',
            'قلّب كل 5 دقائق لمدة 30 دقيقة',
            'أضف العسل والفانيليا والهيل',
            'قلّب حتى يثخن القوام',
            'اسكبه في أكواب واتركه يبرد',
            'زيّنه بالقرفة والمكسرات'
        ],
        stepsEn: [
            'Rinse rice well',
            'Place rice and milk in pot',
            'Bring to boil then reduce heat',
            'Stir every 5 minutes for 30 minutes',
            'Add honey, vanilla, and cardamom',
            'Stir until thickened',
            'Pour into cups and let cool',
            'Garnish with cinnamon and nuts'
        ],
        tips: 'حلى تقليدي صحي ومغذي',
        tipsEn: 'Traditional healthy and nutritious dessert'
    },
    {
        id: 35,
        category: 'فطور',
        categoryEn: 'Breakfast',
        icon: '🍞',
        title: 'سندويش الديك الرومي',
        titleEn: 'Turkey Sandwich',
        time: '10 دقائق',
        timeEn: '10 minutes',
        servings: 1,
        calories: 290,
        nutrition: {
            protein: 28,
            carbs: 32,
            fat: 7,
            fiber: 6
        },
        ingredients: [
            'شريحتان خبز أسمر',
            '80 جرام ديك رومي مدخن',
            'شريحة جبن قليل الدسم',
            'خس وطماطم',
            '1 ملعقة صغيرة خردل',
            'خيار مخلل'
        ],
        ingredientsEn: [
            '2 slices whole wheat bread',
            '80g smoked turkey',
            '1 slice low-fat cheese',
            'Lettuce and tomato',
            '1 teaspoon mustard',
            'Pickle slices'
        ],
        steps: [
            'حمّص الخبز قليلاً',
            'ادهن الخردل على شريحة واحدة',
            'رتّب الديك الرومي والجبن',
            'أضف الخس والطماطم',
            'ضع المخلل',
            'غطِّ بالشريحة الثانية'
        ],
        stepsEn: [
            'Lightly toast bread',
            'Spread mustard on one slice',
            'Arrange turkey and cheese',
            'Add lettuce and tomato',
            'Add pickles',
            'Top with second slice'
        ],
        tips: 'فطور سريع غني بالبروتين',
        tipsEn: 'Quick breakfast rich in protein'
    }
];

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = recipesDatabase;
}
