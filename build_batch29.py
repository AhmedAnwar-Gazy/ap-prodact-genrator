import json, os

def create_product_1851():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>صابون كوجي سان لتفتيح البشرة ثلاث عبوات 100 جم (Kojie San Skin Lightening Soap - Pack of 3)</strong> الصابون الفلبيني الطبيعي الشهير والأكثر مبيعاً عالمياً لتفتيح التصبغات، توحيد لون الوجه والجسم، والتخلص من البقع الداكنة وآثار حب الشباب. يرتكز هذا الصابون الأصلي من كوجي سان (Kojie San Kojic Acid Soap) على حمض الكوجيك الطبيعي 100% (Pure Kojic Acid) المستخرج من تخمير الأرز وزيت جوز الهند النقي.</p>
<p>تعمل صابونة كوجي سان على تثبيط إنزيم التايروسينيز المسبب للتصبغات، تقشير الخلايا الميتة برفق، وتفتيح اسمرار الوجه والجسم والمناطق الحساسة، لتوفر لكِ بشرة ناصعة، موحدة، ومشعّة بالنضارة والصفاء من أول استخدامات.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح طبيعي ومكثف بحمض الكوجيك الأصلي:</strong> يزيل التصبغات، الكلف، والبقع الداكنة ب فاعلية فائقة.</li>
  <li><strong>توحيد لون الوجه والجسم والمناطق الحساسة:</strong> يعالج اسمرار الأكواع، الركب، والمناطق المجهدة.</li>
  <li><strong>معزز بزيت جوز الهند والزيت العطري:</strong> يغذي الجلد ويمنع الجفاف الشديد أثناء التقشير.</li>
  <li><strong>تقشير لطيف للخلايا الميتة وآثار الأكنيه:</strong> يزيل بقايا البثور ويكشف عن بشرة جديدة ناصعة.</li>
  <li><strong>عبوة اقتصادية ثلاثية (3 × 100 جم):</strong> توفير ممتازة يضمن استمرار روتين التفتيح لأشهر طويلة.</li>
  <li><strong>صنع في الفلبين بمكونات طبيعية 100%:</strong> الصابون الفلبيني الأصلي الخالي من المواد الكيميائية الضارة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الرغوة):</strong> افركي صابونة كوجي سان بين يدين مبللتين بالماء الفاتر لتوليد رغوة ناصعة.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي الرغوة على بشرة الوجه أو الجسم ودلكي برفق دون فرك قسي.</li>
  <li><strong>الخطوة الثالثة (الانتظار والشطف):</strong> اتصفي الرغوة لـ 30 ثانية إلى 1 دقيقة ثم اشطفي بالماء الفاتر واستعملي كريم مرطب (مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>حمض الكوجيك الطبيعي (Pure Kojic Acid):</strong> يثبط إنزيم التايروسينيز ويفتح التصبغات والكلف.</li>
  <li><strong>زيت جوز الهند النقي (Coconut Oil):</strong> يغذي البشرة ويحفظ ترطيبها أثناء التقشير.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والجسم فقط.</li>
  <li>تجنبي ملامسة الرغوة المباشرة للعينين ويُنصح بتطبيق كريم واقي شمس عند الخروج.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بوعاء صابون جاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من التصبغات، الكلف، واسمرار البشرة وتفتش عن صابون كوجي سان الفلبيني الأصلي 3 قطع.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كوجي سان (Kojie San)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / صابون تفتيح البشرة وتقشير التصبغات الأصلي</td></tr>
  <tr><th>نوع المنتج</th><td>صابون طبيعي لتفتيح البشرة بحمض الكوجيك (عبوة 3 قطع × 100g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>3 × 100 جم (إجمالي 300 جم)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (العادية، الدهنية، والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناصعة، موحدة اللون، خالية من التصبغات والكلف ومشعّة بالنضارة</td></tr>
  <tr><th>الملمس</th><td>قالب صابوني ناعم برتقالي يولد رغوة لطيفة بسلاسة</td></tr>
  <tr><th>العطر</th><td>عطر برتقال طبيعي فواح ومنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>حمض الكوجيك النقي، زيت جوز الهند، خلاصة الأرز</td></tr>
  <tr><th>بلد المنشأ</th><td>الفلبين (Philippines)</td></tr>
  <tr><th>الشركة المصنعة</th><td>BEVI (Beauty Elements Ventures Inc.)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد حمض الكوجيك الأصلي من كوجي سان (Kojie San Soap)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج صابونة كوجي سان مشكلة التصبغات الجلديّة، الكلف، آثـار حب الشباب، واسمرار الأكواع والركب والوجه.</p>

<h3>لماذا تنجح تركيبة حمض الكوجيك الطبيعي؟</h3>
<p>لأن حمض الكوجيك يمنع تشكل صبغة الميلامين عن طريق منافسة طاقة إنزيم التايروسينيز، فتتفتح البشرة طبيعياً.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>المرطب بعد الاستعمال:</strong> وضعي كريم مرطب فورياً بعد الشطف لمنع جفاف البشرة.<br>
2. <strong>واقي الشمس الزامي:</strong> استعملي واقي شمس SPF 50 لمنع عودة التصبغات أثناء العلاج.<br>
3. <strong>التدرج في الاستخدام:</strong> ابدئي بـ 30 ثانية على الوجه ثم زيدي المدة تدريجياً.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "صابون كوجي سان البرتقالي يسبب حرقان دائم للبشرة."<br>
<strong>الحقيقة:</strong> الحكة الخفيفة أولية نتيجة تقشير حمض الكوجيك، وتزول فور استخدام مرطب طبي آمن.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يستخلب حمض الكوجيك أيونات النحاس بإنزيم التايروسينيز، مما يوقف تحول التايروسين إلى ميلامين غامق.</p>"""

    faqs = [
        ("ما هو صابون كوجي سان لتفتيح البشرة ثلاث عبوات 100 جم؟", "هو الصابون الفلبيني الأصلي بحمض الكوجيك وزيت جوز الهند لتفتيح التصبغات وتوحيد لون الوجه والجسم عبوة 3 قطع 100 جم."),
        ("ما هي فوائد حمض الكوجيك وزيت جوز الهند؟", "يثبط حمض الكوجيك إنزيم الميلامين ويفتح التصبغات والكلف، بينما يغذي زيت جوز الهند البشرة."),
        ("هل يفتح اسمرار الوجه والجسم والمناطق الحساسة؟", "نعم، مثبت سريرياً في تفتيح اسمرار الوجه، الجسم، الأكواع، والركب والمناطق الحساسة."),
        ("ما حجم العبوة الثلاثية؟", "تحتوي العبوة على 3 قطع صابون بوزن 100 جم لكل قطعة (إجمالي 300 جم)."),
        ("كيف يُستخدم بالشكل الصحيح؟", "افركي الصابونة لتوليد رغوة، وضعي الرغوة على البشرة 30-60 ثانية واشطفي بالماء ثم ضعي مرطباً."),
        ("هل هو الصابون الفلبيني الأصلي 100%؟", "نعم، صابون كوجي سان الأصلي المستورد من الفلبين بختم الجودة."),
        ("ما هو بلد صنع صابون كوجي سان؟", "صُنع بفخر في الفلبين بواسطة شركة BEVI العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات كوجي سان لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يتطلب استخدام كريم مرطب بعده؟", "نعم، يُوصى دائماً باستخدام كريم مرطب طبي بعد الشطف لحماية البشرة."),
        ("ما هي رائحة صابون كوجي سان؟", "يتميز برائحة البرتقال الفواحة المنعشة واللذيذة."),
        ("هل يزيل آثار حب الشباب والكلف؟", "نعم، يزيل بقع الكلف، النمش، وآثار حب الشباب القديمة ب فاعلية."),
        ("هل العبوة الثلاثية 3 × 100 جم اقتصادية؟", "نعم، عبوة توفير ممتازة تكفي للاستخدام المستمر لأشهر طويلة."),
        ("كيف أحتفظ بالصابونة؟", "تُحفظ في وعاء صابون جاف بعيداً عن الماء لمنع الذوبان."),
        ("هل يترك البشرة ناصعة ومشرقة؟", "نعم، يمنح البشرة نضارة وصفاءً ملحوظاً من أول أسابيع."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة كرتونية أنيقة مغلفة بالبلاستيك الحامي."),
        ("هل يلزم استخدام واقي شمس معه؟", "نعم، يفضل استخدام واقي الشمس لحماية البشرة المفتحة حديثاً."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُفضل استخدامه 1 إلى 2 مرة يومياً."),
        ("هل يناسب جميع الأعمار؟", "مناسب للفتيات والبالغين من سن 12 سنة فما فوق."),
        ("هل يناسب البشرة الدهنية والمعرضة للحبوب؟", "ممتاز جداً للبشرة الدهنية حيث يزيل الدهون وتقشير الآثار."),
        ("هل هو صابون التفتيح الأقوى عالمياً؟", "نعم، صابون كوجي سان الأصلي الأكثر شهرة وطلباً عالمياً."),
        ("هل يمنح حس نضارة وصفاء طوال اليوم؟", "نعم، يضمن إشراقة وصفاءً رائعاً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة كوجي سان صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يزيل الخلايا الميتة برفق؟", "نعم، يقشر الطبقة السطحية الميتة ب سلاسة."),
        ("هل يترك ملمساً نظيفاً؟", "نعم، ينظف المسام ويترك الوجه ناصعاً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Kojie San Skin Lightening Soap - Pack of 3 (100g each)</strong> is the world's #1 iconic Philippine natural skin lightening soap engineered to fade hyperpigmentation, unify face and body skin tone, and eliminate dark spots and post-acne blemishes. Formulated with 100% pure natural Kojic Acid blended with pure coconut oil.</p>
<p>Kojie San Soap inhibits tyrosinase melanin synthesis, gently exfoliates dead skin cells, and brightens dark elbows, knees, and sensitive areas, delivering a visibly glowing, clear, and even-toned skin matrix from early applications.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intense Natural Whitening with Pure Kojic Acid:</strong> Fades dark spots, melasma, and hyperpigmentation effectively.</li>
  <li><strong>Unifies Face, Body & Intimate Skin Tone:</strong> Treats dark elbows, knees, and sun-damaged skin patches.</li>
  <li><strong>Enriched with Pure Coconut Oil:</strong> Nourishes skin fibers and prevents severe dryness during exfoliation.</li>
  <li><strong>Gentle Exfoliation for Dead Skin & Acne Scars:</strong> Clears dead cell layers to reveal radiant new skin.</li>
  <li><strong>High-Value Triple Pack (3 x 100g):</strong> Economic pack ensuring months of continuous whitening routines.</li>
  <li><strong>Made in the Philippines 100% Natural Formula:</strong> Iconic authentic Philippine soap free from harmful chemicals.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Lather):</strong> Rub Kojie San soap between wet hands with warm water to create a vibrant foam.</li>
  <li><strong>Step 2 (Apply):</strong> Apply lather onto facial or body skin and massage gently without harsh scrubbing.</li>
  <li><strong>Step 3 (Rinse):</strong> Leave lather on skin for 30 seconds to 1 minute, rinse thoroughly with warm water, and apply moisturizer (twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Natural Kojic Acid:</strong> Inhibits tyrosinase enzymes to fade dark spots and hyperpigmentation.</li>
  <li><strong>Pure Coconut Oil:</strong> Deeply hydrates and nourishes skin during natural acid exfoliation.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and body skin application only.</li>
  <li>Avoid direct contact with eyes; apply sunscreen SPF 50 when exposed to daylight.</li>
  <li>Keep out of reach of children and store in a dry soap dish in a cool place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with skin hyperpigmentation, melasma, or dark spots seeking the authentic Philippine Kojie San Kojic Acid Soap 3-pack.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Kojie San</td></tr>
  <tr><th>Category</th><td>Skincare / Pure Kojic Acid Skin Lightening Soap Bars</td></tr>
  <tr><th>Product Type</th><td>Natural Kojic Acid Whitening Soap Bar (Pack of 3 x 100g)</td></tr>
  <tr><th>Volume/Weight</th><td>3 x 100 g (Total 300g)</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Normal, Oily & Combination)</td></tr>
  <tr><th>Finish</th><td>Radiant, even-toned, hyperpigmentation-free & clear skin</td></tr>
  <tr><th>Texture</th><td>Smooth orange soap bar generating rich lather</td></tr>
  <tr><th>Fragrance</th><td>Fresh vibrant natural Orange scent</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Kojic Acid, Virgin Coconut Oil, Rice Extract</td></tr>
  <tr><th>Country of Origin</th><td>Philippines</td></tr>
  <tr><th>Manufacturer</th><td>BEVI (Beauty Elements Ventures Inc.)</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Kojic Acid Tyrosinase Chelation & Melanin Inhibition</h2>

<h3>What problem does this solve?</h3>
<p>Kojie San Soap resolves dark skin hyperpigmentation, melasma, acne scars, and uneven elbow and knee tone.</p>

<h3>Why choose Kojie San Kojic Soap?</h3>
<p>Pure Kojic Acid chelates copper ions within tyrosinase enzymes, blocking DOPA-chrome conversion to safely lighten skin.</p>"""

    en_faqs = [
        ("What is Kojie San Skin Lightening Soap - Pack of 3 (100g each)?", "It is the authentic Philippine Kojic Acid soap formulated to fade dark spots, melasma, and unify skin tone in a 3-pack of 100g bars."),
        ("What are the benefits of Kojic Acid and Coconut Oil?", "Kojic Acid inhibits melanin production and brightens skin, while Coconut Oil hydrates and nourishes during exfoliation."),
        ("Does it brighten face, body, and sensitive areas?", "Yes, clinically proven to lighten dark spots on face, body, elbows, knees, and sensitive zones."),
        ("What weight is contained in this 3-pack?", "Contains 3 soap bars weighing 100g each (total 300g)."),
        ("How do I use it correctly?", "Lather, apply foam onto skin for 30-60 seconds, rinse with warm water, and follow with a moisturizing cream."),
        ("Is it 100% authentic Philippine Kojie San?", "Yes, 100% genuine Kojie San imported directly from the Philippines."),
        ("Where is Kojie San manufactured?", "It is proudly manufactured in the Philippines by BEVI."),
        ("How do I verify authenticity at Ekleel Abha?", "All Kojie San products at Ekleel Abha are 100% original from certified distributors."),
        ("Is a moisturizer required after use?", "Yes, always apply a moisturizing body or face cream post-rinse to prevent skin dryness."),
        ("What scent does Kojie San soap have?", "Features a fresh, vibrant, natural orange fragrance."),
        ("Does it erase melasma and post-acne marks?", "Yes, highly effective at fading melasma, freckles, and old post-acne blemishes."),
        ("Is the 3-pack economical?", "Yes, high-value triple pack lasts through months of daily whitening care."),
        ("How should I store the soap bars?", "Store in a dry soap dish away from standing water to prevent melting."),
        ("Does it leave skin touchably clear and radiant?", "Yes, bestows a bright, clear, and radiant glow within weeks."),
        ("Is the packaging securely sealed?", "Yes, comes in a protective cardboard box wrapped in plastic film."),
        ("Should sunscreen be used during treatment?", "Yes, applying SPF 50 sunscreen daily protects newly brightened skin."),
        ("How many times daily should I use it?", "Recommended for use 1 to 2 times daily."),
        ("Is it safe for oily and acne-prone skin?", "Excellent for oily skin as Kojic Acid purifies pores and sweeps away excess sebum."),
        ("Is Kojie San the #1 whitening soap worldwide?", "Yes, Kojie San is the globally celebrated #1 Kojic Acid whitening soap."),
        ("Does it provide long-lasting radiance?", "Yes, guarantees visible skin clarity and radiance."),
        ("Is the packaging recyclable?", "Yes, 100% recyclable environmentally friendly packaging."),
        ("Does it exfoliate dead skin cells gently?", "Yes, gently sloughs off dead superficial epidermal layers."),
        ("Does it leave skin feeling clean?", "Yes, purifies pores leaving skin fresh and clean."),
        ("Is it suitable for all age groups?", "Suitable for teens and adults aged 12+."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1851",
        "sku": "EK-1851",
        "gtin": "4809014128337",
        "category": "العناية بالبشرة / صابون تفتيح البشرة وتقشير التصبغات الأصلي",
        "brand": "Kojie San",
        "ar": {
            "title": "صابون كوجي سان لتفتيح البشرة ثلاث عبوات 100 جم",
            "meta_title": "صابون كوجي سان الأصلي 3 قطع | صيدلية إكليل أبها",
            "meta_description": "اشتري صابون كوجي سان لتفتيح البشرة ثلاث عبوات (100 جم لكل قطعة). صابون بحمض الكوجيك الأصلي لتفتيح الوجه والجسم والتصبغات. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["كوجي_سان", "صابون_كوجي_سان", "تفتيح_التصبغات", "حمض_الكوجيك", "إكليل_أبها"]
        },
        "en": {
            "title": "Kojie San Skin Lightening Soap - Pack of 3 (100g each)",
            "meta_title": "Kojie San Soap Pack of 3 | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Kojie San Skin Lightening Soap (Pack of 3 x 100g). Authentic Philippine Kojic Acid whitening soap bar. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["kojie_san", "kojic_acid_soap", "skin_lightening", "philippine_soap", "ekleel_abha"]
        },
        "schema": {
            "brand": "Kojie San",
            "category": "Skincare / Whitening Soap",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "kojie-san-skin-lightening-soap-pack-of-3-100g-each.webp",
            "alt": "Kojie San Skin Lightening Soap Pack of 3 100g each",
            "title": "Kojie San Skin Lightening Soap Pack of 3 100g each"
        }
    }

def create_product_1852():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>صابون تبييض كلاسيكي من سكينوايت، 135جم (SkinWhite Classic Whitening Soap, 135g)</strong> الصابون الفلبيني المفضل والأكثر نجاحاً لتفتيح وتنعيم بشرة الوجه والجسم في 14 يوماً فقط. يرتكز هذا الصابون الأصلي من سكينوايت (SkinWhite Classic Synchronized Whitening Soap) على تقنية التبييض المتزامنة (RonaCare® Synchronized Whitening) المعززة بـ فيتامين B3 (Niacinamide)، فيتامين C و E، والمرطبات الحليبية.</p>
<p>تعمل صابونة سكينوايت الكلاسيكية على تفتيح التصبغات، إزالة البقع الداكنة، وحماية البشرة من الاسمرار ومخاطر الأشعة فوق البنفسجية، لتمنحكِ بشرة موحدة، ناعمة كالحرير، ومفعمة بالصفاء والانتعاش العطري طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح ملحوظ وموحد في 14 يوماً:</strong> تقنية متزامنة تفتح تصبغات الوجه والجسم بسرعة وتألق.</li>
  <li><strong>مدعم بـ فيتامينات B3 و C و E:</strong> يغذي ألياف البشرة ويعيد نضارتها وحيويتها.</li>
  <li><strong>حماية متكاملة من اسمرار الشمس:</strong> يمنع تكاثر صبغة الميلامين الناتجة عن الأشعة فوق البنفسجية.</li>
  <li><strong>مرطبات حليبية تمنع الجفاف:</strong> تترك الوجه والجسم بطراوة ونعومة ناصعة.</li>
  <li><strong>رغوة غنية وعطر كلاسيكي منعش:</strong> يطهر الجلد من الدهون والشوائب ويريح الحواس.</li>
  <li><strong>قطعة صابون وافرة بوزن 135 جم:</strong> حجم ممتاز يدوم لعدة أسابيع من العناية اليومية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الرغوة):</strong> افركي صابونة سكينوايت بين يدين مبللتين بالماء الفاتر لتوليد رغوة غنية.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي الرغوة على بشرة الوجه والجسم ودلكي برفق دون فرك قسي.</li>
  <li><strong>الخطوة الثالثة (الشطف):</strong> اشطفي بالماء الفاتر جيداً واستعملي كريم مرطب (تُستعمل مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>فيتامين B3 وفيتامين C (Niacinamide & Vit C):</strong> يثبطان نقل الميلامين ويفتحان التصبغات.</li>
  <li><strong>فيتامين E ومرطبات حليبية:</strong> تحمي خلايا الجلد وتمنع الجفاف أثناء التفتيح.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والجسم فقط.</li>
  <li>تجنبي ملامسة الرغوة المباشرة للعينين ويُنصح بتطبيق واقي شمس عند الخروج.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بوعاء صابون جاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تفتش عن صابونة سكينوايت الكلاسيكية الفلبينية لتفتيح الوجه والجسم وتوحيد اللون في 14 يوماً.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سكينوايت (SkinWhite)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / صابون تفتيح البشرة الفلبيني الكلاسيكي</td></tr>
  <tr><th>نوع المنتج</th><td>صابون كلاسيكي متزامن لتفتيح البشرة في 14 يوماً (135g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>135 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (العادية، الجافة، والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناصعة، موحدة اللون، مرطبة ومشعة بالنضارة في 14 يوماً</td></tr>
  <tr><th>الملمس</th><td>قالب صابوني ناعم يولد رغوة حليبية لطيفة</td></tr>
  <tr><th>العطر</th><td>عطر سكينوايت الكلاسيكي المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>فيتامين B3، فيتامين C، فيتامين E، مرطبات حليبية</td></tr>
  <tr><th>بلد المنشأ</th><td>الفلبين (Philippines)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Splash Corporation / Wipro SkinWhite</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد التبييض المتزامن من سكينوايت (SkinWhite Classic)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج صابونة سكينوايت الكلاسيكية مشكلة اسمرار الوجه والجسم، التصبغات البقعية، الجفاف، وشحوب البشرة.</p>

<h3>لماذا تنجح تقنية التبييض المتزامن؟</h3>
<p>لأن فيتامين B3 يمنع انتقال صبغة الميلامين للطبقة السطحية، بينما ينقي فيتامين C الشوائب ويعيد النضارة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>المضمضة والرغوة اليومية:</strong> استعمليها مرتين يومياً على الوجه والجسم.<br>
2. <strong>المرطب بعد الاستعمال:</strong> استعملي لوشن سكينوايت بعد الشطف لنتائج تفتيح مضاعفة.<br>
3. <strong>واقي الشمس الزامي:</strong> طبقي واقي الشمس لمنع عودة الاسمرار أثناء العلاج.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "صابون سكينوايت يجفف الجلد ويسبب قشوراً."<br>
<strong>الحقيقة:</strong> صابونة سكينوايت مدعمة بالمرطبات الحليبية وفيتامين E لمنع الجفاف وتنعيم الجلد.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعطل النياسيناميد (B3) انتقال الميلانوسومات من خلايا الميلاين إلى الميلانوسايت، فيفتح لون الجلد برفق.</p>"""

    faqs = [
        ("ما هو صابون تبييض كلاسيكي من سكينوايت 135جم؟", "هو صابون تفتيح فلبيني كلاسيكي بفيتامين B3 و C و E لتفتيح وتوحيد لون الوجه والجسم في 14 يوماً 135 جم."),
        ("ما هي فوائد تقنية التبييض المتزامن وفيتامين B3؟", "تمنع انتقال التصبغات للطبقة السطحية وتفتح البقع الداكنة وتوحد لون البشرة بسرعة."),
        ("هل يفتح الوجه والجسم في 14 يوماً؟", "نعم، مثبت سريرياً في منح تفتيح ملحوظ ولون موحد خلال 14 يوماً من الاستخدام المنتظم."),
        ("ما حجم ووزن قالب الصابونة؟", "تأتي بوزن وافر 135 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "افركي الصابونة بين يدين مبللتين لتوليد رغوة، وضعي الرغوة على الوجه والجسم واشطفي بالماء الفاتر مرتين يومياً."),
        ("هل يحتوي على مرطبات حليبية لمنع الجفاف؟", "نعم، مدعم بمرطبات حليبية وفيتامين E لتنعيم الجلد ومنع الجفاف."),
        ("ما هو بلد صنع صابون سكينوايت؟", "صُنع بفخر في الفلبين بواسطة شركة سبلاش (Splash Corporation)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات سكينوايت لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يزيل اسمرار الشمس والبقع الداكنة؟", "نعم، يزيل اسمرار الشمس، البقع الداكنة، والتصبغات ب فاعلية."),
        ("ما هي رائحة صابون سكينوايت الكلاسيكي؟", "يتميز برائحة سكينوايت الكلاسيكية الفواحة والمنعشة."),
        ("هل يناسب جميع أنواع البشرة؟", "مناسب للبشرة العادية، الجافة، والمختلطة."),
        ("هل العبوة 135 جم اقتصادية وتدوم طويلاً؟", "نعم، قالب وافر يكفي للاستخدام اليومي لعدة أسابيع."),
        ("كيف أحتفظ بالصابونة؟", "تُحفظ في وعاء صابون جاف بعيداً عن تجمع الماء."),
        ("هل يترك أثراً لزجاً؟", "لا، ينظف الجلد تماماً ويتركه طرياً ونظيفاً دون أي لزوجة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة كرتونية أنيقة مغلفة بالبلاستيك الحامي."),
        ("هل يلزم استخدام واقي شمس معه؟", "نعم، يُوصى باستخدام واقي الشمس لحماية تفتيح البشرة."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل 2 مرات يومياً (صباحاً ومساءً)."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع الفئات العمرية للنساء والرجال من سن 12 سنة."),
        ("هل يحتوي على مواد كيميائية قاسية؟", "خالي من المواد الكيميائية الضارة ومجرب لسلامة البشرة."),
        ("هل هو صابون التفتيح الكلاسيكي الأشهر لسكينوايت؟", "نعم، SkinWhite Classic الصابون الأول والأكثر مبيعاً لسكينوايت."),
        ("هل يمنح حس نضارة وثقة؟", "نعم، يضمن إشراقة وثقة مطلقة بشرتكِ."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يزيل الشوائب والدهون الزائدة؟", "نعم، ينظف الشوائب والدهون ويكشف عن بشرة ناصعة."),
        ("هل يترك الجلد طرياً كالحرير؟", "نعم، يترك البشرة طرية ومخملية كالحرير."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>SkinWhite Classic Whitening Soap, 135g</strong> is the iconic Philippine classic whitening soap bar engineered to brighten and smooth facial and body skin in just 14 days. Formulated by SkinWhite (Classic Synchronized Whitening), it features RonaCare® Synchronized Whitening technology enriched with Vitamin B3 (Niacinamide), Vitamins C & E, and milk moisturizers.</p>
<p>SkinWhite Classic Soap fades hyperpigmentation, removes dark spots, and shields skin from UV darkening, leaving your face and body touchably soft, evenly toned, and freshly fragranced all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Visible Whitening in 14 Days:</strong> Synchronized technology brightens face and body skin tone rapidly.</li>
  <li><strong>Enriched with Vitamins B3, C & E:</strong> Nourishes skin fibers and restores healthy radiant vitality.</li>
  <li><strong>Shields Against Sun Darkening:</strong> Prevents melanin overproduction triggered by UV sunlight exposure.</li>
  <li><strong>Milk Moisturisers Prevent Dryness:</strong> Softens face and body skin, leaving it silky and hydrated.</li>
  <li><strong>Rich Foaming Classic Fragrance:</strong> Purifies pores from impurities while refreshing your senses.</li>
  <li><strong>Generous 135g Soap Bar:</strong> High-value bar providing weeks of continuous daily whitening care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Lather):</strong> Rub SkinWhite soap bar between wet hands with warm water to create a creamy lather.</li>
  <li><strong>Step 2 (Apply):</strong> Apply lather over facial and body skin and massage gently without harsh scrubbing.</li>
  <li><strong>Step 3 (Rinse):</strong> Rinse thoroughly with warm water and apply a moisturizing body lotion (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Vitamin B3 & Vitamin C:</strong> Inhibit melanosome transfer and clarify dark spots.</li>
  <li><strong>Vitamin E & Milk Moisturisers:</strong> Protect dermal cells and prevent skin dryness during whitening.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and body skin application only.</li>
  <li>Avoid direct contact with eyes; apply sunscreen SPF 50 when exposed to daylight.</li>
  <li>Keep out of reach of children and store in a dry soap dish in a cool place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking the iconic Philippine SkinWhite Classic Whitening Soap for visible 14-day face and body brightening.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>SkinWhite</td></tr>
  <tr><th>Category</th><td>Skincare / Philippine Classic Synchronized Whitening Soap Bars</td></tr>
  <tr><th>Product Type</th><td>14-Day Synchronized Whitening Soap Bar (135g)</td></tr>
  <tr><th>Volume/Weight</th><td>135 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Normal, Dry & Combination)</td></tr>
  <tr><th>Finish</th><td>Radiant, even-toned, 14-day brightened & soft skin</td></tr>
  <tr><th>Texture</th><td>Smooth soap bar generating creamy foam</td></tr>
  <tr><th>Fragrance</th><td>Iconic fresh SkinWhite Classic aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Vitamin B3, Vitamin C, Vitamin E, Milk Moisturisers</td></tr>
  <tr><th>Country of Origin</th><td>Philippines</td></tr>
  <tr><th>Manufacturer</th><td>Splash Corporation / Wipro SkinWhite</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Synchronized Whitening & Niacinamide Melanosome Block</h2>

<h3>What problem does this solve?</h3>
<p>SkinWhite Classic Whitening Soap resolves facial dullness, dark spots, sun tanning, and uneven skin tone.</p>

<h3>Why choose SkinWhite Classic Soap?</h3>
<p>Niacinamide (Vitamin B3) blocks melanosome transfer to keratinocytes, while Milk Moisturisers keep skin touchably soft.</p>"""

    en_faqs = [
        ("What is SkinWhite Classic Whitening Soap, 135g?", "It is the iconic Philippine classic whitening soap bar enriched with Vitamins B3, C, E, and Milk Moisturisers for 14-day skin brightening."),
        ("What are the benefits of Synchronized Whitening technology and Vitamin B3?", "Inhibits melanosome transfer, fades dark spots, and unifies face and body skin tone in 14 days."),
        ("Does it brighten face and body skin in 14 days?", "Yes, clinically proven to deliver visible skin brightening and even tone within 14 days of regular use."),
        ("What weight is contained in this soap bar?", "It comes as a generous 135g soap bar."),
        ("How do I use it correctly?", "Lather between wet hands, apply foam onto face and body, massage gently, and rinse with warm water twice daily."),
        ("Does it contain Milk Moisturisers to prevent dryness?", "Yes, enriched with Milk Moisturisers and Vitamin E to keep skin touchably soft and hydrated."),
        ("Where is SkinWhite Soap manufactured?", "It is proudly manufactured in the Philippines by Splash Corporation."),
        ("How do I verify authenticity at Ekleel Abha?", "All SkinWhite products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it remove sun tan and dark spots?", "Yes, highly effective at clearing sun tan, dark spots, and hyperpigmentation."),
        ("What scent does SkinWhite Classic soap have?", "Features the iconic, fresh SkinWhite Classic scent."),
        ("Is it suitable for all skin types?", "Ideal for normal, dry, and combination skin types."),
        ("Is the 135g soap bar economical?", "Yes, high-value 135g bar lasts through weeks of daily whitening care."),
        ("How should I store the soap bar?", "Store in a dry soap dish away from standing water to prevent melting."),
        ("Does it leave skin touchably soft and clear?", "Yes, bestows a bright, clear, and touchably soft skin feel."),
        ("Is the packaging securely sealed?", "Yes, comes in a protective cardboard box wrapped in plastic film."),
        ("Should sunscreen be used during treatment?", "Yes, applying SPF 50 sunscreen daily protects newly brightened skin."),
        ("How many times daily should I use it?", "Recommended for use twice daily, morning and evening."),
        ("Is it suitable for men and women?", "Suitable for all age groups, both men and women aged 12+."),
        ("Is it free of harsh chemicals?", "Dermatologically tested and safe for daily facial and body skin cleansing."),
        ("Is it SkinWhite's best-selling classic soap?", "Yes, SkinWhite Classic is the #1 iconic best-selling soap bar by SkinWhite."),
        ("Does it deliver complete radiance confidence?", "Yes, guarantees visible skin clarity and radiance confidence."),
        ("Is the packaging recyclable?", "Yes, 100% recyclable environmentally friendly packaging."),
        ("Does it sweep away excess oil and impurities?", "Yes, cleanses pores leaving skin fresh and clean."),
        ("Does it leave skin touchably silky?", "Yes, leaves face and body skin soft, supple, and smooth."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1852",
        "sku": "EK-1852",
        "gtin": "4800119120943",
        "category": "العناية بالبشرة / صابون تفتيح البشرة الفلبيني الكلاسيكي",
        "brand": "SkinWhite",
        "ar": {
            "title": "صابون تبييض كلاسيكي من سكينوايت، 135جم",
            "meta_title": "صابون سكينوايت الكلاسيكي 135جم | إكليل أبها",
            "meta_description": "اشتري صابون تبييض كلاسيكي من سكينوايت (135جم). صابون تفتيح فلبيني بفيتامين B3 و C لنتائج في 14 يوماً. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["سكينوايت", "صابون_سكينوايت", "تفتيح_في_14_يوما", "تفتيح_الفلبين", "إكليل_أبها"]
        },
        "en": {
            "title": "SkinWhite Classic Whitening Soap, 135g",
            "meta_title": "SkinWhite Classic Whitening Soap 135g | Ekleel Abha",
            "meta_description": "Buy original SkinWhite Classic Whitening Soap (135g). 14-day synchronized whitening Philippine soap bar. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["skinwhite", "skinwhite_soap", "classic_whitening", "philippine_soap", "ekleel_abha"]
        },
        "schema": {
            "brand": "SkinWhite",
            "category": "Skincare / Whitening Soap",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "skinwhite-classic-whitening-soap-135g.webp",
            "alt": "SkinWhite Classic Whitening Soap 135g",
            "title": "SkinWhite Classic Whitening Soap 135g"
        }
    }

def create_product_1853():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم علاج فوري لخشونة البشرة من يوسيرين 71جم (Eucerin Roughness Relief Spot Treatment Cream - 71g)</strong> المستحضر الطبي العلاجي الفائق الأكثر توصية عالمياً من أطباء الجلدية للقضاء على الخشونة الشديدة، جلد الدجاجة (Keratosis Pilaris)، وتنعيم الأكواع، الركب، والكعبين شديدة الجفاف. يرتكز هذا الكريم الطبي المكثف من يوسيرين (Eucerin Roughness Relief Spot Treatment) على تركيز استثنائي 30% يوريا (Urea 30%) مع خلاصة السيراميد والنعومة الطبيعية (NMFs).</p>
<p>يعمل كريم يوسيرين العلاجي الفوري على تقشير الجلد السميك المتقشر، إذابة التكتلات الكيراتينية المسدودة ببصيلات الشعر، وتأمين ترطيب عميق وموجه للبقع شديدة الخشونة، ليترك بشرتكِ ناعمة كالحرير وخالية تماماً من النتوءات من أول أيام الاستخدام.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>علاج فوري وموجه لخشونة الجلد وجلد الدجاجة (30% Urea):</strong> يقشر التكتلات الكيراتينية وينعم الجلد الخشن.</li>
  <li><strong>تنعيم وترميم الأكواع، الركب، والكعبين:</strong> يذوب القشور والسمك المزعج بالأماكن الجافة.</li>
  <li><strong>مدعم بالسيراميد وعوامل الترطيب الطبيعية (NMFs):</strong> يعيد بناء حاجز البشرة التالف ويحبس الرطوبة.</li>
  <li><strong>خالي 100% من العطور، البارابين، والصبغات:</strong> تركيبة دقيقة ومجربة جلدياً لا تسبب حرقاناً للبشرة الحساسة.</li>
  <li><strong>أنبوب مخصص للتطبيق الموجه:</strong> يسهل وضع الكريم بدقة على البقع والنتوءات الخشنة.</li>
  <li><strong>أنبوب سعة 71 جم:</strong> حجم عالي التركيز والفاعلية لنتائج علاجية سريعة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> نظفي المنطقة شديدة الخشونة (الأكواع، الركب، أو جلد الدجاجة) وجففيها.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي كمية صغيرة من كريم يوسيرين الموجه على البقعة الخشنة فقط.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي برفق حتى امتصاص الكريم بالكامل (يُستعمل 1 إلى 3 مرات يومياً حسب الخشونة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>اليوريا بتركيز مكثف 30% (Urea 30%):</strong> تذوب الكيراتين وتقشر القشور الجافة الفائقة.</li>
  <li><strong>السيراميد وعوامل NMFs:</strong> تعيد حماية حاجز البشرة وتحبس الترطيب لـ 48 ساعة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي الموجه على البقع الخشنة فقط؛ لا يوضع على الوجه أو الجلد المصاب بجروح.</li>
  <li>تجنبي ملامسة الكريم المباشرة للعينين ويُنصح بحماية البشرة من الشمس عند الخروج.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من جلد الدجاجة، الخشونة الشديدة بالأكواع والركب، ويفتش عن كريم يوسيرين 30% يوريا العلاجي.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>يوسيرين (Eucerin)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات يوسيرين الطبية لعلاج الخشونة وجلد الدجاجة 30% يوريا</td></tr>
  <tr><th>نوع المنتج</th><td>كريم علاج موجه فوري لخشونة وجلد الدجاجة بتركيز 30% يوريا (71g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>71 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة شديدة الخشونة، المتقشرة، وجلد الدجاجة (Keratosis Pilaris)</td></tr>
  <tr><th>المظهر النهائي</th><td>جلد ناعم أملس، مرطب عميقاً، خالي من النتوءات والقشور والسمك المزعج</td></tr>
  <tr><th>الملمس</th><td>كريم علاجي سميك مخصص للبقع الخشنة يمتص بالتدليك</td></tr>
  <tr><th>العطر</th><td>عديم الرائحة (100% Unscented)</td></tr>
  <tr><th>المكونات النشطة</th><td>30% يوريا، سيراميد، عوامل الترطيب الطبيعية (NMFs)</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا / الولايات المتحدة (Beiersdorf)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beiersdorf (يوسيرين)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والأطفال (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الـ 30% يوريا والسيراميد في يوسيرين (Eucerin Roughness Relief)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم يوسيرين الموجه مشكلة جلد الدجاجة (Keratosis Pilaris)، الخشونة الشديدة بالأكواع والركب، والقشور السميكة للكعبين.</p>

<h3>لماذا تنجح تركيبة 30% يوريا الموجهة؟</h3>
<p>لأن تركيز اليوريا العالي (30%) يكسر الروابط الهيدروجينية لبروتين الكيراتين المتكتل، فيحل النتوءات ويطري الجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق الموجه:</strong> وضعي الكريم على النتوءات والبقع الخشنة فقط ولا تنشريه بالكامل.<br>
2. <strong>الاستمرار لـ 7 أيام:</strong> يضمن الاستخدام المنتظم تنعيماً ملموساً واختفاء النتوءات.<br>
3. <strong>المرطب اليومي المكمل:</strong> استخدمي لوشن يوسيرين يوريا اليومي للبقية للحفاظ على النتيجة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "جلد الدجاجة لا يمكن علاجه أو تنعيمه إطلاقاً."<br>
<strong>الحقيقة:</strong> كريم يوسيرين 30% يوريا يذوب التكتلات الكيراتينية وينعم جلد الدجاجة بكفاءة طبية مثبتة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>ترطب جزيئات اليوريا القرنية العميقة، فتنشط الإنزيمات المحللة للبروتينات الميتة وتسقط القشور السميكة.</p>"""

    faqs = [
        ("ما هو كريم علاج فوري لخشونة البشرة من يوسيرين 71جم؟", "هو كريم طبي علاجي موجه بتركيز 30% يوريا وسيراميد للقضاء على جلد الدجاجة والخشونة الشديدة بالأكواع والركب 71 جم."),
        ("ما هي فوائد تركيز 30% يوريا والسيراميد؟", "تذوب اليوريا 30% التكتلات الكيراتينية والقشور السميكة، بينما يعيد السيراميد حماية حاجز البشرة."),
        ("هل يعالج جلد الدجاجة (Keratosis Pilaris) فلياً؟", "نعم، مثبت سريرياً في تنعيم نتوءات جلد الدجاجة وإذابة الكيراتين المتكتل حول الشعرة."),
        ("ما حجم العبوة؟", "تأتي لأنبوب علاجي موجه بوزن 71 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي كمية صغيرة على البقع الخشنة فقط (الأكواع، الركب، أو جلد الدجاجة)، ودلكي برفق 1 إلى 3 مرات يومياً."),
        ("هل هو خالي 100% من العطور والبارابين؟", "نعم، تركيبة علاجية طبية خالية 100% من العطور والصبغات والبارابين."),
        ("ما هو بلد صنع كريم يوسيرين؟", "صُنع بواسطة شركة بايرسدورف (Beiersdorf) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات يوسيرين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يوضع على بشرة الوجه؟", "لا، مخصص للبقع شديدة الخشونة بالجسم كالركب والأكواع وجلد الدجاجة ولا يوضع على الوجه."),
        ("ما هي رائحة كريم يوسيرين العلاجي؟", "عديم الرائحة تماماً (Unscented)."),
        ("هل ينعم الكعبين شديدة الجفاف؟", "نعم، ممتاز جداً لتنعيم الكعبين والقشور السميكة المزعجة."),
        ("هل أنبوب العبوة 71 جم سهل الاستخدام؟", "نعم، أنبوب ذكي بفتحة مخصصة للتطبيق الموجه والدقيق."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل يترك أثراً لزجاً؟", "ينفذ بالتدليك بالمنطقة الخشنة ليترك الجلد أملساً ونظيفاً."),
        ("هل العبوة محكمة الغلق؟", "تأتي في أنبوب محكم الإغلاق لمنع التسرب."),
        ("هل ينصح به أطباء الجلدية عالمياً؟", "نعم، يوسيرين الماركة رقم 1 الموصى بها من أطباء الجلدية لعلاج الخشونة."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل من 1 إلى 3 مرات يومياً حسب شدة الخشونة."),
        ("هل يناسب جميع الأعمار؟", "مناسب للبالغين والأطفال من سن 12 سنة فما فوق."),
        ("هل يسبب حرقاناً للبشرة؟", "تركيبة آمنة، ويُفضل عدم تطبيقه على الجلد المصاب بجروح أو التهابات مفتوحة."),
        ("هل هو الكريم العلاجي الأقوى لخشونة الجلد من يوسيرين؟", "نعم، الكريم الأكثر تركيزاً وفاعلية (30% Urea) للبقع الخشنة."),
        ("هل يمنح نتائج ملموسة خلال أيام؟", "نعم، تظهر نتائج التنعيم واختفاء القشور خلال أسبوع من الاستخدام."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يحمي من عودة الخشونة؟", "نعم، السيراميد وعوامل NMFs يحفظان ترطيب وتنعيم الجلد."),
        ("هل يترك ملمساً أملساً كالحرير؟", "نعم، يترك الجلد خالي من أي نتوءات خشنة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Eucerin Roughness Relief Spot Treatment Cream - 71g</strong> is the world's #1 dermatologist-recommended clinical spot treatment engineered to eliminate severe skin roughness, Keratosis Pilaris (chicken skin), and smooth dry elbows, knees, and cracked heels. Formulated with a concentrated 30% Urea matrix enriched with Ceramides and Natural Moisturizing Factors (NMFs).</p>
<p>Eucerin Spot Treatment Cream exfoliates thick, scaly skin, dissolves keratin plugs clogging hair follicles, and delivers targeted deep moisture to rough patches, leaving skin touchably smooth and bump-free from early applications.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Targeted Spot Treatment for Roughness & Keratosis Pilaris (30% Urea):</strong> Dissolves keratin bumps and smooths rough patches.</li>
  <li><strong>Intense Softening for Elbows, Knees & Heels:</strong> Melts scaly buildup and stubborn dry skin thickness.</li>
  <li><strong>Enriched with Ceramides & NMFs:</strong> Restores damaged skin barrier and seals in 48-hour moisture.</li>
  <li><strong>100% Fragrance, Paraben & Dye Free:</strong> Clinically proven safe formula causing zero irritation.</li>
  <li><strong>Precision Precision Applicator Tube:</strong> Easy targeted application directly onto rough bumps and patches.</li>
  <li><strong>Concentrated 71g Tube:</strong> High-efficacy medical size for rapid clinical skin smoothing.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse extremely rough skin patches (elbows, knees, or Keratosis Pilaris areas) and pat dry.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a small amount of Eucerin Spot Treatment cream directly onto rough patches.</li>
  <li><strong>Step 3 (Massage):</strong> Massage gently until fully absorbed (use 1 to 3 times daily based on roughness severity).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Concentrated 30% Urea:</strong> Dissolves keratin buildup and exfoliates severe scaly skin layers.</li>
  <li><strong>Ceramides & Natural Moisturizing Factors (NMFs):</strong> Restore skin barrier defense and lock in deep moisture.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical targeted body spot application only; do not apply to facial skin or wounded areas.</li>
  <li>Avoid direct contact with eyes; wear protective clothing or sunscreen when exposed to sunlight.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with Keratosis Pilaris (chicken skin), extreme elbow or knee roughness, seeking Eucerin's 30% Urea clinical spot treatment.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Eucerin</td></tr>
  <tr><th>Category</th><td>Skincare / Clinical 30% Urea Roughness Relief Spot Treatments</td></tr>
  <tr><th>Product Type</th><td>Targeted 30% Urea Keratosis Pilaris & Roughness Cream (71g)</td></tr>
  <tr><th>Volume/Weight</th><td>71 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Severely Rough, Scaly Skin & Keratosis Pilaris</td></tr>
  <tr><th>Finish</th><td>Touchably smooth, bump-free, hydrated & soft skin</td></tr>
  <tr><th>Texture</th><td>Rich concentrated spot treatment cream</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-Free (Unscented)</td></tr>
  <tr><th>Active Ingredients</th><td>30% Urea, Ceramides, Natural Moisturizing Factors (NMFs)</td></tr>
  <tr><th>Country of Origin</th><td>Germany / USA (Beiersdorf)</td></tr>
  <tr><th>Manufacturer</th><td>Beiersdorf (Eucerin)</td></tr>
  <tr><th>Age Group</th><td>Adults & Kids (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 30% Urea Keratolysis & Ceramide Barrier Repair</h2>

<h3>What problem does this solve?</h3>
<p>Eucerin Roughness Relief Spot Treatment resolves Keratosis Pilaris (chicken skin), severe elbow/knee roughness, and thick heel scales.</p>

<h3>Why choose Eucerin 30% Urea Spot Treatment?</h3>
<p>30% Urea breaks hydrogen bonds within hyperkeratotic protein plugs, melting keratin bumps while Ceramides rebuild epidermal barrier defense.</p>"""

    en_faqs = [
        ("What is Eucerin Roughness Relief Spot Treatment Cream - 71g?", "It is a targeted clinical cream formulated with 30% Urea and Ceramides to eliminate Keratosis Pilaris and severe skin roughness."),
        ("What are the benefits of 30% Urea and Ceramides?", "30% Urea dissolves keratin plugs and scaly buildup, while Ceramides restore and protect the damaged skin barrier."),
        ("Does it treat Keratosis Pilaris (chicken skin) effectively?", "Yes, clinically proven to smooth Keratosis Pilaris bumps and dissolve keratin plugs around hair follicles."),
        ("What volume is contained in this tube?", "It comes in a concentrated 71g targeted tube."),
        ("How do I apply it correctly?", "Apply a small amount directly onto rough patches (elbows, knees, or chicken skin bumps) 1 to 3 times daily."),
        ("Is it 100% fragrance-free, dye-free, and paraben-free?", "Yes, dermatologist-tested clinical formula free of fragrance, dyes, and parabens."),
        ("Where is Eucerin Spot Treatment manufactured?", "Produced by Beiersdorf following global dermatological standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Eucerin products at Ekleel Abha are 100% original from certified distributors."),
        ("Can it be applied onto facial skin?", "No, intended for targeted body rough patches only (elbows, knees, heels) and not for facial application."),
        ("What scent does Eucerin Spot Treatment have?", "It is completely fragrance-free (unscented)."),
        ("Does it soften extremely rough dry heels?", "Yes, highly effective at melting thick scaly skin on dry rough heels."),
        ("Is the 71g tube convenient for targeted application?", "Yes, precision tube nozzle allows easy targeted application onto rough patches."),
        ("How should I store the tube?", "Store in a cool, dry place away from direct heat."),
        ("Does it leave a greasy sticky residue?", "Absorbs into rough patches during massage leaving skin smooth and soft."),
        ("Is the tube cap leak-proof?", "Yes, comes with a secure screw-top cap."),
        ("Is Eucerin recommended by dermatologists worldwide?", "Yes, Eucerin is the #1 dermatologist-recommended brand for skin roughness."),
        ("How many times daily should I use it?", "Use 1 to 3 times daily depending on roughness severity."),
        ("Is it safe for adults and teens?", "Suitable for adults and teens aged 12+."),
        ("Does it cause skin stinging?", "Safe formula; do not apply onto open wounds or irritated skin."),
        ("Is it Eucerin's most concentrated roughness cream?", "Yes, the flagship 30% Urea concentrated spot treatment by Eucerin."),
        ("Does it deliver visible smoothing results in days?", "Yes, skin smoothing and bump reduction are visible within one week."),
        ("Is the tube recyclable?", "Yes, 100% recyclable environmentally friendly tube."),
        ("Does it prevent roughness from returning?", "Yes, Ceramides and NMFs lock in deep moisture to prevent roughness return."),
        ("Does it leave skin touchably smooth?", "Yes, leaves skin touchably smooth and bump-free."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1853",
        "sku": "EK-1853",
        "gtin": "072140024406",
        "category": "العناية بالبشرة / كريمات يوسيرين الطبية لعلاج الخشونة وجلد الدجاجة 30% يوريا",
        "brand": "Eucerin",
        "ar": {
            "title": "كريم علاج فوري لخشونة البشرة من يوسيرين 71جم",
            "meta_title": "كريم يوسيرين 30% يوريا للخشونة 71جم | إكليل أبها",
            "meta_description": "اشتري كريم علاج فوري لخشونة البشرة من يوسيرين (71جم). كريم علاجي 30% يوريا وسيراميد لجلد الدجاجة والأكواع والركب. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["يوسيرين", "يوسيرين_يوريا", "علاج_جلد_الدجاجة", "تنعيم_الأكواع", "إكليل_أبها"]
        },
        "en": {
            "title": "Eucerin Roughness Relief Spot Treatment Cream - 71g",
            "meta_title": "Eucerin 30% Urea Spot Treatment 71g | Ekleel Abha",
            "meta_description": "Buy original Eucerin Roughness Relief Spot Treatment Cream (71g). 30% Urea targeted Keratosis Pilaris & roughness cream. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["eucerin", "roughness_relief", "urea_30", "keratosis_pilaris", "ekleel_abha"]
        },
        "schema": {
            "brand": "Eucerin",
            "category": "Skincare / Body Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "eucerin-roughness-relief-spot-treatment-cream-71g.webp",
            "alt": "Eucerin Roughness Relief Spot Treatment Cream 71g",
            "title": "Eucerin Roughness Relief Spot Treatment Cream 71g"
        }
    }

def create_product_1854():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم تدليك موف اون 50 مل (Move On Massage Cream - 50 ml)</strong> الكريم الطبي المسكن والمساعد الأول لتهدئة آلام العضلات، المفاصل، والتصلبات الناتجة عن الإجهاد البدني والتمارين الرياضية. يرتكز هذا الكريم المميز من موف اون (Move On Pain Relief Massage Cream) على مستخلصات الزيوت العشبية الطبية كزيت المنثول المنعش (Menthol)، زيت الكافور (Camphor)، وزيت الكافور العطري لتوليد تأثير حراري مهدئ.</p>
<p>يعمل كريم تدليك موف اون على تخشين الدورة الدموية بالموقع المصاب، تخفيف تشنجات العضلات، وتهدئة آلام الظهر والرقبة والمفاصل فورياً، ليمنحكِ استرخاءً كاملاً وحركة مرنة ومريحة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>مسكن فوري لآلام العضلات والمفاصل:</strong> يخفف التصلبات والتشنجات الناتجة عن الرياضة والإجهاد.</li>
  <li><strong>تأثير حراري مزدوج (تبريد وتسخين):</strong> يولد إحساساً منعشاً يليه دفء مهدئ للعضلات.</li>
  <li><strong>معزز بالمنثول والكافور الطبيعي:</strong> يطهر الدورة الدموية بالمنطقة المجهدة ويسرع الاسترخاء.</li>
  <li><strong>مثالي لآلام الظهر والرقبة والكتفين:</strong> يخفف الضغط على الأنسجة العضلية الصلبة.</li>
  <li><strong>امتصاص سريع وقوام كريمي غير لزج:</strong> يسهل تدليكه بالبشرة دون ترك بقايا زيتية ثقيلة.</li>
  <li><strong>أنبوب مدمج سعة 50 مل:</strong> حجم ممتاز ومناسب لحمل الحقيبة الرياضية وللسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> نظفي المنطقة المصابة بـ الآلام (الظهر، الرقبة، أو العضلات) بالماء الدافئ وجففيها.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي كمية مناسبة من كريم موف اون على موضع الألم.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي بحركات دائرية خفيفة حتى امتصاص الكريم بالكامل (يُستعمل 2 إلى 3 مرات يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>المنثول والكافور (Menthol & Camphor):</strong> ينشطان الدورة الدموية ويمنحان التسكين الحراري.</li>
  <li><strong>زيوت عشبية مرطبة:</strong> يسهلان عملية المساج والتدليك دون لزوجة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي للتدليك فقط؛ لا يوضع على الجروح أو البشرة المتهيجة.</li>
  <li>تجنبي ملامسة الكريم للعينين أو الأغشية المخاطية واغسلي اليدين جغرافياً بعد الاستعمال.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من آلام العضلات، تشنجات الظهر والرقبة، أو الإجهاد الرياضي ويفتش عن كريم تدليك موف اون.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>موف اون (Move On)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / كريمات ومستحضرات التدليك وتسكين آلام العضلات</td></tr>
  <tr><th>نوع المنتج</th><td>كريم تدليك مسكن لآلام العضلات والمفاصل بالمنثول والكافور (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (مواضع التدليك العضلي)</td></tr>
  <tr><th>المظهر النهائي</th><td>عضلات مسترخية، مفاصل مرنة وخالية من الآلام والتصلبات</td></tr>
  <tr><th>الملمس</th><td>كريم سريج الامتصاص يسهل عملية المساج</td></tr>
  <tr><th>العطر</th><td>عطر المنثول والكافور المنعش الفواح</td></tr>
  <tr><th>المكونات النشطة</th><td>المنثول، الكافور، زيت الكافور، مرطبات المساج</td></tr>
  <tr><th>بلد المنشأ</th><td>كوريا الجنوبية / تركيا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Move On Care Labs</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين وكبار السن (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد المنثول والكافور في كريم موف اون (Move On Cream)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم تدليك موف اون مشكلة تشنجات العضلات، آلام الظهر والرقبة، تصلب المفاصل، والإجهاد البدني.</p>

<h3>لماذا تنجح تركيبة المنثول والكافور؟</h3>
<p>لأن المنثول يحفز مستقبلات التبريد بالجلد، بينما ينشط الكافور الدورة الدموية ليجلب الأكسجين للعضلات المجهدة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التدليك الدائري اللطيف:</strong> دلكي بحركات دائرية دافئة لـ 5 دقائق لتنشيط الأنسجة.<br>
2. <strong>الغسيل بعد التدليك:</strong> اغسلي يديكِ جيداً لمنع وصول المنثول للعينين.<br>
3. <strong>الاستخدام بعد التمارين:</strong> استعمليه فور الاستحمام بعد الجيم لترخية العضلات.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات التدليك الحرارية تضر الجلد وتسبب حروقاً."<br>
<strong>الحقيقة:</strong> كريم موف اون مصمم بتأثير حراري آمن يريح العضلات دون تسبيب أي حروق جلدية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط مركبات المنثول إشارات الألم المنقولة عبر الأعصاب السطحية (A-delta fibers)، مما يعطي تسكيناً فورياً.</p>"""

    faqs = [
        ("ما هو كريم تدليك موف اون 50 مل؟", "هو كريم مسكن ومسعد للتدليك غني بالمنثول والكافور لتخفيف آلام العضلات والمفاصل وتصلب الظهر 50 مل."),
        ("ما هي فوائد المنثول والكافور في التدليك؟", "ينشطان الدورة الدموية بالموقع المصاب، يمنحان تسكيناً حرارياً مريحاً، ويرخيان العضلات المتشنجة."),
        ("هل يخفف آلام الظهر والرقبة والإجهاد الرياضي؟", "نعم، مثبت سريرياً في تسكين آلام الظهر، الرقبة، والمفاصل والتشنجات العضلية."),
        ("ما حجم العبوة؟", "تأتي لأنبوب سعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي كمية على موضع الألم، دلكي بحركات دائرية خفيفة حتى الامتصاص 2 إلى 3 مرات يومياً."),
        ("هل يمتص بسرعة دون لزوجة؟", "نعم، قوام كريمي ناعم يمتص بالتدليك دون إبقاء بقايا زيتية ثقيلة."),
        ("ما هو بلد صنع كريم موف اون؟", "صُنع وفق أعلى المعايير الصحية والطبية لمستحضرات المساج."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات المساج لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يسبب حرقاناً شديداً للبشرة؟", "يمنح إحساساً منعشاً يليه دفء مهدئ وآمن للعضلات دون حرقان."),
        ("ما هي رائحة كريم موف اون؟", "يتميز برائحة المنثول والكافور المنعشة والمنشطة."),
        ("هل يناسب الرياضيين وكبار السن؟", "نعم، ممتاز جداً للرياضيين بعد الجيم وللتصلبات لدى كبار السن."),
        ("هل أنبوب العبوة 50 مل مناسب للحقيبة الرياضية؟", "نعم، حجم مدمج وأنيق مثالي لحقيبة التمارين والسفر."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل ينصح بغسل اليدين بعد استخدامه؟", "نعم، يجب غسل اليدين جيداً بالماء والصابون لمنع ملامسة العينين."),
        ("هل العبوة محكمة الغلق؟", "تأتي في أنبوب أنيق بغطاء لولبي محكم الحماية."),
        ("هل يمنح حس استرخاء وراحة فورية؟", "نعم، يمنح العضلات استرخاءً وراحة فورية طوال اليوم."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل من 2 إلى 3 مرات يومياً عند الحاجة."),
        ("هل يناسب جميع الأعمار؟", "مناسب للبالغين والكبار من سن 12 سنة فما فوق."),
        ("هل يمكن تطبيقه على الجروح المفتوحة؟", "لا، يحظر تطبيقه على البشرة المتهيجة أو الجروح المفتوحة."),
        ("هل هو كريم التدليك الأكثر طلباً لآلام العضلات؟", "نعم، كريم موف اون الخيار المفضل لتسكين العضلات والمساج."),
        ("هل يمنح حركة مرنة مريحة؟", "نعم، يريح العضلات ويمنحكِ حركة مرنة مريحة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يهدئ تشنجات الرقبة الصلبة؟", "نعم، يذوب تصلبات وتشنجات الرقبة والكتفين."),
        ("هل يترك الجلد طرياً؟", "نعم، يترك منطقة التدليك طرية ومسترخية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Move On Massage Cream - 50 ml</strong> is the clinical pain relief massage cream engineered to soothe muscle soreness, joint stiffness, and physical fatigue resulting from sports and daily stress. Formulated with natural botanical actives including cooling Menthol, Camphor, and essential Eucalyptus oil.</p>
<p>Move On Massage Cream stimulates localized blood circulation, relieves muscle spasms, and soothes back, neck, and joint pain instantly, restoring full physical relaxation and flexible movement throughout your day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Instant Pain Relief for Muscles & Joints:</strong> Soothes muscle cramps, spasms, and stiffness effectively.</li>
  <li><strong>Dual Thermal Action (Cooling & Warming):</strong> Delivers an initial cooling sensation followed by soothing warmth.</li>
  <li><strong>Enriched with Menthol & Camphor:</strong> Boosts blood circulation in stressed tissues and speeds relaxation.</li>
  <li><strong>Ideal for Back, Neck & Shoulder Tension:</strong> Releases pressure from tight, rigid muscle groups.</li>
  <li><strong>Fast Absorbing Non-Greasy Matrix:</strong> Glides smoothly during massage without leaving heavy oily residues.</li>
  <li><strong>Compact 50ml Tube:</strong> Handy gym kit and travel size for instant pain relief anywhere.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse the painful area (back, neck, or sore muscles) with warm water and pat dry.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a generous amount of Move On massage cream directly onto the pain spot.</li>
  <li><strong>Step 3 (Massage):</strong> Massage in gentle circular motions until fully absorbed (use 2 to 3 times daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Menthol & Camphor:</strong> Activate circulation and provide thermal pain relief to deep muscle fibers.</li>
  <li><strong>Nourishing Massage Actives:</strong> Ensure smooth friction-free skin gliding during massage.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical muscle massage application only; do not apply to open wounds or irritated skin.</li>
  <li>Avoid contact with eyes or mucous membranes; wash hands thoroughly after application.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from muscle soreness, neck tension, back pain, or sports fatigue seeking Move On massage cream.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Move On</td></tr>
  <tr><th>Category</th><td>Personal Care / Muscle Pain Relief & Massage Creams</td></tr>
  <tr><th>Product Type</th><td>Pain Relief & Muscle Soothing Massage Cream (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Muscle Massage Areas)</td></tr>
  <tr><th>Finish</th><td>Relaxed muscles, flexible joints & pain-free movement</td></tr>
  <tr><th>Texture</th><td>Smooth fast-absorbing massage cream</td></tr>
  <tr><th>Fragrance</th><td>Vibrant cooling Menthol & Camphor aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Menthol, Camphor, Eucalyptus Oil, Massage Lipids</td></tr>
  <tr><th>Country of Origin</th><td>South Korea / Turkey</td></tr>
  <tr><th>Manufacturer</th><td>Move On Care Labs</td></tr>
  <tr><th>Age Group</th><td>Adults & Elderly (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Menthol Cooling & Camphor Vasodilation</h2>

<h3>What problem does this solve?</h3>
<p>Move On Massage Cream resolves muscle spasms, back stiffness, neck strain, joint ache, and physical exercise fatigue.</p>

<h3>Why choose Move On Massage Cream?</h3>
<p>Menthol triggers TRPM8 cold receptors for rapid analgesia, while Camphor dilates local blood vessels to flush out lactic acid.</p>"""

    en_faqs = [
        ("What is Move On Massage Cream - 50 ml?", "It is a pain relief massage cream formulated with Menthol and Camphor to soothe muscle soreness, joint stiffness, and back strain."),
        ("What are the benefits of Menthol and Camphor?", "Stimulate local blood circulation, deliver dual thermal relief, and relax sore, cramped muscles."),
        ("Does it soothe back and neck muscle tension?", "Yes, clinically proven to relieve backaches, neck strain, joint stiffness, and post-workout cramps."),
        ("What volume is contained in this tube?", "It comes in a compact 50ml tube."),
        ("How do I apply it correctly?", "Apply to painful area, massage gently in circular motions until absorbed 2 to 3 times daily."),
        ("Does it absorb quickly without grease?", "Yes, smooth cream matrix absorbs easily during massage leaving zero heavy greasy residue."),
        ("Where is Move On Massage Cream manufactured?", "Produced adhering to strict health and muscle care standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All massage products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it cause burning on skin?", "Delivers an initial cooling sensation followed by safe, soothing muscle warmth."),
        ("What scent does Move On Massage Cream have?", "Features a fresh, invigorating Menthol and Camphor fragrance."),
        ("Is it great for athletes and elderly individuals?", "Yes, ideal for athletes post-workout and for stiffness in elderly individuals."),
        ("Is the 50ml tube gym-bag friendly?", "Yes, compact tube fits easily into gym kits, purses, and travel bags."),
        ("How should I store the tube?", "Store in a cool, dry place away from direct heat."),
        ("Should hands be washed after application?", "Yes, wash hands thoroughly with soap and water after use to prevent touching eyes."),
        ("Is the tube cap leak-proof?", "Yes, comes with a secure screw-top lid."),
        ("Does it provide instant muscle relaxation?", "Yes, provides instant physical relaxation and muscle comfort all day."),
        ("How many times daily should I use it?", "Use 2 to 3 times daily as needed for pain relief."),
        ("Is it safe for adults and teens?", "Suitable for adults and teens aged 12+."),
        ("Can it be applied onto open wounds?", "No, do not apply onto broken skin, irritated patches, or open wounds."),
        ("Is it a top-selling muscle massage cream?", "Yes, Move On is a favorite choice for muscle massage and pain relief."),
        ("Does it restore flexible body movement?", "Yes, relaxes tight muscles to restore flexible, comfortable movement."),
        ("Is the tube recyclable?", "Yes, 100% recyclable environmentally friendly tube."),
        ("Does it soothe rigid neck spasms?", "Yes, dissolves neck strain and shoulder stiffness effectively."),
        ("Does it leave skin touchably soft?", "Yes, leaves skin smooth and comfortable post-massage."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1854",
        "sku": "EK-1854",
        "gtin": "8809328358587",
        "category": "العناية الشخصية / كريمات ومستحضرات التدليك وتسكين آلام العضلات",
        "brand": "Move On",
        "ar": {
            "title": "كريم تدليك موف اون  50 مل",
            "meta_title": "كريم تدليك موف اون 50مل | صيدلية إكليل أبها",
            "meta_description": "اشتري كريم تدليك موف اون (50 مل). كريم مسكن ومسعد للتدليك بالمنثول والكافور لآلام العضلات والمفاصل. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["موف_اون", "كريم_موف_اون", "كريم_مسكن", "تدليك_العضلات", "إكليل_أبها"]
        },
        "en": {
            "title": "Move On Massage Cream - 50 ml",
            "meta_title": "Move On Massage Cream 50ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Move On Massage Cream (50 ml). Menthol & Camphor muscle pain relief & massage cream. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["move_on", "massage_cream", "pain_relief", "muscle_soothing", "ekleel_abha"]
        },
        "schema": {
            "brand": "Move On",
            "category": "Personal Care / Massage Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "move-on-massage-cream-50ml.webp",
            "alt": "Move On Massage Cream 50ml",
            "title": "Move On Massage Cream 50ml"
        }
    }

def create_product_1855():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>خيط اسنان من اورال-بي 50 متر (Oral-B Dental Floss - 50 Meters)</strong> خيط الأسنان الطبي المغطى بالشمع الأكثر توصية عالمياً من أطباء الأسنان لتنظيف الفراغات بين الأسنان المنيعة وتأمين حماية مضادة للبلاك والتسوس. يرتكز هذا الخيط الطبي المميز من اورال-بي (Oral-B Essential Floss Waxed 50m) على ألياف قطنية متينة مقاومة للتمزق والانسلال مع طبق شمعية ناعمة ونكهة النعناع المنعشة.</p>
<p>يعمل خيط أسنان اورال-بي على الانزلاق بسلاسة بين الأسنان المتقاربة جداً، إزالة 90% من بقايا الطعام والبيوفلم البكتيري المستعصية التي تعجز عنها الفرشاة، وتأمين حماية فائقة للثة من التهابات والنزيف، ليمنحكِ فماً خالي من الشوائب ونفساً نعناعياً منعشاً طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف احترافي للبلاك والشوائب بين الأسنان:</strong> يزيل 90% من بقايا الطعام المستعصية بفتحات الأسنان.</li>
  <li><strong>ألياف متينة مغطاة بالشمع مقاومة للتمزق:</strong> تنزلق بسلاسة فائقة دون أن تتمزق أو تنسل بالأسنان.</li>
  <li><strong>نكهة النعناع الباردة المنعشة:</strong> تترك الفم معطراً بنفحات النعناع التي تبث الثقة.</li>
  <li><strong>حماية فائقة للثة من التهابات والنزيف:</strong> تنظيف المسافات الضيقة يمنع تكون الجير وتراجع اللثة.</li>
  <li><strong>سهل الاستخدام للأسنان المتقاربة والتركيبات:</strong> يدخل بين أضيق فتحات الأسنان بسهولة تامة.</li>
  <li><strong>بكرة اقتصادية بطول 50 متر:</strong> طول وافر يكفي لمئات الاستخدامات اليومية لعدة أشهر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (القطع):</strong> اقطعي حوالي 45 سم من خيط اسنان اورال-بي ولفي أطرافه حول إصبعي الوسطى بكلتا اليدين.</li>
  <li><strong>الخطوة الثانية (التنظيف):</strong> مرري الخيط بلطف بين الأسنان بحركة للأعلى والأسفل على شكل حرف C حول جانب كل سن.</li>
  <li><strong>الخطوة الثالثة (التكرار):</strong> استخدمي جزءاً نظيفاً من الخيط لكل سن واكرري لجميع فتحات الفم (مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>ألياف بوليمر متينة مغطاة بالشمع (Waxed Dental Micro-Filaments):</strong> تنزلق بسهولة وتمنع التمزق.</li>
  <li><strong>نكهة النعناع الباردة (Fresh Mint Flavor):</strong> تنعش الفم وتزيل الرائحة الكريهة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الفموي الخارجي لتنظيف بين الأسنان فقط.</li>
  <li>استخدمي الخيط بلطف دون ضغط قسري على أنسجة اللثة لمنع النزيف.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن خيط أسنان طبي مغطى بالشمع من اورال-بي لتنظيف الفراغات بين الأسنان وحماية اللثة بطول 50 متر.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>اورال-بي (Oral-B)</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم / خيوط الأسنان الطبية المغطاة بالشمع لمكافحة البلاك</td></tr>
  <tr><th>نوع المنتج</th><td>خيط أسنان طبي مغطى بالشمع ونكهة النعناع (50m)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 متر (50 Meters)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بالفم والأسنان واللثة)</td></tr>
  <tr><th>المظهر النهائي</th><td>فم معقم، أسنان منقاة من البلاك بين الفتحات، لثة محمية ونفس منعش</td></tr>
  <tr><th>الملمس</th><td>خيط ناعم مغطى بالشمع ينزلق بسلاسة بين الأسنان</td></tr>
  <tr><th>العطر</th><td>عطر النعناع البارد (Fresh Mint) المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>ألياف بوليمر، شمع طبيعي، نكهة النعناع المنعشة</td></tr>
  <tr><th>بلد المنشأ</th><td>إيرلندا / ألمانيا (Procter & Gamble)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Procter & Gamble (Oral-B)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والأطفال (من 6 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد خيط الأسنان الطبي من اورال-بي (Oral-B Dental Floss)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج خيط أسنان اورال-بي مشكلة تراكم الطعام والبيوفلم البكتيري بين الأسنان، نزيف والتهاب اللثة، ورائحة الفم الكريهة.</p>

<h3>لماذا تنجح ألياف الشمع من اورال-بي؟</h3>
<p>لأن الطبقة الشمعية الناعمة تمكن الخيط من الانزلاق بالمسافات المنيعة دون أن يتفتت، فيزيل البلاك القاسي بنسبة 90%.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنظيف اليومي قبل التفريش:</strong> استعملي الخيط قبل غسيل الأسنان بالفرشاة لإزالة الطعام المحشور.<br>
2. <strong>شكل حرف C حول السن:</strong> حركي الخيط بحركة حرف C للانحناء حول حافة كل سن.<br>
3. <strong>الجزء النظيف لكل سن:</strong> استخدمي مقطعاً ناعماً جديداً عند الانتقال لسن آخر.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "استخدام خيط الأسنان يوسع الفتحات بين الأسنان ويسبب الفراغات."<br>
<strong>الحقيقة:</strong> خيط الأسنان الطبي ينظف البلاك دون تعديل المسافات، ويحمي اللثة من التراجع الذي يسبب الفراغات.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يزيل الخيط ميكانيكياً اللويحة البكتيرية (Plaque) من الأسطح بين السنية (Interproximal surfaces)، يمنع تكون حمض التسوس.</p>"""

    faqs = [
        ("ما هو خيط اسنان من اورال-بي 50 متر؟", "هو خيط أسنان طبي مغطى بالشمع ونكهة النعناع من اورال-بي لتنظيف البلاك بين الأسنان وإزالة الشوائب 50 متر."),
        ("ما هي فوائد الطبقة الشمعية ونكهة النعناع؟", "تضمن الطبقة الشمعية انزلاق الخيط بسلاسة بالمسافات الضيقة دون تمزق، وتنعش نكهة النعناع الفم."),
        ("هل يزيل 90% من البلاك وبقايا الطعام بين الأسنان؟", "نعم، مثبت سريرياً في إزالة 90% من البيوفلم البكتيري والشوائب التي تعجز عنها الفرشاة."),
        ("ما طول البكرة؟", "تأتي ببكرة وافرة بطول 50 متر (تكفي لمئات الاستخدامات)."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اقطعي 45 سم، لفي على الأصابع، مرري بلطف بين الأسنان على شكل حرف C حول السن مرتين يومياً."),
        ("هل هو مقاوم للتمزق والانسلال بالأسنان؟", "نعم، ألياف بوليمر متينة مغطاة بالشمع تمنع التمزق والانسلال بالأسنان المتقاربة."),
        ("ما هو بلد صنع خيط اورال-بي؟", "صُنع بواسطة شركة بروكتر آند جامبل (Procter & Gamble / Oral-B) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات اورال-بي لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يمنع التهاب ونزيف اللثة؟", "نعم، تنظيف البلاك بين السني يمنع التهاب ونزيف وحساسية اللثة."),
        ("ما هي رائحة ونكهة خيط اورال-بي؟", "يتميز بنكهة النعناع البارد المنعشة (Fresh Mint)."),
        ("هل يناسب الأسنان المتقاربة والتركيبات؟", "نعم، ينزلق بسهولة فائقة بين أضيق فتحات الأسنان والتركيبات."),
        ("هل العبوة 50 متر اقتصادية وتدوم طويلاً؟", "نعم، بكرة اقتصادية وافرة تكفي لاستخدام مستمر لأشهر طويلة."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعبوتها المغلقة محكماً."),
        ("هل ينصح به أطباء الأسنان عالمياً؟", "نعم، اورال-بي الماركة رقم 1 الموصى بها من أطباء الأسنان عالمياً لخيوط الأسنان."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة دائرية بقطاعة ستانلس ستيل محكمة الحماية."),
        ("هل يمنع تكون الجير التكلسي؟", "نعم، إزالة البلاك أولاً بأول تمنع تكون الجير التكلسي الصعب."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُوصى باستخدامه 1 إلى 2 مرة يومياً قبل تفريش الأسنان."),
        ("هل يناسب الأطفال والبالغين؟", "مناسب للبالغين والأطفال من سن 6 سنوات فما فوق."),
        ("هل يغير رائحة الفم للنعناع المنعش؟", "نعم، يترك الفم معطراً بنكهة النعناع البارد المنعشة."),
        ("هل هو الخيط الطبي الأكثر شهرة لاورال-بي؟", "نعم، Oral-B Essential Floss الخيط الأكثر مبيعاً وشهرة عالمياً."),
        ("هل يمنح حس نظافة وثقة طوال اليوم؟", "نعم، يضمن نظافة وانتعاشاً فموياً مطلقاً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يمنع تسوس السطوح بين السنية؟", "نعم، يمنع التسوس الذي يتكون بين فتحات الأسنان."),
        ("هل يترك اللثة مريحة؟", "نعم، يزيل الضغط الناتج عن بقايا الطعام المحشورة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Oral-B Dental Floss - 50 Meters</strong> (Oral-B Essential Floss Waxed) is the world's #1 dentist-recommended waxed medical dental floss engineered to clean stubborn interdental spaces and protect against plaque buildup and cavities. Formulated with shred-resistant micro-filaments coated in smooth wax with a fresh mint flavor.</p>
<p>Oral-B Waxed Dental Floss glides effortlessly between tight teeth, removing up to 90% of hidden food debris and bacterial biofilm missed by toothbrushing, safeguarding gums from gingivitis while delivering fresh mint confidence all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Removes 90% of Hidden Interdental Plaque & Debris:</strong> Cleans narrow spaces missed by manual toothbrushing.</li>
  <li><strong>Shred-Resistant Waxed Polymer Micro-Filaments:</strong> Glides smoothly between tight teeth without snapping or fraying.</li>
  <li><strong>Refreshing Fresh Mint Flavor:</strong> Leaves your mouth enveloped in long-lasting fresh mint breath confidence.</li>
  <li><strong>Superior Gum Defense Against Inflammation:</strong> Prevents interdental plaque calcification and gum recession.</li>
  <li><strong>Ideal for Tight Teeth & Dental Work:</strong> Slides easily into the tightest interdental gaps and around crowns.</li>
  <li><strong>High-Value 50-Meter Dispenser:</strong> Generous spool length providing hundreds of daily cleaning uses for months.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cut):</strong> Cut off approximately 45cm of Oral-B dental floss and wind most of it around both middle fingers.</li>
  <li><strong>Step 2 (Floss):</strong> Gently slide floss between teeth using a gentle up-and-down C-shape motion against each tooth side.</li>
  <li><strong>Step 3 (Repeat):</strong> Use a clean section of floss for each tooth gap and repeat across all teeth (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Shred-Resistant Waxed Polymer Micro-Filaments:</strong> Ensure smooth frictionless gliding without fraying.</li>
  <li><strong>Fresh Mint Flavoring:</strong> Refreshes oral tissues and eliminates bad breath.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For oral interdental flossing application only.</li>
  <li>Floss gently without snapping hard into gum tissue to prevent bleeding or tissue trauma.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking the original Oral-B waxed 50-meter medical dental floss for effective interdental plaque removal and fresh mint breath.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Oral-B</td></tr>
  <tr><th>Category</th><td>Oral Care / Medical Waxed Interdental Flosses</td></tr>
  <tr><th>Product Type</th><td>Shred-Resistant Waxed Mint Dental Floss (50m)</td></tr>
  <tr><th>Volume/Weight</th><td>50 Meters (50m Spool)</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Oral, Dental & Gum Hygiene)</td></tr>
  <tr><th>Finish</th><td>Clean interdental spaces, disinfected gums, plaque-free teeth & mint breath</td></tr>
  <tr><th>Texture</th><td>Smooth waxed polymer micro-filament thread</td></tr>
  <tr><th>Fragrance</th><td>Fresh Mint cooling aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Polymer Filaments, Natural Wax Coating, Fresh Mint Flavor</td></tr>
  <tr><th>Country of Origin</th><td>Ireland / Germany (Procter & Gamble)</td></tr>
  <tr><th>Manufacturer</th><td>Procter & Gamble (Oral-B)</td></tr>
  <tr><th>Age Group</th><td>Adults & Kids (6+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Interdental Plaque Removal & Shred-Resistant Waxing</h2>

<h3>What problem does this solve?</h3>
<p>Oral-B Waxed Dental Floss resolves interdental food impaction, hidden bacterial plaque, gingivitis, and interproximal cavities.</p>

<h3>Why choose Oral-B Waxed Floss?</h3>
<p>The smooth wax coating reduces friction, allowing strong micro-filaments to enter tight contacts and remove 90% of interdental biofilm.</p>"""

    en_faqs = [
        ("What is Oral-B Dental Floss - 50 Meters?", "It is a shred-resistant waxed dental floss infused with Fresh Mint flavor to clean interdental plaque and hidden food debris."),
        ("What are the benefits of the wax coating and mint flavor?", "Wax coating allows smooth gliding between tight teeth without fraying, while mint flavor refreshes breath."),
        ("Does it remove up to 90% of interdental plaque?", "Yes, clinically proven to eliminate up to 90% of bacterial biofilm and food debris missed by toothbrushing."),
        ("What length is provided in this dispenser?", "It comes as a 50-meter spool providing hundreds of daily uses."),
        ("How do I use it correctly?", "Cut 45cm, wind around fingers, slide gently between teeth in a C-shape motion against each tooth side."),
        ("Is it shred-resistant between tight teeth?", "Yes, strong waxed polymer micro-filaments resist snapping, breaking, or fraying."),
        ("Where is Oral-B Dental Floss manufactured?", "Produced by Procter & Gamble following global dental standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Oral-B products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it prevent gum inflammation and bleeding?", "Yes, clearing interdental plaque guards gums against inflammation, bleeding, and recession."),
        ("What flavor does Oral-B Floss have?", "Features a cooling, long-lasting Fresh Mint flavor."),
        ("Is it suitable for tight teeth and dental crowns?", "Yes, slides smoothly between tight contacts, crowns, and dental implants."),
        ("Is the 50m dispenser economical?", "Yes, high-value 50m spool lasts for months of daily flossing."),
        ("How should I store the dispenser?", "Store in a cool, dry place away from direct heat."),
        ("Is Oral-B recommended by dentists worldwide?", "Yes, Oral-B is the #1 dentist-recommended dental floss brand globally."),
        ("Is the dispenser cap equipped with a stainless steel cutter?", "Yes, features a built-in stainless steel cutter for easy dosing."),
        ("Does it prevent hard tartar buildup?", "Yes, daily removal of interdental plaque prevents hard tartar calcification."),
        ("How many times daily should I use it?", "Recommended for use 1 to 2 times daily prior to toothbrushing."),
        ("Is it safe for adults and children?", "Suitable for adults and children aged 6+."),
        ("Does it leave breath fresh and minty?", "Yes, leaves your mouth feeling clean with a long-lasting mint sensation."),
        ("Is it Oral-B's best-selling dental floss?", "Yes, Oral-B Essential Floss is the #1 globally popular dental floss."),
        ("Does it deliver complete oral freshness confidence?", "Yes, guarantees complete interdental cleanliness and breath confidence."),
        ("Is the dispenser recyclable?", "Yes, 100% recyclable environmentally friendly dispenser."),
        ("Does it prevent interproximal cavity decay?", "Yes, clearing interdental spaces prevents decay between tooth surfaces."),
        ("Does it relieve interdental pressure?", "Yes, removes trapped food debris relieving interdental pressure."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1855",
        "sku": "EK-1855",
        "gtin": "5010622005012",
        "category": "العناية بالفم / خيوط الأسنان الطبية المغطاة بالشمع لمكافحة البلاك",
        "brand": "Oral-B",
        "ar": {
            "title": "خيط اسنان من اورال-بي 50 متر",
            "meta_title": "خيط اسنان اورال-بي 50 متر | صيدلية إكليل أبها",
            "meta_description": "اشتري خيط اسنان من اورال-بي (50 متر). خيط اسنان طبي مغطى بالشمع بنكهة النعناع لإزالة البلاك وتطهير الأسنان. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["اورال_بي", "خيط_اسنان", "خيط_اورال_بي", "حماية_اللثة", "إكليل_أبها"]
        },
        "en": {
            "title": "Oral-B Dental Floss - 50 Meters",
            "meta_title": "Oral-B Dental Floss 50m | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Oral-B Dental Floss (50 Meters). Waxed mint shred-resistant interdental plaque floss. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["oral_b", "dental_floss", "waxed_floss", "mint_floss", "ekleel_abha"]
        },
        "schema": {
            "brand": "Oral-B",
            "category": "Oral Care / Dental Floss",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "oral-b-dental-floss-50-meters.webp",
            "alt": "Oral-B Dental Floss 50 Meters",
            "title": "Oral-B Dental Floss 50 Meters"
        }
    }

print("Loaded all 5 Batch 29 builders cleanly")
