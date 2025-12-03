// WiBo Health - Recipes Database (Part 2/5: Recipes 21-35)
// Bilingual (Arabic/English) Recipe Data

const recipesDatabase_Part2 = [
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
    module.exports = recipesDatabase_Part2;
}
