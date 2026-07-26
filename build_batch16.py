import json, os

def create_product_1783():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>فرشاة تنظيف الوجه ستارت مايكرز ذو الوجهين لتنظيف عميق ومساج للبشرة (Start Makers Double-Sided Facial Cleansing Brush)</strong> الأداة المزدوجة التجميلية المتطورة لتنظيف وتدليك وتنقية مسام البشرة بفاعلية احترافية. تجمع هذه الفرشاة الذكية بين جانبين وظيفيين: جانب بشعيرات فائقة النعومة فائقة الدقة (Ultra-soft Microfibers) لإزالة الأوساخ والبلاك وبقايا المكياج من المسام، وجانب آخر من السيليكون الطبي المرن (Medical Silicone Massager) لتدليك الوجه، تنشيط الدورة الدموية، وإزالة الرؤوس السوداء والجلد الميت.</p>
<p>تساعدكِ فرشاة ستارت مايكرز في تنظيف الوجه بعمق يزيد عن 5 أضعاف مقارنة بالتنظيف اليدوي، مما يعزز امتصاص السيرومات والكريمات ويترك بشرتكِ ناعمة، مشدودة، ومشرقة بنظافة فائقة دون التسبب في أي تهيج أو خدش للبشرة الحساسة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تصميم مزدوج الوظائف 2 في 1:</strong> جانب شعيرات فائقة النعومة وجانب سيليكون طبي مرن للتنعيم والتدليك.</li>
  <li><strong>تنظيف عميق للمسام 5 أضعاف:</strong> يزيل الرؤوس السوداء، الدهون الزائدة، وبقايا المكياج العميقة.</li>
  <li><strong>تدليك وتنشيط الدورة الدموية:</strong> يساعد جانب السيليكون في شد البشرة وتحفيز الكولاجين.</li>
  <li><strong>لطيفة وآمنة على البشرة الحساسة:</strong> شعيرات ناعمة جداً لا تسبب خدوشاً أو تهيجاً جلدياً.</li>
  <li><strong>مقبض مريح ومضاد للانزلاق:</strong> تصميم مقبض دافئ مريح يسهل التحكم به داخل الحمام.</li>
  <li><strong>سهلة التنظيف وسريعة التجفيف:</strong> مقاومة للبكتيريا وسهلة الشطف بالماء وتجف بسرعة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل والتنظيف):</strong> بلي وجهك والفرشاة بالماء الفاتر وضعي الغسول المفضل على الشعيرات الناعمة.</li>
  <li><strong>الخطوة الثانية (الفرك):</strong> دلكي الوجه بحركات دائرية خفيفة بالشعيرات الناعمة لتنظيف المسام لمدة 1 دقيقة.</li>
  <li><strong>الخطوة الثالثة (التدليك بالسيليكون):</strong> استخدمي جانب السيليكون لتدليك المناطق المعرضة للرؤوس السوداء (الأنف والذقن).</li>
  <li><strong>الخطوة الرابعة (الشطف والحفظ):</strong> اشطفي الوجه والفرشاة جيداً بالماء وعلقيها لتجف.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>شعيرات ميكروفايبر ناعمة جداً (Ultra-Soft Microfiber Bristles):</strong> تنظف المسام بدقة دون خدش.</li>
  <li><strong>سيليكون طبي مرن (Medical-Grade Silicone):</strong> يدلك البشرة ويزيل الرؤوس السوداء والجلد الميت.</li>
  <li><strong>مقبض بلاستيكي مريح (Ergonomic ABS Handle):</strong> يضمن ثبات وقبضة سهلة أثناء الاستعمال.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على بشرة الوجه فقط.</li>
  <li>تجنبي الفرك القسري على البشرة المصابة بالتهابات أو جروح مفتوحة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان جاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تبحث عن أداة تنظيف مزدوجة لتنقية مسام الوجه، إزالة الرؤوس السوداء، وتدليك البشرة اليومي.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ستارت مايكرز (Start Makers)</td></tr>
  <tr><th>الفئة</th><td>أجهزة ومستلزمات التجميل / فرش تنظيف وتدليك الوجه</td></tr>
  <tr><th>نوع المنتج</th><td>فرشاة تنظيف الوجه مزدوجة الجوانب (شعيرات + سيليكون)</td></tr>
  <tr><th>الحجم/الوزن</th><td>أداة يدوية واحدة قطعتين في جانبين</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (العادية، الدهنية، الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة، مسام منقاة، خالية من الرؤوس السوداء ومشدودة</td></tr>
  <tr><th>الملمس</th><td>شعيرات ناعمة جداً وجانب سيليكون مرن</td></tr>
  <tr><th>العطر</th><td>عديم الرائحة</td></tr>
  <tr><th>المكونات النشطة</th><td>شعيرات ميكروفايبر، سيليكون طبي، مقبض ABS</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين</td></tr>
  <tr><th>الشركة المصنعة</th><td>Start Makers Beauty Tools</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد تنظيف الوجه المزدوج (Start Makers)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تحل فرشاة ستارت مايكرز المزدوجة مشكلة انسداد المسام بالرؤوس السوداء، تراكم الخلايا الميتة، وضعف امتصاص سيرومات الوجه عند التنظيف اليدوي.</p>

<h3>لماذا تنجح تقنية الجانبين؟</h3>
<p>لأن الشعيرات الناعمة تفتح المسام وتزيل الدهون، بينما يزيل جانب السيليكون الرؤوس السوداء ويدلك الدورة الدموية لشد البشرة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام مع الغسول:</strong> استعملي الفرشاة دائماً مع غسولكِ المفضل المبلل بالماء.<br>
2. <strong>عدم الضغط القسري:</strong> دلكي بحركات دائرية خفيفة دون ضغط شديد.<br>
3. <strong>التجفيف الجيد:</strong> اشطفي الفرشاة وعلقيها في مكان جيد التهوية لمنع نمو البكتيريا.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "فرش تنظيف الوجه تسبب توسع المسام وتجريح البشرة."<br>
<strong>الحقيقة:</strong> الشعيرات فائقة النعومة والسيليكون الطبي ينظفان داخل المسام دون توسيعها أو خدش الجلد.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تزيل الشعيرات الدقيقة الرواسب الدقيقة والبيوفلم الزهمي من فتحات الجريبات الشعري، بينما يحفز التدليك بالسيليكون التدفق اللمفاوي والتروية الدموية للبشرة.</p>"""

    faqs = [
        ("ما هي فرشاة تنظيف الوجه ستارت مايكرز ذو الوجهين؟", "هي أداة تنظيف وتدليك مزدوجة تحتوي على جانب بشعيرات فائقة النعومة وجانب سيليكون طبي لتدليك وتنقية مسام الوجه."),
        ("ما هي فوائد استخدام الجانبين؟", "ينظف جانب الشعيرات الناعمة المسام والمكياج، بينما يزيل جانب السيليكون الرؤوس السوداء ويدلك الوجه."),
        ("هل تسبب خدشاً للبشرة الحساسة؟", "لا، الشعيرات فائقة النعومة والسيليكون الطبي آمنان تماماً ولطيفان على البشرة الحساسة."),
        ("هل تساعد في إزالة الرؤوس السوداء؟", "نعم، جانب السيليكون ممتاز لتقشير الرؤوس السوداء في منطقة الأنف والذقن."),
        ("هل تحتاج إلى بطاريات أو شحن؟", "لا، أداة يدوية بالكامل لا تحتاج لبطاريات أو شحن."),
        ("ما هو بلد صنع الفرشاة؟", "صُنع بتقنية وتصميم عالي الجودة للجمال."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع أجهزة ومستلزمات التجميل لدى إكليل أبها أصلية 100% ومصنوعة من مواد آمنة."),
        ("كيف تنظف الفرشاة بعد كل استخدام؟", "تُغسل بالماء الفاتر والصابون وتترك لتعلق وتجف للهواء."),
        ("كم مرة يُنصح باستخدامها أسبوعياً؟", "يُنصح باستخدامها من 2 إلى 4 مرات أسبوعياً حسب نوع البشرة."),
        ("هل تزيد امتصاص سيرومات الوجه؟", "نعم، تنظيف المسام العميق يزيد فاعلية امتصاص السيرومات والكريمات."),
        ("هل تناسب جميع أنواع البشرة؟", "مناسبة للبشرة الدهنية، المختلطة، الجافة، والحساسة."),
        ("هل مقبض الفرشاة مضاد للانزلاق؟", "نعم، مقبض ABS مريح ومصمم لمنع الانزلاق أثناء الاستحمام."),
        ("هل تعزز نضارة البشرة؟", "نعم، تدليك السيليكون ينشط الدورة الدموية ويعيد النضارة الحيوية."),
        ("هل تترك حساسية أو احمراراً؟", "إذا استخدمت برفق ودون ضغط قسري فلا تسبب أي احمرار."),
        ("هل هي خيار اقتصادي؟", "نعم، أداة متينة تدوم طويلاً بديل ممتا ممتاز للأجهزة الكهربائية المكلفة."),
        ("هل العبوة مدمجة وسهلة السفر؟", "نعم، حجمها مدمج وخفيف الوزن لحملها في حقيبة التجميل."),
        ("هل تنظف بقايا المكياج الثقيل؟", "نعم، تزيل رواسب الفاونديشن والبودرة العميقة."),
        ("هل يمكن استخدامها مع الغسول الزيتي؟", "نعم، تعمل بفاعلية مع كافة أنواع الغسولات المائية والزيتية والرغوية."),
        ("هل العبوة محكمة التغليف؟", "تأتي في عبوة مغلفة طبقاً لأعلى المعايير الصحية."),
        ("هل تساعد في تقليل حب الشباب؟", "نعم، منع انسداد المسام بالدهون يقلل فرص تكون الحبوب."),
        ("هل تناسب الرجال والنساء؟", "نعم، مناسبة لكلا الجنسين لروتين العناية بالبشرة."),
        ("هل تصمد مع الاستخدام المتكرر؟", "نعم، تصنع من مواد عالية الجودة لا تتلف بالماء."),
        ("كيف تحفظ الفرشاة لمنع البكتيريا؟", "تعلق من الخيط المرفق ليجف جانب الشعيرات بالكامل."),
        ("هل تقلل مظهر المسام الواسعة؟", "نعم، تنظيف الدهون يقلل بروز وتوسع فتحات المسام."),
        ("هل تشجع على الالتزام بروتين العناية؟", "تصميمها العملي المريح يجعل روتين التنظيف ممتعاً وسريعاً.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Start Makers Double-Sided Facial Cleansing Brush</strong> is the professional dual-action skincare tool designed to deeply cleanse, exfoliate, and massage facial skin. Featuring a dual-head design, one side boasts ultra-soft microfibers that clear pore impurities, sweat, and makeup residue, while the reverse side features a medical-grade silicone massager for targeted blackhead removal and micro-circulation enhancement.</p>
<p>Cleansing up to 5 times more effectively than manual hand washing, the Start Makers facial brush boosts skincare product absorption, leaving your skin touchably soft, firm, and radiant without causing skin friction or redness.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>2-in-1 Dual Action Design:</strong> Ultra-soft microfibers for deep cleansing plus medical silicone for massage.</li>
  <li><strong>5x Deeper Pore Cleansing:</strong> Sweeps away blackheads, excess sebum, and embedded makeup residue.</li>
  <li><strong>Facial Massage & Circulation Boost:</strong> Silicone massager stimulates collagen synthesis and tightens skin.</li>
  <li><strong>Ultra-Gentle on Sensitive Skin:</strong> Microfine bristles clear pores smoothly without scratching skin.</li>
  <li><strong>Ergonomic Non-Slip Grip:</strong> Soft-touch ABS handle designed for effortless shower control.</li>
  <li><strong>Hygienic & Quick Drying:</strong> Mold-resistant materials easily rinsed with water that dry rapidly.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Prep & Apply):</strong> Wet face and brush head with warm water and apply your favorite cleanser onto soft bristles.</li>
  <li><strong>Step 2 (Cleanse):</strong> Gently massage face in circular motions using micro-bristles for 1 minute to clear pores.</li>
  <li><strong>Step 3 (Massaging Exfoliation):</strong> Use the silicone side to exfoliate blackhead-prone T-zone areas (nose and chin).</li>
  <li><strong>Step 4 (Rinse & Hang):</strong> Rinse face and brush thoroughly with water, then hang to air dry.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Ultra-Soft Microfiber Bristles:</strong> Deeply cleanse pores without scratching delicate facial skin.</li>
  <li><strong>Medical-Grade Silicone Massager:</strong> Exfoliates dead skin cells and blackheads gently.</li>
  <li><strong>Ergonomic ABS Plastic Handle:</strong> Provides a sturdy, anti-slip grip.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external facial cleansing use only.</li>
  <li>Avoid aggressive friction on inflamed, broken, or acne-erupted skin.</li>
  <li>Keep out of reach of children and store in a dry, ventilated area.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a dual-action manual cleansing brush for deep pore purification, blackhead care, and daily facial massage.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Start Makers</td></tr>
  <tr><th>Category</th><td>Beauty Tools / Facial Cleansing & Massaging Brushes</td></tr>
  <tr><th>Product Type</th><td>Dual-Sided Facial Cleansing & Massaging Brush</td></tr>
  <tr><th>Volume/Weight</th><td>Single Handheld Dual-Head Tool</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Normal, Oily, Combination, Sensitive)</td></tr>
  <tr><th>Finish</th><td>Deeply cleansed, exfoliated, radiant & firm facial skin</td></tr>
  <tr><th>Texture</th><td>Ultra-soft microfibers & flexible medical silicone</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-Free</td></tr>
  <tr><th>Active Ingredients</th><td>Microfiber Bristles, Medical Silicone, ABS Handle</td></tr>
  <tr><th>Country of Origin</th><td>China</td></tr>
  <tr><th>Manufacturer</th><td>Start Makers Beauty Tools</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Microfiber & Silicone Facial Cleansing</h2>

<h3>What problem does this solve?</h3>
<p>Start Makers Dual-Sided Brush resolves clogged pores, blackheads, dead skin accumulation, and ineffective manual hand cleansing.</p>

<h3>Why choose Start Makers?</h3>
<p>Microfine fibers dislodge sebum biofilms, while medical silicone massagers stimulate lymphatic drainage and boost facial blood circulation.</p>"""

    en_faqs = [
        ("What is the Start Makers Double-Sided Facial Cleansing Brush?", "It is a 2-in-1 facial tool featuring ultra-soft microfine bristles on one side and a medical silicone massager on the reverse."),
        ("What are the benefits of the dual-sided design?", "Soft bristles deeply cleanse pores and makeup, while the silicone side exfoliates blackheads and massages facial skin."),
        ("Does it scratch or irritate sensitive skin?", "No, ultra-soft microfibers and medical silicone are 100% gentle and safe for sensitive skin."),
        ("Does it help eliminate blackheads?", "Yes, the silicone side excels at exfoliating blackheads around the nose and chin T-zone."),
        ("Does it require batteries or power?", "No, it is a manual tool needing zero batteries or charging."),
        ("Where is Start Makers manufactured?", "It is manufactured under precision beauty tool quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All beauty tools at Ekleel Abha are 100% original and made from safe materials."),
        ("How do I clean the brush after use?", "Rinse thoroughly with warm water and soap, then hang to air dry."),
        ("How many times a week should I use it?", "Use 2 to 4 times weekly depending on your skin type."),
        ("Does it enhance skincare absorption?", "Yes, deep pore purification allows serums and moisturizers to absorb more effectively."),
        ("Is it suitable for all skin types?", "Ideal for oily, combination, dry, and sensitive skin types."),
        ("Is the handle anti-slip?", "Yes, features an ergonomic ABS handle designed for easy shower grip."),
        ("Does it boost skin radiance?", "Yes, silicone facial massage stimulates blood micro-circulation for a radiant glow."),
        ("Does it cause skin redness?", "When used with gentle pressure, it causes zero redness or friction irritation."),
        ("Is it an economical choice?", "Yes, a durable manual tool offering salon-grade cleansing without electric device costs."),
        ("Is it travel-friendly?", "Yes, compact and lightweight for travel beauty kits."),
        ("Does it remove heavy makeup residue?", "Yes, effectively sweeps away deep foundation and powder residue."),
        ("Can it be used with oil cleansers?", "Yes, compatible with water, foam, gel, and oil cleansers."),
        ("Is the packaging hygienic?", "Yes, packaged securely following hygiene standards."),
        ("Does it help reduce acne breakouts?", "Yes, unclogging pores prevents acne-causing sebum buildups."),
        ("Can both men and women use it?", "Yes, suitable for both men and women."),
        ("Is the tool durable?", "Yes, crafted from high-grade water-resistant materials."),
        ("How should I store it to prevent mold?", "Hang using the attached loop in a well-ventilated area so bristles air dry."),
        ("Does it help minimize enlarged pores?", "Yes, clearing trapped sebum reduces the appearance of enlarged pores."),
        ("Does it make daily skincare enjoyable?", "Yes, its ergonomic design makes facial cleansing quick and relaxing.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1783",
        "sku": "EK-1783",
        "gtin": "6911183230181",
        "category": "أجهزة ومستلزمات التجميل / فرش تنظيف وتدليك الوجه",
        "brand": "Start Makers",
        "ar": {
            "title": "فرشاة تنظيف الوجه ستارت مايكرز ذو الوجهين لتنظيف عميق ومساج للبشرة",
            "meta_title": "فرشاة تنظيف الوجه ستارت مايكرز ذو الوجهين | صيدلية إكليل أبها",
            "meta_description": "اشتري فرشاة تنظيف الوجه ستارت مايكرز ذو الوجهين. تنظيف عميق للمسام ومساج بالسيليكون لتنقيه البشرة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["ستارت_مايكرز", "فرشاة_الوجه", "تنظيف_المسام", "مساج_السيليكون", "إكليل_أبها"]
        },
        "en": {
            "title": "Start Makers Double-Sided Facial Cleansing Brush",
            "meta_title": "Start Makers Double-Sided Facial Cleansing Brush | Ekleel Abha",
            "meta_description": "Buy original Start Makers Double-Sided Facial Cleansing Brush. Ultra-soft microfibers & silicone massager for deep pore cleansing. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["start_makers", "facial_brush", "pore_cleansing", "silicone_massager", "ekleel_abha"]
        },
        "schema": {
            "brand": "Start Makers",
            "category": "Beauty Tool / Facial Cleansing Brush",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "start-makers-double-sided-facial-cleansing-brush.webp",
            "alt": "Start Makers Double-Sided Facial Cleansing Brush",
            "title": "Start Makers Double-Sided Facial Cleansing Brush"
        }
    }

def create_product_ogx(prod_id, title_ar, title_en, meta_desc_ar, meta_desc_en, active_ing_ar, active_ing_en, desc_intro_ar, desc_intro_en, tags_ar, tags_en, gtin, img_slug):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{title_ar}</strong> المستحضر المغذي الفاخر والأكثر شهرة عالمياً لإعادة الحيوية، المرونة، والترطيب الاستثنائي لألياف الشعر. يرتكز هذا الشامبو المتطور من او جي اكس (OGX) على تركيبة غنية بـ {active_ing_ar} ورغوة فاخرة خالية تماماً من السلفات القاسية (Sulfate-Free Surfactants)، حيث ينظف الفروة وألياف الشعر بفاعلية ولطف دون تجريد الزيوت الطبيعية.</p>
<p>يمتاز شامبو او جي اكس بقوام كريمي ينفذ في ألياف الشعر ليمنحها مرونة ونعومة فائقة، ويترك شعركِ مصففاً، مشرقاً ببريق كريستالي، ورائحة استوائية زكية تدوم طويلاً بعد كل غسلة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتغذية مكثفة للشعر:</strong> يزود ألياف الشعر بالمرطبات والزيوت المغذية لإعادة الحيوية.</li>
  <li><strong>خالي من السلفات والبارابين (Sulfate-Free Surfactants):</strong> ينظف الفروة بلطف دون تجفيف الخصلات.</li>
  <li><strong>قوة ولمعان كريستالي:</strong> يعيد البريق والنعومة للشعر الباهت والجاف.</li>
  <li><strong>حماية ضد التكسر والهيشان:</strong> يغلف الشعر بحجاب واقٍ يمنع الهيشان بفعل الرطوبة.</li>
  <li><strong>عطر استوائي فاخر يدوم طويلاً:</strong> يترك عبقاً زكياً يرافق شعركِ طوال اليوم.</li>
  <li><strong>عبوة وافرة سعة 385 مل:</strong> تصميم بيضاوي أنيق يضمن عناية وتغذية مستمرة يومياً.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل):</strong> بلي شعركِ بالماء الفاتر جيداً.</li>
  <li><strong>الخطوة الثانية (التطبيق والفرك):</strong> وضعي كمية مناسبة من الشامبو على كف اليد ودلكي الفروة بحركات دائرية حتى تشكيل رغوة كريمية غنية.</li>
  <li><strong>الخطوة الثالثة (الشطف):</strong> اشطفي بالماء الفاتر جيداً، ويفضل إتباعه ببلسم OGX المماثل لنتائج مضاعفة.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>{active_ing_ar}:</strong> يغذي قشرة الشعرة ويمنحها المرونة واللمعان.</li>
  <li><strong>منظفات خالية من السلفات (Sulfate-Free Base):</strong> تنظف برفق دون تجريف الحواجز الدهنية الطبيعية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الشعر وفروة الرأس فقط.</li>
  <li>تجنبي ملامسة الشامبو المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تبحث عن شامبو خالي من السلفات بغنى {active_ing_ar} لترطيب وتغذية الشعر.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>او جي اكس (OGX)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / شامبو خالي من السلفات لتغذية الشعر</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو مغذٍ ومجدد للشعر خالي من السلفات (385ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>385 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (الجاف، التالف، والمجهد)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم، حريري، لامع وخالٍ من الهيشان والجفاف</td></tr>
  <tr><th>الملمس</th><td>سائل شامبو كريمي رغوي خالي من السلفات</td></tr>
  <tr><th>العطر</th><td>عطر استوائي غني وفريد من OGX</td></tr>
  <tr><th>المكونات النشطة</th><td>{active_ing_ar}، منظفات خالية من السلفات</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة الأمريكية / المملكة المتحدة (Johnson & Johnson)</td></tr>
  <tr><th>الشركة المصنعة</th><td>OGX Beauty (Johnson & Johnson)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد منتجات OGX الخالية من السلفات</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج الشامبو مشكلة جفاف الشعر، الهيشان، وتلف قشرة الشعرة الناجم عن غسيل الشامبوهات التقليدية القاسية.</p>

<h3>لماذا تنجح تركيبة OGX؟</h3>
<p>لأن المنظفات الخالية من السلفات تنظف الفروة برفق، بينما يزود {active_ing_ar} الألياف بالبروتينات والزيوت الحيوية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام الماء الفاتر:</strong> اشطفي بالماء الفاتر لحفظ الترطيب.<br>
2. <strong>الإتباع بالبلسم المماثل:</strong> استعملي بلسم OGX المماثل بعد الشامبو لنتائج مضاعفة.<br>
3. <strong>التجفيف بالربت:</strong> جففي الشعر بفوطة ناعمة بالربت دون فرك قسري.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الشامبو الخالي من السلفات لا يرغي ولا ينظف."<br>
<strong>الحقيقة:</strong> شامبو OGX يولد رغوة كريمية غنية تنظف الفروة بعمق ورقة متناهية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتكامل المكونات المغذية مع حراشف الشعرة القشرية (Cuticles)، مما يزيد من مرونتها ويمنع تكسر الألياف ويمنح لمعاناً استثنائياً.</p>"""

    faqs = [
        (f"ما هو {title_ar}؟", f"هو شامبو مغذٍ خالي من السلفات سعة 385 مل غني بـ {active_ing_ar} لترطيب وتغذية الشعر."),
        (f"ما هي فوائد {active_ing_ar} للشعر؟", "يغذي قشرة الشعرة، يعزز المرونة واللمعان، ويمنع الجفاف والهيشان."),
        ("هل الشامبو خالي من السلفات والبارابين؟", "نعم، خالي من السلفات القاسية والبارابين (Sulfate-Free Surfactants)."),
        ("ما حجم العبوة؟", "تأتي بحجم وافر يبلغ 385 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي كمية على الشعر المبلل، دلكي الفروة للحصول على رغوة غنية، ثم اشطفي جيداً."),
        ("هل يناسب الشعر الجاف والتالف؟", "نعم، ممتاز جداً لإعادة الحيوية والترطيب للشعر الجاف والمجهد."),
        ("ما هو بلد صنع OGX؟", "صُنع بواسطة شركة OGX العالمية (Johnson & Johnson)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات OGX لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يترك رائحة زكية؟", "نعم، يتميز بعطر استوائي فاخر يدوم على الشعر طوال اليوم."),
        ("هل يساعد في فك تشابك الشعر؟", "نعم، ينعم ألياف الشعر ويسهل مرور المشط بسلاسة."),
        ("هل يناسب الشعر المسبوغ والمعالج؟", "نعم، تركيبة خالية من السلفات تحافظ على لون ومرونة الشعر المعالج."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب لكلا الجنسين."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف داخل الحمام."),
        ("هل العبوة 385 مل اقتصادية؟", "نعم، عبوة كبيرة البيضاوية تدوم لأشهر طويلة."),
        ("هل يرغي بشكل ممتاز؟", "نعم، يولد رغوة كريمية فاخرة تنظف بفاعلية."),
        ("هل يمنع هيشان الشعر في الرطوبة؟", "نعم، يغلف الخصلات ويمنع تأثير الرطوبة والهيشان."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة بيضاوية أنيقة بغطاء محكم يمنع التسرب."),
        ("هل يناسب جميع أنواع الشعر؟", "مناسب جداً للشعر العادي، الجاف، المجهد، والمجعد."),
        ("هل يعيد لمعان ونعومة الشعر؟", "نعم، يترك الشعر حريرياً ولامعاً ببريق كريستالي."),
        ("هل يناسب الأطفال والمراهقين؟", "مناسب للأطفال والبالغين من سن 12 سنة فما فوق."),
        ("هل يمكن استخدامه يومياً؟", "نعم، آمن وممتاز للاستخدام المنتظم."),
        ("هل يعالج تقصف الأطراف؟", "نعم، يغذي وينعم الأطراف المتضررة."),
        ("هل يمنع تكسر الشعر عند التمشيط؟", "نعم، زيادة مرونة الألياف يمنع تكسرها أثناء التمشيط."),
        ("هل يفضل استخدامه مع البلسم المماثل؟", "نعم، يُفضل إتباعه ببلسم OGX المماثل لنتائج مضاعفة."),
        ("هل هو الشامبو المفضل عالمياً للعناية بالبروتين؟", "نعم، الماركة الأولى الموصى بها عالمياً للشعر المعالج.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{title_en}</strong> is the world-renowned sulfate-free nourishing shampoo designed to restore hydration, resilience, and radiant silkiness to dry or damaged hair. Formulated by OGX Beauty using eco-conscious sulfate-free surfactants, it gently cleanses the scalp and hair without stripping essential natural oils.</p>
<p>Enriched with {active_ing_en}, it penetrates deep into hair cuticles to deliver weightless moisture, leaving your hair touchably soft, smooth, and beautifully scented with an exotic long-lasting tropical aroma.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intensive Moisture & Nourishment:</strong> Infuses hair cuticles with restorative nutrients for silky elasticity.</li>
  <li><strong>100% Sulfate-Free Surfactants Base:</strong> Gently cleanses without drying or stripping natural oils.</li>
  <li><strong>Crystal Shine & Frizz Control:</strong> Smooths unruly flyaways and imparts a healthy glossy shine.</li>
  <li><strong>Breakage & Humidity Shield:</strong> Coats hair strands against moisture loss and humidity frizz.</li>
  <li><strong>Signature Long-Lasting Exotic Aroma:</strong> Leaves hair scented with a luxurious tropical fragrance.</li>
  <li><strong>Generous 385ml Bottle:</strong> Iconic oval bottle providing months of continuous premium hair care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet hair thoroughly with warm water.</li>
  <li><strong>Step 2 (Lather):</strong> Apply OGX Shampoo onto palms and massage into scalp to create a rich creamy lather.</li>
  <li><strong>Step 3 (Rinse):</strong> Rinse thoroughly with warm water; follow with matching OGX Conditioner for best results.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>{active_ing_en}:</strong> Deeply feeds hair cuticles and fortifies structural elasticity.</li>
  <li><strong>Sulfate-Free Surfactants Cleansing Base:</strong> Cleanses gently preserving natural moisture barriers.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external hair cleansing application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a sulfate-free shampoo enriched with {active_ing_en} to nourish and hydrate dry, frizzy, or damaged hair.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>OGX Beauty</td></tr>
  <tr><th>Category</th><td>Hair Care / Sulfate-Free Nourishing Shampoos</td></tr>
  <tr><th>Product Type</th><td>Sulfate-Free Nourishing & Hydrating Shampoo (385ml)</td></tr>
  <tr><th>Volume/Weight</th><td>385 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Dry, Damaged, Frizzy)</td></tr>
  <tr><th>Finish</th><td>Silky, smooth, shiny & frizz-free hair</td></tr>
  <tr><th>Texture</th><td>Creamy rich sulfate-free foaming shampoo</td></tr>
  <tr><th>Fragrance</th><td>Exotic OGX signature tropical fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>{active_ing_en}، Sulfate-Free Surfactants Base</td></tr>
  <tr><th>Country of Origin</th><td>USA / UK (Johnson & Johnson)</td></tr>
  <tr><th>Manufacturer</th><td>OGX Beauty (Johnson & Johnson)</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Sulfate-Free Surfactants & Hair Cuticle Hydration</h2>

<h3>What problem does this solve?</h3>
<p>OGX Shampoo resolves severe hair dryness, coarse frizz, and cuticle stripping caused by harsh sulfates.</p>

<h3>Why choose OGX?</h3>
<p>Sulfate-free surfactants cleanse hair gently while {active_ing_en} integrates into structural cuticles to lock in moisture.</p>"""

    en_faqs = [
        (f"What is {title_en}?", f"It is a sulfate-free nourishing shampoo in a 385ml bottle enriched with {active_ing_en}."),
        (f"What are the benefits of {active_ing_en}?", "Feeds hair cuticles, enhances elasticity and shine, and locks out moisture loss."),
        ("Is it sulfate-free and paraben-free?", "Yes, formulated with sulfate-free surfactants and free of parabens."),
        ("What volume is contained in this bottle?", "It comes in a generous 385ml iconic oval bottle."),
        ("How do I use it correctly?", "Apply to wet hair, massage into a rich lather, and rinse thoroughly with warm water."),
        ("Is it suitable for dry, damaged hair?", "Yes, excellent for restoring softness and hydration to dry, stressed hair."),
        ("Where is OGX manufactured?", "It is produced by OGX Beauty under Johnson & Johnson standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All OGX products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it leave a pleasant scent?", "Yes, features an exotic, long-lasting signature tropical fragrance."),
        ("Does it ease hair detangling?", "Yes, smooths hair cuticles so combs glide through effortlessly."),
        ("Is it safe for color-treated and keratin hair?", "Yes, sulfate-free formula preserves hair color and keratin bonds."),
        ("Can both men and women use it?", "Yes, suitable for both men and women."),
        ("How should I store the bottle?", "Store in a cool, dry place inside your shower area."),
        ("Is the 385ml bottle economical?", "Yes, generous volume provides months of daily washing."),
        ("Does it lather well despite being sulfate-free?", "Yes, produces a rich, creamy cleansing lather."),
        ("Does it protect against humidity frizz?", "Yes, coats strands to lock out atmospheric humidity frizz."),
        ("Is the bottle securely sealed?", "Yes, comes in a sturdy bottle with a leak-proof cap."),
        ("Is it suitable for all hair types?", "Ideal for normal, dry, frizzy, coarse, and damaged hair."),
        ("Does it impart brilliant shine?", "Yes, leaves hair touchably soft with a healthy glossy shine."),
        ("Is it safe for teenagers?", "Safe for adults and teens aged 12+."),
        ("Can it be used daily?", "Yes, safe and gentle for daily use."),
        ("Does it smooth split ends?", "Yes, nourishes and smooths dry split ends."),
        ("Does it prevent friction breakage?", "Yes, increased strand lubricity prevents friction breakage during combing."),
        ("Should it be paired with OGX Conditioner?", "Yes, pairing with matching OGX Conditioner maximizes silkiness."),
        ("Is OGX a top choice for protein care?", "Yes, globally famous for sulfate-free hair maintenance.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "العناية بالشعر / شامبو خالي من السلفات لتغذية الشعر",
        "brand": "OGX",
        "ar": {
            "title": title_ar,
            "meta_title": f"{title_ar[:35]} | صيدلية إكليل أبها",
            "meta_description": f"اشتري {title_ar}. شامبو خالي من السلفات {meta_desc_ar}. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": title_en,
            "meta_title": f"{title_en[:35]} | Ekleel Abha Pharmacy",
            "meta_description": f"Buy original {title_en}. Sulfate-free shampoo {meta_desc_en}. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": tags_en
        },
        "schema": {
            "brand": "OGX",
            "category": "Hair Care / Shampoo",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"{img_slug}.webp",
            "alt": title_en,
            "title": title_en
        }
    }

print("Loaded Batch 16 builders")
