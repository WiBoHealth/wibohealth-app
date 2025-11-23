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
        id: 113,
        name: 'كشري مصري',
        nameEn: 'Egyptian Koshari',
        icon: '🍝',
        category: 'أطعمة عربية',
        gi: 52,
        ii: 58,
        nutrition: {
            calories: 267,
            protein: 11,
            carbs: 48,
            fat: 4.2,
            fiber: 8.5
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
 * دالة للحصول على نص المستوى بالعربية
 */
function getIndexLevelText(value) {
    if (value <= 55) return 'منخفض';
    if (value <= 69) return 'متوسط';
    return 'مرتفع';
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