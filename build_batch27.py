import json, os

def build_beesline_deo(prod_id, title_ar, title_en, frag_ar, frag_en, benefit_ar, benefit_en, pack_str_ar, pack_str_en, gtin, img_slug):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{title_ar}</strong> مستحضر العناية الطبية الطبيعي المبتكر الأكثر مبيعاً في الشرق الأوسط لتفتيح منطقة الإبطين وتأمين حماية مضادة للتعرق تدوم لـ 48 ساعة متواصلة. يرتكز هذا المزيل الفريد من بيزلين (Beesline Whitening Roll-On Deodorant) على توليفة صمغ النحل (Propolis)، حجر الشبة النقي (Alum Rock)، ومركب اللوميسكين الطبيعي (Lumiskin) مع عبير {frag_ar}.</p>
<p>يمتاز رول اون بيزلين بتركيبة طبيعية 100% آمنة على البشرة الحساسة، حيث يعمل على تأخير نمو الشعر غير المرغوب فيه، تفتيح التصبغات والداكنة تحت الإبط، وتوفير جفاف وانتعاش مطلق دون التسبب في انسداد مسام الجلد أو بقع الملابس.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية 48 ساعة مضادة للتعرق والرائحة:</strong> يمتص العرق ويمنع تكون البكتيريا المسببة للرائحة الكريهة.</li>
  <li><strong>تفتيح طبيعي لمنطقة تحت الإبط (Lumiskin):</strong> يزيل البقع الداكنة والتصبغات ويجمع لون البشرة.</li>
  <li><strong>معزز بصمغ النحل وحجر الشبة:</strong> مطهر طبيعي يقضي على الجراثيم ويرمم خلايا الجلد المجهدة.</li>
  <li><strong>تأخير نمو الشعر وتلطيف البشرة:</strong> يهدئ الحكة ويحمي منطقة الإبط الرقيقة بعد الحلاقة.</li>
  <li><strong>خالي 100% من الكحول، البارابين، والكلوروهيدرات الضار:</strong> تركيبة دقيقة وآمنة لمستحضرات بيزلين الطبية.</li>
  <li><strong>عبوة {pack_str_ar}:</strong> حجم ممتاز يضمن عناية يومية وانتعاشاً مستمراً.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> وضعي رول اون بيزلين على بشرة إبطين نظيفة وجافة تماماً بعد الاستحمام.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> مرري كرة الرول اون مرتين على كل إبط بالتساوي.</li>
  <li><strong>الخطوة الثالثة (التجفيف):</strong> دعي السائل يجف لـ 30 ثانية قبل ارتداء الملابس للاستفادة القصوى من التفتيح.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>حجر الشبة النقي وصمغ النحل (Alum & Propolis):</strong> يمتصان العرق ويعقمان جلد الإبطين ب أمان.</li>
  <li><strong>مركب اللوميسكين وفيتامين C (Lumiskin & Vitamin C):</strong> يفتحان التصبغات ويجددان نضارة البشرة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على منطقة الإبطين فقط.</li>
  <li>تجنبي تطبيقه على الجلد المصاب بجروح أو التهابات حادة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن رول اون بيزلين الطبي لتفتيح الإبطين وحماية 48 ساعة بعبير {frag_ar}.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / مزيلات عرق بيزلين المفتحة للبشرة 48 ساعة</td></tr>
  <tr><th>نوع المنتج</th><td>رول اون مزيل عرق طبي ممتد المفعول لتفتيح الإبطين ({pack_str_ar})</td></tr>
  <tr><th>الحجم/الوزن</th><td>{pack_str_ar}</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (بما في ذلك الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>إبطين مفتحين، ناعمين، خاليين من التصبغات وجافين لـ 48 ساعة</td></tr>
  <tr><th>الملمس</th><td>سائل رول اون خفيف سريع الجفاف دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر {frag_ar} الفاخر المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>صمغ النحل، حجر الشبة، لوميسكين، فيتامين C، خالي من الكحول</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Beesline Laboratories)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد اللوميسكين وصمغ النحل من بيزلين (Beesline Whitening)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج رول اون بيزلين مشكلة اسمرار وسواد منطقة الإبطين، رائحة العرق الكريهة، وتهيج الجلد بعد الحلاقة.</p>

