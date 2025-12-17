// WiBo Health - Recipes Database (Part 1/5: Recipes 1-20)
// Bilingual (Arabic/English) Recipe Data

const recipesDatabase_Part1 = [
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
    }
];

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = recipesDatabase_Part1;
}
