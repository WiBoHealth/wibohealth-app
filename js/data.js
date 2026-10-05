/**
 * WiBo Health - Master Food Database (Tri-Lingual: AR / EN / NL)
 * قاعدة بيانات الأطعمة الموحدة والخالية من التكرار
 * تم التدقيق اللغوي السريري وإضافة اللغة الهولندية بالكامل
 */

const foodsDatabase = [
    // === الحبوب والنشويات (Granen & Zetmeel) ===
    { id: 1, name: 'أرز أبيض مطبوخ', nameEn: 'White Rice', nameNl: 'Witte rijst (gekookt)', icon: '🍚', category: 'حبوب', categoryNl: 'Granen', gi: 73, ii: 79, nutrition: { calories: 130, protein: 2.7, carbs: 28, fat: 0.3, fiber: 0.4 } },
    { id: 2, name: 'أرز بني مطبوخ', nameEn: 'Brown Rice', nameNl: 'Zilvervliesrijst (gekookt)', icon: '🍚', category: 'حبوب', categoryNl: 'Granen', gi: 50, ii: 62, nutrition: { calories: 111, protein: 2.6, carbs: 23, fat: 0.9, fiber: 1.8 } },
    { id: 3, name: 'خبز أبيض', nameEn: 'White Bread', nameNl: 'Witbrood', icon: '🍞', category: 'حبوب', categoryNl: 'Granen', gi: 75, ii: 100, nutrition: { calories: 265, protein: 9, carbs: 49, fat: 3.2, fiber: 2.7 } },
    { id: 4, name: 'خبز قمح كامل (أسمر)', nameEn: 'Whole Wheat Bread', nameNl: 'Volkorenbrood', icon: '🍞', category: 'حبوب', categoryNl: 'Granen', gi: 53, ii: 56, nutrition: { calories: 247, protein: 13, carbs: 41, fat: 3.4, fiber: 7 } },
    { id: 5, name: 'معكرونة بيضاء', nameEn: 'White Pasta', nameNl: 'Witte pasta', icon: '🍝', category: 'حبوب', categoryNl: 'Granen', gi: 58, ii: 46, nutrition: { calories: 131, protein: 5, carbs: 25, fat: 1.1, fiber: 1.8 } },
    { id: 6, name: 'معكرونة القمح الكامل', nameEn: 'Whole Wheat Pasta', nameNl: 'Volkoren pasta', icon: '🍝', category: 'حبوب', categoryNl: 'Granen', gi: 42, ii: 40, nutrition: { calories: 124, protein: 5.3, carbs: 26, fat: 0.5, fiber: 3.9 } },
    { id: 7, name: 'شوفان', nameEn: 'Oatmeal', nameNl: 'Havermout', icon: '🥣', category: 'حبوب', categoryNl: 'Granen', gi: 55, ii: 40, nutrition: { calories: 68, protein: 2.4, carbs: 12, fat: 1.4, fiber: 1.7 } },
    { id: 8, name: 'كينوا مطبوخة', nameEn: 'Quinoa', nameNl: 'Gekookte quinoa', icon: '🌾', category: 'حبوب', categoryNl: 'Granen', gi: 53, ii: 48, nutrition: { calories: 120, protein: 4.4, carbs: 21, fat: 1.9, fiber: 2.8 } },
    { id: 9, name: 'برغل مطبوخ', nameEn: 'Bulgur', nameNl: 'Gekookte bulgur', icon: '🌾', category: 'حبوب', categoryNl: 'Granen', gi: 48, ii: 46, nutrition: { calories: 83, protein: 3.1, carbs: 19, fat: 0.2, fiber: 4.5 } },
    { id: 10, name: 'كسكسي مطبوخ', nameEn: 'Couscous', nameNl: 'Gekookte couscous', icon: '🌾', category: 'حبوب', categoryNl: 'Granen', gi: 65, ii: 58, nutrition: { calories: 112, protein: 3.8, carbs: 23, fat: 0.2, fiber: 1.4 } },
    { id: 11, name: 'ذرة مسلوقة', nameEn: 'Boiled Corn', nameNl: 'Gekookte maïs', icon: '🌽', category: 'حبوب', categoryNl: 'Granen', gi: 52, ii: 54, nutrition: { calories: 86, protein: 3.3, carbs: 19, fat: 1.4, fiber: 2.4 } },
    { id: 12, name: 'خبز الشعير', nameEn: 'Barley Bread', nameNl: 'Gerstebrood', icon: '🍞', category: 'حبوب', categoryNl: 'Granen', gi: 34, ii: 40, nutrition: { calories: 240, protein: 8.5, carbs: 47, fat: 1.5, fiber: 9.2 } },
    { id: 13, name: 'خبز الشوفان', nameEn: 'Oat Bread', nameNl: 'Haverbrood', icon: '🍞', category: 'حبوب', categoryNl: 'Granen', gi: 47, ii: 44, nutrition: { calories: 255, protein: 10, carbs: 43, fat: 4.2, fiber: 5.8 } },
    { id: 14, name: 'أرز بسمتي مطبوخ', nameEn: 'Basmati Rice', nameNl: 'Basmatirijst', icon: '🍚', category: 'حبوب', categoryNl: 'Granen', gi: 58, ii: 65, nutrition: { calories: 121, protein: 3, carbs: 25, fat: 0.4, fiber: 0.6 } },
    { id: 15, name: 'فريكة خضراء', nameEn: 'Freekeh', nameNl: 'Freekeh', icon: '🌾', category: 'حبوب', categoryNl: 'Granen', gi: 43, ii: 40, nutrition: { calories: 130, protein: 5, carbs: 26, fat: 0.8, fiber: 8 } },
    { id: 16, name: 'دخن مسلوق', nameEn: 'Millet', nameNl: 'Gierst', icon: '🌾', category: 'حبوب', categoryNl: 'Granen', gi: 71, ii: 60, nutrition: { calories: 119, protein: 3.5, carbs: 23.7, fat: 1, fiber: 1.3 } },
    { id: 17, name: 'نخالة الشوفان', nameEn: 'Oat Bran', nameNl: 'Haverzemelen', icon: '🌾', category: 'حبوب', categoryNl: 'Granen', gi: 55, ii: 60, nutrition: { calories: 246, protein: 17.3, carbs: 66.2, fat: 7, fiber: 15.4 } },

    // === البقوليات (Peulvruchten) ===
    { id: 18, name: 'عدس بني/أخضر مطبوخ', nameEn: 'Lentils', nameNl: 'Gekookte linzen', icon: '🫘', category: 'بقوليات', categoryNl: 'Peulvruchten', gi: 32, ii: 58, nutrition: { calories: 116, protein: 9, carbs: 20, fat: 0.4, fiber: 7.9 } },
    { id: 19, name: 'حمص مسلوق', nameEn: 'Chickpeas', nameNl: 'Gekookte kikkererwten', icon: '🫘', category: 'بقوليات', categoryNl: 'Peulvruchten', gi: 28, ii: 42, nutrition: { calories: 164, protein: 8.9, carbs: 27, fat: 2.6, fiber: 7.6 } },
    { id: 20, name: 'فول عريض مطبوخ', nameEn: 'Fava Beans', nameNl: 'Tuinbonen', icon: '🫘', category: 'بقوليات', categoryNl: 'Peulvruchten', gi: 40, ii: 84, nutrition: { calories: 110, protein: 7.6, carbs: 19, fat: 0.4, fiber: 5.4 } },
    { id: 21, name: 'فاصوليا بيضاء مطبوخة', nameEn: 'White Beans', nameNl: 'Witte bonen', icon: '🫘', category: 'بقوليات', categoryNl: 'Peulvruchten', gi: 38, ii: 40, nutrition: { calories: 139, protein: 9.7, carbs: 25, fat: 0.5, fiber: 6.4 } },
    { id: 22, name: 'فاصوليا حمراء مطبوخة', nameEn: 'Red Kidney Beans', nameNl: 'Rode kidneybonen', icon: '🫘', category: 'بقوليات', categoryNl: 'Peulvruchten', gi: 24, ii: 39, nutrition: { calories: 127, protein: 8.7, carbs: 23, fat: 0.5, fiber: 7.4 } },
    { id: 23, name: 'لوبيا ذات العين السوداء', nameEn: 'Black-eyed Peas', nameNl: 'Zwarte-ogenbonen', icon: '🫘', category: 'بقوليات', categoryNl: 'Peulvruchten', gi: 33, ii: 40, nutrition: { calories: 116, protein: 8, carbs: 21, fat: 0.5, fiber: 6 } },
    { id: 24, name: 'فول الصويا المسلوق (إداماميه)', nameEn: 'Edamame', nameNl: 'Edamame boontjes', icon: '🫛', category: 'بقوليات', categoryNl: 'Peulvruchten', gi: 15, ii: 22, nutrition: { calories: 121, protein: 11, carbs: 10, fat: 5, fiber: 5 } },
    { id: 25, name: 'ترمس حلو مسلوق', nameEn: 'Lupini Beans', nameNl: 'Lupinebonen', icon: '🫘', category: 'بقوليات', categoryNl: 'Peulvruchten', gi: 15, ii: 20, nutrition: { calories: 119, protein: 16.4, carbs: 9.9, fat: 2.9, fiber: 4.8 } },

    // === الخضروات (Groenten - معدلة لشامي: بطاطا، بندورة، كوسا) ===
    { id: 26, name: 'بطاطا مسلوقة', nameEn: 'Boiled Potato', nameNl: 'Gekookte aardappel', icon: '🥔', category: 'خضروات', categoryNl: 'Groenten', gi: 78, ii: 121, nutrition: { calories: 87, protein: 2, carbs: 20, fat: 0.1, fiber: 1.8 } },
    { id: 27, name: 'بطاطا حلوة مشوية', nameEn: 'Sweet Potato', nameNl: 'Zoete aardappel', icon: '🍠', category: 'خضروات', categoryNl: 'Groenten', gi: 63, ii: 94, nutrition: { calories: 90, protein: 2, carbs: 21, fat: 0.2, fiber: 3.3 } },
    { id: 28, name: 'بطاطا مقلية (فرايز)', nameEn: 'French Fries', nameNl: 'Frietjes', icon: '🍟', category: 'خضروات', categoryNl: 'Groenten', gi: 75, ii: 89, nutrition: { calories: 312, protein: 3.4, carbs: 41, fat: 15, fiber: 3.8 } },
    { id: 29, name: 'بطاطا مهروسة (بيوريه)', nameEn: 'Mashed Potato', nameNl: 'Aardappelpuree', icon: '🥔', category: 'خضروات', categoryNl: 'Groenten', gi: 85, ii: 121, nutrition: { calories: 113, protein: 2.1, carbs: 17, fat: 4.2, fiber: 1.5 } },
    { id: 30, name: 'بندورة طازجة', nameEn: 'Tomato', nameNl: 'Verse tomaat', icon: '🍅', category: 'خضروات', categoryNl: 'Groenten', gi: 15, ii: 38, nutrition: { calories: 18, protein: 0.9, carbs: 4, fat: 0.2, fiber: 1.2 } },
    { id: 31, name: 'خيار طازج', nameEn: 'Cucumber', nameNl: 'Komkommer', icon: '🥒', category: 'خضروات', categoryNl: 'Groenten', gi: 15, ii: 15, nutrition: { calories: 15, protein: 0.7, carbs: 3.6, fat: 0.1, fiber: 0.5 } },
    { id: 32, name: 'كوسا طازجة', nameEn: 'Zucchini', nameNl: 'Courgette', icon: '🥒', category: 'خضروات', categoryNl: 'Groenten', gi: 15, ii: 8, nutrition: { calories: 17, protein: 1.2, carbs: 3.1, fat: 0.3, fiber: 1 } },
    { id: 33, name: 'باذنجان مشوي', nameEn: 'Grilled Eggplant', nameNl: 'Gegrilde aubergine', icon: '🍆', category: 'خضروات', categoryNl: 'Groenten', gi: 15, ii: 11, nutrition: { calories: 35, protein: 0.8, carbs: 8.6, fat: 0.2, fiber: 2.5 } },
    { id: 34, name: 'جزر طازج', nameEn: 'Carrot', nameNl: 'Wortel', icon: '🥕', category: 'خضروات', categoryNl: 'Groenten', gi: 39, ii: 51, nutrition: { calories: 41, protein: 0.9, carbs: 10, fat: 0.2, fiber: 2.8 } },
    { id: 35, name: 'بروكلي مطبوخ على البخار', nameEn: 'Broccoli', nameNl: 'Gestoomde broccoli', icon: '🥦', category: 'خضروات', categoryNl: 'Groenten', gi: 10, ii: 10, nutrition: { calories: 34, protein: 2.8, carbs: 7, fat: 0.4, fiber: 2.6 } },
    { id: 36, name: 'قرنبيط (زهوة)', nameEn: 'Cauliflower', nameNl: 'Bloemkool', icon: '🥦', category: 'خضروات', categoryNl: 'Groenten', gi: 10, ii: 10, nutrition: { calories: 25, protein: 1.9, carbs: 5, fat: 0.3, fiber: 2 } },
    { id: 37, name: 'سبانخ طازجة', nameEn: 'Spinach', nameNl: 'Verse spinazie', icon: '🥬', category: 'خضروات', categoryNl: 'Groenten', gi: 15, ii: 15, nutrition: { calories: 23, protein: 2.9, carbs: 3.6, fat: 0.4, fiber: 2.2 } },
    { id: 38, name: 'ملوخية ورق خضراء', nameEn: 'Molokhia', nameNl: 'Jutemelk (Molokhia)', icon: '🥬', category: 'خضروات', categoryNl: 'Groenten', gi: 15, ii: 15, nutrition: { calories: 37, protein: 4.5, carbs: 6.9, fat: 0.2, fiber: 2 } },
    { id: 39, name: 'بامية خضراء', nameEn: 'Okra', nameNl: 'Okra', icon: '🫛', category: 'خضروات', categoryNl: 'Groenten', gi: 20, ii: 24, nutrition: { calories: 33, protein: 1.9, carbs: 7.5, fat: 0.2, fiber: 3.2 } },
    { id: 40, name: 'فطر أبيض (مشروم)', nameEn: 'Mushroom', nameNl: 'Champignons', icon: '🍄', category: 'خضروات', categoryNl: 'Groenten', gi: 10, ii: 17, nutrition: { calories: 22, protein: 3.1, carbs: 3.3, fat: 0.3, fiber: 1 } },
    { id: 41, name: 'أرضي شوكي (خرشوف)', nameEn: 'Artichoke', nameNl: 'Artisjok', icon: '🥬', category: 'خضروات', categoryNl: 'Groenten', gi: 20, ii: 21, nutrition: { calories: 47, protein: 3.3, carbs: 11, fat: 0.2, fiber: 5.4 } },
    { id: 42, name: 'هليون أخضر', nameEn: 'Asparagus', nameNl: 'Groene asperges', icon: '🌿', category: 'خضروات', categoryNl: 'Groenten', gi: 15, ii: 16, nutrition: { calories: 20, protein: 2.2, carbs: 3.9, fat: 0.2, fiber: 2.1 } },
    { id: 43, name: 'شمندر أحمر (بنجر)', nameEn: 'Beetroot', nameNl: 'Rode biet', icon: '🥕', category: 'خضروات', categoryNl: 'Groenten', gi: 61, ii: 55, nutrition: { calories: 43, protein: 1.6, carbs: 9.6, fat: 0.2, fiber: 2.8 } },
    { id: 44, name: 'جرجير بلدي', nameEn: 'Arugula (Rocket)', nameNl: 'Rucola', icon: '🌿', category: 'خضروات', categoryNl: 'Groenten', gi: 15, ii: 15, nutrition: { calories: 25, protein: 2.6, carbs: 3.7, fat: 0.7, fiber: 1.6 } },
    { id: 45, name: 'بصل أحمر/أبيض', nameEn: 'Onion', nameNl: 'Uien', icon: '🧅', category: 'خضروات', categoryNl: 'Groenten', gi: 10, ii: 14, nutrition: { calories: 40, protein: 1.1, carbs: 9.3, fat: 0.1, fiber: 1.7 } },
    { id: 46, name: 'ثوم طازج', nameEn: 'Garlic', nameNl: 'Knoflook', icon: '🧄', category: 'خضروات', categoryNl: 'Groenten', gi: 10, ii: 10, nutrition: { calories: 149, protein: 6.4, carbs: 33, fat: 0.5, fiber: 2.1 } },
    { id: 47, name: 'فلفل أخضر بارد', nameEn: 'Green Bell Pepper', nameNl: 'Groene paprika', icon: '🫑', category: 'خضروات', categoryNl: 'Groenten', gi: 10, ii: 10, nutrition: { calories: 20, protein: 0.9, carbs: 4.6, fat: 0.2, fiber: 1.7 } },

    // === الفواكه (Fruit) ===
    { id: 48, name: 'تفاح أحمر/أخضر', nameEn: 'Apple', nameNl: 'Appel', icon: '🍎', category: 'فواكه', categoryNl: 'Fruit', gi: 36, ii: 59, nutrition: { calories: 52, protein: 0.3, carbs: 14, fat: 0.2, fiber: 2.4 } },
    { id: 49, name: 'موز أصفر', nameEn: 'Banana', nameNl: 'Banaan', icon: '🍌', category: 'فواكه', categoryNl: 'Fruit', gi: 51, ii: 81, nutrition: { calories: 89, protein: 1.1, carbs: 23, fat: 0.3, fiber: 2.6 } },
    { id: 50, name: 'برتقال أبو صرة', nameEn: 'Orange', nameNl: 'Sinaasappel', icon: '🍊', category: 'فواكه', categoryNl: 'Fruit', gi: 43, ii: 60, nutrition: { calories: 47, protein: 0.9, carbs: 12, fat: 0.1, fiber: 2.4 } },
    { id: 51, name: 'بطيخ أحمر (جبس)', nameEn: 'Watermelon', nameNl: 'Watermeloen', icon: '🍉', category: 'فواكه', categoryNl: 'Fruit', gi: 72, ii: 51, nutrition: { calories: 30, protein: 0.6, carbs: 8, fat: 0.2, fiber: 0.4 } },
    { id: 52, name: 'فراولة طازجة', nameEn: 'Strawberry', nameNl: 'Aardbeien', icon: '🍓', category: 'فواكه', categoryNl: 'Fruit', gi: 40, ii: 40, nutrition: { calories: 32, protein: 0.7, carbs: 8, fat: 0.3, fiber: 2 } },
    { id: 53, name: 'عنب أحمر/أخضر', nameEn: 'Grapes', nameNl: 'Druiven', icon: '🍇', category: 'فواكه', categoryNl: 'Fruit', gi: 59, ii: 82, nutrition: { calories: 69, protein: 0.7, carbs: 18, fat: 0.2, fiber: 0.9 } },
    { id: 54, name: 'أناناس طازج', nameEn: 'Pineapple', nameNl: 'Ananas', icon: '🍍', category: 'فواكه', categoryNl: 'Fruit', gi: 59, ii: 84, nutrition: { calories: 50, protein: 0.5, carbs: 13, fat: 0.1, fiber: 1.4 } },
    { id: 55, name: 'مانجو طازجة', nameEn: 'Mango', nameNl: 'Mango', icon: '🥭', category: 'فواكه', categoryNl: 'Fruit', gi: 51, ii: 60, nutrition: { calories: 60, protein: 0.8, carbs: 15, fat: 0.4, fiber: 1.6 } },
    { id: 56, name: 'توت أزرق (بلوبيري)', nameEn: 'Blueberry', nameNl: 'Blauwe bessen', icon: '🫐', category: 'فواكه', categoryNl: 'Fruit', gi: 53, ii: 56, nutrition: { calories: 57, protein: 0.7, carbs: 14, fat: 0.3, fiber: 2.4 } },
    { id: 57, name: 'توت العليق (راسبيري)', nameEn: 'Raspberry', nameNl: 'Frambozen', icon: '🍇', category: 'فواكه', categoryNl: 'Fruit', gi: 32, ii: 37, nutrition: { calories: 52, protein: 1.2, carbs: 12, fat: 0.7, fiber: 6.5 } },
    { id: 58, name: 'كرز أحمر', nameEn: 'Cherry', nameNl: 'Kersen', icon: '🍒', category: 'فواكه', categoryNl: 'Fruit', gi: 22, ii: 40, nutrition: { calories: 63, protein: 1.1, carbs: 16, fat: 0.2, fiber: 2.1 } },
    { id: 59, name: 'أفوكادو', nameEn: 'Avocado', nameNl: 'Avocado', icon: '🥑', category: 'فواكه', categoryNl: 'Fruit', gi: 15, ii: 10, nutrition: { calories: 160, protein: 2, carbs: 9, fat: 15, fiber: 7 } },
    { id: 60, name: 'تين أسود/أخضر', nameEn: 'Fig', nameNl: 'Vijgen', icon: '🍇', category: 'فواكه', categoryNl: 'Fruit', gi: 61, ii: 58, nutrition: { calories: 74, protein: 0.8, carbs: 19, fat: 0.3, fiber: 2.9 } },
    { id: 61, name: 'رمان حب', nameEn: 'Pomegranate', nameNl: 'Granaatappel', icon: '🍎', category: 'فواكه', categoryNl: 'Fruit', gi: 53, ii: 60, nutrition: { calories: 83, protein: 1.7, carbs: 19, fat: 1.2, fiber: 4 } },
    { id: 62, name: 'تمر رطب (سكري/مجدول)', nameEn: 'Fresh Dates', nameNl: 'Verse dadels (Medjoul)', icon: '🌴', category: 'فواكه', categoryNl: 'Fruit', gi: 103, ii: 110, nutrition: { calories: 277, protein: 1.8, carbs: 75, fat: 0.2, fiber: 6.7 } },
    { id: 63, name: 'تمر مجفف', nameEn: 'Dried Dates', nameNl: 'Gedroogde dadels', icon: '🌴', category: 'فواكه', categoryNl: 'Fruit', gi: 62, ii: 85, nutrition: { calories: 282, protein: 2.5, carbs: 75, fat: 0.4, fiber: 8 } },
    { id: 64, name: 'كيوي أخضر', nameEn: 'Kiwi', nameNl: 'Kiwi', icon: '🥝', category: 'فواكه', categoryNl: 'Fruit', gi: 53, ii: 47, nutrition: { calories: 61, protein: 1.1, carbs: 15, fat: 0.5, fiber: 3 } },
    { id: 65, name: 'خوخ طازج (دراق)', nameEn: 'Peach', nameNl: 'Perzik', icon: '🍑', category: 'فواكه', categoryNl: 'Fruit', gi: 42, ii: 60, nutrition: { calories: 39, protein: 0.9, carbs: 10, fat: 0.3, fiber: 1.5 } },
    { id: 66, name: 'كمثرى (إجاص)', nameEn: 'Pear', nameNl: 'Peer', icon: '🍐', category: 'فواكه', categoryNl: 'Fruit', gi: 38, ii: 60, nutrition: { calories: 57, protein: 0.4, carbs: 15, fat: 0.1, fiber: 3.1 } },
    { id: 67, name: 'شمام (بطيخ أصفر)', nameEn: 'Cantaloupe', nameNl: 'Meloen', icon: '🍈', category: 'فواكه', categoryNl: 'Fruit', gi: 65, ii: 70, nutrition: { calories: 34, protein: 0.8, carbs: 8, fat: 0.2, fiber: 0.9 } },
    { id: 68, name: 'زبيب أسود مجفف', nameEn: 'Raisins', nameNl: 'Rozijnen', icon: '🍇', category: 'فواكه', categoryNl: 'Fruit', gi: 64, ii: 62, nutrition: { calories: 299, protein: 3.1, carbs: 79, fat: 0.5, fiber: 3.7 } },

    // === الألبان والأجبان (Zuivel & Kaas) ===
    { id: 69, name: 'حليب كامل الدسم 3.5%', nameEn: 'Whole Milk', nameNl: 'Volle melk', icon: '🥛', category: 'ألبان', categoryNl: 'Zuivel', gi: 39, ii: 90, nutrition: { calories: 61, protein: 3.2, carbs: 4.8, fat: 3.3, fiber: 0 } },
    { id: 70, name: 'حليب خالي الدسم', nameEn: 'Skim Milk', nameNl: 'Magere melk', icon: '🥛', category: 'ألبان', categoryNl: 'Zuivel', gi: 32, ii: 90, nutrition: { calories: 34, protein: 3.4, carbs: 5, fat: 0.1, fiber: 0 } },
    { id: 71, name: 'لبن زبادي يوناني 10%', nameEn: 'Greek Yogurt 10%', nameNl: 'Griekse yoghurt 10%', icon: '🥛', category: 'ألبان', categoryNl: 'Zuivel', gi: 11, ii: 20, nutrition: { calories: 120, protein: 9, carbs: 3.9, fat: 10, fiber: 0 } },
    { id: 72, name: 'لبنة مصفاة بلدية', nameEn: 'Labneh', nameNl: 'Labneh (uitgelekte yoghurt)', icon: '🧈', category: 'ألبان', categoryNl: 'Zuivel', gi: 10, ii: 30, nutrition: { calories: 111, protein: 5.2, carbs: 3.8, fat: 9, fiber: 0 } },
    { id: 73, name: 'جبنة موزاريلا', nameEn: 'Mozzarella', nameNl: 'Mozzarella', icon: '🧀', category: 'ألبان', categoryNl: 'Zuivel', gi: 0, ii: 45, nutrition: { calories: 280, protein: 28, carbs: 2.2, fat: 17, fiber: 0 } },
    { id: 74, name: 'جبنة شيدر معتقة', nameEn: 'Cheddar Cheese', nameNl: 'Cheddar kaas', icon: '🧀', category: 'ألبان', categoryNl: 'Zuivel', gi: 0, ii: 42, nutrition: { calories: 403, protein: 25, carbs: 1.3, fat: 33, fiber: 0 } },
    { id: 75, name: 'جبنة جودا هولندية', nameEn: 'Gouda Cheese', nameNl: 'Goudse kaas', icon: '🧀', category: 'ألبان', categoryNl: 'Zuivel', gi: 0, ii: 43, nutrition: { calories: 356, protein: 25, carbs: 2.2, fat: 27, fiber: 0 } },
    { id: 76, name: 'جبنة قريش خفيفة', nameEn: 'Cottage Cheese', nameNl: 'Hüttenkäse', icon: '🧀', category: 'ألبان', categoryNl: 'Zuivel', gi: 10, ii: 32, nutrition: { calories: 98, protein: 11, carbs: 3.4, fat: 4.3, fiber: 0 } },
    { id: 77, name: 'جبنة حلوم', nameEn: 'Halloumi Cheese', nameNl: 'Halloumi', icon: '🧀', category: 'ألبان', categoryNl: 'Zuivel', gi: 0, ii: 39, nutrition: { calories: 316, protein: 21, carbs: 2.7, fat: 25, fiber: 0 } },
    { id: 78, name: 'زبدة طبيعية حيوانية', nameEn: 'Butter', nameNl: 'Roomboter', icon: '🧈', category: 'ألبان', categoryNl: 'Zuivel', gi: 0, ii: 7, nutrition: { calories: 717, protein: 0.9, carbs: 0.1, fat: 81, fiber: 0 } },
    { id: 79, name: 'كفير طبيعي مخمر', nameEn: 'Kefir', nameNl: 'Kefir', icon: '🥛', category: 'ألبان', categoryNl: 'Zuivel', gi: 30, ii: 40, nutrition: { calories: 41, protein: 3.3, carbs: 4.5, fat: 1, fiber: 0 } },

    // === المكسرات والبذور (Noten & Zaden) ===
    { id: 80, name: 'لوز نيء', nameEn: 'Raw Almonds', nameNl: 'Rauwe amandelen', icon: '🥜', category: 'مكسرات', categoryNl: 'Noten & Zaden', gi: 0, ii: 15, nutrition: { calories: 579, protein: 21, carbs: 22, fat: 50, fiber: 12.5 } },
    { id: 81, name: 'جوز عين الجمل', nameEn: 'Walnuts', nameNl: 'Walnoten', icon: '🥜', category: 'مكسرات', categoryNl: 'Noten & Zaden', gi: 15, ii: 16, nutrition: { calories: 654, protein: 15, carbs: 14, fat: 65, fiber: 6.7 } },
    { id: 82, name: 'كاجو محمص', nameEn: 'Cashews', nameNl: 'Cashewnoten', icon: '🥜', category: 'مكسرات', categoryNl: 'Noten & Zaden', gi: 22, ii: 25, nutrition: { calories: 553, protein: 18, carbs: 30, fat: 44, fiber: 3.3 } },
    { id: 83, name: 'فستق حلبي', nameEn: 'Pistachios', nameNl: 'Pistachenoten', icon: '🥜', category: 'مكسرات', categoryNl: 'Noten & Zaden', gi: 15, ii: 20, nutrition: { calories: 560, protein: 20, carbs: 28, fat: 45, fiber: 10.6 } },
    { id: 84, name: 'بندق طازج', nameEn: 'Hazelnuts', nameNl: 'Hazelnoten', icon: '🌰', category: 'مكسرات', categoryNl: 'Noten & Zaden', gi: 15, ii: 17, nutrition: { calories: 628, protein: 15, carbs: 17, fat: 61, fiber: 9.7 } },
    { id: 85, name: 'بذور الشيا العضوية', nameEn: 'Chia Seeds', nameNl: 'Chiazaden', icon: '🌾', category: 'مكسرات', categoryNl: 'Noten & Zaden', gi: 1, ii: 1, nutrition: { calories: 486, protein: 17, carbs: 42, fat: 31, fiber: 34 } },
    { id: 86, name: 'بذور الكتان الذهبية', nameEn: 'Flax Seeds', nameNl: 'Lijnzaad', icon: '🌾', category: 'مكسرات', categoryNl: 'Noten & Zaden', gi: 35, ii: 18, nutrition: { calories: 534, protein: 18, carbs: 29, fat: 42, fiber: 27 } },
    { id: 87, name: 'بذور اليقطين (بزر أبيض)', nameEn: 'Pumpkin Seeds', nameNl: 'Pompoenpitten', icon: '🎃', category: 'مكسرات', categoryNl: 'Noten & Zaden', gi: 25, ii: 15, nutrition: { calories: 559, protein: 30, carbs: 11, fat: 49, fiber: 6 } },
    { id: 88, name: 'بذور دوار الشمس (بزر سوري)', nameEn: 'Sunflower Seeds', nameNl: 'Zonnebloempitten', icon: '🌻', category: 'مكسرات', categoryNl: 'Noten & Zaden', gi: 35, ii: 20, nutrition: { calories: 584, protein: 21, carbs: 20, fat: 51, fiber: 8.6 } },
    { id: 89, name: 'فول سوداني محمص', nameEn: 'Peanuts', nameNl: 'Pinda\'s', icon: '🥜', category: 'مكسرات', categoryNl: 'Noten & Zaden', gi: 14, ii: 20, nutrition: { calories: 567, protein: 26, carbs: 16, fat: 49, fiber: 8.5 } },
    { id: 90, name: 'زبدة فول سوداني 100% طبيعية', nameEn: 'Natural Peanut Butter', nameNl: 'Pindakaas 100% natuurlijk', icon: '🥜', category: 'مكسرات', categoryNl: 'Noten & Zaden', gi: 14, ii: 20, nutrition: { calories: 588, protein: 25, carbs: 20, fat: 50, fiber: 6 } },

    // === اللحوم، الأسماك، والبروتين (Vlees, Vis & Eiwitten) ===
    { id: 91, name: 'صدر دجاج مشوي', nameEn: 'Grilled Chicken Breast', nameNl: 'Gegrilde kipfilet', icon: '🍗', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 51, nutrition: { calories: 165, protein: 31, carbs: 0, fat: 3.6, fiber: 0 } },
    { id: 92, name: 'لحم بقري ستيك مشوي', nameEn: 'Grilled Beef Steak', nameNl: 'Runderbiefstuk', icon: '🥩', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 51, nutrition: { calories: 250, protein: 26, carbs: 0, fat: 15, fiber: 0 } },
    { id: 93, name: 'لحم غنم مشوي', nameEn: 'Lamb Meat', nameNl: 'Lamsvlees', icon: '🥩', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 51, nutrition: { calories: 294, protein: 25, carbs: 0, fat: 21, fiber: 0 } },
    { id: 94, name: 'سمك سلمون طازج مشوي', nameEn: 'Grilled Salmon', nameNl: 'Gegrilde zalm', icon: '🐟', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 59, nutrition: { calories: 208, protein: 20, carbs: 0, fat: 13, fiber: 0 } },
    { id: 95, name: 'سلمون مدخن', nameEn: 'Smoked Salmon', nameNl: 'Gerookte zalm', icon: '🐟', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 40, nutrition: { calories: 117, protein: 18.3, carbs: 0, fat: 4.3, fiber: 0 } },
    { id: 96, name: 'سمك القد الأبيض (Kabeljauw)', nameEn: 'Cod Fish', nameNl: 'Kabeljauwfilet', icon: '🐟', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 59, nutrition: { calories: 82, protein: 17.8, carbs: 0, fat: 0.7, fiber: 0 } },
    { id: 97, name: 'سمك الماكريل (Makreel)', nameEn: 'Mackerel', nameNl: 'Makreel', icon: '🐟', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 55, nutrition: { calories: 205, protein: 18.6, carbs: 0, fat: 13.9, fiber: 0 } },
    { id: 98, name: 'تونة معلبة بالماء', nameEn: 'Canned Tuna in Water', nameNl: 'Tonijn in water (blik)', icon: '🥫', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 26, nutrition: { calories: 116, protein: 26, carbs: 0, fat: 0.8, fiber: 0 } },
    { id: 99, name: 'سردين معلب بالزيت', nameEn: 'Canned Sardines', nameNl: 'Sardines in olie (blik)', icon: '🥫', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 30, nutrition: { calories: 208, protein: 25, carbs: 0, fat: 11, fiber: 0 } },
    { id: 100, name: 'روبيان (جمبري) مشوي', nameEn: 'Grilled Shrimp', nameNl: 'Gegrilde garnalen', icon: '🦐', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 28, nutrition: { calories: 99, protein: 24, carbs: 0.2, fat: 0.3, fiber: 0 } },
    { id: 101, name: 'بيض مسلوق كامل', nameEn: 'Boiled Egg', nameNl: 'Gekookt ei', icon: '🥚', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 42, nutrition: { calories: 155, protein: 13, carbs: 1.1, fat: 11, fiber: 0 } },
    { id: 102, name: 'أومليت بيض بالزبدة', nameEn: 'Egg Omelette', nameNl: 'Omelet met boter', icon: '🍳', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 42, nutrition: { calories: 154, protein: 11, carbs: 1.3, fat: 12, fiber: 0 } },
    { id: 103, name: 'كبدة عجل مشوية', nameEn: 'Beef Liver', nameNl: 'Runderlever', icon: '🥩', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 73, nutrition: { calories: 135, protein: 20, carbs: 3.9, fat: 4, fiber: 0 } },

    // === الأطباق العربية والشرقية (Arabische Gerechten) ===
    { id: 104, name: 'حمص بطحينة أصلي', nameEn: 'Hummus with Tahini', nameNl: 'Hummus met tahini', icon: '🥣', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 15, ii: 25, nutrition: { calories: 166, protein: 8, carbs: 14, fat: 10, fiber: 6 } },
    { id: 105, name: 'فلافل مقلية مقرمشة', nameEn: 'Falafel', nameNl: 'Falafel', icon: '🧆', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 35, ii: 40, nutrition: { calories: 333, protein: 13, carbs: 32, fat: 18, fiber: 5 } },
    { id: 106, name: 'فول مدمس بالزيت والكمون', nameEn: 'Foul Mudammas', nameNl: 'Ful Mudammas', icon: '🫘', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 40, ii: 57, nutrition: { calories: 187, protein: 10, carbs: 23, fat: 7, fiber: 9.3 } },
    { id: 107, name: 'متبل باذنجان (بابا غنوج)', nameEn: 'Baba Ghanoush', nameNl: 'Baba Ghanoush (Moutabal)', icon: '🍆', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 15, ii: 20, nutrition: { calories: 160, protein: 3, carbs: 9, fat: 13, fiber: 4 } },
    { id: 108, name: 'تبولة بلدية بالبقدونس', nameEn: 'Tabbouleh', nameNl: 'Taboulé salade', icon: '🥗', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 35, ii: 30, nutrition: { calories: 90, protein: 2.5, carbs: 14, fat: 3.5, fiber: 3.5 } },
    { id: 109, name: 'فتوش بالدبس وزيت الزيتون', nameEn: 'Fattoush', nameNl: 'Fattoush salade', icon: '🥗', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 40, ii: 38, nutrition: { calories: 115, protein: 2.8, carbs: 16, fat: 5, fiber: 3 } },
    { id: 110, name: 'ملوخية ورق بالدجاج', nameEn: 'Molokhia with Chicken', nameNl: 'Molokhia met kip', icon: '🥬', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 15, ii: 25, nutrition: { calories: 115, protein: 14, carbs: 6, fat: 4, fiber: 2 } },
    { id: 111, name: 'شاورما دجاج سوري', nameEn: 'Chicken Shawarma', nameNl: 'Kip shoarma', icon: '🌯', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 45, ii: 58, nutrition: { calories: 265, protein: 22, carbs: 18, fat: 12, fiber: 2 } },
    { id: 112, name: 'شاورما لحم عجل', nameEn: 'Beef Shawarma', nameNl: 'Runder shoarma', icon: '🌯', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 40, ii: 65, nutrition: { calories: 295, protein: 24, carbs: 18, fat: 15, fiber: 2.5 } },
    { id: 113, name: 'شيش طاووق مشوي', nameEn: 'Shish Taouk', nameNl: 'Shish Taouk spiesjes', icon: '🍢', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 0, ii: 51, nutrition: { calories: 185, protein: 26, carbs: 2, fat: 8, fiber: 0.5 } },
    { id: 114, name: 'كفتة مشوية على الفحم', nameEn: 'Grilled Kofta', nameNl: 'Gegrilde gehaktspies (Kofta)', icon: '🍢', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 0, ii: 52, nutrition: { calories: 255, protein: 22, carbs: 4, fat: 17, fiber: 1 } },
    { id: 115, name: 'كبة مقلية شامية', nameEn: 'Fried Kibbeh', nameNl: 'Gebakken Kibbeh', icon: '🧆', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 58, ii: 62, nutrition: { calories: 285, protein: 14, carbs: 22, fat: 16, fiber: 3 } },
    { id: 116, name: 'كبة نية بلحم الهبرة', nameEn: 'Raw Kibbeh', nameNl: 'Rauwe Kibbeh', icon: '🥩', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 42, ii: 55, nutrition: { calories: 195, protein: 15, carbs: 18, fat: 7, fiber: 3 } },
    { id: 117, name: 'ورق عنب يالنجي بالزيت', nameEn: 'Stuffed Grape Leaves', nameNl: 'Gevulde wijnbladeren (Yalanji)', icon: '🍃', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 42, ii: 40, nutrition: { calories: 158, protein: 3, carbs: 22, fat: 6.5, fiber: 2.1 } },
    { id: 118, name: 'كوسا محشي باللحم والأرز', nameEn: 'Stuffed Zucchini', nameNl: 'Gevulde courgette', icon: '🥒', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 45, ii: 50, nutrition: { calories: 145, protein: 6.5, carbs: 18, fat: 5.5, fiber: 3 } },
    { id: 119, name: 'منسف أردني بلحم الغنم', nameEn: 'Jordanian Mansaf', nameNl: 'Mansaf met lamsvlees', icon: '🍲', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 52, ii: 70, nutrition: { calories: 380, protein: 24, carbs: 38, fat: 15, fiber: 1.5 } },
    { id: 120, name: 'مقلوبة دجاج بالباذنجان', nameEn: 'Maqluba', nameNl: 'Maqluba met kip en aubergine', icon: '🍲', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 55, ii: 65, nutrition: { calories: 295, protein: 18, carbs: 38, fat: 8.5, fiber: 3.5 } },
    { id: 121, name: 'مجدرة برغل بزيت الزيتون', nameEn: 'Mujadara', nameNl: 'Mujaddara (linzen & bulgur)', icon: '🍚', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 44, ii: 52, nutrition: { calories: 212, protein: 9, carbs: 35, fat: 4, fiber: 7.8 } },
    { id: 122, name: 'فتة حمص باللبن والمكسرات', nameEn: 'Fatteh Hummus', nameNl: 'Fatteh met kikkererwten en yoghurt', icon: '🥙', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 48, ii: 62, nutrition: { calories: 310, protein: 12, carbs: 32, fat: 15, fiber: 7 } },
    { id: 123, name: 'صيادية سمك بالبصل المحمر', nameEn: 'Fish Sayadieh', nameNl: 'Sayadieh vis met rijst', icon: '🐟', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 52, ii: 64, nutrition: { calories: 298, protein: 22, carbs: 30, fat: 10, fiber: 2 } },
    { id: 124, name: 'مسخن دجاج فلسطيني', nameEn: 'Palestinian Musakhan', nameNl: 'Palestijnse Musakhan', icon: '🍗', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 55, ii: 65, nutrition: { calories: 358, protein: 22, carbs: 38, fat: 14, fiber: 2.8 } },
    { id: 125, name: 'شكشوكة بيض بالبندورة', nameEn: 'Shakshuka', nameNl: 'Shakshuka', icon: '🍳', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 25, ii: 45, nutrition: { calories: 167, protein: 11, carbs: 8, fat: 11, fiber: 2.1 } },
    { id: 126, name: 'شوربة عدس سورية صفراء', nameEn: 'Lentil Soup', nameNl: 'Gele linzensoep', icon: '🍲', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 32, ii: 50, nutrition: { calories: 116, protein: 8.6, carbs: 19, fat: 0.8, fiber: 7.8 } },
    { id: 127, name: 'كشري مصري', nameEn: 'Egyptian Koshari', nameNl: 'Egyptische Koshari', icon: '🍝', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 62, ii: 58, nutrition: { calories: 320, protein: 11, carbs: 58, fat: 5, fiber: 8 } },

    // === الزيوت والدهون الطبيعية (Natuurlijke Oliën & Vetten) ===
    { id: 128, name: 'زيت زيتون بكر ممتاز', nameEn: 'Extra Virgin Olive Oil', nameNl: 'Extra vierge olijfolie', icon: '🫒', category: 'زيوت', categoryNl: 'Oliën & Vetten', gi: 0, ii: 0, nutrition: { calories: 884, protein: 0, carbs: 0, fat: 100, fiber: 0 } },
    { id: 129, name: 'سمن بلدي بقري/غنم', nameEn: 'Ghee', nameNl: 'Ghee (geklaarde boter)', icon: '🧈', category: 'زيوت', categoryNl: 'Oliën & Vetten', gi: 0, ii: 7, nutrition: { calories: 898, protein: 0, carbs: 0, fat: 99.8, fiber: 0 } },
    { id: 130, name: 'زيت جوز هند بكر', nameEn: 'Virgin Coconut Oil', nameNl: 'Kokosolie', icon: '🥥', category: 'زيوت', categoryNl: 'Oliën & Vetten', gi: 0, ii: 0, nutrition: { calories: 862, protein: 0, carbs: 0, fat: 100, fiber: 0 } },
    { id: 131, name: 'طحينة سمسم سائلة', nameEn: 'Tahini Paste', nameNl: 'Witte sesampasta (Tahini)', icon: '🥜', category: 'زيوت', categoryNl: 'Oliën & Vetten', gi: 12, ii: 18, nutrition: { calories: 595, protein: 17, carbs: 21, fat: 54, fiber: 9.3 } },

    // === المشروبات (Dranken) ===
    { id: 132, name: 'قهوة سوداء سادة (إسبريسو)', nameEn: 'Black Coffee', nameNl: 'Zwarte koffie (Espresso)', icon: '☕', category: 'مشروبات', categoryNl: 'Dranken', gi: 0, ii: 0, nutrition: { calories: 2, protein: 0.3, carbs: 0, fat: 0, fiber: 0 } },
    { id: 133, name: 'شاي أخضر طبيعي', nameEn: 'Green Tea', nameNl: 'Groene thee', icon: '🍵', category: 'مشروبات', categoryNl: 'Dranken', gi: 0, ii: 0, nutrition: { calories: 2, protein: 0.2, carbs: 0, fat: 0, fiber: 0 } },
    { id: 134, name: 'ماتشا يابانية عضوية', nameEn: 'Matcha Tea', nameNl: 'Japanse matcha thee', icon: '🍵', category: 'مشروبات', categoryNl: 'Dranken', gi: 0, ii: 5, nutrition: { calories: 3, protein: 0.3, carbs: 0.4, fat: 0, fiber: 0.4 } },
    { id: 135, name: 'حليب اللوز غير محلى', nameEn: 'Unsweetened Almond Milk', nameNl: 'Ongezoete amandelmelk', icon: '🥛', category: 'مشروبات', categoryNl: 'Dranken', gi: 25, ii: 20, nutrition: { calories: 15, protein: 0.6, carbs: 0.3, fat: 1.1, fiber: 0.2 } },
    { id: 136, name: 'عيران (شنينة / لبن مملح)', nameEn: 'Ayran', nameNl: 'Ayran karnemelk', icon: '🥛', category: 'مشروبات', categoryNl: 'Dranken', gi: 30, ii: 35, nutrition: { calories: 38, protein: 2.2, carbs: 3.5, fat: 1.8, fiber: 0 } },
    { id: 137, name: 'ماء جوز الهند الطبيعي', nameEn: 'Coconut Water', nameNl: 'Kokoswater', icon: '🥥', category: 'مشروبات', categoryNl: 'Dranken', gi: 54, ii: 45, nutrition: { calories: 19, protein: 0.7, carbs: 3.7, fat: 0.2, fiber: 1.1 } },
    { id: 138, name: 'عصير برتقال طازج', nameEn: 'Fresh Orange Juice', nameNl: 'Vers geperst sinaasappelsap', icon: '🍊', category: 'مشروبات', categoryNl: 'Dranken', gi: 50, ii: 71, nutrition: { calories: 45, protein: 0.7, carbs: 10, fat: 0.2, fiber: 0.2 } },
    { id: 139, name: 'عصير رمان طبيعي', nameEn: 'Pomegranate Juice', nameNl: 'Vers granaatappelsap', icon: '🍎', category: 'مشروبات', categoryNl: 'Dranken', gi: 53, ii: 58, nutrition: { calories: 54, protein: 0.4, carbs: 13, fat: 0.3, fiber: 0.1 } },
    { id: 140, name: 'كولا غازية عادية', nameEn: 'Coca Cola', nameNl: 'Coca Cola', icon: '🥤', category: 'مشروبات', categoryNl: 'Dranken', gi: 63, ii: 70, nutrition: { calories: 42, protein: 0, carbs: 11, fat: 0, fiber: 0 } },

    // === وجبات سريعة ومطاعم (Fastfood) ===
    { id: 141, name: 'بيج ماك', nameEn: 'Big Mac', nameNl: 'Big Mac burger', icon: '🍔', category: 'مطاعم', categoryNl: 'Fastfood', gi: 55, ii: 72, nutrition: { calories: 563, protein: 26, carbs: 46, fat: 33, fiber: 3.2 } },
    { id: 142, name: 'تشيكن ناغتس (6 قطع)', nameEn: 'Chicken Nuggets (6pc)', nameNl: 'Kipnuggets (6 stuks)', icon: '🍗', category: 'مطاعم', categoryNl: 'Fastfood', gi: 46, ii: 55, nutrition: { calories: 270, protein: 16, carbs: 16, fat: 17, fiber: 1 } },
    { id: 143, name: 'دجاج مقلي بروستد (KFC)', nameEn: 'KFC Fried Chicken', nameNl: 'KFC Krokante kip', icon: '🍗', category: 'مطاعم', categoryNl: 'Fastfood', gi: 45, ii: 58, nutrition: { calories: 320, protein: 24, carbs: 12, fat: 21, fiber: 1 } },
    { id: 144, name: 'بيتزا مارغريتا (شريحة)', nameEn: 'Margherita Pizza (Slice)', nameNl: 'Pizza Margherita (punt)', icon: '🍕', category: 'مطاعم', categoryNl: 'Fastfood', gi: 60, ii: 68, nutrition: { calories: 250, protein: 11, carbs: 32, fat: 9, fiber: 2 } },
    { id: 145, name: 'بيتزا بيبروني (شريحة)', nameEn: 'Pepperoni Pizza (Slice)', nameNl: 'Pizza Pepperoni (punt)', icon: '🍕', category: 'مطاعم', categoryNl: 'Fastfood', gi: 60, ii: 70, nutrition: { calories: 300, protein: 13, carbs: 33, fat: 13, fiber: 2 } },
    { id: 146, name: 'ساندويش صب واي دجاج تيرياكي', nameEn: 'Subway Chicken Teriyaki', nameNl: 'Subway Chicken Teriyaki broodje', icon: '🥖', category: 'مطاعم', categoryNl: 'Fastfood', gi: 52, ii: 62, nutrition: { calories: 360, protein: 24, carbs: 54, fat: 5, fiber: 5 } },
    { id: 147, name: 'سلطة كول سلو', nameEn: 'Coleslaw', nameNl: 'Koolsalade (Coleslaw)', icon: '🥗', category: 'مطاعم', categoryNl: 'Fastfood', gi: 30, ii: 35, nutrition: { calories: 152, protein: 1.4, carbs: 11, fat: 12, fiber: 2.3 } },

    // === الحلويات والمخبوزات (Desserts & Gebak) ===
    { id: 148, name: 'بقلاوة بالفستق الحلبي', nameEn: 'Baklava', nameNl: 'Baklava met pistache', icon: '🥐', category: 'حلويات', categoryNl: 'Desserts', gi: 67, ii: 72, nutrition: { calories: 428, protein: 6, carbs: 51, fat: 23, fiber: 2.5 } },
    { id: 149, name: 'كنافة نابلسية بالجبن', nameEn: 'Nabulsi Kunafa', nameNl: 'Knafeh met kaas', icon: '🧀', category: 'حلويات', categoryNl: 'Desserts', gi: 72, ii: 85, nutrition: { calories: 385, protein: 8, carbs: 47, fat: 19, fiber: 1.2 } },
    { id: 150, name: 'بسبوسة بالسمن البلدي', nameEn: 'Basbousa', nameNl: 'Basbousa griesmeelcake', icon: '🍰', category: 'حلويات', categoryNl: 'Desserts', gi: 70, ii: 80, nutrition: { calories: 358, protein: 5, carbs: 52, fat: 15, fiber: 1.8 } },
    { id: 151, name: 'معمول بالتمر والشومر', nameEn: 'Date Maamoul', nameNl: 'Ma\'amoul dadelkoekjes', icon: '🍪', category: 'حلويات', categoryNl: 'Desserts', gi: 62, ii: 65, nutrition: { calories: 325, protein: 4.5, carbs: 48, fat: 13, fiber: 4 } },
    { id: 152, name: 'حلاوة طحينية بالمكسرات', nameEn: 'Halva', nameNl: 'Halva sesamsnoep', icon: '🍯', category: 'حلويات', categoryNl: 'Desserts', gi: 45, ii: 50, nutrition: { calories: 469, protein: 13, carbs: 58, fat: 21, fiber: 3.5 } },
    { id: 153, name: 'مهلبية الحليب والمستكة', nameEn: 'Mahalabia', nameNl: 'Mahalabia melkpudding', icon: '🍮', category: 'حلويات', categoryNl: 'Desserts', gi: 55, ii: 65, nutrition: { calories: 142, protein: 3.5, carbs: 22, fat: 4.5, fiber: 0.3 } },
    { id: 154, name: 'أرز بالحليب والقرفة', nameEn: 'Rice Pudding', nameNl: 'Rijstpudding', icon: '🍮', category: 'حلويات', categoryNl: 'Desserts', gi: 65, ii: 70, nutrition: { calories: 133, protein: 3.2, carbs: 23, fat: 3.3, fiber: 0.3 } },
    { id: 155, name: 'شوكولاتة داكنة 85%', nameEn: 'Dark Chocolate 85%', nameNl: 'Pure chocolade 85%', icon: '🍫', category: 'حلويات', categoryNl: 'Desserts', gi: 20, ii: 25, nutrition: { calories: 599, protein: 8, carbs: 35, fat: 48, fiber: 12 } },
    { id: 156, name: 'كرواسون زبدة فرنسي', nameEn: 'Butter Croissant', nameNl: 'Boter croissant', icon: '🥐', category: 'حلويات', categoryNl: 'Desserts', gi: 67, ii: 74, nutrition: { calories: 406, protein: 8, carbs: 46, fat: 21, fiber: 2.6 } },
    { id: 157, name: 'تشيز كيك نيويورك', nameEn: 'Cheesecake', nameNl: 'New York cheesecake', icon: '🍰', category: 'حلويات', categoryNl: 'Desserts', gi: 55, ii: 55, nutrition: { calories: 321, protein: 5.5, carbs: 26, fat: 23, fiber: 0.8 } },
// === أطعمة مكسيكية (Mexicaanse Keuken) ===
    { id: 158, name: 'تاكو لحم بقري', nameEn: 'Beef Taco', nameNl: 'Mexicaanse runder taco', icon: '🌮', category: 'أطعمة مكسيكية', categoryNl: 'Mexicaanse Keuken', gi: 50, ii: 60, nutrition: { calories: 226, protein: 11, carbs: 20, fat: 11, fiber: 3.5 } },
    { id: 159, name: 'بوريتو دجاج وفاصوليا', nameEn: 'Chicken Burrito', nameNl: 'Kip burrito met bonen', icon: '🌯', category: 'أطعمة مكسيكية', categoryNl: 'Mexicaanse Keuken', gi: 52, ii: 65, nutrition: { calories: 380, protein: 20, carbs: 48, fat: 12, fiber: 5 } },
    { id: 160, name: 'كويساديلا بالجبنة الذائبة', nameEn: 'Cheese Quesadilla', nameNl: 'Quesadilla met gesmolten kaas', icon: '🫔', category: 'أطعمة مكسيكية', categoryNl: 'Mexicaanse Keuken', gi: 48, ii: 58, nutrition: { calories: 337, protein: 14, carbs: 32, fat: 17, fiber: 2.5 } },
    { id: 161, name: 'فاهيتا دجاج مع فلفل وبصل', nameEn: 'Chicken Fajitas', nameNl: 'Kip fajitas met paprika', icon: '🌮', category: 'أطعمة مكسيكية', categoryNl: 'Mexicaanse Keuken', gi: 45, ii: 58, nutrition: { calories: 290, protein: 24, carbs: 28, fat: 10, fiber: 4 } },
    { id: 162, name: 'ناتشوز مقرمش بالجبن', nameEn: 'Nachos with Cheese', nameNl: 'Nachos met kaassaus', icon: '🧀', category: 'أطعمة مكسيكية', categoryNl: 'Mexicaanse Keuken', gi: 55, ii: 60, nutrition: { calories: 346, protein: 9, carbs: 36, fat: 19, fiber: 3 } },
    { id: 163, name: 'جواكامولي (صلصة أفوكادو مكسيكية)', nameEn: 'Guacamole', nameNl: 'Verse guacamole', icon: '🥑', category: 'أطعمة مكسيكية', categoryNl: 'Mexicaanse Keuken', gi: 15, ii: 15, nutrition: { calories: 150, protein: 2, carbs: 9, fat: 14, fiber: 7 } },
    { id: 164, name: 'صلصة سالسا طماطم حارة', nameEn: 'Tomato Salsa', nameNl: 'Pikante tomatensalsa', icon: '🍅', category: 'أطعمة مكسيكية', categoryNl: 'Mexicaanse Keuken', gi: 15, ii: 20, nutrition: { calories: 36, protein: 1.5, carbs: 8, fat: 0.2, fiber: 2 } },
    { id: 165, name: 'تشيلي كون كارني (لحم وفاصوليا)', nameEn: 'Chili Con Carne', nameNl: 'Chili con carne', icon: '🍲', category: 'أطعمة مكسيكية', categoryNl: 'Mexicaanse Keuken', gi: 38, ii: 52, nutrition: { calories: 199, protein: 15, carbs: 18, fat: 8, fiber: 6.2 } },

    // === أطعمة إيطالية (Italiaanse Keuken) ===
    { id: 166, name: 'لازانيا باللحم والبشاميل', nameEn: 'Meat Lasagna', nameNl: 'Lasagne bolognese', icon: '🍝', category: 'أطعمة إيطالية', categoryNl: 'Italiaanse Keuken', gi: 55, ii: 65, nutrition: { calories: 195, protein: 11, carbs: 18, fat: 9, fiber: 2.2 } },
    { id: 167, name: 'سباغيتي كاربونارا', nameEn: 'Spaghetti Carbonara', nameNl: 'Spaghetti carbonara', icon: '🍝', category: 'أطعمة إيطالية', categoryNl: 'Italiaanse Keuken', gi: 52, ii: 65, nutrition: { calories: 384, protein: 17, carbs: 37, fat: 19, fiber: 2 } },
    { id: 168, name: 'سباغيتي بولونيز', nameEn: 'Spaghetti Bolognese', nameNl: 'Spaghetti bolognese', icon: '🍝', category: 'أطعمة إيطالية', categoryNl: 'Italiaanse Keuken', gi: 52, ii: 58, nutrition: { calories: 182, protein: 8, carbs: 27, fat: 5, fiber: 2.8 } },
    { id: 169, name: 'فيتوتشيني ألفريدو بالكريمة', nameEn: 'Fettuccine Alfredo', nameNl: 'Fettuccine alfredo', icon: '🍝', category: 'أطعمة إيطالية', categoryNl: 'Italiaanse Keuken', gi: 50, ii: 60, nutrition: { calories: 320, protein: 10, carbs: 38, fat: 14, fiber: 2 } },
    { id: 170, name: 'ريزوتو بالفطر وجبن البارميزان', nameEn: 'Mushroom Risotto', nameNl: 'Paddenstoelenrisotto', icon: '🍚', category: 'أطعمة إيطالية', categoryNl: 'Italiaanse Keuken', gi: 69, ii: 62, nutrition: { calories: 166, protein: 4.5, carbs: 26, fat: 5, fiber: 1.5 } },
    { id: 171, name: 'جنوكي البطاطا الإيطالي', nameEn: 'Potato Gnocchi', nameNl: 'Aardappelgnocchi', icon: '🍝', category: 'أطعمة إيطالية', categoryNl: 'Italiaanse Keuken', gi: 68, ii: 72, nutrition: { calories: 130, protein: 3.2, carbs: 28, fat: 0.5, fiber: 1.5 } },
    { id: 172, name: 'كالزوني (بيتزا مطوية محشية)', nameEn: 'Calzone Pizza', nameNl: 'Calzone pizza', icon: '🥙', category: 'أطعمة إيطالية', categoryNl: 'Italiaanse Keuken', gi: 58, ii: 68, nutrition: { calories: 364, protein: 16, carbs: 42, fat: 14, fiber: 2.8 } },
    { id: 173, name: 'بروسكيتا بالطماطم والريحان', nameEn: 'Bruschetta', nameNl: 'Bruschetta met tomaat en basilicum', icon: '🥖', category: 'أطعمة إيطالية', categoryNl: 'Italiaanse Keuken', gi: 55, ii: 58, nutrition: { calories: 143, protein: 4, carbs: 20, fat: 5, fiber: 2 } },
    { id: 174, name: 'سلطة كابريزي (موزاريلا وطماطم)', nameEn: 'Caprese Salad', nameNl: 'Caprese salade met mozzarella', icon: '🍅', category: 'أطعمة إيطالية', categoryNl: 'Italiaanse Keuken', gi: 15, ii: 35, nutrition: { calories: 150, protein: 8, carbs: 4, fat: 12, fiber: 1 } },
    { id: 175, name: 'شوربة مينيستروني الإيطالية', nameEn: 'Minestrone Soup', nameNl: 'Minestronesoep', icon: '🍲', category: 'أطعمة إيطالية', categoryNl: 'Italiaanse Keuken', gi: 39, ii: 45, nutrition: { calories: 82, protein: 3.8, carbs: 13, fat: 2, fiber: 3.2 } },

    // === أطعمة آسيوية وهندية (Aziatische Keuken) ===
    { id: 176, name: 'سوشي سلمون رول', nameEn: 'Salmon Sushi Roll', nameNl: 'Zalm sushi roll', icon: '🍣', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 52, ii: 55, nutrition: { calories: 180, protein: 9, carbs: 21, fat: 7, fiber: 1 } },
    { id: 177, name: 'سوشي كاليفورنيا رول', nameEn: 'California Roll', nameNl: 'California maki roll', icon: '🍣', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 55, ii: 58, nutrition: { calories: 140, protein: 6, carbs: 19, fat: 4.5, fiber: 1.5 } },
    { id: 178, name: 'ساشيمي سلمون نيء', nameEn: 'Salmon Sashimi', nameNl: 'Zalm sashimi (rauw)', icon: '🍣', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 0, ii: 59, nutrition: { calories: 127, protein: 20, carbs: 0, fat: 4.4, fiber: 0 } },
    { id: 179, name: 'شوربة رامن يابانية بالدجاج', nameEn: 'Chicken Ramen', nameNl: 'Kip ramen noedelsoep', icon: '🍜', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 55, ii: 62, nutrition: { calories: 436, protein: 13, carbs: 56, fat: 17, fiber: 2.8 } },
    { id: 180, name: 'نودلز باد تاي تايلاندي', nameEn: 'Pad Thai', nameNl: 'Pad Thai noedels', icon: '🍜', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 50, ii: 58, nutrition: { calories: 354, protein: 9, carbs: 41, fat: 16, fiber: 2.5 } },
    { id: 181, name: 'دجاج تيرياكي ياباني', nameEn: 'Chicken Teriyaki', nameNl: 'Kip teriyaki', icon: '🍗', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 45, ii: 52, nutrition: { calories: 240, protein: 28, carbs: 18, fat: 6, fiber: 1 } },
    { id: 182, name: 'دجاج كاتسو مقرمش', nameEn: 'Chicken Katsu', nameNl: 'Kip katsu', icon: '🍗', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 55, ii: 65, nutrition: { calories: 320, protein: 22, carbs: 28, fat: 14, fiber: 2 } },
    { id: 183, name: 'دمبلنج مطهو على البخار', nameEn: 'Dumplings (Gyoza)', nameNl: 'Gestoomde dumplings (Gyoza)', icon: '🥟', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 45, ii: 52, nutrition: { calories: 206, protein: 7.5, carbs: 23, fat: 9, fiber: 1.2 } },
    { id: 184, name: 'سبرنج رول خضار مقلي', nameEn: 'Spring Rolls', nameNl: 'Groente loempia', icon: '🥟', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 48, ii: 55, nutrition: { calories: 140, protein: 4, carbs: 19, fat: 5.5, fiber: 1.8 } },
    { id: 185, name: 'شوربة ميسو اليابانية', nameEn: 'Miso Soup', nameNl: 'Miso soep met zeewier', icon: '🍵', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 25, ii: 30, nutrition: { calories: 40, protein: 2.2, carbs: 5.5, fat: 1.2, fiber: 1 } },
    { id: 186, name: 'توفو صويا طبيعي', nameEn: 'Tofu', nameNl: 'Tofu (Naturel)', icon: '🧈', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 15, ii: 20, nutrition: { calories: 76, protein: 8, carbs: 1.9, fat: 4.8, fiber: 0.3 } },
    { id: 187, name: 'تمبيه مخمر (بروتين نباتي)', nameEn: 'Tempeh', nameNl: 'Tempeh', icon: '🫘', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 18, ii: 22, nutrition: { calories: 193, protein: 20, carbs: 7.6, fat: 11, fiber: 0 } },
    { id: 188, name: 'كيمتشي كوري حار ومخمر', nameEn: 'Kimchi', nameNl: 'Kimchi (gefermenteerde kool)', icon: '🥬', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 15, ii: 15, nutrition: { calories: 15, protein: 1.1, carbs: 2.4, fat: 0.5, fiber: 1.6 } },
    { id: 189, name: 'دجاج تكا ماسالا هندي', nameEn: 'Chicken Tikka Masala', nameNl: 'Kip Tikka Masala', icon: '🍛', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 45, ii: 58, nutrition: { calories: 204, protein: 14, carbs: 12, fat: 12, fiber: 2.5 } },
    { id: 190, name: 'بالاك بانير (سبانخ وجبن هندي)', nameEn: 'Palak Paneer', nameNl: 'Palak Paneer', icon: '🍛', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 30, ii: 48, nutrition: { calories: 220, protein: 12, carbs: 8, fat: 16, fiber: 3 } },
    { id: 191, name: 'برياني دجاج هندي متبل', nameEn: 'Chicken Biryani', nameNl: 'Kip biryani', icon: '🍚', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 58, ii: 70, nutrition: { calories: 356, protein: 16, carbs: 45, fat: 12, fiber: 2.2 } },
    { id: 192, name: 'خبز النان الهندي بالثوم', nameEn: 'Garlic Naan', nameNl: 'Knoflook naanbrood', icon: '🫓', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 71, ii: 65, nutrition: { calories: 262, protein: 7.9, carbs: 45, fat: 5.3, fiber: 2.1 } },
    { id: 193, name: 'شوربة دال عدس هندي', nameEn: 'Indian Dal', nameNl: 'Indiase dal soep', icon: '🍲', category: 'أطعمة آسيوية', categoryNl: 'Aziatische Keuken', gi: 32, ii: 50, nutrition: { calories: 104, protein: 7.6, carbs: 17, fat: 0.6, fiber: 6.7 } },

    // === المخبوزات والسندويشات (Bakkerij & Broodjes) ===
    { id: 194, name: 'باغيت فرنسي مقرمش', nameEn: 'French Baguette', nameNl: 'Frans stokbrood', icon: '🥖', category: 'مخبوزات', categoryNl: 'Bakkerij', gi: 75, ii: 95, nutrition: { calories: 272, protein: 9, carbs: 55, fat: 1.6, fiber: 3 } },
    { id: 195, name: 'خبز التورتيلا المكسيكي', nameEn: 'Tortilla Wrap', nameNl: 'Tortilla wrap', icon: '🌮', category: 'مخبوزات', categoryNl: 'Bakkerij', gi: 52, ii: 55, nutrition: { calories: 218, protein: 5.7, carbs: 36, fat: 5.6, fiber: 2.3 } },
    { id: 196, name: 'خبز البيتا العربي', nameEn: 'Pita Bread', nameNl: 'Pitabroodje', icon: '🫓', category: 'مخبوزات', categoryNl: 'Bakkerij', gi: 68, ii: 57, nutrition: { calories: 275, protein: 9.1, carbs: 55, fat: 1.2, fiber: 2.2 } },
    { id: 197, name: 'فطيرة سبانخ شامية', nameEn: 'Spinach Pie', nameNl: 'Spinazie pasteitje', icon: '🥟', category: 'مخبوزات', categoryNl: 'Bakkerij', gi: 52, ii: 58, nutrition: { calories: 235, protein: 6, carbs: 26, fat: 12, fiber: 2.1 } },
    { id: 198, name: 'فطيرة جبنة بلدية', nameEn: 'Cheese Pie', nameNl: 'Kaas pasteitje', icon: '🥟', category: 'مخبوزات', categoryNl: 'Bakkerij', gi: 50, ii: 65, nutrition: { calories: 312, protein: 12, carbs: 28, fat: 17, fiber: 1.5 } },
    { id: 199, name: 'لحم بعجين صفيحة شامية', nameEn: 'Lahmacun (Meat Sfiha)', nameNl: 'Lahmacun (Turkse pizza)', icon: '🫓', category: 'مخبوزات', categoryNl: 'Bakkerij', gi: 62, ii: 68, nutrition: { calories: 285, protein: 14, carbs: 32, fat: 11, fiber: 2.5 } },
    { id: 200, name: 'مناقيش زعتر بلدي بزيت الزيتون', nameEn: 'Zaatar Manakeesh', nameNl: 'Za\'atar manakish', icon: '🫓', category: 'مخبوزات', categoryNl: 'Bakkerij', gi: 58, ii: 62, nutrition: { calories: 268, protein: 7, carbs: 40, fat: 9, fiber: 3 } },
    { id: 201, name: 'مناقيش جبنة عكاوي', nameEn: 'Cheese Manakeesh', nameNl: 'Kaas manakish', icon: '🫓', category: 'مخبوزات', categoryNl: 'Bakkerij', gi: 55, ii: 70, nutrition: { calories: 312, protein: 13, carbs: 38, fat: 12, fiber: 2.2 } },
    { id: 202, name: 'سمبوسك باللحمة المفرومة', nameEn: 'Meat Sambousek', nameNl: 'Vlees samosa / sambousek', icon: '🥟', category: 'مخبوزات', categoryNl: 'Bakkerij', gi: 58, ii: 65, nutrition: { calories: 295, protein: 10, carbs: 26, fat: 17, fiber: 2 } },
    { id: 203, name: 'ساندويش كلوب حبش وجبن', nameEn: 'Club Sandwich', nameNl: 'Club sandwich kip & kaas', icon: '🥪', category: 'سندويشات', categoryNl: 'Broodjes', gi: 55, ii: 65, nutrition: { calories: 390, protein: 24, carbs: 36, fat: 16, fiber: 3 } },
    { id: 204, name: 'ساندويش تونة بالمايونيز والخس', nameEn: 'Tuna Sandwich', nameNl: 'Broodje tonijnsalade', icon: '🥪', category: 'سندويشات', categoryNl: 'Broodjes', gi: 52, ii: 58, nutrition: { calories: 287, protein: 16, carbs: 29, fat: 12, fiber: 2.5 } },
    { id: 205, name: 'بانيني حلومي مشوي وطماطم', nameEn: 'Grilled Halloumi Panini', nameNl: 'Panini gegrilde halloumi', icon: '🥪', category: 'سندويشات', categoryNl: 'Broodjes', gi: 42, ii: 55, nutrition: { calories: 345, protein: 16, carbs: 32, fat: 18, fiber: 3 } },
    { id: 206, name: 'توست أفوكادو مع بيض مسلوق', nameEn: 'Avocado Toast with Egg', nameNl: 'Avocado toast met ei', icon: '🥑', category: 'سندويشات', categoryNl: 'Broodjes', gi: 40, ii: 45, nutrition: { calories: 235, protein: 10, carbs: 23, fat: 13, fiber: 7 } },

    // === الشوربات والوجبات المنزلية (Soepen & Maaltijden) ===
    { id: 207, name: 'شوربة خضار مشكلة طازجة', nameEn: 'Vegetable Soup', nameNl: 'Verse groentesoep', icon: '🍲', category: 'وجبات منزلية', categoryNl: 'Huisgemaakte Maaltijden', gi: 30, ii: 35, nutrition: { calories: 67, protein: 2.4, carbs: 12, fat: 1.5, fiber: 2.5 } },
    { id: 208, name: 'شوربة دجاج بالشعيرية', nameEn: 'Chicken Noodle Soup', nameNl: 'Kippensoep met vermicelli', icon: '🍲', category: 'وجبات منزلية', categoryNl: 'Huisgemaakte Maaltijden', gi: 35, ii: 48, nutrition: { calories: 86, protein: 6.7, carbs: 8.5, fat: 2.9, fiber: 0.6 } },
    { id: 209, name: 'شوربة قرع عسلي بالكريمة', nameEn: 'Pumpkin Soup', nameNl: 'Romige pompoensoep', icon: '🍲', category: 'وجبات منزلية', categoryNl: 'Huisgemaakte Maaltijden', gi: 51, ii: 48, nutrition: { calories: 71, protein: 1.8, carbs: 12, fat: 2.2, fiber: 1.9 } },
    { id: 210, name: 'شوربة بروكلي كريمية', nameEn: 'Broccoli Soup', nameNl: 'Romige broccolisoep', icon: '🍲', category: 'وجبات منزلية', categoryNl: 'Huisgemaakte Maaltijden', gi: 25, ii: 32, nutrition: { calories: 89, protein: 4.5, carbs: 10, fat: 4, fiber: 2.8 } },
    { id: 211, name: 'شوربة الفطر البري بالكريمة', nameEn: 'Mushroom Cream Soup', nameNl: 'Romige champignonsoep', icon: '🍲', category: 'وجبات منزلية', categoryNl: 'Huisgemaakte Maaltijden', gi: 30, ii: 35, nutrition: { calories: 85, protein: 2.8, carbs: 9, fat: 4.8, fiber: 1.2 } },
    { id: 212, name: 'شوربة طماطم إيطالية محمصة', nameEn: 'Roasted Tomato Soup', nameNl: 'Geroosterde tomatensoep', icon: '🍲', category: 'وجبات منزلية', categoryNl: 'Huisgemaakte Maaltijden', gi: 38, ii: 45, nutrition: { calories: 74, protein: 2, carbs: 16, fat: 0.7, fiber: 1.5 } },
    { id: 213, name: 'شوربة فريكة باللحم', nameEn: 'Freekeh Soup with Meat', nameNl: 'Freekeh soep met vlees', icon: '🍲', category: 'وجبات منزلية', categoryNl: 'Huisgemaakte Maaltijden', gi: 42, ii: 48, nutrition: { calories: 165, protein: 9, carbs: 24, fat: 4, fiber: 6 } },
    { id: 214, name: 'مسقعة باذنجان باللحمة المفرومة', nameEn: 'Eggplant Moussaka', nameNl: 'Moussaka met rundergehakt', icon: '🍆', category: 'وجبات منزلية', categoryNl: 'Huisgemaakte Maaltijden', gi: 42, ii: 52, nutrition: { calories: 189, protein: 12, carbs: 15, fat: 10, fiber: 3.5 } },
    { id: 215, name: 'يخنة بامية باللحم والأرز', nameEn: 'Okra Stew with Meat', nameNl: 'Okra stoofpot met vlees', icon: '🫛', category: 'وجبات منزلية', categoryNl: 'Huisgemaakte Maaltijden', gi: 35, ii: 50, nutrition: { calories: 156, protein: 14, carbs: 10, fat: 7, fiber: 3.8 } },
    { id: 216, name: 'يخنة فاصوليا خضراء باللحم', nameEn: 'Green Bean Stew', nameNl: 'Sperziebonen stoofpot met vlees', icon: '🫛', category: 'وجبات منزلية', categoryNl: 'Huisgemaakte Maaltijden', gi: 30, ii: 48, nutrition: { calories: 142, protein: 12, carbs: 9, fat: 6.5, fiber: 3.2 } },
    { id: 217, name: 'مفركة بطاطا بالبيض (شامية)', nameEn: 'Potato & Egg Hash (Mfarakah)', nameNl: 'Aardappel roerbak met ei', icon: '🥔', category: 'وجبات منزلية', categoryNl: 'Huisgemaakte Maaltijden', gi: 55, ii: 60, nutrition: { calories: 225, protein: 7, carbs: 28, fat: 10, fiber: 4 } },
    { id: 218, name: 'أرز بالشعيرية ومطبوخ بالسمن', nameEn: 'Rice with Vermicelli', nameNl: 'Rijst met vermicelli', icon: '🍚', category: 'وجبات منزلية', categoryNl: 'Huisgemaakte Maaltijden', gi: 65, ii: 68, nutrition: { calories: 158, protein: 3.2, carbs: 30, fat: 2.5, fiber: 0.9 } },
    { id: 219, name: 'معكرونة بصلصة البشاميل واللحم', nameEn: 'Baked Pasta Bechamel', nameNl: 'Ovenschotel pasta bechamel', icon: '🍝', category: 'وجبات منزلية', categoryNl: 'Huisgemaakte Maaltijden', gi: 58, ii: 70, nutrition: { calories: 245, protein: 14, carbs: 24, fat: 11, fiber: 1.8 } },
    { id: 220, name: 'كفتة داوود باشا بصلصة البندورة', nameEn: 'Dawood Basha Meatballs', nameNl: 'Gehaktballetjes in tomatensaus', icon: '🧆', category: 'وجبات منزلية', categoryNl: 'Huisgemaakte Maaltijden', gi: 42, ii: 65, nutrition: { calories: 285, protein: 18, carbs: 15, fat: 18, fiber: 3 } },

    // === السلطات المتخصصة (Gezonde Salades) ===
    { id: 221, name: 'سلطة سيزر بالدجاج المشوي', nameEn: 'Chicken Caesar Salad', nameNl: 'Caesarsalade met kip', icon: '🥗', category: 'سلطات', categoryNl: 'Salades', gi: 20, ii: 45, nutrition: { calories: 234, protein: 22, carbs: 8, fat: 14, fiber: 2.5 } },
    { id: 222, name: 'سلطة يونانية بجبن الفيتا والزيتون', nameEn: 'Greek Salad with Feta', nameNl: 'Griekse salade met fetakaas', icon: '🥗', category: 'سلطات', categoryNl: 'Salades', gi: 15, ii: 20, nutrition: { calories: 106, protein: 3.2, carbs: 7, fat: 8, fiber: 2.2 } },
    { id: 223, name: 'سلطة كينوا بالأفوكادو والخضار', nameEn: 'Quinoa Avocado Salad', nameNl: 'Quinoasalade met avocado', icon: '🥗', category: 'سلطات', categoryNl: 'Salades', gi: 53, ii: 50, nutrition: { calories: 172, protein: 6.3, carbs: 25, fat: 5.5, fiber: 4 } },
    { id: 224, name: 'سلطة جرجير بالرمان والجوز', nameEn: 'Arugula Walnut Salad', nameNl: 'Rucolasalade met walnoten', icon: '🥗', category: 'سلطات', categoryNl: 'Salades', gi: 15, ii: 15, nutrition: { calories: 95, protein: 3, carbs: 6, fat: 7, fiber: 2.5 } },
    { id: 225, name: 'سلطة بطاطا مسلوقة بالبقدونس', nameEn: 'Potato Herb Salad', nameNl: 'Aardappelsalade met peterselie', icon: '🥗', category: 'سلطات', categoryNl: 'Salades', gi: 56, ii: 62, nutrition: { calories: 143, protein: 2.6, carbs: 17, fat: 7.5, fiber: 1.6 } },
    { id: 226, name: 'سلطة شمندر مسلوق بالليمون', nameEn: 'Beetroot Salad', nameNl: 'Bietensalade met citroen', icon: '🥗', category: 'سلطات', categoryNl: 'Salades', gi: 64, ii: 48, nutrition: { calories: 75, protein: 2.3, carbs: 13, fat: 2, fiber: 3 } },
    { id: 227, name: 'سلطة تونة بالذرة والمايونيز الخفيف', nameEn: 'Tuna Corn Salad', nameNl: 'Tonijnsalade met maïs', icon: '🥗', category: 'سلطات', categoryNl: 'Salades', gi: 15, ii: 35, nutrition: { calories: 187, protein: 16, carbs: 3, fat: 13, fiber: 0.8 } },

    // === فواكه استوائية ومجففة نادرة (Tropisch & Gedroogd Fruit) ===
    { id: 228, name: 'دراغون فروت (فاكهة التنين)', nameEn: 'Dragon Fruit (Pitaya)', nameNl: 'Drakenvrucht (Pitaya)', icon: '🐉', category: 'فواكه', categoryNl: 'Fruit', gi: 48, ii: 40, nutrition: { calories: 60, protein: 1.2, carbs: 13, fat: 0.4, fiber: 3 } },
    { id: 229, name: 'باشن فروت (ماراكوجا)', nameEn: 'Passion Fruit', nameNl: 'Passievrucht', icon: '🥭', category: 'فواكه', categoryNl: 'Fruit', gi: 30, ii: 35, nutrition: { calories: 97, protein: 2.2, carbs: 23.4, fat: 0.7, fiber: 10.4 } },
    { id: 230, name: 'ليتشي استوائي', nameEn: 'Lychee', nameNl: 'Lychee', icon: '🍒', category: 'فواكه', categoryNl: 'Fruit', gi: 50, ii: 45, nutrition: { calories: 66, protein: 0.8, carbs: 16.5, fat: 0.4, fiber: 1.3 } },
    { id: 231, name: 'تين شوكي (صبار)', nameEn: 'Prickly Pear', nameNl: 'Cactusvijg', icon: '🌵', category: 'فواكه', categoryNl: 'Fruit', gi: 45, ii: 50, nutrition: { calories: 41, protein: 0.7, carbs: 9.6, fat: 0.5, fiber: 3.6 } },
    { id: 232, name: 'مشمش مجفف طبيعي', nameEn: 'Dried Apricots', nameNl: 'Gedroogde abrikozen', icon: '🍑', category: 'فواكه', categoryNl: 'Fruit', gi: 30, ii: 42, nutrition: { calories: 241, protein: 3.4, carbs: 63, fat: 0.5, fiber: 7.3 } },
    { id: 233, name: 'تين مجفف بلدي', nameEn: 'Dried Figs', nameNl: 'Gedroogde vijgen', icon: '🍇', category: 'فواكه', categoryNl: 'Fruit', gi: 61, ii: 58, nutrition: { calories: 249, protein: 3.3, carbs: 64, fat: 0.9, fiber: 9.8 } },
    { id: 234, name: 'برقوق مجفف (قراصيا)', nameEn: 'Prunes', nameNl: 'Gedroogde pruimen', icon: '🍑', category: 'فواكه', categoryNl: 'Fruit', gi: 29, ii: 38, nutrition: { calories: 240, protein: 2.2, carbs: 64, fat: 0.4, fiber: 7.1 } },
    { id: 235, name: 'توت غوجي بيري مجفف', nameEn: 'Goji Berry', nameNl: 'Goji bessen', icon: '🫐', category: 'فواكه', categoryNl: 'Fruit', gi: 29, ii: 35, nutrition: { calories: 349, protein: 14.3, carbs: 77.1, fat: 0.4, fiber: 13 } },

    // === الأعشاب والتوابل الطبية (Specerijen & Kruiden) ===
    { id: 236, name: 'كركم طازج مبشور', nameEn: 'Fresh Turmeric', nameNl: 'Verse kurkuma', icon: '🟡', category: 'بهارات', categoryNl: 'Specerijen', gi: 15, ii: 10, nutrition: { calories: 312, protein: 9.7, carbs: 67.1, fat: 3.3, fiber: 22.7 } },
    { id: 237, name: 'زنجبيل طازج', nameEn: 'Fresh Ginger', nameNl: 'Verse gember', icon: '🟤', category: 'بهارات', categoryNl: 'Specerijen', gi: 15, ii: 12, nutrition: { calories: 80, protein: 1.8, carbs: 17.8, fat: 0.8, fiber: 2 } },
    { id: 238, name: 'قرفة سيلانية حقيقية', nameEn: 'Ceylon Cinnamon', nameNl: 'Ceylon kaneel', icon: '🟫', category: 'بهارات', categoryNl: 'Specerijen', gi: 5, ii: 5, nutrition: { calories: 247, protein: 4, carbs: 80.6, fat: 1.2, fiber: 53.1 } },
    { id: 239, name: 'هيل أخضر حب', nameEn: 'Green Cardamom', nameNl: 'Groene kardemom', icon: '💚', category: 'بهارات', categoryNl: 'Specerijen', gi: 10, ii: 8, nutrition: { calories: 311, protein: 10.8, carbs: 68.5, fat: 6.7, fiber: 28 } },
    { id: 240, name: 'زعفران نقي', nameEn: 'Saffron', nameNl: 'Saffraan', icon: '🟡', category: 'بهارات', categoryNl: 'Specerijen', gi: 5, ii: 5, nutrition: { calories: 310, protein: 11.4, carbs: 65.4, fat: 5.9, fiber: 3.9 } },
    { id: 241, name: 'زعتر بري مجفف (أوريجانو)', nameEn: 'Dried Wild Thyme', nameNl: 'Wilde tijm (Oregano)', icon: '🌿', category: 'بهارات', categoryNl: 'Specerijen', gi: 10, ii: 8, nutrition: { calories: 276, protein: 9.1, carbs: 63.9, fat: 7.4, fiber: 37 } },

    // === المكملات والبدائل الصحية (Supplementen & Gezond) ===
    { id: 242, name: 'سبيرولينا عضوية بودرة', nameEn: 'Spirulina Powder', nameNl: 'Spirulina poeder', icon: '🌾', category: 'مكملات', categoryNl: 'Supplementen', gi: 15, ii: 18, nutrition: { calories: 290, protein: 57, carbs: 24, fat: 8, fiber: 3.6 } },
    { id: 243, name: 'بروتين مصل اللبن (واي آيسوليت)', nameEn: 'Whey Protein Isolate', nameNl: 'Whey proteïne isolaat', icon: '🥛', category: 'مكملات', categoryNl: 'Supplementen', gi: 15, ii: 35, nutrition: { calories: 385, protein: 82, carbs: 7, fat: 5, fiber: 0 } },
    { id: 244, name: 'طحين اللوز الخالي من الغلوتين', nameEn: 'Almond Flour', nameNl: 'Amandelmeel glutenvrij', icon: '🌰', category: 'مكملات', categoryNl: 'Supplementen', gi: 0, ii: 10, nutrition: { calories: 571, protein: 21, carbs: 21, fat: 50, fiber: 11 } },
    { id: 245, name: 'طحين جوز الهند العضوي', nameEn: 'Coconut Flour', nameNl: 'Kokosmeel biologisch', icon: '🥥', category: 'مكملات', categoryNl: 'Supplementen', gi: 45, ii: 48, nutrition: { calories: 400, protein: 20, carbs: 60, fat: 13, fiber: 40 } },

    // === المشروبات التقليدية الصحية (Traditionele Gezonde Dranken) ===
    { id: 246, name: 'شراب التمر هندي الطبيعي', nameEn: 'Tamarind Drink', nameNl: 'Tamarinde drank', icon: '🥤', category: 'مشروبات', categoryNl: 'Dranken', gi: 40, ii: 48, nutrition: { calories: 58, protein: 0.3, carbs: 15, fat: 0.1, fiber: 0.5 } },
    { id: 247, name: 'عصير خروب بلدي طبيعي', nameEn: 'Carob Drink', nameNl: 'Johannesbrood drank (Carob)', icon: '🥤', category: 'مشروبات', categoryNl: 'Dranken', gi: 40, ii: 45, nutrition: { calories: 62, protein: 0.4, carbs: 16, fat: 0.1, fiber: 0.7 } },
    { id: 248, name: 'سحلب ساخن بالقرفة والمكسرات', nameEn: 'Sahlab Drink', nameNl: 'Sahlab warme melkdrank', icon: '🥛', category: 'مشروبات', categoryNl: 'Dranken', gi: 55, ii: 60, nutrition: { calories: 145, protein: 4, carbs: 22, fat: 4.5, fiber: 0.5 } },
    { id: 249, name: 'قهوة عربية شقراء بالهيل', nameEn: 'Arabic Coffee with Cardamom', nameNl: 'Arabische koffie met kardemom', icon: '☕', category: 'مشروبات', categoryNl: 'Dranken', gi: 0, ii: 15, nutrition: { calories: 2, protein: 0.3, carbs: 0, fat: 0, fiber: 0 } },
    { id: 250, name: 'شاي كرك بالحليب والتوابل', nameEn: 'Karak Tea', nameNl: 'Karak chai met specerijen', icon: '🍵', category: 'مشروبات', categoryNl: 'Dranken', gi: 50, ii: 60, nutrition: { calories: 78, protein: 1.8, carbs: 14, fat: 2, fiber: 0 } },
// === فواكه استوائية ونادرة (Exotisch Fruit) ===
    { id: 251, name: 'رامبوتان استوائي', nameEn: 'Rambutan', nameNl: 'Rambutan', icon: '🍒', category: 'فواكه', categoryNl: 'Fruit', gi: 50, ii: 45, nutrition: { calories: 82, protein: 0.7, carbs: 20.9, fat: 0.2, fiber: 0.9 } },
    { id: 252, name: 'كمكوات (برتقال ياباني صغير)', nameEn: 'Kumquat', nameNl: 'Kumquat', icon: '🍊', category: 'فواكه', categoryNl: 'Fruit', gi: 30, ii: 32, nutrition: { calories: 71, protein: 1.9, carbs: 15.9, fat: 0.9, fiber: 6.5 } },
    { id: 253, name: 'دوريان استوائي', nameEn: 'Durian', nameNl: 'Doerian', icon: '🥥', category: 'فواكه', categoryNl: 'Fruit', gi: 49, ii: 45, nutrition: { calories: 147, protein: 1.5, carbs: 27.1, fat: 5.3, fiber: 3.8 } },
    { id: 254, name: 'فاكهة النجمة (كرامبولا)', nameEn: 'Star Fruit', nameNl: 'Carambola (Stervrucht)', icon: '⭐', category: 'فواكه', categoryNl: 'Fruit', gi: 45, ii: 40, nutrition: { calories: 31, protein: 1, carbs: 6.7, fat: 0.3, fiber: 2.8 } },
    { id: 255, name: 'جاك فروت (خبزية)', nameEn: 'Jackfruit', nameNl: 'Jackfruit', icon: '🍈', category: 'فواكه', categoryNl: 'Fruit', gi: 75, ii: 80, nutrition: { calories: 95, protein: 1.7, carbs: 23.2, fat: 0.6, fiber: 1.5 } },
    { id: 256, name: 'مانجوستين ملكي', nameEn: 'Mangosteen', nameNl: 'Mangistan', icon: '💜', category: 'فواكه', categoryNl: 'Fruit', gi: 46, ii: 52, nutrition: { calories: 73, protein: 0.4, carbs: 17.9, fat: 0.6, fiber: 1.8 } },
    { id: 257, name: 'خرما (كاكا طازجة)', nameEn: 'Persimmon (Kaki)', nameNl: 'Kaki fruit', icon: '🟠', category: 'فواكه', categoryNl: 'Fruit', gi: 50, ii: 55, nutrition: { calories: 70, protein: 0.6, carbs: 18.6, fat: 0.2, fiber: 3.6 } },
    { id: 258, name: 'إسكدنيا (أكي دنيا)', nameEn: 'Loquat', nameNl: 'Mispel (Loquat)', icon: '🍊', category: 'فواكه', categoryNl: 'Fruit', gi: 55, ii: 58, nutrition: { calories: 47, protein: 0.4, carbs: 12.1, fat: 0.2, fiber: 1.7 } },
    { id: 259, name: 'كيوانو (خيار مقرن أفريقي)', nameEn: 'Kiwano', nameNl: 'Kiwano (Gehoornde meloen)', icon: '🥒', category: 'فواكه', categoryNl: 'Fruit', gi: 25, ii: 30, nutrition: { calories: 44, protein: 1.8, carbs: 7.6, fat: 1.3, fiber: 0.5 } },
    { id: 260, name: 'توت الأكاي المركز', nameEn: 'Acai Berry', nameNl: 'Açaí bessen', icon: '🫐', category: 'فواكه', categoryNl: 'Fruit', gi: 42, ii: 45, nutrition: { calories: 70, protein: 1, carbs: 4, fat: 5, fiber: 2 } },

    // === خضروات وجذور إضافية (Groenten & Wortels) ===
    { id: 261, name: 'كحلبي (لفت ألماني)', nameEn: 'Kohlrabi', nameNl: 'Koolrabi', icon: '🥔', category: 'خضروات', categoryNl: 'Groenten', gi: 15, ii: 22, nutrition: { calories: 27, protein: 1.7, carbs: 6.2, fat: 0.1, fiber: 3.6 } },
    { id: 262, name: 'كراث بلدي (كرات)', nameEn: 'Leeks', nameNl: 'Prei', icon: '🧅', category: 'خضروات', categoryNl: 'Groenten', gi: 15, ii: 22, nutrition: { calories: 61, protein: 1.5, carbs: 14.2, fat: 0.3, fiber: 1.8 } },
    { id: 263, name: 'ملفوف بنفسجي أحمر', nameEn: 'Red Cabbage', nameNl: 'Rode kool', icon: '🥬', category: 'خضروات', categoryNl: 'Groenten', gi: 10, ii: 18, nutrition: { calories: 31, protein: 1.4, carbs: 7.4, fat: 0.2, fiber: 2.1 } },
    { id: 264, name: 'فجل أحمر مقرمش', nameEn: 'Red Radish', nameNl: 'Rode radijs', icon: '🥕', category: 'خضروات', categoryNl: 'Groenten', gi: 15, ii: 18, nutrition: { calories: 16, protein: 0.7, carbs: 3.4, fat: 0.1, fiber: 1.6 } },
    { id: 265, name: 'خبيزة برية مطبوخة بزيت الزيتون', nameEn: 'Khubeza (Mallow)', nameNl: 'Kaasjeskruid (Khubeza)', icon: '🥬', category: 'خضروات', categoryNl: 'Groenten', gi: 15, ii: 18, nutrition: { calories: 29, protein: 3.7, carbs: 5.4, fat: 0.3, fiber: 2.8 } },
    { id: 266, name: 'قرنبيط مقلي مقرمش بالكمون', nameEn: 'Fried Cauliflower', nameNl: 'Gebakken bloemkool met komijn', icon: '🥦', category: 'خضروات', categoryNl: 'Groenten', gi: 35, ii: 42, nutrition: { calories: 195, protein: 4, carbs: 12, fat: 15, fiber: 3.5 } },

    // === توابل وبهارات طبية (Geneeskrachtige Kruiden) ===
    { id: 267, name: 'قرنفل مسامير حب', nameEn: 'Cloves', nameNl: 'Kruidnagel', icon: '🟤', category: 'بهارات', categoryNl: 'Specerijen', gi: 10, ii: 8, nutrition: { calories: 274, protein: 6, carbs: 65.5, fat: 13, fiber: 33.9 } },
    { id: 268, name: 'جوزة الطيب مبشورة', nameEn: 'Nutmeg', nameNl: 'Nootmuskaat', icon: '🟫', category: 'بهارات', categoryNl: 'Specerijen', gi: 10, ii: 8, nutrition: { calories: 525, protein: 5.8, carbs: 49.3, fat: 36.3, fiber: 20.8 } },
    { id: 269, name: 'إكليل الجبل (روزماري مجفف)', nameEn: 'Dried Rosemary', nameNl: 'Gedroogde rozemarijn', icon: '🌿', category: 'بهارات', categoryNl: 'Specerijen', gi: 10, ii: 8, nutrition: { calories: 331, protein: 4.9, carbs: 64.1, fat: 15.2, fiber: 42.6 } },
    { id: 270, name: 'ريحان مجفف بلدي', nameEn: 'Dried Basil', nameNl: 'Gedroogde basilicum', icon: '🌿', category: 'بهارات', categoryNl: 'Specerijen', gi: 10, ii: 8, nutrition: { calories: 233, protein: 22.9, carbs: 47.8, fat: 4, fiber: 37.7 } },
    { id: 271, name: 'حبة البركة (الحبة السوداء)', nameEn: 'Black Seed (Nigella)', nameNl: 'Nigellazaad (Zwarte komijn)', icon: '🖤', category: 'بهارات', categoryNl: 'Specerijen', gi: 10, ii: 8, nutrition: { calories: 345, protein: 16, carbs: 52, fat: 15, fiber: 8 } },
    { id: 272, name: 'سماق بلدي حامض', nameEn: 'Sumac', nameNl: 'Sumak poeder', icon: '🔴', category: 'بهارات', categoryNl: 'Specerijen', gi: 10, ii: 8, nutrition: { calories: 240, protein: 3.5, carbs: 40, fat: 7, fiber: 14 } },

    // === أسماك ومأكولات بحرية إضافية (Extra Zeevruchten) ===
    { id: 273, name: 'سمك البلطي الطازج المشوي', nameEn: 'Tilapia', nameNl: 'Tilapiafilet', icon: '🐟', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 59, nutrition: { calories: 96, protein: 20.1, carbs: 0, fat: 1.7, fiber: 0 } },
    { id: 274, name: 'سمك الهامور الفاخر', nameEn: 'Grouper Fish', nameNl: 'Tandbaars filet (Grouper)', icon: '🐟', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 59, nutrition: { calories: 92, protein: 19.4, carbs: 0, fat: 1, fiber: 0 } },
    { id: 275, name: 'أخطبوط مشوي بالزيت والليمون', nameEn: 'Grilled Octopus', nameNl: 'Gegrilde octopus', icon: '🐙', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 60, nutrition: { calories: 82, protein: 14.9, carbs: 2.2, fat: 1, fiber: 0 } },
    { id: 276, name: 'حبار مقلي (كاليماري مقرمش)', nameEn: 'Fried Calamari', nameNl: 'Gefrituurde inktvisringen', icon: '🦑', category: 'بروتين', categoryNl: 'Eiwitten', gi: 15, ii: 50, nutrition: { calories: 175, protein: 15, carbs: 8, fat: 9.5, fiber: 0.5 } },
    { id: 277, name: 'كافيار سمك أصلي فخم', nameEn: 'Black Caviar', nameNl: 'Zwarte kaviaar', icon: '🥚', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 30, nutrition: { calories: 264, protein: 24.6, carbs: 4, fat: 17.9, fiber: 0 } },
    { id: 278, name: 'سمك أنشوفة مملح (Ansjovis)', nameEn: 'Anchovies', nameNl: 'Ansjovis in olijfolie', icon: '🐟', category: 'بروتين', categoryNl: 'Eiwitten', gi: 0, ii: 59, nutrition: { calories: 131, protein: 20.4, carbs: 0, fat: 4.8, fiber: 0 } },

    // === وجبات عربية خاصة ومميزة (Authentieke Gerechten) ===
    { id: 279, name: 'كبدة إسكندراني حارة بالفلفل', nameEn: 'Alexandrian Liver', nameNl: 'Pittige runderlever Alexandrië', icon: '🥩', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 0, ii: 68, nutrition: { calories: 195, protein: 22, carbs: 2.5, fat: 11, fiber: 0.5 } },
    { id: 280, name: 'فتة المكدوس باللحم واللبن', nameEn: 'Makdous Fatteh', nameNl: 'Makdous fatteh met aubergine', icon: '🍆', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 55, ii: 62, nutrition: { calories: 298, protein: 10, carbs: 28, fat: 17, fiber: 5 } },
    { id: 281, name: 'شاكرية لحم غنم باللبن والنشا', nameEn: 'Shakriyyeh (Lamb in Yogurt)', nameNl: 'Shakriyyeh (Lamsvlees in warme yoghurt)', icon: '🍲', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 52, ii: 68, nutrition: { calories: 289, protein: 20, carbs: 18, fat: 16, fiber: 1.2 } },
    { id: 282, name: 'جريش سعودي بالسمن والبصل', nameEn: 'Saudi Jareesh', nameNl: 'Saoedische Jareesh tarwepap', icon: '🍚', category: 'أطعمة عربية', categoryNl: 'Arabische Gerechten', gi: 50, ii: 48, nutrition: { calories: 185, protein: 8, carbs: 32, fat: 3, fiber: 4.5 } },
    { id: 283, name: 'عريكة ملكية بالتمر والعسل والسمن', nameEn: 'Areeka with Dates', nameNl: 'Areeka dadeldessert', icon: '🍯', category: 'حلويات', categoryNl: 'Desserts', gi: 75, ii: 78, nutrition: { calories: 425, protein: 6, carbs: 55, fat: 20, fiber: 2 } },

    // === مكملات وبدائل حمية الكيتو (Keto & Supplementen) ===
    { id: 284, name: 'خميرة غذائية مدعمة (Nutritional Yeast)', nameEn: 'Nutritional Yeast', nameNl: 'Edelgistvlokken (B-vitamines)', icon: '🌾', category: 'مكملات', categoryNl: 'Supplementen', gi: 10, ii: 15, nutrition: { calories: 340, protein: 50, carbs: 36, fat: 4, fiber: 20 } },
    { id: 285, name: 'خل تفاح عضوي غير مفلتر مع الأم', nameEn: 'Organic Apple Cider Vinegar', nameNl: 'Biologische appelazijn (ongefilterd)', icon: '🍎', category: 'مكملات', categoryNl: 'Supplementen', gi: 0, ii: 0, nutrition: { calories: 22, protein: 0, carbs: 0.9, fat: 0, fiber: 0 } },
    { id: 286, name: 'بروتين بار بنكهة الشوكولاتة والكراميل', nameEn: 'Chocolate Protein Bar', nameNl: 'Eiwitreep chocolade karamel', icon: '🍫', category: 'مكملات', categoryNl: 'Supplementen', gi: 35, ii: 42, nutrition: { calories: 200, protein: 20, carbs: 22, fat: 7, fiber: 3 } },
    { id: 287, name: 'خبز كيتو خالي من الجلوتين', nameEn: 'Gluten-Free Keto Bread', nameNl: 'Keto glutenvrij brood', icon: '🍞', category: 'مخبوزات', categoryNl: 'Bakkerij', gi: 25, ii: 30, nutrition: { calories: 210, protein: 12, carbs: 6, fat: 15, fiber: 9 } },
    { id: 288, name: 'معكرونة خالية من الجلوتين (أرز وذرة)', nameEn: 'Gluten-Free Pasta', nameNl: 'Glutenvrije pasta', icon: '🍝', category: 'حبوب', categoryNl: 'Granen', gi: 54, ii: 58, nutrition: { calories: 348, protein: 7, carbs: 76, fat: 2, fiber: 3.5 } },

    // === صلصات ومقبلات (Sauzen & Toppings) ===
    { id: 289, name: 'دبس رمان طبيعي مركز بدون سكر', nameEn: 'Pomegranate Molasses', nameNl: 'Granaatappelmelasse', icon: '🍇', category: 'صلصات', categoryNl: 'Sauzen', gi: 55, ii: 58, nutrition: { calories: 250, protein: 1, carbs: 65, fat: 0, fiber: 0 } },
    { id: 290, name: 'صلصة صويا مخمرة طبيعياً (Kikkoman)', nameEn: 'Naturally Brewed Soy Sauce', nameNl: 'Natuurlijk gebrouwen sojasaus', icon: '🥫', category: 'صلصات', categoryNl: 'Sauzen', gi: 15, ii: 15, nutrition: { calories: 53, protein: 5.6, carbs: 4.9, fat: 0.1, fiber: 0.8 } },
    { id: 291, name: 'صلصة سريراتشا حارة', nameEn: 'Sriracha Hot Sauce', nameNl: 'Sriracha hete chilisaus', icon: '🌶️', category: 'صلصات', categoryNl: 'Sauzen', gi: 35, ii: 40, nutrition: { calories: 93, protein: 2, carbs: 19, fat: 0.9, fiber: 1.5 } },
    { id: 292, name: 'مخلل خيار بلدي مقرمش', nameEn: 'Pickled Cucumbers (Gherkins)', nameNl: 'Augurken (zout/zuur)', icon: '🥒', category: 'صلصات', categoryNl: 'Sauzen', gi: 15, ii: 15, nutrition: { calories: 11, protein: 0.3, carbs: 2.3, fat: 0.2, fiber: 1.2 } },
    { id: 293, name: 'زيتون كلاماتا يوناني أسود', nameEn: 'Kalamata Olives', nameNl: 'Kalamata olijven', icon: '🫒', category: 'صلصات', categoryNl: 'Sauzen', gi: 15, ii: 10, nutrition: { calories: 115, protein: 0.8, carbs: 6.3, fat: 10.7, fiber: 3.2 } },

    // === مشروبات كحولية (لأغراض سريرية وتحذيرية صحية) ===
    { id: 294, name: 'بيرة عادية (Pilsener)', nameEn: 'Regular Beer', nameNl: 'Pilsener bier (alcohol)', icon: '🍺', category: 'مشروبات كحولية', categoryNl: 'Alcoholische Dranken', gi: 89, ii: 15, nutrition: { calories: 43, protein: 0.5, carbs: 3.6, fat: 0, fiber: 0 }, warning: '⚠️ يحتوي على كحول (5%). يرفع حمض اليوريك والدهون الثلاثية على الكبد.' },
    { id: 295, name: 'نبيذ أحمر جاف', nameEn: 'Dry Red Wine', nameNl: 'Droge rode wijn', icon: '🍷', category: 'مشروبات كحولية', categoryNl: 'Alcoholische Dranken', gi: 0, ii: 3, nutrition: { calories: 85, protein: 0.1, carbs: 2.6, fat: 0, fiber: 0 }, warning: '⚠️ يحتوي على كحول (13%). استهلاك الكحول يجهد إنزيمات الكبد ومسارات الحرق.' },
    { id: 296, name: 'مشروب عرق سوس بلدي طبيعي', nameEn: 'Licorice Drink', nameNl: 'Zoethout drank (Licorice)', icon: '🥤', category: 'مشروبات', categoryNl: 'Dranken', gi: 35, ii: 40, nutrition: { calories: 38, protein: 0.2, carbs: 10, fat: 0, fiber: 0.3 } },
    { id: 297, name: 'شاي كركديه بارد أحمر', nameEn: 'Hibiscus Iced Tea', nameNl: 'Hibiscusthee koud', icon: '🌺', category: 'مشروبات', categoryNl: 'Dranken', gi: 10, ii: 15, nutrition: { calories: 15, protein: 0.2, carbs: 3.5, fat: 0, fiber: 0.2 } },
    { id: 298, name: 'منقوع بابونج مهدئ للأعصاب', nameEn: 'Chamomile Tea', nameNl: 'Kamille thee kalmerend', icon: '🌼', category: 'مشروبات', categoryNl: 'Dranken', gi: 0, ii: 0, nutrition: { calories: 1, protein: 0, carbs: 0.2, fat: 0, fiber: 0 } },
    { id: 299, name: 'قهوة تركية بالهيل', nameEn: 'Turkish Coffee with Cardamom', nameNl: 'Turkse koffie met kardemom', icon: '☕', category: 'مشروبات', categoryNl: 'Dranken', gi: 0, ii: 5, nutrition: { calories: 2, protein: 0.1, carbs: 0.3, fat: 0, fiber: 0 } },
    { id: 300, name: 'شاي أخضر بالنعناع المغربي', nameEn: 'Moroccan Mint Green Tea', nameNl: 'Marokkaanse muntthee', icon: '🍵', category: 'مشروبات', categoryNl: 'Dranken', gi: 0, ii: 0, nutrition: { calories: 2, protein: 0.2, carbs: 0.4, fat: 0, fiber: 0 } }
];

