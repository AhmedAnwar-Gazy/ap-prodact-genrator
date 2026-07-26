import json, os

def _make_hair_styling_b56(pid, gtin, ar_name, en_name, brand_ar, brand_en, type_ar, type_en, volume_ar, volume_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> مستحضر تصفيف وتثبيت الشعر الفاخر الأصيل من {brand_ar} المصمم لمنح شعرك ثباتاً مثالياً، لمعاناً ساحراً، وتحديداً جذاباً للتوجات والتسريحة يدوم طوال اليوم دون إثقال. يرتكز هذا المستحضر الأصيل ({en_name}) على بوليمرات التثبيت المرنة، الفيتامينات المغذية لجيلاتين الشعر، وخلاصات التنعيم المنشطة.</p>
<p>يعمل مستحضر {brand_ar} على تثبيت التسريحات وتشكيل الخصلات بمرونة كاملة، حماية الشعر من التجعّد والرطوبة الجوية، وإبراز كمال المظهر واللمعان الطبيعي، ليترك شعرك مصففاً بأناقة، مرناً، وناعماً كالحرير طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تثبيت قوي ومرن للتسريحات لـ 24 ساعة:</strong> يحافظ على شكل التسريحة والتوجات دون تيبس.</li>
  <li><strong>إبراز اللمعان الطبيعي والبياض الصحي للشعر:</strong> يضفي بريقاً ونعومة حريرية على ألياف الشعر.</li>
  <li><strong>مقاومة الرطوبة والتطاير والجفاف:</strong> يحمي الشعر من التعديات الجوية والهيشات.</li>
  <li><strong>سهل التمشيط والإزالة دون قشور:</strong> لا يترك أي ترسبات أو قشور بيضاء.</li>
  <li><strong>تركيبة خفيفة الوزن مغذية:</strong> لا تثقل الشعر ولا تسبب تلاصقه.</li>
  <li><strong>عبوة سعة {volume_ar}:</strong> حجم ممتاز للاستخدام اليومي والتصفيف الاحترافي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> وزعي/رشّي كمية مناسبة من مستحضر {brand_ar} على شعر رطب أو جاف.</li>
  <li><strong>الخطوة الثانية:</strong> صففي الشعر بأطراف الأصابع أو المشط/الفرشاة للشكل المطلوب (يُستعمل عند التصفيف).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>بوليمرات التثبيت المرنة المتطورة:</strong> تشكل غلافاً ميكروياً حول ألياف الشعر ليثبت التسريحة بحرية.</li>
  <li><strong>الفيتامينات والمكونات المنعمة:</strong> تغذي ساق الشعر وتحميه من التلف والجفاف.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على الشعر فقط.</li>
  <li>تجنبي التلامس مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} للتثبيت المرن واللمعان والسيطرة على الشعر والتسريحة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>{brand_ar} ({brand_en})</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / مستحضرات تصفيف وتثبيت الشعر من {brand_ar} {volume_ar}</td></tr>
  <tr><th>نوع المنتج</th><td>مستحضر تصفيف وتثبيت الشعر ({type_ar}) لثبات ولمعان يدوم طوال اليوم ({volume_ar})</td></tr>
  <tr><th>الحجم/الوزن</th><td>{volume_ar}</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع انواع الشعر (العادي، المموج، الجاف والدهني)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر مصفف بثبات أنيق، مرن، براق وخالٍ من القشور واللزوجة</td></tr>
  <tr><th>الملمس</th><td>سائل/رغوة/بخاخ ناعم خفيف الوزن</td></tr>
  <tr><th>العطر</th><td>عطر {brand_ar} الأنيق الفواح</td></tr>
  <tr><th>المكونات النشطة</th><td>بوليمرات تثبيت مرنة، فيتامينات مغذية، مركبات تنعيم</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا / فرنسا / السعودية</td></tr>
  <tr><th>الشركة المصنعة</th><td>{brand_en} Beauty Care</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد البوليمرات المرنة والمركبات المنعمة في مستحضر {brand_ar}</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مستحضر تصفيف {brand_ar} مشكلة تطاير الشعر، فقدان تحديد التموجات، التجعّد بفعل الرطوبة، والشعر الباهت.</p>

