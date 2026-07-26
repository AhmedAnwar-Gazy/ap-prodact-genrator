import json, os

def _make_soap_b61(pid, gtin, ar_name, en_name, brand_ar, brand_en, weight_g, key_ing_ar, key_ing_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> صابون التنظيف والعناية بالجمال الفاخر الأصيل من {brand_ar} المصمم خصيصاً لتنظيف، تصفية، وترطيب بشرة الوجه والجسم والتخلص من الزيوت والشوائب والبقع. يرتكز هذا الصابون الأصيل ({en_name}) على خلاصات {key_ing_ar}، المكونات المنظفة النباتية اللطيفة، والمركبات المغذية للبشرة.</p>
<p>يعمل صابون {brand_ar} على تنظيف مسام الوجه والجسم عمقاً، تقليل الشوائب والبقع، وتغذية الجلد وحفظ رطوبته الطبيعية، ليترك بشرتك ناعمة كالحرير، ناصعة النظافة، موحدة اللون، ومفعمة بالنضارة من الاستخدامات الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف وتصفية فائقة للبشرة:</strong> ينظف المسام من الدهون الميتة والشوائب دون جفاف.</li>
  <li><strong>تغذية وتلطيف البشرة بـ {key_ing_ar}:</strong> يحفظ نضارة الجلد وملمسه الناعم.</li>
  <li><strong>تحسين مرونة ونعومة الوجه والجسم:</strong> يمنح الجلد ملمساً حريرياً رائعاً.</li>
  <li><strong>حماية البشرة من الخشونة والتهيجات:</strong> تركيبة غنية بالمكونات الطبيعية المهدئة.</li>
  <li><strong>مناسب للاستخدام اليومي للوجه والجسم:</strong> رغوة غنية تنشطف بالماء بسهولة.</li>
  <li><strong>قطعة مدمجة سعة {weight_g} جم:</strong> حجم ممتاز للاستخدام العائلي اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي صابونة {brand_ar} بالماء الدافئ وكوّني رغوة غنية بين الكفين.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي الرغوة على بشرة الوجه والجسم ودلكي برفق بحركات دائرية لمدة دقيقة.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء الدافئ وجففي البشرة (يُستعمل مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصات {key_ing_ar} والمكونات المنقية:</strong> تمنح البشرة نضارة وتصفي الشوائب.</li>
  <li><strong>الزيوت النباتية والجليسرين المرطب:</strong> يحفظان التوازن المائي للبشرة لمنع الجفاف.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والجسم فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف فوق صحن صابون مصفى.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لتنظيف وتصفية وتفتيح بشرة الوجه والجسم.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>{brand_ar} ({brand_en})</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / صابون تنظيف وتغذية الوجه والجسم {weight_g}g</td></tr>
  <tr><th>نوع المنتج</th><td>صابون طبي لتنظيف وتصفية الوجه والجسم بـ {key_ing_ar} ({weight_g}g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>{weight_g} جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (العادية، الجافة والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناصعة النظافة، موحدة اللون، ناعمة كالحرير وخالية من الزيوت</td></tr>
  <tr><th>الملمس</th><td>رغوة غنية ناعمة كريمية</td></tr>
  <tr><th>العطر</th><td>عطر لطيف ناعم منعش</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصات {key_ing_ar}، جليسرين مرطب، منظفات لطيفة</td></tr>
  <tr><th>بلد المنشأ</th><td>المغرب / السعودية</td></tr>
  <tr><th>الشركة المصنعة</th><td>{brand_en} Personal Care</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد خلاصات {key_ing_ar} في صابون {brand_ar}</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج صابون {brand_ar} مشكلة تراكم الدهون، انسداد المسام، والخشونة الناتجة عن الصابون القاسي.</p>

<h3>لماذا تنجح تركيبة {key_ing_ar}؟</h3>
<p>لأن المواد اللطيفة تذيب الدهون والشوائب دون هدم حاجز البشرة الهيدروليبيدي.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام مرتين يومياً بالماء الدافئ:</strong> ينظف المسام بانتظام.<br>
2. <strong>الترطيب بمرطب خفيف بعد الغسل:</strong> يدعم مرونة ونعومة البشرة.<br>
3. <strong>حفظ الصابونة جافة:</strong> يمنع ذوبانها ويطيل عمر استخدامها.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الصابون الطبيعي يسبب جفاف شديد للبشرة."<br>
<strong>الحقيقة:</strong> صابون {brand_ar} مدعم بمركبات مرطبة تحفظ الرطوبة والنعومة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخفض المكونات التوتر السطحي للماء مشكلة ميكروسفيرات تنظف الدهون الزائدة وتترك جزيئات الجليسرين مرتبطة بالكيراتين.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو صابون جمال وتنظيف للوجه والجسم من {brand_ar} بخلاصات {key_ing_ar} بحجم {weight_g} جم."),
        (f"ما هي فوائد صابون {brand_ar} بـ {key_ing_ar}؟", f"ينظف المسام بعمق، يزيل الزيوت، ويوحد لون الوجه والجسم."),
        ("هل ينظف المسام ويصفي البشرة بفاعلية؟", "نعم، مثبت سريرياً في تنظيف المسام وتصفية البشرة بفاعلية."),
        (f"ما وزن القطعة؟", f"{weight_g} جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "كوّني رغوة، وزعيها على الوجه والجسم، دلكي برفق واشطفي بالماء مرتين يومياً."),
        ("هل هو آمن للبشرة الحساسة؟", "نعم، آمن ومناسب لجميع أنواع البشرة."),
        (f"أين صُنع صابون {brand_ar}؟", "صُنع بأعلى معايير جودة العناية بالبشرة العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة صابون {brand_ar}؟", "عطر لطيف ناعم منعش."),
        ("هل يمنح رغوة غنية ولطيفة؟", "نعم، ينتج رغوة ناعمة تنظف بفاعلية ولطف."),
        (f"هل العبوة {weight_g} جم تكفي لفترة جيدة؟", "نعم، تكفي لعدة أسابيع من الاستخدام اليومي المنتظم."),
        ("كيف أحتفظ بالصابونة؟", "في مكان بارد وجاف فوق صحن صابون مصفى لمنع الذوبان."),
        ("هل يناسب الوجه والجسم معاً؟", "نعم، صابون شامل ممتاز للوجه والجسم."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        (f"هل {brand_ar} علامة شهيرة وموثوقة؟", f"نعم، {brand_en} علامة موثوقة ومشهورة جداً في العناية بالبشرة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يزيل الخلايا الميتة والزيوت الزائدة؟", "نعم، ينظف الدهون الميتة والشوائب من المسام."),
        ("هل يترك البشرة ناعمة كالحرير؟", "نعم، يترك البشرة مفعمة بالنعومة والإشراق."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب للرجال والنساء."),
        ("هل يفضل استخدام مرطب بعده؟", "نعم، يُفضل استخدام مرطب خفيف بعد غسل الوجه للحفاظ على الترطيب."),
        ("هل يناسب الاستخدام في الصيف والشتاء؟", "نعم، ممتاز لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة؟", "نعم، منتج عناية مفيد وأنيق."),
        ("هل يقلل لمعان البشرة الدهنية؟", "نعم، يسيطر على الإفرازات الدهنية الزائدة ويترك الوجه منتعشاً غير لامع."),
        ("هل يعيد التوهج الطبيعي للبشرة؟", "نعم، يمنح البشرة توهجاً وإشراقة ناصعة.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic luxury skin cleansing, clarifying, and hydrating soap from {brand_en} designed to cleanse, clarify, and smooth facial and body skin while removing excess oil and impurities. Built upon {key_ing_en} extracts, mild plant cleansers, and skin-nourishing compounds.</p>
<p>{brand_en} Soap deeply cleanses face and body pores, reduces impurities and dark spots, and nourishes skin while preserving its natural hydration, leaving your skin touchably silky soft, spotlessly clean, even-toned, and radiant from initial uses.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Superior Skin Cleansing & Clarifying:</strong> Cleanses pores of dead sebum and impurities without dryness.</li>
  <li><strong>Skin Nourishment & Soothing with {key_ing_en}:</strong> Preserves skin vitality and soft touch.</li>
  <li><strong>Skin Smoothness & Elasticity Enhancement:</strong> Imparts a touchably silky smooth feel to face and body.</li>
  <li><strong>Skin Protection Against Roughness:</strong> Rich formula with natural soothing ingredients.</li>
  <li><strong>Mild Daily Formula for Face & Body:</strong> Rich lather that rinses off smoothly with water.</li>
  <li><strong>Compact {weight_g}g Bar:</strong> Excellent volume for continuous family daily care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet {brand_en} soap bar with warm water and work into a rich lather between hands.</li>
  <li><strong>Step 2:</strong> Spread lather over damp face and body skin, massaging gently in circular motions for one minute.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and pat dry (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>{key_ing_en} Extracts & Purifying Agents:</strong> Impart radiant clarity while removing impurities and spots.</li>
  <li><strong>Plant Oils & Hydrating Glycerin:</strong> Preserve skin moisture balance guarding against dryness and roughness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical face and body skin application only.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place on a draining soap dish.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for facial and body cleansing, skin clarifying, and tone evening.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>{brand_en}</td></tr>
  <tr><th>Category</th><td>Skincare / {brand_en} Face & Body Cleansing Soaps {weight_g}g</td></tr>
  <tr><th>Product Type</th><td>Skin Purifying & Cleansing Soap with {key_ing_en} ({weight_g}g)</td></tr>
  <tr><th>Volume/Weight</th><td>{weight_g} g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Normal, Dry & Oily Skin)</td></tr>
  <tr><th>Finish</th><td>Spotlessly clean, even-toned, silky soft & oil-free radiant skin</td></tr>
  <tr><th>Texture</th><td>Rich smooth foaming lather</td></tr>
  <tr><th>Fragrance</th><td>Gentle pleasant soft scent</td></tr>
  <tr><th>Active Ingredients</th><td>{key_ing_en} Extracts, Hydrating Glycerin, Mild Cleansers</td></tr>
  <tr><th>Country of Origin</th><td>Morocco / KSA</td></tr>
  <tr><th>Manufacturer</th><td>{brand_en} Personal Care</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of {key_ing_en} Epidermal Sebum Solubilization & Hydrolipid Protection</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves excess sebum accumulation, clogged pores, dark spots, and soap-induced dryness.</p>

<h3>Why choose {brand_en} Soap?</h3>
<p>Mild surfactants combined with active {key_ing_en} solubilize trapped sebum without disrupting intercellular stratum corneum lipid bilayers.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a skin purifying face and body soap from {brand_en} with {key_ing_en} extracts ({weight_g}g)."),
        (f"What are the benefits of {brand_en} Soap with {key_ing_en}?", f"Deeply cleanses pores, removes oil, and unifies face and body skin tone."),
        ("Does it clean pores and clarify skin effectively?", "Yes, clinically proven to cleanse pores and clarify skin effectively."),
        (f"What weight is contained in this bar?", f"{weight_g}g bar."),
        ("How do I use it correctly?", "Work into a lather, apply to face and body, massage gently and rinse twice daily."),
        ("Is it safe for sensitive skin?", "Yes, safe and suitable for all skin types."),
        (f"Where is {brand_en} Soap manufactured?", "Manufactured to international skincare quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original."),
        (f"What scent does {brand_en} Soap have?", "Gentle pleasant soft refreshing scent."),
        ("Does it yield a rich gentle lather?", "Yes, produces a smooth lather that cleanses gently and effectively."),
        (f"Does the {weight_g}g bar last long?", "Yes, lasts weeks of regular daily use."),
        ("How should I store the soap bar?", "In a cool, dry place on a draining soap dish to prevent melting."),
        ("Is it suitable for both face and body?", "Yes, versatile soap excellent for face and body."),
        ("How many times daily?", "Twice daily (morning and evening)."),
        (f"Is {brand_en} a trusted famous brand?", f"Yes, {brand_en} is a trusted famous brand in skincare."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it remove dead skin cells and excess oil?", "Yes, cleanses dead sebum and impurities from pores."),
        ("Does it leave skin silky soft?", "Yes, leaves skin touchably soft and radiant."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it recommended to follow with a moisturizer?", "Yes, follow with a lightweight moisturizer to lock in hydration."),
        ("Is it suitable for all seasons?", "Yes, excellent for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, practical and thoughtful skincare gift."),
        ("Does it reduce oily shine?", "Yes, controls excess sebum shine leaving face fresh and matte."),
        ("Does it restore natural radiant glow?", "Yes, imparts a bright radiant glow to skin.")
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
            "meta_description": f"اشتري {ar_name}. صابون تنظيف وتصفية الوجه والجسم بـ {key_ing_ar}. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. {brand_en} face & body cleansing and purifying soap with {key_ing_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2018():
    return _make_soap_b61(
        pid=2018, gtin="6111024000922",
        ar_name="صابون الطاووس الاصلي 125 جم",
        en_name="Original Peacock Soap 125g",
        brand_ar="الطاووس", brand_en="Peacock Soap", weight_g=125,
        key_ing_ar="زيت الزيتون الطبيعي وخلاصة الخزامى المغربي الأصيل", key_ing_en="Natural Olive Oil & Moroccan Lavender Extract",
        feature_ar="تنظيف ونظافة أصلية وتنعيم لبشرة الوجه والجسم بالطاووس المغربي 125 جم", feature_en="original Moroccan olive oil and lavender purifying soap 125g",
        tags_ar=["الطاووس", "صابون_الطاووس_الاصلي", "صابون_مغربي", "تنظيف_البشرة", "إكليل_أبها"],
        tags_en=["peacock_soap", "original_peacock_soap", "moroccan_soap", "natural_soap", "ekleel_abha"]
    )


def create_product_2019():
    return _make_soap_b61(
        pid=2019, gtin="6287035850198",
        ar_name="صابون مستكة كيوت 100جم",
        en_name="Cute Mastic Soap 100g",
        brand_ar="كيوت", brand_en="Cute", weight_g=100,
        key_ing_ar="صمغ المستكة الطبيعية العطرية المطهرة", key_ing_en="Natural Mastic Gum Extract",
        feature_ar="تطهير وتنقية المسام وإعادة المرونة لبشرة الوجه بالمستكة 100 جم", feature_en="purifies pores and restores skin elasticity with natural mastic 100g",
        tags_ar=["كيوت", "صابون_المستكة", "مستكة_طبيعية", "تصفية_الوجه", "إكليل_أبها"],
        tags_en=["cute", "mastic_soap", "mastic_gum", "purifying_soap", "ekleel_abha"]
    )


def create_product_2020():
    return _make_soap_b61(
        pid=2020, gtin="6287035850150",
        ar_name="صابون الصبار كيوت 100جم",
        en_name="Cute Aloe Vera Soap 100g",
        brand_ar="كيوت", brand_en="Cute", weight_g=100,
        key_ing_ar="جل الصبار الطبيعي (Aloe Vera Gel)", key_ing_en="Natural Aloe Vera Gel",
        feature_ar="تهدئة وترطيب وتغذية البشرة الحساسة والمجهدة بالصبار 100 جم", feature_en="soothes, hydrates, and nourishes sensitive skin with Aloe Vera 100g",
        tags_ar=["كيوت", "صابون_الصبار", "جل_الصبار", "ترطيب_البشرة", "إكليل_أبها"],
        tags_en=["cute", "aloe_vera_soap", "aloe_soap", "soothing_soap", "ekleel_abha"]
    )


def create_product_2021():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول جسم عطري رومانسية الكركديه من لوكس 700مل (Lux Hibiscus Romance Perfumed Body Wash 700ml)</strong> سائل الاستحمام العطري الفاخر الأيقوني من لوكس المصمم لمنح جسمك نظافة عميقة ورغوة مخملية غنية وعطراً فواحاً يدوم لـ 24 ساعة. يرتكز هذا الغسول الأصيل (Lux Hibiscus Romance 700ml) على زيت الزهور المسكوبة نادرة الوجود (Everscent Essential Oil)، خلاصة زهور الكركديه الرومانسية، والمركبات المرطبة لبشرة الجسم.</p>
<p>يعمل غسول لوكس برومانسية الكركديه على تنظيف مسام الجسم وإزالة الدهون والأوساخ، حماية الجلد من الجفاف وحفظ طراوته، وتغليف جسمك بنفحات الزهور الفواحة الساحرة، ليترك بشرتك ناعمة كالحرير، مرطبة، ومعطرة بالنظافة والأناقة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عطر فواح يدوم لـ 24 ساعة بزيت الزهور المسكوبة:</strong> يمنح الجسد عبقاً رومانسياً فواحاً طول اليوم.</li>
  <li><strong>تنظيف عميق ورغوة كريمية غنية:</strong> ينظف الجسم بلطف دون انتزاع الزيوت الطبيعية.</li>
  <li><strong>ترطيب وتنعيم لبشرة الجسم:</strong> يحفظ حاجز الترطيب الطبيعي للجلد.</li>
  <li><strong>تركيبة خفيفة متوازنة الحموضة (pH Balanced):</strong> مناسبة للاستخدام اليومي لجميع أنواع البشرة.</li>
  <li><strong>جودة لوكس (Lux) العالمية الشهيرة:</strong> العلامة الأولى في عطور وجمال الاستحمام.</li>
  <li><strong>عبوة اقتصادية ضخمة سعة 700 مل مزودة بضاغط:</strong> حجم ممتازة يكفي لاستخدام عائلي يومي مستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الجسم بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> اضغطي كمية مناسبة من سائل لوكس على ليفة الاستحمام أو الكفين وكوّني رغوة غنية.</li>
  <li><strong>الخطوة الثالثة:</strong> دلكي الجسم برفق بحركات دائرية ثم اشطفي جيداً بالماء (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الزهور الأساسية وخلاصة الكركديه:</strong> تثبت العطر الفواح على ألياف البشرة وتمنح انطباعاً عاطراً.</li>
  <li><strong>المنظفات اللطيفة والمركبات المرطبة:</strong> تنظف الجسم وتحفظ نعومته الحريرية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن غسول لوكس برومانسية الكركديه 700 مل للانتعاش العطري والنظافة الحريرية.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لوكس (Lux)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / غسولات ومجموعات الاستحمام المعطرة من لوكس 700ml</td></tr>
  <tr><th>نوع المنتج</th><td>غسول جسم عطري مرطب بنفحات زهور الكركديه وزيت Everscent (700ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>700 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (العادية، الجافة والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، مرطب، ناصع النظافة ومفعم بعطر الكركديه لـ 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>سائل جل عطري رغوي غني</td></tr>
  <tr><th>العطر</th><td>عطر رومانسية زهور الكركديه الفواح لـ 24 ساعة</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت Everscent Essential Oil، خلاصة الكركديه، منظفات لطيفة</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الإمارات</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever Group</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت Everscent وخلاصة الكركديه في غسول لوكس (Lux Hibiscus Romance)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول لوكس مشكلة جفاف البشرة بعد الاستحمام بالصابون القاسي، تراكم الدهون، وتلاشي عطر النظافة سريعاً.</p>

<h3>لماذا تنجح تركيبة Lux Hibiscus Romance؟</h3>
<p>لأن تقنية زيوت Everscent العطرية تفرز جزيئات عطرية ترتبط بروابط البروتين الجلدية لتمنح ثباتاً عاطراً لـ 24 ساعة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام اليومي بالماء الدافئ:</strong> ينظف المسام وينشط الدورة الدموية.<br>
2. <strong>استخدام ليفة ناعمة:</strong> يزيد تكوين الرغوة الغنية ويزيل التراكمات السطحية.<br>
3. <strong>الشطف الجيد بالماء:</strong> يضمن عدم بقاء أي ترسبات صابونية على الجلد.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "غسولات الجسم المعطرة تجفف البشرة."<br>
<strong>الحقيقة:</strong> غسول لوكس مدعم بمركبات مرطبة تحفظ التوازن المائي للجلد أثناء التنظيف.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخفض السورفاكتانتات اللطيفة التوتر السطحي للماء وتأطر الجزيئات الزيتية والأوساخ داخل ميكروسفيرات ينشطف بها الماء بسلاسة.</p>"""

    faqs = [
        ("ما هو غسول جسم عطري رومانسية الكركديه من لوكس 700مل؟", "هو سائل استحمام عطري فاخر من لوكس بنفحات زهور الكركديه وزيت Everscent لثبات العطر 24 ساعة (700 مل)."),
        ("ما هي فوائد خلاصة الكركديه وزيت Everscent؟", "تنظف المنظفات اللطيفة البشرة دون جفاف، بينما يثبت زيت Everscent عطر الكركديه لـ 24 ساعة."),
        ("هل يمنح رغوة غنية وعطراً يدوم لـ 24 ساعة؟", "نعم، مثبت سريرياً في توفير رغوة غنية وثبات عطري يدوم 24 ساعة."),
        ("ما حجم العبوة؟", "تأتي بعبوة ضخمة مزودة بضاغط بسعة 700 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الجسم، اضغطي كمية على الليفة وكوّني رغوة، دلكي برفق واشطفي بالماء يومياً."),
        ("هل هو آمن لجميع أنواع البشرة؟", "نعم، تركيبة متوازنة الحموضة آمنة لجميع أنواع بشرة الجسم."),
        ("أين صُنع غسول لوكس؟", "صُنع بواسطة مجموعة Unilever العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لوكس لدى إكليل أبها أصلية 100%."),
        ("ما رائحة غسول لوكس الكركديه؟", "عطر زهور الكركديه الفواح الرومانسي الأنيق."),
        ("هل يترك البشرة ناعمة ومرطبة؟", "نعم، يحافظ على رطوبة الجلد ونعومته الحريرية."),
        ("هل 700 مل تكفي للاستخدام العائلي؟", "نعم، عبوة ضخمة بضاغط تكفي لعدة أشهر من الاستخدام العائلي اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع أفراد الأسرة وخاصة محبي العطور الزهرية الفاخرة."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً أثناء الاستحمام."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، ينشطف بالماء الدافئ بسهولة دون ترك أثر لزج."),
        ("هل لوكس علامة عالمية شهيرة؟", "نعم، Lux علامة رائدة ومشهورة جداً عالمياً لمنتجات الاستحمام العطرية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في إزالة رائحة العرق؟", "نعم، ينظف بفاعلية ويعطر الجسم بنفحات عاطرة."),
        ("هل يناسب الاستخدام بعد الرياضة؟", "نعم، ممتاز للانتعاش والنظافة بعد التمارين والرياضة."),
        ("هل يترك أثراً دهنياً؟", "لا، ينظف وينشطف بالكامل دون دهنية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل العبوة مزودة بضاغط مريح؟", "نعم، ضاغط مريح جداً يسهل استخدام الجل أثناء الاستحمام."),
        ("هل يناسب الشتاء والصيف؟", "نعم، ممتاز لجميع فصول السنة."),
        ("هل يصلح هدية ضمن مجموعة الاستحمام؟", "نعم، خيار ممتاز جداً في مجموعات العناية الشخصية."),
        ("هل يغني عن استخدام الصابون القاسي؟", "نعم، بديل مرطب وألطف بكثير من الصابون القاسي.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Lux Hibiscus Romance Perfumed Body Wash 700ml</strong> is an iconic luxury fragranced body wash from Lux designed to deliver deep cleansing, a rich velvety lather, and a 24-hour long-lasting floral fragrance. Built upon Everscent Essential Oil technology, romantic Hibiscus flower extract, and body-moisturizing compounds.</p>
<p>Lux Hibiscus Romance Body Wash cleanses body pores of dirt and excess sebum, guards skin against dryness, and wraps your body in enchanting floral notes, leaving your skin touchably silky soft, hydrated, and fragranced with elegance all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>24-Hour Long-Lasting Fragrance with Everscent Oil:</strong> Coats body in a romantic floral scent all day.</li>
  <li><strong>Deep Cleansing & Rich Creamy Lather:</strong> Cleanses body gently without stripping natural skin oils.</li>
  <li><strong>Body Skin Softening & Hydration:</strong> Preserves the skin's natural moisture barrier.</li>
  <li><strong>pH-Balanced Mild Formula:</strong> Suitable for daily use on all skin types.</li>
  <li><strong>Famous Quality of Lux Global:</strong> #1 recognized brand in perfumed bath and beauty care.</li>
  <li><strong>Generous 700ml Jumbo Pump Bottle:</strong> Excellent value lasting months of continuous daily family use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet body skin with warm water during shower.</li>
  <li><strong>Step 2:</strong> Pump a suitable amount of Lux gel onto a shower loofah or hands and work into a rich lather.</li>
  <li><strong>Step 3:</strong> Massage body gently in circular motions, then rinse thoroughly with water (use daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Everscent Essential Oil & Hibiscus Extract:</strong> Bind fragrance molecules to skin layers delivering 24-hour freshness.</li>
  <li><strong>Gentle Cleansers & Hydrating Agents:</strong> Cleanse body while maintaining touchable silky softness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application only.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every woman seeking Lux Hibiscus Romance 700ml Body Wash for 24-hour fragrance and silky clean skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lux</td></tr>
  <tr><th>Category</th><td>Body Care / Lux Perfumed Hydrating Body Washes 700ml</td></tr>
  <tr><th>Product Type</th><td>24H Perfumed Hibiscus & Everscent Essential Oil Body Wash (700ml)</td></tr>
  <tr><th>Volume/Weight</th><td>700 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Normal, Dry & Oily Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, hydrated, spotlessly clean body skin fragranced with Hibiscus for 24H</td></tr>
  <tr><th>Texture</th><td>Rich foaming fragranced clear gel fluid</td></tr>
  <tr><th>Fragrance</th><td>Romantic long-lasting Hibiscus floral scent for 24 hours</td></tr>
  <tr><th>Active Ingredients</th><td>Everscent Essential Oil, Hibiscus Extract, Gentle Cleansers</td></tr>
  <tr><th>Country of Origin</th><td>KSA / UAE</td></tr>
  <tr><th>Manufacturer</th><td>Unilever Group</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Everscent Essential Oil Binding & 24-Hour Floral Fragrance Retention</h2>

<h3>What problem does this solve?</h3>
<p>Lux Hibiscus Romance Body Wash resolves skin dryness caused by harsh soaps, daily sweat accumulation, and fading body fragrance.</p>

<h3>Why choose Lux Body Wash?</h3>
<p>Everscent Essential Oil technology binds perfume micro-droplets to skin keratin providing sustained 24-hour fragrance release.</p>"""

    en_faqs = [
        ("What is Lux Hibiscus Romance Perfumed Body Wash 700ml?", "It is a luxury perfumed body wash from Lux with Hibiscus flowers and Everscent Oil for 24-hour fragrance (700ml)."),
        ("What are the benefits of Hibiscus extract and Everscent Oil?", "Gentle cleansers cleanse skin without dryness, while Everscent Oil binds Hibiscus fragrance for 24 hours."),
        ("Does it yield a rich lather and 24-hour fragrance?", "Yes, clinically proven to produce a rich lather and deliver 24-hour fragrance retention."),
        ("What volume is contained in this bottle?", "700ml jumbo pump bottle."),
        ("How do I use it correctly?", "Wet body, pump gel onto loofah, lather, massage gently and rinse with water daily."),
        ("Is it safe for all skin types?", "Yes, pH-balanced formula safe for all body skin types."),
        ("Where is Lux Body Wash manufactured?", "By Unilever Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All Lux products at Ekleel Abha are 100% original."),
        ("What scent does Lux Hibiscus Romance have?", "Romantic elegant Hibiscus floral fragrance."),
        ("Does it leave skin soft and hydrated?", "Yes, preserves skin moisture and silky softness."),
        ("Does 700ml last long for family use?", "Yes, jumbo pump bottle lasts months of regular family use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for men and women?", "Yes, suitable for the entire family."),
        ("How many times daily?", "Once or twice daily during showers."),
        ("Does it rinse off easily?", "Yes, rinses off smoothly with warm water without sticky residue."),
        ("Is Lux a world-famous brand?", "Yes, Lux is a globally leading brand in perfumed bath care."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help remove sweat odor?", "Yes, effectively cleanses and perfumes body skin."),
        ("Is it good post-workout?", "Yes, excellent for post-workout refreshing shower routines."),
        ("Does it leave a greasy film?", "No, cleanses completely clean without greasiness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is the pump bottle convenient?", "Yes, convenient pump dispenser for easy showering."),
        ("Is it good for summer and winter?", "Yes, excellent for all seasons."),
        ("Is it a nice shower gift?", "Yes, excellent addition to personal care gift sets."),
        ("Does it replace harsh soaps?", "Yes, a much gentler hydrating alternative to harsh bar soaps.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2021",
        "sku": "EK-2021",
        "gtin": "6281006569836",
        "brand": "Lux",
        "ar": {
            "title": "غسول جسم عطري رومانسية الكركديه من لوكس 700مل",
            "meta_title": "غسول جسم لوكس الكركديه 700مل | إكليل أبها",
            "meta_description": "اشتري غسول جسم عطري رومانسية الكركديه من لوكس (700 مل). سائل استحمام بعطر الكركديه الفواح لـ 24 ساعة وترطيب البشرة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["لوكس", "غسول_جسم_لوكس", "رومانسية_الكركديه", "سائل_استحمام_معطر", "إكليل_أبها"]
        },
        "en": {
            "title": "Lux Hibiscus Romance Perfumed Body Wash 700ml",
            "meta_title": "Lux Hibiscus Romance Body Wash 700ml | Ekleel Abha",
            "meta_description": "Buy original Lux Hibiscus Romance Perfumed Body Wash (700ml). 24H perfumed Hibiscus floral body wash. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["lux", "lux_body_wash", "hibiscus_romance", "perfumed_body_wash", "ekleel_abha"]
        }
    }


def create_product_2022():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>واقي شمس سائل للبشرة الحساسة انثيليوس من لاروش بوزي 50 مل (La Roche-Posay Anthelios Sunscreen 50 ml)</strong> واقي الشمس الطبي الفاخر الأكثر توصية عالمياً من لاروش بوزي الفرنسية المصمم لمنح البشرة الحساسة أعلى حماية فائقة بـ SPF 50+ ضد أشعة الشمس الضارة (UVA/UVB/Long-UVA). يرتكز هذا الفلويد الأسطوري (La Roche-Posay Anthelios UVMune 400 Fluid 50ml) على مرشح الشمس الثوري المبتكر (Mexoryl 400 Filter)، مياه لاروش بوزي الحرارية المهدئة، ومركب Netlock لثبات مائي غير مرئي.</p>
<p>يعمل واقي شمس لاروش انثيليوس على حماية الوجه والعينين من حروق الشمس، التصبغات الشمسيّة، والتجاعيد والشيخوخة الضوئية المبكرة دون ترك أي أثر أبيض أو لزوجة، ليترك بشرتك ناعمة، محمية تماماً، غير لامعة بالدهون، وآمنة حتى على منطقة محيط العينين الحساسة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>أعلى حماية فائقة SPF 50+ بمرشح Mexoryl 400 الثوري:</strong> يحمي من أطول أشعة UVA المسببة لشيخوخة الجلد وتصبغاته.</li>
  <li><strong>ملمس سائل فلويد غير مرئي (Invisible Fluid):</strong> امتصاص فوري دون ترك أي أثر أبيض أو طبقة دهنية.</li>
  <li><strong>مقاومة فائقة للماء، العرق، والرمال:</strong> ثبات ممتد أثناء السباحة والرياضة والأنشطة الخارجية.</li>
  <li><strong>آمن ومخصص للبشرة شديدة الحساسية ومحيط العينين:</strong> لا يسبب حرقان العينين (Anti-Eye Stinging).</li>
  <li><strong>مختبر درماتولوجياً وموصى به من 60,000 طبيب جلدية:</strong> الواقي الطبي رقم 1 عالمياً لحماية الوجه.</li>
  <li><strong>عبوة مدمجة سعة 50 مل:</strong> حجم ممتاز للاستخدام الصباحي والسفر والتنقل.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> رجّي العبوة جيداً قبل الاستخدام لتفعيل مركب Netlock.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية كافية من سائل لاروش انثيليوس على بشرة الوجه والرقبة ومحيط العينين قبل التعرض للشمس بـ 20 دقيقة.</li>
  <li><strong>الخطوة الثالثة:</strong> كرري التطبيق كل ساعتين أو بعد السباحة والتنشيف بالمنشفة (يُستعمل كل صباح).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مرشح Mexoryl 400 ومركبات الفلترة المتقدمة:</strong> تحمي من الأشعة فوق البنفسجية UVA العميقة والـ UVB.</li>
  <li><strong>مياه لاروش بوزي الحرارية المهدئة (Thermal Spring Water):</strong> تلطف البشرة وتحميها من الأكسدة والتهيج.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي الصباحي على بشرة الوجه والرقبة ومحيط العينين.</li>
  <li>تجنبي التعرض المباشر لظهر الظهيرة الحادة حتى مع استخدام واقي الشمس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يملك بشرة حساسة ويبحث عن واقي شمس لاروش انثيليوس فلويد 50 مل لأعلى حماية غير مرئية.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لاروش بوزي (La Roche-Posay)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / واقيات الشمس الطبية انثيليوس من لاروش بوزي 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>سائل واقي شمس فلويد بمرشح Mexoryl 400 و SPF 50+ للبشرة الحساسة (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (خصيصاً البشرة الحساسة والمفرطة التحسس ومحيط العينين)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه محمٍ تماماً، غير لامع، خالٍ من الأثر الأبيض ومنتعش</td></tr>
  <tr><th>الملمس</th><td>سائل فلويد غير مرئي مائي امتصاصه فوري دون دهنية</td></tr>
  <tr><th>العطر</th><td>خالٍ من العطور الصناعية (أو عطر ناعم طبي)</td></tr>
  <tr><th>المكونات النشطة</th><td>مرشح Mexoryl 400، مياه لاروش بوزي الحرارية، مركب Netlock</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>La Roche-Posay Laboratoire Dermatologique France</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد مرشح Mexoryl 400 ومياه لاروش الحرارية في Anthelios</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج واقي شمس انثيليوس حروق الشمس، الكلف والتصبغات الناتجة عن الأشعة البنفسجية العميقة، والشيخوخة الضوئية وتأثر محيط العينين.</p>

<h3>لماذا تنجح تقنية Mexoryl 400 و Netlock؟</h3>
<p>لأن مرشح Mexoryl 400 هو الوحيد الذي يغطي أطول أشعة بنفسجية (Ultra-Long UVA: 380-400nm) بينما يشكل Netlock شبكة حماية مائية غير مرئية تثبت على الجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق الصباحي وتكراره كل ساعتين:</strong> يضمن استمرار أعلى درجات الحماية.<br>
2. <strong>الرج الجيد قبل التطبيق:</strong> يضمن توزيع مرشحات الشمس بسلاسة.<br>
3. <strong>التطبيق على محيط العينين وآذان والرقبة:</strong> يحمي كامل المناطق المكشوفة للشمس.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "واقي الشمس يسبب حرقان العينين ولمعاناً دهنياً."<br>
<strong>الحقيقة:</strong> انثيليوس فلويد مصمم بتقنية Anti-Eye Stinging خالية من الزيوت تمتص فورياً دون أي حرقان أو لمعان.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تمتص مرشحات Mexoryl الطول الموجي 380-400nm وتحول الطاقة الضوئية الحرارية إلى طاقة غير ضارة مانعة تدمير حمض DNA الخلوي.</p>"""

    faqs = [
        ("ما هو واقي شمس سائل للبشرة الحساسة انثيليوس من لاروش بوزي 50 مل؟", "هو واقي شمس فلويد طبي ثوري من لاروش بوزي الفرنسية بمرشح Mexoryl 400 و SPF 50+ للبشرة الحساسة ومحيط العينين (50 مل)."),
        ("ما هي فوائد مرشح Mexoryl 400 والـ SPF 50+؟", "يحمي Mexoryl 400 من أطول أشعة UVA المسببة للتجاعيد والتصبغات، وتضمن SPF 50+ حماية كاملة من حروق الشمس."),
        ("هل يترك أثراً أبيض أو لمسة دهنية؟", "لا، ملمس فلويد سائل غير مرئي يمتص فورياً دون أي أثر أبيض أو دهني."),
        ("ما حجم العبوة؟", "تأتي بعبوة سائل مدمجة بسعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "رجّي العبوة، ضعي كمية على الوجه والرقبة ومحيط العينين قبل التعرض للشمس بـ 20 دقيقة وكرري كل ساعتين."),
        ("هل هو آمن على منطقة محيط العينين دون حرقان؟", "نعم، مختبر طبياً وآمن على منطقة محيط العينين دون حرقان (Anti-Eye Stinging)."),
        ("أين صُنع واقي شمس لاروش بوزي؟", "صُنع في فرنسا بواسطة La Roche-Posay Laboratoire Dermatologique."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لاروش بوزي لدى إكليل أبها أصلية 100%."),
        ("هل هو مقاوم للماء والعرق والرمال؟", "نعم، ثبات فائق مقاوم للماء والعرق والرمال أثناء الرياضة والسباحة."),
        ("هل يناسب جميع أنواع البشرة وخاصة الحساسة؟", "نعم، مصمم خصيصاً للبشرة الحساسة، المفرطة التحسس، والدهنية."),
        ("هل 50 مل مناسبة للحقيبة والسفر؟", "نعم، حجم أنيق مدمج مثالي لحقيبة اليد والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل هو الواقي رقم 1 الموصى به من أطباء الجلدية؟", "نعم، La Roche-Posay العلامة رقم 1 الموصى بها عالمياً من 60,000 طبيب جلدية."),
        ("كم مرة يومياً؟", "صباحاً وقبل التعرض للشمس، ويكرر كل ساعتين وعند الحاجة."),
        ("هل يقي من التصبغات والكلف والشيخوخة الضوئية؟", "نعم، يحمي بفاعلية من التصبغات والكلف والتجاعيد المبكرة الناتجة عن الشمس."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يصلح كقاعدة ممتازة تحت المكياج؟", "نعم، قاعدة ممتازة جداً للمكياج بفضل امطصاطه السريع وملمسه غير المرئي."),
        ("هل يجب رج العبوة قبل الاستخدام؟", "نعم، رج العبوة ضروري لتوزيع مرشح Mexoryl ومركب Netlock."),
        ("هل يسبب انسداد المسام أو حب الشباب؟", "لا، تركيبة خفيفة غير مسببة للانسداد (Non-Comedogenic)."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يحمي في الأيام الغائمة والمغلقة؟", "نعم، الأشعة البنفسجية تخترق السحب وتستلزم الوقاية اليومية."),
        ("هل يصلح هدية راقية مفيدة؟", "نعم، منتج طبي فاخر وأساسي لكل روتين عناية."),
        ("هل يجف في ثوانٍ معدودة؟", "نعم، يمتص ويجف في ثوانٍ معدودة دون أثر."),
        ("هل تتوفر إصدارات بخاخ وأويل من انثيليوس؟", "نعم، تتوفر عائلة Anthelios بخيارات متنوعة لدى لاروش بوزي.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>La Roche-Posay Anthelios Sunscreen 50 ml</strong> is the world's most dermatologist-recommended medical sunscreen fluid from La Roche-Posay France engineered to provide sensitive skin with ultimate SPF 50+ protection against harmful solar radiation (UVA/UVB/Long-UVA). Built upon the breakthrough Mexoryl 400 filter, soothing La Roche-Posay Thermal Spring Water, and Netlock technology for invisible water-resistant defense.</p>
<p>La Roche-Posay Anthelios Invisible Fluid shields face and eyes against sunburn, solar hyperpigmentation, wrinkles, and premature photo-aging without leaving white marks or a greasy film, leaving your skin touchably soft, fully protected, matte, and safe even on delicate eye contours.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Ultimate SPF 50+ Protection with Breakthrough Mexoryl 400 Filter:</strong> Shields against ultra-long UVA rays responsible for deep skin aging and spots.</li>
  <li><strong>Invisible Fluid Ultra-Lightweight Texture:</strong> Instant absorption leaving zero white marks or greasy shine.</li>
  <li><strong>High Resistance to Water, Sweat & Sand:</strong> Sustained protection during swimming, sports, and outdoor activities.</li>
  <li><strong>Ophthalmologically Tested Safe for Sensitive Eyes:</strong> Formulated to prevent eye stinging (Anti-Eye Stinging).</li>
  <li><strong>#1 Dermatologist Recommended Sunscreen Worldwide:</strong> Trusted by over 60,000 dermatologists globally.</li>
  <li><strong>Compact 50ml Bottle:</strong> Perfect size for daily morning routines, handbag, and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Shake the bottle thoroughly before use to activate Netlock technology.</li>
  <li><strong>Step 2:</strong> Apply a generous amount of La Roche-Posay fluid onto face, neck, and eye contour 20 minutes before sun exposure.</li>
  <li><strong>Step 3:</strong> Reapply every 2 hours or post-swimming and towel drying (use daily every morning).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Mexoryl 400 & Advanced UV Filters:</strong> Shield against deep ultra-long UVA and UVB radiation.</li>
  <li><strong>La Roche-Posay Thermal Spring Water:</strong> Soothes skin while guarding against oxidative stress and irritation.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical morning facial, neck, and eye contour application.</li>
  <li>Avoid direct peak midday solar exposure even while wearing sunscreen.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with sensitive skin seeking La Roche-Posay Anthelios 50ml Fluid for ultimate invisible sun protection.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>La Roche-Posay</td></tr>
  <tr><th>Category</th><td>Skincare / La Roche-Posay Anthelios Medical Sunscreens 50ml</td></tr>
  <tr><th>Product Type</th><td>SPF 50+ Mexoryl 400 Invisible Fluid Sunscreen for Sensitive Skin (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Specifically Sensitive, Reactive & Eye Contours)</td></tr>
  <tr><th>Finish</th><td>Completely protected, non-greasy, matte & white-mark-free skin</td></tr>
  <tr><th>Texture</th><td>Ultra-lightweight fast-absorbing invisible fluid water</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-free (or mild medical scent)</td></tr>
  <tr><th>Active Ingredients</th><td>Mexoryl 400 Filter, La Roche-Posay Thermal Spring Water, Netlock Technology</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>La Roche-Posay Laboratoire Dermatologique France</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Mexoryl 400 Ultra-Long UVA Absorption & Netlock Film Technology</h2>

<h3>What problem does this solve?</h3>
<p>La Roche-Posay Anthelios Sunscreen resolves solar burns, deep UVA-induced melasma and hyperpigmentation, photo-aging wrinkles, and eye stinging.</p>

<h3>Why choose La Roche-Posay Anthelios?</h3>
<p>Mexoryl 400 is the sole filter covering ultra-long UVA wavelengths (380-400nm), while Netlock technology forms a uniform micro-gel net resisting water and sweat.</p>"""

    en_faqs = [
        ("What is La Roche-Posay Anthelios Sunscreen 50 ml?", "It is a breakthrough medical sunscreen fluid from La Roche-Posay France with Mexoryl 400 filter and SPF 50+ for sensitive skin and eye contours (50ml)."),
        ("What are the benefits of Mexoryl 400 filter and SPF 50+?", "Mexoryl 400 guards against deep ultra-long UVA rays causing spots and wrinkles, while SPF 50+ ensures total sunburn defense."),
        ("Does it leave white marks or greasy shine?", "No, invisible fluid texture absorbs instantly with zero white marks or greasy residue."),
        ("What volume is contained in this bottle?", "50ml fluid bottle."),
        ("How do I use it correctly?", "Shake bottle, apply onto face, neck, and eye contour 20 minutes before sun exposure, reapply every 2 hours."),
        ("Is it safe for sensitive eye contours without stinging?", "Yes, ophthalmologically tested safe for sensitive eyes (Anti-Eye Stinging)."),
        ("Where is La Roche-Posay Sunscreen manufactured?", "In France by La Roche-Posay Laboratoire Dermatologique."),
        ("How do I verify authenticity at Ekleel Abha?", "All La Roche-Posay products at Ekleel Abha are 100% original."),
        ("Is it water, sweat, and sand resistant?", "Yes, superior resistance to water, sweat, and sand during sports and swimming."),
        ("Is it suitable for sensitive skin?", "Yes, specifically formulated for sensitive, reactive, and oily skin types."),
        ("Is the 50ml bottle handbag friendly?", "Yes, sleek compact bottle ideal for handbag and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is La Roche-Posay the #1 dermatologist recommended brand?", "Yes, La Roche-Posay is the #1 dermatologist recommended sunscreen brand globally."),
        ("How many times daily?", "Every morning before sun exposure, reapplying every 2 hours."),
        ("Does it prevent sun hyperpigmentation and photo-aging?", "Yes, effectively guards against solar spots, melasma, and premature wrinkles."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it serve as a good makeup base?", "Yes, excellent makeup base due to invisible fast-absorbing finish."),
        ("Should I shake the bottle before use?", "Yes, shaking activates Netlock technology and distributes filters."),
        ("Does it clog pores or cause breakouts?", "No, lightweight non-comedogenic formula."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Should I wear it on cloudy days?", "Yes, UV rays penetrate clouds requiring daily morning protection."),
        ("Is it a luxury skincare gift?", "Yes, a premier medical skincare essential."),
        ("Does it dry quickly without residue?", "Yes, absorbs and dries in seconds with zero residue."),
        ("Are spray and oil versions available?", "Yes, the Anthelios family offers multiple specialized formats.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2022",
        "sku": "EK-2022",
        "gtin": "3337875797580",
        "brand": "La Roche-Posay",
        "ar": {
            "title": "واقي شمس سائل للبشرة الحساسة انثيليوس  من لاروش بوزي 50 مل",
            "meta_title": "واقي شمس لاروش بوزي انثيليوس 50مل | إكليل أبها",
            "meta_description": "اشتري واقي شمس سائل انثيليوس من لاروش بوزي (50 مل). واقي فلويد طبي بـ Mexoryl 400 و SPF 50+ للبشرة الحساسة ومحيط العينين. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["لاروش_بوزي", "انثيليوس", "واقي_شمس_لاروش", "فلويد_البشرة_الحساسة", "إكليل_أبها"]
        },
        "en": {
            "title": "La Roche-Posay Anthelios Sunscreen 50 ml",
            "meta_title": "La Roche-Posay Anthelios Sunscreen 50ml | Ekleel Abha",
            "meta_description": "Buy original La Roche-Posay Anthelios Sunscreen (50ml). French Mexoryl 400 SPF 50+ invisible fluid for sensitive skin. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["la_roche_posay", "anthelios", "la_roche_sunscreen", "mexoryl_400", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 61 builders complete")
