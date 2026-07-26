import json, os

def _make_bench_cologne_b67(pid, gtin, ar_name, en_name, scent_ar, scent_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> كولونيا ومعطر الجسم اليومي الفواح الفاخر الأصيل من بنش (Bench / Pinch) الفلبينية الشهيرة المصمم لمنح بشرتك وجسمك انتعاشاً يومياً مبهجاً وعطراً ساحراً يدوم طوال اليوم. يرتكز هذا المعطر الأصيل ({en_name}) على الزيوت العطرية الخفيفة المهدئة بنفحات {scent_ar} المنعشة، والمركبات المرطبة لبشرة الجسم.</p>
<p>يعمل معطر بنش دايلي سينت على تعطير الجسم وتنعيم البشرة، السيطرة على روائح التعرق اليومية، وتزويدك بهالة عاطرة مفعمة بالحيوية والشباب، ليترك بشرتك ناعمة، مرطبة، ومعطرة بالنظافة والانتعاش من الرشة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عطر فواح ومبهج يومياً بنفحات {scent_ar}:</strong> يمنح الانتعاش والحيوية طوال اليوم.</li>
  <li><strong>تركيبة خفيفة آمنة على البشرة والملابس:</strong> تنعش دون تسبيب أي تحسس أو بقع.</li>
  <li><strong>السيطرة على روائح التعرق والانتعاش اليومي:</strong> ممتاز للاستخدام بعد الاستحمام والرياضة.</li>
  <li><strong>مناسب للاستخدام اليومي للشباب، الفتيات والأطفال:</strong> عطر النظافة العائلي المثالي.</li>
  <li><strong>جودة Bench العالمية الشهيرة في الكولونيا:</strong> العلامة الأولى في كولونيا Daily Scent.</li>
  <li><strong>زجاجة مدمجة سعة 125 مل:</strong> حجم ممتاز للحقيبة والتنقل والاستخدام اليومي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> رشّي كولونيا بنش على بشرة الجسم والرقبة والملابس بعد الاستحمام أو في أي وقت خلال اليوم.</li>
  <li><strong>الخطوة الثانية:</strong> دعي المعطر يجف طبيعياً واستمتعي بهالة العطور المنعشة (يُستعمل عدة مرات يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الزيوت العطرية الفواحة بنفحات {scent_ar}:</strong> تمنح ثباتاً عطرياً ناعماً ومبهجاً.</li>
  <li><strong>المكونات المائية والمنعشة:</strong> تلطف بشرة الجسم وتمنع الجفاف والتهيج.</li>
</ul>

<h2>تحذيرات وااحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على الجسم والملابس.</li>
  <li>تجنبي الرش المباشر داخل العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن الحرارة والشمس.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} للانتعاش العطري والنظافة اليومية.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بنش / بنتش (Bench / Pinch Daily Scent)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / كولونيا ومعطرات بنش دايلي سينت 125ml</td></tr>
  <tr><th>نوع المنتج</th><td>كولونيا ومعطر جسم يومي بنفحات {scent_ar} (125ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>125 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (النساء، الرجال، والشباب)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم معطر بالانتعاش، ناعم وناصع النظافة بنفحات {scent_ar}</td></tr>
  <tr><th>الملمس</th><td>سائل عطر شفاف رغوي خفيف تنفذ سرعة</td></tr>
  <tr><th>العطر</th><td>عطر {scent_ar} المبهج المنعش لـ Daily Scent</td></tr>
  <tr><th>المكونات النشطة</th><td>زيوت عطرية مهدئة، محاليل منشطة، مرطبات جلدية</td></tr>
  <tr><th>بلد المنشأ</th><td>الفلبين (Philippines)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Suyen Corporation Philippines (Bench)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 10 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد الكولونيا اليومية بنفحات {scent_ar} من بنش (Bench Daily Scent)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج كولونيا بنش مشكلة الروائح اليومية وسرعة تلاشي المعطرات والتسبب في بقع الملابس.</p>

<h3>لماذا تنجح تركيبة Bench Daily Scent؟</h3>
<p>لأن تركيبة الكولونيا الخفيفة المائية تمتزج بمركبات مهدئة تنتشر بسلاسة وتمنح عبقاً ناعماً ممتداً.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الرش فوراً بعد الاستحمام على بشرة رطبة:</strong> يضاعف ثبات العطر على الجلد.<br>
2. <strong>الرش على نقاط النبض (المعصمين والرقبة):</strong> ينشر العطر مع حرارة الجسم الطبيعية.<br>
3. <strong>الاحتفاظ بعبوة 125 مل بالحقيبة:</strong> للتحديث العطري السريع أثناء العمل أو المدرسة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الكولونيا المعطرة تسبب جفاف واسمرار الجلد."<br>
<strong>الحقيقة:</strong> كولونيا بنش مصممة بمكونات مهدئة خفيفة آمنة على الجلد ولا تسبب الاسمرار.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتطاير الجزيئات العطرية بخفة مع حرارة البشرة محققة انبعاثاً عطرياً ناعماً ومتجدداً.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو كولونيا ومعطر جسم يومي فواح من بنش بنفحات {scent_ar} بحجم 125 مل."),
        (f"ما هي فوائد كولونيا بنش دايلي سينت بنفحات {scent_ar}؟", f"تمنح الجسد انتعاشاً وعطراً مبهجاً، تسيطر على روائح التعرق، وتلطف البشرة."),
        ("هل يمنح انتعاشاً وعطراً يدوم طوال اليوم؟", "نعم، مثبت شعبياً وسريرياً في توفير انتعاش عطري مبهج ومستمر."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة سعة 125 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "رشّي على بشرة الجسم والرقبة والملابس بعد الاستحمام ودعيه يجف طبيعياً."),
        ("هل هو آمن على الجلد والملابس ولا يسبب بقعاً؟", "نعم، 100% آمن على الجلد والملابس ولا يترك أي بقع."),
        ("أين صُنعت كولونيا بنش؟", "صُنع في الفلبين بواسطة Suyen Corporation (Bench)."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات بنش لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {scent_ar} المبهج المنعش."),
        ("هل يناسب الشباب والفتيات والأطفال؟", "نعم، عطر النظافة العائلي المثالي للجميع."),
        ("هل عبوة 125 مل مناسبة للحقيبة؟", "نعم، زجاجة أنيقة مدمجة مثالية لحقيبة اليد والسفر والتنقل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الحرارة للشمس."),
        ("هل بنش العلامة الأولى في كولونيا Daily Scent؟", "نعم، Bench العلامة رقم 1 الأكثر شهرة عالمياً في كولونيا Daily Scent."),
        ("كم مرة يومياً؟", "عدة مرات يومياً وعند الحاجة للانتعاش العطري."),
        ("هل يناسب الاستخدام بعد الاستحمام والرياضة؟", "نعم، ممتاز للانتعاش والنظافة بعد السباحة والرياضة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في تنشيط اليوم بالروائح المبهجة؟", "نعم، يمنح طاقة وانتعاشاً عاطراً مبهجاً."),
        ("هل يترك ملمساً ناعماً؟", "نعم، يترك البشرة مرطبة ومعطرة بلمسة ناعمة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للجميع حسب النكهة العطرية المفضلة."),
        ("هل يناسب جميع فصول السنة؟", "نعم، ممتاز للصيف والشتاء والدوام اليومي."),
        ("هل يصلح هدية ممتازة ولطيفة؟", "نعم، هدية أنيقة ومفيدة جداً للطلاب والشباب."),
        ("هل يجف سريعاً على الجلد؟", "نعم، يجف في ثوانٍ معدودة محققاً العبق المطلوب."),
        ("هل تتوفر نكهات أخرى من كولونيا بنش؟", "نعم، تتوفر عائلة Bench Daily Scent خيارات متعددة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic luxury refreshing daily cologne body mist from Bench (Pinch) Philippines designed to infuse your body and skin with uplifting daily freshness and a delightful scent all day. Built upon mild soothing aromatic oils with refreshing {scent_en} notes and skin-moisturizing compounds.</p>
<p>Bench Daily Scent Cologne perfumes body skin, tames daily sweat odors, and surrounds you with a youthful vibrant aura, leaving your skin soft, hydrated, and fragranced with clean freshness from the very first spray.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Uplifting Daily Fresh Fragrance with {scent_en}:</strong> Delivers continuous vibrancy all day.</li>
  <li><strong>Lightweight Formula Safe for Skin & Clothing:</strong> Refreshes without irritation or staining clothes.</li>
  <li><strong>Sweat Odor Control & Daily Refreshment:</strong> Excellent post-shower, post-sports, or daily routine use.</li>
  <li><strong>Suitable for Teens, Adults & Children:</strong> Ideal universal clean family cologne.</li>
  <li><strong>World-Famous Bench Quality:</strong> #1 recognized global brand in Daily Scent colognes.</li>
  <li><strong>Compact 125ml Bottle:</strong> Ideal size for handbag, school, work, and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Spray Bench cologne onto body skin, neck, and clothing post-shower or any time during the day.</li>
  <li><strong>Step 2:</strong> Allow mist to dry naturally and enjoy the refreshing fragrance aura (use multiple times daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Aromatic Essential Oils with {scent_en} Notes:</strong> Provide a smooth, soft, and long-lasting scent aura.</li>
  <li><strong>Aqua & Refreshing Agents:</strong> Soothe body skin preventing tightness and dryness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body and clothing application.</li>
  <li>Avoid direct spraying into eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from heat and direct sunlight.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for daily fragrant refreshment and clean skin softness.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Bench / Pinch (Daily Scent)</td></tr>
  <tr><th>Category</th><td>Body Care / Bench Daily Scent Colognes 125ml</td></tr>
  <tr><th>Product Type</th><td>Daily Fragranced Refreshing Cologne Mist with {scent_en} (125ml)</td></tr>
  <tr><th>Volume/Weight</th><td>125 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Teens, Men & Women)</td></tr>
  <tr><th>Finish</th><td>Refreshed, soft, clean body skin fragranced with {scent_en}</td></tr>
  <tr><th>Texture</th><td>Clear fast-absorbing lightweight liquid mist</td></tr>
  <tr><th>Fragrance</th><td>Uplifting delightful {scent_en} signature Daily Scent</td></tr>
  <tr><th>Active Ingredients</th><td>Soothing Aromatic Oils, Aqua Solubilizers, Skin Hydrators</td></tr>
  <tr><th>Country of Origin</th><td>Philippines</td></tr>
  <tr><th>Manufacturer</th><td>Suyen Corporation Philippines (Bench)</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 10+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Aqua-Based Cologne Vaporization & Volatile Fragrance Diffusion</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves body sweat odors, heavy perfume suffocating notes, and clothing stain issues.</p>

<h3>Why choose Bench Daily Scent Cologne?</h3>
<p>The lightweight water-based cologne formula diffuses refreshing aromatic notes smoothly across skin without staining fabric.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a refreshing daily cologne body mist from Bench with {scent_en} notes (125ml)."),
        (f"What are the benefits of Bench Daily Scent with {scent_en}?", "Delivers uplifting daily freshness, controls sweat odors, and soothes body skin."),
        ("Does it yield a long-lasting refreshing scent?", "Yes, clinically and traditionally proven to deliver continuous delightful fragrance."),
        ("What volume is contained in this bottle?", "125ml compact bottle."),
        ("How do I use it correctly?", "Spray onto body skin, neck, and clothes post-shower and allow to dry naturally."),
        ("Is it safe for skin and clothing without staining?", "Yes, 100% safe for skin and clothing with zero stainings."),
        ("Where is Bench Cologne manufactured?", "In the Philippines by Suyen Corporation (Bench)."),
        ("How do I verify authenticity at Ekleel Abha?", "All Bench products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", f"Uplifting delightful {scent_en} fragrance."),
        ("Is it suitable for teens, adults, and kids?", "Yes, ideal universal clean family cologne."),
        ("Is the 125ml bottle handbag friendly?", "Yes, sleek compact bottle ideal for handbag, school, and travel."),
        ("How should I store it?", "In a cool, dry place away from heat and direct sunlight."),
        ("Is Bench the #1 Daily Scent cologne brand?", "Yes, Bench is the world's most famous #1 brand in Daily Scent colognes."),
        ("How many times daily?", "Multiple times daily whenever refreshing fragrance is needed."),
        ("Is it great post-workout and post-shower?", "Yes, excellent for refreshing shower routines and post-sports freshness."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help energize the day with uplifting notes?", "Yes, imparts vibrant energy and fresh scent."),
        ("Does it leave skin soft?", "Yes, leaves skin touchably soft and fragranced."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for everyone based on fragrance preference."),
        ("Is it good for all seasons?", "Yes, excellent for summer, winter, school, and daily work."),
        ("Is it a nice gift?", "Yes, an elegant practical gift for students and young adults."),
        ("Does it dry quickly on skin?", "Yes, dries in seconds achieving the desired fragrance aura."),
        ("Are other Bench scents available?", "Yes, the full Bench Daily Scent range is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Bench",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. كولونيا ومعطر جسم يومي فواح بنفحات {scent_ar} من بنش دايلي سينت. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Bench Daily Scent refreshing cologne body mist with {scent_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2050():
    return _make_bench_cologne_b67(
        pid=2050, gtin="4800417064888",
        ar_name="روائح معطرة فقاعة البوب من بنتش 125مل",
        en_name="Pinch Bubble Pop Fragrance Mist 125ml",
        scent_ar="فقاعة البوب الزاهية والمبهجة", scent_en="Vibrant Bubble Pop",
        feature_ar="معطر كولونيا فقاعة البوب بنفحات الحلوى المنعشة المبهجة 125 مل", feature_en="vibrant bubble pop sweet fragrance mist cologne 125ml",
        tags_ar=["بنتش", "فقاعة_البوب_بنتش", "معطر_فقاعة_البوب", "كولونيا_بنتش", "إكليل_أبها"],
        tags_en=["pinch", "bubble_pop_mist", "bench_bubble_pop", "daily_scent_mist", "ekleel_abha"]
    )


def create_product_2051():
    return _make_bench_cologne_b67(
        pid=2051, gtin="4800417059556",
        ar_name="روائح معطرة  انديان سمر ديلي سينت من بنتش 125مل",
        en_name="Bench Indian Summer Daily Scent Fragrance Mist 125ml",
        scent_ar="انديان سمر الدافئة والزهور الاستوائية", scent_en="Warm Indian Summer",
        feature_ar="معطر كولونيا انديان سمر بنفحات الصيف الدافئة المنعشة 125 مل", feature_en="indian summer warm floral daily scent fragrance mist 125ml",
        tags_ar=["بنتش", "انديان_سمر_بنش", "كولونيا_انديان_سمر", "معطر_جسم_صيفي", "إكليل_أبها"],
        tags_en=["bench", "indian_summer_mist", "bench_indian_summer", "daily_scent_summer", "ekleel_abha"]
    )


def create_product_2052():
    return _make_bench_cologne_b67(
        pid=2052, gtin="4800417059563",
        ar_name="روائح معطرة ليزي لفترة ما بعد الظهيرة سينت من بنتش 125مل",
        en_name="Pinch Scent Lazy Afternoon Fragrance Mist - 125ml",
        scent_ar="ليزي ما بعد الظهيرة المريحة الهادئة", scent_en="Relaxing Lazy Afternoon",
        feature_ar="معطر كولونيا ليزي أفترنون بنفحات الهدوء والاسترخاء الدافئة 125 مل", feature_en="lazy afternoon relaxing smooth fragrance mist 125ml",
        tags_ar=["بنتش", "ليزي_افترنون_بنتش", "كولونيا_ما_بعد_الظهيرة", "معطر_جسم_هادئ", "إكليل_أبها"],
        tags_en=["pinch", "lazy_afternoon_mist", "bench_lazy_afternoon", "daily_scent_relax", "ekleel_abha"]
    )


def create_product_2053():
    return _make_bench_cologne_b67(
        pid=2053, gtin="4800417059594",
        ar_name="روائح معطرة صباح الاحد من بنتش 125مل",
        en_name="Pinch Sunday Morning Fragrance Mist 125ml",
        scent_ar="صباح الأحد النقية المنعشة", scent_en="Crisp Sunday Morning",
        feature_ar="معطر كولونيا صان داي مورنينغ بنفحات النظافة والصباح المنعش 125 مل", feature_en="sunday morning crisp clean fragrance mist cologne 125ml",
        tags_ar=["بنتش", "صباح_الاحد_بنتش", "كولونيا_صان_داي_مورنينغ", "معطر_النظافة_الصباحي", "إكليل_أبها"],
        tags_en=["pinch", "sunday_morning_mist", "bench_sunday_morning", "daily_scent_morning", "ekleel_abha"]
    )


def create_product_2054():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول جسم عطري المسك الساحر من لوكس 700مل (Lux Magical Musk Fragrant Body Wash - 700ml)</strong> سائل الاستحمام العطري الفاخر الأيقوني من لوكس المصمم لمنح جسمك نظافة عميقة ورغوة مخملية غنية وعطراً فواحاً يدوم لـ 24 ساعة. يرتكز هذا الغسول الأصيل (Lux Magical Musk 700ml) على زيت المسك الأسود والأوركيد الساحر (Black Orchid & Musk Everscent Oil)، خلاصة الزهور النادرة، والمركبات المرطبة لبشرة الجسم.</p>
<p>يعمل غسول لوكس بالمسك الساحر على تنظيف مسام الجسم وإزالة الدهون والأوساخ، حماية الجلد من الجفاف وحفظ طراوته، وتغليف جسمك بنفحات المسك والأوركيد الفواحة الفاخرة، ليترك بشرتك ناعمة كالحرير، مرطبة، ومعطرة بالنظافة والجاذبية طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عطر المسك والأوركيد يدوم لـ 24 ساعة بزيت Everscent:</strong> يمنح الجسد عبقاً جذاباً فواحاً طول اليوم.</li>
  <li><strong>تنظيف عميق ورغوة كريمية غنية:</strong> ينظف الجسم بلطف دون انتزاع الزيوت الطبيعية.</li>
  <li><strong>ترطيب وتنعيم لبشرة الجسم:</strong> يحفظ حاجز الترطيب الطبيعي للجلد.</li>
  <li><strong>تركيبة خفيفة متوازنة الحموضة (pH Balanced):</strong> مناسبة للاستخدام اليومي لجميع أنواع البشرة.</li>
  <li><strong>جودة لوكس (Lux) العالمية الشهيرة:</strong> العلامة الأولى في عطور وجمال الاستحمام.</li>
  <li><strong>عبوة اقتصادية ضخمة سعة 700 مل مزودة بضاغط:</strong> حجم ممتازة يكفي لاستخدام عائلي يومي مستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الجسم بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> اضغطي كمية مناسبة من سائل لوكس على ليفة الاستحمام أو الكفين وكوّني رغوة غنية.</li>
  <li><strong>الخطوة الثالثة:</strong> دلكي الجسم برفق بحركات دائرية ثم اشطفي جيداً بالماء (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت المسك والأوركيد الأساسي:</strong> يثبت العطر الفواح على ألياف البشرة وتمنح انطباعاً عاطراً.</li>
  <li><strong>المنظفات اللطيفة والمركبات المرطبة:</strong> تنظف الجسم وتحفظ نعومته الحريرية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن غسول لوكس بالمسك الساحر 700 مل للانتعاش العطري والنظافة الحريرية.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لوكس (Lux)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / غسولات ومجموعات الاستحمام المعطرة من لوكس 700ml</td></tr>
  <tr><th>نوع المنتج</th><td>غسول جسم عطري مرطب بنفحات المسك الساحر والأوركيد وزيت Everscent (700ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>700 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (العادية، الجافة والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، مرطب، ناصع النظافة ومفعم بعطر المسك لـ 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>سائل جل عطري رغوي غني</td></tr>
  <tr><th>العطر</th><td>عطر المسك الأوركيد الساحر الفواح لـ 24 ساعة</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت Everscent Essential Oil، خلاصة المسك والأوركيد، منظفات لطيفة</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الإمارات</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever Group</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت Everscent وخلاصة المسك في غسول لوكس (Lux Magical Musk)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول لوكس مشكلة جفاف البشرة بعد الاستحمام بالصابون القاسي، تراكم الدهون، وتلاشي عطر النظافة سريعاً.</p>

<h3>لماذا تنجح تركيبة Lux Magical Musk؟</h3>
<p>لأن تقنية زيوت Everscent العطرية تفرز جزيئات المسك والأوركيد التي ترتبط بروابط البروتين الجلدية لتمنح ثباتاً عاطراً لـ 24 ساعة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام اليومي بالماء الدافئ:</strong> ينظف المسام وينشط الدورة الدموية.<br>
2. <strong>استخدام ليفة ناعمة:</strong> يزيد تكوين الرغوة الغنية ويزيل التراكمات السطحية.<br>
3. <strong>الشطف الجيد بالماء:</strong> يضمن عدم بقاء أي ترسبات صابونية على الجلد.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "غسولات الجسم المعطرة تجفف البشرة."<br>
<strong>الحقيقة:</strong> غسول لوكس مدعم بمركبات مرطبة تحفظ التوازن المائي للجلد أثناء التنظيف.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخفض السورفاكتانتات اللطيفة التوتر السطحي للماء وتأطر الجزيئات الزيتية والأوساخ داخل ميكروسفيرات ينشطف بها الماء بسلاسة.</p>"""

    faqs = [
        ("ما هو غسول جسم عطري المسك الساحر من لوكس 700مل؟", "هو سائل استحمام عطري فاخر من لوكس بنفحات المسك الساحر وزيت Everscent لثبات العطر 24 ساعة (700 مل)."),
        ("ما هي فوائد خلاصة المسك والأوركيد وزيت Everscent؟", "تنظف المنظفات اللطيفة البشرة دون جفاف، بينما يثبت زيت Everscent عطر المسك لـ 24 ساعة."),
        ("هل يمنح رغوة غنية وعطراً يدوم لـ 24 ساعة؟", "نعم، مثبت سريرياً في توفير رغوة غنية وثبات عطري يدوم 24 ساعة."),
        ("ما حجم العبوة؟", "تأتي بعبوة ضخمة مزودة بضاغط بسعة 700 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الجسم، اضغطي كمية على الليفة وكوّني رغوة، دلكي برفق واشطفي بالماء يومياً."),
        ("هل هو آمن لجميع أنواع البشرة؟", "نعم، تركيبة متوازنة الحموضة آمنة لجميع أنواع بشرة الجسم."),
        ("أين صُنع غسول لوكس؟", "صُنع بواسطة مجموعة Unilever العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لوكس لدى إكليل أبها أصلية 100%."),
        ("ما رائحة غسول لوكس بالمسك الساحر؟", "عطر المسك والأسود والأوركيد الساحر الفواح الأنيق."),
        ("هل يترك البشرة ناعمة ومرطبة؟", "نعم، يحافظ على رطوبة الجلد ونعومته الحريرية."),
        ("هل 700 مل تكفي للاستخدام العائلي؟", "نعم، عبوة ضخمة بضاغط تكفي لعدة أشهر من الاستخدام العائلي اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع أفراد الأسرة وخاصة محبي عطور المسك الفاخرة."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً أثناء الاستحمام."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، ينشطف بالماء الدافئ بسهولة دون ترك أثر لزج."),
        ("هل لوكس علامة عالمية شهيرة؟", "نعم، Lux علامة رائدة ومشهورة جداً عالمياً لمنتجات الاستحمام العطرية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في إزالة رائحة العرق؟", "نعم، ينظف بفاعلية ويعطر الجسم بنفحات عاطرة."),
        ("هل يناسب الاستخدام بعد الرياضة؟", "نعم، ممتاز للانتعاش والنظافة بعد التمارين والرياضة."),
        ("هل يترك أثراً دهنياً؟", "لا، ينظف وينشطف بالكامل دون دهنية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل العبوة مزودة بضاغط مريح؟", "نعم، ضاغط مريح جداً يسهل استخدام الجل أثناء الاستحمام."),
        ("هل يناسب الشتاء والصيف؟", "نعم، ممتاز لجميع فصول السنة."),
        ("هل يصلح هدية ضمن مجموعة الاستحمام؟", "نعم، خيار ممتاز جداً في مجموعات العناية الشخصية."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Lux Magical Musk Fragrant Body Wash - 700ml</strong> is an iconic luxury fragranced body wash from Lux designed to deliver deep cleansing, a rich velvety lather, and a 24-hour long-lasting musk fragrance. Built upon Everscent Essential Oil technology, seductive Black Orchid & Musk extracts, and body-moisturizing compounds.</p>
<p>Lux Magical Musk Body Wash cleanses body pores of dirt and excess sebum, guards skin against dryness, and wraps your body in captivating musk and orchid notes, leaving your skin touchably silky soft, hydrated, and fragranced with elegance all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>24-Hour Long-Lasting Musk Fragrance with Everscent Oil:</strong> Coats body in a captivating musk scent all day.</li>
  <li><strong>Deep Cleansing & Rich Creamy Lather:</strong> Cleanses body gently without stripping natural skin oils.</li>
  <li><strong>Body Skin Softening & Hydration:</strong> Preserves the skin's natural moisture barrier.</li>
  <li><strong>pH-Balanced Mild Formula:</strong> Suitable for daily use on all skin types.</li>
  <li><strong>Famous Quality of Lux Global:</strong> #1 recognized brand in perfumed bath and beauty care.</li>
  <li><strong>Generous 700ml Jumbo Pump Bottle:</strong> Excellent value lasting months of continuous daily family use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet body skin with warm water during shower.</li>
  <li><strong>Step 2:</strong> Pump a suitable amount of Lux gel onto a shower loofah or hands and work into a rich lather.</li>
  <li><strong>Step 3:</strong> Massage body gently in circular motions, then rinse thoroughly with water (use daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Everscent Essential Oil & Musk Extract:</strong> Bind fragrance molecules to skin layers delivering 24-hour freshness.</li>
  <li><strong>Gentle Cleansers & Hydrating Agents:</strong> Cleanse body while maintaining touchable silky softness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application only.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every woman seeking Lux Magical Musk 700ml Body Wash for 24-hour fragrance and silky clean skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lux</td></tr>
  <tr><th>Category</th><td>Body Care / Lux Perfumed Hydrating Body Washes 700ml</td></tr>
  <tr><th>Product Type</th><td>24H Perfumed Magical Musk & Everscent Essential Oil Body Wash (700ml)</td></tr>
  <tr><th>Volume/Weight</th><td>700 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Normal, Dry & Oily Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, hydrated, spotlessly clean body skin fragranced with Musk for 24H</td></tr>
  <tr><th>Texture</th><td>Rich foaming fragranced clear gel fluid</td></tr>
  <tr><th>Fragrance</th><td>Captivating long-lasting Magical Musk & Orchid floral scent for 24 hours</td></tr>
  <tr><th>Active Ingredients</th><td>Everscent Essential Oil, Black Orchid & Musk Extract, Gentle Cleansers</td></tr>
  <tr><th>Country of Origin</th><td>KSA / UAE</td></tr>
  <tr><th>Manufacturer</th><td>Unilever Group</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Everscent Essential Oil Binding & 24-Hour Musk Fragrance Retention</h2>

<h3>What problem does this solve?</h3>
<p>Lux Magical Musk Body Wash resolves skin dryness caused by harsh soaps, daily sweat accumulation, and fading body fragrance.</p>

<h3>Why choose Lux Body Wash?</h3>
<p>Everscent Essential Oil technology binds perfume micro-droplets to skin keratin providing sustained 24-hour fragrance release.</p>"""

    en_faqs = [
        ("What is Lux Magical Musk Fragrant Body Wash - 700ml?", "It is a luxury perfumed body wash from Lux with Magical Musk and Everscent Oil for 24-hour fragrance (700ml)."),
        ("What are the benefits of Musk extract and Everscent Oil?", "Gentle cleansers cleanse skin without dryness, while Everscent Oil binds Musk fragrance for 24 hours."),
        ("Does it yield a rich lather and 24-hour fragrance?", "Yes, clinically proven to produce a rich lather and deliver 24-hour fragrance retention."),
        ("What volume is contained in this bottle?", "700ml jumbo pump bottle."),
        ("How do I use it correctly?", "Wet body, pump gel onto loofah, lather, massage gently and rinse with water daily."),
        ("Is it safe for all skin types?", "Yes, pH-balanced formula safe for all body skin types."),
        ("Where is Lux Body Wash manufactured?", "By Unilever Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All Lux products at Ekleel Abha are 100% original."),
        ("What scent does Lux Magical Musk have?", "Captivating elegant Magical Musk and Orchid fragrance."),
        ("Does it leave skin soft and hydrated?", "Yes, preserves skin moisture and silky softness."),
        ("Does 700ml last long for family use?", "Yes, jumbo pump bottle lasts months of regular family use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for men and women?", "Yes, suitable for the entire family."),
        ("How many times daily?", "Once or twice daily during showers."),
        ("Does it rinse off easily?", "Yes, rinses off smoothly with warm water without sticky residue."),
        ("Is Lux a world-famous brand?", "Yes, Lux is a globally leading brand in perfumed bath care."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help remove sweat odor?", "Yes, effectively cleanses and perfumes body skin."),
        ("Is it good post-workout?", "Yes, excellent for post-workout refreshing shower routines."),
        ("Does it leave a greasy film?", "No, cleanses completely clean without greasiness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is the pump bottle convenient?", "Yes, convenient pump dispenser for easy showering."),
        ("Is it good for summer and winter?", "Yes, excellent for all seasons."),
        ("Is it a nice shower gift?", "Yes, excellent addition to personal care gift sets."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2054",
        "sku": "EK-2054",
        "gtin": "6281006569980",
        "brand": "Lux",
        "ar": {
            "title": "غسول جسم عطري المسك الساحر  من لوكس 700مل",
            "meta_title": "غسول جسم لوكس بالمسك الساحر 700مل | إكليل أبها",
            "meta_description": "اشتري غسول جسم عطري المسك الساحر من لوكس (700 مل). سائل استحمام بعطر المسك الفواح لـ 24 ساعة وترطيب البشرة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["لوكس", "غسول_جسم_لوكس_بالمسك", "المسك_الساحر", "سائل_استحمام_معطر", "إكليل_أبها"]
        },
        "en": {
            "title": "Lux Magical Musk Fragrant Body Wash - 700ml",
            "meta_title": "Lux Magical Musk Body Wash 700ml | Ekleel Abha",
            "meta_description": "Buy original Lux Magical Musk Fragrant Body Wash (700ml). 24H perfumed Magical Musk body wash. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["lux", "lux_magical_musk", "musk_body_wash", "perfumed_body_wash", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 67 builders complete")
