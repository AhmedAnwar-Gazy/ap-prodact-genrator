import json, os

def create_product_1743():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>لوشن نيفيا لترطيب الجسم بخلاصة الصبار المنعش (NIVEA Aloe Vera Body Moisturizing Lotion - 400ml)</strong> الخيار الأمثل للحصول على بشرة ناعمة ورطبة طوال اليوم. يدمج هذا اللوشن المتطور بين القوة المرطبة لسيروم الترطيب العميق (Deep Moisture Serum) وخلاصة الصبار الطبيعي النقية، حيث يتغلغل بسرعة في طبقات الجلد ليمنحكِ 72 ساعة من الترطيب المستمر والانتعاش الفوري دون أي ملمس زيتي.</p>
<p>صُمم اللوشن ليناسب البشرة العادية إلى الجافة، حيث يعيد توازن رطوبة الجلد، يقلل المظهر الخشن والجاف، ويترك البشرة مفعمة بالحيوية والنعومة المخملية بعطر الصبار الكلاسيكي المنعش.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب عميق يدوم 72 ساعة:</strong> معزز بسيروم الترطيب العميق لحبس الماء داخل طبقات الجلد.</li>
  <li><strong>بخلاصة الصبار الطبيعي:</strong> يهدئ البشرة المتهيجة ويزودها بانتعاش ورطوبة مائية فورية.</li>
  <li><strong>امتصاص سريع وغير دهني:</strong> يتغلغل فورياً داخل الأنسجة دون ترك لزوجة أو أثر زيتي.</li>
  <li><strong>تنعيم وتلطيف البشرة الجافة:</strong> يزيل خشونة الجلد ويترك الجسم ناعماً كالحرير.</li>
  <li><strong>مناسب للبشرة العادية والجافة:</strong> تركيبة متوازنة ومجربة جلدياً تناسب الاستخدام اليومي.</li>
  <li><strong>عبوة اقتصادية 400 مل:</strong> حجم مناسب للاستخدام المنتظم لجميع أفراد العائلة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> استحممي بالماء الفاتر وجففي جسمكِ بلطف بمنشفة ناعمة.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية مناسبة من لوشن نيفيا بالصبار على كف اليد.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> وزعي اللوشن ودلكيه بحركات دائرية على كامل الجسم حتى يتم امتصاصه كاملاً.</li>
  <li><strong>الخطوة الرابعة (الاستمرارية):</strong> يُفضل استخدامه يومياً بعد الاستحمام للحفاظ على رطوبة ممتدة.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة الصبار (Aloe Barbadensis Leaf Juice):</strong> تلطف الجلد وتمنحه ترطيباً مائياً مهدئاً.</li>
  <li><strong>سيروم الترطيب العميق (Deep Moisture Serum):</strong> تركيب ذكي يحبس الرطوبة داخل الخلايا لـ 72 ساعة.</li>
  <li><strong>الهيالورونيك (Sodium Hyaluronate):</strong> يجذب جزيئات الماء لزيادة مرونة الجلد ونضارته.</li>
  <li><strong>الجليسرين:</strong> يمنع تبخر الماء من السطح الخارجي للبشرة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الجسم فقط.</li>
  <li>تجنبي ملامسة اللوشن المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من جفاف جلد الجسم وترغب في ترطيب مائي خفيف يدوم 72 ساعة بخلاصة الصبار.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>نيفيا (NIVEA)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / لوشن وترطيب الجسم</td></tr>
  <tr><th>نوع المنتج</th><td>لوشن ترطيب الجسم بخلاصة الصبار (Aloe & Hydration)</td></tr>
  <tr><th>الحجم/الوزن</th><td>400 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة العادية إلى الجافة</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة، مرطبة، خالية من اللمعان والدهون</td></tr>
  <tr><th>الملمس</th><td>لوشن سائل خفيف سريع الامتصاص</td></tr>
  <tr><th>العطر</th><td>عطر الصبار والنعناع المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة الصبار، سيروم الترطيب العميق، هيالورونات الصوديوم، جليسرين</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا / الإمارات (Beiersdorf)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beiersdorf (نيفيا)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الصبار وسيروم الترطيب العميق (NIVEA)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج لوشن نيفيا بالصبار مشكلة جفاف وشحوب جلد الجسم والخشونة الناتجة عن فقدان رطوبة الليبيدات السطحية.</p>

