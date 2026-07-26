import json, os

def create_product_1887():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>صابون تفتيح البشرة من بيزلين 85جم (Beesline Skin Whitening Soap 85g)</strong> صابون التفتيح الطبي الكلاسيكي الأصيل من بيزلين المصمم لتفتيح وتوحيد لون جميع مناطق الجسم والوجه وإزالة التصبغات الداكنة بكل أمان وفعالية. يرتكز هذا الصابون الفاخر (Beesline Skin Whitening Soap 85g) على مركب اللوميسكين المبيض (Lumiskin)، صمغ النحل النقي (Propolis)، وخلاصة فيتامين C المجدد للخلايا.</p>
<p>يعمل صابون بيزلين لتفتيح البشرة على إزالة بقع الشمس والتصبغات الداكنة، تقشير خلايا الجلد الميتة بلطف شديد، وتغذية وتجديد بشرة الجسم والوجه بمضادات الأكسدة القوية، ليترك جسمك بشرة ناصعة، موحدة اللون، مشرقة، وأكثر حيوية من اليوم الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح شامل لجميع مناطق الجسم والوجه باللوميسكين:</strong> يوحد لون البشرة ويزيل التصبغات والبقع الداكنة.</li>
  <li><strong>تقشير لطيف لخلايا الجلد الميتة:</strong> يكشف طبقة بشرة جديدة أكثر إشراقاً وحيوية.</li>
  <li><strong>غني بفيتامين C ومضادات الأكسدة القوية:</strong> يجدد الخلايا ويمنع تشكّل التصبغات مستقبلاً.</li>
  <li><strong>تطهير وتهدئة بـ صمغ النحل النقي (Propolis):</strong> يطهر المسام ويهدئ الجلد المتهيج.</li>
  <li><strong>صابون طبي آمن خالٍ من الهيدروكينون والبارابين:</strong> تفتيح آمن دون أي مواد كيميائية ضارة.</li>
  <li><strong>عبوة 85 جم اقتصادية:</strong> تدوم عدة أشهر من الاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (البلل):</strong> بللي الجسم أو الوجه بالماء الفاتر لفتح المسام.</li>
  <li><strong>الخطوة الثانية (التغسيل):</strong> حركي صابونة بيزلين بين راحتي اليدين أو على ليفة حتى تتكون رغوة كثيفة.</li>
  <li><strong>الخطوة الثالثة (المسح):</strong> دلكي الجسم والوجه بالرغوة بحركات دائرية خفيفة لـ 30-60 ثانية ثم اشطفي بالماء البارد (يُستعمل يومياً صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركب اللوميسكين وفيتامين C:</strong> يثبطان إنزيم التايروسينيز ويفتحان البقع التصبغية الداكنة.</li>
  <li><strong>صمغ النحل ومضادات الأكسدة:</strong> يطهران المسام ويحميان الجلد من التلف الجذري الحر.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي لتنظيف وتفتيح بشرة الجسم والوجه فقط.</li>
  <li>تجنبي التلامس مع العينين ويُستعمل الماء الفاتر للشطف الفوري.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من تصبغات الجسم والوجه الداكنة وتبحث عن صابون بيزلين لتفتيح البشرة 85جم لنتائج مشرقة وآمنة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / صابونات بيزلين الطبية لتفتيح الجسم والوجه 85جم</td></tr>
  <tr><th>نوع المنتج</th><td>صابونة طبية شاملة لتفتيح بشرة الجسم والوجه باللوميسكين وفيتامين C (85جم)</td></tr>
  <tr><th>الحجم/الوزن</th><td>85 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم والوجه (بما في ذلك البشرة ذات التصبغات)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناصعة، موحدة اللون، مشرقة، خالية من التصبغات والبقع الداكنة</td></tr>
  <tr><th>الملمس</th><td>صابونة صلبة تنتج رغوة لطيفة كثيفة للتنظيف والتفتيح</td></tr>
  <tr><th>العطر</th><td>عطر بيزلين الطبيعي المنعش والناعم</td></tr>
  <tr><th>المكونات النشطة</th><td>لوميسكين، فيتامين C، صمغ النحل (Propolis)، مضادات الأكسدة</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد اللوميسكين وفيتامين C في صابون بيزلين للتفتيح (Beesline Skin Whitening)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج صابون بيزلين لتفتيح البشرة مشكلة التصبغات الداكنة على الجسم والوجه، بقع الشمس، وعدم توحد لون البشرة عموماً.</p>

<h3>لماذا تنجح تركيبة اللوميسكين وفيتامين C للتفتيح؟</h3>
<p>لأن اللوميسكين يثبط مسار DAG-PKC للميلانين بأمان، بينما يثبط فيتامين C مباشرة إنزيم التايروسينيز ويعزز تجديد الكولاجين.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الغسل مرتين يومياً بماء فاتر ثم بارد:</strong> يفتح الماء الفاتر المسام ويغلقها البارد بعد التنظيف العميق.<br>
2. <strong>استخدام واقي شمس SPF 30+ بعد التنظيف:</strong> لمنع عودة التصبغات بعد التفتيح.<br>
3. <strong>تكمل الصابونة كريم بيزلين المبيض:</strong> الدمج مع كريم بيزلين للتفتيح يضاعف النتائج.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "صابون التفتيح يسبب رقة البشرة وحساسيتها الشديدة."<br>
<strong>الحقيقة:</strong> صابون بيزلين مصنوع من مكونات طبيعية آمنة باللوميسكين وفيتامين C دون هيدروكينون أو عوامل حمضية ضارة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يمنع مركب اللوميسكين تشكل ثنائي أسيل الجليسيرول الناقل لإشارات الميلانين، مما يؤدي إلى تقليل تدريجي وآمن للمنين الزائد.</p>"""

    faqs = [
        ("ما هو صابون تفتيح البشرة من بيزلين 85جم؟", "هو صابون طبيعي طبي من بيزلين باللوميسكين وفيتامين C وصمغ النحل لتفتيح وتوحيد لون بشرة الجسم والوجه 85 جم."),
        ("ما هي فوائد اللوميسكين وفيتامين C وصمغ النحل؟", "يثبط اللوميسكين الميلامين للتفتيح، يجدد فيتامين C الخلايا ويوحد اللون، ويطهر صمغ النحل المسام."),
        ("هل يفتّح التصبغات وبقع الشمس بسرعة؟", "نعم، مثبت سريرياً في التفتيح التدريجي لتصبغات الجسم والوجه مع الاستخدام المنتظم."),
        ("ما حجم الصابونة؟", "تأتي بوزن 85 جم."),
        ("كيف تُستخدم الصابونة بالشكل الصحيح؟", "بللي الجسم أو الوجه بالماء الفاتر، كوّني رغوة كثيفة وادلكي بحركات دائرية 30-60 ثانية ثم اشطفي بالماء البارد مرتين يومياً."),
        ("هل هي خالية من الهيدروكينون والبارابين؟", "نعم، تفتيح آمن خالٍ 100% من الهيدروكينون والبارابين."),
        ("ما هو بلد صنع صابون بيزلين لتفتيح البشرة؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% من الوكيل المعتمد."),
        ("هل تناسب جميع أنواع بشرة الجسم والوجه؟", "نعم، مناسبة لجميع أنواع البشرة بما في ذلك البشرة الدهنية والمختلطة."),
        ("ما هي رائحة صابون بيزلين للتفتيح؟", "يتميز بعطر بيزلين الطبيعي المنعش والناعم."),
        ("هل تنتج رغوة كثيفة وغنية؟", "نعم، تنتج رغوة لطيفة كثيفة تنظف المسام وتفتّح البشرة."),
        ("هل تقشّر خلايا الجلد الميتة بلطف؟", "نعم، تقشير لطيف يكشف طبقة بشرة جديدة أكثر إشراقاً."),
        ("كيف أحتفظ بالصابونة؟", "تُحفظ في مكان جاف بعيداً عن الرطوبة الزائدة."),
        ("هل يُفضل استخدامها صباحاً أو مساءً أو كلاهما؟", "يُستعمل مرتين يومياً صباحاً ومساءً لنتائج تفتيح أسرع."),
        ("هل تهدئ التهيج والاحمرار؟", "نعم، صمغ النحل يهدئ الالتهابات والاحمرار."),
        ("كم يستغرق التفتيح لرؤية نتائج واضحة؟", "تظهر نتائج التفتيح التدريجي خلال 4-6 أسابيع من الاستخدام المنتظم."),
        ("هل تمنع ظهور تصبغات جديدة؟", "يُفضل استخدام واقي الشمس بعدها لمنع عودة التصبغات."),
        ("هل تناسب المراهقين والبالغين؟", "نعم، مناسبة للمراهقين والبالغين من سن 12 سنة."),
        ("هل هي صابونة التفتيح الأكثر طلباً لبيزلين؟", "نعم، Skin Whitening Soap من أبرز وأشهر صابونات التفتيح من بيزلين."),
        ("هل تترك الجلد ناصعاً ومشرقاً بعد الغسيل؟", "نعم، تترك بشرة الجسم والوجه ناصعة ومشرقة وموحدة اللون."),
        ("هل صابونة 85 جم تدوم طويلاً؟", "نعم، صابونة صلبة 85 جم تدوم عدة أشهر من الاستخدام اليومي."),
        ("هل تحمي من أكسدة الشمس والتشيّخ؟", "نعم، مضادات الأكسدة تحمي من التلف الشمسي والتشيّخ المبكر."),
        ("هل تصلح كجزء من روتين العناية الشامل؟", "نعم، تكمل صابونة بيزلين مراحل التنظيف والتفتيح في الروتين اليومي."),
        ("هل تناسب الاستخدام على كامل الجسم؟", "نعم، مناسبة لتفتيح وتنظيف كامل الجسم والوجه."),
        ("هل تتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، تتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Skin Whitening Soap 85g</strong> is the original classic medical whitening soap from Beesline designed for comprehensive brightening and unifying of body and facial skin tone, safely removing dark hyperpigmentation. Formulated with Lumiskin, Propolis, and Vitamin C.</p>
<p>Beesline Skin Whitening Soap eliminates sun spots and dark hyperpigmentation, gently exfoliates dead skin cells, and nourishes body and facial skin with powerful antioxidants, leaving your skin touchably radiant, even-toned, and glowing from day one.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Comprehensive Body & Facial Brightening with Lumiskin:</strong> Unifies skin tone and removes dark spots.</li>
  <li><strong>Gentle Exfoliation of Dead Skin Cells:</strong> Reveals a brighter, more radiant skin layer.</li>
  <li><strong>Rich in Vitamin C & Antioxidants:</strong> Renews cells and prevents future hyperpigmentation.</li>
  <li><strong>Purifying Propolis Defense:</strong> Cleanses pores and soothes irritated skin.</li>
  <li><strong>Safe Medical Formula, Free of Hydroquinone & Parabens:</strong> Safe brightening without harmful chemicals.</li>
  <li><strong>Economical 85g Bar:</strong> Lasts months of daily continuous use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet body or face with warm water to open pores.</li>
  <li><strong>Step 2 (Lather):</strong> Work Beesline Whitening soap between palms until rich lather forms.</li>
  <li><strong>Step 3 (Cleanse):</strong> Massage lather onto body/face in circles for 30-60 seconds, rinse with cold water (use morning and evening).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Lumiskin & Vitamin C:</strong> Inhibit tyrosinase melanin synthesis and brighten dark spots.</li>
  <li><strong>Propolis & Antioxidants:</strong> Purify pores and protect against free radical damage.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body and facial skin cleansing and whitening only.</li>
  <li>Avoid eye contact; rinse immediately with warm water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with body or facial dark hyperpigmentation seeking Beesline's 85g Skin Whitening Soap for safe, effective brightening.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Skincare / Beesline Medical Body & Facial Whitening Soaps 85g</td></tr>
  <tr><th>Product Type</th><td>Medical Lumiskin & Vitamin C Comprehensive Body & Facial Whitening Soap (85g)</td></tr>
  <tr><th>Volume/Weight</th><td>85 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body & Facial Skin Types (Including Hyperpigmented Skin)</td></tr>
  <tr><th>Finish</th><td>Radiant, even-toned, brightened, spot-free body and facial skin</td></tr>
  <tr><th>Texture</th><td>Firm bar soap producing gentle rich brightening lather</td></tr>
  <tr><th>Fragrance</th><td>Fresh natural Beesline aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Lumiskin, Vitamin C, Propolis, Antioxidants</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Lumiskin DAG-PKC Melanin Inhibition & Vitamin C Tyrosinase Block</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Skin Whitening Soap resolves dark body and facial hyperpigmentation, sun spots, and uneven skin tone.</p>

<h3>Why choose Beesline Skin Whitening Soap?</h3>
<p>Lumiskin blocks diacylglycerol-PKC melanin signaling pathways safely, while Vitamin C directly inhibits tyrosinase and enhances collagen renewal.</p>"""

    en_faqs = [
        ("What is Beesline Skin Whitening Soap 85g?", "It is a natural medical whitening soap with Lumiskin, Vitamin C, and Propolis for brightening and unifying body and facial skin tone."),
        ("What are the benefits of Lumiskin, Vitamin C, and Propolis?", "Lumiskin inhibits melanin for brightening, Vitamin C renews cells, and Propolis purifies pores."),
        ("Does it brighten dark body and facial spots quickly?", "Yes, clinically proven to progressively brighten hyperpigmentation and unify skin tone."),
        ("What size is this soap bar?", "It comes in an 85g bar."),
        ("How do I use the soap correctly?", "Wet body/face, create lather, massage in circles for 30-60 seconds, rinse with cold water morning and evening."),
        ("Is it free of hydroquinone and parabens?", "Yes, 100% safe brightening formula free of hydroquinone, parabens, and harmful chemicals."),
        ("Where is Beesline Skin Whitening Soap manufactured?", "Proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Is it suitable for all skin types?", "Yes, suitable for all body and facial skin types."),
        ("What does Beesline Skin Whitening Soap smell like?", "Features a fresh, pleasant natural Beesline aroma."),
        ("Does it produce a rich lather?", "Yes, produces a gentle rich brightening lather."),
        ("Does it gently exfoliate dead skin cells?", "Yes, gentle exfoliation reveals a brighter, fresher skin layer."),
        ("How should I store the soap?", "Store in a dry place away from excess moisture."),
        ("Should I use it morning, evening, or both?", "Use twice daily, morning and evening, for faster brightening results."),
        ("Does it calm irritation and redness?", "Yes, Propolis soothes inflammation and redness."),
        ("How long does brightening take?", "Visible brightening results appear gradually within 4-6 weeks of regular use."),
        ("Does it prevent new dark spots?", "Apply sunscreen after use to prevent sun-induced spot recurrence."),
        ("Is it suitable for teens and adults?", "Yes, suitable for teens and adults aged 12+."),
        ("Is it Beesline's most iconic whitening soap?", "Yes, Skin Whitening Soap is among Beesline's most iconic and popular soaps."),
        ("Does it leave skin radiant after washing?", "Yes, leaves body and facial skin radiant, even-toned, and spot-free."),
        ("Does an 85g bar last a long time?", "Yes, a solid 85g bar lasts months of daily use."),
        ("Does it protect skin from sun damage and aging?", "Yes, antioxidants protect against UV-induced damage and premature aging."),
        ("Is it part of a complete skincare routine?", "Yes, complements Beesline whitening creams in a full body care routine."),
        ("Can it be used on the whole body?", "Yes, suitable for brightening and cleansing the entire body and face."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1887",
        "sku": "EK-1887",
        "gtin": "5281018003077",
        "brand": "Beesline",
        "ar": {
            "title": "صابون تفتيح البشرة من بيزلين 85جم",
            "meta_title": "صابون تفتيح البشرة بيزلين 85جم | إكليل أبها",
            "meta_description": "اشتري صابون تفتيح البشرة من بيزلين (85 جم). صابون طبي باللوميسكين وفيتامين C لتفتيح وتوحيد لون الجسم والوجه. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["بيزلين", "صابون_تفتيح_البشرة", "تفتيح_الجسم", "لوميسكين", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Skin Whitening Soap 85g",
            "meta_title": "Beesline Skin Whitening Soap 85g | Ekleel Abha",
            "meta_description": "Buy original Beesline Skin Whitening Soap (85g). Lumiskin & Vitamin C medical whitening bar for brightening body and facial skin. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["beesline", "skin_whitening_soap", "body_whitening", "lumiskin_soap", "ekleel_abha"]
        }
    }


def create_product_1888():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم إصلاح القدم من سيرافي 88 مل (CeraVe Renewing Foot Cream 88ml)</strong> كريم العناية الطبية الفائقة بالقدمين المصمم طبياً لإصلاح الجلد الجاف والمتشقق والخشن في منطقتي القدمين والكعبين. يرتكز هذا الكريم الطبي الفاخر من سيرافي (CeraVe Renewing Foot Cream 88ml) على تكنولوجيا السيراميدات الثلاثة (Ceramides 1, 3, 6-II)، حمض الساليسيليك المقشر اللطيف (Salicylic Acid)، وحمض اللاكتيك المجدد (Lactic Acid).</p>
<p>يعمل كريم سيرافي لإصلاح القدمين على تجديد وتنعيم جلد القدمين الجاف والمتشقق بتقنية MVE التدريجية الحصرية، تقشير الخلايا الميتة بلطف، واستعادة حاجز الجلد الطبيعي، ليترك قدمَيك ناعمتين كالحرير، مرطبتين لـ 24 ساعة، ومحميتين من الجفاف والتشقق المتكرر.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>إصلاح فائق للقدمين الجافة والمتشققة بتكنولوجيا MVE:</strong> يجدد حاجز الجلد ويمنح الترطيب العميق لـ 24 ساعة.</li>
  <li><strong>مدعم بالسيراميدات الثلاثة (Ceramides 1, 3, 6-II):</strong> تستعيد حاجز الدهون الطبيعي للجلد.</li>
  <li><strong>تقشير لطيف بـ حمض الساليسيليك وحمض اللاكتيك:</strong> يزيل خلايا القدمين الميتة والجلد المتقرن بكفاءة.</li>
  <li><strong>موصى به من قِبل أطباء الجلدية (Dermatologist Recommended):</strong> ابتُكر بتعاون مع أطباء الجلدية.</li>
  <li><strong>خالي 100% من العطور والبارابين:</strong> آمن للبشرة الحساسة لمنطقة القدمين.</li>
  <li><strong>عبوة مدمجة سعة 88 مل:</strong> كمية وافرة للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> اغسلي قدميك بالماء الفاتر والصابون وجففيهما جيداً قبل الاستعمال.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية مناسبة من كريم سيرافي لإصلاح القدمين على الكعبين والنعلين والأصابع.</li>
  <li><strong>الخطوة الثالثة (التدليك والشرب):</strong> دلكي القدمين بحركات دائرية لطيفة حتى امتصاص الكريم ويُفضل استعماله مساءً قبل النوم مع الجوارب.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>السيراميدات الثلاثة (Ceramides 1, 3, 6-II):</strong> تستعيد حاجز الجلد الطبيعي وتحفظ الترطيب العميق.</li>
  <li><strong>حمض الساليسيليك وحمض اللاكتيك:</strong> يقشران الخلايا الميتة والجلد المتقرن بلطف ودقة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة القدمين فقط.</li>
  <li>تجنبي التلامس مع العينين والجروح المفتوحة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من القدمين الجافتين والكعبين المتشققين ويبحث عن كريم سيرافي لإصلاح القدمين 88 مل الطبي الأصلي.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سيرافي (CeraVe)</td></tr>
  <tr><th>الفئة</th><td>العناية الطبية بالقدمين / كريمات سيرافي الطبية لإصلاح وترطيب القدمين 88ml</td></tr>
  <tr><th>نوع المنتج</th><td>كريم طبي فائق لإصلاح القدمين الجافة والمتشققة بالسيراميدات والأحماض (88ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>88 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جلد القدمين الجاف والمتشقق والمتقرن (بما في ذلك البشرة الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>قدمان ناعمتان كالحرير، مرطبتان لـ 24 ساعة، خاليتان من الجفاف والتشقق</td></tr>
  <tr><th>الملمس</th><td>كريم ثقيل سريع الامتصاص دون لزوجة مفرطة</td></tr>
  <tr><th>العطر</th><td>خالٍ من العطور (Fragrance-Free)</td></tr>
  <tr><th>المكونات النشطة</th><td>سيراميدات (1, 3, 6-II)، حمض الساليسيليك، حمض اللاكتيك</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة الأمريكية (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>CeraVe (L'Oréal Group)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد السيراميدات وتكنولوجيا MVE في كريم سيرافي للقدمين (CeraVe Foot Cream)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم سيرافي لإصلاح القدمين مشكلة جفاف القدمين الشديد، تشقق الكعبين المؤلم، وتقرن الجلد الميت في منطقتي الكعب والنعل.</p>

<h3>لماذا تنجح تكنولوجيا MVE وسيراميدات سيرافي؟</h3>
<p>لأن تقنية MVE (Multivesicular Emulsion) تطلق مكونات الترطيب تدريجياً طوال اليوم، بينما تستعيد السيراميدات الثلاثة حاجز الدهون الطبيعي للجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق مساءً مع الجوارب:</strong> ضعي الكريم ليلاً وارتدي جوارب قطنية للحصول على نتائج إصلاح عميق أسرع.<br>
2. <strong>النقع في الماء الدافئ:</strong> نقع القدمين 10 دقائق قبل تطبيق الكريم يفتح المسام ويعزز الامتصاص.<br>
3. <strong>الاستخدام المنتظم يومياً:</strong> يضمن تجديد حاجز الجلد منعاً للتشقق المتكرر.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "حمض الساليسيليك في كريمات القدمين يسبب حرقان وتهيج الجلد."<br>
<strong>الحقيقة:</strong> تركيز الساليسيليك في كريم سيرافي للقدمين متوازن بعناية ومجرب جلدياً لسلامة البشرة الحساسة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتكامل سيراميدات CeraVe مع الحمض الدهني والكوليسترول لاستعادة بنية ثلاثية الطبقات (Triple-Lamellar) لحاجز الجلد الطبيعي المفقود بالجفاف.</p>"""

    faqs = [
        ("ما هو كريم إصلاح القدم من سيرافي 88 مل؟", "هو كريم طبي فائق من سيرافي بالسيراميدات الثلاثة وحمض الساليسيليك لإصلاح وترطيب القدمين الجافة والمتشققة 88 مل."),
        ("ما هي فوائد السيراميدات وحمض الساليسيليك وحمض اللاكتيك؟", "تستعيد السيراميدات حاجز الجلد، يقشر الساليسيليك الخلايا الميتة، ويجدد اللاكتيك الجلد المتقرن."),
        ("هل يصلح القدمين الجافتين والكعبين المتشققين؟", "نعم، مثبت سريرياً في إصلاح جفاف القدمين وتشقق الكعبين بتكنولوجيا MVE والسيراميدات."),
        ("ما حجم العبوة؟", "تأتي بعبوة سعة 88 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية مناسبة على القدمين الجافتين، دلكي حتى الامتصاص، ويُفضل مساءً مع الجوارب القطنية."),
        ("هل هو موصى به من أطباء الجلدية؟", "نعم، طُور بتعاون مع أطباء الجلدية وموصى به طبياً."),
        ("ما هو بلد صنع كريم سيرافي للقدمين؟", "صُنع في الولايات المتحدة الأمريكية بواسطة مجموعة L'Oréal."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات سيرافي لدى إكليل أبها أصلية 100% من الوكيل المعتمد."),
        ("هل يناسب البشرة الحساسة؟", "نعم، خالٍ من العطور والبارابين وآمن للبشرة الحساسة."),
        ("ما رائحة كريم سيرافي للقدمين؟", "خالٍ من العطور تماماً (Fragrance-Free)."),
        ("هل يمتص بسرعة دون ترك لزوجة؟", "نعم، قوام خفيف يمتص بسرعة دون لزوجة مفرطة."),
        ("هل العبوة 88 مل تدوم طويلاً للاستخدام اليومي؟", "نعم، تكفي لعدة أشهر من الاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل يناسب الرجال والنساء؟", "مناسب لجميع الفئات العمرية للنساء والرجال من سن 12 سنة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة أنبوبية أنيقة محكمة الغلق."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل يومياً ويُفضل مساءً قبل النوم مع الجوارب للحصول على نتائج أسرع."),
        ("هل يمنع تكرار تشقق الكعبين؟", "نعم، الاستخدام المنتظم يحافظ على حاجز الجلد الطبيعي ويمنع الجفاف والتشقق المتكرر."),
        ("هل يناسب مرضى السكري الذين يعانون من جفاف القدمين؟", "يُنصح بمشورة الطبيب قبل استخدامه لمرضى السكري."),
        ("هل هو كريم القدمين الأكثر طلباً لسيرافي؟", "نعم، CeraVe Renewing Foot Cream كريم القدمين الأول والأكثر مبيعاً لسيرافي."),
        ("هل يمنح قدمين ناعمتين كالحرير؟", "نعم، يضمن قدمين ناعمتين وخاليتين من الجفاف والتشقق."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة قابلة لإعادة التدوير."),
        ("هل يعالج مشكلة الكعبين المتقرنة والسميكة؟", "نعم، حمض الساليسيليك واللاكتيك يقشران الجلد المتقرن والسميك تدريجياً."),
        ("هل يترك الجلد طرياً بعد الاستيقاظ؟", "نعم، مع ارتداء الجوارب القطنية يترك القدمين ناعمتين بشكل مدهش."),
        ("هل يساعد في التشقق العميق الدموي؟", "يعالج جفاف القدمين والتشقق العادي ويُنصح بمشورة الطبيب للتشقق الدموي العميق."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>CeraVe Renewing Foot Cream 88ml</strong> is a medical-grade foot care cream designed to repair dry, cracked, and rough skin on feet and heels. Formulated with three essential Ceramides (1, 3, 6-II), exfoliating Salicylic Acid, and renewing Lactic Acid.</p>
<p>CeraVe Foot Cream renews and softens dry, cracked foot skin using exclusive MVE technology, gently exfoliates dead skin cells, and restores the natural skin barrier, leaving your feet touchably smooth, moisturized for 24 hours, and protected from recurring dryness.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Superior Foot Repair with MVE Technology:</strong> Renews skin barrier and delivers deep 24-hour hydration.</li>
  <li><strong>Enriched with Three Ceramides (1, 3, 6-II):</strong> Restore natural lipid barrier of foot skin.</li>
  <li><strong>Gentle Exfoliation with Salicylic & Lactic Acid:</strong> Removes dead skin cells and calluses effectively.</li>
  <li><strong>Dermatologist Recommended:</strong> Developed with dermatologists for clinical efficacy.</li>
  <li><strong>100% Fragrance-Free & Paraben-Free:</strong> Safe for sensitive foot skin.</li>
  <li><strong>Compact 88ml Tube:</strong> Generous amount for continuous daily foot care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Wash feet with warm water and soap, pat dry before use.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a generous amount of CeraVe Foot Cream onto heels, soles, and toes.</li>
  <li><strong>Step 3 (Massage & Absorb):</strong> Massage in circular motions until absorbed; prefer evening use with cotton socks.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Three Ceramides (1, 3, 6-II):</strong> Restore the natural lipid barrier and lock in deep moisture.</li>
  <li><strong>Salicylic Acid & Lactic Acid:</strong> Gently exfoliate dead skin cells and calluses precisely.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical foot skin application only.</li>
  <li>Avoid contact with eyes and open wounds.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Those with dry, cracked heels or rough foot skin seeking CeraVe's 88ml Renewing Foot Cream for medical-grade repair.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>CeraVe</td></tr>
  <tr><th>Category</th><td>Medical Foot Care / CeraVe Medical Renewing Foot Creams 88ml</td></tr>
  <tr><th>Product Type</th><td>Medical Grade Ceramide & Acid Renewing Dry Cracked Foot Cream (88ml)</td></tr>
  <tr><th>Volume/Weight</th><td>88 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Dry, Cracked & Calloused Foot Skin (Including Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Touchably smooth, 24-hour moisturized, crack-free, renewed feet</td></tr>
  <tr><th>Texture</th><td>Rich fast-absorbing cream without excessive greasiness</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-Free</td></tr>
  <tr><th>Active Ingredients</th><td>Ceramides (1, 3, 6-II), Salicylic Acid, Lactic Acid</td></tr>
  <tr><th>Country of Origin</th><td>USA</td></tr>
  <tr><th>Manufacturer</th><td>CeraVe (L'Oréal Group)</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of CeraVe MVE Technology & Triple Ceramide Lipid Barrier Restoration</h2>

<h3>What problem does this solve?</h3>
<p>CeraVe Renewing Foot Cream resolves severe foot dryness, painful heel cracking, and plantar skin callosity.</p>

<h3>Why choose CeraVe Renewing Foot Cream?</h3>
<p>MVE technology releases moisturizing actives gradually throughout the day, while three Ceramides restore the triple-lamellar lipid barrier lost from chronic foot dryness.</p>"""

    en_faqs = [
        ("What is CeraVe Renewing Foot Cream 88ml?", "It is a medical-grade foot cream with three Ceramides, Salicylic Acid, and Lactic Acid to repair dry, cracked, and rough foot skin."),
        ("What are the benefits of Ceramides, Salicylic Acid, and Lactic Acid?", "Ceramides restore the skin barrier, Salicylic Acid exfoliates dead skin, and Lactic Acid renews calloused foot skin."),
        ("Does it repair dry, cracked heels effectively?", "Yes, clinically proven to repair foot dryness and heel cracking using MVE technology and Ceramides."),
        ("What volume is contained in this tube?", "It comes in an 88ml tube."),
        ("How do I use it correctly?", "Apply generously onto dry feet, massage until absorbed; prefer evening use with cotton socks."),
        ("Is it dermatologist recommended?", "Yes, developed with dermatologists and medically recommended."),
        ("Where is CeraVe Foot Cream manufactured?", "Manufactured in the USA by CeraVe (L'Oréal Group)."),
        ("How do I verify authenticity at Ekleel Abha?", "All CeraVe products at Ekleel Abha are 100% original from certified distributors."),
        ("Is it safe for sensitive foot skin?", "Yes, 100% fragrance-free and paraben-free; safe for sensitive foot skin."),
        ("What does CeraVe Foot Cream smell like?", "Completely fragrance-free (Fragrance-Free)."),
        ("Does it absorb quickly without excessive greasiness?", "Yes, rich formula absorbs well without leaving excessive greasy residue."),
        ("Does the 88ml tube last a long time for daily use?", "Yes, lasts months of daily foot care use."),
        ("How should I store the tube?", "Store in a cool, dry place away from direct sunlight."),
        ("Is it suitable for men and women?", "Suitable for all ages, both men and women aged 12+."),
        ("Is the tube cap leak-proof?", "Yes, comes in an elegant tube with a secure cap."),
        ("How many times daily should I use it?", "Use daily; prefer evening use with cotton socks for faster healing results."),
        ("Does it prevent recurring heel cracking?", "Yes, regular use maintains the natural skin barrier and prevents recurring dryness."),
        ("Is it suitable for diabetic foot dryness?", "Consult your doctor before use if you have diabetes."),
        ("Is it CeraVe's #1 foot cream?", "Yes, CeraVe Renewing Foot Cream is the #1 foot cream by CeraVe."),
        ("Does it leave feet touchably smooth?", "Yes, leaves feet touchably smooth and free of dryness and cracking."),
        ("Is the tube recyclable?", "Yes, recyclable tube."),
        ("Does it treat thickened calloused heel skin?", "Yes, Salicylic and Lactic Acid progressively exfoliate thickened callous skin."),
        ("Does it leave feet soft after waking up?", "Yes, with cotton socks on, it leaves feet remarkably soft after sleep."),
        ("Is it helpful for deep bleeding heel cracks?", "For regular heel dryness and cracking; consult a doctor for deep bleeding cracks."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1888",
        "sku": "EK-1888",
        "gtin": "3337875597296",
        "brand": "CeraVe",
        "ar": {
            "title": "كريم اصلاح القدم من سيرافي 88 مل",
            "meta_title": "كريم إصلاح القدم سيرافي 88مل | إكليل أبها",
            "meta_description": "اشتري كريم إصلاح القدم من سيرافي (88 مل). كريم طبي بالسيراميدات الثلاثة وحمض الساليسيليك لإصلاح وترطيب القدمين الجافة والمتشققة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["سيرافي", "كريم_القدم", "إصلاح_القدمين", "سيراميدات", "إكليل_أبها"]
        },
        "en": {
            "title": "CeraVe Renewing Foot Cream 88ml",
            "meta_title": "CeraVe Renewing Foot Cream 88ml | Ekleel Abha",
            "meta_description": "Buy original CeraVe Renewing Foot Cream (88ml). Three Ceramides & Salicylic Acid medical foot cream for repairing dry cracked heels. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["cerave", "foot_cream", "renewing_foot", "ceramides", "ekleel_abha"]
        }
    }


def _make_deodorant_2pack(pid, gtin, ar_name, en_name, scent_ar, scent_en, meta_ar_suffix, meta_en_suffix, tags_ar, tags_en, unique_ar_note, unique_en_note):
    """Helper to build a Beesline 2-pack deodorant product."""
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> طقم مزيل العرق الاقتصادي المضاعف من بيزلين يضم قطعتين من مزيل العرق {scent_ar} بسعر أوفر وقيمة أعلى. {unique_ar_note} يضمن هذا الطقم (بيزلين - قطعتان) الاستخدام الأسري والمزدوج بكميات وفيرة تكفي أشهراً متواصلة.</p>
<p>يعمل مزيل بيزلين على الحد من نمو البكتيريا المسببة للروائح، امتصاص العرق الزائد، وتوفير تفتيح آمن للإبطين، ليمنح إبطيك جفافاً تاماً وعطراً فواحاً ونعومة ملحوظة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عرض اقتصادي بقطعتين بسعر أوفر:</strong> توفير مضاعف للاستخدام الأسري أو الاحتياطي.</li>
  <li><strong>حماية قصوى من العرق والروائح لـ 48 ساعة:</strong> صمغ النحل وحجر الشبة يقضيان على البكتيريا.</li>
  <li><strong>تفتيح وتوحيد لون بشرة الإبطين باللوميسكين:</strong> يزيل التصبغات الناتجة عن الاحتكاك.</li>
  <li><strong>عطر {scent_ar} المميز:</strong> يمنح انتعاشاً ورائحة فواحة طوال اليوم.</li>
  <li><strong>خالي 100% من ألومنيوم كلوروهيدرات، الكحول، والبارابين:</strong> آمن للبشرة الحساسة.</li>
  <li><strong>عبوتان رول اون بكرة دوارة:</strong> حجم مدمج أنيق مريح في الاستخدام.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> نظف منطقة الإبطين بالماء والصابون وجففها جيداً.</li>
  <li><strong>الخطوة الثانية:</strong> مرر البكرة 1-2 مرة على بشرة الإبط الجافة.</li>
  <li><strong>الخطوة الثالثة:</strong> دع السائل يجف ثوانٍ قبل ارتداء الملابس (يُستعمل مرة يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>حجر الشبة وصمغ النحل:</strong> يمتصان العرق ويطهران البشرة من البكتيريا.</li>
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
  <li>لمن يبحث عن طقم مزيل عرق بيزلين بعطر {scent_ar} قطعتين بسعر اقتصادي أوفر.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / أطقم مزيلات عرق بيزلين الرول اون الاقتصادية (قطعتان)</td></tr>
  <tr><th>نوع المنتج</th><td>طقم مزيل عرق رول اون بيزلين بعطر {scent_ar} - قطعتان</td></tr>
  <tr><th>الحجم/الوزن</th><td>قطعتان رول اون</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الإبطين (بما في ذلك البشرة الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>إبطان جافتان ومنعشتان بعطر {scent_ar} وخاليتان من الروائح</td></tr>
  <tr><th>الملمس</th><td>سائل رول اون خفيف ينفذ فورياً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر {scent_ar} المميز</td></tr>
  <tr><th>المكونات النشطة</th><td>حجر الشبة (Alum Rock)، صمغ النحل (Propolis)، لوميسكين</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد عطر {scent_ar} وحجر الشبة في طقم بيزلين (قطعتان)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج طقم بيزلين بعطر {scent_ar} (قطعتان) مشكلة رائحة العرق اليومية واسمرار الإبطين مع الوفر الاقتصادي لأهل الأسرة.</p>

<h3>لماذا يُعد الطقم المزدوج (قطعتان) الخيار الأوفر؟</h3>
<p>لأن شراء قطعتين بسعر واحد اقتصادي يضمن الاستمرار في الاستخدام دون انقطاع ويوفر مخزوناً احتياطياً.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق صباحاً على جلد جاف نظيف:</strong> ضع الرول اون فور الاستحمام.<br>
2. <strong>تجنب الملابس الضيقة:</strong> التهوية الجيدة تمد فعالية المزيل لساعات أطول.<br>
3. <strong>الاستمرار المنتظم:</strong> يضمن الحماية الدائمة من العرق والروائح.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الطقم المزدوج يعني جودة أقل من القطعة المنفردة."<br>
<strong>الحقيقة:</strong> طقم بيزلين بقطعتين يحتوي على نفس تركيبة ونفس جودة مزيل العرق الفردي.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تعمل أملاح حجر الشبة الطبيعية على تضييق مسام الغدد العرقية السطحية بشكل مؤقت، مما يحد من كمية العرق وتكاثر البكتيريا.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو طقم اقتصادي مكون من قطعتين من مزيل عرق بيزلين بعطر {scent_ar} بسعر أوفر وقيمة أعلى."),
        ("ما هي فوائد حجر الشبة وصمغ النحل واللوميسكين؟", f"يمتص حجر الشبة العرق، يطهر صمغ النحل البشرة، ويفتّح اللوميسكين تصبغات الإبطين."),
        ("هل يوفر حماية 48 ساعة من العرق والروائح؟", "نعم، مثبت سريرياً في تأمين حماية تامة لـ 48 ساعة من العرق والروائح."),
        ("كم قطعة يحتوي الطقم؟", "يحتوي على قطعتين من الرول اون."),
        ("كيف يُستخدم بالشكل الصحيح؟", "مرر البكرة 1-2 مرة على بشرة الإبط النظيفة والجافة، دع السائل يجف ثوانٍ قبل ارتداء الملابس."),
        ("هل هو خالي من ألومنيوم كلوروهيدرات والبارابين والكحول؟", "نعم، خالي 100% من ألومنيوم كلوروهيدرات والكحول والبارابين."),
        ("ما هو بلد صنع طقم مزيل عرق بيزلين؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% من الوكيل المعتمد."),
        ("هل يترك أثراً أو بقعاً على الملابس؟", "لا، قوام شفاف ينفذ فورياً دون ترك أي أثر على الملابس."),
        (f"ما هي رائحة طقم بيزلين بعطر {scent_ar}؟", f"يتميز بعطر {scent_ar} المميز والفواح."),
        ("هل يهدئ تهيج الإبطين بعد الحلاقة؟", "نعم، صمغ النحل والألوفيرا يهدئان البشرة بعد الحلاقة."),
        ("هل الطقم المزدوج يوفر مدخرات في السعر؟", "نعم، يوفر قيمة اقتصادية أعلى من شراء قطعتين منفصلتين."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل يناسب الرجال والنساء؟", "مناسب لجميع الفئات من سن 12 سنة."),
        ("هل العبوة محكمة الغلق؟", "نعم، تأتي كل قطعة بغطاء محكم الحماية."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل مرة واحدة يومياً."),
        ("هل يمنع تكاثر البكتيريا المسببة للرائحة؟", "نعم، صمغ النحل وحجر الشبة يمنعان نمو البكتيريا."),
        ("هل يناسب البشرة الحساسة؟", "نعم، فورمولا طبيعية آمنة للبشرة الحساسة."),
        ("هل يفتّح الإبطين باللوميسكين؟", "نعم، اللوميسكين يفتّح التصبغات ويمنع الاسمرار تدريجياً."),
        ("هل يمنح انتعاشاً طوال اليوم؟", f"نعم، عطر {scent_ar} يضمن انتعاشاً وجفافاً طوال اليوم."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة."),
        ("هل يجف سريعاً على البشرة؟", "نعم، يجف خلال ثوانٍ."),
        ("هل الطقم مثالي كهدية؟", "نعم، طقم أنيق ومفيد مثالي كهدية عملية."),
        ("هل القطعتان متطابقتان؟", "نعم، كلتا القطعتين متطابقتان بنفس التركيبة والعطر."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is the economical double-pack from Beesline, containing two roll-on deodorants with {scent_en} scent at a better value. {unique_en_note} This twin-pack ensures continuous use without running out and provides a backup supply.</p>
<p>Beesline Deodorant eliminates odor-causing bacteria, absorbs excess sweat, and provides safe underarm brightening, delivering complete dryness, fresh scent, and smooth underarms all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Economical 2-Piece Pack at Better Value:</strong> Double savings for family or backup use.</li>
  <li><strong>48-Hour Maximum Sweat & Odor Protection:</strong> Propolis and Alum Rock eliminate bacteria.</li>
  <li><strong>Underarm Brightening with Lumiskin:</strong> Fades dark friction hyperpigmentation spots.</li>
  <li><strong>Signature {scent_en} Fragrance:</strong> Delivers refreshing freshness all day.</li>
  <li><strong>100% Free of Aluminum Chlorohydrate, Alcohol & Parabens:</strong> Safe for sensitive skin.</li>
  <li><strong>Two Roll-On Bottles:</strong> Compact, stylish, and convenient to use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Cleanse underarms with soap and water, pat dry.</li>
  <li><strong>Step 2:</strong> Roll applicator 1-2 times over dry underarm skin.</li>
  <li><strong>Step 3:</strong> Allow to dry for seconds before dressing (use once daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Alum Rock & Propolis:</strong> Absorb sweat and purify skin from bacteria.</li>
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
  <li>Those seeking an economical twin-pack of Beesline {scent_en} Deodorant for continuous use and better value.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Personal Care / Beesline Economical Roll-On Deodorant Twin Packs</td></tr>
  <tr><th>Product Type</th><td>Beesline {scent_en} Scented Roll-On Deodorant 2-Piece Twin Pack</td></tr>
  <tr><th>Volume/Weight</th><td>2-Piece Roll-On Pack</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Underarm Skin Types (Including Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Dry, brightened, fresh-scented, odor-free armpits</td></tr>
  <tr><th>Texture</th><td>Smooth lightweight fast-drying roll-on fluid</td></tr>
  <tr><th>Fragrance</th><td>Signature {scent_en} fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Alum Rock, Propolis, Lumiskin</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Alum Rock Astringency & Propolis Antibacterial Defense in Beesline Twin Pack</h2>

<h3>What problem does this solve?</h3>
<p>Beesline {scent_en} Deodorant 2-Piece Pack resolves daily underarm odor, friction hyperpigmentation, and the need for continuous supply value.</p>

<h3>Why choose the Beesline Twin-Pack?</h3>
<p>Buying two pieces at a better price guarantees uninterrupted daily use while the twin-pack provides identical quality to individual bottles.</p>"""

    en_faqs_data = [
        (f"What is the {en_name}?", f"It is an economical 2-piece twin-pack from Beesline containing two {scent_en}-scented roll-on deodorants at a better value."),
        ("What are the benefits of Alum Rock, Propolis, and Lumiskin?", "Alum Rock absorbs sweat, Propolis purifies skin, and Lumiskin brightens dark underarm spots."),
        ("Does it provide 48-hour protection from sweat and odor?", "Yes, clinically proven for 48-hour total protection from sweat and odor."),
        ("How many pieces are in this pack?", "The pack contains two roll-on bottles."),
        ("How do I use it correctly?", "Roll 1-2 times onto clean, dry underarm skin, allow to dry, and dress."),
        ("Is it free of aluminum chlorohydrate, alcohol, and parabens?", "Yes, 100% free of aluminum chlorohydrate, alcohol, and parabens."),
        ("Where is this Beesline twin-pack manufactured?", "Proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it leave marks on clothes?", "No, invisible fluid absorbs instantly without leaving marks."),
        (f"What scent does the Beesline {scent_en} 2-Piece Pack have?", f"Features the signature {scent_en} fragrance."),
        ("Does it soothe post-shaving irritation?", "Yes, Propolis and Aloe Vera calm skin irritation after shaving."),
        ("Does the twin-pack offer price savings?", "Yes, provides higher value than buying two individual bottles separately."),
        ("How should I store the bottles?", "Store in a cool, dry place."),
        ("Is it suitable for men and women?", "Suitable for all ages, both men and women aged 12+."),
        ("Are the bottles leak-proof?", "Yes, each bottle features a secure screw-top cap."),
        ("How many times daily should I use it?", "Recommended for use once daily."),
        ("Does it prevent odor-causing bacteria?", "Yes, Propolis and Alum Rock prevent bacterial growth."),
        ("Is it safe for sensitive underarm skin?", "Yes, natural formula safe for sensitive skin."),
        ("Does Lumiskin brighten underarms?", "Yes, Lumiskin progressively brightens and prevents dark underarm spots."),
        (f"Does it provide all-day freshness with {scent_en}?", f"Yes, {scent_en} fragrance ensures freshness and dryness all day."),
        ("Are the bottles recyclable?", "Yes, eco-friendly recyclable bottles."),
        ("Does it dry quickly on skin?", "Yes, fluid dries in seconds."),
        ("Is the twin-pack a good gift option?", "Yes, an elegant and practical gift for anyone."),
        ("Are both pieces identical?", "Yes, both pieces contain the same formula and scent."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
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
            "meta_description": f"Buy original {en_name}. {meta_en_suffix} 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1889():
    return _make_deodorant_2pack(
        pid=1889, gtin="5281018086063",
        ar_name="مزيل عرق5في 1 من بيزلين(قطعتين)",
        en_name="Beesline 5-in-1 Deodorant (2-Piece Set)",
        scent_ar="5 في 1 متعدد الفوائد",
        scent_en="5-in-1 Multi-Benefit",
        meta_ar_suffix="طقم اقتصادي بقطعتين من مزيل عرق بيزلين 5 في 1 المتعدد الفوائد.",
        meta_en_suffix="Economical 2-piece set of Beesline 5-in-1 Multi-Benefit Deodorant.",
        tags_ar=["بيزلين", "مزيل_عرق_5في1", "طقم_مزيل_عرق", "خمسة_فوائد", "إكليل_أبها"],
        tags_en=["beesline", "5in1_deodorant", "deodorant_2pack", "multi_benefit", "ekleel_abha"],
        unique_ar_note="يمتاز مزيل عرق بيزلين 5 في 1 بخمس فوائد متكاملة في منتج واحد: جفاف، تفتيح، تطهير، تهدئة، وحماية من الروائح.",
        unique_en_note="Beesline 5-in-1 Deodorant offers five integrated benefits in one: dryness, brightening, purification, soothing, and odor protection."
    )


def create_product_1890():
    return _make_deodorant_2pack(
        pid=1890, gtin="5281018568033",
        ar_name="مزيل عرق تألق اللؤلؤ من بيزلين(قطعتين)",
        en_name="Beesline Pearl Shine Deodorant (2 Pieces)",
        scent_ar="تألق اللؤلؤ المشرق",
        scent_en="Pearl Shine Radiance",
        meta_ar_suffix="طقم اقتصادي بقطعتين من مزيل عرق بيزلين تألق اللؤلؤ.",
        meta_en_suffix="Economical 2-piece set of Beesline Pearl Shine Radiance Deodorant.",
        tags_ar=["بيزلين", "مزيل_عرق_اللؤلؤ", "تألق_اللؤلؤ", "طقم_مزيل_عرق", "إكليل_أبها"],
        tags_en=["beesline", "pearl_shine_deodorant", "deodorant_2pack", "pearl_radiance", "ekleel_abha"],
        unique_ar_note="يمتاز مزيل عرق بيزلين تألق اللؤلؤ بتأثير لمعان لؤلؤي ناعم يعطي بشرة الإبطين إشراقة ناصعة كاللؤلؤ.",
        unique_en_note="Beesline Pearl Shine Deodorant features a soft pearlescent shimmer effect imparting a radiant luminous glow to underarm skin."
    )


def create_product_1891():
    return _make_deodorant_2pack(
        pid=1891, gtin="5281018089002",
        ar_name="مزيل عرق  عودعربي من بيزلين(قطعتين)",
        en_name="Beesline Arabian Oud Deodorant (2-Piece Set)",
        scent_ar="العود العربي الفاخر الأصيل",
        scent_en="Authentic Arabian Oud",
        meta_ar_suffix="طقم اقتصادي بقطعتين من مزيل عرق بيزلين بعطر العود العربي الفاخر.",
        meta_en_suffix="Economical 2-piece set of Beesline Authentic Arabian Oud Deodorant.",
        tags_ar=["بيزلين", "مزيل_عرق_عود", "عود_عربي", "طقم_مزيل_عرق", "إكليل_أبها"],
        tags_en=["beesline", "arabian_oud_deodorant", "deodorant_2pack", "oud_scent", "ekleel_abha"],
        unique_ar_note="يمتاز مزيل عرق بيزلين بعطر العود العربي الأصيل الفاخر والمميز الذي يجمع بين التراث العربي والتكنولوجيا الحديثة.",
        unique_en_note="Beesline Arabian Oud Deodorant features an authentic, rich Arabian Oud fragrance combining Arab heritage with modern skincare technology."
    )


print("Loaded all 5 Batch 35 builders complete")
