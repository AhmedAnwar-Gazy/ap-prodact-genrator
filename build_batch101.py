import json, os

def _make_guerlain_kisskiss_liquid_b101(pid, gtin, ar_title, en_title, shade_code, shade_ar, shade_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_title}</strong> أحمر الشفاه السائل الفاخر الأسطوري ناصع البريق والترطيب من الدار الفرنسية العريقة جيرلان (Guerlain KissKiss Liquid Lipstick - {shade_code}) المصمم لمنح شفاهك صبغة سائلة حريرية مكثفة، لمعاناً زجاجياً ساحراً، وترطيباً عميقاً يدوم 24 ساعة دون أي لزوجة أو تشقق. يرتكز هذا المستحضر الفرنسي الأصيل ({en_title}) على زيت المانبرين الطبيعي المرطب، حمض الهيالورونيك، وجزيئات اللمعان الفرنسية الفاخرة.</p>

<p>يعمل أحمر شفاه جيرلان كيس كيس السائل بدرجة {shade_code} على تغليف الشفاه بلون {shade_ar} الساطع، ملء الخطوط الدقيقة للشفاه، وتزويد خلايا الشفاه برطوبة زجاجية تجعل الشفاه أكثر امتلاءً ونعومة كالحرير من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>صبغة سائلة ناصعة ولمعان زجاجي فاخر ({shade_code} - {shade_ar}):</strong> لون دائم وبريق يدوم لعدة ساعات.</li>
  <li><strong>امتلاء وتنعيم خطوط الشفاه بكرات حمض الهيالورونيك:</strong> مظهر أكثر حجماً وجاذبية.</li>
  <li><strong>ترطيب وتغذية فائقة بزيت المانبرين الطبيعي:</strong> يمنع تشقق وجفاف الشفاه طوال اليوم.</li>
  <li><strong>ملمس سائل حريري خفيف ينزلق بسهولة دون لزوجة:</strong> يمنح شعوراً مريحاً للغاية.</li>
  <li><strong>مختبر درماتولوجياً وآمن 100% لبشرة الشفاه الحساسة:</strong> خالي من المكونات الضارة.</li>
  <li><strong>عبوة أنيقة فاخرة بأداة تطبيق دقيقة سعة 5.8 مل:</strong> قمة الفخامة الفرنسية في أحمر الشفاه السائل.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> وزعي أحمر شفاه جيرلان السائل باستخدام أداة التطبيق الدقيقة المرفقة بالعبوة.</li>
  <li><strong>الخطوة الثانية:</strong> ابدئي من منتصف الشفة العلوية واتجهي نحو الزوايا الخارجية.</li>
  <li><strong>الخطوة الثالثة:</strong> كرري على الشفة السفلية للحصول على تغطية زجاجية ناصعة (يُستعمل daily وعند المكياج).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>كرات الهيالورونيك وزيت المانبرين:</strong> يحفزان امتلاء الشفاه ويحفظان رطوبتها طوال اليوم.</li>
  <li><strong>الصبغات الفرنسية الفاخرة المضيئة:</strong> تضمن لوناً غنياً وثابتاً دون سيلان.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي التجميلي على الشفاه.</li>
  <li>احفظي الغطاء مغلقاً بإحكام لحماية أحمر الشفاه السائل من الجفاف.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن {ar_title} للترطيب الفاخر والبريق الناصع لشفاهها.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جيرلان باريس (Guerlain Paris France)</td></tr>
  <tr><th>الفئة</th><td>مكياج الشفاه / أحمر شفاه جيرلان كيس كيس السائل 5.8ml</td></tr>
  <tr><th>نوع المنتج</th><td>أحمر شفاه سائل مرطب ومكثف البريق بحمض الهيالورونيك (درجة {shade_code} - {shade_ar})</td></tr>
  <tr><th>الحجم/الوزن</th><td>5.8 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الشفاه (خصيصاً الشفاه الجافة والمشققة)</td></tr>
  <tr><th>المظهر النهائي</th><td>شفاه ممتلئة، ناعمة كالحرير، مرطبة 24 ساعة بلون وبريق {shade_ar} ناصع</td></tr>
  <tr><th>الملمس</th><td>سائل دسم خفيف غير لزج ينزلق بسلاسة</td></tr>
  <tr><th>العطر</th><td>عطر الفانيليا والزهور الفرنسي الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>كرات حمض الهيالورونيك، زيت المانبرين، صبغات لامعة مكثفة</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>LVMH Guerlain France</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد الهيالورونيك وزيت المانبرين في أحمر شفاه جيرلان السائل (Guerlain KissKiss Liquid {shade_code})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج أحمر شفاه جيرلان السائل مشكلة اللزوجة المزعجة بملمعات الشفاه، خفوت البريق، الشفاه الرقيقة، والجفاف.</p>

