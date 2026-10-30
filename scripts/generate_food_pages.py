"""Generate static, crawlable food pages (pilot batch) in three languages.

    python scripts/generate_food_pages.py

Output (re-running rebuilds everything, nothing is appended twice):
    foods/<slug>.html            Arabic (x-default)
    en/foods/<slug>.html         English
    nl/foods/<slug>.html         Dutch
    sv/foods/<slug>.html         Swedish, only for the foods in food_sv.PUBLISH (copy and names in scripts/food_sv.py;
                                 links to pages without a Swedish version open in English)
    js/food-pages.js             id -> slug map used by foods.html / food-details.html
    sitemap.xml                  block between <!-- FOOD-PAGES:START --> and <!-- FOOD-PAGES:END -->

Sources: js/data.js (values, GI provenance), doctor.html (design system: CSS, logo, nav labels).
Per-food text can be overridden in scripts/food_pages_overrides.json (lead, tips, faq, slug, title, desc).
"""
import hashlib
import html
import json
import re
import sys
from pathlib import Path

import food_sv as FSV

GA_TAG = """    <!-- Google tag (gtag.js) with Consent Mode v2: everything stays denied until the visitor accepts (js/consent.js) -->
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('consent', 'default', {'ad_storage': 'denied', 'ad_user_data': 'denied', 'ad_personalization': 'denied', 'analytics_storage': 'denied', 'wait_for_update': 500});
      try { if (localStorage.getItem('wibo_consent') === 'granted') gtag('consent', 'update', {'ad_storage': 'granted', 'ad_user_data': 'granted', 'ad_personalization': 'granted', 'analytics_storage': 'granted'}); } catch (e) {}
    </script>
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-WG6S4KXXJS"></script>
    <script>
      gtag('js', new Date());

      gtag('config', 'G-WG6S4KXXJS');
    </script>
    <script src="/js/consent.js?v=1" defer></script>"""   # GA4 property of wibohealth.com, first thing in every <head>


ROOT = Path(__file__).resolve().parent.parent
SITE = 'https://wibohealth.com'
REVIEWED = '2026-10-12'
REVIEWED_TXT = {'ar': '12 أكتوبر 2026', 'en': '12 October 2026', 'nl': '12 oktober 2026'}
TEAM_REVIEWED = '2026-10-13'             # batch 2: reviewed by the WiBo Health medical team
TEAM_REVIEWED_TXT = {'ar': '13 أكتوبر 2026', 'en': '13 October 2026', 'nl': '13 oktober 2026'}
LANGS = ('ar', 'en', 'nl')
SV = 'sv'
# Dr. Wassim Habib's jobTitle in every JSON-LD block, by page language (user decision 2026-10-30: the same role everywhere,
# no "medical director / medicinskt ansvarig" title)
JOB_TITLE = {'ar': 'مؤسس WiBo Health', 'en': 'Founder, WiBo Health', 'nl': 'Oprichter, WiBo Health', 'sv': 'Grundare, WiBo Health'}
ALL_LANGS = LANGS + (SV,)        # Swedish is opt-in per food (food_sv.PUBLISH); LANGS stays ar/en/nl for the other generators

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
    # batch 17: classic European pastries and cakes, cured and canned seafood
    # (portions from Dr. Wassim's copy, 18 October 2026)
    601: ('sweets', 80), 602: ('sweets', 85), 603: ('sweets', 100), 604: ('sweets', 110), 605: ('sweets', 35),
    606: ('sweets', 100), 607: ('sweets', 120), 608: ('sweets', 90), 609: ('sweets', 100), 610: ('sweets', 105),
    611: ('sweets', 75), 612: ('sweets', 80), 613: ('sweets', 120), 614: ('sweets', 30), 615: ('sweets', 40),
    616: ('sweets', 90), 617: ('sweets', 95), 618: ('protein', 25), 619: ('protein', 100), 620: ('protein', 120),
    621: ('protein', 120), 622: ('protein', 110), 623: ('protein', 115), 624: ('protein', 115), 625: ('protein', 85),
    # batch 18: Italian pasta and condiments, cured cod liver, fast food (fast-food values rebuilt per 100 g
    # from the approved item weights; 627-629 rebuilt as cooked pasta)
    626: ('protein', 60), 627: ('italian', 150), 628: ('italian', 150), 629: ('italian', 140),
    630: ('italian', 150), 631: ('italian', 150), 632: ('italian', 70), 633: ('condiment', 30),
    634: ('condiment', 30), 635: ('pantry', 30), 636: ('condiment', 30), 637: ('condiment', 50),
    638: ('fastfood', 280), 639: ('fastfood', 210), 640: ('fastfood', 180), 641: ('fastfood', 80), 642: ('fastfood', 85),
    643: ('fastfood', 85), 644: ('fastfood', 85), 645: ('fastfood', 200), 646: ('fastfood', 180),
    647: ('fastfood', 115), 648: ('fastfood', 130), 649: ('fastfood', 280), 650: ('fastfood', 85),
    # batch 19: Latin American, Nordic and Eastern European dishes, starches (portions from the
    # medical team's copy, 18 October 2026)
    651: ('latin', 100), 652: ('latin', 150), 653: ('latin', 120), 654: ('latin', 100), 655: ('latin', 100), 656: ('latin', 150),
    657: ('latin', 250), 658: ('latin', 100), 659: ('latin', 150), 660: ('latin', 250), 661: ('protein', 150), 662: ('pantry', 20),
    663: ('grain', 25), 664: ('protein', 60), 665: ('sandwich', 150), 666: ('sweets', 90), 667: ('veg', 150), 668: ('home', 300),
    669: ('grain', 150), 670: ('home', 250), 671: ('home', 250), 672: ('salad', 150), 673: ('grain', 100), 674: ('pantry', 20),
    675: ('pantry', 20),
    # batch 20: flours, ancient grains and specialty rice, Egyptian, Levantine, Gulf and Yemeni dishes
    # (portions from the medical team's copy, 18 October 2026)
    676: ('grain', 30), 677: ('grain', 30), 678: ('grain', 15), 679: ('grain', 40), 680: ('grain', 150), 681: ('grain', 150),
    682: ('grain', 150), 683: ('grain', 30), 684: ('grain', 150), 685: ('grain', 150), 686: ('grain', 150), 687: ('arabic', 250),
    688: ('arabic', 200), 689: ('arabic', 250), 690: ('arabic', 250), 691: ('arabic', 120), 692: ('arabic', 250), 693: ('arabic', 300),
    694: ('arabic', 250), 695: ('arabic', 150), 696: ('arabic', 200), 697: ('arabic', 200), 698: ('arabic', 300), 699: ('arabic', 300),
    700: ('bakery', 120),
    # batch 21: mustards, dressings, sauces, Asian ferments, vinegars and sesame oil
    # (portions from the medical team's copy, 18 October 2026)
    701: ('condiment', 10), 702: ('condiment', 10), 703: ('condiment', 15), 704: ('condiment', 30), 705: ('condiment', 30), 706: ('condiment', 30),
    707: ('condiment', 30), 708: ('condiment', 30), 709: ('condiment', 20), 710: ('condiment', 20), 711: ('condiment', 15), 712: ('condiment', 15),
    713: ('condiment', 10), 714: ('condiment', 18), 715: ('condiment', 18), 716: ('condiment', 20), 717: ('condiment', 20), 718: ('condiment', 50),
    719: ('condiment', 30), 720: ('condiment', 30), 721: ('condiment', 15), 722: ('condiment', 15), 723: ('condiment', 15), 724: ('condiment', 15),
    725: ('fat', 5),
    # batch 22: oils and animal fats, Levantine cheeses and butter, mezze pickles and olives, honey, molasses, jams, halawet el jibn
    # (portions from the medical team's copy, 18 October 2026)
    726: ('fat', 10), 727: ('fat', 10), 728: ('fat', 10), 729: ('fat', 10), 730: ('fat', 10), 731: ('fat', 12),
    732: ('fat', 12), 733: ('dairy_solid', 30), 734: ('dairy_solid', 30), 735: ('dairy_solid', 30), 736: ('dairy_solid', 30), 737: ('fat', 10),
    738: ('arabic', 40), 739: ('condiment', 25), 740: ('condiment', 30), 741: ('condiment', 30), 742: ('condiment', 30), 743: ('condiment', 20),
    744: ('dairy_solid', 30), 745: ('pantry', 20), 746: ('pantry', 20), 747: ('pantry', 20), 748: ('pantry', 20), 749: ('pantry', 20),
    750: ('sweets', 75),
    # batch 23: Levantine holiday sweets, teas and herbal infusions, coffee, mocktails, cold-pressed juices, breakfast grains
    # (portions from the medical team's copy, 18 October 2026)
    751: ('sweets', 20), 752: ('sweets', 35), 753: ('sweets', 35), 754: ('sweets', 20), 755: ('sweets', 18), 756: ('bakery', 30),
    757: ('drink', 150), 758: ('drink', 200), 759: ('drink', 200), 760: ('drink', 200), 761: ('drink', 200), 762: ('drink', 200),
    763: ('drink', 200), 764: ('drink', 200), 765: ('drink', 200), 766: ('drink', 200), 767: ('drink', 200), 768: ('drink', 200),
    769: ('drink', 200), 770: ('drink', 200), 771: ('drink', 200), 772: ('drink', 200), 773: ('grain', 150), 774: ('grain', 40),
    775: ('grain', 40),
    # batch 24: breakfast grains, soy and wheat proteins, Japanese dishes, Dutch supermarket staples
    # (portions from the medical team's copy, 19 October 2026)
    776: ('grain', 40), 777: ('grain', 30), 778: ('grain', 30), 779: ('sweets', 150), 780: ('grain', 200), 781: ('asian', 100),
    782: ('asian', 120), 783: ('asian', 35), 784: ('asian', 50), 785: ('asian', 100), 786: ('asian', 100), 787: ('asian', 60),
    788: ('asian', 120), 789: ('asian', 120), 790: ('asian', 180), 791: ('asian', 120), 792: ('asian', 120), 793: ('dairy_solid', 30),
    794: ('dairy_drink', 200), 795: ('nuts', 30), 796: ('bakery', 30), 797: ('grain', 35), 798: ('dairy_solid', 30), 799: ('protein', 80),
    800: ('sweets', 50),
    # batch 25: Dutch snacks and crisps, world soups, roots and tubers, specialty vegetables, cherimoya
    # (portions from the medical team's copy, 19 October 2026)
    801: ('fastfood', 25), 802: ('fastfood', 25), 803: ('fastfood', 220), 804: ('fastfood', 110), 805: ('fastfood', 70), 806: ('fastfood', 75),
    807: ('fastfood', 85), 808: ('asian', 400), 809: ('indian', 300), 810: ('asian', 300), 811: ('tuber', 150), 812: ('tuber', 150),
    813: ('tuber', 100), 814: ('tuber', 100), 815: ('veg', 150), 816: ('veg', 150), 817: ('veg', 150), 818: ('veg', 150),
    819: ('veg', 100), 820: ('veg', 150), 821: ('veg', 100), 822: ('veg', 100), 823: ('veg', 50), 824: ('veg', 50),
    825: ('fruit', 150),
    # batch 26: tropical fruits, citrus and wild berries, exotic nuts and seeds, fresh water chestnut, European cheeses
    # (portions from Dr. Wassim's copy, 20 October 2026)
    826: ('fruit', 100), 827: ('fruit', 100), 828: ('fruit', 100), 829: ('fruit', 15), 830: ('fruit', 15), 831: ('fruit', 100),
    832: ('fruit', 100), 833: ('fruit', 80), 834: ('fruit', 100), 835: ('fruit', 125), 836: ('fruit', 125), 837: ('fruit', 50),
    838: ('nuts', 30), 839: ('nuts', 30), 840: ('nuts', 30), 841: ('nuts', 30), 842: ('nuts', 20), 843: ('veg', 100),
    844: ('dairy_solid', 30), 845: ('dairy_solid', 30), 846: ('dairy_solid', 30), 847: ('dairy_solid', 30),
    848: ('dairy_solid', 30), 849: ('dairy_solid', 100), 850: ('dairy_solid', 30),
    # batch 27: Nordic, Italian, Mexican and French cheeses, cured meats, French pâtés and confit, Belgian classics
    # (portions from Dr. Wassim's copy, 21 October 2026)
    851: ('dairy_solid', 30), 852: ('dairy_solid', 30), 853: ('dairy_solid', 20), 854: ('dairy_solid', 15),
    855: ('dairy_solid', 50), 856: ('dairy_solid', 15), 857: ('dairy_solid', 30), 858: ('protein', 50),
    859: ('protein', 80), 860: ('protein', 30), 861: ('protein', 35), 862: ('protein', 40), 863: ('protein', 150),
    864: ('protein', 40), 865: ('condiment', 40), 866: ('home', 250), 867: ('home', 300), 868: ('home', 220),
    869: ('home', 200), 870: ('salad', 200), 871: ('protein', 100), 872: ('home', 250), 873: ('home', 180),
    874: ('sweets', 100), 875: ('sweets', 12),
}
# foods whose page is signed by the medical team instead of a named reviewer
TEAM_REVIEW = {6, 12, 13, 15, 16, 20, 21, 23, 24, 25, 28, 33, 34, 41, 42, 43, 44, 45, 46, 47, 52, 56, 57, 58, 60, 61,
               64, 65, 67, 73, 75, 76, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 95, 96, 97, 99, 100, 102,
               103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126,
               127, 129, 130, 131, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
               156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180,
               181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206}
