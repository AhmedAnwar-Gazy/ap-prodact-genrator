import json, os

def create_product_2116():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>قناع المغناطيس بنترات الذهب من دكتور راشيل - 80 جرام (Dr. Rashel Gold Atoms Magnetic Mask - 80g)</strong> القناع المغناطيسي المذهب الفاخر المجدد للشباب والأيقوني من دكتور راشيل (Dr. Rashel Gold Mask) المصمم خصيصاً لتنقية، تفتيح، وتأطير بشرة الوجه بشحنات مغناطيسية تعمل على سحب الأوساخ والسموم والدهون المترسبة بالمسام بواسطة الحجر المغناطيسي المرفق دون الحاجة للماء. يرتكز هذا القناع الأصيل (Dr. Rashel Magnetic Mask 80g) على جزيئات الذهب الخالص عيار 24 (24K Gold Atoms)، المعادن المغناطيسية، والزيوت المغذية للبشرة.</p>
<p>يعمل قناع الذهب المغناطيسي من دكتور راشيل على إحياء الدورة الدموية، تحفيز إنتاج الكولاجين، والقضاء على البهتان والشيخوخة، ليترك بشرتك ناعمة كالحرير، مرطبة، ناصعة الصفاء، ومفعمة بالبريق والتوهج الذهبي من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنقية مغناطيسية مبتكرة لسحب الشوائب والسموم دون ماء:</strong> يزيل الرواسب بالمغناطيس المرفق.</li>
  <li><strong>تغذية وتجديد نضارة الوجه بجزيئات الذهب 24K:</strong> يحفز الكولاجين ويعيد الشباب.</li>
  <li><strong>تفتيح وتوحيد لون البشرة وإزالة البهتان:</strong> يمنح الوجه بريقاً ذهبياً وجمالاً ناصعاً.</li>
  <li><strong>ترطيب وتنعيم ممتد لـ 24 ساعة بالزيوت الطبيعية:</strong> يترك طبقة مخملية حريرية.</li>
  <li><strong>تركيبة فاخرة ومختبرة درماتولوجياً:</strong> مناسبة لجميع أنواع البشرة.</li>
  <li><strong>عبوة سعة 80 جرام مرفقة بحجر مغناطيسي وغلاف واقٍ:</strong> تجربة عناية بالمنتجعات الفاخرة بالمنزل.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> وزعي طبقة متساوية من قناع الذهب على بشرة الوجه النظيفة مع تجنب منطقة العينين.</li>
  <li><strong>الخطوة الثانية:</strong> اتركي القناع لمدة 10-15 دقيقة على الوجه.</li>
  <li><strong>الخطوة الثالثة:</strong> غلفي الحجر المغناطيسي المرفق بالمنديل البلاستيكي، ومرريه بالقرب من الوجه لسحب القناع والشوائب كلياً دون ماء (يُستعمل 1-2 مرة أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>جزيئات الذهب عيار 24 والمعادن المغناطيسية:</strong> تسحب السموم وتحفز التدفق الدموي للكولاجين.</li>
  <li><strong>الزيوت النباتية الفاخرة والمركبات المرطبة:</strong> تغذي أدمة الوجه وتحفظ مرونتها.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه.</li>
  <li>تجنبي التلامس المباشر مع العينين ولا يغسل بالماء مباشرة بل يسحب بالمغناطيس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن قناع المغناطيس بنترات الذهب من دكتور راشيل 80 جم للتنقية المغناطيسية والتوهج الذهبي.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>دكتور راشيل (Dr. Rashel Beauty)</td></tr>
  <tr><th>الفئة</th><td>العناية بالوجه / أقنعة ومستحضرات الذهب والمغناطيس 80g</td></tr>
  <tr><th>نوع المنتج</th><td>قناع مغناطيسي مذهب بجزيئات الذهب 24K لسحب الشوائب بدون ماء (80g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>80 جم + حجر مغناطيسي</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (خصيصاً الباهتة، المجهدة، والجافة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، ناصع الصفاء، مرطب ومفعم بالتوهج الذهبي الفاخر</td></tr>
  <tr><th>الملمس</th><td>معجون مذهب غني جزيئي ينحسر بالمغناطيس تاركاً زيتاً مرطباً</td></tr>
  <tr><th>العطر</th><td>عطر الذهب والمنتجعات الفاخرة</td></tr>
  <tr><th>المكونات النشطة</th><td>جزيئات الذهب 24K، حديد مغناطيسي مصفى، زيوت نباتية مرطبة</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين / الإمارات (Dubai)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Dr. Rashel Cosmetics Inc.</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 18 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الشحنات المغناطيسية وجزيئات الذهب 24K في قناع دكتور راشيل (Dr. Rashel Gold Mask)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج قناع دكتور راشيل المغناطيسي مشكلة بهتان الوجه، انسداد المسام العميقة، التلوث البيئي، وفقدان النضارة والشباب.</p>

<h3>لماذا تنجح تركيبة Dr. Rashel Gold Atoms Magnetic Mask؟</h3>
<p>لأن مركب الحديد المغناطيسي ينجذب للحجر المغناطيسي ساحباً معه الشوائب والسموم بينما ينفذ الذهب للبشرة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام الغلاف البلاستيكي على المغناطيس:</strong> يسهل تنظيف الحجر المغناطيسي بعد السحب.<br>
2. <strong>عدم غسل الوجه بالماء بعد السحب المغناطيسي:</strong> يترك الزيوت الذهبية لتغذي الوجه طوال الليل.<br>
3. <strong>الاستخدام 1-2 مرة أسبوعياً:</strong> يضمن نضارة وتوهجاً مستمراً.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الأقنعة المغناطيسية تتطلب غسيل بالصابون والماء بعد إزالتها."<br>
<strong>الحقيقة:</strong> قناع دكتور راشيل يسحب بالكامل بالمغناطيس ويترك طبقة زوت مرطبة تدلك بالوجه دون ماء.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تولد الجزيئات المغناطيسية تياراً ميكروياً ينشط الدورة الدموية الكولاجينية بالأدمة المصلحة.</p>"""

    faqs = [
        ("ما هو قناع المغناطيس بنترات الذهب من دكتور راشيل - 80 جرام؟", "هو قناع مغناطيسي مذهب فاخر بجزيئات الذهب 24K لسحب الشوائب والسموم بالحجر المغناطيسي بدون ماء من دكتور راشيل (80 جم)."),
        ("ما هي فوائد جزيئات الذهب 24K والسحب المغناطيسي؟", "تسحب الشوائب والسموم مغناطيسياً، تحفز الكولاجين، تفتح الوجه، وتمنح توهجاً ذهبيًا."),
        ("هل ينقي الوجه ويسحب الشوائب بدون ماء ويمنح توهجاً ذهبياً؟", "نعم، مثبت سريرياً في سحب السموم مغناطيسياً وإكاب الوجه نضارة وتوهجاً ذهبياً."),
        ("ما حجم العبوة ومحتوياتها؟", "تأتي بعبوة أنيقة سعة 80 جم + حجر مغناطيسي مرفق."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي القناع، اتركيه 10-15 دقيقة، غلفي المغناطيس بمنديل ومرريه لسحب القناع كلياً دون ماء."),
        ("هل هو آمن ومختبر درماتولوجياً؟", "نعم، 100% آمن ومختبر درماتولوجياً ومناسب لجميع أنواع البشرة."),
        ("أين صُنع قناع دكتور راشيل المغناطيسي؟", "صُنع بواسطة Dr. Rashel Cosmetics العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات دكتور راشيل لدى إكليل أبها أصلية 100%."),
        ("ما رائحة قناع دكتور راشيل الذهب؟", "عطر الذهب والمنتجعات الفاخرة الزكي."),
        ("هل يناسب جميع أنواع البشرة؟", "نعم، ممتاز للبشرة الباهتة، المجهدة، الجافة، والمختلطة."),
        ("هل عبوة 80 جم تكفي لعدة جلسات؟", "نعم، عبوة أنيقة تكفي لعدة أشهر من الجلسات الأسبوعية."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل دكتور راشيل الماركة الأكثر تفضيلاً في أقنعة الذهب؟", "نعم، Dr. Rashel الماركة الأكثر شهرة وتفضيلاً في أقنعة الذهب الفاخرة."),
        ("كم مرة أسبوعياً؟", "1 إلى 2 مرة أسبوعياً."),
        ("هل يتطلب غسيل بالماء بعد السحب؟", "لا يتطلب غسيل بالماء، يترك السيروم والزيت الذهبي ليدلك بالوجه."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يجدد شباب البشرة ويحارب الشيخوخة؟", "نعم، يحفز إنتاج الكولاجين ويجدد شباب ونضارة الوجه."),
        ("هل يترك ملمس الوجه ناعماً كالحرير؟", "نعم، يترك الوجه في غاية النعومة والترطيب الحريري."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والفتيات؟", "نعم، ممتاز للنساء والفتيات من سن 18 سنة."),
        ("هل يناسب الشتاء والصيف؟", "نعم، عناية وتألق ذهبي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن العناية؟", "نعم، منتج عناية وتألق ذهبي فاخر ومبهر كهدية."),
        ("هل يعيد المظهر الصافي المشرق للوجه؟", "نعم، يمنح الوجه مظهراً ناصع الصفاء والتوهج."),
        ("هل تتوفر منتجات دكتور راشيل الذهب الأخرى؟", "نعم، تتوفر عائلة Dr. Rashel Gold كاملة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Dr. Rashel Gold Atoms Magnetic Mask - 80g</strong> is an authentic luxury rejuvenating magnetic gold face mask from Dr. Rashel (Dr. Rashel Gold Mask) designed to purify, brighten, and frame facial skin using magnetic charges that extract trapped dirt, toxins, and sebum from pores using the included magnetic stone without water. Built upon pure 24K Gold Atoms, magnetic minerals, and skin-nourishing botanical oils.</p>
<p>Dr. Rashel Gold Magnetic Mask revives micro-circulation, boosts collagen synthesis, and banishes skin dullness and aging, leaving your facial skin touchably silky soft, hydrated, spotlessly clean, and radiant with a golden glow from first application.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Innovative Waterless Magnetic Extraction:</strong> Sweeps away impurities using the included magnet.</li>
  <li><strong>Skin Rejuvenation & Nourishment with 24K Gold Atoms:</strong> Stimulates collagen restoring youth.</li>
  <li><strong>Facial Brightening & Dullness Removal:</strong> Imparts a brilliant golden skin radiance.</li>
  <li><strong>24-Hour Extended Hydration with Natural Botanical Oils:</strong> Leaves a touchable silky soft finish.</li>
  <li><strong>Dermatologically Tested Luxury Formulation:</strong> Suitable for all facial skin types.</li>
  <li><strong>Generous 80g Container with Magnetic Stone:</strong> Delivers a spa-like luxury facial experience at home.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply an even layer of gold mask over clean facial skin avoiding eye areas.</li>
  <li><strong>Step 2:</strong> Leave the mask on the face for 10-15 minutes.</li>
  <li><strong>Step 3:</strong> Wrap the included magnetic stone in plastic tissue, hover near face to magnetically extract the mask completely without water (use 1-2 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>24K Gold Atoms & Magnetic Minerals:</strong> Extract impurities and boost micro-circulation for collagen support.</li>
  <li><strong>Botanical Oils & Emollients:</strong> Nourish facial skin layers maintaining elasticity and moisture.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial skin application.</li>
  <li>Avoid direct contact with eyes; do not rinse directly with water, extract with magnet.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Any woman seeking Dr. Rashel Gold Atoms Magnetic Mask 80g for waterless magnetic cleansing and golden skin radiance.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Dr. Rashel Beauty</td></tr>
  <tr><th>Category</th><td>Skincare / Dr. Rashel Gold & Magnetic Masks 80g</td></tr>
  <tr><th>Product Type</th><td>24K Gold Atoms Waterless Magnetic Extraction Face Mask (80g)</td></tr>
  <tr><th>Volume/Weight</th><td>80 g + Magnetic Stone</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Specifically Dull, Stressed & Dry Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, spotlessly clean & golden-glowing face</td></tr>
  <tr><th>Texture</th><td>Rich golden molecular paste extracted magnetically leaving a hydrating oil layer</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh spa gold fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>24K Gold Atoms, Purified Magnetic Iron, Botanical Oils</td></tr>
  <tr><th>Country of Origin</th><td>China / UAE (Dubai)</td></tr>
  <tr><th>Manufacturer</th><td>Dr. Rashel Cosmetics Inc.</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 18+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Magnetic Charge Extraction & 24K Gold Collagen Synthesis</h2>

<h3>What problem does this solve?</h3>
<p>Dr. Rashel Gold Magnetic Mask resolves facial dullness, deep pore impactions, environmental pollution, and loss of skin elasticity.</p>

<h3>Why choose Dr. Rashel Gold Magnetic Mask?</h3>
<p>Magnetic iron particles attract the magnet extracting impurities while 24K gold atoms penetrate to stimulate collagen.</p>"""

    en_faqs = [
        ("What is Dr. Rashel Gold Atoms Magnetic Mask - 80g?", "It is a luxury 24K gold magnetic face mask from Dr. Rashel that extracts impurities waterlessly using an included magnet (80g)."),
        ("What are the benefits of 24K Gold Atoms and magnetic extraction?", "Extract impurities magnetically, boost collagen, brighten skin, and impart a brilliant golden radiance."),
        ("Does it purify facial skin waterlessly and deliver a golden glow?", "Yes, clinically proven to extract impurities magnetically and impart a clear golden skin radiance."),
        ("What volume and contents are included?", "80g sleek tub container + included magnetic stone."),
        ("How do I use it correctly?", "Apply mask, leave 10-15 minutes, wrap magnet in tissue, hover near face to extract completely without water."),
        ("Is it safe and dermatologically tested?", "Yes, 100% safe, dermatologically tested, and suitable for all facial skin types."),
        ("Where is Dr. Rashel Magnetic Mask manufactured?", "By Dr. Rashel Cosmetics."),
        ("How do I verify authenticity at Ekleel Abha?", "All Dr. Rashel products at Ekleel Abha are 100% original."),
        ("What scent does Dr. Rashel Gold Mask have?", "Luxurious fresh spa gold fragrance."),
        ("Is it suitable for all skin types?", "Yes, excellent for dull, stressed, dry, and combination skin."),
        ("Does the 80g jar last for multiple treatments?", "Yes, sleek jar lasts months of regular weekly treatments."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Dr. Rashel a top gold mask brand?", "Yes, Dr. Rashel is the world's most famous brand in luxury gold skincare masks."),
        ("How many times weekly?", "1 to 2 times weekly."),
        ("Does it require water rinsing after extraction?", "No, leaves a rich golden oil layer to be massaged into skin without water."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it help rejuvenate skin and fight aging?", "Yes, boosts collagen synthesis restoring youthful skin vitality."),
        ("Does it leave facial skin touchably silky soft?", "Yes, leaves facial skin silky soft and deeply hydrated."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and teens?", "Yes, suitable for women and teens aged 18+."),
        ("Is it good for all seasons?", "Yes, ideal luxury gold skincare for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, a premier luxury gold gift for skincare routines."),
        ("Does it restore clean radiant skin appearance?", "Yes, gives facial skin a clear healthy radiant look."),
        ("Are other Dr. Rashel Gold products available?", "Yes, the full Dr. Rashel Gold range is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2116",
        "sku": "EK-2116",
        "gtin": "6948996212998",
        "brand": "Dr. Rashel",
        "ar": {
            "title": "قناع المغناطيس بنترات الذهب من دكتور راشيل - 80 جرام",
            "meta_title": "قناع الذهب المغناطيسي من دكتور راشيل 80جم | إكليل أبها",
            "meta_description": "اشتري قناع المغناطيس بنترات الذهب من دكتور راشيل (80 جم). قناع مغناطيسي مذهب بجزيئات الذهب 24K لسحب الشوائب بدون ماء. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["دكتور_راشيل", "قناع_الذهب_المغناطيسي", "قناع_المغناطيس_دكتور_راشيل", "تفتيح_الوجه_بالذهب", "إكليل_أبها"]
        },
        "en": {
            "title": "Dr. Rashel Gold Atoms Magnetic Mask - 80g",
            "meta_title": "Dr. Rashel Gold Atoms Magnetic Mask 80g | Ekleel Abha",
            "meta_description": "Buy original Dr. Rashel Gold Atoms Magnetic Mask (80g). 24K Gold Atoms waterless magnetic extraction face mask. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["dr_rashel", "gold_magnetic_mask", "24k_gold_mask", "magnetic_face_mask", "ekleel_abha"]
        }
    }


def create_product_2117():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>قطرة عرق السوس من كوفكس - 50مل (Kovix Licorice Drops - 50ml)</strong> السيروم الطبي النقي المفتح والمصفي للوجه والندبات الأيقوني من كوفيكس (Kovix / Cofix Care Licorice Drops) المصمم خصيصاً لتفتيح التصبغات، إزالة الكلف والبقع الداكنة، وتوحيد لون بشرة الوجه والجسم بنقاء أسطوري. يرتكز هذا السيروم الأصيل (Kovix Licorice 50ml) على خلاصة عرق السوس الطبيعية المركزة (Licorice Root Extract)، الفلافونويدات المبيضة (Glabridin)، ودرجة حموضة متوازنة للبشرة.</p>
<p>تعمل قطرة عرق السوس من كوفيكس على تثبيط إنزيم التايروسينيز المسبب للتصبغات، القضاء على البقع الداكنة وأثر الشمس، وتوفير نضارة وإشراقة ناصعة، لتترك بشرتك ناعمة كالحرير، مرطبة، موحدة اللون، ومفعمة بالصفاء والتوهج من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وتوحيد لون الوجه والجسم بخلاصة عرق السوس الطبيعية:</strong> يزيل الكلف والتصبغات.</li>
  <li><strong>قوة الغلابريدين (Glabridin) لتثبيط صبغة الميلانين:</strong> يمنع ظهور البقع الداكنة مجدداً.</li>
  <li><strong>يمكن خلطها مع كريمات المرطب واللوشن:</strong> مضاعفة مفعول التفتيح اليومي.</li>
  <li><strong>ترطيب وتنعيم فائق لبشرة الوجه:</strong> ينفذ فورياً دون ترك لزوجة أو دهنية.</li>
  <li><strong>تركيبة آمنة 100% ومختبرة جلدياً:</strong> خالية من الهيدروكينون والمواد الضارة.</li>
  <li><strong>زجاجة قطارة أنيقة سعة 50 مل:</strong> حجم ممتاز للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي 3-5 قطرات من سيروم عرق السوس على بشرة الوجه والجسم النظيفة.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي برفق بحركات دائرية حتى الامتصاص، أو اخلطي القطرات مع كريمك المرطب اليومي.</li>
  <li><strong>الخطوة الثالثة:</strong> يُستعمل مرتين يومياً صباحاً ومساءً (مع اتباع واقي شمس صباحاً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة جذر عرق السوس النقي (Glycyrrhiza Glabra):</strong> غني بمادة الغلابريدين المبيضة والمطهرة.</li>
  <li><strong>المركبات المائية السيرومية:</strong> تنفذ لعمق خلايا الوجه وتحفظ الطراوة الحريرية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين واختبري التحسس قبل الاستخدام.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن الشمس.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن قطرة عرق السوس من كوفيكس 50 مل لتفتيح وتصفية التصبغات والكلف والوجه.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كوفيكس / كوفكس (Kovix / Cofix Care)</td></tr>
  <tr><th>الفئة</th><td>العناية بالوجه / سيروم وقطرات عرق السوس المفتحة 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>سيروم قطرة مركز بخلاصة جذر عرق السوس الطبيعي للتفتيح (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه والجسم (خصيصاً المتصبغة، الداكنة، والمصابة بالملازما)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، موحد اللون، ناصع الصفاء ومفعم بالإشراق خالي من البقع</td></tr>
  <tr><th>الملمس</th><td>سيروم سائل شفاف خفيف يمتص فورياً دون دهنية</td></tr>
  <tr><th>العطر</th><td>عطر عرق السوس الطبيعي الناعم المحايد</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة جذر عرق السوس (Licorice Glabridin)، مرطبات مائية</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية (KSA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Cofix Care Products</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد مادة الغلابريدين في قطرة عرق السوس (Kovix Licorice Drops)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج قطرة عرق السوس من كوفيكس مشكلة الكلف والتصبغات المستعصية، أثار حب الشباب الداكنة، عدم توحد الوجه، والبهتان.</p>

<h3>لماذا تنجح تركيبة Kovix Licorice Drops؟</h3>
<p>لأن مركب Glabridin النقي بعرق السوس يمنع أكسدة إنزيم Tyrosinase مانعاً تكون البقع الداكنة كلياً.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الخلط مع الكريم المرطب:</strong> يضاعف مفعول التفتيح اليومي بأمان كامل.<br>
2. <strong>الاستخدام مرتين يومياً (صباحاً ومساءً):</strong> يضمن تفتيح التصبغات بسرعة.<br>
3. <strong>اتباع واقي شمس صباحاً:</strong> يحمي نتائج تفتيح عرق السوس.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "قطرات عرق السوس تسبب تحسس البشرة والجفاف."<br>
<strong>الحقيقة:</strong> سيروم عرق السوس من كوفيكس مصمم بتركيبة مائية آمنة 100% تهدئ البشرة وتمنع التحسس.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط الفلافونويدات بعرق السوس الإفرازات الصباغية وتلطف التهابات الجلد مظهرة بشرة صافية وموحدة.</p>"""

    faqs = [
        ("ما هي قطرة عرق السوس من كوفكس - 50مل؟", "هي سيروم مصلح ومفتح طبيعي مصفٍ للوجه بخلاصة جذر عرق السوس من كوفيكس (50 مل)."),
        ("ما هي فوائد خلاصة عرق السوس (Glabridin) للبشرة؟", "تفتح التصبغات والكلف، توحد لون الوجه والجسم، وتمنع ظهور البقع الداكنة."),
        ("هل تفتح وتصفي التصبغات والكلف بدون دهنية؟", "نعم، مثبتة سريرياً في تفتيح وتصفية الوجه والتصبغات والامتصاص السريع."),
        ("ما حجم العبوة؟", "تأتي بعبوة قطارة أنيقة سعة 50 مل."),
        ("كيف يُستعمل بالشكل الصحيح؟", "ضعي 3-5 قطرات على الوجه أو اخلطيها مع الكريم المرطب ودلكي مرتين يومياً."),
        ("هل هو خالٍ من الهيدروكينون والمواد الضارة؟", "نعم، 100% خالٍ من الهيدروكينون ومواد التقشير الضارة ومختبر جلدياً."),
        ("أين صُنعت قطرة عرق السوس من كوفيكس؟", "صُنعت في المملكة العربية السعودية بواسطة Cofix Care Products."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كوفيكس لدى إكليل أبها أصلية 100%."),
        ("ما رائحة قطرة عرق السوس؟", "عطر عرق السوس الطبيعي الناعم اللطيف."),
        ("هل يناسب الوجه والجسم والمناطق الداكنة؟", "نعم، ممتاز لتفتيح وتوحيد الوجه والجسم والرقبة والكوعين."),
        ("هل زجاجة القطارة 50 مل مريحة وموفرة؟", "نعم، قطارة دقيقة وموفرة جداً للاستخدام اليومي والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل عرق السوس المكون الأول الموصى به لتفتيح التصبغات؟", "نعم، عرق السوس المكون الطبيعي رقم 1 الأكثر أماناً وشهرة لتفتيح التصبغات."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل يمتص فورياً؟", "نعم، يمتص فورياً تاركاً البشرة ناعمة كالحرير دون دهنية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع تكرار الكلف؟", "نعم، يثبط إنزيم التايروسينيز فيمنع تكرار تكون الكلف والبقع."),
        ("هل يمكن خلطه مع لوشن الجسم؟", "نعم، خلطه مع لوشن الجسم يمنح تفتيحاً كاملاً لبشرة الجسم."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يناسب الشتاء والصيف؟", "نعم، تفتيح طبيعي آمن لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج تفتيح طبيعي فاخر وأساسي لكل روتين عناية."),
        ("هل يعيد المظهر الصافي المشرق للوجه؟", "نعم، يمنح الوجه مظهراً ناصع الصفاء والتوهج."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها."),
        ("هل يفضل استخدام واقي شمس معه صباحاً؟", "نعم، يُفضل اتباع واقي شمس حماية لحفظ نتائج التفتيح.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Kovix Licorice Drops - 50ml</strong> is an authentic luxury natural facial and body brightening serum from Kovix (Cofix Care Licorice Drops) designed to fade hyperpigmentation, eliminate melasma, dark spots, and unify facial skin tone with legendary clarity. Built upon concentrated natural Licorice Root Extract, brightening Glabridin flavonoids, and a skin-balanced formulation.</p>
<p>Kovix Licorice Drops inhibit tyrosinase enzyme activity responsible for dark spot formation, eliminate sun tanning and discoloration, and provide illuminated skin clarity, leaving your face and body touchably silky soft, hydrated, even-toned, and radiant from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Natural Face & Body Whitening with Licorice Root Extract:</strong> Fades melasma and dark spots.</li>
  <li><strong>Glabridin Pigment Inhibition:</strong> Prevents melanin synthesis and dark spot recurrence.</li>
  <li><strong>Mixable with Daily Creams & Lotions:</strong> Multiplies daily skin brightening efficacy.</li>
  <li><strong>Superior Hydration & Fast Absorption:</strong> Penetrates rapidly without greasy or sticky residue.</li>
  <li><strong>100% Safe Hydroquinone-Free Formula:</strong> Dermatologically tested for sensitive skin.</li>
  <li><strong>Sleek 50ml Dropper Bottle:</strong> Ideal size for continuous daily care and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply 3-5 drops of licorice serum onto clean facial or body skin.</li>
  <li><strong>Step 2:</strong> Massage gently in circular motions until absorbed, or mix drops with your daily moisturizer.</li>
  <li><strong>Step 3:</strong> Use twice daily morning and night (follow with sunscreen during daytime).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Licorice Root Extract (Glycyrrhiza Glabra):</strong> Rich in Glabridin whitening and clarifying flavonoids.</li>
  <li><strong>Aqueous Serum Emollients:</strong> Penetrate deep facial skin layers maintaining touchable silky softness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and body skin application.</li>
  <li>Avoid direct contact with eyes; perform a patch test prior to full application.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from sunlight.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Kovix Licorice Drops 50ml for natural hyperpigmentation fading, melasma removal, and skin brightening.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Kovix / Cofix Care</td></tr>
  <tr><th>Category</th><td>Skincare / Kovix Licorice Brightening Serums 50ml</td></tr>
  <tr><th>Product Type</th><td>Concentrated Natural Licorice Root Extract Brightening Serum Drops (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial & Body Skin Types (Specifically Hyperpigmented, Dark & Melasma Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, even-toned & spotlessly clear radiant skin</td></tr>
  <tr><th>Texture</th><td>Ultra-lightweight fast-absorbing clear liquid serum</td></tr>
  <tr><th>Fragrance</th><td>100% Mild natural neutral licorice scent</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Licorice Root Extract (Glabridin), Aqueous Serum Hydrators</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia (KSA)</td></tr>
  <tr><th>Manufacturer</th><td>Cofix Care Products</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Licorice Glabridin Tyrosinase Inhibition & Melanogenesis Prevention</h2>

<h3>What problem does this solve?</h3>
<p>Kovix Licorice Drops resolve dark spots, stubborn melasma, post-acne hyperpigmentation, and uneven skin tone.</p>

<h3>Why choose Kovix Licorice Drops?</h3>
<p>Pure Glabridin inhibits tyrosinase enzyme oxidation preventing dark melanin transfer to the skin surface.</p>"""

    en_faqs = [
        ("What is Kovix Licorice Drops - 50ml?", "It is a natural concentrated brightening serum drop from Kovix with Licorice Root Extract for face and body (50ml)."),
        ("What are the benefits of Licorice Root Extract (Glabridin)?", "Fades melasma and hyperpigmentation, evens facial skin tone, and prevents dark spot formation."),
        ("Does it fade dark spots and clarify facial skin without greasiness?", "Yes, clinically proven to fade dark spots and clarify skin tone with rapid non-greasy absorption."),
        ("What volume is contained in this bottle?", "50ml sleek dropper bottle."),
        ("How do I use it correctly?", "Apply 3-5 drops directly or mix with your daily moisturizer twice daily."),
        ("Is it hydroquinone-free and safe?", "Yes, 100% hydroquinone-free, safe, and dermatologically tested."),
        ("Where is Kovix Licorice Drops manufactured?", "In Saudi Arabia by Cofix Care Products."),
        ("How do I verify authenticity at Ekleel Abha?", "All Kovix products at Ekleel Abha are 100% original."),
        ("What scent does Kovix Licorice Drops have?", "Mild natural neutral licorice fragrance."),
        ("Is it suitable for face, body, and dark spots?", "Yes, excellent for face, body, neck, knees, and dark spot treatment."),
        ("Is the 50ml dropper bottle travel friendly?", "Yes, precise dropper bottle ideal for daily care and travel."),
        ("How should I store it?", "In a cool, dry place away from direct light."),
        ("Is Licorice the #1 natural ingredient for hyperpigmentation?", "Yes, Licorice is the world's most trusted natural ingredient for safe skin brightening."),
        ("How many times daily?", "Twice daily (morning and night)."),
        ("Does it absorb instantly?", "Yes, absorbs instantly leaving skin touchably silky soft without greasiness."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it prevent melasma recurrence?", "Yes, inhibits tyrosinase activity preventing melasma recurrence."),
        ("Can it be mixed with body lotions?", "Yes, mixing with body lotions provides comprehensive body skin brightening."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it good for all seasons?", "Yes, ideal natural skin brightening for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, a premier natural essential for skincare routines."),
        ("Does it restore clean radiant skin appearance?", "Yes, gives facial skin a clear healthy radiant look."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy."),
        ("Is following with sunscreen recommended in daytime?", "Yes, follow with a broad-spectrum sunscreen during daytime routines.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2117",
        "sku": "EK-2117",
        "gtin": "697794488291",
        "brand": "Kovix",
        "ar": {
            "title": "قطرة عرق السوس من كوفكس - 50مل",
            "meta_title": "قطرة عرق السوس من كوفيكس لتفتيح الوجه 50مل | إكليل أبها",
            "meta_description": "اشتري قطرة عرق السوس من كوفيكس (50 مل). سيروم طبيعي بـ الغلابريدين لتفتيح الكلف والتصبغات وتوحيد لون البشرة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كوفيكس", "قطرة_عرق_السوس_كوفيكس", "تفتيح_التصبغات_عرق_السوس", "سيروم_عرق_السوس", "إكليل_أبها"]
        },
        "en": {
            "title": "Kovix Licorice Drops - 50ml",
            "meta_title": "Kovix Licorice Drops Brightening 50ml | Ekleel Abha",
            "meta_description": "Buy original Kovix Licorice Drops (50ml). Natural Glabridin concentrated licorice root extract hyperpigmentation & melasma fading serum. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["kovix", "licorice_drops", "licorice_brightening_serum", "glabridin_serum", "ekleel_abha"]
        }
    }


def _make_qv_baby_cream_b79(pid, gtin, ar_title, en_title, weight_str, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_title}</strong> الكريم الطبي المرطب والمغذي الفاخر الأسطوري الأكثر توصية من أطباء الأطفال من كيوفي بيبي (QV Baby) المصمم خصيصاً لترطيب، تغذية، وحماية بشرة الرضع والأطفال الجافة والحساسة والوقاية من الطفح الجلدي والجفاف الشديد والأكزيما. يرتكز هذا الكريم الأصيل ({en_title}) على مجمع السكوالان الطبيعي (Squalane)، الجليسرين المرطب (Glycerin 10%)، البارافين الطبي، والتركيبة الخالية 100% من الصابون والعطور واللانولين.</p>
<p>يعمل كريم كيوفي بيبي على تشكيل درع وقائي يحبس رطوبة جلد الطفل لـ 24 ساعة، الوقاية من طفح الحفاض والطفح الجلدي والتقشر، وإعادة البناء البيولوجي لحاجز البشرة الرقيق، ليترك بشرة طفلك ناعمة كالحرير، مرطبة عمقاً، ناصعة النقاء، ومحمية من الحساسية والجفاف من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتغذية مكثفة لـ 24 ساعة ببشرة الأطفال:</strong> يمنح الرضع نعومة وطراوة فائقة.</li>
  <li><strong>وقاية طبيعية من الطفح الجلدي وطفح الحفاض والجفاف:</strong> بفضل مجمع السكوالان الطبيعي.</li>
  <li><strong>امتصاص فوري دون ترك أثر دهني لزج:</strong> يسهل الارتداء السريع للملابس والحفاضات.</li>
  <li><strong>تركيبة خالية 100% من العطور، اللانولين، والبارابين:</strong> مناسبة لبشرة الرضع والأكزيما.</li>
  <li><strong>موصى به من أطباء الأطفال وأطباء الجلدية:</strong> آمن لحديثي الولادة والأطفال والبالغين.</li>
  <li><strong>عبوة أنيقة سعة {weight_str}:</strong> حجم ممتاز للاستخدام اليومي والحقيبة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسبة من كريم كيوفي بيبي على بشرة الطفل النظيفة والجافة.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي برفق بحركات دائرية ناعمة حتى الامتصاص الكامل (يُستعمل مرتين يومياً وبعد الاستحمام وتغيير الحفاض).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مجمع السكوالان الطبيعي والجليسرين (10%):</strong> يحبسان الرطوبة ويشكلان عازلاً يمنع التعرية والطفح.</li>
  <li><strong>البارافين والزيوت الطبية المطرية:</strong> تحفظان التوازن المائي لجلد الرضع النامي.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الرضع والأطفال.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل أم تبحث عن {ar_title} لحماية طفلها من الطفح والترطيب المكثف.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كيوفي بيبي (QV Baby Ego)</td></tr>
  <tr><th>الفئة</th><td>العناية بالأطفال / كريمات كيوفي بيبي المرطبة {weight_str}</td></tr>
  <tr><th>نوع المنتج</th><td>كريم مرطب طبي خالي من العطور بالسكوالان لبشرة الرضع والأطفال ({weight_str})</td></tr>
  <tr><th>الحجم/الوزن</th><td>{weight_str}</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>بشرة الرضع، حديثي الولادة، والأطفال الجافة، الحساسة والمصابة بالأكزيما والطفح</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة طفل ناعمة كالحرير، مرطبة 24 ساعة ومحمية من الطفح والتقشر</td></tr>
  <tr><th>الملمس</th><td>كريم ناعم غني يمتص فورياً دون لزوجة زلقة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور والصبغات (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>سكوالان طبيعي، جليسرين (10%)، بارافين طبي</td></tr>
  <tr><th>بلد المنشأ</th><td>أستراليا (Australia)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>الفئة العمرية</th><td>حديثو الولادة والأطفال والبالغون (من عمر يوم)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد مجمع السكوالان الطبيعي والجليسرين في كريم كيوفي بيبي (QV Baby Cream)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم كيوفي بيبي مشكلة الطفح الجلدي للرضع، جفاف بشرة الأطفال، الأكزيما، والتقشر الناتج عن الجفاف.</p>

<h3>لماذا تنجح تركيبة QV Baby Moisturising Cream؟</h3>
<p>لأن السكوالان ممركّب مطاطي طبيعي يطابق دهون جلد الطفل فيشكل عازلاً يمنع الطفح ويحبس الترطيب.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق فوراً بعد الاستحمام وتغيير الحفاض:</strong> يحمي بشرة الرضيع من التهيج بالبول.<br>
2. <strong>الاستخدام مرتين يومياً صباحاً ومساءً:</strong> يضمن ترطيباً متواصلاً 24 ساعة.<br>
3. <strong>الاستخدام اللطيف دون فرك شديد:</strong> يحافظ على نعومة واستقرار جلد الطفل.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الكريمات المرطبة للأطفال تسبب انسداد المسام."<br>
<strong>الحقيقة:</strong> كريم كيوفي بيبي خالي 100% من الزيوت الثقيلة وغير مسبب للانسداد مخصص لبشرة الأطفال الحساسة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يتسلل السكوالان والجليسرين بين الخلايا القرنية النامية مصلحين حاجز بشرة حديثي الولادة البيولوجي.</p>"""

    faqs_data = [
        (f"ما هو {ar_title}؟", f"هو كريم مرطب طبي خالي من العطور بالسكوالان من كيوفي بيبي لحماية وترطيب بشرة الرضع والأطفال والوقاية من الطفح ({weight_str})."),
        ("ما هي فوائد السكوالان والجليسرين لجلد الرضع؟", "يحبسان الترطيب لـ 24 ساعة، يمنعان الطفح الجلدي وطفح الحفاض، ويهدئان الأكزيما والجفاف."),
        ("هل يحمي من الطفح الجلدي ويرطب لـ 24 ساعة بدون دهنية؟", "نعم، مثبت سريرياً في حماية بشرة الرضع من الطفح وتوفير ترطيب 24 ساعة."),
        ("ما حجم العبوة؟", f"تأتي بعبوة أنيقة سعة {weight_str}."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على بشرة الطفل، دلكي برفق مرتين يومياً وبعد الاستحمام وتغيير الحفاض."),
        ("هل هو خالٍ من العطور واللانولين والبارابين؟", "نعم، 100% خالٍ من العطور واللانولين والبارابين ومختبر طبياً على بشرة الأطفال."),
        ("أين صُنع كريم كيوفي بيبي؟", "صُنع في أستراليا بواسطة Ego Pharmaceuticals."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كيوفي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب حديثي الولادة والأطفال والبالغين؟", "نعم، ممتاز لحديثي الولادة والأطفال والبالغين ذوي البشرة الحساسة."),
        ("هل يترك بشرة الطفل ناعمة كالحرير؟", "نعم، يمتص فورياً ليترك بشرة الطفل ناعمة كالحرير دون دهنية."),
        (f"هل حجم {weight_str} مناسب للحقيبة والاستخدام اليومي؟", "نعم، حجم ممتاز ومريح جداً للاستخدام اليومي والسفر والحقيبة."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كيوفي بيبي الماركة الأولى الموصى بها من أطباء الأطفال؟", "نعم، QV Baby الماركة رقم 1 الموصى بها طبياً في أستراليا."),
        ("كم مرة يومياً؟", "مرتين يومياً أو حسب الحاجة."),
        ("هل يمنع طفح الحفاض والتهيج؟", "نعم، يشكل عازلاً واقياً يمنع طفح الحفاض والتهيج."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يسبب انسداد المسام؟", "لا، تركيبة خالية من الزيوت الثقيلة وغير مسببة للانسداد (Non-Comedogenic)."),
        ("هل يناسب البشرة المصابة بالأكزيما؟", "نعم، ممتاز لبشرة الرضع والأطفال المصابة بالأكزيما والجفاف الشديد."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الأمهات والمواليد؟", "نعم، ممتاز للأمهات والمواليد."),
        ("هل يناسب الشتاء والصيف؟", "نعم، ترطيب وحماية طبيعية مثالية لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة للمواليد؟", "نعم، منتج طبي فاخر وأساسي لكل روتين عناية بالمواليد."),
        ("هل يعيد المظهر الناعم السلس لبشرة الطفل؟", "نعم، يجعل بشرة الطفل في غاية النعومة والنقاء."),
        ("هل تتوفر منتجات QV Baby الأخرى؟", "نعم، تتوفر عائلة QV Baby كاملة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is the world's most pediatrician-recommended authentic luxury medical baby hydrating cream from QV Baby designed to moisturize, nourish, and protect delicate infant and baby skin while preventing rash, severe dryness, and eczema. Built upon a natural Squalane complex, hydrating Glycerin (10%), medical paraffin, and a 100% fragrance-free, lanolin-free, paraben-free formulation.</p>
<p>QV Baby Moisturizing Cream forms a protective shield locking in infant skin moisture for 24 hours, shielding against diaper rash, skin irritation, and flaking, leaving your baby's skin touchably silky soft, deeply hydrated, spotlessly clean, and protected from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intensive 24-Hour Hydration & Rash Prevention for Infants:</strong> Delivers extreme softness.</li>
  <li><strong>Natural Protection Against Diaper Rash & Dryness:</strong> Powered by natural Squalane complex.</li>
  <li><strong>Fast Absorption with Zero Slippery Residue:</strong> Allows immediate diaper and clothing changes.</li>
  <li><strong>100% Fragrance-Free, Lanolin-Free & Paraben-Free:</strong> Suitable for infant eczema skin.</li>
  <li><strong>Pediatrician & Dermatologist Recommended Medical Brand:</strong> Safe for newborns, infants, and adults.</li>
  <li><strong>Sleek {weight_str} Container:</strong> Ideal format for handbag, travel, and daily care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of QV Baby cream onto clean dry infant skin.</li>
  <li><strong>Step 2:</strong> Massage gently in smooth circular motions until fully absorbed (use twice daily post-bath & diaper change).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Squalane Complex & Glycerin (10%):</strong> Lock in moisture and form a protective barrier preventing diaper rash.</li>
  <li><strong>Medical Paraffin & Softening Emollients:</strong> Maintain skin moisture balance for growing infant skin.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical infant and baby skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Mothers and anyone seeking {en_title} for safe infant skin hydration, rash protection, and softness.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>QV Baby (Ego)</td></tr>
  <tr><th>Category</th><td>Baby Care / QV Baby Moisturizing Creams {weight_str}</td></tr>
  <tr><th>Product Type</th><td>Fragrance-Free Squalane Medical Infant Rash Protection Cream ({weight_str})</td></tr>
  <tr><th>Volume/Weight</th><td>{weight_str}</td></tr>
  <tr><th>Skin/Hair Type</th><td>Newborn, Infant, Sensitive & Eczema-Prone Baby Skin</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, spotlessly clean & rash-protected baby skin</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-slippery hydrating cream</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free & Dye-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Squalane, Glycerin (10%), Medical Paraffin</td></tr>
  <tr><th>Country of Origin</th><td>Australia</td></tr>
  <tr><th>Manufacturer</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>Age Group</th><td>Newborns, Babies & Adults (Ages 0+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Squalane Hydrolipid Protection & Infant Diaper Rash Prevention</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves infant skin rash, diaper irritation, severe dryness, and eczema flaking.</p>

<h3>Why choose QV Baby Moisturizing Cream?</h3>
<p>Natural Squalane mimics natural infant skin lipids forming a protective shield that locks in moisture and prevents urine irritation.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a medical fragrance-free baby moisturizing cream from QV Baby with Squalane for infant rash prevention and hydration ({weight_str})."),
        ("What are the benefits of Squalane and Glycerin for infant skin?", "Lock in 24-hour moisture, prevent skin and diaper rash, and soothe infant eczema."),
        ("Does it protect against rashes and hydrate for 24 hours without greasiness?", "Yes, clinically proven to protect infant skin from rashes and deliver 24-hour hydration."),
        ("What volume is contained in this container?", f"{weight_str} sleek container."),
        ("How do I use it correctly?", "Apply to clean infant skin, massage gently twice daily post-bath and diaper change."),
        ("Is it fragrance-free, lanolin-free, and paraben-free?", "Yes, 100% free from fragrances, lanolin, and parabens, and clinically tested on baby skin."),
        ("Where is QV Baby Cream manufactured?", "In Australia by Ego Pharmaceuticals."),
        ("How do I verify authenticity at Ekleel Abha?", "All QV products at Ekleel Abha are 100% original."),
        ("Is it suitable for newborns, babies, and adults?", "Yes, safe and mild for newborns, babies, and sensitive skin adults."),
        ("Does it leave baby skin touchably silky soft?", "Yes, absorbs instantly leaving baby skin silky soft without greasiness."),
        (f"Is the {weight_str} size convenient for travel and daily care?", "Yes, compact size ideal for handbag, travel, and daily care."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is QV Baby the #1 pediatrician recommended brand in Australia?", "Yes, QV Baby is the #1 pediatrician recommended brand in Australia."),
        ("How many times daily?", "Twice daily or as needed."),
        ("Does it help prevent diaper rash?", "Yes, forms a protective shield preventing diaper rash and urine irritation."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it clog pores?", "No, oil-free non-comedogenic formula."),
        ("Is it suitable for eczema-prone baby skin?", "Yes, excellent for infant eczema and severe skin dryness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for mothers and newborns?", "Yes, suitable for both mothers and newborns."),
        ("Is it good for all seasons?", "Yes, ideal medical protection for summer and winter care."),
        ("Is it a nice baby shower gift?", "Yes, a premier medical essential for baby care routines."),
        ("Does it restore smooth touchable baby skin?", "Yes, gives baby skin a healthy smooth clean look."),
        ("Are other QV Baby products available?", "Yes, the full QV Baby range is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "QV Baby",
        "ar": {
            "title": ar_title,
            "meta_title": f"{ar_title} | إكليل أبها",
            "meta_description": f"اشتري {ar_title}. كريم طبي بالسكوالان والجليسرين لحماية بشرة الرضع من الطفح والترطيب 24 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. Medical Squalane infant rash protection and hydrating cream. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2118():
    return _make_qv_baby_cream_b79(
        pid=2118, gtin="9314839014215",
        ar_title="كريم مرطب للأطفال من كيوفي للوقاية من الطفح الجلدي للرضع 50 جم",
        en_title="QV Baby Moisturizing Cream 50gm",
        weight_str="50 جم",
        tags_ar=["كيوفي_بيبي", "كريم_كيوفي_بيبي_50جم", "وقاية_طفح_الحفاض", "ترطيب_الأطفال", "إكليل_أبها"],
        tags_en=["qv_baby", "qv_baby_cream_50g", "diaper_rash_cream", "infant_moisturizer", "ekleel_abha"]
    )


def create_product_2120():
    return _make_qv_baby_cream_b79(
        pid=2120, gtin="9314839005053",
        ar_title="كريم مرطب للاطفال من كيوفي للجلد الجاف والحساس 100جم",
        en_title="QV Baby Moisturising Cream for Dry and Sensitive Skin - 100g",
        weight_str="100 جم",
        tags_ar=["كيوفي_بيبي", "كريم_كيوفي_بيبي_100جم", "كريم_البشرة_الحساسة_للأطفال", "ترطيب_الرضع", "إكليل_أبها"],
        tags_en=["qv_baby", "qv_baby_cream_100g", "sensitive_baby_cream", "infant_moisturizer", "ekleel_abha"]
    )


def create_product_2119():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول فلير اب من كيوفي 150مل (QV Flare Up Wash 150ml)</strong> السائل المنظف العلاجي الفاخر الأكثر توصية عالمياً من كيوفي (QV / QV Flare Up Wash) المصمم خصيصاً لتنظيف، تطهير، وتهدئة نوبات نكسة الأكزيما الحادة (Eczema Flare-Ups)، التقيحات الجلدية، والبشرة الحساسة للغاية والمصابة بالحكة الشديدة والبكتيريا. يرتكز هذا الغسول الأصيل (QV Flare Up Wash 150ml) على مركب البنزالكونيوم كلورايد المطهر (Benzalkonium Chloride 1.0%)، التريكولسان، والتركيبة الخالية 100% من الصابون والعطور.</p>
<p>يعمل غسول كيوفي فلير اب العلاجي على القضاء على البكتيريا العنقودية والميكروبات المسببة لنكسات الأكزيما، تقليل الحكة الشديدة والتهيج، وتطهير مسام الجلد، ليترك بشرتك ناعمة كالحرير، مطهرة، ناصعة النقاء، ومحمية من مضاعفات الأكزيما من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تطهير علاج نوبات الأكزيما الحادة (Eczema Flare-Ups):</strong> يقضي على البكتيريا المسببة للنكسة.</li>
  <li><strong>تقليل الحكة الشديدة والتقيح والتهيج:</strong> يهدئ البشرة المصابة بالأكزيما فورياً.</li>
  <li><strong>تركيبة خالية 100% من الصابون والعطور والصبغات:</strong> تنظف دون تسبيب أي حرقان أو تهيج.</li>
  <li><strong>درجة حموضة متوازنة (pH Balanced):</strong> تحافظ على الفلورا الجلدية الطبيعية أثناء التطهير.</li>
  <li><strong>موصى به من أطباء الجلدية لعلاج الأكزيما:</strong> آمن للأطفال والبالغين أثناء النكسات.</li>
  <li><strong>زجاجة علاجية سعة 150 مل بمقاس ممتازة:</strong> تكفي لفترة علاج نوبات الأكزيما.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> خففي كمية مناسية من غسول كيوفي فلير اب في ماء الدافئ بالحوض أو الشاور.</li>
  <li><strong>الخطوة الثانية:</strong> اغسلي البشرة المصابة بالنكسة برفق ووزعي الرغوة العلاجية Softly على الجلد.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركي الرغوة 3-5 دقائق ثم اشطفي جيداً بالماء الدافئ وجففي بالطبطبة اللطيفة (يُستعمل أثناء نوبات الأكزيما الحادة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>بنزالكونيوم كلورايد (Benzalkonium Chloride 1.0%):</strong> يقضي على البكتيريا العنقودية الذهبية (Staph) المسببة للتقيح.</li>
  <li><strong>المنظفات العلاجية الخالية من الصابون:</strong> تنظف البشرة المصابة وتمنع الجفاف والتهيج.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي العلاجي الموضعي على بشرة الجسم والوجه المصابة.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من نوبات نكسة الأكزيما الحادة والحكة الشديدة ويبحث عن غسول فلير اب من كيوفي 150 مل للتطهير والتهدئة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كيوفي (QV Ego)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / غسولات ومستحضرات الأكزيما العلاجية من كيوفي 150ml</td></tr>
  <tr><th>نوع المنتج</th><td>سائل غسول طبي مطهر خالي من الصابون لعلاج نوبات الأكزيما الحادة (150ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>150 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة المصابة بالأكزيما الحادة، نكسات Flare-Up، التقيحات والتحسس الشديد</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة مطهرة، هادئة 100%، خالية من الحكة الشديدة والبكتيريا ومستردة للصحة</td></tr>
  <tr><th>الملمس</th><td>سائل مطهر شفاف لطيف ينشطف بالماء بسلاسة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور والصبغات (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>بنزالكونيوم كلورايد 1.0%، منظفات علاجية خالية من الصابون</td></tr>
  <tr><th>بلد المنشأ</th><td>أستراليا (Australia)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد البنزالكونيوم كلورايد 1.0% في غسول كيوفي فلير اب (QV Flare Up Wash)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول كيوفي فلير اب مشكلة نوبات نكسة الأكزيما الحادة (Flare-Ups)، التقيح البكتيري، الحكة الشديدة، والالتهاب المفرط.</p>

<h3>لماذا تنجح تركيبة QV Flare Up Wash 1.0% Benzalkonium Chloride؟</h3>
<p>لأن مركب Benzalkonium Chloride يقضي على استعمار بكتيريا Staph aureus بالجلد المسبب الرئيسي لنكسة الأكزيما.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام أثناء النكسة حتى انحسار الحكة:</strong> يطهر الجلد ويمنع التقيح.<br>
2. <strong>الشطف الجيد بالماء الفاتر:</strong> يضمن إزالة الشوائب والبكتيريا الميتة.<br>
3. <strong>التكميل بـ كريم كيوفي فلير اب المرطب:</strong> يحفظ حاجز الترطيب العلاجي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الغسولات المطهرة للأكزيما تسبب حرقان وشد شديد بالجلد."<br>
<strong>الحقيقة:</strong> غسول كيوفي فلير اب خالي 100% من الصابون ومصمم بحموضة متوازنة تمنع أي حرقان أو جفاف.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يخترق البنزالكونيوم الغشاء البكتيري للبكتيريا العنقودية شالاً نموها ومقللاً التحرير الهيستاميني للحكة.</p>"""

    faqs = [
        ("ما هو غسول فلير اب من كيوفي 150مل؟", "هو سائل غسول طبي مطهر خالي من الصابون والعطور من كيوفي بالبنزالكونيوم كلورايد لعلاج نوبات الأكزيما الحادة (150 مل)."),
        ("ما هي فوائد البنزالكونيوم كلورايد 1.0% لنكسات الأكزيما؟", "يقضي على بكتيريا الأكزيما العنقودية، يقلل الحكة الشديدة والتقيح، ويطهر البشرة المصابة."),
        ("هل يطهر البشرة ويهدئ نوبات الأكزيما الحادة والحكة؟", "نعم، مثبت سريرياً في تطهير بشرة الأكزيما وتقليل الحكة ونكسات Flare-Up."),
        ("ما حجم العبوة؟", "تأتي بزجاجة علاجية أنيقة سعة 150 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "خففي في ماء دافئ، اغسلي البشرة المصابة بالنكسة برفق، اتركيه 3-5 دقائق واشطفي بالماء."),
        ("هل هو خالٍ من الصابون والعطور والصبغات؟", "نعم، 100% خالٍ من الصابون والعطور والصبغات ومختبر طبياً للأكزيما."),
        ("أين صُنع غسول كيوفي فلير اب؟", "صُنع في أستراليا بواسطة Ego Pharmaceuticals."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كيوفي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب الأطفال والبالغين أثناء نكسات الأكزيما؟", "نعم، ممتاز وآمن للأطفال والبالغين أثناء نوبات ونكسات الأكزيما الحادة."),
        ("هل يترك البشرة مطهرة دون حرقان؟", "نعم، ينظف ويطهر دون تسبيب أي حرقان أو تهيج."),
        ("هل زجاجة 150 مل مناسبة لفترة العلاج؟", "نعم، حجم ممتاز تكفي لفترة علاج نوبات الأكزيما."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كيوفي فلير اب العلاج الأول الموصى به للأكزيما؟", "نعم، QV Flare Up العلاج رقم 1 الموصى به طبياً لنكسات الأكزيما في أستراليا."),
        ("كم مرة يُستخدم؟", "مرة إلى مرتين يومياً أثناء نكسات ونوبات الأكزيما الحادة."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، ينشطف بالماء الدافئ بسهولة دون ترك أثر لزج."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يقضي على البكتيريا العنقودية؟", "نعم، يقضي على بكتيريا Staph aureus المسببة لالتهاب وتفاقم الأكزيما."),
        ("هل يفضل اتباع كريم كيوفي فلير اب بعده؟", "نعم، يُفضل استخدام كريم فلير اب العلاجي بعد الغسيل."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للنساء والرجال والأطفال."),
        ("هل يناسب الشتاء والصيف؟", "نعم، تطهير وعلاج طبي لموجات الأكزيما في جميع فصول السنة."),
        ("هل يصلح ضمن روتين الصيدلية المنزلية للأكزيما؟", "نعم، منتج علاجي طبي أساسي للسلامة والصحة الجلدية."),
        ("هل يعيد الهدوء والنقاء للبشرة المصابة؟", "نعم، يجعل البشرة هادئة ومطهرة وخالية من الحكة."),
        ("هل تتوفر منتجات QV Flare Up الأخرى؟", "نعم، تتوفر عائلة QV Flare Up كاملة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>QV Flare Up Wash 150ml</strong> is the world's most dermatologist-recommended authentic luxury medical antibacterial liquid cleanser from QV (QV Flare Up Wash) designed to cleanse, sanitize, and calm severe eczema flare-up episodes, skin suppuration, and ultra-sensitive itch-plagued skin. Built upon Benzalkonium Chloride (1.0%), Triclosan, and a 100% soap-free, fragrance-free formula.</p>
<p>QV Flare Up Medical Wash eliminates staphylococcal bacteria and microbes responsible for eczema aggravation, reduces severe itching and redness, and purifies skin pores, leaving your skin touchably silky soft, sanitized, spotlessly clean, and protected against eczema complications from first application.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Medical Sanitizing Treatment for Severe Eczema Flare-Ups:</strong> Eliminates eczema-aggravating bacteria.</li>
  <li><strong>Severe Itching, Redness & Suppuration Relief:</strong> Instantly soothes inflamed eczema-plagued skin.</li>
  <li><strong>100% Soap-Free, Fragrance-Free & Dye-Free Formula:</strong> Cleanses without causing skin stinging.</li>
  <li><strong>Skin Barrier Protection with Balanced pH (pH 6.0):</strong> Preserves the skin's natural biological flora.</li>
  <li><strong>Dermatologist Recommended Eczema Flare-Up Treatment:</strong> Safe for children and adults during flare-ups.</li>
  <li><strong>Generous 150ml Treatment Bottle:</strong> Sufficient size for full eczema flare-up treatment courses.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Dilute a suitable amount of QV Flare Up Wash in warm bath water or shower.</li>
  <li><strong>Step 2:</strong> Wash flare-up plagued skin gently and spread the therapeutic lather softly over the body.</li>
  <li><strong>Step 3:</strong> Leave lather on skin for 3-5 minutes, then rinse thoroughly with warm water and pat dry (use during acute eczema flare-ups).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Benzalkonium Chloride (1.0%):</strong> Eliminates Staphylococcus aureus bacteria preventing secondary infection.</li>
  <li><strong>Soap-Free Therapeutic Cleansers:</strong> Cleanse affected skin while preventing dryness and stinging.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body and facial skin medical application during flare-ups.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from acute eczema flare-ups and severe itching seeking QV Flare Up Wash 150ml for medical sanitizing.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>QV (Ego)</td></tr>
  <tr><th>Category</th><td>Skincare / QV Medical Eczema Flare-Up Washes 150ml</td></tr>
  <tr><th>Product Type</th><td>Soap-Free Fragrance-Free 1.0% Benzalkonium Chloride Eczema Flare-Up Wash (150ml)</td></tr>
  <tr><th>Volume/Weight</th><td>150 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Acute Eczema Flare-Up, Suppurating, Highly Sensitive & Itch-Plagued Skin</td></tr>
  <tr><th>Finish</th><td>Silky soft, 100% sanitized, itch-relieved & spotlessly clean skin</td></tr>
  <tr><th>Texture</th><td>Clear fast-rinsing therapeutic antibacterial liquid gel</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free & Dye-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>1.0% Benzalkonium Chloride, Soap-Free Cleansers (pH 6.0)</td></tr>
  <tr><th>Country of Origin</th><td>Australia</td></tr>
  <tr><th>Manufacturer</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 3+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 1.0% Benzalkonium Chloride Staphylococcal Eradication & Eczema Relief</h2>

<h3>What problem does this solve?</h3>
<p>QV Flare Up Wash resolves acute eczema flare-up episodes, staphylococcal bacterial infection, severe itching, and skin suppuration.</p>

<h3>Why choose QV Flare Up Wash?</h3>
<p>Benzalkonium Chloride 1.0% eradicates Staphylococcus aureus bacterial colonization stopping secondary infection and histamine release.</p>"""

    en_faqs = [
        ("What is QV Flare Up Wash 150ml?", "It is a medical soap-free antibacterial liquid wash from QV with Benzalkonium Chloride for acute eczema flare-up episodes (150ml)."),
        ("What are the benefits of 1.0% Benzalkonium Chloride?", "Eradicates eczema-aggravating staph bacteria, reduces severe itching and suppuration, and sanitizes inflamed skin."),
        ("Does it sanitize skin and soothe acute eczema flare-ups without stinging?", "Yes, clinically proven to sanitize eczema skin and reduce flare-up itching without stinging."),
        ("What volume is contained in this bottle?", "150ml treatment bottle."),
        ("How do I use it correctly?", "Dilute in warm water, wash affected skin, leave 3-5 minutes and rinse thoroughly during flare-up episodes."),
        ("Is it soap-free, fragrance-free, and dye-free?", "Yes, 100% free from soap, fragrances, and dyes, and clinically tested on eczema skin."),
        ("Where is QV Flare Up Wash manufactured?", "In Australia by Ego Pharmaceuticals."),
        ("How do I verify authenticity at Ekleel Abha?", "All QV products at Ekleel Abha are 100% original."),
        ("Is it safe for children and adults during flare-ups?", "Yes, safe and effective for children and adults during acute eczema flare-ups."),
        ("Does it leave skin sanitized without stinging?", "Yes, sanitizes smoothly leaving skin calm without stinging."),
        ("Is the 150ml bottle sufficient for treatment courses?", "Yes, generous treatment bottle ideal for flare-up care courses."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is QV Flare Up the #1 recommended eczema flare-up treatment in Australia?", "Yes, QV Flare Up is the #1 dermatologist recommended eczema flare-up line in Australia."),
        ("How many times daily?", "Once or twice daily during acute flare-up episodes."),
        ("Does it rinse off easily?", "Yes, rinses off smoothly with warm water without sticky residue."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it eradicate Staphylococcus aureus bacteria?", "Yes, eradicates Staph aureus bacteria preventing secondary infection."),
        ("Is following with a QV Flare Up cream recommended?", "Yes, follow with a QV Flare Up moisturizing cream post-wash."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it good for all seasons?", "Yes, ideal medical flare-up treatment for summer and winter care."),
        ("Is it a home pharmacy essential for eczema?", "Yes, a vital medical essential for family skin health."),
        ("Does it restore calm sanitized skin?", "Yes, gives affected skin a healthy calm sanitized look."),
        ("Are other QV Flare Up products available?", "Yes, the full QV Flare Up medical range is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2119",
        "sku": "EK-2119",
        "gtin": "9314839015373",
        "brand": "QV",
        "ar": {
            "title": "غسول فلير اب من كيوفي 150مل",
            "meta_title": "غسول كيوفي فلير اب للأكزيما الحادة 150مل | إكليل أبها",
            "meta_description": "اشتري غسول فلير اب من كيوفي (150 مل). سائل طبي مطهر خالي من الصابون بالبنزالكونيوم كلورايد لعلاج نوبات نكسة الأكزيما والحكة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كيوفي", "غسول_كيوفي_فلير_اب", "علاج_نكسات_الأكزيما", "كيوفي_فلير_اب_150مل", "إكليل_أبها"]
        },
        "en": {
            "title": "QV Flare Up Wash 150ml",
            "meta_title": "QV Flare Up Wash 150ml | Ekleel Abha",
            "meta_description": "Buy original QV Flare Up Wash (150ml). Soap-free fragrance-free 1.0% Benzalkonium Chloride eczema flare-up antibacterial wash. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["qv", "qv_flare_up_wash", "eczema_flare_up_wash", "antibacterial_eczema_wash", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 79 builders complete")
