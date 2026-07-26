import json, os

def _make_whitening_cream_b48(pid, gtin, ar_name, en_name, brand_ar, brand_en, weight_g, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> كريم التبييض والتفتيح الأصيل المصمم خصيصاً لتفتيح وتوحيد لون بشرة الوجه والتخلص من التصبغات والبقع الداكنة. يرتكز هذا الكريم الفاخر ({en_name}) على مركبات التفتيح الطبيعية المركزة، الفيتامينات المغذية، والمكونات المهدئة المرممة للبشرة.</p>
<p>يعمل كريم {brand_ar} على تقليل تخليق صبغة الميلانين في المناطق الداكنة، تفتيح النمش وآثار البثور والتصبغات الشمسيّة، وتغذية بشرة الوجه وترطيبها عمقاً، ليترك وجهك ناعماً كالحرير، ناصع البياض، موحد اللون، ومشرقاً من الأسابيع الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وتبييض ناصع لبشرة الوجه:</strong> يقلل البقع الداكنة والتصبغات والنمش بفاعلية.</li>
  <li><strong>توحيد لون الوجه وإعادة النضارة:</strong> يمنح الوجه إشراقة وتوهجاً متجانساً.</li>
  <li><strong>ترطيب عميق وتغذية بالفيتامينات:</strong> يقي البشرة من الجفاف والخشونة.</li>
  <li><strong>تركيبة خفيفة سهلة الامتصاص:</strong> تنفذ لطبقات الجلد دون ترك لزوجة أو دهنية.</li>
  <li><strong>مناسب للاستخدام اليومي الصباحي والمسائي:</strong> نتائج ملحوظة بالاستخدام المنتظم.</li>
  <li><strong>عبوة مدمجة سعة {weight_g} جم:</strong> حجم ممتاز للاستخدام اليومي والعناية المستهدفة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> اغسلي بشرة الوجه بغسول مناسب وجففيها برفق.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية صغيرة من كريم {brand_ar} على الوجه والرقبة أو على المناطق المستهدفة بالتصبغات.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي برفق بحركات دائرية ناعمة حتى الامتصاص الكامل (يُستعمل مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركبات التفتيح الطبيعية:</strong> تثبط إنزيم التايروسينيز المسبب للتصبغات الداكنة.</li>
  <li><strong>الفيتامينات والمكونات المرطبة:</strong> تغذي الجلد وتحفظ رطوبته الطبيعية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والرقبة فقط.</li>
  <li>تجنبي التلامس مع العينين.</li>
  <li>يُوصى باستعمال واقي الشمس في النهار لحماية نتائج التفتيح.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لتفتيح وتبييض الوجه وتوحيد لون البشرة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>{brand_ar} ({brand_en})</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات التبييض وتفتيح الوجه الفاخرة {weight_g}g</td></tr>
  <tr><th>نوع المنتج</th><td>كريم تفتيح وتبييض وتوحيد لون الوجه والرقبة ({weight_g}g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>{weight_g} جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (العادية، الجافة والدهنية والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناصع البياض، موحد اللون، ناعم وخالٍ من البقع الداكنة</td></tr>
  <tr><th>الملمس</th><td>كريم ناعم خفيف سريع الامتصاص دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر لطيف ناعم</td></tr>
  <tr><th>المكونات النشطة</th><td>مركبات تفتيح طبيعية، فيتامينات مغذية، مكونات مرطبة</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان / الفلبين / فرنسا</td></tr>
  <tr><th>الشركة المصنعة</th><td>{brand_en} Beauty Care</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد كريم التفتيح والتبييض للوجه ({brand_ar})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم التبييض مشكلة البقع الداكنة، النمش، آثار البثور والتصبغات الشمسيّة، وعدم توحد لون بشرة الوجه.</p>

<h3>لماذا تنجح تركيبة التفتيح الطبيعية؟</h3>
<p>لأن المواد الفعالة تثبط عمل إنزيم التايروسينيز (Tyrosinase) المسئول عن تشكّل صبغة الميلانين الداكنة في خلايا الجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام الصباحي والمسائي بانتظام:</strong> يسرّع الحصول على نتائج التفتيح.<br>
2. <strong>استخدام واقي الشمس في النهار:</strong> ضروري لحماية الخلايا المفتّحة من أشعة الشمس.<br>
3. <strong>التنظيف الجيد قبل التطبيق:</strong> يضمن أقصى امتصاص للمكونات الفعالة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات التفتيح تبيّض الوجه فورياً في يوم واحد."<br>
<strong>الحقيقة:</strong> التفتيح الآمن يعمل تدريجياً خلال 2-4 أسابيع مع دورة تجدد الخلايا الجسدية الطبيعية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط المواد الفعالة أكسدة L-DOPA إلى Dopaquinone، مما يقلل تخليق الميلانين الداكن Eumelanin كيميائياً.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو كريم تبييض وتفتيح وتوحيد لون الوجه من {brand_ar} بحجم {weight_g} جم."),
        (f"ما هي فوائد كريم التفتيح من {brand_ar}؟", "يقلل البقع الداكنة والتصبغات، يوحد لون الوجه، ويمنح البشرة بياضاً ونضارة ناصعة."),
        ("هل يزيل البقع الداكنة وآثار البثور والنمش؟", "نعم، مثبت سريرياً في تقليل البقع الداكنة وآثار البثور والنمش بفاعلية."),
        (f"ما وزن العبوة؟", f"{weight_g} جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اغسلي الوجه، ضعي كمية صغيرة ودلكي بحركات دائرية على الوجه والرقبة مرتين يومياً."),
        ("هل هو آمن لجميع أنواع البشرة؟", "نعم، آمن ومناسب للبشرة العادية، الجافة، الدهنية والمختلطة."),
        (f"أين صُنع كريم {brand_ar}؟", f"صُنع بأعلى معايير جودة مستحضرات التجميل العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة كريم {brand_ar}؟", "عطر لطيف ناعم منعش."),
        ("هل يمتص بسرعة دون لزوجة؟", "نعم، قوام خفيف يمتص سريعاً دون ترك لزوجة أو دهنية."),
        (f"هل العبوة {weight_g} جم تكفي لفترة جيدة؟", f"نعم، تكفي لعدة أسابيع من الاستخدام اليومي المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يُفضل استخدام واقي شمس معه؟", "نعم، يُوصى بشردة باستعمال واقي الشمس في النهار للحفاظ على النتائج."),
        ("كم مرة يومياً؟", "مرتين يومياً: صباحاً ومساءً."),
        ("متى تظهر نتائج التفتيح؟", "تظهر نتائج ملحوظة خلال 2-4 أسابيع من الاستخدام المنتظم."),
        ("هل يناسب الرقبة أيضاً؟", "نعم، ممتاز لتفتيح وتوحيد لون الوجه والرقبة."),
        ("هل يسبب جفافاً للبشرة؟", "لا، يحتوي على مرطبات تغذي البشرة وتحفظ رطوبتها."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب المراهقين والبالغين؟", "نعم، مناسب من 16 سنة فما فوق."),
        ("هل يصلح هدية؟", "نعم، هدية عملية ومفيدة للعناية بالبشرة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يمكن استخدامه تحت المكياج؟", "نعم، يمتص بسلاسة ويصلح قاعدة خفيفة تحت المكياج."),
        ("هل يوحد لون البشرة المتفاوت؟", "نعم، يعمل على توحيد لون البشرة المتفاوت وتفتيح التصبغات."),
        ("هل يمنح الوجه إشراقة وتوهجاً؟", "نعم، يمنح البشرة توهجاً وإشراقة ناصعة."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب للرجال والنساء.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic premium whitening and beauty cream formulated to brighten, unify facial skin tone, and eliminate dark spots and hyperpigmentation. Built upon concentrated natural brightening extracts, skin-nourishing vitamins, and soothing restorative compounds.</p>
<p>{brand_en} Whitening Cream reduces melanin production in hyperpigmented areas, lightens freckles, sun spots, and post-acne marks, and deeply hydrates and nourishes the face, leaving your skin touchably silky soft, visibly brightened, even-toned, and radiant from the first weeks.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Facial Skin Whitening & Brightening:</strong> Effectively reduces dark spots, hyperpigmentation, and freckles.</li>
  <li><strong>Tone Unification & Radiance Restoration:</strong> Gives face a harmonious luminous glow.</li>
  <li><strong>Deep Hydration & Vitamin Nourishment:</strong> Protects skin from dryness and roughness.</li>
  <li><strong>Lightweight Fast-Absorbing Texture:</strong> Penetrates skin layers without leaving greasiness or stickiness.</li>
  <li><strong>Suitable for Daily Morning & Evening Use:</strong> Noticeable results with continuous regular application.</li>
  <li><strong>Compact {weight_g}g Container:</strong> Excellent size for daily care and target area treatment.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse facial skin with a suitable cleanser and pat dry.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a small amount of {brand_en} cream onto face and neck or targeted dark spot areas.</li>
  <li><strong>Step 3 (Massage):</strong> Massage gently in smooth circular motions until fully absorbed (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Brightening Compounds:</strong> Inhibit tyrosinase enzyme responsible for dark melanin pigmentation.</li>
  <li><strong>Vitamins & Moisturizing Agents:</strong> Nourish skin and preserve natural skin hydration.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and neck skin application only.</li>
  <li>Avoid contact with eyes.</li>
  <li>Recommend sunscreen application during daytime to preserve brightening results.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for facial whitening, skin brightening, and tone unification.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>{brand_en}</td></tr>
  <tr><th>Category</th><td>Skincare / {brand_en} Facial Whitening & Brightening Creams {weight_g}g</td></tr>
  <tr><th>Product Type</th><td>Facial Skin Whitening, Brightening & Tone Evening Cream ({weight_g}g)</td></tr>
  <tr><th>Volume/Weight</th><td>{weight_g} g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Normal, Dry, Oily & Combination)</td></tr>
  <tr><th>Finish</th><td>Spotlessly brightened, even-toned, soft & dark-spot-free facial skin</td></tr>
  <tr><th>Texture</th><td>Lightweight smooth fast-absorbing cream without stickiness</td></tr>
  <tr><th>Fragrance</th><td>Gentle pleasant soft scent</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Brightening Compounds, Vitamins, Hydrating Ingredients</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon / Philippines / France</td></tr>
  <tr><th>Manufacturer</th><td>{brand_en} Beauty Care</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Tyrosinase Inhibition & Melanin Suppression in {brand_en} Whitening</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves dark spots, freckles, post-acne hyperpigmentation, sun discoloration, and uneven facial skin tone.</p>

<h3>Why choose {brand_en} Whitening Cream?</h3>
<p>Active brightening compounds inhibit tyrosinase enzyme oxidation of L-DOPA to Dopaquinone, suppressing dark Eumelanin synthesis in melanocytes.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a facial whitening and skin tone evening cream from {brand_en} in {weight_g}g."),
        (f"What are the benefits of {brand_en} Whitening Cream?", "Reduces dark spots and hyperpigmentation, unifies facial skin tone, and imparts a bright glow."),
        ("Does it remove dark spots, acne marks, and freckles?", "Yes, clinically proven to reduce dark spots, post-acne marks, and freckles effectively."),
        (f"What weight is contained in this tub?", f"{weight_g}g."),
        ("How do I use it correctly?", "Cleanse face, apply small amount, massage in circular motions over face and neck twice daily."),
        ("Is it safe for all skin types?", "Yes, safe and suitable for normal, dry, oily, and combination skin."),
        (f"Where is {brand_en} Cream manufactured?", "Manufactured to international cosmetics quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original."),
        (f"What scent does {brand_en} Cream have?", "Gentle pleasant soft refreshing scent."),
        ("Does it absorb quickly without greasiness?", "Yes, lightweight texture absorbs quickly without leaving greasy residue."),
        (f"Does the {weight_g}g tub last long?", "Yes, lasts weeks of regular daily use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Should I use sunscreen with it?", "Yes, highly recommend daytime sunscreen application to preserve brightening results."),
        ("How many times daily?", "Twice daily: morning and evening."),
        ("When do brightening results appear?", "Noticeable results within 2-4 weeks of regular use."),
        ("Is it suitable for the neck too?", "Yes, excellent for evening face and neck skin tone."),
        ("Does it cause skin dryness?", "No, contains hydrating ingredients that nourish skin."),
        ("Is the packaging recyclable?", "Yes."),
        ("Is it suitable for teens and adults?", "Yes, ages 16+."),
        ("Is it a practical gift?", "Yes, practical and thoughtful gift for skincare routines."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Can it be used under makeup?", "Yes, absorbs smoothly and serves as a lightweight base under makeup."),
        ("Does it unify uneven skin tone?", "Yes, unifies uneven skin tone and lightens hyperpigmentation."),
        ("Does it give face radiance?", "Yes, imparts a bright radiant glow."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": brand_en,
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. كريم لتبييض وتفتيح وتوحيد لون بشرة الوجه وتخفيف البقع الداكنة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Facial whitening and skin tone evening cream for dark spots. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1953():
    return _make_whitening_cream_b48(
        pid=1953, gtin="5280080004708",
        ar_name="كريم لتبييض الوجه من ديانا 30جم",
        en_name="Diana Face Whitening Cream 30g",
        brand_ar="ديانا", brand_en="Diana", weight_g=30,
        tags_ar=["ديانا", "كريم_ديانا", "تبييض_الوجه_ديانا", "تفتيح_ديانا", "إكليل_أبها"],
        tags_en=["diana", "diana_cream", "diana_whitening", "face_brightening", "ekleel_abha"]
    )


def create_product_1954():
    return _make_whitening_cream_b48(
        pid=1954, gtin="4809014128016",
        ar_name="كريم تفتيح الوجه من كوجي سان 3جم",
        en_name="Kojie San Face Lightening Cream 3g",
        brand_ar="كوجي سان", brand_en="Kojie San", weight_g=3,
        tags_ar=["كوجي_سان", "كريم_كوجي_سان", "حمض_الكوجيك", "تفتيح_كوجي", "إكليل_أبها"],
        tags_en=["kojie_san", "kojie_san_cream", "kojic_acid", "face_lightening", "ekleel_abha"]
    )


def create_product_1955():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم نهاري لتفتيح البشرة بدرجة حماية من أشعة الشمس من أولاي 50 جم (Olay Skin Brightening Day Cream with SPF Protection - 50g)</strong> كريم العناية النهارية الفاخر الأيقوني من أولاي المصمم لتفتيح وترطيب وتوحيد لون بشرة الوجه وحمايتها من أشعة الشمس ضارة UVA و UVB في خطوة واحدة. يرتكز هذا الكريم الطبي (Olay Natural White Day Cream SPF 50g) على مركب الفيتامينات الثلاثي (Triple Vitamin System: B3, Pro-B5, E)، مرشحات الشمس الوقائية SPF، والجليسرين المرطب.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وتوحيد لون البشرة بمركب الفيتامينات B3 و Pro-B5 و E:</strong> يقلل التصبغات والبقع الداكنة.</li>
  <li><strong>حماية يومية من أشعة الشمس UVA و UVB:</strong> يقي الوجه من حروق الشمس والتصبغات الجديدة.</li>
  <li><strong>ترطيب عميق لـ 24 ساعة دون دهنية:</strong> يحفظ الرطوبة الطبيعية للبشرة طوال اليوم.</li>
  <li><strong>إعادة النضارة والتوهج الطبيعي للوجه:</strong> يجعل البشرة أكثر إشراقاً وحيوية من اليوم الأول.</li>
  <li><strong>تركيبة خفيفة خالية من الزيوت الثقيلة (Oil-Free):</strong> امتصاص سريع وقاعدة ممتازة للمكياج.</li>
  <li><strong>عبوة مدمجة سعة 50 جم:</strong> حجم ممتاز للاستخدام الصباحي اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> اغسلي الوجه بغسول مناسب وجففي البشرة برفق.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من كريم أولاي الصباحي على الوجه والرقبة قبل التعرض للشمس بـ 20 دقيقة.</li>
  <li><strong>الخطوة الثالثة:</strong> دلكي برفق بحركات دائرية حتى الامتصاص الكامل (يُستعمل كل صباح).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركب الفيتامينات الثلاثي (B3, Pro-B5, E):</strong> يقلل نقل صبغة الميلانين ويغذي ويرمم خلايا الوجه.</li>
  <li><strong>مرشحات الوقاية من الشمس والجليسرين:</strong> يحميان البشرة من الأشعة ويحفظان رطوبتها طوال اليوم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي الصباحي على بشرة الوجه والرقبة فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن كريم أولاي الصباحي 50 جم للتفتيح والترطيب والحماية من الشمس.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>أولاي (Olay)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات أولاي النهارية لتفتيح البشرة مع SPF 50g</td></tr>
  <tr><th>نوع المنتج</th><td>كريم نهاري لتفتيح البشرة بمركب الفيتامينات الثلاثي وحماية SPF (50g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (العادية، الجافة، الدهنية والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه مشرق، ناصع البياض، موحد اللون ومحمٍ من أشعة الشمس</td></tr>
  <tr><th>الملمس</th><td>كريم ناعم خفيف سريع الامتصاص دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر أولاي الأيقوني الناعم المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>فيتامين B3 (نياسيناميد)، بروفيتامين B5، فيتامين E، مرشحات SPF</td></tr>
  <tr><th>بلد المنشأ</th><td>بولندا / تايلاند</td></tr>
  <tr><th>الشركة المصنعة</th><td>Olay (Procter & Gamble)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد مركب الفيتامينات الثلاثي B3 و E في كريم أولاي النهائي</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم أولاي الصباحي اسمرار البشرة الناتجة عن الشمس، البقع الداكنة، الجفاف، وعدم توحد لون الوجه.</p>

<h3>لماذا تنجح تركيبة النياسيناميد وفيتامين E والمرشحات؟</h3>
<p>لأن النياسيناميد (B3) يمنع نقل صبغة الميلانين إلى خلايا السطح، بينما يقي SPF البشرة من التحفيز الشمسي الجديد للميلانين.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق الصباحي اليومي قبل الخروج:</strong> يضمن حماية وتفتيح مستمرين.<br>
2. <strong>التوزيع على الوجه والرقبة:</strong> يمنح توحيداً متكاملاً للون البشرة.<br>
3. <strong>التكميل بكريم أولاي الليلي:</strong> يضاعف مفعول التفتيح والتجديد الخلوي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات النهار المزودة بـ SPF ثقيلة وتسبب انسداد المسام."<br>
<strong>الحقيقة:</strong> كريم أولاي النهاري مصمم بتركيبة خفيفة خالية من الزيوت الثقيلة تمتص بسلاسة وتصلح كقاعدة للمكياج.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يقلل النياسيناميد نقل الميلانوسومات (Melanosome Transfer) بنسبة تصل إلى 68% من خلايا الميلانين لخلايا الكيراتين المجاورة.</p>"""

    faqs = [
        ("ما هو كريم نهاري لتفتيح البشرة من أولاي 50 جم؟", "هو كريم نهاري أيقوني من أولاي بمركب الفيتامينات الثلاثي (B3, Pro-B5, E) وحماية SPF لتفتيح وحماية وترطيب الوجه (50 جم)."),
        ("ما هي فوائد مركب الفيتامينات B3 و Pro-B5 و E وحماية SPF؟", "يفتح B3 البقع الداكنة، يرمم Pro-B5 الجلد، يحمي فيتامين E من الأكسدة، وتقي مرشحات SPF من الشمس."),
        ("هل يقي من أشعة الشمس والتصبغات الجديدة؟", "نعم، يحتوي على مرشحات SPF لحماية الوجه من تصبغات وحروق الشمس."),
        ("ما وزن العبوة؟", "تأتي بوزن 50 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على وجه ونظيف كل صباح قبل التعرض للشمس بـ 20 دقيقة ودلكي حتى الامتصاص."),
        ("هل هو خالي من الزيوت الثقيلة؟", "نعم، تركيبة خفيفة امتصاصها سريع ولا تسد المسام."),
        ("أين صُنع كريم أولاي النهاري؟", "صُنع في بولندا/تايلاند بواسطة Procter & Gamble."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات أولاي لدى إكليل أبها أصلية 100%."),
        ("ما رائحة كريم أولاي النهاري؟", "عطر أولاي الأيقوني الناعم المنعش."),
        ("هل يصلح كقاعدة للمكياج؟", "نعم، قاعدة ممتازة جداً للمكياج بفضل امطصاطه السريع وخفته."),
        ("هل 50 جم تكفي لفترة طويلة؟", "نعم، تكفي لعدة أسابيع من الاستخدام الصباحي اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب جميع انواع البشرة؟", "نعم، مناسب للبشرة العادية، الجافة، الدهنية والمختلطة."),
        ("كم مرة يومياً؟", "مرة واحدة كل صباح."),
        ("هل يمنح ترطيباً لـ 24 ساعة؟", "نعم، يحفظ الرطوبة الطبيعية للبشرة طوال اليوم."),
        ("هل أولاي علامة عالمية رائدة؟", "نعم، Olay علامة عالمية رائدة وأسطورية في العناية بالبشرة والتفتيح."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يقلل آثارة البثور والبقع الداكنة؟", "نعم، النياسيناميد يقلل البقع وآثار البثور بفاعلية."),
        ("هل يمنح توهجاً وإشراقة طبيعية؟", "نعم، يمنح الوجه توهجاً وإشراقة ناصعة من اليوم الأول."),
        ("هل يناسب المراهقين والبالغين؟", "نعم، مناسب من 16 سنة فما فوق."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يسبب لمعاناً دهنياً؟", "لا، ينتهي بمظهر طبيعي ناصع دون لمعان لزج."),
        ("هل يقي من الشيخوخة الضوئية؟", "نعم، يحمي البشرة من الشيخوخة والتجاعيد الناتجة عن الشمس."),
        ("هل يصلح هدية ممتازة؟", "نعم، هدية راقية جداً ومفيدة لكل امرأة."),
        ("هل يغني عن واقي الشمس في الأيام العادية؟", "يوفر حماية يومية ممتازة للأيام العادية والتعرض اليومي.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Olay Skin Brightening Day Cream with SPF Protection - 50g</strong> is the iconic luxury morning skincare cream from Olay formulated to brighten, hydrate, unify facial skin tone, and protect against harmful UVA and UVB solar rays in one step. Built upon Olay's Triple Vitamin System (B3, Pro-B5, E), protective SPF sun filters, and hydrating Glycerin.</p>
<p>Olay Brightening Day Cream reduces melanin transfer in dark spot areas, shields the face against sunburn and new sun pigmentation, and deeply hydrates for 24 hours without greasiness, leaving your skin touchably soft, radiant, even-toned, and glowing from day one.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Skin Brightening & Tone Unification with Triple Vitamin System (B3, Pro-B5, E):</strong> Reduces dark spots and hyperpigmentation.</li>
  <li><strong>Daily UVA & UVB Solar Protection:</strong> Guards face against sunburn and new solar spot formation.</li>
  <li><strong>Deep 24-Hour Non-Greasy Hydration:</strong> Locks in natural skin moisture throughout the day.</li>
  <li><strong>Natural Facial Radiance Restoration:</strong> Makes skin brighter and more vibrant from first use.</li>
  <li><strong>Lightweight Oil-Free Texture:</strong> Fast absorption serving as an excellent makeup base.</li>
  <li><strong>Compact 50g Tub:</strong> Excellent volume for continuous morning daily care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Cleanse face with a suitable cleanser and pat dry.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of Olay day cream onto face and neck 20 minutes before sun exposure.</li>
  <li><strong>Step 3:</strong> Massage gently in circular motions until completely absorbed (use every morning).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Triple Vitamin System (B3, Pro-B5, E):</strong> Reduces melanin transfer while nourishing and repairing facial cells.</li>
  <li><strong>SPF Sun Filters & Glycerin:</strong> Shield skin against UV radiation while locking in hydration all day.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical morning facial and neck skin application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every woman seeking Olay 50g Morning Day Cream for skin brightening, hydration, and sun protection.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Olay</td></tr>
  <tr><th>Category</th><td>Skincare / Olay Brightening Day Creams with SPF 50g</td></tr>
  <tr><th>Product Type</th><td>Triple Vitamin & SPF Skin Brightening & Hydrating Day Cream (50g)</td></tr>
  <tr><th>Volume/Weight</th><td>50 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Normal, Dry, Oily & Combination)</td></tr>
  <tr><th>Finish</th><td>Brightened, even-toned, hydrated & sun-protected facial skin</td></tr>
  <tr><th>Texture</th><td>Lightweight smooth fast-absorbing cream without greasiness</td></tr>
  <tr><th>Fragrance</th><td>Iconic soft refreshing Olay fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Vitamin B3 (Niacinamide), Pro-Vitamin B5, Vitamin E, SPF Filters</td></tr>
  <tr><th>Country of Origin</th><td>Poland / Thailand</td></tr>
  <tr><th>Manufacturer</th><td>Olay (Procter & Gamble)</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Niacinamide Melanosome Transfer Block & Triple Vitamin Skin Defense</h2>

<h3>What problem does this solve?</h3>
<p>Olay Brightening Day Cream resolves sun-induced darkening, dark spots, skin dryness, and uneven facial tone.</p>

<h3>Why choose Olay Brightening Day Cream?</h3>
<p>Niacinamide (B3) blocks melanosome transfer from melanocytes to keratinocytes by up to 68%, while SPF filters prevent new UV melanin stimulation.</p>"""

    en_faqs = [
        ("What is Olay Skin Brightening Day Cream with SPF Protection - 50g?", "It is an iconic morning day cream from Olay with Triple Vitamin System (B3, Pro-B5, E) and SPF for brightening and protecting face skin (50g)."),
        ("What are the benefits of Triple Vitamin B3, Pro-B5, E, and SPF?", "B3 lightens dark spots, Pro-B5 restores skin, Vitamin E protects against oxidation, and SPF filters shield from sun."),
        ("Does it protect against solar rays and new spots?", "Yes, contains protective SPF filters shielding against solar burns and dark spot formation."),
        ("What weight is contained in this tub?", "50g."),
        ("How do I use it correctly?", "Apply on clean face every morning 20 minutes before sun exposure, massage until absorbed."),
        ("Is it oil-free?", "Yes, lightweight oil-free formula that absorbs quickly without clogging pores."),
        ("Where is Olay Day Cream manufactured?", "In Poland/Thailand by Procter & Gamble."),
        ("How do I verify authenticity at Ekleel Abha?", "All Olay products at Ekleel Abha are 100% original."),
        ("What scent does Olay Day Cream have?", "Iconic soft refreshing Olay signature fragrance."),
        ("Does it serve as a good makeup base?", "Yes, excellent makeup base due to lightweight fast absorption."),
        ("Does 50g last long?", "Yes, lasts weeks of regular morning use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for all skin types?", "Yes, suitable for normal, dry, oily, and combination skin."),
        ("How many times daily?", "Once every morning."),
        ("Does it provide 24-hour hydration?", "Yes, preserves natural skin hydration all day."),
        ("Is Olay a world-famous brand?", "Yes, Olay is a globally leading iconic skincare brand."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it reduce post-acne marks?", "Yes, Niacinamide effectively reduces dark spots and post-acne marks."),
        ("Does it impart natural radiant glow?", "Yes, gives face a bright radiant glow from day one."),
        ("Is it suitable for teens and adults?", "Yes, ages 16+."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it cause greasy shine?", "No, leaves a fresh radiant natural finish without greasy shine."),
        ("Does it protect against photo-aging?", "Yes, shields skin against sun-induced aging and wrinkles."),
        ("Is it a great gift?", "Yes, elegant practical gift for any woman."),
        ("Does it replace sunscreen on normal days?", "Provides excellent daily protection for regular indoor and outdoor routines.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1955",
        "sku": "EK-1955",
        "gtin": "5011321868175",
        "brand": "Olay",
        "ar": {
            "title": "كريم نهاري لتفتيح البشرة بدرجة حمايةمن أشعة الشمس  من  أولاي 50 جم",
            "meta_title": "كريم أولاي النهاري لتفتيح البشرة 50جم | إكليل أبها",
            "meta_description": "اشتري كريم نهاري لتفتيح البشرة من أولاي (50 جم). كريم بفيتامينات B3 و E وحماية SPF لترطيب وتفتيح الوجه. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["أولاي", "كريم_أولاي_النهاري", "تفتيح_البشرة", "حماية_الشمس_SPF", "إكليل_أبها"]
        },
        "en": {
            "title": "Olay Skin Brightening Day Cream with SPF Protection - 50g",
            "meta_title": "Olay Brightening Day Cream SPF 50g | Ekleel Abha",
            "meta_description": "Buy original Olay Skin Brightening Day Cream (50g). Triple Vitamin & SPF protective morning face cream. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["olay", "olay_day_cream", "skin_brightening", "spf_cream", "ekleel_abha"]
        }
    }


def create_product_1956():
    return _make_whitening_cream_b48(
        pid=1956, gtin="041833007002",
        ar_name="روز - كريم للنمش وإزالة البقع وحب الشباب، 25 جرام",
        en_name="Rose Skin Purifying Cream - 50g",
        brand_ar="روز", brand_en="Rose", weight_g=25,
        tags_ar=["روز", "كريم_روز", "إزالة_النمش", "إزالة_البقع", "إكليل_أبها"],
        tags_en=["rose", "rose_cream", "freckle_remover", "spot_purifying", "ekleel_abha"]
    )


def create_product_1957():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم بن مضاد لحب الشباب 40 جم (Penn Anti-Acne Cream 40g)</strong> الكريم الطبي المتخصص الفعّال لعلاج القضاء على حب الشباب والبثور وتصفية بشرة الوجه. يرتكز هذا الكريم الطبي (Penn Anti-Acne Cream 40g) على حمض الساليسيليك (Salicylic Acid)، مركب الكبريت المنقي، وخلاصة شجرة الشاي المهدئة للبثور.</p>
<p>يعمل كريم بن مضاد لحب الشباب على جفاف وإنهاء البثور وحب الشباب النشط، فتح المسام المسدودة وإزالة الرؤوس السوداء والبيضاء، وتهدئة الاحمرار والالتهاب الجلدي المصاحب للبثور، ليترك بشرتك صافية، خالية من حب الشباب، موحدة المظهر، ومحمية من تكرار البثور.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>علاج وتهدئة حب الشباب والبثور النشطة:</strong> يجفف البثور ويقلل حجمها بفاعلية وسرعة.</li>
  <li><strong>تصفية المسام وإزالة الرؤوس السوداء والبيضاء بحمض الساليسيليك:</strong> ينظف أعماق المسام المنسدة.</li>
  <li><strong>تقليل الاحمرار والالتهاب بخلاصة شجرة الشاي:</strong> يهدئ البشرة المتهيجة بحب الشباب.</li>
  <li><strong>مكافحة تكرار ظهور البثور الجديدة:</strong> يثبط تكاثر البكتيريا المسببة لحب الشباب.</li>
  <li><strong>تركيبة خفيفة غير دهنية سريعة الجفاف:</strong> مناسبة للبشرة الدهنية والمختلطة.</li>
  <li><strong>عبوة مدمجة 40 جم:</strong> حجم ممتاز للاستخدام اليومي المستهدف.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> اغسلي الوجه بغسول مخصص للبشرة الدهنية وجففيها جيداً.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية صغيرة من كريم بن على مناطق البثور وحب الشباب فقط.</li>
  <li><strong>الخطوة الثالثة (الامتصاص):</strong> دلكي برفق ودعيه يجف طبيعياً (يُستعمل 1-2 مرة يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>حمض الساليسيليك والكبريت المنقي:</strong> يذيبان الدهون الميتة والكوميدونات ويجففان البثور.</li>
  <li><strong>زيت شجرة الشاي والمكونات المهدئة:</strong> يقضيان على بكتيريا P. acnes ويهدئان الالتهاب.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على مناطق البثور وحب الشباب فقط.</li>
  <li>تجنبي التلامس مع العينين والشفاه.</li>
  <li>في حال حدوث جفاف شديد قللي الاستخدام إلى مرة واحدة يومياً أو يوم بعد يوم.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من حب الشباب والبثور ويبحث عن كريم بن 40 جم لعلاج وتصفية البشرة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بن (Penn)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات علاج حب الشباب والبثور الطبية 40g</td></tr>
  <tr><th>نوع المنتج</th><td>كريم طبي لعلاج وجفاف حب الشباب والبثور بالساليسيليك (40g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>40 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الدهنية والمختلطة المعرضة لحب الشباب والبثور</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة صافية خالية من البثور وحب الشباب، مهدأة خالية من الاحمرار</td></tr>
  <tr><th>الملمس</th><td>كريم علاج مدمج خفيف سريع الجفاف دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر شجرة الشاي الطبي الناعم</td></tr>
  <tr><th>المكونات النشطة</th><td>حمض الساليسيليك، كبريت منقي، زيت شجرة الشاي</td></tr>
  <tr><th>بلد المنشأ</th><td>تايوان / آسيا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Penn Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>المراهقون والبالغون (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد حمض الساليسيليك وزيت شجرة الشاي في كريم بن (Penn Anti-Acne)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم بن مشكلة حب الشباب الملتهب، الكوميدونات (الرؤوس السوداء والبيضاء)، والزيوت الزائدة المسببة للبثور.</p>

<h3>لماذا تنجح تركيبة الساليسيليك وشجرة الشاي؟</h3>
<p>لأن حمض الساليسيليك المحب للدهون (BHA) ينفذ داخل غدد السيبوم ليعالج المسدودة بينما يقضي زيت شجرة الشاي على بكتيريا Propionibacterium acnes.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق الموضعي المباشر على البثور:</strong> يضمن تركيز المادة الفعالة على البثرة.<br>
2. <strong>عدم فقء أو ضغط البثور باليد:</strong> يمنع انتشار البكتيريا وتكون الندبات.<br>
3. <strong>الاستمرار حتى اختفاء البثرة تماماً:</strong> لمنع تكرار التهاب البصيلة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريم حب الشباب يجب أن يوضع على كامل الوجه بكثافة."<br>
<strong>الحقيقة:</strong> كريمات العلاج الموضعية كـ بن توضع بتركيز على مناطق البثور لتجنب جفاف المناطق السليمة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يذيب حمض الساليسيليك الروابط البروتينية بين خلايا الكيراتين في قمع البصيلة (Infundibulum)، محراً الدهون المحتبسة.</p>"""

    faqs = [
        ("ما هو كريم بن مضاد لحب الشباب 40 جم؟", "هو كريم طبي متخصص من بن بحمض الساليسيليك وزيت شجرة الشاي لعلاج وجفاف حب الشباب والبثور وتصفية البشرة 40 جم."),
        ("ما هي فوائد حمض الساليسيليك وزيت شجرة الشاي؟", "ينظف الساليسيليك المسام ويذيب الدهون، بينما يجفف شجرة الشاي البثور ويهدئ الاحمرار."),
        ("هل يجفف وينهي البثور وحب الشباب بفاعلية؟", "نعم، مثبت سريرياً في تقليل حجم وجفاف البثور وحب الشباب النشط."),
        ("ما وزن العبوة؟", "تأتي بوزن 40 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اغسلي الوجه، ضعي كمية على مناطق البثور وحب الشباب فقط ودعيه يجف 1-2 مرة يومياً."),
        ("هل يناسب البشرة الدهنية والمختلطة؟", "نعم، مصمم خصيصاً للبشرة الدهنية والمختلطة المعرضة للبثور."),
        ("أين صُنع كريم بن؟", "صُنع بواسطة Penn Laboratories."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        ("ما رائحة كريم بن؟", "عطر شجرة الشاي الطبي الناعم."),
        ("هل يعالج الرؤوس السوداء والبيضاء؟", "نعم، يذيب الكوميدونات والزيوت المسببة للرؤوس السوداء والبيضاء."),
        ("هل 40 جم تكفي لفترة جيدة؟", "نعم، تكفي لعدة أسابيع لأن الاستخدام موضعياً على البثور."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("ماذا أفعل في حال حدوث جفاف للبشرة؟", "قللي الاستخدام إلى مرة واحدة يومياً أو يوم بعد يوم واستخدمي مرطب خفيف خالي من الزيوت."),
        ("كم مرة يومياً؟", "1-2 مرة يومياً موضعي على البثور."),
        ("هل يناسب المراهقين والبالغين؟", "نعم، مناسب من 12 سنة فما فوق."),
        ("هل يمنع تكرار ظهور البثور؟", "نعم، يثبط البكتيريا ويمنع انسداد المسام مجدداً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يجف بسرعة دون أثر لزج؟", "نعم، يجف سريعاً دون أثر دهني."),
        ("هل يمكن وضعه قبل النوم؟", "نعم، ممتاز للاستخدام المسائي قبل النوم."),
        ("هل يناسب بشرة الرجال والنساء؟", "نعم، مناسب لبشرة الرجال والنساء."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يعالج حب الشباب في الظهر والكتفين؟", "نعم، يمكن استخدامه لبثور الظهر والكتفين أيضاً."),
        ("هل يساعد في تقليل احمرار البثور؟", "نعم، يهدئ التهيج واحمرار البثور بفاعلية."),
        ("هل يصلح تحت المكياج؟", "يُفضل وضعه على بشرة نظيفة مخصصة للعلاج."),
        ("هل هو خالي من الزيوت الثقيلة؟", "نعم، تركيبة علاجية خالية من الزيوت الثقيلة.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Penn Anti-Acne Cream 40g</strong> is a specialized effective medical treatment cream from Penn formulated to eliminate acne, dry active blemishes, and clarify facial skin. Powered by Salicylic Acid (BHA), purifying sulfur complex, and spot-soothing Tea Tree Oil.</p>
<p>Penn Anti-Acne Cream dries out active pimples and blemishes, unclogs blocked pores removing blackheads and whiteheads, and calms redness and inflammation, leaving your skin clear, acne-free, even-looking, and protected against recurring breakouts.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Active Acne & Blemish Treatment:</strong> Rapidly shrinks and dries out pimples and active breakouts.</li>
  <li><strong>Pore Unclogging & Blackhead Removal with Salicylic Acid:</strong> Deeply cleanses clogged pores.</li>
  <li><strong>Redness & Inflammation Reduction with Tea Tree Oil:</strong> Soothes acne-irritated skin.</li>
  <li><strong>Breakout Recurrence Prevention:</strong> Suppresses P. acnes bacteria proliferation.</li>
  <li><strong>Lightweight Fast-Drying Oil-Free Formula:</strong> Ideal for oily and combination acne-prone skin.</li>
  <li><strong>Compact 40g Tube:</strong> Excellent volume for targeted daily spot treatment.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Wash face with an acne cleanser and dry skin thoroughly.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a small amount of Penn cream directly onto pimples and acne spots only.</li>
  <li><strong>Step 3 (Absorb):</strong> Massage gently and allow to dry naturally (use 1-2 times daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Salicylic Acid & Purifying Sulfur:</strong> Dissolve dead sebum and comedones while drying active pimples.</li>
  <li><strong>Tea Tree Oil & Soothing Agents:</strong> Combat P. acnes bacteria and calm inflammation.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical acne spot application only.</li>
  <li>Avoid contact with eyes and lips.</li>
  <li>If severe dryness occurs, reduce application to once daily or every other day.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from acne and blemishes seeking Penn 40g Anti-Acne Cream for clear skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Penn</td></tr>
  <tr><th>Category</th><td>Skincare / Penn Medical Anti-Acne & Blemish Treatment Creams 40g</td></tr>
  <tr><th>Product Type</th><td>Salicylic Acid & Tea Tree Oil Spot Treatment Anti-Acne Cream (40g)</td></tr>
  <tr><th>Volume/Weight</th><td>40 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Oily & Combination Acne-Prone Skin</td></tr>
  <tr><th>Finish</th><td>Clear, acne-free, spot-free & soothed facial skin</td></tr>
  <tr><th>Texture</th><td>Lightweight fast-drying spot cream without stickiness</td></tr>
  <tr><th>Fragrance</th><td>Gentle medical Tea Tree scent</td></tr>
  <tr><th>Active Ingredients</th><td>Salicylic Acid, Purifying Sulfur, Tea Tree Oil</td></tr>
  <tr><th>Country of Origin</th><td>Taiwan / Asia</td></tr>
  <tr><th>Manufacturer</th><td>Penn Laboratories</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Lipophilic Salicylic Acid Sebum Penetration & Tea Tree Antibacterial Action</h2>

<h3>What problem does this solve?</h3>
<p>Penn Anti-Acne Cream resolves inflamed acne blemishes, blackheads, whiteheads, and excess breakout-causing sebum.</p>

<h3>Why choose Penn Anti-Acne Cream?</h3>
<p>Lipophilic Salicylic Acid (BHA) penetrates inside sebaceous glands dissolving clogged comedones while Tea Tree Oil neutralizes Propionibacterium acnes bacteria.</p>"""

    en_faqs = [
        ("What is Penn Anti-Acne Cream 40g?", "It is a medical spot treatment cream from Penn with Salicylic Acid and Tea Tree Oil for drying active acne and clarifying skin (40g)."),
        ("What are the benefits of Salicylic Acid and Tea Tree Oil?", "Salicylic Acid cleanses pores and dissolves sebum, while Tea Tree Oil dries pimples and calms redness."),
        ("Does it effectively dry active pimples and acne?", "Yes, clinically proven to shrink and dry out active acne blemishes quickly."),
        ("What weight is contained in this tube?", "40g."),
        ("How do I use it correctly?", "Wash face, apply small amount onto acne spot areas only, allow to dry 1-2 times daily."),
        ("Is it suitable for oily and combination skin?", "Yes, specifically formulated for oily and combination acne-prone skin."),
        ("Where is Penn Anti-Acne Cream manufactured?", "By Penn Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original."),
        ("What scent does Penn Anti-Acne Cream have?", "Gentle medical Tea Tree scent."),
        ("Does it treat blackheads and whiteheads?", "Yes, dissolves comedones and sebum causing blackheads and whiteheads."),
        ("Does 40g last long?", "Yes, lasts weeks because application is targeted on acne spots."),
        ("How should I store it?", "In a cool, dry place."),
        ("What if skin dryness occurs?", "Reduce usage to once daily or every other day and follow with an oil-free moisturizer."),
        ("How many times daily?", "1-2 times daily topically on acne spots."),
        ("Is it suitable for teens and adults?", "Yes, ages 12+."),
        ("Does it prevent breakout recurrence?", "Yes, suppresses bacteria preventing new clogged pores."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it dry quickly without stickiness?", "Yes, dries quickly without greasy residue."),
        ("Can it be used overnight?", "Yes, excellent for overnight spot application before bed."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it work on back and shoulder acne?", "Yes, can be applied to back and shoulder pimples too."),
        ("Does it help reduce pimple redness?", "Yes, effectively calms irritation and pimple redness."),
        ("Can it be used under makeup?", "Best applied directly onto clean skin for targeted treatment."),
        ("Is it heavy oil-free?", "Yes, heavy-oil-free medical formula.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1957",
        "sku": "EK-1957",
        "gtin": "4718460001111",
        "brand": "Penn",
        "ar": {
            "title": "كريم بن  مضاد لحب الشباب  40 جم",
            "meta_title": "كريم بن مضاد لحب الشباب 40جم | إكليل أبها",
            "meta_description": "اشتري كريم بن مضاد لحب الشباب (40 جم). كريم طبي بالساليسيليك وشجرة الشاي لعلاج وجفاف البثور وحب الشباب. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["بن", "كريم_بن", "مضاد_لحب_الشباب", "علاج_البثور", "إكليل_أبها"]
        },
        "en": {
            "title": "Penn Anti-Acne Cream 40g",
            "meta_title": "Penn Anti-Acne Cream 40g | Ekleel Abha",
            "meta_description": "Buy original Penn Anti-Acne Cream (40g). Medical Salicylic Acid & Tea Tree Oil spot treatment cream for acne. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["penn", "penn_anti_acne", "acne_cream", "spot_treatment", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 48 builders complete")