TEAM_REVIEW |= set(range(207, 826))
# foods whose copy Dr. Wassim reviewed and signed himself: the page names him with the date he approved it
NAMED_REVIEW = {i: '2026-10-20' for i in range(826, 851)}
NAMED_REVIEW.update({i: '2026-10-21' for i in range(851, 876)})
NAMED_REVIEW_TXT = {'2026-10-20': {'ar': '20 أكتوبر 2026', 'en': '20 October 2026', 'nl': '20 oktober 2026'},
                    '2026-10-21': {'ar': '21 أكتوبر 2026', 'en': '21 October 2026', 'nl': '21 oktober 2026'}}


def review_date(fid):
    return NAMED_REVIEW.get(fid) or (TEAM_REVIEWED if fid in TEAM_REVIEW else REVIEWED)
# drinks whose third tip is the approved caffeine note (others get the carbohydrate / not-applicable note)
CAFFEINE = {132, 133, 134, 140}
SLUG_OVERRIDES = {71: 'greek-yogurt', 7: 'oatmeal'}   # 7 was renamed 'Cooked Oatmeal'; keep its URL

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
    'latin': ('أطباق أمريكا اللاتينية', 'Latin American dishes', 'Latijns-Amerikaanse gerechten'),
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

for _g in ('mexican', 'latin', 'italian', 'spanish', 'french', 'greek', 'turkish', 'moroccan', 'indian', 'asian', 'bakery', 'sandwich', 'home', 'salad', 'spice', 'pantry', 'condiment', 'alcohol'):
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
        boodi_text='يحلل بودي المنتجات المعلّبة فوراً، ويفحص المكونات، ويقترح بدائل أقل سكراً من نفس الرف.',
        boodi_btn='اكتشف تطبيق بودي',
        src_gi='📚 المراجع العلمية المعتمدة: الجداول الدولية للمؤشر الجلايسيمي (Atkinson et al., Am J Clin Nutr 2021) • أبحاث جامعة هارفارد الطبية (Harvard Health).',
        src_value='القيمة المعتمدة: متوسط {studies} (النطاق {lo}–{hi})، درجة الثقة {grade}.',
        src_ii='📚 مراجع مؤشر الإنسولين: Holt SH et al., Am J Clin Nutr 1997;66(5):1264–76 • Bao J et al., Am J Clin Nutr 2009;90(4):986–92.',
        src_link='المنهجية والتفاصيل ←',
        disclaimer='إخلاء مسؤولية: هذه البيانات استرشادية لنمط الحياة وليست جهازاً طبياً تشخيصياً وفق اللائحة الأوروبية EU MDR 2017/745. استشر طبيبك دائماً قبل تعديل نظامك العلاجي.',
        reviewed='راجعه طبياً: <a href="{doctor}">د. وسيم حبيب</a> · آخر مراجعة {date}',
        reviewed_named='تمت المراجعة من قبل <a href="{doctor}">الدكتور وسيم حبيب</a> · آخر مراجعة {date}',
        portion_note='الحصة المعتادة تقريبية لأغراض المقارنة.',
        theme='تبديل المظهر', footer_rights='© 2026 WiBo Health Group. جميع الحقوق محفوظة.',
        nav=('الرئيسية', 'دليل الأطعمة', 'الحاسبات', 'المكملات', 'المقالات', 'تطبيق بودي 💚'), privacy='الخصوصية', partners='الشراكات', diabetes='السكري ومتلازمة الأيض',
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
        boodi_text='boodi analyses packaged products instantly, checks the ingredients and suggests lower-sugar alternatives from the same shelf.',
        boodi_btn='Discover the boodi app',
        src_gi='📚 Scientific sources: International Tables of Glycemic Index (Atkinson et al., Am J Clin Nutr 2021) • Harvard Health Publishing.',
        src_value='Approved value: average of {studies} (range {lo}–{hi}), confidence grade {grade}.',
        src_ii='📚 Insulin index sources: Holt SH et al., Am J Clin Nutr 1997;66(5):1264–76 • Bao J et al., Am J Clin Nutr 2009;90(4):986–92.',
        src_link='Methodology & details →',
        disclaimer='Disclaimer: This guidance is for nutritional lifestyle orientation and does not constitute a diagnostic medical device under EU Regulation MDR 2017/745.',
        reviewed='Medically reviewed by <a href="{doctor}">Dr. Wassim Habib</a> · Last reviewed {date}',
        reviewed_named='Reviewed by <a href="{doctor}">Dr. Wassim Habib</a> · Last reviewed {date}',
        portion_note='The typical portion is approximate, for comparison purposes.',
        theme='Toggle theme', footer_rights='© 2026 WiBo Health Group. All rights reserved.',
        nav=('Home', 'Food Guide', 'Calculators', 'Supplements', 'Articles', 'boodi App 💚'), privacy='Privacy', partners='Partnerships', diabetes='Diabetes',
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
        boodi_text='boodi analyseert verpakte producten direct, controleert de ingrediënten en stelt suikerarmere alternatieven uit hetzelfde schap voor.',
        boodi_btn='Ontdek de boodi-app',
        src_gi='📚 Wetenschappelijke bronnen: Internationale GI-tabellen (Atkinson et al., Am J Clin Nutr 2021) • Harvard Health Publishing.',
        src_value='Goedgekeurde waarde: gemiddelde van {studies} (bereik {lo}–{hi}), betrouwbaarheidsgraad {grade}.',
        src_ii='📚 Bronnen insuline-index: Holt SH et al., Am J Clin Nutr 1997;66(5):1264–76 • Bao J et al., Am J Clin Nutr 2009;90(4):986–92.',
        src_link='Methodologie & details →',
        disclaimer='Algemene disclaimer: Deze informatie is uitsluitend bedoeld als voedingsadvies en is geen medisch diagnostisch hulpmiddel volgens EU MDR 2017/745.',
        reviewed='Medisch gecontroleerd door <a href="{doctor}">dr. Wassim Habib</a> · Laatst gecontroleerd {date}',
        reviewed_named='Beoordeeld door <a href="{doctor}">Dr. Wassim Habib</a> · Laatst beoordeeld {date}',
        portion_note='De gangbare portie is een benadering, bedoeld om te vergelijken.',
        theme='Thema wisselen', footer_rights='© 2026 WiBo Health Group. Alle rechten voorbehouden.',
        nav=('Home', 'Voedingswijzer', 'Calculators', 'Supplementen', 'Artikelen', 'boodi App 💚'), privacy='Privacy', partners='Partners', diabetes='Diabetes',
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
                 504, 508, 510, 527, 543, 546, 399},
          'nl': {17, 18, 19, 22, 40, 53, 62, 63, 68, 20, 21, 23, 24, 25, 28, 42, 45, 52, 56, 57, 58, 60, 80, 81, 82,
                 83, 84, 85, 87, 88, 89, 99, 100, 113, 117, 142, 151, 161, 162, 183, 220, 232, 233, 234, 235, 260, 276, 284, 292, 293, 302,
                 411, 412, 413, 423, 424, 425,
                 426, 427, 428, 429, 430, 431, 432, 434, 435, 436, 437, 438, 439, 440, 443, 448, 449,
                 451, 465, 472, 476, 478, 479, 495,
                 504, 508, 527, 543, 546, 399}}
VERBS = {'en': (dict(is_='is', does='does', contains='contains', provides='provides'),
                dict(is_='are', does='do', contains='contain', provides='provide')),
         'nl': (dict(is_='is', bevat='bevat', levert='levert'), dict(is_='zijn', bevat='bevatten', levert='leveren')),
         'ar': (dict(), dict())}


