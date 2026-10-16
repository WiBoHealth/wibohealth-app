"""Generate static, crawlable food pages (pilot batch) in three languages.

    python scripts/generate_food_pages.py

Output (re-running rebuilds everything, nothing is appended twice):
    foods/<slug>.html            Arabic (x-default)
    en/foods/<slug>.html         English
    nl/foods/<slug>.html         Dutch
    js/food-pages.js             id -> slug map used by foods.html / food-details.html
    sitemap.xml                  block between <!-- FOOD-PAGES:START --> and <!-- FOOD-PAGES:END -->

Sources: js/data.js (values, GI provenance), doctor.html (design system: CSS, logo, nav labels).
Per-food text can be overridden in scripts/food_pages_overrides.json (lead, tips, slug).
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://wibohealth.com'
REVIEWED = '2026-10-12'
REVIEWED_TXT = {'ar': '12 أكتوبر 2026', 'en': '12 October 2026', 'nl': '12 oktober 2026'}
TEAM_REVIEWED = '2026-10-13'             # batch 2: reviewed by the WiBo Health medical team
TEAM_REVIEWED_TXT = {'ar': '13 أكتوبر 2026', 'en': '13 October 2026', 'nl': '13 oktober 2026'}
LANGS = ('ar', 'en', 'nl')

# --------------------------------------------------------------------------------------------
# Pilot batch: id -> (group, typical portion in grams). Portions are approximate household
# servings pending Dr. Wassim's approval; they only drive the per-portion column and the GL.
# --------------------------------------------------------------------------------------------
PILOT = {
    # measured GI (Atkinson 2021)
    1: ('grain', 150), 14: ('grain', 150), 2: ('grain', 150), 3: ('grain', 50), 4: ('grain', 50), 196: ('grain', 60),
    5: ('grain', 150), 7: ('grain', 250), 17: ('grain', 30), 8: ('grain', 150), 9: ('grain', 150), 10: ('grain', 150),
    11: ('grain', 100), 26: ('tuber', 150), 27: ('tuber', 130), 29: ('tuber', 150), 18: ('legume', 150),
    19: ('legume', 150), 22: ('legume', 150), 48: ('fruit', 150), 49: ('fruit', 120), 50: ('fruit', 130),
    51: ('fruit', 280), 53: ('fruit', 120), 54: ('fruit', 150), 55: ('fruit', 150), 66: ('fruit', 170),
    62: ('dried', 70), 63: ('dried', 40), 68: ('dried', 40), 69: ('dairy_drink', 250), 70: ('dairy_drink', 250),
    79: ('dairy_drink', 250),
    # GI not applicable (< 5 g available carbohydrate / 100 g), high search interest
    101: ('protein', 50), 91: ('protein', 100), 92: ('protein', 100), 93: ('protein', 100), 94: ('protein', 100),
    98: ('protein', 100), 128: ('fat', 14), 59: ('fat', 75), 71: ('dairy_solid', 170), 72: ('dairy_solid', 30),
    74: ('dairy_solid', 30), 77: ('dairy_solid', 30), 30: ('veg', 120), 31: ('veg', 100), 32: ('veg', 120),
    35: ('veg', 90), 36: ('veg', 100), 37: ('veg', 80), 38: ('veg', 100), 39: ('veg', 100), 40: ('veg', 70),
    132: ('drink', 240), 133: ('drink', 240),
    # batch 2: GI is a clinically reviewed estimate (gi_status 'reviewed', not Atkinson-measured) or not applicable
    6: ('grain', 150), 12: ('grain', 50), 13: ('grain', 50), 15: ('grain', 150), 16: ('grain', 150),
    20: ('legume', 150), 21: ('legume', 150), 23: ('legume', 150), 24: ('legume', 100), 25: ('legume', 50),
    28: ('tuber', 100), 33: ('veg', 100), 34: ('veg', 80), 41: ('veg', 120), 42: ('veg', 90), 43: ('veg', 80),
    44: ('veg', 30), 45: ('veg', 50), 46: ('veg', 5), 47: ('veg', 100),
    52: ('fruit', 150), 56: ('fruit', 100), 57: ('fruit', 100), 58: ('fruit', 120), 60: ('fruit', 100),
    61: ('fruit', 100), 64: ('fruit', 75), 65: ('fruit', 150), 67: ('fruit', 150),
    73: ('dairy_solid', 30), 75: ('dairy_solid', 30), 76: ('dairy_solid', 100), 78: ('fat', 10),
    80: ('nuts', 30), 81: ('nuts', 30), 82: ('nuts', 30), 83: ('nuts', 30), 84: ('nuts', 30), 85: ('nuts', 15),
    86: ('nuts', 10), 87: ('nuts', 30), 88: ('nuts', 30), 89: ('nuts', 30), 90: ('nuts', 16),
    95: ('protein', 50), 96: ('protein', 120), 97: ('protein', 100), 99: ('protein', 90), 100: ('protein', 100),
    102: ('protein', 120),
    # batch 3: Arabic dishes, drinks, fast food and sweets (reviewed estimate or not applicable)
    103: ('protein', 100), 104: ('arabic', 60), 105: ('arabic', 50), 106: ('arabic', 150), 107: ('arabic', 60),
    108: ('arabic', 150), 109: ('arabic', 150), 110: ('arabic', 250), 111: ('arabic', 200), 112: ('arabic', 200),
    113: ('arabic', 150), 114: ('arabic', 120), 115: ('arabic', 80), 116: ('arabic', 100), 117: ('arabic', 100),
    118: ('arabic', 200), 119: ('arabic', 300), 120: ('arabic', 250), 121: ('arabic', 200), 122: ('arabic', 200),
    123: ('arabic', 250), 124: ('arabic', 200), 125: ('arabic', 200), 126: ('arabic', 250), 127: ('arabic', 300),
    129: ('fat', 10), 130: ('fat', 10), 131: ('fat', 15),
    134: ('drink', 240), 135: ('drink', 250), 136: ('dairy_drink', 250), 137: ('drink', 250), 138: ('drink', 200),
    139: ('drink', 200), 140: ('drink', 330),
    141: ('fastfood', 215), 142: ('fastfood', 100), 143: ('fastfood', 120), 144: ('fastfood', 100),
    145: ('fastfood', 100), 146: ('fastfood', 230), 147: ('fastfood', 100),
    148: ('sweets', 40), 149: ('sweets', 100), 150: ('sweets', 60), 151: ('sweets', 40), 152: ('sweets', 30),
    153: ('sweets', 150), 154: ('sweets', 150), 155: ('sweets', 20),
    # batch 4: world dishes, bakery and sandwiches (reviewed estimate or not applicable)
    156: ('sweets', 60), 157: ('sweets', 100), 158: ('mexican', 100), 159: ('mexican', 250), 160: ('mexican', 150),
    161: ('mexican', 250), 162: ('mexican', 100), 163: ('mexican', 50), 164: ('mexican', 50), 165: ('mexican', 250),
    166: ('italian', 250), 167: ('italian', 250), 168: ('italian', 300), 169: ('italian', 250),
    170: ('italian', 200), 171: ('italian', 200), 172: ('italian', 200), 173: ('italian', 60),
    174: ('italian', 150), 175: ('italian', 300), 176: ('asian', 180), 177: ('asian', 180), 178: ('asian', 100),
    179: ('asian', 500), 180: ('asian', 300), 181: ('asian', 200), 182: ('asian', 150), 183: ('asian', 150),
    184: ('asian', 60), 185: ('asian', 250), 186: ('asian', 150), 187: ('asian', 100), 188: ('asian', 50),
    189: ('asian', 250), 190: ('asian', 250), 191: ('asian', 300), 192: ('asian', 100), 193: ('asian', 250),
    194: ('bakery', 50), 195: ('bakery', 60), 197: ('bakery', 100), 198: ('bakery', 100), 199: ('bakery', 120),
    200: ('bakery', 100), 201: ('bakery', 100), 202: ('bakery', 60), 203: ('sandwich', 250), 204: ('sandwich', 200),
    205: ('sandwich', 150), 206: ('sandwich', 150),
    # batch 5: home-cooked dishes, salads and tropical fruit
    207: ('home', 250), 208: ('home', 250), 209: ('home', 250), 210: ('home', 250), 211: ('home', 250),
    212: ('home', 250), 213: ('home', 250), 214: ('home', 250), 215: ('home', 300), 216: ('home', 300),
    217: ('home', 200), 218: ('home', 150), 219: ('home', 250), 220: ('home', 250), 221: ('salad', 250),
    222: ('salad', 200), 223: ('salad', 200), 224: ('salad', 100), 225: ('salad', 150), 226: ('salad', 80),
    227: ('salad', 200), 228: ('fruit', 150), 229: ('fruit', 40), 230: ('fruit', 60), 231: ('fruit', 150),
    # batch 6: dried fruit, spices, special ingredients, traditional drinks and tropical fruit
    232: ('dried', 30), 233: ('dried', 40), 234: ('dried', 30), 235: ('dried', 20), 236: ('spice', 5), 237: ('spice', 5),
    238: ('spice', 2), 239: ('spice', 2), 240: ('spice', 1), 241: ('spice', 2), 242: ('pantry', 5), 243: ('pantry', 30),
    244: ('pantry', 30), 245: ('pantry', 20), 246: ('drink', 250), 247: ('drink', 250), 248: ('drink', 250),
    249: ('drink', 100), 250: ('drink', 200), 251: ('fruit', 100), 252: ('fruit', 80), 253: ('fruit', 100),
    254: ('fruit', 120), 255: ('fruit', 100), 256: ('fruit', 80),
    # batch 7: seasonal fruit, vegetables, spices, seafood and Levantine dishes
    257: ('fruit', 150), 258: ('fruit', 100), 259: ('fruit', 100), 260: ('fruit', 100), 261: ('veg', 100), 262: ('veg', 80),
    263: ('veg', 80), 264: ('veg', 50), 265: ('veg', 150), 266: ('veg', 100), 267: ('spice', 1), 268: ('spice', 1),
    269: ('spice', 1), 270: ('spice', 1), 271: ('spice', 3), 272: ('spice', 3), 273: ('protein', 150), 274: ('protein', 150),
    275: ('protein', 150), 276: ('protein', 100), 277: ('protein', 15), 278: ('protein', 15), 279: ('arabic', 150),
    280: ('arabic', 250), 281: ('arabic', 250),
    # batch 8: regional dishes, pantry items, condiments, drinks (incl. alcohol, with warnings) and Dutch staples
    282: ('arabic', 250), 283: ('sweets', 60), 284: ('pantry', 10), 285: ('pantry', 15), 286: ('pantry', 60),
    287: ('bakery', 40), 288: ('grain', 150), 289: ('condiment', 10), 290: ('condiment', 15), 291: ('condiment', 5),
    292: ('condiment', 50), 293: ('condiment', 20), 294: ('alcohol', 330), 295: ('alcohol', 150), 296: ('drink', 250),
    297: ('drink', 300), 298: ('drink', 250), 299: ('drink', 70), 300: ('drink', 200), 301: ('veg', 80), 302: ('veg', 100),
    303: ('dairy_drink', 250), 304: ('dairy_solid', 150), 305: ('dairy_solid', 100), 306: ('grain', 40),
    # batch 9: Dutch classics - fish, stamppot, snacks, cheeses, sweets and breakfast toppings
    # (portions approved by Dr. Wassim on 13 October 2026)
    307: ('protein', 80), 308: ('home', 300), 309: ('home', 250), 310: ('home', 250), 311: ('protein', 60),
    312: ('protein', 150), 313: ('sweets', 30), 314: ('sweets', 50), 315: ('sweets', 15), 316: ('sweets', 25),
    317: ('fastfood', 60), 318: ('fastfood', 70), 319: ('fastfood', 70), 320: ('protein', 30), 321: ('protein', 25),
    322: ('dairy_solid', 30), 323: ('dairy_solid', 30), 324: ('dairy_solid', 30), 325: ('dairy_solid', 30),
    326: ('sweets', 100), 327: ('dairy_drink', 200), 328: ('pantry', 10), 329: ('bakery', 10), 330: ('bakery', 30),
    331: ('sweets', 15),
    # batch 10: European cheeses, artisan breads and ancient grains & flours
    # (portions approved by Dr. Wassim on 13 October 2026)
    332: ('dairy_solid', 15), 333: ('dairy_solid', 10), 334: ('dairy_solid', 30), 335: ('dairy_solid', 30),
    336: ('dairy_solid', 30), 337: ('dairy_solid', 60), 338: ('dairy_solid', 15), 339: ('dairy_solid', 30),
    340: ('dairy_solid', 30), 341: ('dairy_solid', 10), 342: ('dairy_solid', 30), 343: ('dairy_solid', 150),
    344: ('grain', 40), 345: ('grain', 40), 346: ('grain', 60), 347: ('grain', 35), 348: ('grain', 35),
    349: ('grain', 50), 350: ('grain', 150), 351: ('grain', 30), 352: ('grain', 150), 353: ('grain', 30),
    354: ('grain', 30), 355: ('grain', 120), 356: ('grain', 30),
    # batch 11: muesli & granola, European and leafy vegetables, peppers, squash and berries
    # (portions approved by Dr. Wassim on 13 October 2026)
    357: ('grain', 45), 358: ('grain', 30), 359: ('veg', 100), 360: ('veg', 150), 361: ('veg', 100),
    362: ('veg', 150), 363: ('veg', 80), 364: ('veg', 80), 365: ('veg', 80), 366: ('veg', 80), 367: ('veg', 100),
    368: ('veg', 100), 369: ('veg', 15), 370: ('veg', 10), 371: ('veg', 150), 372: ('veg', 50), 373: ('veg', 80),
    374: ('veg', 100), 375: ('veg', 150), 376: ('veg', 100), 377: ('veg', 15), 378: ('veg', 5), 379: ('veg', 120),
    380: ('veg', 100), 381: ('fruit', 140),
    # batch 12: berries, stone fruit, citrus, tropical fruit, premium nuts and hemp seeds
    # (portions approved by Dr. Wassim on 13 October 2026)
    382: ('fruit', 100), 383: ('fruit', 50), 384: ('fruit', 50), 385: ('fruit', 100), 386: ('fruit', 100),
    387: ('fruit', 140), 388: ('fruit', 100), 389: ('fruit', 100), 390: ('fruit', 150), 391: ('fruit', 100),
    392: ('fruit', 150), 393: ('fruit', 15), 394: ('fruit', 15), 395: ('fruit', 100), 396: ('fruit', 145),
    397: ('nuts', 30), 398: ('nuts', 15), 399: ('nuts', 10), 400: ('nuts', 20),
    # batch 13: white fish, shellfish, lean & cured meats, offal, pulses, canned vegetables and Spanish tapas
    401: ('protein', 150), 402: ('protein', 150), 403: ('protein', 150), 404: ('protein', 150), 405: ('protein', 150),
    406: ('protein', 150), 407: ('protein', 150), 408: ('protein', 150), 409: ('protein', 100), 410: ('protein', 100),
    411: ('protein', 100), 412: ('protein', 150), 413: ('protein', 100), 414: ('protein', 50), 415: ('protein', 120),
    416: ('protein', 120), 417: ('protein', 120), 418: ('protein', 40), 419: ('protein', 30), 420: ('protein', 50),
    421: ('protein', 75), 422: ('protein', 120), 423: ('protein', 100), 424: ('protein', 100), 425: ('legume', 150),
    426: ('legume', 150), 427: ('legume', 150), 428: ('legume', 150), 429: ('legume', 150), 430: ('legume', 150),
    431: ('legume', 150), 432: ('legume', 150), 433: ('veg', 80), 434: ('veg', 100), 435: ('veg', 100),
    436: ('veg', 100), 437: ('veg', 100), 438: ('veg', 80), 439: ('veg', 100), 440: ('condiment', 100),
    441: ('veg', 100), 442: ('veg', 100), 443: ('condiment', 10), 444: ('spanish', 250), 445: ('spanish', 150),
    446: ('spanish', 200), 447: ('spanish', 150), 448: ('spanish', 100), 449: ('spanish', 150), 450: ('spanish', 150),
    # batch 14: tapas, French and German/Austrian classics, Greek dishes, Levantine kibbeh & offal, breads and spreads
    451: ('spanish', 100), 452: ('sweets', 60), 453: ('spanish', 80), 454: ('french', 300), 455: ('french', 200),
    456: ('french', 150), 457: ('french', 250), 458: ('french', 250), 459: ('salad', 300), 460: ('french', 150),
    461: ('french', 120), 462: ('french', 150), 463: ('sweets', 100), 464: ('protein', 150), 465: ('grain', 150),
    466: ('salad', 150), 467: ('home', 300), 468: ('bakery', 90), 469: ('sweets', 100), 470: ('sweets', 150),
    471: ('greek', 250), 472: ('greek', 150), 473: ('greek', 50), 474: ('greek', 120), 475: ('greek', 100),
    476: ('greek', 250), 477: ('greek', 300), 478: ('greek', 300), 479: ('arabic', 200), 480: ('arabic', 150),
    481: ('arabic', 100), 482: ('arabic', 300), 483: ('arabic', 250), 484: ('arabic', 150), 485: ('arabic', 300),
    486: ('arabic', 150), 487: ('arabic', 300), 488: ('arabic', 200), 489: ('arabic', 300), 490: ('arabic', 250),
    491: ('arabic', 250), 492: ('arabic', 150), 493: ('arabic', 150), 494: ('bakery', 100), 495: ('arabic', 150),
    496: ('arabic', 60), 497: ('salad', 200), 498: ('salad', 150), 499: ('pantry', 15), 500: ('pantry', 15),
    # batch 15: Turkish, Moroccan and Indian kitchens, South-East Asian dishes, breads, sweets and drinks
    501: ('turkish', 150), 502: ('turkish', 300), 503: ('turkish', 150), 504: ('turkish', 250), 505: ('turkish', 200),
    506: ('turkish', 120), 507: ('turkish', 200), 508: ('turkish', 150), 509: ('turkish', 300), 510: ('turkish', 100),
    511: ('sweets', 30), 512: ('drink', 250), 513: ('moroccan', 300), 514: ('moroccan', 300), 515: ('moroccan', 300),
    516: ('moroccan', 150), 517: ('moroccan', 150), 518: ('moroccan', 300), 519: ('moroccan', 350),
    520: ('moroccan', 100), 521: ('moroccan', 100), 522: ('bakery', 70), 523: ('sweets', 80), 524: ('bakery', 80),
    525: ('sweets', 30), 526: ('sweets', 30), 527: ('condiment', 10), 528: ('condiment', 15), 529: ('indian', 250),
    530: ('indian', 250), 531: ('indian', 250), 532: ('indian', 250), 533: ('indian', 200), 534: ('indian', 200),
    535: ('indian', 200), 536: ('indian', 150), 537: ('indian', 250), 538: ('indian', 100), 539: ('bakery', 40),
    540: ('bakery', 80), 541: ('dairy_drink', 250), 542: ('drink', 250), 543: ('sweets', 50), 544: ('sweets', 150),
    545: ('asian', 500), 546: ('asian', 150), 547: ('asian', 300), 548: ('asian', 250), 549: ('asian', 250),
    550: ('salad', 200),
    # batch 16: East Asian dishes and noodles, seaweed, mushrooms, superfoods, seeds, oils and wild fruit
    # (portions approved by Dr. Wassim on 16 October 2026)
    551: ('asian', 150), 552: ('asian', 200), 553: ('asian', 150), 554: ('asian', 250), 555: ('asian', 250),
    556: ('protein', 50), 557: ('grain', 150), 558: ('grain', 150), 559: ('grain', 200), 560: ('asian', 300),
    561: ('asian', 150), 562: ('asian', 150), 563: ('veg', 30), 564: ('veg', 3), 565: ('veg', 80), 566: ('veg', 80),
    567: ('pantry', 10), 568: ('pantry', 20), 569: ('pantry', 5), 570: ('pantry', 10), 571: ('pantry', 10),
    572: ('pantry', 10), 573: ('fat', 10), 574: ('nuts', 15), 575: ('nuts', 10), 576: ('nuts', 16), 577: ('nuts', 16),
    578: ('fat', 10), 579: ('fat', 5), 580: ('fat', 5), 581: ('fruit', 100), 582: ('fruit', 50), 583: ('fruit', 50),
    584: ('fruit', 150), 585: ('dried', 40), 586: ('fruit', 100), 587: ('dried', 30), 588: ('nuts', 80),
    589: ('nuts', 15), 590: ('nuts', 10), 591: ('drink', 250), 592: ('drink', 250), 593: ('drink', 250),
    594: ('drink', 250), 595: ('drink', 250), 596: ('drink', 250), 597: ('drink', 250), 598: ('drink', 250),
    599: ('drink', 250), 600: ('pantry', 15),
}
# foods whose page is signed by the medical team instead of a named reviewer
TEAM_REVIEW = {6, 12, 13, 15, 16, 20, 21, 23, 24, 25, 28, 33, 34, 41, 42, 43, 44, 45, 46, 47, 52, 56, 57, 58, 60, 61,
               64, 65, 67, 73, 75, 76, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 95, 96, 97, 99, 100, 102,
               103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126,
               127, 129, 130, 131, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
               156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180,
               181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206}
TEAM_REVIEW |= set(range(207, 601))
# drinks whose third tip is the approved caffeine note (others get the carbohydrate / not-applicable note)
CAFFEINE = {132, 133, 134, 140}
SLUG_OVERRIDES = {71: 'greek-yogurt'}

GROUPS = {
    'grain': ('الحبوب والنشويات', 'Grains & starches', 'Granen & zetmeel'),
    'tuber': ('البطاطا والدرنيات', 'Potatoes & tubers', 'Aardappelen & knollen'),
    'legume': ('البقوليات', 'Legumes', 'Peulvruchten'),
    'fruit': ('الفواكه', 'Fruit', 'Fruit'),
    'dried': ('التمور والفواكه المجففة', 'Dates & dried fruit', 'Dadels & gedroogd fruit'),
    'dairy_drink': ('الحليب ومشروبات الألبان', 'Milk & dairy drinks', 'Melk & zuiveldranken'),
    'dairy_solid': ('الألبان والأجبان', 'Dairy & cheese', 'Zuivel & kaas'),
    'protein': ('اللحوم والأسماك والبيض', 'Meat, fish & eggs', 'Vlees, vis & eieren'),
    'fat': ('الدهون الصحية', 'Healthy fats', 'Gezonde vetten'),
    'nuts': ('المكسرات والبذور', 'Nuts & seeds', 'Noten & zaden'),
    'arabic': ('الأطباق العربية', 'Arabic dishes', 'Arabische gerechten'),
    'fastfood': ('وجبات المطاعم السريعة', 'Fast food', 'Fastfood'),
    'sweets': ('الحلويات', 'Sweets & desserts', 'Zoetigheid & desserts'),
    'mexican': ('الأطباق المكسيكية', 'Mexican dishes', 'Mexicaanse gerechten'),
    'italian': ('الأطباق الإيطالية', 'Italian dishes', 'Italiaanse gerechten'),
    'spanish': ('الأطباق الإسبانية', 'Spanish dishes', 'Spaanse gerechten'),
    'french': ('الأطباق الفرنسية', 'French dishes', 'Franse gerechten'),
    'greek': ('الأطباق اليونانية', 'Greek dishes', 'Griekse gerechten'),
    'turkish': ('الأطباق التركية', 'Turkish dishes', 'Turkse gerechten'),
    'moroccan': ('الأطباق المغربية', 'Moroccan dishes', 'Marokkaanse gerechten'),
    'indian': ('الأطباق الهندية', 'Indian dishes', 'Indiase gerechten'),
    'asian': ('الأطباق الآسيوية', 'Asian dishes', 'Aziatische gerechten'),
    'bakery': ('المخبوزات والفطائر', 'Breads & pastries', 'Brood & hartige baksels'),
    'sandwich': ('السندويشات', 'Sandwiches', 'Broodjes'),
    'home': ('الشوربات والطبخات المنزلية', 'Soups & home-cooked dishes', 'Soepen & huisgemaakte gerechten'),
    'salad': ('السلطات', 'Salads', 'Salades'),
    'spice': ('التوابل والأعشاب', 'Spices & herbs', 'Specerijen & kruiden'),
    'pantry': ('المكونات الخاصة والمكملات', 'Special ingredients & supplements', 'Speciale ingrediënten & supplementen'),
    'condiment': ('الصلصات والمخللات والزيتون', 'Sauces, pickles & olives', 'Sauzen, zuur & olijven'),
    'alcohol': ('المشروبات الكحولية', 'Alcoholic drinks', 'Alcoholische dranken'),
    'veg': ('الخضار', 'Vegetables', 'Groenten'),
    'drink': ('المشروبات', 'Drinks', 'Dranken'),
}

CARB_NOTE = (
    'لمرضى السكري ومقاومة الإنسولين، يُوصى دائماً بمراعاة الحمل الجلايسيمي (GL) الكلي للوجبة وعدم الاعتماد على المؤشر منفرداً.',
    'For people with diabetes or insulin resistance, it is always recommended to consider the total glycemic load (GL) of the meal rather than relying on the glycemic index alone.',
    'Bij diabetes of insulineresistentie wordt altijd aangeraden rekening te houden met de totale glykemische lading (GL) van de maaltijd, en niet alleen met de glykemische index.')
NA_NOTE = (
    'لا يحتاج هذا الصنف إلى مؤشر جلايسيمي، لكن الأطعمة المرافقة له في الوجبة هي التي تحدد أثرها على سكر الدم.',
    'This food does not need a glycemic index, but the foods eaten with it determine the meal\u2019s effect on blood sugar.',
    'Voor dit product is geen glykemische index nodig, maar de producten die je erbij eet bepalen het effect van de maaltijd op de bloedsuiker.')

# (consumption advice, preparation, important note) per group and language
TIPS = {
    'grain': (
        ('تناوله ضمن وجبة متوازنة وبحصة معتدلة، واجمعه مع مصدر بروتين وخضار غنية بالألياف لإبطاء ارتفاع سكر الدم.',
         'اختر الأصناف الكاملة متى أمكن ولا تُفرط في الطهي؛ فالطهي الطويل يرفع المؤشر الجلايسيمي، وتبريد النشويات المطبوخة ثم إعادة تسخينها قد يخفّض استجابة السكر قليلاً.', CARB_NOTE[0]),
        ('Eat it as part of a balanced meal in a moderate portion, together with a protein source and fibre-rich vegetables to slow the rise in blood sugar.',
         'Choose wholegrain versions when possible and avoid overcooking: longer cooking raises the GI, while cooling cooked starches and reheating them may lower the glucose response slightly.', CARB_NOTE[1]),
        ('Eet het als onderdeel van een evenwichtige maaltijd in een gematigde portie, samen met een eiwitbron en vezelrijke groenten om de bloedsuikerstijging te vertragen.',
         'Kies waar mogelijk volkoren varianten en kook niet te lang: langer koken verhoogt de GI, terwijl afkoelen en opnieuw opwarmen van gekookte zetmeelproducten de glucoserespons iets kan verlagen.', CARB_NOTE[2])),
    'tuber': (
        ('اعتبره مصدر النشويات في الوجبة وليس من الخضار، وقلّل الحصة إذا تناولت معه خبزاً أو أرزاً.',
         'السلق أو الخبز بالقشر أفضل من القلي والهرس؛ فالهرس يرفع المؤشر الجلايسيمي، والقلي يضيف سعرات ودهوناً كثيرة.', CARB_NOTE[0]),
        ('Count it as the starch of the meal rather than as a vegetable, and reduce the portion if you also eat bread or rice.',
         'Boiling or baking with the skin on is better than frying or mashing: mashing raises the GI and frying adds many calories and fat.', CARB_NOTE[1]),
        ('Tel het als zetmeelbron van de maaltijd, niet als groente, en neem een kleinere portie als je er ook brood of rijst bij eet.',
         'Koken of bakken met schil is beter dan frituren of pureren: pureren verhoogt de GI en frituren voegt veel calorieën en vet toe.', CARB_NOTE[2])),
    'legume': (
        ('البقوليات من أفضل مصادر الألياف والبروتين النباتي، ويمكن أن تحل جزئياً محل الأرز أو الخبز في الوجبة.',
         'انقعها جيداً قبل الطهي واطبخها حتى تنضج، واغسل المعلّب منها لتقليل الملح.', CARB_NOTE[0]),
        ('Legumes are among the best sources of fibre and plant protein, and can partly replace rice or bread in a meal.',
         'Soak them well before cooking and cook until tender; rinse canned legumes to reduce the salt.', CARB_NOTE[1]),
        ('Peulvruchten behoren tot de beste bronnen van vezels en plantaardig eiwit en kunnen rijst of brood in een maaltijd deels vervangen.',
         'Week ze goed voor het koken en kook ze gaar; spoel peulvruchten uit blik af om zout te verminderen.', CARB_NOTE[2])),
    'fruit': (
        ('تناول الفاكهة كاملة بقشرها متى أمكن بدلاً من العصير، فالألياف تبطئ امتصاص السكر وتزيد الشبع.',
         'تناولها طازجة وفي موسمها، ويمكن جمعها مع حفنة مكسرات أو لبن لإبطاء الاستجابة السكرية.', CARB_NOTE[0]),
        ('Eat the whole fruit, with the skin where possible, rather than juice: the fibre slows sugar absorption and increases fullness.',
         'Enjoy it fresh and in season; pairing it with a handful of nuts or yoghurt can slow the glucose response.', CARB_NOTE[1]),
        ('Eet het hele fruit, waar mogelijk met schil, in plaats van sap: de vezels vertragen de suikeropname en geven meer verzadiging.',
         'Eet het vers en in het seizoen; combineren met een handje noten of yoghurt kan de glucoserespons vertragen.', CARB_NOTE[2])),
    'dried': (
        ('السكريات فيه مركّزة، لذا التزم بحصة صغيرة واعتبرها جزءاً من سكريات يومك.',
         'اجمعه مع مصدر بروتين أو دهون صحية كالمكسرات أو اللبن لإبطاء ارتفاع سكر الدم.', CARB_NOTE[0]),
        ('Its sugars are concentrated, so keep to a small portion and count it as part of your daily sugar intake.',
         'Combine it with protein or healthy fats such as nuts or yoghurt to slow the rise in blood sugar.', CARB_NOTE[1]),
        ('De suikers zijn geconcentreerd, dus houd het bij een kleine portie en tel het mee als onderdeel van je dagelijkse suikerinname.',
         'Combineer het met eiwit of gezonde vetten zoals noten of yoghurt om de bloedsuikerstijging te vertragen.', CARB_NOTE[2])),
    'dairy_drink': (
        ('مصدر جيد للبروتين والكالسيوم بمؤشر جلايسيمي منخفض؛ اختر الأنواع غير المحلاة.',
         'تجنب إضافة السكر أو العسل أو المنكهات، فهي ترفع الحمل الجلايسيمي للمشروب بشكل كبير.', CARB_NOTE[0]),
        ('A good source of protein and calcium with a low GI; choose unsweetened versions.',
         'Avoid adding sugar, honey or flavourings, which raise the drink\u2019s glycemic load considerably.', CARB_NOTE[1]),
        ('Een goede bron van eiwit en calcium met een lage GI; kies ongezoete varianten.',
         'Voeg geen suiker, honing of smaakstoffen toe; die verhogen de glykemische lading van de drank aanzienlijk.', CARB_NOTE[2])),
    'dairy_solid': (
        ('غني بالبروتين وأثره المباشر على سكر الدم ضئيل، لكنه قد يحتوي دهوناً مشبعة وملحاً، فالتزم بحصة معتدلة.',
         'اختر الأنواع الأقل ملحاً ودهوناً، وقدّمه مع الخضار أو خبز الحبوب الكاملة.', NA_NOTE[0]),
        ('Rich in protein with minimal direct effect on blood sugar, but it can be high in saturated fat and salt, so keep to a moderate portion.',
         'Choose lower-salt, lower-fat versions and serve it with vegetables or wholegrain bread.', NA_NOTE[1]),
        ('Rijk aan eiwit met weinig direct effect op de bloedsuiker, maar het kan veel verzadigd vet en zout bevatten; houd de portie gematigd.',
         'Kies varianten met minder zout en vet en eet het met groenten of volkorenbrood.', NA_NOTE[2])),
    'protein': (
        ('مصدر ممتاز للبروتين الذي يعزز الشبع، ووجوده في الوجبة مع النشويات يساعد على إبطاء ارتفاع سكر الدم.',
         'فضّل الشوي أو السلق أو الطهي بالبخار على القلي العميق، وتجنب التحمير الزائد والتفحّم.', NA_NOTE[0]),
        ('An excellent source of protein, which supports fullness; eating it with starchy foods helps slow the rise in blood sugar.',
         'Prefer grilling, boiling or steaming over deep-frying, and avoid charring.', NA_NOTE[1]),
        ('Een uitstekende eiwitbron die verzadiging bevordert; samen met zetmeelrijke producten helpt het de bloedsuikerstijging te vertragen.',
         'Kies grillen, koken of stomen in plaats van frituren, en vermijd aanbranden.', NA_NOTE[2])),
    'fat': (
        ('غني بالدهون غير المشبعة المفيدة لكنه مرتفع السعرات، فالكمية الصغيرة تكفي.',
         'إضافة كمية معتدلة منه إلى وجبة نشوية قد تبطئ امتصاص السكر؛ استخدمه نيئاً في السلطات متى أمكن.', NA_NOTE[0]),
        ('Rich in healthy unsaturated fats but high in calories, so a small amount is enough.',
         'Adding a moderate amount to a starchy meal can slow sugar absorption; use it raw in salads when possible.', NA_NOTE[1]),
        ('Rijk aan gezonde onverzadigde vetten maar calorierijk, dus een kleine hoeveelheid is genoeg.',
         'Een gematigde hoeveelheid bij een zetmeelrijke maaltijd kan de suikeropname vertragen; gebruik het waar mogelijk rauw in salades.', NA_NOTE[2])),
    'nuts': (
        ('غنية بالدهون الصحية والبروتين والألياف لكنها مرتفعة السعرات، فالتزم بحفنة صغيرة.',
         'اخترها نيئة أو محمصة دون ملح أو سكر أو زيوت مضافة.', CARB_NOTE[0]),
        ('Rich in healthy fats, protein and fibre but high in calories, so keep to a small handful.',
         'Choose them raw or dry-roasted, without added salt, sugar or oil.', CARB_NOTE[1]),
        ('Rijk aan gezonde vetten, eiwit en vezels maar calorierijk, dus houd het bij een klein handje.',
         'Kies ze rauw of droog geroosterd, zonder toegevoegd zout, suiker of olie.', CARB_NOTE[2])),
    'arabic': (
        ('تناوله بحصة معتدلة ضمن وجبة فيها خضار وبروتين.', 'فضّل الشوي أو الخبز في الفرن على القلي، واستخدم زيت الزيتون باعتدال.', CARB_NOTE[0]),
        ('Eat it in a moderate portion as part of a meal with vegetables and protein.', 'Prefer grilling or baking over frying, and use olive oil in moderation.', CARB_NOTE[1]),
        ('Eet het in een gematigde portie als onderdeel van een maaltijd met groenten en eiwit.', 'Kies grillen of bakken in de oven in plaats van frituren, en gebruik olijfolie met mate.', CARB_NOTE[2])),
    'fastfood': (
        ('اجعلها وجبة متباعدة بحصة صغيرة، ومعها سلطة وماء بدلاً من البطاطا والمشروبات الغازية.', 'اختر الخيارات المشوية والخبز الأسمر وقلل الصلصات المحلاة.', CARB_NOTE[0]),
        ('Keep it occasional and small, with a salad and water instead of fries and soft drinks.', 'Choose grilled options and wholegrain bread, and limit sweet sauces.', CARB_NOTE[1]),
        ('Houd het bij af en toe en een kleine portie, met salade en water in plaats van friet en frisdrank.', 'Kies gegrilde opties en volkorenbrood, en beperk zoete sauzen.', CARB_NOTE[2])),
    'sweets': (
        ('تناولها بحصة صغيرة بعد وجبة فيها بروتين وألياف، لا على معدة فارغة.', 'اختر الأصناف الأقل قطراً وسكراً، وحضّرها منزلياً بكمية سكر أقل.', CARB_NOTE[0]),
        ('Have a small portion after a meal with protein and fibre, not on an empty stomach.', 'Choose versions with less syrup and sugar, and make them at home with less sugar.', CARB_NOTE[1]),
        ('Neem een kleine portie na een maaltijd met eiwit en vezels, niet op een lege maag.', 'Kies varianten met minder siroop en suiker, en maak ze thuis met minder suiker.', CARB_NOTE[2])),
    'mexican': None, 'italian': None, 'spanish': None, 'french': None, 'greek': None, 'turkish': None, 'moroccan': None, 'indian': None, 'asian': None, 'bakery': None, 'sandwich': None,   # filled from 'arabic' below
    'veg': (
        ('خضار منخفضة السعرات وغنية بالماء والألياف، ويمكن أن تملأ نصف الطبق.',
         'تناولها نيئة أو مطهوة قليلاً على البخار للحفاظ على الفيتامينات، وقلّل الزيت عند الطهي.', NA_NOTE[0]),
        ('A low-calorie vegetable rich in water and fibre; it can fill half your plate.',
         'Eat it raw or lightly steamed to preserve vitamins, and use little oil when cooking.', NA_NOTE[1]),
        ('Een caloriearme groente, rijk aan water en vezels; ze kan de helft van je bord vullen.',
         'Eet ze rauw of licht gestoomd om vitamines te behouden, en gebruik weinig olie bij het koken.', NA_NOTE[2])),
    'drink': (
        ('خالٍ تقريباً من السعرات والسكريات عند تناوله دون إضافات.',
         'تجنب السكر والشراب المحلّى والكريمة؛ فهي التي تضيف السعرات والحمل الجلايسيمي.',
         'يحتوي على الكافيين؛ اعتدل في الكمية خاصة في المساء، واستشر طبيبك في حالات الحمل أو عند تناول أدوية تتأثر بالكافيين.'),
        ('Almost free of calories and sugars when taken without additions.',
         'Avoid sugar, syrups and cream, which are what add calories and glycemic load.',
         'Contains caffeine: keep intake moderate, especially in the evening, and ask your doctor if you are pregnant or take medication affected by caffeine.'),
        ('Vrijwel zonder calorieën en suikers als je het zonder toevoegingen drinkt.',
         'Vermijd suiker, siropen en room; die voegen de calorieën en glykemische lading toe.',
         'Bevat cafeïne: drink met mate, vooral \u2019s avonds, en overleg met je arts als je zwanger bent of medicijnen gebruikt die door cafeïne beïnvloed worden.')),
}

for _g in ('mexican', 'italian', 'spanish', 'french', 'greek', 'turkish', 'moroccan', 'indian', 'asian', 'bakery', 'sandwich', 'home', 'salad', 'spice', 'pantry', 'condiment', 'alcohol'):
    TIPS[_g] = TIPS['arabic']                # generic fallback; every food in these groups has its own approved tips

UI = {
    'ar': dict(
        dir='rtl', title='{name}: السعرات والمؤشر الجلايسيمي والقيم الغذائية | WiBo Health',
        desc_measured='{name}: {kcal} سعرة لكل 100 غ، المؤشر الجلايسيمي {gi} ({level}) وفق Atkinson 2021، والحمل الجلايسيمي {gl} لحصة {p} غ. قيم غذائية كاملة ونصائح وبدائل.',
        desc_reviewed='{name}: {kcal} سعرة لكل 100 غ، المؤشر الجلايسيمي {gi} ({level}، تقدير مراجع سريرياً)، والحمل الجلايسيمي {gl} لحصة {p} غ. قيم غذائية كاملة ونصائح وبدائل.',
        desc_na='{name}: {kcal} سعرة و{protein} غ بروتين لكل 100 غ. المؤشر الجلايسيمي لا ينطبق (أقل من 5 غ كربوهيدرات متاحة). قيم غذائية كاملة ونصائح وبدائل.',
        home='الرئيسية', guide='دليل الأطعمة', gi='المؤشر الجلايسيمي', gl='الحمل الجلايسيمي', kcal='السعرات الحرارية',
        protein='البروتين', per100='لكل 100 غ', per_portion='لحصة {p} غ', na='لا ينطبق',
        levels=('منخفض', 'متوسط', 'مرتفع'), gram='غ', kcal_unit='سعرة',
        tips='💡 الإرشاد الغذائي الذكي', tip_titles=('توصيات الاستهلاك', 'أفضل طرق التحضير', 'ملاحظة غذائية هامة'),
        table='القيم الغذائية', nutrient='العنصر الغذائي', col100='لكل 100 غ', colp='لحصة معتادة ({p} غ)',
        rows=('السعرات الحرارية', 'البروتين', 'الكربوهيدرات', 'الكربوهيدرات المتاحة', 'الدهون', 'الألياف الغذائية'),
        ii_row='مؤشر الإنسولين', ii_tested='مختبر سريرياً (Holt / Bao)',
        compare='مقارنة وبدائل ذكية', alt_lower='بدائل بمؤشر جلايسيمي أقل:', alt_same='أصناف قريبة من نفس العائلة:',
        alt_family='بدائل ذكية من نفس العائلة:',
        lowest_note='هذا من أقل الأصناف مؤشراً في فئته.',
        rank_measured='{ya}أتي في المرتبة {rank} من {m_items} في فئة {group} من حيث المؤشر الجلايسيمي (الأقل أولاً).',
        rank_protein='{ya}وفر {v} غ بروتين لكل 100 سعرة، في المرتبة {rank} من {m} في فئة {group} (الأعلى أولاً).',
        rank_kcal='{ya}حتوي على {v} سعرة لكل 100 غ، في المرتبة {rank} من {m} في فئة {group} (الأقل أولاً).',
        lead_measured='كل 100 غ من {name} تحتوي على {kcal} سعرة حرارية و{avail} غ كربوهيدرات متاحة. مؤشر{h} الجلايسيمي {gi} ({level})، وهو متوسط {studies} في الجداول الدولية (Atkinson 2021). وفي حصة معتادة من {p} غ يبلغ حمل{h} الجلايسيمي {gl} ({gl_level}).',
        lead_reviewed='كل 100 غ من {name} تحتوي على {kcal} سعرة حرارية و{avail} غ كربوهيدرات متاحة. مؤشر{h} الجلايسيمي {gi} ({level})، وهو تقدير مراجع سريرياً وليس قياساً مخبرياً. وفي حصة معتادة من {p} غ يبلغ حمل{h} الجلايسيمي {gl} ({gl_level}).',
        gi_reviewed='تقدير مراجع سريرياً',
        rank_reviewed='{ya}أتي في المرتبة {rank} بين أصناف فئة {group} التي لها مؤشر جلايسيمي (وعددها {m})، من الأقل إلى الأعلى.',
        src_reviewed='📚 قيمة المؤشر الجلايسيمي لهذا الصنف تقدير مراجع سريرياً من فريق ويبو هيلث الطبي، وليست قياساً مخبرياً من الجداول الدولية (Atkinson 2021).',
        reviewed_team='تمت مراجعته من قبل فريق ويبو هيلث الطبي · آخر مراجعة {date}',
        lead_na='كل 100 غ من {name} تحتوي على {kcal} سعرة حرارية و{protein} غ بروتين. ولأن{h} {ya}حتوي على أقل من 5 غ كربوهيدرات متاحة لكل 100 غ، فلا ينطبق علي{h} المؤشر الجلايسيمي، ويكون أثر{h} المباشر على سكر الدم ضئيلاً.',
        boodi_title='امسح الباركود في السوبرماركت مع تطبيق بودي 💚',
        boodi_text='يحلل بودي المنتجات المعلّبة فوراً، ويفحص الحلال، ويقترح بدائل أقل سكراً من نفس الرف.',
        boodi_btn='اكتشف تطبيق بودي',
        src_gi='📚 المراجع العلمية المعتمدة: الجداول الدولية للمؤشر الجلايسيمي (Atkinson et al., Am J Clin Nutr 2021) • أبحاث جامعة هارفارد الطبية (Harvard Health).',
        src_value='القيمة المعتمدة: متوسط {studies} (النطاق {lo}–{hi})، درجة الثقة {grade}.',
        src_ii='📚 مراجع مؤشر الإنسولين: Holt SH et al., Am J Clin Nutr 1997;66(5):1264–76 • Bao J et al., Am J Clin Nutr 2009;90(4):986–92.',
        src_link='المنهجية والتفاصيل ←',
        disclaimer='إخلاء مسؤولية: هذه البيانات استرشادية لنمط الحياة وليست جهازاً طبياً تشخيصياً وفق اللائحة الأوروبية EU MDR 2017/745. استشر طبيبك دائماً قبل تعديل نظامك العلاجي.',
        reviewed='راجعه طبياً: <a href="{doctor}">د. وسيم حبيب</a> · آخر مراجعة {date}',
        portion_note='الحصة المعتادة تقريبية لأغراض المقارنة.',
        theme='تبديل المظهر', footer_rights='© 2026 WiBo Health Group. جميع الحقوق محفوظة.',
        nav=('الرئيسية', 'دليل الأطعمة', 'الحاسبات', 'المكملات', 'المقالات', 'تطبيق بودي 💚'), privacy='الخصوصية',
        methodology='المنهجية والمراجع العلمية'),
    'en': dict(
        dir='ltr', title='{name}: Calories, Glycemic Index & Nutrition Facts | WiBo Health',
        desc_measured='{name}: {kcal} kcal per 100 g, glycemic index {gi} ({level}) from Atkinson 2021, glycemic load {gl} per {p} g portion. Full nutrition facts, tips and alternatives.',
        desc_reviewed='{name}: {kcal} kcal per 100 g, glycemic index {gi} ({level}, clinically reviewed estimate), glycemic load {gl} per {p} g portion. Full nutrition facts, tips and alternatives.',
        desc_na='{name}: {kcal} kcal and {protein} g protein per 100 g. Glycemic index not applicable (under 5 g available carbohydrate). Full nutrition facts, tips and alternatives.',
        home='Home', guide='Food guide', gi='Glycemic index', gl='Glycemic load', kcal='Calories', protein='Protein',
        per100='per 100 g', per_portion='per {p} g portion', na='Not applicable', levels=('Low', 'Medium', 'High'),
        gram='g', kcal_unit='kcal', tips='💡 Smart Nutritional Guidance',
        tip_titles=('Consumption advice', 'Best preparation methods', 'Important Nutritional Note'),
        table='Nutrition facts', nutrient='Nutrient', col100='Per 100 g', colp='Per typical portion ({p} g)',
        rows=('Calories', 'Protein', 'Carbohydrate', 'Available carbohydrate', 'Fat', 'Dietary fibre'),
        ii_row='Insulin index', ii_tested='clinically tested (Holt / Bao)',
        compare='Comparison & smarter alternatives', alt_lower='Lower-GI alternatives:', alt_same='Related foods from the same family:',
        alt_family='Smart alternatives from the same family:',
        lowest_note='This is one of the lowest-GI foods in its group.',
        rank_measured='It ranks {rank} of {m} measured foods in {group} by glycemic index (lowest first).',
        rank_protein='It provides {v} g of protein per 100 kcal, ranking {rank} of {m} in {group} (highest first).',
        rank_kcal='It has {v} kcal per 100 g, ranking {rank} of {m} in {group} (lowest first).',
        lead_measured='Every 100 g of {name} contains {kcal} kcal and {avail} g of available carbohydrate. Its glycemic index is {gi} ({level}), the average of {studies} in the International GI Tables (Atkinson 2021). A typical {p} g portion has a glycemic load of {gl} ({gl_level}).',
        lead_reviewed='Every 100 g of {name} contains {kcal} kcal and {avail} g of available carbohydrate. Its glycemic index is {gi} ({level}), a clinically reviewed estimate rather than a laboratory measurement. A typical {p} g portion has a glycemic load of {gl} ({gl_level}).',
        gi_reviewed='Clinically reviewed estimate',
        rank_reviewed='Among the foods in {group} with a glycemic index ({m}), it ranks {rank} (lowest first).',
        src_reviewed='📚 The glycemic index of this food is a clinically reviewed estimate by the WiBo Health medical team, not a laboratory measurement from the International GI Tables (Atkinson 2021).',
        reviewed_team='Reviewed by the WiBo Health medical team · Last reviewed {date}',
        lead_na='Every 100 g of {name} contains {kcal} kcal and {protein} g of protein. Because it has less than 5 g of available carbohydrate per 100 g, the glycemic index does not apply and its direct effect on blood sugar is minimal.',
        boodi_title='Scan supermarket barcodes with the boodi app 💚',
        boodi_text='boodi analyses packaged products instantly, checks halal status and suggests lower-sugar alternatives from the same shelf.',
        boodi_btn='Discover the boodi app',
        src_gi='📚 Scientific sources: International Tables of Glycemic Index (Atkinson et al., Am J Clin Nutr 2021) • Harvard Health Publishing.',
        src_value='Approved value: average of {studies} (range {lo}–{hi}), confidence grade {grade}.',
        src_ii='📚 Insulin index sources: Holt SH et al., Am J Clin Nutr 1997;66(5):1264–76 • Bao J et al., Am J Clin Nutr 2009;90(4):986–92.',
        src_link='Methodology & details →',
        disclaimer='Disclaimer: This guidance is for nutritional lifestyle orientation and does not constitute a diagnostic medical device under EU Regulation MDR 2017/745.',
        reviewed='Medically reviewed by <a href="{doctor}">Dr. Wassim Habib</a> · Last reviewed {date}',
        portion_note='The typical portion is approximate, for comparison purposes.',
        theme='Toggle theme', footer_rights='© 2026 WiBo Health Group. All rights reserved.',
        nav=('Home', 'Food Guide', 'Calculators', 'Supplements', 'Articles', 'boodi App 💚'), privacy='Privacy',
        methodology='Methodology & scientific references'),
    'nl': dict(
        dir='ltr', title='{name}: calorieën, glykemische index & voedingswaarde | WiBo Health',
        desc_measured='{name}: {kcal} kcal per 100 g, glykemische index {gi} ({level}) volgens Atkinson 2021, glykemische lading {gl} per portie van {p} g. Volledige voedingswaarden, tips en alternatieven.',
        desc_reviewed='{name}: {kcal} kcal per 100 g, glykemische index {gi} ({level}, klinisch beoordeelde schatting), glykemische lading {gl} per portie van {p} g. Volledige voedingswaarden, tips en alternatieven.',
        desc_na='{name}: {kcal} kcal en {protein} g eiwit per 100 g. Glykemische index niet van toepassing (minder dan 5 g beschikbare koolhydraten). Volledige voedingswaarden, tips en alternatieven.',
        home='Home', guide='Voedingswijzer', gi='Glykemische index', gl='Glykemische lading', kcal='Calorieën', protein='Eiwit',
        per100='per 100 g', per_portion='per portie van {p} g', na='Niet van toepassing', levels=('Laag', 'Gemiddeld', 'Hoog'),
        gram='g', kcal_unit='kcal', tips='💡 Slimme voedingsbegeleiding',
        tip_titles=('Consumptieadvies', 'Beste bereidingswijzen', 'Belangrijke voedingsnotitie'),
        table='Voedingswaarden', nutrient='Voedingsstof', col100='Per 100 g', colp='Per gangbare portie ({p} g)',
        rows=('Calorieën', 'Eiwit', 'Koolhydraten', 'Beschikbare koolhydraten', 'Vet', 'Voedingsvezels'),
        ii_row='Insuline-index', ii_tested='klinisch getest (Holt / Bao)',
        compare='Vergelijking & slimme alternatieven', alt_lower='Alternatieven met een lagere GI:',
        alt_same='Verwante producten uit dezelfde familie:', alt_family='Slimme alternatieven uit dezelfde familie:', lowest_note='Dit is een van de producten met de laagste GI in zijn groep.',
        rank_measured='Het staat op plaats {rank} van {m} gemeten producten in {group} op glykemische index (laagste eerst).',
        rank_protein='Het levert {v} g eiwit per 100 kcal en staat op plaats {rank} van {m} in {group} (hoogste eerst).',
        rank_kcal='Het bevat {v} kcal per 100 g en staat op plaats {rank} van {m} in {group} (laagste eerst).',
        lead_measured='Elke 100 g {name} bevat {kcal} kcal en {avail} g beschikbare koolhydraten. De glykemische index is {gi} ({level}), het gemiddelde van {studies} in de internationale GI-tabellen (Atkinson 2021). Een gangbare portie van {p} g heeft een glykemische lading van {gl} ({gl_level}).',
        lead_reviewed='Elke 100 g {name} bevat {kcal} kcal en {avail} g beschikbare koolhydraten. De glykemische index is {gi} ({level}), een klinisch beoordeelde schatting en geen laboratoriummeting. Een gangbare portie van {p} g heeft een glykemische lading van {gl} ({gl_level}).',
        gi_reviewed='Klinisch beoordeelde schatting',
        rank_reviewed='Van de producten in {group} met een glykemische index ({m}) staat het op plaats {rank} (laagste eerst).',
        src_reviewed='📚 De glykemische index van dit product is een klinisch beoordeelde schatting van het medisch team van WiBo Health, geen laboratoriummeting uit de internationale GI-tabellen (Atkinson 2021).',
        reviewed_team='Gecontroleerd door het medisch team van WiBo Health · Laatst gecontroleerd {date}',
        lead_na='Elke 100 g {name} bevat {kcal} kcal en {protein} g eiwit. Omdat het minder dan 5 g beschikbare koolhydraten per 100 g bevat, is de glykemische index niet van toepassing en is het directe effect op de bloedsuiker minimaal.',
        boodi_title='Scan barcodes in de supermarkt met de boodi-app 💚',
        boodi_text='boodi analyseert verpakte producten direct, controleert de halalstatus en stelt suikerarmere alternatieven uit hetzelfde schap voor.',
        boodi_btn='Ontdek de boodi-app',
        src_gi='📚 Wetenschappelijke bronnen: Internationale GI-tabellen (Atkinson et al., Am J Clin Nutr 2021) • Harvard Health Publishing.',
        src_value='Goedgekeurde waarde: gemiddelde van {studies} (bereik {lo}–{hi}), betrouwbaarheidsgraad {grade}.',
        src_ii='📚 Bronnen insuline-index: Holt SH et al., Am J Clin Nutr 1997;66(5):1264–76 • Bao J et al., Am J Clin Nutr 2009;90(4):986–92.',
        src_link='Methodologie & details →',
        disclaimer='Algemene disclaimer: Deze informatie is uitsluitend bedoeld als voedingsadvies en is geen medisch diagnostisch hulpmiddel volgens EU MDR 2017/745.',
        reviewed='Medisch gecontroleerd door <a href="{doctor}">dr. Wassim Habib</a> · Laatst gecontroleerd {date}',
        portion_note='De gangbare portie is een benadering, bedoeld om te vergelijken.',
        theme='Thema wisselen', footer_rights='© 2026 WiBo Health Group. Alle rechten voorbehouden.',
        nav=('Home', 'Voedingswijzer', 'Calculators', 'Supplementen', 'Artikelen', 'boodi App 💚'), privacy='Privacy',
        methodology='Methodologie & wetenschappelijke bronnen'),
}


FAQ = {
    'ar': dict(
        title='أسئلة شائعة',
        q=('هل {ya}ناسب {name} الدايت وإنقاص الوزن؟', 'كيف {ya}ؤثر {name} على سكر الدم؟', 'ما القيمة الغذائية لحصة معتادة من {name}؟'),
        w_high='يحتوي {name} على {kcal} سعرة لكل 100 غ، وهي كمية مرتفعة من السعرات، لذلك يُستحسن استخدام كميات صغيرة ومقاسة من{h} في نظام إنقاص الوزن؛ فحصة {p} غ تعطي {kcal_p} سعرة.',
        w_low='نعم، فسعرات {name} منخفضة جداً ({kcal} سعرة لكل 100 غ)، ويمكن تناول كمية جيدة من{h} لزيادة حجم الوجبة والشعور بالشبع دون سعرات كثيرة.',
        w_protein='يمكن أن {ya}كون جزءاً مفيداً من نظام إنقاص الوزن، لأن{h} {ya}وفر {ppk} غ بروتين لكل 100 سعرة، والبروتين يعزز الشبع. وحصة {p} غ تعطي {kcal_p} سعرة.',
        w_fiber='يمكن إدخال{h} باعتدال، ف{huwa} {ya}حتوي على {fiber} غ ألياف لكل 100 غ تساعد على الشبع، وحصة {p} غ تعطي {kcal_p} سعرة.',
        w_general='يمكن إدخال{h} ضمن نظام متوازن مع التحكم بالحصة: حصة {p} غ تعطي {kcal_p} سعرة، والمهم هو مجموع سعرات اليوم ونوعية بقية الوجبة.',
        s_measured='مؤشر{h} الجلايسيمي {gi} ({level}) وفق Atkinson 2021. وفي حصة معتادة من {p} غ يبلغ حمل{h} الجلايسيمي {gl} ({gl_level}){advice}',
        s_reviewed='مؤشر{h} الجلايسيمي {gi} ({level})، وهو تقدير مراجع سريرياً وليس قياساً مخبرياً. وفي حصة معتادة من {p} غ يبلغ حمل{h} الجلايسيمي {gl} ({gl_level}){advice}',
        s_advice=('، لذلك يكون تأثير هذه الحصة على سكر الدم محدوداً.', '، لذلك يُفضّل تناول{h} مع بروتين أو خضار غنية بالألياف.',
                  '، لذلك يُفضّل تقليل الحصة أو تقسيمها وتناول{h} مع البروتين والألياف.'),
        s_na_zero='لا يحتوي {name} تقريباً على كربوهيدرات متاحة، لذلك لا ينطبق علي{h} المؤشر الجلايسيمي، وأثر{h} المباشر على سكر الدم ضئيل. أما أثر الوجبة فتحدده الأطعمة المرافقة ل{h} كالخبز والأرز والصلصات المحلاة.',
        s_na='يحتوي {name} على {avail} غ فقط من الكربوهيدرات المتاحة لكل 100 غ، لذلك لا ينطبق علي{h} المؤشر الجلايسيمي، وأثر{h} المباشر على سكر الدم ضئيل. أما أثر الوجبة فتحدده الأطعمة المرافقة ل{h} كالخبز والأرز والصلصات المحلاة.',
        portion='حصة معتادة من {p} غ من {name} تحتوي تقريباً على {kcal_p} سعرة، و{prot_p} غ بروتين، و{carb_p} غ كربوهيدرات، و{fat_p} غ دهون، و{fib_p} غ ألياف.'),
    'en': dict(
        title='Frequently asked questions',
        q=('{Is_} {name} good for weight loss?', 'How {does} {name} affect blood sugar?', 'What is the nutritional value of a typical portion of {name}?'),
        w_high='{name} {provides} {kcal} kcal per 100 g, so it is high in calories and fits a weight-loss plan only in small, measured amounts; a {p} g portion gives {kcal_p} kcal.',
        w_low='Yes. {name} {is_} very low in calories ({kcal} kcal per 100 g), so you can eat a generous amount to add volume and fullness to a meal without many calories.',
        w_protein='It can be a useful part of a weight-loss plan because it provides {ppk} g of protein per 100 kcal, and protein supports fullness. A {p} g portion gives {kcal_p} kcal.',
        w_fiber='It can be included in moderation: it contains {fiber} g of fibre per 100 g, which supports fullness, and a {p} g portion gives {kcal_p} kcal.',
        w_general='It can fit a balanced plan with portion control: a {p} g portion gives {kcal_p} kcal, and what matters most is your total daily intake and the rest of the meal.',
        s_measured='Its glycemic index is {gi} ({level}) according to Atkinson 2021. A typical {p} g portion has a glycemic load of {gl} ({gl_level}){advice}',
        s_reviewed='Its glycemic index is {gi} ({level}), a clinically reviewed estimate rather than a laboratory measurement. A typical {p} g portion has a glycemic load of {gl} ({gl_level}){advice}',
        s_advice=(', so the effect of this portion on blood sugar is limited.', ', so it is best combined with protein or fibre-rich vegetables.',
                  ', so it is best to reduce or split the portion and combine it with protein and fibre.'),
        s_na='{name} {contains} only {avail} g of available carbohydrate per 100 g, so the glycemic index does not apply and its direct effect on blood sugar is minimal. The meal’s effect depends on what you eat with it, such as bread, rice or sweetened sauces.',
        s_na_zero='{name} {contains} virtually no available carbohydrate, so the glycemic index does not apply and its direct effect on blood sugar is minimal. The meal’s effect depends on what you eat with it, such as bread, rice or sweetened sauces.',
        portion='A typical {p} g portion of {name} provides about {kcal_p} kcal, {prot_p} g protein, {carb_p} g carbohydrate, {fat_p} g fat and {fib_p} g fibre.'),
    'nl': dict(
        title='Veelgestelde vragen',
        q=('{Is_} {name} geschikt om af te vallen?', 'Wat is het effect van {name} op de bloedsuiker?', 'Wat is de voedingswaarde van een gangbare portie {name}?'),
        w_high='{name} {levert} {kcal} kcal per 100 g en {is_} dus calorierijk; in een afvalplan past het alleen in kleine, afgemeten hoeveelheden. Een portie van {p} g geeft {kcal_p} kcal.',
        w_low='Ja. {name} {is_} zeer caloriearm ({kcal} kcal per 100 g), dus je kunt er royaal van eten om een maaltijd volume en verzadiging te geven zonder veel calorieën.',
        w_protein='Het kan een nuttig onderdeel zijn van een afvalplan, omdat het {ppk} g eiwit per 100 kcal levert en eiwit de verzadiging bevordert. Een portie van {p} g geeft {kcal_p} kcal.',
        w_fiber='Het past met mate: het bevat {fiber} g vezels per 100 g, wat de verzadiging ondersteunt, en een portie van {p} g geeft {kcal_p} kcal.',
        w_general='Het past in een evenwichtig eetpatroon met aandacht voor de portie: een portie van {p} g geeft {kcal_p} kcal, en het gaat vooral om je totale dagelijkse inname en de rest van de maaltijd.',
        s_measured='De glykemische index is {gi} ({level}) volgens Atkinson 2021. Een gangbare portie van {p} g heeft een glykemische lading van {gl} ({gl_level}){advice}',
        s_reviewed='De glykemische index is {gi} ({level}), een klinisch beoordeelde schatting en geen laboratoriummeting. Een gangbare portie van {p} g heeft een glykemische lading van {gl} ({gl_level}){advice}',
        s_advice=(', dus het effect van deze portie op de bloedsuiker is beperkt.', ', dus combineer het bij voorkeur met eiwit of vezelrijke groenten.',
                  ', dus verklein of verdeel de portie bij voorkeur en combineer haar met eiwit en vezels.'),
        s_na='{name} {bevat} slechts {avail} g beschikbare koolhydraten per 100 g, dus de glykemische index is niet van toepassing en het directe effect op de bloedsuiker is minimaal. Het effect van de maaltijd hangt af van wat je erbij eet, zoals brood, rijst of gezoete sauzen.',
        s_na_zero='{name} {bevat} vrijwel geen beschikbare koolhydraten, dus de glykemische index is niet van toepassing en het directe effect op de bloedsuiker is minimaal. Het effect van de maaltijd hangt af van wat je erbij eet, zoals brood, rijst of gezoete sauzen.',
        portion='Een gangbare portie van {p} g {name} levert ongeveer {kcal_p} kcal, {prot_p} g eiwit, {carb_p} g koolhydraten, {fat_p} g vet en {fib_p} g vezels.'),
}


PLURAL = {'en': {18, 19, 22, 53, 62, 63, 68, 20, 21, 23, 25, 28, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 99, 117, 142, 161, 162, 183, 184, 220, 232, 233, 234, 262, 267, 278, 292, 293, 302,
                 411, 412, 413, 414, 420, 424, 425,
                 426, 427, 428, 429, 430, 431, 432, 434, 435, 436, 437, 438, 439, 442, 443, 448, 449,
                 451, 465, 472, 476, 478, 479, 495,
                 504, 508, 510, 527, 543, 546},
          'nl': {17, 18, 19, 22, 40, 53, 62, 63, 68, 20, 21, 23, 24, 25, 28, 42, 45, 52, 56, 57, 58, 60, 80, 81, 82,
                 83, 84, 85, 87, 88, 89, 99, 100, 113, 117, 142, 151, 161, 162, 183, 220, 232, 233, 234, 235, 260, 276, 284, 292, 293, 302,
                 411, 412, 413, 423, 424, 425,
                 426, 427, 428, 429, 430, 431, 432, 434, 435, 436, 437, 438, 439, 440, 443, 448, 449,
                 451, 465, 472, 476, 478, 479, 495,
                 504, 508, 527, 543, 546}}
VERBS = {'en': (dict(is_='is', does='does', contains='contains', provides='provides'),
                dict(is_='are', does='do', contains='contain', provides='provide')),
         'nl': (dict(is_='is', bevat='bevat', levert='levert'), dict(is_='zijn', bevat='bevatten', levert='leveren')),
         'ar': (dict(), dict())}


def build_faq(food, lang, name, portion, measured, gi=None, lvl=None, gl=None, glv=None, g=None, reviewed=False):
    """Three questions whose answers are computed from the food's own numbers."""
    f, u = FAQ[lang], UI[lang]
    v = dict(VERBS[lang][1 if food['id'] in PLURAL.get(lang, set()) else 0])
    if 'is_' in v:
        v['Is_'] = v['is_'].capitalize()
    v.update(g or {})
    pf = portion / 100.0
    kcal = food['kcal']
    kcal_p = round(kcal * pf)
    ppk = food['protein'] / kcal * 100 if kcal else 0
    if kcal >= 400:
        w = f['w_high']
    elif kcal <= 60:
        w = f['w_low']
    elif ppk >= 8:
        w = f['w_protein']
    elif food['fiber'] >= 3:
        w = f['w_fiber']
    else:
        w = f['w_general']
    a1 = w.format(name=name, kcal=round(kcal), p=portion, kcal_p=kcal_p, ppk=fmt(ppk), fiber=fmt(food['fiber']), **v)
    if measured:
        a2 = f['s_reviewed' if reviewed else 's_measured'].format(gi=gi, level=u['levels'][lvl], p=portion, gl=fmt(gl), gl_level=u['levels'][glv],
                                    advice=f['s_advice'][glv].format(**v), **v)
    else:
        tmpl = f['s_na_zero'] if food['avail'] < 0.5 else f['s_na']
        a2 = tmpl.format(name=name, avail=fmt(food['avail']), **v)
    a3 = f['portion'].format(**v, p=portion, name=name, kcal_p=kcal_p, prot_p=fmt(food['protein'] * pf),
                             carb_p=fmt(food['carbs'] * pf), fat_p=fmt(food['fat'] * pf), fib_p=fmt(food['fiber'] * pf))
    return [(q.format(name=name, **v), a) for q, a in zip(f['q'], (a1, a2, a3))]


