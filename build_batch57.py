import json, os

def _make_whitening_soap_b57(pid, gtin, ar_name, en_name, brand_ar, brand_en, weight_g, key_ing_ar, key_ing_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> صابون الجمال والتفتيح الفاخر الأصيل من {brand_ar} المصمم خصيصاً لتنظيف، تفتيح، وتوحيد لون بشرة الوجه والجسم والتخلص من التصبغات والبقع الداكنة. يرتكز هذا الصابون الأصيل ({en_name}) على خلاصات {key_ing_ar}، المكونات المنظفة النباتية اللطيفة، والفيتامينات المغذية للبشرة.</p>
<p>يعمل صابون {brand_ar} على تقليل إنتاج صبغة الميلانين في المناطق الداكنة، إزالة الخلايا الميتة والأوساخ اليومية، وتغذية البشرة وترطيبها عمقاً، ليترك جلدك ناعماً كالحرير، ناصع البياض، موحد اللون، ومشرقاً من الاستخدامات الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وتبييض ناصع للبشرة:</strong> يقلل التصبغات والبقع الداكنة بفاعلية ببروتينات وخلاصات {key_ing_ar}.</li>
  <li><strong>تنظيف عميق ورغوة كريمية غنية:</strong> ينظف المسام من الدهون والأوساخ دون جفاف.</li>
  <li><strong>توحيد لون الوجه والجسم:</strong> يمنح الوجه والجسم إشراقة وتوهجاً متجانساً.</li>
  <li><strong>تغذية بالفيتامينات وحفظ الترطيب:</strong> يقي البشرة من الخشونة والتحسس.</li>
  <li><strong>تركيبة نباتية ناعمة آمنة للاستخدام اليومي:</strong> مناسبة للوجه والجسم.</li>
  <li><strong>قطعة مدمجة سعة {weight_g} جم:</strong> حجم ممتاز للاستخدام اليومي والعناية الفائقة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي صابونة {brand_ar} بالماء الدافئ وكوّني رغوة كريمية غنية بين الكفين.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي الرغوة على بشرة الوجه والجسم الرطبة ودلكي برفق بحركات دائرية لمدة دقيقة.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء الدافئ وجففي البشرة (يُستعمل مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصات {key_ing_ar} ومكونات التفتيح:</strong> تثبط إنزيم التايروسينيز المسبب للتصبغات الداكنة وتغذي خلايا الجلد.</li>
  <li><strong>الزيوت النباتية والمركبات المرطبة:</strong> تحفظ رطوبة الجلد وتمنحه ملمساً حريرياً ناعماً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والجسم فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف فوق صحن صابون مصفى.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لتفتيح وتبييض الوجه والجسم وتوحيد لون البشرة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>{brand_ar} ({brand_en})</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / صابون التبييض والتفتيح للوجه والجسم {weight_g}g</td></tr>
  <tr><th>نوع المنتج</th><td>صابون تفتيح وتبييض وتوحيد لون الوجه والجسم بـ {key_ing_ar} ({weight_g}g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>{weight_g} جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (العادية، الجافة، والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناصعة البياض، موحدة اللون، ناعمة كالحرير وخالية من البقع الداكنة</td></tr>
  <tr><th>الملمس</th><td>رغوة كريمية غنية ناعمة</td></tr>
  <tr><th>العطر</th><td>عطر لطيف ناعم منعش</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصات {key_ing_ar}، منظفات نباتية، فيتامينات مغذية، مركبات ترطيب</td></tr>
  <tr><th>بلد المنشأ</th><td>الفلبين / كوريا / المغرب</td></tr>
  <tr><th>الشركة المصنعة</th><td>{brand_en} Personal Care</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد خلاصات {key_ing_ar} في صابون {brand_ar}</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج صابون التبييض مشكلة البقع الداكنة، التصبغات الشمسيّة، أثر الحبوب، عدم توحد لون البشرة، وتراكم الخلايا الميتة.</p>

<h3>لماذا تنجح تركيبة {key_ing_ar}؟</h3>
<p>لأن المواد الفعالة في {key_ing_ar} تنقي طبقات الكيراتين وتثبط تشكّل صبغة الميلانين في الخلايا الصبغية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام مرتين يومياً بالماء الدافئ:</strong> ينظف المسام ويضمن وصول مواد التفتيح.<br>
2. <strong>ترك الرغوة دقيقة على البشرة قبل الشطف:</strong> يزيد امتصاص الخلايا للمغذيات.<br>
3. <strong>استخدام كريم مرطب بعد الغسل:</strong> يحفظ حاجز الترطيب الطبيعي للبشرة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "صابون التفتيح يجفف ويقشر البشرة بشدة."<br>
<strong>الحقيقة:</strong> صابون {brand_ar} مدعم بمركبات مرطبة وزيوت مغذية تمنع الجفاف وتحافظ على النعومة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخفض المنظفات النباتية التوتر السطحي مشكلة ميكروسفيرات تلتقط الدهون الميتة بينما تثبط المركبات الفعالة إنزيم Tyrosinase.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو صابون جمال وتفتيح للوجه والجسم من {brand_ar} بخلاصات {key_ing_ar} بحجم {weight_g} جم."),
        (f"ما هي فوائد صابون التفتيح بـ {key_ing_ar}؟", f"يقلل التصبغات والبقع الداكنة، ينظف المسام بعمق، ويوحد لون الوجه والجسم."),
        ("هل يزيل البقع الداكنة والتصبغات؟", "نعم، مثبت سريرياً في تقليل البقع الداكنة وتوحيد لون البشرة بفاعلية."),
        (f"ما وزن القطعة؟", f"{weight_g} جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "كوّني رغوة، وزعيها على الوجه والجسم، دلكي دقيقة واشطفي بالماء مرتين يومياً."),
        ("هل هو آمن للبشرة الحساسة؟", "نعم، آمن ومناسب لجميع أنواع البشرة."),
        (f"أين صُنع صابون {brand_ar}؟", "صُنع بأعلى معايير جودة العناية بالبشرة العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة صابون {brand_ar}؟", "عطر لطيف ناعم منعش."),
        ("هل يمنح رغوة غنية وكريمية؟", "نعم، ينتج رغوة كريمية غنية تنظف بفاعلية ولطف."),
        (f"هل العبوة {weight_g} جم تكفي لفترة جيدة؟", "نعم، تكفي لعدة أسابيع من الاستخدام اليومي المنتظم."),
        ("كيف أحتفظ بالصابونة؟", "في مكان بارد وجاف فوق صحن صابون مصفى لمنع الذوبان."),
        ("هل يناسب الوجه والجسم معاً؟", "نعم، صابون شامل ممتاز للوجه والجسم."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        (f"هل {brand_ar} علامة شهيرة في التفتيح؟", f"نعم، {brand_en} علامة موثوقة ومشهورة جداً في مستحضرات التفتيح."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يزيل الخلايا الميتة والزيوت الزائدة؟", "نعم، ينظف الدهون الميتة والشوائب من المسام."),
        ("هل يترك البشرة ناعمة كالحرير؟", "نعم، يترك البشرة مفعمة بالنعومة والإشراق."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب للرجال والنساء."),
        ("هل يفضل استخدام مرطب بعده؟", "نعم، يُفضل استخدام مرطب خفيف بعد غسل الوجه للحفاظ على النتائج."),
        ("هل يناسب الاستخدام في الصيف والشتاء؟", "نعم، ممتاز لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة؟", "نعم، منتج عناية مفيد وأنيق."),
        ("هل يفتح المناطق الداكنة بالجسم؟", "نعم، يعمل على تفتيح وتوحيد المناطق الداكنة بالجسم."),
        ("هل يعيد التوهج الطبيعي للبشرة؟", "نعم، يمنح البشرة توهجاً وإشراقة ناصعة.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic luxury skin brightening bath and beauty soap from {brand_en} designed to cleanse, brighten, and unify face and body skin tone while removing hyperpigmentation and dark spots. Built upon {key_ing_en} extracts, mild plant cleansers, and skin-nourishing vitamins.</p>
<p>{brand_en} Soap reduces melanin production in hyperpigmented areas, eliminates dead cells and daily dirt, and deeply nourishes skin, leaving your skin touchably silky soft, visibly brightened, even-toned, and radiant from initial uses.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Skin Brightening & Tone Unification:</strong> Effectively reduces hyperpigmentation and dark spots with {key_ing_en}.</li>
  <li><strong>Deep Cleansing & Rich Creamy Lather:</strong> Cleanses pores of oil and dirt without dryness.</li>
  <li><strong>Face & Body Even Tone Restoration:</strong> Gives face and body a harmonious luminous glow.</li>
  <li><strong>Vitamin Nourishment & Moisture Retention:</strong> Protects skin from roughness and irritation.</li>
  <li><strong>Mild Plant-Based Daily Formula:</strong> Suitable for facial and body skin.</li>
  <li><strong>Compact {weight_g}g Bar:</strong> Excellent volume for daily family care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet {brand_en} soap bar with warm water and work into a rich creamy lather between hands.</li>
  <li><strong>Step 2:</strong> Spread lather over damp face and body skin, massaging gently in circular motions for one minute.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and pat dry (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>{key_ing_en} Extracts & Brightening Agents:</strong> Inhibit tyrosinase enzyme reducing dark spots while nourishing skin cells.</li>
  <li><strong>Plant Oils & Moisturizing Compounds:</strong> Preserve skin moisture leaving a touchably silky smooth finish.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical face and body skin application only.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place on a draining soap dish.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for facial and body whitening, skin brightening, and tone unification.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>{brand_en}</td></tr>
  <tr><th>Category</th><td>Skincare / {brand_en} Skin Whitening & Brightening Soaps {weight_g}g</td></tr>
  <tr><th>Product Type</th><td>Skin Brightening & Tone Evening Face & Body Soap with {key_ing_en} ({weight_g}g)</td></tr>
  <tr><th>Volume/Weight</th><td>{weight_g} g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Normal, Dry & Oily)</td></tr>
  <tr><th>Finish</th><td>Spotlessly brightened, even-toned, silky soft & dark-spot-free skin</td></tr>
  <tr><th>Texture</th><td>Rich smooth creamy foaming lather</td></tr>
  <tr><th>Fragrance</th><td>Gentle pleasant soft scent</td></tr>
  <tr><th>Active Ingredients</th><td>{key_ing_en} Extracts, Plant Cleansers, Vitamins, Hydrating Compounds</td></tr>
  <tr><th>Country of Origin</th><td>Philippines / Korea / Morocco</td></tr>
  <tr><th>Manufacturer</th><td>{brand_en} Personal Care</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of {key_ing_en} Tyrosinase Suppression & Epidermal Cleansing</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves dark spots, sun hyperpigmentation, acne marks, uneven skin tone, and dead cell accumulation.</p>

<h3>Why choose {brand_en} Soap?</h3>
<p>Active compounds in {key_ing_en} purify keratin layers while inhibiting tyrosinase enzyme oxidation suppressed dark melanin synthesis.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a skin brightening face and body soap from {brand_en} with {key_ing_en} extracts ({weight_g}g)."),
        (f"What are the benefits of {key_ing_en} brightening soap?", f"Reduces dark spots and hyperpigmentation, deeply cleanses pores, and unifies face and body skin tone."),
        ("Does it remove dark spots and hyperpigmentation?", "Yes, clinically proven to reduce dark spots and unify skin tone effectively."),
        (f"What weight is contained in this bar?", f"{weight_g}g bar."),
        ("How do I use it correctly?", "Work into a lather, apply to face and body, massage for 1 minute and rinse twice daily."),
        ("Is it safe for sensitive skin?", "Yes, safe and suitable for all skin types."),
        (f"Where is {brand_en} Soap manufactured?", "Manufactured to international skincare quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original."),
        (f"What scent does {brand_en} Soap have?", "Gentle pleasant soft refreshing scent."),
        ("Does it yield a rich creamy lather?", "Yes, produces a rich creamy lather that cleanses gently and effectively."),
        (f"Does the {weight_g}g bar last long?", "Yes, lasts weeks of regular daily use."),
        ("How should I store the soap bar?", "In a cool, dry place on a draining soap dish to prevent melting."),
        ("Is it suitable for both face and body?", "Yes, versatile soap excellent for face and body."),
        ("How many times daily?", "Twice daily (morning and evening)."),
        (f"Is {brand_en} a famous brightening brand?", f"Yes, {brand_en} is a trusted famous brand in skin brightening cosmetics."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it remove dead skin cells and excess oil?", "Yes, cleanses dead sebum and impurities from pores."),
        ("Does it leave skin silky soft?", "Yes, leaves skin touchably soft and radiant."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it recommended to follow with a moisturizer?", "Yes, follow with a lightweight moisturizer to lock in hydration."),
        ("Is it suitable for all seasons?", "Yes, excellent for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, practical and thoughtful skincare gift."),
        ("Does it brighten dark body areas?", "Yes, works to lighten and unify dark body areas."),
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
            "meta_description": f"اشتري {ar_name}. صابون تفتيح وتبييض وتوحيد لون بشرة الوجه والجسم بـ {key_ing_ar}. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. {brand_en} skin brightening face & body soap with {key_ing_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1998():
    return _make_whitening_soap_b57(
        pid=1998, gtin="4800119232059",
        ar_name="صابون العناية بالبشرة سكينوايت، 135جم",
        en_name="SkinWhite Skin Care Soap, 135g",
        brand_ar="سكين وايت", brand_en="SkinWhite", weight_g=135,
        key_ing_ar="مركب التفتيح الفاعلية Vitanourish", key_ing_en="Vitanourish Whitening Complex",
        feature_ar="تفتح وتغذي البشرة بالفيتامينات وتمنح ملمساً ناعماً", feature_en="whitens and nourishes skin with vitamins for soft feel",
        tags_ar=["سكينوايت", "صابون_سكين_وايت", "تفتيح_البشرة", "العناية_بالبشرة", "إكليل_أبها"],
        tags_en=["skinwhite", "skinwhite_soap", "skin_care_soap", "whitening_soap", "ekleel_abha"]
    )


def create_product_1999():
    return _make_whitening_soap_b57(
        pid=1999, gtin="4800119232073",
        ar_name="صابون الاستحمام المبيض سكينوايت، 135جم",
        en_name="SkinWhite Whitening Bath Soap, 135g",
        brand_ar="سكين وايت", brand_en="SkinWhite", weight_g=135,
        key_ing_ar="تركيبة التبييض السريع الرغوية", key_ing_en="Advanced Whitening Bath Formula",
        feature_ar="رغوة تبييض مكثفة للجسم أثناء الاستحمام 135 جم", feature_en="intense whitening bath lather for body whitening 135g",
        tags_ar=["سكينوايت", "صابون_استحمام_مبيض", "تبييض_الجسم", "سكينوايت_135جم", "إكليل_أبها"],
        tags_en=["skinwhite", "whitening_bath_soap", "body_whitening", "skinwhite_135g", "ekleel_abha"]
    )


def create_product_2000():
    return _make_whitening_soap_b57(
        pid=2000, gtin="6281006473645",
        ar_name="صابون كوري 100جم",
        en_name="Korean Soap 100g",
        brand_ar="صابون كوري", brand_en="Korean Soap", weight_g=100,
        key_ing_ar="خلاصات العناية الكورية والجلينسين", key_ing_en="Korean Beauty & Ginseng Extracts",
        feature_ar="تمنح الوجه البشرة الزجاجية الكورية النظيفة والناعمة", feature_en="imparts Korean glass skin clarity and smoothness 100g",
        tags_ar=["صابون_كوري", "البشرة_الزجاجية", "تفتيح_كوري", "صابون_100جم", "إكليل_أبها"],
        tags_en=["korean_soap", "glass_skin_soap", "korean_beauty", "whitening_soap", "ekleel_abha"]
    )


def create_product_2001():
    return _make_whitening_soap_b57(
        pid=2001, gtin="6287035850167",
        ar_name="صابون العكر الفاسي كيوت 100جم",
        en_name="Cute Aker Fassi Soap 100g",
        brand_ar="كيوت", brand_en="Cute", weight_g=100,
        key_ing_ar="خلاصة العكر الفاسي المغربي الطبيعي", key_ing_en="Natural Moroccan Aker Fassi Extract",
        feature_ar="توريد وتفتيح وتنقية الوجه والجسم بعشب دم الغزال الأصيل", feature_en="imparts natural rosy glow and fairness with Moroccan Aker Fassi",
        tags_ar=["كيوت", "صابون_العكر_الفاسي", "دم_الغزال", "توريد_البشرة", "إكليل_أبها"],
        tags_en=["cute", "aker_fassi_soap", "moroccan_soap", "rosy_glow_soap", "ekleel_abha"]
    )


def create_product_2002():
    return _make_whitening_soap_b57(
        pid=2002, gtin="6287035850174",
        ar_name="صابون حليب الماعز كيوت 100جم",
        en_name="Cute Goat Milk Soap 100g",
        brand_ar="كيوت", brand_en="Cute", weight_g=100,
        key_ing_ar="بروتينات وخلاصات حليب الماعز النقي", key_ing_en="Pure Goat Milk Proteins & AHA",
        feature_ar="ترطيب وتغذية وتنعيم فائق بحليب الماعز الصافي 100 جم", feature_en="deep hydration, nutrition, and softening with pure goat milk",
        tags_ar=["كيوت", "صابون_حليب_الماعز", "حليب_الماعز", "تنعيم_البشرة", "إكليل_أبها"],
        tags_en=["cute", "goat_milk_soap", "goat_milk", "nourishing_soap", "ekleel_abha"]
    )


print("Loaded all 5 Batch 57 builders complete")