def build_faq(food, lang, name, portion, measured, gi=None, lvl=None, gl=None, glv=None, g=None, reviewed=False):
    """Three questions whose answers are computed from the food's own numbers."""
    f, u = FAQ[lang], UI[lang]
    lv, lg = u.get('levels_txt', u['levels']), u.get('levels_gl', u['levels'])
    v = dict(VERBS[lang][1 if food['id'] in PLURAL.get(lang, set()) else 0])
    if 'is_' in v:
        v['Is_'] = v['is_'].capitalize()
    v.update(g or {})
    pf = portion / 100.0
    kcal = food['kcal']
    kcal_p = int(kcal * pf + 0.5 + 1e-9)    # half up (130.5 -> 131), not Python's banker's rounding
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
        a2 = f['s_reviewed' if reviewed else 's_measured'].format(gi=gi, level=lv[lvl], p=portion, gl=fmt(gl), gl_level=lg[glv],
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
    # batch 27: construct phrases and proper names that are already definite
    'جبنة دانابلو الدنماركية الزرقاء': 'جبنة دانابلو الدنماركية الزرقاء',
    'جبنة يارلسبيرغ النرويجية': 'جبنة يارلسبيرغ النرويجية',
    'جبنة برونوست النرويجية البنية': 'جبنة برونوست النرويجية البنية',
    'جبنة ريكوتا سالاتا الإيطالية': 'جبنة ريكوتا سالاتا الإيطالية',
    'جبنة كيسو بلانكو المكسيكية': 'جبنة كيسو بلانكو المكسيكية',
    'جبنة كوتيخا المكسيكية': 'جبنة كوتيخا المكسيكية',
    'جبنة شيفر الفرنسية بالرماد': 'جبنة شيفر الفرنسية بالرماد',
    'روبيان بحر الشمال الرمادي المقشر': 'روبيان بحر الشمال الرمادي المقشر',
    'شتومب بروكسل بالجزر والكراث': 'شتومب بروكسل بالجزر والكراث',
    'وافل لييج البلجيكي بسكر اللؤلؤ': 'وافل لييج البلجيكي بسكر اللؤلؤ',
    'بسكويت أيدي أنتويرب بالزبدة واللوز': 'بسكويت أيدي أنتويرب بالزبدة واللوز',
    'سجق سوجوك بقري تركي': 'سجق السوجوك البقري التركي',
    'سجق مرقاز مغاربي': 'سجق المرقاز المغاربي',
    'سيسينا دي ليون الإسبانية (لحم بقري مقدد)': 'سيسينا دي ليون الإسبانية',
    'بيلتونغ لحم بقري جنوب إفريقي': 'بيلتونغ اللحم البقري الجنوب إفريقي',
    'درووورس نقانق لحم بقري جنوب إفريقية مجففة': 'الدرووورس الجنوب إفريقي المجفف',
    'فخذ بط كونفي فرنسي': 'فخذ البط الكونفي الفرنسي',
    'باتيه كبد الدجاج الفرنسي بالأعشاب': 'باتيه كبد الدجاج الفرنسي',
    'يخنة ستوفليز الفلمنكية البلجيكية': 'يخنة الستوفليز الفلمنكية البلجيكية',
    'فاتر زوي البلجيكية بالدجاج والكريمة': 'حساء الفاتر زوي البلجيكي بالدجاج والكريمة',
    'طماطم محشوة بروبيان بحر الشمال': 'الطماطم المحشوة بروبيان بحر الشمال',
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


# "References & scientific sources" block at the bottom of every food page: only sources that actually back the page
REF_ATKINSON = ('Atkinson FS, Brand-Miller JC, Foster-Powell K, Buyken AE, Goletzke J. International tables of glycemic index and '
                'glycemic load values 2021: a systematic review. Am J Clin Nutr. 2021;114(5):1625–1632.', 'https://doi.org/10.1093/ajcn/nqab233')
REF_ISO = ('ISO 26642:2010. Food products — Determination of the glycaemic index (GI) and recommendation for food classification. '
           'International Organization for Standardization; 2010.', 'https://www.iso.org/standard/43633.html')
REF_FAO = ('FAO/WHO. Carbohydrates in human nutrition: report of a joint FAO/WHO expert consultation. FAO Food and Nutrition Paper 66. '
           'Rome; 1998.', 'https://www.fao.org/4/w8079e/w8079e00.htm')
REF_HOLT = ('Holt SH, Miller JC, Petocz P. An insulin index of foods: the insulin demand generated by 1000-kJ portions of common foods. '
            'Am J Clin Nutr. 1997;66(5):1264–1276.', 'https://doi.org/10.1093/ajcn/66.5.1264')
REF_BAO = ('Bao J, de Jong V, Atkinson F, Petocz P, Brand-Miller JC. Food insulin index: physiologic basis for predicting insulin demand '
           'evoked by composite meals. Am J Clin Nutr. 2009;90(4):986–992.', 'https://doi.org/10.3945/ajcn.2009.27720')
REFS_UI = {
    'ar': dict(title='المراجع والمصادر العلمية',
               measured='قيمة المؤشر الجلايسيمي مأخوذة من الجداول الدولية: ',
               reviewed='قيمة المؤشر الجلايسيمي لهذا الصنف تقدير مراجع سريرياً من فريق ويبو هيلث الطبي، وليست قياساً مخبرياً من الجداول الدولية (Atkinson 2021). تصنيف المؤشر (منخفض ≤ 55 · متوسط 56–69 · مرتفع ≥ 70) وفق: ',
               na='لا ينطبق المؤشر الجلايسيمي لأن الصنف يحتوي على أقل من 5 غ كربوهيدرات متاحة لكل 100 غ، واختبار المؤشر يتطلب 25 إلى 50 غ كربوهيدرات متاحة وفق: ',
               iso='تصنيف المؤشر الجلايسيمي وطريقة قياسه: ',
               fao='تعريف الكربوهيدرات المتاحة والحمل الجلايسيمي: ',
               ii='مؤشر الإنسولين: '),
    'en': dict(title='References & Scientific Sources',
               measured='The glycemic index value comes from the international tables: ',
               reviewed='The glycemic index of this food is a clinically reviewed estimate by the WiBo Health medical team, not a laboratory measurement from the International GI Tables (Atkinson 2021). GI bands (low ≤ 55 · medium 56–69 · high ≥ 70) follow: ',
               na='The glycemic index does not apply because this food has less than 5 g of available carbohydrate per 100 g, and a GI test requires 25 to 50 g of available carbohydrate, per: ',
               iso='GI classification and test method: ',
               fao='Definition of available carbohydrate and glycemic load: ',
               ii='Insulin index: '),
    'nl': dict(title='Wetenschappelijke bronnen & Referenties',
               measured='De waarde van de glykemische index komt uit de internationale tabellen: ',
               reviewed='De glykemische index van dit product is een klinisch beoordeelde schatting van het medisch team van WiBo Health, geen laboratoriummeting uit de internationale GI-tabellen (Atkinson 2021). De GI-indeling (laag ≤ 55 · gemiddeld 56–69 · hoog ≥ 70) volgt: ',
               na='De glykemische index is niet van toepassing, omdat dit product minder dan 5 g beschikbare koolhydraten per 100 g bevat, en een GI-test 25 tot 50 g beschikbare koolhydraten vereist, volgens: ',
               iso='GI-indeling en testmethode: ',
               fao='Definitie van beschikbare koolhydraten en glykemische lading: ',
               ii='Insuline-index: '),
}


def ref_cite(ref):
    text, url = ref
    return f'{esc(text)} <a href="{url}" target="_blank" rel="noopener">{url.split("//", 1)[1]}</a>'


def studies_word(n, lang):
    if lang == 'ar':
        return {1: 'دراسة واحدة', 2: 'دراستين'}.get(n, f'{n} دراسات' if 3 <= n <= 10 else f'{n} دراسة')
    if lang == 'en':
        return '1 study' if n == 1 else f'{n} studies'
    if lang == SV:
        return FSV.studies_word(n)
    return '1 studie' if n == 1 else f'{n} studies'


# Swedish copy (scripts/food_sv.py): tuples indexed by language get a fourth entry, dicts a 'sv' key
UI[SV], FAQ[SV], REFS_UI[SV] = FSV.UI, FSV.FAQ, FSV.REFS_UI
VERBS[SV] = (dict(), dict())
GROUPS = {k: v + (FSV.GROUPS[k],) for k, v in GROUPS.items()}
CARB_NOTE, NA_NOTE = CARB_NOTE + (FSV.CARB_NOTE,), NA_NOTE + (FSV.NA_NOTE,)
for _g, _tips in FSV.TIPS.items():
    TIPS[_g] = TIPS[_g] + (_tips,)


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
            id=fid, ar=s('name'), en=s('nameEn'), nl=s('nameNl'), image=s('image'), icon=s('icon'), group=s('group'),
            gi=n('gi'), gi_status=s('gi_status'), gi_grade=s('gi_grade'), gi_n=n('gi_n'), gi_range=arr('gi_range'),
            ii=n('ii'), kcal=n('calories') or 0, protein=n('protein') or 0, carbs=n('carbs') or 0, fat=n('fat') or 0,
            fiber=n('fiber') or 0)
        foods[fid]['avail'] = round(max(0.0, foods[fid]['carbs'] - foods[fid]['fiber']), 1)
    return foods


def load_group_labels():
    """key -> {ar, en, nl} from FOOD_GROUPS in js/food-categories.js (the labels of the foods.html filter bar)."""
    text = (ROOT / 'js' / 'food-categories.js').read_text(encoding='utf-8')
    labels = {}
    for row in re.findall(r"\{\s*key:[^\n]*\}", text):
        get = lambda k: re.search(r"\b%s:\s*'([^']*)'" % k, row).group(1)
        labels[get('key')] = {l: get(l) for l in LANGS}
        labels[get('key')][SV] = FSV.GROUP_LABELS[get('key')]
    assert len(labels) == 10, f'expected 10 food groups, found {len(labels)}'
    return labels


FOOD_GROUP_LABELS = load_group_labels()


def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


DECIMAL = '.'        # ',' while a Swedish or Dutch page is built (set in build())


def fmt(x):
    x = round(x, 1)
    return (str(int(x)) if float(x).is_integer() else str(x)).replace('.', DECIMAL)


# <title>: the name plus the full keyword suffix (calories, glycemic index, nutrition facts), which is never shortened:
# Google ranks on the whole title, the ~60 characters are only what it displays (keywords cut on 2026-10-24 cost
# impressions; restored 2026-10-27, approved by Dr. Wassim Habib). Order of retreat for a long title: the brand, the
# name's (bracketed) part, then the name cut before a joining word, so the title stays within TITLE_HARD_MAX.
TITLE_MAX = 60                  # the brand is kept only while the whole title fits in this
TITLE_HARD_MAX = 80
TITLE_BRAND = ' | WiBo Health'
TITLE_SUFFIXES = {
    'ar': ': السعرات والمؤشر الجلايسيمي والقيم الغذائية',
    'en': ': Calories, Glycemic Index & Nutrition Facts',
    'nl': ': calorieën, glykemische index & voedingswaarde',
    'sv': ': kalorier, glykemiskt index och näringsvärde',
}
# a shortened name stops before one of these words (Arabic: before a word joined with و or ب), never on them
TITLE_JOINS = {'ar': ('مع',), 'en': ('with', 'and', '&', 'in', 'on'), 'nl': ('met', 'en', '&', 'in', 'op'),
               'sv': ('med', 'och', '&', 'i', 'på')}


def fit_title(name, lang):
    suf = TITLE_SUFFIXES[lang]
    if len(name + suf + TITLE_BRAND) <= TITLE_MAX:
        return name + suf + TITLE_BRAND
    short = re.sub(r'\s*\([^)]*\)', '', name).strip() or name
    words = short.split()
    # the name cut before a joining word, longest first: "Gemista gevulde tomaten en paprika's met rijst" -> "Gemista
    # gevulde tomaten"; Arabic "صلصة تزاتزيكي يونانية بالزبادي ..." -> "صلصة تزاتزيكي يونانية"
    joins = TITLE_JOINS[lang]
    cuts = [' '.join(words[:k]) for k in range(len(words) - 1, 1, -1)
            if words[k].lower() in joins or (lang == 'ar' and words[k][:1] in 'وب' and len(words[k]) > 3)]
    for nm in dict.fromkeys((name, short, *cuts)):
        if len(nm + suf) <= TITLE_HARD_MAX:
            return nm + suf
    while len(words) > 1 and len(' '.join(words) + suf) > TITLE_HARD_MAX:
        words.pop()
    return ' '.join(words).rstrip(' ,،-–&') + suf


# "Read also": the medical guides that belong to a food, in the reader's language (titles as published, without
# their claim wording). Swedish pages link the Swedish article where one exists, otherwise the English page.
READ_ALSO_TITLE = {'ar': 'اقرأ أيضاً', 'en': 'Read also', 'nl': 'Lees ook', 'sv': 'Läs även'}
READ_ALSO_KIND = {'guide': {'ar': 'دليل', 'en': 'Guide', 'nl': 'Gids', 'sv': 'Guide'},
                  'article': {'ar': 'مقال', 'en': 'Article', 'nl': 'Artikel', 'sv': 'Artikel'},
                  'supplement': {'ar': 'مكمل', 'en': 'Supplement', 'nl': 'Supplement', 'sv': 'Kosttillskott (engelska)'}}