# --------------------------------------------------------------------------------------------
# Arabic: definite form (ال التعريف) and grammatical gender of a food name, for use inside sentences
# --------------------------------------------------------------------------------------------
AR_DEFINITE_OVERRIDES = {          # names whose natural definite form does not follow the rules
    'ملوخية ورق خضراء': 'الملوخية الخضراء',
    'لحم بقري ستيك مشوي': 'ستيك اللحم البقري المشوي',
    'بيض مسلوق كامل': 'البيض المسلوق',
    'حليب كامل الدسم 3.5%': 'الحليب كامل الدسم',
    'لبن زبادي يوناني 10%': 'الزبادي اليوناني',
    'رمان حب': 'حب الرمان',
    'جوز عين الجمل': 'الجوز',
    'بذور دوار الشمس (بزر سوري)': 'بذور دوار الشمس',
    'زبدة فول سوداني 100% طبيعية': 'زبدة الفول السوداني الطبيعية',
    'أومليت بيض بالزبدة': 'أومليت البيض بالزبدة',
    'كبدة عجل مشوية': 'كبدة العجل المشوية',
    'حمص بطحينة أصلي': 'الحمص بالطحينة',
    'متبل باذنجان (بابا غنوج)': 'متبل الباذنجان',
    'فتوش بالدبس وزيت الزيتون': 'الفتوش',
    'ملوخية ورق بالدجاج': 'الملوخية بالدجاج',
    'شاورما دجاج سوري': 'شاورما الدجاج',
    'شاورما لحم عجل': 'شاورما لحم العجل',
    'شيش طاووق مشوي': 'الشيش طاووق المشوي',
    'ورق عنب يالنجي بالزيت': 'ورق العنب بالزيت',
    'كوسا محشي باللحم والأرز': 'الكوسا المحشية باللحم والأرز',
    'مقلوبة دجاج بالباذنجان': 'مقلوبة الدجاج بالباذنجان',
    'مجدرة برغل بزيت الزيتون': 'مجدرة البرغل',
    'فتة حمص باللبن والمكسرات': 'فتة الحمص باللبن',
    'صيادية سمك بالبصل المحمر': 'صيادية السمك',
    'مسخن دجاج فلسطيني': 'مسخن الدجاج الفلسطيني',
    'شكشوكة بيض بالبندورة': 'شكشوكة البيض بالبندورة',
    'شوربة عدس سورية صفراء': 'شوربة العدس الصفراء',
    'زيت جوز هند بكر': 'زيت جوز الهند البكر',
    'طحينة سمسم سائلة': 'طحينة السمسم',
    'حليب اللوز غير محلى': 'حليب اللوز غير المحلى',
    'ماء جوز الهند الطبيعي': 'ماء جوز الهند الطبيعي',
    'عصير برتقال طازج': 'عصير البرتقال الطازج',
    'عصير رمان طبيعي': 'عصير الرمان الطبيعي',
    'بيج ماك': 'البيج ماك',
    'تشيكن ناغتس (6 قطع)': 'التشيكن ناغتس',
    'دجاج مقلي بروستد (KFC)': 'الدجاج المقلي (البروستد)',
    'بيتزا مارغريتا (شريحة)': 'بيتزا المارغريتا',
    'بيتزا بيبروني (شريحة)': 'بيتزا البيبروني',
    'ساندويش صب واي دجاج تيرياكي': 'ساندويش صب واي بالدجاج تيرياكي',
    'سلطة كول سلو': 'سلطة الكول سلو',
    'كرواسون زبدة فرنسي': 'الكرواسون بالزبدة',
    'تشيز كيك نيويورك': 'تشيز كيك نيويورك',
    'تاكو لحم بقري': 'تاكو اللحم البقري',
    'بوريتو دجاج وفاصوليا': 'بوريتو الدجاج والفاصوليا',
    'فاهيتا دجاج مع فلفل وبصل': 'فاهيتا الدجاج',
    'ناتشوز مقرمش بالجبن': 'الناتشوز بالجبن',
    'صلصة سالسا طماطم حارة': 'صلصة السالسا الحارة',
    'تشيلي كون كارني (لحم وفاصوليا)': 'التشيلي كون كارني',
    'سباغيتي كاربونارا': 'سباغيتي الكاربونارا',
    'سباغيتي بولونيز': 'سباغيتي البولونيز',
    'فيتوتشيني ألفريدو بالكريمة': 'فيتوتشيني ألفريدو بالكريمة',
    'سلطة كابريزي (موزاريلا وطماطم)': 'سلطة الكابريزي',
    'شوربة مينيستروني الإيطالية': 'شوربة المينيستروني الإيطالية',
    'سوشي سلمون رول': 'سوشي السلمون',
    'سوشي كاليفورنيا رول': 'سوشي كاليفورنيا رول',
    'ساشيمي سلمون نيء': 'ساشيمي السلمون النيء',
    'شوربة رامن يابانية بالدجاج': 'شوربة الرامن بالدجاج',
    'نودلز باد تاي تايلاندي': 'نودلز الباد تاي',
    'سبرنج رول خضار مقلي': 'السبرنج رول بالخضار',
    'شوربة ميسو اليابانية': 'شوربة الميسو اليابانية',
    'توفو صويا طبيعي': 'التوفو',
    'كيمتشي كوري حار ومخمر': 'الكيمتشي الكوري',
    'دجاج تكا ماسالا هندي': 'دجاج التكا ماسالا',
    'بالاك بانير (سبانخ وجبن هندي)': 'البالاك بانير',
    'برياني دجاج هندي متبل': 'برياني الدجاج',
    'شوربة دال عدس هندي': 'شوربة الدال',
    'فطيرة سبانخ شامية': 'فطيرة السبانخ',
    'فطيرة جبنة بلدية': 'فطيرة الجبنة',
    'لحم بعجين صفيحة شامية': 'اللحم بعجين',
    'مناقيش زعتر بلدي بزيت الزيتون': 'مناقيش الزعتر',
    'مناقيش جبنة عكاوي': 'مناقيش جبنة العكاوي',
    'ساندويش كلوب حبش وجبن': 'ساندويش الكلوب',
    'ساندويش تونة بالمايونيز والخس': 'ساندويش التونة',
    'بانيني حلومي مشوي وطماطم': 'بانيني الحلوم المشوي',
    'توست أفوكادو مع بيض مسلوق': 'توست الأفوكادو بالبيض',
    'شوربة خضار مشكلة طازجة': 'شوربة الخضار المشكلة',
    'شوربة دجاج بالشعيرية': 'شوربة الدجاج بالشعيرية',
    'شوربة قرع عسلي بالكريمة': 'شوربة القرع العسلي',
    'شوربة بروكلي كريمية': 'شوربة البروكلي الكريمية',
    'شوربة طماطم إيطالية محمصة': 'شوربة الطماطم المحمصة',
    'شوربة فريكة باللحم': 'شوربة الفريكة باللحم',
    'مسقعة باذنجان باللحمة المفرومة': 'مسقعة الباذنجان باللحمة المفرومة',
    'يخنة بامية باللحم والأرز': 'يخنة البامية باللحم',
    'يخنة فاصوليا خضراء باللحم': 'يخنة الفاصوليا الخضراء باللحم',
    'مفركة بطاطا بالبيض (شامية)': 'مفركة البطاطا بالبيض',
    'أرز بالشعيرية ومطبوخ بالسمن': 'الأرز بالشعيرية',
    'كفتة داوود باشا بصلصة البندورة': 'كفتة داوود باشا',
    'سلطة سيزر بالدجاج المشوي': 'سلطة السيزر بالدجاج المشوي',
    'سلطة كينوا بالأفوكادو والخضار': 'سلطة الكينوا بالأفوكادو',
    'سلطة جرجير بالرمان والجوز': 'سلطة الجرجير بالرمان والجوز',
    'سلطة بطاطا مسلوقة بالبقدونس': 'سلطة البطاطا المسلوقة بالبقدونس',
    'سلطة شمندر مسلوق بالليمون': 'سلطة الشمندر المسلوق',
    'سلطة تونة بالذرة والمايونيز الخفيف': 'سلطة التونة بالذرة',
    'دراغون فروت (فاكهة التنين)': 'فاكهة التنين',
    'باشن فروت (ماراكوجا)': 'الباشن فروت',
    'مشمش مجفف طبيعي': 'المشمش المجفف',
    'تين مجفف بلدي': 'التين المجفف',
    'توت غوجي بيري مجفف': 'توت الغوجي المجفف',
    'كركم طازج مبشور': 'الكركم الطازج',
    'هيل أخضر حب': 'الهيل الأخضر',
    'زعفران نقي': 'الزعفران',
    'سبيرولينا عضوية بودرة': 'بودرة السبيرولينا',
    'بروتين مصل اللبن (واي آيسوليت)': 'بروتين مصل اللبن',
    'طحين جوز الهند العضوي': 'طحين جوز الهند',
    'عصير خروب بلدي طبيعي': 'عصير الخروب',
    'سحلب ساخن بالقرفة والمكسرات': 'السحلب الساخن',
    'شاي كرك بالحليب والتوابل': 'شاي الكرك',
    'جاك فروت (خبزية)': 'الجاك فروت',
    'خبيزة برية مطبوخة بزيت الزيتون': 'الخبيزة البرية',
    'قرنبيط مقلي مقرمش بالكمون': 'القرنبيط المقلي بالكمون',
    'قرنفل مسامير حب': 'مسامير القرنفل',
    'ريحان مجفف بلدي': 'الريحان المجفف',
    'سماق بلدي حامض': 'السماق البلدي',
    'سمك البلطي الطازج المشوي': 'سمك البلطي المشوي',
    'سمك الهامور الفاخر': 'سمك الهامور',
    'أخطبوط مشوي بالزيت والليمون': 'الأخطبوط المشوي',
    'كافيار سمك أصلي فخم': 'الكافيار',
    'سمك أنشوفة مملح (Ansjovis)': 'سمك الأنشوفة المملح',
    'كبدة إسكندراني حارة بالفلفل': 'الكبدة الإسكندراني',
    'شاكرية لحم غنم باللبن والنشا': 'الشاكرية',
    'جريش سعودي بالسمن والبصل': 'الجريش',
    'عريكة ملكية بالتمر والعسل والسمن': 'العريكة',
    'خميرة غذائية مدعمة (Nutritional Yeast)': 'الخميرة الغذائية',
    'خل تفاح عضوي غير مفلتر مع الأم': 'خل التفاح',
    'بروتين بار بنكهة الشوكولاتة والكراميل': 'لوح البروتين',
    'خبز كيتو خالي من الجلوتين': 'خبز الكيتو',
    'معكرونة خالية من الجلوتين (أرز وذرة)': 'المعكرونة الخالية من الغلوتين',
    'دبس رمان طبيعي مركز بدون سكر': 'دبس الرمان',
    'صلصة صويا مخمرة طبيعياً (Kikkoman)': 'صلصة الصويا',
    'صلصة سريراتشا حارة': 'صلصة السريراتشا',
    'مخلل خيار بلدي مقرمش': 'مخلل الخيار',
    'زيتون كلاماتا يوناني أسود': 'زيتون كالاماتا',
    'بيرة عادية (Pilsener)': 'البيرة',
    'نبيذ أحمر جاف': 'النبيذ الأحمر',
    'مشروب عرق سوس بلدي طبيعي': 'عرق السوس',
    'شاي كركديه بارد أحمر': 'شاي الكركديه',
    'منقوع بابونج مهدئ للأعصاب': 'منقوع البابونج',
    'قهوة تركية بالهيل': 'القهوة التركية بالهيل',
    'شاي أخضر بالنعناع المغربي': 'الشاي الأخضر بالنعناع',
    'كرنب أجعد هولندي (بورنكول)': 'الكرنب الأجعد',
    'كرنب بروكسل (سبروتس)': 'كرنب بروكسل',
    'حليب خض مع خاثر (كارنملك)': 'حليب الخض',
    'كوارك خالي الدسم (ماخر كفارك)': 'الكوارك خالي الدسم',
    'كوارك كامل الدسم (فول كفارك)': 'الكوارك كامل الدسم',
    'خبز الجاودار الهولندي الخشن (روخه برود)': 'خبز الجاودار الهولندي',
}
AR_GENDER_OVERRIDES = {'حمص بطحينة أصلي': False, 'فاهيتا دجاج مع فلفل وبصل': True, 'لازانيا باللحم والبشاميل': True,
                       'بروسكيتا بالطماطم والريحان': True, 'مناقيش زعتر بلدي بزيت الزيتون': True,
                       'سمبوسك باللحمة المفرومة': False, 'ساندويش تونة بالمايونيز والخس': False,
                       'أرز بالشعيرية ومطبوخ بالسمن': False, 'دراغون فروت (فاكهة التنين)': True,
                       'سبيرولينا عضوية بودرة': True, 'قهوة عربية شقراء بالهيل': True,
                       'خرما (كاكا طازجة)': True, 'قرنفل مسامير حب': True, 'سمك أنشوفة مملح (Ansjovis)': False,
                       'عريكة ملكية بالتمر والعسل والسمن': True, 'خميرة غذائية مدعمة (Nutritional Yeast)': True,
                       'بروتين بار بنكهة الشوكولاتة والكراميل': False, 'معكرونة خالية من الجلوتين (أرز وذرة)': True,
                       'دبس رمان طبيعي مركز بدون سكر': False, 'صلصة صويا مخمرة طبيعياً (Kikkoman)': True,
                       'صلصة سريراتشا حارة': True, 'مخلل خيار بلدي مقرمش': False, 'زيتون كلاماتا يوناني أسود': False,
                       'بيرة عادية (Pilsener)': True, 'نبيذ أحمر جاف': False, 'مشروب عرق سوس بلدي طبيعي': False,
                       'منقوع بابونج مهدئ للأعصاب': False, 'قهوة تركية بالهيل': True,
                       'شاي أخضر بالنعناع المغربي': False}     # True = feminine; for names the head-noun rule gets wrong
