import json, os

def create_product_1943():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>عطر جوفان مسك للرجال 90 مل (Jovan Musk for Men - 90ml)</strong> العطر الرجالي الأيقوني الفاخر والأكثر مبيعاً عبر العقود من دار جوفان الأمريكية المصمم لإضفاء جاذبية ورجولة كلاسيكية لا تُقاوم. يرتكز هذا العطر الفاخر (Jovan Musk Eau de Cologne 90ml) على عبير المسك النقي، الفلفل الأسود، الليمون الحمضي، والأخشاب الدافئة.</p>
<p>يعمل عطر جوفان مسك للرجال على منحك عبيراً خشبياً مسكياً دافئاً يمتزج بطبيعة بشرتك، توفير ثبات وفوحان ممتاز يدوم طوال اليوم، وتعزيز حضورك الرجالي الكلاسيكي الواثق، ليترك انطباعاً ساحراً لا يُنسى في جميع المناسبات واللقاءات.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عبير المسك الكلاسيكي الأيقوني:</strong> رائحة مسكية خشبية دافئة تعكس الرجولة والأناقة.</li>
  <li><strong>ثبات وفوحان ممتاز يدوم طوال اليوم:</strong> يثبت على الجلد والملابس لساعات طويلة.</li>
  <li><strong>امتزاج طبيعي مع كيمياء البشرة:</strong> يمنح كل رجل بصمة عطرية فريدة وخاصة.</li>
  <li><strong>مناسب لجميع الأوقات والمناسبات:</strong> عطر يومي ممتاز للعمل، اللقاءات والمساء.</li>
  <li><strong>عراقة وشهرة دار جوفان العالمية:</strong> رمز الجاذبية الرجالية منذ السبعينيات.</li>
  <li><strong>عبوة زجاجية كلاسيكية سعة 90 مل:</strong> تصميم أنيق ومميز بسعة وافرة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> رشّ العطر على نقاط النبض (الرقبة، المعصمين، وخلف الأذنين) عن بُعد 15 سم.</li>
  <li><strong>الخطوة الثانية:</strong> رشّ رشة خفيفة على الملابس لثبات أطول.</li>
  <li><strong>الخطوة الثالثة:</strong> دع العطر يجف طبيعياً دون فرك المعصمين للحفاظ على جزيئات العطر (يُستعمل عند الحاجة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>المسك النقي والأخشاب الدافئة:</strong> تمنح القاعدة العطرية العمق والثبات والجاذبية.</li>
  <li><strong>الفلفل الأسود والليمون الحمضي:</strong> يمنحان الافتتاحية العطرية انتعاشاً وحيوية رجالية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي فقط.</li>
  <li>تجنب الرش المباشر على العينين أو البشرة المتهيجة.</li>
  <li>يُحفظ بعيداً عن الحرارة المباشرة وأشعة الشمس وأيدي الأطفال.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل رجل يبحث عن عطر جوفان مسك 90 مل للجاذبية المسكية الكلاسيكية والثبات اليومي الممتاز.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جوفان (Jovan)</td></tr>
  <tr><th>الفئة</th><td>العطور الرجالية / عطور جوفان الكلاسيكية للرجال 90ml</td></tr>
  <tr><th>نوع المنتج</th><td>عطر كولونيا مسكي خشبي دافئ للرجال (90ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>90 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة الرجالية</td></tr>
  <tr><th>المظهر النهائي</th><td>رجل معطر بعطري المسك الأيقوني الأنيق بجاذبية وثبات طوال اليوم</td></tr>
  <tr><th>الملمس</th><td>سائل عطري بخاخ رقيق</td></tr>
  <tr><th>العطر</th><td>مسك دافئ، أخشاب، فلفل أسود، وليمون حمضي (Musk & Spicy Woody)</td></tr>
  <tr><th>المكونات النشطة</th><td>مسك نقي، زيوت خشبية دافئة، منكهات حمضية</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة الأمريكية (USA) / فرنسا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Jovan (Coty Inc.)</td></tr>
  <tr><th>الفئة العمرية</th><td>الرجال (من 18 سنة فما فوق)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد المسك النقي والمكونات الخشبية في عطر جوفان مسك (Jovan Musk)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج عطر جوفان مسك للرجال مشكلة سرعة تطاير العطور الخفيفة، عدم ملائمة بعض العطور للاستخدام اليومي، والحاجة لعطر رجالي مسكي جذاب وثابت.</p>

<h3>لماذا تنجح تركيبة جوفان مسك الأيقونية؟</h3>
<p>لأن جزيئات المسك النقي الثقيلة (Macrocyclic Musks) ترتبط بالطبقة الدهنية للبشرة فتتبخر ببطء شديد وتضمن ثباتاً عالي المستوى.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الرش على نقاط النبض الدافئة:</strong> الرقبة والمعصمان يرفعان فوحان العطر بحرارة النبض.<br>
2. <strong>ترطيب البشرة قبل الرش:</strong> البشرة المرطبة بمرطب خالي من العطر تثبت العطر لفترة أطول.<br>
3. <strong>عدم فرك المعصمين بعد الرش:</strong> الفرك يكسر النوتات العطرية العلوية ويقلل ثباتها.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "عطر جوفان مسك يناسب الشتاء فقط."<br>
<strong>الحقيقة:</strong> التوازن بين المسك والليمون والفلفل يجعل جوفان مسك عطراً ممتازاً لجميع الفصول والمناسبات.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تمتلك جزيئات المسك ضغطاً بخارياً منخفضاً (Low Vapor Pressure) يمنحها القدرة على العمل كمثبت عطري (Fixative) للنوتات الحمضية والخشبية.</p>"""

    faqs = [
        ("ما هو عطر جوفان مسك للرجال 90 مل؟", "هو العطر الرجالي المسكي الكلاسيكي الأيقوني من جوفان بتركيبة المسك والأخشاب الدافئة وثبات ممتاز 90 مل."),
        ("ما هي فوائد المسك والأخشاب والفلفل الأسود؟", "يمنح المسك دفئاً وجاذبية تثبت طوال اليوم، بينما تمنح الأخشاب والفلفل انتعاشاً وحيوية رجالية."),
        ("هل يثبت على الجلد والملابس طوال اليوم؟", "نعم، مثبت سريرياً بعطر كولونيا مسكي يدوم طوال اليوم."),
        ("ما حجم العبوة؟", "تأتي بعبوة زجاجية بسعة 90 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "رشّ على نقاط النبض والملابس عن بُعد 15 سم ودعه يجف طبيعياً دون فرك."),
        ("أين صُنع عطر جوفان مسك؟", "صُنع في الولايات المتحدة الأمريكية/فرنسا بواسطة Coty Inc."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع عطور جوفان لدى إكليل أبها أصلية 100%."),
        ("ما عائلة عطر جوفان مسك؟", "عائلة المسك الخشبي التابلي (Woody Spicy Musk)."),
        ("هل يناسب جميع الأوقات والمناسبات؟", "نعم، عطر يومي كلاسيكي ممتاز للعمل والمساء واللقاءات."),
        ("هل 90 مل تكفي لفترة طويلة؟", "نعم، زجاجة 90 مل تكفي لعدة أشهر من الاستخدام اليومي المنتظم."),
        ("كيف أحتفظ بالعطر؟", "في مكان بارد وجاف بعيداً عن الضوء والحرارة المباشرة."),
        ("هل يناسب جميع الفصول؟", "نعم، ممتاز للصيف والشتاء بفضل توازنه العطري."),
        ("كم رشة يُنصح بها؟", "2-4 رشات تكفي لفوحان ممتاز وثبات طوال اليوم."),
        ("هل جوفان ماركة عريقة؟", "نعم، Jovan من أعرق وأشهر ماركات العطور الأمريكية منذ السبعينيات."),
        ("هل يمتزج بكيمياء البشرة؟", "نعم، يمنح كل رجل بصمة عطرية خاصة كلاسيكية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يصلح هدية فاخرة للرجال؟", "نعم، هدية كلاسيكية ممتازة جداً لكل رجل يفضل المسك."),
        ("هل يسبب بقعاً على الملابس البيضاء؟", "رشّ عن بُعد 15 سم لتجنب أي أثر على الأقمشة."),
        ("هل العطور المسكية مرغوبة دائماً؟", "نعم، عطور المسك خيار كلاسيكي لا يزول بمرور الزمن."),
        ("هل يناسب جميع الأعمار للرجال؟", "نعم، مناسب للشباب والكبار من 18 سنة فما فوق."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل بخاخ الزجاجة ناعم ومتجانس؟", "نعم، ينشر الرذاذ العطري بتجانس تام."),
        ("هل يمكن استخدامه بعد الحلاقة؟", "يُفضل استخدامه على نقاط النبض وليس مباشرة على الجلد المحلوق لتجنب الوخز."),
        ("هل يتوفر بأحجام أخرى؟", "يتوفر بأحجام متعددة لدى جوفان."),
        ("هل تركيزه كولونيا أم أو دي تواليت؟", "تركيز كولونيا مسكية ثقيلة وذات ثبات ممتاز.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Jovan Musk for Men - 90ml</strong> is the iconic luxury bestselling men's fragrance across decades from Jovan USA designed to impart an irresistible classic masculine appeal. Built upon pure musk, black pepper, citrus lemon, and warm woody accents.</p>
<p>Jovan Musk for Men gives you a warm woody musky aroma that blends with your natural skin chemistry, provides excellent all-day longevity and sillage, and enhances your confident classic presence, leaving a captivating unforgettable impression in all meetings and occasions.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Iconic Classic Musk Fragrance:</strong> Warm woody musky scent reflecting sophistication and masculinity.</li>
  <li><strong>Excellent All-Day Longevity & Sillage:</strong> Fixes onto skin and clothing for long hours.</li>
  <li><strong>Natural Blend with Skin Chemistry:</strong> Gives every man a unique distinctive fragrance signature.</li>
  <li><strong>Suitable for All Times & Occasions:</strong> Excellent daily fragrance for work, meetings, and evenings.</li>
  <li><strong>Heritage & Renown of Jovan Global Brand:</strong> A symbol of masculine attraction since the 1970s.</li>
  <li><strong>Classic 90ml Glass Bottle:</strong> Elegant bottle design with generous volume.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Spray fragrance onto pulse points (neck, wrists, behind ears) from 15 cm.</li>
  <li><strong>Step 2:</strong> Apply a light mist onto clothing for longer lasting performance.</li>
  <li><strong>Step 3:</strong> Allow to dry naturally without rubbing wrists to protect scent molecules (use as needed).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Musk & Warm Woods:</strong> Impart depth, longevity, and allure to the base.</li>
  <li><strong>Black Pepper & Citrus Lemon:</strong> Give the opening top notes masculine freshness and energy.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical use only.</li>
  <li>Avoid direct spraying into eyes or onto irritated skin.</li>
  <li>Keep away from direct heat, sunlight, and out of reach of children.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every man seeking Jovan Musk 90ml for classic musky allure and excellent daily fragrance longevity.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Jovan</td></tr>
  <tr><th>Category</th><td>Men's Fragrances / Jovan Classic Men's Colognes 90ml</td></tr>
  <tr><th>Product Type</th><td>Warm Woody Spicy Musky Cologne for Men (90ml)</td></tr>
  <tr><th>Volume/Weight</th><td>90 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Men's Skin Types</td></tr>
  <tr><th>Finish</th><td>Concurrently fragranced man with iconic elegant musk appeal all day</td></tr>
  <tr><th>Texture</th><td>Light liquid spray mist</td></tr>
  <tr><th>Fragrance</th><td>Warm Musk, Woods, Black Pepper & Citrus Lemon (Woody Spicy Musk)</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Musk, Warm Wood Oils, Citrus Notes</td></tr>
  <tr><th>Country of Origin</th><td>USA / France</td></tr>
  <tr><th>Manufacturer</th><td>Jovan (Coty Inc.)</td></tr>
  <tr><th>Age Group</th><td>Men (Ages 18+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Macrocyclic Musk Fixation & Epicutaneous Sillage Retention</h2>

<h3>What problem does this solve?</h3>
<p>Jovan Musk for Men resolves rapid fragrance evaporation, unsuitable heavy scents for daily wear, and the desire for a classic masculine musky presence.</p>

<h3>Why choose Jovan Musk for Men?</h3>
<p>Macrocyclic musk molecules possess low vapor pressure acting as natural fixatives that bind to skin epidermal lipids, slowly releasing woody and spicy top notes over hours.</p>"""

    en_faqs = [
        ("What is Jovan Musk for Men - 90ml?", "It is the iconic classic men's musky fragrance from Jovan with pure musk and warm woods in 90ml."),
        ("What are the benefits of pure musk, woods, and black pepper?", "Pure musk delivers warm long-lasting allure, while woods and pepper impart masculine fresh energy."),
        ("Does it stay on skin and clothes all day?", "Yes, clinically proven musky cologne performance lasting all day."),
        ("What volume is contained in this bottle?", "90ml glass bottle."),
        ("How do I use it correctly?", "Spray pulse points and clothes from 15 cm, allow to dry naturally without rubbing."),
        ("Where is Jovan Musk manufactured?", "In USA/France by Coty Inc."),
        ("How do I verify authenticity at Ekleel Abha?", "All Jovan fragrances at Ekleel Abha are 100% original."),
        ("What fragrance family does Jovan Musk belong to?", "Woody Spicy Musk family."),
        ("Is it suitable for all times and occasions?", "Yes, excellent daily scent for work, meetings, and evening wear."),
        ("Does the 90ml bottle last long?", "Yes, lasts months of regular daily use."),
        ("How should I store it?", "In a cool, dry place away from direct light and heat."),
        ("Is it suitable for all seasons?", "Yes, excellent for summer and winter due to balanced composition."),
        ("How many sprays are recommended?", "2-4 sprays are sufficient for excellent sillage and longevity."),
        ("Is Jovan a historic brand?", "Yes, Jovan is an iconic American fragrance brand since the 1970s."),
        ("Does it blend with skin chemistry?", "Yes, gives every man a unique personalized signature scent."),
        ("Is the bottle recyclable?", "Yes."),
        ("Is it a good luxury gift for men?", "Yes, excellent classic gift for any man who appreciates musky scents."),
        ("Does it stain white clothes?", "Spray from 15 cm distance to avoid marks on fabrics."),
        ("Are musky scents timeless?", "Yes, musk fragrances are timeless classics."),
        ("Is it suitable for all men's age groups?", "Yes, suitable for young men and mature adults aged 18+."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is the spray pump smooth?", "Yes, dispenses a fine even fragrance mist."),
        ("Can it be used post-shave?", "Prefer spraying pulse points rather than freshly shaved skin to avoid sting."),
        ("Are other sizes available?", "Jovan offers multiple sizes."),
        ("Is it cologne or EDT concentration?", "Concentrated heavy musky cologne with excellent longevity.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1943",
        "sku": "EK-1943",
        "gtin": "035017009029",
        "brand": "Jovan",
        "ar": {
            "title": "عطر  جوفان مسك للرجال 90 مل",
            "meta_title": "عطر جوفان مسك للرجال 90مل | إكليل أبها",
            "meta_description": "اشتري عطر جوفان مسك للرجال (90 مل). كولونيا رجالية مسكية خشبية كلاسيكية ذات ثبات وفوحان ممتاز. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["جوفان", "جوفان_مسك", "عطر_رجالي_كلاسيكي", "كولونيا_مسك", "إكليل_أبها"]
        },
        "en": {
            "title": "Jovan Musk for Men - 90ml",
            "meta_title": "Jovan Musk for Men 90ml | Ekleel Abha",
            "meta_description": "Buy original Jovan Musk for Men (90ml). Iconic classic woody musky cologne with long-lasting sillage. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["jovan", "jovan_musk", "mens_cologne", "musk_fragrance", "ekleel_abha"]
        }
    }


def _make_whitening_cream(pid, gtin, ar_name, en_name, brand_ar, brand_en, weight_g, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> كريم الجمال والتفتيح الفائق الأصيل المصمم خصيصاً لتفتيح وتوحيد لون بشرة الوجه والتخلص من البقع الداكنة والتصبغات. يرتكز هذا الكريم الفاخر ({en_name}) على خلاصات التفتيح الطبيعية المركزة، الفيتامينات المغذية للبشرة، والمركبات المهدئة المرممة لجلد الوجه.</p>
<p>يعمل كريم {brand_ar} لتبييض الوجه على تقليل إنتاج صبغة الميلانين في المناطق الداكنة، تفتيح النمش والبقع الناتجة عن الشمس وآثار البثور، وتغذية الوجه وترطيبه عمقاً، ليترك بشرتك ناعمة كالحرير، ناصعة البياض، موحدة اللون، ومشرقة من الأسابيع الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وتبييض ناصع لبشرة الوجه:</strong> يقلي البقع الداكنة والتصبغات والنمش بفاعلية.</li>
  <li><strong>توحيد لون الوجه وإعادة النضارة:</strong> يمنح الوجه إشراقة وتوهجاً متجانساً.</li>
  <li><strong>ترطيب عميق وتغذية بالفيتامينات:</strong> يقي البشرة من الجفاف والخشونة.</li>
  <li><strong>تركيبة خفيفة سهلة الامتصاص:</strong> تنفذ لطبقات الجلد دون ترك لزوجة أو دهنية.</li>
  <li><strong>مناسب للاستخدام اليومي الصباحي والمسائي:</strong> نتائج ملحوظة بالاستخدام المنتظم.</li>
  <li><strong>عبوة مدمجة سعة {weight_g} جم:</strong> حجم ممتاز للاستخدام اليومي والعناية الفائقة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> اغسلي بشرة الوجه بغسول مناسب وجففيها برفق.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية صغيرة من كريم {brand_ar} على الوجه والرقبة أو على المناطق المستهدفة بالتصبغات.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي برفق بحركات دائرية ناعمة حتى الامتصاص الكامل (يُستعمل مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركبات التفتيح الطبيعية:</strong> تثبط إنزيم التايروسينيز المسبب للتصبغات الداكنة.</li>
  <li><strong>الفيتامينات والمكونات المرطبة:</strong> تغذي الجلد وتحفظ رطوبته الطبيعية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والرقبة فقط.</li>
  <li>تجنبي التلامس مع العينين.</li>
  <li>يُوصى باستعمال واقي الشمس في النهار لحماية نتائج التفتيح.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لتفتيح وتبييض الوجه وتوحيد لون البشرة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>{brand_ar} ({brand_en})</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات التبييض وتفتيح الوجه الفاخرة {weight_g}g</td></tr>
  <tr><th>نوع المنتج</th><td>كريم تفتيح وتبييض وتوحيد لون الوجه والرقبة ({weight_g}g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>{weight_g} جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (العادية، الجافة والدهنية والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناصع البياض، موحد اللون، ناعم وخالٍ من البقع الداكنة</td></tr>
  <tr><th>الملمس</th><td>كريم ناعم خفيف سريع الامتصاص دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر لطيف ناعم</td></tr>
  <tr><th>المكونات النشطة</th><td>مركبات تفتيح طبيعية، فيتامينات مغذية، مكونات مرطبة</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة المتحدة / آسيا</td></tr>
  <tr><th>الشركة المصنعة</th><td>{brand_en} Beauty Care</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد كريم التفتيح والتبييض للوجه ({brand_ar})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم التبييض مشكلة البقع الداكنة، النمش، آثار البثور والتصبغات الشمسيّة، وعدم توحد لون بشرة الوجه.</p>

<h3>لماذا تنجح تركيبة التفتيح الطبيعية؟</h3>
<p>لأن المواد الفعالة تثبط عمل إنزيم التايروسينيز (Tyrosinase) المسئول عن تشكّل صبغة الميلانين الداكنة في خلايا الجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام الصباحي والمسائي بانتظام:</strong> يسرّع الحصول على نتائج التفتيح.<br>
2. <strong>استخدام واقي الشمس في النهار:</strong> ضروري لحماية الخلايا المفتّحة من أشعة الشمس.<br>
3. <strong>التنظيف الجيد قبل التطبيق:</strong> يضمن أقصى امتصاص للمكونات الفعالة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات التفتيح تبيّض الوجه فورياً في يوم واحد."<br>
<strong>الحقيقة:</strong> التفتيح الآمن يعمل تدريجياً خلال 2-4 أسابيع مع دورة تجدد الخلايا الجسدية الطبيعية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط المواد الفعالة أكسدة L-DOPA إلى Dopaquinone، مما يقلل تخليق الميلانين الداكن Eumelanin كيميائياً.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو كريم تبييض وتفتيح وتوحيد لون الوجه من {brand_ar} بحجم {weight_g} جم."),
        (f"ما هي فوائد كريم التفتيح من {brand_ar}؟", "يقلل البقع الداكنة والتصبغات، يوحد لون الوجه، ويمنح البشرة بياضاً ونضارة ناصعة."),
        ("هل يزيل البقع الداكنة وآثار البثور والنمش؟", "نعم، مثبت سريرياً في تقليل البقع الداكنة وآثار البثور والنمش بفاعلية."),
        (f"ما وزن العبوة؟", f"{weight_g} جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اغسلي الوجه، ضعي كمية صغيرة ودلكي بحركات دائرية على الوجه والرقبة مرتين يومياً."),
        ("هل هو آمن لجميع أنواع البشرة؟", "نعم، آمن ومناسب للبشرة العادية، الجافة، الدهنية والمختلطة."),
        (f"أين صُنع كريم {brand_ar}؟", f"صُنع بأعلى معايير جودة مستحضرات التجميل العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة كريم {brand_ar}؟", "عطر لطيف ناعم منعش."),
        ("هل يمتص بسرعة دون لزوجة؟", "نعم، قوام خفيف يمتص سريعاً دون ترك لزوجة أو دهنية."),
        (f"هل العبوة {weight_g} جم تكفي لفترة جيدة؟", f"نعم، تكفي لعدة أسابيع من الاستخدام اليومي المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يُفضل استخدام واقي شمس معه؟", "نعم، يُوصى بشردة باستعمال واقي الشمس في النهار للحفاظ على النتائج."),
        ("كم مرة يومياً؟", "مرتين يومياً: صباحاً ومساءً."),
        ("متى تظهر نتائج التفتيح؟", "تظهر نتائج ملحوظة خلال 2-4 أسابيع من الاستخدام المنتظم."),
        ("هل يناسب الرقبة أيضاً؟", "نعم، ممتاز لتفتيح وتوحيد لون الوجه والرقبة."),
        ("هل يسبب جفافاً للبشرة؟", "لا، يحتوي على مرطبات تغذي البشرة وتحفظ رطوبتها."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب المراهقين والبالغين؟", "نعم، مناسب من 16 سنة فما فوق."),
        ("هل يصلح هدية؟", "نعم، هدية عملية ومفيدة للعناية بالبشرة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يمكن استخدامه تحت المكياج؟", "نعم، يمتص بسلاسة ويصلح قاعدة خفيفة تحت المكياج."),
        ("هل يوحد لون البشرة المتفاوت؟", "نعم، يعمل على توحيد لون البشرة المتفاوت وتفتيح التصبغات."),
        ("هل يمنح الوجه إشراقة وتوهجاً؟", "نعم، يمنح البشرة توهجاً وإشراقة ناصعة."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب للرجال والنساء.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic premium whitening and beauty cream formulated to brighten, unify facial skin tone, and eliminate dark spots and hyperpigmentation. Built upon concentrated natural brightening extracts, skin-nourishing vitamins, and soothing restorative compounds.</p>
<p>{brand_en} Whitening Cream reduces melanin production in hyperpigmented areas, lightens freckles, sun spots, and post-acne marks, and deeply hydrates and nourishes the face, leaving your skin touchably silky soft, visibly brightened, even-toned, and radiant from the first weeks.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Facial Skin Whitening & Brightening:</strong> Effectively reduces dark spots, hyperpigmentation, and freckles.</li>
  <li><strong>Tone Unification & Radiance Restoration:</strong> Gives face a harmonious luminous glow.</li>
  <li><strong>Deep Hydration & Vitamin Nourishment:</strong> Protects skin from dryness and roughness.</li>
  <li><strong>Lightweight Fast-Absorbing Texture:</strong> Penetrates skin layers without leaving greasiness or stickiness.</li>
  <li><strong>Suitable for Daily Morning & Evening Use:</strong> Noticeable results with continuous regular application.</li>
  <li><strong>Compact {weight_g}g Container:</strong> Excellent size for daily care and target area treatment.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse facial skin with a suitable cleanser and pat dry.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a small amount of {brand_en} cream onto face and neck or targeted dark spot areas.</li>
  <li><strong>Step 3 (Massage):</strong> Massage gently in smooth circular motions until fully absorbed (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Brightening Compounds:</strong> Inhibit tyrosinase enzyme responsible for dark melanin pigmentation.</li>
  <li><strong>Vitamins & Moisturizing Agents:</strong> Nourish skin and preserve natural skin hydration.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and neck skin application only.</li>
  <li>Avoid contact with eyes.</li>
  <li>Recommend sunscreen application during daytime to preserve brightening results.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for facial whitening, skin brightening, and tone unification.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>{brand_en}</td></tr>
  <tr><th>Category</th><td>Skincare / {brand_en} Facial Whitening & Brightening Creams {weight_g}g</td></tr>
  <tr><th>Product Type</th><td>Facial Skin Whitening, Brightening & Tone Evening Cream ({weight_g}g)</td></tr>
  <tr><th>Volume/Weight</th><td>{weight_g} g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Normal, Dry, Oily & Combination)</td></tr>
  <tr><th>Finish</th><td>Spotlessly brightened, even-toned, soft & dark-spot-free facial skin</td></tr>
  <tr><th>Texture</th><td>Lightweight smooth fast-absorbing cream without stickiness</td></tr>
  <tr><th>Fragrance</th><td>Gentle pleasant soft scent</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Brightening Compounds, Vitamins, Hydrating Ingredients</td></tr>
  <tr><th>Country of Origin</th><td>UK / Asia</td></tr>
  <tr><th>Manufacturer</th><td>{brand_en} Beauty Care</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Tyrosinase Inhibition & Melanin Suppression in {brand_en} Whitening</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves dark spots, freckles, post-acne hyperpigmentation, sun discoloration, and uneven facial skin tone.</p>

<h3>Why choose {brand_en} Whitening Cream?</h3>
<p>Active brightening compounds inhibit tyrosinase enzyme oxidation of L-DOPA to Dopaquinone, suppressing dark Eumelanin synthesis in melanocytes.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a facial whitening and skin tone evening cream from {brand_en} in {weight_g}g."),
        (f"What are the benefits of {brand_en} Whitening Cream?", "Reduces dark spots and hyperpigmentation, unifies facial skin tone, and imparts a bright glow."),
        ("Does it remove dark spots, acne marks, and freckles?", "Yes, clinically proven to reduce dark spots, post-acne marks, and freckles effectively."),
        (f"What weight is contained in this tub?", f"{weight_g}g."),
        ("How do I use it correctly?", "Cleanse face, apply small amount, massage in circular motions over face and neck twice daily."),
        ("Is it safe for all skin types?", "Yes, safe and suitable for normal, dry, oily, and combination skin."),
        (f"Where is {brand_en} Cream manufactured?", "Manufactured to international cosmetics quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original."),
        (f"What scent does {brand_en} Cream have?", "Gentle pleasant soft refreshing scent."),
        ("Does it absorb quickly without greasiness?", "Yes, lightweight texture absorbs quickly without leaving greasy residue."),
        (f"Does the {weight_g}g tub last long?", "Yes, lasts weeks of regular daily use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Should I use sunscreen with it?", "Yes, highly recommend daytime sunscreen application to preserve brightening results."),
        ("How many times daily?", "Twice daily: morning and evening."),
        ("When do brightening results appear?", "Noticeable results within 2-4 weeks of regular use."),
        ("Is it suitable for the neck too?", "Yes, excellent for evening face and neck skin tone."),
        ("Does it cause skin dryness?", "No, contains hydrating ingredients that nourish skin."),
        ("Is the packaging recyclable?", "Yes."),
        ("Is it suitable for teens and adults?", "Yes, ages 16+."),
        ("Is it a practical gift?", "Yes, practical and thoughtful gift for skincare routines."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Can it be used under makeup?", "Yes, absorbs smoothly and serves as a lightweight base under makeup."),
        ("Does it unify uneven skin tone?", "Yes, unifies uneven skin tone and lightens hyperpigmentation."),
        ("Does it give face radiance?", "Yes, imparts a bright radiant glow."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": brand_en,
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. كريم لتبييض وتفتيح وتوحيد لون بشرة الوجه وتخفيف البقع الداكنة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Facial whitening and skin tone evening cream for dark spots. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1944():
    return _make_whitening_cream(
        pid=1944, gtin="766730952070",
        ar_name="کريم الجمال لتبييض الوجه من ريكو 50جم",
        en_name="Rico beauty cream for whitening face 50 gm",
        brand_ar="ريكو", brand_en="Rico", weight_g=50,
        tags_ar=["ريكو", "كريم_ريكو", "تبييض_الوجه", "كريم_الجمال", "إكليل_أبها"],
        tags_en=["rico", "rico_cream", "face_whitening", "beauty_cream", "ekleel_abha"]
    )


def create_product_1945():
    return _make_whitening_cream(
        pid=1945, gtin="5019091500455",
        ar_name="کريم للتبيض والجمال من ريو 50جم",
        en_name="Rio Whitening and Beauty Cream 50g",
        brand_ar="ريو", brand_en="Rio", weight_g=50,
        tags_ar=["ريو", "كريم_ريو", "تبييض_البشرة", "كريم_الجمال_ريو", "إكليل_أبها"],
        tags_en=["rio", "rio_whitening", "beauty_cream_rio", "skin_lightening", "ekleel_abha"]
    )


def create_product_1946():
    return _make_whitening_cream(
        pid=1946, gtin="6212410202101",
        ar_name="کريم لتوحيد لون البشرة من بوهلي 20جم",
        en_name="Pohli Skin Tone Evening Cream - 20g",
        brand_ar="بوهلي", brand_en="Pohli", weight_g=20,
        tags_ar=["بوهلي", "كريم_بوهلي", "توحيد_لون_البشرة", "تفتيح_بوهلي", "إكليل_أبها"],
        tags_en=["pohli", "pohli_cream", "skin_tone_evening", "pohli_whitening", "ekleel_abha"]
    )


def create_product_1947():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم تفتيح البشرة ولون الشعر على الوجه والذراعين والجسم من كنت (Skin lightening cream and hair color on the face, arms and body from Kent)</strong> المستحضر الطبي الاحترافي المزدوج المفعول من كنت المصمم لتشقير وتفتيح لون شعر الجسم غير المرغوب فيه وتفتيح لون البشرة المحيطة بأمان وسهولة في المنزل. يرتكز هذا المستحضر (Kent Bleach Cream for Face & Body) على كريم التشقير المنشط، بيروكسيد الهيدروجين المعتمد طبياً، والمكونات المهدئة الملطفة للجلد.</p>
<p>يعمل كريم كنت لتفتيح الشعر والبشرة على تحويل لون الشعر الداكن على الوجه والذراعين والساقين والجسم إلى لون شفاف غير مرئي، تفتيح وتوحيد لون البشرة المحيطة، وتأمين عناية لطيفة تمنع الاحمرار والتهيج، ليترك وجهك وجسمك صافيين، ناعمين، وخاليين من مظاهر الشعر الداكن المزعج.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تشقير وتفتيح مضاعف للشعر والبشرة:</strong> يجعل شعر الوجه والجسم غير مرئي تماماً.</li>
  <li><strong>مناسب للوجه والذراعين والساقين والجسم:</strong> تغطية شاملة للمناطق المراد تشقيرها.</li>
  <li><strong>نتائج سريعة في 10-15 دقيقة فقط:</strong> تحول فوري في لون الشعر الداكن.</li>
  <li><strong>مدعم بمكونات مهدئة لمنع التهيج والاحمرار:</strong> لطيف وآمن على الجلد.</li>
  <li><strong>بديل ممتاز بدون ألم لإزالة الشعر بالشمع أو الخيط:</strong> تفتيح وتشقير آمن وسهل في المنزل.</li>
  <li><strong>عبوة كاملة مجهزة بالمنشط والخلط:</strong> سهولة تامة في التحضير والتطبيق.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (المزج):</strong> امزجي كمية محددة من كريم التشقير مع المسحوق المنشط بالوعاء المرفق حسب النسب المحددة.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وزعي الخليط بالتساوي باستخدام الملعقة المرفقة على الشعر الداكن المراد تشقيره دون فرك.</li>
  <li><strong>الخطوة الثالثة (الانتظار والشطف):</strong> اتركي الخليط لمدة 10-15 دقيقة ثم ازيليه بالملعقة واشطفي البشرة جيداً بالماء البارد (يُستعمل عند الحاجة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>بيروكسيد الهيدروجين المنشط:</strong> يكسر صبغة الميلانين في شعر وجلد الجسم ليحوله إلى لون شفاف ناصع.</li>
  <li><strong>المركبات المهدئة والملطفة:</strong> تحمي البشرة من الاحمرار والتهيج أثناء عملية التشقير.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي فقط على شعر وجلد الوجه والجسم.</li>
  <li>يُوصى بإجراء اختبار حساسية على منطقة صغيرة قبل 24 ساعة من الاستخدام الكامل.</li>
  <li>تجنبي التطبيق قرب العينين أو الحواجب أو الجلد المصاب بجروح.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن كريم كنت لتفتيح وتشقير شعر الوجه والذراعين والجسم بسهولة وبدون ألم.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كنت (Kent)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / كريمات تشقير وتفتيح شعر الوجه والجسم من كنت</td></tr>
  <tr><th>نوع المنتج</th><td>كريم تشقير وتفتيح لون الشعر الداكن على الوجه والذراعين والجسم</td></tr>
  <tr><th>الحجم/الوزن</th><td>عبوة كاملة (كريم + منشط + وعاء وملعقة مزج)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة وشعر الوجه والجسم الداكن</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر وجه وجسم شفاف غير مرئي، وبشرة موحدة اللون وصافية</td></tr>
  <tr><th>الملمس</th><td>كريم ناعم متجانس يُخلط ويوزع بسهولة</td></tr>
  <tr><th>العطر</th><td>عطر لطيف مهدئ</td></tr>
  <tr><th>المكونات النشطة</th><td>بيروكسيد الهيدروجين المنشط، مركب التشقير، مواد مهدئة للجلد</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة المتحدة (UK)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Kent Cosmetics UK</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد التشقير والتفتيح الهيدروجيني في كريم كنت (Kent Bleach Cream)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم كنت مشكلة الشعر الداكن المزعج على الوجه والذراعين والجسم دون الحاجة لطرق إزالة الشعر المؤلمة بالشمع أو الخيط.</p>

<h3>لماذا تنجح تقنية التشقير بالبيروكسيد المنشط؟</h3>
<p>لأن بيروكسيد الهيدروجين المنشط يكسر أربطة صبغة اليوميلانين الداكنة داخل ساق الشعرة والطبقة القرنية ليحوله إلى لون شفاف خفيف.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>اختبار الحساسية أولاً:</strong> وضع كمية صغيرة على الساعد قبل 24 ساعة لضمان سلامة الجلد.<br>
2. <strong>الشطف بالماء البارد دون صابون فورياً:</strong> يهدئ البشرة ويحبس النتيجة.<br>
3. <strong>عدم التعرض للشمس المباشرة فور الاستخدام:</strong> حماية البشرة المفتّحة حديثاً.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريم التشقير يسبب زيادة نمو الشعر."<br>
<strong>الحقيقة:</strong> التشقير يغير لون الشعر السطحي فقط دون أي تأثير على بصيلات الشعر أو سرعة نموه.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تؤكسد جزيئات O2 المحررة مجموعة الكروموفور (Chromophores) في الميلانين الداكن، محولة إياها إلى جزيئات عديمة اللون.</p>"""

    faqs = [
        ("ما هو كريم تفتيح البشرة ولون الشعر من كنت؟", "هو كريم احترافي لتشقير وتفتيح لون الشعر الداكن على الوجه والذراعين والجسم وجعل الشعر غير مرئي من كنت."),
        ("ما هي فوائد بيروكسيد الهيدروجين المنشط والمواد المهدئة؟", "يكسر بيروكسيد الهيدروجين صبغة الشعر الداكنة ليجعل الشعر شفافاً، بينما تحمي المواد المهدئة البشرة من التهيج."),
        ("هل يجعل شعر الوجه والجسم غير مرئي دون ألم؟", "نعم، يشقر الشعر الداكن ويجعله غير مرئي دون أي ألم في 10-15 دقيقة."),
        ("ما محتويات العبوة؟", "تحتوي على كريم التشقير، المسحوق المنشط، وعاء وملعقة المزج."),
        ("كيف يُستخدم بالشكل الصحيح؟", "امزجي الكريم مع المنشط، وزعي على الشعر الداكن 10-15 دقيقة ثم ازيليه واشطفي بالماء البارد."),
        ("هل هو آمن للبشرة الحساسة؟", "نعم، مدعم بمكونات مهدئة، ويُوصى دائماً باختبار الحساسية أولاً."),
        ("أين صُنع كريم كنت؟", "صُنع في المملكة المتحدة بواسطة Kent Cosmetics UK."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كنت لدى إكليل أبها أصلية 100%."),
        ("هل يناسب الوجه والذراعين والساقين؟", "نعم، يناسب تشقير شعر الوجه والذراعين والساقين والجسم."),
        ("ما رائحة كريم كنت؟", "عطر لطيف مهدئ مخصص للتقليل من رائحة المنشط."),
        ("كم دقيقة يترك على البشرة؟", "يترك لمدة 10-15 دقيقة فقط حسب كتافة ولون الشعر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف محكم الإغلاق."),
        ("هل يزيد من كثافة أو نمو الشعر؟", "لا، يغير لون الشعر السطحي فقط دون أي تأثير على البصيلات أو الكثافة."),
        ("كم مرة يُستعمل؟", "يُستعمل عند ظهور الشعر الداكن (كل 3-4 أسابيع)."),
        ("هل هو بديل ممتاز للشمع والخيط؟", "نعم، بديل ممتاز بدون ألم لإخفاء الشعر الداكن."),
        ("هل كنت ماركة بريطانية معتمدة؟", "نعم، Kent من أبرز الماركات البريطانية الشهيرة في مستحضرات التشقير."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يسبب بقعاً على البشرة؟", "لا، ينظف ويوحد لون البشرة المحيطة بالشعر."),
        ("ماذا أفعل في حال حدوث احمرار خفيف؟", "اشطفي بالماء البارد وضعي كريم مهدئ كالزيوت الطبيعية أو زبدة الشيا."),
        ("هل يناسب النساء والرجال؟", "مناسب لكل من يبحث عن تشقير الشعر الداكن."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يسهل تنظيف أدوات الخلط؟", "نعم، اغسلي الوعاء والملعقة بالماء وتجفيفهما لإعادة الاستخدام."),
        ("هل يُستعمل على الحواجب؟", "يُفضل تجنب منطقة العينين والحواجب أو التشقير تحت إشراف متخصص."),
        ("هل تظهر النتائج فورية؟", "نعم، نتائج تشقير وتفتيح فورية بمجرد شطف الكريم."),
        ("هل يناسب المناسبات السريعة؟", "نعم، الحل الأسرع والأمثل قبل المناسبات.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Skin lightening cream and hair color on the face, arms and body from Kent</strong> is a professional dual-action bleaching cream from Kent UK designed to bleach unwanted dark facial and body hair while lightening the surrounding skin safely and easily at home. Formulated with activated bleaching cream, medically approved hydrogen peroxide, and skin-soothing conditioning agents.</p>
<p>Kent Skin & Hair Lightening Cream transforms dark hair on face, arms, legs, and body into a virtually invisible translucent shade, lightens and evens surrounding skin tone, and provides gentle care preventing redness and irritation, leaving your face and body clear, smooth, and free of visible dark hair.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Dual Hair & Skin Bleaching Action:</strong> Renders dark facial and body hair completely invisible.</li>
  <li><strong>Suitable for Face, Arms, Legs & Body:</strong> Comprehensive coverage for target hair areas.</li>
  <li><strong>Fast Results in Just 10-15 Minutes:</strong> Instant transformation of dark hair coloration.</li>
  <li><strong>Enriched with Soothing Agents to Prevent Irritation:</strong> Gentle and safe on skin.</li>
  <li><strong>Pain-Free Alternative to Waxing or Threading:</strong> Easy, safe home hair bleaching.</li>
  <li><strong>Complete Pack with Activator & Mixing Tray:</strong> Effortless preparation and application.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Mix):</strong> Mix the specified ratio of bleach cream with activator powder in the included tray.</li>
  <li><strong>Step 2 (Apply):</strong> Spread mixture evenly using the enclosed spatula over target dark hair without rubbing.</li>
  <li><strong>Step 3 (Wait & Rinse):</strong> Leave for 10-15 minutes, remove with spatula, and rinse skin thoroughly with cold water (use as needed).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Activated Hydrogen Peroxide:</strong> Breaks down melanin pigments inside hair shafts transforming dark hair translucent.</li>
  <li><strong>Soothing & Conditioning Agents:</strong> Protect skin against redness and irritation during bleaching.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and body skin/hair application only.</li>
  <li>Recommend a 24-hour patch test on a small area before full application.</li>
  <li>Avoid applying near eyes, eyebrows, or on broken wounded skin.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every woman seeking Kent Bleach Cream for effortless, pain-free facial, arm, and body hair lightening.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Kent</td></tr>
  <tr><th>Category</th><td>Personal Care / Kent Facial & Body Hair Bleaching Creams</td></tr>
  <tr><th>Product Type</th><td>Pain-Free Hair Bleaching & Skin Lightening Cream Set</td></tr>
  <tr><th>Volume/Weight</th><td>Complete Kit (Bleach Cream + Activator Powder + Tray & Spatula)</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial & Body Skin Types with Dark Unwanted Hair</td></tr>
  <tr><th>Finish</th><td>Invisible translucent hair, bright even-toned clear skin</td></tr>
  <tr><th>Texture</th><td>Smooth consistent cream easily mixed and applied</td></tr>
  <tr><th>Fragrance</th><td>Gentle soft pleasant scent</td></tr>
  <tr><th>Active Ingredients</th><td>Activated Hydrogen Peroxide, Bleaching Complex, Skin Soothers</td></tr>
  <tr><th>Country of Origin</th><td>UK</td></tr>
  <tr><th>Manufacturer</th><td>Kent Cosmetics UK</td></tr>
  <tr><th>Age Group</th><td>Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Activated Peroxide Chromophore Oxidation & Painless Hair Concealment</h2>

<h3>What problem does this solve?</h3>
<p>Kent Bleach Cream resolves unwanted dark hair on face, arms, and body without the pain of waxing, plucking, or threading.</p>

<h3>Why choose Kent Bleach Cream?</h3>
<p>Activated Hydrogen Peroxide oxidizes dark Eumelanin chromophores inside hair cortex shafts, converting dark pigments into colorless structures without affecting hair roots or density.</p>"""

    en_faqs = [
        ("What is Kent Skin & Hair Lightening Cream?", "It is a professional bleach cream set from Kent UK for bleaching dark facial, arm, and body hair to make it invisible."),
        ("What are the benefits of activated hydrogen peroxide and soothers?", "Hydrogen peroxide breaks down dark hair pigment making hair translucent, while soothing agents prevent skin irritation."),
        ("Does it make dark hair invisible painlessly?", "Yes, bleaches dark hair making it translucent and invisible without pain in 10-15 minutes."),
        ("What is included in the box?", "Contains bleach cream, activator powder, mixing tray, and applicator spatula."),
        ("How do I use it correctly?", "Mix cream with activator powder, apply over dark hair for 10-15 minutes, remove spatula and rinse with cold water."),
        ("Is it safe for sensitive skin?", "Yes, formulated with skin soothers; always recommend a 24-hour patch test first."),
        ("Where is Kent Bleach Cream manufactured?", "In the UK by Kent Cosmetics UK."),
        ("How do I verify authenticity at Ekleel Abha?", "All Kent products at Ekleel Abha are 100% original."),
        ("Is it suitable for face, arms, and legs?", "Yes, suitable for bleaching facial, arm, leg, and body hair."),
        ("What scent does Kent Bleach Cream have?", "Gentle soft scent designed to minimize activator odor."),
        ("How many minutes should it stay on skin?", "Leave on for 10-15 minutes depending on hair thickness."),
        ("How should I store it?", "In a cool, dry place tightly closed."),
        ("Does it increase hair growth or thickness?", "No, only changes surface hair color without affecting follicles or growth rate."),
        ("How often can I use it?", "Use whenever dark hair regrows (every 3-4 weeks)."),
        ("Is it a good alternative to waxing and threading?", "Yes, excellent painless alternative to conceal dark hair."),
        ("Is Kent a trusted UK brand?", "Yes, Kent is a premier trusted UK brand in hair bleaching cosmetics."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it cause skin blotches?", "No, cleanses and unifies surrounding skin tone."),
        ("What if slight redness occurs?", "Rinse with cold water and apply a soothing lotion or natural oil."),
        ("Is it suitable for men and women?", "Suitable for anyone seeking to conceal dark body hair."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Are mixing tools reusable?", "Yes, wash tray and spatula with water and dry for next use."),
        ("Can it be used on eyebrows?", "Avoid eye and eyebrow areas unless supervised by a professional."),
        ("Are results instant?", "Yes, instant bleaching results upon rinsing off."),
        ("Is it great before events?", "Yes, fastest painless solution before special events.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1947",
        "sku": "EK-1947",
        "gtin": "5019091500479",
        "brand": "Kent",
        "ar": {
            "title": "كريم تفتيح البشرة   ولون الشعر على الوجه والذراعين والجسم من كنت",
            "meta_title": "كريم كنت لتفتيح البشرة وتشقير الشعر | إكليل أبها",
            "meta_description": "اشتري كريم تفتيح البشرة وتشقير الشعر من كنت. كريم بريطاني احترافي لتشقير شعر الوجه والذراعين والجسم بدون ألم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كنت", "كريم_تشقير_كنت", "تشقير_شعر_الوجه", "تفتيح_البشرة", "إكليل_أبها"]
        },
        "en": {
            "title": "Skin lightening cream and hair color on the face, arms and body from Kent",
            "meta_title": "Kent Skin & Hair Lightening Bleach Cream | Ekleel Abha",
            "meta_description": "Buy original Kent Skin Lightening and Hair Bleaching Cream. Professional UK hair bleaching cream for face, arms, and body. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["kent", "kent_bleach_cream", "hair_lightening", "facial_bleach", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 46 builders complete")
