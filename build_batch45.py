import json, os

def _make_ajmal_powder_80g(pid, gtin, ar_name, en_name, scent_ar, scent_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>{ar_name}</strong> بودرة الجسم المعطرة الملكية الفاخرة من أجمل المصممة لتوفير نعومة مخملية فائقة، جفاف تام، وعطر شرقي فواح يدوم طوال اليوم. ترتكز هذه البودرة الملكية ({en_name}) على التلك المنقى الناعم، عطر {scent_ar} المركّز والفاخر من أجمل، والمكونات المهدئة لجلد الجسم.</p>
<p>تعمل بودرة أجمل المعطرة على امتصاص العرق والرطوبة الزائدة، منع الاحتكاك والتهيج الجلدي بين الثنايا، وتغليف جسمك بنفحات عطرية ملكية فواحة، لتترك بشرتك ناعمة كالحرير، جافة، معطرة بالفخامة، ومفعمة بالثقة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عطر شرقي ملكي فواح يدوم طوال اليوم بعطر {scent_ar}:</strong> يمنح الجسم رائحة راقية تثبت لساعات.</li>
  <li><strong>امتصاص سريع للرطوبة والعرق الزائد:</strong> تحافظ على جفاف ونظافة البشرة.</li>
  <li><strong>تنعيم وملمس مخملي حريري:</strong> تمنح الجلد ملمساً ناعماً ومريحاً.</li>
  <li><strong>حماية من الاحتكاك بين ثنايا الجلد:</strong> تقي من التسلخات الناتجة عن التعرق.</li>
  <li><strong>جودة وعراقة دار أجمل للعطور:</strong> تصنيع فاخر وفق أعلى المعايير.</li>
  <li><strong>عبوة مدمجة 80 جم:</strong> حجم أنيق ممتاز للاستخدام اليومي بعد الاستحمام والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> جففي الجسم جيداً بعد الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من بودرة أجمل المعطرة على اليدين أو إسفنجة البودرة.</li>
  <li><strong>الخطوة الثالثة:</strong> وزعي البودرة برفق على كامل الجسم مع التركيز على الرقبة والصدر والثنايا (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>التلك المنقى الناعم:</strong> يمتص الرطوبة الزائدة ويمنح ملمساً حريرياً ناعماً.</li>
  <li><strong>العطر الفاخر المركّز من أجمل ({scent_ar}):</strong> يمنح الجسم نفساً معطراً فواحاً وثباتاً ممتازاً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم فقط.</li>
  <li>تجنبي استنشاق البودرة أو سكبها قرب الوجه والأنف.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لتعطير وتنعيم وتجفيف بشرة الجسم بعطور أجمل الملكية.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>أجمل (Ajmal Perfumes)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / بودرات أجمل المعطرة الملكية للجسم 80g</td></tr>
  <tr><th>نوع المنتج</th><td>بودرة جسم معطرة ومطراة بعطر {scent_ar} الملكي (80g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>80 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم جاف، ناعم كالحرير، معطر برائحة {scent_ar} الفواحة طوال اليوم</td></tr>
  <tr><th>الملمس</th><td>بودرة ناعمة جداً ذات ملمس مخملي حريري</td></tr>
  <tr><th>العطر</th><td>عطر {scent_ar} الفاخر من أجمل</td></tr>
  <tr><th>المكونات النشطة</th><td>تلك منقى ناعم، عطور أجمل المركزة، مواد ملطفة</td></tr>
  <tr><th>بلد المنشأ</th><td>الإمارات العربية المتحدة (UAE)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ajmal Perfumes International</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد عطور أجمل والتلك المنقى في البودرة المعطرة 80g ({scent_ar})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج بودرة أجمل المعطرة مشكلة التعرق الزائد والرطوبة بالجسم، رائحة العرق، والاحتكاك بين الثنايا الجسدية.</p>

<h3>لماذا تنجح تركيبة أجمل المعطرة؟</h3>
<p>لأن حبيبات التلك الدقيقة تحبس العرق دون انسداد المسام بينما تلتصق زيوت أجمل العطرية على طبقة البشرة السطحية لتبث عبيراً فواحاً.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق بعد الاستحمام مباشرة:</strong> يضمن أقصى ثبات للرائحة.<br>
2. <strong>التمركز على مناطق النبض:</strong> يرفع فوحان العطر بحرارة الجسم الطبيعية.<br>
3. <strong>التجفيف الكامل قبل التطبيق:</strong> يمنح ملمساً ناعماً حريرياً دون تكتل.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "بودرات الجسم تسبب انسداد المسام."<br>
<strong>الحقيقة:</strong> بودرة أجمل مصنعة بتلك منقى ذو مسامية تهوية آمنة لا تسد المسام.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تمتص الصفيحات الميكروية للتلك الرطوبة السطحية، بينما تتحرر الجزيئات العطرية تدريجياً بالتلامس الحراري مع الجلد.</p>"""

    faqs_data = [
        (f"ما هي {ar_name}؟", f"هي بودرة جسم معطرة وفاخرة من أجمل بعطر {scent_ar} لامتصاص الرطوبة وتنعيم وتعطير الجسم (80 جم)."),
        (f"ما هي فوائد التلك المنقى وعطر أجمل {scent_ar}؟", f"يمتص التلك الرطوبة ويمنع الاحتكاك، بينما يغلف عطر {scent_ar} الجسم برائحة فواحة تدوم طوال اليوم."),
        ("هل تمنح الجسم ملمساً ناعماً حريرياً؟", "نعم، تمنح البشرة ملمساً مخملياً ناعماً جداً ومريحاً."),
        ("ما وزن العبوة؟", "تأتي بوزن 80 جم."),
        ("كيف تُستخدم بالشكل الصحيح؟", "جففي الجسم بعد الاستحمام، ضعي كمية على اليدين أو الإسفنجة ووزعيها برفق على الجسم والرقبة والثنايا يومياً."),
        ("هل هي آمنة للاستخدام اليومي؟", "نعم، آمنة ومختبرة للاستخدام اليومي على بشرة الجسم."),
        ("أين صُنعت بودرة أجمل؟", "صُنعت في الإمارات العربية المتحدة بواسطة Ajmal Perfumes."),
        ("كيف أتأكد من أصالتها لدى إكليل أبها؟", "جميع منتجات أجمل لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {scent_ar} الفاخر الفواح من أجمل."),
        ("هل تمنع الاحتكاك والتعرق بين الثنايا؟", "نعم، تمتص العرق وتمنع الاحتكاك والالتصاق الجلدي."),
        ("هل 80 جم تكفي لفترة جيدة؟", "نعم، تكفي لعدة أسابيع من الاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع الفئات حسب العطر المفضل."),
        ("كم مرة يومياً؟", "مرة يومياً بعد الاستحمام وعند الحاجة."),
        ("هل تترك الفم والجسم معطراً طوال اليوم؟", "نعم، فوحان وثبات ممتاز طوال اليوم."),
        ("هل أجمل ماركة عطور عالمية شهيرة؟", "نعم، Ajmal Perfumes دار عطور عالمية عريقة ذات خبرة تزيد عن 70 عاماً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل تمنع رائحة العرق الكريهة؟", "نعم، تحافظ على جفاف ونظافة وتعطير الجسم."),
        ("هل تناسب جميع فصول السنة؟", "نعم، ممتازة في الصيف والشتاء."),
        ("هل تترك أثراً بيضاً سميكاً؟", "تتوزع بنعومة دون ترك تكتلات بيضاء سميكة."),
        ("هل تتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، تتوفرف بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل تناسب الاستخدام بعد حلاقة الجسم؟", "تهدئ الجلد وتنعمه بعد الحلاقة."),
        ("هل تصلح هدية عملية؟", "نعم، هدية أنيقة ومفيدة لكل عشاق عطور أجمل."),
        ("هل يمكن وضعها على الملابس؟", "توضع على الجلد مباشرةً للحصول على أفضل تعطير وتنعيم."),
        ("هل تجفف الجلد؟", "تنعّم وتحفظ التوازن دون جفاف شديد.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is a royal luxury perfumed body talc from Ajmal Perfumes designed to provide complete dryness, velvety smoothness, and an all-day long-lasting oriental fragrance. Formulated with fine pure purified talc, concentrated luxury Ajmal perfume oils ({scent_en}), and skin-soothing agents.</p>
<p>Ajmal Perfumed Body Powder absorbs excess sweat and moisture, prevents skin chafing and irritation, and envelops your body in the captivating scent of {scent_en}, leaving your skin touchably soft, dry, elegantly fragranced, and confident all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>All-Day Long-Lasting Fragrance with {scent_en}:</strong> Envelops body in an elegant scent lasting for hours.</li>
  <li><strong>Fast Absorption of Excess Sweat & Moisture:</strong> Keeps body dry and clean.</li>
  <li><strong>Silky Smooth Velvet Touch:</strong> Imparts an extremely soft comfortable feel to skin.</li>
  <li><strong>Prevents Friction & Chafing in Folds:</strong> Shields skin against sweat-induced friction.</li>
  <li><strong>Heritage & Quality of Ajmal Perfumes:</strong> Decades of expertise in luxury perfumery and body talcs.</li>
  <li><strong>Compact 80g Container:</strong> Elegant size perfect for daily post-shower use and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Dry body thoroughly after shower.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of Ajmal perfumed powder onto hands or a powder puff.</li>
  <li><strong>Step 3:</strong> Smooth gently over full body focusing on neck, chest, and skin folds (use daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Purified Fine Talc:</strong> Absorbs excess moisture and imparts a silky soft touch.</li>
  <li><strong>Concentrated Luxury Ajmal Fragrance ({scent_en}):</strong> Delivers an intense long-lasting pleasant scent.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application only.</li>
  <li>Avoid inhaling powder or dusting near face and nose.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for body perfuming, smoothing, and moisture absorption with luxury Ajmal scents.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Ajmal Perfumes</td></tr>
  <tr><th>Category</th><td>Personal Care / Ajmal Perfumed Body Powders 80g</td></tr>
  <tr><th>Product Type</th><td>Luxury {scent_en} Scented & Smoothing Body Talc (80g)</td></tr>
  <tr><th>Volume/Weight</th><td>80 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types</td></tr>
  <tr><th>Finish</th><td>Dry, silky soft, beautifully fragranced body skin with {scent_en} all day</td></tr>
  <tr><th>Texture</th><td>Ultra-fine silky soft velvet powder</td></tr>
  <tr><th>Fragrance</th><td>Luxury {scent_en} fragrance by Ajmal</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Purified Fine Talc, Concentrated Ajmal Fragrance Oils, Soothing Agents</td></tr>
  <tr><th>Country of Origin</th><td>UAE</td></tr>
  <tr><th>Manufacturer</th><td>Ajmal Perfumes International</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Fine Purified Talc Moisture Adsorption & Ajmal Fragrance Fixation</h2>

<h3>What problem does this solve?</h3>
<p>Ajmal Perfumed Powder resolves excess sweat, body moisture, body odor, and skin chafing friction.</p>

<h3>Why choose Ajmal Perfumed Powder?</h3>
<p>Micro-fine talc platelets physically adsorb skin moisture preventing friction while Ajmal fragrance oils fixate onto epidermal surface layers releasing fragrance continuously.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a luxury perfumed body talc from Ajmal with {scent_en} fragrance for absorbing moisture, smoothing, and perfuming the body (80g)."),
        (f"What are the benefits of Purified Talc and {scent_en} fragrance?", f"Talc absorbs moisture and prevents chafing, while {scent_en} fragrance coats the body in long-lasting scent."),
        ("Does it impart a silky smooth touch?", "Yes, gives skin an extremely soft comfortable velvet touch."),
        ("What weight is contained in this tub?", "80g."),
        ("How do I use it correctly?", "Dry body post-shower, apply on hands or puff, smooth gently over body, neck, and folds daily."),
        ("Is it safe for daily use?", "Yes, safe and tested for daily body skin application."),
        ("Where is Ajmal powder manufactured?", "In UAE by Ajmal Perfumes International."),
        ("How do I verify authenticity at Ekleel Abha?", "All Ajmal products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", f"Luxury signature {scent_en} fragrance by Ajmal."),
        ("Does it prevent chafing and sweat friction in skin folds?", "Yes, absorbs sweat preventing friction and skin sticking."),
        ("Does 80g last long?", "Yes, lasts weeks of daily post-shower use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for men and women?", "Suitable for men and women depending on scent preference."),
        ("How many times daily?", "Once daily post-shower and as needed."),
        ("Does it leave lasting fresh breath and scent all day?", "Yes, excellent sillage and long-lasting scent performance all day."),
        ("Is Ajmal a world-famous perfume house?", "Yes, Ajmal Perfumes is a globally renowned perfume house with over 70 years of heritage."),
        ("Is the container recyclable?", "Yes."),
        ("Does it prevent unpleasant body sweat odor?", "Yes, keeps body dry, clean, and beautifully fragranced."),
        ("Is it good for all seasons?", "Yes, excellent in summer and winter."),
        ("Does it leave a thick white residue?", "Distributes smoothly without leaving thick white clumps."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable post-shaving?", "Soothes and softens skin after shaving."),
        ("Is it a practical gift?", "Yes, elegant and thoughtful gift for Ajmal fragrance lovers."),
        ("Can it be applied on clothing?", "Best applied directly onto skin for optimal perfuming and smoothing."),
        ("Does it dry skin out?", "Softens and preserves skin moisture balance without harsh drying.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Ajmal",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. بودرة جسم معطرة من أجمل بعطر {scent_ar} لامتصاص الرطوبة وتنعيم وتعطير الجسم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Luxury Ajmal perfumed body talc with {scent_en} fragrance for smoothness and freshness. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1937():
    return _make_ajmal_powder_80g(
        pid=1937, gtin="6293708010622",
        ar_name="بودرة وصال ذهب من اجمل 80 جم",
        en_name="Ajmal Wisal Dhahab Perfumed Powder 80g",
        scent_ar="وصال ذهب الشرقي الذهبي الملكي", scent_en="Wisal Dhahab Royal Golden Oriental",
        tags_ar=["أجمل", "وصال_ذهب", "بودرة_وصال_ذهب", "عطر_وصال", "إكليل_أبها"],
        tags_en=["ajmal", "wisal_dhahab_powder", "wisal_talc", "ajmal_wisal", "ekleel_abha"]
    )


def create_product_1938():
    return _make_ajmal_powder_80g(
        pid=1938, gtin="6293708008483",
        ar_name="بودرة سوسن من اجمل 80 جم",
        en_name="Ajmal Susan Powder 80g",
        scent_ar="سوسن الزهري الفاخر", scent_en="Susan Elegant Floral",
        tags_ar=["أجمل", "بودرة_سوسن", "عطر_سوسن", "بودرة_عطرية", "إكليل_أبها"],
        tags_en=["ajmal", "susan_powder", "susan_talc", "ajmal_susan", "ekleel_abha"]
    )


def create_product_1939():
    return _make_ajmal_powder_80g(
        pid=1939, gtin="6293708008490",
        ar_name="بودرة دانة الدنيا من اجمل 80 جم",
        en_name="Ajmal Danat Al Dunya Perfumed Powder 80g",
        scent_ar="دانة الدنيا الشرقية الملكية", scent_en="Danat Al Dunya Royal Oriental",
        tags_ar=["أجمل", "دانة_الدنيا", "بودرة_دانة_الدنيا", "عطر_دانة_الدنيا", "إكليل_أبها"],
        tags_en=["ajmal", "danat_al_dunya_powder", "danat_talc", "ajmal_danat", "ekleel_abha"]
    )


def create_product_1940():
    return _make_ajmal_powder_80g(
        pid=1940, gtin="6293708016921",
        ar_name="بودرة قصيدة من اجمل 80 جم",
        en_name="Qasieda Powder by Ajmal - 80g",
        scent_ar="قصيدة الفاخرة العبقة", scent_en="Qasieda Luxurious Perfume",
        tags_ar=["أجمل", "بودرة_قصيدة", "عطر_قصيدة", "بودرة_عطرية", "إكليل_أبها"],
        tags_en=["ajmal", "qasieda_powder", "qasieda_talc", "ajmal_qasieda", "ekleel_abha"]
    )


def create_product_1942():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>عطر اطفال برائحة الباودر من بيبي لوف 30مل (Baby perfume with the smell of powder from Baby Love 30ml)</strong> عطر الأطفال الرقيق الحنون الخالي من الكحول من بيبي لوف المصمم لتأطير وتعطير ملابس وبشرة الأطفال والرضع برائحة الباودر الزكية النظيفة. يرتكز هذا العطر الناعم (Baby Love Powder Scented Baby Perfume 30ml) على تركيبة خالية 100% من الكحول، خلاصة الباودر الطبيعي، والمكونات المهدئة المعتمدة للأطفال.</p>
<p>يعمل عطر بيبي لوف برائحة الباودر على منح طفلك رائحة النظافة والطفولة الحنونة، إنعاش ملابس وجسم الطفل، وتأمين تعطير آمن لا يسبب أي حساسيه أو تهيج تنفسي أو جلدي، ليترك طفلك معطراً برائحة الباودر الناعمة، منتعشاً، ومحمياً طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عطر باودر طفولي حنون خالي 100% من الكحول:</strong> آمن تماماً لبشرة وملابس الرضع والأطفال.</li>
  <li><strong>تعطير ناعم يدوم طوال اليوم دون تهيج:</strong> لا يسبب حساسية أو تهيجاً لجلد أو تنفس الطفل.</li>
  <li><strong>رائحة الباودر النظيفة المحببة للجميع:</strong> تمنح الطفل انتعاشاً ونظافة فائقة.</li>
  <li><strong>بخاخ أنيق وسهل التطبيق (Spray):</strong> يسهل رش البخاخ على الملابس وفراش الطفل.</li>
  <li><strong>عبوة مدمجة سعة 30 مل:</strong> حجم ممتاز لحقيبة الأم والسفر والتنقل اليومي.</li>
  <li><strong>اختبارات سلامة معتمدة للأطفال:</strong> ملائم للاستخدام من الولادة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> رشّي بضع رشات من عطر بيبي لوف برائحة الباودر على ملابس الطفل أو فراشه عن بُعد مناسب (15-20 سم).</li>
  <li><strong>الخطوة الثانية:</strong> يمكن وضع قطرات بسيطة على بشرة الطفل (بعد التأكد من جفافها).</li>
  <li><strong>الخطوة الثالثة:</strong> دعي العطر يجف طبيعياً واستمتعي بالرائحة الطفولية الناعمة (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>قاعدة مائية خالية من الكحول (Alcohol-Free Water Base):</strong> آمنة ولطيفة لا تجفف بشرة أو ملابس الطفل.</li>
  <li><strong>زيوت الباودر العطرية المعتمدة:</strong> تمنح الرائحة الطفولية الناعمة والمحببة دون مسببات الحساسية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على ملابس وبشرة الأطفال فقط.</li>
  <li>تجنبي الرش المباشر على وجه أو عيني الطفل.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل أم تبحث عن عطر بيبي لوف برائحة الباودر 30 مل الخالي من الكحول لتعطير طفلها بكل أمان.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيبي لوف (Baby Love)</td></tr>
  <tr><th>الفئة</th><td>العناية بالأطفال / عطور الرضع والأطفال الخالية من الكحول 30ml</td></tr>
  <tr><th>نوع المنتج</th><td>عطر أطفال خالي من الكحول برائحة الباودر النظيفة (30ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>30 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة وملابس الأطفال الرضع والصغار (من الولادة)</td></tr>
  <tr><th>المظهر النهائي</th><td>طفل معطر برائحة الباودر الناعمة النظيفة، منتعش ومحمي من التهيج</td></tr>
  <tr><th>الملمس</th><td>رذاذ عطر مائي خفيف خالٍ من الكحول دون لزوجة</td></tr>
  <tr><th>العطر</th><td>رائحة الباودر الطفولية النظيفة الناعمة</td></tr>
  <tr><th>المكونات النشطة</th><td>قاعدة مائية خالية من الكحول، زيوت باودر عطرية معتمدة للأطفال</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين / الإمارات العربية المتحدة</td></tr>
  <tr><th>الشركة المصنعة</th><td>Baby Love Care Products</td></tr>
  <tr><th>الفئة العمرية</th><td>الرضع والأطفال (من الولادة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد عطور الأطفال الخالية من الكحول برائحة الباودر (Baby Love)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج عطر بيبي لوف برائحة الباودر مشكلة مخاطر الكحول والمواد الحافظة الثقيلة في عطور الكبار على بشرة وتنفس الأطفال.</p>

<h3>لماذا تنجح التركيبة المائية الخالية من الكحول؟</h3>
<p>لأن القاعدة المائية تعطر الملابس والجلد دون إحداث جفاف جلدي أو تهيج في الغشاء المخاطي التنفسي للرضع.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الرش على الملابس والفراش:</strong> أفضل طريقة للحصول على تعطير يدوم طويلاً وأمان مضاعف.<br>
2. <strong>الرش عن بُعد 20 سم:</strong> يضمن توزيع الرذاذ المائي بتجانس دون بلل شديد.<br>
3. <strong>التخزين بعيداً عن الحرارة:</strong> يحافظ على ثباتية وتوازن الزيوت العطرية الطفولية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "عطور الأطفال الخالية من الكحول تسبب بقعاً على الملابس."<br>
<strong>الحقيقة:</strong> عطر بيبي لوف مصمم بقاعدة مائية شفافة لا تترك أي أثر أو بقع على ملابس الأطفال.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تنتشر الجزيئات العطرية الآمنة الخالية من الفثاليت والبارابين في الهيدروسول المائي لتنطلق بالتبخر البطيء على الملابس والجلد.</p>"""

    faqs = [
        ("ما هو عطر اطفال برائحة الباودر من بيبي لوف 30مل؟", "هو عطر أطفال رقيق وخالٍ من الكحول من بيبي لوف برائحة الباودر النظيفة لتعطير ملابس وبشرة الأطفال والرضع (30 مل)."),
        ("ما هي فوائد التركيبة الخالية من الكحول ورائحة الباودر؟", "تعطر دون تسبب جفاف أو تهيج للبشرة أو التنفس، وتمنح رائحة الباودر النظيفة الحنونة."),
        ("هل هو آمن للرضع من الولادة؟", "نعم، 100% خالٍ من الكحول وآمن للرضع والأطفال من الولادة."),
        ("ما حجم العبوة؟", "تأتي بعبوة بخاخ سعة 30 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "رشي عن بُعد 15-20 سم على ملابس الطفل وفراشه أو قطرات على الجلد ودعيه يجف طبيعياً."),
        ("هل يسبب حساسية تنفسية أو جلدية؟", "لا، تركيبة خالية من الكحول ومسببات الحساسية المعتمدة للأطفال."),
        ("أين صُنع عطر بيبي لوف؟", "صُنع بواسطة Baby Love Care Products."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات بيبي لوف لدى إكليل أبها أصلية 100%."),
        ("ما رائحة عطر بيبي لوف؟", "رائحة الباودر الطفولية النظيفة الناعمة المحببة."),
        ("هل يترك بقعاً على ملابس الطفل؟", "لا، قاعدة مائية شفافة لا تترك أي أثر على الملابس."),
        ("هل 30 مل مناسبة لحقيبة الأم والسفر؟", "نعم، حجم مدمج أنيق مثالي لحقيبة الأم والسفر والتنقل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب تعطير فراش وعربة الطفل؟", "نعم، ممتاز لتعطير فراش وعربة وملابس الطفل."),
        ("كم مرة يومياً؟", "يُستعمل يومياً حسب الحاجة."),
        ("هل يدوم العطر طويلاً على الملابس؟", "نعم، يثبت بتجانس على الأنسجة القطنية لملابس الطفل."),
        ("هل هو من العطور الطفولية الأكثر طلباً؟", "نعم، Baby Love Powder Perfume من أبرز وأحب عطور الأطفال."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنح الطفل انتعاشاً بعد الاستحمام؟", "نعم، يكمل انتعاش الاستحمام برائحة الباودر الناعمة."),
        ("هل يسبب جفافاً لبشرة الطفل؟", "لا، خالٍ من الكحول ويحافظ على رطوبة الجلد."),
        ("هل ينفع هدية لطيفة لمولود جديد؟", "نعم، هدية رقيقة وعملية وممتازة لكل مولود جديد."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يسهل رش البخاخ؟", "نعم، بخاخ برذاذ ناعم دقيق."),
        ("هل يناسب الأولاد والبنات؟", "نعم، مناسب لجميع الأطفال الرضع والصغار."),
        ("هل يمكن استخدامه للأمهات أيضاً؟", "نعم، بعض الأمهات يحببن استخدامه لرائحته النظيفة."),
        ("هل الرائحة خفيفة وغير مزعجة؟", "نعم، رائحة باودر ناعمة ولطيفة وغير نفاذة.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Baby perfume with the smell of powder from Baby Love 30ml</strong> is a delicate alcohol-free baby perfume from Baby Love designed to fragrance infant and child clothing and skin with a clean powder scent. Formulated with a 100% alcohol-free water base, natural powder notes, and pediatrician-approved gentle ingredients.</p>
<p>Baby Love Powder Perfume imparts a comforting baby cleanliness scent, refreshes child clothing and body, and delivers safe fragrancing without causing skin irritation or respiratory allergy, leaving your child sweetly fragranced, refreshed, and safe all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Alcohol-Free Powder Baby Fragrance:</strong> Completely safe for infant clothing and sensitive skin.</li>
  <li><strong>Soft All-Day Fragrancing Without Irritation:</strong> Does not trigger skin allergy or respiratory sting.</li>
  <li><strong>Clean Beloved Baby Powder Scent:</strong> Gives child a comforting clean freshness.</li>
  <li><strong>Convenient Fine Mist Spray:</strong> Easy to spray onto clothing, bedding, and strollers.</li>
  <li><strong>Compact 30ml Bottle:</strong> Ideal size for mother's diaper bag and travel convenience.</li>
  <li><strong>Child Safety Tested & Approved:</strong> Safe for use from birth.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Spray a few pumps of Baby Love Powder perfume onto child clothing or bedding from a distance (15-20 cm).</li>
  <li><strong>Step 2:</strong> Drops can also be applied onto skin after ensuring skin is clean and dry.</li>
  <li><strong>Step 3:</strong> Allow to dry naturally and enjoy the soft baby powder aroma (use daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Alcohol-Free Water Base:</strong> Safe and gentle, does not dry out infant skin or clothing.</li>
  <li><strong>Approved Baby Powder Fragrance Oils:</strong> Deliver a soft comforting scent without allergens.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external child clothing and skin application only.</li>
  <li>Avoid direct spraying onto baby's face or eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every mother seeking Baby Love 30ml Alcohol-Free Powder Perfume for safe baby fragrancing.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Baby Love</td></tr>
  <tr><th>Category</th><td>Baby Care / Baby Love Alcohol-Free Infant Perfumes 30ml</td></tr>
  <tr><th>Product Type</th><td>Alcohol-Free Clean Baby Powder Scented Fragrance Mist (30ml)</td></tr>
  <tr><th>Volume/Weight</th><td>30 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Infant & Child Skin & Clothing (From Birth)</td></tr>
  <tr><th>Finish</th><td>Softly powder-fragranced child, refreshed & protected from irritation</td></tr>
  <tr><th>Texture</th><td>Lightweight alcohol-free water mist spray</td></tr>
  <tr><th>Fragrance</th><td>Clean soft comforting baby powder scent</td></tr>
  <tr><th>Active Ingredients</th><td>Alcohol-Free Water Base, Approved Baby Powder Fragrance Oils</td></tr>
  <tr><th>Country of Origin</th><td>China / UAE</td></tr>
  <tr><th>Manufacturer</th><td>Baby Love Care Products</td></tr>
  <tr><th>Age Group</th><td>Infants & Children (From Birth)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Alcohol-Free Hydrosol Formulations for Infant Airway & Skin Safety</h2>

<h3>What problem does this solve?</h3>
<p>Baby Love Powder Perfume resolves the risks of adult alcohol-based perfumes causing skin dryness or airway irritation in infants.</p>

<h3>Why choose an Alcohol-Free Water-Based Perfume?</h3>
<p>Alcohol-free water-based hydrosols evaporate slowly on fabrics releasing hypoallergenic powder notes without stripping moisture from baby skin.</p>"""

    en_faqs = [
        ("What is Baby perfume with the smell of powder from Baby Love 30ml?", "It is a delicate alcohol-free baby perfume from Baby Love with a clean powder scent for fragrancing infant clothing and skin (30ml)."),
        ("What are the benefits of the alcohol-free powder formula?", "Fragrances safely without drying skin or irritating respiratory airways, giving a comforting clean powder scent."),
        ("Is it safe for infants from birth?", "Yes, 100% alcohol-free and safe for infants from birth."),
        ("What volume is contained in this bottle?", "30ml spray bottle."),
        ("How do I use it correctly?", "Spray from 15-20 cm onto clothing, bedding, or skin drops, allow to dry naturally."),
        ("Does it cause skin or respiratory allergies?", "No, alcohol-free and allergen-free formula safe for infants."),
        ("Where is Baby Love perfume manufactured?", "By Baby Love Care Products."),
        ("How do I verify authenticity at Ekleel Abha?", "All Baby Love products at Ekleel Abha are 100% original."),
        ("What does Baby Love Powder Perfume smell like?", "Beloved clean soft comforting baby powder scent."),
        ("Does it stain baby clothing?", "No, clear water base does not leave stains on fabrics."),
        ("Is 30ml suitable for a mother's diaper bag?", "Yes, compact sleek size perfect for diaper bags and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for strollers and crib bedding?", "Yes, excellent for fragrancing crib bedding, clothing, and strollers."),
        ("How often daily?", "Use daily as needed."),
        ("Does the scent last long on clothing?", "Yes, fixes evenly onto cotton fabrics lasting for hours."),
        ("Is it a popular baby perfume?", "Yes, Baby Love Powder Perfume is a beloved bestseller in baby care."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it refresh baby post-bath?", "Yes, complements post-bath freshness with a soft powder scent."),
        ("Does it cause skin dryness?", "No, alcohol-free formula preserves skin moisture."),
        ("Is it a nice newborn baby gift?", "Yes, thoughtful delicate newborn care gift."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is the spray pump easy to use?", "Yes, fine mist spray pump for even application."),
        ("Is it suitable for boys and girls?", "Yes, suitable for all infants and young children."),
        ("Can mothers use it too?", "Yes, many mothers love using it for its clean powder scent."),
        ("Is the scent light and non-intrusive?", "Yes, light soft baby powder scent, not overpowering.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1942",
        "sku": "EK-1942",
        "gtin": "6939517180995",
        "brand": "Baby Love",
        "ar": {
            "title": "عطر اطفال برائحة الباودر من بيبي لوف 30مل",
            "meta_title": "عطر أطفال بيبي لوف بالباودر 30مل | إكليل أبها",
            "meta_description": "اشتري عطر أطفال برائحة الباودر من بيبي لوف (30 مل). عطر رقيق خالي من الكحول لتعطير ملابس وبشرة الأطفال. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["بيبي_لوف", "عطر_أطفال", "برائحة_الباودر", "عطر_خالي_من_الكحول", "إكليل_أبها"]
        },
        "en": {
            "title": "Baby perfume with the smell of powder from Baby Love 30ml",
            "meta_title": "Baby Love Powder Scent Baby Perfume 30ml | Ekleel Abha",
            "meta_description": "Buy original Baby Love Powder Scent Baby Perfume (30ml). Alcohol-free clean powder fragrance mist for infants. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["baby_love", "baby_perfume", "powder_scent", "alcohol_free_perfume", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 45 builders complete")
