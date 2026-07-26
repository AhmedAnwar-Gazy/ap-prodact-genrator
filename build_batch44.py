import json, os

def _make_moroccan_black_soap_variant(pid, gtin, ar_name, en_name, ingredient_ar, ingredient_en, benefit_ar, benefit_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> الصابون البلدي المغربي الفاخر بحجم ضخم (500 جم) المصنوع بتركيبة الحمام المغربي والسبا الأصيلة لتنظيف وتطهير وتقشير وتفتيح بشرة الجسم بكفاءة ملكية. يرتكز هذا الصابون البلدي الأصيل ({en_name}) على زيت الزيتون الأسود الطبيعي (Black Olive Oil)، زيت {ingredient_ar}، والركائز المغذية للبشرة.</p>
<p>يعمل الصابون البلدي المغربي على تليين خلايا الجلد الميتة والتراكمات الجافة، تنظيف الفروة والمسام عمقاً، وإزالة السموم من الجسم مع {benefit_ar}، ليترك جسمك ناعماً كالحرير، ناصع النظافة، موحد اللون، وجاهزاً للتقشير المثالي بالليفة المغربية.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تليين وإزالة خلايا الجلد الميتة والتراكمات:</strong> يجهز الجسم للتقشير العميق بالليفة المغربية.</li>
  <li><strong>تنظيف وتطهير مسام الجسم بالكامل:</strong> يزيل السموم والزيوت الزائدة والتلوث.</li>
  <li><strong>مدعم بـ {ingredient_ar} وزيت الزيتون الأسود:</strong> {benefit_ar} وتغذي طبقات الجلد.</li>
  <li><strong>يمنح الجسم ملمساً ناعماً حريرياً:</strong> يرطب البشرة ويحميها من الجفاف.</li>
  <li><strong>عبوة اقتصادية ضخمة 500 جم:</strong> كمية وافرة تكفي لعدة أشهر من الاستخدام المنتظم.</li>
  <li><strong>صنع بتركيبة الحمام المغربي الأصيلة 100%:</strong> تراث مغربي ملكي في العناية والسبا.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (البخار والبلل):</strong> اجلسي في حمام دافئ مليء بالبخار لفتح مسام الجسم وتليين الجلد.</li>
  <li><strong>الخطوة الثانية (التطبيق والانتظار):</strong> وزعي الصابون البلدي على كامل الجسم واتركيه لمدة 10-15 دقيقة.</li>
  <li><strong>الخطوة الثالثة (الفرك والشطف):</strong> اشطفي الصابون بالماء الدافئ ثم افركي الجسم بالليفة المغربية لإزالة الجلد الميت (يُستعمل 1-2 مرة أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الزيتون الأسود الطبيعي:</strong> يلين خلايا الجلد القرنية الميتة ويغذي البشرة بمضادات الأكسدة.</li>
  <li><strong>خلاصة وزيت {ingredient_ar}:</strong> {benefit_ar} وتمنح الجسم عطراً ونقاءً ملكياً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم فقط (لا يُستعمل للوجه).</li>
  <li>تجنبي التلامس مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لروتين الحمام المغربي والسبا وتنظيف وتفتيح الجسم 500 جم.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>العلامة التجارية المعتمدة للصابون البلدي</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / الصابون البلدي المغربي الفاخر بـ {ingredient_ar} 500g</td></tr>
  <tr><th>نوع المنتج</th><td>صابون بلدي مغربي طبيعي بزيت الزيتون وزيت {ingredient_ar} (500g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (بما في ذلك البشرة الجافة والمفتقرة للنضارة)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، ناصع النظافة، موحد اللون وجاهز للتقشير المغربي</td></tr>
  <tr><th>الملمس</th><td>معجون صابوني أسود/داكن ناعم دسم ينزلق برفق</td></tr>
  <tr><th>العطر</th><td>عطر {ingredient_ar} والزيتون المغربي الأصيل</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت زيتون أسود، زيت {ingredient_ar}، بوتاسيوم هيدروكسيد زيتي</td></tr>
  <tr><th>بلد المنشأ</th><td>المغرب (Morocco)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Moroccan Black Soap Products</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد الصابون البلدي المغربي بـ {ingredient_ar} وزيت الزيتون</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج الصابون البلدي المغربي مشكلة التراكمات الجافة الصعبة على الجسم، انسداد المسامات العميق، واسمرار وجفاف جلد الجسم.</p>

<h3>لماذا تنجح تركيبة الصابون البلدي المغربي؟</h3>
<p>لأن التحلل الصابوني لزيت الزيتون ينتج صابوناً قلوياً خفيفاً يذيب الدهون والتراكمات دون تدمير الطبقة الدهنية الحامية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام في بيئة دافئة مليئة بالبخار:</strong> يضاعف تليين الجلد الميت وتفتيح المسام.<br>
2. <strong>الفرك بالليفة المغربية بعد الشطف الكامل للصابون:</strong> الفرك فوق الصابون يقلل الاحتكاك المطلوب للتقشير.<br>
3. <strong>الترطيب بـ زيت الأركان بعد الحمام:</strong> يحافظ على أقصى درجات النعومة والمرونة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الصابون البلدي المغربي يصبغ الجلد بلون أسود."<br>
<strong>الحقيقة:</strong> لونه الأسود ناتج طبيعياً عن زيت الزيتون الأسود وينشطف تماماً دون ترك أي أثر لون على الجلد.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعمل الصابون البلدي كمطري (Emollient) يمتص الماء داخل طبقات الجلد القرنية الجافة فتنتفخ وتتفكك، مما يسهل فركها بالليفة.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو الصابون البلدي المغربي الطبيعي الأصيل بـ {ingredient_ar} وزيت الزيتون الأسود بحجم 500 جم للتنظيف والتقشير المغربي."),
        (f"ما هي فوائد زيت الزيتون الأسود و{ingredient_ar}؟", f"يلين زيت الزيتون الجلد الميت والتراكمات، بينما {benefit_ar} وتغذي طبقات الجلد."),
        ("هل يجهز الجسم للتقشير بالليفة المغربية؟", "نعم، يلين الجلد الميت والتراكمات الجافة ليجعل التقشير بالليفة سهلاً وفائق الفاعلية."),
        ("ما وزن العبوة؟", "تأتي بعبوة ضخمة بوزن 500 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اجلسي في البخار، وزعي الصابون 10-15 دقيقة، اشطفي بالماء ثم افركي بالليفة المغربية 1-2 مرة أسبوعياً."),
        ("هل هو أصلي صُنِع في المغرب؟", "نعم، صُنع في المغرب بتركيبة الحمام المغربي الأصيلة 100%."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات الصابون البلدي لدى إكليل أبها أصلية 100%."),
        ("هل يترك الجسم ناعماً كالحرير؟", "نعم، يمنح الجسم ملمساً حريرياً ناعماً جداً ونظافة ناصعة."),
        (f"ما رائحة {ar_name}؟", f"عطر {ingredient_ar} والزيتون المغربي الفاخر."),
        ("هل يناسب جميع أنواع بشرة الجسم؟", "نعم، مناسب لجميع أنواع بشرة الجسم."),
        ("هل 500 جم تدوم طويلاً؟", "نعم، عبوة ضخمة تكفي لعدة أشهر من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف محكم الإغلاق."),
        ("هل يناسب الوجه؟", "مخصص لبشرة الجسم فقط ولا يُستعمل لبشرة الوجه."),
        ("كم مرة أسبوعياً؟", "1-2 مرة أسبوعياً في الحمام المغربي."),
        ("هل يزيل السموم والزيوت الزائدة؟", "نعم، ينظف المسام العميقة ويزيل السموم والزيوت الزائدة."),
        ("هل الصابون البلدي علامة مغربية تاريخية؟", "نعم، الصابون البلدي هو أساس العناية والسبا المغربي منذ مئات السنين."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب الاستخدام قبل التان والمناسبات؟", "نعم، ينظف ويهيئ البشرة تماماً للتان والمناسبات."),
        ("هل يمنح توحيداً للون البشرة؟", "نعم، إزالة التراكمات الميتة تمنح توحيداً وإشراقاً فورياً للون الجسم."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للنساء والرجال من 16 سنة."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، ينشطف بالماء الدافئ بسلاسة دون أثر لزج."),
        ("هل يصلح هدية فاخرة للعرايس؟", "نعم، هدية ملكية فاخرة جداً للعرايس والسبا."),
        ("هل يساعد في تنشيط الدورة الدموية؟", "نعم، التدليك بالليفة والصابون ينشط الدورة الدموية."),
        ("هل يترك لوناً أسود على الجلد؟", "لا، ينشطف بالماء تماماً دون ترك أي أثر لون."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an iconic luxury Moroccan black soap (Beldi Soap) in a jumbo 500g tub formulated with authentic Moroccan hammam traditions to cleanse, detoxify, soften, and brighten body skin with royal efficacy. Formulated with natural Black Olive Oil, {ingredient_en} essential oil, and nourishing skin bases.</p>
<p>Moroccan Black Soap softens dead skin cells and dry buildup, deeply cleanses pores, and detoxifies body skin while {benefit_en}, leaving your body touchably silky soft, spotlessly clean, even-toned, and perfectly prepared for deep Moroccan Kessa mitt exfoliation.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Dead Skin Softening & Buildup Removal:</strong> Prepares body for deep Kessa mitt exfoliation.</li>
  <li><strong>Full Body Pore Cleansing & Detoxification:</strong> Removes toxins, excess oils, and daily pollution.</li>
  <li><strong>Enriched with {ingredient_en} & Black Olive Oil:</strong> {benefit_en} and nourishes skin layers.</li>
  <li><strong>Silky Smooth Touch & Hydration:</strong> Hydrates skin guarding against dryness.</li>
  <li><strong>Generous 500g Jumbo Tub:</strong> Abundant volume lasting months of regular use.</li>
  <li><strong>100% Made in Morocco Spa Formulation:</strong> Royal Moroccan heritage in hammam and spa care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Steam & Wet):</strong> Relax in a warm steamy bathroom to open pores and soften skin.</li>
  <li><strong>Step 2 (Apply & Wait):</strong> Spread black soap over entire body and leave for 10-15 minutes.</li>
  <li><strong>Step 3 (Rinse & Scrub):</strong> Rinse off soap with warm water, then scrub body with Kessa mitt to peel off dead skin (use 1-2 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Black Olive Oil:</strong> Softens keratinized dead skin cells and feeds skin with antioxidants.</li>
  <li><strong>{ingredient_en} Essential Oil:</strong> {benefit_en} giving body skin royal purity and scent.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application only (do not use on face).</li>
  <li>Avoid contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for Moroccan hammam spa routine, body cleansing, and skin softening (500g).</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Certified Moroccan Beldi Soap Brand</td></tr>
  <tr><th>Category</th><td>Body Care / {ingredient_en} Moroccan Black Soaps (Beldi) 500g</td></tr>
  <tr><th>Product Type</th><td>Natural Black Olive Oil & {ingredient_en} Moroccan Beldi Soap (500g)</td></tr>
  <tr><th>Volume/Weight</th><td>500 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Including Dry & Hyperpigmented Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, spotlessly clean, even-toned body skin prepared for scrubbing</td></tr>
  <tr><th>Texture</th><td>Smooth rich dark soapy paste</td></tr>
  <tr><th>Fragrance</th><td>Authentic Moroccan olive & {ingredient_en} scent</td></tr>
  <tr><th>Active Ingredients</th><td>Black Olive Oil, {ingredient_en} Essential Oil, Saponified Potassium Olivate</td></tr>
  <tr><th>Country of Origin</th><td>Morocco</td></tr>
  <tr><th>Manufacturer</th><td>Moroccan Black Soap Products</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Saponified Olive Oil Emollient Keratin Softening</h2>

<h3>What problem does this solve?</h3>
<p>Moroccan Black Soap resolves stubborn dry skin buildup, deep pore clogging, and body skin roughness.</p>

<h3>Why choose Moroccan Black Soap?</h3>
<p>Saponified black olive oil acts as a powerful emollient hydrating and swelling dry stratum corneum keratin, allowing effortless peeling with a Kessa mitt.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is authentic natural Moroccan Black Soap with Black Olive Oil and {ingredient_en} in a jumbo 500g tub for body cleansing and hammam exfoliation."),
        (f"What are the benefits of Black Olive Oil and {ingredient_en}?", f"Black Olive Oil softens dead skin while {benefit_en} and nourishes skin layers."),
        ("Does it prepare skin for Kessa mitt scrubbing?", "Yes, softens dead skin cells and buildup making Kessa mitt scrubbing effortless and effective."),
        ("What weight is contained in this tub?", "500g jumbo tub."),
        ("How do I use it correctly?", "Sit in steam, apply soap for 10-15 minutes, rinse off thoroughly, then scrub body with Kessa mitt 1-2 times weekly."),
        ("Is it authentic Made in Morocco?", "Yes, 100% made in Morocco with authentic hammam formulations."),
        ("How do I verify authenticity at Ekleel Abha?", "All Moroccan Black Soap products at Ekleel Abha are 100% original."),
        ("Does it leave body silky smooth?", "Yes, imparts a touchably soft silky feel and spotless cleanliness."),
        (f"What does {en_name} smell like?", f"Luxury authentic Moroccan olive & {ingredient_en} scent."),
        ("Is it suitable for all body skin types?", "Yes, suitable for all body skin types."),
        ("Does 500g last long?", "Yes, jumbo tub lasts months of regular hammam use."),
        ("How should I store it?", "In a cool, dry place tightly closed."),
        ("Is it suitable for the face?", "Formulated for body skin only; do not use on face."),
        ("How many times weekly?", "1-2 times weekly in Moroccan hammam routine."),
        ("Does it detoxify body skin?", "Yes, deeply cleanses pores removing toxins and excess sebum."),
        ("Is Beldi Soap a historic Moroccan tradition?", "Yes, Beldi soap is the foundation of Moroccan spa care for centuries."),
        ("Is the tub recyclable?", "Yes."),
        ("Is it good before self-tanning?", "Yes, cleanses and prepares skin perfectly for self-tanning."),
        ("Does it give skin tone unification?", "Yes, removing dead buildup reveals bright even-toned skin."),
        ("Is it suitable for men and women?", "Suitable for men and women aged 16+."),
        ("Does it rinse off easily?", "Yes, rinses smoothly with warm water without sticky residue."),
        ("Is it a luxury bridal gift?", "Yes, royal luxury gift for brides and spa routines."),
        ("Does it stimulate blood circulation?", "Yes, scrubbing with Kessa mitt invigorates blood circulation."),
        ("Does it stain skin black?", "No, rinses off completely clean without leaving color on skin."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Moroccan Beldi",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. صابون بلدي مغربي 500 جم بزيت الزيتون و{ingredient_ar} لتنعيم وتنظيف وتقشير الجسم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Moroccan Black Soap 500g with Black Olive Oil & {ingredient_en} for body scrubbing. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1932():
    return _make_moroccan_black_soap_variant(
        pid=1932, gtin="701197409248",
        ar_name="الصابون البلدي المغربي بالغاسوول وزيت إكليل الجبل الاساسي 500جم",
        en_name="Moroccan Black Soap with Ghassoul and Rosemary Essential Oil - 500g",
        ingredient_ar="طين الغاسول وإكليل الجبل (الروزماي)", ingredient_en="Moroccan Ghassoul & Rosemary Essential Oil",
        benefit_ar="تنقي المسام وتطهر الجلد وتنعش الجسم وتشد البشرة", benefit_en="purifies pores, cleanses skin, refreshes body, and tightens skin",
        tags_ar=["الصابون_البلدي", "الغاسول_المغربي", "إكليل_الجبل", "صابون_مغربي", "إكليل_أبها"],
        tags_en=["moroccan_black_soap", "ghassoul_soap", "rosemary_oil", "beldi_soap", "ekleel_abha"]
    )


def create_product_1933():
    return _make_moroccan_black_soap_variant(
        pid=1933, gtin="701197409231",
        ar_name="الصابون البلدي المغربي بزيت الأوكاليبتوس الأساسي 500جم",
        en_name="Moroccan Black Soap with Eucalyptus Essential Oil - 500g",
        ingredient_ar="زيت الأوكاليبتوس (الكينا) الأساسي", ingredient_en="Eucalyptus Essential Oil",
        benefit_ar="تفتح التنفس وتطهر المسام وتمنح الجسم انتعاشاً ثلجياً مطهراً", benefit_en="opens breathing pathways, purifies pores, and imparts an icy antiseptic freshness",
        tags_ar=["الصابون_البلدي", "الأوكاليبتوس", "انتعاش_الكينا", "صابون_مغربي", "إكليل_أبها"],
        tags_en=["moroccan_black_soap", "eucalyptus_soap", "antiseptic_freshness", "beldi_soap", "ekleel_abha"]
    )


def _make_ajmal_perfumed_powder(pid, gtin, ar_name, en_name, scent_ar, scent_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>{ar_name}</strong> بودرة المعطرة الفاخرة المطفية من أجمل المصممة لتوفير جفاف تام، نعومة فائقة، وعطر شرقي/فرنسي فواح يدوم طوال اليوم. ترتكز هذه البودرة الفاخرة ({en_name}) على التلك المنقى الناعم (Pure Purified Talc)، العطور الفاخرة المركزة من أجمل، والمكونات الملطفة لجلد الجسم.</p>
<p>تعمل بودرة أجمل المعطرة على امتصاص العرق والرطوبة الزائدة في الجسم، منع الاحتكاك والتهيج الجلدي، وتغليف الجسم برائحة {scent_ar} الفواحة، لتترك جسمك ناعماً كالحرير، جافاً، معطراً بالأناقة، ومفعماً بالثقة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تعطير شرقي/فرنسي فواح طوال اليوم بعطر {scent_ar}:</strong> يغلف الجسم برائحة راقية تدوم لساعات.</li>
  <li><strong>امتصاص سريع للرطوبة والعرق الزائد:</strong> تحافظ على جفاف ونظافة الجسم.</li>
  <li><strong>تنعيم وملمس حريري مخملي:</strong> تمنح البشرة ملمساً ناعماً جداً ومريحاً.</li>
  <li><strong>منع الاحتكاك والتهيج بين الثنايا:</strong> تقي من الاحتكاك الجلدي الناتج عن التعرق.</li>
  <li><strong>جودة وعراقة دار أجمل للعطور:</strong> خبرة عقود في تصنيع العطور والبودرات المعطرة الفاخرة.</li>
  <li><strong>عبوة اقتصادية 100 جم:</strong> حجم أنيق ممتاز للاستخدام اليومي بعد الاستحمام.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> جففي الجسم جيداً بعد الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من بودرة أجمل المعطرة على اليدين أو على إسفنجة البودرة.</li>
  <li><strong>الخطوة الثالثة:</strong> وزعي البودرة برفق على كامل الجسم مع التركيز على مناطق الرقبة والصدر والثنايا (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>التلك المنقى الناعم (Pure Purified Talc):</strong> يمتص الرطوبة الزائدة ويمنح ملمساً حريرياً ناعماً.</li>
  <li><strong>العطر الفاخر المركّز من أجمل ({scent_ar}):</strong> يمنح الجسم نفساً معطراً فواحاً يدوم طوال اليوم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم فقط.</li>
  <li>تجنبي استنشاق البودرة أو سكبها قرب الوجه والأنف.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لتعطير وتنعيم وتجفيف بشرة الجسم بعطور أجمل الفاخرة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>أجمل (Ajmal Perfumes)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / بودرات أجمل المعطرة للجسم 100g</td></tr>
  <tr><th>نوع المنتج</th><td>بودرة جسم معطرة ومطراة بعطر {scent_ar} الفاخر (100g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم جاف، ناعم كالحرير، معطر برائحة {scent_ar} الفواحة طوال اليوم</td></tr>
  <tr><th>الملمس</th><td>بودرة ناعمة جداً ذات ملمس مخملي حريري</td></tr>
  <tr><th>العطر</th><td>عطر {scent_ar} الفاخر من أجمل</td></tr>
  <tr><th>المكونات النشطة</th><td>تلك منقى ناعم، عطور أجمل المركزة، مواد ملطفة</td></tr>
  <tr><th>بلد المنشأ</th><td>الإمارات العربية المتحدة (UAE)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ajmal Perfumes International</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد عطور أجمل والتلك المنقى في البودرة المعطرة ({scent_ar})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج بودرة أجمل المعطرة مشكلة التعرق الزائد والرطوبة بالجسم، رائحة العرق، والاحتكاك والالتصاق الجلدي.</p>

<h3>لماذا تنجح تركيبة أجمل المعطرة؟</h3>
<p>لأن حبيبات التلك الدقيقة جداً تحبس العرق دون انسداد مسامي بينما تثبت زيوت أجمل العطرية على طبقة البشرة السطحية لتفوح لساعات طويلة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق بعد الاستحمام مباشرة:</strong> يضمن ثبات الرائحة المعطرة طوال اليوم.<br>
2. <strong>التمركز على مناطق النبض والثنايا:</strong> يزيد فوحان العطر مع حركة الجسم حرارياً.<br>
3. <strong>التجفيف الكامل قبل الوضع:</strong> يمنح أفضل ملمس حريري مخملي دون تكتل.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "بودرات الجسم المعطرة تسبب سمرة الجلد."<br>
<strong>الحقيقة:</strong> بودرة أجمل خالية من المكونات المسببة للسمرة وهي مصنعة وفق أعلى معايير السلامة التجميلية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تمتص الصفيحات الميكروية للتلك الرطوبة السطحية فيزياءً، بينما تحرر الميكروكابسولات العطرية عطر أجمل تدريجياً بالتلامس الحراري مع الجلد.</p>"""

    faqs_data = [
        (f"ما هي {ar_name}؟", f"هي بودرة جسم معطرة وفاخرة من أجمل بعطر {scent_ar} لامتصاص الرطوبة وتنعيم وتعطير الجسم (100 جم)."),
        (f"ما هي فوائد التلك المنقى وعطر أجمل {scent_ar}؟", f"يمتص التلك الرطوبة ويمنع الاحتكاك، بينما يغلف عطر {scent_ar} الجسم برائحة فواحة تدوم طوال اليوم."),
        ("هل تمنح الجسم ملمساً ناعماً حريرياً؟", "نعم، تمنح البشرة ملمساً مخملياً ناعماً جداً ومريحاً."),
        ("ما وزن العبوة؟", "تأتي بوزن 100 جم."),
        ("كيف تُستخدم بالشكل الصحيح؟", "جففي الجسم بعد الاستحمام، ضعي كمية على اليدين أو الإسفنجة ووزعيها برفق على الجسم والرقبة الثنايا يومياً."),
        ("هل هي آمنة للاستخدام اليومي؟", "نعم، آمنة ومختبرة للاستخدام اليومي على بشرة الجسم."),
        ("أين صُنعت بودرة أجمل؟", "صُنعت في الإمارات العربية المتحدة بواسطة Ajmal Perfumes."),
        ("كيف أتأكد من أصالتها لدى إكليل أبها؟", "جميع منتجات أجمل لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {scent_ar} الفاخر الفواح من أجمل."),
        ("هل تمنع الاحتكاك والتعرق بين الثنايا؟", "نعم، تمتص العرق وتمنع الاحتكاك والالتصاق الجلدي."),
        ("هل 100 جم تكفي لفترة جيدة؟", "نعم، تكفي لعدة أسابيع من الاستخدام اليومي بعد الاستحمام."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع الفئات حسب العطر المفضل."),
        ("كم مرة يومياً؟", "مرة يومياً بعد الاستحمام وعند الحاجة."),
        ("هل تترك الفم والجسم معطراً طوال اليوم؟", "نعم، فوحان وثبات ممتاز طوال اليوم."),
        ("هل أجمل ماركة عطور عالمية شهيرة؟", "نعم، Ajmal Perfumes دار عطور عالمية عريقة ذات خبرة تزيد عن 70 عاماً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل تمنع رائحة العرق الكريهة؟", "نعم، تحافظ على جفاف ونظافة وتعطير الجسم."),
        ("هل تناسب جميع فصول السنة؟", "نعم، ممتازة في الصيف والشتاء."),
        ("هل تترك أثراً بيضاً سميكاً؟", "تتوزع بنعومة دون ترك تكتلات بيضاء سميكة."),
        ("هل تتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، تتوفرف بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل تناسب الاستخدام بعد حلاقة الجسم؟", "تهدئ الجلد وتنعمه بعد الحلاقة."),
        ("هل تصلح هدية عملية؟", "نعم، هدية أنيقة ومفيدة لكل عشاق عطور أجمل."),
        ("هل يمكن وضعها على الملابس؟", "توضع على الجلد مباشرةً للحصول على أفضل تعطير وتنعيم."),
        ("هل تجفف الجلد؟", "تنعّم وتحفظ التوازن دون جفاف شديد.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is a luxury perfumed body talc from Ajmal Perfumes designed to provide complete dryness, silky smoothness, and an all-day long-lasting fragrance. Formulated with fine pure purified talc, concentrated luxury Ajmal perfume oils, and skin-soothing agents.</p>
<p>Ajmal Perfumed Body Powder absorbs excess sweat and moisture, prevents skin chafing and irritation, and envelops your body in the captivating scent of {scent_en}, leaving your skin touchably soft, dry, elegantly fragranced, and confident all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>All-Day Long-Lasting Fragrance with {scent_en}:</strong> Envelops body in an elegant scent lasting for hours.</li>
  <li><strong>Fast Absorption of Excess Sweat & Moisture:</strong> Keeps body dry and clean.</li>
  <li><strong>Silky Smooth Velvet Touch:</strong> Imparts an extremely soft comfortable feel to skin.</li>
  <li><strong>Prevents Friction & Chafing in Folds:</strong> Shields skin against sweat-induced friction.</li>
  <li><strong>Heritage & Quality of Ajmal Perfumes:</strong> Decades of expertise in luxury perfumery and body talcs.</li>
  <li><strong>Economical 100g Container:</strong> Elegant size perfect for daily post-shower use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Dry body thoroughly after shower.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of Ajmal perfumed powder onto hands or a powder puff.</li>
  <li><strong>Step 3:</strong> Smooth gently over full body focusing on neck, chest, and skin folds (use daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Purified Fine Talc:</strong> Absorbs excess moisture and imparts a silky soft touch.</li>
  <li><strong>Concentrated Luxury Ajmal Fragrance ({scent_en}):</strong> Delivers an intense long-lasting pleasant scent.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application only.</li>
  <li>Avoid inhaling powder or dusting near face and nose.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for body perfuming, smoothing, and moisture absorption with luxury Ajmal scents.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Ajmal Perfumes</td></tr>
  <tr><th>Category</th><td>Personal Care / Ajmal Perfumed Body Powders 100g</td></tr>
  <tr><th>Product Type</th><td>Luxury {scent_en} Scented & Smoothing Body Talc (100g)</td></tr>
  <tr><th>Volume/Weight</th><td>100 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types</td></tr>
  <tr><th>Finish</th><td>Dry, silky soft, beautifully fragranced body skin with {scent_en} all day</td></tr>
  <tr><th>Texture</th><td>Ultra-fine silky soft velvet powder</td></tr>
  <tr><th>Fragrance</th><td>Luxury {scent_en} fragrance by Ajmal</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Purified Fine Talc, Concentrated Ajmal Fragrance Oils, Soothing Agents</td></tr>
  <tr><th>Country of Origin</th><td>UAE</td></tr>
  <tr><th>Manufacturer</th><td>Ajmal Perfumes International</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Fine Purified Talc Moisture Adsorption & Ajmal Fragrance Fixation</h2>

<h3>What problem does this solve?</h3>
<p>Ajmal Perfumed Powder resolves excess sweat, body moisture, body odor, and skin chafing friction.</p>

<h3>Why choose Ajmal Perfumed Powder?</h3>
<p>Micro-fine talc platelets physically adsorb skin moisture preventing friction while Ajmal fragrance oils fixate onto epidermal surface layers releasing fragrance continuously.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a luxury perfumed body talc from Ajmal with {scent_en} fragrance for absorbing moisture, smoothing, and perfuming the body (100g)."),
        (f"What are the benefits of Purified Talc and {scent_en} fragrance?", f"Talc absorbs moisture and prevents chafing, while {scent_en} fragrance coats the body in long-lasting scent."),
        ("Does it impart a silky smooth touch?", "Yes, gives skin an extremely soft comfortable velvet touch."),
        ("What weight is contained in this tub?", "100g."),
        ("How do I use it correctly?", "Dry body post-shower, apply on hands or puff, smooth gently over body, neck, and folds daily."),
        ("Is it safe for daily use?", "Yes, safe and tested for daily body skin application."),
        ("Where is Ajmal powder manufactured?", "In UAE by Ajmal Perfumes International."),
        ("How do I verify authenticity at Ekleel Abha?", "All Ajmal products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", f"Luxury signature {scent_en} fragrance by Ajmal."),
        ("Does it prevent chafing and sweat friction in skin folds?", "Yes, absorbs sweat preventing friction and skin sticking."),
        ("Does 100g last long?", "Yes, lasts weeks of daily post-shower use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for men and women?", "Suitable for men and women depending on scent preference."),
        ("How many times daily?", "Once daily post-shower and as needed."),
        ("Does it leave lasting fresh breath and scent all day?", "Yes, excellent sillage and long-lasting scent performance all day."),
        ("Is Ajmal a world-famous perfume house?", "Yes, Ajmal Perfumes is a globally renowned perfume house with over 70 years of heritage."),
        ("Is the container recyclable?", "Yes."),
        ("Does it prevent unpleasant body sweat odor?", "Yes, keeps body dry, clean, and beautifully fragranced."),
        ("Is it good for all seasons?", "Yes, excellent in summer and winter."),
        ("Does it leave a thick white residue?", "Distributes smoothly without leaving thick white clumps."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable post-shaving?", "Soothes and softens skin after shaving."),
        ("Is it a practical gift?", "Yes, elegant and thoughtful gift for Ajmal fragrance lovers."),
        ("Can it be applied on clothing?", "Best applied directly onto skin for optimal perfuming and smoothing."),
        ("Does it dry skin out?", "Softens and preserves skin moisture balance without harsh drying.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Ajmal",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. بودرة جسم معطرة من أجمل بعطر {scent_ar} لامتصاص الرطوبة وتنعيم وتعطير الجسم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Luxury Ajmal perfumed body talc with {scent_en} fragrance for smoothness and freshness. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1934():
    return _make_ajmal_perfumed_powder(
        pid=1934, gtin="6293708010868",
        ar_name="بودرة فريش ان كوول من اجمل 100 جم",
        en_name="Ajmal Fresh N Cool Powder 100 gm",
        scent_ar="فريش أند كول الانتعاش الثلجي المنعش", scent_en="Fresh N Cool Icy Refreshment",
        tags_ar=["أجمل", "بودرة_فريش_ان_كول", "انتعاش_البودرة", "بودرة_أجمل", "إكليل_أبها"],
        tags_en=["ajmal", "fresh_n_cool_powder", "body_talc", "ajmal_powder", "ekleel_abha"]
    )


def create_product_1935():
    return _make_ajmal_perfumed_powder(
        pid=1935, gtin="6293708009183",
        ar_name="بودرة ساكرد لوف من اجمل 100 جم",
        en_name="Ajmal Sacred Love Perfumed Powder 100g",
        scent_ar="ساكرد لوف الزهري الفاخر الأنيق", scent_en="Sacred Love Elegant Floral",
        tags_ar=["أجمل", "بودرة_ساكرد_لوف", "بودرة_عطرية", "عطر_ساكرد_لوف", "إكليل_أبها"],
        tags_en=["ajmal", "sacred_love_powder", "perfumed_talc", "sacred_love_scent", "ekleel_abha"]
    )


def create_product_1936():
    return _make_ajmal_perfumed_powder(
        pid=1936, gtin="6293708009220",
        ar_name="بودرة بلو من اجمل 100 جم",
        en_name="Ajmal Blue Powder 100 gm",
        scent_ar="بلو الخشبية البحرية المنعشة", scent_en="Blue Aquatic Woody Freshness",
        tags_ar=["أجمل", "بودرة_بلو", "بودرة_أجمل_بلو", "انتعاش_بلو", "إكليل_أبها"],
        tags_en=["ajmal", "blue_powder", "ajmal_blue_talc", "aquatic_freshness", "ekleel_abha"]
    )


print("Loaded all 5 Batch 44 builders complete")
