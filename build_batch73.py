import json, os

def create_product_2083():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول جسم الياسمين المخملي الورد الناعم من لوكس 700مل (Lux Velvet Jasmine & Soft Rose Body Wash - 700ml)</strong> سائل الاستحمام العطري الفاخر الأيقوني من لوكس (Lux) المصمم لمنح جسمك نظافة عميقة ورغوة مخملية غنية وعطراً فواحاً يدوم لـ 24 ساعة. يرتكز هذا الغسول الأصيل (Lux Velvet Jasmine 700ml) على زيوت Everscent العطرية الأساسية، خلاصات الياسمين المخملي والورد الناعم، والمركبات المرطبة لبشرة الجسم.</p>
<p>يعمل غسول لوكس بالياسمين والورد على تنظيف مسام الجسم وإزالة الشوائب، حماية الجلد من الجفاف وحفظ طراوته، وتغليف جسمك بنفحات الزهور الفواحة، ليترك بشرتك ناعمة كالحرير، مرطبة، ومعطرة بالنظافة والجاذبية طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عطر الياسمين والورد يدوم لـ 24 ساعة بزيت Everscent:</strong> يغلف الجسد بعبير الزهور الفاخر طوال اليوم.</li>
  <li><strong>تنظيف عميق ورغوة كريمية غنية:</strong> ينظف الجسم بلطف دون انتزاع الزيوت الطبيعية.</li>
  <li><strong>ترطيب وتنعيم لبشرة الجسم:</strong> يحفظ حاجز الترطيب الطبيعي للجلد.</li>
  <li><strong>تركيبة خفيفة متوازنة الحموضة (pH Balanced):</strong> مناسبة للاستخدام اليومي لجميع أنواع البشرة.</li>
  <li><strong>جودة لوكس (Lux) العالمية الشهيرة:</strong> العلامة الأولى في عطور وجمال الاستحمام.</li>
  <li><strong>عبوة اقتصادية ضخمة سعة 700 مل مزودة بضاغط:</strong> حجم ممتاز للاستخدام العائلي اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الجسم بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> اضغطي كمية مناسبة من سائل لوكس على ليفة الاستحمام أو الكفين وكوّني رغوة غنية.</li>
  <li><strong>الخطوة الثالثة:</strong> دلكي الجسم برفق بحركات دائرية ثم اشطفي جيداً بالماء (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت Everscent الأساسي وخلاصة الياسمين والورد:</strong> يثبتان جزيئات العطر الفواح على ألياف البشرة.</li>
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
  <li>لكل من يبحث عن غسول لوكس بالياسمين المخملي والورد 700 مل للانتعاش العطري والنظافة الحريرية.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لوكس (Lux)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / غسولات ومجموعات الاستحمام المعطرة من لوكس 700ml</td></tr>
  <tr><th>نوع المنتج</th><td>غسول جسم عطري مرطب بنفحات الياسمين المخملي والورد وزيت Everscent (700ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>700 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (العادية، الجافة والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، مرطب، ناصع النظافة ومفعم بعطر الزهور لـ 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>سائل جل عطري رغوي غني</td></tr>
  <tr><th>العطر</th><td>عطر الياسمين المخملي والورد الناعم لـ 24 ساعة</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت Everscent Essential Oil، خلاصة الياسمين والورد، منظفات لطيفة</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الإمارات</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever Group</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت Everscent وخلاصة الياسمين والورد في غسول لوكس (Lux Velvet Jasmine)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول لوكس مشكلة جفاف البشرة بعد الاستحمام بالصابون القاسي وتلاشي عطر النظافة سريعاً.</p>

<h3>لماذا تنجح تركيبة Lux Perfumed Body Wash؟</h3>
<p>لأن تقنية زيوت Everscent العطرية تفرز جزيئات العطر التي ترتبط بالجلد لتمنح ثباتاً لـ 24 ساعة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام اليومي بالماء الدافئ:</strong> ينظف المسام وينشط الدورة الدموية.<br>
2. <strong>استخدام ليفة ناعمة:</strong> يزيد تكوين الرغوة الغنية ويزيل الشوائب.<br>
3. <strong>الشطف الجيد بالماء:</strong> يضمن عدم بقاء أي ترسبات صابونية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "غسولات الجسم المعطرة تجفف البشرة."<br>
<strong>الحقيقة:</strong> غسول لوكس مدعم بمركبات مرطبة تحفظ التوازن المائي للجلد أثناء التنظيف.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخفض السورفاكتانتات اللطيفة التوتر السطحي للماء وتأطر الزيوت والأوساخ لينشطف بها الماء بسلاسة.</p>"""

    faqs = [
        ("ما هو غسول جسم الياسمين المخملي الورد الناعم من لوكس 700مل؟", "هو سائل استحمام عطري فاخر من لوكس بنفحات الياسمين والورد وزيت Everscent لثبات 24 ساعة (700 مل)."),
        ("ما هي فوائد خلاصة الياسمين والورد وزيت Everscent؟", "تنظف المنظفات اللطيفة البشرة دون جفاف، بينما يثبت زيت Everscent العطر لـ 24 ساعة."),
        ("هل يمنح رغوة غنية وعطراً يدوم لـ 24 ساعة؟", "نعم، مثبت سريرياً في توفير رغوة غنية وثبات عطري يدوم 24 ساعة."),
        ("ما حجم العبوة؟", "تأتي بعبوة ضخمة مزودة بضاغط بسعة 700 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الجسم، اضغطي كمية على الليفة وكوّني رغوة، دلكي برفق واشطفي بالماء يومياً."),
        ("هل هو آمن لجميع أنواع البشرة؟", "نعم، تركيبة متوازنة الحموضة آمنة لجميع أنواع بشرة الجسم."),
        ("أين صُنع غسول لوكس؟", "صُنع بواسطة مجموعة Unilever العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لوكس لدى إكليل أبها أصلية 100%."),
        ("ما رائحة غسول لوكس بالياسمين والورد؟", "عطر الياسمين المخملي والورد الناعم الفواح الأنيق."),
        ("هل يترك البشرة ناعمة ومرطبة؟", "نعم، يحافظ على رطوبة الجلد ونعومته الحريرية."),
        ("هل 700 مل تكفي للاستخدام العائلي؟", "نعم، عبوة ضخمة بضاغط تكفي لعدة أشهر من الاستخدام العائلي اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع أفراد الأسرة وخاصة محبي العطور الفاخرة."),
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
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Lux Velvet Jasmine & Soft Rose Body Wash - 700ml</strong> is an iconic luxury fragranced body wash from Lux designed to deliver deep cleansing, a rich velvety lather, and a 24-hour long-lasting scent. Built upon Everscent Essential Oil technology, seductive Velvet Jasmine & Soft Rose extracts, and body-moisturizing compounds.</p>
<p>Lux Body Wash cleanses body pores of dirt and excess sebum, guards skin against dryness, and wraps your body in captivating floral notes, leaving your skin touchably silky soft, hydrated, and fragranced with elegance all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>24-Hour Long-Lasting Fragrance with Everscent Oil:</strong> Coats body in a captivating Jasmine & Rose scent all day.</li>
  <li><strong>Deep Cleansing & Rich Creamy Lather:</strong> Cleanses body gently without stripping natural skin oils.</li>
  <li><strong>Body Skin Softening & Hydration:</strong> Preserves the skin's natural moisture barrier.</li>
  <li><strong>pH-Balanced Mild Formula:</strong> Suitable for daily use on all skin types.</li>
  <li><strong>Famous Quality of Lux Global:</strong> #1 recognized brand in perfumed bath care.</li>
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
  <li><strong>Everscent Essential Oil & Jasmine/Rose Extract:</strong> Bind fragrance molecules to skin layers delivering 24-hour freshness.</li>
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
  <li>Anyone seeking Lux Velvet Jasmine & Soft Rose Body Wash 700ml for 24-hour fragrance and silky clean skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lux</td></tr>
  <tr><th>Category</th><td>Body Care / Lux Perfumed Hydrating Body Washes 700ml</td></tr>
  <tr><th>Product Type</th><td>24H Perfumed Velvet Jasmine & Soft Rose Body Wash (700ml)</td></tr>
  <tr><th>Volume/Weight</th><td>700 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Normal, Dry & Oily Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, hydrated, spotlessly clean body skin fragranced with Jasmine & Rose for 24H</td></tr>
  <tr><th>Texture</th><td>Rich foaming fragranced clear gel fluid</td></tr>
  <tr><th>Fragrance</th><td>Captivating long-lasting Velvet Jasmine & Soft Rose scent for 24 hours</td></tr>
  <tr><th>Active Ingredients</th><td>Everscent Essential Oil, Jasmine & Rose Extract, Gentle Cleansers</td></tr>
  <tr><th>Country of Origin</th><td>KSA / UAE</td></tr>
  <tr><th>Manufacturer</th><td>Unilever Group</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Everscent Essential Oil Binding & 24-Hour Fragrance Retention</h2>

<h3>What problem does this solve?</h3>
<p>Lux Velvet Jasmine Body Wash resolves skin dryness caused by harsh soaps, daily sweat accumulation, and fading body fragrance.</p>

<h3>Why choose Lux Body Wash?</h3>
<p>Everscent Essential Oil technology binds perfume micro-droplets to skin keratin providing sustained 24-hour fragrance release.</p>"""

    en_faqs = [
        ("What is Lux Velvet Jasmine & Soft Rose Body Wash - 700ml?", "It is a luxury perfumed body wash from Lux with Velvet Jasmine, Soft Rose, and Everscent Oil for 24-hour fragrance (700ml)."),
        ("What are the benefits of Jasmine and Rose extracts and Everscent Oil?", "Gentle cleansers cleanse skin without dryness, while Everscent Oil binds floral fragrance for 24 hours."),
        ("Does it yield a rich lather and 24-hour fragrance?", "Yes, clinically proven to produce a rich lather and deliver 24-hour fragrance retention."),
        ("What volume is contained in this bottle?", "700ml jumbo pump bottle."),
        ("How do I use it correctly?", "Wet body, pump gel onto loofah, lather, massage gently and rinse with water daily."),
        ("Is it safe for all skin types?", "Yes, pH-balanced formula safe for all body skin types."),
        ("Where is Lux Body Wash manufactured?", "By Unilever Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All Lux products at Ekleel Abha are 100% original."),
        ("What scent does Lux Velvet Jasmine have?", "Captivating elegant Velvet Jasmine and Soft Rose fragrance."),
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
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2083",
        "sku": "EK-2083",
        "gtin": "6281006569805",
        "brand": "Lux",
        "ar": {
            "title": "غسول جسم الياسمين المخملي الورد الناعم من لوكس 700مل",
            "meta_title": "غسول جسم لوكس بالياسمين والورد 700مل | إكليل أبها",
            "meta_description": "اشتري غسول جسم الياسمين المخملي والورد الناعم من لوكس (700 مل). سائل استحمام بعبير الياسمين والورد الفواح لـ 24 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["لوكس", "غسول_لوكس_الياسمين", "الياسمين_المخملي", "سائل_استحمام_الورد", "إكليل_أبها"]
        },
        "en": {
            "title": "Lux Velvet Jasmine & Soft Rose Body Wash - 700ml",
            "meta_title": "Lux Velvet Jasmine Body Wash 700ml | Ekleel Abha",
            "meta_description": "Buy original Lux Velvet Jasmine & Soft Rose Body Wash (700ml). 24H perfumed Velvet Jasmine & Rose body wash. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["lux", "lux_velvet_jasmine", "jasmine_body_wash", "lux_rose_wash", "ekleel_abha"]
        }
    }


def _make_johnson_oil_gel_b73(pid, gtin, ar_name, en_name, ing_ar, ing_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> زيت الجل المرطب والمغذي الفاخر الأصيل من جونسون (Johnson's Baby) المصمم خصيصاً لحبس الترطيب داخل بشرة الأطفال والبالغين بمقدار 10 أضعاف مقارنة باللوشن العادي وتوفير نعومة وطراوة حريرية ممتدة لـ 24 ساعة دون أي لزوجة سائلة تسيل. يرتكز هذا الجل الأصيل ({en_name}) على خلاصات {ing_ar}، الزيوت المعدنية عالية النقاوة، والتركيبة الخالية 100% من الصبغات والبارابين والفثالات.</p>
<p>يعمل جل زيت جونسون على غلاف الجلد بحجاب ترطيب مكثف على البشرة المبللة بعد الاستحمام، القضاء على الجفاف والتشققات، وتنعيم بشرة الجسم والرضع، ليترك جسمك ناعماً كالحرير، مرطباً، ومفعماً بالنضارة والانتعاش من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حبس الترطيب بمقدار 10 أضعاف مقارنة باللوشن العادي:</strong> يمنح هالة رطوبة تدوم لـ 24 ساعة.</li>
  <li><strong>تغذية وتنعيم مكثف بـ {ing_ar}:</strong> يغذي البشرة الجافة ويمنع خشونة الجلد.</li>
  <li><strong>قوام جل متماسك غير مسكوب ولا يسيل:</strong> يسهل تطبيقه وتوزيعه بسلاسة على الجلد المبلل.</li>
  <li><strong>تركيبة ثبتت ملاءمتها لبشرة الأطفال (Clinically Proven Mildness):</strong> خالية من البارابين والصبغات.</li>
  <li><strong>مثالي للاستخدام بعد الاستحمام للأطفال والبالغين:</strong> يمنح الجسم توهجاً حريرياً ناصعاً.</li>
  <li><strong>عبوة مريحة سعة 200 مل:</strong> حجم ممتاز للاستخدام العائلي اليومي والتنقل.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسبة من جل زيت جونسون على بشرة الجسم الرطبة فوراً بعد الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي برفق بحركات دائرية حتى الامتصاص وحبس الماء ثم جففي بالمنشفة برفق (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصات {ing_ar} والزيوت النقية:</strong> تحفظ التوازن المائي للجلد وتمنح طراوة فائقة.</li>
  <li><strong>مكثفات الجل الطبية:</strong> تمنح الزيت قواماً متماسكاً يسهل التحكم به.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين واحتفظي به بعيداً عن أنف وفم الأطفال.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل أم ولكل من يبحث عن {ar_name} للترطيب المكثف وحبس الماء لـ 24 ساعة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جونسون للأطفال (Johnson's Baby)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم والأطفال / زيوت وجل زيت جونسون 200ml</td></tr>
  <tr><th>نوع المنتج</th><td>جل زيت مرطب مكثف بـ 10 أضعاف الترطيب بـ {ing_ar} (200ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>200 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (بشرة الرضع، الأطغال، والبالغين)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، مرطب 24 ساعة ومفعم بالتوهج الحريري</td></tr>
  <tr><th>الملمس</th><td>جل زيت شفاف متماسك ينساب بسلاسة على البشرة المبللة</td></tr>
  <tr><th>العطر</th><td>عطر جونسون اللطيف المنعش الأصلي</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصات {ing_ar}، زيوت معدنية نقية، مرطبات جلدية</td></tr>
  <tr><th>بلد المنشأ</th><td>إيطاليا / الولايات المتحدة (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Johnson & Johnson Consumer Inc.</td></tr>
  <tr><th>الفئة العمرية</th><td>حديثو الولادة والأطفال والبالغون (من عمر يوم)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد خلاصات {ing_ar} وتقنية حبس الترطيب بـ 10 أضعاف في جل زيت جونسون</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج جل زيت جونسون مشكلة انسكاب الزيوت السائلة الجافة، جفاف البشرة الشديد بعد الاستحمام، وتبخر الرطوبة فورياً.</p>

<h3>لماذا تنجح تركيبة Johnson's Baby Oil Gel؟</h3>
<p>لأن قوام الجل الزيتي يندمج بقطرات الماء على البشرة الرطبة مشكلاً عازلاً يحبس الرطوبة بـ 10 أضعاف اللوشن.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق فوراً على بشرة مبللة قبل التجفيف:</strong> يضمن أقصى حبس للماء.<br>
2. <strong>التجفيف بالمنشفة بطريقة الطبطبة الخفيفة:</strong> يحافظ على طبقة المرطب الحريرية.<br>
3. <strong>الاستخدام اليومي للرضع والكبار:</strong> يمنح نعومة واستقراراً لجلد الجسم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "زيوت الأطفال تسبب انسداد المسام ولزوجة ثقيلة."<br>
<strong>الحقيقة:</strong> جل زيت جونسون مصمم بزيت نقي مختبر درماتولوجياً لا يسبب انسداد المسام وينفذ بسلاسة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تحتجز الميكروليبيدات قطرات الماء السطحية وتمنع Transepidermal Water Loss (TEWL).</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو جل زيت مرطب مكثف بحبس الترطيب 10 أضعاف من جونسون بـ {ing_ar} للرضع والكبار (200 مل)."),
        (f"ما هي فوائد خلاصة {ing_ar} والتركيبة الجيلية؟", "تحبس الرطوبة بمقدار 10 أضعاف اللوشن، تغذي البشرة الجافة، وتمنع انسكاب الزيت."),
        ("هل يحبس الترطيب بـ 10 أضعاف ويرطب لـ 24 ساعة؟", "نعم، مثبت سريرياً في حبس الترطيب 10 أضعاف وتوفير نعومة 24 ساعة."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة سعة 200 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على بشرة مبللة فوراً بعد الاستحمام، دلكي برفق ثم جففي بالطبطبة يومياً."),
        ("هل هو خالٍ من البارابين والصبغات والفثالات؟", "نعم، 100% خالٍ من البارابين والصبغات ومختبر طبياً على بشرة الأطفال."),
        ("أين صُنع جل زيت جونسون؟", "صُنع بواسطة Johnson & Johnson العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات جونسون لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر جونسون اللطيف المنعش الأصلي بـ {ing_ar}."),
        ("هل يناسب حديثي الولادة والأطفال والبالغين؟", "نعم، آمن وممتاز لحديثي الولادة والأطفال والبالغين."),
        ("هل عبوة 200 مل مناسبة للاستخدام العائلي؟", "نعم، عبوة أنيقة تكفي لعدة أشهر من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل جونسون الماركة الأولى عالمياً في العناية بالأطفال؟", "نعم، Johnson's Baby الماركة رقم 1 العالمية والأكثر ثقة."),
        ("كم مرة يومياً؟", "مرة واحدة يومياً بعد الاستحمام وعند الحاجة."),
        ("هل يترك ملمساً حريرياً دون انسكاب سائل؟", "نعم، قوام جل متماسك ينساب بسهولة دون انسكاب سائل لزج."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع خشونة الجلد وتشققات الجسم؟", "نعم، ينعم الجلد ويحمي من خشونة الكوعين والركبتين والجسم."),
        ("هل يمنح توهجاً وجمالاً للبشرة؟", "نعم، يمنح البشرة توهجاً حريرياً ناصع النظافة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، مرطب جسم ممتاز جداً للنساء والرجال."),
        ("هل يناسب الصيف والشتاء؟", "نعم، ممتاز لجميع فصول السنة وخاصة بعد السباحة والاستحمام."),
        ("هل يصلح هدية ممتازة للأمهات والمواليد؟", "نعم، منتج عناية أساسي ومفيد جداً."),
        ("هل يعيد المظهر المشرق الناعم للجسم؟", "نعم، يمنح الجسد مظهراً ناعماً ومشرقاً."),
        ("هل تتوفر أنواع أخرى من جل زيت جونسون؟", "نعم، تتوفر خيارات متعددة لدى جونسون بـ إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic luxury hydrating oil gel from Johnson's Baby designed to lock in up to 10 times more moisture on wet skin than ordinary lotions, delivering touchable 24-hour silky softness without messy drips. Built upon natural {ing_en} extracts, high-purity mineral oil, and a 100% dye-free, paraben-free, phthalate-free formula.</p>
<p>Johnson's Baby Oil Gel locks in water on wet post-shower skin, eliminates dryness and flaking, and softens baby and adult skin, leaving your body touchably silky soft, deeply hydrated, and glowing from first touch.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Locks in 10x More Moisture Than Ordinary Lotions:</strong> Delivers continuous 24-hour hydration.</li>
  <li><strong>Intensive Nourishment with {ing_en}:</strong> Nourishes dry skin preventing roughness.</li>
  <li><strong>No-Mess Solid Gel Texture:</strong> Easy to apply smoothly over wet post-shower skin without dripping.</li>
  <li><strong>Clinically Proven Mildness for Baby Skin:</strong> Free from parabens, dyes, and phthalates.</li>
  <li><strong>Ideal Post-Shower Routine for Babies & Adults:</strong> Imparts a silky soft natural skin glow.</li>
  <li><strong>Convenient 200ml Flip-Cap Bottle:</strong> Excellent size for daily family bath routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of Johnson's oil gel onto wet body skin immediately after shower or bath.</li>
  <li><strong>Step 2:</strong> Massage gently in smooth circular motions to lock in moisture, then pat dry with a towel (use daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>{ing_en} Extracts & Pure Mineral Oil:</strong> Preserve skin moisture balance delivering extreme touchable softness.</li>
  <li><strong>Medical Gelling Agents:</strong> Give oil a controlled gel texture preventing messy liquid spills.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application.</li>
  <li>Avoid direct contact with eyes; keep out of reach of children's nose and mouth.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Mothers and anyone seeking {en_name} for 10x moisture locking and 24-hour body skin softness.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Johnson's Baby</td></tr>
  <tr><th>Category</th><td>Body & Baby Care / Johnson's Baby Oils & Gel Oils 200ml</td></tr>
  <tr><th>Product Type</th><td>10x Moisture Locking Hydrating Body Oil Gel with {ing_en} (200ml)</td></tr>
  <tr><th>Volume/Weight</th><td>200 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Newborns, Babies & Adults)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, radiant & non-dripping body skin</td></tr>
  <tr><th>Texture</th><td>Clear smooth non-messy gel oil gliding easily</td></tr>
  <tr><th>Fragrance</th><td>Gentle classic clean fresh Johnson's scent</td></tr>
  <tr><th>Active Ingredients</th><td>{ing_en} Extracts, Pure Mineral Oil, Skin Hydrators</td></tr>
  <tr><th>Country of Origin</th><td>Italy / USA</td></tr>
  <tr><th>Manufacturer</th><td>Johnson & Johnson Consumer Inc.</td></tr>
  <tr><th>Age Group</th><td>Newborns, Babies & Adults (Ages 0+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of 10x Transepidermal Moisture Locking & Gelled Mineral Matrix</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves liquid oil spills, post-shower skin dryness, and rapid moisture evaporation.</p>

<h3>Why choose Johnson's Baby Oil Gel?</h3>
<p>The gelled oil formula merges with water droplets on wet skin creating a barrier locking in 10x more moisture than lotions.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is an intensive 10x moisture locking oil gel from Johnson's with {ing_en} for babies and adults (200ml)."),
        (f"What are the benefits of {ing_en} extract and gel formula?", "Locks in 10x more moisture than lotions, nourishes dry skin, and prevents messy oil spills."),
        ("Does it lock in 10x more moisture and hydrate for 24 hours?", "Yes, clinically proven to lock in 10x more moisture and deliver 24-hour skin softness."),
        ("What volume is contained in this bottle?", "200ml flip-cap bottle."),
        ("How do I use it correctly?", "Apply to wet skin post-shower, massage gently, and pat dry with a towel daily."),
        ("Is it paraben-free, dye-free, and phthalate-free?", "Yes, 100% paraben-free, dye-free, and clinically tested on baby skin."),
        ("Where is Johnson's Baby Oil Gel manufactured?", "By Johnson & Johnson Consumer Inc."),
        ("How do I verify authenticity at Ekleel Abha?", "All Johnson's products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", f"Gentle classic fresh Johnson's fragrance with {ing_en}."),
        ("Is it suitable for newborns, babies, and adults?", "Yes, safe and mild for newborns, babies, and adults."),
        ("Does the 200ml bottle last long for family use?", "Yes, lasts months of regular daily post-shower use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Johnson's the #1 global baby care brand?", "Yes, Johnson's Baby is the world's most recognized #1 trusted brand."),
        ("How many times daily?", "Once daily post-shower or bath."),
        ("Does it glide smoothly without messy liquid spills?", "Yes, solid gel texture glides smoothly without dripping."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it prevent skin dryness and roughness?", "Yes, softens skin protecting elbows, knees, and body."),
        ("Does it impart skin glow and radiance?", "Yes, gives body skin a natural silky soft glow."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, an excellent body moisturizer for both men and women."),
        ("Is it good for all seasons?", "Yes, excellent for summer, winter, swimming, and post-shower routines."),
        ("Is it a nice gift for mothers and newborns?", "Yes, a practical essential baby shower and skincare gift."),
        ("Does it restore clean radiant body skin?", "Yes, gives body skin a healthy smooth radiant look."),
        ("Are other Johnson's oil gels available?", "Yes, various Johnson's Baby Oil Gel variants are available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Johnson's Baby",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. جل زيت جونسون بحبس الترطيب 10 أضعاف بـ {ing_ar} للرضع والكبار. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Johnson's 10x moisture locking baby oil gel with {ing_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2084():
    return _make_johnson_oil_gel_b73(
        pid=2084, gtin="3574661665795",
        ar_name="جل زيت الاطفال بخلاصة الصبار من جونسون 200مل",
        en_name="Johnson's Baby Oil Gel with Aloe Vera - 200ml",
        ing_ar="خلاصة الصبار المهدئة وفيتامين E", ing_en="Soothing Aloe Vera & Vitamin E",
        feature_ar="جل زيت ترطيب مكثف بخلاصة الصبار وفيتامين E بحبس الماء 10 أضعاف 200 مل", feature_en="intensive hydrating baby oil gel with aloe vera & vitamin E 200ml",
        tags_ar=["جونسون", "جل_زيت_الصبار_جونسون", "ترطيب_10_أضعاف", "عناية_الأطفال", "إكليل_أبها"],
        tags_en=["johnsons", "aloe_baby_oil_gel", "johnsons_oil_gel", "moisture_locking_gel", "ekleel_abha"]
    )


def create_product_2085():
    return _make_johnson_oil_gel_b73(
        pid=2085, gtin="381371020652",
        ar_name="جل زيت الاطفال بزبدة الشيا والكاكو من جونسون 200مل",
        en_name="Johnson's Baby Oil Gel with Shea & Cocoa Butter - 200ml",
        ing_ar="زبدة الشيا وزبدة الكاكاو المغذية", ing_en="Nourishing Shea & Cocoa Butter",
        feature_ar="جل زيت ترطيب وتغذية فائقة بزبدة الشيا والكاكاو بحبس الماء 10 أضعاف 200 مل", feature_en="nourishing shea & cocoa butter baby oil gel 200ml",
        tags_ar=["جونسون", "جل_زيت_الشيا_والكاكاو", "زبدة_الشيا_جونسون", "ترطيب_مكثف_للبشرة", "إكليل_أبها"],
        tags_en=["johnsons", "shea_cocoa_oil_gel", "johnsons_shea_gel", "10x_moisture_gel", "ekleel_abha"]
    )


def create_product_2086():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول وجه للبشرة الدهنية بالليمون من نيوتروجينا، 200 مل (Neutrogena Oil-Free Lemon Face Wash, 200ml)</strong> الجل المنظف المصفّي والمنشط الفاخر الأكثر توصية من نيتروجينا (Neutrogena) المصمم خصيصاً لتنظيف، تصفية، وموازنة إفرازات الدهون لبشرة الوجه الدهنية والمختلطة والمعرضة للبثور واللمعان دون تسبيب أي انسداد للمسام. يرتكز هذا الغسول الأصيل (Neutrogena Lemon Wash 200ml) على خلاصة الليمون الصافي المنشط (Pure Lemon Extract)، حمض الساليسليك المنقي (Salicylic Acid)، والتركيبة الخالية 100% من الزيوت (Oil-Free).</p>
<p>يعمل غسول الليمون من نيتروجينا على تنظيف مسام الوجه عمقاً من الدهون المتراكمة والشوائب، إزالة اللمعان الدهني، وتفتيح وتنقبة الوجه، ليترك بشرتك ناعمة كالحرير، ناصعة النظافة، مطهرة، ومفعمة بالانتعاش والحيوية من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف وتصفية فائقة للدهون واللمعان بخلاصة الليمون:</strong> يزيل الزيوت الزائدة بفاعلية وانتعاش.</li>
  <li><strong>تنقية المسام ومقاومة البثور بحمض الساليسليك:</strong> يذيب الكوميدونات والدهون المحتبسة بالمسام.</li>
  <li><strong>تركيبة خالية 100% من الزيوت (Oil-Free):</strong> لا تسبب أي انسداد للمسام (Non-Comedogenic).</li>
  <li><strong>منح الوجه مظهرًا صافياً ومات (Matte Finish):</strong> يقلل اللمعان الدهني طوال اليوم.</li>
  <li><strong>مختبر درماتولوجياً ومناسب للبشرة الدهنية والمختلطة:</strong> آمن للاستخدام اليومي.</li>
  <li><strong>عبوة سعة 200 مل مزودة بضاغط مريح:</strong> حجم ممتاز للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الوجه بالماء الدافئ.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسية من جل الليمون وكوّني رغوة ناعمة ودلكي الوجه برفق بحركات دائرية.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء الدافئ وجففي الوجه برفق (يُستعمل مرتين يومياً صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة الليمون وحمض الساليسليك:</strong> تنظيان الدهون المترسبة وتطهران المسام من البكتيريا.</li>
  <li><strong>المنظفات اللطيفة المائية:</strong> تنظف البشرة دون تجريد الزيوت الطبيعية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يملك بشرة دهنية أو مختلطة ويبحث عن غسول الليمون الخالي من الزيوت من نيتروجينا 200 مل لتنظيف وتصفية المسام.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>نيتروجينا (Neutrogena Oil-Free)</td></tr>
  <tr><th>الفئة</th><td>العناية بالوجه / غسولات نيتروجينا للبشرة الدهنية بالليمون 200ml</td></tr>
  <tr><th>نوع المنتج</th><td>جل غسول مصفٍ خالي من الزيوت بخلاصة الليمون وحمض الساليسليك (200ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>200 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الدهنية، المختلطة والمعرضة للبثور واللمعان</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، ناصع النظافة، مطهر وغير لامع بالدهون (Matte)</td></tr>
  <tr><th>الملمس</th><td>جل سائل شفاف ينقلب لرغوة ليمون منعشة غنية</td></tr>
  <tr><th>العطر</th><td>عطر الليمون الحمضي المنعش الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة الليمون الصافي، حمض الساليسليك، منظفات خالية من الزيوت</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا / الولايات المتحدة (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Johnson & Johnson Consumer Inc.</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد خلاصة الليمون وحمض الساليسليك في غسول نيتروجينا (Neutrogena Lemon Wash)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول نيتروجينا بالليمون مشكلة الإفرازات الدهنية الزائدة، لمعان الوجه المزعج، انسداد المسام بالرؤوس السوداء، وبهتان البشرة.</p>

<h3>لماذا تنجح تركيبة Neutrogena Oil-Free Lemon Wash؟</h3>
<p>لأن حمض الساليسليك يذيب الدهون المحتبسة بعمق المسام بينما تقضي خلاصة الليمون على اللمعان وتنعش البشرة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنظيف مرتين يومياً بالماء الدافئ:</strong> ينظف المسام من الأكسدة الدهنية.<br>
2. <strong>التكميل بمرطب نيتروجينا خالي من الزيوت:</strong> يحفظ الترطيب الداخلي دون انسداد.<br>
3. <strong>تجنب الفرك الشديد:</strong> يحافظ على نعومة واستقرار البشرة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "غسولات الليمون تسبب جفافاً واحمراراً كبيراً بالوجه."<br>
<strong>الحقيقة:</strong> غسول نيتروجينا بالليمون مصمم بتركيبة مائية متوازنة تنظف وتصفي الدهون دون تجفيف البشرة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يتغلغل حمض الساليسليك محب الدهون داخل المسام محللاً الزهم ومزصياً الشوائب السطحية.</p>"""

    faqs = [
        ("ما هو غسول وجه للبشرة الدهنية بالليمون من نيوتروجينا، 200 مل؟", "هو جل غسول مصفٍ خالي من الزيوت بخلاصة الليمون وحمض الساليسليك للبشرة الدهنية والمختلطة من نيتروجينا (200 مل)."),
        ("ما هي فوائد خلاصة الليمون وحمض الساليسليك للبشرة الدهنية؟", "تزيل الدهون واللمعان الزائد، تنظف المسام من الرؤوس السوداء، وتنعش وتصفي الوجه."),
        ("هل ينظف المسام ويقلل اللمعان بدون جفاف؟", "نعم، مثبت سريرياً في تنظيف المسام وتقليل اللمعان الدهني وتوفير مظهر مات صافٍ."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة مزودة بضاغط مريح سعة 200 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الوجه، ضعي كمية وكوّني رغوة، دلكي برفق واشطفي بالماء الدافئ مرتين يومياً."),
        ("هل هو خالٍ من الزيوت وغير مسبب للانسداد؟", "نعم، 100% خالي من الزيوت (Oil-Free) غير مسبب لانسداد المسام (Non-Comedogenic)."),
        ("أين صُنع غسول نيتروجينا بالليمون؟", "صُنع بواسطة Johnson & Johnson العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات نيتروجينا لدى إكليل أبها أصلية 100%."),
        ("ما رائحة غسول نيتروجينا بالليمون؟", "عطر الليمون الحمضي المنعش الفاخر."),
        ("هل يناسب البشرة الدهنية والمختلطة؟", "نعم، ممتاز للبشرة الدهنية، المختلطة والمعرضة للبثور واللمعان."),
        ("هل عبوة 200 مل بضاغط مريحة؟", "نعم، عبوة أنيقة بضاغط مريح جداً للاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل نيتروجينا الماركة الأولى الموصى بها للبشرة الدهنية؟", "نعم، Neutrogena الماركة الأكثر شهرة وموثوقية في تنظيف البشرة الدهنية."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل يزيل الزيوت والمكياج والأوساخ؟", "نعم، يزيل الزيوت الزائدة والمكياج اليومي والشوائب بفاعلية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في تقليل الرؤوس السوداء؟", "نعم، ينظف المسام بفضل حمض الساليسليك ويقلل الرؤوس السوداء."),
        ("هل يترك أثراً دهنياً؟", "لا، ينظف وينشطف بالكامل ليترك مظهراً صافياً ومات."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يفضل اتباع مرطب خفيف بعده؟", "نعم، يُفضل استخدام مرطب خفيف خالي من الزيوت بعد الغسل."),
        ("هل يناسب الصيف والشتاء؟", "نعم، ممتاز لجميع فصول السنة وخاصة في الصيف."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج عناية وتصفية أنيق ومفيد."),
        ("هل يعيد المظهر الصافي المشرق للبشرة؟", "نعم، يمنح الوجه مظهراً ناصع النقاء."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Neutrogena Oil-Free Lemon Face Wash, 200ml</strong> is an authentic luxury oil-control purifying facial cleanser from Neutrogena designed to clean, clarify, and balance sebum production for oily, combination, and acne-prone skin without clogging pores. Built upon Pure Lemon Extract, skin-purifying Salicylic Acid, and a 100% oil-free formula.</p>
<p>Neutrogena Oil-Free Lemon Cleanser deeply purifies facial pores of accumulated sebum and impurities, eliminates oily shine, and brightens facial skin, leaving your face touchably silky soft, spotlessly clean, refreshed, and radiant from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Superior Sebum & Shine Control with Pure Lemon Extract:</strong> Removes excess oil with refreshing clarity.</li>
  <li><strong>Pore Purifying & Blackhead Control with Salicylic Acid:</strong> Dissolves trapped sebum and comedones.</li>
  <li><strong>100% Oil-Free Non-Comedogenic Formula:</strong> Will not clog pores or trigger breakouts.</li>
  <li><strong>Delivers a Matte Oil-Free Finish:</strong> Reduces facial shine throughout the day.</li>
  <li><strong>Dermatologically Tested Safe Formula:</strong> Safe for daily morning and night cleansing.</li>
  <li><strong>Convenient 200ml Pump Dispenser Bottle:</strong> Excellent format for daily continuous care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet facial skin with warm water.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of lemon gel cleanser, work into a soft lather, and massage face in circular motions.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and pat face dry (use twice daily morning & night).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Lemon Extract & Salicylic Acid:</strong> Clear trapped sebum while purifying pores of bacteria.</li>
  <li><strong>Mild Aqueous Cleansers:</strong> Cleanse skin effectively without stripping natural hydration.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial skin application.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with oily or combination skin seeking Neutrogena Oil-Free Lemon Face Wash 200ml for pore purifying and oil control.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Neutrogena (Oil-Free)</td></tr>
  <tr><th>Category</th><td>Skincare / Neutrogena Oil-Free Lemon Cleansers 200ml</td></tr>
  <tr><th>Product Type</th><td>Oil-Free Salicylic Acid & Lemon Purifying Gel Cleanser (200ml)</td></tr>
  <tr><th>Volume/Weight</th><td>200 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Oily, Combination & Acne-Prone Skin</td></tr>
  <tr><th>Finish</th><td>Spotlessly clean, matte, 24H refreshed & oil-free silky soft face</td></tr>
  <tr><th>Texture</th><td>Clear liquid gel transforming into a refreshing lemon lather</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh citrus lemon scent</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Lemon Extract, Salicylic Acid, Oil-Free Cleansers</td></tr>
  <tr><th>Country of Origin</th><td>France / USA</td></tr>
  <tr><th>Manufacturer</th><td>Johnson & Johnson Consumer Inc.</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Salicylic Acid Lipophilic Penetration & Lemon Shine Reduction</h2>

<h3>What problem does this solve?</h3>
<p>Neutrogena Lemon Wash resolves excess sebum, facial oil shine, clogged blackhead pores, and dull skin texture.</p>

<h3>Why choose Neutrogena Oil-Free Lemon Wash?</h3>
<p>Salicylic acid dissolves oil inside pores while lemon extract purifies skin surface imparting a long-lasting matte finish.</p>"""

    en_faqs = [
        ("What is Neutrogena Oil-Free Lemon Face Wash, 200ml?", "It is an oil-free purifying gel cleanser from Neutrogena with Pure Lemon Extract and Salicylic Acid for oily and combination skin (200ml)."),
        ("What are the benefits of Lemon Extract and Salicylic Acid?", "Remove excess oil and shine, clear blackheads and pores, and refresh facial skin."),
        ("Does it clean pores and control oil shine without dryness?", "Yes, clinically proven to clean pores and reduce shine delivering a clear matte finish."),
        ("What volume is contained in this bottle?", "200ml pump dispenser bottle."),
        ("How do I use it correctly?", "Wet face, apply gel, lather, massage gently and rinse with warm water twice daily."),
        ("Is it oil-free and non-comedogenic?", "Yes, 100% oil-free and non-comedogenic formula that will not clog pores."),
        ("Where is Neutrogena Lemon Wash manufactured?", "By Johnson & Johnson Consumer Inc."),
        ("How do I verify authenticity at Ekleel Abha?", "All Neutrogena products at Ekleel Abha are 100% original."),
        ("What scent does Neutrogena Lemon Wash have?", "Luxurious fresh citrus lemon fragrance."),
        ("Is it suitable for oily and combination skin?", "Yes, excellent for oily, combination, and acne-prone skin."),
        ("Is the 200ml pump bottle convenient?", "Yes, sleek pump dispenser bottle ideal for daily care."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Neutrogena a trusted oil-control brand?", "Yes, Neutrogena is a world-famous trusted brand in oily skin cleansing."),
        ("How many times daily?", "Twice daily (morning and night)."),
        ("Does it remove excess oil and makeup?", "Yes, effectively cleanses excess oil, light makeup, and daily dirt."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help reduce blackheads?", "Yes, Salicylic acid cleanses pores reducing blackhead formation."),
        ("Does it leave a greasy film?", "No, cleanses completely clean leaving a matte oil-free finish."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is following with an oil-free moisturizer recommended?", "Yes, follow with a lightweight oil-free moisturizer after cleansing."),
        ("Is it good for all seasons?", "Yes, ideal oil-control cleansing for summer and winter."),
        ("Is it a nice skincare gift?", "Yes, a premier daily essential for facial care routines."),
        ("Does it restore clean radiant skin appearance?", "Yes, gives facial skin a clear healthy radiant look."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2086",
        "sku": "EK-2086",
        "gtin": "3574661073224",
        "brand": "Neutrogena",
        "ar": {
            "title": "غسول وجه للبشرة الدهنية بالليمون من نيوتروجينا، 200 مل",
            "meta_title": "غسول نيتروجينا بالليمون للبشرة الدهنية 200مل | إكليل أبها",
            "meta_description": "اشتري غسول وجه للبشرة الدهنية بالليمون من نيتروجينا (200 مل). جل مصفٍ خالي من الزيوت بالليمون وحمض الساليسليك لتقليل اللمعان. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["نيتروجينا", "غسول_نيتروجينا_بالليمون", "غسول_البشرة_الدهنية", "حمض_الساليسليك", "إكليل_أبها"]
        },
        "en": {
            "title": "Neutrogena Oil-Free Lemon Face Wash, 200ml",
            "meta_title": "Neutrogena Oil-Free Lemon Face Wash 200ml | Ekleel Abha",
            "meta_description": "Buy original Neutrogena Oil-Free Lemon Face Wash (200ml). Oil-free lemon & salicylic acid purifying gel cleanser. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["neutrogena", "lemon_face_wash", "oil_free_cleanser", "salicylic_acid_wash", "ekleel_abha"]
        }
    }


def create_product_2087():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول جسم عطر الصنوبر كوفيكس 500 مل (Cofix Pine Scent Body Wash 500ml)</strong> سائل الاستحمام العطري المنشط الفاخر الأصيل من كوفيكس (Cofix Care) المصمم لمنح جسمك نظافة فائقة ورغوة غنية وعطراً فواحاً بنفحات غابات الصنوبر المنعشة تدوم طوال اليوم. يرتكز هذا الغسول الأصيل (Cofix Pine Wash 500ml) على زيت الصنوبر الأساسي (Pine Essential Oil)، المركبات المطهرة للبشرة، والمكونات المرطبة لجسمك.</p>
<p>يعمل غسول كوفيكس بعطر الصنوبر على تنظيف مسام الجسم وإزالة الدهون والشوائب، تنشيط الدورة الدموية والجسم بنكهة الصنوبر البرية، وحماية الجلد من الجفاف، ليترك بشرتك ناعمة كالحرير، مرطبة، ومعطرة بالنظافة والانتعاش الفائق من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عطر الصنوبر البري المنشط والفواح طوال اليوم:</strong> يمنح الجسد طاقة وانتعاشاً استثنائياً.</li>
  <li><strong>تنظيف وتطهير فائق ورغوة كريمية غنية:</strong> ينظف الجسم بلطف دون انتزاع الزيوت الطبيعية.</li>
  <li><strong>ترطيب وتنعيم لبشرة الجسم:</strong> يحفظ حاجز الترطيب الطبيعي للجلد.</li>
  <li><strong>تركيبة خفيفة متوازنة الحموضة (pH Balanced):</strong> مناسبة للاستخدام اليومي لجميع أنواع البشرة.</li>
  <li><strong>جودة كوفيكس (Cofix Care) السعودية الشهيرة:</strong> العلامة الأولى في مستحضرات العناية بالجسم.</li>
  <li><strong>عبوة ضخمة اقتصادية سعة 500 مل مزودة بضاغط:</strong> حجم ممتاز للاستخدام العائلي اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الجسم بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> اضغطي كمية مناسبة من سائل كوفيكس على ليفة الاستحمام أو الكفين وكوّني رغوة غنية.</li>
  <li><strong>الخطوة الثالثة:</strong> دلكي الجسم برفق بحركات دائرية ثم اشطفي جيداً بالماء (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الصنوبر العطري وخلاصة النباتات:</strong> يمنحان عطراً فواحاً منشطاً للأعصاب والجسم.</li>
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
  <li>لكل من يبحث عن غسول كوفيكس بعطر الصنوبر 500 مل للانتعاش العطري والنظافة الفائقة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كوفيكس (Cofix Care)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / غسولات ومجموعات الاستحمام المعطرة من كوفيكس 500ml</td></tr>
  <tr><th>نوع المنتج</th><td>غسول جسم عطري منشط بنفحات عطر الصنوبر البري (500ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (العادية، الجافة والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، مرطب، ناصع النظافة ومفعم بعطر الصنوبر المنشط</td></tr>
  <tr><th>الملمس</th><td>سائل جل عطري رغوي غني ينشطف بالماء بسهولة</td></tr>
  <tr><th>العطر</th><td>عطر الصنوبر الجبلي المنعش الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت الصنوبر العطري، منظفات متوازنة pH، مركبات مرطبة</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية (KSA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Cofix Care Products</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت الصنوبر العطري في غسول كوفيكس (Cofix Pine Body Wash)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول كوفيكس بالصنوبر مشكلة جفاف البشرة بعد الاستحمام بالصابون القاسي، الإجهاد اليومي، وتلاشي عطر النظافة.</p>

<h3>لماذا تنجح تركيبة Cofix Pine Body Wash؟</h3>
<p>لأن الزيوت الأساسية للصنوبر تفرز جزيئات عطريّة منشطة ترتبط بالجلد وتمنح شعوراً بالحيوية والانتعاش الفواح.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام اليومي بالماء الدافئ:</strong> ينظف المسام وينشط الدورة الدموية.<br>
2. <strong>استخدام ليفة ناعمة:</strong> يزيد تكوين الرغوة الغنية ويزيل الشوائب.<br>
3. <strong>الشطف الجيد بالماء:</strong> يضمن عدم بقاء أي ترسبات صابونية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "عطور الصنوبر تسبب تحسس البشرة والجفاف."<br>
<strong>الحقيقة:</strong> غسول كوفيكس مدعم بمركبات مرطبة متوازنة الحموضة تحفظ التوازن المائي للجلد دون أي تحسس.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخفض المنظفات اللطيفة التوتر السطحي للماء وتزيل الشوائب بينما تحفز نفحات الصنوبر الجهاز العصبي الانتعاشي.</p>"""

    faqs = [
        ("ما هو غسول جسم عطر الصنوبر كوفيكس 500 مل؟", "هو سائل استحمام عطري منشط من كوفيكس بنفحات عطر الصنوبر الجبلي الفواح بحجم 500 مل."),
        ("ما هي فوائد زيت الصنوبر العطري والتركيبة متوازنة الحموضة؟", "تنظف وتطهر البشرة، تنشط الدورة الدموية، وتمنح عطراً فواحاً يدوم طوال اليوم."),
        ("هل يمنح رغوة غنية وعطراً منشطاً طوال اليوم؟", "نعم، مثبت سريرياً في توفير رغوة غنية وانتعاش عاطري منشط بالصنوبر."),
        ("ما حجم العبوة؟", "تأتي بعبوة ضخمة مزودة بضاغط سعة 500 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الجسم، اضغطي كمية على الليفة وكوّني رغوة، دلكي برفق واشطفي بالماء يومياً."),
        ("هل هو آمن لجميع أنواع البشرة؟", "نعم، تركيبة متوازنة الحموضة آمنة لجميع أنواع بشرة الجسم."),
        ("أين صُنع غسول كوفيكس بالصنوبر؟", "صُنع في المملكة العربية السعودية بواسطة Cofix Care Products."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كوفيكس لدى إكليل أبها أصلية 100%."),
        ("ما رائحة غسول كوفيكس بالصنوبر؟", "عطر الصنوبر الجبلي البري المنعش الأنيق."),
        ("هل يترك البشرة ناعمة ومرطبة؟", "نعم، يحافظ على رطوبة الجلد ونعومته الحريرية."),
        ("هل 500 مل تكفي للاستخدام العائلي؟", "نعم، عبوة ضخمة بضاغط تكفي لعدة أشهر من الاستخدام العائلي اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع أفراد الأسرة وخاصة الرجال ومحبي عطور الطبيعة."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً أثناء الاستحمام."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، ينشطف بالماء الدافئ بسهولة دون ترك أثر لزج."),
        ("هل كوفيكس علامة موثوقة في العناية بالجسم؟", "نعم، Cofix علامة سعودية رائدة وموثوقة جداً في العناية الشخصية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في إزالة رائحة العرق والتعرق؟", "نعم، ينظف بفاعلية ويعطر الجسم بنفحات صنوبر عاطرة."),
        ("هل يناسب الاستخدام بعد الرياضة؟", "نعم، ممتاز للانتعاش والنظافة والتنشيط بعد التمارين والرياضة."),
        ("هل يترك أثراً دهنياً؟", "لا، ينظف وينشطف بالكامل دون دهنية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل العبوة مزودة بضاغط مريح؟", "نعم، ضاغط مريح جداً يسهل استخدام الجل أثناء الاستحمام."),
        ("هل يناسب الشتاء والصيف؟", "نعم، ممتاز لجميع فصول السنة."),
        ("هل يصلح هدية ضمن مجموعة الاستحمام؟", "نعم، خيار ممتاز جداً في مجموعات العناية الشخصية."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Cofix Pine Scent Body Wash 500ml</strong> is an authentic luxury energizing fragranced body wash from Cofix Care designed to deliver deep cleansing, a rich foaming lather, and an invigorating fresh wild pine forest fragrance all day. Built upon Pine Essential Oil, skin-purifying cleansers, and body-moisturizing compounds.</p>
<p>Cofix Pine Scent Body Wash cleanses body pores of dirt and excess sebum, revitalizes skin and body energy with wild pine notes, and guards skin against dryness, leaving your body touchably silky soft, hydrated, and fragranced with fresh elegance from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Invigorating Wild Pine Forest Fragrance:</strong> Imparts vibrant energy and fresh fragrance all day long.</li>
  <li><strong>Superior Cleansing & Rich Foaming Lather:</strong> Cleanses body gently without stripping natural skin moisture.</li>
  <li><strong>Body Skin Softening & Hydration:</strong> Preserves the skin's natural moisture barrier.</li>
  <li><strong>pH-Balanced Mild Formula:</strong> Suitable for daily use on all skin types.</li>
  <li><strong>Famous Quality of Cofix Care Saudi Arabia:</strong> Leading trusted brand in body personal care.</li>
  <li><strong>Generous 500ml Value Pump Bottle:</strong> Excellent format for daily continuous family use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet body skin with warm water during shower.</li>
  <li><strong>Step 2:</strong> Pump a suitable amount of Cofix gel onto a shower loofah or hands and work into a rich lather.</li>
  <li><strong>Step 3:</strong> Massage body gently in circular motions, then rinse thoroughly with water (use daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pine Essential Oil & Plant Extracts:</strong> Deliver an invigorating aromatic fragrance stimulating senses and body.</li>
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
  <li>Anyone seeking Cofix Pine Scent Body Wash 500ml for invigorating daily shower freshness and clean skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Cofix Care</td></tr>
  <tr><th>Category</th><td>Body Care / Cofix Fragranced Hydrating Body Washes 500ml</td></tr>
  <tr><th>Product Type</th><td>Invigorating Wild Pine Scent Fragranced Body Wash (500ml)</td></tr>
  <tr><th>Volume/Weight</th><td>500 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Normal, Dry & Oily Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, hydrated, spotlessly clean body skin fragranced with Pine</td></tr>
  <tr><th>Texture</th><td>Rich foaming fragranced clear gel fluid</td></tr>
  <tr><th>Fragrance</th><td>Invigorating fresh mountain wild pine forest scent</td></tr>
  <tr><th>Active Ingredients</th><td>Pine Essential Oil, pH-Balanced Cleansers, Hydrating Agents</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia (KSA)</td></tr>
  <tr><th>Manufacturer</th><td>Cofix Care Products</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Pine Essential Oil Olfactory Stimulation & Epidermal Cleansing</h2>

<h3>What problem does this solve?</h3>
<p>Cofix Pine Body Wash resolves skin dryness caused by harsh soaps, daily fatigue, and fading body fragrance.</p>

<h3>Why choose Cofix Pine Body Wash?</h3>
<p>Pine essential oil releases invigorating aromatic molecules that stimulate senses while gentle cleansers purify skin.</p>"""

    en_faqs = [
        ("What is Cofix Pine Scent Body Wash 500ml?", "It is an invigorating fragranced body wash from Cofix with wild mountain pine scent (500ml)."),
        ("What are the benefits of Pine Essential Oil and pH-balanced formula?", "Cleanse and purify skin, stimulate body energy, and deliver a fresh pine fragrance all day."),
        ("Does it yield a rich lather and an invigorating pine scent?", "Yes, clinically proven to produce a rich lather and deliver an energizing pine fragrance."),
        ("What volume is contained in this bottle?", "500ml pump bottle."),
        ("How do I use it correctly?", "Wet body, pump gel onto loofah, lather, massage gently and rinse with water daily."),
        ("Is it safe for all skin types?", "Yes, pH-balanced formula safe for all body skin types."),
        ("Where is Cofix Pine Body Wash manufactured?", "In Saudi Arabia by Cofix Care Products."),
        ("How do I verify authenticity at Ekleel Abha?", "All Cofix products at Ekleel Abha are 100% original."),
        ("What scent does Cofix Pine Body Wash have?", "Invigorating fresh mountain wild pine forest fragrance."),
        ("Does it leave skin soft and hydrated?", "Yes, preserves skin moisture and silky softness."),
        ("Does 500ml last long for family use?", "Yes, pump bottle lasts months of regular family use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for men and women?", "Yes, suitable for the entire family especially men and nature scent lovers."),
        ("How many times daily?", "Once or twice daily during showers."),
        ("Does it rinse off easily?", "Yes, rinses off smoothly with warm water without sticky residue."),
        ("Is Cofix a trusted brand in Saudi Arabia?", "Yes, Cofix is a leading trusted brand in personal care in KSA."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help remove sweat odor?", "Yes, effectively cleanses and perfumes body skin."),
        ("Is it good post-workout?", "Yes, excellent for post-workout invigorating shower routines."),
        ("Does it leave a greasy film?", "No, cleanses completely clean without greasiness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is the pump bottle convenient?", "Yes, convenient pump dispenser for easy showering."),
        ("Is it good for summer and winter?", "Yes, excellent for all seasons."),
        ("Is it a nice shower gift?", "Yes, excellent addition to personal care gift sets."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2087",
        "sku": "EK-2087",
        "gtin": "697794487782",
        "brand": "Cofix",
        "ar": {
            "title": "غسول جسم عطر الصنوبر كوفيكس 500 مل",
            "meta_title": "غسول جسم كوفيكس بعطر الصنوبر 500مل | إكليل أبها",
            "meta_description": "اشتري غسول جسم عطر الصنوبر من كوفيكس (500 مل). سائل استحمام منشط بعطر الصنوبر البري الفواح لترطيب وتنظيف الجسم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كوفيكس", "غسول_الصنوبر_كوفيكس", "سائل_استحمام_الصنوبر", "غسول_منشط_للجسم", "إكليل_أبها"]
        },
        "en": {
            "title": "Cofix Pine Scent Body Wash 500ml",
            "meta_title": "Cofix Pine Scent Body Wash 500ml | Ekleel Abha",
            "meta_description": "Buy original Cofix Pine Scent Body Wash (500ml). Invigorating wild pine scent perfumed body wash. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["cofix", "pine_body_wash", "cofix_pine_wash", "invigorating_body_wash", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 73 builders complete")
