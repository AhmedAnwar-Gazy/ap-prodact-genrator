import json, os

def create_product_2110():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>علاج لمحاربة القمل وبيضه 50 مل (Lice and Nits Treatment - 50 ml)</strong> العلاج الطبي الفاخر الأسطوري الأكثر توصية من الصيدليات (Licener / Licener Single Treatment) المصمم خصيصاً للقضاء التام والنهائي على القمل وبيضه (الصيبان) في جلسة واحدة مدتها 10 دقائق فقط دون تسبيب أي تهيج أو تنفس كيميائي ضار. يرتكز هذا العلاج الأصيل (Lice Treatment 50ml) على خلاصة شجرة النيم الطبيعية (Neem Extract - Neem Extract Liquid)، المكونات الفيزيائية الخانقة للقمل، والتركيبة الخالية 100% من المبيدات الحشرية الكيميائية.</p>
<p>يعمل علاج القمل والصيبان على شلل الخياشيم التنفسية للقمل وتفكيك الغلاف اللاصق لبيض القمل بالكامل، ليترك شعر طفلك وجسم الفروة ناصعي النظافة، خاليين من الحكة والطفيلية، ومحميين بأمان كامل من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>قضاء تام على القمل وبيضه في 10 دقائق وجلسة واحدة:</strong> يقتل القمل والصيبان ميكانيكياً.</li>
  <li><strong>تركيبة خالية 100% من المبيدات الحشرية الكيميائية:</strong> لا تكتسب الطفيليات أي مناعة ضدها.</li>
  <li><strong>آمن ومختبر درماتولوجياً للأطفال والبالغين:</strong> ينظف دون تسبيب أي حرقان بالفروة.</li>
  <li><strong>سهولة الشطف بالماء الدافئ دون بقاء أثر دهني:</strong> ينشطف بسهولة دون الحاجة لشامبو إضافي.</li>
  <li><strong>مرفق بمشط دقيق مخصص لإزالة الصيبان:</strong> يضمن التخلص التام من البيض الميت.</li>
  <li><strong>عبوة سعة 50 مل بحجم مالي ممتاز:</strong> تكفي لعلاج كامل لشعر الطفل.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية كافية من علاج القمل على الشعر الجاف من الجذور حتى الأطراف.</li>
  <li><strong>الخطوة الثانية:</strong> اتركي المحلول على الشعر لمدة 10 دقائق كاملة فقط.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء الدافئ وتمشيط الشعر بمشط القمل المرفق (يُستعمل عند الإصابة وفي جلسة واحدة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة النيم الطبيعية (Neem Extract):</strong> تخنق القمل وتفكك الغلاف الشمعي لبيض القمل.</li>
  <li><strong>المركبات المطرية المائية:</strong> تحفظ طراوة الشعر وتمنع جفافه أثناء العلاج.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على شعر وفروة الرأس فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل أم ولكل من يبحث عن علاج لمحاربة القمل وبيضه 50 مل للتخلص النهائي من القمل والصيبان في 10 دقائق.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لايسنر (Licener / Lice Care)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / مستحضرات علاج القمل والصيبان 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>علاج طبي فيزيائي خالي من المبيدات للقمل وبيضه في 10 دقائق (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل + مشط دقيق</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر والفروة (بشرة الأطفال والبالغين)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناصع النظافة، خالي 100% من القمل وبيضه ومسترد للصحة</td></tr>
  <tr><th>الملمس</th><td>محلول سائل خفيف ينشطف بالماء بسلاسة</td></tr>
  <tr><th>العطر</th><td>عطر عشبي طبيعي ناعم محايد</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة النيم الطبيعية (Neem Extract)، منظفات مائية فيزيائية</td></tr>
  <tr><th>بلد المنشأ</th><td>هولندا / ألمانيا (Germany)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Medical Head Lice Care Inc.</td></tr>
  <tr><th>الفئة العمرية</th><td>الأطفال والبالغون (من عمر سنتين)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد خلاصة النيم الطبيعية في القضاء على القمل وبيضه (Lice Treatment)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مستحضر علاج القمل مشكلة العدوى الطفيلية بالقمل والحكة الشديدة وتلاصق البيض (الصيبان) ببصيلات الشعر.</p>

<h3>لماذا تنجح تركيبة Neem Extract Lice Treatment؟</h3>
<p>لأن خلاصة النيم تسد القنوات التنفسية (Spiracles) للقمل فتخنقه ميكانيكياً وتذيب المادة الصمغية الالتصاقية للبيض.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على شعر جاف بالكامل:</strong> يضمن وصول التركيبة المركزة لخياشيم القمل.<br>
2. <strong>الانتظار 10 دقائق كاملة ثم الشطف:</strong> يكفي لإبادة القمل والصيبان.<br>
3. <strong>تمشيط الشعر بمشط القمل المرفق:</strong> يزيل البيض الميت بالكامل.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "أدوية القمل تتطلب تكرار العلاج لعدة أسابيع متتالية."<br>
<strong>الحقيقة:</strong> هذا العلاج الطبي للقمل يقضي على القمل والبيض من المرة الأولى وفي 10 دقائق فقط دون تكرار.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخترق الزيوت الفيزيائية الشمع الخارجي لجدار القملة مسببة الخنق والانسداد الميكانيكي التام دون مقاومة كيميائية.</p>"""

    faqs = [
        ("ما هو علاج لمحاربة القمل وبيضه 50 مل؟", "هو علاج طبي فيزيائي بخلاصة النيم خالي من المبيدات للقضاء التام على القمل وبيضه في 10 دقائق (50 مل)."),
        ("ما هي فوائد خلاصة النيم والتركيبة الفيزيائية؟", "تخنق القمل ميكانيكياً، تذيب صمغ البيض (الصيبان)، وتمنع اكتساب المقاومة."),
        ("هل يقضي على القمل والصيبان في 10 دقائق وجلسة واحدة؟", "نعم، مثبت سريرياً في القضاء التام على القمل وبيضه في 10 دقائق فقط."),
        ("ما حجم العبوة ومحتوياتها؟", "تأتي بعبوة أنيقة سعة 50 مل + مشط دقيق مجاني."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي على شعر جاف، اتركيه 10 دقائق، اشطفي بالماء الدافئ ومشطي بالمشط المرفق مرة واحدة."),
        ("هل هو خالٍ من المبيدات الحشرية الكيميائية؟", "نعم، 100% خالٍ من المبيدات الحشرية الكيميائية وآمن للأطفال."),
        ("أين صُنع علاج القمل؟", "صُنع في أوروبا وفق أعلى المعايير الطبية للصيدليات."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        ("ما رائحة علاج القمل؟", "عطر عشبي طبيعي ناعم محايد."),
        ("هل يناسب الأطفال والبالغين من عمر سنتين؟", "نعم، ممتاز وآمن للأطفال والبالغين من عمر سنتين فما فوق."),
        ("هل عبوة 50 مل تكفي لعلاج شعر الطفل؟", "نعم، تكفي لعلاج كامل لشعر الطفل أو بالغ."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل هو المستحضر الأكثر توصية في الصيدليات؟", "نعم، علاج القمل بـ 10 دقائق الخيار الطبي الأكثر ثقة وتفضيلاً."),
        ("كم مرة يُستخدم؟", "مرة واحدة فقط لعلاج الإصابة وتكرر بعد 7 أيام إذا لزم الأمر."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، ينشطف بالماء الدافئ بسهولة دون ترك أثر دهني لزج."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يتطلب غسيل شامبو إضافي؟", "لا يتطلب شامبو إضافي، ينشطف بالماء بالكامل."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب البنات والأولاد؟", "نعم، ممتاز للبنات والأولاد."),
        ("هل يمنع تكرار العدوى؟", "نعم، يقضي على البيض والقمل فيمنع التكاثر وتكرار العدوى."),
        ("هل يناسب جميع أنواع الشعر؟", "نعم، ممتاز لجميع أنواع الشعر (الناعم، المجعد، والكثيف)."),
        ("هل يصلح ضمن روتين الصيدلية المنزلية؟", "نعم، منتج علاج أساسي للسلامة والصحة العائلية."),
        ("هل يعيد النقاء والنظافة لفروة الرأس؟", "نعم، يجعل الفروة ناصعة النقاء وخالية من الحكة."),
        ("هل المشط المرفق يساعد في إزالة الصيبان؟", "نعم، مشط دقيق مخصص لإزالة البيض الميت بسلاسة."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Lice and Nits Treatment - 50 ml</strong> is the world's most recommended authentic luxury medical physical lice and nit treatment (Licener / Licener Single Treatment) designed to eliminate head lice and their eggs (nits) in a single 10-minute application without chemical toxicity or harsh odors. Built upon natural Neem Extract (Neem Extract Liquid), physical suffocating compounds, and a 100% chemical insecticide-free formula.</p>
<p>Lice and Nits Treatment mechanically suffocates lice respiratory spiracles and breaks down the glue sticking nits to hair shafts, leaving your child's hair and scalp touchably clean, itch-free, and healthy from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Eliminates Head Lice & Nits in 10 Minutes (Single Treatment):</strong> Kills lice and eggs mechanically.</li>
  <li><strong>100% Chemical Insecticide-Free Formula:</strong> Lice cannot develop resistance to it.</li>
  <li><strong>Dermatologically Tested & Safe for Kids and Adults:</strong> Cleanses without causing scalp stinging.</li>
  <li><strong>Easy Rinse Off with Warm Water:</strong> Rinses out smoothly without needing extra shampoo.</li>
  <li><strong>Includes a Fine-Toothed Nit Comb:</strong> Ensures easy removal of dead eggs from hair shafts.</li>
  <li><strong>Compact 50ml Value Bottle:</strong> Sufficient volume for a full head treatment.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a sufficient amount of the treatment onto dry hair from roots to ends.</li>
  <li><strong>Step 2:</strong> Leave the solution on the hair for 10 full minutes only.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and comb out dead lice/nits using the included comb (use once per infestation).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Neem Extract (Neem Extract Liquid):</strong> Suffocates live lice and dissolves nit glue.</li>
  <li><strong>Aqueous Emollients:</strong> Maintain hair softness preventing dryness during treatment.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hair and scalp application only.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Mothers and anyone seeking Lice and Nits Treatment 50ml for single 10-minute complete lice and egg elimination.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Licener / Lice Care</td></tr>
  <tr><th>Category</th><td>Hair Care / Medical Lice & Nit Treatments 50ml</td></tr>
  <tr><th>Product Type</th><td>10-Minute Insecticide-Free Physical Lice & Nit Treatment (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml + Nit Comb</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair & Scalp Types (Children & Adults)</td></tr>
  <tr><th>Finish</th><td>Spotlessly clean, 100% lice-free & nit-free healthy hair and scalp</td></tr>
  <tr><th>Texture</th><td>Liquid fluid solution rinsing smoothly with water</td></tr>
  <tr><th>Fragrance</th><td>100% Mild natural neutral herbal scent</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Neem Extract, Physical Aqueous Cleansers</td></tr>
  <tr><th>Country of Origin</th><td>Netherlands / Germany</td></tr>
  <tr><th>Manufacturer</th><td>Medical Head Lice Care Inc.</td></tr>
  <tr><th>Age Group</th><td>Children & Adults (Ages 2+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Neem Extract Mechanical Suffocation & Nit Chitin Cleavage</h2>

<h3>What problem does this solve?</h3>
<p>Lice and Nits Treatment resolves parasitic head lice infestation, severe scalp itching, and attached egg nits.</p>

<h3>Why choose Neem Extract Lice Treatment?</h3>
<p>Neem extract physically blocks lice breathing spiracles suffocating them while breaking down nit adhesive chitin.</p>"""

    en_faqs = [
        ("What is Lice and Nits Treatment - 50 ml?", "It is a physical 10-minute insecticide-free medical treatment with Neem Extract for complete head lice and nit elimination (50ml)."),
        ("What are the benefits of Neem Extract and physical action?", "Suffocate live lice mechanically, dissolve nit glue, and prevent chemical resistance."),
        ("Does it eliminate lice and nits in 10 minutes in a single treatment?", "Yes, clinically proven to eliminate head lice and nits in a single 10-minute treatment."),
        ("What volume and contents are included?", "50ml compact bottle + free fine-toothed nit comb."),
        ("How do I use it correctly?", "Apply to dry hair, wait 10 minutes, rinse with warm water and comb out with included comb."),
        ("Is it 100% chemical insecticide-free?", "Yes, 100% chemical insecticide-free and safe for children."),
        ("Where is this lice treatment manufactured?", "In Europe to international pharmaceutical standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original."),
        ("What scent does this treatment have?", "Mild natural neutral herbal scent."),
        ("Is it safe for kids and adults aged 2+?", "Yes, safe and effective for children and adults aged 2+."),
        ("Does the 50ml bottle cover a full head treatment?", "Yes, sufficient for a full treatment for a child or adult."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it a top pharmacy recommended lice remedy?", "Yes, 10-minute physical lice treatment is the most trusted medical choice."),
        ("How many times is it used?", "Once per infestation; repeat after 7 days if necessary."),
        ("Does it rinse out easily without extra shampoo?", "Yes, rinses out easily with warm water without extra shampoo."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it leave a greasy film?", "No, rinses completely clean without greasy residue."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for boys and girls?", "Yes, suitable for both boys and girls."),
        ("Does it prevent infestation recurrence?", "Yes, kills eggs and lice preventing reproduction."),
        ("Is it good for all hair types?", "Yes, suitable for fine, curly, and thick hair types."),
        ("Is it a home pharmacy essential?", "Yes, a vital medical essential for family health and safety."),
        ("Does it restore clean healthy scalp condition?", "Yes, leaves scalp spotlessly clean and itch-free."),
        ("Does the included comb remove nits easily?", "Yes, fine-toothed comb removes dead nits smoothly."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>[a]</p>\n".replace("[a]", a) for q, a in en_faqs])

    return {
        "product_id": "2110",
        "sku": "EK-2110",
        "gtin": "4029125066926",
        "brand": "Licener",
        "ar": {
            "title": "علاج لمحاربة القمل وبيضه 50 مل",
            "meta_title": "علاج القمل وبيضه في 10 دقائق 50مل | إكليل أبها",
            "meta_description": "اشتري علاج لمحاربة القمل وبيضه (50 مل). علاج طبي فيزيائي بخلاصة النيم خالي من المبيدات لإبادة القمل والصيبان في 10 دقائق. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["علاج_القمل", "محاربة_القمل_والصيبان", "لايسنر_القمل", "علاج_القمل_10_دقائق", "إكليل_أبها"]
        },
        "en": {
            "title": "Lice and Nits Treatment - 50 ml",
            "meta_title": "Lice and Nits Treatment 10-Min 50ml | Ekleel Abha",
            "meta_description": "Buy original Lice and Nits Treatment (50ml). 10-Minute physical Neem extract insecticide-free lice & nit elimination treatment. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["lice_treatment", "nits_treatment", "licener", "10_min_lice_remedy", "ekleel_abha"]
        }
    }


def _make_somebymi_kit_b78(pid, gtin, ar_title, en_title, ar_name, en_name, ing_ar, ing_en, main_feature_ar, main_feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>{ar_title}</strong> مجموعة العناية المتكاملة بالمرحلة المبتدئة (Starter Kit) الفاخرة الأسطورية الأصيلة من الماركة الكورية الرائدة سوم باي مي (Some By Mi) المصممة خصيصاً لترميم، إصلاح، وتجديد بشرة الوجه وتخليصها من الندبات، أثار الحبوب، التصبغات، والبهتان بفضل التركيبة الكورية المعجزة. تركز هذه المجموعة الأصيلة ({en_title}) على خلاصات {ing_ar} وتتضمن 4 خطوات متكاملة (غسول، تونر، سيروم، وكريم).</p>
<p>تعمل مجموعة سوم باي مي الكورية على ترميم حاجز الجلد المتضرر، تصفية المسام من التصبغات والندب، وتزويد الخلايا بتغذية استثنائية، لتترك بشرة وجهك ناعمة كالحرير، ناصعة الصفاء، موحدة اللون، ومفعمة بالتوهج والنضارة الكورية من الأسبوع الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>مجموعة كورية معجزة متكاملة من 4 خطوات (غسول، تونر، سيروم، كريم):</strong> توفر عناية شاملة مكثفة.</li>
  <li><strong>ترميم وتجديد الخلايا بـ {ing_ar}:</strong> تعالج الندبات وآثار البثور وتوحد اللون.</li>
  <li><strong>تصفية المسام وتقليل التصبغات والبقع الداكنة:</strong> تمنح الوجه إشراقة وتوهجاً ناصعاً.</li>
  <li><strong>ترطيب عميق لـ 24 ساعة دون لزوجة دهنية:</strong> تحفظ التوازن المائي للبشرة.</li>
  <li><strong>مختبرة درماتولوجياً ومناسبة للبشرة الحساسة والمعرضة للمشاكل:</strong> آمنة 100%.</li>
  <li><strong>عبوة مدمجة مثالية لتجربة المجموعة وللسفر والتنقل:</strong> أحجام تجريبية ممتازة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الغسول):</strong> اغسلي الوجه بالغسول ورغويه بالماء الدافئ ثم اشطفي.</li>
  <li><strong>الخطوة الثانية (التونر):</strong> ضعي التونر على قطنة ومسدي الوجه برفق.</li>
  <li><strong>الخطوة الثالثة (السيروم والكرِم):</strong> وزعي قطرات السيروم ثم ادهني الكريم المرطب (يُستعمل مرتين يومياً صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصات {ing_ar}:</strong> ترمم غشاء البشرة المتضرر وتفتح التصبغات وتسرع التجدد الخلوي.</li>
  <li><strong>المركبات النباتية الكورية والنياسيناميد:</strong> تهدئ التهيج وتمنح البشرة توهجاً ناصعاً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والرقبة.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_title} للتجربة والترميم والتفتيح الكوري المعجزة للوجه.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سوم باي مي (Some By Mi Korea)</td></tr>
  <tr><th>الفئة</th><td>العناية بالوجه / مجموعات سوم باي مي الكورية المعجزة 4 قطع</td></tr>
  <tr><th>نوع المنتج</th><td>مجموعة العناية المتكاملة 4 خطوات لتجديد وترميم البشرة بـ {ing_ar}</td></tr>
  <tr><th>الحجم/الوزن</th><td>طقم 4 قطع تجريبية (غسول + تونر + سيروم + كريم)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (خصيصاً المتضررة، المتصبغة، والحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، موحد اللون، ناصع الصفاء ومفعم بالتوهج الكوري (Glass Skin)</td></tr>
  <tr><th>الملمس</th><td>تركيبة خفيفة متدرجة من الجيل والسائل والكريم الناعم</td></tr>
  <tr><th>العطر</th><td>عطر كوري طبيعي منعش لطيف</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصات {ing_ar}، نياسيناميد، مركبات كورية طبيعية</td></tr>
  <tr><th>بلد المنشأ</th><td>كوريا الجنوبية (South Korea)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Some By Mi Co., Ltd. Korea</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد خلاصات {ing_ar} في مجموعة سوم باي مي (Some By Mi Starter Kit)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج مجموعة سوم باي مي الكورية مشكلة ندبات حب الشباب، أثار البثور، عدم توحد لون الوجه، البهتان، والتصبغات.</p>

<h3>لماذا تنجح تركيبة Some By Mi Miracle Starter Kit؟</h3>
<p>لأن دمج الـ 4 خطوات (غسول، تونر، سيروم، كريم) بـ {ing_ar} يمنح خلايا الوجه تجديداً متكاملاً متسلسلاً.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الالتزام بالخطوات الـ 4 بالتسلسل:</strong> يضاعف الامتصاص والنتائج الكورية.<br>
2. <strong>الاستخدام مرتين يومياً (صباحاً ومساءً):</strong> يسرع ترميم الندبات والتصبغات.<br>
3. <strong>استخدام واقي شمس صباحاً:</strong> يحمي نتائج تجديد البشرة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مجموعات العناية متعددة الخطوات تسبب ثقلاً وانسداداً للمسام."<br>
<strong>الحقيقة:</strong> منتجات سوم باي مي الكورية مصممة بقوام مائي خفيف يمتص فورياً دون التسبب في أي انسداد.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تسرع خلاصات {ing_ar} بناء الكولاجين وتخليق ألياف الأدمة مصلحة الندبات التالفة.</p>"""

    faqs_data = [
        (f"ما هي {ar_title}؟", f"هي مجموعة عناية متكاملة 4 خطوات كورية من سوم باي مي بـ {ing_ar} لترميم وتجديد وتفتيح الوجه."),
        (f"ما هي فوائد خلاصات {ing_ar} والخطوات الـ 4؟", "ترمم الندبات، تعالج آثار البثور، تفتح التصبغات، وتمنح الوجه توهج الزجاج (Glass Skin)."),
        ("هل ترمم وتفتح وتجدد الوجه في أسبوعين؟", "نعم، مثبتة سريرياً في ترميم الندبات وتجديد خلايا الوجه وتوحيد اللون."),
        ("ما هي محتويات الطقم؟", "تتضمن 4 قطع تجريبية (غسول، تونر، سيروم، وكريم)."),
        ("كيف تُستخدم بالشكل الصحيح؟", "اغسلي بالغسول، مسدي التونر بقطنة، ضعي قطرات السيروم، وادهني الكريم مرتين يومياً."),
        ("هل هي آمنة للبشرة الحساسة الكورية؟", "نعم، 100% آمنة ومختبرة درماتولوجياً ومناسبة للبشرة الحساسة والمعرضة للمشاكل."),
        ("أين صُنت مجموعة سوم باي مي الكورية؟", "صُنت في كوريا الجنوبية بواسطة Some By Mi Co., Ltd."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات سوم باي مي لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_title}؟", f"عطر كوري طبيعي منعش لطيف بـ {ing_ar}."),
        ("هل تناسب جميع أنواع البشرة؟", "نعم، ممتازة للبشرة الدهنية، الجافة، المختلطة، والحساسة."),
        ("هل حجم العبوة ممتاز للتجربة والسفر؟", "نعم، طقم مدمج مثالي لتجربة المجموعة وللسفر والتنقل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل سوم باي مي الماركة الكورية الأكثر شهرة عالمياً؟", "نعم، Some By Mi الماركة الكورية المعجزة رقم 1 الأكثر تفضيلاً عالمياً."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل تترك أثراً دهنياً لزجاً؟", "لا، تمتص المنتجات الـ 4 بسلاسة دون دهنية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل تساعد في علاج ندبات وآثار حب الشباب؟", "نعم، ترمم ألياف الجلد وتلاشي ندبات وآثار حب الشباب بفاعلية."),
        ("هل تمنح مظهر بشرة الزجاج (Glass Skin)؟", "نعم، تمنح الوجه مظهراً زجاجياً ناعماً ومشرقاً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يناسب الشتاء والصيف؟", "نعم، عناية وتفتيح كوري مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن العناية؟", "نعم، طقم عناية كوري فاخر ومفيد جداً كهدية."),
        ("هل يعيد المظهر الصافي المشرق للوجه؟", "نعم، يمنح الوجه مظهراً ناصع الصفاء والتوهج."),
        ("هل تتوفر مجموعات سوم باي مي الكورية الأخرى؟", "نعم، تتوفر عائلة Some By Mi Miracle Kits كاملة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury Korean 4-step starter kit from world-leading brand Some By Mi designed to repair, renew, and brighten facial skin while fading acne scars, blemishes, dark spots, and dullness using the Korean Miracle formulation. Built upon concentrated {ing_en} extracts across 4 essential steps (cleanser, toner, serum, and cream).</p>
<p>Some By Mi Korean Miracle Starter Kit repairs damaged skin barriers, clarifies pores of hyperpigmentation, and infuses skin cells with intense nourishment, leaving your facial skin touchably silky soft, spotlessly clear, even-toned, and glowing with Korean glass skin radiance from week one.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Complete 4-Step Korean Miracle Routine (Cleanser, Toner, Serum, Cream):</strong> Provides comprehensive care.</li>
  <li><strong>Intensive Cell Repair & Renewal with {ing_en}:</strong> Fades acne scars, blemishes, and evens skin tone.</li>
  <li><strong>Pore Refining & Hyperpigmentation Control:</strong> Delivers an illuminated healthy facial skin glow.</li>
  <li><strong>Deep 24-Hour Hydration without Greasy Weight:</strong> Preserves skin moisture balance.</li>
  <li><strong>Dermatologically Tested Safe for Sensitive Skin:</strong> 100% safe for acne-prone skin.</li>
  <li><strong>Compact Starter Kit Ideal for Travel & Trial:</strong> Perfect introductory trial sizes.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanser):</strong> Wash face with cleanser and warm water, then rinse.</li>
  <li><strong>Step 2 (Toner):</strong> Apply toner onto a cotton pad and sweep gently over face.</li>
  <li><strong>Step 3 (Serum & Cream):</strong> Apply serum drops then smooth on moisturizing cream (use twice daily morning & night).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>{ing_en} Extracts:</strong> Repair damaged skin barriers, brighten dark spots, and accelerate cell turnover.</li>
  <li><strong>Korean Botanical Extracts & Niacinamide:</strong> Calm irritation imparting a glass skin glow.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and neck skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_title} for Korean miracle trial, skin barrier repair, and facial brightening.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Some By Mi Korea</td></tr>
  <tr><th>Category</th><td>Skincare / Some By Mi Korean Miracle 4-Piece Starter Kits</td></tr>
  <tr><th>Product Type</th><td>4-Step Korean Miracle Repair & Brightening Starter Kit with {ing_en}</td></tr>
  <tr><th>Volume/Weight</th><td>4-Piece Trial Kit (Cleanser + Toner + Serum + Cream)</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Specifically Damaged, Hyperpigmented & Sensitive)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, even-toned & radiant Korean Glass Skin</td></tr>
  <tr><th>Texture</th><td>Multi-layered lightweight gel, fluid liquid, and smooth cream</td></tr>
  <tr><th>Fragrance</th><td>100% Fresh natural mild Korean herbal scent</td></tr>
  <tr><th>Active Ingredients</th><td>{ing_en} Extracts, Niacinamide, Korean Botanicals</td></tr>
  <tr><th>Country of Origin</th><td>South Korea</td></tr>
  <tr><th>Manufacturer</th><td>Some By Mi Co., Ltd. Korea</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of {ing_en} Epidermal Regeneration & 4-Step Sequential Absorption</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves acne scars, post-blemish redness, uneven skin tone, dullness, and damaged skin barriers.</p>

<h3>Why choose Some By Mi Miracle Starter Kit?</h3>
<p>Sequential 4-step application with {ing_en} accelerates collagen synthesis fading scars and restoring glass skin clarity.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a luxury 4-step Korean miracle starter kit from Some By Mi with {ing_en} for skin repair, brightening, and renewal."),
        (f"What are the benefits of {ing_en} extracts and the 4 steps?", "Repair acne scars, fade blemishes and dark spots, and impart Korean glass skin radiance."),
        ("Does it repair, brighten, and renew facial skin in weeks?", "Yes, clinically proven to repair damaged skin, accelerate cell turnover, and even skin tone."),
        ("What items are included in this kit?", "Includes 4 trial items (cleanser, toner, serum, and cream)."),
        ("How do I use it correctly?", "Wash face, apply toner with cotton, apply serum drops, and smooth cream twice daily."),
        ("Is it safe for sensitive Korean skin care?", "Yes, 100% safe, dermatologically tested, and suitable for sensitive and acne-prone skin."),
        ("Where is Some By Mi Starter Kit manufactured?", "In South Korea by Some By Mi Co., Ltd."),
        ("How do I verify authenticity at Ekleel Abha?", "All Some By Mi products at Ekleel Abha are 100% original."),
        (f"What scent does {en_title} have?", f"Fresh natural mild Korean herbal fragrance with {ing_en}."),
        ("Is it suitable for all skin types?", "Yes, excellent for oily, dry, combination, and sensitive skin."),
        ("Is the kit trial and travel friendly?", "Yes, compact kit ideal for trial, travel, and handbag."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Some By Mi the #1 Korean miracle brand?", "Yes, Some By Mi is the world's most famous #1 Korean miracle skincare brand."),
        ("How many times daily?", "Twice daily (morning and night)."),
        ("Does it leave a sticky greasy film?", "No, all 4 products absorb smoothly without greasy residue."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it help fade acne scars and blemishes?", "Yes, repairs damaged skin tissue fading acne scars and blemishes effectively."),
        ("Does it deliver Korean Glass Skin radiance?", "Yes, gives facial skin a smooth clear glass skin look."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it good for all seasons?", "Yes, ideal Korean skincare repair for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, an elegant practical Korean skincare gift kit."),
        ("Does it restore clean radiant skin appearance?", "Yes, gives facial skin a clear healthy radiant look."),
        ("Are other Some By Mi kits available?", "Yes, the full Some By Mi Miracle Kits range is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Some By Mi",
        "ar": {
            "title": ar_title,
            "meta_title": f"{ar_title} | إكليل أبها",
            "meta_description": f"اشتري {ar_title}. مجموعة كورية معجزة 4 خطوات بـ {ing_ar} لترميم وتجديد وتفتيح الوجه. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. Korean 4-step miracle starter kit with {ing_en} for skin repair and brightening. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2111():
    return _make_somebymi_kit_b78(
        pid=2111, gtin="8809647390534",
        ar_title="مجموعة تروسيكا الحلزون  لإصلاح البشرة وتجديدها من سوم باي مي  (المعجزة الكوريه)",
        en_title="Some By Mi Snail Truecica Miracle Repair Starter Kit (The Korean Miracle)",
        ar_name="مجموعة تروسيكا الحلزون الكورية من سوم باي مي",
        en_name="Some By Mi Snail Truecica Miracle Repair Kit",
        ing_ar="مفرزات الحلزون الأسود ومركب تروسيكا (Black Snail & Truecica)", ing_en="Black Snail Mucin & Truecica Complex",
        main_feature_ar="مجموعة تروسيكا الحلزون الكورية المعجزة 4 قطع لإصلاح وتجديد البشرة والندب", main_feature_en="Korean 4-step Black Snail Truecica Miracle Repair Starter Kit",
        tags_ar=["سوم_باي_مي", "مجموعة_تروسيكا_الحلزون", "المعجزة_الكورية", "ترميم_الندبات", "إكليل_أبها"],
        tags_en=["some_by_mi", "snail_truecica_kit", "korean_miracle_kit", "snail_mucin_repair", "ekleel_abha"]
    )


def create_product_2112():
    return _make_somebymi_kit_b78(
        pid=2112, gtin="8809647390558",
        ar_title="مجموعة يوجا نياسين لتفتيح وترطيب البشره  سوم باي مي  (المعجزة الكوريه)",
        en_title="Some By Mi Yuja Niacin Brightening and Hydrating Starter Kit (The Korean Miracle)",
        ar_name="مجموعة يوجا نياسين الكورية لتفتيح البشرة من سوم باي مي",
        en_name="Some By Mi Yuja Niacin Starter Kit",
        ing_ar="خلاصة فاكهة اليوجا والنياسيناميد 5% (Yuja Fruit & 5% Niacinamide)", ing_en="Yuja Fruit Extract & 5% Niacinamide",
        main_feature_ar="مجموعة يوجا نياسين الكورية المعجزة 4 قطع لتفتيح وترطيب وتصفية التصبغات", main_feature_en="Korean 4-step Yuja Niacin Brightening & Hydrating Starter Kit",
        tags_ar=["سوم_باي_مي", "مجموعة_يوجا_نياسين", "المعجزة_الكورية", "تفتيح_البشرة_الكوري", "إكليل_أبها"],
        tags_en=["some_by_mi", "yuja_niacin_kit", "korean_brightening_kit", "yuja_starter_kit", "ekleel_abha"]
    )


def create_product_2113():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>ماسكارا ايسينس اي لوف  ، لون اسود (Essence I Love Mascara, Black)</strong> الماسكارا الأسطورية الأكثر مبيعاً وشهرة عالمياً من إيسينس (Essence Cosmetics / Essence I Love Extreme Crazy Volume Mascara) المصممة خصيصاً لمنح رموشك كثافة بركانية فائقة، طولاً ساحراً، ولوناً أسود فاحماً درامياً من اللمسة الأولى دون تكتل أو تساقط. تركز هذه الماسكارا الأصيل (Essence I Love Mascara Black) على فرشاة السيليكون الضخمة المبتكرة (Elastomer Brush) والتركيبة الشمعية السوداء الغنية بكثافة الصبغات.</p>
<p>تعمل ماسكارا إيسينس آي لوف على تغليف كل رمش من الجذور حتى الأطراف، فصل الرموش بدقة متناهية، وإعطائها رفعة وكثافة مضاعفة 10 أضعاف، لتترك عينيك مؤطرتين بنظرة ساحرة، رموش ناعمة كالحرير، ناصعة السواد، ومحمية طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>كثافة بركانية وطول درامي من المسحة الأولى:</strong> تضاعف حجم الرموش بفاعلية أسطورية.</li>
  <li><strong>صبغة سوداء فاحمة ناصعة السواد (Ultra Black Pigment):</strong> تبرز جمال العينين بقوة.</li>
  <li><strong>فرشاة سيليكون ضخمة مبتكرة تفصل الرموش:</strong> تمنع التكتل أو التلاصق المزعج.</li>
  <li><strong>ثبات عالي طوال اليوم دون تساقط أو تلطيخ تحت العين:</strong> مقاومة للتكتل والتلطخ.</li>
  <li><strong>مختبرة طبياً من أطباء العيون وآمنة للعيون الحساسة والعدسات:</strong> لا تسبب تحسس.</li>
  <li><strong>أنبوب أنيق بمظهر وردي وأسود أيقوني:</strong> الماسكارا الأكثر شعبية عالمياً.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي فرشاة ماسكارا إيسينس عند قاعدة الرموش الجافة والنظيفة.</li>
  <li><strong>الخطوة الثانية:</strong> اسحبي الفرشاة بحركة متعرجة (Zig-Zag) لأعلى باتجاه الأطراف لتغطية كاملة.</li>
  <li><strong>الخطوة الثالثة:</strong> كرري الطبقة للحصول على كثافة بركانية درامية إضافية (تُستعمل يومياً وعند المكياج).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الصبغات السوداء الفاحمة والشمع الطبيعي:</strong> يغلفان الرموش بكثافة سوداء ناصعة ومرونة ممتدة.</li>
  <li><strong>البوليمرات المثبتة:</strong> تضمن ثبات الماسكارا طوال اليوم دون تساقط.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي التجميلي على الرموش فقط.</li>
  <li>تجنبي التلامس المباشر لداخل العين واحفظي الغطاء مغلقاً بجدية.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن ماسكارا إيسينس آي لوف باللون الأسود لكثافة وطول درامي أسطوري للرموش.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>إيسينس (Essence Cosmetics)</td></tr>
  <tr><th>الفئة</th><td>مكياج العيون / ماسكارات إيسينس آي لوف الكثيفة 12ml</td></tr>
  <tr><th>نوع المنتج</th><td>ماسكارا تكثيف وتطويل درامية بفرشاة سيليكون ولون أسود فاحم</td></tr>
  <tr><th>الحجم/الوزن</th><td>12 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الرموش (القصيرة، الخفيفة، والمستقيمة) ومستخدمي العدسات</td></tr>
  <tr><th>المظهر النهائي</th><td>رموش كثيفة بركانياً، طويلة، ناصعة السواد ومفصولة دون تكتل</td></tr>
  <tr><th>الملمس</th><td>كريمي شمعي أسود فاحم ينساب بسلاسة على الرموش</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور المهيجة</td></tr>
  <tr><th>المكونات النشطة</th><td>صبغات سوداء فاحمة، شمع الكارنوبا، بوليمرات تكثيف</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا / إيطاليا (Germany)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Cosnova Beauty Germany</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد فرشاة السيليكون والصبغة السوداء الفاحمة في ماسكارا إيسينس (Essence I Love Mascara)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج ماسكارا إيسينس آي لوف مشكلة الرموش الخفيفة، القصيرة، التكتل المزعج بالماسكارات العادية، والتساقط تحت العين.</p>

<h3>لماذا تنجح تركيبة Essence I Love Extreme Crazy Volume Mascara؟</h3>
<p>لأن فرشاة السيليكون الضخمة تلتقط أدق الرموش وتوزع الشمع الأسود بالتساوي دون تكتل.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق بحركة متعرجة من القاعدة للأطراف:</strong> يضمن رفع وتكثيف كل رمش.<br>
2. <strong>إغلاق العبوة بإحكام بعد كل استخدام:</strong> يمنع جفاف الماسكارا.<br>
3. <strong>الإزالة بـ مزيل مكياج عيون مائي أو زيتي:</strong> يحافظ على سلامة الرموش الطبيعية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الماسكارات الرخيصة تسبب تساقط الرموش وتكتلها."<br>
<strong>الحقيقة:</strong> ماسكارا إيسينس الألمانية مختبرة من أطباء العيون وتمنح نتائج تفوق ماسكارات الفئات الباهظة بأمان.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>ترتبط ألياف الشمع الطبيعي بكيراتين الرمش مسببة تضاعف القطر والطول دون أي ثقل.</p>"""

    faqs = [
        ("ما هي ماسكارا ايسينس اي لوف ، لون اسود؟", "هي ماسكارا تكثيف وتطويل درامية بفرشاة سيليكون ولون أسود فاحم من إيسينس (12 مل)."),
        ("ما هي فوائد فرشاة السيليكون الضخمة واللون الأسود الفاحم؟", "تضاعف حجم الرموش بركانياً، تطول الرموش، تفصلها بدقة، وتمنع التكتل والتساقط."),
        ("هل تمنح كثافة وطول بركاني بدون تكتل؟", "نعم، مثبتة سريرياً في منح الرموش كثافة 10 أضعاف وطولاً درامياً دون أي تكتل."),
        ("ما حجم العبوة؟", "تأتي بأنبوب أيقوني سعة 12 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي عند قاعدة الرموش واسحبي بحركة متعرجة لأعلى وكرري الطبقة حسب الرغبة."),
        ("هل هي آمنة ومختبرة من أطباء العيون؟", "نعم، 100% آمنة ومختبرة من أطباء العيون ومناسبة للعيون الحساسة ومستخدمي العدسات."),
        ("أين صُنعت ماسكارا إيسينس آي لوف؟", "صُنعت في أوروبا بواسطة Cosnova Beauty Germany."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات إيسينس لدى إكليل أبها أصلية 100%."),
        ("ما لون ماسكارا إيسينس آي لوف؟", "لون أسود فاحم درامي غني (Black / Ultra Black)."),
        ("هل يناسب الرموش القصيرة والخفيفة؟", "نعم، ممتازة لتكثيف وتطويل الرموش القصيرة والخفيفة والمستقيمة."),
        ("هل أنبوب 12 مل مريح ولطيف بالحقيبة؟", "نعم، أنبوب أنيق ومريح جداً للحقيبة والمكياج اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف مع إغلاق الغطاء بإحكام."),
        ("هل إيسينس آي لوف الماسكارا الأكثر مبيعاً عالمياً؟", "نعم، Essence I Love Mascara الماسكارا الأكثر شهرة مبيعاً وتفضيلاً حول العالم."),
        ("كم مرة يُستخدم؟", "يومياً وأثناء وضع المكياج."),
        ("هل تتساقط تحت العين أثناء اليوم؟", "لا، تركيبة ثابتة لا تتساقط ولا تلطخ أسفل العينين."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل تزال بسهولة بمزيل المكياج؟", "نعم، تزال بسلاسة بمزيل مكياج العيون دون شد الرموش."),
        ("هل تتكتل عند وضع طبقات إضافية؟", "فرشاة السيليكون تضمن فصل الرموش ومنع التكتل حتى مع الطبقات الإضافية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والفتيات؟", "نعم، ممتازة للنساء والفتيات."),
        ("هل يناسب جميع المناسبات والمكياج اليومي؟", "نعم، ممتازة للمكياج اليومي والمناسبات والسهرات."),
        ("هل يصلح هدية ممتازة ضمن المكياج؟", "نعم، منتج مكياج فاخر وأساسي لكل حقيبة مكياج."),
        ("هل يعيد المظهر الدرامي الساحر للعينين؟", "نعم، يمنح العينين نظرة واسعة ورموشاً درامية ناصعة السواد."),
        ("هل تتوفر أنواع ماسكارا إيسينس الأخرى؟", "نعم، تتوفر عائلة Essence Mascaras كاملة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Essence I Love Mascara, Black</strong> is the world's #1 best-selling authentic luxury dramatic volume mascara from Essence Cosmetics (Essence I Love Extreme Crazy Volume Mascara) designed to deliver extreme volcanic volume, dramatic length, and intense deep black color from the very first stroke without clumping or flaking. Built upon an innovative jumbo elastomer silicone brush and a pigmented black wax formulation.</p>
<p>Essence I Love Mascara coats every lash from root to tip, separates lashes precisely, and multiplies volume by 10x, leaving your eyes touchably framed with dramatic length, deep black color, and defined fan-like lashes all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Extreme Volcanic Volume & Dramatic Length:</strong> Multiplies lash volume effectively with a single coat.</li>
  <li><strong>Ultra-Black Deep Pigment Color:</strong> Defines and enhances eye beauty intensely.</li>
  <li><strong>Innovative Jumbo Elastomer Silicone Brush:</strong> Separates lashes preventing clumping or sticking.</li>
  <li><strong>Long-Lasting Smudge-Proof & Flake-Free Hold:</strong> Resists smudging under the eyes all day.</li>
  <li><strong>Ophthalmologically Tested & Safe for Sensitive Eyes:</strong> Safe for contact lens wearers.</li>
  <li><strong>Iconic Black & Pink Tube Container:</strong> World's most popular affordable luxury mascara.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Place the Essence mascara brush at the base of clean dry eyelashes.</li>
  <li><strong>Step 2:</strong> Sweep brush upwards in a zig-zag motion to coat lashes from root to tip.</li>
  <li><strong>Step 3:</strong> Apply an additional coat for extra dramatic volcanic volume (use daily with makeup).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Deep Black Pigments & Natural Waxes:</strong> Coat lashes in deep black color and flexible volume.</li>
  <li><strong>Long-Wear Polymers:</strong> Ensure all-day smudge-free hold without flaking.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on eyelashes.</li>
  <li>Avoid direct contact inside the eyes and keep cap tightly closed after use.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Essence I Love Mascara Black for extreme volcanic volume, length, and deep black color.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Essence Cosmetics</td></tr>
  <tr><th>Category</th><td>Eye Makeup / Essence I Love Volume Mascaras 12ml</td></tr>
  <tr><th>Product Type</th><td>Extreme Volcanic Volume & Length Deep Black Silicone Brush Mascara (12ml)</td></tr>
  <tr><th>Volume/Weight</th><td>12 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Eyelash Types (Short, Sparse & Straight Lashes) & Contact Lens Wearers</td></tr>
  <tr><th>Finish</th><td>Volcanic volume, dramatically lengthened, deep black & clump-free separated lashes</td></tr>
  <tr><th>Texture</th><td>Rich smooth deep-black creamy wax gliding easily</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (irritant-free)</td></tr>
  <tr><th>Active Ingredients</th><td>Deep Black Pigments, Carnauba Wax, Volumizing Polymers</td></tr>
  <tr><th>Country of Origin</th><td>Germany / Italy</td></tr>
  <tr><th>Manufacturer</th><td>Cosnova Beauty Germany</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Elastomer Silicone Lash Separation & Deep Black Polymer Coating</h2>

<h3>What problem does this solve?</h3>
<p>Essence I Love Mascara resolves short sparse lashes, clumping from ordinary mascaras, and under-eye smudging.</p>

<h3>Why choose Essence I Love Mascara?</h3>
<p>The jumbo elastomer silicone brush captures fine short lashes depositing deep black wax evenly without clumping.</p>"""

    en_faqs = [
        ("What is Essence I Love Mascara, Black?", "It is an extreme volcanic volume and length mascara with a silicone brush and deep black pigment from Essence (12ml)."),
        ("What are the benefits of the jumbo silicone brush and deep black color?", "Multiply lash volume 10x, lengthen lashes, separate precisely, and prevent clumping or smudging."),
        ("Does it deliver volcanic volume and dramatic length without clumping?", "Yes, clinically proven to multiply lash volume and deliver dramatic length without clumping."),
        ("What volume is contained in this tube?", "12ml iconic mascara tube."),
        ("How do I use it correctly?", "Place at lash base, sweep upwards in zig-zag motion, and re-apply for extra volume."),
        ("Is it safe and ophthalmologically tested?", "Yes, 100% safe, ophthalmologically tested, and suitable for sensitive eyes and contact lens wearers."),
        ("Where is Essence Mascara manufactured?", "In Europe by Cosnova Beauty Germany."),
        ("How do I verify authenticity at Ekleel Abha?", "All Essence products at Ekleel Abha are 100% original."),
        ("What color is Essence I Love Mascara?", "Deep intense dramatic black (Black / Ultra Black)."),
        ("Is it suitable for short and sparse lashes?", "Yes, excellent for volumizing and lengthening short, sparse, and straight lashes."),
        ("Is the 12ml tube handbag friendly?", "Yes, sleek iconic tube ideal for makeup bags and daily use."),
        ("How should I store it?", "In a cool, dry place with cap tightly closed."),
        ("Is Essence I Love Mascara a #1 global best-seller?", "Yes, Essence I Love Mascara is the world's #1 most popular best-selling mascara."),
        ("How many times is it used?", "Daily with makeup routines."),
        ("Does it flake or smudge under the eyes?", "No, long-wearing smudge-proof formula stays put all day without flaking."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it remove easily with makeup remover?", "Yes, removes smoothly with eye makeup remover without tugging lashes."),
        ("Does it clump with additional coats?", "Elastomer silicone brush separates lashes preventing clumping even with extra coats."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and teens?", "Yes, suitable for both women and teens."),
        ("Is it good for daily wear and special occasions?", "Yes, ideal for daily makeup, events, and evening looks."),
        ("Is it a nice makeup gift?", "Yes, an essential premier makeup gift for every cosmetic bag."),
        ("Does it restore dramatic eye beauty?", "Yes, gives eyes a wide framed dramatic deep black lash look."),
        ("Are other Essence mascaras available?", "Yes, the full Essence Mascara range is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2113",
        "sku": "EK-2113",
        "gtin": "4250338487516",
        "brand": "Essence",
        "ar": {
            "title": "ماسكارا ايسينس اي لوف  ، لون اسود",
            "meta_title": "ماسكارا إيسينس آي لوف سوداء تكثيف وتطويل 12مل | إكليل أبها",
            "meta_description": "اشتري ماسكارا ايسينس اي لوف لون اسود (12 مل). ماسكارا تكثيف وتطويل درامية بفرشاة سيليكون ولون أسود فاحم بدون تكتل. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["إيسينس", "ماسكارا_إيسينس_آي_لوف", "ماسكارا_تكثيف_الرموش", "إيسينس_البرتقالية", "إكليل_أبها"]
        },
        "en": {
            "title": "Essence I Love Mascara, Black",
            "meta_title": "Essence I Love Mascara Black Volume 12ml | Ekleel Abha",
            "meta_description": "Buy original Essence I Love Mascara, Black (12ml). Extreme volcanic volume & length deep black silicone brush mascara. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["essence", "essence_i_love_mascara", "crazy_volume_mascara", "black_mascara", "ekleel_abha"]
        }
    }


def create_product_2115():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول جسم حماية من الجراثيم مع ليفه من لايفبوي 300مل (Lifebuoy Germ Protection Body Wash with Loofah - 300ml)</strong> طقم الاستحمام الطبي المطهر والمضاد للجراثيم الفاخر الأكثر توصية وحماية عالمياً من لايفبوي (Lifebuoy) المصمم لمنح جسمك حماية فائقة بنسبة 99.9% ضد البكتيريا والجراثيم ونظافة عميقة ورغوة غنية مع ليفة استحمام ناعمة مجانية. يرتكز هذا الغسول الأصيل (Lifebuoy Body Wash 300ml) على تقنية Activ Silver+ المطهرة، المركبات المنظفة متوازنة الحموضة، والعناصر المرطبة لبشرة الجسم.</p>
<p>يعمل غسول لايفبوي بحماية الجراثيم على إزالة الدهون المترسبة والتعرق والقضاء على الجراثيم والميكروبات، وتنشيط جسمك بنفحات النظافة، ليترك بشرتك ناعمة كالحرير، مرطبة، مطهرة بنسبة 99.9%، ومحمية من الأمراض طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية فائقة بنسبة 99.9% ضد الجراثيم والبكتيريا وتقنية Activ Silver+:</strong> يقضي على الميكروبات.</li>
  <li><strong>طقم مدمج يتضمن ليفة استحمام فاخرة مجانية:</strong> تزيد تكوين الرغوة وتقشير الشوائب.</li>
  <li><strong>تنظيف وتطهير عميق ورغوة كريمية غنية:</strong> ينظف الجسم بلطف دون تجفيف الجلد.</li>
  <li><strong>ترطيب وتنعيم لبشرة الجسم:</strong> يحفظ حاجز الترطيب الطبيعي للجلد.</li>
  <li><strong>تركيبة خفيفة متوازنة الحموضة (pH Balanced):</strong> مناسبة للاستخدام اليومي لجميع أفراد الأسرة.</li>
  <li><strong>عبوة سعة 300 مل مزودة بضاغط مريح:</strong> حجم ممتاز للاستخدام اليومي والرياضي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الجسم والليفة المرفقة بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> اضغطي كمية مناسبة من سائل لايفبوي على الليفة وكوّني رغوة غنية.</li>
  <li><strong>الخطوة الثالثة:</strong> دلكي الجسم برفق ثم اشطفي جيداً بالماء الدافئ (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>تقنية الفضة الفعالة (Activ Silver Formula):</strong> تخترق الجدار الخلوي للبكتيريا وتقضي عليها بفاعلية.</li>
  <li><strong>المنظفات اللطيفة والمركبات المرطبة:</strong> تنظف الجسم وتحفظ نعومته الحريرية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن غسول جسم حماية من الجراثيم مع ليفة من لايفبوي 300 مل للتطهير والنظافة الفائقة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لايفبوي (Lifebuoy Unilever)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / غسولات ومجموعات لايفبوي المطهرة للجسم 300ml</td></tr>
  <tr><th>نوع المنتج</th><td>غسول جسم مطهر ومضاد للجراثيم بنسبة 99.9% مع ليفة مجانية (300ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>300 مل + ليفة استحمام مجانية</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (العادية، الجافة والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، مرطب، مطهر 99.9% ومفعم بالنظافة والانتعاش</td></tr>
  <tr><th>الملمس</th><td>سائل جل عطري رغوي مطهر ينشطف بالماء بسهولة</td></tr>
  <tr><th>العطر</th><td>عطر النظافة والحماية الطبية اللطيف الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>جزيئات الفضة الفعالة Activ Silver+، منظفات متوازنة pH، مرطبات جلدية</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الإمارات</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever Group</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد تقنية الفضة الفعالة (Activ Silver+) في غسول لايفبوي (Lifebuoy Body Wash)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول لايفبوي المطهر مشكلة تراكم الجراثيم والبكتيريا، رائحة التعرق بعد الرياضة، وجفاف الجلد بعد الاستحمام.</p>

<h3>لماذا تنجح تركيبة Lifebuoy Germ Protection & Loofah؟</h3>
<p>لأن جزيئات الفضة الفعالة Activ Silver+ تقضي على 99.9% من البكتيريا والجراثيم بينما تزيل الليفة الشوائب.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام اليومي بماء دافئ أثناء الاستحمام:</strong> ينظف ويطهر الجلد بالكامل.<br>
2. <strong>استخدام الليفة المرفقة بحركات دائرية:</strong> يزيل الخلايا الميتة والتعرق.<br>
3. <strong>الشطف الجيد بالماء:</strong> يضمن عدم بقاء ترسبات صابونية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الغسولات المطهرة تجفف البشرة وتسبب قشوراً."<br>
<strong>الحقيقة:</strong> غسول لايفبوي مدعم بمركبات مرطبة متوازنة الحموضة تضمن التطهير مع حفظ نعومة وطراوة الجلد.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخترق أيونات الفضة الفعالة الأغشية الخلوية للبكتيريا مسببة شللها ومنع تكاثرها بحماية 99.9%.</p>"""

    faqs = [
        ("ما هو غسول جسم حماية من الجراثيم مع ليفه من لايفبوي 300مل؟", "هو طقم استحمام مطهر يضم غسول جسم مضاد للجراثيم 99.9% وتقنية Activ Silver+ مع ليفة مجانية من لايفبوي (300 مل)."),
        ("ما هي فوائد تقنية Activ Silver+ والليفة المرفقة؟", "تقضي على 99.9% من الجراثيم والبكتيريا، تزيل التعرق، وتزيل الشوائب برغوة غنية."),
        ("هل يقضي على 99.9% من الجراثيم ويمنح رغوة غنية؟", "نعم، مثبت سريرياً في القضاء على 99.9% من الجراثيم وتوفير نظافة ورغوة غنية."),
        ("ما حجم العبوة ومحتوياتها؟", "تأتي بعبوة أنيقة سعة 300 مل مزودة بضاغط + ليفة استحمام مجانية."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الجسم والليفة، ضعي كمية على الليفة وكوّني رغوة، دلكي برفق واشطفي بالماء يومياً."),
        ("هل هو آمن لجميع أفراد الأسرة؟", "نعم، تركيبة متوازنة الحموضة آمنة للأطفال والبالغين من سن 3 سنوات."),
        ("أين صُنع غسول لايفبوي؟", "صُنع بواسطة مجموعة Unilever العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لايفبوي لدى إكليل أبها أصلية 100%."),
        ("ما رائحة غسول لايفبوي بحماية الجراثيم؟", "عطر النظافة والحماية الطبية اللطيف الفاخر."),
        ("هل يناسب الاستخدام بعد التمارين والرياضة؟", "نعم، ممتاز للانتعاش والنظافة والتطهير بعد الرياضة والأنشطة."),
        ("هل عبوة 300 مل بضاغط مريحة؟", "نعم، عبوة أنيقة بضاغط مريح جداً للاستخدام اليومي والشاور."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل لايفبوي الماركة الأولى عالمياً في الحماية من الجراثيم؟", "نعم، Lifebuoy الماركة رقم 1 العالمية الأكثر ثقة وتفضيلاً في التطهير."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً أثناء الاستحمام."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، ينشطف بالماء الدافئ بسهولة دون ترك أثر لزج."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يزيل رائحة التعرق الكريهة؟", "نعم، يقضي على البكتيريا المسببة لرائحة التعرق ويعطر الجسم."),
        ("هل يترك البشرة ناعمة ومرطبة؟", "نعم، يحافظ على رطوبة الجلد ونعومته الحريرية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء والاطفال؟", "نعم، ممتاز لجميع أفراد الأسرة."),
        ("هل يناسب الشتاء والصيف؟", "نعم، تطهير وترطيب طبيعي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن مجموعة الاستحمام؟", "نعم، منتج عناية وتطهير فاخر وأساسي لجميع أفراد العائلة."),
        ("هل يعيد المظهر المشرق الناعم للبشرة؟", "نعم، يمنح الجسد مظهراً ناعماً ومشرقاً ناصع النقاء."),
        ("هل تتوفر أنواع غسول لايفبوي الأخرى؟", "نعم، تتوفر عائلة Lifebuoy كاملة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Lifebuoy Germ Protection Body Wash with Loofah - 300ml</strong> is the world's #1 trusted authentic luxury antibacterial body wash shower set from Lifebuoy designed to deliver 99.9% germ protection against bacteria, deep cleansing, and a rich lather paired with a free soft shower loofah. Built upon Activ Silver+ germ protection technology, pH-balanced cleansers, and body-moisturizing compounds.</p>
<p>Lifebuoy Germ Protection Body Wash removes sweat and trapped sebum, banishes harmful microbes by 99.9%, and revitalizes your body with fresh cleanliness, leaving your skin touchably silky soft, hydrated, 99.9% sanitized, and protected all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>99.9% Antibacterial Germ Protection with Activ Silver+ Technology:</strong> Banishes harmful microbes.</li>
  <li><strong>Includes a Free Premium Shower Loofah:</strong> Enhances lathering and gently sweeps away impurities.</li>
  <li><strong>Deep Cleansing & Rich Foaming Lather:</strong> Cleanses body gently without stripping moisture.</li>
  <li><strong>Body Skin Softening & Hydration:</strong> Preserves the skin's natural moisture barrier.</li>
  <li><strong>pH-Balanced Mild Formula:</strong> Suitable for daily use for the entire family.</li>
  <li><strong>Convenient 300ml Value Pump Bottle:</strong> Excellent format for sports routines and daily family care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet body skin and the included loofah with warm water during shower.</li>
  <li><strong>Step 2:</strong> Pump a suitable amount of Lifebuoy gel onto loofah and work into a rich lather.</li>
  <li><strong>Step 3:</strong> Massage body gently in circular motions, then rinse thoroughly with warm water (use daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Activ Silver+ Formula:</strong> Penetrates bacterial cell walls destroying 99.9% of microbes effectively.</li>
  <li><strong>Gentle Cleansers & Hydrating Agents:</strong> Cleanse body while maintaining touchable silky softness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application only.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Lifebuoy Germ Protection Body Wash with Loofah 300ml for 99.9% germ protection and clean skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lifebuoy (Unilever)</td></tr>
  <tr><th>Category</th><td>Body Care / Lifebuoy Antibacterial Body Washes 300ml</td></tr>
  <tr><th>Product Type</th><td>99.9% Antibacterial Activ Silver+ Germ Protection Body Wash with Free Loofah (300ml)</td></tr>
  <tr><th>Volume/Weight</th><td>300 ml + Free Shower Loofah</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Normal, Dry & Oily Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, hydrated, 99.9% germ-free & spotlessly clean body skin</td></tr>
  <tr><th>Texture</th><td>Rich foaming antibacterial fragranced clear gel fluid</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh clean medical germ protection scent</td></tr>
  <tr><th>Active Ingredients</th><td>Activ Silver+ Molecules, pH-Balanced Cleansers, Hydrating Agents</td></tr>
  <tr><th>Country of Origin</th><td>KSA / UAE</td></tr>
  <tr><th>Manufacturer</th><td>Unilever Group</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 3+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Activ Silver+ Bacterial Disruption & 99.9% Germ Protection</h2>

<h3>What problem does this solve?</h3>
<p>Lifebuoy Germ Protection Body Wash resolves bacterial accumulation, post-workout sweat odor, and skin dryness.</p>

<h3>Why choose Lifebuoy Germ Protection Body Wash with Loofah?</h3>
<p>Activ Silver+ silver ions disrupt bacterial cell membranes providing 99.9% germ defense while the loofah cleanses sweat pores.</p>"""

    en_faqs = [
        ("What is Lifebuoy Germ Protection Body Wash with Loofah - 300ml?", "It is a luxury antibacterial shower set featuring a 300ml 99.9% germ protection body wash and a free soft shower loofah from Lifebuoy."),
        ("What are the benefits of Activ Silver+ Technology and the free loofah?", "Eliminates 99.9% of germs and bacteria, removes sweat odors, and sweeps away impurities with a rich lather."),
        ("Does it deliver 99.9% germ protection and a rich lather?", "Yes, clinically proven to eliminate 99.9% of germs and deliver a rich cleansing lather."),
        ("What volume and contents are included?", "300ml pump bottle + free shower loofah."),
        ("How do I use it correctly?", "Wet body and loofah, pump gel onto loofah, lather, massage gently and rinse daily."),
        ("Is it safe for the whole family?", "Yes, pH-balanced formula safe for children and adults aged 3+."),
        ("Where is Lifebuoy Body Wash manufactured?", "By Unilever Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All Lifebuoy products at Ekleel Abha are 100% original."),
        ("What scent does Lifebuoy Body Wash have?", "Luxurious fresh clean medical germ protection fragrance."),
        ("Is it good post-workout?", "Yes, excellent for post-workout sanitizing and refreshing shower routines."),
        ("Is the 300ml pump bottle convenient?", "Yes, convenient pump dispenser for easy shower use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Lifebuoy a #1 global germ protection brand?", "Yes, Lifebuoy is the world's #1 trusted germ protection brand."),
        ("How many times daily?", "Once or twice daily during showers."),
        ("Does it rinse off easily?", "Yes, rinses off smoothly with warm water without sticky residue."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help eliminate sweat odor?", "Yes, kills sweat-causing bacteria and perfumes body skin."),
        ("Does it leave skin soft and hydrated?", "Yes, preserves skin moisture and silky softness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men, women, and kids?", "Yes, suitable for the entire family."),
        ("Is it good for all seasons?", "Yes, ideal antibacterial care for summer and winter routines."),
        ("Is it a nice shower gift?", "Yes, excellent addition to family hygiene gift sets."),
        ("Does it restore clean radiant skin appearance?", "Yes, gives body skin a healthy smooth clean look."),
        ("Are other Lifebuoy body washes available?", "Yes, the full Lifebuoy body wash range is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2115",
        "sku": "EK-2115",
        "gtin": "6281006473904",
        "brand": "Lifebuoy",
        "ar": {
            "title": "غسول جسم حماية من الجراثيم مع ليفه من لايفبوي 300مل",
            "meta_title": "غسول لايفبوي بحماية الجراثيم مع ليفة 300مل | إكليل أبها",
            "meta_description": "اشتري غسول جسم حماية من الجراثيم مع ليفة من لايفبوي (300 مل). غسول مطهر بمعدل 99.9% بتقنية الفضة الفعالة Activ Silver+ مع ليفة مجانية. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["لايفبوي", "غسول_لايفبوي_المطهر", "حماية_من_الجراثيم", "غسول_مع_ليفة", "إكليل_أبها"]
        },
        "en": {
            "title": "Lifebuoy Germ Protection Body Wash with Loofah - 300ml",
            "meta_title": "Lifebuoy Germ Protection Body Wash with Loofah 300ml | Ekleel Abha",
            "meta_description": "Buy original Lifebuoy Germ Protection Body Wash with Loofah (300ml). 99.9% antibacterial Activ Silver+ body wash with free shower loofah. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["lifebuoy", "lifebuoy_body_wash", "germ_protection_wash", "activ_silver_wash", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 78 builders complete")
