import json, os

def _make_guerlain_concealer_b93(pid, gtin, ar_title, en_title, shade_num, shade_ar, shade_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_title}</strong> الكونسيلر الطبي المضيء والمجدد الفاخر الأسطوري للشفاه والوجه من الدار الفرنسية العريقة جيرلان (Guerlain Precious Light Illuminating Concealer) المصمم خصيصاً لتصحيح الهالات السوداء، تفتيح محيط الشفاه، محو آثار التعب والخطوط، وتأطير الوجه ببريق ذهبي ناصع ومشرق. يرتكز هذا المستحضر الفرنسي الأصيل ({en_title}) على جزيئات الذهب عيار 24 (24K Gold Pigments)، المركبات المجددة للخلايا (Rejuvenating Complex)، والببتيدات المقوية.</p>
<p>يعمل كونسيلر جيرلان المضيء بدرجة {shade_num} على إخفاء التعب والتصبغات حول الشفاه والعينين، ملء الخطوط الرقيقة، وتمليس بشرة الشفاه والوجه، ليترك بشرتك ناعمة كالحرير، مرطبة، موحدة اللون بدرجة {shade_ar}، ومفعمة بالنقاء والتوهج الذهبي من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>إضاءة وتفتيح ناصع للهالات ومحيط الشفاه (درجة {shade_num}):</strong> يزيل آثار التعب والإجهاد فورياً.</li>
  <li><strong>تجديد وترميم الخلايا والخطوط بمركب الكولاجين والذهب 24K:</strong> يمنح الوجه والشفاه مظهراً مشرقاً.</li>
  <li><strong>تغطية خفيفة حريرية تندمج بسلاسة دون تكتل:</strong> لا تتسرب بكسرات العين أو الشفاه.</li>
  <li><strong>ترطيب وتنعيم ممتد لـ 24 ساعة للشفاه والوجه:</strong> يمنع جفاف وتقشر البشرة.</li>
  <li><strong>مختبر طبياً ومن أطباء العيون والجلدية:</strong> مناسب لبشرة الشفاه الحساسة ومستخدمي العدسات.</li>
  <li><strong>قلم ذهبي فاخر أيقوني مزود بفرشاة دقيقة:</strong> قمة الفخامة الفرنسية في تصحيح المكياج.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> اضغطي على قاعدة قلم كونسيلر جيرلان الذهبي لضخ كمية مناسبة على رأس الفرشاة.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي الكونسيلر المضيء على الهالات السوداء، محيط الشفاه، وجوانب الأنف.</li>
  <li><strong>الخطوة الثالثة:</strong> ادمجي برفق بأطراف الأصابع أو الفرشاة للحصول على إشراقة ناصعة (يُستعمل يومياً وعند المكياج).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>جزيئات الذهب 24K والببتيدات المجددة:</strong> يعكسان الضوء ويحفزان تجدد خلايا البشرة والشفاه.</li>
  <li><strong>المركبات المطرية المائية:</strong> تحفظ النعومة الحريرية وتمنع التجمع في الخطوط الدقيقة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي التجميلي على الشفاه والوجه ومحيط العينين.</li>
  <li>تجنبي التلامس المباشر لداخل العين واغلقي الغطاء بإحكام.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن {ar_title} لتصحيح وإضاءة وتجديد الشفاه والهالات ببريق الذهب.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جيرلان باريس (Guerlain Paris France)</td></tr>
  <tr><th>الفئة</th><td>مكياج الوجه والشفاه / كونسيلر ومصححات جيرلان المضيئة 1.5ml</td></tr>
  <tr><th>نوع المنتج</th><td>كونسيلر ومصحح مضيء ومجدد للشفاه والوجه بجزيئات الذهب 24K (درجة {shade_num})</td></tr>
  <tr><th>الحجم/الوزن</th><td>1.5 مل / قلم بفرشاة دقيقة</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة والشفاه (العادية، الجافة والمجهدة) ومستخدمي العدسات</td></tr>
  <tr><th>المظهر النهائي</th><td>شفاه ووجه ناعمين كالحرير، مرطبين، موحدي اللون بدرجة {shade_ar} ومفعمين بالإشراق الذهبي</td></tr>
  <tr><th>الملمس</th><td>سائل كريمي مضيء خفيف ينزلق ويمتص بسلاسة</td></tr>
  <tr><th>العطر</th><td>عطر الزهور والمسك الفرنسي الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>جزيئات الذهب 24K، ببتيدات مجددة، مرطبات مائية دقيقة</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>LVMH Guerlain France</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 18 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد جزيئات الذهب 24K في كونسيلر جيرلان المضيء (Guerlain Precious Light {shade_num})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كونسيلر جيرلان المضيء مشكلة الهالات السوداء، التصبغات حول الشفاه، الخطوط الدقيقة، وشحوب الوجه.</p>

