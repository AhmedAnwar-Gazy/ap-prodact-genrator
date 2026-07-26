import json, os

def _make_body_soap_scrub_500g(pid, gtin, ar_name, en_name, ingredient_ar, ingredient_en, benefit_ar, benefit_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> صابون ومقشر العناية الفاخرة بالجسم (500 جم) المصنوع بتركيبة الحمام المغربي والسبا الطبيعية المصممة لتقشير وتنظيف وتنعيم وتفتيح بشرة الجسم. يرتكز هذا المنتج الفاخر ({en_name}) على حبيبات المقشر الدقيقة، الصابون البلدي المعزز بـ {ingredient_ar}، والزيوت المرطبة المغذية.</p>
<p>يعمل صابون ومقشر الجسم على إزالة خلايا الجلد الميتة والتراكمات الجافة، تنظيف مسام الجسم العميقة، و{benefit_ar}، ليترك جسمك ناعماً كالحرير، ناضراً، موحد اللون، ومعطراً بعطر {ingredient_ar} الفاخر.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تقشير وتنظيف 2 في 1 بحبيبات طبيعية:</strong> يزيل التراكمات وخلايا الجلد الميتة.</li>
  <li><strong>تغذية وتفتيح بشرة الجسم بـ {ingredient_ar}:</strong> {benefit_ar} ويقضي على التصبغات.</li>
  <li><strong>تنعيم وترطيب عميق للجسم:</strong> يمنح الجلد ملمساً حريرياً دون جفاف.</li>
  <li><strong>تنظيف مسام الجسم وإزالة السموم:</strong> ينشط الدورة الدموية ويعيد الحيوية للجلد.</li>
  <li><strong>عبوة اقتصادية ضخمة 500 جم:</strong> كمية وافرة تكفي لعدة أشهر من الاستخدام.</li>
  <li><strong>مثالي للحمام المغربي والسبا المنزلي:</strong> تجربة عناية استثنائية في المنزل.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي الجسم بالماء الدافئ لفتح المسام.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة ودلكي بحركات دائرية (يُفضل باستخدام الليفة المغربية).</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي الجسم جيداً بالماء الدافئ (يُستعمل 1-2 مرة أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>حبيبات المقشر الطبيعية و{ingredient_ar}:</strong> تقشر الجلد الميت وتفتّح التصبغات.</li>
  <li><strong>الصابون البلدي والزيوت المرطبة:</strong> ينظفان المسام ويحفظان رطوبة الجلد.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم فقط (لا يُستعمل للوجه).</li>
  <li>تجنبي الاستخدام على الجلد المصاب بجروح أو حروق.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لتقشير وتفتيح وتنظيف بشرة الجسم 500 جم.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>العلامة التجارية المعتمدة</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / مقشرات وصابونات الجسم الفاخرة بـ {ingredient_ar} 500g</td></tr>
  <tr><th>نوع المنتج</th><td>صابون ومقشر جسم 2 في 1 بـ {ingredient_ar} للتفتيح والتقشير (500g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (الجافة والمفتقرة للنضارة)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، موحد اللون، ناضر ومعطر بعطر {ingredient_ar}</td></tr>
  <tr><th>الملمس</th><td>معجون صابوني حبيبي ناعم مغذٍ بالزيوت</td></tr>
  <tr><th>العطر</th><td>عطر {ingredient_ar} الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>حبيبات مقشر طبيعية، {ingredient_ar}، صابون بلدي، زيوت مغذية</td></tr>
  <tr><th>بلد المنشأ</th><td>المغرب / الإمارات العربية المتحدة</td></tr>
  <tr><th>الشركة المصنعة</th><td>Body Care Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد تقشير الجسم بـ {ingredient_ar} (500g)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج صابون ومقشر الجسم تراكم خلايا الجلد الميتة، اسمرار الكوعين والركبتين، وجفاف وخشونة الجلد.</p>

<h3>لماذا تنجح تركيبة {ingredient_ar}؟</h3>
<p>لأن التقشير الدقيق يزيل طبقة الكيراتين الميتة فورياً بينما تمنح خلاصات {ingredient_ar} التغذية والتفتيح المستمر.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام 1-2 مرة أسبوعياً:</strong> التكرار المعتدل يضمن تجديد البشرة دون تهيج.<br>
2. <strong>التدليك بالليفة المغربية:</strong> يزيد فاعلية إزالة التراكمات الجافة.<br>
3. <strong>الترطيب بعد الاستحمام:</strong> يحبس الرطوبة ويضاعف نتائج النعومة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "التقشير يسبب جفاف البشرة المفرط."<br>
<strong>الحقيقة:</strong> هذا المنتج مدعم بالزيوت المرطبة والصابون البلدي ليترك الجلد ناعماً ومرطباً بعد الاستخدام.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تزيل جزيئات المقشر الطبيعية التراكمات القرنية بينما تخترق مضادات الأكسدة في {ingredient_ar} البشرة لتغذيتها.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو صابون ومقشر جسم فاخر 2 في 1 بـ {ingredient_ar} بحجم 500 جم لتقشير وتفتيح وتنظيف الجسم."),
        (f"ما هي فوائد {ingredient_ar} والحبيبات الطبيعية؟", f"تقشر الحبيبات الجلد الميت والتراكمات، بينما {benefit_ar} وتوحد لون الجسم."),
        ("هل يزيل التصبغات والجلد الميت؟", "نعم، يزيل خلايا الجلد الميتة والتراكمات الجافة بفاعلية من كامل الجسم."),
        ("ما وزن العبوة؟", "تأتي بعبوة ضخمة بوزن 500 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الجسم بالماء الدافئ، ضعي المقشر ودلكي بحركات دائرية بالليفة المغربية ثم اشطفي 1-2 مرة أسبوعياً."),
        ("هل يناسب جميع أنواع بشرة الجسم؟", "نعم، مناسب لجميع أنواع بشرة الجسم."),
        ("أين صُنع؟", "صُنع في المغرب/الإمارات بتركيبة سبا فاخرة."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {ingredient_ar} الفاخر المميز."),
        ("هل يترك الجسم ناعماً كالحرير؟", "نعم، يمنح البشرة ملمساً حريرياً ناعماً من الاستخدام الأول."),
        ("هل 500 جم تدوم طويلاً؟", "نعم، عبوة ضخمة تكفي لعدة أشهر من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف محكم الإغلاق."),
        ("هل يناسب الوجه؟", "مخصص لبشرة الجسم فقط ولا يُستعمل لبشرة الوجه."),
        ("كم مرة أسبوعياً؟", "1-2 مرة أسبوعياً للحصول على أفضل نتائج."),
        ("هل يساعد في منع شعر تحت الجلد؟", "نعم، التقشير المنتظم يمنع انسداد المسام وشعر تحت الجلد."),
        ("هل ينشط الدورة الدموية؟", "نعم، التدليك بالليفة والمقشر ينشط الدورة الدموية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب الاستخدام قبل التسمير (التان)؟", "نعم، يجهز البشرة لـ تان متجانس."),
        ("هل يناسب الاستخدام في الحمام المغربي والسبا؟", "نعم، خيار مثالي للحمام المغربي والسبا المنزلي."),
        ("هل يمنح توحيداً ونضارة للبشرة؟", "نعم، يمنح نعومة وإشراقاً وتفتيحاً تدريجياً."),
        ("هل يناسب النساء والرجال؟", "نعم، مناسب للنساء والرجال من 16 سنة."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، ينشطف بالماء الدافئ بسلاسة دون لزوجة."),
        ("هل يصلح هدية فاخرة؟", "نعم، هدية ممتازة جداً للعناية بالبشرة والعرائس."),
        ("هل يحافظ على ترطيب الجلد بعد الاستحمام؟", "نعم، الزيوت المرطبة تحفظ ترطيب الجلد ونعومته."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is a luxury 2-in-1 body soap and scrub in a generous 500g tub formulated with Moroccan hammam spa traditions to exfoliate, cleanse, soften, and brighten body skin. Formulated with natural micro-exfoliating beads, traditional soap enriched with {ingredient_en}, and nourishing hydrating oils.</p>
<p>This body soap and scrub removes dead skin cells and dry buildup, deeply cleanses body pores, and {benefit_en}, leaving your body touchably silky soft, radiant, even-toned, and fragranced with luxury {ingredient_en} scent.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>2-in-1 Superior Exfoliation & Cleansing with Natural Beads:</strong> Sloughs off dead skin cells revealing fresh skin.</li>
  <li><strong>Body Skin Brightening & Nourishment with {ingredient_en}:</strong> {benefit_en} and targets dark spots.</li>
  <li><strong>Deep Softening & Body Hydration:</strong> Imparts a silky smooth touch without drying skin.</li>
  <li><strong>Body Pore Cleansing & Detoxification:</strong> Stimulates blood circulation reviving skin vitality.</li>
  <li><strong>Generous 500g Jumbo Tub:</strong> Abundant volume lasting months of regular use.</li>
  <li><strong>Ideal for Moroccan Hammam & Home Spa:</strong> Luxury spa care experience at home.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet body with warm water to open pores.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of soap & scrub, massage in circular motions (preferably with Kessa mitt).</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water (use 1-2 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Exfoliating Beads & {ingredient_en}:</strong> Exfoliate dead skin and brighten dark body hyperpigmentation.</li>
  <li><strong>Traditional Soap & Hydrating Oils:</strong> Cleanse pores while preserving skin moisture and softness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application only (do not use on face).</li>
  <li>Avoid using on broken, wounded, or burned skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for body exfoliation, brightening, and cleansing with 500g spa formula.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Certified Brand</td></tr>
  <tr><th>Category</th><td>Body Care / {ingredient_en} Luxury Body Soaps & Scrubs 500g</td></tr>
  <tr><th>Product Type</th><td>2-in-1 {ingredient_en} Body Exfoliating & Brightening Soap Scrub (500g)</td></tr>
  <tr><th>Volume/Weight</th><td>500 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Including Dry & Dull Skin)</td></tr>
  <tr><th>Finish</th><td>Silky smooth, radiant, even-toned body skin free of dry buildup</td></tr>
  <tr><th>Texture</th><td>Smooth oil-rich granular soapy paste</td></tr>
  <tr><th>Fragrance</th><td>Luxury {ingredient_en} scent</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Exfoliating Beads, {ingredient_en}, Traditional Soap, Hydrating Oils</td></tr>
  <tr><th>Country of Origin</th><td>Morocco / UAE</td></tr>
  <tr><th>Manufacturer</th><td>Body Care Laboratories</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of {ingredient_en} Skin Nourishment & Mechanical Epidermal Desquamation</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves dead skin buildup, body hyperpigmentation, and skin roughness and dryness.</p>

<h3>Why choose this 2-in-1 Soap & Scrub?</h3>
<p>Micro-beads mechanically remove stratum corneum keratinized buildup while natural {ingredient_en} active compounds feed and hydrate skin layers.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a luxury 2-in-1 body soap and scrub infused with {ingredient_en} in a jumbo 500g tub for body exfoliation and brightening."),
        (f"What are the benefits of {ingredient_en} and natural beads?", f"Exfoliating beads remove dead skin while {benefit_en} and unify body tone."),
        ("Does it remove hyperpigmentation and dead skin?", "Yes, effectively removes dead skin cells and dry buildup from full body skin."),
        ("What weight is contained in this tub?", "500g jumbo tub."),
        ("How do I use it correctly?", "Wet body with warm water, apply scrub, massage in circles with Kessa mitt, rinse 1-2 times weekly."),
        ("Is it suitable for all body skin types?", "Yes, suitable for all body skin types."),
        ("Where is this body scrub manufactured?", "In Morocco/UAE with luxury spa formulations."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original."),
        (f"What does {en_name} smell like?", f"Luxury signature {ingredient_en} scent."),
        ("Does it leave body silky smooth?", "Yes, imparts a touchably soft silky feel from first use."),
        ("Does 500g last long?", "Yes, jumbo tub lasts months of regular use."),
        ("How should I store it?", "In a cool, dry place tightly closed."),
        ("Is it suitable for the face?", "Formulated for body skin only; do not use on face."),
        ("How many times weekly?", "1-2 times weekly for best results."),
        ("Does it help with ingrown hair / strawberry legs?", "Yes, regular exfoliation prevents clogged pores and ingrown hairs."),
        ("Does it stimulate blood circulation?", "Yes, massage with scrub and mitt invigorates blood circulation."),
        ("Is the tub recyclable?", "Yes."),
        ("Is it good before self-tanning?", "Yes, prepares skin for a smooth self-tan application."),
        ("Is it suitable for Moroccan Hammam & Spa?", "Yes, perfect choice for Moroccan Hammam and home spa routines."),
        ("Does it give instant tone unification?", "Imparts instant smoothness and radiance with progressive brightening."),
        ("Is it suitable for men and women?", "Yes, suitable for men and women aged 16+."),
        ("Does it rinse off easily?", "Yes, rinses smoothly with warm water without sticky residue."),
        ("Is it a luxury gift?", "Yes, luxurious and practical gift for skincare enthusiasts."),
        ("Does it keep skin hydrated post-shower?", "Yes, moisturizing oils lock in skin hydration and softness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Body Care",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. صابون ومقشر جسم 2 في 1 بـ 500 جم لتقشير وتفتيح وتنظيف الجسم بـ {ingredient_ar}. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. 2-in-1 body soap & scrub 500g for body exfoliation and brightening with {ingredient_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1922():
    return _make_body_soap_scrub_500g(
        pid=1922, gtin="745178721431",
        ar_name="صابون ومقشر الجسم العكر الفاسي 500جم",
        en_name="Aker Fassi Body Soap and Scrub 500g",
        ingredient_ar="مسحوق العكر الفاسي المغربي الأبلج", ingredient_en="Authentic Moroccan Aker Fassi Powder",
        benefit_ar="تمنح الجسم توريداً ناعماً إشراقاً وردياً ملكياً وتفتيحاً", benefit_en="imparts a soft rosy royal blush, radiance, and body brightening",
        tags_ar=["العكر_الفاسي", "مقشر_العكر_الفاسي", "توريد_الجسم", "صابون_العكر", "إكليل_أبها"],
        tags_en=["aker_fassi", "aker_fassi_scrub", "rosy_body_blush", "aker_fassi_soap", "ekleel_abha"]
    )


def create_product_1923():
    return _make_body_soap_scrub_500g(
        pid=1923, gtin="745178721455",
        ar_name="صابون ومقشر الجسم بالقهوه 500جم",
        en_name="Coffee Body Soap and Scrub 500g",
        ingredient_ar="مسحوق القهوة العربية والكافيين", ingredient_en="Arabica Coffee Powder & Caffeine",
        benefit_ar="تكافح السيلوليت وتشد جلد الجسم وتمنحه نعومة فائقة", benefit_en="combats cellulite, tightens body skin, and imparts extreme smoothness",
        tags_ar=["مقشر_القهوة", "صابون_القهوة", "مكافحة_السيلوليت", "شد_الجسم", "إكليل_أبها"],
        tags_en=["coffee_scrub", "coffee_body_soap", "cellulite_control", "skin_tightening", "ekleel_abha"]
    )


def create_product_1924():
    return _make_body_soap_scrub_500g(
        pid=1924, gtin="745178721417",
        ar_name="صابون ومقشر الجسم ايسلند سانت 500جم",
        en_name="Iceland Scent Body Soap and Scrub 500g",
        ingredient_ar="عطر ومستخلصات آيسلند سانت المنعشة", ingredient_en="Refreshing Iceland Scent Extracts",
        benefit_ar="تمنح الجسم انتعاشاً ثلجياً فائقاً وترطيباً وتنعيماً", benefit_en="imparts icy refreshing coolness, hydration, and body smoothness",
        tags_ar=["ايسلند_سانت", "مقشر_ايسلند", "انتعاش_الجسم", "صابون_ايسلند", "إكليل_أبها"],
        tags_en=["iceland_scent", "iceland_scrub", "body_refreshment", "iceland_soap", "ekleel_abha"]
    )


def create_product_1925():
    return _make_body_soap_scrub_500g(
        pid=1925, gtin="745178721394",
        ar_name="صابون ومقشر الجسم الخزامي 500جم",
        en_name="Lavender Body Soap and Scrub 500g",
        ingredient_ar="زيت الخزامى (اللافندر) الطبيعي المهدئ", ingredient_en="Natural Soothing Lavender Oil",
        benefit_ar="تهدئ البشرة المجهدة وتمنح الاسترخاء الكامل والنعومة", benefit_en="soothes stressed skin and delivers complete relaxation and smoothness",
        tags_ar=["الخزامى", "مقشر_اللافندر", "استرخاء_الجسم", "صابون_الخزامى", "إكليل_أبها"],
        tags_en=["lavender", "lavender_scrub", "body_relaxation", "lavender_soap", "ekleel_abha"]
    )


def create_product_1926():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مقشر السكر بزيت الأركان ومسحوق زهرة الكركديه من جاردن دي أوليان - 600جم (Jardin d'Oléane Sugar Scrub with Argan Oil and Hibiscus Flower Powder - 600g)</strong> مقشر السكر المغربي الملكي الفاخر بحجم ضخم (600 جم) من جاردن دي أوليان المصمم لتقشير وترطيب وتفتيح وإعادة الإشراق الوردي الناعم لبشرة الجسم. يرتكز هذا المقشر الفاخر (Jardin d'Oléane Sugar Scrub Argan & Hibiscus 600g) على البلورات السكرية الطبيعية، زيت الأركان المغربي النقي الأصيل، ومسحوق زهرة الكركديه الطبيعية (Hibiscus Powder).</p>
<p>يعمل مقشر جاردن دي أوليان بالكركديه والأركان على تقشير خلايا الجلد الميتة برفق ولطافة، تغذية الجلد بعمق بالأحماض الدهنية وفيتامين E من زيت الأركان، وإكساب الجسم توريداً وردياً ملكياً ونعومة ناصعة، ليترك جسمك ناعماً كالحرير، ناضراً، ممتلئاً بالحيوية، ومعطراً برائحة الكركديه المغربية الساحرة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تقشير لطيف وعميق بالبلورات السكرية الطبيعية:</strong> يزيل التراكمات دون خدش أو تهيج للبشرة.</li>
  <li><strong>تغذية فائقة وحفظ الترطيب بزيت الأركان المغربي النقي:</strong> يغذي طبقات الجلد بالأحماض الدهنية وفيتامين E.</li>
  <li><strong>توريد وإشراق وردي ملكي بمسحوق زهرة الكركديه:</strong> يمنح بشرة الجسم توهجاً وتفتيحاً وردياً ناعماً.</li>
  <li><strong>قوام زيتاني سكري غني جداً:</strong> ينزلق برفق ويترك طبقة ترطيب وتنعيم مخملية.</li>
  <li><strong>عبوة ضخمة سعة 600 جم:</strong> كمية وافرة جداً تكفي لاستخدام أسبوعي منتظم لعدة أشهر.</li>
  <li><strong>صنع في المغرب بتركيبة سبا فاخرة 100%:</strong> تراث أصيل في العناية بالبشرة والسبا المغربي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (البلل):</strong> بللي بشرة الجسم بالماء الدافئ أثناء الاستحمام لفتح المسام.</li>
  <li><strong>الخطوة الثانية (التطبيق والتدليك):</strong> ضعي كمية مناسبة من مقشر السكر ودلكي الجسم بحركات دائرية لطيفة مع التركيز على المناطق الخشنة.</li>
  <li><strong>الخطوة الثالثة (الشطف):</strong> اشطفي الجسم جيداً بالماء الفاتر دون استخدام الصابون بعدها لحبس الزيوت (يُستعمل 1-2 مرة أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>البلورات السكرية ومسحوق زهرة الكركديه:</strong> يقشران الجلد الميت ويمنحان الجسم توريداً وتفتيحاً وردياً طبيعياً.</li>
  <li><strong>زيت الأركان المغربي النقي:</strong> يغذي البشرة بالأحماض الدهنية الأساسية وفيتامين E ويحفظ مرونتها.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم فقط (لا يُستعمل للوجه).</li>
  <li>تجنبي الاستخدام على الحروق والجروح المفتوحة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن مقشر السكر بالكركديه والأركان من جاردن دي أوليان 600 جم لتوريد وتقشير وترطيب الجسم.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جاردن دي أوليان (Jardin d'Oléane)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / مقشرات السكر المغربية الفاخرة بزيت الأركان 600g</td></tr>
  <tr><th>نوع المنتج</th><td>مقشر سكر طبيعي بزيت الأركان ومسحوق زهرة الكركديه للتوريد والتفتيح (600g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>600 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (بما في ذلك البشرة الجافة والمفتقرة للنضارة)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، مرطب بالزيوت، وردي الإشراق وموحد اللون</td></tr>
  <tr><th>الملمس</th><td>معجون سكري زيتاني مغذٍ غني بقبيات الكركديه</td></tr>
  <tr><th>العطر</th><td>عطر زهرة الكركديه والفرمار الساحر</td></tr>
  <tr><th>المكونات النشطة</th><td>بلورات السكر، زيت الأركان المغربي النقي، مسحوق زهرة الكركديه (Hibiscus)</td></tr>
  <tr><th>بلد المنشأ</th><td>المغرب (Morocco)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Jardin d'Oléane Morocco</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زهرة الكركديه وزيت الأركان في مقشر جاردن دي أوليان (Jardin d'Oléane)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مقشر جاردن دي أوليان بالكركديه والأركان مشكلة بهتان وجفاف بشرة الجسم، التراكمات القرنية الميتة، وفقدان الإشراق التوريدي الطبيعي.</p>

<h3>لماذا تنجح تركيبة الكركديه والأركان والسكر؟</h3>
<p>لأن بلورات السكر تذوب تدريجياً بالتدليك لتقشير لطيف، الكركديه الغني بمضادات الأكسدة الأحماض النباتية يوحد اللون ويمنح التوريد، والأركان يغذي عمقاً.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام على بشرة مبللة دافئة:</strong> يسهل ذوبان السكر وامتصاص زيت الأركان.<br>
2. <strong>عدم الغسيل بالصابون بعد المقشر:</strong> لترك طبقة زيت الأركان المغذية على الجسم.<br>
3. <strong>الاستخدام 1-2 مرة أسبوعياً:</strong> يضمن الحصول على أقصى درجات التوريد والنعومة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مقشرات السكر تسبب جروحاً ميكروية في جلد الجسم."<br>
<strong>الحقيقة:</strong> بلورات السكر في جاردن دي أوليان كروية ومحاطة بزيت الأركان لتضمن تقشيراً ناعماً ودون جروح.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تمنح أحماض ألفا هيدروكسي الطبيعية (AHA) في زهرة الكركديه تقشيراً كيميائياً خفيفاً يكمل التقشير الميكانيكي لبلورات السكر.</p>"""

    faqs = [
        ("ما هو مقشر السكر بزيت الأركان ومسحوق زهرة الكركديه من جاردن دي أوليان 600جم؟", "هو مقشر سكر مغربي فاخر من جاردن دي أوليان بزيت الأركان ومسحوق زهرة الكركديه لتوريد وتقشير وترطيب الجسم (600 جم)."),
        ("ما هي فوائد زيت الأركان وزهرة الكركديه وبلورات السكر؟", "تقشر بلورات السكر الجلد الميت، يغذي زيت الأركان البشرة بالأوميقا وفيتامين E، وتمنح الكركديه توريداً وإشراقاً وردياً."),
        ("هل يعطي الجسم توريداً وإشراقاً وردياً ملكياً؟", "نعم، مسحوق زهرة الكركديه يمنح البشرة توهجاً وتوريداً وردياً ناعماً."),
        ("ما وزن العبوة؟", "تأتي بعبوة ضخمة بوزن 600 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "دلكي على جسم مبلل بالماء الدافئ بحركات دائرية، اشطفي بالماء الفاتر دون صابون بعده 1-2 مرة أسبوعياً."),
        ("هل هو منتج أصلي صنع في المغرب؟", "نعم، صُنع بفخر في المغرب بواسطة Jardin d'Oléane Morocco."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات جاردن دي أوليان لدى إكليل أبها أصلية 100%."),
        ("هل يترك الجسم مرطباً بزيت الأركان؟", "نعم، يترك طبقة مخملية مرطبة من زيت الأركان النقي على الجلد."),
        ("ما رائحة مقشر الكركديه من جاردن دي أوليان؟", "عطر زهرة الكركديه المغربية الساحرة الناعمة."),
        ("هل يناسب جميع أنواع بشرة الجسم؟", "نعم، مناسب لجميع أنواع بشرة الجسم."),
        ("هل 600 جم تكفي لفترة طويلة؟", "نعم، عبوة ضخمة 600 جم تكفي لعدة أشهر من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف محكم الإغلاق."),
        ("هل يناسب الوجه؟", "مخصص لبشرة الجسم فقط ولا يُستعمل للوجه."),
        ("كم مرة أسبوعياً؟", "1-2 مرة أسبوعياً لنتائج مثالية."),
        ("هل يساعد في تنعيم المرفقين والركبتين؟", "نعم، ينعم المرفقين والركبتين والمناطق الخشنة بفاعلية."),
        ("هل جاردن دي أوليان علامة مغربية رائدة؟", "نعم، Jardin d'Oléane من أبرز وأشهر الماركات المغربية للسبا والتجميل."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع تشقق وجفاف الجلد في الشتاء؟", "نعم، يحمي البشرة تماماً من الجفاف والتشقق الشتوي."),
        ("هل يناسب الاستخدام قبل التان والمناسبات؟", "نعم، يجهز البشرة ويعطيها توريداً ساحراً للمناسبات."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، بلورات السكر تذوب بالماء وينشطف بسهولة."),
        ("هل يناسب النساء والرجال؟", "مناسب للنساء والرجال من 16 سنة."),
        ("هل يصلح هدية فاخرة جداً للعرائس؟", "نعم، خيار هدية فاخر ومثالي جداً للعرائس."),
        ("هل يزيل التراكمات الجافة؟", "نعم، التقشير السكري يزيل كل التراكمات الجافة."),
        ("هل يغني عن استخدام مرطب بعده؟", "بفضل زيت الأركان النقي قد لا تحتاجين لمرطب إضافي بعده."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Jardin d'Oléane Sugar Scrub with Argan Oil and Hibiscus Flower Powder - 600g</strong> is a royal Moroccan sugar body scrub in a jumbo 600g tub from Jardin d'Oléane designed to exfoliate, hydrate, brighten, and restore a soft rosy glow to body skin. Formulated with natural sugar crystals, pure authentic Moroccan Argan Oil, and natural Hibiscus Flower Powder.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Gentle Deep Exfoliation with Natural Sugar Crystals:</strong> Removes buildup without scratching or irritating skin.</li>
  <li><strong>Superior Nourishment & Moisture Retention with Pure Moroccan Argan Oil:</strong> Feeds skin with fatty acids and Vitamin E.</li>
  <li><strong>Rosy Glow & Brightening with Hibiscus Flower Powder:</strong> Gives body skin a soft rosy blush and radiance.</li>
  <li><strong>Rich Sugar-Oil Texture:</strong> Glides smoothly leaving a velvety moisturizing finish.</li>
  <li><strong>Jumbo 600g Tub:</strong> Generous volume lasting months of regular weekly use.</li>
  <li><strong>100% Made in Morocco Spa Formulation:</strong> Authentic heritage in Moroccan skincare.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet body skin with warm water during shower to open pores.</li>
  <li><strong>Step 2 (Massage):</strong> Apply a suitable amount and massage in gentle circles focusing on rough areas.</li>
  <li><strong>Step 3 (Rinse):</strong> Rinse thoroughly with warm water without soap afterwards to lock in oils (use 1-2 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Sugar Crystals & Hibiscus Powder:</strong> Exfoliate dead skin while giving body skin a natural rosy blush and brightness.</li>
  <li><strong>Pure Moroccan Argan Oil:</strong> Nourishes skin with essential fatty acids and Vitamin E preserving elasticity.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application only (do not use on face).</li>
  <li>Avoid using on burns and open wounds.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Jardin d'Oléane Argan & Hibiscus 600g Sugar Scrub for rosy glowing, exfoliated, and hydrated body skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Jardin d'Oléane</td></tr>
  <tr><th>Category</th><td>Body Care / Jardin d'Oléane Moroccan Argan Sugar Scrubs 600g</td></tr>
  <tr><th>Product Type</th><td>Natural Argan Oil & Hibiscus Flower Powder Sugar Exfoliating Scrub (600g)</td></tr>
  <tr><th>Volume/Weight</th><td>600 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Including Dry & Dull Skin)</td></tr>
  <tr><th>Finish</th><td>Silky smooth, oil-hydrated, rosy glowing & even-toned body skin</td></tr>
  <tr><th>Texture</th><td>Rich oil-infused sugar paste with hibiscus flower particles</td></tr>
  <tr><th>Fragrance</th><td>Enchanting Moroccan Hibiscus flower scent</td></tr>
  <tr><th>Active Ingredients</th><td>Sugar Crystals, Pure Moroccan Argan Oil, Hibiscus Flower Powder</td></tr>
  <tr><th>Country of Origin</th><td>Morocco</td></tr>
  <tr><th>Manufacturer</th><td>Jardin d'Oléane Morocco</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Hibiscus AHA Chemical & Sugar Mechanical Dual Exfoliation with Argan Lipid Protection</h2>

<h3>What problem does this solve?</h3>
<p>Jardin d'Oléane Argan & Hibiscus Sugar Scrub resolves dull dry body skin, keratinized buildup, and loss of natural rosy glow.</p>

<h3>Why choose Jardin d'Oléane Argan & Hibiscus Scrub?</h3>
<p>Natural AHAs in Hibiscus flower powder provide mild chemical exfoliation complementing mechanical sugar crystal desquamation, while Argan oil fatty acids lock in moisture.</p>"""

    en_faqs = [
        ("What is Jardin d'Oléane Sugar Scrub with Argan Oil and Hibiscus Flower Powder - 600g?", "It is a royal Moroccan sugar scrub from Jardin d'Oléane with Argan Oil and Hibiscus Powder for exfoliating, hydrating, and imparting a rosy glow (600g)."),
        ("What are the benefits of Argan Oil, Hibiscus Powder, and Sugar Crystals?", "Sugar crystals exfoliate dead skin, Argan Oil nourishes with Vitamin E and omegas, and Hibiscus gives a soft rosy glow."),
        ("Does it impart a royal rosy glow to body skin?", "Yes, Hibiscus Flower Powder gives skin a soft rosy blush and radiant glow."),
        ("What weight is contained in this tub?", "600g jumbo tub."),
        ("How do I use it correctly?", "Massage onto warm damp skin in circular motions, rinse with warm water without soap afterwards 1-2 times weekly."),
        ("Is it authentic Made in Morocco?", "Yes, proudly made in Morocco by Jardin d'Oléane Morocco."),
        ("How do I verify authenticity at Ekleel Abha?", "All Jardin d'Oléane products at Ekleel Abha are 100% original."),
        ("Does it leave skin hydrated with Argan Oil?", "Yes, leaves a velvety moisturizing layer of pure Argan oil on skin."),
        ("What does Jardin d'Oléane Hibiscus Scrub smell like?", "Enchanting soft Moroccan Hibiscus flower scent."),
        ("Is it suitable for all body skin types?", "Yes, suitable for all body skin types."),
        ("Does the 600g tub last long?", "Yes, jumbo 600g tub lasts months of regular weekly use."),
        ("How should I store it?", "In a cool, dry place tightly closed."),
        ("Is it suitable for the face?", "Formulated for body skin only; do not use on face."),
        ("How many times weekly?", "1-2 times weekly for best results."),
        ("Does it help soften elbows and knees?", "Yes, effectively softens elbows, knees, and rough spots."),
        ("Is Jardin d'Oléane a leading Moroccan brand?", "Yes, Jardin d'Oléane is a premier Moroccan spa and beauty brand."),
        ("Is the tub recyclable?", "Yes."),
        ("Does it prevent winter dryness and cracking?", "Yes, shields skin against winter dryness."),
        ("Is it good before events and tanning?", "Yes, prepares skin giving a radiant rosy glow."),
        ("Does it rinse off easily?", "Yes, sugar crystals dissolve and rinse off smoothly with warm water."),
        ("Is it suitable for men and women?", "Suitable for men and women aged 16+."),
        ("Is it a luxury bridal gift?", "Yes, highly recommended luxury gift for brides."),
        ("Does it eliminate dry skin buildup?", "Yes, sugar exfoliation removes all dry buildup."),
        ("Does it eliminate the need for lotion afterwards?", "Pure Argan oil content often eliminates the need for post-shower lotion."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1926",
        "sku": "EK-1926",
        "gtin": "745114422330",
        "brand": "Jardin d'Oléane",
        "ar": {
            "title": "مقشر السكر بزيت الأركان ومسحوق زهرة الكركديه من جاردن دي اوليان - 600جم",
            "meta_title": "مقشر السكر بالكركديه والأركان جاردن دي أوليان 600جم | إكليل أبها",
            "meta_description": "اشتري مقشر السكر بزيت الأركان ومسحوق زهرة الكركديه من جاردن دي أوليان (600 جم). مقشر مغربي لتوريد وتقشير وترطيب الجسم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["جاردن_دي_اوليان", "مقشر_السكر", "زهرة_الكركديه", "زيت_الأركان", "إكليل_أبها"]
        },
        "en": {
            "title": "Jardin d'Oléane Sugar Scrub with Argan Oil and Hibiscus Flower Powder - 600g",
            "meta_title": "Jardin d'Oléane Argan & Hibiscus Sugar Scrub 600g | Ekleel Abha",
            "meta_description": "Buy original Jardin d'Oléane Sugar Scrub with Argan Oil & Hibiscus Powder (600g). Royal Moroccan exfoliating & hydrating scrub. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["jardin_doleane", "sugar_scrub", "hibiscus_flower", "argan_oil", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 42 builders complete")