<h3>لماذا يحدث الجفاف؟</h3>
<p>يتسبب الاستحمام بالماء الساخن والطقس الجاف في تبخر رطوبة الجلد، مما يجعل البشرة مشدودة وخشنة وتظهر بها قشور دقيقة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الترطيب بعد الاستحمام فوراً:</strong> وضعي اللوشن والجلد ما زال رطباً لحبس الماء.<br>
2. <strong>الاستخدام المنتظم:</strong> استعملي اللوشن يومياً للحصول على نتائج 72 ساعة.<br>
3. <strong>التركيز على المناطق الجافة:</strong> دلكي الساقين والذراعين بعناية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "لوشنات الجسم تترك ملمساً دهنياً مزعجاً."<br>
<strong>الحقيقة:</strong> لوشن نيفيا بالصبار يمتص في ثوانٍ بفضل السيروم المائي الخفيف دون لزوجة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتغلغل خلاصة الصبار والهيالورونيك داخل الخلايا القرنية، بينما يشكل سيروم نيفيا شبكة ترطيب تحفظ توازن الماء ومنع تبخره (TEWL) لـ 72 ساعة.</p>"""

    faqs = [
        ("ما هو لوشن نيفيا لترطيب الجسم بخلاصة الصبار؟", "هو لوشن مرطب للجسم يحتوي على خلاصة الصبار وسيروم الترطيب العميق لمنح البشرة 72 ساعة من الترطيب الانتعاشي."),
        ("ما فائدة الصبار وسيروم الترطيب العميق؟", "يهدئ الصبار الجلد ويمنحه رطوبة مائية، بينما يحبس السيروم الترطيب داخل الخلايا."),
        ("هل يترك اللوشن ملمساً زيتيّاً؟", "لا، يتميز بقوام سائل خفيف ينفذ بسرعة دون أي لزوجة."),
        ("ما حجم العبوة؟", "تأتي بحجم 400 مل."),
        ("هل يناسب البشرة الجافة والعادية؟", "نعم، صُمم خصيصاً للبشرة العادية والجافة."),
        ("كم تدوم فاعلية الترطيب؟", "تدوم حتى 72 ساعة من الترطيب المنتظم."),
        ("ما هو بلد صنع نيفيا؟", "صُنع بواسطة شركة باييرسدورف (Beiersdorf) العالمية."),
        ("هل يناسب الاستخدام اليومي؟", "نعم، آمن وممتاز للاستخدام اليومي بعد الاستحمام."),
        ("هل يناسب الرجال والنساء؟", "نعم، يناسب كلا الجنسين ولجميع الأعمار."),
        ("ما هي رائحة اللوشن؟", "يتميز برائحة الصبار المنعشة والناعمة."),
        ("هل يساعد في تهدئة الجلد بعد الشمس؟", "نعم، خلاصة الصبار تبرد وتهدئ الاحمرار."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات نيفيا لدى إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يحتوي على هيالورونيك؟", "نعم، مدعم بهيالورونات الصوديوم لزيادة المرونة."),
        ("هل يناسب الأطفال؟", "مناسب من سن 12 سنة فما فوق."),
        ("هل يترك أي أثر على الملابس؟", "لا، يمتص بالكامل ولا يترك أثراً."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل يقلل خشونة الساقين؟", "نعم، ينعم الجلد الخشن ويمنحه ملمساً حريرياً."),
        ("هل يحتوي على بارابين؟", "التركيبة مطورة وآمنة جلدياً."),
        ("هل يمكن استخدامه للوجه؟", "مخصص للجسم، للوجه يُفضل كريم نيفيا المخصص للوجه."),
        ("هل العبوة 400 مل سهلة الاستخدام؟", "تأتي بتصميم ضغط مريح وسهل."),
        ("هل يمنع تشقق الجلد صيفاً وشتاءً؟", "نعم، يحمي الجلد في كافة الفصول."),
        ("هل يلزم دلكه كثيراً؟", "يدلك بلطف وينفذ بسرعة."),
        ("هل يساعد في إعطاء نضارة للبشرة الباهتة؟", "نعم، يعيد للبشرة حيويتها ونضارتها."),
        ("هل يحتاج للشطف؟", "لا، هو لوشن مخصص للبقاء على البشرة."),
        ("هل يناسب كبار السن؟", "نعم، يغذي بشرة كبار السن ويحميها من الجفاف.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>NIVEA Aloe Vera Body Moisturizing Lotion (400ml)</strong> is your daily secret to soft, hydrated, and refreshed skin. Combining NIVEA's breakthrough Deep Moisture Serum with pure natural Aloe Vera extract, it penetrates rapidly into skin layers to deliver 72 hours of non-stop hydration and instant cooling freshness without any greasy residue.</p>
<p>Tailored for normal to dry skin types, it restores skin moisture balance, smoothes rough skin patches, and leaves your body touchably soft and delicately scented with a fresh aloe aroma.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>72-Hour Deep Moisture:</strong> Enriched with Deep Moisture Serum to seal in water hydration.</li>
  <li><strong>Natural Aloe Vera Infusion:</strong> Soothes skin flaring and provides instant cooling moisture.</li>
  <li><strong>Fast-Absorbing & Non-Greasy:</strong> Absorbs in seconds without tacky or oily residue.</li>
  <li><strong>Smooths Dry Skin:</strong> Eliminates rough skin texture, leaving it silky soft.</li>
  <li><strong>Ideal for Normal to Dry Skin:</strong> Dermatologically safety-tested formula safe for daily family use.</li>
  <li><strong>Economical 400ml Family Bottle:</strong> Provides extended daily hydration for months.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Shower with warm water and pat skin dry gently.</li>
  <li><strong>Step 2 (Apply):</strong> Dispense lotion into palms.</li>
  <li><strong>Step 3 (Massage):</strong> Smooth gently in circular motions over your whole body until absorbed.</li>
  <li><strong>Step 4 (Daily Routine):</strong> Use daily after showering for maximum 72-hour softness.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Aloe Vera Extract (Aloe Barbadensis):</strong> Soothes skin and provides refreshing cooling hydration.</li>
  <li><strong>Deep Moisture Serum:</strong> Binds water molecules deep within dermal layers for 72 hours.</li>
  <li><strong>Sodium Hyaluronate:</strong> Boosts skin elasticity and moisture retention.</li>
  <li><strong>Glycerin:</strong> Prevents surface transepidermal water loss.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external body application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with normal to dry skin seeking a 72-hour refreshing, fast-absorbing Aloe Vera body lotion.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>NIVEA</td></tr>
  <tr><th>Category</th><td>Skincare / Body Lotions</td></tr>
  <tr><th>Product Type</th><td>72H Deep Moisture Aloe Vera Body Lotion</td></tr>
  <tr><th>Volume/Weight</th><td>400 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Normal to Dry Skin</td></tr>
  <tr><th>Finish</th><td>Soft, hydrated, radiant & non-greasy skin</td></tr>
  <tr><th>Texture</th><td>Lightweight fast-absorbing fluid lotion</td></tr>
  <tr><th>Fragrance</th><td>Fresh classic Aloe Vera fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Aloe Vera Extract, Deep Moisture Serum, Hyaluron, Glycerin</td></tr>
  <tr><th>Country of Origin</th><td>Germany / UAE (Beiersdorf)</td></tr>
  <tr><th>Manufacturer</th><td>Beiersdorf (NIVEA)</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Deep Moisture Serum & Aloe Hydration</h2>

<h3>What problem does this solve?</h3>
<p>NIVEA Aloe Vera Body Lotion resolves skin tightness, roughness, and flaking caused by environmental dryness and lipid loss.</p>

<h3>Why does this condition happen?</h3>
<p>Hot showers and low humidity evaporate water from the stratum corneum, creating dry, rough patches.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Moisturize Post-Shower:</strong> Apply immediately after bathing to lock in moisture.<br>
2. <strong>Daily Care:</strong> Use daily for 72-hour continuous hydration.<br>
3. <strong>Target Dry Areas:</strong> Massage extra lotion into dry arms and legs.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Body lotions leave a sticky oil film."<br>
<strong>Fact:</strong> NIVEA Aloe Lotion absorbs in seconds thanks to its lightweight water-serum formulation.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Aloe Vera and Sodium Hyaluronate penetrate dermal layers, while NIVEA's Deep Moisture Serum forms a breathable moisture barrier, preventing TEWL for up to 72 hours.</p>"""

    en_faqs = [
        ("What is NIVEA Aloe Vera Body Lotion?", "It is a moisturizing body lotion with Aloe Vera and Deep Moisture Serum delivering 72 hours of non-greasy hydration."),
        ("What are the benefits of Aloe Vera and Deep Moisture Serum?", "Aloe cools and soothes skin, while the serum seals in water for 72 hours."),
        ("Does it feel greasy?", "No, it absorbs in seconds without leaving sticky or oily residue."),
        ("What volume is contained in this bottle?", "It comes in a generous 400ml bottle."),
        ("Is it suitable for normal to dry skin?", "Yes, it is specially formulated for normal to dry skin types."),
        ("How long does hydration last?", "It delivers up to 72 hours of continuous hydration."),
        ("Where is NIVEA manufactured?", "It is produced by Beiersdorf under global quality standards."),
        ("Is it suitable for daily use?", "Yes, safe and ideal for daily post-shower application."),
        ("Can men and women use it?", "Yes, it is a unisex body lotion."),
        ("What scent does it have?", "It features a clean, fresh Aloe Vera fragrance."),
        ("Does it help soothe sun-exposed skin?", "Yes, Aloe Vera cools and calms sun-exposed skin redness."),
        ("How do I verify authenticity at Ekleel Abha?", "All NIVEA products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it contain Hyaluronic Acid?", "Yes, it is enriched with Sodium Hyaluronate for elasticity."),
        ("Is it suitable for teenagers?", "Yes, safe for adults and teens aged 12+."),
        ("Does it stain clothing?", "No, it absorbs fully leaving zero residue."),
        ("How should I store the bottle?", "Store in a cool, dry place away from heat."),
        ("Does it smooth rough legs and arms?", "Yes, it smooths rough skin patches, leaving them silky soft."),
        ("Is it paraben-free?", "Yes, modern NIVEA formulas are dermatologically safety-tested."),
        ("Can it be applied to the face?", "It is formulated for the body; NIVEA face creams are recommended for facial skin."),
        ("Is the 400ml bottle easy to handle?", "Yes, it features an ergonomic dispenser bottle."),
        ("Does it prevent year-round skin dryness?", "Yes, it protects skin against winter and summer dryness."),
        ("Does it require heavy rubbing?", "No, it massages gently and absorbs rapidly."),
        ("Does it restore dull skin radiance?", "Yes, deep moisture restores natural healthy skin glow."),
        ("Does it require rinsing?", "No, it is a leave-on body lotion."),
        ("Is it suitable for seniors?", "Yes, it nourishes aging skin and guards against dryness.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1743",
        "sku": "EK-1743",
        "gtin": "4005900490612",
        "category": "العناية بالبشرة / لوشن وترطيب الجسم",
        "brand": "NIVEA",
        "ar": {
            "title": "لوشن نيفيا لترطيب الجسم بخلاصة الصبار المنعش - 400 مل",
            "meta_title": "لوشن نيفيا بالصبار لترطيب الجسم 400مل | صيدلية إكليل أبها",
            "meta_description": "اشتري لوشن نيفيا لترطيب الجسم بخلاصة الصبار المنعش وسيروم الترطيب العميق (400مل). 72 ساعة ترطيب بدون ملمس دهني. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["نيفيا", "لوشن_نيفيا", "ترطيب_الصبار", "لوشن_الجسم", "إكليل_أبها"]
        },
        "en": {
            "title": "NIVEA Aloe Vera Body Moisturizing Lotion - 400ml",
            "meta_title": "NIVEA Aloe Vera Body Lotion 400ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy NIVEA Aloe Vera Body Lotion (400ml). 72H hydration with Deep Moisture Serum & Aloe. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["nivea", "aloe_lotion", "body_lotion", "skincare", "ekleel_abha"]
        },
        "schema": {
            "brand": "NIVEA",
            "category": "Skincare / Body Lotion",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "nivea-aloe-vera-body-moisturizing-lotion-400ml.webp",
            "alt": "NIVEA Aloe Vera Body Moisturizing Lotion 400ml",
            "title": "NIVEA Aloe Vera Body Moisturizing Lotion 400ml"
        }
    }

def build_powder_product(prod_id, name_en, name_ar, main_ing_en, main_ing_ar, gtin, img_slug):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>{name_ar} (100% Natural Powder - {name_en})</strong> الوصفة الطبيعية التقليدية الفاخرة المخصصة للعناية المتكاملة بجمال الوجه والجسم. تعتمد هذه البودرة النقية على خصائص {main_ing_ar} الاستثنائية، حيث توفر تفتيحاً آمناً للبشرة، تنقية للمسام من الدهون، وتوحيداً للون التصبغات الداكنة في الأكواع والركبتين والمناطق الجافة.</p>
<p>تتميز الفرمولة بكونها طبيعية 100% خالية من المواد الكيميائية والعطور، مما يتيح لكِ دمجها بسهولة مع ماء الورد، الزبادي، أو حمام المغربي لصنع أقنعة وتفتيح وتنعيم مذهلة تنعش حيوية ونضارة بشرتكِ من التطبيق الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>طبيعية ونقية 100%:</strong> بودرة نقية خالية من الإضافات الكيميائية والمواد الحافظة والعطور.</li>
  <li><strong>تفتيح وتوحيد لون البشرة:</strong> تقلل التصبغات والبقع الداكنة وتكسب الوجه والجسم إشراقة متجانسة.</li>
  <li><strong>تنقية المسام والحد من الدهون:</strong> تمتص الشوائب والزيوت الزائدة وتطهر المسام العميقة.</li>
  <li><strong>تقشير وتنعيم لطيف:</strong> تزيل خلايا الجلد الميتة وتمنح البشرة ملمساً مخملياً ناعماً.</li>
  <li><strong>متعددة الاستخدامات والأقنعة:</strong> تخلط بسهولة مع ماء الورد أو الحليب أو الزبادي للحصول على أقنعة تجميلية.</li>
  <li><strong>مناسبة لجميع أنواع البشرة:</strong> تركيبة آمنة ولطيفة تناسب جميع أنواع البشرة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الخلط):</strong> اخلطي ملعقة صغيرة من البودرة مع ماء الورد أو الزبادي للحصول على معجون ناعم.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وزعي المعجون بالتساوي على بشرة الوجه أو الجسم النظيفة.</li>
  <li><strong>الخطوة الثالثة (الانتظار):</strong> اتركي القناع على البشرة لمدة 10 إلى 15 دقيقة حتى يجف خفيفاً.</li>
  <li><strong>الخطوة الرابعة (الشطف):</strong> اشطفي بالماء الفاتر جيداً مع تدليك خفيف لإزالة القناع ورطبي بشرتكِ بعدها.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مستخلص {main_ing_ar} النقي 100%:</strong> غني بالمعادن ومضادات الأكسدة التي توحد اللون وتنقي البشرة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي فقط.</li>
  <li>يُوصى بإجراء اختبار تحسس بسيط قبل الاستخدام الكامل.</li>
  <li>تجنبي ملامسة البودرة للعينين.</li>
  <li>تُحفظ في مكان بارد وجاف بعيداً عن الرطوبة.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تبحث عن وصفة طبيعية 100% لتفتيح الوجه والجسم وتوحيد لون البشرة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>اعشاب طبيعية / صيدلية إكليل أبها</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / البودرة والأقنعة الطبيعية</td></tr>
  <tr><th>نوع المنتج</th><td>{name_ar}</td></tr>
  <tr><th>الحجم/الوزن</th><td>عبوة بودرة نقية</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (الوجه والجسم)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة مشرقة، ناعمة، ومتجانسة اللون</td></tr>
  <tr><th>الملمس</th><td>بودرة ناعمة تتجانس مع السوائل بسهولة</td></tr>
  <tr><th>العطر</th><td>عطر طبيعي خفيف بدون إضافات</td></tr>
  <tr><th>المكونات النشطة</th><td>{main_ing_ar} نقي 100%</td></tr>
  <tr><th>بلد المنشأ</th><td>المغرب / الهند</td></tr>
  <tr><th>الشركة المصنعة</th><td>Natural Herbs Products</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد {main_ing_ar} وتفتيح البشرة (Natural Powder)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج البودرة مشكلة شحوب البشرة، التصبغات، واسمرار الأكواع والركبتين، وتراكم الشوائب الزهمية في المسام.</p>

