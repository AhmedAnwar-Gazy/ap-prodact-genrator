import json, os

def create_product_2045():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>ماسك شعر بالأرغان من ناتشر ريبورت 200مل (Nature Report Argan Hair Mask 200ml)</strong> قناع الشعر العلاجي المرطب والمغذي الفاخر الأصيل من ناتشر ريبورت الكورية المصمم خصيصاً لترميم، تغذية، وتنعيم الشعر التالف، الجاف، والمجهد من الصبغات والحرارة. يرتكز هذا الماسك الأصيل (Nature Report Argan Mask 200ml) على زيت الأرغان المغربي النقي الأصيل (Pure Moroccan Argan Oil)، بروتينات السيريسين، ومركبات التغذية العميقة للكيراتين.</p>
<p>يعمل ماسك ناتشر ريبورت بالأرغان على اختراق ألياف الشعر الجافة عمقاً، ترميم التلف والتقصف بالروابط البروتينية، وإعادة الحيوية واللمعان الساحر للخصيلات، ليترك شعرك ناعماً كالحرير، سهلاً في التمشيط، ومفعماً بالنعومة والبريق من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترميم وتغذية مكثفة بزيت الأرغان المغربي النقي:</strong> يصلح الشعر التالف والمجهد من الصبغة والحرارة.</li>
  <li><strong>تنعيم فائق وتسهيل فك تشابك الشعر:</strong> يمنح الخصلات ملمساً حريرياً وانسيابياً رائعاً.</li>
  <li><strong>السيطرة على التقصف والهيشان:</strong> يغلف ساق الشعر ويمنع تسرب الرطوبة الجوية المسببة للهيشان.</li>
  <li><strong>إعادة اللمعان الطبيعي والتحسين الكلي لمرونة الشعر:</strong> يمنح الشعر مظهرًا صحياً متألقاً.</li>
  <li><strong>تركيبة كورية خفيفة مغذية لا تثقل الشعر:</strong> مناسبة للاستخدام الأسبوعي لجميع أنواع الشعر.</li>
  <li><strong>عبوة سعة 200 مل:</strong> حجم ممتاز لروتين حمام الزيت والترميم الأسبوعي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> اغسلي الشعر بالشامبو واشطفيه جيداً بالماء الدافئ ثم عصري الماء الزائد.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي كمية سخية من ماسك ناتشر ريبورت على طول الشعر والأطراف وتجنبي الفروة المباشرة.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركيه لمدة 5-10 دقائق ثم اشطفي جيداً بالماء الدافئ (يُستعمل 1-2 مرة أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الأرغان المغربي النقي (Argania Spinosa Kernel Oil):</strong> غني بالأحماض الدهنية وفيتامين E لترميم الكيراتين.</li>
  <li><strong>البروتينات الطبيعية والمركبات المنعمة:</strong> تغلف ساق الشعر وتمنع التقصف والتشابك.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على الشعر فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من الشعر التالف والجاف ويبحث عن ماسك ناتشر ريبورت بالأرغان 200 مل للتغذية والترميم.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ناتشر ريبورت (Nature Report)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / أقنعة وماسكات ترميم الشعر بالأرغان 200ml</td></tr>
  <tr><th>نوع المنتج</th><td>ماسك علاجي مغذي ومجدد للشعر التالف والجاف بزيت الأرغان (200ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>200 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (خصيصاً التالف، المجهد بالحرارة والصبغة، والجاف)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم كالحرير، مرمم من التقصف، مرطب ومفعم باللمعان الطبيعي</td></tr>
  <tr><th>الملمس</th><td>كريم دسم غني ينفذ بنعومة للشعر</td></tr>
  <tr><th>العطر</th><td>عطر زيت الأرغان الزكي الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت الأرغان المغربي النقي، بروتينات مجددة، فيتامين E</td></tr>
  <tr><th>بلد المنشأ</th><td>كوريا الجنوبية (South Korea)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Nature Report Korea</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت الأرغان الكوري في ماسك ناتشر ريبورت (Nature Report Argan Mask)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج ماسك ناتشر ريبورت مشكلة تقصف أطراف الشعر، خشونة الألياف الناتجة عن الصبغات والحرارة، والتطاطؤ والجفاف.</p>

<h3>لماذا تنجح تركيبة Nature Report Argan Hair Mask؟</h3>
<p>لأن الأحماض الدهنية غير المشبعة في زيت الأرغان تخترق قشرة الكيراتين وتصلح الروابط المكسورة مانعة التقصف.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على شعر مبلل بعد الشامبو:</strong> يزيد تغلغل المواد المغذية.<br>
2. <strong>التركيز على الأطراف المتضررة:</strong> يمنع تكسر أطراف الشعر المستمر.<br>
3. <strong>الاستخدام 1-2 مرة أسبوعياً:</strong> يحافظ على النعومة والترطيب الدائم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "ماسك الأرغان يترك طبقة ثقيلة تجعل الشعر دهنياً."<br>
<strong>الحقيقة:</strong> تركيبة ناتشر ريبورت الكورية مصممة بامتصاص سريع تغذي الخصلات وتنعشها دون تزييت.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تلتصق جزيئات فيتامين E والأحماض الدهنية بطبقة الـ Cuticle الخارجية وتغلف ساق الشعر بحماية حرارية وهيدروليبيدية.</p>"""

    faqs = [
        ("ما هو ماسك شعر بالأرغان من ناتشر ريبورت 200مل؟", "هو ماسك كوري علاجي فاخر بزيت الأرغان المغربي لتغذية وترميم وتنعيم الشعر التالف والجاف (200 مل)."),
        ("ما هي فوائد زيت الأرغان المغربي والبروتينات للشعر؟", "يرممان الشعر التالف من الحرارة والصبغات، يقويان ألياف الكيراتين، ويمنحان نعومة ولمعاناً حريرياً."),
        ("هل يرمم التقصف ويمنح نعومة من الاستخدام الأول؟", "نعم، مثبت سريرياً في ترميم التلف وتنعيم الخصلات ومنع التقصف من الاستخدام الأول."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة بسعة 200 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي على شعر مبلل بعد الشامبو، اتركيه 5-10 دقائق واشطفي بالماء الدافئ 1-2 مرة أسبوعياً."),
        ("هل هو آمن للشعر المصبوغ والمعالج بالبروتين؟", "نعم، آمن وممتاز للشعر المصبوغ والمعالج كيميائياً."),
        ("أين صُنع ماسك ناتشر ريبورت؟", "صُنع في كوريا الجنوبية بواسطة Nature Report Korea."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات ناتشر ريبورت لدى إكليل أبها أصلية 100%."),
        ("ما رائحة ماسك ناتشر ريبورت بالأرغان؟", "عطر زيت الأرغان الزكي الفاخر المنعش."),
        ("هل يسهل فك تشابك الشعر؟", "نعم، يجعل التمشيط وفك التشابك سهلاً وسلساً للغاية."),
        ("هل عبوة 200 مل تكفي لفترة جيدة؟", "نعم، تكفي لعدة أشهر من الاستخدام الأسبوعي المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الحرارة المباشرة."),
        ("هل ناتشر ريبورت علامة كورية موثوقة؟", "نعم، Nature Report علامة كورية شهيرة وموثوقة في مستحضرات التجميل والعناية."),
        ("كم مرة أسبوعياً؟", "1 إلى 2 مرة أسبوعياً."),
        ("هل يترك أثراً دهنياً ثقيلاً؟", "ينفذ بنعومة وينشطف بالماء دون ترك ثقل أو دهنية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يسيطر على هيشان الشعر؟", "نعم، يسيطر على الهيشان والتطاير الناتجة عن الجفاف."),
        ("هل يمنح لمعاناً طبيعياً براقاً؟", "نعم، يكسو الشعر بلمعان وبريق صحي ساحر."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يفضل تغطية الشعر بقبعة دافئة أثناء الاستخدام؟", "نعم، تغطية الشعر بقبعة دافئة تزيل التلف وتضاعف امتصاص الماسك."),
        ("هل يحمي الشعر من حرارة السشوار والجو؟", "نعم، يشكل غلافاً حمائياً يقي الخصلات من حرارة السشوار."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية بالشعر؟", "نعم، منتج كوري فاخر وأساسي لكل روتين عناية."),
        ("هل يعيد المرونة والحيوية للشعر المجهد؟", "نعم، يعيد الحيوية والجمال الطبيعي للشعر التالف."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Nature Report Argan Hair Mask 200ml</strong> is an authentic luxury Korean repairing and hydrating hair mask from Nature Report engineered to restore, nourish, and smooth hair damaged, dry, and stressed by color processing and heat styling. Built upon Pure Moroccan Argan Oil, sericin proteins, and deep keratin nourishment.</p>
<p>Nature Report Argan Hair Mask deeply penetrates dry hair fibers, repairs structural split-end damage with protein bonds, and restores vibrant luster and softness, leaving your hair touchably silky smooth, easy to comb, and radiant from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intensive Repair with Pure Moroccan Argan Oil:</strong> Restores hair damaged by heat and dye treatments.</li>
  <li><strong>Ultra-Softening & Effortless Detangling:</strong> Imparts silky smooth flow to hair strands.</li>
  <li><strong>Frizz & Split-End Control:</strong> Seals the hair shaft preventing moisture-induced flyaways.</li>
  <li><strong>Natural Shine Restoration & Elasticity Boost:</strong> Delivers a healthy vibrant hair finish.</li>
  <li><strong>Lightweight Nourishing Korean Formula:</strong> Suitable for weekly use on all hair types.</li>
  <li><strong>Generous 200ml Tub Container:</strong> Excellent format for weekly deep treatment routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Shampoo hair, rinse thoroughly with warm water, and squeeze out excess moisture.</li>
  <li><strong>Step 2:</strong> Apply a generous amount of Nature Report Mask through hair lengths and ends avoiding scalp.</li>
  <li><strong>Step 3:</strong> Leave on for 5-10 minutes then rinse thoroughly with warm water (use 1-2 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Moroccan Argan Oil (Argania Spinosa):</strong> Rich in essential fatty acids and Vitamin E repairing keratin.</li>
  <li><strong>Natural Proteins & Conditioning Agents:</strong> Coat the hair shaft preventing tangles and breakage.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hair application only.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from dry damaged hair seeking Nature Report Argan Hair Mask 200ml for repair and nutrition.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Nature Report</td></tr>
  <tr><th>Category</th><td>Hair Care / Nature Report Argan Repairing Hair Masks 200ml</td></tr>
  <tr><th>Product Type</th><td>Korean Argan Oil Repairing & Nourishing Hair Mask (200ml)</td></tr>
  <tr><th>Volume/Weight</th><td>200 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Specifically Damaged, Heat-Stressed & Dry Hair)</td></tr>
  <tr><th>Finish</th><td>Silky soft, repaired, deeply hydrated & radiant hair</td></tr>
  <tr><th>Texture</th><td>Rich smooth dense cream penetrating easily</td></tr>
  <tr><th>Fragrance</th><td>Luxurious pleasant natural Argan oil scent</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Moroccan Argan Oil, Restorative Proteins, Vitamin E</td></tr>
  <tr><th>Country of Origin</th><td>South Korea</td></tr>
  <tr><th>Manufacturer</th><td>Nature Report Korea</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Korean Argan Oil Cuticle Impregnation & Keratin Restoration</h2>

<h3>What problem does this solve?</h3>
<p>Nature Report Argan Hair Mask resolves split ends, fiber roughness from chemical dye treatments, and heat damage.</p>

<h3>Why choose Nature Report Argan Hair Mask?</h3>
<p>Unsaturated fatty acids in Argan oil penetrate keratin cuticles repairing broken disulfide links and sealing split ends.</p>"""

    en_faqs = [
        ("What is Nature Report Argan Hair Mask 200ml?", "It is a luxury Korean repairing hair mask with Moroccan Argan oil for damaged and dry hair (200ml)."),
        ("What are the benefits of Moroccan Argan oil and proteins for hair?", "They repair heat and dye damage, reinforce keratin fibers, and deliver silky softness and shine."),
        ("Does it repair split ends and soften hair from first use?", "Yes, clinically proven to repair damage and soften strands from the first application."),
        ("What volume is contained in this tub?", "200ml tub."),
        ("How do I use it correctly?", "Apply to damp hair post-shampoo, leave for 5-10 minutes, and rinse with warm water 1-2 times weekly."),
        ("Is it safe for color-treated and chemically processed hair?", "Yes, safe and excellent for color-treated and chemically processed hair."),
        ("Where is Nature Report Hair Mask manufactured?", "In South Korea by Nature Report Korea."),
        ("How do I verify authenticity at Ekleel Abha?", "All Nature Report products at Ekleel Abha are 100% original."),
        ("What scent does Nature Report Argan Mask have?", "Luxurious pleasant natural Argan oil fragrance."),
        ("Does it make detangling hair easy?", "Yes, makes combing and detangling smooth and effortless."),
        ("Does the 200ml tub last long?", "Yes, lasts months of regular weekly treatment use."),
        ("How should I store it?", "In a cool, dry place away from direct heat."),
        ("Is Nature Report a trusted Korean brand?", "Yes, Nature Report is a famous trusted brand in Korean cosmetics."),
        ("How many times weekly?", "1 to 2 times weekly."),
        ("Does it leave a heavy greasy residue?", "Rinses off smoothly with water without leaving heavy grease."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it control hair frizz?", "Yes, controls frizz and flyaways caused by dryness."),
        ("Does it deliver natural luminous shine?", "Yes, coats hair in healthy radiant shine."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is wrapping hair in a warm towel recommended during use?", "Yes, wrapping hair in a warm towel enhances mask penetration."),
        ("Does it shield hair from blow dryer heat?", "Yes, forms a protective film guarding hair against heat styling."),
        ("Is it a nice hair care gift?", "Yes, a premier Korean hair care treatment gift."),
        ("Does it restore elasticity and life to stressed hair?", "Yes, restores vitality and strength to damaged hair."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2045",
        "sku": "EK-2045",
        "gtin": "16274",
        "brand": "Nature Report",
        "ar": {
            "title": "ماسك شعر بالأرغان من ناتشر ريبورت 200مل",
            "meta_title": "ماسك شعر ناتشر ريبورت بالأرغان 200مل | إكليل أبها",
            "meta_description": "اشتري ماسك شعر بالأرغان من ناتشر ريبورت (200 مل). قناع كوري علاجي بزيت الأرغان المغربي لترميم وتنظيف وتغذية الشعر التالف والجاف. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["ناتشر_ريبورت", "ماسك_الأرغان_الكوري", "ترميم_الشعر", "ماسك_الشعر_التالف", "إكليل_أبها"]
        },
        "en": {
            "title": "Nature Report Argan Hair Mask 200ml",
            "meta_title": "Nature Report Argan Hair Mask 200ml | Ekleel Abha",
            "meta_description": "Buy original Nature Report Argan Hair Mask (200ml). Korean Argan oil repairing and nourishing hair mask. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["nature_report", "argan_hair_mask", "korean_hair_mask", "repairing_hair_mask", "ekleel_abha"]
        }
    }


def _make_bench_cologne_b66(pid, gtin, ar_name, en_name, scent_ar, scent_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> كولونيا ومعطر الجسم اليومي الفواح الفاخر الأصيل من بنش (Bench / Pinch) الفلبينية الشهيرة المصمم لمنح بشرتك وجسمك انتعاشاً يومياً مبهجاً وعطراً ساحراً يدوم طوال اليوم. يرتكز هذا المعطر الأصيل ({en_name}) على الزيوت العطرية الخفيفة المهدئة بنفحات {scent_ar} المنعشة، والمركبات المرطبة لبشرة الجسم.</p>
<p>يعمل معطر بنش دايلي سينت على تعطير الجسم وتنعيم البشرة، السيطرة على روائح التعرق اليومية، وتزويدك بهالة عاطرة مفعمة بالحيوية والشباب، ليترك بشرتك ناعمة، مرطبة، ومعطرة بالنظافة والانتعاش من الرشة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عطر فواح ومبهج يومياً بنفحات {scent_ar}:</strong> يمنح الانتعاش والحيوية طوال اليوم.</li>
  <li><strong>تركيبة خفيفة آمنة على البشرة والملابس:</strong> تنعش دون تسبيب أي تحسس أو بقع.</li>
  <li><strong>السيطرة على روائح التعرق والانتعاش اليومي:</strong> ممتاز للاستخدام بعد الاستحمام والرياضة.</li>
  <li><strong>مناسب للاستخدام اليومي للشباب، الفتيات والأطفال:</strong> عطر النظافة العائلي المثالي.</li>
  <li><strong>جودة Bench العالمية الشهيرة في الكولونيا:</strong> العلامة الأولى في كولونيا Daily Scent.</li>
  <li><strong>زجاجة مدمجة سعة 125 مل:</strong> حجم ممتاز للحقيبة والتنقل والاستخدام اليومي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> رشّي كولونيا بنش على بشرة الجسم والرقبة والملابس بعد الاستحمام أو في أي وقت خلال اليوم.</li>
  <li><strong>الخطوة الثانية:</strong> دعي المعطر يجف طبيعياً واستمتعي بهالة العطور المنعشة (يُستعمل عدة مرات يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الزيوت العطرية الفواحة بنفحات {scent_ar}:</strong> تمنح ثباتاً عطرياً ناعماً ومبهجاً.</li>
  <li><strong>المكونات المائية والمنعشة:</strong> تلطف بشرة الجسم وتمنع الجفاف والتهيج.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على الجسم والملابس.</li>
  <li>تجنبي الرش المباشر داخل العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن الحرارة والشمس.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} للانتعاش العطري والنظافة اليومية.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بنش / بنتش (Bench / Pinch Daily Scent)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / كولونيا ومعطرات بنش دايلي سينت 125ml</td></tr>
  <tr><th>نوع المنتج</th><td>كولونيا ومعطر جسم يومي بنفحات {scent_ar} (125ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>125 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (النساء، الرجال، والشباب)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم معطر بالانتعاش، ناعم وناصع النظافة بنفحات {scent_ar}</td></tr>
  <tr><th>الملمس</th><td>سائل عطر شفاف رغوي خفيف تنفذ سرعة</td></tr>
  <tr><th>العطر</th><td>عطر {scent_ar} المبهج المنعش لـ Daily Scent</td></tr>
  <tr><th>المكونات النشطة</th><td>زيوت عطرية مهدئة، محاليل منشطة، مرطبات جلدية</td></tr>
  <tr><th>بلد المنشأ</th><td>الفلبين (Philippines)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Suyen Corporation Philippines (Bench)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 10 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد الكولونيا اليومية بنفحات {scent_ar} من بنش (Bench Daily Scent)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج كولونيا بنش مشكلة الروائح اليومية وسرعة تلاشي المعطرات والتسبب في بقع الملابس.</p>

<h3>لماذا تنجح تركيبة Bench Daily Scent؟</h3>
<p>لأن تركيبة الكولونيا الخفيفة المائية تمتزج بمركبات مهدئة تنتشر بسلاسة وتمنح عبقاً ناعماً ممتداً.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الرش فوراً بعد الاستحمام على بشرة رطبة:</strong> يضاعف ثبات العطر على الجلد.<br>
2. <strong>الرش على نقاط النبض (المعصمين والرقبة):</strong> ينشر العطر مع حرارة الجسم الطبيعية.<br>
3. <strong>الاحتفاظ بعبوة 125 مل بالحقيبة:</strong> للتحديث العطري السريع أثناء العمل أو المدرسة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الكولونيا المعطرة تسبب جفاف واسمرار الجلد."<br>
<strong>الحقيقة:</strong> كولونيا بنش مصممة بمكونات مهدئة خفيفة آمنة على الجلد ولا تسبب الاسمرار.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتطاير الجزيئات العطرية بخفة مع حرارة البشرة محققة انبعاثاً عطرياً ناعماً ومتجدداً.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو كولونيا ومعطر جسم يومي فواح من بنش بنفحات {scent_ar} بحجم 125 مل."),
        (f"ما هي فوائد كولونيا بنش دايلي سينت بنفحات {scent_ar}؟", f"تمنح الجسد انتعاشاً وعطراً مبهجاً، تسيطر على روائح التعرق، وتلطف البشرة."),
        ("هل يمنح انتعاشاً وعطراً يدوم طوال اليوم؟", "نعم، مثبت شعبياً وسريرياً في توفير انتعاش عطري مبهج ومستمر."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة سعة 125 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "رشّي على بشرة الجسم والرقبة والملابس بعد الاستحمام ودعيه يجف طبيعياً."),
        ("هل هو آمن على الجلد والملابس ولا يسبب بقعاً؟", "نعم، 100% آمن على الجلد والملابس ولا يترك أي بقع."),
        ("أين صُنعت كولونيا بنش؟", "صُنع في الفلبين بواسطة Suyen Corporation (Bench)."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات بنش لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {scent_ar} المبهج المنعش."),
        ("هل يناسب الشباب والفتيات والأطفال؟", "نعم، عطر النظافة العائلي المثالي للجميع."),
        ("هل عبوة 125 مل مناسبة للحقيبة؟", "نعم، زجاجة أنيقة مدمجة مثالية لحقيبة اليد والسفر والتنقل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الحرارة للشمس."),
        ("هل بنش العلامة الأولى في كولونيا Daily Scent؟", "نعم، Bench العلامة رقم 1 الأكثر شهرة عالمياً في كولونيا Daily Scent."),
        ("كم مرة يومياً؟", "عدة مرات يومياً وعند الحاجة للانتعاش العطري."),
        ("هل يناسب الاستخدام بعد الاستحمام والرياضة؟", "نعم، ممتاز للانتعاش والنظافة بعد السباحة والرياضة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في تنشيط اليوم بالروائح المبهجة؟", "نعم، يمنح طاقة وانتعاشاً عاطراً مبهجاً."),
        ("هل يترك ملمساً ناعماً؟", "نعم، يترك البشرة مرطبة ومعطرة بلمسة ناعمة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للجميع حسب النكهة العطرية المفضلة."),
        ("هل يناسب جميع فصول السنة؟", "نعم، ممتاز للصيف والشتاء والدوام اليومي."),
        ("هل يصلح هدية ممتازة ولطيفة؟", "نعم، هدية أنيقة ومفيدة جداً للطلاب والشباب."),
        ("هل يجف سريعاً على الجلد؟", "نعم، يجف في ثوانٍ معدودة محققاً العبق المطلوب."),
        ("هل تتوفر نكهات أخرى من كولونيا بنش؟", "نعم، تتوفر عائلة Bench Daily Scent خيارات متعددة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic luxury refreshing daily cologne body mist from Bench (Pinch) Philippines designed to infuse your body and skin with uplifting daily freshness and a delightful scent all day. Built upon mild soothing aromatic oils with refreshing {scent_en} notes and skin-moisturizing compounds.</p>
<p>Bench Daily Scent Cologne perfumes body skin, tames daily sweat odors, and surrounds you with a youthful vibrant aura, leaving your skin soft, hydrated, and fragranced with clean freshness from the very first spray.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Uplifting Daily Fresh Fragrance with {scent_en}:</strong> Delivers continuous vibrancy all day.</li>
  <li><strong>Lightweight Formula Safe for Skin & Clothing:</strong> Refreshes without irritation or staining clothes.</li>
  <li><strong>Sweat Odor Control & Daily Refreshment:</strong> Excellent post-shower, post-sports, or daily routine use.</li>
  <li><strong>Suitable for Teens, Adults & Children:</strong> Ideal universal clean family cologne.</li>
  <li><strong>World-Famous Bench Quality:</strong> #1 recognized global brand in Daily Scent colognes.</li>
  <li><strong>Compact 125ml Bottle:</strong> Ideal size for handbag, school, work, and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Spray Bench cologne onto body skin, neck, and clothing post-shower or any time during the day.</li>
  <li><strong>Step 2:</strong> Allow mist to dry naturally and enjoy the refreshing fragrance aura (use multiple times daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Aromatic Essential Oils with {scent_en} Notes:</strong> Provide a smooth, soft, and long-lasting scent aura.</li>
  <li><strong>Aqua & Refreshing Agents:</strong> Soothe body skin preventing tightness and dryness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body and clothing application.</li>
  <li>Avoid direct spraying into eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from heat and direct sunlight.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for daily fragrant refreshment and clean skin softness.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Bench / Pinch (Daily Scent)</td></tr>
  <tr><th>Category</th><td>Body Care / Bench Daily Scent Colognes 125ml</td></tr>
  <tr><th>Product Type</th><td>Daily Fragranced Refreshing Cologne Mist with {scent_en} (125ml)</td></tr>
  <tr><th>Volume/Weight</th><td>125 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Teens, Men & Women)</td></tr>
  <tr><th>Finish</th><td>Refreshed, soft, clean body skin fragranced with {scent_en}</td></tr>
  <tr><th>Texture</th><td>Clear fast-absorbing lightweight liquid mist</td></tr>
  <tr><th>Fragrance</th><td>Uplifting delightful {scent_en} signature Daily Scent</td></tr>
  <tr><th>Active Ingredients</th><td>Soothing Aromatic Oils, Aqua Solubilizers, Skin Hydrators</td></tr>
  <tr><th>Country of Origin</th><td>Philippines</td></tr>
  <tr><th>Manufacturer</th><td>Suyen Corporation Philippines (Bench)</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 10+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Aqua-Based Cologne Vaporization & Volatile Fragrance Diffusion</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves body sweat odors, heavy perfume suffocating notes, and clothing stain issues.</p>

<h3>Why choose Bench Daily Scent Cologne?</h3>
<p>The lightweight water-based cologne formula diffuses refreshing aromatic notes smoothly across skin without staining fabric.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a refreshing daily cologne body mist from Bench with {scent_en} notes (125ml)."),
        (f"What are the benefits of Bench Daily Scent with {scent_en}?", "Delivers uplifting daily freshness, controls sweat odors, and soothes body skin."),
        ("Does it yield a long-lasting refreshing scent?", "Yes, clinically and traditionally proven to deliver continuous delightful fragrance."),
        ("What volume is contained in this bottle?", "125ml compact bottle."),
        ("How do I use it correctly?", "Spray onto body skin, neck, and clothes post-shower and allow to dry naturally."),
        ("Is it safe for skin and clothing without staining?", "Yes, 100% safe for skin and clothing with zero stainings."),
        ("Where is Bench Cologne manufactured?", "In the Philippines by Suyen Corporation (Bench)."),
        ("How do I verify authenticity at Ekleel Abha?", "All Bench products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", f"Uplifting delightful {scent_en} fragrance."),
        ("Is it suitable for teens, adults, and kids?", "Yes, ideal universal clean family cologne."),
        ("Is the 125ml bottle handbag friendly?", "Yes, sleek compact bottle ideal for handbag, school, and travel."),
        ("How should I store it?", "In a cool, dry place away from heat and direct sunlight."),
        ("Is Bench the #1 Daily Scent cologne brand?", "Yes, Bench is the world's most famous #1 brand in Daily Scent colognes."),
        ("How many times daily?", "Multiple times daily whenever refreshing fragrance is needed."),
        ("Is it great post-workout and post-shower?", "Yes, excellent for refreshing shower routines and post-sports freshness."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help energize the day with uplifting notes?", "Yes, imparts vibrant energy and fresh scent."),
        ("Does it leave skin soft?", "Yes, leaves skin touchably soft and fragranced."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for everyone based on fragrance preference."),
        ("Is it good for all seasons?", "Yes, excellent for summer, winter, school, and daily work."),
        ("Is it a nice gift?", "Yes, an elegant practical gift for students and young adults."),
        ("Does it dry quickly on skin?", "Yes, dries in seconds achieving the desired fragrance aura."),
        ("Are other Bench scents available?", "Yes, the full Bench Daily Scent range is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Bench",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. كولونيا ومعطر جسم يومي فواح بنفحات {scent_ar} من بنش دايلي سينت. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Bench Daily Scent refreshing cologne body mist with {scent_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2046():
    return _make_bench_cologne_b66(
        pid=2046, gtin="4800417059570",
        ar_name="زجاجة كولونيا بابل بوب دايلي سينت من بنش 125مل",
        en_name="Bench Daily Scent Bubble Pop Cologne 125ml",
        scent_ar="بابل بوب الحلوة المبهجة", scent_en="Sweet Bubble Pop",
        feature_ar="كولونيا بابل بوب المبهجة برائحة العلكة والفواكه المنعشة 125 مل", feature_en="sweet bubble pop fruity fragrance cologne 125ml",
        tags_ar=["بنش", "كولونيا_بابل_بوب", "دايلي_سينت_بنش", "كولونيا_اطفال_وشباب", "إكليل_أبها"],
        tags_en=["bench", "bench_bubble_pop", "daily_scent_cologne", "bubble_pop_cologne", "ekleel_abha"]
    )


def create_product_2047():
    return _make_bench_cologne_b66(
        pid=2047, gtin="4800417059549",
        ar_name="روائح معطرة هابي اور دايلي سينت من بنتش 125مل",
        en_name="Pinch Happy Hour Daily Scent Fragrance Mist - 125ml",
        scent_ar="هابي اور الفواحة والمنعشة", scent_en="Uplifting Happy Hour",
        feature_ar="معطر كولونيا هابي اور بنفحات البهجة والانتعاش الصباحي 125 مل", feature_en="happy hour uplifting fragrance mist cologne 125ml",
        tags_ar=["بنتش", "هابي_اور_بنتش", "كولونيا_دايلي_سينت", "معطر_جسم_يومي", "إكليل_أبها"],
        tags_en=["pinch", "happy_hour_mist", "bench_happy_hour", "daily_scent_mist", "ekleel_abha"]
    )


def create_product_2048():
    return _make_bench_cologne_b66(
        pid=2048, gtin="4800417064925",
        ar_name="روائح معطرة اي كاندي سينت من بنتش 125مل",
        en_name="Pinch Eye Candy Scent Fragrance Mist - 125ml",
        scent_ar="اي كاندي الجذابة الساحرة", scent_en="Charming Eye Candy",
        feature_ar="معطر كولونيا اي كاندي بنفحات الزهور والحلويات الجذابة 125 مل", feature_en="eye candy sweet floral fragrance mist 125ml",
        tags_ar=["بنتش", "اي_كاندي_بنتش", "معطر_اي_كاندي", "كولونيا_بنتش", "إكليل_أبها"],
        tags_en=["pinch", "eye_candy_mist", "bench_eye_candy", "fragrance_mist_125ml", "ekleel_abha"]
    )


def create_product_2049():
    return _make_bench_cologne_b66(
        pid=2049, gtin="4800417059587",
        ar_name="روائح معطرة سبرنغ بريك سينت من بنتش 125مل",
        en_name="Bench Spring Break Scented Mist 125ml",
        scent_ar="سبرنغ بريك الربيعية المنعشة", scent_en="Fresh Spring Break",
        feature_ar="معطر كولونيا سبرنغ بريك بنفحات الانتعاش الربيعي الزاهي 125 مل", feature_en="spring break fresh floral citrus cologne mist 125ml",
        tags_ar=["بنش", "سبرنغ_بريك_بنش", "كولونيا_سبرنج_بريك", "معطر_جسم_ربيعي", "إكليل_أبها"],
        tags_en=["bench", "spring_break_mist", "bench_spring_break", "daily_scent_spring", "ekleel_abha"]
    )


print("Loaded all 5 Batch 66 builders complete")
