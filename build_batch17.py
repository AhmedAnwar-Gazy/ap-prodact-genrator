import json, os

def build_johnson_body_wash(prod_id, ingredient_ar, ingredient_en, benefit_ar, benefit_en, gtin, img_slug):
    title_ar = f"سائل استحمام جونسون {ingredient_ar} - 400 مل"
    title_en = f"Johnson's Body Wash with {ingredient_en} - 400ml"

    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>سائل استحمام جونسون {ingredient_ar} - 400 مل (Johnson's Body Wash with {ingredient_en} - 400ml)</strong> مستحضر الاستحمام المغذي الفاخر المصمم لإعادة النعومة، الترطيب العميق، والانتعاش المخملي لبشرة الجسم يومياً. يجمع هذا الغسول المتطور من جونسون (Johnson's Vita-Rich) بين خواص {ingredient_ar} المرطبة ورغوة جونسون الغنية، حيث ينظف البشرة بلطف دون تجريد رطوبتها الطبيعية.</p>
<p>يمتاز غسول جونسون بقوام كريمي ينفذ في مسام الجلد ليمنحكِ ترطيباً تدوم فاعليته حتى 24 ساعة، مع عطر زكي ومظهر ناعم كالحرير يزيد من إشراقة ونضارة بشرتكِ بعد كل حمام.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتغذية مكثفة لـ 24 ساعة:</strong> يزود بشرة الجسم بالمرطبات الطبيعية ليمنع الجفاف والتأثيرات البيئية.</li>
  <li><strong>مدعم بـ {ingredient_ar}:</strong> يمنح البشرة {benefit_ar} ونضارة مذهلة.</li>
  <li><strong>تنظيف لطيف ورغوة غنية:</strong> يزيل الأوساخ والدهون والعرق برفق شديد دون تجفيف الجلد.</li>
  <li><strong>عطر زكي يدوم طوال اليوم:</strong> يغلف جسمكِ بعبير فواح ومنعش يزيد من حس الثقة والانتعاش.</li>
  <li><strong>تركيبة متوازنة ومجربة جلدياً:</strong> آمنة ومناسبة لجميع أنواع البشرة والجسم يومياً.</li>
  <li><strong>عبوة وافرة سعة 400 مل:</strong> حجم ممتازة يضمن استخداماً ممتداً لجميع أفراد العائلة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل):</strong> بلي بشرة جسمكِ بالماء الفاتر أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية (التطبيق والفرك):</strong> اسكبي كمية مناسبة من سائل استحمام جونسون على ليفة الاستحمام المبللة وافركي لتوليد رغوة غنية.</li>
  <li><strong>الخطوة الثالثة (التدليك والشطف):</strong> دلكي كامل الجسم بحركات دائرية، ثم اشطفي جيداً بالماء الفاتر.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة {ingredient_ar}:</strong> تمنح ترطيباً وتغذية مخملية وتزيد نضارة البشرة.</li>
  <li><strong>جليسرين وعوامل تنظيف لطيفة:</strong> يحافظان على التوازن الهيدروليبيدي للجلد ويمنعان الجفاف.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على جسم الإنسان فقط.</li>
  <li>تجنبي ملامسة سائل الاستحمام المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تبحث عن سائل استحمام مغذٍ ومغرم بـ {ingredient_ar} لترطيب ونعومة 24 ساعة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جونسون (Johnson's)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / سوائل واستحمام الجسم المغذية</td></tr>
  <tr><th>نوع المنتج</th><td>سائل استحمام مغذٍ ومجدد للبشرة (400ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>400 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (الجافة، العادية، الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة، مخملية، مرطبة لـ 24 ساعة ومشرقة</td></tr>
  <tr><th>الملمس</th><td>سائل استحمام كريمي يرغي بكثافة ناعمة</td></tr>
  <tr><th>العطر</th><td>عطر {ingredient_ar} الاستوائي الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة {ingredient_ar}، جليسرين مرطب، زراعة دوار الشمس</td></tr>
  <tr><th>بلد المنشأ</th><td>إيطاليا / المملكة العربية السعودية (Kenvue)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Johnson & Johnson / Kenvue</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد {ingredient_ar} وسوائل استحمام جونسون</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج سائل استحمام جونسون مشكلة جفاف البشرة بعد الاستحمام، فقدان النعومة، والتهيج الناجم عن الصابون القاسي.</p>

<h3>لماذا تنجح تركيبة جونسون Vita-Rich؟</h3>
<p>لأنها تمزج الجليسرين المرطب مع خلاصة {ingredient_ar}، مما يشكل حجاب ترطيب يمنع تبخر الماء لـ 24 ساعة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام مع الليفة:</strong> اسكبي الغسول على ليفة مبللة لتوليد رغوة كثيفة تنظف المسام.<br>
2. <strong>الشطف بالماء الفاتر:</strong> تجنبي الماء شديد السخونة لحفظ زيوت البشرة.<br>
3. <strong>الترطيب المباشر:</strong> وضعي لوشن جونسون المرطب بعد الاستحمام مباشرة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "سوائل الاستحمام المعطرة تسبب جفاف البشرة."<br>
<strong>الحقيقة:</strong> سوائل جونسون Vita-Rich مصممة بمرطبات جليسرينية تحمي مرونة ونعومة الجلد.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتكامل الجزيئات المرطبة لخلاصة {ingredient_ar} مع طبقة الليبيدات السطحية بالجلد، مما يزيد مرونة الخلايا ويحافظ على الملمس المخملي.</p>"""

    faqs = [
        (f"ما هو سائل استحمام جونسون {ingredient_ar} - 400 مل؟", f"هو غسول جسم مغذٍ من مجموعة جونسون Vita-Rich ينظف ويرطب البشرة لـ 24 ساعة بخلاصة {ingredient_ar}."),
        (f"ما هي فوائد خلاصة {ingredient_ar} للبشرة؟", f"تمنح البشرة {benefit_ar}، ترطيباً مخملياً، وإشراقة طبيعية زكية."),
        ("هل يوفر ترطيباً تدوم فاعليته 24 ساعة؟", "نعم، مثبت سريرياً في حفظ رطوبة البشرة لمدة 24 ساعة متواصلة."),
        ("ما حجم العبوة؟", "تأتي بحجم وافر سعة 400 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اسكبي كمية مناسبة على ليفة مبللة، افركي لتوليد رغوة، دلكي الجسم ثم اشطفي بالماء."),
        ("هل يسبب جفاف البشرة بعد الاستحمام؟", "لا، يحتوي على جليسرين مرطب يمنع جفاف البشرة كلياً."),
        ("ما هو بلد صنع سائل استحمام جونسون؟", "صُنع بواسطة شركة جونسون آند جونسون (Johnson & Johnson) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات جونسون لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        (f"ما هي رائحة الغسول؟", f"يتميز برائحة {ingredient_ar} الزكية الفواحة التي تدوم على الجسم طوال اليوم."),
        ("هل يرغي بشكل ممتاز على الليفة؟", "نعم، يولد رغوة كريمية غنية تنظف وتطهر الجسم برفق."),
        ("هل يناسب جميع أنواع البشرة؟", "نعم، مناسب للبشرة العادية، الجافة، والحساسة."),
        ("هل يناسب جميع أفراد العائلة؟", "نعم، غسول عائلي آمن للأطفال والبالغين من سن 3 سنوات."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف داخل الحمام."),
        ("هل العبوة 400 مل اقتصادية؟", "نعم، عبوة وافرة تكفي لاستخدام عائلي مستمر لأشهر."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة أنيقة بغطاء ضاغط محكم يسهل التحكم بالكمية."),
        ("هل يزيل روائح العرق والشوائب؟", "نعم، ينظف المسام وينعش الجسم برائحة عطرة."),
        ("هل يساعد في تحسين مظهر البشرة الجافة؟", "نعم، الترطيب 24 ساعة يعيد المرونة والنضارة للجلد الجاف."),
        ("هل يناسب الاستخدام اليومي؟", "نعم، آمن وممتاز للاستخدام اليومي المتكرر."),
        ("هل يحتوي على مواد قاسية؟", "تركيبة مجربة ومطورة طبقاً لأعلى معايير السلامة والأمان."),
        ("هل يترك ملمساً لزجاً على الجلد؟", "لا، يشطف بسهولة ليترك ملمساً ناعماً ومخملياً دون لزوجة."),
        ("هل يناسب فصول الصيف والشتاء؟", "نعم، يحمي البشرة من حر الصيف وجفاف الشتاء."),
        ("هل يمكن استخدامه بدون ليفة؟", "نعم، يمكن توزيعه باليدين مباشرة على الجسم المبلل."),
        ("هل يعزز إشراقة ونضارة الجسم؟", "نعم، التغذية العميقة تعيد للبشرة إشراقتها الطبيعية."),
        ("هل هو الخيار المفضل عالمياً للاستحمام؟", "نعم، جونسون الماركة الأولى الموثوقة عالمياً للعناية بالبشرة."),
        ("هل يتوفر بنكهات أخرى في إكليل أبها؟", "نعم، تتوفر خيارات متعددة من سوائل استحمام جونسون Vita-Rich.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>Johnson's Body Wash with {ingredient_en} - 400ml</strong> is the premier moisturizing body wash engineered to bring silky softness, deep hydration, and continuous 24-hour skin nourishment. Part of the renowned Johnson's Vita-Rich range, it combines the skin-loving benefits of {ingredient_en} with a rich, velvety lather.</p>
<p>Cleansing gently without stripping skin's natural moisture barrier, Johnson's body wash leaves your body touchably soft, radiant, and enveloped in a long-lasting captivating fragrance after every shower.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>24-Hour Continuous Hydration:</strong> Feeds dermal layers with essential moisturizers to stop dry skin tightness.</li>
  <li><strong>Enriched with {ingredient_en}:</strong> Provides skin with {benefit_en} and healthy glow.</li>
  <li><strong>Gentle Cleansing & Rich Lather:</strong> Sweeps away dirt, sweat, and impurities without stripping natural lipids.</li>
  <li><strong>Long-Lasting Captivating Fragrance:</strong> Envelops your body in a delightful fresh scent throughout the day.</li>
  <li><strong>Dermatologically Tested Formula:</strong> Safe and hypoallergenic for all skin types and daily family bathing.</li>
  <li><strong>Generous 400ml Bottle:</strong> High-value bottle ensuring months of continuous daily family body care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet your body skin thoroughly with warm water during shower.</li>
  <li><strong>Step 2 (Lather):</strong> Pour a suitable amount of Johnson's Body Wash onto a wet loofah and rub to create a rich lather.</li>
  <li><strong>Step 3 (Massage & Rinse):</strong> Massage over wet skin in circular motions, then rinse thoroughly with warm water.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>{ingredient_en} Extract:</strong> Infuses skin with deep moisture, softness, and radiant nourishment.</li>
  <li><strong>Hydrating Glycerin:</strong> Retains moisture in skin layers to prevent dryness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external body cleansing application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a 24-hour hydrating, deliciously scented body wash enriched with {ingredient_en}.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Johnson's</td></tr>
  <tr><th>Category</th><td>Personal Care / Hydrating Body Washes & Shower Gels</td></tr>
  <tr><th>Product Type</th><td>24-Hour Hydrating Vita-Rich Body Wash (400ml)</td></tr>
  <tr><th>Volume/Weight</th><td>400 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Dry, Normal, Sensitive)</td></tr>
  <tr><th>Finish</th><td>Soft, silky, 24h hydrated & deliciously scented skin</td></tr>
  <tr><th>Texture</th><td>Creamy rich-lathering liquid body wash</td></tr>
  <tr><th>Fragrance</th><td>Captivating {ingredient_en} botanical fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>{ingredient_en} Extract, Hydrating Glycerin</td></tr>
  <tr><th>Country of Origin</th><td>Italy / Saudi Arabia (Kenvue)</td></tr>
  <tr><th>Manufacturer</th><td>Johnson & Johnson / Kenvue</td></tr>
  <tr><th>Age Group</th><td>All Ages (3+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Glycerin & {ingredient_en} Skin Nourishment</h2>

<h3>What problem does this solve?</h3>
<p>Johnson's Body Wash resolves post-shower dry tightness, rough skin texture, and moisture loss.</p>

<h3>Why choose Johnson's Vita-Rich?</h3>
<p>Glycerin humectants and {ingredient_en} extracts lock in skin moisture for 24 hours while cleansing without harsh soap dryness.</p>"""

    en_faqs = [
        (f"What is Johnson's Body Wash with {ingredient_en} - 400ml?", f"It is a moisturizing Vita-Rich body wash that cleanses and hydrates skin for 24 hours enriched with {ingredient_en}."),
        (f"What are the benefits of {ingredient_en} for skin?", f"Infuses dermal layers with {benefit_en}, velvet softness, and natural radiance."),
        ("Does it provide 24-hour hydration?", "Yes, clinically proven to lock in skin moisture for 24 continuous hours."),
        ("What volume is contained in this bottle?", "It comes in a generous 400ml bottle."),
        ("How do I use it correctly?", "Pour onto a wet loofah, rub to create a rich lather, massage over wet body, and rinse with water."),
        ("Does it dry out skin after showering?", "No, enriched with moisturizing glycerin to prevent skin dryness completely."),
        ("Where is Johnson's manufactured?", "It is produced by Johnson & Johnson / Kenvue under strict global standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Johnson's products at Ekleel Abha are 100% original from certified distributors."),
        (f"What scent does this body wash have?", f"Features a captivating {ingredient_en} fragrance that lingers all day."),
        ("Does it produce a rich lather?", "Yes, creates a creamy rich lather that cleanses gently."),
        ("Is it suitable for all skin types?", "Ideal for normal, dry, and sensitive skin types."),
        ("Is it safe for family daily use?", "Yes, safe for adults and children aged 3+."),
        ("How should I store the bottle?", "Store in a cool, dry place inside your shower area."),
        ("Is the 400ml bottle economical?", "Yes, high-capacity bottle provides months of daily family use."),
        ("Is the bottle cap leak-proof?", "Yes, features an ergonomic cap dispensing cleanser easily without mess."),
        ("Does it remove sweat and body odors?", "Yes, cleanses pores effectively leaving skin fresh and fragrant."),
        ("Does it improve dry skin texture?", "Yes, 24-hour hydration restores smoothness and elasticity to dry skin."),
        ("Can it be used daily?", "Yes, safe and recommended for daily showering."),
        ("Does it contain harsh soaps?", "Formulated and dermatologically tested to be gentle on skin."),
        ("Does it leave a sticky residue?", "No, rinses away easily leaving skin silky soft and clean."),
        ("Is it great year-round?", "Yes, protects skin against summer heat and winter dryness."),
        ("Can it be applied without a loofah?", "Yes, can be applied directly with hands onto wet skin."),
        ("Does it boost skin radiance?", "Yes, deep nourishment restores natural healthy skin glow."),
        ("Is Johnson's a world-trusted brand?", "Yes, the #1 globally trusted brand for gentle skincare."),
        ("Are other variants available at Ekleel Abha?", "Yes, Ekleel Abha offers various Johnson's Vita-Rich body washes.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "العناية الشخصية / سوائل واستحمام الجسم المغذية",
        "brand": "Johnson's",
        "ar": {
            "title": title_ar,
            "meta_title": f"سائل استحمام جونسون {ingredient_ar[:15]} 400مل | صيدلية إكليل أبها",
            "meta_description": f"اشتري {title_ar}. سائل استحمام مغذٍ بـ {ingredient_ar} لترطيب ونعومة 24 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["جونسون", "سائل_استحمام_جونسون", "ترطيب_24_ساعة", "إكليل_أبها"]
        },
        "en": {
            "title": title_en,
            "meta_title": f"Johnson's Body Wash {ingredient_en[:15]} 400ml | Ekleel Abha",
            "meta_description": f"Buy original {title_en}. 24-hour hydrating body wash with {ingredient_en}. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["johnsons", "body_wash", "24h_hydration", "ekleel_abha"]
        },
        "schema": {
            "brand": "Johnson's",
            "category": "Personal Care / Body Wash",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"{img_slug}.webp",
            "alt": title_en,
            "title": title_en
        }
    }

print("Loaded Batch 17 builders")