AR_IDAFA = {('صدر', 'دجاج'), ('زيت', 'زيتون'), ('سمك', 'سلمون'), ('لحم', 'غنم'), ('خبز', 'قمح'),
            ('جبنة', 'شيدر'), ('جبنة', 'حلوم'), ('جبنة', 'موزاريلا'), ('جبنة', 'جودا'), ('جبنة', 'قريش')}        # construct state: only the second noun takes ال
AR_STOP = {'على', 'في', 'من', 'مع', 'عن', 'إلى', 'أبو', 'بدون'}   # prepositions / proper names: rest stays as is
AR_FEMININE_NOUNS = {'كمثرى', 'بطاطا', 'كوسا', 'مانجو', 'كينوا', 'سبانخ', 'فاصوليا', 'لوبيا', 'بذور', 'شاورما', 'بيتزا'}
AR_FEMININE_ADJ = {'بيضاء', 'سوداء', 'حمراء', 'خضراء', 'صفراء'}


def _core_words(name):
    name = re.sub(r'\(.*?\)', ' ', name)                     # drop parenthetical alternatives
    return [w for w in name.split() if '/' not in w]          # drop colour variants like أحمر/أخضر


def ar_definite(name):
    """'أرز أبيض مطبوخ' -> 'الأرز الأبيض المطبوخ'; 'صدر دجاج مشوي' -> 'صدر الدجاج المشوي'."""
    if name in AR_DEFINITE_OVERRIDES:
        return AR_DEFINITE_OVERRIDES[name]
    words = _core_words(name)
    out, frozen = [], False
    for i, w in enumerate(words):
        nxt = words[i + 1] if i + 1 < len(words) else ''
        if frozen or w in AR_STOP:
            frozen = True
            out.append(w)
        elif re.match(r'^[\d.%]+$', w) or w.startswith(('ال', 'بال', 'لل', 'وال')):
            out.append(w)
        elif (w, nxt) in AR_IDAFA or nxt.startswith('ال'):    # first noun of a construct stays indefinite
            out.append(w)
        else:
            out.append('ال' + w)
    return ' '.join(out)