READ_ALSO = {
    'insulin': ('article', {
        'ar': ('/insulin-resistance.html', 'السكر التراكمي ومقاومة الإنسولين: الدليل الشامل'),
        'en': ('/insulin-resistance.html?lang=en', 'HbA1c & Insulin Resistance: Comprehensive Clinical Guide'),
        'nl': ('/insulin-resistance.html?lang=nl', 'HbA1c & Insulineresistentie: De Complete Klinische Gids'),
        'sv': ('/sv/articles/insulinresistens-hba1c.html', 'HbA1c och insulinresistens: så förstår du dina värden')}),
    'prediabetes': ('guide', {
        'ar': ('/diabetes/prediabetes.html', 'مرحلة ما قبل السكري: كيف توقف القطار وتنزّل التراكمي قبل ما يتحول لسكري؟'),
        'en': ('/en/diabetes/prediabetes.html', 'Prediabetes: How to Stop the Train and Lower Your HbA1c'),
        'nl': ('/nl/diabetes/prediabetes.html', 'Prediabetes: zo zet je de trein stil en verlaag je je HbA1c'),
        'sv': ('/sv/diabetes/prediabetes.html', 'Prediabetes: så bromsar du utvecklingen och sänker ditt HbA1c')}),
    'gestational': ('guide', {
        'ar': ('/diabetes/gestational-diabetes.html', 'دليل سكر الحمل الشامل: المعدل الطبيعي بالأرقام وجدول الأكل'),
        'en': ('/en/diabetes/gestational-diabetes.html', 'Gestational Diabetes Guide: Normal Levels and Foods to Eat'),
        'nl': ('/nl/diabetes/zwangerschapsdiabetes.html', 'Zwangerschapsdiabetes: normale waarden en wat je mag eten'),
        'sv': ('/sv/diabetes/graviditetsdiabetes.html', 'Graviditetsdiabetes: normala blodsockervärden och vad du kan äta')}),
    'thyroid': ('article', {
        'ar': ('/thyroid-health.html', 'لغز خمول الغدة الدرقية وبطء الحرق'),
        'en': ('/thyroid-health.html?lang=en', 'The Hidden Thyroid Sluggishness'),
        'nl': ('/thyroid-health.html?lang=nl', 'De verborgen trage schildklier'),
        'sv': ('/sv/articles/trog-skoldkortel.html', 'Trög sköldkörtel: TSH, T4 och T3 i klartext')}),
    'selenium': ('supplement', {
        'ar': ('/supplements/selenium.html', 'السيلينيوم (سيلينوميثيونين)'),
        'en': ('/en/supplements/selenium.html', 'Selenium (L-Selenomethionine)'),
        'nl': ('/nl/supplements/selenium.html', 'Selenium (L-Selenomethionine)'),
        'sv': ('/en/supplements/selenium.html', 'Selen (L-selenometionin)')}),
    'fatty_liver': ('article', {
        'ar': ('/fatty-liver.html', 'الكبد الدهني الخفي: دليلك السريري'),
        'en': ('/fatty-liver.html?lang=en', 'Silent Fatty Liver (MASLD/NAFLD): Clinical Guide'),
        'nl': ('/fatty-liver.html?lang=nl', 'Stille Leververvetting (MASLD/NAFLD): Klinische Gids'),
        'sv': ('/sv/articles/fettlever.html', 'Fettlever (MASLD): så uppstår den tyst och vad du kan göra')}),
}
STARCH_GROUPS = {'grain', 'tuber', 'bakery', 'sweets', 'fastfood', 'sandwich', 'dried'}
SELENIUM_FOODS = {399}            # the selenium supplement page is linked from Brazil nuts only (approved 2026-10-24)
DISH_GROUPS = {'arabic', 'fastfood', 'mexican', 'latin', 'italian', 'spanish', 'french', 'greek', 'turkish', 'moroccan',
               'indian', 'asian', 'home', 'sandwich'}


def read_also_keys(food, group, gi):
    """Up to three guides, most specific first: nuts and seeds -> thyroid (+ selenium for Brazil nuts), fats -> fatty
    liver, starches, sweets and GI >= 56 -> insulin resistance + prediabetes, GI <= 55 -> prediabetes + gestational
    diabetes, fatty dishes (15 g fat or more per 100 g) -> fatty liver. Alcohol only links the fatty-liver article."""
    if group == 'alcohol':
        return ['fatty_liver']
    keys = []
    if group == 'nuts':
        keys += ['thyroid'] + (['selenium'] if food['id'] in SELENIUM_FOODS else [])
    if group == 'fat':
        keys += ['fatty_liver']
    if group in STARCH_GROUPS or (gi is not None and gi >= 56):
        keys += ['insulin', 'prediabetes']
    if gi is not None and gi <= 55:
        keys += ['prediabetes', 'gestational']
    if group in DISH_GROUPS and food['fat'] >= 15:
        keys += ['fatty_liver']
    return list(dict.fromkeys(keys or ['prediabetes']))[:3]


def fit_override_title(title):
    """An approved search title stays as written; only the brand goes when the title would be cut."""
    return title[:-len(TITLE_BRAND)] if len(title) > TITLE_MAX and title.endswith(TITLE_BRAND) else title


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
LOGO_SVG = ('<img class="brand-logo-svg" src="/images/brand/wibo-logo-64.webp" '   # emerald heart logo
            'srcset="/images/brand/wibo-logo-128.webp 2x" width="34" height="34" alt="" decoding="async">')

# Inline SVG icons (24 px grid, drawn with currentColor) in place of the Font Awesome stylesheet and webfont
ICON_PATHS = {
    'check': '<circle cx="12" cy="12" r="9"/><path d="m8 12.5 2.6 2.6L16 9.5"/>',
    'utensils': '<path d="M6 3v7a2 2 0 0 0 4 0V3M8 3v18M17 21V3c-2.2 0-3.5 2.6-3.5 6.5S14.8 14 17 14"/>',
    'warn': '<path d="M12 3.5 2.5 20h19z"/><path d="M12 10v4.5M12 17.4v.1"/>',
    'table': '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9.5h18M3 15h18M9 9.5V20"/>',
    'scale': '<path d="M12 3v18M7 21h10M4 7h16M7 7l-3 7a3 3 0 0 0 6 0zM17 7l-3 7a3 3 0 0 0 6 0z"/>',
    'question': '<circle cx="12" cy="12" r="9"/><path d="M9.6 9.3a2.5 2.5 0 1 1 3.4 2.4c-.6.3-1 .8-1 1.5v.6M12 16.8v.1"/>',
    'book': '<path d="M5 4.5A1.5 1.5 0 0 1 6.5 3H19v15H6.5A1.5 1.5 0 0 0 5 19.5zM5 19.5A1.5 1.5 0 0 0 6.5 21H19v-3"/><path d="M12 7v6M9 10h6"/>',
    'barcode': '<path d="M4 5v14M7 5v14M10.5 5v14M13 5v14M16.5 5v14M20 5v14"/>',
    'bolt': '<path d="M13 2.5 4.5 13.5H11L10 21.5l8.5-11H12z"/>',
    'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/>',
    'moon': '<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/>',
    'back': '<path d="M19 12H5M11 18l-6-6 6-6"/>',                  # points left; mirrored on RTL pages (css)
}


def icon(name, cls=''):
    return (f'<svg class="ico{" " + cls if cls else ""}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
            f'{ICON_PATHS[name]}</svg>')

