import json, os

def _make_rexona_deodorant(pid, gtin, ar_name, en_name, variant_ar, variant_en, type_ar, type_en, volume_ar, volume_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> مزيل ومضاد التعرق المتطور الأصيل من ريكسونا المزود بتقنية الحركة المبتكرة (MotionSense Technology) للحماية الفائقة من التعرق ورائحة العرق لـ 48 إلى 72 ساعة. يرتكز هذا المزيل الفاخر ({en_name}) على كبسولات العرق الذكية المفعلة بالحركة، أملاح الألومنيوم النشطة المضادة للتعرق، وخلاصة {variant_ar}.</p>
<p>يعمل مزيل عرق ريكسونا {variant_ar} على حماية تحت الإبطين من البلل والتعرق الشديد، القضاء التام على البكتيريا المسببة لرائحة العرق الكريهة، وتوفير الانتعاش المستمر كلما تحركت، ليترك إبطيك جافين، ناعمين، ناصعي النظافة، ومعطرين برائحة {variant_ar} طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية فائقة من التعرق والرائحة الكريهة لـ 48-72 ساعة:</strong> يمنع البلل ويبقي الإبطين جافين تماماً.</li>
  <li><strong>تقنية MotionSense الذكية المفعلة بالحركة:</strong> تطلق كبسولات الانتعاش كلما تحركت.</li>
  <li><strong>عطر {variant_ar} المنعش الفواح:</strong> يمنح الإبطين رائحة النظافة والأناقة طوال اليوم.</li>
  <li><strong>مكافحة بكتيريا رائحة العرق من المصدر:</strong> يمنع تكاثر البكتيريا المسببة للروائح.</li>
  <li><strong>تركيبة خالية من الكحول ولا تسبب بقعاً بيضاء أو صفراء:</strong> حماية لطيفة على الجلد والملابس.</li>
  <li><strong>عبوة مدمجة سعة {volume_ar}:</strong> حجم ممتاز للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> رجّي العبوة جيداً أو جهزي قلم الاستيك/الرول أون بعد الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي مزيل عرق ريكسونا {variant_ar} على بشرة إبطين جافة ونظيفة بالكامل.</li>
  <li><strong>الخطوة الثالثة:</strong> دعي المنتج يجف طبيعياً لبضع ثوان قبل ارتداء الملابس (يُستعمل كل صباح وبعد الاستحمام).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>تقنية MotionSense وأملاح الألومنيوم النشطة:</strong> تشكلان حجاباً واقياً ينظم التعرق وتطلق كبسولات الانتعاش بالحركة.</li>
  <li><strong>خلاصة {variant_ar} والمركبات المهدئة:</strong> تعطر الجلد وتهدئ منطقة تحت الإبطين من التهيج.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة تحت الإبطين فقط.</li>
  <li>تجنبي التطبيق على البشرة الملتهبة أو المصابة بجروح بعيد الحلاقة مباشرة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن {ar_name} للحماية من التعرق والانتعاش المستمر بالحركة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ريكسونا (Rexona)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / مزيلات ومضادات التعرق من ريكسونا للنساء {volume_ar}</td></tr>
  <tr><th>نوع المنتج</th><td>مزيل عرق ومضاد تعرق {type_ar} بتقنية MotionSense لـ 48-72 ساعة ({volume_ar})</td></tr>
  <tr><th>الحجم/الوزن</th><td>{volume_ar}</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة تحت الإبطين للنساء</td></tr>
  <tr><th>المظهر النهائي</th><td>إبطان جافان تماماً، ناعمان، خاليان من رائحة العرق ومفعمان بـ {variant_ar}</td></tr>
  <tr><th>الملمس</th><td>{type_ar} ناعم جاف سريع الامتصاص دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر {variant_ar} المنعش الفواح</td></tr>
  <tr><th>المكونات النشطة</th><td>تقنية MotionSense المفعلة بالحركة، أملاح ألومنيوم مضادة للتعرق، خلاصة {variant_ar}</td></tr>
  <tr><th>بلد المنشأ</th><td>الفلبين / المملكة المتحدة / الإمارات</td></tr>
  <tr><th>الشركة المصنعة</th><td>Rexona (Unilever Group)</td></tr>
  <tr><th>الفئة العمرية</th><td>النساء والفتيات (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد تقنية MotionSense والوقاية 72 ساعة في مزيل عرق ريكسونا ({variant_ar})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مزيل عرق ريكسونا {variant_ar} مشكلة البلل الشديد تحت الإبطين، رائحة العرق الكريهة، وتلاشي العطر مع المجهود البدني والحركة.</p>

<h3>لماذا تنجح تقنية MotionSense المفعلة بالحركة؟</h3>
<p>لأن كبسولات العطر الميكروية تلتصق بالجلد وتتكسر بالتناوب مع احتكاك الحركة والنشاط البدني لإطلاق الانتعاش المستمر.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على بشرة جافة ونظيفة تماماً:</strong> يضمن أقصى أداء لمضاد التعرق.<br>
2. <strong>ترك المنتج ليجف ثوانٍ قبل ارتداء الملابس:</strong> يمنح حماية للملابس من البقع.<br>
3. <strong>الاستخدام الصباحي أو قبل ممارسة الرياضة:</strong> يضمن جفافاً وانتعاشاً تاماً طوال اليوم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مضادات التعرق تمنع الجسم من إخراج السموم."<br>
<strong>الحقيقة:</strong> إخراج السموم يتم عن طريق الكبد والكليتين، بينما العرق تحت الإبطين يشكل 1% فقط من تعرق الجسم والتنظيم الحراري.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تذوب هيدروكسي كلوريد الألومنيوم في عرق الإبطين مكونة هيدروجيل مؤقت يغلق قنوات الغدد العرقية المفترزية بنسبة 90%.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو مزيل عرق ومضاد تعرق متطور من ريكسونا بتقنية MotionSense لحماية 48-72 ساعة وعطر {variant_ar} ({volume_ar})."),
        (f"ما هي فوائد تقنية MotionSense وعطر {variant_ar}؟", f"تطلق MotionSense كبسولات الانتعاش كلما تحركت، بينما يغلف عطر {variant_ar} الإبطين برائحة نظافة فواحة."),
        ("هل يحمي من بلل العرق والرائحة لـ 48-72 ساعة؟", "نعم، مثبت سريرياً في توفير جفاف تام وحماية من الرائحة حتى 72 ساعة."),
        (f"ما حجم العبوة؟", f"تأتي بسعة {volume_ar}."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي على بشرة إبطين جافة ونظيفة، دعي المنتج يجف ثوانٍ قبل ارتداء الملابس يومياً."),
        ("هل هو خالي من الكحول؟", "نعم، 100% خالي من الكحول ولا يسبب تهيج الجلد."),
        ("أين صُنع مزيل عرق ريكسونا؟", "صُنع في الفلبين/المملكة المتحدة بواسطة مجموعة Unilever."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات ريكسونا لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {variant_ar} المنعش الفواح."),
        ("هل يترك بقعاً بيضاء أو صفراء على الملابس؟", "لا، تركيبة مطورة لا تترك أثراً أو بقعاً على الملابس."),
        (f"هل العبوة {volume_ar} مناسبة للحقيبة؟", f"نعم، حجم أنيق مدمج مثالي للحقيبة والسفر والتنقل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب ممارسة الرياضة والأنشطة الشاقة؟", "نعم، ممتاز للرياضة بفضل تقنية الموشن المباشرة مع الحركة."),
        ("كم مرة يومياً؟", "مرة واحدة كل صباح أو عند الحاجة."),
        ("هل ريكسونا الماركة الأولى عالمياً في مضادات التعرق؟", "نعم، Rexona العلامة الأكثر شهرة وتوصية في مضادات التعرق عالمياً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب الفتيات والنساء؟", "نعم، مناسب للفتيات والنساء من 12 سنة."),
        ("هل يمنع تكاثر بكتيريا العرق؟", "نعم، يقضي على البكتيريا المسببة لرائحة العرق الكريهة."),
        ("هل يترك الإبطين ناعمين؟", "نعم، يحتوي على مكونات ملطفة تترك الجلد ناعماً ومحمياً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يجف سريعاً على الجلد؟", "نعم، يجف في ثوانٍ معدودة دون لزوجة."),
        ("هل يناسب البشرة الحساسة تحت الإبطين؟", "نعم، مختبر جلدياً وآمن للبشرة الحساسة."),
        ("هل يصلح هدية ضمن مجموعة العناية؟", "نعم، منتج أنيق وعملي جداً في العناية الشخصية."),
        ("هل يحمي في أيام الصيف الحارة؟", "نعم، حماية ممتازة جداً في أشد أيام الصيف حرارة."),
        ("هل يتوفر بأشكال استيك ورول أون وبخاخ؟", "نعم، تتوفر تشكيلة ريكسونا بأشكال متعددة تناسب الجميع.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an advanced authentic antiperspirant deodorant from Rexona engineered with innovative MotionSense Technology for 48 to 72 hours of powerful sweat and odor protection. Built upon smart motion-activated fragrance micro-capsules, active antiperspirant aluminum salts, and {variant_en} extract.</p>
<p>Rexona Deodorant {variant_en} shields underarms against heavy wetness, completely eliminates odor-causing bacteria, and delivers continuous fresh bursts whenever you move, leaving your underarms dry, smooth, spotlessly clean, and fragranced with {variant_en} all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Superior 48-72 Hour Sweat & Odor Protection:</strong> Prevents wetness keeping underarms dry.</li>
  <li><strong>Smart Motion-Activated MotionSense Technology:</strong> Releases fresh bursts of fragrance as you move.</li>
  <li><strong>Fresh & Invigorating {variant_en} Fragrance:</strong> Imparts a long-lasting scent of cleanliness.</li>
  <li><strong>Eliminates Odor-Causing Bacteria at the Source:</strong> Prevents odor-causing bacterial proliferation.</li>
  <li><strong>Alcohol-Free Non-Staining Formula:</strong> Gentle on skin and safe on clothing.</li>
  <li><strong>Compact {volume_en} Format:</strong> Excellent size for daily care, handbag, and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Shake bottle well or prepare roll-on/stick applicator after shower.</li>
  <li><strong>Step 2:</strong> Apply Rexona {variant_en} deodorant onto clean, completely dry underarm skin.</li>
  <li><strong>Step 3:</strong> Allow product to dry naturally for a few seconds before dressing (use daily every morning).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>MotionSense Technology & Active Aluminum Salts:</strong> Form a protective barrier regulating sweat while releasing motion-activated freshness.</li>
  <li><strong>{variant_en} Extract & Soothing Agents:</strong> Fragrance underarms while calming skin from irritation.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical underarm application only.</li>
  <li>Avoid applying onto irritated, broken, or freshly shaved underarm skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every woman seeking {en_name} for reliable sweat protection and motion-activated freshness.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Rexona</td></tr>
  <tr><th>Category</th><td>Personal Care / Rexona Women's Antiperspirants {volume_en}</td></tr>
  <tr><th>Product Type</th><td>{type_en} MotionSense 48-72H Antiperspirant Deodorant ({volume_en})</td></tr>
  <tr><th>Volume/Weight</th><td>{volume_en}</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Women's Underarm Skin Types</td></tr>
  <tr><th>Finish</th><td>Completely dry, smooth underarms fragranced with {variant_en} all day</td></tr>
  <tr><th>Texture</th><td>Smooth lightweight fast-drying {type_en} without stickiness</td></tr>
  <tr><th>Fragrance</th><td>Fresh bright {variant_en} aroma</td></tr>
  <tr><th>Active Ingredients</th><td>MotionSense Micro-Capsules, Aluminum Chlorohydrate, {variant_en} Extract</td></tr>
  <tr><th>Country of Origin</th><td>Philippines / UK / UAE</td></tr>
  <tr><th>Manufacturer</th><td>Rexona (Unilever Group)</td></tr>
  <tr><th>Age Group</th><td>Teens & Women (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Motion-Activated Micro-Capsule Breakage & Apocrine Sweat Duct Occlusion</h2>

<h3>What problem does this solve?</h3>
<p>Rexona Deodorant {variant_en} resolves underarm wetness, body odor, and fragrance fading during exercise and movement.</p>

<h3>Why choose Rexona MotionSense Deodorant?</h3>
<p>MotionSense micro-capsules adhere to skin surfaces and break via physical friction during movement, releasing fresh fragrance bursts continuous with physical activity.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is an advanced antiperspirant deodorant from Rexona with MotionSense technology for 48-72h protection and {variant_en} fragrance ({volume_en})."),
        (f"What are the benefits of MotionSense and {variant_en} fragrance?", f"MotionSense releases fresh bursts as you move, while {variant_en} coats underarms in a clean scent."),
        ("Does it protect against sweat wetness and odor for 48-72 hours?", "Yes, clinically proven to deliver complete dryness and odor defense up to 72 hours."),
        (f"What volume is contained in this container?", f"{volume_en}."),
        ("How do I use it correctly?", "Apply on clean dry underarm skin, let dry for seconds before dressing daily."),
        ("Is it alcohol-free?", "Yes, 100% alcohol-free and does not cause skin irritation."),
        ("Where is Rexona Deodorant manufactured?", "In Philippines/UK by Unilever Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All Rexona products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", f"Fresh bright {variant_en} aroma."),
        ("Does it leave white or yellow marks on clothes?", "No, advanced non-staining formula leaves no marks on clothing."),
        (f"Is the {volume_en} container handbag friendly?", "Yes, sleek compact size ideal for handbag and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for workouts and heavy activity?", "Yes, ideal for sports due to motion-activated bursts."),
        ("How many times daily?", "Once every morning or as needed."),
        ("Is Rexona a #1 global antiperspirant brand?", "Yes, Rexona is the world's #1 recognized antiperspirant brand."),
        ("Is the container recyclable?", "Yes."),
        ("Is it suitable for teens and women?", "Yes, ages 12+."),
        ("Does it eliminate odor-causing bacteria?", "Yes, eliminates bacteria at the root source."),
        ("Does it leave underarms smooth?", "Yes, contains soothing agents leaving underarm skin soft."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it dry quickly on skin?", "Yes, dries in seconds without stickiness."),
        ("Is it suitable for sensitive underarms?", "Yes, dermatologically tested safe for sensitive underarms."),
        ("Is it a practical personal care gift?", "Yes, sleek practical addition to personal care routines."),
        ("Does it protect in hot summer weather?", "Yes, excellent protection during hot summer days."),
        ("Does Rexona offer sticks, roll-ons, and sprays?", "Yes, Rexona offers multiple formats to suit every preference.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Rexona",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. مزيل ومضاد تعرق من ريكسونا بتقنية MotionSense وعطر {variant_ar} لحماية 48-72 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Rexona MotionSense 48-72H antiperspirant deodorant with {variant_en} fragrance. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1958():
    return _make_rexona_deodorant(
        pid=1958, gtin="4800888209689",
        ar_name="مزيل عرق شاور فرش للنساء من ريكسونا  50مل",
        en_name="Rexona Shower Fresh Deodorant for Women - 50ml",
        variant_ar="شاور فرش النظيف", variant_en="Shower Fresh",
        type_ar="رول أون (Roll-On)", type_en="Roll-On", volume_ar="50 مل", volume_en="50ml",
        tags_ar=["ريكسونا", "مزيل_عرق_ريكسونا", "شاور_فرش", "موشن_سينس", "إكليل_أبها"],
        tags_en=["rexona", "rexona_deodorant", "shower_fresh", "motionsense", "ekleel_abha"]
    )


def create_product_1959():
    return _make_rexona_deodorant(
        pid=1959, gtin="8999999049485",
        ar_name="مزيل عرق  موشن اكتيفيتد شغف منعش مضاد للتعرق يدوم 72 ساعة - 45 مل",
        en_name="Motion Activated Passion Fresh 72 Hour Antiperspirant Deodorant - 45 ml",
        variant_ar="شغف منعش (Passion Fresh)", variant_en="Passion Fresh",
        type_ar="ستيك / رول أون", type_en="Stick/Roll-On", volume_ar="45 مل", volume_en="45ml",
        tags_ar=["موشن_اكتيفيتد", "شغف_منعش", "مزيل_عرق_72_ساعة", "مضاد_للتعرق", "إكليل_أبها"],
        tags_en=["motion_activated", "passion_fresh", "72h_antiperspirant", "deodorant", "ekleel_abha"]
    )


def create_product_1960():
    return _make_rexona_deodorant(
        pid=1960, gtin="4800888209689",
        ar_name="مزيل عرق  شاور فريش للنساء من ريكسونا  50مل",
        en_name="Rexona Shower Fresh Deodorant Roll-On for Women - 50ml",
        variant_ar="شاور فريش الانتعاش الفوار", variant_en="Shower Fresh Roll-On",
        type_ar="رول أون (Roll-On)", type_en="Roll-On", volume_ar="50 مل", volume_en="50ml",
        tags_ar=["ريكسونا", "شاور_فريش_رول_اون", "مزيل_عرق_نساء", "ريكسونا_نساء", "إكليل_أبها"],
        tags_en=["rexona", "shower_fresh_rollon", "womens_deodorant", "rexona_women", "ekleel_abha"]
    )


def create_product_1961():
    return _make_rexona_deodorant(
        pid=1961, gtin="4800888220837",
        ar_name="مزيل عرق ستيك بامبو للنساء من ريكسونا  40مل",
        en_name="Rexona Bamboo Deodorant Stick for Women - 40ml",
        variant_ar="خلاصة البامبو الطبيعية", variant_en="Natural Bamboo Extract",
        type_ar="ستيك صلب (Stick)", type_en="Stick", volume_ar="40 مل", volume_en="40ml",
        tags_ar=["ريكسونا", "ستيك_بامبو", "مزيل_عرق_ستيك", "ريكسونا_بامبو", "إكليل_أبها"],
        tags_en=["rexona", "bamboo_stick", "deodorant_stick", "rexona_bamboo", "ekleel_abha"]
    )


def create_product_1962():
    return _make_rexona_deodorant(
        pid=1962, gtin="013867895887",
        ar_name="مزيل عرق ستيك ريتشيز للنساء من ريكسونا  40مل",
        en_name="Rexona Richies Deodorant Stick for Women - 40ml",
        variant_ar="ريتشيز الغني الفاخر", variant_en="Richies Luxury",
        type_ar="ستيك صلب (Stick)", type_en="Stick", volume_ar="40 مل", volume_en="40ml",
        tags_ar=["ريكسونا", "ستيك_ريتشيز", "مزيل_عرق_ستيك", "ريكسونا_نساء", "إكليل_أبها"],
        tags_en=["rexona", "richies_stick", "deodorant_stick", "rexona_richies", "ekleel_abha"]
    )


print("Loaded all 5 Batch 49 builders complete")
