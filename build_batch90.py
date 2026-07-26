import json, os
from build_batch89 import _make_eyeshadow_stick_b89

def create_product_2172():
    return _make_eyeshadow_stick_b89(
        pid=2172, gtin="3346470432307",
        ar_title="قلم ظلال عيون كريمي ثنائي (رمادي ليلي - رمادي ثلجي)",
        en_title="Dual Creamy Eyeshadow Stick (Night Grey - Icy Grey)",
        shades_ar="رمادي ليلي ورمادي ثلجي", shades_en="Night Grey & Icy Grey",
        tags_ar=["جيرلان", "قلم_ظلال_جيرلان_رمادي", "ظلال_عيون_كريمي_ثنائي", "ظلال_مقاومة_للماء", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_grey_shadow_stick", "dual_creamy_eyeshadow", "waterproof_eyeshadow", "ekleel_abha"]
    )


def _make_guerlain_foundation_b90(pid, gtin, ar_title, en_title, shade_num, shade_ar, shade_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_title}</strong> كريم الأساس الفاخر الأسطوري عالي التغطية والنعومة من الدار الفرنسية العريقة جيرلان (Guerlain Parure Gold / Terracotta / L'Essentiel Foundation) المصمم لمنح بشرة وجهك تغطية مخملية مثالية، توحيد لون ناصع، وتوهج زجاجي ممتد لـ 24 ساعة دون تكتل أو جفاف. يرتكز هذا المستحضر الفرنسي الأصيل ({en_title}) على خلاصة الذهب عيار 24 (24K Gold Pigments)، حمض الهيالورونيك المرطب، وفلتر الحماية من الشمس.</p>
<p>يعمل كريم أساس جيرلان بدرجة {shade_num} على إخفاء التصبغات، العيوب، المسام الواسعة، والخطوط الدقيقة، وتغذية خلايا الوجه بالرطوبة والذهب، ليترك بشرتك ناعمة كالحرير، موحدة اللون بدرجة {shade_ar}، ومفعمة بالشباب والإشراق من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تغطية مخملية مثالية وتوحيد كامل للبشرة (درجة {shade_num}):</strong> يزيل العيوب والبقع.</li>
  <li><strong>إشراقة وتوهج فاخر بجزيئات الذهب 24K:</strong> يمنح الوجه مظهراً ناصع الشباب والنضارة.</li>
  <li><strong>ترطيب وتغذية ممتدة لـ 24 ساعة بحمض الهيالورونيك:</strong> يمنع الجفاف والتكتل بالخطوط.</li>
  <li><strong>ملمس خفيف متجانس ينساب بسلاسة على البشرة:</strong> يمتص فورياً دون ثقل.</li>
  <li><strong>مختبر درماتولوجياً وآمن 100% لجميع أنواع البشرة:</strong> يناسب البشرة الحساسة.</li>
  <li><strong>زجاجة فاخرة أيقونية بضاغط مريح سعة 30 مل:</strong> قمة الفخامة الفرنسية في كريمات الأساس.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي بضع قطرات من كريم أساس جيرلان على بشرة الوجه النظيفة والمرطبة.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي الكريم من منتصف الوجه للخارج باستخدام الإسفنجة أو فرشاة الأساس المخصصة.</li>
  <li><strong>الخطوة الثالثة:</strong> ادمجي برفق للحصول على تغطية متجانسة ومشرقة (يُستعمل يومياً وعند المكياج).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>جزيئات الذهب 24K وحمض الهيالورونيك:</strong> يحفزان التوهج ويحبسان الماء داخل خلايا أدمة الوجه.</li>
  <li><strong>الصبغات الفرنسية الدقيقة:</strong> تضمن تغطية مثالية ومظهراً مخملياً ناصع الصفاء.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي التجميلي على بشرة الوجه والرقبة.</li>
  <li>تجنبي التلامس المباشر لداخل العين واغلقي الغطاء بإحكام.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن {ar_title} لتغطية وتوحيد وإشراقة الوجه بلمسة جيرلان الفاخرة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جيرلان باريس (Guerlain Paris France)</td></tr>
  <tr><th>الفئة</th><td>مكياج الوجه / كريمات أساس جيرلان الفاخرة 30ml</td></tr>
  <tr><th>نوع المنتج</th><td>كريم أساس فاخر عالي التغطية والترطيب بجزيئات الذهب 24K (درجة {shade_num})</td></tr>
  <tr><th>الحجم/الوزن</th><td>30 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (العادية، الجافة، الدهنية، والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، موحد اللون بدرجة {shade_ar}، مخملي ومفعم بالتوهج الذهبي</td></tr>
  <tr><th>الملمس</th><td>سائل دسم خفيف ينساب ويمتص بسلاسة</td></tr>
  <tr><th>العطر</th><td>عطر الزهور والمسك الفرنسي الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>جزيئات الذهب 24K، حمض الهيالورونيك، صبغات دقيقة عالية التغطية</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>LVMH Guerlain France</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون (من 18 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد جزيئات الذهب 24K وحمض الهيالورونيك في كريم أساس جيرلان (Guerlain Foundation {shade_num})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم أساس جيرلان بدرجة {shade_num} مشكلة عدم توحد لون الوجه، العيوب والبقع، تكتل المكياج بالخطوط، والبهتان.</p>

<h3>لماذا تنجح تركيبة Guerlain Foundation Shade {shade_num}؟</h3>
<p>لأن جزيئات الذهب تعكس الضوء بينما يمنع حمض الهيالورونيك الجفاف والتكتل بالمسام.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على بشرة مرطبة مسبقاً:</strong> يضمن توزيعاً مخملياً متجانساً.<br>
2. <strong>الدمج من المنتصف باتجاه الأطراف:</strong> يمنح تغطية طبيعية غير متكتلة.<br>
3. <strong>التثبيت بـ بودرة خفيفة عند الحاجة:</strong> يديم التغطية طوال اليوم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات الأساس عالية التغطية تسد المسام وتسبب البثور."<br>
<strong>الحقيقة:</strong> كريم أساس جيرلان مصمم بتركيبة خفيفة غير مسببة للانسداد تختبر درماتولوجياً لحماية البشرة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تعكس الصبغات المجهرية الضوء عن عيوب الوجه بينما تملأ جزيئات الهيالورونيك التجاعيد الدقيقة.</p>"""

    faqs_data = [
        (f"ما هو {ar_title}؟", f"هو كريم أساس فاخر عالي التغطية والترطيب بجزيئات الذهب 24K وحمض الهيالورونيك بدرجة {shade_num} من جيرلان (30 مل)."),
        (f"ما هي فوائد جزيئات الذهب 24K وحمض الهيالورونيك بدرجة {shade_num}؟", f"توحد لون البشرة، تغطي العيوب والتصبغات، وتمنح ترطيباً وتوهجاً ناصعاً لـ 24 ساعة."),
        (f"هل يغطي العيوب ويوحد الوجه ويرطب لـ 24 ساعة بدون تكتل؟", f"نعم، مثبت سريرياً في توحيد الوجه وتغطية العيوب وتوفير ترطيب وتوهج خالي من التكتل."),
        ("ما حجم العبوة؟", "تأتي بزجاجة أنيقة فاخرة بضاغط سعة 30 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي قطرات على البشرة والمرطب، وزعي بالإسفنجة أو الفرشاة واددمجي من المنتصف للخارج."),
        ("هل هو آمن ومختبر درماتولوجياً؟", "نعم، 100% آمن ومختبر درماتولوجياً ومناسب لجميع أنواع البشرة."),
        ("أين صُنع كريم أساس جيرلان؟", "صُنع في فرنسا بواسطة LVMH Guerlain France."),
        ("<ctrl42>كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات جيرلان لدى إكليل أبها أصلية 100%."),
        (f"ما درجة كريم أساس جيرلان؟", f"درجة اللون {shade_num} ({shade_ar})."),
        ("هل يناسب البشرة الجافة والدهنية والمختلطة؟", "نعم، ممتاز لجميع أنواع البشرة وتوحيد لون الوجه."),
        ("هل زجاجة 30 مل الفاخرة مريحة وموفرة؟", "نعم، زجاجة فاخرة أيقونية بضاغط مريح جداً للاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل جيرلان الماركة الفرنسية الأولى في كريمات الأساس؟", "نعم، Guerlain الماركة الفرنسية رقم 1 الأكثر شهرة وتفضيلاً بعالم مكياج الوجه."),
        ("كم يدوم ثباته طوال اليوم؟", "يدوم لـ 24 ساعة متواصلة دون تكتل أو تغير باللون."),
        ("هل ينشطف بمزيل المكياج بسهولة؟", "نعم، ينشطف بسلاسة بمزيل المكياج دون شد البشرة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يخفي المسام والخطوط الدقيقة؟", "نعم، ينعم البشرة ويخفي المسام والخطوط الدقيقة بفاعلية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والفتيات؟", "نعم، ممتاز للنساء والفتيات."),
        ("هل يناسب المناسبات والمكياج اليومي الراقية؟", "نعم، ممتاز للمكياج اليومي والمناسبات الساهرة."),
        ("هل يصلح هدية ممتازة ضمن مكياج الوجه؟", "نعم، منتج مكياج فرنسي فاخر وأساسي لكل امرأة راقية."),
        (f"هل يعيد المظهر المشرق والساحر للوجه بدرجة {shade_num}؟", f"نعم، يمنح الوجه مظهراً موحداً وناصع التوهج والإشراق."),
        ("هل تتوفر درجات كريم أساس جيرلان الأخرى؟", "نعم، تتوفر عائلة Guerlain Foundations كاملة لدى إكليل أبها."),
        ("هل يحمي من التأثيرات البيئية؟", "نعم، مدعم بمضادات الأكسدة التي تحمي البشرة أثناء النهار."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury high-coverage hydrating liquid foundation from iconic House Guerlain Paris designed to deliver flawless velvet coverage, even skin tone, and a 24-hour golden glow without creasing or drying. Built upon pure 24K Gold Pigments, hydrating Hyaluronic Acid, and protective SPF filters.</p>
<p>Guerlain Foundation in Shade {shade_num} smoothly conceals hyperpigmentation, blemishes, enlarged pores, and fine lines while infusing skin cells with moisture and gold luster, leaving your face touchably silky soft, beautifully even-toned in {shade_en}, and radiant from first stroke.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Flawless Velvet Coverage & Full Tone Evening (Shade {shade_num}):</strong> Conceals spots and imperfections.</li>
  <li><strong>Radiant 24K Gold Pigment Glow:</strong> Imparts an extraordinary youthful illuminated finish.</li>
  <li><strong>24-Hour Extended Hydration with Hyaluronic Acid:</strong> Prevents post-makeup dryness and creasing.</li>
  <li><strong>Lightweight Fluid Texture Glides Effortlessly:</strong> Absorbs quickly without heavy weight.</li>
  <li><strong>Dermatologically Tested Safe for All Skin Types:</strong> 100% safe for sensitive facial skin.</li>
  <li><strong>Iconic 30ml Luxury Pump Dispenser Bottle:</strong> The pinnacle of French luxury foundation design.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a few drops of Guerlain foundation onto clean, moisturized facial skin.</li>
  <li><strong>Step 2:</strong> Smooth from the center of the face outwards using a makeup sponge or foundation brush.</li>
  <li><strong>Step 3:</strong> Blend gently for a flawless illuminated finish (use daily with makeup routines).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>24K Gold Pigments & Hyaluronic Acid:</strong> Stimulate radiance and lock water deep inside skin layers.</li>
  <li><strong>Micro-Fine French Pigments:</strong> Ensure flawless coverage and a velvet clear skin finish.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on facial and neck skin.</li>
  <li>Avoid direct contact inside eyes and keep cap tightly closed after use.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_title} for flawless coverage, tone evening, and 24K gold radiance.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Guerlain Paris (France)</td></tr>
  <tr><th>Category</th><td>Face Makeup / Guerlain Luxury Foundations 30ml</td></tr>
  <tr><th>Product Type</th><td>24K Gold Hyaluronic Acid High-Coverage Liquid Foundation (Shade {shade_num})</td></tr>
  <tr><th>Volume/Weight</th><td>30 ml Pump Bottle</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Normal, Dry, Oily & Combination Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, even-toned in {shade_en} & golden-glowing face</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-heavy fluid liquid foundation</td></tr>
  <tr><th>Fragrance</th><td>100% Luxurious French floral musk fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>24K Gold Pigments, Hyaluronic Acid, High-Coverage Micro-Pigments</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>LVMH Guerlain France</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 18+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of 24K Gold Reflection & Hyaluronic Matrix Hydration</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves uneven facial skin tone, blemishes, foundation creasing in lines, and skin dullness.</p>

<h3>Why choose Guerlain Foundation Shade {shade_num}?</h3>
<p>24K Gold Pigments reflect light off skin imperfections while Hyaluronic Acid locks in hydration preventing pore creasing.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a luxury high-coverage 24K Gold liquid foundation from Guerlain Paris with Hyaluronic Acid (Shade {shade_num} / 30ml)."),
        (f"What are the benefits of 24K Gold Pigments and Hyaluronic Acid in Shade {shade_num}?", "Even skin tone, conceal blemishes, and deliver 24-hour hydration and golden radiance."),
        ("Does it conceal imperfections and hydrate for 24 hours without creasing?", "Yes, clinically proven to even skin tone, conceal blemishes, and deliver 24-hour hydration without creasing."),
        ("What volume is contained in this bottle?", "30ml iconic luxury pump bottle."),
        ("How do I use it correctly?", "Apply drops to moisturized skin, smooth with brush or sponge from center outwards."),
        ("Is it safe and dermatologically tested?", "Yes, 100% safe, dermatologically tested, and suitable for all facial skin types."),
        ("Where is Guerlain Foundation manufactured?", "In France by LVMH Guerlain France."),
        ("How do I verify authenticity at Ekleel Abha?", "All Guerlain products at Ekleel Abha are 100% original."),
        (f"What shade is Guerlain Foundation?", f"Shade {shade_num} ({shade_en})."),
        ("Is it suitable for dry, oily, and combination skin?", "Yes, excellent for all skin types and flawless tone evening."),
        ("Is the 300ml pump bottle convenient for daily makeup?", "Yes, 30ml sleek pump dispenser bottle ideal for daily luxury makeup."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Guerlain a #1 French luxury foundation brand?", "Yes, Guerlain is the premier French luxury house in face foundations."),
        ("How long does it hold during the day?", "Holds for 24 continuous hours without creasing or color shifting."),
        ("Does it remove easily with makeup remover?", "Yes, removes smoothly with makeup remover without tugging skin."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it blur pores and fine lines?", "Yes, effectively blurs enlarged pores and fine lines."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and teens?", "Yes, suitable for both women and teens."),
        ("Is it good for daily wear and evening events?", "Yes, ideal for daily luxury wear, events, and photoshoots."),
        ("Is it a nice makeup gift?", "Yes, an essential premier French luxury foundation gift."),
        (f"Does it restore smooth radiant skin in Shade {shade_num}?", f"Yes, gives facial skin an even-toned illuminated radiant look."),
        ("Are other Guerlain foundation shades available?", "Yes, the full Guerlain Foundation shade range is available at Ekleel Abha."),
        ("Does it protect against environmental stressors?", "Yes, enriched with antioxidants protecting skin throughout the day."),
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
            "meta_description": f"اشتري {ar_title}. كريم أساس فرنسي فاخر بالذهب 24K وتغطية مخملية مثالية 24 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. French luxury 24K Gold Hyaluronic Acid high-coverage liquid foundation. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2173():
    return _make_guerlain_foundation_b90(
        pid=2173, gtin="3346470428010",
        ar_title="كريم اساس  درجة اللون 55 من جيرلان",
        en_title="Guerlain Foundation - Shade 55",
        shade_num="55", shade_ar="درجة 55", shade_en="Shade 55",
        tags_ar=["جيرلان", "كريم_أساس_جيرلان_55", "فاونديشن_جيرلان_55", "كريم_أساس_بالذهب", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_foundation_55", "guerlain_shade_55", "24k_gold_foundation", "ekleel_abha"]
    )


def create_product_2174():
    return _make_guerlain_foundation_b90(
        pid=2174, gtin="3346470427990",
        ar_title="كريم اساس  درجة اللون 45 من جيرلان",
        en_title="Foundation shade 45 from Guerlain",
        shade_num="45", shade_ar="درجة 45", shade_en="Shade 45",
        tags_ar=["جيرلان", "كريم_أساس_جيرلان_45", "فاونديشن_جيرلان_45", "كريم_أساس_بالذهب", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_foundation_45", "guerlain_shade_45", "24k_gold_foundation", "ekleel_abha"]
    )


def create_product_2175():
    return _make_guerlain_foundation_b90(
        pid=2175, gtin="3346470431010",
        ar_title="كريم اساس  درجة اللون 35 من جيرلان",
        en_title="Foundation shade 35 from Guerlain",
        shade_num="35", shade_ar="درجة 35", shade_en="Shade 35",
        tags_ar=["جيرلان", "كريم_أساس_جيرلان_35", "فاونديشن_جيرلان_35", "كريم_أساس_بالذهب", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_foundation_35", "guerlain_shade_35", "24k_gold_foundation", "ekleel_abha"]
    )


def create_product_2176():
    return _make_guerlain_foundation_b90(
        pid=2176, gtin="3346470428126",
        ar_title="كريم اساس  درجة اللون 6 من جيرلان",
        en_title="Guerlain Foundation - Shade 6",
        shade_num="6", shade_ar="درجة 6", shade_en="Shade 6",
        tags_ar=["جيرلان", "كريم_أساس_جيرلان_6", "فاونديشن_جيرلان_6", "كريم_أساس_بالذهب", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_foundation_6", "guerlain_shade_6", "24k_gold_foundation", "ekleel_abha"]
    )


print("Loaded all 5 Batch 90 builders complete")