<h3>لماذا تنجح تركيبة {brand_ar}؟</h3>
<p>لأن البوليمرات الدقيقة تلتصق بساق الشعر مكونة شبكة تثبيت غير مرئية تمنح المرونة وتمنع التكسر.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على شعر رطب أو جاف حسب التسريحة:</strong> يمنح أفضل تشكيل وتثبيت.<br>
2. <strong>التمشيط الخفيف في نهاية اليوم:</strong> يزيل البوليمرات بسهولة دون الحاجة لغسيل قاسي.<br>
3. <strong>تجنب الإفراط الكثيف:</strong> كمية معتدلة تكفي لتثبيت يدوم طوال اليوم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مستحضرات تثبيت الشعر تسبب القشرة وسقوط الشعر."<br>
<strong>الحقيقة:</strong> هذا المنتج مصمم بتركيبة مرنة خالية من الترسبات الثقيلة لا تؤثر على فروة الرأس أو البصيلات.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تشكل البوليمرات غشاء بيولوجياً واقياً ينظم تبخر الرطوبة من ألياف الكيراتين ويمنع تأثير التوتر السطحي الجوي.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو مستحضر تصفيف وتثبيت الشعر من {brand_ar} لمنح الشعر ثباتاً ومرونة ولمعاناً ({volume_ar})."),
        ("ما هي فوائد البوليمرات المرنة والفيتامينات؟", "تثبت البوليمرات التسريحة والتوجات بحرية دون تيبس، بينما تغذي الفيتامينات الشعر وتمنحه لمعاناً براقاً."),
        ("هل يمنح ثباتاً طوال اليوم ومقاومة للرطوبة؟", "نعم، مثبت سريرياً في الحفاظ على شكل التسريحة ومقاومة التجعّد والرطوبة طوال اليوم."),
        (f"ما حجم العبوة؟", f"تأتي بسعة {volume_ar}."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي/رشّي على شعر رطب أو جاف وصففي بالشكل المطلوب بلمسات ناعمة."),
        ("هل يترك قشوراً بيضاء أو لزوجة؟", "لا، تركيبة مطورة تمنح ثباتاً ونعومة دون أي ترسبات أو قشور بيضاء."),
        (f"أين صُنع مستحضر {brand_ar}؟", "صُنع بأعلى معايير جودة العناية بالشعر العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {brand_ar} الأنيق الفواح."),
        ("هل يسهل إزالته بالتمشيط أو الشامبو؟", "نعم، يزول بسهولة بالفرشاة أو عند الغسيل بالشامبو."),
        (f"هل العبوة {volume_ar} تكفي للاستخدام المنتظم؟", "نعم، تكفي لعدة أسابيع من الاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الحرارة."),
        (f"هل {brand_ar} علامة موثوقة في تصفيف الشعر؟", f"نعم، {brand_en} علامة رائدة وموثوقة جداً في العناية بالشعر وتصفيفه."),
        ("كم مرة يومياً؟", "عند تصفيف الشعر."),
        ("هل يناسب جميع أنواع الشعر؟", "نعم، مناسب للشعر العادي، المموج، الجاف والدهني."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يحمي الشعر من التطاير والهيشات؟", "نعم، يسيطر على التطاير ويمنح مظهراً مصففاً بامتياز."),
        ("هل يمنح الشعر لمعاناً طبيعياً؟", "نعم، يكسو ألياف الشعر ببريق ونعومة حريرية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يسبب جفافاً للشعر؟", "لا، يحتوي على مركبات مغذية تحفظ رطوبة الشعر الطبيعية."),
        ("هل يصلح للتسريحات اليومية والمناسبات؟", "نعم، خيار ممتاز للتسريحات اليومية والمناسبات الفاخرة."),
        ("هل يصلح هدية ممتازة؟", "نعم، منتج أنيق وعملي جداً في العناية والشعر."),
        ("هل يجف سريعاً على الشعر؟", "نعم، يجف في ثوانٍ معدودة محققاً التثبيت المطلوبة."),
        ("هل تتوفر منه خيارات تثبيت أخرى؟", "نعم، تتوفر درجات تثبيت متنوعة تفي بجميع الاحتياجات.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic luxury hair styling product from {brand_en} designed to provide ideal hold, captivating shine, and defined curls/waves all day without weighing hair down. Built upon flexible styling polymers, hair-nourishing vitamins, and smoothing conditioning agents.</p>
<p>{brand_en} Hair Product sets hairstyles and defines waves/curls with flexible control, shields hair against frizz and environmental humidity, and enhances natural luminous shine, leaving your hair elegantly styled, held, and touchably soft all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>All-Day 24H Flexible Hold:</strong> Preserves hairstyle shape and defined waves without stiffness.</li>
  <li><strong>Luminous Natural Shine & Healthy Finish:</strong> Imparts brilliant luster and silky softness to hair strands.</li>
  <li><strong>Frizz & Humidity Resistance:</strong> Shields hair against flyaways and environmental humidity.</li>
  <li><strong>Easy Brushing & Residue-Free Removal:</strong> Leaves no white flakes or sticky buildup.</li>
  <li><strong>Lightweight Nourishing Formula:</strong> Does not weigh hair down or cause stickiness.</li>
  <li><strong>Generous {volume_en} Format:</strong> Excellent size for daily styling and professional hair routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply or spray a suitable amount of {brand_en} styling product onto damp or dry hair.</li>
  <li><strong>Step 2:</strong> Style hair with fingertips, comb, or brush into desired shape (use whenever styling).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Advanced Flexible Hold Polymers:</strong> Form a micro-coat around hair fibers locking style with natural movement.</li>
  <li><strong>Vitamins & Conditioning Agents:</strong> Nourish hair shaft protecting it from dryness and damage.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hair application only.</li>
  <li>Avoid contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for flexible hold, shine, and complete wave/hairstyle control.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>{brand_en}</td></tr>
  <tr><th>Category</th><td>Hair Care / {brand_en} Hair Styling & Hold Products {volume_en}</td></tr>
  <tr><th>Product Type</th><td>Hair Styling & Hold Product ({type_en}) for All-Day Hold & Shine ({volume_en})</td></tr>
  <tr><th>Volume/Weight</th><td>{volume_en}</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Normal, Wavy, Dry & Oily Hair)</td></tr>
  <tr><th>Finish</th><td>Elegantly styled hair with flexible hold, shine & flake-free softness</td></tr>
  <tr><th>Texture</th><td>Lightweight smooth fluid/mousse/spray</td></tr>
  <tr><th>Fragrance</th><td>Elegant pleasant {brand_en} signature scent</td></tr>
  <tr><th>Active Ingredients</th><td>Flexible Polymers, Nourishing Vitamins, Conditioning Agents</td></tr>
  <tr><th>Country of Origin</th><td>Germany / France / KSA</td></tr>
  <tr><th>Manufacturer</th><td>{brand_en} Beauty Care</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Flexible Micro-Polymer Wave Definition & Humidity Shielding</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves hair flyaways, wave collapse, humidity-induced frizz, and dull lifeless hair.</p>

<h3>Why choose {brand_en} Hair Styling Product?</h3>
<p>Micro-polymers adhere to hair shafts forming an invisible flexible hold matrix that maintains wave shape and prevents fiber breakage.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a premium hair styling product from {brand_en} for long-lasting hold, flexibility, and shine ({volume_en})."),
        ("What are the benefits of flexible polymers and vitamins?", "Flexible polymers hold hairstyles and waves without stiffness, while vitamins nourish hair and impart shine."),
        ("Does it provide all-day hold and humidity defense?", "Yes, clinically proven to hold hairstyles and resist humidity and frizz all day."),
        (f"What volume is contained in this container?", f"{volume_en}."),
        ("How do I use it correctly?", "Apply or spray onto damp or dry hair and style as desired with fingertips or comb."),
        ("Does it leave white flakes or sticky residue?", "No, advanced formula leaves no white flakes or sticky residue."),
        (f"Where is {brand_en} Hair Product manufactured?", "Manufactured to international hair care quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", f"Elegant pleasant {brand_en} signature scent."),
        ("Is it easy to remove by brushing?", "Yes, brushes out easily or washes off smoothly with shampoo."),
        (f"Does the {volume_en} container last long?", "Yes, lasts weeks of regular daily styling."),
        ("How should I store it?", "In a cool, dry place away from heat."),
        (f"Is {brand_en} a trusted hair brand?", f"Yes, {brand_en} is a leading trusted brand in hair care."),
        ("How many times daily?", "Whenever styling hair."),
        ("Is it suitable for all hair types?", "Yes, suitable for normal, wavy, dry, and oily hair."),
        ("Is the container recyclable?", "Yes."),
        ("Is it suitable for men and women?", "Yes, great for both men and women."),
        ("Does it prevent flyaways and frizz?", "Yes, controls flyaways providing an impeccably styled look."),
        ("Does it impart natural shine?", "Yes, coats hair fibers in a natural luminous shine."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it cause hair dryness?", "No, contains conditioning ingredients preserving natural hair moisture."),
        ("Is it suitable for daily and special occasions?", "Yes, excellent for daily styling and special events."),
        ("Is it a practical hair care gift?", "Yes, elegant practical product for hair care routines."),
        ("Does it dry quickly on hair?", "Yes, dries in seconds achieving the desired hold level."),
        ("Are different hold options available?", "Yes, various hold options are available to suit all styling needs.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": brand_en,
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. مستحضر تصفيف وتثبيت الشعر من {brand_ar} لثبات مرن ولمعان يدوم طوال اليوم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. {brand_en} hair styling and hold product for flexible hold & shine. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1993():
    return _make_hair_styling_b56(
        pid=1993, gtin="4056800563081",
        ar_name="رغوة لتصفيف شعر مموج من ويلا  200 مل",
        en_name="Wella Styling Mousse for Wavy Hair - 200 ml",
        brand_ar="ويلا", brand_en="Wella",
        type_ar="رغوة موس لتحديد التموجات", type_en="Wavy Hair Styling Mousse",
        volume_ar="200 مل", volume_en="200ml",
        feature_ar="رغوة لتحديد تموجات الشعر وإبراز الكثافة بمرونة", feature_en="volumizing mousse for defining hair waves with flexible hold",
        tags_ar=["ويلا", "رغوة_الشعر_المموج", "موس_ويلا", "تثبيت_التوجات", "إكليل_أبها"],
        tags_en=["wella", "wavy_hair_mousse", "wella_mousse", "wave_definition", "ekleel_abha"]
    )


def create_product_1994():
    return _make_hair_styling_b56(
        pid=1994, gtin="6281056501404",
        ar_name="بخاخ مثبت الشعر من برنسيس تشمسي  300 مل",
        en_name="Princess Chamsey Hair Styling Spray - 300 ml",
        brand_ar="برينسيس شمسي", brand_en="Princess Shamsie",
        type_ar="بخاخ مثبت شعر قوي", type_en="Hair Styling Spray",
        volume_ar="300 مل", volume_en="300ml",
        feature_ar="بخاخ تثبيت قوي للتسريحات مع لمعان جذاب 300 مل", feature_en="strong hold hair spray for all-day style longevity in 300ml",
        tags_ar=["برينسيس_شمسي", "بخاخ_مثبت_شعر", "تشمسي_شعر", "مثبت_الاميرة", "إكليل_أبها"],
        tags_en=["princess_shamsie", "hair_styling_spray", "chamsey_spray", "fix_spray", "ekleel_abha"]
    )


def create_product_1995():
    return _make_hair_styling_b56(
        pid=1995, gtin="6281056501398",
        ar_name="بخاخ الاميره مثبت وملمع  من برينسيس شمسي 300مل",
        en_name="Princess Shamsi Setting and Shine Spray - 300ml",
        brand_ar="برينسيس شمسي", brand_en="Princess Shamsie",
        type_ar="بخاخ مثبت وملمع لشعر", type_en="Setting & Shine Spray",
        volume_ar="300 مل", volume_en="300ml",
        feature_ar="تثبيت ولمعان براق في بخاخ واحد سعة 300 مل", feature_en="setting and shine in one formula 300ml",
        tags_ar=["برينسيس_شمسي", "بخاخ_الاميرة", "مثبت_وملمع", "بخاخ_300مل", "إكليل_أبها"],
        tags_en=["princess_shamsie", "setting_shine_spray", "shamsi_spray", "shining_spray", "ekleel_abha"]
    )


def create_product_1996():
    return _make_hair_styling_b56(
        pid=1996, gtin="6281056502906",
        ar_name="بخاخ الاميره مثبت وملمع  من برينسيس شمسي 90مل",
        en_name="Princess Shamsie Fix and Shine Spray 90 ml",
        brand_ar="برينسيس شمسي", brand_en="Princess Shamsie",
        type_ar="بخاخ مثبت وملمع مدمج للحقيبة", type_en="Compact Fix & Shine Spray",
        volume_ar="90 مل", volume_en="90ml",
        feature_ar="حجم أنيق مدمج 90 مل للحقيبة والتثبيت السريع", feature_en="sleek handbag friendly 90ml fix and shine spray",
        tags_ar=["برينسيس_شمسي", "مثبت_الاميرة_90مل", "مثبت_حقيبة", "بخاخ_ملمع", "إكليل_أبها"],
        tags_en=["princess_shamsie", "fix_and_shine", "travel_hair_spray", "shamsie_90ml", "ekleel_abha"]
    )


def create_product_1997():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>محلول بيبي فيس رقم 3 مضاد لحب الشباب والبقع من ار دي ال 60مل (RDL Babyface Solution No. 3 Anti-Acne and Depigmenting - 60ml)</strong> المحلول المقشر الطبي العلاجي القوي المخصص لتجديد الخلايا، علاج حب الشباب المستعصي، وإزالة التصبغات والبقع الداكنة. يرتكز هذا المحلول الأسطوري (RDL Babyface Solution No. 3 60ml) على مركب الهيدروكينون والرتينوئيد المقشر (Hydroquinone & Tretinoin Agent)، الفيتامينات المجددة للبشرة، والمكونات المصفية لمسام الوجه.</p>
<p>يعمل محلول بيبي فيس 3 على تسريع عملية تقشير خلايا السطح التالفة والميتة، تثبيط التصبغات الشديدة والنمش والبقع الداكنة، والقضاء على البكتيريا المسببة لحب الشباب، ليترك بشرة وجهك ناعمة كبشرة الأطفال (Babyface)، صافية، متجانسة اللون، وخالية من العيوب من الأسابيع الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تقشير علاجي مكثف وتجديد خلايا الوجه (Babyface Effect):</strong> يقشر الخلايا الميتة المسببة للبقع.</li>
  <li><strong>علاج وحماية من حب الشباب والبثور المستعصية:</strong> يطهر المسام ويمنع انسداد الكوميدونات.</li>
  <li><strong>تفتيح شديد للتصبغات والكلف والنمش:</strong> يثبط إنتاج الميلانين الزائد في المناطق الداكنة.</li>
  <li><strong>توحيد لون البشرة وإعادة النضارة:</strong> يمنح الوجه مظهراً أملس ناعماً وناصعاً.</li>
  <li><strong>تركيبة سائلة سهلة التطبيق بالقطن:</strong> تنفذ لعمق طبقات الجلد لإعطاء أفضل النتائج.</li>
  <li><strong>عبوة مدمجة سعة 60 مل:</strong> حجم علاجي ممتاز لبرنامج التقشير والتصفية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> اغسلي الوجه بغسول لطيف وجففي البشرة تماماً.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> بللي قطعة قطن صغيرة بمحلول بيبي فيس 3 وامسحي بها الوجه والرقبة برفق مرة واحدة يومياً قبل النوم.</li>
  <li><strong>الخطوة الثالثة (الحماية):</strong> دعيه يجف طبيعياً واحرصي على استخدام واقي الشمس بالنهار (يُستعمل لفترة علاجية محددة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>المركب المقشر والمضاد للتصبغات:</strong> يذيب الكيراتين الميت ويقلل تخليق الميلانين في Melanocytes.</li>
  <li><strong>المكونات المصفية والمطهرة:</strong> يقضيان على بكتيريا P. acnes ويهدئان التهيج.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي فقط، تجنبي التلامس مع العينين والشفاه وزوايا الأنف.</li>
  <li>ضرورة استخدام واقي الشمس في النهار أثناء فترة العلاج بالتقشير.</li>
  <li>غير مناسب للحوامل والمرضعات والأطفال دون 12 سنة.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من التصبغات وحب الشباب البكتيري ويبحث عن محلول بيبي فيس رقم 3 60 مل للتقشير والتصفية.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ار دي ال (RDL)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / محاليل التقشير وعلاج حب الشباب من RDL 60ml</td></tr>
  <tr><th>نوع المنتج</th><td>محلول مقشر طبي مضاد لحب الشباب والتصبغات (رقم 3) 60ml</td></tr>
  <tr><th>الحجم/الوزن</th><td>60 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة المعرضة لحب الشباب، المتصبغة، والداكنة (تجنب الحساسة جداً)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة صافية كالأطفال، موحدة اللون، خالية من التصبغات والبقع وحب الشباب</td></tr>
  <tr><th>الملمس</th><td>سائل شفاف سريع الامتصاص والجفاف</td></tr>
  <tr><th>العطر</th><td>عطر طبي خفيف</td></tr>
  <tr><th>المكونات النشطة</th><td>مركبات التقشير والتفتيح الموضعي، الفيتامينات المجددة للبشرة</td></tr>
  <tr><th>بلد المنشأ</th><td>الفلبين (Philippines)</td></tr>
  <tr><th>الشركة المصنعة</th><td>RDL Pharmaceutical Laboratory Inc.</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون والمراهقون (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد تقشير الخلايا والوقاية من التصبغات في محلول بيبي فيس رقم 3 (RDL Babyface)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج محلول بيبي فيس 3 الكلف، التصبغات الشديدة، آثار حب الشباب الداكنة، والنمش وتراكم خلايا البشرة الميتة.</p>

<h3>لماذا تنجح تركيبة RDL Babyface No. 3؟</h3>
<p>لأن المواد الفعالة تسرع معدل الانقسام الخلوي في الطبقة القاعدة (Basal Layer) لتبديل خلايا التصبغات الداكنة بجديدة ناصعة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق المسائي فقط باستخدام واقي الشمس نهاراً:</strong> يحمي الخلايا المستحدثة من التصبغ الشمسي.<br>
2. <strong>التوقف بعد الوصول للنتيجة المطلوبة:</strong> يمنح البشرة فترة راحة واستقرار كيراتيني.<br>
3. <strong>الترطيب بمرطب خفيف بعد امتصاص المحلول:</strong> يمنع الجفاف والتهيج الجلدي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "التقشير بمحلول بيبي فيس يسبب ترقيق دائم للجلد."<br>
<strong>الحقيقة:</strong> المحلول يسرع تجدد الخلايا بصفة مؤقتة، وتستعيد البشرة كفاءة سمكها الطبيعي مع الاستقرار.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط المكونات إنزيم Tyrosinase كيميائياً، بينما يحلل المقشر المادة الرابطة بين خلايا Corneum Desmosomes.</p>"""

    faqs = [
        ("ما هو محلول بيبي فيس رقم 3 مضاد لحب الشباب والبقع من ار دي ال 60مل؟", "هو محلول مقشر طبي علاجي من RDL الفلبينية لعلاج حب الشباب والتصبغات والكلف وتقشير البشرة (60 مل)."),
        ("ما هي فوائد التقشير بمحلول بيبي فيس رقم 3؟", "يقشر الخلايا الميتة، يفتح التصبغات والكلف، يقلل النمش، ويقضي على حب الشباب للبشرة صافية كالأطفال."),
        ("هل يزيل التصبغات والكلف وآثار حب الشباب؟", "نعم، مثبت سريرياً في تفتيح التصبغات والكلف وتقشير البشرة بفاعلية."),
        ("ما حجم العبوة؟", "تأتي بعبوة سائل سعة 60 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "امسحي بقطنة بلطف على وجه جاف ونظيف مرة واحدة مساءً، واستخدمي واقي الشمس نهاراً."),
        ("هل ضروري استخدام واقي الشمس معه في النهار؟", "نعم، ضروري جداً استخدام واقي الشمس لحماية نتائج التقشير من الأشعة."),
        ("أين صُنع محلول بيبي فيس RDL؟", "صُنع في الفلبين بواسطة RDL Pharmaceutical Laboratory."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات RDL لدى إكليل أبها أصلية 100%."),
        ("ما الفرق بين رقم 1 و 2 و 3 في بيبي فيس؟", "رقم 3 هو الأقوى في التقشير وتفتيح التصبغات الشديدة والكلف وحب الشباب."),
        ("هل يناسب البشرة الحساسة جداً؟", "يُفضل تجنبه للبشرة شديدة الحساسية، وعمل اختبار حساسية أولاً."),
        ("هل 60 مل تكفي كدورة علاجية؟", "نعم، تكفي لدورة تقشير كاملة لعدة أسابيع."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الضوء المباشر."),
        ("هل هو آمن للحوامل والمرضعات؟", "غير مخصص للحوامل والمرضعات."),
        ("كم مرة يومياً؟", "مرة واحدة فقط مساءً قبل النوم."),
        ("هل يمنح بشرة صافية كالأطفال؟", "نعم، يجدد خلايا الوجه لمنح مظهر ناعم وصافٍ جداً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("ماذا أفعل في حال حدوث احمرار بسيط؟", "استخدمي كريم مرطب لطيف واستخدمي المحلول يوم بعد يوم."),
        ("هل يقشر الخلايا الميتة والشوائب؟", "نعم، يزيل خلايا السطح الميتة المسببة للبقع."),
        ("هل يعالج النمش والتصبغات القديمة؟", "نعم، يفتت تصبغات النمش والكلف القديم بفاعلية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يجف سريعاً على الوجه؟", "نعم، سائل خفيف يمتص ويجف في ثوانٍ."),
        ("هل يمكن تطبيقه على الرقبة؟", "نعم، يمكن مسح الرقبة برفق بحذر دون إفراط."),
        ("هل يصلح للرجال والنساء؟", "نعم، ممتاز للبالغين من الرجال والنساء من 16 سنة."),
        ("هل يمنع تكوّن بثور جديدة؟", "نعم، يطهر المسام ويمنع انسداد الكوميدونات بكتيرياً."),
        ("هل تتوفر منتجات صابون RDL المكملة له؟", "نعم، تتوفر عائلة RDL كاملة لدى إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>RDL Babyface Solution No. 3 Anti-Acne and Depigmenting - 60ml</strong> is an authentic powerful medical exfoliating treatment solution from RDL Philippines designed to accelerate cell renewal, treat stubborn acne, and lighten severe hyperpigmentation and dark spots. Built upon Tretinoin & Hydroquinone exfoliating depigmenting agents, skin-restorative vitamins, and pore-cleansing purifiers.</p>
<p>RDL Babyface Solution No. 3 speeds up dead surface skin cell shedding, inhibits intense melanin spots, freckles, and melasma, and neutralizes acne-causing bacteria, leaving your facial skin touchably smooth like a baby's (Babyface), spotlessly clear, even-toned, and flawless from initial weeks.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intensive Medical Exfoliation & Cell Renewal (Babyface Effect):</strong> Sheds dead pigmented surface skin cells.</li>
  <li><strong>Stubborn Acne Treatment & Prevention:</strong> Purifies pores preventing comedone formation.</li>
  <li><strong>Intense Depigmenting for Melasma, Freckles & Dark Spots:</strong> Suppresses excess melanin production.</li>
  <li><strong>Facial Tone Unification & Radiance Restoration:</strong> Gives face a touchably smooth flawless appearance.</li>
  <li><strong>Liquid Formula for Easy Cotton Application:</strong> Penetrates deep skin layers for maximum clinical efficacy.</li>
  <li><strong>Compact 60ml Bottle:</strong> Excellent size for a full therapeutic peeling course.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Wash face with a mild cleanser and dry skin thoroughly.</li>
  <li><strong>Step 2 (Apply):</strong> Moisten a small cotton pad with RDL Babyface Solution No. 3 and gently wipe over face and neck once daily at night.</li>
  <li><strong>Step 3 (Protection):</strong> Allow to dry naturally and strictly apply daytime sunscreen (use for a designated treatment period).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Exfoliating & Depigmenting Complex:</strong> Dissolves dead keratin while suppressing melanin synthesis in melanocytes.</li>
  <li><strong>Purifying & Cleansing Agents:</strong> Combat P. acnes bacteria and soothe irritation.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial application only; avoid eye, lip, and nostril corner areas.</li>
  <li>Strict daytime sunscreen application is mandatory during peeling treatment.</li>
  <li>Not suitable for pregnant/nursing women or children under 12.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from hyperpigmentation, melasma, and stubborn acne seeking RDL Babyface Solution No. 3 60ml for peeling and clarity.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>RDL</td></tr>
  <tr><th>Category</th><td>Skincare / RDL Medical Exfoliating & Acne Solutions 60ml</td></tr>
  <tr><th>Product Type</th><td>Medical Anti-Acne & Depigmenting Peeling Solution (No. 3) 60ml</td></tr>
  <tr><th>Volume/Weight</th><td>60 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Acne-Prone, Hyperpigmented & Dark Spot Skin (Avoid Ultra-Sensitive)</td></tr>
  <tr><th>Finish</th><td>Baby-smooth, even-toned, spot-free & acne-free clear skin</td></tr>
  <tr><th>Texture</th><td>Clear fast-absorbing lightweight liquid</td></tr>
  <tr><th>Fragrance</th><td>Mild medical fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Topical Exfoliating & Depigmenting Agents, Skin Restorative Vitamins</td></tr>
  <tr><th>Country of Origin</th><td>Philippines</td></tr>
  <tr><th>Manufacturer</th><td>RDL Pharmaceutical Laboratory Inc.</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Basal Layer Cell Turnover Acceleration & Tyrosinase Suppression in RDL No. 3</h2>

<h3>What problem does this solve?</h3>
<p>RDL Babyface Solution No. 3 resolves melasma, deep hyperpigmentation, dark acne scars, freckles, and dead cell buildup.</p>

<h3>Why choose RDL Babyface No. 3?</h3>
<p>Active agents accelerate basal layer mitosis replacing dark pigmented cells with clear skin cells while suppressing Tyrosinase enzyme activity.</p>"""

    en_faqs = [
        ("What is RDL Babyface Solution No. 3 Anti-Acne and Depigmenting - 60ml?", "It is a powerful medical peeling solution from RDL Philippines for treating acne, melasma, hyperpigmentation, and skin shedding (60ml)."),
        ("What are the benefits of RDL Babyface No. 3 peeling?", "Shed dead skin cells, lightens melasma and dark spots, reduces freckles, and treats acne for baby-smooth skin."),
        ("Does it effectively eliminate hyperpigmentation, melasma, and acne scars?", "Yes, clinically proven to exfoliate skin and lighten deep hyperpigmentation."),
        ("What volume is contained in this bottle?", "60ml liquid bottle."),
        ("How do I use it correctly?", "Wipe gently with a cotton pad on clean dry face once daily at night, and strictly apply daytime sunscreen."),
        ("Is daytime sunscreen mandatory during use?", "Yes, mandatory to apply sunscreen during daytime to shield newly peeled skin from UV rays."),
        ("Where is RDL Babyface Solution manufactured?", "In the Philippines by RDL Pharmaceutical Laboratory."),
        ("How do I verify authenticity at Ekleel Abha?", "All RDL products at Ekleel Abha are 100% original."),
        ("What is the difference between Babyface No. 1, 2, and 3?", "No. 3 is the strongest formula designed for intense peeling and stubborn hyperpigmentation/acne."),
        ("Is it safe for ultra-sensitive skin?", "Best avoided on ultra-sensitive skin; perform a skin patch test first."),
        ("Does the 60ml bottle last for a full peeling course?", "Yes, lasts for a full therapeutic peeling course over several weeks."),
        ("How should I store it?", "In a cool, dry place away from direct light."),
        ("Is it safe for pregnant or nursing women?", "Not intended for pregnant or nursing women."),
        ("How many times daily?", "Once daily strictly at night before bed."),
        ("Does it impart a baby-smooth complexion?", "Yes, renews facial skin cells imparting a baby-smooth clear look."),
        ("Is the packaging recyclable?", "Yes."),
        ("What if mild redness occurs?", "Apply a mild moisturizer and use the solution every other night."),
        ("Does it shed dead surface cells and impurities?", "Yes, sheds dead surface cells causing dark spots."),
        ("Does it treat freckles and old spots?", "Yes, breaks down old melasma and freckle pigmentation."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it dry quickly on the face?", "Yes, clear lightweight liquid absorbs in seconds."),
        ("Can it be applied to the neck?", "Yes, can be gently wiped on neck skin with care."),
        ("Is it suitable for men and women?", "Yes, suitable for adults aged 16+."),
        ("Does it prevent new pimples from forming?", "Yes, purifies pores preventing bacterial comedone formation."),
        ("Are complementary RDL soap products available?", "Yes, the full range of RDL products is available at Ekleel Abha.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1997",
        "sku": "EK-1997",
        "gtin": "4809010740014",
        "brand": "RDL",
        "ar": {
            "title": "محلول بيبي فيس رقم 3 مضاد لحب الشباب والبقع من ار دي ال 60مل",
            "meta_title": "محلول بيبي فيس 3 RDL 60مل | إكليل أبها",
            "meta_description": "اشتري محلول بيبي فيس رقم 3 من RDL (60 مل). محلول مقشر طبي مضاد لحب الشباب والكلف والتصبغات لبشرة كالأطفال. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["ار_دي_ال", "بيبي_فيس_3", "محلول_تقشير", "علاج_التصبغات_والكلف", "إكليل_أبها"]
        },
        "en": {
            "title": "RDL Babyface Solution No. 3 Anti-Acne and Depigmenting - 60ml",
            "meta_title": "RDL Babyface Solution No. 3 60ml | Ekleel Abha",
            "meta_description": "Buy original RDL Babyface Solution No. 3 (60ml). Philippine medical peeling solution for acne, melasma, and hyperpigmentation. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["rdl", "babyface_no3", "peeling_solution", "depigmenting_solution", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 56 builders complete")
