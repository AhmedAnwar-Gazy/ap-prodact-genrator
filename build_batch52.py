import json, os

def _make_gillette_venus(pid, gtin, ar_name, en_name, count_info_ar, count_info_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> ماكينة وشفرات الحلاقة النسائية الأكثر سلاسة وأماناً من جيليت فينوس العالمية المصممة خصيصاً لمنح المرأة حلاقة دقيقة، ناعمة للغاية، وخالية من التهيج أو الجروح. يرتكز هذا المنتج الأصيل ({en_name}) على تقنية الشفرات الثلاثية الحادة الناعمة (3 Flexible Blades)، شريط الترطيب المدمج بالصبار والزيوت المهدئة، والمقبض المريح المضاد للانزلاق.</p>
<p>تنساب ماكينة جيليت فينوس بحرية فوق منحنيات الجسم (الساقين، تحت الإبطين، والمناطق الحساسة)، لتزيل أدق الشعيرات من الجذور دون شد أو خياشة، وتترك بشرتك ناعمة كالحرير، مرطبة، وخالية من الحبوب والتحسس.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>شفرات مرنة ثلاثية لحلاقة فائقة النعومة:</strong> تلتقط الشعيرات القصيرة والدقيقة من اللمسة الأولى.</li>
  <li><strong>شريط ترطيب مدمج بالصبار والزيوت المهدئة:</strong> يسهل الانزلاق ويحمي من التهيج والجروح.</li>
  <li><strong>مقبض مريح مضاد للانزلاق (MoistureRich Handle):</strong> تحكم آمن وسهل أثناء الاستحمام والماء.</li>
  <li><strong>مصممة خصيصاً لمنحنيات جسم المرأة:</strong> تتكيف بسلاسة مع زوايا الساقين والمناطق الحساسة.</li>
  <li><strong>عبوة اقتصادية شاملة ({count_info_ar}):</strong> توفير ممتاز وعمر استبدال طويل للغاية.</li>
  <li><strong>جودة جيليت فينوس (Gillette Venus) العالمية:</strong> العلامة الأولى الموصى بها عالمياً للحلاقة النسائية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التحضير):</strong> بللي المنطقة المراد حلاقتها بالماء الدافئ ورغوة أو جل الحلاقة.</li>
  <li><strong>الخطوة الثانية (الحلاقة):</strong> مرري ماكينة جيليت فينوس برفق عكس اتجاه نمو الشعر دون الضغط الشديد.</li>
  <li><strong>الخطوة الثالثة (التشطيب):</strong> اشطفي الشفرات بالماء، وجففي البشرة ثم ضعي لوشن مرطب (يُستعمل عند الحاجة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>شفرات ستانلس ستيل ثلاثية فائقة الدقة:</strong> تضمن قصاً ناعماً وآمناً للشعر.</li>
  <li><strong>شريط الترطيب بالصبار وفيتامين E:</strong> يفرز مزلقاً مائياً ناعماً لمنع الاحتكاك والتحسس.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>تُحفظ بعيداً عن متناول الأطفال.</li>
  <li>عدم مسح الشفرات بمنشفة جافة للحفاظ على عمر شريط الترطيب والدقة.</li>
  <li>تُحفظ في مكان جاف بعد الاستخدام.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن {ar_name} للحلاقة النسائية الناعمة والآمنة بدون جروح.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جيليت فينوس (Gillette Venus)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / ماكينات وشفرات الحلاقة النسائية من فينوس</td></tr>
  <tr><th>نوع المنتج</th><td>ماكينة/شفرات حلاقة نسائية ثلاثية الشفرات بشريط ترطيب ({count_info_ar})</td></tr>
  <tr><th>الحجم/العدد</th><td>{count_info_ar}</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع انواع بشرة الجسم النسائية (بما في ذلك الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة كالحرير، خالية تماماً من الشعر، الجروح، والحبوب</td></tr>
  <tr><th>الملمس</th><td>انزلاق ناعم مائي غير محتك</td></tr>
  <tr><th>العطر</th><td>عطر الصبار والزيوت المهدئة اللطيف</td></tr>
  <tr><th>المكونات النشطة</th><td>شفرات فولاذية مرنة ثلاثية، شريط ترطيب بالصبار وفيتامين E</td></tr>
  <tr><th>بلد المنشأ</th><td>بولندا / المكسيك / ألمانيا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Gillette (Procter & Gamble)</td></tr>
  <tr><th>الفئة العمرية</th><td>النساء والفتيات (من 14 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد الشفرات الثلاثية المرنة وشريط الترطيب في جيليت فينوس (Gillette Venus)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تراكم الشعر الزائد، الجروح القطعية الناتجة عن الشفرات العادية، تهيج وانغراس الشعر تحت الجلد (Ingrown Hair).</p>

<h3>لماذا تنجح تقنية Gillette Venus؟</h3>
<p>لأن توزيع الضغط على 3 شفرات مرنة مع إفراز مزلق الصبار المائي يقلل احتكاك الفولاذ بجلد البشرة الحساس بنسبة 80%.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الحلاقة دائماً بالماء الدافئ ورغوة/جل الحلاقة:</strong> يطري الشعيرات ويمنع خدش الجلد.<br>
2. <strong>استبدال الشفرة عند تلاشي شريط الترطيب:</strong> يضمن حلاقة ناعمة وآمنة باستمرار.<br>
3. <strong>الشطف الجيد والتجفيف الهوائي:</strong> يحفظ الشفرات من الصدأ والبكتيريا.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "حلاقة الشعر بالشفرة تجعل الشعر ينمو أكثر كتافة وسمكاً."<br>
<strong>الحقيقة:</strong> الحلاقة تقص الشعر عند السطح فقط ولا تؤثر إطلاقاً على عدد أو سمك بصيلات الشعر الداخلية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تقوم الشفرة الأولى برفع الشعيرة قليلاً، وتقوم الثانية بقطعها تحت مستوى السطح، بينما تمسح الثالثة بقايا البروز.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو ماكينة/شفرات حلاقة نسائية ثلاثية الشفرات بشريط ترطيب بالصبار من جيليت فينوس ({count_info_ar})."),
        ("ما هي فوائد الشفرات الثلاثية وشريط الترطيب بالصبار؟", "تضمن الشفرات الثلاثية حلاقة فائقة النعومة من اللمسة الأولى، بينما يمنع شريط الصبار الجروح والتهيج."),
        ("هل تحمي من الجروح والتهيج والحبوب؟", "نعم، مثبتة سريرياً في توفير حلاقة آمنة للغاية خالية من الجروح والتهيج."),
        (f"ما كمية/محتوى العبوة؟", f"تأتي بـ {count_info_ar}."),
        ("كيف تُستخدم بالشكل الصحيح؟", "بللي البشرة بالماء والجل، مرري الماكينة برفق عكس نمو الشعر واشطفي بالماء."),
        ("هل المقبض مريح ومضاد للانزلاق؟", "نعم، مقبض مريح جداً مضاد للانزلاق أثناء الاستحمام."),
        ("أين صُنع منتج جيليت فينوس؟", "صُنع بواسطة Procter & Gamble العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات جيليت لدى إكليل أبها أصلية 100%."),
        (f"ما ميزة شريط الترطيب في فينوس؟", "يفرز مزلقاً مائياً ناعماً بالصبار وفيتامين E لسهولة الانزلاق."),
        ("هل تناسب جميع مناطق الجسم؟", "نعم، ممتازة للساقين، تحت الإبطين، والمناطق الحساسة."),
        (f"هل العبوة {count_info_ar} عملية واقتصادية؟", "نعم، توفير ممتاز وعمر استخدام طويل."),
        ("كيف أحتفظ بالماكينة بعد الاستخدام؟", "في مكان جاف وعدم مسح الشفرات بمنشفة جافة."),
        ("هل تناسب البشرة الحساسة؟", "نعم، مختبرة جلدياً وآمنة تماماً للبشرة الحساسة."),
        ("كم مرة يُفضل استبدال الشفرة؟", "عند تلاشي لون شريط الترطيب أو عندما تصبح الشفرة غير حادة."),
        ("هل جيليت فينوس العلامة الأولى عالمياً للنساء؟", "نعم، Gillette Venus العلامة الأولى عالمياً في الحلاقة النسائية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل تناسب الفتيات والنساء؟", "نعم، مناسبة من 14 سنة فما فوق."),
        ("هل تمنع انغراس الشعر تحت الجلد؟", "نعم، تقص الشعر بسلاسة دون التسبب في انغراس البصيلات."),
        ("هل تترك البشرة ناعمة كالحرير؟", "نعم، تترك البشرة ناعمة كالحرير خالية من بقايا الشعر."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل تنزلق بسهولة مع جل الحلاقة؟", "نعم، تنزلق بسلاسة فائقة دون أي جهد."),
        ("هل رأس الماكينة متحرك لمتابعة المنحنيات؟", "نعم، تتكيف زاوية الشفرات مع منحنيات الجسم."),
        ("هل تصلح هدية ممتازة ضمن العناية؟", "نعم، منتج أساسي لا غنى عنه في العناية الشخصية."),
        ("هل تسبب اسمرار البشرة؟", "لا، حلاقة آمنة لا تسبب التصلب أو الاسمرار."),
        ("هل تتوافق الشفرات مع مقابض فينوس الأخرى؟", "نعم، معظم شفرات ومقابض فينوس متوافقة.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is the smoothest and safest women's razor and blade system from Gillette Venus designed to deliver a close, touchably smooth, and nick-free shave. Built upon 3 Flexible Blades, an integrated Aloe Vera moisture lubrication strip, and an ergonomic anti-slip handle.</p>
<p>Gillette Venus glides effortlessly over women's body curves (legs, underarms, and sensitive bikini areas), removing the shortest hairs from the surface without pulling, leaving your skin touchably silky soft, hydrated, and free from razor bumps or irritation.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>3 Flexible Blades for Ultra-Smooth Shaving:</strong> Catches short fine hairs from the first pass.</li>
  <li><strong>Integrated Moisture Strip with Aloe Vera & Vitamin E:</strong> Enhances glide protecting skin from nicks and irritation.</li>
  <li><strong>Ergonomic Anti-Slip MoistureRich Handle:</strong> Secure easy control even under shower water.</li>
  <li><strong>Designed Specifically for Female Body Curves:</strong> Pivots smoothly around leg angles and sensitive areas.</li>
  <li><strong>Comprehensive Value Pack ({count_info_en}):</strong> Exceptional value and extended replacement cycle.</li>
  <li><strong>World-Renowned Gillette Venus Quality:</strong> #1 dermatologist recommended female hair removal brand.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Prep):</strong> Wet shaving area with warm water and apply shaving gel or foam.</li>
  <li><strong>Step 2 (Shave):</strong> Glide Gillette Venus razor gently against hair growth without heavy pressure.</li>
  <li><strong>Step 3 (Post-Care):</strong> Rinse blades under water, pat skin dry and follow with body lotion (use as needed).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Triple Flexible Stainless Steel Blades:</strong> Ensure precise safe hair cutting.</li>
  <li><strong>Aloe Vera & Vitamin E Moisture Strip:</strong> Releases water-activated lubricant preventing friction.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>Keep out of reach of children.</li>
  <li>Do not wipe blades with a dry towel to preserve blade precision and moisture strip.</li>
  <li>Store in a dry location after use.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every woman seeking {en_name} for smooth, safe, and nick-free female shaving.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Gillette Venus</td></tr>
  <tr><th>Category</th><td>Personal Care / Gillette Venus Women's Razors & Blades</td></tr>
  <tr><th>Product Type</th><td>3-Blade Women's Razor/Blades with Aloe Moisture Strip ({count_info_en})</td></tr>
  <tr><th>Volume/Count</th><td>{count_info_en}</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Female Body Skin Types (Including Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, hair-free, nick-free & bump-free smooth skin</td></tr>
  <tr><th>Texture</th><td>Smooth water-lubricated frictionless glide</td></tr>
  <tr><th>Fragrance</th><td>Mild pleasant Aloe Vera scent</td></tr>
  <tr><th>Active Ingredients</th><td>3 Flexible Steel Blades, Aloe Vera & Vitamin E Moisture Strip</td></tr>
  <tr><th>Country of Origin</th><td>Poland / Mexico / Germany</td></tr>
  <tr><th>Manufacturer</th><td>Gillette (Procter & Gamble)</td></tr>
  <tr><th>Age Group</th><td>Teens & Women (Ages 14+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Hysteresis Hair Elevation & Aloe Lubrication Friction Reduction</h2>

<h3>What problem does this solve?</h3>
<p>Gillette Venus resolves razor nicks, cuts, skin irritation, ingrown hairs, and painful dry shaving.</p>

<h3>Why choose Gillette Venus?</h3>
<p>Distributing cutting force over 3 flexible blades combined with water-activated Aloe lubricant reduces steel friction against sensitive skin by up to 80%.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a 3-blade women's razor/blade system with Aloe Vera moisture strip from Gillette Venus ({count_info_en})."),
        ("What are the benefits of 3 flexible blades and Aloe moisture strip?", "3 flexible blades deliver an ultra-close smooth shave, while the Aloe moisture strip guards against nicks and irritation."),
        ("Does it protect against cuts, nicks, and razor bumps?", "Yes, clinically proven to provide a safe nick-free shave."),
        (f"What count/pack contents are included?", f"{count_info_en}."),
        ("How do I use it correctly?", "Wet skin with water and shaving gel, glide gently against hair growth, rinse with water."),
        ("Is the handle comfortable and anti-slip?", "Yes, ergonomic anti-slip handle comfortable under shower water."),
        ("Where is Gillette Venus manufactured?", "By Procter & Gamble."),
        ("How do I verify authenticity at Ekleel Abha?", "All Gillette products at Ekleel Abha are 100% original."),
        ("What is the benefit of the Venus moisture strip?", "Releases water-activated Aloe Vera lubricant for smooth glide."),
        ("Is it suitable for all body areas?", "Yes, excellent for legs, underarms, and sensitive bikini areas."),
        (f"Is the {count_info_en} pack economical?", "Yes, exceptional value and long usable lifetime."),
        ("How should I store the razor after use?", "In a dry place without wiping blades with a dry towel."),
        ("Is it safe for sensitive skin?", "Yes, dermatologically tested safe for sensitive skin."),
        ("When should I replace the razor blade?", "When the moisture strip fades or blade glides less smoothly."),
        ("Is Gillette Venus the #1 women's razor brand globally?", "Yes, Gillette Venus is the world's #1 women's shaving brand."),
        ("Is the packaging recyclable?", "Yes."),
        ("Is it suitable for teens and women?", "Yes, ages 14+."),
        ("Does it prevent ingrown hair?", "Yes, cuts hair cleanly preventing ingrown hair bumps."),
        ("Does it leave skin silky smooth?", "Yes, leaves skin touchably silky soft."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it glide easily with shave gel?", "Yes, glides effortlessly with shaving gel."),
        ("Does the razor head pivot around curves?", "Yes, razor head pivots smoothly around body curves."),
        ("Is it a practical personal care product?", "Yes, an essential item in personal care routines."),
        ("Does it cause skin darkening?", "No, safe shaving that does not darken skin."),
        ("Are Venus refill blades interchangeable?", "Yes, most Venus handles fit all Venus refill blades.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Gillette Venus",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. ماكينة وشفرات حلاقة نسائية ثلاثية بشريط ترطيب بالصبار لحلاقة ناعمة وآمنة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Gillette Venus 3-blade women's razor system with Aloe moisture strip. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1973():
    return _make_gillette_venus(
        pid=1973, gtin="7702018069255",
        ar_name="جليت سيمبلي فينوس مكينة ثلاثة شفرات1 + 4 حبة",
        en_name="Gillette Simply Venus 3-Blade Razor 1 + 4 Count",
        count_info_ar="1 ماكينة + 4 شفرات", count_info_en="1 Razor + 4 Blade Cartridges",
        feature_ar="تتضمن ماكينة مع 4 شفرات بديلة اقتصادية", feature_en="includes 1 razor plus 4 economical replacement blades",
        tags_ar=["جيليت_فينوس", "سيمبلي_فينوس", "ماكينة_حلاقة_نسائية", "حلاقة_فينوس", "إكليل_أبها"],
        tags_en=["gillette_venus", "simply_venus", "womens_razor", "venus_3blades", "ekleel_abha"]
    )


def create_product_1974():
    return _make_gillette_venus(
        pid=1974, gtin="7702018018116",
        ar_name="شفرات حلاقة سمبلي فينوسمن جيليت 3قطع",
        en_name="Gillette Simply Venus Razor Blades, 3 Pieces",
        count_info_ar="3 شفرات بديلة", count_info_en="3 Replacement Blades",
        feature_ar="عبوة من 3 شفرات بديلة فائقة الدقة", feature_en="pack of 3 precision replacement razor blades",
        tags_ar=["جيليت_فينوس", "شفرات_فينوس", "شفرات_حلاقة_نسائية", "فينوس_3_قطع", "إكليل_أبها"],
        tags_en=["gillette_venus", "venus_blades", "replacement_blades", "simply_venus_3pcs", "ekleel_abha"]
    )


def create_product_1975():
    return _make_gillette_venus(
        pid=1975, gtin="7702018545964",
        ar_name="شفرة حلاقة فينوس مع 9 شفرات بديلة من جيليت",
        en_name="Gillette Venus Razor with 9 Replacement Blades",
        count_info_ar="1 ماكينة + 9 شفرات بديلة", count_info_en="1 Razor + 9 Replacement Cartridges",
        feature_ar="مجموعة الحجم الضخم الاقتصادي مع 9 شفرات", feature_en="jumbo mega pack with 9 replacement blade cartridges",
        tags_ar=["جيليت_فينوس", "ماكينة_فينوس_9_شفرات", "عبوة_جامبو_فينوس", "حلاقة_نسائية", "إكليل_أبها"],
        tags_en=["gillette_venus", "venus_9blades", "jumbo_venus_pack", "womens_shaving", "ekleel_abha"]
    )


def _make_sensodyne_toothpaste(pid, gtin, ar_name, en_name, variant_ar, variant_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> معجون الأسنان الطبي التخصصي الأكثر توصية عالمياً من سنسوداين المصمم خصيصاً للراحة الفورية والحماية المستمرة من حساسية الأسنان مع الانتعاش الفائق. يرتكز هذا المعجون الطبي ({en_name}) على تركيبة نترات البوتاسيوم/فلوريد الصوديوم النشطة، مركبات التبييض والتنظيف الناعمة، وحبيبات الانتعاش الفوارة {variant_ar}.</p>
<p>يعمل معجون سنسوداين {variant_ar} على غلق قنوات عاج الأسنان المكشوفة لمنع آلام الحساسية الشديدة عند تناول المشروبات الباردة والساخنة، تقوية ميناء الأسنان ومكافحة التسوس، ومنح الفم والأنفاس انتعاشاً عاطراً يدوم طويلاً، ليترك أسنانك قوية، خالية من الألم، ومحمية من التسوس طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية ورعاية مثبتة سريرياً لحساسية الأسنان:</strong> يعالج آلام حساسية الأسنان المزعجة.</li>
  <li><strong>انتعاش فائق يدوم طويلاً بعطر {variant_ar}:</strong> يطرد رائحة الفم الكريهة ويمنح أنفاساً ناصعة.</li>
  <li><strong>تقوية ميناء الأسنان والحماية من التسوس بالفلوريد:</strong> يعيد بناء معادن الميناء الضعيفة.</li>
  <li><strong>إزالة اللويحات البكتيرية (البلاك) والتكتلات:</strong> ينظف الفواصل بين الأسنان بفاعلية.</li>
  <li><strong>معجون الأسنان رقم 1 الموصى به من أطباء الأسنان:</strong> العلامة الطبية الأكثر ثقة عالمياً لحساسية الأسنان.</li>
  <li><strong>عبوة مدمجة سعة 75 مل:</strong> حجم ممتاز للاستخدام العائلي اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية بحجم حبة البازلاء من معجون سنسوداين على فرشاة أسنان ناعمة.</li>
  <li><strong>الخطوة الثانية:</strong> نظفي الأسنان برفق بحركات دائرية لمدة دقيقتين كاملتين مرتين يومياً.</li>
  <li><strong>الخطوة الثالثة:</strong> ابصقي المعجون واشطفي الفم بالماء دون بلع (يُستعمل مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>نترات البوتاسيوم وفلوريد الصوديوم:</strong> يهدئان أعصاب الأسنان المتهيجة ويقويان ميناء السن ضد التسوس.</li>
  <li><strong>المكونات المنظفة وحبيبات الانتعاش:</strong> تمنحان الفم والأنفاس نظافة وانتعاشاً تدوم طوال اليوم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الفموي فقط، تجنبي البلع.</li>
  <li>غير مناسب للأطفال دون سن 12 سنة إلا بتوصية من طبيب الأسنان.</li>
  <li>في حال استمرار حساسية الأسنان استشيري طبيب الأسنان.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من حساسية الأسنان ويبحث عن {ar_name} للراحة والانتعاش.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سنسوداين (Sensodyne)</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم والأسنان / معاجين سنسوداين لحساسية الأسنان 75ml</td></tr>
  <tr><th>نوع المنتج</th><td>معجون أسنان طبي لعلاج الحساسية وتقوية الميناء والانتعاش (75ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>75 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الأسنان (خصيصاً الأسنان واللثة الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان قوية، محمية من الألم والتسوس ومفعمة بانتعاش {variant_ar}</td></tr>
  <tr><th>الملمس</th><td>معجون ناعم رغوي منعش</td></tr>
  <tr><th>العطر</th><td>عطر النعناع والـ {variant_ar} الفواح المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>نترات البوتاسيوم (Potassium Nitrate)، فلوريد الصوديوم، مركبات الانتعاش</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة المتحدة (UK) / الإمارات</td></tr>
  <tr><th>الشركة المصنعة</th><td>Haleon / GlaxoSmithKline (GSK)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون والمراهقون (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد نترات البوتاسيوم وفلوريد الصوديوم في سنسوداين ({variant_ar})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج معجون سنسوداين آلام حساسية الأسنان الشديدة عند تناول المشروبات الساخنة والباردة والحلويات، ورائحة الفم والتسوس.</p>

<h3>لماذا تنجح تركيبة Sensodyne؟</h3>
<p>لأن أيونات البوتاسيوم تفرز حظراً عصبياً داخل القنيات العاجية (Dentin Tubules) تمنع إشارات الألم من الوصول لعصب السن.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنظيف مرتين يومياً بالفرشاة الناعمة:</strong> يضمن حماية مستمرة من ألم الحساسية.<br>
2. <strong>عدم المضمضة الكثيفة بالماء فوراً بعد الغسيل:</strong> يدع طبقة الفلوريد تلتصق بالميناء.<br>
3. <strong>تجنب المشروبات الحمضية بكثرة:</strong> يمنع تآكل طبقة الميناء الوقائية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "معاجين حساسية الأسنان تسبب إضعاف السن وتعمل كمسكن مؤقت فقط."<br>
<strong>الحقيقة:</strong> سنسوداين يدعم ميناء السن بالفلوريد ويبني حماية عاجية طويلة الأمد بالاستخدام اليومي المنتظم.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخترق أيونات K+ القنوات العاجية وتلغي استقطاب أغشية الألياف العصبية المايلينية (A-beta & A-delta fibers) مانعة نسيج الألم.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو معجون أسنان طبي تخصصي من سنسوداين لعلاج حساسية الأسنان وتقوية الميناء والانتعاش ({variant_ar}) بسعة 75 مل."),
        (f"ما هي فوائد نترات البوتاسيوم والفلوريد وعطر {variant_ar}؟", f"تمنع نترات البوتاسيوم آلام الحساسية، يقوي الفلوريد الميناء، ويمنح عطر {variant_ar} أنفاساً ثلجية منعشة."),
        ("هل يوفر راحة مثبتة من آلام حساسية الأسنان؟", "نعم، مثبت سريرياً في توفير راحة وحماية مستمرة من آلام الحساسية."),
        (f"ما حجم العبوة؟", "تأتي بعبوة سعة 75 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية بحجم البازلاء، نظفي لمدة دقيقتين مرتين يومياً وابصقي المعجون."),
        ("هل يقوي ميناء الأسنان ويحميها من التسوس؟", "نعم، يحتوي على فلوريد الصوديوم لإعادة بناء وتقوية ميناء الأسنان."),
        ("أين صُنع معجون سنسوداين؟", "صُنع في المملكة المتحدة/الإمارات بواسطة شركة Haleon العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات سنسوداين لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {variant_ar} والنعناع الفواح المنعش."),
        ("هل يطرد رائحة الفم الكريهة؟", "نعم، يمنح الفم والأنفاس انتعاشاً عاطراً يمتد لساعات طويلة."),
        (f"هل العبوة 75 مل تكفي للاستخدام اليومي؟", "نعم، تكفي لعدة أسابيع من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل هو الماركة الأولى الموصى بها من أطباء الأسنان؟", "نعم، Sensodyne الماركة الأولى الموصى بها عالمياً من أطباء الأسنان للحساسية."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل يناسب الأطفال دون 12 سنة؟", "غير مخصص للأطفال دون 12 سنة إلا بتوصية طبيب الأسنان."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يعالج التصبغات السطحية؟", "نعم، ينظف اللويحات والتصبغات السطحية برفق دون خدش الميناء."),
        ("هل يسبب تهيج اللثة؟", "لا، تركيبة لطيفة للغاية مخصصة للثة والأسنان الحساسة."),
        ("هل يمنع آلام المشروبات الباردة والساخنة؟", "نعم، يغلق قنوات العاج المسببة للألم عند تناول المشروبات الساخنة والباردة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الاستخدام اليومي المستمر؟", "نعم، مصمم للاستخدام اليومي الدائم كمعجون رئيسي."),
        ("هل يعيد بناء طبقة الحماية للأسنان؟", "نعم، يساعد في بناء حماية مستمرة مع الاستخدام يومياً."),
        ("هل يصلح هدية ممتازة للعناية بالفم؟", "نعم، منتج طبي ممتاز لا غنى عنه."),
        ("هل يمنح شعوراً بالنظافة الفائقة؟", "نعم، يترك الفم والأسنان بنظافة وانتعاش فائقين."),
        ("هل تتوفر منه أنواع مفعول سريع وواقية أخرى؟", "نعم، تتوفر عائلة Sensodyne بخيارات متعددة.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is the world's #1 dentist-recommended specialized medical toothpaste from Sensodyne designed to provide clinically proven relief and lasting protection against tooth sensitivity with vibrant fresh breath. Built upon Potassium Nitrate and Sodium Fluoride, gentle cleansing compounds, and {variant_en} micro-fresh granules.</p>
<p>Sensodyne Toothpaste {variant_en} seals exposed dentin tubules preventing sharp nerve sensitivity pain triggered by hot, cold, or sweet food and drinks, strengthens tooth enamel, and neutralizes bad breath odor, leaving your teeth strong, pain-free, and protected against cavities all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Clinically Proven Tooth Sensitivity Relief:</strong> Rapidly calms sensitive nerve endings inside dentin.</li>
  <li><strong>Vibrant Long-Lasting {variant_en} Freshness:</strong> Eliminates bad breath odor imparting fresh icy breath.</li>
  <li><strong>Enamel Strengthening & Cavity Protection with Fluoride:</strong> Remineralizes weakened enamel surfaces.</li>
  <li><strong>Plaque & Bacterial Buildup Removal:</strong> Effectively cleanses interdental spaces.</li>
  <li><strong>#1 Dentist Recommended Toothpaste Brand:</strong> Globally trusted by dental experts for sensitivity care.</li>
  <li><strong>Compact 75ml Tube:</strong> Excellent volume for daily family dental routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a pea-sized amount of Sensodyne toothpaste onto a soft toothbrush.</li>
  <li><strong>Step 2:</strong> Brush teeth thoroughly in gentle circular motions for two minutes twice daily.</li>
  <li><strong>Step 3:</strong> Spit out toothpaste and rinse mouth with water without swallowing (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Potassium Nitrate & Sodium Fluoride:</strong> Desensitize nerve endings while reinforcing enamel against acid decay.</li>
  <li><strong>Cleansing Agents & Freshness Granules:</strong> Leave mouth and breath clean and intensely refreshed all day.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external oral use only; do not swallow.</li>
  <li>Not suitable for children under 12 years unless advised by a dentist.</li>
  <li>If tooth sensitivity pain persists, consult your dentist.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from tooth sensitivity seeking {en_name} for pain relief and long-lasting freshness.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Sensodyne</td></tr>
  <tr><th>Category</th><td>Oral Care / Sensodyne Sensitivity Toothpastes 75ml</td></tr>
  <tr><th>Product Type</th><td>Medical Sensitivity Relief, Enamel Protection & Fresh Toothpaste (75ml)</td></tr>
  <tr><th>Volume/Weight</th><td>75 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Teeth Types (Specifically Sensitive Teeth & Gums)</td></tr>
  <tr><th>Finish</th><td>Strong, pain-free, cavity-protected teeth with {variant_en} fresh breath</td></tr>
  <tr><th>Texture</th><td>Smooth refreshing foaming paste</td></tr>
  <tr><th>Fragrance</th><td>Invigorating {variant_en} mint scent</td></tr>
  <tr><th>Active Ingredients</th><td>Potassium Nitrate, Sodium Fluoride, Freshness Compounds</td></tr>
  <tr><th>Country of Origin</th><td>UK / UAE</td></tr>
  <tr><th>Manufacturer</th><td>Haleon / GlaxoSmithKline (GSK)</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Potassium Nitrate Nerve Desensitization & Sodium Fluoride Remineralization</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves sharp tooth sensitivity pain triggered by hot, cold, and sweet intake, bad breath, and enamel decay.</p>

<h3>Why choose Sensodyne Toothpaste?</h3>
<p>Potassium ions (K+) penetrate dentinal tubules desensitizing A-beta & A-delta nerve fibers while Sodium Fluoride deposits fluorapatite on enamel.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a specialized medical toothpaste from Sensodyne for sensitivity relief, enamel strengthening, and freshness ({variant_en}) in 75ml."),
        (f"What are the benefits of Potassium Nitrate, Fluoride, and {variant_en} fragrance?", "Potassium Nitrate prevents sensitivity pain, Fluoride strengthens enamel, and {variant_en} delivers icy fresh breath."),
        ("Does it provide proven relief from tooth sensitivity pain?", "Yes, clinically proven to provide lasting relief from tooth sensitivity."),
        ("What volume is contained in this tube?", "75ml tube."),
        ("How do I use it correctly?", "Apply pea-sized amount, brush for 2 minutes twice daily, spit and rinse."),
        ("Does it strengthen enamel and protect against cavities?", "Yes, contains Sodium Fluoride to rebuild and strengthen tooth enamel."),
        ("Where is Sensodyne Toothpaste manufactured?", "In UK/UAE by Haleon."),
        ("How do I verify authenticity at Ekleel Abha?", "All Sensodyne products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", f"Invigorating {variant_en} mint fragrance."),
        ("Does it eliminate bad breath?", "Yes, delivers long-lasting fresh breath for hours."),
        ("Does the 75ml tube last long?", "Yes, lasts weeks of regular daily use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Sensodyne the #1 dentist recommended brand?", "Yes, Sensodyne is the #1 dentist recommended brand for sensitivity worldwide."),
        ("How many times daily?", "Twice daily (morning & night)."),
        ("Is it suitable for children under 12?", "Not recommended for children under 12 unless advised by a dentist."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it clean surface stains?", "Yes, gently cleans plaque and surface stains without scratching enamel."),
        ("Does it cause gum irritation?", "No, gentle formula specifically designed for sensitive teeth and gums."),
        ("Does it prevent hot and cold sensitivity pain?", "Yes, seals dentin tubules preventing pain from hot and cold food/drinks."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for daily continuous use?", "Yes, designed for continuous daily use as a main toothpaste."),
        ("Does it rebuild protective tooth barrier?", "Yes, helps build continuous sensitivity protection with daily use."),
        ("Is it a practical oral care product?", "Yes, an indispensable dental health product."),
        ("Does it leave a clean refreshed mouth feel?", "Yes, leaves mouth and teeth feeling intensely clean and refreshed."),
        ("Are Rapid Action and other variants available?", "Yes, the Sensodyne family offers multiple specialized variants.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Sensodyne",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. معجون أسنان طبي من سنسوداين لحساسية الأسنان وتقوية الميناء والانتعاش {variant_ar}. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Sensodyne sensitivity relief & enamel protection toothpaste with {variant_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1976():
    return _make_sensodyne_toothpaste(
        pid=1976, gtin="6805699956027",
        ar_name="معجون إنتعاش زائد من سنسوداين - 75مل",
        en_name="Sensodyne Extra Fresh Toothpaste - 75ml",
        variant_ar="الانتعاش الزائد (Extra Fresh)", variant_en="Extra Fresh",
        feature_ar="يمنح الفم والأنفاس انتعاشاً ثلجياً متضاعفاً", feature_en="imparts doubled icy mint freshness to mouth and breath",
        tags_ar=["سنسوداين", "انتعاش_زائد", "معجون_حساسية_الأسنان", "سنسوداين_75مل", "إكليل_أبها"],
        tags_en=["sensodyne", "extra_fresh", "sensitivity_toothpaste", "sensodyne_75ml", "ekleel_abha"]
    )


def create_product_1977():
    return _make_sensodyne_toothpaste(
        pid=1977, gtin="6805699955501",
        ar_name="معجون اسنان  مفعول سريع من سنسوداين - 75مل",
        en_name="Sensodyne Rapid Action Toothpaste - 75 ml",
        variant_ar="المفعول السريع لـ 60 ثانية (Rapid Action)", variant_en="Rapid Action",
        feature_ar="يوفر راحة فورية من ألم الحساسية خلال 60 ثانية فقط", feature_en="delivers clinically proven fast sensitivity relief in just 60 seconds",
        tags_ar=["سنسوداين", "مفعول_سريع", "راحه_خلال_60_ثانية", "معجون_سنسوداين", "إكليل_أبها"],
        tags_en=["sensodyne", "rapid_action", "60_second_relief", "sensitivity_toothpaste", "ekleel_abha"]
    )


print("Loaded all 5 Batch 52 builders complete")
