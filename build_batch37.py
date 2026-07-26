import json, os

def create_product_1897():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>معجون أسنان أسود دينتيسيمو 75 مل (Dentissimo Black Toothpaste, 75 ml)</strong> معجون الأسنان الفاخر الأسود من دنتسيمو السويسري المصنوع بتقنية الكربون المنشط (Activated Charcoal) والفلوريد عالي الجودة لتبييض عميق وتطهير شامل لأسنان البالغين. يرتكز هذا المعجون الفريد (Dentissimo Black Activated Charcoal Toothpaste 75ml) على الكربون المنشط الفائق المسامية (Super-Porous Activated Charcoal)، الفلوريد بتركيز عالٍ، وخلاصة النعناع الفاحم المنعش.</p>
<p>يعمل معجون دنتسيمو الأسود على إزالة البقع الصفراء والداكنة العميقة من أسطح الأسنان، امتصاص السموم والبكتيريا الضارة بالفم، وتعزيز بياض الأسنان بتقنية الكربون المنشط، ليترك أسنانك ناصعة البياض، فمك معطراً، ومبتسمك أكثر ثقة من أي وقت مضى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تبييض عميق بالكربون المنشط فائق المسامية:</strong> يزيل البقع الداكنة والصفرة العميقة من الأسنان بكفاءة.</li>
  <li><strong>تطهير شامل وامتصاص السموم والبكتيريا:</strong> الكربون المنشط يمتص البكتيريا والمواد الملونة بفاعلية.</li>
  <li><strong>تقوية المينا وحماية من التسوس بالفلوريد عالي الجودة:</strong> يعيد تمعدن مينا الأسنان ويحميها.</li>
  <li><strong>عطر نعناع فاحم انتعاشي:</strong> نكهة منعشة تترك الفم عطرياً لساعات طويلة.</li>
  <li><strong>تركيبة دنتسيمو السويسرية الطبية المعتمدة:</strong> جربت وطورت في سويسرا بأعلى معايير الجودة.</li>
  <li><strong>عبوة فاخرة 75 مل:</strong> تصميم أنيق أسود يعكس الفخامة والتميز.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الكمية):</strong> ضعي كمية بحجم حبة البازلاء من معجون دنتسيمو الأسود على فرشاة أسنان ناعمة أو متوسطة.</li>
  <li><strong>الخطوة الثانية (التنظيف):</strong> نظفي الأسنان بحركات دائرية لطيفة لمدة دقيقتين كاملتين.</li>
  <li><strong>الخطوة الثالثة (الشطف):</strong> اشطفي الفم بالماء جيداً حتى اختفاء لون الكربون (يُستعمل مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الكربون المنشط فائق المسامية (Super-Porous Activated Charcoal):</strong> يمتص ويزيل البقع الداكنة والملونات والبكتيريا.</li>
  <li><strong>الفلوريد عالي الجودة:</strong> يعيد تمعدن المينا ويثبط بكتيريا التسوس.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام من قِبل البالغين فقط (لا يناسب الأطفال دون 12 سنة).</li>
  <li>احرص على الشطف الجيد بعد الاستخدام لإزالة لون الكربون.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن معجون دنتسيمو الأسود 75 مل بالكربون المنشط لتبييض عميق ونكهة فاحمة منعشة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>دنتسيمو (Dentissimo)</td></tr>
  <tr><th>الفئة</th><td>صحة الأسنان / معاجين أسنان دنتسيمو الفاخرة بالكربون المنشط للبالغين 75ml</td></tr>
  <tr><th>نوع المنتج</th><td>معجون أسنان فاخر بالكربون المنشط للتبييض العميق وتطهير الفم (75ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>75 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>أسنان البالغين (من 12 سنة)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان ناصعة البياض، فم منعش معطر، وابتسامة مشرقة واثقة</td></tr>
  <tr><th>الملمس</th><td>معجون كريمي أسود ناعم بنكهة نعناع فاحمة منعشة</td></tr>
  <tr><th>العطر</th><td>نكهة النعناع الفاحمة الغنية المنعشة</td></tr>
  <tr><th>المكونات النشطة</th><td>كربون منشط فائق المسامية، فلوريد عالي الجودة، خلاصة النعناع</td></tr>
  <tr><th>بلد المنشأ</th><td>سويسرا (Switzerland)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Dentissimo Switzerland</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الكربون المنشط والفلوريد في دنتسيمو الأسود (Dentissimo Black)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج معجون دنتسيمو الأسود مشكلة اصفرار وتلطخ الأسنان الشديد، الروائح الفموية، والبلاك العميق المستعصي على المعاجين العادية.</p>

<h3>لماذا تنجح تقنية الكربون المنشط في تبييض الأسنان؟</h3>
<p>لأن الكربون المنشط يمتلك مسامية عالية الكثافة (10,000 مرة أعلى من الكربون العادي) تمتص الجزيئات الملونة والمواد الغريبة المتراكمة على مينا الأسنان.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام مرتين يومياً:</strong> صباحاً ومساءً لنتائج تبييض أسرع وأعمق.<br>
2. <strong>الشطف الجيد بعد الاستخدام:</strong> اشطف بالماء حتى اختفاء لون الكربون الأسود.<br>
3. <strong>تجنب الأطعمة الملونة بعد التنظيف:</strong> انتظر 30 دقيقة قبل الأطعمة الملونة للحفاظ على نتائج التبييض.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الكربون المنشط يتلف مينا الأسنان."<br>
<strong>الحقيقة:</strong> الكربون المنشط في دنتسيمو بحجم جزيئي دقيق لا يؤذي المينا وهو معتمد من طب الأسنان السويسري.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعمل الكربون المنشط بآلية الامتزاز (Adsorption) لا الامتصاص؛ إذ تلتصق الجزيئات الملونة بسطحه المسامي ويُزال بالشطف دون تلف المينا.</p>"""

    faqs = [
        ("ما هو معجون أسنان أسود دينتيسيمو 75 مل؟", "هو معجون أسنان فاخر أسود من دنتسيمو السويسري بالكربون المنشط والفلوريد لتبييض عميق وتطهير شامل للأسنان 75 مل."),
        ("ما هي فوائد الكربون المنشط والفلوريد ونكهة النعناع؟", "يبيّض الكربون المنشط الأسنان ويمتص السموم، يقوي الفلوريد المينا، وتمنح النعناع انتعاشاً فاحماً لساعات."),
        ("هل يبيّض الأسنان بعمق ويزيل البقع الداكنة؟", "نعم، مثبت سريرياً في إزالة البقع الصفراء والداكنة بكفاءة بتقنية الكربون المنشط."),
        ("ما حجم العبوة؟", "تأتي بحجم 75 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضع كمية حبة البازلاء على فرشاة ناعمة، نظف 2 دقيقة بحركات دائرية، اشطف جيداً حتى اختفاء لون الكربون مرتين يومياً."),
        ("هل هو آمن على مينا الأسنان؟", "نعم، الكربون المنشط بحجم جزيئي دقيق معتمد من طب الأسنان السويسري ولا يتلف المينا."),
        ("ما هو بلد صنع دنتسيمو الأسود؟", "صُنع في سويسرا بواسطة Dentissimo Switzerland."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات دنتسيمو لدى إكليل أبها أصلية 100%."),
        ("هل يترك الكربون لوناً أسود على الأسنان؟", "لا، مع الشطف الجيد يختفي اللون تماماً ويترك الأسنان بيضاء."),
        ("ما نكهة معجون دنتسيمو الأسود؟", "نكهة نعناع فاحمة غنية ومنعشة للغاية."),
        ("هل يزيل الجير والبلاك؟", "نعم، الكربون المنشط يمتص ويزيل الجير والبلاك المتراكم."),
        ("هل الحجم 75 مل يدوم طويلاً؟", "نعم، يكفي لشهر ونصف من الاستخدام اليومي مرتين."),
        ("كيف أحفظ المعجون؟", "في مكان بارد وجاف."),
        ("هل يناسب البالغين من 12 سنة؟", "نعم، للبالغين من 12 سنة فما فوق."),
        ("هل يترك الفم معطراً؟", "نعم، يترك نفساً منعشاً لساعات طويلة."),
        ("كم مرة يومياً؟", "مرتين يومياً: صباحاً ومساءً."),
        ("هل يمنع التسوس؟", "نعم، الفلوريد يقي من التسوس ويقوي المينا."),
        ("هل يناسب أصحاب الأسنان الحساسة؟", "يُنصح أصحاب الأسنان الحساسة جداً باستشارة طبيب الأسنان قبل الاستخدام."),
        ("هل هو من أفضل معاجين التبييض لدى دنتسيمو؟", "نعم، Black Toothpaste هو معجون التبييض الأبرز من دنتسيمو السويسري."),
        ("هل التصميم يعكس الفخامة والتميز؟", "نعم، عبوة سوداء فاخرة تعكس التميز والأناقة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة."),
        ("هل يمكن استخدامه يومياً؟", "نعم، آمن للاستخدام اليومي المستمر."),
        ("هل يبيّض الأسنان تدريجياً؟", "نعم، نتائج التبييض تتحسن تدريجياً مع الاستخدام المنتظم."),
        ("هل يصلح هدية للبالغين؟", "نعم، هدية فاخرة ومميزة لمحبي العناية بالأسنان."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Dentissimo Black Toothpaste, 75 ml</strong> is a luxurious Swiss black charcoal toothpaste formulated with Super-Porous Activated Charcoal and High-Quality Fluoride for deep whitening and comprehensive oral purification for adults. Engineered in Switzerland by Dentissimo.</p>
<p>Dentissimo Black Toothpaste removes deep yellow and dark stains from tooth surfaces, absorbs toxins and harmful bacteria, and enhances whiteness with activated charcoal technology, leaving teeth sparkling white, breath refreshed, and smiles more confident than ever.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Deep Whitening with Super-Porous Activated Charcoal:</strong> Removes deep dark stains and yellowing effectively.</li>
  <li><strong>Comprehensive Oral Detox & Bacteria Absorption:</strong> Activated Charcoal absorbs bacteria and staining compounds.</li>
  <li><strong>Enamel Strengthening & Cavity Protection with High-Quality Fluoride:</strong> Remineralizes enamel and prevents decay.</li>
  <li><strong>Bold Refreshing Mint Flavor:</strong> Leaves mouth fragranced for hours.</li>
  <li><strong>Swiss Medical Dentissimo Formula:</strong> Developed and tested in Switzerland to highest quality standards.</li>
  <li><strong>Luxurious 75ml Black Packaging:</strong> Elegant design reflecting premium quality.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Amount):</strong> Apply a pea-sized amount of Dentissimo Black onto a soft or medium toothbrush.</li>
  <li><strong>Step 2 (Clean):</strong> Brush teeth in gentle circular motions for a full 2 minutes.</li>
  <li><strong>Step 3 (Rinse):</strong> Rinse mouth thoroughly with water until charcoal color disappears (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Super-Porous Activated Charcoal:</strong> Adsorbs and removes stains, bacteria, and pigmented compounds.</li>
  <li><strong>High-Quality Fluoride:</strong> Remineralizes enamel and inhibits decay-causing bacteria.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For adult use only (not suitable for children under 12).</li>
  <li>Rinse thoroughly after use to remove charcoal residue.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Adults seeking Dentissimo's 75ml Black Activated Charcoal Toothpaste for deep whitening and bold fresh breath.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Dentissimo</td></tr>
  <tr><th>Category</th><td>Dental Health / Dentissimo Premium Activated Charcoal Adult Toothpastes 75ml</td></tr>
  <tr><th>Product Type</th><td>Luxury Activated Charcoal Deep Whitening & Detox Adult Toothpaste (75ml)</td></tr>
  <tr><th>Volume/Weight</th><td>75 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Adult Teeth (Ages 12+)</td></tr>
  <tr><th>Finish</th><td>Sparkling white, stain-free, cavity-protected teeth & bold fresh breath</td></tr>
  <tr><th>Texture</th><td>Smooth black creamy paste with bold refreshing mint flavor</td></tr>
  <tr><th>Fragrance</th><td>Bold refreshing charcoal mint flavor</td></tr>
  <tr><th>Active Ingredients</th><td>Super-Porous Activated Charcoal, High-Quality Fluoride, Mint Extract</td></tr>
  <tr><th>Country of Origin</th><td>Switzerland</td></tr>
  <tr><th>Manufacturer</th><td>Dentissimo Switzerland</td></tr>
  <tr><th>Age Group</th><td>Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Activated Charcoal Adsorption & Fluoride Remineralization in Dentissimo Black</h2>

<h3>What problem does this solve?</h3>
<p>Dentissimo Black Toothpaste resolves deep tooth yellowing, stubborn stains from coffee and tea, bad breath, and deep plaque accumulation.</p>

<h3>Why choose Dentissimo Black Activated Charcoal Toothpaste?</h3>
<p>Activated Charcoal's adsorption mechanism captures pigmented compounds on enamel via van der Waals forces, while Fluoride remineralizes weakened enamel hydroxyapatite.</p>"""

    en_faqs = [
        ("What is Dentissimo Black Toothpaste, 75 ml?", "It is a luxurious Swiss black toothpaste with Super-Porous Activated Charcoal and Fluoride for deep whitening and oral detox."),
        ("What are the benefits of Activated Charcoal, Fluoride, and mint?", "Activated Charcoal whitens and detoxes teeth, Fluoride strengthens enamel, and mint delivers bold freshness."),
        ("Does it deeply whiten teeth and remove dark stains?", "Yes, clinically proven to remove yellow and dark stains with Super-Porous Activated Charcoal technology."),
        ("What size is this toothpaste?", "75ml tube."),
        ("How do I use it correctly?", "Apply pea-sized amount on a soft brush, brush 2 minutes in circular motions, rinse thoroughly twice daily."),
        ("Is it safe for tooth enamel?", "Yes, micro-particle Activated Charcoal is Swiss dentally approved and safe for enamel."),
        ("Where is Dentissimo Black manufactured?", "In Switzerland by Dentissimo Switzerland."),
        ("How do I verify authenticity at Ekleel Abha?", "All Dentissimo products at Ekleel Abha are 100% original."),
        ("Does charcoal leave black color on teeth?", "No, thorough rinsing removes all charcoal residue leaving teeth white."),
        ("What flavor does Dentissimo Black have?", "Features a bold refreshing charcoal mint flavor."),
        ("Does it remove tartar and plaque?", "Yes, Activated Charcoal adsorbs and removes plaque and tartar."),
        ("Does the 75ml tube last long?", "Yes, lasts about 6 weeks of twice-daily use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for adults aged 12+?", "Yes, for adults aged 12 and above."),
        ("Does it leave mouth fresh?", "Yes, bold mint delivers lasting fresh breath for hours."),
        ("How many times daily?", "Twice daily: morning and evening."),
        ("Does it prevent cavities?", "Yes, Fluoride prevents cavities and strengthens enamel."),
        ("Is it suitable for sensitive teeth?", "Those with very sensitive teeth should consult a dentist before use."),
        ("Is it Dentissimo's premium whitening toothpaste?", "Yes, Black Toothpaste is Dentissimo's flagship charcoal whitening toothpaste."),
        ("Does the packaging reflect premium quality?", "Yes, elegant black tube reflects luxury and exclusivity."),
        ("Is the tube recyclable?", "Yes, eco-friendly recyclable tube."),
        ("Is it safe for daily use?", "Yes, safe for continuous daily use."),
        ("Does whitening improve progressively?", "Yes, whitening results improve progressively with regular use."),
        ("Is it a good gift for adults?", "Yes, a premium, distinctive gift for dental care enthusiasts."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1897",
        "sku": "EK-1897",
        "gtin": "7640162324304",
        "brand": "Dentissimo",
        "ar": {
            "title": "معجون أسنان  أسود،دينتيسيمو  75 مل",
            "meta_title": "معجون أسنان دنتسيمو الأسود 75مل | إكليل أبها",
            "meta_description": "اشتري معجون أسنان دنتسيمو الأسود (75 مل). معجون بالكربون المنشط والفلوريد لتبييض عميق وتطهير الأسنان. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["دنتسيمو", "معجون_أسود", "كربون_منشط", "تبييض_أسنان", "إكليل_أبها"]
        },
        "en": {
            "title": "Dentissimo Black Toothpaste, 75 ml",
            "meta_title": "Dentissimo Black Toothpaste 75ml | Ekleel Abha",
            "meta_description": "Buy original Dentissimo Black Toothpaste (75ml). Activated Charcoal & Fluoride premium whitening toothpaste. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["dentissimo", "black_toothpaste", "activated_charcoal", "teeth_whitening", "ekleel_abha"]
        }
    }


def create_product_1898():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>معجون أسنان ذهبي دينتيسيمو 75 مل (Dentissimo Advanced Gold Toothpaste, 75 ml)</strong> معجون الأسنان الفاخر الذهبي من دنتسيمو السويسري المصنوع بتقنية الذهب الغروي (Colloidal Gold) والفلوريد المتقدم للتبييض الفائق وإعادة الإشراق لأسنان البالغين. يرتكز هذا المعجون المميز (Dentissimo Advanced Gold Toothpaste 75ml) على الذهب الغروي (Colloidal Gold)، الفلوريد المتقدم، وخلاصة النعناع الفاخمة.</p>
<p>يعمل معجون دنتسيمو الذهبي على تبييض الأسنان وإضفاء بريق ذهبي لامع على الابتسامة، تقوية مينا الأسنان بالفلوريد المتقدم، والقضاء على البلاك والبكتيريا، ليترك أسنانك متألقة كالذهب، فمك منعشاً، وابتسامتك ذهبية ساحرة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تبييض فائق وإشراق ذهبي بالذهب الغروي (Colloidal Gold):</strong> تقنية ذهبية حصرية تعطي الأسنان تألقاً استثنائياً.</li>
  <li><strong>تقوية مينا الأسنان بالفلوريد المتقدم:</strong> يعيد تمعدن المينا ويحميها من التسوس والتشقق.</li>
  <li><strong>القضاء على البلاك والبكتيريا الضارة بالفم:</strong> يحافظ على صحة الأسنان واللثة.</li>
  <li><strong>عطر نعناع فاخم منعش:</strong> نكهة راقية تترك الفم عطرياً لساعات.</li>
  <li><strong>تركيبة دنتسيمو السويسرية المتقدمة المعتمدة:</strong> تصنيع سويسري بأعلى معايير جودة الأسنان.</li>
  <li><strong>عبوة فاخرة 75 مل بتصميم ذهبي أنيق:</strong> تصميم يعكس الرقي والفخامة الاستثنائية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضع كمية بحجم حبة البازلاء على فرشاة أسنان ناعمة.</li>
  <li><strong>الخطوة الثانية:</strong> نظف الأسنان بحركات دائرية لطيفة لمدة دقيقتين.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطف الفم بالماء جيداً (يُستعمل مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الذهب الغروي (Colloidal Gold):</strong> يمنح الأسنان بريقاً وتألقاً استثنائياً مع خصائص مضادة للبكتيريا.</li>
  <li><strong>الفلوريد المتقدم:</strong> يعيد تمعدن مينا الأسنان ويثبط بكتيريا التسوس.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام من قِبل البالغين فقط (لا يناسب الأطفال دون 12 سنة).</li>
  <li>في حال استمرار الحساسية أو التهيج تجنب الاستخدام واستشر طبيب الأسنان.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن معجون دنتسيمو الذهبي المتقدم 75 مل لتبييض فائق وابتسامة ذهبية مشرقة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>دنتسيمو (Dentissimo)</td></tr>
  <tr><th>الفئة</th><td>صحة الأسنان / معاجين أسنان دنتسيمو الذهبية المتقدمة للبالغين 75ml</td></tr>
  <tr><th>نوع المنتج</th><td>معجون أسنان متقدم بالذهب الغروي للتبييض الفائق وإشراق الأسنان (75ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>75 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>أسنان البالغين (من 12 سنة)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان ذهبية التألق، ناصعة البياض، مقواة المينا وفم منعش</td></tr>
  <tr><th>الملمس</th><td>معجون كريمي ذهبي اللون ناعم بنكهة نعناع فاخمة</td></tr>
  <tr><th>العطر</th><td>نكهة النعناع الفاخمة الراقية المنعشة</td></tr>
  <tr><th>المكونات النشطة</th><td>ذهب غروي (Colloidal Gold)، فلوريد متقدم، خلاصة النعناع</td></tr>
  <tr><th>بلد المنشأ</th><td>سويسرا (Switzerland)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Dentissimo Switzerland</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الذهب الغروي والفلوريد المتقدم في دنتسيمو الذهبي (Dentissimo Gold)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج معجون دنتسيمو الذهبي مشكلة اصفرار الأسنان، فقدان اللمعة الطبيعية، البلاك المتراكم، ورغبة الحصول على ابتسامة ذهبية مشرقة.</p>

<h3>لماذا تنجح تقنية الذهب الغروي في تألق الأسنان؟</h3>
<p>لأن جزيئات الذهب النانوية الغروية تمتلك خصائص مضادة للبكتيريا وتعطي الأسنان لمعاناً وتألقاً استثنائياً بسبب تفاعلها مع ضوء الفم.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام مرتين يومياً لنتائج ذهبية:</strong> صباحاً ومساءً لنتائج تبييض وتألق أسرع.<br>
2. <strong>تجنب الإفراط في القهوة والشاي:</strong> التقليل من المشروبات الملونة يحافظ على نتائج التبييض.<br>
3. <strong>الاستمرار المنتظم 4-6 أسابيع:</strong> التحسن التدريجي يصل ذروته مع الاستخدام المنتظم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الذهب في المعجون لا يفيد الأسنان وهو مجرد تسويق."<br>
<strong>الحقيقة:</strong> الذهب الغروي النانوي مدروس علمياً بخصائص مضادة للبكتيريا ومحسّنة لبياض الأسنان.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتفاعل نانو جزيئات Au(0) الذهب الغروي مع البلازمون السطحي لتعكس الضوء بطريقة تعطي الأسنان تألقاً استثنائياً مع كبح نمو البكتيريا.</p>"""

    faqs = [
        ("ما هو معجون أسنان ذهبي دينتيسيمو 75 مل؟", "هو معجون أسنان فاخر ذهبي من دنتسيمو السويسري بالذهب الغروي والفلوريد المتقدم لتبييض فائق وابتسامة ذهبية مشرقة 75 مل."),
        ("ما هي فوائد الذهب الغروي والفلوريد المتقدم والنعناع؟", "يمنح الذهب الغروي الأسنان تألقاً استثنائياً ويكافح البكتيريا، يقوي الفلوريد المينا، وتمنح النعناع انتعاشاً فاخماً."),
        ("هل يبيّض الأسنان بتألق ذهبي مميز؟", "نعم، تقنية الذهب الغروي تمنح الأسنان بريقاً وتألقاً استثنائياً مع التبييض."),
        ("ما حجم العبوة؟", "تأتي بحجم 75 مل."),
        ("كيف يُستخدم؟", "ضع حبة البازلاء على فرشاة ناعمة، نظف 2 دقيقة بحركات دائرية، اشطف جيداً مرتين يومياً."),
        ("هل الذهب الغروي آمن على الأسنان؟", "نعم، الذهب الغروي النانوي مدروس علمياً وآمن وفق معايير طب الأسنان السويسري."),
        ("أين صُنع دنتسيمو الذهبي؟", "في سويسرا بواسطة Dentissimo Switzerland."),
        ("كيف أتحقق من أصالته؟", "جميع منتجات دنتسيمو لدى إكليل أبها أصلية 100%."),
        ("ما نكهة المعجون الذهبي؟", "نكهة نعناع فاخمة راقية ومنعشة للغاية."),
        ("هل يقضي على البلاك والبكتيريا؟", "نعم، الذهب الغروي والفلوريد يكافحان البلاك والبكتيريا."),
        ("هل الحجم 75 مل يدوم؟", "نعم، يكفي لشهر ونصف من الاستخدام اليومي."),
        ("كيف أحفظه؟", "في مكان بارد وجاف."),
        ("هل يناسب البالغين؟", "نعم، للبالغين من 12 سنة فما فوق."),
        ("هل يترك نفساً منعشاً؟", "نعم، يترك نفساً فاخماً منعشاً لساعات."),
        ("كم مرة يومياً؟", "مرتين يومياً."),
        ("هل يمنع التسوس؟", "نعم، الفلوريد يقي من التسوس."),
        ("هل يناسب الأسنان الحساسة؟", "يُنصح بمشورة طبيب الأسنان لمن يعاني من حساسية شديدة."),
        ("هل هو أبرز معاجين دنتسيمو المتقدمة؟", "نعم، Gold Toothpaste من أبرز وأفخر معاجين دنتسيمو."),
        ("هل التصميم الذهبي يعكس الفخامة؟", "نعم، عبوة ذهبية فاخرة تعكس التميز والرقي."),
        ("هل قابل لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة."),
        ("هل يمكن الاستخدام اليومي؟", "نعم، آمن للاستخدام اليومي المستمر."),
        ("هل التبييض يتحسن تدريجياً؟", "نعم، التحسن التدريجي يصل ذروته مع الاستخدام المنتظم."),
        ("هل يصلح هدية فاخرة؟", "نعم، هدية فاخرة ومتميزة لمحبي العناية الذهبية بالأسنان."),
        ("هل يمنح ابتسامة ذهبية مشرقة؟", "نعم، يمنح ابتسامة ذهبية مشرقة وواثقة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Dentissimo Advanced Gold Toothpaste, 75 ml</strong> is a luxurious Swiss gold toothpaste formulated with Colloidal Gold technology and Advanced Fluoride for supreme whitening and exceptional smile brilliance for adults. Engineered in Switzerland by Dentissimo.</p>
<p>Dentissimo Gold Toothpaste whitens teeth and imparts a golden brilliance to smiles, strengthens enamel with Advanced Fluoride, and eliminates plaque and bacteria, leaving teeth gleaming like gold, breath refreshed, and smiles brilliantly captivating.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Supreme Whitening & Golden Brilliance with Colloidal Gold:</strong> Exclusive gold technology delivers exceptional tooth radiance.</li>
  <li><strong>Enamel Strengthening with Advanced Fluoride:</strong> Remineralizes enamel and prevents decay and cracking.</li>
  <li><strong>Plaque & Harmful Bacteria Elimination:</strong> Maintains dental and gum health.</li>
  <li><strong>Luxurious Refreshing Mint Flavor:</strong> Premium flavor leaving mouth fragranced for hours.</li>
  <li><strong>Advanced Swiss Medical Dentissimo Formula:</strong> Swiss manufacturing to highest dental quality standards.</li>
  <li><strong>Luxurious 75ml Gold-Design Packaging:</strong> Elegant design reflecting sophistication and exclusivity.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply pea-sized amount onto a soft toothbrush.</li>
  <li><strong>Step 2:</strong> Brush teeth in gentle circular motions for 2 full minutes.</li>
  <li><strong>Step 3:</strong> Rinse mouth thoroughly with water (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Colloidal Gold:</strong> Imparts exceptional tooth brilliance with antibacterial properties.</li>
  <li><strong>Advanced Fluoride:</strong> Remineralizes tooth enamel and inhibits decay-causing bacteria.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For adult use only (not suitable for children under 12).</li>
  <li>Consult a dentist if sensitivity or irritation persists.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Adults seeking Dentissimo's 75ml Advanced Gold Toothpaste for supreme whitening and a brilliantly golden smile.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Dentissimo</td></tr>
  <tr><th>Category</th><td>Dental Health / Dentissimo Advanced Gold Adult Toothpastes 75ml</td></tr>
  <tr><th>Product Type</th><td>Luxury Colloidal Gold Supreme Whitening & Radiance Adult Toothpaste (75ml)</td></tr>
  <tr><th>Volume/Weight</th><td>75 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Adult Teeth (Ages 12+)</td></tr>
  <tr><th>Finish</th><td>Gleaming golden, brilliantly white, cavity-protected teeth & luxurious fresh breath</td></tr>
  <tr><th>Texture</th><td>Smooth golden creamy paste with luxurious refreshing mint flavor</td></tr>
  <tr><th>Fragrance</th><td>Luxurious refreshing sophisticated mint flavor</td></tr>
  <tr><th>Active Ingredients</th><td>Colloidal Gold, Advanced Fluoride, Mint Extract</td></tr>
  <tr><th>Country of Origin</th><td>Switzerland</td></tr>
  <tr><th>Manufacturer</th><td>Dentissimo Switzerland</td></tr>
  <tr><th>Age Group</th><td>Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Colloidal Gold Plasmon Resonance & Advanced Fluoride Remineralization</h2>

<h3>What problem does this solve?</h3>
<p>Dentissimo Gold Toothpaste resolves tooth yellowing, lost natural brilliance, bacterial plaque, and the desire for a dazzling golden smile.</p>

<h3>Why choose Dentissimo Advanced Gold Toothpaste?</h3>
<p>Au(0) nano-particles interact via surface plasmon resonance to reflect light brilliantly from enamel, while Advanced Fluoride remineralizes weakened hydroxyapatite.</p>"""

    en_faqs = [
        ("What is Dentissimo Advanced Gold Toothpaste, 75 ml?", "It is a luxurious Swiss gold toothpaste with Colloidal Gold and Advanced Fluoride for supreme whitening and exceptional smile radiance."),
        ("What are the benefits of Colloidal Gold, Advanced Fluoride, and mint?", "Colloidal Gold imparts exceptional tooth brilliance and fights bacteria, Advanced Fluoride strengthens enamel, and mint delivers luxurious freshness."),
        ("Does it deliver supreme whitening with golden brilliance?", "Yes, Colloidal Gold technology imparts exceptional tooth radiance and brilliance."),
        ("What size is this toothpaste?", "75ml tube."),
        ("How do I use it correctly?", "Apply pea-sized amount on a soft brush, brush 2 minutes in circular motions, rinse thoroughly twice daily."),
        ("Is Colloidal Gold safe for teeth?", "Yes, nano Colloidal Gold is scientifically studied and safe per Swiss dental standards."),
        ("Where is Dentissimo Gold manufactured?", "In Switzerland by Dentissimo Switzerland."),
        ("How do I verify authenticity at Ekleel Abha?", "All Dentissimo products at Ekleel Abha are 100% original."),
        ("What flavor does Dentissimo Gold have?", "Features a luxurious, refreshing sophisticated mint flavor."),
        ("Does it eliminate plaque and bacteria?", "Yes, Colloidal Gold and Advanced Fluoride combat plaque and bacteria."),
        ("Does the 75ml tube last long?", "Yes, lasts about 6 weeks of twice-daily use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for adults aged 12+?", "Yes, for adults aged 12 and above."),
        ("Does it leave mouth fresh?", "Yes, luxurious mint delivers lasting fresh breath for hours."),
        ("How often daily?", "Twice daily."),
        ("Does it prevent cavities?", "Yes, Advanced Fluoride prevents cavities."),
        ("Is it suitable for sensitive teeth?", "Consult a dentist if you have severe sensitivity."),
        ("Is it Dentissimo's premium gold toothpaste?", "Yes, Gold Toothpaste is Dentissimo's most premium advanced toothpaste."),
        ("Does the gold packaging reflect luxury?", "Yes, elegant gold tube reflects sophistication and exclusivity."),
        ("Is the tube recyclable?", "Yes, eco-friendly."),
        ("Is it safe for daily use?", "Yes, safe for continuous daily use."),
        ("Does whitening improve progressively?", "Yes, improvement peaks with regular 4-6 week use."),
        ("Is it a good luxury gift?", "Yes, premium distinctive gift for dental care enthusiasts."),
        ("Does it deliver a brilliantly golden smile?", "Yes, delivers a brilliantly golden, confident smile."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1898",
        "sku": "EK-1898",
        "gtin": "7640162324298",
        "brand": "Dentissimo",
        "ar": {
            "title": "معجون أسنان  ذهبي،دينتيسيمو  75 مل",
            "meta_title": "معجون أسنان دنتسيمو الذهبي المتقدم 75مل | إكليل أبها",
            "meta_description": "اشتري معجون أسنان دنتسيمو الذهبي (75 مل). معجون بالذهب الغروي والفلوريد المتقدم لتبييض فائق وابتسامة ذهبية. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["دنتسيمو", "معجون_ذهبي", "ذهب_غروي", "تبييض_أسنان", "إكليل_أبها"]
        },
        "en": {
            "title": "Dentissimo Advanced Gold Toothpaste, 75 ml",
            "meta_title": "Dentissimo Advanced Gold Toothpaste 75ml | Ekleel Abha",
            "meta_description": "Buy original Dentissimo Advanced Gold Toothpaste (75ml). Colloidal Gold & Advanced Fluoride supreme whitening toothpaste. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["dentissimo", "gold_toothpaste", "colloidal_gold", "teeth_whitening", "ekleel_abha"]
        }
    }


def _make_crystal_serum(pid, gtin, ar_name, en_name, volume_ml, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> سيروم العناية بالبشرة الفائق المستوى من كريستال المصنوع بتركيبة مكثفة لتغذية وترطيب وإشراق بشرة الوجه. يرتكز هذا السيروم (Crystal Serum {volume_ml}ml) على مزيج من المكونات الفعالة التي تعمل على التجديد الخلوي، توحيد لون البشرة، وإعادة الإشراق الطبيعي للوجه.</p>
<p>يعمل سيروم كريستال على تغذية طبقات الجلد العميقة، تقليل ظهور التجاعيد والخطوط الدقيقة، وتوحيد لون بشرة الوجه، ليترك الوجه مشرقاً، كريمياً، وأكثر حيوية من اليوم الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب عميق لـ 24 ساعة:</strong> يغذي طبقات الجلد ويحفظ الترطيب الطبيعي.</li>
  <li><strong>توحيد لون البشرة وإشراقها:</strong> يقلل التصبغات ويمنح الوجه توهجاً طبيعياً.</li>
  <li><strong>تجديد الخلايا وتقليل الخطوط الدقيقة:</strong> يدعم تجديد الخلايا ويقلل علامات التقدم في السن.</li>
  <li><strong>تركيبة خفيفة سريعة الامتصاص:</strong> تنفذ لطبقات الجلد العميقة دون لزوجة.</li>
  <li><strong>مناسب لجميع أنواع البشرة:</strong> آمن للبشرة العادية والجافة والدهنية والمختلطة.</li>
  <li><strong>عبوة سعة {volume_ml} مل:</strong> حجم وافر للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> نظفي وجهك بغسول مناسب وجففي البشرة جيداً.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية صغيرة من سيروم كريستال على الوجه والرقبة.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي بلطف بحركات دائرية لطيفة حتى الامتصاص الكامل (يُستعمل صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركبات الترطيب الفعالة:</strong> تحفظ الرطوبة وتغذي البشرة عمقاً.</li>
  <li><strong>مضادات الأكسدة وعوامل التفتيح:</strong> تقيان البشرة وتوحدان لونها.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والرقبة فقط.</li>
  <li>تجنبي التلامس مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لمن يبحث عن سيروم كريستال {volume_ml} مل للعناية العميقة بالبشرة وتوحيد لونها.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كريستال (Crystal)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / سيرومات كريستال للوجه المغذية والمرطبة {volume_ml}ml</td></tr>
  <tr><th>نوع المنتج</th><td>سيروم فائق للعناية بالبشرة والترطيب العميق وإشراق الوجه ({volume_ml}ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>{volume_ml} مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (العادية والجافة والدهنية والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه مشرق، موحد اللون، مرطب لـ 24 ساعة وأكثر حيوية</td></tr>
  <tr><th>الملمس</th><td>سيروم خفيف سريع الامتصاص دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر ناعم لطيف</td></tr>
  <tr><th>المكونات النشطة</th><td>مركبات ترطيب فعالة، مضادات الأكسدة، عوامل توحيد اللون</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Crystal Cosmetics</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد سيروم كريستال للوجه ({volume_ml}مل)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج سيروم كريستال مشكلة جفاف البشرة، التصبغات وعدم توحد اللون، وفقدان الحيوية والإشراق الطبيعي للوجه.</p>

<h3>لماذا يُعد سيروم كريستال الخيار الأمثل؟</h3>
<p>لأن تركيبته المكثفة تنفذ لطبقات الجلد العميقة وتعمل على الترطيب والتغذية وتوحيد اللون بشكل متزامن.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق صباحاً ومساءً على بشرة نظيفة:</strong> أفضل النتائج تُحقق بالاستخدام المنتظم.<br>
2. <strong>استخدام واقي الشمس في النهار:</strong> لحماية نتائج توحيد اللون من الشمس.<br>
3. <strong>تكميل الروتين بمرطب:</strong> يضاعف نتائج الترطيب العميق.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "السيرومات تعطي نتائج فورية في يوم واحد."<br>
<strong>الحقيقة:</strong> سيروم كريستال يعمل تدريجياً مع الاستخدام المنتظم لـ 4-8 أسابيع لأفضل النتائج.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تعمل الجزيئات الصغيرة للسيروم على التغلغل في الطبقة الشوكية للجلد لتوصيل المكونات الفعالة مباشرة لخلايا البشرة المستهدفة.</p>"""

    faqs = [
        (f"ما هو سيروم كريستال {volume_ml} مل؟", f"هو سيروم عناية بالبشرة فائق من كريستال بتركيبة مكثفة لترطيب عميق وتوحيد لون الوجه وإشراقه بحجم {volume_ml} مل."),
        ("ما هي فوائد سيروم كريستال؟", "يوفر ترطيباً عميقاً لـ 24 ساعة، يوحد لون البشرة، ويجدد الخلايا ويمنح الوجه إشراقاً طبيعياً."),
        ("هل يرطب البشرة بعمق لـ 24 ساعة؟", "نعم، تركيبته المكثفة تحفظ الترطيب الطبيعي للبشرة طوال اليوم."),
        (f"ما حجم العبوة؟", f"تأتي بعبوة سعة {volume_ml} مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية صغيرة على وجه نظيف جاف، دلكي بلطف حتى الامتصاص صباحاً ومساءً."),
        ("هل هو آمن لجميع أنواع البشرة؟", "نعم، مناسب للبشرة العادية والجافة والدهنية والمختلطة."),
        ("ما هو بلد صنع سيروم كريستال؟", "صُنع في المملكة العربية السعودية بواسطة Crystal Cosmetics."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كريستال لدى إكليل أبها أصلية 100%."),
        ("هل يمتص بسرعة دون لزوجة؟", "نعم، قوام خفيف يمتص سريعاً دون لزوجة."),
        ("ما رائحة سيروم كريستال؟", "عطر ناعم لطيف."),
        ("هل يوحد لون البشرة ويقلل التصبغات؟", "نعم، عوامل توحيد اللون تقلل التصبغات وتمنح الوجه توهجاً طبيعياً."),
        (f"هل الحجم {volume_ml} مل يدوم طويلاً؟", f"نعم، عبوة {volume_ml} مل تكفي لفترة جيدة من الاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل يناسب من فوق 16 سنة؟", "نعم، مناسب لجميع الفئات من 16 سنة."),
        ("هل يقلل التجاعيد والخطوط الدقيقة؟", "نعم، يدعم تجديد الخلايا ويقلل علامات التقدم في السن."),
        ("كم مرة يومياً؟", "صباحاً ومساءً."),
        ("هل يناسب البشرة الحساسة؟", "يُنصح بعمل اختبار حساسية قبل الاستخدام الكامل."),
        ("هل يصلح تحت المكياج؟", "نعم، قاعدة ممتازة تحت المكياج بفضل قوامه الخفيف."),
        ("هل هو من أبرز سيرومات كريستال؟", "نعم، Crystal Serum من أبرز منتجات كريستال للعناية بالبشرة."),
        ("هل يمنح البشرة حيوية وإشراقاً؟", "نعم، يمنح الوجه حيوية وإشراقاً طبيعياً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("كم وقتاً تظهر النتائج؟", "نتائج ملحوظة تظهر خلال 4-6 أسابيع من الاستخدام المنتظم."),
        ("هل يصلح للرقبة أيضاً؟", "نعم، مناسب للوجه والرقبة."),
        ("هل يصلح هدية؟", "نعم، هدية عملية لمن يهتم بالعناية بالبشرة."),
        ("هل يتوفر بسعر ممتاز؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is a premium-level facial skincare serum from Crystal formulated with a concentrated blend for deep nourishment, hydration, and brightening of facial skin. This serum works on cellular renewal, skin tone unification, and natural radiance restoration.</p>
<p>Crystal Serum nourishes deep skin layers, reduces fine lines and wrinkles, and unifies facial skin tone, leaving the face glowing, creamy, and more vibrant from day one.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Deep 24-Hour Hydration:</strong> Nourishes skin layers and preserves natural moisture.</li>
  <li><strong>Skin Tone Unification & Radiance:</strong> Reduces hyperpigmentation and imparts natural facial glow.</li>
  <li><strong>Cell Renewal & Fine Line Reduction:</strong> Supports cell renewal and reduces signs of aging.</li>
  <li><strong>Lightweight Fast-Absorbing Formula:</strong> Penetrates deep skin layers without greasiness.</li>
  <li><strong>Suitable for All Skin Types:</strong> Safe for normal, dry, oily, and combination skin.</li>
  <li><strong>{volume_ml}ml Bottle:</strong> Generous volume for continuous daily use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse face with suitable cleanser and pat dry.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a small amount of Crystal Serum on face and neck.</li>
  <li><strong>Step 3 (Massage):</strong> Massage gently in circular motions until fully absorbed (use morning and evening).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Active Moisturizing Compounds:</strong> Preserve moisture and nourish skin deeply.</li>
  <li><strong>Antioxidants & Brightening Agents:</strong> Protect skin and unify tone.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and neck skin application only.</li>
  <li>Avoid contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Those seeking Crystal {volume_ml}ml Serum for deep facial skincare and skin tone unification.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Crystal</td></tr>
  <tr><th>Category</th><td>Skincare / Crystal Nourishing & Hydrating Facial Serums {volume_ml}ml</td></tr>
  <tr><th>Product Type</th><td>Premium Deep Hydration & Brightening Facial Serum ({volume_ml}ml)</td></tr>
  <tr><th>Volume/Weight</th><td>{volume_ml} ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Normal, Dry, Oily & Combination)</td></tr>
  <tr><th>Finish</th><td>Glowing, even-toned, 24-hour hydrated & vibrant facial skin</td></tr>
  <tr><th>Texture</th><td>Lightweight fast-absorbing serum without greasiness</td></tr>
  <tr><th>Fragrance</th><td>Subtle gentle scent</td></tr>
  <tr><th>Active Ingredients</th><td>Active Moisturizing Compounds, Antioxidants, Brightening Agents</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia</td></tr>
  <tr><th>Manufacturer</th><td>Crystal Cosmetics</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Crystal Serum Deep Cellular Penetration & Antioxidant Skin Defense</h2>

<h3>What problem does this solve?</h3>
<p>Crystal Serum resolves facial skin dryness, hyperpigmentation, uneven tone, and loss of natural vitality and radiance.</p>

<h3>Why choose Crystal Serum {volume_ml}ml?</h3>
<p>Its concentrated small-molecule formula penetrates the stratum spinosum to deliver active ingredients directly to targeted skin cells for deep hydration and brightening.</p>"""

    en_faqs = [
        (f"What is Crystal Serum {volume_ml}ml?", f"It is a premium facial skincare serum from Crystal with a concentrated formula for deep hydration, skin tone unification, and brightness in {volume_ml}ml."),
        ("What are the benefits of Crystal Serum?", "Delivers deep 24-hour hydration, unifies skin tone, renews cells, and imparts natural facial radiance."),
        ("Does it hydrate skin deeply for 24 hours?", "Yes, concentrated formula preserves natural skin moisture throughout the day."),
        (f"What volume is contained in this bottle?", f"{volume_ml}ml."),
        ("How do I use it correctly?", "Apply a small amount on clean dry face, massage gently until absorbed, morning and evening."),
        ("Is it safe for all skin types?", "Yes, suitable for normal, dry, oily, and combination skin."),
        ("Where is Crystal Serum manufactured?", "In Saudi Arabia by Crystal Cosmetics."),
        ("How do I verify authenticity at Ekleel Abha?", "All Crystal products at Ekleel Abha are 100% original."),
        ("Does it absorb quickly without greasiness?", "Yes, lightweight formula absorbs quickly without greasiness."),
        ("What scent does Crystal Serum have?", "Subtle gentle pleasant scent."),
        ("Does it unify skin tone and reduce hyperpigmentation?", "Yes, brightening agents reduce hyperpigmentation and impart natural glow."),
        (f"Does the {volume_ml}ml bottle last long?", f"Yes, {volume_ml}ml lasts a good period of daily use."),
        ("How should I store it?", "In a cool, dry place away from sunlight."),
        ("Is it suitable for ages 16+?", "Yes, suitable for all ages from 16."),
        ("Does it reduce fine lines and wrinkles?", "Yes, supports cell renewal and reduces aging signs."),
        ("How many times daily?", "Morning and evening."),
        ("Is it suitable for sensitive skin?", "Recommend a patch test before full use."),
        ("Does it work under makeup?", "Yes, excellent base under makeup due to lightweight texture."),
        ("Is it among Crystal's most popular serums?", "Yes, Crystal Serum is among Crystal's most prominent skincare products."),
        ("Does it give skin vitality and radiance?", "Yes, imparts natural vitality and facial glow."),
        ("Is the bottle recyclable?", "Yes."),
        ("When do results appear?", "Notable results within 4-6 weeks of regular use."),
        ("Is it suitable for neck too?", "Yes, suitable for face and neck."),
        ("Is it a good gift?", "Yes, practical gift for skincare enthusiasts."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Crystal",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. سيروم عناية بالبشرة فائق بتركيبة مكثفة لترطيب وإشراق وتوحيد لون الوجه. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Premium concentrated facial serum for deep hydration and skin brightening. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1899():
    return _make_crystal_serum(
        pid=1899, gtin="6291100270675",
        ar_name="سيروم كريستال  100 مل",
        en_name="Crystal Serum 100ml",
        volume_ml=100,
        tags_ar=["كريستال", "سيروم_كريستال", "سيروم_وجه", "ترطيب_البشرة", "إكليل_أبها"],
        tags_en=["crystal", "crystal_serum", "facial_serum", "skin_hydration", "ekleel_abha"]
    )


def create_product_1900():
    return _make_crystal_serum(
        pid=1900, gtin="6291100272549",
        ar_name="سيروم كريستال  60 مل",
        en_name="Crystal Serum 60ml",
        volume_ml=60,
        tags_ar=["كريستال", "سيروم_كريستال", "سيروم_وجه_60مل", "ترطيب_البشرة", "إكليل_أبها"],
        tags_en=["crystal", "crystal_serum_60ml", "facial_serum", "compact_serum", "ekleel_abha"]
    )


def create_product_1901():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>جل ترطيب وتصحيح البشرة إيفاكلار ديو من لاروش بوزاي - 40مل (La Roche-Posay Effaclar Duo Moisturizing and Correcting Gel - 40ml)</strong> من أشهر وأفضل منتجات لاروش بوزاي الطبية لعلاج حب الشباب وتصحيح آثاره للبشرة الدهنية والمختلطة المعرضة للبثور. يرتكز هذا الجل (Effaclar Duo+ 40ml) على بروكورال (Procerad)، نياسيناميد (Niacinamide)، وحمض الساليسيليك (Salicylic Acid) بتركيزات طبية دقيقة.</p>
<p>يعمل إيفاكلار ديو على علاج حب الشباب والبثور الجديدة والمتكررة، تقليل الاحمرار والبقع ما بعد حب الشباب، تضييق المسام، وترطيب البشرة دون إضافة دهون، ليترك بشرتك صافية، خالية من البثور، موحدة اللون ومرطبة دون إحساس بالثقل أو الدهون.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>علاج حب الشباب والبثور الجديدة بالبروكورال والساليسيليك:</strong> يقلص البثور ويمنع ظهور جديدة.</li>
  <li><strong>تصحيح وتقليل بقع ما بعد حب الشباب بالنياسيناميد:</strong> يوحد لون البشرة ويقلل الاحمرار والبقع الداكنة.</li>
  <li><strong>تضييق المسام وتحكم أفضل بالدهون:</strong> يجعل البشرة أكثر نعومة ومسامات أقل اتساعاً.</li>
  <li><strong>ترطيب 24 ساعة دون دهون:</strong> يرطب البشرة الدهنية دون إضافة زيوت أو لمعان.</li>
  <li><strong>موصى به من أطباء الجلدية (Dermatologist Recommended):</strong> طُور بتعاون مع أطباء جلدية متخصصين.</li>
  <li><strong>عبوة مدمجة 40 مل:</strong> مناسبة للاستخدام اليومي الصباحي والمسائي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> نظفي وجهك بغسول مناسب لبشرة لاروش بوزاي وجففيها برفق.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية صغيرة من إيفاكلار ديو على الوجه أو المناطق المستهدفة بالبثور.</li>
  <li><strong>الخطوة الثالثة (التوزيع):</strong> وزعي الجل بلطف بحركات دائرية حتى الامتصاص (يُستعمل صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>بروكورال (Procerad) وحمض الساليسيليك:</strong> يعالجان حب الشباب ويمنعان تكاثر البكتيريا.</li>
  <li><strong>نياسيناميد والجليسرين:</strong> يوحدان لون البشرة ويحفظان الترطيب دون دهون.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه المعرضة لحب الشباب فقط.</li>
  <li>تجنبي التلامس مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لأصحاب البشرة الدهنية والمختلطة المعرضة لحب الشباب الباحثين عن إيفاكلار ديو لاروش بوزاي 40مل لعلاج وتصحيح البثور.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لاروش بوزاي (La Roche-Posay)</td></tr>
  <tr><th>الفئة</th><td>العناية الطبية بالبشرة / جلات لاروش بوزاي الطبية لعلاج وتصحيح حب الشباب 40ml</td></tr>
  <tr><th>نوع المنتج</th><td>جل طبي لعلاج وتصحيح بشرة حب الشباب بالبروكورال والنياسيناميد (40ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>40 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الدهنية والمختلطة المعرضة لحب الشباب والبثور</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة صافية خالية من البثور، موحدة اللون، مرطبة دون لمعان دهني</td></tr>
  <tr><th>الملمس</th><td>جل خفيف سريع الامتصاص دون لزوجة أو دهنية</td></tr>
  <tr><th>العطر</th><td>خالٍ من العطور (Fragrance-Free)</td></tr>
  <tr><th>المكونات النشطة</th><td>بروكورال (Procerad)، نياسيناميد، حمض الساليسيليك، جليسرين</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>La Roche-Posay (L'Oréal Group)</td></tr>
  <tr><th>الفئة العمرية</th><td>المراهقون والبالغون (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد البروكورال والنياسيناميد في إيفاكلار ديو (Effaclar Duo)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج إيفاكلار ديو مشكلة حب الشباب والبثور المتكررة، الاحمرار وبقع ما بعد حب الشباب، والمسام الواسعة في البشرة الدهنية.</p>

<h3>لماذا تنجح تركيبة إيفاكلار ديو الطبية؟</h3>
<p>لأن البروكورال يكافح بكتيريا P. acnes ويمنع تكرار البثور، بينما يمنع النياسيناميد نقل الميلانين للخلايا ويقلل الاحمرار.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام صباحاً ومساءً بعد التنظيف:</strong> ضع الجل على بشرة جافة نظيفة.<br>
2. <strong>استخدام واقي الشمس في النهار:</strong> الحماية من الشمس تمنع تكون بقع جديدة.<br>
3. <strong>الاستمرار 4-8 أسابيع:</strong> النتائج تتحسن تدريجياً مع الاستخدام المنتظم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مستحضرات البشرة الدهنية لا تحتاج إلى ترطيب."<br>
<strong>الحقيقة:</strong> إيفاكلار ديو يرطب البشرة الدهنية دون زيادة الدهون أو اللمعان، بل يساعد في توازن الإنتاج الزهمي.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يثبط البروكورال مسار C1-INH لتنشيط الكوميدونات، بينما يمنع النياسيناميد نقل الميلانوسومات من خلايا الميلانين إلى خلايا الجلد المجاورة.</p>"""

    faqs = [
        ("ما هو جل ترطيب وتصحيح البشرة إيفاكلار ديو من لاروش بوزاي 40مل؟", "هو جل طبي من لاروش بوزاي بالبروكورال والنياسيناميد وحمض الساليسيليك لعلاج حب الشباب وتصحيح بقوده وترطيب البشرة الدهنية 40 مل."),
        ("ما هي فوائد البروكورال والنياسيناميد وحمض الساليسيليك؟", "يعالج البروكورال حب الشباب، يوحد النياسيناميد لون البشرة ويقلل الاحمرار، ويضيق الساليسيليك المسام."),
        ("هل يعالج حب الشباب والبثور المتكررة بكفاءة؟", "نعم، مثبت سريرياً في علاج حب الشباب والبثور وتقليلها مع الاستخدام المنتظم."),
        ("ما حجم العبوة؟", "تأتي بعبوة سعة 40 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضع كمية صغيرة على وجه نظيف جاف، وزع برفق صباحاً ومساءً."),
        ("هل هو موصى به من أطباء الجلدية؟", "نعم، طُور بتعاون مع أطباء جلدية وموصى به طبياً."),
        ("ما هو بلد صنع إيفاكلار ديو؟", "صُنع في فرنسا بواسطة مجموعة L'Oréal."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لاروش بوزاي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب البشرة الحساسة المعرضة لحب الشباب؟", "نعم، خالٍ من العطور ومناسب للبشرة الحساسة الدهنية."),
        ("ما رائحة إيفاكلار ديو؟", "خالٍ من العطور تماماً."),
        ("هل يرطب دون إضافة دهون أو لمعان؟", "نعم، يرطب البشرة الدهنية دون إضافة زيوت أو لمعان."),
        ("هل 40 مل تدوم طويلاً؟", "نعم، تكفي لعدة أشهر من الاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب المراهقين والبالغين؟", "نعم، من 12 سنة فما فوق."),
        ("هل يضيق المسام الواسعة؟", "نعم، يحسن مظهر المسام ويضيقها."),
        ("كم مرة يومياً؟", "صباحاً ومساءً."),
        ("هل يقلل بقع ما بعد حب الشباب؟", "نعم، النياسيناميد يقلل الاحمرار والبقع الداكنة ما بعد حب الشباب."),
        ("هل يمنع ظهور بثور جديدة؟", "نعم، الاستخدام المنتظم يمنع تكاثر بكتيريا حب الشباب."),
        ("هل هو من أبرز منتجات لاروش بوزاي؟", "نعم، Effaclar Duo من أشهر وأكثر منتجات لاروش بوزاي مبيعاً عالمياً."),
        ("هل يناسب البشرة الدهنية والمختلطة؟", "نعم، مصمم خصيصاً للبشرة الدهنية والمختلطة المعرضة لحب الشباب."),
        ("هل قابل لإعادة التدوير؟", "نعم."),
        ("متى تظهر النتائج؟", "نتائج ملحوظة خلال 4-8 أسابيع من الاستخدام المنتظم."),
        ("هل يناسب الاستخدام تحت المكياج؟", "نعم، قاعدة جيدة تحت المكياج بقوامه الخفيف."),
        ("هل يعالج الكوميدونات والرؤوس السوداء؟", "نعم، حمض الساليسيليك يساعد في تنظيف المسام من الكوميدونات."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>La Roche-Posay Effaclar Duo Moisturizing and Correcting Gel - 40ml</strong> is one of La Roche-Posay's most iconic medical products for treating acne and correcting its aftermath on oily and combination skin. Formulated with Procerad, Niacinamide, and Salicylic Acid at precise medical concentrations.</p>
<p>Effaclar Duo treats new and recurring acne blemishes, reduces post-acne redness and dark spots, tightens pores, and moisturizes skin without adding oils, leaving skin clear, blemish-free, even-toned, and hydrated without heaviness.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Acne & Blemish Treatment with Procerad & Salicylic Acid:</strong> Shrinks blemishes and prevents new ones.</li>
  <li><strong>Post-Acne Spot Correction with Niacinamide:</strong> Unifies skin tone and reduces redness and dark spots.</li>
  <li><strong>Pore Tightening & Sebum Control:</strong> Makes skin smoother with less visible pores.</li>
  <li><strong>24-Hour Oil-Free Hydration:</strong> Moisturizes oily skin without adding oils or shine.</li>
  <li><strong>Dermatologist Recommended:</strong> Developed with dermatology specialists.</li>
  <li><strong>Compact 40ml Tube:</strong> Suitable for daily morning and evening use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse face with a suitable La Roche-Posay cleanser and pat dry gently.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a small amount of Effaclar Duo onto the face or targeted blemish areas.</li>
  <li><strong>Step 3 (Distribute):</strong> Distribute gently in circular motions until absorbed (use morning and evening).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Procerad & Salicylic Acid:</strong> Treat acne and prevent bacterial proliferation.</li>
  <li><strong>Niacinamide & Glycerin:</strong> Unify skin tone and preserve oil-free hydration.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical acne-prone facial skin application only.</li>
  <li>Avoid contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Those with oily and combination acne-prone skin seeking La Roche-Posay Effaclar Duo 40ml for blemish treatment and correction.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>La Roche-Posay</td></tr>
  <tr><th>Category</th><td>Medical Skincare / La Roche-Posay Effaclar Medical Acne Treatment Gels 40ml</td></tr>
  <tr><th>Product Type</th><td>Medical Procerad & Niacinamide Acne Correcting & Moisturizing Gel (40ml)</td></tr>
  <tr><th>Volume/Weight</th><td>40 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Oily & Combination Acne-Prone Skin</td></tr>
  <tr><th>Finish</th><td>Clear, blemish-free, even-toned, hydrated skin without oily shine</td></tr>
  <tr><th>Texture</th><td>Lightweight fast-absorbing gel without greasiness</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-Free</td></tr>
  <tr><th>Active Ingredients</th><td>Procerad, Niacinamide, Salicylic Acid, Glycerin</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>La Roche-Posay (L'Oréal Group)</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Procerad Comedo Inhibition & Niacinamide Melanosome Transfer Block</h2>

<h3>What problem does this solve?</h3>
<p>Effaclar Duo resolves recurring acne blemishes, post-acne redness and dark spots, and enlarged pores in oily and combination skin.</p>

<h3>Why choose La Roche-Posay Effaclar Duo?</h3>
<p>Procerad inhibits C1-INH comedo formation pathway while Niacinamide blocks melanosome transfer from melanocytes to adjacent keratinocytes, reducing post-acne discoloration.</p>"""

    en_faqs = [
        ("What is La Roche-Posay Effaclar Duo Moisturizing and Correcting Gel - 40ml?", "It is a medical gel from La Roche-Posay with Procerad, Niacinamide, and Salicylic Acid for treating acne and correcting its aftermath on oily skin."),
        ("What are the benefits of Procerad, Niacinamide, and Salicylic Acid?", "Procerad treats acne, Niacinamide unifies tone and reduces redness, and Salicylic Acid tightens pores."),
        ("Does it treat recurring acne blemishes effectively?", "Yes, clinically proven to treat acne and reduce blemishes with regular use."),
        ("What volume is contained in this tube?", "40ml."),
        ("How do I use it correctly?", "Apply a small amount on clean dry face, distribute gently morning and evening."),
        ("Is it dermatologist recommended?", "Yes, developed with dermatology specialists and medically recommended."),
        ("Where is Effaclar Duo manufactured?", "In France by La Roche-Posay (L'Oréal Group)."),
        ("How do I verify authenticity at Ekleel Abha?", "All La Roche-Posay products at Ekleel Abha are 100% original."),
        ("Is it suitable for sensitive acne-prone skin?", "Yes, fragrance-free and suitable for sensitive oily skin."),
        ("What does Effaclar Duo smell like?", "Completely fragrance-free."),
        ("Does it moisturize without adding oil or shine?", "Yes, moisturizes oily skin without adding oils or shine."),
        ("Does 40ml last long?", "Yes, lasts months of daily use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for teens and adults?", "Yes, from ages 12+."),
        ("Does it tighten enlarged pores?", "Yes, improves pore appearance and tightens them."),
        ("How many times daily?", "Morning and evening."),
        ("Does it reduce post-acne dark spots?", "Yes, Niacinamide reduces post-acne redness and dark spots."),
        ("Does it prevent new blemishes?", "Yes, regular use prevents acne bacteria proliferation."),
        ("Is it among La Roche-Posay's most famous products?", "Yes, Effaclar Duo is one of La Roche-Posay's most iconic and bestselling products globally."),
        ("Is it for oily and combination skin?", "Yes, specifically designed for oily and combination acne-prone skin."),
        ("Is it recyclable?", "Yes."),
        ("When do results appear?", "Notable results within 4-8 weeks of regular use."),
        ("Does it work under makeup?", "Yes, good base under makeup due to lightweight gel texture."),
        ("Does it treat blackheads and comedones?", "Yes, Salicylic Acid helps unclog pores from comedones."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1901",
        "sku": "EK-1901",
        "gtin": "3337875598071",
        "brand": "La Roche-Posay",
        "ar": {
            "title": "جل ترطيب وتصحيح البشرة  ايفاكلار ديومن لاروش بوزاي - 40مل",
            "meta_title": "جل إيفاكلار ديو لاروش بوزاي 40مل | إكليل أبها",
            "meta_description": "اشتري جل إيفاكلار ديو من لاروش بوزاي (40 مل). جل طبي بالبروكورال والنياسيناميد لعلاج حب الشباب وتصحيح بشرة الوجه الدهنية. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["لاروش_بوزاي", "إيفاكلار_ديو", "علاج_حب_الشباب", "جل_وجه_دهني", "إكليل_أبها"]
        },
        "en": {
            "title": "La Roche-Posay Effaclar Duo Moisturizing and Correcting Gel - 40ml",
            "meta_title": "La Roche-Posay Effaclar Duo Correcting Gel 40ml | Ekleel Abha",
            "meta_description": "Buy original La Roche-Posay Effaclar Duo Moisturizing and Correcting Gel (40ml). Medical Procerad & Niacinamide gel for acne treatment. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["laroche_posay", "effaclar_duo", "acne_treatment", "oily_skin_gel", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 37 builders complete")