<h3>لماذا تنجح هذه الوصفة؟</h3>
<p>لأن مكونات {main_ing_ar} تحتوي على مضادات أكسدة ومعادن تمتص الدهون وتحد من تصبغ الميلانين السطحي بفعالية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الخلط مع ماء الورد:</strong> يفضل الخلط مع ماء الورد لزيادة النضارة والتهدئة.<br>
2. <strong>الاستخدام 2-3 مرات أسبوعياً:</strong> داومي على القناع للحصول على تفتيح مستمر.<br>
3. <strong>الترطيب بعد الشطف:</strong> رطبي بشرتكِ فوراً بعد إزالة القناع.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "البودرة الطبيعية تترك لوناً دائماً على البشرة."<br>
<strong>الحقيقة:</strong> الشطف الجيد بالماء ثم المسح بقطنة بماء الورد أو الزيت يزيل أي أثر صبغي مؤقت فورياً.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتمتع البودرة بخصائص امتصاص حيوية للزيوت (Adsorption) ومكونات مضادة للأكسدة تمنع أكسدة صبغة الميلانين وتزيل الخلايا الميتة.</p>"""

    faqs = [
        (f"ما هي {name_ar}؟", f"هي بودرة طبيعية نقية 100% من {main_ing_ar} مصممة لصنع أقنعة تفتيح وتنعيم وتوحيد لون الوجه والجسم."),
        ("ما هي فوائدها للبشرة؟", "تفتح اللون، تزيل البقع، تمتص الدهون، وتنقي المسام العميقة."),
        ("كيف يتم تحضير القناع؟", "اخلطي ملعقة صغيرة من البودرة مع ماء الورد أو الزبادي حتى تحصلي على معجون ناعم وزعيه على البشرة."),
        ("هل يناسب الوجه والجسم معاً؟", "نعم، آمن وممتاز للوجه والأكواع والركبتين والجسم."),
        ("هل يحتوي على أي مواد كيميائية؟", "لا، هو نقي 100% خالي من العطور والمواد الكيميائية."),
        ("كم من الوقت يُترك القناع؟", "يُترك من 10 إلى 15 دقيقة حتى يجف خفيفاً ثم يشطف بالماء."),
        ("هل يترك أثراً ملوّناً مؤقتاً؟", "قد يترك أثراً خفيفاً يزول بالماء أو بمسح البشرة بقطنة بها زيت أو ماء ورد."),
        ("كم مرة يُنصح باستخدامه أسبوعياً؟", "يُنصح باستخدامه من 1 إلى 3 مرات أسبوعياً."),
        ("هل يناسب البشرة الدهنية؟", "ممتاز جداً للبشرة الدهنية لأنه يمتص الدهون الزائدة."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع الأعشاب لدى إكليل أبها أصلية 100% ومستوردة من المصادر الموثوقة."),
        ("هل يساعد في تضييق المسام؟", "نعم، تنظيف الدهون يقلل مظهر المسام الواسعة."),
        ("هل يناسب جميع أنواع البشرة؟", "نعم، مناسب لجميع الأنواع وتُراعى البشرة الحساسة بالتجربة أولاً."),
        ("هل يمكن خلطه مع الحمام المغربي؟", "نعم، ممتاز لدمجه مع الصابون المغربي في الاستحمام."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان جاف بعيداً عن الرطوبة."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب لكلا الجنسين."),
        ("هل يزيل الخلايا الميتة؟", "نعم، يقشر خلايا الجلد الميتة بلطف."),
        ("هل يناسب الأطفال؟", "مناسب من سن 12 سنة فما فوق."),
        ("هل يساعد في تهدئة حب الشباب؟", "مضادات الأكسدة تنقي المسام وتخفف التهابات الحبوب."),
        ("هل يلزم ترطيب البشرة بعده؟", "نعم، يُفضل دائماً الترطيب بعد الأقنعة."),
        ("هل العبوة اقتصادية؟", "نعم، تكفي لصنع عشرات الأقنعة التجميلية."),
        ("هل يمنح تفتيحاً ملحوظاً؟", "نعم، يمنح إشراقة وتفتيحاً ملحوظاً مع الاستمرار."),
        ("هل يمكن خلطه مع الحليب؟", "نعم، خلطه مع الحليب يمنح ترطيباً وتفتيحاً مضاعفاً."),
        ("هل يسبب جفافاً؟", "قد يمتص الدهون، لذا يُفضل الترطيب بعده."),
        ("هل يحتاج لماء دافئ للشطف؟", "يُفضل الشطف بالماء الفاتر ثم البارد لإغلاق المسام."),
        ("هل العبوة محكمة الغلق؟", "نعم، تحفظ البودرة من الرطوبة.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{name_en}</strong> is a traditional 100% pure natural beauty treatment crafted for face and body skin brightening and purification. Harnessing the natural properties of pure {main_ing_en}, it safely lightens hyperpigmentation, absorbs excess sebum, and unifies dark patches on knees, elbows, and face.</p>
<p>Free from synthetic chemicals, preservatives, and fragrances, this 100% pure powder easily mixes with rose water, milk, or yogurt to create custom K-beauty and Moroccan bath facial masks that restore skin radiance and velvet smoothness from the very first application.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Pure Natural Powder:</strong> Free of chemical additives, synthetic fragrances, and preservatives.</li>
  <li><strong>Skin Brightening & Tone Unification:</strong> Fades dark spots and unifies skin tone on face and body.</li>
  <li><strong>Pore Purification & Oil Control:</strong> Absorbs deep pore sebum and environmental impurities.</li>
  <li><strong>Gentle Exfoliation & Softening:</strong> Lifts dead surface skin cells for velvet softness.</li>
  <li><strong>Versatile DIY Mask Base:</strong> Mixes easily with rose water, yogurt, or milk for custom masks.</li>
  <li><strong>Suitable for All Skin Types:</strong> Hypoallergenic natural formula safe for face and body care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Mix):</strong> Mix 1 teaspoon of powder with rose water or yogurt to form a smooth paste.</li>
  <li><strong>Step 2 (Apply):</strong> Spread evenly over clean face or body skin.</li>
  <li><strong>Step 3 (Wait):</strong> Leave on for 10 to 15 minutes until light drying occurs.</li>
  <li><strong>Step 4 (Rinse):</strong> Rinse thoroughly with warm water, gently massaging, then apply moisturizer.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>100% Pure {main_ing_en}:</strong> Rich in minerals and antioxidants that purify skin and unify tone.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application only.</li>
  <li>Perform a patch test prior to full application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Store in a cool, dry place away from humidity.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a 100% pure natural DIY powder mask for facial and body skin brightening.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Generic Herbs / Ekleel Abha Pharmacy</td></tr>
  <tr><th>Category</th><td>Skincare / Natural Powders & Masks</td></tr>
  <tr><th>Product Type</th><td>100% Pure Natural {main_ing_en} Powder</td></tr>
  <tr><th>Volume/Weight</th><td>Pure Powder Container</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Face & Body)</td></tr>
  <tr><th>Finish</th><td>Radiant, even-toned, purified & smooth skin</td></tr>
  <tr><th>Texture</th><td>Fine natural powder blending easily</td></tr>
  <tr><th>Fragrance</th><td>Natural unperfumed herbal scent</td></tr>
  <tr><th>Active Ingredients</th><td>100% Pure {main_ing_en}</td></tr>
  <tr><th>Country of Origin</th><td>Morocco / India</td></tr>
  <tr><th>Manufacturer</th><td>Natural Herbs Products</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Pure {main_ing_en} & Skin Brightening</h2>

<h3>What problem does this solve?</h3>
<p>{name_en} resolves dull skin, hyperpigmentation, rough elbow/knee textures, and clogged pore oils.</p>

<h3>Why choose this treatment?</h3>
<p>Antioxidants and natural minerals in {main_ing_en} adsorb excess sebum and inhibit surface melanin oxidation.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Mix with Rose Water:</strong> Blend with rose water for enhanced soothing hydration.<br>
2. <strong>Regular Masks:</strong> Apply 2-3 times weekly for consistent brightening.<br>
3. <strong>Moisturize After:</strong> Always moisturize skin after rinsing off the mask.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Natural color powders leave permanent skin stains."<br>
<strong>Fact:</strong> Rinsing thoroughly and wiping with a cotton pad dipped in oil or rose water removes temporary tint instantly.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Pure {main_ing_en} exhibits high bio-adsorption capacity for pore sebum, while natural antioxidants neutralize free radicals and exfoliate dead epidermal cells.</p>"""

    en_faqs = [
        (f"What is {name_en}?", f"It is a 100% pure natural powder derived from {main_ing_en} designed for DIY face and body brightening masks."),
        ("What are its skin benefits?", "It brightens complexion, lifts dark spots, absorbs excess oil, and purifies pores."),
        ("How do I prepare the mask?", "Mix 1 teaspoon of powder with rose water or yogurt into a smooth paste and apply to skin."),
        ("Is it safe for face and body?", "Yes, safe and effective for facial skin, knees, elbows, and body."),
        ("Does it contain chemical additives?", "No, it is 100% pure free of synthetic chemicals and perfumes."),
        ("How long should I leave it on?", "Leave on for 10 to 15 minutes until light drying, then rinse with warm water."),
        ("Does it leave temporary skin tinting?", "Any light temporary tinting washes off easily with water or an oil-dipped cotton pad."),
        ("How often should I use it?", "Use 1 to 3 times weekly for best results."),
        ("Is it good for oily skin?", "Yes, it excels at absorbing deep pore oils."),
        ("How do I verify authenticity at Ekleel Abha?", "All natural herbs at Ekleel Abha are 100% authentic from trusted sources."),
        ("Does it help tighten pores?", "Yes, clearing deep sebum refines enlarged pores."),
        ("Is it suitable for all skin types?", "Yes, suitable for all types; perform a patch test for sensitive skin."),
        ("Can it be mixed into Moroccan Hammam soap?", "Yes, it blends perfectly with Moroccan black soap."),
        ("How should I store it?", "Store in a dry place away from ambient humidity."),
        ("Can men and women use it?", "Yes, it is a unisex DIY skin treatment."),
        ("Does it exfoliate dead skin?", "Yes, it gently buffs away dead epidermal cells."),
        ("Is it suitable for teenagers?", "Safe for adults and teens aged 12+."),
        ("Does it help soothe acne?", "Antioxidants purify pores and calm inflammation."),
        ("Should I moisturize afterward?", "Yes, always apply moisturizer after rinsing off natural mask treatments."),
        ("Is it economical?", "Yes, one jar provides dozens of DIY mask treatments."),
        ("Does it provide noticeable brightening?", "Yes, regular use reveals noticeable complexion radiance."),
        ("Can I mix it with milk?", "Yes, mixing with milk enhances hydration and brightening."),
        ("Does it dry out skin?", "It absorbs oil, so following with moisturizer is recommended."),
        ("What water temperature should I use for rinsing?", "Rinse with lukewarm water followed by a cool water splash."),
        ("Is the container securely sealed?", "Yes, it comes in a moisture-proof sealed jar.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "العناية بالبشرة / البودرة والأقنعة الطبيعية",
        "brand": "Generic Herbs",
        "ar": {
            "title": name_ar,
            "meta_title": f"{name_ar} | صيدلية إكليل أبها",
            "meta_description": f"اشتري {name_ar} الطبيعية النقية 100% لتفتيح البشرة وتنقيتها. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بودرة_طبيعية", "تفتيح_البشرة", "اقنعة_طبيعية", "إكليل_أبها"]
        },
        "en": {
            "title": name_en,
            "meta_title": f"{name_en} | Ekleel Abha Pharmacy",
            "meta_description": f"Buy 100% Pure Natural {name_en} for DIY skin brightening and pore purification. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["natural_powder", "skin_brightening", "diy_mask", "ekleel_abha"]
        },
        "schema": {
            "brand": "Generic Herbs",
            "category": "Skincare / Natural Powder",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"{img_slug}.webp",
            "alt": name_en,
            "title": name_en
        }
    }

