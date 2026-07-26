import json, os

def _make_toothpaste_b53(pid, gtin, ar_name, en_name, brand_ar, brand_en, variant_ar, variant_en, volume_ar, volume_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> معجون الأسنان الطبي الفاخر الأصيل من {brand_ar} المصمم خصيصاً للتنظيف الشامل، تقوية الميناء، الوقاية من التسوس، ومنح الفم انتعاشاً عاطراً يمتد طوال اليوم. يرتكز هذا المعجون الطبي ({en_name}) على فلوريد الصوديوم الفعّال، خلاصة {variant_ar} الفوارة، والمركبات المنظفة للويحات البكتيرية.</p>
<p>يعمل معجون أسنان {brand_ar} {variant_ar} على إزالة اللويحات البكتيرية (البلاك) والتكتلات الجيرية، حماية اللثة والأسنان من التسوس، وتطهير الفم والأنفاس من الروائح الكريهة، ليترك أسنانك ناصعة النظافة، بيضاء، محمية، ومفعمة بانتعاش {variant_ar} من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف شامل وعناية متكاملة لـ 12-24 ساعة:</strong> ينظف الفواصل بين الأسنان ويزيل الرواسب البكتيرية.</li>
  <li><strong>انتعاش فائق بـ {variant_ar}:</strong> يطرد رائحة الفم الكريهة ويمنح أنفاساً معطرة.</li>
  <li><strong>تقوية ميناء الأسنان والحماية من التسوس بالفلوريد:</strong> يعيد بناء المعادن الضعيفة في الميناء.</li>
  <li><strong>حماية وصحة اللثة:</strong> يمنع التهابات اللثة الناتجة عن تراكم البكتيريا.</li>
  <li><strong>جودة {brand_ar} العالمية الموثوقة:</strong> العلامة الأولى الموصى بها في العناية بالفم.</li>
  <li><strong>عبوة سعة {volume_ar}:</strong> حجم ممتاز للاستخدام العائلي اليومي المنتظم.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية بحجم حبة البازلاء من معجون {brand_ar} على فرشاة أسنان مناسبة.</li>
  <li><strong>الخطوة الثانية:</strong> نظفي الأسنان برفق بحركات دائرية لمدة دقيقتين كاملتين مرتين يومياً.</li>
  <li><strong>الخطوة الثالثة:</strong> ابصقي المعجون واشطفي الفم بالماء دون بلع (يُستعمل مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>فلوريد الصوديوم النشط:</strong> يقوي ميناء السن ويحميه من التآكل والحموضة والتسوس.</li>
  <li><strong>خلاصة {variant_ar} والمكونات المنظفة:</strong> تمنحان الفم والأنفاس نظافة وانتعاشاً تدوم طوال اليوم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الفموي فقط، تجنبي البلع.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال دون 6 سنوات دون إشراف عائلي.</li>
  <li>في حال حدوث تهيج غير عادي استشيري طبيب الأسنان.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} للحماية من التسوس والانتعاش اليومي بالفم.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>{brand_ar} ({brand_en})</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم والأسنان / معاجين {brand_ar} لحماية الفم والأسنان {volume_ar}</td></tr>
  <tr><th>نوع المنتج</th><td>معجون أسنان لحماية الميناء والانتعاش والتنظيف ({volume_ar})</td></tr>
  <tr><th>الحجم/الوزن</th><td>{volume_ar}</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الأسنان واللثة</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان ناصعة النظافة، بيضاء، محمية من التسوس ومفعمة بـ {variant_ar}</td></tr>
  <tr><th>الملمس</th><td>معجون/جل ناعم رغوي غني</td></tr>
  <tr><th>العطر</th><td>عطر {variant_ar} الفواح المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>فلوريد الصوديوم، خلاصة {variant_ar}، مركبات تنظيف البلاك</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة المتحدة / الولايات المتحدة / الإمارات</td></tr>
  <tr><th>الشركة المصنعة</th><td>{brand_en} Oral Care</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون والأطفال (من 6 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد الفلوريد وخلاصة {variant_ar} في معجون {brand_ar}</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج معجون أسنان {brand_ar} مشكلة تراكم البلاك واللويحات البكتيرية، التسوس، ورائحة الفم الكريهة.</p>

<h3>لماذا تنجح تركيبة {brand_ar}؟</h3>
<p>لأن الفلوريد يعيد ترسب البلورات المعدنية في نقاط الضعف المجهرية بينما تثبط المواد المطهرة تكاثر البكتيريا.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنظيف مرتين يومياً بالفرشاة لمدة دقيقتين:</strong> يضمن أقصى نظافة وتغطية.<br>
2. <strong>استخدام الخيط الطبي يومياً:</strong> ينظف الفواصل التي لا تصل إليها فرشاة الأسنان.<br>
3. <strong>تقليل السكريات والحلويات:</strong> يقلل تكون الأحماض الضارة بالميناء.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "معاجين الجل أقل كفاءة من المعاجين البيضاء التقليدية."<br>
<strong>الحقيقة:</strong> تحتوي معاجين الجل على نفس تركيز الفلوريد المنظف مع ميزة إضافية في منح انتعاش أسرع وأقوى.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يتفاعل الفلوريد مع هيدروكسي أباتيت الميناء ليتكون فلوروأباتيت (Fluorapatite) الأكثر مقاومة للأحماض الفموية pH < 5.5.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو معجون أسنان طبي تخصصي من {brand_ar} للوقاية من التسوس والانتعاش بـ {variant_ar} ({volume_ar})."),
        (f"ما هي فوائد الفلوريد وعطر {variant_ar}؟", f"يقوي الفلوريد ميناء الأسنان ويحميه من التسوس، بينما يمنح عطر {variant_ar} أنفاساً معطرة ونظيفة."),
        ("هل يقي من التسوس والبلاك بفاعلية؟", "نعم، مثبت سريرياً في حماية الأسنان من التسوس وتراكم اللويحات البكتيرية."),
        (f"ما حجم العبوة؟", f"تأتي بسعة {volume_ar}."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية بحجم البازلاء، نظفي لمدة دقيقتين مرتين يومياً وابصقي المعجون."),
        ("هل يناسب جميع أفراد الأسرة؟", "نعم، آمن ومناسب لجميع أفراد الأسرة من سن 6 سنوات."),
        (f"أين صُنع معجون {brand_ar}؟", f"صُنع بأعلى معايير جودة العناية بالفم العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {variant_ar} المنعش الفواح."),
        ("هل يطرد رائحة الفم الكريهة؟", "نعم، يمنح الفم والأنفاس انتعاشاً عاطراً يمتد طوال اليوم."),
        (f"هل العبوة {volume_ar} تكفي للاستخدام اليومي العائلي؟", "نعم، حجم ممتازة يكفي لأسابيع من الاستخدام العائلي اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        (f"هل {brand_ar} علامة عالمية موثوقة في أطباء الأسنان؟", f"نعم، {brand_en} علامة عالمية رائدة وموثوقة جداً في العناية بالفم والأسنان."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل يناسب الأطفال فوق 6 سنوات؟", "نعم، مناسب للأطفال من 6 سنوات تحت إشراف الوالدين."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يزيل التصبغات السطحية برفق؟", "نعم، يزيل التصبغات السطحية والبقع برفق دون خدش الميناء."),
        ("هل يحمي اللثة من التهابات البكتيريا؟", "نعم، ينظف خط اللثة ويحميها من التهيجات والبكتيريا."),
        ("هل يمنح شعوراً بالنظافة الثلجية الفائقة؟", "نعم، يترك الفم والأسنان بنظافة وانتعاش ثلجي فائق."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الاستخدام اليومي المستمر؟", "نعم، مصمم للاستخدام اليومي الدائم كمعجون أسنان رئيسي."),
        ("هل يحمي من الحموضة الضارة بالأسنان؟", "نعم، يقوي الميناء ضد التآكل الحمضي المباشر."),
        ("هل يصلح ضمن مجموعة العناية الفموية؟", "نعم، منتج كلاسيكي طبي لا غنى عنه في المنزل."),
        ("هل يترك الأسنان بيضاء ومشرقة؟", "نعم، يعيد نضارة وبياض الأسنان الطبيعي بانتظام التنظيف."),
        ("هل تتوفر منه أحجام ونكهات أخرى؟", "نعم، تتوفر تشكيلة واسعة تناسب جميع الأذواق.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic advanced medical toothpaste from {brand_en} designed for comprehensive dental cleaning, enamel strengthening, cavity prevention, and all-day fresh breath. Formulated with active Sodium Fluoride, refreshing {variant_en} extract, and antibacterial plaque-cleansing agents.</p>
<p>{brand_en} Toothpaste {variant_en} removes bacterial plaque buildup and tartar, protects teeth and gums against acid decay, and purifies mouth odor, leaving your teeth spotlessly clean, white, protected, and fragranced with {variant_en} freshness from the first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Comprehensive Cleaning & 12-24H Care:</strong> Cleanses interdental spaces removing bacterial plaque.</li>
  <li><strong>Vibrant {variant_en} Freshness:</strong> Eliminates bad breath imparting an invigorating clean scent.</li>
  <li><strong>Enamel Strengthening & Cavity Protection with Fluoride:</strong> Remineralizes weakened enamel surfaces.</li>
  <li><strong>Gum Health Defense:</strong> Protects gums from inflammation caused by bacterial accumulation.</li>
  <li><strong>Global Trusted Quality of {brand_en}:</strong> Leading globally recognized oral care brand.</li>
  <li><strong>Generous {volume_en} Format:</strong> Excellent size for daily family dental routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a pea-sized amount of {brand_en} toothpaste onto a suitable toothbrush.</li>
  <li><strong>Step 2:</strong> Brush teeth thoroughly in gentle circular motions for two minutes twice daily.</li>
  <li><strong>Step 3:</strong> Spit out toothpaste and rinse mouth with water without swallowing (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Active Sodium Fluoride:</strong> Strengthens tooth enamel protecting it against erosion, acid, and decay.</li>
  <li><strong>{variant_en} Extract & Cleansing Agents:</strong> Leave mouth and breath intensely clean and refreshed all day.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external oral use only; do not swallow.</li>
  <li>Keep out of reach of children under 6 years without parental supervision.</li>
  <li>If unusual irritation occurs, consult your dentist.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for cavity protection, enamel defense, and daily fresh mouth feel.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>{brand_en}</td></tr>
  <tr><th>Category</th><td>Oral Care / {brand_en} Cavity Protection Toothpastes {volume_en}</td></tr>
  <tr><th>Product Type</th><td>Fluoride Cavity Protection, Enamel Defense & Fresh Toothpaste ({volume_en})</td></tr>
  <tr><th>Volume/Weight</th><td>{volume_en}</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Teeth & Gums Types</td></tr>
  <tr><th>Finish</th><td>Spotlessly clean, white, cavity-protected teeth with {variant_en} fresh breath</td></tr>
  <tr><th>Texture</th><td>Smooth refreshing foaming paste/gel</td></tr>
  <tr><th>Fragrance</th><td>Invigorating {variant_en} mint fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Sodium Fluoride, {variant_en} Extract, Plaque-Cleansing Compounds</td></tr>
  <tr><th>Country of Origin</th><td>UK / USA / UAE</td></tr>
  <tr><th>Manufacturer</th><td>{brand_en} Oral Care</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 6+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Sodium Fluoride Fluorapatite Remineralization & Anti-Plaque Defense</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves bacterial plaque accumulation, enamel acid decay, bad breath, and cavity formation.</p>

<h3>Why choose {brand_en} Toothpaste?</h3>
<p>Sodium Fluoride deposits mineral fluorapatite onto enamel surface micro-pores resisting dietary acid attacks below pH 5.5.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a specialized oral care toothpaste from {brand_en} for cavity defense and {variant_en} fresh breath ({volume_en})."),
        (f"What are the benefits of Sodium Fluoride and {variant_en}?", f"Fluoride strengthens tooth enamel preventing decay, while {variant_en} delivers clean fresh breath."),
        ("Does it effectively protect against cavities and plaque?", "Yes, clinically proven to protect teeth against cavities and plaque buildup."),
        (f"What volume is contained in this tube?", f"{volume_en}."),
        ("How do I use it correctly?", "Apply pea-sized amount, brush for 2 minutes twice daily, spit and rinse."),
        ("Is it suitable for the whole family?", "Yes, safe and suitable for all family members aged 6+."),
        (f"Where is {brand_en} Toothpaste manufactured?", "Manufactured to international oral care quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", f"Invigorating {variant_en} fresh mint aroma."),
        ("Does it eliminate bad breath?", "Yes, delivers long-lasting fresh breath throughout the day."),
        (f"Does the {volume_en} tube last long for family use?", "Yes, generous volume lasting weeks of regular family use."),
        ("How should I store it?", "In a cool, dry place."),
        (f"Is {brand_en} a trusted global dental brand?", f"Yes, {brand_en} is a world-renowned leader in oral healthcare."),
        ("How many times daily?", "Twice daily (morning & night)."),
        ("Is it suitable for children aged 6+?", "Yes, suitable for children aged 6+ under adult supervision."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it gently remove surface stains?", "Yes, gently cleans plaque and surface stains without scratching enamel."),
        ("Does it protect gums from bacterial irritation?", "Yes, cleanses gumline protecting against bacterial irritation."),
        ("Does it leave a clean refreshed mouth feel?", "Yes, leaves mouth and teeth feeling intensely clean."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for daily continuous use?", "Yes, designed for continuous daily use as a main toothpaste."),
        ("Does it protect against enamel acid erosion?", "Yes, reinforces enamel against direct dietary acid erosion."),
        ("Is it an essential household item?", "Yes, an indispensable classic household oral care item."),
        ("Does it keep teeth naturally white?", "Yes, restores natural tooth cleanliness and brightness with regular brushing."),
        ("Are other sizes and flavors available?", "Yes, wide variety of sizes and flavors available.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": brand_en,
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. معجون أسنان طبي من {brand_ar} للحماية من التسوس والانتعاش بـ {variant_ar}. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. {brand_en} cavity protection & fluoride toothpaste with {variant_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1978():
    return _make_toothpaste_b53(
        pid=1978, gtin="6805699959189",
        ar_name="معجون اسنان عناية متعددة بالأعشاب من سنسوداين 100 مل",
        en_name="Sensodyne Multi Care Herbal Toothpaste 100ml",
        brand_ar="سنسوداين", brand_en="Sensodyne",
        variant_ar="خلاصة الأعشاب الطبيعية (Herbal Multi Care)", variant_en="Herbal Extracts",
        volume_ar="100 مل", volume_en="100ml",
        feature_ar="يجمع بين الحساسية والعناية بالأعشاب المنعشة", feature_en="combines sensitivity care with herbal freshness",
        tags_ar=["سنسوداين", "سنسوداين_اعشاب", "عناية_متعددة", "معجون_اعشاب_سنسوداين", "إكليل_أبها"],
        tags_en=["sensodyne", "sensodyne_herbal", "multi_care", "herbal_toothpaste", "ekleel_abha"]
    )


def create_product_1979():
    return _make_toothpaste_b53(
        pid=1979, gtin="6805699956744",
        ar_name="معجون اسنان النعناع المنعش من سنسوداين75مل",
        en_name="Sensodyne Fresh Mint Toothpaste 75ml",
        brand_ar="سنسوداين", brand_en="Sensodyne",
        variant_ar="النعناع المنعش (Fresh Mint)", variant_en="Fresh Mint",
        volume_ar="75 مل", volume_en="75ml",
        feature_ar="عطر النعناع الفواح لحساسية الأسنان والانتعاش", feature_en="fresh mint flavor for sensitive teeth and clean breath",
        tags_ar=["سنسوداين", "نعناع_منعش", "سنسوداين_نعناع", "معجون_أسنان_سنسوداين", "إكليل_أبها"],
        tags_en=["sensodyne", "fresh_mint", "sensodyne_mint", "sensitivity_toothpaste", "ekleel_abha"]
    )


def create_product_1980():
    return _make_toothpaste_b53(
        pid=1980, gtin="6281001101185",
        ar_name="معجون اسنان بنكهة النعناع من كولوجيت 100مل",
        en_name="Colgate Mint Toothpaste 100ml",
        brand_ar="كولجيت", brand_en="Colgate",
        variant_ar="نكهة النعناع الأيقونية (Great Regular Flavor Mint)", variant_en="Classic Mint",
        volume_ar="100 مل", volume_en="100ml",
        feature_ar="نكهة كولجيت النعناع الكلاسيكية لحماية التسوس", feature_en="classic Colgate mint flavor for maximum cavity defense",
        tags_ar=["كولجيت", "معجون_كولجيت", "نعناع_كولجيت", "حماية_التسوس", "إكليل_أبها"],
        tags_en=["colgate", "colgate_mint", "cavity_protection", "colgate_toothpaste", "ekleel_abha"]
    )


def create_product_1981():
    return _make_toothpaste_b53(
        pid=1981, gtin="6920354828195",
        ar_name="معجون اسنان توتال 12 من كولوجيت 75مل",
        en_name="Colgate Total 12 Toothpaste 75ml",
        brand_ar="كولجيت", brand_en="Colgate",
        variant_ar="توتال 12 لحماية الـ 12 ساعة (Total 12)", variant_en="Total 12 Antibacterial",
        volume_ar="75 مل", volume_en="75ml",
        feature_ar="حماية البكتيريا الشاملة لـ 12 ساعة متواصلة", feature_en="12-hour continuous antibacterial whole mouth protection",
        tags_ar=["كولجيت", "توتال_12", "كولجيت_توتال", "حماية_12_ساعة", "إكليل_أبها"],
        tags_en=["colgate", "colgate_total12", "total12", "antibacterial_toothpaste", "ekleel_abha"]
    )


def create_product_1982():
    return _make_toothpaste_b53(
        pid=1982, gtin="6281001108030",
        ar_name="معجون اسنان جل بالنعناع من كولوجيت 125مل",
        en_name="Colgate Mint Gel Toothpaste 125ml",
        brand_ar="كولجيت", brand_en="Colgate",
        variant_ar="الجل الأزرق بالنعناع الفوار (Mint Gel)", variant_en="Sparkling Mint Gel",
        volume_ar="125 مل", volume_en="125ml",
        feature_ar="جل منعش بحبيبات النعناع لحماية ونضارة مضاعفة", feature_en="refreshing gel with mint crystals for sparkling clean breath",
        tags_ar=["كولجيت", "كولجيت_جل", "جل_النعناع", "كولجيت_125مل", "إكليل_أبها"],
        tags_en=["colgate", "colgate_gel", "mint_gel", "sparkling_mint", "ekleel_abha"]
    )


print("Loaded all 5 Batch 53 builders complete")
