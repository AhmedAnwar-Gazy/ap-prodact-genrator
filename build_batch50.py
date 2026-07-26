import json, os

def _make_deodorant_generic(pid, gtin, ar_name, en_name, brand_ar, brand_en, variant_ar, variant_en, volume_ar, volume_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> مزيل ومضاد التعرق الأيقوني الأصيل من {brand_ar} المصمم للحماية التامة والعناية المتقدمة تحت الإبطين لـ 48 ساعة. يرتكز هذا المزيل الفاخر ({en_name}) على أملاح الحماية النشطة من التعرق، المركبات المهدئة للجلد، وعطر {variant_ar} المنعش الفواح.</p>
<p>يعمل مزيل عرق {brand_ar} على منع البلل والتعرق المزعج تحت الإبطين، التخلص التام من البكتيريا المسببة لرائحة العرق الكريهة، وتغذية الجلد الحساس في منطقة الإبطين، ليترك بشرتك جافة، ناعمة، موحدة اللون، ومعطرة بعطر {variant_ar} طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية موثوقة من التعرق ورائحة العرق لـ 48 ساعة:</strong> يضمن جفافاً ونظافة فائقتين طوال اليوم.</li>
  <li><strong>عطر {variant_ar} الفواح والأنيق:</strong> يغلف الإبطين بنفحات الانتعاش والنقاء.</li>
  <li><strong>عناية ولطف ببشرة تحت الإبطين الحساسة:</strong> يمنع التهيج ويحفظ الملمس الناعم.</li>
  <li><strong>القضاء على البكتيريا المسببة للرائحة من المصدر:</strong> حماية فعال ضد الروائح الكريهة.</li>
  <li><strong>تركيبة خالية من الكحول ولا تترك أثراً على الملابس:</strong> آمنة ولطيفة تماماً.</li>
  <li><strong>عبوة مدمجة سعة {volume_ar}:</strong> حجم أنيق مثالي للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي/رشّي مزيل عرق {brand_ar} على بشرة إبطين جافة ونظيفة بالكامل بعد الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> دعي المنتج يجف طبيعياً لبضع ثوان قبل ارتداء الملابس (يُستعمل كل صباح).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>أملاح الحماية النشطة والمكونات المهدئة:</strong> تنظم إفراز التعرق وتحفظ نعومة جلد الإبطين.</li>
  <li><strong>زيوت {variant_ar} العطرية المركزة:</strong> تمنح الإبطين رائحة النقاء والانتعاش الفواح طوال اليوم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة تحت الإبطين فقط.</li>
  <li>تجنبي التطبيق على البشرة الملتهبة أو المصابة بجروح بعيد الحلاقة مباشرة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} للحماية من التعرق والانتعاش اليومي الفواح.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>{brand_ar} ({brand_en})</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / مزيلات ومضادات التعرق من {brand_ar} {volume_ar}</td></tr>
  <tr><th>نوع المنتج</th><td>مزيل عرق ومضاد تعرق بـ 48 ساعة حماية بعطر {variant_ar} ({volume_ar})</td></tr>
  <tr><th>الحجم/الوزن</th><td>{volume_ar}</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة تحت الإبطين (العادية والحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>إبطان جافان تماماً، ناعمان، خاليان من الرائحة ومفعمان بـ {variant_ar}</td></tr>
  <tr><th>الملمس</th><td>سائل/ستيك/رول أون ناعم سريع الامتصاص والجفاف</td></tr>
  <tr><th>العطر</th><td>عطر {variant_ar} المنعش الفواح</td></tr>
  <tr><th>المكونات النشطة</th><td>أملاح ألومنيوم مضادة للتعرق، زيوت عطرية، مركبات مهدئة</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا / سويسرا / الفلبين</td></tr>
  <tr><th>الشركة المصنعة</th><td>{brand_en} Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد الوقاية من التعرق وخلاصات {variant_ar} في مزيل {brand_ar}</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مزيل عرق {brand_ar} مشكلة البلل والتعرق الزائد تحت الإبطين، رائحة العرق، والتهيج الجلدي الناتج عن التعرق.</p>

<h3>لماذا تنجح تركيبة {brand_ar}؟</h3>
<p>لأن المواد الفعالة تنظم عمل الغدد العرقية دون سد المسام بالكامل بينما تقضي المكونات المطهرة على البكتيريا المسببة للروائح.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على بشرة جافة ونظيفة تماماً:</strong> بعد الاستحمام صباحاً.<br>
2. <strong>ترك المنتج ليجف ثوانٍ قبل ارتداء الملابس:</strong> يمنح حماية أفضل للأنسجة والملابس.<br>
3. <strong>الاستخدام المنتظم:</strong> يضمن حماية متكاملة طوال 48 ساعة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مزيلات العرق تسبب اسمرار منطقة تحت الإبطين."<br>
<strong>الحقيقة:</strong> هذا المنتج خالي من الكحول والمواد القاسية ومصمم بمركبات مهدئة تحمي من الاسمرار والتهيج.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تذوب أملاح مضاد التعرق في إفرازات الإبطين المائية مكونة هيدروجيل مؤقت يحد من تدفق العرق ويفكك الدهون البكتيرية.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو مزيل عرق ومضاد تعرق متطور من {brand_ar} بعطر {variant_ar} لحماية 48 ساعة ({volume_ar})."),
        (f"ما هي فوائد مركبات الوقاية وعطر {variant_ar}؟", f"تضمن مركبات الوقاية جفافاً تاماً من التعرق، بينما يمنح عطر {variant_ar} الإبطين رائحة نظافة فواحة."),
        ("هل يحمي من بلل العرق والرائحة لـ 48 ساعة؟", "نعم، مثبت سريرياً في توفير جفاف تام وحماية من الرائحة حتى 48 ساعة."),
        (f"ما حجم العبوة؟", f"تأتي بسعة {volume_ar}."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي/رشّي على بشرة إبطين جافة ونظيفة، دعي المنتج يجف ثوانٍ قبل ارتداء الملابس يومياً."),
        ("هل هو خالي من الكحول؟", "نعم، 100% خالٍ من الكحول ولا يسبب تهيج الجلد."),
        (f"أين صُنع مزيل عرق {brand_ar}؟", f"صُنع بأعلى معايير جودة العناية الشخصية العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {variant_ar} المنعش الفواح."),
        ("هل يترك بقعاً بيضاء أو صفراء على الملابس؟", "لا، تركيبة مطورة لا تترك أثراً أو بقعاً على الملابس."),
        (f"هل العبوة {volume_ar} مناسبة للحقيبة؟", f"نعم، حجم أنيق مدمج مثالي للحقيبة والسفر والتنقل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب ممارسة الرياضة والأنشطة الشاقة؟", "نعم، ممتاز للانتعاش والنظافة أثناء وبعد التمارين والرياضة."),
        ("كم مرة يومياً؟", "مرة واحدة كل صباح أو عند الحاجة."),
        (f"هل {brand_ar} ماركة عالمية شهيرة؟", f"نعم، {brand_en} علامة رائدة وموثوقة جداً في العناية الشخصية ومزيلات العرق."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب الفتيات والنساء/الرجال؟", "نعم، مناسب لجميع الفئات حسب التخصص."),
        ("هل يمنع تكاثر بكتيريا العرق؟", "نعم، يقضي على البكتيريا المسببة لرائحة العرق الكريهة."),
        ("هل يترك الإبطين ناعمين؟", "نعم، يحتوي على مكونات ملطفة تترك الجلد ناعماً ومحمياً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يجف سريعاً على الجلد؟", "نعم، يجف في ثوانٍ معدودة دون لزوجة."),
        ("هل يناسب البشرة الحساسة تحت الإبطين؟", "نعم، مختبر جلدياً وآمن للبشرة الحساسة."),
        ("هل يصلح هدية ضمن مجموعة العناية؟", "نعم، منتج أنيق وعملي جداً في العناية الشخصية."),
        ("هل يحمي في أيام الصيف الحارة؟", "نعم، حماية ممتازة جداً في أيام الصيف الحارة."),
        ("هل يغني عن المعطرات العادية؟", "نعم، يجمع بين حماية التعرق والتعطير الفاخر.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic advanced antiperspirant deodorant from {brand_en} designed to deliver 48-hour reliable protection and care for underarm skin. Formulated with active antiperspirant protective salts, skin-soothing compounds, and {variant_en} fragrance.</p>
<p>{brand_en} Deodorant protects underarms against wetness and heavy sweating, completely eliminates odor-causing bacteria, and nourishes delicate underarm skin, leaving your underarms dry, smooth, even-toned, and fragranced with {variant_en} all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Reliable 48-Hour Sweat & Odor Protection:</strong> Keeps underarms spotlessly clean and dry all day.</li>
  <li><strong>Fresh Elegant {variant_en} Fragrance:</strong> Coats underarms in long-lasting freshness.</li>
  <li><strong>Gentle Care for Sensitive Underarm Skin:</strong> Prevents skin irritation maintaining touchable softness.</li>
  <li><strong>Eliminates Odor-Causing Bacteria at the Root:</strong> Effective defense against unpleasant body odor.</li>
  <li><strong>Alcohol-Free Non-Staining Formula:</strong> 100% safe on skin and gentle on fabrics.</li>
  <li><strong>Compact {volume_en} Format:</strong> Elegant size perfect for daily care, handbag, and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply/spray {brand_en} deodorant onto completely clean, dry underarm skin after shower.</li>
  <li><strong>Step 2:</strong> Allow product to dry naturally for a few seconds before dressing (use daily every morning).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Active Protective Salts & Soothing Compounds:</strong> Regulate sweat secretions while preserving underarm skin softness.</li>
  <li><strong>Concentrated {variant_en} Fragrance Oils:</strong> Deliver an all-day fresh clean aura.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical underarm application only.</li>
  <li>Avoid applying onto irritated, broken, or freshly shaved underarm skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for 48-hour sweat protection and fresh long-lasting daily fragrancing.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>{brand_en}</td></tr>
  <tr><th>Category</th><td>Personal Care / {brand_en} Antiperspirant Deodorants {volume_en}</td></tr>
  <tr><th>Product Type</th><td>48H Antiperspirant Deodorant with {variant_en} Fragrance ({volume_en})</td></tr>
  <tr><th>Volume/Weight</th><td>{volume_en}</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Underarm Skin Types (Normal & Sensitive)</td></tr>
  <tr><th>Finish</th><td>Completely dry, smooth underarms fragranced with {variant_en} all day</td></tr>
  <tr><th>Texture</th><td>Smooth lightweight fast-drying liquid/stick/roll-on without stickiness</td></tr>
  <tr><th>Fragrance</th><td>Fresh bright {variant_en} aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Active Aluminum Antiperspirant Salts, Fragrance Oils, Soothing Agents</td></tr>
  <tr><th>Country of Origin</th><td>Germany / Switzerland / Philippines</td></tr>
  <tr><th>Manufacturer</th><td>{brand_en} Laboratories</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Antiperspirant Duct Occlusion & {variant_en} Sillage Retention</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves underarm wetness, body odor, and skin irritation caused by sweating.</p>

<h3>Why choose {brand_en} Deodorant?</h3>
<p>Active antiperspirant ingredients form a temporary hydrogel matrix in sweat gland ducts reducing sweat flow by up to 90% while purifying agents eliminate odor-causing bacteria.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is an advanced antiperspirant deodorant from {brand_en} with {variant_en} fragrance for 48h protection ({volume_en})."),
        (f"What are the benefits of protective compounds and {variant_en} fragrance?", f"Protective compounds ensure total underarm dryness, while {variant_en} fragrance coats underarms in a clean scent."),
        ("Does it protect against sweat wetness and odor for 48 hours?", "Yes, clinically proven to deliver complete dryness and odor defense up to 48 hours."),
        (f"What volume is contained in this container?", f"{volume_en}."),
        ("How do I use it correctly?", "Apply on clean dry underarm skin, let dry for seconds before dressing daily."),
        ("Is it alcohol-free?", "Yes, 100% alcohol-free and does not cause skin irritation."),
        (f"Where is {brand_en} Deodorant manufactured?", "Manufactured to international personal care quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", f"Fresh bright {variant_en} aroma."),
        ("Does it leave white or yellow marks on clothes?", "No, advanced non-staining formula leaves no marks on clothing."),
        (f"Is the {volume_en} container handbag friendly?", "Yes, sleek compact size ideal for handbag and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for workouts and heavy activity?", "Yes, ideal for sports and post-workout fresh showers."),
        ("How many times daily?", "Once every morning or as needed."),
        (f"Is {brand_en} a trusted global brand?", f"Yes, {brand_en} is a globally trusted brand in personal care."),
        ("Is the container recyclable?", "Yes."),
        ("Is it suitable for teens and adults?", "Yes, ages 12+."),
        ("Does it eliminate odor-causing bacteria?", "Yes, eliminates bacteria at the root source."),
        ("Does it leave underarms smooth?", "Yes, contains soothing agents leaving underarm skin soft."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it dry quickly on skin?", "Yes, dries in seconds without stickiness."),
        ("Is it suitable for sensitive underarms?", "Yes, dermatologically tested safe for sensitive underarms."),
        ("Is it a practical personal care gift?", "Yes, sleek practical addition to personal care routines."),
        ("Does it protect in hot summer weather?", "Yes, excellent protection during hot summer days."),
        ("Does it replace regular body sprays?", "Combines antiperspirant protection with luxury fragrancing.")
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
            "meta_description": f"اشتري {ar_name}. مزيل ومضاد تعرق من {brand_ar} بعطر {variant_ar} لحماية 48 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. {brand_en} 48H antiperspirant deodorant with {variant_en} fragrance. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1963():
    return _make_deodorant_generic(
        pid=1963, gtin="4800888221957",
        ar_name="مزيل عرق ستيك موشن سينس من ريكسونا  40مل",
        en_name="Rexona MotionSense Deodorant Stick - 40ml",
        brand_ar="ريكسونا", brand_en="Rexona",
        variant_ar="موشن سينس الانتعاش المفعل بالحركة", variant_en="MotionSense Active",
        volume_ar="40 مل", volume_en="40ml",
        tags_ar=["ريكسونا", "ستيك_موشن_سينس", "مزيل_عرق_ستيك", "ريكسونا_ستيك", "إكليل_أبها"],
        tags_en=["rexona", "motionsense_stick", "deodorant_stick", "rexona_stick", "ekleel_abha"]
    )


def create_product_1964():
    return _make_deodorant_generic(
        pid=1964, gtin="7614700005413",
        ar_name="مزيل عرق عبير المسك من مام 75مل",
        en_name="Mam Deodorant Abeer Al Musk 75ml",
        brand_ar="مام", brand_en="Mam",
        variant_ar="عبير المسك الشرقي الفاخر", variant_en="Abeer Al Musk",
        volume_ar="75 مل", volume_en="75ml",
        tags_ar=["مام", "مزيل_عرق_مام", "عبير_المسك", "مام_مسك", "إكليل_أبها"],
        tags_en=["mam", "mam_deodorant", "musk_deodorant", "mam_musk", "ekleel_abha"]
    )


def create_product_1965():
    return _make_deodorant_generic(
        pid=1965, gtin="7614700005321",
        ar_name="مزيل عرق  انتعاش المحيط  للرجال من مام 75مل",
        en_name="Mam deodorant ocean fresh for men 75ml",
        brand_ar="مام", brand_en="Mam",
        variant_ar="انتعاش المحيط البحري للرجال (Ocean Fresh)", variant_en="Ocean Fresh Men",
        volume_ar="75 مل", volume_en="75ml",
        tags_ar=["مام", "مزيل_عرق_مام_رجالي", "انتعاش_المحيط", "مام_رجالي", "إكليل_أبها"],
        tags_en=["mam", "mam_mens_deodorant", "ocean_fresh", "mam_ocean", "ekleel_abha"]
    )


def create_product_1966():
    return _make_deodorant_generic(
        pid=1966, gtin="4013162034369",
        ar_name="مزيل عرق  انتعاش المحيط  للرجال من مام 75مل",
        en_name="MUM Ocean Fresh Deodorant for Men - 75ml",
        brand_ar="مام", brand_en="MUM",
        variant_ar="انتعاش المحيط البحري الفواح للرجال", variant_en="MUM Ocean Fresh",
        volume_ar="75 مل", volume_en="75ml",
        tags_ar=["مام", "مزيل_عرق_مام", "انتعاش_المحيط_مام", "مام_كلاسيك", "إكليل_أبها"],
        tags_en=["mum", "mum_deodorant", "mum_ocean_fresh", "mens_mum", "ekleel_abha"]
    )


def create_product_1967():
    return _make_deodorant_generic(
        pid=1967, gtin="4005808692842",
        ar_name="مزيل عرق  نيتشرل فيرنيس للسيدات من  نيفيا- 40مل",
        en_name="NIVEA Natural Fairness Deodorant for Women - 40ml",
        brand_ar="نيفيا", brand_en="NIVEA",
        variant_ar="نيتشرل فيرنيس للتفتيح الطبيعي (Natural Fairness)", variant_en="Natural Fairness Whitening",
        volume_ar="40 مل", volume_en="40ml",
        tags_ar=["نيفيا", "نيتشرل_فيرنيس", "تفتيح_الإبطين", "مزيل_عرق_نيفيا", "إكليل_أبها"],
        tags_en=["nivea", "natural_fairness", "underarm_whitening", "nivea_deodorant", "ekleel_abha"]
    )


print("Loaded all 5 Batch 50 builders complete")
