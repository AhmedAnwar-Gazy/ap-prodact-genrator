import json, os

def _make_mufe_primer_b95(pid, gtin, ar_title, en_title, shade_num, shade_ar, shade_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_title}</strong> البرايمر الطبي المعادل للون ومصحح عيوب الوجه الفاخر الأيقوني من ميك أب فور إيفر (Make Up For Ever Step 1 Primer Tone Corrector / Mattifying / Hydrating) المصمم خصيصاً لتصحيح التضاد الصبغي، توحيد لون بشرة الوجه، وإعدادها لاستقبال كريم الأساس بثبات يدوم 24 ساعة دون تكتل أو جفاف. يرتكز هذا البرايمر الفرنسي الأصيل ({en_title}) على الصبغات الدقيقة الموجهة ({shade_ar})، حمض الهيالورونيك المرطب، ومجمع تنعيم المسام.</p>
<p>يعمل برايمر ميك أب فور إيفر ستيب 1 (درجة {shade_num}) على تحييد الشحوب أو التضاد الصبغي، ملء وتنعيم المسام والخطوط الدقيقة، وحفظ رطوبة أدمة الوجه، ليترك بشرتك ناعمة كالحرير، مرطبة، موحدة اللون بدرجة {shade_ar}، وجاهزة للمكياج وثابتة طوال اليوم من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>توحيد اللون وتصحيح العيوب (درجة {shade_num} - {shade_ar}):</strong> يمنح الوجه لوناً متجانساً ومشرقاً.</li>
  <li><strong>تثبيت وإطالة عمر كريم الأساس لـ 24 ساعة:</strong> يمنع تكتل أو تلاشي المكياج.</li>
  <li><strong>إخفاء وتنعيم المسام والخطوط الدقيقة:</strong> يوفر سطحاً ناعماً كالحرير قبل الأساس.</li>
  <li><strong>ترطيب وتغذية فائقة بحمض الهيالورونيك:</strong> يحفظ الرطوبة الداخلية لـ 24 ساعة.</li>
  <li><strong>تركيبة خفيفة آمنة ومختبرة جلدياً:</strong> مناسبة لجميع أنواع البشرة.</li>
  <li><strong>أنبوب أنيق سعة 30 مل بحجم مالي ممتاز:</strong> تكفي للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية صغيرة من برايمر ميك أب فور إيفر على بشرة الوجه النظيفة والمرطبة.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي البرايمر بالأصابع أو الإسفنجة على كامل الوجه أو المناطق المستهدفة.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركي البرايمر لمدة دقيقة واحدة ثم ضعي كريم الأساس المفضل لديك (يُستعمل daily قبل المكياج).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الصبغات المصححة وحمض الهيالورونيك:</strong> تحايد الشحوب وتصلح اللون وتحبس رطوبة الجلد.</li>
  <li><strong>بوليمرات التثبيت والتنعيم:</strong> تنعم سطح البشرة وتمنع ثقل المكياج على المسام.</li>
</ul>

