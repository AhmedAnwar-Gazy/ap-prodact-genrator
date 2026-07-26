import json, os

def _make_mufe_foundation_b96(pid, gtin, ar_title, en_title, shade_code, shade_ar, shade_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_title}</strong> كريم الأساس الفاخر الأسطوري عالي التغطية المخملية غير المرئية من الدار الفرنسية المحترفة ميك أب فور إيفر (Make Up For Ever HD Skin / Ultra HD Foundation {shade_code}) المصمم لمنح بشرة وجهك تغطية طبيعية فائقة النعومة، إخفاء العيوب 100%، وتوحيد لون ناصع بدرجة {shade_ar} ({shade_code}) ممتد لـ 24 ساعة دون تكتل أو جفاف. يرتكز هذا المستحضر الفرنسي الأصيل ({en_title}) على تقنية Micro-Skin Sync، حمض الهيالورونيك، وصبغات الكاميرا الدقيقة high-definition.</p>
<p>يعمل كريم أساس ميك أب فور إيفر بدرجة {shade_code} على التكيف الفوري مع حركات وجهك وتعبيراته، إخفاء التصبغات والمسام والخطوط الدقيقة كلياً، وتزويد خلايا الوجه بالرطوبة والنعومة الحريرية، ليترك بشرتك ناعمة كالحرير، موحدة اللون بدرجة {shade_ar}، ومفعمة بالشباب والإشراق أمام الكاميرا والعين المباشرة من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تغطية مخملية فائقة غير مرئية أمام الكاميرا (درجة {shade_code} - {shade_ar}):</strong> توحد الوجه وتخفي التصبغات.</li>
  <li><strong>ثبات عالي لـ 24 ساعة مقاوم للماء، العرق، والتلطخ:</strong> لا يتغير اللون أو يتكتل بالمسام.</li>
  <li><strong>ترطيب وتغذية فائقة بحمض الهيالورونيك:</strong> يحفظ طراوة ونعومة البشرة طوال اليوم.</li>
  <li><strong>ملمس خفيف سائل يندمج ويمتص بسلاسة:</strong> يمنح شعوراً خفيفاً بدون ثقل.</li>
  <li><strong>مختبر درماتولوجياً وآمن 100% لجميع أنواع البشرة:</strong> مناسب للبشرة الحساسة.</li>
  <li><strong>زجاجة فاخرة أيقونية بضاغط مريح سعة 30 مل:</strong> قمة الاحترافية الفرنسية في كريمات الأساس.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي بضع قطرات من كريم أساس ميك أب فور إيفر {shade_code} على بشرة الوجه النظيفة والمرطبة.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي الكريم من منتصف الوجه للخارج باستخدام الإسفنجة أو فرشاة الأساس المخصصة.</li>
  <li><strong>الخطوة الثالثة:</strong> ادمجي برفق للحصول على تغطية متجانسة ومشرقة (يُستعمل daily وعند المكياج).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>صبغات الكاميرا الدقيقة Micro-Skin Pigments & Hyaluronic Acid:</strong> تضمن تغطية مثالية غير مرئية وتمنع الجفاف.</li>
  <li><strong>بوليمرات التثبيت المرنة:</strong> تتكيف مع تعبيرات الوجه لمنع التكتل والتشقق بالخطوط.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي التجميلي على بشرة الوجه والرقبة.</li>
  <li>تجنبي التلامس المباشر لداخل العين واغلقي الغطاء بإحكام.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن {ar_title} لتغطية وتوحيد وإشراقة الوجه المخملية لـ 24 ساعة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ميك أب فور إيفر (Make Up For Ever France)</td></tr>
  <tr><th>الفئة</th><td>مكياج الوجه / كريمات أساس ميك أب فور إيفر الفاخرة HD 30ml</td></tr>
  <tr><th>نوع المنتج</th><td>كريم أساس احترافي عالي التغطية المخملية بحمض الهيالورونيك (درجة {shade_code} - {shade_ar})</td></tr>
  <tr><th>الحجم/الوزن</th><td>30 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (العادية، الجافة، الدهنية والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، موحد اللون بدرجة {shade_ar} {shade_code}، مخملي وغير مرئي للكاميرا</td></tr>
  <tr><th>الملمس</th><td>سائل دسم خفيف ينساب ويمتص بسلاسة</td></tr>
  <tr><th>العطر</th><td>عطر الزهور والمسك الفرنسي الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>صبغات الكاميرا الدقيقة، حمض الهيالورونيك، بوليمرات المرونة المائية</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>LVMH Make Up For Ever France</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون (من 18 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد تقنية Micro-Skin Sync في كريم أساس ميك أب فور إيفر (MUFE HD Skin {shade_code})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم أساس ميك أب فور إيفر بدرجة {shade_code} مشكلة عدم توحد لون الوجه، ظهور العيوب أمام الكاميرات، تكتل المكياج بالخطوط، والبهتان.</p>

<h3>لماذا تنجح تركيبة Make Up For Ever HD Skin {shade_code}؟</h3>
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

    faqs_data = [
        (f"ما هو {ar_title}؟", f"هو كريم أساس احترافي عالي التغطية المخملية بحمض الهيالورونيك بدرجة {shade_ar} ({shade_code}) من ميك أب فور إيفر (30 مل)."),
        (f"ما هي فوائد صبغات الكاميرا الدقيقة وحمض الهيالورونيك بدرجة {shade_code}؟", "توحد لون البشرة، تخفي العيوب والتصبغات كلياً، وتمنح ترطيباً وتغطية مخملية غير مرئية لـ 24 ساعة."),
        ("هل يغطي العيوب ويوحد الوجه ويرطب لـ 24 ساعة بدون تكتل؟", "نعم، مثبت سريرياً في توحيد الوجه وتغطية العيوب وتوفير ترطيب وتغطية خالية من التكتل."),
        ("ما حجم العبوة؟", "تأتي بزجاجة أنيقة فاخرة بضاغط سعة 30 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي قطرات على البشرة والمرطب، وزعي بالإسفنجة أو الفرشاة واددمجي من المنتصف للخارج."),
        ("هل هو آمن ومختبر درماتولوجياً؟", "نعم، 100% آمن ومختبر درماتولوجياً ومناسب لجميع أنواع البشرة."),
        ("أين صُنع كريم أساس ميك أب فور إيفر؟", "صُنع في فرنسا بواسطة LVMH Make Up For Ever France."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات ميك أب فور إيفر لدى إكليل أبها أصلية 100%."),
        (f"ما درجة كريم أساس ميك أب فور إيفر؟", f"درجة {shade_code} ({shade_ar})."),
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
        (f"هل يعيد المظهر المشرق والساحر للوجه بدرجة {shade_code}؟", f"نعم، يمنح الوجه مظهراً موحداً ومخملي النقاء كالحرير."),
        ("هل تتوفر درجات كريم أساس ميك أب فور إيفر الأخرى؟", "نعم، تتوفر عائلة Make Up For Ever Foundations كاملة لدى إكليل أبها."),
        ("هل يحمي من التأثيرات البيئية؟", "نعم، مدعم بمضادات الأكسدة التي تحمي البشرة أثناء النهار."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury high-coverage invisible HD liquid foundation from professional House Make Up For Ever France (Make Up For Ever HD Skin / Ultra HD Foundation {shade_code} {shade_en}) designed to deliver ultra-smooth natural velvet coverage, 100% blemish concealment, and a 24-hour even {shade_en} complexion (Shade {shade_code}) without creasing or drying. Built upon Micro-Skin Sync technology, hydrating Hyaluronic Acid, and high-definition micro-camera pigments.</p>
<p>Make Up For Ever Foundation {shade_code} smoothly adapts to facial expressions, conceals hyperpigmentation, enlarged pores, and fine lines, while infusing skin cells with moisture and silky softness, leaving your face touchably silky soft, beautifully even-toned in {shade_en} {shade_code}, and camera-ready radiant from first stroke.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Camera-Invisible High Velvet Coverage (Shade {shade_code}):</strong> Evens face and conceals spots.</li>
  <li><strong>24-Hour Waterproof, Sweat-Proof & Smudge-Proof Hold:</strong> Color does not shift or cake.</li>
  <li><strong>Intensive 24-Hour Hydration with Hyaluronic Acid:</strong> Preserves skin softness all day long.</li>
  <li><strong>Lightweight Fluid Liquid Glides Effortlessly:</strong> Blends without heavy weight.</li>
  <li><strong>Dermatologically Tested Safe for All Skin Types:</strong> 100% safe for sensitive facial skin.</li>
  <li><strong>Iconic 30ml Luxury Pump Dispenser Bottle:</strong> The pinnacle of professional French foundation design.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a few drops of Make Up For Ever foundation {shade_code} onto clean, moisturized skin.</li>
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
  <li>Anyone seeking {en_title} for camera-invisible velvet coverage, tone evening, and 24-hour hydration.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Make Up For Ever (France)</td></tr>
  <tr><th>Category</th><td>Face Makeup / Make Up For Ever Luxury HD Foundations 30ml</td></tr>
  <tr><th>Product Type</th><td>Professional High-Coverage Hyaluronic Acid Foundation (Shade {shade_code} {shade_en})</td></tr>
  <tr><th>Volume/Weight</th><td>30 ml Pump Bottle</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Normal, Dry, Oily & Combination Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, even-toned in {shade_en} {shade_code} & camera-invisible velvet face</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-heavy fluid liquid foundation</td></tr>
  <tr><th>Fragrance</th><td>100% Luxurious French floral musk fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Micro-Skin Pigments, Hyaluronic Acid, Flexible Polymers</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>LVMH Make Up For Ever France</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 18+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Micro-Skin Sync Technology & HD Pigment Integration</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves uneven facial skin tone, flash-photography flashback, foundation creasing in lines, and skin dullness.</p>

<h3>Why choose Make Up For Ever HD Skin {shade_code}?</h3>
<p>Micro-skin pigments flex with facial movement preventing cakeiness while Hyaluronic Acid locks in skin hydration.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a professional high-coverage Hyaluronic Acid liquid foundation from Make Up For Ever in Shade {shade_code} {shade_en} (30ml)."),
        (f"What are the benefits of Micro-Skin Pigments and Hyaluronic Acid in Shade {shade_code}?", "Even skin tone, conceal blemishes, and deliver 24-hour hydration and camera-invisible velvet coverage."),
        ("Does it conceal imperfections and hydrate for 24 hours without creasing?", "Yes, clinically proven to even skin tone, conceal blemishes, and deliver 24-hour hydration without creasing."),
        ("What volume is contained in this bottle?", "30ml iconic luxury pump bottle."),
        ("How do I use it correctly?", "Apply drops to moisturized skin, smooth with brush or sponge from center outwards."),
        ("Is it safe and dermatologically tested?", "Yes, 100% safe, dermatologically tested, and suitable for all facial skin types."),
        ("Where is Make Up For Ever Foundation manufactured?", "In France by LVMH Make Up For Ever France."),
        ("How do I verify authenticity at Ekleel Abha?", "All Make Up For Ever products at Ekleel Abha are 100% original."),
        (f"What shade is Make Up For Ever Foundation?", f"Shade {shade_code} ({shade_en})."),
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
        (f"Does it restore smooth radiant skin in Shade {shade_code}?", f"Yes, gives facial skin an even-toned {shade_en} radiant look."),
        ("Are other Make Up For Ever foundation shades available?", "Yes, the full MUFE Foundation shade range is available at Ekleel Abha."),
        ("Does it protect against environmental stressors?", "Yes, enriched with antioxidants protecting skin throughout the day."),
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
            "meta_description": f"اشتري {ar_title}. كريم أساس فرنسي احترافي عالي التغطية المخملية بحمض الهيالورونيك. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. French luxury 24-hour high-coverage Hyaluronic Acid liquid foundation. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2202():
    return _make_mufe_foundation_b96(
        pid=2202, gtin="3548752085397",
        ar_title="كريم أساس ميك أب فور ايفر جولدن ساند (Y375)30مل",
        en_title="Make Up For Ever Foundation - Golden Sand (Y375) 30ml",
        shade_code="Y375", shade_ar="جولدن ساند (رملي ذهبي)", shade_en="Golden Sand",
        tags_ar=["ميك_أب_فور_إيفر", "كريم_أساس_ميك_أب_فور_إيفر_Y375", "فاونديشن_جولدن_ساند", "كريم_أساس_احترافي", "إكليل_أبها"],
        tags_en=["make_up_for_ever", "mufe_foundation_y375", "golden_sand_foundation", "liquid_foundation", "ekleel_abha"]
    )


def create_product_2203():
    return _make_mufe_foundation_b96(
        pid=2203, gtin="3548752085410",
        ar_title="كريم أساس ميك أب فور ايفر عسلي ذهبي (Y405)30مل",
        en_title="Make Up For Ever Foundation - Golden Honey (Y405) 30ml",
        shade_code="Y405", shade_ar="عسلي ذهبي", shade_en="Golden Honey",
        tags_ar=["ميك_أب_فور_إيفر", "كريم_أساس_ميك_أب_فور_إيفر_Y405", "فاونديشن_عسلي_ذهبي", "كريم_أساس_احترافي", "إكليل_أبها"],
        tags_en=["make_up_for_ever", "mufe_foundation_y405", "golden_honey_foundation", "liquid_foundation", "ekleel_abha"]
    )


def create_product_2204():
    return _make_mufe_foundation_b96(
        pid=2204, gtin="3548752085373",
        ar_title="كريم أساس ميك أب فور ايفر ديزيرت (Y365)30مل",
        en_title="Make Up For Ever Desert Foundation (Y365) 30ml",
        shade_code="Y365", shade_ar="ديزيرت (صحراوي)", shade_en="Desert",
        tags_ar=["ميك_أب_فور_إيفر", "كريم_أساس_ميك_أب_فور_إيفر_Y365", "فاونديشن_ديزيرت", "كريم_أساس_احترافي", "إكليل_أبها"],
        tags_en=["make_up_for_ever", "mufe_foundation_y365", "desert_foundation", "liquid_foundation", "ekleel_abha"]
    )


def create_product_2205():
    return _make_mufe_foundation_b96(
        pid=2205, gtin="3548752165273",
        ar_title="كريم أساس ميك أب فور ايفر لون القرفه (Y412)30مل",
        en_title="MAKE UP FOR EVER Foundation - Cinnamon (Y412) 30ml",
        shade_code="Y412", shade_ar="قرفة (Cinnamon)", shade_en="Cinnamon",
        tags_ar=["ميك_أب_فور_إيفر", "كريم_أساس_ميك_أب_فور_إيفر_Y412", "فاونديشن_القرفة", "كريم_أساس_احترافي", "إكليل_أبها"],
        tags_en=["make_up_for_ever", "mufe_foundation_y412", "cinnamon_foundation", "liquid_foundation", "ekleel_abha"]
    )


def create_product_2206():
    return _make_mufe_foundation_b96(
        pid=2206, gtin="3548752165266",
        ar_title="كريم أساس ميك أب فور ايفر ذهبي غامق (Y383)30مل",
        en_title="MAKE UP FOR EVER Foundation Dark Golden (Y383) 30ml",
        shade_code="Y383", shade_ar="ذهبي غامق", shade_en="Dark Golden",
        tags_ar=["ميك_أب_فور_إيفر", "كريم_أساس_ميك_أب_فور_إيفر_Y383", "فاونديشن_ذهبي_غامق", "كريم_أساس_احترافي", "إكليل_أبها"],
        tags_en=["make_up_for_ever", "mufe_foundation_y383", "dark_golden_foundation", "liquid_foundation", "ekleel_abha"]
    )


print("Loaded all 5 Batch 96 builders complete")
