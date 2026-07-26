import json, os

def create_product_1902():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مزيل شعر الحواجب مطلي بالذهب من فلوليس (Flawless Gold-Plated Eyebrow Hair Remover)</strong> جهاز إزالة شعر الحواجب الفاخر الأول من نوعه بطلاء ذهبي أصيل 18 قيراطاً. يجمع هذا الجهاز الأنيق (Flawless Gold-Plated Eyebrow Hair Remover) بين تقنية الشفرة الدوارة الدقيقة المطلية بالذهب (Micro-Rotation Gold-Plated Blade) والقدرة على إزالة الشعر الدقيق بدقة متناهية دون ألم، حرق كيميائي، أو تهيج.</p>
<p>يعمل جهاز فلوليس المطلي بالذهب على إزالة الشعر الزائد بدقة من منطقة الحواجب والوجه، تشكيل وتحديد الحواجب بشكل احترافي، والعناية بالبشرة المحيطة بلطف شديد دون أي تهيج، ليترك حواجبك محددة ومثالية الشكل ووجهك ناعماً كالحرير.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>إزالة الشعر الدقيق بلا ألم بشفرة دوارة مطلية بالذهب 18 قيراطاً:</strong> دقة احترافية في إزالة الشعر الزائد.</li>
  <li><strong>تشكيل احترافي للحواجب والمناطق الدقيقة:</strong> حواجب مثالية بسهولة تامة في المنزل.</li>
  <li><strong>خالٍ تماماً من الألم والتهيج والحرق الكيميائي:</strong> آمن للبشرة الحساسة حول الحواجب.</li>
  <li><strong>تصميم ذهبي فاخر أنيق وعملي:</strong> حجم مدمج مناسب للاستخدام اليومي والسفر.</li>
  <li><strong>يعمل بالبطارية:</strong> سهل الاستخدام في أي وقت ومكان.</li>
  <li><strong>متعدد الاستخدامات:</strong> مناسب لإزالة الشعر الدقيق من الحواجب، الشارب الخفيف، وخطوط الجبهة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> تأكدي من نظافة منطقة الحواجب وجفافها تماماً.</li>
  <li><strong>الخطوة الثانية (التشغيل):</strong> اضغطي على الزر لتشغيل الجهاز.</li>
  <li><strong>الخطوة الثالثة (الإزالة):</strong> مرري الجهاز برفق على الشعر الزائد بحركات خفيفة دائرية لإزالة الشعر بدقة.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>شفرة دوارة مطلية بالذهب 18 قيراطاً:</strong> تزيل الشعر الدقيق بدقة عالية وبدون ألم.</li>
  <li><strong>هيكل مريح مانع للانزلاق:</strong> تصميم مريح وسهل الإمساك لدقة في الإزالة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>لإزالة الشعر الدقيق من الوجه والحواجب فقط.</li>
  <li>لا تُستخدم على الجلد المصاب أو البشرة المتهيجة أو المحروقة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تبحث عن جهاز فلوليس المطلي بالذهب لتشكيل الحواجب واحتراف إزالة الشعر الدقيق بلا ألم.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>فلوليس (Flawless)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / أجهزة إزالة شعر الحواجب الفاخرة المطلية بالذهب</td></tr>
  <tr><th>نوع المنتج</th><td>جهاز فاخر لإزالة شعر الحواجب والوجه الدقيق بشفرة دوارة مطلية بالذهب 18 قيراطاً</td></tr>
  <tr><th>الحجم/الوزن</th><td>حجم مدمج للاستخدام اليومي والسفر</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (بما في ذلك البشرة الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>حواجب محددة مثالية، وجه ناعم خالٍ من الشعر الزائد الدقيق</td></tr>
  <tr><th>الملمس</th><td>جهاز مريح الإمساك بهيكل مانع للانزلاق</td></tr>
  <tr><th>العطر</th><td>لا ينطبق</td></tr>
  <tr><th>المكونات النشطة</th><td>شفرة دوارة مطلية بالذهب 18 قيراطاً، محرك دقيق هادئ</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة الأمريكية (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Finishing Touch Flawless</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد تقنية الشفرة الدوارة المطلية بالذهب في جهاز فلوليس (Flawless)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج جهاز فلوليس المطلي بالذهب مشكلة الشعر الزائد الدقيق حول الحواجب والوجه وصعوبة التشكيل الدقيق في المنزل.</p>

<h3>لماذا تنجح تقنية الشفرة الدوارة المطلية بالذهب؟</h3>
<p>لأن طلاء الذهب يقلل الاحتكاك ويمنع حساسية الجلد، بينما تدور الشفرة بسرعة محددة تقطع الشعر بدقة دون ألم أو تهيج.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام على جلد جاف نظيف:</strong> للحصول على أفضل نتائج إزالة الشعر.<br>
2. <strong>الحركة الدائرية الخفيفة:</strong> تضمن إزالة كاملة لأدق الشعرات.<br>
3. <strong>التنظيف بعد الاستخدام:</strong> نظف رأس الجهاز بعد كل جلسة لضمان الدقة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "أجهزة إزالة الشعر الكهربائية تزيد سماكة الشعر."<br>
<strong>الحقيقة:</strong> الجهاز يقطع الشعر من السطح فقط دون تأثير على الجريب، مما يعني عدم تغيير سُمك الشعر.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تعمل الشفرة الدوارة بمبدأ القطع الموازي للجلد مما يضمن قطع الشعر من قاعدته السطحية دون لمس الجلد أو إحداث جروح.</p>"""

    faqs = [
        ("ما هو مزيل شعر الحواجب مطلي بالذهب من فلوليس؟", "هو جهاز احترافي فاخر مطلي بالذهب 18 قيراطاً من فلوليس لإزالة شعر الحواجب والوجه الدقيق بدون ألم."),
        ("ما هي فوائد الشفرة المطلية بالذهب؟", "طلاء الذهب يقلل الاحتكاك ويمنع التهيج ويمنح دقة احترافية في إزالة الشعر الدقيق."),
        ("هل يزيل الشعر بدون ألم؟", "نعم، تقنية الشفرة الدوارة تزيل الشعر بدقة ودون ألم أو حرق كيميائي."),
        ("هل يناسب تشكيل الحواجب؟", "نعم، مصمم خصيصاً لتشكيل وتحديد الحواجب بدقة احترافية."),
        ("كيف يُستخدم الجهاز؟", "شغلي الجهاز ومرريه برفق على الشعر الزائد بحركات دائرية على جلد جاف نظيف."),
        ("هل يناسب البشرة الحساسة؟", "نعم، آمن للبشرة الحساسة حول منطقة الحواجب والوجه."),
        ("ما هو بلد صنع جهاز فلوليس؟", "صُنع في الولايات المتحدة الأمريكية بواسطة Finishing Touch Flawless."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات فلوليس لدى إكليل أبها أصلية 100%."),
        ("هل هو صامت في الاستخدام؟", "نعم، يعمل بمحرك هادئ دقيق."),
        ("هل الحجم مناسب للسفر؟", "نعم، حجم مدمج مثالي للسفر والاستخدام في أي مكان."),
        ("هل يزيل شعر الشارب الخفيف؟", "نعم، مناسب لإزالة الشعر الدقيق من الشارب وخطوط الجبهة."),
        ("ما مصدر الطاقة؟", "يعمل بالبطارية لسهولة الاستخدام في أي وقت."),
        ("كيف أنظف الجهاز؟", "نظف رأس الجهاز بالفرشاة المرفقة أو قطعة قماش ناعمة بعد الاستخدام."),
        ("هل يناسب المبتدئين في تشكيل الحواجب؟", "نعم، سهل الاستخدام للمبتدئين والمحترفات على حد سواء."),
        ("هل التصميم الذهبي يعكس الفخامة؟", "نعم، تصميم ذهبي فاخر أنيق."),
        ("هل يؤثر على سُمك الشعر؟", "لا، يقطع الشعر من السطح دون التأثير على الجريب أو سُمك الشعر."),
        ("هل يُستخدم بشكل يومي؟", "نعم، آمن للاستخدام اليومي."),
        ("هل يناسب النساء والرجال؟", "نعم، مناسب لكليهما لإزالة الشعر الدقيق من الوجه."),
        ("هل ورد ذكر فلوليس في وسائل الإعلام؟", "نعم، فلوليس علامة عالمية شهيرة في أجهزة إزالة الشعر."),
        ("هل يمنع الاحمرار بعد الإزالة؟", "نعم، طلاء الذهب يمنع التهيج والاحمرار بعد الاستخدام."),
        ("هل يمكن استخدامه أكثر من مرة؟", "نعم، قابل لإعادة الاستخدام المتكرر."),
        ("هل يناسب إزالة الشعر حول منطقة الشفاه؟", "نعم، مناسب لإزالة الشعر الدقيق حول الشفاه."),
        ("هل الشفرة قابلة للاستبدال؟", "يُنصح بمراجعة المواصفات للتحقق من إمكانية استبدال الرأس."),
        ("هل يصلح هدية فاخرة؟", "نعم، هدية أنيقة وعملية ومميزة لكل من تهتم بالعناية بالحواجب."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Flawless Gold-Plated Eyebrow Hair Remover</strong> is the world's first luxury eyebrow hair removal device with an authentic 18-karat gold-plated micro-rotation blade. It combines the Micro-Rotation Gold-Plated Blade technology with pinpoint precision hair removal without pain, chemical burns, or irritation.</p>
<p>The Flawless Gold-Plated device removes excess facial hair with precision from the eyebrow area, professionally shapes and defines eyebrows, and gently cares for surrounding skin without any irritation, leaving eyebrows perfectly defined and facial skin silky smooth.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Pain-Free Precision Hair Removal with 18K Gold-Plated Rotating Blade:</strong> Professional-grade precision for fine hair removal.</li>
  <li><strong>Professional Eyebrow & Fine Area Shaping:</strong> Perfect eyebrows easily at home.</li>
  <li><strong>Completely Pain-Free, Irritation-Free & Chemical-Burn-Free:</strong> Safe for sensitive skin around eyebrows.</li>
  <li><strong>Luxurious Elegant Gold Design:</strong> Compact size for daily use and travel.</li>
  <li><strong>Battery-Powered:</strong> Easy to use anywhere and anytime.</li>
  <li><strong>Multipurpose:</strong> Suitable for eyebrows, light upper lip, and hairline fine hair.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Clean):</strong> Ensure eyebrow area is completely clean and dry.</li>
  <li><strong>Step 2 (Power On):</strong> Press the button to turn on the device.</li>
  <li><strong>Step 3 (Remove):</strong> Glide device gently over excess hair in light circular motions for precise removal.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>18K Gold-Plated Rotating Blade:</strong> Removes fine hair with high precision without pain.</li>
  <li><strong>Comfortable Non-Slip Handle:</strong> Ergonomic design for precision in removal.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For fine facial and eyebrow hair removal only.</li>
  <li>Do not use on broken, irritated, or burned skin.</li>
  <li>Keep out of reach of children.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking the Flawless Gold-Plated device for professional-grade eyebrow shaping and pain-free fine hair removal.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Flawless</td></tr>
  <tr><th>Category</th><td>Personal Care / Luxury Gold-Plated Eyebrow Hair Removal Devices</td></tr>
  <tr><th>Product Type</th><td>Luxury Gold-Plated Micro-Rotation Eyebrow & Fine Facial Hair Remover</td></tr>
  <tr><th>Volume/Weight</th><td>Compact travel-friendly size</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Including Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Perfectly defined eyebrows, smooth facial skin free of fine hair</td></tr>
  <tr><th>Texture</th><td>Comfortable ergonomic non-slip handle</td></tr>
  <tr><th>Fragrance</th><td>N/A</td></tr>
  <tr><th>Active Ingredients</th><td>18K Gold-Plated Rotating Blade, Precision Quiet Motor</td></tr>
  <tr><th>Country of Origin</th><td>USA</td></tr>
  <tr><th>Manufacturer</th><td>Finishing Touch Flawless</td></tr>
  <tr><th>Age Group</th><td>Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 18K Gold-Plated Parallel-Cut Rotation Blade Technology in Flawless</h2>

<h3>What problem does this solve?</h3>
<p>Flawless Gold-Plated Eyebrow Remover solves unwanted fine eyebrow and facial hair, difficulty achieving professional eyebrow shaping at home.</p>

<h3>Why choose Flawless Gold-Plated?</h3>
<p>Gold plating reduces blade friction and prevents skin sensitization, while the micro-rotation cutting mechanism precisely severs hair at surface level without contacting the dermis.</p>"""

    en_faqs = [
        ("What is the Flawless Gold-Plated Eyebrow Hair Remover?", "It is a luxury 18K gold-plated professional device from Flawless for pain-free precision fine eyebrow and facial hair removal."),
        ("What are the benefits of the gold-plated blade?", "Gold plating reduces friction, prevents irritation, and delivers professional-grade precision in fine hair removal."),
        ("Does it remove hair without pain?", "Yes, the rotating blade technology removes hair precisely without pain or chemical burns."),
        ("Is it suitable for eyebrow shaping?", "Yes, specifically designed for precise professional-grade eyebrow shaping and definition."),
        ("How do I use the device?", "Turn on, glide gently over excess hair in light circular motions on clean, dry skin."),
        ("Is it suitable for sensitive skin?", "Yes, safe for sensitive skin around the eyebrow and facial area."),
        ("Where is Flawless manufactured?", "In the USA by Finishing Touch Flawless."),
        ("How do I verify authenticity at Ekleel Abha?", "All Flawless products at Ekleel Abha are 100% original."),
        ("Is it quiet during operation?", "Yes, operates with a precision quiet motor."),
        ("Is it travel-friendly?", "Yes, compact design perfect for travel."),
        ("Can it remove upper lip fine hair?", "Yes, suitable for fine hair around upper lip and hairline."),
        ("What powers the device?", "Battery-powered for use anywhere and anytime."),
        ("How do I clean the device?", "Clean the head with the included brush or a soft cloth after use."),
        ("Is it suitable for beginners?", "Yes, easy to use for both beginners and professionals."),
        ("Does the gold design reflect luxury?", "Yes, elegant luxurious gold design."),
        ("Does it affect hair thickness?", "No, cuts hair at surface level without affecting the follicle or hair thickness."),
        ("Is it safe for daily use?", "Yes, safe for daily use."),
        ("Is it suitable for men and women?", "Yes, suitable for both for fine facial hair removal."),
        ("Is Flawless a globally recognized brand?", "Yes, Flawless is a world-renowned brand in hair removal devices."),
        ("Does it prevent redness after use?", "Yes, gold plating prevents post-use irritation and redness."),
        ("Is it reusable?", "Yes, suitable for repeated reuse."),
        ("Can it be used around the lip area?", "Yes, suitable for fine hair removal around the lips."),
        ("Is the blade replaceable?", "Check product specifications for blade/head replacement availability."),
        ("Is it a good luxury gift?", "Yes, elegant and practical gift for eyebrow care enthusiasts."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1902",
        "sku": "EK-1902",
        "gtin": "5010724536162",
        "brand": "Flawless",
        "ar": {
            "title": "مزيل شعر الحواجب مطلي بالذهب من  فلوليس",
            "meta_title": "مزيل شعر الحواجب المطلي بالذهب فلوليس | إكليل أبها",
            "meta_description": "اشتري مزيل شعر الحواجب المطلي بالذهب من فلوليس. جهاز احترافي بشفرة ذهبية لإزالة الشعر بدون ألم وتشكيل الحواجب. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["فلوليس", "مزيل_شعر_حواجب", "مطلي_بالذهب", "تشكيل_الحواجب", "إكليل_أبها"]
        },
        "en": {
            "title": "Flawless Gold-Plated Eyebrow Hair Remover",
            "meta_title": "Flawless Gold-Plated Eyebrow Hair Remover | Ekleel Abha",
            "meta_description": "Buy original Flawless Gold-Plated Eyebrow Hair Remover. Professional 18K gold blade device for pain-free eyebrow shaping. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["flawless", "gold_plated_eyebrow", "eyebrow_remover", "hair_remover", "ekleel_abha"]
        }
    }


def create_product_1903():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>فوط ذات عطر منعش من كيرفري 48 قطعة (Carefree Fresh Scent Daily Pantyliners - 48 Pieces)</strong> الباند اليومي المنعش والموثوق من كيرفري المصمم لتوفير شعور بالنظافة والانتعاش اليومي المستمر. يمتاز هذا الباند الفاخر (Carefree Fresh Scent Pantyliners 48 Pieces) بتقنية الامتصاص السريع، العطر المنعش الخفيف، والطبقة الخارجية الناعمة كالحرير لأقصى درجات الراحة.</p>
<p>يعمل باند كيرفري المنعش على امتصاص الإفرازات اليومية الخفيفة بسرعة وكفاءة، توفير شعور بالنظافة والانتعاش الدائم بعطره المنعش، والثبات التام طوال اليوم بلاصق القاع المحكم، ليمنحك ثقة وانتعاشاً وشعوراً بالنظافة من الصباح حتى المساء.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>امتصاص سريع وكفء للإفرازات اليومية:</strong> يحفظ جفاف ونظافة المنطقة الحساسة طوال اليوم.</li>
  <li><strong>عطر منعش خفيف لاستمرار الإحساس بالنظافة:</strong> يمنح شعوراً منتعشاً طوال ساعات اليوم.</li>
  <li><strong>طبقة سطحية ناعمة كالحرير:</strong> مريح جداً على البشرة الحساسة دون تهيج أو احتكاك.</li>
  <li><strong>لاصق قاع محكم للثبات التام:</strong> يبقى في مكانه دون تحرك طوال اليوم.</li>
  <li><strong>عبوة اقتصادية 48 قطعة:</strong> تكفي لشهر ونصف من الاستخدام اليومي المنتظم.</li>
  <li><strong>رفيع وغير مرئي:</strong> لا يُلاحظ تحت الملابس لأقصى راحة وثقة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> أزيلي الغلاف الواقي الخلفي عن اللاصق.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي الباند في وسط الملابس الداخلية مع التأكد من ثباته باللاصق.</li>
  <li><strong>الخطوة الثالثة:</strong> غيري الباند كل 4-6 ساعات أو عند الحاجة للحفاظ على أفضل نظافة وانتعاش.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>طبقة ناعمة كالحرير وجوهر ممتص سريع:</strong> يمتص الإفرازات سريعاً ويحافظ على الجفاف.</li>
  <li><strong>عطر منعش خفيف:</strong> يمنح شعوراً بالنظافة والانتعاش الدائم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي في الملابس الداخلية فقط وليس داخلياً.</li>
  <li>لا تُعاد الاستخدام، يُستعمل لمرة واحدة فقط.</li>
  <li>يُحفظ في مكان بارد وجاف بعيداً عن الرطوبة.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن باند كيرفري المنعش (48 قطعة) للحماية اليومية والانتعاش الدائم.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كيرفري (Carefree)</td></tr>
  <tr><th>الفئة</th><td>النظافة النسائية / بانديات كيرفري اليومية المنعشة العطرية</td></tr>
  <tr><th>نوع المنتج</th><td>باند نسائي يومي منعش بعطر خفيف لامتصاص الإفرازات اليومية (48 قطعة)</td></tr>
  <tr><th>الحجم/الوزن</th><td>48 قطعة</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (بما في ذلك البشرة الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>منطقة حساسة جافة ومنتعشة ونظيفة طوال اليوم</td></tr>
  <tr><th>الملمس</th><td>طبقة سطحية ناعمة كالحرير رفيعة وغير مرئية</td></tr>
  <tr><th>العطر</th><td>عطر منعش خفيف (Fresh Scent)</td></tr>
  <tr><th>المكونات النشطة</th><td>طبقة ناعمة، جوهر ممتص سريع، لاصق قاع محكم، عطر منعش</td></tr>
  <tr><th>بلد المنشأ</th><td>اوروبا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Carefree (Edgewell Personal Care)</td></tr>
  <tr><th>الفئة العمرية</th><td>النساء من جميع الأعمار</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد العطر المنعش وتقنية الامتصاص السريع في باند كيرفري (Carefree)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج باند كيرفري المنعش مشكلة الإفرازات اليومية الخفيفة، الإحساس بعدم النظافة، والحاجة لانتعاش يومي مستمر.</p>

<h3>لماذا يُعد باند كيرفري المنعش الخيار الأمثل؟</h3>
<p>لأن عطره المنعش الخفيف يمنح شعوراً دائماً بالنظافة بينما تمتص التقنية السريعة الإفرازات فوراً دون تراكمها.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التغيير كل 4-6 ساعات:</strong> للحفاظ على أقصى درجات النظافة والانتعاش.<br>
2. <strong>الاستخدام اليومي المنتظم:</strong> لحماية الملابس الداخلية وتجنب الإفرازات.<br>
3. <strong>التخلص الصحيح بعد الاستخدام:</strong> لفّ الباند وضعه في الزبالة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "البانديات المنعشة تسبب تهيج المنطقة الحساسة."<br>
<strong>الحقيقة:</strong> باند كيرفري مصنوع من مواد ناعمة لطيفة اختبرت سريرياً وآمنة للاستخدام اليومي.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تعمل طبقة البوليمر المسامية السطحية على توجيه الإفرازات للجوهر الممتص بسرعة عبر نظام أحادي الاتجاه يمنع عودة الرطوبة.</p>"""

    faqs = [
        ("ما هو باند كيرفري ذو العطر المنعش 48 قطعة؟", "هو باند نسائي يومي منعش من كيرفري بعطر خفيف وامتصاص سريع لحماية وانتعاش المنطقة الحساسة (48 قطعة)."),
        ("ما هي فوائد العطر المنعش والامتصاص السريع؟", "يمنح العطر شعوراً دائماً بالنظافة والانتعاش بينما تمتص التقنية السريعة الإفرازات فوراً."),
        ("هل يمتص الإفرازات اليومية بسرعة؟", "نعم، تقنية الامتصاص السريع تمتص الإفرازات اليومية الخفيفة فوراً."),
        ("كم قطعة في العبوة؟", "تحتوي العبوة على 48 قطعة."),
        ("كيف يُستخدم بالشكل الصحيح؟", "أزيلي الغلاف الواقي، ضعي الباند في وسط الملابس الداخلية، وغيريه كل 4-6 ساعات."),
        ("هل هو آمن للبشرة الحساسة؟", "نعم، مصنوع من مواد ناعمة لطيفة اختبرت سريرياً وآمنة."),
        ("أين صُنع باند كيرفري؟", "صُنع في أوروبا بواسطة Carefree (Edgewell Personal Care)."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كيرفري لدى إكليل أبها أصلية 100%."),
        ("هل رفيع وغير مرئي تحت الملابس؟", "نعم، تصميم رفيع وغير مرئي لأقصى ثقة وراحة."),
        ("ما نوع العطر في الباند؟", "عطر منعش خفيف (Fresh Scent) لطيف."),
        ("هل يثبت في مكانه طوال اليوم؟", "نعم، لاصق قاع محكم يثبته تماماً دون تحرك."),
        ("هل 48 قطعة تكفي شهراً؟", "نعم، تكفي لشهر ونصف من الاستخدام اليومي."),
        ("كيف أتخلص منه بعد الاستخدام؟", "لفّ الباند وضعه في الزبالة ولا تُرميه في المرحاض."),
        ("هل الطبقة السطحية ناعمة؟", "نعم، طبقة سطحية ناعمة كالحرير مريحة جداً."),
        ("هل يناسب الاستخدام اليومي المنتظم؟", "نعم، مصمم خصيصاً للاستخدام اليومي المنتظم."),
        ("كم ساعة تدوم فاعليته؟", "يُوصى بالتغيير كل 4-6 ساعات لأفضل نظافة."),
        ("هل يناسب النساء في جميع الأعمار؟", "نعم، مناسب للنساء من جميع الأعمار."),
        ("هل له رائحة قوية تزعج؟", "لا، العطر خفيف جداً وغير مزعج."),
        ("هل يتوفر بحجم آخر؟", "يتوفر بمقاسات وكميات متعددة في منتجات كيرفري."),
        ("هل يحمي الملابس الداخلية؟", "نعم، يحمي الملابس الداخلية من الإفرازات اليومية."),
        ("هل يمكن استخدامه خلال الدورة الشهرية؟", "هو مخصص للإفرازات اليومية الخفيفة وليس للحيض."),
        ("هل يترك أثراً على الملابس؟", "لا، اللاصق لا يترك أثراً على الملابس الداخلية."),
        ("هل يصلح للسفر؟", "نعم، العبوة مدمجة مثالية للسفر."),
        ("هل هو منتج طبي أو للنظافة العامة؟", "هو منتج للنظافة الشخصية اليومية العامة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Carefree Fresh Scent Daily Pantyliners - 48 Pieces</strong> are the trusted refreshing daily pantyliners from Carefree designed to provide continuous daily cleanliness and freshness. Features fast-absorption technology, a light fresh scent, and a silky-soft outer layer for maximum comfort.</p>
<p>Carefree Fresh Scent Pantyliners quickly and efficiently absorb light daily discharge, provide all-day cleanliness and freshness with their light fragrance, and stay securely in place with a firm base adhesive, giving you confidence, freshness, and a feeling of cleanliness from morning to night.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Fast Efficient Absorption of Daily Discharge:</strong> Keeps sensitive area dry and clean all day.</li>
  <li><strong>Light Fresh Scent for Continuous Cleanliness:</strong> Delivers refreshing feeling throughout the day.</li>
  <li><strong>Silky-Soft Surface Layer:</strong> Very comfortable on sensitive skin without irritation or friction.</li>
  <li><strong>Secure Base Adhesive for All-Day Stay:</strong> Stays in place without moving throughout the day.</li>
  <li><strong>Economical 48-Piece Pack:</strong> Lasts 6 weeks of daily regular use.</li>
  <li><strong>Thin & Invisible:</strong> Not noticeable under clothing for maximum comfort and confidence.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Remove the protective backing from the adhesive.</li>
  <li><strong>Step 2:</strong> Place pantyliner in the center of underwear ensuring it adheres securely.</li>
  <li><strong>Step 3:</strong> Change every 4-6 hours or as needed to maintain best cleanliness and freshness.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Soft Surface & Fast-Absorbing Core:</strong> Quickly absorbs discharge while maintaining dryness.</li>
  <li><strong>Light Fresh Fragrance:</strong> Delivers a continuous feeling of cleanliness and freshness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external use in underwear only; not for internal use.</li>
  <li>Single-use only; do not reuse.</li>
  <li>Store in a cool, dry place away from moisture.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every woman seeking Carefree Fresh Scent Pantyliners (48 pieces) for daily protection and continuous freshness.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Carefree</td></tr>
  <tr><th>Category</th><td>Feminine Hygiene / Carefree Fresh Scented Daily Pantyliners</td></tr>
  <tr><th>Product Type</th><td>Fresh-Scented Daily Women's Pantyliner for Light Daily Discharge Absorption (48 pieces)</td></tr>
  <tr><th>Volume/Weight</th><td>48 pieces</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Including Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Dry, refreshed, clean sensitive area all day</td></tr>
  <tr><th>Texture</th><td>Silky-soft thin invisible surface layer</td></tr>
  <tr><th>Fragrance</th><td>Light Fresh Scent</td></tr>
  <tr><th>Active Ingredients</th><td>Soft surface layer, fast-absorbing core, secure base adhesive, fresh fragrance</td></tr>
  <tr><th>Country of Origin</th><td>Europe</td></tr>
  <tr><th>Manufacturer</th><td>Carefree (Edgewell Personal Care)</td></tr>
  <tr><th>Age Group</th><td>Women of All Ages</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Carefree Fast-Absorption Unidirectional Core & Light Fresh Fragrance Technology</h2>

<h3>What problem does this solve?</h3>
<p>Carefree Fresh Scent Pantyliners solve light daily discharge, the feeling of uncleanliness, and the need for continuous daily freshness.</p>

<h3>Why choose Carefree Fresh Scent Pantyliners?</h3>
<p>The light fresh scent delivers a continuous feeling of cleanliness while the porous polymer surface layer rapidly channels discharge into the absorbing core via a unidirectional system preventing moisture return.</p>"""

    en_faqs = [
        ("What are Carefree Fresh Scent Daily Pantyliners - 48 Pieces?", "They are fresh-scented daily pantyliners from Carefree with fast absorption for daily protection and all-day freshness (48 pieces)."),
        ("What are the benefits of the fresh scent and fast absorption?", "The fresh scent delivers a continuous cleanliness feeling while fast absorption instantly absorbs light daily discharge."),
        ("Do they absorb daily discharge quickly?", "Yes, fast-absorption technology instantly absorbs light daily discharge."),
        ("How many pieces are in the pack?", "48 pieces per pack."),
        ("How do I use them correctly?", "Remove backing, place in center of underwear, change every 4-6 hours."),
        ("Are they safe for sensitive skin?", "Yes, clinically tested soft materials safe for daily use."),
        ("Where are Carefree pantyliners manufactured?", "In Europe by Carefree (Edgewell Personal Care)."),
        ("How do I verify authenticity at Ekleel Abha?", "All Carefree products at Ekleel Abha are 100% original."),
        ("Are they thin and invisible under clothing?", "Yes, thin design invisible under clothing for maximum confidence."),
        ("What type of scent do they have?", "Light Fresh Scent, not overpowering."),
        ("Do they stay securely in place all day?", "Yes, secure base adhesive ensures all-day stay without shifting."),
        ("Does 48 pieces last a month?", "Yes, lasts about 6 weeks of daily use."),
        ("How do I dispose of them after use?", "Wrap and place in the bin; do not flush."),
        ("Is the surface layer soft?", "Yes, silky-soft surface layer very comfortable on skin."),
        ("Are they suitable for daily regular use?", "Yes, specifically designed for daily regular use."),
        ("How many hours do they last?", "Change every 4-6 hours for best cleanliness."),
        ("Are they suitable for women of all ages?", "Yes, suitable for women of all ages."),
        ("Do they have an overwhelming smell?", "No, the fresh scent is very light and pleasant."),
        ("Are other sizes available?", "Carefree offers multiple sizes and quantities."),
        ("Do they protect underwear?", "Yes, protect underwear from light daily discharge."),
        ("Can they be used during menstruation?", "Designed for light daily discharge, not for menstrual flow."),
        ("Do they leave residue on clothing?", "No, adhesive leaves no residue on underwear."),
        ("Are they good for travel?", "Yes, compact pack ideal for travel."),
        ("Are they medical or general hygiene?", "General daily personal hygiene product."),
        ("Are they available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1903",
        "sku": "EK-1903",
        "gtin": "3574660625769",
        "brand": "Carefree",
        "ar": {
            "title": "فوط ذات عطرمنعش من كيرفري 48 قطعة",
            "meta_title": "باند كيرفري المنعش 48 قطعة | إكليل أبها",
            "meta_description": "اشتري باند كيرفري ذات العطر المنعش (48 قطعة). باند يومي بامتصاص سريع وعطر منعش خفيف للحماية اليومية. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كيرفري", "باند_يومي", "باند_منعش", "نظافة_نسائية", "إكليل_أبها"]
        },
        "en": {
            "title": "Carefree Fresh Scent Daily Pantyliners - 48 Pieces",
            "meta_title": "Carefree Fresh Scent Daily Pantyliners 48 Pieces | Ekleel Abha",
            "meta_description": "Buy original Carefree Fresh Scent Daily Pantyliners (48 pieces). Fast-absorbing daily pantyliners for all-day freshness. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["carefree", "fresh_scent_pantyliners", "daily_pantyliners", "feminine_hygiene", "ekleel_abha"]
        }
    }


def create_product_1904():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>حناء بني للشعر من فاتيكا 60 جم (Vatika Brown Hair Henna - 60g)</strong> حناء الشعر الطبيعي الفاخر من فاتيكا دافرس المصنوع بتركيبة طبيعية مركّزة لصباغة الشعر باللون البني الطبيعي الأصيل وتغذيته في آنٍ واحد. يرتكز هذا المنتج الفاخر (Vatika Brown Henna 60g) على ورق الحناء الطبيعي المُعالَج (Natural Henna), خلاصة الأعشاب المغذية، والمواد الطبيعية المجففة والمطحونة بعناية.</p>
<p>يعمل حناء فاتيكا البني على صباغة الشعر بلون بني طبيعي أصيل ومميز، تغذية وتقوية جذور الشعر والخيوط بالأعشاب الطبيعية، ومنح الشعر لمعاناً استثنائياً وقوة وحيوية، ليترك شعرك بلوناً بنياً ناعماً، لامعاً، مجدداً وأكثر كثافة وقوة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>صبغة طبيعية أصيلة بلون بني جميل:</strong> تمنح الشعر لوناً بنياً طبيعياً أنيقاً.</li>
  <li><strong>تغطية الشعر الأبيض والرمادي بفاعلية:</strong> يغطي الشعر الأبيض بلون بني طبيعي متجانس.</li>
  <li><strong>تقوية وتغذية الشعر بخلاصة الأعشاب:</strong> يمنح الشعر كثافة وقوة ولمعاناً استثنائياً.</li>
  <li><strong>خالٍ 100% من الأمونيا والكيماويات الضارة:</strong> صباغة طبيعية آمنة دون تلف الشعر.</li>
  <li><strong>وصفة فاتيكا دافرس التقليدية الفاخرة:</strong> تراث أصيل في الصباغة الطبيعية للشعر.</li>
  <li><strong>عبوة اقتصادية 60 جم:</strong> كافية لصباغة الشعر بالكامل.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التحضير):</strong> امزجي الحناء بالماء الدافئ حتى قوام كريمي متجانس.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وزعي الحناء بالتساوي على الشعر الجاف من الجذور حتى الأطراف.</li>
  <li><strong>الخطوة الثالثة (الانتظار):</strong> غطي الشعر بالكيس البلاستيكي وانتظري 30-60 دقيقة ثم اشطفي بالماء الدافئ جيداً.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>ورق الحناء الطبيعي (Natural Henna):</strong> يصبغ الشعر بلون طبيعي أصيل دون كيماويات ضارة.</li>
  <li><strong>خلاصة الأعشاب المغذية:</strong> تقوي وتغذي خيوط الشعر والجذور.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الشعر وفروة الرأس فقط.</li>
  <li>تجنبي التلامس مع العينين واشطفي بالماء فوراً في حال التلامس.</li>
  <li>يُوصى باختبار الحساسية قبل 24 ساعة على منطقة صغيرة من الجلد.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن حناء فاتيكا البني 60 جم لصباغة شعره بلون بني طبيعي وتغذيته.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>فاتيكا (Vatika)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / حناء فاتيكا الطبيعية لصباغة الشعر بالألوان الطبيعية 60جم</td></tr>
  <tr><th>نوع المنتج</th><td>حناء شعر طبيعي بلون بني أصيل لصباغة الشعر وتغذيته (60جم)</td></tr>
  <tr><th>الحجم/الوزن</th><td>60 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (العادي والجاف والدهني والمصبوغ)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر بلون بني طبيعي جميل لامع، كثيف، مغذى ومقوى</td></tr>
  <tr><th>الملمس</th><td>مسحوق حناء طبيعي يمزج بالماء لقوام كريمي ناعم</td></tr>
  <tr><th>العطر</th><td>عطر الحناء الطبيعي الأصيل</td></tr>
  <tr><th>المكونات النشطة</th><td>ورق الحناء الطبيعي، خلاصة الأعشاب المغذية، مواد طبيعية</td></tr>
  <tr><th>بلد المنشأ</th><td>الإمارات العربية المتحدة (UAE)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Vatika (Dabur Group)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الحناء الطبيعية وخلاصة الأعشاب في فاتيكا البني (Vatika Brown Henna)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج حناء فاتيكا البني مشكلة الشعر الأبيض والرمادي الغير مرغوب فيه، وضعف وجفاف الشعر وضياع لمعانه الطبيعي.</p>

<h3>لماذا تنجح الحناء الطبيعية في الصباغة والتغذية؟</h3>
<p>لأن ورق الحناء يحتوي على اللوسون (Lawsone) الذي يرتبط بكيراتين الشعر كيميائياً ليمنحه اللون البني الأصيل الثابت.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>تحضير القوام الكريمي الصحيح:</strong> أضيفي الماء تدريجياً للحصول على قوام كريمي مثالي للتطبيق.<br>
2. <strong>التغطية الكاملة من الجذور للأطراف:</strong> ضمان تغطية متجانسة اللون.<br>
3. <strong>الانتظار ساعة كاملة للون أكثر ثباتاً:</strong> كلما طالت مدة التطبيق كلما كان اللون أكثر عمقاً وثباتاً.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الحناء تجفف الشعر وتزيد هشاشته."<br>
<strong>الحقيقة:</strong> حناء فاتيكا مدعومة بخلاصة الأعشاب المغذية التي تقوي الشعر وتمنحه الترطيب الطبيعي.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يرتبط اللوسون (2-Hydroxy-1,4-naphthoquinone) في الحناء بمجموعات الأمين (-NH2) في كيراتين الشعر برابطة كيميائية تساهمية ثابتة لمنح اللون الطبيعي الأصيل.</p>"""

    faqs = [
        ("ما هو حناء بني للشعر من فاتيكا 60 جم؟", "هو حناء شعر طبيعي من فاتيكا دافرس بتركيبة طبيعية مركزة لصباغة الشعر بلون بني طبيعي أصيل وتغذيته 60 جم."),
        ("ما هي فوائد الحناء الطبيعية وخلاصة الأعشاب؟", "تصبغ الحناء الشعر بلون بني طبيعي ثابت وتغطي الشعر الأبيض، بينما تقوي خلاصة الأعشاب الشعر."),
        ("هل تغطي الشعر الأبيض والرمادي بفاعلية؟", "نعم، تغطي الشعر الأبيض والرمادي بلون بني طبيعي متجانس."),
        ("ما وزن العبوة؟", "تأتي بوزن 60 جم."),
        ("كيف تُستخدم بالشكل الصحيح؟", "امزجي بالماء الدافئ لقوام كريمي، وزعي على الشعر الجاف، انتظري 30-60 دقيقة، اشطفي جيداً."),
        ("هل هي خالية من الأمونيا والكيماويات الضارة؟", "نعم، 100% طبيعية خالية من الأمونيا."),
        ("أين صُنع حناء فاتيكا البني؟", "صُنع في الإمارات العربية المتحدة بواسطة Vatika (Dabur Group)."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات فاتيكا لدى إكليل أبها أصلية 100%."),
        ("هل اللون البني ثابت لفترة طويلة؟", "نعم، اللوسون يرتبط بكيراتين الشعر كيميائياً لثبات طويل الأمد."),
        ("ما رائحة حناء فاتيكا؟", "رائحة الحناء الطبيعي الأصيل."),
        ("هل تمنح الشعر لمعاناً؟", "نعم، تمنح الشعر لمعاناً استثنائياً وحيوية."),
        ("هل 60 جم تكفي لصبغ الشعر الكامل؟", "تكفي لصبغ شعر طبيعي إلى متوسط الطول."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الرطوبة."),
        ("هل تناسب جميع أنواع الشعر؟", "نعم، مناسبة لجميع أنواع الشعر."),
        ("هل تقوي جذور الشعر؟", "نعم، خلاصة الأعشاب تقوي جذور الشعر وتغذيها."),
        ("كم مرة يمكن صبغ الشعر بها؟", "يُنصح بالصباغة كل 3-4 أسابيع للحفاظ على اللون."),
        ("هل تناسب الشعر المصبوغ مسبقاً؟", "يُوصى باختبار صغير قبل التطبيق الكامل على الشعر المصبوغ."),
        ("هل تُوصى بها للحوامل؟", "يُنصح باستشارة الطبيب قبل الاستخدام أثناء الحمل."),
        ("هل فاتيكا من أشهر ماركات الحناء؟", "نعم، Vatika من أشهر وأوثق ماركات الحناء الطبيعية عالمياً."),
        ("هل يختلف اللون حسب الشعر الطبيعي؟", "نعم، النتيجة تعتمد على لون الشعر الطبيعي ومدة التطبيق."),
        ("هل تصلح للرجال أيضاً؟", "نعم، مناسبة للرجال والنساء."),
        ("هل يمكن خلطها بزيوت طبيعية؟", "نعم، يمكن إضافة زيت جوز الهند أو الزيتون لقوام أفضل."),
        ("هل تترك لوناً أحمراً أولاً ثم يصبح بنياً؟", "الحناء البني مُعالجة للحصول على اللون البني مباشرةً."),
        ("هل تصلح هدية؟", "نعم، هدية طبيعية ومفيدة للاهتمام بصحة الشعر."),
        ("هل تتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، تتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Vatika Brown Hair Henna - 60g</strong> is a premium natural hair henna from Vatika Dabur formulated with a concentrated natural blend for coloring hair with an authentic natural brown shade while nourishing it simultaneously. Made with Natural Processed Henna Leaves, nourishing herb extracts, and carefully dried and ground natural materials.</p>
<p>Vatika Brown Henna colors hair with an authentic natural brown shade, nourishes and strengthens hair roots and strands with natural herbs, and imparts exceptional shine and vitality, leaving hair beautifully brown, shiny, renewed, and noticeably thicker and stronger.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Authentic Natural Brown Color:</strong> Imparts a beautiful natural elegant brown shade.</li>
  <li><strong>Effective White & Gray Hair Coverage:</strong> Covers white hair with natural uniform brown.</li>
  <li><strong>Strengthening & Nourishing with Herb Extracts:</strong> Imparts thickness, strength, and exceptional shine.</li>
  <li><strong>100% Ammonia-Free & Chemical-Free:</strong> Safe natural coloring without hair damage.</li>
  <li><strong>Vatika Dabur Traditional Premium Formula:</strong> Authentic heritage in natural hair coloring.</li>
  <li><strong>Economical 60g Pack:</strong> Sufficient for complete hair coloring.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Prepare):</strong> Mix henna with warm water until creamy consistent paste.</li>
  <li><strong>Step 2 (Apply):</strong> Distribute henna evenly on dry hair from roots to tips.</li>
  <li><strong>Step 3 (Wait):</strong> Cover with plastic cap, wait 30-60 minutes, then rinse thoroughly with warm water.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Henna Leaves:</strong> Color hair with authentic natural shade without harmful chemicals.</li>
  <li><strong>Nourishing Herb Extracts:</strong> Strengthen and nourish hair strands and roots.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external hair and scalp use only.</li>
  <li>Avoid contact with eyes; rinse immediately with water if contact occurs.</li>
  <li>Recommend 24-hour patch test on a small skin area before use.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Vatika Brown Henna 60g for natural brown hair coloring and nourishment.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Vatika</td></tr>
  <tr><th>Category</th><td>Hair Care / Vatika Natural Hair Henna for Natural Color Shades 60g</td></tr>
  <tr><th>Product Type</th><td>Natural Brown Shade Hair Henna for Coloring & Nourishing (60g)</td></tr>
  <tr><th>Volume/Weight</th><td>60 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Normal, Dry, Oily & Previously Colored)</td></tr>
  <tr><th>Finish</th><td>Beautiful natural brown hair, shiny, nourished, strengthened, and vibrant</td></tr>
  <tr><th>Texture</th><td>Natural henna powder mixed with water for smooth creamy paste</td></tr>
  <tr><th>Fragrance</th><td>Authentic natural henna aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Henna Leaves, Nourishing Herb Extracts, Natural Materials</td></tr>
  <tr><th>Country of Origin</th><td>UAE</td></tr>
  <tr><th>Manufacturer</th><td>Vatika (Dabur Group)</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Lawsone Keratin Covalent Binding & Herb Extract Protein Strengthening</h2>

<h3>What problem does this solve?</h3>
<p>Vatika Brown Henna solves unwanted white and gray hair, hair weakness and dryness, and the loss of natural hair shine.</p>

<h3>Why choose Vatika Brown Hair Henna?</h3>
<p>Lawsone (2-Hydroxy-1,4-naphthoquinone) in henna covalently bonds to hair keratin amine (-NH2) groups forming a stable long-lasting brown color, while herb extracts supply amino acids and proteins.</p>"""

    en_faqs = [
        ("What is Vatika Brown Hair Henna - 60g?", "It is a premium natural hair henna from Vatika Dabur with a concentrated natural formula for authentic brown hair coloring and nourishment."),
        ("What are the benefits of natural henna and herb extracts?", "Henna colors hair with stable natural brown shade and covers white hair, while herb extracts strengthen and nourish."),
        ("Does it cover white and gray hair effectively?", "Yes, covers white and gray hair with uniform natural brown color."),
        ("What weight is this pack?", "60g."),
        ("How do I use it correctly?", "Mix with warm water for creamy paste, apply on dry hair root to tip, wait 30-60 minutes, rinse well."),
        ("Is it ammonia-free and chemical-free?", "Yes, 100% natural and ammonia-free."),
        ("Where is Vatika Brown Henna manufactured?", "In UAE by Vatika (Dabur Group)."),
        ("How do I verify authenticity at Ekleel Abha?", "All Vatika products at Ekleel Abha are 100% original."),
        ("Is the brown color long-lasting?", "Yes, Lawsone covalently bonds to keratin for long-lasting color stability."),
        ("What does Vatika Henna smell like?", "Authentic natural henna aroma."),
        ("Does it give hair shine?", "Yes, imparts exceptional natural shine and vitality."),
        ("Does 60g cover all hair?", "Sufficient for short to medium length natural hair."),
        ("How should I store it?", "In a cool, dry place away from moisture."),
        ("Is it suitable for all hair types?", "Yes, suitable for all hair types."),
        ("Does it strengthen hair roots?", "Yes, herb extracts strengthen and nourish hair roots."),
        ("How often can I color with it?", "Every 3-4 weeks to maintain color."),
        ("Is it suitable for previously colored hair?", "Recommend a small patch test before full application."),
        ("Is it recommended for pregnant women?", "Consult a doctor before use during pregnancy."),
        ("Is Vatika among the most famous henna brands?", "Yes, Vatika is one of the most trusted natural henna brands globally."),
        ("Does the color vary based on natural hair?", "Yes, results depend on natural hair color and application duration."),
        ("Is it suitable for men too?", "Yes, suitable for both men and women."),
        ("Can it be mixed with natural oils?", "Yes, adding coconut or olive oil enhances the consistency."),
        ("Is the brown formulated directly without red?", "Brown Henna is specially processed for direct brown output."),
        ("Is it a good gift?", "Yes, natural and beneficial gift for hair care enthusiasts."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1904",
        "sku": "EK-1904",
        "gtin": "6291069701746",
        "brand": "Vatika",
        "ar": {
            "title": "حناء بني للشعر  من فاتيكا 60 جم",
            "meta_title": "حناء شعر بني فاتيكا 60جم | إكليل أبها",
            "meta_description": "اشتري حناء بني للشعر من فاتيكا (60 جم). حناء طبيعي لصباغة الشعر بلون بني طبيعي وتغذيته. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["فاتيكا", "حناء_بني", "صباغة_شعر_طبيعية", "حناء_شعر", "إكليل_أبها"]
        },
        "en": {
            "title": "Vatika Brown Hair Henna - 60g",
            "meta_title": "Vatika Brown Hair Henna 60g | Ekleel Abha",
            "meta_description": "Buy original Vatika Brown Hair Henna (60g). Natural henna for authentic brown hair coloring and nourishment. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["vatika", "brown_henna", "natural_hair_color", "hair_henna", "ekleel_abha"]
        }
    }


def create_product_1905():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>بودرة للأطفال من نونو 100 جم (Nunu Baby Powder 100g)</strong> بودرة الأطفال اللطيفة الحنون من نونو المصممة خصيصاً لحماية وعناية وتلطيف بشرة الأطفال الرقيقة الحساسة. يرتكز هذا المنتج الطبي (Nunu Baby Powder 100g) على التلك الطبيعي المنقى (Natural Purified Talc)، خلاصة البابونج المهدئة، والمواد اللطيفة الآمنة للرضع والأطفال الصغار.</p>
<p>تعمل بودرة نونو على تجفيف واستيعاب الرطوبة الزائدة في ثنايا بشرة الطفل، تهدئة وتلطيف البشرة المتهيجة والحساسة، ومنع الاحتكاك والطفح الجلدي الناتج عن الرطوبة المتراكمة، ليبقى طفلك جافاً، ناعماً، مرتاحاً، ومحمياً من الطفح الجلدي طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تجفيف وامتصاص الرطوبة الزائدة من ثنايا بشرة الطفل:</strong> يمنع تراكم الرطوبة والاحتكاك الجلدي.</li>
  <li><strong>تهدئة وتلطيف البشرة المتهيجة بخلاصة البابونج:</strong> يهدئ الاحمرار والتهيج ببشرة الطفل الحساسة.</li>
  <li><strong>منع الطفح الجلدي والاحمرار الناتج عن الحفاضات:</strong> حماية فائقة من طفح الحفاضة.</li>
  <li><strong>تركيبة لطيفة آمنة للرضع والأطفال الصغار:</strong> مجربة ومعتمدة طبياً للاستخدام على بشرة الأطفال.</li>
  <li><strong>عطر نونو اللطيف الناعم الخاص بالأطفال:</strong> يمنح الطفل رائحة ناعمة منعشة.</li>
  <li><strong>عبوة اقتصادية 100 جم:</strong> كافية للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> نظف وجفف بشرة الطفل جيداً قبل الاستعمال.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضع البودرة في راحة يدك أولاً ثم وزعها برفق على مناطق ثنايا بشرة الطفل (الرقبة، الإبط، منطقة الحفاضة).</li>
  <li><strong>الخطوة الثالثة (التغطية):</strong> وزعي البودرة برفق حتى التوزيع الكامل المتجانس (يُستعمل عند كل تغيير للحفاضة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>التلك الطبيعي المنقى (Natural Purified Talc):</strong> يمتص الرطوبة الزائدة ويبقي بشرة الطفل جافة.</li>
  <li><strong>خلاصة البابونج المهدئة:</strong> تهدئ البشرة المتهيجة وتلطف الاحمرار.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على بشرة الأطفال فقط.</li>
  <li>تجنب استنشاق الرذاذ قرب وجه الطفل أو أنفه.</li>
  <li>في حال تهيج أو احمرار مستمر استشر طبيب الأطفال.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل أم تبحث عن بودرة نونو للأطفال 100 جم لحماية وعناية بشرة طفلها الرقيقة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>نونو (Nunu)</td></tr>
  <tr><th>الفئة</th><td>العناية بالأطفال / بودرات نونو اللطيفة لحماية بشرة الأطفال الحساسة 100جم</td></tr>
  <tr><th>نوع المنتج</th><td>بودرة طبيعية لطيفة لتجفيف وحماية بشرة الأطفال الحساسة (100جم)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>بشرة الأطفال الحساسة الرقيقة (الرضع والأطفال الصغار)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة طفل جافة ناعمة، مهدأة، محمية من الطفح الجلدي</td></tr>
  <tr><th>الملمس</th><td>بودرة ناعمة خفيفة لطيفة ذات ملمس حريري</td></tr>
  <tr><th>العطر</th><td>عطر نونو اللطيف الناعم الخاص بالأطفال</td></tr>
  <tr><th>المكونات النشطة</th><td>تلك طبيعي منقى، خلاصة البابونج، مواد لطيفة آمنة</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Nunu Baby Care Products</td></tr>
  <tr><th>الفئة العمرية</th><td>الرضع والأطفال (من الولادة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد التلك المنقى وخلاصة البابونج في بودرة نونو للأطفال</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج بودرة نونو للأطفال مشكلة رطوبة بشرة الطفل الزائدة، الطفح الجلدي من الحفاضة، والاحمرار والتهيج في ثنايا البشرة الحساسة.</p>

<h3>لماذا ينجح التلك المنقى وخلاصة البابونج في حماية بشرة الطفل؟</h3>
<p>لأن التلك يمتص الرطوبة الزائدة بسرعة فائقة ويقلل الاحتكاك، بينما يثبط مستخلص البابونج مسارات الالتهاب الخلوي COX-2.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الوضع في الراحة أولاً:</strong> ضعي البودرة في راحة يدك لتجنب استنشاق الطفل.<br>
2. <strong>التطبيق عند كل تغيير للحفاضة:</strong> لضمان الحماية المستمرة.<br>
3. <strong>التجفيف الكامل قبل الوضع:</strong> يضاعف فاعلية البودرة في منع الاحتكاك.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "بودرة الأطفال تسبب مشاكل تنفسية."<br>
<strong>الحقيقة:</strong> بودرة نونو آمنة عند الاستخدام الصحيح بوضعها في اليد أولاً وتجنب استنشاقها قرب وجه الطفل.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تمتص حبيبات التلك الدقيقة الرطوبة عبر مسامح السطحية بشكل فوري وتكوّن طبقة حاجزة تمنع الاحتكاك بين ثنايا الجلد.</p>"""

    faqs = [
        ("ما هي بودرة نونو للأطفال 100 جم؟", "هي بودرة أطفال لطيفة من نونو بالتلك الطبيعي المنقى وخلاصة البابونج لتجفيف وحماية وتهدئة بشرة الأطفال الحساسة 100 جم."),
        ("ما هي فوائد التلك المنقى وخلاصة البابونج؟", "يمتص التلك الرطوبة الزائدة ويمنع الاحتكاك، بينما يهدئ البابونج التهيج والاحمرار."),
        ("هل تمنع طفح الحفاضة؟", "نعم، تحمي من تراكم الرطوبة والاحتكاك المسبب لطفح الحفاضة."),
        ("ما وزن العبوة؟", "تأتي بوزن 100 جم."),
        ("كيف تُستخدم بالشكل الصحيح؟", "ضعي البودرة في راحة يدك أولاً ثم وزعيها برفق على مناطق ثنايا الطفل عند كل تغيير للحفاضة."),
        ("هل هي آمنة للرضع والأطفال الصغار؟", "نعم، تركيبة لطيفة مجربة ومعتمدة للاستخدام على بشرة الرضع والأطفال."),
        ("أين صُنعت بودرة نونو؟", "صُنعت في المملكة العربية السعودية."),
        ("كيف أتأكد من أصالتها لدى إكليل أبها؟", "جميع منتجات نونو لدى إكليل أبها أصلية 100%."),
        ("هل تهدئ بشرة الطفل المتهيجة؟", "نعم، خلاصة البابونج تهدئ الاحمرار والتهيج بلطف."),
        ("ما رائحة بودرة نونو؟", "عطر نونو اللطيف الناعم الخاص بالأطفال."),
        ("هل ملمسها ناعم على بشرة الطفل؟", "نعم، بودرة ناعمة خفيفة بملمس حريري."),
        ("هل 100 جم تدوم طويلاً؟", "نعم، تكفي لعدة أسابيع من الاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الرطوبة."),
        ("هل مناسبة من الولادة؟", "نعم، آمنة للاستخدام منذ الولادة."),
        ("هل تمنع الاحتكاك الجلدي في الثنايا؟", "نعم، تقلل الاحتكاك في مناطق الثنايا والثنيات الجلدية."),
        ("كم مرة تُستخدم يومياً؟", "عند كل تغيير للحفاضة."),
        ("هل تناسب الأطفال الذين يعانون من الحساسية؟", "يُنصح باستشارة طبيب الأطفال للأطفال الذين لديهم حساسية شديدة."),
        ("هل تترك بقعاً على الملابس؟", "قد تترك أثراً خفيفاً يزول بالغسيل."),
        ("هل مناسبة للإبطين والرقبة أيضاً؟", "نعم، مناسبة لجميع مناطق الثنايا في جسم الطفل."),
        ("هل بودرة نونو مشهورة في السعودية؟", "نعم، من العلامات المحبوبة للأمهات السعوديات."),
        ("هل يمكن استخدامها للكبار أيضاً؟", "مصممة للأطفال، لكنها ناعمة بما يكفي للكبار أيضاً."),
        ("هل تحمي من الاحتكاك في الصيف؟", "نعم، تحمي من الاحتكاك الناتج عن التعرق في الصيف."),
        ("هل تتوفر بأحجام أخرى؟", "تتوفر منتجات نونو بأحجام متعددة."),
        ("هل تصلح هدية للأم الجديدة؟", "نعم، هدية عملية ومميزة للأمهات الجدد."),
        ("هل تتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، تتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Nunu Baby Powder 100g</strong> is a gentle, caring baby powder from Nunu specifically designed to protect, care for, and soothe delicate sensitive baby skin. Formulated with Natural Purified Talc, soothing Chamomile extract, and gentle materials safe for infants and young children.</p>
<p>Nunu Baby Powder absorbs excess moisture in baby skin folds, soothes and calms irritated sensitive skin, and prevents friction and rash from accumulated moisture, keeping your baby dry, soft, comfortable, and protected from rash all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Moisture Absorption in Baby Skin Folds:</strong> Prevents moisture accumulation and skin friction.</li>
  <li><strong>Soothing Irritated Skin with Chamomile Extract:</strong> Calms redness and irritation on sensitive baby skin.</li>
  <li><strong>Diaper Rash Prevention:</strong> Superior protection from diaper rash and redness.</li>
  <li><strong>Gentle Safe Formula for Infants:</strong> Medically tested and approved for baby skin use.</li>
  <li><strong>Gentle Nunu Baby Fragrance:</strong> Imparts a soft refreshing baby scent.</li>
  <li><strong>Economical 100g Pack:</strong> Sufficient for continuous daily use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Clean):</strong> Clean and thoroughly dry baby's skin before use.</li>
  <li><strong>Step 2 (Apply):</strong> Place powder in your palm first, then gently distribute on baby skin fold areas (neck, armpits, diaper area).</li>
  <li><strong>Step 3 (Distribute):</strong> Gently spread until evenly distributed (use at every diaper change).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Purified Talc:</strong> Absorbs excess moisture and keeps baby skin dry.</li>
  <li><strong>Soothing Chamomile Extract:</strong> Calms irritated skin and soothes redness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external baby skin use only.</li>
  <li>Avoid inhalation near baby's face or nose.</li>
  <li>Consult a pediatrician if persistent irritation or redness occurs.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every mother seeking Nunu Baby Powder 100g for protecting and caring for their baby's delicate skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Nunu</td></tr>
  <tr><th>Category</th><td>Baby Care / Nunu Gentle Baby Powders for Sensitive Baby Skin Protection 100g</td></tr>
  <tr><th>Product Type</th><td>Gentle Natural Baby Powder for Drying & Protecting Sensitive Baby Skin (100g)</td></tr>
  <tr><th>Volume/Weight</th><td>100 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Sensitive Delicate Baby Skin (Infants & Young Children)</td></tr>
  <tr><th>Finish</th><td>Dry, soft, soothed, rash-protected baby skin</td></tr>
  <tr><th>Texture</th><td>Fine lightweight silky-soft gentle powder</td></tr>
  <tr><th>Fragrance</th><td>Gentle soft Nunu Baby fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Purified Talc, Chamomile Extract, Gentle Safe Materials</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia</td></tr>
  <tr><th>Manufacturer</th><td>Nunu Baby Care Products</td></tr>
  <tr><th>Age Group</th><td>Infants & Children (From Birth)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Purified Talc Microporous Moisture Absorption & Chamomile COX-2 Anti-Inflammatory</h2>

<h3>What problem does this solve?</h3>
<p>Nunu Baby Powder solves excess baby skin moisture, diaper rash, and redness and irritation in sensitive skin folds.</p>

<h3>Why choose Nunu Baby Powder?</h3>
<p>Purified Talc micro-particles instantly absorb excess moisture via surface adsorption forming a protective barrier reducing skin fold friction, while Chamomile extract inhibits COX-2 inflammatory pathways.</p>"""

    en_faqs = [
        ("What is Nunu Baby Powder 100g?", "It is a gentle baby powder from Nunu with Natural Purified Talc and Chamomile extract for drying, protecting, and soothing sensitive baby skin."),
        ("What are the benefits of Purified Talc and Chamomile Extract?", "Purified Talc absorbs excess moisture and prevents friction, while Chamomile soothes irritation and redness."),
        ("Does it prevent diaper rash?", "Yes, protects against moisture accumulation and friction causing diaper rash."),
        ("What weight is this pack?", "100g."),
        ("How do I use it correctly?", "Place in palm first, then gently distribute on baby's skin fold areas at every diaper change."),
        ("Is it safe for infants from birth?", "Yes, gentle formula tested and approved for baby skin from birth."),
        ("Where is Nunu Baby Powder manufactured?", "In Saudi Arabia by Nunu Baby Care Products."),
        ("How do I verify authenticity at Ekleel Abha?", "All Nunu products at Ekleel Abha are 100% original."),
        ("Does it soothe irritated baby skin?", "Yes, Chamomile extract gently soothes redness and irritation."),
        ("What does Nunu Baby Powder smell like?", "Gentle soft Nunu Baby fragrance."),
        ("Is the texture silky-soft on baby skin?", "Yes, fine lightweight powder with silky-soft texture."),
        ("Does 100g last long?", "Yes, lasts weeks of daily use."),
        ("How should I store it?", "In a cool, dry place away from moisture."),
        ("Is it suitable from birth?", "Yes, safe from birth."),
        ("Does it prevent friction in skin folds?", "Yes, reduces friction in skin folds and creases."),
        ("How many times daily?", "At every diaper change."),
        ("Is it suitable for babies with sensitive skin?", "Consult a pediatrician for babies with severe sensitivities."),
        ("Does it leave stains on clothes?", "May leave a slight residue that washes out."),
        ("Is it suitable for neck and armpits too?", "Yes, suitable for all baby skin fold areas."),
        ("Is Nunu popular in Saudi Arabia?", "Yes, a beloved brand among Saudi mothers."),
        ("Can adults use it too?", "Designed for babies but gentle enough for adults."),
        ("Does it protect from summer friction?", "Yes, protects from sweat-induced friction in summer."),
        ("Are other sizes available?", "Nunu products available in multiple sizes."),
        ("Is it a good gift for new mothers?", "Yes, practical and thoughtful gift for new mothers."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1905",
        "sku": "EK-1905",
        "gtin": "6281053210309",
        "brand": "Nunu",
        "ar": {
            "title": "بودرة  للأطفال من نونو 100 جم",
            "meta_title": "بودرة الأطفال من نونو 100جم | إكليل أبها",
            "meta_description": "اشتري بودرة الأطفال من نونو (100 جم). بودرة لطيفة بالتلك وخلاصة البابونج لتجفيف وحماية بشرة الأطفال الحساسة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["نونو", "بودرة_أطفال", "حماية_بشرة_الرضيع", "عناية_أطفال", "إكليل_أبها"]
        },
        "en": {
            "title": "Nunu Baby Powder 100g",
            "meta_title": "Nunu Baby Powder 100g | Ekleel Abha",
            "meta_description": "Buy original Nunu Baby Powder (100g). Gentle Purified Talc & Chamomile baby powder for protecting and soothing sensitive baby skin. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["nunu", "baby_powder", "infant_skin_protection", "baby_care", "ekleel_abha"]
        }
    }


def create_product_1906():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول طهارة للمناطق الحساسة 100مل (Taharah Intimate Wash 100ml)</strong> غسول طبي طبيعي متخصص مصنوع بتركيبة موازنة لحموضة المنطقة الحميمة لتنظيف وحماية المنطقة الحساسة للمرأة بأمان وفاعلية. يرتكز هذا الغسول (Taharah Intimate Wash 100ml) على تركيبة الـ pH المتوازن (pH 3.5-4.5)، خلاصة اللافندر المهدئة، والمواد اللطيفة الخالية من الصابون.</p>
<p>يعمل غسول طهارة على تنظيف المنطقة الحميمة بأمان دون الإخلال بتوازن البيئة البكتيرية الطبيعية، حماية وتهدئة البشرة الحساسة من التهيج والجفاف، ومنع العدوى البكتيرية والفطرية، ليترك المنطقة الحساسة نظيفة، منتعشة، محمية وآمنة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف آمن وموازن لحموضة المنطقة الحميمة (pH 3.5-4.5):</strong> لا يخل بتوازن البيئة البكتيرية الطبيعية الواقية.</li>
  <li><strong>حماية وتهدئة البشرة الحساسة من التهيج والجفاف:</strong> يقي من الجفاف والاحمرار.</li>
  <li><strong>منع العدوى البكتيرية والفطرية:</strong> يدعم الحماية الطبيعية للمنطقة الحميمة.</li>
  <li><strong>عطر لافندر خفيف مهدئ:</strong> يمنح شعوراً منتعشاً وناعماً طوال اليوم.</li>
  <li><strong>خالٍ من الصابون والكحول والبارابين:</strong> آمن ولطيف للاستخدام اليومي.</li>
  <li><strong>عبوة مدمجة 100 مل:</strong> مناسبة للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية صغيرة من غسول طهارة على راحة اليد أو إسفنجة ناعمة.</li>
  <li><strong>الخطوة الثانية:</strong> غسلي المنطقة الخارجية الحساسة فقط بلطف (لا تستخدمي داخلياً).</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي بالماء الفاتر جيداً وجففي برفق (يُستعمل مرة أو مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>تركيبة pH متوازن (3.5-4.5):</strong> توازي الحموضة الطبيعية للمنطقة الحميمة وتحافظ على توازن البيئة البكتيرية.</li>
  <li><strong>خلاصة اللافندر والمواد اللطيفة:</strong> تهدئ التهيج وتمنح انتعاشاً ناعماً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي فقط على المنطقة الخارجية الحميمة.</li>
  <li>تجنبي الاستخدام الداخلي (لا يُستعمل مهبلياً).</li>
  <li>في حال استمرار التهيج أو الإفرازات غير الطبيعية استشيري طبيب النساء.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن غسول طهارة للمنطقة الحساسة 100 مل للتنظيف الآمن والحماية اليومية.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>طهارة (Taharah)</td></tr>
  <tr><th>الفئة</th><td>النظافة النسائية الطبية / غسولات طهارة الطبية للمنطقة الحميمة 100ml</td></tr>
  <tr><th>نوع المنتج</th><td>غسول طبي موازن pH للمنطقة الحميمة للتنظيف الآمن والحماية اليومية (100ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>بشرة المنطقة الحميمة الحساسة (جميع أنواع)</td></tr>
  <tr><th>المظهر النهائي</th><td>منطقة حميمة نظيفة، منتعشة، محمية ومتوازنة طوال اليوم</td></tr>
  <tr><th>الملمس</th><td>جل غسول سائل لطيف ناعم</td></tr>
  <tr><th>العطر</th><td>عطر لافندر خفيف مهدئ</td></tr>
  <tr><th>المكونات النشطة</th><td>تركيبة pH متوازن (3.5-4.5)، خلاصة اللافندر، مواد لطيفة خالية من الصابون</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Taharah Personal Care</td></tr>
  <tr><th>الفئة العمرية</th><td>النساء من جميع الأعمار</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد تركيبة pH المتوازن في غسول طهارة للمنطقة الحميمة</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول طهارة مشكلة اضطراب التوازن البكتيري للمنطقة الحميمة، التهيج والجفاف، والحاجة للتنظيف الآمن اليومي.</p>

<h3>لماذا تنجح تركيبة pH المتوازن في حماية المنطقة الحميمة؟</h3>
<p>لأن الحفاظ على pH 3.5-4.5 يدعم نمو البكتيريا المفيدة (Lactobacillus) الحامية طبيعياً من العدوى والفطريات.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الغسل مرة إلى مرتين يومياً:</strong> للحفاظ على النظافة المثالية.<br>
2. <strong>الشطف الجيد بالماء الفاتر:</strong> لإزالة أي بقايا غسول تماماً.<br>
3. <strong>التجفيف الكامل بعد الغسل:</strong> لمنع تراكم الرطوبة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الصابون العادي يكفي لتنظيف المنطقة الحميمة."<br>
<strong>الحقيقة:</strong> الصابون العادي قلوي (pH 9-10) ويخل بتوازن البيئة الحمضية الواقية للمنطقة الحميمة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يحافظ تركيب pH 3.5-4.5 على بيئة حمضية تدعم هيمنة Lactobacillus acidophilus المنتجة للحمض اللاكتيكي الحامية طبيعياً.</p>"""

    faqs = [
        ("ما هو غسول طهارة للمنطقة الحساسة 100 مل؟", "هو غسول طبي متخصص من طهارة بتركيبة pH متوازن (3.5-4.5) وخلاصة اللافندر للتنظيف الآمن والحماية اليومية للمنطقة الحميمة."),
        ("ما هي فوائد pH المتوازن وخلاصة اللافندر؟", "يحافظ pH المتوازن على التوازن البكتيري الطبيعي ويمنع العدوى، بينما يهدئ اللافندر التهيج."),
        ("هل يحافظ على التوازن البكتيري الطبيعي؟", "نعم، تركيبة pH 3.5-4.5 تدعم بيئة الـ Lactobacillus الواقية طبيعياً."),
        ("ما حجم العبوة؟", "تأتي بسعة 100 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية صغيرة على راحة اليد، غسلي المنطقة الخارجية الحساسة فقط بلطف، اشطفي بالماء الفاتر واجففي."),
        ("هل هو آمن للاستخدام اليومي؟", "نعم، تركيبة لطيفة خالية من الصابون والكحول آمنة للاستخدام اليومي."),
        ("أين صُنع غسول طهارة؟", "صُنع في المملكة العربية السعودية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات طهارة لدى إكليل أبها أصلية 100%."),
        ("هل يهدئ التهيج والجفاف في المنطقة الحساسة؟", "نعم، يهدئ التهيج ويمنع الجفاف."),
        ("ما رائحة غسول طهارة؟", "عطر لافندر خفيف مهدئ."),
        ("هل يمنع العدوى الفطرية؟", "يدعم البيئة الحمضية الواقية الطبيعية من العدوى الفطرية."),
        ("هل 100 مل تدوم طويلاً؟", "نعم، تكفي لعدة أسابيع من الاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب النساء في جميع الأعمار؟", "نعم، مناسب للنساء من جميع الأعمار."),
        ("هل يمنح انتعاشاً طوال اليوم؟", "نعم، يمنح شعوراً منتعشاً وناعماً طوال اليوم."),
        ("كم مرة يومياً؟", "مرة أو مرتين يومياً."),
        ("هل يُستخدم خارجياً أم داخلياً؟", "للاستخدام الخارجي فقط على المنطقة الخارجية."),
        ("هل يناسب فترة ما بعد الولادة؟", "يُنصح بمشورة الطبيب قبل الاستخدام في الفترة ما بعد الولادة."),
        ("هل مناسب للسفر؟", "نعم، حجم مدمج مثالي للسفر."),
        ("هل الصابون العادي مناسب بديلاً؟", "لا، الصابون العادي قلوي يخل بتوازن المنطقة الحميمة."),
        ("هل قابل لإعادة التدوير؟", "نعم."),
        ("هل يناسب البشرة الحساسة؟", "نعم، تركيبة لطيفة خاصة للبشرة الحساسة."),
        ("هل يمكن استخدامه أثناء الدورة الشهرية؟", "نعم، مناسب للاستخدام خلال الدورة الشهرية."),
        ("هل هو منتج طبي أو للنظافة؟", "منتج للنظافة الصحية النسائية المتخصصة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Taharah Intimate Wash 100ml</strong> is a specialized medical natural wash formulated with a pH-balanced formula for the intimate area to safely and effectively cleanse and protect women's sensitive area. Formulated with pH-balanced formula (3.5-4.5), soothing Lavender extract, and gentle soap-free materials.</p>
<p>Taharah Intimate Wash safely cleanses the intimate area without disrupting the natural bacterial environment balance, protects and soothes sensitive skin from irritation and dryness, and prevents bacterial and fungal infections, leaving the sensitive area clean, refreshed, protected, and safe all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Safe pH-Balanced Intimate Area Cleansing (pH 3.5-4.5):</strong> Does not disrupt the natural protective bacterial environment.</li>
  <li><strong>Soothing Sensitive Skin from Irritation & Dryness:</strong> Protects against dryness and redness.</li>
  <li><strong>Bacterial & Fungal Infection Prevention:</strong> Supports natural intimate area protection.</li>
  <li><strong>Light Soothing Lavender Fragrance:</strong> Delivers refreshing soft feeling all day.</li>
  <li><strong>Soap-Free, Alcohol-Free & Paraben-Free:</strong> Safe and gentle for daily use.</li>
  <li><strong>Compact 100ml Bottle:</strong> Ideal for daily use and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a small amount of Taharah Intimate Wash onto palm or soft sponge.</li>
  <li><strong>Step 2:</strong> Gently wash the external sensitive area only (do not use internally).</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and pat dry gently (use once or twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>pH-Balanced Formula (3.5-4.5):</strong> Matches natural intimate area acidity maintaining bacterial balance.</li>
  <li><strong>Lavender Extract & Gentle Materials:</strong> Soothes irritation and delivers soft refreshing feeling.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external intimate area use only.</li>
  <li>Do not use internally (not for vaginal use).</li>
  <li>Consult a gynecologist if persistent irritation or abnormal discharge occurs.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every woman seeking Taharah Intimate Wash 100ml for safe daily cleansing and intimate area protection.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Taharah</td></tr>
  <tr><th>Category</th><td>Medical Feminine Hygiene / Taharah Medical Intimate Area Washes 100ml</td></tr>
  <tr><th>Product Type</th><td>Medical pH-Balanced Intimate Wash for Safe Daily Cleansing & Protection (100ml)</td></tr>
  <tr><th>Volume/Weight</th><td>100 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Sensitive Intimate Area Skin (All Types)</td></tr>
  <tr><th>Finish</th><td>Clean, refreshed, protected, pH-balanced intimate area all day</td></tr>
  <tr><th>Texture</th><td>Gentle smooth liquid wash gel</td></tr>
  <tr><th>Fragrance</th><td>Light soothing Lavender fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>pH-Balanced Formula (3.5-4.5), Lavender Extract, Soap-Free Gentle Materials</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia</td></tr>
  <tr><th>Manufacturer</th><td>Taharah Personal Care</td></tr>
  <tr><th>Age Group</th><td>Women of All Ages</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of pH-Balanced Formula Supporting Lactobacillus Dominant Microbiome</h2>

<h3>What problem does this solve?</h3>
<p>Taharah Intimate Wash solves intimate area bacterial imbalance, irritation and dryness, and the need for safe daily cleansing.</p>

<h3>Why choose Taharah Intimate Wash?</h3>
<p>Maintaining pH 3.5-4.5 supports Lactobacillus acidophilus dominance producing protective lactic acid, creating an inhospitable environment for pathogenic bacteria and Candida species.</p>"""

    en_faqs = [
        ("What is Taharah Intimate Wash 100ml?", "It is a specialized medical intimate wash from Taharah with pH-balanced formula (3.5-4.5) and Lavender extract for safe daily cleansing and intimate area protection."),
        ("What are the benefits of pH balance and Lavender extract?", "pH balance maintains natural bacterial balance and prevents infection, while Lavender soothes irritation."),
        ("Does it maintain the natural bacterial balance?", "Yes, pH 3.5-4.5 formula supports natural Lactobacillus protective environment."),
        ("What volume is this bottle?", "100ml."),
        ("How do I use it correctly?", "Apply small amount to palm, gently wash external area only, rinse with warm water and pat dry once or twice daily."),
        ("Is it safe for daily use?", "Yes, gentle soap-free, alcohol-free formula safe for daily use."),
        ("Where is Taharah manufactured?", "In Saudi Arabia by Taharah Personal Care."),
        ("How do I verify authenticity at Ekleel Abha?", "All Taharah products at Ekleel Abha are 100% original."),
        ("Does it soothe intimate area irritation and dryness?", "Yes, soothes irritation and prevents dryness."),
        ("What scent does Taharah have?", "Light soothing Lavender fragrance."),
        ("Does it prevent fungal infections?", "Supports the acidic protective environment naturally resistant to fungal infections."),
        ("Does 100ml last long?", "Yes, lasts weeks of daily use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for women of all ages?", "Yes, suitable for women of all ages."),
        ("Does it provide all-day freshness?", "Yes, delivers refreshing soft feeling all day."),
        ("How many times daily?", "Once or twice daily."),
        ("Is it for external or internal use?", "External intimate area use only; not for internal use."),
        ("Is it suitable post-childbirth?", "Consult a doctor before use post-childbirth."),
        ("Is it travel-friendly?", "Yes, compact bottle ideal for travel."),
        ("Is regular soap a suitable alternative?", "No, regular soap is alkaline (pH 9-10) disrupting intimate area balance."),
        ("Is it recyclable?", "Yes."),
        ("Is it suitable for sensitive intimate skin?", "Yes, specially formulated gentle formula for sensitive skin."),
        ("Can it be used during menstruation?", "Yes, suitable for use during menstruation."),
        ("Is it a medical or hygiene product?", "Specialized women's personal hygiene product."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1906",
        "sku": "EK-1906",
        "gtin": "6287001780085",
        "brand": "Taharah",
        "ar": {
            "title": "غسول طهارة للمناطق الحساسة 100مل",
            "meta_title": "غسول طهارة للمنطقة الحساسة 100مل | إكليل أبها",
            "meta_description": "اشتري غسول طهارة للمنطقة الحساسة (100 مل). غسول طبي بـ pH متوازن وخلاصة اللافندر للتنظيف الآمن اليومي. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["طهارة", "غسول_مناطق_حساسة", "نظافة_نسائية_طبية", "pH_متوازن", "إكليل_أبها"]
        },
        "en": {
            "title": "Taharah Intimate Wash 100ml",
            "meta_title": "Taharah Intimate Wash 100ml | Ekleel Abha",
            "meta_description": "Buy original Taharah Intimate Wash (100ml). Medical pH-balanced intimate wash for safe daily cleansing and protection. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["taharah", "intimate_wash", "pH_balanced", "feminine_hygiene", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 38 builders complete")