<h3>لماذا تنجح تركيبة اللوميسكين وحجر الشبة؟</h3>
<p>لأن حجر الشبة يقلل التعرق بطبيعية دون سد المسام، بينما يثبط اللوميسكين إنتاج انزيم التايروسينيز المسبب للتصبغات.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على بشرة جافة:</strong> استعمليه دائماً بعد تجفيف الإبطين جيداً بالمنشفة.<br>
2. <strong>ترك السائل يجف:</strong> انتظري 30 ثانية قبل ارتداء الملابس لمنع البقع.<br>
3. <strong>الاستمرار لـ 4 أسابيع:</strong> يضمن الاستخدام اليومي تفتيحاً ملموساً ولوناً موحداً.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مزيلات عرق بيزلين تسد مسام الإبطين وتمنع التنفس الطبيعي."<br>
<strong>الحقيقة:</strong> بيزلين يعتمد حجر الشبة الطبيعي الذي ينظم العرق ويعقم البشرة دون انسداد المسام.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يحتجز صمغ النحل (Propolis) البكتيريا المسببة للرائحة، بينما يعيد فيتامين C النضارة والصفاء للأنسجة.</p>"""

    faqs = [
        (f"ما هو {title_ar}؟", f"هو رول اون طبي طبيعي من بيزلين لتفتيح منطقة الإبطين وحماية 48 ساعة ضد العرق بعبير {frag_ar} ({pack_str_ar})."),
        (f"ما هي فوائد مركبات اللوميسكين وصمغ النحل؟", "يفتح اللوميسكين البقع الداكنة والتصبغات، بينما يقضي صمغ النحل وحجر الشبة على البكتيريا المسببة للرائحة."),
        ("هل يضمن حماية 48 ساعة مضادة للتعرق؟", "نعم، مثبت سريرياً في امتصاص العرق وتأمين حماية وانتعاش يدوم لـ 48 ساعة."),
        (f"ما حجم ونوع العبوة؟", f"تأتي بحجم {pack_str_ar}."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي الرول اون على بشرة إبطين نظيفة وجافة بعد الاستحمام ودعيه يجف لـ 30 ثانية قبل ارتداء الملابس."),
        ("هل يساعد في تفتيح وتوحيد لون الإبطين؟", "نعم، يزيل اسمرار الإبطين ويمنح البشرة لوناً موحداً ونضارة ملحوظة."),
        ("ما هو بلد صنع مستحضرات بيزلين؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين العالمية (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يترك بقعاً بيضاء أو صفراء على الملابس؟", "لا، فورمولا نقية جافة لا تترك أي أثر أو بقع على الملابس البيضاء أو السوداء."),
        (f"ما هي رائحة هذا المزيل؟", f"يتميز برائحة {frag_ar} المنعشة التي تدوم طوال اليوم."),
        ("هل يناسب البشرة الحساسة وبعد الحلاقة؟", "نعم، خالي من الكحول والبارابين ويهدئ البشرة الحساسة تماماً بعد الحلاقة."),
        ("هل العبوة مناسبة لحقيبة اليد والسفر؟", "نعم، حجم مدمج وأنيق مثالي للحقيبة والسفر والرحلات."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعبوتها المغلقة محكماً."),
        ("هل يترك ملمساً لزجاً؟", "لا، يجف فورياً خلال ثوانٍ ليترك الإبط ناعماً وجافاً."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة دائرية بغطاء لولبي محكم الحماية."),
        ("هل يساعد في تأخير نمو الشعر؟", "نعم، يساعد في تلطيف الجذور وتأخير ظهور الشعر غير المرغوب فيه."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل مرة واحدة يومياً أو عند الحاجة للانتعاش."),
        ("هل يناسب الرجال والنساء؟", "مناسب للنساء والرجال والفتيات."),
        ("هل يحتوي على كلوروهيدرات الألومنيوم الضار؟", "خالي 100% من الكلوروهيدرات الضار والبارابين."),
        ("هل هو مزيل العرق الأكثر مبيعاً في الشرق الأوسط؟", "نعم، بيزلين رول اون المزيل الطبي الأول والأكثر شهرة بالشرق الأوسط."),
        ("هل يمنح حس نضارة وثقة طوال اليوم؟", "نعم، ثبات 48 ساعة يضمن ثقة وانتعاشاً رائعاً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة بيزلين صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يغني عن المعطرات الثقيلة؟", "نعم، يمنح عبيراً ناعماً يغني عن الرش العطري الزائد."),
        ("هل يترك الجلد طرياً؟", "نعم، يترك الإبطين بطراوة ونعومة كالحرير."),
        ("هل يتوفر بعبوات وأحجام متنوعة لدى إكليل أبها؟", "نعم، تتوفر روائح وأحجام متعددة من بيزلين لدى إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{title_en}</strong> is the Middle East's #1 best-selling natural medical whitening roll-on deodorant engineered to lighten underarm skin while providing 48-hour antiperspirant protection. Formulated by Beesline Whitening Roll-On, it blends Propolis, pure Alum Rock, and natural Lumiskin with {frag_en} notes.</p>
<p>Featuring a 100% safe, alcohol-free natural formula ideal for sensitive skin, Beesline Roll-On delays unwanted hair growth, fades dark underarm hyperpigmentation, and provides all-day dry freshness without clogging pores or staining clothes.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>48-Hour Antiperspirant & Odor Defense:</strong> Absorbs sweat and halts odor-causing bacteria growth.</li>
  <li><strong>Natural Underarm Whitening (Lumiskin):</strong> Fades dark spots and unifies underarm skin tone.</li>
  <li><strong>Enriched with Propolis & Alum Rock:</strong> Natural antibacterial base purifying and soothing tender skin.</li>
  <li><strong>Delays Hair Growth & Soothes Shaved Skin:</strong> Calms itching and protects delicate underarms post-shaving.</li>
  <li><strong>100% Free of Alcohol, Parabens & Harmful Aluminum Chlorohydrate:</strong> Safe, clinical formulation.</li>
  <li><strong>{pack_str_en} Packaging:</strong> Convenient size for daily grooming and continuous whitening care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Apply Beesline Roll-On onto clean, dry underarm skin after showering.</li>
  <li><strong>Step 2 (Apply):</strong> Roll the ball twice evenly over each underarm.</li>
  <li><strong>Step 3 (Dry):</strong> Allow fluid to dry for 30 seconds before dressing for optimal whitening absorption.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Alum Rock & Propolis:</strong> Absorb moisture and sanitize underarm skin safely.</li>
  <li><strong>Lumiskin & Vitamin C:</strong> Fade dark pigmentation and restore skin radiance.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical underarm application only.</li>
  <li>Do not apply to broken, wounded, or severely irritated skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking the original natural Beesline whitening roll-on deodorant for 48-hour protection and {frag_en} aroma.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Personal Care / 48-Hour Natural Whitening Roll-On Deodorants</td></tr>
  <tr><th>Product Type</th><td>48-Hour Whitening Natural Roll-On Deodorant ({pack_str_en})</td></tr>
  <tr><th>Volume/Weight</th><td>{pack_str_en}</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Including Sensitive)</td></tr>
  <tr><th>Finish</th><td>Brightened, smooth, even-toned & 48h dry underarm skin</td></tr>
  <tr><th>Texture</th><td>Light fast-drying non-sticky roll-on fluid</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh {frag_en} scent</td></tr>
  <tr><th>Active Ingredients</th><td>Propolis, Alum Rock, Lumiskin, Vitamin C, Alcohol-Free Base</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon (Beesline Laboratories)</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Lumiskin Tyrosinase Inhibition & Alum Rock Deodorization</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Whitening Roll-On resolves dark underarm hyperpigmentation, body odor, and razor burn irritation.</p>

<h3>Why choose Beesline Roll-On?</h3>
<p>Pure Alum Rock controls perspiration without blocking pores, while Lumiskin inhibits tyrosinase activity to fade melanin deposits.</p>"""

    en_faqs = [
        (f"What is {title_en}?", f"It is a natural medical whitening roll-on deodorant by Beesline providing 48-hour antiperspirant protection and underarm skin brightening in a {pack_str_en} pack."),
        ("What are the benefits of Lumiskin and Propolis?", "Lumiskin fades dark underarm pigmentation, while Propolis and Alum Rock sanitize skin and stop odor."),
        ("Does it guarantee 48-hour antiperspirant defense?", "Yes, clinically proven to absorb sweat and maintain dry freshness for 48 hours."),
        (f"What size and packaging is provided?", f"It comes as a {pack_str_en}."),
        ("How do I apply it correctly?", "Apply to clean, dry underarm skin after showering and let dry 30 seconds before dressing."),
        ("Does it brighten and unify underarm skin tone?", "Yes, clears underarm dark spots and unifies skin tone visibly."),
        ("Where is Beesline manufactured?", "It is proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it leave yellow or white marks on clothes?", "No, clear fast-drying formula leaves zero stains on white or black clothes."),
        (f"What scent does this deodorant have?", f"Features a delicate, long-lasting {frag_en} fragrance."),
        ("Is it safe for sensitive skin post-shaving?", "Yes, 100% alcohol-free and paraben-free; soothes sensitive skin post-shaving."),
        ("Is the pack travel-friendly?", "Yes, compact roll-on design fits easily into handbags and travel kits."),
        ("How should I store the product?", "Store in a cool, dry place away from direct heat."),
        ("Does it leave a sticky film?", "No, dries within seconds leaving underarms smooth and dry."),
        ("Is the bottle cap leak-proof?", "Yes, comes with a sturdy screw-top lid."),
        ("Does it delay unwanted hair growth?", "Yes, soothes roots and helps delay unwanted hair regrowth."),
        ("How many times daily should I use it?", "Use once daily or as needed for fresh confidence."),
        ("Is it suitable for men and women?", "Suitable for women, men, and teens."),
        ("Does it contain harmful aluminum chlorohydrate?", "100% free of harmful aluminum chlorohydrate and parabens."),
        ("Is Beesline the #1 whitening deodorant in the Middle East?", "Yes, Beesline is the #1 trusted natural whitening deodorant line."),
        ("Does it provide all-day fresh confidence?", "Yes, 48-hour efficacy guarantees lasting confidence and freshness."),
        ("Is the packaging recyclable?", "Yes, 100% recyclable environmentally friendly packaging."),
        ("Does it replace heavy body sprays?", "Yes, provides a gentle fresh scent replacing heavy sprays."),
        ("Does it leave underarm skin touchably soft?", "Yes, leaves underarm skin touchably soft and supple."),
        ("Are other variants available at Ekleel Abha?", "Yes, Ekleel Abha offers various Beesline roll-on scents and sizes.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "العناية الشخصية / مزيلات عرق بيزلين المفتحة للبشرة 48 ساعة",
        "brand": "Beesline",
        "ar": {
            "title": title_ar,
            "meta_title": f"مزيل عرق بيزلين {pack_str_ar} | صيدلية إكليل أبها",
            "meta_description": f"اشتري {title_ar}. رول اون طبي لتفتيح الإبطين وحماية 48 ساعة من العرق. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بيزلين", "بيزلين_رول_اون", "مزيل_عرق_بيزلين", "تفتيح_الإبط", "إكليل_أبها"]
        },
        "en": {
            "title": title_en,
            "meta_title": f"Beesline Deodorant {pack_str_en} | Ekleel Abha Pharmacy",
            "meta_description": f"Buy original {title_en}. 48-hour natural whitening roll-on deodorant. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["beesline", "beesline_deodorant", "whitening_roll_on", "48h_protection", "ekleel_abha"]
        },
        "schema": {
            "brand": "Beesline",
            "category": "Personal Care / Deodorant",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"{img_slug}.webp",
            "alt": title_en,
            "title": title_en
        }
    }

