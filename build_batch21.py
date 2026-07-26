import json, os

def create_product_1810():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول الفم الذهبي لتبييض الأسنان250مل (Golden Teeth Whitening Mouthwash 250ml)</strong> مستحضر الفخامة السويسرية الأكثر تطوراً (Dentissimo Gold) لتفتيح وتبييض الأسنان وحماية الفم بنقاء الذهب ومركبات الطبيعة. يرتكز هذا الغسول الذهبي الاستثنائي على جزيئات الذهب الخالص عيار 24 قيراط (24K Gold Particles)، حمض الهيالورونيك (Hyaluronic Acid)، ومستخلصات الزهور السويسرية المطهرة.</p>
<p>يعمل غسول ديتانسيمو الذهبي على إزالة التصبغات والبقع الصفراء، تعقيم الفم من البكتيريا المسببة للرائحة الكريهة، وترطيب اللثة والأنسجة الفموية بفاعلية فائقة خالية تماماً من الكحول والبارابين، ليمنحكِ ابتسامة ملكية ناصعة البياض ونفساً منعشاً يبث الثقة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تبييض ملكي بجزيئات الذهب 24K:</strong> تزيل البقع والتصبغات وتمنح الأسنان بريقاً ناصعاً.</li>
  <li><strong>ترطيب اللثة بحمض الهيالورونيك:</strong> يجدد خلايا اللثة ويرطب الفم ويمنع التهاب الأنسجة.</li>
  <li><strong>تعقيم الفم ونفس منعش:</strong> يقضي على البكتيريا المسببة لرائحة الفم الكريهة وتراكم البلاك.</li>
  <li><strong>خالي من الكحول والبارابين وSLS:</strong> تركيبة سويسرية فائقة النقاء لا تسبب حرقاناً أو جفافاً.</li>
  <li><strong>حماية مينا الأسنان من التسوس:</strong> يدعم تقوية المينا ويمنع تراكم التكلسات الجيرية.</li>
  <li><strong>عبوة أنيقة سعة 250 مل:</strong> حجم ممتازة ومناسبة للاستخدام الفمي اليومي الراقي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (المكيال):</strong> اسكبي 20 مل من غسول الأسنان الذهبي في غطاء العبوة.</li>
  <li><strong>الخطوة الثانية (المضمضة):</strong> مضمضي الفم جيداً لمدة 30 ثانية مع التمرير بين الأسنان.</li>
  <li><strong>الخطوة الثالثة (البصق):</strong> ابصقي السائل دون شطف بالماء أو تناول الطعام لمدة 30 دقيقة (يُستعمل مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>جزيئات الذهب الخالص (24K Gold Particles):</strong> تمنح تبييضاً ملكياً وحماية مضادة للبكتيريا.</li>
  <li><strong>حمض الهيالورونيك (Hyaluronic Acid):</strong> يجدد ويرطب أنسجة اللثة والفم.</li>
  <li><strong>مستخلصات نباتية سويسرية مطهرة:</strong> تلطف اللثة وتنعش الفم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الفموي للمضمضة فقط؛ لا يبتلع الغسول.</li>
  <li>غير مناسب للأطفال دون سن 6 سنوات.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تفتش عن تبييض فاخر للأسنان، عناية باللثة بحمض الهيالورونيك، ونفس ذهبي منعش خالي من الكحول.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ديتانسيمو / سويس بينت (Dentissimo Gold)</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم / غسولات الأسنان الفاخرة للتبييض</td></tr>
  <tr><th>نوع المنتج</th><td>غسول الفم الذهبي للتبييض والترطيب (250ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>250 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بالفم والأسنان)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان بيضاء براقة، لثة صحية مرطبة ونفس ملكي منعش</td></tr>
  <tr><th>الملمس</th><td>سائل عالي النقاء بجزيئات ذهبية براقة</td></tr>
  <tr><th>العطر</th><td>عطر النعناع والزهور السويسرية الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>جزيئات ذهب 24K، حمض هيالورونيك، سيراميدات، نعناع مطهر</td></tr>
  <tr><th>بلد المنشأ</th><td>سويسرا (Switzerland)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Medpack Swiss Group / Dentissimo</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والأطفال (من 6 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الذهب وحمض الهيالورونيك للأسنان (Dentissimo)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول الفم الذهبي مشكلة تصفر الأسنان، تراجع وترهل اللثة، رائحة الفم الكريهة، وجفاف الفم الناجم عن غسولات الكحول.</p>

<h3>لماذا تنجح تقنية الذهب والهيالورونيك؟</h3>
<p>لأن جزيئات الذهب 24K تمنع نمو البكتيريا وتصقل المينا، بينما يعيد حمض الهيالورونيك ترطيب وتجديد أنسجة اللثة المتهالكة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>المضمضة 30 ثانية:</strong> مضمضي مرتين يومياً بعد تفريش الأسنان.<br>
2. <strong>تجنب الشطف بالماء:</strong> لا تشطفي الفم بالماء فوراً بعد المضمضة لامتصاص الهيالورونيك.<br>
3. <strong>الاستخدام المكمل للمعجون:</strong> استعمليه مع معجون ديتانسيمو الذهبي لنتائج تبييض مضاعفة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "جزيئات الذهب تخدش مينا الأسنان."<br>
<strong>الحقيقة:</strong> جزيئات الذهب السويسرية نانوية فائقة النعومة تصقل المينا بصفاء دون إحداث أي خدوش.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط أيونات الذهب النشطة تكاثر البكتيريا اللاهوائية بالفم، بينما يرتبط حمض الهيالورونيك بمستقبلات الخلايا اللثوية لترميم غشائها.</p>"""

    faqs = [
        ("ما هو غسول الفم الذهبي لتبييض الأسنان250مل؟", "هو غسول فم سويسري فاخر من ديتانسيمو غني بجزيئات الذهب 24K وحمض الهيالورونيك لتبييض الأسنان وعناية اللثة الخالية من الكحول."),
        ("ما هي فوائد جزيئات الذهب عيار 24 قيراط للأسنان؟", "تصقل المينا، تزيل التصبغات، وتوفر حماية ملكية مضادة للبكتيريا."),
        ("ما هي فوائد حمض الهيالورونيك للثة؟", "يرطب أنسجة اللثة، يجدد الخلايا، ويمنع نزيف والتهاب اللثة."),
        ("هل هو خالي من الكحول والبارابين؟", "نعم، خالي 100% من الكحول والبارابين وSLS ومناسب للفم الحساس."),
        ("ما حجم العبوة؟", "تأتي بحجم 250 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اسكبي 20 مل، مضمضي الفم 30 ثانية ثم ابصقي دون شطف بالماء."),
        ("ما هو بلد صنع غسول ديتانسيمو الذهبي؟", "صُنع بفخر في سويسرا بواسطة Medpack Swiss Group."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات ديتانسيمو لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يزيل رائحة الفم الكريهة؟", "نعم، يقضي على البكتيريا المسببة للرائحة الكريهة ويمنح نفساً منعشاً."),
        ("ما هي رائحة غسول الفم الذهبي؟", "يتميز برائحة النعناع والزهور السويسرية المنعشة والفاخرة."),
        ("هل يسبب حرقان بالفم؟", "خلوه من الكحول يمنع أي حرقان أو جفاف بالفم تماماً."),
        ("هل يناسب جميع أنواع الأسنان واللثة؟", "نعم، آمن وممتاز للأسنان الحساسة ولثة الحوامل."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل العبوة 250 مل مناسبة للاستخدام اليومي؟", "نعم، تكفي للاستخدام اليومي المستمر لعدة أسابيع."),
        ("هل يمنع تكلس الجير والبلاك؟", "نعم، يقلل تراكم البلاك والجير على أسطح الأسنان."),
        ("هل العبوة زجاجية أم بلاستيكية؟", "تأتي في عبوة بلاستيكية فاخرة محكمة الإغلاق."),
        ("هل يناسب الأطفال؟", "مناسب للأطفال والبالغين من سن 6 سنوات فما فوق."),
        ("هل ينصح به أطباء الأسنان بسويسرا؟", "نعم، العلامة السويسرية الأولى المعتمدة طبياً للعناية الفاخرة بالفم."),
        ("هل يساعد في تحسين ثبات ابتسامة هوليوود؟", "نعم، يحافظ على بريق وبياض التركيبات وابتسامة هوليوود."),
        ("هل يغير طعم الأكل بعده؟", "لا يغير طعم الأطعمة بعد المضمضة."),
        ("هل يحتوي على الفلورايد؟", "يحتوي على نسبة فلورايد آمنة لتقوية المينا."),
        ("هل القارورة شفافة تظهر جزيئات الذهب؟", "نعم، تظهر الجزيئات الذهبية اللامعة داخل السائل."),
        ("هل يساعد في الوقاية من التسوس؟", "نعم، يحمي الأسنان من النخر والتسوس بفاعلية."),
        ("هل يمنع جفاف الفم ليلاً؟", "نعم، حمض الهيالورونيك يحافظ على رطوبة الفم طوال الليل."),
        ("هل هو غسول الفم الأفخر في إكليل أبها؟", "نعم، الغسول الذهبي الأكثر فخامة وطلباً.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Golden Teeth Whitening Mouthwash 250ml</strong> (Dentissimo Gold) is the pinnacle of Swiss luxury oral care engineered to whiten teeth and rejuvenate gums with pure 24K gold particles and Hyaluronic Acid. Free from alcohol and parabens, it offers an extraordinary whitening and gum-nourishing rinse.</p>
<p>Dentissimo Gold mouthwash sweeps away surface stains, neutralizes bad breath bacteria, and hydrates oral tissues, delivering a royal, brilliant white smile and long-lasting fresh breath confidence.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>24K Gold Whitening Particles:</strong> Gently polish enamel and eliminate surface discoloration.</li>
  <li><strong>Hyaluronic Acid Gum Hydration:</strong> Regenerates gum tissues, seals moisture, and prevents bleeding.</li>
  <li><strong>Antibacterial & Breath Freshening:</strong> Neutralizes odor-causing bacteria and prevents plaque.</li>
  <li><strong>100% Alcohol, Paraben & SLS Free:</strong> Swiss ultra-pure formula causing zero burning or dryness.</li>
  <li><strong>Enamel Strengthening:</strong> Reinforces primary and permanent enamel against cavity decay.</li>
  <li><strong>Sleek 250ml Bottle:</strong> Premium size ideal for daily luxury oral hygiene routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Measure):</strong> Pour 20ml of Golden Whitening Mouthwash into the cap.</li>
  <li><strong>Step 2 (Rinse):</strong> Rinse mouth thoroughly for 30 seconds, swishing between teeth.</li>
  <li><strong>Step 3 (Spit):</strong> Spit out solution without rinsing with water; refrain from eating for 30 minutes (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>24K Gold Particles:</strong> Provide royal whitening polish and antibacterial protection.</li>
  <li><strong>Hyaluronic Acid:</strong> Hydrates and regenerates delicate gum tissues.</li>
  <li><strong>Swiss Botanical Extracts:</strong> Soothe gums and freshen breath naturally.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For oral rinsing application only; do not swallow.</li>
  <li>Not suitable for children under 6 years old.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Swiss luxury 24K gold teeth whitening, Hyaluronic Acid gum care, and an alcohol-free fresh rinse.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Dentissimo Gold / Swissdent</td></tr>
  <tr><th>Category</th><td>Oral Care / Luxury Whitening Mouthwashes</td></tr>
  <tr><th>Product Type</th><td>24K Gold & Hyaluronic Acid Whitening Mouthwash (250ml)</td></tr>
  <tr><th>Volume/Weight</th><td>250 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Oral & Dental Care)</td></tr>
  <tr><th>Finish</th><td>Brilliant white teeth, hydrated gums & royal fresh breath</td></tr>
  <tr><th>Texture</th><td>Clear luxury liquid infused with 24K gold particles</td></tr>
  <tr><th>Fragrance</th><td>Fresh Swiss mint & botanical aroma</td></tr>
  <tr><th>Active Ingredients</th><td>24K Gold Particles, Hyaluronic Acid, Mint, Ceramides</td></tr>
  <tr><th>Country of Origin</th><td>Switzerland</td></tr>
  <tr><th>Manufacturer</th><td>Medpack Swiss Group / Dentissimo</td></tr>
  <tr><th>Age Group</th><td>Adults & Kids (6+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 24K Gold & Hyaluronic Acid Oral Rejuvenation</h2>

<h3>What problem does this solve?</h3>
<p>Golden Teeth Whitening Mouthwash resolves teeth yellowing, gum recession, bad breath, and alcohol dryness.</p>

<h3>Why choose Dentissimo Gold?</h3>
<p>Micro-fine 24K Gold particles polish enamel discoloration while Hyaluronic Acid binds to oral mucosal cells to regenerate gum tissue.</p>"""

    en_faqs = [
        ("What is Golden Teeth Whitening Mouthwash 250ml?", "It is a Swiss luxury 24K Gold and Hyaluronic Acid whitening mouthwash free from alcohol and parabens."),
        ("What are the benefits of 24K Gold particles?", "Polishes enamel, eliminates yellow stains, and provides antibacterial protection."),
        ("What are the benefits of Hyaluronic Acid for gums?", "Hydrates gum tissue, accelerates cell regeneration, and prevents bleeding."),
        ("Is it alcohol-free and paraben-free?", "Yes, 100% free of alcohol, parabens, and SLS for gentle oral care."),
        ("What volume is contained in this bottle?", "It comes in a 250ml luxury bottle."),
        ("How do I use it correctly?", "Pour 20ml, rinse for 30 seconds, and spit out without water rinsing."),
        ("Where is Dentissimo Gold manufactured?", "It is proudly manufactured in Switzerland by Medpack Swiss Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All Dentissimo products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it eliminate bad breath?", "Yes, neutralizes odor-causing bacteria for long-lasting fresh breath."),
        ("What flavor does it have?", "Features a fresh, luxurious Swiss mint aroma."),
        ("Does it cause burning sensations?", "Alcohol-free formulation prevents burning or dry mouth."),
        ("Is it safe for sensitive teeth and gums?", "Yes, safe for sensitive teeth and pregnant women's gums."),
        ("How should I store the bottle?", "Store in a cool, dry place away from heat."),
        ("Is the 250ml bottle economical?", "Yes, provides weeks of daily luxury rinsing."),
        ("Does it prevent tartar and plaque buildup?", "Yes, reduces plaque formation on tooth surfaces."),
        ("Is the bottle glass or plastic?", "Comes in a sleek, durable luxury plastic bottle."),
        ("Is it suitable for children?", "Suitable for adults and children aged 6+."),
        ("Is it Swiss dentist recommended?", "Yes, top recommended Swiss brand for luxury oral care."),
        ("Does it maintain Hollywood smile veneers?", "Yes, preserves brilliance and whiteness of veneers and natural teeth."),
        ("Does it alter food taste after rinsing?", "No, does not alter food taste after use."),
        ("Does it contain fluoride?", "Contains a safe fluoride level to strengthen enamel."),
        ("Are gold particles visible in the liquid?", "Yes, beautiful glistening 24K gold particles are visible in the bottle."),
        ("Does it protect against cavities?", "Yes, fortifies enamel to resist cavity decay."),
        ("Does it prevent overnight mouth dryness?", "Yes, Hyaluronic Acid maintains oral moisture throughout the night."),
        ("Is it the most luxurious mouthwash at Ekleel Abha?", "Yes, the #1 most luxurious whitening mouthwash choice.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1810",
        "sku": "EK-1810",
        "gtin": "7640162327428",
        "category": "العناية بالفم / غسولات الأسنان الفاخرة للتبييض",
        "brand": "Dentissimo",
        "ar": {
            "title": "غسول الفم الذهبي لتبييض الأسنان250مل",
            "meta_title": "غسول الفم الذهبي ديتانسيمو 250مل | صيدلية إكليل أبها",
            "meta_description": "اشتري غسول الفم الذهبي لتبييض الأسنان (250مل). تبييض بجزيئات الذهب 24K وحمض الهيالورونيك خالي من الكحول. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["ديتانسيمو", "غسول_الذهب", "تبييض_الأسنان", "حمض_الهيالورونيك", "إكليل_أبها"]
        },
        "en": {
            "title": "Golden Teeth Whitening Mouthwash 250ml",
            "meta_title": "Golden Teeth Whitening Mouthwash 250ml | Ekleel Abha",
            "meta_description": "Buy original Golden Teeth Whitening Mouthwash (250ml). Swiss 24K Gold & Hyaluronic Acid alcohol-free formula. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["dentissimo", "gold_mouthwash", "teeth_whitening", "hyaluronic_acid", "ekleel_abha"]
        },
        "schema": {
            "brand": "Dentissimo",
            "category": "Oral Care / Mouthwash",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "golden-teeth-whitening-mouthwash-250ml.webp",
            "alt": "Golden Teeth Whitening Mouthwash 250ml",
            "title": "Golden Teeth Whitening Mouthwash 250ml"
        }
    }

def create_product_1811():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>جل بيو اويل للبشرة الجافة، 50 مل (Bio-Oil Dry Skin Gel, 50 ml)</strong> الابتكار الثوري العالمي الأحدث لإعادة الترطيب المكثف والعميق للبشرة شديدة الجفاف والتطير. يمتاز هذا الجل من بيو أويل (Bio-Oil) بتركيبة فريدة ترتكز على 84% من الزيوت المغذية والزبدة الشافية مع 3% فقط من الماء (بعكس الكريمات التقليدية التي تحتوي على 70% ماء)، مما يمنح الجلد حجاب ترطيب ينفذ بسرعة ويرمم حاجز البشرة التالف.</p>
<p>يجمع جل بيو أويل بين فوائد زبدة الشيا، نبتة البابونج، روزماري، فيتامين A، وفيتامين E، ليمنح بشرتكِ نضارة حريرية وترطيباً تدوم فاعليته لـ 24 ساعة دون ترك أثر دهني لزج على الجلد.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب مكثف بـ 84% زيوت مغذية:</strong> يعوض ترطيب البشرة شديدة الجفاف 3 أضعاف مقارنة بالكريمات العادية.</li>
  <li><strong>ترميم حاجز البشرة التالف:</strong> يمنع تبخر رطوبة الجلد (TEWL) ويقضي على القشور والتطير.</li>
  <li><strong>غني بزبدة الشيا وفيتامينات A و E:</strong> يغذي خلايا الجلد ويزيد المرونة والإشراقة.</li>
  <li><strong>خلاصة البابونج والروز ماري المهدئة:</strong> تلطف تهيج واحمرار البشرة الحساسة والجافة.</li>
  <li><strong>قوام جل فريد سريع الامتصاص:</strong> يذوب عند ملامسة الجلد ويمتص فورياً دون لزوجة.</li>
  <li><strong>عبوة مدمجة 50 مل:</strong> حجم ممتازة ومثالية للعناية باليدين، الوجه، والجسم والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق):</strong> وضعي كمية صغيرة جداً من جل بيو أويل على البشرة الجافة (كمية أقل بكثير من الكريم العادي).</li>
  <li><strong>الخطوة الثانية (التدليك):</strong> دلكي بحركات دائرية خفيفة حتى يذوب الجل وينفذ بالكامل.</li>
  <li><strong>الخطوة الثالثة (التكرار):</strong> استعمليه مرتين يومياً صباحاً ومساءً لنتائج ترطيب مذهلة.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زبدة الشيا والزيوت النباتية (84% Formulation):</strong> تغذي غشاء البشرة وتحفظ الماء.</li>
  <li><strong>فيتامين A وفيتامين E والبابونج:</strong> يسرعان تجدد الخلايا ويهدئان التهيج الجلدي.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على البشرة فقط.</li>
  <li>تجنبي ملامسة الجل المباشرة للعينين أو الجروح المفتوحة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من البشرة شديدة الجفاف، التشققات، التطير، وترغب في ترطيب بيو أويل المبتكر.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيو أويل (Bio-Oil)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / جل وترطيب البشرة شديدة الجفاف</td></tr>
  <tr><th>نوع المنتج</th><td>جل علاج ترطيب البشرة شديدة الجفاف (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة شديدة الجفاف، المتقشرة، والحساسة</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة، مرنة، مرطبة عميقاً وخالية من التطير والقشور</td></tr>
  <tr><th>الملمس</th><td>جل وردي فاخر يذوب وينفذ فورياً بالبشرة</td></tr>
  <tr><th>العطر</th><td>عطر الزهور العطري الخفيف من بيو أويل</td></tr>
  <tr><th>المكونات النشطة</th><td>زبدة الشيا، فيتامين A، فيتامين E، زيت البابونج والروزماري</td></tr>
  <tr><th>بلد المنشأ</th><td>جنوب إفريقيا / جنوب إفريقيا (Union Swiss)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Union Swiss / Bio-Oil</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد جل بيو أويل للبشرة الجافة (Bio-Oil Gel)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج جل بيو أويل مشكلة تبخر ماء البشرة شديدة الجفاف، قشور الوجه والجسم، وتلف حاجز البشرة الدهني.</p>

<h3>لماذا تنجح تركيبة الجل المبتكرة؟</h3>
<p>لأنها تستبدل ماء الكريمات التقليدي (70%) بنسبة 84% من الزيوت المغذية، مما يغلف الجلد ويمنع التبخر بنسبة 100%.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام كمية صغيرة:</strong> كمية صغيرة جداً تكفي لمساحة واسعة من الجلد.<br>
2. <strong>التدليك حتى يذوب:</strong> دلكي الجل بين الأصابع قبل التطبيق ليذوب بسلاسة.<br>
3. <strong>الاستخدام المباشر بعد الاستحمام:</strong> وضعي الجل على بشرة رطبة خفيفاً لزيادة الامتصاص.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الجل المغذي بالزيوت يترك أثراً لزجاً وثقيلاً."<br>
<strong>الحقيقة:</strong> جل بيو أويل مصمم بتركيبة تمتص فورياً داخل المسام دون إبقاء لزوجة دهنية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتكامل ليبيدات زبدة الشيا والفيتامينات مع الطبقة القرنية (Stratum Corneum)، مما يقلل معدل التبخر الجلدي (TEWL) بنسبة 98%.</p>"""

    faqs = [
        ("ما هو جل بيو اويل للبشرة الجافة 50 مل؟", "هو جل ترطيب مبتكر يحتوي على 84% زيوت مغذية وزبدة الشيا لعلاج البشرة شديدة الجفاف والقشور."),
        ("ما هي فوائد نسبة 84% زيوت في الجل؟", "تغذي خلايا الجلد وتمنع تبخر الماء 3 أضعاف مقارنة بالكريمات المائية العادية."),
        ("هل يترك ملمساً دهنياً لزجاً؟", "لا، يذوب عند ملامسة البشرة ويمتص فورياً دون لزوجة."),
        ("ما حجم العبوة؟", "تأتي بحجم 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية صغيرة جداً ودلكي بحركات دائرية حتى الامتصاص الكامل مرتين يومياً."),
        ("هل يناسب بشرة الوجه والجسم معاً؟", "نعم، آمن وممتاز لبشرة الوجه، اليدين، الأكواع، وكامل الجسم."),
        ("ما هو بلد صنع بيو أويل؟", "صُنع بفخر في جنوب إفريقيا بواسطة Union Swiss."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيو أويل لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يهدئ الحكة الناجمة عن الجفاف؟", "نعم، يلطف تهيج وحكة الجلد الجاف فورياً."),
        ("ما هي رائحة جل بيو أويل؟", "يتميز برائحة الزهور الناعمة واللطيفة المميزة لبيو أويل."),
        ("هل يناسب البشرة الحساسة؟", "تركيبة مجربة جلدياً ومناسبة للبشرة الحساسة والشديدة الجفاف."),
        ("هل العبوة 50 مل مناسبة للسفر والحقيبة؟", "نعم، عبوة مدمجة وأنيقة مثالية لحمل الحقيبة والسفر."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل يناسب جميع الأعمار؟", "مناسب للأطفال والبالغين من سن 3 سنوات فما فوق."),
        ("هل يعالج قشور الوجه والجسم؟", "نعم، يقضي على القشور والتطير ويرمم الجلد."),
        ("هل يمكن استخدامه للأكواع والركب؟", "ممتاز جداً لتنعيم الأكواع والركب والكعبين الجافة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة دائرية شفافة بغطاء محكم الحماية."),
        ("هل يحتوي على فيتامين A و E؟", "نعم، مدعم بفيتامينات A و E لزيادة النضارة والمرونة."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُفضل استخدامه مرتين يومياً (صباحاً ومساءً)."),
        ("هل يناسب جفاف الشتاء؟", "ممتاز جداً لحماية البشرة من جفاف وبرودة الشتاء."),
        ("هل يمنح حس نضارة وإشراقة؟", "نعم، يعيد للبشرة مظهرها المشرق والحيوي."),
        ("هل يغني عن كريمات الترطيب العادية؟", "يعطي ترطيباً أعمق وأطول بكثير من الكريمات العادية."),
        ("هل يناسب الحوامل؟", "آمن وممتاز لترطيب بشرة الحوامل الجافة."),
        ("هل يمتص بسرعة؟", "نعم، ينفذ فورياً في خلايا الجلد."),
        ("هل هو الجل المرطب الأول عالمياً للجفاف؟", "نعم، الابتكار الأول الحائز على جوائز تجميلية عالمية.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Bio-Oil Dry Skin Gel, 50 ml</strong> is the globally award-winning, revolutionary hydration gel formulation designed to intensively restore extremely dry, flaking skin. Engineered by Bio-Oil, it replaces the traditional 70% water found in creams with an 84% nutrient-rich oil and Shea butter gel matrix with only 3% water.</p>
<p>Combining the restorative powers of Shea Butter, Chamomile Oil, Rosemary Oil, Vitamin A, and Vitamin E, Bio-Oil Dry Skin Gel melts into skin instantly, locking in deep 24-hour hydration without leaving an oily or sticky residue.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intensive 84% Nourishing Oil Gel Matrix:</strong> Replenishes dry skin moisture 3x more effectively than water creams.</li>
  <li><strong>Restores Compromised Lipid Barrier:</strong> Stops transepidermal water loss (TEWL) and clears skin flaking.</li>
  <li><strong>Enriched with Shea Butter & Vitamins A & E:</strong> Feeds skin cells to restore elastic suppleness and radiance.</li>
  <li><strong>Soothing Chamomile & Rosemary Oils:</strong> Calms redness and irritation associated with dry skin.</li>
  <li><strong>Unique Fast-Melting Gel Texture:</strong> Melts on contact with skin and absorbs instantly without stickiness.</li>
  <li><strong>Compact 50ml Jar:</strong> Ideal high-value size for face, hands, body, and travel use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply):</strong> Apply a small amount of Bio-Oil Dry Skin Gel onto dry skin (use much less than traditional creams).</li>
  <li><strong>Step 2 (Massage):</strong> Massage in light circular motions until the gel melts and fully absorbs.</li>
  <li><strong>Step 3 (Repeat):</strong> Use twice daily, morning and evening, for maximum hydration results.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Shea Butter & Plant Oils (84% Base):</strong> Nourish the epidermal barrier and seal in moisture.</li>
  <li><strong>Vitamin A, Vitamin E & Chamomile:</strong> Accelerate cell turnover and soothe skin flaring.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical skin application only.</li>
  <li>Avoid direct contact with eyes or open wounds.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with extremely dry, flaking, or tight skin seeking Bio-Oil's revolutionary oil-gel hydration.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Bio-Oil</td></tr>
  <tr><th>Category</th><td>Skincare / Extremely Dry Skin Gel Treatments</td></tr>
  <tr><th>Product Type</th><td>84% Oil-Gel Hydrating Dry Skin Treatment (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Extremely Dry, Flaking, Tight & Sensitive Skin</td></tr>
  <tr><th>Finish</th><td>Deeply hydrated, soft, elastic & flake-free skin</td></tr>
  <tr><th>Texture</th><td>Melting pink oil-gel matrix absorbing instantly</td></tr>
  <tr><th>Fragrance</th><td>Subtle floral Bio-Oil signature scent</td></tr>
  <tr><th>Active Ingredients</th><td>Shea Butter, Vitamin A, Vitamin E, Chamomile & Rosemary Oils</td></tr>
  <tr><th>Country of Origin</th><td>South Africa (Union Swiss)</td></tr>
  <tr><th>Manufacturer</th><td>Union Swiss / Bio-Oil</td></tr>
  <tr><th>Age Group</th><td>All Ages (3+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 84% Oil-Gel Matrix & Barrier Recovery</h2>

<h3>What problem does this solve?</h3>
<p>Bio-Oil Dry Skin Gel resolves extreme skin dryness, flaking, tight discomfort, and transepidermal water loss.</p>

<h3>Why choose Bio-Oil Gel?</h3>
<p>By replacing water with an 84% oil-gel matrix, it forms a 100% occlusive barrier that stops water evaporation for 24 hours.</p>"""

    en_faqs = [
        ("What is Bio-Oil Dry Skin Gel 50 ml?", "It is a revolutionary hydrating gel formulated with 84% nourishing oils and Shea Butter to treat extremely dry skin."),
        ("What are the benefits of 84% oils in the gel?", "Provides 3x deeper hydration than water creams by creating a moisture-sealing lipid barrier."),
        ("Does it leave a greasy sticky residue?", "No, melts on skin contact and absorbs rapidly without leaving greasy heaviness."),
        ("What volume is contained in this jar?", "It comes in a compact 50ml jar."),
        ("How do I apply it correctly?", "Apply a small amount and massage gently until absorbed twice daily."),
        ("Is it safe for face and body?", "Yes, safe and effective for facial skin, hands, elbows, knees, and full body."),
        ("Where is Bio-Oil manufactured?", "It is proudly manufactured in South Africa by Union Swiss."),
        ("How do I verify authenticity at Ekleel Abha?", "All Bio-Oil products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it soothe dry skin itching?", "Yes, calms dry skin tightness, flaring, and itching instantly."),
        ("What scent does Bio-Oil Gel have?", "Features the subtle, pleasant signature floral Bio-Oil fragrance."),
        ("Is it suitable for sensitive skin?", "Dermatologically tested and safe for sensitive and extremely dry skin."),
        ("Is the 50ml jar travel-friendly?", "Yes, compact clear tub fits easily into travel bags and purses."),
        ("How should I store the jar?", "Store in a cool, dry place away from direct sunlight."),
        ("Is it suitable for all ages?", "Safe for adults and children aged 3+."),
        ("Does it clear flaking skin?", "Yes, clears dry flaking patches and restores skin smoothness."),
        ("Is it effective for dry elbows and knees?", "Yes, highly effective at softening rough dry elbows, knees, and heels."),
        ("Is the jar securely sealed?", "Yes, comes in a sturdy round jar with a screw-top lid."),
        ("Does it contain Vitamins A & E?", "Yes, enriched with Vitamins A & E for cell renewal and elasticity."),
        ("How often should I use it?", "Use twice daily, morning and evening."),
        ("Is it great for winter dryness?", "Yes, essential for protecting skin against harsh winter cold dryness."),
        ("Does it restore skin radiance?", "Yes, restores a healthy, radiant glow to dull dry skin."),
        ("Does it outperform regular creams?", "Provides longer-lasting occlusive hydration than traditional water creams."),
        ("Is it safe during pregnancy?", "Yes, safe and excellent for hydrating pregnant skin."),
        ("Does it absorb quickly?", "Yes, absorbs completely into skin cells within seconds."),
        ("Is it an award-winning dry skin innovation?", "Yes, globally celebrated as the #1 dry skin gel innovation.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1811",
        "sku": "EK-1811",
        "gtin": "6001159119166",
        "category": "العناية بالبشرة / جل وترطيب البشرة شديدة الجفاف",
        "brand": "Bio-Oil",
        "ar": {
            "title": "جل بيو اويل للبشرة الجافة، 50 مل",
            "meta_title": "جل بيو اويل للبشرة الجافة 50مل | صيدلية إكليل أبها",
            "meta_description": "اشتري جل بيو اويل للبشرة الجافة (50 مل). ترطيب مكثف بـ 84% زيوت مغذية وزبدة الشيا. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بيو_اويل", "جل_بيو_اويل", "البشرة_الجافة", "زبدة_الشيا", "إكليل_أبها"]
        },
        "en": {
            "title": "Bio-Oil Dry Skin Gel, 50 ml",
            "meta_title": "Bio-Oil Dry Skin Gel 50ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Bio-Oil Dry Skin Gel (50 ml). 84% oil-gel matrix with Shea Butter for extreme dry skin. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["bio_oil", "dry_skin_gel", "shea_butter", "intense_hydration", "ekleel_abha"]
        },
        "schema": {
            "brand": "Bio-Oil",
            "category": "Skincare / Dry Skin Gel",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "bio-oil-dry-skin-gel-50ml.webp",
            "alt": "Bio-Oil Dry Skin Gel 50 ml",
            "title": "Bio-Oil Dry Skin Gel 50 ml"
        }
    }

def create_product_1812():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>بيو أويل زيت لعلاج الندوب وعلامات التمدد - 60 مل (Bio-Oil Skincare Oil - 60ml)</strong> الزيت العلاجي الأسطوري المفضل والأرقى عالمياً الموصى به طبياً لتحسين مظهر الندوب (Scars)، علامات تمدد الجلد (Stretch Marks)، وتفاوت لون البشرة. يرتكز هذا الزيت المتطور من بيو أويل (Bio-Oil) على الزيت الابتكاري الخفيف الموثوق (PurCellin Oil)، المعزز بالفيتامينات المغذية A و E وخلاصة زيوت اللافندر، الروز ماري، البابونج، والخزامى.</p>
<p>يمتاز زيت بيو أويل بقدرته المذهلة على التغلغل العميق في أدمة الجلد دون ترك أي أثر دهني، مما يرطب البشرة الجافة، يعيد المرونة للأنسجة التالفة، ويقلل مظهر الندوب القديمة والحديثة وخطوط الحمل بفاعلية مثبتة سريرياً.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تحسين مظهر الندوب وعلامات التمدد:</strong> يخفف أثر الندوب الجراحية وخطوط تمدد الحمل وتغير الوزن.</li>
  <li><strong>توحيد لون البشرة والتصبغات:</strong> يقلل مظهر البقع الداكنة وتفاوت لون الوجه والجسم.</li>
  <li><strong>مدعم بـ PurCellin Oil المبتكر:</strong> يمنح الزيت قواماً خفيفاً ينفذ في الجلد فورياً دون لزوجة.</li>
  <li><strong>غني بفيتامينات A و E وخلاصات النباتات:</strong> يحفز تجدد خلايا الجلد ويرمم الكولاجين التالف.</li>
  <li><strong>ترطيب وتنعيم البشرة الجافة والمجهدة:</strong> يعيد المرونة والنعومة للجلد الجاف والمجعد.</li>
  <li><strong>عبوة أنيقة سعة 60 مل:</strong> حجم ممتازة ومناسبة للعناية اليومية المركزة والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق):</strong> وضعي قطرات من زيت بيو أويل على المنطقة المراد علاجها (الندوب، خطوط التمدد، أو الوجه).</li>
  <li><strong>الخطوة الثانية (التدليك):</strong> دلكي بحركات دائرية خفيفة باستخدام أطراف الأصابع حتى الامتصاص الكامل.</li>
  <li><strong>الخطوة الثالثة (التكرار):</strong> يُستعمل مرتين يومياً لمدة 3 أشهر على الأقل للحصول على أفضل النتائج.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت PurCellin Oil المبتكر:</strong> يقلل كثافة الزيت ويضمن امتصاص الفيتامينات عميقاً.</li>
  <li><strong>فيتامينات A و E وزيوت نباتية:</strong> تعزز مرونة أنسجة الكولاجين وتوحد لون الجلد.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على الجلد فقط؛ لا يوضع على الجروح المفتوحة أو البشرة المتهيجة.</li>
  <li>تجنبي ملامسة الزيت المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من الندوب، علامات تمدد الجلد للحوامل، التصبغات، وجفاف البشرة وتفتش عن بيو أويل الأصلي.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيو أويل (Bio-Oil)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / زيوت علاج الندوب وعلامات التمدد</td></tr>
  <tr><th>نوع المنتج</th><td>زيت علاج الندوب والتمدد وتوحيد لون البشرة (60ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>60 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (بما في ذلك الحساسة والحوامل)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة مرنة، موحدة اللون، مخففة الندوب وخطوط التمدد</td></tr>
  <tr><th>الملمس</th><td>زيت خفيف جداً يمتص فورياً غير دهني</td></tr>
  <tr><th>العطر</th><td>عطر الزهور واللافندر العطري الخفيف</td></tr>
  <tr><th>المكونات النشطة</th><td>PurCellin Oil، فيتامين A، فيتامين E، زيت اللافندر والبابونج</td></tr>
  <tr><th>بلد المنشأ</th><td>جنوب إفريقيا (Union Swiss)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Union Swiss / Bio-Oil</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد PurCellin Oil وعلاج الندوب (Bio-Oil)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج زيت بيو أويل مشكلة ظهور الندوب الجراحية وناتجة الحبوب، خطوط تمدد الحمل (Stretch Marks)، وتفاوت لون البشرة.</p>

<h3>لماذا تنجح تقنية PurCellin Oil؟</h3>
<p>لأن PurCellin Oil يقلل سمك الزيت، مما يضمن نفاذ الفيتامينات A و E داخل عمق الأدمة لترميم ألياف الكولاجين.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>البدء المبكر أثناء الحمل:</strong> استعملي بيو أويل من الشهر الرابع للحمل للوقاية من التمدد.<br>
2. <strong>التدليك مرتين يومياً:</strong> دلكي بحركات دائرية لمدة 3 أشهر متواصلة لنتائج مثبتة.<br>
3. <strong>التطبيب على بشرة نظيفة:</strong> ضعي الزيت بعد الاستحمام مباشرة للامتصاص الأعلى.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "زيوت العناية بالبشرة تسبب انسداد المسام والحبوب."<br>
<strong>الحقيقة:</strong> زيت بيو أويل مصمم بتركيبة غير كوميدوجينيك خفيفة تنفذ بالكامل دون سد المسام.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتغلغل الفيتامينات والزيوت العطرية في الطبقة الوسطى (Dermis)، حيث تحفز إعادة بناء الروابط البروتينية وترمم أنسجة الندوب.</p>"""

    faqs = [
        ("ما هو بيو أويل زيت لعلاج الندوب وعلامات التمدد 60 مل؟", "هو زيت علاجي عالمي مثبت سريرياً لتحسين مظهر الندوب، علامات تمدد الحامل، وتوحيد لون البشرة الجافة."),
        ("ما هي فوائد زيت PurCellin Oil المبتكر؟", "يقلل سمك الزيت ويضمن نفاذ الفيتامينات A و E في عمق أدمة الجلد دون لزوجة."),
        ("هل يمنع ويخفف علامات تمدد الحمل؟", "نعم، مثبت سريرياً في تحسين مرونة الجلد والحد من خطوط التمدد أثناء وبعد الحمل."),
        ("ما حجم العبوة؟", "تأتي بحجم 60 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "دلكي قطرات من الزيت بحركات دائرية على المنطقة المراد علاجها مرتين يومياً لمدة 3 أشهر على الأقل."),
        ("هل يناسب بشرة الوجه والجسم؟", "نعم، آمن وممتاز لبشرة الوجه، البطن، الوركين، والجسم بالكامل."),
        ("ما هو بلد صنع بيو أويل؟", "صُنع بفخر في جنوب إفريقيا بواسطة Union Swiss."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيو أويل لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يساعد في توحيد لون البشرة والتصغبات؟", "نعم، يقلل مظهر البقع الداكنة وتفاوت لون الوجه والجسم."),
        ("ما هي رائحة زيت بيو أويل؟", "يتميز برائحة اللافندر والزهور الخفيفة المبهجة والمنعشة."),
        ("هل يترك أثراً دهنياً لزجاً؟", "لا، يمتص فورياً في الجلد بفضل تركيبة PurCellin Oil الخفيفة."),
        ("هل يناسب البشرة الحساسة؟", "نعم، تركيبة مجربة جلدياً ومناسبة لجميع أنواع البشرة."),
        ("متى يجب البدء باستخدامه أثناء الحمل؟", "يُفضل البدء باستخدامه من المجسم الثاني للحمل (الشهر الرابع)."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل العبوة 60 مل مناسبة للسفر والحقيبة؟", "نعم، حجم زجاجة مدمج وأنيق مثالي لحمل الحقيبة والسفر."),
        ("هل يساعد في تنعيم البشرة المجهدة والمجعدة؟", "نعم، يعيد الترطيب والمرونة للجلد المجعد والجاف."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب لكلا الجنسين."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة أنيقة بقطارة محكمة لمنع التسرب."),
        ("هل يحتوي على فيتامين A و E؟", "نعم، غني بفيتامينات A و E لزيادة النضارة وتجديد الخلايا."),
        ("هل يوضع على الجروح الحديثة؟", "يمنع وضعه على الجروح المفتوحة؛ يوضع فقط بعد اندمال الجرح."),
        ("هل ينصح به أطباء الجلدية والنساء؟", "نعم، الزيت رقم 1 الموصى به طبياً للندوب والتمدد عالمياً."),
        ("هل يمكن وضعه قبل المرطب اليومي؟", "نعم، دلكي الزيت أولاً حتى الامتصاص ثم ضعي كريمكِ اليومي."),
        ("هل يعالج آثار حب الشباب؟", "نعم، يساعد في تنعيم وتخفيف آثار وتصبغات حب الشباب القديمة."),
        ("هل يمتص بسرعة؟", "نعم، ينفذ فورياً داخل خلايا الجلد."),
        ("هل يتوفر بأحجام أخرى لدى إكليل أبها؟", "نعم، تتوفر أحجام 60مل، 125مل، و200مل لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Bio-Oil Skincare Oil - 60ml</strong> is the world's #1 dermatologist-recommended specialist skincare oil clinically proven to improve the appearance of scars, stretch marks, and uneven skin tone. Engineered by Bio-Oil, it features the breakthrough ingredient PurCellin Oil, enriched with Vitamins A & E, Lavender, Rosemary, and Chamomile oils.</p>
<p>Bio-Oil Skincare Oil absorbs deeply into the dermal layers without leaving a greasy residue, restoring moisture to aging or dehydrated skin and visibly fading stretch marks and scars over time.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Fades Scars & Stretch Marks:</strong> Clinically proven to minimize surgical scars, acne marks, and pregnancy stretch lines.</li>
  <li><strong>Evens Skin Tone & Pigmentation:</strong> Fades dark spots, sun discoloration, and uneven facial skin tone.</li>
  <li><strong>Infused with Breakthrough PurCellin Oil:</strong> Ensures rapid absorption of vitamins deep into skin without greasiness.</li>
  <li><strong>Enriched with Vitamins A & E & Botanicals:</strong> Stimulates collagen renewal and improves skin elasticity.</li>
  <li><strong>Deep Hydration for Dehydrated & Aging Skin:</strong> Smooths fine lines and restores supple moisture to dry skin.</li>
  <li><strong>Sleek 60ml Bottle:</strong> Ideal high-value size for daily targeted treatment and travel kits.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply):</strong> Apply a few drops of Bio-Oil Skincare Oil onto target skin areas (scars, stretch marks, or face).</li>
  <li><strong>Step 2 (Massage):</strong> Massage in gentle circular motions using fingertips until fully absorbed.</li>
  <li><strong>Step 3 (Repeat):</strong> Apply twice daily for a minimum of 3 months for optimal clinical results.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>PurCellin Oil:</strong> Reduces oil viscosity ensuring rapid absorption of active vitamins into skin.</li>
  <li><strong>Vitamins A & E with Natural Plant Oils:</strong> Restructure collagen fibers and even skin tone.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical skin application only; do not apply on broken skin or open wounds.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone looking to fade scars, pregnancy stretch marks, uneven skin tone, or hydrate aging dry skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Bio-Oil</td></tr>
  <tr><th>Category</th><td>Skincare / Specialist Scar & Stretch Mark Oils</td></tr>
  <tr><th>Product Type</th><td>PurCellin Oil Scar, Stretch Mark & Skincare Oil (60ml)</td></tr>
  <tr><th>Volume/Weight</th><td>60 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Including Sensitive & Pregnant Skin)</td></tr>
  <tr><th>Finish</th><td>Elastic, supple, even-toned & scar-faded skin</td></tr>
  <tr><th>Texture</th><td>Ultra-light fast-absorbing non-greasy oil</td></tr>
  <tr><th>Fragrance</th><td>Subtle Lavender & floral Bio-Oil scent</td></tr>
  <tr><th>Active Ingredients</th><td>PurCellin Oil, Vitamin A, Vitamin E, Lavender & Chamomile Oils</td></tr>
  <tr><th>Country of Origin</th><td>South Africa (Union Swiss)</td></tr>
  <tr><th>Manufacturer</th><td>Union Swiss / Bio-Oil</td></tr>
  <tr><th>Age Group</th><td>All Ages (3+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of PurCellin Oil & Scar Dermal Restructuring</h2>

<h3>What problem does this solve?</h3>
<p>Bio-Oil Skincare Oil resolves surgical scars, pregnancy stretch marks, hyperpigmentation, and aging skin dehydration.</p>

<h3>Why choose Bio-Oil Skincare Oil?</h3>
<p>PurCellin Oil decreases liquid viscosity, delivering Vitamins A & E deep into the dermis to rebuild broken collagen fibers.</p>"""

    en_faqs = [
        ("What is Bio-Oil Skincare Oil 60ml?", "It is the globally #1 clinical specialist skincare oil formulated to fade scars, stretch marks, and uneven skin tone."),
        ("What are the benefits of PurCellin Oil?", "Reduces oil thickness, allowing active vitamins to absorb deeply into skin without greasiness."),
        ("Does it prevent and fade pregnancy stretch marks?", "Yes, clinically proven to improve skin elasticity and fade stretch marks during and after pregnancy."),
        ("What volume is contained in this bottle?", "It comes in a sleek 60ml bottle."),
        ("How do I apply it correctly?", "Massage a few drops in circular motions onto target areas twice daily for at least 3 months."),
        ("Is it safe for face and body?", "Yes, safe and effective for facial skin, tummy, hips, and full body areas."),
        ("Where is Bio-Oil manufactured?", "It is proudly manufactured in South Africa by Union Swiss."),
        ("How do I verify authenticity at Ekleel Abha?", "All Bio-Oil products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it help even out skin tone and dark spots?", "Yes, fades dark spots, hyperpigmentation, and uneven skin tone."),
        ("What scent does Bio-Oil Skincare Oil have?", "Features a light, soothing Lavender and herbal floral aroma."),
        ("Does it leave a heavy greasy feel?", "No, PurCellin Oil formulation ensures instant absorption without oily residue."),
        ("Is it safe for sensitive skin?", "Yes, dermatologically tested and suitable for all skin types."),
        ("When should expecting mothers start using it?", "Start applying from the second trimester (fourth month of pregnancy)."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct sunlight."),
        ("Is the 60ml bottle travel-friendly?", "Yes, compact bottle size fits easily into travel kits and handbags."),
        ("Does it hydrate aging dry skin?", "Yes, restores moisture and elasticity to aging and dry skin."),
        ("Can both men and women use it?", "Yes, suitable for both men and women."),
        ("Is the bottle cap leak-proof?", "Yes, comes in a sturdy bottle with a dropper dispenser cap."),
        ("Does it contain Vitamins A & E?", "Yes, enriched with Vitamins A & E for cell turnover and collagen renewal."),
        ("Can it be applied on open wounds?", "No, apply only after wounds have completely healed."),
        ("Is it dermatologist and OB/GYN recommended?", "Yes, the #1 globally recommended specialist oil for scars and stretch marks."),
        ("Can it be worn under daily moisturizers?", "Yes, apply oil first until absorbed, then follow with daily moisturizer."),
        ("Does it fade acne scars?", "Yes, smooths and fades old and new acne scars."),
        ("Does it absorb quickly?", "Yes, absorbs completely into skin cells within seconds."),
        ("Are other sizes available at Ekleel Abha?", "Yes, Ekleel Abha offers 60ml, 125ml, and 200ml Bio-Oil sizes.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1812",
        "sku": "EK-1812",
        "gtin": "6001159113126",
        "category": "العناية بالبشرة / زيوت علاج الندوب وعلامات التمدد",
        "brand": "Bio-Oil",
        "ar": {
            "title": "بيو أويل زيت لعلاج الندوب وعلامات التمدد - 60 مل",
            "meta_title": "زيت بيو اويل لعلاج الندوب والتمدد 60مل | صيدلية إكليل أبها",
            "meta_description": "اشتري بيو أويل زيت لعلاج الندوب وعلامات التمدد (60 مل). مثبت سريرياً بتوظيف PurCellin Oil وتوحيد لون البشرة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بيو_اويل", "زيت_بيو_اويل", "علاج_الندوب", "علامات_التمدد", "إكليل_أبها"]
        },
        "en": {
            "title": "Bio-Oil Skincare Oil - 60ml",
            "meta_title": "Bio-Oil Skincare Oil 60ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Bio-Oil Skincare Oil (60ml). Fades scars, pregnancy stretch marks, & evens skin tone with PurCellin Oil. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["bio_oil", "skincare_oil", "scar_treatment", "stretch_marks", "ekleel_abha"]
        },
        "schema": {
            "brand": "Bio-Oil",
            "category": "Skincare / Body Oil",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "bio-oil-skincare-oil-60ml.webp",
            "alt": "Bio-Oil Skincare Oil 60ml",
            "title": "Bio-Oil Skincare Oil 60ml"
        }
    }

def create_product_1813():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم تخفيف الام العضلات من جيليجا، 20 جم (Geliga Muscle Pain Relief Cream, 20g)</strong> المسكن الموضعي الحراري الأسرع والأكثر فاعلية لتسكين آلام العضلات، التيبس، والشد العضلي الناتج عن الرياضة أو المجهود البدني. يرتكز هذا الكريم الطبي من جيليجا (Geliga Muscular Balm / Cream) على فورمولا منشطة تجمع بين ساليسيلات الميثيل (Methyl Salicylate) والمنثول الطبيعي (Menthol) وزيت الكافور.</p>
<p>يمتاز كريم جيليجا بتوفير دفء مهدئ ينفذ في عمق الأنسجة العضلية والمفاصل، مما يسرع تدفق الدورة الدموية، يزيل تشنج العضلات، ويمنحكِ راحة فورية تدوم لعدة ساعات بعد كل تدليك.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تسكين راحة فورية لآلام العضلات:</strong> يهدئ الشد العضلي، التيبس، وآلام الرقبة والظهر.</li>
  <li><strong>مزيج ساليسيلات الميثيل والمنثول:</strong> يوفر دفئاً منشطاً يخترق الأنسجة العضلية عميقاً.</li>
  <li><strong>تنشيط الدورة الدموية بالمنطقة المصابة:</strong> يسرع اندمال تشنجات العضلات والإجهاد الرياضي.</li>
  <li><strong>امتصاص موصلي سريع دون لزوجة:</strong> يدلك بسهولة وينفذ بالبشرة لراحة سريعة.</li>
  <li><strong>مثالي للرياضيين وكبار السن:</strong> يسكن الآلام المفاصل العضلية بعد التمارين والمجهود الشاق.</li>
  <li><strong>أنبوب مدمج وزن 20 جم:</strong> حجم ممتاز ومثالي لحقيبة الرياضة والسفر والتنقل.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> نظفي المنطقة المصابة بالماء الفاتر وجففيها.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي كمية مناسبة من كريم جيليجا على منطقة الألم (الظهر، الرقبة، الكتف، أو الساقين).</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي بحركات دائرية خفيفة 2 إلى 3 مرات يومياً حتى ينفذ الكريم بالكامل.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>ساليسيلات الميثيل (Methyl Salicylate):</strong> مسكن موضعي مضاد لالتهاب العضلات والمفاصل.</li>
  <li><strong>المنثول وزيت الكافور (Menthol & Camphor Oil):</strong> يوفران الدفء والانتعاش ويهدئان إشارات الألم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي فقط؛ لا يوضع على الجروح المفتوحة أو البشرة المتهيجة أو بالقرب من العينين.</li>
  <li>تجنبي تغطية المنطقة بضمادات محكمة الحرارة بعد الرش أو التطبيق.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>للرياضيين، كبار السن، ولكل من يعاني من آلام العضلات، الشد العضلي، وتيبس الظهر والرقبة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جيليجا (Geliga)</td></tr>
  <tr><th>الفئة</th><td>الأدوية والمستلزمات الطبية / مسكنات آلام العضلات والمفاصل الموضعية</td></tr>
  <tr><th>نوع المنتج</th><td>كريم مسكن ومسخن لآلام العضلات والشد العضلي (20g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>20 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (تطبيب موضي على العضلات والمفاصل)</td></tr>
  <tr><th>المظهر النهائي</th><td>استرخاء عضلات، تسكين الألم، وراحة حرارية فورية</td></tr>
  <tr><th>الملمس</th><td>كريم زيتي مسخن يمتص بالتدليك</td></tr>
  <tr><th>العطر</th><td>عطر المنثول وساليسيلات الميثيل الطبي المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>ساليسيلات الميثيل، منثول، زيت الكافور، زيت النعناع</td></tr>
  <tr><th>بلد المنشأ</th><td>إندونيسيا (Eagle / Geliga)</td></tr>
  <tr><th>الشركة المصنعة</th><td>PT Eagle Indo Pharma (Geliga)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد كريم جيليجا لآلام العضلات (Geliga Relief)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم جيليجا مشكلة الشد العضلي، آلام تيبس الرقبة والظهر، وتشنجات الأنسجة بعد التمرين والمجهود.</p>

<h3>لماذا تنجح تركيبته الحرارية؟</h3>
<p>لأن ساليسيلات الميثيل والمنثول يحدثان توسعاً بالشعيرات الدموية الموضعية، مما يبث دفئاً يفك التشنج ويسكن مسارات الألم.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التدليك بعد المجهود:</strong> دلكي العضلات المجهدة بالكريم بعد التمرين أو الحمام الدافئ.<br>
2. <strong>غسل اليدين فوراً:</strong> اغسلي اليدين بالصابون جيداً بعد التطبيق لتجنب ملامسة العينين.<br>
3. <strong>تجنب الضمادات المحكمة:</strong> دع البشرة تتنفس دون ربط محكم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات تسكين العضلات تسخن وتسبب حرقاناً دائماً بالجلد."<br>
<strong>الحقيقة:</strong> كريم جيليجا يمنح دفئاً مهدئاً متوازناً يزول تدريجياً بعد تنشيط الدورة الدموية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط ساليسيلات الميثيل إنزيمات السايكلوأوكسيجينيز (COX) الموضعية، مما يقلل إفراز البروستاجلاندين المسببة لألم العضلات.</p>"""

    faqs = [
        ("ما هو كريم تخفيف الام العضلات من جيليجا 20 جم؟", "هو كريم مسكن ومسخن موضعي يحتوي على ساليسيلات الميثيل والمنثول لتسكين آلام العضلات والشد العضلي وتيبس المفاصل."),
        ("ما هي فوائد ساليسيلات الميثيل والمنثول؟", "تخفف التهابات العضلات الموضعية، تبث دفئاً مهدئاً، وتنشط الدورة الدموية."),
        ("هل يمنح راحة فورية للشد العضلي؟", "نعم، مثبت في توفير راحة مسكنة ودافئة فورية للعضلات المجهدة."),
        ("ما وزن أنبوب الكريم؟", "يأتي بحجم 20 جم مدمج."),
        ("كيف يُستخدم بالشكل الصحيح؟", "دلكي كمية مناسبة على منطقة الألم (الظهر، الرقبة، الساقين) 2 إلى 3 مرات يومياً."),
        ("هل يترك ملمساً لزجاً؟", "يمتص بالتصفيف والتدليك ليريح العضلات دون لزوجة شديدة."),
        ("ما هو بلد صنع كريم جيليجا؟", "صُنع بفخر في إندونيسيا بواسطة PT Eagle Indo Pharma."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات جيليجا لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يناسب الرياضيين بعد التمارين؟", "ممتاز جداً للرياضيين لتسكين إجهاد وتشنج العضلات بعد التمارين الشاقة."),
        ("ما هي رائحة كريم جيليجا؟", "يتميز برائحة المنثول والنعناع الطبية المنعشة والدافئة."),
        ("هل يوضع على الجروح أو الجلد التالف؟", "يمنع وضعه على الجروح المفتوحة أو الجلد المصاب بحساسية."),
        ("هل يناسب كبار السن لآلام المفاصل؟", "نعم، مسكن ممتاز لآلام المفاصل والظهر لدى كبار السن."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعبوتها المغلقة محكماً."),
        ("هل أنبوب 20 جم مناسب لحقيبة الجيم والسفر؟", "نعم، حجم أنبوب أنيق ومدمج مثالي لحقيبة الرياضة والسفر."),
        ("هل يجب غسل اليدين بعد التطبيق؟", "نعم، يُوصى بغسل اليدين بالماء والصابون فوراً لتجنب ملامسة العينين."),
        ("هل العبوة محكمة الغلق؟", "تأتي في أنبوب محكم يمنع تسرب الكريم."),
        ("هل يناسب آلام الرقبة وتيبس الكتف؟", "نعم، ممتاز جداً لتسكين آلام الرقبة والكتف المجهدة بالعمل."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستخدم 2 إلى 3 مرات يومياً عند الحاجة."),
        ("هل يحتاج إلى وصفة طبية؟", "مستحضر مسكن آمن متاح بدون وصفة طبية."),
        ("هل يناسب الأطفال؟", "مناسب للمراهقين والبالغين من سن 12 سنة فما فوق."),
        ("هل يسبب حساسية؟", "تركيبة مجربة ومناسبة للجلد الخارجي."),
        ("هل يساعد في تسريع التعافي العضلي؟", "نعم، تنشيط الدورة الدموية يسرع استرخاء العضلات."),
        ("هل هو الكريم المسكن المشهور بجيليجا؟", "نعم، بلسم وكريم جيليجا الأكثر شهرة لآلام العضلات بالشرق الأوسط."),
        ("هل يمكن استخدامه قبل النوم؟", "نعم، تدليكه قبل النوم يوفر دفئاً ونوماً مريحاً."),
        ("هل يتوفر بقيمة ممتازة لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Geliga Muscle Pain Relief Cream, 20g</strong> is the fast-acting topical analgesic cream engineered to relieve muscular aches, stiffness, strain, and joint soreness caused by sports, fitness workouts, or physical exertion. Formulated by Geliga (PT Eagle Indo Pharma), it combines active warming ingredients: Methyl Salicylate, Natural Menthol, and Camphor Oil.</p>
<p>Geliga Muscle Cream provides deep penetrating warming relief that stimulates blood micro-circulation, eases muscle spasms, and delivers long-lasting pain relief after every massage.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Fast-Acting Muscle Pain Relief:</strong> Soothes muscle strains, neck stiffness, and backaches effectively.</li>
  <li><strong>Methyl Salicylate & Menthol Dual Formula:</strong> Delivers penetrating warming relief deep into muscle tissues.</li>
  <li><strong>Stimulates Blood Micro-Circulation:</strong> Accelerates recovery from sports fatigue and muscle cramps.</li>
  <li><strong>Easy-Absorbing Topical Massage:</strong> Massages smoothly into skin providing rapid thermal pain relief.</li>
  <li><strong>Ideal for Athletes & Seniors:</strong> Relieves joint and muscular pain after workouts or daily exertion.</li>
  <li><strong>Compact 20g Tube:</strong> High-value compact size perfect for gym bags, first aid kits, and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Clean affected skin area with warm water and pat dry.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a suitable amount of Geliga Cream onto the painful muscle or joint area (back, neck, legs, shoulders).</li>
  <li><strong>Step 3 (Massage):</strong> Massage in gentle circular motions 2 to 3 times daily until fully absorbed.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Methyl Salicylate:</strong> Topical anti-inflammatory analgesic that eases muscular and joint pain.</li>
  <li><strong>Menthol & Camphor Oil:</strong> Provide warm soothing sensations and block pain signals.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical muscle application only; do not apply to open wounds, damaged skin, or near eyes.</li>
  <li>Do not wrap tightly with tight thermal bandages after application.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Athletes, seniors, and anyone suffering from muscle aches, stiffness, or strains seeking fast warming topical relief.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Geliga</td></tr>
  <tr><th>Category</th><td>Medicine & Healthcare / Topical Muscle Pain Relief Creams</td></tr>
  <tr><th>Product Type</th><td>Fast Warming Muscle & Joint Pain Relief Cream (20g)</td></tr>
  <tr><th>Volume/Weight</th><td>20 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Topical Muscle & Joint Application)</td></tr>
  <tr><th>Finish</th><td>Relieved muscle pain, relaxed soreness & warm comfort</td></tr>
  <tr><th>Texture</th><td>Warming topical massage cream</td></tr>
  <tr><th>Fragrance</th><td>Medicated Menthol & Methyl Salicylate scent</td></tr>
  <tr><th>Active Ingredients</th><td>Methyl Salicylate, Menthol, Camphor Oil, Peppermint Oil</td></tr>
  <tr><th>Country of Origin</th><td>Indonesia (Eagle / Geliga)</td></tr>
  <tr><th>Manufacturer</th><td>PT Eagle Indo Pharma (Geliga)</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Methyl Salicylate & Thermal Muscle Relaxation</h2>

<h3>What problem does this solve?</h3>
<p>Geliga Muscle Pain Relief Cream resolves muscle strains, neck stiffness, backaches, and post-workout soreness.</p>

<h3>Why choose Geliga?</h3>
<p>Methyl Salicylate inhibits local COX enzymes while Menthol vasodilates capillaries, broadcasting warming relief that calms pain signals.</p>"""

    en_faqs = [
        ("What is Geliga Muscle Pain Relief Cream 20g?", "It is a fast-acting topical warming analgesic cream enriched with Methyl Salicylate and Menthol to relieve muscle pain and stiffness."),
        ("What are the benefits of Methyl Salicylate and Menthol?", "They ease local muscle inflammation, deliver deep warming relief, and boost blood circulation."),
        ("Does it provide fast relief for muscle strains?", "Yes, clinically effective at delivering fast warming relief for strained muscles."),
        ("What volume is contained in this tube?", "It comes in a compact 20g tube."),
        ("How do I apply it correctly?", "Massage a suitable amount onto painful muscle or joint areas 2 to 3 times daily."),
        ("Does it leave a greasy residue?", "Absorbs smoothly into skin during massage without heavy stickiness."),
        ("Where is Geliga manufactured?", "It is proudly manufactured in Indonesia by PT Eagle Indo Pharma."),
        ("How do I verify authenticity at Ekleel Abha?", "All Geliga products at Ekleel Abha are 100% original from certified distributors."),
        ("Is it great for athletes post-workout?", "Yes, highly recommended for athletes to ease muscle soreness and fatigue after exercise."),
        ("What scent does Geliga have?", "Features a fresh medicated Menthol and Peppermint warming aroma."),
        ("Can it be applied on broken skin?", "No, do not apply to open wounds, cuts, or irritated skin."),
        ("Is it suitable for seniors with joint pain?", "Yes, excellent topical relief for senior joint and back soreness."),
        ("How should I store the tube?", "Store in a cool, dry place with cap tightly closed."),
        ("Is the 20g tube gym-bag friendly?", "Yes, compact tube fits easily into gym bags and first aid travel kits."),
        ("Should I wash hands after application?", "Yes, always wash hands with soap immediately after application to prevent eye contact."),
        ("Is the tube cap leak-proof?", "Yes, comes in a sturdy squeeze tube with a secure cap."),
        ("Does it soothe neck and shoulder stiffness?", "Yes, excellent for easing stiff neck and shoulder tension from desk work."),
        ("How many times daily can it be used?", "Apply 2 to 3 times daily as needed."),
        ("Does it require a prescription?", "No, it is a safe over-the-counter topical analgesic cream."),
        ("Is it safe for teenagers?", "Suitable for adults and teens aged 12+."),
        ("Does it cause skin allergies?", "Dermatologically tested and safe for external skin application."),
        ("Does it speed up muscle recovery?", "Yes, boosting micro-circulation accelerates muscle tension recovery."),
        ("Is Geliga a famous muscle pain brand?", "Yes, Geliga is a top-selling muscle pain balm and cream across the Middle East."),
        ("Can it be applied before bedtime?", "Yes, massaging before sleep provides warm relaxation for restful sleep."),
        ("Is it available at a great value at Ekleel Abha?", "Yes, available at an exceptional price at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1813",
        "sku": "EK-1813",
        "gtin": "8993176722161",
        "category": "الأدوية والمستلزمات الطبية / مسكنات آلام العضلات والمفاصل الموضعية",
        "brand": "Geliga",
        "ar": {
            "title": "كريم تخفيف الام العضلات من جيليجا، 20 جم",
            "meta_title": "كريم جيليجا لتخفيف آلام العضلات 20جم | صيدلية إكليل أبها",
            "meta_description": "اشتري كريم تخفيف الام العضلات من جيليجا (20 جم). مسكن موضعي حراري بالمنثول وساليسيلات الميثيل للشد العضلي. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["جيليجا", "كريم_جيليجا", "تسكين_العضلات", "الشد_العضلي", "إكليل_أبها"]
        },
        "en": {
            "title": "Geliga Muscle Pain Relief Cream, 20g",
            "meta_title": "Geliga Muscle Pain Relief Cream 20g | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Geliga Muscle Pain Relief Cream (20g). Fast warming topical analgesic with Methyl Salicylate & Menthol. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["geliga", "muscle_pain_cream", "topical_analgesic", "muscle_relief", "ekleel_abha"]
        },
        "schema": {
            "brand": "Geliga",
            "category": "Medicine / Analgesic Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "geliga-muscle-pain-relief-cream-20g.webp",
            "alt": "Geliga Muscle Pain Relief Cream 20g",
            "title": "Geliga Muscle Pain Relief Cream 20g"
        }
    }

def create_product_1814():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>معجون أسنان من  ديتانسيمو، 75 مل (Ditansimo Toothpaste, 75 ml)</strong> معجون الأسنان السويسري الطبي المتقدم (Dentissimo Health Care) المصمم خصيصاً لحماية الفم، تقوية مينا الأسنان، ومنع تراكم البلاك والتسوس بفاعلية فائقة. يعتمد هذا المعجون السويسري من ديتانسيمو على فورمولا النظافة الفائقة المدعمة بـ الفلورايد الطبي، مستخلصات الأعشاب المطهرة، وزيوت النعناع السويسرية الناصعة.</p>
<p>يعمل معجون ديتانسيمو على تلميع الأسنان، تنظيف المسافات الضيقة، تهدئة اللثة المتهيجة، وتأمين حماية فموية متكاملة خالية من المواد الكيميائية القاسية، ليمنحكِ ابتسامة صحية بيضاء ونفساً منعشاً يبث الثقة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية فائقة لمينا الأسنان من التسوس:</strong> الفلورايد الطبي يقوي المينا ويحميها من النخر وحمض البكتيريا.</li>
  <li><strong>تنظيف وإزالة طبقات البلاك والجير:</strong> حبيبات السيليكا الناعمة تنظف أسطح الأسنان وتمنع التكلسات.</li>
  <li><strong>تهدئة وحماية اللثة الحساسة:</strong> الخلاصات العشبية المطهرة تمنع نزيف اللثة والتهاب الأنسجة.</li>
  <li><strong>نفساً منعشاً طوال اليوم:</strong> زيوت النعناع السويسرية تقضي على البكتيريا المسببة للرائحة الكريهة.</li>
  <li><strong>تركيبة سويسرية طبية نقية:</strong> خالية من المواد الضارة ومناسبة للاستخدام الفمي اليومي.</li>
  <li><strong>أنبوب سعة 75 مل:</strong> حجم طبي مدمج ومثالي للاستخدام الفردي وللسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق):</strong> وضعي كمية بحجم حبة البازلاء من معجون ديتانسيمو على شعيرات فرشاة الأسنان.</li>
  <li><strong>الخطوة الثانية (التفريش):</strong> فرشي أسنانكِ واللسان بحركات دائرية خفيفة لمدة 2 دقيقة على الأقل.</li>
  <li><strong>الخطوة الثالثة (الشطف):</strong> ابصقي المعجون واشطفي الفم بالماء الفاتر جيداً (يُستعمل 2 إلى 3 مرات يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>فلورايد الصوديوم (Sodium Fluoride):</strong> يقوي مينا الأسنان ويحمي من التسوس.</li>
  <li><strong>خلاصات أعشاب سويسرية وزيوت نعناع:</strong> تطهر الفم وتهدئ اللثة وتنعش النفس.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الفموي لتفريش الأسنان فقط؛ لا يبتلع المعجون.</li>
  <li>للأطفال دون 6 سنوات يُفضل استخدام كمية بحجم حبة البازلاء تحت إشراف الوالدين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن معجون أسنان سويسري طبي لحماية المينا، تهدئة اللثة، وانتعاش النفس.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ديتانسيمو (Dentissimo)</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم / معاجين الأسنان الطبية السويسرية</td></tr>
  <tr><th>نوع المنتج</th><td>معجون أسنان طبي لحماية المينا واللثة (75ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>75 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بالفم والأسنان)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان نظيفة بيضاء، لثة صحية ونفس منعش طوال اليوم</td></tr>
  <tr><th>الملمس</th><td>معجون ناعم يرغي بكثافة ينظف بفاعلية</td></tr>
  <tr><th>العطر</th><td>عطر النعناع والأعشاب السويسرية المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>فلورايد الصوديوم، خلاصات أعشاب سويسرية، نعناع مطهر</td></tr>
  <tr><th>بلد المنشأ</th><td>سويسرا (Switzerland)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Medpack Swiss Group / Dentissimo</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والأطفال (من 6 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد معجون ديتانسيمو السويسري (Dentissimo Care)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج معجون ديتانسيمو مشكلة تسوس الأسنان، تراكم البلاك والبكتيريا، رائحة الفم الكريهة، وتهيج أنسجة اللثة.</p>

<h3>لماذا تنجح التركيبة السويسرية؟</h3>
<p>لأن الفلورايد الطبي والخلاصات العشبية السويسرية يقويان المينا ويطهران المسافات الضيقة دون جرح اللثة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التفريش دقيقتين كاملتين:</strong> فرشي الأسنان مرتين يومياً صباحاً ومساءً.<br>
2. <strong>تنظيف اللسان:</strong> مرري الفرشاة بلطف على اللسان لإزالة البكتيريا.<br>
3. <strong>الاستخدام مع الغسول:</strong> استعملي معجون ديتانسيمو مع غسول الفم المماثل لنتائج مضاعفة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "معاجين الأسنان العادية تغني عن المعاجين السويسرية الطبية."<br>
<strong>الحقيقة:</strong> معجون ديتانسيمو السويسري يوفر حماية المينا وتطهير اللثة بمعايير جودة سويسرية متقدمة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تندمج أيونات الفلورايد مع بلورات الهيدروكسي أباتيت بمينا الأسنان، مما يجعلها أكثر مقاومة للأحماض البكتيرية.</p>"""

    faqs = [
        ("ما هو معجون أسنان من ديتانسيمو 75 مل؟", "هو معجون أسنان سويسري طبي من ديتانسيمو بالفلورايد والأعشاب السويسرية لحماية مينا الأسنان وتقوية اللثة ونظافة الفم."),
        ("ما هي فوائد الفلورايد الطبي والأعشاب السويسرية؟", "يقوي الفلورايد مينا الأسنان ضد التسوس، بينما تطهر الأعشاب السويسرية اللثة وتنعش النفس."),
        ("هل يقي من تسوس الأسنان والتكلسات الجيرية؟", "نعم، مثبت في حماية المينا ومنع تراكم طبقات البلاك والتكلس الجيري."),
        ("ما حجم أنبوب المعجون؟", "يأتي بحجم 75 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي كمية بحجم حبة البازلاء، فرشي الأسنان واللسان دقيقتين ثم اشطفي بالماء الفاتر مرتين يومياً."),
        ("ما هو بلد صنع معجون ديتانسيمو؟", "صُنع بفخر في سويسرا بواسطة Medpack Swiss Group."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات ديتانسيمو لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يساعد في تهدئة اللثة المتهيجة؟", "نعم، الخلاصات العشبية المطهرة تمنع التهاب ونزيف اللثة."),
        ("ما هي رائحة معجون ديتانسيمو؟", "يتميز برائحة النعناع والأعشاب السويسرية المنعشة."),
        ("هل يزيل رائحة الفم الكريهة؟", "نعم، يقضي على البكتيريا المسببة للرائحة ويضمن نفساً منعشاً."),
        ("هل المعجون آمن للأطفال؟", "آمن للأطفال من سن 6 سنوات فما فوق مع استخدام كمية بحجم حبة البازلاء تحت الإشراف."),
        ("كيف أحتفظ بأنبوب المعجون؟", "يُحفظ في مكان بارد وجاف."),
        ("هل حجم 75 مل مناسب للسفر والحقيبة؟", "نعم، أنبوب مدمج وأنيق مثالي لحمل الحقيبة والسفر."),
        ("هل يرغي بشكل ممتاز؟", "نعم، يولد رغوة ناعمة تنظف كامل أنحاء الفم."),
        ("هل يساعد في تلميع الأسنان؟", "نعم، حبيبات التلميع الناعمة تزيل التصبغات السطحية وتلمع الأسنان."),
        ("هل العبوة محكمة الغلق؟", "تأتي في أنبوب محكم بغطاء لولبي يمنع التسرب."),
        ("هل ينصح به أطباء الأسنان بسويسرا؟", "نعم، العلامة السويسرية الطبية الأولى المعتمدة للعناية اليومية بالفم."),
        ("كم مرة يُفضل تفريش الأسنان يومياً؟", "يُوصى بالتفريش مرتين إلى 3 مرات يومياً بعد الوجبات."),
        ("هل يمنع تكلس البلاك؟", "نعم، يقلل تراكم البلاك والبكتيريا على الأسنان."),
        ("هل يناسب الأسنان الحساسة؟", "تركيبة طبية لطيفة آمنة ومناسبة للأسنان واللثة الحساسة."),
        ("هل يترك طعماً لذيذاً بالفم؟", "نعم، طعم النعناع السويسري يترك نفساً منعشاً وطيباً."),
        ("هل يناسب الاستخدام قبل النوم؟", "نعم، ممتاز لتنظيف الفم وتأمين حماية طوال الليل."),
        ("هل يحتوي على مواد قاسية؟", "خالي من المواد الكيميائية الضارة ومصرح به صحياً."),
        ("هل يتوفر بنوعيات أخرى لدى إكليل أبها؟", "نعم، تتوفر معاجين وغسولات ديتانسيمو السويسرية المتعددة."),
        ("هل هو خيار معجون الأسنان الطبي الممتاز؟", "نعم، المعجون السويسري الطبي المفضل للعائلة.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Ditansimo Toothpaste, 75 ml</strong> (Dentissimo Health Care) is the advanced Swiss clinical toothpaste formulated to deliver complete cavity protection, enamel strengthening, and gum care. Engineered in Switzerland, it combines medical Sodium Fluoride with soothing Swiss botanical extracts and refreshing mint oils.</p>
<p>Dentissimo Toothpaste gently polishes teeth surfaces, dislodges food particles from tight interdental spaces, soothes sensitive gums, and neutralizes bad breath bacteria to leave you with a healthy white smile and fresh breath confidence.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Advanced Cavity & Enamel Protection:</strong> Medical Sodium Fluoride reinforces enamel against bacterial acid decay.</li>
  <li><strong>Plaque Removal & Teeth Polishing:</strong> Silica micro-particles clean tooth surfaces and prevent tartar formation.</li>
  <li><strong>Soothes & Protects Sensitive Gums:</strong> Antiseptic Swiss botanical extracts prevent gum inflammation and bleeding.</li>
  <li><strong>Long-Lasting Fresh Breath:</strong> Swiss mint oils eliminate bad breath bacteria for hours.</li>
  <li><strong>Pure Swiss Medical Formula:</strong> Free from harsh chemicals, ideal for daily family oral care.</li>
  <li><strong>Compact 75ml Tube:</strong> Clinical tube size perfect for individual daily use and travel kits.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply):</strong> Apply a pea-sized amount of Ditansimo toothpaste onto toothbrush bristles.</li>
  <li><strong>Step 2 (Brush):</strong> Brush teeth and tongue surface gently in circular motions for at least 2 minutes.</li>
  <li><strong>Step 3 (Rinse):</strong> Spit out toothpaste and rinse mouth thoroughly with warm water (use 2 to 3 times daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Sodium Fluoride:</strong> Strengthens tooth enamel and defends against cavities.</li>
  <li><strong>Swiss Botanical Extracts & Mint Oils:</strong> Sanitize oral cavity, soothe gums, and freshen breath.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For oral brushing application only; do not swallow.</li>
  <li>For children under 6 years, use a pea-sized amount under adult supervision.</li>
  <li>Keep out of reach of young children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a Swiss clinical fluoride toothpaste for complete enamel protection, gum soothing, and fresh breath.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Dentissimo / Ditansimo</td></tr>
  <tr><th>Category</th><td>Oral Care / Swiss Clinical Toothpastes</td></tr>
  <tr><th>Product Type</th><td>Swiss Fluoride Enamel Protection & Gum Care Toothpaste (75ml)</td></tr>
  <tr><th>Volume/Weight</th><td>75 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Oral & Dental Care)</td></tr>
  <tr><th>Finish</th><td>Clean white teeth, healthy gums & fresh minty breath</td></tr>
  <tr><th>Texture</th><td>Creamy foaming toothpaste</td></tr>
  <tr><th>Fragrance</th><td>Fresh Swiss mint & botanical herbal aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Sodium Fluoride, Swiss Botanical Extracts, Mint Oils</td></tr>
  <tr><th>Country of Origin</th><td>Switzerland</td></tr>
  <tr><th>Manufacturer</th><td>Medpack Swiss Group / Dentissimo</td></tr>
  <tr><th>Age Group</th><td>Adults & Kids (6+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Swiss Fluoride & Botanical Oral Protection</h2>

<h3>What problem does this solve?</h3>
<p>Ditansimo Toothpaste resolves tooth cavity decay, plaque buildup, bad breath, and sensitive gum bleeding.</p>

<h3>Why choose Dentissimo?</h3>
<p>Medical Sodium Fluoride ions remineralize tooth enamel while Swiss herbal extracts soothe gingival tissues to stop bleeding.</p>"""

    en_faqs = [
        ("What is Ditansimo Toothpaste 75 ml?", "It is a Swiss clinical toothpaste formulated with Fluoride and Swiss herbal extracts to protect enamel, soothe gums, and freshen breath."),
        ("What are the benefits of Sodium Fluoride and Swiss botanicals?", "Fluoride fortifies enamel against cavities, while botanicals soothe gums and eliminate oral bacteria."),
        ("Does it prevent cavities and tartar?", "Yes, clinically proven to strengthen enamel and prevent plaque calcification into tartar."),
        ("What volume is contained in this tube?", "It comes in a compact 75ml tube."),
        ("How do I apply it correctly?", "Brush teeth and tongue for 2 minutes with a pea-sized amount, then rinse with water twice daily."),
        ("Where is Ditansimo manufactured?", "It is proudly manufactured in Switzerland by Medpack Swiss Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All Dentissimo products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it soothe sensitive gums?", "Yes, antiseptic herbal extracts prevent gum inflammation and bleeding."),
        ("What scent does it have?", "Features a fresh, clean Swiss mint and herbal aroma."),
        ("Does it eliminate bad breath?", "Yes, destroys odor-causing bacteria for long-lasting fresh breath."),
        ("Is it safe for children?", "Safe for children aged 6+ using a pea-sized amount under supervision."),
        ("How should I store the tube?", "Store in a cool, dry place away from direct heat."),
        ("Is the 75ml tube handbag-friendly?", "Yes, compact tube fits easily into handbags and travel kits."),
        ("Does it foam well?", "Yes, produces a smooth cleansing foam that reaches tight interdental spaces."),
        ("Does it polish teeth stains?", "Yes, gentle silica polishers clean surface discoloration and polish teeth."),
        ("Is the tube cap leak-proof?", "Yes, comes in a sturdy squeeze tube with a screw cap."),
        ("Is it Swiss dentist recommended?", "Yes, top recommended Swiss clinical toothpaste for daily family care."),
        ("How many times daily should I brush?", "Brush 2 to 3 times daily after meals."),
        ("Does it prevent plaque buildup?", "Yes, reduces plaque formation on tooth enamel."),
        ("Is it safe for sensitive teeth?", "Yes, gentle clinical formulation safe for sensitive teeth and gums."),
        ("Does it leave a pleasant taste?", "Yes, leaves a clean Swiss mint aftertaste."),
        ("Is it great for nighttime brushing?", "Yes, cleanses oral cavity for overnight cavity protection."),
        ("Does it contain harsh additives?", "Free from harmful banned chemicals and health certified."),
        ("Are other Dentissimo products available at Ekleel Abha?", "Yes, Ekleel Abha offers various Swiss Dentissimo toothpastes and mouthwashes."),
        ("Is it a top clinical toothpaste choice?", "Yes, the #1 Swiss clinical family toothpaste choice.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1814",
        "sku": "EK-1814",
        "gtin": "7640162322355",
        "category": "العناية بالفم / معاجين الأسنان الطبية السويسرية",
        "brand": "Dentissimo",
        "ar": {
            "title": "معجون أسنان من  ديتانسيمو، 75 مل",
            "meta_title": "معجون اسنان ديتانسيمو 75مل | صيدلية إكليل أبها",
            "meta_description": "اشتري معجون أسنان من ديتانسيمو (75 مل). حماية المينا واللثة بالفلورايد والأعشاب السويسرية. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["ديتانسيمو", "معجون_ديتانسيمو", "حماية_المينا", "معجون_سويسري", "إكليل_أبها"]
        },
        "en": {
            "title": "Ditansimo Toothpaste, 75 ml",
            "meta_title": "Ditansimo Toothpaste 75ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Ditansimo Toothpaste (75 ml). Swiss clinical enamel protection & gum care with Fluoride. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["dentissimo", "ditansimo_toothpaste", "enamel_protection", "swiss_toothpaste", "ekleel_abha"]
        },
        "schema": {
            "brand": "Dentissimo",
            "category": "Oral Care / Toothpaste",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "ditansimo-toothpaste-75ml.webp",
            "alt": "Ditansimo Toothpaste 75 ml",
            "title": "Ditansimo Toothpaste 75 ml"
        }
    }

print("Loaded Batch 21 builders")
