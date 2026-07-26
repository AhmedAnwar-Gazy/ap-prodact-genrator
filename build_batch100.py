import json, os

def _make_guerlain_lipstick_b100(pid, gtin, ar_title, en_title, shade_code, shade_ar, shade_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_title}</strong> أحمر الشفاه الفاخر الأسطوري غني الترطيب واللون الناصع من الدار الفرنسية العريقة جيرلان (Guerlain KissKiss / Rouge G Lipstick - {shade_code}) المصمم لمنح شفاهك صبغة مخملية حريرية مكثفة، امتلاءً جذاباً، وترطيباً عميقاً يدوم 24 ساعة دون جفاف أو تشقق. يرتكز هذا المستحضر الفرنسي الأصيل ({en_title}) على كرات حمض الهيالورونيك الفائقة الترطيب، زيت المانجو النقي، ومركب حماية الشفاه.</p>
<p>يعمل أحمر شفاه جيرلان بدرجة {shade_code} على تغليف الشفاه بلون {shade_ar} غني، ملء الخطوط الدقيقة للشفاه، وتزويد خلايا الشفاه برطوبة مخملية تجعل الشفاه أكثر امتلاءً ونعومة كالحرير من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>صبغة ناصعة غنية وترطيب مكثف للشفاه ({shade_code} - {shade_ar}):</strong> لون فاخر يدوم طويلاً.</li>
  <li><strong>امتلاء وتنعيم خطوط الشفاه بكرات حمض الهيالورونيك:</strong> مظهر أكثر حجماً وجاذبية.</li>
  <li><strong>تغذية فائقة بزيت المانجو الطبيعي:</strong> يمنع تشقق وجفاف الشفاه طوال اليوم.</li>
  <li><strong>ملمس كريمي ناعم ينزلق بسهولة دون تكتل:</strong> يمنح شعوراً خفيفاً مريحاً.</li>
  <li><strong>مختبر درماتولوجياً وآمن 100% لبشرة الشفاه الحساسة:</strong> خالي من المكونات الضارة.</li>
  <li><strong>عبوة أنيقة فاخرة بحجم 3.5 جم:</strong> قمة الفخامة الفرنسية في أحمر الشفاه.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> وزعي أحمر شفاه جيرلان مباشرة من العبوة أو باستخدام فرشاة الشفاه.</li>
  <li><strong>الخطوة الثانية:</strong> ابدئي من منتصف الشفة العلوية واتجهي نحو الزوايا الخارجية.</li>
  <li><strong>الخطوة الثالثة:</strong> كرري على الشفة السفلية للحصول على تغطية كريمية ناصعة (يُستعمل daily وعند المكياج).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>كرات الهيالورونيك وزيت المانجو:</strong> يحفزان امتلاء الشفاه ويحفظان رطوبتها طوال اليوم.</li>
  <li><strong>الصبغات الفرنسية الفاخرة:</strong> تضمن لوناً غنياً وثابتاً دون سيلان.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي التجميلي على الشفاه.</li>
  <li>احفظي الغطاء مغلقاً بإحكام لحماية أحمر الشفاه من الجفاف.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن {ar_title} للترطيب الفاخر والتلوين الناصع لشفاهها.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جيرلان باريس (Guerlain Paris France)</td></tr>
  <tr><th>الفئة</th><td>مكياج الشفاه / أحمر شفاه جيرلان الفاخر 3.5g</td></tr>
  <tr><th>نوع المنتج</th><td>أحمر شفاه كريمي مرطب غني بحمض الهيالورونيك وزيت المانجو (درجة {shade_code} - {shade_ar})</td></tr>
  <tr><th>الحجم/الوزن</th><td>3.5 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الشفاه (خصيصاً الشفاه الجافة والمشققة)</td></tr>
  <tr><th>المظهر النهائي</th><td>شفاه ممتلئة، ناعمة كالحرير، مرطبة 24 ساعة بلون {shade_ar} ناصع</td></tr>
  <tr><th>الملمس</th><td>كريمي دسم ينزلق بسلاسة متناهية</td></tr>
  <tr><th>العطر</th><td>عطر الفانيليا والزهور الفرنسي الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>كرات حمض الهيالورونيك، زيت المانجو، صبغات مكثفة</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>LVMH Guerlain France</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد الهيالورونيك وزيت المانجو في أحمر شفاه جيرلان (Guerlain Lipstick {shade_code})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج أحمر شفاه جيرلان مشكلة تشقق الشفاه، خفوت اللون، الخطوط الدقيقة بالشفاه، والتكتل بالروج العادي.</p>