PAGE_CSS = """
        a.lang-btn { text-decoration: none; }
        .food-page h1, .food-page h3, .food-page td, .boodi-card h2, .food-page strong { color: var(--text-main); }
        .food-page { max-width: 980px; }
        .ico { width: 1.1em; height: 1.1em; flex-shrink: 0; vertical-align: -0.18em; fill: none; stroke: currentColor;
            stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
        .theme-toggle-btn .ico { width: 16px; height: 16px; }
        .theme-toggle-btn .ti-moon, html[data-theme="light"] .theme-toggle-btn .ti-sun { display: none; }
        html[data-theme="light"] .theme-toggle-btn .ti-moon { display: inline-block; }
        .sr-only { position: absolute !important; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
        /* back to the food guide (js/food-serving.js returns to the same place in the list when the reader came from it) */
        .fp-back { display: inline-flex; align-items: center; gap: 7px; margin-bottom: 12px; padding: 7px 14px 7px 12px;
            border-radius: 999px; border: 1px solid var(--primary-glow); background: var(--bg-input); color: var(--primary);
            font-size: 0.9rem; font-weight: 700; text-decoration: none; line-height: 1.3; }
        .fp-back:hover { background: var(--primary); border-color: var(--primary); color: #fff; }
        .fp-back:focus-visible { outline: 3px solid var(--primary); outline-offset: 2px; }
        [dir="rtl"] .fp-back { padding: 7px 12px 7px 14px; }
        [dir="rtl"] .fp-back .ico { transform: scaleX(-1); }
        .breadcrumb { font-size: 0.85rem; color: var(--text-muted); margin-bottom: 14px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .breadcrumb a { color: var(--text-muted); text-decoration: none; }
        .breadcrumb a:hover { color: var(--primary); }
        /* compact hero: thumbnail beside the name */
        .fp-hero { display: flex; gap: 14px; align-items: center; margin-bottom: 14px; }
        .fp-hero img, .fp-hero .food-emoji { width: 96px; height: 96px; border-radius: 18px; object-fit: cover; flex-shrink: 0;
            border: 2px solid var(--primary-glow); background: var(--bg-input); }
        .fp-hero .food-emoji { display: flex; align-items: center; justify-content: center; font-size: 2.6rem; }
        .fp-hero-text { min-width: 0; }
        .fp-hero-text h1 { font-size: 1.9rem; font-weight: 900; line-height: 1.25; margin: 0 0 4px; overflow-wrap: anywhere; }
        .fp-sub { display: flex; flex-wrap: wrap; gap: 6px 10px; align-items: center; color: var(--text-muted); font-weight: 600; font-size: 0.88rem; }
        .group-chip {
            display: inline-block; padding: 2px 10px; border-radius: 999px; font-size: 0.76rem;
            font-weight: 700; color: var(--primary); background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.25);
        }
        /* quick answer (static, the medium portion) */
        .quick-answer { background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3);
            border-inline-start: 4px solid var(--primary); border-radius: var(--radius-md); padding: 12px 14px; margin-bottom: 14px; }
        .quick-answer h2 { display: flex; align-items: center; gap: 6px; font-size: 0.8rem; font-weight: 800; color: var(--primary); margin: 0 0 4px; }
        .about-card .quick-answer p { margin: 0; font-size: 0.95rem; line-height: 1.75; color: var(--text-main); }
        /* macro card: portion pills, energy ring, 2x2 macros, GI / GL */
        .fp { --c-carb: #38bdf8; --c-prot: #a78bfa; --c-fat: #fb7185; --c-fib: #34d399; }
        html[data-theme="light"] .fp { --c-carb: #0284c7; --c-prot: #7c3aed; --c-fat: #e11d48; --c-fib: #059669; }
        .macro-card { background: var(--bg-input); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 12px; margin-bottom: 16px; }
        .servings { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 5px; border: 0; padding: 0; margin: 0 0 12px; min-width: 0; }
        .pill { position: relative; cursor: pointer; }
        .pill input { position: absolute; opacity: 0; inset: 0; margin: 0; cursor: pointer; }
        .pill > span { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 48px;
            padding: 4px 2px; border-radius: 12px; border: 1px solid var(--border-color); background: var(--bg-card);
            text-align: center; line-height: 1.2; transition: background .15s, border-color .15s, color .15s; }
        .pill-name { white-space: nowrap; font-size: 0.74rem; font-weight: 800; color: var(--text-main); }
        .pill small { font-size: 0.7rem; font-weight: 700; color: var(--text-muted); font-variant-numeric: tabular-nums; }
        .pill input:checked + span { background: var(--primary); border-color: var(--primary); }
        .pill input:checked + span .pill-name, .pill input:checked + span small { color: #ffffff; }
        html[data-theme="dark"] .pill input:checked + span { background: #047857; border-color: #047857; }
        .pill input:focus-visible + span { outline: 2px solid var(--primary); outline-offset: 2px; }
        .macro-body { display: flex; align-items: center; gap: 14px; }
        .donut { position: relative; width: 116px; height: 116px; flex-shrink: 0; margin: 0; }
        .donut svg { width: 100%; height: 100%; transform: rotate(-90deg); }
        html[dir="rtl"] .donut svg { transform: rotate(-90deg) scaleY(-1); }   /* clockwise from the top in RTL too */
        .donut circle { fill: none; stroke-width: 5.2; }
        .donut .track { stroke: var(--border-color); }
        .donut .seg-c { stroke: var(--c-carb); } .donut .seg-p { stroke: var(--c-prot); } .donut .seg-f { stroke: var(--c-fat); }
        .donut figcaption { position: absolute; inset: 0; display: flex; flex-direction: column; align-items: center; justify-content: center; line-height: 1.1; }
        .donut figcaption b { font-size: 1.55rem; font-weight: 900; color: var(--text-main); font-variant-numeric: tabular-nums; }
        .donut figcaption span { font-size: 0.72rem; font-weight: 700; color: var(--text-muted); }
        .macro-legend { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 10px 8px; flex: 1; min-width: 0; }
        .macro-legend li { display: grid; grid-template-columns: 10px minmax(0, 1fr); column-gap: 6px; align-items: center; }
        .dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }
        .dot-c { background: var(--c-carb); } .dot-p { background: var(--c-prot); } .dot-f { background: var(--c-fat); } .dot-fib { background: var(--c-fib); }
        .m-name { font-size: 0.72rem; font-weight: 700; color: var(--text-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .m-val { grid-column: 2; font-size: 1.05rem; font-weight: 900; color: var(--text-main); font-variant-numeric: tabular-nums; white-space: nowrap; }
        .m-pct { grid-column: 2; white-space: nowrap; font-size: 0.7rem; font-weight: 600; color: var(--text-muted); }
        .about-card .macro-note { margin: 8px 0 0; font-size: 0.68rem; font-weight: 600; color: var(--text-muted); text-align: center; }
        .gi-strip { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 12px; }
        .gi-box { display: grid; grid-template-columns: auto minmax(0, 1fr); grid-template-areas: "label label" "num badge" "sub sub";
            align-items: center; column-gap: 8px; background: var(--bg-card); border: 1px solid var(--border-color);
            border-radius: 12px; padding: 8px 10px; }
        .gi-label { grid-area: label; font-size: 0.72rem; font-weight: 700; color: var(--text-muted); }
        .gi-num { grid-area: num; font-size: 1.45rem; font-weight: 900; line-height: 1.2; font-variant-numeric: tabular-nums; min-width: 2.4ch; }
        .gi-num.low { color: #10b981; } .gi-num.medium { color: #f39c12; } .gi-num.high { color: #e74c3c; } .gi-num.muted { color: var(--text-muted); }
        html[data-theme="dark"] .gi-num.low { color: #6ee7b7; } html[data-theme="dark"] .gi-num.medium { color: #fcd34d; }
        html[data-theme="dark"] .gi-num.high { color: #fca5a5; }
        .gi-box .badge { grid-area: badge; justify-self: start; margin: 0; max-width: 100%; text-align: center; }
        .gi-sub { grid-area: sub; font-size: 0.68rem; font-weight: 600; color: var(--text-muted); }
        /* introduction: two lines until "read more" (the class is set by js/food-serving.js) */
        .lead-fold { margin-bottom: 6px; }
        .about-card .lead-fold .lead { margin: 0; font-size: 0.95rem; }
        .lead-fold.clamped .lead { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
        .more-btn { background: none; border: 0; padding: 4px 0; color: var(--primary); font: inherit; font-size: 0.85rem; font-weight: 800; cursor: pointer; }
        .reviewed { font-size: 0.85rem; color: var(--text-muted); margin: 12px 0 0; }
        .reviewed a { color: var(--primary); text-decoration: none; font-weight: 700; }
        .badge {
            display: inline-block; margin-top: 6px; padding: 2px 10px; border-radius: 999px; font-size: 0.72rem;
            font-weight: 700; border: 1px solid transparent;
        }
        .badge.low { background: rgba(16, 185, 129, 0.12); border-color: rgba(16, 185, 129, 0.45); color: #10b981; }
        .badge.medium { background: rgba(243, 156, 18, 0.12); border-color: rgba(243, 156, 18, 0.45); color: #f39c12; }
        .badge.high { background: rgba(231, 76, 60, 0.12); border-color: rgba(231, 76, 60, 0.45); color: #e74c3c; }
        .badge.neutral { background: rgba(148, 163, 184, 0.14); border-color: rgba(148, 163, 184, 0.45); color: var(--text-muted); }
        /* tips and FAQ: accordions, the first one open */
        .acc-list { display: grid; gap: 8px; margin: 8px 0 22px; }
        .acc { background: var(--bg-input); border: 1px solid var(--border-color); border-radius: var(--radius-sm); }
        .acc.tip { border-inline-start: 4px solid var(--primary); }
        .acc.tip.warn { border-inline-start-color: #f39c12; }
        .acc summary { list-style: none; cursor: pointer; padding: 12px 14px; font-weight: 800; color: var(--text-main);
            display: flex; align-items: center; gap: 8px; font-size: 0.95rem; }
        .acc summary::-webkit-details-marker { display: none; }
        .acc summary::after { content: "+"; margin-inline-start: auto; padding-inline-start: 8px; font-weight: 900; color: var(--primary); font-size: 1.1rem; }
        .acc[open] summary::after { content: "\\2212"; }
        .acc summary h3 { font-size: inherit; font-weight: inherit; margin: 0; }
        .acc.tip summary .ico { color: var(--primary); } .acc.tip.warn summary .ico { color: #f39c12; }
        .about-card .acc p { margin: 0; padding: 0 14px 12px; color: var(--text-muted); }
        .section-title .ico { width: 0.95em; height: 0.95em; }
        .boodi-btn .ico { width: 18px; height: 18px; }
        .nutrition-table td b { font-weight: 700; font-variant-numeric: tabular-nums; }
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
        .read-also a { overflow-wrap: anywhere; }      /* long names such as (L-Selenomethionine) on 320 px */
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
        .references {
            background: var(--bg-input); border: 1px solid rgba(16, 185, 129, 0.35); border-inline-start: 4px solid var(--primary);
            border-radius: 14px; padding: 4px 18px 14px; margin: 18px 0 10px;
        }
        .references .section-title { margin-top: 12px; }
        .ref-list { margin: 0; padding-inline-start: 22px; color: var(--text-muted); font-size: 0.85rem; line-height: 1.7; overflow-wrap: anywhere; }
        .ref-list li { margin-bottom: 8px; }
        .ref-list a, .ref-method a { color: var(--primary); font-weight: 700; text-decoration: none; }
        .ref-method { margin: 4px 0 0; font-size: 0.85rem; font-weight: 800; }
        .disclaimer-box {
            margin-top: 18px; padding: 14px 18px; border-radius: 12px; background: rgba(15, 23, 42, 0.62);
            border: 1px solid rgba(226, 232, 240, 0.22); color: #e2e8f0; font-size: 0.85rem; text-align: center;
        }
        html[data-theme="light"] .disclaimer-box { background: #f1f5f9; border-color: rgba(15, 23, 42, 0.12); color: #334155; }
        @media (min-width: 761px) {
            .donut { width: 150px; height: 150px; }
            .macro-legend { grid-template-columns: repeat(4, minmax(0, 1fr)); }
        }
        @media (max-width: 760px) {
            .food-page.page-wrapper { margin: 12px auto 50px; padding: 0 10px; }
            .food-page .about-card { padding: 16px 14px; }
            .food-page .section-title { font-size: 1.15rem; margin: 22px 0 10px; }
            .fp-hero img, .fp-hero .food-emoji { width: 72px; height: 72px; border-radius: 16px; }
            .fp-hero .food-emoji { font-size: 2rem; }
            .fp-hero-text h1 { font-size: 1.45rem; }
            .fp-hero-text h1.long { font-size: 1.2rem; }
            .donut { width: 104px; height: 104px; }
            .macro-body { gap: 10px; }
        }
        @media (max-width: 360px) {
            .donut { width: 92px; height: 92px; }
            .donut figcaption b { font-size: 1.3rem; }
            .pill-name { font-size: 0.68rem; }
        }
"""


# Mobile-first top of the page (approved by Dr. Wassim, 25 October 2026): quick answer, portion pills, energy ring.
# Quick answer: the approved Arabic sentence and its faithful translations; qa_na is its first sentence, for foods
# without a glycemic index. Portions: 100 g and 0.5 / 1.0 / 1.5 x the approved typical portion (medium = typical).
SERVING_FACTORS = (('small', 0.5), ('medium', 1.0), ('large', 1.5))
FP_UI = {
    'ar': dict(
        qa_title='الإجابة السريعة',
        qa='في حصة متوسطة من {name} ({g} غ) توجد {kcal} سعرة حرارية، مع {net} غ كاربوهيدرات صافية و{protein} غ بروتين. '
           'مؤشر{h} الجلايسيمي {gi} ({gi_level}) في سرعة رفع السكر، بينما حمل{h} الجلايسيمي للحصة {gl} ({gl_level}) في تأثير{h} الفعلي.',
        qa_na='في حصة متوسطة من {name} ({g} غ) توجد {kcal} سعرة حرارية، مع {net} غ كاربوهيدرات صافية و{protein} غ بروتين.',
        choose='اختر الحصة', card='القيم الغذائية حسب الحصة', ref='مرجعي', g100='100 غ',
        servings=dict(small='حصة صغيرة', medium='حصة متوسطة', large='حصة كبيرة'),
        short=dict(small='صغيرة', medium='متوسطة', large='كبيرة'),
        col='{label} ({g} غ)', macros=('كربوهيدرات', 'بروتين', 'دهون', 'ألياف'), pct='{v}%',
        energy_note='النسب المئوية من إجمالي الطاقة (السعرات)', energy_aria='توزيع الطاقة: كربوهيدرات {c}، بروتين {p}، دهون {f}',
        gi_same='ثابت لكل الحصص', more='اقرأ المزيد', less='عرض أقل', back='العودة لدليل الأطعمة'),
    'en': dict(
        qa_title='Quick answer',
        qa='A medium portion of {name} ({g} g) contains {kcal} kcal, with {net} g of net carbohydrates and {protein} g of protein. '
           'Its glycemic index is {gi} ({gi_level}) for how fast it raises blood sugar, while its glycemic load per portion is '
           '{gl} ({gl_level}) for its actual effect.',
        qa_na='A medium portion of {name} ({g} g) contains {kcal} kcal, with {net} g of net carbohydrates and {protein} g of protein.',
        choose='Choose a portion', card='Nutrition by portion', ref='reference', g100='100 g',
        servings=dict(small='Small portion', medium='Medium portion', large='Large portion'),
        short=dict(small='Small', medium='Medium', large='Large'),
        col='{label} ({g} g)', macros=('Carbs', 'Protein', 'Fat', 'Fibre'), pct='{v}%',
        energy_note='Percentages of total energy (calories)', energy_aria='Energy split: carbohydrates {c}, protein {p}, fat {f}',
        gi_same='Same for every portion', more='Read more', less='Show less', back='Back to foods'),
    'nl': dict(
        qa_title='Snel antwoord',
        qa='Een middelgrote portie {name} ({g} g) bevat {kcal} kcal, met {net} g netto koolhydraten en {protein} g eiwit. '
           'De glykemische index is {gi} ({gi_level}) voor hoe snel de bloedsuiker stijgt, terwijl de glykemische lading per '
           'portie {gl} ({gl_level}) is voor het werkelijke effect.',
        qa_na='Een middelgrote portie {name} ({g} g) bevat {kcal} kcal, met {net} g netto koolhydraten en {protein} g eiwit.',
        choose='Kies een portie', card='Voedingswaarden per portie', ref='referentie', g100='100 g',
        servings=dict(small='Kleine portie', medium='Middelgrote portie', large='Grote portie'),
        short=dict(small='Klein', medium='Middel', large='Groot'),
        col='{label} ({g} g)', macros=('Koolhydraten', 'Eiwit', 'Vet', 'Vezels'), pct='{v}%',
        energy_note='Percentages van de totale energie (calorieën)', energy_aria='Energieverdeling: koolhydraten {c}, eiwit {p}, vet {f}',
        gi_same='Gelijk voor elke portie', more='Lees meer', less='Toon minder', back='Terug naar voedingsmiddelen'),
    SV: dict(
        qa_title='Snabbt svar',
        qa='En medelstor portion {name} ({g} g) innehåller {kcal} kcal, med {net} g nettokolhydrater och {protein} g protein. '
           'Det glykemiska indexet är {gi} ({gi_level}) för hur snabbt blodsockret stiger, medan den glykemiska belastningen per '
           'portion är {gl} ({gl_level}) för den faktiska effekten.',
        qa_na='En medelstor portion {name} ({g} g) innehåller {kcal} kcal, med {net} g nettokolhydrater och {protein} g protein.',
        choose='Välj portion', card='Näringsvärde per portion', ref='referens', g100='100 g',
        servings=dict(small='Liten portion', medium='Medelstor portion', large='Stor portion'),
        short=dict(small='Liten', medium='Medel', large='Stor'),
        col='{label} ({g} g)', macros=('Kolhydrater', 'Protein', 'Fett', 'Fiber'), pct='{v} %',
        energy_note='Andel av den totala energin (kalorier)', energy_aria='Energifördelning: kolhydrater {c}, protein {p}, fett {f}',
        gi_same='Samma för alla portioner', more='Läs mer', less='Visa mindre', back='Tillbaka till livsmedel'),
}


