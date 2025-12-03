/**
 * WiBo Health - Food Database
 * قاعدة بيانات الأطعمة مع المعلومات الغذائية الكاملة
 */

const foodsDatabase = [
    // الحبوب والنشويات
    {
        id: 1,
        name: 'أرز أبيض مطبوخ',
        nameEn: 'White Rice',
        icon: '🍚',
        category: 'حبوب',
        gi: 73,
        ii: 79,
        nutrition: {
            calories: 130,
            protein: 2.7,
            carbs: 28,
            fat: 0.3,
            fiber: 0.4
        }
    },
    {
        id: 2,
        name: 'أرز بني مطبوخ',
        nameEn: 'Brown Rice',
        icon: '🍚',
        category: 'حبوب',
        gi: 50,
        ii: 62,
        nutrition: {
            calories: 111,
            protein: 2.6,
            carbs: 23,
            fat: 0.9,
            fiber: 1.8
        }
    },
    {
        id: 3,
        name: 'خبز أبيض',
        nameEn: 'White Bread',
        icon: '🍞',
        category: 'حبوب',
        gi: 75,
        ii: 100,
        nutrition: {
            calories: 265,
            protein: 9,
            carbs: 49,
            fat: 3.2,
            fiber: 2.7
        }
    },
    {
        id: 4,
        name: 'خبز أسمر (قمح كامل)',
        nameEn: 'Whole Wheat Bread',
        icon: '🍞',
        category: 'حبوب',
        gi: 53,
        ii: 56,
        nutrition: {
            calories: 247,
            protein: 13,
            carbs: 41,
            fat: 3.4,
            fiber: 7
        }
    },
    {
        id: 5,
        name: 'معكرونة بيضاء',
        nameEn: 'White Pasta',
        icon: '🍝',
        category: 'حبوب',
        gi: 58,
        ii: 46,
        nutrition: {
            calories: 131,
            protein: 5,
            carbs: 25,
            fat: 1.1,
            fiber: 1.8
        }
    },
    {
        id: 6,
        name: 'معكرونة القمح الكامل',
        nameEn: 'Whole Wheat Pasta',
        icon: '🍝',
        category: 'حبوب',
        gi: 42,
        ii: 40,
        nutrition: {
            calories: 124,
            protein: 5.3,
            carbs: 26,
            fat: 0.5,
            fiber: 3.9
        }
    },
    {
        id: 7,
        name: 'شوفان',
        nameEn: 'Oatmeal',
        icon: '🥣',
        category: 'حبوب',
        gi: 55,
        ii: 40,
        nutrition: {
            calories: 68,
            protein: 2.4,
            carbs: 12,
            fat: 1.4,
            fiber: 1.7
        }
    },
    // البقوليات
    {
        id: 8,
        name: 'عدس مطبوخ',
        nameEn: 'Lentils',
        icon: '🫘',
        category: 'بقوليات',
        gi: 32,
        ii: 58,
        nutrition: {
            calories: 116,
            protein: 9,
            carbs: 20,
            fat: 0.4,
            fiber: 7.9
        }
    },
    {
        id: 9,
        name: 'حمص مطبوخ',
        nameEn: 'Chickpeas',
        icon: '🫘',
        category: 'بقوليات',
        gi: 28,
        ii: 42,
        nutrition: {
            calories: 164,
            protein: 8.9,
            carbs: 27,
            fat: 2.6,
            fiber: 7.6
        }
    },
    {
        id: 10,
        name: 'فول مطبوخ',
        nameEn: 'Fava Beans',
        icon: '🫘',
        category: 'بقوليات',
        gi: 40,
        ii: 84,
        nutrition: {
            calories: 110,
            protein: 7.6,
            carbs: 19,
            fat: 0.4,
            fiber: 5.4
        }
    },
    // الفواكه
    {
        id: 11,
        name: 'تفاح',
        nameEn: 'Apple',
        icon: '🍎',
        category: 'فواكه',
        gi: 36,
        ii: 59,
        nutrition: {
            calories: 52,
            protein: 0.3,
            carbs: 14,
            fat: 0.2,
            fiber: 2.4
        }
    },
    {
        id: 12,
        name: 'موز',
        nameEn: 'Banana',
        icon: '🍌',
        category: 'فواكه',
        gi: 51,
        ii: 81,
        nutrition: {
            calories: 89,
            protein: 1.1,
            carbs: 23,
            fat: 0.3,
            fiber: 2.6
        }
    },
    {
        id: 13,
        name: 'برتقال',
        nameEn: 'Orange',
        icon: '🍊',
        category: 'فواكه',
        gi: 43,
        ii: 60,
        nutrition: {
            calories: 47,
            protein: 0.9,
            carbs: 12,
            fat: 0.1,
            fiber: 2.4
        }
    },
    {
        id: 14,
        name: 'بطيخ',
        nameEn: 'Watermelon',
        icon: '🍉',
        category: 'فواكه',
        gi: 72,
        ii: 51,
        nutrition: {
            calories: 30,
            protein: 0.6,
            carbs: 8,
            fat: 0.2,
            fiber: 0.4
        }
    },
    {
        id: 15,
        name: 'فراولة',
        nameEn: 'Strawberry',
        icon: '🍓',
        category: 'فواكه',
        gi: 40,
        ii: 40,
        nutrition: {
            calories: 32,
            protein: 0.7,
            carbs: 8,
            fat: 0.3,
            fiber: 2
        }
    },
    // الخضروات
    {
        id: 16,
        name: 'بطاطس مسلوقة',
        nameEn: 'Boiled Potato',
        icon: '🥔',
        category: 'خضروات',
        gi: 78,
        ii: 121,
        nutrition: {
            calories: 87,
            protein: 2,
            carbs: 20,
            fat: 0.1,
            fiber: 1.8
        }
    },
    {
        id: 17,
        name: 'بطاطا حلوة',
        nameEn: 'Sweet Potato',
        icon: '🍠',
        category: 'خضروات',
        gi: 63,
        ii: 94,
        nutrition: {
            calories: 90,
            protein: 2,
            carbs: 21,
            fat: 0.2,
            fiber: 3.3
        }
    },
    {
        id: 18,
        name: 'جزر',
        nameEn: 'Carrot',
        icon: '🥕',
        category: 'خضروات',
        gi: 39,
        ii: 51,
        nutrition: {
            calories: 41,
            protein: 0.9,
            carbs: 10,
            fat: 0.2,
            fiber: 2.8
        }
    },
    {
        id: 19,
        name: 'بروكلي',
        nameEn: 'Broccoli',
        icon: '🥦',
        category: 'خضروات',
        gi: 10,
        ii: 10,
        nutrition: {
            calories: 34,
            protein: 2.8,
            carbs: 7,
            fat: 0.4,
            fiber: 2.6
        }
    },
    {
        id: 20,
        name: 'طماطم',
        nameEn: 'Tomato',
        icon: '🍅',
        category: 'خضروات',
        gi: 15,
        ii: 38,
        nutrition: {
            calories: 18,
            protein: 0.9,
            carbs: 4,
            fat: 0.2,
            fiber: 1.2
        }
    },
    // منتجات الألبان
    {
        id: 21,
        name: 'حليب كامل الدسم',
        nameEn: 'Whole Milk',
        icon: '🥛',
        category: 'ألبان',
        gi: 39,
        ii: 90,
        nutrition: {
            calories: 61,
            protein: 3.2,
            carbs: 4.8,
            fat: 3.3,
            fiber: 0
        }
    },
    {
        id: 22,
        name: 'لبن رائب',
        nameEn: 'Yogurt',
        icon: '🥛',
        category: 'ألبان',
        gi: 36,
        ii: 115,
        nutrition: {
            calories: 59,
            protein: 3.5,
            carbs: 4.7,
            fat: 3.3,
            fiber: 0
        }
    },
    {
        id: 23,
        name: 'جبنة بيضاء',
        nameEn: 'White Cheese',
        icon: '🧀',
        category: 'ألبان',
        gi: 0,
        ii: 45,
        nutrition: {
            calories: 264,
            protein: 18,
            carbs: 1.3,
            fat: 21,
            fiber: 0
        }
    },
    // المكسرات
    {
        id: 24,
        name: 'لوز',
        nameEn: 'Almonds',
        icon: '🥜',
        category: 'مكسرات',
        gi: 0,
        ii: 20,
        nutrition: {
            calories: 579,
            protein: 21,
            carbs: 22,
            fat: 50,
            fiber: 12.5
        }
    },
    {
        id: 25,
        name: 'جوز',
        nameEn: 'Walnuts',
        icon: '🥜',
        category: 'مكسرات',
        gi: 15,
        ii: 16,
        nutrition: {
            calories: 654,
            protein: 15,
            carbs: 14,
            fat: 65,
            fiber: 6.7
        }
    },
    // البروتينات
    {
        id: 26,
        name: 'دجاج مشوي',
        nameEn: 'Grilled Chicken',
        icon: '🍗',
        category: 'بروتين',
        gi: 0,
        ii: 51,
        nutrition: {
            calories: 165,
            protein: 31,
            carbs: 0,
            fat: 3.6,
            fiber: 0
        }
    },
    {
        id: 27,
        name: 'سمك مشوي',
        nameEn: 'Grilled Fish',
        icon: '🐟',
        category: 'بروتين',
        gi: 0,
        ii: 59,
        nutrition: {
            calories: 143,
            protein: 26,
            carbs: 0,
            fat: 3.2,
            fiber: 0
        }
    },
    {
        id: 28,
        name: 'بيض مسلوق',
        nameEn: 'Boiled Egg',
        icon: '🥚',
        category: 'بروتين',
        gi: 0,
        ii: 42,
        nutrition: {
            calories: 155,
            protein: 13,
            carbs: 1.1,
            fat: 11,
            fiber: 0
        }
    },
    // السكريات والحلويات
    {
        id: 29,
        name: 'عسل',
        nameEn: 'Honey',
        icon: '🍯',
        category: 'سكريات',
        gi: 61,
        ii: 48,
        nutrition: {
            calories: 304,
            protein: 0.3,
            carbs: 82,
            fat: 0,
            fiber: 0.2
        }
    },
    {
        id: 30,
        name: 'شوكولاتة داكنة',
        nameEn: 'Dark Chocolate',
        icon: '🍫',
        category: 'سكريات',
        gi: 23,
        ii: 39,
        nutrition: {
            calories: 599,
            protein: 8,
            carbs: 46,
            fat: 43,
            fiber: 11
        }
    },
    // المزيد من الحبوب والنشويات
    {
        id: 31,
        name: 'كورن فليكس',
        nameEn: 'Corn Flakes',
        icon: '🥣',
        category: 'حبوب',
        gi: 81,
        ii: 75,
        nutrition: {
            calories: 357,
            protein: 7.5,
            carbs: 84,
            fat: 0.9,
            fiber: 3.3
        }
    },
    {
        id: 32,
        name: 'كينوا مطبوخة',
        nameEn: 'Quinoa',
        icon: '🌾',
        category: 'حبوب',
        gi: 53,
        ii: 62,
        nutrition: {
            calories: 120,
            protein: 4.4,
            carbs: 21,
            fat: 1.9,
            fiber: 2.8
        }
    },
    {
        id: 33,
        name: 'برغل مطبوخ',
        nameEn: 'Bulgur',
        icon: '🌾',
        category: 'حبوب',
        gi: 48,
        ii: 46,
        nutrition: {
            calories: 83,
            protein: 3.1,
            carbs: 19,
            fat: 0.2,
            fiber: 4.5
        }
    },
    {
        id: 34,
        name: 'كسكس مطبوخ',
        nameEn: 'Couscous',
        icon: '🌾',
        category: 'حبوب',
        gi: 65,
        ii: 58,
        nutrition: {
            calories: 112,
            protein: 3.8,
            carbs: 23,
            fat: 0.2,
            fiber: 1.4
        }
    },
    {
        id: 35,
        name: 'ذرة مسلوقة',
        nameEn: 'Boiled Corn',
        icon: '🌽',
        category: 'حبوب',
        gi: 52,
        ii: 54,
        nutrition: {
            calories: 86,
            protein: 3.3,
            carbs: 19,
            fat: 1.4,
            fiber: 2.4
        }
    },
    {
        id: 36,
        name: 'بليلة (قمح مسلوق)',
        nameEn: 'Boiled Wheat',
        icon: '🌾',
        category: 'حبوب',
        gi: 41,
        ii: 45,
        nutrition: {
            calories: 151,
            protein: 5.5,
            carbs: 32,
            fat: 0.4,
            fiber: 4.1
        }
    },
    {
        id: 37,
        name: 'خبز الشعير',
        nameEn: 'Barley Bread',
        icon: '🍞',
        category: 'حبوب',
        gi: 34,
        ii: 40,
        nutrition: {
            calories: 240,
            protein: 8.5,
        carbs: 47,
            fat: 1.5,
            fiber: 9.2
        }
    },
    {
        id: 38,
        name: 'خبز الشوفان',
        nameEn: 'Oat Bread',
        icon: '🍞',
        category: 'حبوب',
        gi: 47,
        ii: 44,
        nutrition: {
            calories: 255,
            protein: 10,
            carbs: 43,
            fat: 4.2,
            fiber: 5.8
        }
    },
    {
        id: 39,
        name: 'رز بسمتي مطبوخ',
        nameEn: 'Basmati Rice',
        icon: '🍚',
        category: 'حبوب',
        gi: 58,
        ii: 65,
        nutrition: {
            calories: 121,
            protein: 3,
            carbs: 25,
            fat: 0.4,
            fiber: 0.6
        }
    },
    {
        id: 40,
        name: 'مكرونة بالبشاميل',
        nameEn: 'Pasta Bechamel',
        icon: '🍝',
        category: 'حبوب',
        gi: 64,
        ii: 72,
        nutrition: {
            calories: 182,
            protein: 7.5,
            carbs: 21,
            fat: 8.1,
            fiber: 1.5
        }
    },
    // المزيد من الخضروات
    {
        id: 41,
        name: 'خيار',
        nameEn: 'Cucumber',
        icon: '🥒',
        category: 'خضروات',
        gi: 15,
        ii: 15,
        nutrition: {
            calories: 15,
            protein: 0.7,
            carbs: 3.6,
            fat: 0.1,
            fiber: 0.5
        }
    },
    {
        id: 42,
        name: 'خس',
        nameEn: 'Lettuce',
        icon: '🥬',
        category: 'خضروات',
        gi: 10,
        ii: 10,
        nutrition: {
            calories: 15,
            protein: 1.4,
            carbs: 2.9,
            fat: 0.2,
            fiber: 1.3
        }
    },
    {
        id: 43,
        name: 'فلفل أخضر',
        nameEn: 'Green Pepper',
        icon: '🫑',
        category: 'خضروات',
        gi: 10,
        ii: 10,
        nutrition: {
            calories: 20,
            protein: 0.9,
            carbs: 4.6,
            fat: 0.2,
            fiber: 1.7
        }
    },
    {
        id: 44,
        name: 'باذنجان مشوي',
        nameEn: 'Grilled Eggplant',
        icon: '🍆',
        category: 'خضروات',
        gi: 15,
        ii: 11,
        nutrition: {
            calories: 35,
            protein: 0.8,
            carbs: 8.6,
            fat: 0.2,
            fiber: 2.5
        }
    },
    {
        id: 45,
        name: 'كوسا',
        nameEn: 'Zucchini',
        icon: '🥒',
        category: 'خضروات',
        gi: 15,
        ii: 8,
        nutrition: {
            calories: 17,
            protein: 1.2,
            carbs: 3.1,
            fat: 0.3,
            fiber: 1
        }
    },
    {
        id: 46,
        name: 'قرنبيط',
        nameEn: 'Cauliflower',
        icon: '🥦',
        category: 'خضروات',
        gi: 10,
        ii: 10,
        nutrition: {
            calories: 25,
            protein: 1.9,
            carbs: 5,
            fat: 0.3,
            fiber: 2
        }
    },
    {
        id: 47,
        name: 'سبانخ',
        nameEn: 'Spinach',
        icon: '🥬',
        category: 'خضروات',
        gi: 15,
        ii: 15,
        nutrition: {
            calories: 23,
            protein: 2.9,
            carbs: 3.6,
            fat: 0.4,
            fiber: 2.2
        }
    },
    {
        id: 48,
        name: 'فجل',
        nameEn: 'Radish',
        icon: '🥕',
        category: 'خضروات',
        gi: 15,
        ii: 12,
        nutrition: {
            calories: 16,
            protein: 0.7,
            carbs: 3.4,
            fat: 0.1,
            fiber: 1.6
        }
    },
    {
        id: 49,
        name: 'فاصوليا خضراء',
        nameEn: 'Green Beans',
        icon: '🫛',
        category: 'خضروات',
        gi: 15,
        ii: 29,
        nutrition: {
            calories: 31,
            protein: 1.8,
            carbs: 7,
            fat: 0.2,
            fiber: 2.7
        }
    },
    {
        id: 50,
        name: 'بصل',
        nameEn: 'Onion',
        icon: '🧅',
        category: 'خضروات',
        gi: 10,
        ii: 14,
        nutrition: {
            calories: 40,
            protein: 1.1,
            carbs: 9.3,
            fat: 0.1,
            fiber: 1.7
        }
    },
    {
        id: 51,
        name: 'ثوم',
        nameEn: 'Garlic',
        icon: '🧄',
        category: 'خضروات',
        gi: 10,
        ii: 10,
        nutrition: {
            calories: 149,
            protein: 6.4,
            carbs: 33,
            fat: 0.5,
            fiber: 2.1
        }
    },
    {
        id: 52,
        name: 'بامية',
        nameEn: 'Okra',
        icon: '🫛',
        category: 'خضروات',
        gi: 20,
        ii: 24,
        nutrition: {
            calories: 33,
            protein: 1.9,
            carbs: 7.5,
            fat: 0.2,
            fiber: 3.2
        }
    },
    {
        id: 53,
        name: 'كرنب (ملفوف)',
        nameEn: 'Cabbage',
        icon: '🥬',
        category: 'خضروات',
        gi: 10,
        ii: 10,
        nutrition: {
            calories: 25,
            protein: 1.3,
            carbs: 5.8,
            fat: 0.1,
            fiber: 2.5
        }
    },
    {
        id: 54,
        name: 'فطر (مشروم)',
        nameEn: 'Mushroom',
        icon: '🍄',
        category: 'خضروات',
        gi: 10,
        ii: 17,
        nutrition: {
            calories: 22,
            protein: 3.1,
            carbs: 3.3,
            fat: 0.3,
            fiber: 1
        }
    },
    {
        id: 55,
        name: 'خرشوف',
        nameEn: 'Artichoke',
        icon: '🥬',
        category: 'خضروات',
        gi: 20,
        ii: 21,
        nutrition: {
            calories: 47,
            protein: 3.3,
            carbs: 11,
            fat: 0.2,
            fiber: 5.4
        }
    },
    // المزيد من الفواكه
    {
        id: 56,
        name: 'عنب',
        nameEn: 'Grapes',
        icon: '🍇',
        category: 'فواكه',
        gi: 59,
        ii: 82,
        nutrition: {
            calories: 69,
            protein: 0.7,
            carbs: 18,
            fat: 0.2,
            fiber: 0.9
        }
    },
    {
        id: 57,
        name: 'أناناس',
        nameEn: 'Pineapple',
        icon: '🍍',
        category: 'فواكه',
        gi: 59,
        ii: 84,
        nutrition: {
            calories: 50,
            protein: 0.5,
            carbs: 13,
            fat: 0.1,
            fiber: 1.4
        }
    },
    {
        id: 58,
        name: 'مانجو',
        nameEn: 'Mango',
        icon: '🥭',
        category: 'فواكه',
        gi: 51,
        ii: 60,
        nutrition: {
            calories: 60,
            protein: 0.8,
            carbs: 15,
            fat: 0.4,
            fiber: 1.6
        }
    },
    {
        id: 59,
        name: 'كيوي',
        nameEn: 'Kiwi',
        icon: '🥝',
        category: 'فواكه',
        gi: 53,
        ii: 47,
        nutrition: {
            calories: 61,
            protein: 1.1,
            carbs: 15,
            fat: 0.5,
            fiber: 3
        }
    },
    {
        id: 60,
        name: 'خوخ',
        nameEn: 'Peach',
        icon: '🍑',
        category: 'فواكه',
        gi: 42,
        ii: 60,
        nutrition: {
            calories: 39,
            protein: 0.9,
            carbs: 10,
            fat: 0.3,
            fiber: 1.5
        }
    },
    {
        id: 61,
        name: 'مشمش',
        nameEn: 'Apricot',
        icon: '🍑',
        category: 'فواكه',
        gi: 34,
        ii: 53,
        nutrition: {
            calories: 48,
            protein: 1.4,
            carbs: 11,
            fat: 0.4,
            fiber: 2
        }
    },
    {
        id: 62,
        name: 'كمثرى',
        nameEn: 'Pear',
        icon: '🍐',
        category: 'فواكه',
        gi: 38,
        ii: 60,
        nutrition: {
            calories: 57,
            protein: 0.4,
            carbs: 15,
            fat: 0.1,
            fiber: 3.1
        }
    },
    {
        id: 63,
        name: 'توت أزرق',
        nameEn: 'Blueberry',
        icon: '🫐',
        category: 'فواكه',
        gi: 53,
        ii: 56,
        nutrition: {
            calories: 57,
            protein: 0.7,
            carbs: 14,
            fat: 0.3,
            fiber: 2.4
        }
    },
    {
        id: 64,
        name: 'توت العليق',
        nameEn: 'Raspberry',
        icon: '🍇',
        category: 'فواكه',
        gi: 32,
        ii: 37,
        nutrition: {
            calories: 52,
            protein: 1.2,
            carbs: 12,
            fat: 0.7,
            fiber: 6.5
        }
    },
    {
        id: 65,
        name: 'كرز',
        nameEn: 'Cherry',
        icon: '🍒',
        category: 'فواكه',
        gi: 22,
        ii: 40,
        nutrition: {
            calories: 63,
            protein: 1.1,
            carbs: 16,
            fat: 0.2,
            fiber: 2.1
        }
    },
    {
        id: 66,
        name: 'تمر (رطب)',
        nameEn: 'Fresh Dates',
        icon: '🫐',
        category: 'فواكه',
        gi: 103,
        ii: 110,
        nutrition: {
            calories: 277,
            protein: 1.8,
            carbs: 75,
            fat: 0.2,
            fiber: 6.7
        }
    },
    {
        id: 67,
        name: 'تمر جاف',
        nameEn: 'Dried Dates',
        icon: '🫐',
        category: 'فواكه',
        gi: 62,
        ii: 85,
        nutrition: {
            calories: 282,
            protein: 2.5,
            carbs: 75,
            fat: 0.4,
            fiber: 8
        }
    },
    {
        id: 68,
        name: 'زبيب',
        nameEn: 'Raisins',
        icon: '🍇',
        category: 'فواكه',
        gi: 64,
        ii: 62,
        nutrition: {
            calories: 299,
            protein: 3.1,
            carbs: 79,
            fat: 0.5,
            fiber: 3.7
        }
    },
    {
        id: 69,
        name: 'تين',
        nameEn: 'Fig',
        icon: '🍇',
        category: 'فواكه',
        gi: 61,
        ii: 58,
        nutrition: {
            calories: 74,
            protein: 0.8,
            carbs: 19,
            fat: 0.3,
            fiber: 2.9
        }
    },
    {
        id: 70,
        name: 'رمان',
        nameEn: 'Pomegranate',
        icon: '🍎',
        category: 'فواكه',
        gi: 53,
        ii: 60,
        nutrition: {
            calories: 83,
            protein: 1.7,
            carbs: 19,
            fat: 1.2,
            fiber: 4
        }
    },
    {
        id: 71,
        name: 'جوافة',
        nameEn: 'Guava',
        icon: '🍐',
        category: 'فواكه',
        gi: 12,
        ii: 30,
        nutrition: {
            calories: 68,
            protein: 2.6,
            carbs: 14,
            fat: 1,
            fiber: 5.4
        }
    },
    {
        id: 72,
        name: 'بابايا',
        nameEn: 'Papaya',
        icon: '🥭',
        category: 'فواكه',
        gi: 60,
        ii: 59,
        nutrition: {
            calories: 43,
            protein: 0.5,
            carbs: 11,
            fat: 0.3,
            fiber: 1.7
        }
    },
    {
        id: 73,
        name: 'شمام',
        nameEn: 'Cantaloupe',
        icon: '🍈',
        category: 'فواكه',
        gi: 65,
        ii: 70,
        nutrition: {
            calories: 34,
            protein: 0.8,
            carbs: 8,
            fat: 0.2,
            fiber: 0.9
        }
    },
    {
        id: 74,
        name: 'يوسفي',
        nameEn: 'Tangerine',
        icon: '🍊',
        category: 'فواكه',
        gi: 42,
        ii: 58,
        nutrition: {
            calories: 53,
            protein: 0.8,
            carbs: 13,
            fat: 0.3,
            fiber: 1.8
        }
    },
    {
        id: 75,
        name: 'جريب فروت',
        nameEn: 'Grapefruit',
        icon: '🍊',
        category: 'فواكه',
        gi: 25,
        ii: 48,
        nutrition: {
            calories: 42,
            protein: 0.8,
            carbs: 11,
            fat: 0.1,
            fiber: 1.6
        }
    },
    // المزيد من منتجات الألبان
    {
        id: 76,
        name: 'حليب خالي الدسم',
        nameEn: 'Skim Milk',
        icon: '🥛',
        category: 'ألبان',
        gi: 32,
        ii: 90,
        nutrition: {
            calories: 34,
            protein: 3.4,
            carbs: 5,
            fat: 0.1,
            fiber: 0
        }
    },
    {
        id: 77,
        name: 'زبادي يوناني',
        nameEn: 'Greek Yogurt',
        icon: '🥛',
        category: 'ألبان',
        gi: 11,
        ii: 84,
        nutrition: {
            calories: 97,
            protein: 9,
            carbs: 3.9,
            fat: 5,
            fiber: 0
        }
    },
    {
        id: 78,
        name: 'لبنة',
        nameEn: 'Labneh',
        icon: '🧈',
        category: 'ألبان',
        gi: 10,
        ii: 65,
        nutrition: {
            calories: 111,
            protein: 5.2,
            carbs: 3.8,
            fat: 9,
            fiber: 0
        }
    },
    {
        id: 79,
        name: 'جبنة موزاريلا',
        nameEn: 'Mozzarella',
        icon: '🧀',
        category: 'ألبان',
        gi: 0,
        ii: 57,
        nutrition: {
            calories: 280,
            protein: 28,
            carbs: 2.2,
            fat: 17,
            fiber: 0
        }
    },
    {
        id: 80,
        name: 'جبنة شيدر',
        nameEn: 'Cheddar Cheese',
        icon: '🧀',
        category: 'ألبان',
        gi: 0,
        ii: 45,
        nutrition: {
            calories: 403,
            protein: 25,
            carbs: 1.3,
            fat: 33,
            fiber: 0
        }
    },
    {
        id: 81,
        name: 'جبنة قريش',
        nameEn: 'Cottage Cheese',
        icon: '🧀',
        category: 'ألبان',
        gi: 10,
        ii: 32,
        nutrition: {
            calories: 98,
            protein: 11,
            carbs: 3.4,
            fat: 4.3,
            fiber: 0
        }
    },
    {
        id: 82,
        name: 'جبنة كريمي',
        nameEn: 'Cream Cheese',
        icon: '🧀',
        category: 'ألبان',
        gi: 0,
        ii: 32,
        nutrition: {
            calories: 342,
            protein: 6,
            carbs: 4.1,
            fat: 34,
            fiber: 0
        }
    },
    {
        id: 83,
        name: 'زبدة',
        nameEn: 'Butter',
        icon: '🧈',
        category: 'ألبان',
        gi: 0,
        ii: 7,
        nutrition: {
            calories: 717,
            protein: 0.9,
            carbs: 0.1,
            fat: 81,
            fiber: 0
        }
    },
    {
        id: 84,
        name: 'قشطة',
        nameEn: 'Cream',
        icon: '🧈',
        category: 'ألبان',
        gi: 0,
        ii: 24,
        nutrition: {
            calories: 340,
            protein: 2.1,
            carbs: 3.1,
            fat: 36,
            fiber: 0
        }
    },
    {
        id: 85,
        name: 'آيس كريم فانيليا',
        nameEn: 'Vanilla Ice Cream',
        icon: '🍦',
        category: 'ألبان',
        gi: 61,
        ii: 89,
        nutrition: {
            calories: 207,
            protein: 3.5,
            carbs: 24,
            fat: 11,
            fiber: 0.7
        }
    },
    // المزيد من المكسرات والبذور
    {
        id: 86,
        name: 'كاجو',
        nameEn: 'Cashew',
        icon: '🥜',
        category: 'مكسرات',
        gi: 22,
        ii: 25,
        nutrition: {
            calories: 553,
            protein: 18,
            carbs: 30,
            fat: 44,
            fiber: 3.3
        }
    },
    {
        id: 87,
        name: 'فستق حلبي',
        nameEn: 'Pistachio',
        icon: '🥜',
        category: 'مكسرات',
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 560,
            protein: 20,
            carbs: 28,
            fat: 45,
            fiber: 10.6
        }
    },
    {
        id: 88,
        name: 'بندق',
        nameEn: 'Hazelnut',
        icon: '🌰',
        category: 'مكسرات',
        gi: 15,
        ii: 17,
        nutrition: {
            calories: 628,
            protein: 15,
            carbs: 17,
            fat: 61,
            fiber: 9.7
        }
    },
    {
        id: 89,
        name: 'فول سوداني',
        nameEn: 'Peanuts',
        icon: '🥜',
        category: 'مكسرات',
        gi: 14,
        ii: 20,
        nutrition: {
            calories: 567,
            protein: 26,
            carbs: 16,
            fat: 49,
            fiber: 8.5
        }
    },
    {
        id: 90,
        name: 'بذور دوار الشمس',
        nameEn: 'Sunflower Seeds',
        icon: '🌻',
        category: 'مكسرات',
        gi: 35,
        ii: 35,
        nutrition: {
            calories: 584,
            protein: 21,
            carbs: 20,
            fat: 51,
            fiber: 8.6
        }
    },
    {
        id: 91,
        name: 'بذور اليقطين',
        nameEn: 'Pumpkin Seeds',
        icon: '🎃',
        category: 'مكسرات',
        gi: 25,
        ii: 30,
        nutrition: {
            calories: 559,
            protein: 30,
            carbs: 11,
            fat: 49,
            fiber: 6
        }
    },
    {
        id: 92,
        name: 'بذور الشيا',
        nameEn: 'Chia Seeds',
        icon: '🌾',
        category: 'مكسرات',
        gi: 1,
        ii: 1,
        nutrition: {
            calories: 486,
            protein: 17,
            carbs: 42,
            fat: 31,
            fiber: 34
        }
    },
    {
        id: 93,
        name: 'بذور الكتان',
        nameEn: 'Flax Seeds',
        icon: '🌾',
        category: 'مكسرات',
        gi: 35,
        ii: 35,
        nutrition: {
            calories: 534,
            protein: 18,
            carbs: 29,
            fat: 42,
            fiber: 27
        }
    },
    {
        id: 94,
        name: 'سمسم',
        nameEn: 'Sesame Seeds',
        icon: '🌾',
        category: 'مكسرات',
        gi: 35,
        ii: 35,
        nutrition: {
            calories: 573,
            protein: 18,
            carbs: 23,
            fat: 50,
            fiber: 11.8
        }
    },
    {
        id: 95,
        name: 'زبدة الفول السوداني',
        nameEn: 'Peanut Butter',
        icon: '🥜',
        category: 'مكسرات',
        gi: 14,
        ii: 20,
        nutrition: {
            calories: 588,
            protein: 25,
            carbs: 20,
            fat: 50,
            fiber: 6
        }
    },
    // المزيد من البروتينات
    {
        id: 96,
        name: 'لحم بقري مشوي',
        nameEn: 'Grilled Beef',
        icon: '🥩',
        category: 'بروتين',
        gi: 0,
        ii: 51,
        nutrition: {
            calories: 250,
            protein: 26,
            carbs: 0,
            fat: 15,
            fiber: 0
        }
    },
    {
        id: 97,
        name: 'لحم خروف',
        nameEn: 'Lamb',
        icon: '🥩',
        category: 'بروتين',
        gi: 0,
        ii: 51,
        nutrition: {
            calories: 294,
            protein: 25,
            carbs: 0,
            fat: 21,
            fiber: 0
        }
    },
    {
        id: 98,
        name: 'ديك رومي',
        nameEn: 'Turkey',
        icon: '🍗',
        category: 'بروتين',
        gi: 0,
        ii: 40,
        nutrition: {
            calories: 189,
            protein: 29,
            carbs: 0,
            fat: 7,
            fiber: 0
        }
    },
    {
        id: 99,
        name: 'سمك السلمون',
        nameEn: 'Salmon',
        icon: '🐟',
        category: 'بروتين',
        gi: 0,
        ii: 59,
        nutrition: {
            calories: 208,
            protein: 20,
            carbs: 0,
            fat: 13,
            fiber: 0
        }
    },
    {
        id: 100,
        name: 'سمك التونة',
        nameEn: 'Tuna',
        icon: '🐟',
        category: 'بروتين',
        gi: 0,
        ii: 26,
        nutrition: {
            calories: 144,
            protein: 23,
            carbs: 0,
            fat: 5,
            fiber: 0
        }
    },
    {
        id: 101,
        name: 'جمبري',
        nameEn: 'Shrimp',
        icon: '🦐',
        category: 'بروتين',
        gi: 0,
        ii: 28,
        nutrition: {
            calories: 99,
            protein: 24,
            carbs: 0.2,
            fat: 0.3,
            fiber: 0
        }
    },
    {
        id: 102,
        name: 'كابوريا',
        nameEn: 'Crab',
        icon: '🦀',
        category: 'بروتين',
        gi: 0,
        ii: 30,
        nutrition: {
            calories: 97,
            protein: 19,
            carbs: 0,
            fat: 1.5,
            fiber: 0
        }
    },
    {
        id: 103,
        name: 'حبار',
        nameEn: 'Calamari',
        icon: '🦑',
        category: 'بروتين',
        gi: 0,
        ii: 31,
        nutrition: {
            calories: 92,
            protein: 16,
            carbs: 3.1,
            fat: 1.4,
            fiber: 0
        }
    },
    {
        id: 104,
        name: 'أخطبوط',
        nameEn: 'Octopus',
        icon: '🐙',
        category: 'بروتين',
        gi: 0,
        ii: 30,
        nutrition: {
            calories: 82,
            protein: 15,
            carbs: 2.2,
            fat: 1,
            fiber: 0
        }
    },
    {
        id: 105,
        name: 'كبدة بقري',
        nameEn: 'Beef Liver',
        icon: '🥩',
        category: 'بروتين',
        gi: 0,
        ii: 73,
        nutrition: {
            calories: 135,
            protein: 20,
            carbs: 3.9,
            fat: 4,
            fiber: 0
        }
    },
    // المزيد من البقوليات
    {
        id: 106,
        name: 'فاصوليا بيضاء',
        nameEn: 'White Beans',
        icon: '🫘',
        category: 'بقوليات',
        gi: 38,
        ii: 40,
        nutrition: {
            calories: 139,
            protein: 9.7,
            carbs: 25,
            fat: 0.5,
            fiber: 6.4
        }
    },
    {
        id: 107,
        name: 'فاصوليا حمراء',
        nameEn: 'Red Beans',
        icon: '🫘',
        category: 'بقوليات',
        gi: 24,
        ii: 39,
        nutrition: {
            calories: 127,
            protein: 8.7,
            carbs: 23,
            fat: 0.5,
            fiber: 7.4
        }
    },
    {
        id: 108,
        name: 'لوبيا',
        nameEn: 'Black-eyed Peas',
        icon: '🫘',
        category: 'بقوليات',
        gi: 33,
        ii: 40,
        nutrition: {
            calories: 116,
            protein: 8,
            carbs: 21,
            fat: 0.5,
            fiber: 6
        }
    },
    {
        id: 109,
        name: 'فول الصويا',
        nameEn: 'Soybeans',
        icon: '🫘',
        category: 'بقوليات',
        gi: 15,
        ii: 43,
        nutrition: {
            calories: 173,
            protein: 17,
            carbs: 10,
            fat: 9,
            fiber: 6
        }
    },
    {
        id: 110,
        name: 'فول أخضر',
        nameEn: 'Green Peas',
        icon: '🫛',
        category: 'بقوليات',
        gi: 48,
        ii: 47,
        nutrition: {
            calories: 81,
            protein: 5.4,
            carbs: 14,
            fat: 0.4,
            fiber: 5.7
        }
    },
    // أطعمة عربية شعبية
    {
        id: 111,
        name: 'كبسة دجاج',
        nameEn: 'Chicken Kabsa',
        icon: '🍛',
        category: 'أطعمة عربية',
        gi: 58,
        ii: 72,
        nutrition: {
            calories: 285,
            protein: 18,
            carbs: 32,
            fat: 9,
            fiber: 2.1
        }
    },
    {
        id: 112,
        name: 'مندي لحم',
        nameEn: 'Lamb Mandi',
        icon: '🍛',
        category: 'أطعمة عربية',
        gi: 55,
        ii: 68,
        nutrition: {
            calories: 320,
            protein: 22,
            carbs: 35,
            fat: 12,
            fiber: 1.8
        }
    },
    {
        id: 114,
        name: 'فول مدمس',
        nameEn: 'Foul Mudammas',
        icon: '🫘',
        category: 'أطعمة عربية',
        gi: 40,
        ii: 57,
        nutrition: {
            calories: 187,
            protein: 10,
            carbs: 23,
            fat: 7,
            fiber: 9.3
        }
    },
    {
        id: 115,
        name: 'فلافل',
        nameEn: 'Falafel',
        icon: '🧆',
        category: 'أطعمة عربية',
        gi: 32,
        ii: 35,
        nutrition: {
            calories: 333,
            protein: 13,
            carbs: 32,
            fat: 18,
            fiber: 5
        }
    },
    {
        id: 116,
        name: 'حمص بالطحينة',
        nameEn: 'Hummus',
        icon: '🥙',
        category: 'أطعمة عربية',
        gi: 6,
        ii: 25,
        nutrition: {
            calories: 166,
            protein: 8,
            carbs: 14,
            fat: 10,
            fiber: 6
        }
    },
    {
        id: 117,
        name: 'بابا غنوج',
        nameEn: 'Baba Ghanoush',
        icon: '🍆',
        category: 'أطعمة عربية',
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 160,
            protein: 3,
            carbs: 9,
            fat: 13,
            fiber: 4
        }
    },
    {
        id: 118,
        name: 'طبولة',
        nameEn: 'Tabbouleh',
        icon: '🥗',
        category: 'أطعمة عربية',
        gi: 47,
        ii: 45,
        nutrition: {
            calories: 36,
            protein: 1.3,
            carbs: 5.6,
            fat: 1.2,
            fiber: 1.4
        }
    },
    {
        id: 119,
        name: 'فتوش',
        nameEn: 'Fattoush',
        icon: '🥗',
        category: 'أطعمة عربية',
        gi: 40,
        ii: 38,
        nutrition: {
            calories: 89,
            protein: 2.5,
            carbs: 12,
            fat: 3.8,
            fiber: 2.6
        }
    },
    {
        id: 120,
        name: 'ملوخية',
        nameEn: 'Molokhia',
        icon: '🥬',
        category: 'أطعمة عربية',
        gi: 15,
        ii: 25,
        nutrition: {
            calories: 58,
            protein: 5,
            carbs: 10,
            fat: 0.5,
            fiber: 2
        }
    },
    {
        id: 121,
        name: 'شاورما دجاج',
        nameEn: 'Chicken Shawarma',
        icon: '🌯',
        category: 'أطعمة عربية',
        gi: 45,
        ii: 58,
        nutrition: {
            calories: 265,
            protein: 22,
            carbs: 18,
            fat: 12,
            fiber: 2
        }
    },
    {
        id: 122,
        name: 'شيش طاووق',
        nameEn: 'Shish Taouk',
        icon: '串',
        category: 'أطعمة عربية',
        gi: 0,
        ii: 51,
        nutrition: {
            calories: 195,
            protein: 27,
            carbs: 2,
            fat: 8,
            fiber: 0.3
        }
    },
    {
        id: 123,
        name: 'كفتة مشوية',
        nameEn: 'Grilled Kofta',
        icon: '🍖',
        category: 'أطعمة عربية',
        gi: 0,
        ii: 52,
        nutrition: {
            calories: 278,
            protein: 21,
            carbs: 3,
            fat: 20,
            fiber: 0.5
        }
    },
    {
        id: 124,
        name: 'محشي ورق عنب',
        nameEn: 'Stuffed Grape Leaves',
        icon: '🍃',
        category: 'أطعمة عربية',
        gi: 48,
        ii: 55,
        nutrition: {
            calories: 158,
            protein: 3,
            carbs: 22,
            fat: 6.5,
            fiber: 2.1
        }
    },
    {
        id: 125,
        name: 'محشي كوسا',
        nameEn: 'Stuffed Zucchini',
        icon: '🥒',
        category: 'أطعمة عربية',
        gi: 45,
        ii: 52,
        nutrition: {
            calories: 142,
            protein: 6,
            carbs: 18,
            fat: 5.5,
            fiber: 2.3
        }
    },
    {
        id: 126,
        name: 'منسف',
        nameEn: 'Mansaf',
        icon: '🍲',
        category: 'أطعمة عربية',
        gi: 52,
        ii: 75,
        nutrition: {
            calories: 380,
            protein: 24,
            carbs: 38,
            fat: 15,
            fiber: 1.5
        }
    },
    {
        id: 127,
        name: 'مجدرة',
        nameEn: 'Mujadara',
        icon: '🍚',
        category: 'أطعمة عربية',
        gi: 44,
        ii: 52,
        nutrition: {
            calories: 212,
            protein: 9,
            carbs: 35,
            fat: 4,
            fiber: 7.8
        }
    },
    {
        id: 128,
        name: 'فتة حمص',
        nameEn: 'Fatteh',
        icon: '🥙',
        category: 'أطعمة عربية',
        gi: 48,
        ii: 62,
        nutrition: {
            calories: 310,
            protein: 12,
            carbs: 32,
            fat: 15,
            fiber: 7
        }
    },
    {
        id: 129,
        name: 'كباب حلة',
        nameEn: 'Halla Kebab',
        icon: '🍲',
        category: 'أطعمة عربية',
        gi: 15,
        ii: 55,
        nutrition: {
            calories: 245,
            protein: 20,
            carbs: 8,
            fat: 15,
            fiber: 2.5
        }
    },
    {
        id: 130,
        name: 'صيادية سمك',
        nameEn: 'Sayyadieh',
        icon: '🐟',
        category: 'أطعمة عربية',
        gi: 52,
        ii: 64,
        nutrition: {
            calories: 298,
            protein: 22,
            carbs: 30,
            fat: 10,
            fiber: 2
        }
    },
    // حلويات عربية
    {
        id: 131,
        name: 'بقلاوة',
        nameEn: 'Baklava',
        icon: '🥐',
        category: 'حلويات',
        gi: 67,
        ii: 72,
        nutrition: {
            calories: 428,
            protein: 6,
            carbs: 51,
            fat: 23,
            fiber: 2.5
        }
    },
    {
        id: 132,
        name: 'كنافة',
        nameEn: 'Kunafa',
        icon: '🧀',
        category: 'حلويات',
        gi: 72,
        ii: 85,
        nutrition: {
            calories: 385,
            protein: 8,
            carbs: 47,
            fat: 19,
            fiber: 1.2
        }
    },
    {
        id: 133,
        name: 'بسبوسة',
        nameEn: 'Basbousa',
        icon: '🍰',
        category: 'حلويات',
        gi: 70,
        ii: 80,
        nutrition: {
            calories: 358,
            protein: 5,
            carbs: 52,
            fat: 15,
            fiber: 1.8
        }
    },
    {
        id: 134,
        name: 'قطايف',
        nameEn: 'Qatayef',
        icon: '🥞',
        category: 'حلويات',
        gi: 68,
        ii: 76,
        nutrition: {
            calories: 312,
            protein: 6,
            carbs: 48,
            fat: 11,
            fiber: 2
        }
    },
    {
        id: 135,
        name: 'هريسة',
        nameEn: 'Harisa',
        icon: '🍰',
        category: 'حلويات',
        gi: 72,
        ii: 78,
        nutrition: {
            calories: 367,
            protein: 4,
            carbs: 55,
            fat: 15,
            fiber: 1.5
        }
    },
    {
        id: 136,
        name: 'لقيمات',
        nameEn: 'Luqaimat',
        icon: '🍩',
        category: 'حلويات',
        gi: 76,
        ii: 82,
        nutrition: {
            calories: 342,
            protein: 4,
            carbs: 48,
            fat: 15,
            fiber: 1
        }
    },
    {
        id: 137,
        name: 'مهلبية',
        nameEn: 'Mahalabia',
        icon: '🍮',
        category: 'حلويات',
        gi: 61,
        ii: 70,
        nutrition: {
            calories: 142,
            protein: 3.5,
            carbs: 22,
            fat: 4.5,
            fiber: 0.3
        }
    },
    {
        id: 138,
        name: 'أم علي',
        nameEn: 'Om Ali',
        icon: '🥧',
        category: 'حلويات',
        gi: 69,
        ii: 78,
        nutrition: {
            calories: 328,
            protein: 7,
            carbs: 38,
            fat: 17,
            fiber: 1.5
        }
    },
    {
        id: 139,
        name: 'معمول بالتمر',
        nameEn: 'Date Maamoul',
        icon: '🍪',
        category: 'حلويات',
        gi: 64,
        ii: 70,
        nutrition: {
            calories: 378,
            protein: 5,
            carbs: 52,
            fat: 17,
            fiber: 3.2
        }
    },
    {
        id: 140,
        name: 'غريبة',
        nameEn: 'Ghorayeba',
        icon: '🍪',
        category: 'حلويات',
        gi: 68,
        ii: 65,
        nutrition: {
            calories: 485,
            protein: 6,
            carbs: 54,
            fat: 27,
            fiber: 1.2
        }
    },
    // حلويات عالمية
    {
        id: 141,
        name: 'كيك شوكولاتة',
        nameEn: 'Chocolate Cake',
        icon: '🍰',
        category: 'حلويات',
        gi: 42,
        ii: 65,
        nutrition: {
            calories: 371,
            protein: 5,
            carbs: 50,
            fat: 17,
            fiber: 2
        }
    },
    {
        id: 142,
        name: 'كوكيز الشوفان',
        nameEn: 'Oatmeal Cookies',
        icon: '🍪',
        category: 'حلويات',
        gi: 54,
        ii: 58,
        nutrition: {
            calories: 442,
            protein: 6.5,
            carbs: 64,
            fat: 18,
            fiber: 3.2
        }
    },
    {
        id: 143,
        name: 'دونات',
        nameEn: 'Donut',
        icon: '🍩',
        category: 'حلويات',
        gi: 76,
        ii: 74,
        nutrition: {
            calories: 452,
            protein: 5,
            carbs: 51,
            fat: 25,
            fiber: 1.5
        }
    },
    {
        id: 144,
        name: 'براوني',
        nameEn: 'Brownie',
        icon: '🍫',
        category: 'حلويات',
        gi: 42,
        ii: 60,
        nutrition: {
            calories: 466,
            protein: 6,
            carbs: 59,
            fat: 24,
            fiber: 3
        }
    },
    {
        id: 145,
        name: 'بان كيك',
        nameEn: 'Pancake',
        icon: '🥞',
        category: 'حلويات',
        gi: 67,
        ii: 96,
        nutrition: {
            calories: 227,
            protein: 6,
            carbs: 28,
            fat: 10,
            fiber: 0.9
        }
    },
    {
        id: 146,
        name: 'وافل',
        nameEn: 'Waffle',
        icon: '🧇',
        category: 'حلويات',
        gi: 76,
        ii: 74,
        nutrition: {
            calories: 291,
            protein: 6,
            carbs: 33,
            fat: 15,
            fiber: 1.7
        }
    },
    {
        id: 147,
        name: 'تشيز كيك',
        nameEn: 'Cheesecake',
        icon: '🍰',
        category: 'حلويات',
        gi: 55,
        ii: 48,
        nutrition: {
            calories: 321,
            protein: 5.5,
            carbs: 26,
            fat: 23,
            fiber: 0.8
        }
    },
    {
        id: 148,
        name: 'تيراميسو',
        nameEn: 'Tiramisu',
        icon: '🍰',
        category: 'حلويات',
        gi: 55,
        ii: 60,
        nutrition: {
            calories: 240,
            protein: 4.5,
            carbs: 22,
            fat: 15,
            fiber: 0.4
        }
    },
    {
        id: 149,
        name: 'كريم كراميل',
        nameEn: 'Creme Caramel',
        icon: '🍮',
        category: 'حلويات',
        gi: 61,
        ii: 68,
        nutrition: {
            calories: 150,
            protein: 4,
            carbs: 23,
            fat: 4.5,
            fiber: 0
        }
    },
    {
        id: 150,
        name: 'جيلي',
        nameEn: 'Jelly',
        icon: '🍮',
        category: 'حلويات',
        gi: 70,
        ii: 50,
        nutrition: {
            calories: 62,
            protein: 1.5,
            carbs: 14,
            fat: 0,
            fiber: 0
        }
    },
    // مشروبات
    {
        id: 151,
        name: 'قهوة سوداء',
        nameEn: 'Black Coffee',
        icon: '☕',
        category: 'مشروبات',
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 2,
            protein: 0.3,
            carbs: 0,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 152,
        name: 'قهوة بالحليب',
        nameEn: 'Coffee with Milk',
        icon: '☕',
        category: 'مشروبات',
        gi: 27,
        ii: 48,
        nutrition: {
            calories: 38,
            protein: 2,
            carbs: 3.5,
            fat: 2,
            fiber: 0
        }
    },
    {
        id: 153,
        name: 'كابتشينو',
        nameEn: 'Cappuccino',
        icon: '☕',
        category: 'مشروبات',
        gi: 30,
        ii: 52,
        nutrition: {
            calories: 74,
            protein: 4,
            carbs: 6,
            fat: 4,
            fiber: 0
        }
    },
    {
        id: 154,
        name: 'لاتيه',
        nameEn: 'Latte',
        icon: '☕',
        category: 'مشروبات',
        gi: 32,
        ii: 55,
        nutrition: {
            calories: 103,
            protein: 5.5,
            carbs: 8.5,
            fat: 5.5,
            fiber: 0
        }
    },
    {
        id: 155,
        name: 'شاي أخضر',
        nameEn: 'Green Tea',
        icon: '🍵',
        category: 'مشروبات',
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 2,
            protein: 0.2,
            carbs: 0,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 156,
        name: 'شاي أسود',
        nameEn: 'Black Tea',
        icon: '🍵',
        category: 'مشروبات',
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 2,
            protein: 0,
            carbs: 0.7,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 157,
        name: 'شاي بالحليب والسكر',
        nameEn: 'Tea with Milk & Sugar',
        icon: '🍵',
        category: 'مشروبات',
        gi: 55,
        ii: 65,
        nutrition: {
            calories: 65,
            protein: 1.5,
            carbs: 12,
            fat: 1.5,
            fiber: 0
        }
    },
    {
        id: 158,
        name: 'عصير برتقال طازج',
        nameEn: 'Fresh Orange Juice',
        icon: '🍊',
        category: 'مشروبات',
        gi: 50,
        ii: 71,
        nutrition: {
            calories: 45,
            protein: 0.7,
            carbs: 10,
            fat: 0.2,
            fiber: 0.2
        }
    },
    {
        id: 159,
        name: 'عصير تفاح',
        nameEn: 'Apple Juice',
        icon: '🍎',
        category: 'مشروبات',
        gi: 41,
        ii: 63,
        nutrition: {
            calories: 46,
            protein: 0.1,
            carbs: 11,
            fat: 0.1,
            fiber: 0.2
        }
    },
    {
        id: 160,
        name: 'عصير عنب',
        nameEn: 'Grape Juice',
        icon: '🍇',
        category: 'مشروبات',
        gi: 59,
        ii: 74,
        nutrition: {
            calories: 60,
            protein: 0.4,
            carbs: 15,
            fat: 0.1,
            fiber: 0.2
        }
    },
    {
        id: 161,
        name: 'عصير أناناس',
        nameEn: 'Pineapple Juice',
        icon: '🍍',
        category: 'مشروبات',
        gi: 46,
        ii: 68,
        nutrition: {
            calories: 53,
            protein: 0.4,
            carbs: 13,
            fat: 0.1,
            fiber: 0.3
        }
    },
    {
        id: 162,
        name: 'عصير مانجو',
        nameEn: 'Mango Juice',
        icon: '🥭',
        category: 'مشروبات',
        gi: 55,
        ii: 60,
        nutrition: {
            calories: 60,
            protein: 0.4,
            carbs: 15,
            fat: 0.2,
            fiber: 0.4
        }
    },
    {
        id: 163,
        name: 'عصير جوافة',
        nameEn: 'Guava Juice',
        icon: '🍐',
        category: 'مشروبات',
        gi: 31,
        ii: 48,
        nutrition: {
            calories: 56,
            protein: 0.5,
            carbs: 14,
            fat: 0.2,
            fiber: 0.3
        }
    },
    {
        id: 164,
        name: 'عصير رمان',
        nameEn: 'Pomegranate Juice',
        icon: '🍎',
        category: 'مشروبات',
        gi: 53,
        ii: 58,
        nutrition: {
            calories: 54,
            protein: 0.4,
            carbs: 13,
            fat: 0.3,
            fiber: 0.1
        }
    },
    {
        id: 165,
        name: 'سموذي فراولة وموز',
        nameEn: 'Strawberry Banana Smoothie',
        icon: '🥤',
        category: 'مشروبات',
        gi: 44,
        ii: 62,
        nutrition: {
            calories: 88,
            protein: 2.5,
            carbs: 18,
            fat: 1.2,
            fiber: 2
        }
    },
    {
        id: 166,
        name: 'حليب شوكولاتة',
        nameEn: 'Chocolate Milk',
        icon: '🥛',
        category: 'مشروبات',
        gi: 42,
        ii: 63,
        nutrition: {
            calories: 83,
            protein: 3.2,
            carbs: 13,
            fat: 2.5,
            fiber: 0.8
        }
    },
    {
        id: 167,
        name: 'كاكاو ساخن',
        nameEn: 'Hot Chocolate',
        icon: '☕',
        category: 'مشروبات',
        gi: 51,
        ii: 55,
        nutrition: {
            calories: 193,
            protein: 9,
            carbs: 27,
            fat: 6,
            fiber: 2.5
        }
    },
    {
        id: 168,
        name: 'كوكا كولا',
        nameEn: 'Coca Cola',
        icon: '🥤',
        category: 'مشروبات',
        gi: 63,
        ii: 70,
        nutrition: {
            calories: 42,
            protein: 0,
            carbs: 11,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 169,
        name: 'بيبسي',
        nameEn: 'Pepsi',
        icon: '🥤',
        category: 'مشروبات',
        gi: 63,
        ii: 70,
        nutrition: {
            calories: 41,
            protein: 0,
            carbs: 11,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 170,
        name: 'سفن أب',
        nameEn: '7Up',
        icon: '🥤',
        category: 'مشروبات',
        gi: 59,
        ii: 68,
        nutrition: {
            calories: 38,
            protein: 0,
            carbs: 10,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 171,
        name: 'ماء جوز الهند',
        nameEn: 'Coconut Water',
        icon: '🥥',
        category: 'مشروبات',
        gi: 54,
        ii: 45,
        nutrition: {
            calories: 19,
            protein: 0.7,
            carbs: 3.7,
            fat: 0.2,
            fiber: 1.1
        }
    },
    {
        id: 172,
        name: 'مياه معدنية',
        nameEn: 'Mineral Water',
        icon: '💧',
        category: 'مشروبات',
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 0,
            protein: 0,
            carbs: 0,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 173,
        name: 'قهوة فرابتشينو',
        nameEn: 'Frappuccino',
        icon: '☕',
        category: 'مشروبات',
        gi: 58,
        ii: 65,
        nutrition: {
            calories: 240,
            protein: 4,
            carbs: 42,
            fat: 6,
            fiber: 0
        }
    },
    {
        id: 174,
        name: 'عصير قصب',
        nameEn: 'Sugarcane Juice',
        icon: '🥤',
        category: 'مشروبات',
        gi: 43,
        ii: 72,
        nutrition: {
            calories: 69,
            protein: 0.2,
            carbs: 18,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 175,
        name: 'سحلب',
        nameEn: 'Sahlab',
        icon: '🥛',
        category: 'مشروبات',
        gi: 62,
        ii: 68,
        nutrition: {
            calories: 148,
            protein: 3.5,
            carbs: 24,
            fat: 4,
            fiber: 0.5
        }
    },
    // وجبات مطاعم - ماكدونالدز
    {
        id: 176,
        name: 'بيج ماك',
        nameEn: 'Big Mac',
        icon: '🍔',
        category: 'مطاعم',
        gi: 55,
        ii: 72,
        nutrition: {
            calories: 563,
            protein: 26,
            carbs: 46,
            fat: 33,
            fiber: 3.2
        }
    },
    {
        id: 177,
        name: 'ماك تشيكن',
        nameEn: 'McChicken',
        icon: '🍔',
        category: 'مطاعم',
        gi: 52,
        ii: 68,
        nutrition: {
            calories: 410,
            protein: 15,
            carbs: 42,
            fat: 21,
            fiber: 2
        }
    },
    {
        id: 178,
        name: 'تشيز برجر',
        nameEn: 'Cheeseburger',
        icon: '🍔',
        category: 'مطاعم',
        gi: 53,
        ii: 70,
        nutrition: {
            calories: 300,
            protein: 15,
            carbs: 33,
            fat: 12,
            fiber: 1.5
        }
    },
    {
        id: 179,
        name: 'بطاطس ماكدونالدز وسط',
        nameEn: 'McDonalds Medium Fries',
        icon: '🍟',
        category: 'مطاعم',
        gi: 75,
        ii: 89,
        nutrition: {
            calories: 340,
            protein: 4,
            carbs: 44,
            fat: 16,
            fiber: 4
        }
    },
    {
        id: 180,
        name: 'تشيكن ناجتس (6 قطع)',
        nameEn: 'Chicken Nuggets (6pc)',
        icon: '🍗',
        category: 'مطاعم',
        gi: 46,
        ii: 55,
        nutrition: {
            calories: 270,
            protein: 16,
            carbs: 16,
            fat: 17,
            fiber: 1
        }
    },
    {
        id: 181,
        name: 'فيليه أو فيش',
        nameEn: 'Filet-O-Fish',
        icon: '🍔',
        category: 'مطاعم',
        gi: 54,
        ii: 66,
        nutrition: {
            calories: 390,
            protein: 15,
            carbs: 39,
            fat: 19,
            fiber: 2
        }
    },
    {
        id: 182,
        name: 'ماك فلوري أوريو',
        nameEn: 'McFlurry Oreo',
        icon: '🍦',
        category: 'مطاعم',
        gi: 62,
        ii: 70,
        nutrition: {
            calories: 340,
            protein: 9,
            carbs: 53,
            fat: 11,
            fiber: 1
        }
    },
    // وجبات مطاعم - KFC
    {
        id: 183,
        name: 'دجاج KFC أصلي (قطعة)',
        nameEn: 'KFC Original Chicken',
        icon: '🍗',
        category: 'مطاعم',
        gi: 20,
        ii: 52,
        nutrition: {
            calories: 320,
            protein: 29,
            carbs: 10,
            fat: 18,
            fiber: 1
        }
    },
    {
        id: 184,
        name: 'دجاج KFC حار (قطعة)',
        nameEn: 'KFC Hot & Crispy',
        icon: '🍗',
        category: 'مطاعم',
        gi: 22,
        ii: 54,
        nutrition: {
            calories: 350,
            protein: 30,
            carbs: 12,
            fat: 21,
            fiber: 1.2
        }
    },
    {
        id: 185,
        name: 'زينجر KFC',
        nameEn: 'KFC Zinger',
        icon: '🍔',
        category: 'مطاعم',
        gi: 54,
        ii: 70,
        nutrition: {
            calories: 545,
            protein: 28,
            carbs: 52,
            fat: 25,
            fiber: 2.5
        }
    },
    {
        id: 186,
        name: 'تويستر KFC',
        nameEn: 'KFC Twister',
        icon: '🌯',
        category: 'مطاعم',
        gi: 52,
        ii: 68,
        nutrition: {
            calories: 470,
            protein: 22,
            carbs: 45,
            fat: 22,
            fiber: 3
        }
    },
    {
        id: 187,
        name: 'بطاطس كول سلو KFC',
        nameEn: 'KFC Coleslaw',
        icon: '🥗',
        category: 'مطاعم',
        gi: 15,
        ii: 22,
        nutrition: {
            calories: 170,
            protein: 1.5,
            carbs: 14,
            fat: 12,
            fiber: 2
        }
    },
    {
        id: 188,
        name: 'بسكويت KFC',
        nameEn: 'KFC Biscuit',
        icon: '🥐',
        category: 'مطاعم',
        gi: 70,
        ii: 65,
        nutrition: {
            calories: 180,
            protein: 3,
            carbs: 20,
            fat: 10,
            fiber: 0.5
        }
    },
    // وجبات مطاعم - بيتزا هت
    {
        id: 189,
        name: 'بيتزا مارجريتا (شريحة)',
        nameEn: 'Margherita Pizza',
        icon: '🍕',
        category: 'مطاعم',
        gi: 60,
        ii: 68,
        nutrition: {
            calories: 250,
            protein: 11,
            carbs: 32,
            fat: 9,
            fiber: 2
        }
    },
    {
        id: 190,
        name: 'بيتزا بيبروني (شريحة)',
        nameEn: 'Pepperoni Pizza',
        icon: '🍕',
        category: 'مطاعم',
        gi: 60,
        ii: 70,
        nutrition: {
            calories: 300,
            protein: 13,
            carbs: 33,
            fat: 13,
            fiber: 2
        }
    },
    {
        id: 191,
        name: 'بيتزا سوبر سوبريم (شريحة)',
        nameEn: 'Super Supreme Pizza',
        icon: '🍕',
        category: 'مطاعم',
        gi: 58,
        ii: 72,
        nutrition: {
            calories: 340,
            protein: 15,
            carbs: 34,
            fat: 16,
            fiber: 2.5
        }
    },
    {
        id: 192,
        name: 'بيتزا أربع أجبان (شريحة)',
        nameEn: 'Four Cheese Pizza',
        icon: '🍕',
        category: 'مطاعم',
        gi: 58,
        ii: 75,
        nutrition: {
            calories: 310,
            protein: 14,
            carbs: 32,
            fat: 14,
            fiber: 2
        }
    },
    {
        id: 193,
        name: 'أصابع الموزاريلا',
        nameEn: 'Mozzarella Sticks',
        icon: '🧀',
        category: 'مطاعم',
        gi: 50,
        ii: 58,
        nutrition: {
            calories: 280,
            protein: 12,
            carbs: 24,
            fat: 15,
            fiber: 1
        }
    },
    {
        id: 194,
        name: 'أجنحة دجاج حارة (6 قطع)',
        nameEn: 'Hot Wings (6pc)',
        icon: '🍗',
        category: 'مطاعم',
        gi: 18,
        ii: 52,
        nutrition: {
            calories: 480,
            protein: 48,
            carbs: 12,
            fat: 27,
            fiber: 1
        }
    },
    // وجبات مطاعم - صب واي
    {
        id: 195,
        name: 'صب واي دجاج تيرياكي',
        nameEn: 'Subway Chicken Teriyaki',
        icon: '🥖',
        category: 'مطاعم',
        gi: 52,
        ii: 62,
        nutrition: {
            calories: 360,
            protein: 24,
            carbs: 54,
            fat: 5,
            fiber: 5
        }
    },
    {
        id: 196,
        name: 'صب واي تونا',
        nameEn: 'Subway Tuna',
        icon: '🥖',
        category: 'مطاعم',
        gi: 48,
        ii: 55,
        nutrition: {
            calories: 480,
            protein: 20,
            carbs: 46,
            fat: 25,
            fiber: 4
        }
    },
    {
        id: 197,
        name: 'صب واي ستيك وجبنة',
        nameEn: 'Subway Steak & Cheese',
        icon: '🥖',
        category: 'مطاعم',
        gi: 50,
        ii: 65,
        nutrition: {
            calories: 380,
            protein: 24,
            carbs: 48,
            fat: 10,
            fiber: 5
        }
    },
    {
        id: 198,
        name: 'صب واي خضار',
        nameEn: 'Subway Veggie Delite',
        icon: '🥖',
        category: 'مطاعم',
        gi: 44,
        ii: 38,
        nutrition: {
            calories: 230,
            protein: 8,
            carbs: 44,
            fat: 2.5,
            fiber: 5
        }
    },
    // وجبات مطاعم - برجر كنج
    {
        id: 199,
        name: 'ووبر',
        nameEn: 'Whopper',
        icon: '🍔',
        category: 'مطاعم',
        gi: 54,
        ii: 70,
        nutrition: {
            calories: 657,
            protein: 28,
            carbs: 49,
            fat: 40,
            fiber: 2
        }
    },
    {
        id: 200,
        name: 'تشيكن رويال',
        nameEn: 'Chicken Royale',
        icon: '🍔',
        category: 'مطاعم',
        gi: 52,
        ii: 68,
        nutrition: {
            calories: 690,
            protein: 27,
            carbs: 54,
            fat: 42,
            fiber: 3
        }
    },
    // المزيد من المعلبات والمصنعات
    {
        id: 201,
        name: 'تونة معلبة في ماء',
        nameEn: 'Canned Tuna in Water',
        icon: '🥫',
        category: 'معلبات',
        gi: 0,
        ii: 26,
        nutrition: {
            calories: 116,
            protein: 26,
            carbs: 0,
            fat: 0.8,
            fiber: 0
        }
    },
    {
        id: 202,
        name: 'تونة معلبة في زيت',
        nameEn: 'Canned Tuna in Oil',
        icon: '🥫',
        category: 'معلبات',
        gi: 0,
        ii: 28,
        nutrition: {
            calories: 198,
            protein: 29,
            carbs: 0,
            fat: 8,
            fiber: 0
        }
    },
    {
        id: 203,
        name: 'سردين معلب',
        nameEn: 'Canned Sardines',
        icon: '🥫',
        category: 'معلبات',
        gi: 0,
        ii: 30,
        nutrition: {
            calories: 208,
            protein: 25,
            carbs: 0,
            fat: 11,
            fiber: 0
        }
    },
    {
        id: 204,
        name: 'ذرة حلوة معلبة',
        nameEn: 'Canned Sweet Corn',
        icon: '🥫',
        category: 'معلبات',
        gi: 46,
        ii: 52,
        nutrition: {
            calories: 86,
            protein: 2.7,
            carbs: 19,
            fat: 0.7,
            fiber: 2.4
        }
    },
    {
        id: 205,
        name: 'فاصوليا بيضاء معلبة',
        nameEn: 'Canned White Beans',
        icon: '🥫',
        category: 'معلبات',
        gi: 38,
        ii: 40,
        nutrition: {
            calories: 114,
            protein: 7.3,
            carbs: 21,
            fat: 0.3,
            fiber: 6.3
        }
    },
    {
        id: 206,
        name: 'فول مدمس معلب',
        nameEn: 'Canned Fava Beans',
        icon: '🥫',
        category: 'معلبات',
        gi: 40,
        ii: 57,
        nutrition: {
            calories: 110,
            protein: 7.6,
            carbs: 19,
            fat: 0.4,
            fiber: 5.4
        }
    },
    {
        id: 207,
        name: 'حمص معلب',
        nameEn: 'Canned Chickpeas',
        icon: '🥫',
        category: 'معلبات',
        gi: 28,
        ii: 42,
        nutrition: {
            calories: 134,
            protein: 7.3,
            carbs: 22,
            fat: 2.1,
            fiber: 6.2
        }
    },
    {
        id: 208,
        name: 'زيتون أخضر',
        nameEn: 'Green Olives',
        icon: '🫒',
        category: 'معلبات',
        gi: 15,
        ii: 15,
        nutrition: {
            calories: 145,
            protein: 1,
            carbs: 4,
            fat: 15,
            fiber: 3.3
        }
    },
    {
        id: 209,
        name: 'زيتون أسود',
        nameEn: 'Black Olives',
        icon: '🫒',
        category: 'معلبات',
        gi: 15,
        ii: 15,
        nutrition: {
            calories: 115,
            protein: 0.8,
            carbs: 6,
            fat: 11,
            fiber: 3.2
        }
    },
    {
        id: 210,
        name: 'مخلل خيار',
        nameEn: 'Pickled Cucumber',
        icon: '🥒',
        category: 'معلبات',
        gi: 15,
        ii: 15,
        nutrition: {
            calories: 11,
            protein: 0.3,
            carbs: 2.3,
            fat: 0.2,
            fiber: 1.2
        }
    },
    {
        id: 211,
        name: 'طماطم معلبة',
        nameEn: 'Canned Tomatoes',
        icon: '🥫',
        category: 'معلبات',
        gi: 15,
        ii: 38,
        nutrition: {
            calories: 18,
            protein: 0.9,
            carbs: 4,
            fat: 0.2,
            fiber: 1.2
        }
    },
    {
        id: 212,
        name: 'صلصة طماطم',
        nameEn: 'Tomato Sauce',
        icon: '🥫',
        category: 'معلبات',
        gi: 38,
        ii: 45,
        nutrition: {
            calories: 29,
            protein: 1.2,
            carbs: 6.7,
            fat: 0.2,
            fiber: 1.5
        }
    },
    {
        id: 213,
        name: 'معجون طماطم',
        nameEn: 'Tomato Paste',
        icon: '🥫',
        category: 'معلبات',
        gi: 38,
        ii: 40,
        nutrition: {
            calories: 82,
            protein: 4.3,
            carbs: 19,
            fat: 0.5,
            fiber: 4.1
        }
    },
    {
        id: 214,
        name: 'كاتشب',
        nameEn: 'Ketchup',
        icon: '🍅',
        category: 'معلبات',
        gi: 55,
        ii: 60,
        nutrition: {
            calories: 112,
            protein: 1.2,
            carbs: 27,
            fat: 0.1,
            fiber: 0.3
        }
    },
    {
        id: 215,
        name: 'مايونيز',
        nameEn: 'Mayonnaise',
        icon: '🥫',
        category: 'معلبات',
        gi: 0,
        ii: 5,
        nutrition: {
            calories: 680,
            protein: 1,
            carbs: 1,
            fat: 75,
            fiber: 0
        }
    },
    {
        id: 216,
        name: 'خردل',
        nameEn: 'Mustard',
        icon: '🥫',
        category: 'معلبات',
        gi: 35,
        ii: 35,
        nutrition: {
            calories: 66,
            protein: 4,
            carbs: 6,
            fat: 4,
            fiber: 3
        }
    },
    {
        id: 217,
        name: 'مربى فراولة',
        nameEn: 'Strawberry Jam',
        icon: '🍓',
        category: 'معلبات',
        gi: 51,
        ii: 55,
        nutrition: {
            calories: 278,
            protein: 0.4,
            carbs: 69,
            fat: 0.1,
            fiber: 1.1
        }
    },
    {
        id: 218,
        name: 'زبدة الفول السوداني',
        nameEn: 'Peanut Butter',
        icon: '🥜',
        category: 'معلبات',
        gi: 14,
        ii: 20,
        nutrition: {
            calories: 588,
            protein: 25,
            carbs: 20,
            fat: 50,
            fiber: 6
        }
    },
    {
        id: 219,
        name: 'نوتيلا',
        nameEn: 'Nutella',
        icon: '🍫',
        category: 'معلبات',
        gi: 33,
        ii: 40,
        nutrition: {
            calories: 539,
            protein: 6.3,
            carbs: 57,
            fat: 31,
            fiber: 3.4
        }
    },
    {
        id: 220,
        name: 'شوربة دجاج معلبة',
        nameEn: 'Canned Chicken Soup',
        icon: '🥫',
        category: 'معلبات',
        gi: 38,
        ii: 45,
        nutrition: {
            calories: 65,
            protein: 4,
            carbs: 8,
            fat: 2,
            fiber: 0.5
        }
    },
    // وجبات خفيفة ومسليات
    {
        id: 221,
        name: 'شيبس بطاطس',
        nameEn: 'Potato Chips',
        icon: '🥔',
        category: 'وجبات خفيفة',
        gi: 54,
        ii: 61,
        nutrition: {
            calories: 536,
            protein: 6.6,
            carbs: 53,
            fat: 34,
            fiber: 4.8
        }
    },
    {
        id: 222,
        name: 'بوبكورن',
        nameEn: 'Popcorn',
        icon: '🍿',
        category: 'وجبات خفيفة',
        gi: 72,
        ii: 54,
        nutrition: {
            calories: 387,
            protein: 12,
            carbs: 78,
            fat: 4.5,
            fiber: 15
        }
    },
    {
        id: 223,
        name: 'بسكويت سادة',
        nameEn: 'Plain Biscuits',
        icon: '🍪',
        category: 'وجبات خفيفة',
        gi: 70,
        ii: 66,
        nutrition: {
            calories: 502,
            protein: 6.5,
            carbs: 63,
            fat: 25,
            fiber: 2.1
        }
    },
    {
        id: 224,
        name: 'بسكويت شوكولاتة',
        nameEn: 'Chocolate Biscuits',
        icon: '🍪',
        category: 'وجبات خفيفة',
        gi: 55,
        ii: 62,
        nutrition: {
            calories: 524,
            protein: 6.2,
            carbs: 64,
            fat: 27,
            fiber: 2.8
        }
    },
    {
        id: 225,
        name: 'كراكرز',
        nameEn: 'Crackers',
        icon: '🍘',
        category: 'وجبات خفيفة',
        gi: 74,
        ii: 65,
        nutrition: {
            calories: 430,
            protein: 9,
            carbs: 70,
            fat: 11,
            fiber: 3
        }
    },
    {
        id: 226,
        name: 'كورن فليكس حلو',
        nameEn: 'Sweet Corn Flakes',
        icon: '🥣',
        category: 'وجبات خفيفة',
        gi: 81,
        ii: 75,
        nutrition: {
            calories: 357,
            protein: 7.5,
            carbs: 84,
            fat: 0.9,
            fiber: 3.3
        }
    },
    {
        id: 227,
        name: 'جرانولا',
        nameEn: 'Granola',
        icon: '🥣',
        category: 'وجبات خفيفة',
        gi: 47,
        ii: 50,
        nutrition: {
            calories: 471,
            protein: 10.3,
            carbs: 64,
            fat: 20,
            fiber: 7.5
        }
    },
    {
        id: 228,
        name: 'بار بروتين',
        nameEn: 'Protein Bar',
        icon: '🍫',
        category: 'وجبات خفيفة',
        gi: 30,
        ii: 40,
        nutrition: {
            calories: 390,
            protein: 20,
            carbs: 40,
            fat: 14,
            fiber: 10
        }
    },
    {
        id: 229,
        name: 'بار الطاقة',
        nameEn: 'Energy Bar',
        icon: '🍫',
        category: 'وجبات خفيفة',
        gi: 65,
        ii: 70,
        nutrition: {
            calories: 420,
            protein: 8,
            carbs: 60,
            fat: 16,
            fiber: 4
        }
    },
    {
        id: 230,
        name: 'دبس التمر',
        nameEn: 'Date Syrup',
        icon: '🫐',
        category: 'سكريات',
        gi: 68,
        ii: 75,
        nutrition: {
            calories: 287,
            protein: 1.8,
            carbs: 75,
            fat: 0.2,
            fiber: 3
        }
    },
    {
        id: 231,
        name: 'سكر أبيض',
        nameEn: 'White Sugar',
        icon: '🧂',
        category: 'سكريات',
        gi: 65,
        ii: 70,
        nutrition: {
            calories: 387,
            protein: 0,
            carbs: 100,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 232,
        name: 'سكر بني',
        nameEn: 'Brown Sugar',
        icon: '🧂',
        category: 'سكريات',
        gi: 64,
        ii: 68,
            nutrition: {
            calories: 380,
            protein: 0.1,
            carbs: 98,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 233,
        name: 'شراب القيقب',
        nameEn: 'Maple Syrup',
        icon: '🍯',
        category: 'سكريات',
        gi: 54,
        ii: 37,
        nutrition: {
            calories: 260,
            protein: 0,
            carbs: 67,
            fat: 0.1,
            fiber: 0
        }
    },
    {
        id: 234,
        name: 'دبس السكر',
        nameEn: 'Molasses',
        icon: '🍯',
        category: 'سكريات',
        gi: 55,
        ii: 50,
        nutrition: {
            calories: 290,
            protein: 0,
            carbs: 75,
            fat: 0.1,
            fiber: 0
        }
    },
    {
        id: 235,
        name: 'أغاف (شراب الصبار)',
        nameEn: 'Agave Syrup',
        icon: '🍯',
        category: 'سكريات',
        gi: 15,
        ii: 25,
        nutrition: {
            calories: 310,
            protein: 0.1,
            carbs: 76,
            fat: 0,
            fiber: 0.2
        }
    },
    // زيوت ودهون
    {
        id: 236,
        name: 'زيت زيتون',
        nameEn: 'Olive Oil',
        icon: '🫒',
        category: 'زيوت',
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 884,
            protein: 0,
            carbs: 0,
            fat: 100,
            fiber: 0
        }
    },
    {
        id: 237,
        name: 'زيت عباد الشمس',
        nameEn: 'Sunflower Oil',
        icon: '🌻',
        category: 'زيوت',
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 884,
            protein: 0,
            carbs: 0,
            fat: 100,
            fiber: 0
        }
    },
    {
        id: 238,
        name: 'زيت جوز الهند',
        nameEn: 'Coconut Oil',
        icon: '🥥',
        category: 'زيوت',
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 862,
            protein: 0,
            carbs: 0,
            fat: 100,
            fiber: 0
        }
    },
    {
        id: 239,
        name: 'زيت الكانولا',
        nameEn: 'Canola Oil',
        icon: '🌾',
        category: 'زيوت',
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 884,
            protein: 0,
            carbs: 0,
            fat: 100,
            fiber: 0
        }
    },
    {
        id: 240,
        name: 'زيت السمسم',
        nameEn: 'Sesame Oil',
        icon: '🌾',
        category: 'زيوت',
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 884,
            protein: 0,
            carbs: 0,
            fat: 100,
            fiber: 0
        }
    },
    {
        id: 241,
        name: 'سمن بلدي',
        nameEn: 'Ghee',
        icon: '🧈',
        category: 'زيوت',
        gi: 0,
        ii: 7,
        nutrition: {
            calories: 898,
            protein: 0,
            carbs: 0,
            fat: 99.8,
            fiber: 0
        }
    },
    {
        id: 242,
        name: 'زيت أفوكادو',
        nameEn: 'Avocado Oil',
        icon: '🥑',
        category: 'زيوت',
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 884,
            protein: 0,
            carbs: 0,
            fat: 100,
            fiber: 0
        }
    },
    // أطعمة آسيوية
    {
        id: 243,
        name: 'سوشي سلمون',
        nameEn: 'Salmon Sushi',
        icon: '🍣',
        category: 'أطعمة آسيوية',
        gi: 55,
        ii: 60,
        nutrition: {
            calories: 143,
            protein: 6.6,
            carbs: 18,
            fat: 4.5,
            fiber: 0.5
        }
    },
    {
        id: 244,
        name: 'رامن',
        nameEn: 'Ramen',
        icon: '🍜',
        category: 'أطعمة آسيوية',
        gi: 55,
        ii: 62,
        nutrition: {
            calories: 436,
            protein: 13,
            carbs: 56,
            fat: 17,
            fiber: 2.8
        }
    },
    {
        id: 245,
        name: 'نودلز',
        nameEn: 'Noodles',
        icon: '🍜',
        category: 'أطعمة آسيوية',
        gi: 52,
        ii: 58,
        nutrition: {
            calories: 138,
            protein: 4.5,
            carbs: 25,
            fat: 2,
            fiber: 1.2
        }
    },
    {
        id: 246,
        name: 'بات تاي',
        nameEn: 'Pad Thai',
        icon: '🍜',
        category: 'أطعمة آسيوية',
        gi: 50,
        ii: 58,
        nutrition: {
            calories: 354,
            protein: 9,
            carbs: 41,
            fat: 16,
            fiber: 2.5
        }
    },
    {
        id: 247,
        name: 'دجاج تيرياكي',
        nameEn: 'Teriyaki Chicken',
        icon: '🍗',
        category: 'أطعمة آسيوية',
        gi: 48,
        ii: 65,
        nutrition: {
            calories: 267,
            protein: 22,
            carbs: 15,
            fat: 13,
            fiber: 0.5
        }
    },
    {
        id: 248,
        name: 'دمبلنج (فطائر صينية)',
        nameEn: 'Dumplings',
        icon: '🥟',
        category: 'أطعمة آسيوية',
        gi: 45,
        ii: 52,
        nutrition: {
            calories: 206,
            protein: 7.5,
            carbs: 23,
            fat: 9,
            fiber: 1.2
        }
    },
    {
        id: 249,
        name: 'سبرنج رول',
        nameEn: 'Spring Rolls',
        icon: '🥙',
        category: 'أطعمة آسيوية',
        gi: 48,
        ii: 55,
        nutrition: {
            calories: 140,
            protein: 4,
            carbs: 19,
            fat: 5.5,
            fiber: 1.8
        }
    },
    {
        id: 250,
        name: 'دجاج كاري',
        nameEn: 'Chicken Curry',
        icon: '🍛',
        category: 'أطعمة آسيوية',
        gi: 45,
        ii: 58,
        nutrition: {
            calories: 277,
            protein: 18,
            carbs: 12,
            fat: 18,
            fiber: 2
        }
    },
    {
        id: 251,
        name: 'توفو',
        nameEn: 'Tofu',
        icon: '🧈',
        category: 'أطعمة آسيوية',
        gi: 15,
        ii: 21,
        nutrition: {
            calories: 76,
            protein: 8,
            carbs: 1.9,
            fat: 4.8,
            fiber: 0.3
        }
    },
    {
        id: 252,
        name: 'أرز مقلي',
        nameEn: 'Fried Rice',
        icon: '🍚',
        category: 'أطعمة آسيوية',
        gi: 68,
        ii: 75,
        nutrition: {
            calories: 163,
            protein: 4.2,
            carbs: 27,
            fat: 4.5,
            fiber: 0.8
        }
    },
    {
        id: 253,
        name: 'ساشيمي',
        nameEn: 'Sashimi',
        icon: '🍣',
        category: 'أطعمة آسيوية',
        gi: 0,
        ii: 59,
        nutrition: {
            calories: 127,
            protein: 20,
            carbs: 0,
            fat: 4.4,
            fiber: 0
        }
    },
    {
        id: 254,
        name: 'ميسو سوب',
        nameEn: 'Miso Soup',
        icon: '🍵',
        category: 'أطعمة آسيوية',
        gi: 25,
        ii: 30,
        nutrition: {
            calories: 40,
            protein: 2.2,
            carbs: 5.5,
            fat: 1.2,
            fiber: 1
        }
    },
    {
        id: 255,
        name: 'بيبيمباب',
        nameEn: 'Bibimbap',
        icon: '🍲',
        category: 'أطعمة آسيوية',
        gi: 52,
        ii: 60,
        nutrition: {
            calories: 490,
            protein: 15,
            carbs: 75,
            fat: 14,
            fiber: 4.5
        }
    },
    // مخبوزات إضافية
    {
        id: 256,
        name: 'كرواسون',
        nameEn: 'Croissant',
        icon: '🥐',
        category: 'مخبوزات',
        gi: 67,
        ii: 74,
        nutrition: {
            calories: 406,
            protein: 8,
            carbs: 46,
            fat: 21,
            fiber: 2.6
        }
    },
    {
        id: 257,
        name: 'بريوش',
        nameEn: 'Brioche',
        icon: '🥐',
        category: 'مخبوزات',
        gi: 70,
        ii: 78,
        nutrition: {
            calories: 378,
            protein: 10,
            carbs: 50,
            fat: 15,
            fiber: 2
        }
    },
    {
        id: 258,
        name: 'باجيت فرنسي',
        nameEn: 'French Baguette',
        icon: '🥖',
        category: 'مخبوزات',
        gi: 75,
        ii: 80,
        nutrition: {
            calories: 274,
            protein: 9,
            carbs: 56,
            fat: 1.6,
            fiber: 2.4
        }
    },
    {
        id: 259,
        name: 'كعك بالسمسم',
        nameEn: 'Sesame Bagel',
        icon: '🥯',
        category: 'مخبوزات',
        gi: 72,
        ii: 68,
        nutrition: {
            calories: 289,
            protein: 11,
            carbs: 56,
            fat: 2.1,
            fiber: 2.3
        }
    },
    {
        id: 260,
        name: 'خبز البيتا',
        nameEn: 'Pita Bread',
        icon: '🫓',
        category: 'مخبوزات',
        gi: 68,
        ii: 57,
        nutrition: {
            calories: 275,
            protein: 9.1,
            carbs: 55,
            fat: 1.2,
            fiber: 2.2
        }
    },
    {
        id: 261,
        name: 'خبز تورتيلا',
        nameEn: 'Tortilla',
        icon: '🌮',
        category: 'مخبوزات',
        gi: 52,
        ii: 55,
        nutrition: {
            calories: 218,
            protein: 5.7,
            carbs: 36,
            fat: 5.6,
            fiber: 2.3
        }
    },
    {
        id: 262,
        name: 'فطيرة السبانخ',
        nameEn: 'Spinach Pie',
        icon: '🥙',
        category: 'مخبوزات',
        gi: 48,
        ii: 55,
        nutrition: {
            calories: 235,
            protein: 6,
            carbs: 26,
            fat: 12,
            fiber: 2.1
        }
    },
    {
        id: 263,
        name: 'فطيرة بالجبنة',
        nameEn: 'Cheese Pie',
        icon: '🥙',
        category: 'مخبوزات',
        gi: 50,
        ii: 65,
        nutrition: {
            calories: 312,
            protein: 12,
            carbs: 28,
            fat: 17,
            fiber: 1.5
        }
    },
    {
        id: 264,
        name: 'فطيرة اللحم',
        nameEn: 'Meat Pie',
        icon: '🥙',
        category: 'مخبوزات',
        gi: 52,
        ii: 68,
        nutrition: {
            calories: 336,
            protein: 15,
            carbs: 30,
            fat: 18,
            fiber: 1.8
        }
    },
    {
        id: 265,
        name: 'سمبوسك',
        nameEn: 'Sambousek',
        icon: '🥟',
        category: 'مخبوزات',
        gi: 48,
        ii: 58,
        nutrition: {
            calories: 298,
            protein: 8,
            carbs: 28,
            fat: 17,
            fiber: 1.5
        }
    },
    {
        id: 266,
        name: 'بوريك تركي',
        nameEn: 'Turkish Borek',
        icon: '🥙',
        category: 'مخبوزات',
        gi: 55,
        ii: 62,
        nutrition: {
            calories: 340,
            protein: 11,
            carbs: 32,
            fat: 19,
            fiber: 2
        }
    },
    {
        id: 267,
        name: 'مناقيش زعتر',
        nameEn: 'Zaatar Manakeesh',
        icon: '🫓',
        category: 'مخبوزات',
        gi: 58,
        ii: 62,
        nutrition: {
            calories: 268,
            protein: 7,
            carbs: 40,
            fat: 9,
            fiber: 3
        }
    },
    {
        id: 268,
        name: 'مناقيش جبنة',
        nameEn: 'Cheese Manakeesh',
        icon: '🫓',
        category: 'مخبوزات',
        gi: 55,
        ii: 70,
        nutrition: {
            calories: 312,
            protein: 13,
            carbs: 38,
            fat: 12,
            fiber: 2.2
        }
    },
    // وجبات إفطار
    {
        id: 269,
        name: 'أومليت بيض',
        nameEn: 'Egg Omelette',
        icon: '🍳',
        category: 'إفطار',
        gi: 0,
        ii: 42,
        nutrition: {
            calories: 154,
            protein: 11,
            carbs: 1.3,
            fat: 12,
            fiber: 0
        }
    },
    {
        id: 270,
        name: 'بيض مقلي',
        nameEn: 'Fried Eggs',
        icon: '🍳',
        category: 'إفطار',
        gi: 0,
        ii: 42,
        nutrition: {
            calories: 196,
            protein: 13.6,
            carbs: 0.8,
            fat: 15,
            fiber: 0
        }
    },
    {
        id: 271,
        name: 'بيض مخفوق',
        nameEn: 'Scrambled Eggs',
        icon: '🍳',
        category: 'إفطار',
        gi: 0,
        ii: 42,
        nutrition: {
            calories: 148,
            protein: 10,
            carbs: 1.2,
            fat: 11,
            fiber: 0
        }
    },
    {
        id: 272,
        name: 'شكشوكة',
        nameEn: 'Shakshuka',
        icon: '🍳',
        category: 'إفطار',
        gi: 15,
        ii: 45,
        nutrition: {
            calories: 167,
            protein: 11,
            carbs: 8,
            fat: 11,
            fiber: 2.1
        }
    },
    {
        id: 273,
        name: 'جرانولا بالحليب',
        nameEn: 'Granola with Milk',
        icon: '🥣',
        category: 'إفطار',
        gi: 45,
        ii: 58,
        nutrition: {
            calories: 380,
            protein: 11,
            carbs: 54,
            fat: 14,
            fiber: 5
        }
    },
    {
        id: 274,
        name: 'فول الصويا بالحليب',
        nameEn: 'Cereal with Milk',
        icon: '🥣',
        category: 'إفطار',
        gi: 55,
        ii: 70,
        nutrition: {
            calories: 232,
            protein: 8.5,
            carbs: 42,
            fat: 3.5,
            fiber: 3
        }
    },
    {
        id: 275,
        name: 'توست فرنسي',
        nameEn: 'French Toast',
        icon: '🍞',
        category: 'إفطار',
        gi: 69,
        ii: 84,
        nutrition: {
            calories: 240,
            protein: 8,
            carbs: 34,
            fat: 8,
            fiber: 1.5
        }
    },
    {
        id: 276,
        name: 'مافن تو توت',
        nameEn: 'Blueberry Muffin',
        icon: '🧁',
        category: 'إفطار',
        gi: 59,
        ii: 65,
        nutrition: {
            calories: 313,
            protein: 5.5,
            carbs: 54,
            fat: 9,
            fiber: 2
        }
    },
    {
        id: 277,
        name: 'توست بالأفوكادو',
        nameEn: 'Avocado Toast',
        icon: '🥑',
        category: 'إفطار',
        gi: 40,
        ii: 45,
        nutrition: {
            calories: 195,
            protein: 6,
            carbs: 23,
            fat: 10,
            fiber: 7
        }
    },
    {
        id: 278,
        name: 'سندويش بيض',
        nameEn: 'Egg Sandwich',
        icon: '🥪',
        category: 'إفطار',
        gi: 50,
        ii: 65,
        nutrition: {
            calories: 310,
            protein: 16,
            carbs: 32,
            fat: 13,
            fiber: 2
        }
    },
    // وجبات منزلية شعبية
    {
        id: 279,
        name: 'شوربة عدس',
        nameEn: 'Lentil Soup',
        icon: '🍲',
        category: 'وجبات منزلية',
        gi: 32,
        ii: 50,
        nutrition: {
            calories: 116,
            protein: 8.6,
            carbs: 19,
            fat: 0.8,
            fiber: 7.8
        }
    },
    {
        id: 280,
        name: 'شوربة دجاج',
        nameEn: 'Chicken Soup',
        icon: '🍲',
        category: 'وجبات منزلية',
        gi: 35,
        ii: 48,
        nutrition: {
            calories: 86,
            protein: 6.7,
            carbs: 8.5,
            fat: 2.9,
            fiber: 0.6
        }
    },
    {
        id: 281,
        name: 'شوربة خضار',
        nameEn: 'Vegetable Soup',
        icon: '🍲',
        category: 'وجبات منزلية',
        gi: 30,
        ii: 35,
        nutrition: {
            calories: 67,
            protein: 2.4,
            carbs: 12,
            fat: 1.5,
            fiber: 2.5
        }
    },
    {
        id: 282,
        name: 'يخنة لحم',
        nameEn: 'Beef Stew',
        icon: '🍲',
        category: 'وجبات منزلية',
        gi: 40,
        ii: 55,
        nutrition: {
            calories: 232,
            protein: 22,
            carbs: 13,
            fat: 11,
            fiber: 2.8
        }
    },
    {
        id: 283,
        name: 'مسقعة',
        nameEn: 'Moussaka',
        icon: '🍆',
        category: 'وجبات منزلية',
        gi: 42,
        ii: 52,
        nutrition: {
            calories: 189,
            protein: 12,
            carbs: 15,
            fat: 10,
            fiber: 3.5
        }
    },
    {
        id: 284,
        name: 'بامية باللحم',
        nameEn: 'Okra with Meat',
        icon: '🫛',
        category: 'وجبات منزلية',
        gi: 35,
        ii: 50,
        nutrition: {
            calories: 156,
            protein: 14,
            carbs: 10,
            fat: 7,
            fiber: 3.8
        }
    },
    {
        id: 285,
        name: 'فاصوليا باللحم',
        nameEn: 'Green Beans with Meat',
        icon: '🫛',
        category: 'وجبات منزلية',
        gi: 30,
        ii: 48,
        nutrition: {
            calories: 142,
            protein: 12,
            carbs: 9,
            fat: 6.5,
            fiber: 3.2
        }
    },
    {
        id: 286,
        name: 'كوسا بالحم',
        nameEn: 'Zucchini with Meat',
        icon: '🥒',
        category: 'وجبات منزلية',
        gi: 32,
        ii: 50,
        nutrition: {
            calories: 138,
            protein: 11,
            carbs: 8,
            fat: 7,
            fiber: 2.5
        }
    },
    {
        id: 287,
        name: 'بطاطس محمرة',
        nameEn: 'Roasted Potatoes',
        icon: '🥔',
        category: 'وجبات منزلية',
        gi: 85,
        ii: 98,
        nutrition: {
            calories: 149,
            protein: 2.5,
            carbs: 24,
            fat: 5,
            fiber: 2.2
        }
    },
    {
        id: 288,
        name: 'رز بالشعيرية',
        nameEn: 'Rice with Vermicelli',
        icon: '🍚',
        category: 'وجبات منزلية',
        gi: 68,
        ii: 74,
        nutrition: {
            calories: 158,
            protein: 3.2,
            carbs: 30,
            fat: 2.5,
            fiber: 0.9
        }
    },
    {
        id: 289,
        name: 'مكرونة بالصلصة',
        nameEn: 'Pasta with Sauce',
        icon: '🍝',
        category: 'وجبات منزلية',
        gi: 55,
        ii: 62,
        nutrition: {
            calories: 178,
            protein: 6.4,
            carbs: 31,
            fat: 3.2,
            fiber: 2.5
        }
    },
    {
        id: 290,
        name: 'مكرونة بالبشاميل واللحم',
        nameEn: 'Pasta Bechamel with Meat',
        icon: '🍝',
        category: 'وجبات منزلية',
        gi: 58,
        ii: 70,
        nutrition: {
            calories: 245,
            protein: 14,
            carbs: 24,
            fat: 11,
            fiber: 1.8
        }
    },
    // سلطات
    {
        id: 291,
        name: 'سلطة خضراء',
        nameEn: 'Green Salad',
        icon: '🥗',
        category: 'سلطات',
        gi: 15,
        ii: 15,
        nutrition: {
            calories: 15,
            protein: 1.2,
            carbs: 3,
            fat: 0.2,
            fiber: 1.5
        }
    },
    {
        id: 292,
        name: 'سلطة يونانية',
        nameEn: 'Greek Salad',
        icon: '🥗',
        category: 'سلطات',
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 106,
            protein: 3.2,
            carbs: 7,
            fat: 8,
            fiber: 2.2
        }
    },
    {
        id: 293,
        name: 'سلطة سيزر',
        nameEn: 'Caesar Salad',
        icon: '🥗',
        category: 'سلطات',
        gi: 20,
        ii: 35,
        nutrition: {
            calories: 184,
            protein: 6,
            carbs: 6,
            fat: 16,
            fiber: 2
        }
    },
    {
        id: 294,
        name: 'سلطة جرجير',
        nameEn: 'Arugula Salad',
        icon: '🥗',
        category: 'سلطات',
        gi: 15,
        ii: 15,
        nutrition: {
            calories: 25,
            protein: 2.6,
            carbs: 3.7,
            fat: 0.7,
            fiber: 1.6
        }
    },
    {
        id: 295,
        name: 'سلطة كول سلو',
        nameEn: 'Coleslaw',
        icon: '🥗',
        category: 'سلطات',
        gi: 15,
        ii: 22,
        nutrition: {
            calories: 152,
            protein: 1.4,
            carbs: 11,
            fat: 12,
            fiber: 2.3
        }
    },
    {
        id: 296,
        name: 'سلطة بنجر',
        nameEn: 'Beet Salad',
        icon: '🥗',
        category: 'سلطات',
        gi: 64,
        ii: 48,
        nutrition: {
            calories: 75,
            protein: 2.3,
            carbs: 13,
            fat: 2,
            fiber: 3
        }
    },
    {
        id: 297,
        name: 'سلطة بطاطس',
        nameEn: 'Potato Salad',
        icon: '🥗',
        category: 'سلطات',
        gi: 56,
        ii: 62,
        nutrition: {
            calories: 143,
            protein: 2.6,
            carbs: 17,
            fat: 7.5,
            fiber: 1.6
        }
    },
    {
        id: 298,
        name: 'سلطة تونة',
        nameEn: 'Tuna Salad',
        icon: '🥗',
        category: 'سلطات',
        gi: 15,
        ii: 35,
        nutrition: {
            calories: 187,
            protein: 16,
            carbs: 3,
            fat: 13,
            fiber: 0.8
        }
    },
    {
        id: 299,
        name: 'سلطة دجاج',
        nameEn: 'Chicken Salad',
        icon: '🥗',
        category: 'سلطات',
        gi: 15,
        ii: 42,
        nutrition: {
            calories: 201,
            protein: 18,
            carbs: 4,
            fat: 13,
            fiber: 1.2
        }
    },
    {
        id: 300,
        name: 'سلطة باستا',
        nameEn: 'Pasta Salad',
        icon: '🥗',
        category: 'سلطات',
        gi: 48,
        ii: 52,
        nutrition: {
            calories: 178,
            protein: 5,
            carbs: 24,
            fat: 7,
            fiber: 2
        }
    },
    // أطعمة مكسيكية
    {
        id: 301,
        name: 'تاكو',
        nameEn: 'Taco',
        icon: '🌮',
        category: 'أطعمة مكسيكية',
        gi: 50,
        ii: 62,
        nutrition: {
            calories: 226,
            protein: 12,
            carbs: 20,
            fat: 11,
            fiber: 3.2
        }
    },
    {
        id: 302,
        name: 'بوريتو',
        nameEn: 'Burrito',
        icon: '🌯',
        category: 'أطعمة مكسيكية',
        gi: 52,
        ii: 65,
        nutrition: {
            calories: 404,
            protein: 18,
            carbs: 48,
            fat: 15,
            fiber: 6
        }
    },
    {
        id: 303,
        name: 'كويساديلا',
        nameEn: 'Quesadilla',
        icon: '🫔',
        category: 'أطعمة مكسيكية',
        gi: 48,
        ii: 58,
        nutrition: {
            calories: 337,
            protein: 14,
            carbs: 32,
            fat: 17,
            fiber: 2.5
        }
    },
    {
        id: 304,
        name: 'ناتشوز',
        nameEn: 'Nachos',
        icon: '🌮',
        category: 'أطعمة مكسيكية',
        gi: 55,
        ii: 60,
        nutrition: {
            calories: 346,
            protein: 9,
            carbs: 36,
            fat: 19,
            fiber: 3
        }
    },
    {
        id: 305,
        name: 'جواكامولي',
        nameEn: 'Guacamole',
        icon: '🥑',
        category: 'أطعمة مكسيكية',
        gi: 15,
        ii: 15,
        nutrition: {
            calories: 150,
            protein: 2,
            carbs: 9,
            fat: 14,
            fiber: 7
        }
    },
    {
        id: 306,
        name: 'سالسا',
        nameEn: 'Salsa',
        icon: '🍅',
        category: 'أطعمة مكسيكية',
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 36,
            protein: 1.5,
            carbs: 8,
            fat: 0.2,
            fiber: 2
        }
    },
    {
        id: 307,
        name: 'فاهيتا دجاج',
        nameEn: 'Chicken Fajitas',
        icon: '🌮',
        category: 'أطعمة مكسيكية',
        gi: 45,
        ii: 58,
        nutrition: {
            calories: 290,
            protein: 24,
            carbs: 28,
            fat: 10,
            fiber: 4
        }
    },
    {
        id: 308,
        name: 'تشيميتشانجا',
        nameEn: 'Chimichanga',
        icon: '🌯',
        category: 'أطعمة مكسيكية',
        gi: 55,
        ii: 68,
        nutrition: {
            calories: 425,
            protein: 17,
            carbs: 42,
            fat: 21,
            fiber: 5
        }
    },
    // أطعمة إيطالية
    {
        id: 309,
        name: 'لازانيا',
        nameEn: 'Lasagna',
        icon: '🍝',
        category: 'أطعمة إيطالية',
        gi: 58,
        ii: 68,
        nutrition: {
            calories: 135,
            protein: 7.3,
            carbs: 13,
            fat: 6,
            fiber: 1.2
        }
    },
    {
        id: 310,
        name: 'كاربونارا',
        nameEn: 'Carbonara',
        icon: '🍝',
        category: 'أطعمة إيطالية',
        gi: 52,
        ii: 65,
        nutrition: {
            calories: 384,
            protein: 17,
            carbs: 37,
            fat: 19,
            fiber: 2
        }
    },
    {
        id: 311,
        name: 'ريزوتو',
        nameEn: 'Risotto',
        icon: '🍚',
        category: 'أطعمة إيطالية',
        gi: 69,
        ii: 75,
        nutrition: {
            calories: 166,
            protein: 4,
            carbs: 28,
            fat: 4.5,
            fiber: 0.6
        }
    },
    {
        id: 312,
        name: 'بولونيز',
        nameEn: 'Bolognese',
        icon: '🍝',
        category: 'أطعمة إيطالية',
        gi: 52,
        ii: 62,
        nutrition: {
            calories: 195,
            protein: 11,
            carbs: 25,
            fat: 6,
            fiber: 2.5
        }
    },
    {
        id: 313,
        name: 'مينيستروني',
        nameEn: 'Minestrone',
        icon: '🍲',
        category: 'أطعمة إيطالية',
        gi: 39,
        ii: 45,
        nutrition: {
            calories: 82,
            protein: 3.8,
            carbs: 13,
            fat: 2,
            fiber: 3.2
        }
    },
    {
        id: 314,
        name: 'كالزوني',
        nameEn: 'Calzone',
        icon: '🥙',
        category: 'أطعمة إيطالية',
        gi: 58,
        ii: 68,
        nutrition: {
            calories: 364,
            protein: 16,
            carbs: 42,
            fat: 14,
            fiber: 2.8
        }
    },
    {
        id: 315,
        name: 'برسكيتا',
        nameEn: 'Bruschetta',
        icon: '🥖',
        category: 'أطعمة إيطالية',
        gi: 55,
        ii: 58,
        nutrition: {
            calories: 143,
            protein: 4,
            carbs: 20,
            fat: 5,
            fiber: 2
        }
    },
    {
        id: 316,
        name: 'كابريزي',
        nameEn: 'Caprese',
        icon: '🍅',
        category: 'أطعمة إيطالية',
        gi: 15,
        ii: 35,
        nutrition: {
            calories: 150,
            protein: 8,
            carbs: 4,
            fat: 12,
            fiber: 1
        }
    },
    {
        id: 317,
        name: 'جنوكي',
        nameEn: 'Gnocchi',
        icon: '🍝',
        category: 'أطعمة إيطالية',
        gi: 68,
        ii: 72,
        nutrition: {
            calories: 130,
            protein: 3.2,
            carbs: 28,
            fat: 0.5,
            fiber: 1.5
        }
    },
    // حلويات شرقية إضافية
    {
        id: 318,
        name: 'زلابية',
        nameEn: 'Zalabya',
        icon: '🍩',
        category: 'حلويات',
        gi: 75,
        ii: 80,
        nutrition: {
            calories: 338,
            protein: 4.5,
            carbs: 47,
            fat: 15,
            fiber: 1.2
        }
    },
    {
        id: 319,
        name: 'عوامة',
        nameEn: 'Awameh',
        icon: '🍩',
        category: 'حلويات',
        gi: 74,
        ii: 78,
        nutrition: {
            calories: 325,
            protein: 4,
            carbs: 45,
            fat: 14,
            fiber: 1
        }
    },
    {
        id: 320,
        name: 'حلاوة طحينية',
        nameEn: 'Halva',
        icon: '🍫',
        category: 'حلويات',
        gi: 35,
        ii: 42,
        nutrition: {
            calories: 469,
            protein: 13,
            carbs: 58,
            fat: 21,
            fiber: 3.5
        }
    },
    {
        id: 321,
        name: 'مبروشة',
        nameEn: 'Mabrouma',
        icon: '🥐',
        category: 'حلويات',
        gi: 68,
        ii: 74,
        nutrition: {
            calories: 392,
            protein: 5.8,
            carbs: 48,
            fat: 20,
            fiber: 2
        }
    },
    {
        id: 322,
        name: 'قطايف بالقشطة',
        nameEn: 'Qatayef with Cream',
        icon: '🥞',
        category: 'حلويات',
        gi: 65,
        ii: 75,
        nutrition: {
            calories: 285,
            protein: 5.5,
            carbs: 38,
            fat: 13,
            fiber: 1.5
        }
    },
    {
        id: 323,
        name: 'رز بحليب',
        nameEn: 'Rice Pudding',
        icon: '🍮',
        category: 'حلويات',
        gi: 65,
        ii: 72,
        nutrition: {
            calories: 133,
            protein: 3.2,
            carbs: 23,
            fat: 3.3,
            fiber: 0.3
        }
    },
    {
        id: 324,
        name: 'بودينغ شوكولاتة',
        nameEn: 'Chocolate Pudding',
        icon: '🍮',
        category: 'حلويات',
        gi: 47,
        ii: 55,
        nutrition: {
            calories: 158,
            protein: 3.6,
            carbs: 25,
            fat: 5.4,
            fiber: 0.8
        }
    },
    {
        id: 325,
        name: 'بودينغ فانيليا',
        nameEn: 'Vanilla Pudding',
        icon: '🍮',
        category: 'حلويات',
        gi: 62,
        ii: 68,
        nutrition: {
            calories: 135,
            protein: 3,
            carbs: 23,
            fat: 3.7,
            fiber: 0
        }
    },
    {
        id: 326,
        name: 'ترايفل',
        nameEn: 'Trifle',
        icon: '🍰',
        category: 'حلويات',
        gi: 58,
        ii: 65,
        nutrition: {
            calories: 246,
            protein: 4.2,
            carbs: 35,
            fat: 11,
            fiber: 1
        }
    },
    {
        id: 327,
        name: 'بسكويت بالشوكولاتة تشيبس',
        nameEn: 'Chocolate Chip Cookies',
        icon: '🍪',
        category: 'حلويات',
        gi: 43,
        ii: 55,
        nutrition: {
            calories: 488,
            protein: 5.6,
            carbs: 68,
            fat: 22,
            fiber: 2.3
        }
    },
    {
        id: 328,
        name: 'كوكيز السكر',
        nameEn: 'Sugar Cookies',
        icon: '🍪',
        category: 'حلويات',
        gi: 72,
        ii: 65,
        nutrition: {
            calories: 466,
            protein: 5.5,
            carbs: 72,
            fat: 18,
            fiber: 0.9
        }
    },
    {
        id: 329,
        name: 'كب كيك',
        nameEn: 'Cupcake',
        icon: '🧁',
        category: 'حلويات',
        gi: 68,
        ii: 72,
        nutrition: {
            calories: 305,
            protein: 3.6,
            carbs: 46,
            fat: 13,
            fiber: 0.7
        }
    },
    {
        id: 330,
        name: 'ماكرون',
        nameEn: 'Macaron',
        icon: '🍪',
        category: 'حلويات',
        gi: 60,
        ii: 55,
        nutrition: {
            calories: 403,
            protein: 8.2,
            carbs: 62,
            fat: 14,
            fiber: 2.8
        }
    },
    // مشروبات طاقة ورياضية
    {
        id: 331,
        name: 'ريد بول',
        nameEn: 'Red Bull',
        icon: '🥤',
        category: 'مشروبات',
        gi: 65,
        ii: 70,
        nutrition: {
            calories: 45,
            protein: 0.4,
            carbs: 11,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 332,
        name: 'باور ريد',
        nameEn: 'Powerade',
        icon: '🥤',
        category: 'مشروبات',
        gi: 78,
        ii: 75,
        nutrition: {
            calories: 32,
            protein: 0,
            carbs: 8,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 333,
        name: 'جاتوريد',
        nameEn: 'Gatorade',
        icon: '🥤',
        category: 'مشروبات',
        gi: 78,
        ii: 72,
        nutrition: {
            calories: 25,
            protein: 0,
            carbs: 6,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 334,
        name: 'بروتين شيك شوكولاتة',
        nameEn: 'Chocolate Protein Shake',
        icon: '🥤',
        category: 'مشروبات',
        gi: 30,
        ii: 45,
        nutrition: {
            calories: 160,
            protein: 20,
            carbs: 10,
            fat: 5,
            fiber: 1
        }
    },
    {
        id: 335,
        name: 'حليب بالشوكولاتة الساخنة',
        nameEn: 'Hot Chocolate Milk',
        icon: '☕',
        category: 'مشروبات',
        gi: 51,
        ii: 55,
        nutrition: {
            calories: 193,
            protein: 9,
            carbs: 27,
            fat: 6,
            fiber: 2.5
        }
    },
    // مكملات وأطعمة صحية
    {
        id: 336,
        name: 'أفوكادو',
        nameEn: 'Avocado',
        icon: '🥑',
        category: 'فواكه',
        gi: 15,
        ii: 10,
        nutrition: {
            calories: 160,
            protein: 2,
            carbs: 9,
            fat: 15,
            fiber: 7
        }
    },
    {
        id: 337,
        name: 'كيل (ملفوف أجعد)',
        nameEn: 'Kale',
        icon: '🥬',
        category: 'خضروات',
        gi: 15,
        ii: 15,
        nutrition: {
            calories: 49,
            protein: 4.3,
            carbs: 9,
            fat: 0.9,
            fiber: 3.6
        }
    },
    {
        id: 338,
        name: 'سبيرولينا',
        nameEn: 'Spirulina',
        icon: '🌾',
        category: 'مكملات',
        gi: 15,
        ii: 18,
        nutrition: {
            calories: 290,
            protein: 57,
            carbs: 24,
            fat: 8,
            fiber: 3.6
        }
    },
    {
        id: 339,
        name: 'بروتين مصل اللبن',
        nameEn: 'Whey Protein',
        icon: '🥛',
        category: 'مكملات',
        gi: 15,
        ii: 94,
        nutrition: {
            calories: 385,
            protein: 82,
            carbs: 7,
            fat: 5,
            fiber: 0
        }
    },
    {
        id: 340,
        name: 'كرياتين',
        nameEn: 'Creatine',
        icon: '⚡',
        category: 'مكملات',
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 0,
            protein: 0,
            carbs: 0,
            fat: 0,
            fiber: 0
        }
    },
    // أطعمة متنوعة إضافية
    {
        id: 341,
        name: 'شيبس تورتيلا',
        nameEn: 'Tortilla Chips',
        icon: '🌮',
        category: 'وجبات خفيفة',
        gi: 63,
        ii: 55,
        nutrition: {
            calories: 503,
            protein: 7,
            carbs: 63,
            fat: 25,
            fiber: 5.3
        }
    },
    {
        id: 342,
        name: 'بريتزل',
        nameEn: 'Pretzels',
        icon: '🥨',
        category: 'وجبات خفيفة',
        gi: 83,
        ii: 74,
        nutrition: {
            calories: 380,
            protein: 9.1,
            carbs: 79,
            fat: 2.6,
            fiber: 3.2
        }
    },
    {
        id: 343,
        name: 'فشار بالجبنة',
        nameEn: 'Cheese Popcorn',
        icon: '🍿',
        category: 'وجبات خفيفة',
        gi: 55,
        ii: 62,
        nutrition: {
            calories: 535,
            protein: 9.4,
            carbs: 48,
            fat: 35,
            fiber: 9.2
        }
    },
    {
        id: 344,
        name: 'شيبس بروتين',
        nameEn: 'Protein Chips',
        icon: '🥔',
        category: 'وجبات خفيفة',
        gi: 30,
        ii: 38,
        nutrition: {
            calories: 390,
            protein: 21,
            carbs: 42,
            fat: 14,
            fiber: 5
        }
    },
    {
        id: 345,
        name: 'ترمس',
        nameEn: 'Lupini Beans',
        icon: '🫘',
        category: 'بقوليات',
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 116,
            protein: 15,
            carbs: 10,
            fat: 2.9,
            fiber: 4.8
        }
    },
    {
        id: 346,
        name: 'فول سوداني محمص',
        nameEn: 'Roasted Peanuts',
        icon: '🥜',
        category: 'مكسرات',
        gi: 14,
        ii: 20,
        nutrition: {
            calories: 587,
            protein: 26,
            carbs: 21,
            fat: 50,
            fiber: 8.4
        }
    },
    {
        id: 347,
        name: 'حمص محمص',
        nameEn: 'Roasted Chickpeas',
        icon: '🫘',
        category: 'وجبات خفيفة',
        gi: 28,
        ii: 35,
        nutrition: {
            calories: 364,
            protein: 19,
            carbs: 61,
            fat: 6,
            fiber: 17
        }
    },
    {
        id: 348,
        name: 'لب (بذور القرع)',
        nameEn: 'Roasted Pumpkin Seeds',
        icon: '🎃',
        category: 'مكسرات',
        gi: 25,
        ii: 30,
        nutrition: {
            calories: 446,
            protein: 19,
            carbs: 54,
            fat: 19,
            fiber: 18
        }
    },
    {
        id: 349,
        name: 'لب سوري',
        nameEn: 'Sunflower Seeds',
        icon: '🌻',
        category: 'مكسرات',
        gi: 35,
        ii: 35,
        nutrition: {
            calories: 584,
            protein: 21,
            carbs: 20,
            fat: 51,
            fiber: 8.6
        }
    },
    {
        id: 350,
        name: 'فستق محمص',
        nameEn: 'Roasted Pistachios',
        icon: '🥜',
        category: 'مكسرات',
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 562,
            protein: 20,
            carbs: 28,
            fat: 45,
            fiber: 10.3
        }
    },
    // المزيد من اللحوم والأسماك
    {
        id: 351,
        name: 'برجر لحم',
        nameEn: 'Beef Burger',
        icon: '🍔',
        category: 'بروتين',
        gi: 0,
        ii: 51,
        nutrition: {
            calories: 295,
            protein: 17,
            carbs: 0,
            fat: 25,
            fiber: 0
        }
    },
    {
        id: 352,
        name: 'سجق (نقانق)',
        nameEn: 'Sausage',
        icon: '🌭',
        category: 'بروتين',
        gi: 0,
        ii: 28,
        nutrition: {
            calories: 301,
            protein: 12,
            carbs: 1.8,
            fat: 27,
            fiber: 0
        }
    },
    {
        id: 353,
        name: 'بيبروني',
        nameEn: 'Pepperoni',
        icon: '🍕',
        category: 'بروتين',
        gi: 0,
        ii: 10,
        nutrition: {
            calories: 504,
            protein: 23,
            carbs: 4,
            fat: 44,
            fiber: 0
        }
    },
    {
        id: 354,
        name: 'سلامي',
        nameEn: 'Salami',
        icon: '🥓',
        category: 'بروتين',
        gi: 0,
        ii: 10,
        nutrition: {
            calories: 407,
            protein: 23,
            carbs: 1.6,
            fat: 34,
            fiber: 0
        }
    },
    {
        id: 355,
        name: 'بسطرمة',
        nameEn: 'Pastrami',
        icon: '🥓',
        category: 'بروتين',
        gi: 0,
        ii: 51,
        nutrition: {
            calories: 98,
            protein: 16,
            carbs: 0.9,
            fat: 3.2,
            fiber: 0
        }
    },
    {
        id: 356,
        name: 'لحم مقدد (بيكون)',
        nameEn: 'Bacon',
        icon: '🥓',
        category: 'بروتين',
        gi: 0,
        ii: 9,
        nutrition: {
            calories: 541,
            protein: 37,
            carbs: 1.4,
            fat: 42,
            fiber: 0
        }
    },
    {
        id: 357,
        name: 'هوت دوج',
        nameEn: 'Hot Dog',
        icon: '🌭',
        category: 'بروتين',
        gi: 0,
        ii: 25,
        nutrition: {
            calories: 290,
            protein: 10,
            carbs: 2,
            fat: 26,
            fiber: 0
        }
    },
    {
        id: 358,
        name: 'دجاج مقلي',
        nameEn: 'Fried Chicken',
        icon: '🍗',
        category: 'بروتين',
        gi: 20,
        ii: 58,
        nutrition: {
            calories: 246,
            protein: 19,
            carbs: 8.8,
            fat: 15,
            fiber: 0.5
        }
    },
    {
        id: 359,
        name: 'أجنحة دجاج',
        nameEn: 'Chicken Wings',
        icon: '🍗',
        category: 'بروتين',
        gi: 0,
        ii: 52,
        nutrition: {
            calories: 203,
            protein: 30,
            carbs: 0,
            fat: 8,
            fiber: 0
        }
    },
    {
        id: 360,
        name: 'سمك مشوي بالفرن',
        nameEn: 'Baked Fish',
        icon: '🐟',
        category: 'بروتين',
        gi: 0,
        ii: 59,
        nutrition: {
            calories: 136,
            protein: 22,
            carbs: 0,
            fat: 4.5,
            fiber: 0
        }
    },
    {
        id: 361,
        name: 'سمك مقلي',
        nameEn: 'Fried Fish',
        icon: '🐟',
        category: 'بروتين',
        gi: 15,
        ii: 59,
        nutrition: {
            calories: 232,
            protein: 18,
            carbs: 10,
            fat: 14,
            fiber: 0.5
        }
    },
    {
        id: 362,
        name: 'سمك فيليه',
        nameEn: 'Fish Fillet',
        icon: '🐟',
        category: 'بروتين',
        gi: 0,
        ii: 59,
        nutrition: {
            calories: 110,
            protein: 23,
            carbs: 0,
            fat: 1.5,
            fiber: 0
        }
    },
    {
        id: 363,
        name: 'محار',
        nameEn: 'Oysters',
        icon: '🦪',
        category: 'بروتين',
        gi: 0,
        ii: 45,
        nutrition: {
            calories: 68,
            protein: 7,
            carbs: 3.9,
            fat: 2.5,
            fiber: 0
        }
    },
    {
        id: 364,
        name: 'بلح البحر',
        nameEn: 'Mussels',
        icon: '🦪',
        category: 'بروتين',
        gi: 0,
        ii: 28,
        nutrition: {
            calories: 172,
            protein: 24,
            carbs: 7.4,
            fat: 4.5,
            fiber: 0
        }
    },
    {
        id: 365,
        name: 'سمك الماكريل',
        nameEn: 'Mackerel',
        icon: '🐟',
        category: 'بروتين',
        gi: 0,
        ii: 59,
        nutrition: {
            calories: 205,
            protein: 19,
            carbs: 0,
            fat: 14,
            fiber: 0
        }
    },
    {
        id: 366,
        name: 'سمك البلطي',
        nameEn: 'Tilapia',
        icon: '🐟',
        category: 'بروتين',
        gi: 0,
        ii: 59,
        nutrition: {
            calories: 128,
            protein: 26,
            carbs: 0,
            fat: 2.7,
            fiber: 0
        }
    },
    {
        id: 367,
        name: 'سمك القد',
        nameEn: 'Cod',
        icon: '🐟',
        category: 'بروتين',
        gi: 0,
        ii: 59,
        nutrition: {
            calories: 82,
            protein: 18,
            carbs: 0,
            fat: 0.7,
            fiber: 0
        }
    },
    {
        id: 368,
        name: 'سلطعون',
        nameEn: 'Lobster',
        icon: '🦞',
        category: 'بروتين',
        gi: 0,
        ii: 30,
        nutrition: {
            calories: 89,
            protein: 19,
            carbs: 0,
            fat: 0.9,
            fiber: 0
        }
    },
    // المزيد من الخضروات
    {
        id: 369,
        name: 'هليون',
        nameEn: 'Asparagus',
        icon: '🥒',
        category: 'خضروات',
        gi: 15,
        ii: 16,
        nutrition: {
            calories: 20,
            protein: 2.2,
            carbs: 3.9,
            fat: 0.2,
            fiber: 2.1
        }
    },
    {
        id: 370,
        name: 'بروكسل سبراوت',
        nameEn: 'Brussels Sprouts',
        icon: '🥬',
        category: 'خضروات',
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 43,
            protein: 3.4,
            carbs: 9,
            fat: 0.3,
            fiber: 3.8
        }
    },
    {
        id: 371,
        name: 'كرنب بنفسجي',
        nameEn: 'Red Cabbage',
        icon: '🥬',
        category: 'خضروات',
        gi: 10,
        ii: 10,
        nutrition: {
            calories: 31,
            protein: 1.4,
            carbs: 7.4,
            fat: 0.2,
            fiber: 2.1
        }
    },
    {
        id: 372,
        name: 'كرفس',
        nameEn: 'Celery',
        icon: '🥬',
        category: 'خضروات',
        gi: 15,
        ii: 15,
        nutrition: {
            calories: 14,
            protein: 0.7,
            carbs: 3,
            fat: 0.2,
            fiber: 1.6
        }
    },
    {
        id: 373,
        name: 'كرنب صيني (بوك تشوي)',
        nameEn: 'Bok Choy',
        icon: '🥬',
        category: 'خضروات',
        gi: 10,
        ii: 10,
        nutrition: {
            calories: 13,
            protein: 1.5,
            carbs: 2.2,
            fat: 0.2,
            fiber: 1
        }
    },
    {
        id: 374,
        name: 'شمندر (بنجر)',
        nameEn: 'Beetroot',
        icon: '🥕',
        category: 'خضروات',
        gi: 64,
        ii: 48,
        nutrition: {
            calories: 43,
            protein: 1.6,
            carbs: 10,
            fat: 0.2,
            fiber: 2.8
        }
    },
    {
        id: 375,
        name: 'لفت',
        nameEn: 'Turnip',
        icon: '🥕',
        category: 'خضروات',
        gi: 30,
        ii: 25,
        nutrition: {
            calories: 28,
            protein: 0.9,
            carbs: 6.4,
            fat: 0.1,
            fiber: 1.8
        }
    },
    {
        id: 376,
        name: 'جزر مسلوق',
        nameEn: 'Boiled Carrot',
        icon: '🥕',
        category: 'خضروات',
        gi: 41,
        ii: 60,
        nutrition: {
            calories: 35,
            protein: 0.8,
            carbs: 8.2,
            fat: 0.2,
            fiber: 2.4
        }
    },
    {
        id: 377,
        name: 'بطاطس مهروسة',
        nameEn: 'Mashed Potato',
        icon: '🥔',
        category: 'خضروات',
        gi: 85,
        ii: 121,
        nutrition: {
            calories: 113,
            protein: 2.1,
            carbs: 17,
            fat: 4.2,
            fiber: 1.5
        }
    },
    {
        id: 378,
        name: 'فطر محمر',
        nameEn: 'Sautéed Mushrooms',
        icon: '🍄',
        category: 'خضروات',
        gi: 10,
        ii: 17,
        nutrition: {
            calories: 35,
            protein: 3.3,
            carbs: 3.9,
            fat: 1.2,
            fiber: 1.1
        }
    },
    {
        id: 379,
        name: 'ذرة مشوية',
        nameEn: 'Grilled Corn',
        icon: '🌽',
        category: 'خضروات',
        gi: 55,
        ii: 58,
        nutrition: {
            calories: 96,
            protein: 3.4,
            carbs: 21,
            fat: 1.5,
            fiber: 2.4
        }
    },
    {
        id: 380,
        name: 'باذنجان محشي',
        nameEn: 'Stuffed Eggplant',
        icon: '🍆',
        category: 'خضروات',
        gi: 35,
        ii: 45,
        nutrition: {
            calories: 156,
            protein: 7,
            carbs: 16,
            fat: 7.5,
            fiber: 3.2
        }
    },
    // المزيد من الفواكه المجففة
    {
        id: 381,
        name: 'مشمش مجفف',
        nameEn: 'Dried Apricots',
        icon: '🍑',
        category: 'فواكه',
        gi: 30,
        ii: 42,
        nutrition: {
            calories: 241,
            protein: 3.4,
            carbs: 63,
            fat: 0.5,
            fiber: 7.3
        }
    },
    {
        id: 382,
        name: 'تين مجفف',
        nameEn: 'Dried Figs',
        icon: '🍇',
        category: 'فواكه',
        gi: 61,
        ii: 58,
        nutrition: {
            calories: 249,
            protein: 3.3,
            carbs: 64,
            fat: 0.9,
            fiber: 9.8
        }
    },
    {
        id: 383,
        name: 'خوخ مجفف (برقوق)',
        nameEn: 'Prunes',
        icon: '🍑',
        category: 'فواكه',
        gi: 29,
        ii: 38,
        nutrition: {
            calories: 240,
            protein: 2.2,
            carbs: 64,
            fat: 0.4,
            fiber: 7.1
        }
    },
    {
        id: 384,
        name: 'كرانبري مجفف',
        nameEn: 'Dried Cranberries',
        icon: '🍇',
        category: 'فواكه',
        gi: 62,
        ii: 55,
        nutrition: {
            calories: 308,
            protein: 0.1,
            carbs: 82,
            fat: 1.4,
            fiber: 5.3
        }
    },
    {
        id: 385,
        name: 'موز مجفف',
        nameEn: 'Dried Banana',
        icon: '🍌',
        category: 'فواكه',
        gi: 62,
        ii: 70,
        nutrition: {
            calories: 346,
            protein: 3.9,
            carbs: 88,
            fat: 1.8,
            fiber: 9.9
        }
    },
    {
        id: 386,
        name: 'جوز هند مجفف',
        nameEn: 'Dried Coconut',
        icon: '🥥',
        category: 'فواكه',
        gi: 35,
        ii: 38,
        nutrition: {
            calories: 660,
            protein: 6.9,
            carbs: 24,
            fat: 65,
            fiber: 16.3
        }
    },
    {
        id: 387,
        name: 'قراصيا (برقوق أسود)',
        nameEn: 'Black Plums',
        icon: '🍑',
        category: 'فواكه',
        gi: 24,
        ii: 35,
        nutrition: {
            calories: 240,
            protein: 2.2,
            carbs: 64,
            fat: 0.4,
            fiber: 7.1
        }
    },
    // منتجات الصويا
    {
        id: 388,
        name: 'حليب الصويا',
        nameEn: 'Soy Milk',
        icon: '🥛',
        category: 'ألبان',
        gi: 34,
        ii: 62,
        nutrition: {
            calories: 54,
            protein: 3.3,
            carbs: 6,
            fat: 1.8,
            fiber: 0.6
        }
    },
    {
        id: 389,
        name: 'حليب اللوز',
        nameEn: 'Almond Milk',
        icon: '🥛',
        category: 'ألبان',
        gi: 25,
        ii: 35,
        nutrition: {
            calories: 17,
            protein: 0.6,
            carbs: 1.5,
            fat: 1.1,
            fiber: 0.4
        }
    },
    {
        id: 390,
        name: 'حليب جوز الهند',
        nameEn: 'Coconut Milk',
        icon: '🥛',
        category: 'ألبان',
        gi: 40,
        ii: 35,
        nutrition: {
            calories: 230,
            protein: 2.3,
            carbs: 6,
            fat: 24,
            fiber: 0
        }
    },
    {
        id: 391,
        name: 'حليب الشوفان',
        nameEn: 'Oat Milk',
        icon: '🥛',
        category: 'ألبان',
        gi: 69,
        ii: 55,
        nutrition: {
            calories: 47,
            protein: 1,
            carbs: 8,
            fat: 1.5,
            fiber: 0.8
        }
    },
    {
        id: 392,
        name: 'تمبيه',
        nameEn: 'Tempeh',
        icon: '🫘',
        category: 'بقوليات',
        gi: 15,
        ii: 21,
        nutrition: {
            calories: 193,
            protein: 20,
            carbs: 9.4,
            fat: 11,
            fiber: 0
        }
    },
    {
        id: 393,
        name: 'ميسو',
        nameEn: 'Miso',
        icon: '🫘',
        category: 'بقوليات',
        gi: 34,
        ii: 30,
        nutrition: {
            calories: 199,
            protein: 13,
            carbs: 26,
            fat: 6,
            fiber: 5.4
        }
    },
    // أطعمة هندية
    {
        id: 394,
        name: 'تكا ماسالا',
        nameEn: 'Tikka Masala',
        icon: '🍛',
        category: 'أطعمة آسيوية',
        gi: 45,
        ii: 58,
        nutrition: {
            calories: 204,
            protein: 14,
            carbs: 12,
            fat: 12,
            fiber: 2.5
        }
    },
    {
        id: 395,
        name: 'بالاك بانير',
        nameEn: 'Palak Paneer',
        icon: '🍛',
        category: 'أطعمة آسيوية',
        gi: 30,
        ii: 48,
        nutrition: {
            calories: 220,
            protein: 12,
            carbs: 8,
            fat: 16,
            fiber: 3
        }
    },
    {
        id: 396,
        name: 'بريياني دجاج',
        nameEn: 'Chicken Biryani',
        icon: '🍚',
        category: 'أطعمة آسيوية',
        gi: 58,
        ii: 70,
        nutrition: {
            calories: 356,
            protein: 16,
            carbs: 45,
            fat: 12,
            fiber: 2.2
        }
    },
    {
        id: 397,
        name: 'سمبوسة',
        nameEn: 'Samosa',
        icon: '🥟',
        category: 'أطعمة آسيوية',
        gi: 50,
        ii: 58,
        nutrition: {
            calories: 262,
            protein: 5,
            carbs: 25,
            fat: 16,
            fiber: 2.5
        }
    },
    {
        id: 398,
        name: 'نان (خبز هندي)',
        nameEn: 'Naan Bread',
        icon: '🫓',
        category: 'مخبوزات',
        gi: 71,
        ii: 65,
        nutrition: {
            calories: 262,
            protein: 7.9,
            carbs: 45,
            fat: 5.3,
            fiber: 2.1
        }
    },
    {
        id: 399,
        name: 'تشاباتي',
        nameEn: 'Chapati',
        icon: '🫓',
        category: 'مخبوزات',
        gi: 52,
        ii: 55,
        nutrition: {
            calories: 120,
            protein: 3.6,
            carbs: 25,
            fat: 0.8,
            fiber: 2.8
        }
    },
    {
        id: 400,
        name: 'دال (شوربة عدس هندية)',
        nameEn: 'Dal',
        icon: '🍲',
        category: 'أطعمة آسيوية',
        gi: 32,
        ii: 50,
        nutrition: {
            calories: 104,
            protein: 7.6,
            carbs: 17,
            fat: 0.6,
            fiber: 6.7
        }
    },
    // سندويشات ووجبات سريعة
    {
        id: 401,
        name: 'سندويش فلافل',
        nameEn: 'Falafel Sandwich',
        icon: '🥙',
        category: 'سندويشات',
        gi: 40,
        ii: 52,
        nutrition: {
            calories: 333,
            protein: 13,
            carbs: 44,
            fat: 12,
            fiber: 6
        }
    },
    {
        id: 402,
        name: 'سندويش شاورما لحم',
        nameEn: 'Beef Shawarma Sandwich',
        icon: '🌯',
        category: 'سندويشات',
        gi: 48,
        ii: 62,
        nutrition: {
            calories: 380,
            protein: 26,
            carbs: 35,
            fat: 16,
            fiber: 3
        }
    },
    {
        id: 403,
        name: 'سندويش كفتة',
        nameEn: 'Kofta Sandwich',
        icon: '🥙',
        category: 'سندويشات',
        gi: 45,
        ii: 58,
        nutrition: {
            calories: 395,
            protein: 22,
            carbs: 32,
            fat: 20,
            fiber: 2.5
        }
    },
    {
        id: 404,
        name: 'سندويش دجاج مشوي',
        nameEn: 'Grilled Chicken Sandwich',
        icon: '🥪',
        category: 'سندويشات',
        gi: 48,
        ii: 60,
        nutrition: {
            calories: 320,
            protein: 28,
            carbs: 30,
            fat: 10,
            fiber: 3
        }
    },
    {
        id: 405,
        name: 'سندويش حلومي مشوي',
        nameEn: 'Grilled Halloumi Sandwich',
        icon: '🥪',
        category: 'سندويشات',
        gi: 42,
        ii: 55,
        nutrition: {
            calories: 345,
            protein: 16,
            carbs: 32,
            fat: 18,
            fiber: 3
        }
    },
    {
        id: 406,
        name: 'سندويش بي إل تي',
        nameEn: 'BLT Sandwich',
        icon: '🥪',
        category: 'سندويشات',
        gi: 50,
        ii: 55,
        nutrition: {
            calories: 344,
            protein: 13,
            carbs: 30,
            fat: 20,
            fiber: 2
        }
    },
    {
        id: 407,
        name: 'سندويش كلوب',
        nameEn: 'Club Sandwich',
        icon: '🥪',
        category: 'سندويشات',
        gi: 52,
        ii: 62,
        nutrition: {
            calories: 590,
            protein: 33,
            carbs: 52,
            fat: 28,
            fiber: 4
        }
    },
    {
        id: 408,
        name: 'كباب رول',
        nameEn: 'Kebab Roll',
        icon: '🌯',
        category: 'سندويشات',
        gi: 50,
        ii: 62,
        nutrition: {
            calories: 368,
            protein: 20,
            carbs: 38,
            fat: 15,
            fiber: 3.5
        }
    },
    // وجبات صحية ونباتية
    {
        id: 409,
        name: 'سلطة الكينوا',
        nameEn: 'Quinoa Salad',
        icon: '🥗',
        category: 'سلطات',
        gi: 53,
        ii: 50,
        nutrition: {
            calories: 172,
            protein: 6.3,
            carbs: 25,
            fat: 5.5,
            fiber: 4
        }
    },
    {
        id: 410,
        name: 'بول الأكاي',
        nameEn: 'Acai Bowl',
        icon: '🥣',
        category: 'إفطار',
        gi: 42,
        ii: 48,
        nutrition: {
            calories: 211,
            protein: 3.8,
            carbs: 35,
            fat: 7,
            fiber: 7
        }
    },
    {
        id: 411,
        name: 'سموذي بول',
        nameEn: 'Smoothie Bowl',
        icon: '🥣',
        category: 'إفطار',
        gi: 45,
        ii: 52,
        nutrition: {
            calories: 185,
            protein: 5.5,
            carbs: 32,
            fat: 4.5,
            fiber: 6
        }
    },
    {
        id: 412,
        name: 'برجر نباتي',
        nameEn: 'Veggie Burger',
        icon: '🍔',
        category: 'وجبات منزلية',
        gi: 40,
        ii: 35,
        nutrition: {
            calories: 150,
            protein: 12,
            carbs: 18,
            fat: 4.5,
            fiber: 6
        }
    },
    {
        id: 413,
        name: 'فطائر البروتين',
        nameEn: 'Protein Pancakes',
        icon: '🥞',
        category: 'إفطار',
        gi: 40,
        ii: 58,
        nutrition: {
            calories: 180,
            protein: 15,
            carbs: 22,
            fat: 4,
            fiber: 3
        }
    },
    {
        id: 414,
        name: 'شوفان بالبروتين',
        nameEn: 'Protein Oatmeal',
        icon: '🥣',
        category: 'إفطار',
        gi: 48,
        ii: 52,
        nutrition: {
            calories: 195,
            protein: 12,
            carbs: 28,
            fat: 4,
            fiber: 5
        }
    },
    {
        id: 415,
        name: 'بودينغ الشيا',
        nameEn: 'Chia Pudding',
        icon: '🍮',
        category: 'حلويات',
        gi: 1,
        ii: 10,
        nutrition: {
            calories: 138,
            protein: 4.4,
            carbs: 12,
            fat: 8.6,
            fiber: 10.6
        }
    },
    // المزيد من الأطعمة العربية الشعبية
    {
        id: 416,
        name: 'كسكسي مغربي',
        nameEn: 'Moroccan Couscous',
        icon: '🍲',
        category: 'أطعمة عربية',
        gi: 65,
        ii: 58,
        nutrition: {
            calories: 176,
            protein: 6,
            carbs: 36,
            fat: 0.3,
            fiber: 2.2
        }
    },
    {
        id: 417,
        name: 'طاجين مغربي',
        nameEn: 'Moroccan Tajine',
        icon: '🍲',
        category: 'أطعمة عربية',
        gi: 42,
        ii: 52,
        nutrition: {
            calories: 198,
            protein: 16,
            carbs: 15,
            fat: 9,
            fiber: 3.5
        }
    },
    {
        id: 418,
        name: 'حريرة مغربية',
        nameEn: 'Moroccan Harira',
        icon: '🍲',
        category: 'أطعمة عربية',
        gi: 38,
        ii: 48,
        nutrition: {
            calories: 142,
            protein: 8,
            carbs: 22,
            fat: 3,
            fiber: 5
        }
    },
    {
        id: 419,
        name: 'مسخن فلسطيني',
        nameEn: 'Palestinian Musakhan',
        icon: '🍗',
        category: 'أطعمة عربية',
        gi: 55,
        ii: 65,
        nutrition: {
            calories: 358,
            protein: 22,
            carbs: 38,
            fat: 14,
            fiber: 2.8
        }
    },
    {
        id: 420,
        name: 'مقلوبة',
        nameEn: 'Maqluba',
        icon: '🍲',
        category: 'أطعمة عربية',
        gi: 58,
        ii: 68,
        nutrition: {
            calories: 312,
            protein: 18,
            carbs: 36,
            fat: 11,
            fiber: 3
        }
    },
    {
        id: 421,
        name: 'ورق عنب بالزيت',
        nameEn: 'Grape Leaves with Oil',
        icon: '🍃',
        category: 'أطعمة عربية',
        gi: 48,
        ii: 40,
        nutrition: {
            calories: 158,
            protein: 3,
            carbs: 22,
            fat: 6.5,
            fiber: 2.1
        }
    },
    {
        id: 422,
        name: 'فتة باذنجان',
        nameEn: 'Fatteh Eggplant',
        icon: '🍆',
        category: 'أطعمة عربية',
        gi: 45,
        ii: 55,
        nutrition: {
            calories: 268,
            protein: 10,
            carbs: 28,
            fat: 13,
            fiber: 4.5
        }
    },
    {
        id: 423,
        name: 'شاكرية',
        nameEn: 'Shakriyyeh',
        icon: '🍲',
        category: 'أطعمة عربية',
        gi: 52,
        ii: 68,
        nutrition: {
            calories: 289,
            protein: 20,
            carbs: 18,
            fat: 16,
            fiber: 1.2
        }
    },
    {
        id: 424,
        name: 'مجبوس',
        nameEn: 'Majboos',
        icon: '🍛',
        category: 'أطعمة عربية',
        gi: 58,
        ii: 72,
        nutrition: {
            calories: 295,
            protein: 19,
            carbs: 33,
            fat: 10,
            fiber: 2
        }
    },
    {
        id: 425,
        name: 'هريس',
        nameEn: 'Harees',
        icon: '🍲',
        category: 'أطعمة عربية',
        gi: 55,
        ii: 65,
        nutrition: {
            calories: 178,
            protein: 12,
            carbs: 26,
            fat: 3.5,
            fiber: 2.8
        }
    },
    // المزيد من الحلويات
    {
        id: 426,
        name: 'كريب',
        nameEn: 'Crepe',
        icon: '🥞',
        category: 'حلويات',
        gi: 66,
        ii: 70,
        nutrition: {
            calories: 112,
            protein: 4,
            carbs: 13,
            fat: 5,
            fiber: 0.5
        }
    },
    {
        id: 427,
        name: 'سينابون',
        nameEn: 'Cinnabon',
        icon: '🥐',
        category: 'حلويات',
        gi: 72,
        ii: 78,
        nutrition: {
            calories: 880,
            protein: 13,
            carbs: 127,
            fat: 37,
            fiber: 3
        }
    },
    {
        id: 428,
        name: 'موس شوكولاتة',
        nameEn: 'Chocolate Mousse',
        icon: '🍫',
        category: 'حلويات',
        gi: 34,
        ii: 42,
        nutrition: {
            calories: 189,
            protein: 3.2,
            carbs: 17,
            fat: 13,
            fiber: 1.5
        }
    },
    {
        id: 429,
        name: 'إكلير',
        nameEn: 'Eclair',
        icon: '🥐',
        category: 'حلويات',
        gi: 65,
        ii: 70,
        nutrition: {
            calories: 262,
            protein: 5.2,
            carbs: 24,
            fat: 16,
            fiber: 0.6
        }
    },
    {
        id: 430,
        name: 'بروفيترول',
        nameEn: 'Profiterole',
        icon: '🥐',
        category: 'حلويات',
        gi: 62,
        ii: 68,
        nutrition: {
            calories: 298,
            protein: 4.5,
            carbs: 28,
            fat: 19,
            fiber: 0.8
        }
    },
    {
        id: 431,
        name: 'ميلفي',
        nameEn: 'Mille-feuille',
        icon: '🥐',
        category: 'حلويات',
        gi: 68,
        ii: 72,
        nutrition: {
            calories: 377,
            protein: 4.8,
            carbs: 39,
            fat: 23,
            fiber: 1
        }
    },
    {
        id: 432,
        name: 'كريم برولي',
        nameEn: 'Creme Brulee',
        icon: '🍮',
        category: 'حلويات',
        gi: 58,
        ii: 65,
        nutrition: {
            calories: 258,
            protein: 4.8,
            carbs: 26,
            fat: 15,
            fiber: 0
        }
    },
    {
        id: 433,
        name: 'بافلوفا',
        nameEn: 'Pavlova',
        icon: '🍰',
        category: 'حلويات',
        gi: 65,
        ii: 55,
        nutrition: {
            calories: 179,
            protein: 2.2,
            carbs: 40,
            fat: 2.1,
            fiber: 0.8
        }
    },
    {
        id: 434,
        name: 'بانا كوتا',
        nameEn: 'Panna Cotta',
        icon: '🍮',
        category: 'حلويات',
        gi: 55,
        ii: 60,
        nutrition: {
            calories: 222,
            protein: 2.9,
            carbs: 18,
            fat: 16,
            fiber: 0
        }
    },
    {
        id: 435,
        name: 'فلان',
        nameEn: 'Flan',
        icon: '🍮',
        category: 'حلويات',
        gi: 62,
        ii: 68,
        nutrition: {
            calories: 223,
            protein: 5.5,
            carbs: 33,
            fat: 7.8,
            fiber: 0
        }
    },
    // المزيد من المشروبات
    {
        id: 436,
        name: 'عصير ليمون بالنعناع',
        nameEn: 'Lemon Mint Juice',
        icon: '🍋',
        category: 'مشروبات',
        gi: 30,
        ii: 40,
        nutrition: {
            calories: 48,
            protein: 0.4,
            carbs: 13,
            fat: 0.1,
            fiber: 0.3
        }
    },
    {
        id: 437,
        name: 'جلاب',
        nameEn: 'Jallab',
        icon: '🥤',
        category: 'مشروبات',
        gi: 65,
        ii: 70,
        nutrition: {
            calories: 124,
            protein: 0.5,
            carbs: 32,
            fat: 0.2,
            fiber: 0.5
        }
    },
    {
        id: 438,
        name: 'تمر هندي',
        nameEn: 'Tamarind Juice',
        icon: '🥤',
        category: 'مشروبات',
        gi: 40,
        ii: 48,
        nutrition: {
            calories: 58,
            protein: 0.3,
            carbs: 15,
            fat: 0.1,
            fiber: 0.5
        }
    },
    {
        id: 439,
        name: 'سوبيا',
        nameEn: 'Sobya',
        icon: '🥤',
        category: 'مشروبات',
        gi: 58,
        ii: 62,
        nutrition: {
            calories: 86,
            protein: 1.2,
            carbs: 18,
            fat: 1.5,
            fiber: 0.8
        }
    },
    {
        id: 440,
        name: 'خروب',
        nameEn: 'Carob Juice',
        icon: '🥤',
        category: 'مشروبات',
        gi: 40,
        ii: 45,
        nutrition: {
            calories: 62,
            protein: 0.4,
            carbs: 16,
            fat: 0.1,
            fiber: 0.7
        }
    },
    {
        id: 441,
        name: 'عرق سوس',
        nameEn: 'Licorice Juice',
        icon: '🥤',
        category: 'مشروبات',
        gi: 35,
        ii: 40,
        nutrition: {
            calories: 38,
            protein: 0.2,
            carbs: 10,
            fat: 0,
            fiber: 0.3
        }
    },
    {
        id: 442,
        name: 'قهوة تركية',
        nameEn: 'Turkish Coffee',
        icon: '☕',
        category: 'مشروبات',
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 2,
            protein: 0.1,
            carbs: 0.3,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 443,
        name: 'قهوة عربية',
        nameEn: 'Arabic Coffee',
        icon: '☕',
        category: 'مشروبات',
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 2,
            protein: 0.2,
            carbs: 0,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 444,
        name: 'شاي كرك',
        nameEn: 'Karak Tea',
        icon: '🍵',
        category: 'مشروبات',
        gi: 50,
        ii: 60,
        nutrition: {
            calories: 78,
            protein: 1.8,
            carbs: 14,
            fat: 2,
            fiber: 0
        }
    },
    {
        id: 445,
        name: 'شاي مثلج',
        nameEn: 'Iced Tea',
        icon: '🍵',
        category: 'مشروبات',
        gi: 52,
        ii: 58,
        nutrition: {
            calories: 35,
            protein: 0,
            carbs: 9,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 446,
        name: 'ماتشا لاتيه',
        nameEn: 'Matcha Latte',
        icon: '🍵',
        category: 'مشروبات',
        gi: 40,
        ii: 48,
        nutrition: {
            calories: 120,
            protein: 5,
            carbs: 16,
            fat: 4,
            fiber: 2
        }
    },
    {
        id: 447,
        name: 'ميلك شيك فانيليا',
        nameEn: 'Vanilla Milkshake',
        icon: '🥤',
        category: 'مشروبات',
        gi: 58,
        ii: 72,
        nutrition: {
            calories: 254,
            protein: 8.5,
            carbs: 37,
            fat: 8.5,
            fiber: 0
        }
    },
    {
        id: 448,
        name: 'ميلك شيك فراولة',
        nameEn: 'Strawberry Milkshake',
        icon: '🥤',
        category: 'مشروبات',
        gi: 56,
        ii: 70,
        nutrition: {
            calories: 246,
            protein: 8,
            carbs: 39,
            fat: 7,
            fiber: 0.5
        }
    },
    {
        id: 449,
        name: 'موهيتو بدون كحول',
        nameEn: 'Virgin Mojito',
        icon: '🍹',
        category: 'مشروبات',
        gi: 45,
        ii: 52,
        nutrition: {
            calories: 56,
            protein: 0.2,
            carbs: 15,
            fat: 0,
            fiber: 0.3
        }
    },
    {
        id: 450,
        name: 'عصير تفاح طازج',
        nameEn: 'Fresh Apple Juice',
        icon: '🍎',
        category: 'مشروبات',
        gi: 44,
        ii: 64,
        nutrition: {
            calories: 46,
            protein: 0.1,
            carbs: 11,
            fat: 0.1,
            fiber: 0.2
        }
    },
    // أطعمة إضافية متنوعة
    {
        id: 451,
        name: 'شوربة البصل الفرنسية',
        nameEn: 'French Onion Soup',
        icon: '🍲',
        category: 'وجبات منزلية',
        gi: 35,
        ii: 45,
        nutrition: {
            calories: 147,
            protein: 6.5,
            carbs: 15,
            fat: 7,
            fiber: 2
        }
    },
    {
        id: 452,
        name: 'شوربة الطماطم',
        nameEn: 'Tomato Soup',
        icon: '🍲',
        category: 'وجبات منزلية',
        gi: 38,
        ii: 45,
        nutrition: {
            calories: 74,
            protein: 2,
            carbs: 16,
            fat: 0.7,
            fiber: 1.5
        }
    },
    {
        id: 453,
        name: 'شوربة القرع',
        nameEn: 'Pumpkin Soup',
        icon: '🍲',
        category: 'وجبات منزلية',
        gi: 51,
        ii: 48,
        nutrition: {
            calories: 71,
            protein: 1.8,
            carbs: 12,
            fat: 2.2,
            fiber: 1.9
        }
    },
    {
        id: 454,
        name: 'شوربة البروكلي',
        nameEn: 'Broccoli Soup',
        icon: '🍲',
        category: 'وجبات منزلية',
        gi: 25,
        ii: 32,
        nutrition: {
            calories: 89,
            protein: 4.5,
            carbs: 10,
            fat: 4,
            fiber: 2.8
        }
    },
    {
        id: 455,
        name: 'شوربة الفطر',
        nameEn: 'Mushroom Soup',
        icon: '🍲',
        category: 'وجبات منزلية',
        gi: 30,
        ii: 35,
        nutrition: {
            calories: 85,
            protein: 2.8,
            carbs: 9,
            fat: 4.8,
            fiber: 1.2
        }
    },
    {
        id: 456,
        name: 'قرع محمص',
        nameEn: 'Roasted Pumpkin',
        icon: '🎃',
        category: 'خضروات',
        gi: 75,
        ii: 65,
        nutrition: {
            calories: 49,
            protein: 1.8,
            carbs: 12,
            fat: 0.2,
            fiber: 2.7
        }
    },
    {
        id: 457,
        name: 'جزر مخلل',
        nameEn: 'Pickled Carrots',
        icon: '🥕',
        category: 'معلبات',
        gi: 35,
        ii: 40,
        nutrition: {
            calories: 30,
            protein: 0.6,
            carbs: 7,
            fat: 0.1,
            fiber: 2
        }
    },
    {
        id: 458,
        name: 'فلفل محشي بالأرز',
        nameEn: 'Stuffed Peppers with Rice',
        icon: '🫑',
        category: 'وجبات منزلية',
        gi: 52,
        ii: 58,
        nutrition: {
            calories: 168,
            protein: 5.8,
            carbs: 24,
            fat: 6,
            fiber: 3.5
        }
    },
    {
        id: 459,
        name: 'فلفل محشي باللحم',
        nameEn: 'Stuffed Peppers with Meat',
        icon: '🫑',
        category: 'وجبات منزلية',
        gi: 45,
        ii: 58,
        nutrition: {
            calories: 198,
            protein: 12,
            carbs: 18,
            fat: 9,
            fiber: 3.2
        }
    },
    {
        id: 460,
        name: 'كرات اللحم',
        nameEn: 'Meatballs',
        icon: '🍖',
        category: 'بروتين',
        gi: 0,
        ii: 51,
        nutrition: {
            calories: 267,
            protein: 18,
            carbs: 5,
            fat: 20,
            fiber: 0.5
        }
    },
    {
        id: 461,
        name: 'سمك بالليمون والثوم',
        nameEn: 'Fish with Lemon & Garlic',
        icon: '🐟',
        category: 'بروتين',
        gi: 0,
        ii: 59,
        nutrition: {
            calories: 158,
            protein: 24,
            carbs: 2,
            fat: 6,
            fiber: 0.2
        }
    },
    {
        id: 462,
        name: 'فاهيتا لحم',
        nameEn: 'Beef Fajitas',
        icon: '🌮',
        category: 'أطعمة مكسيكية',
        gi: 48,
        ii: 62,
        nutrition: {
            calories: 325,
            protein: 26,
            carbs: 30,
            fat: 12,
            fiber: 4.5
        }
    },
    {
        id: 463,
        name: 'إنتشيلادا',
        nameEn: 'Enchiladas',
        icon: '🌯',
        category: 'أطعمة مكسيكية',
        gi: 52,
        ii: 65,
        nutrition: {
            calories: 323,
            protein: 16,
            carbs: 36,
            fat: 13,
            fiber: 5
        }
    },
    {
        id: 464,
        name: 'تشيلي كون كارني',
        nameEn: 'Chili Con Carne',
        icon: '🍲',
        category: 'أطعمة مكسيكية',
        gi: 38,
        ii: 52,
        nutrition: {
            calories: 199,
            protein: 15,
            carbs: 18,
            fat: 8,
            fiber: 6.2
        }
    },
    {
        id: 465,
        name: 'كاساديا',
        nameEn: 'Quesadilla',
        icon: '🫔',
        category: 'أطعمة مكسيكية',
        gi: 48,
        ii: 58,
        nutrition: {
            calories: 337,
            protein: 14,
            carbs: 32,
            fat: 17,
            fiber: 2.5
        }
    },
    {
        id: 466,
        name: 'تامالي',
        nameEn: 'Tamales',
        icon: '🌮',
        category: 'أطعمة مكسيكية',
        gi: 52,
        ii: 58,
        nutrition: {
            calories: 285,
            protein: 9.4,
            carbs: 40,
            fat: 11,
            fiber: 4.8
        }
    },
    {
        id: 467,
        name: 'كارباتشيو',
        nameEn: 'Carpaccio',
        icon: '🥩',
        category: 'أطعمة إيطالية',
        gi: 0,
        ii: 51,
        nutrition: {
            calories: 120,
            protein: 21,
            carbs: 0.5,
            fat: 3.8,
            fiber: 0
        }
    },
    {
        id: 468,
        name: 'أرانشيني',
        nameEn: 'Arancini',
        icon: '🍙',
        category: 'أطعمة إيطالية',
        gi: 70,
        ii: 72,
        nutrition: {
            calories: 252,
            protein: 8.3,
            carbs: 32,
            fat: 10,
            fiber: 1.5
        }
    },
    {
        id: 469,
        name: 'فوكاتشيا',
        nameEn: 'Focaccia',
        icon: '🍞',
        category: 'مخبوزات',
        gi: 71,
        ii: 68,
        nutrition: {
            calories: 267,
            protein: 6.7,
            carbs: 44,
            fat: 7.5,
            fiber: 2
        }
    },
    {
        id: 470,
        name: 'بانيني',
        nameEn: 'Panini',
        icon: '🥪',
        category: 'سندويشات',
        gi: 58,
        ii: 65,
        nutrition: {
            calories: 354,
            protein: 16,
            carbs: 41,
            fat: 14,
            fiber: 2.8
        }
    },
    {
        id: 471,
        name: 'باربكيو دجاج',
        nameEn: 'BBQ Chicken',
        icon: '🍗',
        category: 'بروتين',
        gi: 0,
        ii: 51,
        nutrition: {
            calories: 239,
            protein: 27,
            carbs: 7,
            fat: 11,
            fiber: 0.2
        }
    },
    {
        id: 472,
        name: 'برجر سمك',
        nameEn: 'Fish Burger',
        icon: '🍔',
        category: 'سندويشات',
        gi: 50,
        ii: 62,
        nutrition: {
            calories: 285,
            protein: 16,
            carbs: 34,
            fat: 10,
            fiber: 2
        }
    },
    {
        id: 473,
        name: 'كوكتيل الجمبري',
        nameEn: 'Shrimp Cocktail',
        icon: '🦐',
        category: 'بروتين',
        gi: 15,
        ii: 35,
        nutrition: {
            calories: 123,
            protein: 18,
            carbs: 8,
            fat: 2,
            fiber: 0.5
        }
    },
    {
        id: 474,
        name: 'ريزوتو بالجمبري',
        nameEn: 'Shrimp Risotto',
        icon: '🍚',
        category: 'أطعمة إيطالية',
        gi: 69,
        ii: 75,
        nutrition: {
            calories: 278,
            protein: 12,
            carbs: 38,
            fat: 9,
            fiber: 1.2
        }
    },
    {
        id: 475,
        name: 'بيتزا نباتية',
        nameEn: 'Veggie Pizza',
        icon: '🍕',
        category: 'مطاعم',
        gi: 58,
        ii: 65,
        nutrition: {
            calories: 235,
            protein: 9,
            carbs: 33,
            fat: 8,
            fiber: 2.5
        }
    },
    {
        id: 476,
        name: 'بيتزا دجاج',
        nameEn: 'Chicken Pizza',
        icon: '🍕',
        category: 'مطاعم',
        gi: 60,
        ii: 72,
        nutrition: {
            calories: 268,
            protein: 14,
            carbs: 32,
            fat: 10,
            fiber: 2
        }
    },
    {
        id: 477,
        name: 'سلطة سيزر بالدجاج',
        nameEn: 'Chicken Caesar Salad',
        icon: '🥗',
        category: 'سلطات',
        gi: 20,
        ii: 45,
        nutrition: {
            calories: 234,
            protein: 22,
            carbs: 8,
            fat: 14,
            fiber: 2.5
        }
    },
    {
        id: 478,
        name: 'سلطة جمبري',
        nameEn: 'Shrimp Salad',
        icon: '🥗',
        category: 'سلطات',
        gi: 15,
        ii: 35,
        nutrition: {
            calories: 156,
            protein: 20,
            carbs: 5,
            fat: 6.5,
            fiber: 1.8
        }
    },
    {
        id: 479,
        name: 'سلطة نيسواز',
        nameEn: 'Nicoise Salad',
        icon: '🥗',
        category: 'سلطات',
        gi: 20,
        ii: 38,
        nutrition: {
            calories: 234,
            protein: 16,
            carbs: 12,
            fat: 15,
            fiber: 3.5
        }
    },
    {
        id: 480,
        name: 'وراب دجاج',
        nameEn: 'Chicken Wrap',
        icon: '🌯',
        category: 'سندويشات',
        gi: 50,
        ii: 62,
        nutrition: {
            calories: 298,
            protein: 22,
            carbs: 32,
            fat: 9,
            fiber: 3.5
        }
    },
    {
        id: 481,
        name: 'وراب فلافل',
        nameEn: 'Falafel Wrap',
        icon: '🌯',
        category: 'سندويشات',
        gi: 42,
        ii: 52,
        nutrition: {
            calories: 315,
            protein: 12,
            carbs: 42,
            fat: 11,
            fiber: 6
        }
    },
    {
        id: 482,
        name: 'إسكالوب دجاج',
        nameEn: 'Chicken Escalope',
        icon: '🍗',
        category: 'بروتين',
        gi: 18,
        ii: 52,
        nutrition: {
            calories: 295,
            protein: 22,
            carbs: 12,
            fat: 18,
            fiber: 0.8
        }
    },
    {
        id: 483,
        name: 'قطع دجاج مقلي',
        nameEn: 'Chicken Tenders',
        icon: '🍗',
        category: 'بروتين',
        gi: 22,
        ii: 58,
        nutrition: {
            calories: 263,
            protein: 18,
            carbs: 14,
            fat: 16,
            fiber: 0.6
        }
    },
    {
        id: 484,
        name: 'دجاج كريسبي',
        nameEn: 'Crispy Chicken',
        icon: '🍗',
        category: 'بروتين',
        gi: 25,
        ii: 58,
        nutrition: {
            calories: 298,
            protein: 19,
            carbs: 16,
            fat: 19,
            fiber: 0.7
        }
    },
    {
        id: 485,
        name: 'ستيك لحم',
        nameEn: 'Beef Steak',
        icon: '🥩',
        category: 'بروتين',
        gi: 0,
        ii: 51,
        nutrition: {
            calories: 271,
            protein: 26,
            carbs: 0,
            fat: 18,
            fiber: 0
        }
    },
    {
        id: 486,
        name: 'تيبون ستيك',
        nameEn: 'T-Bone Steak',
        icon: '🥩',
        category: 'بروتين',
        gi: 0,
        ii: 51,
        nutrition: {
            calories: 247,
            protein: 24,
            carbs: 0,
            fat: 16,
            fiber: 0
        }
    },
    {
        id: 487,
        name: 'ريب آي ستيك',
        nameEn: 'Ribeye Steak',
        icon: '🥩',
        category: 'بروتين',
        gi: 0,
        ii: 51,
        nutrition: {
            calories: 291,
            protein: 25,
            carbs: 0,
            fat: 21,
            fiber: 0
        }
    },
    {
        id: 488,
        name: 'فيليه ميجنون',
        nameEn: 'Filet Mignon',
        icon: '🥩',
        category: 'بروتين',
        gi: 0,
        ii: 51,
        nutrition: {
            calories: 227,
            protein: 27,
            carbs: 0,
            fat: 13,
            fiber: 0
        }
    },
    {
        id: 489,
        name: 'لحم مشوي بطيء',
        nameEn: 'Slow Roasted Beef',
        icon: '🥩',
        category: 'بروتين',
        gi: 0,
        ii: 51,
        nutrition: {
            calories: 265,
            protein: 24,
            carbs: 0,
            fat: 18,
            fiber: 0
        }
    },
    {
        id: 490,
        name: 'سلمون مدخن',
        nameEn: 'Smoked Salmon',
        icon: '🐟',
        category: 'بروتين',
        gi: 0,
        ii: 59,
        nutrition: {
            calories: 117,
            protein: 18,
            carbs: 0,
            fat: 4.3,
            fiber: 0
        }
    },
    {
        id: 491,
        name: 'سلمون سوشي',
        nameEn: 'Salmon Nigiri',
        icon: '🍣',
        category: 'أطعمة آسيوية',
        gi: 55,
        ii: 60,
        nutrition: {
            calories: 50,
            protein: 3.7,
            carbs: 6.3,
            fat: 1.2,
            fiber: 0.2
        }
    },
    {
        id: 492,
        name: 'تونة سوشي',
        nameEn: 'Tuna Nigiri',
        icon: '🍣',
        category: 'أطعمة آسيوية',
        gi: 55,
        ii: 58,
        nutrition: {
            calories: 44,
            protein: 4.5,
            carbs: 5.8,
            fat: 0.4,
            fiber: 0.2
        }
    },
    {
        id: 493,
        name: 'ماكي سوشي',
        nameEn: 'Maki Sushi',
        icon: '🍣',
        category: 'أطعمة آسيوية',
        gi: 55,
        ii: 60,
        nutrition: {
            calories: 48,
            protein: 2.1,
            carbs: 8.5,
            fat: 0.8,
            fiber: 0.3
        }
    },
    {
        id: 494,
        name: 'كاليفورنيا رول',
        nameEn: 'California Roll',
        icon: '🍣',
        category: 'أطعمة آسيوية',
        gi: 55,
        ii: 60,
        nutrition: {
            calories: 33,
            protein: 1.4,
            carbs: 5.8,
            fat: 0.6,
            fiber: 0.2
        }
    },
    {
        id: 495,
        name: 'تمبورا جمبري',
        nameEn: 'Shrimp Tempura',
        icon: '🍤',
        category: 'أطعمة آسيوية',
        gi: 45,
        ii: 55,
        nutrition: {
            calories: 175,
            protein: 8,
            carbs: 14,
            fat: 10,
            fiber: 0.5
        }
    },
    {
        id: 496,
        name: 'تمبورا خضار',
        nameEn: 'Vegetable Tempura',
        icon: '🥦',
        category: 'أطعمة آسيوية',
        gi: 45,
        ii: 42,
        nutrition: {
            calories: 138,
            protein: 2.5,
            carbs: 18,
            fat: 6.8,
            fiber: 1.8
        }
    },
    {
        id: 497,
        name: 'وسابي',
        nameEn: 'Wasabi',
        icon: '🥦',
        category: 'أطعمة آسيوية',
        gi: 10,
        ii: 10,
        nutrition: {
            calories: 109,
            protein: 4.8,
            carbs: 24,
            fat: 0.6,
            fiber: 7.8
        }
    },
    {
        id: 498,
        name: 'زنجبيل مخلل',
        nameEn: 'Pickled Ginger',
        icon: '🥒',
        category: 'معلبات',
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 51,
            protein: 0.5,
            carbs: 12,
            fat: 0.1,
            fiber: 0.8
        }
    },
    {
        id: 499,
        name: 'صوص الصويا',
        nameEn: 'Soy Sauce',
        icon: '🥫',
        category: 'معلبات',
        gi: 20,
        ii: 18,
        nutrition: {
            calories: 53,
            protein: 5,
            carbs: 4.9,
            fat: 0.6,
            fiber: 0.8
        }
    },
    {
        id: 500,
        name: 'كيمتشي',
        nameEn: 'Kimchi',
        icon: '🥬',
        category: 'معلبات',
        gi: 15,
        ii: 15,
        nutrition: {
            calories: 15,
            protein: 1.1,
            carbs: 2.4,
            fat: 0.5,
            fiber: 1.6
        }
    },
    {
        id: 501,
        name: 'إداماميه',
        nameEn: 'Edamame',
        icon: '🫛',
        category: 'بقوليات',
        gi: 15,
        ii: 43,
        nutrition: {
            calories: 122,
            protein: 11,
            carbs: 10,
            fat: 5,
            fiber: 5
        }
    },
    {
        id: 502,
        name: 'تاكوياكي',
        nameEn: 'Takoyaki',
        icon: '🍡',
        category: 'أطعمة آسيوية',
        gi: 52,
        ii: 58,
        nutrition: {
            calories: 175,
            protein: 7,
            carbs: 23,
            fat: 6.5,
            fiber: 0.8
        }
    },
    {
        id: 503,
        name: 'أوكونومياكي',
        nameEn: 'Okonomiyaki',
        icon: '🥞',
        category: 'أطعمة آسيوية',
        gi: 50,
        ii: 58,
        nutrition: {
            calories: 232,
            protein: 10,
            carbs: 28,
            fat: 9,
            fiber: 2.1
        }
    },
    {
        id: 504,
        name: 'ياكيتوري',
        nameEn: 'Yakitori',
        icon: '🍢',
        category: 'أطعمة آسيوية',
        gi: 0,
        ii: 51,
        nutrition: {
            calories: 178,
            protein: 22,
            carbs: 4,
            fat: 8,
            fiber: 0.2
        }
    },
    {
        id: 505,
        name: 'كاتسو كاري',
        nameEn: 'Katsu Curry',
        icon: '🍛',
        category: 'أطعمة آسيوية',
        gi: 58,
        ii: 68,
        nutrition: {
            calories: 412,
            protein: 18,
            carbs: 52,
            fat: 15,
            fiber: 3.2
        }
    },
    
    // === أسماك ومأكولات بحرية جديدة ===
    {
        id: 506,
        name: "سمك الماكريل",
        nameEn: "Mackerel",
        icon: "🐟",
        category: "أسماك",
        gi: 0,
        ii: 59,
        nutrition: {
            calories: 205,
            protein: 18.6,
            carbs: 0,
            fat: 13.9,
            fiber: 0
        }
    },
    {
        id: 507,
        name: "الروبيان (الجمبري)",
        nameEn: "Shrimp",
        icon: "🦐",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 60,
        nutrition: {
            calories: 99,
            protein: 20.9,
            carbs: 0.2,
            fat: 1.7,
            fiber: 0
        }
    },
    {
        id: 508,
        name: "سمك القد",
        nameEn: "Cod",
        icon: "🐟",
        category: "أسماك",
        gi: 0,
        ii: 59,
        nutrition: {
            calories: 82,
            protein: 17.8,
            carbs: 0,
            fat: 0.7,
            fiber: 0
        }
    },
    {
        id: 509,
        name: "سمك البلطي",
        nameEn: "Tilapia",
        icon: "🐟",
        category: "أسماك",
        gi: 0,
        ii: 59,
        nutrition: {
            calories: 96,
            protein: 20.1,
            carbs: 0,
            fat: 1.7,
            fiber: 0
        }
    },
    {
        id: 510,
        name: "الأخطبوط",
        nameEn: "Octopus",
        icon: "🐙",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 60,
        nutrition: {
            calories: 82,
            protein: 14.9,
            carbs: 2.2,
            fat: 1.0,
            fiber: 0
        }
    },
    {
        id: 511,
        name: "سمك الهامور",
        nameEn: "Grouper",
        icon: "🐟",
        category: "أسماك",
        gi: 0,
        ii: 59,
        nutrition: {
            calories: 92,
            protein: 19.4,
            carbs: 0,
            fat: 1.0,
            fiber: 0
        }
    },
    {
        id: 512,
        name: "الكاليماري (الحبار)",
        nameEn: "Calamari",
        icon: "🦑",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 60,
        nutrition: {
            calories: 92,
            protein: 15.6,
            carbs: 3.1,
            fat: 1.4,
            fiber: 0
        }
    },
    {
        id: 513,
        name: "سمك السردين",
        nameEn: "Sardines",
        icon: "🐟",
        category: "أسماك",
        gi: 0,
        ii: 59,
        nutrition: {
            calories: 208,
            protein: 24.6,
            carbs: 0,
            fat: 11.5,
            fiber: 0
        }
    },
    {
        id: 514,
        name: "سمك الأنشوفة",
        nameEn: "Anchovies",
        icon: "🐟",
        category: "أسماك",
        gi: 0,
        ii: 59,
        nutrition: {
            calories: 131,
            protein: 20.4,
            carbs: 0,
            fat: 4.8,
            fiber: 0
        }
    },
    {
        id: 515,
        name: "بلح البحر (المحار)",
        nameEn: "Mussels",
        icon: "🦪",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 60,
        nutrition: {
            calories: 86,
            protein: 11.9,
            carbs: 3.7,
            fat: 2.2,
            fiber: 0
        }
    },

    // === مكسرات وبذور جديدة ===
    {
        id: 516,
        name: "جوز البقان",
        nameEn: "Pecans",
        icon: "🥜",
        category: "مكسرات",
        gi: 10,
        ii: 10,
        nutrition: {
            calories: 691,
            protein: 9.2,
            carbs: 13.9,
            fat: 72.0,
            fiber: 9.6
        }
    },
    {
        id: 517,
        name: "بذور الشيا",
        nameEn: "Chia Seeds",
        icon: "🌾",
        category: "بذور",
        gi: 1,
        ii: 1,
        nutrition: {
            calories: 486,
            protein: 16.5,
            carbs: 42.1,
            fat: 30.7,
            fiber: 34.4
        }
    },
    {
        id: 518,
        name: "الكاجو",
        nameEn: "Cashews",
        icon: "🥜",
        category: "مكسرات",
        gi: 25,
        ii: 20,
        nutrition: {
            calories: 553,
            protein: 18.2,
            carbs: 30.2,
            fat: 43.9,
            fiber: 3.3
        }
    },
    {
        id: 519,
        name: "بذور القرع (اللب الأبيض)",
        nameEn: "Pumpkin Seeds",
        icon: "🌰",
        category: "بذور",
        gi: 25,
        ii: 15,
        nutrition: {
            calories: 446,
            protein: 18.6,
            carbs: 53.8,
            fat: 19.4,
            fiber: 18.4
        }
    },
    {
        id: 520,
        name: "جوز الماكاداميا",
        nameEn: "Macadamia Nuts",
        icon: "🥜",
        category: "مكسرات",
        gi: 10,
        ii: 10,
        nutrition: {
            calories: 718,
            protein: 7.9,
            carbs: 13.8,
            fat: 75.8,
            fiber: 8.6
        }
    },
    {
        id: 521,
        name: "بذور الكتان",
        nameEn: "Flax Seeds",
        icon: "🌾",
        category: "بذور",
        gi: 35,
        ii: 18,
        nutrition: {
            calories: 534,
            protein: 18.3,
            carbs: 28.9,
            fat: 42.2,
            fiber: 27.3
        }
    },
    {
        id: 522,
        name: "الفستق الحلبي",
        nameEn: "Pistachios",
        icon: "🥜",
        category: "مكسرات",
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 560,
            protein: 20.2,
            carbs: 27.2,
            fat: 45.3,
            fiber: 10.6
        }
    },
    {
        id: 523,
        name: "البندق",
        nameEn: "Hazelnuts",
        icon: "🌰",
        category: "مكسرات",
        gi: 15,
        ii: 12,
        nutrition: {
            calories: 628,
            protein: 15.0,
            carbs: 16.7,
            fat: 60.8,
            fiber: 9.7
        }
    },
    {
        id: 524,
        name: "بذور دوار الشمس",
        nameEn: "Sunflower Seeds",
        icon: "🌻",
        category: "بذور",
        gi: 35,
        ii: 20,
        nutrition: {
            calories: 584,
            protein: 20.8,
            carbs: 20.0,
            fat: 51.5,
            fiber: 8.6
        }
    },
    {
        id: 525,
        name: "جوز الهند المجفف",
        nameEn: "Dried Coconut",
        icon: "🥥",
        category: "مكسرات",
        gi: 35,
        ii: 20,
        nutrition: {
            calories: 660,
            protein: 6.9,
            carbs: 23.7,
            fat: 64.5,
            fiber: 16.3
        }
    },

    // === فواكه استوائية ونادرة ===
    {
        id: 526,
        name: "فاكهة التنين (البيتايا)",
        nameEn: "Dragon Fruit",
        icon: "🐉",
        category: "فواكه",
        gi: 48,
        ii: 40,
        nutrition: {
            calories: 60,
            protein: 1.2,
            carbs: 13.0,
            fat: 0.4,
            fiber: 3.0
        }
    },
    {
        id: 527,
        name: "البابايا",
        nameEn: "Papaya",
        icon: "🍈",
        category: "فواكه",
        gi: 60,
        ii: 52,
        nutrition: {
            calories: 43,
            protein: 0.5,
            carbs: 10.8,
            fat: 0.3,
            fiber: 1.7
        }
    },
    {
        id: 528,
        name: "الليتشي",
        nameEn: "Lychee",
        icon: "🍒",
        category: "فواكه",
        gi: 50,
        ii: 45,
        nutrition: {
            calories: 66,
            protein: 0.8,
            carbs: 16.5,
            fat: 0.4,
            fiber: 1.3
        }
    },
    {
        id: 529,
        name: "فاكهة الكيوانو (البطيخ المقرن)",
        nameEn: "Kiwano",
        icon: "🥒",
        category: "فواكه",
        gi: 49,
        ii: 42,
        nutrition: {
            calories: 44,
            protein: 1.8,
            carbs: 7.6,
            fat: 1.3,
            fiber: 2.0
        }
    },
    {
        id: 530,
        name: "الجوافة",
        nameEn: "Guava",
        icon: "🍐",
        category: "فواكه",
        gi: 12,
        ii: 25,
        nutrition: {
            calories: 68,
            protein: 2.6,
            carbs: 14.3,
            fat: 1.0,
            fiber: 5.4
        }
    },
    {
        id: 531,
        name: "الباشن فروت (فاكهة العاطفة)",
        nameEn: "Passion Fruit",
        icon: "🥭",
        category: "فواكه",
        gi: 30,
        ii: 35,
        nutrition: {
            calories: 97,
            protein: 2.2,
            carbs: 23.4,
            fat: 0.7,
            fiber: 10.4
        }
    },
    {
        id: 532,
        name: "الرامبوتان",
        nameEn: "Rambutan",
        icon: "🍒",
        category: "فواكه",
        gi: 50,
        ii: 45,
        nutrition: {
            calories: 82,
            protein: 0.7,
            carbs: 20.9,
            fat: 0.2,
            fiber: 0.9
        }
    },
    {
        id: 533,
        name: "الكمكوات",
        nameEn: "Kumquat",
        icon: "🍊",
        category: "فواكه",
        gi: 30,
        ii: 32,
        nutrition: {
            calories: 71,
            protein: 1.9,
            carbs: 15.9,
            fat: 0.9,
            fiber: 6.5
        }
    },
    {
        id: 534,
        name: "الدوريان",
        nameEn: "Durian",
        icon: "🥥",
        category: "فواكه",
        gi: 49,
        ii: 45,
        nutrition: {
            calories: 147,
            protein: 1.5,
            carbs: 27.1,
            fat: 5.3,
            fiber: 3.8
        }
    },
    {
        id: 535,
        name: "فاكهة النجمة (الكرامبولا)",
        nameEn: "Star Fruit",
        icon: "⭐",
        category: "فواكه",
        gi: 45,
        ii: 40,
        nutrition: {
            calories: 31,
            protein: 1.0,
            carbs: 6.7,
            fat: 0.3,
            fiber: 2.8
        }
    },

    // === خضروات ورقية ونادرة ===
    {
        id: 536,
        name: "الكرنب الصيني (بوك تشوي)",
        nameEn: "Bok Choy",
        icon: "🥬",
        category: "خضروات ورقية",
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 13,
            protein: 1.5,
            carbs: 2.2,
            fat: 0.2,
            fiber: 1.0
        }
    },
    {
        id: 537,
        name: "الجرجير",
        nameEn: "Arugula",
        icon: "🌿",
        category: "خضروات ورقية",
        gi: 15,
        ii: 18,
        nutrition: {
            calories: 25,
            protein: 2.6,
            carbs: 3.7,
            fat: 0.7,
            fiber: 1.6
        }
    },
    {
        id: 538,
        name: "الكرفس",
        nameEn: "Celery",
        icon: "🌿",
        category: "خضروات",
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 14,
            protein: 0.7,
            carbs: 3.0,
            fat: 0.2,
            fiber: 1.6
        }
    },
    {
        id: 539,
        name: "الشمندر الأحمر (البنجر)",
        nameEn: "Beetroot",
        icon: "🥕",
        category: "خضروات جذرية",
        gi: 61,
        ii: 55,
        nutrition: {
            calories: 43,
            protein: 1.6,
            carbs: 9.6,
            fat: 0.2,
            fiber: 2.8
        }
    },
    {
        id: 540,
        name: "الكحلبي (اللفت الأحمر)",
        nameEn: "Kohlrabi",
        icon: "🥔",
        category: "خضروات جذرية",
        gi: 15,
        ii: 22,
        nutrition: {
            calories: 27,
            protein: 1.7,
            carbs: 6.2,
            fat: 0.1,
            fiber: 3.6
        }
    },
    {
        id: 541,
        name: "الهليون",
        nameEn: "Asparagus",
        icon: "🌿",
        category: "خضروات",
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 20,
            protein: 2.2,
            carbs: 3.9,
            fat: 0.1,
            fiber: 2.1
        }
    },
    {
        id: 542,
        name: "الكرات (الكراث)",
        nameEn: "Leeks",
        icon: "🧅",
        category: "خضروات",
        gi: 15,
        ii: 22,
        nutrition: {
            calories: 61,
            protein: 1.5,
            carbs: 14.2,
            fat: 0.3,
            fiber: 1.8
        }
    },
    {
        id: 543,
        name: "الملفوف الأحمر",
        nameEn: "Red Cabbage",
        icon: "🥬",
        category: "خضروات ورقية",
        gi: 10,
        ii: 18,
        nutrition: {
            calories: 31,
            protein: 1.4,
            carbs: 7.4,
            fat: 0.2,
            fiber: 2.1
        }
    },
    {
        id: 544,
        name: "الخرشوف",
        nameEn: "Artichoke",
        icon: "🌿",
        category: "خضروات",
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 47,
            protein: 3.3,
            carbs: 10.5,
            fat: 0.2,
            fiber: 5.4
        }
    },
    {
        id: 545,
        name: "الفجل الأحمر",
        nameEn: "Radish",
        icon: "🥕",
        category: "خضروات جذرية",
        gi: 15,
        ii: 18,
        nutrition: {
            calories: 16,
            protein: 0.7,
            carbs: 3.4,
            fat: 0.1,
            fiber: 1.6
        }
    },

    // === بقوليات وحبوب كاملة ===
    {
        id: 546,
        name: "الكينوا",
        nameEn: "Quinoa",
        icon: "🌾",
        category: "حبوب كاملة",
        gi: 53,
        ii: 48,
        nutrition: {
            calories: 368,
            protein: 14.1,
            carbs: 64.2,
            fat: 6.1,
            fiber: 7.0
        }
    },
    {
        id: 547,
        name: "العدس الأخضر",
        nameEn: "Green Lentils",
        icon: "🌰",
        category: "بقوليات",
        gi: 30,
        ii: 32,
        nutrition: {
            calories: 116,
            protein: 9.0,
            carbs: 20.1,
            fat: 0.4,
            fiber: 7.9
        }
    },
    {
        id: 548,
        name: "الحمص الحب",
        nameEn: "Chickpeas",
        icon: "🌰",
        category: "بقوليات",
        gi: 28,
        ii: 30,
        nutrition: {
            calories: 164,
            protein: 8.9,
            carbs: 27.4,
            fat: 2.6,
            fiber: 7.6
        }
    },
    {
        id: 549,
        name: "الفاصوليا السوداء",
        nameEn: "Black Beans",
        icon: "🌰",
        category: "بقوليات",
        gi: 30,
        ii: 32,
        nutrition: {
            calories: 132,
            protein: 8.9,
            carbs: 23.7,
            fat: 0.5,
            fiber: 8.7
        }
    },
    {
        id: 550,
        name: "الشعير المقشر",
        nameEn: "Pearl Barley",
        icon: "🌾",
        category: "حبوب كاملة",
        gi: 28,
        ii: 32,
        nutrition: {
            calories: 354,
            protein: 12.5,
            carbs: 73.5,
            fat: 2.3,
            fiber: 17.3
        }
    },
    {
        id: 551,
        name: "الفاصوليا الحمراء",
        nameEn: "Kidney Beans",
        icon: "🌰",
        category: "بقوليات",
        gi: 24,
        ii: 28,
        nutrition: {
            calories: 127,
            protein: 8.7,
            carbs: 22.8,
            fat: 0.5,
            fiber: 6.4
        }
    },
    {
        id: 552,
        name: "الدخن",
        nameEn: "Millet",
        icon: "🌾",
        category: "حبوب كاملة",
        gi: 71,
        ii: 60,
        nutrition: {
            calories: 378,
            protein: 11.0,
            carbs: 73.0,
            fat: 4.2,
            fiber: 8.5
        }
    },
    {
        id: 553,
        name: "اللوبيا",
        nameEn: "Black-eyed Peas",
        icon: "🌰",
        category: "بقوليات",
        gi: 26,
        ii: 30,
        nutrition: {
            calories: 116,
            protein: 7.7,
            carbs: 21.0,
            fat: 0.4,
            fiber: 6.5
        }
    },
    {
        id: 554,
        name: "الفريكة",
        nameEn: "Freekeh",
        icon: "🌾",
        category: "حبوب كاملة",
        gi: 43,
        ii: 40,
        nutrition: {
            calories: 346,
            protein: 12.7,
            carbs: 72.5,
            fat: 2.5,
            fiber: 16.5
        }
    },
    {
        id: 555,
        name: "الترمس",
        nameEn: "Lupini Beans",
        icon: "🌰",
        category: "بقوليات",
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 119,
            protein: 16.4,
            carbs: 9.9,
            fat: 2.9,
            fiber: 2.8
        }
    },
    // مشروبات صحية (556-580)
    {
        id: 556,
        name: "عصير برتقال طبيعي",
        nameEn: "Fresh Orange Juice",
        icon: "🍊",
        category: "مشروبات",
        gi: 50,
        ii: 60,
        nutrition: {
            calories: 45,
            protein: 0.7,
            carbs: 10.4,
            fat: 0.2,
            fiber: 0.2
        }
    },
    {
        id: 557,
        name: "عصير رمان طازج",
        nameEn: "Pomegranate Juice",
        icon: "🍹",
        category: "مشروبات",
        gi: 53,
        ii: 58,
        nutrition: {
            calories: 54,
            protein: 0.5,
            carbs: 13.1,
            fat: 0.3,
            fiber: 0.1
        }
    },
    {
        id: 558,
        name: "شاي أخضر",
        nameEn: "Green Tea",
        icon: "🍵",
        category: "مشروبات",
        gi: 0,
        ii: 5,
        nutrition: {
            calories: 2,
            protein: 0.2,
            carbs: 0,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 559,
        name: "قهوة سوداء",
        nameEn: "Black Coffee",
        icon: "☕",
        category: "مشروبات",
        gi: 0,
        ii: 5,
        nutrition: {
            calories: 2,
            protein: 0.3,
            carbs: 0,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 560,
        name: "حليب لوز غير محلى",
        nameEn: "Unsweetened Almond Milk",
        icon: "🥛",
        category: "مشروبات",
        gi: 25,
        ii: 30,
        nutrition: {
            calories: 17,
            protein: 0.6,
            carbs: 0.6,
            fat: 1.4,
            fiber: 0.2
        }
    },
    {
        id: 561,
        name: "ماء جوز الهند",
        nameEn: "Coconut Water",
        icon: "🥥",
        category: "مشروبات",
        gi: 54,
        ii: 55,
        nutrition: {
            calories: 19,
            protein: 0.7,
            carbs: 3.7,
            fat: 0.2,
            fiber: 1.1
        }
    },
    {
        id: 562,
        name: "عصير جزر طازج",
        nameEn: "Carrot Juice",
        icon: "🥕",
        category: "مشروبات",
        gi: 43,
        ii: 50,
        nutrition: {
            calories: 40,
            protein: 0.9,
            carbs: 9.2,
            fat: 0.2,
            fiber: 0.8
        }
    },
    {
        id: 563,
        name: "عصير تفاح طبيعي",
        nameEn: "Apple Juice",
        icon: "🍎",
        category: "مشروبات",
        gi: 41,
        ii: 48,
        nutrition: {
            calories: 46,
            protein: 0.1,
            carbs: 11.3,
            fat: 0.1,
            fiber: 0.2
        }
    },
    {
        id: 564,
        name: "سموذي أخضر",
        nameEn: "Green Smoothie",
        icon: "🥬",
        category: "مشروبات",
        gi: 35,
        ii: 40,
        nutrition: {
            calories: 55,
            protein: 1.5,
            carbs: 11,
            fat: 0.5,
            fiber: 2.5
        }
    },
    {
        id: 565,
        name: "لبن رائب",
        nameEn: "Buttermilk",
        icon: "🥛",
        category: "مشروبات",
        gi: 32,
        ii: 35,
        nutrition: {
            calories: 40,
            protein: 3.3,
            carbs: 4.8,
            fat: 0.9,
            fiber: 0
        }
    },
    {
        id: 566,
        name: "شاي زنجبيل وليمون",
        nameEn: "Ginger Lemon Tea",
        icon: "🍵",
        category: "مشروبات",
        gi: 10,
        ii: 15,
        nutrition: {
            calories: 5,
            protein: 0.1,
            carbs: 1.2,
            fat: 0,
            fiber: 0.1
        }
    },
    {
        id: 567,
        name: "عصير شمندر",
        nameEn: "Beetroot Juice",
        icon: "🍹",
        category: "مشروبات",
        gi: 64,
        ii: 68,
        nutrition: {
            calories: 43,
            protein: 1.6,
            carbs: 9.6,
            fat: 0.2,
            fiber: 0.8
        }
    },
    {
        id: 568,
        name: "حليب الصويا غير محلى",
        nameEn: "Unsweetened Soy Milk",
        icon: "🥛",
        category: "مشروبات",
        gi: 30,
        ii: 35,
        nutrition: {
            calories: 33,
            protein: 3.3,
            carbs: 1.7,
            fat: 1.8,
            fiber: 0.6
        }
    },
    {
        id: 569,
        name: "عصير كرنب (ملفوف)",
        nameEn: "Cabbage Juice",
        icon: "🥬",
        category: "مشروبات",
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 25,
            protein: 1.3,
            carbs: 5.8,
            fat: 0.1,
            fiber: 2.5
        }
    },
    {
        id: 570,
        name: "قهوة بالحليب (كابتشينو)",
        nameEn: "Cappuccino",
        icon: "☕",
        category: "مشروبات",
        gi: 30,
        ii: 40,
        nutrition: {
            calories: 73,
            protein: 4,
            carbs: 6.5,
            fat: 4,
            fiber: 0
        }
    },
    {
        id: 571,
        name: "شاي أسود",
        nameEn: "Black Tea",
        icon: "🍵",
        category: "مشروبات",
        gi: 0,
        ii: 5,
        nutrition: {
            calories: 2,
            protein: 0,
            carbs: 0.7,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 572,
        name: "عصير كيوي",
        nameEn: "Kiwi Juice",
        icon: "🥝",
        category: "مشروبات",
        gi: 47,
        ii: 52,
        nutrition: {
            calories: 53,
            protein: 0.9,
            carbs: 12.8,
            fat: 0.4,
            fiber: 1.4
        }
    },
    {
        id: 573,
        name: "مشروب الشوفان",
        nameEn: "Oat Milk",
        icon: "🥛",
        category: "مشروبات",
        gi: 69,
        ii: 75,
        nutrition: {
            calories: 47,
            protein: 1,
            carbs: 7.5,
            fat: 1.5,
            fiber: 0.8
        }
    },
    {
        id: 574,
        name: "عصير أناناس طازج",
        nameEn: "Fresh Pineapple Juice",
        icon: "🍍",
        category: "مشروبات",
        gi: 46,
        ii: 55,
        nutrition: {
            calories: 50,
            protein: 0.4,
            carbs: 13.1,
            fat: 0.1,
            fiber: 0.2
        }
    },
    {
        id: 575,
        name: "عصير طماطم",
        nameEn: "Tomato Juice",
        icon: "🍅",
        category: "مشروبات",
        gi: 38,
        ii: 42,
        nutrition: {
            calories: 17,
            protein: 0.8,
            carbs: 3.9,
            fat: 0.1,
            fiber: 0.4
        }
    },
    {
        id: 576,
        name: "ماء الورد",
        nameEn: "Rose Water",
        icon: "🌹",
        category: "مشروبات",
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 0,
            protein: 0,
            carbs: 0,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 577,
        name: "شاي بالنعناع",
        nameEn: "Mint Tea",
        icon: "🍵",
        category: "مشروبات",
        gi: 0,
        ii: 5,
        nutrition: {
            calories: 2,
            protein: 0,
            carbs: 0.5,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 578,
        name: "قهوة تركية",
        nameEn: "Turkish Coffee",
        icon: "☕",
        category: "مشروبات",
        gi: 0,
        ii: 10,
        nutrition: {
            calories: 2,
            protein: 0.1,
            carbs: 0.3,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 579,
        name: "عصير فراولة طازج",
        nameEn: "Fresh Strawberry Juice",
        icon: "🍓",
        category: "مشروبات",
        gi: 40,
        ii: 45,
        nutrition: {
            calories: 33,
            protein: 0.7,
            carbs: 7.7,
            fat: 0.3,
            fiber: 2
        }
    },
    {
        id: 580,
        name: "عصير ليمون طبيعي",
        nameEn: "Fresh Lemon Juice",
        icon: "🍋",
        category: "مشروبات",
        gi: 20,
        ii: 25,
        nutrition: {
            calories: 22,
            protein: 0.4,
            carbs: 6.9,
            fat: 0.2,
            fiber: 0.3
        }
    },
    // وجبات خفيفة وسناك صحي (581-630)
    {
        id: 581,
        name: "فشار بدون زبدة",
        nameEn: "Air-Popped Popcorn",
        icon: "🍿",
        category: "وجبات خفيفة",
        gi: 65,
        ii: 54,
        nutrition: {
            calories: 31,
            protein: 1,
            carbs: 6.2,
            fat: 0.4,
            fiber: 1.2
        }
    },
    {
        id: 582,
        name: "حمص بالطحينة",
        nameEn: "Hummus",
        icon: "🥣",
        category: "وجبات خفيفة",
        gi: 6,
        ii: 20,
        nutrition: {
            calories: 177,
            protein: 4.9,
            carbs: 20.1,
            fat: 8.6,
            fiber: 4
        }
    },
    {
        id: 583,
        name: "بابا غنوج",
        nameEn: "Baba Ghanoush",
        icon: "🍆",
        category: "وجبات خفيفة",
        gi: 15,
        ii: 25,
        nutrition: {
            calories: 90,
            protein: 1.5,
            carbs: 8.5,
            fat: 6.2,
            fiber: 3.5
        }
    },
    {
        id: 584,
        name: "جواكامولي (غواكامولي)",
        nameEn: "Guacamole",
        icon: "🥑",
        category: "وجبات خفيفة",
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 160,
            protein: 2,
            carbs: 8.5,
            fat: 14.7,
            fiber: 6.7
        }
    },
    {
        id: 585,
        name: "بذور عباد الشمس",
        nameEn: "Sunflower Seeds",
        icon: "🌻",
        category: "وجبات خفيفة",
        gi: 35,
        ii: 20,
        nutrition: {
            calories: 584,
            protein: 20.8,
            carbs: 20,
            fat: 51.5,
            fiber: 8.6
        }
    },
    {
        id: 586,
        name: "بذور اليقطين (القرع)",
        nameEn: "Pumpkin Seeds",
        icon: "🎃",
        category: "وجبات خفيفة",
        gi: 25,
        ii: 15,
        nutrition: {
            calories: 559,
            protein: 30.2,
            carbs: 10.7,
            fat: 49,
            fiber: 6
        }
    },
    {
        id: 587,
        name: "بار بروتين",
        nameEn: "Protein Bar",
        icon: "🍫",
        category: "وجبات خفيفة",
        gi: 43,
        ii: 55,
        nutrition: {
            calories: 200,
            protein: 20,
            carbs: 22,
            fat: 7,
            fiber: 3
        }
    },
    {
        id: 588,
        name: "بار جرانولا",
        nameEn: "Granola Bar",
        icon: "🍪",
        category: "وجبات خفيفة",
        gi: 61,
        ii: 70,
        nutrition: {
            calories: 120,
            protein: 2.5,
            carbs: 20,
            fat: 4,
            fiber: 1.5
        }
    },
    {
        id: 589,
        name: "كعك الأرز",
        nameEn: "Rice Cakes",
        icon: "🍘",
        category: "وجبات خفيفة",
        gi: 82,
        ii: 85,
        nutrition: {
            calories: 35,
            protein: 0.7,
            carbs: 7.3,
            fat: 0.3,
            fiber: 0.4
        }
    },
    {
        id: 590,
        name: "مقرمشات القمح الكامل",
        nameEn: "Whole Wheat Crackers",
        icon: "🍘",
        category: "وجبات خفيفة",
        gi: 67,
        ii: 72,
        nutrition: {
            calories: 71,
            protein: 1.4,
            carbs: 11.5,
            fat: 2.2,
            fiber: 1.4
        }
    },
    {
        id: 591,
        name: "زيتون أخضر",
        nameEn: "Green Olives",
        icon: "🫒",
        category: "وجبات خفيفة",
        gi: 15,
        ii: 10,
        nutrition: {
            calories: 145,
            protein: 1,
            carbs: 3.8,
            fat: 15.3,
            fiber: 3.3
        }
    },
    {
        id: 592,
        name: "زيتون أسود",
        nameEn: "Black Olives",
        icon: "🫒",
        category: "وجبات خفيفة",
        gi: 15,
        ii: 10,
        nutrition: {
            calories: 115,
            protein: 0.8,
            carbs: 6.3,
            fat: 10.7,
            fiber: 3.2
        }
    },
    {
        id: 593,
        name: "لبنة",
        nameEn: "Labneh",
        icon: "🥛",
        category: "وجبات خفيفة",
        gi: 20,
        ii: 30,
        nutrition: {
            calories: 75,
            protein: 5,
            carbs: 3,
            fat: 5,
            fiber: 0
        }
    },
    {
        id: 594,
        name: "جبنة حلوم مشوية",
        nameEn: "Grilled Halloumi",
        icon: "🧀",
        category: "وجبات خفيفة",
        gi: 0,
        ii: 55,
        nutrition: {
            calories: 316,
            protein: 21.2,
            carbs: 2.4,
            fat: 25.4,
            fiber: 0
        }
    },
    {
        id: 595,
        name: "فلافل مشوي",
        nameEn: "Baked Falafel",
        icon: "🧆",
        category: "وجبات خفيفة",
        gi: 35,
        ii: 50,
        nutrition: {
            calories: 333,
            protein: 13.3,
            carbs: 31.8,
            fat: 17.8,
            fiber: 4.9
        }
    },
    {
        id: 596,
        name: "خبز البيتا المحمص",
        nameEn: "Toasted Pita Chips",
        icon: "🥖",
        category: "وجبات خفيفة",
        gi: 57,
        ii: 65,
        nutrition: {
            calories: 327,
            protein: 10.5,
            carbs: 62,
            fat: 4.8,
            fiber: 4.2
        }
    },
    {
        id: 597,
        name: "جزر بيبي",
        nameEn: "Baby Carrots",
        icon: "🥕",
        category: "وجبات خفيفة",
        gi: 39,
        ii: 35,
        nutrition: {
            calories: 35,
            protein: 0.6,
            carbs: 8.2,
            fat: 0.2,
            fiber: 2.3
        }
    },
    {
        id: 598,
        name: "شرائح خيار",
        nameEn: "Cucumber Slices",
        icon: "🥒",
        category: "وجبات خفيفة",
        gi: 15,
        ii: 10,
        nutrition: {
            calories: 16,
            protein: 0.7,
            carbs: 3.6,
            fat: 0.1,
            fiber: 0.5
        }
    },
    {
        id: 599,
        name: "كرفس بالزبدة الفول السوداني",
        nameEn: "Celery with Peanut Butter",
        icon: "🥜",
        category: "وجبات خفيفة",
        gi: 15,
        ii: 30,
        nutrition: {
            calories: 110,
            protein: 4.5,
            carbs: 6.5,
            fat: 8.5,
            fiber: 2.5
        }
    },
    {
        id: 600,
        name: "تفاح مقطع",
        nameEn: "Apple Slices",
        icon: "🍎",
        category: "وجبات خفيفة",
        gi: 36,
        ii: 42,
        nutrition: {
            calories: 52,
            protein: 0.3,
            carbs: 13.8,
            fat: 0.2,
            fiber: 2.4
        }
    },
    {
        id: 601,
        name: "لوز محمص",
        nameEn: "Roasted Almonds",
        icon: "🥜",
        category: "وجبات خفيفة",
        gi: 0,
        ii: 15,
        nutrition: {
            calories: 607,
            protein: 21.2,
            carbs: 21.7,
            fat: 53.4,
            fiber: 12.2
        }
    },
    {
        id: 602,
        name: "فستق مملح قليلاً",
        nameEn: "Lightly Salted Pistachios",
        icon: "🥜",
        category: "وجبات خفيفة",
        gi: 15,
        ii: 18,
        nutrition: {
            calories: 562,
            protein: 20.3,
            carbs: 27.5,
            fat: 45.4,
            fiber: 10.3
        }
    },
    {
        id: 603,
        name: "تمر محشي بالمكسرات",
        nameEn: "Dates Stuffed with Nuts",
        icon: "🌴",
        category: "وجبات خفيفة",
        gi: 42,
        ii: 50,
        nutrition: {
            calories: 320,
            protein: 5.5,
            carbs: 50,
            fat: 12,
            fiber: 7.5
        }
    },
    {
        id: 604,
        name: "شيبس الخضار المخبوزة",
        nameEn: "Baked Veggie Chips",
        icon: "🥔",
        category: "وجبات خفيفة",
        gi: 60,
        ii: 68,
        nutrition: {
            calories: 150,
            protein: 2,
            carbs: 18,
            fat: 8,
            fiber: 3
        }
    },
    {
        id: 605,
        name: "توت مجفف",
        nameEn: "Dried Berries",
        icon: "🫐",
        category: "وجبات خفيفة",
        gi: 50,
        ii: 55,
        nutrition: {
            calories: 325,
            protein: 2.5,
            carbs: 82,
            fat: 1.5,
            fiber: 10
        }
    },
    {
        id: 606,
        name: "لوح طاقة بالشوفان",
        nameEn: "Oat Energy Ball",
        icon: "⚡",
        category: "وجبات خفيفة",
        gi: 42,
        ii: 50,
        nutrition: {
            calories: 150,
            protein: 3.5,
            carbs: 18,
            fat: 7.5,
            fiber: 3
        }
    },
    {
        id: 607,
        name: "جوز هند مبشور",
        nameEn: "Shredded Coconut",
        icon: "🥥",
        category: "وجبات خفيفة",
        gi: 45,
        ii: 35,
        nutrition: {
            calories: 354,
            protein: 3.3,
            carbs: 15.2,
            fat: 33.5,
            fiber: 9
        }
    },
    {
        id: 608,
        name: "كاجو محمص",
        nameEn: "Roasted Cashews",
        icon: "🥜",
        category: "وجبات خفيفة",
        gi: 25,
        ii: 20,
        nutrition: {
            calories: 553,
            protein: 18.2,
            carbs: 30.2,
            fat: 43.8,
            fiber: 3.3
        }
    },
    {
        id: 609,
        name: "لب أبيض",
        nameEn: "White Melon Seeds",
        icon: "🌰",
        category: "وجبات خفيفة",
        gi: 10,
        ii: 15,
        nutrition: {
            calories: 557,
            protein: 24.5,
            carbs: 4.6,
            fat: 47.4,
            fiber: 4
        }
    },
    {
        id: 610,
        name: "مكس المكسرات",
        nameEn: "Mixed Nuts",
        icon: "🥜",
        category: "وجبات خفيفة",
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 607,
            protein: 19.5,
            carbs: 21.5,
            fat: 54,
            fiber: 7
        }
    },
    {
        id: 611,
        name: "زبيب أسود",
        nameEn: "Black Raisins",
        icon: "🍇",
        category: "وجبات خفيفة",
        gi: 64,
        ii: 68,
        nutrition: {
            calories: 299,
            protein: 3.1,
            carbs: 79.2,
            fat: 0.5,
            fiber: 3.7
        }
    },
    {
        id: 612,
        name: "قمر الدين (مشمش مجفف)",
        nameEn: "Apricot Leather",
        icon: "🍑",
        category: "وجبات خفيفة",
        gi: 30,
        ii: 42,
        nutrition: {
            calories: 241,
            protein: 3.4,
            carbs: 62.6,
            fat: 0.5,
            fiber: 7.3
        }
    },
    {
        id: 613,
        name: "جبن أبيض قليل الدسم",
        nameEn: "Low-Fat White Cheese",
        icon: "🧀",
        category: "وجبات خفيفة",
        gi: 0,
        ii: 45,
        nutrition: {
            calories: 72,
            protein: 10.5,
            carbs: 1.4,
            fat: 3,
            fiber: 0
        }
    },
    {
        id: 614,
        name: "معمول بالتمر",
        nameEn: "Date-Filled Cookies",
        icon: "🍪",
        category: "وجبات خفيفة",
        gi: 55,
        ii: 65,
        nutrition: {
            calories: 125,
            protein: 1.8,
            carbs: 18,
            fat: 5.5,
            fiber: 1.5
        }
    },
    {
        id: 615,
        name: "لوز بالعسل",
        nameEn: "Honey-Roasted Almonds",
        icon: "🍯",
        category: "وجبات خفيفة",
        gi: 32,
        ii: 45,
        nutrition: {
            calories: 597,
            protein: 20,
            carbs: 28,
            fat: 48,
            fiber: 11
        }
    },
    {
        id: 616,
        name: "كرات جوز الهند",
        nameEn: "Coconut Balls",
        icon: "🥥",
        category: "وجبات خفيفة",
        gi: 42,
        ii: 50,
        nutrition: {
            calories: 165,
            protein: 1.5,
            carbs: 17,
            fat: 10.5,
            fiber: 2.5
        }
    },
    {
        id: 617,
        name: "بسكويت الشوفان",
        nameEn: "Oatmeal Cookies",
        icon: "🍪",
        category: "وجبات خفيفة",
        gi: 54,
        ii: 62,
        nutrition: {
            calories: 105,
            protein: 1.5,
            carbs: 15.5,
            fat: 4.5,
            fiber: 1
        }
    },
    {
        id: 618,
        name: "كرات التمر والطحينة",
        nameEn: "Date & Tahini Balls",
        icon: "🌴",
        category: "وجبات خفيفة",
        gi: 40,
        ii: 48,
        nutrition: {
            calories: 145,
            protein: 2.5,
            carbs: 18.5,
            fat: 7.5,
            fiber: 2.8
        }
    },
    {
        id: 619,
        name: "قطايف محشية بالجوز",
        nameEn: "Walnut-Stuffed Qatayef",
        icon: "🥞",
        category: "وجبات خفيفة",
        gi: 52,
        ii: 62,
        nutrition: {
            calories: 195,
            protein: 3.5,
            carbs: 25,
            fat: 9.5,
            fiber: 2
        }
    },
    {
        id: 620,
        name: "حلاوة طحينية",
        nameEn: "Tahini Halva",
        icon: "🍬",
        category: "وجبات خفيفة",
        gi: 50,
        ii: 58,
        nutrition: {
            calories: 469,
            protein: 12.6,
            carbs: 58.3,
            fat: 23,
            fiber: 3.9
        }
    },
    {
        id: 621,
        name: "كنافة بالجبن",
        nameEn: "Cheese Kunafa",
        icon: "🧀",
        category: "وجبات خفيفة",
        gi: 60,
        ii: 70,
        nutrition: {
            calories: 285,
            protein: 6.5,
            carbs: 35,
            fat: 13.5,
            fiber: 1
        }
    },
    {
        id: 622,
        name: "بسبوسة",
        nameEn: "Basbousa",
        icon: "🍰",
        category: "وجبات خفيفة",
        gi: 65,
        ii: 72,
        nutrition: {
            calories: 340,
            protein: 5,
            carbs: 48,
            fat: 15,
            fiber: 1.5
        }
    },
    {
        id: 623,
        name: "لقيمات",
        nameEn: "Luqaimat",
        icon: "🍩",
        category: "وجبات خفيفة",
        gi: 76,
        ii: 82,
        nutrition: {
            calories: 275,
            protein: 3.5,
            carbs: 38,
            fat: 12.5,
            fiber: 0.8
        }
    },
    {
        id: 624,
        name: "مهلبية",
        nameEn: "Mahalabia",
        icon: "🍮",
        category: "وجبات خفيفة",
        gi: 48,
        ii: 55,
        nutrition: {
            calories: 142,
            protein: 4,
            carbs: 24,
            fat: 3.5,
            fiber: 0.2
        }
    },
    {
        id: 625,
        name: "كراميل بودينج",
        nameEn: "Caramel Pudding",
        icon: "🍮",
        category: "وجبات خفيفة",
        gi: 52,
        ii: 60,
        nutrition: {
            calories: 158,
            protein: 3.8,
            carbs: 26,
            fat: 4.5,
            fiber: 0
        }
    },
    {
        id: 626,
        name: "بودينج الشوكولاتة",
        nameEn: "Chocolate Pudding",
        icon: "🍫",
        category: "وجبات خفيفة",
        gi: 47,
        ii: 55,
        nutrition: {
            calories: 155,
            protein: 4,
            carbs: 25,
            fat: 5,
            fiber: 1
        }
    },
    {
        id: 627,
        name: "أيس كريم فانيلا قليل الدسم",
        nameEn: "Low-Fat Vanilla Ice Cream",
        icon: "🍦",
        category: "وجبات خفيفة",
        gi: 50,
        ii: 60,
        nutrition: {
            calories: 140,
            protein: 3.5,
            carbs: 24,
            fat: 3.5,
            fiber: 0.5
        }
    },
    {
        id: 628,
        name: "فروزن يوغرت",
        nameEn: "Frozen Yogurt",
        icon: "🍦",
        category: "وجبات خفيفة",
        gi: 46,
        ii: 52,
        nutrition: {
            calories: 127,
            protein: 3.4,
            carbs: 24,
            fat: 2,
            fiber: 0
        }
    },
    {
        id: 629,
        name: "سوربيه الفواكه",
        nameEn: "Fruit Sorbet",
        icon: "🍧",
        category: "وجبات خفيفة",
        gi: 65,
        ii: 70,
        nutrition: {
            calories: 100,
            protein: 0.2,
            carbs: 26,
            fat: 0,
            fiber: 1
        }
    },
    {
        id: 630,
        name: "موس الشوكولاتة الداكنة",
        nameEn: "Dark Chocolate Mousse",
        icon: "🍫",
        category: "وجبات خفيفة",
        gi: 23,
        ii: 40,
        nutrition: {
            calories: 170,
            protein: 3,
            carbs: 18,
            fat: 10,
            fiber: 2
        }
    },
    // أطعمة محلية عربية (631-680)
    {
        id: 631,
        name: "ملوخية",
        nameEn: "Molokhia",
        icon: "🥬",
        category: "خضروات",
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 37,
            protein: 4.5,
            carbs: 6.9,
            fat: 0.2,
            fiber: 2
        }
    },
    {
        id: 632,
        name: "باميا",
        nameEn: "Okra",
        icon: "🌶️",
        category: "خضروات",
        gi: 20,
        ii: 25,
        nutrition: {
            calories: 33,
            protein: 1.9,
            carbs: 7.5,
            fat: 0.2,
            fiber: 3.2
        }
    },
    {
        id: 633,
        name: "كوسا محشي",
        nameEn: "Stuffed Zucchini",
        icon: "🥒",
        category: "وجبات رئيسية",
        gi: 35,
        ii: 48,
        nutrition: {
            calories: 145,
            protein: 6.5,
            carbs: 18,
            fat: 5.5,
            fiber: 3
        }
    },
    {
        id: 634,
        name: "ورق عنب محشي",
        nameEn: "Stuffed Grape Leaves",
        icon: "🍃",
        category: "وجبات رئيسية",
        gi: 30,
        ii: 42,
        nutrition: {
            calories: 158,
            protein: 3.2,
            carbs: 22,
            fat: 6.8,
            fiber: 2.5
        }
    },
    {
        id: 635,
        name: "كبة نية",
        nameEn: "Raw Kibbeh",
        icon: "🍖",
        category: "لحوم",
        gi: 0,
        ii: 70,
        nutrition: {
            calories: 245,
            protein: 18,
            carbs: 12,
            fat: 14,
            fiber: 2.5
        }
    },
    {
        id: 636,
        name: "كبة مقلية",
        nameEn: "Fried Kibbeh",
        icon: "🍖",
        category: "لحوم",
        gi: 0,
        ii: 75,
        nutrition: {
            calories: 345,
            protein: 15,
            carbs: 18,
            fat: 24,
            fiber: 1.5
        }
    },
    {
        id: 637,
        name: "تبولة",
        nameEn: "Tabbouleh",
        icon: "🥗",
        category: "سلطات",
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 90,
            protein: 2.5,
            carbs: 14,
            fat: 3.5,
            fiber: 3.5
        }
    },
    {
        id: 638,
        name: "فتوش",
        nameEn: "Fattoush",
        icon: "🥗",
        category: "سلطات",
        gi: 35,
        ii: 45,
        nutrition: {
            calories: 115,
            protein: 2.8,
            carbs: 16,
            fat: 5,
            fiber: 3
        }
    },
    {
        id: 639,
        name: "مجدرة",
        nameEn: "Mujadara",
        icon: "🍚",
        category: "وجبات رئيسية",
        gi: 37,
        ii: 50,
        nutrition: {
            calories: 185,
            protein: 8,
            carbs: 32,
            fat: 3,
            fiber: 6
        }
    },
    {
        id: 640,
        name: "كشك",
        nameEn: "Kishk",
        icon: "🥣",
        category: "وجبات رئيسية",
        gi: 40,
        ii: 52,
        nutrition: {
            calories: 165,
            protein: 7.5,
            carbs: 28,
            fat: 2.5,
            fiber: 3
        }
    },
    {
        id: 641,
        name: "منسف",
        nameEn: "Mansaf",
        icon: "🍖",
        category: "وجبات رئيسية",
        gi: 45,
        ii: 72,
        nutrition: {
            calories: 385,
            protein: 28,
            carbs: 35,
            fat: 15,
            fiber: 2
        }
    },
    {
        id: 642,
        name: "مقلوبة",
        nameEn: "Maqluba",
        icon: "🍚",
        category: "وجبات رئيسية",
        gi: 52,
        ii: 68,
        nutrition: {
            calories: 295,
            protein: 18,
            carbs: 38,
            fat: 8.5,
            fiber: 3.5
        }
    },
    {
        id: 643,
        name: "فتة حمص",
        nameEn: "Fatteh Hummus",
        icon: "🍲",
        category: "وجبات رئيسية",
        gi: 42,
        ii: 58,
        nutrition: {
            calories: 285,
            protein: 11,
            carbs: 32,
            fat: 13,
            fiber: 7
        }
    },
    {
        id: 644,
        name: "شاورما دجاج",
        nameEn: "Chicken Shawarma",
        icon: "🌯",
        category: "وجبات رئيسية",
        gi: 40,
        ii: 65,
        nutrition: {
            calories: 265,
            protein: 22,
            carbs: 18,
            fat: 12,
            fiber: 2.5
        }
    },
    {
        id: 645,
        name: "شاورما لحم",
        nameEn: "Beef Shawarma",
        icon: "🌯",
        category: "وجبات رئيسية",
        gi: 40,
        ii: 70,
        nutrition: {
            calories: 295,
            protein: 24,
            carbs: 18,
            fat: 15,
            fiber: 2.5
        }
    },
    {
        id: 646,
        name: "كفتة مشوية",
        nameEn: "Grilled Kofta",
        icon: "🍖",
        category: "لحوم",
        gi: 0,
        ii: 65,
        nutrition: {
            calories: 255,
            protein: 22,
            carbs: 5,
            fat: 16,
            fiber: 1
        }
    },
    {
        id: 647,
        name: "مشاوي مشكلة",
        nameEn: "Mixed Grill",
        icon: "🍖",
        category: "لحوم",
        gi: 0,
        ii: 75,
        nutrition: {
            calories: 325,
            protein: 28,
            carbs: 0,
            fat: 23,
            fiber: 0
        }
    },
    {
        id: 648,
        name: "شيش طاووق",
        nameEn: "Shish Taouk",
        icon: "🍗",
        category: "دواجن",
        gi: 0,
        ii: 55,
        nutrition: {
            calories: 185,
            protein: 26,
        carbs: 2,
            fat: 8,
            fiber: 0.5
        }
    },
    {
        id: 649,
        name: "كباب حلة",
        nameEn: "Kabab Halla",
        icon: "🍖",
        category: "لحوم",
        gi: 0,
        ii: 68,
        nutrition: {
            calories: 285,
            protein: 24,
            carbs: 8,
            fat: 18,
            fiber: 2
        }
    },
    {
        id: 650,
        name: "صيادية سمك",
        nameEn: "Fish Sayadieh",
        icon: "🐟",
        category: "مأكولات بحرية",
        gi: 48,
        ii: 60,
        nutrition: {
            calories: 295,
            protein: 22,
            carbs: 32,
            fat: 8,
            fiber: 2.5
        }
    },
    {
        id: 651,
        name: "سمك مشوي",
        nameEn: "Grilled Fish",
        icon: "🐟",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 45,
        nutrition: {
            calories: 145,
            protein: 26,
            carbs: 0,
            fat: 4.5,
            fiber: 0
        }
    },
    {
        id: 652,
        name: "جمبري مشوي",
        nameEn: "Grilled Shrimp",
        icon: "🦐",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 42,
        nutrition: {
            calories: 99,
            protein: 20.9,
            carbs: 0.2,
            fat: 1.7,
            fiber: 0
        }
    },
    {
        id: 653,
        name: "حبار مقلي",
        nameEn: "Fried Calamari",
        icon: "🦑",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 50,
        nutrition: {
            calories: 175,
            protein: 15,
            carbs: 8,
            fat: 9.5,
            fiber: 0.5
        }
    },
    {
        id: 654,
        name: "سمك سلمون مدخن",
        nameEn: "Smoked Salmon",
        icon: "🐟",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 40,
        nutrition: {
            calories: 117,
            protein: 18.3,
            carbs: 0,
            fat: 4.3,
            fiber: 0
        }
    },
    {
        id: 655,
        name: "تونة معلبة بالماء",
        nameEn: "Canned Tuna in Water",
        icon: "🐟",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 38,
        nutrition: {
            calories: 116,
            protein: 25.5,
            carbs: 0,
            fat: 0.8,
            fiber: 0
        }
    },
    {
        id: 656,
        name: "سردين معلب",
        nameEn: "Canned Sardines",
        icon: "🐟",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 42,
        nutrition: {
            calories: 208,
            protein: 24.6,
            carbs: 0,
            fat: 11.5,
            fiber: 0
        }
    },
    {
        id: 657,
        name: "محار",
        nameEn: "Oysters",
        icon: "🦪",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 35,
        nutrition: {
            calories: 68,
            protein: 7,
            carbs: 3.9,
            fat: 2.5,
            fiber: 0
        }
    },
    {
        id: 658,
        name: "بلح البحر",
        nameEn: "Mussels",
        icon: "🦪",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 40,
        nutrition: {
            calories: 86,
            protein: 11.9,
            carbs: 3.7,
            fat: 2.2,
            fiber: 0
        }
    },
    {
        id: 659,
        name: "سلطعون",
        nameEn: "Crab",
        icon: "🦀",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 38,
        nutrition: {
            calories: 97,
            protein: 19.4,
            carbs: 0,
            fat: 1.5,
            fiber: 0
        }
    },
    {
        id: 660,
        name: "كافيار",
        nameEn: "Caviar",
        icon: "🥚",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 30,
        nutrition: {
            calories: 264,
            protein: 24.6,
            carbs: 4,
            fat: 17.9,
            fiber: 0
        }
    },
    {
        id: 661,
        name: "ملوحة (فسيخ)",
        nameEn: "Salted Fish",
        icon: "🐟",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 45,
        nutrition: {
            calories: 195,
            protein: 23,
            carbs: 0,
            fat: 11,
            fiber: 0
        }
    },
    {
        id: 662,
        name: "جبنة عكاوي",
        nameEn: "Akkawi Cheese",
        icon: "🧀",
        category: "ألبان",
        gi: 0,
        ii: 52,
        nutrition: {
            calories: 290,
            protein: 18,
            carbs: 1.5,
            fat: 24,
            fiber: 0
        }
    },
    {
        id: 663,
        name: "جبنة بلدية",
        nameEn: "Baladi Cheese",
        icon: "🧀",
        category: "ألبان",
        gi: 0,
        ii: 48,
        nutrition: {
            calories: 265,
            protein: 20,
            carbs: 2,
            fat: 20,
            fiber: 0
        }
    },
    {
        id: 664,
        name: "جبنة مجدولة",
        nameEn: "Majdoule Cheese",
        icon: "🧀",
        category: "ألبان",
        gi: 0,
        ii: 50,
        nutrition: {
            calories: 275,
            protein: 19.5,
            carbs: 1.8,
            fat: 21.5,
            fiber: 0
        }
    },
    {
        id: 665,
        name: "شنكليش",
        nameEn: "Shanklish",
        icon: "🧀",
        category: "ألبان",
        gi: 0,
        ii: 35,
        nutrition: {
            calories: 195,
            protein: 17,
            carbs: 3.5,
            fat: 13,
            fiber: 2
        }
    },
    {
        id: 666,
        name: "جميد",
        nameEn: "Jameed",
        icon: "🧀",
        category: "ألبان",
        gi: 0,
        ii: 45,
        nutrition: {
            calories: 245,
            protein: 22,
            carbs: 4.5,
            fat: 16,
            fiber: 0
        }
    },
    {
        id: 667,
        name: "روب (زبادي)",
        nameEn: "Yogurt",
        icon: "🥛",
        category: "ألبان",
        gi: 33,
        ii: 40,
        nutrition: {
            calories: 61,
            protein: 3.5,
            carbs: 4.7,
            fat: 3.3,
            fiber: 0
        }
    },
    {
        id: 668,
        name: "عيران",
        nameEn: "Ayran",
        icon: "🥛",
        category: "مشروبات",
        gi: 30,
        ii: 35,
        nutrition: {
            calories: 38,
            protein: 2.2,
            carbs: 3.5,
            fat: 1.8,
            fiber: 0
        }
    },
    {
        id: 669,
        name: "جلاش باللحم",
        nameEn: "Meat Goulash",
        icon: "🥟",
        category: "وجبات رئيسية",
        gi: 52,
        ii: 68,
        nutrition: {
            calories: 315,
            protein: 14,
            carbs: 28,
            fat: 16,
            fiber: 1.5
        }
    },
    {
        id: 670,
        name: "سمبوسك باللحم",
        nameEn: "Meat Samosa",
        icon: "🥟",
        category: "وجبات خفيفة",
        gi: 60,
        ii: 72,
        nutrition: {
            calories: 252,
            protein: 9.5,
            carbs: 23,
            fat: 14,
            fiber: 1.8
        }
    },
    {
        id: 671,
        name: "سمبوسك بالجبن",
        nameEn: "Cheese Samosa",
        icon: "🥟",
        category: "وجبات خفيفة",
        gi: 58,
        ii: 68,
        nutrition: {
            calories: 245,
            protein: 8,
            carbs: 24,
            fat: 13.5,
            fiber: 1.5
        }
    },
    {
        id: 672,
        name: "فطاير سبانخ",
        nameEn: "Spinach Pies",
        icon: "🥟",
        category: "وجبات خفيفة",
        gi: 55,
        ii: 65,
        nutrition: {
            calories: 195,
            protein: 5.5,
            carbs: 26,
            fat: 7.5,
            fiber: 3
        }
    },
    {
        id: 673,
        name: "فطاير زعتر",
        nameEn: "Zaatar Pies",
        icon: "🥟",
        category: "وجبات خفيفة",
        gi: 60,
        ii: 70,
        nutrition: {
            calories: 215,
            protein: 4.5,
            carbs: 30,
            fat: 8.5,
            fiber: 2
        }
    },
    {
        id: 674,
        name: "مناقيش جبن",
        nameEn: "Cheese Manakish",
        icon: "🍕",
        category: "وجبات خفيفة",
        gi: 62,
        ii: 72,
        nutrition: {
            calories: 285,
            protein: 11,
            carbs: 32,
            fat: 13,
            fiber: 2
        }
    },
    {
        id: 675,
        name: "كعك بسمسم",
        nameEn: "Sesame Kaak",
        icon: "🥯",
        category: "حبوب",
        gi: 65,
        ii: 75,
        nutrition: {
            calories: 310,
            protein: 8.5,
            carbs: 48,
            fat: 10,
            fiber: 3.5
        }
    },
    {
        id: 676,
        name: "خبز الصاج",
        nameEn: "Saj Bread",
        icon: "🫓",
        category: "حبوب",
        gi: 68,
        ii: 78,
        nutrition: {
            calories: 275,
            protein: 8,
            carbs: 58,
            fat: 1.5,
            fiber: 2.5
        }
    },
    {
        id: 677,
        name: "خبز طابون",
        nameEn: "Taboon Bread",
        icon: "🍞",
        category: "حبوب",
        gi: 70,
        ii: 80,
        nutrition: {
            calories: 270,
            protein: 7.5,
            carbs: 56,
            fat: 2,
            fiber: 3
        }
    },
    {
        id: 678,
        name: "خبز تنور",
        nameEn: "Tandoor Bread",
        icon: "🫓",
        category: "حبوب",
        gi: 68,
        ii: 78,
        nutrition: {
            calories: 265,
            protein: 8,
            carbs: 54,
            fat: 2.5,
            fiber: 2.8
        }
    },
    {
        id: 679,
        name: "رقاق (خبز رقيق)",
        nameEn: "Raqaq Bread",
        icon: "🫓",
        category: "حبوب",
        gi: 72,
        ii: 82,
        nutrition: {
            calories: 290,
            protein: 7,
            carbs: 62,
            fat: 1,
            fiber: 2
        }
    },
    {
        id: 680,
        name: "خبيزة",
        nameEn: "Khubeza (Mallow)",
        icon: "🥬",
        category: "خضروات",
        gi: 15,
        ii: 18,
        nutrition: {
            calories: 29,
            protein: 3.7,
            carbs: 5.4,
            fat: 0.3,
            fiber: 2.8
        }
    },
    // فواكه استوائية ونادرة (681-720)
    {
        id: 681,
        name: "دراغون فروت",
        nameEn: "Dragon Fruit",
        icon: "🐉",
        category: "فواكه",
        gi: 48,
        ii: 50,
        nutrition: {
            calories: 60,
            protein: 1.2,
            carbs: 13,
            fat: 0,
            fiber: 3
        }
    },
    {
        id: 682,
        name: "باشن فروت",
        nameEn: "Passion Fruit",
        icon: "💜",
        category: "فواكه",
        gi: 30,
        ii: 35,
        nutrition: {
            calories: 97,
            protein: 2.2,
            carbs: 23.4,
            fat: 0.7,
            fiber: 10.4
        }
    },
    {
        id: 683,
        name: "ليتشي",
        nameEn: "Lychee",
        icon: "🍒",
        category: "فواكه",
        gi: 57,
        ii: 62,
        nutrition: {
            calories: 66,
            protein: 0.8,
            carbs: 16.5,
            fat: 0.4,
            fiber: 1.3
        }
    },
    {
        id: 684,
        name: "رامبوتان",
        nameEn: "Rambutan",
        icon: "🔴",
        category: "فواكه",
        gi: 59,
        ii: 63,
        nutrition: {
            calories: 82,
            protein: 0.9,
            carbs: 20.9,
            fat: 0.2,
            fiber: 0.9
        }
    },
    {
        id: 685,
        name: "مانجوستين",
        nameEn: "Mangosteen",
        icon: "💜",
        category: "فواكه",
        gi: 46,
        ii: 52,
        nutrition: {
            calories: 73,
            protein: 0.4,
            carbs: 17.9,
            fat: 0.6,
            fiber: 1.8
        }
    },
    {
        id: 686,
        name: "دوريان",
        nameEn: "Durian",
        icon: "🌰",
        category: "فواكه",
        gi: 49,
        ii: 55,
        nutrition: {
            calories: 147,
            protein: 1.5,
            carbs: 27.1,
            fat: 5.3,
            fiber: 3.8
        }
    },
    {
        id: 687,
        name: "جاك فروت",
        nameEn: "Jackfruit",
        icon: "🍈",
        category: "فواكه",
        gi: 75,
        ii: 80,
        nutrition: {
            calories: 95,
            protein: 1.7,
            carbs: 23.2,
            fat: 0.6,
            fiber: 1.5
        }
    },
    {
        id: 688,
        name: "كرامبولا (فاكهة النجمة)",
        nameEn: "Star Fruit",
        icon: "⭐",
        category: "فواكه",
        gi: 45,
        ii: 48,
        nutrition: {
            calories: 31,
            protein: 1,
            carbs: 6.7,
            fat: 0.3,
            fiber: 2.8
        }
    },
    {
        id: 689,
        name: "جوافة",
        nameEn: "Guava",
        icon: "🍐",
        category: "فواكه",
        gi: 30,
        ii: 38,
        nutrition: {
            calories: 68,
            protein: 2.6,
            carbs: 14.3,
            fat: 1,
            fiber: 5.4
        }
    },
    {
        id: 690,
        name: "بابايا",
        nameEn: "Papaya",
        icon: "🟠",
        category: "فواكه",
        gi: 60,
        ii: 65,
        nutrition: {
            calories: 43,
            protein: 0.5,
            carbs: 10.8,
            fat: 0.3,
            fiber: 1.7
        }
    },
    {
        id: 691,
        name: "تين شوكي",
        nameEn: "Prickly Pear",
        icon: "🌵",
        category: "فواكه",
        gi: 45,
        ii: 50,
        nutrition: {
            calories: 41,
            protein: 0.7,
            carbs: 9.6,
            fat: 0.5,
            fiber: 3.6
        }
    },
    {
        id: 692,
        name: "كمكوات",
        nameEn: "Kumquat",
        icon: "🟠",
        category: "فواكه",
        gi: 35,
        ii: 40,
        nutrition: {
            calories: 71,
            protein: 1.9,
            carbs: 15.9,
            fat: 0.9,
            fiber: 6.5
        }
    },
    {
        id: 693,
        name: "أكي دنيا (إسكدنيا)",
        nameEn: "Loquat",
        icon: "🍊",
        category: "فواكه",
        gi: 55,
        ii: 58,
        nutrition: {
            calories: 47,
            protein: 0.4,
            carbs: 12.1,
            fat: 0.2,
            fiber: 1.7
        }
    },
    {
        id: 694,
        name: "فيجوا",
        nameEn: "Feijoa",
        icon: "🥝",
        category: "فواكه",
        gi: 40,
        ii: 45,
        nutrition: {
            calories: 55,
            protein: 1.2,
            carbs: 13,
            fat: 0.6,
            fiber: 6.4
        }
    },
    {
        id: 695,
        name: "خرما",
        nameEn: "Persimmon",
        icon: "🟠",
        category: "فواكه",
        gi: 50,
        ii: 55,
        nutrition: {
            calories: 70,
            protein: 0.6,
            carbs: 18.6,
            fat: 0.2,
            fiber: 3.6
        }
    },
    {
        id: 696,
        name: "كيوانو (خيار أفريقي)",
        nameEn: "Kiwano",
        icon: "🥒",
        category: "فواكه",
        gi: 25,
        ii: 30,
        nutrition: {
            calories: 44,
            protein: 1.8,
            carbs: 7.6,
            fat: 1.3,
            fiber: 0.5
        }
    },
    {
        id: 697,
        name: "أكاي",
        nameEn: "Acai Berry",
        icon: "🫐",
        category: "فواكه",
        gi: 42,
        ii: 45,
        nutrition: {
            calories: 70,
            protein: 1,
            carbs: 4,
            fat: 5,
            fiber: 2
        }
    },
    {
        id: 698,
        name: "غوجي بيري",
        nameEn: "Goji Berry",
        icon: "🔴",
        category: "فواكه",
        gi: 29,
        ii: 35,
        nutrition: {
            calories: 349,
            protein: 14.3,
            carbs: 77.1,
            fat: 0.4,
            fiber: 13
        }
    },
    {
        id: 699,
        name: "تمر هندي",
        nameEn: "Tamarind",
        icon: "🌰",
        category: "فواكه",
        gi: 23,
        ii: 30,
        nutrition: {
            calories: 239,
            protein: 2.8,
            carbs: 62.5,
            fat: 0.6,
            fiber: 5.1
        }
    },
    {
        id: 700,
        name: "كرز هندي (أملا)",
        nameEn: "Indian Gooseberry",
        icon: "🟢",
        category: "فواكه",
        gi: 20,
        ii: 25,
        nutrition: {
            calories: 44,
            protein: 0.9,
            carbs: 10.2,
            fat: 0.6,
            fiber: 4.3
        }
    },
    {
        id: 701,
        name: "كوسكوس",
        nameEn: "Couscous",
        icon: "🍚",
        category: "حبوب",
        gi: 65,
        ii: 72,
        nutrition: {
            calories: 112,
            protein: 3.8,
            carbs: 23.2,
            fat: 0.2,
            fiber: 1.4
        }
    },
    {
        id: 702,
        name: "برغل خشن",
        nameEn: "Coarse Bulgur",
        icon: "🌾",
        category: "حبوب",
        gi: 48,
        ii: 55,
        nutrition: {
            calories: 342,
            protein: 12.3,
            carbs: 75.9,
            fat: 1.3,
            fiber: 18.3
        }
    },
    {
        id: 703,
        name: "فريكة",
        nameEn: "Freekeh",
        icon: "🌾",
        category: "حبوب",
        gi: 43,
        ii: 50,
        nutrition: {
            calories: 325,
            protein: 12.7,
            carbs: 72,
            fat: 2.3,
            fiber: 16.5
        }
    },
    {
        id: 704,
        name: "سميد",
        nameEn: "Semolina",
        icon: "🌾",
        category: "حبوب",
        gi: 60,
        ii: 68,
        nutrition: {
            calories: 360,
            protein: 12.7,
            carbs: 72.8,
            fat: 1.1,
            fiber: 3.9
        }
    },
    {
        id: 705,
        name: "دقيق الذرة",
        nameEn: "Corn Flour",
        icon: "🌽",
        category: "حبوب",
        gi: 70,
        ii: 75,
        nutrition: {
            calories: 361,
            protein: 6.9,
            carbs: 76.9,
            fat: 3.9,
            fiber: 7.3
        }
    },
    {
        id: 706,
        name: "دقيق الحمص",
        nameEn: "Chickpea Flour",
        icon: "🫘",
        category: "بقوليات",
        gi: 35,
        ii: 42,
        nutrition: {
            calories: 387,
            protein: 22.4,
            carbs: 57.8,
            fat: 6.7,
            fiber: 10.8
        }
    },
    {
        id: 707,
        name: "دقيق اللوز",
        nameEn: "Almond Flour",
        icon: "🥜",
        category: "مكسرات",
        gi: 0,
        ii: 10,
        nutrition: {
            calories: 571,
            protein: 21.2,
            carbs: 21.4,
            fat: 50,
            fiber: 10.7
        }
    },
    {
        id: 708,
        name: "دقيق جوز الهند",
        nameEn: "Coconut Flour",
        icon: "🥥",
        category: "مكسرات",
        gi: 45,
        ii: 35,
        nutrition: {
            calories: 400,
            protein: 19.3,
            carbs: 60,
            fat: 8.7,
            fiber: 38.5
        }
    },
    {
        id: 709,
        name: "نخالة القمح",
        nameEn: "Wheat Bran",
        icon: "🌾",
        category: "حبوب",
        gi: 30,
        ii: 35,
        nutrition: {
            calories: 216,
            protein: 15.6,
            carbs: 64.5,
            fat: 4.2,
            fiber: 42.8
        }
    },
    {
        id: 710,
        name: "نخالة الشوفان",
        nameEn: "Oat Bran",
        icon: "🌾",
        category: "حبوب",
        gi: 55,
        ii: 60,
        nutrition: {
            calories: 246,
            protein: 17.3,
            carbs: 66.2,
            fat: 7,
            fiber: 15.4
        }
    },
    {
        id: 711,
        name: "جنين القمح",
        nameEn: "Wheat Germ",
        icon: "🌾",
        category: "حبوب",
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 360,
            protein: 23.2,
            carbs: 51.8,
            fat: 9.7,
            fiber: 13.2
        }
    },
    {
        id: 712,
        name: "طحينة سائلة",
        nameEn: "Liquid Tahini",
        icon: "🥜",
        category: "مكسرات",
        gi: 12,
        ii: 18,
        nutrition: {
            calories: 595,
            protein: 17,
            carbs: 21.2,
            fat: 53.8,
            fiber: 9.3
        }
    },
    {
        id: 713,
        name: "زبدة كاجو",
        nameEn: "Cashew Butter",
        icon: "🥜",
        category: "مكسرات",
        gi: 27,
        ii: 32,
        nutrition: {
            calories: 587,
            protein: 17.6,
            carbs: 27.6,
            fat: 49.4,
            fiber: 2
        }
    },
    {
        id: 714,
        name: "زبدة اللوز",
        nameEn: "Almond Butter",
        icon: "🥜",
        category: "مكسرات",
        gi: 0,
        ii: 15,
        nutrition: {
            calories: 614,
            protein: 21,
            carbs: 18.8,
            fat: 55.5,
            fiber: 10.3
        }
    },
    {
        id: 715,
        name: "زبدة بذور عباد الشمس",
        nameEn: "Sunflower Seed Butter",
        icon: "🌻",
        category: "مكسرات",
        gi: 30,
        ii: 35,
        nutrition: {
            calories: 617,
            protein: 17.2,
            carbs: 20,
            fat: 55.8,
            fiber: 8.8
        }
    },
    {
        id: 716,
        name: "شراب القيقب",
        nameEn: "Maple Syrup",
        icon: "🍁",
        category: "محليات",
        gi: 54,
        ii: 60,
        nutrition: {
            calories: 260,
            protein: 0,
            carbs: 67,
            fat: 0.1,
            fiber: 0
        }
    },
    {
        id: 717,
        name: "دبس الرمان",
        nameEn: "Pomegranate Molasses",
        icon: "🍇",
        category: "محليات",
        gi: 60,
        ii: 65,
        nutrition: {
            calories: 250,
            protein: 1,
            carbs: 65,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 718,
        name: "دبس التمر",
        nameEn: "Date Syrup",
        icon: "🌴",
        category: "محليات",
        gi: 68,
        ii: 72,
        nutrition: {
            calories: 287,
            protein: 2,
            carbs: 75,
            fat: 0,
            fiber: 0.5
        }
    },
    {
        id: 719,
        name: "رب البندورة (معجون طماطم)",
        nameEn: "Tomato Paste",
        icon: "🍅",
        category: "خضروات",
        gi: 27,
        ii: 35,
        nutrition: {
            calories: 82,
            protein: 4.3,
            carbs: 18.9,
            fat: 0.5,
            fiber: 4.1
        }
    },
    {
        id: 720,
        name: "صلصة الصويا",
        nameEn: "Soy Sauce",
        icon: "🥫",
        category: "بهارات",
        gi: 0,
        ii: 15,
        nutrition: {
            calories: 53,
            protein: 5.6,
            carbs: 4.9,
            fat: 0.1,
            fiber: 0.8
        }
    },
    // منتجات ألبان متنوعة (721-730)
    {
        id: 721,
        name: "جبن الكواركيزو",
        nameEn: "Queso Fresco",
        icon: "🧀",
        category: "ألبان",
        gi: 30,
        ii: 55,
        nutrition: {
            calories: 100,
            protein: 8,
            carbs: 2,
            fat: 7,
            fiber: 0
        }
    },
    {
        id: 722,
        name: "جبن الماسكاربوني",
        nameEn: "Mascarpone",
        icon: "🧀",
        category: "ألبان",
        gi: 30,
        ii: 60,
        nutrition: {
            calories: 430,
            protein: 3,
            carbs: 5,
            fat: 44,
            fiber: 0
        }
    },
    {
        id: 723,
        name: "زبادي الماعز",
        nameEn: "Goat Yogurt",
        icon: "🥛",
        category: "ألبان",
        gi: 35,
        ii: 60,
        nutrition: {
            calories: 69,
            protein: 3.5,
            carbs: 4.7,
            fat: 3.8,
            fiber: 0
        }
    },
    {
        id: 724,
        name: "زبادي الأغنام",
        nameEn: "Sheep Yogurt",
        icon: "🥛",
        category: "ألبان",
        gi: 35,
        ii: 65,
        nutrition: {
            calories: 108,
            protein: 5.5,
            carbs: 5.4,
            fat: 7,
            fiber: 0
        }
    },
    {
        id: 725,
        name: "الكفير",
        nameEn: "Kefir",
        icon: "🥛",
        category: "ألبان",
        gi: 30,
        ii: 40,
        nutrition: {
            calories: 41,
            protein: 3.3,
            carbs: 4.5,
            fat: 1,
            fiber: 0
        }
    },
    {
        id: 726,
        name: "الأيران (مشروب اللبن)",
        nameEn: "Ayran",
        icon: "🥤",
        category: "ألبان",
        gi: 35,
        ii: 50,
        nutrition: {
            calories: 38,
            protein: 1.5,
            carbs: 1.9,
            fat: 3,
            fiber: 0
        }
    },
    {
        id: 727,
        name: "جبن الريكوتا قليل الدسم",
        nameEn: "Low-Fat Ricotta",
        icon: "🧀",
        category: "ألبان",
        gi: 30,
        ii: 55,
        nutrition: {
            calories: 138,
            protein: 11.4,
            carbs: 5.1,
            fat: 8,
            fiber: 0
        }
    },
    {
        id: 728,
        name: "حليب الجاموس",
        nameEn: "Buffalo Milk",
        icon: "🥛",
        category: "ألبان",
        gi: 40,
        ii: 70,
        nutrition: {
            calories: 97,
            protein: 3.8,
            carbs: 5.2,
            fat: 6.9,
            fiber: 0
        }
    },
    {
        id: 729,
        name: "زبدة الغنم",
        nameEn: "Sheep Butter",
        icon: "🧈",
        category: "ألبان",
        gi: 0,
        ii: 25,
        nutrition: {
            calories: 717,
            protein: 0.9,
            carbs: 0.1,
            fat: 81,
            fiber: 0
        }
    },
    {
        id: 730,
        name: "اللبنة المصفاة",
        nameEn: "Strained Labneh",
        icon: "🥛",
        category: "ألبان",
        gi: 30,
        ii: 55,
        nutrition: {
            calories: 80,
            protein: 5,
            carbs: 3,
            fat: 6,
            fiber: 0
        }
    },
    // مأكولات بحرية متنوعة (731-740)
    {
        id: 731,
        name: "السلمون المدخن",
        nameEn: "Smoked Salmon",
        icon: "🐟",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 50,
        nutrition: {
            calories: 117,
            protein: 18.3,
            carbs: 0,
            fat: 4.3,
            fiber: 0
        }
    },
    {
        id: 732,
        name: "سمك الماكريل",
        nameEn: "Mackerel",
        icon: "🐟",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 55,
        nutrition: {
            calories: 205,
            protein: 18.6,
            carbs: 0,
            fat: 13.9,
            fiber: 0
        }
    },
    {
        id: 733,
        name: "سمك السردين",
        nameEn: "Sardines",
        icon: "🐟",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 50,
        nutrition: {
            calories: 208,
            protein: 24.6,
            carbs: 0,
            fat: 11.5,
            fiber: 0
        }
    },
    {
        id: 734,
        name: "الكافيار",
        nameEn: "Caviar",
        icon: "🥚",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 45,
        nutrition: {
            calories: 264,
            protein: 24.6,
            carbs: 4,
            fat: 17.9,
            fiber: 0
        }
    },
    {
        id: 735,
        name: "سمك الهلبوت",
        nameEn: "Halibut",
        icon: "🐟",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 45,
        nutrition: {
            calories: 111,
            protein: 22.5,
            carbs: 0,
            fat: 2.3,
            fiber: 0
        }
    },
    {
        id: 736,
        name: "الحبار (كاليماري)",
        nameEn: "Squid (Calamari)",
        icon: "🦑",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 40,
        nutrition: {
            calories: 92,
            protein: 15.6,
            carbs: 3.1,
            fat: 1.4,
            fiber: 0
        }
    },
    {
        id: 737,
        name: "الأخطبوط",
        nameEn: "Octopus",
        icon: "🐙",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 40,
        nutrition: {
            calories: 82,
            protein: 14.9,
            carbs: 2.2,
            fat: 1,
            fiber: 0
        }
    },
    {
        id: 738,
        name: "بلح البحر",
        nameEn: "Mussels",
        icon: "🦪",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 50,
        nutrition: {
            calories: 86,
            protein: 11.9,
            carbs: 3.7,
            fat: 2.2,
            fiber: 0
        }
    },
    {
        id: 739,
        name: "المحار",
        nameEn: "Oysters",
        icon: "🦪",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 45,
        nutrition: {
            calories: 68,
            protein: 7,
            carbs: 3.9,
            fat: 2.5,
            fiber: 0
        }
    },
    {
        id: 740,
        name: "سلطعون الثلج",
        nameEn: "Snow Crab",
        icon: "🦀",
        category: "مأكولات بحرية",
        gi: 0,
        ii: 48,
        nutrition: {
            calories: 90,
            protein: 18.5,
            carbs: 0,
            fat: 1.2,
            fiber: 0
        }
    },
    // أعشاب وتوابل طبيعية (741-750)
    {
        id: 741,
        name: "الكركم الطازج",
        nameEn: "Fresh Turmeric",
        icon: "🟡",
        category: "بهارات",
        gi: 15,
        ii: 10,
        nutrition: {
            calories: 312,
            protein: 9.7,
            carbs: 67.1,
            fat: 3.3,
            fiber: 22.7
        }
    },
    {
        id: 742,
        name: "الزنجبيل الطازج",
        nameEn: "Fresh Ginger",
        icon: "🟤",
        category: "بهارات",
        gi: 15,
        ii: 12,
        nutrition: {
            calories: 80,
            protein: 1.8,
            carbs: 17.8,
            fat: 0.8,
            fiber: 2
        }
    },
    {
        id: 743,
        name: "القرفة السيلانية",
        nameEn: "Ceylon Cinnamon",
        icon: "🟫",
        category: "بهارات",
        gi: 5,
        ii: 5,
        nutrition: {
            calories: 247,
            protein: 4,
            carbs: 80.6,
            fat: 1.2,
            fiber: 53.1
        }
    },
    {
        id: 744,
        name: "الهيل الأخضر",
        nameEn: "Green Cardamom",
        icon: "💚",
        category: "بهارات",
        gi: 10,
        ii: 8,
        nutrition: {
            calories: 311,
            protein: 10.8,
            carbs: 68.5,
            fat: 6.7,
            fiber: 28
        }
    },
    {
        id: 745,
        name: "القرنفل",
        nameEn: "Cloves",
        icon: "🟤",
        category: "بهارات",
        gi: 10,
        ii: 8,
        nutrition: {
            calories: 274,
            protein: 6,
            carbs: 65.5,
            fat: 13,
            fiber: 33.9
        }
    },
    {
        id: 746,
        name: "جوزة الطيب",
        nameEn: "Nutmeg",
        icon: "🟫",
        category: "بهارات",
        gi: 10,
        ii: 8,
        nutrition: {
            calories: 525,
            protein: 5.8,
            carbs: 49.3,
            fat: 36.3,
            fiber: 20.8
        }
    },
    {
        id: 747,
        name: "الزعفران",
        nameEn: "Saffron",
        icon: "🟡",
        category: "بهارات",
        gi: 5,
        ii: 5,
        nutrition: {
            calories: 310,
            protein: 11.4,
            carbs: 65.4,
            fat: 5.9,
            fiber: 3.9
        }
    },
    {
        id: 748,
        name: "الريحان المجفف",
        nameEn: "Dried Basil",
        icon: "🌿",
        category: "بهارات",
        gi: 10,
        ii: 8,
        nutrition: {
            calories: 233,
            protein: 22.9,
            carbs: 47.8,
            fat: 4,
            fiber: 37.7
        }
    },
    {
        id: 749,
        name: "إكليل الجبل المجفف",
        nameEn: "Dried Rosemary",
        icon: "🌿",
        category: "بهارات",
        gi: 10,
        ii: 8,
        nutrition: {
            calories: 331,
            protein: 4.9,
            carbs: 64.1,
            fat: 15.2,
            fiber: 42.6
        }
    },
    {
        id: 750,
        name: "الزعتر البري المجفف",
        nameEn: "Dried Wild Thyme",
        icon: "🌿",
        category: "بهارات",
        gi: 10,
        ii: 8,
        nutrition: {
            calories: 276,
            protein: 9.1,
            carbs: 63.9,
            fat: 7.4,
            fiber: 37
        }
    },
    // أطعمة عربية تقليدية إضافية (751-800)
    {
        id: 751,
        name: "الملوخية الطازجة",
        nameEn: "Fresh Molokhia",
        icon: "🥬",
        category: "خضروات",
        gi: 15,
        ii: 10,
        nutrition: {
            calories: 58,
            protein: 4.8,
            carbs: 9.8,
            fat: 0.4,
            fiber: 2
        }
    },
    {
        id: 752,
        name: "الملوخية المجففة",
        nameEn: "Dried Molokhia",
        icon: "🌿",
        category: "خضروات",
        gi: 15,
        ii: 12,
        nutrition: {
            calories: 345,
            protein: 26,
            carbs: 58,
            fat: 4,
            fiber: 11
        }
    },
    {
        id: 753,
        name: "الفتة المصرية",
        nameEn: "Egyptian Fatta",
        icon: "🍲",
        category: "أطباق عربية",
        gi: 68,
        ii: 72,
        nutrition: {
            calories: 285,
            protein: 12,
            carbs: 38,
            fat: 9,
            fiber: 3
        }
    },
    {
        id: 754,
        name: "الكشري المصري",
        nameEn: "Egyptian Koshari",
        icon: "🍝",
        category: "أطباق عربية",
        gi: 62,
        ii: 58,
        nutrition: {
            calories: 320,
            protein: 11,
            carbs: 58,
            fat: 5,
            fiber: 8
        }
    },
    {
        id: 755,
        name: "المحشي (ورق عنب)",
        nameEn: "Stuffed Grape Leaves",
        icon: "🍃",
        category: "أطباق عربية",
        gi: 54,
        ii: 48,
        nutrition: {
            calories: 180,
            protein: 3.5,
            carbs: 26,
            fat: 7,
            fiber: 4
        }
    },
    {
        id: 756,
        name: "المحشي (كوسا)",
        nameEn: "Stuffed Zucchini",
        icon: "🥒",
        category: "أطباق عربية",
        gi: 50,
        ii: 45,
        nutrition: {
            calories: 155,
            protein: 5,
            carbs: 22,
            fat: 5.5,
            fiber: 3.5
        }
    },
    {
        id: 757,
        name: "المحشي (باذنجان)",
        nameEn: "Stuffed Eggplant",
        icon: "🍆",
        category: "أطباق عربية",
        gi: 48,
        ii: 42,
        nutrition: {
            calories: 165,
            protein: 4.5,
            carbs: 24,
            fat: 6,
            fiber: 5
        }
    },
    {
        id: 758,
        name: "الفلافل",
        nameEn: "Falafel",
        icon: "🧆",
        category: "أطباق عربية",
        gi: 45,
        ii: 40,
        nutrition: {
            calories: 333,
            protein: 13.3,
            carbs: 31.8,
            fat: 17.8,
            fiber: 4.9
        }
    },
    {
        id: 759,
        name: "الطعمية المصرية",
        nameEn: "Egyptian Taamiya",
        icon: "🧆",
        category: "أطباق عربية",
        gi: 42,
        ii: 38,
        nutrition: {
            calories: 315,
            protein: 14,
            carbs: 29,
            fat: 16,
            fiber: 6
        }
    },
    {
        id: 760,
        name: "الشكشوكة",
        nameEn: "Shakshuka",
        icon: "🍳",
        category: "أطباق عربية",
        gi: 35,
        ii: 42,
        nutrition: {
            calories: 189,
            protein: 11,
            carbs: 12,
            fat: 11,
            fiber: 3
        }
    },
    {
        id: 761,
        name: "المسخن الفلسطيني",
        nameEn: "Palestinian Musakhan",
        icon: "🍗",
        category: "أطباق عربية",
        gi: 58,
        ii: 62,
        nutrition: {
            calories: 385,
            protein: 24,
            carbs: 32,
            fat: 18,
            fiber: 2.5
        }
    },
    {
        id: 762,
        name: "المجدرة",
        nameEn: "Mujaddara",
        icon: "🍚",
        category: "أطباق عربية",
        gi: 52,
        ii: 45,
        nutrition: {
            calories: 195,
            protein: 8,
            carbs: 35,
            fat: 2.5,
            fiber: 6
        }
    },
    {
        id: 763,
        name: "المفتول الفلسطيني",
        nameEn: "Palestinian Maftoul",
        icon: "🌾",
        category: "أطباق عربية",
        gi: 55,
        ii: 50,
        nutrition: {
            calories: 170,
            protein: 6,
            carbs: 34,
            fat: 1,
            fiber: 4
        }
    },
    {
        id: 764,
        name: "الفريكة",
        nameEn: "Freekeh",
        icon: "🌾",
        category: "حبوب",
        gi: 43,
        ii: 38,
        nutrition: {
            calories: 130,
            protein: 5,
            carbs: 26,
            fat: 0.8,
            fiber: 8
        }
    },
    {
        id: 765,
        name: "البرغل الناعم",
        nameEn: "Fine Bulgur",
        icon: "🌾",
        category: "حبوب",
        gi: 48,
        ii: 42,
        nutrition: {
            calories: 342,
            protein: 12.3,
            carbs: 75.9,
            fat: 1.3,
            fiber: 12.5
        }
    },
    {
        id: 766,
        name: "البرغل الخشن",
        nameEn: "Coarse Bulgur",
        icon: "🌾",
        category: "حبوب",
        gi: 46,
        ii: 40,
        nutrition: {
            calories: 342,
            protein: 12.3,
            carbs: 75.9,
            fat: 1.3,
            fiber: 18.3
        }
    },
    {
        id: 767,
        name: "التبولة",
        nameEn: "Tabbouleh",
        icon: "🥗",
        category: "أطباق عربية",
        gi: 42,
        ii: 35,
        nutrition: {
            calories: 120,
            protein: 3.5,
            carbs: 15,
            fat: 6,
            fiber: 3.5
        }
    },
    {
        id: 768,
        name: "الفتوش",
        nameEn: "Fattoush",
        icon: "🥗",
        category: "أطباق عربية",
        gi: 48,
        ii: 40,
        nutrition: {
            calories: 98,
            protein: 2.5,
            carbs: 12,
            fat: 5,
            fiber: 3
        }
    },
    {
        id: 769,
        name: "المتبل (بابا غنوج)",
        nameEn: "Mutabal (Baba Ghanoush)",
        icon: "🍆",
        category: "مقبلات",
        gi: 30,
        ii: 25,
        nutrition: {
            calories: 107,
            protein: 2.4,
            carbs: 8.7,
            fat: 7.9,
            fiber: 4
        }
    },
    {
        id: 770,
        name: "المحمرة",
        nameEn: "Muhammara",
        icon: "🌶️",
        category: "مقبلات",
        gi: 42,
        ii: 38,
        nutrition: {
            calories: 168,
            protein: 4.2,
            carbs: 13,
            fat: 11.5,
            fiber: 3
        }
    },
    {
        id: 771,
        name: "اللبنة",
        nameEn: "Labneh",
        icon: "🥛",
        category: "ألبان",
        gi: 30,
        ii: 55,
        nutrition: {
            calories: 80,
            protein: 5,
            carbs: 3,
            fat: 6,
            fiber: 0
        }
    },
    {
        id: 772,
        name: "الجميد (جميد الأردني)",
        nameEn: "Jameed",
        icon: "🧀",
        category: "ألبان",
        gi: 30,
        ii: 60,
        nutrition: {
            calories: 110,
            protein: 7,
            carbs: 4,
            fat: 8,
            fiber: 0
        }
    },
    {
        id: 773,
        name: "القشطة العربية",
        nameEn: "Arabic Qashta",
        icon: "🥛",
        category: "ألبان",
        gi: 35,
        ii: 65,
        nutrition: {
            calories: 340,
            protein: 3,
            carbs: 5,
            fat: 35,
            fiber: 0
        }
    },
    {
        id: 774,
        name: "الشنينة (لبن رائب)",
        nameEn: "Shenina",
        icon: "🥛",
        category: "ألبان",
        gi: 35,
        ii: 50,
        nutrition: {
            calories: 52,
            protein: 3.2,
            carbs: 5,
            fat: 2,
            fiber: 0
        }
    },
    {
        id: 775,
        name: "الكليجا",
        nameEn: "Kleija",
        icon: "🥮",
        category: "حلويات",
        gi: 72,
        ii: 75,
        nutrition: {
            calories: 415,
            protein: 5,
            carbs: 58,
            fat: 18,
            fiber: 2
        }
    },
    {
        id: 776,
        name: "القطايف",
        nameEn: "Qatayef",
        icon: "🥞",
        category: "حلويات",
        gi: 70,
        ii: 72,
        nutrition: {
            calories: 295,
            protein: 4.5,
            carbs: 48,
            fat: 10,
            fiber: 1.5
        }
    },
    {
        id: 777,
        name: "الكنافة النابلسية",
        nameEn: "Nabulsi Kunafa",
        icon: "🧀",
        category: "حلويات",
        gi: 75,
        ii: 78,
        nutrition: {
            calories: 385,
            protein: 8,
            carbs: 52,
            fat: 16,
            fiber: 1
        }
    },
    {
        id: 778,
        name: "البسبوسة",
        nameEn: "Basbousa",
        icon: "🍰",
        category: "حلويات",
        gi: 72,
        ii: 75,
        nutrition: {
            calories: 345,
            protein: 5.2,
            carbs: 48,
            fat: 15,
            fiber: 1.2
        }
    },
    {
        id: 779,
        name: "الهريسة الحلبية",
        nameEn: "Aleppian Harissa",
        icon: "🍰",
        category: "حلويات",
        gi: 70,
        ii: 73,
        nutrition: {
            calories: 365,
            protein: 6,
            carbs: 50,
            fat: 16,
            fiber: 1.5
        }
    },
    {
        id: 780,
        name: "القطر (الشيرة)",
        nameEn: "Sugar Syrup (Qater)",
        icon: "🍯",
        category: "حلويات",
        gi: 85,
        ii: 90,
        nutrition: {
            calories: 260,
            protein: 0,
            carbs: 65,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 781,
        name: "الشاورما (دجاج)",
        nameEn: "Chicken Shawarma",
        icon: "🌯",
        category: "أطباق عربية",
        gi: 55,
        ii: 58,
        nutrition: {
            calories: 225,
            protein: 18,
            carbs: 12,
            fat: 12,
            fiber: 2
        }
    },
    {
        id: 782,
        name: "الشاورما (لحم)",
        nameEn: "Beef Shawarma",
        icon: "🌯",
        category: "أطباق عربية",
        gi: 52,
        ii: 62,
        nutrition: {
            calories: 265,
            protein: 20,
            carbs: 10,
            fat: 16,
            fiber: 1.5
        }
    },
    {
        id: 783,
        name: "الكباب الحلبي",
        nameEn: "Aleppian Kebab",
        icon: "🍢",
        category: "أطباق عربية",
        gi: 0,
        ii: 65,
        nutrition: {
            calories: 285,
            protein: 24,
            carbs: 2,
            fat: 20,
            fiber: 0.5
        }
    },
    {
        id: 784,
        name: "الكفتة المشوية",
        nameEn: "Grilled Kofta",
        icon: "🍢",
        category: "أطباق عربية",
        gi: 0,
        ii: 60,
        nutrition: {
            calories: 255,
            protein: 22,
            carbs: 4,
            fat: 17,
            fiber: 1
        }
    },
    {
        id: 785,
        name: "الكبة النية",
        nameEn: "Raw Kibbeh",
        icon: "🥩",
        category: "أطباق عربية",
        gi: 42,
        ii: 55,
        nutrition: {
            calories: 195,
            protein: 15,
            carbs: 18,
            fat: 7,
            fiber: 3
        }
    },
    {
        id: 786,
        name: "الكبة المقلية",
        nameEn: "Fried Kibbeh",
        icon: "🥟",
        category: "أطباق عربية",
        gi: 58,
        ii: 62,
        nutrition: {
            calories: 365,
            protein: 14,
            carbs: 28,
            fat: 22,
            fiber: 2.5
        }
    },
    {
        id: 787,
        name: "السمبوسك باللحم",
        nameEn: "Meat Samosa",
        icon: "🥟",
        category: "أطباق عربية",
        gi: 60,
        ii: 65,
        nutrition: {
            calories: 295,
            protein: 10,
            carbs: 26,
            fat: 17,
            fiber: 2
        }
    },
    {
        id: 788,
        name: "الرقاق باللحم",
        nameEn: "Ruqaq with Meat",
        icon: "🥙",
        category: "أطباق عربية",
        gi: 55,
        ii: 58,
        nutrition: {
            calories: 245,
            protein: 12,
            carbs: 28,
            fat: 10,
            fiber: 2
        }
    },
    {
        id: 789,
        name: "الفطير المشلتت",
        nameEn: "Feteer Meshaltet",
        icon: "🥐",
        category: "مخبوزات",
        gi: 68,
        ii: 70,
        nutrition: {
            calories: 425,
            protein: 7,
            carbs: 52,
            fat: 21,
            fiber: 2
        }
    },
    {
        id: 790,
        name: "الصاج (خبز صاج)",
        nameEn: "Saj Bread",
        icon: "🫓",
        category: "مخبوزات",
        gi: 70,
        ii: 68,
        nutrition: {
            calories: 265,
            protein: 8,
            carbs: 55,
            fat: 1.5,
            fiber: 2
        }
    },
    {
        id: 791,
        name: "المرقوق",
        nameEn: "Marqooq",
        icon: "🍲",
        category: "أطباق عربية",
        gi: 58,
        ii: 55,
        nutrition: {
            calories: 215,
            protein: 11,
            carbs: 28,
            fat: 7,
            fiber: 3.5
        }
    },
    {
        id: 792,
        name: "الجريش السعودي",
        nameEn: "Saudi Jareesh",
        icon: "🍚",
        category: "أطباق عربية",
        gi: 50,
        ii: 48,
        nutrition: {
            calories: 185,
            protein: 8,
            carbs: 32,
            fat: 3,
            fiber: 4.5
        }
    },
    {
        id: 793,
        name: "القرصان",
        nameEn: "Qursan",
        icon: "🍲",
        category: "أطباق عربية",
        gi: 55,
        ii: 52,
        nutrition: {
            calories: 235,
            protein: 10,
            carbs: 34,
            fat: 7,
            fiber: 4
        }
    },
    {
        id: 794,
        name: "الهريس",
        nameEn: "Harees",
        icon: "🥣",
        category: "أطباق عربية",
        gi: 62,
        ii: 65,
        nutrition: {
            calories: 245,
            protein: 12,
            carbs: 38,
            fat: 5,
            fiber: 3
        }
    },
    {
        id: 795,
        name: "العريكة",
        nameEn: "Areeka",
        icon: "🍯",
        category: "حلويات",
        gi: 75,
        ii: 78,
        nutrition: {
            calories: 425,
            protein: 6,
            carbs: 55,
            fat: 20,
            fiber: 2
        }
    },
    {
        id: 796,
        name: "القهوة العربية",
        nameEn: "Arabic Coffee",
        icon: "☕",
        category: "مشروبات",
        gi: 0,
        ii: 15,
        nutrition: {
            calories: 2,
            protein: 0.3,
            carbs: 0,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 797,
        name: "الشاي بالنعناع",
        nameEn: "Mint Tea",
        icon: "🍵",
        category: "مشروبات",
        gi: 0,
        ii: 10,
        nutrition: {
            calories: 2,
            protein: 0,
            carbs: 0.5,
            fat: 0,
            fiber: 0
        }
    },
    {
        id: 798,
        name: "السحلب",
        nameEn: "Sahlab",
        icon: "🥛",
        category: "مشروبات",
        gi: 55,
        ii: 60,
        nutrition: {
            calories: 145,
            protein: 4,
            carbs: 22,
            fat: 4.5,
            fiber: 0.5
        }
    },
    {
        id: 799,
        name: "التمر الهندي",
        nameEn: "Tamarind Drink",
        icon: "🥤",
        category: "مشروبات",
        gi: 42,
        ii: 38,
        nutrition: {
            calories: 85,
            protein: 0.5,
            carbs: 21,
            fat: 0.2,
            fiber: 1
        }
    },
    {
        id: 800,
        name: "الخروب",
        nameEn: "Carob Drink",
        icon: "🥤",
        category: "مشروبات",
        gi: 40,
        ii: 35,
        nutrition: {
            calories: 95,
            protein: 0.8,
            carbs: 23,
            fat: 0.3,
            fiber: 1.5
        }
    },
    // مشروبات كحولية (لأغراض تعليمية وصحية فقط)
    {
        id: 801,
        name: "بيرة عادية",
        nameEn: "Regular Beer",
        icon: "🍺",
        category: "مشروبات كحولية",
        gi: 0,
        ii: 15,
        nutrition: {
            calories: 43,
            protein: 0.5,
            carbs: 3.6,
            fat: 0,
            fiber: 0,
            alcohol: 4.0
        },
        warning: "⚠️ يحتوي على كحول (4%). يضر الكبد والدماغ. يسبب الإدمان. ممنوع للحوامل."
    },
    {
        id: 802,
        name: "بيرة خفيفة",
        nameEn: "Light Beer",
        icon: "🍺",
        category: "مشروبات كحولية",
        gi: 0,
        ii: 10,
        nutrition: {
            calories: 29,
            protein: 0.2,
            carbs: 1.6,
            fat: 0,
            fiber: 0,
            alcohol: 3.5
        },
        warning: "⚠️ يحتوي على كحول (3.5%). يضر الكبد والدماغ. يسبب الإدمان. ممنوع للحوامل."
    },
    {
        id: 803,
        name: "نبيذ أحمر",
        nameEn: "Red Wine",
        icon: "🍷",
        category: "مشروبات كحولية",
        gi: 0,
        ii: 3,
        nutrition: {
            calories: 85,
            protein: 0.1,
            carbs: 2.6,
            fat: 0,
            fiber: 0,
            alcohol: 10.6
        },
        warning: "⚠️ يحتوي على كحول (13%). يضر الكبد والقلب والدماغ. يسبب الإدمان. ممنوع للحوامل."
    },
    {
        id: 804,
        name: "نبيذ أبيض",
        nameEn: "White Wine",
        icon: "🍷",
        category: "مشروبات كحولية",
        gi: 0,
        ii: 3,
        nutrition: {
            calories: 82,
            protein: 0.1,
            carbs: 2.1,
            fat: 0,
            fiber: 0,
            alcohol: 10.4
        },
        warning: "⚠️ يحتوي على كحول (12.5%). يضر الكبد والقلب. يسبب الإدمان. ممنوع للحوامل."
    },
    {
        id: 805,
        name: "شامبانيا",
        nameEn: "Champagne",
        icon: "🍾",
        category: "مشروبات كحولية",
        gi: 0,
        ii: 5,
        nutrition: {
            calories: 89,
            protein: 0.2,
            carbs: 3.8,
            fat: 0,
            fiber: 0,
            alcohol: 10.0
        },
        warning: "⚠️ يحتوي على كحول (12%). يضر الكبد والدماغ. يسبب الإدمان. ممنوع للحوامل."
    },
    {
        id: 806,
        name: "ويسكي",
        nameEn: "Whiskey",
        icon: "🥃",
        category: "مشروبات كحولية",
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 250,
            protein: 0,
            carbs: 0,
            fat: 0,
            fiber: 0,
            alcohol: 33.4
        },
        warning: "⚠️ يحتوي على كحول (40%). خطر جداً على الكبد والدماغ. يسبب الإدمان الشديد. ممنوع للحوامل."
    },
    {
        id: 807,
        name: "فودكا",
        nameEn: "Vodka",
        icon: "🥃",
        category: "مشروبات كحولية",
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 231,
            protein: 0,
            carbs: 0,
            fat: 0,
            fiber: 0,
            alcohol: 33.4
        },
        warning: "⚠️ يحتوي على كحول (40%). خطر جداً على الكبد والدماغ. يسبب الإدمان الشديد. ممنوع للحوامل."
    },
    {
        id: 808,
        name: "روم",
        nameEn: "Rum",
        icon: "🥃",
        category: "مشروبات كحولية",
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 231,
            protein: 0,
            carbs: 0,
            fat: 0,
            fiber: 0,
            alcohol: 33.4
        },
        warning: "⚠️ يحتوي على كحول (40%). خطر جداً على الكبد والدماغ. يسبب الإدمان الشديد. ممنوع للحوامل."
    },
    {
        id: 809,
        name: "جن",
        nameEn: "Gin",
        icon: "🥃",
        category: "مشروبات كحولية",
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 263,
            protein: 0,
            carbs: 0,
            fat: 0,
            fiber: 0,
            alcohol: 37.5
        },
        warning: "⚠️ يحتوي على كحول (45%). خطر جداً على الكبد والدماغ. يسبب الإدمان الشديد. ممنوع للحوامل."
    },
    {
        id: 810,
        name: "تيكيلا",
        nameEn: "Tequila",
        icon: "🥃",
        category: "مشروبات كحولية",
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 231,
            protein: 0,
            carbs: 0,
            fat: 0,
            fiber: 0,
            alcohol: 33.4
        },
        warning: "⚠️ يحتوي على كحول (40%). خطر جداً على الكبد والدماغ. يسبب الإدمان الشديد. ممنوع للحوامل."
    },
    {
        id: 811,
        name: "براندي",
        nameEn: "Brandy",
        icon: "🥃",
        category: "مشروبات كحولية",
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 231,
            protein: 0,
            carbs: 0,
            fat: 0,
            fiber: 0,
            alcohol: 33.4
        },
        warning: "⚠️ يحتوي على كحول (40%). خطر جداً على الكبد والقلب. يسبب الإدمان الشديد. ممنوع للحوامل."
    },
    {
        id: 812,
        name: "كونياك",
        nameEn: "Cognac",
        icon: "🥃",
        category: "مشروبات كحولية",
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 239,
            protein: 0,
            carbs: 0,
            fat: 0,
            fiber: 0,
            alcohol: 34.5
        },
        warning: "⚠️ يحتوي على كحول (41%). خطر جداً على الكبد والقلب. يسبب الإدمان الشديد. ممنوع للحوامل."
    },
    {
        id: 813,
        name: "ساكي (نبيذ أرز ياباني)",
        nameEn: "Sake",
        icon: "🍶",
        category: "مشروبات كحولية",
        gi: 0,
        ii: 5,
        nutrition: {
            calories: 134,
            protein: 0.5,
            carbs: 5.0,
            fat: 0,
            fiber: 0,
            alcohol: 15.6
        },
        warning: "⚠️ يحتوي على كحول (15-20%). يضر الكبد والدماغ. يسبب الإدمان. ممنوع للحوامل."
    },
    {
        id: 814,
        name: "موهيتو",
        nameEn: "Mojito",
        icon: "🍹",
        category: "مشروبات كحولية",
        gi: 15,
        ii: 18,
        nutrition: {
            calories: 168,
            protein: 0.2,
            carbs: 20,
            fat: 0.1,
            fiber: 0,
            alcohol: 10.0
        },
        warning: "⚠️ يحتوي على كحول وسكر عالي. يضر الكبد والدماغ. يسبب الإدمان. ممنوع للحوامل."
    },
    {
        id: 815,
        name: "مارغريتا",
        nameEn: "Margarita",
        icon: "🍹",
        category: "مشروبات كحولية",
        gi: 18,
        ii: 20,
        nutrition: {
            calories: 168,
            protein: 0,
            carbs: 13,
            fat: 0.1,
            fiber: 0.2,
            alcohol: 11.7
        },
        warning: "⚠️ يحتوي على كحول وسكر. يضر الكبد والدماغ. يسبب الإدمان. ممنوع للحوامل."
    },
    {
        id: 816,
        name: "بينا كولادا",
        nameEn: "Pina Colada",
        icon: "🍹",
        category: "مشروبات كحولية",
        gi: 25,
        ii: 28,
        nutrition: {
            calories: 245,
            protein: 0.8,
            carbs: 32,
            fat: 2.9,
            fiber: 0.5,
            alcohol: 10.0
        },
        warning: "⚠️ يحتوي على كحول وسكر ودهون عالية. يضر الكبد. يسبب السمنة والإدمان. ممنوع للحوامل."
    },
    {
        id: 817,
        name: "كوزموبوليتان",
        nameEn: "Cosmopolitan",
        icon: "🍸",
        category: "مشروبات كحولية",
        gi: 12,
        ii: 15,
        nutrition: {
            calories: 146,
            protein: 0,
            carbs: 10,
            fat: 0,
            fiber: 0,
            alcohol: 13.0
        },
        warning: "⚠️ يحتوي على كحول عالي وسكر. يضر الكبد والدماغ. يسبب الإدمان. ممنوع للحوامل."
    },
    {
        id: 818,
        name: "مارتيني",
        nameEn: "Martini",
        icon: "🍸",
        category: "مشروبات كحولية",
        gi: 0,
        ii: 0,
        nutrition: {
            calories: 176,
            protein: 0,
            carbs: 0.3,
            fat: 0,
            fiber: 0,
            alcohol: 21.5
        },
        warning: "⚠️ يحتوي على كحول عالي جداً (26%). خطر على الكبد والدماغ. يسبب الإدمان الشديد. ممنوع للحوامل."
    },
    {
        id: 819,
        name: "دايكيري",
        nameEn: "Daiquiri",
        icon: "🍹",
        category: "مشروبات كحولية",
        gi: 20,
        ii: 22,
        nutrition: {
            calories: 186,
            protein: 0.1,
            carbs: 15,
            fat: 0,
            fiber: 0.1,
            alcohol: 13.4
        },
        warning: "⚠️ يحتوي على كحول وسكر عالي. يضر الكبد والدماغ. يسبب الإدمان. ممنوع للحوامل."
    },
    {
        id: 820,
        name: "سانجريا",
        nameEn: "Sangria",
        icon: "🍷",
        category: "مشروبات كحولية",
        gi: 22,
        ii: 25,
        nutrition: {
            calories: 125,
            protein: 0.3,
            carbs: 13,
            fat: 0.2,
            fiber: 0.5,
            alcohol: 8.9
        },
        warning: "⚠️ يحتوي على كحول وسكر من الفواكه. يضر الكبد. يسبب الإدمان. ممنوع للحوامل."
    },
    // أطعمة عالمية شهيرة
    {
        id: 821,
        name: "بيتزا مارغريتا",
        nameEn: "Pizza Margherita",
        icon: "🍕",
        category: "أطعمة إيطالية",
        gi: 60,
        ii: 70,
        nutrition: {
            calories: 266,
            protein: 11,
            carbs: 33,
            fat: 10,
            fiber: 2.5
        }
    },
    {
        id: 822,
        name: "بيتزا بيبروني",
        nameEn: "Pepperoni Pizza",
        icon: "🍕",
        category: "أطعمة إيطالية",
        gi: 60,
        ii: 75,
        nutrition: {
            calories: 298,
            protein: 12,
            carbs: 34,
            fat: 13,
            fiber: 2.3
        }
    },
    {
        id: 823,
        name: "سباغيتي بولونيز",
        nameEn: "Spaghetti Bolognese",
        icon: "🍝",
        category: "أطعمة إيطالية",
        gi: 52,
        ii: 58,
        nutrition: {
            calories: 182,
            protein: 8,
            carbs: 27,
            fat: 5,
            fiber: 2.8
        }
    },
    {
        id: 824,
        name: "لازانيا باللحم",
        nameEn: "Meat Lasagna",
        icon: "🍝",
        category: "أطعمة إيطالية",
        gi: 55,
        ii: 65,
        nutrition: {
            calories: 195,
            protein: 11,
            carbs: 18,
            fat: 9,
            fiber: 2.2
        }
    },
    {
        id: 825,
        name: "فيتوتشيني ألفريدو",
        nameEn: "Fettuccine Alfredo",
        icon: "🍝",
        category: "أطعمة إيطالية",
        gi: 50,
        ii: 60,
        nutrition: {
            calories: 320,
            protein: 10,
            carbs: 38,
            fat: 14,
            fiber: 2
        }
    },
    {
        id: 826,
        name: "ريزوتو بالفطر",
        nameEn: "Mushroom Risotto",
        icon: "🍚",
        category: "أطعمة إيطالية",
        gi: 69,
        ii: 62,
        nutrition: {
            calories: 166,
            protein: 4.5,
            carbs: 26,
            fat: 5,
            fiber: 1.5
        }
    },
    {
        id: 827,
        name: "كرواسون سادة",
        nameEn: "Plain Croissant",
        icon: "🥐",
        category: "أطعمة فرنسية",
        gi: 67,
        ii: 79,
        nutrition: {
            calories: 406,
            protein: 8,
            carbs: 46,
            fat: 21,
            fiber: 2.6
        }
    },
    {
        id: 828,
        name: "كرواسون بالشوكولاتة",
        nameEn: "Chocolate Croissant",
        icon: "🥐",
        category: "أطعمة فرنسية",
        gi: 70,
        ii: 85,
        nutrition: {
            calories: 450,
            protein: 7.5,
            carbs: 52,
            fat: 24,
            fiber: 2.8
        }
    },
    {
        id: 829,
        name: "باغيت فرنسي",
        nameEn: "French Baguette",
        icon: "🥖",
        category: "أطعمة فرنسية",
        gi: 75,
        ii: 95,
        nutrition: {
            calories: 272,
            protein: 9,
            carbs: 55,
            fat: 1.6,
            fiber: 3
        }
    },
    {
        id: 830,
        name: "كيش لورين",
        nameEn: "Quiche Lorraine",
        icon: "🥧",
        category: "أطعمة فرنسية",
        gi: 40,
        ii: 55,
        nutrition: {
            calories: 350,
            protein: 14,
            carbs: 22,
            fat: 23,
            fiber: 1.2
        }
    },
    {
        id: 831,
        name: "كريب بالنوتيلا",
        nameEn: "Nutella Crepe",
        icon: "🥞",
        category: "أطعمة فرنسية",
        gi: 65,
        ii: 75,
        nutrition: {
            calories: 380,
            protein: 7,
            carbs: 52,
            fat: 16,
            fiber: 2
        }
    },
    {
        id: 832,
        name: "برغر لحم بقري",
        nameEn: "Beef Burger",
        icon: "🍔",
        category: "أطعمة أمريكية",
        gi: 66,
        ii: 74,
        nutrition: {
            calories: 295,
            protein: 17,
            carbs: 24,
            fat: 14,
            fiber: 1.5
        }
    },
    {
        id: 833,
        name: "تشيز برغر",
        nameEn: "Cheeseburger",
        icon: "🍔",
        category: "أطعمة أمريكية",
        gi: 66,
        ii: 80,
        nutrition: {
            calories: 354,
            protein: 20,
            carbs: 25,
            fat: 19,
            fiber: 1.5
        }
    },
    {
        id: 834,
        name: "هوت دوج",
        nameEn: "Hot Dog",
        icon: "🌭",
        category: "أطعمة أمريكية",
        gi: 65,
        ii: 73,
        nutrition: {
            calories: 290,
            protein: 10,
            carbs: 25,
            fat: 17,
            fiber: 1
        }
    },
    {
        id: 835,
        name: "بانكيك بالعسل",
        nameEn: "Pancakes with Syrup",
        icon: "🥞",
        category: "أطعمة أمريكية",
        gi: 67,
        ii: 82,
        nutrition: {
            calories: 227,
            protein: 6,
            carbs: 38,
            fat: 6,
            fiber: 1.5
        }
    },
    {
        id: 836,
        name: "وافل بلجيكي",
        nameEn: "Belgian Waffle",
        icon: "🧇",
        category: "أطعمة أمريكية",
        gi: 76,
        ii: 85,
        nutrition: {
            calories: 310,
            protein: 7,
            carbs: 41,
            fat: 13,
            fiber: 1.8
        }
    },
    {
        id: 837,
        name: "ناتشوز بالجبن",
        nameEn: "Nachos with Cheese",
        icon: "🧀",
        category: "أطعمة مكسيكية",
        gi: 55,
        ii: 65,
        nutrition: {
            calories: 346,
            protein: 9,
            carbs: 36,
            fat: 19,
            fiber: 4
        }
    },
    {
        id: 838,
        name: "تاكو لحم بقري",
        nameEn: "Beef Taco",
        icon: "🌮",
        category: "أطعمة مكسيكية",
        gi: 50,
        ii: 60,
        nutrition: {
            calories: 226,
            protein: 11,
            carbs: 20,
            fat: 11,
            fiber: 3.5
        }
    },
    {
        id: 839,
        name: "بوريتو دجاج",
        nameEn: "Chicken Burrito",
        icon: "🌯",
        category: "أطعمة مكسيكية",
        gi: 55,
        ii: 65,
        nutrition: {
            calories: 380,
            protein: 20,
            carbs: 48,
            fat: 12,
            fiber: 5
        }
    },
    {
        id: 840,
        name: "كويساديلا بالجبن",
        nameEn: "Cheese Quesadilla",
        icon: "🫓",
        category: "أطعمة مكسيكية",
        gi: 52,
        ii: 70,
        nutrition: {
            calories: 380,
            protein: 16,
            carbs: 32,
            fat: 21,
            fiber: 3
        }
    },
    {
        id: 841,
        name: "جواكامولي",
        nameEn: "Guacamole",
        icon: "🥑",
        category: "أطعمة مكسيكية",
        gi: 15,
        ii: 18,
        nutrition: {
            calories: 161,
            protein: 2,
            carbs: 9,
            fat: 15,
            fiber: 7
        }
    },
    {
        id: 842,
        name: "موساكا يونانية",
        nameEn: "Greek Moussaka",
        icon: "🍆",
        category: "أطعمة يونانية",
        gi: 45,
        ii: 50,
        nutrition: {
            calories: 180,
            protein: 9,
            carbs: 12,
            fat: 11,
            fiber: 3
        }
    },
    {
        id: 843,
        name: "سوفلاكي دجاج",
        nameEn: "Chicken Souvlaki",
        icon: "�串",
        category: "أطعمة يونانية",
        gi: 40,
        ii: 45,
        nutrition: {
            calories: 230,
            protein: 28,
            carbs: 5,
            fat: 10,
            fiber: 1
        }
    },
    {
        id: 844,
        name: "جيروس (شاورما يونانية)",
        nameEn: "Gyros",
        icon: "🥙",
        category: "أطعمة يونانية",
        gi: 57,
        ii: 62,
        nutrition: {
            calories: 350,
            protein: 21,
            carbs: 35,
            fat: 13,
            fiber: 2.5
        }
    },
    {
        id: 845,
        name: "سلطة يونانية",
        nameEn: "Greek Salad",
        icon: "🥗",
        category: "أطعمة يونانية",
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 156,
            protein: 5,
            carbs: 8,
            fat: 12,
            fiber: 3
        }
    },
    {
        id: 846,
        name: "دولماس (ورق عنب يوناني)",
        nameEn: "Dolmas",
        icon: "🍃",
        category: "أطعمة يونانية",
        gi: 35,
        ii: 40,
        nutrition: {
            calories: 90,
            protein: 2,
            carbs: 13,
            fat: 3.5,
            fiber: 2.5
        }
    },
    {
        id: 847,
        name: "باييلا إسبانية",
        nameEn: "Spanish Paella",
        icon: "🥘",
        category: "أطعمة إسبانية",
        gi: 58,
        ii: 62,
        nutrition: {
            calories: 215,
            protein: 12,
            carbs: 28,
            fat: 6,
            fiber: 2
        }
    },
    {
        id: 848,
        name: "تورتيلا إسبانية",
        nameEn: "Spanish Tortilla",
        icon: "🥚",
        category: "أطعمة إسبانية",
        gi: 48,
        ii: 55,
        nutrition: {
            calories: 190,
            protein: 8,
            carbs: 15,
            fat: 11,
            fiber: 1.8
        }
    },
    {
        id: 849,
        name: "تشوروس بالشوكولاتة",
        nameEn: "Churros with Chocolate",
        icon: "🍩",
        category: "أطعمة إسبانية",
        gi: 75,
        ii: 85,
        nutrition: {
            calories: 380,
            protein: 5,
            carbs: 51,
            fat: 18,
            fiber: 2
        }
    },
    {
        id: 850,
        name: "فلافل",
        nameEn: "Falafel",
        icon: "🧆",
        category: "أطعمة شرق أوسطية",
        gi: 35,
        ii: 40,
        nutrition: {
            calories: 333,
            protein: 13,
            carbs: 31,
            fat: 18,
            fiber: 6
        }
    },
    {
        id: 851,
        name: "شاورما دجاج عربية",
        nameEn: "Chicken Shawarma Wrap",
        icon: "🌯",
        category: "أطعمة شرق أوسطية",
        gi: 57,
        ii: 65,
        nutrition: {
            calories: 350,
            protein: 24,
            carbs: 38,
            fat: 11,
            fiber: 3
        }
    },
    {
        id: 852,
        name: "كباب مشوي",
        nameEn: "Grilled Kebab",
        icon: "🍢",
        category: "أطعمة شرق أوسطية",
        gi: 0,
        ii: 35,
        nutrition: {
            calories: 270,
            protein: 25,
            carbs: 2,
            fat: 18,
            fiber: 0
        }
    },
    {
        id: 853,
        name: "منسف أردني",
        nameEn: "Jordanian Mansaf",
        icon: "🍚",
        category: "أطعمة شرق أوسطية",
        gi: 60,
        ii: 65,
        nutrition: {
            calories: 420,
            protein: 22,
            carbs: 45,
            fat: 16,
            fiber: 2
        }
    },
    {
        id: 854,
        name: "سمك مشوي",
        nameEn: "Grilled Fish",
        icon: "🐟",
        category: "أطعمة بحرية",
        gi: 0,
        ii: 28,
        nutrition: {
            calories: 165,
            protein: 25,
            carbs: 0,
            fat: 6.5,
            fiber: 0
        }
    },
    {
        id: 855,
        name: "روبيان (جمبري) مشوي",
        nameEn: "Grilled Shrimp",
        icon: "🍤",
        category: "أطعمة بحرية",
        gi: 0,
        ii: 25,
        nutrition: {
            calories: 99,
            protein: 24,
            carbs: 0.2,
            fat: 0.3,
            fiber: 0
        }
    },
    {
        id: 856,
        name: "سلمون مشوي",
        nameEn: "Grilled Salmon",
        icon: "🐟",
        category: "أطعمة بحرية",
        gi: 0,
        ii: 30,
        nutrition: {
            calories: 206,
            protein: 22,
            carbs: 0,
            fat: 13,
            fiber: 0
        }
    },
    {
        id: 857,
        name: "سي فود مقلي",
        nameEn: "Fried Seafood",
        icon: "🦐",
        category: "أطعمة بحرية",
        gi: 45,
        ii: 55,
        nutrition: {
            calories: 340,
            protein: 18,
            carbs: 22,
            fat: 20,
            fiber: 1
        }
    },
    {
        id: 858,
        name: "سوشي كاليفورنيا رول",
        nameEn: "California Roll",
        icon: "🍣",
        category: "أطعمة يابانية",
        gi: 55,
        ii: 58,
        nutrition: {
            calories: 140,
            protein: 6,
            carbs: 19,
            fat: 4.5,
            fiber: 1.5
        }
    },
    {
        id: 859,
        name: "سوشي سالمون",
        nameEn: "Salmon Sushi",
        icon: "🍣",
        category: "أطعمة يابانية",
        gi: 52,
        ii: 55,
        nutrition: {
            calories: 180,
            protein: 9,
            carbs: 21,
            fat: 7,
            fiber: 1
        }
    },
    {
        id: 860,
        name: "دجاج تيرياكي",
        nameEn: "Chicken Teriyaki",
        icon: "🍗",
        category: "أطعمة يابانية",
        gi: 45,
        ii: 52,
        nutrition: {
            calories: 240,
            protein: 28,
            carbs: 18,
            fat: 6,
            fiber: 1
        }
    },
    {
        id: 861,
        name: "دجاج كاتسو",
        nameEn: "Chicken Katsu",
        icon: "🍗",
        category: "أطعمة يابانية",
        gi: 55,
        ii: 65,
        nutrition: {
            calories: 320,
            protein: 22,
            carbs: 28,
            fat: 14,
            fiber: 2
        }
    },
    {
        id: 862,
        name: "تشاو مين (نودلز صيني)",
        nameEn: "Chow Mein",
        icon: "🍜",
        category: "أطعمة صينية",
        gi: 53,
        ii: 60,
        nutrition: {
            calories: 237,
            protein: 8,
            carbs: 26,
            fat: 11,
            fiber: 2.5
        }
    },
    {
        id: 863,
        name: "دجاج بالليمون صيني",
        nameEn: "Chinese Lemon Chicken",
        icon: "🍗",
        category: "أطعمة صينية",
        gi: 60,
        ii: 70,
        nutrition: {
            calories: 380,
            protein: 20,
            carbs: 42,
            fat: 15,
            fiber: 1.5
        }
    },
    {
        id: 864,
        name: "سبرينج رول (لفائف ربيع)",
        nameEn: "Spring Rolls",
        icon: "🥟",
        category: "أطعمة صينية",
        gi: 48,
        ii: 55,
        nutrition: {
            calories: 140,
            protein: 4,
            carbs: 18,
            fat: 6,
            fiber: 2
        }
    },
    {
        id: 865,
        name: "دمبلنغ (زلابية صينية)",
        nameEn: "Dumplings",
        icon: "🥟",
        category: "أطعمة صينية",
        gi: 50,
        ii: 58,
        nutrition: {
            calories: 175,
            protein: 7,
            carbs: 21,
            fat: 7,
            fiber: 1.5
        }
    },
    {
        id: 866,
        name: "أرز مقلي صيني",
        nameEn: "Chinese Fried Rice",
        icon: "🍚",
        category: "أطعمة صينية",
        gi: 68,
        ii: 72,
        nutrition: {
            calories: 228,
            protein: 5,
            carbs: 33,
            fat: 8,
            fiber: 1.5
        }
    },
    {
        id: 867,
        name: "فيش آند تشيبس",
        nameEn: "Fish and Chips",
        icon: "🐟",
        category: "أطعمة بريطانية",
        gi: 65,
        ii: 70,
        nutrition: {
            calories: 450,
            protein: 22,
            carbs: 42,
            fat: 22,
            fiber: 3.5
        }
    },
    {
        id: 868,
        name: "بيض بنديكت",
        nameEn: "Eggs Benedict",
        icon: "🍳",
        category: "أطعمة أمريكية",
        gi: 48,
        ii: 60,
        nutrition: {
            calories: 440,
            protein: 19,
            carbs: 28,
            fat: 28,
            fiber: 1.5
        }
    },
    {
        id: 869,
        name: "ساندويش كلوب",
        nameEn: "Club Sandwich",
        icon: "🥪",
        category: "ساندويشات",
        gi: 55,
        ii: 65,
        nutrition: {
            calories: 390,
            protein: 24,
            carbs: 36,
            fat: 16,
            fiber: 3
        }
    },
    {
        id: 870,
        name: "ساندويش تونة",
        nameEn: "Tuna Sandwich",
        icon: "🥪",
        category: "ساندويشات",
        gi: 52,
        ii: 58,
        nutrition: {
            calories: 287,
            protein: 16,
            carbs: 29,
            fat: 12,
            fiber: 2.5
        }
    },
    // حلويات ومخبوزات عالمية (40 عنصر)
    {
        id: 871,
        name: "كيك شوكولاتة",
        nameEn: "Chocolate Cake",
        icon: "🍰",
        category: "حلويات",
        gi: 65,
        ii: 75,
        nutrition: {
            calories: 352,
            protein: 5,
            carbs: 50,
            fat: 16,
            fiber: 2
        }
    },
    {
        id: 872,
        name: "كيك فانيليا",
        nameEn: "Vanilla Cake",
        icon: "🍰",
        category: "حلويات",
        gi: 67,
        ii: 77,
        nutrition: {
            calories: 340,
            protein: 4.5,
            carbs: 48,
            fat: 15,
            fiber: 1.5
        }
    },
    {
        id: 873,
        name: "ريد فلفت كيك",
        nameEn: "Red Velvet Cake",
        icon: "🍰",
        category: "حلويات",
        gi: 68,
        ii: 80,
        nutrition: {
            calories: 385,
            protein: 5,
            carbs: 52,
            fat: 18,
            fiber: 1.8
        }
    },
    {
        id: 874,
        name: "تشيز كيك",
        nameEn: "Cheesecake",
        icon: "🍰",
        category: "حلويات",
        gi: 55,
        ii: 65,
        nutrition: {
            calories: 321,
            protein: 6,
            carbs: 26,
            fat: 23,
            fiber: 0.5
        }
    },
    {
        id: 875,
        name: "تيراميسو",
        nameEn: "Tiramisu",
        icon: "🍰",
        category: "حلويات",
        gi: 60,
        ii: 70,
        nutrition: {
            calories: 240,
            protein: 5,
            carbs: 28,
            fat: 12,
            fiber: 0.8
        }
    },
    {
        id: 876,
        name: "براوني بالشوكولاتة",
        nameEn: "Chocolate Brownie",
        icon: "🍫",
        category: "حلويات",
        gi: 70,
        ii: 80,
        nutrition: {
            calories: 466,
            protein: 6,
            carbs: 60,
            fat: 24,
            fiber: 3
        }
    },
    {
        id: 877,
        name: "كوكيز شوكولاتة تشيب",
        nameEn: "Chocolate Chip Cookies",
        icon: "🍪",
        category: "حلويات",
        gi: 65,
        ii: 72,
        nutrition: {
            calories: 488,
            protein: 5,
            carbs: 67,
            fat: 23,
            fiber: 2.5
        }
    },
    {
        id: 878,
        name: "بسكويت أوريو",
        nameEn: "Oreo Cookies",
        icon: "🍪",
        category: "حلويات",
        gi: 67,
        ii: 75,
        nutrition: {
            calories: 437,
            protein: 4,
            carbs: 71,
            fat: 16,
            fiber: 2.9
        }
    },
    {
        id: 879,
        name: "دونات محلاة",
        nameEn: "Glazed Donut",
        icon: "🍩",
        category: "حلويات",
        gi: 76,
        ii: 88,
        nutrition: {
            calories: 255,
            protein: 3.5,
            carbs: 31,
            fat: 14,
            fiber: 0.9
        }
    },
    {
        id: 880,
        name: "دونات بالشوكولاتة",
        nameEn: "Chocolate Donut",
        icon: "🍩",
        category: "حلويات",
        gi: 78,
        ii: 90,
        nutrition: {
            calories: 270,
            protein: 4,
            carbs: 35,
            fat: 15,
            fiber: 1.2
        }
    },
    {
        id: 881,
        name: "كب كيك",
        nameEn: "Cupcake",
        icon: "🧁",
        category: "حلويات",
        gi: 72,
        ii: 82,
        nutrition: {
            calories: 305,
            protein: 3.5,
            carbs: 44,
            fat: 13,
            fiber: 1
        }
    },
    {
        id: 882,
        name: "مافن توت أزرق",
        nameEn: "Blueberry Muffin",
        icon: "🧁",
        category: "حلويات",
        gi: 59,
        ii: 68,
        nutrition: {
            calories: 340,
            protein: 5,
            carbs: 52,
            fat: 13,
            fiber: 2.5
        }
    },
    {
        id: 883,
        name: "سينابون",
        nameEn: "Cinnamon Roll",
        icon: "🥐",
        category: "حلويات",
        gi: 75,
        ii: 85,
        nutrition: {
            calories: 420,
            protein: 7,
            carbs: 62,
            fat: 16,
            fiber: 2
        }
    },
    {
        id: 884,
        name: "آيس كريم فانيليا",
        nameEn: "Vanilla Ice Cream",
        icon: "🍦",
        category: "حلويات",
        gi: 57,
        ii: 70,
        nutrition: {
            calories: 207,
            protein: 3.5,
            carbs: 24,
            fat: 11,
            fiber: 0.7
        }
    },
    {
        id: 885,
        name: "آيس كريم شوكولاتة",
        nameEn: "Chocolate Ice Cream",
        icon: "🍦",
        category: "حلويات",
        gi: 60,
        ii: 73,
        nutrition: {
            calories: 216,
            protein: 3.8,
            carbs: 28,
            fat: 11,
            fiber: 1.5
        }
    },
    {
        id: 886,
        name: "آيس كريم فراولة",
        nameEn: "Strawberry Ice Cream",
        icon: "🍦",
        category: "حلويات",
        gi: 56,
        ii: 68,
        nutrition: {
            calories: 192,
            protein: 3.2,
            carbs: 24,
            fat: 9,
            fiber: 0.9
        }
    },
    {
        id: 887,
        name: "كريم بروليه",
        nameEn: "Creme Brulee",
        icon: "🍮",
        category: "حلويات",
        gi: 50,
        ii: 60,
        nutrition: {
            calories: 288,
            protein: 5,
            carbs: 26,
            fat: 18,
            fiber: 0
        }
    },
    {
        id: 888,
        name: "بودينغ شوكولاتة",
        nameEn: "Chocolate Pudding",
        icon: "🍮",
        category: "حلويات",
        gi: 47,
        ii: 58,
        nutrition: {
            calories: 156,
            protein: 4,
            carbs: 26,
            fat: 4.5,
            fiber: 1.2
        }
    },
    {
        id: 889,
        name: "موس شوكولاتة",
        nameEn: "Chocolate Mousse",
        icon: "🍫",
        category: "حلويات",
        gi: 45,
        ii: 55,
        nutrition: {
            calories: 189,
            protein: 3,
            carbs: 17,
            fat: 13,
            fiber: 1.5
        }
    },
    {
        id: 890,
        name: "إكلير بالشوكولاتة",
        nameEn: "Chocolate Eclair",
        icon: "🍩",
        category: "حلويات",
        gi: 60,
        ii: 70,
        nutrition: {
            calories: 262,
            protein: 6,
            carbs: 24,
            fat: 16,
            fiber: 1
        }
    },
    {
        id: 891,
        name: "ميلك شيك شوكولاتة",
        nameEn: "Chocolate Milkshake",
        icon: "🥤",
        category: "مشروبات",
        gi: 55,
        ii: 68,
        nutrition: {
            calories: 270,
            protein: 8,
            carbs: 40,
            fat: 9,
            fiber: 1.5
        }
    },
    {
        id: 892,
        name: "ميلك شيك فانيليا",
        nameEn: "Vanilla Milkshake",
        icon: "🥤",
        category: "مشروبات",
        gi: 52,
        ii: 65,
        nutrition: {
            calories: 254,
            protein: 8,
            carbs: 38,
            fat: 8,
            fiber: 0.5
        }
    },
    {
        id: 893,
        name: "فرابتشينو كراميل",
        nameEn: "Caramel Frappuccino",
        icon: "🥤",
        category: "مشروبات",
        gi: 58,
        ii: 70,
        nutrition: {
            calories: 380,
            protein: 5,
            carbs: 58,
            fat: 15,
            fiber: 0
        }
    },
    {
        id: 894,
        name: "لاتيه كراميل",
        nameEn: "Caramel Latte",
        icon: "☕",
        category: "مشروبات",
        gi: 45,
        ii: 55,
        nutrition: {
            calories: 250,
            protein: 9,
            carbs: 34,
            fat: 9,
            fiber: 0
        }
    },
    {
        id: 895,
        name: "كابتشينو",
        nameEn: "Cappuccino",
        icon: "☕",
        category: "مشروبات",
        gi: 35,
        ii: 40,
        nutrition: {
            calories: 120,
            protein: 6,
            carbs: 12,
            fat: 5,
            fiber: 0
        }
    },
    {
        id: 896,
        name: "هوت شوكليت",
        nameEn: "Hot Chocolate",
        icon: "☕",
        category: "مشروبات",
        gi: 50,
        ii: 62,
        nutrition: {
            calories: 192,
            protein: 9,
            carbs: 26,
            fat: 6,
            fiber: 2
        }
    },
    {
        id: 897,
        name: "بان كيك بالشوكولاتة",
        nameEn: "Chocolate Pancakes",
        icon: "🥞",
        category: "حلويات",
        gi: 70,
        ii: 85,
        nutrition: {
            calories: 280,
            protein: 7,
            carbs: 42,
            fat: 9,
            fiber: 2.5
        }
    },
    {
        id: 898,
        name: "فرينش توست",
        nameEn: "French Toast",
        icon: "🍞",
        category: "حلويات",
        gi: 62,
        ii: 75,
        nutrition: {
            calories: 240,
            protein: 8,
            carbs: 34,
            fat: 8,
            fiber: 1.5
        }
    },
    {
        id: 899,
        name: "كرواسون باللوز",
        nameEn: "Almond Croissant",
        icon: "🥐",
        category: "حلويات",
        gi: 65,
        ii: 78,
        nutrition: {
            calories: 446,
            protein: 9,
            carbs: 50,
            fat: 24,
            fiber: 3
        }
    },
    {
        id: 900,
        name: "دانش (معجنات دانماركية)",
        nameEn: "Danish Pastry",
        icon: "🥐",
        category: "حلويات",
        gi: 70,
        ii: 80,
        nutrition: {
            calories: 374,
            protein: 6,
            carbs: 45,
            fat: 19,
            fiber: 2
        }
    },
    {
        id: 901,
        name: "بسكويت الزنجبيل",
        nameEn: "Gingerbread Cookies",
        icon: "🍪",
        category: "حلويات",
        gi: 68,
        ii: 75,
        nutrition: {
            calories: 355,
            protein: 4,
            carbs: 62,
            fat: 10,
            fiber: 1.5
        }
    },
    {
        id: 902,
        name: "ماكارون فرنسي",
        nameEn: "French Macaron",
        icon: "🍪",
        category: "حلويات",
        gi: 60,
        ii: 70,
        nutrition: {
            calories: 140,
            protein: 2.5,
            carbs: 19,
            fat: 6.5,
            fiber: 0.8
        }
    },
    {
        id: 903,
        name: "بروفيترول",
        nameEn: "Profiterole",
        icon: "🍰",
        category: "حلويات",
        gi: 58,
        ii: 68,
        nutrition: {
            calories: 175,
            protein: 4,
            carbs: 17,
            fat: 10,
            fiber: 0.5
        }
    },
    {
        id: 904,
        name: "كريم كراميل",
        nameEn: "Flan (Creme Caramel)",
        icon: "🍮",
        category: "حلويات",
        gi: 45,
        ii: 55,
        nutrition: {
            calories: 150,
            protein: 4,
            carbs: 24,
            fat: 4,
            fiber: 0
        }
    },
    {
        id: 905,
        name: "تارت الفواكه",
        nameEn: "Fruit Tart",
        icon: "🥧",
        category: "حلويات",
        gi: 55,
        ii: 62,
        nutrition: {
            calories: 250,
            protein: 3,
            carbs: 35,
            fat: 12,
            fiber: 2
        }
    },
    {
        id: 906,
        name: "تارت التفاح",
        nameEn: "Apple Pie",
        icon: "🥧",
        category: "حلويات",
        gi: 58,
        ii: 65,
        nutrition: {
            calories: 237,
            protein: 2,
            carbs: 34,
            fat: 11,
            fiber: 2
        }
    },
    {
        id: 907,
        name: "سموثي فراولة وموز",
        nameEn: "Strawberry Banana Smoothie",
        icon: "🥤",
        category: "مشروبات",
        gi: 42,
        ii: 50,
        nutrition: {
            calories: 180,
            protein: 5,
            carbs: 36,
            fat: 2,
            fiber: 3.5
        }
    },
    {
        id: 908,
        name: "بان كيك بالتوت",
        nameEn: "Berry Pancakes",
        icon: "🥞",
        category: "حلويات",
        gi: 63,
        ii: 75,
        nutrition: {
            calories: 245,
            protein: 7,
            carbs: 40,
            fat: 7,
            fiber: 3
        }
    },
    {
        id: 909,
        name: "شوكولاتة داكنة (70%)",
        nameEn: "Dark Chocolate 70%",
        icon: "🍫",
        category: "حلويات",
        gi: 23,
        ii: 25,
        nutrition: {
            calories: 598,
            protein: 8,
            carbs: 46,
            fat: 43,
            fiber: 11
        }
    },
    {
        id: 910,
        name: "شوكولاتة بالحليب",
        nameEn: "Milk Chocolate",
        icon: "🍫",
        category: "حلويات",
        gi: 43,
        ii: 50,
        nutrition: {
            calories: 535,
            protein: 8,
            carbs: 59,
            fat: 30,
            fiber: 3.5
        }
    },
    // وجبات سريعة Fast Food (30 عنصر)
    {
        id: 911,
        name: "بيج ماك",
        nameEn: "Big Mac",
        icon: "🍔",
        category: "وجبات سريعة",
        gi: 66,
        ii: 78,
        nutrition: {
            calories: 563,
            protein: 26,
            carbs: 46,
            fat: 33,
            fiber: 3.5
        }
    },
    {
        id: 912,
        name: "وابر (برغر كنج)",
        nameEn: "Whopper",
        icon: "🍔",
        category: "وجبات سريعة",
        gi: 68,
        ii: 80,
        nutrition: {
            calories: 657,
            protein: 28,
            carbs: 49,
            fat: 40,
            fiber: 2.5
        }
    },
    {
        id: 913,
        name: "دجاج مقلي (KFC)",
        nameEn: "Fried Chicken (KFC)",
        icon: "🍗",
        category: "وجبات سريعة",
        gi: 45,
        ii: 60,
        nutrition: {
            calories: 320,
            protein: 24,
            carbs: 12,
            fat: 21,
            fiber: 1
        }
    },
    {
        id: 914,
        name: "ناغتس دجاج (6 قطع)",
        nameEn: "Chicken Nuggets (6pc)",
        icon: "🍗",
        category: "وجبات سريعة",
        gi: 50,
        ii: 65,
        nutrition: {
            calories: 287,
            protein: 15,
            carbs: 18,
            fat: 18,
            fiber: 1.5
        }
    },
    {
        id: 915,
        name: "بروست دجاج",
        nameEn: "Broasted Chicken",
        icon: "🍗",
        category: "وجبات سريعة",
        gi: 42,
        ii: 58,
        nutrition: {
            calories: 290,
            protein: 26,
            carbs: 10,
            fat: 17,
            fiber: 0.8
        }
    },
    {
        id: 916,
        name: "فرايز (بطاطس مقلية)",
        nameEn: "French Fries",
        icon: "🍟",
        category: "وجبات سريعة",
        gi: 75,
        ii: 89,
        nutrition: {
            calories: 312,
            protein: 3.4,
            carbs: 41,
            fat: 15,
            fiber: 3.8
        }
    },
    {
        id: 917,
        name: "أونيون رينجز",
        nameEn: "Onion Rings",
        icon: "🧅",
        category: "وجبات سريعة",
        gi: 70,
        ii: 80,
        nutrition: {
            calories: 411,
            protein: 5,
            carbs: 46,
            fat: 23,
            fiber: 2.5
        }
    },
    {
        id: 918,
        name: "موزاريلا ستيكس",
        nameEn: "Mozzarella Sticks",
        icon: "🧀",
        category: "وجبات سريعة",
        gi: 55,
        ii: 70,
        nutrition: {
            calories: 280,
            protein: 13,
            carbs: 22,
            fat: 16,
            fiber: 1.2
        }
    },
    {
        id: 919,
        name: "كرسبي تشيكن ساندويش",
        nameEn: "Crispy Chicken Sandwich",
        icon: "🥪",
        category: "وجبات سريعة",
        gi: 60,
        ii: 72,
        nutrition: {
            calories: 470,
            protein: 22,
            carbs: 42,
            fat: 24,
            fiber: 2.5
        }
    },
    {
        id: 920,
        name: "فيش فيليه ساندويش",
        nameEn: "Fish Fillet Sandwich",
        icon: "🥪",
        category: "وجبات سريعة",
        gi: 58,
        ii: 68,
        nutrition: {
            calories: 390,
            protein: 15,
            carbs: 39,
            fat: 19,
            fiber: 2
        }
    },
    {
        id: 921,
        name: "بيتزا هت بيبروني (شريحة)",
        nameEn: "Pizza Hut Pepperoni (slice)",
        icon: "🍕",
        category: "وجبات سريعة",
        gi: 62,
        ii: 75,
        nutrition: {
            calories: 313,
            protein: 13,
            carbs: 30,
            fat: 16,
            fiber: 2
        }
    },
    {
        id: 922,
        name: "دومينوز بيتزا مارغريتا (شريحة)",
        nameEn: "Dominos Margherita (slice)",
        icon: "🍕",
        category: "وجبات سريعة",
        gi: 60,
        ii: 72,
        nutrition: {
            calories: 280,
            protein: 11,
            carbs: 32,
            fat: 12,
            fiber: 2.2
        }
    },
    {
        id: 923,
        name: "صب واي دجاج تيرياكي",
        nameEn: "Subway Chicken Teriyaki",
        icon: "🥪",
        category: "وجبات سريعة",
        gi: 52,
        ii: 60,
        nutrition: {
            calories: 370,
            protein: 26,
            carbs: 57,
            fat: 5,
            fiber: 4
        }
    },
    {
        id: 924,
        name: "صب واي تونة",
        nameEn: "Subway Tuna",
        icon: "🥪",
        category: "وجبات سريعة",
        gi: 50,
        ii: 58,
        nutrition: {
            calories: 480,
            protein: 20,
            carbs: 46,
            fat: 25,
            fiber: 4
        }
    },
    {
        id: 925,
        name: "بوب آيز دجاج مقلي",
        nameEn: "Popeyes Fried Chicken",
        icon: "🍗",
        category: "وجبات سريعة",
        gi: 45,
        ii: 62,
        nutrition: {
            calories: 340,
            protein: 24,
            carbs: 14,
            fat: 22,
            fiber: 1.5
        }
    },
    {
        id: 926,
        name: "تاكو بل كرانشي تاكو",
        nameEn: "Taco Bell Crunchy Taco",
        icon: "🌮",
        category: "وجبات سريعة",
        gi: 48,
        ii: 58,
        nutrition: {
            calories: 170,
            protein: 8,
            carbs: 13,
            fat: 10,
            fiber: 3
        }
    },
    {
        id: 927,
        name: "ويندي'ز دجاج كرسبي",
        nameEn: "Wendy's Crispy Chicken",
        icon: "🍗",
        category: "وجبات سريعة",
        gi: 58,
        ii: 70,
        nutrition: {
            calories: 350,
            protein: 16,
            carbs: 36,
            fat: 17,
            fiber: 2
        }
    },
    {
        id: 928,
        name: "برغر مشروم سويس",
        nameEn: "Mushroom Swiss Burger",
        icon: "🍔",
        category: "وجبات سريعة",
        gi: 62,
        ii: 75,
        nutrition: {
            calories: 620,
            protein: 34,
            carbs: 42,
            fat: 34,
            fiber: 3
        }
    },
    {
        id: 929,
        name: "دبل تشيز برغر",
        nameEn: "Double Cheeseburger",
        icon: "🍔",
        category: "وجبات سريعة",
        gi: 68,
        ii: 82,
        nutrition: {
            calories: 440,
            protein: 25,
            carbs: 34,
            fat: 23,
            fiber: 2
        }
    },
    {
        id: 930,
        name: "بيكون برغر",
        nameEn: "Bacon Burger",
        icon: "🍔",
        category: "وجبات سريعة",
        gi: 65,
        ii: 78,
        nutrition: {
            calories: 595,
            protein: 32,
            carbs: 42,
            fat: 32,
            fiber: 2.5
        }
    },
    {
        id: 931,
        name: "تشيكن رانش ساندويش",
        nameEn: "Chicken Ranch Sandwich",
        icon: "🥪",
        category: "وجبات سريعة",
        gi: 57,
        ii: 68,
        nutrition: {
            calories: 520,
            protein: 28,
            carbs: 44,
            fat: 26,
            fiber: 3
        }
    },
    {
        id: 932,
        name: "كرسبي تشيكن راب",
        nameEn: "Crispy Chicken Wrap",
        icon: "🌯",
        category: "وجبات سريعة",
        gi: 55,
        ii: 65,
        nutrition: {
            calories: 440,
            protein: 22,
            carbs: 40,
            fat: 22,
            fiber: 3.5
        }
    },
    {
        id: 933,
        name: "جريلد تشيكن راب",
        nameEn: "Grilled Chicken Wrap",
        icon: "🌯",
        category: "وجبات سريعة",
        gi: 52,
        ii: 60,
        nutrition: {
            calories: 360,
            protein: 26,
            carbs: 38,
            fat: 12,
            fiber: 4
        }
    },
    {
        id: 934,
        name: "كول سلو",
        nameEn: "Coleslaw",
        icon: "🥗",
        category: "وجبات سريعة",
        gi: 30,
        ii: 35,
        nutrition: {
            calories: 150,
            protein: 1.5,
            carbs: 15,
            fat: 10,
            fiber: 2
        }
    },
    {
        id: 935,
        name: "بطاطس ودجز",
        nameEn: "Potato Wedges",
        icon: "🥔",
        category: "وجبات سريعة",
        gi: 70,
        ii: 82,
        nutrition: {
            calories: 240,
            protein: 3,
            carbs: 34,
            fat: 11,
            fiber: 3.5
        }
    },
    {
        id: 936,
        name: "هاش براون",
        nameEn: "Hash Browns",
        icon: "🥔",
        category: "وجبات سريعة",
        gi: 72,
        ii: 85,
        nutrition: {
            calories: 150,
            protein: 1.5,
            carbs: 15,
            fat: 9,
            fiber: 1.5
        }
    },
    {
        id: 937,
        name: "ماك تشيكن",
        nameEn: "McChicken",
        icon: "🍔",
        category: "وجبات سريعة",
        gi: 58,
        ii: 70,
        nutrition: {
            calories: 400,
            protein: 14,
            carbs: 39,
            fat: 21,
            fiber: 2
        }
    },
    {
        id: 938,
        name: "فيليه أو فيش",
        nameEn: "Filet-O-Fish",
        icon: "🍔",
        category: "وجبات سريعة",
        gi: 55,
        ii: 65,
        nutrition: {
            calories: 380,
            protein: 15,
            carbs: 38,
            fat: 18,
            fiber: 2
        }
    },
    {
        id: 939,
        name: "كوارتر باوندر",
        nameEn: "Quarter Pounder",
        icon: "🍔",
        category: "وجبات سريعة",
        gi: 66,
        ii: 78,
        nutrition: {
            calories: 520,
            protein: 30,
            carbs: 42,
            fat: 26,
            fiber: 3
        }
    },
    {
        id: 940,
        name: "ماك نوجتس (10 قطع)",
        nameEn: "Chicken McNuggets (10pc)",
        icon: "🍗",
        category: "وجبات سريعة",
        gi: 52,
        ii: 68,
        nutrition: {
            calories: 470,
            protein: 24,
            carbs: 30,
            fat: 30,
            fiber: 2
        }
    },
    // منتجات ألبان وأجبان (20 عنصر)
    {
        id: 941,
        name: "جبن موتزاريلا",
        nameEn: "Mozzarella Cheese",
        icon: "🧀",
        category: "ألبان وأجبان",
        gi: 0,
        ii: 45,
        nutrition: {
            calories: 280,
            protein: 28,
            carbs: 2.2,
            fat: 17,
            fiber: 0
        }
    },
    {
        id: 942,
        name: "جبن بارميزان",
        nameEn: "Parmesan Cheese",
        icon: "🧀",
        category: "ألبان وأجبان",
        gi: 0,
        ii: 40,
        nutrition: {
            calories: 431,
            protein: 38,
            carbs: 4.1,
            fat: 29,
            fiber: 0
        }
    },
    {
        id: 943,
        name: "جبن شيدر",
        nameEn: "Cheddar Cheese",
        icon: "🧀",
        category: "ألبان وأجبان",
        gi: 0,
        ii: 42,
        nutrition: {
            calories: 403,
            protein: 25,
            carbs: 1.3,
            fat: 33,
            fiber: 0
        }
    },
    {
        id: 944,
        name: "جبن فيتا",
        nameEn: "Feta Cheese",
        icon: "🧀",
        category: "ألبان وأجبان",
        gi: 0,
        ii: 38,
        nutrition: {
            calories: 264,
            protein: 14,
            carbs: 4.1,
            fat: 21,
            fiber: 0
        }
    },
    {
        id: 945,
        name: "جبن جودا",
        nameEn: "Gouda Cheese",
        icon: "🧀",
        category: "ألبان وأجبان",
        gi: 0,
        ii: 43,
        nutrition: {
            calories: 356,
            protein: 25,
            carbs: 2.2,
            fat: 27,
            fiber: 0
        }
    },
    {
        id: 946,
        name: "جبن حلوم",
        nameEn: "Halloumi Cheese",
        icon: "🧀",
        category: "ألبان وأجبان",
        gi: 0,
        ii: 39,
        nutrition: {
            calories: 316,
            protein: 21,
            carbs: 2.7,
            fat: 25,
            fiber: 0
        }
    },
    {
        id: 947,
        name: "جبن كريمي (Philadelphia)",
        nameEn: "Cream Cheese",
        icon: "🧈",
        category: "ألبان وأجبان",
        gi: 0,
        ii: 35,
        nutrition: {
            calories: 342,
            protein: 6,
            carbs: 4.1,
            fat: 34,
            fiber: 0
        }
    },
    {
        id: 948,
        name: "جبن ريكوتا",
        nameEn: "Ricotta Cheese",
        icon: "🧀",
        category: "ألبان وأجبان",
        gi: 0,
        ii: 30,
        nutrition: {
            calories: 174,
            protein: 11,
            carbs: 3.0,
            fat: 13,
            fiber: 0
        }
    },
    {
        id: 949,
        name: "زبادي يوناني كامل الدسم",
        nameEn: "Full-Fat Greek Yogurt",
        icon: "🥛",
        category: "ألبان وأجبان",
        gi: 11,
        ii: 20,
        nutrition: {
            calories: 97,
            protein: 9,
            carbs: 3.6,
            fat: 5,
            fiber: 0
        }
    },
    {
        id: 950,
        name: "زبادي يوناني قليل الدسم",
        nameEn: "Low-Fat Greek Yogurt",
        icon: "🥛",
        category: "ألبان وأجبان",
        gi: 12,
        ii: 22,
        nutrition: {
            calories: 59,
            protein: 10,
            carbs: 3.6,
            fat: 0.4,
            fiber: 0
        }
    },
    {
        id: 951,
        name: "زبادي بالفواكه",
        nameEn: "Fruit Yogurt",
        icon: "🥛",
        category: "ألبان وأجبان",
        gi: 35,
        ii: 48,
        nutrition: {
            calories: 110,
            protein: 4,
            carbs: 19,
            fat: 2,
            fiber: 0.5
        }
    },
    {
        id: 952,
        name: "لبنة",
        nameEn: "Labneh",
        icon: "🥛",
        category: "ألبان وأجبان",
        gi: 10,
        ii: 18,
        nutrition: {
            calories: 80,
            protein: 5,
            carbs: 3,
            fat: 6,
            fiber: 0
        }
    },
    {
        id: 953,
        name: "قشطة",
        nameEn: "Qishta (Clotted Cream)",
        icon: "🥛",
        category: "ألبان وأجبان",
        gi: 0,
        ii: 25,
        nutrition: {
            calories: 586,
            protein: 1.6,
            carbs: 2.3,
            fat: 64,
            fiber: 0
        }
    },
    {
        id: 954,
        name: "كريمة طازجة",
        nameEn: "Fresh Cream",
        icon: "🥛",
        category: "ألبان وأجبان",
        gi: 0,
        ii: 28,
        nutrition: {
            calories: 345,
            protein: 2.1,
            carbs: 2.8,
            fat: 37,
            fiber: 0
        }
    },
    {
        id: 955,
        name: "حليب كامل الدسم",
        nameEn: "Whole Milk",
        icon: "🥛",
        category: "ألبان وأجبان",
        gi: 32,
        ii: 40,
        nutrition: {
            calories: 61,
            protein: 3.2,
            carbs: 4.8,
            fat: 3.3,
            fiber: 0
        }
    },
    {
        id: 956,
        name: "حليب قليل الدسم",
        nameEn: "Low-Fat Milk",
        icon: "🥛",
        category: "ألبان وأجبان",
        gi: 30,
        ii: 38,
        nutrition: {
            calories: 42,
            protein: 3.4,
            carbs: 5,
            fat: 1,
            fiber: 0
        }
    },
    {
        id: 957,
        name: "حليب خالي الدسم",
        nameEn: "Skim Milk",
        icon: "🥛",
        category: "ألبان وأجبان",
        gi: 32,
        ii: 40,
        nutrition: {
            calories: 34,
            protein: 3.4,
            carbs: 5,
            fat: 0.1,
            fiber: 0
        }
    },
    {
        id: 958,
        name: "حليب لوز",
        nameEn: "Almond Milk",
        icon: "🥛",
        category: "ألبان وأجبان",
        gi: 25,
        ii: 30,
        nutrition: {
            calories: 15,
            protein: 0.6,
            carbs: 1.4,
            fat: 1.1,
            fiber: 0.4
        }
    },
    {
        id: 959,
        name: "حليب صويا",
        nameEn: "Soy Milk",
        icon: "🥛",
        category: "ألبان وأجبان",
        gi: 34,
        ii: 43,
        nutrition: {
            calories: 54,
            protein: 3.3,
            carbs: 6,
            fat: 1.8,
            fiber: 0.6
        }
    },
    {
        id: 960,
        name: "حليب شوفان",
        nameEn: "Oat Milk",
        icon: "🥛",
        category: "ألبان وأجبان",
        gi: 69,
        ii: 65,
        nutrition: {
            calories: 47,
            protein: 1,
            carbs: 7.5,
            fat: 1.5,
            fiber: 0.8
        }
    },
    // صلصات ومقبلات (15 عنصر)
    {
        id: 961,
        name: "كاتشب",
        nameEn: "Ketchup",
        icon: "🍅",
        category: "صلصات",
        gi: 55,
        ii: 60,
        nutrition: {
            calories: 101,
            protein: 1.1,
            carbs: 25,
            fat: 0.1,
            fiber: 0.3
        }
    },
    {
        id: 962,
        name: "مايونيز",
        nameEn: "Mayonnaise",
        icon: "🥫",
        category: "صلصات",
        gi: 0,
        ii: 5,
        nutrition: {
            calories: 680,
            protein: 1,
            carbs: 0.6,
            fat: 75,
            fiber: 0
        }
    },
    {
        id: 963,
        name: "مستردة",
        nameEn: "Mustard",
        icon: "🥫",
        category: "صلصات",
        gi: 5,
        ii: 8,
        nutrition: {
            calories: 66,
            protein: 3.7,
            carbs: 6,
            fat: 3.3,
            fiber: 2.1
        }
    },
    {
        id: 964,
        name: "صلصة باربيكيو",
        nameEn: "BBQ Sauce",
        icon: "🍖",
        category: "صلصات",
        gi: 50,
        ii: 58,
        nutrition: {
            calories: 172,
            protein: 1,
            carbs: 41,
            fat: 0.5,
            fiber: 1.5
        }
    },
    {
        id: 965,
        name: "صلصة صويا",
        nameEn: "Soy Sauce",
        icon: "🥫",
        category: "صلصات",
        gi: 20,
        ii: 25,
        nutrition: {
            calories: 53,
            protein: 5.6,
            carbs: 4.9,
            fat: 0.1,
            fiber: 0.8
        }
    },
    {
        id: 966,
        name: "صلصة تيرياكي",
        nameEn: "Teriyaki Sauce",
        icon: "🥫",
        category: "صلصات",
        gi: 45,
        ii: 52,
        nutrition: {
            calories: 89,
            protein: 2.8,
            carbs: 15,
            fat: 0.4,
            fiber: 0.3
        }
    },
    {
        id: 967,
        name: "سريراتشا (صلصة حارة)",
        nameEn: "Sriracha Hot Sauce",
        icon: "🌶️",
        category: "صلصات",
        gi: 35,
        ii: 40,
        nutrition: {
            calories: 93,
            protein: 2,
            carbs: 19,
            fat: 0.9,
            fiber: 1.5
        }
    },
    {
        id: 968,
        name: "صلصة رانش",
        nameEn: "Ranch Dressing",
        icon: "🥗",
        category: "صلصات",
        gi: 10,
        ii: 15,
        nutrition: {
            calories: 458,
            protein: 1.5,
            carbs: 8,
            fat: 48,
            fiber: 0.5
        }
    },
    {
        id: 969,
        name: "صلصة سيزر",
        nameEn: "Caesar Dressing",
        icon: "🥗",
        category: "صلصات",
        gi: 8,
        ii: 12,
        nutrition: {
            calories: 540,
            protein: 2,
            carbs: 3,
            fat: 58,
            fiber: 0
        }
    },
    {
        id: 970,
        name: "طحينة",
        nameEn: "Tahini",
        icon: "🥫",
        category: "صلصات",
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 595,
            protein: 17,
            carbs: 21,
            fat: 54,
            fiber: 9.3
        }
    },
    {
        id: 971,
        name: "حمص (مقبلات)",
        nameEn: "Hummus",
        icon: "🥫",
        category: "صلصات",
        gi: 6,
        ii: 10,
        nutrition: {
            calories: 166,
            protein: 8,
            carbs: 14,
            fat: 10,
            fiber: 6
        }
    },
    {
        id: 972,
        name: "بابا غنوج",
        nameEn: "Baba Ghanoush",
        icon: "🍆",
        category: "صلصات",
        gi: 10,
        ii: 15,
        nutrition: {
            calories: 102,
            protein: 2.6,
            carbs: 7,
            fat: 8,
            fiber: 3.3
        }
    },
    {
        id: 973,
        name: "متبل",
        nameEn: "Moutabal",
        icon: "🍆",
        category: "صلصات",
        gi: 12,
        ii: 18,
        nutrition: {
            calories: 135,
            protein: 3,
            carbs: 9,
            fat: 11,
            fiber: 4
        }
    },
    {
        id: 974,
        name: "نوتيلا",
        nameEn: "Nutella",
        icon: "🍫",
        category: "صلصات",
        gi: 55,
        ii: 65,
        nutrition: {
            calories: 539,
            protein: 6.3,
            carbs: 57,
            fat: 31,
            fiber: 5.4
        }
    },
    {
        id: 975,
        name: "مربى فراولة",
        nameEn: "Strawberry Jam",
        icon: "🍓",
        category: "صلصات",
        gi: 51,
        ii: 58,
        nutrition: {
            calories: 278,
            protein: 0.4,
            carbs: 69,
            fat: 0.1,
            fiber: 1.1
        }
    },
    // أطعمة صحية ونباتية (25 عنصر)
    {
        id: 976,
        name: "برغر نباتي (Beyond Meat)",
        nameEn: "Plant-Based Burger",
        icon: "🍔",
        category: "أطعمة نباتية",
        gi: 45,
        ii: 50,
        nutrition: {
            calories: 250,
            protein: 20,
            carbs: 15,
            fat: 14,
            fiber: 3
        }
    },
    {
        id: 977,
        name: "توفو",
        nameEn: "Tofu",
        icon: "🧊",
        category: "أطعمة نباتية",
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 76,
            protein: 8,
            carbs: 1.9,
            fat: 4.8,
            fiber: 0.3
        }
    },
    {
        id: 978,
        name: "تمبيه",
        nameEn: "Tempeh",
        icon: "🥜",
        category: "أطعمة نباتية",
        gi: 18,
        ii: 22,
        nutrition: {
            calories: 193,
            protein: 20,
            carbs: 7.6,
            fat: 11,
            fiber: 0
        }
    },
    {
        id: 979,
        name: "سيتان (بروتين القمح)",
        nameEn: "Seitan",
        icon: "🥩",
        category: "أطعمة نباتية",
        gi: 25,
        ii: 30,
        nutrition: {
            calories: 370,
            protein: 75,
            carbs: 14,
            fat: 1.9,
            fiber: 0.6
        }
    },
    {
        id: 980,
        name: "كينوا مطبوخة",
        nameEn: "Cooked Quinoa",
        icon: "🌾",
        category: "أطعمة صحية",
        gi: 53,
        ii: 55,
        nutrition: {
            calories: 120,
            protein: 4.4,
            carbs: 21,
            fat: 1.9,
            fiber: 2.8
        }
    },
    {
        id: 981,
        name: "بذور الشيا",
        nameEn: "Chia Seeds",
        icon: "🌱",
        category: "أطعمة صحية",
        gi: 1,
        ii: 5,
        nutrition: {
            calories: 486,
            protein: 17,
            carbs: 42,
            fat: 31,
            fiber: 34
        }
    },
    {
        id: 982,
        name: "بذور الكتان",
        nameEn: "Flax Seeds",
        icon: "🌱",
        category: "أطعمة صحية",
        gi: 35,
        ii: 38,
        nutrition: {
            calories: 534,
            protein: 18,
            carbs: 29,
            fat: 42,
            fiber: 27
        }
    },
    {
        id: 983,
        name: "بودرة البروتين (واي)",
        nameEn: "Whey Protein Powder",
        icon: "💪",
        category: "أطعمة صحية",
        gi: 15,
        ii: 35,
        nutrition: {
            calories: 412,
            protein: 80,
            carbs: 8,
            fat: 8,
            fiber: 2
        }
    },
    {
        id: 984,
        name: "بروتين بار",
        nameEn: "Protein Bar",
        icon: "🍫",
        category: "أطعمة صحية",
        gi: 35,
        ii: 42,
        nutrition: {
            calories: 200,
            protein: 20,
            carbs: 22,
            fat: 7,
            fiber: 3
        }
    },
    {
        id: 985,
        name: "جرانولا",
        nameEn: "Granola",
        icon: "🥣",
        category: "أطعمة صحية",
        gi: 43,
        ii: 50,
        nutrition: {
            calories: 471,
            protein: 13,
            carbs: 64,
            fat: 20,
            fiber: 11
        }
    },
    {
        id: 986,
        name: "إديمامي (فول صويا مسلوق)",
        nameEn: "Edamame",
        icon: "🫛",
        category: "أطعمة نباتية",
        gi: 18,
        ii: 22,
        nutrition: {
            calories: 121,
            protein: 11,
            carbs: 10,
            fat: 5,
            fiber: 5
        }
    },
    {
        id: 987,
        name: "أفوكادو",
        nameEn: "Avocado",
        icon: "🥑",
        category: "فواكه",
        gi: 15,
        ii: 10,
        nutrition: {
            calories: 160,
            protein: 2,
            carbs: 9,
            fat: 15,
            fiber: 7
        }
    },
    {
        id: 988,
        name: "زبدة الفول السوداني",
        nameEn: "Peanut Butter",
        icon: "🥜",
        category: "أطعمة صحية",
        gi: 14,
        ii: 20,
        nutrition: {
            calories: 588,
            protein: 25,
            carbs: 20,
            fat: 50,
            fiber: 6
        }
    },
    {
        id: 989,
        name: "زبدة اللوز",
        nameEn: "Almond Butter",
        icon: "🌰",
        category: "أطعمة صحية",
        gi: 0,
        ii: 15,
        nutrition: {
            calories: 614,
            protein: 21,
            carbs: 19,
            fat: 56,
            fiber: 10
        }
    },
    {
        id: 990,
        name: "مكسرات مشكلة نيئة",
        nameEn: "Raw Mixed Nuts",
        icon: "🥜",
        category: "أطعمة صحية",
        gi: 15,
        ii: 18,
        nutrition: {
            calories: 607,
            protein: 20,
            carbs: 21,
            fat: 54,
            fiber: 7
        }
    },
    {
        id: 991,
        name: "لوز محمص",
        nameEn: "Roasted Almonds",
        icon: "🌰",
        category: "أطعمة صحية",
        gi: 0,
        ii: 10,
        nutrition: {
            calories: 579,
            protein: 21,
            carbs: 22,
            fat: 50,
            fiber: 12
        }
    },
    {
        id: 992,
        name: "كاجو محمص",
        nameEn: "Roasted Cashews",
        icon: "🥜",
        category: "أطعمة صحية",
        gi: 22,
        ii: 25,
        nutrition: {
            calories: 553,
            protein: 18,
            carbs: 30,
            fat: 44,
            fiber: 3.3
        }
    },
    {
        id: 993,
        name: "بذور اليقطين",
        nameEn: "Pumpkin Seeds",
        icon: "🌱",
        category: "أطعمة صحية",
        gi: 25,
        ii: 28,
        nutrition: {
            calories: 559,
            protein: 30,
            carbs: 14,
            fat: 49,
            fiber: 6
        }
    },
    {
        id: 994,
        name: "بذور دوار الشمس",
        nameEn: "Sunflower Seeds",
        icon: "🌻",
        category: "أطعمة صحية",
        gi: 20,
        ii: 22,
        nutrition: {
            calories: 584,
            protein: 21,
            carbs: 20,
            fat: 51,
            fiber: 9
        }
    },
    {
        id: 995,
        name: "خبز خالي من الجلوتين",
        nameEn: "Gluten-Free Bread",
        icon: "🍞",
        category: "أطعمة صحية",
        gi: 70,
        ii: 78,
        nutrition: {
            calories: 258,
            protein: 4,
            carbs: 50,
            fat: 4,
            fiber: 4
        }
    },
    {
        id: 996,
        name: "باستا خالية من الجلوتين",
        nameEn: "Gluten-Free Pasta",
        icon: "🍝",
        category: "أطعمة صحية",
        gi: 54,
        ii: 58,
        nutrition: {
            calories: 348,
            protein: 7,
            carbs: 76,
            fat: 2,
            fiber: 3.5
        }
    },
    {
        id: 997,
        name: "حليب جوز الهند",
        nameEn: "Coconut Milk",
        icon: "🥥",
        category: "ألبان وأجبان",
        gi: 40,
        ii: 45,
        nutrition: {
            calories: 230,
            protein: 2.3,
            carbs: 6,
            fat: 24,
            fiber: 2.2
        }
    },
    {
        id: 998,
        name: "طحين اللوز",
        nameEn: "Almond Flour",
        icon: "🌰",
        category: "أطعمة صحية",
        gi: 0,
        ii: 10,
        nutrition: {
            calories: 571,
            protein: 21,
            carbs: 21,
            fat: 50,
            fiber: 11
        }
    },
    {
        id: 999,
        name: "طحين جوز الهند",
        nameEn: "Coconut Flour",
        icon: "🥥",
        category: "أطعمة صحية",
        gi: 45,
        ii: 48,
        nutrition: {
            calories: 400,
            protein: 20,
            carbs: 60,
            fat: 13,
            fiber: 40
        }
    },
    {
        id: 1000,
        name: "شاي أخضر ماتشا",
        nameEn: "Matcha Green Tea",
        icon: "🍵",
        category: "مشروبات",
        gi: 0,
        ii: 5,
        nutrition: {
            calories: 3,
            protein: 0.3,
            carbs: 0.4,
            fat: 0,
            fiber: 0.4
        }
    },
    {
        id: 1001,
        name: "معكرونة بالبشاميل",
        nameEn: "Pasta Bechamel",
        icon: "🍝",
        category: "أطعمة عربية",
        gi: 68,
        ii: 72,
        nutrition: {
            calories: 320,
            protein: 12,
            carbs: 38,
            fat: 14,
            fiber: 2.5
        }
    },
    {
        id: 1002,
        name: "أرز بالحليب",
        nameEn: "Rice Pudding",
        icon: "🍚",
        category: "حلويات عربية",
        gi: 70,
        ii: 68,
        nutrition: {
            calories: 180,
            protein: 4.5,
            carbs: 32,
            fat: 3.8,
            fiber: 0.5
        }
    },
    {
        id: 1003,
        name: "كبدة إسكندراني",
        nameEn: "Alexandrian Liver",
        icon: "🥩",
        category: "أطعمة عربية",
        gi: 0,
        ii: 68,
        nutrition: {
            calories: 195,
            protein: 22,
            carbs: 2.5,
            fat: 11,
            fiber: 0.5
        }
    },
    {
        id: 1004,
        name: "كفتة داوود باشا",
        nameEn: "Dawood Basha Kofta",
        icon: "🧆",
        category: "أطعمة عربية",
        gi: 42,
        ii: 65,
        nutrition: {
            calories: 285,
            protein: 18,
            carbs: 15,
            fat: 18,
            fiber: 3
        }
    },
    {
        id: 1005,
        name: "شوربة العدس التركية",
        nameEn: "Turkish Lentil Soup",
        icon: "🍲",
        category: "شوربات",
        gi: 38,
        ii: 45,
        nutrition: {
            calories: 145,
            protein: 8,
            carbs: 22,
            fat: 3.5,
            fiber: 5.5
        }
    },
    {
        id: 1006,
        name: "كبة نية (نيئة)",
        nameEn: "Raw Kibbeh",
        icon: "🥩",
        category: "أطعمة عربية",
        gi: 52,
        ii: 58,
        nutrition: {
            calories: 215,
            protein: 16,
            carbs: 18,
            fat: 9,
            fiber: 3.5
        }
    },
    {
        id: 1007,
        name: "فتة المكدوس",
        nameEn: "Makdous Fatteh",
        icon: "🍆",
        category: "أطعمة عربية",
        gi: 55,
        ii: 62,
        nutrition: {
            calories: 298,
            protein: 10,
            carbs: 28,
            fat: 17,
            fiber: 5
        }
    },
    {
        id: 1008,
        name: "مجدرة",
        nameEn: "Mujadara",
        icon: "🍚",
        category: "أطعمة عربية",
        gi: 48,
        ii: 52,
        nutrition: {
            calories: 245,
            protein: 11,
            carbs: 38,
            fat: 6,
            fiber: 8
        }
    },
    {
        id: 1009,
        name: "ملوخية بالأرانب",
        nameEn: "Molokhia with Rabbit",
        icon: "🥬",
        category: "أطعمة عربية",
        gi: 15,
        ii: 48,
        nutrition: {
            calories: 195,
            protein: 22,
            carbs: 8,
            fat: 9,
            fiber: 4
        }
    },
    {
        id: 1010,
        name: "صيادية السمك",
        nameEn: "Fish Sayadieh",
        icon: "🐟",
        category: "أطعمة عربية",
        gi: 58,
        ii: 62,
        nutrition: {
            calories: 315,
            protein: 24,
            carbs: 35,
            fat: 9,
            fiber: 2.5
        }
    },
    {
        id: 1011,
        name: "مسقعة",
        nameEn: "Moussaka",
        icon: "🍆",
        category: "أطعمة عربية",
        gi: 52,
        ii: 58,
        nutrition: {
            calories: 235,
            protein: 9,
            carbs: 18,
            fat: 15,
            fiber: 5.5
        }
    },
    {
        id: 1012,
        name: "بامية باللحم",
        nameEn: "Okra with Meat",
        icon: "🌱",
        category: "أطعمة عربية",
        gi: 25,
        ii: 55,
        nutrition: {
            calories: 198,
            protein: 14,
            carbs: 12,
            fat: 11,
            fiber: 5
        }
    },
    {
        id: 1013,
        name: "فاصوليا بيضاء بالصلصة",
        nameEn: "White Beans in Sauce",
        icon: "🫘",
        category: "أطعمة عربية",
        gi: 38,
        ii: 48,
        nutrition: {
            calories: 185,
            protein: 10,
            carbs: 28,
            fat: 4,
            fiber: 9
        }
    },
    {
        id: 1014,
        name: "شكشوكة",
        nameEn: "Shakshuka",
        icon: "🍳",
        category: "أطعمة عربية",
        gi: 32,
        ii: 52,
        nutrition: {
            calories: 195,
            protein: 11,
            carbs: 10,
            fat: 13,
            fiber: 3
        }
    },
    {
        id: 1015,
        name: "عكاوي مشوي",
        nameEn: "Grilled Akawi Cheese",
        icon: "🧀",
        category: "أجبان",
        gi: 0,
        ii: 55,
        nutrition: {
            calories: 285,
            protein: 18,
            carbs: 2,
            fat: 23,
            fiber: 0
        }
    },
    {
        id: 1016,
        name: "مناقيش جبنة",
        nameEn: "Cheese Manakish",
        icon: "🫓",
        category: "مخبوزات",
        gi: 65,
        ii: 68,
        nutrition: {
            calories: 295,
            protein: 12,
            carbs: 35,
            fat: 12,
            fiber: 2
        }
    },
    {
        id: 1017,
        name: "لبنة بالنعناع",
        nameEn: "Labneh with Mint",
        icon: "🥛",
        category: "ألبان",
        gi: 15,
        ii: 42,
        nutrition: {
            calories: 118,
            protein: 7,
            carbs: 5,
            fat: 8,
            fiber: 0.5
        }
    },
    {
        id: 1018,
        name: "بيض بالقاورما",
        nameEn: "Eggs with Qawarma",
        icon: "🍳",
        category: "أطعمة عربية",
        gi: 0,
        ii: 55,
        nutrition: {
            calories: 315,
            protein: 16,
            carbs: 1,
            fat: 28,
            fiber: 0
        }
    },
    {
        id: 1019,
        name: "كبة مقلية",
        nameEn: "Fried Kibbeh",
        icon: "🧆",
        category: "أطعمة عربية",
        gi: 58,
        ii: 65,
        nutrition: {
            calories: 285,
            protein: 14,
            carbs: 22,
            fat: 16,
            fiber: 3
        }
    },
    {
        id: 1020,
        name: "فتة حمص",
        nameEn: "Hummus Fatteh",
        icon: "🍲",
        category: "أطعمة عربية",
        gi: 48,
        ii: 55,
        nutrition: {
            calories: 265,
            protein: 12,
            carbs: 32,
            fat: 10,
            fiber: 7
        }
    },
    {
        id: 1021,
        name: "ورق العنب بالزيت",
        nameEn: "Vegetarian Stuffed Grape Leaves",
        icon: "🍃",
        category: "أطعمة عربية",
        gi: 42,
        ii: 48,
        nutrition: {
            calories: 165,
            protein: 3,
            carbs: 22,
            fat: 7,
            fiber: 4
        }
    },
    {
        id: 1022,
        name: "كنافة نابلسية",
        nameEn: "Nabulsi Kunafa",
        icon: "🥧",
        category: "حلويات عربية",
        gi: 72,
        ii: 75,
        nutrition: {
            calories: 385,
            protein: 8,
            carbs: 48,
            fat: 18,
            fiber: 1.5
        }
    },
    {
        id: 1023,
        name: "قطايف محشية",
        nameEn: "Stuffed Qatayef",
        icon: "🥮",
        category: "حلويات عربية",
        gi: 68,
        ii: 72,
        nutrition: {
            calories: 295,
            protein: 6,
            carbs: 42,
            fat: 12,
            fiber: 2
        }
    },
    {
        id: 1024,
        name: "حلاوة طحينية",
        nameEn: "Halva",
        icon: "🍯",
        category: "حلويات عربية",
        gi: 55,
        ii: 58,
        nutrition: {
            calories: 420,
            protein: 12,
            carbs: 52,
            fat: 20,
            fiber: 5
        }
    },
    {
        id: 1025,
        name: "معمول بالتمر",
        nameEn: "Date Ma'amoul",
        icon: "🥮",
        category: "حلويات عربية",
        gi: 62,
        ii: 65,
        nutrition: {
            calories: 325,
            protein: 4.5,
            carbs: 48,
            fat: 13,
            fiber: 4
        }
    },
    {
        id: 1026,
        name: "زلابية",
        nameEn: "Zalabia",
        icon: "🍩",
        category: "حلويات عربية",
        gi: 75,
        ii: 78,
        nutrition: {
            calories: 395,
            protein: 5,
            carbs: 55,
            fat: 17,
            fiber: 1.5
        }
    },
    {
        id: 1027,
        name: "بسبوسة",
        nameEn: "Basbousa",
        icon: "🍰",
        category: "حلويات عربية",
        gi: 70,
        ii: 72,
        nutrition: {
            calories: 365,
            protein: 6,
            carbs: 52,
            fat: 15,
            fiber: 2.5
        }
    },
    {
        id: 1028,
        name: "غريبة",
        nameEn: "Ghorayeba",
        icon: "🍪",
        category: "حلويات عربية",
        gi: 58,
        ii: 62,
        nutrition: {
            calories: 385,
            protein: 4,
            carbs: 42,
            fat: 22,
            fiber: 1
        }
    },
    {
        id: 1029,
        name: "مهلبية",
        nameEn: "Muhallabia",
        icon: "🍮",
        category: "حلويات عربية",
        gi: 65,
        ii: 68,
        nutrition: {
            calories: 165,
            protein: 4,
            carbs: 28,
            fat: 4,
            fiber: 0.5
        }
    },
    {
        id: 1030,
        name: "حلى الجلي",
        nameEn: "Jelly Dessert",
        icon: "🍮",
        category: "حلويات",
        gi: 55,
        ii: 58,
        nutrition: {
            calories: 125,
            protein: 2,
            carbs: 28,
            fat: 1,
            fiber: 0
        }
    },
    {
        id: 1031,
        name: "فطيرة بالسبانخ",
        nameEn: "Spinach Pie",
        icon: "🥟",
        category: "مخبوزات",
        gi: 52,
        ii: 58,
        nutrition: {
            calories: 245,
            protein: 8,
            carbs: 32,
            fat: 10,
            fiber: 4
        }
    },
    {
        id: 1032,
        name: "سمبوسك باللحم",
        nameEn: "Meat Samosa",
        icon: "🥟",
        category: "مخبوزات",
        gi: 58,
        ii: 65,
        nutrition: {
            calories: 295,
            protein: 12,
            carbs: 28,
            fat: 15,
            fiber: 2
        }
    },
    {
        id: 1033,
        name: "فتة باذنجان",
        nameEn: "Eggplant Fatteh",
        icon: "🍆",
        category: "أطعمة عربية",
        gi: 48,
        ii: 55,
        nutrition: {
            calories: 285,
            protein: 9,
            carbs: 30,
            fat: 15,
            fiber: 6
        }
    },
    {
        id: 1034,
        name: "مقلوبة بالدجاج",
        nameEn: "Chicken Maqluba",
        icon: "🍚",
        category: "أطعمة عربية",
        gi: 62,
        ii: 68,
        nutrition: {
            calories: 345,
            protein: 22,
            carbs: 38,
            fat: 12,
            fiber: 3.5
        }
    },
    {
        id: 1035,
        name: "منسف بلحم الغنم",
        nameEn: "Mansaf with Lamb",
        icon: "🍚",
        category: "أطعمة عربية",
        gi: 58,
        ii: 65,
        nutrition: {
            calories: 425,
            protein: 28,
            carbs: 42,
            fat: 18,
            fiber: 2.5
        }
    },
    {
        id: 1036,
        name: "مفركة البطاطا",
        nameEn: "Mfaraket Batata",
        icon: "🥔",
        category: "أطعمة عربية",
        gi: 55,
        ii: 60,
        nutrition: {
            calories: 225,
            protein: 7,
            carbs: 28,
        fat: 10,
            fiber: 4
        }
    },
    {
        id: 1037,
        name: "لحم بعجين",
        nameEn: "Lahmacun",
        icon: "🫓",
        category: "مخبوزات",
        gi: 62,
        ii: 68,
        nutrition: {
            calories: 285,
            protein: 14,
            carbs: 32,
            fat: 11,
            fiber: 2.5
        }
    },
    {
        id: 1038,
        name: "عجة بالخضار",
        nameEn: "Vegetable Omelette",
        icon: "🍳",
        category: "أطعمة عربية",
        gi: 25,
        ii: 48,
        nutrition: {
            calories: 185,
            protein: 12,
            carbs: 8,
            fat: 12,
            fiber: 2.5
        }
    },
    {
        id: 1039,
        name: "حمص بالطحينة",
        nameEn: "Hummus with Tahini",
        icon: "🫘",
        category: "مقبلات",
        gi: 28,
        ii: 38,
        nutrition: {
            calories: 165,
            protein: 7,
            carbs: 14,
            fat: 10,
            fiber: 6
        }
    },
    {
        id: 1040,
        name: "متبل باذنجان",
        nameEn: "Baba Ganoush",
        icon: "🍆",
        category: "مقبلات",
        gi: 18,
        ii: 28,
        nutrition: {
            calories: 125,
            protein: 3,
            carbs: 9,
            fat: 9,
            fiber: 4.5
        }
    },
    {
        id: 1041,
        name: "محمرة",
        nameEn: "Muhammara",
        icon: "🌶️",
        category: "مقبلات",
        gi: 35,
        ii: 42,
        nutrition: {
            calories: 185,
            protein: 4,
            carbs: 15,
            fat: 13,
            fiber: 3.5
        }
    },
    {
        id: 1042,
        name: "شاورما دجاج",
        nameEn: "Chicken Shawarma",
        icon: "🌯",
        category: "ساندويشات",
        gi: 52,
        ii: 62,
        nutrition: {
            calories: 325,
            protein: 24,
            carbs: 32,
            fat: 12,
            fiber: 3
        }
    },
    {
        id: 1043,
        name: "شاورما لحم",
        nameEn: "Beef Shawarma",
        icon: "🌯",
        category: "ساندويشات",
        gi: 52,
        ii: 65,
        nutrition: {
            calories: 355,
            protein: 26,
            carbs: 32,
            fat: 15,
            fiber: 3
        }
    },
    {
        id: 1044,
        name: "فلافل",
        nameEn: "Falafel",
        icon: "🧆",
        category: "أطعمة عربية",
        gi: 42,
        ii: 48,
        nutrition: {
            calories: 185,
            protein: 8,
            carbs: 18,
            fat: 10,
            fiber: 5
        }
    },
    {
        id: 1045,
        name: "طرشي مشكل",
        nameEn: "Mixed Pickles",
        icon: "🥒",
        category: "مخللات",
        gi: 15,
        ii: 20,
        nutrition: {
            calories: 25,
            protein: 0.8,
            carbs: 5,
            fat: 0.2,
            fiber: 1.5
        }
    },
    {
        id: 1046,
        name: "زيتون أخضر محشي",
        nameEn: "Stuffed Green Olives",
        icon: "🫒",
        category: "مقبلات",
        gi: 15,
        ii: 22,
        nutrition: {
            calories: 145,
            protein: 1.2,
            carbs: 3.8,
            fat: 15,
            fiber: 3
        }
    },
    {
        id: 1047,
        name: "شوربة فريكة",
        nameEn: "Freekeh Soup",
        icon: "🍲",
        category: "شوربات",
        gi: 42,
        ii: 48,
        nutrition: {
            calories: 165,
            protein: 9,
            carbs: 24,
            fat: 4,
            fiber: 6
        }
    },
    {
        id: 1048,
        name: "رز بالشعيرية",
        nameEn: "Rice with Vermicelli",
        icon: "🍚",
        category: "أطعمة عربية",
        gi: 65,
        ii: 68,
        nutrition: {
            calories: 195,
            protein: 4.5,
            carbs: 38,
            fat: 3,
            fiber: 1.5
        }
    },
    {
        id: 1049,
        name: "يخنة بامية",
        nameEn: "Okra Stew",
        icon: "🍲",
        category: "أطعمة عربية",
        gi: 28,
        ii: 45,
        nutrition: {
            calories: 125,
            protein: 6,
            carbs: 15,
            fat: 5,
            fiber: 5
        }
    },
    {
        id: 1050,
        name: "كوسا محشي",
        nameEn: "Stuffed Zucchini",
        icon: "🥒",
        category: "أطعمة عربية",
        gi: 42,
        ii: 52,
        nutrition: {
            calories: 165,
            protein: 9,
            carbs: 18,
            fat: 7,
            fiber: 3.5
        }
    },
    {
        id: 1051,
        name: "قرنبيط مقلي",
        nameEn: "Fried Cauliflower",
        icon: "🥦",
        category: "أطعمة عربية",
        gi: 35,
        ii: 42,
        nutrition: {
            calories: 195,
            protein: 4,
            carbs: 12,
            fat: 15,
            fiber: 3.5
        }
    }
];

/**
 * دالة للحصول على مستوى المؤشر (منخفض، متوسط، مرتفع)
 */
function getIndexLevel(value) {
    if (value <= 55) return 'low';
    if (value <= 69) return 'medium';
    return 'high';
}

/**
 * دالة للحصول على نص المستوى بالعربية أو الإنجليزية
 */
function getIndexLevelText(value, lang = 'ar') {
    if (lang === 'en') {
        if (value <= 55) return 'Low';
        if (value <= 69) return 'Medium';
        return 'High';
    } else {
        if (value <= 55) return 'منخفض';
        if (value <= 69) return 'متوسط';
        return 'مرتفع';
    }
}

/**
 * دالة لتصفية الأطعمة حسب البحث
 */
function filterFoodsBySearch(searchTerm) {
    if (!searchTerm || searchTerm.trim() === '') {
        return foodsDatabase;
    }
    
    const term = searchTerm.toLowerCase().trim();
    return foodsDatabase.filter(food => 
        food.name.toLowerCase().includes(term) ||
        food.nameEn.toLowerCase().includes(term) ||
        food.category.toLowerCase().includes(term)
    );
}

/**
 * دالة لتصفية الأطعمة حسب الفئة
 */
function filterFoodsByCategory(category) {
    if (!category || category === 'all') {
        return foodsDatabase;
    }
    return foodsDatabase.filter(food => food.category === category);
}

/**
 * دالة للحصول على الفئات المتاحة
 */
function getCategories() {
    const categories = [...new Set(foodsDatabase.map(food => food.category))];
    return categories;
}