import json, os

def create_product_2121():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>لوشن ترطيب بشرة الطفل من كيوفي - 250 مل (QV Baby Moisturising Lotion - 250ml)</strong> اللوشن الطبي المرطب والمغذي الفاخر الأسطوري الأكثر توصية من أطباء الأطفال من كيوفي بيبي (QV Baby) المصمم خصيصاً لترطيب، تغذية، وتهدئة بشرة الرضع والأطفال الجافة والحساسة دون ترك أي طبقة دهنية ثقيلة. يرتكز هذا اللوشن الأصيل (QV Baby Lotion 250ml) على البارافين السائل الطبي (Liquid Paraffin)، الجليسرين المرطب، وخلوه التام 100% من الصابون والعطور واللانولين.</p>
<p>يعمل لوشن كيوفي بيبي الطبي على حبس رطوبة جلد الطفل لـ 24 ساعة، تقليل التقشر والشد والجفاف، وإعادة البناء البيولوجي لحاجز البشرة الرقيق، ليترك بشرة طفلك ناعمة كالحرير، مرطبة، خالية من التهيجات، ومحمية طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتغذية خفيفة لـ 24 ساعة لبشرة الرضع والأطفال:</strong> يمنح الجلد طراوة ونعومة فائقة.</li>
  <li><strong>امتصاص فوري دون ترك أثر دهني لزج:</strong> يسهل ارتداء الملابس والحفاضات فوراً بعد الاستحمام.</li>
  <li><strong>ترميم حاجز بشرة الطفل بالبارافين والجليسرين الطبي:</strong> يمنع تبخر المياه الداخلية.</li>
  <li><strong>تركيبة خالية 100% من العطور، اللانولين، والبارابين:</strong> مناسبة للبشرة المفرطة الحساسية والأكزيما.</li>
  <li><strong>موصى به من أطباء الأطفال وأطباء الجلدية:</strong> آمن لحديثي الولادة والأطفال والبالغين.</li>
  <li><strong>عبوة سعة 250 مل مزودة بضاغط مريح:</strong> حجم ممتاز للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسبة من لوشن كيوفي بيبي على بشرة الطفل النظيفة.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي برفق بحركات دائرية ناعمة حتى الامتصاص الكامل (يُستعمل مرتين يومياً صباحاً ومساءً وبعد الاستحمام).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>البارافين الطبي والجليسرين:</strong> يشكلان عازلاً يحبس الرطوبة ويمنع الجفاف والتقشر.</li>
  <li><strong>المركبات المطرية المائية:</strong> تحفظ النعومة الحريرية لبشرة الطفل دون غلق المسام.</li>
</ul>