<h2>تحذيرات وااحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي التجميلي على بشرة الوجه والرقبة.</li>
  <li>تجنبي التلامس المباشر لداخل العين واغلقي الغطاء بإحكام.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن {ar_title} لتصحيح وتوحيد لون البشرة وتثبيت المكياج لـ 24 ساعة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ميك أب فور إيفر (Make Up For Ever France)</td></tr>
  <tr><th>الفئة</th><td>مكياج الوجه / برايمرات ومصححات ميك أب فور إيفر ستيب 1 (30ml)</td></tr>
  <tr><th>نوع المنتج</th><td>برايمر ومصحح لون الوجه بحمض الهيالورونيك تثبيت 24 ساعة (درجة {shade_num})</td></tr>
  <tr><th>الحجم/الوزن</th><td>30 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (العادية، الجافة، الدهنية والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، موحد اللون بدرجة {shade_ar}، ومجهز لمكياج 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>كريمي مائي خفيف ينزلق ويمتص بسلاسة</td></tr>
  <tr><th>العطر</th><td>عطر الزهور والمسك الفرنسي اللطيف المحايد</td></tr>
  <tr><th>المكونات النشطة</th><td>صبغات دقيقة مصححة للون، حمض الهيالورونيك، مجمع تنعيم المسام</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>LVMH Make Up For Ever France</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد الصبغات المصححة وحمض الهيالورونيك في برايمر ميك أب فور إيفر ستيب 1 (MUFE Step 1 {shade_num})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج برايمر ميك أب فور إيفر ستيب 1 (درجة {shade_num}) مشكلة شحوب البشرة، عدم التوافق الصبغي، تلاشي المكياج، والمسام البارزة.</p>

<h3>لماذا تنجح تركيبة Make Up For Ever Step 1 Primer Shade {shade_num}؟</h3>
<p>لأن الصبغات الدقيقة الموجهة تحايد العيوب اللونية بينما ينعم الهيالورونيك المسام.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على البشرة النظيفة قبل الأساس:</strong> يضمن توحيد البشرة.<br>
2. <strong>الانتظار دقيقة قبل وضع كريم الأساس:</strong> يتيح للبرايمر الثبات وامتصاص الزيوت.<br>
3. <strong>التكميل بـ فاونديشن ميك أب فور إيفر:</strong> يضمن ثباتاً مطلقاً لـ 24 ساعة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "البرايمرات الملونة تجفف البشرة."<br>
<strong>الحقيقة:</strong> برايمر ميك أب فور إيفر مدعم بحمض الهيالورونيك لحفظ الرطوبة النسيجية بالجلد.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تغير الصبغات المجهرية الطول الموجي للضوء المنعكس عن الوجه مظهراً بشرة موحدة وناصعة.</p>"""

    faqs_data = [
        (f"ما هو {ar_title}؟", f"هو برايمر ومصحح لون الوجه بحمض الهيالورونيك تثبيت 24 ساعة بدرجة {shade_num} من ميك أب فور إيفر (30 مل)."),
        (f"ما هي فوائد الصبغات المصححة وحمض الهيالورونيك بدرجة {shade_num}؟", "توحد لون البشرة، تنعم المسام والخطوط، وتثبت كريم الأساس لـ 24 ساعة دون جفاف."),
        ("هل يصحح لون البشرة ويثبت المكياج لـ 24 ساعة بدون تكتل؟", "نعم، مثبت سريرياً في توحيد لون الوجه وتثبيت كريم الأساس 24 ساعة وتنعيم المسام."),
        ("ما حجم العبوة؟", "تأتي بأنبوب أنيق سعة 30 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على البشرة، وزعي على كامل الوجه، انتظري دقيقة ثم ضعي كريم الأساس."),
        ("هل هو آمن ومختبر جلدياً؟", "نعم، 100% آمن ومختبر جلدياً ومناسب لجميع أنواع البشرة."),
        ("أين صُنع برايمر ميك أب فور إيفر؟", "صُنع في فرنسا بواسطة LVMH Make Up For Ever France."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات ميك أب فور إيفر لدى إكليل أبها أصلية 100%."),
        (f"ما درجة برايمر ميك أب فور إيفر ستيب 1؟", f"درجة {shade_num} ({shade_ar})."),
        ("هل يناسب البشرة الجافة والدهنية والمختلطة والمسام؟", "نعم، ممتاز لجميع أنواع البشرة وتغطية المسام الواسعة."),
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
        (f"هل يعيد المظهر المشرق الموحد للبشرة بدرجة {shade_num}؟", f"نعم، يمنح البشرة مظهراً موحداً وناصع النقاء كالحرير."),
        ("هل تتوفر درجات برايمر ميك أب فور إيفر ستيب 1 الأخرى؟", "نعم، تتوفر عائلة MUFE Step 1 Primers كاملة لدى إكليل أبها."),
        ("هل يمكن استخدامه بمفرده دون فاونديشن؟", "نعم، يمكن استخدامه بمفرده لتوحيد وتنعيم البشرة وتعديل اللمعان."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury tone-correcting, complexion-unifying, and 24-hour face primer from professional House Make Up For Ever France (Make Up For Ever Step 1 Primer Tone Corrector) designed to neutralize skin discoloration, unify dull facial complexions, and prep skin for 24-hour foundation hold without creasing or dryness. Built upon color-correcting micro-pigments ({shade_en}), hydrating Hyaluronic Acid, and a pore-blurring complex.</p>
<p>Make Up For Ever Step 1 Primer (Shade {shade_num}) neutralizes sallowness and uneven skin tones, fills enlarged pores and fine lines, and locks in skin moisture, leaving your facial skin touchably silky soft, hydrated, even-toned in {shade_en}, and perfectly prepared for 24-hour makeup from first stroke.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Tone Correction & Complexion Unification (Shade {shade_num} - {shade_en}):</strong> Imparts an even, bright facial skin tone.</li>
  <li><strong>24-Hour Foundation Fixation & Wear Extension:</strong> Prevents makeup creasing, sliding, or fading.</li>
  <li><strong>Blurs & Smooths Enlarged Pores & Fine Lines:</strong> Creates a silky smooth canvas prior to foundation.</li>
  <li><strong>Intensive 24-Hour Hydration with Hyaluronic Acid:</strong> Preserves internal facial skin moisture.</li>
  <li><strong>Dermatologically Tested Safe Formula:</strong> 100% safe for all facial skin types.</li>
  <li><strong>Sleek 30ml Tube Container:</strong> Outstanding value for daily professional face prepping.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a small amount of Make Up For Ever primer onto clean, moisturized facial skin.</li>
  <li><strong>Step 2:</strong> Spread primer with fingers or a sponge over the entire face or targeted areas.</li>
  <li><strong>Step 3:</strong> Allow primer to set for 1 minute before applying your favorite foundation (use daily prior to makeup).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Color Correcting Pigments & Hyaluronic Acid:</strong> Offset sallowness while locking in skin moisture.</li>
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
  <li>Anyone seeking {en_title} for tone correction, pore smoothing, and 24-hour makeup hold.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Make Up For Ever (France)</td></tr>
  <tr><th>Category</th><td>Face Makeup / Make Up For Ever Step 1 Face Primers 30ml</td></tr>
  <tr><th>Product Type</th><td>24-Hour Tone-Correcting Hyaluronic Acid Face Primer (Shade {shade_num})</td></tr>
  <tr><th>Volume/Weight</th><td>30 ml Tube</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Normal, Dry, Oily & Combination Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, even-toned in {shade_en} & makeup-ready face</td></tr>
  <tr><th>Texture</th><td>Ultra-lightweight fast-absorbing fluid cream</td></tr>
  <tr><th>Fragrance</th><td>100% Mild gentle French floral musk fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Color-Correcting Pigments, Hyaluronic Acid, Pore-Blurring Complex</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>LVMH Make Up For Ever France</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Color Correcting Pigments & Hyaluronic Moisture Matrix</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves dull facial skin tone, uneven pigmentation, enlarged pores, foundation sliding, and dryness.</p>

<h3>Why choose Make Up For Ever Step 1 Primer {shade_num}?</h3>
<p>Color-correcting micro-pigments neutralize sallowness while Hyaluronic Acid fills skin micro-lines.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a professional 24-hour tone-correcting face primer with Hyaluronic Acid from Make Up For Ever (Shade {shade_num} / 30ml)."),
        (f"What are the benefits of Color Correcting Pigments and Hyaluronic Acid in Shade {shade_num}?", "Neutralize sallowness, blur enlarged pores and fine lines, and extend foundation hold for 24 hours without dryness."),
        ("Does it correct skin tone and extend foundation hold for 24 hours?", "Yes, clinically proven to neutralize tone imperfections, smooth pores, and lock foundation for 24 hours."),
        ("What volume is contained in this tube?", "30ml sleek tube."),
        ("How do I use it correctly?", "Apply small amount to clean skin, spread over face, wait 1 minute and apply foundation."),
        ("Is it safe and dermatologically tested?", "Yes, 100% safe, dermatologically tested, and suitable for all facial skin types."),
        ("Where is Make Up For Ever Primer manufactured?", "In France by LVMH Make Up For Ever France."),
        ("How do I verify authenticity at Ekleel Abha?", "All Make Up For Ever products at Ekleel Abha are 100% original."),
        (f"What shade is Make Up For Ever Step 1 Primer?", f"Shade {shade_num} ({shade_en})."),
        ("Is it suitable for dry, oily, and combination skin?", "Yes, excellent for all skin types and blurring enlarged pores."),
        ("Is the 30ml tube convenient for daily use?", "Yes, sleek tube ideal for daily professional use and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Make Up For Ever a #1 professional primer brand?", "Yes, Make Up For Ever Step 1 is the #1 trusted primer line in professional makeup studios."),
        ("How long does it hold during the day?", "Holds for 24 continuous hours without fading or creasing."),
        ("Does it remove easily with makeup remover?", "Yes, removes smoothly with makeup remover without tugging skin."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it prevent foundation sliding and creasing?", "Yes, forms a protective shield preventing foundation from sliding into pores."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and teens?", "Yes, suitable for both women and teens."),
        ("Is it good for all seasons?", "Yes, ideal tone correction for summer and winter routines."),
        ("Is it a nice makeup gift?", "Yes, an essential premier French luxury makeup prep gift."),
        (f"Does it restore smooth even-toned skin in Shade {shade_num}?", f"Yes, gives facial skin a healthy smooth even-toned look."),
        ("Are other Make Up For Ever Step 1 primer shades available?", "Yes, the full MUFE Step 1 Primer range is available at Ekleel Abha."),
        ("Can it be worn alone without foundation?", "Yes, can be worn alone to neutralize tone imperfections and smooth skin texture."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Make Up For Ever",
        "ar": {
            "title": ar_title,
            "meta_title": f"{ar_title} | إكليل أبها",
            "meta_description": f"اشتري {ar_title}. برايمر فرنسي مصحح للون البشرة بحمض الهيالورونيك وتثبيت 24 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. French luxury 24-hour tone-correcting Hyaluronic Acid face primer. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2197():
    return _make_mufe_primer_b95(
        pid=2197, gtin="3548752073325",
        ar_title="برايمر ستيب ون من ميك اب فور ايفر(10) - 30مل",
        en_title="MAKE UP FOR EVER Step 1 Primer (10) - 30ml",
        shade_num="10", shade_ar="درجة 10 (مصحح التوهج الصفراني)", shade_en="Shade 10 (Yellow Illuminator)",
        tags_ar=["ميك_أب_فور_إيفر", "برايمر_ميك_أب_فور_إيفر_10", "برايمر_تعديل_اللون", "ستيب_ون_برايمر", "إكليل_أبها"],
        tags_en=["make_up_for_ever", "mufe_step1_primer_10", "yellow_tone_primer", "face_primer", "ekleel_abha"]
    )


def create_product_2198():
    return _make_mufe_primer_b95(
        pid=2198, gtin="3548752073301",
        ar_title="برايمر ستيب ون من ميك اب فور ايفر(8) - 30مل",
        en_title="Make Up For Ever Step 1 Primer (8) - 30ml",
        shade_num="8", shade_ar="درجة 8 (مصحح الشحوب الداكن)", shade_en="Shade 8 (Peach Corrector)",
        tags_ar=["ميك_أب_فور_إيفر", "برايمر_ميك_أب_فور_إيفر_8", "برايمر_تعديل_اللون", "ستيب_ون_برايمر", "إكليل_أبها"],
        tags_en=["make_up_for_ever", "mufe_step1_primer_8", "peach_tone_primer", "face_primer", "ekleel_abha"]
    )


def create_product_2199():
    return _make_mufe_primer_b95(
        pid=2199, gtin="3548752073318",
        ar_title="برايمر ستيب ون من ميك اب فور ايفر(4) - 30مل",
        en_title="Make Up For Ever Step One Primer (4) - 30 ml",
        shade_num="4", shade_ar="درجة 4 (مصحح الشحوب الباهت)", shade_en="Shade 4 (Caramel Corrector)",
        tags_ar=["ميك_أب_فور_إيفر", "برايمر_ميك_أب_فور_إيفر_4", "برايمر_تعديل_اللون", "ستيب_ون_برايمر", "إكليل_أبها"],
        tags_en=["make_up_for_ever", "mufe_step1_primer_4", "caramel_tone_primer", "face_primer", "ekleel_abha"]
    )


def create_product_2200():
    return _make_mufe_primer_b95(
        pid=2200, gtin="3548752073264",
        ar_title="برايمر ستيب ون من ميك اب فور ايفر(9) - 30مل",
        en_title="Make Up For Ever (9) Step One Primer - 30 ml",
        shade_num="9", shade_ar="درجة 9 (مصحح الأصفرار الحاد)", shade_en="Shade 9 (Blue Illuminator)",
        tags_ar=["ميك_أب_فور_إيفر", "برايمر_ميك_أب_فور_إيفر_9", "برايمر_تعديل_اللون", "ستيب_ون_برايمر", "إكليل_أبها"],
        tags_en=["make_up_for_ever", "mufe_step1_primer_9", "blue_tone_primer", "face_primer", "ekleel_abha"]
    )


def create_product_2201():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم أساس ميك أب فور بيج ناعم (Y436)30مل (Make Up For Beige Smooth Foundation (Y436) 30ml)</strong> كريم الأساس الفاخر الأسطوري عالي التغطية المخملية غير المرئية من الدار الفرنسية المحترفة ميك أب فور إيفر (Make Up For Ever HD Skin / Ultra HD Foundation Y436 Warm Beige) المصمم لمنح بشرة وجهك تغطية طبيعية فائقة النعومة، إخفاء العيوب 100%، وتوحيد لون ناصع بدرجة بيج ناعم دافئ (Y436) ممتد لـ 24 ساعة دون تكتل أو جفاف. يرتكز هذا المستحضر الفرنسي الأصيل (MUFE Y436 30ml) على تقنية Micro-Skin Sync، حمض الهيالورونيك، وصبغات الكاميرا الدقيقة high-definition.</p>
<p>يعمل كريم أساس ميك أب فور إيفر Y436 على التكيف الفوري مع حركات وجهك وتعبيراته، إخفاء التصبغات والمسام والخطوط الدقيقة كلياً، وتزويد خلايا الوجه بالرطوبة والنعومة الحريرية، ليترك بشرتك ناعمة كالحرير، موحدة اللون بدرجة بيج ناعم، ومفعمة بالشباب والإشراق أمام الكاميرا والعين المباشرة من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تغطية مخملية فائقة غير مرئية أمام الكاميرا (درجة Y436):</strong> توحد الوجه وتخفي التصبغات.</li>
  <li><strong>ثبات عالي لـ 24 ساعة مقاوم للماء، العرق، والتلطخ:</strong> لا يتغير اللون أو يتكتل بالمسام.</li>
  <li><strong>ترطيب وتغذية فائقة بحمض الهيالورونيك:</strong> يحفظ طراوة ونعومة البشرة طوال اليوم.</li>
  <li><strong>ملمس خفيف سائل يندمج ويمتص بسلاسة:</strong> يمنح شعوراً خفيفاً بدون ثقل.</li>
  <li><strong>مختبر درماتولوجياً وآمن 100% لجميع أنواع البشرة:</strong> مناسب للبشرة الحساسة.</li>
  <li><strong>زجاجة فاخرة أيقونية بضاغط مريح سعة 30 مل:</strong> قمة الاحترافية الفرنسية في كريمات الأساس.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي بضع قطرات من كريم أساس ميك أب فور إيفر Y436 على بشرة الوجه النظيفة والمرطبة.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي الكريم من منتصف الوجه للخارج باستخدام الإسفنجة أو فرشاة الأساس المخصصة.</li>
  <li><strong>الخطوة الثالثة:</strong> ادمجي برفق للحصول على تغطية متجانسة ومشرقة (يُستعمل يومياً وعند المكياج).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>صبغات الكاميرا الدقيقة Micro-Skin Pigments & Hyaluronic Acid:</strong> تضمن تغطية مثالية غير مرئية وتمنع الجفاف.</li>
  <li><strong>بوليمرات التثبيت المرنة:</strong> تتكيف مع تعبيرات الوجه لمنع التكتل والتشقق بالخطوط.</li>
</ul>

<h2>تحذيرات وااحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي التجميلي على بشرة الوجه والرقبة.</li>
  <li>تجنبي التلامس المباشر لداخل العين واغلقي الغطاء بإحكام.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن كريم أساس ميك أب فور إيفر Y436 لتغطية وتوحيد وإشراقة الوجه المخملية لـ 24 ساعة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ميك أب فور إيفر (Make Up For Ever France)</td></tr>
  <tr><th>الفئة</th><td>مكياج الوجه / كريمات أساس ميك أب فور إيفر الفاخرة HD 30ml</td></tr>
  <tr><th>نوع المنتج</th><td>كريم أساس احترافي عالي التغطية المخملية بحمض الهيالورونيك (درجة Y436 Warm Beige)</td></tr>
  <tr><th>الحجم/الوزن</th><td>30 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (العادية، الجافة، الدهنية والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، موحد اللون بدرجة بيج ناعم Y436، مخملي وغير مرئي للكاميرا</td></tr>
  <tr><th>الملمس</th><td>سائل دسم خفيف ينساب ويمتص بسلاسة</td></tr>
  <tr><th>العطر</th><td>عطر الزهور والمسك الفرنسي الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>صبغات الكاميرا الدقيقة، حمض الهيالورونيك، بوليمرات المرونة المائية</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>LVMH Make Up For Ever France</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون (من 18 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد تقنية Micro-Skin Sync في كريم أساس ميك أب فور إيفر (MUFE HD Skin Y436)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم أساس ميك أب فور إيفر بدرجة Y436 مشكلة عدم توحد لون الوجه، ظهور العيوب أمام الكاميرات، تكتل المكياج بالخطوط، والبهتان.</p>

<h3>لماذا تنجح تركيبة Make Up For Ever HD Skin Y436؟</h3>
<p>لأن صبغات الكاميرا المجهرية تتكيف مع حركات الجلد وتمنع التكتل بينما يحافظ الهيالورونيك على المرونة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على بشرة مرطبة بـ برايمر ميك أب فور إيفر:</strong> يضمن توزيعاً مخملياً متجانساً.<br>
2. <strong>الدمج من المنتصف باتجاه الأطراف:</strong> يمنح تغطية طبيعية غير متكتلة.<br>
3. <strong>التثبيت بـ بودرة شفافة عند الحاجة:</strong> يديم التغطية طوال اليوم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات الأساس الاحترافية تبدو كالقناع السميك بالضوء الطبيعي."<br>
<strong>الحقيقة:</strong> كريم أساس ميك أب فور إيفر مصمم بصبغات مجهرية تندمج مع البشرة كطبقة جلد ثانية ناعمة كالحرير.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تندمج بوليمرات Micro-Skin مع تعبيرات الوجه دون تشقق بالخطوط وتوفر تغطية 100% للعيوب.</p>"""

    faqs = [
        ("ما هو كريم أساس ميك أب فور بيج ناعم (Y436)30مل؟", "هو كريم أساس احترافي عالي التغطية المخملية بحمض الهيالورونيك بدرجة Y436 البيج الناعم من ميك أب فور إيفر (30 مل)."),
        ("ما هي فوائد صبغات الكاميرا الدقيقة وحمض الهيالورونيك بدرجة Y436؟", "توحد لون البشرة، تخفي العيوب والتصبغات كلياً، وتمنح ترطيباً وتغطية مخملية غير مرئية لـ 24 ساعة."),
        ("هل يغطي العيوب ويوحد الوجه ويرطب لـ 24 ساعة بدون تكتل؟", "نعم، مثبت سريرياً في توحيد الوجه وتغطية العيوب وتوفير ترطيب وتغطية خالية من التكتل."),
        ("ما حجم العبوة؟", "تأتي بزجاجة أنيقة فاخرة بضاغط سعة 30 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي قطرات على البشرة والمرطب، وزعي بالإسفنجة أو الفرشاة واددمجي من المنتصف للخارج."),
        ("هل هو آمن ومختبر درماتولوجياً؟", "نعم، 100% آمن ومختبر درماتولوجياً ومناسب لجميع أنواع البشرة."),
        ("أين صُنع كريم أساس ميك أب فور إيفر؟", "صُنع في فرنسا بواسطة LVMH Make Up For Ever France."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات ميك أب فور إيفر لدى إكليل أبها أصلية 100%."),
        ("ما درجة كريم أساس ميك أب فور إيفر؟", "درجة Y436 (Warm Beige / بيج ناعم دافئ)."),
        ("هل يناسب البشرة الجافة والدهنية والمختلطة؟", "نعم، ممتاز لجميع أنواع البشرة وتوحيد لون الوجه."),
        ("هل زجاجة 30 مل الفاخرة مريحة وموفرة؟", "نعم، زجاجة فاخرة أيقونية بضاغط مريح جداً للاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل ميك أب فور إيفر الماركة الفرنسية الأولى في كريمات الأساس؟", "نعم، Make Up For Ever الماركة الفرنسية رقم 1 الأكثر شهرة وتفضيلاً بعالم مكياج الوجه الاحترافي."),
        ("كم يدوم ثباته طوال اليوم؟", "يدوم لـ 24 ساعة متواصلة دون تكتل أو تغير باللون."),
        ("هل ينشطف بمزيل المكياج بسهولة؟", "نعم، ينشطف بسلاسة بمزيل المكياج دون شد البشرة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يخفي المسام والخطوط الدقيقة؟", "نعم، ينعم البشرة ويخفي المسام والخطوط الدقيقة بفاعلية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والفتيات؟", "نعم، ممتاز للنساء والفتيات."),
        ("هل يناسب المناسبات والتصوير والمكياج اليومي؟", "نعم، ممتاز للمكياج اليومي والتصوير عالي الدقة."),
        ("هل يصلح هدية ممتازة ضمن مكياج الوجه؟", "نعم، منتج مكياج فرنسي فاخر وأساسي لكل امرأة راقية."),
        ("هل يعيد المظهر المشرق والساحر للوجه بدرجة Y436؟", "نعم، يمنح الوجه مظهراً موحداً ومخملي النقاء كالحرير."),
        ("هل تتوفر درجات كريم أساس ميك أب فور إيفر الأخرى؟", "نعم، تتوفر عائلة Make Up For Ever Foundations كاملة لدى إكليل أبها."),
        ("هل يحمي من التأثيرات البيئية؟", "نعم، مدعم بمضادات الأكسدة التي تحمي البشرة أثناء النهار."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Make Up For Beige Smooth Foundation (Y436) 30ml</strong> is an authentic luxury high-coverage invisible HD liquid foundation from professional House Make Up For Ever France (Make Up For Ever HD Skin / Ultra HD Foundation Y436 Warm Beige) designed to deliver ultra-smooth natural velvet coverage, 100% blemish concealment, and a 24-hour even warm beige complexion (Shade Y436) without creasing or drying. Built upon Micro-Skin Sync technology, hydrating Hyaluronic Acid, and high-definition micro-camera pigments.</p>
<p>Make Up For Ever Foundation Y436 smoothly adapts to facial expressions, conceals hyperpigmentation, enlarged pores, and fine lines, while infusing skin cells with moisture and silky softness, leaving your face touchably silky soft, beautifully even-toned in warm beige Y436, and camera-ready radiant from first stroke.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Camera-Invisible High Velvet Coverage (Shade Y436):</strong> Evens face and conceals spots.</li>
  <li><strong>24-Hour Waterproof, Sweat-Proof & Smudge-Proof Hold:</strong> Color does not shift or cake.</li>
  <li><strong>Intensive 24-Hour Hydration with Hyaluronic Acid:</strong> Preserves skin softness all day long.</li>
  <li><strong>Lightweight Fluid Liquid Glides Effortlessly:</strong> Blends without heavy weight.</li>
  <li><strong>Dermatologically Tested Safe for All Skin Types:</strong> 100% safe for sensitive facial skin.</li>
  <li><strong>Iconic 30ml Luxury Pump Dispenser Bottle:</strong> The pinnacle of professional French foundation design.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a few drops of Make Up For Ever foundation Y436 onto clean, moisturized skin.</li>
  <li><strong>Step 2:</strong> Smooth from center of face outwards using a makeup sponge or foundation brush.</li>
  <li><strong>Step 3:</strong> Blend gently for a flawless illuminated finish (use daily with makeup routines).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Micro-Skin Camera Pigments & Hyaluronic Acid:</strong> Guarantee flawless invisible coverage and prevent dryness.</li>
  <li><strong>Flexible Fixing Polymers:</strong> Adapt to facial movements preventing creasing in lines.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on facial and neck skin.</li>
  <li>Avoid direct contact inside eyes and cap tightly after use.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Make Up For Ever Foundation Y436 for camera-invisible velvet coverage, tone evening, and 24-hour hydration.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Make Up For Ever (France)</td></tr>
  <tr><th>Category</th><td>Face Makeup / Make Up For Ever Luxury HD Foundations 30ml</td></tr>
  <tr><th>Product Type</th><td>Professional High-Coverage Hyaluronic Acid Foundation (Shade Y436 Warm Beige)</td></tr>
  <tr><th>Volume/Weight</th><td>30 ml Pump Bottle</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Normal, Dry, Oily & Combination Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, even-toned in Y436 warm beige & camera-invisible velvet face</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-heavy fluid liquid foundation</td></tr>
  <tr><th>Fragrance</th><td>100% Luxurious French floral musk fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Micro-Skin Pigments, Hyaluronic Acid, Flexible Polymers</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>LVMH Make Up For Ever France</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 18+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Micro-Skin Sync Technology & HD Pigment Integration</h2>

<h3>What problem does this solve?</h3>
<p>Make Up For Ever Foundation Y436 resolves uneven facial skin tone, flash-photography flashback, foundation creasing in lines, and skin dullness.</p>

<h3>Why choose Make Up For Ever HD Skin Y436?</h3>
<p>Micro-skin pigments flex with facial movement preventing cakeiness while Hyaluronic Acid locks in skin hydration.</p>"""

    en_faqs = [
        ("What is Make Up For Beige Smooth Foundation (Y436) 30ml?", "It is a professional high-coverage Hyaluronic Acid liquid foundation from Make Up For Ever in Shade Y436 Warm Beige (30ml)."),
        ("What are the benefits of Micro-Skin Pigments and Hyaluronic Acid in Shade Y436?", "Even skin tone, conceal blemishes, and deliver 24-hour hydration and camera-invisible velvet coverage."),
        ("Does it conceal imperfections and hydrate for 24 hours without creasing?", "Yes, clinically proven to even skin tone, conceal blemishes, and deliver 24-hour hydration without creasing."),
        ("What volume is contained in this bottle?", "30ml iconic luxury pump bottle."),
        ("How do I use it correctly?", "Apply drops to moisturized skin, smooth with brush or sponge from center outwards."),
        ("Is it safe and dermatologically tested?", "Yes, 100% safe, dermatologically tested, and suitable for all facial skin types."),
        ("Where is Make Up For Ever Foundation manufactured?", "In France by LVMH Make Up For Ever France."),
        ("How do I verify authenticity at Ekleel Abha?", "All Make Up For Ever products at Ekleel Abha are 100% original."),
        ("What shade is Make Up For Ever Foundation?", "Shade Y436 (Warm Beige)."),
        ("Is it suitable for dry, oily, and combination skin?", "Yes, excellent for all skin types and flawless tone evening."),
        ("Is the 30ml pump bottle convenient for daily makeup?", "Yes, 30ml sleek pump dispenser bottle ideal for daily luxury makeup."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Make Up For Ever a #1 French luxury foundation brand?", "Yes, Make Up For Ever is the #1 trusted professional French foundation house."),
        ("How long does it hold during the day?", "Holds for 24 continuous hours without creasing or color shifting."),
        ("Does it remove easily with makeup remover?", "Yes, removes smoothly with makeup remover without tugging skin."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it blur pores and fine lines?", "Yes, effectively blurs enlarged pores and fine lines."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and teens?", "Yes, suitable for both women and teens."),
        ("Is it good for HD photography and daily wear?", "Yes, ideal for daily luxury wear, photoshoots, and HD video."),
        ("Is it a nice makeup gift?", "Yes, an essential premier French luxury foundation gift."),
        ("Does it restore smooth radiant skin in Shade Y436?", "Yes, gives facial skin an even-toned warm beige radiant look."),
        ("Are other Make Up For Ever foundation shades available?", "Yes, the full MUFE Foundation shade range is available at Ekleel Abha."),
        ("Does it protect against environmental stressors?", "Yes, enriched with antioxidants protecting skin throughout the day."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2201",
        "sku": "EK-2201",
        "gtin": "3548752165297",
        "brand": "Make Up For Ever",
        "ar": {
            "title": "كريم أساس ميك أب فور بيج ناعم (Y436)30مل",
            "meta_title": "كريم أساس ميك أب فور إيفر Y436 30مل | إكليل أبها",
            "meta_description": "اشتري كريم أساس ميك أب فور بيج ناعم (Y436) (30مل). كريم أساس فرنسي احترافي عالي التغطية المخملية بحمض الهيالورونيك. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["ميك_أب_فور_إيفر", "كريم_أساس_ميك_أب_فور_إيفر_Y436", "فاونديشن_ميك_أب_فور_إيفر", "كريم_أساس_احترافي", "إكليل_أبها"]
        },
        "en": {
            "title": "Make Up For Beige Smooth Foundation (Y436) 30ml",
            "meta_title": "Make Up For Ever Foundation Y436 30ml | Ekleel Abha",
            "meta_description": "Buy original Make Up For Beige Smooth Foundation (Y436) (30ml). French luxury 24-hour high-coverage Hyaluronic Acid liquid foundation. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["make_up_for_ever", "mufe_foundation_y436", "mufe_hd_skin", "liquid_foundation", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 95 builders complete")