def create_product_1746():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>مبخرة الشعر الذكية من OVAST (OVAST Smart Hair Incense Burner)</strong> الابتكار العصري الأكثر فخامة وسهولة لتعطير الشعر والجسم بالبخور والعود دون عناء الفحم والحرارة التقليدية. تعتمد هذه المبخرة الإلكترونية الذكية على تقنية التسخين السيراميكي المتقدم السريع، حيث تبخر العود والمنتجات العطرية بفاعلية وثبات عالي، مع توزيع الدخان بالتساوي عبر مشط الشعر المدمج المخصص.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>مبخرة شعر وجسم إلكترونية ذكية:</strong> تعطر الشعر والجسم بالبخور والعود بثبات وأمان دون الحاجة للفحم.</li>
  <li><strong>تقنية تسخين سيراميكي سريع:</strong> تسخن البخور بفاعلية وتخرج الدخان العطري في ثوانٍ معدودة.</li>
  <li><strong>مشط مخصص لتوزيع البخور:</strong> يوزع الدخان العطري بين خصلات الشعر من الجذور حتى الأطراف.</li>
  <li><strong>شحن USB لاسلكي:</strong> بطارية قابلة للشحن تدوم لعدة استخدامات ومثالية للمنزل والسفر.</li>
  <li><strong>آمنة تماماً على الشعر:</strong> تحمي الشعر من الاحتراق أو الحرارة المفرطة بتصميم ذكي.</li>
  <li><strong>تصميم عصري وفاخر:</strong> عبوة أنيقة تشمل ملحقات متعددة ورأسين للتبخير.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الشحن والتحضير):</strong> اشحني المبخرة كلياً بكابل USB المرفق، وضعي قطعة بخور أو عود صغيرة في غرفة التسخين.</li>
  <li><strong>الخطوة الثانية (التشغيل):</strong> ثبتي مشط الشعر أو رأس التبخير العام، ثم اضغطي زر التشغيل لعدة ثوانٍ.</li>
  <li><strong>الخطوة الثالثة (التبخير):</strong> مرري المشط بلطف بين خصلات الشعر ليتغلغل الدخان العطري بالكامل.</li>
  <li><strong>الخطوة الرابعة (الإيقاف):</strong> اغلقي المبخرة واتركيها تبرد قبل التنظيف.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>غرفة تسخين سيراميكية (Ceramic Heating Chamber):</strong> توزع الحرارة بأمان ودون إحراق البخور.</li>
  <li><strong>مشط توزيع دقيق:</strong> مصنوع من مواد مقاومة للحرارة لتصفيف وتبخير الشعر.</li>
  <li><strong>بطارية ليثيوم قابلة للشحن:</strong> سريعة الشحن وتدوم لاستخدامات متعددة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي لتبخير الشعر والجسم والملابس فقط.</li>
  <li>يُمنع غمر المبخرة بالماء؛ تُنظف غرفة البخور بفرشاة جافة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة ورجل يبحثون عن وسيلة سهلة وآمنة وعصرية لتعطير الشعر والجسم بالبخور والعود.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>أوفاست (OVAST)</td></tr>
  <tr><th>الفئة</th><td>أجهزة التجميل / مبخرة الشعر الذكية</td></tr>
  <tr><th>نوع المنتج</th><td>مبخرة شعر وجسم إلكترونية قابلة للشحن (Smart Hair Incense Burner)</td></tr>
  <tr><th>الحجم/الوزن</th><td>جهاز مبخرة مدمج مع ملحقاته</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر والملابس والجسم</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر معطر بالعود والبخور بثبات وأمان</td></tr>
  <tr><th>الملمس</th><td>جهاز إلكتروني أنيق بمقبض مريح</td></tr>
  <tr><th>العطر</th><td>تتبخر برائحة البخور والعود المفضل لديكِ</td></tr>
  <tr><th>المكونات النشطة</th><td>غرفة سيراميك، بطارية ليثيوم، مشط حراري</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين</td></tr>
  <tr><th>الشركة المصنعة</th><td>OVAST Technology</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 15 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لتقنية مبخرة الشعر الذكية والتسخين السيراميكي (OVAST)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تحل مبخرة OVAST الذكية مشكلة خطر احتراق الشعر أو الملابس بالفحم التقليدي وصعوبة توزيع البخور بين خصلات الشعر.</p>