<h3>لماذا تنجح تركيبة Guerlain Lipstick Shade {shade_code}؟</h3>
<p>لأن كرات الهيالورونيك تمتص الرطوبة وتنتفخ داخل خطوط الشفاه لتمنح امتلاءً وطراوة ممتدة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق مباشرة على الشفاه:</strong> ينعم السطح وينسلق بسلاسة.<br>
2. <strong>الاستخدام المباشر أو فوق كونسيلر الشفاه:</strong> يبرز ثبات وجمال اللون {shade_ar}.<br>
3. <strong>إغلاق الغطاء بإحكام:</strong> يحفظ طراوة أحمر الشفاه.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "أحمر الشفاه ذو الصبغة القوية يجفف الشفاه."<br>
<strong>الحقيقة:</strong> أحمر شفاه جيرلان مدعم بـ زيت المانجو والهيالورونيك لتوفير ترطيب ممتد طوال اليوم.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تغلف الزيوت الطبيعية سطح الشفاه مانعة تبخر الماء ورابطة الصبغات الملونة بأمان.</p>"""

    faqs_data = [
        (f"ما هو {ar_title}؟", f"هو أحمر شفاه كريمي مرطب بحمض الهيالورونيك وزيت المانجو بدرجة {shade_code} ({shade_ar}) من جيرلان (3.5 جم)."),
        (f"ما هي فوائد كرات الهيالورونيك وزيت المانجو بدرجة {shade_code}؟", "تمنح الشفاه امتلاءً طبيعياً، تلونها بصبغة ناصعة، وترطبها لـ 24 ساعة دون تشقق."),
        ("هل يلون الشفاه ويرطبها لـ 24 ساعة بدون تكتل؟", "نعم، مثبت سريرياً في ترطيب الشفاه ومنحها لوناً ناصعاً وامتلاءً خالي من التكتل."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة فاخرة بحجم 3.5 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي مباشرة من العبوة أو بالفرشاة من المنتصف نحو الزوايا الخارجية."),
        ("هل هو آمن ومختبر درماتولوجياً؟", "نعم، 100% آمن ومختبر درماتولوجياً ومناسب لجميع أنواع الشفاه."),
        ("أين صُنع أحمر شفاه جيرلان؟", "صُنع في فرنسا بواسطة LVMH Guerlain France."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات جيرلان لدى إكليل أبها أصلية 100%."),
        (f"ما درجة أحمر شفاه جيرلان؟", f"درجة {shade_code} ({shade_ar})."),
        ("هل يناسب الشفاه الجافة والمشققة؟", "نعم، ممتاز للشفاه الجافة والمشققة وإعادة الطراوة والامتلاء."),
        ("هل عبوة 3.5 جم فاخرة ومناسبة؟", "نعم، عبوة أنيقة أيقونية مريحة بالحقيبة وللاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل جيرلان الماركة الفرنسية الأولى في أحمر الشفاه؟", "نعم، Guerlain الماركة الفرنسية رقم 1 الأكثر شهرة بأحمر الشفاه الفاخر."),
        ("كم يدوم ثباته طوال اليوم؟", "يدوم لعدة ساعات متواصلة بلون ناصع وترطيب غني."),
        ("هل ينشطف بمزيل المكياج بسهولة؟", "نعم، ينشطف بسلاسة بمزيل المكياج دون شد الشفاه."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يخفي خطوط وتجاعيد الشفاه؟", "نعم، يملأ ينعم خطوط وتجاعيد الشفاه بفاعلية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والفتيات؟", "نعم، ممتاز للنساء والفتيات."),
        ("هل يناسب المناسبات والاستخدام اليومي؟", "نعم، ممتاز للمكياج اليومي والمناسبات الراقية."),
        ("هل يصلح هدية ممتازة ضمن مكياج الشفاه؟", "نعم، منتج مكياج فرنسي فاخر وأساسي لكل امرأة راقية."),
        (f"هل يعيد المظهر الناعم الممتلئ للشفاه بدرجة {shade_code}؟", f"نعم، يمنح الشفاه مظهراً ممتلئاً ومرطباً بلون ناصع."),
        ("هل تتوفر درجات أحمر شفاه جيرلان الأخرى؟", "نعم، تتوفر عائلة Guerlain Lipsticks كاملة لدى إكليل أبها."),
        ("هل يترك ملمساً لزجاً؟", "لا، ينزلق بسلاسة ويترك ملمساً كريمياً مخملياً غير لزج."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury hydrating and intensely pigmented lipstick from iconic House Guerlain Paris (Guerlain KissKiss / Rouge G Lipstick - {shade_code}) designed to deliver rich velvet color, attractive lip plumping, and 24-hour hydration without dryness or cracking. Built upon ultra-hydrating Hyaluronic Acid spheres, pure Mango Butter, and lip-protecting complexes.</p>
<p>Guerlain Lipstick in Shade {shade_code} smoothly coats lips in rich {shade_en} color, fills lip micro-lines, and infuses lip cells with velvet moisture leaving your lips touchably silky soft, hydrated, plumped, and vibrant from first stroke.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intense Rich Color & Hydration ({shade_code} - {shade_en}):</strong> Luxurious long-lasting finish.</li>
  <li><strong>Plumps & Smooths Lip Lines with Hyaluronic Spheres:</strong> Delivers fuller attractive lips.</li>
  <li><strong>Nourishes Deeply with Pure Natural Mango Butter:</strong> Prevents lip cracking all day long.</li>
  <li><strong>Creamy Smooth Texture Glides Without Caking:</strong> Lightweight comfortable feel.</li>
  <li><strong>Dermatologically Tested Safe for Sensitive Lips:</strong> 100% safe formula.</li>
  <li><strong>Iconic 3.5g Luxury Casing:</strong> The pinnacle of French luxury lipstick craft.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply Guerlain lipstick directly from bullet or using a lip brush.</li>
  <li><strong>Step 2:</strong> Start at the center of upper lip and move towards outer corners.</li>
  <li><strong>Step 3:</strong> Repeat on lower lip for rich creamy coverage (use daily with makeup).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Hyaluronic Spheres & Mango Butter:</strong> Stimulate lip plumping and preserve moisture all day.</li>
  <li><strong>Luxurious French Pigments:</strong> Guarantee rich intense color payoff without bleeding.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on lips.</li>
  <li>Keep cap closed tightly after use to prevent bullet dryness.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_title} for luxury hydration, lip plumping, and intense color payoff.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Guerlain Paris (France)</td></tr>
  <tr><th>Category</th><td>Lip Makeup / Guerlain Luxury Lipsticks 3.5g</td></tr>
  <tr><th>Product Type</th><td>Hydrating Hyaluronic & Mango Butter Creamy Lipstick (Shade {shade_code} - {shade_en})</td></tr>
  <tr><th>Volume/Weight</th><td>3.5 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Lip Types (Specifically Dry & Chapped Lips)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, plumped & vibrant {shade_en} lips</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-sticky creamy bullet gliding easily</td></tr>
  <tr><th>Fragrance</th><td>100% Luxurious French floral vanilla fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Hyaluronic Acid Spheres, Mango Butter, Intense Pigments</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>LVMH Guerlain France</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Hyaluronic Spheres & Mango Butter Lip Plumping</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves chapped lips, color fading, lip fine lines, and caking lipstick.</p>

<h3>Why choose Guerlain Lipstick {shade_code}?</h3>
<p>Hyaluronic spheres swell inside lip micro-lines upon moisture contact giving fuller smoother lips over time.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a luxury hydrating creamy lipstick with Hyaluronic Acid and Mango Butter from Guerlain Paris (Shade {shade_code} / 3.5g)."),
        (f"What are the benefits of Hyaluronic Spheres and Mango Butter in Shade {shade_code}?", "Plump lips naturally, coat with intense color, and hydrate for 24 hours without cracking."),
        ("Does it color lips and hydrate for 24 hours without caking?", "Yes, clinically proven to hydrate lips and deliver intense color and plumping without caking."),
        ("What volume is contained in this bullet?", "3.5g iconic luxury casing."),
        ("How do I use it correctly?", "Apply directly or with a brush from center towards outer corners."),
        ("Is it safe and dermatologically tested?", "Yes, 100% safe, dermatologically tested, and suitable for all lip types."),
        ("Where is Guerlain Lipstick manufactured?", "In France by LVMH Guerlain France."),
        ("How do I verify authenticity at Ekleel Abha?", "All Guerlain products at Ekleel Abha are 100% original."),
        (f"What shade is Guerlain Lipstick?", f"Shade {shade_code} ({shade_en})."),
        ("Is it suitable for dry and chapped lips?", "Yes, excellent for dry chapped lips restoring moisture and smoothness."),
        ("Is the 3.5g casing travel friendly?", "Yes, iconic luxury casing ideal for handbags and daily use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Guerlain a #1 French luxury lipstick brand?", "Yes, Guerlain is the premier French luxury house in lipsticks."),
        ("How long does it hold during the day?", "Holds for continuous hours with rich color and hydration."),
        ("Does it remove easily with makeup remover?", "Yes, removes smoothly with makeup remover without tugging lips."),
        ("Is the casing recyclable?", "Yes."),
        ("Does it fill lip micro-lines?", "Yes, effectively fills and smooths lip micro-lines."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and teens?", "Yes, suitable for both women and teens."),
        ("Is it good for special events and daily wear?", "Yes, ideal for daily makeup and special events."),
        ("Is it a nice makeup gift?", "Yes, an essential premier French luxury lipstick gift."),
        (f"Does it restore smooth plumped lips in Shade {shade_code}?", f"Yes, gives lips a smooth plumped radiant look."),
        ("Are other Guerlain lipstick shades available?", "Yes, the full Guerlain Lipstick shade range is available at Ekleel Abha."),
        ("Is it non-sticky?", "Yes, glides smoothly leaving a silky non-sticky finish."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Guerlain",
        "ar": {
            "title": ar_title,
            "meta_title": f"{ar_title} | إكليل أبها",
            "meta_description": f"اشتري {ar_title}. أحمر شفاه فرنسي فاخر بالهيالورونيك وزيت المانجو وتغطية 24 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. French luxury 24-hour hydrating Hyaluronic Acid & Mango Butter lipstick. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2222():
    return _make_guerlain_lipstick_b100(
        pid=2222, gtin="3346470431959",
        ar_title="روج احمر شفاه(N 677 - وردي) من جيرلان  3.5جم",
        en_title="Guerlain Lipstick (N 677 - Pink) 3.5g",
        shade_code="N 677", shade_ar="وردي (Pink)", shade_en="Pink",
        tags_ar=["جيرلان", "روج_جيرلان_677", "أحمر_شفاه_جيرلان_وردي", "روج_فرنسي_فاخر", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_lipstick_677", "pink_guerlain_lipstick", "french_lipstick", "ekleel_abha"]
    )


def create_product_2223():
    return _make_guerlain_lipstick_b100(
        pid=2223, gtin="3346470431966",
        ar_title="روج احمر شفاه(N 688 -لون الزهر) من جيرلان  3.5جم",
        en_title="Guerlain Lipstick (N 688 - Rose Color) 3.5g",
        shade_code="N 688", shade_ar="لون الزهر (Rose Color)", shade_en="Rose Color",
        tags_ar=["جيرلان", "روج_جيرلان_688", "أحمر_شفاه_جيرلان_زهر", "روج_فرنسي_فاخر", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_lipstick_688", "rose_guerlain_lipstick", "french_lipstick", "ekleel_abha"]
    )


def create_product_2224():
    return _make_guerlain_lipstick_b100(
        pid=2224, gtin="3346470431942",
        ar_title="روج احمر شفاه(N 588 -لون الزهر) من جيرلان  3.5جم",
        en_title="Guerlain Lipstick (N 588 - Rose Pink) 3.5g",
        shade_code="N 588", shade_ar="روز بينك (Rose Pink)", shade_en="Rose Pink",
        tags_ar=["جيرلان", "روج_جيرلان_588", "أحمر_شفاه_جيرلان_روز", "روج_فرنسي_فاخر", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_lipstick_588", "rose_pink_guerlain_lipstick", "french_lipstick", "ekleel_abha"]
    )


def create_product_2226():
    return _make_guerlain_lipstick_b100(
        pid=2226, gtin="3346470432017",
        ar_title="روج احمر شفاه(N 00 -لون بيج) من جيرلان  3.5جم",
        en_title="Guerlain Lipstick (N 00 - Beige) 3.5g",
        shade_code="N 00", shade_ar="بيج (Beige)", shade_en="Beige",
        tags_ar=["جيرلان", "روج_جيرلان_00", "أحمر_شفاه_جيرلان_بيج", "روج_فرنسي_فاخر", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_lipstick_00", "beige_guerlain_lipstick", "french_lipstick", "ekleel_abha"]
    )


def create_product_2228():
    return _make_guerlain_lipstick_b100(
        pid=2228, gtin="3346470431928",
        ar_title="روج احمر شفاه(N 007 -لون بيج فاتح ) من جيرلان  3.5جم",
        en_title="Guerlain Lipstick (N 007 - Light Beige) 3.5g",
        shade_code="N 007", shade_ar="بيج فاتح (Light Beige)", shade_en="Light Beige",
        tags_ar=["جيرلان", "روج_جيرلان_007", "أحمر_شفاه_جيرلان_بيج_فاتح", "روج_فرنسي_فاخر", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_lipstick_007", "light_beige_guerlain_lipstick", "french_lipstick", "ekleel_abha"]
    )


print("Loaded all 5 Batch 100 builders complete")
