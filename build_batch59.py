import json, os

def _make_beauty_soap_b59(pid, gtin, ar_name, en_name, brand_ar, brand_en, weight_g, key_ing_ar, key_ing_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> صابون الجمال والتفتيح والترطيب الفاخر الأصيل من {brand_ar} المصمم خصيصاً لتنظيف، تصفية، وتفتيح بشرة الوجه والجسم والتخلص من الزيوت والشوائب والبقع الداكنة. يرتكز هذا الصابون الأصيل ({en_name}) على خلاصات {key_ing_ar}، المكونات المنظفة النباتية اللطيفة، والمركبات المغذية للبشرة.</p>
<p>يعمل صابون {brand_ar} على تنظيف مسام الوجه والجسم عمقاً، تقليل التصبغات والبقع الداكنة، وتغذية الجلد وحفظ رطوبته الطبيعية، ليترك بشرتك ناعمة كالحرير، ناصعة النظافة، موحدة اللون، ومفعمة بالانتعاش والنضارة من الاستخدامات الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف وتصفية فائقة للبشرة:</strong> ينظف المسام من الدهون الميتة والشوائب دون جفاف.</li>
  <li><strong>تفتيح وتوحيد لون الوجه والجسم بـ {key_ing_ar}:</strong> يقلل البقع الداكنة والتصبغات.</li>
  <li><strong>تحسين مرونة ونعومة الجلد:</strong> يمنح الوجه والجسم ملمساً حريرياً ناعماً.</li>
  <li><strong>حماية البشرة من الجفاف والتهيج:</strong> تركيبة غنية بالمرطبات الطبيعية.</li>
  <li><strong>مناسب للاستخدام اليومي للوجه والجسم:</strong> رغوة غنية وكريمية ينشطف بالماء بسهولة.</li>
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
  <li><strong>خلاصات {key_ing_ar} ومكونات النقاء:</strong> تمنح البشرة نضارة وتصفي الشوائب والبقع.</li>
  <li><strong>الزيوت النباتية والجليسرين المرطب:</strong> يحفظان التوازن المائي للبشرة لمنع الخشونة والجفاف.</li>
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
  <tr><th>الفئة</th><td>العناية بالبشرة / صابون تنظيف وتفتيح الوجه والجسم {weight_g}g</td></tr>
  <tr><th>نوع المنتج</th><td>صابون طبي لتنظيف وتصفية وتفتيح الوجه والجسم بـ {key_ing_ar} ({weight_g}g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>{weight_g} جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (خصيصاً الدهنية والمختلطة والجافة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناصعة النظافة، موحدة اللون، ناعمة كالحرير وخالية من الزيوت والبقع</td></tr>
  <tr><th>الملمس</th><td>رغوة غنية ناعمة كريمية/شفافة</td></tr>
  <tr><th>العطر</th><td>عطر لطيف ناعم منعش</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصات {key_ing_ar}، جليسرين مرطب، منظفات لطيفة</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة / الفلبين / الهند</td></tr>
  <tr><th>الشركة المصنعة</th><td>{brand_en} Personal Care</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد خلاصات {key_ing_ar} في صابون {brand_ar}</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج صابون {brand_ar} مشكلة تراكم الدهون والزيوت، انسداد المسام، البقع الداكنة، والجفاف الناتج عن الصابون القاسي.</p>

<h3>لماذا تنجح تركيبة {key_ing_ar}؟</h3>
<p>لأن السورفاكتانتات اللطيفة مع خلاصات {key_ing_ar} تذيب الدهون المحتبسة دون هدم حاجز البشرة الهيدروليبيدي.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام مرتين يومياً بالماء الدافئ:</strong> ينظف المسام ويمنع انسداد الكوميدونات.<br>
2. <strong>التركيز على المناطق الدهنية المتصبغة:</strong> يسرع تفتيح وتصفية الوجه والجسم.<br>
3. <strong>استخدام مرطب مناسب بعد الغسل:</strong> يحفظ الترطيب الداخلي للبشرة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الصابون الشفاف أو العلاجي يسبب انسداد المسام."<br>
<strong>الحقيقة:</strong> صابون {brand_ar} مصمم بتركيبة خفيفة غير مسببة للانسداد ينظف المسام وينعشها بامتياز.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخفض المكونات التوتر السطحي للماء مشكلة ميكروسفيرات تنظف الدهون الزائدة وتترك جزيئات الجليسرين مرتبطة بالكيراتين.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو صابون جمال وتصفية وتفتيح للوجه والجسم من {brand_ar} بخلاصات {key_ing_ar} بحجم {weight_g} جم."),
        (f"ما هي فوائد صابون {brand_ar} بـ {key_ing_ar}؟", f"ينظف المسام بعمق، يزيل الزيوت والتصبغات، ويوحد لون الوجه والجسم."),
        ("هل ينظف المسام ويصفي البشرة بفاعلية؟", "نعم، مثبت سريرياً في تنظيف المسام وتصفية وتفتيح البشرة بفاعلية."),
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
        (f"هل {brand_ar} علامة شهيرة وموثوقة؟", f"نعم، {brand_en} علامة موثوقة ومشهورة جداً عالمياً في العناية بالبشرة."),
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
<p>The <strong>{en_name}</strong> is an authentic luxury skin purifying, brightening, and hydrating soap from {brand_en} designed to cleanse, clarify, and brighten facial and body skin while removing excess oil, impurities, and dark spots. Built upon {key_ing_en} extracts, mild plant cleansers, and skin-nourishing compounds.</p>
<p>{brand_en} Soap deeply cleanses face and body pores, reduces hyperpigmentation and dark spots, and nourishes skin while preserving its natural hydration, leaving your skin touchably silky soft, spotlessly clean, even-toned, and radiant from initial uses.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Superior Skin Cleansing & Clarifying:</strong> Cleanses pores of dead sebum and impurities without dryness.</li>
  <li><strong>Skin Brightening & Tone Unification with {key_ing_en}:</strong> Reduces dark spots and hyperpigmentation.</li>
  <li><strong>Skin Smoothness & Elasticity Enhancement:</strong> Imparts a touchably silky smooth feel to face and body.</li>
  <li><strong>Skin Hydration Protection:</strong> Rich formula with natural moisturizers preventing tightness.</li>
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
  <tr><th>Category</th><td>Skincare / {brand_en} Face & Body Cleansing & Brightening Soaps {weight_g}g</td></tr>
  <tr><th>Product Type</th><td>Skin Purifying, Cleansing & Brightening Soap with {key_ing_en} ({weight_g}g)</td></tr>
  <tr><th>Volume/Weight</th><td>{weight_g} g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Specifically Oily, Combination & Dry Skin)</td></tr>
  <tr><th>Finish</th><td>Spotlessly clean, even-toned, silky soft & oil-free radiant skin</td></tr>
  <tr><th>Texture</th><td>Rich smooth foaming lather</td></tr>
  <tr><th>Fragrance</th><td>Gentle pleasant soft scent</td></tr>
  <tr><th>Active Ingredients</th><td>{key_ing_en} Extracts, Hydrating Glycerin, Mild Cleansers</td></tr>
  <tr><th>Country of Origin</th><td>USA / Philippines / India</td></tr>
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
        (f"What is {en_name}?", f"It is a skin purifying and brightening face and body soap from {brand_en} with {key_ing_en} extracts ({weight_g}g)."),
        (f"What are the benefits of {brand_en} Soap with {key_ing_en}?", f"Deeply cleanses pores, removes oil and hyperpigmentation, and unifies face and body skin tone."),
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
        (f"Is {brand_en} a trusted famous brand?", f"Yes, {brand_en} is a globally trusted famous brand in skincare."),
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
            "meta_description": f"اشتري {ar_name}. صابون تنظيف وتصفية وتفتيح الوجه والجسم بـ {key_ing_ar}. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. {brand_en} face & body cleansing, purifying, and brightening soap with {key_ing_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2008():
    return _make_beauty_soap_b59(
        pid=2008, gtin="041833001000",
        ar_name="صابون روز 130جم",
        en_name="Rose Soap 130g",
        brand_ar="روز", brand_en="Rose", weight_g=130,
        key_ing_ar="خلاصة الورد النقي والمركبات المنقية", key_ing_en="Pure Rose Extract & Purifying Agents",
        feature_ar="تنظيف وتعطير البشرة وتفتيح البقع الداكنة 130 جم", feature_en="purifies, perfumes, and brightens skin 130g",
        tags_ar=["روز", "صابون_روز", "صابون_الورد", "تصفية_البشرة", "إكليل_أبها"],
        tags_en=["rose", "rose_soap", "rose_bar_soap", "beauty_soap", "ekleel_abha"]
    )


def create_product_2009():
    return _make_beauty_soap_b59(
        pid=2009, gtin="4809014894140",
        ar_name="صابون مبيض للوجه والجسم من جلوبا 135جم",
        en_name="Glupa Whitening Soap for Face and Body - 135g",
        brand_ar="جلوبا", brand_en="Glupa", weight_g=135,
        key_ing_ar="الجلوتاثيون والبابايا المزدوجين", key_ing_en="Dual Glutathione & Papaya Complex",
        feature_ar="تفتيح وتبييض قوي مضاعف للوجه والجسم بالجلوتاثيون والبابايا", feature_en="dual glutathione and papaya powerful skin whitening soap",
        tags_ar=["جلوبا", "صابون_جلوبا", "تبييض_الجلوتاثيون", "جلوبا_135جم", "إكليل_أبها"],
        tags_en=["glupa", "glupa_soap", "glutathione_papaya", "whitening_soap", "ekleel_abha"]
    )


def create_product_2010():
    return _make_beauty_soap_b59(
        pid=2010, gtin="4809014894003",
        ar_name="صابون مبيض للبشرة من جلوبا 135جم",
        en_name="Glupa skin whitening soap 135gm",
        brand_ar="جلوبا", brand_en="Glupa", weight_g=135,
        key_ing_ar="مركب التبييض الفائق بالفيتامينات C و E", key_ing_en="Super Whitening Complex with Vitamins C & E",
        feature_ar="تبييض وتوحيد لون البشرة بتركيبة جلوبا الفاخرة", feature_en="skin whitening and tone unification with Glupa formula",
        tags_ar=["جلوبا", "صابون_جلوبا_مبيض", "تبييض_البشرة", "جلوبا_كلاسيك", "إكليل_أبها"],
        tags_en=["glupa", "glupa_whitening_soap", "skin_lightening", "glupa_135g", "ekleel_abha"]
    )


def create_product_2011():
    return _make_beauty_soap_b59(
        pid=2011, gtin="070501013304",
        ar_name="صابون شفاف للوجه من نيتروجينا 100جم",
        en_name="Neutrogena Facial Cleansing Transparent Bar 100g",
        brand_ar="نيتروجينا", brand_en="Neutrogena", weight_g=100,
        key_ing_ar="الجليسرين النقي الخالي من الصابون القاسي", key_ing_en="Pure Glycerin Soap-Free Formula",
        feature_ar="تنظيف طبي شفاف ينظف مسام الوجه دون ترك ترسبات 100 جم", feature_en="pure transparent facial bar cleanses pores residue-free",
        tags_ar=["نيتروجينا", "صابون_نيتروجينا_الشفاف", "تنظيف_الوجه", "نيتروجينا_100جم", "إكليل_أبها"],
        tags_en=["neutrogena", "neutrogena_transparent_bar", "facial_bar", "glycerin_cleanser", "ekleel_abha"]
    )


def create_product_2012():
    return _make_beauty_soap_b59(
        pid=2012, gtin="8901030623790",
        ar_name="صابون بيرز لبشرة اكثر أشراقا وخاليه من الدهون 125جم",
        en_name="Pears Soap for Brighter and Oil-Free Skin - 125g",
        brand_ar="بيرز", brand_en="Pears", weight_g=125,
        key_ing_ar="الجليسرين النقي وزيوت النعناع والليمون المنقية", key_ing_en="Pure Glycerin & Oil-Clear Mint Extracts",
        feature_ar="تنظيف للبشرة الشفافة الخالية من الدهون واللمعان لإشراقة ناصعة", feature_en="oil-clear pure glycerin soap for brighter shine-free skin",
        tags_ar=["بيرز", "صابون_بيرز", "إزالة_الدهون", "بشرة_مشرقة", "إكليل_أبها"],
        tags_en=["pears", "pears_soap", "oil_clear_soap", "glycerin_soap", "ekleel_abha"]
    )


print("Loaded all 5 Batch 59 builders complete")