<h2>تحذيرات وااحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الرضع والأطفال.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل أم تبحث عن لوشن ترطيب بشرة الطفل من كيوفي 250 مل للترطيب اليومي خفيف الملمس.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كيوفي بيبي (QV Baby Ego)</td></tr>
  <tr><th>الفئة</th><td>العناية بالأطفال / لوشنات كيوفي بيبي الطبية المرطبة 250ml</td></tr>
  <tr><th>نوع المنتج</th><td>لوشن مرطب طبي خالي من العطور واللانولين لبشرة الرضع والأطفال (250ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>250 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>بشرة الرضع، حديثي الولادة، الأطفال الجافة، الحساسة والمصابة بالأكزيما</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة طفل ناعمة كالحرير، مرطبة 24 ساعة، خالية من التقشر والدهنية</td></tr>
  <tr><th>الملمس</th><td>لوشن سائل خفيف يمتص فورياً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور والصبغات (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>بارافين طبي، جليسرين، مركبات ترطيب مائية</td></tr>
  <tr><th>بلد المنشأ</th><td>أستراليا (Australia)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>الفئة العمرية</th><td>حديثو الولادة والأطفال والبالغون (من عمر يوم)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد البارافين الطبي والجليسرين في لوشن كيوفي بيبي (QV Baby Lotion)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج لوشن كيوفي بيبي مشكلة جفاف بشرة الرضع والأطفال، التقشر الصباحي، والتهيج الناتج عن العوامل الجوية.</p>

<h3>لماذا تنجح تركيبة QV Baby Moisturising Lotion؟</h3>
<p>لأن البارافين الطبي الخفيف يشكل درعاً يمنع تبخر الماء بينما يجذب الجليسرين الرطوبة للطبقة القرنية للطفل.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق فوراً بعد الاستحمام على بشرة رطبة:</strong> يضاعف امتصاص المرطب.<br>
2. <strong>الاستخدام مرتين يومياً صباحاً ومساءً:</strong> يضمن ترطيباً متواصلاً 24 ساعة.<br>
3. <strong>التدليك اللطيف دون فرك شديد:</strong> يحافظ على نعومة واستقرار جلد الطفل.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "اللوشنات الخفيفة للأطفال لا تمنح ترطيباً كافياً."<br>
<strong>الحقيقة:</strong> لوشن كيوفي بيبي مدعم بتركيبة طبية تمنح ترطيباً مكثفاً يضاهي الكريمات الثقيلة دون أي لزوجة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتسلل الميكروليبيدات بين الخلايا الجلدية مصلحة الغشاء الهيدروليبيدي الحامي للطفل.</p>"""

    faqs = [
        ("ما هو لوشن ترطيب بشرة الطفل من كيوفي - 250 مل؟", "هو لوشن مرطب طبي خالي من العطور واللانولين من كيوفي بيبي لبشرة الرضع والأطفال الجافة والحساسة (250 مل)."),
        ("ما هي فوائد البارافين الطبي والجليسرين لبشرة الأطفال؟", "يحبسان الترطيب لـ 24 ساعة، يمنعان الجفاف والتقشر، ويهدئان البشرة الحساسة والأكزيما."),
        ("هل يمتص فورياً ويرطب لـ 24 ساعة بدون دهنية؟", "نعم، مثبت سريرياً في الامتصاص السريع والترطيب 24 ساعة دون طبقة دهنية لزجة."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة مزودة بضاغط مريح سعة 250 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية مناسبة على بشرة الطفل، دلكي برفق حتى الامتصاص مرتين يومياً وبعد الاستحمام."),
        ("هل هو خالٍ من العطور واللانولين والبارابين؟", "نعم، 100% خالٍ من العطور واللانولين والبارابين ومختبر طبياً على بشرة الأطفال."),
        ("أين صُنع لوشن كيوفي بيبي؟", "صُنع في أستراليا بواسطة Ego Pharmaceuticals."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كيوفي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب حديثي الولادة والأطفال والبالغين؟", "نعم، ممتاز لحديثي الولادة والأطفال والبالغين ذوي البشرة الحساسة."),
        ("هل يترك بشرة الطفل ناعمة كالحرير؟", "نعم، يمتص فورياً ليترك بشرة الطفل ناعمة كالحرير دون دهنية."),
        ("هل عبوة 250 مل بضاغط مريحة؟", "نعم، عبوة أنيقة بضاغط مريح جداً للاستخدام اليومي والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كيوفي بيبي الماركة الأولى الموصى بها من أطباء الأطفال؟", "نعم، QV Baby الماركة رقم 1 الموصى بها طبياً في أستراليا."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل يناسب الوجه والجسم معاً؟", "نعم، لوشن طبي شامل مخصص لبشرة الوجه والجسم للأطفال."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في الوقاية من جفاف الشتاء للأطفال؟", "نعم، ترطيب وتنعيم طبيعي مثالي لجميع فصول السنة."),
        ("هل يسبب انسداد المسام؟", "لا، تركيبة خالية من الزيوت الثقيلة وغير مسببة للانسداد (Non-Comedogenic)."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب المواليد والأمهات؟", "نعم، ممتاز للمواليد والأمهات."),
        ("هل يناسب الصيف والشتاء؟", "نعم، ترطيب طبي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة للمواليد؟", "نعم، منتج طبي فاخر وأساسي لكل روتين عناية بالمواليد."),
        ("هل يعيد المظهر الناعم السلس لبشرة الطفل؟", "نعم، يجعل بشرة الطفل في غاية النعومة والنقاء."),
        ("هل تتوفر منتجات QV Baby الأخرى؟", "نعم، تتوفر عائلة QV Baby كاملة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>QV Baby Moisturising Lotion - 250ml</strong> is the world's most pediatrician-recommended authentic luxury medical hydrating infant and baby lotion from QV Baby designed to hydrate, nourish, and soothe dry and sensitive baby skin without leaving a heavy greasy film. Built upon liquid medical paraffin, hydrating Glycerin, and a 100% fragrance-free, lanolin-free, paraben-free formula.</p>
<p>QV Baby Medical Lotion locks in infant skin hydration for 24 hours, reduces flaking, tightness, and dryness, and restores the delicate protective skin barrier, leaving your baby's skin touchably silky soft, hydrated, clear of irritation, and protected all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Lightweight 24-Hour Hydration for Baby Skin:</strong> Imparts silky softness and flexibility.</li>
  <li><strong>Instant Absorption with Zero Greasy Residue:</strong> Allows immediate diaper and clothing changes.</li>
  <li><strong>Skin Barrier Restoration with Medical Paraffin & Glycerin:</strong> Prevents transepidermal water loss.</li>
  <li><strong>100% Fragrance-Free, Lanolin-Free & Paraben-Free:</strong> Suitable for ultra-sensitive and infant eczema skin.</li>
  <li><strong>Pediatrician & Dermatologist Recommended Medical Brand:</strong> Safe for newborns, infants, and adults.</li>
  <li><strong>Convenient 250ml Pump Dispenser Bottle:</strong> Ideal format for continuous daily family care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of QV Baby lotion onto clean infant skin.</li>
  <li><strong>Step 2:</strong> Massage gently in smooth circular motions until fully absorbed (use twice daily morning, night & post-bath).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Medical Paraffin & Glycerin:</strong> Form an occlusive barrier locking in moisture and preventing flaking.</li>
  <li><strong>Lightweight Emollient Compounds:</strong> Maintain touchable silky softness without clogging pores.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical infant and baby skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Mothers and anyone seeking QV Baby Moisturising Lotion 250ml for lightweight daily infant skin hydration.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>QV Baby (Ego)</td></tr>
  <tr><th>Category</th><td>Baby Care / QV Baby Moisturizing Lotions 250ml</td></tr>
  <tr><th>Product Type</th><td>Fragrance-Free Lanolin-Free Medical Hydrating Infant Lotion (250ml)</td></tr>
  <tr><th>Volume/Weight</th><td>250 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Newborn, Infant, Sensitive & Eczema-Prone Baby Skin</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, non-greasy & spotlessly clean baby skin</td></tr>
  <tr><th>Texture</th><td>Ultra-lightweight fast-absorbing smooth liquid lotion</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>Medical Paraffin, Glycerin, Aqueous Hydrating Compounds</td></tr>
  <tr><th>Country of Origin</th><td>Australia</td></tr>
  <tr><th>Manufacturer</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>Age Group</th><td>Newborns, Babies & Adults (Ages 0+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Medical Paraffin Occlusion & Infant Skin Hydration</h2>

<h3>What problem does this solve?</h3>
<p>QV Baby Moisturising Lotion resolves infant skin dryness, flaking, tightness, and environmental sensitivity.</p>

<h3>Why choose QV Baby Moisturising Lotion?</h3>
<p>Medical paraffin forms a protective shield preventing transepidermal water loss while glycerin draws moisture into infant skin cells.</p>"""

    en_faqs = [
        ("What is QV Baby Moisturising Lotion - 250ml?", "It is a medical fragrance-free lanolin-free lotion from QV Baby for dry and sensitive infant skin (250ml)."),
        ("What are the benefits of medical paraffin and glycerin for baby skin?", "Lock in 24-hour hydration, prevent flaking and dryness, and soothe sensitive eczema-prone infant skin."),
        ("Does it absorb instantly and hydrate for 24 hours without greasiness?", "Yes, clinically proven to absorb rapidly and hydrate for 24 hours without greasy residue."),
        ("What volume is contained in this bottle?", "250ml pump dispenser bottle."),
        ("How do I use it correctly?", "Apply to clean baby skin, massage gently until absorbed twice daily and post-bath."),
        ("Is it fragrance-free, lanolin-free, and paraben-free?", "Yes, 100% free from fragrances, lanolin, and parabens, and clinically tested on baby skin."),
        ("Where is QV Baby Lotion manufactured?", "In Australia by Ego Pharmaceuticals."),
        ("How do I verify authenticity at Ekleel Abha?", "All QV products at Ekleel Abha are 100% original."),
        ("Is it suitable for newborns, babies, and adults?", "Yes, safe and mild for newborns, babies, and sensitive skin adults."),
        ("Does it leave baby skin touchably silky soft?", "Yes, absorbs instantly leaving baby skin silky soft without greasiness."),
        ("Is the 250ml pump bottle convenient?", "Yes, sleek pump dispenser bottle ideal for daily care and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is QV Baby the #1 pediatrician recommended brand in Australia?", "Yes, QV Baby is the #1 pediatrician recommended brand in Australia."),
        ("How many times daily?", "Twice daily (morning and night)."),
        ("Is it suitable for face and body together?", "Yes, versatile medical moisturizer for facial and body baby skin."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help prevent winter skin dryness for babies?", "Yes, ideal medical hydration for summer and winter care."),
        ("Does it clog pores?", "No, oil-free non-comedogenic formula."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for mothers and newborns?", "Yes, suitable for both mothers and newborns."),
        ("Is it good for all seasons?", "Yes, ideal medical hydration for summer and winter care."),
        ("Is it a nice baby shower gift?", "Yes, a premier medical essential for daily baby skincare routines."),
        ("Does it restore smooth radiant baby skin appearance?", "Yes, gives baby skin a healthy smooth radiant look."),
        ("Are other QV Baby products available?", "Yes, the full QV Baby range is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2121",
        "sku": "EK-2121",
        "gtin": "9314839014222",
        "brand": "QV Baby",
        "ar": {
            "title": "لوشن ترطيب بشرة الطفل من كيوفي - 250 مل",
            "meta_title": "لوشن كيوفي بيبي المرطب للبشرة 250مل | إكليل أبها",
            "meta_description": "اشتري لوشن ترطيب بشرة الطفل من كيوفي (250 مل). لوشن طبي خالي من العطور واللانولين لترطيب وتنعيم بشرة الرضع والأطفال. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كيوفي_بيبي", "لوشن_كيوفي_بيبي", "ترطيب_بشرة_الطفل", "لوشن_الأطفال_الحساسة", "إكليل_أبها"]
        },
        "en": {
            "title": "QV Baby Moisturising Lotion - 250ml",
            "meta_title": "QV Baby Moisturising Lotion 250ml | Ekleel Abha",
            "meta_description": "Buy original QV Baby Moisturising Lotion (250ml). Fragrance-free lanolin-free medical infant skin hydrating lotion. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["qv_baby", "qv_baby_lotion", "infant_moisturizing_lotion", "baby_lotion", "ekleel_abha"]
        }
    }


def create_product_2122():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول اطفال لطيف للبشرة الحساسة من كيوفي - 250 جم (QV Baby Gentle Wash for Sensitive Skin - 250g)</strong> الكريم المنظف الطبي السائل الفاخر الخالي من الصابون الأكثر توصية من أطباء الأطفال من كيوفي بيبي (QV Baby) المصمم خصيصاً لتنظيف، تنقية، وترطيب بشرة الرضع والأطفال الحساسة والجافة جداً دون التسبب في أي حرقان أو تهيج أو تجريد للحجاب الدهني. يرتكز هذا الغسول الأصيل (QV Baby Gentle Wash 250g) على الجليسرين المرطب المكثف (Glycerin 15%)، التركيبة الخالية 100% من الصابون والعطور، ودرجة الحموضة المتوازنة (pH 6.0).</p>
<p>يعمل غسول كيوفي بيبي اللطيف على إزالة الأوساخ والشوائب بسلاسة، حماية الوجه والجسم من الجفاف الشديد والطفح، وإعادة التوازن المائي لجلد الطفل، ليترك بشرة طفلك ناعمة كالحرير، مرطبة، ناصعة النقاء، ومحمية من التهيجات من الغسلة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف سائل لطيف خالي من الصابون مخصص لبشرة الأطفال:</strong> ينظف دون تجفيف أو تهيج.</li>
  <li><strong>ترطيب وتغذية ممتدة بالجليسرين الطبي (15%):</strong> يمنع شعور الشد والجفاف والحكة.</li>
  <li><strong>حماية حاجز البشرة بدرجة حموضة متوازنة (pH 6.0):</strong> تحافظ على الغشاء الهيدروليبيدي للطفل.</li>
  <li><strong>تركيبة خالية 100% من الصابون، العطور، الصبغات، والبارابين:</strong> لا تسبب تحسس العينين.</li>
  <li><strong>موصى به من أطباء الأطفال وأطباء الجلدية:</strong> مناسب لحديثي الولادة والأطفال والبالغين.</li>
  <li><strong>عبوة سعة 250 جم مزودة بضاغط مريح:</strong> حجم ممتاز للاستخدام اليومي والشاور.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الوجه والجسم للطفل بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من سائل كيوفي ودلكي البشرة برفق برغوة ناعمة.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء الدافئ وجففي البشرة بالطبطبة اللطيفة (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الجليسرين الطبي المكثف (Glycerin 15%):</strong> يحبس جزيئات الماء داخل خلايا جلد الطفل.</li>
  <li><strong>المنظفات السائلة الخالية من الصابون:</strong> تنظف المسام وتحفظ النعومة الحريرية لبشرة الرضيع.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والجسم للطفل.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل أم تبحث عن غسول اطفال لطيف للبشرة الحساسة من كيوفي 250 جم لتنظيف وترطيب طفلها بآمان.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كيوفي بيبي (QV Baby Ego)</td></tr>
  <tr><th>الفئة</th><td>العناية بالأطفال / غسولات كيوفي بيبي الطبية 250g</td></tr>
  <tr><th>نوع المنتج</th><td>سائل غسول طبي مرطب خالي من الصابون والعطور لبشرة الرضع (250g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>250 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>بشرة الرضع، حديثي الولادة، الأطفال الجافة، الحساسة والمصابة بالأكزيما</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة طفل ناعمة كالحرير، مرطبة 24 ساعة، ناصعة النقاء وخالية من الجفاف والتهيج</td></tr>
  <tr><th>الملمس</th><td>سائل جل شفاف لطيف يمتص وينشطف بالماء بسهولة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور والصبغات (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>جليسرين طبي (15%)، منظفات خالية من الصابون (pH 6.0)، بارافين مرطب</td></tr>
  <tr><th>بلد المنشأ</th><td>أستراليا (Australia)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>الفئة العمرية</th><td>حديثو الولادة والأطفال والبالغون (من عمر يوم)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الجليسرين الطبي ودرجة pH 6.0 في غسول كيوفي بيبي (QV Baby Gentle Wash)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول كيوفي بيبي اللطيف مشكلة جفاف بشرة الرضع، حرقان الصابون التقليدي، الأكزيما، وتقشر جلد الأطفال.</p>

<h3>لماذا تنجح تركيبة QV Baby Gentle Wash؟</h3>
<p>لأن التركيبة الخالية من الصابون وبدرجة pH 6.0 تنظف مسام الطفل دون التأثير على الأغشية الدهنية الضعيفة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام اليومي مع ماء دافئ أثناء الاستحمام:</strong> ينظف بشرة الطفل بأمان بيولوجي.<br>
2. <strong>التكميل بـ لوشن كيوفي بيبي بعد الشطف:</strong> يحفظ الترطيب الداخلي طوال اليوم.<br>
3. <strong>التجفيف اللطيف بالمنشفة بالطبطبة:</strong> يحافظ على استقرار حواجز البشرة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الغسولات السائلة للأطفال تجفف البشرة."<br>
<strong>الحقيقة:</strong> غسول كيوفي بيبي السائل خالي 100% من الصابون ومدعم بالجليسرين لحفظ رطوبة ونعومة الأطفال.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>ترتبط جزيئات الجليسرين بماء الخلايا بينما تزيل السورفاكتانتات اللطيفة الشوائب دون أي حرقان.</p>"""

    faqs = [
        ("ما هو غسول اطفال لطيف للبشرة الحساسة من كيوفي - 250 جم؟", "هو سائل غسول طبي خالي من الصابون والعطور من كيوفي بيبي بالجليسرين لبشرة الرضع والأطفال الحساسة (250 جم)."),
        ("ما هي فوائد الجليسرين والتركيبة الخالية من الصابون للطفل؟", "تنظف بشرة الطفل بلطف، تحبس الترطيب لـ 24 ساعة، وتمنع الاحمرار والشد والجفاف والأكزيما."),
        ("هل ينظف بشرة الطفل ويرطب بدون صابون أو تهيج؟", "نعم، مثبت سريرياً في تنظيف بشرة الأطفال الحساسة وتوفير نعومة وترطيب خالي من التهيج."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة مزودة بضاغط مريح سعة 250 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الوجه والجسم للطفل، ضعي كمية وكوّني رغوة، دلكي برفق واشطفي بالماء مرتين يومياً."),
        ("هل هو خالٍ من العطور واللانولين والبارابين؟", "نعم، 100% خالٍ من العطور واللانولين والبارابين ومختبر درماتولوجياً."),
        ("أين صُنع غسول كيوفي بيبي اللطيف؟", "صُنع في أستراليا بواسطة Ego Pharmaceuticals."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كيوفي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب حديثي الولادة والأطفال والأكزيما؟", "نعم، ممتاز لحديثي الولادة والأطفال والبالغين ذوي البشرة الحساسة والمصابة بالأكزيما."),
        ("هل يترك بشرة الطفل ناعمة ومرطبة دون شد؟", "نعم، يترك بشرة الطفل ناعمة كالحرير ومرطبة دون أي شعور بالشد."),
        ("هل عبوة 250 جم بضاغط مريحة؟", "نعم، عبوة أنيقة بضاغط مريح جداً للاستخدام اليومي في الشاور."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كيوفي بيبي الماركة الأولى طبياً في أستراليا؟", "نعم، QV Baby الماركة رقم 1 الموصى بها طبياً في أستراليا."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً أثناء الاستحمام."),
        ("هل يناسب الوجه والجسم معاً؟", "نعم، غسول طبي شامل مخصص لبشرة الوجه والجسم للأطفال."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يسبب تحسس العينين؟", "تركيبة لطيفة جداً لا تسبب تحسس العينين أو البشرة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب المواليد والأمهات؟", "نعم، ممتاز للمواليد والأمهات."),
        ("هل يناسب الصيف والشتاء؟", "نعم، تنظيف وترطيب طبي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة للمواليد؟", "نعم، منتج طبي فاخر وأساسي لكل روتين عناية بالمواليد."),
        ("هل يعيد المظهر الناعم السلس لبشرة الطفل؟", "نعم، يجعل بشرة الطفل في غاية النعومة والنقاء."),
        ("هل تتوفر منتجات QV Baby الأخرى؟", "نعم، تتوفر عائلة QV Baby كاملة لدى إكليل أبها."),
        ("هل يفضل استخدام لوشن كيوفي بيبي بعده؟", "نعم، يُفضل استخدام لوشن كيوفي بيبي بعد الغسيل لختم الترطيب."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>QV Baby Gentle Wash for Sensitive Skin - 250g</strong> is the world's most pediatrician-recommended authentic luxury medical soap-free liquid cleansing wash from QV Baby designed to clean, clarify, and moisturize delicate baby and infant skin without harsh soap stinging, irritation, or lipid stripping. Built upon intensive hydrating Glycerin (15%), a 100% soap-free fragrance-free formula, and balanced pH (pH 6.0).</p>
<p>QV Baby Gentle Wash smoothly cleanses facial and body baby pores, shields skin against severe dryness and rashes, and restores biological skin balance, leaving your baby's skin touchably silky soft, hydrated, spotlessly clean, and protected from first wash.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Ultra-Gentle Soap-Free Liquid Wash Formulated for Sensitive Baby Skin:</strong> Cleanses without dryness.</li>
  <li><strong>Extended Hydration with Medical Glycerin (15%):</strong> Prevents post-wash tightness and itching.</li>
  <li><strong>Skin Barrier Protection with Balanced pH (pH 6.0):</strong> Preserves the natural hydrolipid film of infants.</li>
  <li><strong>100% Soap-Free, Fragrance-Free, Dye-Free & Paraben-Free:</strong> Causes zero eye stinging.</li>
  <li><strong>Pediatrician & Dermatologist Recommended Medical Brand:</strong> Safe for newborns, infants, and adults.</li>
  <li><strong>Convenient 250g Pump Dispenser Bottle:</strong> Ideal format for continuous daily bath routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet baby facial and body skin with warm water during bath time.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of QV liquid wash, work into a gentle lather, and massage skin.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and pat skin dry (use twice daily morning & night).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Medical Grade Glycerin (15%):</strong> Locks water molecules deep inside infant skin cells.</li>
  <li><strong>Soap-Free Liquid Cleansers (pH 6.0):</strong> Cleanse pores while preserving touchable silky softness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical infant facial and body skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Mothers and anyone seeking QV Baby Gentle Wash 250g for safe medical baby cleansing and hydration.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>QV Baby (Ego)</td></tr>
  <tr><th>Category</th><td>Baby Care / QV Baby Gentle Cleansers 250g</td></tr>
  <tr><th>Product Type</th><td>Soap-Free Fragrance-Free Medical Infant Liquid Cleansing Wash (250g)</td></tr>
  <tr><th>Volume/Weight</th><td>250 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Newborn, Infant, Sensitive & Eczema-Prone Baby Skin</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, spotlessly clean & tear-free baby skin</td></tr>
  <tr><th>Texture</th><td>Clear fast-rinsing lightweight gentle liquid gel</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free & Dye-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>Medical Glycerin (15%), Soap-Free Cleansers (pH 6.0), Hydrating Paraffin</td></tr>
  <tr><th>Country of Origin</th><td>Australia</td></tr>
  <tr><th>Manufacturer</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>Age Group</th><td>Newborns, Babies & Adults (Ages 0+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Medical Glycerin 15% Hydration & Infant Soap-Free Cleansing</h2>

<h3>What problem does this solve?</h3>
<p>QV Baby Gentle Wash resolves infant skin dryness, eczema flaking, stinging from soap, and post-shower dryness.</p>

<h3>Why choose QV Baby Gentle Wash?</h3>
<p>The soap-free pH 6.0 liquid formula cleanses infant skin pores effectively without stripping natural protective lipids.</p>"""

    en_faqs = [
        ("What is QV Baby Gentle Wash for Sensitive Skin - 250g?", "It is a medical soap-free fragrance-free liquid wash from QV Baby with Glycerin for sensitive infant skin (250g)."),
        ("What are the benefits of 15% Glycerin and the soap-free formula?", "Cleanse baby face and body gently, lock in 24-hour hydration, and prevent tightness and eczema dryness."),
        ("Does it clean and hydrate baby skin without soap or irritation?", "Yes, clinically proven to clean sensitive baby skin and deliver hydration without irritation."),
        ("What volume is contained in this bottle?", "250g pump dispenser bottle."),
        ("How do I use it correctly?", "Wet skin, apply liquid wash, lather gently, massage and rinse with warm water daily."),
        ("Is it fragrance-free, lanolin-free, and paraben-free?", "Yes, 100% free from fragrances, lanolin, and parabens, and clinically tested on baby skin."),
        ("Where is QV Baby Gentle Wash manufactured?", "In Australia by Ego Pharmaceuticals."),
        ("How do I verify authenticity at Ekleel Abha?", "All QV products at Ekleel Abha are 100% original."),
        ("Is it suitable for newborns, babies, and eczema skin?", "Yes, safe and mild for newborns, babies, adults, and eczema-prone skin."),
        ("Does it leave baby skin touchably silky soft?", "Yes, leaves baby skin touchably silky soft and hydrated without tight feeling."),
        ("Is the 250g pump bottle convenient for bath time?", "Yes, sleek pump dispenser bottle ideal for daily bath use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is QV Baby the #1 pediatrician recommended brand in Australia?", "Yes, QV Baby is the #1 pediatrician recommended brand in Australia."),
        ("How many times daily?", "Once or twice daily during shower or bath."),
        ("Is it suitable for face and body together?", "Yes, versatile medical cleanser for facial and body baby skin."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it cause eye stinging?", "Gentle formula causes zero eye or skin stinging."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for mothers and newborns?", "Yes, suitable for both mothers and newborns."),
        ("Is it good for all seasons?", "Yes, ideal medical hydration for summer and winter care."),
        ("Is it a nice baby shower gift?", "Yes, a premier medical essential for daily baby bath routines."),
        ("Does it restore smooth touchable baby skin?", "Yes, gives baby skin a healthy smooth clean look."),
        ("Are other QV Baby products available?", "Yes, the full QV Baby range is available at Ekleel Abha."),
        ("Is following with a QV Baby lotion recommended?", "Yes, follow with a QV Baby moisturizing lotion post-wash."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2122",
        "sku": "EK-2122",
        "gtin": "9314839014192",
        "brand": "QV Baby",
        "ar": {
            "title": "غسول اطفال لطيف  للبشرة الحساسة من كيوفي - 250 جم",
            "meta_title": "غسول كيوفي بيبي اللطيف للبشرة الحساسة 250جم | إكليل أبها",
            "meta_description": "اشتري غسول اطفال لطيف للبشرة الحساسة من كيوفي (250 جم). سائل طبي خالي من الصابون والعطور بالجليسرين لترطيب وتنظيف الوجه والجسم للأطفال. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كيوفي_بيبي", "غسول_كيوفي_بيبي_اللطيف", "غسول_بشرة_الأطفال_الحساسة", "غسول_بدون_صابون_للأطفال", "إكليل_أبها"]
        },
        "en": {
            "title": "QV Baby Gentle Wash for Sensitive Skin - 250g",
            "meta_title": "QV Baby Gentle Wash Sensitive Skin 250g | Ekleel Abha",
            "meta_description": "Buy original QV Baby Gentle Wash for Sensitive Skin (250g). Soap-free fragrance-free medical infant liquid wash. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["qv_baby", "qv_baby_gentle_wash", "infant_gentle_wash", "soap_free_baby_wash", "ekleel_abha"]
        }
    }


def create_product_2123():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>شامبو وبلسم 2 في 1 بلا دموع من كيوفي 200جرام (QV Tear Free Shampoo and Conditioner 2 in 1 200gm)</strong> الشامبو والبلسم الطبي 2 في 1 الخالي من الدموع والصابون الفاخر والأكثر توصية من أطباء الأطفال من كيوفي كيدز (QV Kids / QV 2 in 1) المصمم خصيصاً لتنظيف، تنقية، وتفكيك تشابك شعر الرضع والأطفال الحساس والناعم دون تسبيب أي حرقان للعينين أو جفاف للفروة. يرتكز هذا المستحضر الأصيل (QV 2 in 1 Shampoo 200g) على المرطبات الطبية المزدوجة، التركيبة الخالية 100% من الصابون والعطور والعوامل المهيجة، ودرجة الحموضة المتوازنة (pH 6.0).</p>
<p>يعمل شامبو وبلسم كيوفي 2 في 1 على غسل فروة شعر الطفل بسلاسة، تفكيك التشاك والعقد بسهولة، وحفظ طراوة ونعومة الشعر، ليترك شعر طفلك ناعماً كالحرير، مرطباً، سهلاً بالتمشيط، ومحمياً من الدموع من الغسلة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تركيبة خالية 100% من الدموع والصابون والعطور (Tear-Free Formula):</strong> تجعل وقت الاستحمام ممتعاً.</li>
  <li><strong>عناية مزدوجة 2 في 1 (شامبو + بلسم):</strong> ينظف الفروة ويفكك تشابك وعقد الشعر بسهولة.</li>
  <li><strong>ترطيب وتغذية لفروة رأس وشعر الأطفال:</strong> يمنع الجفاف والتقشر والحكة.</li>
  <li><strong>حماية حاجز الفروة بدرجة حموضة متوازنة (pH 6.0):</strong> تحافظ على الفلورا الجلدية الطبيعية للطفل.</li>
  <li><strong>موصى به من أطباء الأطفال وأطباء الجلدية:</strong> مناسب للأطفال والبالغين ذوي العيون الحساسة.</li>
  <li><strong>أنبوب سعة 200 جم بحجم مالي ممتاز:</strong> تكفي لعدة أشهر من الاستخدام المنتظم.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي شعر وفروة رأس الطفل بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من شامبو وبلسم كيوفي وكوّني رغوة لطيفة ودلكي الشعر والفروة.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء الدافئ وتمشيط الشعر بسهولة (يُستعمل 2-3 مرات أسبوعياً أو عند الاستحمام).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>المنظفات الخالية من الصابون والدموع (pH 6.0):</strong> تنظف شعر الطفل دون تسبيب أي حرقة للعينين.</li>
  <li><strong>عوامل التكييف المطرية (Conditioning Agents):</strong> تنعم ألياف الشعر وتفكك التراكبات والعقد.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على شعر وفروة رأس الأطفال.</li>
  <li>تجنبي التلامس المباشر لداخل العين الشديد برغم أنه خالي من الدموع.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل أم تبحث عن شامبو وبلسم 2 في 1 بلا دموع من كيوفي 200 جم لتنظيف وتسهيل تمشيط شعر طفلها بآمان.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كيوفي كيدز (QV Kids Ego)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر والأطفال / شامبوهات وبلسم كيوفي بلا دموع 200g</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو وبلسم طبي 2 في 1 خالي من الصابون والدموع والعطور للأطفال (200g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>200 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>شعر وفروة الرأس للأطفال، الرضع، والأطغال ذوي العيون الحساسة والتسهيلات المفككة</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر طفل ناعم كالحرير، مرطب 24 ساعة، سهل التمشيط وخالي من التشابك والدموع</td></tr>
  <tr><th>الملمس</th><td>جل سائل ناعم غير حارق ينقلب لرغوة تنظيف وتكييف لطيفة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور والصبغات (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>منظفات خالية من الصابون والدموع (pH 6.0)، عوامل بلسم مطرية</td></tr>
  <tr><th>بلد المنشأ</th><td>أستراليا (Australia)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>الفئة العمرية</th><td>الأطفال والبالغون (من عمر 6 أشهر)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد التركيبة الخالية من الدموع والصابون في شامبو وبلسم كيوفي 2 في 1 (QV 2 in 1)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج شامبو وبلسم كيوفي 2 في 1 مشكلة دموع الأطفال أثناء الغسيل، عقد وتشابك الشعر، وجفاف فروة الرأس من الشامبوهات القاسية.</p>

<h3>لماذا تنجح تركيبة QV Tear Free Shampoo and Conditioner 2 in 1؟</h3>
<p>لأن التركيبة الخالية من الصابون والمطابقة لمعايير pH العينين والجلد (pH 6.0) تفكك العقد وتمنع حرقة الدموع.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق مع ماء دافئ أثناء الاستحمام:</strong> يجعل غسيل شعر الطفل تجربة ممتعة ومريحة.<br>
2. <strong>تمشيط الشعر بمشط واسع الأسنان وهو رطب:</strong> يسهل الانزلاق بفضل البلسم المدمج.<br>
3. <strong>الشطف بالماء الفاتر:</strong> يترك الشعر حريرياً ولامعاً.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مستحضرات 2 في 1 لا تنظف شعر الأطفال جيداً."<br>
<strong>الحقيقة:</strong> شامبو وبلسم كيوفي ينظف الفروة بفاعلية كاملة ويفكك العقد بفضل مركبات البلسم المطرية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبت عوامل التكثيف المطرية على جدار كيراتين الشعر مقللة الاحتكاك والتشابك بين الألياف دون دموع.</p>"""

    faqs = [
        ("ما هو شامبو وبلسم 2 في 1 بلا دموع من كيوفي 200جرام؟", "هو شامبو وبلسم طبي 2 في 1 خالي من الدموع والصابون والعطور من كيوفي لتنظيف وتسهيل تمشيط شعر الأطفال (200 جم)."),
        ("ما هي فوائد التركيبة الخالية من الدموع والصابون (2 في 1)؟", "تنظف شعر الطفل وفروته بلطف، تفكك التشابك والعقد، وتمنع حرقة الدموع والجفاف."),
        ("هل يمنع الدموع ويفكك تشابك الشعر بدون صابون؟", "نعم، مثبت سريرياً في منع حرقة الدموع وتسهيل تمشيط شعر الأطفال وتوفير النعومة."),
        ("ما حجم العبوة؟", "تأتي بأنبوب أنيق سعة 200 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي شعر الطفل، ضعي كمية وكوّني رغوة، دلكي الشعر والفروة واشطفي بالماء الدافئ."),
        ("هل هو خالٍ من الصابون والعطور والبارابين؟", "نعم، 100% خالٍ من الصابون والعطور والبارابين ومختبر درماتولوجياً."),
        ("أين صُنع شامبو وبلسم كيوفي 2 في 1؟", "صُنع في أستراليا بواسطة Ego Pharmaceuticals."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كيوفي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب الأطفال والفتيات والأولاد؟", "نعم، ممتاز للأطفال والفتيات والأولاد ذوي الشعر الناعم والمجعد."),
        ("هل يترك شعر الطفل ناعماً وسهل التمشيط؟", "نعم، ينظف ويفكك العقد ليترك شعر الطفل ناعماً كالحرير وسهل التمشيط."),
        ("هل أنبوب 200 جم مريح ومناسب للاستخدام؟", "نعم، أنبوب أنيق ومريح جداً للاستخدام المنتظم في الاستحمام."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كيوفي الماركة الأولى طبياً في العناية بالأطفال؟", "نعم، QV الماركة رقم 1 الموصى بها طبياً في أستراليا."),
        ("كم مرة أسبوعياً؟", "2 إلى 3 مرات أسبوعياً أو عند الاستحمام."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، ينشطف بالماء الدافئ بسهولة دون ترك أثر لزج."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يسبب تحسس العينين؟", "تركيبة بلا دموع خالية 100% من مسببات تحسس العينين."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب البنات والأولاد؟", "نعم، ممتاز للبنات والأولاد."),
        ("هل يناسب الشتاء والصيف؟", "نعم، غسيل وتنعيم طبيعي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة للأطفال؟", "نعم، منتج طبي فاخر وأساسي لكل روتين عناية بأطفالنا."),
        ("هل يعيد المظهر الناعم السلس لشعر الطفل؟", "نعم، يجعل شعر الطفل في غاية النعومة واللمعان."),
        ("هل تتوفر منتجات QV Kids الأخرى؟", "نعم، تتوفر عائلة QV Kids كاملة لدى إكليل أبها."),
        ("هل يغني عن استخدام بلسم منفصل؟", "نعم، بلسم مدمج 2 في 1 يغني عن استخدام بلسم منفصل."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>QV Tear Free Shampoo and Conditioner 2 in 1 200gm</strong> is the world's most pediatrician-recommended authentic luxury medical tear-free 2-in-1 shampoo and conditioner from QV Kids (QV 2 in 1) designed to clean, clarify, and detangle delicate baby and child hair without eye stinging, scalp dryness, or knotting. Built upon dual medical conditioning agents, a 100% soap-free fragrance-free formula, and balanced pH (pH 6.0).</p>
<p>QV 2-in-1 Tear-Free Shampoo & Conditioner gently cleanses child scalp skin, detangles knots and tangles effortlessly, and preserves hair moisture, leaving your child's hair touchably silky soft, hydrated, easy to comb, and tear-free from first wash.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Tear-Free, Soap-Free & Fragrance-Free Formula:</strong> Makes bath time enjoyable and comfortable.</li>
  <li><strong>Dual 2-in-1 Action (Shampoo + Conditioner):</strong> Cleanses scalp while effortlessly detangling hair knots.</li>
  <li><strong>Hair & Scalp Hydration & Nourishment:</strong> Prevents scalp dryness, flaking, and itching.</li>
  <li><strong>Scalp Barrier Protection with Balanced pH (pH 6.0):</strong> Preserves the natural biological flora of children.</li>
  <li><strong>Pediatrician & Dermatologist Recommended Medical Brand:</strong> Safe for kids and sensitive-eyed adults.</li>
  <li><strong>Sleek 200g Tube Container:</strong> Excellent size lasting months of continuous bath routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet child hair and scalp skin with warm water during bath time.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of QV 2-in-1, work into a gentle lather, and massage scalp and hair softly.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and comb out hair easily (use 2-3 times weekly or during bath time).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Soap-Free & Tear-Free Cleansers (pH 6.0):</strong> Cleanse child hair with zero eye stinging.</li>
  <li><strong>Conditioning Emollient Agents:</strong> Soften hair fibers and detangle knots smoothly.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical child hair and scalp application.</li>
  <li>Avoid direct contact inside the eyes despite tear-free safety.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Mothers and anyone seeking QV Tear Free Shampoo and Conditioner 2 in 1 200g for safe child hair cleansing and detangling.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>QV Kids (Ego)</td></tr>
  <tr><th>Category</th><td>Hair & Baby Care / QV Kids Tear-Free Shampoos 200g</td></tr>
  <tr><th>Product Type</th><td>Soap-Free Fragrance-Free 2-in-1 Tear-Free Child Shampoo & Conditioner (200g)</td></tr>
  <tr><th>Volume/Weight</th><td>200 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Child, Infant & Sensitive-Eyed Hair & Scalp (Fine & Tangled Hair)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, detangled, easy-to-comb & tear-free child hair</td></tr>
  <tr><th>Texture</th><td>Non-stinging clear liquid gel transforming into a gentle conditioning lather</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free & Dye-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>Soap-Free & Tear-Free Cleansers (pH 6.0), Conditioning Emollients</td></tr>
  <tr><th>Country of Origin</th><td>Australia</td></tr>
  <tr><th>Manufacturer</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>Age Group</th><td>Children & Adults (Ages 6 months+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Soap-Free pH 6.0 Tear-Free Cleansing & Fiber Detangling</h2>

<h3>What problem does this solve?</h3>
<p>QV 2-in-1 Tear Free Shampoo and Conditioner resolves child eye stinging during bath time, hair tangles, knots, and scalp dryness.</p>

<h3>Why choose QV 2-in-1 Shampoo & Conditioner?</h3>
<p>The soap-free pH 6.0 formula matches eye fluid acidity preventing tears while built-in conditioning agents untangle knots.</p>"""

    en_faqs = [
        ("What is QV Tear Free Shampoo and Conditioner 2 in 1 200gm?", "It is a medical soap-free fragrance-free 2-in-1 tear-free shampoo and conditioner from QV for child hair cleansing and detangling (200g)."),
        ("What are the benefits of the 2-in-1 tear-free formula?", "Cleanse child hair and scalp gently, detangle knots effortlessly, and prevent eye tears and scalp dryness."),
        ("Does it prevent tears and detangle hair without soap?", "Yes, clinically proven to prevent eye tears, detangle hair knots, and deliver silky hair softness."),
        ("What volume is contained in this tube?", "200g sleek tube."),
        ("How do I use it correctly?", "Apply to wet hair, lather, massage scalp gently and rinse with warm water."),
        ("Is it soap-free, fragrance-free, and paraben-free?", "Yes, 100% free from soap, fragrances, and parabens, and dermatologically tested."),
        ("Where is QV 2-in-1 Shampoo manufactured?", "In Australia by Ego Pharmaceuticals."),
        ("How do I verify authenticity at Ekleel Abha?", "All QV products at Ekleel Abha are 100% original."),
        ("Is it suitable for boys and girls?", "Yes, excellent for boys and girls with fine, curly, or tangled hair."),
        ("Does it leave child hair touchably silky soft and easy to comb?", "Yes, cleanses and untangles knots leaving hair silky soft and easy to comb."),
        ("Is the 200g tube convenient for bath routines?", "Yes, sleek tube ideal for regular daily bath use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is QV Kids a #1 pediatrician recommended brand in Australia?", "Yes, QV Kids is the #1 pediatrician recommended brand in Australia."),
        ("How many times weekly?", "2 to 3 times weekly or during bath time."),
        ("Does it rinse off easily?", "Yes, rinses off smoothly with warm water without sticky residue."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it cause eye stinging?", "Tear-free formula causes zero eye or scalp stinging."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for girls and boys?", "Yes, suitable for both girls and boys."),
        ("Is it good for all seasons?", "Yes, ideal medical hair cleansing for summer and winter care."),
        ("Is it a nice child skincare gift?", "Yes, a premier medical essential for daily child care routines."),
        ("Does it restore smooth shiny child hair?", "Yes, gives child hair a healthy smooth shiny look."),
        ("Are other QV Kids products available?", "Yes, the full QV Kids range is available at Ekleel Abha."),
        ("Does it eliminate the need for a separate conditioner?", "Yes, built-in 2-in-1 conditioner eliminates the need for a separate conditioner."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2123",
        "sku": "EK-2123",
        "gtin": "9314839013874",
        "brand": "QV Kids",
        "ar": {
            "title": "شامبو وبلسم 2 في 1 بلا دموع من كيوفي 200جرام",
            "meta_title": "شامبو وبلسم كيوفي 2 في 1 بلا دموع 200جم | إكليل أبها",
            "meta_description": "اشتري شامبو وبلسم 2 في 1 بلا دموع من كيوفي (200 جم). مستحضر طبي خالي من الصابون والعطور لتنظيف وتفكيك تشابك شعر الأطفال. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كيوفي_كيدز", "شامبو_بلسم_كيوفي_2في1", "شامبو_أطفال_بلا_دموع", "تفكيك_تشابك_الشعر", "إكليل_أبها"]
        },
        "en": {
            "title": "QV Tear Free Shampoo and Conditioner 2 in 1 200gm",
            "meta_title": "QV Tear Free Shampoo & Conditioner 2 in 1 200g | Ekleel Abha",
            "meta_description": "Buy original QV Tear Free Shampoo and Conditioner 2 in 1 (200g). Soap-free fragrance-free 2-in-1 child hair detangling shampoo. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["qv_kids", "qv_2in1_shampoo", "tear_free_shampoo", "child_detangling_shampoo", "ekleel_abha"]
        }
    }


def create_product_2124():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>شامبو وايت سيلفر معزز للون الشعر المصبوغ بالرمادي او الاشقر من لاكمي 300مل (Lakme Teknia White Silver Shampoo for Blonde and Grey Hair - 300ml)</strong> الشامبو البنفسجي المصحح والمعزز للون الشعر الأشقر والرمادي الفاخر الأصيل من لاكمي تيكنيا (Lakme Teknia White Silver) المصمم خصيصاً لتحييد وإزالة الانعكاسات الصفراء والبرتقالية غير المرغوبة وإعادة الصفاء الفضي والنقاء البارد للشعر الأشقر والمصبوغ والرمادي. يرتكز هذا الشامبو الأصيل (Lakme White Silver 300ml) على الصبغة البنفسجية المركز النقية (Violet Pigment)، زهرة الخزامى العضوية (Organic Lotus Flower)، وحمض اللبنيك المقوي لألياف الشعر.</p>
<p>يعمل شامبو لاكمي وايت سيلفر على حماية وتثبيت لون صبغة الشعر الرمادية والأشقر، حماية الشعر من الأكسدة والاصفرار، وتغذية خصلات الشعر المصبوغة، ليترك شعرك ناعماً كالحرير، مرطباً، ناصع الفضة، ومسحوراً باللون الرمادي البارد من الغسلة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تحييد الانعكاسات الصفراء والبرتقالية غير المرغوبة:</strong> يعزز اللون الفضي والرمادي والأشقر البارد.</li>
  <li><strong>حمائية ولون فاقع ومشرق للصبغة:</strong> يطيل عمر صبغة الشعر الأشقر والرمادي والسيلفر.</li>
  <li><strong>ترطيب وتغذية فائقة بأزهار الخزامى العضوية:</strong> يمنع جفاف وتقصف الشعر المصبوغ.</li>
  <li><strong>تركيبة خالية 100% من السلفات والبارابين والزيوت المعدنية:</strong> مناسبة للشعر المصبوغ والمعالج.</li>
  <li><strong>جودة لاكمي تيكنيا (Lakme Teknia) الإسبانية الشهيرة:</strong> العناية الاحترافية بصالونات التجميل.</li>
  <li><strong>عبوة سعة 300 مل بمقاس مالي ممتاز:</strong> تكفي للحفاظ على لون صبغتك لعدة أشهر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي شعر الرأس بالماء الدافئ أثناء الغسيل.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من شامبو لاكمي البنفسجي وكوّني رغوة ودلكي الشعر والفروة برفق.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركي الشامبو على الشعر 1-3 دقائق ثم اشطفي جيداً بالماء الدافئ (يُستعمل 1-2 مرة أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الصبغة البنفسجية المباشرة (Direct Violet Pigment):</strong> تعادل اللون الأصفر في عجلة الألوان وتبرز السيلفر.</li>
  <li><strong>خلاصة زهرة الخزامى وحمض اللبنيك:</strong> يعيدان البناء والنعومة لألياف الشعر المصبوغ.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على شعر الرأس المصبوغ والرمادي.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يملك شعراً مصبوغاً باللون الأشقر أو الرمادي أو الفضي ويبحث عن شامبو لاكمي وايت سيلفر 300 مل لتحييد الاصفرار.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لاكمي (Lakme Teknia Spain)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / شامبوهات لاكمي البنفسجية للشعر الأشقر والرمادي 300ml</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو بنفسجي مصحح ومحييد للاصفرار للشعر الأشقر والرمادي (300ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>300 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>الشعر المصبوغ بالرمادي، الأشقر البارد، الفضي، والشعر الأبيض الطبيعي</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم كالحرير، موحد اللون، ناصع الفضة وخالٍ كلياً من الانعكاسات الصفراء</td></tr>
  <tr><th>الملمس</th><td>سائل بنفسجي دكن غني ينقلب لرغوة تنظيف ناعمة</td></tr>
  <tr><th>العطر</th><td>عطر الأزهار والفواكه الأسباني الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>صبغة بنفسجية مباشرة، خلاصة زهرة الخزامى العضوية، حمض اللبنيك</td></tr>
  <tr><th>بلد المنشأ</th><td>إسبانيا (Spain)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Lakme Cosmetics Spain</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الصبغة البنفسجية وزهرة الخزامى في شامبو لاكمي وايت سيلفر (Lakme White Silver)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج شامبو لاكمي وايت سيلفر مشكلة اصفرار الصبغة الرمادية والأشقر، الانعكاسات البرتقالية، بهتان اللون، وجفاف الشعر المصبوغ.</p>

<h3>لماذا تنجح تركيبة Lakme Teknia White Silver Shampoo؟</h3>
<p>لأن الصبغة البنفسجية المركز تقع في المقابل المباشر للون الأصفر على عجلة الألوان فتحايده وتبرز النغمة الفضية الباردة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام 1-2 مرة أسبوعياً:</strong> يحافظ على النغمة الفضية الباردة دون إفراط.<br>
2. <strong>ترك الشامبو 1-3 دقائق على الشعر:</strong> يتيح للصبغة البنفسجية تحييد الاصفرار.<br>
3. <strong>التكميل بـ بلسم أو ماسك لاكمي تيكنيا:</strong> يحفظ ليونة ورطوبة الشعر المصبوغ.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الشامبو البنفسجي يصبغ الشعر باللون الأرجواني الداكن."<br>
<strong>الحقيقة:</strong> شامبو لاكمي مصمم بتركيبة متوازنة تحايد الاصفرار وتمنح لوناً فضياً بارداً ناصعاً دون صبغ أرجواني.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تلتصق جزيئات الصبغة البنفسجية بكيراتين الشعر المصبوغ ملغية الطول الموجي الأصفر مظهرة النقاء السيلفر.</p>"""

    faqs = [
        ("ما هو شامبو وايت سيلفر معزز للون الشعر المصبوغ بالرمادي او الاشقر من لاكمي 300مل؟", "هو شامبو بنفسجي مصحح ومحييد للاصفرار للشعر الأشقر والرمادي والفضي من لاكمي تيكنيا (300 مل)."),
        ("ما هي فوائد الصبغة البنفسجية وزهرة الخزامى للشعر المصبوغ؟", "تحايد الانعكاسات الصفراء والبرتقالية، تبرز اللون الفضي والرمادي البارد، وترطب ألياف الشعر المصبوغ."),
        ("هل يزيل الانعكاسات الصفراء ويعزز اللون الفضي بدون جفاف؟", "نعم، مثبت سريرياً في تحييد الاصفرار وإبراز اللون الفضي والرمادي البارد دون تجفيف الشعر."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة سعة 300 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الشعر، ضعي كمية، كوّني رغوة، اتركيه 1-3 دقائق واشطفي بالماء الدافئ 1-2 مرة أسبوعياً."),
        ("هل هو خالٍ من السلفات والبارابين والزيوت المعدنية؟", "نعم، 100% خالٍ من السلفات والبارابين وآمن للشعر المصبوغ والمعالج."),
        ("أين صُنع شامبو لاكمي وايت سيلفر؟", "صُنع في إسبانيا بواسطة Lakme Cosmetics Spain."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لاكمي لدى إكليل أبها أصلية 100%."),
        ("ما رائحة شامبو لاكمي وايت سيلفر؟", "عطر الأزهار والفواكه الأسباني الفاخر."),
        ("هل يناسب الشعر الأشقر والرمادي والفضي والأبيض؟", "نعم، ممتاز للشعر المصبوغ بالأشقر، الرمادي، الفضي، والشعر الأبيض الطبيعي."),
        ("هل عبوة 300 مل مريحة وموفرة؟", "نعم، عبوة أنيقة موفرة جداً للحفاظ على صبغة الشعر لعدة أشهر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل لاكمي تيكنيا الماركة الأولى في صالونات التجميل؟", "نعم، Lakme Teknia الماركة الإسبانية رقم 1 الأكثر تفضيلاً في الصالونات."),
        ("كم مرة أسبوعياً؟", "1 إلى 2 مرة أسبوعياً حسب درجة الاصفرار."),
        ("هل يترك الشعر ناعماً ومرطباً؟", "نعم، ينظف ويعادل اللون ليترك الشعر المصبوغ ناعماً كالحرير."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يحافظ على صبغة الشعر الرمادي لفترة أطول؟", "نعم، يطيل عمر صبغة الشعر الرمادية والأشقر ويمنع البهتان والاصفرار."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للنساء والرجال أصحاب الشعر الأشقر والرمادي."),
        ("هل يناسب الشتاء والصيف؟", "نعم، حماية وتصحيح لون مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة لمن يصبغ شعره؟", "نعم، منتج عناية وتصحيح لون فاخر وأساسي لكل شعر مصبوغ."),
        ("هل يعيد المظهر الفضي البارد المشرق للشعر؟", "نعم، يمنح الشعر مظهراً فضياً رمادياً بارداً وناصعاً."),
        ("هل تتوفر منتجات Lakme Teknia الأخرى؟", "نعم، تتوفر عائلة Lakme Teknia كاملة لدى إكليل أبها."),
        ("هل يفضل اتباع بلسم أو ماسك بعده؟", "نعم، يُفضل استخدام بلسم أو ماسك لاكمي تيكنيا بعد الشامبو لحفظ الطراوة."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Lakme Teknia White Silver Shampoo for Blonde and Grey Hair - 300ml</strong> is an authentic luxury neutralizing purple toning shampoo from Lakme Teknia Spain designed to neutralize unwanted yellow, brassy, and orange undertones in blonde, silver, and grey hair. Built upon pure Direct Violet Pigment, Organic Lotus Flower extract, and hair-strengthening Lactic Acid.</p>
<p>Lakme Teknia White Silver Shampoo protects and brightens grey and blonde hair color dyes, shields hair from oxidation and yellowing, and deeply nourishes color-treated locks, leaving your hair touchably silky soft, hydrated, brilliantly silver, and toned from first wash.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Neutralizes Unwanted Yellow & Brassy Undertones:</strong> Enhances cold silver, grey, and blonde hair tones.</li>
  <li><strong>Protects & Brightens Color Vibrancy:</strong> Prolongs the life of silver and blonde dyes.</li>
  <li><strong>Superior Hydration with Organic Lotus Flower:</strong> Prevents dryness and breakage in color-treated hair.</li>
  <li><strong>100% Sulfate-Free, Paraben-Free & Mineral Oil-Free:</strong> Safe for color-treated and processed hair.</li>
  <li><strong>Famous Spanish Lakme Teknia Quality:</strong> Professional salon-grade hair care line.</li>
  <li><strong>Generous 300ml Bottle:</strong> Outstanding value keeping your hair silver for months.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet hair thoroughly with warm water during washing.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of Lakme purple shampoo, lather, and massage hair and scalp gently.</li>
  <li><strong>Step 3:</strong> Leave on hair for 1-3 minutes, then rinse thoroughly with warm water (use 1-2 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Direct Violet Pigment:</strong> Offsets yellow undertones on the color wheel revealing cool silver tones.</li>
  <li><strong>Organic Lotus Flower Extract & Lactic Acid:</strong> Restore strength, flexibility, and softness to color-treated hair fibers.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hair and scalp application on blonde and grey hair.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with blonde, grey, silver, or bleached hair seeking Lakme Teknia White Silver Shampoo 300ml to eliminate yellow undertones.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lakme Teknia (Spain)</td></tr>
  <tr><th>Category</th><td>Hair Care / Lakme Purple Toning Shampoos 300ml</td></tr>
  <tr><th>Product Type</th><td>Sulfate-Free Violet Toning Shampoo for Blonde & Grey Hair (300ml)</td></tr>
  <tr><th>Volume/Weight</th><td>300 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Blonde, Grey, Silver, Bleached & Natural White Hair</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, cool-toned silver & brass-free bright hair</td></tr>
  <tr><th>Texture</th><td>Rich deep-purple liquid shampoo transforming into a gentle lather</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh Spanish floral and fruity scent</td></tr>
  <tr><th>Active Ingredients</th><td>Direct Violet Pigment, Organic Lotus Flower Extract, Lactic Acid</td></tr>
  <tr><th>Country of Origin</th><td>Spain</td></tr>
  <tr><th>Manufacturer</th><td>Lakme Cosmetics Spain</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Direct Violet Pigment Color Neutralization & Organic Lotus Hydration</h2>

<h3>What problem does this solve?</h3>
<p>Lakme Teknia White Silver Shampoo resolves brassy yellow undertones in blonde hair, fading grey dyes, and color-treated hair dryness.</p>

<h3>Why choose Lakme Teknia White Silver Shampoo?</h3>
<p>Direct Violet Pigments fall directly opposite yellow on the color wheel neutralizing warm tones and enhancing cool silver pigments.</p>"""

    en_faqs = [
        ("What is Lakme Teknia White Silver Shampoo for Blonde and Grey Hair - 300ml?", "It is a luxury sulfate-free purple toning shampoo from Lakme Teknia Spain for blonde, silver, and grey hair (300ml)."),
        ("What are the benefits of Direct Violet Pigment and Organic Lotus Flower?", "Neutralize yellow brassiness, enhance cold silver tones, and hydrate color-treated hair fibers."),
        ("Does it remove yellow tones and enhance silver hair without dryness?", "Yes, clinically proven to eliminate brassy yellow tones and enhance cold silver hair without drying."),
        ("What volume is contained in this bottle?", "300ml sleek bottle."),
        ("How do I use it correctly?", "Wet hair, apply shampoo, lather, leave on 1-3 minutes and rinse with warm water 1-2 times weekly."),
        ("Is it sulfate-free, paraben-free, and mineral oil-free?", "Yes, 100% free from sulfates, parabens, and mineral oils, safe for color-treated hair."),
        ("Where is Lakme White Silver Shampoo manufactured?", "In Spain by Lakme Cosmetics Spain."),
        ("How do I verify authenticity at Ekleel Abha?", "All Lakme products at Ekleel Abha are 100% original."),
        ("What scent does Lakme White Silver Shampoo have?", "Luxurious fresh Spanish floral and fruity fragrance."),
        ("Is it suitable for blonde, grey, silver, and white hair?", "Yes, excellent for dyed blonde, silver, grey, and natural white hair."),
        ("Is the 300ml bottle convenient?", "Yes, sleek value bottle keeping your silver hair toned for months."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Lakme Teknia a #1 salon professional brand in Spain?", "Yes, Lakme Teknia is a premier Spanish salon-grade hair care brand."),
        ("How many times weekly?", "1 to 2 times weekly depending on yellowing degree."),
        ("Does it leave hair soft and hydrated?", "Yes, cleanses and tones leaving color-treated hair touchably silky soft."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it prolong grey dye vibrancy?", "Yes, prolongs silver and blonde dye vibrancy preventing fading and yellowing."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women with blonde or grey hair."),
        ("Is it good for all seasons?", "Yes, ideal hair color toning for summer and winter care."),
        ("Is it a nice gift for color-treated hair?", "Yes, a premier salon essential for color-treated hair routines."),
        ("Does it restore bright cool silver hair appearance?", "Yes, gives hair a vibrant cold silver radiant look."),
        ("Are other Lakme Teknia products available?", "Yes, the full Lakme Teknia range is available at Ekleel Abha."),
        ("Is following with a Teknia conditioner recommended?", "Yes, follow with a Lakme Teknia conditioner or mask after shampooing."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2124",
        "sku": "EK-2124",
        "gtin": "8429421440127",
        "brand": "Lakme",
        "ar": {
            "title": "شامبو وايت سيلفر معزز  للون الشعر المصبوغ بالرمادي او الاشقر من لاكمي 300مل",
            "meta_title": "شامبو لاكمي وايت سيلفر البنفسجي 300مل | إكليل أبها",
            "meta_description": "اشتري شامبو وايت سيلفر معزز للون الشعر المصبوغ بالرمادي أو الأشقر من لاكمي (300 مل). شامبو بنفسجي إسباني خالي من السلفات لستحيد الاصفرار وإبراز السيلفر. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["لاكمي", "شامبو_لاكمي_البنفسجي", "لاكمي_وايت_سيلفر", "شامبو_الشعر_الرمادي", "إكليل_أبها"]
        },
        "en": {
            "title": "Lakme Teknia White Silver Shampoo for Blonde and Grey Hair - 300ml",
            "meta_title": "Lakme Teknia White Silver Shampoo 300ml | Ekleel Abha",
            "meta_description": "Buy original Lakme Teknia White Silver Shampoo for Blonde and Grey Hair (300ml). Sulfate-free purple toning shampoo for yellow undertone neutralization. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["lakme", "lakme_white_silver", "purple_shampoo", "blonde_grey_shampoo", "ekleel_abha"]
        }
    }


def create_product_2125():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>اوكسجين كريم (8.4 %) 28 v من لاكمي 1000 مل (Lakme Color Developer OXY Cream (8.4%) 28 Vol - 1000 ml)</strong> مظهر اللون والصبغة الطبي المحترف الفاخر الأصيل من لاكمي تيكنيا كولور (Lakme Collage / Gloss OXY Cream) المصمم خصيصاً لتفعيل وتفتيح لون صبغات وسحب لون الشعر بتركيز 28 فوليوم (28 Vol - 8.4% Hydrogen Peroxide) وتوفير نتائج تفتيح متجانسة وحماية فائقة لألياف الشعر أثناء التلوين. يرتكز هذا الأكسجين الأصيل (Lakme Oxy Cream 28Vol 1000ml) على بيروكسيد الهيدروجين النقي، زيت الأبيسينين المرطب (Abyssinian Oil)، والمكونات المهدئة للفروة.</p>
<p>يعمل أكسجين كريم لاكمي 28 فوليوم على فتح حراشف الشعر بسلاسة لتغلغل صبغة اللون، حماية هيكل الكيراتين الداخلي من التلف والتقصف، وإعطاء لون صبغة زاهي ومستقر لعدة أسابيع، ليترك شعرك المصبوغ ناعماً كالحرير، مرطباً، ناصع اللون، ومحمياً من الجفاف من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وتفعيل مثالي للصبغة بتركيز 28 Vol (8.4% Hydrogen Peroxide):</strong> يفتح اللون حتى 2-3 درجات بتجانس.</li>
  <li><strong>حماية ألياف وكيراتين الشعر بزيت الأبيسينين:</strong> يمنع الجفاف والتلف الناتج عن التلوين.</li>
  <li><strong>قوام كريمي متماسك يسهل الخلط والتطبيق دون تساقط:</strong> يندمج بسلاسة مع صبغات ومسحوق التفتيح.</li>
  <li><strong>تركيبة مهدئة لفروة الرأس تقيم التحسس والحرقان:</strong> تمنح راحة تامة أثناء الصبغ.</li>
  <li><strong>جودة لاكمي (Lakme Cosmetics Spain) الإسبانية الشهيرة:</strong> الأكسجين المفضل بمشاغل وصالونات التجميل.</li>
  <li><strong>عبوة صالونات ضخمة سعة 1000 مل (1 ليتر):</strong> حجم اقتصادي ممتاز يدوم لعدة صبغات وتطبيقات.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> اخلطي أكسجين كريم لاكمي 28 Vol مع صبغة لاكمي أو بودرة التفتيح في وعاء غير معدني بالنسبة الموصى بها (مثال 1:1.5).</li>
  <li><strong>الخطوة الثانية:</strong> وزعي المزيج الكريمي على خصلات الشعر بالفرشاة المخصصة.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركيه لمدة 30-45 دقيقة حسب درجة التفتيح المطلوبة ثم اشطفي جيداً بالماء والشامبو (يُستعمل عند الصبغ).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>بيروكسيد الهيدروجين (8.4% H2O2 / 28 Vol):</strong> يفتح صبغة الشعر الطبيعية ويتيح ثبات اللون الجديد.</li>
  <li><strong>زيت الأبيسينين والمركبات المطرية:</strong> يغلفان الشعر ويحفظان رطوبته ونعومته أثناء الصباغة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي المهني والموضعي على شعر الرأس فقط؛ يحتوي على بيروكسيد الهيدروجين.</li>
  <li>يجب ارتداء القفازات المناسبة وتجنب التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن الحرارة والشمس.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل خبيرة تجميل وكل من يبحث عن أكسجين كريم 28 Vol (8.4%) من لاكمي 1000 مل لتفتيح وتفعيل صبغات الشعر بآمان.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لاكمي (Lakme Color Spain)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / أكسجين ومظهرات لون الصبغة 1000ml (1L)</td></tr>
  <tr><th>نوع المنتج</th><td>كريم أكسجين مظهر للون الصبغة بتركيز 28 فوليوم 8.4% بزيت الأبيسينين (1000ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>1000 مل (1 ليتر)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (خصيصاً المجهد والمصبوغ والمطلوب تفتيحه 2-3 درجات)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم كالحرير، مرطب، لون صبغة ناصع ومتجانس ومحمي من التلف</td></tr>
  <tr><th>الملمس</th><td>كريم دسم أبيض متماسك يسهل الدمج والخلط</td></tr>
  <tr><th>العطر</th><td>عطر كتم كريمي لطيف محايد</td></tr>
  <tr><th>المكونات النشطة</th><td>بيروكسيد الهيدروجين 8.4% (28 Vol)، زيت الأبيسينين، مرطبات جلدية</td></tr>
  <tr><th>بلد المنشأ</th><td>إسبانيا (Spain)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Lakme Cosmetics Spain</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون (من 18 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت الأبيسينين وبيروكسيد الهيدروجين 8.4% في أكسجين لاكمي (Lakme OXY Cream 28 Vol)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج أكسجين كريم لاكمي 28 Vol مشكلة التفتيح غير المتجانس، تلف حراشف الشعر أثناء الصبغ، التحسس، وبهتان صبغات الشعر.</p>

<h3>لماذا تنجح تركيبة Lakme Color Developer OXY Cream 28 Vol (8.4%)؟</h3>
<p>لأن تركيز 28 Vol يفتح 2-3 درجات بدقة متناهية بينما يحمي زيت الأبيسينين الروابط البيبتيدية للكيراتين.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الخلط بالوعاء البلاستيكي بالمعايير الصحيحة:</strong> يضمن تجانس المزيج الكريمي.<br>
2. <strong>ارتداء القفازات وتجنب ملامسة الفروة المتهجة:</strong> يضمن صباغة مريحة وآمنة.<br>
3. <strong>الشطف بالماء والشامبو المخصص بعد انتهاء الوقت:</strong> يوقف تفاعل الأكسدة ويحفظ اللون.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الأكسجين يسبب تكسر وتساقط الشعر دائماً."<br>
<strong>الحقيقة:</strong> أكسجين لاكمي الإسباني مدعم بزيت الأبيسينين لحماية الألياف ومنع التكسر والتلف كلياً أثناء التلوين.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يفتح بيروكسيد الهيدروجين 8.4% ميلانين الشعر ويتيح إرساء الصبغات الجديدة بينما يغلف زيت الأبيسينين الجدار الخارجي.</p>"""

    faqs = [
        ("ما هو اوكسجين كريم (8.4 %) 28 v من لاكمي 1000 مل؟", "هو كريم أكسجين طبي مظهر ومفتّح لصبغات الشعر بتركيز 28 Vol (8.4%) بزيت الأبيسينين من لاكمي (1000 مل)."),
        ("ما هي فوائد بيروكسيد الهيدروجين 8.4% وزيت الأبيسينين؟", "يفتح الشعر 2-3 درجات، يفعل صبغات الشعر بتجانس، ويحمي الألياف والكيراتين من التلف."),
        ("هل يفتح اللون ويفعل الصبغة بتجانس وبدون تلف؟", "نعم، مثبت سريرياً في تفتيح الشعر وتفعيل صبغات اللون بتجانس وحماية كاملة لألياف الشعر."),
        ("ما حجم العبوة؟", "تأتي بعبوة صالونات ضخمة بسعة 1000 مل (1 ليتر)."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اخلطي مع الصبغة أو بودرة التفتيح في وعاء غير معدني، وزعي بالفرشاة واتركيه 30-45 دقيقة ثم اشطفي."),
        ("هل هو آمن ومختبر في الصالونات الإسبانية؟", "نعم، 100% آمن ومختبر درماتولوجياً وفي صالونات التجميل العالمية."),
        ("أين صُنع أكسجين كريم لاكمي؟", "صُنع في إسبانيا بواسطة Lakme Cosmetics Spain."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لاكمي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب جميع أنواع الصبغات ومساحيق التفتيح؟", "نعم، ممتاز لخلطه مع جميع أنواع صبغات لاكمي ومساحيق سحب اللون."),
        ("هل يمنع خشونة وتلف الشعر بعد الصبغ؟", "نعم، ينعم ويغلف الشعر بزيت الأبيسينين لمنع الخشونة والتلف."),
        ("هل عبوة 1000 مل ليتر موفرة واقتصادية؟", "نعم، عبوة جامبو اقتصادية جداً تكفي لعدة تطبيقات وتعد الخيار الأول للصالونات."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الحرارة وضوء الشمس."),
        ("هل لاكمي الماركة الأولى في صبغات وأكسجين الشعر؟", "نعم، Lakme Color الماركة الإسبانية رقم 1 العالمية الأكثر ثقة وتفضيلاً."),
        ("متى يُستعمل؟", "عند التلوين وصباغة وسحب لون الشعر."),
        ("هل يمتزج بسهولة دون تكتل؟", "نعم، قوام كريمي دسم يمتزج فورياً وسلس مع الصبغات."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يقلل الحرقان والتحسس بالفروة؟", "نعم، مدعم بمركبات مهدئة تقلل تحسس الفروة أثناء الصبغ."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب خبيرات التجميل والاستخدام المنزلي؟", "نعم، ممتاز للاستخدام المهني بالصالونات والاستخدام المنزلي الخبير."),
        ("هل يناسب الشتاء والصيف؟", "نعم، أكسجين صبغ مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة لمن تصبغ شعرها؟", "نعم، منتج صالونات فاخر وأساسي لكل روتين صباغة وتلوين."),
        ("هل يعيد المظهر الناعم السلس للشعر المصبوغ؟", "نعم، يجعل الشعر المصبوغ في غاية النعومة والنقاء."),
        ("هل تتوفر تراكيز أكسجين لاكمي الأخرى؟", "نعم، تتوفر تراكيز Lakme OXY Creams كاملة لدى إكليل أبها."),
        ("هل يمنح لون صبغة ناصع ومستقر؟", "نعم، يضمن استقرار اللون وزهاء الصبغة لعدة أسابيع."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Lakme Color Developer OXY Cream (8.4%) 28 Vol - 1000 ml</strong> is an authentic luxury professional hair color developer cream from Lakme Cosmetics Spain designed to activate, lift, and develop hair color dyes and bleaching powders at 28 Volume (8.4% Hydrogen Peroxide) while delivering uniform lifting and superior hair fiber protection. Built upon pure Hydrogen Peroxide, hydrating Abyssinian Oil, and scalp-soothing emollient compounds.</p>
<p>Lakme 28 Vol OXY Cream smoothly opens hair cuticles for optimal pigment penetration, shields internal keratin structures from damage and breakage, and ensures vibrant long-lasting color results, leaving your color-treated hair touchably silky soft, hydrated, brilliantly colored, and protected from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Optimal 28 Vol Color Lift & Activation (8.4% Hydrogen Peroxide):</strong> Lifts hair 2-3 levels evenly.</li>
  <li><strong>Hair Fiber & Keratin Protection with Abyssinian Oil:</strong> Prevents chemical dryness and damage.</li>
  <li><strong>Creamy Smooth Consistency for Easy Non-Drip Mixing:</strong> Blends effortlessly with dyes and bleaches.</li>
  <li><strong>Scalp Soothing Formulation:</strong> Minimizes scalp irritation and stinging during dyeing.</li>
  <li><strong>Famous Spanish Salon Lakme Quality:</strong> #1 choice in professional hair salons worldwide.</li>
  <li><strong>Jumbo 1000ml (1 Liter) Salon Bottle:</strong> Outstanding economic size lasting for multiple applications.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Mix Lakme 28 Vol OXY Cream with Lakme hair dye or bleaching powder in a non-metallic bowl at the recommended ratio (e.g. 1:1.5).</li>
  <li><strong>Step 2:</strong> Apply the smooth creamy mixture onto hair strands using a tint brush.</li>
  <li><strong>Step 3:</strong> Process for 30-45 minutes depending on desired lift, then rinse thoroughly with water and shampoo (use during hair coloring).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>8.4% Hydrogen Peroxide (28 Vol H2O2):</strong> Lightens natural hair melanin enabling vibrant color deposition.</li>
  <li><strong>Abyssinian Oil & Emollients:</strong> Coat hair strands maintaining moisture and softness during chemical processing.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external professional topical hair application only; contains Hydrogen Peroxide.</li>
  <li>Wear suitable gloves and avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from heat and direct sunlight.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Hair colorists and anyone seeking Lakme Color Developer OXY Cream 28 Vol (8.4%) 1000ml for safe color lifting and activation.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lakme Color (Spain)</td></tr>
  <tr><th>Category</th><td>Hair Care / Lakme Professional Color Developers 1000ml (1L)</td></tr>
  <tr><th>Product Type</th><td>28 Vol (8.4%) Abyssinian Oil Professional Hair Color Developer Cream (1000ml)</td></tr>
  <tr><th>Volume/Weight</th><td>1000 ml (1 Liter)</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Specifically Hair Requiring 2-3 Levels of Lift & Dye Activation)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, vibrant & damage-free evenly colored hair</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-drip white developer cream</td></tr>
  <tr><th>Fragrance</th><td>100% Mild gentle neutral creamy scent</td></tr>
  <tr><th>Active Ingredients</th><td>8.4% Hydrogen Peroxide (28 Vol), Abyssinian Oil, Skin Soothing Emollients</td></tr>
  <tr><th>Country of Origin</th><td>Spain</td></tr>
  <tr><th>Manufacturer</th><td>Lakme Cosmetics Spain</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 18+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 8.4% Hydrogen Peroxide Melanin Oxidation & Abyssinian Fiber Shielding</h2>

<h3>What problem does this solve?</h3>
<p>Lakme Color Developer OXY Cream 28 Vol resolves uneven color lifting, chemical fiber damage during dyeing, scalp stinging, and color fading.</p>

<h3>Why choose Lakme OXY Cream 28 Vol?</h3>
<p>Concentrated 28 Vol (8.4% H2O2) lifts hair 2-3 levels with precision while Abyssinian oil coats keratin fibers preventing chemical breakage.</p>"""

    en_faqs = [
        ("What is Lakme Color Developer OXY Cream (8.4%) 28 Vol - 1000 ml?", "It is a professional 28 Vol (8.4%) hair color developer cream from Lakme Spain with Abyssinian Oil (1000ml / 1 Liter)."),
        ("What are the benefits of 8.4% Hydrogen Peroxide and Abyssinian Oil?", "Lifts hair 2-3 levels, activates color dyes evenly, and protects hair fibers and keratin from chemical damage."),
        ("Does it lift hair color evenly and protect hair from chemical damage?", "Yes, clinically proven to lift hair color 2-3 levels evenly while protecting hair fibers with Abyssinian oil."),
        ("What volume is contained in this bottle?", "1000ml (1 Liter) jumbo salon bottle."),
        ("How do I use it correctly?", "Mix with hair dye or bleach in a non-metallic bowl, apply with brush, process 30-45 minutes and rinse thoroughly."),
        ("Is it safe and tested in Spanish professional salons?", "Yes, 100% safe, dermatologically tested, and trusted in international professional salons."),
        ("Where is Lakme OXY Cream manufactured?", "In Spain by Lakme Cosmetics Spain."),
        ("How do I verify authenticity at Ekleel Abha?", "All Lakme products at Ekleel Abha are 100% original."),
        ("Is it suitable for mixing with all dyes and bleaching powders?", "Yes, excellent for mixing with all Lakme hair dyes and bleaching powders."),
        ("Does it prevent hair roughness after dyeing?", "Yes, nourishes and coats hair with Abyssinian oil preventing chemical roughness."),
        ("Is the 1000ml (1 Liter) bottle economic?", "Yes, jumbo economic bottle lasting for multiple coloring treatments."),
        ("How should I store it?", "In a cool, dry place away from heat and direct sunlight."),
        ("Is Lakme a #1 salon hair color brand?", "Yes, Lakme Color is a premier globally trusted Spanish professional hair color brand."),
        ("When is it used?", "During hair dyeing, bleaching, and color lifting processing."),
        ("Does it mix smoothly without clumping?", "Yes, rich smooth cream blends instantly and smoothly with dyes."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it reduce scalp stinging?", "Yes, formulated with soothing emollients reducing scalp stinging during coloring."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for hair colorists and home use?", "Yes, suitable for both salon colorists and expert home hair coloring."),
        ("Is it good for all seasons?", "Yes, ideal hair developer for summer and winter care."),
        ("Is it a nice gift for hair coloring?", "Yes, a premier salon essential for hair coloring routines."),
        ("Does it restore smooth vibrant color-treated hair?", "Yes, gives color-treated hair a healthy smooth vibrant look."),
        ("Are other Lakme OXY Cream volumes available?", "Yes, the full Lakme OXY Cream range is available at Ekleel Abha."),
        ("Does it deliver long-lasting vibrant color results?", "Yes, ensures vibrant long-lasting color results for weeks."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2125",
        "sku": "EK-2125",
        "gtin": "8429421402019",
        "brand": "Lakme",
        "ar": {
            "title": "اوكسجين كريم   (8.4 %) 28 v  من لاكمي 1000 مل",
            "meta_title": "أكسجين كريم لاكمي 28 فوليوم 8.4% 1000مل | إكليل أبها",
            "meta_description": "اشتري أكسجين كريم (8.4%) 28 Vol من لاكمي (1000 مل). مظهر لون الصبغة الإسباني بزيت الأبيسينين لتفتيح الشعر وتفعيل الصبغات 1 ليتر. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["لاكمي", "أكسجين_لاكمي_28v", "مظهر_صبغة_لاكمي", "أكسجين_لاكمي_1000مل", "إكليل_أبها"]
        },
        "en": {
            "title": "Lakme Color Developer OXY Cream (8.4%) 28 Vol - 1000 ml",
            "meta_title": "Lakme Color Developer OXY Cream 28 Vol 1000ml | Ekleel Abha",
            "meta_description": "Buy original Lakme Color Developer OXY Cream (8.4%) 28 Vol (1000ml). Professional Abyssinian Oil hair color developer 1 Liter. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["lakme", "lakme_oxy_cream_28vol", "color_developer", "lakme_developer_1000ml", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 80 builders complete")