<h3>لماذا تنجح هذه المبخرة؟</h3>
<p>لأنها تعتمد على تسخين سيراميكي آمن يخرج الدخان العطري عبر مشط حراري مخصص يتغلغل بين جذور الشعر دون حرارة مفرطة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الشحن التام قبل الاستخدام:</strong> اشحني الجهاز بالكامل بـ USB لضمان حرارة ثابتة.<br>
2. <strong>تنظيف غرفة السيراميك:</strong> نظفي بقايا البخور بفرشاة جافة فور تبريد الجهاز.<br>
3. <strong>الاستخدام مع البخور الجاف:</strong> استعملي العود الطبيعي الجاف وتجنبي الزيوت السائلة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "المبخرة الإلكترونية تحرق الشعر وتتلف أطرافه."<br>
<strong>الحقيقة:</strong> التسخين السيراميكي الذكي بالحرارة المنضبطة يثبت البخور دون تعرض الشعر للجمر أو الحرق.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يقوم عنصر السيراميك (PTC Ceramic Element) بتسخين الرقائق العطرية في العود بدرجة حرارة ثابتة، مما يحرر الدخان العطري دون إنتاج ثاني أكسيد الكربون أو انبعاث حرارة مفرطة.</p>"""

    faqs = [
        ("ما هي مبخرة الشعر الذكية من OVAST؟", "هي مبخرة إلكترونية شمسية ذكية قابلة للشحن عبر USB مصممة لتبخير وتعطير الشعر والجسم بالبخور والعود ب أمان دون فحم."),
        ("كيف تعمل المبخرة الذكية؟", "تعتمد على غرفة تسخين سيراميكية تسخن البخور بضغط زر وتخرج الدخان العطري عبر مشط مخصص للشعر."),
        ("هل المبخرة آمنة على الشعر ولا تسبب احتراقه؟", "نعم، آمنة تماماً وتحمي الشعر من الحرارة المفرطة ولا تستخدم أي جمر أو فحم."),
        ("هل تأتي مع شاحن USB؟", "نعم، تأتي مع كابل شحن USB وبطارية ليثيوم تدوم لعدة استخدامات."),
        ("ما الملحقات المرفقة مع المبخرة؟", "تأتي مع مشط خاص بالشعر، رأس تبخير للملابس والجسم، ملقط بخور، فرشاة تنظيف، وكابل شحن."),
        ("هل يمكن استخدامها لتبخير الملابس والجسم؟", "نعم، تأتي مع رأس إضافي لتبخير الملابس والجسم والمكان بسهولة."),
        ("ما نوع البخور المناسب للمبخرة؟", "يناسبها العود الطبيعي والقطع الصغيرة من البخور الجاف."),
        ("ما هو بلد صنع مبخرة OVAST؟", "صُنعت بتقنية إلكترونية عالية الجودة."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع الأجهزة لدى إكليل أبها أصلية 100% ومضمونة من الوكلاء المعتمدين."),
        ("كم مدة الشحن المطلوبة؟", "تشحن خلال 1 إلى 2 ساعة وتعمل لعدة مرات."),
        ("كيف يتم تنظيف المبخرة؟", "تُنظف غرفة السيراميك بفرشاة التنظيف المرفقة بعد أن تبرد تماماً دون استخدام الماء."),
        ("هل المبخرة سهلة الحمل بالسفر؟", "نعم، مدمجة وحجمها مثالي لحملها في الحقيبة والسفر."),
        ("هل تخرج دخاناً كثيفاً؟", "نعم، تخرج دخاناً عطرياً كثيفاً يثبت في الشعر لساعات طويلة."),
        ("هل تناسب الرجال والنساء؟", "نعم، ممتازة لتبخير شعر ولحية الرجال وشعر النساء."),
        ("هل تفصل المبخرة تلقائياً؟", "نعم، تحتوي على نظام أمان ذكي يفصل التسخين تلقائياً بعد فترة للتبريد."),
        ("هل يمكن استخدام الزيوت العطرية بها؟", "مخصصة للبخور الصلب والعود الجاف فقط وتجنبي السوائل."),
        ("ما لون الجهاز؟", "تأتي بتصميم أسود/ذهبي أنيق وفاخر."),
        ("هل الضمان شامل؟", "نعم، تشمل ضمان صيدلية إكليل أبها ضد عيوب التصنيع."),
        ("هل تسبب رائحة حريق؟", "لا، التسخين السيراميكي يبخر البخور بصورة صافية دون رائحة احتراق الفحم."),
        ("كيف أحتفظ بالجهاز؟", "يُحفظ في مكان جاف داخل علبته المخصصة."),
        ("هل الوزن خفيف؟", "نعم، خفيفة الوزن ومريحة في قبضة اليد."),
        ("هل هي هادئة الصوت؟", "نعم، تعمل بهدوء تام دون أي ضوضاء."),
        ("هل يصلح إهداؤها؟", "نعم، تعتبر هدية فاخرة وممتازة لجميع المناسبات."),
        ("هل المشط سهل الفك والتركيب؟", "نعم، المشط ورأس التبخير يركبان وينزعان بسهولة شديدة."),
        ("هل تناسب جميع أنواع الشعر؟", "نعم، تناسب الشعر الناعم، الكيرلي، والكثيف.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>OVAST Smart Hair Incense Burner</strong> is the ultimate modern electronic solution for safely infusing your hair, body, and clothes with the rich fragrance of bakhoor and oud without traditional charcoal or fire risks. Powered by a rapid ceramic heating element and a rechargeable USB battery, it releases aromatic incense smoke evenly through a specially designed hair comb attachment.</p>
<p>Extremely safe, portable, and elegant, the OVAST burner protects hair strands from heat damage while ensuring long-lasting scent retention from root to tip. Complete with interchangeable attachments for hair and body misting, it is your essential luxury beauty gadget for home and travel.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Smart Electronic Hair & Body Burner:</strong> Safely scents hair and clothing with bakhoor without charcoal.</li>
  <li><strong>Rapid Ceramic Heating Element:</strong> Warms incense quickly to emit rich aromatic smoke in seconds.</li>
  <li><strong>Specialized Hair Comb Attachment:</strong> Distributes incense smoke evenly through hair strands.</li>
  <li><strong>Rechargeable USB Battery:</strong> Cordless operation with long-lasting battery life perfect for travel.</li>
  <li><strong>100% Safe on Hair:</strong> Protects hair cuticles from heat damage with automatic cooling shut-off.</li>
  <li><strong>Luxury Ergonomic Design:</strong> Stylish compact body with interchangeable heads and cleaning kit.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Charge & Load):</strong> Fully charge burner via USB; place a small piece of dry bakhoor in the ceramic chamber.</li>
  <li><strong>Step 2 (Attach & Power):</strong> Secure the comb head attachment, then press and hold the power button.</li>
  <li><strong>Step 3 (Comb Hair):</strong> Gently comb through hair strands to allow fragrant incense smoke to penetrate completely.</li>
  <li><strong>Step 4 (Turn Off):</strong> Turn off and allow device to cool down before cleaning.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Ceramic Heating Chamber:</strong> Distributes safe, controlled heat without burning incense.</li>
  <li><strong>Heat-Resistant Hair Comb Attachment:</strong> Combs hair while releasing incense smoke safely.</li>
  <li><strong>Rechargeable Lithium Battery:</strong> Fast-charging long-life battery system.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external hair, body, and clothes incensing only.</li>
  <li>Do not submerge device in water; clean ceramic chamber with dry brush kit.</li>
  <li>Keep out of reach of young children.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a safe, portable, charcoal-free electronic burner for scenting hair and clothing with bakhoor.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>OVAST</td></tr>
  <tr><th>Category</th><td>Beauty Gadgets / Smart Hair Incense Burners</td></tr>
  <tr><th>Product Type</th><td>Rechargeable Smart Hair Incense Burner</td></tr>
  <tr><th>Volume/Weight</th><td>Compact Electronic Device Kit</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types, Clothes & Body</td></tr>
  <tr><th>Finish</th><td>Fragrant hair infused with long-lasting oud scent</td></tr>
  <tr><th>Texture</th><td>Sleek metallic/plastic ergonomic device</td></tr>
  <tr><th>Fragrance</th><td>Emits fragrance of your chosen Bakhoor/Oud</td></tr>
  <tr><th>Active Ingredients</th><td>Ceramic Heating Core, Lithium Battery, Comb Head</td></tr>
  <tr><th>Country of Origin</th><td>China</td></tr>
  <tr><th>Manufacturer</th><td>OVAST Technology</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens (15+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Ceramic Incense Heating & Fragrance Penetration</h2>

<h3>What problem does this solve?</h3>
<p>The OVAST Smart Hair Incense Burner eliminates charcoal fire hazards, smoke odor burning, and hair damage associated with traditional bakhoor burning.</p>

<h3>Why choose OVAST?</h3>
<p>Controlled ceramic heating vaporizes incense oils cleanly, delivering fragrant smoke through comb teeth to coat hair cuticles safely.</p>"""

    en_faqs = [
        ("What is OVAST Smart Hair Incense Burner?", "It is a rechargeable electronic incense burner with a comb head designed to safely scent hair and clothes with bakhoor without charcoal."),
        ("How does it work?", "It uses a ceramic heating element to warm bakhoor, releasing fragrant smoke through comb teeth into hair."),
        ("Is it safe for hair?", "Yes, it protects hair from excessive heat damage and uses zero charcoal."),
        ("Does it include a USB charger?", "Yes, it includes a USB charging cable and long-lasting lithium battery."),
        ("What accessories are included?", "It includes a hair comb attachment, body/clothes nozzle, cleaning brush, tweezers, and USB cable."),
        ("Can it be used for clothes and body?", "Yes, it includes a specialized nozzle for scenting clothes and body."),
        ("What type of bakhoor should I use?", "Use natural dry oud pieces or solid bakhoor chunks."),
        ("Where is OVAST manufactured?", "It is manufactured under high quality electronic standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All OVAST devices at Ekleel Abha are 100% original with official warranty."),
        ("How long does it take to charge?", "It charges fully in 1 to 2 hours."),
        ("How do I clean it?", "Clean the cooled ceramic chamber with the provided dry cleaning brush."),
        ("Is it portable for travel?", "Yes, its compact cordless design is perfect for travel."),
        ("Does it produce thick fragrant smoke?", "Yes, it produces rich incense smoke that clings to hair for hours."),
        ("Is it suitable for both men and women?", "Yes, ideal for women's hair as well as men's hair and beards."),
        ("Does it feature automatic shut-off?", "Yes, it includes a smart safety timer that shuts off heating automatically."),
        ("Can essential oils be used in it?", "No, use solid dry bakhoor or oud pieces only."),
        ("What color is the device?", "It features an elegant black/gold luxury finish."),
        ("Does it include a warranty?", "Yes, it is backed by Ekleel Abha Pharmacy warranty against defects."),
        ("Does it smell like burning charcoal?", "No, ceramic heating vaporizes pure incense without charcoal burning smells."),
        ("How should I store it?", "Store in its protective box in a cool, dry place."),
        ("Is it lightweight?", "Yes, it is lightweight and comfortable to hold."),
        ("Is it quiet during operation?", "Yes, it operates silently."),
        ("Does it make a good gift?", "Yes, it is a luxurious, popular gift choice."),
        ("Are attachments easy to swap?", "Yes, comb and nozzle attachments twist on and off easily."),
        ("Is it suitable for all hair types?", "Yes, works on straight, wavy, curly, and thick hair.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1746",
        "sku": "EK-1746",
        "gtin": "2022050160242",
        "category": "أجهزة التجميل / مبخرة الشعر الذكية",
        "brand": "OVAST",
        "ar": {
            "title": "مبخرة الشعر الذكية من OVAST",
            "meta_title": "مبخرة الشعر الذكية OVAST | صيدلية إكليل أبها",
            "meta_description": "اشتري مبخرة الشعر الذكية الإلكترونية من OVAST بالبخور والعود بدون فحم. مشك مخصص لتعطير خصلات الشعر بأمان. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["اوفاست", "مبخرة_الشعر", "مبخرة_ذكية", "بخور_الشعر", "إكليل_أبها"]
        },
        "en": {
            "title": "OVAST Smart Hair Incense Burner",
            "meta_title": "OVAST Smart Hair Incense Burner | Ekleel Abha Pharmacy",
            "meta_description": "Buy original OVAST Smart Hair Incense Burner. Charcoal-free rechargeable electronic burner with comb attachment. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["ovast", "hair_burner", "incense_burner", "smart_burner", "ekleel_abha"]
        },
        "schema": {
            "brand": "OVAST",
            "category": "Beauty Gadget / Hair Burner",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "ovast-smart-hair-incense-burner.webp",
            "alt": "OVAST Smart Hair Incense Burner",
            "title": "OVAST Smart Hair Incense Burner"
        }
    }

def create_product_1748():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>صبغة شعر حناء باللون الأسود من فاتيكا (Vatika Henna Hair Color - Black)</strong> الخيار الطبيعي والأمثل لتغطية الشعر الأبيض والشيب بلون أسود غني ولطيف دون التسبب في إجهاد ألياف الشعر. تجمع هذه الصبغة العشبية بين الخواص المغذية والمقوية للحناء الطبيعية (Lawsonia Inermis) ومستخلصات الأعشاب الهندية الشهيرة مثل الأملا والشيكاكاي والنييم، مما يمنحكِ تغطية متكاملة للشيب بنسبة 100% مع لمعان وقوة للشعر من الجذور حتى الأطراف.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تغطية كاملة 100% للشعر الأبيض:</strong> صبغة حناء عشبية تغطي الشيب بلون أسود غني وطبيعي.</li>
  <li><strong>مدعمة بخلاصة الحناء الطبيعية:</strong> تقوي بصلات الشعر وتغلف الألياف لحمايتها من التكسر والتلف.</li>
  <li><strong>خلاصة الأعشاب الثلاثية (أملا، شيكاكاي، نييم):</strong> تغذي فروة الرأس وتمنح الخصلات لمعاناً وحيوية استثنائية.</li>
  <li><strong>خالية من الأمونيا:</strong> تركيبة عشبية لطيفة على الفروة تحافظ على سلامة نسيج الشعر.</li>
  <li><strong>تطبيق سهل في المنزل:</strong> أظرف بودرة مقسمة تخلط مع الماء فقط لتطبيق مريح وسريع.</li>
  <li><strong>مناسبة للرجال والنساء:</strong> مثالية لتغطية الشيب في شعر الرأس بأمان وطبيعية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التحضير):</strong> افرغي ظرف صبغة حناء فاتيكا في وعاء غير معدني واضيفي الماء الفاتر بالتدريج واخلطي للحصول على معجون ناعم.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ارتدي القفازات المرفقة ووزعي معجون الحناء بالتساوي على الشعر الجاف والنظيف مع التركيز على المناطق الشائبة.</li>
  <li><strong>الخطوة الثالثة (الانتظار):</strong> اتركي الحناء على الشعر لمدة 30 دقيقة ليتشرب اللون والتغذية.</li>
  <li><strong>الخطوة الرابعة (الشطف):</strong> اشطفي الشعر جيداً بالماء الفاتر حتى يزول أثر الحناء تماماً وظهر اللون الأسود الطبيعي.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مسحوق أوراق الحناء (Lawsonia Inermis Leaf Powder):</strong> يغلف الشعر برطوبة ولون طبيعي ويقوي البصلات.</li>
  <li><strong>مسحوق ثمار الأملا (Amla):</strong> غني بفيتامين C يمنح الشعر لمعاناً وسواداً غنياً.</li>
  <li><strong>مسحوق الشيكاكاي (Shikakai):</strong> ينظف الفروة بلطف ويعزز مرونة الخصلات.</li>
  <li><strong>خلاصة النييم (Neem):</strong> يطهر الفروة ويحميها من القشرة والتهيج.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على شعر الرأس فقط؛ يُمنع استخدامها لصبغ الحواجب أو الرموش.</li>
  <li>يجب إجراء اختبار تحسس جلدي قبل 48 ساعة من التطبيق.</li>
  <li>تجنبي ملامسة المنتج للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تبحث عن تغطية عشبية آمنة 100% للشيب باللون الأسود دون استخدام أمونيا.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>فاتيكا (Vatika)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / صبغات الشعر العشبية بالحناء</td></tr>
  <tr><th>نوع المنتج</th><td>صبغة شعر حناء عشبية سوداء لتغطية الشيب</td></tr>
  <tr><th>الحجم/الوزن</th><td>أظرف بودرة حناء</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (الشعر الأبيض والشائب)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر أسود غني، لامع، وخالٍ من الشيب 100%</td></tr>
  <tr><th>الملمس</th><td>بودرة تخلط إلى معجون ناعم</td></tr>
  <tr><th>العطر</th><td>عطر الأعشاب والحناء الطبيعي</td></tr>
  <tr><th>المكونات النشطة</th><td>حناء طبيعية، أملا، شيكاكاي، نييم</td></tr>
  <tr><th>بلد المنشأ</th><td>الهند / الإمارات (Dabur)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Dabur International (دابر فاتيكا)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين (الرجال والنساء)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الحناء العشبية وتغطية الشيب (Vatika)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تحل صبغة حناء فاتيكا السوداء مشكلة ظهور الشيب وتلف الشعر الناجم عن الصبغات الكيميائية المحتوية على الأمونيا.</p>

