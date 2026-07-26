import json, os

def create_product_1795():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>بخاخ مثبت مكياج مرطب بفيتامين هـ (150 مل) لثبات يدوم طويلاً (Makeup Setting Spray with Vitamin E - 150ml)</strong> المستحضر المثالي والأهم في روتين المكياج لتثبيت الإطلالة وحمايتها من التلطخ، التكتل، والذوبان طوال اليوم. يمزج هذا البخاخ المتطور بين خواص تثبيت المكياج عالية الأداء والتغذية المرطبة لفيتامين هـ (Vitamin E)، حيث ينعش البشرة ويمنع جفاف طبقات الفاونديشن والبودرة.</p>
<p>يمتاز مثبت المكياج برذاذ دقيق جداً (Fine Mist) يتوزع بالتساوي على الوجه، مما يمنحكِ مظهر مكياج متماسكاً، ناعماً، وطبيعياً بدون أثر دهني لزج أو شعور بالشد.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ثبات مضاعف للمكياج طوال اليوم:</strong> يثبت كريم الأساس والبودرة وظلال العيون لـ 16 ساعة متواصلة.</li>
  <li><strong>مدعم بفيتامين هـ (Vitamin E):</strong> يرطب البشرة ويحميها من الأكسدة والعوامل البيئية الجافة.</li>
  <li><strong>رذاذ ميكرو دقيق غير متكتل:</strong> يتوزع بسلاسة دون إذابة البودرة أو إحداث خطوط على الوجه.</li>
  <li><strong>لمسة نهائية طبيعية ومشرقة:</strong> يزيل المظهر البودري الثقيل ويمنح البشرة نضارة حيوية.</li>
  <li><strong>مقاوم للتلطخ والحرارة والرطوبة:</strong> يحمي المكياج من الذوبان بفعل العرق والحرارة.</li>
  <li><strong>عبوة أنيقة سعة 150 مل:</strong> حجم ممتازة تكفي لعدة أشهر من التثبيت اليومي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الرج):</strong> رجي العبوة جيداً قبل الاستعمال.</li>
  <li><strong>الخطوة الثانية (الرش):</strong> أغمضي العينين والفم ورشي بخاخ تثبيت المكياج بحرف (X) و (T) على بُعد 20 سم من الوجه.</li>
  <li><strong>الخطوة الثالثة (التجفيف):</strong> اتركي الرذاذ يجف طبيعياً في الهواء دون لمسه للاستمتاع بـ ثبات تام.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>فيتامين هـ (Tocopheryl Acetate):</strong> يرطب البشرة ويمنع جفاف وتأكسد المكياج.</li>
  <li><strong>بوليمرات تثبيت مرنة خفيفة:</strong> تغلف طبقات المكياج بحجاب واقٍ مقاوم للتلطخ.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على بشرة الوجه فقط.</li>
  <li>أغمضي العينين جيداً أثناء الرش وتجنبي ملامسته المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من ترغب في تثبيت مكياجها طوال اليوم بدون ذوبان أو تلطخ وبنضارة فيتامين E.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>عام / صيدلية إكليل أبها</td></tr>
  <tr><th>الفئة</th><td>المكياج / بخاخات تثبيت وانتعاش المكياج</td></tr>
  <tr><th>نوع المنتج</th><td>بخاخ مثبت ومقوي للمكياج بفيتامين E (150ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>150 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (الدهنية، الجافة، والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>مكياج ثابت، طبيعي، مشرق، وخالٍ من الذوبان والتلطخ</td></tr>
  <tr><th>الملمس</th><td>رذاذ مائي خفيف جداً ناعم غير لزج</td></tr>
  <tr><th>العطر</th><td>عطر ناعم خفيف منعش</td></tr>
  <tr><th>المكونات النشطة</th><td>فيتامين E، بوليمرات التثبيت المرنة، جليسرين</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / كوريا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Make-Up Care Labs</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 15 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد بخاخ تثبيت المكياج وفيتامين E</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج بخاخ مثبت المكياج مشكلة ذوبان كريم الأساس، تكتل البودرة، تلطخ الظلال، والمظهر البودري الجاف للوجه.</p>

<h3>لماذا يفضل فيتامين E في مثبت المكياج؟</h3>
<p>لأن فيتامين E يرطب الطبقة السطحية، مما يمنع تشقق الفاونديشن ويمنح المظهر النهائي نضارة طبيعية دون لمعان زيتي.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الرش بمسافة كافية:</strong> رشي من مسافة 20 سم لضمان توزيع الرذاذ بالتساوي.<br>
2. <strong>الاستخدام قبل وبعد المكياج:</strong> يمكن رشه قبل المكياج لتهيئة البشرة وبعده لتثبيت الإطلالة.<br>
3. <strong>ترك الرذاذ يجف طبيعياً:</strong> لا تمسحي الوجه بعد الرش ودعيه يجف في الهواء.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "بخاخات مثبت المكياج تسد المسام وتسبب الحبوب."<br>
<strong>الحقيقة:</strong> مثبت المكياج بمكونات خفيفة وغير كوميدوجينية يثبت المكياج سطحياً دون سد المسام.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تشكل البوليمرات الدقيقة غشائاً شفافاً يربط مساحيق البودرة والفاونديشن ببعضها، بينما يحميكِ فيتامين E من التأكسد والحرارة.</p>"""

    faqs = [
        ("ما هو بخاخ مثبت مكياج مرطب بفيتامين هـ 150 مل؟", "هو بخاخ تثبيت رذاذي ناعم يثبت المكياج طوال اليوم ويحمي البشرة من التلطخ والذوبان بغنى فيتامين E."),
        ("ما هي فوائد فيتامين E في مثبت المكياج؟", "يرطب البشرة، يمنع جفاف الفاونديشن، ويزيل المظهر البودري الثقيل."),
        ("كم ساعة يثبت المكياج؟", "يثبت المكياج لـ 16 ساعة متواصلة ضد العرق والحرارة والرطوبة."),
        ("ما حجم العبوة؟", "تأتي بحجم 150 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "أغمضي العينين ورشي بحرف (X) و (T) من مسافة 20 سم ثم دعي الرذاذ يجف طبيعياً."),
        ("هل يناسب جميع أنواع البشرة؟", "نعم، آمن وممتاز للبشرة الدهنية، الجافة، والمختلطة."),
        ("ما هو بلد صنع المنتج؟", "تم تصنيعه وفق أعلى معايير جودة التجميل العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع مستحضرات التجميل لدى إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يترك ملمساً لزجاً أو زيتياً؟", "لا، يمتص ويجف فورياً ليترك ملمساً ناعماً وطبيعياً."),
        ("هل يمكن رشه قبل تطبيق المكياج؟", "نعم، رشه قبل المكياج يجهز ويهيئ البشرة للفاونديشن."),
        ("هل يحمي من تلطخ ظلال العيون والكحل؟", "نعم، يثبت المكياج الكامل بما في ذلك ظلال العيون والبلاشر."),
        ("هل العبوة 150 مل مناسبة للسفر والحقيبة؟", "نعم، حجم مدمج وأنيق لحمله في حقيبة المكياج والسفر."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل يسبب سد المسام؟", "تركيبة غير كوميدوجينيك آمنة للمسام."),
        ("هل يناسب الاستخدام اليومي والمناسبات؟", "نعم، ممتاز للاستخدام اليومي وفي الحفلات والمناسبات."),
        ("هل يمنح حس نضارة حيوية؟", "نعم، يزيل جفاف البودرة ويمنح الوجه نضارة حيوية."),
        ("هل البخاخ دقيق في التوزيع؟", "نعم، بخاخ ميكرو يوزع الرذاذ بالتساوي."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة أنيقة بغطاء محكم يمنع التسرب."),
        ("هل يناسب الصيف والحر؟", "ممتاز جداً لمنع ذوبان المكياج في حر الصيف."),
        ("هل يناسب جميع الأعمار؟", "مناسب للمراهقين والبالغين من سن 15 سنة فما فوق."),
        ("هل يترك بقعاً على الملابس؟", "رذاذ شفاف لا يترك أثراً على الملابس."),
        ("هل يغني عن البودرة الحرة؟", "يعزز تثبيت البودرة والفاونديشن معاً."),
        ("هل يحمي من التأكسد؟", "نعم، فيتامين E يمنع تغير لون الفاونديشن بالهواء."),
        ("هل هو خيار خبراء التجميل؟", "نعم، خيار أساسي لدى مصففي ومكياجي الصالونات."),
        ("هل يتوفر بسعر ممتاز؟", "نعم، قيمة اقتصادية ممتازة لحجم 150 مل.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Makeup Setting Spray with Vitamin E - 150ml</strong> is the essential makeup finishing mist designed to lock in your makeup look, preventing smudging, creasing, and melting all day. Combining high-performance makeup locking polymers with skin-nourishing Vitamin E, it hydrates the skin and keeps foundation and powder looking freshly applied.</p>
<p>Featuring a micro-fine mist spray that dispenses evenly across the face, this setting spray creates a seamless, natural finish without feeling greasy, sticky, or tight.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>16-Hour Makeup Lock:</strong> Locks foundation, powder, blush, and eyeshadow in place for up to 16 hours.</li>
  <li><strong>Enriched with Vitamin E:</strong> Hydrates skin and guards against oxidative stress and environmental dryness.</li>
  <li><strong>Micro-Fine Non-Clumping Mist:</strong> Dispenses smoothly without melting powders or streaking makeup.</li>
  <li><strong>Natural Radiant Finish:</strong> Melts away powdery flashback textures, leaving a fresh skin glow.</li>
  <li><strong>Smudge, Sweat & Humidity Resistant:</strong> Shields makeup against melting in heat and humidity.</li>
  <li><strong>Sleek 150ml Bottle:</strong> High-value bottle providing months of continuous daily makeup setting.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Shake):</strong> Shake bottle well before use.</li>
  <li><strong>Step 2 (Mist):</strong> Close eyes and mouth, then spray setting mist in (X) and (T) motions 20 cm away from face.</li>
  <li><strong>Step 3 (Set):</strong> Allow mist to air dry naturally without touching for complete makeup fixation.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Vitamin E (Tocopheryl Acetate):</strong> Hydrates skin and prevents foundation oxidation.</li>
  <li><strong>Flexible Fixing Polymers:</strong> Form an invisible protective shield resisting smudges.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external facial makeup application only.</li>
  <li>Keep eyes and mouth firmly closed while spraying; avoid direct eye contact.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone wanting long-lasting 16-hour makeup fixation with the skin-hydrating power of Vitamin E.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Generic / Ekleel Abha Pharmacy</td></tr>
  <tr><th>Category</th><td>Makeup / Makeup Setting & Refreshing Sprays</td></tr>
  <tr><th>Product Type</th><td>Hydrating Makeup Setting Spray with Vitamin E (150ml)</td></tr>
  <tr><th>Volume/Weight</th><td>150 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Oily, Dry, Combination)</td></tr>
  <tr><th>Finish</th><td>Locked, natural, radiant & smudge-proof makeup</td></tr>
  <tr><th>Texture</th><td>Micro-fine weightless non-sticky liquid mist</td></tr>
  <tr><th>Fragrance</th><td>Soft subtle fresh scent</td></tr>
  <tr><th>Active Ingredients</th><td>Vitamin E, Flexible Fixing Polymers, Glycerin</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / Korea</td></tr>
  <tr><th>Manufacturer</th><td>Make-Up Care Labs</td></tr>
  <tr><th>Age Group</th><td>All Ages (15+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Micro-Polymer Fixation & Vitamin E Hydration</h2>

<h3>What problem does this solve?</h3>
<p>Makeup Setting Spray with Vitamin E resolves foundation melting, powder cakey textures, eyeshadow creasing, and heat smudging.</p>

<h3>Why choose Vitamin E in setting spray?</h3>
<p>Vitamin E conditions upper dermal layers, melting powder textures into skin for a natural glow without oily shine.</p>"""

    en_faqs = [
        ("What is Makeup Setting Spray with Vitamin E 150ml?", "It is a micro-fine setting mist enriched with Vitamin E to lock makeup for 16 hours and prevent smudging."),
        ("What are the benefits of Vitamin E in a setting spray?", "Hydrates skin, prevents foundation oxidation, and melts away cakey powder textures."),
        ("How many hours does it lock makeup?", "Locks makeup in place for up to 16 hours against sweat, heat, and humidity."),
        ("What volume is contained in this bottle?", "It comes in a sleek 150ml bottle."),
        ("How do I apply it correctly?", "Shake well, close eyes, spray in (X) and (T) patterns 20 cm from face, and let air dry."),
        ("Is it suitable for all skin types?", "Yes, safe and effective for oily, dry, and combination skin types."),
        ("Where is it manufactured?", "Produced under global beauty formulation standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All makeup products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it leave a sticky or greasy residue?", "No, absorbs quickly leaving a smooth, natural weightless finish."),
        ("Can it be used before applying makeup?", "Yes, spraying before foundation primes and hydrates the skin."),
        ("Does it protect eye makeup and blush?", "Yes, locks in entire makeup including eyeshadows and blushes."),
        ("Is the 150ml bottle travel-friendly?", "Yes, compact size easily fits into travel makeup pouches."),
        ("How should I store the bottle?", "Store in a cool, dry place away from heat."),
        ("Is it non-comedogenic?", "Yes, lightweight formula will not clog pores."),
        ("Is it good for daily and special event makeup?", "Yes, ideal for daily work makeup and long events."),
        ("Does it give a radiant finish?", "Yes, removes dry powdery finishes leaving a healthy glow."),
        ("Is the mist dispenser micro-fine?", "Yes, dispenses a fine mist evenly across the face."),
        ("Is the bottle securely sealed?", "Yes, comes in a sturdy bottle with a protective cap."),
        ("Is it great for summer heat?", "Yes, essential for stopping makeup meltdown in hot summer weather."),
        ("What age group is it for?", "Suitable for teens and adults aged 15+."),
        ("Does it stain clothing?", "No, clear fine mist leaves zero residue on clothes."),
        ("Does it replace setting powder?", "Enhances powder and foundation longevity together."),
        ("Does it prevent foundation oxidation?", "Yes, Vitamin E shields foundation pigments from air oxidation."),
        ("Is it recommended by makeup artists?", "Yes, a staple tool among professional makeup artists."),
        ("Is it an economical choice?", "Yes, generous 150ml size offers great long-term value.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1795",
        "sku": "EK-1795",
        "gtin": "6281056379522",
        "category": "المكياج / بخاخات تثبيت وانتعاش المكياج",
        "brand": "Generic Make-Up",
        "ar": {
            "title": "بخاخ مثبت مكياج مرطب بفيتامين هـ (150 مل) لثبات يدوم طويلاً",
            "meta_title": "بخاخ مثبت مكياج بفيتامين هـ 150مل | صيدلية إكليل أبها",
            "meta_description": "اشتري بخاخ مثبت مكياج مرطب بفيتامين هـ (150 مل). ثبات يدوم لـ 16 ساعة ومقاوم للتلطخ والحرارة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["مثبت_مكياج", "فيتامين_E", "ثبات_المكياج", "بخاخ_المكياج", "إكليل_أبها"]
        },
        "en": {
            "title": "Makeup Setting Spray with Vitamin E - 150ml",
            "meta_title": "Makeup Setting Spray with Vitamin E 150ml | Ekleel Abha",
            "meta_description": "Buy original Makeup Setting Spray with Vitamin E (150ml). 16-hour makeup fixation & smudge-proof formula. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["setting_spray", "vitamin_e", "makeup_lock", "smudge_proof", "ekleel_abha"]
        },
        "schema": {
            "brand": "Generic Make-Up",
            "category": "Makeup / Setting Spray",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "makeup-setting-spray-with-vitamin-e-150ml.webp",
            "alt": "Makeup Setting Spray with Vitamin E 150ml",
            "title": "Makeup Setting Spray with Vitamin E 150ml"
        }
    }

def build_rembrandt_body_mist(prod_id, variant_ar, variant_en, scent_ar, scent_en, gtin, img_slug):
    title_ar = f"معطر جسم {variant_ar} من رامبرانت 200مل"
    title_en = f"Rembrandt {variant_en} Body Mist - 200ml"

    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>معطر جسم {variant_ar} من رامبرانت 200مل (Rembrandt {variant_en} Body Mist - 200ml)</strong> بخاخ الجسم العطري الفاخر والأنعش لإضفاء عبير ساحر، جذّاب، يدوم طوال اليوم على البشرة والملابس. يجمع هذا المعطر المتنوع من علامة رامبرانت (Rembrandt Fine Fragrances) بين النغمات العطرية لـ {scent_ar} والمكونات المرطبة اللطيفة على الجلد، مما يمنحكِ سحراً واستثنائية بعد كل غسلة أو استحمام.</p>
<p>يمتاز معطر رامبرانت برذاذ دقيق خفيف يتوزع بسلاسة، ويترك جسمكِ معطراً برائحة فواحة تزيد من حس النظافة، الثقة، والجاذبية في كل الأوقات والمناسبات.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عبير ساحر بـ {scent_ar}:</strong> يمنحكِ رائحة أنثوية راقية تدوم لعدة ساعات.</li>
  <li><strong>رذاذ عطري خفيف وغير لزج:</strong> يتوزع بسلاسة على البشرة دون ترك أي أثر دهني.</li>
  <li><strong>إنعاش فوري للبشرة:</strong> يمنح حس النظافة والانتعاش المباشر بعد الاستحمام.</li>
  <li><strong>ثبات ممتاز على البشرة والملابس:</strong> تركيبة زيتية عطرية متوازنة تدوم طويلاً.</li>
  <li><strong>آمن ومجرب على جميع أنواع البشرة:</strong> لطيف جداً ولا يسبب تهيجاً للجسم.</li>
  <li><strong>عبوة وافرة سعة 200 مل:</strong> حجم ممتاز ومناسب للتعطير اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الرش):</strong> رشي معطر جسم رامبرانت على بشرة الجسم المبللة أو الجافة من مسافة 15 سم بعد الاستحمام.</li>
  <li><strong>الخطوة الثانية (التركيز):</strong> ركزي الرش على نقاط النبض (المعصمين، خلف الأذنين، والرقبة) لثبات أعلى.</li>
  <li><strong>الخطوة الثالثة (التجفيف):</strong> دعي المعطر يجف طبيعياً واستمتعي بالعبير الساحر.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيوت عطرية بـ {scent_ar}:</strong> تمنح ثباتاً وعبقاً فواحاً راقياً.</li>
  <li><strong>قاعدة مائية مرطبة خاليه من الكحول القاسي:</strong> لطيفة على البشرة والملابس.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الجسم فقط.</li>
  <li>تجنبي رش المعطر المباشر على العينين أو البشرة المتهيكة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن معطر جسم راقٍ برائحة {scent_ar} للتعطير والانتعاش اليومي.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>رامبرانت (Rembrandt)</td></tr>
  <tr><th>الفئة</th><td>العطور / معطرات وبخاخات الجسم العطرية (Body Mists)</td></tr>
  <tr><th>نوع المنتج</th><td>معطر جسم فواح (Rembrandt Body Mist 200ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>200 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم معطر، فواح، رطب، ومفعم بالجاذبية والانتعاش</td></tr>
  <tr><th>الملمس</th><td>رذاذ عطري شفاف غير لزج</td></tr>
  <tr><th>العطر</th><td>عطر {scent_ar} الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>زيوت عطرية نقية بـ {scent_ar}، مرطبات جلدية</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / فرنسا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Rembrandt Fine Fragrances</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد معطرات جسم رامبرانت (Rembrandt Mists)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج معطر جسم رامبرانت مشكلة زوال العطور بسرعة، جفاف البشرة من الكحول، ورائحة العرق المزعجة.</p>

<h3>لماذا تنجح تركيبات رامبرانت؟</h3>
<p>لأن الزيوت العطرية النقية لـ {scent_ar} تندمج مع المرطبات، مما يمنح ثباتاً عاطرياً دون تهيج البشرة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الرش بعد الاستحمام مباشرة:</strong> رشي على بشرة دافئة رطبة للامتصاص والثبات.<br>
2. <strong>الرش على نقاط النبض:</strong> ركزي على الرقبة والمعصمين.<br>
3. <strong>الحفظ بعيداً عن الحرارة:</strong> احفظي الزجاجة في مكان بارد للحفاظ على النغمات العطرية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "معطرات الجسم تزول في دقائق معدودة."<br>
<strong>الحقيقة:</strong> معطرات رامبرانت مصممة بنسبة زيوت عطرية تضمن ثباتاً يدوم لعدة ساعات.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتفاعل الزيوت العطرية مع حرارة الجلد الطبيعية في نقاط النبض، مما يبث العبير تدريجياً ليبقى فواحاً طوال اليوم.</p>"""

    faqs = [
        (f"ما هو معطر جسم {variant_ar} من رامبرانت 200مل؟", f"هو بخاخ معطر للجسم غني بنغمات {scent_ar} يمنح الجسم ثباتاً وانتعاشاً عاطرياً راقياً سعة 200 مل."),
        (f"ما هي رائحة {variant_ar}؟", f"تتميز برائحة {scent_ar} الأنثوية الفاخرة والجذّابة."),
        ("كم يدوم ثبات المعطر على الجسم؟", "يثبت لعدة ساعات على البشرة والملابس برائحة فواحة وغير نفاذة."),
        ("ما حجم العبوة؟", "تأتي بحجم 200 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "رشي على بشرة دافئة بعد الاستحمام وعلى نقاط النبض من مسافة 15 سم."),
        ("هل يسبب بقعاً على الملابس؟", "لا، رذاذ شفاف لا يترك أي أثر على الملابس الأقمشة."),
        ("ما هو بلد صنع معطر رامبرانت؟", "تم تصنيعه وفق أعلى معايير صناعة العطور الفرنسية والعربية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع معطرات رامبرانت لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يترك ملمساً لزجاً على الجلد؟", "لا، يجف فورياً ليترك ملمساً ناعماً ومحسوساً بالانتعاش."),
        ("هل يناسب البشرة الحساسة؟", "تركيبة لطيفة آمنة على بشرة الجسم."),
        ("هل العبوة 200 مل اقتصادية؟", "نعم، عبوة وافرة تكفي للاستخدام اليومي لأشهر طويلة."),
        ("هل يمكن استخدامه للشعر أيضاً؟", "يمكن رشه على أطراف الشعر من مسافة كافية لتعطير خفيف."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس المباشرة."),
        ("هل العبوة محكمة التغليف؟", "تأتي في عبوة أنيقة ببخاخ دقيق ورش محكم."),
        ("هل يناسب الصيف والحر؟", "ممتاز جداً لإنعاش الجسم بعد الشاور في الأيام الحارة."),
        ("هل يناسب جميع الأعمار؟", "مناسب للمراهقات والبالغين من سن 12 سنة فما فوق."),
        ("هل يمنح حس الثقة والأنوثة؟", "نعم، عبيره الفاخر يعزز مشاعر الثقة والجاذبية."),
        ("هل بخاخ المعطر يوزع بالتساوي؟", "نعم، بخاخ دقيق يغطي المساحات بمرونة."),
        ("هل يغني عن العطر الثقيل؟", "ممتاز جداً للاستخدام اليومي الخفيف بدلاً من العطور الثقيلة."),
        ("هل يناسب الاستخدام بعد الرياضة؟", "نعم، يمنح الجسم انتعاشاً فورياً بعد التمارين والاستحمام."),
        ("هل يحتوي على مواد ضارة؟", "خالي من المواد الضارة ومصرح به صحياً."),
        ("هل تتوفر نكهات أخرى من رامبرانت في إكليل أبها؟", "نعم، تتوفر التشكيلة الكاملة من معطرات رامبرانت 200مل."),
        ("هل هو خيار ممتاز كهدية؟", "نعم، تصميم أنيق ورائحة جذابة يمثل هدية راقية."),
        ("هل يمكن رشه على المفارش؟", "نعم، يمكن استخدامه لتعطير المفارش والغرفة برائحة زكية."),
        ("هل يترك انطباعاً عاطرياً مميزاً؟", "نعم، يترك عبقاً يذكر بكِ في كل مكان.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>Rembrandt {variant_en} Body Mist - 200ml</strong> is a luxurious, refreshing body fragrance spray designed to coat your body with a captivating, long-lasting scent. Crafted by Rembrandt Fine Fragrances, it fuses note harmonies of {scent_en} with skin-hydrating conditioning agents for effortless daily elegance.</p>
<p>Delivering a micro-fine non-sticky mist, Rembrandt Body Mist leaves your skin beautifully scented, enveloped in fresh, confident elegance after every shower or workout.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Captivating Scent of {scent_en}:</strong> Delivers an alluring feminine fragrance that lingers for hours.</li>
  <li><strong>Lightweight Non-Sticky Mist:</strong> Sprays smoothly over skin without greasy or heavy residue.</li>
  <li><strong>Instant Shower Refreshment:</strong> Provides an immediate burst of clean freshness post-shower.</li>
  <li><strong>Long-Lasting Skin & Clothes Sillage:</strong> Perfectly balanced perfume oils stay on skin and clothes.</li>
  <li><strong>Safe & Gentle on Skin:</strong> Hypoallergenic formula safe for daily body application.</li>
  <li><strong>Generous 200ml Bottle:</strong> Excellent value bottle for long-term daily body scenting.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Spray):</strong> Spray Rembrandt Body Mist onto damp or dry body skin from 15 cm away after showering.</li>
  <li><strong>Step 2 (Target):</strong> Focus spray on pulse points (wrists, neck, and behind ears) for long-lasting sillage.</li>
  <li><strong>Step 3 (Dry):</strong> Allow mist to air dry naturally and enjoy the captivating aroma.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>{scent_en} Fragrance Oils:</strong> Provide a rich, elegant scent sillage.</li>
  <li><strong>Gentle Hydrating Water Base:</strong> Gentle on skin and clothing fibers.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external body application only.</li>
  <li>Avoid spraying directly into eyes or onto irritated skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Any woman seeking a luxurious, long-lasting body mist enriched with notes of {scent_en}.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Rembrandt</td></tr>
  <tr><th>Category</th><td>Fragrances / Fine Body Mists & Perfume Sprays</td></tr>
  <tr><th>Product Type</th><td>Long-Lasting Fine Body Mist Spray (200ml)</td></tr>
  <tr><th>Volume/Weight</th><td>200 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types</td></tr>
  <tr><th>Finish</th><td>Scented, refreshed, hydrated & captivating body skin</td></tr>
  <tr><th>Texture</th><td>Clear non-sticky fine mist spray</td></tr>
  <tr><th>Fragrance</th><td>Luxurious {scent_en} fragrance notes</td></tr>
  <tr><th>Active Ingredients</th><td>Pure {scent_en} Oils, Skin Conditioners</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / France</td></tr>
  <tr><th>Manufacturer</th><td>Rembrandt Fine Fragrances</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Pulse Point Sillage & Fragrance Oils</h2>

<h3>What problem does this solve?</h3>
<p>Rembrandt Body Mist resolves rapid perfume fade, alcohol dryness, and sweat odor during warm weather.</p>

<h3>Why choose Rembrandt?</h3>
<p>Concentrated perfume oils of {scent_en} bind to skin hydration layers, broadcasting captivating sillage from pulse points.</p>"""

    en_faqs = [
        (f"What is Rembrandt {variant_en} Body Mist 200ml?", f"It is a fine body mist spray enriched with notes of {scent_en} in a generous 200ml bottle."),
        (f"What does {variant_en} smell like?", f"Features a luxurious, feminine scent of {scent_en}."),
        ("How long does the scent stay on skin?", "Stays on skin and clothes for hours without being harsh."),
        ("What volume is contained in this bottle?", "It comes in a 200ml bottle."),
        ("How do I use it correctly?", "Spray onto warm skin post-shower and focus on pulse points from 15 cm away."),
        ("Does it stain clothing?", "No, clear fine mist leaves zero residue on fabrics."),
        ("Where is Rembrandt manufactured?", "Produced adhering to French and Arabian fine fragrance standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Rembrandt mists at Ekleel Abha are 100% original from certified distributors."),
        ("Does it leave a sticky residue?", "No, absorbs quickly leaving skin fresh and smooth."),
        ("Is it safe for sensitive skin?", "Yes, gentle formula safe for body skin."),
        ("Is the 200ml bottle economical?", "Yes, generous volume provides months of daily usage."),
        ("Can it be sprayed lightly on hair ends?", "Yes, can be sprayed lightly on hair ends from a distance."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Is the spray nozzle reliable?", "Yes, dispenses a fine mist evenly."),
        ("Is it great for summer heat?", "Yes, perfect for refreshing body post-shower in warm weather."),
        ("What age group is it suitable for?", "Suitable for teens and adults aged 12+."),
        ("Does it boost confidence and elegance?", "Yes, captivating scent enhances feeling of fresh elegance."),
        ("Does the nozzle spray evenly?", "Yes, micro-fine nozzle covers body areas effortlessly."),
        ("Can it replace heavy evening perfumes?", "Great for lightweight daily scenting instead of heavy perfumes."),
        ("Is it great post-workout?", "Yes, provides instant post-workout shower freshness."),
        ("Does it contain harmful additives?", "Free from banned chemicals and health certified."),
        ("Are other Rembrandt variants available at Ekleel Abha?", "Yes, Ekleel Abha offers the full range of Rembrandt 200ml body mists."),
        ("Is it a great gift choice?", "Yes, elegant bottle and lovely scent make it a great gift."),
        ("Can it be sprayed on bed linens?", "Yes, can be used to lightly scent bed linens."),
        ("Does it leave a lasting memorable sillage?", "Yes, leaves a lovely memorable scent trail wherever you go.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "العطور / معطرات وبخاخات الجسم العطرية",
        "brand": "Rembrandt",
        "ar": {
            "title": title_ar,
            "meta_title": f"معطر جسم رامبرانت {variant_ar[:15]} 200مل | صيدلية إكليل أبها",
            "meta_description": f"اشتري {title_ar}. معطر جسم برائحة {scent_ar} لثبات وانتعاش يدوم طوال اليوم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["رامبرانت", "معطر_جسم_رامبرانت", "معطرات_الجسم", "إكليل_أبها"]
        },
        "en": {
            "title": title_en,
            "meta_title": f"Rembrandt {variant_en[:15]} Body Mist 200ml | Ekleel Abha",
            "meta_description": f"Buy original {title_en}. Long-lasting body mist with notes of {scent_en}. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["rembrandt", "body_mist", "fine_fragrance", "ekleel_abha"]
        },
        "schema": {
            "brand": "Rembrandt",
            "category": "Fragrance / Body Mist",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"{img_slug}.webp",
            "alt": title_en,
            "title": title_en
        }
    }

print("Loaded Batch 18 builders")
