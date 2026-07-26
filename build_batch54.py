import json, os

def _make_colgate_whitening(pid, gtin, ar_name, en_name, variant_ar, variant_en, volume_ar, volume_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> معجون الأسنان المطور المخصص لتبييض الأسنان وإعادة النضارة الطبيعية من كولجيت العالمية المصمم خصيصاً لإزالة التصبغات والبقع السطحية الصعبة الناتجة عن القهوة والشاي والتطهر الفوري للفم. يرتكز هذا المعجون الأصيل ({en_name}) على بلورات التبييض الدقيقة (Micro-Whitening Crystals)، فلوريد الصوديوم الفعّال ضد التسوس، وحبيبات الانتعاش الفوارة {variant_ar}.</p>
<p>يعمل معجون كولجيت {variant_ar} على تلميع الأسنان بأمان دون خدش الميناء، إزالة اللويحات البكتيرية والتصبغات الصفراء، وتقوية ميناء السن ضد الأحماض الفموية، ليترك أسنانك بيضاء ناصعة، ناعمة الملمس، ومحمية بابتسامة مشرقة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تبييض ناصع وإزالة التصبغات الصفراء والبقع:</strong> تلميع آمن ببلورات الدقيقة الناعمة.</li>
  <li><strong>انتعاش فائق يدوم طويلاً بـ {variant_ar}:</strong> يطرد الروائح الكريهة ويمنح أنفاساً معطرة.</li>
  <li><strong>تقوية ميناء الأسنان والحماية من التسوس بالفلوريد:</strong> يحمي الأسنان من تآكل الأحماض.</li>
  <li><strong>حماية وصحة اللثة والفم:</strong> ينظف الفواصل ورواسب البكتيريا بفاعلية.</li>
  <li><strong>معجون التبييض رقم 1 الموصى به عالمياً من كولجيت:</strong> نتائج سريرية ملحوظة من الأسابيع الأولى.</li>
  <li><strong>عبوة سعة {volume_ar}:</strong> حجم ممتاز للاستخدام العائلي اليومي المنتظم.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية بحجم حبة البازلاء من معجون كولجيت على فرشاة أسنان مناسبة.</li>
  <li><strong>الخطوة الثانية:</strong> نظفي الأسنان برفق بحركات دائرية لمدة دقيقتين كاملتين مرتين يومياً.</li>
  <li><strong>الخطوة الثالثة:</strong> ابصقي المعجون واشطفي الفم بالماء دون بلع (يُستعمل مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>بلورات التبييض الدقيقة وفلوريد الصوديوم:</strong> تلمع السطح المجهري للسن وتمنع التسوس.</li>
  <li><strong>المكونات المنظفة وحبيبات الانتعاش:</strong> تمنحان الفم والأنفاس نظافة وانتعاشاً تدوم طوال اليوم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الفموي فقط، تجنبي البلع.</li>
  <li>غير مناسب للأطفال دون 6 سنوات دون إشراف عائلي.</li>
  <li>في حال حدوث تهيج استشيري طبيب الأسنان.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لتبييض الأسنان وإزالة البقع الصفراء والانتعاش.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كولجيت (Colgate)</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم والأسنان / معاجين كولجيت للتبييض وحماية الأسنان {volume_ar}</td></tr>
  <tr><th>نوع المنتج</th><td>معجون أسنان طبي لتبييض الأسنان وتقوية الميناء والانتعاش ({volume_ar})</td></tr>
  <tr><th>الحجم/الوزن</th><td>{volume_ar}</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الأسنان واللثة</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان بيضاء ناصعة، ناعمة، محمية من التسوس ومفعمة بـ {variant_ar}</td></tr>
  <tr><th>الملمس</th><td>معجون/جل ناعم رغوي ببلورات دقيقة</td></tr>
  <tr><th>العطر</th><td>عطر {variant_ar} الفواح المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>بلورات التبييض الدقيقة، فلوريد الصوديوم، حبيبات الانتعاش</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة / المملكة المتحدة / الإمارات</td></tr>
  <tr><th>الشركة المصنعة</th><td>Colgate-Palmolive Company</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون والأطفال (من 6 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد بلورات التبييض الدقيقة والفلوريد في كولجيت ({variant_ar})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج معجون كولجيت للتبييض مشكلة اصفرار الأسنان، بقع القهوة والشاي، تراكم البلاك، ورائحة الفم الكريهة.</p>

<h3>لماذا تنجح تقنية بلورات التبييض الدقيقة؟</h3>
<p>لأن البلورات الدقيقة تذيل البقع السطحية الخفيفة دون التأثير على كرات البنية البروتينية للميناء أو إحداث تآكل.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنظيف مرتين يومياً بالفرشاة لمدة دقيقتين:</strong> يمنع تراكم تصبغات الأطعمة والمشروبات.<br>
2. <strong>المضمضة بالماء بعد تناول القهوة أو الشاي:</strong> يقلل ترسب صبغات التانين على السن.<br>
3. <strong>الاستخدام المنتظم:</strong> يضمن بياضاً مستمراً وابتسامة مشرقة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "معاجين التبييض تزيل طبقة الميناء وتسبب حساسيتها."<br>
<strong>الحقيقة:</strong> كولجيت التبييض مصمم بمعامل حت آمن (RDA) يلمع السطح دون إيذاء أو ترقيق طبقة الميناء.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تزيل المواد التلميعية الدقيقة (Silica Micro-Particles) التصبغات العضوية اللاصقة في غشاء السن البيوكيميائي (Pellicle Layer).</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو معجون أسنان تخصصي للتبييض من كولجيت يزيل التصبغات الصفراء ويقوي الميناء بـ {variant_ar} ({volume_ar})."),
        (f"ما هي فوائد بلورات التبييض الدقيقة والفلوريد وعطر {variant_ar}؟", f"تلمع البللورات التصبغات، يقوي الفلوريد الميناء، ويمنح عطر {variant_ar} أنفاساً معطرة ونظيفة."),
        ("هل يبيض الأسنان ويزيل بقع القهوة والشاي؟", "نعم، مثبت سريرياً في تبييض الأسنان وإزالة التصبغات السطحية بفاعلية."),
        (f"ما حجم العبوة؟", f"تأتي بسعة {volume_ar}."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية بحجم البازلاء، نظفي لمدة دقيقتين مرتين يومياً وابصقي المعجون."),
        ("هل هو آمن على ميناء الأسنان؟", "نعم، آمن ومختبر سريرياً بتلميع لطيف لا يخدش الميناء."),
        (f"أين صُنع معجون كولجيت؟", "صُنع بواسطة Colgate-Palmolive العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كولجيت لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {variant_ar} المنعش الفواح."),
        ("هل يطرد رائحة الفم الكريهة؟", "نعم، يمنح الفم والأنفاس انتعاشاً عاطراً يمتد لساعات طويلة."),
        (f"هل العبوة {volume_ar} تكفي للاستخدام اليومي؟", "نعم، تكفي لعدة أسابيع من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كولجيت العلامة الأولى عالمياً في العناية بالأسنان؟", "نعم، Colgate علامة عالمية رائدة وأسطورية في العناية بالفم."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل يناسب الأطفال فوق 6 سنوات؟", "نعم، يناسب الأطفال من 6 سنوات تحت إشراف الوالدين."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يعالج البلاك وتراكمات الجير البسيطة؟", "نعم، ينظف البلاك ويقلل تكون الجير المترسب."),
        ("هل يحمي اللثة من التهابات البكتيريا؟", "نعم، ينظف خط اللثة ويحميها من البكتيريا."),
        ("هل يمنح شعوراً بالنظافة الفائقة؟", "نعم، يترك الفم والأسنان بنظافة وبياض فائقين."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الاستخدام اليومي المستمر؟", "نعم، مصمم للاستخدام اليومي الدائم كمعجون أسنان رئيسي."),
        ("هل يعيد البياض الطبيعي للابتسامة؟", "نعم، يعيد البياض المشرق الطبيعي للأسنان."),
        ("هل يصلح هدية ممتازة ضمن العناية الفموية؟", "نعم، منتج طبي ممتاز لا غنى عنه."),
        ("هل يمنح انتعاشاً يدوم طوال اليوم؟", "نعم، يترك الفم مفعماً بالانتعاش والنظافة."),
        ("هل تتوفر منه أنواع وأحجام أخرى لدى كولجيت؟", "نعم، تتوفر خيارات واسعة لدى Colgate.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic advanced whitening toothpaste from Colgate formulated to brighten teeth, remove stubborn coffee and tea surface stains, and deliver all-day oral freshness. Built upon Micro-Whitening Crystals, active Sodium Fluoride cavity defense, and invigorating {variant_en} fresh particles.</p>
<p>Colgate Toothpaste {variant_en} safely polishes teeth without scratching enamel, removes yellow discoloration and bacterial plaque, and reinforces tooth enamel against dietary acids, leaving your teeth spotlessly white, smooth, protected, and radiant all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Spotless Whitening & Yellow Stain Removal:</strong> Safe polishing with smooth micro-crystals.</li>
  <li><strong>Vibrant Long-Lasting {variant_en} Freshness:</strong> Eliminates bad breath imparting clean fresh breath.</li>
  <li><strong>Enamel Strengthening & Cavity Protection with Fluoride:</strong> Shields teeth against acid erosion.</li>
  <li><strong>Gum & Oral Health Protection:</strong> Effectively cleanses interdental spaces and bacterial plaque.</li>
  <li><strong>#1 Globally Recommended Whitening Brand from Colgate:</strong> Noticeable clinical whitening results from first weeks.</li>
  <li><strong>Generous {volume_en} Tube:</strong> Excellent volume for daily family dental routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a pea-sized amount of Colgate toothpaste onto a suitable toothbrush.</li>
  <li><strong>Step 2:</strong> Brush teeth thoroughly in gentle circular motions for two minutes twice daily.</li>
  <li><strong>Step 3:</strong> Spit out toothpaste and rinse mouth with water without swallowing (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Micro-Whitening Crystals & Sodium Fluoride:</strong> Polish tooth enamel surface micro-pores while defending against cavity decay.</li>
  <li><strong>Cleansing Agents & Freshness Particles:</strong> Leave mouth and breath intensely clean and refreshed all day.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external oral use only; do not swallow.</li>
  <li>Not suitable for children under 6 years without adult supervision.</li>
  <li>If irritation occurs, consult your dentist.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for tooth whitening, yellow stain removal, and long-lasting freshness.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Colgate</td></tr>
  <tr><th>Category</th><td>Oral Care / Colgate Whitening & Cavity Protection Toothpastes {volume_en}</td></tr>
  <tr><th>Product Type</th><td>Tooth Whitening, Micro-Crystal Polishing & Fluoride Toothpaste ({volume_en})</td></tr>
  <tr><th>Volume/Weight</th><td>{volume_en}</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Teeth & Gums Types</td></tr>
  <tr><th>Finish</th><td>Spotlessly white, polished, cavity-protected teeth with {variant_en} fresh breath</td></tr>
  <tr><th>Texture</th><td>Smooth micro-crystal polishing paste/gel</td></tr>
  <tr><th>Fragrance</th><td>Invigorating {variant_en} mint fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Micro-Whitening Crystals, Sodium Fluoride, Freshness Particles</td></tr>
  <tr><th>Country of Origin</th><td>USA / UK / UAE</td></tr>
  <tr><th>Manufacturer</th><td>Colgate-Palmolive Company</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 6+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Silica Micro-Particle Pellicle Stain Cleansing & Enamel Safety</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves yellowing teeth, coffee and tea surface stains, bacterial plaque, and bad breath.</p>

<h3>Why choose Colgate Whitening Toothpaste?</h3>
<p>Micro-polishing Silica particles remove extrinsic organic pellicle stains safely within low RDA abrasivity limits preserving enamel matrix integrity.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a specialized whitening toothpaste from Colgate for yellow stain removal and {variant_en} fresh breath ({volume_en})."),
        (f"What are the benefits of Micro-Whitening Crystals, Fluoride, and {variant_en}?", f"Micro-crystals polish surface stains, Fluoride strengthens enamel, and {variant_en} delivers fresh breath."),
        ("Does it whiten teeth and remove coffee/tea stains?", "Yes, clinically proven to whiten teeth and remove surface stains effectively."),
        (f"What volume is contained in this tube?", f"{volume_en}."),
        ("How do I use it correctly?", "Apply pea-sized amount, brush for 2 minutes twice daily, spit and rinse."),
        ("Is it safe for tooth enamel?", "Yes, safe and clinically tested for gentle non-scratching enamel polishing."),
        ("Where is Colgate Toothpaste manufactured?", "By Colgate-Palmolive Company."),
        ("How do I verify authenticity at Ekleel Abha?", "All Colgate products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", f"Invigorating {variant_en} fresh mint aroma."),
        ("Does it eliminate bad breath?", "Yes, delivers long-lasting fresh breath for hours."),
        (f"Does the {volume_en} tube last long?", "Yes, lasts weeks of regular daily use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Colgate a global #1 oral care brand?", "Yes, Colgate is a world-renowned leader in dental care."),
        ("How many times daily?", "Twice daily (morning & night)."),
        ("Is it suitable for children aged 6+?", "Yes, suitable for children aged 6+ under adult supervision."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it clean plaque and tartar buildup?", "Yes, cleans plaque and reduces tartar accumulation."),
        ("Does it protect gums against bacteria?", "Yes, cleanses gumline protecting against bacterial irritation."),
        ("Does it leave a clean refreshed mouth feel?", "Yes, leaves mouth and teeth feeling intensely clean."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for daily continuous use?", "Yes, designed for continuous daily use as a main toothpaste."),
        ("Does it restore natural smile brightness?", "Yes, restores natural tooth cleanliness and bright smile."),
        ("Is it a practical oral care product?", "Yes, an indispensable dental product."),
        ("Does it provide all-day freshness?", "Yes, leaves mouth feeling fresh and clean all day."),
        ("Are other variants available?", "Yes, wide variety of Colgate variants available.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Colgate",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. معجون أسنان للتبييض وتقوية الميناء بـ {variant_ar} من كولجيت. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Colgate whitening & enamel protection toothpaste with {variant_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1983():
    return _make_colgate_whitening(
        pid=1983, gtin="6920354824845",
        ar_name="معجون اسنان ماكس وايت من كولوجيت 100مل",
        en_name="Colgate Max White Toothpaste 100ml",
        variant_ar="ماكس وايت بلورات التبييض (Max White)", variant_en="Max White Crystals",
        volume_ar="100 مل", volume_en="100ml",
        tags_ar=["كولجيت", "ماكس_وايت", "تبييض_الأسنان", "معجون_كولجيت", "إكليل_أبها"],
        tags_en=["colgate", "max_white", "teeth_whitening", "colgate_toothpaste", "ekleel_abha"]
    )


def create_product_1984():
    return _make_colgate_whitening(
        pid=1984, gtin="6920354821660",
        ar_name="معجون اسنان باليمون من كولوجيت 75مل",
        en_name="Colgate Lemon Toothpaste 75ml",
        variant_ar="انتعاش الليمون والنعناع (Lemon Mint)", variant_en="Lemon Mint Refreshment",
        volume_ar="75 مل", volume_en="75ml",
        tags_ar=["كولجيت", "كولجيت_ليمون", "انتعاش_الليمون", "معجون_أسنان", "إكليل_أبها"],
        tags_en=["colgate", "lemon_colgate", "lemon_mint", "colgate_toothpaste", "ekleel_abha"]
    )


def create_product_1985():
    return _make_colgate_whitening(
        pid=1985, gtin="6281001101192",
        ar_name="معجون اسنان ادفانس وايت من كولوجيت 100مل",
        en_name="Colgate Advanced White Toothpaste 100ml",
        variant_ar="التبييض المتقدم لـ 14 يوماً (Advanced White)", variant_en="Advanced White",
        volume_ar="100 مل", volume_en="100ml",
        tags_ar=["كولجيت", "ادفانس_وايت", "تبييض_متقدم", "كولجيت_100مل", "إكليل_أبها"],
        tags_en=["colgate", "advanced_white", "whitening_toothpaste", "colgate_white", "ekleel_abha"]
    )


def _make_loreal_clay_mask(pid, gtin, ar_name, en_name, color_ar, color_en, clay_type_ar, clay_type_en, benefit_ar, benefit_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> قناع الطين النقي العلاجي الفاخر الأصيل من لوريال باريس الفرنسية المصمم خصيصاً لتنقية وتنظيف وتقشير وإعادة النضارة الفائقة لبشرة الوجه في 10 دقائق فقط. يرتكز هذا الماسك الأسطوري ({en_name}) على خليط الطين النقي الثلاثي (3 Pure Clays: Kaolin, Montmorillonite, Ghassoul) المدعم بخلاصة {clay_type_ar}.</p>
<p>يعمل قناع الطين {color_ar} من لوريال باريس على امتصاص الدهون الزائدة والزيوت المفرزة، تنقية المسام من الرؤوس السوداء والشوائب العميقة، و{benefit_ar}، ليترك بشرتك ناعمة كالحرير، مشدودة، ناصعة النقاء، ومفعمة بالنضارة والتوهج من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنقية عميقة وتنظيف للمسام في 10 دقائق:</strong> يزيل السموم والأوساخ والزيوت الزائدة.</li>
  <li><strong>خليط الطين النقي الثلاثي (كاولين، مونتموريلونيت، غاسول):</strong> يجمع بين الامتصاص والترميم والتنعيم.</li>
  <li><strong>{benefit_ar}:</strong> يمنح الوجه إشراقة وتوهجاً ناصعاً دون جفاف.</li>
  <li><strong>تقليل الرؤوس السوداء واللمعان الدهني:</strong> يترك البشرة مات وغير لامعة بالدهون.</li>
  <li><strong>اختبر جلدياً لحماية وسلامة البشرة:</strong> قوام كريمي طيني ناعم يسهل غسله بالماء.</li>
  <li><strong>عبوة زجاجية فاخرة سعة 50 مل:</strong> حجم ممتازة يكفي لـ 10-12 تطبيقاً علاجياً.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> اغسلي الوجه بغسول مناسب وجففي البشرة برفق.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وزعي طبقة رقيقة متساوية من قناع الطين {color_ar} على كامل الوجه مع تجنب منطقتي العينين والشفاه.</li>
  <li><strong>الخطوة الثالثة (الانتظار والغسيل):</strong> اتركيه يجف لمدة 10-15 دقيقة ثم اشطفي جيداً بالماء الدافئ (يُستعمل 2-3 مرات أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>3 أنواع من الطين النقي الطبيعي (Kaolin, Montmorillonite, Ghassoul):</strong> تمتص الدهون وتنظف المسام وتنعيم البشرة.</li>
  <li><strong>خلاصة {clay_type_ar}:</strong> {benefit_ar} وتغذي خلايا الجلد بالنضارة والترميم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه فقط.</li>
  <li>تجنبي التلامس مع العينين والشفاه واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن {ar_name} لتنقية البشرة وتنظيف المسام وإعادة التوهج والنضارة في 10 دقائق.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لوريال باريس (L'Oréal Paris)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / أقنعة ومقشرات الطين النقي من لوريال باريس 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>قناع طين نقي ثلاثي لتنقية الوجه وتنظيف المسام ({color_ar}) 50ml</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (خصيصاً الدهنية والمختلطة والباهتة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة كالحرير، ناصعة النقاء، منتعشة، خالية من الدهون والرؤوس السوداء</td></tr>
  <tr><th>الملمس</th><td>قوام كريمي طيني ناعم فائق السلاسة</td></tr>
  <tr><th>العطر</th><td>عطر لوريال الطيني الناعم المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>3 أنواع طين نقي (كاولين، مونتموريلونيت، غاسول)، خلاصة {clay_type_ar}</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>L'Oréal Paris France</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد الطين النقي الثلاثي وخلاصة {clay_type_ar} في قناع لوريال ({color_ar})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج قناع الطين من لوريال باريس مشكلة انسداد المسام، الزيوت الزائدة واللمعان، البشرات الباهتة والمجهدة، والرؤوس السوداء.</p>

<h3>لماذا تنجح تركيبة الطين النقي الثلاثي؟</h3>
<p>لأن دمج الكاولين (امتصاص الدهون)، المونتموريلونيت (تصفية الشوائب)، والغاسول (تنعيم وإشعاع) يمنح تنقية متكاملة في 10 دقائق.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام 2-3 مرات أسبوعياً:</strong> يحافظ على مسام نظيفة وغير منسدة.<br>
2. <strong>عدم ترك الماسك حتى يتشقق شديداً:</strong> الغسيل بعد 10-15 دقيقة فور جفافه يمنع جفاف البشرة.<br>
3. <strong>التكميل بمرطب خفيف بعد الغسل:</strong> يحفظ التوازن المائي للبشرة المفتحة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "أقنعة الطين تسبب جفافاً شديداً للبشرة."<br>
<strong>الحقيقة:</strong> لوريال باريس صممت قناع الطين بتركيبة كريمية ملطفة تنقي دون انتزاع الترطيب الطبيعي.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تمتلك جزيئات السليكات والألومينا في الطين شحنات كهربائية سالبة تجذب كاتيونات الدهون والسموم الموجبة وتدمصها كيميائياً (Adsorption).</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو قناع طين نقي ثلاثي علاج لتنقية الوجه وتنظيف المسام وإعادة التوهج من لوريال باريس بـ {clay_type_ar} (50 مل)."),
        (f"ما هي فوائد الطين النقي الثلاثي وخلاصة {clay_type_ar}؟", f"يمتص الطين الثلاثي الدهون والشوائب، بينما تعمل خلاصة {clay_type_ar} على {benefit_ar}."),
        ("هل ينظف المسام ويزيل الرؤوس السوداء واللمعان في 10 دقائق؟", "نعم، مثبت سريرياً في تنقية المسام وإزالة الزيوت الزائدة في 10 دقائق فقط."),
        (f"ما حجم العبوة؟", "تأتي بعبوة زجاجية فاخرة بسعة 50 مل (تكفي 10-12 مرة)."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي طبقة رقيقة على وجه نظيف، دعيها 10-15 دقيقة ثم اشطفي بالماء الدافئ 2-3 مرات أسبوعياً."),
        ("هل يسبب جفافاً للبشرة؟", "لا، تركيبة طينية كريمية ملطفة تنقي البشرة دون جفاف."),
        ("أين صُنع قناع لوريال باريس؟", "صُنع في فرنسا بواسطة L'Oréal Paris France."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لوريال لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", "عطر لوريال الطيني الناعم المنعش الفاخر."),
        ("هل يترك البشرة ناعمة ومشدودة؟", "نعم، يترك البشرة ناعمة كالحرير، مشدودة ومفعمة بالنضارة."),
        ("هل يناسب البشرة الدهنية والمختلطة؟", "نعم، ممتاز جداً للبشرة الدهنية والمختلطة والباهتة."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف مع إغلاق الغطاء جيداً."),
        ("كم مرة أسبوعياً؟", "2-3 مرات أسبوعياً."),
        ("هل لوريال باريس العلامة الأولى عالمياً في التجميل؟", "نعم، L'Oréal Paris العلامة الفرنسية الأيقونية الأولى عالمياً في التجميل."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب للرجال والنساء من 16 سنة."),
        ("هل يقلل مظهر المسام الواسعة؟", "نعم، ينظف المسام وينشط مرونتها ليقلل مظهر المسام الواسعة."),
        ("هل يمكن تطبيقه مع أقنعة الطين الأخرى (Multi-Masking)؟", "نعم، ممتاز لتقنية تقنيات الماسكات المتعددة حسب مناطق الوجه."),
        ("هل ينشطف بالماء الدافئ بسهولة؟", "نعم، ينشطف بالماء الدافئ بسلاسة ناعمة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يمنح الوجه إشراقة وتوهجاً ناصعاً؟", "نعم، يعيد النضارة والتوهج الطبيعي للوجه من التطبيق الأول."),
        ("هل يزيل السموم والتراكمات اليومية؟", "نعم، يزيل ترسبات التلوث والسموم من عمق المسام."),
        ("هل يصلح هدية راقية للعناية بالبشرة؟", "نعم، عبوة زجاجية فاخرة خيار ممتاز للهدايا."),
        ("هل ينعم ملمس الوجه الخشن؟", "نعم، يقشر خلايا السطح الميتة لينعم الوجه."),
        ("هل تتوفر ألوان أخرى من أقنعة الطين لدى لوريال؟", "نعم، تتوفر التشكيلة الملونة كاملة من أقنعة الطين لدى لوريال.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic luxury purifying clay mask treatment from L'Oréal Paris France formulated to purify, cleanse, exfoliate, and restore radiant glow to facial skin in just 10 minutes. Built upon 3 Pure Clays (Kaolin, Montmorillonite, Ghassoul) enriched with {clay_type_en} extract.</p>
<p>L'Oréal Paris Pure Clay {color_en} Mask absorbs excess sebum and oil, unblocks pores from deep impurities and blackheads, and {benefit_en}, leaving your skin touchably silky soft, toned, spotlessly clear, and luminous from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>10-Minute Deep Pore Purification & Detox:</strong> Removes toxins, dirt, and excess sebum.</li>
  <li><strong>3 Pure Clay Blend (Kaolin, Montmorillonite, Ghassoul):</strong> Combines oil absorption, mineral repair, and skin refining.</li>
  <li><strong>{benefit_en}:</strong> Imparts a radiant luminous glow without drying skin.</li>
  <li><strong>Blackhead & Shine Reduction:</strong> Leaves skin matte, clean, and non-greasy.</li>
  <li><strong>Dermatologically Tested:</strong> Creamy smooth clay formula easily rinsed with warm water.</li>
  <li><strong>Luxury 50ml Glass Jar Container:</strong> Excellent volume providing 10-12 therapeutic mask applications.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Wash face with a suitable cleanser and pat dry gently.</li>
  <li><strong>Step 2 (Apply):</strong> Apply an even thin layer of {color_en} clay mask over face avoiding eye and lip areas.</li>
  <li><strong>Step 3 (Rinse):</strong> Allow to dry for 10-15 minutes, then rinse thoroughly with warm water (use 2-3 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>3 Pure Clays (Kaolin, Montmorillonite, Ghassoul):</strong> Absorb sebum, unclog pores, and refine skin texture.</li>
  <li><strong>{clay_type_en} Extract:</strong> {benefit_en} while nourishing facial skin cells.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial application only.</li>
  <li>Avoid contact with eyes and lips; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every woman seeking {en_name} to purify skin, unclog pores, and restore radiant glow in 10 minutes.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>L'Oréal Paris</td></tr>
  <tr><th>Category</th><td>Skincare / L'Oréal Paris Pure Clay Facial Masks 50ml</td></tr>
  <tr><th>Product Type</th><td>3 Pure Clay Purifying & Glow Restoring Facial Mask ({color_en}) 50ml</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Oily, Combination & Dull Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, spotlessly purified, refreshed & non-greasy matte skin</td></tr>
  <tr><th>Texture</th><td>Smooth creamy clay texture gliding effortlessly</td></tr>
  <tr><th>Fragrance</th><td>Luxury fresh L'Oréal clay fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>3 Pure Clays (Kaolin, Montmorillonite, Ghassoul), {clay_type_en} Extract</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>L'Oréal Paris France</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of 3 Pure Clays Ionic Cation Adsorption & {clay_type_en} Epidermal Radiance</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves clogged pores, excess sebum shine, dull tired skin, blackheads, and uneven skin texture.</p>

<h3>Why choose L'Oréal Pure Clay Mask?</h3>
<p>Blending Kaolin (sebum absorption), Montmorillonite (impurity clearance), and Ghassoul (refining) delivers comprehensive 10-minute facial purification.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a 3 Pure Clay purifying facial mask treatment from L'Oréal Paris with {clay_type_en} for deep pore detox and radiance (50ml)."),
        (f"What are the benefits of 3 Pure Clays and {clay_type_en} extract?", f"3 Pure Clays absorb oil and impurities, while {clay_type_en} extract works to {benefit_en}."),
        ("Does it clean pores and remove blackheads/shine in 10 minutes?", "Yes, clinically proven to purify pores and eliminate excess oil in just 10 minutes."),
        ("What volume is contained in this jar?", "50ml luxury glass jar (10-12 applications)."),
        ("How do I use it correctly?", "Apply thin layer on clean face, leave 10-15 minutes, rinse with warm water 2-3 times weekly."),
        ("Does it dry out the skin?", "No, soothing creamy clay formula purifies skin without stripping moisture."),
        ("Where is L'Oréal Paris Pure Clay Mask manufactured?", "In France by L'Oréal Paris France."),
        ("How do I verify authenticity at Ekleel Abha?", "All L'Oréal products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", "Luxury fresh L'Oréal clay signature fragrance."),
        ("Does it leave skin soft and toned?", "Yes, leaves skin silky soft, toned, and glowing."),
        ("Is it suitable for oily and combination skin?", "Yes, excellent for oily, combination, and dull skin types."),
        ("How should I store it?", "In a cool, dry place with lid tightly closed."),
        ("How many times weekly?", "2-3 times weekly."),
        ("Is L'Oréal Paris a global #1 beauty brand?", "Yes, L'Oréal Paris is the world's premier iconic French beauty brand."),
        ("Is the glass jar recyclable?", "Yes."),
        ("Is it suitable for men and women?", "Yes, suitable for men and women aged 16+."),
        ("Does it minimize visible pores?", "Yes, cleanses pores and restores elasticity minimizing visible pore appearance."),
        ("Can it be used for Multi-Masking?", "Yes, excellent for multi-masking targeted facial zones."),
        ("Does it rinse off easily with warm water?", "Yes, rinses off smoothly with warm water."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it impart a luminous radiant glow?", "Yes, restores vibrant natural radiance from first application."),
        ("Does it remove daily pollution and toxins?", "Yes, purifies environmental pollution and toxins deep inside pores."),
        ("Is it a luxury skincare gift?", "Yes, elegant glass jar makes a great skincare gift."),
        ("Does it smooth rough facial skin?", "Yes, exfoliates dead surface skin cells smoothing texture."),
        ("Are other color clay masks available from L'Oréal?", "Yes, the full range of L'Oréal Pure Clay masks is available.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "L'Oréal Paris",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. قناع الطين النقي الثلاثي من لوريال باريس لتنقية الوجه وتنظيف المسام بـ 10 دقائق. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. L'Oréal Paris 3 Pure Clay 10-minute purifying and radiance facial mask. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1986():
    return _make_loreal_clay_mask(
        pid=1986, gtin="3600523516926",
        ar_name="قناع الطين النقي الازرق  من لوريال باريس - 50 مل",
        en_name="L'Oréal Paris Pure Clay Blue Mask - 50ml",
        color_ar="الأزرق (Blue Marine)", color_en="Blue Marine",
        clay_type_ar="الطحالب البحرية الزرقاء (Marine Algae)", clay_type_en="Blue Marine Algae",
        benefit_ar="تصفية البشرة وإزالة الشوائب وتنظيف المسام المحتقنة", benefit_en="clarify skin, remove impurities, and clear congested pores",
        tags_ar=["لوريال", "قناع_الطين_الازرق", "طين_لوريال", "ماسك_الطحالب_البحرية", "إكليل_أبها"],
        tags_en=["loreal", "pure_clay_blue", "loreal_mask", "marine_algae_mask", "ekleel_abha"]
    )


def create_product_1987():
    return _make_loreal_clay_mask(
        pid=1987, gtin="3600523306183",
        ar_name="قناع الطين النقي الاحمر من لوريال باريس - 50 مل",
        en_name="L'Oréal Paris Pure Clay Red Mask - 50ml",
        color_ar="الأحمر (Red Algae Exfoliating)", color_en="Red Algae Exfoliating",
        clay_type_ar="الطحالب الحمراء المقشرة (Red Algae Extract)", clay_type_en="Exfoliating Red Algae",
        benefit_ar="تقشير البشرة وتنعيم المسام وإعادة التوهج المشرق", benefit_en="exfoliate skin cells, smooth pores, and restore luminous radiance",
        tags_ar=["لوريال", "قناع_الطين_الاحمر", "تقشير_الطين", "طين_لوريال_احمر", "إكليل_أبها"],
        tags_en=["loreal", "pure_clay_red", "exfoliating_clay_mask", "loreal_red_mask", "ekleel_abha"]
    )


print("Loaded all 5 Batch 54 builders complete")
