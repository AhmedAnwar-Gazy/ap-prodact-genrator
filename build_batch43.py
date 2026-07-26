import json, os

def _make_jardin_sugar_scrub(pid, gtin, ar_name, en_name, ingredient_ar, ingredient_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> مقشر السكر المغربي الفاخر بحجم ضخم (600 جم) من جاردن دي أوليان المصمم لتقشير وترطيب وتفتيح وتنظيف بشرة الجسم بفاعلية فائقة. يرتكز هذا المقشر الملكي ({en_name}) على البلورات السكرية الطبيعية، زيت الأركان المغربي الأصيل، وخلاصة {ingredient_ar}.</p>
<p>يعمل مقشر جاردن دي أوليان على إذابة خلايا الجلد الميتة والتراكمات الجافة، تغذية الجلد بالأحماض الدهنية وفيتامين E، و{feature_ar}، ليترك جسمك ناعماً كالحرير، ناضراً، موحد اللون، ومعطراً برائحة {ingredient_ar} المغربية الفاخرة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تقشير لطيف بالبلورات السكرية الطبيعية:</strong> يزيل التراكمات الجافة والجلد الميت دون خدش.</li>
  <li><strong>تغذية وترطيب بزيت الأركان المغربي النقي:</strong> يحفظ مرونة الجلد ويمنع الجفاف.</li>
  <li><strong>تفتيح وتوحيد لون الجسم بـ {ingredient_ar}:</strong> {feature_ar} ويقضي على التصبغات.</li>
  <li><strong>قوام زيتاني سكري غني بالمغذيات:</strong> ينزلق بسلاسة ويترك طبقة ترطيب مخملية.</li>
  <li><strong>عبوة ضخمة سعة 600 جم:</strong> كمية وافرة تكفي لعدة أشهر من الاستخدام المنتظم.</li>
  <li><strong>صنع في المغرب بتركيبة السبا الأصيلة 100%:</strong> تراث مغربي فاخر في العناية بالبشرة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الجسم بالماء الدافئ أثناء الاستحمام لفتح المسام.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة ودلكي الجسم بحركات دائرية مع التركيز على المناطق الخشنة.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي بالماء الفاتر دون استخدام صابون بعدها (يُستعمل 1-2 مرة أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>البلورات السكرية وخلاصة {ingredient_ar}:</strong> تقشر التراكمات وتفتّح وتوحد لون الجلد.</li>
  <li><strong>زيت الأركان المغربي النقي:</strong> يغذي البشرة بالأحماض الدهنية الأساسية وفيتامين E.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم فقط (لا يُستعمل للوجه).</li>
  <li>تجنبي الاستخدام على الجروح والحروق.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لتقشير وترطيب وتفتيح بشرة الجسم 600 جم.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جاردن دي أوليان (Jardin d'Oléane)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / مقشرات السكر المغربية بـ {ingredient_ar} 600g</td></tr>
  <tr><th>نوع المنتج</th><td>مقشر سكر مغربي طبيعي بزيت الأركان وخلاصة {ingredient_ar} (600g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>600 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (الجافة والتالفة والمفتقرة للنضارة)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، موحد اللون، مرطب بزيت الأركان ومعطر بـ {ingredient_ar}</td></tr>
  <tr><th>الملمس</th><td>معجون سكري زيتاني مغذٍ غني بالزيوت</td></tr>
  <tr><th>العطر</th><td>عطر {ingredient_ar} المغربي الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>بلورات السكر، زيت الأركان المغربي، خلاصة {ingredient_ar}</td></tr>
  <tr><th>بلد المنشأ</th><td>المغرب (Morocco)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Jardin d'Oléane Morocco</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد مقشر السكر بـ {ingredient_ar} وزيت الأركان من جاردن دي أوليان</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج هذا المقشر مشكلة جفاف وخمول بشرة الجسم، تراكم خلايا الجلد الميتة، وتصبغات الكوعين والركبتين.</p>

<h3>لماذا تنجح تركيبة السكر والأركان و{ingredient_ar}؟</h3>
<p>لأن السكر يتقشر ميكانيكياً ولطفاً بينما يخترق زيت الأركان وخلاصة {ingredient_ar} لترطيب وتغذية وتفتيح البشرة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على جسم مبلل بالماء الدافئ:</strong> يسهل الانزلاق والتطبيق.<br>
2. <strong>عدم استخدام الصابون بعده:</strong> يحافظ على طبقة زيت الأركان المرطبة.<br>
3. <strong>الاستخدام 1-2 مرة أسبوعياً:</strong> يمنح نتائج نعومة وتفتيح مستمرة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مقشرات السكر تسبب تهيج البشرة الجافة."<br>
<strong>الحقيقة:</strong> وجود زيت الأركان النقي يمنع التهيج ويغذي البشرة الجافة عمقاً أثناء التقشير.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تذوب جزيئات السكر كروياً بالتدليك لتقشير الخلايا القرنية الميتة دون حك قاسٍ على الجلد.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو مقشر سكر مغربي فاخر من جاردن دي أوليان بزيت الأركان وخلاصة {ingredient_ar} بحجم 600 جم."),
        (f"ما هي فوائد زيت الأركان و{ingredient_ar}؟", f"يغذي زيت الأركان البشرة بالأحماض الدهنية وفيتامين E، بينما {feature_ar} وتوحد لون الجسم."),
        ("هل يزيل التصبغات والجلد الميت؟", "نعم، يزيل خلايا الجلد الميتة والتراكمات الجافة والتصبغات بكفاءة."),
        ("ما وزن العبوة؟", "تأتي بعبوة ضخمة بوزن 600 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "دلكي على جسم مبلل بالماء الدافئ، اشطفي بالماء الفاتر دون صابون بعده 1-2 مرة أسبوعياً."),
        ("هل هو أصلي صُنِع في المغرب؟", "نعم، صُنع في المغرب بواسطة Jardin d'Oléane Morocco."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات جاردن دي أوليان لدى إكليل أبها أصلية 100%."),
        ("هل يترك الجسم ناعماً بزيت الأركان؟", "نعم، يترك طبقة مرطبة ناعمة كالحرير من زيت الأركان."),
        (f"ما رائحة {ar_name}؟", f"عطر {ingredient_ar} المغربي الفاخر المميز."),
        ("هل يناسب جميع أنواع بشرة الجسم؟", "نعم، مناسب لجميع أنواع بشرة الجسم."),
        ("هل 600 جم تدوم طويلاً؟", "نعم، عبوة ضخمة تكفي لعدة أشهر من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف محكم الإغلاق."),
        ("هل يناسب الوجه؟", "مخصص لبشرة الجسم فقط ولا يُستعمل للوجه."),
        ("كم مرة أسبوعياً؟", "1-2 مرة أسبوعياً."),
        ("هل ينعم الكوعين والركبتين؟", "نعم، ينعم المرفقين والركبتين والمناطق الخشنة بفاعلية."),
        ("هل جاردن دي أوليان علامة مغربية رائدة؟", "نعم، من أشهر وأعرق علامات التجميل والسبا المغربي."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع تشقق وجفاف الشتاء؟", "نعم، يحمي البشرة تماماً من الجفاف الشتوي."),
        ("هل يناسب الاستخدام قبل التان؟", "نعم، يجهز البشرة لـ تان متجانس."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، البلورات تذوب وتنشطف بالماء بسهولة."),
        ("هل يناسب النساء والرجال؟", "مناسب للنساء والرجال من 16 سنة."),
        ("هل يصلح هدية فاخرة؟", "نعم، هدية فاخرة وممتازة جداً للعرايس والعناية الشخصية."),
        ("هل يغني عن استخدام مرطب بعده؟", "بفضل زيت الأركان النقي قد لا تحتاجين لمرطب إضافي."),
        ("هل يمنح توحيداً ونضارة؟", "نعم، يمنح نعومة وإشراقاً وتوحيداً تدريجياً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is a luxury Moroccan sugar body scrub in a jumbo 600g tub from Jardin d'Oléane formulated to exfoliate, hydrate, brighten, and cleanse body skin with superior efficacy. Built upon natural sugar crystals, pure authentic Moroccan Argan Oil, and {ingredient_en} extract.</p>
<p>Jardin d'Oléane Sugar Scrub dissolves dead skin cells and dry buildup, nourishes skin with fatty acids and Vitamin E, and {feature_en}, leaving your body touchably silky soft, radiant, even-toned, and fragranced with luxury Moroccan {ingredient_en} scent.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Gentle Exfoliation with Natural Sugar Crystals:</strong> Sloughs off dry buildup and dead skin without scratching.</li>
  <li><strong>Nourishment & Hydration with Pure Moroccan Argan Oil:</strong> Preserves skin elasticity and guards against dryness.</li>
  <li><strong>Body Skin Brightening & Tone Unification with {ingredient_en}:</strong> {feature_en} and targets dark spots.</li>
  <li><strong>Nutrient-Rich Oil-Sugar Texture:</strong> Glides smoothly leaving a velvety moisturizing layer.</li>
  <li><strong>Generous 600g Jumbo Tub:</strong> Abundant volume lasting months of regular use.</li>
  <li><strong>100% Made in Morocco Spa Formulation:</strong> Authentic Moroccan heritage in luxury skincare.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet body skin with warm water during shower to open pores.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount and massage in gentle circular motions focusing on rough areas.</li>
  <li><strong>Step 3:</strong> Rinse with warm water without using soap afterwards (use 1-2 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Sugar Crystals & {ingredient_en}:</strong> Exfoliate buildup while brightening and unifying skin tone.</li>
  <li><strong>Pure Moroccan Argan Oil:</strong> Nourishes skin with essential fatty acids and Vitamin E.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application only (do not use on face).</li>
  <li>Avoid using on wounds and burns.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for body exfoliation, hydration, and brightening with 600g spa formula.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Jardin d'Oléane</td></tr>
  <tr><th>Category</th><td>Body Care / Jardin d'Oléane Moroccan Argan Sugar Scrubs 600g</td></tr>
  <tr><th>Product Type</th><td>Natural Argan Oil & {ingredient_en} Sugar Exfoliating Scrub (600g)</td></tr>
  <tr><th>Volume/Weight</th><td>600 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Including Dry & Dull Skin)</td></tr>
  <tr><th>Finish</th><td>Silky smooth, oil-hydrated, even-toned & fragranced body skin</td></tr>
  <tr><th>Texture</th><td>Rich oil-infused sugar paste</td></tr>
  <tr><th>Fragrance</th><td>Luxury Moroccan {ingredient_en} scent</td></tr>
  <tr><th>Active Ingredients</th><td>Sugar Crystals, Pure Moroccan Argan Oil, {ingredient_en} Extract</td></tr>
  <tr><th>Country of Origin</th><td>Morocco</td></tr>
  <tr><th>Manufacturer</th><td>Jardin d'Oléane Morocco</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of {ingredient_en} Hydration & Argan Oil Lipid Barrier Protection</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves dull dry body skin, dead skin buildup, and body hyperpigmentation.</p>

<h3>Why choose Jardin d'Oléane Sugar Scrub?</h3>
<p>Sugar crystals dissolve spherical-wise on wet skin providing gentle mechanical exfoliation while pure Argan oil feeds deep epidermal layers.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a luxury Moroccan sugar scrub from Jardin d'Oléane with Argan Oil and {ingredient_en} in a jumbo 600g tub."),
        (f"What are the benefits of Argan Oil and {ingredient_en}?", f"Argan Oil nourishes with Vitamin E and omegas, while {feature_en} and unifies body tone."),
        ("Does it remove hyperpigmentation and dead skin?", "Yes, effectively removes dead skin cells and dry buildup from body skin."),
        ("What weight is contained in this tub?", "600g jumbo tub."),
        ("How do I use it correctly?", "Massage onto warm damp body skin, rinse with warm water without soap 1-2 times weekly."),
        ("Is it authentic Made in Morocco?", "Yes, proudly made in Morocco by Jardin d'Oléane Morocco."),
        ("How do I verify authenticity at Ekleel Abha?", "All Jardin d'Oléane products at Ekleel Abha are 100% original."),
        ("Does it leave skin soft with Argan Oil?", "Yes, leaves a silky soft moisturizing layer of pure Argan oil."),
        (f"What does {en_name} smell like?", f"Luxury signature Moroccan {ingredient_en} scent."),
        ("Is it suitable for all body skin types?", "Yes, suitable for all body skin types."),
        ("Does the 600g tub last long?", "Yes, jumbo tub lasts months of regular weekly use."),
        ("How should I store it?", "In a cool, dry place tightly closed."),
        ("Is it suitable for the face?", "Formulated for body skin only; do not use on face."),
        ("How many times weekly?", "1-2 times weekly for best results."),
        ("Does it soften elbows and knees?", "Yes, effectively softens elbows, knees, and rough spots."),
        ("Is Jardin d'Oléane a leading brand?", "Yes, a premier Moroccan spa and beauty brand."),
        ("Is the tub recyclable?", "Yes."),
        ("Does it prevent winter dryness?", "Yes, shields skin against winter dryness."),
        ("Is it good before self-tanning?", "Yes, prepares skin for a smooth self-tan application."),
        ("Does it rinse off easily?", "Yes, sugar crystals dissolve and rinse off smoothly."),
        ("Is it suitable for men and women?", "Suitable for men and women aged 16+."),
        ("Is it a luxury gift?", "Yes, luxurious gift for brides and personal care."),
        ("Does it eliminate post-shower lotion need?", "Pure Argan oil content often eliminates post-shower lotion need."),
        ("Does it give tone unification?", "Imparts softness, radiance, and progressive tone unification."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Jardin d'Oléane",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. مقشر سكر مغربي بزيت الأركان وخلاصة {ingredient_ar} بحجم 600 جم لتقشير وتفتيح وترطيب الجسم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Moroccan sugar scrub with Argan Oil & {ingredient_en} 600g for body exfoliation & hydration. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1927():
    return _make_jardin_sugar_scrub(
        pid=1927, gtin="745114422125",
        ar_name="مقشر السكر بزيت الأركان وجوز الهند من جاردن دي اوليان - 600جم",
        en_name="Jardin d'Oleane Sugar Scrub with Argan Oil and Coconut - 600g",
        ingredient_ar="جوز الهند المرطب المغذي", ingredient_en="Nourishing Coconut",
        feature_ar="تغذي وترطب وتمنح الجسم نعومة استوائية فائقة", feature_en="nourishes, hydrates, and imparts extreme tropical body softness",
        tags_ar=["جاردن_دي_اوليان", "مقشر_جوز_الهند", "زيت_الأركان", "تقشير_الجسم", "إكليل_أبها"],
        tags_en=["jardin_doleane", "coconut_scrub", "argan_oil", "body_scrub", "ekleel_abha"]
    )


def create_product_1928():
    return _make_jardin_sugar_scrub(
        pid=1928, gtin="745114422552",
        ar_name="مقشر السكر النيلة الزرقاء من جاردن دي اوليان - 600جم",
        en_name="Jardin d'Oleane Blue Nila Sugar Scrub - 600g",
        ingredient_ar="النيلة الزرقاء المغربية الأصيلة", ingredient_en="Authentic Moroccan Blue Nila",
        feature_ar="تفتّح التصبغات الداكنة وتمنح الجسم بياضاً ملكياً ناصعاً", feature_en="brightens dark hyperpigmentation and imparts a royal bright white body glow",
        tags_ar=["جاردن_دي_اوليان", "مقشر_النيلة_الزرقاء", "تفتيح_النيلة", "زيت_الأركان", "إكليل_أبها"],
        tags_en=["jardin_doleane", "blue_nila_scrub", "nila_brightening", "argan_oil", "ekleel_abha"]
    )


def _make_moroccan_black_soap(pid, gtin, ar_name, en_name, ingredient_ar, ingredient_en, benefit_ar, benefit_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> الصابون البلدي المغربي الفاخر الأيقوني بحجم ضخم (500 جم) المصنوع بتركيبة الحمام المغربي الأصيلة لتنظيف وتطهير وتقشير وتفتيح بشرة الجسم بكفاءة ملكية. يرتكز هذا الصابون البلدي الأصيل ({en_name}) على زيت الزيتون الأسود الطبيعي (Black Olive Oil)، خلاصة {ingredient_ar}، والركائز المغذية للبشرة.</p>
<p>يعمل الصابون البلدي المغربي على تلين خلايا الجلد الميتة والتراكمات الجافة، تنظيف الفروة والمسام عمقاً، وإزالة السموم من الجسم مع {benefit_ar}، ليترك جسمك ناعماً كالحرير، ناصع النظافة، موحد اللون، وجاهزاً للتقشير المثالي بالليفة المغربية.</p>

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
  <li><strong>خلاصة {ingredient_ar}:</strong> {benefit_ar} وتمنح الجسم عطراً ونقاءً ملكياً.</li>
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
  <tr><th>نوع المنتج</th><td>صابون بلدي مغربي طبيعي بزيت الزيتون وخلاصة {ingredient_ar} (500g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (بما في ذلك البشرة الجافة والمفتقرة للنضارة)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، ناصع النظافة، موحد اللون وجاهز للتقشير المغربي</td></tr>
  <tr><th>الملمس</th><td>معجون صابوني أسود/داكن ناعم دسم ينزلق برفق</td></tr>
  <tr><th>العطر</th><td>عطر {ingredient_ar} والزيتون المغربي الأصيل</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت زيتون أسود، خلاصة {ingredient_ar}، بوتاسيوم هيدروكسيد زيتي</td></tr>
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
<p>The <strong>{en_name}</strong> is an iconic luxury Moroccan black soap (Beldi Soap) in a jumbo 500g tub formulated with authentic Moroccan hammam traditions to cleanse, detoxify, soften, and brighten body skin with royal efficacy. Formulated with natural Black Olive Oil, {ingredient_en} extract, and nourishing skin bases.</p>
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
  <li><strong>{ingredient_en} Extract:</strong> {benefit_en} giving body skin royal purity and scent.</li>
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
  <tr><th>Active Ingredients</th><td>Black Olive Oil, {ingredient_en} Extract, Saponified Potassium Olivate</td></tr>
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


def create_product_1929():
    return _make_moroccan_black_soap(
        pid=1929, gtin="701197409262",
        ar_name="الصابون البلدي المغربي  بزيت الزيتون500جم",
        en_name="Moroccan Black Soap with Olive Oil - 500g",
        ingredient_ar="زيت الزيتون النقي المعصر", ingredient_en="Pure Pressed Olive Oil",
        benefit_ar="تغذي وتنعيم وتنعش طبقات الجلد بعمق", benefit_en="deeply nourishes, softens, and refreshes skin layers",
        tags_ar=["الصابون_البلدي", "زيت_الزيتون", "صابون_مغربي", "تنظيف_الجسم", "إكليل_أبها"],
        tags_en=["moroccan_black_soap", "olive_oil_soap", "beldi_soap", "body_cleansing", "ekleel_abha"]
    )


def create_product_1930():
    return _make_moroccan_black_soap(
        pid=1930, gtin="745114421586",
        ar_name="الصابون البلدي المغربي النيلة الزرقاء 500جم",
        en_name="Moroccan Black Soap with Blue Nila - 500g",
        ingredient_ar="مسحوق النيلة الزرقاء المغربية", ingredient_en="Moroccan Blue Nila Powder",
        benefit_ar="تفتّح التصبغات الداكنة وتمنح الجسم بياضاً ناصعاً وتوحيداً للون", benefit_en="brightens dark hyperpigmentation and imparts a bright white even body glow",
        tags_ar=["الصابون_البلدي", "النيلة_الزرقاء", "تفتيح_الجسم", "صابون_مغربي", "إكليل_أبها"],
        tags_en=["moroccan_black_soap", "blue_nila_soap", "body_brightening", "beldi_soap", "ekleel_abha"]
    )


def create_product_1931():
    return _make_moroccan_black_soap(
        pid=1931, gtin="745178721097",
        ar_name="الصابون البلدي المغربي بالعكر الفاسي 500جم",
        en_name="Moroccan Black Soap with Aker Fassi - 500g",
        ingredient_ar="مسحوق العكر الفاسي المغربي", ingredient_en="Moroccan Aker Fassi Powder",
        benefit_ar="تمنح الجسم توريداً وردياً ناعماً ونضارة وإشراقاً ملكياً", benefit_en="imparts a soft rosy royal blush, radiance, and body glow",
        tags_ar=["الصابون_البلدي", "العكر_الفاسي", "توريد_الجسم", "صابون_مغربي", "إكليل_أبها"],
        tags_en=["moroccan_black_soap", "aker_fassi_soap", "rosy_body_blush", "beldi_soap", "ekleel_abha"]
    )


print("Loaded all 5 Batch 43 builders complete")
