import json, os

def create_product_1755():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم راديان للتدليك وتخفيف آلام العضلات والمفاصل 100 جم (Radian Massage Cream 100g)</strong> المسكن الموضعي الأكثر اعتماداً وفاعلية لتخفيف الآلام العضلية والمفصلية وإراحة الجسم المجهد. يجمع هذا الكريم البريطاني الشهير بين أربعة مكونات فعالة تعمل بتناغم مذهل: المنتول (Menthol) للتبريد والتسكين، الكافور (Camphor) لتنشيط الدورة الدموية، ميثيل ساليسيلات (Methyl Salicylate) لتخفيف الالتهاب، ومستخلص الفلفل (Capsicum) لمنح الدفء المهدئ للعضلات.</p>
<p>يمتاز كريم راديان بقدرته الفريدة على اختراق الأنسجة العضلية فور دلكه، حيث يخفف من التصلب العضلي، التشنجات، آلام الظهر والرقبة، وآلام الروماتيزم والمفاصل، ليعيد إليكِ حرية الحركة والانتعاش بعد التمارين أو المجهود البدني الشاق.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تسكين سريع ومزدوج (تبريد وتدفئة):</strong> يمنح شعوراً بالبرودة الفورية يليه دفء مهدئ للعضلات.</li>
  <li><strong>تخفيف آلام المفاصل والروماتيزم:</strong> يقلل التصلب والتهابات المفاصل وآلام الفقرات والظهر.</li>
  <li><strong>فك تشنجات وتصلب العضلات:</strong> يرخي العضلات المشدودة والمجهدة بعد التمرين أو العمل الشاق.</li>
  <li><strong>تنشيط الدورة الدموية الموضعية:</strong> يساعد الكافور ومستخلص الفلفل في تحسين تدفق الدم وتنسيق الاستشفاء.</li>
  <li><strong>سهل الامتصاص وغير دهني:</strong> يدلك بسهولة ويتغلغل في الأنسجة دون ترك لزوجة قاسية.</li>
  <li><strong>عبوة اقتصادية 100 جم:</strong> حجم ممتاز ومناسب للاستخدام العائلي والرياضي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف والتحضير):</strong> وضعي الكريم على المنطقة المصابة (الظهر، الرقبة، المفاصل، أو الساقين).</li>
  <li><strong>الخطوة الثانية (التدليك):</strong> دلكي بحركات دائرية خفيفة حتى يتغلغل الكريم كاملاً في الجلد.</li>
  <li><strong>الخطوة الثالثة (التكرار):</strong> يُستخدم من 2 إلى 3 مرات يومياً حسب الحاجة، ويفضل بعد حمام دافئ.</li>
  <li><strong>الخطوة الرابعة (النظافة):</strong> اغسلي يديكِ جيداً بالماء والصابون بعد الاستخدام وتجنبي ملامسة العينين.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>المنتول (Menthol 2.54%):</strong> يبرد المنطقة المصابة ويهدئ مستقبلات الألم المباشرة.</li>
  <li><strong>الكافور (Camphor 1.43%):</strong> ينشط الدورة الدموية ويوسع الأوعية الموضعية للتسكين.</li>
  <li><strong>ميثيل ساليسيلات (Methyl Salicylate 0.42%):</strong> مسكن مسدد للالتهابات العضلية والمفصلية.</li>
  <li><strong>مستخلص الفلفل (Oleoresin Capsicum):</strong> يمنح الدفء المهدئ الذي يشتت الشعور بالألم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي فقط؛ يُمنع وضعه على الجروح المفتوحة أو البشرة المتهيجة أو الوجه.</li>
  <li>تجنبي ملامسة العينين والغشاء المخاطي.</li>
  <li>غير مناسب للأطفال دون سن 6 سنوات.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعانون من آلام العضلات، تشنجات الظهر والرقبة، تيبس المفاصل، وآلام الرياضيين.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>راديان (Radian)</td></tr>
  <tr><th>الفئة</th><td>العناية بالصحة / مسكنات وكريمات مساج العضلات</td></tr>
  <tr><th>نوع المنتج</th><td>كريم مساج وتسكين آلام العضلات والمفاصل (100g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (الرش والتدليك الموضعي)</td></tr>
  <tr><th>المظهر النهائي</th><td>عضلات مرتاحة، مفاصل مرنة، وزوال للتصلب والألم</td></tr>
  <tr><th>الملمس</th><td>كريمي دافئ وسهل الامتصاص</td></tr>
  <tr><th>العطر</th><td>عطر المنتول والكافور المنعش القوي</td></tr>
  <tr><th>المكونات النشطة</th><td>منتول، كافور، ميثيل ساليسيلات، مستخلص الكابسيكوم</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة المتحدة (UK) / إنجلترا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Radian Health UK</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والأطفال فوق 6 سنوات</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي للتسكين الحراري والتدليك العضلي (Radian)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم راديان مشكلة تشنج وتيبس العضلات، آلام الانزلاق والظهر والرقبة، وآلام التهاب المفاصل الروماتزمية.</p>

<h3>لماذا يحدث التشنج والألم؟</h3>
<p>يتسبب المجهود البدني والتمارين وتراكم حمض اللاكتيك في عضلات مشدودة ومتهيجة تفقد مرونتها وتسبب أليماً موضعيًا.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التدليك بعد الاستحمام الدافئ:</strong> يساعد الحمام الدافئ في فتح المسام وزيادة امتصاص الكريم.<br>
2. <strong>غسل اليدين فوراً:</strong> اغسلي يديكِ جيداً لتفادي ملامسة العينين الكافور والمنتول.<br>
3. <strong>التسخين قبل الرياضة:</strong> استخدمي الكريم لتسخين العضلات قبل التمارين الشاقة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريم راديان مخصص لكبار السن فقط."<br>
<strong>الحقيقة:</strong> كريم راديان ممتاز جداً للرياضيين والشباب لتخفيف إجهاد التمارين وتشنج الرقبة والظهر.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعتمد كريم راديان على تقنية التشتيت التبريدي الحراري (Counter-Irritant Mechanism). يبرد المنتول مستقبلات TRPM8 الجلدية لتخدير الألم فورياً، بينما يحفز الكافور ميثيل ساليسيلات تدفق الدم الموضعي لسرعة الاستشفاء وتشتيت الإشارة العصبية بالألم.</p>"""

    faqs = [
        ("ما هو كريم راديان للتدليك وتخفيف آلام العضلات؟", "هو مسكن موصلي بريطاني فاخر 100 جم يدمج بين المنتول والكافور وميثيل ساليسيلات لتسكين آلام العضلات والمفاصل والمظهر المجهد."),
        ("ما هي فوائد المنتول والكافور في الكريم؟", "يبرد المنتول الألم فورياً، بينما يحفز الكافور الدورة الدموية ويمنح الدفء المهدئ للعضلات."),
        ("هل يزيل آلام الظهر والرقبة وتشنج التمارين؟", "نعم، ممتاز جداً لإرخاء تشنجات الظهر، الرقبة، الساقين، وآلام الإجهاد الرياضي."),
        ("ما حجم العبوة؟", "تأتي العبوة بحجم 100 جم."),
        ("كم مرة يُنصح باستخدامه يومياً؟", "يُستخدم من 2 إلى 3 مرات يومياً بدلك خفيف على المنطقة المصابة."),
        ("هل يناسب مرضى الروماتيزم وآلام المفاصل؟", "نعم، يقلل تيبس وتصلب المفاصل ويهدئ آلام الروماتيزم."),
        ("ما هو بلد صنع كريم راديان؟", "صُنع بفخر في المملكة المتحدة (إنجلترا) وفق أعلى المعايير الطبية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع كريمات راديان لدى إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يجب غسل اليدين بعد الاستخدام؟", "نعم، ينبغي غسل اليدين بالماء والصابون لتفادي ملامسة العينين."),
        ("هل يناسب الأطفال؟", "مناسب للبالغين والأطفال فوق 6 سنوات."),
        ("هل يوضع على الجروح المفتوحة؟", "لا، يُمنع وضعه على الجروح المفتوحة أو الجلد المتهيج."),
        ("ما هي رائحة كريم راديان؟", "يتميز برائحة المنتول والكافور المنعشة والنفّاذة."),
        ("هل يفضل استخدامه بعد الاستحمام الدافئ؟", "نعم، الاستحمام الدافئ يفتح المسام ويضاعف مفعول التسكين."),
        ("هل يناسب كبار السن والرياضيين؟", "نعم، ممتاز لكلا الفئتين لتسهيل الحركة وفك التصلب."),
        ("هل يترك أثراً دهنياً لزجاً؟", "لا، يتغلغل في الأنسجة بسرعة دون أثر دهني لزج."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن حرارة الشمس."),
        ("هل يحتاج لوصفة طبية؟", "لا، مسكن موصلي آمن يباع بدون وصفة طبية."),
        ("هل يساعد في تسخين العضلات قبل الرياضة؟", "نعم، تدليكه قبل الرياضة ينشط الدورة الدموية ويقي من التشنج."),
        ("هل العبوة محكمة الغلق؟", "تأتي في أنبوب محكم يسهل الضغط والتحكم في الكمية."),
        ("هل يسبب احمراراً خفيفاً في الجلد؟", "تنشيط الدورة الدموية والدفء قد يسببان احمراراً خفيفاً مؤقتاً يزول سريعاً."),
        ("هل يناسب الحوامل؟", "يُفضل استشارة الطبيب قبل استخدام المسكنات الموضعية للحوامل."),
        ("هل يعاد إغلاق الأنبوب بإحكام؟", "نعم، بغطاء لولبي محكم يمنع جفاف الكريم."),
        ("هل يناسب تشنج الرقبة من النوم الخاطئ؟", "نعم، يفك تشنج الرقبة والكتفين بفاعلية."),
        ("هل العبوة 100 جم اقتصادية؟", "نعم، تكفي لأسابيع من الاستخدام المتكرر."),
        ("هل يمنح شعوراً فورياً بالراحة؟", "نعم، يبدأ التسكين والراحة الفورية في ثوانٍ بعد الدلك.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Radian Massage Cream 100g</strong> is Britain's most trusted topical pain relief treatment engineered to soothe muscle soreness, joint stiffness, and physical fatigue. Combining four powerful active ingredients—cooling Menthol, circulation-boosting Camphor, anti-inflammatory Methyl Salicylate, and warming Oleoresin Capsicum—it penetrates targeted tissues to deliver rapid warming and cooling relief.</p>
<p>Radian Massage Cream effectively relieves muscle spasms, backache, neck tension, rheumatic aches, and joint discomfort, restoring physical mobility and body relaxation post-workout or after strenuous labor.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Rapid Dual Action (Cooling & Warming):</strong> Instant cooling relief followed by deep muscle warming.</li>
  <li><strong>Relieves Joint & Rheumatic Pain:</strong> Reduces stiffness, joint inflammation, and lower back soreness.</li>
  <li><strong>Unlocks Muscle Spasms:</strong> Relaxes tight, overworked muscle fibers post-exercise.</li>
  <li><strong>Boosts Local Circulation:</strong> Camphor and Capsicum stimulate blood flow to speed tissue recovery.</li>
  <li><strong>Fast-Absorbing & Non-Greasy:</strong> Massages smoothly into skin without heavy sticky residue.</li>
  <li><strong>Generous 100g Family Tube:</strong> Ideal value size for athletes and family home care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply):</strong> Apply a small amount to the affected area (back, neck, joints, or legs).</li>
  <li><strong>Step 2 (Massage):</strong> Massage gently in circular motions until fully absorbed.</li>
  <li><strong>Step 3 (Repeat):</strong> Use 2 to 3 times daily as needed, ideally after a warm shower.</li>
  <li><strong>Step 4 (Cleanse Hands):</strong> Wash hands thoroughly with soap and water after application.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Menthol (2.54%):</strong> Cools targeted tissue and numbs pain receptors instantly.</li>
  <li><strong>Camphor (1.43%):</strong> Dilates blood vessels and stimulates circulation.</li>
  <li><strong>Methyl Salicylate (0.42%):</strong> Topical analgesic addressing muscle and joint inflammation.</li>
  <li><strong>Oleoresin Capsicum:</strong> Delivers comforting warmth that distracts from deep pain.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical application only; do not apply to broken skin, face, or eyes.</li>
  <li>Avoid contact with eyes and mucous membranes.</li>
  <li>Not recommended for children under 6 years old.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from muscle soreness, back/neck spasms, joint stiffness, or athletic fatigue.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Radian</td></tr>
  <tr><th>Category</th><td>Healthcare / Muscle & Joint Pain Analgesic Creams</td></tr>
  <tr><th>Product Type</th><td>Dual Action Muscle & Joint Massage Cream</td></tr>
  <tr><th>Volume/Weight</th><td>100 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Topical Massage Application)</td></tr>
  <tr><th>Finish</th><td>Relieved muscles, flexible joints & relaxed body</td></tr>
  <tr><th>Texture</th><td>Smooth warming cream absorbing rapidly</td></tr>
  <tr><th>Fragrance</th><td>Fresh invigorating Menthol & Camphor aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Menthol 2.54%, Camphor 1.43%, Methyl Salicylate 0.42%, Capsicum</td></tr>
  <tr><th>Country of Origin</th><td>United Kingdom (UK)</td></tr>
  <tr><th>Manufacturer</th><td>Radian Health UK</td></tr>
  <tr><th>Age Group</th><td>Adults & Children 6+</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Thermal Analgesia & Counter-Irritant Muscle Relief</h2>

<h3>What problem does this solve?</h3>
<p>Radian Massage Cream resolves muscle spasms, lower back tightness, neck stiffening, and rheumatic joint pain.</p>

<h3>Why choose Radian?</h3>
<p>Its dual thermal mechanism cools dermal pain signals before delivering deep blood-flow warmth to flush out lactic acid.</p>"""

    en_faqs = [
        ("What is Radian Massage Cream 100g?", "It is a British topical pain relief cream combining Menthol, Camphor, and Methyl Salicylate for muscle and joint pain."),
        ("How do Menthol and Camphor work?", "Menthol numbs pain immediately with cooling relief, while Camphor warms tissues and boosts blood circulation."),
        ("Does it relieve backache and neck stiffness?", "Yes, it excels at relaxing tight back, neck, leg muscles, and post-workout fatigue."),
        ("What volume is contained in this tube?", "It comes in a generous 100g tube."),
        ("How many times daily should I apply it?", "Apply 2 to 3 times daily, massaging gently into affected areas."),
        ("Is it suitable for rheumatic joint pain?", "Yes, it eases joint stiffness and relieves rheumatic aches."),
        ("Where is Radian manufactured?", "It is proudly manufactured in the United Kingdom under strict medical standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Radian creams at Ekleel Abha are 100% original from certified distributors."),
        ("Should I wash my hands after applying?", "Yes, always wash hands with soap to prevent accidental eye contact."),
        ("Is it safe for children?", "Suitable for adults and children aged 6+."),
        ("Can it be applied to open wounds?", "No, do not apply to broken skin, face, or open wounds."),
        ("What scent does it have?", "It features an invigorating fresh Menthol and Camphor fragrance."),
        ("Is applying after a warm shower recommended?", "Yes, warm showers open pores and enhance pain-relieving absorption."),
        ("Is it suitable for athletes and seniors?", "Yes, ideal for athletes easing muscle strain and seniors managing joint stiffness."),
        ("Does it leave a greasy film?", "No, it absorbs into skin tissues quickly without heavy grease."),
        ("How should I store the tube?", "Store in a cool, dry place away from direct sunlight."),
        ("Does it require a prescription?", "No, it is an over-the-counter topical analgesic."),
        ("Can it be used to warm muscles before sports?", "Yes, massaging prior to sports stimulates blood flow and guards against cramps."),
        ("Is the tube easy to squeeze?", "Yes, it comes in an easy-squeeze hygienic tube."),
        ("Does it cause skin redness?", "Increased circulation and warmth may cause mild temporary redness."),
        ("Is it safe during pregnancy?", "Consult a physician before using topical analgesics during pregnancy."),
        ("Does the cap seal tightly?", "Yes, it features a tight screw cap preventing drying."),
        ("Does it help stiff neck from sleeping wrong?", "Yes, it effectively unlocks stiff neck and shoulder muscles."),
        ("Is the 100g tube economical?", "Yes, provides weeks of frequent family usage."),
        ("Does it deliver immediate relief?", "Yes, cooling relief begins within seconds of massage.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1755",
        "sku": "EK-1755",
        "gtin": "5011309146912",
        "category": "العناية بالصحة / مسكنات وكريمات مساج العضلات",
        "brand": "Radian",
        "ar": {
            "title": "كريم راديان للتدليك وتخفيف آلام العضلات والمفاصل 100 جم",
            "meta_title": "كريم راديان للتدليك 100جم | صيدلية إكليل أبها",
            "meta_description": "اشتري كريم راديان للتدليك وتخفيف آلام العضلات والمفاصل البريطاني (100جم). تبريد وتدفئة سريعة للتصلب والآلام. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["راديان", "كريم_راديان", "تسكين_العضلات", "آلام_المفاصل", "إكليل_أبها"]
        },
        "en": {
            "title": "Radian Massage Cream 100g",
            "meta_title": "Radian Massage Cream 100g | Ekleel Abha Pharmacy",
            "meta_description": "Buy original British Radian Massage Cream (100g) for muscle & joint pain relief. Dual cooling & warming action. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["radian", "massage_cream", "pain_relief", "muscle_relief", "ekleel_abha"]
        },
        "schema": {
            "brand": "Radian",
            "category": "Healthcare / Analgesic Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "radian-massage-cream-100g.webp",
            "alt": "Radian Massage Cream 100g",
            "title": "Radian Massage Cream 100g"
        }
    }

def create_product_1757():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>صبغة شعر بيجين البودرة باللون الأسود 6 جم (Bigen Powder Hair Color Black - 6g)</strong> الصبغة اليابانية الدائمة الأكثر اعتماداً وشهرة عالمياً لتغطية الشيب الكاملة والسهلة دون استخدام الأمونيا. تمتاز هذه الصبغة البودرة بكونها تُفعل بالماء العادي فقط دون الحاجة لإضافة أكسجين أو بيروكسيد، مما يوفر صبغاً آمناً ولطيفاً يغطي الشعر الأبيض بنسبة 100% بلون أسود شرقي غني ولامع.</p>
<p>تحتوي صبغة بيجين على مرطبات ومكونات لطيفة تحافظ على سلامة نسيج الشعر وتمنع جفافه أو تكسره، وتأتي بحجم 6 جم مدمج واقتصادي يسهل تحضيره وتطبيقه على الشعر أو اللحية للرجال والنساء في المنزل.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تغطية كاملة 100% للشيب والشعر الأبيض:</strong> يمنح لوناً أسود شرقياً غنياً وثابتاً.</li>
  <li><strong>تُفعل بالماء فقط (Water-Activated):</strong> لا تحتاج إلى إضافة أكسجين أو هيدروجين بيروكسيد.</li>
  <li><strong>خالية تماماً من الأمونيا:</strong> تركيبة لطيفة خالية من الأمونيا تمنع تهيج الفروة ورائحة الكيماويات.</li>
  <li><strong>ثبات ممتاز ويدوم طويلاً:</strong> يدوم اللون الأسود لعدة أسابيع دون أن يبهت أو يتغير.</li>
  <li><strong>مناسبة لشعر الرأس واللحية:</strong> خيار ممتاز ومجرب للرجال والنساء لتغطية الشيب.</li>
  <li><strong>عبوة مدمجة 6 جم اقتصادية:</strong> توفر كمية مناسبة لصبغ الشيب بدقة وسهولة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الخلط):</strong> اسكبي بودرة بيجين في وعاء غير معدني وأضيفي الماء العادي بالتدريج واخلطي حتى يتكون معجون ناعم.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ارتدي القفازات وزعي معجون الصبغة بالتساوي على الشعر الجاف والنظيف بفرشاة الصبغة.</li>
  <li><strong>الخطوة الثالثة (الانتظار):</strong> اتركي الصبغة على الشعر لمدة 20 إلى 30 دقيقة.</li>
  <li><strong>الخطوة الرابعة (الشطف):</strong> اشطفي الشعر جيداً بالماء الفاتر حتى يزول أثر الصبغة تماماً واغسليه بشامبو خفيف.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركبات الصباغة الدقيقة (P-Phenylenediamine Sulfate):</strong> تمنح اللون الأسود الغني والثابت.</li>
  <li><strong>صمغ الخشب والنشا (Cellulose Gum & Potato Starch):</strong> يمنحان المعجون قواماً كريمياً يسهل تطبيقه.</li>
  <li><strong>تركيبة خالية من الأمونيا:</strong> تحمي الشعر من الجفاف والتكسر.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على شعر الرأس واللحية فقط؛ يُمنع صبغ الحواجب والرموش.</li>
  <li>يجب إجراء اختبار تحسس جلدي قبل 48 ساعة من التطبيق.</li>
  <li>تجنبي ملامسة المنتج للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحثون عن صبغة يابانية بودرة بدون أمونيا لتغطية الشيب بالماء فقط بلون أسود غني.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيجين (Bigen)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / صبغات الشعر البودرة</td></tr>
  <tr><th>نوع المنتج</th><td>صبغة شعر بودرة دائمة بالماء باللون الأسود (6g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>6 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (الشعر الشائب والأبيض)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر أسود غني، لامع، وخالٍ من الشيب 100%</td></tr>
  <tr><th>الملمس</th><td>بودرة تخلط بالماء إلى معجون كريمي</td></tr>
  <tr><th>العطر</th><td>عديم رائحة الأمونيا القاسية</td></tr>
  <tr><th>المكونات النشطة</th><td>مركبات الصباغة السوداء، صمغ السليلوز، نشا البطاطس</td></tr>
  <tr><th>بلد المنشأ</th><td>اليابان (Hoyu Co.)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Hoyu Co., Ltd. Japan</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين (الرجال والنساء)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لصبغة بيجين البودرة بالماء (Bigen Japan)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تحل صبغة بيجين البودرة مشكلة ظهور الشيب وتلف الشعر الناجم عن استخدام الأكسجين والأمونيا القاسية.</p>

<h3>لماذا تنجح الصبغة البودرة؟</h3>
<p>لأنها تُفعل بالماء العادي فقط، وتغلف ألياف الشعر بلون أسود غني وثابت دون فتح الحراشف بالأكسجين.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>اختبار التحسس:</strong> أوجدي اختبار تحسس بسيط قبل 48 ساعة من التطبيق.<br>
2. <strong>ارتداء القفازات:</strong> ارتدي القفازات لحماية الأيدي من التصبغ.<br>
3. <strong>الخلط بالماء فقط:</strong> اخلطي بالماء العادي فقط وتجنبي إضافة المظهر أو الأكسجين.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الصبغة البودرة تزول بالماء بسرعة."<br>
<strong>الحقيقة:</strong> صبغة بيجين البودرة اليابانية صبغة دائمة تثبت لأسابيع وتغطي الشيب 100%.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتحد جزيئات الصباغة السوداء في بيجين مع بروتينات الشعر عند مزجها بالماء، حيث تترسب الرقائق الملونة داخل غلاف الشعرة دون حاجة لأمونيا تخترق الأنسجة.</p>"""

    faqs = [
        ("ما هي صبغة شعر بيجين البودرة باللون الأسود 6 جم؟", "هي صبغة شعر يابانية بودرة تُفعل بالماء فقط دون أمونيا لتغطية الشيب 100% بلون أسود شرقي غني."),
        ("هل تحتاج صبغة بيجين لإضافة أكسجين؟", "لا، تُفعل بالماء العادي فقط دون الحاجة لأي هيدروجين بيروكسيد أو أكسجين."),
        ("هل تحتوي على أمونيا؟", "لا، هي خالية تماماً من الأمونيا وتتميز بعدم وجود رائحة كيميائية قاسية."),
        ("هل تغطي الشيب بالكامل؟", "نعم، تضمن تغطية متكاملة 100% للشعر الأبيض والشيب."),
        ("كيف يتم تحضير وتطبيق الصبغة؟", "اخلطي البودرة مع الماء العادي في وعاء غير معدني، وزعيها على الشعر الجاف لمدة 20-30 دقيقة ثم اشطفي بالماء."),
        ("هل تناسب شعر اللحية للرجال؟", "نعم، خيار ياباني شهير وممتاز لصبغ شعر الرأس واللحية."),
        ("ما هو بلد صنع صبغة بيجين؟", "صُنع بفخر في اليابان بواسطة شركة Hoyu العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع صبغات بيجين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يلزم إجراء اختبار تحسس قبل الاستخدام؟", "نعم، يُنصح دائماً بإجراء اختبار تحسس جلدي قبل 48 ساعة."),
        ("كم تدوم نتيجة اللون الأسود؟", "يدوم اللون لعدة أسابيع دون أن يبهت."),
        ("هل يجوز استخدامها للحواجب؟", "لا، يُمنع استخدامها للحواجب أو الرموش وتُستخدم لشعر الرأس واللحية فقط."),
        ("ما حجم العبوة؟", "تأتي في عبوة زجاجية صغيرة مدمجة بحجم 6 جم."),
        ("هل يسبب جفافاً للشعر؟", "عدم وجود أمونيا يقلل الجفاف ويحافظ على نسيج الشعر."),
        ("هل يلزم ارتداء قفازات؟", "نعم، ارتدي القفازات المرفقة لتجنب تصبغ اليدين."),
        ("هل العبوة 6 جم اقتصادية؟", "نعم، تكفي لصبغ الشيب واللحية بدقة."),
        ("ما هي رائحة الصبغة؟", "خالية من رائحة الأمونيا النفاذة."),
        ("هل يمكن استخدامها للشعر المسبوغ سابقاً؟", "نعم، توحد لون الشعر باللون الأسود الغني."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الرطوبة."),
        ("هل تزول مع الغسيل الأول؟", "لا، صبغة دائمة تثبت لأسابيع."),
        ("هل تناسب النساء والرجال؟", "نعم، صُممت لكلا الجنسين."),
        ("هل المشط مرفق؟", "يمكن توزيعها بفرشاة صبغة ناعمة."),
        ("هل تساعد في إعطاء لمعان للشعر؟", "نعم، تمنح الشعر الأسود بريقاً غنياً."),
        ("هل توجد ألوان أخرى؟", "تتوفر بدرجات أسود وبني مختلفة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في قارورة زجاجية محكمة الغطاء."),
        ("هل هي خيار ممتاز للسفر؟", "حجمها 6 جم مدمج ومثالي جداً للسفر.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Bigen Powder Hair Color Black (6g)</strong> is Japan's world-famous permanent powder hair dye engineered for 100% gray coverage without using ammonia. Water-activated, it requires no hydrogen peroxide developer, delivering a safe, gentle, and long-lasting oriental black shade.</p>
<p>Bigen Powder Hair Color preserves hair fiber integrity, preventing dryness and breakage. Packed in a compact 6g glass bottle, it is easy to prepare and apply for both men's beard care and women's hair gray coverage at home.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Full Gray & White Hair Coverage:</strong> Delivers a permanent, rich oriental black shade.</li>
  <li><strong>Water-Activated Formula:</strong> Requires only plain water; zero peroxide developer needed.</li>
  <li><strong>100% Ammonia-Free:</strong> Gentle on scalp and free of harsh chemical fumes.</li>
  <li><strong>Long-Lasting Permanent Color:</strong> Black shade stays vibrant for weeks without fading.</li>
  <li><strong>Ideal for Hair & Beard:</strong> Trusted Japanese dye for men's beard and women's hair.</li>
  <li><strong>Compact 6g Glass Bottle:</strong> Easy, precise, and economical for home application.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Mix):</strong> Pour Bigen powder into a non-metallic bowl, add plain water gradually, and stir into a smooth paste.</li>
  <li><strong>Step 2 (Apply):</strong> Wear gloves and apply paste evenly onto clean dry hair with a tint brush.</li>
  <li><strong>Step 3 (Process):</strong> Leave paste on hair for 20 to 30 minutes.</li>
  <li><strong>Step 4 (Rinse):</strong> Rinse thoroughly with warm water until clear, then wash with mild shampoo.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Black Colorant Powder (P-Phenylenediamine Sulfate):</strong> Delivers a deep, permanent black shade.</li>
  <li><strong>Cellulose Gum & Potato Starch:</strong> Provide a smooth, easy-to-apply paste texture.</li>
  <li><strong>Ammonia-Free Base:</strong> Protects hair cuticles from drying and breakage.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external application on head hair and beard only; do not use on eyebrows or eyelashes.</li>
  <li>Perform a skin patch test 48 hours prior to application.</li>
  <li>Avoid contact with eyes.</li>
  <li>Keep out of reach of children.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a Japanese water-activated, ammonia-free 100% gray coverage black hair and beard dye.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Bigen</td></tr>
  <tr><th>Category</th><td>Hair Care / Powder Hair Color</td></tr>
  <tr><th>Product Type</th><td>Water-Activated Permanent Black Powder Hair Dye</td></tr>
  <tr><th>Volume/Weight</th><td>6 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Gray & White Hair)</td></tr>
  <tr><th>Finish</th><td>Rich oriental black, shiny, 100% gray-free hair</td></tr>
  <tr><th>Texture</th><td>Fine powder mixing with water into paste</td></tr>
  <tr><th>Fragrance</th><td>Ammonia-Free (No harsh chemical odor)</td></tr>
  <tr><th>Active Ingredients</th><td>P-Phenylenediamine Sulfate, Cellulose Gum, Starch</td></tr>
  <tr><th>Country of Origin</th><td>Japan (Hoyu Co.)</td></tr>
  <tr><th>Manufacturer</th><td>Hoyu Co., Ltd. Japan</td></tr>
  <tr><th>Age Group</th><td>Adults (Men & Women)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Water-Activated Powder Dye & Gray Coverage</h2>

<h3>What problem does this solve?</h3>
<p>Bigen Powder Hair Color resolves gray hair visibility and chemical damage caused by ammonia and peroxide developers.</p>

<h3>Why choose Bigen?</h3>
<p>Activated by plain water, its gentle powder deposits intense black pigments into hair fibers without opening cuticle scales aggressively.</p>"""

    en_faqs = [
        ("What is Bigen Powder Hair Color Black 6g?", "It is a Japanese water-activated, ammonia-free permanent powder hair dye for 100% black gray coverage."),
        ("Does Bigen require peroxide developer?", "No, it is activated by plain water only; no hydrogen peroxide required."),
        ("Is it ammonia-free?", "Yes, it is 100% ammonia-free with no harsh fumes."),
        ("Does it cover white hair completely?", "Yes, it guarantees 100% complete gray and white hair coverage."),
        ("How do I mix and apply it?", "Mix powder with plain water into a paste, apply onto dry hair for 20-30 minutes, then rinse."),
        ("Is it suitable for men's beards?", "Yes, it is a globally popular dye for both head hair and beards."),
        ("Where is Bigen manufactured?", "It is proudly manufactured in Japan by Hoyu Co., Ltd."),
        ("How do I verify authenticity at Ekleel Abha?", "All Bigen products at Ekleel Abha are 100% original from certified distributors."),
        ("Is a skin allergy test required?", "Yes, perform a patch test 48 hours prior to application."),
        ("How long does the black color last?", "It is a permanent dye lasting several weeks."),
        ("Can it be used on eyebrows?", "No, strictly do not apply to eyebrows or eyelashes."),
        ("What volume is contained in the bottle?", "It comes in a compact 6g glass bottle."),
        ("Does it cause hair damage?", "Being ammonia-free, it minimizes drying and preserves hair strength."),
        ("Are gloves recommended?", "Yes, wear enclosed gloves to prevent temporary skin staining."),
        ("Is the 6g size economical?", "Yes, provides exact amounts for gray root and beard touch-ups."),
        ("What scent does it have?", "It is free of harsh chemical ammonia odors."),
        ("Can it be applied over previously dyed hair?", "Yes, it unifies hair tone into a rich black shade."),
        ("How should I store it?", "Store in a cool, dry place away from moisture."),
        ("Does it wash out after one shower?", "No, it is a permanent hair dye."),
        ("Can both men and women use it?", "Yes, formulated for both men and women."),
        ("Does it enhance black shine?", "Yes, it imparts rich, natural black shine."),
        ("Is it available in other shades?", "Available in various black and brown shades."),
        ("Is the glass bottle secure?", "Yes, comes in a tightly capped glass container."),
        ("Is it travel-friendly?", "Yes, its compact 6g size is perfect for travel."),
        ("Is it dentist/dermatologist tested?", "Yes, dermatologically safety-tested globally.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1757",
        "sku": "EK-1757",
        "gtin": "4902806001945",
        "category": "العناية بالشعر / صبغات الشعر البودرة",
        "brand": "Bigen",
        "ar": {
            "title": "صبغة شعر، اسود - 6 جم",
            "meta_title": "صبغة بيجين اسود بودرة بالماء 6جم | صيدلية إكليل أبها",
            "meta_description": "اشتري صبغة شعر بيجين اليابانية البودرة باللون الأسود (6جم). تُفعل بالماء بدون أمونيا لتغطية الشيب 100%. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بيجين", "صبغة_بيجين", "صبغة_بودرة", "تغطية_الشيب", "إكليل_أبها"]
        },
        "en": {
            "title": "Hair Dye, Black - 6g",
            "meta_title": "Bigen Powder Hair Color Black 6g | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Bigen Powder Hair Color Black (6g) from Japan. Water-activated & ammonia-free 100% gray coverage. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["bigen", "powder_dye", "black_dye", "water_activated", "ekleel_abha"]
        },
        "schema": {
            "brand": "Bigen",
            "category": "Hair Care / Hair Dye",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "bigen-powder-hair-color-black-6g.webp",
            "alt": "Bigen Powder Hair Color Black 6g",
            "title": "Bigen Powder Hair Color Black 6g"
        }
    }

def create_product_1758():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>علبة دبوس شعر sasha ياباني متوسط اصلي (Sasha Original Japanese Hair Pins Box - Medium Size)</strong> المستحضر الأساسي المعتمد لدى صالونات التجميل والسيدات لثبات وتثبيت تسريحات الشعر بكل أناقة ومتانة. صُنعت هذه الدبابيس اليابانية من الفولاذ المقاوم للصدأ عالي الجودة والصلابة، حيث تمتاز بتصميم متوسط الحجم بحواف كروية محمية تمنع خدش فروة الرأس أو تقصف خصلات الشعر أثناء التثبيت.</p>
<p>تضمن دبابيس ساشا اليابانية ثباتاً استثنائياً للتسريحات والمرفوعات وربطات الشعر طوال اليوم دون أن تنزلق، وتأتي في علبة دائرية محكمة تجعلها سهلة التخزين والحمل في الحقيبة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>دبابيس شعر يابانية أصيلة 100%:</strong> فولاذ صلب مقاوم للصدأ والانثناء.</li>
  <li><strong>حواف كروية محمية (Ball Tips):</strong> تمنع خدش الفروة أو تقصف الشعر أثناء الإدخال والسحب.</li>
  <li><strong>ثبات عالي وتثبيت محكم:</strong> تمسك التسريحات والمرفوعات بثبات قوي طوال اليوم دون انزلاق.</li>
  <li><strong>حجم متوسط مثالي:</strong> يناسب جميع أنواع الشعر والتسريحات اليومية والمناسبات.</li>
  <li><strong>طلاء أسود مقاوم للتأكل:</strong> لون أسود مطفي يختفي داخل الشعر دون إحداث لمعان غير مرغوب.</li>
  <li><strong>علبة مدمجة للتخزين:</strong> علبة عملية تحفظ الدبابيس من الضياع والتلوث.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التحضير):</strong> صممي تسريحة الشعر المطلوبة (كعكة، مرفوعات، أو طيات جانبية).</li>
  <li><strong>الخطوة الثانية (الإدخال):</strong> ادخلي دبوس ساشا الياباني والجانب المضلع لأسفل نحو الفروة للتثبيت المحكم.</li>
  <li><strong>الخطوة الثالثة (التثبيت):</strong> ثبتي الخصلات بالعدد المناسب من الدبابيس للحصول على ثبات كامل.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>فولاذ ياباني صلب (Japanese Stainless Steel):</strong> قوة وثبات مرن مقاوم للصدأ.</li>
  <li><strong>رؤوس كروية حامية:</strong> تضمن سلامة فروة الرأس والشعر.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي بتثبيت الشعر فقط.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال الصغار لتفادي الابتلاع.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة ومصفف شعر يبحثون عن دبابيس شعر يابانية أصيلة ذات ثبات متين وحماية للفروة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ساشا (Sasha Japan)</td></tr>
  <tr><th>الفئة</th><td>مستلزمات الشعر / دبابيس وإكسسوارات الشعر</td></tr>
  <tr><th>نوع المنتج</th><td>دبابيس شعر يابانية متوسطة الحجم (Original Hair Pins Box)</td></tr>
  <tr><th>الحجم/الوزن</th><td>علبة دبابيس شعر متوسطة</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (لجميع التسريحات)</td></tr>
  <tr><th>المظهر النهائي</th><td>تسريحة شعر متماسكة ومثبتة بجمال طوال اليوم</td></tr>
  <tr><th>الملمس</th><td>دبابيس معدنية ناعمة بحواف كروية</td></tr>
  <tr><th>العطر</th><td>غير مطبق (عديم الرائحة)</td></tr>
  <tr><th>المكونات النشطة</th><td>فولاذ ياباني صلب طلاء أسود</td></tr>
  <tr><th>بلد المنشأ</th><td>اليابان</td></tr>
  <tr><th>الشركة المصنعة</th><td>Sasha Hair Accessories Japan</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لتثبيت الشعر بالدبابيس اليابانية (Sasha)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تحل دبابيس ساشا اليابانية مشكلة انزلاق دبابيس الشعر العادية وتلف فروة الرأس بالرؤوس الحادة وتفكك التسريحات.</p>

<h3>لماذا تنجح دبابيس ساشا؟</h3>
<p>لأنها مصنوعة من فولاذ ياباني مرن ذي حواف كروية محمية يثبت الخصلات بقوة دون خدش الفروة أو تقصف الشعر.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الإدخال بالجانب المضلع أسفل:</strong> ادخلي الدبوس والجانب المضلع لأسفل نحو الفروة لثبات محكم.<br>
2. <strong>التخزين بالعلبة:</strong> احفظي الدبابيس بالعلبة المرفقة لمنع ضياعها.<br>
3. <strong>التثبيت المتوازن:</strong> وزعي الدبابيس بالتساوي في التسريحات الكثيفة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "جميع دبابيس الشعر متشابهة في التثبيت."<br>
<strong>الحقيقة:</strong> الفولاذ الياباني في دبابيس ساشا يمنح مرونة وانثنائية تحافظ على ثبات التسريحة دون الانزلاق.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتمتع الدبابيس اليابانية بمرونة فولاذية مصقولة تفصل وتضغط الخصلات بنظام التوتر المرن (Elastic Tension)، مما يمنع انزلاق الشعر أثناء الحركة.</p>"""

    faqs = [
        ("ما هي علبة دبوس شعر sasha ياباني متوسط اصلي؟", "هي علبة دبابيس شعر يابانية أصيلة مصنوعة من الفولاذ الصلب بحواف كروية لتثبيت التسريحات والمرفوعات متانة وأمان."),
        ("ما فائدة الرؤوس الكروية في دبابيس ساشا؟", "تحمي فروة الرأس من الخدوش وتمنع تقصف وقتل خصلات الشعر أثناء الإدخال والسحب."),
        ("هل الدبابيس ثابتة ولا تنزلق؟", "نعم، تمتاز بمرونة وقوة تثبيت يابانية تمسك الشعر طوال اليوم."),
        ("ما حجم الدبابيس؟", "تأتي بحجم متوسط مثالي للاستخدام اليومي والمناسبات."),
        ("ما هو بلد صنع دبابيس ساشا؟", "صُنع بفخر في اليابان وفق أعلى معايير الجودة."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع إكسسوارات ساشا لدى إكليل أبها أصلية 100% ومستوردة من اليابان مباشرة."),
        ("هل تصدأ الدبابيس مع الوقت؟", "لا، مصنوعة من فولاذ مقاوم للصدأ والتأكل."),
        ("هل اللون أسود مطفي؟", "نعم، طلاء أسود مطفي يختفي داخل الشعر بجمال."),
        ("هل يناسب جميع أنواع الشعر؟", "نعم، ممتاز للشعر الناعم، الكثيف، والمجعد."),
        ("هل العبوة عملية للتخزين؟", "نعم، تأتي في علبة تحفظ الدبابيس من الضياع."),
        ("كيف يتم إدخال الدبوس بالشكل الصحيح؟", "يُفضل إدخال الدبوس والجانب المضلع لأسفل نحو الفروة لثبات مضاعف."),
        ("هل تناسب الاستخدام في الصالونات؟", "نعم، خيار معتمد ومفضل لدى مصففي الشعر في الصالونات."),
        ("هل يناسب الأطفال؟", "مناسب لاستخدام الأطفال تحت إشراف لتثبيت تسريحات المدرسة."),
        ("هل الدبابيس حادة؟", "لا، حوافها كروية ناعمة وآمنة."),
        ("هل تتكسر أو تنثني بسهولة؟", "لا، الفولاذ الياباني يتميز بصلابة ومرونة عالية يمنع الانثناء."),
        ("كم دبوس تحتوي العلبة؟", "تحتوي على عدد وافر يكفي لاستخدامات متعددة."),
        ("هل هي مناسبة لتثبيت تسريحة الكعكة؟", "نعم، ممتازة جداً لتثبيت الكعكة والمرفوعات."),
        ("كيف أحتفظ بالعلبة؟", "تُحفظ في مكان جاف داخل حقيبة المكياج أو التسريحة."),
        ("هل يغير طلاء الدبوس لونه مع الاستخدام؟", "طلاء متين يظل ثابتاً دون تقشر."),
        ("هل تناسب الشعر الخفيف؟", "نعم، مسكتها المرنة تمسك الشعر الخفيف دون انزلاق."),
        ("هل تناسب تثبيت حجاب الرأس؟", "ممتازة لتثبيت طيات الحجاب والشعر الجانبي."),
        ("هل هي خفيفة الوزن؟", "نعم، خفيفة ولا تسبب ثقلاً على الرأس."),
        ("هل تناسب المناسبات والحفلات؟", "نعم، تضمن ثبات التسريحات المعقدة في الحفلات طوال السهرة."),
        ("هل العبوة اقتصادية؟", "نعم، خيار ممتاز وعالي الجودة يدوم لفترة طويلة."),
        ("هل العلبة سهلة الفتح؟", "نعم، علبة مدمجة وسهلة الاستخدام.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Sasha Original Japanese Hair Pins Box - Medium Size</strong> is the essential salon-grade accessory trusted globally for styling and securing hairstyles with durability and precision. Crafted from high-tensile Japanese stainless steel, these bobby pins feature smooth protective ball tips that prevent scalp scratching and hair strand breakage during insertion.</p>
<p>Providing firm, non-slip grip for buns, updos, and daily hair styling, Sasha Japanese hair pins come in a compact storage box that keeps your styling kit organized at home or on the go.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Original Japanese Steel:</strong> High-tensile stainless steel resistant to rust and bending.</li>
  <li><strong>Protective Ball Tips:</strong> Smooth rounded ends prevent scalp scratches and hair breakage.</li>
  <li><strong>Firm Non-Slip Grip:</strong> Securely holds updos, buns, and hair sections all day without slipping.</li>
  <li><strong>Versatile Medium Size:</strong> Ideal dimensions suitable for all hair types and styling needs.</li>
  <li><strong>Matte Black Coating:</strong> Blends invisibly into hair without unwanted glare.</li>
  <li><strong>Handy Storage Container:</strong> Keeps bobby pins organized and protected from loss.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Style):</strong> Arrange hair into desired bun, updo, or section.</li>
  <li><strong>Step 2 (Insert):</strong> Insert Sasha hair pin with the wavy side facing down toward the scalp for optimal grip.</li>
  <li><strong>Step 3 (Secure):</strong> Use necessary pins to firmly lock hair style in place.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Japanese Tempered Stainless Steel:</strong> Provides flexible, rust-resistant, long-lasting holding power.</li>
  <li><strong>Coated Protective Ball Tips:</strong> Ensure gentle scalp contact and hair safety.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external hair styling use only.</li>
  <li>Keep out of reach of young children to prevent choking hazard.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking authentic Japanese hair pins offering strong, scalp-safe hold for professional and daily hair styles.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Sasha Japan</td></tr>
  <tr><th>Category</th><td>Hair Accessories / Hair Pins & Clips</td></tr>
  <tr><th>Product Type</th><td>Original Japanese Medium Bobby Hair Pins Box</td></tr>
  <tr><th>Volume/Weight</th><td>Medium Hair Pins Storage Box</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (All Hairstyles)</td></tr>
  <tr><th>Finish</th><td>Firmly secured, non-slipping, elegant hair style</td></tr>
  <tr><th>Texture</th><td>Smooth coated steel pins with ball tips</td></tr>
  <tr><th>Fragrance</th><td>Unscented</td></tr>
  <tr><th>Active Ingredients</th><td>Japanese Stainless Steel, Protective Ball Tips</td></tr>
  <tr><th>Country of Origin</th><td>Japan</td></tr>
  <tr><th>Manufacturer</th><td>Sasha Hair Accessories Japan</td></tr>
  <tr><th>Age Group</th><td>All Ages</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Japanese Steel & Hair Styling Grip</h2>

<h3>What problem does this solve?</h3>
<p>Sasha Japanese Hair Pins resolve pin slipping, scalp scratches, and hairstyle collapse experienced with cheap bobby pins.</p>

<h3>Why choose Sasha?</h3>
<p>Tempered Japanese steel delivers spring-like tension that grips hair firmly, while smooth ball tips shield the scalp from abrasion.</p>"""

    en_faqs = [
        ("What is Sasha Original Japanese Hair Pins Box Medium Size?", "It is an authentic box of Japanese stainless steel bobby pins featuring protective ball tips for non-slip hair styling."),
        ("What are protective ball tips for?", "They protect the scalp from scratching and prevent hair strand tearing upon insertion."),
        ("Do these hair pins slip out easily?", "No, high-tensile Japanese steel provides a firm non-slip grip all day."),
        ("What size are these hair pins?", "They come in a versatile medium size ideal for daily and occasion hair styling."),
        ("Where are Sasha hair pins manufactured?", "They are proudly manufactured in Japan following high quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Sasha accessories at Ekleel Abha are 100% genuine Japanese imports."),
        ("Do these pins rust over time?", "No, they are made from high-grade rust-resistant stainless steel."),
        ("What color finish do they have?", "They feature a sleek matte black coating that blends invisibly into hair."),
        ("Are they suitable for fine and thick hair?", "Yes, their flexible spring tension holds fine, thick, and curly hair textures."),
        ("Is the box convenient for storage?", "Yes, it keeps bobby pins neat and prevents loss."),
        ("How do I insert bobby pins correctly?", "Insert with the wavy side facing down toward the scalp for maximum holding power."),
        ("Are they suitable for professional salon use?", "Yes, they are a preferred choice among professional hairstylists."),
        ("Can children use them?", "Safe for styling children's hair under adult supervision."),
        ("Are the pin ends sharp?", "No, they feature smooth rounded ball tips."),
        ("Do they bend out of shape easily?", "No, tempered Japanese steel retains its shape and elasticity after repeated use."),
        ("How many pins are in the box?", "Contains a generous supply for multiple styling uses."),
        ("Are they good for securing hair buns?", "Yes, excellent for holding buns, chignons, and updos firmly."),
        ("How should I store the box?", "Store in a dry place inside your beauty bag."),
        ("Does the coating peel off?", "No, durable matte coating resists chipping."),
        ("Do they hold thin hair securely?", "Yes, flexible spring grip holds thin hair without sliding."),
        ("Can they be used for securing scarves?", "Yes, useful for securing headscarves and side hair sections."),
        ("Are they lightweight?", "Yes, lightweight and comfortable without causing head pressure."),
        ("Are they ideal for party updos?", "Yes, they hold complex event hairstyles securely all evening."),
        ("Is the box economical?", "Yes, offers durable long-lasting value."),
        ("Is the box easy to open?", "Yes, compact dispenser box opens easily.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1758",
        "sku": "EK-1758",
        "gtin": "6900865722021",
        "category": "مستلزمات الشعر / دبابيس وإكسسوارات الشعر",
        "brand": "Sasha Japan",
        "ar": {
            "title": "علبة دبوس شعر sasha ياباني متوسط اصلي",
            "meta_title": "دبابيس شعر ساشا ياباني متوسط اصلي | صيدلية إكليل أبها",
            "meta_description": "اشتري علبة دبوس شعر sasha ياباني متوسط اصلي. دبابيس فولاذ ياباني برؤوس كروية لثبات التسريحات بدون انزلاق. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["ساشا", "دبابيس_شعر", "دبوس_ياباني", "تسريحات_الشعر", "إكليل_أبها"]
        },
        "en": {
            "title": "Sasha Original Japanese Hair Pins Box - Medium Size",
            "meta_title": "Sasha Japanese Hair Pins Medium Box | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Sasha Japanese Medium Hair Pins Box. High-tensile stainless steel bobby pins with ball tips. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["sasha", "hair_pins", "bobby_pins", "japanese_pins", "ekleel_abha"]
        },
        "schema": {
            "brand": "Sasha Japan",
            "category": "Hair Accessory / Hair Pins",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "sasha-original-japanese-hair-pins-box-medium-size.webp",
            "alt": "Sasha Original Japanese Hair Pins Box Medium Size",
            "title": "Sasha Original Japanese Hair Pins Box Medium Size"
        }
    }

def create_product_1761():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>صابون الحواجب الشفاف لتنسيق وتثبيت الحواجب 25 جم (Eyebrow Soap 25g)</strong> سر المكياج العصري الأكثر اعتماداً للحصول على حواجب ممتلئة، مرفوعة، ومثبتة بدقة متناهية (تأثير ميكروبليدينج صالونات) طوال اليوم. صُمم هذا الصابون الشفاف خصيصاً بمكونات مرطبة ولطيفة تغلف شعيرات الحاجب دون ترك أي أثر أبيض أو لزوجة، مما يتيح لكِ رسم وتمشيط وتثبيت الحواجب بالشكل المرغوب بسهولة فائقة.</p>
<p>تأتي العبوة بحجم 25 جم مدمج يشمل فرشاة سبولي (Spoolie Brush) مخصصة، لتمنحكِ حواجب طبيعية، مرتبة، ومرفوعة تعزز جمال عينيكِ ومكياجكِ اليومي والمحتص في ثوانٍ معدودة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تثبيت فائق يدوم طوال اليوم:</strong> يثبت شعيرات الحاجب في مكانها ب مظهر مرفوع وممتلئ دون تساقط.</li>
  <li><strong>شفاف 100% دون أثر أبيض:</strong> تركيبة شفافة لا تترك أي بقايا بيضاء أو تكتلات على الحاجب.</li>
  <li><strong>مظهر ميكروبليدينج طبيعي (Soap Brows):</strong> يمنح الحواجب مظهراً كثيفاً ومرتباً كالمحترفين.</li>
  <li><strong>مرفق بفرشاة تمشيط مخصصة:</strong> تأتي مع فرشاة سبولي مرنة لتسهيل التنسيق والتثبيت.</li>
  <li><strong>لطيف وغير متهيج:</strong> غني بالمرطبات التي تغذي شعر الحاجب وتمنع جفافه.</li>
  <li><strong>عبوة مدمجة 25 جم:</strong> حجم ممتاز وسهل الحمل في حقيبة المكياج اليومية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل):</strong> رشي قطرة ماء أو مثبت مكياج على فرشاة الحواجب المرفقة.</li>
  <li><strong>الخطوة الثانية (التحميل):</strong> مرري الفرشاة المبللة على صابون الحواجب الشفاف لتحميل كمية منا سبة.</li>
  <li><strong>الخطوة الثالثة (التمشيط والتثبيت):</strong> مشطي شعر الحاجبين للأعلى والداخل لتثبيتها بالمظهر المرفوع والممتلئ.</li>
  <li><strong>الخطوة الرابعة (الرسم):</strong> املئي الفراغات بقلم أو بودرة الحواجب بعد التثبيت للحصول على نتيجة مثالية.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>قاعدة جليسرين شفافة (Clear Glycerin Base):</strong> تثبت الشعر وتمنحه رطوبة ولمعاناً طبيعياً دون تكتل.</li>
  <li><strong>مركبات ثبات آمنة:</strong> تحافظ على شكل الحاجب المرفوع طوال اليوم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الحواجب فقط.</li>
  <li>تجنبي ملامسة الصابون المباشرة داخل العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان جاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن صابون شفاف مخصص لرفع وتثبيت الحواجب بمظهر كثيف وطبيعي يدوم طوال اليوم.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>عام / إكليل ابها للمكياج</td></tr>
  <tr><th>الفئة</th><td>المكياج / تثبيت وتنسيق الحواجب</td></tr>
  <tr><th>نوع المنتج</th><td>صابون الحواجب الشفاف لتثبيت ورفع الحواجب (25g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>25 جم مع فرشاة</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة وشعر الحواجب</td></tr>
  <tr><th>المظهر النهائي</th><td>حواجب ممتلئة، مرفوعة، مثبتة ومجملة بطبيعية</td></tr>
  <tr><th>الملمس</th><td>جل شمعي شفاف ناعم</td></tr>
  <tr><th>العطر</th><td>عديم الرائحة (عديم العطور)</td></tr>
  <tr><th>المكونات النشطة</th><td>جليسرين نقي، شمع تثبيت آمن</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين / تركيا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Professional Makeup Care</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 15 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لتقنية صابون الحواجب الشفاف (Soap Brows)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج صابون الحواجب الشفاف مشكلة تطاير وترهل شعر الحواجب وفقدان التثبيت طوال اليوم مع تجنب تكتلات الجل الأبيض.</p>

<h3>لماذا تنجح هذه التقنية؟</h3>
<p>لأن الجليسرين والشمع الشفاف يغلفان كل شعيرة بنظافة، ويمنحان الحواجب رفعة وتماسكاً طبيعياً كالميكروبليدينج.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>بيل الفرشاة خفيفاً:</strong> رشي قطرة ماء واحدة على الفرشاة لتفادي تسييل الصابون.<br>
2. <strong>التمشيط للأعلى:</strong> مشطي شعر الحاجب للأعلى والداخل لرفع زاوية العين.<br>
3. <strong>الرسم بعد التثبيت:</strong> ارسمي الفراغات بقلم الحواجب بعد جفاف صابون الحواجب.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "صابون الحواجب يسبب تساقط الشعر."<br>
<strong>الحقيقة:</strong> يحتوي الصابون المخصص على الجليسرين الذي يرطب شعر الحاجب ويحميه من التكسر.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يشكل الشمع الشفاف مع الجليسرين طبقة مرنة تغلف ألياف شعر الحاجب وتثبت زاوية انحنائها دون تغيير اللون الطبيعي.</p>"""

    faqs = [
        ("ما هو صابون الحواجب الشفاف 25 جم؟", "هو صابون شفاف مخصص لرفع وتمشيط وتثبيت شعيرات الحواجب بمظهر ممتلئ وطبيعي طوال اليوم مع فرشاة مرفقة."),
        ("هل يترك الصابون بقايا أو تكتلات بيضاء؟", "لا، يتميز بفرومولة شفافة 100% لا تترك أي أثر أبيض أو تكتل على شعر الحاجب."),
        ("هل يأتي مع فرشاة؟", "نعم، تأتي مع فرشاة سبولي مخصصة لتسهيل التمشيط والتثبيت."),
        ("ما حجم العبوة؟", "تأتي بحجم 25 جم مدمج ومريح."),
        ("كيف يتم استخدام صابون الحواجب؟", "بلي الفرشاة بقطرة ماء، مرريها على الصابون، ومشطي الحواجب للأعلى لرفعها وتثبيتها."),
        ("هل يدوم التثبيت طوال اليوم؟", "نعم، يوفر تثبيتاً فائقاً يدوم طوال اليوم دون أن يترهل الشعر."),
        ("هل يمكن رسم الحواجب بعده؟", "نعم، يمكنكِ ملء الفراغات بقلم أو بودرة الحواجب بعد التثبيت."),
        ("هل يسبب تساقط شعر الحواجب؟", "لا، يحتوي على الجليسرين والمرطبات التي تغذي شعر الحاجب وتمنع الجفاف."),
        ("ما هو بلد صنع المنتج؟", "تم تصنيعه وفق أعلى معايير الجودة لمستحضرات التجميل."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع مستحضرات التجميل لدى إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يناسب الاستخدام اليومي؟", "نعم، آمن وممتاز للاستخدام اليومي وفي المناسبات."),
        ("هل يناسب جميع ألوان الحواجب؟", "نعم، هو شفاف تماماً ويناسب الحواجب السوداء، البنية، والفاتحة."),
        ("هل يذوب مع العرق؟", "مقاوم للرطوبة ويثبت الشعيرات بثبات قوي."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان جاف ومغلقة بإحكام."),
        ("هل يناسب الحواجب الخفيفة؟", "نعم، يرفع الشعيرات ويمنح الحواجب الخفيفة مظهراً أكثر كثافة واملاءً."),
        ("هل يمكن بيل الفرشاة بمثبت المكياج؟", "نعم، بيل الفرشاة بمثبت المكياج يمنح ثباتاً مضاعفاً."),
        ("هل العبوة سهلة الحمل؟", "نعم، عبوة مدمجة وخفيفة الوزن في حقيبة المكياج."),
        ("هل يترك أثراً لزجاً؟", "يجف بمظهر طبيعي غير لزج."),
        ("هل يغسل بسهولة بالماء؟", "نعم، يغسل بسهولة بماء فاتر أو غسول الوجه."),
        ("هل يناسب الرجال لتنسيق الحواجب؟", "نعم، خيار ممتاز لتنسيق الحواجب بطبيعية دون لون."),
        ("هل العبوة 25 جم تكفي لفترة طويلة؟", "نعم، تكفي لأشهر من الاستخدام اليومي المنتظم."),
        ("هل يغير لون صبغة الحواجب؟", "لا، شفاف يحافظ على لون حاجبيكِ الطبيعي."),
        ("هل يلزم ترطيب الحواجب بعده؟", "الجليسرين يرطب الشعر تلقائياً أثناء التثبيت."),
        ("هل الفرشاة قابلة للتنظيف؟", "نعم، تُغسل الفرشاة بالماء وتجفف للاستخدام المتكرر."),
        ("هل يمنح مظهر الصالونات؟", "نعم، يمنح مظهر Soap Brows الكثيف والمرفوع كالمحترفين.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Eyebrow Soap 25g</strong> is the ultimate modern makeup secret to achieving feathered, lifted, and perfectly styled "soap brows" that stay locked in place all day. Formulated with clear hydrating glycerin, this transparent wax-soap coats each eyebrow hair without leaving white flakes, residue, or stiffness.</p>
<p>Composed in a compact 25g container with a specialized spoolie brush included, it empowers you to comb, lift, and shape natural or microbladed-style eyebrows effortlessly within seconds.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>All-Day Firm Hold:</strong> Locks eyebrow hairs in place with a lifted, fuller appearance without flaking.</li>
  <li><strong>100% Transparent Zero White Residue:</strong> Clear formula leaves zero white flakes or clumping.</li>
  <li><strong>Natural Feathered Soap Brow Look:</strong> Creates salon-style microbladed, voluminous brow shapes.</li>
  <li><strong>Spoolie Brush Included:</strong> Comes with a flexible spoolie applicator for easy styling.</li>
  <li><strong>Gentle Hydrating Base:</strong> Enriched with glycerin to condition eyebrow hairs and prevent dryness.</li>
  <li><strong>Compact 25g Travel Tin:</strong> Portable tin ideal for your daily makeup bag.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Dampen):</strong> Spritz a drop of water or setting spray onto the included spoolie brush.</li>
  <li><strong>Step 2 (Load):</strong> Rub the damp spoolie over the eyebrow soap to pick up product.</li>
  <li><strong>Step 3 (Style):</strong> Comb eyebrow hairs upward and outward to lift and lock them in place.</li>
  <li><strong>Step 4 (Fill):</strong> Fill sparse gaps with your favorite brow pencil or powder afterward if desired.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Clear Glycerin Base:</strong> Conditions brow hairs while providing transparent, long-lasting holding power.</li>
  <li><strong>Safe Styling Wax Polymers:</strong> Keep brow hairs locked in a lifted shape all day.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external eyebrow styling use only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a transparent, long-lasting eyebrow soap for salon-style lifted, fuller brows.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Generic / Ekleel Abha Makeup</td></tr>
  <tr><th>Category</th><td>Makeup / Eyebrow Styling & Fixers</td></tr>
  <tr><th>Product Type</th><td>Transparent Eyebrow Styling Soap & Spoolie Kit</td></tr>
  <tr><th>Volume/Weight</th><td>25 g with Spoolie Brush</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin & Eyebrow Hair Types</td></tr>
  <tr><th>Finish</th><td>Fuller, lifted, styled & natural eyebrow finish</td></tr>
  <tr><th>Texture</th><td>Smooth clear wax-soap gel</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-Free</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Glycerin, Safe Holding Wax Polymers</td></tr>
  <tr><th>Country of Origin</th><td>China / Turkey</td></tr>
  <tr><th>Manufacturer</th><td>Professional Makeup Care</td></tr>
  <tr><th>Age Group</th><td>All Ages (15+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Clear Glycerin & Feathered Soap Brows</h2>

<h3>What problem does this solve?</h3>
<p>Eyebrow Soap 25g resolves messy, drooping brow hairs and white gel flaking experienced with traditional brow gels.</p>

<h3>Why choose Eyebrow Soap?</h3>
<p>Clear glycerin coats brow hairs evenly, holding them in a lifted, voluminous shape without stiffness or residue.</p>"""

    en_faqs = [
        ("What is Eyebrow Soap 25g?", "It is a clear eyebrow wax-soap designed to lift, style, and set eyebrow hairs into a full feathered look with an included spoolie brush."),
        ("Does it leave white flakes or residue?", "No, its 100% transparent formula leaves zero white flakes or clumping."),
        ("Does it include a brush?", "Yes, it includes a flexible spoolie brush for easy brow styling."),
        ("What size is the container?", "It comes in a compact 25g tin."),
        ("How do I use eyebrow soap?", "Dampen spoolie with water, rub onto soap, and comb brows upward to set."),
        ("Does the hold last all day?", "Yes, it provides firm all-day hold keeping brows lifted."),
        ("Can I fill brows with a pencil afterward?", "Yes, fill sparse gaps with brow pencil or powder after styling."),
        ("Does it cause eyebrow hair loss?", "No, glycerin conditions brow hairs to prevent drying and damage."),
        ("Where is it manufactured?", "It is produced following cosmetic safety standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All makeup products at Ekleel Abha are 100% original."),
        ("Is it safe for daily use?", "Yes, safe and ideal for daily makeup routines."),
        ("Does it suit all eyebrow colors?", "Yes, it is completely transparent and suits black, brown, and blonde brows."),
        ("Is it sweat-resistant?", "Yes, moisture-resistant formula locks brows in place."),
        ("How should I store it?", "Store tightly closed in a cool, dry place."),
        ("Does it work on thin brows?", "Yes, lifting thin brow hairs makes brows appear thicker and fuller."),
        ("Can setting spray be used to dampen the brush?", "Yes, dampening with setting spray provides extra long-lasting hold."),
        ("Is it travel-friendly?", "Yes, compact 25g tin fits easily into makeup bags."),
        ("Does it feel sticky?", "It dries down to a natural, non-sticky finish."),
        ("How do I wash it off?", "Washes off easily with warm water or facial cleanser."),
        ("Can men use it for brow grooming?", "Yes, great for natural, clear men's brow grooming."),
        ("Does the 25g tin last long?", "Yes, lasts for months of daily application."),
        ("Does it alter dyed brow color?", "No, transparent formula preserves natural or dyed brow color."),
        ("Does it require post-application moisturizer?", "Glycerin automatically hydrates brow hair during wear."),
        ("Is the spoolie brush washable?", "Yes, wash spoolie with water and dry for reuse."),
        ("Does it give a salon microbladed look?", "Yes, creates voluminous, feathered salon-style brows easily.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1761",
        "sku": "EK-1761",
        "gtin": "6930236302897",
        "category": "المكياج / تثبيت وتنسيق الحواجب",
        "brand": "Generic Makeup",
        "ar": {
            "title": "صابون الحواجب الشفاف لتنسيق وتثبيت الحواجب - 25 جم",
            "meta_title": "صابون الحواجب الشفاف 25جم | صيدلية إكليل أبها",
            "meta_description": "اشتري صابون الحواجب الشفاف لتنسيق وتثبيت الحواجب (25جم) مع فرشاة. تثبيت فائق يدوم طوال اليوم دون أثر أبيض. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["صابون_الحواجب", "تثبيت_الحواجب", "مكياج_الحواجب", "soap_brows", "إكليل_أبها"]
        },
        "en": {
            "title": "Eyebrow Soap 25g",
            "meta_title": "Eyebrow Soap 25g with Spoolie Brush | Ekleel Abha Pharmacy",
            "meta_description": "Buy Eyebrow Soap (25g) with Spoolie Brush. Transparent firm hold for feathered soap brows without white flakes. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["eyebrow_soap", "brow_styling", "soap_brows", "makeup", "ekleel_abha"]
        },
        "schema": {
            "brand": "Generic Makeup",
            "category": "Makeup / Eyebrow Fixer",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "eyebrow-soap-25g.webp",
            "alt": "Eyebrow Soap 25g",
            "title": "Eyebrow Soap 25g"
        }
    }

def create_product_1762():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول الجسم لايف بوي انتعاش الليمون للحماية من الجراثيم 300 مل مع ليفة (Lifebuoy Lemon Fresh Body Wash 300ml with Loofah)</strong> الحل المتكامل للحصول على نظافة فائقة وانتعاش حمضي يوقظ الحواس مع حماية قوية ومثبتة من 99.9% من الجراثيم والبكتيريا. يجمع هذا الغسول المتطور من لايف بوي بين خلاصة الليمون الطبيعي المنعشة وتقنية الفضة المتقدمة (Activ Silver Formula)، مما يضمن لكِ ولعائلتكِ حماية حميمة ونظافة عميقة طوال اليوم.</p>
<p>يأتي غسول لايف بوي بحجم 300 مل مرفقاً بليفة استحمام فاخرة ترغي الصابون بكثافة، لتزيل الأوساخ والدهون الزائدة وروائح العرق، وتترك بشرة جسمكِ ناعمة، صحية، ومفعمة بعقير الليمون المنعش.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية مثبتة من 99.9% من الجراثيم:</strong> تركيبة الفضة النشطة تحمي البشرة من البكتيريا والجراثيم.</li>
  <li><strong>انتعاش الليمون الطبيعي:</strong> يمنح شعوراً مضاعفاً بالنظافة والحيوية والانتعاش طوال اليوم.</li>
  <li><strong>مرفق بليفة استحمام مجانية:</strong> ليفة ناعمة تولد رغوة غنية وتقشر البشرة بلطف.</li>
  <li><strong>إزالة الشوائب وعرق الجسم:</strong> ينظف المسام العميقة ويقضي على البكتيريا المسببة لرائحة العرق.</li>
  <li><strong>لطيف وغير مسبب للجفاف:</strong> ينظف بفاعلية مع الحفاظ على رطوبة الجلد الطبيعية.</li>
  <li><strong>عبوة اقتصادية 300 مل:</strong> حجم ممتازة للاستخدام العائلي اليومي مع ليفة فاخرة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل):</strong> بلي ليفة الاستحمام المرفقة بالماء الفاتر.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> اسكبي كمية مناسبة من غسول لايف بوي بالليمون على الليفة واضغطيها لتوليد رغوة كثيفة.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي كامل بشرة الجسم بالرغوة الغنية لتنظيفها وتهدئتها.</li>
  <li><strong>الخطوة الرابعة (الشطف):</strong> اشطفي الجسم بالماء الفاتر واستمتعي بالانتعاش والنظافة.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة الليمون الطبيعي (Lemon Juice Extract):</strong> ينعش البشرة ويطهر الدهون والرواسب.</li>
  <li><strong>تقنية الفضة النشطة (Activ Silver Formula):</strong> توفر حماية متكاملة ضد الجراثيم والبكتيريا الضارة.</li>
  <li><strong>الجليسرين والمرطبات:</strong> تمنع جفاف الجلد أثناء الاستحمام.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي أثناء الاستحمام فقط.</li>
  <li>تجنبي ملامسة الغسول المباشرة للعينين؛ وفي حال ملامستهما اشطفي بالماء.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحثون عن حماية يومية قوية من الجراثيم وانتعاش حمضي مائل بالليمون لجميع أفراد العائلة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لايف بوي (Lifebuoy)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / غسول وشاور جل الجسم</td></tr>
  <tr><th>نوع المنتج</th><td>غسول الجسم للحماية من الجراثيم بانتعاش الليمون (300ml + ليفة)</td></tr>
  <tr><th>الحجم/الوزن</th><td>300 مل مع ليفة مجانية</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (الجلد والجسم)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم نظيف، صحي، محمي من الجراثيم ومفعم بالانتعاش</td></tr>
  <tr><th>الملمس</th><td>جل سائل غني يولد رغوة كثيفة</td></tr>
  <tr><th>العطر</th><td>عطر اللوز والليمون الطبيعي المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة الليمون، الفضة النشطة (Activ Silver)، جليسرين</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الإمارات (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (لايف بوي)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 6 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لتقنية الفضة النشطة وانتعاش الليمون (Lifebuoy)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول لايف بوي بالليمون مشكلة تراكم البكتيريا ورائحة العرق والجراثيم الناتجة عن التلوث والمجهود اليومي.</p>

<h3>لماذا تنجح تركيبته؟</h3>
<p>لأن الفضة النشطة تقضي على 99.9% من الجراثيم، بينما يطهر الليمون الدهون الزائدة ويمنح انتعاشاً يدوم طوال اليوم.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام مع الليفة المرفقة:</strong> اسكبي الغسول على الليفة المبللة لتوليد رغوة كثيفة تنظف المسام.<br>
2. <strong>التركيز على مناطق العرق:</strong> دلكي الإبطين والجسم بعناية للتخلص من البكتيريا المسببة للرائحة.<br>
3. <strong>الشطف بالماء الفاتر:</strong> اشطفي الجسم جيداً بالماء للحفاظ على النظافة والانتعاش.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الغسول المضاد للجراثيم يسبب جفاف البشرة."<br>
<strong>الحقيقة:</strong> يحتوي غسول لايف بوي على مرطبات ومكونات ناعمة تحمي البشرة من الجفاف أثناء التنظيف.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخترق جزيئات الفضة النشطة (Activ Silver) غشاء جدار الخلايا البكتيرية وتوقف تكاثرها بنسبة 99.9%، بينما تفكك حمضية الليمون الطبيعية الدهون السطحية الملتصقة بالبشرة.</p>"""

    faqs = [
        ("ما هو غسول الجسم لايف بوي انتعاش الليمون 300 مل؟", "هو غسول جسم مضاد للجراثيم يمنح حماية 99.9% وانتعاش الليمون الطبيعي مع ليفة استحمام مجانية مرفقة."),
        ("ما فائدة تقنية الفضة النشطة وخلاصة الليمون؟", "تقضي الفضة النشطة على الجراثيم والبكتيريا، بينما يطهر الليمون الرواسب ويمنح انتعاشاً حيوياً."),
        ("هل تأتي مع ليفة استحمام مجانية؟", "نعم، تأتي العبوة 300 مل مرفقة بليفة استحمام فاخرة مجانية."),
        ("ما حجم العبوة؟", "تأتي بحجم 300 مل."),
        ("هل يقضي على رائحة العرق؟", "نعم، يقضي على البكتيريا المسببة لرائحة العرق وينعش الجسم طوال اليوم."),
        ("هل يناسب جميع أنواع البشرة؟", "نعم، مناسب للبشرة العادية، الدهنية، والمختلطة."),
        ("ما هو بلد صنع لايف بوي؟", "صُنع بواسطة شركة يونيلفر (Unilever) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات لايف بوي لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يسبب جفافاً للبشرة؟", "لا، يحتوي على مرطبات تحافظ على نعومة ورطوبة الجلد."),
        ("هل يناسب جميع أفراد العائلة؟", "نعم، ممتاز للبالغين والأطفال فوق 6 سنوات."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اسكبي الغسول على الليفة المبللة، دلكي الجسم للحصول على رغوة، ثم اشطفي بالماء."),
        ("هل ينظف المسام العميقة؟", "نعم، يزيل الشوائب والدهون الزائدة من مسام الجسم."),
        ("ما هي رائحة الغسول؟", "يتميز برائحة الليمون الحمضية المنعشة والحيوية."),
        ("هل يناسب الاستخدام اليومي؟", "نعم، آمن وممتاز للاستحمام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف داخل الحمام."),
        ("هل الرغوة كثيفة؟", "نعم، تولد الليفة المرفقة رغوة كريمية كثيفة."),
        ("هل يساعد في حماية الأطفال من الجراثيم؟", "نعم، يمنح حماية ممتازة للأطفال بعد اللعب والدراسة."),
        ("هل العبوة محكمة الغلق؟", "تأتي بعبوة ضغط متينة بغطاء محكم."),
        ("هل يناسب الاستخدام بعد ممارسة الرياضة؟", "ممتاز جداً بعد التمارين لإزالة العرق والجراثيم والانتعاش."),
        ("هل يترك أي بقايا زلتة على الجسم؟", "لا، يشطف بسهولة وسرعة بالماء الفاتر."),
        ("هل يحمي من العدوى الجلدية البكتيرية؟", "نعم، حمايته من 99.9% من الجراثيم تقي من الالتهابات البكتيرية."),
        ("هل الليفة قابلة لإعادة الاستخدام؟", "نعم، تُشطف وتجفف للاستخدام المتكرر."),
        ("هل يعزز حيوية الجسم الصباحية؟", "نعم، انتعاش الليمون يوقظ الحواس ويمنح نشاطاً صباحياً."),
        ("هل العبوة 300 مل + ليفة اقتصادية؟", "نعم، توفر قيمة اقتصادية ممتازة للعناية اليومية."),
        ("هل يوصى به للأطباء والعائلات؟", "نعم، لايف بوي العلامة الأولى المعتمدة للحماية من الجراثيم عالمياً.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Lifebuoy Lemon Fresh Body Wash 300ml with Loofah</strong> is the complete family showering solution delivering superior germ protection and refreshing citrus vitality. Powered by Lifebuoy's advanced Activ Silver Formula, it protects skin against 99.9% of harmful bacteria and germs while lifting away deep pore dirt and sweat odor.</p>
<p>Paired with a complimentary luxury shower loofah, this 300ml body wash builds rich, cleansing lather that leaves skin feeling soft, healthy, and energized with a long-lasting natural lemon aroma.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Proven 99.9% Germ Protection:</strong> Activ Silver Formula shields skin against disease-causing bacteria.</li>
  <li><strong>Natural Lemon Freshness:</strong> Invigorates senses with a vibrant, lasting citrus fragrance.</li>
  <li><strong>Complimentary Shower Loofah Included:</strong> Soft loofah creates rich foam and gently exfoliates skin.</li>
  <li><strong>Clears Body Sweat & Impurities:</strong> Deep cleanses pores and neutralizes odor-causing bacteria.</li>
  <li><strong>Gentle Non-Drying Formula:</strong> Cleanses effectively while preserving skin's natural moisture balance.</li>
  <li><strong>Economical 300ml Pack:</strong> Great family value bundle complete with a bath loofah.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet the included shower loofah with warm water.</li>
  <li><strong>Step 2 (Apply):</strong> Pour a suitable amount of Lifebuoy Lemon Fresh Body Wash onto loofah and squeeze for rich lather.</li>
  <li><strong>Step 3 (Massage):</strong> Massage rich foam over whole body skin to cleanse and refresh.</li>
  <li><strong>Step 4 (Rinse):</strong> Rinse body with warm water and enjoy lasting freshness.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Lemon Juice Extract:</strong> Purifies surface oils and delivers a refreshing citrus fragrance.</li>
  <li><strong>Activ Silver Formula:</strong> Advanced germ-protection technology shielding against 99.9% of bacteria.</li>
  <li><strong>Glycerin & Conditioners:</strong> Prevent skin moisture loss during showering.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external body shower cleansing only.</li>
  <li>Avoid direct contact with eyes; rinse immediately with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking daily 99.9% germ protection paired with refreshing citrus lemon vitality for the whole family.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lifebuoy</td></tr>
  <tr><th>Category</th><td>Personal Care / Body Washes & Shower Gels</td></tr>
  <tr><th>Product Type</th><td>Antibacterial Lemon Fresh Body Wash + Loofah</td></tr>
  <tr><th>Volume/Weight</th><td>300 ml + Free Loofah</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Body Skin)</td></tr>
  <tr><th>Finish</th><td>Clean, germ-protected, vibrant & smooth body skin</td></tr>
  <tr><th>Texture</th><td>Rich lathering fluid gel</td></tr>
  <tr><th>Fragrance</th><td>Vibrant Natural Lemon Fresh fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Lemon Juice Extract, Activ Silver Formula, Glycerin</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / UAE (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever (Lifebuoy)</td></tr>
  <tr><th>Age Group</th><td>All Ages (6+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Activ Silver & Citrus Antibacterial Protection</h2>

<h3>What problem does this solve?</h3>
<p>Lifebuoy Lemon Fresh Body Wash resolves bacterial accumulation, body sweat odor, and environmental dirt build-up.</p>

<h3>Why choose Lifebuoy?</h3>
<p>Activ Silver technology targets cell walls of 99.9% of harmful bacteria, while lemon extract purifies excess sebum.</p>"""

    en_faqs = [
        ("What is Lifebuoy Lemon Fresh Body Wash 300ml with Loofah?", "It is an antibacterial body wash providing 99.9% germ protection and fresh lemon fragrance with a free loofah included."),
        ("What are the benefits of Activ Silver and Lemon Extract?", "Activ Silver shields against 99.9% of germs, while lemon purifies excess oils and refreshes skin."),
        ("Is a shower loofah included?", "Yes, it comes with a complimentary luxury bath loofah."),
        ("What size is the bottle?", "It comes in a 300ml bottle."),
        ("Does it eliminate sweat odor?", "Yes, it neutralizes odor-causing bacteria for all-day freshness."),
        ("Is it suitable for all skin types?", "Yes, suitable for normal, oily, and combination skin types."),
        ("Where is Lifebuoy manufactured?", "It is produced by Unilever under global hygiene standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Lifebuoy products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it dry out skin?", "No, it contains humectants that preserve skin softness and moisture."),
        ("Is it safe for the whole family?", "Yes, ideal for adults and children aged 6+."),
        ("How do I use it correctly?", "Pour onto wet loofah, lather over body skin, and rinse thoroughly with water."),
        ("Does it deep clean pores?", "Yes, clears trapped dirt and excess sebum from body pores."),
        ("What fragrance does it have?", "It features a fresh, vibrant natural lemon citrus scent."),
        ("Is it safe for daily use?", "Yes, safe and ideal for daily shower use."),
        ("How should I store the bottle?", "Store in a cool, dry place inside your shower area."),
        ("Does it create rich foam?", "Yes, the included loofah builds creamy, abundant lather."),
        ("Does it protect kids from germs?", "Yes, provides excellent germ protection for kids after play and school."),
        ("Is the bottle securely sealed?", "Yes, it comes in an easy-squeeze bottle with a flip cap."),
        ("Is it good after workouts?", "Yes, excellent for washing off workout sweat and bacteria."),
        ("Does it rinse out easily?", "Yes, rinses cleanly with warm water leaving zero sticky film."),
        ("Does it help prevent bacterial skin infections?", "Yes, shielding against 99.9% of germs helps prevent bacterial skin flare-ups."),
        ("Is the loofah reusable?", "Yes, rinse and hang loofah to dry after each use."),
        ("Does it boost morning shower energy?", "Yes, vibrant lemon aroma energizes senses during morning showers."),
        ("Is the 300ml + Loofah bundle economical?", "Yes, offers great value for family personal care."),
        ("Is Lifebuoy globally recommended?", "Yes, Lifebuoy is the world's leading germ protection brand.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1762",
        "sku": "EK-1762",
        "gtin": "6281006482074",
        "category": "العناية الشخصية / غسول وشاور جل الجسم",
        "brand": "Lifebuoy",
        "ar": {
            "title": "غسول الجسم لايف بوي انتعاش الليمون للحماية من الجراثيم 300 مل مع ليفة",
            "meta_title": "غسول لايف بوي بالليمون 300مل مع ليفة | صيدلية إكليل أبها",
            "meta_description": "اشتري غسول الجسم لايف بوي انتعاش الليمون للحماية من الجراثيم (300مل) مع ليفة مجانية. حماية 99.9% من الجراثيم بالفضة النشطة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["لايف_بوي", "غسول_لايف_بوي", "انتعاش_الليمون", "حماية_الجراثيم", "إكليل_أبها"]
        },
        "en": {
            "title": "Lifebuoy Lemon Fresh Body Wash 300ml with Loofah",
            "meta_title": "Lifebuoy Lemon Fresh Body Wash 300ml with Loofah | Ekleel Abha",
            "meta_description": "Buy Lifebuoy Lemon Fresh Body Wash (300ml) with free Loofah. 99.9% germ protection with Activ Silver. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["lifebuoy", "body_wash", "lemon_fresh", "germ_protection", "ekleel_abha"]
        },
        "schema": {
            "brand": "Lifebuoy",
            "category": "Personal Care / Body Wash",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "lifebuoy-lemon-fresh-body-wash-300ml-with-loofah.webp",
            "alt": "Lifebuoy Lemon Fresh Body Wash 300ml with Loofah",
            "title": "Lifebuoy Lemon Fresh Body Wash 300ml with Loofah"
        }
    }

print("Loaded Batch 12 builders")
