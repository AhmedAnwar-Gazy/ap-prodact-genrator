import json, os
from build_batch85 import _make_loreal_prodigy_b85

def create_product_2152():
    return _make_loreal_prodigy_b85(
        pid=2152, gtin="3600522599326",
        ar_title="صبغة شعر بروديجي  لون بني احمر عتيق( 4.60)، من لوريال باريس",
        en_title="L'Oréal Paris Prodigy Hair Color - 4.60 Antique Red Brown",
        shade_num="4.60", shade_ar="بني أحمر عتيق", shade_en="Antique Red Brown",
        tags_ar=["لوريال_بروديجي", "صبغة_بروديجي_4.60", "صبغة_بني_أحمر_عتيق", "صبغة_الزيوت_الدقيقة", "إكليل_أبها"],
        tags_en=["loreal_prodigy", "prodigy_4.60", "antique_red_brown_prodigy", "micro_oil_dye", "ekleel_abha"]
    )


def create_product_2153():
    return _make_loreal_prodigy_b85(
        pid=2153, gtin="3600522599296",
        ar_title="صبغة شعر بروديجي  لون بني فاتح ذهبي ارجواني ( 5.35)، من لوريال باريس",
        en_title="L'Oréal Paris Prodigy Hair Color - 5.35 Chocolate (Light Golden Mahogany Brown)",
        shade_num="5.35", shade_ar="بني فاتح ذهبي أرجواني (شوكولاتة)", shade_en="Light Golden Mahogany Brown (Chocolate)",
        tags_ar=["لوريال_بروديجي", "صبغة_بروديجي_5.35", "صبغة_بني_فاتح_أرجواني", "صبغة_الزيوت_الدقيقة", "إكليل_أبها"],
        tags_en=["loreal_prodigy", "prodigy_5.35", "chocolate_mahogany_prodigy", "micro_oil_dye", "ekleel_abha"]
    )


