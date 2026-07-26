import json, os

def _make_hobby_shower_gel(pid, gtin, ar_name, en_name, scent_ar, scent_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> جل الاستحمام اليومي الفاخر بحجم ضخم (500 مل) من هوبي التركية المصمم لمنح جسمك نظافة عميقة ورغوة غنية وانتعاشاً عاطراً يوقظ الحواس. يرتكز هذا الجل المنعش ({en_name}) على تركيبة المكونات المنظفة النباتية اللطيفة، خلاصات {scent_ar} المغذية، والمركبات المرطبة لبشرة الجسم.</p>
<p>يعمل جل استحمام هوبي على تنظيف مسام الجسم وإزالة الدهون والأوساخ دون جفاف البشرة، تغذية الجلد وإعادة التوازن المائي، وتغليف جسمك بنفحات {scent_ar} الفواحة، ليترك بشرتك ناعمة كالحرير، مرطبة، ومعطرة بالنظافة والانتعاش طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف عميق ورغوة كريمية غنية:</strong> ينظف الجسم بلطف دون انتزاع الزيوت الطبيعية.</li>
  <li><strong>انتعاش وعطر يدوم طوال اليوم بنفحات {scent_ar}:</strong> {feature_ar} ويمنح البشرة رائحة فواحة.</li>
  <li><strong>ترطيب وتنعيم لبشرة الجسم:</strong> يحفظ حاجز الترطيب الطبيعي للجلد.</li>
  <li><strong>تركيبة خفيفة متوازنة الحموضة (pH Balanced):</strong> مناسبة للاستخدام اليومي لجميع أنواع البشرة.</li>
  <li><strong>جودة هوبي (Hobby) التركية الشهيرة:</strong> علامة رائدة في العناية الشخصية والاستحمام.</li>
  <li><strong>عبوة اقتصادية ضخمة سعة 500 مل:</strong> حجم ممتازة يكفي لاستخدام عائلي يومي مستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الجسم بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من جل هوبي على ليفة الاستحمام أو الكفين وكوّني رغوة غنية.</li>
  <li><strong>الخطوة الثالثة:</strong> دلكي الجسم برفق بحركات دائرية ثم اشطفي جيداً بالماء (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>منظفات نباتية لطيفة ومتوازنة الحموضة:</strong> تنظف مسام الجسم بفاعلية ودون أي جفاف.</li>
  <li><strong>خلاصات {scent_ar} والمغذيات المرطبة:</strong> {feature_ar} وتمنح الجلد نعومة ورائحة عاطرة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} للانتعاش اليومي والنظافة وترطيب بشرة الجسم 500 مل.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>هوبي (Hobby)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / جلات الاستحمام المعطرة من هوبي 500ml</td></tr>
  <tr><th>نوع المنتج</th><td>جل استحمام يومي مرطب ورغوي بنفحات {scent_ar} (500ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (العادية، الجافة والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، مرطب، ناصع النظافة ومفعم برائحة {scent_ar}</td></tr>
  <tr><th>الملمس</th><td>سائل جل شفاف رغوي غني</td></tr>
  <tr><th>العطر</th><td>عطر {scent_ar} المنعش الفواح</td></tr>
  <tr><th>المكونات النشطة</th><td>منظفات نباتية لطيفة، خلاصات {scent_ar}، مركبات مرطبة</td></tr>
  <tr><th>بلد المنشأ</th><td>تركيا (Turkey)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Hobby Kozmetik Turkey</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد التوازن الهيدروليبيدي وخلاصات {scent_ar} في جل هوبي (Hobby)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج جل استحمام هوبي مشكلة جفاف البشرة بعد الاستحمام بالصابون القاسي، تراكم الدهون والأوساخ اليومية، ورائحة العرق.</p>

<h3>لماذا تنجح تركيبة هوبي المنعشة؟</h3>
<p>لأن المنظفات السطحية متوازنة الحموضة (pH Balanced) تنظف دون تدمير حاجز البشرة الدهني بينما تثبت زيوت {scent_ar} العطرية على الجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام اليومي بالماء الدافئ:</strong> ينظف المسام وينشط الدورة الدموية.<br>
2. <strong>استخدام ليفة ناعمة:</strong> يزيد تكوين الرغوة الغنية ويزيل التراكمات السطحية.<br>
3. <strong>الشطف الجيد:</strong> يضمن عدم بقاء أي ترسبات صابونية على الجلد.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "جلات الاستحمام المعطرة تجفف البشرة."<br>
<strong>الحقيقة:</strong> جل هوبي مدعم بمركبات مرطبة تحفظ التوازن المائي للجلد أثناء التنظيف.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخفض السورفاكتانتات اللطيفة التوتر السطحي للماء وتأطر الجزيئات الزيتية والأوساخ داخل ميكروسفيرات ميكروبية ينشطف بها الماء بسلاسة.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو جل استحمام يومي مرطب ورغوي من هوبي التركية بنفحات {scent_ar} بحجم 500 مل."),
        (f"ما هي فوائد خلاصة {scent_ar} والمنظفات اللطيفة؟", f"تنظف المنظفات اللطيفة البشرة دون جفاف، بينما {feature_ar} وتمنح انطباعاً عاطراً طوال اليوم."),
        ("هل يمنح رغوة غنية وانتعاشاً طوال اليوم؟", "نعم، ينتج رغوة كريمية غنية ويترك الجسم معطراً ومبتهجاً."),
        ("ما حجم العبوة؟", "تأتي بعبوة ضخمة بسعة 500 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الجسم، ضعي كمية على الليفة وكوّني رغوة، دلكي برفق واشطفي بالماء يومياً."),
        ("هل هو آمن لجميع أنواع البشرة؟", "نعم، تركيبة متوازنة الحموضة آمنة لجميع أنواع بشرة الجسم."),
        ("أين صُنع جل استحمام هوبي؟", "صُنع في تركيا بواسطة Hobby Kozmetik Turkey."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات هوبي لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {scent_ar} المنعش الفواح."),
        ("هل يترك البشرة ناعمة ومرطبة؟", "نعم، يحافظ على رطوبة الجلد ونعومته الحريرية."),
        ("هل 500 مل تكفي للاستخدام العائلي؟", "نعم، عبوة ضخمة تكفي لعدة أشهر من الاستخدام العائلي اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب النساء والرجال؟", "نعم، مناسب لجميع أفراد الأسرة."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً أثناء الاستحمام."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، ينشطف بالماء الدافئ بسهولة دون ترك أثر لزج."),
        ("هل هوبي علامة تركية معتمدة؟", "نعم، Hobby علامة رائدة ومشهورة جداً في تركيا والعالم لمنتجات الاستحمام."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في إزالة رائحة العرق؟", "نعم، ينظف بفاعلية ويعطر الجسم بنفحات عاطرة."),
        ("هل يناسب الاستخدام بعد الرياضة؟", "نعم، ممتاز للانتعاش والنظافة بعد التمارين والرياضة."),
        ("هل يترك أثراً دهنياً؟", "لا، ينظف وينشطف بالكامل دون دهنية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل العبوة مزودة بغطاء مريح؟", "نعم، غطاء مريح يسهل صب كمية الجل."),
        ("هل يناسب الشتاء والصيف؟", "نعم، ممتاز لجميع فصول السنة."),
        ("هل يصلح هدية ضمن مجموعة الاستحمام؟", "نعم، خيار ممتاز جداً في مجموعات العناية الشخصية."),
        ("هل يغني عن استخدام الصابون القاسي؟", "نعم، بديل مرطب وألطف بكثير من الصابون القاسي.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is a luxury daily shower gel in a jumbo 500ml bottle from Hobby Turkey designed to provide deep body cleansing, rich lather, and an awakening fragranced freshness. Built upon gentle plant-derived cleansing agents, nourishing {scent_en} extracts, and skin-moisturizing compounds.</p>
<p>Hobby Shower Gel cleanses body pores of dirt and excess sebum without drying skin, nourishes and restores natural skin moisture balance, and coats your body in captivating {scent_en} notes, leaving your skin touchably silky soft, hydrated, and fresh all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Deep Cleansing & Rich Creamy Lather:</strong> Cleanses body gently without stripping natural skin oils.</li>
  <li><strong>All-Day Freshness & Fragrance with {scent_en} Notes:</strong> {feature_en} and imparts a lasting scent.</li>
  <li><strong>Body Skin Softening & Hydration:</strong> Preserves the skin's natural moisture barrier.</li>
  <li><strong>pH-Balanced Mild Formula:</strong> Suitable for daily use on all skin types.</li>
  <li><strong>Famous Quality of Hobby Turkey:</strong> A leading Turkish personal care and shower brand.</li>
  <li><strong>Generous 500ml Jumbo Bottle:</strong> Excellent value lasting months of continuous daily family use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet body skin with warm water during shower.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of Hobby gel onto a shower loofah or hands and work into a rich lather.</li>
  <li><strong>Step 3:</strong> Massage body gently in circular motions, then rinse thoroughly with water (use daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Gentle Plant Cleansers & pH Balanced Formula:</strong> Cleanse body pores effectively without causing dryness.</li>
  <li><strong>{scent_en} Extracts & Moisturizers:</strong> {feature_en} giving skin a soft touch and fragranced aura.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application only.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for daily body cleansing, hydration, and long-lasting freshness in 500ml.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Hobby</td></tr>
  <tr><th>Category</th><td>Body Care / Hobby Scented Hydrating Shower Gels 500ml</td></tr>
  <tr><th>Product Type</th><td>pH-Balanced {scent_en} Daily Refreshing Shower Gel (500ml)</td></tr>
  <tr><th>Volume/Weight</th><td>500 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Normal, Dry & Oily Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, hydrated, spotlessly clean body skin fragranced with {scent_en}</td></tr>
  <tr><th>Texture</th><td>Rich foaming clear gel fluid</td></tr>
  <tr><th>Fragrance</th><td>Refreshing long-lasting {scent_en} aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Gentle Plant Cleansers, {scent_en} Extracts, Hydrating Compounds</td></tr>
  <tr><th>Country of Origin</th><td>Turkey</td></tr>
  <tr><th>Manufacturer</th><td>Hobby Kozmetik Turkey</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of pH-Balanced Hydrolipid Barrier Maintenance & {scent_en} Fragrance Retention</h2>

<h3>What problem does this solve?</h3>
<p>Hobby Shower Gel resolves skin dryness caused by harsh soaps, daily sweat and pollution accumulation, and body odor.</p>

<h3>Why choose Hobby Shower Gel?</h3>
<p>pH-balanced mild surfactants remove skin dirt without stripping intercellular stratum corneum lipids while {scent_en} fragrance fixatives bind to skin layers.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a daily hydrating foaming shower gel from Hobby Turkey infused with {scent_en} notes in 500ml."),
        (f"What are the benefits of {scent_en} extracts and mild cleansers?", f"Mild cleansers cleanse skin without dryness, while {feature_en} and impart an all-day long-lasting fragrance."),
        ("Does it yield a rich lather and all-day freshness?", "Yes, produces a rich creamy lather and leaves body fragranced and invigorated."),
        ("What volume is contained in this bottle?", "500ml jumbo bottle."),
        ("How do I use it correctly?", "Wet body, apply gel onto loofah, lather, massage gently and rinse with water daily."),
        ("Is it safe for all skin types?", "Yes, pH-balanced formula safe for all body skin types."),
        ("Where is Hobby Shower Gel manufactured?", "In Turkey by Hobby Kozmetik Turkey."),
        ("How do I verify authenticity at Ekleel Abha?", "All Hobby products at Ekleel Abha are 100% original."),
        (f"What does {en_name} smell like?", f"Refreshing long-lasting {scent_en} scent."),
        ("Does it leave skin soft and hydrated?", "Yes, preserves skin moisture and silky softness."),
        ("Does 500ml last long for family use?", "Yes, jumbo bottle lasts months of regular family use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for men and women?", "Yes, suitable for the entire family."),
        ("How many times daily?", "Once or twice daily during showers."),
        ("Does it rinse off easily?", "Yes, rinses off smoothly with warm water without sticky residue."),
        ("Is Hobby a trusted Turkish brand?", "Yes, Hobby is a leading Turkish brand in shower and personal care."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help remove sweat odor?", "Yes, effectively cleanses and perfumes body skin."),
        ("Is it good post-workout?", "Yes, excellent for post-workout refreshing shower routines."),
        ("Does it leave a greasy film?", "No, cleanses completely clean without greasiness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is the bottle cap convenient?", "Yes, convenient flip-top cap for easy pouring."),
        ("Is it good for summer and winter?", "Yes, excellent for all seasons."),
        ("Is it a nice shower gift?", "Yes, excellent addition to personal care gift sets."),
        ("Does it replace harsh soaps?", "Yes, a much gentler hydrating alternative to harsh bar soaps.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Hobby",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. جل استحمام يومي مرطب بنفحات {scent_ar} لرغوة وانتعاش غني. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Daily hydrating shower gel with {scent_en} for rich lather and freshness. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1948():
    return _make_hobby_shower_gel(
        pid=1948, gtin="8690937011532",
        ar_name="جل استحمام معادن البحر من هوبي500 مل",
        en_name="Hobby Sea Minerals Shower Gel - 500ml",
        scent_ar="معادن البحر المنعشة", scent_en="Refreshing Sea Minerals",
        feature_ar="تنعش الجسد وتزوده بالطاقة الحيوية البحرية", feature_en="invigorates body with marine minerals energy and hydration",
        tags_ar=["هوبي", "جل_استحمام_معادن_البحر", "انتعاش_البحر", "جل_استحمام_هوبي", "إكليل_أبها"],
        tags_en=["hobby", "sea_minerals_gel", "shower_gel", "marine_freshness", "ekleel_abha"]
    )


def create_product_1949():
    return _make_hobby_shower_gel(
        pid=1949, gtin="8690937011556",
        ar_name="جل استحمام الأوركيد من هوبي500 مل",
        en_name="Hobby Orchid Shower Gel - 500ml",
        scent_ar="زهور الأوركيد الفاخرة", scent_en="Luxurious Orchid Flowers",
        feature_ar="تغلف الجسم بعبير الزهور الفاخر وتمنح النعومة", feature_en="envelops body in luxurious floral fragrance and softness",
        tags_ar=["هوبي", "جل_استحمام_الأوركيد", "عبير_الأوركيد", "جل_استحمام_هوبي", "إكليل_أبها"],
        tags_en=["hobby", "orchid_shower_gel", "floral_shower_gel", "hobby_gel", "ekleel_abha"]
    )


def create_product_1950():
    return _make_hobby_shower_gel(
        pid=1950, gtin="8690937003605",
        ar_name="جل استحمام فواكه منعشة من هوبي500 مل",
        en_name="Hobby Refreshing Fruits Shower Gel - 500ml",
        scent_ar="الفواكه المنعشة الاستوائية", scent_en="Refreshing Tropical Fruits",
        feature_ar="تمنح البشرة طاقة الفواكه والحيوية والانتعاش الفوار", feature_en="gives skin fruit vitality, energy, and sparkling freshness",
        tags_ar=["هوبي", "جل_استحمام_فواكه", "انتعاش_الفواكه", "جل_استحمام_هوبي", "إكليل_أبها"],
        tags_en=["hobby", "refreshing_fruits_gel", "fruit_shower_gel", "hobby_gel", "ekleel_abha"]
    )


def _make_whitening_cream_variant(pid, gtin, ar_name, en_name, brand_ar, brand_en, weight_g, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> كريم الجمال والتفتيح الفائق الأصيل المصمم خصيصاً لتفتيح وتوحيد لون بشرة الوجه والتخلص من البقع الداكنة والتصبغات. يرتكز هذا الكريم الفاخر ({en_name}) على خلاصات التفتيح الطبيعية المركزة، الفيتامينات المغذية للبشرة، والمركبات المهدئة المرممة لجلد الوجه.</p>
<p>يعمل كريم {brand_ar} لتبييض الوجه على تقليل إنتاج صبغة الميلانين في المناطق الداكنة، تفتيح النمش والبقع الناتجة عن الشمس وآثار البثور، وتغذية الوجه وترطيبه عمقاً، ليترك بشرتك ناعمة كالحرير، ناصعة البياض، موحدة اللون، ومشرقة من الأسابيع الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وتبييض ناصع لبشرة الوجه:</strong> يقلل البقع الداكنة والتصبغات والنمش بفاعلية.</li>
  <li><strong>توحيد لون الوجه وإعادة النضارة:</strong> يمنح الوجه إشراقة وتوهجاً متجانساً.</li>
  <li><strong>ترطيب عميق وتغذية بالفيتامينات:</strong> يقي البشرة من الجفاف والخشونة.</li>
  <li><strong>تركيبة خفيفة سهلة الامتصاص:</strong> تنفذ لطبقات الجلد دون ترك لزوجة أو دهنية.</li>
  <li><strong>مناسب للاستخدام اليومي الصباحي والمسائي:</strong> نتائج ملحوظة بالاستخدام المنتظم.</li>
  <li><strong>عبوة مدمجة سعة {weight_g} جم:</strong> حجم ممتاز للاستخدام اليومي والعناية الفائقة.</li>
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
  <tr><th>بلد المنشأ</th><td>تايلاند / آسيا</td></tr>
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
  <tr><th>Country of Origin</th><td>Thailand / Asia</td></tr>
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


def create_product_1951():
    return _make_whitening_cream_variant(
        pid=1951, gtin="8850252030049",
        ar_name="كريم تفتيح البشرة من ارشي 4 جم",
        en_name="Archie Skin Whitening Cream 4g",
        brand_ar="أرشي", brand_en="Archie", weight_g=4,
        tags_ar=["ارشي", "كريم_ارشي", "تفتيح_الوجه", "كريم_تبييض_صغير", "إكليل_أبها"],
        tags_en=["archie", "archie_cream", "skin_whitening", "compact_whitening", "ekleel_abha"]
    )


def create_product_1952():
    return _make_whitening_cream_variant(
        pid=1952, gtin="5842109854239",
        ar_name="كريم فائزة لتفتيح البشرة( 223190)  50 جم",
        en_name="Faiza Skin Whitening Cream (223190) 50g",
        brand_ar="فائزة", brand_en="Faiza", weight_g=50,
        tags_ar=["فائزة", "كريم_فائزة", "تفتيح_البشرة_فائزة", "تبييض_الوجه", "إكليل_أبها"],
        tags_en=["faiza", "faiza_cream", "faiza_whitening", "skin_lightening", "ekleel_abha"]
    )


print("Loaded all 5 Batch 47 builders complete")
