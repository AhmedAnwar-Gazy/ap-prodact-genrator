import json, os

def create_product_1749():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>زيت فيتامين E النقي للبشرة والوجه من سندوشاين (Sundoshine Vitamin E Oil for Skin and Face - 75ml)</strong> الإليكسير الذهبي والمغذي الفاخر المصمم لإعادة الشباب والنضارة الفائقة للبشرة المجهدة والجافة. يعتمد هذا الزيت على تركيز عالٍ ومكثف من فيتامين E (مضاد الأكسدة الأول عالمياً)، حيث يتغلغل في الطبقات العميقة للجلد ليحميه من أعراض الشيخوخة المبكرة والتجاعيد والهالات السوداء.</p>
<p>يمنح زيت سندوشاين ترطيباً عميقاً يعالج التشققات والبقع الداكنة وآثار ندبات الجروح والحروق، ويساعد في استعادة مرونة الجلد وإكسابه ملمساً مخملياً مشرقاً ومفعماً بالحيوية.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>مضاد أكسدة قوي ومكثف:</strong> يحمي خلايا الوجه والجسم من التلف البيئي والجذور الحرة.</li>
  <li><strong>ترطيب وترميم البشرة الجافة:</strong> يعالج تشققات الجلد والتصفيات السطحية ويعيد للمصل مرونته.</li>
  <li><strong>تقليل التصبغات وآثار الندبات:</strong> يساعد في تفتيح الهالات السوداء تحت العين وتقليل آثار الندبات القديمة.</li>
  <li><strong>مكافحة علامات الشيخوخة:</strong> يحد من ظهور الخطوط الدقيقة والتجاعيد ويعزز إنتاج الكولاجين.</li>
  <li><strong>مستحضر متعدد الاستخدامات:</strong> ممتاز للوجه، الرقبة، الأظافر، والجسم بأمان.</li>
  <li><strong>عبوة زجاجية بحجم 75 مل:</strong> تكفي لعناية مكثفة ومستمرة لعدة أشهر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> اغسلي بشرة الوجه أو المنطقة المطلوبة بالماء الفاتر وجففيها بلطف.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي بضع قطرات من زيت فيتامين E على كف اليد.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي الزيت بحركات دائرية خفيفة حتى يتم امتصاصه كاملاً (يُفضل قبل النوم).</li>
  <li><strong>الخطوة الرابعة (الخلط):</strong> يمكن دمج قطرات منه مع كريمكِ المرطب المفصل لزيادة فاعليته.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>فيتامين E النقي (Tocopheryl Acetate):</strong> مضاد الأكسدة الأقوى لحماية الخلايا وترميم الأنسجة.</li>
  <li><strong>زيوت ناقلة طبيعية خفيفة:</strong> تضمن سرعة امتصاص الزيت دون سد المسام.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي فقط.</li>
  <li>تجنبي ملامسة الزيت المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من جفاف البشرة الشديد، الهالات السوداء، وآثار التصبغات أو الخطوط الدقيقة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سندوشاين (Sundoshine)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / الزيوت المغذية والمرطبة</td></tr>
  <tr><th>نوع المنتج</th><td>زيت فيتامين E النقي للبشرة والوجه (75ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>75 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (خاصة الجافة والمجهدة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة رطبة، مشرقة، خالية من الجفاف والخطوط</td></tr>
  <tr><th>الملمس</th><td>زيت ذهبي ناعم سريع الامتصاص</td></tr>
  <tr><th>العطر</th><td>عطر طبيعي خفيف عديم الرائحة قريباً</td></tr>
  <tr><th>المكونات النشطة</th><td>فيتامين E النقي، زيوت مرطبة طبيعية</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين / المملكة العربية السعودية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Sundoshine Skincare Labs</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 15 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت فيتامين E ومكافحة الأكسدة (Sundoshine)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج زيت فيتامين E من سندوشاين مشكلة جفاف وشحوب الوجه، التصبغات تحت العين، وآثار التمدد والندبات السطحية.</p>

<h3>لماذا يحدث الجفاف والشيخوخة؟</h3>
<p>تتلف أكسدة أشعة الشمس والجذور الحرة غشاء خلايا الجلد، فتفقد البشرة الكولاجين وترطبها الداخلي فتظهر الخطوط والبقع.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطريق قبل النوم:</strong> وضعي قطرات من الزيت ليلاً لاستفادة مضاعفة أثناء التجدد الخلوي.<br>
2. <strong>الدمج مع المرطب:</strong> اخلطي قطرة مع كريم النهار لزيادة الحماية من الأكسدة.<br>
3. <strong>العناية بالأظافر:</strong> دلكي الزيت حول الجلد المحيط بالأظافر لمنع التشقق.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "زيت فيتامين E يسد المسام دائماً."<br>
<strong>الحقيقة:</strong> الاستخدام المعتدل بضع قطرات يمتصه الجلد بسرعة ويزوده بمضادات الأكسدة دون سد المسام.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>ينفذ فيتامين E (التوكوفيرول) داخل جدران الليبيدات في الخلايا، حيث يبطل فاعلية الجذور الحرة الحرة الناتجة عن الأشعة فوق البنفسجية ويحمي الكولاجين من التحلل.</p>"""

    faqs = [
        ("ما هو زيت فيتامين E من سندوشاين 75 مل؟", "هو زيت مغذي ومكثف للبشرة والوجه غني بفيتامين E لحماية الخلايا وترميم الجفاف وتقليل الندبات والهالات."),
        ("ما هي فوائد فيتامين E للبشرة؟", "يحمي من الأكسدة، يرطب الجفاف، يقلل الخطوط الدقيقة، ويفتّح الهالات والتصبغات."),
        ("هل يمكن استخدامه للوجه والجسم معاً؟", "نعم، آمن وممتاز للوجه، الرقبة، الأيدي، والجسم."),
        ("ما حجم العبوة؟", "تأتي العبوة بحجم 75 مل."),
        ("هل يساعد في تفتيح الهالات السوداء؟", "نعم، مسح قطرة خفيفة ليلاً يساعد في تفتيح وترطيب منطقة تحت العينين."),
        ("هل يناسب البشرة الجافة؟", "ممتاز جداً للبشرة الجافة والمجهدة."),
        ("هل يترك ملمساً ثقيلاً؟", "يمتصه الجلد بمرونة عند استخدام بضع قطرات خفيفة."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي قطرات على بشرة نظيفة ودلكي بلطف قبل النوم."),
        ("هل يمكن خلطه مع كريمات الترطيب؟", "نعم، ممتاز لدمج قطرة منه مع كريمكِ المفصل."),
        ("ما هو بلد صنع زيت سندوشاين؟", "تم تصنيعه وفق أعلى معايير الجودة."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع المستحضرات لدى إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يساعد في تقليل آثار الندبات والجروح؟", "نعم، يسرع التئام وترميم الأنسجة الجلدية."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب لكلا الجنسين."),
        ("هل يناسب الأطفال؟", "مناسب للمراهقين والبالغين من 15 سنة فما فوق."),
        ("هل يمنع تشقق الشفاه والأظافر؟", "نعم، يغذي الأظافر الشفاه ويمنع تشققها."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن حرارة الشمس."),
        ("هل يساعد في الوقاية من التجاعيد؟", "نعم، يحمي الكولاجين ويحد من ظهور الخطوط الدقيقة."),
        ("هل يناسب البشرة الدهنية؟", "تُستخدم قطرة خفيفة جداً ليلاً فقط."),
        ("هل العبوة زجاجية؟", "نعم، تحفظ نقاء الزيت من التأكسد."),
        ("هل يمكن استخدامه للشعر؟", "يمكن مسح قطرات منه على أطراف الشعر المتقصفة."),
        ("هل يحتوي على معطرات قاسية؟", "خالي من العطور القاسية والمواد المتهيجة."),
        ("كم تدوم فاعلية العبوة؟", "تكفي العبوة 75 مل لأشهر من الاستخدام المنتظم."),
        ("هل يمنح تفتيحاً للبشرة؟", "نعم، يحسن إشراقة وتجانس لون البشرة."),
        ("هل يلزم غسله بالماء؟", "لا، يترك على البشرة للامتصاص الكامل."),
        ("هل يمنع جفاف الشتاء؟", "نعم، يحمي البشرة من التقشر وجفاف الشتاء.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Sundoshine Vitamin E Oil for Skin and Face (75ml)</strong> is a luxurious nutrient-rich elixir engineered to restore radiance, elasticity, and deep hydration to dry or stressed skin. Featuring a concentrated dose of Vitamin E—the world's premier antioxidant—it penetrates deep skin layers to shield against environmental aging, fine lines, and under-eye dark circles.</p>
<p>Sundoshine Vitamin E Oil heals skin flaking, fades dark spots and scar marks, and boosts collagen health, leaving your complexion velvety smooth and naturally luminous.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intensive Antioxidant Shield:</strong> Protects face and body skin cells from free radical damage.</li>
  <li><strong>Deep Hydration & Skin Repair:</strong> Treats skin chapping and dryness, restoring dermal elasticity.</li>
  <li><strong>Fades Scars & Dark Circles:</strong> Lightens under-eye circles and minimizes the appearance of scar marks.</li>
  <li><strong>Anti-Aging Support:</strong> Reduces visible fine lines and supports natural collagen synthesis.</li>
  <li><strong>Versatile Application:</strong> Safe for facial skin, neck, hands, nails, and body care.</li>
  <li><strong>Generous 75ml Sealed Bottle:</strong> Provides months of ongoing nutrient-rich skin care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse targeted face or body skin with warm water and gently dry.</li>
  <li><strong>Step 2 (Dispense):</strong> Dispense a few drops of Sundoshine Vitamin E Oil onto palms.</li>
  <li><strong>Step 3 (Massage):</strong> Massage gently in circular motions until fully absorbed (ideally before sleep).</li>
  <li><strong>Step 4 (Blend):</strong> Mix a drop with your favorite moisturizer to boost hydrating efficacy.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Vitamin E (Tocopheryl Acetate):</strong> Potent antioxidant protecting dermal cells and repairing tissue.</li>
  <li><strong>Light Carrier Oils:</strong> Facilitate rapid skin absorption without clogging pores.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dry, stressed skin, dark under-eye circles, scar marks, or early fine lines.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Sundoshine</td></tr>
  <tr><th>Category</th><td>Skincare / Nourishing Oils</td></tr>
  <tr><th>Product Type</th><td>Pure Vitamin E Skin & Face Oil</td></tr>
  <tr><th>Volume/Weight</th><td>75 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Ideal for Dry & Stressed Skin)</td></tr>
  <tr><th>Finish</th><td>Hydrated, radiant, smooth & scar-reduced skin</td></tr>
  <tr><th>Texture</th><td>Rich golden lightweight absorbing oil</td></tr>
  <tr><th>Fragrance</th><td>Natural unperfumed scent</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Vitamin E, Natural Carrier Oils</td></tr>
  <tr><th>Country of Origin</th><td>China / Saudi Arabia</td></tr>
  <tr><th>Manufacturer</th><td>Sundoshine Skincare Labs</td></tr>
  <tr><th>Age Group</th><td>All Ages (15+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Vitamin E & Cellular Antioxidant Protection</h2>

<h3>What problem does this solve?</h3>
<p>Sundoshine Vitamin E Oil resolves skin dryness, dark under-eye circles, fine lines, and scar tissue marks.</p>

<h3>Why choose Vitamin E Oil?</h3>
<p>Ultraviolet radiation and pollution oxidise dermal lipids; Vitamin E neutralises free radicals, protecting collagen integrity.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Nightly Application:</strong> Apply before sleep to support overnight cellular renewal.<br>
2. <strong>Moisturizer Boost:</strong> Blend a drop into your daily cream for enhanced anti-aging defense.<br>
3. <strong>Nail Cuticle Care:</strong> Massage onto dry cuticles to prevent cracking.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Vitamin E oil clogs facial pores."<br>
<strong>Fact:</strong> Applying a few drops absorbs quickly, delivering antioxidant nutrition without clogging pores.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Tocopherol molecules integrate into cell membrane lipid bilayers, neutralizing reactive oxygen species (ROS) and promoting scar tissue healing.</p>"""

    en_faqs = [
        ("What is Sundoshine Vitamin E Oil 75ml?", "It is a concentrated skin and face oil rich in Vitamin E designed to hydrate, repair scars, and protect against aging."),
        ("What are the skin benefits of Vitamin E?", "It neutralizes free radicals, hydrates dry skin, reduces fine lines, and fades dark circles."),
        ("Can it be used on face and body?", "Yes, safe and effective for face, neck, hands, and body."),
        ("What volume is contained in this bottle?", "It comes in a 75ml bottle."),
        ("Does it help lighten dark under-eye circles?", "Yes, patting a light drop nightly hydrates and brightens under-eye skin."),
        ("Is it suitable for dry skin?", "Yes, it excels at treating dry, stressed, and flaking skin."),
        ("Does it feel greasy?", "Applying a few drops absorbs smoothly without excessive oiliness."),
        ("How should I apply it?", "Massage a few drops onto clean skin before sleep."),
        ("Can I mix it with moisturizer?", "Yes, blending a drop into your moisturizer enhances hydration."),
        ("Where is Sundoshine manufactured?", "It is produced following cosmetic quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it help reduce scar marks?", "Yes, it accelerates tissue repair and fades scars over time."),
        ("Can both men and women use it?", "Yes, it is a unisex skincare oil."),
        ("Is it suitable for teens?", "Suitable for adults and teens aged 15+."),
        ("Does it condition cuticles and nails?", "Yes, it prevents cuticle cracking and strengthens nails."),
        ("How should I store it?", "Store in a cool, dry place away from direct sunlight."),
        ("Does it prevent fine lines?", "Yes, it protects collagen to minimize early fine lines."),
        ("Is it suitable for oily skin?", "Oily skin types should use a very light single drop at night."),
        ("Is the bottle glass-sealed?", "Yes, it comes in a sealed bottle protecting oil potency."),
        ("Can it be applied to hair ends?", "Yes, a drop smoothed onto dry hair ends tames split ends."),
        ("Does it contain harsh perfumes?", "No, it is free of harsh artificial fragrances."),
        ("How long does the 75ml bottle last?", "The 75ml bottle lasts several months of daily usage."),
        ("Does it enhance skin radiance?", "Yes, it restores healthy, natural skin radiance."),
        ("Should it be washed off?", "No, leave it on for complete skin absorption."),
        ("Does it protect against winter dryness?", "Yes, it shields skin against harsh cold weather flaking.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1749",
        "sku": "EK-1749",
        "gtin": "6947825835247",
        "category": "العناية بالبشرة / الزيوت المغذية والمرطبة",
        "brand": "Sundoshine",
        "ar": {
            "title": "زيت فيتامين E النقي للبشرة والوجه من سندوشاين - 75 مل",
            "meta_title": "زيت فيتامين E سندوشاين 75مل | صيدلية إكليل أبها",
            "meta_description": "اشتري زيت فيتامين E النقي للبشرة والوجه من سندوشاين (75مل). ترطيب مكثف، تفتيح للهالات، وتقليل للندبات والخطوط. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["سندوشاين", "زيت_فيتامين_E", "ترطيب_البشرة", "تفتيح_الهالات", "إكليل_أبها"]
        },
        "en": {
            "title": "Sundoshine Vitamin E Oil for Skin and Face - 75ml",
            "meta_title": "Sundoshine Vitamin E Oil 75ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy Sundoshine Pure Vitamin E Oil for Face & Skin (75ml). Fades scars, dark circles, & fine lines. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["sundoshine", "vitamin_e_oil", "skincare", "anti_aging", "ekleel_abha"]
        },
        "schema": {
            "brand": "Sundoshine",
            "category": "Skincare / Facial Oil",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "sundoshine-vitamin-e-oil-for-skin-and-face-75ml.webp",
            "alt": "Sundoshine Vitamin E Oil for Skin and Face 75ml",
            "title": "Sundoshine Vitamin E Oil for Skin and Face 75ml"
        }
    }

def build_sponge_product(prod_id, title_ar, title_en, gtin, img_slug):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>{title_ar} (Moroccanoil Bath Sponge)</strong> الأداة المثالية والناعمة التي تضمن تنظيفاً عميقاً وتقشيراً لطيفاً لجسمكِ أثناء الاستحمام اليومي. صُنعت هذه الإسفنجة من ألياف دقيقة عالية الجودة ولطيفة جداً على البشرة، حيث ترغي الصابون وجل الاستحمام بكفاءة فائقة وتزيل خلايا الجلد الميتة دون التسبب في خدوش أو تهيج للبشرة.</p>
<p>تمتاز الإسفنجة بقوام ناعم ومريح في قبضة اليد، وتصل بسهولة إلى كافة أجزاء الجسم لتمنحكِ تجربة استحمام منعشة ومريحة تعيد للبشرة نضارتها ونظافتها الفائقة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف وتقشير لطيف للجسم:</strong> تزيل الأوساخ وخلايا الجلد الميتة برفق ودون تهيج.</li>
  <li><strong>توليد رغوة غنية واقتصادية:</strong> تضاعف رغوة صابون وجل الاستحمام وتوفر في الاستهلاك.</li>
  <li><strong>نسيج قطني ناعم على البشرة:</strong> لطيفة جداً على البشرة الحساسة ومناسبة للاستخدام اليومي.</li>
  <li><strong>تصميم مريح وسهل الاستخدام:</strong> قبضة مريحة تتيح لكِ تنظيف الجسم بسلاسة.</li>
  <li><strong>تنساب وتجف بسرعة:</strong> نسيج يقاوم الرطوبة وسهل التعليق والجفاف لمنع تكون البكتيريا.</li>
  <li><strong>مناسبة لجميع أفراد العائلة:</strong> خيار آمن وممتاز للاستحمام اليومي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل):</strong> بلي إسفنجة موروكان أويل بالماء الفاتر أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية (إضافة الصابون):</strong> وضعي كمية مناسبة من جل الاستحمام أو الصابون على الإسفنجة واضغطيها لتوليد رغوة كثيفة.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي كامل بشرة الجسم بحركات دائرية خفيفة لتنظيفها وتقشيرها.</li>
  <li><strong>الخطوة الرابعة (الشطف والتجفيف):</strong> اشطفي الإسفنجة جيداً بالماء، اعصريها، وعلقيها في مكان جاف.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>ألياف إسفنجية ناعمة فائقة الجودة (Soft Hypoallergenic Sponge):</strong> لطيفة على الأنسجة ومقاومة للتأكل.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي أثناء الاستحمام فقط.</li>
  <li>يُفضل استبدال الإسفنجة دورياً كل 1-2 شهر لضمان أقصى درجات النظافة.</li>
  <li>تُعلق في مكان جاف بعد كل استخدام.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحثون عن إسفنجة استحمام ناعمة وعالية الجودة لتنظيف وتقشير الجسم بلطف.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>موروكان أويل (Moroccanoil)</td></tr>
  <tr><th>الفئة</th><td>مستلزمات الاستحمام / إسفنج وعناية الجسم</td></tr>
  <tr><th>نوع المنتج</th><td>إسفنجة استحمام ناعمة لتنظيف وتقشير الجسم</td></tr>
  <tr><th>الحجم/الوزن</th><td>إسفنجة استحمام قطعة واحدة</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (الجلد والجسم)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم نظيف، ناعم، وخالٍ من خلايا الجلد الميتة</td></tr>
  <tr><th>الملمس</th><td>إسفنجي ناعم يرغي بكثافة</td></tr>
  <tr><th>العطر</th><td>عديم الرائحة (تستخدم مع جل الاستحمام)</td></tr>
  <tr><th>المكونات النشطة</th><td>ألياف إسفنجية مضادة للحساسية</td></tr>
  <tr><th>بلد المنشأ</th><td>المغرب / الصين</td></tr>
  <tr><th>الشركة المصنعة</th><td>Moroccanoil Care</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لأهمية إسفنجة الاستحمام وتقشير الجسم (Moroccanoil)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج إسفنجة موروكان أويل مشكلة تراكم خلايا الجلد الميتة والأوساخ السطحية وتساعد في تنظيف المسام دون جرح الجلد.</p>

<h3>لماذا يحدث تراكم الشوائب؟</h3>
<p>لأن خلايا الجلد تتجدد باستمرار وتتراكم الخلايا الميتة على السطح الخارجي، مما يجعل ملمس الجسم خشناً ويمنع امتصاص المرطبات.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام اللطيف:</strong> دلكي البشرة بحركات دائرية خفيفة دون فرك قسري.<br>
2. <strong>الشطف والتعليق:</strong> اشطفي الإسفنجة جيداً واعصريها وعلقيها لتجف فوراً.<br>
3. <strong>التغيير الدوري:</strong> استبدلي الإسفنجة كل 1-2 شهر لضمان أقصى درجات النظافة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "إسفنجة الاستحمام تجمع البكتيريا دائماً."<br>
<strong>الحقيقة:</strong> النسيج المطور في إسفنجة موروكان أويل يجف بسرعة ويقاوم تكون البكتيريا عند تعليقها في مكان تهوية مناسب.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تقوم ألياف الإسفنجة الميكرونية بإحداث مسح فيزيائي لطيف يرفع الخلايا الميتة من الطبقة القرنية، بينما تحبس الفجوات الإسفنجية الصابون لتوليد رغوة كثيفة تنظف المسام العميقة.</p>"""

    faqs = [
        (f"ما هي {title_ar}؟", "هي إسفنجة استحمام ناعمة وعالية الجودة مصممة لتوليد رغوة كثيفة وتنظيف وتقشير جلد الجسم بلطف."),
        ("هل الإسفنجة ناعمة على البشرة الحساسة؟", "نعم، نسيجها ناعم جداً ومصمم ليكون آمن ولطيف على البشرة الحساسة."),
        ("هل تساعد في توفير جل الاستحمام؟", "نعم، تضاعف رغوة الصابون وجل الاستحمام وتوفر في الاستهلاك بشكل ملحوظ."),
        ("كيف أعتني بالإسفنجة بعد الاستحمام؟", "اشطفيها جيداً بالماء الفاتر، اعصريها، وعلقيها في مكان جيد التهوية لتجف."),
        ("كم مرة يُفضل تغيير الإسفنجة؟", "يُفضل تغيير إسفنجة الاستحمام كل 1 إلى 2 شهر لضمان أعلى مستويات النظافة."),
        ("هل تناسب جميع أفراد العائلة؟", "نعم، آمنة وممتازة للبالغين والأطفال."),
        ("ما هو بلد صنع إسفنجة موروكان أويل؟", "صُنع وفق أعلى معايير مستلزمات العناية الشخصية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع مستلزمات الاستحمام لدى إكليل أبها أصلية 100% ومضمونة."),
        ("هل تقشر الجلد الميت بدون ألم؟", "نعم، تقشر خلايا الجلد الميتة السطحية برفق ودون أي ألم أو حكة."),
        ("هل الإسفنجة سهلة التجفيف؟", "نعم، نسيجها يجف بسرعة لمنع تكون البكتيريا."),
        ("هل تترك ملمساً ناعماً على الجسم؟", "نعم، تنعم الجلد وتتركه مشرقاً ونظيفاً."),
        ("هل تناسب الاستخدام اليومي؟", "نعم، ممتازة للاستحمام اليومي."),
        ("هل تصمد الإسفنجة مع الاستخدام؟", "نعم، نسيج متين ومقاوم للتفتت."),
        ("هل يمكن استخدامها مع الصابون المغربي؟", "نعم، ممتازة جداً للاستخدام مع الصابون المغربي والجليسرين."),
        ("هل الحجم مريح في اليد؟", "نعم، حجمها وقبضتها مريحة ومناسبة تماماً لليد."),
        ("هل تسبب أي حساسية للجلد؟", "لا، أليافها مضادة للحساسية وخالية من المواد الكيميائية الضارة."),
        ("هل العبوة محكمة الحفظ؟", "تأتي مغلفة لحمايتها حتى فتحها."),
        ("هل تساعد في تنظيف مسام الظهر؟", "نعم، تصل للمناطق المختلفة وتنظف المسام العميقة."),
        ("هل تعطي إحساساً بالاسترخاء؟", "تدليك الجسم بها أثناء الاستحمام ينشط الدورة الدموية ويرخي العضلات."),
        ("هل توجد ألوان مختلفة؟", "تأتي بألوان أنيقة تناسب ديكور الحمام."),
        ("هل تناسب الأطفال الصغار؟", "ناعمة وآمنة لأجسام الأطفال."),
        ("هل يمكن غسلها في الغسالة؟", "يُفضل غسلها يدوياً بالماء الفاتر والصابون."),
        ("هل تترك أثراً على البشرة؟", "لا، تنظف وتشطف بالكامل دون أي أثر."),
        ("هل تساعد في منع نمو الشعر تحت الجلد؟", "نعم، التقشير اليومي يقلل نمو الشعر تحت الجلد."),
        ("هل العبوة اقتصادية؟", "نعم، خيار ممتاز وعالي الجودة بسعر مناسب.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{title_en}</strong> is your ideal soft body cleansing companion designed to deliver gentle daily exfoliation and rich lather during showers. Crafted from premium, ultra-soft micro-sponge fibers, it glides comfortably over skin, lifting away dead skin cells and surface impurities without irritation.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Gentle Body Cleansing & Exfoliation:</strong> Lifts dead skin cells and surface dirt without irritating skin.</li>
  <li><strong>Generates Rich Lather Economically:</strong> Multiplies shower gel lather to maximize cleansing efficiency.</li>
  <li><strong>Ultra-Soft Skin Texture:</strong> Hypoallergenic fibers safe for daily use on sensitive skin.</li>
  <li><strong>Ergonomic Grip:</strong> Comfortable size that reaches all body contours easily.</li>
  <li><strong>Quick Drying & Hygienic:</strong> Moisture-resistant weave that dries fast to prevent bacterial growth.</li>
  <li><strong>Suitable for Whole Family:</strong> Safe, comfortable bath accessory for adults and kids.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet sponge with warm shower water.</li>
  <li><strong>Step 2 (Add Soap):</strong> Apply shower gel onto sponge and squeeze to create rich lather.</li>
  <li><strong>Step 3 (Massage):</strong> Massage gently over body skin in circular motions.</li>
  <li><strong>Step 4 (Rinse & Hang):</strong> Rinse thoroughly with water, squeeze out excess water, and hang to dry.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Soft Hypoallergenic Sponge Fibers:</strong> Durable, skin-friendly micro-fiber sponge composition.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external body shower cleansing only.</li>
  <li>Replace sponge every 1-2 months for maximum hygiene.</li>
  <li>Hang in a ventilated dry area after use.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a soft, high-quality bath sponge for gentle body cleansing and daily exfoliation.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Moroccanoil</td></tr>
  <tr><th>Category</th><td>Bath Accessories / Bath Sponges</td></tr>
  <tr><th>Product Type</th><td>Soft Gentle Body Cleansing & Exfoliating Sponge</td></tr>
  <tr><th>Volume/Weight</th><td>Single Bath Sponge</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Body Skin)</td></tr>
  <tr><th>Finish</th><td>Clean, smooth, refreshed body skin</td></tr>
  <tr><th>Texture</th><td>Soft rich-lathering sponge</td></tr>
  <tr><th>Fragrance</th><td>Unscented (Use with shower gel)</td></tr>
  <tr><th>Active Ingredients</th><td>Hypoallergenic Sponge Micro-Fibers</td></tr>
  <tr><th>Country of Origin</th><td>Morocco / China</td></tr>
  <tr><th>Manufacturer</th><td>Moroccanoil Care</td></tr>
  <tr><th>Age Group</th><td>All Ages</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Gentle Body Exfoliation & Bath Sponges</h2>

<h3>What problem does this solve?</h3>
<p>The Moroccanoil Bath Sponge resolves dead skin cell accumulation, surface dirt build-up, and uneven shower gel distribution.</p>

<h3>Why choose this sponge?</h3>
<p>Its soft micro-pore structure creates rich foam that buffs away dead stratum corneum cells without scratching skin tissue.</p>"""

    en_faqs = [
        (f"What is {title_en}?", "It is a soft, high-quality bath sponge designed for rich shower gel lathering and gentle body cleansing."),
        ("Is it safe for sensitive skin?", "Yes, its ultra-soft texture is safe and gentle on sensitive skin."),
        ("Does it help conserve shower gel?", "Yes, it multiplies foam production, reducing shower gel consumption."),
        ("How do I care for the sponge after use?", "Rinse with warm water, squeeze out excess moisture, and hang in a dry place."),
        ("How often should I replace it?", "Replace bath sponges every 1-2 months for optimal hygiene."),
        ("Is it suitable for the whole family?", "Yes, safe for adults and children."),
        ("Where is it manufactured?", "It is produced following personal care accessory quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All bath items at Ekleel Abha are 100% genuine."),
        ("Does it exfoliate dead skin painlessly?", "Yes, it gently lifts dead surface skin cells without irritation."),
        ("Is it quick-drying?", "Yes, its open cell design dries fast to prevent bacterial buildup."),
        ("Does it leave skin feeling soft?", "Yes, it leaves skin feeling clean, smooth, and refreshed."),
        ("Is it safe for daily shower use?", "Yes, perfect for daily bathing."),
        ("Is the sponge durable?", "Yes, made from tear-resistant durable sponge fibers."),
        ("Can it be used with Moroccan Black Soap?", "Yes, excellent for use with Moroccan soap and body washes."),
        ("Is the size comfortable to hold?", "Yes, designed with an ergonomic comfortable grip."),
        ("Does it cause skin allergies?", "No, made from hypoallergenic skin-safe materials."),
        ("Is it hygienically packaged?", "Yes, sealed for cleanliness until first use."),
        ("Does it help cleanse back pores?", "Yes, easily reaches body areas to clear pore impurities."),
        ("Does it relax muscles?", "Gentle massaging action stimulates circulation during showers."),
        ("Does it come in attractive colors?", "Yes, available in stylish bathroom-friendly shades."),
        ("Is it safe for young children?", "Yes, soft and safe for children's bodies."),
        ("Can it be machine washed?", "Hand rinsing with warm water and soap is recommended."),
        ("Does it leave residue on skin?", "No, rinses away completely with water."),
        ("Does it help prevent ingrown hairs?", "Yes, gentle daily scrubbing reduces ingrown hair risk."),
        ("Is it an economical bath choice?", "Yes, offers premium quality at an affordable price.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "مستلزمات الاستحمام / إسفنج وعناية الجسم",
        "brand": "Moroccanoil",
        "ar": {
            "title": title_ar,
            "meta_title": f"{title_ar} | صيدلية إكليل أبها",
            "meta_description": f"اشتري {title_ar}. اسفنجة ناعمة لتوليد رغوة كثيفة وتنظيف وتقشير الجسم بلطف. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["موروكان_اويل", "اسفنجة_استحمام", "تقشير_الجسم", "عناية_بالجسم", "إكليل_أبها"]
        },
        "en": {
            "title": title_en,
            "meta_title": f"{title_en} | Ekleel Abha Pharmacy",
            "meta_description": f"Buy {title_en}. Ultra-soft bath sponge for rich lather & gentle body cleansing. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["moroccanoil", "bath_sponge", "body_cleansing", "shower_sponge", "ekleel_abha"]
        },
        "schema": {
            "brand": "Moroccanoil",
            "category": "Bath / Sponge",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"{img_slug}.webp",
            "alt": title_en,
            "title": title_en
        }
    }

def create_product_1753():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>معجون أسنان مبيض من لاكالوت (Lacalut Whitening Toothpaste - 75 ml)</strong> المستحضر الألماني الطبي الأرقى لاستعادة البياض الطبيعي المشرق للأسنان مع توفير حماية فائقة ومتكاملة للثة ومينا الأسنان. يجمع هذا المعجون المتقدم بين مركبات التبييض اللطيفة (Hydrated Silica & Pyrophosphates) ومادة <strong>لاكتات الألومنيوم (Aluminum Lactate)</strong> الشهيرة بطبيعتها القابضة والمقوية للثة، مما يزيل التصبغات والبقع الناتجة عن القهوة والشاي والتدخين دون إضرار بطلاء المينا.</p>
<p>يحتوي المعجون على الفلورايد الفعال (Sodium Fluoride) بتركيز 1360 ppm لإعادة تمعدن طبقة المينا والوقاية الشاملة من التسوس والنخر الجانبي، مما يضمن لكِ أسنان بيضاء كاللؤلؤ، لثة صحية مشدودة، ونفساً منعشاً طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تبييض آمن واستعادة البياض الطبيعي:</strong> يزيل التصبغات والاصفرار الناجم عن القهوة والشاي والتدخين.</li>
  <li><strong>مدعم بـ لاكتات الألومنيوم (Aluminum Lactate):</strong> يقوي اللثة المترهلة ويزيل الالتهابات ويوقف النزيف.</li>
  <li><strong>حماية المينا وإعادة التمعدن:</strong> يحتوي على 1360 ppm فلورايد لتقوية جدار المينا والوقاية من التسوس.</li>
  <li><strong>مكافحة البلاك والجير الصلب:</strong> يمنع تكلس البيوفلم وتحوله إلى جير صلب بين الأسنان.</li>
  <li><strong>نفس منعش ونظافة ألمانية فاخرة:</strong> يقضي على البكتيريا المسببة لرائحة الفم وتلطخ الأسنان.</li>
  <li><strong>عبوة طبية 75 مل:</strong> خيار طبي مجرب وموصى به من أطباء الأسنان عالمياً.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق):</strong> وضعي كمية بحجم حبة البازلاء من معجون لاكالوت على فرشاة أسنان ناعمة.</li>
  <li><strong>الخطوة الثانية (التفريش):</strong> فرشي أسنانكِ جيداً بحركات دائرية ولطيفة لمدة دقيقتين على الأقل.</li>
  <li><strong>الخطوة الثالثة (البصق والشطف):</strong> ابصقي المعجون واشطفي الفم جيدا بالماء؛ يُفضل الاستخدام مرتين يومياً.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>لاكتات الألومنيوم (Aluminum Lactate):</strong> مركب ألماني فريد يشد اللثة ويمنع نزيفها.</li>
  <li><strong>فلورايد الصوديوم (Sodium Fluoride 1360 ppm):</strong> يعزز تمعدن المينا ويحمي من التسوس.</li>
  <li><strong>حبيبات السيليكا المنقية (Hydrated Silica):</strong> تقشر التصبغات السطحية بلطف دون خدش المينا.</li>
  <li><strong>مركبات البيروفوسفات (Pyrophosphates):</strong> تمنع تكلس الجير والبقع الصبغية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الفموي فقط.</li>
  <li>للأطفال دون 6 سنوات يُستعمل بحجم حبة البازلاء تحت إشراف لمنع البلع.</li>
  <li>يُحفظ بعيداً عن حرارة الشمس المباشرة.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن تبييض آمن للأسنان مع حماية كاملة للثة الضعيفة من النزيف والالتهاب.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لاكالوت (Lacalut)</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم / معاجين الأسنان المبيضة</td></tr>
  <tr><th>نوع المنتج</th><td>معجون أسنان مبيض ومقوي للثة (Lacalut White)</td></tr>
  <tr><th>الحجم/الوزن</th><td>75 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بالفم والأسنان)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان بيضاء، لثة مشدودة وصحية ونفس منعش</td></tr>
  <tr><th>الملمس</th><td>معجون ناعم غني بحبيبات التنظيف</td></tr>
  <tr><th>العطر</th><td>عطر النعناع الطبيعي المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>لاكتات الألومنيوم، فلورايد الصوديوم، هيدرات السيليكا، بيروفوسفات</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا (Dr. Theiss Naturwaren)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Dr. Theiss Naturwaren GmbH</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والأطفال فوق 6 سنوات</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد لاكتات الألومنيوم وتبييض الأسنان (Lacalut)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج معجون لاكالوت مبيض مشكلة اصفرار الأسنان الناتجة عن المشروبات والتدخين، ونزيف وترهل اللثة الناجم عن الالتهابات.</p>

<h3>لماذا يحدث النزيف والتصبغ؟</h3>
<p>يتسبب بقاء البلاك والبكتيريا بين الأسنان في تهيج حواف اللثة ونزيفها، بينما تصبغ مادة التانين بالقهوة والتدخين مينا السن.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التفريش دقيقتين:</strong> فرشي أسنانكِ دقيقتين كاملتين مرتين يومياً.<br>
2. <strong>استخدام فرشاة ناعمة:</strong> استعملي فرشاة أسنان ناعمة لحماية اللثة.<br>
3. <strong>المضمضة الجيدة:</strong> ابصقي المعجون واشطفي الفم بالماء.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "معاجين التبييض تسبب دائماً حساسية الأسنان وتآكل المينا."<br>
<strong>الحقيقة:</strong> معجون لاكالوت مبيض صُمم بحبيبات سيليكا ناعمة تبيّض وتزيل البقع دون خدش المينا.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يقوم مركب لاكتات الألومنيوم بشد بروتينات الأوعية الدموية في اللثة لوقف النزيف فورياً، بينما تعمل السيليكا المنقية والفلورايد على صقل السطح الخارجي وإعادة تمعدن المينا.</p>"""

    faqs = [
        ("ما هو معجون أسنان مبيض من لاكالوت 75 مل؟", "هو معجون أسنان طبي ألماني يجمع بين حبيبات التبييض الآمنة ولاكتات الألومنيوم لشد اللثة واستعادة البياض الطبيعي."),
        ("ما فائدة مركب لاكتات الألومنيوم في لاكالوت؟", "يقوي أنسجة اللثة المترهلة، يشدها، ويزيل النزيف والالتهابات بفاعلية ألمانية."),
        ("هل يسبب المعجون حساسيه لمينا الأسنان؟", "لا، يحتوي على حبيبات سيليكا ناعمة تبيّض وتزيل البقع دون إحداث خدوش في طبقة المينا."),
        ("ما حجم العبوة؟", "تأتي العبوة بحجم 75 مل."),
        ("هل يقي المعجون من تسوس الأسنان؟", "نعم، مدعم بـ 1360 ppm فلورايد الصوديوم لإعادة تمعدن المينا والوقاية من التسوس."),
        ("ما هي فوائده لمشروبي القهوة والشاي والمدخنين؟", "يزيل بقع التبغ والقهوة واصفرار الأسنان بفاعلية ويمنع تراكم الجير."),
        ("ما هو بلد صنع معجون لاكالوت؟", "صُنع بفخر في ألمانيا بواسطة شركة Dr. Theiss Naturwaren العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع معاجين لاكالوت لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("كم مرة يُنصح باستخدامه يومياً؟", "يُنصح بالتفريش مرتين يومياً صباحاً ومساءً."),
        ("هل يناسب الأطفال؟", "مناسب للأطفال فوق 6 سنوات بكمية بحجم حبة البازلاء وتحت الإشراف."),
        ("هل المعجون خالي من المواد المبيضة القاسية؟", "نعم، خالي من المواد المبيضة الكيميائية القاسية وتبييضه طبيعي آمن."),
        ("هل يساعد في القضاء على رائحة الفم؟", "نعم، يقضي على البكتيريا المسببة للرائحة الكريهة ويمنح نكهة نعناع منعشة."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل يمنع تكلس الجير بين الأسنان؟", "نعم، البيروفوسفات يمنع تكلس البلاك وتحوله لجير صلب."),
        ("هل يوصى به من أطباء الأسنان؟", "نعم، لاكالوت من أشهر العلامات الطبية الموصى بها عالمياً للثة والأسنان."),
        ("هل المعجون يرغي بكثافة؟", "يرغي بشكل متوازن ولطيف لتنظيف كافة زوايا الفم."),
        ("هل يشد اللثة من الاستخدام الأول؟", "تأثير لاكتات الألومنيوم القابض يظهر فورياً في شد اللثة وتخفيف النزيف."),
        ("هل يناسب الأسنان الحساسة؟", "نعم، تركيبته لطيفة وتحمي المينا واللثة الحساسة."),
        ("هل العبوة محكمة الحفظ؟", "تأتي في أنبوب طبقي محكم بغطاء لولبي."),
        ("هل يترك انطباع نظافة ألمانية؟", "نعم، يمنح شعوراً طويلاً بالانتعاش والنظافة الطبية."),
        ("هل يناسب كبار السن؟", "ممتاز جداً لكبار السن لحماية لثتهم وأسنانهم."),
        ("هل يزيل التصبغات القديمة؟", "نعم، الاستخدام المنتظم يستعيد البياض الطبيعي للأسنان."),
        ("هل يحتاج لاستخدام مضمضة بعده؟", "يمكن استخدامه بمفرده أو دمج مضمضة لاكالوت لنتائج مضاعفة."),
        ("هل العبوة 75 مل اقتصادية؟", "نعم، تكفي لأسابيع من الاستخدام العائلي اليومي."),
        ("هل يمنع انحسار اللثة؟", "شد وتقوية اللثة بـ لاكتات الألومنيوم يقي من انحسارها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Lacalut Whitening Toothpaste (75 ml)</strong> is a premier German medical oral care solution engineered to restore the natural brightness of your teeth while providing intensive protection for gums and tooth enamel. Fusing gentle silica whitening agents with signature <strong>Aluminum Lactate</strong>, it lifts stubborn coffee, tea, and tobacco stains without damaging enamel integrity.</p>
<p>Enriched with 1360 ppm Sodium Fluoride, Lacalut White remineralizes tooth enamel, guards against interdental cavities, firms bleeding gums, and delivers long-lasting fresh mint breath.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Safe Whitening & Stain Removal:</strong> Lifts surface discoloration caused by coffee, tea, and smoking.</li>
  <li><strong>Enriched with Aluminum Lactate:</strong> Tightens loose gum tissue, stops bleeding, and soothes inflammation.</li>
  <li><strong>Enamel Remineralization:</strong> Contains 1360 ppm Sodium Fluoride to fortify enamel and prevent cavities.</li>
  <li><strong>Plaque & Tartar Protection:</strong> Prevents plaque calcification into hard interdental tartar deposits.</li>
  <li><strong>German Medical Hygiene Standard:</strong> Neutralizes odor-causing bacteria with a long-lasting mint burst.</li>
  <li><strong>75ml Medical Tube:</strong> Dermatologically and dentist-recommended globally.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply):</strong> Apply a pea-sized amount of Lacalut White onto a soft toothbrush.</li>
  <li><strong>Step 2 (Brush):</strong> Brush teeth thoroughly in circular motions for at least 2 minutes.</li>
  <li><strong>Step 3 (Rinse):</strong> Spit out and rinse mouth with water; use twice daily for best results.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Aluminum Lactate:</strong> Signature German astringent compound that firms gums and halts bleeding.</li>
  <li><strong>Sodium Fluoride (1360 ppm):</strong> Fortifies tooth enamel and guards against acid decay.</li>
  <li><strong>Hydrated Silica Micro-Particles:</strong> Gently polish away surface stains without scratching enamel.</li>
  <li><strong>Pyrophosphates:</strong> Inhibit tartar buildup and stain re-adhesion.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For oral interdental brushing only.</li>
  <li>Children under 6 years should use a pea-sized amount under adult supervision.</li>
  <li>Store away from direct heat and sunlight.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking safe tooth whitening combined with intensive medical gum protection.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lacalut</td></tr>
  <tr><th>Category</th><td>Oral Care / Whitening Toothpastes</td></tr>
  <tr><th>Product Type</th><td>Medical Whitening & Gum Protection Toothpaste</td></tr>
  <tr><th>Volume/Weight</th><td>75 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Oral Care)</td></tr>
  <tr><th>Finish</th><td>White teeth, firm healthy gums & fresh breath</td></tr>
  <tr><th>Texture</th><td>Smooth paste with fine polishing micro-particles</td></tr>
  <tr><th>Fragrance</th><td>Fresh Natural Mint aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Aluminum Lactate, Sodium Fluoride (1360 ppm), Hydrated Silica</td></tr>
  <tr><th>Country of Origin</th><td>Germany (Dr. Theiss Naturwaren)</td></tr>
  <tr><th>Manufacturer</th><td>Dr. Theiss Naturwaren GmbH</td></tr>
  <tr><th>Age Group</th><td>Adults & Children 6+</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Aluminum Lactate & Enamel Remineralization</h2>

<h3>What problem does this solve?</h3>
<p>Lacalut Whitening Toothpaste resolves surface tooth staining and gum bleeding (gingivitis).</p>

<h3>Why choose Lacalut?</h3>
<p>Its dual-action formula pairs fine silica stain-polishing particles with Aluminum Lactate to tighten gingival tissues immediately.</p>"""

    en_faqs = [
        ("What is Lacalut Whitening Toothpaste 75ml?", "It is a German medical toothpaste combining safe stain-removal silica and Aluminum Lactate for gum protection."),
        ("What are the benefits of Aluminum Lactate?", "It tightens loose gums, stops bleeding, and reduces gingival inflammation."),
        ("Does it damage tooth enamel?", "No, its fine hydrated silica polishes surface stains without scratching enamel."),
        ("What volume is contained in this tube?", "It comes in a 75ml medical tube."),
        ("Does it prevent cavities?", "Yes, it contains 1360 ppm Sodium Fluoride to strengthen enamel and prevent cavities."),
        ("Is it effective for coffee and tobacco stains?", "Yes, it effectively lifts coffee, tea, and tobacco stains."),
        ("Where is Lacalut manufactured?", "It is proudly manufactured in Germany by Dr. Theiss Naturwaren."),
        ("How do I verify authenticity at Ekleel Abha?", "All Lacalut products at Ekleel Abha are 100% original from certified distributors."),
        ("How many times daily should I brush?", "Brush twice daily, morning and evening."),
        ("Is it safe for children?", "Safe for children over 6 years old with a pea-sized amount under supervision."),
        ("Is it free from harsh chemical bleaches?", "Yes, its whitening action relies on physical polishing and tartar prevention without harsh bleaches."),
        ("Does it neutralize bad breath?", "Yes, it eliminates odor-causing bacteria and provides fresh mint breath."),
        ("How should I store the tube?", "Store in a cool, dry place away from heat."),
        ("Does it prevent tartar formation?", "Yes, pyrophosphates prevent plaque from calcifying into hard tartar."),
        ("Is it dentist-recommended?", "Yes, Lacalut is a globally trusted, dentist-recommended medical brand."),
        ("Does it foam well?", "It produces a balanced, creamy foam for thorough cleansing."),
        ("Does it firm gums quickly?", "Yes, Aluminum Lactate delivers an immediate astringent gum-tightening effect."),
        ("Is it suitable for sensitive teeth?", "Yes, its gentle formula protects enamel and sensitive gums."),
        ("Is the tube securely sealed?", "Yes, it comes in a sealed hygienic tube."),
        ("Does it leave a medical clean feeling?", "Yes, it provides a long-lasting German medical clean sensation."),
        ("Is it suitable for seniors?", "Yes, ideal for protecting senior gums and enamel."),
        ("Does it lift old stains?", "Yes, regular brushing restores natural white tooth shade."),
        ("Should I use mouthwash after brushing?", "It can be used alone or paired with Lacalut mouthwash for enhanced protection."),
        ("Is the 75ml tube economical?", "Yes, provides weeks of daily family oral care."),
        ("Does it help prevent gum recession?", "Yes, firming gums with Aluminum Lactate helps guard against recession.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1753",
        "sku": "EK-1753",
        "gtin": "4016369546727",
        "category": "العناية بالفم / معاجين الأسنان المبيضة",
        "brand": "Lacalut",
        "ar": {
            "title": "معجون أسنان مبيض من لاكالوت لحماية اللثة واستعادة البياض الطبيعي - 75 مل",
            "meta_title": "معجون اسنان مبيض لاكالوت 75مل | صيدلية إكليل أبها",
            "meta_description": "اشتري معجون أسنان مبيض من لاكالوت (75مل). تبييض آمن وحماية للثة بـ لاكتات الألومنيوم والفلورايد. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["لاكالوت", "معجون_لاكالوت", "تبييض_الاسنان", "حماية_اللثة", "إكليل_أبها"]
        },
        "en": {
            "title": "Lacalut Whitening Toothpaste, 75 ml",
            "meta_title": "Lacalut Whitening Toothpaste 75ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy Lacalut Whitening Toothpaste (75ml). Safe whitening & gum protection with Aluminum Lactate & Fluoride. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["lacalut", "whitening_toothpaste", "gum_protection", "oral_care", "ekleel_abha"]
        },
        "schema": {
            "brand": "Lacalut",
            "category": "Oral Care / Toothpaste",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "lacalut-whitening-toothpaste-75ml.webp",
            "alt": "Lacalut Whitening Toothpaste 75ml",
            "title": "Lacalut Whitening Toothpaste 75ml"
        }
    }

print("Loaded Batch 11 builders")