<h3>لماذا تنجح تركيبة Guerlain KissKiss Liquid Lipstick {shade_code}؟</h3>
<p>لأن كرات الهيالورونيك تنتفخ بالرطوبة وتملأ ثنايا الشفاه بينما يمنح زيت المانبرين بريقاً زجاجياً غير لزج.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق المباشر بأداة التطبيق:</strong> يضمن توزيعاً زجاجياً متجانساً.<br>
2. <strong>الاستخدام المباشر أو فوق أحمر الشفاه الجاف:</strong> يضاعف البريق والكثافة.<br>
3. <strong>إغلاق العبوة بإحكام:</strong> يحفظ طراوة السائل الحريري.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "أحمر الشفاه السائل ذو البريق الزجاجي يلتصق بالشعر والملابس بلزوجة."<br>
<strong>الحقيقة:</strong> أحمر شفاه جيرلان كيس كيس السائل مصمم بتركيبة خفيفة غير لزجة تمنح رطوبة ناعمة كالحرير.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تغلف الزيوت المضيئة سطح الشفاه عاكسة الضوء ومكونة درعاً زجاجياً يحمي الرطوبة الداخلية.</p>"""

    faqs_data = [
        (f"ما هو {ar_title}؟", f"هو أحمر شفاه سائل مرطب ومكثف البريق بحمض الهيالورونيك بدرجة {shade_code} ({shade_ar}) من جيرلان (5.8 مل)."),
        (f"ما هي فوائد كرات الهيالورونيك وزيت المانبرين بدرجة {shade_code}؟", "تمنح الشفاه امتلاءً وبريقاً زجاجياً ناصعاً، وترطبها لـ 24 ساعة دون لزوجة أو تشقق."),
        ("هل يلون الشفاه ويرطبها لـ 24 ساعة بدون لزوجة؟", "نعم، مثبت سريرياً في ترطيب الشفاه ومنحها بريقاً زجاجياً غير لزج."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة فاخرة بأداة تطبيق دقيقة بسعة 5.8 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي بأداة التطبيق الدقيقة من منتصف الشفة نحو الزوايا الخارجية."),
        ("هل هو آمن ومختبر درماتولوجياً؟", "نعم، 100% آمن ومختبر درماتولوجياً ومناسب لجميع أنواع الشفاه."),
        ("أين صُنع أحمر شفاه جيرلان السائل؟", "صُنع في فرنسا بواسطة LVMH Guerlain France."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات جيرلان لدى إكليل أبها أصلية 100%."),
        (f"ما درجة أحمر شفاه جيرلان السائل؟", f"درجة {shade_code} ({shade_ar})."),
        ("هل يناسب الشفاه الجافة والمشققة؟", "نعم، ممتاز للشفاه الجافة والمشققة وإعادة الطراوة والبريق الزجاجي."),
        ("هل عبوة 5.8 مل فاخرة ومناسبة؟", "نعم، عبوة أنيقة أيقونية مريحة بالحقيبة وللاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل جيرلان الماركة الفرنسية الأولى في أحمر الشفاه السائل؟", "نعم، Guerlain KissKiss Liquid الماركة الفرنسية رقم 1 الأكثر شهرة بأحمر الشفاه السائل الفاخر."),
        ("كم يدوم ثباته طوال اليوم؟", "يدوم لعدة ساعات متواصلة ببريق زجاجي وترطيب غني."),
        ("هل ينشطف بمزيل المكياج بسهولة؟", "نعم، ينشطف بسلاسة بمزيل المكياج دون شد الشفاه."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يخفي خطوط وتجاعيد الشفاه؟", "نعم، يملأ ينعم خطوط وتجاعيد الشفاه بفاعلية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والفتيات؟", "نعم، ممتاز للنساء والفتيات."),
        ("هل يناسب المناسبات والاستخدام اليومي؟", "نعم، ممتاز للمكياج اليومي والمناسبات الراقية."),
        ("هل يصلح هدية ممتازة ضمن مكياج الشفاه؟", "نعم، منتج مكياج فرنسي فاخر وأساسي لكل امرأة راقية."),
        (f"هل يعيد المظهر الناعم الممتلئ للشفاه بدرجة {shade_code}؟", f"نعم، يمنح الشفاه مظهراً ممتلئاً ومرطباً ببريق ناصع."),
        ("هل تتوفر درجات أحمر شفاه جيرلان السائل الأخرى؟", "نعم، تتوفر عائلة Guerlain KissKiss Liquid كاملة لدى إكليل أبها."),
        ("هل يترك ملمساً لزجاً؟", "لا، ينزلق بسلاسة ويترك ملمساً حريرياً زجاجياً غير لزج."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury hydrating and glassy-shine liquid lipstick from iconic House Guerlain Paris (Guerlain KissKiss Liquid Lipstick - {shade_code}) designed to deliver rich fluid color, captivating mirror shine, and 24-hour hydration without stickiness or cracking. Built upon hydrating Cranberry Oil, Hyaluronic Acid spheres, and luminous French pigment complexes.</p>

<p>Guerlain KissKiss Liquid Lipstick in Shade {shade_code} smoothly coats lips in fluid {shade_en} color, fills lip micro-lines, and infuses lip cells with mirror-shine moisture leaving your lips touchably silky soft, hydrated, plumped, and luminous from first stroke.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Fluid Intense Color & Glassy Mirror Shine ({shade_code} - {shade_en}):</strong> Luxurious long-lasting shine.</li>
  <li><strong>Plumps & Smooths Lip Lines with Hyaluronic Spheres:</strong> Delivers fuller attractive lips.</li>
  <li><strong>Nourishes Deeply with Pure Natural Cranberry Oil:</strong> Prevents lip cracking all day long.</li>
  <li><strong>Silky Fluid Non-Sticky Texture Glides Effortlessly:</strong> Ultra-comfortable non-tacky feel.</li>
  <li><strong>Dermatologically Tested Safe for Sensitive Lips:</strong> 100% safe formula.</li>
  <li><strong>Iconic 5.8ml Luxury Applicator Casing:</strong> The pinnacle of French luxury liquid lipstick craft.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply Guerlain liquid lipstick using the precise doe-foot applicator.</li>
  <li><strong>Step 2:</strong> Start at the center of upper lip and glide towards outer corners.</li>
  <li><strong>Step 3:</strong> Repeat on lower lip for full mirror-shine coverage (use daily with makeup).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Hyaluronic Spheres & Cranberry Oil:</strong> Stimulate lip plumping and preserve moisture all day.</li>
  <li><strong>Luminous French Pigments:</strong> Guarantee rich intense color payoff without bleeding.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on lips.</li>
  <li>Keep cap closed tightly after use to prevent fluid dryness.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_title} for luxury non-sticky hydration, lip plumping, and mirror-shine color.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Guerlain Paris (France)</td></tr>
  <tr><th>Category</th><td>Lip Makeup / Guerlain Luxury Liquid Lipsticks 5.8ml</td></tr>
  <tr><th>Product Type</th><td>Hydrating Hyaluronic & Cranberry Oil Non-Sticky Liquid Lipstick (Shade {shade_code} - {shade_en})</td></tr>
  <tr><th>Volume/Weight</th><td>5.8 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Lip Types (Specifically Dry & Chapped Lips)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, plumped & mirror-shine {shade_en} lips</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-sticky fluid liquid gliding easily</td></tr>
  <tr><th>Fragrance</th><td>100% Luxurious French floral vanilla fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Hyaluronic Acid Spheres, Cranberry Oil, Luminous Pigments</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>LVMH Guerlain France</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Hyaluronic Spheres & Cranberry Oil Mirror Shine</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves tacky lip gloss, color dullness, lip fine lines, and chapped lips.</p>

<h3>Why choose Guerlain KissKiss Liquid Lipstick {shade_code}?</h3>
<p>Hyaluronic spheres swell inside lip micro-lines while Cranberry Oil creates a smooth non-sticky mirror-shine barrier.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a luxury hydrating liquid lipstick with Hyaluronic Acid and Cranberry Oil from Guerlain Paris (Shade {shade_code} / 5.8ml)."),
        (f"What are the benefits of Hyaluronic Spheres and Cranberry Oil in Shade {shade_code}?", "Plump lips naturally, coat with intense mirror shine, and hydrate for 24 hours without stickiness."),
        ("Does it color lips and hydrate for 24 hours without stickiness?", "Yes, clinically proven to hydrate lips and deliver mirror shine and plumping without stickiness."),
        ("What volume is contained in this tube?", "5.8ml iconic luxury applicator casing."),
        ("How do I use it correctly?", "Apply with precise doe-foot applicator from center towards outer corners."),
        ("Is it safe and dermatologically tested?", "Yes, 100% safe, dermatologically tested, and suitable for all lip types."),
        ("Where is Guerlain Liquid Lipstick manufactured?", "In France by LVMH Guerlain France."),
        ("How do I verify authenticity at Ekleel Abha?", "All Guerlain products at Ekleel Abha are 100% original."),
        (f"What shade is Guerlain Liquid Lipstick?", f"Shade {shade_code} ({shade_en})."),
        ("Is it suitable for dry and chapped lips?", "Yes, excellent for dry chapped lips restoring moisture and mirror shine."),
        ("Is the 5.8ml casing travel friendly?", "Yes, iconic luxury casing ideal for handbags and daily use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Guerlain a #1 French luxury liquid lipstick brand?", "Yes, Guerlain is the premier French luxury house in liquid lipsticks."),
        ("How long does it hold during the day?", "Holds for continuous hours with rich mirror shine and hydration."),
        ("Does it remove easily with makeup remover?", "Yes, removes smoothly with makeup remover without tugging lips."),
        ("Is the casing recyclable?", "Yes."),
        ("Does it fill lip micro-lines?", "Yes, effectively fills and smooths lip micro-lines."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and teens?", "Yes, suitable for both women and teens."),
        ("Is it good for special events and daily wear?", "Yes, ideal for daily makeup and special events."),
        ("Is it a nice makeup gift?", "Yes, an essential premier French luxury liquid lipstick gift."),
        (f"Does it restore smooth plumped lips in Shade {shade_code}?", f"Yes, gives lips a smooth plumped mirror-shine look."),
        ("Are other Guerlain liquid lipstick shades available?", "Yes, the full Guerlain KissKiss Liquid shade range is available at Ekleel Abha."),
        ("Is it non-sticky?", "Yes, glides smoothly leaving a silky non-tacky mirror-shine finish."),
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
            "meta_description": f"اشتري {ar_title}. أحمر شفاه سائل فرنسي فاخر ببريق زجاجي غير لزج وترطيب 24 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. French luxury 24-hour hydrating Hyaluronic Acid non-sticky liquid lipstick. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2232():
    return _make_guerlain_kisskiss_liquid_b101(
        pid=2232, gtin="3346470429598",
        ar_title="أحمر شفاه سائلkiss kiss (L323- واو جيتر) من جيرلان  - 5.8 مل",
        en_title="Guerlain KissKiss Liquid Lipstick (L323 Wow Glitter) - 5.8ml",
        shade_code="L323", shade_ar="واو جليتر (Wow Glitter)", shade_en="Wow Glitter",
        tags_ar=["جيرلان", "روج_جيرلان_سائل_L323", "كيس_كيس_سائل_جيرلان", "روج_سائل_لامع", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_kisskiss_liquid_323", "wow_glitter_guerlain", "liquid_lipstick", "ekleel_abha"]
    )


def create_product_2233():
    return _make_guerlain_kisskiss_liquid_b101(
        pid=2233, gtin="3346470429550",
        ar_title="أحمر شفاه سائلkiss kiss (L302- نود شاين) من جيرلان  - 5.8 مل",
        en_title="Guerlain KissKiss Liquid Lipstick (L302 - Nude Shine) - 5.8 ml",
        shade_code="L302", shade_ar="نود شاين (Nude Shine)", shade_en="Nude Shine",
        tags_ar=["جيرلان", "روج_جيرلان_سائل_L302", "كيس_كيس_سائل_جيرلان", "روج_سائل_نود", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_kisskiss_liquid_302", "nude_shine_guerlain", "liquid_lipstick", "ekleel_abha"]
    )


def create_product_2234():
    return _make_guerlain_kisskiss_liquid_b101(
        pid=2234, gtin="3346470429505",
        ar_title="أحمر شفاه سائلkiss kiss (L361- لفلي شاين) من جيرلان  - 5.8 مل",
        en_title="Guerlain KissKiss Liquid Lipstick (L361- Lovely Shine) - 5.8 ml",
        shade_code="L361", shade_ar="لفلي شاين (Lovely Shine)", shade_en="Lovely Shine",
        tags_ar=["جيرلان", "روج_جيرلان_سائل_L361", "كيس_كيس_سائل_جيرلان", "روج_سائل_وردي", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_kisskiss_liquid_361", "lovely_shine_guerlain", "liquid_lipstick", "ekleel_abha"]
    )


def create_product_2235():
    return _make_guerlain_kisskiss_liquid_b101(
        pid=2235, gtin="3346470429512",
        ar_title="أحمر شفاه سائلkiss kiss (L362- جلام شاين) من جيرلان  - 5.8 مل",
        en_title="Guerlain KissKiss Liquid Lipstick (L362 Glam Shine) - 5.8 ml",
        shade_code="L362", shade_ar="جلام شاين (Glam Shine)", shade_en="Glam Shine",
        tags_ar=["جيرلان", "روج_جيرلان_سائل_L362", "كيس_كيس_سائل_جيرلان", "روج_سائل_جلام", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_kisskiss_liquid_362", "glam_shine_guerlain", "liquid_lipstick", "ekleel_abha"]
    )


def create_product_2236():
    return _make_guerlain_kisskiss_liquid_b101(
        pid=2236, gtin="3346470429529",
        ar_title="أحمر شفاه سائلkiss kiss (L363- ليدي شاين) من جيرلان  - 5.8 مل",
        en_title="Guerlain kiss kiss liquid lipstick (L363- Lady shine) - 5.8 ml",
        shade_code="L363", shade_ar="ليدي شاين (Lady Shine)", shade_en="Lady Shine",
        tags_ar=["جيرلان", "روج_جيرلان_سائل_L363", "كيس_كيس_سائل_جيرلان", "روج_سائل_ليدي", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_kisskiss_liquid_363", "lady_shine_guerlain", "liquid_lipstick", "ekleel_abha"]
    )


print("Loaded all 5 Batch 101 builders complete")
