import json, os

def _make_jb_dye_shampoo_b85(pid, gtin, ar_title, en_title, shade_ar, shade_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_title}</strong> شامبو الصبغة الطبي السريع والفاخر والأصيل 3 في 1 (شامبو + صبغة + بلسم) من جيه بي (JB / JP Argan Oil Dye Shampoo) المصمم خصيصاً لتغطية الشيب بالكامل باللون {shade_ar} وتنعيم وترميم شعر الرأس واللحية في 8-10 دقائق فقط. تركز هذه الصبغة الشامبوية الأصيلة ({en_title}) على زيت الأرجان المغربي الطبيعي (Natural Argan Oil)، الصبغات الناصعة خالية الأمونيا، والعبوة الكبيرة المزودة بضاغط سعة 400 مل.</p>
<p>يعمل شامبو صبغة جيه بي بالأرغان على صبغ وتغطية 100% من الشعر الأبيض والرمادي بالرأس واللحية، تغذية الفروة والجذور، وإعطاء لمعان حريري ممتد لـ 4 أسابيع، ليترك شعرك ولحيتك بلون {shade_ar} ناصع، ممتلئين بالنضارة والشباب، ومحميين من الجفاف من الغسلة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تغطية كاملة 100% للشيب باللون {shade_ar} في 8-10 دقائق:</strong> صباغة سريعة وسهولة غسيل الشامبو.</li>
  <li><strong>تركيبة 3 في 1 متكاملة (شامبو + صبغة + بلسم):</strong> تنظف وتصبغ وتكثف الشعر بآن واحد.</li>
  <li><strong>ترميم وتنعيم مكثف بزيت الأرجان المغربي الطبيعي:</strong> يمنع جفاف وخشونة الشعر واللحية.</li>
  <li><strong>تركيبة خالية 100% من الأمونيا والروائح الكيميائية:</strong> تناسب الفروة الحساسة والشعر المجهد.</li>
  <li><strong>مناسب لشعر الرأس واللحية للرجال والنساء:</strong> مستحضر شامل ومريح جداً.</li>
  <li><strong>عبوة سعة 400 مل مزودة بضاغط مريح:</strong> تكفي لعدة أشهر من الصباغة المنتظمة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ارتدي القفازات المرفقة واضغطي كمية من شامبو جيه بي على اليدين واخلطيهما جيداً.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي الشامبو على الشعر واللحية الجافين أو الرطبين ودلكي برفق حتى تتكون رغوة صابونية.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركي الصبغة 8-10 دقائق على الشعر ثم اشطفي جيداً بالماء الفاتر (يُستعمل عند الحاجة لتغطية الشيب).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الأرجان المغربي الطبيعي:</strong> يغذي بويصلات الشعر والكيراتين ويمنح مرونة حريرية.</li>
  <li><strong>الصبغات الناصعة خالية الأمونيا:</strong> ترتبط بكيراتين الشعر وتغطي الشيب 100% باللون {shade_ar}.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على شعر الرأس واللحية؛ اختبري التحسس قبل 48 ساعة.</li>
  <li>ارتدي القفازات المخصصة وتجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_title} للتغطية السريعة للشيب في 8 دقائق وتلوين الشعر بالأرغان.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جيه بي (JB / JP Products)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / شامبوهات وصبغات JB 3 في 1 بالأرغان 400ml</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو صبغة 3 في 1 خالي من الأمونيا بزيت الأرجان لتغطية الشيب باللون {shade_ar} (400ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>400 مل بضاغط مريح + قفازات</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر واللحية (خصيصاً الشعر الأبيض، الرمادي، والجاف)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ولحية ناعمين كالحرير، مرطبين، بلون {shade_ar} ناصع وتغطية شيب 100%</td></tr>
  <tr><th>الملمس</th><td>سائل جل صبغة غني ينقلب لرغوة تنظيف وتغطية ناعمة</td></tr>
  <tr><th>العطر</th><td>عطر الأرغان الطبيعي المنعش الخالي من الأمونيا</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت الأرجان المغربي، صبغات ناصعة خالية من الأمونيا، مرطبات مائية</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الإمارات (KSA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>JB Beauty Products</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون (من 18 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد زيت الأرجان المغربي في شامبو صبغة جيه بي 3 في 1 (JB Argan Color Shampoo)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج شامبو صبغة جيه بي 3 في 1 مشكلة الشيب بالرأس واللحية، جفاف الصبغات التقليدية، ورائحة الأمونيا النفاذة.</p>

<h3>لماذا تنجح تركيبة JB 3-in-1 Argan Oil Dye Shampoo {shade_ar}؟</h3>
<p>لأن زيت الأرجان يغذي طبقة الكيراتين الخارجية أثناء تسلل صبغة {shade_ar} الخالية من الأمونيا لتغطية الشيب في 8 دقائق.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق مع ارتداء القفازات المرفقة:</strong> يحمي الأيدي والأظافر من التلون.<br>
2. <strong>الانتظار 8-10 دقائق كاملة:</strong> يضمن تغطية 100% للشيب.<br>
3. <strong>الشطف الجيد بالماء الفاتر:</strong> يمنح لوناً ناصعاً ومظهراً حريرياً.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "شامبوهات 3 في 1 تترك الشعر جافاً ومتقصفاً."<br>
<strong>الحقيقة:</strong> شامبو جيه بي مدعم بالبلسم وزيت الأرجان الطبيعي الذي ينعم الشعر ويحميه من الجفاف كلياً.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>ترتبط جزيئات الصبغة الدقيقة ببروتين كيراتين الشعر بينما تزود الأحماض الدهنية بالأرغان المرونة لـ 4 أسابيع.</p>"""

    faqs_data = [
        (f"ما هو {ar_title}؟", f"هو شامبو صبغة 3 في 1 خالي من الأمونيا بزيت الأرجان لتغطية الشيب بالكامل باللون {shade_ar} في 8 دقائق من جيه بي (400 مل)."),
        (f"ما هي فوائد زيت الأرجان والتركيبة الخالية من الأمونيا (3 في 1)؟", f"تغطي الشيب 100% في 8 دقائق، تمنح لون {shade_ar} غنياً يدوم 4 أسابيع، وترطب وتغسل وتكيف شعر الرأس واللحية."),
        (f"هل يغطي الشيب 100% في 8 دقائق ويرطب بـ زيت الأرجان؟", f"نعم، مثبت سريرياً في تغطية 100% للشيب بالرأس واللحية في 8 دقائق وتوفير نعومة الأرغان."),
        ("ما حجم العبوة ومحتوياتها؟", "تأتي بعبوة ضخمة مزودة بضاغط مريح سعة 400 مل + قفازات مخصصة."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ارتدي القفازات، اضغطي الشامبو، وزعي على شعر ولحية دلكي برغوة، اتركيه 8-10 دقائق واشطفي بالماء الفاتر."),
        ("هل هو خالٍ من الأمونيا والروائح الكيميائية؟", "نعم، 100% خالٍ من الأمونيا ومصمم بعطر الأرغان المنعش."),
        ("أين صُنع شامبو صبغة جيه بي؟", "صُنع بواسطة JB Beauty Products."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات جيه بي لدى إكليل أبها أصلية 100%."),
        (f"ما لون صبغة جيه بي {shade_ar}؟", f"لون {shade_ar} غني وناصع."),
        ("هل يناسب شعر الرأس واللحية وللرجال والنساء؟", "نعم، ممتازة لشعر الرأس واللحية وللرجال والنساء على حد سواء."),
        ("هل عبوة 400 مل بضاغط مريحة وموفرة؟", "نعم، عبوة ضخمة بضاغط تكفي لعدة أشهر من الصباغة المنتظمة."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل جيه بي الماركة الأكثر شهرة في شامبوهات صبغة الأرغان 3 في 1؟", "نعم، JB Argan Color Shampoo الماركة الأكثر تفضيلاً وشهرة في شامبوهات الصبغة بالأرغان."),
        ("كم يدوم ثبات اللون؟", "يدوم حتى 4 أسابيع متواصلة بنفس النضارة."),
        ("هل ينشطف بسهولة دون ترك أثر لزج؟", "نعم، ينشطف بالماء الفاتر بسهولة دون أي لزوجة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع جفاف وخشونة شعر اللحية والرأس؟", "نعم، غني بزيت الأرجان لمنع الجفاف والخشونة وزيادة النعومة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يناسب الشتاء والصيف؟", "نعم، صباغة سريعة وتنعيم مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة لمن يعاني من الشيب؟", "نعم، منتج عناية وصباغة أنيق وعملي جداً كهدية."),
        (f"هل يعيد المظهر الشاب والمشرق للون {shade_ar}؟", f"نعم، يمنح الشعر واللحية مظهراً ناصع اللون {shade_ar} ومفعماً بالشباب."),
        ("هل تتوفر ألوان شامبو صبغة جيه بي الأخرى؟", "نعم، تتوفر عائلة JB Argan Dye Shampoos كاملة لدى إكليل أبها."),
        ("هل يفضل إجراء اختبار تحسس قبل الاستخدام؟", "نعم، يُفضل إجراء اختبار التحسس الموضعي قبل 48 ساعة."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury 3-in-1 (shampoo + color + conditioner) Argan oil hair and beard color shampoo from JB / JP designed to deliver 100% gray hair coverage in {shade_en} while nourishing head hair and beard in just 8-10 minutes. Built upon Natural Moroccan Argan Oil, vibrant ammonia-free pigments, and a generous 400ml pump bottle.</p>
<p>JB 3-in-1 Argan Dye Shampoo completely covers white and gray hair on head and beard, cleanses and conditions hair fibers, and imparts silky gloss lasting 4 weeks, leaving your hair and beard touchably silky soft, naturally {shade_en}, and protected from dryness from first wash.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Gray Coverage in {shade_en} in 8-10 Minutes:</strong> Quick and easy color application just like washing.</li>
  <li><strong>3-in-1 Action (Shampoo + Color + Conditioner):</strong> Colors, washes, and conditions simultaneously.</li>
  <li><strong>Intensive Restoration & Softening with Moroccan Argan Oil:</strong> Prevents post-dye hair and beard dryness.</li>
  <li><strong>100% Ammonia-Free Safe Formula:</strong> Suitable for sensitive scalp and chemical-treated hair.</li>
  <li><strong>Suitable for Head Hair & Beard for Men & Women:</strong> All-in-one convenient format.</li>
  <li><strong>Generous 400ml Value Pump Bottle:</strong> Outstanding size lasting months of continuous coloring.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wear gloves, pump a suitable amount of JB shampoo onto hands, and mix gently.</li>
  <li><strong>Step 2:</strong> Apply over dry or damp head hair and beard, massaging to work into a rich lather.</li>
  <li><strong>Step 3:</strong> Leave dye on hair for 8-10 minutes, then rinse thoroughly with warm water (use as needed for gray coverage).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Moroccan Argan Oil:</strong> Nourishes hair follicles and keratin restoring silky flexibility.</li>
  <li><strong>Ammonia-Free Color Pigments:</strong> Bind to hair protein covering 100% of gray hairs in {shade_en}.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical head hair and beard application; perform an allergy test 48 hours prior.</li>
  <li>Wear protective gloves and avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_title} for 8-minute 100% gray coverage and 3-in-1 Argan oil hair care.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>JB / JP (JB Beauty Products)</td></tr>
  <tr><th>Category</th><td>Hair Care / JB 3-in-1 Argan Color Shampoos 400ml</td></tr>
  <tr><th>Product Type</th><td>100% Ammonia-Free Moroccan Argan Oil 3-in-1 Gray Coverage Color Shampoo ({shade_en} 400ml)</td></tr>
  <tr><th>Volume/Weight</th><td>400 ml Pump Dispenser Bottle + Gloves</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Head Hair & Beard Types (Specifically White, Gray & Dry Hair)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, 100% gray-covered & vibrant {shade_en} hair/beard</td></tr>
  <tr><th>Texture</th><td>Rich smooth easy-to-apply foaming color shampoo gel</td></tr>
  <tr><th>Fragrance</th><td>100% Fresh natural Argan fragrance (ammonia-free)</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Moroccan Argan Oil, Ammonia-Free Color Dyes, Hydrating Emollients</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / UAE</td></tr>
  <tr><th>Manufacturer</th><td>JB Beauty Products</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 18+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Moroccan Argan Lipid Conditioning & 3-in-1 Pigment Binding</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves graying hair on head and beard, post-color dryness, and chemical ammonia odors.</p>

<h3>Why choose JB 3-in-1 Argan Color Shampoo?</h3>
<p>Natural Moroccan Argan Oil and built-in conditioners nourish the hair cuticle while ammonia-free pigments coat 100% of gray hairs in 8 minutes.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is an 8-minute 100% ammonia-free 3-in-1 color shampoo with Moroccan Argan Oil from JB for 100% gray coverage in {shade_en} (400ml)."),
        (f"What are the benefits of Moroccan Argan Oil and the 3-in-1 formula?", f"Covers 100% gray hair in 8 minutes, delivers vibrant {shade_en} color, and cleanses and conditions hair and beard."),
        (f"Does it cover 100% gray hair in {shade_en} in 8 minutes with Argan Oil?", f"Yes, clinically proven to deliver 100% gray coverage in 8 minutes with Argan oil nourishment."),
        ("What volume and contents are included?", "400ml jumbo pump dispenser bottle + protective gloves."),
        ("How do I use it correctly?", "Wear gloves, pump shampoo, apply to hair/beard, lather, wait 8-10 minutes and rinse with warm water."),
        ("Is it 100% ammonia-free?", "Yes, 100% ammonia-free with a fresh natural Argan fragrance."),
        ("Where is JB Shampoo Color manufactured?", "By JB Beauty Products."),
        ("How do I verify authenticity at Ekleel Abha?", "All JB products at Ekleel Abha are 100% original."),
        (f"What color is JB Shampoo Color?", f"Vibrant rich {shade_en}."),
        ("Is it suitable for head hair and beard for men and women?", "Yes, suitable for head hair and beard for both men and women."),
        ("Is the 400ml pump bottle convenient?", "Yes, jumbo pump dispenser bottle ideal for months of regular coloring."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is JB a trusted Argan 3-in-1 color shampoo brand?", "Yes, JB is a premier brand in 3-in-1 Argan oil color shampoos."),
        ("How long does the color stay vibrant?", "Stays vibrant for up to 4 continuous weeks."),
        ("Does it rinse out easily?", "Yes, rinses out smoothly with warm water without sticky residue."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it prevent beard and hair stiffness?", "Yes, enriched with Moroccan Argan oil preventing beard and hair stiffness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it good for all seasons?", "Yes, ideal quick color care for summer and winter routines."),
        ("Is it a nice hair care gift?", "Yes, an elegant practical quick coloring essential."),
        (f"Does it restore smooth youthful {shade_en} hair?", f"Yes, gives hair and beard a healthy smooth youthful {shade_en} look."),
        ("Are other JB color shades available?", "Yes, the full JB color shade range is available at Ekleel Abha."),
        ("Is performing an allergy test recommended prior to use?", "Yes, performing an allergy patch test 48 hours prior is recommended."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "JB",
        "ar": {
            "title": ar_title,
            "meta_title": f"{ar_title} | إكليل أبها",
            "meta_description": f"اشتري {ar_title}. شامبو صبغة 3 في 1 خالي من الأمونيا بزيت الأرجان لتغطية الشيب 100% باللون {shade_ar} 400 مل. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. 100% Ammonia-free Moroccan Argan Oil 3-in-1 8-minute gray coverage color shampoo 400ml. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2147():
    return _make_jb_dye_shampoo_b85(
        pid=2147, gtin="799439315556",
        ar_title="شامبو صبغة شعر بزيت الارجان 3 في 1 من جيه بي (بني غامق). 400مل",
        en_title="JB 3-in-1 Argan Oil Hair Dye Shampoo (Dark Brown) - 400ml",
        shade_ar="بني غامق", shade_en="Dark Brown",
        tags_ar=["جيه_بي", "شامبو_صبغة_جيه_بي_بني_غامق", "صبغة_الأرجان_3في1_بني_غامق", "تغطية_الشيب_جيه_بي", "إكليل_أبها"],
        tags_en=["jb", "jb_dark_brown_shampoo", "argan_3in1_dark_brown_dye", "dark_brown_dye_shampoo", "ekleel_abha"]
    )


def create_product_2148():
    return _make_jb_dye_shampoo_b85(
        pid=2148, gtin="799439315150",
        ar_title="شامبو صبغة شعر بزيت الارجان 3 في 1 من جيه بي (اسود). 400مل",
        en_title="JP 3-in-1 Argan Oil Hair Dye Shampoo (Black) - 400ml",
        shade_ar="أسود", shade_en="Black",
        tags_ar=["جيه_بي", "شامبو_صبغة_جيه_بي_أسود", "صبغة_الأرجان_3في1_أسود", "تغطية_الشيب_جيه_بي", "إكليل_أبها"],
        tags_en=["jb", "jb_black_shampoo", "argan_3in1_black_dye", "black_dye_shampoo", "ekleel_abha"]
    )


def _make_loreal_prodigy_b85(pid, gtin, ar_title, en_title, shade_num, shade_ar, shade_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>{ar_title}</strong> صبغة الشعر الطبية المعتمدة على تقنية الزيوت الدقيقة (Micro-Oil Technology) الفاخرة الأيقونية الخالية 100% من الأمونيا من لوريال باريس بروديجي (L'Oréal Paris Prodigy) المصممة خصيصاً لتمنح شعرك لوناً {shade_ar} ناصعاً، طبيعياً للغاية، ومفعماً بالبريق وملايين الانعكاسات مع تغطية الشيب 100%. تركز هذه الصبغة الفرنسية الأصيلة ({en_title}) على تقنية الزيوت النفيسة المرطبة (Micro-Oil System)، خلوها التام من الأمونيا، وثبات اللون لعدة أسابيع.</p>
<p>تعمل صبغة لوريال بروديجي بدرجة {shade_num} على تزويد ألياف الشعر بجزيئات اللون في عمق الكيراتين دون إتلاف الغمد الخارجي، حفظ طراوة ونعومة الشعر، وإعطاء لون {shade_ar} ساحر، ليترك شعرك ناعماً كالحرير، مرطباً، ناصع اللون، ومحمياً من الجفاف من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تغطية كاملة 100% للشيب باللون {shade_ar} (درجة {shade_num}):</strong> يمنح لوناً طبيعياً غنياً بالانعكاسات.</li>
  <li><strong>تقنية الزيوت الدقيقة 100% خالية من الأمونيا (Micro-Oil):</strong> تنقل جزيئات اللون بأمان لعمق ألياف الشعر.</li>
  <li><strong>ترطيب وتنعيم فائق لألياف الشعر أثناء التلوين:</strong> يمنع الخشونة والجفاف والتلف.</li>
  <li><strong>لون ناصع يدوم لعدة أسابيع دون بهتان:</strong> يعكس الضوء لمنح بريق مذهل.</li>
  <li><strong>جودة لوريال باريس (L'Oréal Paris France) الفرنسية الشهيرة:</strong> الصبغة الفاخرة الأكثر تفضيلاً عالمياً.</li>
  <li><strong>طقم صباغة فاخر مدمج:</strong> يتضمن كريم الصبغة، مستحضر الزيت المظهر، والبلسم المنعم والقفازات.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> اخلطي كريم الصبغة بروديجي {shade_num} مع مستحضر الزيت المظهر في الوعاء المخصص واخلطي جيداً.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي المزيج الكريمي على الشعر الجاف النظيف من الجذور حتى الأطراف باستخدام الفرشاة المخصصة.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركي الصبغة 30 دقيقة، ثم اشطفي بالماء الدافئ وادهني البلسم المرفق لختم النعومة (يُستعمل عند الصبغ).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مجمع الزيوت الدقيقة (Micro-Oil System):</strong> ينشر جزيئات الصبغة لعمق ألياف الشعر دون أمونيا.</li>
  <li><strong>المركبات المطرية والبلسم المرفق:</strong> ينعمان ألياف الكيراتين ويحفظان البريق والنعومة الحريرية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على شعر الرأس؛ اختبري التحسس قبل 48 ساعة من الاستخدام.</li>
  <li>ارتدي القفازات المرفقة وتجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن {ar_title} للتغطية الكاملة للشيب وتلوين الشعر باللون {shade_ar} بآمان الزيوت الدقيقة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لوريال باريس (L'Oréal Paris France)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / صبغات لوريال بروديجي بالزيوت الدقيقة 100ml</td></tr>
  <tr><th>نوع المنتج</th><td>صبغة شعر خالية من الأمونيا بتقنية الزيوت الدقيقة لتغطية الشيب (درجة {shade_num})</td></tr>
  <tr><th>الحجم/الوزن</th><td>أنبوب الصبغة + كريم المظهر + البلسم المرفق + قفازات</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (خصيصاً الجاف، المجهد، والشعر المصاب بالشيب)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم كالحرير، مرطب 24 ساعة، بلون {shade_ar} ناصع وتغطية شيب 100%</td></tr>
  <tr><th>الملمس</th><td>كريم صبغة زيتي ناعم يمتص بسلاسة بألياف الشعر</td></tr>
  <tr><th>العطر</th><td>عطر الزهور والزيوت الفرنسي الزكي الخالي من الأمونيا</td></tr>
  <tr><th>المكونات النشطة</th><td>نظام الزيوت الدقيقة Micro-Oil، صبغات غنية خالية من الأمونيا، بلسم الكيراتين</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا / بلجيكا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>L'Oréal Group France</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون (من 18 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد تقنية الزيوت الدقيقة (Micro-Oil) في صبغة لوريال بروديجي (L'Oréal Prodigy {shade_num})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج صبغة لوريال بروديجي بدرجة {shade_num} مشكلة الشيب، جفاف الصبغات العادية، التلف الناتجة عن الأمونيا، واللون الباهت.</p>

<h3>لماذا تنجح تركيبة L'Oréal Paris Prodigy {shade_num}?</h3>
<p>لأن الزيوت الدقيقة تدفع جزيئات اللون لعمق قلب الشعر دون فتح حراشف الكيراتين بعنف مسببة الجفاف.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على شعر جاف ونظيف بالكامل:</strong> يضمن وصول جزيئات الزيوت الدقيقة.<br>
2. <strong>الانتظار 30 دقيقة كاملة:</strong> يضمن تغطية 100% للشيب باللون {shade_ar}.<br>
3. <strong>استخدام البلسم المرفق بعد الشطف:</strong> يحبس الرطوبة ويغلق حراشف الشعر.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "صبغات الزيوت الخالية من الأمونيا تزول بسرعة مع الغسيل."<br>
<strong>الحقيقة:</strong> صبغة لوريال بروديجي تثبت جزيئات اللون في عمق الشعر لتمنح ثباتاً واستقراراً لعدة أسابيع.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تنقل الزيوت النباتية النفيسة الصبغات عبر الغشاء الكيراتيني مصلحة الفراغات ومحافظة على ليونة الشعر.</p>"""

    faqs_data = [
        (f"ما هي {ar_title}؟", f"هي صبغة شعر خالية من الأمونيا بتقنية الزيوت الدقيقة لتغطية الشيب 100% باللون {shade_ar} (درجة {shade_num}) من لوريال باريس."),
        (f"ما هي فوائد تقنية الزيوت الدقيقة (Micro-Oil) في صبغة بروديجي {shade_num}؟", f"تغطي الشيب 100%، تنقل جزيئات اللون لألياف الشعر دون أمونيا، وتمنح لون {shade_ar} ناصعاً ومشرقاً."),
        (f"هل تغطي الشيب 100% وتمنح لون {shade_ar} بالزيوت بدون أمونيا؟", f"نعم، مثبتة سريرياً في تغطية 100% للشيب وتوفير لون {shade_ar} غني وبراق بفضل الزيوت الدقيقة."),
        ("ما هي محتويات الطقم؟", "يتضمن أنبوب كريم الصبغة + مستحضر الزيت المظهر + البلسم المنعم + القفازات المخصصة."),
        ("كيف تُستخدم بالشكل الصحيح؟", "اخلطي كريم الصبغة والمظهر الزيتي، وزعي على الشعر الجاف، اتركي 30 دقيقة، اشطفي بالماء واستخدمي البلسم المرفق."),
        ("هل هي خالية من الأمونيا والروائح النفاذة؟", "نعم، 100% خالية من الأمونيا ومصممة بعطر الزيوت والزهور الفرنسي الزكي."),
        ("أين صُنت صبغة لوريال بروديجي؟", "صُنت في فرنسا بواسطة L'Oréal Group."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لوريال لدى إكليل أبها أصلية 100%."),
        (f"ما لون صبغة لوريال بروديجي {shade_num}؟", f"لون {shade_ar} غني وناصع الطبيعية (درجة {shade_num})."),
        ("هل تناسب جميع أنواع الشعر للشيب؟", "نعم، ممتازة لجميع أنواع الشعر والتغطية الكاملة للشيب المزعج."),
        ("هل الطقم مريح وكافٍ للشعر؟", "نعم، طقم مدمج فاخر أنيق يكفي لصبغة كاملة لشعر متوسط الطول."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل لوريال باريس بروديجي صبغة الزيوت الفاخرة رقم 1 عالمياً؟", "نعم، L'Oréal Prodigy صبغة الزيوت الدقيقة رقم 1 الأكثر تفضيلاً وشهرة عالمياً."),
        ("كم يدوم ثبات اللون؟", "يدوم لعدة أسابيع متواصلة بنفس البريق والزهاء."),
        ("هل ينشطف بسهولة دون ترك لزوجة؟", "نعم، ينشطف بالماء الدافئ بسهولة دون أي لزوجة ثقيلة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع تقصف وخشونة الشعر المصبوغ؟", "نعم، بتقنية الزيوت الدقيقة تمنع الخشونة والتقصف وزيادة النعومة الحريرية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يناسب الشتاء والصيف؟", "نعم، صباغة وتغذية بالزيوت مثالية لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة للعناية بالشعر؟", "نعم، منتج صباغة وتنعيم فاخر وأساسي لكل روتين جمال."),
        (f"هل يعيد المظهر المشرق الناعم للون {shade_ar}؟", f"نعم، يمنح الشعر مظهراً ناصع اللون {shade_ar} ومفعماً باللمعان الحريري."),
        ("هل تتوفر درجات صبغة لوريال بروديجي الأخرى؟", "نعم، تتوفر عائلة L'Oréal Prodigy كاملة لدى إكليل أبها."),
        ("هل يفضل إجراء اختبار تحسس قبل الاستخدام؟", "نعم، يُنصح دائماً باختبار التحسس الموضعي قبل 48 ساعة."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury ammonia-free Micro-Oil hair color from L'Oréal Paris Prodigy designed to deliver 100% gray coverage, vibrant natural {shade_en} color (Shade {shade_num}), and million-fold color reflections without damaging hair cuticles. Built upon the revolutionary Micro-Oil Technology System, 100% ammonia-free formulation, and long-lasting color lock.</p>
<p>L'Oréal Paris Prodigy Hair Color Shade {shade_num} diffuses color pigments deep into the hair fiber shaft without harsh ammonia, preserves hair smoothness and moisture, and imparts brilliant {shade_en} luster, leaving your hair touchably silky soft, hydrated, brilliantly colored, and protected from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Gray Coverage with Natural {shade_en} Color (Shade {shade_num}):</strong> Imparts multi-dimensional reflections.</li>
  <li><strong>100% Ammonia-Free Micro-Oil Technology System:</strong> Transports color pigments safely into hair fibers.</li>
  <li><strong>Intensive Hair Fiber Softening & Hydration:</strong> Prevents post-dye dryness, damage, and roughness.</li>
  <li><strong>Long-Lasting Vibrancy for Weeks:</strong> Reflects light delivering extraordinary glossy shine.</li>
  <li><strong>Famous French L'Oréal Paris Quality:</strong> World's #1 luxury salon-grade home hair color line.</li>
  <li><strong>Complete Luxury Coloring Kit Included:</strong> Contains color cream, oil developer, conditioner, and gloves.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Mix Prodigy color cream Shade {shade_num} with oil developer in the provided bottle and shake well.</li>
  <li><strong>Step 2:</strong> Apply the creamy mixture onto clean dry hair from roots to tips using the applicator nozzle or brush.</li>
  <li><strong>Step 3:</strong> Leave dye on hair for 30 minutes, then rinse thoroughly with warm water and apply included conditioner.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Micro-Oil System:</strong> Infuses color pigments deep into hair fibers preserving natural hair moisture.</li>
  <li><strong>Conditioning Agents & Included Conditioner:</strong> Soften keratin fibers locking in silky smoothness and shine.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical head hair application; perform an allergy test 48 hours prior to use.</li>
  <li>Wear included gloves and avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_title} for 100% gray coverage, {shade_en} hair coloring, and Micro-Oil hair protection.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>L'Oréal Paris (France)</td></tr>
  <tr><th>Category</th><td>Hair Care / L'Oréal Prodigy Micro-Oil Hair Dyes 100ml</td></tr>
  <tr><th>Product Type</th><td>100% Ammonia-Free Micro-Oil Technology 100% Gray Coverage Hair Dye (Shade {shade_num})</td></tr>
  <tr><th>Volume/Weight</th><td>Color Cream + Oil Developer + Conditioner + Gloves</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Specifically Dry, Stressed & Gray-Plagued Hair)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, 100% gray-covered & multi-dimensional {shade_en} hair</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-drip oil-in-cream conditioning dye</td></tr>
  <tr><th>Fragrance</th><td>100% Luxurious French floral fragrance (ammonia-free)</td></tr>
  <tr><th>Active Ingredients</th><td>Micro-Oil System, Ammonia-Free Color Pigments, Keratin Conditioner</td></tr>
  <tr><th>Country of Origin</th><td>France / Belgium</td></tr>
  <tr><th>Manufacturer</th><td>L'Oréal Group France</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 18+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Micro-Oil Pigment Diffusion & Ammonia-Free Hair Protection</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves gray hair coverage, dull hair color, ammonia chemical damage, and post-dye dryness.</p>

<h3>Why choose L'Oréal Paris Prodigy Shade {shade_num}?</h3>
<p>Micro-Oil technology diffuses color pigments deep into hair fibers without forcing open cuticles with harsh ammonia.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a luxury ammonia-free Micro-Oil hair dye from L'Oréal Paris for 100% gray coverage in {shade_en} (Shade {shade_num})."),
        (f"What are the benefits of Micro-Oil Technology in Prodigy {shade_num}?", f"Covers 100% gray hair, diffuses color pigments deep into hair fibers without ammonia, and delivers vibrant {shade_en} gloss."),
        (f"Does it cover 100% gray hair in {shade_en} without ammonia?", f"Yes, clinically proven to deliver 100% gray coverage in {shade_en} with Micro-Oil technology protection."),
        ("What items are included in this kit?", "Color cream tube + oil developer bottle + conditioning cream + gloves."),
        ("How do I use it correctly?", "Mix color cream with oil developer, apply to dry hair, wait 30 minutes, rinse and apply included conditioner."),
        ("Is it 100% ammonia-free?", "Yes, 100% ammonia-free with a luxury French floral fragrance."),
        ("Where is L'Oréal Prodigy manufactured?", "In France by L'Oréal Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All L'Oréal products at Ekleel Abha are 100% original."),
        (f"What color shade is Prodigy {shade_num}?", f"Natural multi-dimensional {shade_en} (Shade {shade_num})."),
        ("Is it suitable for all hair types and gray coverage?", "Yes, excellent for all hair types and complete gray hair coverage."),
        ("Is the kit convenient for full head dyeing?", "Yes, sleek luxury kit sufficient for full head application on medium hair."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is L'Oréal Paris Prodigy a #1 global micro-oil hair dye brand?", "Yes, L'Oréal Prodigy is the world's most famous #1 micro-oil ammonia-free hair color line."),
        ("How long does the color stay vibrant?", "Stays vibrant for continuous weeks."),
        ("Does it rinse out smoothly?", "Yes, rinses out smoothly with warm water and conditioner."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it prevent post-dye hair roughness?", "Yes, Micro-Oil technology preserves natural hair moisture preventing post-dye roughness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it good for all seasons?", "Yes, ideal hair coloring and oil care for summer and winter routines."),
        ("Is it a nice hair care gift?", "Yes, a premier luxury hair dye for daily beauty routines."),
        (f"Does it restore smooth shiny {shade_en} hair?", f"Yes, gives hair a vibrant smooth shiny {shade_en} look."),
        ("Are other L'Oréal Prodigy shades available?", "Yes, the full L'Oréal Prodigy shade range is available at Ekleel Abha."),
        ("Is performing an allergy test recommended prior to use?", "Yes, performing an allergy patch test 48 hours prior is recommended."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "L'Oreal Paris",
        "ar": {
            "title": ar_title,
            "meta_title": f"{ar_title} | إكليل أبها",
            "meta_description": f"اشتري {ar_title}. صبغة شعر فرنسية بالزيوت الدقيقة خالية من الأمونيا لتغطية الشيب 100% باللون {shade_ar}. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. 100% Ammonia-free Micro-Oil French hair dye for 100% gray coverage in {shade_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2149():
    return _make_loreal_prodigy_b85(
        pid=2149, gtin="3600522599432",
        ar_title="صبغة شعر بروديجي  لون اشقر فاتح8.0، من لوريال باريس",
        en_title="L'Oreal Paris Prodigy Hair Color - 8.0 Light Blonde",
        shade_num="8.0", shade_ar="أشقر فاتح", shade_en="Light Blonde",
        tags_ar=["لوريال_بروديجي", "صبغة_بروديجي_8.0", "صبغة_أشقر_فاتح_لوريال", "صبغة_الزيوت_الدقيقة", "إكليل_أبها"],
        tags_en=["loreal_prodigy", "prodigy_8.0", "light_blonde_prodigy", "micro_oil_dye", "ekleel_abha"]
    )


def create_product_2150():
    return _make_loreal_prodigy_b85(
        pid=2150, gtin="3600522599340",
        ar_title="صبغة شعر بروديجي  لون بني (4.0) من لوريال باريس",
        en_title="L'Oréal Paris Prodigy Hair Color - Brown (4.0)",
        shade_num="4.0", shade_ar="بني", shade_en="Brown",
        tags_ar=["لوريال_بروديجي", "صبغة_بروديجي_4.0", "صبغة_بني_لوريال", "صبغة_الزيوت_الدقيقة", "إكليل_أبها"],
        tags_en=["loreal_prodigy", "prodigy_4.0", "brown_prodigy", "micro_oil_dye", "ekleel_abha"]
    )


def create_product_2151():
    return _make_loreal_prodigy_b85(
        pid=2151, gtin="3600522599364",
        ar_title="صبغة شعر بروديجي  لون بني غامق( 3.0)، من لوريال باريس",
        en_title="L'Oréal Paris Prodigy Hair Color - Dark Brown (3.0)",
        shade_num="3.0", shade_ar="بني غامق", shade_en="Dark Brown",
        tags_ar=["لوريال_بروديجي", "صبغة_بروديجي_3.0", "صبغة_بني_غامق_لوريال", "صبغة_الزيوت_الدقيقة", "إكليل_أبها"],
        tags_en=["loreal_prodigy", "prodigy_3.0", "dark_brown_prodigy", "micro_oil_dye", "ekleel_abha"]
    )


print("Loaded all 5 Batch 85 builders complete")
