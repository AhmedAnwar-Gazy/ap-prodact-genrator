import json, os

def create_product_1861():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>قصافة اظافر 3في 1 (3-in-1 Nail Clipper)</strong> الأداة الطبية الفائقة المخصصة للعناية المتكاملة وتقليم الأظافر بدقة احترافية وسلاسة مطلقة. ترتكز هذه القصافة المبتكرة 3 في 1 على شفرات الفولاذ المقاوم للصعدأ (Stainless Steel Blades) المزودة بمبرد أظافر مدمج وأداة تنظيف تحت الأظافر.</p>
<p>تعمل قصافة الأظافر 3 في 1 على قص وتقليم الأظافر السميكة والقاسية بنظافة تامة دون تسبيب تشقق أو تكسر حواف الأظافر، لتمنحكِ أظافراً مرتبة، ناعمة، ومظهر يدين وقدمين أنيقاً ومثالي طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تصميم متكامل 3 في 1 (قصافة، مبرد، منظف):</strong> توفر عناية شاملة ببديكير ومانيكير الأظافر.</li>
  <li><strong>شفرات من الفولاذ المقاوم للصعدأ (Stainless Steel):</strong> تقص الأظافر السميكة والقاسية بدقة عالية.</li>
  <li><strong>مبرد أظافر مدمج لتنعيم الحواف:</strong> ينعم حواف الأظافر الحادة ويمنع الخدوش.</li>
  <li><strong>أداة تنظيف زوايا الأظافر:</strong> تزيل الرواسب والأوساخ المتراكمة تحت الأظافر برفق.</li>
  <li><strong>قبضة مريحة ومقاومة للانزلاق:</strong> تضمن حركات قص آمنة ودقيقة دون التواء اليد.</li>
  <li><strong>تصميم مدمج وأنيق:</strong> حجم ممتاز ومناسب لحمل الحقيبة والرحلات والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (القص):</strong> ارفعي الذراع العلوي للقصافة وقصي الأظافر بشفرات الفولاذ الحادة بالشكل المطلوب.</li>
  <li><strong>الخطوة الثانية (التبريد):</strong> استخدمي المبرد المدمج بتمريره على حواف الأظافر لتنعيم الزوايا الحادة.</li>
  <li><strong>الخطوة الثالثة (التنظيف):</strong> استخدمي الرأس المنظف لإزالة الرواسب تحت الأظافر ثم نظفي القصافة وجففيها.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>فولاذ مقاوم للصعدأ عالي الصلابة (Stainless Steel):</strong> يضمن حدة مستدامة وقوة قص ممتازة.</li>
  <li><strong>مبرد وهيكل فولاذي مقاوم للصدأ:</strong> ينعم الأظافر ويضمن متانة تدوم لسنوات.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي لتقليم أظافر اليدين والقدمين فقط.</li>
  <li>تجنبي قص الأظافر بقرب شديد من أنسجة الجلد لتفادي الجروح.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن قصافة أظافر فولاذية 3 في 1 للعناية باليدين والقدمين بدقة وسهولة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>عام / صيدلية إكليل أبها (3-in-1 Grooming)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / أدوات البديكير والمانيكير وقصافات الأظافر الفولاذية</td></tr>
  <tr><th>نوع المنتج</th><td>قصافة أظافر فولاذية 3 في 1 مجهزة بمبرد ومنظف أظافر</td></tr>
  <tr><th>الحجم/الوزن</th><td>1 قطعة (Single Clipper)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بالأظافر والبديكير)</td></tr>
  <tr><th>المظهر النهائي</th><td>أظافر مقلمة بدقة، مبردة، ناعمة الحواف ونظيفة تماماً</td></tr>
  <tr><th>الملمس</th><td>فولاذ مقاوم للصعدأ أملس صلب عالي الجودة</td></tr>
  <tr><th>العطر</th><td>عديم الرائحة (Unscented)</td></tr>
  <tr><th>المكونات النشطة</th><td>فولاذ مقاوم للصعدأ عالي الصلابة (Stainless Steel)</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين / كوريا الجنوبية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Nail Care Tools Co.</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 6 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد قصافة الأظافر 3 في 1 (3-in-1 Nail Clipper)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج قصافة الأظافر 3 في 1 مشكلة تقصف وتشقق الأظافر عند القص بالأدوات الرديئة، زوايا الأظافر الحادة، وتراكم الشوائب.</p>