<h3>لماذا تنجح الحناء العشبية؟</h3>
<p>لأن الحناء تعتمد على التغليف الطبيعي لألياف الشعر مع الأعشاب المغذية (أملا وشيكاكاي) التي ترمم الخصلات وتغطي الشيب دون فتح الحراشف بقسوة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>اختبار التحسس:</strong> أوجدي اختبار تحسس بسيط قبل 48 ساعة من التطبيق.<br>
2. <strong>الشطف الجيد:</strong> اشطفي الشعر جيداً بالماء الفاتر حتى يزول أثر المعجون.<br>
3. <strong>ارتداء القفازات:</strong> ارتدي القفازات لحماية الأيدي من التصبغ.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "صبغة الحناء تسبب تساقط الشعر وجفافه."<br>
<strong>الحقيقة:</strong> خلاصة الحناء والأملا تغذي الجذور وتزيد سمك الشعرة وتمنع التساقط المسبب عن التكسر.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتحد جزيئات صبغة اللوسون (Lawsone) الطبيعية بالحناء مع بروتينات الكيراتين قشرية الشعرة، حيث تغلف السطح الخارجي بلون أسود ثابت غني دون فتح المسام بأكسجين أو أمونيا.</p>"""

    faqs = [
        ("ما هي صبغة شعر حناء باللون الأسود من فاتيكا؟", "هي صبغة شعر عشبية تجمع بين الحناء الطبيعية والأعشاب الهندية لتغطية الشيب 100% بلون أسود غني."),
        ("هل تحتوي صبغة حناء فاتيكا على أمونيا؟", "لا، هي خالية تماماً من الأمونيا وتعتمد على مكونات عشبية مغذية."),
        ("ما هي الأعشاب المضافة للحناء؟", "تحتوي على الأملا، الشيكاكاي، والنييم لتغذية الفروة وتقوية الشعر."),
        ("هل تغطي الشعر الأبيض بالكامل؟", "نعم، تضمن تغطية متكاملة 100% للشعر الأبيض والشيب."),
        ("كيف يتم تحضير وتطبيق الحناء؟", "اخلطي ظرف البودرة مع الماء الفاتر حتى يتكون معجون، وزعيه على الشعر 30 دقيقة ثم اشطفي بالماء."),
        ("كم من الوقت تُترك الحناء على الشعر؟", "تُترك لمدة 30 دقيقة فقط ليتشرب الشعر اللون والتغذية."),
        ("هل تناسب الرجال والنساء؟", "نعم، مناسبة لتغطية الشيب لدى الرجال والنساء."),
        ("هل يجوز استخدامها للحواجب أو الرموش؟", "لا، يُمنع استخدامها للحواجب أو الرموش وتُستخدم لشعر الرأس فقط."),
        ("ما هو بلد صنع حناء فاتيكا؟", "صُنعت بواسطة شركة دابر (Dabur) العالمية بالهند والإمارات."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع صبغات فاتيكا لدى صيدلية إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يلزم إجراء اختبار تحسس قبل الاستخدام؟", "نعم، يُنصح دائماً بإجراء اختبار تحسس جلدي قبل 48 ساعة."),
        ("هل تسبب جفافاً للشعر؟", "الأعشاب المغذية والحناء تمنح ترطيباً وتمنع الجفاف المصاحب للصبغات العادية."),
        ("ما هي رائحة صبغة الحناء؟", "تتميز برائحة الأعشاب الطبيعية والناعمة."),
        ("هل يلزم استخدام قفازات؟", "نعم، ينبغي ارتداء القفازات المرفقة لتجنب تصبغ اليدين."),
        ("كم تدوم نتيجة اللون الأسود؟", "يدوم اللون لعدة أسابيع بحسب معدل نمو وغسيل الشعر."),
        ("هل العبوة مقسمة لأظرف؟", "نعم، تأتي في أظرف مقسمة لسهولة الاستخدام المتكرر."),
        ("هل يمكن استخدامها للشعر المسبوغ سابقاً؟", "نعم، توحد لون الشعر وتغطي الشيب والدرجات المتفاوتة."),
        ("هل تمنع تساقط الشعر؟", "تقوية الألياف بالأملا والحناء تمنع التساقط الناجم عن التكسر."),
        ("هل يناسب الأطفال؟", "مناسبة للبالغين والمراهقين من سن 15 سنة فما فوق."),
        ("هل تترك أي بقايا بعد الشطف الجيد؟", "لا، تشطف بسهولة بالماء الفاتر لتترك شعراً لامعاً ونظيفاً."),
        ("كيف أحتفظ بالأظرف المتبقية؟", "تُحفظ في مكان بارد وجاف بعيداً عن الرطوبة."),
        ("هل تزول النتيجة مع الغسيل الأول؟", "لا، اللون ثابتاً يدوم لأسابيع."),
        ("هل يحتاج لخلط أكسجين معها؟", "لا، تخلط بالماء الفاتر فقط دون أكسجين."),
        ("هل تعزز لمعان الشعر الأسود؟", "نعم، تمنح بريقاً كراستالياً وسواداً غنياً."),
        ("هل العبوة اقتصادية؟", "نعم، توفر تغطية عشبية فاخرة بسعر ممتاز.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Vatika Henna Hair Color - Black</strong> provides a safe, natural, herbal solution for 100% gray hair coverage without subjecting hair fibers to chemical stress. Fusing pure natural Lawsonia Inermis (Henna) leaf powder with iconic Ayurvedic herbs including Amla, Shikakai, and Neem, it delivers a rich, natural black shade while nourishing strands from root to tip.</p>
<p>Ammonia-free and easy to mix with water at home, Vatika Henna Hair Color repairs damaged hair cuticles, imparts brilliant shine, and leaves your hair looking rich, healthy, and completely gray-free.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Full Gray Coverage:</strong> Natural herbal henna powder covering gray hair in a rich natural black shade.</li>
  <li><strong>Enriched with Natural Henna:</strong> Strengthens hair roots and coats strands to prevent breakage.</li>
  <li><strong>Triple Ayurvedic Herb Blend (Amla, Shikakai, Neem):</strong> Nourishes the scalp and imparts crystal shine.</li>
  <li><strong>100% Ammonia-Free Formula:</strong> Gentle on scalp and hair shaft integrity.</li>
  <li><strong>Easy Home Mixing:</strong> Single-use sachets mix simply with warm water.</li>
  <li><strong>Unisex Application:</strong> Ideal for men and women seeking natural black hair color.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Mix):</strong> Empty a Vatika Henna sachet into a non-metallic bowl, add warm water gradually, and stir into a smooth paste.</li>
  <li><strong>Step 2 (Apply):</strong> Wear enclosed gloves and apply paste evenly onto clean dry hair, focusing on gray areas.</li>
  <li><strong>Step 3 (Process):</strong> Leave paste on hair for 30 minutes to allow color and herbal nutrient absorption.</li>
  <li><strong>Step 4 (Rinse):</strong> Rinse hair thoroughly with warm water until clear.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Henna Leaf Powder (Lawsonia Inermis):</strong> Natural colorant that coats hair fibers and fortifies roots.</li>
  <li><strong>Amla Fruit Powder (Phyllanthus Emblica):</strong> Rich in Vitamin C, boosting deep black shine.</li>
  <li><strong>Shikakai Powder:</strong> Gently cleanses scalp while improving fiber flexibility.</li>
  <li><strong>Neem Leaf Extract:</strong> Purifies scalp and protects against dandruff irritation.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external application on head hair only; do not use on eyebrows or eyelashes.</li>
  <li>Perform a skin patch test 48 hours prior to full application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking safe, ammonia-free 100% natural herbal gray coverage in a rich black shade.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Vatika</td></tr>
  <tr><th>Category</th><td>Hair Care / Herbal Henna Hair Color</td></tr>
  <tr><th>Product Type</th><td>Ammonia-Free Herbal Black Henna Dye</td></tr>
  <tr><th>Volume/Weight</th><td>Henna Powder Sachets</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Gray & White Hair)</td></tr>
  <tr><th>Finish</th><td>Rich natural black, shiny, gray-free hair</td></tr>
  <tr><th>Texture</th><td>Powder mixing into a smooth paste</td></tr>
  <tr><th>Fragrance</th><td>Natural herbal henna aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Henna, Amla, Shikakai, Neem</td></tr>
  <tr><th>Country of Origin</th><td>India / UAE (Dabur)</td></tr>
  <tr><th>Manufacturer</th><td>Dabur International (Vatika)</td></tr>
  <tr><th>Age Group</th><td>Adults (Men & Women)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Ayurvedic Henna & Ammonia-Free Gray Coverage</h2>

<h3>What problem does this solve?</h3>
<p>Vatika Henna Hair Color resolves white hair visibility and chemical damage caused by ammonia-based synthetic dyes.</p>

<h3>Why choose Herbal Henna?</h3>
<p>Natural Lawsonia molecules bind onto keratin proteins outer sheaths, depositing natural black pigment while Amla and Shikakai strengthen hair elasticity.</p>"""

    en_faqs = [
        ("What is Vatika Henna Hair Color Black?", "It is a natural herbal henna hair dye blending pure henna and Ayurvedic herbs for 100% black gray coverage."),
        ("Is Vatika Henna ammonia-free?", "Yes, it is 100% ammonia-free and relies on nourishing botanical ingredients."),
        ("What herbs are included in the formula?", "It contains Amla, Shikakai, and Neem extracts to nourish hair and scalp."),
        ("Does it cover white hair completely?", "Yes, it provides 100% complete gray and white hair coverage."),
        ("How do I prepare and apply the henna?", "Mix sachet powder with warm water into a paste, apply for 30 minutes, then rinse with water."),
        ("How long should I leave it on hair?", "Leave on for 30 minutes to allow pigment and nutrient absorption."),
        ("Can both men and women use it?", "Yes, it is suitable for men and women."),
        ("Can it be used for eyebrows or eyelashes?", "No, it is strictly formulated for head hair only."),
        ("Where is Vatika Henna manufactured?", "It is manufactured by Dabur International under strict quality controls."),
        ("How do I verify authenticity at Ekleel Abha?", "All Vatika products at Ekleel Abha are 100% genuine from certified Dabur distributors."),
        ("Is a patch test required?", "Yes, always perform a skin allergy patch test 48 hours prior to application."),
        ("Does it cause hair dryness?", "Nourishing herbs prevent dryness commonly associated with chemical dyes."),
        ("What fragrance does it have?", "It features a natural herbal henna scent."),
        ("Are gloves necessary?", "Yes, wear enclosed gloves to prevent temporary hand skin staining."),
        ("How long does the black color last?", "The color stays vibrant for several weeks depending on wash frequency."),
        ("Are sachets individually packed?", "Yes, it comes in convenient single-use sachets."),
        ("Can it be applied to previously dyed hair?", "Yes, it unifies hair tone and covers gray roots."),
        ("Does it reduce hair fall?", "Fortifying fibers with Henna and Amla reduces breakage-induced hair fall."),
        ("Is it suitable for teenagers?", "Suitable for adults and teens aged 15+."),
        ("Does it rinse out cleanly?", "Yes, it rinses out completely with warm water."),
        ("How should I store remaining sachets?", "Store in a cool, dry place away from moisture."),
        ("Does the color wash out in one shower?", "No, it provides lasting permanent hair color."),
        ("Does it require developer or peroxide?", "No, it mixes simply with warm water without developer."),
        ("Does it enhance hair shine?", "Yes, it imparts brilliant black shine and smoothness."),
        ("Is it an economical option?", "Yes, it offers premium herbal gray coverage at an affordable price.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1748",
        "sku": "EK-1748",
        "gtin": "6291069701753",
        "category": "العناية بالشعر / صبغات الشعر العشبية بالحناء",
        "brand": "Vatika",
        "ar": {
            "title": "صبغة شعر حناء باللون الأسود من فاتيكا - لتغطية مثالية للشيب وتغذية طبيعية",
            "meta_title": "صبغة حناء فاتيكا اسود | صيدلية إكليل أبها",
            "meta_description": "اشتري صبغة شعر حناء باللون الأسود من فاتيكا لتغطية الشيب 100% بدون أمونيا. فرمولة بالأملا والشيكاكاي. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["فاتيكا", "حناء_فاتيكا", "صبغة_حناء", "تغطية_الشيب", "إكليل_أبها"]
        },
        "en": {
            "title": "Vatika Henna Hair Color - Black",
            "meta_title": "Vatika Henna Hair Color Black | Ekleel Abha Pharmacy",
            "meta_description": "Buy Vatika Henna Hair Color Black. Ammonia-free 100% natural gray coverage with Amla & Shikakai. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["vatika", "henna_hair_color", "black_henna", "gray_coverage", "ekleel_abha"]
        },
        "schema": {
            "brand": "Vatika",
            "category": "Hair Care / Henna Dye",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "vatika-henna-hair-color-black.webp",
            "alt": "Vatika Henna Hair Color Black",
            "title": "Vatika Henna Hair Color Black"
        }
    }

print("Loaded Batch 10 builders")
