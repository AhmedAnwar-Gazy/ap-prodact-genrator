import json, os

def _make_cofix_wash_b69(pid, gtin, ar_name, en_name, key_ing_ar, key_ing_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> مستحضر التنظيف والعناية الفاخر الأصيل من كوفيكس المصمم خصيصاً لتنظيف، مطهرة، وترطيب بشرة الجسم أو المناطق الحميمة دون أي جفاف أو تهيج. يرتكز هذا الغسول الأصيل ({en_name}) على خلاصات {key_ing_ar}، المنظفات اللطيفة متوازنة الحموضة، والمركبات المهدئة للبشرة.</p>
<p>يعمل غسول كوفيكس على تنظيف مسام البشرة عمقاً، القضاء على البكتيريا والفطريات والروائح غير المرغوبة، وحفظ التوازن الطبيعي ورطوبة الجلد، ليترك بشرتك ناعمة كالحرير، مطهرة، ناصعة النظافة، ومفعمة بالانتعاش من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف وتطهير فائق لـ 24 ساعة بـ {key_ing_ar}:</strong> ينظف المسام والبشرة بلطف وأمان.</li>
  <li><strong>حماية ممتدة من البكتيريا والفطريات والروائح:</strong> يمنح شعوراً طازجاً بالانتعاش والنظافة.</li>
  <li><strong>تركيبة متوازنة الحموضة (pH Balanced) مهدئة:</strong> تحافظ على البيئة الطبيعية للجلد.</li>
  <li><strong>رغوة غنية كريمية ينشطف بالماء بسهولة:</strong> لا تترك أي ترسبات لزجة أو جفاف.</li>
  <li><strong>مختبر جلدياً وآمن للاستخدام اليومي:</strong> خالي من المواد القاسية والصبغات الضارة.</li>
  <li><strong>عبوة سعة 400ml/215ml مزودة بضاغط مريح:</strong> حجم ممتاز للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الجسم أو المنطقة الحميمة بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من غسول كوفيكس وكوّني رغوة ناعمة ودلكي برفق.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء وجففي البشرة برفق (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصات {key_ing_ar} والمكونات المطهرة:</strong> تمنح البشرة نضارة وتصفي الشوائب والبكتيريا.</li>
  <li><strong>المركبات المائية متوازنة الحموضة:</strong> تحفظ التوازن البيولوجي والترطيب الطبيعي.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} للتنظيف والتطهير والانتعاش اليومي.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كوفيكس (Cofix Care)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / غسولات كوفيكس المعطرة والحميمة 400ml/215ml</td></tr>
  <tr><th>نوع المنتج</th><td>غسول تنظيف وتطهير للجسم/المناطق الحميمة بـ {key_ing_ar}</td></tr>
  <tr><th>الحجم/الوزن</th><td>400 مل / 215 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (العادية، الجافة، والحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة مطهرة، ناعمة كالحرير، ناصعة النظافة ومفعمة بالانتعاش 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>جل سائل شفاف رغوي لطيف</td></tr>
  <tr><th>العطر</th><td>عطر {key_ing_ar} المنعش الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصات {key_ing_ar}، منظفات متوازنة pH، مركبات مهدئة</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية (KSA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Cofix Care Products</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد خلاصات {key_ing_ar} في غسولات كوفيكس (Cofix Washes)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول كوفيكس مشكلة تراكم البكتيريا والفطريات، الروائح غير المرغوبة، والجفاف والتهيج الجلدي.</p>

<h3>لماذا تنجح تركيبة Cofix pH-Balanced?</h3>
<p>لأن التركيبة متوازنة الحموضة تقضي على الميكروبات الضارة مع الحفاظ على الفلورا الجلدية النافعة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام اليومي بماء دافئ أثناء الاستحمام:</strong> ينظف ويطهر المسام بانتظام.<br>
2. <strong>الشطف الجيد بالماء:</strong> يضمن عدم بقاء ترسبات صابونية.<br>
3. <strong>التجفيف اللطف بمنشفة قطنية:</strong> يمنع نمو البكتيريا بفعل الرطوبة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الغسولات المطهرة تسبب الجفاف والتحسس."<br>
<strong>الحقيقة:</strong> غسولات كوفيكس مدعمة بمركبات مرطبة مهدئة تحفظ طراوة الجلد ونعومته.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخفض المنظفات اللطيفة التوتر السطحي للماء وتزيل الإفرازات الزهمية مع حماية الغشاء المخاطي.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو غسول تنظيف وتطهير للجسم أو المناطق الحميمة من كوفيكس بـ {key_ing_ar}."),
        (f"ما هي فوائد خلاصة {key_ing_ar} والتركيبة متوازنة الحموضة؟", "تنظف وتطهر البشرة، تقضي على البكتيريا والروائح، وتحفظ الترطيب الطبيعي."),
        ("هل يطهر البشرة ويزيل الروائح دون جفاف؟", "نعم، مثبت سريرياً في التطهير والسيطرة على الروائح ومنع الجفاف."),
        (f"ما حجم العبوة؟", "تأتي بعبوة أنيقة بضاغط مريح سعة 400 مل أو 215 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على بشرة مبللة، دلكي برفق برغوة ناعمة واشطفي بالماء يومياً."),
        ("هل هو آمن ومتوازن الحموضة (pH Balanced)؟", "نعم، 100% آمن ومتوازن الحموضة ومختبر جلدياً."),
        (f"أين صُنع غسول كوفيكس؟", "صُنع في المملكة العربية السعودية بواسطة Cofix Care Products."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كوفيكس لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {key_ing_ar} المنعش الفاخر."),
        ("هل يناسب الاستخدام اليومي لجميع أنواع البشرة؟", "نعم، ممتاز للاستخدام اليومي لجميع أنواع البشرة."),
        (f"هل العبوة تكفي لفترة جيدة؟", "نعم، تكفي لعدة أشهر من الاستخدام اليومي المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        (f"هل كوفيكس علامة موثوقة في العناية الشخصية؟", f"نعم، Cofix علامة سعودية رائدة وموثوقة جداً في المستحضرات الشخصية."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً أثناء الاستحمام."),
        ("هل يمنح رغوة غنية وينشطف بسهولة؟", "نعم، ينتج رغوة ناعمة ينشطف بالماء بسلاسة دون أثر لزج."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع تكون الفطريات والحكة؟", "نعم، يطهر البشرة ويمنع الفطريات والحكة المزعجة."),
        ("هل يترك ملمساً ناعماً؟", "نعم، يترك البشرة مرطبة ومصقولة بنعومة حريرية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للجميع حسب التخصص."),
        ("هل يناسب جميع فصول السنة؟", "نعم، ممتاز للصيف والشتاء والانتعاش اليومي."),
        ("هل يصلح هدية ممتازة؟", "نعم، منتج عناية مفيد وأنيق."),
        ("هل يعيد الشفافية والانتعاش للجلد؟", "نعم، يمنح الجسد مظهرًا مطهراً ومشرقاً."),
        ("هل الضاغط مريح جداً للاستخدام في الشاور؟", "نعم، ضاغط مريح يتيح الاستخدام السهل أثناء الاستحمام."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic luxury medical cleansing and purifying wash from Cofix designed to cleanse, purify, and moisturize body skin or intimate areas without dryness or irritation. Built upon {key_ing_en} extracts, pH-balanced mild cleansers, and skin-soothing compounds.</p>
<p>Cofix Cleansing Wash deeply purifies skin pores, eliminates unwanted bacteria, fungi, and odors, and maintains natural skin moisture balance, leaving your skin touchably silky soft, purified, spotlessly clean, and refreshed from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>24-Hour Superior Cleansing & Purifying with {key_ing_en}:</strong> Cleanses pores and skin gently and safely.</li>
  <li><strong>Extended Protection Against Bacteria, Fungi & Odors:</strong> Delivers a fresh clean feeling of vibrancy.</li>
  <li><strong>pH-Balanced Soothing Formula:</strong> Preserves the natural biological environment of the skin.</li>
  <li><strong>Rich Creamy Lather Rinsing Easily:</strong> Leaves zero sticky residue or dry tightness.</li>
  <li><strong>Dermatologically Tested Safe Daily Wash:</strong> Free from harsh chemicals and artificial dyes.</li>
  <li><strong>Convenient 400ml/215ml Pump Bottle:</strong> Excellent format for daily family bath routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet body or intimate skin with warm water during shower.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of Cofix wash, work into a soft lather, and massage gently.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with water and pat skin dry (use daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>{key_ing_en} Extracts & Purifying Agents:</strong> Impart radiant clarity while eliminating impurities and bacteria.</li>
  <li><strong>pH-Balanced Aqueous Solution:</strong> Preserves biological skin balance and natural hydration.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical application only.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for daily cleansing, purifying, and fragrant refreshment.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Cofix</td></tr>
  <tr><th>Category</th><td>Body Care / Cofix Fragranced & Intimate Washes 400ml/215ml</td></tr>
  <tr><th>Product Type</th><td>Body/Intimate Cleansing & Purifying Wash with {key_ing_en}</td></tr>
  <tr><th>Volume/Weight</th><td>400 ml / 215 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Normal, Dry & Sensitive)</td></tr>
  <tr><th>Finish</th><td>Purified, silky soft, spotlessly clean & 24H refreshed skin</td></tr>
  <tr><th>Texture</th><td>Clear fast-foaming lightweight gel liquid</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh {key_ing_en} fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>{key_ing_en} Extracts, pH-Balanced Cleansers, Soothing Agents</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia (KSA)</td></tr>
  <tr><th>Manufacturer</th><td>Cofix Care Products</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of pH-Balanced Cleansing & Epidermal Microflora Protection</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves bacterial/fungal buildup, body odor, and skin irritation caused by harsh soaps.</p>

<h3>Why choose Cofix pH-Balanced Washes?</h3>
<p>The pH-balanced formula eliminates harmful microbes while preserving beneficial microflora and hydrolipid barriers.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a body or intimate cleansing and purifying wash from Cofix with {key_ing_en}."),
        (f"What are the benefits of {key_ing_en} extract and pH-balanced formula?", "Cleanse and purify skin, eliminate bacteria and odors, and maintain natural hydration."),
        ("Does it purify skin and eliminate odors without dryness?", "Yes, clinically proven to purify skin, control odors, and prevent dryness."),
        (f"What volume is contained in this bottle?", "400ml or 215ml convenient pump bottle."),
        ("How do I use it correctly?", "Apply to wet skin, massage gently into a soft lather, and rinse daily with water."),
        ("Is it safe and pH-balanced?", "Yes, 100% safe, pH-balanced, and dermatologically tested."),
        ("Where is Cofix Wash manufactured?", "In Saudi Arabia by Cofix Care Products."),
        ("How do I verify authenticity at Ekleel Abha?", "All Cofix products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", f"Luxurious fresh {key_ing_en} fragrance."),
        ("Is it suitable for daily use on all skin types?", "Yes, excellent for daily use on all skin types."),
        (f"Does the bottle last long?", "Yes, lasts months of regular daily bath use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Cofix a trusted brand in Saudi Arabia?", "Yes, Cofix is a leading trusted brand in personal care in KSA."),
        ("How many times daily?", "Once or twice daily during showers."),
        ("Does it yield a rich lather and rinse off easily?", "Yes, produces a smooth lather that rinses off smoothly without sticky residue."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it prevent fungal growth and itching?", "Yes, purifies skin preventing fungal growth and annoying itchiness."),
        ("Does it leave skin soft?", "Yes, leaves skin touchably soft and fragranced."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for everyone based on product type."),
        ("Is it good for all seasons?", "Yes, excellent for summer and winter care."),
        ("Is it a nice shower gift?", "Yes, practical and thoughtful personal care gift."),
        ("Does it restore clean radiant skin appearance?", "Yes, gives skin a healthy purified radiant look."),
        ("Is the pump bottle convenient for showering?", "Yes, convenient pump dispenser for easy shower use."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Cofix",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. غسول تنظيف وتطهير غير دهني للجسم والمناطق الحميمة بـ {key_ing_ar} من كوفيكس. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Cofix cleansing and purifying body/intimate wash with {key_ing_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2061():
    return _make_cofix_wash_b69(
        pid=2061, gtin="792625756591",
        ar_name="غسول الجسم بخلاصة الزهور من كوفيكس 400مل",
        en_name="Cofix Body Wash with Flower Extract - 400ml",
        key_ing_ar="خلاصة الزهور الفواحة والمنظفات اللطيفة", key_ing_en="Aromatic Flower Extracts & Mild Cleansers",
        feature_ar="سائل استحمام ترطيب وتنظيف عطري بخلاصة الزهور 400 مل", feature_en="hydrating perfumed flower extract body wash 400ml",
        tags_ar=["كوفيكس", "غسول_الزهور_كوفيكس", "سائل_استحمام_الزهور", "غسول_جسم_معطر", "إكليل_أبها"],
        tags_en=["cofix", "flower_body_wash", "cofix_flower_wash", "perfumed_body_wash", "ekleel_abha"]
    )


def create_product_2062():
    return _make_cofix_wash_b69(
        pid=2062, gtin="792625756508",
        ar_name="غسول الجسم بخلاصة التوت البري من كوفيكس 400مل",
        en_name="Cofix Cranberry Extract Body Wash - 400ml",
        key_ing_ar="خلاصة التوت البري (Cranberry) ومضادات الأكسدة", key_ing_en="Antioxidant Cranberry Extract",
        feature_ar="سائل استحمام مغذٍ ومنشط بخلاصة التوت البري 400 مل", feature_en="energizing antioxidant cranberry body wash 400ml",
        tags_ar=["كوفيكس", "غسول_التوت_البري_كوفيكس", "سائل_استحمام_التوت", "غسول_منشط", "إكليل_أبها"],
        tags_en=["cofix", "cranberry_body_wash", "cofix_cranberry", "energizing_wash", "ekleel_abha"]
    )


def create_product_2063():
    return _make_cofix_wash_b69(
        pid=2063, gtin="792625756607",
        ar_name="غسول نسائي مضاد للجراثيم والفطريات للمناطق الحميمة من كوفيكس 400مل",
        en_name="Cofix Antibacterial and Antifungal Intimate Wash for Women - 400ml",
        key_ing_ar="المركبات المضادة للجراثيم والفطريات وحمض اللاكتيك", key_ing_en="Antibacterial, Antifungal & Lactic Acid Complex",
        feature_ar="غسول نسائي طبي مطهر ومضاد للجراثيم والفطريات للمناطق الحميمة 400 مل", feature_en="antibacterial antifungal medical intimate wash for women 400ml",
        tags_ar=["كوفيكس", "غسول_نسائي_كوفيكس", "غسول_حميمي_مضاد_للفطريات", "العناية_الحميمة", "إكليل_أبها"],
        tags_en=["cofix", "intimate_wash_women", "antibacterial_intimate_wash", "cofix_intimate", "ekleel_abha"]
    )


def create_product_2064():
    return _make_cofix_wash_b69(
        pid=2064, gtin="792625756485",
        ar_name="غسول العناية اليومية للمناطق الحميمة بخلاصة الصبار من كوفيكس 215مل",
        en_name="Cofix Daily Intimate Care Wash with Aloe Vera Extract - 215ml",
        key_ing_ar="جل الصبار الطبيعي المهدئ وحمض اللاكتيك", key_ing_en="Soothing Aloe Vera Gel & Lactic Acid",
        feature_ar="غسول يومي لطيف ومهدئ للمناطق الحميمة بخلاصة الصبار 215 مل", feature_en="gentle soothing daily intimate wash with aloe vera 215ml",
        tags_ar=["كوفيكس", "غسول_الصبار_الحميمي", "العناية_اليومية_الحميمة", "غسول_كوفيكس_215مل", "إكليل_أبها"],
        tags_en=["cofix", "aloe_intimate_wash", "daily_intimate_care", "cofix_aloe_wash", "ekleel_abha"]
    )


def create_product_2065():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>لوشن ترطيب خالي من العطور الوجه والجسم من سيرافي 236مل (CeraVe Moisturizing Lotion for Face and Body - 236ml)</strong> لوشن الترطيب والترميم المكثف الطبي الفاخر الأكثر توصية عالمياً من سيرافي (CeraVe) المصمم خصيصاً لترطيب، تغذية، وإصلاح حاجز بشرة الوجه والجسم الجافة والعادية دون أي ثقل دهني أو انسداد للمسام. يرتكز هذا اللوشن الأصيل (CeraVe Lotion 236ml) على السيراميدات الثلاثية الأساسية (Ceramides 1, 3, 6-II)، حمض الهيالورونيك (Hyaluronic Acid)، وتقنية MVE المبتكرة لترطيب ممتد طوال 24 ساعة.</p>
<p>يعمل لوشن سيرافي الطبي على حبس رطوبة البشرة الداخلية، إعادة بناء غلاف الجلد الدهني المتضرر، وتهدئة الخشونة والجفاف، ليترك بشرة وجهك وجسمك ناعمة كالحرير، مرطبة عمقاً، صحية، ومحمية من الحساسية والجفاف طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتغدية ممتدة لـ 24 ساعة بتقنية MVE الثورية:</strong> يفرز جزيئات الترطيب بشكل مستمر طوال اليوم.</li>
  <li><strong>ترميم حاجز البشرة بالسيراميدات الثلاثية الأساسية:</strong> تعوض النقص في سيراميدات الجلد الطبيعية.</li>
  <li><strong>حبس الرطوبة بحمض الهيالورونيك:</strong> يجذب جزيئات الماء لعمق الخلايا القرنية.</li>
  <li><strong>تركيبة خفيفة خالية 100% من العطور والزيوت والبارابين:</strong> لا تسبب انسداد المسام (Non-Comedogenic).</li>
  <li><strong>موصى به من أطباء الجلدية ومناسب للوجه والجسم:</strong> لوشن العناية العائلية الشاملة.</li>
  <li><strong>عبوة سعة 236 مل مزودة بضاغط مريح:</strong> حجم ممتاز للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسية من لوشن سيرافي على بشرة الوجه والجسم النظيفة.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي برفق بحركات دائرية حتى الامتصاص الكامل (يُستعمل عند الحاجة ومرتين يومياً صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>السيراميدات 1 و 3 و 6-II:</strong> تطابق سيراميدات الجلد الطبيعية وتصلح الحجاب الوقائي.</li>
  <li><strong>حمض الهيالورونيك وتقنية MVE:</strong> يحبسان الرطوبة ويضمنان انبعاث ممتد للمغذيات طوال 24 ساعة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن لوشن سيرافي المرطب الخالي من العطور 236 مل لترطيب وتصفية الوجه والجسم.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سيرافي (CeraVe)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / لوشنات وكريمات سيرافي الطبية المرطبة 236ml</td></tr>
  <tr><th>نوع المنتج</th><td>لوشن مرطب طبي خالي من العطور بالسيراميدات وحمض الهيالورونيك للوجه والجسم (236ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>236 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الجافة، العادية، والمفرطة الحساسية (للوجه والجسم)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة كالحرير، مرطبة 24 ساعة، مشفية من الجفاف وخالية من الزيوت</td></tr>
  <tr><th>الملمس</th><td>لوشن سائل خفيف الوزن يمتص فورياً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>سيراميدات أساسية (1, 3, 6-II)، حمض الهيالورونيك، تقنية MVE</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا / الولايات المتحدة (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>CeraVe LLC (L'Oréal Group)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد السيراميدات الثلاثية وتقنية MVE في لوشن سيرافي (CeraVe Lotion)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج لوشن سيرافي مشكلة تضرر حاجز البشرة، الجفاف الشديد، الخشونة الناتجة عن نقص السيراميدات، والتهيجات.</p>

<h3>لماذا تنجح تقنية CeraVe MVE & Ceramides؟</h3>
<p>لأن السيراميدات 1 و 3 و 6-II تعوض 50% من سيراميدات الجلد الطبيعية بينما تطلق MVE الترطيب على مدار 24 ساعة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق فوراً بعد الغسل والاستحمام:</strong> يحبس الرطوبة المائية في الخلايا.<br>
2. <strong>التطبيق مرتين يومياً (صباحاً ومساءً):</strong> يحافظ على حماية واستقرار حاجز الجلد.<br>
3. <strong>الاستخدام الآمن تحت المكياج:</strong> امتصاصه الخفيف يجعله قاعدة مثالية للوجه.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "لوشنات الترطيب تسبب انسداد المسام وحبوب الوجه."<br>
<strong>الحقيقة:</strong> لوشن سيرافي خالي 100% من الزيوت والعطور وغير مسبب للانسداد (Non-Comedogenic).</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تندمج السيراميدات بالطبقة القرنية (Stratum Corneum) مصلحة الثقوب بين الخلوية ومستعادة حماية الجلد البيولوجية.</p>"""

    faqs = [
        ("ما هو لوشن ترطيب خالي من العطور الوجه والجسم من سيرافي 236مل؟", "هو لوشن مرطب طبي خالي من العطور والزيوت من سيرافي بالسيراميدات الهيالورونيك للوجه والجسم (236 مل)."),
        ("ما هي فوائد السيراميدات الثلاثية وحمض الهيالورونيك؟", "ترمم حاجز البشرة، تحبس الرطوبة لـ 24 ساعة، وتمنع الجفاف والخشونة."),
        ("هل يمتص فورياً ويرطب لـ 24 ساعة دون انسداد المسام؟", "نعم، مثبت سريرياً في الامتصاص السريع والترطيب 24 ساعة دون تسبيب انسداد المسام."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة مزودة بضاغط مريح سعة 236 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية مناسبة على بشرة الوجه والجسم ودلكي برفق حتى الامتصاص مرتين يومياً."),
        ("هل هو خالٍ من العطور والزيوت والبارابين؟", "نعم، 100% خالٍ من العطور والزيوت والبارابين ومختبر درماتولوجياً."),
        ("أين صُنع لوشن سيرافي؟", "صُنع بواسطة CeraVe LLC (مجموعة L'Oréal العالمية)."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات سيرافي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب الوجه والجسم معاً؟", "نعم، مرطب شامل فاخر مخصص لبشرة الوجه والجسم."),
        ("هل يترك ملمساً ناعماً وغير دهني؟", "نعم، يمتص فورياً ليترك البشرة ناعمة كالحرير دون دهنية."),
        ("هل عبوة 236 مل بضاغط مريحة؟", "نعم، عبوة أنيقة بضاغط مريح جداً للاستخدام اليومي والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل سيرافي الماركة الأولى الموصى بها من أطباء الجلدية؟", "نعم، CeraVe الماركة رقم 1 الموصى بها طبياً في ألميركا والعالم."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل يناسب البشرة الجافة والعادية والحساسة؟", "نعم، ممتاز للبشرة الجافة والعادية والمفرطة الحساسية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع تشقق وخشونة الجلد؟", "نعم، يزيل الخشونة ويحمي الجلد من التشققات والجفاف."),
        ("هل يصلح كقاعدة تحت المكياج؟", "نعم، قاعدة ممتازة للمكياج بفضل امطصاطه السريع وملمسه الخفيف."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء والاطفال؟", "نعم، آمن وممتاز للجميع من سن 12 سنة."),
        ("هل يناسب الشتاء والصيف؟", "نعم، ترطيب طبي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج طبي فاخر وأساسي لكل روتين عناية."),
        ("هل يعيد المظهر الصحي الناعم للبشرة؟", "نعم، يعيد النضارة والنعومة الطبيعية للبشرة."),
        ("هل تتوفر أحجام أخرى من لوشن سيرافي؟", "نعم، تتوفر أحجام متعددة لدى CeraVe."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>CeraVe Moisturizing Lotion for Face and Body - 236ml</strong> is the world's most dermatologist-recommended authentic luxury medical hydrating lotion from CeraVe engineered to hydrate, nourish, and repair the skin barrier for dry to normal facial and body skin without heavy oils or pore clogging. Built upon 3 Essential Ceramides (1, 3, 6-II), Hyaluronic Acid, and revolutionary MVE Technology for sustained 24-hour hydration.</p>
<p>CeraVe Medical Lotion locks in internal skin moisture, rebuilds the damaged protective lipid barrier, and calms roughness and dryness, leaving your facial and body skin touchably silky soft, deeply hydrated, healthy, and protected against sensitivity and dryness all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>24-Hour Sustained Hydration with MVE Technology:</strong> Continuously releases moisturizing ingredients throughout the day.</li>
  <li><strong>Skin Barrier Restoration with 3 Essential Ceramides:</strong> Replenishes 50% of skin's natural protective ceramides.</li>
  <li><strong>Internal Moisture Locking with Hyaluronic Acid:</strong> Draws water molecules deep into stratum corneum cells.</li>
  <li><strong>100% Fragrance-Free, Oil-Free & Paraben-Free:</strong> Non-comedogenic formula that will not clog pores.</li>
  <li><strong>Dermatologist Recommended for Face & Body:</strong> Comprehensive family medical hydration lotion.</li>
  <li><strong>Convenient 236ml Pump Dispenser Bottle:</strong> Ideal size for daily care and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of CeraVe lotion onto clean facial and body skin.</li>
  <li><strong>Step 2:</strong> Massage gently in smooth circular motions until fully absorbed (use as needed & twice daily morning and night).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Essential Ceramides 1, 3 & 6-II:</strong> Mimic natural skin ceramides repairing damaged skin barriers.</li>
  <li><strong>Hyaluronic Acid & MVE Technology:</strong> Lock in moisture providing controlled 24-hour hydration release.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and body skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking CeraVe Fragrance-Free Moisturizing Lotion 236ml for facial and body hydration and barrier repair.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>CeraVe</td></tr>
  <tr><th>Category</th><td>Skincare / CeraVe Medical Moisturizing Lotions 236ml</td></tr>
  <tr><th>Product Type</th><td>Fragrance-Free Oil-Free Ceramide & Hyaluronic Acid Face & Body Lotion (236ml)</td></tr>
  <tr><th>Volume/Weight</th><td>236 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Dry, Normal & Sensitive Skin (Face & Body)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, crack-healed & non-greasy clear skin</td></tr>
  <tr><th>Texture</th><td>Ultra-lightweight fast-absorbing smooth lotion</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>3 Essential Ceramides (1, 3, 6-II), Hyaluronic Acid, MVE Technology</td></tr>
  <tr><th>Country of Origin</th><td>France / USA</td></tr>
  <tr><th>Manufacturer</th><td>CeraVe LLC (L'Oréal Group)</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 3 Essential Ceramides & MVE Controlled-Release Technology</h2>

<h3>What problem does this solve?</h3>
<p>CeraVe Lotion resolves compromised skin barriers, severe skin dryness, roughness from ceramide deficiency, and irritation.</p>

<h3>Why choose CeraVe Lotion?</h3>
<p>Ceramides 1, 3, 6-II restore 50% of natural lipid bilayers while MVE technology provides continuous 24-hour hydration release.</p>"""

    en_faqs = [
        ("What is CeraVe Moisturizing Lotion for Face and Body - 236ml?", "It is a medical fragrance-free oil-free lotion from CeraVe with Ceramides and Hyaluronic Acid for face and body (236ml)."),
        ("What are the benefits of 3 essential Ceramides and Hyaluronic Acid?", "They restore skin barriers, lock in 24-hour hydration, and prevent dryness and roughness."),
        ("Does it absorb instantly and hydrate for 24 hours without clogging pores?", "Yes, clinically proven to absorb rapidly and hydrate for 24 hours without causing breakouts or clogged pores."),
        ("What volume is contained in this bottle?", "236ml pump dispenser bottle."),
        ("How do I use it correctly?", "Apply to clean facial and body skin, massage gently until absorbed twice daily."),
        ("Is it fragrance-free, oil-free, and paraben-free?", "Yes, 100% free from fragrances, oils, and parabens, and dermatologically tested."),
        ("Where is CeraVe Lotion manufactured?", "By CeraVe LLC (L'Oréal Group)."),
        ("How do I verify authenticity at Ekleel Abha?", "All CeraVe products at Ekleel Abha are 100% original."),
        ("Is it suitable for face and body together?", "Yes, versatile medical moisturizer for facial and body skin."),
        ("Does it leave a soft non-greasy feel?", "Yes, absorbs instantly leaving skin silky soft without greasiness."),
        ("Is the 236ml pump dispenser bottle convenient?", "Yes, sleek pump bottle ideal for daily care and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is CeraVe the #1 dermatologist recommended brand?", "Yes, CeraVe is the #1 dermatologist recommended moisturizer brand in the US and globally."),
        ("How many times daily?", "Twice daily (morning and night)."),
        ("Is it suitable for dry, normal, and sensitive skin?", "Yes, excellent for dry, normal, and sensitive skin types."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it prevent skin cracking and roughness?", "Yes, eliminates roughness and shields skin from cracking."),
        ("Does it serve as a good makeup base?", "Yes, excellent lightweight makeup base due to fast absorption."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, safe and suitable for everyone aged 12+."),
        ("Is it good for all seasons?", "Yes, ideal medical hydration for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, a premier medical essential for skincare routines."),
        ("Does it restore healthy smooth skin appearance?", "Yes, restores natural radiance and softness to skin."),
        ("Are larger sizes available from CeraVe?", "Yes, multiple sizes are available from CeraVe."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2065",
        "sku": "EK-2065",
        "gtin": "3337875597210",
        "brand": "CeraVe",
        "ar": {
            "title": "لوشن ترطيب خالي من العطور الوجه والجسم من سيرافي 236مل",
            "meta_title": "لوشن سيرافي المرطب للوجه والجسم 236مل | إكليل أبها",
            "meta_description": "اشتري لوشن ترطيب خالي من العطور للوجه والجسم من سيرافي (236 مل). لوشن طبي بالسيراميدات الهيالورونيك لترميم البشرة والترطيب 24 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["سيرافي", "لوشن_سيرافي", "ترطيب_الوجه_والجسم", "سيراميدات_سيرافي", "إكليل_أبها"]
        },
        "en": {
            "title": "CeraVe Moisturizing Lotion for Face and Body - 236ml",
            "meta_title": "CeraVe Moisturizing Lotion 236ml | Ekleel Abha",
            "meta_description": "Buy original CeraVe Moisturizing Lotion for Face and Body (236ml). Fragrance-free oil-free ceramide lotion. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["cerave", "cerave_lotion", "moisturizing_lotion", "ceramide_lotion", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 69 builders complete")
