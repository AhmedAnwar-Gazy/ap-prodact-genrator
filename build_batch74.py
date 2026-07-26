import json, os

def create_product_2088():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول جسم عطر اللافندر مع ليفه من كوفيكس 500 مل (Cofix Lavender Scented Body Wash with Loofah - 500 ml)</strong> طقم الاستحمام العطري المهدئ الفاخر الأصيل من كوفيكس المصمم لمنح جسمك نظافة عميقة ورغوة كريمية غنية وعطراً فواحاً بنفحات اللافندر الهدئة طوال اليوم مع ليفة استحمام ناعمة مجانية. يرتكز هذا الغسول الأصيل (Cofix Lavender 500ml) على زيت اللافندر الأساسي (Lavender Essential Oil)، المنظفات اللطيفة متوازنة الحموضة، والمركبات المرطبة لبشرة الجسم.</p>
<p>يعمل غسول كوفيكس باللافندر على تنظيف مسام الجسم وإزالة الدهون والشوائب، تهدئة البشرة والأعصاب، وحفظ رطوبة الجلد، ليترك بشرتك ناعمة كالحرير، مرطبة، ومعطرة بالاسترخاء والنظافة من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عطر اللافندر المهدئ والمسترخي طوال اليوم:</strong> يريح الحواس ويوفر عبقاً زكياً فواحاً.</li>
  <li><strong>طقم مدمج يتضمن ليفة استحمام فاخرة مجانية:</strong> تزيد تكوين الرغوة وتقشير الخلايا الميتة.</li>
  <li><strong>تنظيف وتطهير فائق ورغوة كريمية غنية:</strong> ينظف الجسم بلطف دون تجفيف الجلد.</li>
  <li><strong>ترطيب وتنعيم لبشرة الجسم:</strong> يحفظ حاجز الترطيب الطبيعي للجلد.</li>
  <li><strong>تركيبة خفيفة متوازنة الحموضة (pH Balanced):</strong> مناسبة للاستخدام اليومي لجميع أنواع البشرة.</li>
  <li><strong>عبوة ضخمة سعة 500 مل مزودة بضاغط:</strong> حجم ممتاز للاستخدام العائلي اليومي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الجسم والليفة المرفقة بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> اضغطي كمية مناسبة من سائل كوفيكس على الليفة وكوّني رغوة غنية.</li>
  <li><strong>الخطوة الثالثة:</strong> دلكي الجسم برفق بحركات دائرية ثم اشطفي جيداً بالماء (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت اللافندر العطري والمركبات المهدئة:</strong> تمنحان عطراً زكياً مهدئاً للأعصاب والبشرة.</li>
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
  <li>لكل من يبحث عن غسول كوفيكس باللافندر مع ليفة 500 مل للانتعاش العطري والنظافة والاسترخاء.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كوفيكس (Cofix Care)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / غسولات ومجموعات الاستحمام المعطرة من كوفيكس 500ml</td></tr>
  <tr><th>نوع المنتج</th><td>غسول جسم عطري مهدئ باللافندر مع ليفة استحمام مجانية (500ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 مل + ليفة استحمام</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (العادية، الجافة والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، مرطب، ناصع النظافة ومفعم بعطر اللافندر لـ 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>سائل جل عطري رغوي غني</td></tr>
  <tr><th>العطر</th><td>عطر اللافندر الفرنسي المهدئ المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت اللافندر العطري، منظفات متوازنة pH، مرطبات جلدية</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية (KSA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Cofix Care Products</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت اللافندر العطري والليفة في غسول كوفيكس (Cofix Lavender Wash)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول كوفيكس باللافندر مشكلة جفاف البشرة بعد الاستحمام، التوتر اليومي، وتراكم الخلايا الميتة.</p>

<h3>لماذا تنجح تركيبة Cofix Lavender Wash & Loofah؟</h3>
<p>لأن نسيج الليفة يزيل الجلد الميت ميكانيكياً بينما يهدئ زيت اللافندر العطري الأعصاب ويغذي الجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام اليومي بماء دافئ:</strong> ينظف المسام ويريح الجسم.<br>
2. <strong>استخدام الليفة بحركات دائرية لطيفة:</strong> يحفز الدورة الدموية.<br>
3. <strong>الشطف الجيد بالماء:</strong> يضمن عدم بقاء ترسبات صابونية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "استخدام الليفة يومياً يسبب خدش وتقشر الجلد."<br>
<strong>الحقيقة:</strong> ليفة كوفيكس المرفقة مصممة بألياف ناعمة مرنة تنظف وتقشر بأمان كامل.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط مركبات اللافندر العطرية التوتر العصبي بينما تزيل الليفة القشور القرنية السطحية.</p>"""

    faqs = [
        ("ما هو غسول جسم عطر اللافندر مع ليفه من كوفيكس 500 مل؟", "هو طقم استحمام فاخر يتضمن غسول جسم عطري باللافندر 500 مل وليفة استحمام ناعمة مجانية من كوفيكس."),
        ("ما هي فوائد زيت اللافندر العطري والليفة المرفقة؟", "تزيل الليفة الخلايا الميتة، ويهدئ زيت اللافندر الأعصاب والبشرة، ويمنح عطراً فواحاً."),
        ("هل يمنح رغوة غنية وعطراً مهدئاً طوال اليوم؟", "نعم، مثبت سريرياً في توفير رغوة غنية وانتعاش عاطري باللافندر لـ 24 ساعة."),
        ("ما حجم العبوة ومحتوياتها؟", "تأتي بعبوة 500 مل مزودة بضاغط مريح + ليفة استحمام مجانية."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الجسم والليفة، ضعي كمية على الليفة وكوّني رغوة، دلكي برفق واشطفي بالماء يومياً."),
        ("هل هو آمن لجميع أنواع البشرة؟", "نعم، تركيبة متوازنة الحموضة آمنة لجميع أنواع بشرة الجسم."),
        ("أين صُنع غسول كوفيكس باللافندر؟", "صُنع في المملكة العربية السعودية بواسطة Cofix Care Products."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كوفيكس لدى إكليل أبها أصلية 100%."),
        ("ما رائحة غسول كوفيكس باللافندر؟", "عطر اللافندر الفرنسي المهدئ المنعش الفاخر."),
        ("هل يترك البشرة ناعمة ومرطبة؟", "نعم، يحافظ على رطوبة الجلد ونعومته الحريرية."),
        ("هل 500 مل مع ليفة تكفي للاستخدام العائلي؟", "نعم، عبوة ضخمة بضاغط وليفة تكفي لعدة أشهر من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع أفراد الأسرة وخاصة محبي اللافندر والاسترخاء."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً أثناء الاستحمام."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، ينشطف بالماء الدافئ بسهولة دون ترك أثر لزج."),
        ("هل كوفيكس علامة موثوقة في العناية بالجسم؟", "نعم، Cofix علامة سعودية رائدة وموثوقة جداً في العناية الشخصية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في إزالة رائحة العرق؟", "نعم، ينظف بفاعلية ويعطر الجسم بنفحات لافندر عاطرة."),
        ("هل يناسب الاستخدام قبل النوم للاسترخاء؟", "نعم، ممتاز للاستحمام المسائي لتهدئة الأعصاب والنوم المريح."),
        ("هل يترك أثراً دهنياً؟", "لا، ينظف وينشطف بالكامل دون دهنية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل العبوة مزودة بضاغط مريح؟", "نعم، ضاغط مريح جداً يسهل استخدام الجل أثناء الاستحمام."),
        ("هل يناسب الشتاء والصيف؟", "نعم، ممتاز لجميع فصول السنة."),
        ("هل يصلح هدية ضمن مجموعة الاستحمام؟", "نعم، خيار ممتاز جداً في مجموعات العناية الشخصية والهدايا."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Cofix Lavender Scented Body Wash with Loofah - 500 ml</strong> is an authentic luxury soothing shower set from Cofix designed to deliver deep cleansing, a rich creamy lather, and a calming lavender scent all day long paired with a free soft shower loofah. Built upon Lavender Essential Oil, pH-balanced mild cleansers, and body-moisturizing compounds.</p>
<p>Cofix Lavender Body Wash cleanses body pores of dirt and excess sebum, soothes skin and mind, and guards skin moisture, leaving your body touchably silky soft, hydrated, and fragranced with fresh relaxation from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Soothing All-Day Lavender Fragrance:</strong> Relaxes senses delivering a long-lasting floral aroma.</li>
  <li><strong>Includes a Free Premium Shower Loofah:</strong> Enhances foaming and gently exfoliates dead skin cells.</li>
  <li><strong>Superior Cleansing & Rich Creamy Lather:</strong> Cleanses body gently without drying skin.</li>
  <li><strong>Body Skin Softening & Hydration:</strong> Preserves the skin's natural moisture barrier.</li>
  <li><strong>pH-Balanced Mild Formula:</strong> Suitable for daily use on all skin types.</li>
  <li><strong>Generous 500ml Value Pump Bottle:</strong> Excellent format for daily continuous family use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet body skin and the included loofah with warm water during shower.</li>
  <li><strong>Step 2:</strong> Pump a suitable amount of Cofix gel onto loofah and work into a rich lather.</li>
  <li><strong>Step 3:</strong> Massage body gently in circular motions, then rinse thoroughly with water (use daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Lavender Essential Oil & Soothing Agents:</strong> Deliver a calming fragrance relaxing body and mind.</li>
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
  <li>Anyone seeking Cofix Lavender Body Wash with Loofah 500ml for fragrant shower relaxation and clean skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Cofix Care</td></tr>
  <tr><th>Category</th><td>Body Care / Cofix Fragranced Body Washes 500ml</td></tr>
  <tr><th>Product Type</th><td>Soothing Lavender Perfumed Body Wash with Free Loofah (500ml)</td></tr>
  <tr><th>Volume/Weight</th><td>500 ml + Free Shower Loofah</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Normal, Dry & Oily Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, hydrated, spotlessly clean body skin fragranced with Lavender</td></tr>
  <tr><th>Texture</th><td>Rich foaming fragranced clear gel fluid</td></tr>
  <tr><th>Fragrance</th><td>Calming fresh French lavender floral scent</td></tr>
  <tr><th>Active Ingredients</th><td>Lavender Essential Oil, pH-Balanced Cleansers, Hydrating Agents</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia (KSA)</td></tr>
  <tr><th>Manufacturer</th><td>Cofix Care Products</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Lavender Essential Oil Relaxation & Mechanical Loofah Exfoliation</h2>

<h3>What problem does this solve?</h3>
<p>Cofix Lavender Body Wash resolves post-shower dryness, daily stress, and dead skin cell buildup.</p>

<h3>Why choose Cofix Lavender Body Wash with Loofah?</h3>
<p>The soft loofah exfoliates surface flaking while lavender essential oil calms neural tension and hydrates skin.</p>"""

    en_faqs = [
        ("What is Cofix Lavender Scented Body Wash with Loofah - 500 ml?", "It is a luxury shower set featuring a 500ml lavender fragranced body wash and a free soft shower loofah from Cofix."),
        ("What are the benefits of Lavender Essential Oil and the free loofah?", "The loofah exfoliates dead skin cells, while lavender essential oil relaxes mind and skin and delivers a fresh scent."),
        ("Does it yield a rich lather and a calming lavender scent?", "Yes, clinically proven to produce a rich lather and deliver 24-hour lavender scent retention."),
        ("What volume and contents are included?", "500ml pump bottle + free shower loofah."),
        ("How do I use it correctly?", "Wet body and loofah, pump gel onto loofah, lather, massage gently and rinse daily."),
        ("Is it safe for all skin types?", "Yes, pH-balanced formula safe for all body skin types."),
        ("Where is Cofix Lavender Wash manufactured?", "In Saudi Arabia by Cofix Care Products."),
        ("How do I verify authenticity at Ekleel Abha?", "All Cofix products at Ekleel Abha are 100% original."),
        ("What scent does Cofix Lavender Wash have?", "Calming fresh French lavender floral fragrance."),
        ("Does it leave skin soft and hydrated?", "Yes, preserves skin moisture and silky softness."),
        ("Does 500ml with loofah last long?", "Yes, lasts months of regular daily bath use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for men and women?", "Yes, suitable for the entire family especially relaxation lovers."),
        ("How many times daily?", "Once or twice daily during showers."),
        ("Does it rinse off easily?", "Yes, rinses off smoothly with warm water without sticky residue."),
        ("Is Cofix a trusted brand in Saudi Arabia?", "Yes, Cofix is a leading trusted brand in personal care in KSA."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help remove sweat odor?", "Yes, effectively cleanses and perfumes body skin."),
        ("Is it good for bedtime shower relaxation?", "Yes, excellent for evening showers calming mind and promoting sleep."),
        ("Does it leave a greasy film?", "No, cleanses completely clean without greasiness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is the pump bottle convenient?", "Yes, convenient pump dispenser for easy shower use."),
        ("Is it good for summer and winter?", "Yes, excellent for all seasons."),
        ("Is it a nice shower gift?", "Yes, excellent addition to personal care gift sets."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2088",
        "sku": "EK-2088",
        "gtin": "697794487751",
        "brand": "Cofix",
        "ar": {
            "title": "غسول جسم عطر اللافندر مع ليفه من كوفيكس 500 مل",
            "meta_title": "غسول جسم كوفيكس باللافندر مع ليفة 500مل | إكليل أبها",
            "meta_description": "اشتري غسول جسم عطر اللافندر مع ليفة من كوفيكس (500 مل). سائل استحمام مهدئ بعطر اللافندر مع ليفة ناعمة مجانية. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كوفيكس", "غسول_اللافندر_كوفيكس", "غسول_مع_ليفة", "سائل_استحمام_اللافندر", "إكليل_أبها"]
        },
        "en": {
            "title": "Cofix Lavender Scented Body Wash with Loofah - 500 ml",
            "meta_title": "Cofix Lavender Body Wash with Loofah 500ml | Ekleel Abha",
            "meta_description": "Buy original Cofix Lavender Scented Body Wash with Loofah (500ml). Soothing lavender perfumed body wash with free shower loofah. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["cofix", "lavender_body_wash", "body_wash_with_loofah", "cofix_lavender", "ekleel_abha"]
        }
    }


def create_product_2089():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول جسم إحساس البروده مع ليفه من كوفيكس 500 مل (Cofix Cool Sensation Body Wash with Loofah - 500 ml)</strong> طقم الاستحمام العطري المنشط الفاخر الأصيل من كوفيكس المصمم لمنح جسمك انتعاشاً مبرداً ونظافة فائقة ورغوة غنية بنفحات النعناع والبرودة المنشطة طوال اليوم مع ليفة استحمام ناعمة مجانية. يرتكز هذا الغسول الأصيل (Cofix Cool Sensation 500ml) على خُلاصة المنتهول المبردة (Menthol Extract)، المنظفات اللطيفة متوازنة الحموضة، والمركبات المرطبة لبشرة الجسم.</p>
<p>يعمل غسول كوفيكس بإحساس البرودة على تنظيف مسام الجسم وإزالة الدهون والتعرق، إطفاء حرارة الصيف والرياضة، وحفظ رطوبة الجلد، ليترك بشرتك ناعمة كالحرير، مرطبة، ومعطرة بالانتعاش البرودي الثلجي من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>إحساس البرودة والنعناع المنشط طوال اليوم:</strong> يطفئ حرارة الصيف والجهد ويوفر برودة منعشة.</li>
  <li><strong>طقم مدمج يتضمن ليفة استحمام فاخرة مجانية:</strong> تزيد تكوين الرغوة وتقشير الشوائب.</li>
  <li><strong>تنظيف وتطهير فائق ورغوة كريمية غنية:</strong> ينظف الجسم بفاعلية دون تجفيف البشرة.</li>
  <li><strong>ترطيب وتنعيم لبشرة الجسم:</strong> يحفظ حاجز الترطيب الطبيعي للجلد.</li>
  <li><strong>تركيبة خفيفة متوازنة الحموضة (pH Balanced):</strong> مناسبة للاستخدام اليومي لجميع أنواع البشرة.</li>
  <li><strong>عبوة ضخمة سعة 500 مل مزودة بضاغط:</strong> حجم ممتاز للاستخدام العائلي والرياضي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الجسم والليفة المرفقة بالماء الدافئ أو البارد أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> اضغطي كمية مناسبة من سائل كوفيكس على الليفة وكوّني رغوة غنية.</li>
  <li><strong>الخطوة الثالثة:</strong> دلكي الجسم برفق واستمتعي بإحساس البرودة ثم اشطفي بالماء (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة المنتهول المبردة والمركبات المنشطة:</strong> تمنحان شعوراً بالانتعاش الثلجي وتنعيش الجسم.</li>
  <li><strong>المنظفات اللطيفة والمركبات المرطبة:</strong> تنظف المسام وتحفظ النعومة الحريرية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن غسول كوفيكس بإحساس البرودة مع ليفة 500 مل للانتعاش الرياضي والصيفي الفائق.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كوفيكس (Cofix Care)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / غسولات ومجموعات الاستحمام المعطرة من كوفيكس 500ml</td></tr>
  <tr><th>نوع المنتج</th><td>غسول جسم عطري مبرد بالمنثول مع ليفة استحمام مجانية (500ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 مل + ليفة استحمام</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (العادية، الجافة والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، مرطب، ناصع النظافة ومفعم ببرودة المنثول لـ 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>سائل جل عطري رغوي مبرد غني</td></tr>
  <tr><th>العطر</th><td>عطر النعناع والمنثول الثلجي المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة المنتهول المبردة، منظفات متوازنة pH، مرطبات جلدية</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية (KSA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Cofix Care Products</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد خلاصة المنتهول المبردة والليفة في غسول كوفيكس (Cofix Cool Sensation Wash)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول كوفيكس بالبرودة مشكلة حرارة الجسم بالصيف، الإجهاد العضلي بعد الرياضة، ورائحة التعرق.</p>

<h3>لماذا تنجح تركيبة Cofix Cool Sensation & Loofah؟</h3>
<p>لأن مستقبلات البرودة الجلدية تتنشط بفعل المنتهول بينما تزيل الليفة الرواسب والتعرق السطحي.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام فوراً بعد التمارين الرياضية:</strong> يبرد الجسم ويقضي على الجراثيم والتعرق.<br>
2. <strong>استخدام الليفة بحركات دائرية:</strong> يزيل الخلايا الميتة وينشط الدورة الدموية.<br>
3. <strong>الشطف بالماء الفاتر:</strong> يعزز الانتعاش الشعوري بالبرودة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "غسولات البرودة تسبب حرقان بالجلد."<br>
<strong>الحقيقة:</strong> غسول كوفيكس مصمم بجرعة منثول طبية متوازنة تمنح برودة لطيفة دون أي حرقان.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يرتبط المنتهول بمستقبلات TRPM8 الجلدية محفزاً إشارة البرودة الطبيعية لإنعاش الجسم.</p>"""

    faqs = [
        ("ما هو غسول جسم إحساس البروده مع ليفه من كوفيكس 500 مل؟", "هو طقم استحمام فاخر يتضمن غسول جسم مبرد بالمنثول 500 مل وليفة استحمام ناعمة مجانية من كوفيكس."),
        ("ما هي فوائد خلاصة المنتهول المبردة والليفة المرفقة؟", "تزيل الليفة الشوائب، ويبرد المنتهول الجسم ويقضي على التعرق، ويمنح انتعاشاً ثلجياً."),
        ("هل يمنح رغوة غنية وإحساساً بالبرودة طوال اليوم؟", "نعم، مثبت سريرياً في توفير رغوة غنية وانتعاش مبرد برائحة النعناع لـ 24 ساعة."),
        ("ما حجم العبوة ومحتوياتها؟", "تأتي بعبوة 500 مل مزودة بضاغط مريح + ليفة استحمام مجانية."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الجسم والليفة، ضعي كمية على الليفة وكوّني رغوة، دلكي برفق واشطفي بالماء يومياً."),
        ("هل هو آمن لجميع أنواع البشرة؟", "نعم، تركيبة متوازنة الحموضة آمنة لجميع أنواع بشرة الجسم."),
        ("أين صُنع غسول كوفيكس بإحساس البرودة؟", "صُنع في المملكة العربية السعودية بواسطة Cofix Care Products."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كوفيكس لدى إكليل أبها أصلية 100%."),
        ("ما رائحة غسول كوفيكس بإحساس البرودة؟", "عطر النعناع والمنثول الثلجي المنعش الفاخر."),
        ("هل يترك البشرة ناعمة ومرطبة؟", "نعم، يحافظ على رطوبة الجلد ونعومته الحريرية."),
        ("هل 500 مل مع ليفة تكفي للاستخدام العائلي والرياضي؟", "نعم، عبوة ضخمة بضاغط وليفة تكفي لعدة أشهر من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب الرجال والنساء والرياضيين؟", "نعم، ممتاز جداً للرياضيين والرجال والنساء بالصيف."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً أثناء الاستحمام."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، ينشطف بالماء بسهولة دون ترك أثر لزج."),
        ("هل كوفيكس علامة موثوقة في العناية بالجسم؟", "نعم، Cofix علامة سعودية رائدة وموثوقة جداً في العناية الشخصية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في إزالة رائحة التعرق بعد الرياضة؟", "نعم، ينظف بفاعلية ويطرد رائحة التعرق بنفحات النعناع المبردة."),
        ("هل يناسب الاستخدام في أيام الحر الشديد؟", "نعم، خيار أسطوري لإطفاء حرارة الصيف والشعور بالانتعاش الثلجي."),
        ("هل يترك أثراً دهنياً؟", "لا، ينظف وينشطف بالكامل دون دهنية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل العبوة مزودة بضاغط مريح؟", "نعم، ضاغط مريح جداً يسهل استخدام الجل أثناء الاستحمام."),
        ("هل يناسب الصيف والشتاء؟", "ممتاز جداً للصيف وبعد التمارين والأنشطة الرياضية."),
        ("هل يصلح هدية ضمن مجموعة الاستحمام؟", "نعم، خيار ممتاز جداً في مجموعات العناية الشخصية والرياضية."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Cofix Cool Sensation Body Wash with Loofah - 500 ml</strong> is an authentic luxury cooling energizing shower set from Cofix designed to deliver instant cooling, deep cleansing, a rich foaming lather, and an ice-mint sensation all day paired with a free soft shower loofah. Built upon Menthol Extract, pH-balanced mild cleansers, and body-moisturizing compounds.</p>
<p>Cofix Cool Sensation Body Wash cleanses body pores of sweat and excess sebum, quenches summer and post-workout body heat, and guards skin moisture, leaving your body touchably silky soft, hydrated, and fragranced with icy mint freshness from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>All-Day Cooling Menthol & Icy Mint Sensation:</strong> Quenches summer heat and post-workout fatigue.</li>
  <li><strong>Includes a Free Premium Shower Loofah:</strong> Enhances lathering and gently sweeps away impurities.</li>
  <li><strong>Superior Cleansing & Rich Foaming Lather:</strong> Cleanses body effectively without drying skin.</li>
  <li><strong>Body Skin Softening & Hydration:</strong> Preserves the skin's natural moisture barrier.</li>
  <li><strong>pH-Balanced Mild Formula:</strong> Suitable for daily use on all skin types.</li>
  <li><strong>Generous 500ml Value Pump Bottle:</strong> Excellent format for sports routines and daily family use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet body skin and the included loofah with warm or cool water during shower.</li>
  <li><strong>Step 2:</strong> Pump a suitable amount of Cofix gel onto loofah and work into a rich lather.</li>
  <li><strong>Step 3:</strong> Massage body gently enjoying the cooling sensation, then rinse with water (use daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Cooling Menthol Extract & Energizing Agents:</strong> Deliver an icy mint sensation refreshing the body.</li>
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
  <li>Athletes and anyone seeking Cofix Cool Sensation Body Wash with Loofah 500ml for icy shower freshness and clean skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Cofix Care</td></tr>
  <tr><th>Category</th><td>Body Care / Cofix Fragranced Body Washes 500ml</td></tr>
  <tr><th>Product Type</th><td>Cooling Menthol Icy Scent Body Wash with Free Loofah (500ml)</td></tr>
  <tr><th>Volume/Weight</th><td>500 ml + Free Shower Loofah</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Normal, Dry & Oily Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, hydrated, spotlessly clean body skin fragranced with Menthol</td></tr>
  <tr><th>Texture</th><td>Rich foaming fragranced cooling clear gel fluid</td></tr>
  <tr><th>Fragrance</th><td>Invigorating fresh icy mint menthol scent</td></tr>
  <tr><th>Active Ingredients</th><td>Cooling Menthol Extract, pH-Balanced Cleansers, Hydrating Agents</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia (KSA)</td></tr>
  <tr><th>Manufacturer</th><td>Cofix Care Products</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Menthol TRPM8 Receptor Activation & Post-Workout Thermal Relief</h2>

<h3>What problem does this solve?</h3>
<p>Cofix Cool Sensation Body Wash resolves post-workout body heat, heavy summer sweat, and skin tiredness.</p>

<h3>Why choose Cofix Cool Sensation Body Wash with Loofah?</h3>
<p>Menthol activates cutaneous TRPM8 cold receptors providing thermal relief while the loofah cleanses sweat pores.</p>"""

    en_faqs = [
        ("What is Cofix Cool Sensation Body Wash with Loofah - 500 ml?", "It is a luxury cooling shower set featuring a 500ml menthol cooling body wash and a free soft shower loofah from Cofix."),
        ("What are the benefits of Menthol Extract and the free loofah?", "The loofah sweeps away impurities, while menthol cools skin, eliminates sweat odors, and delivers icy freshness."),
        ("Does it yield a rich lather and a cooling mint sensation?", "Yes, clinically proven to produce a rich lather and deliver 24-hour icy mint cooling retention."),
        ("What volume and contents are included?", "500ml pump bottle + free shower loofah."),
        ("How do I use it correctly?", "Wet body and loofah, pump gel onto loofah, lather, massage gently and rinse daily."),
        ("Is it safe for all skin types?", "Yes, pH-balanced formula safe for all body skin types."),
        ("Where is Cofix Cool Sensation Wash manufactured?", "In Saudi Arabia by Cofix Care Products."),
        ("How do I verify authenticity at Ekleel Abha?", "All Cofix products at Ekleel Abha are 100% original."),
        ("What scent does Cofix Cool Sensation Wash have?", "Invigorating fresh icy mint menthol fragrance."),
        ("Does it leave skin soft and hydrated?", "Yes, preserves skin moisture and silky softness."),
        ("Does 500ml with loofah last long?", "Yes, lasts months of regular daily sports bath use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for athletes, men, and women?", "Yes, suitable for the entire family especially athletes and summer sports lovers."),
        ("How many times daily?", "Once or twice daily during showers."),
        ("Does it rinse off easily?", "Yes, rinses off smoothly with water without sticky residue."),
        ("Is Cofix a trusted brand in Saudi Arabia?", "Yes, Cofix is a leading trusted brand in personal care in KSA."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help remove sweat odor after sports?", "Yes, effectively cleanses and banishes post-workout sweat odors with icy mint."),
        ("Is it good for hot summer days?", "Yes, an ultimate shower essential for quenching summer body heat."),
        ("Does it leave a greasy film?", "No, cleanses completely clean without greasiness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is the pump bottle convenient?", "Yes, convenient pump dispenser for easy shower use."),
        ("Is it good for summer and sports?", "Yes, ideal for summer, gym workouts, and sports routines."),
        ("Is it a nice shower gift?", "Yes, excellent addition to sports and personal care gift sets."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2089",
        "sku": "EK-2089",
        "gtin": "697794487775",
        "brand": "Cofix",
        "ar": {
            "title": "غسول جسم إحساس البروده مع ليفه من كوفيكس 500 مل",
            "meta_title": "غسول جسم كوفيكس إحساس البرودة مع ليفة 500مل | إكليل أبها",
            "meta_description": "اشتري غسول جسم إحساس البرودة مع ليفة من كوفيكس (500 مل). سائل استحمام مبرد بالمنثول والنعناع الثلجي مع ليفة ناعمة مجانية. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كوفيكس", "غسول_البرودة_كوفيكس", "غسول_المنثول", "سائل_استحمام_مبرد", "إكليل_أبها"]
        },
        "en": {
            "title": "Cofix Cool Sensation Body Wash with Loofah - 500 ml",
            "meta_title": "Cofix Cool Sensation Body Wash with Loofah 500ml | Ekleel Abha",
            "meta_description": "Buy original Cofix Cool Sensation Body Wash with Loofah (500ml). Cooling menthol icy mint body wash with free shower loofah. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["cofix", "cool_sensation_wash", "menthol_body_wash", "cooling_body_wash", "ekleel_abha"]
        }
    }


def create_product_2091():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>زيت إكليل الجبل العطري ( الروزماري ) ناو 30 مل (NOW Rosemary Essential Oil - 30 ml)</strong> الزيت العطري العلاجي الفاخر الأصيل 100% من ناو فودز (NOW Foods) المصمم خصيصاً لتحفيز نمو الشعر، إنبات الفراغات، تقوية بصيلات الشعر، وتنشيط الدورة الدموية بفروة الرأس والتركيز الذهني. يرتكز هذا الزيت الأصيل (NOW Rosemary Oil 30ml) على زيت الروزماري النقي 100% المستخلص بالتقطير بالبخار من أوراق <em>Rosmarinus Officinalis</em> العضوية.</p>
<p>يعمل زيت الروزماري من ناو عند تخفيفه بزيت ناقل على تنشيط فروة الرأس، الحد من تساقط الشعر، تغذية البصيلات الضعيفة، وتزويدك بعبق عشبي منشط ومصفٍ للذهن، ليترك شعرك أكثر كثافة، قوة، وحيوية، وفروة رأسك ناصعة النقاء من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>نقي 100% مستخلص بالتقطير بالبخار (100% Pure & Steam-Distilled):</strong> أعلى درجات النقاء والجودة العالمية.</li>
  <li><strong>تحفيز نمو وإنبات الشعر وتقوية البصيلات:</strong> يقلل التساقط ويساعد في زيادة كثافة الشعر.</li>
  <li><strong>تنشيط الدورة الدموية لفروة الرأس:</strong> يوصل الأكسجين والمغذيات لجذور الشعر.</li>
  <li><strong>إنعاش وتصفية الذهن والعقل بالعلاج العطري (Aromatherapy):</strong> يحسن التركيز والذاكرة عند الفواحة.</li>
  <li><strong>جودة NOW Solutions العالمية الشهيرة:</strong> الزيت العطري الأكثر توصية وشهرة عالمياً.</li>
  <li><strong>زجاجة مدمجة سعة 30 مل بحطارة قطارة مريحة:</strong> حجم ممتاز للاستخدام المتكرر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> للعناية بالشعر: خففي 3-5 قطرات من زيت الروزماري مع ملعقة من زيت ناقل (كالجوجوبا أو الأرغان).</li>
  <li><strong>الخطوة الثانية:</strong> دلكي فروة الرأس برفق بحركات دائرية واتركيه من 30 دقيقة إلى ساعة قبل الشامبو.</li>
  <li><strong>الخطوة الثالثة:</strong> للعلاج العطري: أضيفي 3-5 قطرات في الفواحة المائية واستنشقي الانتعاش العشبي (يُستعمل 2-3 مرات أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الروزماري النقي 100% (Rosmarinus Officinalis Leaf Oil):</strong> غني بمركبات السينيول والألفا بينين المنشطة للبصيلات.</li>
</ul>

<h2>تحذيرات وااحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي والعطري فقط؛ يمنع بلعه أو استخدامه مركزاً مباشرة دون تخفيف.</li>
  <li>تجنبي التلامس المباشر مع العينين واختبري التحسس على مساحة صغيرة من الجلد قبل الاستخدام.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن الشمس.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن زيت إكليل الجبل العطري (الروزماري) ناو 30 مل لتكثيف الشعر ومنع التساقط والعلاج العطري.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ناو / ناو فودز (NOW Solutions)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر والجسم / الزيوت العطرية العضوية النقية 30ml</td></tr>
  <tr><th>نوع المنتج</th><td>زيت إكليل الجبل (روزماري) عطري نقي 100% مصفى بالتقطير (30ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>30 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع فروة الرأس والشعر (خصيصاً الشعر الخفيف والمتقصف والمتساقط)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر أكثر كثافة، بصيلات قوية، وفروة رأس ناصعة الصحة منشطة</td></tr>
  <tr><th>الملمس</th><td>زيت عطري مركّز خفيف الامتصاص عند التخفيف</td></tr>
  <tr><th>العطر</th><td>عطر الروزماري العشبي المنعش المنشط الأصيل</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت أوراق الروزماري النقي 100% (Rosmarinus Officinalis)</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة الأمريكية (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>NOW Foods USA</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون والمراهقون (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت الروزماري النقي في تكثيف الشعر وإنبات الفراغات (NOW Rosemary Oil)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج زيت الروزماري من ناو مشكلة تساقط الشعر، الفراغات، ضعف البصيلات، وتشتت التركيز الذهني.</p>

<h3>لماذا تنجح تركيبة Pure Rosemary Essential Oil؟</h3>
<p>لأن مركب 1,8-Cineole في الروزماري النقي يوسع الأوعية الدموية بالدقيقة حول البصيلة مشابهاً لمفعول المينوكسيديل الطبيعي.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التخفيف دائماً بزيت ناقل (الجوجوبا أو اللوز):</strong> يمنع تهيج الفروة ويضمن الامتصاص.<br>
2. <strong>التدليك اللطيف 5 دقائق:</strong> ينشط تروية الدم لبصيلات الشعر.<br>
3. <strong>الاستخدام المنتظم 2-3 مرات أسبوعياً:</strong> يمنح نتائج تكثيف سريرية ملموسة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "يمكن وضع زيت الروزماري العطري مباشرة مركزاً على فروة الرأس."<br>
<strong>الحقيقة:</strong> زيوت NOW العطرية نقية ومكثفة 100% ويجب تخفيفها بزيت ناقل لتفادي الاحمرار والتهيج.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يحفز الروزماري عامل نمو الأعصاب (NGF) ويمنع أكسدة هرمون DHT المسبب للصلع الوراثي والتساقط.</p>"""

    faqs = [
        ("ما هو زيت إكليل الجبل العطري ( الروزماري ) ناو 30 مل؟", "هو زيت عطري نقي 100% مستخلص بالتقطير بالبخار من ناو فودز لتكثيف الشعر وإنبات الفراغات والعلاج العطري (30 مل)."),
        ("ما هي فوائد زيت الروزماري النقي للشعر وفروة الرأس؟", "يحفز إنبات البصيلات، يقلل التساقط، ينشط الدورة الدموية، ويقوي الشعر من الجذور."),
        ("هل يساعد في تكثيف الشعر ومنع التساقط من الاستخدام المنتظم؟", "نعم، مثبت سريرياً في تحفيز نمو الشعر وتكثيف البصيلات وتقليل التساقط."),
        ("ما حجم العبوة؟", "تأتي بعبوة زجاجية داكنة لحفظ الزيت سعة 30 مل."),
        ("كيف يُستخدم بالشكل الصحيح للشعر؟", "خففي 3-5 قطرات مع زيت ناقل، دلكي الفروة، اتركيه 30-60 دقيقة واغسلي بالشامبو 2-3 مرات أسبوعياً."),
        ("هل هو نقي 100% وخالٍ من المواد الكيميائية؟", "نعم، 100% زيت نقي مستخلص بالتقطير بالبخار دون أي إضافات."),
        ("أين صُنع زيت الروزماري من ناو؟", "صُنع في الولايات المتحدة الأمريكية بواسطة NOW Foods USA."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات ناو لدى إكليل أبها أصلية 100%."),
        ("ما رائحة زيت الروزماري؟", "عطر الروزماري العشبي المنعش المنشط الكلاسيكي."),
        ("هل يوضع مباشرة على الفروة أم يجب تخفيفه؟", "يجب تخفيفه دائماً بزيت ناقل كالجوجوبا أو اللوز قبل التطبيق على الفروة."),
        ("هل يناسب الفواحات العطرية والاستنشاق؟", "نعم، ممتاز للفواحات المائية لتصفية الذهن وتحسين التركيز."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الضوء والشمس."),
        ("هل ناو الماركة الأولى عالمياً في الزيوت العطرية؟", "نعم، NOW Solutions الماركة الأكثر شهرة وتفضصيلاً عالمياً في الزيوت النقية."),
        ("كم مرة أسبوعياً؟", "2 إلى 3 مرات أسبوعياً للشعر."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال لعلاج التساقط والتكثيف."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في تنقية فروة الرأس من القشرة؟", "نعم، يمتلك خواص مطهرة تنقي الفروة وتقلل القشرة."),
        ("هل يترك الشعر قوياً ومشرقاً؟", "نعم، يقوي ألياف الشعر ويمنحها مظهراً صحياً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يسبب تساقطاً في البداية؟", "لا يسبب تساقطاً، بل يسرع دخول البصيلات في مرحلة النمو (Anagen)."),
        ("هل يناسب جميع أنواع الشعر؟", "نعم، مناسب لجميع أنواع الشعر والفروة."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج طبيعي فاخر وأساسي لكل روتين عناية بالشعر."),
        ("هل يعيد الكثافة والحيوية للفراغات؟", "نعم، يساعد في إنبات الفراغات وتغذيتها."),
        ("هل تتوفر زيوت ناو النقية الأخرى؟", "نعم، تتوفر عائلة NOW Essential Oils كاملة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>NOW Rosemary Essential Oil - 30 ml</strong> is an authentic 100% pure steam-distilled therapeutic essential oil from NOW Foods designed to stimulate hair growth, nourish follicles, improve scalp blood circulation, and sharpen mental focus. Built upon 100% pure steam-distilled <em>Rosmarinus Officinalis</em> leaf oil.</p>
<p>NOW Rosemary Oil, when diluted with a carrier oil, revitalizes scalp tissue, reduces hair shedding, fuels weak roots, and provides an invigorating herbal aromatherapy experience, leaving your hair thicker, stronger, and your scalp thoroughly clarified from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Pure & Steam-Distilled:</strong> Premier global quality certified pure essential oil.</li>
  <li><strong>Hair Growth & Follicle Stimulation:</strong> Reduces hair shedding and promotes hair density.</li>
  <li><strong>Scalp Micro-Circulation Boosting:</strong> Delivers oxygen and vital nutrients to hair roots.</li>
  <li><strong>Aromatherapy Mental Focus & Clarity:</strong> Sharpens memory and concentration when diffused.</li>
  <li><strong>World-Famous NOW Solutions Quality:</strong> Most recommended essential oil brand globally.</li>
  <li><strong>Compact 30ml Amber Glass Bottle:</strong> UV-protective glass bottle with internal dropper.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> For Hair Care: Dilute 3-5 drops of NOW Rosemary oil with 1 tablespoon of a carrier oil (Jojoba or Argan).</li>
  <li><strong>Step 2:</strong> Massage gently into scalp using fingertips, leave for 30-60 minutes, then shampoo out.</li>
  <li><strong>Step 3:</strong> For Aromatherapy: Add 3-5 drops to a water diffuser and enjoy fresh herbal clarity (use 2-3 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>100% Pure Rosemary Leaf Oil (Rosmarinus Officinalis):</strong> Rich in 1,8-cineole and alpha-pinene stimulating hair follicles.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hair/scalp and aromatherapy use only; never ingest or apply undiluted to skin.</li>
  <li>Avoid direct contact with eyes; perform a patch test prior to full scalp application.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from sunlight.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking NOW Rosemary Essential Oil 30ml for hair thickening, hair loss control, and mental clarity aromatherapy.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>NOW Solutions (NOW Foods)</td></tr>
  <tr><th>Category</th><td>Hair & Body Care / NOW 100% Pure Essential Oils 30ml</td></tr>
  <tr><th>Product Type</th><td>100% Pure Steam-Distilled Rosemary Essential Oil (30ml)</td></tr>
  <tr><th>Volume/Weight</th><td>30 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Scalp & Hair Types (Specifically Thinning & Shedding Hair)</td></tr>
  <tr><th>Finish</th><td>Thicker hair, reinforced follicles & energized healthy clarified scalp</td></tr>
  <tr><th>Texture</th><td>Concentrated aromatic liquid oil absorbing smoothly when diluted</td></tr>
  <tr><th>Fragrance</th><td>Crisp fresh herbal natural Rosemary fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>100% Pure Rosmarinus Officinalis Leaf Oil</td></tr>
  <tr><th>Country of Origin</th><td>USA</td></tr>
  <tr><th>Manufacturer</th><td>NOW Foods USA</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 1,8-Cineole Vasodilation & Follicular Anagen Phase Induction</h2>

<h3>What problem does this solve?</h3>
<p>NOW Rosemary Essential Oil resolves hair loss, thinning areas, weak hair follicles, and mental fatigue.</p>

<h3>Why choose NOW Pure Rosemary Oil?</h3>
<p>Steam-distilled 1,8-Cineole dilates micro-capillaries around hair follicles matching natural growth stimulation.</p>"""

    en_faqs = [
        ("What is NOW Rosemary Essential Oil - 30 ml?", "It is a 100% pure steam-distilled essential oil from NOW Foods for hair growth, scalp stimulation, and aromatherapy (30ml)."),
        ("What are the benefits of pure Rosemary oil for hair and scalp?", "Stimulates hair growth, reduces shedding, boosts micro-circulation, and reinforces hair roots."),
        ("Does it help thicken hair and reduce hair loss with regular use?", "Yes, clinically proven to stimulate hair growth and improve hair density and strength."),
        ("What volume is contained in this bottle?", "30ml amber UV-protective glass bottle."),
        ("How do I use it correctly for hair?", "Dilute 3-5 drops in a carrier oil, massage scalp, leave 30-60 minutes and shampoo out 2-3 times weekly."),
        ("Is it 100% pure and chemical-free?", "Yes, 100% pure steam-distilled oil with zero synthetic additives."),
        ("Where is NOW Rosemary Oil manufactured?", "In the USA by NOW Foods."),
        ("How do I verify authenticity at Ekleel Abha?", "All NOW products at Ekleel Abha are 100% original."),
        ("What scent does Rosemary oil have?", "Crisp fresh herbal natural Rosemary fragrance."),
        ("Should it be applied directly or diluted?", "Always dilute with a carrier oil like Jojoba or Argan before scalp application."),
        ("Is it suitable for diffusers and aromatherapy?", "Yes, excellent for water diffusers to improve focus and mental clarity."),
        ("How should I store it?", "In a cool, dry place away from direct light."),
        ("Is NOW a #1 global essential oil brand?", "Yes, NOW Solutions is the world's most recognized premier pure essential oil brand."),
        ("How many times weekly?", "2 to 3 times weekly for hair routines."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help clarify dandruff from scalp?", "Yes, natural purifying properties clarify scalp reducing dandruff."),
        ("Does it leave hair strong and shiny?", "Yes, reinforces hair fibers giving a healthy vibrant look."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it cause initial hair loss?", "No, accelerates follicle entry into the active growth (Anagen) phase."),
        ("Is it good for all hair types?", "Yes, suitable for all hair and scalp types."),
        ("Is it a nice hair care gift?", "Yes, a premier natural essential for holistic hair routines."),
        ("Does it restore thickness to thinning areas?", "Yes, helps nourish and restore density to thinning hair zones."),
        ("Are other NOW essential oils available?", "Yes, the full NOW Essential Oils range is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2091",
        "sku": "EK-2091",
        "gtin": "733739147981",
        "brand": "NOW Solutions",
        "ar": {
            "title": "زيت إكليل الجبل العطري ( الروزماري ) ناو 30 مل",
            "meta_title": "زيت الروزماري النقي من ناو 30مل | إكليل أبها",
            "meta_description": "اشتري زيت إكليل الجبل العطري (الروزماري) من ناو (30 مل). زيت نقي 100% مصفى بالتقطير لتكثير وتغذية الشعر وإنبات الفراغات. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["ناو", "زيت_الروزماري_ناو", "زيت_إكليل_الجبل", "تكثيف_الشعر", "إكليل_أبها"]
        },
        "en": {
            "title": "NOW Rosemary Essential Oil - 30 ml",
            "meta_title": "NOW Rosemary Essential Oil 30ml | Ekleel Abha",
            "meta_description": "Buy original NOW Rosemary Essential Oil (30ml). 100% pure steam-distilled hair growth and scalp essential oil. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["now_solutions", "rosemary_essential_oil", "now_rosemary_oil", "hair_growth_oil", "ekleel_abha"]
        }
    }


def create_product_2092():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>زيت الجوجوبا نقي 100% من ناو 118 مل (NOW Solutions 100% Pure Jojoba Oil - 118 ml)</strong> الزيت العضوي الناقل الفاخر الأكثر توصية وشهرة عالمياً من ناو فودز (NOW Foods) المصمم خصيصاً لترطيب، تغذية، وإعادة التوازن لبشرة الوجه، الجسم، والشعر دون التسبب في أي انسداد للمسام أو لزوجة دهنية. يرتكز هذا الزيت الأصيل (NOW Jojoba Oil 118ml) على زيت شجيرة الجوجوبا النقي 100% المستخلص بالكبس على البارد من بذور <em>Simmondsia Chinensis</em>.</p>
<p>يمتاز زيت الجوجوبا من ناو بمطابقته الشديدة لتركيبة الدهون الطبيعية (Sebum) التي تفرزها البشرة، مما يتيح له النفاذ السريع لعمق الخلايا، ترميم حاجز الجلد المتضرر، تغذية أطراف الشعر الجافة، وتنظيم الإفرازات الدهنية، ليترك وجهك وشعرك وجسمك في غاية النعومة والترطيب والنضارة من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>نقي 100% ومستخلص بالكبس على البارد (100% Pure & Cold-Pressed):</strong> يحافظ على كامل المغذيات والفيتامينات.</li>
  <li><strong>مطابق لدهون البشرة الطبيعية (Sebum-Mimicking):</strong> ينفذ فورياً دون ترك لزوجة أو انسداد للمسام.</li>
  <li><strong>ترطيب وتغذية فائقة للوجه والجسم والشعر:</strong> يعالج الجفاف والتقشر والخشونة.</li>
  <li><strong>مثالي كزيت ناقل لتخفيف الزيوت العطرية (مثل الروزماري):</strong> يضاعف امتصاص وتغذية البصيلات.</li>
  <li><strong>تغذية وتنعيم الشعر المتقصف والجاف:</strong> يمنح الشعر لمعاناً وطراوة حريرية.</li>
  <li><strong>عبوة سعة 118 مل بحجم مالي ممتاز:</strong> تكفي لروتين العناية الشامل اليومي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> للوجه والجسم: ضعي قطرات قليلة على البشرة النظيفة ودلكي برفق حتى الامتصاص.</li>
  <li><strong>الخطوة الثانية:</strong> للشعر: وزعي قطرات على أطراف الشعر الجافة أو دلكي به الفروة كحمام زيت مرطب.</li>
  <li><strong>الخطوة الثالثة:</strong> كزيت ناقل: اخلطي ملعقة من الجوجوبا مع 3-5 قطرات من زيت عطري (يُستعمل يومياً وعند الحاجة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الجوجوبا النقي 100% (Simmondsia Chinensis Seed Oil):</strong> غني بالأحماض الدهنية وفيتامينات E و B المركبة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على البشرة والشعر فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن زيت الجوجوبا النقي 100% من ناو 118 مل لترطيب الوجه والشعر والجسم والاستخدام كزيت ناقل.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ناو / ناو فودز (NOW Solutions)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة والشعر / الزيوت المغذية والناقلة النقية 118ml</td></tr>
  <tr><th>نوع المنتج</th><td>زيت الجوجوبا نقي 100% معصور على البارد للوجه والجسم والشعر (118ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>118 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة والشعر (خصيصاً البشرة الجافة، الحساسة، والشعر المتقصف)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة وشعر ناعمين كالحرير، مرطبين 24 ساعة ومفعمين بالتوهج الطبيعي دون دهنية</td></tr>
  <tr><th>الملمس</th><td>زيت مرطب خفيف الامتصاص يطابق الدهون الطبيعية للجلد</td></tr>
  <tr><th>العطر</th><td>عطر خفيف طبيعي جداً محايد</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت بذور الجوجوبا النقي 100% (Simmondsia Chinensis)</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة الأمريكية (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>NOW Foods USA</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد استبدال الدهون بـ زيت الجوجوبا النقي (NOW Jojoba Oil)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج زيت الجوجوبا من ناو مشكلة جفاف الوجه والجسم، تقصف أطراف الشعر، والحاجة لزيت ناقل خفيف آمن.</p>

<h3>لماذا تنجح تركيبة Pure Cold-Pressed Jojoba Oil؟</h3>
<p>لأن الجوجوبا عبارة عن شمع سائل مطاطي يطابق الكيمياء الحيوية لزهم البشرة (Sebum) مما يمنع انسداد المسام.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على وجه رطب بعد الغسيل:</strong> يحبس الترطيب ويعيد النضارة الفورية.<br>
2. <strong>الاستخدام كزيت ناقل لـ زيت الروزماري:</strong> يضمن وصول زيت الروزماري العطري للبصيلات بأمان.<br>
3. <strong>الاستخدام اليومي لأطراف الشعر:</strong> يحمي من التقصف والتكسر.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "زيوت الترطيب تسبب ظهور الحبوب للبشرة الدهنية."<br>
<strong>الحقيقة:</strong> زيت الجوجوبا ينظم الإفرازات الدهنية الذاتية ويمتص فورياً دون تسبيب حبوب أو انسداد.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>ترتبط الإسترات الشمعية بغشاء الجلد الدهني موازنة إنتاج الغدد الزهمية دون أي أثر دهني لزج.</p>"""

    faqs = [
        ("ما هو زيت الجوجوبا نقي 100% من ناو 118 مل؟", "هو زيت عضوي نقي 100% معصور على البارد من ناو فودز لترطيب الوجه والشعر والجسم وكزيت ناقل (118 مل)."),
        ("ما هي فوائد زيت الجوجوبا النقي للبشرة والشعر؟", "يطابق دهون البشرة الطبيعية، يمتص فورياً، يرطب الوجه والشعر والجسم، ويغذي الأطراف المتشققة."),
        ("هل يمتص فورياً ويرطب بدون لزوجة أو انسداد للمسام؟", "نعم، مثبت سريرياً في الامتصاص السريع والمطابقة التامة لزهم البشرة دون تسبيب انسداد."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة سعة 118 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي قطرات على الوجه أو الشعر أو الجسم ودلكي برفق حتى الامتصاص يومياً وعند الحاجة."),
        ("هل هو خالٍ من المواد الكيميائية والزيوت المعدنية؟", "نعم، 100% زيت نقي نقي معصور على البارد خالي من الإضافات."),
        ("أين صُنع زيت الجوجوبا من ناو؟", "صُنع في الولايات المتحدة الأمريكية بواسطة NOW Foods USA."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات ناو لدى إكليل أبها أصلية 100%."),
        ("هل يناسب الاستخدام كزيت ناقل للزيوت العطرية؟", "نعم، التخفيف به ممتاز جداً لخلطه مع زيت الروزماري والزيوت العطرية."),
        ("هل يترك ملمساً ناعماً وغير دهني؟", "نعم، يمتص فورياً ليترك البشرة والشعر ناعمين دون أي دهنية لزجة."),
        ("هل عبوة 118 مل مناسبة للحقيبة والسفر؟", "نعم، عبوة أنيقة مدمجة مثالية للحقيبة والسفر والتنقل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل ناو الماركة الأولى عالمياً في الزيوت النقية؟", "نعم، NOW Solutions الماركة العالمية الأكثر ثقة وتفضصيلاً في الزيوت الطبيعية."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً أو حسب الحاجة."),
        ("هل يناسب جميع أنواع البشرة؟", "نعم، ممتاز للبشرة الجافة، العادية، الحساسة وحتى الدهنية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في حماية أطراف الشعر من التقصف؟", "نعم، ينعم أطراف الشعر ويحميها من الجفاف والتقصف."),
        ("هل يزيل المكياج بفاعلية؟", "نعم، ينظف مكياج الوجه والعينين بلطف وأمان تام."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال والأطفال؟", "نعم، آمن وممتاز للجميع من سن 3 سنوات."),
        ("هل يناسب الشتاء والصيف؟", "نعم، مرطب طبيعي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج طبيعي فاخر وأساسي لكل روتين عناية."),
        ("هل يعيد المظهر المشرق الناعم للبشرة والشعر؟", "نعم، يمنح البشرة والشعر مظهراً ناعماً ومشرقاً."),
        ("هل تتوفر الزيوت الناقلة الأخرى من ناو؟", "نعم، تتوفر عائلة NOW Carrier Oils كاملة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>NOW Solutions 100% Pure Jojoba Oil - 118 ml</strong> is the world's most recommended authentic 100% pure cold-pressed organic carrier oil from NOW Foods designed to hydrate, nourish, and rebalance facial, body, and hair skin without clogging pores or leaving greasy weight. Built upon 100% pure cold-pressed oil derived from <em>Simmondsia Chinensis</em> shrub seeds.</p>
<p>NOW Jojoba Oil mimics the natural sebum chemistry produced by skin glands, allowing it to penetrate deeply, rebuild damaged skin barriers, nourish dry hair ends, and regulate oiliness, leaving your face, hair, and body touchably silky soft, deeply hydrated, and radiant from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Pure & Cold-Pressed:</strong> Retains full natural nutrients, fatty acids, and vitamins.</li>
  <li><strong>Sebum-Mimicking Fast Absorption:</strong> Penetrates rapidly with zero greasy residue or pore clogging.</li>
  <li><strong>Superior Hydration for Face, Body & Hair:</strong> Treats dryness, flaking, and split hair ends.</li>
  <li><strong>Ideal Carrier Oil for Essential Oil Dilution (e.g. Rosemary):</strong> Maximizes nutrient delivery to follicles.</li>
  <li><strong>Hair Split-End Softening & Shine Boost:</strong> Delivers natural silky hair smoothness and luster.</li>
  <li><strong>Generous 118ml Value Bottle:</strong> Excellent size for daily comprehensive skincare routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> For Face & Body: Apply a few drops onto clean skin and massage gently until absorbed.</li>
  <li><strong>Step 2:</strong> For Hair: Smooth drops through dry hair ends or massage into scalp as a pre-shampoo treatment.</li>
  <li><strong>Step 3:</strong> As a Carrier Oil: Mix 1 tablespoon of Jojoba oil with 3-5 drops of an essential oil (use daily as needed).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>100% Pure Jojoba Seed Oil (Simmondsia Chinensis):</strong> Rich in essential fatty acids and Vitamins E and B-complex.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical skin and hair application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking NOW Solutions 100% Pure Jojoba Oil 118ml for face, body, and hair hydration and essential oil dilution.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>NOW Solutions (NOW Foods)</td></tr>
  <tr><th>Category</th><td>Skincare / NOW 100% Pure Carrier & Hydrating Oils 118ml</td></tr>
  <tr><th>Product Type</th><td>100% Pure Cold-Pressed Sebum-Mimicking Jojoba Oil (118ml)</td></tr>
  <tr><th>Volume/Weight</th><td>118 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin & Hair Types (Dry, Sensitive, Oily & Damaged Hair)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, nourished & non-greasy clear skin and hair</td></tr>
  <tr><th>Texture</th><td>Lightweight fast-absorbing golden fluid oil</td></tr>
  <tr><th>Fragrance</th><td>100% Natural mild neutral scent</td></tr>
  <tr><th>Active Ingredients</th><td>100% Pure Simmondsia Chinensis (Jojoba) Seed Oil</td></tr>
  <tr><th>Country of Origin</th><td>USA</td></tr>
  <tr><th>Manufacturer</th><td>NOW Foods USA</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 3+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Sebum-Mimicking Wax Esters & Barrier Lipid Integration</h2>

<h3>What problem does this solve?</h3>
<p>NOW Pure Jojoba Oil resolves facial dryness, hair split ends, skin flaking, and the need for a safe light carrier oil.</p>

<h3>Why choose NOW Pure Jojoba Oil?</h3>
<p>Cold-pressed liquid wax esters mimic human skin sebum chemistry nourishing cells without clogging pores.</p>"""

    en_faqs = [
        ("What is NOW Solutions 100% Pure Jojoba Oil - 118 ml?", "It is a 100% pure cold-pressed organic carrier oil from NOW Foods for face, body, and hair hydration (118ml)."),
        ("What are the benefits of pure Jojoba oil for skin and hair?", "Mimics natural skin sebum, absorbs rapidly, hydrates face, body, and hair, and nourishes dry split ends."),
        ("Does it absorb instantly and hydrate without greasiness or clogged pores?", "Yes, clinically proven to absorb rapidly and match skin sebum without clogging pores."),
        ("What volume is contained in this bottle?", "118ml compact value bottle."),
        ("How do I use it correctly?", "Apply drops to face, body, or hair ends and massage gently daily as needed."),
        ("Is it pure and chemical-free?", "Yes, 100% pure cold-pressed oil free from synthetic additives."),
        ("Where is NOW Jojoba Oil manufactured?", "In the USA by NOW Foods."),
        ("How do I verify authenticity at Ekleel Abha?", "All NOW products at Ekleel Abha are 100% original."),
        ("Is it great as a carrier oil for essential oils?", "Yes, excellent for diluting essential oils like Rosemary before scalp application."),
        ("Does it leave a soft non-greasy feel?", "Yes, absorbs instantly leaving skin and hair touchably soft without greasiness."),
        ("Is the 118ml bottle travel friendly?", "Yes, sleek compact bottle ideal for handbag and travel."),
        ("How should I store it?", "In a cool, dry place away from direct light."),
        ("Is NOW a #1 global pure oil brand?", "Yes, NOW Solutions is the world's most trusted brand in pure natural oils."),
        ("How many times daily?", "Once or twice daily or as needed."),
        ("Is it suitable for all skin types?", "Yes, suitable for dry, normal, sensitive, and oily skin."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help protect hair ends from split ends?", "Yes, smooths hair ends protecting against dryness and splitting."),
        ("Does it make a good gentle makeup remover?", "Yes, gently cleanses facial and eye makeup safely."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men, women, and kids?", "Yes, safe and suitable for everyone aged 3+."),
        ("Is it good for all seasons?", "Yes, ideal natural moisturizer for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, a premier natural essential for skincare routines."),
        ("Does it restore smooth radiant skin and hair?", "Yes, gives skin and hair a healthy smooth radiant look."),
        ("Are other NOW carrier oils available?", "Yes, the full NOW Carrier Oils range is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2092",
        "sku": "EK-2092",
        "gtin": "733739077172",
        "brand": "NOW Solutions",
        "ar": {
            "title": "زيت الجوجوبا نقي 100%  من ناو 118 مل",
            "meta_title": "زيت الجوجوبا النقي من ناو 118مل | إكليل أبها",
            "meta_description": "اشتري زيت الجوجوبا نقي 100% من ناو (118 مل). زيت عضوي معصور على البارد للوجه والجسم والشعر والتخفيف كزيت ناقل. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["ناو", "زيت_الجوجوبا_ناو", "زيت_ناقل", "ترطيب_الوجه_والشعر", "إكليل_أبها"]
        },
        "en": {
            "title": "NOW Solutions 100% Pure Jojoba Oil - 118 ml",
            "meta_title": "NOW Solutions 100% Pure Jojoba Oil 118ml | Ekleel Abha",
            "meta_description": "Buy original NOW Solutions 100% Pure Jojoba Oil (118ml). Cold-pressed face, body, and hair hydrating carrier oil. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["now_solutions", "jojoba_oil", "pure_jojoba_oil", "carrier_oil", "ekleel_abha"]
        }
    }


def create_product_2093():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>صابونية بياض الثلج 500جم (Snow White Body Soap - 500g)</strong> خلطة الصابونية الطبيعية المفتحة والمبيضة الفاخرة للأستحمام والجسم المصممة خصيصاً لتفتيح وتوحيد لون بشرة الجسم والتخلص من التصبغات، البقع الداكنة، وتراكمات الجلد الميت والخشونة. تركز هذه الصابونية الأصيلة (Snow White Soap 500g) على مجمع خلاصات الأعشاب المغربية والزيوت المبيضة، فيتامين C، والنياسيناميد.</p>
<p>تعمل صابونية بياض الثلج على تقشير وتصفية مسام الجسم، إزالة الطبقات الداكنة والجلد الجاف، وتزويد الجسم بنضارة ونعومة فائقة، لتترك بشرتك ناعمة كالحرير، ناصعة البياض، موحدة اللون، ومفعمة بالانتعاش والنظافة من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وتوحيد لون بشرة الجسم كبياض الثلج:</strong> تزيل التصبغات والبقع الداكنة.</li>
  <li><strong>تقشير وتصفية الشوائب والجلد الميت:</strong> تنظف مسام الجسم بفاعلية ونعومة.</li>
  <li><strong>ترطيب وتنعيم فائق لبشرة الجسم:</strong> يمنع الجفاف وشعور الشد بعد الاستحمام.</li>
  <li><strong>تحسين ملمس البشرة وإعادة التوهج والجمال:</strong> تمنح الجسم إشراقة ناصعة.</li>
  <li><strong>تركيبة طبيعية غنية بالأعشاب والزيوت المغذية:</strong> آمنة ومختبرة لجميع أنواع البشرة.</li>
  <li><strong>عبوة ضخمة سعة 500 جم:</strong> حجم ممتاز للاستخدام اليومي المستمر وحمامات المغربي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الجسم بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي كمية سخية من صابونية بياض الثلج على الجسم وافركي برفق بالليفة المغربية أو الناعمة.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركي الرغوة 5-10 دقائق ثم اشطفي جيداً بالماء (يُستعمل 2-3 مرات أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصات الأعشاب المفتحة وفيتامين C:</strong> تقضي على التصبغات وتفتح المناطق الداكنة.</li>
  <li><strong>الزيوت النباتية والمنظفات الصابونية الطبيعية:</strong> تنظف الجسم وتحفظ الرطوبة الداخلية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين والوجه الحساس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن صابونية بياض الثلج 500 جم لتفتيح وتوحيد لون الجسم والتخلص من التصبغات.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بياض الثلج (Snow White Beauty)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / الصابونيات المغربية وخلطات التفتيح 500g</td></tr>
  <tr><th>نوع المنتج</th><td>خلطة صابونية مغربية مبيضة ومفتحة ومقشرة للجسم (500g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (خصيصاً المتصبغة والداكنة والجافة)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، موحد اللون، ناصع البياض ومفعم بالنظافة والإشراق</td></tr>
  <tr><th>الملمس</th><td>معجون صابوني كريمي غني ينقلب لرغوة تنظيف ناعمة</td></tr>
  <tr><th>العطر</th><td>عطر الصابونيات المغربية العشبي الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصات أعشاب التفتيح المغربية، فيتامين C، زيوت مبيضة</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / المغرب</td></tr>
  <tr><th>الشركة المصنعة</th><td>Snow White Cosmetics Inc.</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد خلطة الأعشاب المغربية في صابونية بياض الثلج (Snow White Soap)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج صابونية بياض الثلج مشكلة تصبغات الجسم، عدم توحد اللون، تضرر البشرة بالشمس، وتراكم الجلد الميت.</p>

<h3>لماذا تنجح تركيبة Snow White Herbal Soap?</h3>
<p>لأن الأعشاب المغربية المبيضة تفكك الروابط بين الخلايا الميتة الملونة بينما يثبط فيتامين C تكوّن الميلانين.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على جسم دافئ بالبخار:</strong> يفتح المسام ويضاعف امتصاص خلاصات التفتيح.<br>
2. <strong>الفرك بالليفة المغربية برفق:</strong> يزيل القشور الداكنة بفعالية.<br>
3. <strong>الترطيب بـ لوشن مرطب بعد الشطف:</strong> يحفظ ليونة ونعومة البشرة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الصابونيات تسبب جفافاً شديداً وحكة بالجلد."<br>
<strong>الحقيقة:</strong> صابونية بياض الثلج مدعمة بالزيوت النباتية المرطبة التي تحفظ طراوة الجلد أثناء التنظيف.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تقشر الأحماض العشبية الطبقة الكيراتينية السطحية مظهرة خلايا فتية ناصعة البياض وموحدة.</p>"""

    faqs = [
        ("ما هي صابونية بياض الثلج 500جم؟", "هي خلطة صابونية مغربية مبيضة ومفتحة ومقشرة للجسم بالأعشاب الطبيعية وفيتامين C بحجم 500 جم."),
        ("ما هي فوائد خلاصة الأعشاب المغربية وفيتامين C للجسم؟", "تزيل التصبغات والبقع الداكنة، تقشر الجلد الميت، ووفوت وحد لون البشرة لتصبح كبياض الثلج."),
        ("هل تفتح وتوحد لون الجسم وتزيل التصبغات؟", "نعم، مثبتة في تفتيح وتوحيد لون بشرة الجسم وتصفية الشوائب الداكنة."),
        ("ما حجم العبوة؟", "تأتي بعبوة ضخمة بسعة 500 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي على جسم مبلل دافئ، افركي بالليفة المغربية، اتركيه 5-10 دقائق واشطفي 2-3 مرات أسبوعياً."),
        ("هل هي آمنة ومصنوعة من أعشاب طبيعية؟", "نعم، 100% آمنة ومصنوعة من خلاصات أعشاب وزيوت مرطبة خالية من المواد الضارة."),
        ("أين صُنعت صابونية بياض الثلج؟", "صُنع وفق أعلى معايير الخلطات الصابونية العنايتية بـ KSA والمغرب."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات بياض الثلج لدى إكليل أبها أصلية 100%."),
        ("ما رائحة صابونية بياض الثلج؟", "عطر الصابونيات المغربية العشبي المنعش الفاخر."),
        ("هل تناسب جميع مناطق الجسم الداكنة؟", "نعم، ممتازة لتفتيح وتوحيد الجسم والرقبة والكوعين والركبتين."),
        ("هل عبوة 500 جم تكفي لفترة جيدة؟", "نعم، عبوة ضخمة تكفي لعدة أشهر من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل هي الخلطة الصابونية الأكثر طلبًا للتفتيح؟", "نعم، صابونية بياض الثلج الخيار الأكثر شهيرة وتفضيلاً لتفتيح الجسم."),
        ("كم مرة أسبوعياً؟", "2 إلى 3 مرات أسبوعياً أثناء الاستحمام."),
        ("هل تنشطف بالماء بسهولة؟", "نعم، تنشطف بالماء الدافئ بسهولة دون أثر لزج."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يفضل استخدام لوشن مرطب بعدها؟", "نعم، يُفضل استخدام لوشن مرطب بعد الشطف لحفظ الطراوة."),
        ("هل تترك البشرة ناعمة كالحرير؟", "نعم، تترك بشرة الجسم في غاية النعومة والنظافة الحريرية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتازة للنساء والرجال."),
        ("هل يناسب جميع فصول السنة؟", "نعم، ممتاز للصيف والشتاء وحمامات البخار."),
        ("هل يصلح هدية ممتازة ضمن العناية؟", "نعم، منتج عناية وتفتيح مغربي فاخر ومفيد جداً."),
        ("هل يعيد المظهر الناصع المشرق للبشرة؟", "نعم، يمنح الجسد مظهراً ناصع البياض والإشراق."),
        ("هل يناسب العرائس قبل الزفاف؟", "نعم، خيار أسطوري أساسي للعرائس لتفتيح وتوحيد الجسم."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Snow White Body Soap - 500g</strong> is an authentic luxury Moroccan whitening, brightening, and exfoliating body soap paste designed to unify body skin tone, lighten dark spots, and remove dead skin cell accumulation and roughness. Built upon Moroccan herbal extracts, whitening oil complexes, Vitamin C, and Niacinamide.</p>
<p>Snow White Body Soap exfoliates and clarifies body pores, sweeps away dark surface layers and dry skin, and infuses body skin with radiant smoothness, leaving your skin touchably silky soft, visibly whitened, even-toned, and refreshed from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Snow White Skin Whitening & Tone Evening:</strong> Fades hyperpigmentation and dark spots across the body.</li>
  <li><strong>Exfoliates & Clarifies Dead Skin Cells:</strong> Purifies body skin pores effectively and gently.</li>
  <li><strong>Superior Body Softening & Hydration:</strong> Prevents post-shower dryness and tight feeling.</li>
  <li><strong>Skin Texture Improvement & Radiance Restoration:</strong> Delivers an illuminated healthy skin glow.</li>
  <li><strong>Natural Formula Rich in Botanical Herbs & Oils:</strong> Safe and tested for all skin types.</li>
  <li><strong>Generous 500g Value Tub Container:</strong> Excellent format for regular use and Moroccan bath rituals.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet body skin with warm water during shower or steam bath.</li>
  <li><strong>Step 2:</strong> Spread a generous layer of Snow White soap paste over body and scrub gently with a loofah.</li>
  <li><strong>Step 3:</strong> Leave lather on for 5-10 minutes, then rinse thoroughly with water (use 2-3 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Moroccan Herbal Extracts & Vitamin C:</strong> Eliminate hyperpigmentation and brighten dark zones.</li>
  <li><strong>Plant Oils & Natural Soap Cleansers:</strong> Cleanse body while maintaining internal moisture balance.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application.</li>
  <li>Avoid direct contact with eyes and sensitive facial skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Any woman seeking Snow White Body Soap 500g for body whitening, tone evening, and dark spot removal.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Snow White Beauty</td></tr>
  <tr><th>Category</th><td>Body Care / Moroccan Soaps & Whitening Pastes 500g</td></tr>
  <tr><th>Product Type</th><td>Moroccan Whitening, Brightening & Exfoliating Body Soap Paste (500g)</td></tr>
  <tr><th>Volume/Weight</th><td>500 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Specifically Hyperpigmented, Dark & Dry Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, even-toned, snow-white brightened & radiant body skin</td></tr>
  <tr><th>Texture</th><td>Rich smooth foaming herbal soap paste</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh Moroccan herbal scent</td></tr>
  <tr><th>Active Ingredients</th><td>Moroccan Whitening Herbs, Vitamin C, Niacinamide, Botanical Oils</td></tr>
  <tr><th>Country of Origin</th><td>KSA / Morocco</td></tr>
  <tr><th>Manufacturer</th><td>Snow White Cosmetics Inc.</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Moroccan Botanical Exfoliation & Vitamin C Depigmentation</h2>

<h3>What problem does this solve?</h3>
<p>Snow White Body Soap resolves body hyperpigmentation, uneven skin tone, sun damage, and dead skin cell buildup.</p>

<h3>Why choose Snow White Herbal Soap?</h3>
<p>Moroccan herbal acids break down colored surface desmosomes while Vitamin C inhibits ongoing melanin synthesis.</p>"""

    en_faqs = [
        ("What is Snow White Body Soap - 500g?", "It is a luxury Moroccan whitening, brightening, and exfoliating body soap paste with natural herbs and Vitamin C (500g)."),
        ("What are the benefits of Moroccan herbal extracts and Vitamin C?", "Fade dark spots and hyperpigmentation, exfoliate dead skin, and even body tone to a snow-white finish."),
        ("Does it brighten body skin and remove dark spots effectively?", "Yes, proven to brighten body skin tone, even discoloration, and sweep away dark surface layers."),
        ("What volume is contained in this tub?", "500g jumbo tub."),
        ("How do I use it correctly?", "Apply to wet warm skin, scrub with a loofah, leave 5-10 minutes and rinse 2-3 times weekly."),
        ("Is it safe and made from natural herbs?", "Yes, 100% safe, formulated with natural herbal extracts and moisturizing oils."),
        ("Where is Snow White Soap manufactured?", "Manufactured to international Moroccan bath quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Snow White products at Ekleel Abha are 100% original."),
        ("What scent does Snow White Soap have?", "Luxurious fresh Moroccan herbal fragrance."),
        ("Is it suitable for dark body zones?", "Yes, excellent for brightening dark body zones, neck, knees, and elbows."),
        ("Does the 500g tub last long?", "Yes, jumbo tub lasts months of regular use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it a famous whitening soap paste?", "Yes, Snow White is a famous premier choice in body whitening soap pastes."),
        ("How many times weekly?", "2 to 3 times weekly during showers or baths."),
        ("Does it rinse off easily?", "Yes, rinses off smoothly with warm water without sticky residue."),
        ("Is the container recyclable?", "Yes."),
        ("Is applying a body lotion recommended afterwards?", "Yes, follow with a hydrating lotion after rinsing to seal in moisture."),
        ("Does it leave skin touchably silky soft?", "Yes, leaves body skin silky soft, clear, and spotlessly clean."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it good for all seasons?", "Yes, excellent for summer, winter, and steam bath routines."),
        ("Is it a nice skincare gift?", "Yes, an elegant practical Moroccan body whitening gift."),
        ("Does it restore bright radiant skin appearance?", "Yes, gives body skin a bright snow-white radiant look."),
        ("Is it ideal for brides before weddings?", "Yes, an essential legendary preparation choice for brides for body whitening."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2093",
        "sku": "EK-2093",
        "gtin": "2781214011959",
        "brand": "Snow White Beauty",
        "ar": {
            "title": "صابونية بياض الثلج  500جم",
            "meta_title": "صابونية بياض الثلج لتفتيح الجسم 500جم | إكليل أبها",
            "meta_description": "اشتري صابونية بياض الثلج لتفتيح الجسم (500 جم). خلطة صابونية مغربية بالأعشاب وفيتامين C لتفتيح وتوحيد لون البشرة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["صابونية_بياض_الثلج", "تفتيح_الجسم_المغربي", "صابون_تفتيح_البشرة", "خلطة_بياض_الثلج", "إكليل_أبها"]
        },
        "en": {
            "title": "Snow White Body Soap - 500g",
            "meta_title": "Snow White Body Soap Whitening 500g | Ekleel Abha",
            "meta_description": "Buy original Snow White Body Soap (500g). Moroccan herbal whitening, brightening, and exfoliating body soap paste. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["snow_white_soap", "moroccan_whitening_soap", "body_whitening_soap", "snow_white_paste", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 74 builders complete")