<h3>لماذا تنجح تركيبة Guerlain Precious Light Concealer Shade {shade_num}؟</h3>
<p>لأن جزيئات الذهب عيار 24 تعكس الضوء بعيداً عن الظلال والخطوط بينما تجدد الببتيدات خلايا الشفاه والوجه.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على محيط الشفاه قبل أحمر الشفاه:</strong> يبرز حجم الشفاه ويمنع تسرب الروج.<br>
2. <strong>الدمج برفق بالطبطبة بأطراف الأصابع:</strong> يحافظ على تركيز الإضاءة الذهبية.<br>
3. <strong>إغلاق غطاء القلم بإحكام:</strong> يحفظ طراوة الفرشاة والتركيبة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الكونسيلر المضيء يجفف بشرة الشفاه والعيون."<br>
<strong>الحقيقة:</strong> كونسيلر جيرلان المضيء مدعم بمركبات مرطبة مجددة تحفظ رطوبة ونعومة الشفاه والعينين.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تشتت الجزيئات الذهبية الضوء الساقط على ثنايا الجلد مظهرة السطح أكثر استواءً وإشراقاً.</p>"""

    faqs_data = [
        (f"ما هو {ar_title}؟", f"هو كونسيلر ومصحح مضيء ومجدد للشفاه والوجه بجزيئات الذهب 24K والببتيدات بدرجة {shade_num} من جيرلان."),
        (f"ما هي فوائد جزيئات الذهب 24K والببتيدات المجددة بدرجة {shade_num}؟", "تضيء وتفتح الهالات ومحيط الشفاه، تجدد الخلايا والخطوط، وتمنح إشراقة ذهبية ناصعة لـ 24 ساعة."),
        ("هل يضيء الشفاه والوجه ويجدد الخلايا بدون تكتل؟", "نعم، مثبت سريرياً في إضاءة وتجديد الشفاه والوجه وتغطية الهالات خالي من التكتل."),
        ("ما حجم العبوة ومظهرها؟", "تأتي بقلم ذهبي أنيق مزود بفرشاة دقيقة سعة 1.5 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اضغطي قاعدة القلم، وزعي على الهالات ومحيط الشفاه واددمجي بالطبطبة بأطراف الأصابع."),
        ("هل هو آمن ومختبر طبياً؟", "نعم، 100% آمن ومختبر درماتولوجياً ومناسب لمحيط الشفاه والعيون الحساسة."),
        ("أين صُنع كونسيلر جيرلان المضيء؟", "صُنع في فرنسا بواسطة LVMH Guerlain France."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات جيرلان لدى إكليل أبها أصلية 100%."),
        (f"ما درجة كونسيلر جيرلان المضيء؟", f"درجة {shade_num} ({shade_ar})."),
        ("هل يناسب الشفاه والهالات السوداء وجوانب الوجه؟", "نعم، ممتاز لتحديد وإضاءة الشفاه، الهالات، وجوانب الوجه."),
        ("هل القلم الذهبي 1.5 مل مريح ولطيف بالحقيبة؟", "نعم، قلم ذهبي أنيق جداً ومريح بالحقيبة وللتعديل السريع."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل جيرلان الماركة الفرنسية الأولى في المصححات المضيئة؟", "نعم، Guerlain Precious Light المصحح المضيء الفاخر رقم 1 الأكثر تفضيلاً عالمياً."),
        ("كم يدوم ثباته طوال اليوم؟", "يدوم طوال اليوم بإشراقة ونضارة ثابته."),
        ("هل ينشطف بمزيل المكياج بسهولة؟", "نعم، ينشطف بسلاسة بمزيل المكياج دون شد البشرة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يبرز جمال الشفاه ويمنع تسرب الروج؟", "نعم، يحدد ويضيء الشفاه ويمنع سيلان أحمر الشفاه بالخطوط."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والفتيات؟", "نعم، ممتاز للنساء والفتيات."),
        ("هل يناسب جميع فصول السنة؟", "نعم، إضاءة وتجديد فاخر مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن مكياج الشفاه والوجه؟", "نعم، منتج فرنسي فاخر وأساسي لكل حقيبة تجميل."),
        (f"هل يعيد المظهر المشرق الناعم للشفاه والوجه بدرجة {shade_num}؟", f"نعم، يمنح الشفاه والوجه مظهراً ناصع التوهج والإشراق."),
        ("هل تتوفر درجات كونسيلر جيرلان المضيء الأخرى؟", "نعم، تتوفر عائلة Guerlain Precious Light كاملة لدى إكليل أبها."),
        ("هل يغني عن إضاءة الهايلايتر الكثيفة؟", "نعم، يمنح إضاءة ذهبية طبيعية ناعمة تسبق أو تغني عن الهايلايتر."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury illuminating and rejuvenating lip and facial concealer pen from iconic House Guerlain Paris (Guerlain Precious Light Illuminating Concealer) designed to correct dark circles, brighten lip contours, erase signs of fatigue, and frame the face with a radiant 24K gold luster. Built upon pure 24K Gold Pigments, Rejuvenating Peptide Complex, and hydrating emollients.</p>

<p>Guerlain Precious Light Concealer in Shade {shade_num} smoothly conceals dark shadows around lips and eyes, fills micro-lines, and smoothes lip and facial skin, leaving your skin touchably silky soft, hydrated, beautifully even-toned in {shade_en}, and illuminated with a golden glow from first stroke.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Illuminates & Brightens Lip Contours & Dark Circles (Shade {shade_num}):</strong> Erases fatigue and dark spots instantly.</li>
  <li><strong>Rejuvenates Skin Cells & Fills Fine Lines with 24K Gold & Peptides:</strong> Imparts a youthful radiant look.</li>
  <li><strong>Silky Lightweight Coverage Blends Seamlessly:</strong> Does not settle into eyelid or lip micro-creases.</li>
  <li><strong>24-Hour Extended Hydration for Lips & Face:</strong> Prevents skin dryness and flaking.</li>
  <li><strong>Ophthalmologically & Dermatologically Tested:</strong> Safe for sensitive lip skin and contact lens wearers.</li>
  <li><strong>Iconic Luxury Gold Pen with Precise Brush Applicator:</strong> The pinnacle of French makeup correction craft.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Click the base of the gold Guerlain concealer pen to dispense product onto the brush tip.</li>
  <li><strong>Step 2:</strong> Apply the illuminating concealer over dark circles, lip contours, and sides of the nose.</li>
  <li><strong>Step 3:</strong> Blend gently by patting with fingertips or a brush for a radiant finish (use daily with makeup).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>24K Gold Pigments & Rejuvenating Peptides:</strong> Reflect light and stimulate lip and skin cell renewal.</li>
  <li><strong>Aqueous Hydrating Agents:</strong> Preserve silky softness preventing settlement into fine lines.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on lips, face, and eye contours.</li>
  <li>Avoid direct contact inside eyes and cap tightly after use.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_title} for 24K gold lip contour brightening, dark circle correction, and skin rejuvenation.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Guerlain Paris (France)</td></tr>
  <tr><th>Category</th><td>Face & Lip Makeup / Guerlain Luxury Illuminating Concealers 1.5ml</td></tr>
  <tr><th>Product Type</th><td>24K Gold Rejuvenating Lip & Face Illuminating Concealer Pen (Shade {shade_num})</td></tr>
  <tr><th>Volume/Weight</th><td>1.5 ml Brush Pen</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin & Lip Types (Normal, Dry & Stressed Skin) & Contact Lens Wearers</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, even-toned in {shade_en} & golden-illuminated lips/face</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-heavy fluid liquid concealer</td></tr>
  <tr><th>Fragrance</th><td>100% Luxurious French floral musk fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>24K Gold Pigments, Rejuvenating Peptides, Hydrating Emollients</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>LVMH Guerlain France</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 18+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of 24K Gold Light Reflection & Lip-Skin Peptide Regeneration</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves lip contour dullness, dark circles, lipstick feathering in fine lines, and facial fatigue.</p>

<h3>Why choose Guerlain Precious Light Concealer Shade {shade_num}?</h3>
<p>24K Gold Pigments reflect light away from dark shadows and lip creases while peptides stimulate cell renewal.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a luxury 24K Gold illuminating and rejuvenating lip and face concealer pen from Guerlain Paris (Shade {shade_num} / 1.5ml)."),
        (f"What are the benefits of 24K Gold Pigments and Rejuvenating Peptides in Shade {shade_num}?", "Illuminate dark circles and lip contours, renew skin cells, fill fine lines, and deliver golden radiance."),
        ("Does it illuminate lip contours and face without creasing?", "Yes, clinically proven to illuminate lip contours and conceal dark circles with zero creasing."),
        ("What volume and applicator format are included?", "1.5ml gold luxury pen with a precise brush tip."),
        ("How do I use it correctly?", "Click pen base, apply brush over lip contours and dark circles, and blend gently by patting."),
        ("Is it safe and tested by dermatologists?", "Yes, 100% safe, dermatologically tested, and suitable for sensitive lips and eye areas."),
        ("Where is Guerlain Concealer manufactured?", "In France by LVMH Guerlain France."),
        ("How do I verify authenticity at Ekleel Abha?", "All Guerlain products at Ekleel Abha are 100% original."),
        (f"What shade is Guerlain Precious Light Concealer?", f"Shade {shade_num} ({shade_en})."),
        ("Is it suitable for lip contours, dark circles, and face touch-ups?", "Yes, versatile luxury illuminator for lip contours, eye circles, and face highlight."),
        ("Is the 1.5ml gold pen travel friendly?", "Yes, sleek gold pen ideal for handbags and quick touch-ups."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Guerlain Precious Light a #1 luxury illuminator?", "Yes, Guerlain Precious Light is the world's #1 premier luxury French illuminating concealer."),
        ("How long does it hold during the day?", "Holds throughout the day with radiant fresh glow."),
        ("Does it remove easily with makeup remover?", "Yes, removes smoothly with makeup remover without tugging skin."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it prevent lipstick feathering into fine lines?", "Yes, defines lip contours preventing lipstick from bleeding into fine lines."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and teens?", "Yes, suitable for both women and teens."),
        ("Is it good for all seasons?", "Yes, ideal luxury gold illumination for summer and winter care."),
        ("Is it a nice makeup gift?", "Yes, an essential premier French luxury makeup correction gift."),
        (f"Does it restore smooth radiant lips and face in Shade {shade_num}?", "Yes, gives lips and face an illuminated golden radiant look."),
        ("Are other Guerlain Precious Light shades available?", "Yes, the full Guerlain Precious Light shade range is available at Ekleel Abha."),
        ("Does it replace heavy highlighter makeup?", "Yes, provides a natural soft golden glow replacing heavy powdered highlighters."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Guerlain",
        "ar": {
            "title": ar_title,
            "meta_title": f"{ar_title} | إكليل أبها",
            "meta_description": f"اشتري {ar_title}. كونسيلر فرنسي مضيء ومجدد للشفاه والوجه بالذهب 24K. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. French luxury 24K Gold rejuvenating lip & face illuminating concealer pen. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2187():
    return _make_guerlain_concealer_b93(
        pid=2187, gtin="3346470426146",
        ar_title="كونسيلر مضيء ومجدد الشفاه(1.5) من جيرلان",
        en_title="Illuminating and regenerating lip concealer (1.5) from Guerlain",
        shade_num="1.5", shade_ar="درجة 1.5", shade_en="Shade 1.5",
        tags_ar=["جيرلان", "كونسيلر_جيرلان_المضيء_1.5", "مجدد_الشفاه_جيرلان", "كونسيلر_بالذهب", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_precious_light_1.5", "guerlain_lip_concealer", "24k_gold_concealer", "ekleel_abha"]
    )


def create_product_2188():
    return _make_guerlain_concealer_b93(
        pid=2188, gtin="3346470408760",
        ar_title="كونسيلر مضيء ومجدد الشفاه(02) من جيرلان",
        en_title="Illuminating and rejuvenating concealer (02) from Guerlain",
        shade_num="02", shade_ar="درجة 02", shade_en="Shade 02",
        tags_ar=["جيرلان", "كونسيلر_جيرلان_المضيء_02", "مجدد_الشفاه_جيرلان", "كونسيلر_بالذهب", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_precious_light_02", "guerlain_lip_concealer", "24k_gold_concealer", "ekleel_abha"]
    )


def _make_guerlain_eyeliner_b93(pid, gtin, ar_title, en_title, shade_num, shade_ar, shade_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_title}</strong> قلم كحل تحديد العيون الفاخر الأسطوري ذو الثبات العالي المرفق ببراية دقيقة من الدار الفرنسية العريقة جيرلان (Guerlain Crayon Yeux Eyeliner) المصمم لمنح عينيك تحديداً حاداً، لوناً غنياً بالصبغات الكثيفة، وثباتاً 24 ساعة دون تلطيخ أو سيلان. يرتكز هذا القلم الفرنسي الأصيل ({en_title}) على التركيبة الشمعية الحريرية المقاومة للماء، براية دقيقة مرفقة بالغطاء، وزيوت التثبيت الناعمة.</p>
<p>يعمل قلم كحل جيرلان بدرجة {shade_num} على رسم وتأطير عينيك بدقة متناهية، تحديد خط الرموش الداخلي والخارجي بسهولة، وتزويد نظرتك ببريق دافئ وسحر فرنسي، ليترك عينيك مؤطرتين بنقاء، مرطبتين، ناصعتي اللون بدرجة {shade_ar}، ومحميتين من التلطخ لـ 24 ساعة من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تحديد حاد ورسم دقيق للعينين باللون {shade_ar} (درجة {shade_num}):</strong> صبغات غنية وكثيفة.</li>
  <li><strong>قوام شمعي كريمي ينساب بسلاسة دون شد الجفن:</strong> يسهل الرسم داخل وخارج العين.</li>
  <li><strong>ثبات عالي لـ 24 ساعة مقاوم للماء، العرق، والتلطخ:</strong> تدوم نظرتك ناصعة طوال اليوم.</li>
  <li><strong>مرفق ببراية دقيقة مخصصة لحفظ حدة رأس القلم:</strong> تضمن براية دقيقة دائماً.</li>
  <li><strong>مختبر طبياً ومن أطباء العيون وآمن للعيون الحساسة والعدسات:</strong> خالي من التهيج.</li>
  <li><strong>أنبوب أنيق ومريح باليد من جيرلان باريس:</strong> قمة الفخامة الفرنسية بكحل تحديد العيون.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ارسمي خطاً دقيقاً بقلم كحل جيرلان على طول خط الرموش العلوية والسفلية.</li>
  <li><strong>الخطوة الثانية:</strong> يمكنك استخدامه داخل العين كـ كحل مائي محدد بأمان كامل.</li>
  <li><strong>الخطوة الثالثة:</strong> استخدمي البراية المرفقة بانتظام لحفظ حدة رأس القلم (يُستعمل daily وعند المكياج).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الشمع الطبيعي وزيوت التثبيت:</strong> يضمنان انزلاق الكحل بسلاسة وثبات الصبغة 24 ساعة.</li>
  <li><strong>الصبغات الفرنسية الفاخرة:</strong> تمنح لون {shade_ar} ناصعاً ومحدداً بقوة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي التجميلي على خط الرموش والعينين.</li>
  <li>احفظي الغطاء مغلقاً بإحكام بعد الاستخدام لمنع جفاف رأس القلم.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن {ar_title} للتحديد الدقيق والثابت لـ 24 ساعة كحلفرنسي فاخر.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جيرلان باريس (Guerlain Paris France)</td></tr>
  <tr><th>الفئة</th><td>مكياج العيون / أقلام كحل جيرلان الفاخرة مع براية</td></tr>
  <tr><th>نوع المنتج</th><td>قلم كحل وتحديد عيون مقاوم للماء ثبات 24 ساعة مع براية مرفقة (درجة {shade_num})</td></tr>
  <tr><th>الحجم/الوزن</th><td>قلم كحل مدمج + براية دقيقة مخصصة</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع عيون وجفون الوجه ومستخدمي العدسات اللاصقة</td></tr>
  <tr><th>المظهر النهائي</th><td>عينان محددتان بدقة، ناصعتا اللون بدرجة {shade_ar} ومحميتان من التلطخ لـ 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>قوام شمعي دسم ناعم ينزلق بسلاسة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور المهيجة</td></tr>
  <tr><th>المكونات النشطة</th><td>شمع طبيعي، صبغات غنية مقاومة للماء، زيوت تثبيت ناعمة</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا / ألمانيا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>LVMH Guerlain France</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد القوام الشمعي المقاوم للماء في كحل جيرلان (Guerlain Eyeliner Pencil {shade_num})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج قلم كحل جيرلان مشكلة سيلان الكحل، التلطخ أسفل العين، صعوبة الرسم الداخلي، والبراية المفقودة.</p>

<h3>لماذا تنجح تركيبة Guerlain Eyeliner Pencil Shade {shade_num}؟</h3>
<p>لأن الزيوت الشمعية تثبت الصبغة فورياً على خط الرموش بينما تضمن البراية المرفقة رأس دقيق دائماً.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام البراية المرفقة قبل الرسم:</strong> يضمن حواف دقيقة ومحددة للعينين.<br>
2. <strong>الرسم من الزاوية الداخلية للخارجية:</strong> يمنح نظرة واسعة وجذابة.<br>
3. <strong>إغلاق الغطاء بإحكام:</strong> يحافظ على طراوة وانزلاق الشمع الكحلي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "أقلام الكحل الشمعية تسيل وتلطخ أسفل العينين بعد ساعات."<br>
<strong>الحقيقة:</strong> قلم كحل جيرلان صُمم بتركيبة شمعية مقاومة للماء تجف وتثبت لـ 24 ساعة كاملة دون سيلان.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تشكل الشموع كرتوناً عازلاً على خط دموع العين مانعاً سيلان الصبغات الملونة.</p>"""

    faqs_data = [
        (f"ما هو {ar_title}؟", f"هو قلم كحل وتحديد عيون مقاوم للماء ثبات 24 ساعة مع براية مرفقة باللون {shade_ar} (درجة {shade_num}) من جيرلان."),
        (f"ما هي فوائد القوام الشمعي والبراية المرفقة بدرجة {shade_num}؟", "يحدد العينين بدقة حادة، ينزلق بسلاسة دون شد الجفن، ويثبت لـ 24 ساعة مقاوم للماء والتلطخ."),
        ("هل يحدد العينين ويثبت لـ 24 ساعة بدون سيلان؟", "نعم، مثبت سريرياً في التحديد الدقيق والثبات 24 ساعة المقاوم للماء والسيلان."),
        ("ما هي محتويات العبوة؟", "تأتي بقلم كحل أنيق + براية مخصصة مرفقة."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ارسمي على خط الرموش أو داخل العين، واستخدمي البراية المرفقة بانتظام لحفظ حدة رأس القلم."),
        ("هل هو خالٍ من العطور وآمن للعيون الحساسة والعدسات؟", "نعم، 100% خالٍ من العطور المهيجة ومختبر من أطباء العيون ومناسب لمستخدمي العدسات."),
        ("أين صُنع قلم كحل جيرلان؟", "صُنع في فرنسا بواسطة LVMH Guerlain France."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات جيرلان لدى إكليل أبها أصلية 100%."),
        (f"ما لون قلم كحل جيرلان {shade_num}؟", f"لون {shade_ar} غني وناصع (درجة {shade_num})."),
        ("هل يناسب خط الرموش الداخلي والخارجي؟", "نعم، ممتاز لرسم وتأطير خط الرموش الداخلي والخارجي بأمان."),
        ("هل البراية المرفقة مريحة ومناسبة؟", "نعم، براية دقيقة مخصصة تحافظ على حدة القلم دائماً."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف مع إغلاق الغطاء بإحكام."),
        ("هل جيرلان الماركة الفرنسية الأولى في أقلام الكحل؟", "نعم، Guerlain Eyeliner Pencil الماركة الفاخرة رقم 1 الأكثر شهرة وتفضيلاً بعالم الجمال."),
        ("كم يدوم ثباته طوال اليوم؟", "يدوم لـ 24 ساعة متواصلة مقاوم للماء والعرق والتلطخ."),
        ("هل ينشطف بمزيل المكياج بسهولة؟", "نعم، ينشطف بسلاسة بمزيل مكياج العيون دون شد الجفون."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل ينزلق بسهولة دون شد الجفن؟", "نعم، قوام شمعي ناعم ينزلق بسلاسة دون تسبيب أي شد للعينين."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والفتيات؟", "نعم، ممتاز للنساء والفتيات."),
        ("هل يناسب جميع ألوان العيون والمناسبات؟", "نعم، ممتاز للمكياج اليومي والمناسبات الساهرة."),
        ("هل يصلح هدية ممتازة ضمن مكياج العيون؟", "نعم، منتج فرنسي فاخر وأساسي لكل حقيبة تجميل."),
        (f"هل يعيد المظهر الناصع المحدّد للعينين بدرجة {shade_num}؟", f"نعم، يمنح العينين مظهراً محدد بدقة وناصع باللون {shade_ar}."),
        ("هل تتوفر ألوان أقلام كحل جيرلان الأخرى؟", "نعم، تتوفر عائلة Guerlain Eyeliner Pencils كاملة لدى إكليل أبها."),
        ("هل يسبب تحسس العينين؟", "تركيبة لطيفة خالية من العطور المهيجة تمنع أي تحسس للعينين."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury long-wear waterproof eyeliner pencil with an included custom sharpener from iconic House Guerlain Paris (Guerlain Crayon Yeux Eyeliner) designed to deliver sharp definition, rich intense color payoff, and 24-hour smudge-proof hold. Built upon a silky waterproof wax formulation, precise custom sharpener, and setting emollients.</p>

<p>Guerlain Eyeliner Pencil in Shade {shade_num} smoothly frames your eyes with high precision, effortlessly lines inner waterlines and outer lash lines, and imparts sophisticated French elegance, leaving your eyes touchably defined, hydrated, brilliantly colored in {shade_en}, and protected from smudging for 24 hours from first application.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Sharp Definition & Intense Color Payoff in {shade_en} (Shade {shade_num}):</strong> Rich intense pigment.</li>
  <li><strong>Smooth Creamy Wax Texture Glides Without Tugging:</strong> Lines inner and outer eye areas easily.</li>
  <li><strong>24-Hour Waterproof, Sweat-Proof & Smudge-Proof Hold:</strong> Resists fading all day long.</li>
  <li><strong>Includes Custom Precision Sharpener:</strong> Ensures a sharp tip for crisp eye lining at all times.</li>
  <li><strong>Ophthalmologically Tested Safe for Sensitive Eyes & Contact Lenses:</strong> Zero irritation formula.</li>
  <li><strong>Iconic French Luxury Guerlain Casing:</strong> The pinnacle of French luxury eyeliner craft.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Draw a precise line along upper and lower lash lines using Guerlain eyeliner pencil.</li>
  <li><strong>Step 2:</strong> Can be applied along inner waterlines safely for intense eye definition.</li>
  <li><strong>Step 3:</strong> Use included sharpener regularly to keep the pencil tip sharp (use daily with makeup).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Waxes & Setting Oils:</strong> Ensure smooth glide and 24-hour waterproof pigment lock.</li>
  <li><strong>Luxurious French Pigments:</strong> Provide a rich, intense {shade_en} color definition.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on eye contours and waterlines.</li>
  <li>Keep cap tightly closed after use to prevent pencil tip dryness.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_title} for sharp, 24-hour waterproof luxury French eyeliner definition.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Guerlain Paris (France)</td></tr>
  <tr><th>Category</th><td>Eye Makeup / Guerlain Luxury Eyeliner Pencils with Sharpener</td></tr>
  <tr><th>Product Type</th><td>24-Hour Waterproof Smudge-Proof Eyeliner Pencil with Custom Sharpener (Shade {shade_num})</td></tr>
  <tr><th>Volume/Weight</th><td>Compact Pencil + Custom Sharpener</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Eye Types & Sensitive Contact Lens Wearers</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, waterproof, smudge-proof & sharply defined eyes</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-tugging creamy wax gliding easily</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (irritant-free)</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Waxes, Waterproof Pigment Complexes, Setting Oils</td></tr>
  <tr><th>Country of Origin</th><td>France / Germany</td></tr>
  <tr><th>Manufacturer</th><td>LVMH Guerlain France</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Waterproof Wax Integration & 24-Hour Pigment Fixation</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves running eyeliner, under-eye smudging, lost sharpeners, and dull eye definition.</p>

<h3>Why choose Guerlain Eyeliner Pencil Shade {shade_num}?</h3>
<p>Silky wax polymers set instantly on lash lines forming a waterproof shield while the custom sharpener ensures crisp application every time.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a luxury 24-hour waterproof eyeliner pencil with custom sharpener from Guerlain Paris in {shade_en} (Shade {shade_num})."),
        (f"What are the benefits of the creamy wax texture and sharpener in Shade {shade_num}?", "Deliver sharp definition, glide smoothly without tugging, and hold for 24 hours waterproof and smudge-proof."),
        ("Does it define eyes and hold for 24 hours without smudging?", "Yes, clinically proven to deliver 24-hour waterproof smudge-proof eye definition."),
        ("What items are included in this box?", "Sleek eyeliner pencil + custom sharpener."),
        ("How do I use it correctly?", "Line lash lines or waterlines smoothly, and sharpen tip regularly using included sharpener."),
        ("Is it fragrance-free and safe for contact lens wearers?", "Yes, 100% fragrance-free, ophthalmologically tested, and safe for sensitive eyes and contact lens wearers."),
        ("Where is Guerlain Eyeliner Pencil manufactured?", "In France by LVMH Guerlain France."),
        ("How do I verify authenticity at Ekleel Abha?", "All Guerlain products at Ekleel Abha are 100% original."),
        (f"What color is Guerlain Eyeliner {shade_num}?", f"Rich intense {shade_en} (Shade {shade_num})."),
        ("Is it suitable for inner waterlines and outer lash lines?", "Yes, safe and effective for inner waterlines and outer lash lines."),
        ("Is the included sharpener convenient?", "Yes, custom sharpener maintains a precise sharp tip at all times."),
        ("How should I store it?", "In a cool, dry place with cap closed tightly."),
        ("Is Guerlain a #1 French luxury eyeliner brand?", "Yes, Guerlain Eyeliner Pencil is a premier French luxury eye makeup essential."),
        ("How long does it hold during the day?", "Holds for 24 continuous hours waterproof and smudge-proof."),
        ("Does it remove easily with makeup remover?", "Yes, removes smoothly with eye makeup remover without tugging delicat eyelid skin."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it glide without tugging eyelids?", "Yes, smooth wax formula glides easily without tugging."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and teens?", "Yes, suitable for both women and teens."),
        ("Is it good for all occasions and daily wear?", "Yes, ideal for daily makeup, events, and evening looks."),
        ("Is it a nice makeup gift?", "Yes, an essential premier French luxury makeup gift."),
        (f"Does it restore sharp eye definition in Shade {shade_num}?", f"Yes, gives eyes a crisp vibrant defined look."),
        ("Are other Guerlain eyeliner shades available?", "Yes, the full Guerlain Eyeliner Pencil shade range is available at Ekleel Abha."),
        ("Does it cause eye stinging?", "Zero irritant fragrance-free formula prevents eye stinging."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Guerlain",
        "ar": {
            "title": ar_title,
            "meta_title": f"{ar_title} | إكليل أبها",
            "meta_description": f"اشتري {ar_title}. قلم كحل فرنسي فاخر ببراية ومقاوم للماء ثبات 24 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. French luxury 24-hour waterproof smudge-proof eyeliner pencil with sharpener. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2189():
    return _make_guerlain_eyeliner_b93(
        pid=2189, gtin="3346470421912",
        ar_title="قلم كحل تحديد العيون كاتي  مع براية  رقم (01)من جيرلان",
        en_title="Eyeliner pencil with sharpener No. (01) from Guerlain",
        shade_num="01", shade_ar="أسود فاحم (كاتي)", shade_en="Katy Black (01)",
        tags_ar=["جيرلان", "قلم_كحل_جيرلان_01", "كحل_جيرلان_مع_براية", "كحل_مقاوم_للماء", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_eyeliner_01", "guerlain_pencil_sharpener", "waterproof_eyeliner", "ekleel_abha"]
    )


def create_product_2190():
    return _make_guerlain_eyeliner_b93(
        pid=2190, gtin="3346470421899",
        ar_title="قلم كحل تحديد العيون بني  مع براية  رقم (02)من جيرلان",
        en_title="Brown eyeliner pencil with sharpener No. (02) from Guerlain",
        shade_num="02", shade_ar="بني", shade_en="Brown (02)",
        tags_ar=["جيرلان", "قلم_كحل_جيرلان_02_بني", "كحل_جيرلان_مع_براية", "كحل_مقاوم_للماء", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_brown_eyeliner_02", "guerlain_pencil_sharpener", "waterproof_eyeliner", "ekleel_abha"]
    )


def create_product_2191():
    return _make_guerlain_eyeliner_b93(
        pid=2191, gtin="3346470421929",
        ar_title="قلم كحل تحديد العيون كاكي مع براية  رقم (05)من جيرلان",
        en_title="Khaki eyeliner pencil with sharpener No. (05) from Guerlain",
        shade_num="05", shade_ar="كاكي", shade_en="Khaki (05)",
        tags_ar=["جيرلان", "قلم_كحل_جيرلان_05_كاكي", "كحل_جيرلان_مع_براية", "كحل_مقاوم_للماء", "إكليل_أبها"],
        tags_en=["guerlain", "guerlain_khaki_eyeliner_05", "guerlain_pencil_sharpener", "waterproof_eyeliner", "ekleel_abha"]
    )


print("Loaded all 5 Batch 93 builders complete")
