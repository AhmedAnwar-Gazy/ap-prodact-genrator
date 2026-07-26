import json, os

def create_product_2066():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>رغوة تنظيف البشرة العادية الى الدهنيه من سيرافي 236مل (CeraVe Foaming Facial Cleanser for Normal to Oily Skin - 236ml)</strong> الغسول المنظف الطبي الفاخر الأكثر توصية عالمياً من سيرافي المصمم خصيصاً لتنظيف، تصفية، وإزالة الزيوت الزائدة والمكياج لبشرة الوجه العادية والدهنية دون التسبب في جفاف أو حكة أو تضرر لحاجز البشرة. يرتكز هذا الغسول الأصيل (CeraVe Foaming Cleanser 236ml) على السيراميدات الثلاثية الأساسية (Ceramides 1, 3, 6-II)، النياسيناميد المهدئ (Niacinamide)، وحمض الهيالورونيك (Hyaluronic Acid).</p>
<p>يعمل غسول رغوة سيرافي على تنظيف مسام الوجه عمقاً من الدهون المتراكمة والشوائب، تقليل اللمعان الدهني، وتهدئة البشرة وإعادة توازنها المائي، ليترك وجهك ناعماً كالحرير، ناصع النظافة، منتعشاً، ومحمياً من الانسداد والبثور من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف رغوي ناعم وتصفية فائقة للدهون والشوائب:</strong> ينظف المسام بفاعلية دون تجريد الزيوت الطبيعية.</li>
  <li><strong>ترميم حاجز البشرة بالسيراميدات الثلاثية الأساسية:</strong> تعوض النقص في سيراميدات الوجه الطبيعية.</li>
  <li><strong>تهدئة البشرة وتقليل الاحمرار واللمعان بالنياسيناميد:</strong> ينظم إفراز السيبوم ويهدئ التهيجات.</li>
  <li><strong>ترطيب وحبس الماء بحمض الهيالورونيك:</strong> يمنع شعور الشد والجفاف بعد الغسيل.</li>
  <li><strong>تركيبة خالية 100% من العطور والزيوت والبارابين:</strong> لا تسبب انسداد المسام (Non-Comedogenic).</li>
  <li><strong>عبوة سعة 236 مل بضاغط مريح:</strong> حجم ممتاز للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الوجه بالماء الدافئ.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من جل سيرافي وكوّني رغوة غنية ودلكي برفق بحركات دائرية.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء الدافئ وجففي الوجه برفق (يُستعمل مرتين يومياً صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>السيراميدات الأساسية والنياسيناميد:</strong> ترممان حاجز البشرة وتلطفان التهيج وتنظمان الدهون.</li>
  <li><strong>حمض الهيالورونيك والمنظفات الرغوية اللطيفة:</strong> تنظف المسام وتحفظ الرطوبة الداخلية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يملك بشرة عادية إلى دهنية ويبحث عن رغوة سيرافي المنظفة 236 مل لتنظيف المسام وتصفية الدهون.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سيرافي (CeraVe)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / منظفات سيرافي الرغوية للوجه 236ml</td></tr>
  <tr><th>نوع المنتج</th><td>رغوة غسول طبي مصفٍ للدهون بالسيراميدات والنياسيناميد (236ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>236 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة العادية، الدهنية، المختلطة والمعرضة لحب الشباب</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، مرطب، ناصع النظافة وغير لامع بالدهون</td></tr>
  <tr><th>الملمس</th><td>جل سائل شفاف ينقلب لرغوة منعشة غنية</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>سيراميدات (1, 3, 6-II)، نياسيناميد، حمض الهيالورونيك</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا / الولايات المتحدة (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>CeraVe LLC (L'Oréal Group)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد النياسيناميد والسيراميدات في رغوة سيرافي (CeraVe Foaming Cleanser)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول سيرافي الرغوي مشكلة الإفرازات الدهنية الزائدة، اللمعان بالوجه، انسداد المسام بالكوميدونات، وجفاف الجلد بعد الغسل.</p>

<h3>لماذا تنجح تركيبة CeraVe Foaming Formula؟</h3>
<p>لأن النياسيناميد ينظم عمل الغدد الدهنية بينما تضمن السيراميدات عدم تهدم الغشاء الوقائي أثناء التنظيف.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنظيف مرتين يومياً بالماء الدافئ:</strong> يمنع تراكم الدهون والأكسدة.<br>
2. <strong>التكميل بمرطب خفيف خالي من الزيوت من سيرافي:</strong> يحفظ الترطيب الداخلي.<br>
3. <strong>تجنب الفرك الشديد:</strong> يحافظ على نعومة واستقرار البشرة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الغسولات الرغوية تجفف البشرة دائماً."<br>
<strong>الحقيقة:</strong> رغوة سيرافي مصممة بحمض الهيالورونيك والسيراميدات لمنح تنظيف ناصع دون أي جفاف.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يذيب النياسيناميد الدهون المحتبسة بينما تلتصق السيراميدات بالكيراتين لحماية الحاجز الدهني (Lipid Barrier).</p>"""

    faqs = [
        ("ما هو رغوة تنظيف البشرة العادية الى الدهنيه من سيرافي 236مل؟", "هو غسول طبي رغوي خالي من العطور والزيوت من سيرافي بالسيراميدات والنياسيناميد للبشرة العادية والدهنية (236 مل)."),
        ("ما هي فوائد النياسيناميد والسيراميدات الثلاثية للبشرة الدهنية؟", "ينظم النياسيناميد الدهون ويهدئ التهيجات، بينما ترمم السيراميدات حاجز الوجه وتمنع الجفاف."),
        ("هل ينظف المسام ويقلل الدهون دون جفاف؟", "نعم، مثبت سريرياً في تنظيف المسام وتقليل الدهون دون تسبيب أي جفاف أو شد بالوجه."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة مزودة بضاغط مريح سعة 236 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الوجه، ضعي كمية وكوّني رغوة، دلكي برفق واشطفي بالماء مرتين يومياً."),
        ("هل هو خالٍ من العطور والزيوت والبارابين؟", "نعم، 100% خالٍ من العطور والزيوت والبارابين ومختبر درماتولوجياً."),
        ("أين صُنع غسول سيرافي الرغوي؟", "صُنع بواسطة CeraVe LLC (مجموعة L'Oréal العالمية)."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات سيرافي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب البشرة الدهنية والمختلطة والمكونة للبثور؟", "نعم، ممتاز للبشرة العادية، الدهنية، المختلطة والمعرضة للبثور."),
        ("هل يترك البشرة غير لامعة ونظيفة؟", "نعم، يترك البشرة غير لامعة بالدهون ونظيفة وناعمة كالحرير."),
        ("هل عبوة 236 مل بضاغط مريحة؟", "نعم، عبوة أنيقة بضاغط مريح جداً للاستخدام اليومي والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل سيرافي الماركة الأولى الموصى بها طبياً؟", "نعم، CeraVe الماركة رقم 1 الموصى بها طبياً من أطباء الجلدية."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل يزيل المكياج والأوساخ؟", "نعم، يزيل المكياج الخفيف والزيوت والأوساخ بفاعلية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يقلل الرؤوس السوداء والبيضاء؟", "نعم، ينظف المسام ويقلل الرؤوس السوداء والبيضاء."),
        ("هل يسبب انسداد المسام؟", "لا، تركيبة خالية من الزيوت وغير مسببة للانسداد (Non-Comedogenic)."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يفضل اتباع مرطب خفيف بعده؟", "نعم، يُفضل استخدام مرطب خفيف خالي من الزيوت بعد الغسل."),
        ("هل يناسب الصيف والشتاء؟", "نعم، ممتاز لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج طبي فاخر وأساسي لكل روتين عناية."),
        ("هل يعيد المظهر المشرق الصافي للوجه؟", "نعم، يمنح الوجه مظهراً صافياً ومشرقاً."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>CeraVe Foaming Facial Cleanser for Normal to Oily Skin - 236ml</strong> is the world's most dermatologist-recommended authentic luxury medical foaming cleanser from CeraVe designed to clean, clarify, and remove excess oil and makeup for normal to oily facial skin without drying, stinging, or damaging the skin barrier. Built upon 3 Essential Ceramides (1, 3, 6-II), soothing Niacinamide, and Hyaluronic Acid.</p>
<p>CeraVe Foaming Cleanser deeply purifies facial pores of accumulated sebum and impurities, reduces oily shine, and soothes and balances skin moisture, leaving your face touchably silky soft, spotlessly clean, refreshed, and protected against breakouts from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Gentle Foaming Cleansing for Oil & Sebum Control:</strong> Cleanses pores effectively without stripping natural oils.</li>
  <li><strong>Skin Barrier Restoration with 3 Essential Ceramides:</strong> Replenishes natural facial skin ceramides.</li>
  <li><strong>Soothing Care & Shine Control with Niacinamide:</strong> Regulates sebum production while calming redness.</li>
  <li><strong>Internal Hydration Locking with Hyaluronic Acid:</strong> Prevents post-wash tightness and dryness.</li>
  <li><strong>100% Fragrance-Free, Oil-Free & Paraben-Free:</strong> Non-comedogenic formula that will not clog pores.</li>
  <li><strong>Convenient 236ml Pump Dispenser Bottle:</strong> Ideal size for daily care and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet facial skin with warm water.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of CeraVe gel, work into a rich lather, and massage gently in circular motions.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and pat face dry (use twice daily morning and night).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Essential Ceramides & Niacinamide:</strong> Repair damaged skin barriers while calming irritation and regulating oil.</li>
  <li><strong>Hyaluronic Acid & Mild Foaming Cleansers:</strong> Cleanse pores while maintaining internal moisture balance.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial skin application.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with normal to oily skin seeking CeraVe Foaming Cleanser 236ml for pore cleansing and oil control.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>CeraVe</td></tr>
  <tr><th>Category</th><td>Skincare / CeraVe Medical Foaming Cleansers 236ml</td></tr>
  <tr><th>Product Type</th><td>Fragrance-Free Oil-Free Ceramide & Niacinamide Foaming Cleanser (236ml)</td></tr>
  <tr><th>Volume/Weight</th><td>236 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Normal, Oily, Combination & Acne-Prone Skin</td></tr>
  <tr><th>Finish</th><td>Spotlessly clean, 24H hydrated, matte & silky soft oil-free face</td></tr>
  <tr><th>Texture</th><td>Clear liquid gel transforming into a rich gentle foaming lather</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>3 Essential Ceramides (1, 3, 6-II), Niacinamide, Hyaluronic Acid</td></tr>
  <tr><th>Country of Origin</th><td>France / USA</td></tr>
  <tr><th>Manufacturer</th><td>CeraVe LLC (L'Oréal Group)</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Niacinamide Sebum Regulation & Ceramide Barrier Protection</h2>

<h3>What problem does this solve?</h3>
<p>CeraVe Foaming Cleanser resolves excess sebum, facial oil shine, clogged pores, comedones, and post-wash dryness.</p>

<h3>Why choose CeraVe Foaming Cleanser?</h3>
<p>Niacinamide regulates sebaceous gland activity while 3 Essential Ceramides protect the skin lipid barrier during washing.</p>"""

    en_faqs = [
        ("What is CeraVe Foaming Facial Cleanser for Normal to Oily Skin - 236ml?", "It is a medical fragrance-free oil-free foaming cleanser from CeraVe with Ceramides and Niacinamide for normal to oily skin (236ml)."),
        ("What are the benefits of Niacinamide and 3 essential Ceramides?", "Niacinamide regulates oil and soothes irritation, while Ceramides restore the facial skin barrier and prevent dryness."),
        ("Does it clean pores and control oil shine without dryness?", "Yes, clinically proven to clean pores and reduce excess shine without tightness or dryness."),
        ("What volume is contained in this bottle?", "236ml pump dispenser bottle."),
        ("How do I use it correctly?", "Wet face, apply gel, lather, massage gently and rinse with warm water twice daily."),
        ("Is it fragrance-free, oil-free, and paraben-free?", "Yes, 100% free from fragrances, oils, and parabens, and dermatologically tested."),
        ("Where is CeraVe Foaming Cleanser manufactured?", "By CeraVe LLC (L'Oréal Group)."),
        ("How do I verify authenticity at Ekleel Abha?", "All CeraVe products at Ekleel Abha are 100% original."),
        ("Is it suitable for normal, oily, and acne-prone skin?", "Yes, excellent for normal, oily, combination, and acne-prone skin."),
        ("Does it leave face matte and clean?", "Yes, leaves face matte, oil-free, spotlessly clean, and silky soft."),
        ("Is the 236ml pump bottle convenient?", "Yes, sleek pump dispenser bottle ideal for daily care and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is CeraVe the #1 dermatologist recommended brand?", "Yes, CeraVe is the #1 dermatologist recommended facial cleanser brand globally."),
        ("How many times daily?", "Twice daily (morning and night)."),
        ("Does it remove makeup and dirt?", "Yes, effectively cleanses light makeup, excess sebum, and daily dirt."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help reduce blackheads and whiteheads?", "Yes, cleanses pores reducing blackheads and comedone formation."),
        ("Does it clog pores?", "No, oil-free non-comedogenic formula."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is following with an oil-free moisturizer recommended?", "Yes, follow with a lightweight oil-free moisturizer after cleansing."),
        ("Is it good for all seasons?", "Yes, ideal oil-control cleansing for summer and winter."),
        ("Is it a nice skincare gift?", "Yes, a premier medical essential for facial care routines."),
        ("Does it restore clean radiant skin appearance?", "Yes, gives facial skin a clear healthy radiant look."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2066",
        "sku": "EK-2066",
        "gtin": "3337875597197",
        "brand": "CeraVe",
        "ar": {
            "title": "رغوة تنظيف البشرة العادية الى الدهنيه من سيرافي 236مل",
            "meta_title": "رغوة سيرافي للبشرة العادية والدهنية 236مل | إكليل أبها",
            "meta_description": "اشتري رغوة تنظيف البشرة العادية إلى الدهنية من سيرافي (236 مل). غسول طبي بالسيراميدات والنياسيناميد لتصفية المسام وتقليل الدهون. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["سيرافي", "رغوة_سيرافي", "غسول_البشرة_الدهنية", "نياسيناميد_سيرافي", "إكليل_أبها"]
        },
        "en": {
            "title": "CeraVe Foaming Facial Cleanser for Normal to Oily Skin - 236ml",
            "meta_title": "CeraVe Foaming Facial Cleanser 236ml | Ekleel Abha",
            "meta_description": "Buy original CeraVe Foaming Facial Cleanser for Normal to Oily Skin (236ml). Fragrance-free oil-control ceramide cleanser. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["cerave", "cerave_foaming_cleanser", "oily_skin_cleanser", "niacinamide_cleanser", "ekleel_abha"]
        }
    }


def create_product_2067():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>لوشن الجسم فيتامين سي للتفتيح والترطيب بعد الاستحمام 480مل (Vitamin C Body Lotion for Brightening and Hydration Post-Shower - 480ml)</strong> لوشن التفتيح والترطيب المكثف الفاخر الأصيل المصمم خصيصاً لتفتيح وتوحيد لون بشرة الجسم والتخلص من التصبغات والبقع الداكنة والجفاف بعد الاستحمام مباشرة. يرتكز هذا اللوشن الأصيل (Vitamin C Body Lotion 480ml) على فيتامين C النقي المضاد للأكسدة (Pure Vitamin C)، حمض الهيالورونيك، وخلاصات التفتيح النباتية.</p>
<p>يعمل لوشن فيتامين سي للجسم على تثبيط إنزيم التايروسينيز المسبب للتصبغات الداكنة، إزالة الخلايا الميتة والخشونة، وتغذية الجلد وحفظ رطوبته لـ 24 ساعة، ليترك بشرة جسمك ناعمة كالحرير، ناصعة البياض، موحدة اللون، ومفعمة بالانتعاش والإشراق بعد كل استحمام.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وتوحيد لون بشرة الجسم بفيتامين C النقي:</strong> يقلل التصبغات والبقع الداكنة وآثار الشمس.</li>
  <li><strong>ترطيب وتغذية مكثفة بعد الاستحمام لـ 24 ساعة:</strong> بحجم كبير 480 مل يحفظ ليونة ونعومة الجلد.</li>
  <li><strong>تحسين مرونة ونضارة البشرة:</strong> يمنح الوجه والجسم ملمساً حريرياً ناعماً وتوهجاً صحياً.</li>
  <li><strong>امتصاص سريع ودون ترك طبقة دهنية ملتصقة:</strong> يسهل ارتداء الملابس فوراً بعد التطبيق.</li>
  <li><strong>تركيبة غنية بمضادات الأكسدة:</strong> تحمي الجلد من التلوث والإجهاد البيئي.</li>
  <li><strong>عبوة ضخمة مزودة بضاغط سعة 480 مل:</strong> حجم ممتاز للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسية من لوشن فيتامين سي على بشرة الجسم النظيفة والرطبة بعد الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي برفق بحركات دائرية ناعمة حتى الامتصاص الكامل (يُستعمل يومياً بعد الاستحمام وقبل النوم).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>فيتامين C النقي (Pure Vitamin C):</strong> يثبط تشكّل صبغة الميلانين ويفتح المناطق الداكنة.</li>
  <li><strong>حمض الهيالورونيك والمركبات المرطبة:</strong> يحفظان التوازن المائي للجلد ويمنعان التققوق والجفاف.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن لوشن فيتامين سي للجسم 480 مل لتفتيح وتوحيد لون البشرة والترطيب بعد الاستحمام.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>فيتامين سي كير (Vitamin C Care)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / لوشنات التفتيح والترطيب بفيتامين سي 480ml</td></tr>
  <tr><th>نوع المنتج</th><td>لوشن مبيض ومفتح ومغدٍ للجسم بفيتامين C بعد الاستحمام (480ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>480 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (خصيصاً المتصبغة، الجافة، والداكنة)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، موحد اللون، ناصع البياض ومفعم بالتوهج 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>لوشن كريمي خفيف يمتص فورياً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر فيتامين سي الحمضي المنعش الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>فيتامين C نقي، حمض الهيالورونيك، خلاصات تفتيح نباتية</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين / كوريا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Vitamin C Beauty Care Inc.</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد فيتامين C النقي والتفتيح بعد الاستحمام في Vitamin C Body Lotion</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج لوشن فيتامين سي مشكلة التصبغات الداكنة بالجسم، أثر الشمس، عدم توحد اللون، والجفاف بعد الاستحمام.</p>

<h3>لماذا تنجح تركيبة Pure Vitamin C Body Lotion؟</h3>
<p>لأن فيتامين C النقي يثبط إنزيم Tyrosinase المسبب للتصبغ بينما يضمن الامتصاص بعد الاستحمام وصول المغذيات لعمق المسام.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق فوراً على بشرة دافئة بعد الاستحمام:</strong> يستغل تفتح المسام لزيادة امتصاص فيتامين C.<br>
2. <strong>الاستخدام المنتظم مرتين يومياً:</strong> يسرع توحيد وتفتيح مناطق الجسم الداكنة.<br>
3. <strong>الترطيب المستمر:</strong> يحمي البشرة من نكسات التصبغ والجفاف.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "لوشنات فيتامين سي تسبب حساسية واحرار بالجلد."<br>
<strong>الحقيقة:</strong> هذا اللوشن مدعم بحمض الهيالورونيك والمركبات المهدئة التي تمنع التهيج وتضمن ترطيباً ناعماً.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يكافح فيتامين C الشوارد الحرة (Free Radicals) ويثبط تخليق صبغة الميلانين محققاً تفتيحاً وتوحيداً ناصعاً.</p>"""

    faqs = [
        ("ما هو لوشن الجسم فيتامين سي للتفتيح والترطيب بعد الاستحمام 480مل؟", "هو لوشن مبيض ومفتح ومغدٍ للجسم بفيتامين C النقي والهيالورونيك للترطيب وتوحيد اللون بعد الاستحمام (480 مل)."),
        ("ما هي فوائد فيتامين C النقي وحمض الهيالورونيك للجسم؟", "يفتحان التصبغات والبقع الداكنة، يوحدان لون البشرة، ويمنحان ترطيباً 24 ساعة دون دهنية."),
        ("هل يفتح الجسم ويوحد اللون فورياً بعد الاستحمام؟", "نعم، مثبت سريرياً في تفتيح وتوحيد لون بشرة الجسم والترطيب الفائق 24 ساعة."),
        ("ما حجم العبوة؟", "تأتي بعبوة ضخمة مزودة بضاغط مريح سعة 480 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على بشرة دافئة بعد الاستحمام ودلكي برفق حتى الامتصاص مرتين يومياً."),
        ("هل يمتص سريعاً دون ترك طبقة دهنية؟", "نعم، يمتص فورياً مما يتيح ارتداء الملابس فوراً دون بقع."),
        ("أين صُنع لوشن فيتامين سي للجسم؟", "صُنع وفق أعلى معايير جودة العناية والتفتيح العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        ("ما رائحة لوشن فيتامين سي؟", "عطر فيتامين سي الحمضي المنعش الفاخر."),
        ("هل يناسب المناطق الداكنة بالجسم؟", "نعم، ممتاز لتفتيح وتوحيد المناطق الداكنة بالجسم واليدين والكوعين."),
        ("هل عبوة 480 مل بضاغط مريحة؟", "نعم، عبوة ضخمة بضاغط مريح جداً للاستخدام العائلي اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل هو ماركة موثوقة في التفتيح؟", "نعم، علامة شهيرة وموثوقة جداً في مستحضرات التفتيح."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً بعد الاستحمام وقبل النوم."),
        ("هل يمنح البشرة توهجاً ولمعاناً؟", "نعم، يمنح البشرة توهجاً وإشراقة ناصعة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في الوقاية من جفاف الشتاء؟", "نعم، ترطيب وتفتيح مثالي لجميع فصول السنة."),
        ("هل يترك ملمساً ناعماً كالحرير؟", "نعم، يترك الجسم مفعماً بالنضارة والنعومة الحريرية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يفضل استخدامه على بشرة رطبة؟", "نعم، تطبيقه على بشرة رطبة بعد الاستحمام يضاعف فاعلية التفتيح والترطيب."),
        ("هل يناسب جميع أنواع البشرة؟", "نعم، مناسب لجميع أنواع بشرة الجسم."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج عناية وتفتيح مفيد وأنيق جداً."),
        ("هل يمنح ترطيباً طوال اليوم؟", "نعم، يحبس الترطيب الداخلي لـ 24 ساعة متواصلة."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Vitamin C Body Lotion for Brightening and Hydration Post-Shower - 480ml</strong> is an authentic luxury post-shower body whitening, brightening, and hydrating lotion designed to lighten dark spots, unify body skin tone, and eliminate post-shower dryness. Built upon Pure Vitamin C antioxidants, Hyaluronic Acid, and botanical brightening extracts.</p>
<p>Vitamin C Body Lotion suppresses tyrosinase enzymes responsible for dark pigmentation, removes dead skin roughness, and locks in internal skin hydration for 24 hours, leaving your body skin touchably silky soft, visibly brightened, even-toned, and radiant after every shower.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Skin Brightening & Tone Evening with Pure Vitamin C:</strong> Reduces hyperpigmentation, dark spots, and sun damage.</li>
  <li><strong>Intensive 24-Hour Post-Shower Hydration:</strong> Large 480ml format maintaining skin softness and elasticity.</li>
  <li><strong>Skin Elasticity & Radiance Restoration:</strong> Delivers a silky soft touch and natural healthy skin glow.</li>
  <li><strong>Rapid Absorption with Zero Heavy Greasy Residue:</strong> Allows immediate dressing post-application without staining.</li>
  <li><strong>Antioxidant-Rich Formula:</strong> Shields skin against environmental stress and pollution.</li>
  <li><strong>Generous 480ml Pump Dispenser Bottle:</strong> Excellent value for continuous daily family use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of Vitamin C lotion onto clean damp body skin post-shower.</li>
  <li><strong>Step 2:</strong> Massage gently in smooth circular motions until fully absorbed (use daily post-shower & bedtime).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Vitamin C:</strong> Suppresses melanin synthesis and lightens hyperpigmented dark zones.</li>
  <li><strong>Hyaluronic Acid & Hydrating Agents:</strong> Preserve water balance preventing cracking and skin tightness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Vitamin C Body Lotion 480ml for post-shower skin brightening, tone evening, and hydration.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Vitamin C Care</td></tr>
  <tr><th>Category</th><td>Body Care / Vitamin C Skin Brightening Lotions 480ml</td></tr>
  <tr><th>Product Type</th><td>Post-Shower Vitamin C Brightening & Hydrating Body Lotion (480ml)</td></tr>
  <tr><th>Volume/Weight</th><td>480 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Specifically Hyperpigmented, Dark & Dry Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, even-toned, brightened & 24H hydrated body skin</td></tr>
  <tr><th>Texture</th><td>Lightweight fast-absorbing smooth lotion</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh citrus Vitamin C scent</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Vitamin C, Hyaluronic Acid, Botanical Brightening Extracts</td></tr>
  <tr><th>Country of Origin</th><td>China / Korea</td></tr>
  <tr><th>Manufacturer</th><td>Vitamin C Beauty Care Inc.</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Pure Vitamin C Tyrosinase Suppression & Post-Shower Epidermal Absorption</h2>

<h3>What problem does this solve?</h3>
<p>Vitamin C Body Lotion resolves dark body spots, sun damage, uneven skin tone, and post-shower dryness.</p>

<h3>Why choose Pure Vitamin C Body Lotion?</h3>
<p>Pure Vitamin C inhibits Tyrosinase enzyme oxidation while post-shower damp skin application maximizes deep nutrient absorption.</p>"""

    en_faqs = [
        ("What is Vitamin C Body Lotion for Brightening and Hydration Post-Shower - 480ml?", "It is a post-shower body brightening and hydrating lotion with Pure Vitamin C and Hyaluronic Acid (480ml)."),
        ("What are the benefits of Pure Vitamin C and Hyaluronic Acid for the body?", "They brighten dark spots, unify body skin tone, and deliver 24-hour hydration without greasiness."),
        ("Does it brighten body skin and unify tone effectively post-shower?", "Yes, clinically proven to brighten body skin tone and deliver 24-hour hydration."),
        ("What volume is contained in this bottle?", "480ml pump dispenser bottle."),
        ("How do I use it correctly?", "Apply to warm damp skin post-shower, massage gently until absorbed twice daily."),
        ("Does it absorb rapidly without leaving a greasy film?", "Yes, absorbs rapidly allowing immediate dressing without staining clothes."),
        ("Where is Vitamin C Body Lotion manufactured?", "Manufactured to international skincare and brightening standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original."),
        ("What scent does Vitamin C Body Lotion have?", "Luxurious fresh citrus Vitamin C fragrance."),
        ("Is it suitable for dark body zones?", "Yes, excellent for brightening and unifying dark body zones, hands, and elbows."),
        ("Is the 480ml pump bottle convenient?", "Yes, generous pump bottle convenient for daily family use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it a trusted brightening brand?", "Yes, a famous trusted brand in skin brightening cosmetics."),
        ("How many times daily?", "Once or twice daily post-shower and bedtime."),
        ("Does it impart skin glow and radiance?", "Yes, gives body skin a bright natural glow."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help prevent winter skin dryness?", "Yes, ideal brightening and hydration for all seasons."),
        ("Does it leave a silky soft feel?", "Yes, leaves body skin touchably soft and fresh."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is applying on damp skin recommended?", "Yes, applying on damp skin post-shower doubles brightening and hydration efficacy."),
        ("Is it suitable for all skin types?", "Yes, suitable for all body skin types."),
        ("Is it a nice skincare gift?", "Yes, an elegant practical body care gift."),
        ("Does it deliver long-lasting hydration?", "Yes, locks in internal skin moisture for 24 continuous hours."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2067",
        "sku": "EK-2067",
        "gtin": "6947835825276",
        "brand": "Vitamin C Care",
        "ar": {
            "title": "لوشن الجسم فيتامين سي للتفتيح والترطيب بعد الاستحمام 480مل",
            "meta_title": "لوشن الجسم فيتامين سي للتفتيح 480مل | إكليل أبها",
            "meta_description": "اشتري لوشن الجسم فيتامين سي للتفتيح والترطيب بعد الاستحمام (480 مل). لوشن مبيض بفيتامين C النقي والهيالورونيك لتوحيد لون الجسم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["لوشن_فيتامين_سي", "تفتيح_الجسم", "لوشن_بعد_الاستحمام", "توحيد_لون_البشرة", "إكليل_أبها"]
        },
        "en": {
            "title": "Vitamin C Body Lotion for Brightening and Hydration Post-Shower - 480ml",
            "meta_title": "Vitamin C Body Lotion Brightening 480ml | Ekleel Abha",
            "meta_description": "Buy original Vitamin C Body Lotion for Brightening and Hydration Post-Shower (480ml). Pure Vitamin C skin whitening body lotion. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["vitamin_c_lotion", "body_brightening_lotion", "post_shower_lotion", "skin_whitening", "ekleel_abha"]
        }
    }


def create_product_2068():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>مناديل تنظيف الاسنان 12منديل (Teeth Cleaning Wipes - 12 Wipes)</strong> مناديل العناية بالفم وتنظيف الأسنان الابتكارية الفاخرة المصممة خصيصاً لتنظيف وإزالة الطبقات البكتيرية والترسبات وبقع القهوة والشاي والتنعيم الفوري للفم والأنفاس دون الحاجة للماء أو الفرشاة. تركز هذه المناديل الأصيلة (Teeth Wipes 12 Pack) على خلاصة النعناع الطبيعي المبتكرة، المركبات المطهرة لطبقة المينا، والتركيبة الخالية 100% من السكر والمواد الحافظة القاسية.</p>
<p>تعمل مناديل تنظيف الأسنان على مسح وإزالة البلاك والطبقات الملونة عن أسطح الأسنان، تلطيف اللثة، وتزويدك بأنفاس معطرة بالنعناع النقي والانتعاش، لتترك أسنانك ناصعة النظافة، ملساء، ومحمية من الروائح البكتيرية أثناء السفر والعمل وفي أي وقت ومكان.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف وإزالة سريعة لبقع القهوة والبلاك بدون ماء:</strong> تمسح الترسبات عن أسطح الأسنان بسلاسة.</li>
  <li><strong>إنعاش فوري للأنفاس بنكهة النعناع الطبيعي:</strong> تسيطر على الروائح البكتيرية وتمنح ثقة كاملة.</li>
  <li><strong>مناديل لبس على الأصبع ابتكارية وعملية:</strong> تتيح مسح الأسنان بسهولة وأمان في أي مكان.</li>
  <li><strong>خالية 100% من السكر، البارابين، والمواد القاسية:</strong> آمنة ولطيفة جداً على مينا الأسنان واللثة.</li>
  <li><strong>عبوة مغلفة فردياً سعة 12 منديل:</strong> حجم مدمج مثالي للحقيبة، الجيب، والسفر والتنقل.</li>
  <li><strong>مثالية بعد الوجبات والمشروبات الملونة أثناء العمل والتنقل:</strong> لا تتطلب الشطف.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> افتحي الغلاف الفردي والبسي المنديل على أصبعك السبابة (Finger Wipe).</li>
  <li><strong>الخطوة الثانية:</strong> امسحي أسطح الأسنان الأمامية والخلفية واللثة برفق لإزالة الترسبات والبقع.</li>
  <li><strong>الخطوة الثالثة:</strong> تخلصي من المنديل المستخدم واستمتعي بأنفاس ناصعة النظافة (يُستعمل بعد الوجبات والمشروبات وعند الحاجة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة النعناع الطبيعي والزيوت المنقية:</strong> تمنح أنفاساً عاطرة وتطهر الفم من البكتيريا.</li>
  <li><strong>نسيج المنديل الدقيق والمكونات المنظفة للمينا:</strong> تزيل بقايا الطعام والبلاك دون خدش الأسنان.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الفموي الموضعي لتنظيف الأسنان واللثة.</li>
  <li>تجنبي البلع الشديد وتخلصي من المنديل بعد الاستخدام.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن مناديل تنظيف الأسنان 12 منديل لتنظيف الفم وتنعيم الأنفاس أثناء العمل والتنقل.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كير تيث (Teeth Care Wipes)</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم / مناديل تنظيف الأسنان وإزالة البقع 12 Wipes</td></tr>
  <tr><th>نوع المنتج</th><td>مناديل أصبع ابتكارية لتنظيف الأسنان وإنعاش الأنفاس بنكهة النعناع (12 منديل)</td></tr>
  <tr><th>الحجم/الوزن</th><td>12 منديل مغلف فردياً</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع الفئات والأسنان (مناسب للأسنان واللثة الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان ناصعة النظافة، ملساء، معطرة بالنعناع وخالية من بقايا الطعام والتصطبغات</td></tr>
  <tr><th>الملمس</th><td>مناديل أصبع قماشية ناعمة مرطبة بسائل النعناع المنعش</td></tr>
  <tr><th>العطر</th><td>عطر ونكهة النعناع الطبيعي المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة النعناع الطبيعي، منظفات مينا الأسنان، زايليتول خالي من السكر</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين / كوريا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Oral Care Products Inc.</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون والمراهقون (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد مناديل الأسنان الأصبع ونكهة النعناع (Teeth Wipes)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج مناديل الأسنان مشكلة بقايا الطعام وتصبغات القهوة والشاي والروائح الفموية أثناء العمل والتنقل بعيداً عن الفرشاة والماء.</p>

<h3>لماذا تنجح تركيبة Finger Teeth Wipes؟</h3>
<p>لأن النسيج الدقيق يزيل البلاك ميكانيكياً بينما يقضي خلاصة النعناع والزايليتول على بكتيريا البخر الفموي.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>المسح الفوري بعد تناول القهوة أو الوجبات:</strong> يمنع تغلغل التصبغات في مينا الأسنان.<br>
2. <strong>الحفظ بالحقيبة أو الجيب:</strong> يضمن الاستعداد الدائم للأنفاس العاطرة.<br>
3. <strong>التكميل بالفرشاة والمعجون ليلاً:</strong> يحافظ على صحة الفم والأسنان الشاملة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مناديل الأسنان تخدش مينا الأسنان وتسبب جروح اللثة."<br>
<strong>الحقيقة:</strong> نسيج المناديل مصمم بألياف فائقة النعومة تنظف أسطح الأسنان وتلطف اللثة بأمان تام.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تزيل الألياف طبقة البايوفيلم (Biofilm) البكتيرية ميكانيكياً مع تحييد الأحماض الفموية ومنع التسوس.</p>"""

    faqs = [
        ("ما هي مناديل تنظيف الاسنان 12منديل؟", "هي مناديل أصبع ابتكارية فاخرة بنكهة النعناع لتنظيف الأسنان وإنعاش الأنفاس وإزالة بقع القهوة بدون ماء (12 منديل)."),
        ("ما هي فوائد مناديل الأسنان الأصبع ونكهة النعناع؟", "تزيل البلاك وتصبغات القهوة والطعام، تسيطر على روائح الفم، وتنعش الأنفاس فورا."),
        ("هل تنظف الأسنان وتزيل البقع بدون فرشاة أو ماء؟", "نعم، مثبتة في تنظيف أسطح الأسنان وإزالة البقع والروائح بدون ماء أو فرشاة."),
        ("ما عدد المناديل بالعبوة؟", "تأتي بعبوة أنيقة تحتوي على 12 منديل مغلف فردياً."),
        ("كيف يُستخدم بالشكل الصحيح؟", "البسي المنديل على أصبعك السبابة، امسحي أسطح الأسنان واللثة وتخلصي منه بعد الاستخدام."),
        ("هل هي خالية 100% من السكر والبارابين؟", "نعم، 100% خالية من السكر والبارابين وآمنة على المينا."),
        ("أين صُنعت مناديل الأسنان؟", "صُنع وفق أعلى معايير جودة العناية بالفم العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        ("ما رائحة ونكهة مناديل الأسنان؟", "نكهة النعناع الطبيعي المنعش اللطيف."),
        ("هل هي مغلفة فردياً وسهلة الحمل؟", "نعم، كل منديل مغلف فردياً بنظافة تامة ومثالي للجيب والحقيبة."),
        ("هل عبوة 12 منديل مناسبة للسفر والعمل؟", "نعم، عبوة أنيقة مدمجة مثالية للعمل، السفر، والمناسبات."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل هي مناسبة بعد شرب القهوة والشاي؟", "نعم، ممتازة جداً لمسح تصبغات القهوة والشاي فورياً بعد الشرب."),
        ("كم مرة يومياً؟", "عند الحاجة وبعد الوجبات والمشروبات الملونة."),
        ("هل تتطلب الشطف بالماء بعد المسح؟", "لا تتطلب الشطف بالماء على الإطلاق."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل تناسب الأسنان واللثة الحساسة؟", "نعم، نسيج ناعم جداً آمن على الأسنان واللثة الحساسة."),
        ("هل تمنح ثقة كاملة بأنفاس منعشة؟", "نعم، تمنح أنفاساً معطرة بنكهة النعناع وثقة كاملة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يصلح للمكتبيين وأصحاب الأعمال؟", "نعم، خيار مثالي جداً في المكتب والعمل والتنقل."),
        ("هل تمنع تشكل البلاك والبقع؟", "نعم، مسح الأسنان يمنع تراكم وتصلب البلاك على المينا."),
        ("هل يصلح هدية مبتكرة وأنيقة؟", "نعم، منتج مبتكر وعملي جداً في العناية الشخصية."),
        ("هل يترك أسطح الأسنان ملساء؟", "نعم، ينظف الأسنان ويترك ملمسها أملس وناصعاً."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Teeth Cleaning Wipes - 12 Wipes</strong> are authentic luxury innovative finger dental care wipes designed to clean, remove plaque and coffee/tea stains, and immediately freshen breath without water or a toothbrush. Built upon natural refreshing mint extracts, enamel-safe cleansers, and a 100% sugar-free, harsh chemical-free formula.</p>
<p>Teeth Cleaning Wipes sweep away plaque film and colored food deposits from tooth surfaces, soothe gums, and infuse your mouth with crisp mint freshness, leaving your teeth touchably smooth, spotlessly clean, and protected against bacterial odors during work, travel, and on-the-go moments.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Waterless Coffee Stain & Plaque Removal:</strong> Wipes away deposits from tooth surfaces smoothly.</li>
  <li><strong>Instant Minty Breath Freshening:</strong> Controls bacterial breath odors delivering complete confidence.</li>
  <li><strong>Innovative Practical Finger Sleeve Wipes:</strong> Enables safe easy tooth wiping anywhere without water.</li>
  <li><strong>100% Sugar-Free & Paraben-Free Formula:</strong> Safe and gentle on enamel and sensitive gums.</li>
  <li><strong>12 Individually Wrapped Wipes:</strong> Compact size ideal for pocket, handbag, work, and travel.</li>
  <li><strong>Ideal Post-Meals & Coffee Drinks:</strong> Requires no water rinsing.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Tear open individual wrapper and slip the wipe onto your index finger (Finger Wipe).</li>
  <li><strong>Step 2:</strong> Gently wipe across front and back tooth surfaces and gums to remove deposits and stains.</li>
  <li><strong>Step 3:</strong> Discard used wipe and enjoy fresh minty breath (use post-meals, coffee & as needed).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Mint Extract & Purifying Essential Oils:</strong> Deliver fresh minty breath while purifying the mouth.</li>
  <li><strong>Micro-Textured Cloth & Enamel Cleansers:</strong> Remove food particles and plaque without scratching tooth enamel.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For oral topical application on teeth and gums.</li>
  <li>Do not swallow wipe; discard after single use.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Teeth Cleaning Wipes 12 Pack for instant waterless oral cleansing and minty breath freshening.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Teeth Care Wipes</td></tr>
  <tr><th>Category</th><td>Oral Care / Teeth Cleaning & Stain Removal Wipes 12 Pack</td></tr>
  <tr><th>Product Type</th><td>Innovative Waterless Mint Finger Teeth Cleaning Wipes (12 Wipes)</td></tr>
  <tr><th>Volume/Weight</th><td>12 Individually Wrapped Wipes</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Dental & Oral Types (Safe for Sensitive Teeth & Gums)</td></tr>
  <tr><th>Finish</th><td>Spotlessly clean, smooth teeth & fresh minty breath without stains</td></tr>
  <tr><th>Texture</th><td>Soft micro-textured finger cloth moistened with mint solution</td></tr>
  <tr><th>Fragrance</th><td>Fresh natural mint flavor and aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Mint Extract, Enamel Cleansers, Sugar-Free Xylitol</td></tr>
  <tr><th>Country of Origin</th><td>China / Korea</td></tr>
  <tr><th>Manufacturer</th><td>Oral Care Products Inc.</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Micro-Textured Biofilm Removal & Minty Odor Neutralization</h2>

<h3>What problem does this solve?</h3>
<p>Teeth Cleaning Wipes resolve coffee stains, food particles, bacterial breath odor, and lack of toothbrush access on-the-go.</p>

<h3>Why choose Finger Teeth Cleaning Wipes?</h3>
<p>Micro-textured fibers mechanically remove bacterial plaque film while natural mint and xylitol neutralize volatile sulfur compounds.</p>"""

    en_faqs = [
        ("What are Teeth Cleaning Wipes - 12 Wipes?", "They are innovative luxury mint-flavored finger wipes for cleaning teeth, removing coffee stains, and freshening breath without water (12 wipes)."),
        ("What are the benefits of finger teeth wipes and mint flavor?", "Remove plaque and coffee stains, control mouth odors, and deliver instant minty breath."),
        ("Do they clean teeth and remove stains without a brush or water?", "Yes, clinically proven to sweep away tooth surface stains and odors without water or a toothbrush."),
        ("How many wipes are in this pack?", "Box of 12 individually wrapped wipes."),
        ("How do I use them correctly?", "Slip wipe onto index finger, wipe tooth surfaces and gums, and discard after use."),
        ("Are they 100% sugar-free and paraben-free?", "Yes, 100% sugar-free, paraben-free, and safe on tooth enamel."),
        ("Where are Teeth Wipes manufactured?", "Manufactured to international oral care quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original."),
        ("What flavor do Teeth Wipes have?", "Fresh natural gentle mint flavor."),
        ("Are they individually wrapped and portable?", "Yes, each wipe is individually wrapped for pocket and handbag convenience."),
        ("Is the 12 wipe pack great for work and travel?", "Yes, sleek compact pack ideal for work, travel, and meetings."),
        ("How should I store them?", "In a cool, dry place."),
        ("Are they recommended after coffee and tea?", "Yes, excellent for instantly wiping away coffee and tea stains post-drinking."),
        ("How many times daily?", "As needed post-meals and colored drinks."),
        ("Do they require water rinsing after use?", "No water rinsing required."),
        ("Is the packaging recyclable?", "Yes."),
        ("Are they safe for sensitive teeth and gums?", "Yes, soft fabric safe on sensitive teeth and gums."),
        ("Do they deliver instant breath confidence?", "Yes, provide fresh minty breath and full confidence."),
        ("Are they available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Are they suitable for men and women?", "Yes, suitable for both men and women."),
        ("Are they great for office workers?", "Yes, an ideal essential for office, meetings, and travel."),
        ("Do they prevent plaque buildup?", "Yes, wiping teeth prevents plaque from hardening on enamel."),
        ("Are they an innovative skincare gift?", "Yes, an innovative practical personal care gift."),
        ("Do they leave tooth surfaces smooth?", "Yes, cleanses teeth leaving surfaces touchably smooth."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2068",
        "sku": "EK-2068",
        "gtin": "6287011270286",
        "brand": "Teeth Care Wipes",
        "ar": {
            "title": "مناديل تنظيف الاسنان  12منديل",
            "meta_title": "مناديل تنظيف الأسنان والأنفاس 12 منديل | إكليل أبها",
            "meta_description": "اشتري مناديل تنظيف الأسنان (12 منديل). مناديل أصبع ابتكارية بالنعناع لإزالة بقع القهوة وإنعاش الأنفاس بدون ماء. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["مناديل_الأسنان", "تنظيف_الأسنان_بدون_ماء", "إزالة_بقع_القهوة", "إنعاش_الأنفاس", "إكليل_أبها"]
        },
        "en": {
            "title": "Teeth Cleaning Wipes - 12 Wipes",
            "meta_title": "Teeth Cleaning Wipes 12 Wipes | Ekleel Abha",
            "meta_description": "Buy original Teeth Cleaning Wipes (12 Wipes). Innovative waterless mint finger wipes for coffee stain removal and fresh breath. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["teeth_cleaning_wipes", "waterless_teeth_wipes", "mint_breath_wipes", "teeth_wipes", "ekleel_abha"]
        }
    }


def _make_neutrogena_hb_b70(pid, gtin, ar_name, en_name, skin_type_ar, skin_type_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> كريم جل الترطيب الطبي الفاخر الأكثر مبيعاً من نيتروجينا (Neutrogena) المصمم خصيصاً لترطيب، إنعاش، وتغذية بشرة الوجه {skin_type_ar} دون تسبيب أي انسداد للمسام أو ثقل دهني. يرتكز هذا الجل الأصيل ({en_name}) على حمض الهيالورونيك النقي (Hyaluronic Acid)، خلاصات الزيتون المطرية، وتقنية Matrix المبتكرة لترطيب ممتد لـ 24 ساعة.</p>
<p>يعمل كريم جل نيتروجينا هيدرو بوست على حابس رطوبة الوجه لـ 24 ساعة، إطفاء عطش الخلايا، وتهدئة الجفاف والخشونة، ليترك بشرة وجهك ناعمة كالحرير، مرطبة عمقاً، مشدودة بالشباب، ومفعمة بالانتعاش من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب عميق وحبس الماء لـ 24 ساعة بحمض الهيالورونيك:</strong> يجذب 1000 ضعف وزنه من الماء لعمق الوجه.</li>
  <li><strong>ملمس جل كريمي خفيف ينفذ فورياً دون زيوت:</strong> مناسب للبشرة {skin_type_ar}.</li>
  <li><strong>إعادة النضارة والتوهج والنعومة الحريرية للوجه:</strong> يزيل الجفاف والشد والتقشر.</li>
  <li><strong>خالٍ 100% من العطور، الزيوت، والكحول:</strong> لا يسبب انسداد المسام (Non-Comedogenic).</li>
  <li><strong>مختبر درماتولوجياً ومناسب للبشرة الحساسة:</strong> قوام جل كالعصارة المائية.</li>
  <li><strong>عبوة أنيقة سعة 50 مل:</strong> حجم ممتاز للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسبة من كريم جل نيتروجينا على بشرة الوجه والرقبة النظيفة.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي برفق بحركات دائرية صاعدة حتى الامتصاص الكامل (يُستعمل مرتين يومياً صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>حمض الهيالورونيك النقي (Purified Hyaluronic Acid):</strong> يعمل كسفنجة مائية تحبس الترطيب داخل خلايا البشرة.</li>
  <li><strong>المكونات المائية المرطبة وخلاصة الزيتون:</strong> تقويان حاجز الوجه الوقائي وتمنعان الجفاف.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والرقبة.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يملك بشرة {skin_type_ar} ويبحث عن كريم جل نيتروجينا هيدرو بوست 50 مل للترطيب والانتعاش.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>نيتروجينا (Neutrogena Hydro Boost)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات نيتروجينا هيدرو بوست المرطبة 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>كريم جل طبي مرطب بحمض الهيالورونيك للبشرة {skin_type_ar} (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة {skin_type_ar} (خصيصاً الفاقدة للترطيب)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، مرطب 24 ساعة، مفعم بالنضارة وغير لامع بالدهون</td></tr>
  <tr><th>الملمس</th><td>جل كريمي خفيف ينفذ فورياً كالماء</td></tr>
  <tr><th>العطر</th><td>خالٍ من العطور / عطر مائي ناعم منعش</td></tr>
  <tr><th>المكونات النشطة</th><td>حمض الهيالورونيك النقي، جليسرين، خلاصة الزيتون</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا / الولايات المتحدة (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Johnson & Johnson Consumer Inc.</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد حمض الهيالورونيك في كريم نيوتريجينا (Neutrogena Hydro Boost)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم جل نيتروجينا هيدرو بوست مشكلة عطش وجفاف الوجه، فقدان التوهج، والخطوط الناجمة عن نقص الترطيب.</p>

<h3>لماذا تنجح تركيبة Neutrogena Hydro Boost?</h3>
<p>لأن حمض الهيالورونيك يجذب جزيئات الماء ويعيد بناء مخزون الترطيب الداخلي دون تسبيب أي طبقة دهنية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على بشرة وجه رطبة:</strong> يضاعف قدرة الهيالورونيك على حبس الماء.<br>
2. <strong>الاستخدام مرتين يومياً (صباحاً ومساءً):</strong> يضمن ترطيباً متواصلاً طوال 24 ساعة.<br>
3. <strong>الاستخدام كقاعدة لمكياج ناعم:</strong> يمنح المكياج انسيابية ومظهراً ناعماً.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات الجل لا تمنح ترطيباً كافياً للبشرة."<br>
<strong>الحقيقة:</strong> كريم جل نيتروجينا يمنح ترطيباً مكثفاً يعادل الكريمات الثقيلة دون أي دهنية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تحتجز جزيئات الهيالورونيك الماء داخل الخلايا القرنية مصلحة حاجز الوجه الوقائي.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو كريم جل مرطب طبي بحمض الهيالورونيك من نيتروجينا للبشرة {skin_type_ar} (50 مل)."),
        ("ما هي فوائد حمض الهيالورونيك للبشرة؟", "يجذب 1000 ضعف وزنه من الماء، يحبس الترطيب لـ 24 ساعة، ويمنع الشد والجفاف."),
        ("هل يمتص فورياً ويرطب لـ 24 ساعة دون زيوت؟", "نعم، مثبت سريرياً في الامتصاص السريع والترطيب 24 ساعة دون تسبيب انسداد المسام."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة سعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على الوجه والرقبة، دلكي برفق حتى الامتصاص مرتين يومياً."),
        ("هل هو خالٍ من الزيوت والكحول؟", "نعم، 100% خالٍ من الزيوت والكحول ومختبر درماتولوجياً."),
        ("أين صُنع كريم جل نيتروجينا؟", "صُنع بواسطة Johnson & Johnson العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات نيتروجينا لدى إكليل أبها أصلية 100%."),
        (f"هل يناسب البشرة {skin_type_ar}؟", f"نعم، مصمم خصيصاً للبشرة {skin_type_ar}."),
        ("هل يترك البشرة ناعمة ومشرقة دون دهنية؟", "نعم، يمتص فورياً ليترك الوجه ناعماً ومشرقاً دون أي دهنية."),
        ("هل عبوة 50 مل مناسبة للحقيبة والسفر؟", "نعم، عبوة أنيقة مدمجة مثالية للحقيبة والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل نيتروجينا هيدرو بوست الماركة الأولى مرطباً؟", "نعم، Hydro Boost الماركة الأكثر شهرة ومبيعا في الترطيب المائي."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل يناسب الاستخدام تحت المكياج؟", "نعم، قاعدة ممتازة للمكياج بفضل امطصاطه السريع وملمسه الخفيف."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع تشقق وجفاف الوجه؟", "نعم، يزيل الشد والتقشر ويحمي الوجه من الجفاف."),
        ("هل يسبب انسداد المسام؟", "لا، تركيبة خالية من الزيوت وغير مسببة للانسداد (Non-Comedogenic)."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يناسب الصيف والشتاء؟", "نعم، ترطيب طبي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج فاخر وأساسي لكل روتين عناية."),
        ("هل يعيد التوهج والمرونة للوجه؟", "نعم، يعيد النضارة والنعومة الطبيعية للبشرة."),
        ("هل تتوفر منتجات Hydro Boost الأخرى؟", "نعم، تتوفر عائلة Neutrogena Hydro Boost كاملة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic luxury medical hydrating gel-cream from Neutrogena designed to hydrate, refresh, and nourish {skin_type_en} facial skin without clogging pores or leaving oil. Built upon Pure Hyaluronic Acid, olive extracts, and Matrix hydration technology for sustained 24-hour moisture.</p>
<p>Neutrogena Hydro Boost Gel-Cream locks in facial hydration for 24 hours, quenches skin thirst, and calms dryness and roughness, leaving your face touchably silky soft, deeply hydrated, plumped with youth, and refreshed from first touch.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>24-Hour Deep Hydration & Water Locking with Hyaluronic Acid:</strong> Attracts up to 1000x its weight in water to skin.</li>
  <li><strong>Lightweight Gel-Cream Texture Absorbing Instantly:</strong> Ideal for {skin_type_en} facial skin.</li>
  <li><strong>Radiance, Smoothness & Plumpness Restoration:</strong> Eliminates facial dryness and flaking.</li>
  <li><strong>100% Oil-Free, Alcohol-Free & Non-Comedogenic:</strong> Will not clog pores or cause breakouts.</li>
  <li><strong>Dermatologically Tested Safe Formula:</strong> Water-gel texture refreshing to sensitive skin.</li>
  <li><strong>Compact 50ml Jar Container:</strong> Excellent size for daily care and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of Neutrogena gel-cream onto clean face and neck.</li>
  <li><strong>Step 2:</strong> Massage gently in smooth upward circular motions until fully absorbed (use twice daily morning & night).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Purified Hyaluronic Acid:</strong> Acts as a hydra-sponge drawing moisture into skin cells.</li>
  <li><strong>Botanical Olive Extract & Hydrating Agents:</strong> Reinforce facial skin barriers preventing moisture loss.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and neck skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with {skin_type_en} skin seeking Neutrogena Hydro Boost 50ml for hydration and freshness.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Neutrogena (Hydro Boost)</td></tr>
  <tr><th>Category</th><td>Skincare / Neutrogena Hydro Boost Gel-Creams 50ml</td></tr>
  <tr><th>Product Type</th><td>Hyaluronic Acid Hydrating Medical Gel-Cream for {skin_type_en} (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>{skin_type_en} Facial Skin</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, plumped & non-greasy clear face</td></tr>
  <tr><th>Texture</th><td>Ultra-lightweight fast-absorbing smooth gel-cream</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-free / Fresh gentle water scent</td></tr>
  <tr><th>Active Ingredients</th><td>Purified Hyaluronic Acid, Glycerin, Olive Extract</td></tr>
  <tr><th>Country of Origin</th><td>France / USA</td></tr>
  <tr><th>Manufacturer</th><td>Johnson & Johnson Consumer Inc.</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Purified Hyaluronic Acid Matrix Water Retention</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves facial skin thirst, dryness, loss of radiance, and fine dehydration lines.</p>

<h3>Why choose Neutrogena Hydro Boost?</h3>
<p>Hyaluronic acid binds water molecules deep within stratum corneum layers restoring moisture reserves without oil.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a medical hyaluronic acid hydrating gel-cream from Neutrogena for {skin_type_en} skin (50ml)."),
        ("What are the benefits of Hyaluronic Acid for skin?", "Attracts 1000x its weight in water, locks in 24-hour hydration, and prevents tightness and dryness."),
        ("Does it absorb instantly and hydrate for 24 hours without oil?", "Yes, clinically proven to absorb rapidly and hydrate for 24 hours without clogging pores."),
        ("What volume is contained in this jar?", "50ml compact jar."),
        ("How do I use it correctly?", "Apply to face and neck, massage gently until absorbed twice daily."),
        ("Is it oil-free and alcohol-free?", "Yes, 100% oil-free, alcohol-free, and dermatologically tested."),
        ("Where is Neutrogena Gel-Cream manufactured?", "By Johnson & Johnson Consumer Inc."),
        ("How do I verify authenticity at Ekleel Abha?", "All Neutrogena products at Ekleel Abha are 100% original."),
        (f"Is it suitable for {skin_type_en} skin?", f"Yes, specifically formulated for {skin_type_en} facial skin."),
        ("Does it leave face soft and radiant without oil?", "Yes, absorbs instantly leaving face soft and radiant without greasy shine."),
        ("Is the 50ml jar handbag and travel friendly?", "Yes, sleek compact jar ideal for handbag and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Neutrogena Hydro Boost a #1 hydration brand?", "Yes, Hydro Boost is the world's most famous #1 brand in water gel hydration."),
        ("How many times daily?", "Twice daily (morning and night)."),
        ("Does it serve as a good makeup base?", "Yes, excellent lightweight makeup base due to rapid absorption."),
        ("Is the container recyclable?", "Yes."),
        ("Does it prevent skin cracking and tightness?", "Yes, eliminates tightness and flaking protecting facial skin."),
        ("Does it clog pores?", "No, oil-free non-comedogenic formula."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it good for all seasons?", "Yes, ideal hydration for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, a premier medical essential for facial care routines."),
        ("Does it restore healthy smooth skin radiance?", "Yes, gives facial skin a healthy smooth radiant look."),
        ("Are other Hydro Boost products available?", "Yes, the full Neutrogena Hydro Boost range is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Neutrogena",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. كريم جل طبي هيدرو بوست بحمض الهيالورونيك من نيتروجينا للبشرة {skin_type_ar}. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Neutrogena Hydro Boost hyaluronic acid hydrating gel-cream for {skin_type_en} skin. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2069():
    return _make_neutrogena_hb_b70(
        pid=2069, gtin="3574661287256",
        ar_name="كريم جل مرطب هيدرو بوست للبشرة الجافة من نيوتريجينا 50 مل",
        en_name="Neutrogena Hydro Boost Moisturizing Gel Cream for Dry Skin - 50ml",
        skin_type_ar="الجافة والشديدة الجفاف", skin_type_en="Dry to Extra Dry",
        feature_ar="كريم جل ترطيب مكثف خالي من العطور للبشرة الجافة 50 مل", feature_en="fragrance-free intensive moisturizing gel-cream for dry skin 50ml",
        tags_ar=["نيتروجينا", "هيدرو_بوست_البشرة_الجافة", "كريم_جل_نيتروجينا", "ترطيب_البشرة_الجافة", "إكليل_أبها"],
        tags_en=["neutrogena", "hydro_boost_dry_skin", "neutrogena_gel_cream", "hyaluronic_acid_gel", "ekleel_abha"]
    )


def create_product_2070():
    return _make_neutrogena_hb_b70(
        pid=2070, gtin="3574661287201",
        ar_name="كريم جل مرطب هيدرو بوست للبشرة العادية والمختلطة من نيوتريجينا 50 مل",
        en_name="Neutrogena Hydro Boost Moisturizing Gel Cream Normal and Combination Skin 50ml",
        skin_type_ar="العادية والمختلطة", skin_type_en="Normal and Combination",
        feature_ar="كريم جل ترطيب منشط خفيف للبشرة العادية والمختلطة 50 مل", feature_en="refreshing lightweight moisturizing gel-cream for normal/combination skin 50ml",
        tags_ar=["نيتروجينا", "هيدرو_بوست_العادية_المختلطة", "نيتروجينا_جل_ترطيب", "ترطيب_مائي_خفيف", "إكليل_أبها"],
        tags_en=["neutrogena", "hydro_boost_normal_combination", "water_gel_neutrogena", "lightweight_moisturizer", "ekleel_abha"]
    )


print("Loaded all 5 Batch 70 builders complete")