def ar_is_feminine(name):
    if name in AR_GENDER_OVERRIDES:
        return AR_GENDER_OVERRIDES[name]
    words = _core_words(name)
    head = words[0] if words else ''
    if head.endswith('ة') or head in AR_FEMININE_NOUNS:
        return True
    return bool(len(words) > 1 and (words[1].endswith('ة') or words[1] in AR_FEMININE_ADJ))


def ar_pron(name):
    """Placeholders for Arabic templates: {h} = ه/ها (its), {ya} = ي/ت (verb prefix), {huwa} = هو/هي."""
    fem = ar_is_feminine(name)
    return dict(h='ها' if fem else 'ه', ya='ت' if fem else 'ي', huwa='هي' if fem else 'هو')


# --------------------------------------------------------------------------------------------
# Culinary-aware alternatives: each food's family, in order of preference (curated by hand).
# Measured foods list lower-GI options first; the heading says "lower GI" only when all are lower.
# --------------------------------------------------------------------------------------------
ALTERNATIVES = {
    1: [14, 2, 8], 14: [8, 9, 2], 2: [8, 9, 14], 8: [9, 18, 14], 9: [18, 8, 14], 10: [9, 8, 5], 5: [9, 18, 8],
    3: [4, 7, 17], 196: [4, 7, 17], 4: [7, 17, 8], 7: [17, 4, 8], 17: [7, 4, 8],
    11: [27, 19, 22], 26: [27, 18, 19], 29: [26, 27, 18], 27: [11, 19, 18],
    18: [19, 22, 9], 19: [18, 22, 9], 22: [18, 19, 8],
    54: [48, 66, 50], 51: [66, 48, 50], 49: [48, 66, 50], 53: [48, 66, 50], 55: [48, 66, 50],
    48: [66, 50, 55], 50: [48, 66, 55], 66: [48, 50, 55],
    62: [66, 48, 50], 63: [62, 66, 48], 68: [62, 48, 53],
    69: [70, 79, 71], 70: [69, 79, 71], 79: [69, 70, 72],
    101: [91, 98, 72], 91: [98, 94, 101], 92: [91, 94, 98], 93: [91, 92, 94], 94: [98, 91, 101], 98: [94, 91, 101],
    128: [59], 59: [128],
    71: [72, 79, 69], 72: [71, 77, 74], 74: [77, 72, 71], 77: [72, 74, 71],
    30: [31, 37, 32], 31: [30, 32, 35], 32: [39, 36, 30], 35: [36, 37, 32], 36: [35, 32, 40], 37: [38, 35, 30],
    38: [37, 39, 32], 39: [32, 38, 30], 40: [32, 35, 36],
    132: [133], 133: [132],
    # batch 2
    6: [15, 9, 8], 12: [13, 4, 196], 13: [12, 4, 7], 15: [9, 6, 8], 16: [8, 15, 9],
    20: [18, 19, 21], 21: [23, 22, 18], 23: [21, 18, 22], 24: [25, 19, 18], 25: [24, 89, 19],
    28: [27, 26, 36], 33: [32, 47, 36], 34: [30, 31, 47], 41: [42, 35, 37], 42: [35, 41, 37], 43: [34, 30, 33],
    44: [37, 31, 30], 45: [46, 30, 47], 46: [45, 30, 37], 47: [30, 31, 32],
    52: [57, 56, 48], 56: [57, 52, 58], 57: [52, 56, 58], 58: [57, 66, 52], 60: [58, 66, 65], 61: [52, 57, 48],
    64: [50, 52, 48], 65: [66, 48, 58], 67: [51, 65, 52],
    73: [76, 72, 77], 75: [74, 73, 77], 76: [71, 72, 73], 78: [128, 59],
    80: [81, 84, 83], 81: [80, 84, 83], 82: [80, 83, 89], 83: [80, 81, 87], 84: [80, 81, 83], 85: [86, 87, 88],
    86: [85, 87, 88], 87: [88, 85, 80], 88: [87, 85, 80], 89: [80, 25, 87], 90: [80, 89, 84],
    95: [94, 97, 99], 96: [100, 98, 94], 97: [94, 99, 95], 99: [97, 98, 94], 100: [96, 98, 91], 102: [101, 76, 95],
    # batch 3
    103: [91, 101, 92], 104: [107, 19, 106], 105: [104, 106, 19], 106: [20, 104, 18], 107: [104, 33, 108],
    108: [109, 9, 44], 109: [108, 107, 44], 110: [38, 113, 126], 111: [113, 112, 91], 112: [114, 111, 92],
    113: [91, 111, 114], 114: [113, 92, 112], 115: [116, 114, 121], 116: [115, 114, 121], 117: [118, 121, 108],
    118: [117, 32, 121], 119: [120, 123, 121], 120: [121, 123, 119], 121: [9, 18, 126], 122: [104, 106, 121],
    123: [94, 120, 121], 124: [113, 120, 111], 125: [101, 102, 106], 126: [18, 121, 106], 127: [121, 126, 18],
    129: [128, 78, 130], 130: [128, 129, 78], 131: [104, 128, 80], 134: [133, 132], 135: [70, 69, 79],
    136: [79, 70, 71], 137: [136, 135, 133], 138: [50, 64, 139], 139: [61, 138, 50], 140: [133, 136, 137],
    141: [146, 114, 113], 142: [143, 113, 91], 143: [142, 113, 91], 144: [145, 146, 104], 145: [144, 146, 141],
    146: [111, 144, 141], 147: [108, 109, 44], 148: [151, 152, 155], 149: [150, 148, 153], 150: [149, 151, 153],
    151: [62, 152, 148], 152: [131, 155, 151], 153: [154, 71, 155], 154: [153, 71, 155], 155: [152, 80, 151],
    # batch 4
    156: [4, 151, 157], 157: [71, 153, 155], 158: [161, 159, 163], 159: [161, 158, 165], 160: [161, 158, 163],
    161: [158, 165, 163], 162: [158, 163, 164], 163: [164, 59, 104], 164: [163, 30, 108], 165: [22, 161, 159],
    166: [168, 167, 175], 167: [168, 166, 5], 168: [6, 167, 166], 169: [167, 168, 6], 170: [5, 167, 14],
    171: [26, 6, 170], 172: [144, 166, 173], 173: [174, 200, 4], 174: [173, 73, 108], 175: [126, 193, 21],
    176: [178, 177, 94], 177: [176, 178, 59], 178: [94, 176, 95], 179: [183, 180, 185], 180: [179, 183, 181],
    181: [182, 113, 91], 182: [181, 113, 143], 183: [184, 179, 186], 184: [183, 176, 186], 185: [186, 126, 193],
    186: [187, 24, 189], 187: [186, 24, 25], 188: [109, 108, 185], 189: [190, 181, 113], 190: [189, 186, 37],
    191: [189, 14, 121], 192: [195, 194, 196], 193: [126, 18, 185], 194: [4, 192, 195], 195: [194, 196, 4],
    197: [198, 200, 37], 198: [197, 201, 200], 199: [197, 200, 202], 200: [201, 197, 199], 201: [200, 198, 197],
    202: [199, 197, 115], 203: [204, 206, 205], 204: [203, 206, 98], 205: [206, 204, 77], 206: [205, 204, 59],
    # batch 5
    207: [210, 216, 175], 208: [207, 126, 179], 209: [207, 210, 212], 210: [207, 211, 35], 211: [210, 207, 40],
    212: [207, 175, 209], 213: [126, 15, 208], 214: [33, 216, 220], 215: [216, 39, 110], 216: [215, 207, 214],
    217: [125, 26, 102], 218: [14, 9, 15], 219: [166, 168, 214], 220: [114, 214, 168],
    221: [222, 113, 224], 222: [221, 174, 224], 223: [8, 108, 222], 224: [44, 222, 109], 225: [26, 108, 223],
    226: [43, 224, 108], 227: [204, 221, 98],
    228: [64, 229, 230], 229: [228, 57, 64], 230: [228, 58, 53], 231: [228, 66, 65],
    # batch 6
    232: [234, 233, 235], 233: [232, 234, 63], 234: [232, 235, 233], 235: [232, 234, 57], 236: [237, 238, 241],
    237: [236, 238, 239], 238: [239, 237, 236], 239: [238, 249, 237], 240: [239, 238, 236], 241: [238, 236, 237],
    242: [243, 85, 86], 243: [242, 71, 76], 244: [245, 80, 85], 245: [244, 86, 85], 246: [247, 133, 136],
    247: [246, 133, 136], 248: [250, 153, 69], 249: [132, 133, 250], 250: [249, 133, 248], 251: [230, 256, 228],
    252: [50, 64, 254], 253: [255, 256, 55], 254: [252, 228, 64], 255: [253, 256, 55], 256: [251, 230, 228],
    # batch 7
    257: [258, 65, 48], 258: [257, 65, 232], 259: [228, 31, 229], 260: [56, 57, 85], 261: [264, 36, 31],
    262: [45, 207, 263], 263: [264, 44, 147], 264: [263, 261, 31], 265: [38, 37, 44], 266: [36, 33, 105],
    267: [239, 238, 268], 268: [238, 267, 239], 269: [241, 270, 272], 270: [269, 241, 236], 271: [272, 241, 85],
    272: [241, 271, 269], 273: [274, 96, 94], 274: [273, 96, 97], 275: [100, 276, 96], 276: [275, 100, 143],
    277: [95, 278, 94], 278: [99, 277, 97], 279: [103, 113, 114], 280: [122, 214, 104], 281: [119, 220, 113],
    # batch 8
    282: [121, 213, 15], 283: [151, 62, 152], 284: [243, 242, 85], 285: [289, 290, 292], 286: [243, 80, 155],
    287: [306, 4, 244], 288: [6, 5, 8], 289: [285, 139, 61], 290: [285, 289, 291], 291: [164, 290, 289],
    292: [293, 285, 31], 293: [128, 292, 59], 294: [297, 300, 133], 295: [53, 297, 139], 296: [297, 247, 246],
    297: [300, 298, 133], 298: [300, 297, 133], 299: [249, 132, 300], 300: [133, 298, 297], 301: [37, 35, 302],
    302: [35, 36, 301], 303: [79, 136, 70], 304: [305, 76, 71], 305: [304, 71, 76], 306: [4, 12, 287],
}


