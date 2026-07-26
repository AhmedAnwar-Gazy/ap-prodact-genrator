import json, os

def _make_nyx_primer_b99(pid, gtin, ar_title, en_title, shade_code, shade_ar, shade_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_title}</strong> البرايمر الملون الطبي المعادل للون ومصفي البشرة الفاخر من الدار الأمريكية الشهيرة نيكس (NYX Professional Makeup Tinted Primer) المصمم خصيصاً لتصحيح شوائب وعيوب لون بشرة الوجه، إخفاء المسام الواسعة، وتوفير قاعدة حريرية موحدة تزيد ثبات كريم الأساس لـ 24 ساعة دون تكتل أو جفاف. يرتكز هذا المستحضر الأمريكي الأصيل ({en_title}) على الصبغات الملونة الخفيفة المصححة ({shade_ar})، مجمع السليكون الحريري المنعم، وفيتامين E المحافظ على الرطوبة.</p>
<p>يعمل برايمر نيكس الملون بدرجة {shade_code} على توحيد لون البشرة، ملس سطح الجلد، وإخفاء اللمعان والزيوت الزائدة، ليترك بشرتك ناعمة كالحرير، مرطبة، موحدة اللون بدرجة {shade_ar}، ومجهزة كلياً لاستقبال المكياج بثبات لـ 24 ساعة من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>توحيد وتصفية ناعمة للبشرة الملونة (درجة {shade_code} - {shade_ar}):</strong> يزيل العيوب الخفيفة فورياً.</li>
  <li><strong>تثبيت وإطالة عمر كريم الأساس لـ 24 ساعة:</strong> يمنع تكتل أو سيلان المكياج بالحرارة.</li>
  <li><strong>إخفاء وتنعيم المسام والخطوط الدقيقة:</strong> يوفر سطحاً ناعماً كالحرير قبل الأساس.</li>
  <li><strong>ترطيب وتغذية فائقة بفيتامين E ومجمع السليكون:</strong> يحفظ الرطوبة الداخلية لـ 24 ساعة.</li>
  <li><strong>تركيبة خفيفة خالية من الزيوت ومختبرة جلدياً:</strong> 100% آمنة لجميع أنواع البشرة.</li>
  <li><strong>أنبوب أنيق سعة 25 مل بحجم مالي ممتاز:</strong> مريح للحقيبة ولليوميات.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية صغيرة من برايمر نيكس الملون على بشرة الوجه النظيفة والمرطبة.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي البرايمر بالأصابع أو الإسفنجة على كامل الوجه بالتساوي.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركي البرايمر لمدة دقيقة واحدة ثم ضعي كريم الأساس المفضل لديك (يُستعمل daily قبل المكياج).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الصبغات المصححة الخفيفة وفيتامين E:</strong> تحايد العيوب وتصلح اللون وتحبس رطوبة الجلد.</li>
  <li><strong>بوليمرات السليكون التمهيدية:</strong> تنعم المسام وتمنع ثقل المكياج على أدمة الوجه.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي التجميلي على بشرة الوجه والرقبة.</li>
  <li>تجنبي التلامس المباشر لداخل العين واغلقي الغطاء بإحكام.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن {ar_title} لتوحيد وتصفية لون البشرة وتثبيت المكياج لـ 24 ساعة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>نيكس بروفيشنال مكياج (NYX Professional Makeup USA)</td></tr>
  <tr><th>الفئة</th><td>مكياج الوجه / برايمرات ومصفيات نيكس الملونة 25ml</td></tr>
  <tr><th>نوع المنتج</th><td>برايمر ملون ومصفي للبشرة بحمض الهيالورونيك وفيتامين E (درجة {shade_code} - {shade_ar})</td></tr>
  <tr><th>الحجم/الوزن</th><td>25 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (العادية، الجافة، الدهنية والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، موحد اللون بدرجة {shade_ar} ومجهز لمكياج 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>كريمي مخملي خفيف ينزلق ويمتص بسلاسة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور المهيجة</td></tr>
  <tr><th>المكونات النشطة</th><td>صبغات ناعمة ملونة، فيتامين E، مجمع السليكون المنعم</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة الأمريكية (USA) / الصين</td></tr>
  <tr><th>الشركة المصنعة</th><td>NYX Professional Makeup L'Oréal USA</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد الصبغات المصححة الملونة وفيتامين E في برايمر نيكس (NYX Tinted Primer {shade_code})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج برايمر نيكس الملون مشكلة تفاوت لون الوجه، المسام الواسعة، تلاشي المكياج، واللمعان الدهني.</p>

<h3>لماذا تنجح تركيبة NYX Tinted Primer Shade {shade_code}؟</h3>
<p>لأن الصبغات الخفيفة تعادل اللون بينما ينعم مجمع السليكون المسام ويمتص الزيوت.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على البشرة النظيفة قبل كريم الأساس:</strong> يضمن توزيعاً مخملياً متجانساً.<br>
2. <strong>الانتظار دقيقة قبل وضع الفاونديشن:</strong> يتيح للبرايمر امتصاص الزيوت والثبات.<br>
3. <strong>إغلاق الغطاء بإحكام:</strong> يحفظ طراوة ونقاء البرايمر.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "البرايمرات الملونة تسبب انسداد المسام وتثقل المكياج."<br>
<strong>الحقيقة:</strong> برايمر نيكس مصمم بتركيبة خفيفة خالية من الزيوت تتيح للبشرة التنفس طوال اليوم.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تندمج بوليمرات السليكون مع صبغات التصفية لتخلق درعاً حريرياً يحفظ رطوبة أدمة الجلد.</p>"""

    faqs_data = [
        (f"ما هو {ar_title}؟", f"هو برايمر ملون ومصفي للبشرة بفيتامين E ومجمع السليكون المنعم بدرجة {shade_code} من نيكس (25 مل)."),
        (f"ما هي فوائد الصبغات الملونة وفيتامين E بدرجة {shade_code}؟", "توحد لون البشرة، تنعم المسام، وتثبت كريم الأساس لـ 24 ساعة دون جفاف أو تكتل."),
        ("هل يصحح لون البشرة ويثبت المكياج لـ 24 ساعة بدون تكتل؟", "نعم، مثبت سريرياً في توحيد لون الوجه وتثبيت كريم الأساس 24 ساعة وتنعيم المسام."),
        ("ما حجم العبوة؟", "تأتي بأنبوب أنيق سعة 25 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على البشرة، وزعي على كامل الوجه بالتساوي، انتظري دقيقة ثم ضعي كريم الأساس."),
        ("هل هو خالٍ من العطور وآمن لجميع أنواع البشرة؟", "نعم، 100% خالٍ من العطور ومختبر جلدياً وآمن لجميع أنواع البشرة."),
        ("أين صُنع برايمر نيكس الملون؟", "صُنع بواسطة NYX Professional Makeup L'Oréal USA."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات نيكس لدى إكليل أبها أصلية 100%."),
        (f"ما درجة برايمر نيكس الملون؟", f"درجة {shade_code} ({shade_ar})."),
        ("هل يناسب البشرة الجافة والدهنية والمختلطة والمسام؟", "نعم، ممتاز لجميع أنواع البشرة وإخفاء المسام واللمعان الزائد."),
        ("هل أنبوب 25 مل مريح ومناسب للاستخدام اليومي؟", "نعم، أنبوب أنيق ومريح جداً للاستخدام اليومي والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل نيكس الماركة الأمريكية الأولى في البرايمرات الملونة؟", "نعم، NYX Tinted Primer البرايمر الملون رقم 1 الأكثر تفضيلاً بعالم مكياج الوجه."),
        ("كم يدوم ثباته طوال اليوم؟", "يدوم لـ 24 ساعة متواصلة دون تلاشي أو تكتل."),
        ("هل ينشطف بمزيل المكياج بسهولة؟", "نعم، ينشطف بسلاسة بمزيل المكياج دون شد البشرة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع سيلان وتلاشي كريم الأساس؟", "نعم، يشكل درعاً يمنع امتصاص البشرة لكريم الأساس أو تكتله."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والفتيات؟", "نعم، ممتاز للنساء والفتيات."),
        ("هل يناسب جميع فصول السنة؟", "نعم، تصحيح وتثبيت مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن مكياج الوجه؟", "نعم، منتج مكياج أمريكي فاخر وأساسي لكل حقيبة تجميل."),
        (f"هل يعيد المظهر المشرق الموحد للبشرة بدرجة {shade_code}؟", f"نعم، يمنح البشرة مظهراً موحداً وناصع النقاء كالحرير."),
        ("هل تتوفر درجات برايمر نيكس الملون الأخرى؟", "نعم، تتوفر عائلة NYX Tinted Primers كاملة لدى إكليل أبها."),
        ("هل يمكن استخدامه بمفرده دون فاونديشن؟", "نعم، يمكن استخدامه بمفرده لتوحيد وتنعيم البشرة وتعديل اللمعان."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury tone-correcting, pore-blurring, and 24-hour face primer from iconic US brand NYX Professional Makeup (NYX Professional Makeup Tinted Primer) designed to correct skin discolorations, unify facial complexions, and prep skin for 24-hour foundation hold without creasing or drying. Built upon color-correcting micro-pigments ({shade_en}), a silky silicone complex, and moisture-retaining Vitamin E.</p>
<p>NYX Tinted Primer (Shade {shade_code}) neutralizes sallowness and uneven skin tones, fills enlarged pores and fine lines, and controls excess shine, leaving your facial skin touchably silky soft, hydrated, even-toned in {shade_en}, and perfectly prepared for 24-hour makeup from first stroke.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Tone Correction & Soft Complexion Unification (Shade {shade_code} - {shade_en}):</strong> Conceals minor discolorations instantly.</li>
  <li><strong>24-Hour Foundation Fixation & Wear Extension:</strong> Prevents makeup creasing, sliding, or fading.</li>
  <li><strong>Blurs & Smooths Enlarged Pores & Fine Lines:</strong> Creates a silky smooth canvas prior to foundation.</li>
  <li><strong>Intensive Hydration with Vitamin E & Silicone Complex:</strong> Preserves internal facial skin moisture.</li>
  <li><strong>Oil-Free & Dermatologically Tested Safe Formula:</strong> 100% safe for all facial skin types.</li>
  <li><strong>Sleek 25ml Tube Container:</strong> Outstanding value for daily professional face prepping.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a small amount of NYX tinted primer onto clean, moisturized facial skin.</li>
  <li><strong>Step 2:</strong> Spread primer evenly over the face using fingers or a sponge.</li>
  <li><strong>Step 3:</strong> Allow primer to set for 1 minute before applying your favorite foundation (use daily prior to makeup).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Color-Correcting Micro-Pigments & Vitamin E:</strong> Offset discolorations while locking in skin moisture.</li>
  <li><strong>Silicone Prepping Polymers:</strong> Smooth skin texture and prevent heavy makeup from sinking into pores.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on facial and neck skin.</li>
  <li>Avoid direct contact inside eyes and cap tightly after use.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_title} for tone correction, pore smoothing, and 24-hour makeup hold.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>NYX Professional Makeup (USA)</td></tr>
  <tr><th>Category</th><td>Face Makeup / NYX Tinted Face Primers 25ml</td></tr>
  <tr><th>Product Type</th><td>24-Hour Tone-Correcting Vitamin E Face Primer (Shade {shade_code})</td></tr>
  <tr><th>Volume/Weight</th><td>25 ml Tube</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Normal, Dry, Oily & Combination Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, even-toned in {shade_en} & makeup-ready face</td></tr>
  <tr><th>Texture</th><td>Ultra-lightweight fast-absorbing fluid cream</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (irritant-free)</td></tr>
  <tr><th>Active Ingredients</th><td>Color-Correcting Pigments, Vitamin E, Silicone Smoothing Complex</td></tr>
  <tr><th>Country of Origin</th><td>USA / China</td></tr>
  <tr><th>Manufacturer</th><td>NYX Professional Makeup L'Oréal USA</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Color Correcting Pigments & Silicone Smooth Matrix</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves uneven facial skin tone, enlarged pores, foundation sliding, and excess shine.</p>

<h3>Why choose NYX Tinted Primer {shade_code}?</h3>
<p>Color-correcting micro-pigments neutralize discolorations while the silicone complex smoothes skin texture and absorbs excess oil.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a professional 24-hour tone-correcting face primer with Vitamin E from NYX Professional Makeup (Shade {shade_code} / 25ml)."),
        (f"What are the benefits of Color Correcting Pigments and Vitamin E in Shade {shade_code}?", "Neutralize discolorations, blur enlarged pores and fine lines, and extend foundation hold for 24 hours without dryness."),
        ("Does it correct skin tone and extend foundation hold for 24 hours?", "Yes, clinically proven to neutralize tone imperfections, smooth pores, and lock foundation for 24 hours."),
        ("What volume is contained in this tube?", "25ml sleek tube."),
        ("How do I use it correctly?", "Apply small amount to clean skin, spread evenly over face, wait 1 minute and apply foundation."),
        ("Is it safe and dermatologically tested?", "Yes, 100% safe, dermatologically tested, and suitable for all facial skin types."),
        ("Where is NYX Tinted Primer manufactured?", "By NYX Professional Makeup L'Oréal USA."),
        ("How do I verify authenticity at Ekleel Abha?", "All NYX products at Ekleel Abha are 100% original."),
        (f"What shade is NYX Tinted Primer?", f"Shade {shade_code} ({shade_en})."),
        ("Is it suitable for dry, oily, and combination skin?", "Yes, excellent for all skin types and blurring enlarged pores."),
        ("Is the 25ml tube convenient for daily use?", "Yes, sleek tube ideal for daily use and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is NYX a #1 professional primer brand?", "Yes, NYX Tinted Primer is a premier trusted US face primer."),
        ("How long does it hold during the day?", "Holds for 24 continuous hours without fading or creasing."),
        ("Does it remove easily with makeup remover?", "Yes, removes smoothly with makeup remover without tugging skin."),
        ("Is the tube recyclable?", "Yes."),
        ("Does it prevent foundation sliding and creasing?", "Yes, forms a protective shield preventing foundation from sliding into pores."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and teens?", "Yes, suitable for both women and teens."),
        ("Is it good for all seasons?", "Yes, ideal tone correction for summer and winter routines."),
        ("Is it a nice makeup gift?", "Yes, an essential premier US professional makeup prep gift."),
        (f"Does it restore smooth even-toned skin in Shade {shade_code}?", f"Yes, gives facial skin a healthy smooth even-toned look."),
        ("Are other NYX Tinted Primer shades available?", "Yes, the full NYX Tinted Primer range is available at Ekleel Abha."),
        ("Can it be worn alone without foundation?", "Yes, can be worn alone to neutralize tone imperfections and smooth skin texture."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "NYX",
        "ar": {
            "title": ar_title,
            "meta_title": f"{ar_title} | إكليل أبها",
            "meta_description": f"اشتري {ar_title}. برايمر ملون أمريكي مصحي للبشرة بفيتامين E وتثبيت 24 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. US professional 24-hour tone-correcting Vitamin E face primer. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2217():
    return _make_nyx_primer_b99(
        pid=2217, gtin="800897056148",
        ar_title="برايمر ملون  p01 كلير خفيف  من نيكس 25مل",
        en_title="NYX Tinted Primer P01 Clear Light - 25ml",
        shade_code="P01", shade_ar="كلير خفيف (Clear Light)", shade_en="Clear Light",
        tags_ar=["نيكس", "برايمر_نيكس_P01", "برايمر_ملون_نيكس", "برايمر_كلير_خفيف", "إكليل_أبها"],
        tags_en=["nyx", "nyx_tinted_primer_p01", "clear_light_primer", "face_primer", "ekleel_abha"]
    )


def create_product_2218():
    return _make_nyx_primer_b99(
        pid=2218, gtin="800897056155",
        ar_title="برايمر ملون p02 بيج متوسط  من نيكس 25مل",
        en_title="NYX Tinted Primer P02 Medium Beige - 25ml",
        shade_code="P02", shade_ar="بيج متوسط (Medium Beige)", shade_en="Medium Beige",
        tags_ar=["نيكس", "برايمر_نيكس_P02", "برايمر_ملون_نيكس", "برايمر_بيج_متوسط", "إكليل_أبها"],
        tags_en=["nyx", "nyx_tinted_primer_p02", "medium_beige_primer", "face_primer", "ekleel_abha"]
    )


def _make_nyx_foundation_b99(pid, gtin, ar_title, en_title, shade_name_ar, shade_name_en, volume_str, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_title}</strong> كريم الأساس الفاخر الأسطوري عالي التغطية المات الخالية من اللمعان من الدار الأمريكية الشهيرة نيكس (NYX Professional Makeup HD Studio / Stay Matte Liquid Foundation) المصمم خصيصاً لمنح بشرة وجهك تغطية مخملية مثالية، إخفاء المسام والتصبغات 100%، والتحكم باللمعان والزيوت الزائدة لـ 24 ساعة دون تكتل أو جفاف. يرتكز هذا المستحضر الأمريكي الأصيل ({en_title}) على صبغات HD عالية الدقة، المركبات المطفأة للمعة (Matte Complex)، والمركبات المطرية المائية.</p>
<p>يعمل كريم أساس نيكس السائل بدرجة {shade_name_ar} على التكيف مع تعبيرات وجهك، امتصاص إفرازات الدهون الزائدة، وإخفاء المسام والخطوط الدقيقة، ليترك بشرتك ناعمة كالحرير، موحدة اللون بدرجة {shade_name_ar}، ومفعمة بالنقاء والمظهر المات المشرق أمام الكاميرات وفي الضوء الطبيعي من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تغطية مخملية مات خالية من اللمعان والزيوت ({shade_name_ar}):</strong> يزيل التصبغات والعيوب.</li>
  <li><strong>ثبات عالي لـ 24 ساعة مقاوم للماء، العرق، والحرارة:</strong> لا يتغير اللون أو يتكتل بالمسام.</li>
  <li><strong>إخفاء وتنعيم المسام والخطوط الدقيقة بصبغات HD:</strong> مظهر غير مرئي أمام الكاميرات.</li>
  <li><strong>ترطيب وتغذية ممتدة تحافظ على مرونة البشرة:</strong> يمنع الجفاف والتشقق.</li>
  <li><strong>تركيبة خالية من الكرولتي ومختبرة من أطباء الجلدية:</strong> 100% آمنة لجميع أنواع البشرة.</li>
  <li><strong>أنبوب مريح وعصري بحجم {volume_str}:</strong> مالي وممتاز للاستخدام اليومي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسبة من كريم أساس نيكس على بشرة الوجه النظيفة والمرطبة.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي الكريم من منتصف الوجه للخارج باستخدام الإسفنجة أو فرشاة الأساس.</li>
  <li><strong>الخطوة الثالثة:</strong> ادمجي برفق للحصول على تغطية متجانسة ومات مشرقة (يُستعمل daily وعند المكياج).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>صبغات HD عالية الدقة والمركبات المطفأة:</strong> تضمن تغطية مات مخملية وتمتص الدهون.</li>
  <li><strong>العوامل المطرية الحريرية:</strong> تحفظ طراوة الجلد وتمنع التجمع بالخطوط الدقيقة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي التجميلي على بشرة الوجه والرقبة.</li>
  <li>تجنبي التلامس المباشر لداخل العين واغلقي الغطاء بإحكام.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن {ar_title} لتغطية وتوحيد وإطفاء لمعان البشرة لـ 24 ساعة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>نيكس بروفيشنال مكياج (NYX Professional Makeup USA)</td></tr>
  <tr><th>الفئة</th><td>مكياج الوجه / كريمات أساس نيكس المات والمصورة HD {volume_str}</td></tr>
  <tr><th>نوع المنتج</th><td>كريم أساس سائل مات عالي التغطية والتحكم بالدهون ({shade_name_ar})</td></tr>
  <tr><th>الحجم/الوزن</th><td>{volume_str}</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (خصيصاً البشرة الدهنية والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، موحد اللون بدرجة {shade_name_ar} ومات خالي كلياً من اللمعان</td></tr>
  <tr><th>الملمس</th><td>سائل دسم خفيف ينزلق ويمتص بسلاسة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور المهيجة</td></tr>
  <tr><th>المكونات النشطة</th><td>صبغات HD عالية الدقة، مركب مطفأ للدهون Matte Complex، مرطبات حريرية</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة الأمريكية (USA) / الصين</td></tr>
  <tr><th>الشركة المصنعة</th><td>NYX Professional Makeup L'Oréal USA</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد صبغات HD والمركب المطفأ في كريم أساس نيكس (NYX Foundation {shade_name_ar})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم أساس نيكس المات مشكلة اللمعان الدهني، تكتل المسام، تلاشي الفاونديشن بالحرارة، وتفاوت اللون.</p>

<h3>لماذا تنجح تركيبة NYX Liquid Foundation {shade_name_ar}؟</h3>
<p>لأن المركبات المطفأة تمتص الإفرازات الدهنية الزائدة بينما تعكس صبغات HD الضوء بنعومة كالحرير.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على بشرة مرطبة بـ برايمر نيكس:</strong> يضمن توزيعاً متجانساً ومات ثابتاً.<br>
2. <strong>الدمج السريع بالإسفنجة أو الفرشاة:</strong> يمنح تغطية مخملية غير متبقعة.<br>
3. <strong>إغلاق العبوة بإحكام:</strong> يحفظ طراوة القوام السائل من الجفاف.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات الأساس المات تجفف الوجه وتظهر التجاعيد."<br>
<strong>الحقيقة:</strong> كريم أساس نيكس مدعم بعوامل مطرية مائية تمنع الجفاف وتحفظ مرونة الجلد طوال اليوم.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبت بوليمرات المات على السطح ممتصة الزيوت الزائدة فور فرزها من الغدد الدهنية.</p>"""

    faqs_data = [
        (f"ما هو {ar_title}؟", f"هو كريم أساس سائل مات عالي التغطية والتحكم بالدهون بصبغات HD بدرجة {shade_name_ar} من نيكس ({volume_str})."),
        (f"ما هي فوائد صبغات HD والمركب المطفأ بدرجة {shade_name_ar}؟", "توحد لون البشرة، تخفي العيوب والمسام، وتمتص اللمعان والزيوت الزائدة لـ 24 ساعة دون جفاف."),
        ("هل يغطي العيوب ويمتص اللمعان لـ 24 ساعة بدون تكتل؟", "نعم، مثبت سريرياً في إطفاء اللمعان وتوحيد البشرة وتغطية المسام لـ 24 ساعة."),
        ("ما حجم العبوة؟", f"تأتي بأنبوب عصري مريح بسعة {volume_str}."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على البشرة، وزعي بالإسفنجة أو الفرشاة واددمجي من المنتصف للخارج."),
        ("هل هو آمن ومختبر درماتولوجياً؟", "نعم، 100% آمن ومختبر درماتولوجياً ومناسب لجميع أنواع البشرة."),
        ("أين صُنع كريم أساس نيكس؟", "صُنع بواسطة NYX Professional Makeup L'Oréal USA."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات نيكس لدى إكليل أبها أصلية 100%."),
        (f"ما درجة كريم أساس نيكس؟", f"درجة {shade_name_ar}."),
        ("هل يناسب البشرة الدهنية والمختلطة والعادية؟", "نعم، ممتاز خصيصاً للبشرة الدهنية والمختلطة وللتحكم بالزيوت."),
        ("هل عبوة {volume_str} مريحة ومناسبة؟", f"نعم، أنبوب أنيق ومريح جداً للاستخدام اليومي والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل نيكس الماركة الأمريكية الأولى في كريمات الأساس المات؟", "نعم، NYX Professional Makeup الماركة الأمريكية رقم 1 الأكثر تفضيلاً بكريمات الأساس المات."),
        ("كم يدوم ثباته طوال اليوم؟", "يدوم لـ 24 ساعة متواصلة دون تلطخ أو تغير باللون."),
        ("هل ينشطف بمزيل المكياج بسهولة؟", "نعم، ينشطف بسلاسة بمزيل المكياج دون شد البشرة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يخفي المسام والخطوط الدقيقة؟", "نعم، ينعم البشرة ويخفي المسام والخطوط الدقيقة بفاعلية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والفتيات؟", "نعم، ممتاز للنساء والفتيات."),
        ("هل يناسب المناسبات والتصوير والمكياج اليومي؟", "نعم، ممتاز للمكياج اليومي والتصوير عالي الدقة."),
        ("هل يصلح هدية ممتازة ضمن مكياج الوجه؟", "نعم، منتج مكياج أمريكي فاخر وأساسي لكل امرأة راقية."),
        (f"هل يعيد المظهر المات الموحد للبشرة بدرجة {shade_name_ar}؟", f"نعم، يمنح الوجه مظهراً موحداً ومات ناصع النقاء كالحرير."),
        ("هل تتوفر درجات كريم أساس نيكس الأخرى؟", "نعم، تتوفر عائلة NYX Foundations كاملة لدى إكليل أبها."),
        ("هل هو خالي من الكرولتي ولم يُجرب على الحيوانات؟", "نعم، علامة معتمدة 100% خالية من التجريب على الحيوانات (Cruelty-Free)."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury high-coverage matte liquid foundation from iconic US brand NYX Professional Makeup (NYX Professional Makeup HD Studio / Stay Matte Liquid Foundation) designed to deliver flawless velvet coverage, 100% pore and blemish concealment, and 24-hour oil control without creasing or drying. Built upon high-definition HD pigments, a matting complex, and hydrating emollients.</p>
<p>NYX Liquid Foundation in Shade {shade_name_en} smoothly flexes with facial expressions, absorbs excess sebum, and conceals enlarged pores and fine lines, leaving your face touchably silky soft, beautifully even-toned in {shade_name_en}, and camera-ready matte from first stroke.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>High Velvet Matte Coverage & Oil Control ({shade_name_en}):</strong> Conceals spots and blemishes.</li>
  <li><strong>24-Hour Waterproof, Sweat-Proof & Heat-Proof Hold:</strong> Color does not shift or cake.</li>
  <li><strong>Blurs & Smooths Enlarged Pores with HD Pigments:</strong> Camera-invisible natural finish.</li>
  <li><strong>Intensive Extended Hydration Preserves Skin Flexibility:</strong> Prevents dryness and cracking.</li>
  <li><strong>Cruelty-Free & Dermatologically Tested Safe Formula:</strong> 100% safe for all facial skin types.</li>
  <li><strong>Sleek Convenient {volume_str} Container:</strong> Outstanding value for daily luxury makeup.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of NYX foundation onto clean, moisturized skin.</li>
  <li><strong>Step 2:</strong> Smooth from center of face outwards using a makeup sponge or foundation brush.</li>
  <li><strong>Step 3:</strong> Blend gently for a flawless matte illuminated finish (use daily with makeup).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>High-Definition HD Pigments & Matting Complex:</strong> Guarantee velvet matte coverage and absorb sebum.</li>
  <li><strong>Silky Emollient Agents:</strong> Preserve skin softness preventing settlement into fine lines.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on facial and neck skin.</li>
  <li>Avoid direct contact inside eyes and cap tightly after use.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_title} for high-coverage matte finish, oil control, and 24-hour hydration.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>NYX Professional Makeup (USA)</td></tr>
  <tr><th>Category</th><td>Face Makeup / NYX Matte & HD Studio Liquid Foundations {volume_str}</td></tr>
  <tr><th>Product Type</th><td>Professional High-Coverage Matte Liquid Foundation ({shade_name_en})</td></tr>
  <tr><th>Volume/Weight</th><td>{volume_str}</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Specifically Oily, Combination & Normal Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, even-toned in {shade_name_en} & matte shine-free face</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-heavy fluid liquid foundation</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (irritant-free)</td></tr>
  <tr><th>Active Ingredients</th><td>HD Micro-Pigments, Matte Complex, Silky Emollients</td></tr>
  <tr><th>Country of Origin</th><td>USA / China</td></tr>
  <tr><th>Manufacturer</th><td>NYX Professional Makeup L'Oréal USA</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of HD Micro-Pigments & Matting Sebum Control</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves excess facial shine, pore clogging, foundation sliding in heat, and uneven skin tone.</p>

<h3>Why choose NYX Liquid Foundation {shade_name_en}?</h3>
<p>Matte complex polymers absorb excess sebum upon secretion while HD pigments reflect light softly.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a professional high-coverage matte liquid foundation with HD pigments from NYX Professional Makeup in Shade {shade_name_en} ({volume_str})."),
        (f"What are the benefits of HD Pigments and Matte Complex in Shade {shade_name_en}?", "Even skin tone, conceal blemishes, and deliver 24-hour oil control and velvet matte coverage."),
        ("Does it conceal imperfections and control shine for 24 hours?", "Yes, clinically proven to control oil and even skin tone for 24 hours without creasing."),
        ("What volume is contained in this bottle?", f"{volume_str} sleek container."),
        ("How do I use it correctly?", "Apply drops to moisturized skin, smooth with brush or sponge from center outwards."),
        ("Is it safe and dermatologically tested?", "Yes, 100% safe, dermatologically tested, and suitable for all facial skin types."),
        ("Where is NYX Foundation manufactured?", "By NYX Professional Makeup L'Oréal USA."),
        ("How do I verify authenticity at Ekleel Abha?", "All NYX products at Ekleel Abha are 100% original."),
        (f"What shade is NYX Foundation?", f"Shade {shade_name_en}."),
        ("Is it suitable for oily, combination, and normal skin?", "Yes, excellent specifically for oily and combination skin types."),
        (f"Is the {volume_str} container convenient?", "Yes, sleek container ideal for daily use and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is NYX a #1 US matte foundation brand?", "Yes, NYX Professional Makeup is a premier US brand in matte liquid foundations."),
        ("How long does it hold during the day?", "Holds for 24 continuous hours without creasing or color shifting."),
        ("Does it remove easily with makeup remover?", "Yes, removes smoothly with makeup remover without tugging skin."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it blur pores and fine lines?", "Yes, effectively blurs enlarged pores and fine lines."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and teens?", "Yes, suitable for both women and teens."),
        ("Is it good for photoshoots and daily wear?", "Yes, ideal for daily luxury wear, photoshoots, and HD video."),
        ("Is it a nice makeup gift?", "Yes, an essential premier US professional makeup gift."),
        (f"Does it restore smooth matte skin in Shade {shade_name_en}?", f"Yes, gives facial skin an even-toned matte radiant look."),
        ("Are other NYX foundation shades available?", "Yes, the full NYX Foundation shade range is available at Ekleel Abha."),
        ("Is it 100% cruelty-free?", "Yes, NYX is PETA certified 100% cruelty-free."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "NYX",
        "ar": {
            "title": ar_title,
            "meta_title": f"{ar_title} | إكليل أبها",
            "meta_description": f"اشتري {ar_title}. كريم أساس سائل مات أمريكي بصبغات HD وتغطية مخملية لـ 24 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. US professional 24-hour high-coverage HD matte liquid foundation. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2219():
    return _make_nyx_foundation_b99(
        pid=2219, gtin="800897834609",
        ar_title="كريم أساس اتش دي ستوديو بيج رملي من نيكس 30مل",
        en_title="NYX HD Studio Foundation - Sand Beige 30ml",
        shade_name_ar="بيج رملي (Sand Beige)", shade_name_en="Sand Beige", volume_str="30 مل",
        tags_ar=["نيكس", "كريم_أساس_نيكس_اتش_دي", "فاونديشن_بيج_رملي", "كريم_أساس_مات_نيكس", "إكليل_أبها"],
        tags_en=["nyx", "nyx_hd_studio_foundation", "sand_beige_foundation", "matte_foundation", "ekleel_abha"]
    )


def create_product_2220():
    return _make_nyx_foundation_b99(
        pid=2220, gtin="800897047665",
        ar_title="كريم أساس سائل ستاي مات من نيكس 35مل",
        en_title="NYX Stay Matte Liquid Foundation 35ml",
        shade_name_ar="ستاي مات بيج (Stay Matte)", shade_name_en="Stay Matte Beige", volume_str="35 مل",
        tags_ar=["نيكس", "كريم_أساس_نيكس_ستاي_مات", "فاونديشن_ستاي_مات", "كريم_أساس_سائل_نيكس", "إكليل_أبها"],
        tags_en=["nyx", "nyx_stay_matte_foundation", "stay_matte_liquid", "matte_foundation", "ekleel_abha"]
    )


def create_product_2221():
    return _make_nyx_foundation_b99(
        pid=2221, gtin="800897813789",
        ar_title="كريم أساس سائل ستاي مات المرمر من نيكس 35مل",
        en_title="Nyx Stay Matte Liquid Foundation Alabaster 35ml",
        shade_name_ar="المرمر (Alabaster)", shade_name_en="Alabaster", volume_str="35 مل",
        tags_ar=["نيكس", "كريم_أساس_نيكس_المرمر", "فاونديشن_ألاباستر", "كريم_أساس_سائل_نيكس", "إكليل_أبها"],
        tags_en=["nyx", "nyx_alabaster_foundation", "alabaster_stay_matte", "matte_foundation", "ekleel_abha"]
    )


print("Loaded all 5 Batch 99 builders complete")
