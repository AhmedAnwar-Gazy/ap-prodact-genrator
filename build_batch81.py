import json, os

def _make_lakme_developer_b81(pid, gtin, ar_title, en_title, vol_str, percent_str, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_title}</strong> مظهر اللون والصبغة الطبي المحترف الفاخر الأصيل من لاكمي تيكنيا كولور (Lakme Collage / Gloss OXY Cream) المصمم خصيصاً لتفعيل وتفتيح لون صبغات وسحب لون الشعر بتركيز {vol_str} ({percent_str} Hydrogen Peroxide) وتوفير نتائج تفتيح متجانسة وحماية فائقة لألياف الشعر أثناء التلوين. يرتكز هذا الأكسجين الأصيل ({en_title}) على بيروكسيد الهيدروجين النقي، زيت الأبيسينين المرطب (Abyssinian Oil)، والمكونات المهدئة للفروة.</p>
<p>يعمل أكسجين كريم لاكمي بتركيز {vol_str} على فتح حراشف الشعر بسلاسة لتغلغل صبغة اللون، حماية هيكل الكيراتين الداخلي من التلف والتقصف، وإعطاء لون صبغة زاهي ومستقر لعدة أسابيع، ليترك شعرك المصبوغ ناعماً كالحرير، مرطباً، ناصع اللون، ومحمياً من الجفاف من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وتفعيل مثالي للصبغة بتركيز {vol_str} ({percent_str} Hydrogen Peroxide):</strong> يفتح اللون بتجانس فائق.</li>
  <li><strong>حماية ألياف وكيراتين الشعر بزيت الأبيسينين:</strong> يمنع الجفاف والتلف الناتج عن التلوين.</li>
  <li><strong>قوام كريمي متماسك يسهل الخلط والتطبيق دون تساقط:</strong> يندمج بسلاسة مع صبغات ومسحوق التفتيح.</li>
  <li><strong>تركيبة مهدئة لفروة الرأس تقي التحسس والحرقان:</strong> تمنح راحة تامة أثناء الصبغ.</li>
  <li><strong>جودة لاكمي (Lakme Cosmetics Spain) الإسبانية الشهيرة:</strong> الأكسجين المفضل بمشاغل وصالونات التجميل.</li>
  <li><strong>عبوة سعة 120 مل بحجم مالي ممتاز:</strong> تكفي لصبغة كاملة وشعر متوسط إلى طويل.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> اخلطي أكسجين كريم لاكمي {vol_str} مع صبغة لاكمي في وعاء غير معدني بالنسبة الموصى بها (مثال 1:1.5).</li>
  <li><strong>الخطوة الثانية:</strong> وزعي المزيج الكريمي على خصلات الشعر بالفرشاة المخصصة.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركي المزيج 30-40 دقيقة ثم اشطفي جيداً بالماء والشامبو (يُستعمل عند الصبغ).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>بيروكسيد الهيدروجين ({percent_str} H2O2 / {vol_str}):</strong> يفتح صبغة الشعر الطبيعية ويتيح ثبات اللون الجديد.</li>
  <li><strong>زيت الأبيسينين والمركبات المطرية:</strong> يغلفان الشعر ويحفظان رطوبته ونعومته أثناء الصباغة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي المهني والموضعي على شعر الرأس فقط؛ يحتوي على بيروكسيد الهيدروجين.</li>
  <li>يجب ارتداء القفازات المناسبة وتجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن الحرارة والشمس.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_title} لتفتيح وتفعيل صبغات الشعر بآمان وبحجم مدمج 120 مل.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لاكمي (Lakme Color Spain)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / أكسجين ومظهرات لون الصبغة 120ml</td></tr>
  <tr><th>نوع المنتج</th><td>كريم أكسجين مظهر للون الصبغة بتركيز {vol_str} {percent_str} بزيت الأبيسينين (120ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>120 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (خصيصاً المجهد والمصبوغ والمطلوب تفتيحه بتجانس)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم كالحرير، مرطب، لون صبغة ناصع ومتجانس ومحمي من التلف</td></tr>
  <tr><th>الملمس</th><td>كريم دسم أبيض متماسك يسهل الدمج والخلط</td></tr>
  <tr><th>العطر</th><td>عطر كتم كريمي لطيف محايد</td></tr>
  <tr><th>المكونات النشطة</th><td>بيروكسيد الهيدروجين {percent_str} ({vol_str})، زيت الأبيسينين، مرطبات جلدية</td></tr>
  <tr><th>بلد المنشأ</th><td>إسبانيا (Spain)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Lakme Cosmetics Spain</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون (من 18 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد زيت الأبيسينين وبيروكسيد الهيدروجين {percent_str} في أكسجين لاكمي (Lakme OXY Cream {vol_str})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج أكسجين كريم لاكمي بتركيز {vol_str} مشكلة التفتيح غير المتجانس، تلف حراشف الشعر أثناء الصبغ، التحسس، وبهتان صبغات الشعر.</p>

<h3>لماذا تنجح تركيبة Lakme Color Developer OXY Cream {vol_str} ({percent_str})؟</h3>
<p>لأن تركيز {vol_str} يفتح درجات الشعر بدقة متناهية بينما يحمي زيت الأبيسينين الروابط البيبتيدية للكيراتين.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الخلط بالوعاء البلاستيكي بالمعايير الصحيحة:</strong> يضمن تجانس المزيج الكريمي.<br>
2. <strong>ارتداء القفازات وتجنب ملامسة الفروة المتهجة:</strong> يضمن صباغة مريحة وآمنة.<br>
3. <strong>الشطف بالماء والشامبو المخصص بعد انتهاء الوقت:</strong> يوقف تفاعل الأكسدة ويحفظ اللون.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الأكسجين يسبب تكسر وتساقط الشعر دائماً."<br>
<strong>الحقيقة:</strong> أكسجين لاكمي الإسباني مدعم بزيت الأبيسينين لحماية الألياف ومنع التكسر والتلف كلياً أثناء التلوين.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يفتح بيروكسيد الهيدروجين {percent_str} ميلانين الشعر ويتيح إرساء الصبغات الجديدة بينما يغلف زيت الأبيسينين الجدار الخارجي.</p>"""

    faqs_data = [
        (f"ما هو {ar_title}؟", f"هو كريم أكسجين طبي مظهر ومفتّح لصبغات الشعر بتركيز {vol_str} ({percent_str}) بزيت الأبيسينين من لاكمي (120 مل)."),
        (f"ما هي فوائد بيروكسيد الهيدروجين {percent_str} وزيت الأبيسينين؟", "يفتح الشعر بتجانس، يفعل صبغات الشعر، ويحمي الألياف والكيراتين من التلف."),
        ("هل يفتح اللون ويفعل الصبغة بتجانس وبدون تلف؟", "نعم، مثبت سريرياً في تفتيح الشعر وتفعيل صبغات اللون بتجانس وحماية كاملة لألياف الشعر."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة سعة 120 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اخلطي مع الصبغة في وعاء غير معدني، وزعي بالفرشاة واتركيه 30-40 دقيقة ثم اشطفي."),
        ("هل هو آمن ومختبر في الصالونات الإسبانية؟", "نعم، 100% آمن ومختبر درماتولوجياً وفي صالونات التجميل العالمية."),
        ("أين صُنع أكسجين كريم لاكمي؟", "صُنع في إسبانيا بواسطة Lakme Cosmetics Spain."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لاكمي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب جميع أنواع الصبغات ومساحيق التفتيح؟", "نعم، ممتاز لخلطه مع جميع أنواع صبغات لاكمي."),
        ("هل يمنع خشونة وتلف الشعر بعد الصبغ؟", "نعم، ينعم ويغلف الشعر بزيت الأبيسينين لمنع الخشونة والتلف."),
        ("هل عبوة 120 مل مناسبة للاستخدام الشخصي؟", "نعم، عبوة أنيقة تكفي لصبغة كاملة وشعر متوسط إلى طويل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الحرارة وضوء الشمس."),
        ("هل لاكمي الماركة الأولى في صبغات وأكسجين الشعر؟", "نعم، Lakme Color الماركة الإسبانية رقم 1 العالمية الأكثر ثقة وتفضيلاً."),
        ("متى يُستعمل؟", "عند التلوين وصباغة الشعر."),
        ("هل يمتزج بسهولة دون تكتل؟", "نعم، قوام كريمي دسم يمتزج فورياً وسلس مع الصبغات."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يقلل الحرقان والتحسس بالفروة؟", "نعم، مدعم بمركبات مهدئة تقلل تحسس الفروة أثناء الصبغ."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الاستخدام المنزلي والمهني؟", "نعم، ممتاز للاستخدام المنزلي والمهني بالصالونات."),
        ("هل يناسب الشتاء والصيف؟", "نعم، أكسجين صبغ مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة لمن تصبغ شعرها؟", "نعم، منتج صالونات فاخر وأساسي لكل روتين صباغة وتلوين."),
        ("هل يعيد المظهر الناعم السلس للشعر المصبوغ؟", "نعم، يجعل الشعر المصبوغ في غاية النعومة والنقاء."),
        (f"هل تتوفر تراكيز أكسجين لاكمي الأخرى؟", "نعم، تتوفر تراكيز Lakme OXY Creams كاملة لدى إكليل أبها."),
        ("هل يمنح لون صبغة ناصع ومستقر؟", "نعم، يضمن استقرار اللون وزهاء الصبغة لعدة أسابيع."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury professional hair color developer cream from Lakme Cosmetics Spain designed to activate, lift, and develop hair color dyes at {vol_str} ({percent_str} Hydrogen Peroxide) while delivering uniform lifting and superior hair fiber protection. Built upon pure Hydrogen Peroxide, hydrating Abyssinian Oil, and scalp-soothing emollient compounds.</p>
<p>Lakme {vol_str} OXY Cream smoothly opens hair cuticles for optimal pigment penetration, shields internal keratin structures from damage and breakage, and ensures vibrant long-lasting color results, leaving your color-treated hair touchably silky soft, hydrated, brilliantly colored, and protected from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Optimal {vol_str} Color Lift & Activation ({percent_str} Hydrogen Peroxide):</strong> Lifts hair color evenly.</li>
  <li><strong>Hair Fiber & Keratin Protection with Abyssinian Oil:</strong> Prevents chemical dryness and damage.</li>
  <li><strong>Creamy Smooth Consistency for Easy Non-Drip Mixing:</strong> Blends effortlessly with hair dyes.</li>
  <li><strong>Scalp Soothing Formulation:</strong> Minimizes scalp irritation and stinging during dyeing.</li>
  <li><strong>Famous Spanish Salon Lakme Quality:</strong> #1 choice in professional hair salons worldwide.</li>
  <li><strong>Convenient 120ml Bottle:</strong> Outstanding size for full head application.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Mix Lakme {vol_str} OXY Cream with Lakme hair dye in a non-metallic bowl at the recommended ratio (e.g. 1:1.5).</li>
  <li><strong>Step 2:</strong> Apply the smooth creamy mixture onto hair strands using a tint brush.</li>
  <li><strong>Step 3:</strong> Process for 30-40 minutes depending on desired lift, then rinse thoroughly with water and shampoo (use during hair coloring).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>{percent_str} Hydrogen Peroxide ({vol_str} H2O2):</strong> Lightens natural hair melanin enabling vibrant color deposition.</li>
  <li><strong>Abyssinian Oil & Emollients:</strong> Coat hair strands maintaining moisture and softness during chemical processing.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external professional topical hair application only; contains Hydrogen Peroxide.</li>
  <li>Wear suitable gloves and avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from heat and direct sunlight.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_title} for safe personal and professional hair color lifting and activation.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lakme Color (Spain)</td></tr>
  <tr><th>Category</th><td>Hair Care / Lakme Professional Color Developers 120ml</td></tr>
  <tr><th>Product Type</th><td>{vol_str} ({percent_str}) Abyssinian Oil Professional Hair Color Developer Cream (120ml)</td></tr>
  <tr><th>Volume/Weight</th><td>120 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Specifically Hair Requiring Even Color Lift & Dye Activation)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, vibrant & damage-free evenly colored hair</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-drip white developer cream</td></tr>
  <tr><th>Fragrance</th><td>100% Mild gentle neutral creamy scent</td></tr>
  <tr><th>Active Ingredients</th><td>{percent_str} Hydrogen Peroxide ({vol_str}), Abyssinian Oil, Skin Soothing Emollients</td></tr>
  <tr><th>Country of Origin</th><td>Spain</td></tr>
  <tr><th>Manufacturer</th><td>Lakme Cosmetics Spain</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 18+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of {percent_str} Hydrogen Peroxide Melanin Oxidation & Abyssinian Fiber Shielding</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves uneven color lifting, chemical fiber damage during dyeing, scalp stinging, and color fading.</p>

<h3>Why choose Lakme OXY Cream {vol_str}?</h3>
<p>Concentrated {vol_str} ({percent_str} H2O2) lifts hair levels with precision while Abyssinian oil coats keratin fibers preventing chemical breakage.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a professional {vol_str} ({percent_str}) hair color developer cream from Lakme Spain with Abyssinian Oil (120ml)."),
        (f"What are the benefits of {percent_str} Hydrogen Peroxide and Abyssinian Oil?", "Lifts hair color evenly, activates color dyes, and protects hair fibers and keratin from chemical damage."),
        ("Does it lift hair color evenly and protect hair from chemical damage?", "Yes, clinically proven to lift hair color evenly while protecting hair fibers with Abyssinian oil."),
        ("What volume is contained in this bottle?", "120ml sleek bottle."),
        ("How do I use it correctly?", "Mix with hair dye in a non-metallic bowl, apply with brush, process 30-40 minutes and rinse thoroughly."),
        ("Is it safe and tested in Spanish professional salons?", "Yes, 100% safe, dermatologically tested, and trusted in international professional salons."),
        ("Where is Lakme OXY Cream manufactured?", "In Spain by Lakme Cosmetics Spain."),
        ("How do I verify authenticity at Ekleel Abha?", "All Lakme products at Ekleel Abha are 100% original."),
        ("Is it suitable for mixing with all dyes?", "Yes, excellent for mixing with all Lakme hair dyes."),
        ("Does it prevent hair roughness after dyeing?", "Yes, nourishes and coats hair with Abyssinian oil preventing chemical roughness."),
        ("Is the 120ml bottle convenient for home use?", "Yes, sleek bottle ideal for full head application at home."),
        ("How should I store it?", "In a cool, dry place away from heat and direct sunlight."),
        ("Is Lakme a #1 salon hair color brand?", "Yes, Lakme Color is a premier globally trusted Spanish professional hair color brand."),
        ("When is it used?", "During hair dyeing and color lifting processing."),
        ("Does it mix smoothly without clumping?", "Yes, rich smooth cream blends instantly and smoothly with dyes."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it reduce scalp stinging?", "Yes, formulated with soothing emollients reducing scalp stinging during coloring."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for hair colorists and home use?", "Yes, suitable for both salon colorists and home hair coloring."),
        ("Is it good for all seasons?", "Yes, ideal hair developer for summer and winter care."),
        ("Is it a nice gift for hair coloring?", "Yes, a premier salon essential for hair coloring routines."),
        ("Does it restore smooth vibrant color-treated hair?", "Yes, gives color-treated hair a healthy smooth vibrant look."),
        (f"Are other Lakme OXY Cream volumes available?", "Yes, the full Lakme OXY Cream range is available at Ekleel Abha."),
        ("Does it deliver long-lasting vibrant color results?", "Yes, ensures vibrant long-lasting color results for weeks."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Lakme",
        "ar": {
            "title": ar_title,
            "meta_title": f"{ar_title} | إكليل أبها",
            "meta_description": f"اشتري {ar_title}. مظهر لون الصبغة الإسباني بزيت الأبيسينين لتفتيح الشعر وتفعيل الصبغات 120 مل. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. Professional Abyssinian Oil hair color developer cream 120ml. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2126():
    return _make_lakme_developer_b81(
        pid=2126, gtin="8429421403115",
        ar_title="اوكسجين كريم   (8.4 %) 28 v  من لاكمي 120 مل",
        en_title="Lakme Color Developer Cream (8.4%) 28 Vol - 120 ml",
        vol_str="28 Vol", percent_str="8.4%",
        feature_ar="أكسجين كريم 28 Vol (8.4%) 120 مل بزيت الأبيسينين لتفتيح الشعر 2-3 درجات", feature_en="Lakme 28 Vol (8.4%) Color Developer Cream 120ml",
        tags_ar=["لاكمي", "أكسجين_لاكمي_28v_120مل", "مظهر_صبغة_لاكمي", "أكسجين_لاكمي_120مل", "إكليل_أبها"],
        tags_en=["lakme", "lakme_oxy_cream_28vol_120ml", "color_developer_120ml", "lakme_developer", "ekleel_abha"]
    )


def create_product_2127():
    return _make_lakme_developer_b81(
        pid=2127, gtin="8429421402118",
        ar_title="اوكسجين كريم   (5.4 %) 18 v  من لاكمي 120 مل",
        en_title="Lakme Color Developer OXY Cream (5.4%) 18V - 120ml",
        vol_str="18 Vol", percent_str="5.4%",
        feature_ar="أكسجين كريم 18 Vol (5.4%) 120 مل بزيت الأبيسينين للتثبيت وتفتيح درجة واحدة", feature_en="Lakme 18 Vol (5.4%) Color Developer OXY Cream 120ml",
        tags_ar=["لاكمي", "أكسجين_لاكمي_18v_120مل", "مظهر_صبغة_لاكمي_18v", "أكسجين_لاكمي_120مل", "إكليل_أبها"],
        tags_en=["lakme", "lakme_oxy_cream_18vol_120ml", "color_developer_18vol", "lakme_developer", "ekleel_abha"]
    )


def create_product_2128():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>قناع الشعر تيكينيا وايت سيلفر معزز للون الرمادي والزيتي من لاكمي، 250 مل (Lakmé Teknia White Silver Hair Mask for Grey and Ash Tones, 250 ml)</strong> الماسك البنفسجي المعالج والمغذي والمحييد للاصفرار الفاخر الأصيل من لاكمي تيكنيا (Lakmé Teknia White Silver Mask) المصمم خصيصاً لترميم، تحييد الانعكاسات الصفراء والبرتقالية، وإعادة البرق الفضي والزيتي البارد للشعر الأشقر والرمادي والزيتي المصبوغ. يرتكز هذا الماسك الأصيل (Lakme White Silver Mask 250ml) على الصبغة البنفسجية المركز النقية (Direct Violet Pigment)، زهرة الخزامى العضوية (Organic Lotus Flower)، ونظام Ceramide Rebuild System.</p>
<p>يعمل ماسك لاكمي وايت سيلفر على ترويض التقصف والخشونة في الشعر المصبوغ، إعادة بناء السيراميدات التالفة بفعل الصبغة، وحماية ثبات اللون الرمادي والزيتي، ليترك شعرك ناعماً كالحرير، مرطباً عمقاً، ناصع الفضة، ومفعماً بالبريق واللمعان البارد من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تحييد الانعكاسات الصفراء والبرتقالية وتعزيز اللون الرمادي والزيتي:</strong> يمنح نغمة فضية باردة ناصعة.</li>
  <li><strong>ترميم وإعادة بناء السيراميدات التالفة بفعل الصبغة:</strong> يعالج الخشونة والتقصف عمقاً.</li>
  <li><strong>ترطيب وتغذية فائقة بأزهار الخزامى العضوية:</strong> يعيد المرونة واللمعان للشعر المصبوغ.</li>
  <li><strong>تركيبة خالية 100% من البارابين والزيوت المعدنية:</strong> مناسبة للشعر المصبوغ والمعالج.</li>
  <li><strong>جودة لاكمي تيكنيا (Lakmé Teknia Spain) الاحترافية:</strong> العناية المركزة بصالونات التجميل.</li>
  <li><strong>عبوة سعة 250 مل بحجم مالي ممتاز:</strong> تكفي لعلاج وترميم اللون لعدة أشهر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بعد غسل الشعر بشامبو لاكمي وايت سيلفر، اعصري الماء الزائد من الشعر.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من ماسك لاكمي البنفسجي ووزعيها بالتساوي على الأطوال والأطراف.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركي الماسك على الشعر لمدة 5-10 دقائق ثم اشطفي جيداً بالماء الدافئ (يُستعمل 1-2 مرة أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الصبغة البنفسجية المباشرة ونظام السيراميد:</strong> يعادلان الاصفرار ويرممان حراشف الكيراتين المتضررة.</li>
  <li><strong>خلاصة زهرة الخزامى العضوية:</strong> تمنح غلافاً مرطباً يحمي اللون من الأكسدة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على شعر الرأس المصبوغ والرمادي.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يملك شعراً مصبوغاً باللون الرمادي أو الأشقر أو الزيتي ويبحث عن ماسك لاكمي وايت سيلفر 250 مل للترميم وتصحيح اللون.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لاكمي (Lakmé Teknia Spain)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / أقنعة وماسكات لاكمي البنفسجية للشعر المصبوغ 250ml</td></tr>
  <tr><th>نوع المنتج</th><td>ماسك بنفسجي معالج ومصحييد للاصفرار ومقوٍ للشعر الأشقر والرمادي (250ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>250 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>الشعر المصبوغ بالرمادي، الأشقر البارد، الزيتي، الفضي والشعر التالف بالصبغة</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم كالحرير، رمادي زيتي بارد، موحد اللون، ناصع الفضة ومحمي من التلف</td></tr>
  <tr><th>الملمس</th><td>كريم بنفسجي داكن غني يمتص بسلاسة بألياف الشعر</td></tr>
  <tr><th>العطر</th><td>عطر الأزهار والفواكه الأسباني الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>صبغة بنفسجية مباشرة، خلاصة زهرة الخزامى العضوية، مجمع السيراميد المصلح</td></tr>
  <tr><th>بلد المنشأ</th><td>إسبانيا (Spain)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Lakme Cosmetics Spain</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد مجمع السيراميد والصبغة البنفسجية في ماسك لاكمي وايت سيلفر (Lakmé White Silver Mask)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج ماسك لاكمي وايت سيلفر مشكلة اصفرار اللون الرمادي والزيتي، تلف وتقصف الشعر المصبوغ، البهتان، وفقدان النعومة.</p>

<h3>لماذا تنجح تركيبة Lakmé Teknia White Silver Hair Mask؟</h3>
<p>لأن الصبغة البنفسجية تحايد الدفء الأصفر بينما يتغلغل مجمع السيراميد ليعيد بناء هيكل الكيراتين المجهد بالصبغة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام 1-2 مرة أسبوعياً بعد الشامبو:</strong> يحافظ على اللون الفضي والنعومة الحريرية.<br>
2. <strong>ترك الماسك 5-10 دقائق تحت منشفة دافئة:</strong> يضاعف امتصاص السيراميدات والتغذية.<br>
3. <strong>الشطف بالماء الفاتر:</strong> يغلق حراشف الشعر ويحفظ بريق اللون.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "أقنعة الشعر البنفسجية تجفف الشعر المصبوغ."<br>
<strong>الحقيقة:</strong> ماسك لاكمي وايت سيلفر مدعم بزهرة الخزامى والسيراميدات لمنح ترطيب وترميم مكثف يزيل الجفاف كلياً.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تعوض السيراميدات الكاتيونية الدهون المفقودة بالصبغة بينما تكسو الصبغة البنفسجية الغلاف الخارجي بنقاء بارد.</p>"""

    faqs = [
        ("ما هو قناع الشعر تيكينيا وايت سيلفر معزز للون الرمادي والزيتي من لاكمي، 250 مل؟", "هو ماسك بنفسجي معالج ومحييد للاصفرار ومقوٍ للشعر الأشقر والرمادي والزيتي المصبوغ من لاكمي تيكنيا (250 مل)."),
        ("ما هي فوائد الصبغة البنفسجية ومجمع السيراميد للشعر المصبوغ؟", "تحايد الانعكاسات الصفراء والبرتقالية، تبرز اللون الرمادي والزيتي البارد، وترمم تقصف وجفاف الصبغة."),
        ("هل يرمم الشعر المصبوغ ويعزز اللون الرمادي والزيتي بدون جفاف؟", "نعم، مثبت سريرياً في تحييد الاصفرار وإعادة بناء السيراميدات وتوفير نعومة حريرية للشعر المصبوغ."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة سعة 250 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعيه على شعر رطب بعد الشامبو، وزعيه على الأطوال والأطراف، اتركيه 5-10 دقائق واشطفي 1-2 مرة أسبوعياً."),
        ("هل هو خالٍ من البارابين والزيوت المعدنية؟", "نعم، 100% خالٍ من البارابين والزيوت المعدنية وآمن للشعر المصبوغ."),
        ("أين صُنع ماسك لاكمي وايت سيلفر؟", "صُنع في إسبانيا بواسطة Lakme Cosmetics Spain."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لاكمي لدى إكليل أبها أصلية 100%."),
        ("ما رائحة ماسك لاكمي وايت سيلفر؟", "عطر الأزهار والفواكه الأسباني الفاخر."),
        ("هل يناسب الشعر المصبوغ بالرمادي والزيتي والأشقر البارد؟", "نعم، ممتاز للشعر المصبوغ بالرمادي، الزيتي، الأشقر البارد، والفضي."),
        ("هل عبوة 250 مل مريحة وموفرة؟", "نعم، عبوة أنيقة موفرة جداً للحفاظ على صبغتك وترميم شعرك لعدة أشهر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل لاكمي تيكنيا الماركة الأولى في صالونات التجميل؟", "نعم، Lakmé Teknia الماركة الإسبانية رقم 1 العالمية الأكثر تفضيلاً بالصالونات."),
        ("كم مرة أسبوعياً؟", "1 إلى 2 مرة أسبوعياً بدلاً من البلسم."),
        ("هل يترك الشعر ناعماً ومفكك التشابك؟", "نعم، يغلف الشعر ويفكك التشابك ليتركه ناعماً كالحرير."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يحافظ على صبغة الشعر الرمادي والزيتي لفترة أطول؟", "نعم، يطيل عمر صبغة الشعر الرمادية والزيتية ويمنع البهتان والاصفرار."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للنساء والرجال أصحاب الشعر الأشقر والرمادي والزيتي."),
        ("هل يناسب الشتاء والصيف؟", "نعم، حماية وترميم لون مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة لمن تصبغ شعرها؟", "نعم، منتج عناية وتصحيح لون فاخر وأساسي لكل شعر مصبوغ."),
        ("هل يعيد المظهر الفضي والزيتي البارد المشرق للشعر؟", "نعم، يمنح الشعر مظهراً فضياً وزيتياً بارداً وناصعاً."),
        ("هل تتوفر منتجات Lakmé Teknia الأخرى؟", "نعم، تتوفر عائلة Lakmé Teknia كاملة لدى إكليل أبها."),
        ("هل يغني عن البلسم التقليدي في يوم الاستخدام؟", "نعم، ماسك مغذي مكثف يغني عن البلسم التقليدي في يوم الاستخدام."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Lakmé Teknia White Silver Hair Mask for Grey and Ash Tones, 250 ml</strong> is an authentic luxury neutralizing and repairing purple hair mask from Lakmé Teknia Spain designed to repair, neutralize brassy yellow undertones, and restore cool ash, grey, and silver tones in blonde, ash, and grey color-treated hair. Built upon pure Direct Violet Pigment, Organic Lotus Flower extract, and the Ceramide Rebuild System.</p>
<p>Lakmé Teknia White Silver Hair Mask tames rough damaged color-treated hair fibers, rebuilds broken ceramides from chemical processing, and shields ash and grey color vibrancy, leaving your hair touchably silky soft, deeply hydrated, brilliantly silver, and restored from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Neutralizes Yellow & Orange Undertones for Grey, Ash & Silver Tones:</strong> Delivers a cool clear finish.</li>
  <li><strong>Ceramide Rebuild System for Damaged Color-Treated Hair:</strong> Deeply repairs roughness and breakage.</li>
  <li><strong>Superior Hydration with Organic Lotus Flower:</strong> Restores natural hair elasticity and shine.</li>
  <li><strong>100% Paraben-Free & Mineral Oil-Free:</strong> Safe for bleached, ash-toned, and processed hair.</li>
  <li><strong>Professional Spanish Lakmé Teknia Salon Quality:</strong> Intensive repair line trusted by stylists.</li>
  <li><strong>Generous 250ml Jar Container:</strong> Excellent size lasting months of color maintenance.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> After washing hair with Lakmé White Silver Shampoo, squeeze out excess water.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of purple mask evenly through hair lengths and ends.</li>
  <li><strong>Step 3:</strong> Leave mask on hair for 5-10 minutes, then rinse thoroughly with warm water (use 1-2 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Direct Violet Pigment & Ceramide Complex:</strong> Neutralize yellow tones and rebuild damaged keratin cuticles.</li>
  <li><strong>Organic Lotus Flower Extract:</strong> Forms a protective hydrating shield preventing color oxidation.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hair application on blonde, ash, and grey hair.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with grey, ash, silver, or blonde color-treated hair seeking Lakmé Teknia White Silver Hair Mask 250ml for repair and tone correction.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lakmé Teknia (Spain)</td></tr>
  <tr><th>Category</th><td>Hair Care / Lakmé Purple Repair Masks 250ml</td></tr>
  <tr><th>Product Type</th><td>Ceramide Rebuild & Violet Toning Repair Mask for Grey & Ash Hair (250ml)</td></tr>
  <tr><th>Volume/Weight</th><td>250 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Grey, Ash, Silver, Bleached & Damaged Color-Treated Hair</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, cool ash-toned silver & damage-repaired hair</td></tr>
  <tr><th>Texture</th><td>Rich deep-purple smooth conditioning cream mask</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh Spanish floral and fruity scent</td></tr>
  <tr><th>Active Ingredients</th><td>Direct Violet Pigment, Organic Lotus Flower Extract, Ceramide Rebuild System</td></tr>
  <tr><th>Country of Origin</th><td>Spain</td></tr>
  <tr><th>Manufacturer</th><td>Lakme Cosmetics Spain</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Ceramide Rebuild Lipid Integration & Violet Ash Toning</h2>

<h3>What problem does this solve?</h3>
<p>Lakmé Teknia White Silver Hair Mask resolves yellowing in ash and grey dyes, hair damage from bleaching, dryness, and roughness.</p>

<h3>Why choose Lakmé Teknia White Silver Mask?</h3>
<p>Direct Violet Pigments offset yellow warmth while the Ceramide Rebuild System repairs broken internal keratin bonds.</p>"""

    en_faqs = [
        ("What is Lakmé Teknia White Silver Hair Mask for Grey and Ash Tones, 250 ml?", "It is a luxury purple repair and toning hair mask from Lakmé Teknia Spain for grey, ash, silver, and blonde color-treated hair (250ml)."),
        ("What are the benefits of Direct Violet Pigment and the Ceramide Rebuild System?", "Neutralize yellow brassiness, restore cold ash and grey tones, and repair damaged color-treated hair cuticles."),
        ("Does it repair damaged color-treated hair and enhance ash/grey tones?", "Yes, clinically proven to repair damaged hair, rebuild ceramides, and enhance cold ash and grey tones."),
        ("What volume is contained in this jar?", "250ml sleek jar container."),
        ("How do I use it correctly?", "Apply to wet hair after shampooing, distribute through lengths, leave on 5-10 minutes and rinse 1-2 times weekly."),
        ("Is it paraben-free and mineral oil-free?", "Yes, 100% free from parabens and mineral oils, safe for color-treated hair."),
        ("Where is Lakmé White Silver Mask manufactured?", "In Spain by Lakme Cosmetics Spain."),
        ("How do I verify authenticity at Ekleel Abha?", "All Lakmé products at Ekleel Abha are 100% original."),
        ("What scent does Lakmé White Silver Mask have?", "Luxurious fresh Spanish floral and fruity fragrance."),
        ("Is it suitable for ash, grey, silver, and blonde hair?", "Yes, excellent for dyed ash, grey, silver, and bleached blonde hair."),
        ("Is the 250ml jar convenient?", "Yes, sleek value jar keeping your hair silver and repaired for months."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Lakmé Teknia a #1 salon brand in Spain?", "Yes, Lakmé Teknia is a premier Spanish professional salon hair care brand."),
        ("How many times weekly?", "1 to 2 times weekly in place of regular conditioner."),
        ("Does it leave hair touchably soft and detangled?", "Yes, coats hair fibers leaving them touchably silky soft and detangled."),
        ("Is the container recyclable?", "Yes."),
        ("Does it prolong ash and grey dye vibrancy?", "Yes, prolongs ash and grey dye vibrancy preventing fading and yellowing."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women with ash or grey hair."),
        ("Is it good for all seasons?", "Yes, ideal color repair and toning for summer and winter care."),
        ("Is it a nice gift for color-treated hair?", "Yes, a premier salon repair essential for color-treated hair routines."),
        ("Does it restore bright cool ash hair appearance?", "Yes, gives hair a vibrant cold ash-toned radiant look."),
        ("Are other Lakmé Teknia products available?", "Yes, the full Lakmé Teknia range is available at Ekleel Abha."),
        ("Does it replace regular conditioner on use days?", "Yes, intensive nourishing mask replaces regular conditioner on application days."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2128",
        "sku": "EK-2128",
        "gtin": "8429421440226",
        "brand": "Lakme",
        "ar": {
            "title": "قناع الشعر تيكينيا وايت سيلفر معزز للون الرمادي والزيتي من لاكمي، 250 مل",
            "meta_title": "ماسك لاكمي وايت سيلفر للون الرمادي والزيتي 250مل | إكليل أبها",
            "meta_description": "اشتري قناع الشعر تيكينيا وايت سيلفر معزز للون الرمادي والزيتي من لاكمي (250 مل). ماسك بنفسجي بالسيراميدات وزهرة الخزامى لترميم وتصحيح اللون الرمادي. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["لاكمي", "ماسك_لاكمي_وايت_سيلفر", "ماسك_الشعر_الرمادي_والزيتي", "تيكينيا_وايت_سيلفر", "إكليل_أبها"]
        },
        "en": {
            "title": "Lakmé Teknia White Silver Hair Mask for Grey and Ash Tones, 250 ml",
            "meta_title": "Lakmé Teknia White Silver Hair Mask 250ml | Ekleel Abha",
            "meta_description": "Buy original Lakmé Teknia White Silver Hair Mask for Grey and Ash Tones (250ml). Ceramide rebuild purple repair mask for ash & grey hair. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["lakme", "lakme_white_silver_mask", "grey_ash_hair_mask", "purple_mask", "ekleel_abha"]
        }
    }


def create_product_2129():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>شامبو بيو ارجان من لاكمي 300مل (Lakme Bio-Argan Shampoo 300ml)</strong> الشامبو المغذي والمصلح العضوي الفاخر بالأرغان الأصيل من لاكمي تيكنيا (Lakme Teknia Bio-Argan Dry Oil Shampoo) المصمم خصيصاً لتنظيف، تغذية، وترميم شعر الرأس الجاف والتالف والمتقصف وإعادة اللمعان الحريري والمرونة لألياف الشعر. يرتكز هذا الشامبو الأصيل (Lakme Bio-Argan 300ml) على زيت الأرجان المغربي العضوي النقي 100% (Organic Argan Oil)، الأحماض الدهنية الأساسية (Omega 6)، وفيتامين E المضاد للأكسدة.</p>
<p>يعمل شامبو لاكمي بيو أرغان على تنظيف الفروة والأطراف بسلاسة، حماية الشعر من الجفاف والتكسر، وتزويده بنعومة حريرية ملموسة، ليترك شعرك ناعماً كالحرير، مرطباً عمقاً، ناصع البريق، ومحمياً من الهيشان من الغسلة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترميم وتغذية فائقة بزيت الأرجان المغربي العضوي 100%:</strong> يعيد الحيوية للشعر الجاف والتالف.</li>
  <li><strong>حماية ألياف الشعر من التكسر والهيشان بأوميغا 6 وفيتامين E:</strong> يمنح الشعر مرونة حريرية.</li>
  <li><strong>تنظيف لطيف خالي 100% من السلفات والبارابين والزيوت المعدنية:</strong> يحافظ على رطوبة الفروة والشعر.</li>
  <li><strong>إعادة اللمعان الطبيعي والنضارة للرموش والخصلات المجهدة:</strong> يمنح مظهرًا صحياً براقاً.</li>
  <li><strong>جودة لاكمي تيكنيا (Lakme Teknia) الإسبانية الشهيرة:</strong> العناية العضوية بصالونات التجميل.</li>
  <li><strong>عبوة سعة 300 مل بمقاس مالي ممتاز:</strong> تكفي للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي شعر الرأس بالماء الدافئ أثناء الغسيل.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من شامبو لاكمي بيو أرغان وكوّني رغوة غنية ودلكي الشعر والفروة برفق.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء الدافئ وتمشيط الشعر بسهولة (يُستعمل 2-3 مرات أسبوعياً أو عند الحاجة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الأرجان العضوي 100% (Organic Argan Oil):</strong> يغذي الشعر بالأحماض الدهنية ويعيد البناء الزيتي.</li>
  <li><strong>أوميغا 6 وفيتامين E:</strong> يحميان الشعر من أكسدة الجفاف ويمنحان لمعاناً ناصعاً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على شعر وفروة الرأس.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يملك شعراً جافاً أو تالفاً أو متقصفاً ويبحث عن شامبو بيو أرغان العضوي من لاكمي 300 مل للتغذية والترميم.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لاكمي (Lakme Teknia Spain)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / شامبوهات لاكمي العضوية بالأرغان 300ml</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو مغذي مصلح خالي من السلفات بزيت الأرجان العضوي 100% (300ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>300 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (خصيصاً الجاف، التالف، المتقصف، والمجهد بالحرارة)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم كالحرير، مرطب 24 ساعة، ناصع اللمعان وخالٍ من الهيشان والتكسر</td></tr>
  <tr><th>الملمس</th><td>سائل ذهبي ناعم ينقلب لرغوة تنظيف كريمية مغذية</td></tr>
  <tr><th>العطر</th><td>عطر الأرغان والعنبر الأسباني الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت الأرجان المغربي العضوي 100%، أوميغا 6، فيتامين E</td></tr>
  <tr><th>بلد المنشأ</th><td>إسبانيا (Spain)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Lakme Cosmetics Spain</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت الأرجان العضوي 100% وأوميغا 6 في شامبو لاكمي بيو أرغان (Lakme Bio-Argan)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج شامبو لاكمي بيو أرغان مشكلة جفاف الشعر، التلف الناتج عن الاستشوار والصبغة، الهيشان، وتكسر الأطراف.</p>

<h3>لماذا تنجح تركيبة Lakme Bio-Argan Shampoo؟</h3>
<p>لأن زيت الأرجان العضوي 100% غني بالأحماض الدهنية وأوميغا 6 التي تنفذ لعمق ألياف الشعر وتغلف الكيراتين.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام 2-3 مرات أسبوعياً بماء دافئ:</strong> ينظف ويغذي الشعر دون تجفيف.<br>
2. <strong>التكميل بـ زيت لاكمي بيو أرغان أو البلسم:</strong> يضاعف مفعول التغذية واللمعان.<br>
3. <strong>التجفيف اللطيف بالمنشفة:</strong> يحافظ على نعومة واستقرار الشعر.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "شامبوهات الزيوت تترك الشعر دهنياً وثقيلاً."<br>
<strong>الحقيقة:</strong> شامبو لاكمي بيو أرغان ينظف بتركيبة خفيفة خالية من السلفات ويمتص فورياً دون أي دهنية ثقيلة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>ترمم أوميغا 6 الأغشية الخلوية لكيراتين الشعر بينما يمنع فيتامين E الأكسدة ويحفظ المرونة.</p>"""

    faqs = [
        ("ما هو شامبو بيو ارجان من لاكمي 300مل؟", "هو شامبو مغذي مصلح خالي من السلفات بزيت الأرجان المغربي العضوي 100% من لاكمي تيكنيا (300 مل)."),
        ("ما هي فوائد زيت الأرجان العضوي 100% وأوميغا 6 للشعر؟", "يغذي ويصلح الشعر الجاف والتالف، يحمي من التكسر والهيشان، ويمنح لمعاناً حريرياً."),
        ("هل يغذي ويرمم الشعر الجاف والتالف بدون سلفات؟", "نعم، مثبت سريرياً في تغذية وترميم الشعر التالف وتوفير نعومة ولمعان خالي من السلفات."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة سعة 300 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الشعر، ضعي كمية، كوّني رغوة، دلكي الفروة والشعر واشطفي بالماء الدافئ 2-3 مرات أسبوعياً."),
        ("هل هو خالٍ من السلفات والبارابين والزيوت المعدنية؟", "نعم، 100% خالٍ من السلفات والبارابين وآمن للشعر المصبوغ والمعالج."),
        ("أين صُنع شامبو لاكمي بيو أرغان؟", "صُنع في إسبانيا بواسطة Lakme Cosmetics Spain."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لاكمي لدى إكليل أبها أصلية 100%."),
        ("ما رائحة شامبو لاكمي بيو أرغان؟", "عطر الأرغان والعنبر الأسباني الفاخر."),
        ("هل يناسب الشعر الجاف والتالف والمتقصف؟", "نعم، ممتاز للشعر الجاف، التالف، المتقصف، والمعالج بالبروتين والصبغة."),
        ("هل عبوة 300 مل مريحة وموفرة؟", "نعم، عبوة أنيقة موفرة جداً للاستخدام اليومي والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل لاكمي تيكنيا الماركة العضوية الأولى في الصالونات؟", "نعم، Lakme Teknia الماركة الإسبانية العضوية رقم 1 الأكثر ثقة بالصالونات."),
        ("كم مرة أسبوعياً؟", "2 إلى 3 مرات أسبوعياً أو حسب الحاجة."),
        ("هل يترك الشعر ناعماً ولامعاً؟", "نعم، ينظف ليترك الشعر ناعماً كالحرير ومفعماً باللمعان الطبيعي."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يقلل هيشان وتكسر أطراف الشعر؟", "نعم، يغلف الشعر بأوميغا 6 ويقلل الهيشان والتكسر بفاعلية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يناسب الشعر المصبوغ والمعالج؟", "نعم، خالي من السلفات ومثالي لحماية الشعر المصبوغ والمعالج."),
        ("هل يناسب الشتاء والصيف؟", "نعم، تغذية وترطيب مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج عناية وتغذية عضوية فاخر وأساسي لكل روتين شعر."),
        ("هل يعيد المظهر الصحي والمشرق للشعر؟", "نعم، يمنح الشعر مظهراً ناعماً ومشرقاً براقاً."),
        ("هل تتوفر منتجات Lakme Bio-Argan الأخرى؟", "نعم، تتوفر عائلة Lakme Bio-Argan كاملة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Lakme Bio-Argan Shampoo 300ml</strong> is an authentic luxury organic nourishing and repairing argan shampoo from Lakme Teknia Spain (Lakme Teknia Bio-Argan Dry Oil Shampoo) designed to clean, nourish, and repair dry, damaged, and brittle hair while restoring silky shine and flexibility to hair fibers. Built upon 100% pure Organic Moroccan Argan Oil, Essential Fatty Acids (Omega 6), and antioxidant Vitamin E.</p>
<p>Lakme Bio-Argan Shampoo smoothly cleanses scalp and ends, shields hair from dryness and breakage, and infuses touchable silky softness, leaving your hair touchably soft, deeply hydrated, brilliantly shiny, and frizz-free from first wash.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Superior Nourishment & Repair with 100% Organic Moroccan Argan Oil:</strong> Revitalizes dry and damaged hair.</li>
  <li><strong>Hair Fiber Protection Against Breakage with Omega 6 & Vitamin E:</strong> Delivers silky flexibility.</li>
  <li><strong>Sulfate-Free, Paraben-Free & Mineral Oil-Free Gentle Formula:</strong> Preserves hair moisture balance.</li>
  <li><strong>Restores Natural Luster & Radiance:</strong> Gives hair a vibrant healthy shine.</li>
  <li><strong>Famous Spanish Salon Lakme Teknia Quality:</strong> Professional organic hair care line.</li>
  <li><strong>Generous 300ml Bottle:</strong> Outstanding value for daily continuous use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet hair thoroughly with warm water during washing.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of Lakme Bio-Argan shampoo, work into a rich lather, and massage scalp and hair gently.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and comb out easily (use 2-3 times weekly or as needed).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>100% Organic Argan Oil:</strong> Nourishes hair with fatty acids restoring natural lipid barriers.</li>
  <li><strong>Omega 6 & Vitamin E:</strong> Protect hair against oxidative dryness and impart brilliant shine.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hair and scalp application.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dry, damaged, or brittle hair seeking Lakme Bio-Argan Shampoo 300ml for organic nourishment and repair.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lakme Teknia (Spain)</td></tr>
  <tr><th>Category</th><td>Hair Care / Lakme Organic Argan Shampoos 300ml</td></tr>
  <tr><th>Product Type</th><td>100% Organic Argan Oil Sulfate-Free Nourishing & Repairing Shampoo (300ml)</td></tr>
  <tr><th>Volume/Weight</th><td>300 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Specifically Dry, Damaged, Brittle & Heat-Stressed Hair)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, brilliantly shiny & frizz-free healthy hair</td></tr>
  <tr><th>Texture</th><td>Rich golden liquid shampoo transforming into a smooth nourishing lather</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh Spanish argan and amber fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>100% Organic Moroccan Argan Oil, Omega 6, Vitamin E</td></tr>
  <tr><th>Country of Origin</th><td>Spain</td></tr>
  <tr><th>Manufacturer</th><td>Lakme Cosmetics Spain</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 100% Organic Argan Oil Omega 6 Lipid Repair & Oxidative Protection</h2>

<h3>What problem does this solve?</h3>
<p>Lakme Bio-Argan Shampoo resolves hair dryness, damage from heat styling and dyes, frizz, and split ends.</p>

<h3>Why choose Lakme Bio-Argan Shampoo?</h3>
<p>100% Organic Argan Oil rich in Omega 6 fatty acids penetrates deep into hair fibers rebuilding damaged cuticle layers.</p>"""

    en_faqs = [
        ("What is Lakme Bio-Argan Shampoo 300ml?", "It is a luxury sulfate-free organic argan nourishing and repairing shampoo from Lakme Teknia Spain (300ml)."),
        ("What are the benefits of 100% Organic Argan Oil and Omega 6?", "Nourish and repair dry damaged hair, protect against breakage and frizz, and deliver a silky shine."),
        ("Does it nourish and repair dry damaged hair without sulfates?", "Yes, clinically proven to nourish and repair damaged hair delivering silky softness without sulfates."),
        ("What volume is contained in this bottle?", "300ml sleek bottle."),
        ("How do I use it correctly?", "Wet hair, apply shampoo, lather, massage scalp gently and rinse with warm water 2-3 times weekly."),
        ("Is it sulfate-free, paraben-free, and mineral oil-free?", "Yes, 100% free from sulfates, parabens, and mineral oils, safe for color-treated hair."),
        ("Where is Lakme Bio-Argan Shampoo manufactured?", "In Spain by Lakme Cosmetics Spain."),
        ("How do I verify authenticity at Ekleel Abha?", "All Lakme products at Ekleel Abha are 100% original."),
        ("What scent does Lakme Bio-Argan Shampoo have?", "Luxurious fresh Spanish argan and amber fragrance."),
        ("Is it suitable for dry, damaged, and brittle hair?", "Yes, excellent for dry, damaged, brittle, and heat-styled hair."),
        ("Is the 300ml bottle convenient?", "Yes, sleek value bottle ideal for daily care and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Lakme Teknia a #1 organic salon brand in Spain?", "Yes, Lakme Teknia is a premier Spanish organic salon hair care brand."),
        ("How many times weekly?", "2 to 3 times weekly or as needed."),
        ("Does it leave hair soft and shiny?", "Yes, cleanses leaving hair touchably silky soft and full of natural shine."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help reduce frizz and split ends?", "Yes, coats hair strands with Omega 6 effectively reducing frizz and split ends."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it safe for color-treated and keratin-treated hair?", "Yes, sulfate-free formula safe for color-treated and processed hair."),
        ("Is it good for all seasons?", "Yes, ideal organic nourishment for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, a premier organic hair care gift for every routine."),
        ("Does it restore healthy shiny hair appearance?", "Yes, gives hair a healthy smooth radiant look."),
        ("Are other Lakme Bio-Argan products available?", "Yes, the full Lakme Bio-Argan range is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2129",
        "sku": "EK-2129",
        "gtin": "8429421430043",
        "brand": "Lakme",
        "ar": {
            "title": "شامبو بيو ارجان من لاكمي300مل",
            "meta_title": "شامبو لاكمي بيو أرغان المغذي 300مل | إكليل أبها",
            "meta_description": "اشتري شامبو بيو أرغان من لاكمي (300 مل). شامبو مغذي مصلح خالي من السلفات بزيت الأرجان المغربي العضوي 100% للشعر الجاف والتالف. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["لاكمي", "شامبو_لاكمي_بيو_أرغان", "شامبو_الأرغان_العضوي", "لاكمي_تيكنيا_أرغان", "إكليل_أبها"]
        },
        "en": {
            "title": "Lakme Bio-Argan Shampoo 300ml",
            "meta_title": "Lakme Bio-Argan Shampoo 300ml | Ekleel Abha",
            "meta_description": "Buy original Lakme Bio-Argan Shampoo (300ml). 100% Organic Moroccan Argan Oil sulfate-free nourishing & repairing shampoo. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["lakme", "lakme_bio_argan", "argan_shampoo", "sulfate_free_shampoo", "ekleel_abha"]
        }
    }


def create_product_2131():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>شامبو وصبغة (اسود طبيعي)للرجال من غارنييه (Garnier Men Shampoo Color - Natural Black)</strong> شامبو الصبغة السريع السهل المطور خصيصاً للرجال من غارنييه (Garnier Men Shampoo Color) لمنح الشعر واللحية صبغة أسود طبيعي 100% وتغطية كاملة للشيب في 5 دقائق فقط دون تلطيخ أو حرقان. يرتكز هذا الشامبو الأصيل (Garnier Men Black 100% Coverage) على خلاصة زيت الزيتون المغذي (Olive Oil)، زيت الأرغان، والتركيبة الخالية 100% من الأمونيا (Ammonia-Free).</p>
<p>يعمل شامبو وصبغة غارنييه للرجال باللون الأسود الطبيعي على تغطية 100% من الشعر الأبيض والرمادي بالرأس واللحية، تزويد الشعر باللمعان والمرونة الطبيعية، وتغذية الفروة، ليترك شعرك ولحيتك بلون أسود طبيعي ناصع، ممتلئين بالنضارة والشباب، ومحميين لـ 5 أسابيع متواصلة من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تغطية كاملة 100% للشيب بالرأس واللحية في 5 دقائق:</strong> صبغة سريعة وسهلة كالغسيل.</li>
  <li><strong>لون أسود طبيعي 100% يدوم حتى 5 أسابيع:</strong> يمنح مظهراً رجالياً أنيقاً وجذاباً.</li>
  <li><strong>تركيبة خالية 100% من الأمونيا (Ammonia-Free):</strong> لا تسبب رائحة نفاذة أو تحسس.</li>
  <li><strong>تغذية وتنعيم للشعر بزيت الزيتون والأرغان:</strong> يمنع خشونة وجفاف الشعر واللحية.</li>
  <li><strong>سهولة التطبيق الذاتي بالمنزل دون الحاجة لصالون:</strong> كيس شامبو صبغة جاهز.</li>
  <li><strong>محتوى مدمج متكامل يتضمن قفازات مخصصة:</strong> تجربة صباغة رجالية نظيفة وسريعة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ارتدي القفازات المرفقة واعصري الشامبو والصبغة من الكيس في اليدين واخلطيهما جيداً.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي الشامبو بالتساوي على الشعر واللحية الجافين ودلكي برفق حتى تتكون رغوة.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركي الصبغة لمدة 5 دقائق فقط ثم اشطفي جيداً بالماء الدافئ (يُستعمل عند الحاجة لتغطية الشيب).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الزيتون وزيت الأرغان:</strong> يغذيان ألياف الشعر واللحية ويمنعان الجفاف.</li>
  <li><strong>الصبغات السوداء الطبيعية الخالية من الأمونيا:</strong> ترتبط بكيراتين الشعر مكملة تغطية الشيب لـ 5 أسابيع.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على شعر الرأس واللحية للرجال؛ اختبري التحسس قبل 48 ساعة.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل رجل يبحث عن شامبو وصبغة باللون الأسود الطبيعي من غارنييه لتغطية الشيب بالرأس واللحية في 5 دقائق.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>غارنييه (Garnier Men L'Oréal)</td></tr>
  <tr><th>الفئة</th><td>العناية بالرجال / شامبوهات وصبغات غارنييه السريعة للرجال</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو وصبغة أسود طبيعي 100% خالي من الأمونيا للشعر واللحية (5 دقائق)</td></tr>
  <tr><th>الحجم/الوزن</th><td>كيس صبغة شامبو مدمج مخصص للرجال + قفازات</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع شعر الرأس واللحية للرجال (خصيصاً الشعر الأبيض والرمادي)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ولحية ناعمين كالحرير، بلون أسود طبيعي 100% وتغطية شيب كاملة لـ 5 أسابيع</td></tr>
  <tr><th>الملمس</th><td>جل صبغة شامبو رغوي سهل التطبيق والخلط باليدين</td></tr>
  <tr><th>العطر</th><td>عطر رجالي طبيعي منعش خالٍ من الأمونيا النفاذة</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت الزيتون، زيت الأرغان، صبغ الأسود الطبيعي خالي الأمونيا</td></tr>
  <tr><th>بلد المنشأ</th><td>الهند / فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>L'Oréal Group</td></tr>
  <tr><th>الفئة العمرية</th><td>الرجال (من 18 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد التركيبة الخالية من الأمونيا وزيت الزيتون في شامبو صبغة غارنييه للرجال (Garnier Men Shampoo Color)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج شامبو صبغة غارنييه للرجال مشكلة الشيب المبكر، الشعر الأبيض بالرأس واللحية، طول وقت الصبغات التقليدية، ورائحة الأمونيا.</p>

<h3>لماذا تنجح تركيبة Garnier Men Shampoo Color Natural Black؟</h3>
<p>لأن التقنية السريعة تدمج الصبغة الشامبوية الخالية من الأمونيا لتلتصق بشيب الرأس واللحية وتغطيه كلياً في 5 دقائق.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على شعر ولحية جافين:</strong> يضمن تثبيت الصبغة السوداء بسرعة.<br>
2. <strong>الانتظار 5 دقائق كاملة:</strong> يضمن تغطية 100% للشيب.<br>
3. <strong>الشطف الجيد بالماء الفاتر:</strong> ينظف بقايا الصبغة تاركاً لوناً طبيعياً.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "شامبو الصبغة يلطخ جلد الوجه واللحية باللون الأسود."<br>
<strong>الحقيقة:</strong> شامبو غارنييه صُمم بتركيبة تنظيف متوازنة تنشطف بالماء دون ترك أي تلطخ على جلد اللحية والوجه.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبت الصبغة المباشرة الخالية من الأمونيا على قشرة كيراتين الشعر واللحية بينما يمنح زيت الزيتون مرونة لـ 5 أسابيع.</p>"""

    faqs = [
        ("ما هو شامبو وصبغة (اسود طبيعي)للرجال من غارنييه؟", "هو شامبو وصبغة سريعة خالية من الأمونيا بزيت الزيتون لتغطية الشيب 100% بالرأس واللحية في 5 دقائق باللون الأسود الطبيعي من غارنييه للرجال."),
        ("ما هي فوائد زيت الزيتون والتركيبة الخالية من الأمونيا للرجال؟", "تغطي الشيب 100% في 5 دقائق، تمنح لوناً أسود طبيعياً يدوم 5 أسابيع، وتغذي شعر الرأس واللحية دون جفاف."),
        ("هل يغطي الشيب 100% في 5 دقائق بالرأس واللحية؟", "نعم، مثبت سريرياً في تغطية 100% للشيب بالرأس واللحية في 5 دقائق باللون الأسود الطبيعي."),
        ("ما هي محتويات العبوة؟", "تأتي بكيس صبغة شامبو مدمج مخصص للرجال + قفازات مخصصة."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ارتدي القفازات، اعصري الشامبو باليدين، وزعي على شعر ولحية جافين، اتركيه 5 دقائق واشطفي بالماء."),
        ("هل هو خالٍ من الأمونيا والروائح النفاذة؟", "نعم، 100% خالٍ من الأمونيا ومصممة برائحة رجالية منعشة."),
        ("أين صُنع شامبو وصبغة غارنييه للرجال؟", "صُنع بواسطة L'Oréal Group العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات غارنييه لدى إكليل أبها أصلية 100%."),
        ("ما لون صبغة غارنييه للرجال؟", "لون أسود طبيعي 100% أنيق (Natural Black)."),
        ("هل يناسب شعر الرأس واللحية معاً؟", "نعم، شامبو صبغة مخصص ومصمم لشعر الرأس واللحية للرجال معاً."),
        ("هل تطبيقه بالمنزل سهل وسريع؟", "نعم، يطبق بسهولة بالمنزل كالغسيل بالشامبو في 5 دقائق فقط."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل غارنييه الماركة الأولى عالمياً في صبغات الرجال؟", "نعم، Garnier Men الماركة رقم 1 العالمية الأكثر شهرة وتفضيلاً في صبغات الرجال."),
        ("كم يدوم اللون الأسود الطبيعي؟", "يدوم حتى 5 أسابيع متواصلة بنفس النضارة."),
        ("هل يلطخ جلد اللحية والوجه؟", "لا، ينشطف بسهولة دون ترك أي تلطيخ على الجلد."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع خشونة شعر اللحية؟", "نعم، بزيت الزيتون والأرغان يمنع خشونة شعر اللحية ويتركه ناعماً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب جميع الرجال؟", "نعم، ممتاز لجميع الرجال الراغبين بتغطية الشيب بالرأس واللحية."),
        ("هل يناسب الشتاء والصيف؟", "نعم، صباغة سريعة مثالية لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة للرجال؟", "نعم، منتج عناية وصباغة سريعة أنيق وعملي جداً للرجال."),
        ("هل يعيد المظهر الشاب والمشرق للرجل؟", "نعم، يمنح الرجل مظهراً ناصع السواد ومفعماً بالشباب والجاذبية."),
        ("هل تتوفر درجات صبغة غارنييه للرجال الأخرى؟", "نعم، تتوفر درجات Garnier Men كاملة لدى إكليل أبها."),
        ("هل ينشطف بالماء فقط؟", "نعم، ينشطف بالماء الدافئ بالكامل."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Garnier Men Shampoo Color (Natural Black)</strong> is an authentic luxury 5-minute quick ammonia-free hair and beard color shampoo from Garnier Men designed to deliver 100% gray hair coverage across head hair and beard in just 5 minutes without staining or stinging. Built upon nourishing Olive Oil, Argan Oil, and a 100% Ammonia-Free formula.</p>
<p>Garnier Men Shampoo Color Natural Black completely covers white and gray hairs on head and beard, imparts natural shine and hair flexibility, and nourishes scalp and beard skin, leaving your hair and beard touchably silky soft, naturally black, and protected for 5 continuous weeks from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Gray Hair & Beard Coverage in 5 Minutes:</strong> Quick and easy color application just like washing.</li>
  <li><strong>100% Natural Black Color Lasting up to 5 Weeks:</strong> Delivers an elegant masculine look.</li>
  <li><strong>100% Ammonia-Free Formula:</strong> Causes zero harsh chemical odor or scalp stinging.</li>
  <li><strong>Nourishment & Softening with Olive & Argan Oils:</strong> Prevents hair and beard stiffness or dryness.</li>
  <li><strong>Easy Self-Application at Home:</strong> Convenient pre-mixed shampoo color sachet.</li>
  <li><strong>Complete Kit Includes Gloves:</strong> Provides a clean and fast masculine coloring experience.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wear included gloves, squeeze shampoo color onto hands, and mix thoroughly.</li>
  <li><strong>Step 2:</strong> Apply evenly over dry head hair and beard, massaging gently to form a lather.</li>
  <li><strong>Step 3:</strong> Leave color on for 5 minutes only, then rinse thoroughly with warm water (use as needed for gray coverage).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Olive Oil & Argan Oil:</strong> Nourish hair and beard fibers preventing post-color dryness.</li>
  <li><strong>Ammonia-Free Natural Black Pigments:</strong> Bind to hair keratin delivering 100% gray coverage lasting 5 weeks.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical head hair and beard application; perform an allergy test 48 hours prior.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Men seeking Garnier Men Shampoo Color Natural Black for 5-minute 100% gray hair and beard coverage.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Garnier Men (L'Oréal)</td></tr>
  <tr><th>Category</th><td>Men's Care / Garnier Men 5-Min Shampoo Colors</td></tr>
  <tr><th>Product Type</th><td>100% Ammonia-Free 5-Minute Head Hair & Beard Natural Black Color Shampoo</td></tr>
  <tr><th>Volume/Weight</th><td>Single Sachet Kit + Gloves</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Men's Head Hair & Beard Types (Specifically White & Gray Hair)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 100% gray-covered, 5-week natural black hair and beard</td></tr>
  <tr><th>Texture</th><td>Rich easy-to-apply foaming shampoo color gel</td></tr>
  <tr><th>Fragrance</th><td>100% Fresh natural masculine fragrance (ammonia-free)</td></tr>
  <tr><th>Active Ingredients</th><td>Olive Oil, Argan Oil, Natural Black Ammonia-Free Dyes</td></tr>
  <tr><th>Country of Origin</th><td>India / France</td></tr>
  <tr><th>Manufacturer</th><td>L'Oréal Group</td></tr>
  <tr><th>Age Group</th><td>Men (Ages 18+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 5-Minute Ammonia-Free Pigment Binding & Olive Oil Conditioning</h2>

<h3>What problem does this solve?</h3>
<p>Garnier Men Shampoo Color Natural Black resolves premature graying, white beard hairs, long salon visits, and harsh ammonia smells.</p>

<h3>Why choose Garnier Men Shampoo Color?</h3>
<p>Fast-acting ammonia-free shampoo dyes bind to hair keratin covering 100% of gray head and beard hairs in 5 minutes.</p>"""

    en_faqs = [
        ("What is Garnier Men Shampoo Color (Natural Black)?", "It is a 5-minute 100% ammonia-free natural black hair and beard color shampoo with Olive Oil from Garnier Men."),
        ("What are the benefits of Olive Oil and the ammonia-free formula?", "Covers 100% gray hair in 5 minutes, delivers a natural black color lasting 5 weeks, and nourishes hair and beard."),
        ("Does it cover 100% gray hair on head and beard in 5 minutes?", "Yes, clinically proven to deliver 100% gray coverage on head hair and beard in 5 minutes."),
        ("What items are included in this sachet?", "Single sachet kit + included protective gloves."),
        ("How do I use it correctly?", "Wear gloves, mix in hands, apply to dry hair and beard, wait 5 minutes and rinse with warm water."),
        ("Is it 100% ammonia-free and harsh-odor free?", "Yes, 100% ammonia-free with a fresh natural masculine fragrance."),
        ("Where is Garnier Men Shampoo Color manufactured?", "By L'Oréal Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All Garnier products at Ekleel Abha are 100% original."),
        ("What color is Garnier Men Shampoo Color?", "100% elegant Natural Black."),
        ("Is it suitable for head hair and beard together?", "Yes, specially formulated for head hair and beard application together."),
        ("Is home application quick and easy?", "Yes, easy self-application at home just like washing hair in 5 minutes."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Garnier Men a #1 global men's hair color brand?", "Yes, Garnier Men is the world's #1 trusted men's hair color brand."),
        ("How long does the natural black color last?", "Lasts up to 5 continuous weeks with vibrant tone."),
        ("Does it stain skin or beard area?", "No, rinses off smoothly without leaving stains on skin."),
        ("Is the sachet recyclable?", "Yes."),
        ("Does it prevent beard stiffness?", "Yes, enriched with Olive and Argan oils preventing beard stiffness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for all men?", "Yes, suitable for all men seeking fast 100% gray coverage."),
        ("Is it good for all seasons?", "Yes, ideal quick color care for summer and winter routines."),
        ("Is it a nice gift for men?", "Yes, an elegant practical quick coloring essential for men."),
        ("Does it restore a youthful masculine appearance?", "Yes, gives men a healthy smooth youthful natural black look."),
        ("Are other Garnier Men color shades available?", "Yes, the full Garnier Men color shade range is available at Ekleel Abha."),
        ("Does it rinse out with water only?", "Yes, rinses out completely with warm water."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2131",
        "sku": "EK-2131",
        "gtin": "8901526591664",
        "brand": "Garnier",
        "ar": {
            "title": "شامبو وصبغة (اسود طبيعي)للرجال من غارنييه",
            "meta_title": "شامبو وصبغة غارنييه أسود طبيعي للرجال | إكليل أبها",
            "meta_description": "اشتري شامبو وصبغة (أسود طبيعي) للرجال من غارنييه. شامبو صبغة سريعة خالية من الأمونيا بزيت الزيتون لتغطية الشيب بالرأس واللحية في 5 دقائق. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["غارنييه_رجال", "شامبو_صبغة_غارنييه", "صبغة_الرجال_أسود_طبيعي", "تغطية_الشيب_5_دقائق", "إكليل_أبها"]
        },
        "en": {
            "title": "Garnier Men Shampoo Color (Natural Black)",
            "meta_title": "Garnier Men Shampoo Color Natural Black | Ekleel Abha",
            "meta_description": "Buy original Garnier Men Shampoo Color (Natural Black). 5-Minute 100% ammonia-free head hair & beard gray coverage shampoo. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["garnier_men", "garnier_shampoo_color", "natural_black_men_dye", "5_min_beard_color", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 81 builders complete")