def num_attr(x):
    """A per-100 g value for a data-v100 attribute: the same float the page was computed from."""
    return repr(float(x))


def energy_ring(food):
    """Energy split (carbohydrate x4, protein x4, fat x9) as dash lengths on a ring of length 100, precomputed."""
    e = (('c', food['carbs'] * 4), ('p', food['protein'] * 4), ('f', food['fat'] * 9))
    total = sum(v for _, v in e)
    share = {k: (v / total * 100 if total else 0.0) for k, v in e}
    segs, start = [], 0.0
    for k, _ in e:
        a = share[k]
        if a >= 0.05:
            gap = 0.9 if a > 3 else 0.3                     # a thin gap between segments, kept visible on small shares
            dash = max(a - gap, 0.3)
            segs.append(f'<circle class="seg seg-{k}" cx="21" cy="21" r="15.9155" pathLength="100" '
                        f'stroke-dasharray="{dash:.2f} {100 - dash:.2f}" stroke-dashoffset="{-start:.2f}"/>')
        start += a
    return share, ''.join(segs)


def write_assets():
    """css/food-page.css (the design system from doctor.html + the food page styles) and the cache-busting versions."""
    css = '/* Generated by scripts/generate_food_pages.py - do not edit by hand. */\n' + \
          '\n'.join(line[8:] if line.startswith('        ') else line for line in (BASE_CSS + PAGE_CSS).split('\n'))
    (ROOT / 'css' / 'food-page.css').write_text(css, encoding='utf-8', newline='\n')
    js = (ROOT / 'js' / 'food-serving.js').read_text(encoding='utf-8')
    short = lambda s: hashlib.sha1(s.encode('utf-8')).hexdigest()[:8]
    return short(css), short(js)


# js/* is served with a one-year immutable cache, so the hand-written pages that load the food data must ask for it by a
# content hash: a new batch (data.js) or a new page (food-pages.js) then reaches every visitor at once.
STAMPED_PAGES = ('foods.html', 'food-details.html')
STAMPED_SCRIPTS = ('data.js', 'food-pages.js', 'food-categories.js')


def stamp_script_versions():
    vers = {n: hashlib.sha1((ROOT / 'js' / n).read_bytes()).hexdigest()[:8] for n in STAMPED_SCRIPTS}
    for page in STAMPED_PAGES:
        path = ROOT / page
        text = path.read_text(encoding='utf-8')
        new = re.sub(r'src="(/?)js/(%s)(?:\?v=[^"]*)?"' % '|'.join(re.escape(n) for n in STAMPED_SCRIPTS),
                     lambda m: f'src="{m.group(1)}js/{m.group(2)}?v={vers[m.group(2)]}"', text)
        if new != text:
            path.write_text(new, encoding='utf-8', newline='\n')
    return vers


ASSET_VER = ('', '')      # (css/food-page.css, js/food-serving.js) content hashes, set in main()


def page_url(slug, lang, absolute=True):
    path = f'/foods/{slug}.html' if lang == 'ar' else f'/{lang}/foods/{slug}.html'
    return SITE + path if absolute else path


def nav_html(lang, active=None):
    """Header capsules shared by every generated page; `active` is the nav path to highlight."""
    u = UI[lang]
    items = list(zip(['/', '/foods.html', '/calculators.html', '/supplements.html', '/#articles'], u['nav'][:5]))
    items += [('/diabetes.html', u['diabetes'])] + list(zip(['/boodi.html'], u['nav'][5:])) + [('/partners.html', u['partners'])]
    out = []
    for path, label in items:
        # the Diabetes hub is a static page per language (/en/diabetes.html), not a ?lang= page
        href = (path if lang == 'ar' else f'/{lang}{path}') if path == '/diabetes.html' else site_link(path, lang)
        cls = 'nav-link' + {'/partners.html': ' nav-partners', '/diabetes.html': ' nav-diabetes'}.get(path, '') + (' active' if path == active else '')
        out.append(f'                <a href="{href}" class="{cls}">{label}</a>')
    return '\n'.join(out)


def langs_of(fid):
    """Languages a food page exists in: ar/en/nl always, sv for the foods in food_sv.PUBLISH."""
    return ALL_LANGS if fid in FSV.PUBLISH else LANGS


def sv_slugs():
    """Slugs of the foods with a Swedish page (from js/food-pages.js), for the article and calculator generators."""
    pages = json.loads(re.search(r'window\.FOOD_PAGES = (\{.*\});', (ROOT / 'js' / 'food-pages.js').read_text(encoding='utf-8')).group(1))
    return {slug for fid, slug in pages.items() if int(fid) in FSV.PUBLISH}


def food_url(slug, fid, lang, absolute=True):
    """A food page in the reader's language; on a Swedish page, foods without a Swedish version open in English."""
    return page_url(slug, lang if lang in langs_of(fid) else 'en', absolute)


def any_link(path, lang):
    """site_link() for every language; Swedish uses the article generator's map of /sv/ pages (imported here, because
    generate_article_pages imports this module)."""
    if lang != SV:
        return site_link(path, lang)
    from generate_article_pages import link
    return link(path, lang)


def site_link(path, lang):
    """Link to a regular site page in the reader's language."""
    if lang == 'ar':
        return path
    path, hash_, frag = path.partition('#')  # the query must sit before an #anchor
    return f"{path}{'&' if '?' in path else '?'}lang={lang}{hash_}{frag}"


def dir_url(kind, lang, absolute=True):
    """Static index page that links every food or supplement page (scripts/generate_directory_pages.py).
    foods.html and supplements.html render their cards in JS, so breadcrumbs and footers point here."""
    path = f'/{kind}/index.html' if lang == 'ar' else f'/{lang}/{kind}/index.html'
    return SITE + path if absolute else path


def replace_sitemap_block(name, lines):
    """Swap the <!-- NAME:START --> ... <!-- NAME:END --> block of sitemap.xml in place (added before </urlset> the first time),
    so re-running one generator does not reorder the other blocks."""
    sm_path = ROOT / 'sitemap.xml'
    sm = sm_path.read_text(encoding='utf-8')
    eol = '\r\n' if '\r\n' in sm else '\n'
    block = eol.join([f'  <!-- {name}:START -->'] + lines + [f'  <!-- {name}:END -->'])
    pattern = re.compile(r'  <!-- %s:START -->.*?<!-- %s:END -->' % (name, name), re.S)
    sm = pattern.sub(lambda m: block, sm, count=1) if pattern.search(sm) else sm.replace('</urlset>', block + eol + '</urlset>', 1)
    sm_path.write_text(sm, encoding='utf-8', newline='')


