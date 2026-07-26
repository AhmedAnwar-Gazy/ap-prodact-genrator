import json, os
from build_batch93 import _make_guerlain_eyeliner_b93, _make_guerlain_concealer_b93

def create_product_2192():
    return _make_guerlain_eyeliner_b93(
        pid=2192, gtin="3346470421905",
        ar_title="قلم كحل تحديد العيون ديب بيربل مع براية  رقم (03)من جيرلان",
        en_title="Guerlain Deep Purple Eyeliner Pencil with Sharpener No. (03).",
        shade_num="03", shade_ar="ديب بيربل (أرجواني داكن)", shade_en="Deep Purple (03)",
        tags_ar=["جيرلان", "قلم_كحل_جيرلان_03_أرجواني", "كحل_جيرلان_مع_براية", "كحل_مقاوم_للماء", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_purple_eyeliner_03", "guerlain_pencil_sharpener", "waterproof_eyeliner", "ekleel_abha"]
    )

def create_product_2193():
    return _make_guerlain_eyeliner_b93(
        pid=2193, gtin="3346470421882",
        ar_title="قلم كحل تحديد العيون اسود مع براية  رقم (01)من جيرلان",
        en_title="Black eyeliner pencil with sharpener No. (01) from Guerlain",
        shade_num="01", shade_ar="أسود فاحم", shade_en="Black (01)",
        tags_ar=["جيرلان", "قلم_كحل_جيرلان_01_أسود", "كحل_جيرلان_مع_براية", "كحل_مقاوم_للماء", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_black_eyeliner_01", "guerlain_pencil_sharpener", "waterproof_eyeliner", "ekleel_abha"]
    )

def create_product_2194():
    return _make_guerlain_concealer_b93(
        pid=2194, gtin="3346470408753",
        ar_title="كونسيلر مضيء ومجدد الشفاه(01) من جيرلان",
        en_title="Illuminating and rejuvenating concealer (01) from Guerlain",
        shade_num="01", shade_ar="درجة 01", shade_en="Shade 01",
        tags_ar=["جيرلان", "كونسيلر_جيرلان_المضيء_01", "مجدد_الشفاه_جيرلان", "كونسيلر_بالذهب", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_precious_light_01", "guerlain_lip_concealer", "24k_gold_concealer", "ekleel_abha"]
    )

def create_product_2195():
    return _make_guerlain_concealer_b93(
        pid=2195, gtin="3346470408746",
        ar_title="كونسيلر مضيء ومجدد الشفاه(0 0) من جيرلان",
        en_title="Guerlain Illuminating and Lip Replenishing Concealer (00)",
        shade_num="00", shade_ar="درجة 00", shade_en="Shade 00",
        tags_ar=["جيرلان", "كونسيلر_جيرلان_المضيء_00", "مجدد_الشفاه_جيرلان", "كونسيلر_بالذهب", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_precious_light_00", "guerlain_lip_concealer", "24k_gold_concealer", "ekleel_abha"]
    )


def create_product_2196():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>برايمر ستيب ون من ميك اب فور ايفر(3) - 30مل (Make Up For Ever Step 1 Primer (3) - 30ml)</strong> البرايمر الطبي المعادل للون ومصحح الاحمرار والتهيجات الفاخر الأيقوني من ميك أب فور إيفر (Make Up For Ever Step 1 Primer Tone Neutralizer / Fresh Neutralizer) المصمم خصيصاً لتصحيح الاحمرار، توحيد لون بشرة الوجه المتهرجة، وإعدادها لاستقبال كريم الأساس بثبات يدوم 24 ساعة دون تكتل أو جفاف. يرتكز هذا البرايمر الفرنسي الأصيل (MUFE Step 1 Primer 3 30ml) على الصبغات الخضراء المصححة للاحمرار، حمض الهيالورونيك المرطب، ومجمع تنعيم المسام.</p>
<p>يعمل برايمر ميك أب فور إيفر ستيب 1 (درجة 3) على تحييد الاحمرار والشعيرات الدموية الظاهرة، ملء وتنعيم المسام والخطوط الدقيقة، وحفظ رطوبة أدمة الوجه، ليترك بشرتك ناعمة كالحرير، مرطبة، موحدة اللون، وجاهزة للمكياج وثابتة طوال اليوم من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تحييد الاحمرار وتصحيح لون البشرة المتهيجة (درجة 3):</strong> يمنح الوجه لوناً ناصع المتجانس.</li>
  <li><strong>تثبيت وإطالة عمر كريم الأساس لـ 24 ساعة:</strong> يمنع تكتل أو تلاشي المكياج.</li>
  <li><strong>إخفاء وتنعيم المسام والخطوط الدقيقة:</strong> يوفر سطحاً ناعماً كالحرير قبل الأساس.</li>
  <li><strong>ترطيب وتغذية فائقة بحمض الهيالورونيك:</strong> يحفظ الرطوبة الداخلية لـ 24 ساعة.</li>
  <li><strong>تركيبة خفيفة آمنة ومختبرة جلدياً:</strong> مناسبة للبشرة الحساسة والمصابة بالاحمرار.</li>
  <li><strong>أنبوب أنيق سعة 30 مل بحجم مالي ممتاز:</strong> تكفي للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية صغيرة من برايمر ميك أب فور إيفر على بشرة الوجه النظيفة والمرطبة.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي البرايمر بالأصابع أو الإسفنجة على مناطق الاحمرار (الخدين، الأنف، والذقن).</li>
  <li><strong>الخطوة الثالثة:</strong> اتركي البرايمر لمدة دقيقة واحدة ثم ضعي كريم الأساس المفضل لديك (يُستعمل daily قبل المكياج).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الصبغات الخضراء المصححة وحمض الهيالورونيك:</strong> تحايد الاحمرار وفق عجلة الألوان وتحبس رطوبة الجلد.</li>
  <li><strong>بوليمرات التثبيت والتنعيم:</strong> تنعم سطح البشرة وتمنع ثقل المكياج على المسام.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي التجميلي على بشرة الوجه والرقبة.</li>
  <li>تجنبي التلامس المباشر لداخل العين واغلقي الغطاء بإحكام.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن برايمر ستيب ون من ميك أب فور إيفر 3 لتصحيح الاحمرار وتثبيت المكياج لـ 24 ساعة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ميك أب فور إيفر (Make Up For Ever France)</td></tr>
  <tr><th>الفئة</th><td>مكياج الوجه / برايمرات ومصححات ميك أب فور إيفر ستيب 1 (30ml)</td></tr>
  <tr><th>نوع المنتج</th><td>برايمر ومصحح احمرار ولون الوجه بحمض الهيالورونيك تثبيت 24 ساعة (30ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>30 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (خصيصاً البشرة الحساسة والمصابة بالاحمرار والشعيرات)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، موحد اللون، خالي كلياً من الاحمرار ومجهز لمكياج 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>كريمي مائي خفيف خضر فاتح ينزلق ويمتص بسلاسة</td></tr>
  <tr><th>العطر</th><td>عطر الزهور والمسك الفرنسي اللطيف المحايد</td></tr>
  <tr><th>المكونات النشطة</th><td>صبغات خضراء مصححة للاحمرار، حمض الهيالورونيك، مجمع تنعيم المسام</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>LVMH Make Up For Ever France</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الصبغات الخضراء المصححة وحمض الهيالورونيك في برايمر ميك أب فور إيفر ستيب 1 (MUFE Step 1)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج برايمر ميك أب فور إيفر ستيب 1 (درجة 3) مشكلة احمرار الوجه، تهيج الشرايين الصغيرة، تلاشي المكياج، والمسام البارزة.</p>

<h3>لماذا تنجح تركيبة Make Up For Ever Step 1 Primer 3؟</h3>
<p>لأن الصبغة الخضراء تقع في المقابل المباشر للون الأحمر على عجلة الألوان فتحايده بينما ينعم الهيالورونيك المسام.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على مناطق الاحمرار والمسام:</strong> يضمن توحيد البشرة دون إثقال المناطق الجافة.<br>
2. <strong>الانتظار دقيقة قبل وضع كريم الأساس:</strong> يتيح للبرايمر الثبات وامتصاص الزيوت.<br>
3. <strong>التكميل بـ فاونديشن ميك أب فور إيفر:</strong> يضمن ثباتاً مطلقاً لـ 24 ساعة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "البرايمرات الخضراء تترك الوجه بلون أخصر غريب."<br>
<strong>الحقيقة:</strong> برايمر ميك أب فور إيفر يندمج بسلاسة ويتحول إلى لون شفاف حيادي يزيل الاحمرار كلياً.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تغيّر الصبغات الخضراء المجهرية الطول الموجي للضوء المنعكس عن احمرار الوجه مظهراً بشرة موحدة بيضاء.</p>"""

    faqs = [
        ("ما هو برايمر ستيب ون من ميك اب فور ايفر(3) - 30مل؟", "هو برايمر ومصحح احمرار ولون الوجه بحمض الهيالورونيك تثبيت 24 ساعة بدرجة 3 من ميك أب فور إيفر (30 مل)."),
        ("ما هي فوائد الصبغات الخضراء المصححة وحمض الهيالورونيك؟", "تحايد الاحمرار والتهيجات، تنعم المسام والخطوط، وتثبت كريم الأساس لـ 24 ساعة دون جفاف."),
        ("هل يحايد الاحمرار ويثبت المكياج لـ 24 ساعة بدون تكتل؟", "نعم، مثبت سريرياً في تحييد احمرار الوجه وتثبيت كريم الأساس 24 ساعة وتنعيم المسام."),
        ("ما حجم العبوة؟", "تأتي بأنبوب أنيق سعة 30 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على البشرة، وزعي على مناطق الاحمرار، انتظري دقيقة ثم ضعي كريم الأساس."),
        ("هل هو خالٍ من الزيوت وآمن للبشرة الحساسة؟", "نعم، 100% خالٍ من الزيوت الثقيلة ومختبر جلدياً ومناسب للبشرة الحساسة."),
        ("أين صُنع برايمر ميك أب فور إيفر؟", "صُنع في فرنسا بواسطة LVMH Make Up For Ever France."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات ميك أب فور إيفر لدى إكليل أبها أصلية 100%."),
        ("ما درجة برايمر ميك أب فور إيفر ستيب 1؟", "درجة 3 (Green Tone Neutralizer)."),
        ("هل يناسب البشرة المصابة بالاحمرار والشعيرات والمسام؟", "نعم، ممتاز للبشرة الحساسة والمصابة بالاحمرار والمسام الواسعة."),
        ("هل أنبوب 30 مل مريح ومناسب للاستخدام اليومي؟", "نعم، أنبوب أنيق ومريح جداً للاستخدام اليومي والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل ميك أب فور إيفر الماركة الأولى عالمياً في البرايمرات؟", "نعم، Make Up For Ever Step 1 البرايمر الاحترافي رقم 1 الأكثر تفضيلاً بجميع صالونات التجميل."),
        ("كم يدوم ثباته طوال اليوم؟", "يدوم لـ 24 ساعة متواصلة دون تلاشي أو تكتل."),
        ("هل ينشطف بمزيل المكياج بسهولة؟", "نعم، ينشطف بسلاسة بمزيل المكياج دون شد البشرة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع سيلان وتلاشي كريم الأساس؟", "نعم، يشكل درعاً يمنع امتصاص البشرة لكريم الأساس أو تكتله."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والفتيات؟", "نعم، ممتاز للنساء والفتيات."),
        ("هل يناسب جميع فصول السنة؟", "نعم، تصحيح وتثبيت مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن مكياج الوجه؟", "نعم، منتج فرنسي فاخر وأساسي لكل حقيبة تجميل."),
        ("هل يعيد المظهر المشرق الموحد للبشرة المتهرجة؟", "نعم، يمنح البشرة مظهراً موحداً وناصع النقاء كالحرير."),
        ("هل تتوفر درجات برايمر ميك أب فور إيفر ستيب 1 الأخرى؟", "نعم، تتوفر عائلة MUFE Step 1 Primers كاملة لدى إكليل أبها."),
        ("هل يمكن استخدامه بمفرده دون فاونديشن؟", "نعم، يمكن استخدامه بمفرده لتوحيد وتنعيم البشرة وإزالة الاحمرار."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Make Up For Ever Step 1 Primer (3) - 30ml</strong> is an authentic luxury redness-correcting, tone-neutralizing, and 24-hour face primer from professional House Make Up For Ever France (Make Up For Ever Step 1 Primer Tone Neutralizer / Fresh Neutralizer) designed to neutralize skin redness, unify flushed facial complexions, and prep skin for 24-hour foundation hold without creasing or dryness. Built upon green redness-correcting pigments, hydrating Hyaluronic Acid, and a pore-blurring complex.</p>
<p>Make Up For Ever Step 1 Primer (Shade 3) neutralizes redness and visible micro-capillaries, fills enlarged pores and fine lines, and locks in skin moisture, leaving your facial skin touchably silky soft, hydrated, even-toned, and perfectly prepared for 24-hour makeup from first stroke.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Redness Neutralization & Complexion Correction (Shade 3):</strong> Imparts an even, clear facial skin tone.</li>
  <li><strong>24-Hour Foundation Fixation & Wear Extension:</strong> Prevents makeup creasing, sliding, or fading.</li>
  <li><strong>Blurs & Smooths Enlarged Pores & Fine Lines:</strong> Creates a silky smooth canvas prior to foundation.</li>
  <li><strong>Intensive 24-Hour Hydration with Hyaluronic Acid:</strong> Preserves internal facial skin moisture.</li>
  <li><strong>Oil-Free & Dermatologically Tested Safe Formula:</strong> 100% safe for sensitive and red-plagued skin.</li>
  <li><strong>Sleek 30ml Tube Container:</strong> Outstanding value for daily professional face preppring.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a small amount of Make Up For Ever primer onto clean, moisturized facial skin.</li>
  <li><strong>Step 2:</strong> Spread primer with fingers or a sponge over redness-prone areas (cheeks, nose, and chin).</li>
  <li><strong>Step 3:</strong> Allow primer to set for 1 minute before applying your favorite foundation (use daily prior to makeup).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Green Neutralizing Pigments & Hyaluronic Acid:</strong> Offset redness on the color wheel while locking in moisture.</li>
  <li><strong>Smoothing & Fixing Polymers:</strong> Smooth skin texture and prevent heavy makeup from sinking into pores.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on facial and neck skin.</li>
  <li>Avoid direct contact inside eyes and cap tightly after use.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Make Up For Ever Step 1 Primer 3 for redness neutralization, pore smoothing, and 24-hour makeup hold.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Make Up For Ever (France)</td></tr>
  <tr><th>Category</th><td>Face Makeup / Make Up For Ever Step 1 Face Primers 30ml</td></tr>
  <tr><th>Product Type</th><td>24-Hour Redness-Neutralizing Hyaluronic Acid Face Primer (Shade 3)</td></tr>
  <tr><th>Volume/Weight</th><td>30 ml Tube</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Specifically Sensitive, Redness-Prone & Flushed Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, even-toned, redness-free & makeup-ready face</td></tr>
  <tr><th>Texture</th><td>Ultra-lightweight fast-absorbing pale green fluid cream</td></tr>
  <tr><th>Fragrance</th><td>100% Mild gentle French floral musk fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Green Neutralizing Pigments, Hyaluronic Acid, Pore-Blurring Complex</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>LVMH Make Up For Ever France</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Green Pigment Neutralization & Hyaluronic Moisture Matrix</h2>

<h3>What problem does this solve?</h3>
<p>Make Up For Ever Step 1 Primer 3 resolves facial redness, flushed skin, enlarged pores, foundation sliding, and dryness.</p>

<h3>Why choose Make Up For Ever Step 1 Primer 3?</h3>
<p>Green micro-pigments lie directly opposite red on the color wheel neutralizing flush while Hyaluronic Acid fills skin micro-lines.</p>"""

    en_faqs = [
        ("What is Make Up For Ever Step 1 Primer (3) - 30ml?", "It is a professional 24-hour redness-neutralizing face primer with Hyaluronic Acid from Make Up For Ever (Shade 3 / 30ml)."),
        ("What are the benefits of Green Neutralizing Pigments and Hyaluronic Acid?", "Neutralize redness, blur enlarged pores and fine lines, and extend foundation hold for 24 hours without dryness."),
        ("Does it neutralize redness and extend foundation hold for 24 hours?", "Yes, clinically proven to neutralize redness, smooth pores, and lock foundation for 24 hours."),
        ("What volume is contained in this tube?", "30ml sleek tube."),
        ("How do I use it correctly?", "Apply small amount to clean skin, spread over redness-prone areas, wait 1 minute and apply foundation."),
        ("Is it oil-free and safe for sensitive skin?", "Yes, 100% oil-free, dermatologically tested, and suitable for sensitive redness-prone skin."),
        ("Where is Make Up For Ever Primer manufactured?", "In France by LVMH Make Up For Ever France."),
        ("How do I verify authenticity at Ekleel Abha?", "All Make Up For Ever products at Ekleel Abha are 100% original."),
        ("What shade is Make Up For Ever Step 1 Primer?", "Shade 3 (Green Tone Neutralizer)."),
        ("Is it suitable for sensitive skin with capillaries and pores?", "Yes, excellent for sensitive skin, redness, visible capillaries, and enlarged pores."),
        ("Is the 30ml tube convenient for daily use?", "Yes, sleek tube ideal for daily professional use and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Make Up For Ever a #1 professional primer brand?", "Yes, Make Up For Ever Step 1 is the #1 trusted primer line in professional makeup studios."),
        ("How long does it hold during the day?", "Holds for 24 continuous hours without fading or creasing."),
        ("Does it remove easily with makeup remover?", "Yes, removes smoothly with makeup remover without tugging skin."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it prevent foundation sliding and creasing?", "Yes, forms a protective shield preventing foundation from sliding into pores."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and teens?", "Yes, suitable for both women and teens."),
        ("Is it good for all seasons?", "Yes, ideal redness correction for summer and winter routines."),
        ("Is it a nice makeup gift?", "Yes, an essential premier French luxury makeup prep gift."),
        ("Does it restore smooth even-toned skin?", "Yes, gives facial skin a healthy smooth even-toned look."),
        ("Are other Make Up For Ever Step 1 primer shades available?", "Yes, the full MUFE Step 1 Primer range is available at Ekleel Abha."),
        ("Can it be worn alone without foundation?", "Yes, can be worn alone to neutralize redness and smooth skin texture."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2196",
        "sku": "EK-2196",
        "gtin": "3548752073257",
        "brand": "Make Up For Ever",
        "ar": {
            "title": "برايمر ستيب ون من ميك اب فور ايفر(3) - 30مل",
            "meta_title": "برايمر ميك أب فور إيفر ستيب 1 (3) 30مل | إكليل أبها",
            "meta_description": "اشتري برايمر ستيب ون من ميك أب فور إيفر (3). برايمر فرنسي مصحح للاحمرار بحمض الهيالورونيك وتثبيت 24 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["ميك_أب_فور_إيفر", "برايمر_ميك_أب_فور_إيفر_3", "برايمر_تصحح_الاحمرار", "ستيب_ون_برايمر", "إكليل_أبها"]
        },
        "en": {
            "title": "Make Up For Ever Step 1 Primer (3) - 30ml",
            "meta_title": "Make Up For Ever Step 1 Primer 3 30ml | Ekleel Abha",
            "meta_description": "Buy original Make Up For Ever Step 1 Primer (3) (30ml). French luxury 24-hour redness-neutralizing Hyaluronic Acid face primer. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["make_up_for_ever", "mufe_step1_primer_3", "redness_neutralizing_primer", "face_primer", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 94 builders complete")