/**
 * دالة لتحديد مستوى المؤشر السريري
 */
function getIndexLevel(value) {
    if (value <= 55) return 'low';
    if (value <= 69) return 'medium';
    return 'high';
}

/**
 * دالة للحصول على نص المستوى بـ 3 لغات (عربي - إنجليزي - هولندي)
 */
function getIndexLevelText(value, lang = 'ar') {
    if (lang === 'en') {
        if (value <= 55) return 'Low';
        if (value <= 69) return 'Medium';
        return 'High';
    } else if (lang === 'nl') {
        if (value <= 55) return 'Laag';
        if (value <= 69) return 'Gemiddeld';
        return 'Hoog';
    } else {
        if (value <= 55) return 'منخفض';
        if (value <= 69) return 'متوسط';
        return 'مرتفع';
    }
}

/**
 * دالة البحث الذكي بـ 3 لغات
 */
function filterFoodsBySearch(searchTerm) {
    if (!searchTerm || searchTerm.trim() === '') {
        return foodsDatabase;
    }
    
    const term = searchTerm.toLowerCase().trim();
    return foodsDatabase.filter(food => 
        (food.name && food.name.toLowerCase().includes(term)) ||
        (food.nameEn && food.nameEn.toLowerCase().includes(term)) ||
        (food.nameNl && food.nameNl.toLowerCase().includes(term)) ||
        (food.category && food.category.toLowerCase().includes(term)) ||
        (food.categoryNl && food.categoryNl.toLowerCase().includes(term))
    );
}

/**
 * دالة التصفية حسب الفئة
 */
function filterFoodsByCategory(category) {
    if (!category || category === 'all') {
        return foodsDatabase;
    }
    return foodsDatabase.filter(food => food.category === category || food.categoryNl === category);
}

/**
 * دالة جلب كافة التصنيفات دون تكرار
 */
function getCategories() {
    return [...new Set(foodsDatabase.map(food => food.category))];
}