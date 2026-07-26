import json, os

def create_product_1763():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>ممحاة شعر من كريستال (Crystal Hair Eraser)</strong> الابتكار الثوري والأحدث عالمياً لإزالة الشعر وتقشير البشرة بدون ألم أو استخدام شفرات أو شمع أو مواد كيميائية قاسية. تعتمد هذه الممحاة الكريستالية السحرية على تقنية النانو الكريستالية (Nano-Crystalline Technology)، حيث تفرك السطح الدقيق على الجلد بحركات دائرية خفيفة لتكتل وإزالة الشعر من الجذور السطحية بفعالية مذهلة.</p>
<p>تمنحكِ ممحاة الكريستال تقشيراً لطيفاً يزيل خلايا الجلد الميتة، مما يقلل مظهر "جلد الدجاجة" (Strawberry Legs)، ويمنع نمو الشعر تحت الجلد، ويترك بشرتكِ ناعمة كالحرير ومشرقة في دقائق معدودة، وهي أداة قابلة لإعادة الاستخدام لعدة سنوات دون الحاجة لشحن أو شفرات.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>إزالة الشعر وتقشير البشرة بدون ألم:</strong> تكنس الشعر وتقشر الجلد الميت بحركات دائرية خفيفة.</li>
  <li><strong>تقنية النانو الكريستالية السحرية:</strong> تفتت وتقشر الشعر بسهولة دون جرح أو حرق للبشرة.</li>
  <li><strong>الوقاية من الشعر تحت الجلد (جلد الدجاجة):</strong> تنعم البشرة الخشنة وتحد من ظهور الحبوب بعد إزالة الشعر.</li>
  <li><strong>خالية من المواد الكيميائية والشفرات:</strong> لا تحتاج لشفرات، شمع، أو كهرباء، مما يجعلها آمنة 100%.</li>
  <li><strong>قابلة لإعادة الاستخدام وتوفير اقتصادي:</strong> تدوم حتى 3 سنوات من الاستخدام المتكرر وسهلة التنظيف بالماء.</li>
  <li><strong>تصميم مدمج ومثالي للسفر:</strong> قبضة مريحة وحجم مدمج يسهل حملها في الحقيبة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل والتجهيز):</strong> يُفضل الاستخدام على بشرة جافة أو رطبة خفيفاً بعد الحمام الدافئ.</li>
  <li><strong>الخطوة الثانية (التطبيق والفرك):</strong> وضعي السطح الكريستالي على المنطقة المطلوبة وافركي بلطف بحركات دائرية خفيفة دون ضغط قسري.</li>
  <li><strong>الخطوة الثالثة (التنظيف وشطف البشرة):</strong> اشطفي المنطقة بالماء الفاتر وضعي كريم مرطب فوراً لحبس الترطيب.</li>
  <li><strong>الخطوة الخامسة (غسل الأداة):</strong> اشطفي ممحاة الكريستال بالماء وافتحيها لتجف للاستخدام القادم.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>سطح النانو كريستال (Nano-Crystalline Glass Surface):</strong> زجاج دقيق محفور بتقنية تقشر الشعر والجلد الميت بأمان.</li>
  <li><strong>مقبض مريح بلاستيكي (Ergonomic ABS Handle):</strong> يمنحكِ تحكماً كاملاً أثناء التدليك.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الساقين، الذراعين، والظهر؛ تجنبي استخدامها على البشرة شديدة الحساسية أو الوجه والمناطق الحساسة.</li>
  <li>تجنبي الضغط الشديد أثناء الفرك لمنع تهيج الجلد.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تبحث عن أداة سحرية وآمنة لإزالة شعر الساقين والذراعين وتقشير الجلد الميت بدون ألم أو شفرات.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>عام / الكريستال السحري</td></tr>
  <tr><th>الفئة</th><td>أجهزة ومستلزمات التجميل / إزالة الشعر الكريستالية</td></tr>
  <tr><th>نوع المنتج</th><td>ممحاة إزالة الشعر وتقشير البشرة الكريستالية (Crystal Hair Eraser)</td></tr>
  <tr><th>الحجم/الوزن</th><td>أداة كريستالية مدمجة قطعة واحدة</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (الساقين، الذراعين، الظهر)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة، حريرية، خالية من الشعر والجلد الميت</td></tr>
  <tr><th>الملمس</th><td>سطح زجاجي كريستالي دقيق المحفور</td></tr>
  <tr><th>العطر</th><td>عديم الرائحة</td></tr>
  <tr><th>المكونات النشطة</th><td>زجاج نانو كريستال، بلاستيك ABS مقوى</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beauty Care Technologies</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (من 15 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لتقنية النانو الكريستالية وإزالة الشعر (Crystal Eraser)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تحل ممحاة الكريستال مشكلة جروح الشفرات، حروق الشمع، نمو الشعر تحت الجلد (جلد الدجاجة)، وآلام إزالة الشعر التقليدية.</p>

<h3>لماذا تنجح هذه التقنية؟</h3>
<p>لأن محفورات الزجاج الكريستالية الدقيقة تلتف حول شعر السطح وتكسره بلطف عند الفرك الدائري، بالتزامن مع تقشير الخلايا الميتة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الفرك الخفيف:</strong> لا تضغطي بقوة على الجلد لتفادي الاحمرار.<br>
2. <strong>الترطيب المباشر:</strong> وضعي كريم لوشن مرطب فوراً بعد الاستخدام.<br>
3. <strong>تجنب الوجه والمناطق الحساسة:</strong> استعمليها للساقين والذراعين والظهر بشكل أساسي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "ممحاة الكريستال تجعل الشعر ينمو أكثر سمكاً."<br>
<strong>الحقيقة:</strong> إزالة الشعر وتقشيره بحركات دائرية يترك أطراف الشعر النابت ناعمة ودون حواف حادة بعكس الشفرة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تُحدث الجزيئات الكريستالية الدقيقة احتكاكاً ميكانيكياً م controlado يجذب شعرات الجلد ويقشر الطبقة القرنية، مما يرفع الشعر ويصقل البشرة.</p>"""

    faqs = [
        ("ما هي ممحاة شعر من كريستال؟", "هي أداة زجاجية نانو كريستالية مصممة لإزالة الشعر وتقشير خلايا الجلد الميتة بدون ألم أو شفرات أو شمع."),
        ("كيف تعمل ممحاة الكريستال؟", "تُفرك على البشرة بحركات دائرية خفيفة فتفتت الشعر وتقشر الجلد الميت في ثوانٍ."),
        ("هل تسبب أليماً أو جروحاً؟", "لا تسبب أي ألم أو جروح لأنها خالية من الشفرات والشمع."),
        ("هل تساعد في التخلص من جلد الدجاجة والشعر تحت الجلد؟", "نعم، تقشير خلايا الجلد الميتة يمنع نمو الشعر تحت الجلد وينعم البشرة الخشنة."),
        ("ما هي المناطق المناسبة لاستخدامها؟", "ممتازة جداً للساقين، الذراعين، الظهر، والساعدين."),
        ("هل يمكن استخدامها للوجه أو المناطق الحساسة؟", "لا يُنصح باستخدامها على الوجه أو المناطق شديدة الحساسية تفادياً لتهيج البشرة الرقيقة."),
        ("ما هي مدة استخدام الأداة؟", "قابلة لإعادة الاستخدام وتدوم حتى 3 سنوات دون الحاجة لشحن أو استبدال قطع."),
        ("ما هو بلد صنع الأداة؟", "صُنع بتقنية النانو الكريستالية الحديثة."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع المستلزمات لدى إكليل أبها أصلية 100% ومصنوعة من كريستال عالي الجودة."),
        ("كيف تنظف الأداة بعد الاستخدام؟", "تغسل بسهولة بالماء الفاتر وتترك لتجف."),
        ("هل يلزم ترطيب البشرة بعدها؟", "نعم، يُفضل دائماً وضع كريمكِ المرطب المفضل بعد التقشير."),
        ("هل تستخدم على بشرة جافة أم مبللة؟", "يمكن استخدامها على بشرة جافة أو رطبة خفيفاً بعد حمام دافئ."),
        ("هل تسبب احمراراً للبشرة؟", "إذا تم الفرك برفق ودون ضغط قسري فلا تسبب احمراراً."),
        ("هل تناسب الرجال والنساء؟", "نعم، مناسبة لكلا الجنسين لإزالة شعر الجسم."),
        ("هل يحتاج الجهاز لبطارية أو كهرباء؟", "لا، أداة يدوية بالكامل لا تحتاج لبطارية أو شحن."),
        ("هل العبوة مدمجة وسهلة السفر؟", "نعم، حجمها مدمج ومريح جداً لحملها في حقيبة السفر."),
        ("هل تترك ملمساً ناعماً كالحرير؟", "نعم، تقشير الجلد الميت يترك البشرة ناعمة ومشرقة فورياً."),
        ("كم مرة يُنصح باستخدامها؟", "تُستخدم مرة كل 1 إلى 2 أسابيع حسب معدل نمو الشعر."),
        ("هل تترك رائحة؟", "خالية تماماً من الكيماويات والعطور."),
        ("كيف أحتفظ بالأداة؟", "تُحفظ في مكان جاف ونظيف."),
        ("هل تزيد سمك الشعر النابت؟", "لا، لا تغير سمك الشعرة الطبيعي."),
        ("هل تصمد مع الاستخدام التكراري؟", "نعم، سطح الكريستال محفور بمتانة لا تضعف مع الماء."),
        ("هل تناسب البشرة الحساسة؟", "تُجرى تجربة بسيطة على مساحة صغيرة أولاً للبشرة الحساسة."),
        ("هل يسهل التحكم بمسكتها؟", "نعم، المقبض البلاستيكي مصمم لراحة قبضة اليد."),
        ("هل العبوة اقتصادية؟", "تغنيكِ عن الشفرات والشمع لعدة سنوات بسعر ممتاز.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Crystal Hair Eraser</strong> is the revolutionary painless physical hair removal and skin exfoliation tool. Utilizing advanced Nano-Crystalline Glass Technology, it gently buffs away surface hair and dead skin cells in light circular motions without blades, waxing, or harsh chemicals.</p>
<p>Designed to reduce strawberry legs and prevent ingrown hairs, the Crystal Hair Eraser leaves your skin touchably silky smooth and radiant within minutes. Reusable for up to 3 years, it requires no refills, charging, or maintenance.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Painless Hair Removal & Exfoliation:</strong> Buffs away hair and dead skin cells gently in circular motions.</li>
  <li><strong>Magic Nano-Crystalline Glass Tech:</strong> Breaks down surface hair smoothly without razor cuts or wax burns.</li>
  <li><strong>Prevents Ingrown Hairs & Strawberry Legs:</strong> Exfoliates rough skin texture to reduce clogged pores.</li>
  <li><strong>100% Chemical & Blade Free:</strong> Completely safe physical hair remover needing zero refills or electricity.</li>
  <li><strong>Reusable & Highly Economical:</strong> Lasts up to 3 years of regular use; easily rinsed clean with water.</li>
  <li><strong>Compact Travel Design:</strong> Ergonomic palm grip easy to carry in any beauty pouch.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Prepare):</strong> Use on dry or slightly damp skin ideally after a warm shower.</li>
  <li><strong>Step 2 (Buff):</strong> Place crystal glass surface against skin and rub gently in small circular motions without pressing hard.</li>
  <li><strong>Step 3 (Moisturize):</strong> Rinse skin with water and apply a rich hydrating body lotion immediately.</li>
  <li><strong>Step 4 (Clean Tool):</strong> Rinse the Crystal Hair Eraser with water and allow to dry.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Nano-Crystalline Glass Surface:</strong> Precision etched glass engineered to safely buff hair and dead skin.</li>
  <li><strong>Ergonomic ABS Plastic Handle:</strong> Provides a firm, non-slip palm grip.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external use on legs, arms, and back; avoid using on facial, underarm, or sensitive bikini areas.</li>
  <li>Do not apply excessive pressure to prevent skin friction redness.</li>
  <li>Keep out of reach of young children.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a painless, reusable physical hair remover and body exfoliator for smooth legs and arms.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Generic / Magic Crystal</td></tr>
  <tr><th>Category</th><td>Beauty Tools / Crystal Hair Removal</td></tr>
  <tr><th>Product Type</th><td>Nano-Crystalline Painless Physical Hair Eraser</td></tr>
  <tr><th>Volume/Weight</th><td>Single Handheld Tool</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Legs, Arms, Back)</td></tr>
  <tr><th>Finish</th><td>Silky smooth, hair-free & exfoliated skin</td></tr>
  <tr><th>Texture</th><td>Etched nano-crystalline glass surface</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-Free</td></tr>
  <tr><th>Active Ingredients</th><td>Nano-Crystalline Glass, Durable ABS Handle</td></tr>
  <tr><th>Country of Origin</th><td>China</td></tr>
  <tr><th>Manufacturer</th><td>Beauty Care Technologies</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens (15+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Nano-Crystalline Friction & Physical Hair Buffing</h2>

<h3>What problem does this solve?</h3>
<p>The Crystal Hair Eraser resolves razor cuts, wax burns, ingrown hairs, and strawberry leg texture.</p>

<h3>Why choose Crystal Hair Eraser?</h3>
<p>Etched glass micro-patterns create controlled friction that clumps and detaches surface hair strands while gently exfoliating dead skin cells.</p>"""

    en_faqs = [
        ("What is the Crystal Hair Eraser?", "It is a handheld nano-crystalline glass tool designed to physically buff away body hair and dead skin cells painlessly."),
        ("How does it work?", "Rubbed in gentle circular motions, its etched glass surface clumps and removes hair while exfoliating skin."),
        ("Does it hurt or cut skin?", "No, it is 100% painless and blade-free with zero risk of cuts or wax burns."),
        ("Does it help reduce strawberry legs and ingrown hairs?", "Yes, buffing away dead skin cells unclogs pores and prevents ingrown hairs."),
        ("What body areas can it be used on?", "Ideal for legs, arms, back, and knuckles."),
        ("Can it be used on face or bikini areas?", "Avoid using on facial, underarm, or delicate bikini areas to prevent friction redness."),
        ("How long does the tool last?", "It is reusable and lasts up to 3 years without needing refills."),
        ("Where is it manufactured?", "It is produced following precision glass etching technology."),
        ("How do I verify authenticity at Ekleel Abha?", "All beauty tools at Ekleel Abha are 100% original high-grade crystal products."),
        ("How do I clean the eraser?", "Rinse thoroughly under running water and let it air dry."),
        ("Should I moisturize after use?", "Yes, always apply body lotion after buffing to lock in moisture."),
        ("Should it be used on dry or wet skin?", "Can be used on dry or slightly damp skin after a warm shower."),
        ("Does it cause skin redness?", "If used with light pressure, it does not cause redness; avoid pressing hard."),
        ("Can both men and women use it?", "Yes, it is a unisex physical hair removal tool."),
        ("Does it require batteries or charging?", "No, it is a 100% manual tool needing no batteries or power."),
        ("Is it travel-friendly?", "Yes, compact palm size fits easily in travel beauty kits."),
        ("Does it leave skin smooth?", "Yes, physical exfoliation leaves skin touchably smooth instantly."),
        ("How often should I use it?", "Use once every 1 to 2 weeks depending on hair regrowth."),
        ("Does it contain chemicals?", "No, it is 100% chemical-free and fragrance-free."),
        ("How should I store it?", "Store in a clean, dry place."),
        ("Does it make hair grow back thicker?", "No, physical buffing leaves soft-edged regrowth unlike sharp razor shaves."),
        ("Is the glass surface durable?", "Yes, precision etched glass retains buffing friction indefinitely."),
        ("Is it safe for sensitive skin?", "Test on a small leg area first if you have sensitive skin."),
        ("Is the handle comfortable?", "Yes, its ergonomic ABS body provides an easy palm grip."),
        ("Is it an economical choice?", "Yes, replaces razors and wax refills for up to 3 years.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1763",
        "sku": "EK-1763",
        "gtin": "6878899955566",
        "category": "أجهزة ومستلزمات التجميل / إزالة الشعر الكريستالية",
        "brand": "Generic Crystal",
        "ar": {
            "title": "ممحاة شعر من كريستال",
            "meta_title": "ممحاة شعر كريستال بدون الم | صيدلية إكليل أبها",
            "meta_description": "اشتري ممحاة شعر من كريستال لإزالة الشعر وتقشير البشرة بدون ألم. تقنية النانو الكريستالية قابلة لإعادة الاستخدام. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["ممحاة_الكريستال", "ازالة_الشعر", "كريستال_الشعر", "تقشير_البشرة", "إكليل_أبها"]
        },
        "en": {
            "title": "Crystal Hair Eraser",
            "meta_title": "Crystal Hair Eraser Painless Hair Removal | Ekleel Abha",
            "meta_description": "Buy original Crystal Hair Eraser. Painless nano-crystalline hair removal & physical exfoliation tool. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["crystal_hair_eraser", "painless_hair_removal", "nano_crystal", "body_exfoliator", "ekleel_abha"]
        },
        "schema": {
            "brand": "Generic Crystal",
            "category": "Beauty Tool / Hair Eraser",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "crystal-hair-eraser.webp",
            "alt": "Crystal Hair Eraser",
            "title": "Crystal Hair Eraser"
        }
    }

def create_product_1764():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>فرشاه أسنان سيجنال للأطفال 1+1 مجاناً (Signal Toothbrush For Kids 1+1 FREE)</strong> الاختيار الطبي الأمثل والأكثر مرحاً لتأمين صحة فم وأسنان أطفالكِ اليومية. صُممت هذه الفرشاة الذكية من علامة سيجنال العالمية بشعيرات ناعمة جداً ودائرية الأطراف لحماية اللثة الرقيقة ومينا أسنان الأطفال اللبنية من الخدش أو التهيج أثناء التفريش.</p>
<p>تمتاز الفرشاة بمقبض مريح ومضاد للانزلاق مخصص لراحة يد الطفل، وتأتي بحجم رأس صغير مدمج يصل بسهولة لكافة الفتحات والأسنان الخلفية، مع عرض 1+1 مجاناً يوفر حماية مضاعفة وقيمة اقتصادية لأطفالكِ.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>شعيرات ناعمة جداً ودائرية الأطراف:</strong> تحمي لثة الأطفال الرقيقة ومينا الأسنان اللبنية من التهيج.</li>
  <li><strong>رأس صغير مخصص لفم الأطفال:</strong> يصل بسهولة للأسنان الفكية الخلفية والفراغات الضيقة.</li>
  <li><strong>مقبض مريح ومضاد للانزلاق:</strong> يسهل على الطفل الإمساك بالفرشاة وتعلّم التفريش الذاتي.</li>
  <li><strong>عرض توفيري 1+1 مجاناً:</strong> عبوة تحتوي على فرشاتين بقيمة اقتصادية ممتازة للاستخدام الممتد.</li>
  <li><strong>تصميم مرح ومبهج للأطفال:</strong> تشجع الطفل على الالتزام بروتين تفريش الأسنان اليومي.</li>
  <li><strong>خالية من المواد الضارة BPA:</strong> مصنوعة من بلاستيك طبي آمن 100% للأطفال.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق):</strong> وضعي كمية بحجم حبة البازلاء من معجون أسنان الأطفال على شعيرات فرشاة سيجنال.</li>
  <li><strong>الخطوة الثانية (التفريش):</strong> ساعدي طفلكِ على تفريش الأسنان بحركات دائرية خفيفة لمدة دقيقتين.</li>
  <li><strong>الخطوة الثالثة (الشطف):</strong> اشطفي الفم والفرشاة جيداً بالماء الفاتر وعلقيها لتجف.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>شعيرات نايلون ناعمة دائرية (Soft Rounded Nylon Bristles):</strong> تنظف المينا بلطف بدون خدش.</li>
  <li><strong>مقبض مدمج خالي من BPA:</strong> مريح ومضاد للانزلاق لأيدي الأطفال.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الفموي لتفريش الأسنان فقط تحت إشراف الوالدين.</li>
  <li>يُوصى باستبدال فرشاة الأسنان كل 2 إلى 3 أشهر.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>للأطفال والوالدين الراغبين في فرشاة أسنان طبية ناعمة ومرحة بعرض 1+1 مجاناً.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سيجنال (Signal)</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم / فرش أسنان الأطفال</td></tr>
  <tr><th>نوع المنتج</th><td>فرشاة أسنان ناعمة للأطفال (عرض 1+1 مجاناً)</td></tr>
  <tr><th>الحجم/الوزن</th><td>عبوة تحتوي على 2 فرشاة أسنان</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بأسنان الأطفال)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان لبنية نظيفة، لثة صحية ونفس منعش</td></tr>
  <tr><th>الملمس</th><td>شعيرات ناعمة جداً بمقبض مريح</td></tr>
  <tr><th>العطر</th><td>عديم الرائحة</td></tr>
  <tr><th>المكونات النشطة</th><td>شعيرات نايلون دائرية، مقبض مطاطي خالي من BPA</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا / المملكة العربية السعودية (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (سيجنال)</td></tr>
  <tr><th>الفئة العمرية</th><td>الأطفال (من 2 إلى 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي للعناية بأسنان الأطفال وفرشاة سيجنال (Signal Kids)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تحل فرشاة سيجنال للأطفال مشكلة انزعاج الأطفال من شعيرات الفرش القاسية وتراكم البلاك والتسوس على الأسنان اللبنية.</p>

<h3>لماذا يحدث تسوس الأسنان اللبنية؟</h3>
<p>يتسبب تراكم السكريات والبكتيريا بين أسنان الأطفال في فرز أحماض تنقر المينا اللبنية وتسبب الآلام والتسوس.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التفريش دقيقتين:</strong> شجعي طفلكِ على تفريش الأسنان دقيقتين كاملتين مرتين يومياً.<br>
2. <strong>استخدام معجون للأطفال:</strong> وضعي كمية بحجم حبة البازلاء من معجون فلورايد الأطفال.<br>
3. <strong>التغيير الدوري:</strong> استبدلي فرشاة الأسنان كل 2 إلى 3 أشهر لضمان سلامة الشعيرات.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الأسنان اللبنية ليست مهمة لأنها ستتبدل."<br>
<strong>الحقيقة:</strong> العناية بالأسنان اللبنية تحافظ على موقع الفك وتضمن نمواً سليماً للأسنان الدائمة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تقوم الشعيرات النايلونية النايلونية دائرية الأطراف بمسح البيوفلم والبكتيريا عن أسطح المينا اللبنية، دون إحداث جروح في الأنسجة اللثوية الرقيقة للأطفال.</p>"""

    faqs = [
        ("ما هي فرشاه أسنان سيجنال للأطفال 1+1 مجاناً؟", "هي عبوة توفيرية تحتوي على فرشاتين ناعمتين لأسنان الأطفال بشعيرات دائرية لحماية اللثة ومينا الأسنان اللبنية."),
        ("هل الشعيرات ناعمة وآمنة على لثة الأطفال؟", "نعم، شعيرات ناعمة جداً ودائرية الأطراف لحماية لثة ومينا أسنان الأطفال."),
        ("ما هي الفئة العمرية المناسبة للفرشاة؟", "مناسبة للأطفال من سن 2 إلى 12 سنة."),
        ("هل العبوة تحتوي على 2 فرشاة؟", "نعم، تأتي بعرض 1+1 مجاناً (فرشاتين بسعر واحدة)."),
        ("ما هو بلد صنع سيجنال؟", "صُنع بواسطة شركة يونيلفر (Unilever) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات سيجنال لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل المقبض مضاد للانزلاق؟", "نعم، مقبض مريح ومطاطي يسهل تحكم يد الطفل أثناء التفريش."),
        ("هل الفرشاة خالية من BPA؟", "نعم، مصنوعة من مواد بلاستيكية طبية آمنة خالية من BPA."),
        ("كم مرة يُفضل تغيير فرشاة الأسنان؟", "يُوصى بتغيير فرشاة الأسنان كل 2 إلى 3 أشهر لضمان أقصى حماية."),
        ("هل تشجع الأطفال على التفريش؟", "نعم، تصاميمها وألوانها المرحة تشجع الأطفال على العناية بأسنانهم يومياً."),
        ("هل يصل رأس الفرشاة للأسنان الخلفية؟", "نعم، رأس مدمج وصغير ينزلق للأسنان الفكية بسهولة."),
        ("كيف أحتفظ بالفرشاة بعد التفريش؟", "تُشطف بالماء وتُعلق رأسياً لتجف."),
        ("هل تناسب الأسنان اللبنية والدائمة؟", "نعم، تنظف الأسنان اللبنية والدائمة اللطيفة بفاعلية."),
        ("هل يحتاج الطفل لإشراف الوالدين؟", "يُفضل إشراف الوالدين للأطفال دون 6 سنوات لضمان تفريش صحيح."),
        ("هل تسبب نزيف اللثة؟", "شعيراتها الناعمة تمنع نزيف أو جرح اللثة تماماً."),
        ("هل العبوة اقتصادية؟", "نعم، عرض 1+1 يوفر حماية مضاعفة بسعر مميز."),
        ("هل تتوفر بألوان متعددة؟", "تأتي بألوان مبهجة تناسب الأولاد والبنات."),
        ("هل تمنع تسوس الأسنان اللبنية؟", "تنظيف البلاك بانتظام بالفرشاة يقي الأسنان اللبنية من التسوس."),
        ("هل يمكن استخدامها مع معجون سيجنال للأطفال؟", "نعم، يفضل استخدامها مع معجون سيجنال بالفلورايد للأطفال لنتائج مضاعفة."),
        ("هل الشعيرات متينة ولا تتفتت؟", "نعم، نايلون ناعم ومتين ينظف بكفاءة."),
        ("هل تناسب الأطفال ذوي اللثة الحساسة؟", "نعم، خيار طبي ممتاز للثة الحساسة."),
        ("هل العبوة غلافها محكم؟", "تأتي في عبوة مغلفة طبياً."),
        ("ما هي مدة التفريش الموصى بها؟", "دقيقتين كاملتين مرتين يومياً."),
        ("هل رأس الفرشاة مرن؟", "مصمم بزاوية مرنة ينزلق في الفم."),
        ("هل تساعد في تعلم الطفل العناية المستقلة؟", "نعم، المقبض المطاطي يسهل التعلم الذاتي.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Signal Toothbrush For Kids 1+1 FREE</strong> is the premier dentist-recommended oral care choice designed to protect your child's developing teeth and delicate gums. Featuring ultra-soft rounded bristles, it gently sweeps away dental plaque from milk teeth without scratching enamel or irritating sensitive gum tissue.</p>
<p>Designed with an ergonomic anti-slip handle custom-built for small hands, its compact brush head easily reaches back molars. Available in a 1+1 FREE value pack, it offers double the protection and exceptional value for your family's oral hygiene routine.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Ultra-Soft Rounded Bristles:</strong> Protect delicate primary milk teeth enamel and sensitive gums.</li>
  <li><strong>Compact Child-Sized Brush Head:</strong> Reaches back molars and tight interdental spaces effortlessly.</li>
  <li><strong>Ergonomic Anti-Slip Grip:</strong> Fits comfortably in small hands to encourage independent brushing.</li>
  <li><strong>Double Pack Value 1+1 FREE:</strong> Includes 2 toothbrushes for long-lasting family oral protection.</li>
  <li><strong>Fun Child-Friendly Design:</strong> Makes daily morning and evening brushing fun for kids.</li>
  <li><strong>100% BPA-Free Safe Plastic:</strong> Made from food-grade medical materials safe for children.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply):</strong> Apply a pea-sized amount of children's fluoride toothpaste onto Signal bristles.</li>
  <li><strong>Step 2 (Brush):</strong> Guide child to brush teeth gently in circular motions for at least 2 minutes.</li>
  <li><strong>Step 3 (Rinse):</strong> Rinse mouth and brush thoroughly with warm water, then store upright to dry.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Soft Rounded Nylon Bristles:</strong> Gently polish milk teeth enamel without scratching.</li>
  <li><strong>Ergonomic BPA-Free Rubberized Handle:</strong> Anti-slip grip designed for child hand sizes.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For oral brushing use only under adult supervision.</li>
  <li>Replace toothbrush every 2 to 3 months.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Parents seeking dentist-recommended soft kids toothbrushes in a 1+1 FREE value pack.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Signal</td></tr>
  <tr><th>Category</th><td>Oral Care / Kids Toothbrushes</td></tr>
  <tr><th>Product Type</th><td>Ultra-Soft Kids Toothbrush 1+1 FREE Pack</td></tr>
  <tr><th>Volume/Weight</th><td>Twin Toothbrush Pack (2 Pieces)</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Child Dental Care)</td></tr>
  <tr><th>Finish</th><td>Clean milk teeth, healthy gums & fresh breath</td></tr>
  <tr><th>Texture</th><td>Ultra-soft rounded bristles with rubberized grip</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-Free</td></tr>
  <tr><th>Active Ingredients</th><td>Rounded Soft Nylon Bristles, BPA-Free Rubber</td></tr>
  <tr><th>Country of Origin</th><td>France / Saudi Arabia (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever (Signal)</td></tr>
  <tr><th>Age Group</th><td>Kids (Ages 2 to 12)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Primary Teeth Care & Soft Bristles</h2>

<h3>What problem does this solve?</h3>
<p>Signal Toothbrush For Kids resolves toothbrush resistance, gum irritation, and plaque buildup on primary milk teeth.</p>

<h3>Why choose Signal Kids?</h3>
<p>Ultra-soft rounded bristles and a compact head glide smoothly around delicate primary enamel without causing gingival bleeding.</p>"""

    en_faqs = [
        ("What is Signal Toothbrush For Kids 1+1 FREE?", "It is a twin pack of soft kids toothbrushes featuring rounded bristles to protect primary teeth and gums."),
        ("Are bristles safe for child gums?", "Yes, ultra-soft rounded bristles protect milk teeth enamel and delicate gums."),
        ("What age group is this toothbrush for?", "Suitable for children aged 2 to 12 years old."),
        ("Does it contain 2 toothbrushes?", "Yes, it comes in a 1+1 FREE value pack containing 2 toothbrushes."),
        ("Where is Signal manufactured?", "It is produced by Unilever following global oral care standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Signal products at Ekleel Abha are 100% original from certified distributors."),
        ("Is the handle anti-slip?", "Yes, it features an ergonomic rubberized grip designed for small hands."),
        ("Is it BPA-free?", "Yes, made from 100% child-safe BPA-free materials."),
        ("How often should the toothbrush be replaced?", "Replace toothbrushes every 2 to 3 months."),
        ("Does it encourage children to brush?", "Yes, fun vibrant designs motivate kids to maintain daily brushing habits."),
        ("Does the brush head reach back molars?", "Yes, its compact head easily reaches back molars."),
        ("How should I store it after brushing?", "Rinse with water and store upright in a toothbrush holder to air dry."),
        ("Is it suitable for primary and permanent teeth?", "Yes, cleans primary milk teeth and emerging permanent teeth gently."),
        ("Should parents supervise brushing?", "Adult supervision is recommended for children under 6 years old."),
        ("Does it cause gum bleeding?", "No, soft rounded bristles prevent gum scratches and bleeding."),
        ("Is the 1+1 pack economical?", "Yes, offers double the value at an affordable price."),
        ("Does it come in different colors?", "Yes, available in bright colors for boys and girls."),
        ("Does it prevent cavities in milk teeth?", "Yes, regular plaque removal guards milk teeth against decay."),
        ("Can it be paired with Signal Kids Toothpaste?", "Yes, pairing with Signal fluoride kids toothpaste maximizes cavity protection."),
        ("Are bristles durable?", "Yes, high-quality nylon bristles clean effectively without fraying quickly."),
        ("Is it good for sensitive child gums?", "Yes, highly recommended for sensitive gums."),
        ("Is the packaging hygienic?", "Yes, sealed in sterile blister packaging."),
        ("What is recommended brushing time?", "Brush for 2 full minutes twice daily."),
        ("Is the brush neck flexible?", "Designed with a flexible angle gliding easily in small mouths."),
        ("Does it foster independent brushing habits?", "Yes, the rubberized grip helps children master self-brushing.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1764",
        "sku": "EK-1764",
        "gtin": "6281006524439",
        "category": "العناية بالفم / فرش أسنان الأطفال",
        "brand": "Signal",
        "ar": {
            "title": "فرشاه أسنان سيجنال للأطفال 1+1 مجاناً",
            "meta_title": "فرشاة اسنان سيجنال للاطفال 1+1 مجاناً | صيدلية إكليل أبها",
            "meta_description": "اشتري فرشاه أسنان سيجنال للأطفال 1+1 مجاناً. شعيرات ناعمة دائرية لحماية اللثة والأسنان اللبنية. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["سيجنال", "فرشاة_سيجنال", "أسنان_الأطفال", "توفير_1+1", "إكليل_أبها"]
        },
        "en": {
            "title": "Signal Toothbrush For Kids 1+1 FREE",
            "meta_title": "Signal Toothbrush For Kids 1+1 FREE | Ekleel Abha Pharmacy",
            "meta_description": "Buy Signal Toothbrush For Kids 1+1 FREE. Soft rounded bristles for milk teeth & delicate gums. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["signal", "kids_toothbrush", "milk_teeth", "twin_pack", "ekleel_abha"]
        },
        "schema": {
            "brand": "Signal",
            "category": "Oral Care / Kids Toothbrush",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "signal-toothbrush-for-kids-1-plus-1-free.webp",
            "alt": "Signal Toothbrush For Kids 1+1 FREE",
            "title": "Signal Toothbrush For Kids 1+1 FREE"
        }
    }

def build_disposable_towel_product(prod_id, dimensions_str, pcs_cnt, gtin, img_slug):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>مناشف للاستعمال مرة واحدة من وورلد كير - مقاس {dimensions_str} سم ({pcs_cnt} قطعة) (World Care Disposable Towels)</strong> الحل الصحي المعقم والأكثر فخامة وسهولة للاستخدام الشخصي وفي صالونات التجميل والنوادي والسفر. صُنعت هذه المناشف من ألياف نباتية فائقة الامتصاص والنعومة بوزن وقوة متينة، حيث تمتص الماء والسوائل بكفاءة تماثل المناشف القطنية التقليدية دون تفتت أو تمزق أثناء البلل.</p>
<p>تضمن مناشف وورلد كير النظافة التامة والوقاية الفائقة من انتقال البكتيريا والجراثيم، حيث تستخدم لمرة واحدة وتتخلصين منها بأمان، مما يغنيكِ عن غسيل المناشف القماشية ويعزز مستوى العناية الصحية اليومية.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>مناشف معقمة للاستعمال المرة الواحدة:</strong> تضمن حماية كاملة من العدوى والبكتيريا بين الاستخدامات.</li>
  <li><strong>امتصاص فائق للماء والسوائل:</strong> ألياف نباتية فائقة الامتصاص تمتص الرطوبة في ثوانٍ.</li>
  <li><strong>متينة وقوية ولا تتفتت:</strong> نسيج متماسك لا يتمزق أو يترك وبر على البشرة أثناء البلل.</li>
  <li><strong>ملمس ناعم ولطيف على البشرة:</strong> ناعمة جداً على الوجه والجسم ومناسبة للبشرة الحساسة.</li>
  <li><strong>مقاس عملي {dimensions_str} سم ({pcs_cnt} قطعة):</strong> حجم مثالي للتجفيف في المنازل، الصالونات، والنوادي بالسفر.</li>
  <li><strong>عبوة اقتصادية وحفظ صحي:</strong> عبوة سهلة الفتح تحفظ المناشف من الغبار والتلوث.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (السحب):</strong> اسحبي منشفة واحدة من عبوة مناشف وورلد كير.</li>
  <li><strong>الخطوة الثانية (التجفيف):</strong> استخدمي المنشفة لتجفيف الوجه، الأيدي، الجسم، أو الشعر بعد الاستحمام أو الغسيل.</li>
  <li><strong>الخطوة الثالثة (التخلص الآمن):</strong> تخلصي من المنشفة المستعملة في سلة المهملات؛ ولا تعيدي استخدامها.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>ألياف سلولوزية نباتية 100% (100% Plant Cellulosic Fibers):</strong> فائقة الامتصاص والنعومة والصديقة للبشرة.</li>
  <li><strong>نسيج مضغوط بدون بوليستر قاسي:</strong> يمنح مرونة وتماسكاً دون وبر.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي للتجفيف فقط.</li>
  <li>تُحفظ في مكان جاف ونظيف بعيداً عن الرطوبة.</li>
  <li>تخلصي من المنشفة في سلة المهملات ولا ترميها في المرحاض.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحثون عن مناشف صحية معقمة للاستعمال مرة واحدة في السفر، النوادي، الصالونات، والمنزل.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>وورلد كير (World Care)</td></tr>
  <tr><th>الفئة</th><td>المستلزمات الشخصية / المناشف الصحية للاستعمال مرة واحدة</td></tr>
  <tr><th>نوع المنتج</th><td>مناشف صحية معقمة للاستعمال مرة واحدة (مقاس {dimensions_str} سم)</td></tr>
  <tr><th>الحجم/الوزن</th><td>عبوة تحتوي على {pcs_cnt} منشفة</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (الوجه، الجسم، الأيدي، الشعر)</td></tr>
  <tr><th>المظهر النهائي</th><td>تجفيف تام، ناعم، وخالٍ من الرطوبة والبكتيريا</td></tr>
  <tr><th>الملمس</th><td>نسيج قطني ناعم فائق الامتصاص</td></tr>
  <tr><th>العطر</th><td>عديم الرائحة (عديم العطور)</td></tr>
  <tr><th>المكونات النشطة</th><td>ألياف سلولوز نباتية 100%</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الصين</td></tr>
  <tr><th>الشركة المصنعة</th><td>World Care Hygienic Products</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لأهمية المناشف ذات الاستعمال الواحد (World Care)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تحل مناشف وورلد كير مشكلة انتقال البكتيريا والميكروبات عبر المناشف القماشية المشتركة أو الرطبة، وتمنح تجفيفاً صحياً ناعماً.</p>

<h3>لماذا يحدث نقل البكتيريا عبر المناشف القماشية؟</h3>
<p>لأن رطوبة المناشف القماشية توفر بيئة خصبة لتكاثر البكتيريا والفطريات، مما ينقل العدوى ويسبب حب الشباب وتسلخات الجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام منشفة جديدة معقمة:</strong> استعملي منشفة جديدة لكل عملية تجفيف.<br>
2. <strong>التجفيف بالربت اللطيف:</strong> جففي الوجه بالربت الخفيف بدلاً من الفرك القسري.<br>
3. <strong>التخلص في سلة المهملات:</strong> ارمي المنشفة المستعملة في سلة المهملات فوراً.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "المناشف ذات الاستعمال الواحد تتفتت وتتمزق بالماء."<br>
<strong>الحقيقة:</strong> مناشف وورلد كير مصنوعة من ألياف نباتية مضغوطة فائقة المتانة تماثل المناشف القطنية دون تفتت.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتمتع الألياف السلولوزية النباتية بخاصية اسموزية عالية تمتص الماء والرطوبة من البشرة في ثوانٍ، مع توفير نسيج خالي من الميكروبات تمنع ظهور الحبوب.</p>"""

    faqs = [
        (f"ما هي مناشف للاستعمال مرة واحدة من وورلد كير - مقاس {dimensions_str} سم؟", f"هي مناشف صحية معقمة عالية الامتصاص مخصصة للاستخدام الشخصي والصالونات والسفر مقاس {dimensions_str} سم بحجم {pcs_cnt} قطعة."),
        ("ما هي فوائد استخدام المناشف ذات الاستعمال الواحد؟", "تضمن نظافة معقمة 100%، تمنع نقل البكتيريا وحب الشباب، وتوفر عناء الغسيل."),
        ("هل المناشف ناعمة وتمتص الماء بفاعلية؟", "نعم، مصنوعة من ألياف نباتية فائقة الامتصاص تمتص الماء في ثوانٍ وتماثل المناشف القطنية."),
        (f"كم قطعة تحتوي هذه العبوة؟", f"تحتوي العبوة على {pcs_cnt} قطعة منشفة معقمة."),
        (f"ما هو مقاس المنشفة؟", f"تأتي بمقاس {dimensions_str} سم."),
        ("هل تتفتت المنشفة أو تترك وبر أثناء البلل؟", "لا، نسيجها متين ومضغوط لا يتفتت أو يترك وباراً على الوجه والجسم."),
        ("هل تناسب البشرة الحساسة وبشرة الوجه؟", "نعم، ناعمة جداً وخالية من العطور والمواد القاسية وممتازة للبشرة الحساسة."),
        ("ما هو بلد صنع مناشف وورلد كير؟", "تم تصنيعها وفق أعلى معايير الجودة والنظافة الصحية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات وورلد كير لدى إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل تناسب الاستخدام في السفر والنوادي والصالونات؟", "نعم، مثالية وعملية جداً للسفر، والرحلات، والنوادي الرياضية، وصالونات التجميل."),
        ("هل يمكن استخدامها لتجفيف الشعر؟", "نعم، ممتازة جداً لتجفيف الشعر والوجه والجسم بفاعلية."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان جاف ونظيف بعيداً عن الرطوبة."),
        ("هل ترمى المناشف في المرحاض؟", "لا، تُرمى في سلة المهملات تفادياً لانسداد الأنابيب."),
        ("هل هي خالية من البوليستر القاسي؟", "نعم، مصنوعة من ألياف نباتية ناعمة وصديقة للبشرة."),
        ("هل تساعد في الحد من حب الشباب؟", "نعم، استخدام منشفة جديدة معقمة يمنع إعادة البكتيريا للوجه."),
        ("هل يناسب جميع الأعمار؟", "نعم، مناسب للبالغين والأطفال."),
        ("هل العبوة محكمة الحفظ؟", "نعم، العبوة تحفظ المناشف من الغبار والتلوث."),
        ("هل تناسب العناية بالرضع؟", "نعم، نسيجها المعقم النقي آمن للبشرة الرقيقة."),
        ("هل تتمدد المنشفة عند البلل؟", "تحافظ على تماسكها ومقاسها دون تمدد مفرط."),
        ("هل تصمد مع المسح والتجفيف القوي؟", "نعم، نسيج متين يتحمل المسح والتجفيف بسهولة."),
        ("هل تتوفر بمقاسات مختلفة لدى إكليل أبها؟", "نعم، تتوفر بمقاسات متعددة تناسب الوجه والجسم والشعر."),
        ("هل هي خيار اقتصادي؟", "نعم، توفر تكاليف غسيل وتطهير المناشف التقليدية."),
        ("هل خالية من المعطرات؟", "نعم، خالية تماماً من العطور والمواد الكيميائية."),
        ("هل تناسب العناية بالأظافر والبديكير؟", "نعم، ممتازة جداً لمركز البديكير والمانيكير بالصالونات."),
        ("هل العبوة سهلة السحب؟", "نعم، سحب مريح وسهل لمنشفة واحدة في كل مرة.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>World Care Disposable Towels - Size {dimensions_str} cm ({pcs_cnt} Pieces)</strong> offer the ultimate hygienic, sterile, and luxurious drying solution for personal home use, salons, gyms, and travel. Crafted from 100% plant cellulosic micro-fibers, these towels deliver high absorbency equivalent to premium cotton towels without tearing or lint shedding when wet.</p>
<p>Providing 100% sterile protection against bacterial cross-contamination, World Care disposable towels eliminate the hassle of laundering fabric towels, elevating your daily skincare and personal hygiene standards.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Hygienic Disposable Towels:</strong> Ensures sterile, single-use protection against bacterial cross-contamination.</li>
  <li><strong>Ultra-High Absorbency:</strong> Plant cellulosic fibers absorb water and moisture in seconds.</li>
  <li><strong>Tear-Resistant & Lint-Free:</strong> Durable non-woven texture that will not tear or leave lint on skin.</li>
  <li><strong>Ultra-Soft Skin Touch:</strong> Hypoallergenic, soft touch safe for sensitive facial and body skin.</li>
  <li><strong>Convenient Size {dimensions_str} cm ({pcs_cnt} Pcs):</strong> Ideal dimensions for drying face, hands, body, or hair.</li>
  <li><strong>Hygienic Protective Packaging:</strong> Easy-dispense pack keeping unused towels clean and dust-free.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Dispense):</strong> Pull a single disposable towel from the World Care package.</li>
  <li><strong>Step 2 (Dry):</strong> Use to gently dry face, hands, body, or hair after showering or cleansing.</li>
  <li><strong>Step 3 (Dispose):</strong> Discard used towel responsibly in a waste bin; do not reuse.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>100% Plant Cellulosic Fibers:</strong> Highly absorbent, skin-friendly, non-woven plant fiber weave.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external drying application only.</li>
  <li>Store in a clean, dry place away from moisture.</li>
  <li>Dispose of in a trash bin; do not flush down toilets.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking 100% sterile, ultra-absorbent disposable towels for travel, gyms, salons, and home skincare.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>World Care</td></tr>
  <tr><th>Category</th><td>Personal Care / Disposable Hygienic Towels</td></tr>
  <tr><th>Product Type</th><td>Sterile Disposable Towels (Size {dimensions_str} cm)</td></tr>
  <tr><th>Volume/Weight</th><td>Pack of {pcs_cnt} Towels</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Face, Hands, Body, Hair)</td></tr>
  <tr><th>Finish</th><td>Completely dry, soft & hygienic skin</td></tr>
  <tr><th>Texture</th><td>Ultra-absorbent soft non-woven plant texture</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-Free</td></tr>
  <tr><th>Active Ingredients</th><td>100% Plant Cellulosic Fibers</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / China</td></tr>
  <tr><th>Manufacturer</th><td>World Care Hygienic Products</td></tr>
  <tr><th>Age Group</th><td>All Ages</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Plant Cellulosic Fibers & Single-Use Hygiene</h2>

<h3>What problem does this solve?</h3>
<p>World Care Disposable Towels resolve bacterial cross-contamination, acne flare-ups, and laundry hassle associated with damp fabric towels.</p>

<h3>Why choose World Care?</h3>
<p>Sterile non-woven plant fibers absorb dermal water rapidly, providing single-use hygiene that prevents bacterial transfer onto facial skin.</p>"""

    en_faqs = [
        (f"What are World Care Disposable Towels - Size {dimensions_str} cm?", f"They are sterile, highly absorbent single-use towels sized {dimensions_str} cm in a {pcs_cnt}-piece pack for personal, travel, and salon care."),
        ("What are the benefits of disposable towels?", "They ensure 100% sterile hygiene, prevent bacterial cross-contamination, and eliminate laundry hassle."),
        ("Are these towels soft and absorbent?", "Yes, made from 100% plant cellulosic fibers, they absorb water in seconds just like cotton towels."),
        (f"How many towels are in this pack?", f"This pack contains {pcs_cnt} sterile disposable towels."),
        (f"What dimensions do these towels have?", f"They measure {dimensions_str} cm."),
        ("Do they tear or shed lint when wet?", "No, their durable non-woven weave will not tear or shed lint on skin."),
        ("Are they safe for sensitive facial skin?", "Yes, hypoallergenic and fragrance-free, making them ideal for sensitive skin and acne care."),
        ("Where are World Care towels manufactured?", "They are manufactured under strict hygiene standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All World Care products at Ekleel Abha are 100% original."),
        ("Are they good for travel, gyms, and salons?", "Yes, perfect for travel, gym workouts, spa treatments, and beauty salons."),
        ("Can they be used for hair drying?", "Yes, excellent for drying hair, face, hands, and body."),
        ("How should I store the pack?", "Store in a dry, clean place away from moisture."),
        ("Can they be flushed down the toilet?", "No, dispose of used towels in a trash bin to avoid plumbing clogs."),
        ("Are they free of harsh polyester?", "Yes, made from soft plant-based cellulosic fibers."),
        ("Do they help reduce acne flare-ups?", "Yes, using a fresh sterile towel prevents re-introducing bacteria onto facial skin."),
        ("Are they safe for all ages?", "Yes, suitable for adults, kids, and infants."),
        ("Is the packaging hygienic?", "Yes, packaged to protect unused towels from dust and contamination."),
        ("Are they safe for baby care?", "Yes, their pure sterile texture is gentle enough for baby skin."),
        ("Do they hold shape when wet?", "Yes, they retain structure and absorbency without stretching."),
        ("Can they withstand firm drying?", "Yes, strong non-woven fabric handles firm wiping easily."),
        ("Are different sizes available at Ekleel Abha?", "Yes, available in various sizes for face, body, and hair drying."),
        ("Are they an economical choice?", "Yes, saves laundry costs and offers convenient hygiene."),
        ("Are they fragrance-free?", "Yes, completely free of artificial perfumes and chemicals."),
        ("Are they great for nail salons and pedicures?", "Yes, widely preferred in professional manicure and pedicure centers."),
        ("Is the pack easy to dispense?", "Yes, features an easy single-towel pull dispenser.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "المستلزمات الشخصية / المناشف الصحية للاستعمال مرة واحدة",
        "brand": "World Care",
        "ar": {
            "title": f"مناشف للاستعمال مرة واحدة من وورلد كير - مقاس {dimensions_str}  {pcs_cnt}قطعة",
            "meta_title": f"مناشف وورلد كير {dimensions_str}سم {pcs_cnt}حبة | صيدلية إكليل أبها",
            "meta_description": f"اشتري مناشف للاستعمال مرة واحدة من وورلد كير - مقاس {dimensions_str} سم ({pcs_cnt} قطعة). معقمة، ناعمة، وفائقة الامتصاص للسفر والصالونات. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["وورلد_كير", "مناشف_استعمال_واحد", "مناشف_معقمة", "مناشف_سفر", "إكليل_أبها"]
        },
        "en": {
            "title": f"World Care Disposable Towels - Size {dimensions_str} cm, {pcs_cnt} Pieces",
            "meta_title": f"World Care Disposable Towels {dimensions_str}cm {pcs_cnt}Pcs | Ekleel Abha",
            "meta_description": f"Buy World Care Disposable Towels (Size {dimensions_str} cm, {pcs_cnt} Pcs). Sterile, soft, ultra-absorbent towels for travel & salons. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["world_care", "disposable_towels", "sterile_towels", "travel_towels", "ekleel_abha"]
        },
        "schema": {
            "brand": "World Care",
            "category": "Personal Care / Disposable Towel",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"{img_slug}.webp",
            "alt": f"World Care Disposable Towels Size {dimensions_str} cm {pcs_cnt} Pieces",
            "title": f"World Care Disposable Towels Size {dimensions_str} cm {pcs_cnt} Pieces"
        }
    }

print("Loaded Batch 13 builders")