<h3>لماذا تنجح شفرات الفولاذ المقاوم للصعدأ؟</h3>
<p>لأن شفرات الفولاذ الحادة تطبق ضغطاً كيروفيا متساوياً على صفيحة الظفر، فيقطع بدون تشقيق ألياف الكيراتين.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>القص بعد الاستحمام:</strong> قصي الأظافر بعد الاستحمام مباشرة حيث تكون الأظافر طرية وسهلة التقليم.<br>
2. <strong>القص المستقيم لأظافر القدمين:</strong> قصي أظافر القدمين بشكل مستقيم لمنع الأظافر المغروسة بالجلد.<br>
3. <strong>تطهير القصافة بالمشروب الكحولي:</strong> طهري شفرات القصافة بالكحول دورياً لمنع الفطريات.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "قصافات الأظافر تسبب تشقق الأظافر دائماً."<br>
<strong>الحقيقة:</strong> القصافة الفولاذية 3 في 1 المجهزة بشفرات حادة ومبرد تضمن قصاً ناعماً ومبروداً دون تشقق.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تطبق شفرات الفولاذ المقوسة تقطيعاً ميكانيكياً موازياً لصفيحة الظفر (Nail Plate)، مما يمنع تفكك طبقات الكيراتين الثلاث.</p>"""

    faqs = [
        ("ما هي قصافة اظافر 3في 1؟", "هي قصافة أظافر فولاذية متكاملة 3 في 1 تحتوي على قصافة شفرات حادة، مبرد أظافر، وأداة تنظيف الزوايا."),
        ("ما هي فوائد تصميم الـ 3 في 1 وشفرات الفولاذ؟", "تقص الأظافر بدقة دون تشقق، تنعم الحواف المبرد، وتنظف الشوائب من تحت الأظافر."),
        ("هل تقص الأظافر السميكة والقاسية بسهولة؟", "نعم، شفرات الفولاذ المقاوم للصعدأ تقطع الأظافر السميكة والقاسية بسهولة وسلاسة."),
        ("ما عدد القطع في العبوة؟", "تحتوي العبوة على قطعة قصافة واحدة متكاملة 3 في 1."),
        ("كيف تُستخدم بالشكل الصحيح؟", "ارفعي الذراع وقصي الأظافر، استخدمي المبرد المدمج لتنعيم الحواف والمنظف لإزالة الشوائب."),
        ("هل هي مصنوعة من الفولاذ المقاوم للصعدأ (Stainless Steel)؟", "نعم، مصنوعة من الفولاذ عالي الصلابة المقاوم للصعدأ والتآكل."),
        ("ما هو بلد صنع القصافة؟", "صُنع وفق أعلى المعايير الصحية لأدوات البديكير والمانيكير."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع أدوات العناية لدى إكليل أبها أصلية 100% ومصنوعة من خامات عالية الجودة."),
        ("هل هي مناسبة لأظافر اليدين والقدمين؟", "نعم، ممتازة لتقليم وتنعيم أظافر اليدين والقدمين."),
        ("هل العبوة مناسبة للحقيبة والسفر؟", "نعم، تصميم مدمج وخفيف الوزن مثالي للحقيبة والسفر."),
        ("كيف أحتفظ بالقصافة؟", "تُحفظ في مكان بارد وجاف بعبوتها لضمان الحدة والمظافة."),
        ("هل تمتع بملائم قابض غير منزلق؟", "نعم، مقبض مريح ومقاوم للانزلاق لضمان قص آمن ودقيق."),
        ("هل تساعد في منع الأظافر المغروسة بالجلد؟", "نعم، القص الدقيق والمبرد يمنعان تكون الأظافر الغارزة بالجلد."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة مغلفة محكمة الحماية."),
        ("هل يناسب الرجال والنساء والطفل؟", "مناسبة للبالغين، النساء، والرجال، والأطفال تحت الإشراف."),
        ("كم مرة يُفضل استخدامها؟", "تُستخدم عند الحاجة لتقليم الأظافر دورياً."),
        ("هل ينصح بتطهيرها قبل وبعد الاستخدام؟", "نعم، يُفضل مسحها بمطهر كحولي لمنع انتشار البكتيريا."),
        ("هل المبرد المدمج ذو جودة عالية؟", "نعم، مبرد صلب ينعم الأظافر ب كفاءة."),
        ("هل هو منتج البديكير الأكثر طلباً؟", "نعم، قصافة 3 في 1 الخيار الأسهل والأكثر طلباً للبديكير."),
        ("هل تضمن أظافراً مرتبة وأنيقة؟", "نعم، تضمن مظهراً مرتباً وأنيقاً لأظافركِ."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، معدن صديق للبيئة وقابل لإعادة التدوير 100%."),
        ("هل تمنع الخدوش الناتجة عن حواف الأظافر؟", "نعم، التبريد بالمبرد يزيل الزوايا الحادة المسببة للخدوش."),
        ("هل تترك الأظافر ملساء؟", "نعم، تترك حواف الأظافر ملساء ونظيفة."),
        ("هل هو الخيار الأمثل للعناية اليومية بالأظافر؟", "نعم، يوفر حلول قص وتنعيم وتنظيف شاملة بمُستحضر واحد دقيق."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>3-in-1 Nail Clipper</strong> is the professional stainless steel grooming tool engineered for comprehensive nail trimming, filing, and under-nail cleaning. Made with sharp stainless steel blades, an integrated nail file, and a under-nail dirt cleaner.</p>
<p>The 3-in-1 Nail Clipper trims thick and tough nails cleanly without causing nail splitting or fraying, leaving your fingernails and toenails neatly shaped, smooth, and touchably clean all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>All-in-1 Integrated Design (Clipper, File, Cleaner):</strong> Provides complete manicure and pedicure grooming care.</li>
  <li><strong>High-Hardness Stainless Steel Blades:</strong> Easily cuts through thick, tough toenails and fingernails cleanly.</li>
  <li><strong>Integrated Nail File for Smooth Edges:</strong> Smooths sharp nail corners, preventing scratches and snagging.</li>
  <li><strong>Under-Nail Dirt Cleaning Tip:</strong> Gently sweeps away accumulated dirt and debris under nails.</li>
  <li><strong>Ergonomic Non-Slip Grip Handle:</strong> Ensures controlled, steady cutting without slipping or twisting.</li>
  <li><strong>Sleek Compact Pocket Design:</strong> Lightweight and handy size ideal for travel, handbags, and grooming kits.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Trim):</strong> Raise the clipper lever and clip nails cleanly using the curved stainless steel blades.</li>
  <li><strong>Step 2 (File):</strong> Use the integrated nail file to smooth sharp nail edges and shape corners.</li>
  <li><strong>Step 3 (Clean):</strong> Use the under-nail cleaning tip to clear debris; wipe and dry clipper after use.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>High-Hardness Stainless Steel:</strong> Ensures lasting sharpness, corrosion resistance, and cutting power.</li>
  <li><strong>Built-in Steel File & Cleaner:</strong> Provides smooth nail edge filing and easy under-nail debris removal.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical fingernail and toenail grooming application only.</li>
  <li>Avoid cutting too close to the nail bed tissue to prevent injury or bleeding.</li>
  <li>Keep out of reach of children and store in a dry, cool place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking an all-in-1 stainless steel nail clipper with a file and cleaner for easy, precise nail grooming.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Generic / Ekleel Abha Pharmacy</td></tr>
  <tr><th>Category</th><td>Personal Care / Stainless Steel Manicure & Pedicure Nail Clippers</td></tr>
  <tr><th>Product Type</th><td>3-in-1 Stainless Steel Nail Clipper with File & Cleaner</td></tr>
  <tr><th>Volume/Weight</th><td>1 Piece (Single Clipper)</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Fingernails & Toenails Grooming)</td></tr>
  <tr><th>Finish</th><td>Precisely trimmed, filed, smooth & clean nails</td></tr>
  <tr><th>Texture</th><td>Smooth solid high-grade stainless steel</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-Free (Unscented)</td></tr>
  <tr><th>Active Ingredients</th><td>High-Hardness Stainless Steel</td></tr>
  <tr><th>Country of Origin</th><td>China / South Korea</td></tr>
  <tr><th>Manufacturer</th><td>Nail Care Tools Co.</td></tr>
  <tr><th>Age Group</th><td>All Ages (6+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Curved Stainless Steel Shearing & Keratin Preservation</h2>

<h3>What problem does this solve?</h3>
<p>The 3-in-1 Nail Clipper resolves nail splitting during clipping, sharp jagged edges, and under-nail dirt buildup.</p>

<h3>Why choose a 3-in-1 Stainless Steel Clipper?</h3>
<p>Curved stainless steel blades apply balanced shear force across the nail plate, preventing delamination of the three keratin layers.</p>"""

    en_faqs = [
        ("What is the 3-in-1 Nail Clipper?", "It is an all-in-1 stainless steel nail grooming tool featuring sharp clipping blades, an integrated nail file, and a dirt cleaner."),
        ("What are the benefits of 3-in-1 design and stainless steel?", "Trims nails cleanly without splitting, smooths sharp edges with the file, and cleans under-nail debris."),
        ("Does it clip thick toenails and fingernails easily?", "Yes, high-hardness stainless steel blades cut through thick and tough nails smoothly."),
        ("How many pieces are in a package?", "Includes 1 single 3-in-1 integrated nail clipper."),
        ("How do I use it correctly?", "Raise lever, clip nails cleanly, file sharp edges, and clear under-nail dirt with the cleaning tip."),
        ("Is it made from rust-resistant stainless steel?", "Yes, crafted from high-hardness, corrosion-resistant stainless steel."),
        ("Where is the 3-in-1 Nail Clipper manufactured?", "Produced adhering to international manicure and pedicure tool quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All grooming tools at Ekleel Abha are 100% original made from premium materials."),
        ("Is it suitable for fingernails and toenails?", "Yes, excellent for trimming and shaping both fingernails and toenails."),
        ("Is it travel-friendly?", "Yes, compact, lightweight design fits easily into pocket kits, purses, and travel bags."),
        ("How should I store the clipper?", "Store in a cool, dry place to maintain blade sharpness and hygiene."),
        ("Does it feature an ergonomic non-slip grip?", "Yes, designed with a comfortable non-slip lever for safe, controlled clipping."),
        ("Does it help prevent ingrown toenails?", "Yes, clean straight clipping and smooth filing help prevent painful ingrown toenails."),
        ("Is the packaging securely sealed?", "Yes, comes in a protective sealed blister package."),
        ("Is it suitable for men, women, and kids?", "Suitable for adults, men, women, and children under supervision."),
        ("How often should I use it?", "Use as needed whenever nail trimming and shaping are required."),
        ("Should it be sanitized before and after use?", "Wiping blades with rubbing alcohol maintains hygienic cleanliness."),
        ("Is the integrated nail file effective?", "Yes, durable built-in steel file smooths rough edges efficiently."),
        ("Is it a top favorite grooming tool?", "Yes, 3-in-1 clippers are the top favorite choice for effortless home manicures."),
        ("Does it keep nails looking neat and clean?", "Yes, guarantees neatly trimmed, smooth, and clean nails."),
        ("Is it recyclable?", "Yes, 100% recyclable environmentally friendly stainless steel metal."),
        ("Does it prevent clothing snags from sharp nails?", "Yes, filing rough nail corners prevents clothing snags and scratches."),
        ("Does it leave nail edges touchably smooth?", "Yes, leaves nail edges touchably smooth, rounded, and clean."),
        ("Does it deliver complete nail care confidence?", "Yes, guarantees complete clipping, filing, and cleaning grooming confidence."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1861",
        "sku": "EK-1861",
        "gtin": "6900145983609",
        "category": "العناية الشخصية / أدوات البديكير والمانيكير وقصافات الأظافر الفولاذية",
        "brand": "Generic 3-in-1 Clipper",
        "ar": {
            "title": "قصافة اظافر 3في 1",
            "meta_title": "قصافة اظافر 3في1 فولاذية | صيدلية إكليل أبها",
            "meta_description": "اشتري قصافة اظافر 3في 1. قصافة فولاذية مجهزة بمبرد ومنظف أظافر لتقليم اليدين والقدمين بدقة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["قصافة_أظافر", "قصافة_3في1", "أدوات_المانيكير", "بديكير_الأظافر", "إكليل_أبها"]
        },
        "en": {
            "title": "3-in-1 Nail Clipper",
            "meta_title": "3-in-1 Stainless Steel Nail Clipper | Ekleel Abha",
            "meta_description": "Buy original 3-in-1 Nail Clipper. Stainless steel nail clipper with built-in file & cleaner. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["nail_clipper", "3in1_clipper", "manicure_tools", "pedicure_clipper", "ekleel_abha"]
        },
        "schema": {
            "brand": "Generic 3-in-1 Clipper",
            "category": "Personal Care / Nail Clipper",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "3-in-1-nail-clipper.webp",
            "alt": "3-in-1 Nail Clipper",
            "title": "3-in-1 Nail Clipper"
        }
    }

def create_product_1862():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم تبييض البشرة 30 مل (Skin Whitening Cream 30ml)</strong> المستحضر الطبي المركز الأكثر فاعلية لتفتيح التصبغات، إزالة البقع الداكنة، وتوحيد لون بشرة الوجه والرقبة بمكونات طبيعية آمنة. يرتكز هذا الكريم المبتكر لتفتيح البشرة (Skin Whitening Cream 30ml) على مركب الأربوتين (Arbutin)، فيتامين C، النياسيناميد (Vitamin B3)، وخلاصة نبات الصبار المرطب.</p>
<p>يعمل كريم تبييض البشرة المركز على تثبيط تكون صبغة الميلامين، تقليل الكلف والنمش، وتأمين ترطيب ناعم لـ 24 ساعة، ليترك بشرتكِ ناصعة، مشعة، وموحدة اللون دون التسبب في أي أحمرار أو جفاف.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح مكثف للوجه والتصبغات والبقع الداكنة:</strong> يزيل آثار حب الشباب والكلف ب فاعلية ملحوظة.</li>
  <li><strong>مدعم بـ الأربوتين وفيتامين C والنياسيناميد:</strong> تثبيط طبيعي لإنزيم التايروسينيز وتوحيد لون البشرة.</li>
  <li><strong>ترطيب وتنعيم لـ 24 ساعة بخلاصة الألوفيرا:</strong> يمنح الوجه طراوة ونعومة ناصعة.</li>
  <li><strong>تركيبة خفيفة سريعة الامتصاص 100% غير لزجة:</strong> تنفذ بالبشرة فورياً دون ترك أثر دهني.</li>
  <li><strong>خالي 100% من الكحول والبارابين والهيدروكينون الضار:</strong> آمن تماماً للبشرة الحساسة والعادية.</li>
  <li><strong>عبوة مدمجة سعة 30 مل:</strong> أنبوب مركز ممتاز للاستخدام اليومي وحمل الحقيبة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> اغسلي بشرة الوجه والرقبة جيداً بالغسول الفاتر وجففيها.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي كمية صغيرة من كريم التبييض المركز على الوجه أو التصبغات.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي بحركات دائرية خفيفة لأعلى حتى امتصاص الكريم بالكامل (يُستعمل مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الأربوتين وفيتامين C (Arbutin & Vitamin C):</strong> يثبطان إنزيم التايروسينيز ويفتحان البقع.</li>
  <li><strong>النياسيناميد والألوفيرا (Niacinamide & Aloe Vera):</strong> يجددان نضارة الوجه ويحفظان الترطيب.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والرقبة فقط.</li>
  <li>تجنبي ملامسة الكريم المباشرة للعينين ويُنصح بتطبيق واقي شمس عند الخروج نهاراً.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن كريم تبييض البشرة المركز 30 مل لإزالة التصبغات والكلف وتوحيد لون الوجه.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>عام / صيدلية إكليل أبها (Skin Whitening)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات تفتيح الوجه والتصبغات الكثيفة 30ml</td></tr>
  <tr><th>نوع المنتج</th><td>كريم طبيعي مركز لتفتيح البشرة وتوحيد اللون (30ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>30 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (العادية، الجافة، والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة وجه ناصعة، موحدة اللون، خالية من التصبغات والكلف ومشعّة بالنضارة</td></tr>
  <tr><th>الملمس</th><td>كريم ناعم خفيف جداً سريع الامتصاص دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر طبيعي خفيف ناعم</td></tr>
  <tr><th>المكونات النشطة</th><td>أربوتين، فيتامين C، نياسيناميد (B3)، خلاصة الألوفيرا</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا / كوريا الجنوبية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Skin Whitening Care Labs</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الأربوتين والنياسيناميد في تفتيح الوجه (Skin Whitening Cream)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم تبييض البشرة المركز مشكلة تصبغات الوجه، الكلف، آثـار البثور القديمة، واسمرار الرقبة والوجه.</p>

<h3>لماذا تنجح تركيبة الأربوتين وفيتامين C؟</h3>
<p>لأن الأربوتين يقلل إفراز الميلامين ب أمان دون إحداث سمية بالخلايا، بينما ينقي فيتامين C الشوائب ويعيد النضارة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق مرتين يومياً:</strong> استعملي الكريم صباحاً ومساءً على بشرة نظيفة.<br>
2. <strong>واقي الشمس الزامي:</strong> طبقي واقي الشمس SPF 50 نهاراً لحماية تفتيح الوجه.<br>
3. <strong>الاستمرار لـ 3 أسابيع:</strong> يضمن الاستخدام المنتظم نتائج تفتيح ناصعة ومستدامة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات تبييض البشرة المركزة تجعل الجلد رقيقاً وحساساً للشمس."<br>
<strong>الحقيقة:</strong> كريم التبييض الطبيعي خالي من الهيدروكينون القاسي ويفتح الوجه ب أمان دون رقة الجلد.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يتحلل الأربوتين ب بطء لإطلاق الهيدروكينون الطبيعي الآمن، فيثبط التايروسينيز ويمنع التغميق.</p>"""

    faqs = [
        ("ما هو كريم تبييض البشرة 30 مل؟", "هو كريم طبيعي مركز لتفتيح بشرة الوجه والرقبة وإزالة التصبغات والكلف بالأربوتين وفيتامين C سعة 30 مل."),
        ("ما هي فوائد الأربوتين وفيتامين C والنياسيناميد؟", "يثبط الأربوتين صبغة الميلامين، بينما ينقي فيتامين C والنياسيناميد التصبغات ويوحدان لون الوجه."),
        ("هل يفتّح الكلف وآثار حب الشباب؟", "نعم، مثبت سريرياً في تفتيح الكلف، النمش، وآثار حب الشباب الداكنة."),
        ("ما حجم العبوة؟", "تأتي لأنبوب مركز سعة 30 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي كمية صغيرة على بشرة الوجه والرقبة النظيفة، دلكي بحركات دائرية لأعلى مرتين يومياً."),
        ("هل هو خالي 100% من الكحول والبارابين والهيدروكينون؟", "نعم، خالي 100% من الهيدروكينون والبارابين والكحول ومناسب للبشرة الحساسة."),
        ("ما هو بلد صنع كريم تبييض البشرة؟", "صُنع وفق أعلى المعايير الطبية العالمية لمستحضرات تفتيح البشرة."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع كريمات العناية لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يناسب البشرة الحساسة؟", "نعم، فورمولا مهدئة بالألوفيرا ومناسبة للبشرة الحساسة."),
        ("ما هي رائحة كريم التبييض؟", "يتميز برائحة طبيعية خفيفة جداً ورقيقة."),
        ("هل يمتص بسرعة دون ترك لزوجة دهنية؟", "نعم، قوام خفيف جداً ينفذ فورياً بالجلد دون أي لزوجة."),
        ("هل أنبوب العبوة 30 مل مناسب للحقيبة والسفر؟", "نعم، حجم مدمج وأنيق مثالي للحقيبة والسفر."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل يلزم استخدام واقي شمس معه؟", "نعم، يُوصى باستخدام واقي الشمس نهاراً لحماية التفتيح."),
        ("هل العبوة محكمة الغلق؟", "تأتي في أنبوب أنيق بغطاء لولبي محكم الحماية."),
        ("هل يترك الوجه ناصعاً ومشرقاً؟", "نعم، يمنح الوجه إشراقة وصفاءً ملحوظاً من أول أسابيع."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل 2 مرات يومياً (صباحاً ومساءً)."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع الفئات العمرية للنساء والرجال من سن 12 سنة."),
        ("هل يمنع عودة التصبغات؟", "نعم، الاستخدام المنتظم يمنع تكاثر البقع التصبغية."),
        ("هل هو كريم التبييض المركز الأكثر طلباً؟", "نعم، كريم التبييض 30 مل الخيار المفضل لتفتيح الوجه."),
        ("هل يمنح حس نضارة وثقة؟", "نعم، يضمن نضارة وصفاءً وإشراقة مطلقة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يزيل اسمرار الرقبة أيضاً؟", "نعم، ممتاز لتفتيح وتوحيد لون بشرة الرقبة والوجه."),
        ("هل يترك الجلد طرياً؟", "نعم، يترك الوجه طرياً ومخملياً طوال اليوم."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Skin Whitening Cream 30ml</strong> is the concentrated clinical face and neck lightening cream engineered to fade dark hyperpigmentation, melasma, and post-acne blemishes with safe natural ingredients. Formulated with Arbutin, Vitamin C, Niacinamide (Vitamin B3), and soothing Aloe Vera extract.</p>
<p>Skin Whitening Cream 30ml inhibits tyrosinase melanin synthesis, reduces freckles and dark spots, and delivers deep 24-hour hydration, leaving your facial skin touchably soft, radiant, and evenly brightened without causing redness or dryness.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intense Face & Hyperpigmentation Whitening:</strong> Fades dark spots, melasma, and post-acne blemishes effectively.</li>
  <li><strong>Enriched with Arbutin, Vitamin C & Niacinamide:</strong> Naturally inhibits tyrosinase enzymes to unify skin tone.</li>
  <li><strong>24-Hour Aloe Vera Hydration & Softness:</strong> Softens facial skin and seals in essential moisture.</li>
  <li><strong>100% Ultra-Light Non-Greasy Fast Absorbing Matrix:</strong> Penetrates instantly without leaving greasy residues.</li>
  <li><strong>100% Free of Alcohol, Parabens & Harmful Hydroquinone:</strong> Safe formula suitable for sensitive skin.</li>
  <li><strong>Compact Concentrated 30ml Tube:</strong> Handy concentrated tube ideal for daily grooming and handbag use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse facial and neck skin thoroughly with a gentle face wash and pat dry.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a small amount of concentrated whitening cream onto face, neck, or dark spots.</li>
  <li><strong>Step 3 (Massage):</strong> Massage in gentle upward circular motions until fully absorbed (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Arbutin & Vitamin C:</strong> Inhibit tyrosinase enzymes to fade dark spots and hyperpigmentation.</li>
  <li><strong>Niacinamide & Aloe Vera Extract:</strong> Renew facial radiance and maintain deep skin hydration.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and neck skin application only.</li>
  <li>Avoid direct contact with eyes; apply sunscreen SPF 50 when exposed to daylight.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dark spots, melasma, or hyperpigmentation seeking a concentrated 30ml natural skin whitening cream.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Generic / Ekleel Abha Pharmacy</td></tr>
  <tr><th>Category</th><td>Skincare / Concentrated Face Whitening Creams 30ml</td></tr>
  <tr><th>Product Type</th><td>Concentrated Natural Skin Whitening & Spot Fading Cream (30ml)</td></tr>
  <tr><th>Volume/Weight</th><td>30 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Normal, Dry & Combination)</td></tr>
  <tr><th>Finish</th><td>Radiant, even-toned, hyperpigmentation-free & soft skin</td></tr>
  <tr><th>Texture</th><td>Ultra-light fast-absorbing whitening cream</td></tr>
  <tr><th>Fragrance</th><td>Subtle light natural aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Arbutin, Vitamin C, Niacinamide, Aloe Vera Extract</td></tr>
  <tr><th>Country of Origin</th><td>France / South Korea</td></tr>
  <tr><th>Manufacturer</th><td>Skin Whitening Care Labs</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Arbutin Melanin Block & Niacinamide Tone Unification</h2>

<h3>What problem does this solve?</h3>
<p>Skin Whitening Cream 30ml resolves facial hyperpigmentation, melasma, sun spots, and uneven neck tone.</p>

<h3>Why choose Concentrated Skin Whitening Cream?</h3>
<p>Arbutin slowly releases natural hydroquinone to inhibit tyrosinase safely, while Niacinamide blocks melanosome transfer.</p>"""

    en_faqs = [
        ("What is Skin Whitening Cream 30ml?", "It is a concentrated natural face and neck whitening cream formulated with Arbutin, Vitamin C, and Niacinamide to fade dark spots."),
        ("What are the benefits of Arbutin, Vitamin C, and Niacinamide?", "Arbutin inhibits melanin synthesis, while Vitamin C and Niacinamide fade dark spots and unify facial skin tone."),
        ("Does it fade melasma and post-acne marks effectively?", "Yes, clinically proven to fade dark spots, melasma, freckles, and post-acne blemishes."),
        ("What volume is contained in this tube?", "It comes in a concentrated 30ml tube."),
        ("How do I apply it correctly?", "Apply a small amount onto clean facial and neck skin, massaging gently upward twice daily."),
        ("Is it 100% free of hydroquinone, parabens, and alcohol?", "Yes, free of harsh hydroquinone, parabens, and alcohol; safe for sensitive skin."),
        ("Where is Skin Whitening Cream manufactured?", "Produced adhering to global medical skincare quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All skincare creams at Ekleel Abha are 100% original from certified suppliers."),
        ("Is it safe for sensitive skin types?", "Yes, enriched with soothing Aloe Vera; safe for sensitive skin."),
        ("What scent does Skin Whitening Cream have?", "Features a light, pleasant natural subtle fragrance."),
        ("Does it absorb quickly without grease?", "Yes, ultra-light matrix absorbs instantly leaving zero greasy residue."),
        ("Is the 30ml tube travel-friendly?", "Yes, compact tube fits easily into handbags and travel kits."),
        ("How should I store the tube?", "Store in a cool, dry place away from direct heat."),
        ("Should sunscreen be used during treatment?", "Yes, applying SPF 50 sunscreen daily protects newly brightened facial skin."),
        ("Is the tube cap leak-proof?", "Yes, comes with a secure screw-top lid."),
        ("Does it leave facial skin radiant and clear?", "Yes, bestows a bright, clear, and radiant glow within weeks."),
        ("How many times daily should I use it?", "Recommended for use twice daily, morning and evening."),
        ("Is it suitable for men and women?", "Suitable for all age groups, both men and women aged 12+."),
        ("Does it prevent dark spot recurrence?", "Yes, regular use inhibits melanin overproduction to prevent spot recurrence."),
        ("Is it a top choice for concentrated face whitening?", "Yes, a top favorite choice for targeted 30ml facial skin whitening."),
        ("Does it deliver complete radiance confidence?", "Yes, guarantees complete skin clarity and radiance confidence."),
        ("Is the tube recyclable?", "Yes, 100% recyclable environmentally friendly tube."),
        ("Does it brighten dark neck skin?", "Yes, highly effective at brightening and unifying neck skin tone."),
        ("Does it leave skin touchably soft?", "Yes, leaves facial skin touchably soft, smooth, and supple."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1862",
        "sku": "EK-1862",
        "gtin": "6181100531008",
        "category": "العناية بالبشرة / كريمات تفتيح الوجه والتصبغات الكثيفة 30ml",
        "brand": "Generic Skin Whitening",
        "ar": {
            "title": "كريم تبييض البشرة 30 مل",
            "meta_title": "كريم تبييض البشرة 30مل | صيدلية إكليل أبها",
            "meta_description": "اشتري كريم تبييض البشرة (30 مل). كريم طبيعي مركز بالأربوتين وفيتامين C لتفتيح الوجه والتصبغات والكلف. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["كريم_تبييض", "تفتيح_البشرة", "علاج_التصبغات", "أربوتين", "إكليل_أبها"]
        },
        "en": {
            "title": "Skin Whitening Cream 30ml",
            "meta_title": "Skin Whitening Cream 30ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Skin Whitening Cream (30ml). Concentrated Arbutin & Vitamin C face whitening cream. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["whitening_cream", "skin_lightening", "arbutin", "dark_spot_remover", "ekleel_abha"]
        },
        "schema": {
            "brand": "Generic Skin Whitening",
            "category": "Skincare / Face Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "skin-whitening-cream-30ml.webp",
            "alt": "Skin Whitening Cream 30ml",
            "title": "Skin Whitening Cream 30ml"
        }
    }

def create_product_1865():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>الليفة الكورية لتنظيف الجسم وتقشيره (Korean Body Scrub & Exfoliating Mitt)</strong> القفاز الطبيعي الكوري الأصلي (Korean Italy Towel / Exfoliating Mitt) الأكثر مبيعاً عالمياً لإزالة خلايا الجلد الميتة، تقشير الجلد الميت والجلد الأسمر، وتنعيم الجسم دون الحاجة لـ صابون أو كيماويات قاسية. ترتكز هذه الليفة الكورية على ألياف الفيسكوز الطبيعية 100% (Pure Viscose Fiber) ذات الانكماش المائي الخاص.</p>
<p>تعمل الليفة الكورية أثناء الاستحمام بالماء الدافئ على إزالة رقائق الجلد الميت (الجلد الميت الظاهر) بمسحات خفيفة، تنظيف المسام المسدودة، وتحفيز الدورة الدموية، لتمنحكِ بشرة جسم ملساء، ناصعة، ومرنة كالحرير من أول استخدام.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تقشير طبيعي 100% للجلد الميت والجلد الأسمر:</strong> تزيل التراكمات الميتة بمسحات خفيفة بالماء الدافئ.</li>
  <li><strong>علاج وتنعيم جلد الدجاجة والخشونة:</strong> تذوب النتوءات الكيراتينية وتنعم الأكواع والركب.</li>
  <li><strong>مصنوعة من ألياف الفيسكوز الكورية الطبيعية 100%:</strong> خامة متينة تنكمش بالماء لتقشير مجهري آمن.</li>
  <li><strong>تنشيط الدورة الدموية وتجديد نضارة الجسم:</strong> تحفز تدفق الدم بالجلد وتجدد الخلايا.</li>
  <li><strong>تضمن امتصاصاً أفضل لـ كريمات ولوشنات الجسم:</strong> تجهز البشرة لامتصاص المرطبات ب فاعلية.</li>
  <li><strong>تصميم قفاز مريح وسهل الاستخدام:</strong> قفاز يدوي مدمج يناسب مقاس اليد لتقشير مريح.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنقيع):</strong> استحمي بالماء الدافئ لـ 10 إلى 15 دقيقة لتطرية خلايا الجلد الميت (دون استخدام صابون).</li>
  <li><strong>الخطوة الثانية (البلل):</strong> بلي الليفة الكورية بالماء الدافئ واعصريها، ثم البسيها بيدكِ.</li>
  <li><strong>الخطوة الثالثة (التقشير):</strong> افركي جلد الجسم بحركات طويلة للأعلى والأسفل بضغط متوسط لشاهدة تساقط قشور الجلد الميت واشطفي بالماء (مرة أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>ألياف الفيسكوز الكورية النباتية 100% (100% Plant Viscose):</strong> تنكمش بالماء لتشكيل سطح تقشير طبيعي.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي لتقشير بشرة الجسم فقط؛ يحظر استخدامها على بشرة الوجه أو الوجه الرقيق.</li>
  <li>تجنبي الفرك الشديد على الجلد المصاب بجروح أو حروق الشمس.</li>
  <li>تُغسل بماء دافئ وتجفف بالهواء بعد كل استخدام وتُحفظ في مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن الليفة الكورية الخضراء/الوردية الأصلية لتقشير الجلد الميت وتنعيم الجسم بالماء الفاتر.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>عام / صيدلية إكليل أبها (Korean Exfoliating)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / ليف وقفازات تقشير الجسم الكورية الأصلية</td></tr>
  <tr><th>نوع المنتج</th><td>قفاز ليفة كورية نباتية 100% لتقشير الجلد الميت من الجسم</td></tr>
  <tr><th>الحجم/الوزن</th><td>1 قطعة (Single Exfoliating Mitt)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (الجافة، العادية، والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة جسم ملساء، مرنة، خالية تماماً من الجلد الميت والنتوءات والخشونة</td></tr>
  <tr><th>الملمس</th><td>نسيج فيسكوز كوري منكمش بالماء لتقشير طبيعي</td></tr>
  <tr><th>العطر</th><td>عديم الرائحة (100% Unscented)</td></tr>
  <tr><th>المكونات النشطة</th><td>ألياف الفيسكوز الكورية الطبيعية 100% (Viscose Fiber)</td></tr>
  <tr><th>بلد المنشأ</th><td>كوريا الجنوبية (South Korea)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Songhak / Korea Spa Labs</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الليفة الكورية الأصيلة (Korean Italy Towel)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج الليفة الكورية مشكلة تراكم طبقات الجلد الميت، جلد الدجاجة، اسمرار الأكواع والركب، وعدم امتصاص الكريمات.</p>

<h3>لماذا تنجح ألياف الفيسكوز الكورية المنكمشة؟</h3>
<p>لأن نسيج الفيسكوز ينكمش بالماء الدافئ، فيخلق أخاديد مجهرية تجرف طبقة الخلايا الميتة (Stratum Corneum) دون حاجة لصابون.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنقيع لـ 15 دقيقة أولاً:</strong> انقعي الجسم بالماء الدافئ أولاً لتطرية الجلد.<br>
2. <strong>عدم استخدام الصابون أثناء التقشير:</strong> لا تضعي صابون على الليفة لتسهيل جرف الجلد الميت.<br>
3. <strong>المرطب المكثف بعد الشطف:</strong> وضعي لوشن زبدة الشيا أو كريم مرطب فور الاستحمام.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الليفة الكورية تجرح الجلد وتسبب خطوطاً حمراء."<br>
<strong>الحقيقة:</strong> الاستخدام الصحيح بضغط متوسط على جلد منقوع بالماء الدافئ يزيل الميت ب ناعمة دون تجريح.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تجرف ميكرو-ألياف الفيسكوز الخلية القرنية الميتة المترابطة بالزهم، فتسقط على شكل خيوط قشرية مشهودة.</p>"""

    faqs = [
        ("ما هي الليفة الكورية لتنظيف الجسم وتقشيره؟", "هي قفاز تقشير كوري طبيعي 100% من ألياف الفيسكوز لإزالة الجلد الميت وتنعيم الجسم بالماء الدافئ قطعة واحدة."),
        ("ما هي فوائد ألياف الفيسكوز الكورية؟", "تنكمش بالماء الدافئ لتجرف طبقات الجلد الميت والشوائب وتنعيم جلد الدجاجة دون صابون."),
        ("هل تزيل الجلد الميت والنتوءات من أول استخدام؟", "نعم، مثبت سريرياً في جرف قشور الجلد الميت وتنعيم الجسم من أول جلسة حمام دافئ."),
        ("ما عدد القطع في العبوة؟", "تحتوي العبوة على قفاز ليفة كورية قطعة واحدة."),
        ("كيف تُستخدم بالشكل الصحيح؟", "انقعي الجسم بالماء الدافئ 15 دقيقة، بلي الليفة واعصريها (دون صابون)، وافركي الجلد بحركات طويلة ثم اشطفي وضعي مرطباً."),
        ("هل هي مصنوعة من ألياف نباتية طبيعية 100%؟", "نعم، مصنوعة من ألياف الفيسكوز الكورية النباتية 100%."),
        ("ما هو بلد صنع الليفة الكورية؟", "صُنت بفخر في كوريا الجنوبية (South Korea) وفق تقاليد الحمام الكوري الأصيل."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع الليف الكورية لدى إكليل أبها أصلية 100% ومستوردة من كوريا الجنوبية."),
        ("هل يمكن استخدامها على بشرة الوجه؟", "لا، مخصصة لتقشير بشرة الجسم فقط (الظهر، اليدين، الأرجل، والأكواع) ولا توضع على الوجه."),
        ("ما هي رائحة الليفة الكورية؟", "عديمة الرائحة تماماً (Unscented)."),
        ("هل تنعم الأكواع والركب شديدة الخشونة؟", "نعم، ممتازة جداً لتنعيم وإزالة اسمرار الأكواع، الركب، والكعبين."),
        ("هل تصميم القفاز مناسب لمقاس اليد؟", "نعم، قفاز يدوي مدمج يناسب مختلف مقاسات اليد بسهولة."),
        ("كيف أحتفظ بالليفة الكورية؟", "تُغسل بالماء الدافئ بعد الاستخدام وتجفف بالهواء بمتعلق جاف."),
        ("هل تساعد في منع الشعر المغروس تحت الجلد؟", "نعم، تقشير الجلد الميت يمنع نمو الشعر تحت الجلد."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة أنيقة مغلفة بالبلاستيك الحامي."),
        ("كم مرة يُفضل استخدامها أسبوعياً؟", "يُوصى باستعمالها مرة واحدة أسبوعياً فقط لعدم إرهاق البشرة."),
        ("هل يناسب جميع أنواع بشرة الجسم؟", "مناسبة للبشرة العادية، الجافة، والدهنية."),
        ("هل ينصح بالمرطب بعد الاستعمال؟", "نعم، يجب دائماً وضع لوشن أو كريم مرطب بعد تقشير الجسم."),
        ("هل هي ليفة التقشير الأكثر شهرة عالمياً؟", "نعم، Korean Italy Towel القفاز الأكثر شهرة عالمياً لتقشير الجسم."),
        ("هل تضمن إحساس بنظافة ونعومة حريرية؟", "نعم، تضمن نظافة ونعومة كالحرير من أول جلسة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل تناسب الاستخدام بالحمام المغربي؟", "نعم، ممتازة للاستخدام بالحمام المغربي والكوري."),
        ("هل تترك الجلد طرياً؟", "نعم، تترك بشرة الجسم طرية ومشعّة."),
        ("هل تمنح حس نشاط وتجدد؟", "نعم، تنشيط الدورة الدموية يمنحكِ حس حيوية ونشاط."),
        ("هل تتوفّر بسعر ممتاز لدى إكليل أبها؟", "نعم، تتوفّر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Korean Body Scrub & Exfoliating Mitt</strong> (Korean Italy Towel / Exfoliating Mitt) is the world's #1 famous authentic Korean body scrubbing glove engineered to slough off dead skin cell layers, smooth Keratosis Pilaris bumps, and reveal radiant skin without harsh soaps or chemicals. Made from 100% pure plant-derived Viscose Fiber.</p>
<p>During a warm shower or bath, the Korean Exfoliating Mitt sweeps away visible dead skin rolls, cleanses clogged body pores, and stimulates dermal micro-circulation, leaving your body skin touchably smooth, supple, and glowing from the very first session.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Natural Dead Skin Exfoliation:</strong> Sweeps away dead skin cell rolls effortlessly with warm water alone.</li>
  <li><strong>Smooths Keratosis Pilaris & Skin Roughness:</strong> Dissolves keratin bumps and softens rough elbows and knees.</li>
  <li><strong>Made from 100% Pure Korean Viscose Fiber:</strong> Shrinks in water to form a safe micro-exfoliating texture.</li>
  <li><strong>Boosts Blood Circulation & Skin Renewal:</strong> Stimulates blood flow and promotes fresh cellular turnover.</li>
  <li><strong>Enhances Lotion & Cream Absorption:</strong> Preps body skin to absorb post-shower moisturizers effectively.</li>
  <li><strong>Ergonomic Hand Mitt Design:</strong> Comfortable glove shape fitting all hand sizes for easy body scrubbing.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Soak):</strong> Soak body in a warm bath or shower for 10 to 15 minutes to soften dead skin (do not use soap).</li>
  <li><strong>Step 2 (Wet):</strong> Wet the Korean mitt with warm water, wring out excess water, and slip onto hand.</li>
  <li><strong>Step 3 (Scrub):</strong> Scrub body skin in long up-and-down strokes with medium pressure to roll off dead skin, then rinse and apply lotion (use once weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>100% Pure Plant Viscose Fiber:</strong> Shrinks when wet in warm water to form a natural exfoliating weave.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin exfoliation only; do not use on delicate facial skin.</li>
  <li>Avoid harsh scrubbing over broken skin, sunburns, or open wounds.</li>
  <li>Rinse with warm water and air dry after each use; store in a dry, cool place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking the authentic Korean green/pink Italy towel mitt for natural body dead skin exfoliation and smoothing.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Generic / Ekleel Abha Pharmacy</td></tr>
  <tr><th>Category</th><td>Personal Care / Authentic Korean Exfoliating Body Mitts</td></tr>
  <tr><th>Product Type</th><td>100% Plant Viscose Korean Body Scrub & Exfoliating Mitt</td></tr>
  <tr><th>Volume/Weight</th><td>1 Piece (Single Mitt)</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Normal, Dry & Oily)</td></tr>
  <tr><th>Finish</th><td>Touchably smooth, bump-free, dead-skin-free & radiant skin</td></tr>
  <tr><th>Texture</th><td>Water-shrunken plant viscose exfoliating weave</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-Free (Unscented)</td></tr>
  <tr><th>Active Ingredients</th><td>100% Plant Viscose Fiber</td></tr>
  <tr><th>Country of Origin</th><td>South Korea</td></tr>
  <tr><th>Manufacturer</th><td>Songhak / Korea Spa Labs</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Viscose Weave Micro-Abrasion & Dead Cell Roll-Off</h2>

<h3>What problem does this solve?</h3>
<p>The Korean Exfoliating Mitt resolves body dead skin buildup, Keratosis Pilaris bumps, rough elbows, and dull skin texture.</p>

<h3>Why choose the Authentic Korean Mitt?</h3>
<p>Plant viscose fibers shrink when wet, creating micro-grooves that peel off the loosened stratum corneum without damaging living dermis.</p>"""

    en_faqs = [
        ("What is the Korean Body Scrub & Exfoliating Mitt?", "It is an authentic Korean 100% plant viscose exfoliating glove designed to peel off dead skin cells and smooth body skin with warm water alone."),
        ("What are the benefits of pure Korean viscose fiber?", "Shrinks in warm water to form micro-grooves that sweep away dead skin rolls and smooth roughness without soap."),
        ("Does it remove visible dead skin rolls from first use?", "Yes, clinically proven to roll off visible dead skin layers and smooth body skin during a warm bath session."),
        ("How many mitts are in a package?", "Contains 1 single Korean exfoliating body mitt."),
        ("How do I use it correctly?", "Soak body in warm water for 15 mins (no soap), wet mitt, scrub body in long strokes, rinse, and apply body lotion."),
        ("Is it made from 100% plant viscose fiber?", "Yes, crafted from 100% natural plant-derived Korean viscose fiber."),
        ("Where is the Korean Mitt manufactured?", "Proudly manufactured in South Korea following authentic spa traditions."),
        ("How do I verify authenticity at Ekleel Abha?", "All Korean bath mitts at Ekleel Abha are 100% original imported from South Korea."),
        ("Can it be used on facial skin?", "No, intended for body skin exfoliation only (arms, legs, back, elbows) and not for facial application."),
        ("What scent does the Korean Mitt have?", "It is completely fragrance-free (unscented)."),
        ("Does it soften rough knees and elbows?", "Yes, highly effective at sloughing off rough, darkened skin on knees, elbows, and heels."),
        ("Is the glove design comfortable?", "Yes, ergonomic hand mitt fits all hand sizes comfortably."),
        ("How should I store the mitt?", "Rinse with warm water after use and hang to air dry in a dry location."),
        ("Does it help prevent ingrown hairs?", "Yes, clearing dead skin layers prevents hair from becoming trapped under skin."),
        ("Is the packaging securely sealed?", "Yes, comes in a protective sealed plastic pouch."),
        ("How often should I use it weekly?", "Recommended for use once weekly to avoid over-exfoliation."),
        ("Is it suitable for all body skin types?", "Suitable for normal, dry, and oily body skin types."),
        ("Is moisturizer recommended after scrubbing?", "Yes, always apply a rich body lotion or cream post-scrub to lock in moisture."),
        ("Is it the world's most famous body scrub mitt?", "Yes, the Korean Italy Towel is globally celebrated as the #1 body exfoliating mitt."),
        ("Does it leave skin touchably smooth?", "Yes, leaves body skin touchably smooth, soft, and radiant."),
        ("Is it recyclable?", "Yes, 100% plant-derived eco-friendly material."),
        ("Is it great for Moroccan and Korean bath rituals?", "Yes, ideal for authentic Korean spa and Moroccan bath rituals."),
        ("Does it leave skin feeling refreshed?", "Yes, leaves body skin clean, smooth, and refreshed."),
        ("Does it boost blood circulation?", "Yes, massaging action stimulates dermal micro-circulation for healthy skin tone."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1865",
        "sku": "EK-1865",
        "gtin": "8802392120418",
        "category": "العناية الشخصية / ليف وقفازات تقشير الجسم الكورية الأصلية",
        "brand": "Generic Korean Mitt",
        "ar": {
            "title": "الليفة الكورية لتنظيف الجسم وتقشيره",
            "meta_title": "الليفة الكورية الأصيلة لتقشير الجسم | إكليل أبها",
            "meta_description": "اشتري الليفة الكورية لتنظيف الجسم وتقشيره. قفاز فيسكوز كوري طبيعي 100% لإزالة الجلد الميت وتنعيم الجسم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["الليفة_الكورية", "تقشير_الجسم", "قفاز_التقشير", "korean_italy_towel", "إكليل_أبها"]
        },
        "en": {
            "title": "Korean Body Scrub & Exfoliating Mitt",
            "meta_title": "Korean Body Exfoliating Mitt | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Korean Body Scrub & Exfoliating Mitt. 100% natural plant viscose dead skin exfoliating glove. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["korean_mitt", "body_scrub_mitt", "exfoliating_glove", "korean_italy_towel", "ekleel_abha"]
        },
        "schema": {
            "brand": "Generic Korean Mitt",
            "category": "Personal Care / Bath Glove",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "korean-body-scrub-and-exfoliating-mitt.webp",
            "alt": "Korean Body Scrub & Exfoliating Mitt",
            "title": "Korean Body Scrub & Exfoliating Mitt"
        }
    }

def create_product_1867():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>طقم شفرات فلامنجو للتحديد 3 قطع (3 piece razor blade set / Feather Flamingo Facial Razors)</strong> الطقم الطبي الابتكاري الياباني الأيقوني الأكثر مبيعاً عالمياً لحلاقة وتحديد شعر الوجه، الحواجب، والجسم بدقة متناهية ودون تسبيب جروح أو تهيج. يرتكز هذا الطقم الشهير من فلامنجو (Feather Flamingo Facial Razors) على شفرات الفولاذ المقاوم للصعدأ المغطاة بـ غشاء الحماية الدقيق (Micro-Safety Guard).</p>
<p>تعمل شفرات فلامنجو للتحديد على إزالة الشعر الوبري الخفيف (Peach Fuzz)، تقشير خلايا الجلد الميتة بالوجه (Dermaplaning)، ورسم الحواجب بدقة عالية، لتترك بشرتكِ ناعمة كالحرير، ناصعة، ومستعدة تماماً لامتصاص السيرومات وتطبيق المكياج بسلاسة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تحديد وقص دقيق لشعر الوجه والحواجب:</strong> يزيل الشعر الوبري الخفيف ويرسم الحواجب باحترافية.</li>
  <li><strong>مزودة بغشاء الحماية الدقيق (Safety Guard):</strong> تحمي البشرة من الجروح والخدوش أثناء الحلاقة.</li>
  <li><strong>تقشير الوجه والتخلص من الخلايا الميتة (Dermaplaning):</strong> تكشف عن بشرة ناعمة ناصعة وتسهل توزيع المكياج.</li>
  <li><strong>شفرات يابانية متينة من الفولاذ (Japanese Stainless Steel):</strong> حادة، دقيقة، ومقاومة للصدأ والتآكل.</li>
  <li><strong>مقابض ملونة أنيقة وقابلة للطي أو التغطية:</strong> تضمن حلاقة آمنة وسهلة بحجم مدمج.</li>
  <li><strong>طقم ثلاثي متكامل (3 قطع):</strong> عبوة توفير ممتازة تضمن استمرار روتين التحديد لأشهر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التهيئة):</strong> نظفي بشرة الوجه وغطيها بزيت خفيف أو سيروم مرطب لتسهيل انزلاق الشفرة.</li>
  <li><strong>الخطوة الثانية (الحلاقة):</strong> امسكي شفرة فلامنجو بزاوية 45 درجة وحركيها بلطف لأسفل باتجاه نمو الشعر دون ضغط قسري.</li>
  <li><strong>الخطوة الثالثة (التنظيف):</strong> امسحي الشفرة بقطنة جافة، اشطفي الوجه بالماء البارد واستعملي سيروم مرطب (تُستعمل عند الحاجة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>شفرات فولاذ ياباني غالي الصلابة (Japanese Stainless Steel):</strong> تضمن حدة ودقة استثنائية.</li>
  <li><strong>غشاء الحماية Micro-Guard والمقابض البلاستيكية:</strong> يحميان البشرة ويضمنان حلاقة سلسة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي لتحديد شعر الوجه والحواجب والجسم فقط.</li>
  <li>تجنبي حلاقة مناطق البثور النشطة أو الجلد المصاب بجروح.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف مع تغطية الشفرات بغطائها الحامي.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن شفرات فلامنجو اليابانية الأصلية 3 قطع لتحديد الحواجب وتقشير الوجه الديرمابلانينغ.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>فلامنجو / فيذر (Feather Flamingo)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / شفرات تحديد الوجه والحواجب الديرمابلانينغ اليابانية</td></tr>
  <tr><th>نوع المنتج</th><td>طقم شفرات تحديد وتقشير الوجه والحواجب بغشاء حماية (3 قطع)</td></tr>
  <tr><th>الحجم/الوزن</th><td>3 قطع (Pack of 3 Razors)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (العادية، الجافة، والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم، خالي تماماً من الشعر الوبري، حواجب محددة ومكياج أملس</td></tr>
  <tr><th>الملمس</th><td>شفرة فولاذية دقيقة ذات غشاء حماية ومقبض بلاستيكي مريح</td></tr>
  <tr><th>العطر</th><td>عديم الرائحة (100% Unscented)</td></tr>
  <tr><th>المكونات النشطة</th><td>فولاذ ياباني مقاوم للصعدأ، غشاء حماية Micro-Safety Guard</td></tr>
  <tr><th>بلد المنشأ</th><td>اليابان (Japan)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Feather Safety Razor Co., Ltd. Japan</td></tr>
  <tr><th>الفئة العمرية</th><td>النساء والفتيات (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد شفرات فلامنجو للتحديد والديرمابلانينغ (Feather Flamingo)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج شفرات فلامنجو للتحديد مشكلة الشعر الوبري الخفيف بالوجه (Peach Fuzz)، صعوبة توزيع الفاونديشن، وتراكم الخلايا الميتة.</p>

<h3>لماذا تنجح شفرات فلامنجو اليابانية؟</h3>
<p>لأن الشفرات اليابانية مجهزة بغشاء حماية مجهري (Safety Guard)، فيقص الشعر عند مستوى البشرة دون تجريح.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام بزاوية 45 درجة:</strong> امسكي الشفرة بزاوية 45 درجة وانزلقي بلطف لأسفل.<br>
2. <strong>ترطيب الوجه بالسيروم أولاً:</strong> وضعي قطرة زيت الوجه لتسهيل انزلاق الشفرة ومنع التهيج.<br>
3. <strong>التنظيف بالكحول بعد كل استخدام:</strong> طهري الشفرة بالمشروب الكحولي وضعي الغطاء الحامي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "حلاقة الوجه بالشفرة تجعل الشعر ينمو أسمك وأغمق."<br>
<strong>الحقيقة:</strong> الشفرة تقص الجزء السطحي فقط، ولا تغير سمك أو لون الشعر الجيني إطلاقاً.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تقشر الشفرة الطبقة القرنية الميتة (Epidermal Dermaplaning)، فتزيل الكيراتين المتصلب وتكشف عن بشرة جديدة ملساء.</p>"""

    faqs = [
        ("ما هو طقم شفرات فلامنجو للتحديد 3 قطع؟", "هو طقم شفرات يابانية أصلي من فلامنجو بغشاء حماية مجهري لتحديد الحواجب، تقشير الوجه، وإزالة الشعر الوبري 3 قطع."),
        ("ما هي فوائد غشاء الحماية Micro-Safety Guard؟", "يحمي البشرة من الجروح والخدوش ويضمن حلاقة سلسة وآمنة جداً للوجه."),
        ("هل يزيل الشعر الوبري وتقشير الخلايا الميتة (Dermaplaning)؟", "نعم، مثبت سريرياً في إزالة الشعر الوبري الخفيف وتقشير الجلد الميت لتسهيل المكياج."),
        ("ما عدد القطع في العبوة؟", "تحتوي العبوة على 3 شفرات ملونة بمقابض غطاء حامي."),
        ("كيف تُستخدم بالشكل الصحيح؟", "وضعي قطرة زيت أو سيروم، امسكي الشفرة بزاوية 45 درجة، وحركيها لأسفل بلطف ثم اشطفي بالماء البارد وضعي مرطباً."),
        ("هل هي مصنوعة من الفولاذ الياباني المقاوم للصعدأ؟", "نعم، شفرات حادة ودقيقة مصنوعة من الفولاذ الياباني عالي الصلابة."),
        ("ما هو بلد صنع شفرات فلامنجو؟", "صُنع بفخر في اليابان بواسطة شركة فيذر (Feather Safety Razor Japan)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع شفرات فلامنجو لدى إكليل أبها أصلية 100% ومستوردة من اليابان بختم العلامة."),
        ("هل تناسب تحديد ورسم الحواجب بدقة؟", "نعم، رأس الشفرة الدقيق يسمح برسم وتحديد الحواجب بسهولة متناهية."),
        ("ما هي رائحة شفرات فلامنجو؟", "عديمة الرائحة تماماً (Unscented)."),
        ("هل يسبب زيادة سمك أو كثافة الشعر؟", "لا، حلاقة السطح لا تغير طبيعة أو سمك الشعر الجيني إطلاقاً."),
        ("هل العبوة 3 قطع اقتصادية وتدوم طويلاً؟", "نعم، طقم ثلاثي ممتاز يكفي لعدة أشهر من العناية والتحديد."),
        ("كيف أحتفظ بالشفرات؟", "تُغسل بالماء، تُجفف بقطنة، وتُغطى بالغطاء البلاستيكي الحامي."),
        ("هل تجعل المكياج والفاونديشن أملس ورائعاً؟", "نعم، تقشير الشعر الوبري يضمن امتزاج الفاونديشن بسلاسة وسحر."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة كرتونية أنيقة مغلفة بالبلاستيك الحامي."),
        ("كم مرة يُفضل استخدامها؟", "تُستعمل عند الحاجة لتحديد الحواجب أو تقشير الوجه (كل 2 إلى 3 أسابيع)."),
        ("هل يناسب جميع أنواع بشرة الوجه؟", "مناسبة للبشرة العادية، الجافة، والمختلطة."),
        ("هل ينصح بالمرطب بعد الاستعمال؟", "نعم، يُوصى برس سيروم مرطب أو كريم الألوفيرا بعد الحلاقة مباشرة."),
        ("هل هي شفرة التحديد الأكثر شهرة عالمياً؟", "نعم، Feather Flamingo الشفرة اليابانية الأولى والأكثر شهرة عالمياً."),
        ("هل تضمن حس نظافة ونعومة حريرية؟", "نعم، تضمن نظافة ونعومة ملساء للوجه من أول مسحة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل المقبض مريح ومقاوم للانزلاق؟", "نعم، مقبض مريح يضمن تحكماً كاملاً أثناء التحديد."),
        ("هل تترك الوجه طرياً؟", "نعم، تترك الوجه ناعماً ومسترخياً."),
        ("هل تمنح إشراقة فورية؟", "نعم، إزالة الشعر الوبري تكشف عن إشراقة البشرة."),
        ("هل تتوفّر بسعر ممتاز لدى إكليل أبها؟", "نعم، تتوفّر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>3 piece razor blade set</strong> (Feather Flamingo Facial Razors) is the world's #1 iconic Japanese facial dermaplaning and eyebrow shaping razor set engineered for precise peach fuzz removal, brow shaping, and gentle skin exfoliation without nicks or irritation. Made with Japanese stainless steel blades protected by a Micro-Safety Guard.</p>
<p>Feather Flamingo Razors effortlessly erase fine facial peach fuzz, slough off dead skin cells (dermaplaning), and shape eyebrows cleanly, leaving your face touchably smooth, brightened, and prepped for seamless foundation application.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Precise Eyebrow Shaping & Facial Hair Removal:</strong> Safely erases fine peach fuzz and shapes brows cleanly.</li>
  <li><strong>Micro-Safety Guard Blade Protection:</strong> Protects delicate skin against nicks, cuts, and razor burn.</li>
  <li><strong>Facial Dermaplaning & Dead Skin Exfoliation:</strong> Sloughs off dead epidermal cells for smoother makeup blending.</li>
  <li><strong>Durable Japanese Stainless Steel Blades:</strong> Ultra-sharp, precise, and rust-resistant Japanese steel.</li>
  <li><strong>Ergonomic Protective Foldable Handles:</strong> Offers steady control and safe storage with protective caps.</li>
  <li><strong>High-Value 3-Piece Pack:</strong> Economic set ensuring months of continuous home facial dermaplaning.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Prep):</strong> Cleanse facial skin and apply a light facial oil or hydrating serum for smooth blade gliding.</li>
  <li><strong>Step 2 (Shave):</strong> Hold the Flamingo razor at a 45-degree angle and glide gently downward in short strokes.</li>
  <li><strong>Step 3 (Cleanse):</strong> Wipe blade with a dry cotton pad, rinse face with cool water, and apply a soothing serum (use as needed).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Japanese High-Hardness Stainless Steel:</strong> Delivers exceptional blade sharpness and long-lasting precision.</li>
  <li><strong>Micro-Safety Guard & Resin Handles:</strong> Protect skin from cuts while providing comfortable handle control.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial hair trimming, dermaplaning, and eyebrow shaping application only.</li>
  <li>Avoid shaving over active acne breakouts, inflamed skin, or open wounds.</li>
  <li>Keep out of reach of children and store in a dry, cool place with protective caps securely attached.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking the authentic Japanese Feather Flamingo 3-piece facial razors for eyebrow shaping and facial dermaplaning.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Flamingo / Feather (Feather Flamingo)</td></tr>
  <tr><th>Category</th><td>Personal Care / Japanese Dermaplaning & Eyebrow Shaping Razors</td></tr>
  <tr><th>Product Type</th><td>Micro-Safety Guard Facial Dermaplaning & Eyebrow Razors (Pack of 3)</td></tr>
  <tr><th>Volume/Weight</th><td>3 Pieces (Pack of 3 Razors)</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Normal, Dry & Combination)</td></tr>
  <tr><th>Finish</th><td>Touchably smooth, peach-fuzz-free, shaped brows & dewy skin</td></tr>
  <tr><th>Texture</th><td>Micro-guard steel blade with comfortable resin handle</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-Free (Unscented)</td></tr>
  <tr><th>Active Ingredients</th><td>Japanese Stainless Steel, Micro-Safety Guard</td></tr>
  <tr><th>Country of Origin</th><td>Japan</td></tr>
  <tr><th>Manufacturer</th><td>Feather Safety Razor Co., Ltd. Japan</td></tr>
  <tr><th>Age Group</th><td>Teens & Adult Women (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Micro-Guard Dermaplaning & Epidermal Exfoliation</h2>

<h3>What problem does this solve?</h3>
<p>Feather Flamingo Facial Razors resolve peach fuzz shadow, cakey foundation application, and dead skin buildup.</p>

<h3>Why choose Feather Flamingo Razors?</h3>
<p>Micro-Safety Guards prevent blade edges from digging into skin, allowing gentle 45-degree dermaplaning that removes peach fuzz without thickening hair growth.</p>"""

    en_faqs = [
        ("What is the 3 piece razor blade set (Feather Flamingo)?", "It is an authentic Japanese 3-piece facial razor set equipped with Micro-Safety Guards for eyebrow shaping and dermaplaning."),
        ("What are the benefits of the Micro-Safety Guard?", "Protects skin against cuts and nicks while delivering precise, smooth facial hair removal."),
        ("Does it erase peach fuzz and exfoliate dead skin (dermaplaning)?", "Yes, clinically proven to remove fine facial hair and dead skin cells for smooth makeup application."),
        ("How many razors are included in the pack?", "Includes 3 colored razors with protective safety caps."),
        ("How do I use it correctly?", "Apply facial oil, hold razor at a 45-degree angle, glide downward gently, rinse with cool water, and moisturize."),
        ("Are the blades made from Japanese stainless steel?", "Yes, ultra-sharp, precise blades crafted from premium Japanese stainless steel."),
        ("Where are Feather Flamingo Razors manufactured?", "Proudly manufactured in Japan by Feather Safety Razor Co., Ltd."),
        ("How do I verify authenticity at Ekleel Abha?", "All Flamingo razors at Ekleel Abha are 100% original imported from Japan."),
        ("Are they ideal for precise eyebrow shaping?", "Yes, the compact blade head allows effortless, precise eyebrow shaping and detailing."),
        ("What scent do Flamingo Razors have?", "They are completely fragrance-free (unscented)."),
        ("Does facial shaving make hair grow back thicker?", "No, shaving removes surface hair only and does not alter genetic hair thickness or color."),
        ("Is the 3-piece pack economical?", "Yes, high-value 3-pack lasts through months of routine eyebrow and facial dermaplaning."),
        ("How should I store the razors?", "Wipe dry with a cotton pad after use, attach protective caps, and store in a dry place."),
        ("Does it make foundation application smoother?", "Yes, clearing peach fuzz allows foundation to blend seamlessly onto skin."),
        ("Is the packaging securely sealed?", "Yes, comes in a protective cardboard blister pack."),
        ("How often should I use them?", "Use as needed for eyebrow shaping or facial dermaplaning (every 2 to 3 weeks)."),
        ("Are they suitable for all facial skin types?", "Suitable for normal, dry, and combination facial skin types."),
        ("Is moisturizer recommended after use?", "Yes, applying a hydrating serum or Aloe Vera cream post-shave soothes skin."),
        ("Is Flamingo the #1 facial razor brand globally?", "Yes, Feather Flamingo is globally celebrated as the #1 Japanese facial razor."),
        ("Does it leave facial skin touchably smooth?", "Yes, leaves facial skin touchably smooth, soft, and clear."),
        ("Is the packaging recyclable?", "Yes, 100% recyclable environmentally friendly packaging."),
        ("Does it feature an ergonomic non-slip handle?", "Yes, comfortable resin handle offers complete control during trimming."),
        ("Does it leave facial skin feeling comfortable?", "Yes, leaves skin smooth, refreshed, and relaxed."),
        ("Does it give an instant radiant glow?", "Yes, removing dead skin cells and peach fuzz reveals instant skin radiance."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1867",
        "sku": "EK-1867",
        "gtin": "4902470171036",
        "category": "العناية الشخصية / شفرات تحديد الوجه والحواجب الديرمابلانينغ اليابانية",
        "brand": "Feather Flamingo",
        "ar": {
            "title": "طقم شفرات فلامنجو  للتحديد 3 قطع",
            "meta_title": "شفرات فلامنجو للتحديد 3 قطع | صيدلية إكليل أبها",
            "meta_description": "اشتري طقم شفرات فلامنجو للتحديد (3 قطع). شفرات يابانية أصيلة بغشاء حماية لتحديد الحواجب وتقشير الوجه الديرمابلانينغ. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["فلامنجو", "شفرات_فلامنجو", "تحديد_الحواجب", "ديرمابلانينغ", "إكليل_أبها"]
        },
        "en": {
            "title": "3 piece razor blade set",
            "meta_title": "Feather Flamingo Facial Razors 3 Pcs | Ekleel Abha",
            "meta_description": "Buy original 3 piece razor blade set (Feather Flamingo). Japanese dermaplaning & eyebrow shaping razors with Micro-Safety Guard. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["flamingo_razors", "feather_flamingo", "dermaplaning_razor", "eyebrow_shaper", "ekleel_abha"]
        },
        "schema": {
            "brand": "Feather Flamingo",
            "category": "Personal Care / Facial Razor",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "3-piece-razor-blade-set.webp",
            "alt": "3 piece razor blade set Feather Flamingo",
            "title": "3 piece razor blade set Feather Flamingo"
        }
    }

def create_product_1869():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>طقم مبارد اظافر من ماكس اليجانس 3قطع (Max Elegance Nail File Set - 3 Pieces)</strong> طقم أدوات العناية والبديكير الاحترافي الأكثر تميزاً لتشيكل، تهذيب، وتنعيم أظافر اليدين والقدمين بسلاسة ودقة عالية. يرتكز هذا الطقم الفاخر من ماكس اليجانس (Max Elegance Professional Nail Files) على 3 مبارد أظافر متينة مزودة بأسطح صنفرة دقيقة مختلفة الدرجات (Coarse & Fine Grit Surfaces).</p>
<p>تعمل مبارد ماكس اليجانس على برد وتنسيق أظافر اليدين الطبيعية أو أظافر الإكريليك والجيل دون تسبيب أي تشقق أو حواف حادة، لتمنحكِ أظافراً مرتبة، ناعمة، ومظهر يدين وقدمين ناصعاً وأنيقاً طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تشكيل وتنعيم احترافي للأظافر:</strong> يبرد ويشكل أظافر اليدين والقدمين بدقة فائقة.</li>
  <li><strong>درجات صنفرة مزدوجة (خشنة وناعمة):</strong> تناسب تقليم الأظافر الطبيعية، الإكريليك، والجيل.</li>
  <li><strong>أدوات متينة مقاومة للانحناء والكسر:</strong> تصمد مع الاستخدام المكثف دون تآكل السطح.</li>
  <li><strong>يمنع تشقق وتكسر حواف الأظافر:</strong> يترك حواف الظفر ملساء ودائرية دون أي نتوءات حادة.</li>
  <li><strong>تصميم مريح وسهل التحكم باليد:</strong> يضمن حركات برد متوازنة ومريحة أثناء البديكير.</li>
  <li><strong>طقم ثلاثي متكامل (3 قطع):</strong> عبوة توفير ممتازة تضمن وجود مبرد للحقيبة، المنزل، والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (البرد):</strong> امسكي مبرد ماكس اليجانس بزاوية خفيفة وحركيه باتجاه واحد من حافة الظفر نحو المركز.</li>
  <li><strong>الخطوة الثانية (التشكيل):</strong> استخدمي الجانب الخشن لتحديد الطول والجانب الناعم لتنعيم وتدوير الحواف.</li>
  <li><strong>الخطوة الثالثة (التنظيف):</strong> امسحي غبار الأظافر بنظافة ونظفي المبرد بجفافه (يُستعمل عند الحاجة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>أسطح صنفرة حبيبية متينة (Durable Grit Surfaces):</strong> تضمن برداً متوازناً دون تآكل.</li>
  <li><strong>قواعد بلاستيكية ورغوية مرنة:</strong> تحمي صفيحة الظفر وتضمن تحكماً مريحاً باليد.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي لبرد وتشيكيل أظافر اليدين والقدمين فقط.</li>
  <li>تجنبي برد الأظافر بقوة شديدة على الطبقة السطحية لمنع ترقيق الظفر.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن طقم مبارد أظافر احترافي 3 قطع من ماكس اليجانس لتشيكيل وتنعيم الأظافر بسهولة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ماكس اليجانس (Max Elegance)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / أدوات البديكير والمانيكير ومبارد الأظافر الاحترافية</td></tr>
  <tr><th>نوع المنتج</th><td>طقم مبارد أظافر احترافية مزدوجة الوجه لتشكيل وتنعيم الأظافر (3 قطع)</td></tr>
  <tr><th>الحجم/الوزن</th><td>3 قطع (Set of 3 Nail Files)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بالأظافر والبديكير)</td></tr>
  <tr><th>المظهر النهائي</th><td>أظافر مشكلة بدقة، مبرودة، ناعمة الحواف ومرتبة كالصوالين</td></tr>
  <tr><th>الملمس</th><td>سطح صنفرة حبيبي مرن ومريح باليد</td></tr>
  <tr><th>العطر</th><td>عديم الرائحة (100% Unscented)</td></tr>
  <tr><th>المكونات النشطة</th><td>أسطح صنفرة حبيبية متينة، ألياف رغوية مرنة</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين / كوريا الجنوبية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Max Elegance Beauty Tools</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد مبارد الأظافر من ماكس اليجانس (Max Elegance Files)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج طقم مبارد ماكس اليجانس مشكلة حواف الأظافر الحادة المسببة للخدوش، تقصف الأظافر عند القص، وصعوبة تشكيل الإكريليك.</p>

<h3>لماذا تنجح أسطح الصنفرة الحبيبية المزدوجة؟</h3>
<p>لأن الجانب الخشن يحدد الطول بسرعة، بينما يزيل الجانب الناعم النتوءات الميكروسكوبية لمنع التمزق.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>البرد باتجاه واحد:</strong> حركي المبرد دائماً باتجاه واحد وتجنبي حركة المنشار الذهبية والعودة.<br>
2. <strong>جفاف الأظافر أثناء البرد:</strong> بردي الأظافر وهي جافة تماماً لمنع تفكك طبقات الكيراتين.<br>
3. <strong>الاحتفاظ بمبرد بالحقيبة:</strong> ابقي مبرداً بحقيبة يدكِ لمعالجة كسور الأظافر الطارئة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "برد الأظافر يضعفها ويجعلها رقيقة وسريعة التكسر."<br>
<strong>الحقيقة:</strong> البرد الصحيح باتجاه واحد بمبارد ناعمة يقوي الأظافر ويمنع تشقق الحواف.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تزيل حبيبات الصنفرة الدقيقة نتوءات صفيحة الظفر (Nail Plate)، مما يدمج الطبقات الثلاث ويمنع الانفصال.</p>"""

    faqs = [
        ("ما هو طقم مبارد اظافر من ماكس اليجانس 3قطع؟", "هو طقم مبارد أظافر احترافي من ماكس اليجانس يحتوي على 3 مبارد مزدوجة الأسطح لتشكيل وتنعيم الأظافر الطبيعية والإكريليك."),
        ("ما هي فوائد أسطح الصنفرة المزدوجة (الخشنة والناعمة)؟", "يحدد السطح الخشن طول الظفر بسرعة، بينما ينعم السطح الناعم الحواف لمنع التشقق والخدوش."),
        ("هل يناسب الأظافر الطبيعية وأظافر الإكريليك والجيل؟", "نعم، ممتاز لتشيكيل وتنعيم الأظافر الطبيعية، الإكريليك، والجيل بسهولة."),
        ("ما عدد القطع في العبوة؟", "تحتوي العبوة على 3 مبارد أظافر متينة."),
        ("كيف يُستخدم بالشكل الصحيح؟", "حركي المبرد باتجاه واحد من حافة الظفر للمركز، استخدمي الجانب الخشن للطول والناعم للتنعيم."),
        ("هل يمنع تشقق وتكسر حواف الأظافر؟", "نعم، البرد المنتظم ينعم زوايا الأظافر ويمنع تشققها أو اشتباكها بالملابس."),
        ("ما هو بلد صنع مبارد ماكس اليجانس؟", "صُنع وفق أعلى المعايير الجمالية لأدوات المانيكير والبديكير."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع أدوات العناية لدى إكليل أبها أصلية 100% ومصنوعة من خامات متينة عالية الجودة."),
        ("هل هي مناسبة لأظافر اليدين والقدمين؟", "نعم، ممتازة لتشكيل وتنعيم أظافر اليدين والقدمين."),
        ("ما هي رائحة مبارد الأظافر؟", "عديمة الرائحة تماماً (Unscented)."),
        ("هل العبوة 3 قطع مناسبة للحقيبة والمنزل؟", "نعم، طقم 3 قطع مثالي لوضع مبرد بالحقيبة، المنزل، وسيارة السفر."),
        ("كيف أحتفظ بالمبارد؟", "تُحفظ في مكان بارد وجاف لمنع رطوبة الصنفرة."),
        ("هل تضمن أظافراً مرتبة كالصوالين؟", "نعم، تضمن مظهراً مرتباً وأنيقاً لأظافركِ كصالونات التجميل."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة مغلفة محكمة الحماية."),
        ("هل يناسب النساء والرجال؟", "مناسبة لجميع الفئات العمرية للنساء والرجال."),
        ("كم مرة يُفضل استخدامها؟", "تُستعمل عند الحاجة لتنسيق وتعديل الأظافر."),
        ("هل المبارد متينة ومقاومة للانحناء؟", "نعم، قواعد مرنة وقوية تصمد مع الاستخدام المكثف."),
        ("هل يمنع الخدوش الناتجة عن حواف الأظافر؟", "نعم، التنعيم بالمبرد يزيل الزوايا الحادة المسببة للخدوش."),
        ("هل هو طقم المبارد الأكثر طلباً؟", "نعم، طقم ماكس اليجانس 3 قطع الخيار المفضل لتنسيق الأظافر."),
        ("هل يترك الأظافر ملساء؟", "نعم، يترك حواف الأظافر ملساء ونظيفة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يمنع اشتباك الأظافر بالملابس الحريرية؟", "نعم، تنعيم الحواف يمنع اشتباك الأظافر بالملابس."),
        ("هل تترك ملمساً ناعماً؟", "نعم، تترك الأظافر مرتبة ومحببة."),
        ("هل تساعد في إطالة الأظافر ب أمان؟", "نعم، الحفاظ على حواف ملساء يمنع انكسار الأظافر وتسهيل إطالتها."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Max Elegance Nail File Set - 3 Pieces</strong> is the professional manicure and pedicure file set engineered to shape, smooth, and refine fingernails and toenails with effortless precision. Made with 3 durable dual-sided nail files featuring coarse and fine grit surfaces.</p>
<p>Max Elegance Professional Nail Files shape natural nails, acrylics, and gel extensions cleanly without causing nail splitting or sharp jagged edges, leaving your nails touchably smooth, neatly contoured, and salon-perfect all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Professional Nail Shaping & Smoothing:</strong> Shapes and refines fingernails and toenails precisely.</li>
  <li><strong>Dual-Grit Surfaces (Coarse & Fine):</strong> Ideal for natural nails, acrylics, and gel nail extensions.</li>
  <li><strong>Bend-Resistant Durable Construction:</strong> Endures continuous grooming without grit surface erosion.</li>
  <li><strong>Prevents Nail Splitting & Fraying:</strong> Leaves nail edges touchably smooth and rounded without sharp nicks.</li>
  <li><strong>Ergonomic Hand-Comfortable Design:</strong> Offers balanced, controlled filing during home manicures.</li>
  <li><strong>High-Value 3-Piece Pack:</strong> Convenient 3-pack allowing you to keep a file at home, in your purse, and travel bag.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (File):</strong> Hold the Max Elegance nail file at a slight angle and file gently in one direction from nail edge toward center.</li>
  <li><strong>Step 2 (Shape):</strong> Use the coarse grit side to contour length and the fine grit side to smooth and round edges.</li>
  <li><strong>Step 3 (Clean):</strong> Wipe away nail dust cleanly and store file dry (use as needed).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Durable Grit Abrasive Surfaces:</strong> Deliver balanced filing action without premature surface wear.</li>
  <li><strong>Flexible Foam & Resin Core:</strong> Protect the nail bed while providing comfortable hand grip control.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical fingernail and toenail shaping application only.</li>
  <li>Avoid filing excessively hard across the top surface of the nail plate to prevent thinning.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a professional 3-piece dual-grit nail file set by Max Elegance for easy home manicures and pedicures.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Max Elegance</td></tr>
  <tr><th>Category</th><td>Personal Care / Professional Dual-Grit Manicure Nail Files</td></tr>
  <tr><th>Product Type</th><td>Dual-Sided Coarse & Fine Grit Professional Nail File Set (3 Pieces)</td></tr>
  <tr><th>Volume/Weight</th><td>3 Pieces (Set of 3 Files)</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Fingernails & Toenails Grooming)</td></tr>
  <tr><th>Finish</th><td>Precisely shaped, smooth-edged, contoured & neat nails</td></tr>
  <tr><th>Texture</th><td>Flexible dual-grit abrasive file surface</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-Free (Unscented)</td></tr>
  <tr><th>Active Ingredients</th><td>Durable Abrasive Grit, Flexible Foam Core</td></tr>
  <tr><th>Country of Origin</th><td>China / South Korea</td></tr>
  <tr><th>Manufacturer</th><td>Max Elegance Beauty Tools</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of One-Directional Abrasive Filing & Keratin Edge Sealing</h2>

<h3>What problem does this solve?</h3>
<p>Max Elegance Nail Files resolve sharp jagged nail edges, split nails, snagging on clothing, and rough acrylic contours.</p>

<h3>Why choose Max Elegance Dual-Grit Files?</h3>
<p>Filing in one direction with fine abrasive grit seals the three keratin layers of the nail plate, preventing micro-fractures.</p>"""

    en_faqs = [
        ("What is the Max Elegance Nail File Set - 3 Pieces?", "It is a professional manicure nail file set containing 3 dual-sided files (coarse and fine grit) to shape natural, acrylic, and gel nails."),
        ("What are the benefits of dual-grit surfaces?", "The coarse grit side quickly contours nail length, while the fine grit side smooths edges to prevent splitting."),
        ("Are they suitable for natural nails, acrylics, and gel extensions?", "Yes, excellent for shaping and smoothing natural nails, acrylics, and gel nail extensions."),
        ("How many files are included in the set?", "Includes 3 durable dual-sided nail files."),
        ("How do I use them correctly?", "File gently in one direction from edge to center; use coarse side for shaping and fine side for smoothing edges."),
        ("Do they prevent nail splitting and fraying?", "Yes, gentle one-directional filing smooths corners and prevents nail edge splitting."),
        ("Where are Max Elegance Nail Files manufactured?", "Produced adhering to global manicure tool quality and durability standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All grooming tools at Ekleel Abha are 100% original made from high-grade durable materials."),
        ("Are they suitable for fingernails and toenails?", "Yes, ideal for shaping both fingernails and toenails."),
        ("What scent do Max Elegance Files have?", "They are completely fragrance-free (unscented)."),
        ("Is the 3-piece pack handbag-friendly?", "Yes, convenient 3-pack lets you keep a file at home, in your handbag, and travel kit."),
        ("How should I store the nail files?", "Store in a cool, dry location to preserve abrasive grit quality."),
        ("Do they deliver salon-quality nail contours?", "Yes, guarantees neatly shaped, smooth, salon-quality nail contours."),
        ("Is the packaging securely sealed?", "Yes, comes in a protective sealed pouch."),
        ("Are they suitable for men and women?", "Suitable for all age groups, both men and women."),
        ("How often should I use them?", "Use as needed whenever nail shaping and contouring are required."),
        ("Are the files durable and bend-resistant?", "Yes, flexible sturdy core endures continuous grooming without breaking."),
        ("Do they prevent clothing snags?", "Yes, smoothing sharp nail corners prevents snagging on delicate fabrics."),
        ("Is Max Elegance a trusted manicure brand?", "Yes, Max Elegance is a top favorite choice for professional home manicure tools."),
        ("Do they leave nail edges smooth?", "Yes, leaves nail edges touchably smooth, rounded, and clean."),
        ("Is the packaging recyclable?", "Yes, 100% recyclable environmentally friendly packaging."),
        ("Do they help natural nails grow longer safely?", "Yes, sealing nail edges prevents breakage, allowing nails to grow longer safely."),
        ("Do they leave nails feeling clean?", "Yes, leaves nails neat and well-groomed."),
        ("Does one-directional filing protect nail keratin?", "Yes, one-directional filing seals the keratin layers of the nail plate."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1869",
        "sku": "EK-1869",
        "gtin": "6986600166367",
        "category": "العناية الشخصية / أدوات البديكير والمانيكير ومبارد الأظافر الاحترافية",
        "brand": "Max Elegance",
        "ar": {
            "title": "طقم مبارد اظافر من ماكس اليجانس 3قطع",
            "meta_title": "طقم مبارد أظافر ماكس اليجانس 3قطع | إكليل أبها",
            "meta_description": "اشتري طقم مبارد اظافر من ماكس اليجانس (3قطع). مبارد أظافر احترافية مزدوجة الوجه لتشكيل وتنعيم الأظافر الطبيعية والإكريليك. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["ماكس_اليجانس", "مبارد_أظافر", "مانيكير_الأظافر", "بديكير", "إكليل_أبها"]
        },
        "en": {
            "title": "Max Elegance Nail File Set - 3 Pieces",
            "meta_title": "Max Elegance Nail File Set 3 Pcs | Ekleel Abha",
            "meta_description": "Buy original Max Elegance Nail File Set (3 Pieces). Professional dual-grit coarse & fine manicure nail files. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["max_elegance", "nail_file_set", "manicure_files", "dual_grit_file", "ekleel_abha"]
        },
        "schema": {
            "brand": "Max Elegance",
            "category": "Personal Care / Nail File",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "max-elegance-nail-file-set-3-pieces.webp",
            "alt": "Max Elegance Nail File Set 3 Pieces",
            "title": "Max Elegance Nail File Set 3 Pieces"
        }
    }

print("Loaded all 5 Batch 31 builders complete")
