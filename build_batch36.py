import json, os

def _make_beesline_deodorant_50ml(pid, gtin, ar_name, en_name, scent_ar, scent_en, meta_ar_suffix, meta_en_suffix, tags_ar, tags_en, unique_ar_note, unique_en_note, extra_feature_ar="", extra_feature_en=""):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> مزيل عرق بيزلين الطبيعي الفاخر المصمم لتأمين جفاف تام وحماية مضادة للبكتيريا والروائح الكريهة لـ 48 ساعة. {unique_ar_note} يرتكز هذا المزيل على حجر الشبة الطبيعي (Alum Rock)، صمغ النحل النقي (Propolis)، واللوميسكين المبيض.</p>
<p>يعمل مزيل بيزلين على الحد من نمو البكتيريا المسببة للروائح، امتصاص العرق الزائد، وتفتيح آمن للإبطين، ليترك المنطقة جافة، معطرة بعطر {scent_ar}، ومحمية طوال اليوم.{extra_feature_ar}</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية 48 ساعة من العرق والروائح:</strong> صمغ النحل وحجر الشبة يقضيان على البكتيريا.</li>
  <li><strong>تفتيح وتوحيد لون بشرة الإبطين باللوميسكين:</strong> يزيل التصبغات الناتجة عن الاحتكاك.</li>
  <li><strong>عطر {scent_ar} المميز الفواح:</strong> يمنح انتعاشاً ورائحة ناعمة طوال اليوم.</li>
  <li><strong>تطهير وتهدئة بـ صمغ النحل النقي:</strong> يحمي البشرة من البكتيريا والالتهابات.</li>
  <li><strong>خالي 100% من ألومنيوم كلوروهيدرات، الكحول، والبارابين:</strong> آمن للبشرة الحساسة.</li>
  <li><strong>عبوة مدمجة سعة 50 مل:</strong> حجم ممتاز للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> نظف منطقة الإبطين بالماء والصابون وجففها جيداً.</li>
  <li><strong>الخطوة الثانية:</strong> مرر البكرة 1-2 مرة على بشرة الإبط الجافة.</li>
  <li><strong>الخطوة الثالثة:</strong> دع السائل يجف ثوانٍ قبل ارتداء الملابس (يُستعمل مرة يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>حجر الشبة الطبيعي وصمغ النحل:</strong> يمتصان العرق ويقضيان على البكتيريا طبيعياً.</li>
  <li><strong>اللوميسكين:</strong> يفتّح التصبغات الداكنة بشكل آمن ومستمر.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على بشرة الإبطين الجافة فقط.</li>
  <li>لا يوضع على الجلد المصاب بجروح مفتوحة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن مزيل عرق بيزلين بعطر {scent_ar} 50 مل للحماية اليومية وتفتيح الإبطين.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / مزيلات العرق الرول اون من بيزلين بعطر {scent_ar} 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>مزيل عرق رول اون طبيعي بعطر {scent_ar} ومبيض للإبطين (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الإبطين (بما في ذلك البشرة الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>إبطان جافتان ومنعشتان بعطر {scent_ar} وخاليتان من الروائح والتصبغات</td></tr>
  <tr><th>الملمس</th><td>سائل رول اون خفيف ينفذ فورياً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر {scent_ar} المميز</td></tr>
  <tr><th>المكونات النشطة</th><td>حجر الشبة (Alum Rock)، صمغ النحل (Propolis)، لوميسكين</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد عطر {scent_ar} وحجر الشبة وصمغ النحل في مزيل بيزلين</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مزيل بيزلين بعطر {scent_ar} مشكلة رائحة العرق اليومية، اسمرار الإبطين، والحاجة إلى عطر مميز ومنعش.</p>

<h3>لماذا تنجح تركيبة حجر الشبة وصمغ النحل واللوميسكين؟</h3>
<p>لأن حجر الشبة يضيق المسام الغدية السطحية طبيعياً، صمغ النحل يطهر البكتيريا، واللوميسكين يثبط الميلامين بأمان.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق صباحاً على جلد جاف نظيف:</strong> أفضل وقت للاستعمال بعد الاستحمام مباشرةً.<br>
2. <strong>الانتظار ثوانٍ قبل اللبس:</strong> لضمان الجفاف التام ومنع اللزوجة.<br>
3. <strong>الاستمرار المنتظم:</strong> يضمن الحماية الدائمة والتفتيح التدريجي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مزيلات العرق الطبيعية أقل فعالية من المزيلات الكيميائية."<br>
<strong>الحقيقة:</strong> مزيل بيزلين الطبيعي مثبت سريرياً في الفعالية المعادلة لمزيلات الألومنيوم دون مخاطرها الصحية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تشكّل أيونات بوتاسيوم ألوم من حجر الشبة معقدات بروتينية على سطح الغدد العرقية تضيق المسام مؤقتاً بشكل آمن.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو مزيل عرق رول اون طبيعي من بيزلين بعطر {scent_ar} وبحجر الشبة واللوميسكين لجفاف 48 ساعة وتفتيح الإبطين."),
        ("ما هي فوائد حجر الشبة وصمغ النحل واللوميسكين؟", "يمتص حجر الشبة العرق، يطهر صمغ النحل البشرة، ويفتّح اللوميسكين التصبغات."),
        ("هل يوفر حماية 48 ساعة من العرق والروائح؟", "نعم، مثبت سريرياً لـ 48 ساعة."),
        ("ما حجم العبوة؟", "تأتي لعلبة رول اون سعة 50 مل."),
        ("كيف يُستخدم؟", "مرر البكرة 1-2 مرة على الإبط الجاف، دع يجف ثوانٍ ثم البس."),
        ("هل خالٍ من الكحول والبارابين والألومنيوم الكيميائي؟", "نعم، خالي 100%."),
        ("أين صُنع؟", "في لبنان بواسطة مختبرات بيزلين."),
        ("كيف أتحقق من أصالته؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100%."),
        ("هل يترك آثاراً على الملابس؟", "لا، شفاف لا يترك أي أثر."),
        (f"ما رائحة مزيل بيزلين بعطر {scent_ar}؟", f"يتميز بعطر {scent_ar} المميز الفواح."),
        ("هل يهدئ التهيج بعد الحلاقة؟", "نعم، صمغ النحل يهدئ التهيج."),
        ("هل 50 مل يكفي للاستخدام اليومي؟", "نعم، يكفي لعدة أسابيع من الاستخدام اليومي."),
        ("كيف أحفظ العبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب الرجال والنساء؟", "مناسب لجميع الفئات من سن 12 سنة."),
        ("هل العبوة محكمة؟", "نعم، بغطاء محكم."),
        ("كم مرة يومياً؟", "مرة واحدة يومياً."),
        ("هل يمنع البكتيريا؟", "نعم، صمغ النحل وحجر الشبة يمنعان البكتيريا."),
        ("هل آمن للبشرة الحساسة؟", "نعم، فورمولا طبيعية آمنة."),
        ("هل يفتّح الإبطين؟", "نعم، اللوميسكين يفتّح تدريجياً."),
        ("هل يمنح انتعاشاً طوال اليوم؟", f"نعم، عطر {scent_ar} يضمن الانتعاش."),
        ("هل قابل لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة."),
        ("هل يجف سريعاً؟", "نعم، خلال ثوانٍ."),
        ("هل يترك الجلد طرياً؟", "نعم، يترك الجلد طرياً ومريحاً."),
        ("هل يصلح للسفر؟", "نعم، حجم مدمج مثالي."),
        ("هل يتوفر بسعر ممتاز؟", "نعم، بقيمة ممتازة لدى إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is a natural Beesline roll-on deodorant providing 48-hour total dryness and antibacterial protection. {unique_en_note} Formulated with natural Alum Rock, Propolis, and Lumiskin whitening compound.</p>
<p>Beesline Deodorant limits odor-causing bacteria, absorbs excess sweat, and provides safe underarm brightening, delivering complete dryness, {scent_en} fresh scent, and smooth armpits all day.{extra_feature_en}</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>48-Hour Sweat & Odor Protection:</strong> Propolis and Alum Rock eliminate bacteria.</li>
  <li><strong>Underarm Brightening with Lumiskin:</strong> Fades dark friction hyperpigmentation.</li>
  <li><strong>Signature {scent_en} Fragrance:</strong> Delivers refreshing all-day freshness.</li>
  <li><strong>Purifying Propolis Defense:</strong> Protects skin from bacteria and inflammation.</li>
  <li><strong>100% Free of Aluminum Chlorohydrate, Alcohol & Parabens:</strong> Safe for sensitive skin.</li>
  <li><strong>Compact 50ml Roll-On Bottle:</strong> Ideal daily-use size.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Cleanse underarms with soap and water, pat dry.</li>
  <li><strong>Step 2:</strong> Roll applicator 1-2 times over dry underarm skin.</li>
  <li><strong>Step 3:</strong> Allow to dry for seconds before dressing (use once daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Alum Rock & Propolis:</strong> Absorb sweat and naturally eliminate odor bacteria.</li>
  <li><strong>Lumiskin:</strong> Safely and progressively brightens dark underarm spots.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical dry underarm skin application only.</li>
  <li>Do not apply onto open wounds or broken skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Those seeking Beesline's {scent_en} 50ml Roll-On Deodorant for daily protection and underarm brightening.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Personal Care / Beesline {scent_en} Scented Roll-On Deodorants 50ml</td></tr>
  <tr><th>Product Type</th><td>Natural {scent_en} Scented & Brightening Roll-On Deodorant (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Underarm Skin Types (Including Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Dry, brightened, {scent_en}-fresh, odor-free armpits</td></tr>
  <tr><th>Texture</th><td>Smooth lightweight fast-drying roll-on fluid</td></tr>
  <tr><th>Fragrance</th><td>Signature {scent_en} fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Alum Rock, Propolis, Lumiskin</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Alum Rock Astringency & Lumiskin Melanin Suppression in Beesline {scent_en}</h2>

<h3>What problem does this solve?</h3>
<p>Beesline {scent_en} Roll-On resolves daily underarm odor, dark hyperpigmentation, and the desire for a distinctive {scent_en} fresh scent.</p>

<h3>Why choose Beesline {scent_en} Roll-On?</h3>
<p>Potassium alum ions naturally tighten sweat gland pores while Propolis provides antibacterial defense and Lumiskin safely inhibits melanin production.</p>"""

    en_faqs_data = [
        (f"What is the {en_name}?", f"It is a natural Beesline roll-on deodorant with {scent_en} scent, Alum Rock, and Lumiskin for 48-hour protection and underarm brightening."),
        ("What are the benefits of Alum Rock, Propolis, and Lumiskin?", "Alum Rock absorbs sweat, Propolis purifies skin, and Lumiskin brightens dark underarm spots."),
        ("Does it provide 48-hour protection?", "Yes, clinically proven for 48-hour total dryness and odor protection."),
        ("What volume is this?", "It comes in a compact 50ml roll-on bottle."),
        ("How do I use it correctly?", "Roll 1-2 times onto clean, dry underarm skin, allow to dry, and dress."),
        ("Is it free of aluminum chlorohydrate, alcohol, and parabens?", "Yes, 100% free."),
        ("Where is it manufactured?", "In Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity?", "All Beesline products at Ekleel Abha are 100% original."),
        ("Does it leave marks on clothes?", "No, invisible fluid absorbs instantly."),
        (f"What scent does the {en_name} have?", f"Features the signature {scent_en} fragrance."),
        ("Does it soothe post-shaving irritation?", "Yes, Propolis calms skin irritation after shaving."),
        ("Is the 50ml bottle ideal for daily use?", "Yes, compact bottle lasts weeks of daily use."),
        ("How should I store it?", "Store in a cool, dry place."),
        ("Is it for men and women?", "Suitable for all ages aged 12+."),
        ("Is the bottle leak-proof?", "Yes, secure screw-top cap."),
        ("How often daily?", "Once daily is recommended."),
        ("Does it stop bacteria?", "Yes, Propolis and Alum Rock prevent bacterial growth."),
        ("Is it safe for sensitive skin?", "Yes, gentle natural formula."),
        ("Does Lumiskin brighten underarms?", "Yes, Lumiskin progressively brightens underarm spots."),
        (f"Does it provide all-day {scent_en} freshness?", f"Yes, signature {scent_en} ensures all-day freshness."),
        ("Is the bottle recyclable?", "Yes, eco-friendly."),
        ("Does it dry quickly?", "Yes, in seconds."),
        ("Does it leave skin soft?", "Yes, touchably soft."),
        ("Is it good for travel?", "Yes, compact size ideal."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Beesline",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. {meta_ar_suffix} أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. {meta_en_suffix} 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1892():
    return _make_beesline_deodorant_50ml(
        pid=1892, gtin="5281018567975",
        ar_name="مزيل عرق  عناية التفتيح خصم 50% على الحبة الثانية من بيزلين",
        en_name="Beesline Whitening Care Deodorant - 50% Off on the Second Piece",
        scent_ar="عناية التفتيح",
        scent_en="Whitening Care",
        meta_ar_suffix="مزيل عرق بيزلين عناية التفتيح بخصم 50% على الحبة الثانية.",
        meta_en_suffix="Beesline Whitening Care Deodorant with 50% off on the second piece.",
        tags_ar=["بيزلين", "مزيل_عرق_تفتيح", "خصم_50", "عناية_الإبط", "إكليل_أبها"],
        tags_en=["beesline", "whitening_deodorant", "50off_deal", "whitening_care", "ekleel_abha"],
        unique_ar_note="يتميز هذا العرض الرائع بخصم 50% على الحبة الثانية من مزيل عرق بيزلين عناية التفتيح مما يجعله أفضل قيمة لتفتيح الإبطين.",
        unique_en_note="This exceptional deal includes 50% off the second piece of Beesline Whitening Care Deodorant making it the best value for underarm brightening.",
        extra_feature_ar=" يُعد هذا العرض الاقتصادي المثالي لمن يريد الاستمرار في روتين تفتيح الإبطين بأقل تكلفة.",
        extra_feature_en=" This deal is ideal for continuous whitening routine at the best possible cost."
    )


def create_product_1893():
    return _make_beesline_deodorant_50ml(
        pid=1893, gtin="5281018088159",
        ar_name="مزيل عرق مدعم بالفضة  للنساء من بيزلين 50 مل",
        en_name="Beesline Silver-Infused Deodorant for Women - 50ml",
        scent_ar="الفضة النانوية النسائي الأنثوي",
        scent_en="Silver-Infused Feminine",
        meta_ar_suffix="مزيل عرق نسائي من بيزلين بالفضة النانوية لحماية 48 ساعة وتفتيح الإبطين.",
        meta_en_suffix="Women's Beesline Silver-Infused roll-on for 48-hour protection and brightening.",
        tags_ar=["بيزلين_للنساء", "مزيل_عرق_فضة_نساء", "فضة_نانوية", "تفتيح_الإبط", "إكليل_أبها"],
        tags_en=["beesline_women", "silver_women_deodorant", "nano_silver", "whitening_deodorant", "ekleel_abha"],
        unique_ar_note="يمتاز مزيل عرق بيزلين بالفضة للنساء بأيونات الفضة النانوية المضادة للبكتيريا المصممة خصيصاً لبشرة المرأة الرقيقة.",
        unique_en_note="Beesline Silver-Infused Women's Deodorant features Nano Silver Ions specifically formulated for delicate female underarm skin."
    )


def create_product_1894():
    return _make_beesline_deodorant_50ml(
        pid=1894, gtin="5281018003152",
        ar_name="مزيل عرق بعطر الورد من بيزلين50مل",
        en_name="Beesline Rose Fragrance Deodorant - 50ml",
        scent_ar="الورد الجوري الطبيعي",
        scent_en="Natural Damask Rose",
        meta_ar_suffix="مزيل عرق بيزلين بعطر الورد الجوري الطبيعي لجفاف تام وتفتيح الإبطين 50 مل.",
        meta_en_suffix="Beesline Natural Damask Rose roll-on for total dryness and underarm brightening 50ml.",
        tags_ar=["بيزلين", "مزيل_عرق_ورد", "عطر_الورد", "تفتيح_الإبط", "إكليل_أبها"],
        tags_en=["beesline", "rose_deodorant", "damask_rose", "whitening_deodorant", "ekleel_abha"],
        unique_ar_note="يمتاز مزيل عرق بيزلين بعطر الورد الجوري الطبيعي الأنثوي الراقي الذي يجمع بين العناية الطبية وجمال عطر الورد الأبدي.",
        unique_en_note="Beesline Rose Deodorant features the timeless natural Damask Rose fragrance combining medical skincare with elegant feminine rose perfumery."
    )


def create_product_1895():
    return _make_beesline_deodorant_50ml(
        pid=1895, gtin="5281018003879",
        ar_name="مزيل عرق  عودعربي من بيزلين 50مل",
        en_name="Beesline Arabian Oud Roll-On Deodorant - 50ml",
        scent_ar="العود العربي الأصيل الفاخر",
        scent_en="Authentic Arabian Oud",
        meta_ar_suffix="مزيل عرق بيزلين بعطر العود العربي الأصيل لجفاف تام وتفتيح الإبطين 50 مل.",
        meta_en_suffix="Beesline Authentic Arabian Oud roll-on for total dryness and underarm brightening 50ml.",
        tags_ar=["بيزلين", "مزيل_عرق_عود", "عود_عربي", "تفتيح_الإبط", "إكليل_أبها"],
        tags_en=["beesline", "arabian_oud_deodorant", "oud_rollOn", "whitening_deodorant", "ekleel_abha"],
        unique_ar_note="يمتاز مزيل عرق بيزلين بعطر العود العربي الأصيل الفاخر الذي يجسّد روح التراث العربي الأصيل بتقنية المزيل الطبيعي الحديثة.",
        unique_en_note="Beesline Arabian Oud Deodorant embodies authentic Arab heritage with an opulent Oud fragrance combined with modern natural deodorant technology."
    )


def create_product_1896():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>معجون أسنان الأطفال دنتسيمو من عمر (+6 سنوات) (Dentissimo Kids Toothpaste 6+ Years)</strong> معجون الأسنان الطبي المتخصص المصنوع بتركيبة دقيقة للأطفال في مرحلة الأسنان الدائمة من عمر 6 سنوات فما فوق. يرتكز هذا المعجون الفاخر (Dentissimo Kids Toothpaste 6+ Years) على الفلوريد عالي الجودة (High-Quality Fluoride)، خلاصة النعناع الخفيفة اللطيفة، والكالسيوم المعزز لبنيان الأسنان الدائمة.</p>
<p>يعمل معجون دنتسيمو للأطفال 6 سنوات+ على تقوية مينا الأسنان الدائمة وحمايتها من التسوس، منع تكوّن الجير وطبقة البلاك، وتبييض وتلميع أسنان الأطفال الصغار، ليترك الأسنان ناصعة البياض، الفم منتعشاً، والطفل مبتسماً بثقة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تقوية وحماية مينا الأسنان الدائمة بالفلوريد عالي الجودة:</strong> يحمي من التسوس ويقوي المينا في مرحلة نمو الأسنان الدائمة.</li>
  <li><strong>منع تكوّن الجير والبلاك والبكتيريا الضارة:</strong> يحافظ على صحة اللثة وسلامة الأسنان الدائمة لأطفال 6 سنوات+.</li>
  <li><strong>تبييض وتلميع لطيف لأسنان الأطفال:</strong> يزيل الاصفرار ويعطي الأسنان بياضاً طبيعياً ناصعاً.</li>
  <li><strong>نكهة نعناع خفيفة محببة للأطفال:</strong> تجعل تجربة التنظيف ممتعة ومشجعة للأطفال على الاستمرار.</li>
  <li><strong>تركيبة دنتسيمو الطبية المجربة طبياً ودنداناً:</strong> آمنة ومعتمدة لاستخدام الأطفال من 6 سنوات فأكبر.</li>
  <li><strong>عبوة أنبوبية ملونة جذابة للأطفال:</strong> تصميم يحبه الأطفال ويشجعهم على تنظيف أسنانهم يومياً.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الكمية):</strong> ضعي كمية بحجم حبة البازلاء من معجون دنتسيمو للأطفال على فرشاة أسنان ناعمة.</li>
  <li><strong>الخطوة الثانية (التنظيف):</strong> دلّكي أسنان الطفل بحركات دائرية لطيفة لمدة دقيقتين كاملتين.</li>
  <li><strong>الخطوة الثالثة (الشطف):</strong> اشطفي الفم بالماء وشجعي الطفل على المضمضة (يُستعمل مرتين يومياً: صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الفلوريد عالي الجودة (High-Fluoride):</strong> يعيد تمعدن مينا الأسنان الدائمة ويحميها من التسوس.</li>
  <li><strong>الكالسيوم والنعناع الخفيف:</strong> يعززان بنيان الأسنان الدائمة ويمنحان نضارة وانتعاشاً محبباً للأطفال.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>مخصص للأطفال من عمر 6 سنوات فما فوق فقط (ليس لما دون 6 سنوات).</li>
  <li>يُشرف ولي الأمر على تنظيف أسنان الأطفال دون سن 8 سنوات.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال الصغار وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل طفل من عمر 6 سنوات فما فوق يحتاج إلى معجون أسنان دنتسيمو الطبي الأصلي لتقوية وحماية أسنانه الدائمة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>دنتسيمو (Dentissimo)</td></tr>
  <tr><th>الفئة</th><td>صحة الأسنان / معاجين أسنان دنتسيمو الطبية للأطفال من 6 سنوات+</td></tr>
  <tr><th>نوع المنتج</th><td>معجون أسنان طبي للأطفال من 6 سنوات+ بالفلوريد وكالسيوم لتقوية الأسنان الدائمة</td></tr>
  <tr><th>الحجم/الوزن</th><td>حسب مواصفات العبوة</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>أسنان الأطفال الدائمة (من 6 سنوات فما فوق)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان دائمة ناصعة البياض، مقواة بالمينا، مقاومة للتسوس، وفم منتعش</td></tr>
  <tr><th>الملمس</th><td>معجون كريمي ناعم بنكهة نعناع خفيفة محببة للأطفال</td></tr>
  <tr><th>العطر</th><td>نكهة النعناع الخفيفة الطبيعية المحببة للأطفال</td></tr>
  <tr><th>المكونات النشطة</th><td>فلوريد عالي الجودة، كالسيوم، خلاصة النعناع</td></tr>
  <tr><th>بلد المنشأ</th><td>سويسرا (Switzerland)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Dentissimo Switzerland</td></tr>
  <tr><th>الفئة العمرية</th><td>الأطفال من 6 سنوات فما فوق</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الفلوريد والكالسيوم في معجون دنتسيمو للأطفال 6+ (Dentissimo Kids 6+)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج معجون دنتسيمو للأطفال 6 سنوات+ مشكلة تسوس الأسنان الدائمة، تكوّن الجير والبلاك، والاصفرار في مرحلة الأسنان الدائمة الحرجة للأطفال.</p>

<h3>لماذا تنجح تركيبة الفلوريد والكالسيوم لأطفال 6+؟</h3>
<p>لأن الفلوريد يعيد تمعدن مينا الأسنان الدائمة ويثبط أحماض بكتيريا التسوس، بينما يدعم الكالسيوم بنيان الأسنان الدائمة في مرحلة النمو.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنظيف مرتين يومياً لمدة دقيقتين:</strong> صباحاً بعد الإفطار ومساءً قبل النوم.<br>
2. <strong>الإشراف على الأطفال دون 8 سنوات:</strong> للتأكد من عدم ابتلاع المعجون.<br>
3. <strong>الزيارة الدورية لطبيب الأسنان:</strong> كل 6 أشهر لفحص الأسنان الدائمة النامية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الفلوريد في معاجين الأطفال ضار بصحتهم."<br>
<strong>الحقيقة:</strong> تركيزات الفلوريد في معاجين دنتسيمو 6+ معايرة بعناية ومعتمدة من منظمة الصحة العالمية لسلامة الأطفال.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تستبدل أيونات الفلورايد مجموعات الهيدروكسيل في هيدروكسيباتيت المينا مكونةً فلورأباتيت أقوى وأكثر مقاومة لأحماض بكتيريا التسوس.</p>"""

    faqs = [
        ("ما هو معجون أسنان الأطفال دنتسيمو من عمر +6 سنوات؟", "هو معجون أسنان طبي متخصص من دنتسيمو بالفلوريد والكالسيوم لتقوية وحماية أسنان الأطفال الدائمة من عمر 6 سنوات+."),
        ("ما هي فوائد الفلوريد والكالسيوم والنعناع الخفيف؟", "يقوي الفلوريد المينا ويمنع التسوس، يدعم الكالسيوم الأسنان الدائمة، وتمنح نكهة النعناع الخفيف انتعاشاً محبباً للأطفال."),
        ("هل يقي من تسوس الأسنان الدائمة لأطفال 6+؟", "نعم، مثبت سريرياً في تقوية مينا الأسنان الدائمة والحماية من التسوس لأطفال 6 سنوات فأكبر."),
        ("ما هو عمر الاستخدام الصحيح؟", "مخصص للأطفال من عمر 6 سنوات فما فوق فقط."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية حبة البازلاء على فرشاة ناعمة، دلّكي 2 دقيقة بحركات دائرية، اشطفي واضمضضي مرتين يومياً."),
        ("هل تركيبة الفلوريد آمنة وطبياً مجربة؟", "نعم، تركيبة معيّرة طبياً ومعتمدة من منظمة الصحة العالمية لسلامة الأطفال."),
        ("ما هو بلد صنع معجون دنتسيمو للأطفال 6+؟", "صُنع بفخر في سويسرا بواسطة Dentissimo Switzerland."),
        ("كيف أتأكد من أصالة المنتج لدى إكليل أبها؟", "جميع منتجات دنتسيمو لدى إكليل أبها أصلية 100% من الوكيل المعتمد."),
        ("هل نكهة النعناع خفيفة ومقبولة للأطفال؟", "نعم، نكهة نعناع خفيفة لطيفة خصيصاً للأطفال دون حدة أو لسعة."),
        ("هل يبيّض ويلمّع أسنان الأطفال؟", "نعم، يزيل الاصفرار ويمنح الأسنان الدائمة بياضاً طبيعياً ناصعاً."),
        ("هل يمنع الجير والبلاك؟", "نعم، يمنع تراكم الجير وطبقة البلاك على أسنان الأطفال الدائمة."),
        ("هل العبوة آمنة ومصممة للأطفال؟", "نعم، عبوة أنبوبية ملونة جذابة تصميمها مناسب للأطفال."),
        ("كيف أحتفظ بالمعجون؟", "يُحفظ في مكان بارد وجاف بعيداً عن الحرارة."),
        ("هل يمنح الطفل فماً منتعشاً؟", "نعم، يترك الفم منتعشاً وأسنان ناعمة نظيفة."),
        ("هل يناسب الأطفال بعمر 6-12 سنة؟", "نعم، مصمم خصيصاً لأسنان الأطفال الدائمة من 6 سنوات وما فوق."),
        ("كم مرة يُفضل استخدامه يومياً؟", "مرتين يومياً: صباحاً ومساءً لمدة دقيقتين."),
        ("هل يُشرف ولي الأمر أثناء التنظيف؟", "نعم، يُشرف ولي الأمر على الأطفال دون 8 سنوات."),
        ("هل يناسب الأطفال الذين يبدأون باستخدام الفلوريد؟", "نعم، مناسب لأطفال 6+ في مرحلة الأسنان الدائمة."),
        ("هل هو معجون الأطفال الأكثر طلباً من دنتسيمو؟", "نعم، Dentissimo Kids 6+ أبرز وأشهر معاجين الأطفال من دنتسيمو."),
        ("هل يشجع الأطفال على التنظيف اليومي؟", "نعم، نكهته الخفيفة وعبوته الملونة تشجع الأطفال على تنظيف أسنانهم."),
        ("هل آمن إذا ابتلع الطفل كمية صغيرة؟", "كميات بحبة البازلاء آمنة، لكن يُنصح بتجنب الابتلاع والمضمضة."),
        ("هل يمنع التسوس في الأسنان الدائمة الجديدة؟", "نعم، الفلوريد يمنع التسوس في الأسنان الدائمة منذ ظهورها."),
        ("هل يناسب الأطفال الذين يرتدون تقويم الأسنان؟", "نعم، مناسب للأطفال مرتدي التقويم مع التنظيف حول الأسلاك."),
        ("هل يصلح هدية صحية للأطفال؟", "نعم، هدية صحية مثالية لأطفال 6+ تدعم صحة أسنانهم."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Dentissimo Kids Toothpaste (6+ Years)</strong> is a specialized medical toothpaste formulated precisely for children in the permanent teeth stage aged 6 years and above. Formulated with High-Quality Fluoride, gentle Mint extract, and Calcium for strengthening permanent teeth.</p>
<p>Dentissimo Kids Toothpaste 6+ strengthens and protects permanent tooth enamel from cavities, prevents tartar and plaque formation, and whitens and polishes children's teeth, leaving teeth sparkling white, mouth refreshed, and children smiling confidently all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Permanent Enamel Strengthening & Cavity Protection with High-Quality Fluoride:</strong> Protects against cavities during the critical permanent teeth stage.</li>
  <li><strong>Tartar, Plaque & Bacteria Prevention:</strong> Maintains gum health and permanent tooth integrity for ages 6+.</li>
  <li><strong>Gentle Whitening & Polishing:</strong> Removes discoloration for naturally bright permanent teeth.</li>
  <li><strong>Child-Friendly Mild Mint Flavor:</strong> Makes cleaning fun and encourages daily brushing habits.</li>
  <li><strong>Dentissimo Medical Formula, Dentally & Clinically Tested:</strong> Safe and approved for children aged 6+.</li>
  <li><strong>Colorful, Child-Appealing Tube Design:</strong> Designed to inspire children to brush daily.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Amount):</strong> Apply a pea-sized amount of Dentissimo Kids toothpaste onto a soft toothbrush.</li>
  <li><strong>Step 2 (Clean):</strong> Brush teeth in gentle circular motions for a full 2 minutes.</li>
  <li><strong>Step 3 (Rinse):</strong> Rinse mouth with water and encourage gargling (use twice daily: morning and evening).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>High-Quality Fluoride:</strong> Remineralizes permanent tooth enamel and inhibits decay-causing bacterial acids.</li>
  <li><strong>Calcium & Gentle Mint:</strong> Strengthen permanent teeth and impart child-friendly freshness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For children aged 6 years and above only (not for children under 6).</li>
  <li>Adult supervision recommended for children under 8 years.</li>
  <li>Keep out of reach of young children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Children aged 6+ needing Dentissimo's original medical toothpaste for strengthening and protecting permanent teeth.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Dentissimo</td></tr>
  <tr><th>Category</th><td>Dental Health / Dentissimo Medical Kids Toothpastes for Ages 6+</td></tr>
  <tr><th>Product Type</th><td>Medical Fluoride & Calcium Kids Toothpaste for Permanent Teeth Ages 6+</td></tr>
  <tr><th>Volume/Weight</th><td>As per packaging specifications</td></tr>
  <tr><th>Skin/Hair Type</th><td>Children's Permanent Teeth (Ages 6+)</td></tr>
  <tr><th>Finish</th><td>Sparkling white, strengthened enamel, cavity-resistant permanent teeth & fresh mouth</td></tr>
  <tr><th>Texture</th><td>Smooth creamy paste with mild child-friendly mint flavor</td></tr>
  <tr><th>Fragrance</th><td>Child-friendly mild natural mint flavor</td></tr>
  <tr><th>Active Ingredients</th><td>High-Quality Fluoride, Calcium, Mint Extract</td></tr>
  <tr><th>Country of Origin</th><td>Switzerland</td></tr>
  <tr><th>Manufacturer</th><td>Dentissimo Switzerland</td></tr>
  <tr><th>Age Group</th><td>Children Ages 6 and Above</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Fluoride Enamel Fluorapatite Formation & Calcium Permanent Tooth Support</h2>

<h3>What problem does this solve?</h3>
<p>Dentissimo Kids Toothpaste 6+ resolves permanent tooth decay, tartar and plaque buildup, and discoloration during the critical permanent teeth growth stage.</p>

<h3>Why choose Dentissimo Kids Toothpaste 6+?</h3>
<p>Fluoride ions replace hydroxyl groups in enamel hydroxyapatite forming stronger fluorapatite resistant to bacterial decay acids, while Calcium supports permanent tooth development.</p>"""

    en_faqs = [
        ("What is Dentissimo Kids Toothpaste (6+ Years)?", "It is a specialized medical toothpaste from Dentissimo with Fluoride and Calcium for strengthening and protecting permanent teeth in children aged 6+."),
        ("What are the benefits of Fluoride, Calcium, and mild Mint?", "Fluoride strengthens enamel and prevents cavities, Calcium supports permanent teeth, and mild Mint provides child-friendly freshness."),
        ("Does it protect permanent teeth from cavities?", "Yes, clinically proven to strengthen permanent tooth enamel and prevent cavities for children aged 6+."),
        ("What age group is it for?", "Designed specifically for children aged 6 years and above only."),
        ("How do I use it correctly?", "Apply pea-sized amount on a soft brush, brush 2 minutes in circular motions, rinse and gargle twice daily."),
        ("Is the Fluoride formula medically safe and approved?", "Yes, WHO-approved medically calibrated fluoride formula safe for children 6+."),
        ("Where is Dentissimo Kids 6+ manufactured?", "Proudly manufactured in Switzerland by Dentissimo Switzerland."),
        ("How do I verify authenticity at Ekleel Abha?", "All Dentissimo products at Ekleel Abha are 100% original from certified distributors."),
        ("Is the mint flavor mild and acceptable for children?", "Yes, specially formulated mild mint flavor without sharpness or burning."),
        ("Does it whiten and polish children's teeth?", "Yes, removes discoloration and gives permanent teeth a naturally bright white shine."),
        ("Does it prevent tartar and plaque?", "Yes, prevents tartar and plaque accumulation on children's permanent teeth."),
        ("Is the packaging safe and child-friendly?", "Yes, colorful appealing tube design encouraging children to brush."),
        ("How should I store the tube?", "Store in a cool, dry place away from heat."),
        ("Does it leave children's mouth fresh?", "Yes, leaves mouth refreshed and teeth touchably clean."),
        ("Is it suitable for children aged 6-12 years?", "Yes, specifically designed for permanent teeth of children aged 6 and above."),
        ("How often should children use it?", "Twice daily: morning and evening for 2 minutes."),
        ("Should adults supervise brushing?", "Yes, adult supervision recommended for children under 8 years."),
        ("Is it suitable for children starting fluoride use?", "Yes, ideal for children 6+ entering the permanent teeth stage."),
        ("Is it Dentissimo's most popular kids toothpaste?", "Yes, Dentissimo Kids 6+ is the flagship children's toothpaste by Dentissimo."),
        ("Does it encourage children to brush daily?", "Yes, mild flavor and colorful tube encourage daily brushing habits."),
        ("Is it safe if a child swallows a small amount?", "Pea-sized amounts are safe but encourage spitting and rinsing."),
        ("Does it prevent cavities in new permanent teeth?", "Yes, Fluoride prevents cavities in permanent teeth from the moment they erupt."),
        ("Is it suitable for children with braces?", "Yes, suitable for children wearing braces with proper brushing around brackets."),
        ("Is it a good healthy gift for children?", "Yes, ideal healthy gift for children 6+ supporting their dental health."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1896",
        "sku": "EK-1896",
        "gtin": "7640162322409",
        "brand": "Dentissimo",
        "ar": {
            "title": "معجون أسنان الأطفال دنتسيمو من عمر (+6 سنوات)",
            "meta_title": "معجون أسنان دنتسيمو للأطفال 6+ سنوات | إكليل أبها",
            "meta_description": "اشتري معجون أسنان الأطفال دنتسيمو (6+ سنوات). معجون طبي بالفلوريد والكالسيوم لتقوية وحماية الأسنان الدائمة لأطفال 6+. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["دنتسيمو", "معجون_أسنان_أطفال", "6_سنوات_فأكبر", "فلوريد_أطفال", "إكليل_أبها"]
        },
        "en": {
            "title": "Dentissimo Kids Toothpaste (6+ Years)",
            "meta_title": "Dentissimo Kids Toothpaste 6+ Years | Ekleel Abha",
            "meta_description": "Buy original Dentissimo Kids Toothpaste (6+ Years). Medical Fluoride & Calcium toothpaste for permanent teeth protection. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["dentissimo", "kids_toothpaste", "6_plus_years", "fluoride_toothpaste", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 36 builders complete")