def ar_measured_items(n):
    """Arabic counted noun: 3-10 take a plural, 11+ a singular accusative."""
    if n == 1:
        return 'صنف مقاس واحد'
    if n == 2:
        return 'صنفين مقاسين'
    if 3 <= n <= 10:
        return f'{n} أصناف مقاسة'
    return f'{n} صنفاً مقاساً'


def studies_word(n, lang):
    if lang == 'ar':
        return {1: 'دراسة واحدة', 2: 'دراستين'}.get(n, f'{n} دراسات' if 3 <= n <= 10 else f'{n} دراسة')
    if lang == 'en':
        return '1 study' if n == 1 else f'{n} studies'
    return '1 studie' if n == 1 else f'{n} studies'


# --------------------------------------------------------------------------------------------
# Data
# --------------------------------------------------------------------------------------------
def load_foods():
    text = (ROOT / 'js' / 'data.js').read_text(encoding='utf-8')
    foods = {}
    for line in re.findall(r"\{\s*id:\s*\d+,[^\n]*", text):
        def s(k):
            m = re.search(r"\b%s:\s*'((?:[^'\\]|\\.)*)'" % k, line)
            return m.group(1).replace("\\'", "'") if m else ''

        def n(k):
            m = re.search(r"\b%s:\s*(-?[\d.]+|null)" % k, line)
            return None if not m or m.group(1) == 'null' else float(m.group(1))

        def arr(k):
            m = re.search(r"\b%s:\s*\[([^\]]*)\]" % k, line)
            return [float(x) for x in m.group(1).split(',')] if m and m.group(1).strip() else []

        fid = int(re.search(r'id:\s*(\d+)', line).group(1))
        foods[fid] = dict(
            id=fid, ar=s('name'), en=s('nameEn'), nl=s('nameNl'), image=s('image'), icon=s('icon'),
            gi=n('gi'), gi_status=s('gi_status'), gi_grade=s('gi_grade'), gi_n=n('gi_n'), gi_range=arr('gi_range'),
            ii=n('ii'), kcal=n('calories') or 0, protein=n('protein') or 0, carbs=n('carbs') or 0, fat=n('fat') or 0,
            fiber=n('fiber') or 0)
        foods[fid]['avail'] = round(max(0.0, foods[fid]['carbs'] - foods[fid]['fiber']), 1)
    return foods


