import json, os

def create_product_1988():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مقشر ناعم بالسكر من لوريال باريس - 50 مل (L'Oréal Paris Smooth Sugars Scrub - 50ml)</strong> المقشر الطبيعي الفاخر الأيقوني من لوريال باريس الفرنسية المصمم خصيصاً لتنعيم وتقشير وتنظيف بشرة الوجه والشفتين بلمسة ناعمة كالحرير. يرتكز هذا المقشر الأسطوري (L'Oréal Smooth Sugars Scrub 50ml) على حبيبات السكر الطبيعي الثلاثية (3 Fine Sugars: Brown, Blond, White) المدعمة بزيوت كاكاو وجوز الهند المغذية.</p>
<p>يعمل مقشر لوريال بالسكر على إذابة وتذويب الخلايا الميتة من سطح الوجه والشفتين، تنظيف المسام وتمليس الخشونة دون أي خدش أو تهيج، ومسح علامات الإجهاد، ليترك بشرتك ناعمة للغاية، ناضرة، مرطبة، ومكتسبة لملمس مخملي ناعم من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تقشير ناعم ومزدوج للوجه والشفتين بالسكر الطبيعي:</strong> يزيل خلايا الجلد الميتة برفق.</li>
  <li><strong>خليط السكر الطبيعي الثلاثي (الأسمر، الأشقر، والأبيض):</strong> يذوب بسلاسة عند التدليك بالماء.</li>
  <li><strong>تغذية وترطيب مكثف بزبدة الكاكاو وجوز الهند:</strong> يمنع الجفاف ويترك البشرة مرطبة.</li>
  <li><strong>مناسب لتنعيم وتقشير الشفتين الجافتين:</strong> يزيل القشور ويمنح الشفتين ناعمتين ممتلئتين.</li>
  <li><strong>تركيبة خالية من الميكروبلاستيك والمواد القاسية:</strong> 100% مكونات مقشرة طبيعية وآمنة.</li>
  <li><strong>عبوة زجاجية أنيقة سعة 50 مل:</strong> حجم ممتاز للاستخدام الأسبوعي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق):</strong> ضعي كمية صغيرة من مقشر السكر بأصابع جافة على بشرة الوجه والشفتين النظيفة والجافة.</li>
  <li><strong>الخطوة الثانية (التدليك):</strong> أضيفي القليل من الماء الدافئ ودلكي برفق بحركات دائرية حتى تذوب حبيبات السكر.</li>
  <li><strong>الخطوة الثالثة (الشطف):</strong> اشطفي بالماء الدافئ وجففي البشرة (يُستعمل 3 مرات أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>3 أنواع سكر طبيعي ناعم (أسمر، أشقر، أبيض):</strong> تذوب بالماء وتزيل القشور والخلايا الميتة.</li>
  <li><strong>زبدة الكاكاو وزيت جوز الهند:</strong> يغذيان حاجز البشرة ويحفظان المرونة والنعومة الحريرية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والشفتين فقط.</li>
  <li>تجنبي التلامس المباشر مع داخل العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف مع إغلاق العبوة فوراً لمنع دخول الماء.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن مقشر السكر الناعم من لوريال 50 مل لتنعيم وتقشير الوجه والشفتين.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لوريال باريس (L'Oréal Paris)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / مقشرات لوريال بالسكر الطبيعي للوجه والشفتين 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>مقشر ناعم بالسكر الطبيعي الثلاثي وزبدة الكاكاو للوجه والشفتين (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه والشفتين (بما في ذلك الجافة والحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه وشفتان ناعمان كالحرير، ناضران، خاليان من القشور ومفعمان بالمرونة</td></tr>
  <tr><th>الملمس</th><td>قوام سكري ناعم يذوب بالماء إلى لوشن مغذٍ</td></tr>
  <tr><th>العطر</th><td>عطر الكاكاو والسكر اللذيذ الدافئ</td></tr>
  <tr><th>المكونات النشطة</th><td>3 أنواع سكر طبيعي (أسمر، أشقر، أبيض)، زبدة الكاكاو، زيت جوز الهند</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>L'Oréal Paris France</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 14 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد السكر الطبيعي الثلاثي وزبدة الكاكاو في مقشر لوريال (Smooth Sugars)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مقشر السكر من لوريال خشونة الوجه، القشور الجافة على الشفتين، تراكم الخلايا الميتة، والبشرة الباهتة.</p>

<h3>لماذا تنجح تركيبة السكر الثلاثية؟</h3>
<p>لأن حبيبات السكر الميكروية تذوب بالماء تباعدياً أثناء التدليك، مما يضمن تقشيراً كاشطاً ناعماً يتكيف مع حساسية الجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام 3 مرات أسبوعياً:</strong> يجدد سطح البشرة والشفتين باستمرار.<br>
2. <strong>التطبيق بأيدٍ جافة:</strong> يمنع ذوبان حبيبات السكر داخل العبوة قبل التطبيق.<br>
3. <strong>التطبيق قبل روج الشفاه:</strong> يضمن ثبات الروج ونعومة الشفتين دون تشققات.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مقشرات السكر تجرح بشرة الوجه والشفتين."<br>
<strong>الحقيقة:</strong> لوريال Smooth Sugars مصمم بحبيبات سكر ناعمة جداً تذوب بالماء دون أي حواف حادة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يذيب السكروز (Sucrose) الروابط الكيراتينية الميتة سطحيًا بينما يخترق حمض الجليكوليك الطبيعي المسام لتنعيم الملمس.</p>"""

    faqs = [
        ("ما هو مقشر ناعم بالسكر من لوريال باريس - 50 مل؟", "هو مقشر طبيعي فاخر للوجه والشفتين من لوريال باريس بحبيبات السكر الثلاثية وزبدة الكاكاو (50 مل)."),
        ("ما هي فوائد السكر الثلاثي وزبدة الكاكاو؟", "يزيل السكر الخلايا الميتة والقشور، بينما تغذي زبدة الكاكاو وزيت جوز الهند البشرة والشفتين."),
        ("هل ينعم وتقشر الشفتين والوجه بفاعلية؟", "نعم، مثبت سريرياً في تنعيم وتقشير الوجه والشفتين ومنحهما ملمساً مخملياً."),
        ("ما حجم العبوة؟", "تأتي بعبوة زجاجية بسعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي بأصابع جافة، أضيفي ماء دافئ ودلكي حتى يذوب السكر ثم اشطفي 3 مرات أسبوعياً."),
        ("هل يذوب السكر بالماء أثناء التدليك؟", "نعم، تذوب الحبيبات بالماء الدافئ متحولة إلى لوشن ناعم."),
        ("أين صُنع مقشر لوريال بالسكر؟", "صُنع في فرنسا بواسطة L'Oréal Paris France."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لوريال لدى إكليل أبها أصلية 100%."),
        ("ما رائحة مقشر لوريال بالسكر؟", "عطر الكاكاو والسكر الدافئ اللذيذ."),
        ("هل يصلح كقاعدة قبل وضع الروج؟", "نعم، ممتاز جداً لتقشير الشفتين قبل الروج لضمان ثباته ونعومته."),
        ("هل 50 مل تكفي لفترة جيدة؟", "نعم، تكفي لعدة أسابيع من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف واحرصي على عدم دخول الماء إلى العبوة."),
        ("هل يناسب البشرة الجافة والحساسة؟", "نعم، آمن ومناسب لجميع أنواع البشرة والشفتين."),
        ("كم مرة أسبوعياً؟", "3 مرات أسبوعياً."),
        ("هل لوريال باريس العلامة الأولى عالمياً في التجميل؟", "نعم، L'Oréal Paris العلامة الفرنسية الأيقونية الأولى عالمياً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب للرجال والنساء من 14 سنة."),
        ("هل يزيل علامات الإجهاد والبشرة الباهتة؟", "نعم، يجدد الدورة الدموية ويعيد النضارة والحيوية للوجه."),
        ("هل ينشطف بالماء الدافئ بسهولة؟", "نعم، ينشطف بالماء الدافئ بسلاسة دون أثر دهني لزج."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل هو خالي من الميكروبلاستيك؟", "نعم، 100% مكونات مقشرة طبيعية من السكر."),
        ("هل يمنح الشفتين مظهر ممتلئاً وناضراً؟", "نعم، ينعم الشفتين ويكسبهما نضارة ولوناً وردياً طبيعياً."),
        ("هل يصلح هدية راقية؟", "نعم، عبوة زجاجية أنيقة خيار ممتاز للهدايا."),
        ("هل يغني عن المقشرات الكيميائية القاسية؟", "نعم، مقشر ميكانيكي ناعم ولطيف جداً."),
        ("هل تتوفر منه أنواع أخرى بالسكر لدى لوريال؟", "نعم، تتوفر تشكيلة أقنعة السكر كاملة لدى لوريال.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>L'Oréal Paris Smooth Sugars Scrub - 50ml</strong> is the iconic luxury natural facial and lip scrub from L'Oréal Paris France formulated to polish, refine, and smooth face and lip skin with touchable softness. Built upon 3 Fine Sugars (Brown, Blond, White) enriched with nourishing Cocoa Butter and Coconut Oil.</p>
<p>L'Oréal Smooth Sugars Scrub dissolves dead skin cells from face and lips, unblocks pores, and smooths skin roughness without scratching or irritation, leaving your skin touchably silky soft, radiant, hydrated, and velvety smooth from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Gentle Dual Exfoliation for Face & Lips with Natural Sugars:</strong> Gently removes dead skin cells and flakes.</li>
  <li><strong>3 Fine Natural Sugar Blend (Brown, Blond, White):</strong> Melts smoothly upon water-assisted massage.</li>
  <li><strong>Intensive Nourishment with Cocoa Butter & Coconut Oil:</strong> Prevents dryness leaving skin hydrated.</li>
  <li><strong>Ideal for Chapped Lip Smoothing:</strong> Removes lip flakes leaving lips plump and smooth.</li>
  <li><strong>Microplastic-Free 100% Natural Exfoliants:</strong> Safe, natural, and gentle on facial skin.</li>
  <li><strong>Luxury 50ml Glass Jar Container:</strong> Excellent volume for continuous weekly routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply):</strong> Apply a small amount of sugar scrub with dry fingers onto clean dry face and lips.</li>
  <li><strong>Step 2 (Massage):</strong> Add warm water and massage gently in circular motions until sugar crystals melt.</li>
  <li><strong>Step 3 (Rinse):</strong> Rinse thoroughly with warm water and pat dry (use 3 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>3 Fine Natural Sugars (Brown, Blond, White):</strong> Melt with water dissolving flakes and dead skin cells.</li>
  <li><strong>Cocoa Butter & Coconut Oil:</strong> Nourish skin barrier locking in softness and moisture.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and lip application only.</li>
  <li>Avoid direct contact inside eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place closing jar tightly to prevent water ingress.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every woman seeking L'Oréal Smooth Sugars Scrub 50ml for gentle facial and lip exfoliation.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>L'Oréal Paris</td></tr>
  <tr><th>Category</th><td>Skincare / L'Oréal Paris Smooth Sugars Face & Lip Scrubs 50ml</td></tr>
  <tr><th>Product Type</th><td>3 Fine Natural Sugars & Cocoa Butter Face & Lip Exfoliating Scrub (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Face & Lip Skin Types (Including Dry & Sensitive)</td></tr>
  <tr><th>Finish</th><td>Silky soft, radiant, flake-free face and lips with touchable elasticity</td></tr>
  <tr><th>Texture</th><td>Smooth melting sugar texture transforming into nourishing lotion</td></tr>
  <tr><th>Fragrance</th><td>Warm delicious cocoa and sugar fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>3 Fine Sugars (Brown, Blond, White), Cocoa Butter, Coconut Oil</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>L'Oréal Paris France</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 14+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Sucrose Water-Soluble Mechanical Exfoliation & Lipidic Barrier Care</h2>

<h3>What problem does this solve?</h3>
<p>L'Oréal Smooth Sugars Scrub resolves facial roughness, dry chapped lips, dead cell buildup, and dull complexion.</p>

<h3>Why choose L'Oréal Smooth Sugars Scrub?</h3>
<p>Fine sucrose micro-particles melt progressively with warm water, guaranteeing a self-limiting gentle mechanical exfoliation adapted to skin sensitivity.</p>"""

    en_faqs = [
        ("What is L'Oréal Paris Smooth Sugars Scrub - 50ml?", "It is a luxury natural face and lip scrub from L'Oréal Paris with 3 fine sugars and Cocoa Butter (50ml)."),
        ("What are the benefits of 3 fine sugars and Cocoa Butter?", "Fine sugars exfoliate dead cells, while Cocoa Butter and Coconut Oil deeply nourish face and lips."),
        ("Does it effectively smooth and exfoliate face and lips?", "Yes, clinically proven to smooth and exfoliate face and lips leaving a velvety feel."),
        ("What volume is contained in this jar?", "50ml luxury glass jar."),
        ("How do I use it correctly?", "Apply with dry fingers, add warm water, massage until sugar melts, rinse 3 times weekly."),
        ("Does the sugar melt with water during massage?", "Yes, sugar crystals melt with warm water into a smooth lotion."),
        ("Where is L'Oréal Paris Smooth Sugars Scrub manufactured?", "In France by L'Oréal Paris France."),
        ("How do I verify authenticity at Ekleel Abha?", "All L'Oréal products at Ekleel Abha are 100% original."),
        ("What scent does L'Oréal Sugars Scrub have?", "Warm delicious cocoa and sugar signature fragrance."),
        ("Is it a good prep before lipstick application?", "Yes, excellent for smoothing lips before applying lipstick for long wear."),
        ("Does the 50ml jar last long?", "Yes, lasts weeks of regular weekly use."),
        ("How should I store it?", "In a cool, dry place ensuring no water enters the jar."),
        ("Is it suitable for dry and sensitive skin?", "Yes, safe and suitable for all face and lip skin types."),
        ("How many times weekly?", "3 times weekly."),
        ("Is L'Oréal Paris a global #1 beauty brand?", "Yes, L'Oréal Paris is the world's premier iconic French beauty brand."),
        ("Is the glass jar recyclable?", "Yes."),
        ("Is it suitable for men and women?", "Yes, suitable for men and women aged 14+."),
        ("Does it remove dullness and signs of fatigue?", "Yes, stimulates circulation restoring radiance and vitality."),
        ("Does it rinse off easily with warm water?", "Yes, rinses off smoothly without greasy residue."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it microplastic-free?", "Yes, 100% natural sugar exfoliating particles."),
        ("Does it give lips a plump smooth look?", "Yes, smooths lips imparting a natural fresh pink appearance."),
        ("Is it a luxury skincare gift?", "Yes, elegant glass jar makes a great skincare gift."),
        ("Does it replace harsh chemical scrubs?", "Yes, a very gentle natural mechanical exfoliant."),
        ("Are other sugar scrub variants available from L'Oréal?", "Yes, the full range of L'Oréal sugar scrubs is available.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1988",
        "sku": "EK-1988",
        "gtin": "3600523542178",
        "brand": "L'Oréal Paris",
        "ar": {
            "title": "مقشر ناعم بالسكر من لوريال باريس - 50 مل",
            "meta_title": "مقشر لوريال بالسكر للوجه والشفتين 50مل | إكليل أبها",
            "meta_description": "اشتري مقشر ناعم بالسكر من لوريال باريس (50 مل). مقشر طبيعي بثلاثة أنواع سكر وزبدة الكاكاو لتنعيم وتقشير الوجه والشفتين. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["لوريال", "مقشر_السكر", "مقشر_لوريال_بالسكر", "تقشير_الشفتين", "إكليل_أبها"]
        },
        "en": {
            "title": "L'Oréal Paris Smooth Sugars Scrub - 50ml",
            "meta_title": "L'Oréal Smooth Sugars Scrub 50ml | Ekleel Abha",
            "meta_description": "Buy original L'Oréal Paris Smooth Sugars Scrub (50ml). French 3 Fine Sugars & Cocoa Butter face and lip exfoliating scrub. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["loreal", "smooth_sugars", "loreal_sugar_scrub", "lip_scrub", "ekleel_abha"]
        }
    }


def _make_hair_styling_product(pid, gtin, ar_name, en_name, brand_ar, brand_en, type_ar, type_en, volume_ar, volume_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> مستحضر تصفيف وتثبيت الشعر الفاخر الأصيل من {brand_ar} المصمم خصيصاً لمنح شعرك ثباتاً مثالياً، لمعاناً ساحراً، وتصفيفة جذابة تدوم طوال اليوم دون إثقال أو لزوجة. يرتكز هذا المنتج الأسطوري ({en_name}) على بوليمرات التثبيت المرنة المتطورة، الفيتامينات المغذية لجيلاتين الشعر، وخلاصات التنعيم.</p>
<p>يعمل مستحضر تصفيف {brand_ar} على تثبيت التسريحات وتشكيل الخصلات بمرونة كاملة، حماية الشعر من التجعّد والرطوبة العالية، وتغذية ألياف الشعر وإكسابها لمعاناً طبيعياً براقاً، ليترك شعرك مصففاً بأناقة، ثابتاً، وناعماً كالحرير طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تثبيت قوي ومرن للتسريحات طوال اليوم:</strong> يحافظ على شكل التسريحة دون تيبس.</li>
  <li><strong>لمعان طبيعي براق ومظهر صحي:</strong> يضفي بريقاً ونعومة ساحرة على ألياف الشعر.</li>
  <li><strong>مقاومة التجعّد والرطوبة العالية:</strong> يحمي الشعر من التطاير والهيشات الجوية.</li>
  <li><strong>سهل التمشيط والإزالة بالفرشاة والشامبو:</strong> لا يترك أي ترسبات أو قشور بيضاء.</li>
  <li><strong>تركيبة مغذية خفيفة الوزن:</strong> لا تثقل الشعر ولا تسبب جفافه.</li>
  <li><strong>عبوة مدمجة سعة {volume_ar}:</strong> حجم ممتاز للاستخدام اليومي والتصفيف الاحترافي.</li>
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
  <li>لكل من يبحث عن {ar_name} للتثبيت المرن واللمعان والسيطرة على التسريحة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>{brand_ar} ({brand_en})</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / مستحضرات تصفيف وتثبيت الشعر من {brand_ar} {volume_ar}</td></tr>
  <tr><th>نوع المنتج</th><td>مستحضر تصفيف وتثبيت الشعر ({type_ar}) لثبات ولمعان يدوم طوال اليوم ({volume_ar})</td></tr>
  <tr><th>الحجم/الوزن</th><td>{volume_ar}</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (العادي، الجاف، والدهني)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر مصفف بثبات أنيق، مرن، براق وخالٍ من القشور واللزوجة</td></tr>
  <tr><th>الملمس</th><td>سائل/كريم/رغوة/بخاخ ناعم خفيف الوزن</td></tr>
  <tr><th>العطر</th><td>عطر {brand_ar} الأنيق الفواح</td></tr>
  <tr><th>المكونات النشطة</th><td>بوليمرات تثبيت مرنة، فيتامينات مغذية، مركبات تنعيم</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا / ألمانيا / المملكة المتحدة</td></tr>
  <tr><th>الشركة المصنعة</th><td>{brand_en} Hair Care Division</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد البوليمرات المرنة والمركبات المنعمة في مستحضر {brand_ar}</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مستحضر تصفيف {brand_ar} مشكلة تطاير الشعر، فقدان شكل التسريحة، التجعّد بفعل الرطوبة، والشعر الباهت.</p>

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
        (f"ما هو {ar_name}؟", f"هو مستحضر تصفيف وتثبيت الشعر الفاخر من {brand_ar} لمنح الشعر ثباتاً ومرونة ولمعاناً ({volume_ar})."),
        (f"ما هي فوائد البوليمرات المرنة والفيتامينات؟", f"تثبت البوليمرات التسريحة بحرية دون تيبس، بينما تغذي الفيتامينات الشعر وتمنحه لمعاناً براقاً."),
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
        (f"هل {brand_ar} علامة عالمية شهيرة في تصفيف الشعر؟", f"نعم، {brand_en} علامة رائدة وموثوقة جداً عالمياً في العناية بالشعر وتصفيفه."),
        ("كم مرة يومياً؟", "عند تصفيف الشعر."),
        ("هل يناسب جميع أنواع الشعر؟", "نعم، مناسب للشعر العادي، الجاف، الدهني والمجعد."),
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
<p>The <strong>{en_name}</strong> is an authentic luxury hair styling and hold product from {brand_en} designed to provide ideal hold, captivating shine, and long-lasting control without weighing hair down or leaving stickiness. Built upon flexible styling polymers, hair-nourishing vitamins, and smoothing conditioning agents.</p>
<p>{brand_en} Hair Styling Product sets hairstyles and shapes strands with flexible control, shields hair against frizz and high humidity, and nourishes hair fibers with a natural luminous shine, leaving your hair elegantly styled, held, and touchably soft all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>All-Day Strong Flexible Hold:</strong> Preserves hairstyle shape without stiffness.</li>
  <li><strong>Luminous Natural Shine & Healthy Finish:</strong> Imparts brilliant luster and softness to hair strands.</li>
  <li><strong>Frizz & Humidity Resistance:</strong> Shields hair against flyaways and environmental humidity.</li>
  <li><strong>Easy Brushing & Residue-Free Removal:</strong> Leaves no white flakes or sticky buildup.</li>
  <li><strong>Lightweight Nourishing Formula:</strong> Does not weigh hair down or cause dryness.</li>
  <li><strong>Generous {volume_en} Format:</strong> Excellent size for daily styling and professional hair routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply/spray a suitable amount of {brand_en} styling product onto damp or dry hair.</li>
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
  <li>Anyone seeking {en_name} for flexible hold, shine, and complete hairstyle control.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>{brand_en}</td></tr>
  <tr><th>Category</th><td>Hair Care / {brand_en} Hair Styling & Hold Products {volume_en}</td></tr>
  <tr><th>Product Type</th><td>Hair Styling & Hold Product ({type_en}) for All-Day Hold & Shine ({volume_en})</td></tr>
  <tr><th>Volume/Weight</th><td>{volume_en}</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Normal, Dry & Oily Hair)</td></tr>
  <tr><th>Finish</th><td>Elegantly styled hair with flexible hold, shine & flake-free softness</td></tr>
  <tr><th>Texture</th><td>Lightweight smooth fluid/cream/mousse/spray</td></tr>
  <tr><th>Fragrance</th><td>Elegant pleasant {brand_en} signature scent</td></tr>
  <tr><th>Active Ingredients</th><td>Flexible Polymers, Nourishing Vitamins, Conditioning Agents</td></tr>
  <tr><th>Country of Origin</th><td>France / Germany / UK</td></tr>
  <tr><th>Manufacturer</th><td>{brand_en} Hair Care Division</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Flexible Micro-Polymer Film Formation & Humidity Shielding</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves hair flyaways, hairstyle collapse, humidity-induced frizz, and dull lifeless hair.</p>

<h3>Why choose {brand_en} Hair Styling Product?</h3>
<p>Micro-polymers adhere to hair shafts forming an invisible flexible hold matrix that maintains shape and prevents fiber breakage.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a premium hair styling and hold product from {brand_en} for long-lasting hold, flexibility, and shine ({volume_en})."),
        ("What are the benefits of flexible polymers and vitamins?", "Flexible polymers hold hairstyles without stiffness, while vitamins nourish hair and impart a brilliant shine."),
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
        (f"Is {brand_en} a world-famous hair brand?", f"Yes, {brand_en} is a globally leading trusted brand in hair care."),
        ("How many times daily?", "Whenever styling hair."),
        ("Is it suitable for all hair types?", "Yes, suitable for normal, dry, oily, and curly hair."),
        ("Is the container recyclable?", "Yes."),
        ("Is it suitable for men and women?", "Yes, great for both men and women."),
        ("Does it prevent flyaways and frizz?", "Yes, controls flyaways providing an impeccably styled look."),
        ("Does it impart natural shine?", "Yes, coats hair fibers in a natural luminous shine."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it cause hair dryness?", "No, contains conditioning ingredients preserving natural hair moisture."),
        ("Is it suitable for daily and special occasions?", "Yes, excellent for daily styling and special events."),
        ("Is it a practical hair care gift?", "Yes, elegant practical product for hair care routines."),
        ("Does it dry quickly on hair?", "Yes, dries in seconds achieving the desired hold level."),
        ("Are different hold levels available?", "Yes, various hold levels are available to suit all styling needs.")
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


def create_product_1989():
    return _make_hair_styling_product(
        pid=1989, gtin="3600522506898",
        ar_name="كريم مثبت شعر ايلينت من لوريال باريس 200مل",
        en_name="L'Oréal Paris Elnett Hair Styling Cream 200ml",
        brand_ar="لوريال باريس إيلينت", brand_en="L'Oréal Paris Elnett",
        type_ar="كريم تصفيف وتثبيت مغذٍ", type_en="Nourishing Styling Cream",
        volume_ar="200 مل", volume_en="200ml",
        feature_ar="تثبيت إيلينت الأسطوري مع تغذية كريمية حريرية", feature_en="legendary Elnett hold with silky cream nourishment",
        tags_ar=["لوريال", "إيلينت", "كريم_مثبت_شعر", "لوريال_إيلينت", "إكليل_أبها"],
        tags_en=["loreal", "elnett", "hair_styling_cream", "elnett_cream", "ekleel_abha"]
    )


def create_product_1990():
    return _make_hair_styling_product(
        pid=1990, gtin="6281056500292",
        ar_name="بخاخ ملمع ومغذي شعر منمن جيه كزانوفا 200 مل",
        en_name="J. Casanova Hair Shine and Nourishing Spray 200ml",
        brand_ar="جيه كازانوفا", brand_en="J. Casanova",
        type_ar="بخاخ لمعان وتغذية", type_en="Shine & Nourishing Spray",
        volume_ar="200 مل", volume_en="200ml",
        feature_ar="بخاخ المعان الفرنسي المغذي لإشراقة وسلامة الشعر", feature_en="French hair shine spray imparting brilliant nourish and gloss",
        tags_ar=["كازانوفا", "بخاخ_ملمع_شعر", "كازانوفا_شعر", "تغذية_الشعر", "إكليل_أبها"],
        tags_en=["casanova", "hair_shine_spray", "j_casanova", "nourishing_hair_spray", "ekleel_abha"]
    )


def create_product_1991():
    return _make_hair_styling_product(
        pid=1991, gtin="4056800759316",
        ar_name="بخاخ  نيو ويف لتصفيف الشعر  رقم 5 من ويلا 250مل",
        en_name="Wella New Wave Hair Styling Spray No. 5 - 250ml",
        brand_ar="ويلا نيو ويف", brand_en="Wella New Wave",
        type_ar="بخاخ سبراي تثبيت فائق رقم 5", type_en="Ultra Strong Hold Spray No. 5",
        volume_ar="250 مل", volume_en="250ml",
        feature_ar="تثبيت فائق القوة رقم 5 لـ 24 ساعة ومقاومة الرطوبة", feature_en="ultra strong hold level 5 for 24-hour style longevity",
        tags_ar=["ويلا", "نيو_ويف", "بخاخ_مثبت_شعر", "ويلا_رقم_5", "إكليل_أبها"],
        tags_en=["wella", "new_wave", "hair_spray", "wella_no5", "ekleel_abha"]
    )


def create_product_1992():
    return _make_hair_styling_product(
        pid=1992, gtin="4056800759286",
        ar_name="رغوة تكثيف الشعرمن ويلا  200 مل",
        en_name="Wella Hair Volumizing Mousse - 200 ml",
        brand_ar="ويلا", brand_en="Wella",
        type_ar="رغوة موس تكثيف رفيعة", type_en="Volumizing Hair Mousse",
        volume_ar="200 مل", volume_en="200ml",
        feature_ar="رغوة موس لمنح الشعر حجماً وكثافة وتثبيتاً مرناً", feature_en="volumizing mousse for full-bodied lift, volume, and flexible hold",
        tags_ar=["ويلا", "رغوة_تكثيف_الشعر", "موس_ويلا", "تكثيف_الشعر", "إكليل_أبها"],
        tags_en=["wella", "volumizing_mousse", "hair_mousse", "wella_volume", "ekleel_abha"]
    )


print("Loaded all 5 Batch 55 builders complete")
