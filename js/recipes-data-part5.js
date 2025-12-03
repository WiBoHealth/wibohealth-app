/**
 * WiBo Health - Recipes Database - Part 5
 * قاعدة بيانات الوصفات - الجزء الخامس (الوصفات 71-91)
 * Bilingual: Arabic & English
 * Total Recipes: 21 (IDs: 71-91)
 */

const recipesDatabase_Part5 = [
    // === الوصفات 71-91 ===
    {
        id: 71,
        category: 'أطباق رئيسية',
        categoryEn: 'Main Courses',
        icon: '🐟',
        title: 'سلمون مشوي بالليمون والشبت',
        titleEn: 'Grilled Salmon with Lemon and Dill',
        time: '25 دقيقة',
        timeEn: '25 minutes',
        servings: 4,
        calories: 295,
        nutrition: {
            protein: '34 جم',
            proteinEn: '34g',
            carbs: '2 جم',
            carbsEn: '2g',
            fat: '17 جم',
            fatEn: '17g',
            fiber: '0 جم',
            fiberEn: '0g'
        },
        ingredients: [
            '4 قطع سلمون (150 جرام لكل قطعة)',
            '2 ملعقة كبيرة زيت زيتون',
            'عصير ليمونتين',
            '3 ملعقة كبيرة شبت طازي',
            '2 فص ثوم مهروس',
            'ملح وفلفل أسود'
        ],
        ingredientsEn: [
            '4 salmon fillets (150g each)',
            '2 tablespoons olive oil',
            'Juice of 2 lemons',
            '3 tablespoons fresh dill',
            '2 cloves garlic minced',
            'Salt and black pepper'
        ],
        steps: [
            'سخّن الفرن على 200 درجة',
            'اخلط زيت الزيتون والليمون والثوم والشبت',
            'ضع السلمون في صينية',
            'ادهن السلمون بخليط الليمون',
            'تبّل بالملح والفلفل',
            'اشوِ في الفرن 12-15 دقيقة',
            'قدّمه مع الخضار المشوية'
        ],
        stepsEn: [
            'Preheat oven to 200°C',
            'Mix olive oil, lemon, garlic, and dill',
            'Place salmon in baking dish',
            'Brush salmon with lemon mixture',
            'Season with salt and pepper',
            'Bake in oven 12-15 minutes',
            'Serve with grilled vegetables'
        ],
        tips: 'غني بأوميغا-3 المفيدة لصحة القلب والدماغ',
        tipsEn: 'Rich in omega-3 beneficial for heart and brain health'
    },
    {
        id: 72,
        category: 'حلويات صحية',
        categoryEn: 'Healthy Desserts',
        icon: '🍫',
        title: 'براونيز الفاصوليا السوداء',
        titleEn: 'Black Bean Brownies',
        time: '35 دقيقة',
        timeEn: '35 minutes',
        servings: 12,
        calories: 130,
        nutrition: {
            protein: '5 جم',
            proteinEn: '5g',
            carbs: '18 جم',
            carbsEn: '18g',
            fat: '5 جم',
            fatEn: '5g',
            fiber: '4 جم',
            fiberEn: '4g'
        },
        ingredients: [
            '1.5 كوب فاصوليا سوداء مسلوقة ومصفاة',
            '3 بيضات',
            '⅓ كوب كاكاو خام',
            '¼ كوب عسل',
            '¼ كوب زيت جوز هند',
            '1 ملعقة صغيرة فانيليا',
            '½ ملعقة صغيرة بيكنج باودر',
            '¼ كوب شوكولاتة داكنة'
        ],
        ingredientsEn: [
            '1.5 cups cooked drained black beans',
            '3 eggs',
            '⅓ cup raw cocoa',
            '¼ cup honey',
            '¼ cup coconut oil',
            '1 teaspoon vanilla',
            '½ teaspoon baking powder',
            '¼ cup dark chocolate'
        ],
        steps: [
            'سخّن الفرن على 180 درجة',
            'اخلط الفاصوليا في الخلاط حتى تصبح ناعمة',
            'أضف البيض والعسل والزيت والفانيليا',
            'أضف الكاكاو والبيكنج باودر',
            'اخلط جيداً ثم أضف الشوكولاتة',
            'اسكب في صينية مدهونة',
            'اخبز 20-25 دقيقة'
        ],
        stepsEn: [
            'Preheat oven to 180°C',
            'Blend black beans until smooth',
            'Add eggs, honey, oil, and vanilla',
            'Add cocoa and baking powder',
            'Mix well then add chocolate',
            'Pour into oiled baking dish',
            'Bake 20-25 minutes'
        ],
        tips: 'حلوى غنية بالبروتين والألياف - لا أحد سيعرف أنها فاصوليا!',
        tipsEn: 'Rich in protein and fiber - no one will know it\'s beans!'
    },
    {
        id: 73,
        category: 'فطور',
        categoryEn: 'Breakfast',
        icon: '🥣',
        title: 'بودينغ الشيا بالفانيليا',
        titleEn: 'Vanilla Chia Pudding',
        time: '5 دقائق + نقع',
        timeEn: '5 minutes + soaking',
        servings: 2,
        calories: 185,
        nutrition: {
            protein: '6 جم',
            proteinEn: '6g',
            carbs: '20 جم',
            carbsEn: '20g',
            fat: '9 جم',
            fatEn: '9g',
            fiber: '10 جم',
            fiberEn: '10g'
        },
        ingredients: [
            '¼ كوب بذور شيا',
            '1 كوب حليب لوز',
            '1 ملعقة كبيرة عسل',
            '1 ملعقة صغيرة فانيليا',
            'توبينج: فواكه طازجة، مكسرات، جوز هند'
        ],
        ingredientsEn: [
            '¼ cup chia seeds',
            '1 cup almond milk',
            '1 tablespoon honey',
            '1 teaspoon vanilla',
            'Toppings: fresh fruits, nuts, coconut'
        ],
        steps: [
            'اخلط بذور الشيا والحليب',
            'أضف العسل والفانيليا',
            'قلّب جيداً',
            'غطّه واتركه في الثلاجة ليلة كاملة',
            'قلّب في الصباح',
            'أضف التوبينج المفضل'
        ],
        stepsEn: [
            'Mix chia seeds and milk',
            'Add honey and vanilla',
            'Stir well',
            'Cover and refrigerate overnight',
            'Stir in morning',
            'Add preferred toppings'
        ],
        tips: 'غني بالأوميغا-3 والألياف - جاهز من الليل',
        tipsEn: 'Rich in omega-3 and fiber - ready from night before'
    },
    {
        id: 74,
        category: 'سلطات',
        categoryEn: 'Salads',
        icon: '🥗',
        title: 'سلطة الحمص بالخضار المشوية',
        titleEn: 'Roasted Vegetable Chickpea Salad',
        time: '40 دقيقة',
        timeEn: '40 minutes',
        servings: 4,
        calories: 245,
        nutrition: {
            protein: '10 جم',
            proteinEn: '10g',
            carbs: '35 جم',
            carbsEn: '35g',
            fat: '8 جم',
            fatEn: '8g',
            fiber: '9 جم',
            fiberEn: '9g'
        },
        ingredients: [
            '1 كوب حمص حب مسلوق',
            '1 باذنجان مقطع',
            '2 فلفل ألوان',
            '1 كوسا',
            '2 طماطم',
            '3 ملاعق كبيرة زيت زيتون',
            'عصير ليمونة',
            '1 ملعقة صغيرة كمون',
            'بقدونس وملح'
        ],
        ingredientsEn: [
            '1 cup cooked chickpeas',
            '1 eggplant chopped',
            '2 colored bell peppers',
            '1 zucchini',
            '2 tomatoes',
            '3 tablespoons olive oil',
            'Juice of 1 lemon',
            '1 teaspoon cumin',
            'Parsley and salt'
        ],
        steps: [
            'قطّع الخضار قطع متوسطة',
            'ادهن الخضار بزيت الزيتون والكمون',
            'اشوِ الخضار في فرن 200 درجة 25 دقيقة',
            'اخلط الحمص مع الخضار المشوية',
            'أضف عصير الليمون',
            'زيّن بالبقدونس'
        ],
        stepsEn: [
            'Chop vegetables into medium pieces',
            'Coat vegetables with olive oil and cumin',
            'Roast at 200°C for 25 minutes',
            'Mix chickpeas with roasted vegetables',
            'Add lemon juice',
            'Garnish with parsley'
        ],
        tips: 'غنية بالبروتين النباتي والألياف',
        tipsEn: 'Rich in plant protein and fiber'
    },
    {
        id: 75,
        category: 'أطباق رئيسية',
        categoryEn: 'Main Courses',
        icon: '🥙',
        title: 'دجاج تندوري بالزبادي',
        titleEn: 'Tandoori Chicken with Yogurt',
        time: '2 ساعة + 30 دقيقة طبخ',
        timeEn: '2 hours + 30 minutes cooking',
        servings: 6,
        calories: 265,
        nutrition: {
            protein: '38 جم',
            proteinEn: '38g',
            carbs: '8 جم',
            carbsEn: '8g',
            fat: '10 جم',
            fatEn: '10g',
            fiber: '1 جم',
            fiberEn: '1g'
        },
        ingredients: [
            '1 كيلو صدور دجاج',
            '1 كوب زبادي يوناني',
            '3 ملعقة كبيرة عصير ليمون',
            '2 ملعقة كبيرة بابريكا',
            '1 ملعقة كبيرة كمون',
            '1 ملعقة كبيرة كركم',
            '1 ملعقة صغيرة زنجبيل',
            '4 فصوص ثوم',
            'ملح وفلفل حار'
        ],
        ingredientsEn: [
            '1kg chicken breasts',
            '1 cup Greek yogurt',
            '3 tablespoons lemon juice',
            '2 tablespoons paprika',
            '1 tablespoon cumin',
            '1 tablespoon turmeric',
            '1 teaspoon ginger',
            '4 cloves garlic',
            'Salt and hot pepper'
        ],
        steps: [
            'اخلط الزبادي مع جميع البهارات والليمون',
            'قطّع الدجاج قطع متوسطة',
            'اغمر الدجاج في خليط الزبادي',
            'غطّه واتركه في الثلاجة ساعتين',
            'سخّن الفرن على 220 درجة',
            'رتّب الدجاج في صينية',
            'اشوِ 25-30 دقيقة حتى ينضج',
            'قدّمه مع الأرز والسلطة'
        ],
        stepsEn: [
            'Mix yogurt with all spices and lemon',
            'Cut chicken into medium pieces',
            'Marinate chicken in yogurt mixture',
            'Cover and refrigerate 2 hours',
            'Preheat oven to 220°C',
            'Arrange chicken in baking dish',
            'Bake 25-30 minutes until cooked',
            'Serve with rice and salad'
        ],
        tips: 'طبق هندي صحي وعالي البروتين',
        tipsEn: 'Healthy Indian dish high in protein'
    },
    {
        id: 76,
        category: 'وجبات خفيفة',
        categoryEn: 'Snacks',
        icon: '🥕',
        title: 'هيومس الشمندر',
        titleEn: 'Beetroot Hummus',
        time: '15 دقيقة',
        timeEn: '15 minutes',
        servings: 8,
        calories: 95,
        nutrition: {
            protein: '4 جم',
            proteinEn: '4g',
            carbs: '12 جم',
            carbsEn: '12g',
            fat: '4 جم',
            fatEn: '4g',
            fiber: '3 جم',
            fiberEn: '3g'
        },
        ingredients: [
            '1 كوب حمص حب مسلوق',
            '1 شمندر متوسط مسلوق',
            '2 ملعقة كبيرة طحينة',
            '2 فص ثوم',
            'عصير ليمونة',
            '2 ملعقة كبيرة زيت زيتون',
            '½ ملعقة صغيرة كمون',
            'ملح'
        ],
        ingredientsEn: [
            '1 cup cooked chickpeas',
            '1 medium cooked beetroot',
            '2 tablespoons tahini',
            '2 cloves garlic',
            'Juice of 1 lemon',
            '2 tablespoons olive oil',
            '½ teaspoon cumin',
            'Salt'
        ],
        steps: [
            'ضع جميع المكونات في الخلاط',
            'اخلط حتى يصبح القوام ناعماً',
            'أضف ماء إذا كان سميكاً جداً',
            'تذوق وعدّل الملح',
            'اسكب في طبق التقديم',
            'زيّن بزيت الزيتون والسمسم',
            'قدّمه مع الخضار أو الخبز'
        ],
        stepsEn: [
            'Place all ingredients in blender',
            'Blend until smooth',
            'Add water if too thick',
            'Taste and adjust salt',
            'Pour into serving bowl',
            'Garnish with olive oil and sesame',
            'Serve with vegetables or bread'
        ],
        tips: 'لونه وردي جميل وغني بمضادات الأكسدة',
        tipsEn: 'Beautiful pink color and rich in antioxidants'
    },
    {
        id: 77,
        category: 'شوربات',
        categoryEn: 'Soups',
        icon: '🍲',
        title: 'شوربة الطماطم المشوية',
        titleEn: 'Roasted Tomato Soup',
        time: '55 دقيقة',
        timeEn: '55 minutes',
        servings: 6,
        calories: 125,
        nutrition: {
            protein: '3 جم',
            proteinEn: '3g',
            carbs: '18 جم',
            carbsEn: '18g',
            fat: '5 جم',
            fatEn: '5g',
            fiber: '4 جم',
            fiberEn: '4g'
        },
        ingredients: [
            '1 كيلو طماطم',
            '1 بصلة كبيرة',
            '4 فصوص ثوم',
            '3 أكواب مرق خضار',
            '¼ كوب ريحان طازج',
            '2 ملعقة كبيرة زيت زيتون',
            '1 ملعقة صغيرة عسل',
            'ملح وفلفل'
        ],
        ingredientsEn: [
            '1kg tomatoes',
            '1 large onion',
            '4 cloves garlic',
            '3 cups vegetable broth',
            '¼ cup fresh basil',
            '2 tablespoons olive oil',
            '1 teaspoon honey',
            'Salt and pepper'
        ],
        steps: [
            'قطّع الطماطم والبصل نصفين',
            'ضع الخضار في صينية مع الثوم',
            'ادهن بزيت الزيتون',
            'اشوِ في فرن 200 درجة 30 دقيقة',
            'انقل الخضار المشوية لقدر',
            'أضف المرق والريحان',
            'اخلط حتى يصبح ناعماً',
            'أضف العسل وسخّن'
        ],
        stepsEn: [
            'Cut tomatoes and onion in half',
            'Place vegetables in baking dish with garlic',
            'Drizzle with olive oil',
            'Roast at 200°C for 30 minutes',
            'Transfer roasted vegetables to pot',
            'Add broth and basil',
            'Blend until smooth',
            'Add honey and heat'
        ],
        tips: 'الشوي يعزز النكهة والحلاوة الطبيعية',
        tipsEn: 'Roasting enhances flavor and natural sweetness'
    },
    {
        id: 78,
        category: 'حلويات صحية',
        categoryEn: 'Healthy Desserts',
        icon: '🍮',
        title: 'كاسترد البروتين',
        titleEn: 'Protein Custard',
        time: '15 دقيقة + تبريد',
        timeEn: '15 minutes + chilling',
        servings: 4,
        calories: 140,
        nutrition: {
            protein: '15 جم',
            proteinEn: '15g',
            carbs: '12 جم',
            carbsEn: '12g',
            fat: '3 جم',
            fatEn: '3g',
            fiber: '1 جم',
            fiberEn: '1g'
        },
        ingredients: [
            '2 كوب حليب خالي الدسم',
            '1 سكوب واي بروتين فانيليا',
            '2 ملعقة كبيرة نشا الذرة',
            '2 ملعقة كبيرة عسل',
            '1 ملعقة صغيرة فانيليا',
            'رشة ملح'
        ],
        ingredientsEn: [
            '2 cups skim milk',
            '1 scoop vanilla whey protein',
            '2 tablespoons cornstarch',
            '2 tablespoons honey',
            '1 teaspoon vanilla',
            'Pinch of salt'
        ],
        steps: [
            'اخلط النشا مع ربع كوب حليب بارد',
            'سخّن باقي الحليب في قدر',
            'أضف العسل والفانيليا',
            'أضف خليط النشا وقلّب باستمرار',
            'عندما يصبح سميكاً، ارفعه عن النار',
            'أضف البروتين وقلّب جيداً',
            'اسكب في أكواب وبرّده'
        ],
        stepsEn: [
            'Mix cornstarch with ¼ cup cold milk',
            'Heat remaining milk in pot',
            'Add honey and vanilla',
            'Add cornstarch mixture and stir constantly',
            'When thickened, remove from heat',
            'Add protein and stir well',
            'Pour into cups and chill'
        ],
        tips: 'حلوى غنية بالبروتين ومنخفضة السعرات',
        tipsEn: 'High protein dessert low in calories'
    },
    {
        id: 79,
        category: 'فطور',
        categoryEn: 'Breakfast',
        icon: '🥖',
        title: 'خبز الموز بالشوفان',
        titleEn: 'Banana Oat Bread',
        time: '60 دقيقة',
        timeEn: '60 minutes',
        servings: 10,
        calories: 165,
        nutrition: {
            protein: '5 جم',
            proteinEn: '5g',
            carbs: '28 جم',
            carbsEn: '28g',
            fat: '4 جم',
            fatEn: '4g',
            fiber: '3 جم',
            fiberEn: '3g'
        },
        ingredients: [
            '3 حبات موز ناضج مهروس',
            '2 بيضة',
            '¼ كوب عسل',
            '1.5 كوب شوفان مطحون',
            '1 ملعقة صغيرة بيكنج صودا',
            '1 ملعقة صغيرة قرفة',
            '¼ كوب حليب',
            '¼ كوب جوز مفروم',
            'رشة ملح'
        ],
        ingredientsEn: [
            '3 ripe bananas mashed',
            '2 eggs',
            '¼ cup honey',
            '1.5 cups ground oats',
            '1 teaspoon baking soda',
            '1 teaspoon cinnamon',
            '¼ cup milk',
            '¼ cup chopped walnuts',
            'Pinch of salt'
        ],
        steps: [
            'سخّن الفرن على 180 درجة',
            'اهرس الموز جيداً',
            'اخلط البيض والعسل مع الموز',
            'أضف الشوفان والبيكنج صودا والقرفة',
            'أضف الحليب حتى يصبح القوام مناسباً',
            'أضف الجوز',
            'اسكب في قالب خبز مدهون',
            'اخبز 45-50 دقيقة'
        ],
        stepsEn: [
            'Preheat oven to 180°C',
            'Mash banana well',
            'Mix eggs and honey with banana',
            'Add oats, baking soda, and cinnamon',
            'Add milk for appropriate consistency',
            'Add walnuts',
            'Pour into oiled loaf pan',
            'Bake 45-50 minutes'
        ],
        tips: 'بديل صحي للخبز التقليدي - بدون طحين أبيض',
        tipsEn: 'Healthy alternative to traditional bread - no white flour'
    },
    {
        id: 80,
        category: 'أطباق رئيسية',
        categoryEn: 'Main Courses',
        icon: '🍛',
        title: 'كاري الحمص بحليب جوز الهند',
        titleEn: 'Chickpea Curry with Coconut Milk',
        time: '35 دقيقة',
        timeEn: '35 minutes',
        servings: 5,
        calories: 285,
        nutrition: {
            protein: '11 جم',
            proteinEn: '11g',
            carbs: '38 جم',
            carbsEn: '38g',
            fat: '11 جم',
            fatEn: '11g',
            fiber: '10 جم',
            fiberEn: '10g'
        },
        ingredients: [
            '2 كوب حمص حب مسلوق',
            '1 علبة حليب جوز هند (400 مل)',
            '1 بصلة مفرومة',
            '3 فصوص ثوم',
            '1 ملعقة كبيرة زنجبيل طازج',
            '2 ملعقة كبيرة كاري بودر',
            '1 ملعقة صغيرة كمون',
            '2 طماطم مقطعة',
            '1 كوب سبانخ',
            'ملح وكزبرة طازجة'
        ],
        ingredientsEn: [
            '2 cups cooked chickpeas',
            '1 can coconut milk (400ml)',
            '1 onion chopped',
            '3 cloves garlic',
            '1 tablespoon fresh ginger',
            '2 tablespoons curry powder',
            '1 teaspoon cumin',
            '2 tomatoes chopped',
            '1 cup spinach',
            'Salt and fresh cilantro'
        ],
        steps: [
            'قلّب البصل والثوم والزنجبيل',
            'أضف الكاري والكمون وقلّب',
            'أضف الطماطم واطبخ 5 دقائق',
            'أضف الحمص وحليب جوز الهند',
            'اتركه يغلي ثم خفّف الحرارة',
            'اطبخ 15 دقيقة',
            'أضف السبانخ قبل التقديم',
            'زيّن بالكزبرة'
        ],
        stepsEn: [
            'Sauté onion, garlic, and ginger',
            'Add curry and cumin and stir',
            'Add tomatoes and cook 5 minutes',
            'Add chickpeas and coconut milk',
            'Bring to boil then reduce heat',
            'Cook 15 minutes',
            'Add spinach before serving',
            'Garnish with cilantro'
        ],
        tips: 'غني بالبروتين النباتي ونكهته رائعة',
        tipsEn: 'Rich in plant protein with great flavor'
    },
    {
        id: 81,
        category: 'وجبات خفيفة/دايت',
        categoryEn: 'Snacks/Diet',
        icon: '🥗',
        title: 'سلطة التونة بالأفوكادو (خالية من المايونيز)',
        titleEn: 'Tuna Avocado Salad (Mayonnaise-Free)',
        time: '10 دقائق',
        timeEn: '10 minutes',
        servings: 2,
        calories: 220,
        nutrition: {
            protein: '25 جم',
            proteinEn: '25g',
            carbs: '8 جم',
            carbsEn: '8g',
            fat: '11 جم',
            fatEn: '11g',
            fiber: '5 جم',
            fiberEn: '5g'
        },
        ingredients: [
            '1 علبة تونة بالماء مصفاة',
            '½ حبة أفوكادو ناضجة',
            '2 كوب خس مقطع',
            '½ كوب خيار مكعبات',
            '¼ كوب طماطم كرزية',
            'عصير نصف ليمونة',
            '1 ملعقة صغيرة زيت زيتون',
            'ملح وفلفل أسود'
        ],
        ingredientsEn: [
            '1 can tuna in water drained',
            '½ ripe avocado',
            '2 cups chopped lettuce',
            '½ cup diced cucumber',
            '¼ cup cherry tomatoes',
            'Juice of ½ lemon',
            '1 teaspoon olive oil',
            'Salt and black pepper'
        ],
        steps: [
            'اهرس الأفوكادو بالشوكة',
            'اخلط التونة مع الأفوكادو',
            'أضف عصير الليمون والملح والفلفل',
            'رتّب الخس في طبق التقديم',
            'ضع خليط التونة فوق الخس',
            'أضف الخيار والطماطم',
            'رش زيت الزيتون'
        ],
        stepsEn: [
            'Mash avocado with fork',
            'Mix tuna with avocado',
            'Add lemon juice, salt, and pepper',
            'Arrange lettuce on serving plate',
            'Place tuna mixture on lettuce',
            'Add cucumber and tomatoes',
            'Drizzle olive oil'
        ],
        tips: 'وجبة دايت غنية بالبروتين وأوميغا-3 - بدون مايونيز',
        tipsEn: 'Diet meal rich in protein and omega-3 - no mayo'
    },
    {
        id: 82,
        category: 'وجبات خفيفة/دايت',
        categoryEn: 'Snacks/Diet',
        icon: '🍗',
        title: 'دجاج مشوي بالليمون والثوم (قليل الدهون)',
        titleEn: 'Lemon Garlic Grilled Chicken (Low Fat)',
        time: '30 دقيقة',
        timeEn: '30 minutes',
        servings: 4,
        calories: 165,
        nutrition: {
            protein: '32 جم',
            proteinEn: '32g',
            carbs: '3 جم',
            carbsEn: '3g',
            fat: '3 جم',
            fatEn: '3g',
            fiber: '0 جم',
            fiberEn: '0g'
        },
        ingredients: [
            '4 صدور دجاج منزوعة الجلد',
            'عصير ليمونتين',
            '5 فصوص ثوم مهروس',
            '1 ملعقة كبيرة خل أبيض',
            '1 ملعقة صغيرة بابريكا',
            '1 ملعقة صغيرة كمون',
            'رشة فلفل حار',
            'ملح وفلفل'
        ],
        ingredientsEn: [
            '4 skinless chicken breasts',
            'Juice of 2 lemons',
            '5 cloves garlic minced',
            '1 tablespoon white vinegar',
            '1 teaspoon paprika',
            '1 teaspoon cumin',
            'Pinch of hot pepper',
            'Salt and pepper'
        ],
        steps: [
            'اخلط الليمون والثوم والخل والبهارات',
            'اغمر الدجاج في التتبيلة',
            'اتركه 20 دقيقة في الثلاجة',
            'سخّن مقلاة شواء أو فرن',
            'اشوِ الدجاج 6 دقائق لكل جهة',
            'تأكد من النضج التام',
            'قطّعه وقدّمه مع السلطة'
        ],
        stepsEn: [
            'Mix lemon, garlic, vinegar, and spices',
            'Marinate chicken in mixture',
            'Refrigerate 20 minutes',
            'Heat grill or oven',
            'Grill chicken 6 minutes per side',
            'Ensure fully cooked',
            'Slice and serve with salad'
        ],
        tips: 'عالي البروتين جداً وقليل الدهون - مثالي للتنشيف',
        tipsEn: 'Very high protein low fat - perfect for cutting'
    },
    {
        id: 83,
        category: 'وجبات خفيفة/دايت',
        categoryEn: 'Snacks/Diet',
        icon: '🥣',
        title: 'شوربة الخضار حارقة الدهون',
        titleEn: 'Fat-Burning Vegetable Soup',
        time: '35 دقيقة',
        timeEn: '35 minutes',
        servings: 6,
        calories: 65,
        nutrition: {
            protein: '3 جم',
            proteinEn: '3g',
            carbs: '14 جم',
            carbsEn: '14g',
            fat: '0.5 جم',
            fatEn: '0.5g',
            fiber: '4 جم',
            fiberEn: '4g'
        },
        ingredients: [
            '2 كوب كرنب مقطع',
            '2 جزر مقطع',
            '2 كوسا مقطعة',
            '1 بصلة كبيرة',
            '2 طماطم مقطعة',
            '1 فلفل أخضر',
            '3 فصوص ثوم',
            '6 أكواب مرق خضار قليل الصوديوم',
            'ملح وفلفل وكمون'
        ],
        ingredientsEn: [
            '2 cups chopped cabbage',
            '2 carrots chopped',
            '2 zucchini chopped',
            '1 large onion',
            '2 tomatoes chopped',
            '1 green bell pepper',
            '3 cloves garlic',
            '6 cups low-sodium vegetable broth',
            'Salt, pepper, and cumin'
        ],
        steps: [
            'قطّع جميع الخضروات قطع متوسطة',
            'ضع المرق في قدر كبير',
            'أضف جميع الخضروات',
            'أضف البهارات',
            'اتركه يغلي ثم خفّف الحرارة',
            'اطبخ 25 دقيقة حتى تنضج الخضار',
            'قدّمها ساخنة'
        ],
        stepsEn: [
            'Chop all vegetables into medium pieces',
            'Place broth in large pot',
            'Add all vegetables',
            'Add spices',
            'Bring to boil then reduce heat',
            'Cook 25 minutes until vegetables soften',
            'Serve hot'
        ],
        tips: 'منخفضة السعرات جداً - يمكن تناولها بكميات كبيرة أثناء الدايت',
        tipsEn: 'Very low calorie - can eat large portions during diet'
    },
    {
        id: 84,
        category: 'وجبات خفيفة/دايت',
        categoryEn: 'Snacks/Diet',
        icon: '🍳',
        title: 'أومليت بياض البيض بالخضار',
        titleEn: 'Egg White Vegetable Omelet',
        time: '15 دقيقة',
        timeEn: '15 minutes',
        servings: 1,
        calories: 135,
        nutrition: {
            protein: '20 جم',
            proteinEn: '20g',
            carbs: '6 جم',
            carbsEn: '6g',
            fat: '3 جم',
            fatEn: '3g',
            fiber: '2 جم',
            fiberEn: '2g'
        },
        ingredients: [
            '5 بياض بيض',
            '½ كوب سبانخ طازجة',
            '¼ كوب طماطم مكعبات',
            '¼ كوب فلفل ألوان',
            '2 ملعقة كبيرة بصل أخضر',
            'رشة ملح وفلفل أسود',
            'بخاخ طبخ (بدون دهون)'
        ],
        ingredientsEn: [
            '5 egg whites',
            '½ cup fresh spinach',
            '¼ cup diced tomato',
            '¼ cup colored peppers',
            '2 tablespoons green onion',
            'Pinch of salt and black pepper',
            'Cooking spray (no fat)'
        ],
        steps: [
            'اخفق بياض البيض مع الملح والفلفل',
            'رش المقلاة ببخاخ الطبخ',
            'قلّب الخضار دقيقتين',
            'اسكب بياض البيض فوق الخضار',
            'اطبخ حتى ينضج من الأسفل',
            'اطوِ الأومليت نصفين',
            'قدّمه فوراً'
        ],
        stepsEn: [
            'Whisk egg whites with salt and pepper',
            'Spray skillet with cooking spray',
            'Sauté vegetables 2 minutes',
            'Pour egg whites over vegetables',
            'Cook until set on bottom',
            'Fold omelet in half',
            'Serve immediately'
        ],
        tips: 'عالي البروتين وخالي تقريباً من الدهون - إفطار مثالي للدايت',
        tipsEn: 'High protein almost fat-free - perfect diet breakfast'
    },
    {
        id: 85,
        category: 'وجبات خفيفة/دايت',
        categoryEn: 'Snacks/Diet',
        icon: '🐟',
        title: 'سمك فيليه بالفرن مع البروكلي',
        titleEn: 'Baked Fish Fillet with Broccoli',
        time: '25 دقيقة',
        timeEn: '25 minutes',
        servings: 2,
        calories: 195,
        nutrition: {
            protein: '28 جم',
            proteinEn: '28g',
            carbs: '8 جم',
            carbsEn: '8g',
            fat: '6 جم',
            fatEn: '6g',
            fiber: '3 جم',
            fiberEn: '3g'
        },
        ingredients: [
            '2 فيليه سمك أبيض (250 جرام)',
            '2 كوب بروكلي',
            'عصير ليمونة',
            '2 فص ثوم مهروس',
            '1 ملعقة صغيرة زيت زيتون',
            '½ ملعقة صغيرة شبت جاف',
            'ملح وفلفل'
        ],
        ingredientsEn: [
            '2 white fish fillets (250g)',
            '2 cups broccoli',
            'Juice of 1 lemon',
            '2 cloves garlic minced',
            '1 teaspoon olive oil',
            '½ teaspoon dry dill',
            'Salt and pepper'
        ],
        steps: [
            'سخّن الفرن على 190 درجة',
            'ضع السمك والبروكلي في صينية',
            'اخلط الليمون والثوم والزيت',
            'ادهن السمك والبروكلي بالخليط',
            'تبّل بالملح والفلفل والشبت',
            'اخبز 15-18 دقيقة',
            'قدّمه ساخناً'
        ],
        stepsEn: [
            'Preheat oven to 190°C',
            'Place fish and broccoli in baking dish',
            'Mix lemon, garlic, and oil',
            'Brush fish and broccoli with mixture',
            'Season with salt, pepper, and dill',
            'Bake 15-18 minutes',
            'Serve hot'
        ],
        tips: 'وجبة كاملة منخفضة السعرات وغنية بالبروتين',
        tipsEn: 'Complete meal low calories and high protein'
    },
    {
        id: 86,
        category: 'وجبات خفيفة/دايت',
        categoryEn: 'Snacks/Diet',
        icon: '🥙',
        title: 'راب الدجاج بخبز التورتيلا قليل السعرات',
        titleEn: 'Low-Calorie Chicken Wrap',
        time: '15 دقيقة',
        timeEn: '15 minutes',
        servings: 2,
        calories: 240,
        nutrition: {
            protein: '26 جم',
            proteinEn: '26g',
            carbs: '24 جم',
            carbsEn: '24g',
            fat: '5 جم',
            fatEn: '5g',
            fiber: '4 جم',
            fiberEn: '4g'
        },
        ingredients: [
            '2 خبز تورتيلا قمح كامل صغير',
            '200 جرام صدور دجاج مشوية مقطعة',
            '1 كوب خس مقطع رفيع',
            '½ كوب طماطم مكعبات',
            '¼ كوب خيار مخلل',
            '2 ملعقة كبيرة زبادي يوناني',
            '1 ملعقة صغيرة خردل',
            'ملح وفلفل'
        ],
        ingredientsEn: [
            '2 whole wheat small tortillas',
            '200g grilled chicken breast sliced',
            '1 cup thinly sliced lettuce',
            '½ cup diced tomato',
            '¼ cup pickled cucumber',
            '2 tablespoons Greek yogurt',
            '1 teaspoon mustard',
            'Salt and pepper'
        ],
        steps: [
            'اخلط الزبادي مع الخردل',
            'سخّن التورتيلا قليلاً',
            'ادهن التورتيلا بصوص الزبادي',
            'رتّب الخس والطماطم',
            'أضف الدجاج المشوي',
            'أضف الخيار المخلل',
            'لفّه بإحكام وقدّمه'
        ],
        stepsEn: [
            'Mix yogurt with mustard',
            'Warm tortilla slightly',
            'Spread yogurt sauce on tortilla',
            'Arrange lettuce and tomato',
            'Add grilled chicken',
            'Add pickled cucumber',
            'Roll tightly and serve'
        ],
        tips: 'وجبة خفيفة ومشبعة - مثالية للغداء أثناء الدايت',
        tipsEn: 'Light filling meal - perfect lunch during diet'
    },
    {
        id: 87,
        category: 'وجبات خفيفة/دايت',
        categoryEn: 'Snacks/Diet',
        icon: '🥗',
        title: 'سلطة الكرنب الملونة (كول سلو صحي)',
        titleEn: 'Colorful Cabbage Salad (Healthy Coleslaw)',
        time: '15 دقيقة',
        timeEn: '15 minutes',
        servings: 4,
        calories: 85,
        nutrition: {
            protein: '2 جم',
            proteinEn: '2g',
            carbs: '12 جم',
            carbsEn: '12g',
            fat: '3 جم',
            fatEn: '3g',
            fiber: '4 جم',
            fiberEn: '4g'
        },
        ingredients: [
            '2 كوب كرنب أبيض مقطع رفيع',
            '1 كوب كرنب أحمر مقطع رفيع',
            '1 جزرة كبيرة مبشورة',
            '¼ كوب زبادي يوناني خالي الدسم',
            '1 ملعقة كبيرة خل تفاح',
            '1 ملعقة صغيرة عسل',
            '½ ملعقة صغيرة خردل',
            'ملح وفلفل'
        ],
        ingredientsEn: [
            '2 cups thinly sliced white cabbage',
            '1 cup thinly sliced red cabbage',
            '1 large shredded carrot',
            '¼ cup fat-free Greek yogurt',
            '1 tablespoon apple cider vinegar',
            '1 teaspoon honey',
            '½ teaspoon mustard',
            'Salt and pepper'
        ],
        steps: [
            'اخلط الكرنب الأبيض والأحمر والجزر',
            'في وعاء منفصل، اخلط الزبادي والخل والعسل والخردل',
            'اسكب الصوص على الخضار',
            'قلّب جيداً',
            'اتركه في الثلاجة 10 دقائق',
            'قدّمه بارداً'
        ],
        stepsEn: [
            'Mix white and red cabbage with carrot',
            'In separate bowl, mix yogurt, vinegar, honey, and mustard',
            'Pour sauce over vegetables',
            'Mix well',
            'Refrigerate 10 minutes',
            'Serve cold'
        ],
        tips: 'بديل صحي للكول سلو التقليدي - بدون مايونيز',
        tipsEn: 'Healthy coleslaw alternative - no mayonnaise'
    },
    {
        id: 88,
        category: 'وجبات خفيفة/دايت',
        categoryEn: 'Snacks/Diet',
        icon: '🍲',
        title: 'يخنة الدجاج بالكوسا (قليلة الكربوهيدرات)',
        titleEn: 'Chicken Zucchini Stew (Low Carb)',
        time: '40 دقيقة',
        timeEn: '40 minutes',
        servings: 4,
        calories: 185,
        nutrition: {
            protein: '24 جم',
            proteinEn: '24g',
            carbs: '10 جم',
            carbsEn: '10g',
            fat: '6 جم',
            fatEn: '6g',
            fiber: '3 جم',
            fiberEn: '3g'
        },
        ingredients: [
            '500 جرام صدور دجاج مقطعة',
            '3 حبات كوسا متوسطة',
            '2 طماطم مقطعة',
            '1 بصلة مفرومة',
            '3 فصوص ثوم',
            '2 كوب مرق دجاج قليل الدهون',
            '1 ملعقة صغيرة كمون',
            'ملح وفلفل'
        ],
        ingredientsEn: [
            '500g chicken breast chopped',
            '3 medium zucchini',
            '2 tomatoes chopped',
            '1 onion chopped',
            '3 cloves garlic',
            '2 cups low-fat chicken broth',
            '1 teaspoon cumin',
            'Salt and pepper'
        ],
        steps: [
            'قلّب البصل والثوم في قدر',
            'أضف الدجاج وقلّب حتى يتغير لونه',
            'أضف الطماطم والبهارات',
            'اسكب المرق واتركه يغلي',
            'خفّف الحرارة واطبخ 15 دقيقة',
            'أضف الكوسا واطبخ 10 دقائق',
            'قدّمها ساخنة'
        ],
        stepsEn: [
            'Sauté onion and garlic in pot',
            'Add chicken and stir until color changes',
            'Add tomatoes and spices',
            'Pour broth and bring to boil',
            'Reduce heat and cook 15 minutes',
            'Add zucchini and cook 10 minutes',
            'Serve hot'
        ],
        tips: 'غنية بالبروتين ومنخفضة الكربوهيدرات - مناسبة للكيتو',
        tipsEn: 'High protein low carb - suitable for keto'
    },
    {
        id: 89,
        category: 'وجبات خفيفة/دايت',
        categoryEn: 'Snacks/Diet',
        icon: '🥚',
        title: 'بيض مسلوق بالأفوكادو والطماطم',
        titleEn: 'Boiled Eggs with Avocado and Tomato',
        time: '15 دقيقة',
        timeEn: '15 minutes',
        servings: 1,
        calories: 245,
        nutrition: {
            protein: '14 جم',
            proteinEn: '14g',
            carbs: '12 جم',
            carbsEn: '12g',
            fat: '16 جم',
            fatEn: '16g',
            fiber: '7 جم',
            fiberEn: '7g'
        },
        ingredients: [
            '2 بيضة مسلوقة',
            '½ حبة أفوكادو',
            '½ كوب طماطم كرزية',
            '1 ملعقة كبيرة بصل أخضر',
            'عصير ربع ليمونة',
            'رشة ملح وفلفل أسود',
            'رشة فلفل أحمر'
        ],
        ingredientsEn: [
            '2 boiled eggs',
            '½ avocado',
            '½ cup cherry tomatoes',
            '1 tablespoon green onion',
            'Juice of ¼ lemon',
            'Pinch of salt and black pepper',
            'Pinch of red pepper'
        ],
        steps: [
            'اسلق البيض 10 دقائق',
            'قشّر البيض وقطّعه نصفين',
            'قطّع الأفوكادو مكعبات',
            'قطّع الطماطم نصفين',
            'رتّب جميع المكونات في طبق',
            'أضف عصير الليمون',
            'رش الملح والفلفل والبصل الأخضر'
        ],
        stepsEn: [
            'Boil eggs for 10 minutes',
            'Peel and cut eggs in half',
            'Cube the avocado',
            'Cut tomatoes in half',
            'Arrange all ingredients on plate',
            'Add lemon juice',
            'Sprinkle salt, pepper, and green onion'
        ],
        tips: 'فطور صحي غني بالدهون الصحية والبروتين',
        tipsEn: 'Healthy breakfast rich in healthy fats and protein'
    },
    {
        id: 90,
        category: 'وجبات خفيفة/دايت',
        categoryEn: 'Snacks/Diet',
        icon: '🦐',
        title: 'روبيان مشوي بالليمون والكزبرة',
        titleEn: 'Lemon Cilantro Grilled Shrimp',
        time: '20 دقيقة',
        timeEn: '20 minutes',
        servings: 3,
        calories: 140,
        nutrition: {
            protein: '26 جم',
            proteinEn: '26g',
            carbs: '3 جم',
            carbsEn: '3g',
            fat: '3 جم',
            fatEn: '3g',
            fiber: '0 جم',
            fiberEn: '0g'
        },
        ingredients: [
            '500 جرام روبيان مقشر',
            'عصير ليمونة',
            '3 فصوص ثوم مهروس',
            '¼ كوب كزبرة طازجة',
            '1 ملعقة صغيرة بابريكا',
            '½ ملعقة صغيرة كمون',
            'رشة فلفل حار',
            'ملح'
        ],
        ingredientsEn: [
            '500g peeled shrimp',
            'Juice of 1 lemon',
            '3 cloves garlic minced',
            '¼ cup fresh cilantro',
            '1 teaspoon paprika',
            '½ teaspoon cumin',
            'Pinch of hot pepper',
            'Salt'
        ],
        steps: [
            'نظّف الروبيان جيداً',
            'اخلط الليمون والثوم والبهارات',
            'اغمر الروبيان في التتبيلة 10 دقائق',
            'سخّن مقلاة شواء',
            'اشوِ الروبيان دقيقتين لكل جهة',
            'زيّن بالكزبرة الطازجة',
            'قدّمه فوراً'
        ],
        stepsEn: [
            'Clean shrimp well',
            'Mix lemon, garlic, and spices',
            'Marinate shrimp 10 minutes',
            'Heat grill pan',
            'Grill shrimp 2 minutes per side',
            'Garnish with fresh cilantro',
            'Serve immediately'
        ],
        tips: 'عالي البروتين جداً وخالي من الدهون تقريباً',
        tipsEn: 'Very high protein almost fat-free'
    },
    {
        id: 91,
        category: 'وجبات خفيفة/دايت',
        categoryEn: 'Snacks/Diet',
        icon: '🥗',
        title: 'سلطة الفاصوليا الخضراء بالليمون',
        titleEn: 'Lemon Green Bean Salad',
        time: '20 دقيقة',
        timeEn: '20 minutes',
        servings: 4,
        calories: 75,
        nutrition: {
            protein: '3 جم',
            proteinEn: '3g',
            carbs: '12 جم',
            carbsEn: '12g',
            fat: '2 جم',
            fatEn: '2g',
            fiber: '5 جم',
            fiberEn: '5g'
        },
        ingredients: [
            '500 جرام فاصوليا خضراء',
            'عصير ليمونة',
            '2 فص ثوم مهروس',
            '1 ملعقة صغيرة زيت زيتون',
            '2 ملعقة كبيرة بقدونس مفروم',
            'رشة فلفل أحمر',
            'ملح'
        ],
        ingredientsEn: [
            '500g green beans',
            'Juice of 1 lemon',
            '2 cloves garlic minced',
            '1 teaspoon olive oil',
            '2 tablespoons chopped parsley',
            'Pinch of red pepper',
            'Salt'
        ],
        steps: [
            'نظّف الفاصوليا وقطّع الأطراف',
            'اسلق الفاصوليا 8 دقائق',
            'صفّيها واغمرها بماء بارد',
            'اخلط الليمون والثوم والزيت',
            'اسكب الخليط على الفاصوليا',
            'أضف البقدونس والفلفل الأحمر',
            'قلّب وقدّمها'
        ],
        stepsEn: [
            'Trim green beans',
            'Boil beans 8 minutes',
            'Drain and shock in cold water',
            'Mix lemon, garlic, and oil',
            'Pour mixture over beans',
            'Add parsley and red pepper',
            'Toss and serve'
        ],
        tips: 'منخفضة السعرات وغنية بالألياف',
        tipsEn: 'Low calorie and high in fiber'
    }
];

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = recipesDatabase_Part5;
}