def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


def fmt(x):
    x = round(x, 1)
    return str(int(x)) if float(x).is_integer() else str(x)


def gi_level(v):
    return 0 if v <= 55 else (1 if v < 70 else 2)


def gl_level(v):
    return 0 if v <= 10 else (1 if v < 20 else 2)


def esc(s):
    return html.escape(s, quote=True)


# --------------------------------------------------------------------------------------------
# Design system from doctor.html
# --------------------------------------------------------------------------------------------
doctor = (ROOT / 'doctor.html').read_text(encoding='utf-8').replace('\r\n', '\n')
BASE_CSS = re.search(r'    <style>\n(.*?)    </style>\n', doctor, re.S).group(1)
LOGO_SVG = re.search(r'(<svg class="brand-logo-svg".*?</svg>)', doctor, re.S).group(1)

PAGE_CSS = """
        a.lang-btn { text-decoration: none; }
        .food-page h1, .food-page h3, .food-page td, .boodi-card h2, .food-page strong { color: var(--text-main); }
        .food-page { max-width: 980px; }
        .breadcrumb { font-size: 0.85rem; color: var(--text-muted); margin-bottom: 18px; }
        .breadcrumb a { color: var(--text-muted); text-decoration: none; }
        .breadcrumb a:hover { color: var(--primary); }
        .food-hero { display: flex; gap: 24px; align-items: center; flex-wrap: wrap; margin-bottom: 18px; }
        .food-hero img, .food-hero .food-emoji {
            width: 150px; height: 150px; border-radius: 22px; object-fit: cover; flex-shrink: 0;
            border: 3px solid var(--primary-glow); box-shadow: var(--shadow); background: var(--bg-input);
        }
        .food-hero .food-emoji { display: flex; align-items: center; justify-content: center; font-size: 4rem; }
        .food-hero-text { flex: 1; min-width: 220px; }
        .food-hero-text h1 { font-size: 2rem; font-weight: 900; line-height: 1.3; margin-bottom: 4px; }
        .food-subtitle { color: var(--text-muted); font-weight: 600; }
        .group-chip {
            display: inline-block; margin-top: 10px; padding: 4px 14px; border-radius: 999px; font-size: 0.82rem;
            font-weight: 700; color: var(--primary); background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.25);
        }
        .lead { font-size: 1.04rem; margin: 6px 0 22px; }
        .reviewed { font-size: 0.85rem; color: var(--text-muted); margin: 12px 0 0; }
        .reviewed a { color: var(--primary); text-decoration: none; font-weight: 700; }
        .stat-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px; margin-bottom: 26px; }
        .stat-box {
            background: var(--bg-input); border: 1px solid var(--border-color); border-radius: var(--radius-md);
            padding: 16px 12px; text-align: center;
        }
        .stat-box h2 { font-size: 0.82rem; color: var(--text-muted); font-weight: 700; margin-bottom: 6px; }
        .stat-num { font-size: 2rem; font-weight: 900; line-height: 1.2; }
        .stat-num.low { color: #10b981; } .stat-num.medium { color: #f39c12; } .stat-num.high { color: #e74c3c; }
        .stat-num.muted { color: var(--text-muted); } .stat-num.kcal { color: #3498db; } .stat-num.protein { color: #9b59b6; }
        .stat-sub { font-size: 0.78rem; color: var(--text-muted); font-weight: 600; }
        .badge {
            display: inline-block; margin-top: 6px; padding: 2px 10px; border-radius: 999px; font-size: 0.72rem;
            font-weight: 700; border: 1px solid transparent;
        }
        .badge.low { background: rgba(16, 185, 129, 0.12); border-color: rgba(16, 185, 129, 0.45); color: #10b981; }
        .badge.medium { background: rgba(243, 156, 18, 0.12); border-color: rgba(243, 156, 18, 0.45); color: #f39c12; }
        .badge.high { background: rgba(231, 76, 60, 0.12); border-color: rgba(231, 76, 60, 0.45); color: #e74c3c; }
        .badge.neutral { background: rgba(148, 163, 184, 0.14); border-color: rgba(148, 163, 184, 0.45); color: var(--text-muted); }
        .tip-list { display: grid; gap: 12px; margin: 10px 0 26px; }
        .tip {
            background: var(--bg-input); border: 1px solid var(--border-color); border-inline-start: 4px solid var(--primary);
            border-radius: var(--radius-sm); padding: 14px 18px;
        }
        .tip h3 { font-size: 1rem; font-weight: 800; margin-bottom: 4px; display: flex; gap: 8px; align-items: center; }
        .tip.warn { border-inline-start-color: #f39c12; }
        .tip p { color: var(--text-muted); margin: 0; }
        .nutrition-table { width: 100%; border-collapse: collapse; margin: 10px 0 6px; font-size: 0.95rem; }
        .nutrition-table th, .nutrition-table td { padding: 11px 12px; border-bottom: 1px solid var(--border-color); text-align: start; }
        .nutrition-table th { color: var(--primary); font-weight: 800; background: rgba(16, 185, 129, 0.06); }
        .nutrition-table td:not(:first-child) { font-weight: 700; }
        .table-note { font-size: 0.8rem; color: var(--text-muted); margin-bottom: 26px; }
        .alt-list { list-style: none; display: grid; gap: 10px; margin: 10px 0 26px; padding: 0; }
        .alt-list a {
            display: flex; justify-content: space-between; gap: 12px; padding: 12px 16px; border-radius: var(--radius-sm);
            background: var(--bg-input); border: 1px solid var(--border-color); color: var(--text-main); text-decoration: none; font-weight: 700;
        }
        .alt-list a:hover { border-color: var(--primary); color: var(--primary); }
        .alt-list span { color: var(--text-muted); font-weight: 600; white-space: nowrap; }
        .faq-list { display: grid; gap: 12px; margin: 10px 0 26px; }
        .faq-item { background: var(--bg-input); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 14px 18px; }
        .faq-item h3 { font-size: 1rem; font-weight: 800; margin-bottom: 6px; }
        .faq-item p { color: var(--text-muted); margin: 0; }
        .boodi-card {
            display: flex; gap: 18px; align-items: center; justify-content: space-between; flex-wrap: wrap;
            padding: 22px 24px; border-radius: var(--radius-md); margin-bottom: 26px;
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.16), rgba(6, 182, 212, 0.12));
            border: 1px solid rgba(16, 185, 129, 0.35);
        }
        .boodi-card h2 { font-size: 1.15rem; font-weight: 800; margin-bottom: 4px; }
        .boodi-card p { color: var(--text-muted); margin: 0; }
        .boodi-btn {
            display: inline-flex; align-items: center; gap: 8px; padding: 11px 22px; border-radius: 30px; background: var(--primary);
            color: #ffffff; font-weight: 800; text-decoration: none; white-space: nowrap;
        }
        .boodi-btn:hover { background: var(--primary-hover); }
        .source-strip {
            background: var(--bg-input); border: 1px solid rgba(16, 185, 129, 0.35); border-inline-start: 4px solid var(--primary);
            border-radius: 14px; padding: 12px 16px; margin-bottom: 10px; color: var(--text-muted); font-size: 0.85rem;
            font-weight: 600; overflow-wrap: anywhere;
        }
        .source-strip a { color: var(--primary); font-weight: 800; text-decoration: none; white-space: nowrap; }
        .disclaimer-box {
            margin-top: 18px; padding: 14px 18px; border-radius: 12px; background: rgba(15, 23, 42, 0.62);
            border: 1px solid rgba(226, 232, 240, 0.22); color: #e2e8f0; font-size: 0.85rem; text-align: center;
        }
        html[data-theme="light"] .disclaimer-box { background: #f1f5f9; border-color: rgba(15, 23, 42, 0.12); color: #334155; }
        @media (max-width: 760px) {
            .stat-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
            .food-hero { flex-direction: column; text-align: center; }
            .food-hero-text h1 { font-size: 1.6rem; }
        }
"""