# --------------------------------------------------------------------------------------------
# Page builder
# --------------------------------------------------------------------------------------------
def build(food, lang, ctx):
    global DECIMAL
    DECIMAL = ',' if lang in (SV, 'nl') else '.'
    u = UI[lang]
    li = ALL_LANGS.index(lang)
    lv, lg = u.get('levels_txt', u['levels']), u.get('levels_gl', u['levels'])    # GI / GL level words in running text
    slug, group, portion = ctx['slug'][food['id']], PILOT[food['id']][0], PILOT[food['id']][1]
    name = food[lang] or food['en']
    # inside Arabic sentences the name takes the definite article; headings keep the display name
    sname = ar_definite(name) if lang == 'ar' else (FSV.NAMES[food['id']][1] if lang == SV else name)
    if lang == 'ar':
        g = ar_pron(name)
    elif lang == SV:                        # capitalised sentence name and the pronoun (det / de for plural names)
        plural = food['id'] in FSV.PLURAL
        det = 'de' if plural else 'det'
        g = {'Name': sname[:1].upper() + sname[1:], 'det': det, 'Det': det.capitalize(), 'dem': 'dem' if plural else 'det'}
    else:
        g = {}
    subtitle = {'ar': food['en'], 'en': food['nl'], 'nl': food['en'], SV: food['en']}[lang]
    if subtitle == name:
        subtitle = ''
    group_name = GROUPS[group][li]
    group_txt = group_name.lower() if lang == SV else group_name      # "i gruppen spannmål och stärkelse"
    measured = food['gi_status'] == 'measured' and food['gi'] is not None      # Atkinson 2021
    reviewed = food['gi_status'] == 'reviewed' and food['gi'] is not None      # clinically reviewed estimate
    has_gi = measured or reviewed
    team = food['id'] in TEAM_REVIEW
    if lang == SV:                          # one approved review line for every Swedish page
        reviewed_line = u['reviewed'].format(doctor=any_link('/doctor.html', lang), date=FSV.REVIEWED_TXT)
    elif food['id'] in NAMED_REVIEW:
        reviewed_line = u['reviewed_named'].format(doctor=site_link('/doctor.html', lang),
                                                   date=NAMED_REVIEW_TXT[NAMED_REVIEW[food['id']]][lang])
    elif team:
        reviewed_line = u['reviewed_team'].format(date=TEAM_REVIEWED_TXT[lang])
    else:
        reviewed_line = u['reviewed'].format(doctor=site_link('/doctor.html', lang), date=REVIEWED_TXT[lang])
    # breadcrumb section: the food's master group on foods.html (labels from js/food-categories.js)
    section = FOOD_GROUP_LABELS.get(food['group'])
    section_href = dir_url('foods', lang, absolute=False) + f"#{food['group']}" if section else ''
    L = lambda path: any_link(path, lang)
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
        lead = u['lead_reviewed'].format(name=sname, kcal=kcal, avail=avail, gi=gi, level=lv[lvl], p=portion,
                                         gl=fmt(gl), gl_level=lg[glv], **g)
        desc = u['desc_reviewed'].format(name=name, kcal=kcal, gi=gi, level=lv[lvl], gl=fmt(gl), p=portion)
    elif measured:
        gi = int(food['gi'])
        lvl = gi_level(gi)
        gl = round(gi * food['avail'] * p_factor / 100, 1)
        glv = gl_level(gl)
        studies = studies_word(int(food['gi_n'] or 1), lang)
        lead = u['lead_measured'].format(name=sname, kcal=kcal, avail=avail, gi=gi, level=lv[lvl], studies=studies,
                                         p=portion, gl=fmt(gl), gl_level=lg[glv], **g)
        desc = u['desc_measured'].format(name=name, kcal=kcal, gi=gi, level=lv[lvl], gl=fmt(gl), p=portion)
    else:
        lead = u['lead_na'].format(name=sname, kcal=kcal, protein=protein, **g)
        desc = u['desc_na'].format(name=name, kcal=kcal, protein=protein)
    # a doctor-approved introduction replaces the computed lead (the numbers stay in the cards and table)
    lead = ctx['overrides'].get(str(food['id']), {}).get('lead', {}).get(lang) or lead
    title = fit_title(name, lang)
    # search-tuned <title> and meta description for high-traffic foods (also used for og: and JSON-LD)
    title_override = ctx['overrides'].get(str(food['id']), {}).get('title', {}).get(lang)
    title = fit_override_title(title_override) if title_override else title
    desc = ctx['overrides'].get(str(food['id']), {}).get('desc', {}).get(lang) or desc

    # -------- FAQ (answers computed from the numbers, unless doctor-approved questions are given)
    faq_override = ctx['overrides'].get(str(food['id']), {}).get('faq', {}).get(lang)
    if faq_override:
        faq = [(item['q'], item['a']) for item in faq_override]
    elif has_gi:
        faq = build_faq(food, lang, sname, portion, True, gi=gi, lvl=lvl, gl=gl, glv=glv, g=g, reviewed=reviewed)
    else:
        faq = build_faq(food, lang, sname, portion, False, g=g)
    # doctor-approved questions appended after the computed ones (batch 22 onwards)
    faq += [(item['q'], item['a']) for item in ctx['overrides'].get(str(food['id']), {}).get('faq_extra', {}).get(lang, [])]
    faq_html = ''.join(f'<details class="acc"{" open" if i == 0 else ""}><summary><h3>{esc(q)}</h3></summary><p>{esc(a)}</p></details>'
                       for i, (q, a) in enumerate(faq))
    read_also = [(READ_ALSO[k][0], *READ_ALSO[k][1][lang])
                 for k in read_also_keys(food, group, food['gi'] if has_gi else None)]
    read_also_html = ''.join(f'<li><a href="{href}">{esc(label)}<span>{READ_ALSO_KIND[kind][lang]}</span></a></li>'
                             for kind, href, label in read_also)
    faq_schema = {
        "@context": "https://schema.org", "@type": "FAQPage", "inLanguage": lang,
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq],
    }

    # -------- comparison & alternatives (within the pilot group)
    peers = [ctx['foods'][i] for i, (g, _) in PILOT.items() if g == group]
    def link_item(f, right):
        return (f'<li><a href="{food_url(ctx["slug"][f["id"]], f["id"], lang, absolute=False)}">'
                f'{esc(f[lang] or f["en"])}'
                f'<span>{right}</span></a></li>')
    family = [ctx['foods'][i] for i in ALTERNATIVES.get(food['id'], []) if i in PILOT]
    def gi_of(f):
        return f['gi'] if f['gi_status'] in ('measured', 'reviewed') and f['gi'] is not None else None
    if has_gi:
        if measured:                        # measured foods are ranked among measured foods only
            ranked = sorted([f for f in peers if f['gi_status'] == 'measured'], key=lambda f: f['gi'])
            rank = [f['id'] for f in ranked].index(food['id']) + 1
            compare_txt = u['rank_measured'].format(rank=rank, m=len(ranked), m_items=ar_measured_items(len(ranked)),
                                                    group=group_txt, **g)
        else:
            ranked = sorted([f for f in peers if gi_of(f) is not None], key=gi_of)
            rank = [f['id'] for f in ranked].index(food['id']) + 1
            compare_txt = u['rank_reviewed'].format(rank=rank, m=len(ranked), group=group_txt, **g)
        if rank == 1:
            compare_txt += ' ' + u['lowest_note']
        lower = sorted([f for f in family if gi_of(f) is not None and gi_of(f) < food['gi']], key=gi_of)
        alts = (lower + [f for f in family if f not in lower])[:3]
        alt_title = u['alt_lower'] if alts and len(lower) == len(alts) else u['alt_family']
        alt_html = ''.join(link_item(f, f"{u.get('gi_short', u['gi'])} {int(gi_of(f))}" if gi_of(f) is not None
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
        compare_txt = tmpl.format(v=v, rank=rank, m=len(ranked), group=group_txt, **g)
        alt_title = u['alt_same']
        alt_html = ''.join(link_item(f, f"{round(f['kcal'])} {u['kcal_unit']}") for f in family[:3])

    # -------- quick answer (static: the medium portion = the approved typical portion)
    fu = FP_UI[lang]
    qa_args = dict(name=sname, g=portion, kcal=round(food['kcal'] * p_factor), net=fmt(food['avail'] * p_factor),
                   protein=fmt(food['protein'] * p_factor), **g)
    quick = (fu['qa'].format(gi=gi, gi_level=lv[lvl], gl=fmt(gl), gl_level=lg[glv], **qa_args) if has_gi
             else fu['qa_na'].format(**qa_args))

    # -------- macro card: portion pills (the medium one checked), energy ring, 2x2 macros, GI / GL
    LV = ('low', 'medium', 'high')
    def live(v100, integer=False):          # a number that follows the portion; it shows the medium portion
        v = v100 * p_factor
        return (f'<b data-v100="{num_attr(v100)}"{" data-int" if integer else ""}>'
                f'{round(v) if integer else fmt(v)}</b>')
    pills = [f'<label class="pill"><input type="radio" name="serving" value="100" data-label="{fu["g100"]}" data-col="{u["col100"]}">'
             f'<span><span class="pill-name">{fu["g100"]}</span><small>{fu["ref"]}</small></span></label>']
    for key, factor in SERVING_FACTORS:
        grams = max(1, int(portion * factor + 0.5))
        label = fu['servings'][key]
        pills.append(f'<label class="pill"><input type="radio" name="serving" value="{grams}" data-label="{label} · {grams} {u["gram"]}"'
                     f' data-col="{esc(fu["col"].format(label=label, g=grams))}"'
                     f'{" checked data-default" if key == "medium" else ""}><span><span class="pill-name">'
                     f'{fu["short"].get(key, label)}</span><small>{grams} {u["gram"]}</small></span></label>')
    share, ring = energy_ring(food)
    pct = lambda k: fu['pct'].format(v=fmt(share[k]))
    macros = ''.join(
        f'<li><i class="dot dot-{k}"></i><span class="m-name">{fu["macros"][i]}</span>'
        f'<span class="m-val">{live(v)} {u["gram"]}</span><span class="m-pct">{pct(k) if k != "fib" else "&nbsp;"}</span></li>'
        for i, (k, v) in enumerate((('c', food['carbs']), ('p', food['protein']), ('f', food['fat']), ('fib', food['fiber']))))
    if has_gi:
        gi_box = (f'<span class="gi-num {LV[lvl]}">{gi}</span><span class="badge {LV[lvl]}">{u["levels"][lvl]}</span>'
                  f'<span class="gi-sub">{u["gi_reviewed"] if reviewed else fu["gi_same"]}</span>')
        gl_box = (f'<span class="gi-num {LV[glv]}" id="glNum">{fmt(gl)}</span>'
                  f'<span class="badge {LV[glv]}" id="glBadge">{u["levels"][glv]}</span>'
                  f'<span class="gi-sub" id="glSub">{u["per_portion"].format(p=portion)}</span>')
        gi_data = f' data-gi="{gi}" data-avail="{num_attr(food["avail"])}" data-levels="{"|".join(u["levels"])}"' \
                  f' data-gl-tpl="{esc(u["per_portion"])}"'
    else:
        gi_box = gl_box = f'<span class="gi-num muted">—</span><span class="badge neutral">{u["na"]}</span>'
        gi_data = ''
    macro_card = f'''<section class="macro-card" id="macroCard" aria-label="{fu["card"]}" data-dec="{DECIMAL}"{gi_data}>
                <fieldset class="servings">
                    <legend class="sr-only">{fu["choose"]}</legend>
                    {"".join(pills)}
                </fieldset>
                <p class="sr-only" id="servingLive" aria-live="polite"></p>
                <div class="macro-body">
                    <figure class="donut" role="img" aria-label="{fu["energy_aria"].format(c=pct("c"), p=pct("p"), f=pct("f"))}">
                        <svg viewBox="0 0 42 42" aria-hidden="true"><circle class="track" cx="21" cy="21" r="15.9155"/>{ring}</svg>
                        <figcaption>{live(food["kcal"], integer=True)}<span>{u["kcal_unit"]}</span></figcaption>
                    </figure>
                    <ul class="macro-legend">{macros}</ul>
                </div>
                <p class="macro-note">{fu["energy_note"]}</p>
                <div class="gi-strip">
                    <div class="gi-box"><span class="gi-label">{u["gi"]}</span>{gi_box}</div>
                    <div class="gi-box"><span class="gi-label">{u["gl"]}</span>{gl_box}</div>
                </div>
            </section>'''

    # -------- nutrition table (the portion column follows the pills)
    def row(label, v100, unit):
        return (f'<tr><td>{label}</td><td>{fmt(v100)} {unit}</td><td>{live(v100)} {unit}</td></tr>')
    rows = ''.join([
        row(u['rows'][0], food['kcal'], u['kcal_unit']), row(u['rows'][1], food['protein'], u['gram']),
        row(u['rows'][2], food['carbs'], u['gram']), row(u['rows'][3], food['avail'], u['gram']),
        row(u['rows'][4], food['fat'], u['gram']), row(u['rows'][5], food['fiber'], u['gram'])])
    if food['ii'] is not None:
        rows += f'<tr><td>{u["ii_row"]}</td><td colspan="2">{int(food["ii"])} · {u["ii_tested"]}</td></tr>'

    # -------- sources: "References & scientific sources" section (only what actually backs this page)
    method_href = L('/methodology.html')
    r = REFS_UI[lang]
    if measured:
        rng = food['gi_range'] or [food['gi'], food['gi']]
        items = [r['measured'] + ref_cite(REF_ATKINSON) + ' ' +
                 u['src_value'].format(studies=studies_word(int(food['gi_n'] or 1), lang), lo=int(rng[0]), hi=int(rng[-1]),
                                       grade=food['gi_grade'] or '-'),
                 r['iso'] + ref_cite(REF_ISO)]
    elif reviewed:
        items = [r['reviewed'] + ref_cite(REF_ISO)]
    else:
        items = [r['na'] + ref_cite(REF_ISO)]
    items.append(r['fao'] + ref_cite(REF_FAO))
    if food['ii'] is not None:
        items.append(r['ii'] + ref_cite(REF_HOLT) + ' • ' + ref_cite(REF_BAO))
    src = (f'<section class="references" aria-labelledby="refs-title">'
           f'<h2 class="section-title" id="refs-title">{icon("book")} <span>{r["title"]}</span></h2>'
           f'<ol class="ref-list">{"".join(f"<li>{x}</li>" for x in items)}</ol>'
           f'<p class="ref-method"><a href="{method_href}">{u["src_link"]}</a></p></section>')

    # -------- head: SEO
    urls = {l: page_url(slug, l) for l in langs_of(food['id'])}
    image_abs = f'{SITE}/{food["image"]}' if food['image'] else f'{SITE}/images/logo.png'
    hreflang = '\n'.join(f'    <link rel="alternate" hreflang="{l}" href="{urls[l]}">' for l in urls)
    if lang == SV:                           # the Swedish role (no title that reads as a Swedish licence)
        from generate_article_pages import DOCTOR_SV
        doctor = {k: DOCTOR_SV[k] for k in ('@type', '@id', 'name', 'jobTitle', 'url')}
        reviewer = doctor
    else:
        doctor = {"@type": "Person", "@id": f"{SITE}/doctor.html#wassim-habib", "name": "Dr. Wassim Habib",
                  "jobTitle": JOB_TITLE[lang], "url": f"{SITE}/doctor.html"}
        reviewer = ({"@type": "Organization", "name": "WiBo Health medical team", "url": SITE + '/'} if team else
                    {"@type": "Person", "@id": f"{SITE}/doctor.html#wassim-habib", "name": "Wassim Habib",
                     "url": f"{SITE}/doctor.html"})
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
        "about": {"@type": "Thing", "name": food['en'],
                  "alternateName": [food['ar'], food['nl']] + ([food[SV]] if SV in urls else [])},
        "isPartOf": {"@type": "WebSite", "name": "WiBo Health", "url": SITE + '/'},
        "relatedLink": [SITE + href for _, href, _ in read_also],
        "author": doctor,
        "publisher": {"@type": "Organization", "name": "WiBo Health", "url": SITE,
                      "logo": {"@type": "ImageObject", "url": f"{SITE}/images/icon-512.png"}},
        "reviewedBy": reviewer,
        "lastReviewed": FSV.REVIEWED if lang == SV else review_date(food['id']),
        "breadcrumb": {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u['home'], "item": SITE + L('/')},
            {"@type": "ListItem", "position": 2, "name": u['guide'], "item": dir_url('foods', lang)}]
            + ([{"@type": "ListItem", "position": 3, "name": section[lang], "item": SITE + section_href}] if section else [])
            + [{"@type": "ListItem", "position": 4 if section else 3, "name": name, "item": urls[lang]}]},
    }

    if lang == SV:
        from generate_article_pages import nav as sv_nav
        nav = sv_nav(lang, active=None)
    else:
        nav = nav_html(lang, active=None)
    lang_links = '\n'.join(
        f'                    <a class="lang-btn{" active" if l == lang else ""}" href="{page_url(slug, l, absolute=False)}" '
        f'hreflang="{l}" lang="{l}"><span>{flag}</span> <span>{l.upper()}</span></a>'
        for l, flag in (('ar', '🇪🇬'), ('nl', '🇳🇱'), ('en', '🇬🇧'), (SV, '🇸🇪')) if l in urls)
    img_html = (f'<img src="/{food["image"]}" alt="{esc(name)}" width="96" height="96" decoding="async">' if food['image']
                else f'<div class="food-emoji" aria-hidden="true">{food["icon"] or "🍽️"}</div>')
    tip_icons = ('check', 'utensils', 'warn')
    tips_html = ''.join(
        f'<details class="acc tip{" warn" if i == 2 else ""}"{" open" if i == 0 else ""}><summary>{icon(tip_icons[i])}'
        f'<h3>{u["tip_titles"][i]}</h3></summary><p>{esc(tips[i])}</p></details>' for i in range(3))
    footer_links = ' <span>•</span> '.join(
        f'<a href="{href}">{label}</a>' for href, label in
        [(L('/'), u['nav'][0]), (dir_url('foods', lang, absolute=False), u['nav'][1]),
         (dir_url('supplements', lang, absolute=False), u['nav'][3]),
         (L('/methodology.html'), u['methodology']),
         (L('/doctor.html'), 'Dr. Wassim Habib' if lang != 'ar' else 'د. وسيم حبيب'),
         (L('/partners.html'), u['partners']), (L('/privacy.html'), u['privacy'])])

    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{u["dir"]}" data-theme="dark">
