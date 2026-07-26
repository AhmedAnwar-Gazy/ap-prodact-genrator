import json, os

def create_product_1769():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم العناية بالبشرة المتهيجة والحساسة لترميم الحاجز الواقي - 100 مل (Soothing Care Cream for Irritated Skin - 100ml)</strong> البلسم العلاجي المكثف المصمم لإعادة بناء وتدعيم حاجز البشرة الواقي وتهدئة الالتهابات والاحمرار فورياً. يجمع هذا المستحضر المتطور بين الخواص المرممة والمضادة للتهيج لمركبات السيكا (Centella Asiatica / Cica)، البانثينول (Pro-Vitamin B5)، والسيراميدات النقية، حيث يقلل الشعور بالحكة والحرارة والتحسس الناتج عن التقشير، الشمس، أو العوامل البيئية الجافة.</p>
<p>يمتاز الكريم بقوام خفيف سريع الامتصاص يشكل حجاب ترطيب واقٍ دون سد المسام، مما يجعله مثاليًا للوجه والجسم ولجميع الفئات العمرية التي تعاني من البشرة الحساسة أو المتهيجة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترميم واستعادة حاجز البشرة الواقي:</strong> يدعم السيراميد والبانثينول بناء غشاء البثور الواقي.</li>
  <li><strong>تهدئة فورية للاحمرار والحكة:</strong> يخفف التهيج والحرارة الناتجة عن التقشير والتعرض للشمس والجفاف.</li>
  <li><strong>ترطيب عميق طويل المفعول:</strong> يحبس الماء داخل خلايا الجلد ويمنع التبخر الجلدي (TEWL).</li>
  <li><strong>خالي من العطور والبارابين:</strong> تركيبة لطيفة وآمنة تماماً للبشرة الأكثر حساسية.</li>
  <li><strong>قوام خفيف وغير كوميدوجينيك:</strong> يمتص فورياً دون ترك أثر دهني لزج أو سد للمسام.</li>
  <li><strong>عبوة أنيقة سعة 100 مل:</strong> تكفي لعناية يومية متكاملة ومستمرة للوجه والجسم.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> اغسلي المنطقة المتهيجة بالماء الفاتر وجففيها بلطف.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي كمية منا سبة من كريم العناية المهدئ على البشرة.</li>
  <li><strong>الخطوة الثالثة (التوزيع):</strong> وزعي الكريم بلطف ودلكيه حتى يتم امتصاصه كاملاً (يُستعمل 2-3 مرات يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مستخلص السيكا (Centella Asiatica):</strong> يهدئ التهابات الجلد ويسرع ترميم خلايا البشرة.</li>
  <li><strong>البانثينول (Pro-Vitamin B5):</strong> يمنح ترطيباً عميقاً ويلطف تهيج الجلد.</li>
  <li><strong>السيراميدات النقية (Ceramides):</strong> تعيد بناء الحاجز الدهني الواقي للبشرة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الوجه والجسم فقط.</li>
  <li>تجنبي ملامسة الكريم المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من تضرر حاجز البشرة، احمرار، تهيج بعد التقشير أو الشمس، والحكة الجافة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>عام / صيدلية إكليل أبها</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات ترميم وتهدئة البشرة</td></tr>
  <tr><th>نوع المنتج</th><td>كريم العناية بالبشرة المتهيجة والحساسة (100ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الحساسة والمتهيجة والتالفة</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة هادئة، مرطبة، خالية من الاحمرار والحكة</td></tr>
  <tr><th>الملمس</th><td>كريم ناعم سريع الامتصاص غير دهني</td></tr>
  <tr><th>العطر</th><td>عديم العطور (Unscented)</td></tr>
  <tr><th>المكونات النشطة</th><td>سيكا (سنبيلا)، بانثينول B5، سيراميدات، جليسرين</td></tr>
  <tr><th>بلد المنشأ</th><td>اليونان / فرنسا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Dermo Skin Care Labs</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لترميم حاجز البشرة وتهدئة التهيج (Soothing Care)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم العناية المهدئ مشكلة تلف حاجز البشرة الواقي، الاحمرار النجم عن التقشير والشمس، والحكة والحساسية الجافة.</p>

<h3>لماذا يتلف حاجز البشرة؟</h3>
<p>يتأثر غشاء البشرة بالتقشير القاسي والمنظفات والشمس، فتتسرب السيراميدات وتفقد الخلايا ماءها فتظهر الحساسية والاحمرار.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام المباشر بعد التقشير:</strong> وضعي الكريم فورياً لترميم خلايا الجلد.<br>
2. <strong>تجنب المنظفات القاسية:</strong> استعملي غسولاً خالياً من الصابون للبشرة الحساسة.<br>
3. <strong>التطبيق التكراري:</strong> استعملي الكريم كلما شعرتِ بحرارة أو حكة بالجلد.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات الترميم تثقل البشرة وتسبب الحبوب."<br>
<strong>الحقيقة:</strong> كريم العناية المهدئ مصمم بقوام غير كوميدوجينيك يمتص فورياً ويرمم دون سد المسام.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تندمج السيراميدات والبانثينول مع الليبيدات الفجوية بالبشرة، بينما تخمد مركبات السيكا المسارات الالتهابية فورياً وتسرع اندمال الخلايا.</p>"""

    faqs = [
        ("ما هو كريم العناية بالبشرة المتهيجة والحساسة 100 مل؟", "هو بلسم علاج مهدئ ومكثف يحتوي على السيكا والبانثينول والسيراميدات لترميم حاجز البشرة وتسكين الاحمرار."),
        ("ما هي فوائد السيكا والسيراميدات للبشرة؟", "تهدئ السيكا الاحمرار والحرارة، بينما تعيد السيراميدات بناء غشاء البشرة الواقي وتمنع الجفاف."),
        ("هل يناسب البشرة المتهيجة بعد التقشير والشمس؟", "نعم، ممتازة جداً لتهدئة الجلد وتخفيف حرارة التقشير وحروق الشمس الخفيفة."),
        ("ما حجم العبوة؟", "تأتي بحجم 100 مل."),
        ("هل يترك ملمساً زيتيّاً ثقيلاً؟", "لا، يمتص بالكامل دون ترك طبقة دهنية أو لزوجة على البشرة."),
        ("هل العطر مجاني وخالي من البارابين؟", "نعم، خالي تماماً من العطور والبارابين والمواد القاسية."),
        ("ما هو بلد صنع المنتج؟", "تم تصنيعه وفق أعلى معايير الجودة الفرنسية والأوروبية للبشرة."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع الكريمات لدى إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("كم مرة يُنصح باستخدامه يومياً؟", "يُستخدم من 2 إلى 3 مرات يومياً أو كلما شعرتِ بتهيج البشرة."),
        ("هل يناسب الوجه والجسم معاً؟", "نعم، آمن وممتاز لبشرة الوجه وكافة مناطق الجسم."),
        ("هل يسبب سد المسام (كوميدوجينيك)؟", "لا، تركيبة غير كوميدوجينيك آمنة للمسام."),
        ("هل يناسب الأطفال؟", "مناسب للأطفال والبالغين من سن 3 سنوات فما فوق."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل يساعد في تقليل الحكة الجافة؟", "نعم، يهدئ الحكة ويرطب الجفاف فورياً."),
        ("هل يناسب البشرة المصابة بالأكزيما الخفيفة؟", "نعم، يلطف تهيج الأكزيما الخفيفة ويحمي الجلد."),
        ("هل العبوة 100 مل مناسبة للسفر؟", "نعم، حجم 100 مل مدمج ومثالي للسفر وتسهيل الحمل."),
        ("هل يعيد نضارة الوجه المجهد؟", "نعم، ترميم حاجز البشرة يحفظ الماء ويعيد الإشراقة."),
        ("هل يلزم غسله بالماء؟", "لا، يترك على البشرة للامتصاص الكامل."),
        ("هل يمكن وضعه تحت المكياج؟", "نعم، يوضع كمكياج مهدئ للبشرة الحساسة قبل المكياج."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب لكلا الجنسين."),
        ("هل يقلل آثار الاحمرار الناتجة عن الحلاقة؟", "نعم، ممتاز لتهدئة البشرة بعد الحلاقة."),
        ("هل يمنع تمدد التسلخات الجافة؟", "نعم، يغلف الجلد ويمنع تسرب الرطوبة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في أنبوب محكم يسهل التحكم بالكمية."),
        ("هل يسبب أي حرقان عند التطبيق؟", "تركيبة لطيفة جداً لا تسبب حرقاناً."),
        ("هل هو خيار ممتاز لجميع الفصول؟", "نعم، يحمي البشرة في الصيف والشتاء.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Soothing Care Cream for Irritated Skin - 100ml</strong> is an intensive restorative barrier cream formulated to repair damaged skin barriers and calm redness and irritation instantly. Fusing the soothing power of Centella Asiatica (Cica), Pro-Vitamin B5 (Panthenol), and pure Ceramides, it halts itching, burning sensations, and dryness caused by chemical peels, sun exposure, or harsh weather.</p>
<p>Featuring a lightweight, fast-absorbing non-comedogenic texture, it forms a protective moisture shield without clogging pores, making it essential for sensitive face and body care across all ages.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Repairs & Restores Skin Barrier:</strong> Ceramides and Panthenol rebuild the compromised epidermal layer.</li>
  <li><strong>Instant Calming for Redness & Itching:</strong> Soothes irritation, peeling heat, and sun-exposed skin.</li>
  <li><strong>Long-Lasting Deep Hydration:</strong> Seals water into skin cells, preventing transepidermal water loss (TEWL).</li>
  <li><strong>Fragrance & Paraben Free:</strong> Hypoallergenic, safe formula tailored for sensitive skin types.</li>
  <li><strong>Non-Comedogenic Lightweight Texture:</strong> Absorbs in seconds without greasy or sticky residue.</li>
  <li><strong>Convenient 100ml Tube:</strong> Perfect volume for daily face and body skin restoration.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse target area with warm water and gently pat dry.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a suitable amount of Soothing Care Cream onto skin.</li>
  <li><strong>Step 3 (Massage):</strong> Smooth gently until fully absorbed; use 2 to 3 times daily as needed.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Centella Asiatica Extract (Cica):</strong> Soothes skin flaring and accelerates cell repair.</li>
  <li><strong>Panthenol (Pro-Vitamin B5):</strong> Infuses deep moisture and calms irritation.</li>
  <li><strong>Pure Ceramides:</strong> Reconstruct the skin's natural protective lipid barrier.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external face and body application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with a damaged skin barrier, post-peel redness, sun irritation, or dry itchy skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Generic / Ekleel Abha Pharmacy</td></tr>
  <tr><th>Category</th><td>Skincare / Restorative & Soothing Creams</td></tr>
  <tr><th>Product Type</th><td>Barrier Restorative & Soothing Care Cream</td></tr>
  <tr><th>Volume/Weight</th><td>100 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Sensitive, Irritated & Damaged Skin</td></tr>
  <tr><th>Finish</th><td>Calmed, hydrated, redness-free & healthy skin</td></tr>
  <tr><th>Texture</th><td>Lightweight fast-absorbing smooth cream</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-Free (Unscented)</td></tr>
  <tr><th>Active Ingredients</th><td>Centella Asiatica (Cica), Panthenol B5, Ceramides</td></tr>
  <tr><th>Country of Origin</th><td>Greece / France</td></tr>
  <tr><th>Manufacturer</th><td>Dermo Skin Care Labs</td></tr>
  <tr><th>Age Group</th><td>All Ages (3+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Cica Extract & Barrier Lipid Restoration</h2>

<h3>What problem does this solve?</h3>
<p>Soothing Care Cream resolves skin barrier damage, post-peel redness, sun flare-ups, and dry itching.</p>

<h3>Why choose Cica & Ceramides?</h3>
<p>Ceramides integrate into intercellular lipid matrix gaps, while Cica downregulates inflammatory skin pathways.</p>"""

    en_faqs = [
        ("What is Soothing Care Cream 100ml?", "It is an intensive barrier repair cream enriched with Cica, Panthenol, and Ceramides to soothe irritated, sensitive skin."),
        ("What are the benefits of Cica and Ceramides?", "Cica calms redness and heat, while Ceramides reconstruct the protective skin barrier."),
        ("Is it effective post-chemical peel and sun exposure?", "Yes, it excels at calming heat, redness, and irritation post-peel and after sun exposure."),
        ("What volume is contained in this tube?", "It comes in a convenient 100ml tube."),
        ("Does it leave a greasy film?", "No, it absorbs in seconds without leaving sticky or oily residue."),
        ("Is it fragrance and paraben free?", "Yes, it is 100% fragrance-free, paraben-free, and hypoallergenic."),
        ("Where is it manufactured?", "It is produced under strict European dermatological standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original from certified distributors."),
        ("How often should I apply it?", "Apply 2 to 3 times daily or whenever skin feels irritated."),
        ("Is it safe for face and body?", "Yes, safe and effective for facial skin and body areas."),
        ("Is it non-comedogenic?", "Yes, it will not clog pores."),
        ("Is it safe for children?", "Safe for adults, children, and infants aged 3+."),
        ("How should I store it?", "Store in a cool, dry place away from heat."),
        ("Does it soothe dry itching?", "Yes, it relieves dry itching and locks in hydration."),
        ("Is it suitable for mild eczema skin?", "Yes, it soothes mild eczema flaring and protects skin."),
        ("Is the 100ml tube travel-friendly?", "Yes, compact 100ml size is ideal for travel."),
        ("Does it restore dull skin radiance?", "Yes, repairing the skin barrier restores healthy radiance."),
        ("Does it require rinsing?", "No, leave it on for complete skin absorption."),
        ("Can it be worn under makeup?", "Yes, acts as a soothing base for sensitive skin before makeup."),
        ("Can both men and women use it?", "Yes, it is a unisex soothing cream."),
        ("Does it calm post-shave irritation?", "Yes, excellent for soothing skin redness after shaving."),
        ("Does it prevent skin flaking?", "Yes, it seals moisture to stop dry flaking."),
        ("Is the tube easy to use?", "Yes, comes in an easy-squeeze hygienic tube."),
        ("Does it sting upon application?", "No, ultra-gentle formula causes zero stinging."),
        ("Is it good year-round?", "Yes, protects skin against summer sun and winter cold.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1769",
        "sku": "EK-1769",
        "gtin": "5205507010124",
        "category": "العناية بالبشرة / كريمات ترميم وتهدئة البشرة",
        "brand": "Generic Dermo",
        "ar": {
            "title": "كريم العناية بالبشرة المتهيجة والحساسة لترميم الحاجز الواقي - 100 مل",
            "meta_title": "كريم ترميم البشرة المتهيجة 100مل | صيدلية إكليل أبها",
            "meta_description": "اشتري كريم العناية بالبشرة المتهيجة والحساسة لترميم الحاجز الواقي (100مل). سيكا، بانثينول وسيراميد لتهدئة الاحمرار والحكة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["كريم_مهدئ", "ترميم_الحاجز", "سيكا_بانثينول", "بشرة_حساسة", "إكليل_أبها"]
        },
        "en": {
            "title": "Soothing Care Cream for Irritated Skin - 100ml",
            "meta_title": "Soothing Care Cream for Irritated Skin 100ml | Ekleel Abha",
            "meta_description": "Buy Soothing Care Cream for Irritated Skin (100ml). Barrier restoration with Cica, Panthenol, & Ceramides. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["soothing_cream", "barrier_repair", "cica_panthenol", "sensitive_skin", "ekleel_abha"]
        },
        "schema": {
            "brand": "Generic Dermo",
            "category": "Skincare / Soothing Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "soothing-care-cream-for-irritated-skin-100ml.webp",
            "alt": "Soothing Care Cream for Irritated Skin 100ml",
            "title": "Soothing Care Cream for Irritated Skin 100ml"
        }
    }

def create_product_1770():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم بالمرز لعلامات تمدد الجلد 125جم (Palmer's for Stretch Marks 125g)</strong> المستحضر الطبيعي الأسطوري ورقم 1 عالمياً للوقاية من علامات تمدد الجلد (Stretch Marks) وتحسين مرونة البشرة أثناء الحمل أو تغير الوزن. يرتكز هذا الكريم المكثف من بالمرز على تركيبة زبدة الكاكاو النقية (Cocoa Butter) وزبدة الشيا، والمعززة بالكولاجين، الإيلاستين، زيت الأرجان، وزيت اللوز الحلو، مما يمنح الجلد مرونة فائقة وتغذية عميقة تمنع تكسر ألياف الجلد.</p>
<p>يساعد كريم بالمرز في ترطيب البطن، الوركين، الفخذين، والصدر بكفاءة مثبتة سريرياً تحسن مرونة الجلد بنسبة تزيد عن 98%، وهو خالي تماماً من الزيوت المعدنية والبارابين لضمان آمان تام للأمهات والحوامل.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>الوقاية والحد من علامات التمدد:</strong> يمنع ويقلل ظهور خطوط التمدد أثناء الحمل وبعد الولادة أو تغير الوزن.</li>
  <li><strong>تركيبة زبدة الكاكاو وزبدة الشيا:</strong> تمنح ترطيباً عميقاً وطويلاً وتغلف الجلد بحجاب حماية مغذٍ.</li>
  <li><strong>مدعم بالكولاجين والإيلاستين:</strong> يعزز مرونة وقوة ألياف الجلد ويمنع تكسر الأنسجة أثناء التمدد.</li>
  <li><strong>غني بزيت الأرجان واللوز الحلو:</strong> يغذي الجلد بالأحماض الدهنية وفيتامين E ويمنع الجفاف والحكة.</li>
  <li><strong>خالي من البارابين والزيوت المعدنية:</strong> تركيبة آمنة تماماً ومجربة جلدياً للحوامل والأمهات.</li>
  <li><strong>عبوة مدمجة 125 جم:</strong> حجم ممتاز ومناسب للعناية اليومية المركزة بمناطق التمدد.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> استحممي وجففي بشرتكِ بلطف.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي كمية مناسبة من كريم بالمرز على مناطق البطن، الوركين، الفخذين، والصدر.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي بحركات دائرية خفيفة مرتين يومياً (صباحاً ومساءً) للحصول على أفضل مرونة.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زبدة الكاكاو النقية (Pure Cocoa Butter):</strong> تطري الجلد وتوفر ترطيباً مكثفاً.</li>
  <li><strong>الكولاجين والإيلاستين (Collagen & Elastin):</strong> يعززان صمود ومرونة أنسجة البشرة.</li>
  <li><strong>زيت الأرجان وزيت اللوز الحلو:</strong> يغذيان الجلد بالأحماض الدهنية وفيتامين E.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي فقط.</li>
  <li>تجنبي ملامسة الكريم المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>للحوامل والأمهات ولكل من تعاني من علامات تمدد الجلد الناتجة عن الحمل أو تغيرات الوزن.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بالمرز (Palmer's)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات وقاية وتخفيف علامات تمدد الجلد</td></tr>
  <tr><th>نوع المنتج</th><td>كريم المساج المركز لعلامات تمدد الجلد (Massage Cream for Stretch Marks)</td></tr>
  <tr><th>الحجم/الوزن</th><td>125 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (خاصة بشرة الحوامل والجافة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة، مرنة، مشدودة، وخالية من خطوط التمدد</td></tr>
  <tr><th>الملمس</th><td>كريمي كثيف يرطب بعمق دون أثر دهني لزج</td></tr>
  <tr><th>العطر</th><td>عطر الكاكاو الطبيعي الغني واللطيف</td></tr>
  <tr><th>المكونات النشطة</th><td>زبدة الكاكاو، زبدة الشيا، كولاجين، إيلاستين، زيت أرجان، فيتامين E</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة الأمريكية (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>E.T. Browne Drug Co. (بالمرز)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين (الحوامل والأمهات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زبدة الكاكاو والكولاجين للتمدد (Palmer's)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم بالمرز مشكلة ظهور علامات تمدد الجلد الحمراء والبيضاء، تكسر ألياف الكولاجين، وحكة بطن الحامل الناتجة عن التمدد السريع.</p>

<h3>لماذا يحدث تمدد الجلد؟</h3>
<p>يتسبب التمدد السريع أثناء الحمل أو تغير الوزن في تمزق ألياف الكولاجين والإيلاستين في أدمة الجلد، فيظهر التخطيط والحكة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>البدء المبكر بالحمل:</strong> استعملي كريم بالمرز من الأشهر الأولى للحمل لزيادة ليونة الجلد.<br>
2. <strong>التدليك مرتين يومياً:</strong> دلكي البطن والوركين والفخذين صباحاً ومساءً.<br>
3. <strong>شرب الماء:</strong> حافظي على شرب الماء لدعم ترطيب الجلد الداخلي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "علامات تمدد الجلد لا يمكن الوقاية منها أبداً."<br>
<strong>الحقيقة:</strong> دعم مرونة الجلد بالكولاجين وزبدة الكاكاو يمنع تكسر الألياف بنسبة تزيد عن 98%.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتغلغل الأحماض الدهنية بزبدة الكاكاو والشيا مع الكولاجين داخل الطبقة الوسطى (Dermis)، حيث تزيد مطاطية الأنسجة وتمنع تمزق ألياف الإيلاستين.</p>"""

    faqs = [
        ("ما هو كريم بالمرز لعلامات تمدد الجلد 125جم؟", "هو كريم مساج مكثف بزبدة الكاكاو والكولاجين والإيلاستين لتحسين مرونة الجلد والوقاية من علامات التمدد أثناء الحمل وتغير الوزن."),
        ("ما هي فوائد زبدة الكاكاو والكولاجين للجلد؟", "تطري زبدة الكاكاو الجلد وتغذيه، بينما يزيد الكولاجين والإيلاستين مرونة وقوة ألياف الجلد."),
        ("هل يمنع ظهور علامات تمدد جديدة أثناء الحمل؟", "نعم، مثبت سريرياً في تحسين مرونة الجلد بنسبة 98% والوقاية من التمدد."),
        ("ما حجم العبوة؟", "تأتي العبوة بحجم 125 جم."),
        ("متى يجب البدء باستخدامه أثناء الحمل؟", "يُفضل البدء باستخدامه من الأشهر الأولى للحمل وحتى بعد الولادة."),
        ("ما هي المناطق التي يُطبق عليها؟", "يطبق على البطن، الوركين، الفخذين، الصدر، والمناطق المعرضة للتمدد."),
        ("هل هو خالي من الزيوت المعدنية والبارابين؟", "نعم، خالي تماماً من البارابين والزيوت المعدنية ومناسب للحوامل."),
        ("ما هو بلد صنع كريم بالمرز؟", "صُنع بفخر في الولايات المتحدة الأمريكية (USA)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بالمرز لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("كم مرة يُنصح باستخدامه يومياً؟", "يُنصح بالتدليك مرتين يومياً (صباحاً ومساءً)."),
        ("هل يساعد في تقليل الحكة المصاحبة لتمدد البطن؟", "نعم، يرطب الجفاف ويهدئ الحكة الناتجة عن تمدد الجلد."),
        ("هل يناسب من يفقدون وزناً بالحمية أو الرياضة؟", "نعم، ممتازة جداً لمن يمارسون حمية أو رياضة لمنع ترهل وتمدد الجلد."),
        ("ما هي رائحة كريم بالمرز؟", "يتميز برائحة الكاكاو والشيا الطبيعية الزكية."),
        ("هل يترك أثراً لزجاً؟", "يمتصه الجلد بمرونة ويمنح ترطيباً طويلاً دون لزوجة قاسية."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل يساعد في تحسين مظهر الخطوط القديمة؟", "نعم، يساعد في تنعيم وتحسين مظهر علامات التمدد السابقة."),
        ("هل يناسب جميع أنواع البشرة؟", "نعم، مناسب للبشرة العادية، الجافة، والحساسة."),
        ("هل يمكن استخدامه أثناء الرضاعة؟", "نعم، آمن ويُراعى تجنب وضعه على حلمة الصدر قبل الرضاعة مباشرة."),
        ("هل العبوة 125 جم تكفي لفترة مناسبة؟", "نعم، تكفي لعدة أسابيع من الاستخدام اليومي المركّز."),
        ("هل يحتوي على زيت أرجان ولوز؟", "نعم، مدعم بزيت الأرجان وزيت اللوز الحلو لزيادة التغذية."),
        ("هل ينصح به أطباء النساء والتوليد؟", "نعم، بالمرز العلامة الأولى الموصى بها عالمياً للحوامل."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة دائرية بغطاء محكم للحفظ."),
        ("هل يمنع ترهل الجلد بعد الولادة؟", "نعم، تعزيز الإيلاستين يساعد في استعادة قوام الجلد بعد الولادة."),
        ("هل يسبب حساسية؟", "تركيبة مجربة جلدياً ومناسبة للبشرة الحساسة."),
        ("هل يمتص بسهولة؟", "يدلك بسهولة وينفذ داخل خلايا الجلد.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Palmer's for Stretch Marks 125g</strong> (Massage Cream for Stretch Marks) is the world's #1 dermatologist-recommended stretch mark prevention cream designed to boost skin elasticity during pregnancy or weight fluctuations. Formulated with pure Cocoa Butter, Shea Butter, Collagen, Elastin, Argan Oil, and Sweet Almond Oil, it feeds dermal cells to prevent fiber tears.</p>
<p>Clinically proven to improve skin elasticity in over 98% of test subjects, Palmer's Massage Cream deeply hydrates the tummy, hips, thighs, and bust while remaining 100% free of mineral oil, parabens, and phthalates for complete maternal safety.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Prevents & Reduces Stretch Marks:</strong> Clinically proven to minimize stretch marks during pregnancy or weight shifts.</li>
  <li><strong>Pure Cocoa & Shea Butter Formula:</strong> Delivers long-lasting deep hydration and seals moisture into skin layers.</li>
  <li><strong>Enriched with Collagen & Elastin:</strong> Fortifies dermal fiber flexibility to prevent structural tears during stretching.</li>
  <li><strong>Packed with Argan & Sweet Almond Oils:</strong> Feeds skin essential fatty acids and Vitamin E to stop dry itching.</li>
  <li><strong>Mineral Oil & Paraben Free:</strong> Hypoallergenic, dermatologist-tested formula safe for expecting mothers.</li>
  <li><strong>Concentrated 125g Jar:</strong> Ideal size for targeted daily massage on stretch-prone body areas.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Shower and gently pat skin dry.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a suitable amount of Palmer's Massage Cream onto tummy, hips, thighs, and bust.</li>
  <li><strong>Step 3 (Massage):</strong> Massage gently in circular motions twice daily (morning and evening) for maximum elasticity.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Cocoa Butter:</strong> Softens skin and provides deep moisture retention.</li>
  <li><strong>Collagen & Elastin:</strong> Boost skin suppleness, firmness, and tensile elasticity.</li>
  <li><strong>Argan Oil & Sweet Almond Oil:</strong> Supply essential fatty acids and Vitamin E to soothe skin.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Expecting mothers, post-partum moms, and individuals managing weight changes wanting to prevent stretch marks.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Palmer's</td></tr>
  <tr><th>Category</th><td>Skincare / Stretch Mark Prevention Creams</td></tr>
  <tr><th>Product Type</th><td>Concentrated Stretch Mark Massage Cream</td></tr>
  <tr><th>Volume/Weight</th><td>125 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Ideal for Pregnancy & Dry Skin)</td></tr>
  <tr><th>Finish</th><td>Soft, elastic, firm & stretch-mark-reduced skin</td></tr>
  <tr><th>Texture</th><td>Rich concentrated non-greasy cream</td></tr>
  <tr><th>Fragrance</th><td>Natural Cocoa & Shea aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Cocoa Butter, Shea Butter, Collagen, Elastin, Argan Oil</td></tr>
  <tr><th>Country of Origin</th><td>United States of America (USA)</td></tr>
  <tr><th>Manufacturer</th><td>E.T. Browne Drug Co. (Palmer's)</td></tr>
  <tr><th>Age Group</th><td>Adults (Mothers & Expecting Moms)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Cocoa Butter & Collagen Elasticity Support</h2>

<h3>What problem does this solve?</h3>
<p>Palmer's Massage Cream resolves stretch mark formation, collagen fiber tearing, and pregnancy belly itching.</p>

<h3>Why choose Palmer's?</h3>
<p>Pure Cocoa Butter fatty acids and Collagen molecules penetrate the dermal layer, increasing tissue elasticity by over 98% to resist stretching tears.</p>"""

    en_faqs = [
        ("What is Palmer's for Stretch Marks 125g?", "It is a concentrated Cocoa Butter massage cream enriched with Collagen and Elastin to improve skin elasticity and prevent stretch marks."),
        ("What are the benefits of Cocoa Butter and Collagen?", "Cocoa Butter deeply moisturizes skin, while Collagen and Elastin boost fiber strength and elasticity."),
        ("Does it prevent stretch marks during pregnancy?", "Yes, clinically proven to improve skin elasticity in over 98% of women."),
        ("What volume is contained in this jar?", "It comes in a concentrated 125g jar."),
        ("When should I start using it during pregnancy?", "Start using from the early months of pregnancy through post-partum recovery."),
        ("Where should I apply it?", "Apply onto tummy, hips, thighs, bust, and stretch-prone areas."),
        ("Is it mineral oil and paraben free?", "Yes, 100% free of mineral oil, parabens, and phthalates."),
        ("Where is Palmer's manufactured?", "It is proudly manufactured in the USA."),
        ("How do I verify authenticity at Ekleel Abha?", "All Palmer's products at Ekleel Abha are 100% original from certified distributors."),
        ("How many times daily should I apply it?", "Massage gently into target areas twice daily, morning and evening."),
        ("Does it relieve pregnancy belly itching?", "Yes, deep hydration calms tightness and stops itching."),
        ("Is it suitable for weight loss stretch marks?", "Yes, ideal for anyone experiencing weight fluctuations or fitness body changes."),
        ("What scent does it have?", "It features a rich, pleasant natural Cocoa scent."),
        ("Does it leave a greasy residue?", "It absorbs smoothly, leaving skin soft without heavy grease."),
        ("How should I store the jar?", "Store in a cool, dry place away from heat."),
        ("Does it improve old stretch marks?", "Yes, regular use softens and fades the appearance of existing stretch marks."),
        ("Is it suitable for all skin types?", "Yes, ideal for normal, dry, and sensitive skin."),
        ("Can it be used while breastfeeding?", "Yes, safe for nursing mothers; avoid applying directly on nipples before feeding."),
        ("Does the 125g jar last long?", "Yes, provides weeks of targeted daily application."),
        ("Does it contain Argan and Almond oils?", "Yes, enriched with Argan Oil and Sweet Almond Oil for added nutrition."),
        ("Is Palmer's OB/GYN recommended?", "Yes, Palmer's is the #1 recommended brand for stretch mark care."),
        ("Is the jar securely sealed?", "Yes, comes in a sturdy round jar with a screw lid."),
        ("Does it help restore post-partum skin firmness?", "Yes, Collagen and Elastin aid post-partum skin bounce-back."),
        ("Does it cause allergies?", "Dermatologically tested and hypoallergenic."),
        ("Does it absorb easily?", "Yes, massages in smoothly to nourish skin cells.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1770",
        "sku": "EK-1770",
        "gtin": "010181040764",
        "category": "العناية بالبشرة / كريمات وقاية وتخفيف علامات تمدد الجلد",
        "brand": "Palmer's",
        "ar": {
            "title": "بالمرز لعلامات تمدد الجلد 125جم",
            "meta_title": "كريم بالمرز لعلامات التمدد 125جم | صيدلية إكليل أبها",
            "meta_description": "اشتري كريم بالمرز لعلامات تمدد الجلد بزبدة الكاكاو والكولاجين (125جم). الوقاية من خطوط الحمل وتحسين المرونة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بالمرز", "علامات_التمدد", "زبدة_الكاكاو", "كريم_الحمل", "إكليل_أبها"]
        },
        "en": {
            "title": "Palmer's for Stretch Marks 125g",
            "meta_title": "Palmer's Massage Cream for Stretch Marks 125g | Ekleel Abha",
            "meta_description": "Buy original Palmer's Cocoa Butter Formula Massage Cream for Stretch Marks (125g). Boosts elasticity with Collagen & Elastin. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["palmers", "stretch_marks", "cocoa_butter", "pregnancy_cream", "ekleel_abha"]
        },
        "schema": {
            "brand": "Palmer's",
            "category": "Skincare / Stretch Mark Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "palmers-for-stretch-marks-125g.webp",
            "alt": "Palmer's for Stretch Marks 125g",
            "title": "Palmer's for Stretch Marks 125g"
        }
    }

def create_product_1773():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم شعر بزيت جوز الهند من بالمرز 250جم لترطيب وتصفيف الشعر الجاف والمجعد (Palmer's Coconut Oil Formula Hair Food Formula 250g)</strong> المغذي الفاخر والأساسي لإعادة الحيوية واللمعان الفائق للشعر الجاف والمجهد والكيرلي. يعتمد هذا المغذي الكريمي من بالمرز على تركيبة زيت جوز الهند البكر الخالص (Pure Coconut Oil) المعزز بزيت المونوي التاهيتي (Tahitian Monoi Oil) وفيتامين E، حيث يتغلغل في عمق ألياف الشعر ليمنحها ترطيباً مكثفاً وتغذية تمنع الهيشان والتكسر.</p>
<p>يمتاز كريم بالمرز بفورمولا غنية تلطف الفروة وتغلف خصلات الشعر بغلاف واقٍ يعيد إليها اللمعان والنعومة الكريستالية، مما يسهل تصفيف الشعر المجعد والخشين ويترك عبيراً استوائياً منعشاً يدوم طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتغذية مكثفة بزيت جوز الهند:</strong> يغذيات ألياف الشعر الجاف ويعوض الرطوبة المفقودة.</li>
  <li><strong>تنعيم وتصفيف الشعر المجعد (الكيرلي):</strong> يلين الخصلات القاسية، يسهل التمشيط، ويمنع الهيشان.</li>
  <li><strong>مدعم بزيت المونوي وفيتامين E:</strong> يرمم الأطراف التالفة والمتقصفة ويعزز لمعان الشعر.</li>
  <li><strong>حماية ضد التكسر والجفاف:</strong> يغلف الشعر بحجاب حماية ضد الإجهاد الحراري والطقس الجاف.</li>
  <li><strong>تغذية الفروة ومنع القشرة الجافة:</strong> يهدئ جفاف الفروة ويرطب الجذور.</li>
  <li><strong>عبوة وافرة 250 جم:</strong> حجم كبير يضمن عناية مستمرة وممتدة لأشهر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> وضعي الكريم على شعر نظيف ورطب خفيفاً أو جاف.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي كمية بحجم حبة الجوز من كريم بالمرز بجوز الهند على كف اليد.</li>
  <li><strong>الخطوة الثالثة (التوزيع والتصفيف):</strong> وزعي الكريم من المنتصف وحتى الأطراف وفروة الرأس، ومشطي شعركِ بالأسلوب المفضل.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت جوز الهند النقي 100% (Coconut Oil):</strong> يمتص بسرعة ليغذي ألياف الشعر الداخلية.</li>
  <li><strong>زيت المونوي التاهيتي (Monoi Oil):</strong> ينعم خصلات الشعر ويمنحها بريقاً استوائياً.</li>
  <li><strong>فيتامين E (Tocopheryl Acetate):</strong> يقوي بصلات الشعر ويمنع أكسدة التلف.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الشعر وفروة الرأس فقط.</li>
  <li>تجنبي ملامسة كريم الشعر المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من الشعر الجاف، المجعد، الباهت، أو المتقصف وترغب في كريم مغذٍ ومصفف بزيت جوز الهند.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بالمرز (Palmer's)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / كريمات ومغذيات الشعر الجاف</td></tr>
  <tr><th>نوع المنتج</th><td>كريم مغذٍ ومصفف للشعر بزيت جوز الهند (Hair Food Formula)</td></tr>
  <tr><th>الحجم/الوزن</th><td>250 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>الشعر الجاف، المجعد، الباهت، والتالف</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم، حريري، لامع ببريق صحي وبدون هيشان</td></tr>
  <tr><th>الملمس</th><td>كريمي غني ومغرم بالزيوت الطبيعية</td></tr>
  <tr><th>العطر</th><td>عطر جوز الهند والمونوي الاستوائي الزكي</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت جوز الهند النقي، زيت المونوي، فيتامين E، لانولين</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة الأمريكية (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>E.T. Browne Drug Co. (بالمرز)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 6 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت جوز الهند ومغذيات الشعر (Palmer's Hair Food)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم بالمرز بجوز الهند مشكلة جفاف الشعر الشديد، هيشان الكيرلي، تقصف الأطراف، وشحوب البريق الطبيعي.</p>

<h3>لماذا يفضل زيت جوز الهند للشعر؟</h3>
<p>لأن حمض اللوريك الموجود بزيت جوز الهند يمتلك وزناً جزيئياً ينفذ داخل قشرة الشعرة لترميم البروتينات المفقودة بعكس الزيوت السطحية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التصفيف بكمية مناسبة:</strong> افركي كمية بحجم حبة الجوز بين الكفين ووزعيها على الشعر.<br>
2. <strong>العناية بالأطراف المتقصفة:</strong> ركزي الكريم على الأطراف الجافة لحمايتها من التكسر.<br>
3. <strong>الاستخدام كحمام كريم:</strong> وضعي كمية وافرة ولفي الشعر بفوطة دافئة كحمام زيت مغذٍ.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريم الشعر بجوز الهند يجعل الشعر لزجاً وثقيلاً."<br>
<strong>الحقيقة:</strong> فورمولا بالمرز تذوب بمرونة وتمتصها ألياف الشعر لتعطي ملمساً حريرياً دون لزوجة قاسية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخترق الأحماض الدهنية بزيت جوز الهند والمونوي طبقة الكيراتين القشرية، حيث ترطب ألياف الشعر الداخلية وتغلف السطح بحجاب يعكس الضوء لمنع الهيشان.</p>"""

    faqs = [
        ("ما هو كريم شعر بزيت جوز الهند من بالمرز 250جم؟", "هو كريم مغذٍ ومصفف مكثف غني بزيت جوز الهند والمونوي وفيتامين E لترطيب وتسهيل تصفيف الشعر الجاف والمجعد."),
        ("ما هي فوائد زيت جوز الهند والمونوي للشعر؟", "يغذي زيت جوز الهند قشرة الشعرة لترميم البروتينات، بينما يمنح زيت المونوي نعومة وبريقاً استوائياً."),
        ("هل يمنع هيشان وتقصف الشعر الجاف؟", "نعم، يغلف الخصلات بغلاف واقٍ يمنع الهيشان ويعالج الأطراف المتقصفة."),
        ("ما حجم العبوة؟", "تأتي العبوة بحجم كبير يبلغ 250 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي كمية مناسبة من الكريم على شعر رطب أو جاف من المنتصف حتى الأطراف ثم صففي بمرونة."),
        ("هل يناسب الشعر الكيرلي والمجعد؟", "ممتاز جداً للشعر المجعد والكيرلي لتحديد التموجات وتليين القسوة."),
        ("ما هو بلد صنع كريم بالمرز للشعر؟", "صُنع بفخر في الولايات المتحدة الأمريكية (USA)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بالمرز لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يغذي فروة الرأس الجافة؟", "نعم، تدليكه على الفروة يرطب الجفاف ويقلل القشرة الجافة."),
        ("ما هي رائحة كريم بالمرز؟", "يتميز برائحة جوز الهند والمونوي الاستوائية الفواحة."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب لتصفيف شعر وتغذية لحية الرجال وشعر النساء."),
        ("هل يثقل الشعر؟", "يُفضل استخدام كمية متوازنة لعدم إثقال الشعر الخفيف جداً."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل يناسب الأطفال؟", "مناسب للأطفال والبالغين من سن 6 سنوات فما فوق."),
        ("هل يساعد في حماية الشعر من حرارة السيشوار؟", "نعم، يوفر ترطيباً يحمي الشعر من الإجهاد الحراري."),
        ("هل العبوة 250 جم اقتصادية؟", "نعم، توفر عناية وتصفيفاً مستمراً لأشهر طويلة."),
        ("هل يترك بريقاً لامعاً؟", "نعم، يمنح الشعر بريقاً كريستالياً ومظهراً صحياً."),
        ("هل يمكن استخدامه يومياً؟", "نعم، آمن وممتاز للاستخدام والتصفيف اليومي."),
        ("هل يساعد في تسهيل التمشيط؟", "نعم، يفك التشابك ويسهل مرور المشط بسلاسة."),
        ("هل يعالج الشعر المصبوغ والتالف؟", "نعم، يعوض الشعر المصبوغ عن الزيوت المفقودة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة دائرية متينة بغطاء لولبي."),
        ("هل يحتوي على فيتامين E؟", "نعم، مدعم بفيتامين E لتقوية الشعر من الجذور."),
        ("هل يمكن استخدامه كحمام زيت مكثف؟", "يمكن وضع كمية وافرة ولف الشعر بفوطة دافئة كحمام كريم مغذٍ."),
        ("هل يمنع تكسر الشعر عند التصفيف؟", "نعم، ليونة الخصلات تمنع تكسرها أثناء التمشيط."),
        ("هل يمنح حس تصفيف طبيعي؟", "نعم، يعطي مظهر شعر ناعم ومشرق وطبيعي.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Palmer's Coconut Oil Formula Hair Food Formula 250g</strong> is a rich, intensive conditioning pomade engineered to restore moisture, softness, and brilliant shine to dry, coarse, or curly hair textures. Infused with raw, natural Virgin Coconut Oil, Tahitian Monoi Oil, and Vitamin E, it deeply penetrates hair shafts to replenish lost nutrients and prevent frizz and breakage.</p>
<p>Palmer's Hair Food coats strands with a protective barrier, restoring crystal softness and manageable shine to frizzy or unmanageable hair while leaving a delightful tropical coconut scent throughout the day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intensive Coconut Oil Moisture:</strong> Feeds dry hair fibers and restores natural moisture balance.</li>
  <li><strong>Smooths & Styles Frizzy/Curly Hair:</strong> Softens coarse strands, eases combing, and defines curls.</li>
  <li><strong>Enriched with Monoi Oil & Vitamin E:</strong> Repairs split ends and enhances natural hair shine.</li>
  <li><strong>Breakage & Heat Protection:</strong> Shields hair shafts from thermal styling stress and weather dryness.</li>
  <li><strong>Nourishes Dry Scalp:</strong> Soothes scalp tightness and hydrates dry roots.</li>
  <li><strong>Generous 250g Tub:</strong> Excellent value tub providing months of continuous hair care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Prepare):</strong> Apply to clean, slightly damp or dry hair.</li>
  <li><strong>Step 2 (Apply):</strong> Rub a walnut-sized amount of Palmer's Hair Food between palms.</li>
  <li><strong>Step 3 (Style):</strong> Smooth through hair from mid-lengths to ends and scalp; style as desired.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>100% Pure Virgin Coconut Oil:</strong> Absorbs into the hair cortex to restore structural proteins.</li>
  <li><strong>Tahitian Monoi Oil:</strong> Softens hair strands and adds a brilliant tropical gloss.</li>
  <li><strong>Vitamin E (Tocopheryl Acetate):</strong> Fortifies hair roots and shields against oxidative stress.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external hair and scalp application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dry, frizzy, coarse, or split-end-prone hair looking for a rich Coconut Oil conditioning pomade.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Palmer's</td></tr>
  <tr><th>Category</th><td>Hair Care / Hair Dressings & Conditioners</td></tr>
  <tr><th>Product Type</th><td>Nourishing Coconut Oil Hair Food Pomade</td></tr>
  <tr><th>Volume/Weight</th><td>250 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Dry, Frizzy, Coarse & Damaged Hair</td></tr>
  <tr><th>Finish</th><td>Soft, shiny, manageable, frizz-free hair</td></tr>
  <tr><th>Texture</th><td>Rich oil-infused pomade cream</td></tr>
  <tr><th>Fragrance</th><td>Tropical Coconut & Monoi Oil aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Virgin Coconut Oil, Monoi Oil, Vitamin E, Lanolin</td></tr>
  <tr><th>Country of Origin</th><td>United States of America (USA)</td></tr>
  <tr><th>Manufacturer</th><td>E.T. Browne Drug Co. (Palmer's)</td></tr>
  <tr><th>Age Group</th><td>All Ages (6+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Lauric Acid & Cortical Hair Conditioning</h2>

<h3>What problem does this solve?</h3>
<p>Palmer's Coconut Hair Food resolves severe hair dryness, coarse frizz, split ends, and dullness.</p>

<h3>Why choose Coconut Oil?</h3>
<p>Lauric acid in Virgin Coconut Oil possesses a molecular structure that penetrates deep into the hair cortex to prevent protein loss.</p>"""

    en_faqs = [
        ("What is Palmer's Coconut Oil Formula Hair Food 250g?", "It is an intensive conditioning pomade rich in Virgin Coconut Oil, Monoi Oil, and Vitamin E to moisturize and style dry, frizzy hair."),
        ("What are the benefits of Coconut Oil and Monoi Oil?", "Coconut Oil penetrates the hair cortex to restore proteins, while Monoi Oil softens strands and adds gloss."),
        ("Does it prevent frizz and split ends?", "Yes, it coats strands to lock out humidity, prevent frizz, and smooth split ends."),
        ("What volume is contained in this tub?", "It comes in a generous 250g tub."),
        ("How do I apply it correctly?", "Rub a small amount between palms and smooth through damp or dry hair from mid-lengths to ends."),
        ("Is it suitable for curly and coarse hair?", "Yes, excellent for taming coarse hair and defining natural curls."),
        ("Where is Palmer's manufactured?", "It is proudly manufactured in the USA."),
        ("How do I verify authenticity at Ekleel Abha?", "All Palmer's products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it condition dry scalps?", "Yes, massaging a small amount into the scalp hydrates dry roots."),
        ("What scent does it have?", "It features a delightful tropical Coconut and Monoi fragrance."),
        ("Can both men and women use it?", "Yes, suitable for styling men's hair and beards as well as women's hair."),
        ("Will it weigh down fine hair?", "Use sparingly on fine hair to avoid weighing down styles."),
        ("How should I store the tub?", "Store in a cool, dry place away from heat."),
        ("Is it safe for children?", "Safe for adults and kids aged 6+."),
        ("Does it protect against heat styling?", "Yes, it provides a protective moisture barrier against thermal stress."),
        ("Is the 250g tub economical?", "Yes, a single tub provides months of regular usage."),
        ("Does it impart brilliant shine?", "Yes, it gives hair a healthy, glossy crystal finish."),
        ("Can it be used daily?", "Yes, safe for daily styling and conditioning."),
        ("Does it ease detangling?", "Yes, it softens strands so combs glide through smoothly."),
        ("Is it suitable for color-treated hair?", "Yes, it replenishes moisture stripped during color processing."),
        ("Is the tub securely sealed?", "Yes, comes in a sturdy round tub with a screw lid."),
        ("Does it contain Vitamin E?", "Yes, enriched with Vitamin E to strengthen hair roots."),
        ("Can it be used as a deep mask treatment?", "Yes, apply generously and wrap with a warm towel for an intensive mask treatment."),
        ("Does it prevent comb breakage?", "Yes, strand lubricity prevents friction breakage during combing."),
        ("Does it provide a natural finish?", "Yes, leaves hair touchably soft and naturally radiant.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1773",
        "sku": "EK-1773",
        "gtin": "010181023705",
        "category": "العناية بالشعر / كريمات ومغذيات الشعر الجاف",
        "brand": "Palmer's",
        "ar": {
            "title": "كريم شعر بزيت جوز الهند من بالمرز 250جم لترطيب وتصفيف الشعر الجاف والمجعد",
            "meta_title": "كريم شعر بالمرز بجوز الهند 250جم | صيدلية إكليل أبها",
            "meta_description": "اشتري كريم شعر بزيت جوز الهند من بالمرز لترطيب وتصفيف الشعر الجاف والمجعد (250جم). فورمولا بزيت المونوي وفيتامين E. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بالمرز", "كريم_جوز_الهند", "ترطيب_الشعر", "تصفيف_الكيرلي", "إكليل_أبها"]
        },
        "en": {
            "title": "Palmer's Coconut Oil Formula Hair Food Formula 250g",
            "meta_title": "Palmer's Coconut Oil Hair Food 250g | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Palmer's Coconut Oil Formula Hair Food Formula (250g). Deep conditioning & styling for dry, frizzy hair. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["palmers", "coconut_hair_food", "hair_conditioning", "frizz_control", "ekleel_abha"]
        },
        "schema": {
            "brand": "Palmer's",
            "category": "Hair Care / Hair Food",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "palmers-coconut-oil-formula-hair-food-formula-250g.webp",
            "alt": "Palmer's Coconut Oil Formula Hair Food Formula 250g",
            "title": "Palmer's Coconut Oil Formula Hair Food Formula 250g"
        }
    }

def create_product_1774():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>مجموعة شامبو وبلسم ميلانو كيراتين ثيرابي من الفا بارف - 2 × 250 مل (Alfaparf Milano Keratin Therapy Shampoo & Conditioner Set, 250ml Each)</strong> الثنائي العلاجي الأنسب والأرقى عالمياً للحفاظ على نتائج جلسات الفرد بالكيراتين والبروتين واستعادة النعومة الحريرية للشعر. يعتمد هذا الطقم الإيطالي من الفا بارف على تقنية مركب الكيراتين المتقدم (Kera-Collagen Complex) المغذى بزيت الباباسو الاستوائي (Babassu Oil)، مما يمنح الشعر تنظيفاً وبلسمة فائقة النعومة خالية تماماً من السلفات والبارابين والأملاح الضارة (Sulfate & Salt Free).</p>
<p>يعمل الشامبو والبلسم على تغذية ألياف الشعر، إعادة بناء الروابط البروتينية، وفك التشابك بسهولة مذهلة، ليترك شعركِ أملس، حريرياً، ومشرقاً ببريق هوليوودي يدوم طويلاً بعد كل غسلة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>طقم علاج متكامل للشعر المعالج بالكيراتين:</strong> يحافظ على نتائج جلسات الفرد والبروتين لأطول مدة.</li>
  <li><strong>خالي تماماً من السلفات والبارابين والأملاح (Sulfate & Salt Free):</strong> يحمي غلاف الكيراتين من التحلل والغسيل القاسي.</li>
  <li><strong>مركب الكيراتين والكولاجين (Kera-Collagen Complex):</strong> يعيد ترميم ألياف الشعر المتضررة ويقوي الجذور.</li>
  <li><strong>مدعم بزيت الباباسو الاستوائي:</strong> يمنح الشعر لمعاناً كراستالياً ونعومة مخملية فائقة.</li>
  <li><strong>فك التشابك وتسهيل التصفيف:</strong> يلين الخصلات القاسية والمجعدة ويمنع الهيشان.</li>
  <li><strong>عبوة مزدوجة 2 × 250 مل:</strong> طقم احترافي إيطالي للشامبو والبلسم بعناية صالونات منزلية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الشامبو):</strong> وضعي كمية منا سبة من شامبو الكيراتين على الشعر المبلل، دلكي الفروة والخصلات برفق، ثم اشطفي بالماء الفاتر.</li>
  <li><strong>الخطوة الثانية (البلسم):</strong> وضعي بلسم الكيراتين من منتصف الشعر وحتى الأطراف، اتركيه لمدة 2 إلى 3 دقائق، ثم اشطفي جيداً بالماء.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركب الكيرا كولاجين (Kera-Collagen Complex):</strong> يرمم ألياف الشعر ويعوض الكيراتين المفقود.</li>
  <li><strong>زيت الباباسو (Babassu Oil):</strong> ينعم الشعر ويمنحه بريقاً حريرياً دون ثقل.</li>
  <li><strong>فورمولا خالية من الأملاح والسلفات:</strong> آمنة 100% للشعر المعالج كيميائياً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الشعر فقط.</li>
  <li>تجنبي ملامسة الشامبو أو البلسم المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من أجرت فرد كيراتين أو بروتين أو تعاني من الشعر الجاف والمجهد وترغب في طقم إيطالي خالي من السلفات.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>الفا بارف ميلانو (Alfaparf Milano)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / مجموعات الشامبو والبلسم العلاجية</td></tr>
  <tr><th>نوع المنتج</th><td>طقم شامبو وبلسم الكيراتين الخالي من السلفات (2 × 250ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>عبوتان 250 مل شامبو + 250 مل بلسم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>الشعر المعالج بالكيراتين والبروتين والشعر الجاف</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر أملس، حريري، لامع وخالٍ من الهيشان والتشابك</td></tr>
  <tr><th>الملمس</th><td>سائل شامبو رغوي مع بلسم كريمي غني</td></tr>
  <tr><th>العطر</th><td>عطر الزهور والباباسو الإيطالي الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>كيرا كولاجين، زيت الباباسو، خالي من السلفات والملح</td></tr>
  <tr><th>بلد المنشأ</th><td>إيطاليا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Alfaparf Group Italy</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد طقم الكيراتين الخالي من السلفات (Alfaparf Milano)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج طقم الفا بارف كيراتين مشكلة التحلل السريع لجلسات الفرد والهيشان والجفاف الناجم عن غسيل الشامبوهات العادية المحتوية على السلفات والملح.</p>

<h3>لماذا تنجح تركيبة الفا بارف؟</h3>
<p>لأنها خالية تماماً من السلفات والأملاح، وتزود الشعر بـ الكيرا كولاجين وزيت الباباسو الذي يحافظ على استقامة ومرونة الشعر المعالج.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام الشامبو ثم البلسم:</strong> اغسلي بشامبو الكيراتين ثم وضعي البلسم 2-3 دقائق لشطف ناعم.<br>
2. <strong>تجنب الغسيل الشديد:</strong> اغسلي الشعر 2-3 مرات أسبوعياً لحفظ زيوت الفرد.<br>
3. <strong>التجفيف بالسيشوار الدافئ:</strong> جففي بالسيشوار الدافئ لتأكيد استقامة ألياف الكيراتين.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الشامبو الخالي من السلفات لا ينظف الشعر جيداً."<br>
<strong>الحقيقة:</strong> شامبو الفا بارف ينظف الفروة بلطف ورغوة كريمية غنية دون تجريد الشعر من غلاف الكيراتين.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يتحد مركب الكيرا كولاجين (Kera-Collagen Complex) مع الروابط البروتينية الداخلية بالشعرة، بينما يغلف زيت الباباسو السطح الخارجي بحجاب حريري يحافظ على ملس الاستقامة.</p>"""

    faqs = [
        ("ما هي مجموعة شامبو وبلسم ميلانو كيراتين ثيرابي من الفا بارف؟", "هي طقم إيطالي علاج يحتوي على شامبو وبلسم سعة 250 مل لكل منهما، خالي من السلفات والملح لتدعيم الشعر المعالج بالكيراتين."),
        ("هل الطقم خالي من السلفات والبارابين والأملاح؟", "نعم، خالي تماماً من السلفات والبارابين والملح (Sulfate & Salt Free) لحماية الكيراتين."),
        ("ما هي فوائد مركب الكيرا كولاجين وزيت الباباسو؟", "يعيد الكيرا كولاجين بناء ألياف الشعر، بينما يمنح زيت الباباسو لمعاناً حريرياً ونعومة فائقة."),
        ("ما حجم العبوات في الطقم؟", "يحتوي الطقم على عبوتين بحجم 250 مل لكل عبوة (250 مل شامبو + 250 مل بلسم)."),
        ("هل يطيل عمر جلسات فرد الكيراتين والبروتين؟", "نعم، مصمم خصيصاً للحفاظ على نتائج الكيراتين والبروتين لأطول مدة ممكنة."),
        ("كيف يُستخدم الشامبو والبلسم بالشكل الصحيح؟", "اغسلي بشامبو الكيراتين واشطفي، ثم ضعي البلسم لـ 2-3 دقائق من المنتصف للأطراف واشطفي جيداً."),
        ("ما هو بلد صنع طقم الفا بارف؟", "صُنع بفخر في إيطاليا بواسطة الفا بارف ميلانو (Alfaparf Milano)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات الفا بارف لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يناسب الشعر المسبوغ والتالف؟", "نعم، ممتاز جداً لحماية وتنعيم الشعر المسبوغ والمجهد كيميائياً."),
        ("ما هي رائحة الشامبو والبلسم؟", "يتميز برائحة إيطالية استوائية فاخرة بفضل زيت الباباسو."),
        ("هل يساعد في فك تشابك الشعر المجهد؟", "نعم، البلسم يسهل تمشيط الشعر وفك التشابك فورياً."),
        ("هل يرغي الشامبو رغم خلوه من السلفات؟", "نعم، يولد رغوة كريمية لطيفة تنظف الفروة بعناية."),
        ("كيف أحتفظ بالطقم؟", "يُحفظ في مكان بارد وجاف داخل الحمام."),
        ("هل يناسب جميع أنواع الشعر؟", "مناسب جداً للشعر المعالج، الجاف، المفرود، والمجهد."),
        ("هل يناسب الاستخدام اليومي؟", "نعم، آمن وممتاز للاستخدام اليومي والمنتظم."),
        ("هل يترك ملمساً زيتيّاً ثقيلاً؟", "لا، يمتصه الشعر بمرونة ليترك خصلات أملس وحريرية دون ثقل."),
        ("هل يعيد حيوية أطراف الشعر المتقصفة؟", "نعم، الكولاجين وزيت الباباسو يرممان الأطراف المتضررة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوتين متينتين بغطاء محكم يمنع التسرب."),
        ("هل يمنع هيشان الشعر في الرطوبة؟", "نعم، يغلف الشعرة ويمنع الهيشان الناجم عن الرطوبة."),
        ("هل تناسب الرجال والنساء؟", "نعم، مناسب لكلا الجنسين."),
        ("هل العبوة المزدوجة اقتصادية؟", "نعم، توفر عناية صالونات إيطالية كاملة بسعر مميز."),
        ("هل يسبب تساقط الشعر؟", "خلوه من الكيماويات القاسية يحمي الفروة والروابط من التساقط."),
        ("كم مدة ترك البلسم على الشعر؟", "يُترك من 2 إلى 3 دقائق للحصول على نتائج ممتازة."),
        ("هل يمنح بريقاً كراستالياً؟", "نعم، زيت الباباسو يمنح بريقاً كريستالياً لافتاً."),
        ("هل هو خيار أطباء التجميل والمصففين؟", "نعم، العلامة الأولى المعتمدة لدى صالونات التجميل العالمية.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>[{a}]</p>\n".replace('[','').replace(']','') for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Alfaparf Milano Keratin Therapy Shampoo and Conditioner Set (250ml Each)</strong> is the ultimate Italian professional salon care duo engineered to prolong the results of keratin and protein smoothing treatments. Free from sulfates, parabens, and harsh salts (Sulfate & Salt Free), this high-performance system combines the Kera-Collagen Complex with exotic Amazonian Babassu Oil.</p>
<p>Together, the shampoo and conditioner gently cleanse, repair damaged hair fibers, detangle coarse strands, and leave your hair touchably silky, smooth, and radiant after every wash.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Prolongs Keratin & Smoothing Treatments:</strong> Keeps hair smooth, straight, and frizz-free for months.</li>
  <li><strong>100% Sulfate & Salt Free Formula:</strong> Protects keratin bonds from washing away or degrading.</li>
  <li><strong>Kera-Collagen Complex:</strong> Restructures damaged hair fibers and fortifies hair roots.</li>
  <li><strong>Infused with Babassu Oil:</strong> Imparts intense silkiness, hydration, and crystal gloss to hair.</li>
  <li><strong>Effortless Detangling & Frizz Control:</strong> Softens coarse texture and prevents humidity frizz.</li>
  <li><strong>Dual 2 x 250ml Salon Set:</strong> Includes 250ml Maintenance Shampoo and 250ml Maintenance Conditioner.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Shampoo):</strong> Apply Alfaparf Keratin Shampoo to wet hair, massage gently into scalp and strands, then rinse with warm water.</li>
  <li><strong>Step 2 (Conditioner):</strong> Apply Alfaparf Keratin Conditioner through mid-lengths to ends, leave on for 2 to 3 minutes, then rinse thoroughly.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Kera-Collagen Complex:</strong> Hydrolyzed Keratin and Collagen complex restructuring internal hair bonds.</li>
  <li><strong>Babassu Oil:</strong> Precious Amazonian oil providing intense silkiness and shine without weight.</li>
  <li><strong>Sulfate & Salt-Free Cleansing Base:</strong> 100% safe for chemically smoothed hair.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external hair application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with keratin, protein, or chemically straightened hair wanting a premium Italian sulfate-free maintenance set.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Alfaparf Milano</td></tr>
  <tr><th>Category</th><td>Hair Care / Shampoo & Conditioner Sets</td></tr>
  <tr><th>Product Type</th><td>Sulfate & Salt Free Keratin Therapy Shampoo & Conditioner Set</td></tr>
  <tr><th>Volume/Weight</th><td>Twin Pack (250ml Shampoo + 250ml Conditioner)</td></tr>
  <tr><th>Skin/Hair Type</th><td>Keratin-Treated, Straightened, Dry & Damaged Hair</td></tr>
  <tr><th>Finish</th><td>Silky, smooth, glossy & frizz-free hair</td></tr>
  <tr><th>Texture</th><td>Creamy fluid shampoo & rich velvet conditioner</td></tr>
  <tr><th>Fragrance</th><td>Luxurious Italian Babassu floral aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Kera-Collagen Complex, Babassu Oil, Sulfate-Free Base</td></tr>
  <tr><th>Country of Origin</th><td>Italy</td></tr>
  <tr><th>Manufacturer</th><td>Alfaparf Group Italy</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Kera-Collagen & Sulfate-Free Hair Maintenance</h2>

<h3>What problem does this solve?</h3>
<p>Alfaparf Milano Keratin Therapy Set resolves rapid keratin wash-out, frizz, and dry damage caused by harsh sulfate shampoos.</p>

<h3>Why choose Alfaparf Milano?</h3>
<p>Sulfate-free cleansing preserves Keratin bonds, while Kera-Collagen and Babassu Oil lock in moisture and mirror shine.</p>"""

    en_faqs = [
        ("What is Alfaparf Milano Keratin Therapy Set?", "It is an Italian salon duo containing 250ml Keratin Maintenance Shampoo and 250ml Conditioner, free from sulfates and salts."),
        ("Is it 100% sulfate and salt free?", "Yes, it is completely free from sulfates, parabens, and salts (Sulfate & Salt Free)."),
        ("What are the benefits of Kera-Collagen and Babassu Oil?", "Kera-Collagen restructures hair fibers, while Babassu Oil infuses brilliant shine and softness."),
        ("What volume is contained in this set?", "It includes two 250ml bottles (250ml Shampoo + 250ml Conditioner)."),
        ("Does it prolong keratin and protein straightening treatments?", "Yes, it is specially formulated to maintain keratin and protein smoothing results for months."),
        ("How do I use the shampoo and conditioner set?", "Apply shampoo to wet hair and rinse; then apply conditioner for 2-3 minutes before rinsing."),
        ("Where is Alfaparf Milano manufactured?", "It is proudly manufactured in Italy by Alfaparf Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All Alfaparf products at Ekleel Abha are 100% original from certified distributors."),
        ("Is it suitable for color-treated and dry hair?", "Yes, excellent for chemically treated, color-treated, and damaged hair."),
        ("What fragrance does the set have?", "It features a luxurious Italian Babassu floral scent."),
        ("Does it help detangle knotty hair?", "Yes, the conditioner eases combing and detangles hair immediately."),
        ("Does the shampoo lather well despite being sulfate-free?", "Yes, it creates a rich creamy lather that cleanses gently."),
        ("How should I store the set?", "Store in a cool, dry place inside your shower area."),
        ("Is it suitable for daily use?", "Yes, safe and ideal for daily maintenance."),
        ("Does it leave a heavy greasy residue?", "No, it absorbs smoothly leaving hair silky and light."),
        ("Does it repair split ends?", "Yes, Collagen and Babassu Oil seal and repair damaged ends."),
        ("Are the bottles securely sealed?", "Yes, comes in sturdy Italian bottles with leak-proof caps."),
        ("Does it protect against humidity frizz?", "Yes, it seals hair cuticles against humidity frizz."),
        ("Can both men and women use it?", "Yes, suitable for both men and women."),
        ("Is the dual pack economical?", "Yes, provides complete salon-grade Italian care at great value."),
        ("Does it prevent hair fall?", "Gentle sulfate-free cleansing protects hair roots from friction breakage."),
        ("How long should the conditioner stay on hair?", "Leave on for 2 to 3 minutes for optimal absorption."),
        ("Does it add crystal shine?", "Yes, Babassu Oil imparts a high-gloss crystal finish."),
        ("Is it stylist-recommended?", "Yes, Alfaparf Milano is a top choice among professional hair stylists globally."),
        ("Is it safe for sensitive scalps?", "Yes, sulfate-free formula is gentle on sensitive scalps.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1774",
        "sku": "EK-1774",
        "gtin": "8021357997111",
        "category": "العناية بالشعر / مجموعات الشامبو والبلسم العلاجية",
        "brand": "Alfaparf Milano",
        "ar": {
            "title": "مجموعة شامبو وبلسم ميلانو كيراتين ثيرابي من الفا بارف - 2 × 250 مل",
            "meta_title": "مجموعة شامبو وبلسم الفا بارف كيراتين 2x250مل | صيدلية إكليل أبها",
            "meta_description": "اشتري مجموعة شامبو وبلسم ميلانو كيراتين ثيرابي من الفا بارف (2 × 250 مل). خالي من السلفات والملح لتثبيت الكيراتين. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["الفا_بارف", "كيراتين_ثيرابي", "شامبو_خالي_سلفات", "علاج_الكيراتين", "إكليل_أبها"]
        },
        "en": {
            "title": "Alfaparf Milano Keratin Therapy Shampoo and Conditioner Set, 250ml Each",
            "meta_title": "Alfaparf Milano Keratin Therapy Set 2x250ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Alfaparf Milano Keratin Therapy Shampoo & Conditioner Set (250ml Each). Sulfate & Salt Free formula. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["alfaparf_milano", "keratin_therapy", "sulfate_free", "hair_set", "ekleel_abha"]
        },
        "schema": {
            "brand": "Alfaparf Milano",
            "category": "Hair Care / Hair Care Set",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "alfaparf-milano-keratin-therapy-shampoo-and-conditioner-set-250ml-each.webp",
            "alt": "Alfaparf Milano Keratin Therapy Shampoo and Conditioner Set 250ml Each",
            "title": "Alfaparf Milano Keratin Therapy Shampoo and Conditioner Set 250ml Each"
        }
    }

def create_product_1776():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>شامبو دوڤ قوة الأفوكادو، 200مل (Dove Avocado Strength Shampoo, 200ml)</strong> المستحضر المغذي الفاخر المصمم لإعادة القوة واللمعان والاستعادة الفائقة للشعر الضعيف والمجهد. يعتمد هذا الشامبو المتطور من دوڤ على مستخلص الأفوكادو الطبيعي وخلاصة إكليل الجبل المغذية، حيث ينظف الفروة وألياف الشعر بفاعلية ولطف، ويغذي البصيلات من الجذور حتى الأطراف لتقليل تساقط الشعر الناتج عن التكسر.</p>
<p>يمتاز شامبو دوڤ الأفوكادو برغوة الغنية والناعمة التي تعيد الحيوية للخصلات الضعيفة، وتمنح شعركِ ملمساً أملساً ورائحة استوائية منعشة تدوم طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تقوية الشعر الضعيف ومنع التكسر:</strong> ينظف ويغذي ألياف الشعر لتقليل التساقط والتكسر.</li>
  <li><strong>مدعم بخلاصة الأفوكادو وإكليل الجبل:</strong> يزود البصيلات بالفيتامينات المغذية والترطيب الطبيعي.</li>
  <li><strong>تنظيف لطيف ورغوة غنية:</strong> ينظف فروة الرأس بفاعلية دون تجفيف ألياف الشعر.</li>
  <li><strong>لمعان ونعومة كريستالية:</strong> يترك الشعر ناعماً، حريراً، ومشرقاً ببريق صحي.</li>
  <li><strong>تركيبة متوازنة للاستخدام اليومي:</strong> مجربة جلدياً وتناسب جميع أنواع الشعر الضعيف والمجهد.</li>
  <li><strong>عبوة مدمجة 200 مل:</strong> حجم ممتاز ومناسب للاستخدام الفردي وللسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل):</strong> بلي شعركِ بالماء الفاتر جيداً.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي كمية مناسبة من شامبو دوڤ الأفوكادو على كف اليد ودلكي الفروة بحركات دائرية.</li>
  <li><strong>الخطوة الثالثة (الشطف):</strong> اشطفي الشعر جيداً بالماء الفاتر، وكرري العملية عند الحاجة.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة ثمار الأفوكادو (Avocado Fruit Extract):</strong> غنية بالأحماض الدهنية وفيتامين E لترطيب وتقوية ألياف الشعر.</li>
  <li><strong>خلاصة إكليل الجبل (Rosemary Extract):</strong> تحفز الدورة الدموية بالفروة وتقوي البصيلات.</li>
  <li><strong>سيروم دوڤ المغذي:</strong> يحمي قشرة الشعرة من التكسر والجفاف.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الشعر وفروة الرأس فقط.</li>
  <li>تجنبي ملامسة الشامبو المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من الشعر الضعيف، الباهت، والمجهد الراغبة في شامبو مغذٍ بقوة الأفوكادو.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>دوڤ (Dove)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / شامبو تقوية وتغذية الشعر</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو تقوية الشعر بخلاصة الأفوكادو وإكليل الجبل (200ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>200 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>الشعر الضعيف، الباهت، والمتقصف</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر قوي، ناعم، لامع وخالٍ من التكسر والهيشان</td></tr>
  <tr><th>الملمس</th><td>سائل شامبو كريمي يرغي بكثافة</td></tr>
  <tr><th>العطر</th><td>عطر الأفوكادو وإكليل الجبل المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة الأفوكادو، خلاصة إكليل الجبل، سيروم دوڤ المغذي</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الإمارات (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (دوڤ)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الأفوكادو وإكليل الجبل لتقوية الشعر (Dove)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج شامبو دوڤ قوة الأفوكادو مشكلة ضعف وتقصف أطراف الشعر والتساقط الناجم عن التكسر والشحوب.</p>

<h3>لماذا تنجح تركيبته؟</h3>
<p>لأن الأفوكادو يزود الشعر بالأحماض الدهنية المغذية، بينما يحفز إكليل الجبل الفروة ويقوي جذر الشعرة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التدليك اللطيف للفروة:</strong> دلكي الفروة بحركات دائرية خفيفة أثناء الغسيل لتنشيط الدورة الدموية.<br>
2. <strong>الشطف بالماء الفاتر:</strong> اشطفي بالماء الفاتر لمنع جفاف الزيوت المغذية.<br>
3. <strong>التمشيط بعد التجفيف الخفيف:</strong> تجنبي تمشيط الشعر القاسي وهو شديد البلل لمنع التكسر.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "شامبو الأفوكادو يزيت الشعر بسرعة."<br>
<strong>الحقيقة:</strong> شامبو دوڤ صُمم بتركيبة خفيفة متوازنة تنظف الفروة وتغذي الخصلات دون تراكم دهني.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تنفذ الأحماض الدهنية وفيتامين E بالأفوكادو داخل الطبقة القشرية لزيادة مرونة الشعرة، بينما تحفز مركبات الروزبارينيك بإكليل الجبل البصيلات وتقوي الجذور.</p>"""

    faqs = [
        ("ما هو شامبو دوڤ قوة الأفوكادو 200مل؟", "هو شامبو مغذٍ ومقوٍ للشعر يحتوي على خلاصة الأفوكادو وإكليل الجبل لتقوية الشعر الضعيف ومنع التكسر."),
        ("ما هي فوائد الأفوكادو وإكليل الجبل للشعر؟", "يغذي الأفوكادو ألياف الشعر بالمرطبات وفيتامين E، بينما يحفز إكليل الجبل الفروة ويقوي البصيلات."),
        ("هل يقلل تساقط الشعر الناجم عن التكسر؟", "نعم، تقوية ألياف الشعر يقلل التساقط المسبب عن التكسر أثناء التمشيط."),
        ("ما حجم العبوة؟", "تأتي العبوة بحجم 200 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي كمية على الشعر المبلل، دلكي الفروة للحصول على رغوة، ثم اشطفي بالماء الفاتر."),
        ("هل يناسب الشعر الضعيف والباهت؟", "نعم، صُمم خصيصاً لإعادة الحيوية والقوة للشعر الضعيف والباهت."),
        ("ما هو بلد صنع شامبو دوڤ؟", "صُنع بواسطة شركة يونيلفر (Unilever) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات دوڤ لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يسبب جفاف الفروة؟", "لا، يحتوي على سيروم دوڤ المغذي الذي يحافظ على رطوبة الفروة والجلد."),
        ("ما هي رائحة الشامبو؟", "يتميز برائحة الأفوكادو وإكليل الجبل المنعشة والطبيعية."),
        ("هل يناسب الاستخدام اليومي؟", "نعم، آمن وممتاز للاستخدام اليومي."),
        ("هل يرغي بشكل جيد؟", "نعم، يولد رغوة كريمية غنية تنظف الخصلات برفق."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل يناسب الشعر المسبوغ؟", "نعم، تركيبة لطيفة تحافظ على مرونة الشعر المسبوغ."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب لكلا الجنسين."),
        ("هل يساعد في إعطاء لمعان ونعومة؟", "نعم، يترك الشعر ناعماً ولامعاً ببريق كريستالي."),
        ("هل العبوة 200 مل مناسبة للسفر؟", "نعم، حجم 200 مل مدمج ومثالي للسفر وحمل الحقيبة."),
        ("هل يسهل التمشيط بعده؟", "نعم، ينعم الشعر ويسهل مرور المشط دون تشابك."),
        ("هل العبوة محكمة الإغلاق؟", "تأتي في عبوة دائرية متينة بغطاء محكم يمنع التسرب."),
        ("هل يحتوي على بارابين؟", "التركيبة مطورة ومجربة جلدياً."),
        ("هل يعالج الأطراف المتقصفة؟", "نعم، يغذي وينعم الأطراف المتقصفة."),
        ("هل يعزز كثافة مظهر الشعر؟", "نعم، تقوية الألياف يمنح الشعر مظهراً أكثر امتلاءً وحيوية."),
        ("هل يناسب الأطفال؟", "مناسب للأطفال والبالغين من سن 12 سنة فما فوق."),
        ("هل ينظف الدهون الزائدة؟", "نعم، ينظف الدهون والشوائب برفق دون تجفيف."),
        ("هل هو خيار ممتاز للعائلة؟", "نعم، شامبو عائلي فاخر ومغذٍ.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Dove Avocado Strength Shampoo, 200ml</strong> is a nourishing strengthening shampoo engineered to restore vitality, strength, and brilliant shine to weak, brittle hair. Powered by natural Avocado Fruit Extract and nourishing Rosemary Extract, it gently cleanses the scalp while feeding hair follicles from root to tip to reduce hair fall caused by breakage.</p>
<p>Featuring Dove's signature rich creamy lather, it smooths coarse cuticles and infuses weak strands with tropical freshness and resilience after every wash.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Strengthens Weak Hair & Prevents Breakage:</strong> Feeds hair fibers to reduce breakage-induced hair fall.</li>
  <li><strong>Enriched with Avocado & Rosemary Extracts:</strong> Delivers essential fatty acids, Vitamin E, and scalp stimulation.</li>
  <li><strong>Gentle Cleansing & Rich Lather:</strong> Cleanses scalp impurities effectively without stripping natural moisture.</li>
  <li><strong>Silky Smoothness & Radiant Shine:</strong> Leaves hair touchably soft, glossy, and resilient.</li>
  <li><strong>Balanced Formula for Daily Care:</strong> Dermatologically safety-tested for weak and stressed hair.</li>
  <li><strong>Compact 200ml Bottle:</strong> Ideal convenient size for home and travel use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet hair thoroughly with warm water.</li>
  <li><strong>Step 2 (Apply):</strong> Dispense Dove Avocado Shampoo onto palms and massage into scalp and hair.</li>
  <li><strong>Step 3 (Rinse):</strong> Rinse thoroughly with warm water; repeat if desired.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Avocado Fruit Extract:</strong> Rich in essential fatty acids and Vitamin E to hydrate and fortify hair fibers.</li>
  <li><strong>Rosemary Extract:</strong> Stimulates scalp micro-circulation and strengthens hair roots.</li>
  <li><strong>Dove Nutritive Serum:</strong> Protects hair cuticles from drying and breakage.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external hair and scalp cleansing only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with weak, dull, or brittle hair seeking a nourishing Avocado strengthening shampoo.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Dove</td></tr>
  <tr><th>Category</th><td>Hair Care / Strengthening Shampoos</td></tr>
  <tr><th>Product Type</th><td>Avocado & Rosemary Hair Strengthening Shampoo</td></tr>
  <tr><th>Volume/Weight</th><td>200 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Weak, Dull, Brittle & Damaged Hair</td></tr>
  <tr><th>Finish</th><td>Strong, shiny, soft & breakage-reduced hair</td></tr>
  <tr><th>Texture</th><td>Creamy rich-lathering liquid shampoo</td></tr>
  <tr><th>Fragrance</th><td>Fresh Avocado & Rosemary botanical fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Avocado Fruit Extract, Rosemary Extract, Nutritive Serum</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / UAE (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever (Dove)</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Avocado Fatty Acids & Rosemary Hair Strengthening</h2>

<h3>What problem does this solve?</h3>
<p>Dove Avocado Strength Shampoo resolves weak hair breakage, split ends, and dullness.</p>

<h3>Why choose Dove Avocado?</h3>
<p>Avocado essential fatty acids hydrate the hair cortex, while Rosemary extract stimulates scalp roots to reduce breakage.</p>"""

    en_faqs = [
        ("What is Dove Avocado Strength Shampoo 200ml?", "It is a strengthening hair shampoo enriched with Avocado and Rosemary extracts to fortify weak hair and reduce breakage."),
        ("What are the benefits of Avocado and Rosemary?", "Avocado feeds hair fibers with essential fatty acids, while Rosemary stimulates scalp circulation to fortify roots."),
        ("Does it reduce hair fall from breakage?", "Yes, it fortifies weak hair fibers, reducing breakage-induced hair fall."),
        ("What volume is contained in this bottle?", "It comes in a 200ml bottle."),
        ("How do I use it correctly?", "Apply to wet hair, massage scalp into a creamy lather, and rinse with warm water."),
        ("Is it suitable for weak, dull hair?", "Yes, specially formulated to restore strength and radiance to weak hair."),
        ("Where is Dove manufactured?", "It is produced by Unilever following global quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Dove products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it dry out the scalp?", "No, it contains Dove Nutritive Serum to preserve scalp moisture."),
        ("What fragrance does it have?", "It features a fresh, natural Avocado and Rosemary scent."),
        ("Is it safe for daily use?", "Yes, safe and ideal for daily hair cleansing."),
        ("Does it lather well?", "Yes, it creates a rich, creamy lather."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Is it safe for color-treated hair?", "Yes, gentle formula preserves color elasticity."),
        ("Can both men and women use it?", "Yes, suitable for both men and women."),
        ("Does it add shine and smoothness?", "Yes, it leaves hair silky soft with a natural healthy shine."),
        ("Is the 200ml bottle travel-friendly?", "Yes, compact 200ml size fits easily into travel bags."),
        ("Does it ease post-wash combing?", "Yes, smooths hair cuticles for snag-free combing."),
        ("Is the bottle securely sealed?", "Yes, comes in a sturdy bottle with a flip top cap."),
        ("Does it contain parabens?", "Formulated and dermatologically tested under safety standards."),
        ("Does it treat split ends?", "Yes, nourishes and smooths dry split ends."),
        ("Does it enhance visible hair volume?", "Yes, strengthening hair fibers gives hair a fuller appearance."),
        ("Is it suitable for teenagers?", "Safe for adults and teens aged 12+."),
        ("Does it clean excess scalp oil?", "Yes, gently cleanses excess oil without stripping moisture."),
        ("Is it a good family shampoo?", "Yes, a premium nourishing family shampoo choice.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1776",
        "sku": "EK-1776",
        "gtin": "6281006604438",
        "category": "العناية بالشعر / شامبو تقوية وتغذية الشعر",
        "brand": "Dove",
        "ar": {
            "title": "شامبو دوڤ قوة الأفوكادو، 200مل",
            "meta_title": "شامبو دوف قوة الأفوكادو 200مل | صيدلية إكليل أبها",
            "meta_description": "اشتري شامبو دوڤ قوة الأفوكادو وإكليل الجبل (200مل). لتقوية الشعر الضعيف وتغذية البصيلات ومنع التكسر. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["دوف", "شامبو_دوف", "قوة_الافوكادو", "تقوية_الشعر", "إكليل_أبها"]
        },
        "en": {
            "title": "Dove Avocado Strength Shampoo, 200ml",
            "meta_title": "Dove Avocado Strength Shampoo 200ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy Dove Avocado Strength Shampoo (200ml). Fortifies weak hair with Avocado & Rosemary. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["dove", "avocado_shampoo", "hair_strength", "unilever", "ekleel_abha"]
        },
        "schema": {
            "brand": "Dove",
            "category": "Hair Care / Shampoo",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "dove-avocado-strength-shampoo-200ml.webp",
            "alt": "Dove Avocado Strength Shampoo 200ml",
            "title": "Dove Avocado Strength Shampoo 200ml"
        }
    }

print("Loaded Batch 14 builders")
