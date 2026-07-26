import json, os

def create_product_2099():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>لوشن مرطب ومهدئ للبشرة من كيو في 250 جم (QV Skin Moisturizing Lotion - 250g)</strong> اللوشن الطبي المرطب والمغذي الفاخر الأكثر توصية عالمياً من كيوفي (QV) المصمم خصيصاً لترطيب، تغذية، وتهدئة بشرة الوجه والجسم الجافة والحساسة دون ترك أي طبقة دهنية ثقيلة. يرتكز هذا اللوشن الأصيل (QV Lotion 250g) على البارافين السائل والمرطب (Liquid Paraffin)، الجليسرين المرطب، وخلوه التام 100% من العطور واللانولين والبارابين.</p>
<p>يعمل لوشن كيوفي الطبي على حبس رطوبة البشرة لـ 24 ساعة، تقليل التقشر والشد والجفاف، وإعادة البناء البيولوجي لحاجز الجلد الوقائي، ليترك بشرة وجهك وجسمك ناعمة كالحرير، مرطبة، خالية من التهيجات، ومحمية طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتغذية خفيفة لـ 24 ساعة للوجه والجسم:</strong> يمنح الجلد طراوة ونعومة فائقة.</li>
  <li><strong>امتصاص فوري دون ترك أثر دهني لزج:</strong> يسهل ارتداء الملابس فوراً بعد الاستحمام.</li>
  <li><strong>ترميم حاجز البشرة بالبارافين والجليسرين الطبي:</strong> يمنع تبخر المياه الداخلية.</li>
  <li><strong>تركيبة خالية 100% من العطور، اللانولين، والبارابين:</strong> مناسبة للبشرة المفرطة الحساسية والأكزيما.</li>
  <li><strong>موصى به من أطباء الجلدية ومختبر طبياً:</strong> آمن لجميع أفراد الأسرة وللأطفال.</li>
  <li><strong>عبوة سعة 250 جم مزودة بضاغط مريح:</strong> حجم ممتاز للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسبة من لوشن كيوفي على بشرة الوجه والجسم النظيفة.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي برفق بحركات دائرية ناعمة حتى الامتصاص الكامل (يُستعمل مرتين يومياً صباحاً ومساءً وبعد الاستحمام).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>البارافين الطبي والجليسرين:</strong> يشكلان عازلاً يحبس الرطوبة ويمنع الجفاف والتقشر.</li>
  <li><strong>المركبات المطرية المائية:</strong> تحفظ النعومة الحريرية للبشرة دون غلق المسام.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن لوشن كيوفي المرطب والمهدئ للبشرة 250 جم للترطيب اليومي خفيف الملمس.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كيوفي (QV Ego)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / لوشنات كيوفي الطبية المرطبة 250g</td></tr>
  <tr><th>نوع المنتج</th><td>لوشن مرطب طبي خالي من العطور واللانولين للوجه والجسم (250g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>250 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الجافة، الحساسة، العادية والمصابة بالأكزيما</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة كالحرير، مرطبة 24 ساعة، خالية من التقشر والدهنية</td></tr>
  <tr><th>الملمس</th><td>لوشن سائل خفيف يمتص فورياً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>بارافين طبي، جليسرين، مركبات ترطيب مائية</td></tr>
  <tr><th>بلد المنشأ</th><td>أستراليا (Australia)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من عمر يوم لحديثي الولادة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد البارافين الطبي والجليسرين في لوشن كيوفي (QV Skin Lotion)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج لوشن كيوفي مشكلة جفاف بشرة الوجه والجسم، التقشر الصباحي، والتهيج الناتج عن العوامل الجوية.</p>

<h3>لماذا تنجح تركيبة QV Skin Moisturizing Lotion؟</h3>
<p>لأن البارافين الطبي الخفيف يشكل درعاً يمنع تبخر الماء بينما يجذب الجليسرين الرطوبة للطبقة القرنية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق فوراً بعد الاستحمام على بشرة رطبة:</strong> يضاعف امتصاص المرطب.<br>
2. <strong>الاستخدام مرتين يومياً صباحاً ومساءً:</strong> يضمن ترطيباً متواصلاً 24 ساعة.<br>
3. <strong>الاستخدام الآمن تحت المكياج:</strong> امتصاصه الخفيف يجعله قاعدة ممتازة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "اللوشنات الخفيفة لا تمنح ترطيباً كافياً للبشرة الجافة."<br>
<strong>الحقيقة:</strong> لوشن كيوفي مدعم بتركيبة طبية تمنح ترطيباً مكثفاً يضاهي الكريمات الثقيلة دون أي لزوجة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتسلل الميكروليبيدات بين الخلايا الجلدية مصلحة الغشاء الهيدروليبيدي الحامي للجلد.</p>"""

    faqs = [
        ("ما هو لوشن مرطب ومهدئ للبشرة من كيو في 250 جم؟", "هو لوشن مرطب طبي خالي من العطور واللانولين من كيوفي للوجه والجسم والبشرة الجافة والحساسة (250 جم)."),
        ("ما هي فوائد البارافين الطبي والجليسرين للوجه والجسم؟", "يحبسان الترطيب لـ 24 ساعة، يمنعان الجفاف والتقشر، ويهدئان البشرة الحساسة والأكزيما."),
        ("هل يمتص فورياً ويرطب لـ 24 ساعة بدون دهنية؟", "نعم، مثبت سريرياً في الامتصاص السريع والترطيب 24 ساعة دون طبقة دهنية لزجة."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة مزودة بضاغط مريح سعة 250 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية مناسبة على الوجه والجسم، دلكي برفق حتى الامتصاص مرتين يومياً وبعد الاستحمام."),
        ("هل هو خالٍ من العطور واللانولين والبارابين؟", "نعم، 100% خالٍ من العطور واللانولين والبارابين ومختبر درماتولوجياً."),
        ("أين صُنع لوشن كيوفي؟", "صُنع في أستراليا بواسطة Ego Pharmaceuticals."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كيوفي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب الوجه والجسم معاً؟", "نعم، لوشن طبي شامل مخصص لبشرة الوجه والجسم."),
        ("هل يترك البشرة ناعمة كالحرير؟", "نعم، يمتص فورياً ليترك البشرة ناعمة كالحرير دون دهنية."),
        ("هل عبوة 250 جم بضاغط مريحة؟", "نعم، عبوة أنيقة بضاغط مريح جداً للاستخدام اليومي والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كيوفي الماركة الأولى طبياً في أستراليا؟", "نعم، QV الماركة رقم 1 الموصى بها طبياً في أستراليا."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل يناسب حديثي الولادة والأطفال والبالغين؟", "نعم، آمن وممتاز لحديثي الولادة والأطفال والبالغين."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في الوقاية من جفاف الشتاء؟", "نعم، ترطيب وتنعيم طبيعي مثالي لجميع فصول السنة."),
        ("هل يسبب انسداد المسام؟", "لا، تركيبة خالية من الزيوت الثقيلة وغير مسببة للانسداد (Non-Comedogenic)."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يصلح كقاعدة تحت المكياج؟", "نعم، قاعدة ممتازة للمكياج بفضل امطصاطه السريع وملمسه الخفيف."),
        ("هل يناسب الشتاء والصيف؟", "نعم، ترطيب طبي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن العناية؟", "نعم، منتج طبي فاخر وأساسي لكل روتين عناية."),
        ("هل يعيد المظهر المشرق الناعم للبشرة؟", "نعم، يمنح البشرة مظهراً ناعماً ومشرقاً."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>QV Skin Moisturizing Lotion - 250g</strong> is the world's most dermatologist-recommended authentic luxury medical hydrating body and facial lotion from QV designed to hydrate, nourish, and soothe dry and sensitive skin without leaving a heavy greasy film. Built upon liquid and soft medical paraffins, hydrating Glycerin, and a 100% fragrance-free, lanolin-free, paraben-free formula.</p>
<p>QV Medical Lotion locks in skin hydration for 24 hours, reduces flaking, tightness, and dryness, and restores the biological protective skin barrier, leaving your face and body touchably silky soft, hydrated, clear of irritation, and protected all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Lightweight 24-Hour Hydration for Face & Body:</strong> Imparts silky softness and flexibility.</li>
  <li><strong>Instant Absorption with Zero Greasy Residue:</strong> Allows immediate dressing post-shower.</li>
  <li><strong>Skin Barrier Restoration with Medical Paraffin & Glycerin:</strong> Prevents transepidermal water loss.</li>
  <li><strong>100% Fragrance-Free, Lanolin-Free & Paraben-Free:</strong> Suitable for ultra-sensitive and eczema skin.</li>
  <li><strong>Dermatologist Recommended & Clinically Tested:</strong> Safe for the whole family, babies, and adults.</li>
  <li><strong>Convenient 250g Pump Dispenser Bottle:</strong> Ideal format for continuous daily care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of QV lotion onto clean facial and body skin.</li>
  <li><strong>Step 2:</strong> Massage gently in smooth circular motions until fully absorbed (use twice daily morning, night & post-shower).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Medical Paraffin & Glycerin:</strong> Form an occlusive barrier locking in moisture and preventing flaking.</li>
  <li><strong>Lightweight Emollient Compounds:</strong> Maintain touchable silky softness without clogging pores.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and body skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking QV Skin Moisturizing Lotion 250g for lightweight daily facial and body skin hydration.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>QV (Ego)</td></tr>
  <tr><th>Category</th><td>Skincare / QV Medical Moisturizing Lotions 250g</td></tr>
  <tr><th>Product Type</th><td>Fragrance-Free Lanolin-Free Medical Hydrating Face & Body Lotion (250g)</td></tr>
  <tr><th>Volume/Weight</th><td>250 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Dry, Sensitive, Normal & Eczema-Prone Skin (Face & Body)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, non-greasy & spotlessly clean skin</td></tr>
  <tr><th>Texture</th><td>Ultra-lightweight fast-absorbing smooth liquid lotion</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>Medical Paraffin, Glycerin, Aqueous Hydrating Compounds</td></tr>
  <tr><th>Country of Origin</th><td>Australia</td></tr>
  <tr><th>Manufacturer</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 0+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Medical Paraffin Occlusion & Lightweight Glycerin Hydration</h2>

<h3>What problem does this solve?</h3>
<p>QV Skin Moisturizing Lotion resolves facial and body dryness, flaking, tightness, and environmental irritation.</p>

<h3>Why choose QV Skin Moisturizing Lotion?</h3>
<p>Medical paraffin forms a protective shield preventing transepidermal water loss while glycerin draws moisture into cells.</p>"""

    en_faqs = [
        ("What is QV Skin Moisturizing Lotion - 250g?", "It is a medical fragrance-free lanolin-free lotion from QV for dry and sensitive face and body skin (250g)."),
        ("What are the benefits of medical paraffin and glycerin for face and body?", "Lock in 24-hour hydration, prevent flaking and dryness, and soothe sensitive eczema-prone skin."),
        ("Does it absorb instantly and hydrate for 24 hours without greasiness?", "Yes, clinically proven to absorb rapidly and hydrate for 24 hours without greasy residue."),
        ("What volume is contained in this bottle?", "250g pump dispenser bottle."),
        ("How do I use it correctly?", "Apply to face and body, massage gently until absorbed twice daily and post-shower."),
        ("Is it fragrance-free, lanolin-free, and paraben-free?", "Yes, 100% free from fragrances, lanolin, and parabens, and dermatologically tested."),
        ("Where is QV Lotion manufactured?", "In Australia by Ego Pharmaceuticals."),
        ("How do I verify authenticity at Ekleel Abha?", "All QV products at Ekleel Abha are 100% original."),
        ("Is it suitable for face and body together?", "Yes, versatile medical moisturizer for facial and body skin."),
        ("Does it leave skin touchably silky soft?", "Yes, absorbs instantly leaving skin silky soft without greasiness."),
        ("Is the 250g pump bottle convenient?", "Yes, sleek pump dispenser bottle ideal for daily care and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is QV the #1 medical skincare brand in Australia?", "Yes, QV is the #1 dermatologist recommended brand in Australia."),
        ("How many times daily?", "Twice daily (morning and night)."),
        ("Is it suitable for newborns, babies, and adults?", "Yes, safe and mild for newborns, babies, and adults."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help prevent winter skin dryness?", "Yes, ideal medical hydration for summer and winter care."),
        ("Does it clog pores?", "No, oil-free non-comedogenic formula."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Does it serve as a good makeup base?", "Yes, lightweight makeup base due to rapid absorption."),
        ("Is it good for all seasons?", "Yes, ideal medical hydration for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, a premier medical essential for daily skincare routines."),
        ("Does it restore smooth radiant skin appearance?", "Yes, gives skin a healthy smooth radiant look."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2099",
        "sku": "EK-2099",
        "gtin": "9314839002618",
        "brand": "QV",
        "ar": {
            "title": "لوشن مرطب ومهدئ للبشرة من كيو في 250 جم",
            "meta_title": "لوشن كيوفي المرطب والمهدئ للبشرة 250جم | إكليل أبها",
            "meta_description": "اشتري لوشن مرطب ومهدئ للبشرة من كيوفي (250 جم). لوشن طبي خالي من العطور واللانولين لترطيب الوجه والجسم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كيوفي", "لوشن_كيوفي_المرطب", "ترطيب_الوجه_والجسم", "لوشن_البشرة_الحساسة", "إكليل_أبها"]
        },
        "en": {
            "title": "QV Skin Moisturizing Lotion - 250g",
            "meta_title": "QV Skin Moisturizing Lotion 250g | Ekleel Abha",
            "meta_description": "Buy original QV Skin Moisturizing Lotion (250g). Fragrance-free lanolin-free medical face and body hydrating lotion. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["qv", "qv_moisturizing_lotion", "qv_lotion", "sensitive_skin_lotion", "ekleel_abha"]
        }
    }


def create_product_2100():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>لوح منظف للطفل بيبي سكين من كيو في - 250 مل (QV Baby Skin Cleansing Bar - 250g)</strong> صابون قالب المنظف الطبي الفاخر الخالي من الصابون من كيوفي بيبي (QV Baby) المصمم خصيصاً لتنظيف، تنقية، وترطيب بشرة الرضع والأطفال الحساسة والرقيقة دون التسبب في أي جفاف أو تحسس أو دموع. يرتكز هذا اللوح الأصيل (QV Baby Bar 250g) على المرطبات الطبية المهدئة، التركيبة الخالية 100% من الصابون والعطور والصبغات، ودرجة الحموضة المتوازنة (pH 6.0).</p>
<p>يعمل لوح منظف كيوفي بيبي على تنظيف مسام جسم ووجه الطفل بسلاسة، حماية حاجز الجلد الرقيق من الجفاف، وحفظ طراوته ونعومته، ليترك بشرة طفلك ناعمة كالحرير، مرطبة، ناصعة النقاء، ومحمية من الحساسية من الغسلة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف خالي من الصابون مخصص لبشرة الأطفال الحساسة:</strong> ينظف دون تجفيف أو تحسس.</li>
  <li><strong>ترطيب وتغذية لحماية بشرة الرضع الرقيقة:</strong> يمنع الشد والجفاف والحكة.</li>
  <li><strong>حماية حاجز الجلد بدرجة حموضة متوازنة (pH 6.0):</strong> تحافظ على الغشاء الهيدروليبيدي للطفل.</li>
  <li><strong>تركيبة خالية 100% من الصابون، العطور، الصبغات، والبارابين:</strong> لا تسبب تحسس العينين أو الجلد.</li>
  <li><strong>موصى به من أطباء الأطفال وأطباء الجلدية:</strong> مناسب لحديثي الولادة والأطفال والبالغين.</li>
  <li><strong>لوح صابوني حجم كبير سعة 250 جم:</strong> يدوم طويلاً للاستخدام العائلي واليومي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الطفل ولوح كيوفي بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> كوّني رغوة ناعمة ودلكي جسم ووجه الطفل برفق.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء الدافئ وجففي البشرة بالطبطبة اللطيفة (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>المركبات الصابونية الخالية من الصابون (pH 6.0):</strong> تنظف جلد الطفل بأمان بيولوجي كامل.</li>
  <li><strong>البارافين والجليسرين الطبي:</strong> يحفظان التوازن المائي للبشرة ويمنعان الجفاف.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف على صحن صابون جاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل أم تبحث عن لوح منظف كيوفي بيبي سكين 250 جم لتنظيف وترطيب بشرة طفلها الحساسة بأمان.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كيوفي بيبي (QV Baby Ego)</td></tr>
  <tr><th>الفئة</th><td>العناية بالأطفال / ألواح وصابون كيوفي بيبي المنظف 250g</td></tr>
  <tr><th>نوع المنتج</th><td>لوح منظف طبي خالي من الصابون والعطور لبشرة الرضع والأطفال (250g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>250 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>بشرة الرضع، حديثي الولادة، الأطفال الحساسة والمصابة بالأكزيما</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة طفل ناعمة كالحرير، مرطبة 24 ساعة، ناصعة النقاء وخالية من الجفاف</td></tr>
  <tr><th>الملمس</th><td>لوح صابوني صلب ينقلب لرغوة تنظيف كريمية لطيفة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور والصبغات (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>منظفات خالية من الصابون (pH 6.0)، بارافين طبي، جليسرين</td></tr>
  <tr><th>بلد المنشأ</th><td>أستراليا (Australia)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>الفئة العمرية</th><td>حديثو الولادة والأطفال والبالغون (من عمر يوم)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد التركيبة الخالية من الصابون بدرجة pH 6.0 في لوح كيوفي بيبي (QV Baby Bar)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج لوح كيوفي بيبي المنظف مشكلة جفاف بشرة الرضع، الأكزيما، التحسس الناتجة عن الصابون العادي، وتجريد الزيوت الطبيعية.</p>

<h3>لماذا تنجح تركيبة QV Baby Skin Cleansing Bar؟</h3>
<p>لأن اللوح خالي تماماً من الصابون وبدرجة حموضة pH 6.0 تماثل حموضة جلد الطفل الطبيعية لمنع الجفاف.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام مع ماء دافئ أثناء الاستحمام:</strong> ينظف جلد الطفل بأمان.<br>
2. <strong>الحفظ على صحن صابون جاف:</strong> يطيل عمر اللوح ويمنع تذوبه.<br>
3. <strong>التكميل بكريم كيوفي بيبي المرطب:</strong> يحفظ الترطيب الداخلي طوال اليوم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "ألواح الصابون تجفف بشرة الأطفال دائماً."<br>
<strong>الحقيقة:</strong> لوح كيوفي بيبي خالي 100% من الصابون ومدعم بمرطبات تحفظ نضارة وجفاف بشرة الرضع.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تحافظ المنظفات خالية الصابون على الغلاف الهيدروليبيدي الرقيق لبشرة حديثي الولادة دون أي تهيج.</p>"""

    faqs = [
        ("ما هو لوح منظف للطفل بيبي سكين من كيو في - 250 مل؟", "هو لوح منظف طبي خالي من الصابون والعطور والصبغات من كيوفي بيبي لبشرة الرضع والأطفال الحساسة (250 جم)."),
        ("ما هي فوائد التركيبة الخالية من الصابون بدرجة pH 6.0 للطفل؟", "تنظف بشرة الطفل بلطف، تحبس الترطيب لـ 24 ساعة، وتمنع الجفاف والاحمرار والأكزيما."),
        ("هل ينظف بشرة الطفل ويرطب بدون صابون أو تهيج؟", "نعم، مثبت سريرياً في تنظيف بشرة الأطفال الحساسة وتوفير نعومة وترطيب خالي من التهيج."),
        ("ما حجم العبوة؟", "تأتي بعبوة لوح صابوني أنيق سعة 250 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي جسم الطفل واللوح، كوّني رغوة، دلكي برفق واشطفي بالماء الدافئ يومياً."),
        ("هل هو خالٍ من الصابون والعطور والصبغات والبارابين؟", "نعم، 100% خالٍ من الصابون والعطور والصبغات ومختبر طبياً على بشرة الأطفال."),
        ("أين صُنع لوح كيوفي بيبي المنظف؟", "صُنع في أستراليا بواسطة Ego Pharmaceuticals."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كيوفي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب حديثي الولادة والأطفال والمصابين بالأكزيما؟", "نعم، ممتاز لحديثي الولادة والأطفال والبالغين والمصابين بالأكزيما والجفاف."),
        ("هل يترك بشرة الطفل ناعمة كالحرير؟", "نعم، ينظف بسلاسة ليترك بشرة الطفل ناعمة كالحرير دون جفاف."),
        ("هل حجم 250 جم يدوم طويلاً؟", "نعم، لوح ضخم يدوم لعدة أشهر من الاستخدام العائلي واليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف على صحن صابون جاف."),
        ("هل كيوفي بيبي الماركة الأولى الموصى بها من أطباء الأطفال؟", "نعم، QV Baby الماركة رقم 1 الموصى بها طبياً في أستراليا."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً أثناء الاستحمام."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، ينشطف بالماء الدافئ بسهولة دون أثر لزج."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يسبب تحسس العينين؟", "تركيبة لطيفة جداً لا تسبب تحسس العينين أو البشرة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الأطفال والبالغين؟", "نعم، ممتاز للأطفال والبالغين أصحاب البشرة الحساسة."),
        ("هل يناسب الشتاء والصيف؟", "نعم، تنظيف وترطيب طبي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة للأمهات والمواليد؟", "نعم، منتج طبي فاخر وأساسي لكل روتين عناية بالمواليد."),
        ("هل يعيد المظهر الناعم السلس لبشرة الطفل؟", "نعم، يجعل بشرة الطفل في غاية النعومة والنقاء."),
        ("هل تتوفر منتجات QV Baby الأخرى؟", "نعم، تتوفر عائلة QV Baby كاملة لدى إكليل أبها."),
        ("هل يفضل استخدام مرطب كيوفي بيبي بعده؟", "نعم، يُفضل استخدام كريم مرطب كيوفي بيبي بعد الاستحمام."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>QV Baby Skin Cleansing Bar - 250g</strong> is the world's most dermatologist and pediatrician-recommended authentic luxury medical soap-free cleansing bar from QV Baby designed to clean, clarify, and moisturize delicate baby and infant skin without dryness, irritation, or teary stinging. Built upon soothing medical emollients, a 100% soap-free fragrance-free dye-free formula, and balanced pH (pH 6.0).</p>
<p>QV Baby Skin Cleansing Bar smoothly cleanses baby body and facial pores, guards delicate skin barriers against dryness, and locks in moisture, leaving your baby's skin touchably silky soft, hydrated, spotlessly clean, and protected from first wash.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Soap-Free Gentle Cleansing Formulated for Sensitive Baby Skin:</strong> Cleanses without drying or irritation.</li>
  <li><strong>Hydration & Nourishment to Protect Delicate Infant Skin:</strong> Prevents tightness, flaking, and itching.</li>
  <li><strong>Skin Barrier Protection with Balanced pH (pH 6.0):</strong> Preserves the natural hydrolipid film of infants.</li>
  <li><strong>100% Soap-Free, Fragrance-Free, Dye-Free & Paraben-Free:</strong> Causes zero eye stinging or skin irritation.</li>
  <li><strong>Pediatrician & Dermatologist Recommended Medical Brand:</strong> Safe for newborns, infants, and adults.</li>
  <li><strong>Large 250g Cleansing Bar:</strong> Long-lasting format for daily continuous family use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet baby skin and the QV bar with warm water during bath time.</li>
  <li><strong>Step 2:</strong> Work into a rich gentle lather and massage baby's face and body softly.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and pat skin dry with a soft towel (use daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Soap-Free Cleansing Agents (pH 6.0):</strong> Cleanse baby skin with complete biological safety.</li>
  <li><strong>Medical Paraffin & Glycerin:</strong> Maintain skin moisture balance preventing dryness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and body skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place on a dry soap dish.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Mothers and anyone seeking QV Baby Skin Cleansing Bar 250g for safe baby skin cleansing and hydration.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>QV Baby (Ego)</td></tr>
  <tr><th>Category</th><td>Baby Care / QV Baby Cleansing Bars 250g</td></tr>
  <tr><th>Product Type</th><td>Soap-Free Fragrance-Free Medical Infant Cleansing Bar (250g)</td></tr>
  <tr><th>Volume/Weight</th><td>250 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Newborn, Infant, Sensitive & Eczema-Prone Baby Skin</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, spotlessly clean & tear-free baby skin</td></tr>
  <tr><th>Texture</th><td>Solid bar transforming into a gentle creamy cleansing lather</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free & Dye-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>Soap-Free Cleansers (pH 6.0), Medical Paraffin, Glycerin</td></tr>
  <tr><th>Country of Origin</th><td>Australia</td></tr>
  <tr><th>Manufacturer</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>Age Group</th><td>Newborns, Babies & Adults (Ages 0+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Soap-Free pH 6.0 Cleansing & Infant Hydrolipid Preservation</h2>

<h3>What problem does this solve?</h3>
<p>QV Baby Skin Cleansing Bar resolves infant skin dryness, eczema irritation, stinging from ordinary soaps, and lipid stripping.</p>

<h3>Why choose QV Baby Cleansing Bar?</h3>
<p>The soap-free pH 6.0 bar matches natural infant skin acidity protecting delicate epidermal barriers.</p>"""

    en_faqs = [
        ("What is QV Baby Skin Cleansing Bar - 250g?", "It is a medical soap-free fragrance-free dye-free cleansing bar from QV Baby for sensitive infant and baby skin (250g)."),
        ("What are the benefits of the soap-free pH 6.0 formula for babies?", "Cleanse baby skin gently, lock in 24-hour hydration, and prevent dryness, redness, and eczema."),
        ("Does it clean and hydrate baby skin without soap or irritation?", "Yes, clinically proven to clean sensitive baby skin and deliver hydration without irritation."),
        ("What volume is contained in this bar?", "250g large cleansing bar."),
        ("How do I use it correctly?", "Wet skin and bar, lather, massage gently and rinse with warm water daily."),
        ("Is it soap-free, fragrance-free, dye-free, and paraben-free?", "Yes, 100% free from soap, fragrances, dyes, and parabens, and clinically tested on baby skin."),
        ("Where is QV Baby Bar manufactured?", "In Australia by Ego Pharmaceuticals."),
        ("How do I verify authenticity at Ekleel Abha?", "All QV products at Ekleel Abha are 100% original."),
        ("Is it suitable for newborns, infants, and eczema skin?", "Yes, excellent for newborns, infants, adults, and eczema-prone skin."),
        ("Does it leave baby skin touchably silky soft?", "Yes, cleanses smoothly leaving baby skin silky soft without dryness."),
        ("Does the 250g bar last long?", "Yes, large bar lasts months of regular daily bath use."),
        ("How should I store it?", "In a cool, dry place on a dry soap dish."),
        ("Is QV Baby the #1 pediatrician recommended brand in Australia?", "Yes, QV Baby is the #1 pediatrician recommended brand in Australia."),
        ("How many times daily?", "Once or twice daily during bath time."),
        ("Does it rinse off easily?", "Yes, rinses off smoothly with warm water without sticky residue."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it cause eye stinging?", "Gentle formula causes zero eye or skin stinging."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for adults and children?", "Yes, suitable for both children and sensitive skin adults."),
        ("Is it good for all seasons?", "Yes, ideal medical cleansing for summer and winter care."),
        ("Is it a nice baby shower gift?", "Yes, a premier medical essential for baby care routines."),
        ("Does it restore smooth touchable baby skin?", "Yes, gives baby skin a healthy smooth clean look."),
        ("Are other QV Baby products available?", "Yes, the full QV Baby medical range is available at Ekleel Abha."),
        ("Is following with a QV Baby moisturizer recommended?", "Yes, follow with a QV Baby moisturizing cream post-bath."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2100",
        "sku": "EK-2100",
        "gtin": "9314839014239",
        "brand": "QV Baby",
        "ar": {
            "title": "لوح منظف للطفل بيبي سكين من كيو في - 250 مل",
            "meta_title": "لوح منظف كيوفي بيبي سكين للأطفال 250جم | إكليل أبها",
            "meta_description": "اشتري لوح منظف للطفل بيبي سكين من كيوفي (250 جم). صابون طبي خالي من الصابون والعطور لبشرة الرضع والأطفال الحساسة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كيوفي_بيبي", "لوح_منظف_كيوفي_بيبي", "صابون_الأطفال_بدون_صابون", "عناية_الرضع", "إكليل_أبها"]
        },
        "en": {
            "title": "QV Baby Skin Cleansing Bar - 250g",
            "meta_title": "QV Baby Skin Cleansing Bar 250g | Ekleel Abha",
            "meta_description": "Buy original QV Baby Skin Cleansing Bar (250g). Soap-free fragrance-free medical infant cleansing bar. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["qv_baby", "qv_baby_bar", "soap_free_baby_bar", "infant_cleansing_bar", "ekleel_abha"]
        }
    }


def create_product_2101():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>لوشن متعدد الاغراض للوجه والجسم البشرة العادية الى الجافة و الحساسة من سيتافيل 236مل (Cetaphil Multi-Purpose Lotion for Face and Body - Normal to Dry and Sensitive Skin - 236ml)</strong> لوشن الترطيب الطبي الفاخر الأكثر توصية عالمياً من سيتافيل (Cetaphil) المصمم خصيصاً لترطيب، تغذية، وترميم بشرة الوجه والجسم العادية إلى الجافة والحساسة دون التسبب في أي ثقل دهني أو انسداد للمسام. يرتكز هذا اللوشن الأصيل (Cetaphil Lotion 236ml) على مركب النياسيناميد المهدئ (Vitamin B3)، البانثينول المغذي (Pro-Vitamin B5)، والجليسرين المرطب المكثف.</p>
<p>يعمل لوشن سيتافيل متعدد الأغراض على حبس رطوبة البشرة لـ 48 ساعة متواصلة، تقليل التقشر والشد والجفاف، وإعادة البناء البيولوجي لحاجز الوجه والجسم الوقائي، ليترك بشرتك ناعمة كالحرير، مرطبة عمقاً، ناصعة النقاء، ومحمية من الحساسية والجفاف من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتغذية ممتدة لـ 48 ساعة بحمض البانثينول والنياسيناميد:</strong> يرمم حاجز الجلد المتضرر.</li>
  <li><strong>لوشن متعدد الأغراض مخصص للوجه والجسم معاً:</strong> يوفر عناية شاملة فائقة البساطة.</li>
  <li><strong>امتصاص فوري دون ترك أثر دهني ثقيل:</strong> مناسب للاستخدام اليومي والارتداء السريع للملابس.</li>
  <li><strong>تركيبة خالية 100% من العطور والبارابين والزيوت:</strong> لا تسبب انسداد المسام (Non-Comedogenic).</li>
  <li><strong>موصى به من أطباء الجلدية للبشرة العادية إلى الجافة والحساسة:</strong> مختبر درماتولوجياً.</li>
  <li><strong>عبوة سعة 236 مل مزودة بضاغط مريح:</strong> حجم ممتاز للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسبة من لوشن سيتافيل على بشرة الوجه والجسم النظيفة.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي برفق بحركات دائرية حتى الامتصاص الكامل (يُستعمل مرتين يومياً صباحاً ومساءً وبعد الاستحمام).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>النياسيناميد والبانثينول (B3 & Pro-B5):</strong> يرممان غطاء الوجه والجسم الدهني ويهدئان الاحمرار.</li>
  <li><strong>الجليسرين والمركبات المطرية المائية:</strong> يحبسان الترطيب الداخلي لـ 48 ساعة متواصلة.</li>
</ul>

<h2>تحذيرات وااحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن لوشن سيتافيل متعدد الأغراض 236 مل لترطيب وتغذية الوجه والجسم للبشرة الجافة والحساسة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سيتافيل (Cetaphil Galderma)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / لوشنات سيتافيل الطبية المرطبة 236ml</td></tr>
  <tr><th>نوع المنتج</th><td>لوشن مرطب طبي متعدد الأغراض خالي من العطور للوجه والجسم (236ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>236 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة العادية، الجافة، الحساسة والمكونة للقشور (للوجه والجسم)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة كالحرير، مرطبة 48 ساعة، ناصعة النقاء وغير دهنية</td></tr>
  <tr><th>الملمس</th><td>لوشن سائل خفيف يمتص فورياً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>نياسيناميد (B3)، بانثينول (Pro-B5)، جليسرين مرطب</td></tr>
  <tr><th>بلد المنشأ</th><td>كندا / الولايات المتحدة (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Galderma Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد النياسيناميد والبانثينول في لوشن سيتافيل (Cetaphil Multi-Purpose Lotion)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج لوشن سيتافيل متعدد الأغراض مشكلة جفاف بشرة الوجه والجسم، التقشر، الحساسية، وتضرر حاجز الترطيب.</p>

<h3>لماذا تنجح تركيبة Cetaphil Multi-Purpose Lotion؟</h3>
<p>لأن النياسيناميد والبانثينول يعيدان بناء الدهون السطحية بينما يمنح الجليسرين ترطيباً 48 ساعة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق فوراً بعد الاستحمام على بشرة رطبة:</strong> يضاعف امتصاص البانثينول.<br>
2. <strong>الاستخدام مرتين يومياً (صباحاً ومساءً):</strong> يضمن ترطيباً متواصلاً 48 ساعة.<br>
3. <strong>الاستخدام الآمن تحت المكياج:</strong> امتصاصه الخفيف يجعله قاعدة ممتازة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "اللوشنات متعددة الأغراض تسبب انسداد مسام الوجه."<br>
<strong>الحقيقة:</strong> لوشن سيتافيل خالي 100% من الزيوت الثقيلة وغير مسبب للانسداد (Non-Comedogenic).</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تحفز فيتامينات B3 و Pro-B5 تخليق سيراميدات الأدمة مصلحة حاجز الوجه والجسم البيولوجي.</p>"""

    faqs = [
        ("ما هو لوشن متعدد الاغراض للوجه والجسم البشرة العادية الى الجافة و الحساسة من سيتافيل 236مل؟", "هو لوشن مرطب طبي خالي من العطور بالنياسيناميد والبانثينول من سيتافيل للوجه والجسم (236 مل)."),
        ("ما هي فوائد النياسيناميد والبانثينول والجليسرين للوجه والجسم؟", "ترمم حاجز البشرة، تحبس الترطيب لـ 48 ساعة، وتمنع الجفاف والتقشر والاحمرار."),
        ("هل يمتص فورياً ويرطب لـ 48 ساعة بدون دهنية؟", "نعم، مثبت سريرياً في الامتصاص السريع والترطيب 48 ساعة دون طبقة دهنية لزجة."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة مزودة بضاغط مريح سعة 236 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية مناسبة على الوجه والجسم، دلكي برفق حتى الامتصاص مرتين يومياً وبعد الاستحمام."),
        ("هل هو خالٍ من العطور والبارابين والزيوت؟", "نعم، 100% خالٍ من العطور والبارابين ومختبر درماتولوجياً."),
        ("أين صُنع لوشن سيتافيل؟", "صُنع بواسطة Galderma Laboratories العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات سيتافيل لدى إكليل أبها أصلية 100%."),
        ("هل يناسب الوجه والجسم معاً؟", "نعم، لوشن طبي متعدد الأغراض مخصص لبشرة الوجه والجسم."),
        ("هل يترك البشرة ناعمة كالحرير؟", "نعم، يمتص فورياً ليترك البشرة ناعمة كالحرير دون دهنية."),
        ("هل عبوة 236 مل بضاغط مريحة؟", "نعم، عبوة أنيقة بضاغط مريح جداً للاستخدام اليومي والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل سيتافيل الماركة الأولى طبياً في العناية الجلدية؟", "نعم، Cetaphil الماركة رقم 1 الموصى بها طبياً من أطباء الجلدية."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل يناسب البشرة العادية والجافة والحساسة؟", "نعم، ممتاز للبشرة العادية، الجافة، الحساسة والمكونة للقشور."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في الوقاية من جفاف الشتاء؟", "نعم، ترطيب وتنعيم طبيعي مثالي لجميع فصول السنة."),
        ("هل يسبب انسداد المسام؟", "لا، تركيبة خالية من الزيوت الثقيلة وغير مسببة للانسداد (Non-Comedogenic)."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء والاطفال؟", "نعم، ممتاز للنساء والرجال والأطفال من سن 3 سنوات."),
        ("هل يصلح كقاعدة تحت المكياج؟", "نعم، قاعدة ممتازة للمكياج بفضل امطصاطه السريع وملمسه الخفيف."),
        ("هل يناسب الشتاء والصيف؟", "نعم، ترطيب طبي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن العناية؟", "نعم، منتج طبي فاخر وأساسي لكل روتين عناية."),
        ("هل يعيد المظهر المشرق الناعم للبشرة؟", "نعم، يمنح البشرة مظهراً ناعماً ومشرقاً."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Cetaphil Multi-Purpose Lotion for Face and Body - Normal to Dry and Sensitive Skin - 236ml</strong> is the world's most dermatologist-recommended authentic luxury medical hydrating face and body lotion from Cetaphil designed to hydrate, nourish, and repair normal to dry and sensitive skin without heavy oiliness or pore clogging. Built upon soothing Niacinamide (Vitamin B3), Panthenol (Pro-Vitamin B5), and hydrating Glycerin.</p>
<p>Cetaphil Multi-Purpose Lotion locks in internal skin moisture for 48 continuous hours, reduces flaking, tightness, and dryness, and restores the biological protective barrier of face and body skin, leaving your skin touchably silky soft, deeply hydrated, spotlessly clean, and protected from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>48-Hour Extended Hydration & Repair with Niacinamide & Panthenol:</strong> Restores damaged skin barriers.</li>
  <li><strong>Multi-Purpose Formulation Designed for Face & Body:</strong> Provides simple comprehensive medical care.</li>
  <li><strong>Instant Absorption with Zero Heavy Greasy Residue:</strong> Allows immediate dressing post-application.</li>
  <li><strong>100% Fragrance-Free, Paraben-Free & Oil-Free:</strong> Non-comedogenic formula that will not clog pores.</li>
  <li><strong>Dermatologist Recommended for Normal, Dry & Sensitive Skin:</strong> Clinically tested.</li>
  <li><strong>Convenient 236ml Pump Dispenser Bottle:</strong> Ideal size for daily care and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of Cetaphil lotion onto clean facial and body skin.</li>
  <li><strong>Step 2:</strong> Massage gently in smooth circular motions until fully absorbed (use twice daily morning, night & post-shower).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Niacinamide & Panthenol (B3 & Pro-B5):</strong> Rebuild protective skin lipids and calm irritation.</li>
  <li><strong>Glycerin & Aqueous Emollients:</strong> Lock in internal moisture for 48 continuous hours.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and body skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Cetaphil Multi-Purpose Lotion 236ml for facial and body skin hydration and barrier repair.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Cetaphil (Galderma)</td></tr>
  <tr><th>Category</th><td>Skincare / Cetaphil Medical Moisturizing Lotions 236ml</td></tr>
  <tr><th>Product Type</th><td>Fragrance-Free Multi-Purpose Niacinamide Face & Body Lotion (236ml)</td></tr>
  <tr><th>Volume/Weight</th><td>236 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Normal, Dry & Sensitive Skin (Face & Body)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 48H hydrated, non-greasy & spotlessly clean skin</td></tr>
  <tr><th>Texture</th><td>Ultra-lightweight fast-absorbing smooth liquid lotion</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>Niacinamide (B3), Panthenol (Pro-B5), Hydrating Glycerin</td></tr>
  <tr><th>Country of Origin</th><td>Canada / USA</td></tr>
  <tr><th>Manufacturer</th><td>Galderma Laboratories</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 3+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Niacinamide B3 Barrier Repair & Panthenol 48-Hour Retention</h2>

<h3>What problem does this solve?</h3>
<p>Cetaphil Multi-Purpose Lotion resolves facial and body dryness, skin flaking, tightness, and environmental sensitivity.</p>

<h3>Why choose Cetaphil Multi-Purpose Lotion?</h3>
<p>Niacinamide and Panthenol stimulate epidermal ceramide synthesis restoring skin barriers while glycerin locks in 48-hour moisture.</p>"""

    en_faqs = [
        ("What is Cetaphil Multi-Purpose Lotion for Face and Body - Normal to Dry and Sensitive Skin - 236ml?", "It is a medical fragrance-free lotion from Cetaphil with Niacinamide and Panthenol for normal, dry, and sensitive face and body skin (236ml)."),
        ("What are the benefits of Niacinamide, Panthenol, and Glycerin for face and body?", "Restore skin barrier, lock in 48-hour hydration, and prevent flaking, dryness, and redness."),
        ("Does it absorb instantly and hydrate for 48 hours without greasiness?", "Yes, clinically proven to absorb rapidly and hydrate for 48 hours without greasy residue."),
        ("What volume is contained in this bottle?", "236ml pump dispenser bottle."),
        ("How do I use it correctly?", "Apply to face and body, massage gently until absorbed twice daily and post-shower."),
        ("Is it fragrance-free, paraben-free, and oil-free?", "Yes, 100% free from fragrances, parabens, and oils, and dermatologically tested."),
        ("Where is Cetaphil Lotion manufactured?", "By Galderma Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Cetaphil products at Ekleel Abha are 100% original."),
        ("Is it suitable for face and body together?", "Yes, multi-purpose medical moisturizer for facial and body skin."),
        ("Does it leave skin touchably silky soft?", "Yes, absorbs instantly leaving skin silky soft without greasiness."),
        ("Is the 236ml pump bottle convenient?", "Yes, sleek pump dispenser bottle ideal for daily care and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Cetaphil a #1 dermatologist recommended brand?", "Yes, Cetaphil is a globally leading dermatologist recommended brand."),
        ("How many times daily?", "Twice daily (morning and night)."),
        ("Is it suitable for normal, dry, and sensitive skin?", "Yes, excellent for normal, dry, sensitive, and flaking skin."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help prevent winter skin dryness?", "Yes, ideal medical hydration for summer and winter care."),
        ("Does it clog pores?", "No, oil-free non-comedogenic formula."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men, women, and kids?", "Yes, safe and suitable for everyone aged 3+."),
        ("Does it serve as a good makeup base?", "Yes, lightweight makeup base due to rapid absorption."),
        ("Is it good for all seasons?", "Yes, ideal medical hydration for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, a premier medical essential for daily skincare routines."),
        ("Does it restore smooth radiant skin appearance?", "Yes, gives skin a healthy smooth radiant look."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2101",
        "sku": "EK-2101",
        "gtin": "5020465202592",
        "brand": "Cetaphil",
        "ar": {
            "title": "لوشن متعدد الاغراض للوجه والجسم  البشرة العادية الى الجافة و الحساسة من سيتافيل 236مل",
            "meta_title": "لوشن سيتافيل للوجه والجسم للبشرة الجافة 236مل | إكليل أبها",
            "meta_description": "اشتري لوشن متعدد الأغراض للوجه والجسم من سيتافيل (236 مل). لوشن طبي بالنياسيناميد والبانثينول لترطيب البشرة الجافة والحساسة 48 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["سيتافيل", "لوشن_سيتافيل_متعدد_الأغراض", "ترطيب_الوجه_والجسم", "سيتافيل_البشرة_الحساسة", "إكليل_أبها"]
        },
        "en": {
            "title": "Cetaphil Multi-Purpose Lotion for Face and Body - Normal to Dry and Sensitive Skin - 236ml",
            "meta_title": "Cetaphil Multi-Purpose Lotion 236ml | Ekleel Abha",
            "meta_description": "Buy original Cetaphil Multi-Purpose Lotion for Face and Body (236ml). Fragrance-free Niacinamide & Panthenol 48H hydrating lotion. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["cetaphil", "cetaphil_multi_purpose_lotion", "cetaphil_lotion", "sensitive_skin_lotion", "ekleel_abha"]
        }
    }


def create_product_2102():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>رغوة تنظيف البشرة العادية والدهنية من سيرافي 473مل (CeraVe Foaming Facial Cleanser for Normal to Oily Skin - 473ml)</strong> الغسول المنظف الطبي الفاخر الضخم الأكثر توصية عالمياً من سيرافي (CeraVe) المصمم خصيصاً لتنظيف، تصفية، وإزالة الزيوت الزائدة والمكياج لبشرة الوجه العادية والدهنية دون التسبب في جفاف أو حكة أو تضرر لحاجز البشرة. يرتكز هذا الغسول الأصيل (CeraVe Foaming Cleanser 473ml) على السيراميدات الثلاثية الأساسية (Ceramides 1, 3, 6-II)، النياسيناميد المهدئ (Niacinamide)، وحمض الهيالورونيك (Hyaluronic Acid).</p>
<p>يعمل غسول رغوة سيرافي على تنظيف مسام الوجه عمقاً من الدهون المتراكمة والشوائب، تقليل اللمعان الدهني، وتهدئة البشرة وإعادة توازنها المائي، ليترك وجهك ناعماً كالحرير، ناصع النظافة، منتعشاً، ومحمياً من الانسداد والبثور من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف رغوي ناعم وتصفية فائقة للدهون والشوائب:</strong> ينظف المسام بفاعلية دون تجريد الزيوت الطبيعية.</li>
  <li><strong>ترميم حاجز البشرة بالسيراميدات الثلاثية الأساسية:</strong> تعوض النقص في سيراميدات الوجه الطبيعية.</li>
  <li><strong>تهدئة البشرة وتقليل الاحمرار واللمعان بالنياسيناميد:</strong> ينظم إفراز السيبوم ويهدئ التهيجات.</li>
  <li><strong>ترطيب وحبس الماء بحمض الهيالورونيك:</strong> يمنع شعور الشد والجفاف بعد الغسيل.</li>
  <li><strong>تركيبة خالية 100% من العطور والزيوت والبارابين:</strong> لا تسبب انسداد المسام (Non-Comedogenic).</li>
  <li><strong>عبوة جامبو ضخمة سعة 473 مل بضاغط مريح:</strong> توفير ممتاز للاستخدام العائلي اليومي المستمر.</li>
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
  <li>لكل من يملك بشرة عادية إلى دهنية ويبحث عن رغوة سيرافي المنظفة الجامبو 473 مل لتنظيف المسام وتصفية الدهون.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سيرافي (CeraVe)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / منظفات سيرافي الرغوية للوجه 473ml</td></tr>
  <tr><th>نوع المنتج</th><td>رغوة غسول طبي مصفٍ للدهون بالسيراميدات والنياسيناميد (473ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>473 مل</td></tr>
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
        ("ما هو رغوة تنظيف البشرة العادية والدهنية من سيرافي 473مل؟", "هو غسول طبي رغوي ضخم خالي من العطور والزيوت من سيرافي بالسيراميدات والنياسيناميد للبشرة العادية والدهنية (473 مل)."),
        ("ما هي فوائد النياسيناميد والسيراميدات الثلاثية للبشرة الدهنية؟", "ينظم النياسيناميد الدهون ويهدئ التهيجات، بينما ترمم السيراميدات حاجز الوجه وتمنع الجفاف."),
        ("هل ينظف المسام ويقلل الدهون دون جفاف؟", "نعم، مثبت سريرياً في تنظيف المسام وتقليل الدهون دون تسبيب أي جفاف أو شد بالوجه."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة ضخمة مزودة بضاغط مريح سعة 473 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الوجه، ضعي كمية وكوّني رغوة، دلكي برفق واشطفي بالماء مرتين يومياً."),
        ("هل هو خالٍ من العطور والزيوت والبارابين؟", "نعم، 100% خالٍ من العطور والزيوت والبارابين ومختبر درماتولوجياً."),
        ("أين صُنع غسول سيرافي الرغوي؟", "صُنع بواسطة CeraVe LLC (مجموعة L'Oréal العالمية)."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات سيرافي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب البشرة الدهنية والمختلطة والمكونة للبثور؟", "نعم، ممتاز للبشرة العادية، الدهنية، المختلطة والمعرضة للبثور."),
        ("هل يترك البشرة غير لامعة ونظيفة؟", "نعم، يترك البشرة غير لامعة بالدهون ونظيفة وناعمة كالحرير."),
        ("هل عبوة 473 مل جامبو مريحة وموفرة؟", "نعم، عبوة جامبو موفرة جداً بضاغط مريح للاستخدام اليومي والعائلي."),
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
<p>The <strong>CeraVe Foaming Facial Cleanser for Normal to Oily Skin - 473ml</strong> is the world's most dermatologist-recommended authentic luxury medical jumbo foaming cleanser from CeraVe designed to clean, clarify, and remove excess oil and makeup for normal to oily facial skin without drying, stinging, or damaging the skin barrier. Built upon 3 Essential Ceramides (1, 3, 6-II), soothing Niacinamide, and Hyaluronic Acid.</p>
<p>CeraVe Foaming Cleanser deeply purifies facial pores of accumulated sebum and impurities, reduces oily shine, and soothes and balances skin moisture, leaving your face touchably silky soft, spotlessly clean, refreshed, and protected against breakouts from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Gentle Foaming Cleansing for Oil & Sebum Control:</strong> Cleanses pores effectively without stripping natural oils.</li>
  <li><strong>Skin Barrier Restoration with 3 Essential Ceramides:</strong> Replenishes natural facial skin ceramides.</li>
  <li><strong>Soothing Care & Shine Control with Niacinamide:</strong> Regulates sebum production while calming redness.</li>
  <li><strong>Internal Hydration Locking with Hyaluronic Acid:</strong> Prevents post-wash tightness and dryness.</li>
  <li><strong>100% Fragrance-Free, Oil-Free & Paraben-Free:</strong> Non-comedogenic formula that will not clog pores.</li>
  <li><strong>Generous 473ml Jumbo Pump Value Bottle:</strong> Outstanding value for daily continuous family use.</li>
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
  <li>Anyone with normal to oily skin seeking CeraVe Foaming Cleanser 473ml for jumbo pore cleansing and oil control.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>CeraVe</td></tr>
  <tr><th>Category</th><td>Skincare / CeraVe Medical Foaming Cleansers 473ml</td></tr>
  <tr><th>Product Type</th><td>Fragrance-Free Oil-Free Ceramide & Niacinamide Foaming Cleanser (473ml)</td></tr>
  <tr><th>Volume/Weight</th><td>473 ml</td></tr>
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
        ("What is CeraVe Foaming Facial Cleanser for Normal to Oily Skin - 473ml?", "It is a medical jumbo fragrance-free oil-free foaming cleanser from CeraVe with Ceramides and Niacinamide for normal to oily skin (473ml)."),
        ("What are the benefits of Niacinamide and 3 essential Ceramides?", "Niacinamide regulates oil and soothes irritation, while Ceramides restore the facial skin barrier and prevent dryness."),
        ("Does it clean pores and control oil shine without dryness?", "Yes, clinically proven to clean pores and reduce excess shine without tightness or dryness."),
        ("What volume is contained in this bottle?", "473ml jumbo pump dispenser bottle."),
        ("How do I use it correctly?", "Wet face, apply gel, lather, massage gently and rinse with warm water twice daily."),
        ("Is it fragrance-free, oil-free, and paraben-free?", "Yes, 100% free from fragrances, oils, and parabens, and dermatologically tested."),
        ("Where is CeraVe Foaming Cleanser manufactured?", "By CeraVe LLC (L'Oréal Group)."),
        ("How do I verify authenticity at Ekleel Abha?", "All CeraVe products at Ekleel Abha are 100% original."),
        ("Is it suitable for normal, oily, and acne-prone skin?", "Yes, excellent for normal, oily, combination, and acne-prone skin."),
        ("Does it leave face matte and clean?", "Yes, leaves face matte, oil-free, spotlessly clean, and silky soft."),
        ("Is the 473ml jumbo pump bottle convenient?", "Yes, generous jumbo pump dispenser bottle ideal for daily family use."),
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
        "product_id": "2102",
        "sku": "EK-2102",
        "gtin": "3337875597357",
        "brand": "CeraVe",
        "ar": {
            "title": "رغوة تنظيف البشرة العادية والدهنية  من سيرافي 473مل",
            "meta_title": "رغوة سيرافي للبشرة العادية والدهنية 473مل | إكليل أبها",
            "meta_description": "اشتري رغوة تنظيف البشرة العادية إلى الدهنية من سيرافي (473 مل). غسول طبي جامبو بالسيراميدات والنياسيناميد لتصفية المسام وتقليل الدهون. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["سيرافي", "رغوة_سيرافي_جامبو", "غسول_البشرة_الدهنية_473مل", "سيرافي_473مل", "إكليل_أبها"]
        },
        "en": {
            "title": "CeraVe Foaming Facial Cleanser for Normal to Oily Skin - 473ml",
            "meta_title": "CeraVe Foaming Facial Cleanser 473ml | Ekleel Abha",
            "meta_description": "Buy original CeraVe Foaming Facial Cleanser for Normal to Oily Skin (473ml). Fragrance-free oil-control ceramide jumbo cleanser. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["cerave", "cerave_foaming_cleanser_473ml", "jumbo_cerave_wash", "ceramide_cleanser", "ekleel_abha"]
        }
    }


def create_product_2103():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم ايس كولد كير للترطيب والانتعاش لليد والجسم من كوفيكس 275 مل (Cofix Ice Cold Care Moisturizing and Refreshing Cream - 275 ml)</strong> كريم الترطيب والانتعاش المبرد الفاخر الأصيل من كوفيكس (Cofix Care) المصمم خصيصاً لترطيب، إنعاش، وتهدئة بشرة اليدين والجسم الجافة والمجهدة وإطفاء سخونة البشرة بفعل الحرارة والشمس. يرتكز هذا الكريم الأصيل (Cofix Ice Cold 275ml) على خلاصة المنتهول المبردة (Cooling Menthol)، زبدة الشيا، والمركبات المطرية لبشرة الجسم.</p>
<p>يعمل كريم كوفيكس أيس كولد على نفاذ السائل المبرد لعمق مسام اليد والجسم، حفظ الرطوبة لـ 24 ساعة دون أي أثر دهني لزج، وإضفاء بريق ونعومة حريرية ممتدة، ليترك جسمك ويديك في غاية النعومة، المرونة، ومفعمين بالانتعاش البرودي الثلجي من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وانتعاش برودي ثلجي ممتد لـ 24 ساعة:</strong> يطفئ سخونة الجلد ويمنح الانتعاش.</li>
  <li><strong>كريم متعدد الأغراض لليدين والجسم معاً:</strong> يغذي البشرة الجافة ويمنع الشد والتقشر.</li>
  <li><strong>امتصاص فوري دون ترك أثر دهني ثقيل:</strong> مناسب للاستخدام اليومي السريع.</li>
  <li><strong>تهدئة التهيجات والاحمرار بفعل الحرارة والشمس:</strong> بفضل خلاصة المنتهول المبردة.</li>
  <li><strong>تركيبة خفيفة آمنة ومختبرة جلدياً:</strong> خالية من البارابين والمواد القاسية.</li>
  <li><strong>عبوة سعة 275 مل مزودة بضاغط مريح:</strong> حجم ممتاز للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسبة من كريم كوفيكس على بشرة اليدين والجسم النظيفة.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي برفق بحركات دائرية ناعمة حتى الامتصاص الكامل (يُستعمل يومياً صباحاً ومساءً وعند الحاجة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة المنتهول المبردة والمركبات المطرية:</strong> تمنحان شعوراً بالانتعاش الثلجي وتنعيش اليدين والجسم.</li>
  <li><strong>زبدة الشيا والجليسرين:</strong> تحفظان التوازن المائي للجلد وتمنحان نعومة فائقة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة اليدين والجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن كريم كوفيكس أيس كولد كير 275 مل للانتعاش المبرد والترطيب الفائق لليدين والجسم.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كوفيكس (Cofix Care)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم واليدين / كريمات كوفيكس المبردة والمرطبة 275ml</td></tr>
  <tr><th>نوع المنتج</th><td>كريم مرطب طبي مبرد بالمنثول لليدين والجسم (275ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>275 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة اليدين والجسم (الجافة، العادية والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>يدين وجسم ناعمين كالحرير، مرطبين 24 ساعة، ناصعين النظافة وغير دهنيين</td></tr>
  <tr><th>الملمس</th><td>كريم جل ناعم خفيف يمتص فورياً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر النعناع والمنثول الثلجي المنعش الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة المنتهول المبردة، زبدة الشيا، جليسرين مرطب</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية (KSA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Cofix Care Products</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد خلاصة المنتهول المبردة وزبدة الشيا في كريم كوفيكس (Cofix Ice Cold Cream)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم كوفيكس أيس كولد مشكلة جفاف اليدين والجسم، سخونة الجلد بالحر الصيفي، والطبقة الدهنية المزعجة.</p>

<h3>لماذا تنجح تركيبة Cofix Ice Cold Cream?</h3>
<p>لأن المنتهول المبرد يتصاعد بالبشرة محفزاً المستقبلات الثلجية بينما تغذي زبدة الشيا الأنسجة الجافة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق فوراً بعد الاستحمام والغسيل:</strong> يضاعف امتصاص المرطب المبرد.<br>
2. <strong>التركيز على اليدين والكوعين:</strong> يحمي من التصلب والخشونة.<br>
3. <strong>الاستخدام اليومي المنتظم:</strong> يمنح نضارة وانتعاشاً ثلجياً دائمين.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الكريمات المبردة تسبب تحسس البشرة الجافة."<br>
<strong>الحقيقة:</strong> كريم كوفيكس مدعم بزبدة الشيا والجليسرين لحفظ التوازن المائي للجلد دون أي تحسس.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>ينشط المنتهول مستقبلات TRPM8 الثلجية بينما تندمج زبدة الشيا مع الدهون السطحية الحامية للجلد.</p>"""

    faqs = [
        ("ما هو كريم ايس كولد كير للترطيب والانتعاش لليد والجسم من كوفيكس 275 مل؟", "هو كريم مرطب ومبرد بالمنثول وزبدة الشيا لليدين والجسم من كوفيكس بحجم 275 مل."),
        ("ما هي فوائد خلاصة المنتهول المبردة وزبدة الشيا؟", "ترطب اليدين والجسم لـ 24 ساعة، تطشئ حرارة الجلد الصيفية، وتمتص فورياً دون دهنية."),
        ("هل يمتص فورياً ويرطب لـ 24 ساعة مع إحساس بالبرودة؟", "نعم، مثبت سريرياً في الامتصاص السريع والترطيب 24 ساعة وتوفير انتعاش ثلجي."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة مزودة بضاغط مريح سعة 275 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على اليدين والجسم، دلكي برفق حتى الامتصاص مرتين يومياً وعند الحاجة."),
        ("هل هو آمن وخالٍ من البارابين؟", "نعم، 100% آمن ومختبر جلدياً ومناسب لجميع أنواع البشرة."),
        ("أين صُنع كريم كوفيكس أيس كولد؟", "صُنع في المملكة العربية السعودية بواسطة Cofix Care Products."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كوفيكس لدى إكليل أبها أصلية 100%."),
        ("ما رائحة كريم كوفيكس أيس كولد؟", "عطر النعناع والمنثول الثلجي المنعش الفاخر."),
        ("هل يناسب اليدين والجسم معاً؟", "نعم، كريم متعدد الأغراض ممتاز لبشرة اليدين والجسم."),
        ("هل عبوة 275 مل بضاغط مريحة؟", "نعم، عبوة أنيقة بضاغط مريح جداً للاستخدام اليومي والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كوفيكس علامة موثوقة في العناية الشخصية؟", "نعم، Cofix علامة سعودية رائدة وموثوقة جداً في المستحضرات الشخصية."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً أو حسب الحاجة."),
        ("هل يمنح البشرة لمعاناً ونعومة حريرية؟", "نعم، يمنح البشرة توهجاً طبيعياً ونعومة حريرية دون دهنية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في الوقاية من خشونة وسخونة اليدين؟", "نعم، يبرد اليدين وينعم الجلد ويحمي من الخشونة."),
        ("هل يترك ملمساً لزجاً؟", "ينفذ فورياً دون ترك لزوجة أو ثقل."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال والرياضيين."),
        ("هل يناسب الاستخدام في الصيف والشتاء؟", "ممتاز جداً في الصيف ولجميع الأوقات الحارة وبعد الرياضة."),
        ("هل يصلح هدية ممتازة؟", "نعم، منتج عناية وتبريد مفيد وأنيق."),
        ("هل يعيد المظهر الصحي والمشرق للبشرة؟", "نعم، يمنح الجسد واليدين مظهراً ناعماً ومشرقاً."),
        ("هل يسهل ارتداء الملابس فوراً بعده؟", "نعم، يمتص سريعاً مما يتيح ارتداء الملابس فوراً دون بقع."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Cofix Ice Cold Care Moisturizing and Refreshing Cream - 275 ml</strong> is an authentic luxury cooling hydrating body and hand cream from Cofix Care designed to moisturize, refresh, and soothe dry and heat-stressed skin while relieving sun and summer heat. Built upon cooling Menthol Extract, Shea Butter, and skin-moisturizing compounds.</p>
<p>Cofix Ice Cold Cream deeply penetrates hand and body skin, locks in hydration for 24 hours without a heavy greasy film, and imparts a silky soft luster, leaving your hands and body touchably soft, flexible, and refreshed with an icy menthol feeling from first touch.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>24-Hour Icy Menthol Cooling & Hydration:</strong> Quenches skin heat delivering instant coolness.</li>
  <li><strong>Multi-Purpose Formulation for Hands & Body:</strong> Nourishes dry skin preventing tightness and flaking.</li>
  <li><strong>Instant Rapid Absorption with Zero Heavy Greasy Residue:</strong> Ideal for daily care and immediate dressing.</li>
  <li><strong>Soothes Sun & Heat Irritation:</strong> Calms skin redness using cooling menthol.</li>
  <li><strong>Dermatologically Tested Safe Formula:</strong> Free from parabens and harsh chemicals.</li>
  <li><strong>Convenient 275ml Pump Value Bottle:</strong> Excellent size for daily care and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of Cofix cream onto clean hand and body skin.</li>
  <li><strong>Step 2:</strong> Massage gently in smooth circular motions until fully absorbed (use daily morning, night & as needed).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Cooling Menthol Extract & Emollients:</strong> Deliver an icy mint sensation refreshing hands and body.</li>
  <li><strong>Shea Butter & Glycerin:</strong> Preserve skin moisture balance delivering extreme touchable softness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hand and body skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Cofix Ice Cold Care Cream 275ml for cooling hydration and skin softness for hands and body.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Cofix Care</td></tr>
  <tr><th>Category</th><td>Body & Hand Care / Cofix Cooling Hydrating Creams 275ml</td></tr>
  <tr><th>Product Type</th><td>Cooling Menthol & Shea Butter Hydrating Hand & Body Cream (275ml)</td></tr>
  <tr><th>Volume/Weight</th><td>275 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hand & Body Skin Types (Dry, Normal & Oily Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, refreshed & non-greasy clear skin</td></tr>
  <tr><th>Texture</th><td>Ultra-lightweight fast-absorbing smooth gel-cream</td></tr>
  <tr><th>Fragrance</th><td>Invigorating fresh icy mint menthol scent</td></tr>
  <tr><th>Active Ingredients</th><td>Cooling Menthol Extract, Shea Butter, Hydrating Glycerin</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia (KSA)</td></tr>
  <tr><th>Manufacturer</th><td>Cofix Care Products</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Menthol TRPM8 Cooling & Shea Butter Lipid Replenishment</h2>

<h3>What problem does this solve?</h3>
<p>Cofix Ice Cold Cream resolves hand and body dryness, summer skin heat, roughness, and greasy lotion residue.</p>

<h3>Why choose Cofix Ice Cold Care Cream?</h3>
<p>Menthol activates TRPM8 cooling receptors delivering instant thermal relief while shea butter nourishes dry cells.</p>"""

    en_faqs = [
        ("What is Cofix Ice Cold Care Moisturizing and Refreshing Cream - 275 ml?", "It is a cooling hydrating hand and body cream from Cofix with Menthol and Shea Butter (275ml)."),
        ("What are the benefits of Menthol Extract and Shea Butter?", "Hydrate hands and body for 24 hours, quench skin heat, and absorb rapidly without greasiness."),
        ("Does it absorb instantly and hydrate for 24 hours with a cooling sensation?", "Yes, clinically proven to absorb rapidly and hydrate for 24 hours with icy menthol coolness."),
        ("What volume is contained in this bottle?", "275ml pump dispenser bottle."),
        ("How do I use it correctly?", "Apply to clean hands and body, massage gently until absorbed twice daily as needed."),
        ("Is it safe and paraben-free?", "Yes, 100% safe, dermatologically tested, and suitable for all skin types."),
        ("Where is Cofix Ice Cold Cream manufactured?", "In Saudi Arabia by Cofix Care Products."),
        ("How do I verify authenticity at Ekleel Abha?", "All Cofix products at Ekleel Abha are 100% original."),
        ("What scent does Cofix Ice Cold Cream have?", "Invigorating fresh icy mint menthol fragrance."),
        ("Is it suitable for hands and body together?", "Yes, multi-purpose cream excellent for hand and body skin."),
        ("Is the 275ml pump bottle convenient?", "Yes, sleek pump dispenser bottle ideal for daily care and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Cofix a trusted brand in Saudi Arabia?", "Yes, Cofix is a leading trusted brand in personal care in KSA."),
        ("How many times daily?", "Once or twice daily or as needed."),
        ("Does it impart shine and silky softness?", "Yes, gives hands and body natural glow and silky softness without greasiness."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help prevent skin roughness and heat?", "Yes, cools hands and body protecting skin from dryness and roughness."),
        ("Does it leave a sticky residue?", "Absorbs instantly without sticky residue or heavy feeling."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it good for summer and sports?", "Yes, ideal for summer heat, workouts, and sports routines."),
        ("Is it a nice gift?", "Yes, practical and thoughtful cooling body care gift."),
        ("Does it restore healthy radiant skin appearance?", "Yes, gives hands and body skin a healthy smooth radiant look."),
        ("Can I get dressed immediately after application?", "Yes, fast absorption allows immediate dressing without staining clothes."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2103",
        "sku": "EK-2103",
        "gtin": "697794487249",
        "brand": "Cofix",
        "ar": {
            "title": "كريم ايس كولد كير للترطيب والانتعاش لليد والجسم من كوفيكس  275 مل",
            "meta_title": "كريم كوفيكس أيس كولد كير لليد والجسم 275مل | إكليل أبها",
            "meta_description": "اشتري كريم أيس كولد كير للترطيب والانتعاش لليد والجسم من كوفيكس (275 مل). كريم طبي مبرد بالمنثول وزبدة الشيا لترطيب اليدين والجسم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كوفيكس", "كريم_كوفيكس_أيس_كولد", "ترطيب_اليدين_والجسم", "كريم_مبرد_بالمنثول", "إكليل_أبها"]
        },
        "en": {
            "title": "Cofix Ice Cold Care Moisturizing and Refreshing Cream - 275 ml",
            "meta_title": "Cofix Ice Cold Care Cream 275ml | Ekleel Abha",
            "meta_description": "Buy original Cofix Ice Cold Care Moisturizing and Refreshing Cream (275ml). Cooling menthol & shea butter hand and body cream. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["cofix", "ice_cold_cream", "cofix_hand_body_cream", "cooling_cream", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 76 builders complete")