<head>
{GA_TAG}
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
    <meta property="og:locale" content="{dict(ar='ar_AR', en='en_US', nl='nl_NL', sv='sv_SE')[lang]}">
    <script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=4)}
    </script>
    <script type="application/ld+json">
{json.dumps(faq_schema, ensure_ascii=False, indent=4)}
    </script>
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
    <link rel="stylesheet" href="/css/food-page.css?v={ASSET_VER[0]}">
    <link rel="stylesheet" href="/css/unified-header.css">
    <script src="/js/food-serving.js?v={ASSET_VER[1]}" defer></script>
</head>
<body>
    <header>
        <div class="header-container">
            <a href="{L('/')}" class="brand-link">
                {LOGO_SVG}
                <span class="brand-title">WiBo Health</span>
            </a>
            <nav class="nav-links-bar">
{nav}
            </nav>
            <div class="header-actions">
                <button type="button" class="theme-toggle-btn" onclick="toggleTheme()" title="{u["theme"]}" aria-label="{u["theme"]}">
                    {icon("sun", "ti-sun")}{icon("moon", "ti-moon")}
                </button>
                <div class="lang-switcher-container">
{lang_links}
                </div>
            </div>
        </div>
    </header>

    <main class="page-wrapper food-page fp">
        <article class="about-card">
            <a class="fp-back" href="/foods.html?lang={lang}" data-back>{icon('back')}<span>{fu['back']}</span></a>
            <nav class="breadcrumb" aria-label="breadcrumb">
                <a href="{L('/')}">{u["home"]}</a> › <a href="{dir_url('foods', lang, absolute=False)}">{u["guide"]}</a> › {f'<a href="{section_href}">{esc(section[lang])}</a> › ' if section else ''}<span>{esc(name)}</span>
            </nav>

            <div class="fp-hero">
                {img_html}
                <div class="fp-hero-text">
                    <h1{' class="long"' if len(name) > 30 else ''}>{esc(name)}</h1>
                    <div class="fp-sub">{f'<span class="food-subtitle">{esc(subtitle)}</span>' if subtitle else ''}<span class="group-chip">{group_name}</span></div>
                </div>
            </div>

            <section class="quick-answer" aria-labelledby="qa-title">
                <h2 id="qa-title">{icon("bolt")} {fu["qa_title"]}</h2>
                <p>{esc(quick)}</p>
            </section>

            {macro_card}

            <div class="lead-fold" id="leadFold">
                <p class="lead" id="leadText">{esc(lead)}</p>
                <button type="button" class="more-btn" aria-expanded="false" aria-controls="leadText" data-more="{fu["more"]}" data-less="{fu["less"]}" hidden>{fu["more"]}</button>
            </div>

            <h2 class="section-title"><span>{u["tips"]}</span></h2>
            <div class="acc-list">{tips_html}</div>

            <h2 class="section-title">{icon("table")} <span>{u["table"]}</span></h2>
            <table class="nutrition-table">
                <thead><tr><th>{u["nutrient"]}</th><th>{u["col100"]}</th><th id="colServing">{u["colp"].format(p=portion)}</th></tr></thead>
                <tbody>{rows}</tbody>
            </table>
            <p class="table-note">{u["portion_note"]}</p>

            <h2 class="section-title">{icon("scale")} <span>{u["compare"]}</span></h2>
            <p>{esc(compare_txt)}</p>
            <p><strong>{alt_title}</strong></p>
            <ul class="alt-list">{alt_html}</ul>

            <h2 class="section-title">{icon("question")} <span>{FAQ[lang]["title"]}</span></h2>
            <div class="acc-list">{faq_html}</div>

            <h2 class="section-title">{icon("book")} <span>{READ_ALSO_TITLE[lang]}</span></h2>
            <ul class="alt-list read-also">{read_also_html}</ul>

            <aside class="boodi-card">
                <div>
                    <h2>{u["boodi_title"]}</h2>
                    <p>{u["boodi_text"]}</p>
                </div>
                <a class="boodi-btn" href="{L('/boodi.html')}">{icon("barcode")} {u["boodi_btn"]}</a>
            </aside>

            {src}
            <p class="reviewed">{reviewed_line}</p>
            <p class="disclaimer-box">{u["disclaimer"]}</p>
        </article>
    </main>

    <footer>
        <div class="footer-links">{footer_links}</div>
        <p>{u["footer_rights"]}</p>
    </footer>

    <script>
        function applyTheme(theme) {{
            document.documentElement.setAttribute('data-theme', theme);     // the sun / moon icon follows in CSS
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
    assert FSV.PUBLISH <= set(FSV.NAMES) and set(FSV.NAMES) <= set(PILOT), 'food_sv: unknown food ids'
    # Swedish versions of the food-specific copy sit in food_sv.OVERRIDES; a Swedish page may not fall back to the
    # computed text where the other languages carry approved copy (copy approved in Arabic; a search snippet written
    # for one language, e.g. an English-only title, needs no Swedish twin)
    for fid, o in FSV.OVERRIDES.items():
        for key, value in o.items():
            overrides.setdefault(str(fid), {}).setdefault(key, {})[SV] = list(value) if key == 'tips' else value
    gaps = [(fid, key) for fid in FSV.PUBLISH - FSV.COMPUTED_COPY for key, value in overrides.get(str(fid), {}).items()
            if isinstance(value, dict) and 'ar' in value and 'en' in value and SV not in value]
    assert not gaps, f'food_sv: Swedish copy missing for {gaps}'
    for fid in foods:
        foods[fid][SV] = FSV.NAMES[fid][0] if fid in FSV.NAMES else ''
    ctx = dict(foods=foods, slug=slugs, overrides=overrides)
    global ASSET_VER
    ASSET_VER = write_assets()

    # --only 63,127,...: rebuild just these foods (a trial batch); the slug map and the sitemap are left as they are
    only = None
    if '--only' in sys.argv:
        only = [int(x) for x in sys.argv[sys.argv.index('--only') + 1].split(',')]
        assert set(only) <= set(PILOT), f'unknown food ids: {set(only) - set(PILOT)}'
    written = 0
    for fid in (only or PILOT):
        for lang in langs_of(fid):
            out = ROOT / (f'foods/{slugs[fid]}.html' if lang == 'ar' else f'{lang}/foods/{slugs[fid]}.html')
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(build(foods[fid], lang, ctx), encoding='utf-8', newline='\n')
            written += 1
    if only:
        print(f'pages written: {written} ({len(only)} foods, --only)')
        print('script versions in foods.html / food-details.html:', stamp_script_versions())
        return

    # id -> slug map for foods.html / food-details.html
    (ROOT / 'js' / 'food-pages.js').write_text(
        '// Generated by scripts/generate_food_pages.py - do not edit by hand.\n'
        '// Food id -> slug of its static page (/foods/<slug>.html, /en/foods/..., /nl/foods/...).\n'
        f'window.FOOD_PAGES = {json.dumps({str(k): v for k, v in sorted(slugs.items())}, separators=(",", ":"))};\n',
        encoding='utf-8', newline='\n')
    print('script versions in foods.html / food-details.html:', stamp_script_versions())

    # sitemap block with hreflang alternates
    block = []
    for fid in PILOT:
        for lang in langs_of(fid):
            lastmod = FSV.REVIEWED if lang == SV else review_date(fid)
            block += ['  <url>', f'    <loc>{page_url(slugs[fid], lang)}</loc>', f'    <lastmod>{lastmod}</lastmod>',
                      '    <changefreq>monthly</changefreq>', '    <priority>0.7</priority>']
            block += [f'    <xhtml:link rel="alternate" hreflang="{l}" href="{page_url(slugs[fid], l)}"/>' for l in langs_of(fid)]
            block += [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{page_url(slugs[fid], "ar")}"/>', '  </url>']
    replace_sitemap_block('FOOD-PAGES', block)

    print(f'pages written: {written} ({len(PILOT)} foods x {len(LANGS)} languages, {len(FSV.PUBLISH)} also in Swedish)')
    print('measured:', sum(1 for i in PILOT if foods[i]['gi_status'] == 'measured'),
          '| reviewed:', sum(1 for i in PILOT if foods[i]['gi_status'] == 'reviewed'),
          '| not applicable:', sum(1 for i in PILOT if foods[i]['gi_status'] == 'not_applicable'))


if __name__ == '__main__':
    main()
