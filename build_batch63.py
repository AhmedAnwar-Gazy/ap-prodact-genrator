import json, os

def create_product_2028():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>شامبو للاطفال بدون رائحة من كيوفي 200جم (QV Baby Fragrance-Free Shampoo 200g)</strong> الشامبو الطبي الفاخر والألطف المخصص لرعاية وشعر الأطفال والرضع من كيو في الأسترالية المصمم لتنظيف شعر وفروة رأس الطفل الحساسة دون أي حرقان في العينين أو جفاف. يرتكز هذا الشامبو الأصيل (QV Baby Shampoo 200g) على الجليسرين المرطب، المكونات المنظفة الخالية من الصابون، والتركيبة الخالية 100% من العطور والدموع.</p>
<p>يعمل شامبو كيوفي للأطفال على تنظيف فروة رأس الطفل وشعره بلطف فائق، إزالة القشور والجفاف دون تهيج، وحفظ رطوبة الشعر الطبيعية، ليترك شعر طفلك ناعماً كالحرير، صحياً، سهلاً في التمشيط، ومحمياً من الحساسية من اليوم الأول للاستخدام.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف لطيف للغاية خالٍ من الدموع (No-Tears Formula):</strong> ينظف فروة رأس الطفل دون حرقان في العينين.</li>
  <li><strong>خالٍ 100% من العطور، الصبغات، الصابون، والبروبيلين جليكول:</strong> آمن ومخصص لبشرة الأطفال الأكثر حساسية.</li>
  <li><strong>ترطيب وتغدية لشعر وفروة الرأس بالجليسرين:</strong> يحفظ ليونة ونعومة الشعر ومنع الجفاف.</li>
  <li><strong>مناسب للاستخدام اليومي من حديثي الولادة والرضع والأطفال:</strong> عناية يومية موثوقة.</li>
  <li><strong>اختبر درماتولوجياً وطبياً لرعاية الأطفال:</strong> لا يسبب حساسية أو تهيج.</li>
  <li><strong>أنبوب مدمج سعة 200 جم:</strong> حجم ممتاز للاستخدام العائلي اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي شعر وفروة رأس الطفل بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من شامبو كيوفي ودلكي فروة الرأس والشعر برفق برغوة خفيفة ناعمة.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء الدافئ وجففي شعر الطفل بمنشفة ناعمة (يُستعمل عند الاستحمام).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الجليسرين الطبيعي والمركبات المرطبة:</strong> تحفظ التوازن المائي لفروة رأس الطفل الحساسة.</li>
  <li><strong>منظفات نباتية خالية من الصابون:</strong> تنظف الشعر بلطف دون حرقان العينين أو انتزاع الدهون الطبيعية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على شعر وفروة رأس الأطفال.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل أم تبحث عن شامبو كيوفي للأطفال بدون رائحة 200 جم لتنظيف ورعاية شعر طفلها بآمان ولطف.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كيو في (QV Baby)</td></tr>
  <tr><th>الفئة</th><td>العناية بالأطفال / شامبو كيو في الطبي الخالي من العطور 200g</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو طبي خالي من الدموع والعطور لتنظيف شعر الأطفال والرضع (200g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>200 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع شعر وفروة رأس الأطفال والرضع (خصيصاً الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر طفل ناعم كالحرير، نظيف، غير متهيج وسهل التمشيط</td></tr>
  <tr><th>الملمس</th><td>جل سائل لطيف ينقلب لرغوة ناعمة خفيفة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور الصناعية (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>جليسرين مرطب، منظفات خالية من الصابون (Soap-Free)</td></tr>
  <tr><th>بلد المنشأ</th><td>أستراليا (Australia)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>الفئة العمرية</th><td>حديثو الولادة، الرضع، والأطفال</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الشامبو الخالي من العطور والصابون لرعاية شعر الرضع (QV Baby)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج شامبو كيوفي للأطفال مشكلة حرقان العينين أثناء الاستحمام، تهيج وقشرة فروة رأس الطفل الحساسة، والجفاف الناتج عن الشامبوهات المعطرة.</p>

<h3>لماذا تنجح تركيبة QV Baby Fragrance-Free؟</h3>
<p>لأن التركيبة متوازنة الحموضة (pH Balanced) وخالية من المنظفات الكبريتية الصابونية القاسية، مما يحفظ الغشاء الوقائي لجلد الطفل.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام ماء دافئ لطيف أثناء الاستحمام:</strong> يريح الطفل ويمنع انكماش الجلد.<br>
2. <strong>التدليك اللطيف بأطراف الأصابع:</strong> ينشط الدورة الدموية بفروة الرأس دون جرح الحفاض الخارجي.<br>
3. <strong>التكميل بزيت أو مرطب كيو في للأطفال:</strong> يحفظ الترطيب الكامل بعد الاستحمام.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "شامبو الأطفال يجب أن يحتوي على عطور قوية لإعطاء رائحة نظافة."<br>
<strong>الحقيقة:</strong> العطور الصناعية من أكثر مسببات أكزيما وحساسية جلد الأطفال، والتركيبة الخالية من العطور هي الخيار الطبي الآمن 100%.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخفض المنظفات غير الأيونية التوتر السطحي برفق عازلة الشوائب دون التسبب في أكسدة الأغشية المخاطية للعين.</p>"""

    faqs = [
        ("ما هو شامبو للاطفال بدون رائحة من كيوفي 200جم؟", "هو شامبو طبي خالي من العطور والدموع والصابون للأطفال والرضع من كيو في الأسترالية (200 جم)."),
        ("ما هي فوائد التركيبة الخالية من العطور والصابون؟", "تنظف شعر وفروة رأس الطفل بلطف دون حرقان العينين أو تسبيب الجفاف والحساسية."),
        ("هل هو خالي من الدموع وآمن لحديثي الولادة؟", "نعم، مثبت طبياً أنه خالٍ من الدموع وآمن من اليوم الأول لحديثي الولادة."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنبوب سعة 200 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي على شعر دلكي برفق برغوة خفيفة واشطفي بالماء الدافئ عند الاستحمام."),
        ("هل هو خالٍ من العطور والصبغات والبارابين؟", "نعم، 100% خالٍ من العطور، الصبغات، الصابون والبروبيلين جليكول."),
        ("أين صُنع شامبو كيوفي للأطفال؟", "صُنع في أستراليا بواسطة Ego Pharmaceuticals Australia."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كيوفي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب فروة الرأس الحساسة والمعرضة للاكزيما؟", "نعم، ممتاز للبشرة وفروة الرأس الحساسة والمعرضة للاكزيما عند الأطفال."),
        ("هل يترك شعر الطفل ناعماً وسهل التمشيط؟", "نعم، يترك شعر الطفل ناعماً كالحرير وسهلاً في التمشيط."),
        ("هل أنبوب 200 جم يكفي لفترة جيدة؟", "نعم، حجم ممتاز يكفي لعدة أسابيع من الاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كيوفي العلامة الطبية الأولى أسترالياً للأطفال؟", "نعم، QV Baby العلامة رقم 1 الموصى بها طبياً في أستراليا."),
        ("كم مرة يومياً/أسبوعياً؟", "عند استحمام الطفل."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، ينشطف بالماء بسلاسة دون ترك أي ترسبات."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع قبعة اللبن (Cradle Cap)؟", "ساعد على تنظيف فروة رأس الرضيع بلطف وتخفيف القشور."),
        ("هل يترك ملمساً ناعماً؟", "نعم، يغلف شعر الطفل بنعومة حريرية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب جميع الأعمار؟", "نعم، ممتاز للرضع والأطفال وحتى الكبار ذوي البشرة الحساسة."),
        ("هل يصلح هدية ممتازة للمولود الجديد؟", "نعم، منتج طبي فاخر وأساسي لكل أم ومولود جديد."),
        ("هل يمنح تنظيفاً دون جفاف؟", "نعم، يحافظ على الترطيب الداخلي لفروة الرأس والشعر."),
        ("هل يسبب حرقان العينين؟", "لا، تركيبة خالية من الدموع لا تسبب حرقان العينين."),
        ("هل تتوفر منتجات QV Baby الأخرى؟", "نعم، تتوفر عائلة QV Baby كاملة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>QV Baby Fragrance-Free Shampoo 200g</strong> is an authentic luxury gentle medical baby shampoo from QV Australia formulated to cleanse sensitive infant and children's hair and scalp without eye stinging or dryness. Built upon hydrating Glycerin, soap-free cleansing agents, and a 100% fragrance-free tear-free formula.</p>
<p>QV Baby Shampoo gently cleanses your baby's hair and scalp, clears dryness without irritation, and seals in natural moisture, leaving your baby's hair touchably silky soft, healthy, easy to comb, and protected against sensitivity from day one.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Gentle Tear-Free Cleaning (No-Tears Formula):</strong> Cleanses baby's scalp without stinging eyes.</li>
  <li><strong>100% Free from Fragrance, Colors, Soap & Propylene Glycol:</strong> Safe for sensitive baby skin.</li>
  <li><strong>Scalp & Hair Hydration with Glycerin:</strong> Maintains hair softness preventing dryness.</li>
  <li><strong>Suitable for Newborns, Infants & Toddlers:</strong> Reliable daily pediatric hair care.</li>
  <li><strong>Dermatologically & Medically Tested:</strong> Non-allergenic gentle formula.</li>
  <li><strong>Compact 200g Tube Container:</strong> Excellent size for daily family bath routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet baby's hair and scalp with warm water during bath time.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of QV Baby Shampoo and massage gently into a soft light lather.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and dry hair with a soft towel (use during bath time).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Glycerin & Hydrating Compounds:</strong> Preserve water balance for sensitive baby scalps.</li>
  <li><strong>Plant-Based Soap-Free Cleansers:</strong> Cleanse hair softly without stinging eyes or stripping natural oils.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hair and scalp application on children.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every mother seeking QV Baby Fragrance-Free Shampoo 200g for safe gentle baby hair cleansing.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>QV Baby</td></tr>
  <tr><th>Category</th><td>Baby Care / QV Medical Fragrance-Free Baby Shampoos 200g</td></tr>
  <tr><th>Product Type</th><td>Medical Fragrance-Free Tear-Free Soap-Free Baby Shampoo (200g)</td></tr>
  <tr><th>Volume/Weight</th><td>200 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Baby & Infant Hair and Scalp Types (Specifically Sensitive)</td></tr>
  <tr><th>Finish</th><td>Silky soft baby hair, clean, unirritated & easy to comb</td></tr>
  <tr><th>Texture</th><td>Gentle clear liquid gel forming a light soft lather</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>Hydrating Glycerin, Soap-Free Cleansers</td></tr>
  <tr><th>Country of Origin</th><td>Australia</td></tr>
  <tr><th>Manufacturer</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>Age Group</th><td>Newborns, Infants & Children</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Soap-Free Fragrance-Free Scalp Cleansing for Infants (QV Baby)</h2>

<h3>What problem does this solve?</h3>
<p>QV Baby Shampoo resolves eye stinging during bath time, sensitive infant scalp irritation and flaking, and dryness from perfumed shampoos.</p>

<h3>Why choose QV Baby Fragrance-Free?</h3>
<p>The pH-balanced formula is free from harsh sulfate soaps, maintaining the protective barrier of infant skin.</p>"""

    en_faqs = [
        ("What is QV Baby Fragrance-Free Shampoo 200g?", "It is an Australian medical fragrance-free tear-free baby shampoo for infants and toddlers (200g)."),
        ("What are the benefits of fragrance-free and soap-free formula?", "Cleanses baby hair and scalp gently without eye stinging or causing dryness and allergies."),
        ("Is it tear-free and safe for newborns?", "Yes, medically proven tear-free and safe from day one for newborns."),
        ("What volume is contained in this tube?", "200g tube."),
        ("How do I use it correctly?", "Apply to wet hair, massage gently into a light lather and rinse with warm water during bath time."),
        ("Is it free from fragrance, colors, and parabens?", "Yes, 100% free from fragrance, colors, soap, and propylene glycol."),
        ("Where is QV Baby Shampoo manufactured?", "In Australia by Ego Pharmaceuticals Australia."),
        ("How do I verify authenticity at Ekleel Abha?", "All QV products at Ekleel Abha are 100% original."),
        ("Is it suitable for sensitive scalp and eczema-prone skin?", "Yes, excellent for sensitive scalps and eczema-prone baby skin."),
        ("Does it leave baby hair soft and easy to comb?", "Yes, leaves baby hair touchably silky soft and easy to comb."),
        ("Does the 200g tube last long?", "Yes, generous size lasting weeks of daily bath use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is QV Baby Australia's #1 medical baby brand?", "Yes, QV Baby is the #1 medically recommended baby brand in Australia."),
        ("How many times daily/weekly?", "Whenever bathing baby."),
        ("Does it rinse off easily?", "Yes, rinses off smoothly with water leaving zero residue."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it help with cradle cap?", "Helps gently cleanse infant scalp and soften scales."),
        ("Does it leave a soft touch?", "Yes, coats baby hair in silky softness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for all ages?", "Yes, great for infants, toddlers, and sensitive adults."),
        ("Is it a premier newborn baby gift?", "Yes, a premier medical essential for mothers and newborns."),
        ("Does it cleanse without drying?", "Yes, maintains internal moisture balance for scalp and hair."),
        ("Does it cause eye stinging?", "No, tear-free formula will not sting eyes."),
        ("Are other QV Baby products available?", "Yes, the full QV Baby product line is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2028",
        "sku": "EK-2028",
        "gtin": "9314839007330",
        "brand": "QV",
        "ar": {
            "title": "شامبو للاطفال بدون رائحة من كيوفي 200جم",
            "meta_title": "شامبو كيوفي للأطفال بدون رائحة 200جم | إكليل أبها",
            "meta_description": "اشتري شامبو للأطفال بدون رائحة من كيو في (200 جم). شامبو أسترالي طبي خالي من الدموع والعطور والصابون للرضع والأطفال. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كيوفي", "شامبو_كيوفي_اطفال", "شامبو_بدون_دموع", "عناية_الأطفال", "إكليل_أبها"]
        },
        "en": {
            "title": "QV Baby Fragrance-Free Shampoo 200g",
            "meta_title": "QV Baby Fragrance-Free Shampoo 200g | Ekleel Abha",
            "meta_description": "Buy original QV Baby Fragrance-Free Shampoo (200g). Australian medical tear-free soap-free shampoo for infants. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["qv", "qv_baby_shampoo", "fragrance_free_shampoo", "tear_free_shampoo", "ekleel_abha"]
        }
    }


def create_product_2029():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>زيت الخروع النقي من وادي النحل 60مل (Pure castor oil from Wadi Alnahil 60ml)</strong> الزيت الطبيعي النقي 100% المعصور على البارد الفاخر من وادي النحل المصمم خصيصاً لتكثيف، تقوية، وتطويل الشعر والحواجب والرموش والأظافر، بالإضافة لترطيب الجلد الجاف. يرتكز هذا الزيت الأصيل (Wadi Alnahil Pure Castor Oil 60ml) على حمض الريسينوليك (Ricinoleic Acid 85%)، الأحماض الدهنية الأساسية أوميغا-9، وفيتامين E.</p>
<p>يعمل زيت الخروع النقي من وادي النحل على تغذية بصيلات الشعر العميقة وتنشيط الدورة الدموية بالفروة لتسريع النمو وتكثيف الفراغات، تقوية ساق الشعر لمنع التقصف والتساقط، وتغليف الجلد برطوبة حمائية مكثفة، ليترك شعرك وحواجبك وأظافرك قوية، كثيفة، مفعمة بالحيوية واللمعان الطبيعي.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تكثيف وتطويل وتقوية الشعر والحواجب والرموش:</strong> يحفز البصيلات الخاملة وينشط نمو الشعر الكثيف.</li>
  <li><strong>زيت طبيعي نقي 100% معصور على البارد:</strong> خالٍ من الإضافات الكيميائية والمواد الصناعية.</li>
  <li><strong>علاج تقصف وتكسر أطراف الشعر:</strong> يعيد بناء الألياف التالفة ويمنحها مرونة وقوة.</li>
  <li><strong>تقوية الأظافر وترطيب الكعبين والمناطق الجافة:</strong> يعالج تشققات الأظافر والجلد.</li>
  <li><strong>مغذي بغنى حمض الريسينوليك وفيتامين E:</strong> يغمر جذور الشعر بالفيتامينات الأساسية.</li>
  <li><strong>عبوة زجاجية مدمجة سعة 60 مل:</strong> حجم ممتاز للاستخدام الزيتي المكثف والخلطات الطبيعية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (للشعر وفروة الرأس):</strong> دلكي قطرات من زيت الخروع على فروة الرأس والشعر وادعميه بمساج دافئ ساعتين قبل الشطف الشامبو (يُستعمل 2-3 مرات أسبوعياً).</li>
  <li><strong>الخطوة الثانية (للرموش والحواجب والأظافر):</strong> ضعي قطرة على مسكرة نظيفة أو قطنة وامسحي بها الحواجب والأظافر مسائياً قبل النوم.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الخروع النقي المعصور على البارد (100% Pure Cold-Pressed Castor Oil):</strong> يمتلك تركيزاً عالياً من Ricinoleic acid المضاد للميكروبات والمحفز لنمو البصيلات.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي فقط.</li>
  <li>تجنبي دخول الزيت داخل العين مباشرة أثناء دهن الرموش.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن الضوء.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن زيت الخروع النقي من وادي النحل 60 مل لتكثيف وتطويل الشعر والحواجب وتقوية الأظافر.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>وادي النحل (Wadi Alnahil)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر والبشرة / الزيوت الطبيعية النقية 100% من وادي النحل 60ml</td></tr>
  <tr><th>نوع المنتج</th><td>زيت خروع نقي معصور على البارد لتكثيف الشعر والحواجب والرموش (60ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>60 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر والبشرة (خصيصاً الشعر الخفيف، التالف، والحواجب)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر وحواجب كثيفة، قوية، مفعمة بالنمو واللمعان وأظافر مرطبة</td></tr>
  <tr><th>الملمس</th><td>زيت دسم كاثف نقي امتصاصه غني</td></tr>
  <tr><th>العطر</th><td>عطر الزيت الطبيعي الأصيل (خالٍ من المعطرات)</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت خروع نقي 100%، حمض الريسينوليك (Ricinoleic Acid)، فيتامين E</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية (KSA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Wadi Alnahil Trading Co.</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد حمض الريسينوليك في زيت الخروع من وادي النحل (Castor Oil)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج زيت الخروع مشكلة تساقط وفراغات الشعر، ضعف فراغات الحواجب والرموش، تقصف الأطراف، وهشاشة الأظافر.</p>

<h3>لماذا تنجح تركيبة Wadi Alnahil Castor Oil؟</h3>
<p>لأن حمض الريسينوليك (Ricinoleic Acid) ينشط مستقبلا PGE2 في البصيلات، مما يرفع تدفق الدورة الدموية ويحفز نمو الشعر.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>المساج الدافئ لفروة الرأس:</strong> يسرع تغلغل الزيت لعمق الجذور.<br>
2. <strong>خلطه مع زيت أخف (كاللوز أو الجوجوبا):</strong> يسهل توزيعه وشطفه بالماء والشامبو.<br>
3. <strong>الاستمرار 8-12 أسبوعاً:</strong> يضمن ظهور نتائج التكثيف الفعالة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "زيت الخروع يسبب انسداد بصيلات الشعر وسقوطه."<br>
<strong>الحقيقة:</strong> زيت الخروع مطهر طبيعي ومضاد للبكتيريا ينظف الفروة ويحفز النمو عند الشطف الصحيح بالشامبو.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يخترق الزيت الطبقة القرنية لساق الشعر معيداً ربط الكيراتين المكسور ومحفزاً الطور النامي (Anagen Phase).</p>"""

    faqs = [
        ("ما هو زيت الخروع النقي من وادي النحل 60مل؟", "هو زيت طبيعي نقي 100% معصور على البارد من وادي النحل لتكثيف وتطويل الشعر والحواجب وتقوية الأظافر (60 مل)."),
        ("ما هي فوائد حمض الريسينوليك وفيتامين E للشعر؟", "ينشطان الدورة الدموية في الفروة، يحفزان نمو البصيلات الخاملة، ويقويان الشعر والحواجب والرموش."),
        ("هل يكثف الشعر والحواجب والرموش بفاعلية؟", "نعم، مثبت سريرياً وشعبياً في تكثيف وتطويل الشعر والحواجب والرموش."),
        ("ما حجم العبوة؟", "تأتي بعبوة زجاجية سعة 60 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "دلكي قطرات على الفروة والحواجب والأظافر مسائياً أو قبل الشطف بـ ساعتين للشعر 2-3 مرات أسبوعياً."),
        ("هل هو زيت خروع نقي 100% معصور على البارد؟", "نعم، 100% نقي، معصور على البارد وخالٍ من المواد الكيميائية."),
        ("أين صُنع زيت الخروع من وادي النحل؟", "صُنع في المملكة العربية السعودية بواسطة شركة وادي النحل."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات وادي النحل لدى إكليل أبها أصلية 100%."),
        ("هل يصلح للرموش والحواجب؟", "نعم، ممتاز جداً لتكثيف وتغليظ الحواجب والرموش بقطنة بحذر."),
        ("هل يعالج تقصف وتكسر أطراف الشعر؟", "نعم، يعيد بناء الألياف التالفة ويمنع التقصف والتكسر."),
        ("هل 60 مل تكفي لفترة جيدة؟", "نعم، زيت كثيف ونقي تكفي قطراته لعدة أسابيع."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الضوء المباشر."),
        ("هل وادي النحل علامة موثوقة في الزيوت؟", "نعم، Wadi Alnahil العلامة الأولى الموثوقة في السعودية للزيوت الطبيعية."),
        ("كم مرة أسبوعياً؟", "2 إلى 3 مرات أسبوعياً للشعر ويومياً للحواجب والأظافر."),
        ("هل يغسل بسهولة بالشامبو؟", "نعم، عند خلطه أو استخدام الشامبو المناسب يزول بسهولة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يقوي الأظافر المتشققة؟", "نعم، يغذي الأظافر ويقويها ويمنع تكسرها."),
        ("هل ينعم الكعبين والمناطق الجافة؟", "نعم، يمنح مرونة وترطيباً مكثفاً للمناطق الجافة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال لتكثيف الشعر واللحية والحواجب."),
        ("هل يفضل خلطه مع زيت اللوز؟", "نعم، خلطه بزيت اللوز الحلو يسهل التوزيع والمساج."),
        ("هل يساعد في إنبات فراغات الشعر؟", "نعم، يحفز إنبات شعر الفراغات بفاعلية."),
        ("هل يصلح هدية طبيعية ممتازة؟", "نعم، زيت طبيعي أساسي لكل روتين عناية."),
        ("هل يمنح شعراً ناعماً وبراقاً؟", "نعم، يكسو الشعر بلمعان وطراوة صحية."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Pure castor oil from Wadi Alnahil 60ml</strong> is an authentic 100% pure cold-pressed natural oil from Wadi Alnahil engineered to densify, strengthen, and lengthen hair, eyebrows, eyelashes, and nails while deeply moisturizing dry skin. Built upon Ricinoleic Acid (85%), essential Omega-9 fatty acids, and natural Vitamin E.</p>
<p>Wadi Alnahil Pure Castor Oil nourishes deep hair follicles and stimulates scalp microcirculation to accelerate growth and fill hair gaps, strengthens the hair shaft against breakage, and seals skin in intensive protective moisture, leaving your hair, eyebrows, and nails strong, thick, radiant, and healthy.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Hair, Eyebrow & Eyelash Densifying & Lengthening:</strong> Stimulates dormant follicles accelerating hair growth.</li>
  <li><strong>100% Pure Cold-Pressed Natural Oil:</strong> Free from chemical additives and synthetic solvents.</li>
  <li><strong>Repairs Split Ends & Hair Breakage:</strong> Rebuilds damaged hair fibers imparting elasticity and strength.</li>
  <li><strong>Nail Fortification & Dry Skin Moisture Sealing:</strong> Treats cracked nails, heels, and dry patches.</li>
  <li><strong>Rich in Ricinoleic Acid & Vitamin E:</strong> Infuses hair roots with essential restorative nutrients.</li>
  <li><strong>Compact 60ml Glass Bottle:</strong> Excellent size for intensive oil routines and natural blends.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Hair & Scalp):</strong> Massage drops of castor oil onto scalp and hair, leave for 2 hours with warm towel, then shampoo off (use 2-3 times weekly).</li>
  <li><strong>Step 2 (Eyelashes, Eyebrows & Nails):</strong> Apply a drop onto a clean mascara wand or cotton pad and gently sweep over eyebrows and nails nightly before bed.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>100% Pure Cold-Pressed Castor Oil:</strong> Contains high concentrations of antimicrobial follicle-stimulating Ricinoleic Acid.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical skin, hair, eyebrow, and nail application only.</li>
  <li>Avoid direct contact with eyes while applying to eyelashes.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from light.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Wadi Alnahil Pure Castor Oil 60ml for hair, eyebrow, and eyelash growth and nail fortification.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Wadi Alnahil</td></tr>
  <tr><th>Category</th><td>Hair & Skincare / Wadi Alnahil 100% Pure Natural Oils 60ml</td></tr>
  <tr><th>Product Type</th><td>100% Pure Cold-Pressed Castor Oil for Hair & Eyebrow Densifying (60ml)</td></tr>
  <tr><th>Volume/Weight</th><td>60 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair & Skin Types (Specifically Thinning, Damaged Hair & Eyebrows)</td></tr>
  <tr><th>Finish</th><td>Thickened, strong, radiant hair, eyebrows & healthy fortified nails</td></tr>
  <tr><th>Texture</th><td>Rich dense pure natural oil fluid</td></tr>
  <tr><th>Fragrance</th><td>Authentic natural oil scent (Fragrance-free)</td></tr>
  <tr><th>Active Ingredients</th><td>100% Pure Castor Oil, Ricinoleic Acid, Natural Vitamin E</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia (KSA)</td></tr>
  <tr><th>Manufacturer</th><td>Wadi Alnahil Trading Co.</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Ricinoleic Acid PGE2 Activation & Follicular Growth Stimulation</h2>

<h3>What problem does this solve?</h3>
<p>Wadi Alnahil Castor Oil resolves hair thinning, eyebrow and eyelash sparse gaps, split ends, and brittle nails.</p>

<h3>Why choose Wadi Alnahil Castor Oil?</h3>
<p>Ricinoleic acid activates PGE2 receptors in hair follicles enhancing blood flow and initiating hair shaft growth.</p>"""

    en_faqs = [
        ("What is Pure castor oil from Wadi Alnahil 60ml?", "It is a 100% pure cold-pressed natural castor oil from Wadi Alnahil for hair, eyebrow, eyelash, and nail growth (60ml)."),
        ("What are the benefits of Ricinoleic Acid and Vitamin E for hair?", "They stimulate scalp microcirculation, activate dormant follicles, and strengthen hair, eyebrows, and lashes."),
        ("Does it effectively densify hair, eyebrows, and eyelashes?", "Yes, clinically and traditionally proven to densify and lengthen hair, eyebrows, and lashes."),
        ("What volume is contained in this bottle?", "60ml glass bottle."),
        ("How do I use it correctly?", "Massage onto scalp 2 hours before shampooing 2-3 times weekly, or apply on eyebrows and nails nightly."),
        ("Is it 100% pure cold-pressed castor oil?", "Yes, 100% pure, cold-pressed, and free from chemicals."),
        ("Where is Wadi Alnahil Castor Oil manufactured?", "In Saudi Arabia by Wadi Alnahil Trading Co."),
        ("How do I verify authenticity at Ekleel Abha?", "All Wadi Alnahil products at Ekleel Abha are 100% original."),
        ("Is it safe for eyelashes and eyebrows?", "Yes, excellent for thickening eyebrows and eyelashes using a cotton pad cautiously."),
        ("Does it repair split ends and hair breakage?", "Yes, rebuilds damaged hair fibers preventing breakage and split ends."),
        ("Does the 60ml bottle last long?", "Yes, dense pure oil requiring only a few drops per application."),
        ("How should I store it?", "In a cool, dry place away from direct light."),
        ("Is Wadi Alnahil a trusted oil brand in Saudi Arabia?", "Yes, Wadi Alnahil is the #1 trusted brand for pure oils in Saudi Arabia."),
        ("How many times weekly?", "2 to 3 times weekly for hair, daily for eyebrows and nails."),
        ("Does it wash out easily with shampoo?", "Yes, washes out smoothly when diluted with lighter oils or proper shampooing."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it strengthen brittle nails?", "Yes, nourishes and fortifies brittle nails against splitting."),
        ("Does it soften dry heels and patches?", "Yes, delivers intense moisture and flexibility to dry skin patches."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, great for women and men for hair, beard, and eyebrow density."),
        ("Is mixing with sweet almond oil recommended?", "Yes, blending with sweet almond oil facilitates easy application and massaging."),
        ("Does it help regrow hair in sparse spots?", "Yes, effectively stimulates hair regrowth in sparse spots."),
        ("Is it a nice natural skincare gift?", "Yes, an essential natural oil for every beauty routine."),
        ("Does it impart hair shine and softness?", "Yes, coats hair in healthy natural luster and softness."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2029",
        "sku": "EK-2029",
        "gtin": "6281112603561",
        "brand": "Wadi Alnahil",
        "ar": {
            "title": "زيت الخروع النقي من وادي النحل 60مل",
            "meta_title": "زيت الخروع النقي وادي النحل 60مل | إكليل أبها",
            "meta_description": "اشتري زيت الخروع النقي من وادي النحل (60 مل). زيت طبيعي نقي 100% معصور على البارد لتكثيف الشعر والحواجب والرموش. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["وادي_النحل", "زيت_الخروع_وادي_النحل", "تكثيف_الشعر", "العناية_بالحواجب", "إكليل_أبها"]
        },
        "en": {
            "title": "Pure castor oil from Wadi Alnahil 60ml",
            "meta_title": "Wadi Alnahil Pure Castor Oil 60ml | Ekleel Abha",
            "meta_description": "Buy original Pure castor oil from Wadi Alnahil (60ml). 100% Pure cold-pressed oil for hair, eyebrow, and eyelash densifying. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["wadi_alnahil", "castor_oil", "pure_castor_oil", "hair_densifying_oil", "ekleel_abha"]
        }
    }


def _make_cantu_b63(pid, gtin, ar_name, en_name, type_ar, type_en, weight_g, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> مستحضر تصفيف وترميم الشعر الفاخر الأصيل من كانتو العالمية المصمم خصيصاً لتنعيم، تقوية، وتثبيت الخصلات والتجعدات ومنع التكسر والهيشان. يرتكز هذا المستحضر الأصيل ({en_name}) على زبدة الشيا الصافية 100%، خلاصة زيت الخروع المنشطة، والمركبات الملطفة للبشرة والشعر.</p>
<p>يعمل مستحضر كانتو للشعر على ترويض الهيشات، تقوية ساق الشعر من الجذور للأطراف، وتغذية الخصلات وحفظ رطوبتها، ليترك شعرك مصففاً بجمال، مرناً، مفعماً بالنعومة واللمعان البراق طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تقوية وتنعيم مكثف للشعر بزبدة الشيا وزيت الخروع:</strong> يقلل تكسر الشعر ويحفز نموه الكثيف.</li>
  <li><strong>تحديد وتثبيت مرن للتسريحات والكيرلي:</strong> يثبت الخصلات دون تيبس أو قشور بيضاء.</li>
  <li><strong>السيطرة الكاملة على الهيشات والتطاير:</strong> يحمي الشعر من الرطوبة والطقس.</li>
  <li><strong>تركيبة خالية من الكبريتات والسيليكون والبارابين:</strong> آمنة ونظيفة للاستخدام اليومي.</li>
  <li><strong>يمنح الشعر لمعاناً طبيعياً براقاً:</strong> يغلف الخصلات ببريق ناعم صحي.</li>
  <li><strong>عبوة سعة {weight_g} جم:</strong> حجم ممتاز للاستخدام اليومي والعناية المستمرة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> وزعي كمية مناسبة من مستحضر كانتو على شعر رطب أو جاف.</li>
  <li><strong>الخطوة الثانية:</strong> صففي الشعر بالأصابع أو المشط وتدليك الأطراف والفروة لتقوية الشعر والتثبيت (يُستعمل عند التصفيف).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زبدة الشيا الصافية 100% وخلاصة الخروع:</strong> تغذيان ساق الشعر وتمنحان القوة والنعومة الفائقة.</li>
  <li><strong>المركبات النباتية المرطبة:</strong> تحفظ رطوبة الشعر الداخلية وتمنع الجفاف والتقصف.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على الشعر فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لتقوية، تنعيم، وتصفية الشعر والتسريحة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كانتو (Cantu)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / مستحضرات تنعيم وتقوية الشعر من كانتو {weight_g}g</td></tr>
  <tr><th>نوع المنتج</th><td>مستحضر تصفيف وتقوية وتنعيم الشعر بـ زبدة الشيا ({type_ar}) {weight_g}g</td></tr>
  <tr><th>الحجم/الوزن</th><td>{weight_g} جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (الكيرلي، المجعد، التالف، والجاف)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر قوي، ناعم كالحرير، محدد وخالٍ من التكسر والهيشان</td></tr>
  <tr><th>الملمس</th><td>جل/كريم ناعم غني ذو ثبات مرن</td></tr>
  <tr><th>العطر</th><td>عطر جوز الهند وجوز الشيا الاستوائي الفواح</td></tr>
  <tr><th>المكونات النشطة</th><td>زبدة الشيا الصافية، زيت الخروع، بذور الكتان، فيتامينات مغذية</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>PDC Brands USA</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد زبدة الشيا وزيت الخروع في كانتو (Cantu Strengthening)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مستحضر كانتو مشكلة تكسر الشعر، هيشان الخصلات، فقدان القوة واللمعان، والجفاف الشديد.</p>

<h3>لماذا تنجح تركيبة Cantu Strengthening?</h3>
<p>لأن دمج زبدة الشيا الصافية مع زيت الخروع النقي يعزز مرونة روابط الكيراتين ويحمي ألياف الشعر من الإجهاد اليومي.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق المباشر على الأطراف والجذور:</strong> يمنح القوة والتغذية المتكاملة.<br>
2. <strong>التصفيف اللطيف بالأصابع:</strong> يحافظ على استقامة وجمال الخصلات.<br>
3. <strong>الاستمرار في الروتين اليومي:</strong> يعيد بناء الشعر التالف بفاعلية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مستحضرات تقوية الشعر تجعل الخصلات قاسية."<br>
<strong>الحقيقة:</strong> مستحضرات كانتو تمنح القوة المرنة والنعومة دون تيبس أو قسوة في الشعر.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تغلف الليبيدات ساق الشعر مانعة تكسر الروابط الهيدروجينية أثناء التمشيط والتصفيف.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو مستحضر تقوية وتنعيم وتصفيف الشعر من كانتو بحجم {weight_g} جم."),
        ("ما هي فوائد زبدة الشيا وزيت الخروع للشعر؟", "تقويان ساق الشعر، تمنعان التكسر والتقصف، وتمنحان نعومة ولمعاناً براقاً."),
        ("هل يقوي الشعر ويمنع التكسر والهيشان؟", "نعم، مثبت سريرياً في تقوية ألياف الشعر والسيطرة على الهيشان والتكسر."),
        (f"ما وزن العبوة؟", f"{weight_g} جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي على شعر رطب أو جاف، دلكي الأطراف وصففي بالأصابع أو المشط."),
        ("هل هو خالٍ من الكبريتات والسيليكون والبارابين؟", "نعم، 100% خالٍ من الكبريتات، السيليكون، والبارابين."),
        (f"أين صُنع مستحضر كانتو؟", "صُنع في الولايات المتحدة بواسطة PDC Brands USA."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كانتو لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", "عطر جوز الهند وجوز الشيا الاستوائي الفواح."),
        ("هل يناسب جميع أنواع الشعر؟", "نعم، ممتاز للشعر الكيرلي، المجعد، التالف والجاف."),
        (f"هل العبوة {weight_g} جم تكفي لفترة جيدة؟", "نعم، تكفي لعدة أسابيع من الاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كانتو العلامة الأولى عالمياً في تقوية وتصفيف الشعر؟", "نعم، Cantu العلامة العالمية الأكثر شهرة ومبيعا."),
        ("كم مرة يومياً؟", "عند تصفيف الشعر."),
        ("هل يمنح الشعر لمعاناً ونعومة حريرية؟", "نعم، يمنح الشعر لمعاناً طبيعياً ونعومة حريرية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في تحفيز نمو الشعر القوي؟", "نعم، يقوي البصيلات والأطراف لتحفيز النمو الصحي."),
        ("هل يترك ملمساً لزجاً؟", "ينفذ بمرونة دون ترك لزوجة أو تراكمات ثقيلة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يحمي الشعر من الحرارة والطقس؟", "نعم، يغلف الشعر ويحميه من المؤثرات الخارجية."),
        ("هل يصلح هدية ممتازة لمحب العناية بالشعر؟", "نعم، منتج أنيق وعملي جداً."),
        ("هل يعيد المظهر الصحي للشعر التالف؟", "نعم، يعيد الحيوية والقوة للشعر المجهد."),
        ("هل يسهل التصفيف اليومي؟", "نعم، يجعل التمشيط والتصفيف سهلاً وسلساً."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic luxury hair strengthening, smoothing, and styling product from Cantu designed to smooth, reinforce, and hold hair strands while preventing breakage and frizz. Built upon 100% Pure Shea Butter, stimulating Castor Oil extract, and hair conditioning compounds.</p>
<p>Cantu Hair Product tames hair flyaways, reinforces the hair shaft from root to tip, and locks in deep moisture, leaving your hair beautifully styled, flexible, silky soft, and radiant all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intensive Hair Strengthening with Shea Butter & Castor Oil:</strong> Reduces hair breakage and promotes healthy growth.</li>
  <li><strong>Flexible Hold & Styling Definition:</strong> Sets hair styles without stiffness or white flakes.</li>
  <li><strong>Complete Frizz & Flyaway Control:</strong> Shields hair against humidity and adverse weather.</li>
  <li><strong>Sulfate-Free, Silicone-Free & Paraben-Free Formula:</strong> Safe clean formula for daily hair care routines.</li>
  <li><strong>Imparts Natural Luminous Shine:</strong> Coats hair strands in a healthy soft luster.</li>
  <li><strong>Generous {weight_g}g Size:</strong> Excellent volume for daily styling and continuous care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of Cantu product onto damp or dry hair.</li>
  <li><strong>Step 2:</strong> Style with fingers or comb, massaging roots and ends for reinforcement (use whenever styling).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>100% Pure Shea Butter & Castor Oil Extract:</strong> Nourish the hair shaft imparting structural strength and extreme softness.</li>
  <li><strong>Moisturizing Botanical Agents:</strong> Lock in internal hair moisture preventing dryness and split ends.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hair application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for strengthening, smoothing, and defining hair styles.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Cantu</td></tr>
  <tr><th>Category</th><td>Hair Care / Cantu Hair Strengthening & Smoothing Products {weight_g}g</td></tr>
  <tr><th>Product Type</th><td>Hair Strengthening & Smoothing Product with Shea Butter ({type_en}) {weight_g}g</td></tr>
  <tr><th>Volume/Weight</th><td>{weight_g} g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Curly, Coily, Damaged & Dry Hair)</td></tr>
  <tr><th>Finish</th><td>Strong hair, silky smooth, defined & breakage-free styled hair</td></tr>
  <tr><th>Texture</th><td>Rich smooth cream/gel with flexible hold</td></tr>
  <tr><th>Fragrance</th><td>Invigorating tropical coconut and shea butter scent</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Shea Butter, Castor Oil, Flaxseed, Nourishing Vitamins</td></tr>
  <tr><th>Country of Origin</th><td>USA</td></tr>
  <tr><th>Manufacturer</th><td>PDC Brands USA</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Castor Oil & Shea Butter Cuticle Reinforcement</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves hair breakage, frizz, loss of strength and shine, and severe hair dryness.</p>

<h3>Why choose Cantu Strengthening Formula?</h3>
<p>Combining 100% Pure Shea Butter with Castor Oil enhances keratin bond elasticity protecting fibers against mechanical friction.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a hair strengthening and smoothing styling product from Cantu ({weight_g}g)."),
        ("What are the benefits of shea butter and castor oil for hair?", "Reinforce the hair shaft, prevent breakage, and deliver silky softness and shine."),
        ("Does it strengthen hair and control breakage and frizz?", "Yes, clinically proven to reinforce hair fibers and control breakage and frizz."),
        (f"What weight is contained in this container?", f"{weight_g}g."),
        ("How do I use it correctly?", "Apply to damp or dry hair, massage ends, and style with fingers or comb."),
        ("Is it sulfate-free, silicone-free, and paraben-free?", "Yes, 100% free from sulfates, silicones, and parabens."),
        ("Where is Cantu Hair Product manufactured?", "In the USA by PDC Brands USA."),
        ("How do I verify authenticity at Ekleel Abha?", "All Cantu products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", "Invigorating tropical coconut and shea butter fragrance."),
        ("Is it suitable for all hair types?", "Yes, excellent for curly, coily, damaged, and dry hair."),
        (f"Does the {weight_g}g container last long?", "Yes, lasts weeks of regular daily styling."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Cantu a globally leading hair strengthening brand?", "Yes, Cantu is a world-famous brand in hair care."),
        ("How many times daily?", "Whenever styling hair."),
        ("Does it impart shine and silky softness?", "Yes, gives hair natural shine and silky softness."),
        ("Is the container recyclable?", "Yes."),
        ("Does it help promote strong hair growth?", "Yes, reinforces roots and ends promoting healthy growth."),
        ("Does it leave a sticky residue?", "Penetrates flexibly without sticky residue or heavy buildup."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Does it shield hair from weather and heat?", "Yes, coats hair guarding against environmental factors."),
        ("Is it a great gift for hair care lovers?", "Yes, elegant and practical gift for hair care."),
        ("Does it restore healthy appearance to damaged hair?", "Yes, restores vitality and strength to stressed hair."),
        ("Does it make daily styling easy?", "Yes, makes combing and styling smooth and effortless."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Cantu",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. مستحضر تصفيف وتقوية وتنعيم الشعر بزبدة الشيا والزيوت من كانتو. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Cantu shea butter and castor oil hair strengthening and smoothing product. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2030():
    return _make_cantu_b63(
        pid=2030, gtin="810006940756",
        ar_name="جل تنعيم الشعر بخلاصة زيت الخروع من كانتو 113جم",
        en_name="Canto Hair Smoothing Gel with Castor Oil Extract - 113g",
        type_ar="جل تنعيم وتقوية الشعر بخلاصة الخروع", type_en="Castor Oil Hair Smoothing Gel", weight_g=113,
        feature_ar="جل تنعيم مصفف ومقوي للشعر بخلاصة زيت الخروع وزبدة الشيا 113 جم", feature_en="smoothing gel with castor oil and shea butter 113g",
        tags_ar=["كانتو", "جل_تنعيم_كانتو", "زيت_الخروع_كانتو", "تنسيق_الشعر", "إكليل_أبها"],
        tags_en=["cantu", "cantu_smoothing_gel", "castor_oil_gel", "hair_smoothing_gel", "ekleel_abha"]
    )


def create_product_2031():
    return _make_cantu_b63(
        pid=2031, gtin="856017000041",
        ar_name="كريم معالج لنمو وتقوية الشعر بربدة الشيا من كانتو 173جم",
        en_name="Cantu Shea Butter Grow Strong Strengthening Treatment 173g",
        type_ar="كريم معالج لنمو وتقوية الشعر (Grow Strong)", type_en="Grow Strong Strengthening Treatment Cream", weight_g=173,
        feature_ar="كريم معالج مركز لنمو وتقوية الشعر بزبدة الشيا الصافية 173 جم", feature_en="intensive Grow Strong strengthening treatment cream 173g",
        tags_ar=["كانتو", "كانتو_جرو_سترونج", "علاج_نمو_الشعر", "تقوية_الشعر_كانتو", "إكليل_أبها"],
        tags_en=["cantu", "grow_strong", "strengthening_treatment", "cantu_grow_strong", "ekleel_abha"]
    )


def create_product_2032():
    return _make_cantu_b63(
        pid=2032, gtin="817513019845",
        ar_name="جل كريم لتنعيم الشعر ببذور الكتان من كانتو 453جم",
        en_name="Cantu Flaxseed Smoothing Hair Cream Gel 453gm",
        type_ar="جل كريم لتنعيم وتثبيت الشعر ببذور الكتان", type_en="Flaxseed Smoothing Hair Cream Gel", weight_g=453,
        feature_ar="جل كريم ضخم لتنعيم وتصفيف الشعر ببذور الكتان وزبدة الشيا 453 جم", feature_en="jumbo flaxseed smoothing hair cream gel 453g",
        tags_ar=["كانتو", "جل_كريم_كانتو", "بذور_الكتان_كانتو", "تنعيم_الشعر_453جم", "إكليل_أبها"],
        tags_en=["cantu", "flaxseed_gel", "cantu_flaxseed", "smoothing_cream_gel", "ekleel_abha"]
    )


print("Loaded all 5 Batch 63 builders complete")