def create_product_1843():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم لترطيب وتفتيح البشرة من بيزلين 150جم (Beesline Skin Moisturizing and Whitening Cream - 150g)</strong> الكريم الفاخر المزدوج الأكثر فعالية لتغذية، ترطيب، وتفتيح الوجه والجسم بمكونات طبيعية ناصعة. يرتكز هذا الكريم المميز من بيزلين (Beesline Whitening & Moisturizing Cream) على خلاصة الشمع العسلي النقي (Beeswax)، زيت زيتون البكر، مركب اللوميسكين (Lumiskin)، وفيتامين C و E.</p>
<p>يعمل كريم بيزلين المرطب والمفتح على استعادة حيوية البشرة الباهتة، إزالة البقع التصبغية، وتأمين ترطيب عميق لـ 24 ساعة، ليترك بشرتكِ ناعمة، مرنة، ومشعّة بالنضارة والصفاء دون ترك أي أثر دهني لزج.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتفتيح مزدوج للبشرة:</strong> يغذي الجلد بعمق ويفتح التصبغات والبقع الداكنة.</li>
  <li><strong>غني بالشمع العسلي النقي وزيت الزيتون:</strong> يحبس الرطوبة ويحمي البشرة من الجفاف والتأثيرات البيئية.</li>
  <li><strong>مركب اللوميسكين وفيتامين C الطبيعي:</strong> يثبط تكون الميلاين ويمنح الوجه إشراقة ونضارة ملحوظة.</li>
  <li><strong>مناسب للوجه والجسم والرقبة:</strong> فورمولا متوازنة تلائم جميع أجزاء البشرة الجافة والمجهدة.</li>
  <li><strong>خالي 100% من الكحول، البارابين، والهيدروكينون:</strong> تركيبة دقيقة وآمنة للبشرة الحساسة.</li>
  <li><strong>عبوة وافرة سعة 150 جم:</strong> حجم عائلي ممتاز يضمن عناية مكثفة ومستمرة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> نظفي بشرة الوجه أو الجسم جيداً بالماء الفاتر ثم جففيها.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي كمية مناسبة من كريم بيزلين على الوجه والرقبة أو الجسم.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي بحركات دائرية خفيفة لأعلى حتى امتصاص الكريم بالكامل (يُستعمل مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الشمع العسلي وزيت الزيتون (Beeswax & Olive Oil):</strong> يغذيان البشرة ويحفظان الترطيب.</li>
  <li><strong>اللوميسكين وفيتامين C & E:</strong> يفتحان التصبغات ويعيدان النضارة والصفاء.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على البشرة فقط.</li>
  <li>تجنبي ملامسة الكريم المباشرة لداخل العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن الشمس.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من جفاف وتصبغات الوجه والجسم وتفتش عن كريم بيزلين المرطب والمفتح بالشمع العسلي.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات بيزلين المغذية والمفتحة للوجه والجسم</td></tr>
  <tr><th>نوع المنتج</th><td>كريم ترطيب وتفتيح البشرة الشامل بالشمع العسلي (150g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>150 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الجافة، العادية، والمختلطة</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة مرطبة عميقاً، ناعمة كالحرير، مشعة وموحدة اللون</td></tr>
  <tr><th>الملمس</th><td>كريم غني مخملي سريع الامتداد والامتصاص</td></tr>
  <tr><th>العطر</th><td>عطر العسل والزهور الطبيعي اللطيف</td></tr>
  <tr><th>المكونات النشطة</th><td>شمع النحل، زيت الزيتون، لوميسكين، فيتامين C، فيتامين E</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Beesline Laboratories)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الشمع العسلي واللوميسكين من بيزلين (Beesline Cream)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم بيزلين المرطب والمفتح مشكلة جفاف وشحوب الوجه والجسم، التصبغات الناتجة عن الشمس، وفقدان النضارة.</p>

<h3>لماذا تنجح تركيبة الشمع العسلي واللوميسكين؟</h3>
<p>لأن الشمع العسلي يشكل حزاماً مرطباً يحبس الماء بالجلد، بينما يوحد اللوميسكين لون البشرة ويمنع البقع.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق مرتين يومياً:</strong> وضعي الكريم صباحاً ومساءً على الوجه والرقبة.<br>
2. <strong>التركيز على المناطق الجافة:</strong> دلكي الركبتين والأكواع بالكريم لترطيب وتفتيح مضاعف.<br>
3. <strong>الاستخدام قبل المكياج:</strong> ممتاز كقاعدة ترطيب مغذية قبل تطبيق الفاونديشن.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات التفتيح التي تحتوي على الشمع تترك ملمساً دهنياً ثقيلاً."<br>
<strong>الحقيقة:</strong> كريم بيزلين مصمم بتركيبة ناعمة تمتصها البشرة بسرعة دون أي لزوجة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتحد الأحماض الدهنية بالشمع العسلي مع خلايا البشرة، فتصلح حاجز الرطوبة وتمنع التبخر الجلدي.</p>"""

    faqs = [
        ("ما هو كريم لترطيب وتفتيح البشرة من بيزلين 150جم؟", "هو كريم مغذٍ ومفتح للوجه والجسم غني بالشمع العسلي، زيت الزيتون، واللوميسكين لترطيب وتفتيح البشرة 150 جم."),
        ("ما هي فوائد الشمع العسلي واللوميسكين؟", "يحبس الشمع العسلي الرطوبة ويغذي الجلد، بينما يفتح اللوميسكين التصبغات ويمنح إشراقة ملحوظة."),
        ("هل يضمن ترطيباً عميقاً لـ 24 ساعة؟", "نعم، مثبت سريرياً في حفظ رطوبة ونعومة البشرة لـ 24 ساعة."),
        ("ما حجم العبوة؟", "تأتي بحجم وافر سعة 150 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي كمية على الوجه والرقبة أو الجسم ونظفي البشرة، دلكي بحركات دائرية مرتين يومياً."),
        ("هل يناسب الوجه والجسم معاً؟", "نعم، فورمولا آمنة ومتوازنة تلائم بشرة الوجه، الرقبة، والجسم."),
        ("ما هو بلد صنع كريم بيزلين؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين العالمية (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يناسب البشرة الحساسة؟", "نعم، خالي من الكحول والبارابين والهيدروكينون ومناسب للبشرة الحساسة."),
        ("ما هي رائحة كريم بيزلين؟", "يتميز برائحة العسل والزهور الطبيعية اللطيفة جداً."),
        ("هل يمكن استخدامه كقاعدة للمكياج؟", "نعم، ممتاز كمرطب مغذٍ ومهيئ للوجه قبل المكياج."),
        ("هل العبوة 150 جم مناسبة للاستخدام العائلي؟", "نعم، حجم وافر ممتاز للاستخدام اليومي لعدة أشهر."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل يترك أثراً دهنياً ثقيلاً؟", "لا، ينفذ بالبشرة ليعطي ملمساً مخملياً ناعماً دون لزوجة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة دائرية فاخرة بغطاء لولبي محكم الحماية."),
        ("هل يساعد في تفتيح الركب والأكواع؟", "نعم، ممتاز لترطيب وتفتيح الركب والأكواع الجافة."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُفضل استخدامه 2 مرات يومياً (صباحاً ومساءً)."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع الفئات العمرية للنساء والرجال."),
        ("هل يحتوي على الهيدروكينون الضار؟", "خالي 100% من الهيدروكينون والبارابين والمواد الكيميائية الضارة."),
        ("هل هو الكريم المرطب الأكثر طلباً لبيزلين؟", "نعم، كريم بيزلين بالشمع العسلي واللوميسكين الخيار الأول للترطيب والتفتيح."),
        ("هل يمنح حس نضارة وصفاء للوجه؟", "نعم، يمنح بشرتكِ نضارة وصفاءً مشعاً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة بيزلين صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يقلل آثار التجاعيد الخفيفة؟", "نعم، فيتامين E والشمع العسلي يحافظان على مرونة البشرة وشبابها."),
        ("هل يترك البشرة طرية كالحرير؟", "نعم، يترك الجلد طرياً ومخملياً طوال اليوم."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Skin Moisturizing and Whitening Cream - 150g</strong> is the dual-action clinical cream formulated to nourish, hydrate, and brighten facial and body skin with pure natural ingredients. Formulated by Beesline, it fuses pure Beeswax, virgin Olive Oil, natural Lumiskin, and Vitamins C & E.</p>
<p>Beesline Whitening & Moisturizing Cream restores dull skin radiance, fades dark pigmentation, and provides deep 24-hour hydration, leaving your skin touchably soft, flexible, and glowing with health without any greasy film.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Dual-Action Whitening & Deep Hydration:</strong> Deeply nourishes skin while fading dark spots and hyperpigmentation.</li>
  <li><strong>Enriched with Pure Beeswax & Olive Oil:</strong> Locks in moisture and shields skin from environmental drying.</li>
  <li><strong>Natural Lumiskin & Vitamin C Base:</strong> Inhibits melanin production, bestowing a radiant, clear complexion.</li>
  <li><strong>Suitable for Face, Body & Neck:</strong> Balanced gentle formula ideal for all dry and tired skin areas.</li>
  <li><strong>100% Free of Alcohol, Parabens & Hydroquinone:</strong> Safe, non-toxic formulation for sensitive skin.</li>
  <li><strong>Generous 150g Jar:</strong> High-value family size providing months of continuous hydration care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse facial or body skin thoroughly with warm water and pat dry.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a generous amount of Beesline Cream onto face, neck, or body.</li>
  <li><strong>Step 3 (Massage):</strong> Massage in gentle upward circular motions until fully absorbed (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Beeswax & Virgin Olive Oil:</strong> Deeply nourish skin layers and lock in moisture.</li>
  <li><strong>Lumiskin & Vitamins C & E:</strong> Fade dark pigmentation and restore skin luminosity and clarity.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and body application only.</li>
  <li>Avoid direct contact with the interior of the eye.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from direct heat.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dull skin, dark spots, or skin dryness seeking Beesline's signature Beeswax whitening and moisturizing cream.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Skincare / Nourishing & Whitening Face and Body Creams</td></tr>
  <tr><th>Product Type</th><td>Dual Whitening & Moisturizing Beeswax Cream (150g)</td></tr>
  <tr><th>Volume/Weight</th><td>150 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Dry, Normal & Combination Skin</td></tr>
  <tr><th>Finish</th><td>Deeply hydrated, silky smooth, glowing & even-toned skin</td></tr>
  <tr><th>Texture</th><td>Rich velvet fast-absorbing cream matrix</td></tr>
  <tr><th>Fragrance</th><td>Subtle natural honey & floral aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Beeswax, Olive Oil, Lumiskin, Vitamin C, Vitamin E</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon (Beesline Laboratories)</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Beeswax Barrier Protection & Lumiskin Whitening</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Whitening & Moisturizing Cream resolves facial dullness, dark spots, skin dryness, and lost elasticity.</p>

<h3>Why choose Beesline Cream?</h3>
<p>Pure Beeswax forms a protective breathable moisture seal, while Lumiskin inhibits melanin synthesis to clarify skin tone.</p>"""

    en_faqs = [
        ("What is Beesline Skin Moisturizing and Whitening Cream - 150g?", "It is a dual-action moisturizing and whitening cream enriched with Beeswax, Olive Oil, and Lumiskin to clarify and hydrate face and body."),
        ("What are the benefits of Beeswax and Lumiskin?", "Beeswax seals in hydration and nourishes skin, while Lumiskin fades dark spots and unifies skin tone."),
        ("Does it guarantee 24-hour deep hydration?", "Yes, clinically proven to maintain skin suppleness and moisture for 24 hours."),
        ("What volume is contained in this jar?", "It comes in a generous 150g jar."),
        ("How do I apply it correctly?", "Apply to clean facial, neck, or body skin twice daily and massage gently until absorbed."),
        ("Is it suitable for both face and body?", "Yes, balanced gentle formula suitable for facial skin, neck, elbows, and body."),
        ("Where is Beesline Cream manufactured?", "It is proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Is it safe for sensitive skin?", "Yes, free of alcohol, parabens, and hydroquinone; safe for sensitive skin."),
        ("What scent does Beesline Cream have?", "Features a light, pleasant natural honey and floral scent."),
        ("Can it be used as a makeup primer?", "Yes, functions excellently as a nourishing moisturizing primer before foundation."),
        ("Is the 150g jar economical?", "Yes, generous size provides months of daily hydration."),
        ("How should I store the jar?", "Store in a cool, dry place away from direct heat."),
        ("Does it leave a heavy greasy film?", "No, absorbs smoothly into skin leaving a velvet soft finish without grease."),
        ("Is the jar securely sealed?", "Yes, comes in a sleek jar with a tight screw-top lid."),
        ("Does it help brighten knees and elbows?", "Yes, highly effective at moisturizing and brightening dry knees and elbows."),
        ("How many times daily should I use it?", "Recommended for use twice daily, morning and evening."),
        ("Is it suitable for men and women?", "Suitable for all age groups, both men and women."),
        ("Is it free of harmful hydroquinone?", "Yes, 100% free of hydroquinone, parabens, and harsh chemicals."),
        ("Is it Beesline's top whitening cream?", "Yes, Beesline Beeswax Whitening Cream is the #1 trusted choice for face & body whitening."),
        ("Does it give facial skin a radiant glow?", "Yes, bestows a bright, radiant, and healthy glow."),
        ("Is the packaging recyclable?", "Yes, 100% recyclable environmentally friendly jar."),
        ("Does it reduce fine dryness lines?", "Yes, Vitamin E and Beeswax maintain skin elasticity to smooth fine lines."),
        ("Does it leave skin touchably soft?", "Yes, leaves skin touchably soft, smooth, and supple."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1843",
        "sku": "EK-1843",
        "gtin": "5281018003138",
        "category": "العناية بالبشرة / كريمات بيزلين المغذية والمفتحة للوجه والجسم",
        "brand": "Beesline",
        "ar": {
            "title": "كريم لترطيب وتفتيح البشرة من بيزلين 150جم",
            "meta_title": "كريم بيزلين المرطب والمفتح 150جم | إكليل أبها",
            "meta_description": "اشتري كريم لترطيب وتفتيح البشرة من بيزلين (150جم). كريم مغذٍ بالشمع العسلي واللوميسكين للوجه والجسم خالي من الهيدروكينون. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بيزلين", "كريم_بيزلين", "تفتيح_البشرة", "ترطيب_البشرة", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Skin Moisturizing and Whitening Cream - 150g",
            "meta_title": "Beesline Whitening & Moisturizing Cream 150g | Ekleel Abha",
            "meta_description": "Buy original Beesline Skin Moisturizing and Whitening Cream (150g). Dual Beeswax & Lumiskin face and body cream. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["beesline", "beesline_cream", "whitening_cream", "moisturizer", "ekleel_abha"]
        },
        "schema": {
            "brand": "Beesline",
            "category": "Skincare / Body Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "beesline-skin-moisturizing-and-whitening-cream-150g.webp",
            "alt": "Beesline Skin Moisturizing and Whitening Cream 150g",
            "title": "Beesline Skin Moisturizing and Whitening Cream 150g"
        }
    }

print("Loaded Batch 27 builders")
