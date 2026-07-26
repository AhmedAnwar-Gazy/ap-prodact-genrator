import json, os

def _make_cantu_b65(pid, gtin, ar_name, en_name, type_ar, type_en, weight_g, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> مستحضر التصفيف والعناية الفاخر الأصيل من كانتو العالمية المصمم خصيصاً لتنعيم، تحديد، وترطيب الشعر الكيرلي والمجعد أو بشرة الجسم دون أي قشور أو تيبس. يرتكز هذا المستحضر الأصيل ({en_name}) على زبدة الشيا وزبدة الكاكاو الصافية 100%، خلاصات بذور الكتان والمركبات الملطفة المغذية.</p>
<p>يعمل مستحضر كانتو على ترويض الهيشات وتحديد الخصلات الكيرلي أو تغذية بشرة الجسم عمقاً، حفظ الرطوبة الطبيعية، وإضفاء بريق ونعومة حريرية على التصفيفة والجلد، ليترك شعرك أو جسمك مصففاً بجمال، مرناً، ومحمياً من الجفاف طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتغذية مكثفة بزبدة الشيا والكاكاو الصافية 100%:</strong> تعيد اللين والنعومة للشعر والبشرة الجافة.</li>
  <li><strong>تحديد وتثبيت مرن للشعر والكيرلي:</strong> يبرز الكيرلي دون تيبس أو قشور بيضاء.</li>
  <li><strong>السيطرة الكاملة على الهيشات والتطاير:</strong> يحمي الشعر من الرطوبة والطقس.</li>
  <li><strong>تركيبة خالية من الكبريتات، السيليكون والبارابين:</strong> آمنة ونظيفة للاستخدام اليومي.</li>
  <li><strong>يمنح الشعر والبشرة لمعاناً طبيعياً براقاً:</strong> يغلف الخصلات والجلد ببريق صحي.</li>
  <li><strong>عبوة سعة {weight_g} جم/مل:</strong> حجم ممتاز للاستخدام اليومي والعناية المستمرة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> وزعي كمية مناسبة من مستحضر كانتو على شعر رطب أو جاف أو بشرة الجسم.</li>
  <li><strong>الخطوة الثانية:</strong> صففي الشعر بالأصابع أو دلكي البشرة بحركات دائرية حتى الامتصاص (يُستعمل عند التصفيف والعناية).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زبدة الشيا والكاكاو الطبيعية وخلاصات بذور الكتان:</strong> تغذي ساق الشعر والجلد وتمنح القوة والنعومة الفائقة.</li>
  <li><strong>المركبات النباتية المرطبة:</strong> تحفظ رطوبة الجلد والشعر الداخلية وتمنح مرونة عالية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على الشعر أو الجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لترطيب، تنعيم، وتصفية الشعر أو بشرة الجسم.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كانتو (Cantu)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر والبشرة / مستحضرات كانتو بزبدة الشيا والكاكاو وبذور الكتان {weight_g}g</td></tr>
  <tr><th>نوع المنتج</th><td>مستحضر تصفيف وترطيب وتحديد الشعر والبشرة ({type_ar}) {weight_g}g</td></tr>
  <tr><th>الحجم/الوزن</th><td>{weight_g} جم/مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (الكيرلي، المجعد، التالف) وبشرة الجسم الجافة</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر وبشرة ناعمة كالحرير، محددة، مرطبة عمقاً وخالية من الهيشات والجفاف</td></tr>
  <tr><th>الملمس</th><td>موس/كريم/بلسم ناعم غني ذو ثبات مرن</td></tr>
  <tr><th>العطر</th><td>عطر جوز الهند وجوز الشيا والكاكاو الاستوائي الفواح</td></tr>
  <tr><th>المكونات النشطة</th><td>زبدة الشيا والكاكاو الصافية، بذور الكتان، فيتامينات مغذية</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>PDC Brands USA</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد زبدة الشيا والكاكاو وبذور الكتان في كانتو (Cantu Care)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مستحضر كانتو مشكلة هيشان الشعر الكيرلي، تكسر الخصلات، جفاف بشرة الجسم، وفقدان اللمعان الطبيعي.</p>

<h3>لماذا تنجح تركيبة Cantu Pure Formula?</h3>
<p>لأن دمج زبدة الشيا والكاكاو وبذور الكتان يوفر غلافاً ترطيبياً يمنع تبخر الماء الداخلي من خلايا الكيراتين والجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق المباشر على الشعر أو البشرة الرطبة:</strong> يحفظ الترطيب الداخلي بأفضل صورة.<br>
2. <strong>التصفيف اللطيف بالأصابع:</strong> يمنع تكسر التجعدات الطبيعية الكيرلي.<br>
3. <strong>الاستمرار في الروتين اليومي:</strong> يمنح مرونة ونعومة فائقة للجلد والشعر.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مستحضرات الشيا والكاكاو تترك طبقة دهنية ملتصقة."<br>
<strong>الحقيقة:</strong> مستحضرات كانتو مصممة بامتصاص متوازن يغذي الشعر والجلد دون تراكم دهني ثقيل.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تغلف الأحماض الدهنية الأساسية ألياف الكيراتين والطبقة القرنية مانعة فقدان الترطيب ومحددة التموجات.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو مستحضر تصفيف وترطيب وتحديد للشعر أو الجسم من كانتو بحجم {weight_g} جم/مل."),
        ("ما هي فوائد زبدة الشيا والكاكاو وبذور الكتان؟", "تغذي وتنعيم الشعر والبشرة، تروض الهيشات، وتمنح ترطيباً ولمعاناً براقاً."),
        ("هل يحدد الكيرلي ويرطب دون قشور أو لزوجة؟", "نعم، مثبت سريرياً في تحديد التموجات وترطيب الجلد دون ترك قشور بيضاء."),
        (f"ما وزن العبوة؟", f"{weight_g} جم/مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي على شعر رطب أو جاف أو بشرة الجسم صففي بالأصابع أو دلكي حتى الامتصاص."),
        ("هل هو خالٍ من الكبريتات والسيليكون والبارابين؟", "نعم، 100% خالٍ من الكبريتات، السيليكون، والبارابين."),
        (f"أين صُنع مستحضر كانتو؟", "صُنع في الولايات المتحدة بواسطة PDC Brands USA."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كانتو لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", "عطر جوز الهند وجوز الشيا والكاكاو الاستوائي الفواح."),
        ("هل يناسب جميع أنواع الشعر والبشرة؟", "نعم، ممتاز للشعر الكيرلي والمجعد والتالف وبشرة الجسم الجافة."),
        (f"هل العبوة {weight_g} جم/مل تكفي لفترة جيدة؟", "نعم، تكفي لعدة أسابيع من الاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كانتو العلامة الأولى عالمياً في العناية بالكيرلي والبشرة؟", "نعم، Cantu العلامة العالمية الأكثر شهرة ومبيعا."),
        ("كم مرة يومياً؟", "عند التصفيف ورعاية البشرة."),
        ("هل يمنح الشعر والبشرة لمعاناً ونعومة حريرية؟", "نعم، يمنح لمعاناً طبيعياً ونعومة حريرية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في حماية الشعر من الجفاف؟", "نعم، يحمي الشعر والجلد من الجفاف والهيشات."),
        ("هل يترك ملمساً لزجاً؟", "ينفذ بمرونة دون ترك لزوجة أو تراكمات ثقيلة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يحمي من التأثيرات الجوية والرطوبة؟", "نعم، يغلف الخصلات والجلد ويحميهما من الرطوبة."),
        ("هل يصلح هدية ممتازة؟", "نعم، منتج أنيق وعملي جداً."),
        ("هل يعيد المظهر الصحي والمشرق؟", "نعم، يعيد الحيوية والقوة للشعر والبشرة."),
        ("هل يسهل التصفيف والعناية؟", "نعم، يجعل التصفيف والعناية سهلة وسلسة."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic luxury hair styling and skincare product from Cantu designed to smooth, define, and hydrate curly hair strands or body skin without flakes or stiffness. Built upon 100% Pure Shea Butter, Cocoa Butter, Flaxseed extracts, and nourishing conditioning compounds.</p>
<p>Cantu Product tames hair flyaways, defines natural curl patterns, deeply hydrates dry body skin, and locks in internal moisture while adding brilliant shine, leaving your hair or body skin beautifully styled, smooth, flexible, and protected all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intensive Hydration with 100% Pure Shea & Cocoa Butter:</strong> Restores softness to dry hair and body skin.</li>
  <li><strong>Flexible Hair & Curl Styling Definition:</strong> Highlights curls without stiffness or white flakes.</li>
  <li><strong>Complete Frizz & Flyaway Control:</strong> Shields hair against humidity and adverse weather.</li>
  <li><strong>Sulfate-Free, Silicone-Free & Paraben-Free Formula:</strong> Safe clean formula for daily hair and skin care.</li>
  <li><strong>Imparts Natural Luminous Shine:</strong> Coats hair strands and skin in a healthy soft luster.</li>
  <li><strong>Generous {weight_g}g/ml Size:</strong> Excellent volume for daily styling and continuous care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of Cantu product onto damp or dry hair or body skin.</li>
  <li><strong>Step 2:</strong> Style with fingers or massage onto skin until fully absorbed (use whenever styling or moisturizing).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Shea & Cocoa Butter with Flaxseed Extracts:</strong> Nourish hair shaft and skin imparting structural strength and extreme softness.</li>
  <li><strong>Moisturizing Botanical Agents:</strong> Lock in internal moisture preventing dryness and rough skin.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hair or body application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for styling, hydrating, and defining curly hair or body skin.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Cantu</td></tr>
  <tr><th>Category</th><td>Hair & Skincare / Cantu Shea & Cocoa Butter Products {weight_g}g</td></tr>
  <tr><th>Product Type</th><td>Styling & Hydrating Hair & Body Product ({type_en}) {weight_g}g</td></tr>
  <tr><th>Volume/Weight</th><td>{weight_g} g/ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Curly, Coily, Damaged) & Dry Body Skin</td></tr>
  <tr><th>Finish</th><td>Soft hair & skin, defined curls, deeply hydrated & frizz-free finish</td></tr>
  <tr><th>Texture</th><td>Rich smooth mousse/cream/conditioner with flexible hold</td></tr>
  <tr><th>Fragrance</th><td>Invigorating tropical coconut, shea & cocoa butter scent</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Shea & Cocoa Butter, Flaxseed Extracts, Nourishing Vitamins</td></tr>
  <tr><th>Country of Origin</th><td>USA</td></tr>
  <tr><th>Manufacturer</th><td>PDC Brands USA</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Pure Shea & Cocoa Butter Epidermal & Cuticle Moisture Occlusion</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves curly hair frizz, curl pattern collapse, dry body skin, and moisture loss.</p>

<h3>Why choose Cantu Pure Formula?</h3>
<p>Combining Pure Shea & Cocoa Butter with Flaxseed extracts forms a protective moisture seal shielding keratin and skin cells.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a hair styling, defining, or body moisturizing product from Cantu ({weight_g}g/ml)."),
        ("What are the benefits of shea butter, cocoa butter, and flaxseed?", "Nourish and soften hair and skin, tame frizz, and deliver shine and hydration."),
        ("Does it define curls and hydrate skin without flakes?", "Yes, clinically proven to define curls and hydrate skin without white flakes."),
        (f"What weight/volume is contained in this container?", f"{weight_g}g/ml."),
        ("How do I use it correctly?", "Apply to damp or dry hair or body skin, style with fingers or massage until absorbed."),
        ("Is it sulfate-free, silicone-free, and paraben-free?", "Yes, 100% free from sulfates, silicones, and parabens."),
        ("Where is Cantu Product manufactured?", "In the USA by PDC Brands USA."),
        ("How do I verify authenticity at Ekleel Abha?", "All Cantu products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", "Invigorating tropical coconut, shea, and cocoa butter fragrance."),
        ("Is it suitable for all hair and skin types?", "Yes, excellent for curly, coily, damaged hair and dry body skin."),
        (f"Does the {weight_g}g/ml container last long?", "Yes, lasts weeks of regular daily use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Cantu a globally leading brand?", "Yes, Cantu is a world-famous brand in hair and body care."),
        ("How many times daily?", "Whenever styling hair or moisturizing skin."),
        ("Does it impart shine and silky softness?", "Yes, gives hair and skin natural shine and silky softness."),
        ("Is the container recyclable?", "Yes."),
        ("Does it help protect against hair dryness?", "Yes, shields hair and skin against dryness and flyaways."),
        ("Does it leave a sticky residue?", "Penetrates flexibly without sticky residue or heavy buildup."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Does it shield hair and skin from weather?", "Yes, coats hair strands and skin guarding against humidity."),
        ("Is it a great gift for beauty lovers?", "Yes, elegant and practical gift for beauty routines."),
        ("Does it restore healthy radiant appearance?", "Yes, restores vitality and strength to hair and skin."),
        ("Does it make styling and care easy?", "Yes, makes styling and care smooth and effortless."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Cantu",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. مستحضر تصفيف وترطيب وتحديد من كانتو. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Cantu styling, hydrating, and defining product. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2038():
    return _make_cantu_b65(
        pid=2038, gtin="817513015700",
        ar_name="موس تمويج وتجعيد طبيعي احمر للشعر من كانتو248مل",
        en_name="Canto Natural Wave & Curl Mousse - Red Edition, 248ml",
        type_ar="موس رغوة لتحديد تموجات وكيرلي الشعر (النسخة الحمراء)", type_en="Natural Wave & Curl Mousse Red Edition", weight_g=248,
        feature_ar="موس رغوي أحمر لتحديد تموجات الكيرلي بمرونة ولمعان 248 مل", feature_en="wave and curl defining mousse red edition 248ml",
        tags_ar=["كانتو", "موس_كانتو_الاحمر", "موس_تمويج_الشعر", "تحديد_الكيرلي", "إكليل_أبها"],
        tags_en=["cantu", "cantu_mousse", "wave_curl_mousse", "cantu_red_mousse", "ekleel_abha"]
    )


def create_product_2039():
    return _make_cantu_b65(
        pid=2039, gtin="810006940589",
        ar_name="كريم مرطب جسم  بزبدة الكاكاو من كانتو،  240جم",
        en_name="Cantu Cocoa Butter Hydrating Body Cream, 240g",
        weight_g=240,
        type_ar="كريم مرطب مكثف للجسم بزبدة الكاكاو والشيا", type_en="Hydrating Cocoa Butter Body Cream",
        feature_ar="كريم ترطيب وتغذية مكثفة لبشرة الجسم بزبدة الكاكاو 240 جم", feature_en="intensive hydrating body cream with cocoa butter 240g",
        tags_ar=["كانتو", "كريم_جسم_كانتو", "زبدة_الكاكاو_كانتو", "ترطيب_الجسم", "إكليل_أبها"],
        tags_en=["cantu", "cantu_body_cream", "cocoa_butter_cream", "cantu_body_lotion", "ekleel_abha"]
    )


def create_product_2041():
    return _make_cantu_b65(
        pid=2041, gtin="817513019838",
        ar_name="بلسم  بذور الكتان من كانتو 400مل للتالف والمتقصف",
        en_name="Cantu Flaxseed Smoothing Conditioner 400ml",
        type_ar="بلسم مرطب ومنعم ببذور الكتان للشعر التالف", type_en="Flaxseed Smoothing Conditioner", weight_g=400,
        feature_ar="بلسم مغذي لمنع التقصف وتسهيل فك تشابك الشعر ببذور الكتان 400 مل", feature_en="smoothing flaxseed conditioner for damaged and split hair 400ml",
        tags_ar=["كانتو", "بلسم_كانتو", "بذور_الكتان_كانتو", "بلسم_الشعر_التالف", "إكليل_أبها"],
        tags_en=["cantu", "cantu_conditioner", "flaxseed_conditioner", "smoothing_conditioner", "ekleel_abha"]
    )


def create_product_2042():
    return _make_cantu_b65(
        pid=2042, gtin="810006940602",
        ar_name="كريم مرطب مزيج خام للشعر والجسم  بزبدة الكاكاو النقية من كانتو -  156جم",
        en_name="Cantu Raw Blend Moisturizing Cream with Pure Cocoa Butter for Hair and Body - 156g",
        type_ar="كريم مرطب مزيج خام (Raw Blend) للشعر والجسم", type_en="Raw Blend Pure Cocoa Butter Cream", weight_g=156,
        feature_ar="كريم ترطيب المزيج الخام 3 في 1 للشعر والجسم بزبدة الكاكاو 156 جم", feature_en="raw blend pure cocoa butter 3-in-1 moisturizing cream 156g",
        tags_ar=["كانتو", "المزيج_الخام_كانتو", "زبدة_الكاكاو_النقية", "ترطيب_الشعر_والجسم", "إكليل_أبها"],
        tags_en=["cantu", "raw_blend", "cantu_raw_blend", "cocoa_butter_hair_body", "ekleel_abha"]
    )


def create_product_2043():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول جسم عطري رومانسية الكركديه من لوكس 500مل (Lux Hibiscus Romance Perfumed Body Wash 500ml)</strong> سائل الاستحمام العطري الفاخر الأيقوني من لوكس المصمم لمنح جسمك نظافة عميقة ورغوة مخملية غنية وعطراً فواحاً يدوم لـ 24 ساعة. يرتكز هذا الغسول الأصيل (Lux Hibiscus Romance 500ml) على زيت الزهور المسكوبة نادرة الوجود (Everscent Essential Oil)، خلاصة زهور الكركديه الرومانسية، والمركبات المرطبة لبشرة الجسم.</p>
<p>يعمل غسول لوكس برومانسية الكركديه على تنظيف مسام الجسم وإزالة الدهون والأوساخ، حماية الجلد من الجفاف وحفظ طراوته، وتغليف جسمك بنفحات الزهور الفواحة الساحرة، ليترك بشرتك ناعمة كالحرير، مرطبة، ومعطرة بالنظافة والأناقة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عطر فواح يدوم لـ 24 ساعة بزيت الزهور المسكوبة:</strong> يمنح الجسد عبقاً رومانسياً فواحاً طول اليوم.</li>
  <li><strong>تنظيف عميق ورغوة كريمية غنية:</strong> ينظف الجسم بلطف دون انتزاع الزيوت الطبيعية.</li>
  <li><strong>ترطيب وتنعيم لبشرة الجسم:</strong> يحفظ حاجز الترطيب الطبيعي للجلد.</li>
  <li><strong>تركيبة خفيفة متوازنة الحموضة (pH Balanced):</strong> مناسبة للاستخدام اليومي لجميع أنواع البشرة.</li>
  <li><strong>جودة لوكس (Lux) العالمية الشهيرة:</strong> العلامة الأولى في عطور وجمال الاستحمام.</li>
  <li><strong>عبوة سعة 500 مل بضاغط أنيق:</strong> حجم ممتاز للاستخدام العائلي اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الجسم بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> اضغطي كمية مناسبة من سائل لوكس على ليفة الاستحمام أو الكفين وكوّني رغوة غنية.</li>
  <li><strong>الخطوة الثالثة:</strong> دلكي الجسم برفق بحركات دائرية ثم اشطفي جيداً بالماء (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الزهور الأساسية وخلاصة الكركديه:</strong> تثبت العطر الفواح على ألياف البشرة وتمنح انطباعاً عاطراً.</li>
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
  <li>لكل امرأة تبحث عن غسول لوكس برومانسية الكركديه 500 مل للانتعاش العطري والنظافة الحريرية.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لوكس (Lux)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / غسولات ومجموعات الاستحمام المعطرة من لوكس 500ml</td></tr>
  <tr><th>نوع المنتج</th><td>غسول جسم عطري مرطب بنفحات زهور الكركديه وزيت Everscent (500ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (العادية، الجافة والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، مرطب، ناصع النظافة ومفعم بعطر الكركديه لـ 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>سائل جل عطري رغوي غني</td></tr>
  <tr><th>العطر</th><td>عطر رومانسية زهور الكركديه الفواح لـ 24 ساعة</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت Everscent Essential Oil، خلاصة الكركديه، منظفات لطيفة</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الإمارات</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever Group</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت Everscent وخلاصة الكركديه في غسول لوكس (Lux Hibiscus Romance)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول لوكس مشكلة جفاف البشرة بعد الاستحمام بالصابون القاسي، تراكم الدهون، وتلاشي عطر النظافة سريعاً.</p>

<h3>لماذا تنجح تركيبة Lux Hibiscus Romance؟</h3>
<p>لأن تقنية زيوت Everscent العطرية تفرز جزيئات عطرية ترتبط بروابط البروتين الجلدية لتمنح ثباتاً عاطراً لـ 24 ساعة.</p>

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
        ("ما هو غسول جسم عطري رومانسية الكركديه من لوكس 500مل؟", "هو سائل استحمام عطري فاخر من لوكس بنفحات زهور الكركديه وزيت Everscent لثبات العطر 24 ساعة (500 مل)."),
        ("ما هي فوائد خلاصة الكركديه وزيت Everscent؟", "تنظف المنظفات اللطيفة البشرة دون جفاف، بينما يثبت زيت Everscent عطر الكركديه لـ 24 ساعة."),
        ("هل يمنح رغوة غنية وعطراً يدوم لـ 24 ساعة؟", "نعم، مثبت سريرياً في توفير رغوة غنية وثبات عطري يدوم 24 ساعة."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة مزودة بضاغط بسعة 500 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الجسم، اضغطي كمية على الليفة وكوّني رغوة، دلكي برفق واشطفي بالماء يومياً."),
        ("هل هو آمن لجميع أنواع البشرة؟", "نعم، تركيبة متوازنة الحموضة آمنة لجميع أنواع بشرة الجسم."),
        ("أين صُنع غسول لوكس؟", "صُنع بواسطة مجموعة Unilever العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لوكس لدى إكليل أبها أصلية 100%."),
        ("ما رائحة غسول لوكس الكركديه؟", "عطر زهور الكركديه الفواح الرومانسي الأنيق."),
        ("هل يترك البشرة ناعمة ومرطبة؟", "نعم، يحافظ على رطوبة الجلد ونعومته الحريرية."),
        ("هل 500 مل تكفي للاستخدام العائلي؟", "نعم، عبوة ممتازة تكفي لعدة أسابيع من الاستخدام العائلي اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع أفراد الأسرة وخاصة محبي العطور الزهرية الفاخرة."),
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
<p>The <strong>Lux Hibiscus Romance Perfumed Body Wash 500ml</strong> is an iconic luxury fragranced body wash from Lux designed to deliver deep cleansing, a rich velvety lather, and a 24-hour long-lasting floral fragrance. Built upon Everscent Essential Oil technology, romantic Hibiscus flower extract, and body-moisturizing compounds.</p>
<p>Lux Hibiscus Romance Body Wash cleanses body pores of dirt and excess sebum, guards skin against dryness, and wraps your body in enchanting floral notes, leaving your skin touchably silky soft, hydrated, and fragranced with elegance all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>24-Hour Long-Lasting Fragrance with Everscent Oil:</strong> Coats body in a romantic floral scent all day.</li>
  <li><strong>Deep Cleansing & Rich Creamy Lather:</strong> Cleanses body gently without stripping natural skin oils.</li>
  <li><strong>Body Skin Softening & Hydration:</strong> Preserves the skin's natural moisture barrier.</li>
  <li><strong>pH-Balanced Mild Formula:</strong> Suitable for daily use on all skin types.</li>
  <li><strong>Famous Quality of Lux Global:</strong> #1 recognized brand in perfumed bath and beauty care.</li>
  <li><strong>Convenient 500ml Pump Bottle:</strong> Excellent value lasting weeks of continuous daily family use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet body skin with warm water during shower.</li>
  <li><strong>Step 2:</strong> Pump a suitable amount of Lux gel onto a shower loofah or hands and work into a rich lather.</li>
  <li><strong>Step 3:</strong> Massage body gently in circular motions, then rinse thoroughly with water (use daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Everscent Essential Oil & Hibiscus Extract:</strong> Bind fragrance molecules to skin layers delivering 24-hour freshness.</li>
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
  <li>Every woman seeking Lux Hibiscus Romance 500ml Body Wash for 24-hour fragrance and silky clean skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lux</td></tr>
  <tr><th>Category</th><td>Body Care / Lux Perfumed Hydrating Body Washes 500ml</td></tr>
  <tr><th>Product Type</th><td>24H Perfumed Hibiscus & Everscent Essential Oil Body Wash (500ml)</td></tr>
  <tr><th>Volume/Weight</th><td>500 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Normal, Dry & Oily Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, hydrated, spotlessly clean body skin fragranced with Hibiscus for 24H</td></tr>
  <tr><th>Texture</th><td>Rich foaming fragranced clear gel fluid</td></tr>
  <tr><th>Fragrance</th><td>Romantic long-lasting Hibiscus floral scent for 24 hours</td></tr>
  <tr><th>Active Ingredients</th><td>Everscent Essential Oil, Hibiscus Extract, Gentle Cleansers</td></tr>
  <tr><th>Country of Origin</th><td>KSA / UAE</td></tr>
  <tr><th>Manufacturer</th><td>Unilever Group</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Everscent Essential Oil Binding & 24-Hour Floral Fragrance Retention</h2>

<h3>What problem does this solve?</h3>
<p>Lux Hibiscus Romance Body Wash resolves skin dryness caused by harsh soaps, daily sweat accumulation, and fading body fragrance.</p>

<h3>Why choose Lux Body Wash?</h3>
<p>Everscent Essential Oil technology binds perfume micro-droplets to skin keratin providing sustained 24-hour fragrance release.</p>"""

    en_faqs = [
        ("What is Lux Hibiscus Romance Perfumed Body Wash 500ml?", "It is a luxury perfumed body wash from Lux with Hibiscus flowers and Everscent Oil for 24-hour fragrance (500ml)."),
        ("What are the benefits of Hibiscus extract and Everscent Oil?", "Gentle cleansers cleanse skin without dryness, while Everscent Oil binds Hibiscus fragrance for 24 hours."),
        ("Does it yield a rich lather and 24-hour fragrance?", "Yes, clinically proven to produce a rich lather and deliver 24-hour fragrance retention."),
        ("What volume is contained in this bottle?", "500ml pump bottle."),
        ("How do I use it correctly?", "Wet body, pump gel onto loofah, lather, massage gently and rinse with water daily."),
        ("Is it safe for all skin types?", "Yes, pH-balanced formula safe for all body skin types."),
        ("Where is Lux Body Wash manufactured?", "By Unilever Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All Lux products at Ekleel Abha are 100% original."),
        ("What scent does Lux Hibiscus Romance have?", "Romantic elegant Hibiscus floral fragrance."),
        ("Does it leave skin soft and hydrated?", "Yes, preserves skin moisture and silky softness."),
        ("Does 500ml last long for family use?", "Yes, pump bottle lasts weeks of regular family use."),
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
        "product_id": "2043",
        "sku": "EK-2043",
        "gtin": "6281006569560",
        "brand": "Lux",
        "ar": {
            "title": "غسول جسم عطري رومانسية الكركديه من لوكس 500مل",
            "meta_title": "غسول جسم لوكس الكركديه 500مل | إكليل أبها",
            "meta_description": "اشتري غسول جسم عطري رومانسية الكركديه من لوكس (500 مل). سائل استحمام بعطر الكركديه الفواح لـ 24 ساعة وترطيب البشرة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["لوكس", "غسول_جسم_لوكس_500مل", "رومانسية_الكركديه", "سائل_استحمام_معطر", "إكليل_أبها"]
        },
        "en": {
            "title": "Lux Hibiscus Romance Perfumed Body Wash 500ml",
            "meta_title": "Lux Hibiscus Romance Body Wash 500ml | Ekleel Abha",
            "meta_description": "Buy original Lux Hibiscus Romance Perfumed Body Wash (500ml). 24H perfumed Hibiscus floral body wash. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["lux", "lux_body_wash_500ml", "hibiscus_romance", "perfumed_body_wash", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 65 builders complete")
