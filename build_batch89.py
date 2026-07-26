import json, os

def _make_guerlain_mascara_b89(pid, gtin, ar_title, en_title, shade_num, shade_ar, shade_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>{ar_title}</strong> الماسكارا الفاخرة الأسطورية المركّزة لتكثيف وتطويل وتأطير الرموش من الدار الفرنسية العريقة جيرلان (Guerlain Mad Eyes Mascara) المصممة لمنح رموشك كثافة قابلة للبناء 112%+، طولاً درامياً، وانحناءة ساحرة بلون {shade_ar} الناصع الجذاب. تركز هذه الماسكارا الفرنسية الأصيلة ({en_title}) على الفرشاة الأليافية المبتكرة ذات الشكل الهرمي، مركب الكيراتين المقوي للرموش، وشمع النحل المغذي.</p>
<p>تعمل ماسكارا جيرلان ماد آيز باللون {shade_ar} على تغليف كل رمش بلون {shade_ar} ناصع، تمشيط الرموش وفصلها بدقة دون أي تكتل، وتزويد بويصلات الرموش بتغذية مستمرة تجعل الرموش أكثر كثافة وطولاً حتى بعد إزالة المكياج، لتترك عينيك مؤطرتين بجمال ساحر طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>كثافة مضاعفة 112%+ وطول وتجعيد ساحر للرموش:</strong> مظهر {shade_ar} ساحر وأنيق للغاية.</li>
  <li><strong>لون {shade_ar} فاخر (درجة {shade_num}):</strong> يمنح نظرة مميزة وساحرة تبرز جمال العينين.</li>
  <li><strong>فرشاة ألياف هرمية تفصل أدق الرموش:</strong> تمنع التكتل والالتصاق كلياً.</li>
  <li><strong>تغذية مستمرة بكيراتين الشعر وشمع النحل:</strong> تزيد كثافة وطول الرموش الطبيعية مع الوقت.</li>
  <li><strong>ثبات عالي لـ 24 ساعة مقاوم للتلطخ والرطوبة:</strong> تدوم طوال اليوم بنضارة.</li>
  <li><strong>أنبوب ذهبي فاخر أيقوني من جيرلان:</strong> قمة الفخامة الفرنسية بمكياج العيون.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي فرشاة ماسكارا جيرلان عند قاعدة الرموش الجافة والنظيفة.</li>
  <li><strong>الخطوة الثانية:</strong> اسحبي الفرشاة بحركة متعرجة (Zig-Zag) لأعلى باتجاه الأطراف لرفع وتكثيف الرموش.</li>
  <li><strong>الخطوة الثالثة:</strong> كرري الطبقة للحصول على كثافة {shade_ar} إضافية حسب الرغبة (تُستعمل يومياً وعند المكياج).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركب الكيراتين وشمع النحل:</strong> يعززان مرونة الرموش وينشطان بويصلات النمو الطبيعي.</li>
  <li><strong>الصبغات {shade_ar} الغنية الفاخرة:</strong> تمنح لوناً راقياً وناعماً دون تكتل.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي التجميلي على الرموش فقط.</li>
  <li>تجنبي التلامس المباشر لداخل العين واحفظي الغطاء مغلقاً بإحكام.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن {ar_title} لكثافة وطول وتغذية رموش فاخرة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جيرلان باريس (Guerlain Paris France)</td></tr>
  <tr><th>الفئة</th><td>مكياج العيون / ماسكارات جيرلان الفاخرة 8.5ml</td></tr>
  <tr><th>نوع المنتج</th><td>ماسكارا تكثيف وتطويل وتغذية باللون {shade_ar} كيراتين وشمع النحل (8.5ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>8.5 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الرموش (خصيصاً الخفيفة، القصيرة والمستقيمة) ومستخدمي العدسات</td></tr>
  <tr><th>المظهر النهائي</th><td>رموش كثيفة 112%+، طويلة، مقوسة، بلون {shade_ar} ومفصولة دون تكتل</td></tr>
  <tr><th>الملمس</th><td>كريم شمعي ناعم ينساب بسلاسة ويغلف الرموش</td></tr>
  <tr><th>العطر</th><td>عطر الزهور والمسك الفرنسي اللطيف الخفيف</td></tr>
  <tr><th>المكونات النشطة</th><td>مركب الكيراتين، شمع النحل، صبغات {shade_ar} فاخرة</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>LVMH Guerlain France</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد مركب الكيراتين وشمع النحل في ماسكارا جيرلان ماد آيز (Guerlain Mad Eyes {shade_num})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج ماسكارا جيرلان ماد آيز مشكلة الرموش الخفيفة، التقصف، التساقط، والتكتل بالماسكارات العادية.</p>

<h3>لماذا تنجح تركيبة Guerlain Mad Eyes Mascara {shade_num}؟</h3>
<p>لأن دمج الكيراتين وشمع النحل يغذي ألياف الرموش الطبيعية بينما تفصل الفرشاة الهرمية الخصلات بلون {shade_ar}.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق بحركة متعرجة من القاعدة للأطراف:</strong> يرفع ويكثف كل رمش.<br>
2. <strong>إغلاق الغطاء بإحكام:</strong> يمنع جفاف ماسكارا جيرلان الفاخرة.<br>
3. <strong>الإزالة بـ مزيل مكياج عيون مائي أو زيتي:</strong> يحافظ على سلامة الرموش الطبيعية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الماسكارات الملونة تجفف ألياف الرموش وتسقطها."<br>
<strong>الحقيقة:</strong> ماسكارا جيرلان مدعمة بالكيراتين وشمع النحل لحماية وتغذية وتكثيف الرموش بأمان فرانسوي كامل.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبت جزيئات الكيراتين وشمع النحل على جدار الرمش مقوية سمك الألياف بنسبة 112%+ مع الوقت.</p>"""

    faqs_data = [
        (f"ما هي {ar_title}؟", f"هي ماسكارا تكثيف وتطويل وتغذية فاخرة باللون {shade_ar} بالكيراتين وشمع النحل من جيرلان (8.5 مل)."),
        (f"ما هي فوائد اللون {shade_ar} ومركب الكيراتين؟", f"تزيد كثافة الرموش 112%+، تطولها وتفصلها، وتغذي البويصلات دون تكتل بلون {shade_ar} أنيق."),
        (f"هل تضاعف الكثافة 112%+ وتغذي الرموش بدون تكتل؟", f"نعم، مثبتة سريرياً في زيادة حجم الرموش 112%+ وتوفير لون {shade_ar} وتغذية خالية من التكتل."),
        ("ما حجم العبوة؟", "تأتي بأنبوب ذهبي أيقوني فاخر بسعة 8.5 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي عند قاعدة الرموش واسحبي بحركة متعرجة لأعلى وكرري الطبقة حسب الرغبة."),
        ("هل هي آمنة ومختبرة من أطباء العيون؟", "نعم، 100% آمنة ومختبرة من أطباء العيون ومناسبة للعيون الحساسة ومستخدمي العدسات."),
        ("أين صُنعت ماسكارا جيرلان ماد آيز؟", "صُنعت في فرنسا بواسطة LVMH Guerlain France."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات جيرلان لدى إكليل أبها أصلية 100%."),
        (f"ما لون ماسكارا جيرلان ماد آيز {shade_num}؟", f"لون {shade_ar} فاخر وأنيق (درجة {shade_num})."),
        ("هل يناسب الرموش القصيرة والخفيفة والمكياج الناعم؟", "نعم، ممتازة لتكثيف وتطويل الرموش وإبراز جمال العينين بنعومة."),
        ("هل أنبوب 8.5 مل الذهبي فاخر ومريح؟", "نعم، أنبوب ذهبي أيقوني قمة في الفخامة والراحة للحقيبة اليومية."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل جيرلان ماد آيز الماسكارا الفرنسية الأولى بالجمال؟", "نعم، Guerlain Mad Eyes الماسكارا الفاخرة رقم 1 الأكثر شهرة وتفضيلاً بعالم الجمال."),
        ("كم يدوم ثباتها طوال اليوم؟", "تدوم لـ 24 ساعة متواصلة مقاومة للتلطخ والرطوبة."),
        ("هل ينشطف بمزيل المكياج بسهولة؟", "نعم، ينشطف بسلاسة بمزيل مكياج العيون دون شد الرموش."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل تزيد كثافة الرموش الطبيعية مع الوقت؟", "نعم، بمركب الكيراتين وشمع النحل تغذي الرموش وتزيد كثافتها وطولها الطبيعي."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والفتيات؟", "نعم، ممتاز للنساء والفتيات."),
        ("هل يناسب المناسبات والمكياج اليومي الراقية؟", "نعم، ممتازة للمكياج اليومي والمناسبات الفاخرة."),
        ("هل يصلح هدية ممتازة ضمن مكياج العيون؟", "نعم، منتج مكياج فرنسي فاخر وأساسي لكل امرأة راقية."),
        (f"هل يعيد المظهر المشرق والساحر للعينين باللون {shade_ar}؟", f"نعم، يمنح العينين نظرة واسعة ورموشاً ناصعة باللون {shade_ar}."),
        ("هل تتوفر ألوان ماسكارا جيرلان الأخرى؟", "نعم، تتوفر عائلة Guerlain Mad Eyes Mascaras كاملة لدى إكليل أبها."),
        ("هل تفصل الرموش بدقة بالفرشاة الهرمية؟", "نعم، الفرشاة الهرمية تفصل أدق الرموش وتمنع التكتل والالتصاق كلياً."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury French volumizing, lengthening, and lash-care mascara from House Guerlain designed to deliver buildable 112%+ volume, dramatic length, and a captivating curl in a vibrant {shade_en} shade. Built upon an innovative hourglass fiber brush, lash-strengthening Keratin complex, and nourishing Beeswax.</p>
<p>Guerlain Mad Eyes Mascara in {shade_en} smoothly coats every single lash in vibrant {shade_en} color, separates lashes precisely without clumping, and continuously infuses lashes with nourishment that increases natural density over time, leaving your eyes touchably framed with sophisticated beauty all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>112%+ Buildable Volume, Length & Curl:</strong> Delivers an extraordinarily elegant {shade_en} finish.</li>
  <li><strong>Luxurious {shade_en} Color (Shade {shade_num}):</strong> Imparts a soft, vivid, sophisticated eye look.</li>
  <li><strong>Hourglass Fiber Brush Separates Fine Lashes:</strong> Prevents clumping or sticking completely.</li>
  <li><strong>Continuous Lash Care with Keratin & Beeswax:</strong> Increases natural lash density and strength over time.</li>
  <li><strong>24-Hour Long-Wear Smudge-Proof Hold:</strong> Resists humidity and smudging all day.</li>
  <li><strong>Iconic Luxury Gold Guerlain Casing:</strong> The pinnacle of French luxury eye makeup craft.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Place the Guerlain mascara brush at the base of clean dry eyelashes.</li>
  <li><strong>Step 2:</strong> Sweep brush upwards in a zig-zag motion to lift, curl, and coat lashes.</li>
  <li><strong>Step 3:</strong> Apply an extra coat for additional {shade_en} volume as desired (use daily with makeup).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Keratin Complex & Beeswax:</strong> Enhance lash flexibility and stimulate natural eyelash growth.</li>
  <li><strong>Rich {shade_en} Pigments:</strong> Provide a sophisticated vibrant lash color without clumping.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on eyelashes.</li>
  <li>Avoid direct contact inside the eyes and keep cap tightly closed after use.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_title} for luxury 112%+ volume, length, and {shade_en} lash care.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Guerlain Paris (France)</td></tr>
  <tr><th>Category</th><td>Eye Makeup / Guerlain Luxury Mascaras 8.5ml</td></tr>
  <tr><th>Product Type</th><td>112%+ Volume & Length Keratin Beeswax {shade_en} Mascara (8.5ml)</td></tr>
  <tr><th>Volume/Weight</th><td>8.5 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Eyelash Types (Sparse, Short & Straight Lashes) & Contact Lens Wearers</td></tr>
  <tr><th>Finish</th><td>112%+ volume, dramatically lengthened, {shade_en} & clump-free separated lashes</td></tr>
  <tr><th>Texture</th><td>Rich smooth {shade_en} creamy wax gliding easily</td></tr>
  <tr><th>Fragrance</th><td>100% Mild gentle French floral musk fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Keratin Complex, Beeswax, Luxury {shade_en} Pigments</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>LVMH Guerlain France</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Hourglass Fiber Separation & Keratin-Beeswax Lash Densification</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves sparse short lashes, ordinary black mascara boredom, lash fallout, and clumping.</p>

<h3>Why choose Guerlain Mad Eyes Mascara {shade_num}?</h3>
<p>The hourglass fiber brush coats fine lashes deposited with Keratin and Beeswax boosting natural lash volume by 112%+ over time.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a luxury volumizing and lash-care mascara from Guerlain Paris with Keratin and Beeswax in {shade_en} (8.5ml)."),
        (f"What are the benefits of {shade_en} color and Keratin complex?", f"Increase volume 112%+, lengthen and curl lashes, and nourish natural lash fibers without clumping."),
        (f"Does it increase lash volume 112%+ and nourish lashes without clumping?", f"Yes, clinically proven to boost lash volume 112%+ while delivering vibrant {shade_en} color and lash care."),
        ("What volume is contained in this gold tube?", "8.5ml iconic gold luxury tube."),
        ("How do I use it correctly?", "Place at lash base, sweep upwards in zig-zag motion, and re-apply for extra volume."),
        ("Is it safe and ophthalmologically tested?", "Yes, 100% safe, ophthalmologically tested, and suitable for sensitive eyes and contact lens wearers."),
        ("Where is Guerlain Mad Eyes Mascara manufactured?", "In France by LVMH Guerlain France."),
        ("How do I verify authenticity at Ekleel Abha?", "All Guerlain products at Ekleel Abha are 100% original."),
        (f"What color is Guerlain Mad Eyes Mascara {shade_num}?", f"Luxurious vibrant {shade_en} (Shade {shade_num})."),
        ("Is it suitable for short, sparse, and straight lashes?", "Yes, excellent for volumizing, lengthening, and softly defining short and fine lashes."),
        ("Is the 8.5ml gold casing travel friendly?", "Yes, iconic gold casing ideal for luxury makeup bags and daily use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Guerlain Mad Eyes a #1 French luxury mascara?", "Yes, Guerlain Mad Eyes is the world's premier luxury French mascara line."),
        ("How long does it hold during the day?", "Holds for 24 continuous hours smudge-free and humidity-proof."),
        ("Does it remove easily with makeup remover?", "Yes, removes smoothly with eye makeup remover without tugging lashes."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it increase natural lash density over time?", "Yes, Keratin and Beeswax nourish lash roots increasing natural lash volume over time."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and teens?", "Yes, suitable for both women and teens."),
        ("Is it good for daily wear and special occasions?", "Yes, ideal for daily makeup, events, and elegant looks."),
        ("Is it a nice makeup gift?", "Yes, an essential premier French luxury makeup gift."),
        (f"Does it restore vibrant eye beauty in {shade_en}?", f"Yes, gives eyes a wide framed vibrant {shade_en} lash look."),
        ("Are other Guerlain mascaras available?", "Yes, the full Guerlain mascara range is available at Ekleel Abha."),
        ("Does the hourglass brush separate fine lashes effectively?", "Yes, hourglass fiber brush captures fine short lashes separating them without clumping."),
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
            "meta_description": f"اشتري {ar_title}. ماسكارا فرنسية فاخرة لتكثيف وتطويل الرموش 112%+ بالكيراتين وشمع النحل باللون {shade_ar}. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. French luxury 112%+ volume & length Keratin Beeswax {shade_en} mascara. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2167():
    return _make_guerlain_mascara_b89(
        pid=2167, gtin="3346470432130",
        ar_title="ماسكارا ماد آيز( 03 ازرق )من جيرلان",
        en_title="Guerlain Mad Eyes Mascara - 03 Blue",
        shade_num="03", shade_ar="أزرق", shade_en="Blue",
        tags_ar=["جيرلان", "ماسكارا_جيرلان_أزرق", "ماسكارا_جيرلان_ماد_آيز_03", "تكثيف_الرموش_جيرلان", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_blue_mascara", "mad_eyes_03_blue", "guerlain_mascara", "ekleel_abha"]
    )


def create_product_2168():
    return _make_guerlain_mascara_b89(
        pid=2168, gtin="3346470419124",
        ar_title="ماسكارا ماد آيز( 01 اسود )من جيرلان",
        en_title="Guerlain Mad Eyes Mascara (01 Mad Black)",
        shade_num="01", shade_ar="أسود فاحم", shade_en="Mad Black",
        tags_ar=["جيرلان", "ماسكارا_جيرلان_أسود", "ماسكارا_جيرلان_ماد_آيز_01", "تكثيف_الرموش_جيرلان", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_black_mascara", "mad_eyes_01_black", "guerlain_mascara", "ekleel_abha"]
    )


def _make_eyeshadow_stick_b89(pid, gtin, ar_title, en_title, shades_ar, shades_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_title}</strong> قلم ظلال العيون الكريمي الثنائي الفاخر المزدوج الطرفين من جيرلان باريس (Guerlain Mad Eyes Contrast Shadow Duo) المصمم لمنح جفنيك ظلال عيون كريمية حريرية غنية بالصبغات وسهلة التحديد والتظليل بلمسة واحدة دون تكتل أو تسرب بالخطوط. تركز هذه الأقلام الفرنسية الأصيلة ({en_title}) على تركيبتها الشمعية الحريرية المقاومة للماء ورأسين كريميين بدرجتين مكملتين هما ({shades_ar}).</p>
<p>يعمل قلم ظلال العيون الكريمي الثنائي من جيرلان على رسم وتظليل وتحديد الجفن بسهولة احترافية، منح العينين نظرة ساحرة ومفعمة بالتألق لـ 24 ساعة متواصلة، وتزويد الجلد برطوبة ناعمة، ليترك جفنيك ناعمين كالحرير، مرطبين، ناصعي البريق، ومحميين من التجمع بالكسرات من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>قلم ظلال عيون ثنائي الطرفين بدرجتين مكملتين ({shades_ar}):</strong> يسهل رسم وتحديد وتظليل العينين ببراعة.</li>
  <li><strong>قوام كريمي شمعي ينساب بسلاسة دون شد الجفن:</strong> يندمج فورياً بأطراف الأصابع أو الفرشاة.</li>
  <li><strong>ثبات عالي لـ 24 ساعة مقاوم للماء، التلطخ، والعرق:</strong> يثبت دون التسرب بكسرات الجفن.</li>
  <li><strong>صبغات ناصعة مركزة تمنح بريقاً مات أو لؤلؤي:</strong> تبرز جمال ونظرة العينين بوضوح.</li>
  <li><strong>تركيبة خفيفة وآمنة للعيون الحساسة ومستخدمي العدسات:</strong> مختبرة من أطباء العيون.</li>
  <li><strong>قلم مدمج فاخر مريح جداً بالحقيبة وللسفر:</strong> تصميم أنيق وسريع الاستخدام.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> وزعي الدرجة الفاتحة من القلم على كامل الجفن المتحرك كأساس ومضيء.</li>
  <li><strong>الخطوة الثانية:</strong> ارسمي وزللي بالدرجة الداكنة عند زاوية العين الخارجية وخط الرموش للتحديد والتأطير.</li>
  <li><strong>الخطوة الثالثة:</strong> ادمجي اللونين برفق بأطراف الأصابع أو الفرشاة للحصول على تدرج ساحر (يُستعمل daily وعند المكياج).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الشمع الطبيعي والزيوت المطرية:</strong> يمنحان القلم ملمساً كريمياً ينساب بمرونة دون تجفيف الجفن.</li>
  <li><strong>الصبغات الجزيئية المقاومة للماء:</strong> تضمن ثبات اللون بريقه طوال اليوم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي التجميلي على جفن وجوانب العين.</li>
  <li>تجنبي التلامس المباشر لداخل العين واغلقي الأغطية بإحكام بعد الاستخدام.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن {ar_title} للتظليل والتحديد الكريمي السريع والمقاوم للماء للعينين.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جيرلان باريس (Guerlain Paris France)</td></tr>
  <tr><th>الفئة</th><td>مكياج العيون / أقلام ظلال العيون الكريمية الثنائية من جيرلان</td></tr>
  <tr><th>نوع المنتج</th><td>قلم ظلال عيون كريمي ثنائي مقاوم للماء والكسرات ({shades_ar})</td></tr>
  <tr><th>الحجم/الوزن</th><td>قلم ثنائي الرأس مدمج (Dual Head Stick)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجفون (العادية، الدهنية والجافة) ومستخدمي العدسات</td></tr>
  <tr><th>المظهر النهائي</th><td>جفون ناعمة كالحرير، مرطبة، مظللة ببريق ساحر ومحددة دون تكتل لـ 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>كريمي شمعي لطيف ينساب ويندمج بسلاسة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور المهيجة</td></tr>
  <tr><th>المكونات النشطة</th><td>شمع طبيعي، صبغات كتلية مقاومة للماء، زيوت مرطبة للجفن</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>LVMH Guerlain France</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد القوام الكريمي المقاوم للماء في قلم ظلال جيرلان الثنائي (Guerlain Dual Shadow Stick)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج قلم ظلال العيون من جيرلان مشكلة تساقط البودرة، التكتل بكسرات الجفن، الصعوبة في دمج الظلال، وتلاشي المكياج.</p>

<h3>لماذا تنجح تركيبة Guerlain Mad Eyes Shadow Duo Stick ({shades_ar})؟</h3>
<p>لأن التركيبة الشمعية الحريرية تثبت فورياً على جلد الجفن دون أن تسرب في خطوط الجفون أو تتأثر بالماء.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق مباشرة من القلم على الجفن:</strong> يسهل رسم التدرج دون حاجة لفرش كثيرة.<br>
2. <strong>الدمج السريع بأطراف الأصابع قبل جفاف القوام:</strong> يمنح تدرجاً ناعماً ساحراً.<br>
3. <strong>إغلاق الغطاءين بإحكام:</strong> يحفظ طراوة القلم الكريمي من الجفاف.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "أقلام الظلال الكريمية تتجمع بكسرات الجفن وتسرب خلال اليوم."<br>
<strong>الحقيقة:</strong> قلم ظلال جيرلان مصمم بتركيبة مقاومة للماء والكسرات تثبت لـ 24 ساعة كاملة بنقاء.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تشكل البوليمرات الشمعية درعاً مرناً يلتصق ببشرة الجفن مانعاً إفرازات الزيوت من إذابة الصبغة.</p>"""

    faqs_data = [
        (f"ما هو {ar_title}؟", f"هو قلم ظلال عيون كريمي ثنائي مقاوم للماء والكسرات بدرجتين مكملتين ({shades_ar}) من جيرلان (فرنسا)."),
        (f"ما هي فوائد القوام الكريمي والدرجتين المكملتين ({shades_ar})؟", "يسهل رسم وتظليل وتحديد العينين، ينزلق بسلاسة، ويثبت لـ 24 ساعة دون تكتل أو تسرب."),
        (f"هل يثبت لـ 24 ساعة ويندمج بسلاسة بدون تكتل؟", "نعم، مثبت سريرياً في الثبات 24 ساعة والدمج السلس والتدوم المقاوم للماء."),
        ("ما هي محتويات العبوة؟", "تأتي بقلم أنيق مزدوج الرأسين بضاغطين محكمين."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي الدرجة الفاتحة على الجفن، ارسمي بالداكنة عند الزوايا والرموش، وادمجيهما بأصابعك أو الفرشاة."),
        ("هل هو خالٍ من العطور وآمن للعيون الحساسة؟", "نعم، 100% خالٍ من العطور المهيجة ومختبر من أطباء العيون ومناسب لمستخدمي العدسات."),
        ("أين صُنع قلم ظلال جيرلان؟", "صُنع في فرنسا بواسطة LVMH Guerlain France."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات جيرلان لدى إكليل أبها أصلية 100%."),
        (f"ما هي ألوان القلم؟", f"درجتان مكملتان ساحرتان ({shades_ar})."),
        ("هل يناسب الاستخدام السريع والمكياج اليومي؟", "نعم، ممتاز لمكياج العينين السريع، اليومي، والمناسبات السريعة."),
        ("هل القلم مريح للحقيبة والسفر؟", "نعم، قلم مدمج مزدوج أنيق ومريح جداً بالحقيبة وللسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف مع إغلاق الغطاءين بإحكام."),
        ("هل جيرلان الماركة الأولى في أقلام الظلال الفاخرة؟", "نعم، Guerlain الماركة الفرنسية رقم 1 الأكثر شهرة وتفضيلاً في أقلام ظلال العيون الكريمية."),
        ("كم يدوم ثباته طوال اليوم؟", "يدوم لـ 24 ساعة متواصلة مقاوم للماء والعرق والتكسر."),
        ("هل ينشطف بمزيل المكياج بسهولة؟", "نعم، ينشطف بسلاسة بمزيل مكياج العيون دون شد الجفون."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل ينزلق بسهولة دون شد الجفن؟", "نعم، قوام كريمي شمعي ينزلق بسلاسة متناهية دون شد الجفن الرقيق."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والفتيات؟", "نعم، ممتاز للنساء والفتيات."),
        ("هل يناسب جميع ألوان العيون؟", "نعم، درجات متناسقة ومصممة لإبراز جميع ألوان العينين."),
        ("هل يصلح هدية ممتازة ضمن مكياج العيون؟", "نعم، منتج مكياج فرنسي فاخر وأساسي لكل حقيبة تجميل."),
        (f"هل يعيد المظهر المشرق والساحر للعينين؟", f"نعم، يمنح العينين مظهراً مظللاً ومحدداً بجمال ناصع."),
        ("هل تتوفر درجات أقلام ظلال جيرلان الأخرى؟", "نعم، تتوفر عائلة Guerlain Shadow Duo Sticks كاملة لدى إكليل أبها."),
        ("هل يمكن استخدامه كـ كحل للرموش أيضاً؟", "نعم، الرأس الداكن يمكن استخدامه ككحل محدد لخط الرموش."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury dual-ended creamy eyeshadow stick from Guerlain Paris (Guerlain Mad Eyes Contrast Shadow Duo) designed to deliver silky, highly pigmented creamy eyeshadow shades that outline, shadow, and highlight eyes in a single stroke without creasing or fallout. Built upon a waterproof silky wax formulation and two complementary dual-ended shades ({shades_en}).</p>
<p>Guerlain Dual Creamy Eyeshadow Stick smoothly shadows and defines eyelids with professional ease, imparting a captivating look for 24 hours while providing delicate skin hydration, leaving your eyelids touchably silky soft, hydrated, brilliantly glowing, and crease-proof from first stroke.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Dual-Ended Stick with 2 Complementary Shades ({shades_en}):</strong> Outlines and shadows eyes effortlessly.</li>
  <li><strong>Glides Smoothly without Tugging Eyelid Skin:</strong> Blends instantly with fingertips or a brush.</li>
  <li><strong>24-Hour Waterproof, Smudge-Proof & Crease-Proof Hold:</strong> Resists fading and gathering in eyelid lines.</li>
  <li><strong>Rich Concentrated Pigments in Matte & Shimmer Finishes:</strong> Defines eye beauty intensely.</li>
  <li><strong>Safe & Gentle for Sensitive Eyes & Contact Lens Wearers:</strong> Ophthalmologically tested formula.</li>
  <li><strong>Sleek Compact Luxury Travel Stick:</strong> Ideal format for handbags, touch-ups, and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply the lighter shade across the mobile eyelid as a base and highlighter.</li>
  <li><strong>Step 2:</strong> Outline and shade with the darker color along the outer corner and lash line for definition.</li>
  <li><strong>Step 3:</strong> Blend gently using fingertips or a brush for a seamless eye gradient (use daily with makeup).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Waxes & Emollient Oils:</strong> Provide a smooth creamy texture that glides without drying eyelid skin.</li>
  <li><strong>Waterproof Molecular Pigments:</strong> Ensure all-day color vibrancy and crease-free hold.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on eyelids and eye contours.</li>
  <li>Avoid direct contact inside eyes and cap tightly after use.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_title} for fast, waterproof, crease-free creamy eyeshadow shading and outlining.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Guerlain Paris (France)</td></tr>
  <tr><th>Category</th><td>Eye Makeup / Guerlain Dual Creamy Eyeshadow Sticks</td></tr>
  <tr><th>Product Type</th><td>Waterproof Crease-Proof Dual-Ended Creamy Eyeshadow Stick ({shades_en})</td></tr>
  <tr><th>Volume/Weight</th><td>Dual-Ended Compact Stick</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Eyelid Skin Types (Normal, Oily & Dry) & Contact Lens Wearers</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, waterproof, crease-proof & shadowed eyelids</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-tugging creamy wax gliding easily</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (irritant-free)</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Waxes, Waterproof Pigment Complexes, Eyelid Hydrating Oils</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>LVMH Guerlain France</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Waterproof Wax Matrix Integration & Crease-Proof Eyelid Shielding</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves eyeshadow powder fallout, creasing in eyelid folds, difficult blending, and color fading.</p>

<h3>Why choose Guerlain Dual Creamy Eyeshadow Stick?</h3>
<p>The silky wax matrix adheres instantly to eyelid skin forming a flexible barrier that resists natural oils and water for 24 hours.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a luxury waterproof crease-proof dual-ended creamy eyeshadow stick from Guerlain Paris with 2 complementary shades ({shades_en})."),
        (f"What are the benefits of the creamy texture and 2 shades ({shades_en})?", "Outline and shadow eyelids effortlessly, glide smoothly without tugging, and hold for 24 hours without creasing."),
        ("Does it hold for 24 hours and blend smoothly without creasing?", "Yes, clinically proven to hold for 24 hours waterproof and blend smoothly without creasing."),
        ("What volume and format are included?", "Dual-ended sleek compact stick with protective caps."),
        ("How do I use it correctly?", "Apply lighter shade across eyelid, outline with darker shade at outer corners and blend with fingers."),
        ("Is it fragrance-free and safe for sensitive eyes?", "Yes, 100% fragrance-free, ophthalmologically tested, and suitable for contact lens wearers."),
        ("Where is Guerlain Eyeshadow Stick manufactured?", "In France by LVMH Guerlain France."),
        ("How do I verify authenticity at Ekleel Abha?", "All Guerlain products at Ekleel Abha are 100% original."),
        (f"What color shades are included?", f"Two complementary luxury shades ({shades_en})."),
        ("Is it good for fast daily makeup and touch-ups?", "Yes, excellent for quick daily eye makeup, touch-ups, and travel."),
        ("Is the stick travel friendly?", "Yes, compact dual-ended stick ideal for handbags and travel."),
        ("How should I store it?", "In a cool, dry place with both caps closed tightly."),
        ("Is Guerlain a #1 French luxury makeup brand?", "Yes, Guerlain is the premier French luxury cosmetics house."),
        ("How long does it hold during the day?", "Holds for 24 continuous hours waterproof, smudge-proof, and crease-proof."),
        ("Does it remove easily with makeup remover?", "Yes, removes smoothly with eye makeup remover without tugging delicate eyelids."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it glide without tugging delicate eyelid skin?", "Yes, smooth creamy wax formula glides effortlessly without tugging."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and teens?", "Yes, suitable for both women and teens."),
        ("Is it good for all eye colors?", "Yes, curated complementary shades designed to enhance all eye colors."),
        ("Is it a nice makeup gift?", "Yes, an essential premier French luxury makeup gift."),
        (f"Does it restore vibrant shadowed eye beauty?", "Yes, gives eyes a beautifully defined radiant shadowed look."),
        ("Are other Guerlain eyeshadow stick shades available?", "Yes, the full Guerlain Dual Eyeshadow Stick range is available at Ekleel Abha."),
        ("Can the darker end be used as an eyeliner?", "Yes, the darker end can be used as a creamy eyeliner along lash lines."),
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
            "meta_description": f"اشتري {ar_title}. قلم ظلال عيون كريمي ثنائي فرنسي مقاوم للماء والكسرات بـ 24 ساعة ثبات. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. French luxury 24-hour waterproof crease-proof dual-ended creamy eyeshadow stick. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2169():
    return _make_eyeshadow_stick_b89(
        pid=2169, gtin="3346470432284",
        ar_title="قلم ظلال عيون كريمي ثنائي (احمر برقوقي، نحاسي  برقوقي)",
        en_title="Dual Creamy Eyeshadow Stick (Plum Red, Plum Copper)",
        shades_ar="أحمر برقوقي ونحاسي برقوقي", shades_en="Plum Red & Plum Copper",
        tags_ar=["جيرلان", "قلم_ظلال_جيرلان_أحمر_برقوقي", "ظلال_عيون_كريمي_ثنائي", "ظلال_مقاومة_للماء", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_plum_shadow_stick", "dual_creamy_eyeshadow", "waterproof_eyeshadow", "ekleel_abha"]
    )


def create_product_2170():
    return _make_eyeshadow_stick_b89(
        pid=2170, gtin="3346470432277",
        ar_title="قلم ظلال عيون كريمي ثنائي (بني دافئ - بني ذهبي)",
        en_title="Dual Creamy Eyeshadow Stick (Warm Brown - Golden Brown)",
        shades_ar="بني دافئ وبني ذهبي", shades_en="Warm Brown & Golden Brown",
        tags_ar=["جيرلان", "قلم_ظلال_جيرلان_بني_دافئ", "ظلال_عيون_كريمي_ثنائي", "ظلال_مقاومة_للماء", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_brown_shadow_stick", "dual_creamy_eyeshadow", "waterproof_eyeshadow", "ekleel_abha"]
    )


def create_product_2171():
    return _make_eyeshadow_stick_b89(
        pid=2171, gtin="3346470432291",
        ar_title="قلم ظلال عيون كريمي ثنائي (اخضر رمادي - اخضر لؤلؤي)",
        en_title="Dual Creamy Eyeshadow Stick (Grey Green - Pearl Green)",
        shades_ar="أخضر رمادي وأخضر لؤلؤي", shades_en="Grey Green & Pearl Green",
        tags_ar=["جيرلان", "قلم_ظلال_جيرلان_أخضر", "ظلال_عيون_كريمي_ثنائي", "ظلال_مقاومة_للماء", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_green_shadow_stick", "dual_creamy_eyeshadow", "waterproof_eyeshadow", "ekleel_abha"]
    )


print("Loaded all 5 Batch 89 builders complete")
