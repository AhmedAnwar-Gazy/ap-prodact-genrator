import json, os
from build_hair_mask import build_hair_mask_product

def create_product_1739():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>خيط تنظيف الأسنان من تيسي للعناية اليومية وحماية اللثة (Taisi Dental Floss)</strong> الأداة الطبية الأساسية التي تضمن نظافة فموية كاملة وحماية فائقة للثة من التراجع والالتهابات. صُمم هذا الخيط من ألياف دقيقة مرنة ومقاومة للتأكل والانقطاع، حيث ينزلق بسلاسة فائقة بين الفراغات الضيقة للأسنان ليصل إلى المناطق التي تعجز فرشاة الأسنان العادية عن الوصول إليها.</p>
<p>يعمل خيط تيسي على إزالة بقايا الطعام والبلاك المتراكم بين الأسنان وتحت خط اللثة بفاعلية مذهلة، مما يمنع تكون الجير الصلب والنخر الجانبي والتسوس، ويحافظ على نفس منعش ولثة صحية وقوية عند استخدامه كجزء من روتين العناية الفموية اليومي.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف عميق بين الأسنان:</strong> يزيل بقايا الطعام والبلاك من الفراغات الضيقة التي لا تصلها الفرشاة.</li>
  <li><strong>ألياف مرنة ومقاومة للانقطاع:</strong> نسيج متين ينزلق بسلاسة دون أن يتفتت أو ينقطع أثناء الاستخدام.</li>
  <li><strong>حماية فائقة للثة:</strong> يقلل التهابات اللثة ونزيفها الناجم عن تراكم البكتيريا والبلاك الجانبي.</li>
  <li><strong>الوقاية من التسوس والجير:</strong> يمنع تكلس البلاك وتحوله إلى جير صلب بين الأسنان.</li>
  <li><strong>نفس منعش ونظافة كاملة:</strong> يساعد في القضاء على البكتيريا المسببة لرائحة الفم الكريهة.</li>
  <li><strong>عبوة مدمجة وعملية:</strong> تصميم محمول وسهل القطع يرافقكِ في المنزل وفي السفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (القطع واللف):</strong> اقطعي حوالي 45 سم من خيط تيسي ولفيظ المعظم حول أصلع الوسطى في كلتا اليدين.</li>
  <li><strong>الخطوة الثانية (التثبيت):</strong> امسكي الخيط بصلابة بين الإبهامين والسبابتين واتركي حوالي 3-5 سم بين اليدين.</li>
  <li><strong>الخطوة الثالثة (الإدخال):</strong> أدخلي الخيط بلطف بحركة إمامية وخلفية بين الأسنان دون ضغط قسري على اللثة.</li>
  <li><strong>الخطوة الرابعة (التنظيف):</strong> انحني بالخيط على شكل حرف C حول كل سن وحركيه للأعلى والأسفل ضد جدار السن.</li>
  <li><strong>الخطوة الخامسة (التكرار):</strong> استخدمي جزءاً نظيفاً من الخيط لكل فراغ سنّي بين الأسنان.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>ألياف البوليمر الدقيقة (Micro-Polymer Fibers):</strong> مقاومة للتمزق والتأكل وتضمن انزلاقاً املساً.</li>
  <li><strong>طبقة شمعية لطيفة (Gentle Wax Coating):</strong> تسهل دخول الخيط بين الأسنان الشديدة التقارب.</li>
  <li><strong>نكهة النعناع المنعشة:</strong> تمنح الفم إحساساً بالفخامة والانتعاش بعد كل استخدام.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الفموي الخارجي فقط.</li>
  <li>تجنبي إدخال الخيط بقوة مفرطة بين الأسنان لتجنب جرح اللثة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال دون سن 6 سنوات.</li>
  <li>تخلصي من الخيط المستعمل ولا تعيدي استخدامه.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحثون عن تنظيف فموي كامل وحماية لثتهم من الالتهابات والجير.</li>
  <li>لمستخدمي تقويم الأسنان والراغبين في إزالة بقايا الطعام الجانبية.</li>
  <li>مناسب للبالغين والأطفال فوق سن 6 سنوات.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>تيسي (Taisi)</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم / خيط الأسنان والعناية باللثة</td></tr>
  <tr><th>نوع المنتج</th><td>خيط تنظيف الأسنان وحماية اللثة (Taisi Dental Floss)</td></tr>
  <tr><th>الحجم/الوزن</th><td>عبوة خيط مدمجة</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بالفم والأسنان)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان نظيفة تماماً، لثة صحية ونفس منعش</td></tr>
  <tr><th>الملمس</th><td>خيط شمعي ناعم مقاوم للانقطاع</td></tr>
  <tr><th>العطر</th><td>نكهة النعناع المنعشة</td></tr>
  <tr><th>المكونات النشطة</th><td>ألياف بوليمر، طبقة شمعية، نكهة نعناع</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين / المملكة العربية السعودية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Taisi Oral Care</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والأطفال فوق 6 سنوات</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لأهمية خيط الأسنان وحماية اللثة (Taisi Care)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج خيط أسنان تيسي مشكلة تراكم بقايا الطعام والبكتيريا في الفراغات الضيقة بين الأسنان وتحت خط اللثة، والتي لا تصلها الفرشاة العادية وتتسبب في التسوس الجانبي ورائحة الفم.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تصل شعيرات فرشاة الأسنان إلى 60% فقط من أسطح الأسنان، وتترك 40% من الأسطح الجانبية الضيقة عرضة لتجمع البلاك والبكتيريا وتكلس الجير الجانبي.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام الخيط يومياً:</strong> استعملي خيط الأسنان مرة واحدة على الأقل يومياً قبل النوم.<br>