def _make_lakme_collage_b86(pid, gtin, ar_title, en_title, shade_num, shade_ar, shade_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>{ar_title}</strong> صبغة الشعر الدائمة الاحترافية بالأرغان ومجمع الكولاجين الفاخرة الأصيلة من لاكمي كولاج ميكس إسبانيا (Lakme Collage Mix Permanent Hair Color) المصممة خصيصاً لتمنح شعرك لوناً {shade_ar} ناصعاً، غنياً بالانعكاسات، وثابتاً 100% مع التغطية الكاملة للشيب. تركز هذه الصبغة الإسبانية الأصيلة ({en_title}) على تقنية High Density Color Pigments، مركب AQ-Save الحامي، ونسبة حموضة متوازنة منخفضة الأمونيا.</p>
<p>تعمل صبغة لاكمي كولاج ميكس بدرجة {shade_num} على تزويد خصلات الشعر بلون {shade_ar} ساحر، حماية ألياف كيراتين الشعر من التكسر والجفاف، وإغلاق حراشف الشعر لتثبيت البريق، ليترك شعرك ناعماً كالحرير، مرطباً، ناصع اللون، ومحمياً لعدة أسابيع من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تغطية كاملة 100% للشيب باللون {shade_ar} (درجة {shade_num}):</strong> لون دائم وعميق غني بالانعكاسات.</li>
  <li><strong>حماية ألياف وكيراتين الشعر بتقنية High Density Pigments & AQ-Save:</strong> يمنع الجفاف والتلف.</li>
  <li><strong>نسبة أمونيا منخفضة جداً مع حماية كاملة للفروة:</strong> تضمن صباغة مريحة خالية من التهيج.</li>
  <li><strong>ثبات عالي وبريق زاهٍ يدوم لعدة أسابيع:</strong> يمنع بهتان اللون بفعل الاستحمام والغسيل.</li>
  <li><strong>جودة لاكمي كولاج (Lakme Collage Spain) صالونات التجميل:</strong> الخيار الأول لخبراء التجميل عالمياً.</li>
  <li><strong>أنبوب أنيق سعة 60 مل بحجم مالي ممتاز:</strong> مخصص للدمج الاحترافي وللصبغ الكامل.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> اخلطي كريم صبغة لاكمي كولاج {shade_num} مع أكسجين لاكمي المناسب (18V أو 28V) في وعاء غير معدني بنسبة 1:1.5.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي المزيج الكريمي على الشعر الجاف النظيف من الجذور حتى الأطراف باستخدام فرشاة الصبغة.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركي الصبغة على الشعر لمدة 30-40 دقيقة ثم اشطفي جيداً بالماء الفاتر والشامبو المخصص.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الصبغات الجزيئية عالية الكثافة (High Density Pigments):</strong> تنفذ لعمق ألياف الشعر وتغطي الشيب 100%.</li>
  <li><strong>مجمع AQ-Save والمركبات المطرية:</strong> يغلفان الشعر ويحفظان رطوبته ونعومته الحريرية أثناء الصباغة.</li>
</ul>

<h2>تحذيرات وااحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي المهني والموضعي على شعر الرأس؛ اختبري التحسس قبل 48 ساعة من الاستخدام.</li>
  <li>ارتدي القفازات المناسبة وتجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل خبيرة تجميل وكل امرأة تبحث عن {ar_title} للتغطية الكاملة للشيب وتلوين الشعر باللون {shade_ar}.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لاكمي (Lakme Collage Spain)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / صبغات لاكمي كولاج الاحترافية 60ml</td></tr>
  <tr><th>نوع المنتج</th><td>صبغة شعر دائمة احترافية منخفضة الأمونيا لتغطية الشيب (درجة {shade_num})</td></tr>
  <tr><th>الحجم/الوزن</th><td>أنبوب الصبغة 60 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (خصيصاً الجاف، المجهد، والشعر المصاب بالشيب)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم كالحرير، مرطب 24 ساعة، بلون {shade_ar} ناصع وتغطية شيب 100%</td></tr>
  <tr><th>الملمس</th><td>كريم صبغة غني متماسك يسهل الدمج والخلط مع الأكسجين</td></tr>
  <tr><th>العطر</th><td>عطر كتم كريمي لطيف محايد</td></tr>
  <tr><th>المكونات النشطة</th><td>صبغات عالية الكثافة High Density Pigments، مجمع AQ-Save المصلح</td></tr>
  <tr><th>بلد المنشأ</th><td>إسبانيا (Spain)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Lakme Cosmetics Spain</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون (من 18 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد تقنية High Density Pigments ومجمع AQ-Save في صبغة لاكمي كولاج (Lakme Collage {shade_num})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج صبغة لاكمي كولاج بدرجة {shade_num} مشكلة الشيب، جفاف الشعر المبوغ بالصبغات العادية، وتغير التدرج الصبغي بفعل الغسيل.</p>

<h3>لماذا تنجح تركيبة Lakme Collage Mix {shade_num}?</h3>
<p>لأن جزيئات الصبغة المرتفعة الكثافة تنفذ لقلب الشعر بينما تحمي مركبات AQ-Save بروتينات الكيراتين الطبيعية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الخلط بنسبة 1:1.5 مع أكسجين لاكمي:</strong> يضمن تفعيلاً متجانساً للون {shade_ar}.<br>
2. <strong>الالتزام بوقت الانتظار (30-40 دقيقة):</strong> يضمن تغطية 100% للشيب.<br>
3. <strong>الشطف بالماء الفاتر واستخدام بلسم مثبت:</strong> يغلق حراشف الشعر ويحفظ بريق اللون.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "صبغات الصالونات الإسبانية تجفف الشعر بسبب تركيز الصبغات."<br>
<strong>الحقيقة:</strong> صبغة لاكمي كولاج مدعمة بمجمع AQ-Save المرطب الذي يحفظ طراوة ونعومة الشعر أثناء الصباغة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>ترتبط الجزيئات عالية الكثافة بكيراتين أدمة الشعر وتمنح تغطية لونية ثابتة تدوم لعدة أسابيع.</p>"""

    faqs_data = [
        (f"ما هي {ar_title}؟", f"هي صبغة شعر دائمة احترافية منخفضة الأمونيا لتغطية الشيب 100% باللون {shade_ar} (درجة {shade_num}) من لاكمي كولاج (60 مل)."),
        (f"ما هي فوائد High Density Pigments ومجمع AQ-Save في صبغة لاكمي {shade_num}؟", f"تغطي الشيب 100%، تحمي كيراتين الشعر من التلف، وتمنح لون {shade_ar} ناصعاً وثابتاً."),
        (f"هل تغطي الشيب 100% وتمنح لون {shade_ar} بدون جفاف؟", f"نعم، مثبتة سريرياً في تغطية 100% للشيب وتوفير لون {shade_ar} غني وثابت بفضل تقنية لاكمي الإسبانية."),
        ("ما حجم العبوة؟", "تأتي بأنبوب صبغة احترافي سعة 60 مل."),
        ("كيف تُستخدم بالشكل الصحيح؟", "اخلطي مع أكسجين لاكمي بنسبة 1:1.5 في وعاء غير معدني، وزعي على الشعر الجاف، اتركي 30-40 دقيقة واشطفي بالماء والشامبو."),
        ("هل هي منخفضة الأمونيا وآمنة للفروة؟", "نعم، مصممة بنسبة أمونيا منخفضة جداً لحماية الفروة والشعر."),
        ("أين صُنت صبغة لاكمي كولاج؟", "صُنت في إسبانيا بواسطة Lakme Cosmetics Spain."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لاكمي لدى إكليل أبها أصلية 100%."),
        (f"ما لون صبغة لاكمي كولاج {shade_num}؟", f"لون {shade_ar} غني وناصع (درجة {shade_num})."),
        ("هل تناسب جميع أنواع الشعر والشيب؟", "نعم، ممتازة لجميع أنواع الشعر والتغطية الكاملة للشيب المزعج."),
        ("هل العبوة مريحة للدمج والخلط؟", "نعم، أنبوب احترافي دقيق مخصص لخلط ودمج درجات الصبغة بالصالون والمنزل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل لاكمي كولاج الصبغة الإسبانية الأولى في صالونات التجميل؟", "نعم، Lakme Collage الصبغة الإسبانية الاحترافية رقم 1 الأكثر تفضيلاً وشهرة بالصالونات."),
        ("كم يدوم ثبات اللون؟", "يدوم لعدة أسابيع متواصلة بنفس الزهاء."),
        ("هل ينشطف بسهولة دون ترك لزوجة؟", "نعم، ينشطف بالماء الدافئ والشامبو بسلاسة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع تقصف وخشونة الشعر المصبوغ؟", "نعم، بمجمع AQ-Save يمنع الخشونة والتقصف وزيادة النعومة الحريرية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يناسب الشتاء والصيف؟", "نعم، صباغة وحماية مثالية لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة للعناية بالشعر؟", "نعم، منتج صباغة وتنعيم فاخر وأساسي لكل روتين جمال."),
        (f"هل يعيد المظهر المشرق الناعم للون {shade_ar}؟", f"نعم، يمنح الشعر مظهراً ناصع اللون {shade_ar} ومفعماً بالبريق."),
        ("هل تتوفر درجات صبغة لاكمي كولاج الأخرى؟", "نعم، تتوفر عائلة Lakme Collage كاملة لدى إكليل أبها."),
        ("هل يفضل إجراء اختبار تحسس قبل الاستخدام؟", "نعم، يُنصح دائماً باختبار التحسس الموضعي قبل 48 ساعة."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury low-ammonia permanent hair color tube from Lakme Collage Mix Spain designed to deliver 100% gray coverage, vibrant {shade_en} color (Shade {shade_num}), and deep hair fiber protection. Built upon High Density Color Pigments, the protective AQ-Save complex, and a balanced low-ammonia formulation.</p>
<p>Lakme Collage Mix Hair Dye Shade {shade_num} diffuses rich {shade_en} pigments into hair fibers, shields internal keratin structures from dryness, and seals hair cuticles for lasting gloss, leaving your hair touchably silky soft, hydrated, brilliantly colored, and protected from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Gray Coverage with Rich {shade_en} Color (Shade {shade_num}):</strong> Deep permanent finish with multi-dimensional shine.</li>
  <li><strong>Keratin Fiber Protection with High Density Pigments & AQ-Save:</strong> Prevents chemical dryness and damage.</li>
  <li><strong>Ultra-Low Ammonia Formula Safe for Scalp:</strong> Ensures comfortable non-irritating application.</li>
  <li><strong>Long-Lasting Color Vibrancy for Weeks:</strong> Resists color fading from washing and sun exposure.</li>
  <li><strong>Professional Spanish Lakme Collage Salon Quality:</strong> #1 choice for hair stylists worldwide.</li>
  <li><strong>Sleek 60ml Professional Tube:</strong> Ideal size for precise salon and home color mixing.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Mix Lakme Collage color tube Shade {shade_num} with Lakme developer cream (18V or 28V) in a non-metallic bowl at 1:1.5 ratio.</li>
  <li><strong>Step 2:</strong> Apply the smooth creamy mixture onto clean dry hair from roots to tips using a tint brush.</li>
  <li><strong>Step 3:</strong> Leave dye on hair for 30-40 minutes, then rinse thoroughly with warm water and color shampoo.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>High Density Color Pigments:</strong> Penetrate deep into hair fibers providing 100% gray coverage in {shade_en}.</li>
  <li><strong>AQ-Save Complex & Emollients:</strong> Coat hair strands preserving moisture and silky smoothness during chemical processing.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external professional topical head hair application; perform an allergy test 48 hours prior to use.</li>
  <li>Wear suitable gloves and avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_title} for 100% gray coverage, {shade_en} hair coloring, and salon-grade hair protection.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lakme Collage (Spain)</td></tr>
  <tr><th>Category</th><td>Hair Care / Lakme Collage Professional Hair Dyes 60ml</td></tr>
  <tr><th>Product Type</th><td>Low-Ammonia High Density Pigment Permanent Hair Dye Tube (Shade {shade_num})</td></tr>
  <tr><th>Volume/Weight</th><td>60 ml Color Tube</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Specifically Dry, Stressed & Gray-Plagued Hair)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, 100% gray-covered & vibrant {shade_en} hair</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-drip professional color cream</td></tr>
  <tr><th>Fragrance</th><td>100% Mild gentle neutral scent (low-ammonia)</td></tr>
  <tr><th>Active Ingredients</th><td>High Density Color Pigments, AQ-Save Complex, Low-Ammonia Base</td></tr>
  <tr><th>Country of Origin</th><td>Spain</td></tr>
  <tr><th>Manufacturer</th><td>Lakme Cosmetics Spain</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 18+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of High Density Pigment Integration & AQ-Save Cuticle Shielding</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves gray hair coverage, fading hair dye tones, post-dye hair damage, and scalp irritation.</p>

<h3>Why choose Lakme Collage Mix Shade {shade_num}?</h3>
<p>High Density Color Pigments diffuse deep into the hair cortex while the AQ-Save complex coats the cuticle layer preventing moisture loss.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a professional low-ammonia permanent hair dye tube from Lakme Collage Spain for 100% gray coverage in {shade_en} (Shade {shade_num} / 60ml)."),
        (f"What are the benefits of High Density Pigments and AQ-Save in Shade {shade_num}?", f"Provide 100% gray coverage, protect keratin fibers, and deliver vibrant {shade_en} color without dryness."),
        (f"Does it cover 100% gray hair in {shade_en} without damage?", f"Yes, clinically proven to deliver 100% gray coverage in {shade_en} with AQ-Save hair protection."),
        ("What volume is contained in this tube?", "60ml professional color tube."),
        ("How do I use it correctly?", "Mix color tube with Lakme developer at 1:1.5 ratio, apply to dry hair, process 30-40 minutes and rinse thoroughly."),
        ("Is it low-ammonia and safe for scalp?", "Yes, formulated with ultra-low ammonia for comfortable non-irritating application."),
        ("Where is Lakme Collage Hair Dye manufactured?", "In Spain by Lakme Cosmetics Spain."),
        ("How do I verify authenticity at Ekleel Abha?", "All Lakme products at Ekleel Abha are 100% original."),
        (f"What color shade is Lakme Collage {shade_num}?", f"Rich vibrant {shade_en} (Shade {shade_num})."),
        ("Is it suitable for all hair types and gray coverage?", "Yes, excellent for all hair types and complete gray hair coverage."),
        ("Is the 60ml tube convenient for salon and home mixing?", "Yes, precise 60ml tube ideal for exact color mixing at home or in salons."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Lakme Collage a #1 salon brand in Spain?", "Yes, Lakme Collage is the premier Spanish professional salon hair color line."),
        ("How long does the color stay vibrant?", "Stays vibrant for continuous weeks."),
        ("Does it rinse out smoothly?", "Yes, rinses out smoothly with warm water and color shampoo."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it prevent post-dye hair roughness?", "Yes, AQ-Save complex preserves natural hair moisture preventing post-dye roughness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it good for all seasons?", "Yes, ideal hair coloring for summer and winter care."),
        ("Is it a nice hair care gift?", "Yes, a premier luxury hair dye for daily beauty routines."),
        (f"Does it restore smooth shiny {shade_en} hair?", f"Yes, gives hair a vibrant smooth shiny {shade_en} look."),
        ("Are other Lakme Collage shades available?", "Yes, the full Lakme Collage shade range is available at Ekleel Abha."),
        ("Is performing an allergy test recommended prior to use?", "Yes, performing an allergy patch test 48 hours prior is recommended."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Lakme",
        "ar": {
            "title": ar_title,
            "meta_title": f"{ar_title} | إكليل أبها",
            "meta_description": f"اشتري {ar_title}. صبغة شعر احترافية إسبانية منخفضة الأمونيا لتغطية الشيب 100% باللون {shade_ar}. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. Professional low-ammonia permanent hair dye tube for 100% gray coverage in {shade_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2154():
    return _make_lakme_collage_b86(
        pid=2154, gtin="8429421290012",
        ar_title="صبغة كولاجميكس اشقر فاتح 9/00 من لاكمي  60 مل",
        en_title="Lakme Collage Mix Permanent Hair Color - 9/00 Very Light Blonde, 60ml",
        shade_num="9/00", shade_ar="أشقر فاتح جداً", shade_en="Very Light Blonde",
        tags_ar=["لاكمي_كولاج", "صبغة_لاكمي_9_00", "صبغة_أشقر_فاتح_جدا", "صبغة_إسبانية_احترافية", "إكليل_أبها"],
        tags_en=["lakme_collage", "collage_9_00", "very_light_blonde_lakme", "spanish_hair_dye", "ekleel_abha"]
    )


def create_product_2155():
    return _make_lakme_collage_b86(
        pid=2155, gtin="8429421299480",
        ar_title="صبغة كولاجميكس بنفسجي رمادي اشقر بلاتيني 10/21 من لاكمي  60 مل",
        en_title="Lakme Collage Mix Violet Ash Platinum Blonde Hair Dye 10/21 - 60 ml",
        shade_num="10/21", shade_ar="بنفسجي رمادي أشقر بلاتيني", shade_en="Violet Ash Platinum Blonde",
        tags_ar=["لاكمي_كولاج", "صبغة_لاكمي_10_21", "صبغة_رمادي_بلاتيني", "صبغة_إسبانية_احترافية", "إكليل_أبها"],
        tags_en=["lakme_collage", "collage_10_21", "violet_ash_platinum_lakme", "spanish_hair_dye", "ekleel_abha"]
    )


def create_product_2156():
    return _make_lakme_collage_b86(
        pid=2156, gtin="8429421251716",
        ar_title="صبغة كولاجميكس  بني فاتح رمادي  5/17 من لاكمي  60 مل",
        en_title="Lakmé Collage Mix Light Ash Brown Hair Dye 5/17 - 60 ml",
        shade_num="5/17", shade_ar="بني فاتح رمادي", shade_en="Light Ash Brown",
        tags_ar=["لاكمي_كولاج", "صبغة_لاكمي_5_17", "صبغة_بني_فاتح_رمادي", "صبغة_إسبانية_احترافية", "إكليل_أبها"],
        tags_en=["lakme_collage", "collage_5_17", "light_ash_brown_lakme", "spanish_hair_dye", "ekleel_abha"]
    )


print("Loaded all 5 Batch 86 builders complete")
