import json, os

def _make_facial_cleanser_remover(pid, gtin, ar_name, en_name, ingredient_ar, ingredient_en, benefit_ar, benefit_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> مستحضر العناية المزدوج بالبشرة المبتكر المصمم لجمع عمليتين في خطوة واحدة: إزالة المكياج بالكامل وتنظيف بشرة الوجه بـ {ingredient_ar}. يرتكز هذا الغسول الفاخر ({en_name}) على خلاصة {ingredient_ar} المرطبة، المركبات المنظفة اللطيفة، والفيتامينات المغذية للبشرة.</p>
<p>يعمل هذا الغسول ومزيل المكياج على إذاية وإزالة المكياج المستعصي والمقاوم للماء من الوجه والعينين والشفتين، تنظيف المسام عمقاً من الأوساخ والدهون، و{benefit_ar}، ليترك وجهك نظيفاً تماماً، ناعماً، مرطباً، ومشرقاً دون أي جفاف أو لزوجة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>فعالية مزدوجة غسول ومزيل مكياج 2 في 1:</strong> يزيل المكياج وينظف البشرة بخطوة واحدة.</li>
  <li><strong>إزالة كاملة للمكياج المقاوم للماء:</strong> يذيب المكياج المستعصي دون فرك قاسٍ.</li>
  <li><strong>مدعم بخلاصة {ingredient_ar} الطبيعية:</strong> {benefit_ar} وتغذي طبقات الجلد.</li>
  <li><strong>تنظيف عميق للمسام دون جفاف:</strong> يحفظ حاجز الترطيب الطبيعي للبشرة.</li>
  <li><strong>لطيف وخالٍ من الكحول والزيوت الثقيلة:</strong> آمن ومناسب لجميع أنواع البشرة.</li>
  <li><strong>عبوة سعة 150 مل بمضخة رغوية أو سائلة:</strong> حجم وافر للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسبة من الغسول ومزيل المكياج على بشرة الوجه المبللة أو باستخدام قطنة ناعمة.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي برفق بحركات دائرية لإذابة المكياج والأوساخ من الوجه والعينين.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي الفم والوجه بالماء الفاتر جيداً (يُستعمل صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة {ingredient_ar} المركزة:</strong> {benefit_ar} وتمنح البشرة نضارة وحيوية.</li>
  <li><strong>مركبات تنظيف ميكروبية لطيفة:</strong> تذيب المكياج والزيوت دون تهيج البشرة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه فقط.</li>
  <li>في حال التلامس المباشر مع داخل العين اشطفي بالماء الفاتر.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لإزالة المكياج وتنظيف بشرة الوجه اليومي بخطوة واحدة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>العلامة التجارية المعتمدة</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / غسولات ومزيلات مكياج الوجه بـ {ingredient_ar} 150ml</td></tr>
  <tr><th>نوع المنتج</th><td>غسول وجه ومزيل مكياج 2 في 1 بخلاصة {ingredient_ar} (150ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>150 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (العادية، الجافة، الدهنية والحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه نظيف تماماً خالي من المكياج، مرطب ومشرق بخلاصة {ingredient_ar}</td></tr>
  <tr><th>الملمس</th><td>سائل غسول ناعم رغوي سريع الامتصاص</td></tr>
  <tr><th>العطر</th><td>عطر {ingredient_ar} الناعم المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة {ingredient_ar}، منظفات ميكروبية لطيفة، فيتامينات مغذية</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين (China)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beauty Care Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد خلاصة {ingredient_ar} في غسول ومزيل مكياج الوجه (150ml)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج هذا المستحضر المزدوج مشكلة تراكم المكياج المقاوم للماء، انسداد المسام بالدهون والأوساخ، وصعوبة التنظيف اليومي بخطوات متعددة.</p>

<h3>لماذا تنجح تركيبة {ingredient_ar} المزدوجة؟</h3>
<p>لأن المنظفات الميكروبية تذيب صبغات المكياج والزيوت فورياً بينما تعوض خلاصة {ingredient_ar} البشرة بالترطيب والتغذية الفورية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام المسائي لإزالة المكياج:</strong> تنظيف البشرة قبل النوم يمنع البثور.<br>
2. <strong>التدليك برفق دون فرك شديد:</strong> لحماية المنطقة الحساسة حول العينين.<br>
3. <strong>الشطف بالماء البارد بعد الغسل:</strong> ليغلق المسام النظيفة ويحبس الترطيب.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مزيلات المكياج المزدوجة تترك زيوتاً على الوجه."<br>
<strong>الحقيقة:</strong> هذا المستحضر ينظف وينشطف بالماء تماماً دون ترك أي أثر دهني لزج.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تكوّن المنظفات مذيبات ميكروية تحيط بجزيئات المكياج الزيتية وتذيبها، بينما تخترق خلاصة {ingredient_ar} الطبقة الشوكية لتغذية الخلايا.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو مستحضر مزدوج 2 في 1 لغسل الوجه وإزالة المكياج بخلاصة {ingredient_ar} لحجم 150 مل."),
        (f"ما هي فوائد خلاصة {ingredient_ar}؟", f"{benefit_ar} وتغذي طبقات الجلد وتمنح الوجه نضارة ورونقاً."),
        ("هل يزيل المكياج المقاوم للماء؟", "نعم، يذيب المكياج المستعصي والمقاوم للماء من الوجه والعينين دون فرك قاسٍ."),
        ("ما حجم العبوة؟", "تأتي بسعة 150 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي الكمية على الوجه المبلل، دلكي برفق لإذابة المكياج ثم اشطفي بالماء الفاتر مرتين يومياً."),
        ("هل هو خالي من الكحول والزيوت الثقيلة؟", "نعم، تركيبة لطيفة خالية من الكحول والزيوت الثقيلة."),
        ("أين صُنع؟", "صُنع في الصين بأعلى معايير جودة مستحضرات التجميل."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة مستحضر {ingredient_ar}؟", f"عطر {ingredient_ar} الناعم المنعش."),
        ("هل يناسب جميع أنواع البشرة؟", "نعم، مناسب للبشرة العادية، الجافة، الدهنية والحساسة."),
        ("هل 150 مل تكفي لفترة طويلة؟", "نعم، تكفي لعدة أشهر من الاستخدام اليومي المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب منطقة العينين والشفتين؟", "نعم، لطيف ومناسب لإزالة مكياج العينين والشفتين."),
        ("كم مرة يومياً؟", "صباحاً ومساءً."),
        ("هل يترك الوجه مرطباً وغير مشدود؟", "نعم، يحافظ على رطوبة الوجه دون شعور الشد أو الجفاف."),
        ("هل يساعد في منع البثور والكوميدونات؟", "نعم، تنظيف المسام العميق يمنع انسدادها وتكون البثور."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يترك أثراً دهنياً بعد الغسل؟", "لا، ينشطف بالماء تماماً دون أثر دهني."),
        ("هل يصلح للمسافرين؟", "نعم، حجم 150 مل ممتاز للسفر."),
        ("هل يوفر الوقت والجهد في الروتين؟", "نعم، يجمع إزالة المكياج وغسول الوجه في خطوة واحدة."),
        ("هل يناسب المراهقين والبالغين؟", "نعم، مناسب من 12 سنة فما فوق."),
        ("هل يجفف البشرة الحساسة؟", "لا، خلاصة المرطب الطبيعي تمنع الجفاف والتهيج."),
        ("هل يصلح هدية لطيفة؟", "نعم، منتج عملي ومفيد لكل امرأة."),
        ("هل ينظف المسام من الأتربة اليومية؟", "نعم، يزيل المكياج والأتربة والزيوت اليومية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an innovative dual-action 2-in-1 facial skincare product designed to combine makeup removal and facial cleansing infused with {ingredient_en}. Formulated with hydrating {ingredient_en} extract, gentle cleansing compounds, and skin-nourishing vitamins.</p>
<p>This face wash and makeup remover dissolves stubborn and waterproof makeup from face, eyes, and lips, deeply cleanses pores of impurities and excess oil, and {benefit_en}, leaving your face spotlessly clean, soft, hydrated, and glowing without dryness or greasiness.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Dual-Action 2-in-1 Face Wash & Makeup Remover:</strong> Removes makeup and cleanses skin in one easy step.</li>
  <li><strong>Complete Waterproof Makeup Removal:</strong> Dissolves stubborn makeup without harsh rubbing.</li>
  <li><strong>Enriched with Natural {ingredient_en} Extract:</strong> {benefit_en} and nourishes deep skin layers.</li>
  <li><strong>Deep Pore Cleansing Without Dryness:</strong> Preserves skin's natural moisture barrier.</li>
  <li><strong>Gentle Alcohol-Free & Oil-Free Formula:</strong> Safe and suitable for all skin types.</li>
  <li><strong>Generous 150ml Bottle:</strong> Excellent volume for continuous daily care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount onto damp facial skin or a soft cotton pad.</li>
  <li><strong>Step 2:</strong> Massage gently in circular motions to dissolve makeup and impurities.</li>
  <li><strong>Step 3:</strong> Rinse face thoroughly with warm water (use morning and evening).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Concentrated {ingredient_en} Extract:</strong> {benefit_en} imparting natural facial radiance and freshness.</li>
  <li><strong>Gentle Micellar Cleansing Compounds:</strong> Dissolve makeup and oils without causing skin irritation.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial skin application only.</li>
  <li>Rinse with warm water if direct contact inside eyes occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for daily 2-in-1 makeup removal and facial skin cleansing.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Certified Beauty Brand</td></tr>
  <tr><th>Category</th><td>Skincare / {ingredient_en} Facial Washes & Makeup Removers 150ml</td></tr>
  <tr><th>Product Type</th><td>2-in-1 {ingredient_en} Facial Cleanser & Makeup Remover (150ml)</td></tr>
  <tr><th>Volume/Weight</th><td>150 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Normal, Dry, Oily & Sensitive)</td></tr>
  <tr><th>Finish</th><td>Spotlessly clean, makeup-free, hydrated & radiant facial skin</td></tr>
  <tr><th>Texture</th><td>Smooth gentle foaming liquid wash</td></tr>
  <tr><th>Fragrance</th><td>Gentle refreshing {ingredient_en} aroma</td></tr>
  <tr><th>Active Ingredients</th><td>{ingredient_en} Extract, Gentle Micellar Cleansers, Vitamins</td></tr>
  <tr><th>Country of Origin</th><td>China</td></tr>
  <tr><th>Manufacturer</th><td>Beauty Care Laboratories</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of {ingredient_en} Extract Hydration & Micellar Makeup Dissolution</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves stubborn waterproof makeup accumulation, pore clogging, and multi-step cleansing hassle.</p>

<h3>Why choose this 2-in-1 formula?</h3>
<p>Micellar cleansers encapsulate and lift oil-based makeup pigments instantly while concentrated {ingredient_en} extract replenishes skin moisture barrier.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a 2-in-1 facial cleanser and makeup remover infused with {ingredient_en} in 150ml."),
        (f"What are the benefits of {ingredient_en} extract?", f"{benefit_en} and nourishes skin layers giving a radiant face glow."),
        ("Does it remove waterproof makeup?", "Yes, dissolves stubborn and waterproof makeup from face, eyes, and lips without harsh rubbing."),
        ("What volume is contained in this bottle?", "150ml."),
        ("How do I use it correctly?", "Apply on damp face, massage gently to dissolve makeup, rinse with warm water twice daily."),
        ("Is it alcohol-free and oil-free?", "Yes, gentle alcohol-free and oil-free formula."),
        ("Where is it manufactured?", "In China to highest cosmetics quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original."),
        (f"What does the {ingredient_en} product smell like?", f"Gentle refreshing natural {ingredient_en} aroma."),
        ("Is it suitable for all skin types?", "Yes, suitable for normal, dry, oily, and sensitive skin."),
        ("Does the 150ml bottle last long?", "Yes, lasts months of regular daily use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for eye and lip makeup?", "Yes, gentle and suitable for eye and lip makeup removal."),
        ("How many times daily?", "Morning and evening."),
        ("Does it leave skin hydrated and not tight?", "Yes, preserves skin moisture without tightness or dryness."),
        ("Does it help prevent breakouts?", "Yes, deep pore cleansing prevents clogging and breakout formation."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it leave a greasy residue?", "No, rinses off completely clean without greasy residue."),
        ("Is it travel friendly?", "Yes, 150ml size suitable for travel."),
        ("Does it save time in daily routine?", "Yes, combines makeup removal and face washing in one step."),
        ("Is it suitable for teens and adults?", "Yes, ages 12+."),
        ("Does it dry sensitive skin?", "No, natural extract prevents dryness and irritation."),
        ("Is it a nice practical gift?", "Yes, practical and thoughtful gift for any woman."),
        ("Does it clean daily pollution and dirt?", "Yes, cleans makeup, dirt, and daily oil accumulation."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Beauty Care",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. غسول وجه ومزيل مكياج 2 في 1 ينظف ويرطب البشرة بخلاصة {ingredient_ar}. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. 2-in-1 facial cleanser and makeup remover infused with {ingredient_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1917():
    return _make_facial_cleanser_remover(
        pid=1917, gtin="6972662282947",
        ar_name="غسول وجه  ومزيل مكياجبالالوفيرا 150مل",
        en_name="Aloe vera face wash and makeup remover 150ml",
        ingredient_ar="الألوفيرا (الصبار)", ingredient_en="Aloe Vera",
        benefit_ar="تهدئ وترطب وتلطف البشرة المتهيجة", benefit_en="soothes, hydrates, and calms irritated skin",
        tags_ar=["غسول_الوفيرا", "مزيل_مكياج_صبار", "ترطيب_البشرة", "غسول_2في1", "إكليل_أبها"],
        tags_en=["aloe_vera_wash", "makeup_remover_aloe", "skin_soothing", "2in1_cleanser", "ekleel_abha"]
    )


def create_product_1918():
    return _make_facial_cleanser_remover(
        pid=1918, gtin="6972662282909",
        ar_name="مزيل مكياج وغسول وجه بالورد 150مل",
        en_name="Rose Makeup Remover & Face Wash 150ml",
        ingredient_ar="الورد الجوري الطبيعي", ingredient_en="Rose Extract",
        benefit_ar="تنعش وتورد وتوحد لون الوجه", benefit_en="refreshes, tones, and unifies facial skin tone",
        tags_ar=["غسول_الورد", "مزيل_مكياج_ورد", "تنعيم_الوجه", "غسول_2في1", "إكليل_أبها"],
        tags_en=["rose_face_wash", "rose_makeup_remover", "skin_toning", "2in1_cleanser", "ekleel_abha"]
    )


def create_product_1919():
    return _make_facial_cleanser_remover(
        pid=1919, gtin="6972662282923",
        ar_name="مزيل مكياج وغسول وجه بفيتامين سي  150مل",
        en_name="Vitamin C Makeup Remover & Face Wash - 150ml",
        ingredient_ar="فيتامين C المجدد", ingredient_en="Vitamin C",
        benefit_ar="تفتح وتضفي إشراقة وتوهجاً استثنائياً للوجه", benefit_en="brightens, renews, and imparts extraordinary face radiance",
        tags_ar=["غسول_فيتامين_سي", "مزيل_مكياج_فيتامين_سي", "تبييض_البشرة", "غسول_2في1", "إكليل_أبها"],
        tags_en=["vitamin_c_wash", "vitamin_c_remover", "skin_brightening", "2in1_cleanser", "ekleel_abha"]
    )


def _make_body_soap_scrub(pid, gtin, ar_name, en_name, ingredient_ar, ingredient_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> مقشر وصابون العناية بالجسم الفاخر الحجم المكثف (500 جم) المصنوع بتركيبة الحمام المغربي والسبا الفاخرة لتقشير وتنظيف وتفتيح بشرة الجسم بالكامل. يرتكز هذا المنتج الفاخر ({en_name}) على حبيبات المقشر الطبيعية الدقيقة، الصابون البلدي المعزز بـ {ingredient_ar}، والزيوت المرطبة المغذية.</p>
<p>يعمل صابون ومقشر الجسم على إزالة خلايا الجلد الميتة والتراكمات الجافة، تنظيف المسام العميقة للجسم، و{feature_ar}، ليترك جسمك ناعماً كالحرير، ناصع البياض، موحد اللون، ومعطراً برائحة السبا الفاخرة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تقشير وتنظيف فائق 2 في 1 بحبيبات طبيعية:</strong> يزيل خلايا الجلد الميتة ويكشف بشرة جديدة ناصعة.</li>
  <li><strong>تفتيح وتوحيد لون بشرة الجسم بـ {ingredient_ar}:</strong> {feature_ar} ويقضي على التصبغات.</li>
  <li><strong>تنعيم وترطيب عميق للجسم:</strong> يمنح الجلد ملمساً حريرياً دون جفاف.</li>
  <li><strong>تنظيف مسام الجسم وإزالة السموم:</strong> ينشط الدورة الدموية ويعيد الحيوية للجلد.</li>
  <li><strong>عبوة اقتصادية ضخمة سعة 500 جم:</strong> كمية وافرة تدوم عدة أشهر من الاستخدام المنتظم.</li>
  <li><strong>مثالي للاستخدام في الحمام المغربي والسبا المنزلي:</strong> تجربة عناية فاخرة في المنزل.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (البلل):</strong> بللي الجسم بالماء الدافئ لفتح مسام البشرة.</li>
  <li><strong>الخطوة الثانية (التطبيق والتدليك):</strong> ضعي كمية مناسبة من الصابون والمقشر ودلكي الجسم بحركات دائرية (يُفضل باستخدام الليفة المغربية).</li>
  <li><strong>الخطوة الثالثة (الشطف):</strong> اشطفي الجسم جيداً بالماء الدافئ (يُستعمل 1-2 مرة أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>حبيبات التقشير الطبيعية و{ingredient_ar}:</strong> تقشر الجلد الميت وتفتّح التصبغات الداكنة للجسم.</li>
  <li><strong>الصابون البلدي والزيوت المغذية:</strong> ينظفان المسام ويحفظان ترطيب الجلد ونعومته.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم فقط (لا يُستعمل للوجه).</li>
  <li>تجنبي الاستخدام على الجلد المصاب بجروح أو حروق.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لتقشير وتفتيح وتنظيف بشرة الجسم بتركيبة السبا 500 جم.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ليتل سيكرت / العلامة المعتمدة</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / مقشرات وصابونات الجسم الفاخرة بـ {ingredient_ar} 500g</td></tr>
  <tr><th>نوع المنتج</th><td>صابون ومقشر جسم 2 في 1 بـ {ingredient_ar} للتفتيح والتقشير (500g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (بما في ذلك البشرة ذات التصبغات والجافة)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، موحد اللون، ناصع البياض وخالٍ من التراكمات الجافة</td></tr>
  <tr><th>الملمس</th><td>معجون صابوني حبيبي ناعم غني بالزيوت</td></tr>
  <tr><th>العطر</th><td>عطر {ingredient_ar} الفاخر الشرقي</td></tr>
  <tr><th>المكونات النشطة</th><td>حبيبات تقشير طبيعية، {ingredient_ar}، صابون بلدي، زيوت مرطبة</td></tr>
  <tr><th>بلد المنشأ</th><td>المغرب / الإمارات العربية المتحدة</td></tr>
  <tr><th>الشركة المصنعة</th><td>Little Secret Body Care</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد تقشير الجسم وتفتيحه بـ {ingredient_ar} (500g)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج صابون ومقشر الجسم مشكلة تراكم خلايا الجلد الميتة، اسمرار وتصبغات مناطق الجسم (كالكوعين والركبتين)، وجفاف وخشونة الجلد.</p>

<h3>لماذا تنجح تركيبة المقشر والصابون بـ {ingredient_ar}؟</h3>
<p>لأن التقشير الميكانيكي يزيل طبقة الكيراتين الميتة فورياً بينما يثبط المركب النشط لـ {ingredient_ar} إنزيم التايروسينيز المسبب للتصبغات.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام 1-2 مرة أسبوعياً:</strong> التكرار المعتدل يضمن التجديد الخلوي دون تهيج.<br>
2. <strong>استخدام الليفة المغربية برفق:</strong> يعزز إزالة التراكمات والجلد الميت.<br>
3. <strong>الترطيب بزبادي أو زبدة الجسم بعد الاستحمام:</strong> يحبس الرطوبة ويضاعف نتائج النعومة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "التقشير القاسي يومياً يسرّع تفتيح البشرة."<br>
<strong>الحقيقة:</strong> التقشير القاسي اليومي يسبب التهاباً عكسياً يزيد التصبغات، بينما التقشير المعتدل 1-2 مرة أسبوعياً هو الصحيح.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تفكك جزيئات المقشر الطبيعي الروابط الدسموزومية (Desmosomes) بين خلايا الطبقة القرنية الميتة، مما يسهل سقوطها وتجدد الخلايا.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو صابون ومقشر جسم فاخر 2 في 1 بـ {ingredient_ar} بحجم ضخم 500 جم لتقشير وتفتيح وتنظيف الجسم."),
        (f"ما هي فوائد {ingredient_ar} والحبيبات الطبيعية؟", f"تقشر الحبيبات الجلد الميت والتراكمات، بينما {feature_ar} وتوحد لون الجسم."),
        ("هل يزيل التصبغات والجلد الميت؟", "نعم، يزيل خلايا الجلد الميتة والتصبغات الداكنة بفاعلية من الكوعين والركبتين وكامل الجسم."),
        ("ما وزن العبوة؟", "تأتي بعبوة ضخمة بوزن 500 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الجسم بالماء الدافئ، ضعي المقشر ودلكي بحركات دائرية بالليفة المغربية ثم اشطفي 1-2 مرة أسبوعياً."),
        ("هل يناسب جميع أنواع بشرة الجسم؟", "نعم، مناسب لجميع أنواع بشرة الجسم (بما في ذلك الجافة والمفتقرة للنضارة)."),
        ("أين صُنع صابون ومقشر الجسم؟", "صُنع في المغرب/الإمارات بواسطة Little Secret Body Care."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {ingredient_ar} الفاخر المنعش."),
        ("هل يترك الجسم ناعماً كالحرير؟", "نعم، يمنح البشرة ملمساً حريرياً ناعماً جداً من الاستخدام الأول."),
        ("هل 500 جم تدوم طويلاً؟", "نعم، عبوة ضخمة تكفي لعدة أشهر من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف محكم الإغلاق بعيداً عن الماء في الحمام."),
        ("هل يناسب الوجه؟", "مخصص لبشرة الجسم فقط ولا يُستعمل لبشرة الوجه الرقيقة."),
        ("كم مرة أسبوعياً؟", "1-2 مرة أسبوعياً للحصول على أفضل نتائج."),
        ("هل يساعد في شعر تحت الجلد (جلد الدجاجة)؟", "نعم، التقشير المنتظم يمنع انسداد المسام وشعر تحت الجلد."),
        ("هل ينشط الدورة الدموية؟", "نعم، التدليك بالليفة والمقشر ينشط الدورة الدموية ويمنح الجلد حيوية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب الاستخدام قبل التسمير (التان)؟", "نعم، يجهز البشرة لـ تان متجانس ومثالي."),
        ("هل يناسب الاستخدام في الحمام المغربي والسبا؟", "نعم، خيار مثالي للحمام المغربي والسبا المنزلي."),
        ("هل يمنح توحيداً فورياً للون الجسم؟", "يمنح نعومة وإشراقاً فورياً وتفتيحاً تدريجياً بالاستمرار."),
        ("هل يناسب النساء والرجال؟", "نعم، مناسب للنساء والرجال من 16 سنة."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، ينشطف بالماء الدافئ بسلاسة دون ترك أثر لزج."),
        ("هل يصلح هدية فاخرة للعرايس؟", "نعم، هدية فاخرة وممتازة جداً للعرايس والعناية بالبشرة."),
        ("هل يحافظ على ترطيب الجلد بعد الاستحمام؟", "نعم، الزيوت المرطبة تحفظ ترطيب الجلد ونعومته."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is a luxury 2-in-1 body soap and scrub in a generous 500g tub formulated with Moroccan hammam spa traditions to exfoliate, cleanse, and brighten body skin. Formulated with natural micro-exfoliating beads, traditional soap enriched with {ingredient_en}, and nourishing hydrating oils.</p>
<p>This body soap and scrub removes dead skin cells and dry buildup, deeply cleanses body pores, and {feature_en}, leaving your body touchably silky soft, visibly brightened, even-toned, and fragranced with luxury spa scent.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>2-in-1 Superior Exfoliation & Cleansing with Natural Beads:</strong> Sloughs off dead skin cells revealing fresh bright skin.</li>
  <li><strong>Body Skin Brightening & Tone Unification with {ingredient_en}:</strong> {feature_en} and targets dark hyperpigmentation.</li>
  <li><strong>Deep Softening & Body Hydration:</strong> Imparts a silky smooth touch without drying skin.</li>
  <li><strong>Body Pore Cleansing & Detoxification:</strong> Stimulates blood circulation reviving skin vitality.</li>
  <li><strong>Generous 500g Jumbo Tub:</strong> Abundant volume lasting months of regular use.</li>
  <li><strong>Ideal for Moroccan Hammam & Home Spa:</strong> Luxury spa care experience at home.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet body with warm water to open pores.</li>
  <li><strong>Step 2 (Apply & Massage):</strong> Apply a suitable amount of soap & scrub, massage in circular motions (preferably with a Kessa mitt).</li>
  <li><strong>Step 3 (Rinse):</strong> Rinse thoroughly with warm water (use 1-2 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Exfoliating Beads & {ingredient_en}:</strong> Exfoliate dead skin and brighten dark body hyperpigmentation.</li>
  <li><strong>Traditional Soap & Hydrating Oils:</strong> Cleanse pores while preserving skin moisture and softness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application only (do not use on face).</li>
  <li>Avoid using on broken, wounded, or burned skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for body exfoliation, brightening, and cleansing with 500g spa formula.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Little Secret / Certified Brand</td></tr>
  <tr><th>Category</th><td>Body Care / {ingredient_en} Luxury Body Soaps & Scrubs 500g</td></tr>
  <tr><th>Product Type</th><td>2-in-1 {ingredient_en} Body Exfoliating & Brightening Soap Scrub (500g)</td></tr>
  <tr><th>Volume/Weight</th><td>500 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Including Hyperpigmented & Dry Skin)</td></tr>
  <tr><th>Finish</th><td>Silky smooth, even-toned, brightened body skin free of dry buildup</td></tr>
  <tr><th>Texture</th><td>Smooth oil-rich granular soapy paste</td></tr>
  <tr><th>Fragrance</th><td>Luxury oriental {ingredient_en} scent</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Exfoliating Beads, {ingredient_en}, Traditional Soap, Hydrating Oils</td></tr>
  <tr><th>Country of Origin</th><td>Morocco / UAE</td></tr>
  <tr><th>Manufacturer</th><td>Little Secret Body Care</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of {ingredient_en} Melanin Suppression & Desmosome Mechanical Dissolution</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves dead skin buildup, body hyperpigmentation (elbows, knees), and skin roughness and dryness.</p>

<h3>Why choose this 2-in-1 Soap & Scrub?</h3>
<p>Mechanical exfoliation breaks desmosomal bonds between dead stratum corneum cells while {ingredient_en} inhibits tyrosinase activity reducing hyperpigmentation.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a luxury 2-in-1 body soap and scrub infused with {ingredient_en} in a jumbo 500g tub for body exfoliation, brightening, and cleansing."),
        (f"What are the benefits of {ingredient_en} and natural beads?", f"Exfoliating beads remove dead skin while {feature_en} and unify body tone."),
        ("Does it remove hyperpigmentation and dead skin?", "Yes, effectively removes dead skin cells and dark spots from elbows, knees, and full body."),
        ("What weight is contained in this tub?", "500g jumbo tub."),
        ("How do I use it correctly?", "Wet body with warm water, apply scrub, massage in circles with Kessa mitt, rinse 1-2 times weekly."),
        ("Is it suitable for all body skin types?", "Yes, suitable for all body skin types (including dry and dull skin)."),
        ("Where is this body scrub manufactured?", "In Morocco/UAE by Little Secret Body Care."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original."),
        (f"What does {en_name} smell like?", f"Luxury oriental {ingredient_en} scent."),
        ("Does it leave body silky smooth?", "Yes, imparts a touchably soft silky feel from first use."),
        ("Does 500g last long?", "Yes, jumbo tub lasts months of regular use."),
        ("How should I store it?", "In a cool, dry place tightly closed away from shower water."),
        ("Is it suitable for the face?", "Formulated for body skin only; do not use on delicate facial skin."),
        ("How many times weekly?", "1-2 times weekly for best results."),
        ("Does it help with strawberry legs / ingrown hair?", "Yes, regular exfoliation prevents clogged pores and ingrown hairs."),
        ("Does it stimulate blood circulation?", "Yes, massage with scrub and mitt invigorates blood circulation."),
        ("Is the tub recyclable?", "Yes."),
        ("Is it good before self-tanning?", "Yes, prepares skin for a smooth flawless self-tan application."),
        ("Is it suitable for Moroccan Hammam & Spa?", "Yes, perfect choice for Moroccan Hammam and home spa routines."),
        ("Does it give instant tone unification?", "Imparts instant smoothness and radiance with progressive brightening upon regular use."),
        ("Is it suitable for men and women?", "Yes, suitable for men and women aged 16+."),
        ("Does it rinse off easily?", "Yes, rinses smoothly with warm water without sticky residue."),
        ("Is it a luxury gift for brides?", "Yes, luxurious and practical gift for brides and body care routines."),
        ("Does it keep skin hydrated post-shower?", "Yes, moisturizing oils lock in skin hydration and softness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Little Secret",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. صابون ومقشر جسم 2 في 1 بـ 500 جم لتقشير وتفتيح وتنظيف الجسم بـ {ingredient_ar}. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. 2-in-1 body soap & scrub 500g for body exfoliation and brightening with {ingredient_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_1920():
    return _make_body_soap_scrub(
        pid=1920, gtin="745178721448",
        ar_name="صابون ومقشر الجسم  الليتل سيكرت 500جم",
        en_name="The Little Secret Body Soap & Scrub 500g",
        ingredient_ar="الخلطة السحرية للزيوت والأعشاب المغربية", ingredient_en="Secret Moroccan Herbs & Oils Blend",
        feature_ar="تفتح وتوحد لون الجسم وتمنحه نعومة فائقة", feature_en="brightens, unifies body skin tone, and imparts extreme softness",
        tags_ar=["الليتل_سيكرت", "مقشر_جسم", "صابون_مغربي", "تفتيح_الجسم", "إكليل_أبها"],
        tags_en=["little_secret", "body_scrub", "moroccan_soap", "body_brightening", "ekleel_abha"]
    )


def create_product_1921():
    return _make_body_soap_scrub(
        pid=1921, gtin="745178721424",
        ar_name="صابون ومقشر الجسم النيلة الزرقاء 500جم",
        en_name="Blue Nila Body Soap and Scrub 500g",
        ingredient_ar="مسحوق النيلة الزرقاء المغربية الأصيلة", ingredient_en="Authentic Moroccan Blue Nila Powder",
        feature_ar="تزيل التصبغات والبقع الداكنة وتمنح الجسم بياضاً ملكياً ناصعاً", feature_en="eliminates hyperpigmentation and imparts a royal bright white body glow",
        tags_ar=["النيلة_الزرقاء", "مقشر_النيلة", "تفتيح_النيلة", "صابون_النيلة", "إكليل_أبها"],
        tags_en=["blue_nila", "nila_scrub", "nila_brightening", "nila_soap", "ekleel_abha"]
    )


print("Loaded all 5 Batch 41 builders complete")
