import json, os

def create_product_1907():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول مورنينج إنرجي من كلين أند كلير 150 مل (Clean & Clear Morning Energy Face Wash 150ml)</strong> غسول الوجه المنعش اليومي الأيقوني المصمم لإيقاظ وتنظيف بشرة الوجه ومنحها دفعة من الحيوية والانتعاش كل صباح. يرتكز هذا الغسول (Clean & Clear Morning Energy Face Wash 150ml) على حبيبات الانتعاش الدقيقة (Bursting Beads)، خلاصة الليمون الحمضية المنعشة، وفيتامين C المجدد لإشراقة البشرة.</p>
<p>يعمل غسول كلين أند كلير مورنينج إنرجي على إزالة الزيوت والأوساخ المتراكمة طوال الليل، تفتيح وتنظيف المسامات العميقة، وإعادة الانتعاش والحيوية للبشرة الباهتة، ليترك وجهك ناصع النظافة، خافقاً بالحيوية، خفيفاً، ومشرقاً طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف عميق وإيقاظ للبشرة بحبيبات الانتعاش:</strong> تذوب الحبيبات عند التدليك لتطلق مفعول الانتعاش الفوري.</li>
  <li><strong>إزالة الدهون الزائدة والأوساخ المتراكمة:</strong> يمنع انسداد المسام وتكون البثور.</li>
  <li><strong>إشراق ونضارة بفضل خلاصة الليمون وفيتامين C:</strong> يمنح البشرة توهجاً وطاقة استثنائية.</li>
  <li><strong>خالٍ من الزيوت الثقيلة (Oil-Free):</strong> ينظف دون ترك أثر دهني أو ثقل على البشرة.</li>
  <li><strong>تركيبة خفيفة مناسبة للاستخدام اليومي الصباحي:</strong> لطيفة على البشرة دون جفاف شديد.</li>
  <li><strong>عبوة سعة 150 مل:</strong> حجم ممتاز يكفي لاستخدام يومي مستمر لعدة أشهر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (البلل):</strong> بللي الوجه بالماء الفاتر لفتح المسام.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية مناسبة من الغسول في كف اليد وكوّني رغوة غنية.</li>
  <li><strong>الخطوة الثالثة (التدليك الشامل):</strong> دلكي الوجه بحركات دائرية خفيفة حتى تذوب حبيبات الانتعاش ثم اشطفي جيداً بالماء البارد (يُستعمل صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>حبيبات الانتعاش (Bursting Beads):</strong> تذوب لتطلق مركبات النظافة والانتعاش الفوري.</li>
  <li><strong>خلاصة الليمون وفيتامين C:</strong> توحد لون البشرة وتمنحها طاقة وإشراقاً طبيعياً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء الفاتر فوراً.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن غسول كلين أند كلير مورنينج إنرجي 150 مل لإيقاظ وتنظيف بشرة الوجه يومياً.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كلين أند كلير (Clean & Clear)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / غسولات الوجه المنعشة اليومية من كلين أند كلير 150ml</td></tr>
  <tr><th>نوع المنتج</th><td>غسول وجه يومي بحبيبات الانتعاش وخلاصة الليمون وفيتامين C (150ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>150 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة العادية، الدهنية والمختلطة</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه مشرق، نظيف تماماً، منعش وخالٍ من الدهون الزائدة</td></tr>
  <tr><th>الملمس</th><td>جل جليدي شفاف بحبيبات ملونة تذوب بالتدليك</td></tr>
  <tr><th>العطر</th><td>عطر الليمون الحمضي المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>حبيبات الانتعاش (Bursting Beads)، خلاصة الليمون، فيتامين C</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا / المملكة المتحدة</td></tr>
  <tr><th>الشركة المصنعة</th><td>Clean & Clear (Johnson & Johnson)</td></tr>
  <tr><th>الفئة العمرية</th><td>المراهقون والبالغون (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد حبيبات الانتعاش وخلاصة الليمون في غسول مورنينج إنرجي</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول مورنينج إنرجي مشكلة خمول وبهتان بشرة الوجه صباحاً، تراكم الزيوت والأوساخ طوال الليل، والانسداد السطحي للمسام.</p>

<h3>لماذا تنجح تقنية حبيبات الانتعاش (Bursting Beads)؟</h3>
<p>لأن الحبيبات تحبس المكونات المنعشة وفيتامين C وتطلقها بتركيز عالٍ لحظة الاحتكاك والتدليك بالبشرة لنتائج فورية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام الصباحي الفوري:</strong> يُستعمل أول شيء صباحاً لإيقاظ البشرة وتنشيط الدورة الدموية.<br>
2. <strong>الشطف بالماء البارد:</strong> يغلق المسام النظيفة ويحبس الانتعاش الداخلي.<br>
3. <strong>التكميل بمرطب خفيف:</strong> يمنع الجفاف ويحفظ التوازن المائي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "حبيبات الغسول تخدش البشرة وتسبب التهابها."<br>
<strong>الحقيقة:</strong> حبيبات Bursting Beads ناعمة جداً تذوب تماماً بالتدليك دون أي خدش أو احتكاك قاسٍ.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تحتوي الكبسولات الميكروية على مستخلصات الليمون وفيتامين C المعزولة كيميائياً حتى لحظة الانفطار بالتفكك الميكانيكي، مما يضمن أقصى ثباتية للمكونات.</p>"""

    faqs = [
        ("ما هو غسول مورنينج انرجي من كلين اند كلير 150 مل؟", "هو غسول وجه يومي منعش بحبيبات الانتعاش وخلاصة الليمون وفيتامين C لإيقاظ وتنظيف البشرة (150 مل)."),
        ("ما هي فوائد حبيبات الانتعاش وخلاصة الليمون؟", "تطلق الحبيبات مركبات الانتعاش فورياً عند التدليك، بينما يمنح الليمون وفيتامين C البشرة إشراقاً ونضارة."),
        ("هل يزيل الزيوت والدهون الزائدة؟", "نعم، ينظف المسام ويزيل الدهون والأوساخ المتراكمة طوال الليل."),
        ("ما حجم العبوة؟", "تأتي بسعة 150 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الوجه، ضعي كمية وكوّني رغوة، دلكي بحركات دائرية حتى تذوب الحبيبات ثم اشطفي بالماء."),
        ("هل هو خالي من الزيوت الثقيلة؟", "نعم، تركيبة خالية من الزيوت (Oil-Free)."),
        ("أين صُنع غسول كلين أند كلير؟", "صُنع في فرنسا/المملكة المتحدة بواسطة Johnson & Johnson."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كلين أند كلير لدى إكليل أبها أصلية 100%."),
        ("هل يناسب البشرة الدهنية والمختلطة؟", "نعم، مناسب للبشرة العادية والدهنية والمختلطة."),
        ("ما رائحة غسول مورنينج إنرجي؟", "عطر الليمون الحمضي المنعش المشرق."),
        ("هل تذوب الحبيبات الملونة بسهولة؟", "نعم، تذوب تماماً بالتدليك وتطلق مكوناتها المنعشة."),
        ("هل 150 مل تكفي لفترة طويلة؟", "نعم، تكفي لعدة أشهر من الاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب المراهقين والبالغين؟", "نعم، من سن 12 سنة فما فوق."),
        ("هل يترك الوجه مشرقاً ومنعشاً؟", "نعم، يمنح دفعة حيوية وإشراقاً فورياً."),
        ("كم مرة يومياً؟", "صباحاً ومساءً."),
        ("هل يسبب جفاف شديد للبشرة؟", "لا، تركيبة لطيفة تنظف دون انتزاع الترطيب الطبيعي."),
        ("هل يساعد في منع البثور؟", "نعم، ينظف المسام من الزيوت المسببة للبثور."),
        ("هل هو غسول كلين أند كلير الأكثر طلباً؟", "نعم، Morning Energy من أشهر وأنجح غسولات كلين أند كلير عالمياً."),
        ("هل يناسب الاستخدام الصباحي قبل المكياج؟", "نعم، ينظف ويهيئ البشرة تماماً قبل وضع المكياج."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب البشرة الجافة جداً؟", "يُفضل استخدام مرطب بعده أصحاب البشرة الجافة جداً."),
        ("هل يترك أي أثر لزج؟", "لا، ينشطف بالماء تماماً دون لزوجة."),
        ("هل يصلح للسفر؟", "عبوة 150 مل مناسبة للحقائب اليومية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Clean & Clear Morning Energy Face Wash, 150ml</strong> is an iconic daily refreshing face wash formulated to awaken and cleanse facial skin, imparting a burst of energy and freshness every morning. Engineered with Bursting Beads technology, refreshing Citrus Lemon extract, and skin-brightening Vitamin C.</p>
<p>Clean & Clear Morning Energy Face Wash removes overnight oil accumulation and impurities, deeply cleanses pores, and revives dull tired skin, leaving your face spotlessly clean, energized, light, and radiant all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Deep Cleansing & Awakening with Bursting Beads:</strong> Beads burst on massage releasing immediate refreshing actives.</li>
  <li><strong>Excess Oil & Overnight Impurity Removal:</strong> Prevents clogged pores and breakout formation.</li>
  <li><strong>Radiance & Vitality with Lemon Extract & Vitamin C:</strong> Gives skin an extraordinary natural glow.</li>
  <li><strong>100% Oil-Free Formula:</strong> Cleanses without leaving greasy residue or heaviness.</li>
  <li><strong>Gentle Daily Morning Wash:</strong> Suitable for daily use without harsh dryness.</li>
  <li><strong>Generous 150ml Bottle:</strong> Excellent volume for months of daily continuous use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet face with warm water to open pores.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a suitable amount in palm and work into a rich lather.</li>
  <li><strong>Step 3 (Massage):</strong> Massage gently in circles until beads dissolve, rinse thoroughly with cold water (use morning and evening).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Bursting Beads:</strong> Micro-beads burst to release instant cleansing and refreshing compounds.</li>
  <li><strong>Lemon Extract & Vitamin C:</strong> Brighten skin tone and impart natural energy and radiance.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial skin application only.</li>
  <li>Avoid direct contact with eyes; rinse immediately with warm water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Clean & Clear Morning Energy 150ml Face Wash for daily skin awakening and deep cleansing.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Clean & Clear</td></tr>
  <tr><th>Category</th><td>Skincare / Clean & Clear Daily Refreshing Facial Washes 150ml</td></tr>
  <tr><th>Product Type</th><td>Bursting Beads & Lemon Vitamin C Refreshing Daily Face Wash (150ml)</td></tr>
  <tr><th>Volume/Weight</th><td>150 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Normal, Oily & Combination Facial Skin</td></tr>
  <tr><th>Finish</th><td>Spotlessly clean, radiant, refreshed & oil-free facial skin</td></tr>
  <tr><th>Texture</th><td>Clear gel texture with colored dissolving beads</td></tr>
  <tr><th>Fragrance</th><td>Refreshing citrus lemon aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Bursting Beads, Lemon Extract, Vitamin C</td></tr>
  <tr><th>Country of Origin</th><td>France / UK</td></tr>
  <tr><th>Manufacturer</th><td>Clean & Clear (Johnson & Johnson)</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Bursting Beads Encapsulation & Vitamin C Citrus Energy</h2>

<h3>What problem does this solve?</h3>
<p>Clean & Clear Morning Energy Face Wash resolves morning facial dullness, overnight oil accumulation, and surface pore clogging.</p>

<h3>Why choose Clean & Clear Morning Energy?</h3>
<p>Micro-encapsulated Bursting Beads isolate Lemon Extract and Vitamin C until mechanical friction breaks the capsule wall, delivering peak active potency upon application.</p>"""

    en_faqs = [
        ("What is Clean & Clear Morning Energy Face Wash, 150ml?", "It is a daily refreshing face wash with Bursting Beads, Lemon Extract, and Vitamin C for skin awakening and deep cleansing (150ml)."),
        ("What are the benefits of Bursting Beads and Lemon Extract?", "Beads burst to release instant refreshing actives, while Lemon and Vitamin C impart natural skin radiance."),
        ("Does it remove excess oils and impurities?", "Yes, cleanses pores and removes overnight oil and dirt accumulation."),
        ("What volume is contained in this bottle?", "150ml."),
        ("How do I use it correctly?", "Wet face, apply product into lather, massage until beads dissolve, rinse with water morning and evening."),
        ("Is it oil-free?", "Yes, 100% oil-free formula."),
        ("Where is Clean & Clear manufactured?", "In France/UK by Johnson & Johnson."),
        ("How do I verify authenticity at Ekleel Abha?", "All Clean & Clear products at Ekleel Abha are 100% original."),
        ("Is it suitable for oily and combination skin?", "Yes, suitable for normal, oily, and combination skin."),
        ("What does Morning Energy smell like?", "Refreshing bright citrus lemon aroma."),
        ("Do the beads dissolve easily?", "Yes, dissolve smoothly upon massage releasing refreshing ingredients."),
        ("Does the 150ml bottle last long?", "Yes, lasts months of daily use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for teens and adults?", "Yes, ages 12+."),
        ("Does it leave skin radiant and energized?", "Yes, imparts instant vitality and bright glow."),
        ("How many times daily?", "Morning and evening."),
        ("Does it cause harsh dryness?", "No, gentle formula cleanses without stripping natural moisture."),
        ("Does it help prevent breakouts?", "Yes, cleanses pores of breakout-causing oils."),
        ("Is it Clean & Clear's most famous wash?", "Yes, Morning Energy is among Clean & Clear's top global bestsellers."),
        ("Is it good before applying makeup?", "Yes, cleanses and prepares skin perfectly for makeup."),
        ("Is the bottle recyclable?", "Yes."),
        ("Is it suitable for very dry skin?", "Those with very dry skin should follow with a moisturizer."),
        ("Does it leave any sticky residue?", "No, rinses off completely clean without stickiness."),
        ("Is it travel-friendly?", "150ml size suitable for daily bags and travel."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1907",
        "sku": "EK-1907",
        "gtin": "3574660682243",
        "brand": "Clean & Clear",
        "ar": {
            "title": "غسول مورنينج انرجي  من كلين اند كلير، 150 مل",
            "meta_title": "غسول كلين أند كلير مورنينج إنرجي 150مل | إكليل أبها",
            "meta_description": "اشتري غسول مورنينج إنرجي من كلين أند كلير (150 مل). غسول منعش بحبيبات الانتعاش وفيتامين C لإيقاظ وتنظيف بشرة الوجه. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كلين_اند_كلير", "غسول_مورنينج_انرجي", "غسول_وجه_منعش", "حبيبات_الانتعاش", "إكليل_أبها"]
        },
        "en": {
            "title": "Clean & Clear Morning Energy Face Wash, 150ml",
            "meta_title": "Clean & Clear Morning Energy Face Wash 150ml | Ekleel Abha",
            "meta_description": "Buy original Clean & Clear Morning Energy Face Wash (150ml). Bursting Beads & Vitamin C refreshing daily face wash. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["clean_and_clear", "morning_energy_wash", "bursting_beads", "face_wash", "ekleel_abha"]
        }
    }


def create_product_1908():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>معجون أسنان سيجنال 100 مل (Signal Toothpaste 100ml)</strong> معجون الأسنان العائلي الكلاسيكي الأول من سيجنال المصمم لتوفير حماية متكاملة وقوية لأسنان جميع أفراد الأسرة ضد التسوس والبلاك. يرتكز هذا المعجون الأصيل (Signal Classic Toothpaste 100ml) على الفلوريد الفعّال المعزز (Active Fluoride)، الكالسيوم المقوي للمينا، وخلاصة النعناع الطبيعي المنعش.</p>
<p>يعمل معجون سيجنال الكلاسيكي على تقوية مينا الأسنان من الجذور، مكافحة تسوس الأسنان والبلاك، وتنظيف الفم بالكامل ومنحه عطراً منعشاً، ليترك أسنان جميع أفراد أسرتك قوية، ناصعة النظافة، ومحمية طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية متكاملة ضد التسوس بالفلوريد الفعّال:</strong> يقي الأسنان من الأحماض وبكتيريا التسوس.</li>
  <li><strong>تقوية المينا بالكالسيوم المقوي:</strong> يدعم بنية الأسنان ويمنع الهشاشة.</li>
  <li><strong>القضاء على البلاك والجير:</strong> ينظف أسطح الأسنان والفواصل بينها بكفاءة.</li>
  <li><strong>عطر نعناع طبيعي أنيق:</strong> يمنح الفم نفساً منعشاً ونظيفاً طوال اليوم.</li>
  <li><strong>معجون الأسنان العائلي الأول الموثوق:</strong> يناسب جميع أفراد الأسرة من الكبار والأطفال.</li>
  <li><strong>عبوة اقتصادية سعة 100 مل:</strong> تكفي لشهرين من الاستخدام الأسري المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية بحجم حبة البازلاء على فرشاة أسنان مناسبة.</li>
  <li><strong>الخطوة الثانية:</strong> نظفي الأسنان بحركات دائرية لطيفة لمدة دقيقتين كاملتين.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي الفم بالماء جيدا (يُستعمل مرتين يومياً: صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الفلوريد الفعّال والكالسيوم:</strong> يعيدان تمعدن المينا ويحميان الأسنان من التسوس والهششة.</li>
  <li><strong>خلاصة النعناع الطبيعي:</strong> تمنح الفم نفساً منعشاً ونظيفاً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام في تنظيف الأسنان فقط (لا يُبتلع).</li>
  <li>يُشرف على الأطفال دون سن 6 سنوات لضمان عدم الابتلاع.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل أسرة تبحث عن معجون أسنان سيجنال 100 مل للحماية اليومية الشاملة ضد التسوس.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سيجنال (Signal)</td></tr>
  <tr><th>الفئة</th><td>صحة الأسنان / معاجين أسنان سيجنال العائلية الكلاسيكية 100ml</td></tr>
  <tr><th>نوع المنتج</th><td>معجون أسنان عائلي بالفلوريد الفعّال والكالسيوم للحماية من التسوس (100ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>أسنان جميع أفراد الأسرة (من 6 سنوات فما فوق)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان ناصعة النظافة، مقواة المينا، خالية من البلاك وفم منعش</td></tr>
  <tr><th>الملمس</th><td>معجون كريمي كلاسيكي أبيض ناعم بنكهة نعناع لطيفة</td></tr>
  <tr><th>العطر</th><td>نكهة النعناع الطبيعي المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>فلوريد فعّال (Active Fluoride)، كالسيوم، خلاصة النعناع</td></tr>
  <tr><th>بلد المنشأ</th><td>مصر / الإمارات العربية المتحدة</td></tr>
  <tr><th>الشركة المصنعة</th><td>Signal (Unilever Group)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع أفراد الأسرة (من 6 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الفلوريد الفعّال والكالسيوم في معجون سيجنال الكلاسيكي (Signal)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج معجون سيجنال الكلاسيكي مشكلة تسوس الأسنان الأسري، تراكم البلاك والجير، وفقدان صلابة مينا الأسنان.</p>

<h3>لماذا تنجح تركيبة الفلوريد الفعّال والكالسيوم؟</h3>
<p>لأن الفلوريد الفعّال يعيد بناء المعدنيات في مينا الأسنان الضعيفة بينما يوفر الكالسيوم الدعم الهيكلي للمينا.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنظيف مرتين يومياً لمدة دقيقتين:</strong> صباحاً بعد الإفطار ومساءً قبل النوم.<br>
2. <strong>استخدام خيط الأسنان:</strong> لتنظيف الفواصل بين الأسنان التي لا تصلها الفرشاة.<br>
3. <strong>زيارة طبيب الأسنان كل 6 أشهر:</strong> لفحص صحة الأسنان واللثة بانتظام.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "معجون سيجنال الكلاسيكي يناسب الكبار فقط."<br>
<strong>الحقيقة:</strong> معجون سيجنال الكلاسيكي مصمم عائلياً وآمن للأطفال من سن 6 سنوات بكمية بحجم حبة البازلاء.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يتفاعل الفلوريد الفعّال مع هيدروكسيباتيت المينا مكوناً الفلورأباتيت الأكثر مقاومة للأحماض التي تفرزها البكتيريا.</p>"""

    faqs = [
        ("ما هو معجون أسنان سيجنال 100 مل؟", "هو معجون الأسنان العائلي الكلاسيكي من سيجنال بالفلوريد الفعّال والكالسيوم لحماية متكاملة ضد التسوس 100 مل."),
        ("ما هي فوائد الفلوريد الفعّال والكالسيوم؟", "يعيد الفلوريد الفعّال بناء المينا ويمنع التسوس، بينما يدعم الكالسيوم بنية الأسنان الصلبة."),
        ("هل يقي من تسوس الأسنان والبلاك؟", "نعم، مثبت سريرياً في الوقاية من التسوس وإزالة البلاك والجير."),
        ("ما حجم العبوة؟", "تأتي بسعة 100 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضع كمية حبة البازلاء على فرشاة مناسبة، نظف 2 دقيقة بحركات دائرية، اشطف جيداً مرتين يومياً."),
        ("هل يناسب جميع أفراد الأسرة؟", "نعم، مناسب للكبار والأطفال من 6 سنوات فما فوق."),
        ("أين صُنع معجون سيجنال؟", "صُنع في مصر/الإمارات بواسطة مجموعة Unilever."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات سيجنال لدى إكليل أبها أصلية 100%."),
        ("ما نكهة معجون سيجنال الكلاسيكي؟", "نكهة النعناع الطبيعي المنعش الأنيق."),
        ("هل يمنح نفساً منعشاً طوال اليوم؟", "نعم، يترك الفم معطراً ونظيفاً طوال اليوم."),
        ("هل 100 مل تكفي للاستخدام الأسري؟", "نعم، تكفي لشهرين من الاستخدام الأسري المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يبيض الأسنان بطريقة طبيعية؟", "ينظف أسطح الأسنان ويزيل الصفرة لإظهار البياض الطبيعي."),
        ("كم مرة يومياً؟", "مرتين يومياً: صباحاً ومساءً."),
        ("هل آمن للأطفال دون 6 سنوات؟", "يُفضل استخدام معاجين خاصة للأطفال دون 6 سنوات لضبط نسبة الفلوريد."),
        ("هل يمنع تراكم الجير؟", "نعم، التنظيف المنتظم يمنع تراكم البلاك والجير."),
        ("هل سيجنال علامة معتمدة عالمياً؟", "نعم، Signal علامة عالمية رائدة وموثوقة في صحة الأسنان منذ عقود."),
        ("هل تركيبه كريمي ناعم؟", "نعم، معجون كريمي كلاسيكي ناعم أبيض."),
        ("هل قابل لإعادة التدوير؟", "نعم."),
        ("هل يحمي اللثة؟", "نعم، إزالة البلاك تنعكس إيجابياً على صحة اللثة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يترك الفم خفيفاً بدون لزوجة؟", "نعم، ينشطف بالماء فورياً دون لزوجة."),
        ("هل يناسب الاستخدام مع الفرشاة الكهربائية؟", "نعم، مناسب للفرشاة العادية والكهربائية."),
        ("هل يصلح للمسافرين؟", "نعم، حجم 100 مل مناسب للمسافرين."),
        ("هل هو الأكثر مبيعاً في سيجنال؟", "نعم، Signal Classic من المعاجين الأكثر مبيعاً وثقة.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Signal Toothpaste 100ml</strong> is the iconic #1 family classic toothpaste from Signal formulated to provide comprehensive powerful protection for the entire family's teeth against cavities and plaque. Built upon Active Fluoride, strengthening Calcium, and natural Mint extract.</p>
<p>Signal Classic Toothpaste strengthens tooth enamel from roots, combats tooth decay and plaque buildup, and completely cleanses the mouth giving long-lasting fresh breath, leaving your entire family's teeth strong, spotlessly clean, and protected all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Comprehensive Cavity Protection with Active Fluoride:</strong> Shields teeth from decay-causing acids and bacteria.</li>
  <li><strong>Enamel Strengthening with Calcium:</strong> Supports tooth structure and prevents weakness.</li>
  <li><strong>Plaque & Tartar Elimination:</strong> Cleans tooth surfaces and interdental spaces efficiently.</li>
  <li><strong>Natural Mint Aroma:</strong> Gives the mouth clean fresh breath throughout the day.</li>
  <li><strong>Trusted #1 Family Toothpaste:</strong> Suitable for all family members, adults and kids.</li>
  <li><strong>Economical 100ml Tube:</strong> Lasts 2 months of continuous family use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a pea-sized amount onto a suitable toothbrush.</li>
  <li><strong>Step 2:</strong> Brush teeth in gentle circular motions for 2 full minutes.</li>
  <li><strong>Step 3:</strong> Rinse mouth thoroughly with water (use twice daily: morning and evening).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Active Fluoride & Calcium:</strong> Remineralize enamel and protect teeth against decay and weakness.</li>
  <li><strong>Natural Mint Extract:</strong> Gives mouth a clean fresh breath.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For tooth brushing use only (do not swallow).</li>
  <li>Supervise children under 6 years to ensure no swallowing.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every family seeking Signal 100ml Toothpaste for comprehensive daily cavity protection.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Signal</td></tr>
  <tr><th>Category</th><td>Dental Health / Signal Classic Family Toothpastes 100ml</td></tr>
  <tr><th>Product Type</th><td>Active Fluoride & Calcium Family Cavity Protection Toothpaste (100ml)</td></tr>
  <tr><th>Volume/Weight</th><td>100 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Family Members' Teeth (Ages 6+)</td></tr>
  <tr><th>Finish</th><td>Spotlessly clean, enamel-strengthened, plaque-free teeth & fresh mouth</td></tr>
  <tr><th>Texture</th><td>Classic smooth white creamy paste with gentle mint flavor</td></tr>
  <tr><th>Fragrance</th><td>Natural fresh mint aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Active Fluoride, Calcium, Mint Extract</td></tr>
  <tr><th>Country of Origin</th><td>Egypt / UAE</td></tr>
  <tr><th>Manufacturer</th><td>Signal (Unilever Group)</td></tr>
  <tr><th>Age Group</th><td>All Family Members (Ages 6+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Active Fluoride Fluorapatite Remineralization & Calcium Structural Support</h2>

<h3>What problem does this solve?</h3>
<p>Signal Classic Toothpaste solves family cavity risks, plaque and tartar accumulation, and enamel mineral loss.</p>

<h3>Why choose Signal Classic Toothpaste?</h3>
<p>Active Fluoride replaces hydroxyl ions in weakened enamel forming acid-resistant fluorapatite while Calcium supplies essential minerals for structural enamel integrity.</p>"""

    en_faqs = [
        ("What is Signal Toothpaste 100ml?", "It is the classic family toothpaste from Signal with Active Fluoride and Calcium for comprehensive cavity protection (100ml)."),
        ("What are the benefits of Active Fluoride and Calcium?", "Active Fluoride rebuilds enamel and prevents cavities, while Calcium supports structural tooth strength."),
        ("Does it protect against cavities and plaque?", "Yes, clinically proven to prevent cavities and eliminate plaque and tartar."),
        ("What volume is contained in this tube?", "100ml."),
        ("How do I use it correctly?", "Apply pea-sized amount on a brush, brush 2 minutes in circular motions, rinse thoroughly twice daily."),
        ("Is it suitable for the whole family?", "Yes, suitable for adults and children aged 6+."),
        ("Where is Signal manufactured?", "In Egypt/UAE by Unilever Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All Signal products at Ekleel Abha are 100% original."),
        ("What flavor does Signal Classic have?", "Natural fresh mint aroma."),
        ("Does it deliver fresh breath all day?", "Yes, leaves mouth fragranced and clean all day."),
        ("Does 100ml last long for family use?", "Yes, lasts about 2 months of continuous family use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Does it naturally whiten teeth?", "Cleans tooth surfaces removing yellowing to reveal natural whiteness."),
        ("How many times daily?", "Twice daily: morning and evening."),
        ("Is it safe for kids under 6?", "Kids under 6 should use specialized kids toothpaste to monitor fluoride intake."),
        ("Does it prevent tartar buildup?", "Yes, regular brushing prevents plaque and tartar accumulation."),
        ("Is Signal a globally trusted brand?", "Yes, Signal is a globally leading trusted dental brand for decades."),
        ("Is the texture smooth white cream?", "Yes, classic smooth white creamy paste."),
        ("Is the tube recyclable?", "Yes."),
        ("Does it protect gums?", "Yes, plaque removal positively impacts gum health."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it rinse easily?", "Yes, rinses off immediately with water without stickiness."),
        ("Is it suitable for electric toothbrushes?", "Yes, suitable for manual and electric toothbrushes."),
        ("Is it good for travel?", "Yes, 100ml size suitable for travel."),
        ("Is it Signal's #1 bestseller?", "Yes, Signal Classic is among Signal's most trusted bestsellers.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>[{a}</p>\n".replace("[","") for q, a in en_faqs])

    return {
        "product_id": "1908",
        "sku": "EK-1908",
        "gtin": "6221155117373",
        "brand": "Signal",
        "ar": {
            "title": "معجون أسنان سيجنال 100 مل",
            "meta_title": "معجون أسنان سيجنال الكلاسيكي 100مل | إكليل أبها",
            "meta_description": "اشتري معجون أسنان سيجنال الكلاسيكي (100 مل). معجون عائلي بالفلوريد الفعّال والكالسيوم لحماية متكاملة ضد التسوس. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["سيجنال", "معجون_أسنان_عائلي", "فلوريد_فعال", "حماية_من_التسوس", "إكليل_أبها"]
        },
        "en": {
            "title": "Signal Toothpaste 100ml",
            "meta_title": "Signal Toothpaste 100ml | Ekleel Abha",
            "meta_description": "Buy original Signal Toothpaste (100ml). Classic family Active Fluoride & Calcium cavity protection toothpaste. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["signal", "family_toothpaste", "active_fluoride", "cavity_protection", "ekleel_abha"]
        }
    }


def create_product_1909():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>معجون أسنان سنسوداين انتعاش زائد 50 مل (Sensodyne Extra Fresh Toothpaste 50ml)</strong> معجون الأسنان الطبي المتخصص الحارس لراحة الأسنان الحساسة والمزود بتقنية الانتعاش الزائد المضاعف من سنسوداين. يرتكز هذا المعجون الطبي الفاخر (Sensodyne Extra Fresh 50ml) على نترات البوتاسيوم الفعّالة (Potassium Nitrate)، الفلوريد لحماية المينا، ونكهة النعناع المنعش المضاعف (Extra Fresh Gel Stripe).</p>
<p>يعمل معجون سنسوداين انتعاش زائد على تهدئة وحماية أعصاب الأسنان الحساسة من ألم المشروبات المشروبة الباردة والساخنة، توفير حماية مستمرة لـ 24 ساعة من الحساسية، ومنح الفم موجة من الانتعاش الزائد الدائم، ليترك أسنانك الحساسة مرتاحة، قوية، وفمك فواحاً بالانتعاش الشديد.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>راحة وحماية مثبتة سريرياً للأسنان الحساسة:</strong> يهدئ ألم الحساسية الناتجة عن البارد والساخن والسكريات.</li>
  <li><strong>موجة انتعاش زائد مضاعف (Extra Freshness):</strong> يمنح نفساً فواحاً وانتعاشاً شديداً لساعات طويلة.</li>
  <li><strong>حماية 24 ساعة من الحساسية بالاستخدام المنتظم:</strong> يغلف أعصاب الأسنان بحجاب واقٍ.</li>
  <li><strong>تقوية المينا والوقاية من التسوس بالفلوريد:</strong> يعيد بناء معدنيات المينا الواقية.</li>
  <li><strong>معجون موصى به من أطباء الأسنان عالمياً:</strong> سنسوداين الماركة رقم 1 للأسنان الحساسة.</li>
  <li><strong>عبوة مدمجة 50 مل:</strong> سعة مناسبة للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية بحجم حبة البازلاء من معجون سنسوداين انتعاش زائد على فرشاة ناعمة.</li>
  <li><strong>الخطوة الثانية:</strong> نظفي الأسنان الحساسة برفق لمدة دقيقتين كاملتين دون ضغط شديد.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي الفم واقلبي البصق (يُستعمل مرتين يومياً ولا يزيد عن 3 مرات).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>نترات البوتاسيوم (Potassium Nitrate):</strong> تكتنف الأعصاب السنية وتمنع إشارات الألم للحساسية.</li>
  <li><strong>الفلوريد وجل النعناع المنعش:</strong> يقويان المينا ويمنحان موجة الانتعاش المضاعفة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام في تنظيف الأسنان فقط (لا يُبتلع).</li>
  <li>لا يناسب الأطفال دون سن 12 سنة إلا بمشورة طبيب الأسنان.</li>
  <li>إذا استمرت الحساسية استشر طبيب الأسنان فوراً.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من حساسيه الأسنان ويبحث عن معجون سنسوداين انتعاش زائد 50 مل للانتعاش الشديد والراحة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سنسوداين (Sensodyne)</td></tr>
  <tr><th>الفئة</th><td>صحة الأسنان / معاجين سنسوداين الطبية للأسنان الحساسة والانتعاش الزائد 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>معجون أسنان طبي مهدئ للأسنان الحساسة ومزود بشريط الجل المنعش (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>الأسنان الحساسة للمشروبات الباردة والساخنة (من 12 سنة)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان حساسة مرتاحة، خالية من الألم ومحمية، وفم شديد الانتعاش</td></tr>
  <tr><th>الملمس</th><td>معجون كريمي أبيض بشريط جل نعناعي أخضر/أزرق منعش</td></tr>
  <tr><th>العطر</th><td>نكهة النعناع المنعش الزائد (Extra Fresh Mint)</td></tr>
  <tr><th>المكونات النشطة</th><td>نترات البوتاسيوم (Potassium Nitrate)، فلوريد صوديوم، شريط الجل المنعش</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة المتحدة (UK)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Sensodyne (Haleon Group / GSK)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون والمراهقون (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد نترات البوتاسيوم وشريط الجل المنعش في سنسوداين (Sensodyne Extra Fresh)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج معجون سنسوداين انتعاش زائد ألم الأسنان الحساسة المفاجئ عند تناول البارد أو الساخن، مع معالجة النفس غير المنعش.</p>

<h3>لماذا تنجح تركيبة نترات البوتاسيوم المهدئة؟</h3>
<p>لأن أيونات البوتاسيوم الاختراقية تنفذ عبر القنوات العاجية لتثبيط إزالة الاستقطاب العصبي العصبي المسبب لألم الحساسية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنظيف مرتين يومياً بانتظام:</strong> التوقف عن الاستخدام يعيد حساسية الأسنان.<br>
2. <strong>تجنب الفرشاة الصلبة:</strong> استخدام فرشاة ناعمة يمنع انحسار اللثة وتعرية العاج.<br>
3. <strong>عدم المضمضة بالماء فورياً:</strong> البصق دون شطف مفرط يتيح للفلوريد والنترات العمل أطول.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "معجون الحساسية يخدّر الفم بالكامل."<br>
<strong>الحقيقة:</strong> نترات البوتاسيوم تعمل فقط على الأعصاب السنية الدقيقة داخل القنوات العاجية دون أي تأثير تخديري عمومي.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تزيد أيونات K+ من التركيز الخارجي حول محاور الأعصاب السنية، مما يمنع توليد جهد الفعل الناقل لإشارة الألم للدماغ.</p>"""

    faqs = [
        ("ما هو معجون أسنان سنسوداين انتعاش زائد 50 مل؟", "هو معجون أسنان طبي من سنسوداين بنترات البوتاسيوم والفلوريد وشريط الجل المنعش لتهدئة الأسنان الحساسة وانتعاش زائد 50 مل."),
        ("ما هي فوائد نترات البوتاسيوم والفلوريد وشريط الجل؟", "تهدئ نترات البوتاسيوم ألم الحساسية، يقوي الفلوريد المينا، ويمنح شريط الجل انتعاشاً شديداً."),
        ("هل يهدئ ألم الحساسية للبارد والساخن؟", "نعم، مثبت سريرياً في تهدئة ألم حساسيه الأسنان للبارد والساخن والسكريات."),
        ("ما حجم العبوة؟", "تأتي بسعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضع حبة البازلاء على فرشاة ناعمة، نظف 2 دقيقة برفق، ابصق واشطف مرتين يومياً."),
        ("هل هو موصى به من أطباء الأسنان؟", "نعم، سنسوداين الماركة رقم 1 الموصى بها من أطباء الأسنان عالمياً للحساسية."),
        ("أين صُنع سنسوداين انتعاش زائد؟", "صُنع في المملكة المتحدة بواسطة مجموعة Haleon (GSK سابقاً)."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات سنسوداين لدى إكليل أبها أصلية 100%."),
        ("ما نكهة سنسوداين انتعاش زائد؟", "نكهة النعناع المنعش الزائد الشديد (Extra Fresh Mint)."),
        ("هل يمنح حماية 24 ساعة من الحساسية؟", "نعم، مع الاستخدام المنتظم مرتين يومياً يوفر حماية 24 ساعة."),
        ("هل 50 مل مناسبة للسفر؟", "نعم، حجم مدمج مثالي للسفر والتنقل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب من هم دون 12 سنة؟", "لا يُفضل دون 12 سنة إلا بمشورة طبيب الأسنان."),
        ("كم مرة يومياً؟", "مرتين يومياً ولا يزيد عن 3 مرات."),
        ("هل يقوي مينا الأسنان؟", "نعم، الفلوريد يعيد بناء معدنيات المينا المقاومة للتسوس."),
        ("ما الفرق بينه وبين سنسوداين العادي؟", "يحتوي على شريط الجل المنعش المزود بانتعاش مضاعف ونكهة أشد."),
        ("هل يترك الفم فواحاً بالنعناع؟", "نعم، يترك موجة انتعاش شديدة تدوم لساعات."),
        ("هل يساعد في منع التسوس؟", "نعم، الفلوريد يقي الأسنان الحساسة من التسوس."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("ماذا أفعل إذا استمرت الحساسية؟", "يُنصح باستشارة طبيب الأسنان للتحقق من سلامة الجذور."),
        ("هل قابل لإعادة التدوير؟", "نعم."),
        ("هل يسبب حرقان في اللسان؟", "نكهته منعشة وقوية ولكنها آمنة وغير حارقة."),
        ("هل يناسب مستخدمي التقويم؟", "نعم، مناسب للأسنان الحساسة مع التقويم."),
        ("هل يبيض الأسنان أيضاً؟", "ينظف البقع السطحية ليحافظ على اللون الطبيعي."),
        ("هل سنسوداين الماركة الأولى عالمياً للحساسية؟", "نعم، Sensodyne الماركة الأكثر شهرة وتوصية للحساسية عالمياً.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Sensodyne Extra Fresh Toothpaste 50ml</strong> is a specialized medical toothpaste designed to safeguard sensitive teeth with Sensodyne's double extra fresh technology. Formulated with effective Potassium Nitrate, enamel-protecting Fluoride, and Extra Fresh Gel Stripe mint flavor.</p>
<p>Sensodyne Extra Fresh soothes and protects sensitive tooth nerves from cold and hot food/drink pain, provides continuous 24-hour sensitivity protection with regular use, and gives a lasting burst of extra freshness, leaving your sensitive teeth comfortable, strong, and highly refreshed.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Clinically Proven Sensitive Teeth Relief:</strong> Soothes sensitivity pain triggered by hot, cold, and sweet.</li>
  <li><strong>Double Extra Freshness Surge:</strong> Delivers intense long-lasting fresh breath for hours.</li>
  <li><strong>24-Hour Sensitivity Protection with Regular Use:</strong> Shields nerve endings inside dentinal tubules.</li>
  <li><strong>Enamel Strengthening & Cavity Protection with Fluoride:</strong> Remineralizes protective tooth enamel.</li>
  <li><strong>#1 Dentist Recommended Brand Worldwide:</strong> Sensodyne is globally recommended for sensitive teeth.</li>
  <li><strong>Compact 50ml Travel Size:</strong> Ideal volume for daily care and travel convenience.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a pea-sized amount of Sensodyne Extra Fresh onto a soft toothbrush.</li>
  <li><strong>Step 2:</strong> Brush sensitive teeth gently for 2 full minutes without pressing hard.</li>
  <li><strong>Step 3:</strong> Spit out and rinse mouth (use twice daily, max 3 times daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Potassium Nitrate:</strong> Calms sensitive tooth nerves blocking pain signals to the brain.</li>
  <li><strong>Fluoride & Extra Fresh Gel Stripe:</strong> Strengthen enamel and deliver double fresh mint surge.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For tooth brushing use only (do not swallow).</li>
  <li>Not suitable for children under 12 without dental consultation.</li>
  <li>Consult a dentist if sensitivity persists continuously.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from tooth sensitivity seeking Sensodyne Extra Fresh 50ml for intense freshness and relief.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Sensodyne</td></tr>
  <tr><th>Category</th><td>Dental Health / Sensodyne Medical Sensitive & Extra Fresh Toothpastes 50ml</td></tr>
  <tr><th>Product Type</th><td>Medical Potassium Nitrate Sensitive Teeth Relief & Extra Fresh Gel Toothpaste (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Sensitive Teeth to Cold & Hot (Ages 12+)</td></tr>
  <tr><th>Finish</th><td>Relieved, protected, pain-free sensitive teeth & intensely refreshed mouth</td></tr>
  <tr><th>Texture</th><td>Smooth white cream with green/blue extra fresh mint gel stripe</td></tr>
  <tr><th>Fragrance</th><td>Intense Extra Fresh Mint flavor</td></tr>
  <tr><th>Active Ingredients</th><td>Potassium Nitrate, Sodium Fluoride, Extra Fresh Gel Stripe</td></tr>
  <tr><th>Country of Origin</th><td>UK</td></tr>
  <tr><th>Manufacturer</th><td>Sensodyne (Haleon Group / GSK)</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Potassium Nitrate Nerve Depolarization Block & Extra Fresh Gel Technology</h2>

<h3>What problem does this solve?</h3>
<p>Sensodyne Extra Fresh Toothpaste resolves sharp sensitive tooth pain triggered by hot, cold, or sweet stimuli while eliminating bad breath.</p>

<h3>Why choose Sensodyne Extra Fresh Toothpaste?</h3>
<p>Potassium ions penetrate dentinal tubules elevating extracellular K+ concentration around sensory nerve endings, blocking action potential generation and pain signals.</p>"""

    en_faqs = [
        ("What is Sensodyne Extra Fresh Toothpaste 50ml?", "It is a medical toothpaste from Sensodyne with Potassium Nitrate, Fluoride, and Extra Fresh Gel Stripe for sensitive teeth relief and intense freshness (50ml)."),
        ("What are the benefits of Potassium Nitrate and Extra Fresh Gel Stripe?", "Potassium Nitrate calms sensitivity pain while the Extra Fresh Gel Stripe delivers intense mint freshness."),
        ("Does it soothe hot and cold sensitivity pain?", "Yes, clinically proven to soothe sensitive tooth pain from cold, hot, and sweet triggers."),
        ("What volume is contained in this tube?", "50ml."),
        ("How do I use it correctly?", "Apply pea-sized amount on a soft brush, brush 2 minutes gently, spit and rinse twice daily."),
        ("Is it dentist recommended?", "Yes, Sensodyne is the #1 dentist recommended brand for sensitive teeth worldwide."),
        ("Where is Sensodyne Extra Fresh manufactured?", "In the UK by Haleon Group (formerly GSK)."),
        ("How do I verify authenticity at Ekleel Abha?", "All Sensodyne products at Ekleel Abha are 100% original."),
        ("What flavor does Sensodyne Extra Fresh have?", "Intense Extra Fresh Mint flavor."),
        ("Does it provide 24-hour sensitivity protection?", "Yes, twice daily regular brushing provides 24-hour sensitivity protection."),
        ("Is 50ml travel friendly?", "Yes, compact size perfect for travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for under 12 years?", "Not recommended for children under 12 without dental advice."),
        ("How many times daily?", "Twice daily, maximum 3 times."),
        ("Does it strengthen tooth enamel?", "Yes, Fluoride remineralizes acid-weakened enamel."),
        ("How does it differ from regular Sensodyne?", "Features an Extra Fresh Gel Stripe for double fresh surge and bolder flavor."),
        ("Does it leave fresh mint breath for hours?", "Yes, leaves an intense fresh wave lasting hours."),
        ("Does it help prevent cavities?", "Yes, Fluoride protects sensitive teeth against cavities."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("What if sensitivity continues?", "Consult a dentist to verify root health if sensitivity persists."),
        ("Is the tube recyclable?", "Yes."),
        ("Is it suitable for braces users?", "Yes, suitable for sensitive teeth with braces."),
        ("Does it clean surface stains?", "Cleans surface stains maintaining natural whiteness."),
        ("Is Sensodyne the #1 global brand for sensitivity?", "Yes, Sensodyne is the most globally recognized brand for sensitivity."),
        ("Does it rinse easily?", "Rinses easily leaving a clean fresh feel.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1909",
        "sku": "EK-1909",
        "gtin": "018653005358",
        "brand": "Sensodyne",
        "ar": {
            "title": "معجون أسنان سنسوداين انتعاش زائد  50 مل",
            "meta_title": "معجون أسنان سنسوداين انتعاش زائد 50مل | إكليل أبها",
            "meta_description": "اشتري معجون أسنان سنسوداين انتعاش زائد (50 مل). معجون طبي بنترات البوتاسيوم والنعناع المكثف لتهدئة الأسنان الحساسة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["سنسوداين", "انتعاش_زائد", "أسنان_حساسة", "نترات_البوتاسيوم", "إكليل_أبها"]
        },
        "en": {
            "title": "Sensodyne Extra Fresh Toothpaste 50ml",
            "meta_title": "Sensodyne Extra Fresh Toothpaste 50ml | Ekleel Abha",
            "meta_description": "Buy original Sensodyne Extra Fresh Toothpaste (50ml). Medical Potassium Nitrate & Extra Fresh Gel for sensitive teeth relief. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["sensodyne", "extra_fresh", "sensitive_teeth", "potassium_nitrate", "ekleel_abha"]
        }
    }


def create_product_1910():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>معجون أسنان سنسوداين عناية متعددة 50 مل (Sensodyne Multi Care Toothpaste 50ml)</strong> معجون الأسنان الطبي الشامل والكامل من سنسوداين المصمم لتوفير 7 فوائد صحية متكاملة لراحة الأسنان الحساسة والعناية بالفم بالكامل. يرتكز هذا المعجون الطبي الفاخر (Sensodyne Multi Care 50ml) على نترات البوتاسيوم الفعّالة، الفلوريد، سترات الزنك المقاومة للجير (Zinc Citrate)، وخلاصة النعناع الطبيعي.</p>
<p>يعمل معجون سنسوداين عناية متعددة على تهدئة حادة لألم الأسنان الحساسة، مكافحة تسوس الأسنان والبلاك، منع تكوّن الجير، تعزيز صحة اللثة، وتبييض وتنعيم أسطح الأسنان، ليترك فمك متكاملاً في الصحة، راحة تامة من الحساسية، ونفساً منعشاً طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>راحة متكاملة من حساسية الأسنان:</strong> يهدئ آلام الحساسية الناتجة عن البارد والساخن والسكريات.</li>
  <li><strong>مكافحة منع تكوّن الجير والبلاك بسترية الزنك:</strong> يقلل ترسبات الجير والبلاكات على أسطح الأسنان.</li>
  <li><strong>تعزيز ودعم صحة اللثة:</strong> يحمي اللثة من الالتهاب والتنزف.</li>
  <li><strong>تقوية المينا ومكافحة التسوس بالفلوريد:</strong> يعيد بناء المينا الواقية كيميائياً.</li>
  <li><strong>تبييض لطيف وإزالة التلطخات السطحية:</strong> يعيد البياض الطبيعي للأسنان.</li>
  <li><strong>عبوة مدمجة 50 مل:</strong> حجم ممتاز للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية بحجم حبة البازلاء على فرشاة ناعمة.</li>
  <li><strong>الخطوة الثانية:</strong> نظفي الأسنان واللثة برفق لمدة دقيقتين كاملتين دون ضغط شديد.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي الفم واقلبي البصق (يُستعمل مرتين يومياً: صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>نترات البوتاسيوم وسترات الزنك:</strong> يهدئان الأعصاب الحساسة ويمنعان ترسبات الجير والبلاك.</li>
  <li><strong>الفلوريد والنعناع:</strong> يقويان المينا ويمنحان الفم نفساً منعشاً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام في تنظيف الأسنان فقط (لا يُبتلع).</li>
  <li>لا يناسب الأطفال دون سن 12 سنة إلا بمشورة طبيب الأسنان.</li>
  <li>إذا استمرت الحساسية استشر طبيب الأسنان.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من حساسية الأسنان ويبحث عن معجون سنسوداين عناية متعددة 50 مل للفوائد الشاملة 7 في 1.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سنسوداين (Sensodyne)</td></tr>
  <tr><th>الفئة</th><td>صحة الأسنان / معاجين سنسوداين الطبية للعناية المتعددة بالأسنان الحساسة 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>معجون أسنان طبي مهدئ للحساسية وعناية متعددة 7 في 1 بسترية الزنك والفلوريد (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>الأسنان الحساسة التي تحتاج إلى عناية شاملة (من 12 سنة)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان حساسة مرتاحة، لثة صحية، أسنان ناصعة البياض خالية من الجير</td></tr>
  <tr><th>الملمس</th><td>معجون كريمي أبيض ناعم بنكهة نعناع متوازنة</td></tr>
  <tr><th>العطر</th><td>نكهة النعناع الطبيعي المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>نترات البوتاسيوم، سترات الزنك (Zinc Citrate)، فلوريد صوديوم</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة المتحدة (UK) / إيرلندا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Sensodyne (Haleon Group / GSK)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون والمراهقون (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد سترات الزنك ونترات البوتاسيوم في سنسوداين عناية متعددة (Sensodyne Multi Care)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج معجون سنسوداين عناية متعددة مشكلة حساسية الأسنان، ترسب الجير، التهاب اللثة، والتسوس والتلطخ السطحي في منتج واحد.</p>

<h3>لماذا تنجح تركيبة العناية المتعددة (Multi Care)؟</h3>
<p>لأن نترات البوتاسيوم تهدئ الأعصاب، سترات الزنك تمنع تبلور فوسفات الكالسيوم المكون للجير، والفلوريد يقوي المينا.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنظيف مرتين يومياً:</strong> يضمن الحصول على الفوائد السبع المكتملة.<br>
2. <strong>العناية بخط اللثة:</strong> نظف بحركات دائرية خفيفة على خط اللثة لحمايتها من التنزف.<br>
3. <strong>استخدام خيط الأسنان يومياً:</strong> يكمل عمل المعجون في الفواصل الحساسة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "معجون العناية المتعددة أضعف في تهدئة الحساسية من المعجون المتخصص."<br>
<strong>الحقيقة:</strong> سنسوداين عناية متعددة يحتوي على نفس التركيز الطبي الكامل لنترات البوتاسيوم المهدئة بالإضافة إلى فوائد اللثة والجير.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط أيونات الزنك (Zn2+) تبلور الكالسيوم الهيدروكسيباتيتي إلى تراكمات جيرية صلبة، مما يمنع تكون الجير على أسطح الأسنان.</p>"""

    faqs = [
        ("ما هو معجون أسنان سنسوداين عناية متعددة 50 مل؟", "هو معجون أسنان طبي شامل من سنسوداين بنترات البوتاسيوم وسترات الزنك والفلوريد لتهدئة الأسنان الحساسة والعناية 7 في 1 (50 مل)."),
        ("ما هي الفوائد السبع لمعجون سنسوداين عناية متعددة؟", "تهدئة الحساسية، الوقاية من التسوس، إزالة البلاك، منع الجير، تعزيز صحة اللثة، التبييض اللطيف، وتنعيم النفس."),
        ("هل يمنع تكوّن الجير وتعزيز صحة اللثة؟", "نعم، سترات الزنك تمنع تبلور الجير وتحمي اللثة من الالتهاب."),
        ("ما حجم العبوة؟", "تأتي بسعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضع حبة البازلاء على فرشاة ناعمة، نظف 2 دقيقة برفق، ابصق واشطف مرتين يومياً."),
        ("هل هو موصى به من أطباء الأسنان؟", "نعم، سنسوداين الماركة رقم 1 الموصى بها عالمياً للحساسية والعناية المتعددة."),
        ("أين صُنع سنسوداين عناية متعددة؟", "صُنع في المملكة المتحدة/إيرلندا بواسطة مجموعة Haleon (GSK)."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات سنسوداين لدى إكليل أبها أصلية 100%."),
        ("ما نكهة سنسوداين عناية متعددة؟", "نكهة النعناع الطبيعي المنعش المتوازن."),
        ("هل يمنح حماية 24 ساعة من الحساسية؟", "نعم، الاستخدام المنتظم مرتين يومياً يمنح حماية دائم 24 ساعة."),
        ("هل 50 مل مناسبة للسفر والتنقل؟", "نعم، حجم مدمج مثالي للسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب من هم دون 12 سنة؟", "لا يُفضل دون 12 سنة إلا بمشورة طبيب الأسنان."),
        ("كم مرة يومياً؟", "مرتين يومياً: صباحاً ومساءً."),
        ("هل يبيض الأسنان بشكل طبيعي؟", "نعم، يزيل التلطخات السطحية ليظهر بياض الأسنان الطبيعي."),
        ("هل يحمي اللثة من التنزف؟", "نعم، مكافحة البلاك تمنع تنزف اللثة والتهابها."),
        ("هل يمنع التسوس؟", "نعم، الفلوريد يعيد بناء المينا ويقي من التسوس."),
        ("هل هو معجون العناية الشاملة الأفضل من سنسوداين؟", "نعم، Multi Care خيار العناية الأكثر شمولية وتكاملاً من سنسوداين."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يترك الفم معطراً بنقاء النعناع؟", "نعم، يترك نفساً خفيفاً ناصعاً بالنقاء."),
        ("هل قابل لإعادة التدوير؟", "نعم."),
        ("هل يناسب مستخدمي التقويم والتركيبات؟", "نعم، يناسب الأسنان الحساسة ذات التركيبات والتقويم."),
        ("هل يسبب حساسية باللثة؟", "لا، مصمم خصيصاً لحماية اللثة والأسنان الحساسة."),
        ("هل ينظف الفواصل بين الأسنان؟", "نعم، ينظف الفواصل بدقة مع الفرشاة المناسبة."),
        ("هل يناسب الاستخدام اليومي الدائم؟", "نعم، مصمم للاستخدام اليومي المستمر.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Sensodyne Multi Care Toothpaste 50ml</strong> is a comprehensive medical toothpaste designed to provide 7 all-in-one health benefits for sensitive teeth and total oral care. Formulated with effective Potassium Nitrate, Sodium Fluoride, anti-tartar Zinc Citrate, and natural Mint extract.</p>
<p>Sensodyne Multi Care soothes sensitive tooth pain, combats cavities and plaque, prevents tartar formation, promotes gum health, and gently whitens tooth enamel, leaving your mouth healthy, relieved from sensitivity, and refreshed all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>All-in-One Sensitive Teeth Relief:</strong> Soothes sensitivity pain triggered by hot, cold, and sweet.</li>
  <li><strong>Tartar & Plaque Prevention with Zinc Citrate:</strong> Reduces tartar crystallization and plaque accumulation.</li>
  <li><strong>Gum Health Enhancement:</strong> Protects gums from inflammation and bleeding.</li>
  <li><strong>Enamel Strengthening & Cavity Protection with Fluoride:</strong> Chemically remineralizes protective enamel.</li>
  <li><strong>Gentle Whitening & Stain Removal:</strong> Restores natural tooth whiteness.</li>
  <li><strong>Compact 50ml Travel Size:</strong> Excellent volume for daily use and travel convenience.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a pea-sized amount onto a soft toothbrush.</li>
  <li><strong>Step 2:</strong> Brush teeth and gums gently for 2 full minutes without pressing hard.</li>
  <li><strong>Step 3:</strong> Spit out and rinse mouth (use twice daily: morning and evening).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Potassium Nitrate & Zinc Citrate:</strong> Soothe sensitive nerves and prevent tartar/plaque crystallization.</li>
  <li><strong>Fluoride & Mint:</strong> Strengthen enamel and impart fresh breath.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For tooth brushing use only (do not swallow).</li>
  <li>Not suitable for children under 12 without dental consultation.</li>
  <li>Consult a dentist if sensitivity persists.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with sensitive teeth seeking Sensodyne Multi Care 50ml for comprehensive 7-in-1 oral protection.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Sensodyne</td></tr>
  <tr><th>Category</th><td>Dental Health / Sensodyne Medical Multi Care Sensitive Toothpastes 50ml</td></tr>
  <tr><th>Product Type</th><td>Medical 7-in-1 Sensitive Teeth Relief & Anti-Tartar Zinc Citrate Toothpaste (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Sensitive Teeth Needing Total Oral Care (Ages 12+)</td></tr>
  <tr><th>Finish</th><td>Relieved sensitive teeth, healthy gums, white tartar-free teeth & fresh breath</td></tr>
  <tr><th>Texture</th><td>Smooth white creamy paste with balanced natural mint flavor</td></tr>
  <tr><th>Fragrance</th><td>Natural balanced fresh mint aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Potassium Nitrate, Zinc Citrate, Sodium Fluoride</td></tr>
  <tr><th>Country of Origin</th><td>UK / Ireland</td></tr>
  <tr><th>Manufacturer</th><td>Sensodyne (Haleon Group / GSK)</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Zinc Citrate Calcium Phosphate Crystal Inhibition & Potassium Nerve Desensitization</h2>

<h3>What problem does this solve?</h3>
<p>Sensodyne Multi Care Toothpaste resolves sensitive tooth pain, tartar crystallization, gum inflammation, cavities, and surface staining in one formula.</p>

<h3>Why choose Sensodyne Multi Care Toothpaste?</h3>
<p>Zinc ions (Zn2+) inhibit hydroxyapatite calcium phosphate crystal growth into solid tartar deposits while Potassium Nitrate desensitizes sensory nerve fibers.</p>"""

    en_faqs = [
        ("What is Sensodyne Multi Care Toothpaste 50ml?", "It is a comprehensive medical toothpaste from Sensodyne with Potassium Nitrate, Zinc Citrate, and Fluoride for 7-in-1 sensitive teeth care (50ml)."),
        ("What are the 7 benefits of Sensodyne Multi Care?", "Sensitivity relief, cavity protection, plaque removal, tartar prevention, gum health support, gentle whitening, and fresh breath."),
        ("Does it prevent tartar formation and promote gum health?", "Yes, Zinc Citrate prevents tartar crystallization and protects gums from inflammation."),
        ("What volume is contained in this tube?", "50ml."),
        ("How do I use it correctly?", "Apply pea-sized amount on a soft brush, brush 2 minutes gently, spit and rinse twice daily."),
        ("Is it dentist recommended?", "Yes, Sensodyne is the #1 global dentist recommended brand for sensitivity and multi-care."),
        ("Where is Sensodyne Multi Care manufactured?", "In UK/Ireland by Haleon Group (GSK)."),
        ("How do I verify authenticity at Ekleel Abha?", "All Sensodyne products at Ekleel Abha are 100% original."),
        ("What flavor does Sensodyne Multi Care have?", "Natural balanced fresh mint flavor."),
        ("Does it provide 24-hour sensitivity protection?", "Yes, twice daily regular use provides 24-hour continuous sensitivity relief."),
        ("Is 50ml compact for travel?", "Yes, ideal travel-friendly size."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for under 12 years?", "Not recommended for children under 12 without dental advice."),
        ("How many times daily?", "Twice daily: morning and evening."),
        ("Does it naturally whiten teeth?", "Yes, removes surface stains restoring natural tooth whiteness."),
        ("Does it protect gums from bleeding?", "Yes, plaque control prevents gum inflammation and bleeding."),
        ("Does it prevent cavities?", "Yes, Fluoride remineralizes enamel protecting against decay."),
        ("Is it Sensodyne's most complete toothpaste?", "Yes, Multi Care is Sensodyne's most comprehensive 7-in-1 formula."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it leave mouth fresh?", "Yes, leaves breath naturally pure and mint-fresh."),
        ("Is the tube recyclable?", "Yes."),
        ("Is it suitable for braces and crowns?", "Yes, suitable for sensitive teeth with braces and crowns."),
        ("Does it cause gum sensitivity?", "No, specially designed to protect gums and sensitive teeth."),
        ("Does it clean between teeth?", "Yes, cleans interdental spaces when used with proper toothbrushing."),
        ("Is it safe for long-term daily use?", "Yes, designed for continuous long-term daily use.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1910",
        "sku": "EK-1910",
        "gtin": "5000198257502",
        "brand": "Sensodyne",
        "ar": {
            "title": "معجون أسنان سنسوداين عناية متعددة 50 مل",
            "meta_title": "معجون أسنان سنسوداين عناية متعددة 50مل | إكليل أبها",
            "meta_description": "اشتري معجون أسنان سنسوداين عناية متعددة (50 مل). معجون طبي بنترات البوتاسيوم وسترات الزنك لعناية 7 في 1 بالأسنان الحساسة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["سنسوداين", "عناية_متعددة", "أسنان_حساسة", "سترات_الزنك", "إكليل_أبها"]
        },
        "en": {
            "title": "Sensodyne Multi Care Toothpaste 50ml",
            "meta_title": "Sensodyne Multi Care Toothpaste 50ml | Ekleel Abha",
            "meta_description": "Buy original Sensodyne Multi Care Toothpaste (50ml). Medical 7-in-1 Potassium Nitrate & Zinc Citrate sensitive toothpaste. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["sensodyne", "multi_care", "sensitive_teeth", "zinc_citrate", "ekleel_abha"]
        }
    }


def create_product_1911():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>زيت للأطفال من نونو 200 مل (Nunu Baby Oil - 200 ml)</strong> زيت الأطفال اللطيف الفاخر من نونو المصمم خصيصاً لحماية وترطيب وتغذية بشرة الرضع والأطفال الرقيقة بكل أمان وحب. يرتكز هذا الزيت الطبي (Nunu Baby Oil 200ml) على الزيت المعدني النقي المنقى طبياً (Pure Medical Grade Mineral Oil)، خلاصة البابونج المهدئة، وفيتامين E المغذي للبشرة.</p>
<p>يعمل زيت نونو للأطفال على حبس الترطيب الداخلي لبشرة الطفل بمقدار 10 أضعاف مقارنة باللوشن العادي، تهدئة وتلطيف الجلد المتهيجة والجاف، وتأمين تدليك ناعم مريح يبعث الاسترخاء في جسم الطفل، ليترك بشرة طفلك ناعمة كالحرير، مرطبة عمقاً، ومعطرة بعطر نونو الدافئ.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حبس الترطيب الداخلي بمقدار 10 أضعاف:</strong> يحفظ الرطوبة الطبيعية لبشرة الطفل الرقيقة.</li>
  <li><strong>تغذية وتهدئة ببشرة الطفل بخلاصة البابونج وفيتامين E:</strong> يهدئ الجفاف والاحمرار.</li>
  <li><strong>مثالي لتدليك الطفل اليومي (Baby Massage):</strong> يساعد في استرخاء الطفل ونومه الهادئ.</li>
  <li><strong>تركيبة خفيفة خالية من البارابين والصبغات:</strong> آمنة ولطيفة 100% لبشرة الرضع من الولادة.</li>
  <li><strong>عطر نونو الخاص بالطفولة:</strong> يمنح الطفل رائحة دافئة ناعمة مريحة.</li>
  <li><strong>عبوة اقتصادية 200 مل:</strong> كمية وافرة تكفي لاستخدام يومي مستمر لعدة أشهر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق بعد الاستحمام):</strong> ضعي بضع قطرات من زيت نونو على راحة يدك وهي دافئة.</li>
  <li><strong>الخطوة الثانية (التدليك):</strong> دلّكي بشرة الطفل المبللة أو الجافة برفق بحركات دائرية ناعمة.</li>
  <li><strong>الخطوة الثالثة (التجفيف):</strong> جففي البشرة برفق بفوطة ناعمة (يُستعمل بعد كل استحمام وقبل النوم).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الزيت المعدني المنقى طبياً (Medical Grade Mineral Oil):</strong> يشكّل غلافاً واقياً يحبس الترطيب الداخلي.</li>
  <li><strong>خلاصة البابونج وفيتامين E:</strong> يغذيان البشرة ويهدئان الالتهاب والجفاف.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على بشرة جسم الطفل فقط.</li>
  <li>تجنب التلامس مع العينين والوجه المباشر.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل أم تبحث عن زيت نونو للأطفال 200 مل لترطيب وتدليك وحماية بشرة طفلها الرقيقة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>نونو (Nunu)</td></tr>
  <tr><th>الفئة</th><td>العناية بالأطفال / زيوت نونو المرطبة لتدليك وحماية بشرة الأطفال 200ml</td></tr>
  <tr><th>نوع المنتج</th><td>زيت طفل مرطب وفاخر بحبس الترطيب 10 أضعاف بخلاصة البابونج وفيتامين E (200ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>200 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>بشرة الأطفال الرضع والصغار الرقيقة الحساسة (من الولادة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة طفل ناعمة كالحرير، مرطبة 10 أضعاف، مهدأة ومعطرة بعطر دافئ</td></tr>
  <tr><th>الملمس</th><td>زيت خفيف شفاف ينزلق بنعومة وسرعة</td></tr>
  <tr><th>العطر</th><td>عطر نونو اللطيف الخاص بالأطفال</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت معدني منقى طبياً، خلاصة البابونج، فيتامين E</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Nunu Baby Care Products</td></tr>
  <tr><th>الفئة العمرية</th><td>الرضع والأطفال (من الولادة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الزيت المعدني المنقى وفيتامين E في زيت نونو للأطفال</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج زيت نونو للأطفال مشكلة جفاف بشرة الطفل الشديد بعد الاستحمام، قشرة الرأس لدى الرضع، وصعوبة الاسترخاء قبل النوم.</p>

<h3>لماذا ينجح الزيت المعدني المنقى في حبس الترطيب 10 أضعاف؟</h3>
<p>لأن الزيت المعدني يشكل طبقة انسدادية آمنة (Occlusive Barrier) تمنع تبخر الماء عبر البشرة (TEWL) بمقدار 10 أضعاف مقارنة باللوشنات المائية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على بشرة رطبة بعد الاستحمام مباشرة:</strong> يحبس أقصى كمية من الماء الداخلي.<br>
2. <strong>جلسة تدليك قبل النوم:</strong> تدليك جسم الطفل بالزيت يهدئ الجهاز العصبي وينشط النوم العميق.<br>
3. <strong>إزالة قشرة الرأس لدى الرضع:</strong> وضع قطرات على فروة الرأس قبل الاستحمام بـ 15 دقيقة ثم تمشيطها برفق.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الزيوت المعدنية تسد مسام بشرة الطفل."<br>
<strong>الحقيقة:</strong> الزيت المعدني المنقى طبياً في نونو غير مسبب للانسداد (Non-Comedogenic) ومخصص لسلامة الرضع.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تكوّن الهيدروكربونات المشبعة ذات السلسلة الطويلة غشاء هيدروفوبياً كاره للماء يمنع فقدان الماء عبر البشرة بنسبة 98%.</p>"""

    faqs = [
        ("ما هو زيت للأطفال من نونو 200 مل؟", "هو زيت مرطب وفاخر للأطفال من نونو بالزيت المعدني المنقى والبابونج وفيتامين E لحبس الترطيب 10 أضعاف وتدليك الطفل (200 مل)."),
        ("ما هي فوائد الزيت المعدني والبابونج وفيتامين E؟", "يحبس الزيت المعدني الترطيب 10 أضعاف، يهدئ البابونج الجلد المتهيج، ويغذي فيتامين E البشرة."),
        ("هل يحبس الترطيب 10 أضعاف مقارنة باللوشن؟", "نعم، يكوّن طبقة واقية تحبس الرطوبة الطبيعية بمقدار 10 أضعاف مقارنة باللوشن العادي."),
        ("ما حجم العبوة؟", "تأتي بسعة 200 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي قطرات على يدك الدافئة، دلكي بشرة الطفل المبللة أو الجافة بحركات دائرية ناعمة بعد الاستحمام."),
        ("هل هو آمن للرضع من الولادة؟", "نعم، تركيبة لطيفة آمنة 100% للرضع والأطفال من الولادة."),
        ("أين صُنع زيت نونو للأطفال؟", "صُنع في المملكة العربية السعودية بواسطة Nunu Baby Care."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات نونو لدى إكليل أبها أصلية 100%."),
        ("هل هو ممتاز لتدليك الطفل (Baby Massage)؟", "نعم، ملمسه الخفيف السلس يجعله الزيت المثالي لتدليك الطفل واسترخائه."),
        ("ما رائحة زيت نونو للأطفال؟", "عطر نونو اللطيف الدافئ الخاص بالأطفال."),
        ("هل يساعد في إزالة قشرة الرأس لدى الرضع؟", "نعم، ضعي قطرات على فروة الرأس قبل الاستحمام وتمشطي برفق لإزالة قشرة الرأس."),
        ("هل 200 مل تكفي لفترة طويلة؟", "نعم، عبوة 200 مل تكفي لعدة أشهر من الاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل هو خالي من البارابين والصبغات؟", "نعم، 100% خالي من البارابين والصبغات الكيميائية."),
        ("هل يترك بشرة الطفل ناعمة كالحرير؟", "نعم، يضمن بشرة طفل ناعمة جداً ومرطبة عمقاً."),
        ("كم مرة يُفضل استخدامه؟", "يُستعمل بعد كل استحمام وقبل النوم لتدليك الطفل."),
        ("هل يناسب البشرة الجافة جداً والحساسة؟", "نعم، يحمي ويهدئ البشرة الجافة والحساسة للطفل."),
        ("هل يمتص بسلاسة على البشرة الرطبة؟", "نعم، ينتشر ويمتص بسلاسة مدهشة على البشرة الرطبة."),
        ("هل زيت نونو محبوب لدى الأمهات؟", "نعم، زيت نونو من أكثر زيوت الأطفال شهرة وثقة لدى الأمهات."),
        ("هل يمكن استخدامه لإزالة مكياج الأم؟", "نعم، الأم يمكنها استخدامه كإزالة لطيفة لمكياج العينين والوجه."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب جميع فصول السنة؟", "نعم، مناسب للصيف والشتاء لحماية بشرة الطفل."),
        ("هل يمنع الجفاف والاحتكاك؟", "نعم، يمنع الجفاف الجلدي والاحتكاك."),
        ("هل يصلح هدية لمولود جديد؟", "نعم، هدية عملية ومميزة جداً لكل مولود جديد."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Nunu Baby Oil - 200 ml</strong> is a gentle luxury baby oil from Nunu specifically designed to protect, hydrate, and nourish delicate infant skin safely and lovingly. Formulated with Pure Medical Grade Mineral Oil, soothing Chamomile extract, and skin-nourishing Vitamin E.</p>
<p>Nunu Baby Oil locks in up to 10 times more moisture on wet skin than ordinary lotion, calms dry irritated skin, and provides a soothing, relaxing massage experience, leaving your baby's skin silky soft, deeply hydrated, and sweetly fragranced with Nunu's signature baby scent.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Locks in Up to 10 Times More Moisture:</strong> Preserves natural skin hydration on baby's delicate skin.</li>
  <li><strong>Nourishes & Soothes with Chamomile & Vitamin E:</strong> Relieves dryness and calms skin irritation.</li>
  <li><strong>Ideal for Daily Baby Massage:</strong> Helps relax baby and promotes peaceful sleep.</li>
  <li><strong>Paraben-Free & Dye-Free Formula:</strong> 100% safe and gentle for infants from birth.</li>
  <li><strong>Gentle Nunu Baby Fragrance:</strong> Imparts a warm, comforting baby scent.</li>
  <li><strong>Generous 200ml Bottle:</strong> Lasts months of daily continuous baby care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply After Bath):</strong> Apply a few drops onto your warm palms.</li>
  <li><strong>Step 2 (Massage):</strong> Massage gently into baby's damp or dry skin in smooth circular motions.</li>
  <li><strong>Step 3 (Pat Dry):</strong> Gently pat dry with a soft towel (use after bath and before bedtime).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Medical Grade Mineral Oil:</strong> Forms a protective occlusive barrier locking in moisture.</li>
  <li><strong>Chamomile Extract & Vitamin E:</strong> Nourish skin and soothe dryness and irritation.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external baby skin application only.</li>
  <li>Avoid direct contact with eyes and face.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every mother seeking Nunu Baby Oil 200ml for baby skin hydration, massage, and gentle protection.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Nunu</td></tr>
  <tr><th>Category</th><td>Baby Care / Nunu Hydrating Baby Oils for Massage & Protection 200ml</td></tr>
  <tr><th>Product Type</th><td>Medical Mineral Oil & Chamomile 10x Moisture Lock Baby Oil (200ml)</td></tr>
  <tr><th>Volume/Weight</th><td>200 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Sensitive Delicate Infant & Child Skin (From Birth)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 10x hydrated, soothed & warmly fragranced baby skin</td></tr>
  <tr><th>Texture</th><td>Clear lightweight silky smooth oil fluid</td></tr>
  <tr><th>Fragrance</th><td>Gentle signature Nunu baby fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Medical Grade Mineral Oil, Chamomile Extract, Vitamin E</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia</td></tr>
  <tr><th>Manufacturer</th><td>Nunu Baby Care Products</td></tr>
  <tr><th>Age Group</th><td>Infants & Children (From Birth)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Medical Mineral Oil Occlusive Barrier & Vitamin E Skin Nutrition</h2>

<h3>What problem does this solve?</h3>
<p>Nunu Baby Oil resolves severe post-bath infant skin dryness, cradle cap in infants, and restlessness before bedtime.</p>

<h3>Why choose Nunu Baby Oil 200ml?</h3>
<p>Medical Grade Mineral Oil creates a safe occlusive barrier reducing transepidermal water loss (TEWL) by up to 10 times compared to aqueous lotions.</p>"""

    en_faqs = [
        ("What is Nunu Baby Oil - 200 ml?", "It is a gentle hydrating baby oil from Nunu with Medical Grade Mineral Oil, Chamomile, and Vitamin E for 10x moisture lock and massage (200ml)."),
        ("What are the benefits of Mineral Oil, Chamomile, and Vitamin E?", "Mineral Oil locks in 10x moisture, Chamomile calms irritated skin, and Vitamin E nourishes."),
        ("Does it lock in 10x more moisture than lotion?", "Yes, forms a protective barrier locking in 10x more natural moisture on damp skin than lotion."),
        ("What volume is contained in this bottle?", "200ml."),
        ("How do I use it correctly?", "Apply drops on warm palms, massage into damp or dry skin in circular motions after bath."),
        ("Is it safe for infants from birth?", "Yes, 100% safe and gentle formula for infants from birth."),
        ("Where is Nunu Baby Oil manufactured?", "In Saudi Arabia by Nunu Baby Care Products."),
        ("How do I verify authenticity at Ekleel Abha?", "All Nunu products at Ekleel Abha are 100% original."),
        ("Is it ideal for baby massage?", "Yes, lightweight silky texture makes it the ideal oil for baby massage and relaxation."),
        ("What does Nunu Baby Oil smell like?", "Gentle signature warm Nunu baby fragrance."),
        ("Does it help remove infant cradle cap?", "Yes, apply drops to scalp 15 minutes before bath and comb gently."),
        ("Does the 200ml bottle last long?", "Yes, lasts months of daily baby care use."),
        ("How should I store it?", "In a cool, dry place away from direct sunlight."),
        ("Is it paraben-free and dye-free?", "Yes, 100% free of parabens and chemical dyes."),
        ("Does it leave baby skin silky soft?", "Yes, ensures touchably soft, deeply hydrated skin."),
        ("How often should I use it?", "Use after bath and before bedtime for baby massage."),
        ("Is it suitable for dry sensitive skin?", "Yes, protects and soothes dry sensitive infant skin."),
        ("Does it absorb smoothly on damp skin?", "Yes, spreads and absorbs smoothly on damp skin."),
        ("Is Nunu a trusted baby brand?", "Yes, Nunu is a highly trusted and beloved baby care brand."),
        ("Can mothers use it for makeup removal?", "Yes, mothers can use it as a gentle eye and face makeup remover."),
        ("Is the bottle recyclable?", "Yes."),
        ("Is it suitable for all seasons?", "Yes, ideal for summer and winter baby skin protection."),
        ("Does it prevent skin dryness and chafing?", "Yes, prevents skin dryness and friction chafing."),
        ("Is it a good newborn gift?", "Yes, a practical and thoughtful newborn baby gift."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1911",
        "sku": "EK-1911",
        "gtin": "6281053212136",
        "brand": "Nunu",
        "ar": {
            "title": "زيت للاطفال من نونو 200 مل",
            "meta_title": "زيت الأطفال نونو 200مل | إكليل أبها",
            "meta_description": "اشتري زيت الأطفال من نونو (200 مل). زيت مرطب بالبابونج وفيتامين E لحبس الترطيب 10 أضعاف وتدليك الطفل. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["نونو", "زيت_أطفال", "ترطيب_10_أضعاف", "تدليك_الطفل", "إكليل_أبها"]
        },
        "en": {
            "title": "Nunu Baby Oil - 200 ml",
            "meta_title": "Nunu Baby Oil 200ml | Ekleel Abha",
            "meta_description": "Buy original Nunu Baby Oil (200ml). Hydrating Mineral Oil & Chamomile baby oil for 10x moisture lock and massage. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["nunu", "baby_oil", "10x_moisture_lock", "baby_massage", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 39 builders complete")
