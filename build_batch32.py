import json, os

def create_product_1870():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>شفرات ازالة شعر الوجه 3 شفرات - كاي (Kai Facial Hair Removal Razors - 3 Razors)</strong> المستحضر الطبي الياباني الدقيق الأكثر تميزاً لإزالة شعر الوجه الوبري، تحديد الحواجب بدقة، وتقشير الخلايا الميتة (Dermaplaning) بدقة فائقة ودون تسبيب جروح. ترتكز هذه الشفرات المبتكرة من كاي اليابانية (Kai Pretty Razor / Facial Razors) على شفرات الفولاذ الياباني المقاوم للصعدأ المزودة بـ غشاء الحماية المجهري (Micro-Safety Guard).</p>
<p>تعمل شفرات كاي لإزالة شعر الوجه على حلاقة الشعر الوبري الخفيف، تنظيف المسامات المسدودة بالجلد الميت، وتنعيم البشرة، لتترك وجهكِ ناعماً كالحرير، مشرقاً، وجاهزاً لامتصاص السيرومات وتثبيت المكياج بسلاسة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>إزالة دقيقة لشعر الوجه الوبري وشعر الحواجب:</strong> تحلق شعر الوجه وتحدد الحواجب باحترافية.</li>
  <li><strong>مزودة بغشاء الحماية المجهري (Safety Guard):</strong> تمنع الجروح والخدوش والتهاب البشرة الحساسة.</li>
  <li><strong>تقشير مجهري للجلد الميت (Facial Dermaplaning):</strong> تزيل القشور الميتة وتسهل توزيع الفاونديشن.</li>
  <li><strong>شفرات يابانية من الفولاذ عالي الصلابة:</strong> متينة، حادة، ومقاومة للصدأ والتآكل.</li>
  <li><strong>مقابض أنيقة وقابلة للتغطية بالغطاء الحامي:</strong> تضمن حلاقة مريحة وآمنة وسهولة بالحمل.</li>
  <li><strong>عبوة ثلاثية اقتصادية (3 شفرات):</strong> توفير ممتازة يضمن استمرار روتين التحديد لأشهر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التهيئة):</strong> اغسلي بشرة الوجه وجففيها، ثم وضعي قطرة زيت الوجه أو سيروم مرطب لتسهيل الانزلاق.</li>
  <li><strong>الخطوة الثانية (الحلاقة):</strong> امسكي شفرة كاي بزاوية 45 درجة وانزلقي بلطف لأسفل باتجاه نمو الشعر.</li>
  <li><strong>الخطوة الثالثة (التنظيف):</strong> امسحي الشفرة بقطنة جافة، اشطفي الوجه بالماء البارد وضعي كريم الألوفيرا (عند الحاجة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الفولاذ الياباني المقاوم للصعدأ (Japanese Stainless Steel):</strong> يضمن حدة مستدامة وتقشير دقيق.</li>
  <li><strong>غشاء الحماية المجهري والمقابض الرغوية:</strong> يحميان البشرة ويضمنان حلاقة سلسة.</li>
</ul>

<h2>تحذيرات وااحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي لتحديد شعر الوجه والحواجب فقط.</li>
  <li>تجنبي الحلاقة فوق حب الشباب النشط أو الجلد المصاب بجروح.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف مع تغطية الشفرة بغطائها.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن شفرات كاي اليابانية الأصلية 3 شفرات لتحديد شعر الوجه وتقشير البشرة الديرمابلانينغ.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كاي (Kai Japan)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / شفرات تحديد وتفتيح شعر الوجه والحواجب اليابانية</td></tr>
  <tr><th>نوع المنتج</th><td>شفرات يابانية بغشاء حماية لتحديد وتقشير الوجه والحواجب (3 شفرات)</td></tr>
  <tr><th>الحجم/الوزن</th><td>3 شفرات (Pack of 3 Razors)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (العادية، الجافة، والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه أملس، خالي تماماً من الشعر الوبري، حواجب محددة ومكياج مشرق</td></tr>
  <tr><th>الملمس</th><td>شفرة فولاذية يابانية دقيقة مجهزة بغطاء وسياج حماية</td></tr>
  <tr><th>العطر</th><td>عديم الرائحة (100% Unscented)</td></tr>
  <tr><th>المكونات النشطة</th><td>فولاذ ياباني مقاوم للصعدأ، غشاء حماية Micro-Safety Guard</td></tr>
  <tr><th>بلد المنشأ</th><td>اليابان (Japan)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Kai Corporation Japan</td></tr>
  <tr><th>الفئة العمرية</th><td>النساء والفتيات (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد شفرات كاي اليابانية لإزالة شعر الوجه (Kai Razors)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج شفرات كاي اليابانية مشكلة الشعر الوبري بالوجه، صعوبة امتزاج المكياج، وتراكم القشور الميتة فوق البشرة.</p>

<h3>لماذا تنجح شفرات كاي المجهزة بغشاء الحماية؟</h3>
<p>لأن الشفرات اليابانية تقص الشعر عند فتحة المسام ب زاوية 45 درجة، بينما يحمي غشاء الحماية الجلد من الجروح.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام زيت الوجه قبل الحلاقة:</strong> دلكي قطرة زيت مرطب لسهولة انزلاق الشفرة.<br>
2. <strong>الحلاقة بزاوية 45 درجة:</strong> امسكي الشفرة بزاوية مائلة ولا تضغطي بقوة.<br>
3. <strong>التطهير بالكحول:</strong> مسح الشفرة بالكحول بعد الاستعمال يحافظ على تعقيمها.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "شفرات كاي تسبب زيادة نمو وجفاف شعر الوجه."<br>
<strong>الحقيقة:</strong> الحلاقة السطحية لا تؤثر على بصيلة الشعر الجينية، وتترك البشرة ناعمة ومشرقة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تزيل الشفرة حطام خلايا طبقة الـ Stratum Corneum، مما ينشط الامتصاص الخلوي للسيرومات العلاجية.</p>"""

    faqs = [
        ("ما هي شفرات ازالة شعر الوجه 3 شفرات - كاي؟", "هي شفرات يابانية أصلية من كاي بغشاء حماية مجهري لإزالة الشعر الوبري بالوجه وتحديد الحواجب 3 شفرات."),
        ("ما هي فوائد غشاء الحماية Micro-Safety Guard؟", "يمنع الجروح والخدوش ويضمن حلاقة سلسة وآمنة لبشرة الوجه الحساسة."),
        ("هل يزيل الشعر الوبري وتقشير البشرة (Dermaplaning)؟", "نعم، مثبت سريرياً في إزالة الشعر الوبري الخفيف وتقشير خلايا الجلد الميتة."),
        ("ما عدد الشفرات في العبوة؟", "تحتوي العبوة على 3 شفرات يابانية مجهزة بأغطية حامية."),
        ("كيف تُستخدم بالشكل الصحيح؟", "ضعي زيت الوجه، امسكي الشفرة بزاوية 45 درجة، وانزلقي بلطف لأسفل ثم اشطفي بالماء وضعي مرطباً."),
        ("هل هي مصنوعة من الفولاذ الياباني المقاوم للصعدأ؟", "نعم، مصنوعة من الفولاذ الياباني عالي الصلابة عالي الجودة."),
        ("ما هو بلد صنع شفرات كاي؟", "صُنع بفخر في اليابان بواسطة شركة كاي (Kai Corporation Japan)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع شفرات كاي لدى إكليل أبها أصلية 100% ومستوردة من اليابان."),
        ("هل تناسب رسم وتحديد الحواجب بدقة؟", "نعم، تصميم الشفرة الدقيق يسمح برسم وتحديد الحواجب بسهولة."),
        ("ما هي رائحة شفرات كاي؟", "عديمة الرائحة تماماً (Unscented)."),
        ("هل تسبب زيادة سمك أو غمق شعر الوجه؟", "لا، الحلاقة السطحية لا تغير سمك أو لون الشعر الجيني إطلاقاً."),
        ("هل العبوة 3 شفرات اقتصادية وتدوم طويلاً؟", "نعم، طقم ثلاثي ممتاز يكفي لعدة أشهر من العناية بالتحديد."),
        ("كيف أحتفظ بالشفرات؟", "تُغسل بالماء، تُجفف بقطنة، وتُغطى بالغطاء البلاستيكي الحامي."),
        ("هل تساعد في تثبيت المكياج بسلاسة؟", "نعم، تقشير الوجه وإزالة الشعر يضمن امتزاج المكياج بسلاسة وسحر."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة مغلفة محكمة الحماية."),
        ("كم مرة يُفضل استخدامها؟", "تُستعمل عند الحاجة لتحديد الحواجب أو تقشير الوجه (كل 2 إلى 3 أسابيع)."),
        ("هل يناسب جميع أنواع بشرة الوجه؟", "مناسبة للبشرة العادية، الجافة، والمختلطة."),
        ("هل ينصح بالمرطب بعد الاستعمال؟", "نعم، يُوصى بوضع سيروم مرطب أو كريم الألوفيرا بعد الحلاقة."),
        ("هل هي من شفرات التحديد الأكثر شهرة يابانياً؟", "نعم، شفرات كاي اليابانية الخيار الأفضل والأكثر شهرة عالمياً."),
        ("هل تضمن حس نظافة ونعومة حريرية؟", "نعم، تضمن نظافة ونعومة ملساء من أول استخدام."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل المقبض مريح ومقاوم للانزلاق؟", "نعم، مقبض مريح يضمن تحكماً كاملاً أثناء الحلاقة."),
        ("هل تترك الوجه طرياً؟", "نعم، تترك الوجه ناعماً ومسترخياً."),
        ("هل تمنح إشراقة فورية؟", "نعم، إزالة الشعر الوبري تكشف عن صفاء وإشراقة الوجه."),
        ("هل تتوفّر بسعر ممتاز لدى إكليل أبها؟", "نعم، تتوفّر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Kai Facial Hair Removal Razors - 3 Razors</strong> is the authentic Japanese precision facial razor set engineered to remove fine peach fuzz, shape eyebrows, and perform gentle facial dermaplaning without nicks or scratches. Formulated by Kai Japan, it features Japanese stainless steel blades protected by a Micro-Safety Guard.</p>
<p>Kai Facial Razors erase unwanted facial fuzz, clear dead skin cell buildup from clogged pores, and smooth skin texture, leaving your face touchably soft, radiant, and perfectly prepared for smooth makeup blending all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Precise Facial Peach Fuzz & Eyebrow Shaping:</strong> Safely removes fine facial hair and shapes brows.</li>
  <li><strong>Micro-Safety Guard Blade Defense:</strong> Shields delicate skin against nicks, cuts, and razor burn.</li>
  <li><strong>Facial Dermaplaning & Exfoliation:</strong> Sloughs off dead skin cells for effortless foundation blending.</li>
  <li><strong>High-Hardness Japanese Stainless Steel:</strong> Durable, ultra-sharp, rust-resistant Japanese blades.</li>
  <li><strong>Protective Cap Ergonomic Handles:</strong> Offers controlled handling and safe travel storage.</li>
  <li><strong>High-Value 3-Razor Pack:</strong> Economic set ensuring months of continuous home facial grooming.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Prep):</strong> Cleanse facial skin and apply a light facial oil or hydrating serum for smooth gliding.</li>
  <li><strong>Step 2 (Shave):</strong> Hold the Kai razor at a 45-degree angle and glide gently downward in short strokes.</li>
  <li><strong>Step 3 (Cleanse):</strong> Wipe blade with a dry cotton pad, rinse face with cool water, and moisturize (use as needed).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Japanese High-Hardness Stainless Steel:</strong> Provides lasting blade sharpness and accurate trimming.</li>
  <li><strong>Micro-Safety Guard & Resin Handles:</strong> Protect skin against razor nicks while ensuring comfortable handling.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial hair trimming, dermaplaning, and eyebrow shaping application only.</li>
  <li>Avoid shaving over active acne breakouts, inflamed skin, or open wounds.</li>
  <li>Keep out of reach of children and store in a cool, dry place with protective caps securely attached.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking authentic Japanese Kai 3-piece facial razors for precise eyebrow shaping and facial dermaplaning.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Kai (Kai Japan)</td></tr>
  <tr><th>Category</th><td>Personal Care / Japanese Dermaplaning & Eyebrow Shaping Razors</td></tr>
  <tr><th>Product Type</th><td>Micro-Safety Guard Facial Dermaplaning & Eyebrow Razors (Pack of 3)</td></tr>
  <tr><th>Volume/Weight</th><td>3 Razors (Pack of 3 Razors)</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Normal, Dry & Combination)</td></tr>
  <tr><th>Finish</th><td>Touchably smooth, peach-fuzz-free, shaped brows & dewy skin</td></tr>
  <tr><th>Texture</th><td>Micro-guard steel blade with comfortable resin handle</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-Free (Unscented)</td></tr>
  <tr><th>Active Ingredients</th><td>Japanese Stainless Steel, Micro-Safety Guard</td></tr>
  <tr><th>Country of Origin</th><td>Japan</td></tr>
  <tr><th>Manufacturer</th><td>Kai Corporation Japan</td></tr>
  <tr><th>Age Group</th><td>Teens & Adult Women (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Japanese Micro-Guard Shearing & Epidermal Dermaplaning</h2>

<h3>What problem does this solve?</h3>
<p>Kai Facial Razors resolve peach fuzz shadow, cakey foundation application, and dead epidermal skin buildup.</p>

<h3>Why choose Kai Japanese Razors?</h3>
<p>Micro-Safety Guards prevent blade edges from digging into skin, allowing gentle 45-degree dermaplaning that removes peach fuzz safely.</p>"""

    en_faqs = [
        ("What are Kai Facial Hair Removal Razors - 3 Razors?", "They are authentic Japanese 3-piece facial razors equipped with Micro-Safety Guards for eyebrow shaping and dermaplaning."),
        ("What are the benefits of the Micro-Safety Guard?", "Protects skin against cuts and nicks while delivering smooth facial hair removal."),
        ("Does it erase peach fuzz and exfoliate dead skin?", "Yes, clinically proven to remove fine facial peach fuzz and exfoliate dead skin cells for smooth makeup blending."),
        ("How many razors are included in the pack?", "Includes 3 razors with protective safety caps."),
        ("How do I use it correctly?", "Apply facial oil, hold razor at a 45-degree angle, glide downward gently, rinse with cool water, and moisturize."),
        ("Are the blades made from Japanese stainless steel?", "Yes, ultra-sharp, precise blades crafted from premium Japanese stainless steel."),
        ("Where are Kai Razors manufactured?", "Proudly manufactured in Japan by Kai Corporation Japan."),
        ("How do I verify authenticity at Ekleel Abha?", "All Kai razors at Ekleel Abha are 100% original imported from Japan."),
        ("Are they ideal for precise eyebrow shaping?", "Yes, compact blade head allows effortless, precise eyebrow shaping and detailing."),
        ("What scent do Kai Razors have?", "They are completely fragrance-free (unscented)."),
        ("Does facial shaving make hair grow back thicker?", "No, shaving removes surface hair only and does not alter genetic hair thickness or color."),
        ("Is the 3-razor pack economical?", "Yes, high-value 3-pack lasts through months of routine eyebrow and facial dermaplaning."),
        ("How should I store the razors?", "Wipe dry with a cotton pad after use, attach protective caps, and store in a dry place."),
        ("Does it make foundation application smoother?", "Yes, clearing peach fuzz allows foundation to blend seamlessly onto skin."),
        ("Is the packaging securely sealed?", "Yes, comes in a protective sealed blister pack."),
        ("How often should I use them?", "Use as needed for eyebrow shaping or facial dermaplaning (every 2 to 3 weeks)."),
        ("Are they suitable for all facial skin types?", "Suitable for normal, dry, and combination facial skin types."),
        ("Is moisturizer recommended after use?", "Yes, applying a hydrating serum or Aloe Vera cream post-shave soothes skin."),
        ("Is Kai a trusted Japanese razor brand?", "Yes, Kai Corporation is globally celebrated for high-quality Japanese blades."),
        ("Does it leave facial skin touchably smooth?", "Yes, leaves facial skin touchably smooth, soft, and clear."),
        ("Is the packaging recyclable?", "Yes, 100% recyclable environmentally friendly packaging."),
        ("Does it feature an ergonomic non-slip handle?", "Yes, comfortable resin handle offers complete control during trimming."),
        ("Does it leave facial skin feeling comfortable?", "Yes, leaves skin smooth, refreshed, and relaxed."),
        ("Does it give an instant radiant glow?", "Yes, removing dead skin cells and peach fuzz reveals instant skin radiance."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1870",
        "sku": "EK-1870",
        "gtin": "8906081442086",
        "category": "العناية الشخصية / شفرات تحديد وتفتيح شعر الوجه والحواجب اليابانية",
        "brand": "Kai Japan",
        "ar": {
            "title": "شفرات ازالة شعر الوجه 3 شفرات - كاي",
            "meta_title": "شفرات إزالة شعر الوجه كاي 3شفرات | إكليل أبها",
            "meta_description": "اشتري شفرات ازالة شعر الوجه 3 شفرات من كاي. شفرات يابانية أصيلة بغشاء حماية لتحديد الحواجب وتقشير الوجه الديرمابلانينغ. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["كاي", "شفرات_كاي", "تحديد_الحواجب", "ديرمابلانينغ", "إكليل_أبها"]
        },
        "en": {
            "title": "Kai Facial Hair Removal Razors - 3 Razors",
            "meta_title": "Kai Facial Hair Removal Razors 3 Pcs | Ekleel Abha",
            "meta_description": "Buy original Kai Facial Hair Removal Razors (3 Razors). Authentic Japanese dermaplaning & eyebrow shaping razors with Micro-Safety Guard. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["kai_razors", "kai_japan", "dermaplaning_razor", "eyebrow_shaper", "ekleel_abha"]
        },
        "schema": {
            "brand": "Kai Japan",
            "category": "Personal Care / Facial Razor",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "kai-facial-hair-removal-razors-3-razors.webp",
            "alt": "Kai Facial Hair Removal Razors 3 Razors",
            "title": "Kai Facial Hair Removal Razors 3 Razors"
        }
    }

def create_product_1871():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>معجون أسنان الأطفال دنتسيمو من عمر (2- 6 سنوات) (Dentissimo Kids Toothpaste - Ages 2-6 Years)</strong> معجون الأسنان الطبي السويسري الفاخر الخالي من الفلورايد المصمم خصيصاً لحماية أسنان الأطفال اللبنية، تقوية المينا، وتطهير اللثة من التسوس بحماية طبيعية آمنة 100% عند البلع. يرتكز هذا المعجون الطبي من دنتسيمو (Dentissimo Kids Caramel Toothpaste 50ml) على خلاصة البابونج الطبيعي (Chamomile)، فيتامين E، والزيليتول (Xylitol) بنكهة الكراميل اللذيذة.</p>
<p>يعمل معجون أسنان دنتسيمو للأطفال على تنظيف البلاك واللويحة الجرثومية برفق دون إيذاء مينا الأسنان اللبنية الرقيقة، التهدئة الحيوية لآلام اللثة، وتشجيع الطفل على التفريش اليومي بفضل نكهة الكراميل المحببة، ليضمن طفلاً بسنون ناصعة، لثة صحية، وابتسامة سعيدة خالية من النخر والتسوس.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية طبيعية 100% خالية من الفلورايد وآمنة عند البلع:</strong> تركيبة آمنة تماماً للأطفال من عمر 2 إلى 6 سنوات.</li>
  <li><strong>مدعم بالزيليتول لمنع تسوس الأسنان اللبنية:</strong> يثبط تكاثر بكتيريا التسوس ويحمي المينا الرقيقة.</li>
  <li><strong>معزز بخلاصة البابونج وفيتامين E:</strong> يهدئ التهابات اللثة ويحمي الأنسجة الفموية للأطفال.</li>
  <li><strong>نكهة الكراميل اللذيذة المحببة للأطفال:</strong> تجعل عملية تفريش الأسنان تجربة ممتعة وسهلة.</li>
  <li><strong>خالي 100% من البارابين، SLS، والمواد الكيميائية القاسية:</strong> تركيبة طبية سويسرية فائقة الأمان.</li>
  <li><strong>أنبوب مدمج سعة 50 مل:</strong> حجم ممتاز ومناسب للاستخدام اليومي للأطفال.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق):</strong> وضعي كمية بحجم حبة البازلاء من معجون دنتسيمو على فرشاة أسنان أطفال ناعمة.</li>
  <li><strong>الخطوة الثانية (التفريش):</strong> ساعدي الطفل على تفريش الأسنان واللثة بلطف لمدة دقيقتين بحركات دائرية ناعمة.</li>
  <li><strong>الخطوة الثالثة (البصق):</strong> اطلبي من الطفل بصق المعجون (آمن تماماً إذا بلع منه كمية صغيرة) واستعمليه مرتين يومياً.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الزيليتول وبابونج الفولكلور (Xylitol & Chamomile Extract):</strong> يمنعان التسوس ويهدئان أنسجة اللثة.</li>
  <li><strong>فيتامين E ونكهة الكراميل الطبيعية:</strong> يغديان اللثة ويعطيان طعماً لذيذاً محبباً للطفل.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الفموي لتفريش أسنان الأطفال تحت إشراف البالغين.</li>
  <li>على الرغم من أنه آمن عند البلع، يُفضل تعليم الطفل البصق بعد التفريش.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال الصغار دون إشراف وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل أم وأب يبحثان عن معجون أسنان دنتسيمو السويسري الطبيعي للأطفال من 2 إلى 6 سنوات بنكهة الكراميل لحماية الأسنان اللبنية.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>دنتسيمو (Dentissimo Switzerland)</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم / معاجين أسنان الأطفال السويسرية الخالية من الفلورايد (2-6 سنوات)</td></tr>
  <tr><th>نوع المنتج</th><td>معجون أسنان طبيعي للأطفال خالي من الفلورايد بنكهة الكراميل (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بالفم والأسنان اللبنية للأطفال)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان لبنية ناصعة، خالية من التسوس والنخر، لثة صحية ونفس طفولي عطر</td></tr>
  <tr><th>الملمس</th><td>جل معجون ناعم يولد رغوة خفيفة ملائمة للأطفال</td></tr>
  <tr><th>العطر</th><td>عطر ونكهة الكراميل الحلوة المحببة للأطفال</td></tr>
  <tr><th>المكونات النشطة</th><td>زيليتول، خلاصة البابونج، فيتامين E، نكهة الكراميل</td></tr>
  <tr><th>بلد المنشأ</th><td>سويسرا (Switzerland)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Medpack Swiss Group (Dentissimo)</td></tr>
  <tr><th>الفئة العمرية</th><td>الأطفال من عمر 2 إلى 6 سنوات (Ages 2-6 Years)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الزيليتول والبابونج في معجون دنتسيمو للأطفال (Dentissimo Kids)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج معجون دنتسيمو للأطفال مشكلة تسوس الأسنان اللبنية المبكر، تهيج اللثة أثناء تبديل الأسنان، ورفض الطفل لتفريش المعاجين الحارة.</p>

<h3>لماذا تنجح تركيبة الزيليتول والبابونج الخالية من الفلورايد؟</h3>
<p>لأن الزيليتول يحل محل السكر ولا تتغذى عليه بكتيريا التسوس، بينما يهدئ البابونج أنسجة اللثة ب أمان طبيعي 100%.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التفريش مرتين يومياً بإشراف الأبويين:</strong> فرشي أسنان الطفل صباحاً ومساءً لـ 2 دقيقة كاملة.<br>
2. <strong>كمية بحجم حبة البازلاء:</strong> استخدمي كمية صغيرة جداً ملائمة للطفل.<br>
3. <strong>فرشاة ناعمة ومخصصة:</strong> استعملي فرشاة أسنان ناعمة مخصصة للأطفال من 2 إلى 6 سنوات.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "معاجين الأطفال الخالية من الفلورايد لا تحمي الأسنان من التسوس."<br>
<strong>الحقيقة:</strong> الزيليتول السويسري يوفر حماية فائقة ضد بكتيريا التسوس وآمن تماماً عند البلع للأطفال.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعطل الزيليتول أيض الجلوكوز ببكتيريا الموتانس (Streptococcus mutans)، فيمنع إنتاج الأحماض التي تذيب مينا الطفل.</p>"""

    faqs = [
        ("ما هو معجون أسنان الأطفال دنتسيمو من عمر (2- 6 سنوات)؟", "هو معجون أسنان سويسري طبيعي للأطفال من 2 إلى 6 سنوات خالي من الفلورايد بالزيليتول والبابونج بنكهة الكراميل سعة 50 مل."),
        ("ما هي فوائد الزيليتول والبابونج والكراميل؟", "يحمي الزيليتول الأسنان اللبنية من التسوس، يهدئ البابونج اللثة، وتشجع نكهة الكراميل الطفل على التفريش."),
        ("هل هو آمن 100% إذا ابتلعه الطفل؟", "نعم، مثبت سريرياً أنه خالي من الفلورايد وآمن تماماً عند البلع للأطفال الصغار."),
        ("ما حجم العبوة؟", "تأتي لأنبوب مدمج للأطفال سعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية بحجم البازلاء على فرشاة ناعمة، فرشي أسنان الطفل دقيقتين مرتين يومياً واطلبي منه البصق."),
        ("هل هو خالي 100% من البارابين و SLS والفلورايد؟", "نعم، تركيبة سويسرية خالية 100% من الفلورايد والبارابين و SLS."),
        ("ما هو بلد صنع معجون دنتسيمو؟", "صُنع بفخر في سويسرا بواسطة مجموعة ميدباك السويسرية (Medpack Swiss Group)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات دنتسيمو لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يمنع تسوس الأسنان اللبنية؟", "نعم، يثبط الزيليتول بكتيريا التسوس ويحمي المينا اللبنية الرقيقة."),
        ("ما هي رائحة ونكهة معجون دنتسيمو للأطفال؟", "يتميز بنكهة الكراميل اللذيذة الحلوة المحببة جدا للأطفال."),
        ("هل يساعد في تهدئة آلام اللثة عند الأطفال؟", "نعم، خلاصة البابونج وفيتامين E يهدئان التهابات وآلام اللثة."),
        ("هل أنبوب العبوة 50 مل سهل الاستخدام للطفل؟", "نعم، أنبوب لطيف ورائع يسهل إخراج المعجون منه."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعبوتها المغلقة محكماً."),
        ("هل العبوة محكمة الغلق؟", "تأتي في أنبوب أنيق بغطاء لولبي محكم الحماية."),
        ("هل يناسب الأطفال من 2 إلى 6 سنوات؟", "مصمم خصيصاً للأطفال في المرحلة العمرية من سنتين إلى 6 سنوات."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُوصى بالتفريش 2 مرات يومياً تحت إشراف البالغين."),
        ("هل يمنح حس نظافة وانتعاش طفولي؟", "نعم، يضمن نظافة وانتعاشاً فموياً سعيداً للطفل."),
        ("هل ينصح به أطباء أسنان الأطفال؟", "نعم، دنتسيمو الماركة السويسرية الأكثر توصية للعناية بأسنان الأطفال."),
        ("هل هو معجون أسنان الأطفال السويسري الأكثر طلباً؟", "نعم، Dentissimo Kids الخيار الأول لأسنان الأطفال اللبنية."),
        ("هل يمنح ثقة وأمان للوالدين؟", "نعم، يضمن حماية فائقة وأماناً مطلقاً لأولادكِ."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، أنبوب صديق للبيئة وقابل لإعادة التدوير."),
        ("هل يزيل البلاك اللطيف عن الأسنان اللبنية؟", "نعم، ينظف طبقات البلاك برفق دون خدش المينا."),
        ("هل يترك فم الطفل عاطراً؟", "نعم، يترك فم الطفل برائحة الكراميل الحلوة."),
        ("هل يترك أسطح الأسنان ملساء؟", "نعم، يترك أسنان الطفل اللبنية ملساء ونظيفة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Dentissimo Kids Toothpaste (Ages 2-6 Years)</strong> (Dentissimo Kids Caramel Toothpaste 50ml) is the Swiss medical fluoride-free toothpaste engineered to protect milk teeth, fortify delicate enamel, and soothe toddler gums with 100% safe natural ingredients. Formulated with Chamomile, Vitamin E, Xylitol, and a delicious Caramel flavor.</p>
<p>Dentissimo Kids Toothpaste cleans interdental plaque gently without abrading soft primary enamel, relieves gum irritation during tooth eruption, and encourages daily toothbrushing habits through its appealing Caramel taste, keeping your child's smile healthy and cavity-free.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Fluoride-Free & Swallow-Safe Protection:</strong> Totally safe formula designed for toddlers aged 2 to 6 years.</li>
  <li><strong>Enriched with Xylitol Against Cavities:</strong> Inhibits cavity-causing bacteria and shields delicate primary enamel.</li>
  <li><strong>Soothing Chamomile Extract & Vitamin E:</strong> Calms tender gum tissue and protects young oral mucosa.</li>
  <li><strong>Delicious Caramel Flavor Kids Love:</strong> Makes daily toothbrushing an enjoyable, fun experience for toddlers.</li>
  <li><strong>100% Free of Parabens, SLS & Harsh Chemicals:</strong> Premium Swiss clinical formula prioritizing child oral safety.</li>
  <li><strong>Child-Friendly 50ml Tube:</strong> Compact size ideal for daily morning and bedtime toddler brushing routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply):</strong> Apply a pea-sized amount of Dentissimo Kids toothpaste onto a soft toddler toothbrush.</li>
  <li><strong>Step 2 (Brush):</strong> Guide your child to brush teeth and gums gently for 2 minutes using smooth circular motions.</li>
  <li><strong>Step 3 (Spit):</strong> Encourage the child to spit out toothpaste (swallowing a small amount is safe) twice daily.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Xylitol & Natural Chamomile Extract:</strong> Prevent cavity decay and calm tender toddler gum tissue.</li>
  <li><strong>Vitamin E & Natural Caramel Flavoring:</strong> Nourish gums while providing an enjoyable taste toddlers love.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For oral toddler toothbrushing application under adult supervision only.</li>
  <li>Although swallow-safe, teach children to spit out toothpaste after brushing.</li>
  <li>Keep out of reach of unsupervised young children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Parents seeking Swiss Dentissimo fluoride-free Caramel toothpaste for children aged 2 to 6 years to protect primary milk teeth.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Dentissimo (Dentissimo Switzerland)</td></tr>
  <tr><th>Category</th><td>Oral Care / Swiss Fluoride-Free Toddler Toothpastes (Ages 2-6)</td></tr>
  <tr><th>Product Type</th><td>Fluoride-Free Natural Xylitol Caramel Toddler Toothpaste (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Oral Hygiene & Milk Teeth for Toddlers)</td></tr>
  <tr><th>Finish</th><td>Clean primary teeth, cavity-free enamel, healthy gums & sweet breath</td></tr>
  <tr><th>Texture</th><td>Smooth gentle foaming paste gel</td></tr>
  <tr><th>Fragrance</th><td>Sweet delicious Caramel flavor</td></tr>
  <tr><th>Active Ingredients</th><td>Xylitol, Chamomile Extract, Vitamin E, Caramel Flavor</td></tr>
  <tr><th>Country of Origin</th><td>Switzerland</td></tr>
  <tr><th>Manufacturer</th><td>Medpack Swiss Group (Dentissimo)</td></tr>
  <tr><th>Age Group</th><td>Toddlers & Kids (Ages 2 to 6 Years)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Xylitol Bacterial Inhibition & Chamomile Mucosal Soothing</h2>

<h3>What problem does this solve?</h3>
<p>Dentissimo Kids Toothpaste resolves early milk teeth cavity decay, toddler gum irritation, and rejection of harsh adult toothpastes.</p>

<h3>Why choose Swiss Dentissimo Kids Fluoride-Free?</h3>
<p>Xylitol replaces dietary sugars so Mutans streptococci cannot ferment acid, while Chamomile calms tender gums with 100% natural safety.</p>"""

    en_faqs = [
        ("What is Dentissimo Kids Toothpaste (Ages 2-6 Years)?", "It is a Swiss natural fluoride-free toothpaste formulated with Xylitol, Chamomile, and a Caramel flavor to protect primary milk teeth."),
        ("What are the benefits of Xylitol, Chamomile, and Caramel flavor?", "Xylitol protects milk teeth against cavities, Chamomile calms gums, and Caramel flavor makes brushing fun for kids."),
        ("Is it 100% safe if swallowed by toddlers?", "Yes, clinically proven fluoride-free formula totally safe if small amounts are swallowed during brushing."),
        ("What volume is contained in this tube?", "It comes in a child-friendly 50ml tube."),
        ("How do I use it correctly?", "Apply a pea-sized amount, guide child to brush for 2 minutes twice daily, and encourage spitting out."),
        ("Is it 100% free of parabens, SLS, and fluoride?", "Yes, 100% free of fluoride, parabens, and SLS for maximum child safety."),
        ("Where is Dentissimo Kids Toothpaste manufactured?", "Proudly manufactured in Switzerland by Medpack Swiss Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All Dentissimo products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it prevent cavity decay in milk teeth?", "Yes, Xylitol inhibits cavity-causing bacteria and shields delicate primary enamel."),
        ("What flavor does Dentissimo Kids Toothpaste have?", "Features a sweet, delicious Caramel flavor that toddlers love."),
        ("Does it soothe toddler gum irritation?", "Yes, natural Chamomile extract and Vitamin E calm tender gum tissue."),
        ("Is the 50ml tube easy for toddlers to handle?", "Yes, convenient tube design easy for parents and children to dispense."),
        ("How should I store the tube?", "Store in a cool, dry place away from direct heat."),
        ("Is the tube cap leak-proof?", "Yes, comes with a secure screw-top cap."),
        ("Is it specifically designed for ages 2 to 6?", "Yes, specially formulated for primary milk teeth of toddlers aged 2 to 6 years."),
        ("How many times daily should it be used?", "Recommended for use twice daily under adult supervision."),
        ("Does it deliver fresh child oral hygiene?", "Yes, leaves your child's mouth feeling clean, healthy, and sweet."),
        ("Is Dentissimo recommended by pediatric dentists?", "Yes, Swiss Dentissimo is a top trusted brand recommended by pediatric dentists."),
        ("Is it a top Swiss choice for toddler dental care?", "Yes, Dentissimo Kids is a flagship choice for safe toddler primary teeth protection."),
        ("Does it give parents peace of mind?", "Yes, guarantees complete enamel defense and swallow-safe safety."),
        ("Is the tube recyclable?", "Yes, 100% recyclable environmentally friendly tube."),
        ("Does it gently clean milk teeth plaque?", "Yes, sweeps away soft plaque without scratching soft primary enamel."),
        ("Does it leave your child's breath sweet?", "Yes, leaves child's breath smelling sweet with a caramel aroma."),
        ("Does it leave tooth surfaces smooth?", "Yes, leaves milk teeth surfaces smooth and clean."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1871",
        "sku": "EK-1871",
        "gtin": "7640162322393",
        "category": "العناية بالفم / معاجين أسنان الأطفال السويسرية الخالية من الفلورايد (2-6 سنوات)",
        "brand": "Dentissimo",
        "ar": {
            "title": "معجون أسنان الأطفال دنتسيمو من عمر (2- 6 سنوات)",
            "meta_title": "معجون اسنان دنتسيمو للأطفال 2-6 سنوات | إكليل أبها",
            "meta_description": "اشتري معجون أسنان الأطفال دنتسيمو (2-6 سنوات). معجون سويسري خالي من الفلورايد بالزيليتول والكراميل لحماية أسنان الأطفال. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["دنتسيمو", "معجون_أطفال", "خالي_من_الفلورايد", "أسنان_الأطفال", "إكليل_أبها"]
        },
        "en": {
            "title": "Dentissimo Kids Toothpaste (Ages 2-6 Years)",
            "meta_title": "Dentissimo Kids Toothpaste Ages 2-6 | Ekleel Abha",
            "meta_description": "Buy original Dentissimo Kids Toothpaste (Ages 2-6 Years). Swiss fluoride-free Xylitol Caramel toddler toothpaste. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["dentissimo", "dentissimo_kids", "fluoride_free", "toddler_toothpaste", "ekleel_abha"]
        },
        "schema": {
            "brand": "Dentissimo",
            "category": "Oral Care / Kids Toothpaste",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "dentissimo-kids-toothpaste-ages-2-6-years.webp",
            "alt": "Dentissimo Kids Toothpaste Ages 2-6 Years",
            "title": "Dentissimo Kids Toothpaste Ages 2-6 Years"
        }
    }

def create_product_1873():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>صابون تبيض وتقشير للجسم من بيزلين، 100 جرام (Beesline Whitening & Exfoliating Body Soap - 100g)</strong> الصابون الطبيعي النباتي الأكثر شهـرة وتأكيداً لتفتيح التصبغات الجلديّة، تقشير الجلد الميت، وتوحيد لون بشرة الجسم والأكواع والركب والمناطق المجهدة. يرتكز هذا الصابون الأيقوني من بيزلين (Beesline Whitening & Exfoliating Soap) على خلاصة الشوفان الطبيعي (Oat Flakes)، لوميسكين (Lumiskin)، حمض اللبن (Lactic Acid)، وصمغ النحل النقي (Propolis).</p>
<p>تعمل صابونة بيزلين للتبييض والتقشير على تقشير خلايا الجلد الميتة برفق بواسطة رقائق الشوفان الناعمة، تثبيط التصبغات البقعية، وتأمين ترطيب عميق يمنع الجفاف، لتمنحكِ بشرة جسم ناصعة السواد، موحدة، ومشعّة بالنضارة والنعومة المخملية من أول أسابيع.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وتقشير طبيعي 2 في 1 للجسم:</strong> يقشر الخلايا الميتة ويفتّح التصبغات ب فاعلية فائقة.</li>
  <li><strong>مدعم برقائق الشوفان واللوميسكين وحمض اللبن:</strong> تقشير ميكانيكي وكيميائي لطيف يجدد البشرة.</li>
  <li><strong>تطهير وترميم بـ صمغ النحل النقي (Propolis):</strong> يطهر الجلد من الشوائب ويحمي الحاجز الطبيعي.</li>
  <li><strong>توحيد لون الأكواع والركب والمناطق الحساسة:</strong> يعالج اسمرار المناطق المجهدة بالجسم.</li>
  <li><strong>رغوة غنية وعطر ناعم منعش:</strong> ينظف الدهون الزائدة ويترك الجسم بطراوة ونعومة ناصعة.</li>
  <li><strong>قطعة صابون وافرة بوزن 100 جم:</strong> حجم ممتاز يدوم لعدة أسابيع من العناية اليومية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الرغوة):</strong> افركي صابونة بيزلين بين يدين مبللتين بالماء الفاتر لتوليد رغوة غنية برقائق الشوفان.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي الرغوة على بشرة الجسم والأكواع والركب ودلكي بحركات دائرية خفيفة لتقشير الجلد.</li>
  <li><strong>الخطوة الثالثة (الشطف):</strong> اشطفي بالماء الفاتر جيداً واستعملي لوشن بيزلين المرطب (تُستعمل 2 إلى 3 مرات أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>رقائق الشوفان واللوميسكين (Oat Flakes & Lumiskin):</strong> تقشر الجلد الميت وتثبط صبغة الميلامين.</li>
  <li><strong>صمغ النحل وحمض اللبن (Propolis & Lactic Acid):</strong> يطهران الجلد ويجددان الخلايا ب طراوة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم فقط.</li>
  <li>تجنبي ملامسة الرغوة المباشرة للعينين ويُنصح بتطبيق كريم مرطب بعد الاستعمال.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بوعاء صابون جاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تعاني من تصبغات الجسم، اسمرار الأكواع والركب، وتفتش عن صابونة بيزلين للتبييض والتقشير 100 جم.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / صابون بيزلين الطبيعي لتفتيح وتقشير بشرة الجسم 100g</td></tr>
  <tr><th>نوع المنتج</th><td>صابون نباتي طبيعي لتفتيح وتقشير بشرة الجسم (100g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (العادية، الجافة، والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة جسم ناصعة، موحدة اللون، خالية من التصبغات والجلد الميت ومخملية</td></tr>
  <tr><th>الملمس</th><td>قالب صابوني مقشر غني برقائق الشوفان يولد رغوة كيروفية</td></tr>
  <tr><th>العطر</th><td>عطر بيزلين العسلي الطبيعي الناعم</td></tr>
  <tr><th>المكونات النشطة</th><td>رقائق الشوفان، لوميسكين، صمغ النحل (Propolis)، حمض اللبن</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد اللوميسكين والشوفان في صابون بيزلين (Beesline Soap)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج صابونة بيزلين للتبييض والتقشير مشكلة تصبغات الجسم، اسمرار الأكواع والركب، تراكم الجلد الميت، وشحوب الجلد.</p>

<h3>لماذا تنجح تركيبة الشوفان واللوميسكين؟</h3>
<p>لأن رقائق الشوفان تقشر الخلايا القرنية الميتة ميكانيكياً، بينما يمنع اللوميسكين نشاط إنزيم التايروسينيز ل تفتيح التصبغات.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام 3 مرات أسبوعياً:</strong> استعملي الصابونة 2-3 مرات أسبوعياً للحفاظ على نضارة التقشير.<br>
2. <strong>التركيز على الأكواع والركب:</strong> دلكي المناطق المجهدة بالرغوة لـ 1 دقيقة لتفتيحها.<br>
3. <strong>المرطب فورياً بعد الشطف:</strong> وضعي لوشن بيزلين المبيض بعد الشطف لنتائج تفتيح مضاعفة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "صابون التقشير بالشوفان يجرح الجلد ويسبب جفافاً شديداً."<br>
<strong>الحقيقة:</strong> صابون بيزلين مدعم بصمغ النحل والجليسرين لتقشير ناعم يحفظ رطوبة البشرة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعمل حمض اللبن (Lactic Acid) على تفكيك الروابط بين الخلايا الميتة، بينما تمنع ألكالويات اللوميسكين تكون الميلامين.</p>"""

    faqs = [
        ("ما هو صابون تبيض وتقشير للجسم من بيزلين، 100 جرام؟", "هو صابون طبيعي نباتي من بيزلين برقائق الشوفان واللوميسكين لتفتيح وتقشير بشرة الجسم والأكواع والركب 100 جم."),
        ("ما هي فوائد رقائق الشوفان واللوميسكين وصمغ النحل؟", "تقشر رقائق الشوفان الجلد الميت، يثبط اللوميسكين التصبغات، ويطهر صمغ النحل البشرة ب طراوة."),
        ("هل يفتّح اسمرار الأكواع والركب والمناطق المجهدة؟", "نعم، مثبت سريرياً في تفتيح اسمرار الأكواع، الركب، والمناطق الحساسة والجسم."),
        ("ما حجم ووزن قالب الصابونة؟", "تأتي بوزن وافر 100 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "افركي الصابونة لتوليد رغوة الشوفان، دلكي بشرة الجسم 1-2 دقيقة واشطفي بالماء الفاتر ثم ضعي مرطباً."),
        ("هل هو مكون من مواد طبيعية ونباتية 100%؟", "نعم، مكونات طبيعية ونباتية خالية من الهيدروكينون والبارابين."),
        ("ما هو بلد صنع صابون بيزلين؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين العالمية (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يناسب جميع أنواع بشرة الجسم؟", "نعم، مناسب للبشرة العادية، الجافة، والمختلطة."),
        ("ما هي رائحة صابون بيزلين للتبييض؟", "يتميز برائحة عسلية طبيعية لطيفة وناعمة."),
        ("هل يزيل التصبغات والجلد الميت ب فاعلية؟", "نعم، يقشر الخلايا الميتة ويكشف عن بشرة ناصعة وموحدة اللون."),
        ("هل العبوة 100 جم اقتصادية وتدوم طويلاً؟", "نعم، قالب وافر يكفي للاستخدام المستمر لعدة أسابيع."),
        ("كيف أحتفظ بالصابونة؟", "تُحفظ في وعاء صابون جاف بعيداً عن تجمع الماء."),
        ("هل يترك الجلد طرياً ومخملياً؟", "نعم، يترك بشرة الجسم طرية ونظيفة ومخملية."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة كرتونية أنيقة مغلفة بالبلاستيك الحامي."),
        ("هل يلزم استخدام واقي شمس مع الجسم؟", "يُفضل استخدام واقي الشمس لحماية تفتيح البشرة عند الخروج نهاراً."),
        ("كم مرة يُفضل استخدامه أسبوعياً؟", "يُستعمل من 2 إلى 3 مرات أسبوعياً."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع الفئات العمرية للنساء والرجال من سن 12 سنة."),
        ("هل خالي من الكيماويات الضارة؟", "نعم، خالي 100% من البارابين، الفثالات، والهيدروكينون."),
        ("هل هو صابون التقشير والتبييض الأشهر لبيزلين؟", "نعم، صابونة الشوفان واللوميسكين الصابونة الأولى والأكثر مبيعاً لبيزلين."),
        ("هل يمنح حس نضارة وصفاء؟", "نعم، يضمن إشراقة وصفاءً ورائحة عسلية ممتازة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يجهز البشرة لامتصاص كريمات التفتيح؟", "نعم، تقشير الجلد الميت يزيد فاعلية امتصاص كريمات ولوشنات بيزلين."),
        ("هل يترك ملمساً نظيفاً؟", "نعم، ينظف المسام ويترك الجسم أملساً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Whitening & Exfoliating Body Soap, 100g</strong> is the iconic natural botanical body soap bar engineered to fade dark skin hyperpigmentation, exfoliate dead skin cell layers, and unify body, elbow, and knee skin tone. Formulated by Beesline, it blends natural Oat Flakes, Lumiskin, Lactic Acid, and pure Propolis.</p>
<p>Beesline Whitening & Exfoliating Soap sloughs off dead epidermal cells gently via soft Oat particles, inhibits melanin production, and provides deep hydration to prevent dryness, leaving your body skin touchably soft, evenly brightened, and velvety smooth from early weeks.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>2-in-1 Natural Whitening & Exfoliation:</strong> Exfoliates dead skin layers and brightens hyperpigmentation.</li>
  <li><strong>Enriched with Oat Flakes, Lumiskin & Lactic Acid:</strong> Dual physical and chemical exfoliation renewing body skin.</li>
  <li><strong>Purifying Propolis Defense:</strong> Cleanses skin pores and preserves the natural cutaneous barrier.</li>
  <li><strong>Unifies Elbow, Knee & Sensitive Zone Tone:</strong> Treats dark spots on stressed body skin patches.</li>
  <li><strong>Rich Foaming Fresh Honey Aroma:</strong> Sweeps away excess sebum leaving body skin soft and hydrated.</li>
  <li><strong>Generous 100g Soap Bar:</strong> High-value soap bar providing weeks of continuous weekly body care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Lather):</strong> Rub Beesline soap bar between wet hands with warm water to create a creamy oat-infused lather.</li>
  <li><strong>Step 2 (Apply):</strong> Apply lather over body skin, elbows, and knees, massaging gently in circular motions.</li>
  <li><strong>Step 3 (Rinse):</strong> Rinse thoroughly with warm water and apply a moisturizing body lotion (use 2 to 3 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Oat Flakes & Lumiskin:</strong> Exfoliate dead superficial skin cells and inhibit tyrosinase melanin synthesis.</li>
  <li><strong>Propolis & Lactic Acid:</strong> Purify skin pores and promote cell renewal while maintaining skin hydration.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application only.</li>
  <li>Avoid direct contact with eyes; apply a moisturizing lotion post-rinse.</li>
  <li>Keep out of reach of children and store in a dry soap dish in a cool place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dark body spots, rough elbows, or knees seeking Beesline's 100g natural Whitening & Exfoliating Soap.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Skincare / Beesline Natural Whitening & Exfoliating Soap Bars 100g</td></tr>
  <tr><th>Product Type</th><td>Natural Oat & Lumiskin Whitening & Exfoliating Body Soap Bar (100g)</td></tr>
  <tr><th>Volume/Weight</th><td>100 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Normal, Dry & Combination)</td></tr>
  <tr><th>Finish</th><td>Radiant, even-toned, dead-skin-free & touchably soft skin</td></tr>
  <tr><th>Texture</th><td>Exfoliating soap bar enriched with oat particles</td></tr>
  <tr><th>Fragrance</th><td>Subtle natural honey Beesline aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Oat Flakes, Lumiskin, Propolis, Lactic Acid</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Lumiskin Melanin Block & Oat Flakes Exfoliation</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Whitening & Exfoliating Body Soap resolves body hyperpigmentation, rough elbows, dead skin buildup, and dull skin texture.</p>

<h3>Why choose Beesline Whitening Soap?</h3>
<p>Natural Oat Flakes provide micro-dermabrasion, while Lumiskin inhibits diacylglycerol synthesis to block melanin formation safely.</p>"""

    en_faqs = [
        ("What is Beesline Whitening & Exfoliating Body Soap, 100g?", "It is a natural botanical soap bar formulated with Oat Flakes, Lumiskin, and Propolis to exfoliate dead skin and brighten body tone."),
        ("What are the benefits of Oat Flakes, Lumiskin, and Propolis?", "Oat Flakes exfoliate dead skin cells, Lumiskin brightens dark spots, and Propolis purifies pores with natural safety."),
        ("Does it lighten dark elbows, knees, and body patches?", "Yes, clinically proven to fade dark hyperpigmentation on elbows, knees, and body skin."),
        ("What weight is contained in this soap bar?", "It comes as a generous 100g soap bar."),
        ("How do I use it correctly?", "Lather between wet hands, massage onto body skin for 1-2 minutes, rinse with warm water, and moisturize 2-3 times weekly."),
        ("Is it 100% natural and cruelty-free?", "Yes, 100% natural botanical formula free of hydroquinone and parabens."),
        ("Where is Beesline Soap manufactured?", "Proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Is it suitable for all body skin types?", "Ideal for normal, dry, and combination body skin types."),
        ("What scent does Beesline Whitening Soap have?", "Features a soft, pleasant natural honey fragrance."),
        ("Does it remove dead skin cells effectively?", "Yes, gentle Oat particles slough off dead skin layers to reveal radiant skin."),
        ("Is the 100g soap bar economical?", "Yes, high-value 100g soap bar lasts through weeks of regular body exfoliation."),
        ("How should I store the soap bar?", "Store in a dry soap dish away from standing water to prevent melting."),
        ("Does it leave skin touchably soft and velvety?", "Yes, leaves body skin touchably soft, smooth, and velvety."),
        ("Is the packaging securely sealed?", "Yes, comes in a protective cardboard box wrapped in plastic film."),
        ("Should sunscreen be used on body skin when outdoors?", "Applying sunscreen to exposed skin when outdoors preserves whitening results."),
        ("How many times weekly should I use it?", "Recommended for use 2 to 3 times weekly."),
        ("Is it suitable for men and women?", "Suitable for all age groups, both men and women aged 12+."),
        ("Is it free of harsh chemicals?", "Dermatologically tested and 100% free of hydroquinone, parabens, and phthalates."),
        ("Is it Beesline's best-selling exfoliating soap bar?", "Yes, Whitening & Exfoliating Soap is the #1 flagship body soap bar by Beesline."),
        ("Does it deliver complete radiance confidence?", "Yes, guarantees visible skin clarity, smoothness, and radiance confidence."),
        ("Is the packaging recyclable?", "Yes, 100% recyclable environmentally friendly packaging."),
        ("Does it enhance lotion absorption?", "Yes, clearing dead skin layers allows body lotions to penetrate deeper."),
        ("Does it leave body skin feeling fresh?", "Yes, purifies pores leaving body skin fresh and clean."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1873",
        "sku": "EK-1873",
        "gtin": "5281018003121",
        "category": "العناية بالبشرة / صابون بيزلين الطبيعي لتفتيح وتقشير بشرة الجسم 100g",
        "brand": "Beesline",
        "ar": {
            "title": "صابون تبيض وتقشير للجسم من بيزلين، 100 جرام",
            "meta_title": "صابون بيزلين لتبيض وتقشير الجسم 100جم | إكليل أبها",
            "meta_description": "اشتري صابون تبيض وتقشير للجسم من بيزلين (100 جرام). صابون طبيعي برقائق الشوفان واللوميسكين لتفتيح وتقشير بشرة الجسم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بيزلين", "صابون_بيزلين", "تفتيح_الجسم", "تقشير_الشوفان", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Whitening & Exfoliating Body Soap, 100g",
            "meta_title": "Beesline Whitening & Exfoliating Soap 100g | Ekleel Abha",
            "meta_description": "Buy original Beesline Whitening & Exfoliating Body Soap (100g). Natural Oat & Lumiskin body whitening soap bar. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["beesline", "beesline_soap", "whitening_soap", "exfoliating_soap", "ekleel_abha"]
        },
        "schema": {
            "brand": "Beesline",
            "category": "Skincare / Body Soap",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "beesline-whitening-and-exfoliating-body-soap-100g.webp",
            "alt": "Beesline Whitening & Exfoliating Body Soap 100g",
            "title": "Beesline Whitening & Exfoliating Body Soap 100g"
        }
    }

def create_product_1874():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم شّد الوجه الليلي المُبيّض من بيزيلين- 50 مل (Beesline Whitening Lifting Night Cream - 50ml)</strong> المستحضر الطبي النباتي الفاخر المخصص لتفتيح تصبغات البشرة الليلية، شد تجاعيد وترهلات الوجه، وإعادة نضارة البشرة أثناء النوم. يرتكز هذا الكريم المميز من بيزلين (Beesline Whitening Lifting Night Cream 50ml) على مركب التفتيح النباتي اللوميسكين (Lumiskin)، حمض الهيالورونيك (Hyaluronic Acid)، زيت التجاعيد من الورد الجوري، وغذاء ملكات النحل (Royal Jelly).</p>
<p>يعمل كريم بيزلين الليلي المبيض والشد على تجديد خلايا الوجه أثناء الليل، تفتيح التصبغات والكلف، وشد خطوط الوجه الدقيقة، ليترك بشرتكِ عند الصباح ناصعة، مشدودة، ومفعمة بالشباب والإشراق دون أي ثقل زيت لزج.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح مكثف وشد لليلي متكامل للبشرة:</strong> يزيل التصبغات وتجاعيد الوجه أثناء النوم.</li>
  <li><strong>مدعم بـ غذاء ملكات النحل وحمض الهيالورونيك:</strong> يحفز إنتاج الكولاجين ويحبس الترطيب لـ 24 ساعة.</li>
  <li><strong>معزز باللوميسكين وزيت الورد الجوري:</strong> يثبط صبغة الميلامين ويمنح الوجه مرونة ناصعة.</li>
  <li><strong>تقليل الخطوط الدقيقة وتعب البشرة:</strong> يعيد بناء ألياف البشرة المجهدة.</li>
  <li><strong>امتصاص مخملي غني 100% غير لزج:</strong> ينفذ بالبشرة ليلاً دون ترك أثر دهني لزج على الوسادة.</li>
  <li><strong>عبوة زجاجية فاخرة سعة 50 مل:</strong> حجم ممتازة ومناسب للروتين الليلي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> نظفي بشرة الوجه والرقبة جيداً بالغسول الفاتر وجففيها قبل النوم.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي كمية مناسبة من كريم بيزلين الليلي على الوجه والرقبة.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي برفق بحركات دائرية صاعدة لأعلى حتى امتصاص الكريم بالكامل (يُستعمل كل ليلة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>غذاء ملكات النحل وحمض الهيالورونيك (Royal Jelly & Hyaluronic Acid):</strong> يشدان البشرة ويحفزان الكولاجين.</li>
  <li><strong>اللوميسكين وزيت الورد الجوري:</strong> يفتحان البقع التصبغية ويعيدان المرونة والشباب.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي الليلي على بشرة الوجه والرقبة فقط.</li>
  <li>تجنبي ملامسة الكريم المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن كريم بيزلين الليلي المبيض والشد 50 مل لتفتيح التصبغات وشد تجاعيد الوجه أثناء النوم.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات بيزلين الليلية لتفتيح وشد الوجه والتجاعيد 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>كريم ليلي طبيعي لتفتيح وتصحيح التصبغات وشد الوجه (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (العادية، الجافة، والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة وجه مشدودة، ناصعة، موحدة اللون، خالية من التصبغات والتجاعيد صباحاً</td></tr>
  <tr><th>الملمس</th><td>كريم مخملي فاخر سريع الامتصاص دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر بيزلين الوردي اللطيف الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>غذاء ملكات النحل، لوميسكين، حمض الهيالورونيك، زيت الورد</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>النساء والفتيات (من 20 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد غذاء ملكات النحل واللوميسكين الليلي في بيزلين (Beesline Lifting Cream)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم بيزلين الليلي المبيض والشد مشكلة تصبغات الوجه الليلية، التجاعيد والخطوط الدقيقة، وفقدان مرونة البشرة.</p>

<h3>لماذا تنجح تركيبة غذاء ملكات النحل واللوميسكين؟</h3>
<p>لأن غذاء ملكات النحل يزود الخلايا بالأحماض الأمينية لبناء الكولاجين ليلاً، بينما يمنع اللوميسكين تشكل الميلامين.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق قبل النوم بـ 20 دقيقة:</strong> وضعي الكريم قبل النوم ليتسنى للبشرة امتصاصه بالكامل.<br>
2. <strong>التدليك بحركات صاعدة لأعلى:</strong> دلكي من الرقبة باتجاه الخدين لتعزيز الشد الطبيعي.<br>
3. <strong>الاستمرار لـ 4 أسابيع:</strong> يضمن الاستخدام الليلي المنتظم خفوت التجاعيد وتفتيح الوجه.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الكريمات الليلية للشد ثقيلة جداً وتسبب انسداد المسام والبثور."<br>
<strong>الحقيقة:</strong> كريم بيزلين الليلي مصمم بتركيبة نباتية مخملية تنفذ فورياً دون ترك أثر دهني لزج.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخترق ببتيدات Royal Jelly الأنسجة أثناء النوم لتنشيط الفيبروبلاست، بينما يثبط اللوميسكين إنزيم التايروسينيز.</p>"""

    faqs = [
        ("ما هو كريم شّد الوجه الليلي المُبيّض من بيزيلين- 50 مل؟", "هو كريم ليلي فاخر من بيزلين بغذاء ملكات النحل واللوميسكين لتفتيح التصبغات وشد تجاعيد الوجه أثناء النوم 50 مل."),
        ("ما هي فوائد غذاء ملكات النحل واللوميسكين وحمض الهيالورونيك؟", "يحفز غذاء ملكات النحل الكولاجين، يثبط اللوميسكين التصبغات، ويحبس الهيالورونيك الترطيب لشباب الوجه."),
        ("هل يفتّح التصبغات ويشد تجاعيد الوجه ليلاً؟", "نعم، مثبت سريرياً في تفتيح التصبغات وشد خطوط الوجه الدقيقة أثناء الليل."),
        ("ما حجم العبوة؟", "تأتي لعلبة زجاجية أنيقة سعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي كمية مناسبة على بشرة الوجه والرقبة النظيفة قبل النوم، دلكي بحركات صاعدة لأعلى كل ليلة."),
        ("هل هو مكون من مواد طبيعية ونباتية 100%؟", "نعم، مكونات طبيعية ونباتية خالية من البارابين والهيدروكينون."),
        ("ما هو بلد صنع كريم بيزلين الليلي؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين العالمية (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يناسب جميع انواع بشرة الوجه؟", "نعم، مناسب للبشرة العادية، الجافة، والمختلطة."),
        ("ما هي رائحة كريم بيزلين الليلي؟", "يتميز برائحة الورد والملكات الطبيعية الناعمة والراقية."),
        ("هل يقلل الخطوط الدقيقة وتعب البشرة صباحاً؟", "نعم، يمنح البشرة عند الاستيقاظ مظهراً مشدوداً، ناصعاً، ومشرقاً."),
        ("هل العبوة 50 مل مناسبة للروتين الليلي؟", "نعم، عبوة وافرة تكفي لعدة أشهر من العناية الليلية."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الحرارة."),
        ("هل يمتص بسرعة دون ترك أثر دهني على الوسادة؟", "نعم، قوام مخملي ينفذ بالبشرة فورياً دون تلطيخ الوسادة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة زجاجية أنيقة بغطاء محكم الحماية."),
        ("هل يناسب السيدات من سن 20 سنة فما فوق؟", "ممتاز جداً للسيدات والفتيات من سن 20 سنة فما فوق ل الوقاية والشد."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل مرة واحدة كل ليلة قبل النوم."),
        ("هل يناسب البشرة الحساسة؟", "نعم، فورمولا مهدئة وخالية من الكيماويات القاسية ومناسبة للبشرة الحساسة."),
        ("هل هو كريم الشد والتفتيح الليلي الأكثر شهرة لبيزلين؟", "نعم، Whitening Lifting Night Cream الكريم الليلي الأول لبيزلين."),
        ("هل يمنح حس شباب ونضارة مطلقة؟", "نعم، يضمن نضارة وشباباً وإشراقة رائعة صبيحة كل يوم."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة زجاجية صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يشد بشرة الرقبة المترهلة؟", "نعم، ممتاز لشد وتفتيح بشرة الرقبة والوجه معا."),
        ("هل يترك الجلد طرياً؟", "نعم، يترك الوجه طرياً ومخملياً."),
        ("هل يمنع ظهور التصبغات الجديدة؟", "نعم، اللوميسكين يثبط تكاثر الميلامين المستقبلي."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Whitening Lifting Night Cream - 50ml</strong> is the luxury natural botanical night cream engineered to brighten facial hyperpigmentation, lift sagging skin contours, and smooth wrinkles during sleep. Formulated by Beesline, it blends Lumiskin, Hyaluronic Acid, Royal Jelly, and Damask Rose oil.</p>
<p>Beesline Whitening Lifting Night Cream regenerates facial skin cells overnight, fading melasma and dark spots while restoring youthful firmness to fine lines, leaving your face visibly lifted, brightened, and glowing by morning without heavy greasy film.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intense Overnight Whitening & Lifting Care:</strong> Fades dark spots and lifts facial wrinkles during sleep.</li>
  <li><strong>Enriched with Royal Jelly & Hyaluronic Acid:</strong> Stimulates collagen production and locks in 24-hour hydration.</li>
  <li><strong>Lumiskin & Damask Rose Oil Matrix:</strong> Inhibits melanin synthesis and restores youthful skin elasticity.</li>
  <li><strong>Reduces Fine Lines & Fatigue Shadow:</strong> Restructures stressed dermal fibers for morning radiance.</li>
  <li><strong>100% Non-Greasy Fast Absorbing Velvety Texture:</strong> Penetrates skin deeply without leaving oily pillow stains.</li>
  <li><strong>Luxury 50ml Glass Jar:</strong> High-value packaging ideal for continuous nightly anti-aging grooming.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse facial and neck skin thoroughly with a gentle cleanser before bed and pat dry.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a small amount of Beesline night cream onto facial and neck skin.</li>
  <li><strong>Step 3 (Massage):</strong> Massage gently in upward circular motions until fully absorbed (use every night).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Royal Jelly & Hyaluronic Acid:</strong> Firm facial contours, stimulate collagen synthesis, and seal in deep moisture.</li>
  <li><strong>Lumiskin & Damask Rose Oil:</strong> Fade dark hyperpigmentation spots and restore supple youthful skin radiance.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical nocturnal facial and neck application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Beesline's 50ml natural Whitening Lifting Night Cream to fade dark spots and lift facial wrinkles during sleep.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Skincare / Beesline Natural Whitening & Lifting Night Creams 50ml</td></tr>
  <tr><th>Product Type</th><td>Natural Royal Jelly & Lumiskin Whitening & Lifting Night Cream (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Normal, Dry & Combination)</td></tr>
  <tr><th>Finish</th><td>Visibly lifted, brightened, even-toned & youthfully firm skin by morning</td></tr>
  <tr><th>Texture</th><td>Rich velvety fast-absorbing night cream</td></tr>
  <tr><th>Fragrance</th><td>Subtle natural Damask Rose Beesline aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Royal Jelly, Lumiskin, Hyaluronic Acid, Rose Oil</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>Adult Women (Ages 20+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Royal Jelly Collagen Stimulation & Lumiskin Nocturnal Block</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Whitening Lifting Night Cream resolves nocturnal facial hyperpigmentation, fine line sagging, and loss of skin elasticity.</p>

<h3>Why choose Beesline Night Lifting Cream?</h3>
<p>Royal Jelly amino acids stimulate fibroblast collagen synthesis overnight, while Lumiskin inhibits tyrosinase for morning radiance.</p>"""

    en_faqs = [
        ("What is Beesline Whitening Lifting Night Cream - 50ml?", "It is a luxury natural night cream formulated with Royal Jelly, Lumiskin, and Hyaluronic Acid to brighten dark spots and lift facial wrinkles overnight."),
        ("What are the benefits of Royal Jelly, Lumiskin, and Hyaluronic Acid?", "Royal Jelly stimulates collagen production, Lumiskin fades dark spots, and Hyaluronic Acid locks in deep moisture."),
        ("Does it lift facial wrinkles and brighten skin during sleep?", "Yes, clinically proven to fade hyperpigmentation and firm fine lines overnight."),
        ("What volume is contained in this jar?", "It comes in a luxury 50ml glass jar."),
        ("How do I apply it correctly?", "Apply onto clean face and neck every night before bed, massaging gently upward until fully absorbed."),
        ("Is it 100% natural and cruelty-free?", "Yes, 100% natural botanical formula free of parabens and hydroquinone."),
        ("Where is Beesline Night Cream manufactured?", "Proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Is it suitable for all facial skin types?", "Ideal for normal, dry, and combination facial skin types."),
        ("What scent does Beesline Night Cream have?", "Features a soft, luxurious Damask Rose fragrance."),
        ("Does it restore morning skin firmness and radiance?", "Yes, leaves skin visibly lifted, brightened, and supple by morning."),
        ("Is the 50ml jar economical for nightly use?", "Yes, generous 50ml jar lasts through months of nightly anti-aging care."),
        ("How should I store the jar?", "Store in a cool, dry place away from direct heat."),
        ("Does it absorb quickly without staining pillows?", "Yes, weightless velvety cream absorbs deeply without leaving greasy pillow stains."),
        ("Is the glass jar securely sealed?", "Yes, comes in a luxury glass jar with a tight protective lid."),
        ("Is it suitable for women aged 20+?", "Yes, ideal for adult women aged 20+ for prevention and firming care."),
        ("How many times daily should it be used?", "Recommended for use once daily every night before bed."),
        ("Is it safe for sensitive skin?", "Yes, soothing formula free of harsh chemicals; safe for sensitive skin."),
        ("Is it Beesline's flagship night lifting cream?", "Yes, Whitening Lifting Night Cream is the #1 iconic night cream by Beesline."),
        ("Does it deliver complete youthful radiance confidence?", "Yes, guarantees visible skin firmness, clarity, and radiance confidence."),
        ("Is the glass jar recyclable?", "Yes, 100% recyclable environmentally friendly glass jar."),
        ("Does it lift sagging neck skin?", "Yes, highly effective at lifting and brightening neck and facial contours."),
        ("Does it leave skin touchably soft?", "Yes, leaves facial skin touchably soft, smooth, and supple."),
        ("Does it prevent new dark spots?", "Yes, Lumiskin inhibits future melanin synthesis overnight."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1874",
        "sku": "EK-1874",
        "gtin": "5281018003237",
        "category": "العناية بالبشرة / كريمات بيزلين الليلية لتفتيح وشد الوجه والتجاعيد 50ml",
        "brand": "Beesline",
        "ar": {
            "title": "كريم شّد الوجه الليلي المُبيّض من بيزيلين- 50 مل",
            "meta_title": "كريم شد الوجه الليلي المبيض بيزلين 50مل | إكليل أبها",
            "meta_description": "اشتري كريم شّد الوجه الليلي المُبيّض من بيزيلين (50 مل). كريم ليلي بغذاء ملكات النحل واللوميسكين لتفتيح التصبغات وشد الوجه. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بيزلين", "كريم_بيزلين_الليلي", "شد_الوجه", "تفتيح_البشرة", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Whitening Lifting Night Cream - 50ml",
            "meta_title": "Beesline Whitening Lifting Night Cream 50ml | Ekleel Abha",
            "meta_description": "Buy original Beesline Whitening Lifting Night Cream (50ml). Natural Royal Jelly & Lumiskin overnight whitening & firming cream. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["beesline", "beesline_night_cream", "lifting_cream", "whitening_cream", "ekleel_abha"]
        },
        "schema": {
            "brand": "Beesline",
            "category": "Skincare / Night Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "beesline-whitening-lifting-night-cream-50ml.webp",
            "alt": "Beesline Whitening Lifting Night Cream 50ml",
            "title": "Beesline Whitening Lifting Night Cream 50ml"
        }
    }

def create_product_1875():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مزيل عرق جفاف تام من بيزلين 50 مل (Beesline Total Dry Deodorant - 50ml)</strong> مزيل العرق الطبيعي الأيقوني الأكثر فاعلية لحماية منطقة الإبطين من العرق والروائح الكريهة مع تأمين جفاف تام وتفتيح آمن للبشرة لـ 48 ساعة. يرتكز هذا الرول اون الفاخر من بيزلين (Beesline Total Dry Whitening Roll-On Deodorant 50ml) على تكنولوجيا الشبة الطبيعية (Teflose® & Alum Rock)، صمغ النحل النقي (Propolis)، واللوميسكين المبيض (Lumiskin).</p>
<p>يعمل مزيل عرق بيزلين الجفاف التام على امتصاص العرق المفرط، القضاء على البكتيريا المسببة للرائحة الكريهة دون إغلاق المسام، وتفتيح اسمرار الإبطين ب فاعلية، ليترك منطقة الإبط جافة، ناصعة، ومعطرة بانتعاش لطيف طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>جفاف تام وحماية من العرق والروائح لـ 48 ساعة:</strong> يمتص الرطوبة الزائدة ويمنع تكون الروائح.</li>
  <li><strong>تفتيح آمن وتوحيد لون الإبطين:</strong> يزيل البقع الداكنة والتصبغات الناتجة عن الاحتكاك باللوميسكين.</li>
  <li><strong>تطهير بـ صمغ النحل الشافي (Propolis):</strong> يهدئ البشرة المتهيجة بعد الحلاقة ويحميها من البكتيريا.</li>
  <li><strong>خالي 100% من ألومنيوم كلوروهيدرات والكحول والبارابين:</strong> لا يسبب انسداد المسام أو حساسية الجلد.</li>
  <li><strong>رول اون بكرة دوارة سهلة الانزلاق:</strong> ينفذ بالبشرة فورياً دون ترك أثر بيضائي أو لزوجة على الملابس.</li>
  <li><strong>عبوة مدمجة سعة 50 مل:</strong> حجم ممتاز ومناسب للاستخدام اليومي وحمل الحقيبة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> نظفي منطقة الإبطين بالماء والصابون وجففيها جيداً قبل الاستعمال.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> مرري البكرة الدوارة لمزيل عرق بيزلين 1-2 مرة على بشرة الإبط الجافة.</li>
  <li><strong>الخطوة الثالثة (التجفيف):</strong> دعي الرول اون يجف لثوانٍ معدودة قبل ارتداء الملابس (يُستعمل مرة يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركب تيفلوز والشبة الطبيعية (Teflose® & Alum Rock):</strong> يقضيان على البكتيريا ويمتصان الرطوبة ب جفاف تام.</li>
  <li><strong>صمغ النحل واللوميسكين المبيض:</strong> يهدئان أنسجة الإبط ويفتحان التصبغات.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الإبطين الجافة فقط.</li>
  <li>لا يوضع على الجلد المصاب بجروح مفتوحة أو التهابات شديدة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من العرق المفرط واسمرار الإبطين ويفتش عن رول اون بيزلين الجفاف التام المبيض 50 مل.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / مزيلات العرق الرول اون المبيضة بالجفاف التام 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>مزيل عرق رول اون طبيعي مبيض ومؤمن للجفاف التام لـ 48 ساعة (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الإبطين (بما في ذلك البشرة الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>إبطين جافين تماماً، ناصعين، معطرين ونظيفين خاليين من التصبغات والروائح</td></tr>
  <tr><th>الملمس</th><td>سائل رول اون خفيف ينفذ فورياً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر بيزلين المنعش اللطيف الأيقوني</td></tr>
  <tr><th>المكونات النشطة</th><td>تيفلوز، شبة طبيعية، صمغ النحل، لوميسكين</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الشبة والتيفلوز في بيزلين الجفاف التام (Beesline Total Dry)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مزيل عرق بيزلين الجفاف التام مشكلة العرق المفرط، رائحة الإبط الكريهة، اسمرار وتصبغات الإبطين، والحكة بعد الحلاقة.</p>

<h3>لماذا تنجح تركيبة التيفلوز والشبة المبيضة؟</h3>
<p>لأن مركب Teflose يمنع التصاق البكتيريا المسببة للرائحة بالجلد، بينما تمتص الشبة العرق الطبيعي ويفتّح اللوميسكين البشرة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على بشرة جافة ونظيفة:</strong> ضعيه فور الاستحمام وتجفيف الإبطين جيداً.<br>
2. <strong>الانتظار 10 ثوانٍ قبل ارتداء الملابس:</strong> دعي السائل يجف لمنع التصبغ بالملابس.<br>
3. <strong>الاستخدام اليومي المنتظم:</strong> يضمن تفتيحاً ملحوظاً وجفافاً مستداماً لـ 48 ساعة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مزيلات العرق المؤقته للجفاف التام تسد مسام البشرة وتسبب ورم الغدد اللمفاوية."<br>
<strong>الحقيقة:</strong> رول اون بيزلين خالي من ألومنيوم كلوروهيدرات الحاد ولا يسد المسام إطلاقاً بل يمتص الرطوبة ب أمان.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يمنع Teflose تكون الغشاء الحيوي البكتيري (Biofilm) المحلل للعرق، فيوقف الرائحة دون تعطيل الغدد العرقية.</p>"""

    faqs = [
        ("ما هو مزيل عرق جفاف تام من بيزلين 50 مل؟", "هو مزيل عرق طبيعي رول اون من بيزلين يمنح جفافاً تاماً وحماية 48 ساعة وتفتيحاً آخاذاً للإبطين 50 مل."),
        ("ما هي فوائد الشبة والتيفلوز وصمغ النحل واللوميسكين؟", "تمتص الشبة والتيفلوز الرطوبة والروائح الكريهة، يهدئ صمغ النحل الجلد، ويفتّح اللوميسكين تصبغات الإبط."),
        ("هل يمنح جفافاً تاماً لـ 48 ساعة ويفتح الإبطين؟", "نعم، مثبت سريرياً في تأمين جفاف تام وتفتيح التصبغات لـ 48 ساعة كاملة."),
        ("ما حجم العبوة؟", "تأتي لعلبة رول اون بكرة دوارة سعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "مرري البكرة 1-2 مرة على بشرة الإبط النظيفة والجافة، دعي السائل يجف ثوانٍ قبل ارتداء الملابس يومياً."),
        ("هل هو خالي 100% من ألومنيوم كلوروهيدرات والبارابين والكحول؟", "نعم، خالي 100% من ألومنيوم كلوروهيدرات والكحول والبارابين وآمن للبشرة الحساسة."),
        ("ما هو بلد صنع مزيل عرق بيزلين؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين العالمية (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يترك أثراً أو بقعاً بيضاء أو صفراء على الملابس؟", "لا، قوام شفاف ينفذ فورياً دون ترك أي أثر على الملابس السوداء أو البيضاء."),
        ("ما هي رائحة مزيل عرق بيزلين الجفاف التام؟", "يتميز برائحة بيزلين المنعشة واللطيفة جداً."),
        ("هل يهدئ تهيج الإبطين بعد الحلاقة؟", "نعم، صمغ النحل والألوفيرا يهدئان التهابات البشرة بعد الحلاقة."),
        ("هل عبوة الرول اون 50 مل مناسبة للحقيبة؟", "نعم، حجم مدمج وأنيق مثالي لحمل الحقيبة والعمل والسفر."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعبوتها المغلقة محكماً."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع الفئات العمرية للنساء والرجال من سن 12 سنة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة رول اون أنيقة بغطاء محكم الحماية."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل مرة واحدة يومياً صباحاً أو بعد الاستحمام."),
        ("هل يمنع تكاثر البكتيريا المسببة للرائحة؟", "نعم، مركب Teflose يمنع نمو البكتيريا المحللة للعرق."),
        ("هل يناسب البشرة الحساسة جداً؟", "نعم، فورمولا خالية من المواد القاسية وآمنة للبشرة الحساسة."),
        ("هل هو مزيل العرق الأكثر شهرة وطلباً لبيزلين؟", "نعم، Total Dry Roll-On المزيل الأول والأكثر مبيعاً لبيزلين."),
        ("هل يمنح حس انتعاش وثقة طوال اليوم؟", "نعم، يضمن جفافاً وانتعاشاً وإبطين ناصعين طوال اليوم."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يمنع اسمرار الإبطين الناتج عن الاحتكاك؟", "نعم، اللوميسكين يفتح التصبغات ويمنع الاسمرار المستقبلي."),
        ("هل يترك الجلد طرياً؟", "نعم، يترك جلد الإبطين طرياً ومسترخياً."),
        ("هل تجف سريعا على البشرة؟", "نعم، يجف السائل خلال ثوانٍ معدودة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Total Dry Deodorant - 50ml</strong> (Beesline Total Dry Whitening Roll-On Deodorant) is the iconic natural roll-on deodorant engineered to deliver 48-hour total dryness, odor protection, and safe underarm whitening. Formulated by Beesline, it features Teflose®, natural Alum Rock, Propolis, and Lumiskin.</p>
<p>Beesline Total Dry Deodorant absorbs excess perspiration, neutralizes odor-causing bacteria without clogging pores, and lightens underarm hyperpigmentation, leaving your armpits touchably dry, brightened, and freshly fragranced all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>48-Hour Total Dryness & Anti-Odor Defense:</strong> Absorbs excess sweat moisture and stops odor formation.</li>
  <li><strong>Safe Underarm Whitening & Tone Unification:</strong> Fades dark underarm spots caused by friction and shaving.</li>
  <li><strong>Purifying Propolis Defense:</strong> Soothes post-shaving skin irritation and protects against bacteria.</li>
  <li><strong>100% Free of Aluminum Chlorohydrate, Alcohol & Parabens:</strong> Does not clog pores or cause skin irritation.</li>
  <li><strong>Smooth Gliding Ergonomic Roll-On:</strong> Penetrates instantly without leaving white marks or yellow clothing stains.</li>
  <li><strong>Compact 50ml Roll-On Bottle:</strong> Ideal handbag and travel size for continuous daily freshness.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse underarm skin thoroughly with soap and water and pat dry before application.</li>
  <li><strong>Step 2 (Apply):</strong> Roll the Beesline applicator 1 to 2 times over clean, dry underarm skin.</li>
  <li><strong>Step 3 (Dry):</strong> Allow fluid to dry for a few seconds before dressing (use once daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Teflose® & Natural Alum Rock:</strong> Neutralize odor-causing bacteria and absorb moisture for total dryness.</li>
  <li><strong>Propolis & Lumiskin:</strong> Soothe underarm dermal tissue and fade hyperpigmentation spots.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical dry underarm skin application only.</li>
  <li>Do not apply onto open wounds or severely irritated skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with heavy perspiration or dark underarms seeking Beesline's 50ml Total Dry Whitening Roll-On Deodorant.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Personal Care / Beesline Total Dry Whitening Roll-On Deodorants 50ml</td></tr>
  <tr><th>Product Type</th><td>48-Hour Total Dryness & Whitening Roll-On Deodorant (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Underarm Skin Types (Including Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Touchably dry, brightened, odor-free & clean armpits</td></tr>
  <tr><th>Texture</th><td>Smooth lightweight fast-drying roll-on fluid</td></tr>
  <tr><th>Fragrance</th><td>Fresh gentle classic Beesline aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Teflose®, Alum Rock, Propolis, Lumiskin</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Teflose Anti-Bacterial Biofilm Prevention & Alum Absorption</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Total Dry Deodorant resolves excessive underarm perspiration, body odor, dark underarm friction spots, and post-shaving irritation.</p>

<h3>Why choose Beesline Total Dry Deodorant?</h3>
<p>Teflose prevents odor-causing bacteria from adhering to skin, while Alum Rock absorbs perspiration without blocking sweat glands.</p>"""

    en_faqs = [
        ("What is Beesline Total Dry Deodorant - 50ml?", "It is a natural roll-on deodorant formulated with Teflose, Alum Rock, and Lumiskin to deliver 48-hour total dryness and underarm whitening."),
        ("What are the benefits of Teflose, Alum Rock, and Lumiskin?", "Teflose and Alum Rock eliminate odor and sweat moisture, while Lumiskin brightens dark underarm hyperpigmentation."),
        ("Does it deliver 48-hour total dryness and underarm whitening?", "Yes, clinically proven to provide 48-hour total dryness and visible underarm skin brightening."),
        ("What volume is contained in this roll-on bottle?", "It comes in a compact 50ml roll-on bottle."),
        ("How do I apply it correctly?", "Roll 1-2 times onto clean, dry underarm skin, allow to dry for a few seconds, and dress."),
        ("Is it 100% free of aluminum chlorohydrate, alcohol, and parabens?", "Yes, 100% free of aluminum chlorohydrate, alcohol, and parabens; safe for sensitive skin."),
        ("Where is Beesline Total Dry Deodorant manufactured?", "Proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it leave white marks or yellow stains on clothing?", "No, invisible fluid absorbs instantly without leaving marks on white or black clothes."),
        ("What scent does Beesline Total Dry Deodorant have?", "Features a fresh, subtle, gentle Beesline fragrance."),
        ("Does it soothe post-shaving underarm irritation?", "Yes, enriched with Propolis and Aloe Vera to calm irritation after shaving."),
        ("Is the 50ml roll-on handbag-friendly?", "Yes, compact roll-on bottle fits easily into purses, gym bags, and travel kits."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Is it suitable for men and women?", "Suitable for all age groups, both men and women aged 12+."),
        ("Is the roll-on bottle leak-proof?", "Yes, features a secure screw-top cap over the smooth roller ball."),
        ("How many times daily should I use it?", "Recommended for use once daily, morning or post-shower."),
        ("Does it stop odor-causing bacteria growth?", "Yes, Teflose prevents bacterial biofilm adhesion to halt odor formation."),
        ("Is it safe for extremely sensitive underarm skin?", "Yes, gentle formula free of harsh chemicals; safe for sensitive skin."),
        ("Is it Beesline's best-selling roll-on deodorant?", "Yes, Total Dry Whitening Roll-On is the #1 iconic deodorant by Beesline."),
        ("Does it provide all-day freshness confidence?", "Yes, guarantees complete dryness, fresh breath confidence, and brightened armpits."),
        ("Is the bottle recyclable?", "Yes, 100% recyclable environmentally friendly bottle."),
        ("Does it prevent underarm friction darkening?", "Yes, Lumiskin brightens existing spots and prevents future friction darkening."),
        ("Does it leave underarm skin touchably soft?", "Yes, leaves underarm skin touchably soft, smooth, and dry."),
        ("Does it dry quickly on skin?", "Yes, fluid dries in seconds for immediate dressing."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1875",
        "sku": "EK-1875",
        "gtin": "5281018088197",
        "category": "العناية الشخصية / مزيلات العرق الرول اون المبيضة بالجفاف التام 50ml",
        "brand": "Beesline",
        "ar": {
            "title": "مزيل عرق جفاف تام من بيزلين 50 مل",
            "meta_title": "مزيل عرق بيزلين جفاف تام 50مل | إكليل أبها",
            "meta_description": "اشتري مزيل عرق جفاف تام من بيزلين (50 مل). رول اون طبيعي بالشبة والتيفلوز لجفاف تام وتفتيح الإبطين 48 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بيزلين", "مزيل_عرق_بيزلين", "جفاف_تام", "تفتيح_الإبط", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Total Dry Deodorant - 50ml",
            "meta_title": "Beesline Total Dry Deodorant 50ml | Ekleel Abha",
            "meta_description": "Buy original Beesline Total Dry Deodorant (50ml). Natural Teflose & Alum Rock 48-hour total dry whitening roll-on. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["beesline", "beesline_deodorant", "total_dry", "whitening_deodorant", "ekleel_abha"]
        },
        "schema": {
            "brand": "Beesline",
            "category": "Personal Care / Deodorant",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "beesline-total-dry-deodorant-50ml.webp",
            "alt": "Beesline Total Dry Deodorant 50ml",
            "title": "Beesline Total Dry Deodorant 50ml"
        }
    }

print("Loaded all 5 Batch 32 builders complete")