def page_url(slug, lang, absolute=True):
    path = f'/foods/{slug}.html' if lang == 'ar' else f'/{lang}/foods/{slug}.html'
    return SITE + path if absolute else path


def site_link(path, lang):
    """Link to a regular site page in the reader's language."""
    if lang == 'ar':
        return path
    path, hash_, frag = path.partition('#')  # the query must sit before an #anchor
    return f"{path}{'&' if '?' in path else '?'}lang={lang}{hash_}{frag}"


# --------------------------------------------------------------------------------------------
# Page builder
# --------------------------------------------------------------------------------------------
def build(food, lang, ctx):
    u = UI[lang]
    li = LANGS.index(lang)
    slug, group, portion = ctx['slug'][food['id']], PILOT[food['id']][0], PILOT[food['id']][1]
    name = food[lang] or food['en']
    # inside Arabic sentences the name takes the definite article; headings keep the display name
    sname = ar_definite(name) if lang == 'ar' else name
    g = ar_pron(name) if lang == 'ar' else {}
    subtitle = {'ar': food['en'], 'en': food['nl'], 'nl': food['en']}[lang]
    if subtitle == name:
        subtitle = ''
    group_name = GROUPS[group][li]
    measured = food['gi_status'] == 'measured' and food['gi'] is not None      # Atkinson 2021
    reviewed = food['gi_status'] == 'reviewed' and food['gi'] is not None      # clinically reviewed estimate
    has_gi = measured or reviewed
    team = food['id'] in TEAM_REVIEW
    p_factor = portion / 100.0
    tips = list(ctx['overrides'].get(str(food['id']), {}).get('tips', {}).get(lang) or TIPS[group][li])
    if len(tips) == 2:                      # food-specific consumption + preparation; keep the approved note
        tips.append(TIPS['drink'][li][2] if food['id'] in CAFFEINE else (CARB_NOTE if has_gi else NA_NOTE)[li])

    # -------- numbers
    kcal, protein, avail = round(food['kcal']), fmt(food['protein']), fmt(food['avail'])
    if reviewed:
        gi = int(food['gi'])
        lvl = gi_level(gi)
        gl = round(gi * food['avail'] * p_factor / 100, 1)
        glv = gl_level(gl)
        lead = u['lead_reviewed'].format(name=sname, kcal=kcal, avail=avail, gi=gi, level=u['levels'][lvl], p=portion,
                                         gl=fmt(gl), gl_level=u['levels'][glv], **g)
        desc = u['desc_reviewed'].format(name=name, kcal=kcal, gi=gi, level=u['levels'][lvl], gl=fmt(gl), p=portion)
    elif measured:
        gi = int(food['gi'])
        lvl = gi_level(gi)
        gl = round(gi * food['avail'] * p_factor / 100, 1)
        glv = gl_level(gl)
        studies = studies_word(int(food['gi_n'] or 1), lang)
        lead = u['lead_measured'].format(name=sname, kcal=kcal, avail=avail, gi=gi, level=u['levels'][lvl], studies=studies,
                                         p=portion, gl=fmt(gl), gl_level=u['levels'][glv], **g)
        desc = u['desc_measured'].format(name=name, kcal=kcal, gi=gi, level=u['levels'][lvl], gl=fmt(gl), p=portion)
    else:
        lead = u['lead_na'].format(name=sname, kcal=kcal, protein=protein, **g)
        desc = u['desc_na'].format(name=name, kcal=kcal, protein=protein)
    # a doctor-approved introduction replaces the computed lead (the numbers stay in the cards and table)
    lead = ctx['overrides'].get(str(food['id']), {}).get('lead', {}).get(lang) or lead
    title = u['title'].format(name=name)

    # -------- FAQ (answers computed from the numbers, unless doctor-approved questions are given)
    faq_override = ctx['overrides'].get(str(food['id']), {}).get('faq', {}).get(lang)
    if faq_override:
        faq = [(item['q'], item['a']) for item in faq_override]
    elif has_gi:
        faq = build_faq(food, lang, sname, portion, True, gi=gi, lvl=lvl, gl=gl, glv=glv, g=g, reviewed=reviewed)
    else:
        faq = build_faq(food, lang, sname, portion, False, g=g)
    faq_html = ''.join(f'<div class="faq-item"><h3>{esc(q)}</h3><p>{esc(a)}</p></div>' for q, a in faq)
    faq_schema = {
        "@context": "https://schema.org", "@type": "FAQPage", "inLanguage": lang,
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq],
    }

    # -------- comparison & alternatives (within the pilot group)
    peers = [ctx['foods'][i] for i, (g, _) in PILOT.items() if g == group]
    def link_item(f, right):
        return (f'<li><a href="{page_url(ctx["slug"][f["id"]], lang, absolute=False)}">{esc(f[lang] or f["en"])}'
                f'<span>{right}</span></a></li>')
    family = [ctx['foods'][i] for i in ALTERNATIVES.get(food['id'], []) if i in PILOT]
    def gi_of(f):
        return f['gi'] if f['gi_status'] in ('measured', 'reviewed') and f['gi'] is not None else None
    if has_gi:
        if measured:                        # measured foods are ranked among measured foods only
            ranked = sorted([f for f in peers if f['gi_status'] == 'measured'], key=lambda f: f['gi'])
            rank = [f['id'] for f in ranked].index(food['id']) + 1
            compare_txt = u['rank_measured'].format(rank=rank, m=len(ranked), m_items=ar_measured_items(len(ranked)),
                                                    group=group_name, **g)
        else:
            ranked = sorted([f for f in peers if gi_of(f) is not None], key=gi_of)
            rank = [f['id'] for f in ranked].index(food['id']) + 1
            compare_txt = u['rank_reviewed'].format(rank=rank, m=len(ranked), group=group_name, **g)
        if rank == 1:
            compare_txt += ' ' + u['lowest_note']
        lower = sorted([f for f in family if gi_of(f) is not None and gi_of(f) < food['gi']], key=gi_of)
        alts = (lower + [f for f in family if f not in lower])[:3]
        alt_title = u['alt_lower'] if alts and len(lower) == len(alts) else u['alt_family']
        alt_html = ''.join(link_item(f, f"{u['gi']} {int(gi_of(f))}" if gi_of(f) is not None
                                     else f"{round(f['kcal'])} {u['kcal_unit']}") for f in alts)
    else:
        if group in ('protein', 'dairy_solid'):
            key = lambda f: -(f['protein'] / f['kcal'] * 100 if f['kcal'] else 0)
            ranked = sorted(peers, key=key)
            v = fmt(food['protein'] / food['kcal'] * 100) if food['kcal'] else '0'
            tmpl = u['rank_protein']
        else:
            ranked = sorted(peers, key=lambda f: f['kcal'])
            v = str(kcal)
            tmpl = u['rank_kcal']
        rank = [f['id'] for f in ranked].index(food['id']) + 1
        compare_txt = tmpl.format(v=v, rank=rank, m=len(ranked), group=group_name, **g)
        alt_title = u['alt_same']
        alt_html = ''.join(link_item(f, f"{round(f['kcal'])} {u['kcal_unit']}") for f in family[:3])

    # -------- cards
    if has_gi:
        gi_card = (f'<div class="stat-num {["low", "medium", "high"][lvl]}">{gi}</div>'
                   f'<span class="badge {["low", "medium", "high"][lvl]}">{u["levels"][lvl]}</span>')
        if reviewed:
            gi_card += f'<div class="stat-sub">{u["gi_reviewed"]}</div>'
        gl_card = (f'<div class="stat-num {["low", "medium", "high"][glv]}">{fmt(gl)}</div>'
                   f'<div class="stat-sub">{u["per_portion"].format(p=portion)}</div>')
    else:
        gi_card = f'<div class="stat-num muted">—</div><span class="badge neutral">{u["na"]}</span>'
        gl_card = f'<div class="stat-num muted">—</div><span class="badge neutral">{u["na"]}</span>'

    # -------- nutrition table
    def row(label, v100, unit):
        return (f'<tr><td>{label}</td><td>{fmt(v100)} {unit}</td><td>{fmt(v100 * p_factor)} {unit}</td></tr>')
    rows = ''.join([
        row(u['rows'][0], food['kcal'], u['kcal_unit']), row(u['rows'][1], food['protein'], u['gram']),
        row(u['rows'][2], food['carbs'], u['gram']), row(u['rows'][3], food['avail'], u['gram']),
        row(u['rows'][4], food['fat'], u['gram']), row(u['rows'][5], food['fiber'], u['gram'])])
    if food['ii'] is not None:
        rows += f'<tr><td>{u["ii_row"]}</td><td colspan="2">{int(food["ii"])} · {u["ii_tested"]}</td></tr>'

    # -------- sources
    method_href = site_link('/methodology.html', lang)
    src = f'<div class="source-strip">{u["src_gi"]} <a href="{method_href}">{u["src_link"]}</a></div>'
    if measured:
        rng = food['gi_range'] or [food['gi'], food['gi']]
        src = (f'<div class="source-strip">{u["src_gi"]}<br>' +
               u['src_value'].format(studies=studies_word(int(food['gi_n'] or 1), lang), lo=int(rng[0]), hi=int(rng[-1]),
                                     grade=food['gi_grade'] or '-') +
               f' <a href="{method_href}">{u["src_link"]}</a></div>')
    elif reviewed:
        src = f'<div class="source-strip">{u["src_reviewed"]} <a href="{method_href}">{u["src_link"]}</a></div>'
    if food['ii'] is not None:
        src += f'<div class="source-strip">{u["src_ii"]}</div>'

    # -------- head: SEO
    urls = {l: page_url(slug, l) for l in LANGS}
    image_abs = f'{SITE}/{food["image"]}' if food['image'] else f'{SITE}/images/logo.png'
    hreflang = '\n'.join(f'    <link rel="alternate" hreflang="{l}" href="{urls[l]}">' for l in LANGS)
    # Educational page, never a Product: Google requires offers/review/aggregateRating on Product,
    # which an information site cannot give (Search Console error, pages left unindexed).
    schema = {
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "@id": urls[lang] + '#webpage',
        "url": urls[lang],
        "name": title,
        "description": desc,
        "inLanguage": lang,
        "primaryImageOfPage": {"@type": "ImageObject", "url": image_abs},
        "about": {"@type": "Thing", "name": food['en'], "alternateName": [food['ar'], food['nl']]},
        "isPartOf": {"@type": "WebSite", "name": "WiBo Health", "url": SITE + '/'},
        "author": {"@type": "Person", "@id": f"{SITE}/doctor.html#wassim-habib", "name": "Dr. Wassim Habib",
                   "jobTitle": "Medical Doctor", "url": f"{SITE}/doctor.html"},
        "publisher": {"@type": "Organization", "name": "WiBo Health", "url": SITE,
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/images/icon-512.png"}},
        "reviewedBy": ({"@type": "Organization", "name": "WiBo Health medical team", "url": SITE + '/'} if team else
                       {"@type": "Person", "@id": f"{SITE}/doctor.html#wassim-habib", "name": "Wassim Habib",
                        "url": f"{SITE}/doctor.html"}),
        "lastReviewed": TEAM_REVIEWED if team else REVIEWED,
        "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u['home'], "item": SITE + site_link('/', lang)},
            {"@type": "ListItem", "position": 2, "name": u['guide'], "item": SITE + site_link('/foods.html', lang)},
            {"@type": "ListItem", "position": 3, "name": name, "item": urls[lang]}]},
    }

    nav_paths = ['/', '/foods.html', '/calculators.html', '/supplements.html', '/#articles', '/boodi.html']
    nav = '\n'.join(f'                <a href="{site_link(p, lang)}" class="nav-link">{label}</a>'
                    for p, label in zip(nav_paths, u['nav']))
    lang_links = '\n'.join(
        f'                    <a class="lang-btn{" active" if l == lang else ""}" href="{page_url(slug, l, absolute=False)}" '
        f'hreflang="{l}" lang="{l}"><span>{flag}</span> <span>{l.upper()}</span></a>'
        for l, flag in (('ar', '🇪🇬'), ('nl', '🇳🇱'), ('en', '🇬🇧')))
    img_html = (f'<img src="/{food["image"]}" alt="{esc(name)}" width="350" height="350">' if food['image']
                else f'<div class="food-emoji" aria-hidden="true">{food["icon"] or "🍽️"}</div>')
    tip_icons = ('fa-check-circle', 'fa-utensils', 'fa-triangle-exclamation')
    tips_html = ''.join(
        f'<div class="tip{" warn" if i == 2 else ""}"><h3><i class="fas {tip_icons[i]}"></i> {u["tip_titles"][i]}</h3>'
        f'<p>{esc(tips[i])}</p></div>' for i in range(3))
    footer_links = ' <span>•</span> '.join(
        f'<a href="{site_link(p, lang)}">{label}</a>' for p, label in
        [('/', u['nav'][0]), ('/foods.html', u['nav'][1]), ('/methodology.html', u['methodology']),
         ('/doctor.html', 'Dr. Wassim Habib' if lang != 'ar' else 'د. وسيم حبيب'), ('/privacy.html', u['privacy'])])

    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{u["dir"]}" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(title)}</title>
    <meta name="description" content="{esc(desc)}">
    <link rel="canonical" href="{urls[lang]}">
{hreflang}
    <link rel="alternate" hreflang="x-default" href="{urls['ar']}">
    <meta property="og:type" content="article">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(desc)}">
    <meta property="og:url" content="{urls[lang]}">
    <meta property="og:image" content="{image_abs}">
    <meta property="og:locale" content="{dict(ar='ar_AR', en='en_US', nl='nl_NL')[lang]}">
    <script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=4)}
    </script>
    <script type="application/ld+json">
{json.dumps(faq_schema, ensure_ascii=False, indent=4)}
    </script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#0f172a">
    <link rel="icon" type="image/png" sizes="192x192" href="/images/icon-192.png">
    <link rel="apple-touch-icon" href="/images/apple-touch-icon.png">
    <!-- Theme boot: one theme for the whole site (saved choice, else the OS setting), set before the first paint -->
    <script>(function(h){{var t;try{{t=localStorage.getItem('wibo_theme')}}catch(e){{}}if(t!=='dark'&&t!=='light'){{t=window.matchMedia&&matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';try{{localStorage.setItem('wibo_theme',t)}}catch(e){{}}}}h.setAttribute('data-theme',t)}})(document.documentElement);</script>
    <!-- Instant theme toggle: while light/dark flips, every transition is disabled so the switch paints in a single frame (0ms) -->
    <style>html.theme-transitioning,html.theme-transitioning *,html.theme-transitioning *::before,html.theme-transitioning *::after{{transition:none!important;animation-duration:0s!important}}</style>
    <script>document.addEventListener('click',function(e){{var t=e.target&&e.target.closest&&e.target.closest('.theme-toggle,.theme-toggle-btn,#themeToggle,#themeToggleBtn,#darkModeToggle,[onclick*="toggleTheme"]');if(!t)return;var h=document.documentElement;h.classList.add('theme-transitioning');cancelAnimationFrame(window.__tsw);window.__tsw=requestAnimationFrame(function(){{window.__tsw=requestAnimationFrame(function(){{h.classList.remove('theme-transitioning')}})}})}},true);</script>
    <style>
{BASE_CSS}{PAGE_CSS}    </style>
    <link rel="stylesheet" href="/css/unified-header.css">
</head>
<body>
    <header>
        <div class="header-container">
            <a href="{site_link('/', lang)}" class="brand-link">
                {LOGO_SVG}
                <span class="brand-title">WiBo Health</span>
            </a>
            <nav class="nav-links-bar">
{nav}
            </nav>
            <div class="header-actions">
                <button type="button" class="theme-toggle-btn" onclick="toggleTheme()" title="{u["theme"]}" aria-label="{u["theme"]}">
                    <i class="fas fa-sun" id="themeIcon"></i>
                </button>
                <div class="lang-switcher-container">
{lang_links}
                </div>
            </div>
        </div>
    </header>

    <main class="page-wrapper food-page">
        <article class="about-card">
            <nav class="breadcrumb" aria-label="breadcrumb">
                <a href="{site_link('/', lang)}">{u["home"]}</a> › <a href="{site_link('/foods.html', lang)}">{u["guide"]}</a> › <span>{esc(name)}</span>
            </nav>

            <div class="food-hero">
                {img_html}
                <div class="food-hero-text">
                    <h1>{esc(name)}</h1>
                    {f'<div class="food-subtitle">{esc(subtitle)}</div>' if subtitle else ''}
                    <span class="group-chip">{group_name}</span>
                </div>
            </div>

            <p class="lead">{esc(lead)}</p>

            <section class="stat-grid" aria-label="{u["gi"]}">
                <div class="stat-box"><h2>{u["gi"]}</h2>{gi_card}</div>
                <div class="stat-box"><h2>{u["gl"]}</h2>{gl_card}</div>
                <div class="stat-box"><h2>{u["kcal"]}</h2><div class="stat-num kcal">{kcal}</div><div class="stat-sub">{u["kcal_unit"]} {u["per100"]}</div></div>
                <div class="stat-box"><h2>{u["protein"]}</h2><div class="stat-num protein">{protein}</div><div class="stat-sub">{u["gram"]} {u["per100"]}</div></div>
            </section>

            <h2 class="section-title"><span>{u["tips"]}</span></h2>
            <div class="tip-list">{tips_html}</div>

            <h2 class="section-title"><i class="fas fa-table-list"></i> <span>{u["table"]}</span></h2>
            <table class="nutrition-table">
                <thead><tr><th>{u["nutrient"]}</th><th>{u["col100"]}</th><th>{u["colp"].format(p=portion)}</th></tr></thead>
                <tbody>{rows}</tbody>
            </table>
            <p class="table-note">{u["portion_note"]}</p>

            <h2 class="section-title"><i class="fas fa-scale-balanced"></i> <span>{u["compare"]}</span></h2>
            <p>{esc(compare_txt)}</p>
            <p><strong>{alt_title}</strong></p>
            <ul class="alt-list">{alt_html}</ul>

            <h2 class="section-title"><i class="fas fa-circle-question"></i> <span>{FAQ[lang]["title"]}</span></h2>
            <section class="faq-list">{faq_html}</section>

            <aside class="boodi-card">
                <div>
                    <h2>{u["boodi_title"]}</h2>
                    <p>{u["boodi_text"]}</p>
                </div>
                <a class="boodi-btn" href="{site_link('/boodi.html', lang)}"><i class="fas fa-barcode"></i> {u["boodi_btn"]}</a>
            </aside>

            {src}
            <p class="reviewed">{u["reviewed_team"].format(date=TEAM_REVIEWED_TXT[lang]) if team else u["reviewed"].format(doctor=site_link('/doctor.html', lang), date=REVIEWED_TXT[lang])}</p>
            <p class="disclaimer-box">{u["disclaimer"]}</p>
        </article>
    </main>

    <footer>
        <div class="footer-links">{footer_links}</div>
        <p>{u["footer_rights"]}</p>
    </footer>

    <script>
        function applyTheme(theme) {{
            document.documentElement.setAttribute('data-theme', theme);
            var icon = document.getElementById('themeIcon');
            if (icon) icon.className = theme === 'light' ? 'fas fa-moon' : 'fas fa-sun';
        }}
        function toggleTheme() {{
            var next = (document.documentElement.getAttribute('data-theme') || 'dark') === 'dark' ? 'light' : 'dark';
            applyTheme(next);
            try {{ localStorage.setItem('wibo_theme', next); }} catch (e) {{}}
        }}
        applyTheme(document.documentElement.getAttribute('data-theme') || 'dark');
        try {{ localStorage.setItem('preferred_language', '{lang}'); localStorage.setItem('wibo_language', '{lang}'); }} catch (e) {{}}
    </script>
</body>
</html>
'''


# --------------------------------------------------------------------------------------------
def main():
    foods = load_foods()
    overrides_path = ROOT / 'scripts' / 'food_pages_overrides.json'
    overrides = json.loads(overrides_path.read_text(encoding='utf-8')).get('foods', {}) if overrides_path.exists() else {}
    missing = [i for i in PILOT if i not in foods]
    assert not missing, f'unknown food ids: {missing}'
    slugs = {i: overrides.get(str(i), {}).get('slug') or SLUG_OVERRIDES.get(i) or slugify(foods[i]['en']) for i in PILOT}
    assert len(set(slugs.values())) == len(slugs), 'duplicate slugs'
    ctx = dict(foods=foods, slug=slugs, overrides=overrides)

    written = 0
    for fid in PILOT:
        for lang in LANGS:
            out = ROOT / (f'foods/{slugs[fid]}.html' if lang == 'ar' else f'{lang}/foods/{slugs[fid]}.html')
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(build(foods[fid], lang, ctx), encoding='utf-8', newline='\n')
            written += 1

    # id -> slug map for foods.html / food-details.html
    (ROOT / 'js' / 'food-pages.js').write_text(
        '// Generated by scripts/generate_food_pages.py - do not edit by hand.\n'
        '// Food id -> slug of its static page (/foods/<slug>.html, /en/foods/..., /nl/foods/...).\n'
        f'window.FOOD_PAGES = {json.dumps({str(k): v for k, v in sorted(slugs.items())}, separators=(",", ":"))};\n',
        encoding='utf-8', newline='\n')

    # sitemap block with hreflang alternates
    sm_path = ROOT / 'sitemap.xml'
    sm = sm_path.read_text(encoding='utf-8')
    eol = '\r\n' if '\r\n' in sm else '\n'
    if 'xmlns:xhtml' not in sm:
        sm = sm.replace('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
                        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">', 1)
    sm = re.sub(r'\s*<!-- FOOD-PAGES:START -->.*?<!-- FOOD-PAGES:END -->', '', sm, flags=re.S)
    block = ['  <!-- FOOD-PAGES:START -->']
    for fid in PILOT:
        for lang in LANGS:
            block += ['  <url>', f'    <loc>{page_url(slugs[fid], lang)}</loc>', f'    <lastmod>{TEAM_REVIEWED if fid in TEAM_REVIEW else REVIEWED}</lastmod>',
                      '    <changefreq>monthly</changefreq>', '    <priority>0.7</priority>']
            block += [f'    <xhtml:link rel="alternate" hreflang="{l}" href="{page_url(slugs[fid], l)}"/>' for l in LANGS]
            block += [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{page_url(slugs[fid], "ar")}"/>', '  </url>']
    block.append('  <!-- FOOD-PAGES:END -->')
    sm = sm.replace('</urlset>', eol.join(block) + eol + '</urlset>', 1)
    sm_path.write_text(sm, encoding='utf-8', newline='')

    print(f'pages written: {written} ({len(PILOT)} foods x {len(LANGS)} languages)')
    print('measured:', sum(1 for i in PILOT if foods[i]['gi_status'] == 'measured'),
          '| reviewed:', sum(1 for i in PILOT if foods[i]['gi_status'] == 'reviewed'),
          '| not applicable:', sum(1 for i in PILOT if foods[i]['gi_status'] == 'not_applicable'))


if __name__ == '__main__':
    main()