2. <strong>الحركة بحرف C:</strong> لفي الخيط حول جذر السن بحرف C لتنظيف الجوانب بالكامل.<br>
3. <strong>عدم الضغط القسري:</strong> أدخلي الخيط بحركة انزلاقية خفيفة لحماية اللثة من الجروح.<br>
4. <strong>استخدام جزء نظيف لكل سن:</strong> غيري مسافة الخيط بين الأسنان لتجنب نقل البكتيريا.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "استخدام خيط الأسنان يوسع الفراغات بين الأسنان."<br>
<strong>الحقيقة:</strong> خيط الأسنان ينظف البلاك الضار وينقذ اللثة من الانحسار والالتهابات دون تغيير المسافات الطبيعية للأسنان.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>ينزلق خيط تيسي الشمعي بسماكته الميكرونية داخل نقاط الاتصال الجانبية للأسنان (Interproximal Contacts)، حيث يزيل غشاء البيوفلم (Biofilm) والبكتيريا اللاهوائية قبل تحولها لأحماض تنقر مينا السن.</p>"""

    faqs = [
        ("ما هو خيط تنظيف الأسنان من تيسي؟", "هو خيط طبي شمعي مقاوم للانقطاع بنكهة النعناع ينزلق بين الأسنان لإزالة بقايا الطعام والبلاك وحماية اللثة."),
        ("لماذا يُعتبر خيط الأسنان مهماً بجانب الفرشاة؟", "لأن الفرشاة لا تصل إلى 40% من أسطح الأسنان الجانبية، بينما يزيل الخيط البلاك المكتنز بين الأسنان."),
        ("هل يسبب خيط تيسي نزيف اللثة؟", "لا، الخيط الشمعي الناعم ينزلق برفق؛ والنزيف الخفيف أول أيام الاستخدام دليل على وجود التهاب سابق يزول بالتنظيف المنتظم."),
        ("ما هي نكهة خيط أسنان تيسي؟", "يتميز بنكهة النعناع المنعشة التي تعطر الفم بالانتعاش."),
        ("هل ينقطع الخيط بسهولة أثناء الاستخدام؟", "لا، صُمم من ألياف دقيقة متينة مقاومة للتمزق والتفتت."),
        ("كيف أستخدم خيط الأسنان بالشكل الصحيح؟", "أدخلي الخيط بلطف بين الأسنان وانحني بحرف C واصعدي وانزلي ضد جدار السن ثم ابصقي الشوائب."),
        ("هل يناسب خيط تيسي مستخدمي تقويم الأسنان؟", "نعم، ممتاز لتنظيف الفراغات بين أسنان التقويم وحماية اللثة من التراكمات."),
        ("كم مرة يُنصح باستخدام خيط الأسنان يومياً؟", "يُنصح باستخدامه مرة واحدة يومياً على الأقل، خاصة قبل النوم."),
        ("هل يتسبب الخيط في توسيع المسافات بين الأسنان؟", "لا، الخيط رقيق جداً وينظف الترسبات دون التأثير على موقع الأسنان الطبيعي."),
        ("هل يناسب الأطفال؟", "مناسب للأطفال فوق سن 6 سنوات بمساعدة الوالدين لتعويدهم على العناية الفموية."),
        ("ما هو بلد صنع خيط أسنان تيسي؟", "تم تصنيعه وفق أعلى معايير الجودة للعناية بالفم والأسنان."),
        ("هل العبوة سهلة الحمل والسفر؟", "نعم، تأتي في عبوة مدمجة صغيرة مزودة بقاطعة خيط معدنية سهلة الاستخدام."),
        ("هل يحمي من تسوس الأسنان الجانبي؟", "نعم، إزالة التراكمات الجانبية يمنع التسوس النتوئي بين الأسنان."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع مستلزمات العناية بالفم لدى صيدلية إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يُستخدم الخيط قبل أم بعد تفريش الأسنان؟", "يُفضل استخدامه قبل التفريش لفتح الفراغات وسماح الفلورايد بالوصول لكافة الجوانب."),
        ("هل الخيط مغلف بطبقة شمعية؟", "نعم، مغلف بطبقة شمعية لطيفة تسلس الدخول بين الأسنان الشديدة التقارب."),
        ("هل يمنع تكون الجير الصلب؟", "نعم، يزيل البلاك قبل أن يتكلس بفعل لعاب الفم ويتحول لجير صلب."),
        ("ماذا أفعل إذا علق الخيط بين الأسنان؟", "اسحبيه بلطف للخارج من أحد الجوانب دون رفعه بقوة للأعلى."),
        ("هل يساعد في القضاء على رائحة الفم الصباحية؟", "نعم، تنظيف التراكمات قبل النوم يحد بشكل كبير من رائحة الفم الصباحية."),
        ("هل العبوة محكمة الحفظ؟", "نعم، تأتي في علبة بلاستيكية تحمي الخيط من الغبار والتلوث."),
        ("هل يحتاج الخيط لرج أو تحضير؟", "لا، جاهز للقطع والاستخدام المباشر."),
        ("هل يناسب الأسنان الملبسة أو التيجان؟", "نعم، ينظف حواف التيجان والتركيبات بأمان دون إتلافها."),
        ("كم مدة استخدام العبوة الواحدة؟", "تكفي العبوة لعدة أسابيع من الاستخدام اليومي المنتظم."),
        ("هل يمنع انحسار اللثة؟", "نعم، إزالة البلاكت المسبب لالتهاب اللثة يحميها من الانحسار والمخاطر."),
        ("هل يناسب جميع الأعمار؟", "مناسب لجميع الفئات العمرية من 6 سنوات فما فوق.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Taisi Dental Floss for Daily Care & Gum Protection</strong> is an essential oral hygiene tool designed to deliver deep interdental cleaning and superior gum protection. Crafted from flexible, shred-resistant micro-polymer fibers, this dental floss glides effortlessly between tight tooth spaces to reach areas that traditional toothbrushes cannot clean.</p>
<p>Taisi Dental Floss effectively removes trapped food debris and plaque beneath the gumline, preventing hard tartar buildup, interproximal cavities, and gum inflammation. Featuring a subtle mint flavor, it leaves your mouth feeling refreshed and completely clean when used in your daily oral care routine.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Deep Interdental Cleansing:</strong> Removes trapped food particles and plaque from tight spaces between teeth.</li>
  <li><strong>Shred-Resistant Flexible Fibers:</strong> Durable micro-fibers glide smoothly without snapping or fraying.</li>
  <li><strong>Gum Health & Protection:</strong> Reduces gum inflammation and bleeding caused by interdental plaque accumulation.</li>
  <li><strong>Cavity & Tartar Prevention:</strong> Prevents plaque calcification into hard tartar deposits between teeth.</li>
  <li><strong>Fresh Mint Breath:</strong> Neutralizes odor-causing oral bacteria with a long-lasting mint burst.</li>
  <li><strong>Compact Travel Container:</strong> Ultra-portable dispenser with built-in stainless steel thread cutter.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Dispense & Wrap):</strong> Cut approximately 45 cm of Taisi dental floss and wrap most of it around middle fingers of both hands.</li>
  <li><strong>Step 2 (Hold Securely):</strong> Hold floss tightly between thumbs and forefingers, leaving 3-5 cm of floss between hands.</li>
  <li><strong>Step 3 (Insert Gently):</strong> Gently guide floss between teeth using a gentle back-and-forth motion without snapping into gums.</li>
  <li><strong>Step 4 (Clean Side):</strong> Curve floss into a C-shape around the base of each tooth; slide gently up and down against tooth surface.</li>
  <li><strong>Step 5 (Repeat):</strong> Use a clean section of floss for every interdental space.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Micro-Polymer Fibers:</strong> High-tensile, shred-resistant fibers engineered for smooth gliding.</li>
  <li><strong>Gentle Wax Coating:</strong> Facilitates easy entry into tight contact points without force.</li>
  <li><strong>Refreshing Mint Flavor:</strong> Imparts a clean, invigorating mint sensation after every use.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For oral interdental flossing only.</li>
  <li>Do not force floss into tight contact points to prevent cutting gum tissue.</li>
  <li>Keep out of reach of children under 6 years of age.</li>
  <li>Dispose of used floss responsibly after single use.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking complete oral cleanliness and interdental gum protection.</li>
  <li>Orthodontic brace wearers wanting to clear food debris from tight teeth spaces.</li>
  <li>Suitable for adults and children over 6 years old.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Taisi</td></tr>
  <tr><th>Category</th><td>Oral Care / Dental Floss & Gum Care</td></tr>
  <tr><th>Product Type</th><td>Shred-Resistant Waxed Dental Floss</td></tr>
  <tr><th>Volume/Weight</th><td>Compact Floss Dispenser</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Oral Care)</td></tr>
  <tr><th>Finish</th><td>Clean teeth, healthy gums & fresh mint breath</td></tr>
  <tr><th>Texture</th><td>Smooth waxed shred-resistant thread</td></tr>
  <tr><th>Fragrance</th><td>Fresh Mint flavor</td></tr>
  <tr><th>Active Ingredients</th><td>Micro-Polymer Fibers, Wax Coating, Mint Flavor</td></tr>
  <tr><th>Country of Origin</th><td>China / Saudi Arabia</td></tr>
  <tr><th>Manufacturer</th><td>Taisi Oral Care</td></tr>
  <tr><th>Age Group</th><td>Adults & Children 6+</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Interdental Flossing & Gum Protection</h2>

<h3>What problem does this solve?</h3>
<p>Taisi Dental Floss resolves plaque buildup, interproximal tooth decay, and gum inflammation (gingivitis) occurring in tight tooth contact areas that toothbrushes cannot access.</p>

<h3>Why does this condition happen?</h3>
<p>Toothbrushes clean only 60% of tooth surfaces, leaving the remaining 40% of interdental surfaces vulnerable to bacterial biofilm accumulation and tartar calcification.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Floss Daily:</strong> Floss at least once daily, ideally before bedtime.<br>
2. <strong>C-Shape Technique:</strong> Curve floss in a C-shape around each tooth surface.<br>
3. <strong>Avoid Snapping:</strong> Guide floss gently to protect delicate gingival papillae.<br>
4. <strong>Clean Section per Tooth:</strong> Advance to a fresh floss section for each interdental space.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Dental flossing creates gaps between teeth."<br>
<strong>Fact:</strong> Dental floss removes damaging plaque, preserving natural gum attachments and preventing bone loss without altering tooth alignment.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Taisi's waxed micro-polymer thread glides past tight contact points, physically scraping anaerobic bacterial biofilm off interproximal enamel surfaces before bacteria convert sugars into enamel-eroding acids.</p>"""

    en_faqs = [
        ("What is Taisi Dental Floss?", "It is a shred-resistant waxed dental floss infused with mint flavor designed to clean interdental spaces and protect gums."),
        ("Why is flossing essential alongside brushing?", "Toothbrushes miss 40% of tooth surfaces between teeth where plaque accumulates."),
        ("Does Taisi floss cause gum bleeding?", "No, its waxed coating glides smoothly; initial light bleeding indicates mild existing inflammation that resolves with regular use."),
        ("What flavor does it have?", "It features an invigorating fresh mint flavor."),
        ("Does the floss shred during use?", "No, it is crafted from high-tensile micro-polymer fibers resistant to fraying."),
        ("How do I use dental floss correctly?", "Insert gently, curve into a C-shape around the tooth, and slide up and down before moving to the next space."),
        ("Is it safe for orthodontic braces?", "Yes, it effectively clears food debris around brackets and interdental wires."),
        ("How often should I floss?", "Floss at least once daily, preferably before bedtime."),
        ("Will flossing widen gaps between teeth?", "No, floss is ultra-thin and removes plaque without shifting natural tooth positions."),
        ("Is it suitable for children?", "Suitable for children over 6 years old with parental guidance."),
        ("Where is Taisi Dental Floss manufactured?", "It is manufactured under international oral care quality standards."),
        ("Is the dispenser travel-friendly?", "Yes, it comes in a compact plastic case with a built-in stainless steel cutter."),
        ("Does it prevent interdental cavities?", "Yes, removing interproximal plaque prevents side tooth decay."),
        ("How do I verify authenticity at Ekleel Abha?", "All oral care items at Ekleel Abha are 100% original from authorized distributors."),
        ("Should I floss before or after brushing?", "Flossing before brushing clears interdental spaces, allowing toothpaste fluoride deeper access."),
        ("Is the floss waxed?", "Yes, it features a smooth wax coating for easy insertion between tight teeth."),
        ("Does it prevent tartar formation?", "Yes, removing plaque before it calcifies prevents hard tartar buildup."),
        ("What if the floss gets stuck?", "Gently pull the floss sideways out of the contact point rather than forcing it upward."),
        ("Does it help reduce morning breath?", "Yes, removing trapped food and bacteria before sleep significantly reduces morning breath."),
        ("Is the dispenser dust-proof?", "Yes, it comes in a durable plastic case protecting the thread from contamination."),
        ("Does it require pre-washing?", "No, it is ready for immediate hygienic cutting and use."),
        ("Is it safe for dental crowns and veneers?", "Yes, it cleans around crown margins safely without dislodging restorations."),
        ("How long does one dispenser last?", "One dispenser lasts several weeks of daily flossing."),
        ("Does it help prevent gum recession?", "Yes, removing plaque prevents chronic gingivitis and gum recession."),
        ("Is it suitable for all ages?", "Suitable for adults and children aged 6+.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1739",
        "sku": "EK-1739",
        "gtin": "1005160028030",
        "category": "العناية بالفم / خيط الأسنان والعناية باللثة",
        "brand": "Taisi",
        "ar": {
            "title": "خيط تنظيف الأسنان من تيسي للعناية اليومية وحماية اللثة",
            "meta_title": "خيط تنظيف الأسنان تيسي | صيدلية إكليل أبها",
            "meta_description": "اشتري خيط تنظيف الأسنان من تيسي للعناية اليومية وحماية اللثة بالنعناع. خيط شمعي مقاوم للانقطاع لتنظيف عميق. أصلي من صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["تيسي", "خيط_اسنان", "حماية_اللثة", "نعناع", "إكليل_أبها"]
        },
        "en": {
            "title": "Tيسي Dental Floss",
            "meta_title": "Taisi Dental Floss for Daily Care & Gum Protection | Ekleel Abha",
            "meta_description": "Buy Taisi Dental Floss for Daily Care & Gum Protection with Mint flavor. Shred-resistant waxed thread for deep interdental care. 100% authentic at Ekleel Abha.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["taisi", "dental_floss", "gum_protection", "mint", "ekleel_abha"]
        },
        "schema": {
            "brand": "Taisi",
            "category": "Oral Care / Dental Floss",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "taisi-dental-floss-for-daily-care-and-gum-protection.webp",
            "alt": "Taisi Dental Floss for Daily Care & Gum Protection",
            "title": "Taisi Dental Floss for Daily Care & Gum Protection"
        }
    }

def create_product_1741():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعتبر <strong>عطر افلون بيش للجنسين من سن سيت كافيه (Sunset Cafe Avalon Peach Unisex Perfume - 100ml)</strong> واحداً من أكثر العطور انتعاشاً ولطفاً والمخصصة للأطفال والعائلة ككل. يجمع هذا العطر الفريد بين نفحات الخوخ الخوخي الزاخرة بالنعومة وعشق زهور الخوخ مع لمسة بودرية رقيقة تمنح إحساساً بالنظافة والدفء يدوم طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عطر زكي ولطيف للجنسين والأطفال:</strong> تركيب مائية لطيفة وآمنة تناسب الأطفال والنساء ولجميع العائلة.</li>
  <li><strong>عبير الخوخ الطبيعي المشرق:</strong> يمنح رائحة خوخ زكية ومفعمة بالحيوية والانتعاش.</li>
  <li><strong>لمسة بودرية زهرية ناعمة:</strong> تمنح شعوراً بالنظافة والدفء بعد الاستحمام.</li>
  <li><strong>تركيبة آمنة على البشرة الحساسة:</strong> خالية من المكونات الكيميائية القاسية ولا تسبب تهيج الجلد.</li>
  <li><strong>ثبات ممتاز وعبير منعش:</strong> يرافقكِ ويضفي بهجة على روتين العناية اليومي.</li>
  <li><strong>عبوة أنيقة سعة 100 مل:</strong> تصميم جذاب وعصري يسهل حمله واستخدامه يومياً.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> يُفضل رش العطر على جسم أو ملابس نظيفة بعد الاستحمام مباشرة.</li>
  <li><strong>الخطوة الثانية (الرش):</strong> رشي العطر من مسافة 15-20 سم على الملابس أو مناطق النبض (المعصمين والرقبة).</li>
  <li><strong>الخطوة الثالثة (الاستمتع):</strong> استمتعي برائحة الخوخ البودرية المنعشة طوال اليوم.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة الخوخ (Peach Blossom & Fruit Extract):</strong> تمنح العطر طابعه الزكي والمشرق.</li>
  <li><strong>لمسات الزهور البودرية:</strong> تضفي الدفء والنظافة.</li>
  <li><strong>قاعدة مائية لطيفة:</strong> تناسب البشرة الحساسة للأطفال.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي فقط.</li>
  <li>تجنبي رش العطر مباشرة على العينين أو الوجه.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال دون إشراف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>للأطفال والنساء والعائلات الراغبين في عطر خوخ بودري منعش ولطيف يومياً.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سن سيت كافيه (Sunset Cafe)</td></tr>
  <tr><th>الفئة</th><td>العطور / عطور الأطفال والعائلة</td></tr>
  <tr><th>نوع المنتج</th><td>عطر خوخ بودري لطيف للجنسين (Avalon Peach)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (الرش على الجسم والملابس)</td></tr>
  <tr><th>المظهر النهائي</th><td>رائحة خوخ ناعمة، بودرية، ومشرقة</td></tr>
  <tr><th>الملمس</th><td>سائل عطر رذاذ خفيف</td></tr>
  <tr><th>العطر</th><td>خوخ طبيعي ولهمسات بودرية زهرية</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة الخوخ، عطور زهرية بودرية، قاعدة مائية</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا / المملكة العربية السعودية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Sunset Cafe Perfumes</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الأعمار (خاصة الأطفال والنساء)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لخصائص عطور الخوخ واللمسات البودرية (Sunset Cafe)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يوفر عطر افلون بيش حلاً عطرياً آمناً ولطيفاً للأطفال والعائلة، يغني عن العطور الكحولية القاسية التي تسبب تحسس البشرة أو الروائح النفاذة المزعجة.</p>

<h3>لماذا يحدث تفضيل عطور الخوخ والبودرة؟</h3>
<p>لأنه يجمع بين الرائحة الفواحة الزكية للجمال والخوخ واللمسة البودرية التي تمنح إحساساً دائماً بالنظافة والدفء دون تهييج الجهاز التنفسي أو الجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الرش على الملابس النظيفة:</strong> رشي العطر على الملابس بعد الاستحمام لحبس العبير.<br>
2. <strong>التخزين الصحيح:</strong> احفظي العبوة بعيداً عن حرارة الشمس المباشرة للحفاظ على نضارة الخوخ.<br>
3. <strong>الاستخدام المعتدل:</strong> بضع رشات خفيفة تكفي لمنح عبق زكي يدوم طوال اليوم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "عطور الأطفال تسبب دائماً تصبغ الملابس."<br>
<strong>الحقيقة:</strong> عطر افلون بيش رذاذ نقي خالي من الصبغات الكيميائية التي تلطخ الأنسجة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتميز جزيئات الفواكه والزهور البودرية في العطر بوزن جزيئي خفيف يتبخر بتدرج ناعم عند ملامسة دفء الجسم أو الملابس، مما ينشر عبيراً الخوخ والدفء البودري بمرونة دون إحداث تهيج زهمي.</p>"""

    faqs = [
        ("ما هو عطر افلون بيش من سن سيت كافيه؟", "هو عطر لطيف برائحة الخوخ واللمسات البودرية سعة 100 مل، آمن ومخصص للأطفال والعائلة."),
        ("هل العطر مناسب للأطفال؟", "نعم، تركيبته الناعمة خالية من الكحول القاسي وتناسب بشرة وملابس الأطفال."),
        ("ما هي الرائحة الأساسية للعطر؟", "يتميز برائحة الخوخ الطبيعي المشرق الممزوجة بلمسات بودرية ناعمة."),
        ("ما حجم عبوة العطر؟", "تأتي العبوة بحجم 100 مل."),
        ("هل يثبت العطر على الملابس؟", "نعم، يمنح الملابس رائحة نظافة وانتعاش تدوم طوال اليوم."),
        ("هل يمكن استخدامه للجنسين؟", "نعم، هو عطر مبهج يناسب جميع الفئات والأجناس."),
        ("ما هو بلد صنع عطر سن سيت كافيه؟", "صُنع وفق أعلى معايير جودة العطور العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع عطور سن سيت كافيه لدى إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يسبب حساسية للجلد؟", "تركيبته لطيفة ومجربة جلدياً."),
        ("هل يمكن رشه على الجسم مباشرة؟", "نعم، يُفضل رشه من مسافة مناسبة على الجسم والملابس."),
        ("هل العبوة سهلة الحمل؟", "نعم، عبوة أنيقة ومريحة للاستخدام اليومي."),
        ("هل يناسب الاستخدام بعد الاستحمام؟", "نعم، يمنح شعوراً مضاعفاً بالنظافة والدفء بعد الاستحمام."),
        ("هل يحتوي على زيوت ثقيلة؟", "لا، هو عطر رذاذ خفيف غير زيتي."),
        ("ما هي الفئة العمرية المناسبة؟", "مناسب لجميع الأعمار من الأطفال حتى الكبار."),
        ("هل العبوة قابلة للإغلاق؟", "نعم، تأتي بغطاء محكم يمنع التسرب."),
        ("هل يترك أثراً على الملابس البيضاء؟", "لا، رذاذ شفاف خالي من الصبغات."),
        ("ما هي أفضل طريقة لزيادة الثبات؟", "رشه على ملابس قطنية وعلى مناطق النبض."),
        ("هل يصلح كهدية للأطفال؟", "نعم، خيار ممتاز وأنيق كهدية للأطفال والعائلات."),
        ("هل يغير رائحته مع الوقت؟", "يحافظ على عبق الخوخ واللمسة البودرية بثبات صافٍ."),
        ("هل يناسب فصل الصيف؟", "ممتاز جداً للصيف لأنه يمنح انتعاشاً ونظافة دائمة."),
        ("هل يناسب الأطفال الرضع؟", "يُفضل رشه على ملابس الرضيع الخارجية دون بشرته مباشرة."),
        ("هل يحتوي على بارابين؟", "خالي من المواد الضارة والبارابين."),
        ("كيف أحفظ العبوه؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل له نكهة خوخ طبيعية؟", "نعم، عبيره يعكس رائحة الخوخ الطبيعي الطازج."),
        ("هل العطر معتمد ومجرب؟", "نعم، معتمد ومجرب وفق أعلى معايير الأمان.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Sunset Cafe Avalon Peach Unisex Perfume (100ml)</strong> is a fresh, gentle, and enchanting fragrance tailored for kids, teens, and the whole family. Fusing vibrant juicy peach notes with soft powdery floral undertones, it delivers an instant sensation of warmth, cleanliness, and joy.</p>
<p>Formulated to be mild and gentle on sensitive skin, Sunset Cafe Avalon Peach comes in a generous 100ml bottle suitable for daily post-bath wear, leaving a delicate and memorable fruity trail throughout the day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Gentle Unisex Family Fragrance:</strong> Mild, safe formulation ideal for children, women, and everyday wear.</li>
  <li><strong>Juicy Natural Peach Aroma:</strong> Delivers vibrant, sweet peach fruit and blossom top notes.</li>
  <li><strong>Soft Powdery Floral Finish:</strong> Imparts a clean, warm, post-bath scent impression.</li>
  <li><strong>Safe for Sensitive Skin:</strong> Free of harsh chemicals, gentle on delicate skin and clothing.</li>
  <li><strong>Long-Lasting Freshness:</strong> Keeps clothes and skin delicately scented all day.</li>
  <li><strong>Elegant 100ml Bottle:</strong> Portable, stylish dispenser perfect for daily application.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Apply onto clean skin or fresh clothing after bathing.</li>
  <li><strong>Step 2 (Spray):</strong> Hold bottle 15-20 cm away and mist onto clothes or pulse points (wrists, neck).</li>
  <li><strong>Step 3 (Enjoy):</strong> Enjoy the refreshing powdery peach aroma throughout the day.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Peach Fruit & Blossom Essence:</strong> Provides vibrant, sweet, natural peach fragrance notes.</li>
  <li><strong>Powdery Floral Accents:</strong> Deliver a soft, clean, comforting aroma.</li>
  <li><strong>Mild Aqueous Solvent Base:</strong> Gentle on child-sensitive skin.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application only.</li>
  <li>Avoid spraying directly into eyes or face.</li>
  <li>Keep out of reach of young children without adult supervision.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Families, kids, and individuals seeking a light, gentle, powdery peach daily fragrance.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Sunset Cafe</td></tr>
  <tr><th>Category</th><td>Fragrance / Kids & Family Perfumes</td></tr>
  <tr><th>Product Type</th><td>Unisex Soft Powdery Peach Eau de Parfum / Mist</td></tr>
  <tr><th>Volume/Weight</th><td>100 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Body & Clothing Mist)</td></tr>
  <tr><th>Finish</th><td>Fresh, soft, powdery peach fragrance</td></tr>
  <tr><th>Texture</th><td>Light liquid mist spray</td></tr>
  <tr><th>Fragrance</th><td>Natural Peach & Soft Floral Powder notes</td></tr>
  <tr><th>Active Ingredients</th><td>Peach Essence, Powdery Floral Notes, Mild Water Base</td></tr>
  <tr><th>Country of Origin</th><td>France / Saudi Arabia</td></tr>
  <tr><th>Manufacturer</th><td>Sunset Cafe Perfumes</td></tr>
  <tr><th>Age Group</th><td>All Ages (Kids & Adults)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Gentle Fruit Essences & Family Fragrances</h2>

<h3>What problem does this solve?</h3>
<p>Sunset Cafe Avalon Peach Perfume solves the issue of harsh alcohol-heavy perfumes that cause respiratory discomfort or skin irritation in children and sensitive individuals.</p>

<h3>Why choose Avalon Peach?</h3>
<p>Its delicate blend of sweet peach blossoms and soft powdery accents provides an invigorating scent of cleanliness without overwhelming sensitive olfactory senses.</p>"""

    en_faqs = [
        ("What is Sunset Cafe Avalon Peach Perfume?", "It is a gentle 100ml unisex fragrance featuring juicy peach and soft powdery notes suitable for kids and family daily wear."),
        ("Is it safe for children?", "Yes, its mild formulation is safe for children's clothing and sensitive skin."),
        ("What are the primary fragrance notes?", "It features natural juicy peach, peach blossom, and a clean powdery floral finish."),
        ("What volume is contained in this bottle?", "It comes in a 100ml glass bottle."),
        ("Does it stay fresh on clothes?", "Yes, it provides a clean, comforting scent that lasts throughout the day."),
        ("Can both boys and girls wear it?", "Yes, it is a universal, fresh unisex fragrance."),
        ("Where is Sunset Cafe manufactured?", "It is produced following global fine fragrance safety standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Sunset Cafe perfumes at Ekleel Abha are 100% genuine from certified distributors."),
        ("Does it cause skin allergies?", "No, its mild formulation is dermatologically safe."),
        ("Can it be sprayed directly on skin?", "Yes, spray onto clothing or pulse points from a safe distance."),
        ("Is the bottle travel-friendly?", "Yes, its compact 100ml size is convenient for daily use."),
        ("Is it suitable after bathing?", "Yes, it enhances post-bath cleanliness and freshness."),
        ("Does it contain heavy oils?", "No, it is a light, non-greasy liquid mist."),
        ("What age group is it for?", "Suitable for all age groups, especially kids and women."),
        ("Does the cap seal securely?", "Yes, it features a tight protective cap."),
        ("Does it stain white clothing?", "No, the clear liquid mist leaves zero stains on white fabrics."),
        ("How to maximize fragrance longevity?", "Spray onto clean cotton fabrics and pulse points."),
        ("Does it make a good gift for children?", "Yes, it is a popular and charming gift choice for kids."),
        ("Does the scent alter over time?", "It maintains a consistent peach and clean powdery aroma."),
        ("Is it suitable for summer?", "Yes, its fresh peach notes are ideal for warm weather."),
        ("Can it be used on infants?", "Spray onto outer baby clothing rather than direct infant skin."),
        ("Is it paraben-free?", "Yes, free from harsh chemical additives."),
        ("How should I store the bottle?", "Store in a cool, dry place away from sunlight."),
        ("Does it smell like fresh peach?", "Yes, it authentically mirrors fresh juicy peaches."),
        ("Is it safety-tested?", "Yes, dermatologically safety-tested for family use.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1741",
        "sku": "EK-1741",
        "gtin": "788119003005",
        "category": "العطور / عطور الأطفال والعائلة",
        "brand": "Sunset Cafe",
        "ar": {
            "title": "عطر افلون بيش للجنسين من سن سيت كافيه 100مل",
            "meta_title": "عطر سن سيت كافيه افلون بيش 100مل | صيدلية إكليل أبها",
            "meta_description": "اشتري عطر افلون بيش للجنسين من سن سيت كافيه (100مل). عبق الخوخ اللطيف واللمسة البودرية للأطفال والعائلة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["سن_سيت_كافيه", "افلون_بيش", "عطر_خوخ", "عطر_اطفال", "إكليل_أبها"]
        },
        "en": {
            "title": "Sunset Cafe Avalon Peach Unisex Perfume - 100ml",
            "meta_title": "Sunset Cafe Avalon Peach Perfume 100ml | Ekleel Abha",
            "meta_description": "Buy Sunset Cafe Avalon Peach Unisex Perfume (100ml). Gentle powdery peach scent for kids & family. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["sunset_cafe", "avalon_peach", "peach_perfume", "kids_perfume", "ekleel_abha"]
        },
        "schema": {
            "brand": "Sunset Cafe",
            "category": "Fragrance / Perfume",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "sunset-cafe-avalon-peach-unisex-perfume-100ml.webp",
            "alt": "Sunset Cafe Avalon Peach Unisex Perfume 100ml",
            "title": "Sunset Cafe Avalon Peach Unisex Perfume 100ml"
        }
    }

def create_product_1742():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعتبر <strong>زيت اللوز الحلو النقي من وادي النحل للشعر والبشرة (Wadi Al-Nahl Sweet Almond Oil - 125 ml)</strong> واحداً من أكثر الزيوت الطبيعية شهرة ونقاءً للعناية الشاملة بالجمال والصحة. يعتمد هذا الزيت من علامة وادي النحل الشهيرة على اعتصار ثمار اللوز الحلو النقي 100%، مما يزود ألياف الشعر وخلايا البشرة بوجبة غذائية مكثفة غنية بفيتامين E، المغنيسيوم، والأحماض الدهنية الأساسية (أوميغا 9).</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>زيت لوز حلو نقي 100%:</strong> خالي من الإضافات الكيميائية والعطور والمواد الحافظة.</li>
  <li><strong>ترطيب وتغذية فائقة للبشرة:</strong> يغذي البشرة الجافة، يعالج التشققات، ويقلل مظهر الهالات السوداء.</li>
  <li><strong>تقوية وتنعيم ألياف الشعر:</strong> يقلل تقصف الشعر، يغذي البصيلات، ويزيد اللمعان والمرونة.</li>
  <li><strong>مكافحة الأكسدة والتجاعيد:</strong> غني بفيتامين E الذي يحمي الخلايا من الشيخوخة والجذور الحرة.</li>
  <li><strong>تهدئة الفروة والجلد:</strong> يهدئ التهابات الجلد والجفاف الخفيف الناتجة عن الشمس.</li>
  <li><strong>عبوة زجاجية 125 مل:</strong> محكمة الغلق تحافظ على قيمة ونقاء الزيت الطبيعي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (للبشرة):</strong> وضعي قطرات من الزيت على بشرة نظيفة ودلكي بلطف قبل النوم.</li>
  <li><strong>الخطوة الثانية (للشعر):</strong> دلكي الزيت على الفروة والخصلات كحمام زيت مهدئ لمدة ساعة ثم اغسليه.</li>
  <li><strong>الخطوة الثالثة (للهالات والشفاه):</strong> مرري قطرة خفيفة تحت العينين وعلى الشفاه ليلاً.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت اللوز الحلو النقي 100% (Prunus Amygdalus Dulcis Oil):</strong> غني بفيتامين E، D، A، والمغنيسيوم وأوميغا 9.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي فقط.</li>
  <li>يُفضل إجراء اختبار حساسية بسيط لمن يعانون من حساسية المكسرات.</li>
  <li>يُحفظ بعيداً عن حرارة الشمس في مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن زيت طبيعي نقي 100% للعناية بالبشرة والشعر والهالات السوداء.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>وادي النحل (Wadi Al-Nahl)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة والشعر / الزيوت الطبيعية</td></tr>
  <tr><th>نوع المنتج</th><td>زيت اللوز الحلو النقي 100% (125 مل)</td></tr>
  <tr><th>الحجم/الوزن</th><td>125 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة والشعر</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة مرطبة، شعر ناعم ومشرق ببريق صحي</td></tr>
  <tr><th>الملمس</th><td>زيت نقي خفيف الامتصاص</td></tr>
  <tr><th>العطر</th><td>عطر اللوز الطبيعي الخفيف جداً</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت اللوز الحلو 100%، فيتامين E، مغنيسيوم، أوميغا 9</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Wadi Al-Nahl Company</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت اللوز الحلو النقي (Wadi Al-Nahl)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج زيت اللوز الحلو من وادي النحل مشكلة جفاف البشرة، الهالات السوداء تحت العين، تقصف أطراف الشعر، وجفاف الشفاه دون استخدام كيماويات صناعية.</p>

<h3>لماذا تحدث هذه المشكلات؟</h3>
<p>لأن التعرض للشمس والغسيل التكراري يسرق الأحماض الدهنية وفيتامين E من غشاء الجلد والشعر، مما يسبب الجفاف وتشقق الشفاه وظهور التصبغات.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطريق اليومي للبشرة:</strong> وضعي قطرات خفيفة قبل النوم لترطيب الوجه والهالات.<br>
2. <strong>حمام زيت للشعر:</strong> دلكي الفروة والأطراف قبل الشامبو بساعة لتقوية البصيلات.<br>
3. <strong>العناية بالأظافر:</strong> مرري الزيت حول الجلد المحيط بالأظافر لمنع التكسر.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "زيت اللوز الحلو يسد مسام الوجه ويسبب الحبوب."<br>
<strong>الحقيقة:</strong> زيت اللوز الحلو يمتاز بمعدل كوميدوجينيك منخفض جداً ويمتصه الجلد بسرعة دون سد المسام.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يتألف الزيت من 100% أحماض أوليك ولينوليك وفيتامين E التي تنفذ بين الخلايا القرنية، حيث تعمل على ترطيب غشاء الجلد وتدعيم بناء الكولاجين ومنع أكسدة صبغة الميلانين تحت العينين.</p>"""

    faqs = [
        ("ما هو زيت اللوز الحلو من وادي النحل؟", "هو زيت طبيعي نقي 100% مستخلص من اللوز الحلو للعناية بالشعر والبشرة والهالات السوداء سعة 125 مل."),
        ("ما هي فوائد زيت اللوز الحلو للبشرة؟", "يرطب البشرة، يقلل التصبغات والهالات السوداء، يحمي من التجاعيد، ويزيد مرونة الجلد."),
        ("ما هي فوائد زيت اللوز الحلو للشعر؟", "يغذي البصيلات، ينعم الشعر، يقلل تقصف الأطراف، ويحفز النمو بفضل المغنيسيوم."),
        ("ما حجم عبوة زيت وادي النحل؟", "تأتي العبوة بحجم 125 مل."),
        ("هل يمكن استخدامه للهالات السوداء تحت العين؟", "نعم، وضع قطرة خفيفة ليلاً يساعد في تفتيح وترطيب منطقة تحت العينين."),
        ("هل يناسب جميع أنواع البشرة والشعر؟", "نعم، هو زيت خفيف ونقي يناسب جميع الأنواع."),
        ("هل يحتوي على أي مضافات كيميائية؟", "لا، هو نقي 100% خالي من العطور والمواد الكيميائية."),
        ("كيف يُستخدم للشعر كحمام زيت؟", "دلكي الزيت على الفروة والأطراف واتركيه ساعة ثم اغسليه بالشامبو."),
        ("ما هو بلد صنع زيت وادي النحل؟", "صُنع بفخر في المملكة العربية السعودية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع زيوت وادي النحل لدى إكليل أبها أصلية 100% ومستوردة من الشركة مباشرة."),
        ("هل يسبب حساسية لمن لديهم حساسية مكسرات؟", "يُفضل إجراء اختبار تحسس بسيط لمن لديهم حساسية مثبتة للمكسرات."),
        ("هل يمكن استخدامه كمزيل مكياج؟", "نعم، يذوب المكياج بفعالية ويرطب البشرة."),
        ("هل يساعد في ترطيب الشفاه المتشققة؟", "نعم، ممتاز لترطيب الشفاه وتنعيمها."),
        ("هل يناسب الأطفال والرضع؟", "نعم، آمن ونقي لترطيب بشرة الأطفال."),
        ("هل يحتاج للحفظ في الثلاجة؟", "يُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل يترك ملمساً ثقيلاً على الوجه؟", "لا، هو زيت خفيف الامتصاص بمرونة."),
        ("كم مرة يُنصح باستخدامه؟", "يمكن استخدامه يومياً للبشرة أو 2-3 مرات أسبوعياً للشعر."),
        ("هل يساعد في تقليل علامات التمدد؟", "نعم، يفرز مرونة للجلد ويقلل التمدد لدى الحوامل."),
        ("هل يصلح لتدليك الجسم؟", "نعم، ممتاز كزيت مساج طبيعي مهدئ."),
        ("هل العبوة زجاجية محكمة؟", "نعم، تحفظ نقاء الزيت من التأكسد."),
        ("هل يغير لون الشعر؟", "لا، لا يؤثر على لون الشعر الطبيعي أو المسبوغ."),
        ("هل يساعد في محاربة القشرة؟", "نعم، ترطيب الفروة يقلل جفاف القشرة."),
        ("هل يناسب كبار السن؟", "نعم، يغذي البشرة الناضجة ويمنع الجفاف."),
        ("هل يمكن خلطه مع زيوت أخرى؟", "نعم، يمكن دمج قطرات منه مع زيت الأرجان أو الخروع."),
        ("هل العبوة 125 مل اقتصادية؟", "نعم، تكفي لأشهر من الاستخدام المزدوج.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Wadi Al-Nahl Sweet Almond Oil (125 ml)</strong> is a 100% pure natural oil designed for comprehensive hair, skin, and under-eye care. Cold-pressed from pure sweet almonds, this trusted oil from Wadi Al-Nahl delivers a nutrient-rich blend of Vitamin E, Vitamin D, Magnesium, and essential Omega-9 fatty acids.</p>
<p>Extremely versatile, it deeply moisturizes dry skin, reduces the appearance of dark under-eye circles, smooths fine lines, and restores shine and strength to damaged, split hair strands.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Pure Sweet Almond Oil:</strong> Completely free of chemical additives, fragrances, and preservatives.</li>
  <li><strong>Intensive Skin Hydration:</strong> Nourishes dry skin, reduces under-eye dark circles, and improves elasticity.</li>
  <li><strong>Hair Fiber Strengthening:</strong> Reduces split ends, nourishes roots, and boosts silky hair shine.</li>
  <li><strong>Antioxidant Anti-Aging Shield:</strong> Rich in Vitamin E to protect cells from free radical damage.</li>
  <li><strong>Soothes Scalp & Skin Irritation:</strong> Calms dry scalp flaking and mild sun exposure dryness.</li>
  <li><strong>Sealed 125ml Bottle:</strong> Preserves oil purity and nutrient potency.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Skin):</strong> Apply a few drops onto clean skin and massage gently before sleep.</li>
  <li><strong>Step 2 (Hair):</strong> Massage oil into scalp and strands as a 1-hour oil treatment before shampooing.</li>
  <li><strong>Step 3 (Under-Eyes & Lips):</strong> Pat a light drop under eyes and on chapped lips nightly.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>100% Pure Sweet Almond Oil (Prunus Amygdalus Dulcis):</strong> Rich in Vitamin E, Magnesium, and Omega-9 fatty acids.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic use only.</li>
  <li>Perform a patch test if you have known nut allergies.</li>
  <li>Store in a cool, dry place away from direct heat and sunlight.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a 100% pure natural oil for skin hydration, dark circle reduction, and hair conditioning.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Wadi Al-Nahl</td></tr>
  <tr><th>Category</th><td>Skincare & Haircare / Natural Oils</td></tr>
  <tr><th>Product Type</th><td>100% Pure Sweet Almond Oil</td></tr>
  <tr><th>Volume/Weight</th><td>125 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin & Hair Types</td></tr>
  <tr><th>Finish</th><td>Hydrated skin, shiny soft hair, nourished dark circles</td></tr>
  <tr><th>Texture</th><td>Pure lightweight absorbing natural oil</td></tr>
  <tr><th>Fragrance</th><td>Subtle natural sweet almond aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Sweet Almond Oil 100%, Vitamin E, Magnesium, Omega-9</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia</td></tr>
  <tr><th>Manufacturer</th><td>Wadi Al-Nahl Company</td></tr>
  <tr><th>Age Group</th><td>All Ages</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Sweet Almond Oil & Skin Lipid Replenishment</h2>

<h3>What problem does this solve?</h3>
<p>Wadi Al-Nahl Sweet Almond Oil resolves skin dryness, dark under-eye circles, split ends, and dry lips without synthetic chemicals.</p>

<h3>Why choose Sweet Almond Oil?</h3>
<p>Rich in oleic acid and Vitamin E, it penetrates skin and hair fibers rapidly, sealing cuticles and restoring cellular elasticity.</p>"""

    en_faqs = [
        ("What is Wadi Al-Nahl Sweet Almond Oil?", "It is a 100% pure natural oil extracted from sweet almonds for hair, skin, and under-eye care."),
        ("What are its skin benefits?", "It hydrates dry skin, lightens under-eye dark circles, and reduces fine lines."),
        ("What are its hair benefits?", "It nourishes roots, smooths hair fibers, and reduces split end breakage."),
        ("What volume is contained in this bottle?", "It comes in a 125ml bottle."),
        ("Can it be used for under-eye dark circles?", "Yes, patting a light drop nightly helps hydrate and lighten dark circles."),
        ("Is it suitable for all skin and hair types?", "Yes, it is a lightweight, pure oil suitable for all types."),
        ("Does it contain synthetic additives?", "No, it is 100% pure without additives or perfumes."),
        ("How do I use it as a hair oil treatment?", "Massage into scalp and strands, leave for 1 hour, then shampoo thoroughly."),
        ("Where is Wadi Al-Nahl oil manufactured?", "It is proudly produced in Saudi Arabia."),
        ("How do I verify authenticity at Ekleel Abha?", "All Wadi Al-Nahl oils at Ekleel Abha are 100% original from certified distributors."),
        ("Should people with nut allergies perform a test?", "Yes, perform a patch test if you have known nut allergies."),
        ("Can it be used as a makeup remover?", "Yes, it dissolves makeup effectively while hydrating skin."),
        ("Does it heal chapped lips?", "Yes, it deeply hydrates and softens chapped lips."),
        ("Is it safe for infants?", "Yes, pure sweet almond oil is safe for moisturizing baby skin."),
        ("Does it require refrigeration?", "Store in a cool, dry place away from heat."),
        ("Is it heavy on the face?", "No, it absorbs smoothly without feeling overly greasy."),
        ("How often should I use it?", "Use daily for skin or 2-3 times weekly for hair treatments."),
        ("Does it help reduce stretch marks?", "Yes, it enhances skin elasticity during pregnancy."),
        ("Can it be used for body massage?", "Yes, it serves as an excellent natural massage oil."),
        ("Is the bottle glass-sealed?", "Yes, it comes in a sealed bottle protecting oil quality."),
        ("Does it affect hair color?", "No, it does not alter natural or dyed hair color."),
        ("Does it help reduce dry dandruff?", "Yes, hydrating scalp dryness reduces flaking."),
        ("Is it suitable for mature skin?", "Yes, it nourishes mature skin and protects against aging."),
        ("Can it be mixed with other natural oils?", "Yes, it blends well with Argan or Castor oil."),
        ("Is the 125ml bottle economical?", "Yes, it provides months of multi-purpose daily usage.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1742",
        "sku": "EK-1742",
        "gtin": "1400300200077",
        "category": "العناية بالبشرة والشعر / الزيوت الطبيعية",
        "brand": "Wadi Al-Nahl",
        "ar": {
            "title": "زيت اللوز الحلو النقي من وادي النحل للشعر والبشرة - 125 مل",
            "meta_title": "زيت اللوز الحلو وادي النحل 125مل | صيدلية إكليل أبها",
            "meta_description": "اشتري زيت اللوز الحلو النقي 100% من وادي النحل للشعر والبشرة والهالات السوداء (125مل). أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["وادي_النحل", "زيت_اللوز_الحلو", "عناية_بالبشرة", "عناية_بالشعر", "إكليل_أبها"]
        },
        "en": {
            "title": "Wadi Al-Nahl Sweet Almond Oil - 125 ml",
            "meta_title": "Wadi Al-Nahl Sweet Almond Oil 125ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy 100% Pure Wadi Al-Nahl Sweet Almond Oil (125ml) for hair, skin, & dark circles. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["wadi_al_nahl", "sweet_almond_oil", "skincare", "haircare", "ekleel_abha"]
        },
        "schema": {
            "brand": "Wadi Al-Nahl",
            "category": "Skincare / Natural Oil",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "wadi-al-nahl-sweet-almond-oil-125ml.webp",
            "alt": "Wadi Al-Nahl Sweet Almond Oil 125ml",
            "title": "Wadi Al-Nahl Sweet Almond Oil 125ml"
        }
    }

print("Loaded 1739, 1741, 1742 builders")
