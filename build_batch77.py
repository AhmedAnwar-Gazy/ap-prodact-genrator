import json, os

def create_product_2104():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم لليدين و الجسم من كوفيكس 275مل (Cofix Hand and Body Cream - 275ml)</strong> كريم الترطيب الطبي الفاخر مغذي للبشرة الأصيل من كوفيكس (Cofix Care) المصمم خصيصاً لترطيب، تغذية، وتنعيم بشرة اليدين والجسم الجافة وتخليصها من التقشر والخشونة. يرتكز هذا الكريم الأصيل (Cofix Cream 275ml) على زبدة الشيا الغنية، الزيوت النباتية المغذية، والمكونات المطرية لبشرة الجسم.</p>
<p>يعمل كريم كوفيكس لليدين والجسم على حبس رطوبة البشرة لـ 24 ساعة، حماية غشاء الجلد من الجفاف، وإعادة المرونة والطراوة الحريرية، ليترك يديك وجسمك في غاية النعومة والنضارة والانتعاش من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتغذية فائقة لـ 24 ساعة لليدين والجسم:</strong> يمنح الجلد طراوة ونعومة ممتدة.</li>
  <li><strong>امتصاص سريع دون ترك أثر دهني لزج:</strong> يسهل الاستخدام اليومي والارتداء السريع للملابس.</li>
  <li><strong>تنعيم اليدين الجافتين والكوعين والركبتين:</strong> يزيل التقشر والخشونة بفاعلية.</li>
  <li><strong>تركيبة لطيفة متوازنة الحموضة (pH Balanced):</strong> مناسبة للاستخدام اليومي لجميع أنواع البشرة.</li>
  <li><strong>جودة كوفيكس (Cofix Care) السعودية الشهيرة:</strong> العلامة الأولى في مستحضرات الترطيب.</li>
  <li><strong>عبوة سعة 275 مل مزودة بضاغط مريح:</strong> حجم ممتاز للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسبة من كريم كوفيكس على بشرة اليدين والجسم النظيفة.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي برفق بحركات دائرية ناعمة حتى الامتصاص الكامل (يُستعمل يومياً صباحاً ومساءً وعند الحاجة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زبدة الشيا والمركبات المطرية:</strong> تحفظان التوازن المائي للجلد وتمنحان نعومة حريرية.</li>
  <li><strong>الجليسرين والزيوت النباتية:</strong> تغذيان البشرة الجافة وتحميان من التقشر.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة اليدين والجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن كريم كوفيكس لليدين والجسم 275 مل للترطيب والتغذية اليومية الفاخرة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كوفيكس (Cofix Care)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم واليدين / كريمات كوفيكس المرطبة 275ml</td></tr>
  <tr><th>نوع المنتج</th><td>كريم مرطب مغذي لليدين والجسم بزبدة الشيا (275ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>275 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة اليدين والجسم (الجافة، العادية والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>يدين وجسم ناعمين كالحرير، مرطبين 24 ساعة، ناصعين النظافة وغير دهنيين</td></tr>
  <tr><th>الملمس</th><td>كريم ناعم غني يمتص فورياً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر النظافة والنعومة الكلاسيكي اللطيف</td></tr>
  <tr><th>المكونات النشطة</th><td>زبدة الشيا، جليسرين، زيوت نباتية مرطبة</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية (KSA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Cofix Care Products</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زبدة الشيا والجليسرين في كريم كوفيكس لليدين والجسم (Cofix Cream)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم كوفيكس لليدين والجسم مشكلة جفاف البشرة الشديد، تقشر الكفين، خشونة الكوعين والركبتين، والطبقة الدهنية الزجة.</p>

<h3>لماذا تنجح تركيبة Cofix Hand and Body Cream?</h3>
<p>لأن زبدة الشيا تعوض الدهون المفقودة بالبشرة بينما يجذب الجليسرين الرطوبة ويحبسها داخل الخلايا.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق فوراً بعد غسل اليدين والاستحمام:</strong> يضاعف امتصاص المرطب.<br>
2. <strong>التركيز على اليدين والكوعين:</strong> يحمي من خشونة الجلد والتصلب.<br>
3. <strong>الاستخدام اليومي المنتظم:</strong> يحافظ على نعومة واستقرار البشرة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات الترطيب تجعل اليدين لزجتين زلقتين."<br>
<strong>الحقيقة:</strong> كريم كوفيكس مصمم بتركيبة ناعمة خفيفة تنفذ فورياً دون ترك أي أثر دهني.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتكامل الأحماض الدهنية في زبدة الشيا مع ميكروليبيدات البشرة مصلحة حاجز الجلد الدهني.</p>"""

    faqs = [
        ("ما هو كريم لليدين و الجسم من كوفيكس 275مل؟", "هو كريم مرطب ومغذي بزبدة الشيا والجليسرين لليدين والجسم من كوفيكس بحجم 275 مل."),
        ("ما هي فوائد زبدة الشيا والجليسرين لليدين والجسم؟", "ترطب وتغذي البشرة لـ 24 ساعة، تمنع الجفاف والتقشر، وتمتص فورياً دون دهنية."),
        ("هل يمتص فورياً ويرطب لـ 24 ساعة بدون دهنية؟", "نعم، مثبت سريرياً في الامتصاص السريع والترطيب 24 ساعة دون طبقة دهنية لزجة."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة مزودة بضاغط مريح سعة 275 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على اليدين والجسم، دلكي برفق حتى الامتصاص مرتين يومياً وعند الحاجة."),
        ("هل هو آمن وخالٍ من المواد القاسية؟", "نعم، 100% آمن ومختبر جلدياً ومناسب لجميع أنواع البشرة."),
        ("أين صُنع كريم كوفيكس لليدين والجسم؟", "صُنع في المملكة العربية السعودية بواسطة Cofix Care Products."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كوفيكس لدى إكليل أبها أصلية 100%."),
        ("ما رائحة كريم كوفيكس؟", "عطر النظافة والنعومة الكلاسيكي اللطيف الفاخر."),
        ("هل يناسب اليدين والجسم معاً؟", "نعم، كريم متعدد الأغراض ممتاز لبشرة اليدين والجسم."),
        ("هل عبوة 275 مل بضاغط مريحة؟", "نعم، عبوة أنيقة بضاغط مريح جداً للاستخدام اليومي والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كوفيكس علامة موثوقة في العناية الشخصية؟", "نعم، Cofix علامة سعودية رائدة وموثوقة جداً في المستحضرات الشخصية."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً أو حسب الحاجة."),
        ("هل يمنح البشرة لمعاناً ونعومة حريرية؟", "نعم، يمنح البشرة توهجاً طبيعياً ونعومة حريرية دون دهنية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في الوقاية من خشونة الكوعين والركبتين؟", "نعم، ينعم الكوعين والركبتين واليدين ويحمي من الخشونة."),
        ("هل يترك ملمساً لزجاً؟", "ينفذ فورياً دون ترك لزوجة أو ثقل."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يناسب الاستخدام في الصيف والشتاء؟", "نعم، ترطيب وتنعيم طبيعي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة؟", "نعم، منتج عناية وترطيب مفيد وأنيق."),
        ("هل يعيد المظهر الصحي والمشرق للبشرة؟", "نعم، يمنح الجسد واليدين مظهراً ناعماً ومشرقاً."),
        ("هل يسهل ارتداء الملابس فوراً بعده؟", "نعم، يمتص سريعاً مما يتيح ارتداء الملابس فوراً دون بقع."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Cofix Hand and Body Cream - 275ml</strong> is an authentic luxury hydrating and nourishing cream from Cofix Care designed to moisturize, nourish, and soften dry hand and body skin while eliminating flaking and roughness. Built upon rich Shea Butter, nourishing botanical oils, and skin-moisturizing compounds.</p>
<p>Cofix Hand and Body Cream locks in skin moisture for 24 hours, protects the skin barrier against dryness, and restores elasticity and silky smoothness, leaving your hands and body touchably soft, radiant, and refreshed from first application.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Superior 24-Hour Hydration & Nourishment for Hands & Body:</strong> Imparts extended softness.</li>
  <li><strong>Fast Rapid Absorption with Zero Heavy Greasy Residue:</strong> Ideal for daily use and immediate dressing.</li>
  <li><strong>Softens Dry Hands, Elbows & Knees:</strong> Eliminates roughness and flaking effectively.</li>
  <li><strong>pH-Balanced Mild Formula:</strong> Suitable for daily use on all skin types.</li>
  <li><strong>Famous Quality of Cofix Care Saudi Arabia:</strong> Premier trusted brand in personal care.</li>
  <li><strong>Convenient 275ml Pump Value Bottle:</strong> Excellent size for daily care and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of Cofix cream onto clean hand and body skin.</li>
  <li><strong>Step 2:</strong> Massage gently in smooth circular motions until fully absorbed (use daily morning, night & as needed).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Shea Butter & Emollients:</strong> Preserve skin moisture balance delivering extreme touchable softness.</li>
  <li><strong>Glycerin & Botanical Oils:</strong> Nourish dry skin protecting against flaking and tightness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hand and body skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Cofix Hand and Body Cream 275ml for daily skin hydration, nourishment, and softness for hands and body.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Cofix Care</td></tr>
  <tr><th>Category</th><td>Body & Hand Care / Cofix Hydrating Creams 275ml</td></tr>
  <tr><th>Product Type</th><td>Nourishing Shea Butter Hydrating Hand & Body Cream (275ml)</td></tr>
  <tr><th>Volume/Weight</th><td>275 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hand & Body Skin Types (Dry, Normal & Oily Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, nourished & non-greasy clear skin</td></tr>
  <tr><th>Texture</th><td>Ultra-lightweight fast-absorbing smooth cream</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh clean soft scent</td></tr>
  <tr><th>Active Ingredients</th><td>Shea Butter, Hydrating Glycerin, Botanical Oils</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia (KSA)</td></tr>
  <tr><th>Manufacturer</th><td>Cofix Care Products</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Shea Butter Fatty Acid Absorption & Epidermal Moisture Locking</h2>

<h3>What problem does this solve?</h3>
<p>Cofix Hand and Body Cream resolves hand and body dryness, flaking palms, rough knees, and greasy cream residue.</p>

<h3>Why choose Cofix Hand and Body Cream?</h3>
<p>Shea butter fatty acids replenish missing skin lipids while glycerin locks in moisture deep within cell layers.</p>"""

    en_faqs = [
        ("What is Cofix Hand and Body Cream - 275ml?", "It is a luxury hydrating and nourishing hand and body cream from Cofix with Shea Butter and Glycerin (275ml)."),
        ("What are the benefits of Shea Butter and Glycerin?", "Hydrate and nourish hands and body for 24 hours, prevent dryness and flaking, and absorb rapidly without greasiness."),
        ("Does it absorb instantly and hydrate for 24 hours without greasiness?", "Yes, clinically proven to absorb rapidly and hydrate for 24 hours without greasy residue."),
        ("What volume is contained in this bottle?", "275ml pump dispenser bottle."),
        ("How do I use it correctly?", "Apply to clean hands and body, massage gently until absorbed twice daily as needed."),
        ("Is it safe and mild for daily use?", "Yes, 100% safe, dermatologically tested, and suitable for all skin types."),
        ("Where is Cofix Hand and Body Cream manufactured?", "In Saudi Arabia by Cofix Care Products."),
        ("How do I verify authenticity at Ekleel Abha?", "All Cofix products at Ekleel Abha are 100% original."),
        ("What scent does Cofix Cream have?", "Luxurious fresh clean soft fragrance."),
        ("Is it suitable for hands and body together?", "Yes, multi-purpose cream excellent for hand and body skin."),
        ("Is the 275ml pump bottle convenient?", "Yes, sleek pump dispenser bottle ideal for daily care and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Cofix a trusted brand in Saudi Arabia?", "Yes, Cofix is a leading trusted brand in personal care in KSA."),
        ("How many times daily?", "Once or twice daily or as needed."),
        ("Does it impart natural glow and silky softness?", "Yes, gives hands and body natural glow and silky softness without greasiness."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help prevent rough elbows and knees?", "Yes, softens elbows, knees, and hands protecting skin from dryness and roughness."),
        ("Does it leave a sticky residue?", "Absorbs instantly without sticky residue or heavy feeling."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it good for all seasons?", "Yes, ideal natural moisturizer for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, practical and thoughtful body care gift."),
        ("Does it restore healthy radiant skin appearance?", "Yes, gives hands and body skin a healthy smooth radiant look."),
        ("Can I get dressed immediately after application?", "Yes, fast absorption allows immediate dressing without staining clothes."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2104",
        "sku": "EK-2104",
        "gtin": "792625756614",
        "brand": "Cofix",
        "ar": {
            "title": "كريم  لليدين و الجسم  من كوفيكس275مل",
            "meta_title": "كريم كوفيكس لليدين والجسم 275مل | إكليل أبها",
            "meta_description": "اشتري كريم لليدين والجسم من كوفيكس (275 مل). كريم طبي بزبدة الشيا والجليسرين لترطيب وتغذية اليدين والجسم 24 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كوفيكس", "كريم_كوفيكس_لليدين_والجسم", "ترطيب_اليدين_والجسم", "كريم_زبدة_الشيا", "إكليل_أبها"]
        },
        "en": {
            "title": "Cofix Hand and Body Cream - 275ml",
            "meta_title": "Cofix Hand and Body Cream 275ml | Ekleel Abha",
            "meta_description": "Buy original Cofix Hand and Body Cream (275ml). Nourishing Shea Butter 24H hand and body hydrating cream. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["cofix", "cofix_hand_body_cream", "shea_cream", "moisturizing_cream", "ekleel_abha"]
        }
    }


def create_product_2105():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم ليلي لتفتيح البشرة المتكامل مع خلاصة التوت البري من اولاي 50 جم (Olay Natural White All-in-One Fairness Night Cream with Mulberry Extract 50g)</strong> الكريم الليلي المفتّح المغذي الفاخر الأصيل من أولاي (Olay) المصمم خصيصاً لتفتيح، تجديد، وترميم بشرة الوجه أثناء النوم والتخلص من التصبغات والبقع الداكنة والشحوب. يرتكز هذا الكريم الأصيل (Olay Night Cream 50g) على خلاصة التوت البري النقية (Mulberry Extract)، الفيتامينات الثلاثية المبيضة (Pro-Vitamin B5, Vitamin B3, Vitamin E)، والتركيبة المغذية الليلية.</p>
<p>يعمل كريم أولاي الليلي على تزويد الخلايا بالتغذية المكثفة أثناء السكون الليلي، تقليل إنتاج صبغة الميلانين، وإعادة التوهج والصفاء الناصع للوجه، ليترك بشرة وجهك ناعمة كالحرير، موحدة اللون، مرطبة، ومشرقة بالنضارة والشباب فور الاستيقاظ صباحاً.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وتوحيد لون الوجه بخلاصة التوت البري والفيتامينات الثلاثية:</strong> يقلل البقع الداكنة والتصبغات.</li>
  <li><strong>تغذية وترميم مكثف أثناء النوم:</strong> يستغل ساعات تجدد الخلايا الليلية لإعادة الحيوية.</li>
  <li><strong>ترطيب وتنعيم فائق لبشرة الوجه:</strong> يحفظ رطوبة الجلد ويمنع الجفاف الصباحي.</li>
  <li><strong>تحسين ملمس ومظهر البشرة الشاحبة:</strong> يمنح الوجه توهجاً ناصعاً ومظهراً مشرقاً.</li>
  <li><strong>تركيبة خفيفة آمنة وغير مسببة لانسداد المسام:</strong> مناسبة للاستخدام الليلي اليومي.</li>
  <li><strong>عبوة سعة 50 جم بحجم أنيق:</strong> تكفي لعدة أشهر من روتين التفتيح الليلي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> نظفي بشرة الوجه والرقبة جيداً والغسيل بالغسول المناسب قبل النوم.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من كريم أولاي الليلي على الوجه والرقبة ودلكي برفق بحركات دائرية لأعلى حتى الامتصاص (يُستعمل يومياً كل ليلة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة التوت البري (Mulberry Extract):</strong> تثبط إنزيم التايروسينيز المسبب للتصبغات والبقع.</li>
  <li><strong>الفيتامينات الثلاثية (B3, B5, E):</strong> تفتح اللون، ترمم الخلايا، وتحمي من الأكسدة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والرقبة ليلاً.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن كريم ليلي لتفتيح البشرة المتكامل مع خلاصة التوت البري من أولاي 50 جم للتفتيح والترميم الليلي.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>أولاي (Olay Procter & Gamble)</td></tr>
  <tr><th>الفئة</th><td>العناية بالوجه / كريمات أولاي الليلية لتفتيح البشرة 50g</td></tr>
  <tr><th>نوع المنتج</th><td>كريم ليلي متكامل لتفتيح البشرة بخلاصة التوت البري والفيتامينات (50g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (خصيصاً المتصبغة، الشاحبة، والجافة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، موحد اللون، ناصع البياض ومفعم بالتوهج الصباحي المشرق</td></tr>
  <tr><th>الملمس</th><td>كريم لؤلؤي غني يمتص بسلاسة ليلاً دون دهنية ثقيلة</td></tr>
  <tr><th>العطر</th><td>عطر لؤلؤي ناعم أنيق</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة التوت البري، فيتامين B3، نياسيناميد، فيتامين B5، فيتامين E</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة المتحدة / بولندا (UK)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Procter & Gamble (P&G)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 18 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد خلاصة التوت البري والفيتامينات الثلاثية في كريم أولاي الليلي (Olay Night Cream)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم أولاي الليلي مشكلة التصبغات الجلدية الليلية، اسمرار وتفاوت لون الوجه، بهتان البشرة، وجفاف الجلد الصباحي.</p>

<h3>لماذا تنجح تركيبة Olay Natural White All-in-One Night Cream؟</h3>
<p>لأن خلاصة التوت البري مع الفيتامينات الثلاثية (B3, B5, E) تستغل ذروة التجدد الخلوي الليلي لتقليل الميلانين.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق كل ليلة على وجه نظيف:</strong> يضمن أقصى امتصاص وترميم لليالي المتتالية.<br>
2. <strong>التدليك بحركات دائرية لأعلى:</strong> ينشط الدورة الدموية الكولاجينية بالوجه.<br>
3. <strong>استخدام واقي شمس صباحاً:</strong> يحمي نتائج التفتيح من الأشعة الفوق بنفسجية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الكريمات الليلية تسبب لزوجة ثقيلة وتنسد المسام."<br>
<strong>الحقيقة:</strong> كريم أولاي الليلي مصمم بتركيبة مائية متميزة تمتص بسلاسة دون التسبب في أي انسداد.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط مركبات الأربوتين الطبيعية بالتوت البري إنزيم Tyrosinase مانعة انتقال الميلانين لسطح البشرة.</p>"""

    faqs = [
        ("ما هو كريم ليلي لتفتيح البشرة المتكامل مع خلاصة التوت البري من اولاي 50 جم؟", "هو كريم ليلي مبيض ومغذي ومفتح للوجه بخلاصة التوت البري والفيتامينات الثلاثية من أولاي (50 جم)."),
        ("ما هي فوائد خلاصة التوت البري والفيتامينات الثلاثية (B3, B5, E) ليلاً؟", "تفتح التصبغات والبقع، توحد لون الوجه، ترمم الخلايا أثناء النوم، وتمنح توهجاً صباحياً مشرقاً."),
        ("هل يفتح ويغذي الوجه ليلاً ويمنح نضارة صباحية؟", "نعم، مثبت سريرياً في تفتيح لون الوجه وتغذيته ليلاً وتوفير إشراقة صباحية ناصعة."),
        ("ما حجم العبوة؟", "تأتي بعبوة زجاجية أنيقة سعة 50 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على الوجه والرقبة النظيفين قبل النوم، دلكي برفق حتى الامتصاص يومياً كل ليلة."),
        ("هل هو آمن وغير مسبب لانسداد المسام؟", "نعم، 100% آمن ومختبر درماتولوجياً وغير مسبب لانسداد المسام (Non-Comedogenic)."),
        ("أين صُنع كريم أولاي الليلي؟", "صُنع بواسطة Procter & Gamble العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات أولاي لدى إكليل أبها أصلية 100%."),
        ("ما رائحة كريم أولاي الليلي؟", "عطر لؤلؤي ناعم أنيق فاخر."),
        ("هل يناسب جميع أنواع البشرة؟", "نعم، ممتاز لجميع أنواع البشرة (الدهنية، الجافة، والمختلطة)."),
        ("هل عبوة 50 جم تكفي لفترة جيدة؟", "نعم، تكفي لعدة أشهر من الاستخدام الليلي المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل أولاي الماركة الأولى عالمياً في تفتيح البشرة؟", "نعم، Olay Natural White الماركة رقم 1 العالمية الأكثر شهرة وتفضيلاً."),
        ("كم مرة يومياً؟", "مرة واحدة يومياً كل ليلة قبل النوم."),
        ("هل يترك أثراً دهنياً ثقيلاً على الوسادة؟", "لا، يمتص بسلاسة ليلية دون أثر دهني لزج."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في الوقاية من البقع الداكنة؟", "نعم، يقلل تكون صبغة الميلانين ويمنع البقع الداكنة."),
        ("هل يناسب الوجه والرقبة؟", "نعم، ممتاز لتفتيح وتوحيد الوجه والرقبة ليلاً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والفتيات؟", "نعم، ممتاز للنساء والفتيات من سن 18 سنة."),
        ("هل يناسب الشتاء والصيف؟", "نعم، تفتيح وترميم ليلي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج عناية وتفتيح فاخر وأساسي لكل روتين ليلة."),
        ("هل يعيد المظهر الوردي المشرق للبشرة؟", "نعم، يمنح الوجه مظهراً ناصع البياض والإشراق."),
        ("هل تتوفر منتجات Olay الأخرى؟", "نعم، تتوفر عائلة Olay Natural White كاملة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Olay Natural White All-in-One Fairness Night Cream with Mulberry Extract 50g</strong> is the world's most recognized authentic luxury medical whitening and nourishing night cream from Olay designed to brighten, renew, and repair facial skin during sleep while fading dark spots, hyperpigmentation, and dullness. Built upon pure Mulberry Extract, Triple Whitening Vitamins (Pro-Vitamin B5, Vitamin B3, Vitamin E), and a nocturnal nourishing formulation.</p>
<p>Olay Night Cream provides intense nourishment to skin cells during peak nocturnal renewal hours, inhibits melanin synthesis, and restores brilliant clarity, leaving your facial skin touchably silky soft, even-toned, hydrated, and radiant upon waking every morning.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Nighttime Whitening & Tone Evening with Mulberry Extract & Triple Vitamins:</strong> Fades dark spots.</li>
  <li><strong>Intensive Nocturnal Cell Repair & Nourishment:</strong> Utilizes sleep hours to renew skin vitality.</li>
  <li><strong>Superior Facial Skin Softening & Hydration:</strong> Seals in internal moisture preventing morning dryness.</li>
  <li><strong>Restores Radiance to Dull Stressed Skin:</strong> Imparts a healthy illuminated morning skin glow.</li>
  <li><strong>Lightweight Non-Comedogenic Formula:</strong> Will not clog pores during sleep.</li>
  <li><strong>Sleek 50g Jar Container:</strong> Excellent size lasting months of continuous nighttime care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Cleanse facial and neck skin thoroughly with a suitable wash before bedtime.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of Olay night cream onto face and neck and massage gently upwards until absorbed (use every night).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Mulberry Extract:</strong> Inhibits tyrosinase enzyme activity reducing dark spot pigmentation.</li>
  <li><strong>Triple Vitamins (B3, B5, E):</strong> Brighten skin tone, repair damaged cells, and provide antioxidant protection.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and neck skin application at night.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Any woman seeking Olay Natural White All-in-One Fairness Night Cream 50g for nighttime skin whitening and repair.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Olay (Procter & Gamble)</td></tr>
  <tr><th>Category</th><td>Skincare / Olay Medical Whitening Night Creams 50g</td></tr>
  <tr><th>Product Type</th><td>All-in-One Mulberry Extract & Triple Vitamin Whitening Night Cream (50g)</td></tr>
  <tr><th>Volume/Weight</th><td>50 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Specifically Hyperpigmented, Dull & Dry Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, even-toned, brightened & morning-radiant glowing face</td></tr>
  <tr><th>Texture</th><td>Rich pearlescent smooth night cream absorbing easily</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh soft elegant scent</td></tr>
  <tr><th>Active Ingredients</th><td>Mulberry Extract, Vitamin B3 (Niacinamide), Pro-Vitamin B5, Vitamin E</td></tr>
  <tr><th>Country of Origin</th><td>UK / Poland</td></tr>
  <tr><th>Manufacturer</th><td>Procter & Gamble (P&G)</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 18+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Mulberry Extract Tyrosinase Inhibition & Nocturnal Cell Regeneration</h2>

<h3>What problem does this solve?</h3>
<p>Olay Natural White Night Cream resolves nighttime skin dullness, uneven facial tone, dark spots, and morning dryness.</p>

<h3>Why choose Olay Natural White Night Cream?</h3>
<p>Mulberry extract combined with Triple Vitamins (B3, B5, E) acts during peak sleep renewal hours to reduce melanin transfer.</p>"""

    en_faqs = [
        ("What is Olay Natural White All-in-One Fairness Night Cream with Mulberry Extract 50g?", "It is a luxury whitening, nourishing, and repairing facial night cream from Olay with Mulberry Extract and Triple Vitamins (50g)."),
        ("What are the benefits of Mulberry Extract and Triple Vitamins (B3, B5, E)?", "Brighten dark spots and tone, nourish cells overnight, and deliver a radiant morning glow."),
        ("Does it brighten and nourish facial skin overnight for morning radiance?", "Yes, clinically proven to brighten skin tone, nourish cells overnight, and impart a clear morning glow."),
        ("What volume is contained in this jar?", "50g sleek glass jar."),
        ("How do I use it correctly?", "Apply to clean face and neck before bedtime, massage gently until absorbed every night."),
        ("Is it safe and non-comedogenic?", "Yes, 100% safe, dermatologically tested, and non-comedogenic (will not clog pores)."),
        ("Where is Olay Night Cream manufactured?", "By Procter & Gamble (P&G)."),
        ("How do I verify authenticity at Ekleel Abha?", "All Olay products at Ekleel Abha are 100% original."),
        ("What scent does Olay Night Cream have?", "Luxurious fresh soft elegant fragrance."),
        ("Is it suitable for all skin types?", "Yes, excellent for dry, oily, and combination facial skin."),
        ("Does the 50g jar last long?", "Yes, lasts months of regular nightly use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Olay a #1 global whitening brand?", "Yes, Olay Natural White is the world's most recognized premier whitening brand."),
        ("How many times daily?", "Once daily every night before bedtime."),
        ("Does it leave a heavy greasy residue on pillows?", "No, absorbs smoothly overnight without heavy greasy residue."),
        ("Is the jar recyclable?", "Yes."),
        ("Does it help prevent dark spot formation?", "Yes, inhibits melanin synthesis preventing dark spot development."),
        ("Is it suitable for face and neck?", "Yes, excellent for whitening face and neck skin overnight."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and teens?", "Yes, suitable for women and teens aged 18+."),
        ("Is it good for all seasons?", "Yes, ideal nighttime whitening for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, an elegant practical nightly whitening gift."),
        ("Does it restore bright glowing skin appearance?", "Yes, gives facial skin a healthy bright radiant look."),
        ("Are other Olay products available?", "Yes, the full Olay Natural White range is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2105",
        "sku": "EK-2105",
        "gtin": "5011321868342",
        "brand": "Olay",
        "ar": {
            "title": "كريم ليلي لتفتيح البشرة المتكامل مع خلاصة التوت البري من اولاي 50 جم",
            "meta_title": "كريم أولاي الليلي لتفتيح البشرة بالتوت البري 50جم | إكليل أبها",
            "meta_description": "اشتري كريم ليلي لتفتيح البشرة المتكامل مع خلاصة التوت البري من أولاي (50 جم). كريم مبيض ومغذي ليلي بالفيتامينات الثلاثية للتخلص من التصبغات. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["أولاي", "كريم_أولاي_الليلي", "تفتيح_البشرة_التوت_البري", "أولاي_ناشرال_وايت", "إكليل_أبها"]
        },
        "en": {
            "title": "Olay Natural White All-in-One Fairness Night Cream with Mulberry Extract 50g",
            "meta_title": "Olay Natural White Night Cream Mulberry 50g | Ekleel Abha",
            "meta_description": "Buy original Olay Natural White All-in-One Fairness Night Cream with Mulberry Extract (50g). Triple Vitamin nighttime skin whitening cream. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["olay", "olay_night_cream", "mulberry_fairness_cream", "olay_natural_white", "ekleel_abha"]
        }
    }


def create_product_2107():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول مقشر بالطين النقي من لوريال - 150مل (L'Oréal Pure Clay Exfoliating Cleanser - 150ml)</strong> الجل المقشر والمنظف الفاخر بالزيوت والطين الأيقوني من لوريال باريس (L'Oréal Paris) المصمم خصيصاً لتنظيف، تقشير، وتصفية مسام الوجه وإزالة الزيوت الزائدة والخلايا الميتة والرؤوس السوداء دون تسبيب أي جفاف. يرتكز هذا الغسول الأصيل (L'Oréal Pure Clay Red Algae 150ml) على 3 أنواع من الطين النقي (Kaolin, Montmorillonite, Ghassoul) مضافاً إليها خلاصة الطحالب الحمراء المقشرة (Red Algae Extract).</p>
<p>يعمل غسول لوريال بالطين النقي والطحالب الحمراء على تقشير البشرة بدقة متناهية، إزالة التكتلات الدهنية من المسام، وتوحيد ملمس الوجه، ليترك بشرتك ناعمة كالحرير، ناصعة النقاء، مطهرة، ومفعمة بالانتعاش والإشراق من الغسلة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تقشير دقيق وتصفية للمسام بخلاصة الطحالب الحمراء:</strong> يزيل الخلايا الميتة والشوائب.</li>
  <li><strong>امتصاص الدهون وتنقية الوجه بـ 3 أنواع من الطين النقي:</strong> الكاولين، المنتيموريلونيت والغاسول.</li>
  <li><strong>تقليل الرؤوس السوداء واللمعان الدهني:</strong> يمنح الوجه مظهرًا صافياً ملساءً.</li>
  <li><strong>ترطيب وتنعيم ملمس بشرة الوجه:</strong> ينظف بفاعلية دون تسبيب أي جفاف.</li>
  <li><strong>مختبر درماتولوجياً ومناسب للبشرة العادية، الدهنية والمختلطة:</strong> آمن للاستخدام اليومي.</li>
  <li><strong>أنبوب سعة 150 مل بمقاس ممتاز:</strong> يناسب الاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الوجه بالماء الدافئ.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من جل الطين النقي ودلكي الوجه برفق بحركات دائرية مع التركيز على منطقة T-Zone.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء الدافئ وجففي الوجه برفق (يُستعمل 2-3 مرات أسبوعياً أو يومياً حسب الحاجة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الطحالب الحمراء و3 أنواع طين نقي:</strong> تقشر الخلايا الميتة وتمتص الدهون وتنقي المسام.</li>
  <li><strong>المنظفات المائية المطرية:</strong> تنظف الوجه وتحفظ النعومة الحريرية للبشرة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه.</li>
  <li>تجنبي التلامس المباشر مع العينين ومحيطهما.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن غسول مقشر بالطين النقي والطحالب الحمراء من لوريال 150 مل لتقشير وتصفية مسام الوجه.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لوريال باريس (L'Oréal Paris)</td></tr>
  <tr><th>الفئة</th><td>العناية بالوجه / غسولات ومقشرات لوريال بالطين النقي 150ml</td></tr>
  <tr><th>نوع المنتج</th><td>جل غسول مقشر بـ 3 أنواع طين نقي وطحالب حمراء (150ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>150 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة العادية، الدهنية، المختلطة والمعرضة لحب الشباب والرؤوس السوداء</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، ناصع النظافة، مطهر ومصمور المسام خالي من الدهنية</td></tr>
  <tr><th>الملمس</th><td>جل طيني دقيق التكتلات ينقلب لرغوة تقشير ناعمة</td></tr>
  <tr><th>العطر</th><td>عطر الطين والورد المعدني المنعش الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>طين الكاولين، المنتيموريلونيت، الغاسول، خلاصة الطحالب الحمراء</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>L'Oréal Paris Group</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الطحالب الحمراء و3 أنواع طين نقي في مقشر لوريال (L'Oréal Pure Clay Cleanser)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول لوريال مقشر الطين النقي مشكلة انسداد المسام بالرؤوس السوداء، تكتل الدهون، خشونة ملمس الوجه، والبهتان.</p>

<h3>لماذا تنجح تركيبة L'Oréal Pure Clay Red Algae Cleanser؟</h3>
<p>لأن دمج الطحالب الحمراء المقشرة مع أنواع الطين الـ 3 (الكاولين والغاسول والمنتيموريلونيت) يمتص الزهم ويقشر الدقائق.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التدليك بحركات دائرية دقيقة على T-Zone:</strong> يزيل الرؤوس السوداء حول الأنف والجبين.<br>
2. <strong>الشطف الجيد بالماء الدافئ:</strong> يضمن إزالة حبيبات الطين بالكامل.<br>
3. <strong>الاستخدام 2-3 مرات أسبوعياً:</strong> يمنح ملمس وجه أملس كالحرير.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "غسولات الطين تسبب خدش وتجفيف البشرة الشديد."<br>
<strong>الحقيقة:</strong> مقشر لوريال بالطين النقي مصمم بحبيبات طحالب حمراء مجهرية تنظف وتقشر بأمان ناعم دون أي خدش.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تمتص الصفيحات الطينية الكاتيونات الدهنية بينما تجدد الطحالب الحمراء الكيراتين السطحي.</p>"""

    faqs = [
        ("ما هو غسول مقشر بالطين النقي من لوريال - 150مل؟", "هو جل غسول مقشر بـ 3 أنواع طين نقي وطحالب حمراء لتقشير وتصفية مسام الوجه من لوريال (150 مل)."),
        ("ما هي فوائد الطحالب الحمراء والـ 3 أنواع طين نقي؟", "تقشر الخلايا الميتة والدقائق، تمتص الدهون الزائدة، وتصفي المسام من الرؤوس السوداء."),
        ("هل يقشر وينظف المسام ويقلل الرؤوس السوداء بدون جفاف؟", "نعم، مثبت سريرياً في تقشير البشرة وتصفية المسام وتقليل الرؤوس السوداء."),
        ("ما حجم العبوة؟", "تأتي بأنبوب أنيق سعة 150 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الوجه، ضعي كمية، دلكي برفق بحركات دائرية واشطفي بالماء الدافئ 2-3 مرات أسبوعياً."),
        ("هل هو آمن ومختبر درماتولوجياً؟", "نعم، 100% آمن ومختبر درماتولوجياً على بشرة الوجه."),
        ("أين صُنع غسول لوريال بالطين النقي؟", "صُنع في فرنسا بواسطة L'Oréal Paris."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لوريال لدى إكليل أبها أصلية 100%."),
        ("ما رائحة غسول لوريال بالطين النقي؟", "عطر الطين والورد المعدني المنعش الفاخر."),
        ("هل يناسب البشرة الدهنية والمختلطة؟", "نعم، ممتاز للبشرة العادية، الدهنية، المختلطة والمعرضة للرؤوس السوداء."),
        ("هل أنبوب 150 مل مريح ومناسب للسفر؟", "نعم، أنبوب أنيق مدمج مثالي للاستخدام اليومي والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل لوريال باريس الماركة الأولى عالمياً في الجمال؟", "نعم، L'Oréal Paris الماركة رقم 1 العالمية الرائدة في الجمال والجماليات."),
        ("كم مرة أسبوعياً؟", "2 إلى 3 مرات أسبوعياً أو حسب الحاجة."),
        ("هل يزيل الرؤوس السوداء والزيوت؟", "نعم، يزيل الزيوت الزائدة والشوائب والرؤوس السوداء بفاعلية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يترك ملمس الوجه ناعماً كالحرير؟", "نعم، ينظف ليترك ملمس الوجه ناعماً وأملس كالحرير."),
        ("هل يسبب انسداد المسام؟", "لا، ينظف المسام ويعالج انسدادها بفاعلية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يفضل اتباع مرطب خفيف بعده؟", "نعم، يُفضل استخدام مرطب خفيف بعد الغسيل والتنظيف."),
        ("هل يناسب الصيف والشتاء؟", "نعم، تقشير وتصفية مثالية لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج تقشير وتصفية فاخر وأساسي لكل روتين عناية."),
        ("هل يعيد المظهر المشرق الصافي للوجه؟", "نعم، يمنح الوجه مظهراً صافياً ومشرقاً."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>L'Oréal Pure Clay Exfoliating Cleanser - 150ml</strong> is an authentic luxury exfoliator and clarifying gel cleanser from L'Oréal Paris designed to clean, exfoliate, and refine facial pores while removing excess sebum, dead skin cells, and blackheads without dryness. Built upon 3 Pure Clays (Kaolin, Montmorillonite, Ghassoul) infused with micro-exfoliating Red Algae Extract.</p>
<p>L'Oréal Pure Clay Cleanser with Red Algae gently polishes skin texture, purifies clogged pores of sebum plugs, and unifies facial softness, leaving your face touchably silky soft, spotlessly clean, refined, and radiant from first wash.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Micro-Exfoliating & Pore Refining with Red Algae Extract:</strong> Gently sweeps away dead cells and dirt.</li>
  <li><strong>Sebum Adsorption & Pore Purifying with 3 Pure Clays:</strong> Kaolin, Montmorillonite, and Ghassoul.</li>
  <li><strong>Blackhead & Shine Reduction:</strong> Delivers a smooth refined facial finish.</li>
  <li><strong>Facial Skin Softening & Smoothing:</strong> Cleanses effectively without causing dryness.</li>
  <li><strong>Dermatologically Tested Safe Formula:</strong> Safe for normal, oily, and combination skin types.</li>
  <li><strong>Sleek 150ml Tube Container:</strong> Convenient format for daily care and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet facial skin with warm water.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of pure clay gel, massage face gently in circular motions focusing on T-zone.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and pat face dry (use 2-3 times weekly or daily as needed).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Red Algae Extract & 3 Pure Clays:</strong> Exfoliate dead cells, absorb excess sebum, and purify pores.</li>
  <li><strong>Aqueous Emollient Cleansers:</strong> Cleanse face while maintaining touchable silky softness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial skin application.</li>
  <li>Avoid direct contact with eyes and eye contour.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking L'Oréal Pure Clay Exfoliating Cleanser 150ml for pore refining, exfoliation, and blackhead control.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>L'Oréal Paris</td></tr>
  <tr><th>Category</th><td>Skincare / L'Oréal Pure Clay Cleansers & Scrubs 150ml</td></tr>
  <tr><th>Product Type</th><td>3 Pure Clays & Red Algae Micro-Exfoliating Facial Cleanser (150ml)</td></tr>
  <tr><th>Volume/Weight</th><td>150 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Normal, Oily, Combination & Blackhead-Prone Skin</td></tr>
  <tr><th>Finish</th><td>Spotlessly clean, smooth, refined & oil-free silky soft face</td></tr>
  <tr><th>Texture</th><td>Micro-beaded clay gel transforming into a smooth exfoliating lather</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh mineral rose clay scent</td></tr>
  <tr><th>Active Ingredients</th><td>Kaolin, Montmorillonite, Ghassoul Clays, Red Algae Extract</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>L'Oréal Paris Group</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Red Algae Micro-Exfoliation & 3 Pure Clay Sebum Adsorption</h2>

<h3>What problem does this solve?</h3>
<p>L'Oréal Pure Clay Exfoliating Cleanser resolves clogged blackhead pores, sebum buildup, rough skin texture, and dullness.</p>

<h3>Why choose L'Oréal Pure Clay Red Algae Cleanser?</h3>
<p>Micro-exfoliating red algae combined with 3 Pure Clays adsorbs sebum while gently polishing dead surface skin cells.</p>"""

    en_faqs = [
        ("What is L'Oréal Pure Clay Exfoliating Cleanser - 150ml?", "It is a micro-exfoliating clay gel cleanser from L'Oréal Paris with 3 Pure Clays and Red Algae Extract (150ml)."),
        ("What are the benefits of Red Algae and 3 Pure Clays?", "Exfoliate dead skin cells, absorb excess sebum, and purify pores from blackheads."),
        ("Does it exfoliate and refine pores without dryness?", "Yes, clinically proven to exfoliate skin, refine pores, and reduce blackheads without drying facial skin."),
        ("What volume is contained in this tube?", "150ml sleek tube."),
        ("How do I use it correctly?", "Wet face, apply gel, massage gently in circular motions and rinse with warm water 2-3 times weekly."),
        ("Is it safe and dermatologically tested?", "Yes, 100% safe and dermatologically tested on facial skin."),
        ("Where is L'Oréal Pure Clay Cleanser manufactured?", "In France by L'Oréal Paris."),
        ("How do I verify authenticity at Ekleel Abha?", "All L'Oréal products at Ekleel Abha are 100% original."),
        ("What scent does L'Oréal Pure Clay Cleanser have?", "Luxurious fresh mineral rose clay fragrance."),
        ("Is it suitable for oily and combination skin?", "Yes, excellent for normal, oily, combination, and blackhead-prone skin."),
        ("Is the 150ml tube travel friendly?", "Yes, sleek compact tube ideal for daily care and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is L'Oréal Paris a #1 global beauty brand?", "Yes, L'Oréal Paris is the world's #1 leading beauty brand."),
        ("How many times weekly?", "2 to 3 times weekly or as needed."),
        ("Does it remove blackheads and oil?", "Yes, effectively cleanses excess oil, impurities, and blackheads."),
        ("Is the tube recyclable?", "Yes."),
        ("Does it leave facial skin touchably smooth?", "Yes, cleanses smoothly leaving facial skin refined and touchably soft."),
        ("Does it clog pores?", "No, purifies and unblocks pores effectively."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is following with a lightweight moisturizer recommended?", "Yes, follow with a lightweight moisturizer after cleansing."),
        ("Is it good for all seasons?", "Yes, ideal exfoliating cleansing for summer and winter."),
        ("Is it a nice skincare gift?", "Yes, a premier skincare essential for facial routines."),
        ("Does it restore clean radiant skin appearance?", "Yes, gives facial skin a clear healthy radiant look."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2107",
        "sku": "EK-2107",
        "gtin": "3600523431168",
        "brand": "L'Oréal Paris",
        "ar": {
            "title": "غسول مقشر بالطين النقي من لوريال - 150مل",
            "meta_title": "غسول لوريال مقشر بالطين النقي والطحالب الحمراء 150مل | إكليل أبها",
            "meta_description": "اشتري غسول مقشر بالطين النقي من لوريال (150 مل). جل غسول مصفٍ بـ 3 أنواع طين نقي وطحالب حمراء لتقشير وتصفية المسام. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["لوريال", "غسول_لوريال_بالطين_النقي", "مقشر_الطحالب_الحمراء", "لوريال_150مل", "إكليل_أبها"]
        },
        "en": {
            "title": "L'Oréal Pure Clay Exfoliating Cleanser - 150ml",
            "meta_title": "L'Oréal Pure Clay Exfoliating Cleanser 150ml | Ekleel Abha",
            "meta_description": "Buy original L'Oréal Pure Clay Exfoliating Cleanser (150ml). 3 Pure Clays & Red Algae micro-exfoliating pore refining wash. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["loreal", "loreal_pure_clay", "red_algae_scrub", "clay_cleanser", "ekleel_abha"]
        }
    }


def create_product_2108():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول الوجه بالشاي الأخضر الياباني فير آند لفلي 150جم (Fair & Lovely Japanese Green Tea Face Wash 150g)</strong> المنظف المفتّح المنعش الفاخر الأصيل من فير آند لفلي (Fair & Lovely / Glow & Lovely) المصمم خصيصاً لتنظيف، تصفية، وتفتيح بشرة الوجه وإزالة الدهون الزائدة وأثر الشمس والشوائب بفضل خلاصات مضادات الأكسدة اليابانية. يرتكز هذا الغسول الأصيل (Fair & Lovely Green Tea 150g) على خلاصة الشاي الأخضر الياباني النقي (Japanese Green Tea Extract)، فيتامين B3 المبيض (Niacinamide)، والتركيبة الرغوية المنشطة.</p>
<p>يعمل غسول فير آند لفلي بالشاي الأخضر الياباني على تقليل الإفرازات الدهنية، تنقية مسام الوجه من الأكسدة والسموم، وتزويد البشرة بفرق فيتـاميني مفتح ملموس، ليترك بشرتك ناعمة كالحرير، ناصعة النقاء، مطهرة، ومفعمة بالانتعاش والإشراق من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وتصفية فائقة للبشرة بالشاي الأخضر الياباني:</strong> يزيل البقع الداكنة وأثر الشمس.</li>
  <li><strong>مضاد أكسدة قوي ومحارب للسموم والدهون:</strong> ينظف مسام الوجه ب فاعلية وانتعاش.</li>
  <li><strong>توحيد لون البشرة وتقليل اللمعان الزائد بفيتامين B3:</strong> يمنح الوجه مظهراً مات ناصعاً.</li>
  <li><strong>ترطيب وتنعيم ملمس بشرة الوجه:</strong> ينظف دون تسبيب أي جفاف أو شد.</li>
  <li><strong>جودة فير آند لفلي (Fair & Lovely) الشهيرة عالمياً:</strong> العلامة الأولى في تفتيح البشرة.</li>
  <li><strong>عبوة سعة 150 جم بحجم مالي ممتاز:</strong> تكفي للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الوجه بالماء الدافئ.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من غسول الشاي الأخضر وكوّني رغوة غنية ودلكي الوجه برفق.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء الدافئ وجففي الوجه برفق (يُستعمل مرتين يومياً صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة الشاي الأخضر الياباني وفيتامين B3:</strong> تحاربان الأكسدة وتفتحان التصبغات وتنظمان الدهون.</li>
  <li><strong>المنظفات الرغوية اللطيفة المائية:</strong> تنظف المسام وتحفظ النعومة الحريرية للوجه.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن غسول الوجه بالشاي الأخضر الياباني فير آند لفلي 150 جم للتنظيف، التفتيح، وتنقية المسام.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>فير آند لفلي (Fair & Lovely / Glow & Lovely)</td></tr>
  <tr><th>الفئة</th><td>العناية بالوجه / غسولات فير آند لفلي المفتحة 150g</td></tr>
  <tr><th>نوع المنتج</th><td>غسول وجه رغوي مفتح ومصفٍ بالشاي الأخضر الياباني وفيتامين B3 (150g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>150 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (خصيصاً الدهنية، المختلطة، والمصحوبة بالتصبغات)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، موحد اللون، ناصع النقاء وغير لامع بالدهون</td></tr>
  <tr><th>الملمس</th><td>كريم سائل رغوي غني ينشطف بالماء بسهولة</td></tr>
  <tr><th>العطر</th><td>عطر الشاي الأخضر الياباني المنعش الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة الشاي الأخضر الياباني، فيتامين B3 (نياسيناميد)، منظفات مائية</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الهند</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever Group</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الشاي الأخضر الياباني وفيتامين B3 في غسول فير آند لفلي (Fair & Lovely Green Tea)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول فير آند لفلي بالشاي الأخضر مشكلة أكسدة البشرة، الدهون الزائدة، اسمرار الشمس، وبهتان ملمس الوجه.</p>

<h3>لماذا تنجح تركيبة Fair & Lovely Japanese Green Tea Face Wash؟</h3>
<p>لأن مادة EGCG بالشاي الأخضر الياباني تقضي على الشوارد الحرة بينما يفتح فيتامين B3 التصبغات.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنظيف مرتين يومياً بالماء الدافئ:</strong> ينظف المسام ويمنع أكسدة الدهون.<br>
2. <strong>التكميل بكريم فير آند لفلي للتفتيح:</strong> يضاعف مفعول تفتيح البشرة.<br>
3. <strong>التجفيف اللطيف بالمنشفة:</strong> يحافظ على نعومة واستقرار الوجه.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "غسولات الشاي الأخضر تسبب جفاف الوجه الشديد."<br>
<strong>الحقيقة:</strong> غسول فير آند لفلي مدعم بمركبات مائية تحفظ رطوبة ونعومة البشرة أثناء الغسل.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط البوليفينولات في الشاي الأخضر الياباني التهابات الأكسدة والدهون مظهرة بشرة صافية وموحدة.</p>"""

    faqs = [
        ("ما هو غسول الوجه بالشاي الأخضر الياباني فير آند لفلي 150جم؟", "هو غسول وجه رغوي مفتح ومصفٍ بالشاي الأخضر الياباني وفيتامين B3 من فير آند لفلي (150 جم)."),
        ("ما هي فوائد الشاي الأخضر الياباني وفيتامين B3 للبشرة؟", "يحاربان الأكسدة، يزيلان الدهون والسموم، يفتحان التصبغات، ويوحدان لون الوجه."),
        ("هل ينظف ويفتح المسام ويقلل الدهون بدون جفاف؟", "نعم، مثبت سريرياً في تنظيف المسام وتفتيح الوجه وتقليل الدهون واللمعان."),
        ("ما حجم العبوة؟", "تأتي بأنبوب أنيق سعة 150 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الوجه، ضعي كمية وكوّني رغوة، دلكي برفق واشطفي بالماء الدافئ مرتين يومياً."),
        ("هل هو آمن ومختبر درماتولوجياً؟", "نعم، 100% آمن ومختبر درماتولوجياً ومناسب لجميع أنواع البشرة."),
        ("أين صُنع غسول فير آند لفلي بالشاي الأخضر؟", "صُنع بواسطة مجموعة Unilever العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات فير آند لفلي لدى إكليل أبها أصلية 100%."),
        ("ما رائحة غسول فير آند لفلي بالشاي الأخضر؟", "عطر الشاي الأخضر الياباني المنعش الفاخر."),
        ("هل يناسب البشرة الدهنية والمختلطة؟", "نعم، ممتاز للبشرة الدهنية، المختلطة، والعادية المعرضة للتصبغات."),
        ("هل أنبوب 150 جم مريح وموفر؟", "نعم، أنبوب موفر ومريح جداً للاستخدام اليومي والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل فير آند لفلي الماركة الأولى عالمياً في التفتيح؟", "نعم، Fair & Lovely الماركة الأكثر شهرة وثقة في تفتيح البشرة."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل يزيل المكياج والزيوت؟", "نعم، يزيل الزيوت الزائدة والمكياج اليومي والشوائب بفاعلية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يقلل أثر الشمس والبهتان؟", "نعم، ينقي المسام ويقلل أثر الشمس والبهتان."),
        ("هل يترك ملمس الوجه ناعماً كالحرير؟", "نعم، يمتص فورياً ليترك الوجه ناعماً كالحرير دون دهنية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء والفتيات؟", "نعم، ممتاز للنساء والفتيات والرجال."),
        ("هل يفضل اتباع كريم مفتح بعده؟", "نعم، يُفضل استخدام كريم مفتح من فير آند لفلي بعد الغسل."),
        ("هل يناسب الصيف والشتاء؟", "نعم، ممتاز لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج تفتيح وتصفية فاخر وأساسي لكل روتين عناية."),
        ("هل يعيد المظهر المشرق الصافي للوجه؟", "نعم، يمنح الوجه مظهراً صافياً ومشرقاً."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Fair & Lovely Japanese Green Tea Face Wash 150g</strong> is an authentic luxury brightening and refreshing cleanser from Fair & Lovely (Glow & Lovely) designed to clean, clarify, and brighten facial skin while sweeping away excess sebum, sun tanning, and impurities using Japanese antioxidant extracts. Built upon Japanese Green Tea Extract, brightening Vitamin B3 (Niacinamide), and an invigorating foaming formulation.</p>
<p>Fair & Lovely Japanese Green Tea Face Wash reduces sebum secretion, purifies facial pores of oxidative stress and toxins, and provides a visible vitamin-brightened skin difference, leaving your face touchably silky soft, spotlessly clean, refined, and radiant from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Superior Skin Brightening & Clarifying with Japanese Green Tea:</strong> Fades dark spots and sun tanning.</li>
  <li><strong>Powerful Antioxidant & Sebum Cleanser:</strong> Cleanses facial pores effectively and refreshingly.</li>
  <li><strong>Tone Evening & Shine Reduction with Vitamin B3:</strong> Delivers a clear matte facial skin finish.</li>
  <li><strong>Facial Skin Softening & Hydration:</strong> Cleanses without causing dryness or tight feelings.</li>
  <li><strong>Famous Quality of Fair & Lovely Global:</strong> #1 recognized brand in skin brightening.</li>
  <li><strong>Generous 150g Value Tube:</strong> Outstanding value lasting months of continuous daily use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet facial skin with warm water.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of green tea face wash, work into a rich lather, and massage gently.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and pat face dry (use twice daily morning and night).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Japanese Green Tea Extract & Vitamin B3:</strong> Combat oxidative stress, brighten dark spots, and regulate oiliness.</li>
  <li><strong>Mild Foaming Aqueous Cleansers:</strong> Cleanse pores while maintaining touchable silky softness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial skin application.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Fair & Lovely Japanese Green Tea Face Wash 150g for facial skin brightening, cleansing, and oil control.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Fair & Lovely (Glow & Lovely)</td></tr>
  <tr><th>Category</th><td>Skincare / Fair & Lovely Brightening Cleansers 150g</td></tr>
  <tr><th>Product Type</th><td>Japanese Green Tea & Vitamin B3 Brightening Foaming Cleanser (150g)</td></tr>
  <tr><th>Volume/Weight</th><td>150 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Specifically Oily, Combination & Hyperpigmented Skin)</td></tr>
  <tr><th>Finish</th><td>Spotlessly clean, 24H hydrated, even-toned & matte silky soft face</td></tr>
  <tr><th>Texture</th><td>Rich smooth foaming cream transforming into a fresh lather</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh Japanese green tea fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Japanese Green Tea Extract, Vitamin B3 (Niacinamide), Aqueous Cleansers</td></tr>
  <tr><th>Country of Origin</th><td>KSA / India</td></tr>
  <tr><th>Manufacturer</th><td>Unilever Group</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Japanese Green Tea EGCG Antioxidants & Vitamin B3 Depigmentation</h2>

<h3>What problem does this solve?</h3>
<p>Fair & Lovely Japanese Green Tea Face Wash resolves facial oxidation, excess sebum, sun tanning, and skin dullness.</p>

<h3>Why choose Fair & Lovely Green Tea Cleanser?</h3>
<p>Japanese Green Tea EGCG neutralizes free radicals while Vitamin B3 reduces melanin transfer to skin surface.</p>"""

    en_faqs = [
        ("What is Fair & Lovely Japanese Green Tea Face Wash 150g?", "It is a luxury brightening and clarifying foaming facial cleanser from Fair & Lovely with Japanese Green Tea and Vitamin B3 (150g)."),
        ("What are the benefits of Japanese Green Tea and Vitamin B3?", "Combat oxidation, clear oil and toxins, brighten dark spots, and even facial skin tone."),
        ("Does it clean pores and brighten facial skin without dryness?", "Yes, clinically proven to clean pores, brighten skin tone, and reduce excess oil."),
        ("What volume is contained in this tube?", "150g value tube."),
        ("How do I use it correctly?", "Wet face, apply wash, lather, massage gently and rinse with warm water twice daily."),
        ("Is it safe and dermatologically tested?", "Yes, 100% safe and dermatologically tested on facial skin."),
        ("Where is Fair & Lovely Green Tea Wash manufactured?", "By Unilever Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All Fair & Lovely products at Ekleel Abha are 100% original."),
        ("What scent does Fair & Lovely Green Tea Wash have?", "Luxurious fresh Japanese green tea fragrance."),
        ("Is it suitable for oily and combination skin?", "Yes, excellent for oily, combination, and hyperpigmented facial skin."),
        ("Is the 150g tube travel friendly?", "Yes, sleek value tube ideal for daily care and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Fair & Lovely a #1 global brightening brand?", "Yes, Fair & Lovely is the world's most recognized premier skin brightening brand."),
        ("How many times daily?", "Twice daily (morning and night)."),
        ("Does it remove makeup and dirt?", "Yes, effectively cleanses excess oil, light makeup, and daily impurities."),
        ("Is the tube recyclable?", "Yes."),
        ("Does it help reduce sun tanning and dullness?", "Yes, clarifies pores reducing sun tanning and dull skin texture."),
        ("Does it leave facial skin touchably silky soft?", "Yes, cleanses smoothly leaving facial skin touchably soft without greasiness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is following with a brightening cream recommended?", "Yes, follow with a Fair & Lovely brightening cream after washing."),
        ("Is it good for all seasons?", "Yes, ideal skin brightening cleansing for summer and winter."),
        ("Is it a nice skincare gift?", "Yes, a premier skincare essential for facial routines."),
        ("Does it restore clean radiant skin appearance?", "Yes, gives facial skin a clear healthy radiant look."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2108",
        "sku": "EK-2108",
        "gtin": "6281006567429",
        "brand": "Fair & Lovely",
        "ar": {
            "title": "غسول الوجه بالشاي الأخضر الياباني  فير آند لفلي 150جم",
            "meta_title": "غسول فير آند لفلي بالشاي الأخضر الياباني 150جم | إكليل أبها",
            "meta_description": "اشتري غسول الوجه بالشاي الأخضر الياباني من فير آند لفلي (150 جم). غسول رغوي مفتح ومصفٍ للبشرة بالنياسيناميد ومضادات الأكسدة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["فير_آند_لفلي", "غسول_الشاي_الأخضر_الياباني", "تفتيح_الوجه_فير_آند_لفلي", "غلو_آند_لفلي", "إكليل_أبها"]
        },
        "en": {
            "title": "Fair & Lovely Japanese Green Tea Face Wash 150g",
            "meta_title": "Fair & Lovely Japanese Green Tea Face Wash 150g | Ekleel Abha",
            "meta_description": "Buy original Fair & Lovely Japanese Green Tea Face Wash (150g). Brightening & antioxidant facial cleanser with Vitamin B3. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["fair_and_lovely", "japanese_green_tea_wash", "glow_and_lovely", "brightening_face_wash", "ekleel_abha"]
        }
    }


def create_product_2109():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>واقي شمسي للوجه بعامل حماية من الشمس بدرجة 50+من بيزلين 60مل (Beesline Facial Sunscreen SPF 50+ - 60ml)</strong> كريم الوقاية والحماية الشمسية الفاخر الأسطوري الأكثر توصية من بيزلين (Beesline) المصمم خصيصاً لحماية بشرة الوجه الحساسة والدقيقة من أضرار حروق الشمس، الأشعة الفوق بنفسجية (UVA/UVB)، والتصبغات والشيخوخة المبكرة مع توفير مظهر مات خالي من اللمعان. يرتكز هذا الواقي الأصيل (Beesline Sunscreen SPF50+ 60ml) على زيت سسمون الشمعي (Beeswax)، زيت السمسم، الفيتامينات المضادة للأكسدة (Vitamin C & E)، والفلاتر الشمسية المعدنية والفيزيائية.</p>
<p>يعمل واقي شمس بيزلين للوجه على حجب أكثر من 98% من الأشعة الفوق بنفسجية الضارة، ترميم حاجز بشرة الوجه، ومنع ظهور التصبغات والكلف، ليترك وجهك ناعماً كالحرير، ناصع النقاء، مرطباً، ومحمياً بحماية كاملة من الشمس من التطبيق الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية فائقة جداً SPF 50+ واسعة الطيف (UVA/UVB Protection):</strong> يحجب 98%+ من الأشعة الضارة.</li>
  <li><strong>وقاية طبيعية بشمع العسل ومضادات الأكسدة:</strong> تمنع شيخوخة البشرة والتصبغات والكلف.</li>
  <li><strong>لمسة نهائية مات خالية من اللمعان والطبقة البيضاء:</strong> يمتص فورياً دون تلطيخ.</li>
  <li><strong>ترطيب وتغذية فائقة لبشرة الوجه الحساسة:</strong> يحافظ على مرونة وطراوة الجلد في الشاطئ والشمس.</li>
  <li><strong>تركيبة خالية 100% من البارابين والفثالات والمواد المهيجة:</strong> مقاومة للماء والتعرق.</li>
  <li><strong>أنبوب مدمج سعة 60 مل بحجم أنيق:</strong> مثالي للحقيبة والسفر والتطبيق المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية سخية من واقي شمس بيزلين على بشرة الوجه والرقبة قبل التعرض للشمس بـ 15-20 دقيقة.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي برفق بحركات دائرية حتى الامتصاص الفوري (يُعاد تطبيقه كل ساعتين وبعد السباحة والتجفيف).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>شمع العسل (Beeswax) وفيتامينات (C & E):</strong> يعزلان الجلد ويحميان من الأكسدة وتضرر الأشعة.</li>
  <li><strong>الفلاتر الشمسية الواقية واسعة الطيف:</strong> تحجب أشعة UVA المسببة للتجاعيد و UVB المسببة للحروق.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والرقبة.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن الشمس.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن واقي شمسي للوجه بعامل حماية 50+ من بيزلين 60 مل للحماية الكاملة من التصبغات والشمس.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline Laboratories)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشمس والوجه / واقيات الشمس من بيزلين SPF50+ 60ml</td></tr>
  <tr><th>نوع المنتج</th><td>كريم واقي شمس طبي واسع الطيف SPF 50+ بشمع العسل (60ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>60 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (خصيصاً الحساسة، الفاتحة، والمصابة بالتصبغات)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، مرطب، محمي 100% وخالٍ من اللمعان الدهني والطبقة البيضاء</td></tr>
  <tr><th>الملمس</th><td>كريم ناعم خفيف يمتص فورياً دون ثقل</td></tr>
  <tr><th>العطر</th><td>عطر بيزلين العسلي النقي اللطيف</td></tr>
  <tr><th>المكونات النشطة</th><td>شمع العسل، فيتامين C و E، فلاتر حماية UV معدنية وفيزيائية</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline International Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد شمع العسل والفلاتر واسعة الطيف في واقي شمس بيزلين (Beesline Sunscreen SPF50+)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج واقي شمس بيزلين مشكلة حروق الشمس، ظهور الكلف والتصبغات، التسمر الداكن، والشيخوخة المبكرة بفعل UV.</p>

<h3>لماذا تنجح تركيبة Beesline Facial Sunscreen SPF 50+؟</h3>
<p>لأن شمع العسل يشكل عازلاً طبيعياً يثبت الفلاتر الشمسية واسعة الطيف (UVA/UVB) ويمنع نفاد الأشعة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق قبل التعرض للشمس بـ 15 دقيقة:</strong> يضمن تشكل درع الحماية الكامل.<br>
2. <strong>إعادة التطبيق كل ساعتين وفي السباحة:</strong> يحافظ على استمرار حماية SPF 50+.<br>
3. <strong>الاستخدام اليومي بالصيف والشتاء:</strong> يحمي الوجه من التصبغات المزمنة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "واقيات الشمس تترك طبقة بيضاء لزجة وتسبب انسداد المسام."<br>
<strong>الحقيقة:</strong> واقي بيزلين مصمم بتركيبة خفيفة غير مسببة للانسداد تمتص فورياً دون أي أثر أبيض.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تعكس الفلاتر الفيزيائية أشعة UVB الحارقة بينما تمتص الفلاتر الكيميائية أشعة UVA المسببة للتجاعيد.</p>"""

    faqs = [
        ("ما هو واقي شمسي للوجه بعامل حماية من الشمس بدرجة 50+من بيزلين 60مل؟", "هو كريم واقي شمس طبي واسع الطيف SPF 50+ بشمع العسل ومضادات الأكسدة من بيزلين للوجه (60 مل)."),
        ("ما هي فوائد شمع العسل وحماية SPF 50+ واسعة الطيف؟", "تحجب 98%+ من الأشعة الضارة (UVA/UVB)، تمنع الكلف والتصبغات، وترطب الوجه دون لمعان."),
        ("هل يحمي من حروق الشمس والتصبغات بدون طبقة بيضاء؟", "نعم، مثبت سريرياً في توفير حماية كاملة SPF 50+ والامتصاص السريع دون طبقة بيضاء."),
        ("ما حجم العبوة؟", "تأتي بأنبوب أنيق سعة 60 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية سخية قبل الشمس بـ 15 دقيقة، دلكي برفق وأعيدي التطبيق كل ساعتين يومياً."),
        ("هل هو خالٍ من البارابين ومقاوم للماء والتعرق؟", "نعم، 100% خالٍ من البارابين ومقاوم للماء والتعرق ومختبر درماتولوجياً."),
        ("أين صُنع واقي شمس بيزلين؟", "صُنع بواسطة Beesline International Laboratories."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100%."),
        ("ما رائحة واقي شمس بيزلين؟", "عطر بيزلين العسلي النقي اللطيف الفاخر."),
        ("هل يناسب البشرة الحساسة والفاتحة؟", "نعم، ممتاز للبشرة الحساسة، الفاتحة، والمصابة بالتصبغات والكلف."),
        ("هل أنبوب 60 مل مناسب للحقيبة والسفر؟", "نعم، أنبوب أنيق مدمج مثالي للحقيبة والسفر والشاطئ."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الضوء الشديد."),
        ("هل بيزلين الماركة الأولى طبياً في الوقاية الشمسية؟", "نعم، Beesline الماركة الأكثر شهرة وثقة في الوقاية من الشمس."),
        ("كم مرة يومياً؟", "يومياً قبل التعرض للشمس وإعادة التطبيق كل ساعتين."),
        ("هل يترك أثراً دهنياً أو لمعاناً؟", "لا، يمتص فورياً تاركاً مسبراً مات خالياً من اللمعان والدهنية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في الوقاية من التجاعيد والكلف؟", "نعم، يمنع شيخوخة البشرة الناتجة عن الشمس والكلف والتصبغات."),
        ("هل يسبب انسداد المسام؟", "لا، تركيبة غير مسببة لانسداد المسام (Non-Comedogenic)."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال والأطفال؟", "نعم، ممتاز للنساء والرجال والأطفال من سن 3 سنوات."),
        ("هل يصلح كقاعدة تحت المكياج؟", "نعم، قاعدة ممتازة للمكياج بفضل امتصاصه السريع وملمسه المات."),
        ("هل يناسب الصيف والشتاء؟", "نعم، حماية شمسية أساسية ممتازة لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج حماية طبي فاخر وأساسي لكل روتين شمس."),
        ("هل يعيد المظهر الناعم السلس للوجه؟", "نعم، يجعل الوجه محمياً وفي غاية النعومة والنقاء."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Facial Sunscreen SPF 50+ - 60ml</strong> is the world's most dermatologist-recommended authentic luxury medical broad-spectrum facial sunscreen from Beesline designed to shield sensitive facial skin against sunburn, UVA/UVB photo-damage, hyperpigmentation, and premature aging with a matte non-greasy finish. Built upon pure Beeswax, Sesame Oil, antioxidant vitamins (Vitamin C & E), and physical/mineral broad-spectrum UV filters.</p>
<p>Beesline Facial Sunscreen blocks over 98% of harmful UV rays, repairs skin barriers, and prevents dark spots and melasma, leaving your facial skin touchably silky soft, spotlessly clean, hydrated, and fully sun-protected from first application.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Ultra-High SPF 50+ Broad-Spectrum Protection (UVA/UVB):</strong> Blocks 98%+ of harmful sun rays.</li>
  <li><strong>Natural Beeswax & Antioxidant Protection:</strong> Prevents photo-aging, dark spots, and melasma.</li>
  <li><strong>Matte Non-Greasy Finish with Zero White Cast:</strong> Absorbs instantly without staining or shine.</li>
  <li><strong>Superior Hydration & Nourishment for Sensitive Face:</strong> Maintains skin elasticity during sun exposure.</li>
  <li><strong>100% Paraben-Free Water & Sweat Resistant Formula:</strong> Clinically tested for sensitive skin.</li>
  <li><strong>Compact 60ml Travel Tube:</strong> Ideal size for handbag, beach travel, and continuous re-application.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a generous amount of Beesline sunscreen onto clean face and neck 15-20 minutes before sun exposure.</li>
  <li><strong>Step 2:</strong> Massage gently in smooth circular motions until absorbed (re-apply every 2 hours & post-swimming/towel drying).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Beeswax & Vitamins C/E:</strong> Form a protective shield shielding skin against oxidative stress and UV damage.</li>
  <li><strong>Broad-Spectrum UV Filters:</strong> Block UVA rays causing wrinkles and UVB rays causing sunburns.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and neck skin application.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from direct sunlight.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Beesline Facial Sunscreen SPF 50+ 60ml for high-level facial broad-spectrum sun protection.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline Laboratories</td></tr>
  <tr><th>Category</th><td>Sun Care & Skincare / Beesline Sunscreens SPF50+ 60ml</td></tr>
  <tr><th>Product Type</th><td>Broad-Spectrum SPF 50+ Beeswax Medical Facial Sunscreen (60ml)</td></tr>
  <tr><th>Volume/Weight</th><td>60 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Specifically Sensitive, Fair & Hyperpigmented Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 100% sun-protected, matte & non-greasy face with zero white cast</td></tr>
  <tr><th>Texture</th><td>Ultra-lightweight fast-absorbing smooth cream</td></tr>
  <tr><th>Fragrance</th><td>Luxurious clean honey beeswax scent</td></tr>
  <tr><th>Active Ingredients</th><td>Beeswax, Vitamin C & E, Mineral & Physical Broad-Spectrum UV Filters</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline International Laboratories</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 3+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Beeswax Physical UV Shielding & Broad-Spectrum Photoprotection</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Facial Sunscreen SPF 50+ resolves sunburns, melasma development, sun tanning, and UV-induced photo-aging.</p>

<h3>Why choose Beesline Facial Sunscreen SPF 50+?</h3>
<p>Beeswax forms a water-resistant film anchoring broad-spectrum UVA/UVB filters ensuring continuous SPF 50+ protection.</p>"""

    en_faqs = [
        ("What is Beesline Facial Sunscreen SPF 50+ - 60ml?", "It is a medical broad-spectrum SPF 50+ facial sunscreen from Beesline with Beeswax and Antioxidants (60ml)."),
        ("What are the benefits of Beeswax and broad-spectrum SPF 50+ protection?", "Block 98%+ of harmful UVA/UVB rays, prevent melasma and dark spots, and hydrate facial skin with a matte finish."),
        ("Does it protect against sunburns and dark spots with zero white cast?", "Yes, clinically proven to deliver complete SPF 50+ protection with instant absorption and zero white cast."),
        ("What volume is contained in this tube?", "60ml compact travel tube."),
        ("How do I use it correctly?", "Apply generously 15 minutes before sun exposure, massage gently and re-apply every 2 hours."),
        ("Is it paraben-free and water/sweat resistant?", "Yes, 100% paraben-free, water-resistant, sweat-resistant, and dermatologically tested."),
        ("Where is Beesline Sunscreen manufactured?", "By Beesline International Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original."),
        ("What scent does Beesline Sunscreen have?", "Luxurious fresh clean honey beeswax fragrance."),
        ("Is it suitable for sensitive and fair facial skin?", "Yes, excellent for sensitive, fair, and hyperpigmentation-prone facial skin."),
        ("Is the 60ml tube travel friendly?", "Yes, sleek compact tube ideal for handbag, travel, and beach use."),
        ("How should I store it?", "In a cool, dry place away from direct light."),
        ("Is Beesline a trusted sun care brand?", "Yes, Beesline is a premier globally trusted sun protection brand."),
        ("How many times daily?", "Daily before sun exposure and re-applied every 2 hours."),
        ("Does it leave a greasy shine or white film?", "No, absorbs instantly leaving a clean matte finish with zero white film."),
        ("Is the tube recyclable?", "Yes."),
        ("Does it help prevent wrinkles and melasma?", "Yes, prevents photo-aging, UV wrinkles, melasma, and hyperpigmentation."),
        ("Does it clog pores?", "No, oil-free non-comedogenic formula."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men, women, and kids?", "Yes, safe and suitable for everyone aged 3+."),
        ("Does it serve as a good makeup base?", "Yes, lightweight matte makeup base due to rapid absorption."),
        ("Is it good for all seasons?", "Yes, essential daily sun protection for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, a premier medical essential for sun protection routines."),
        ("Does it restore smooth protected skin appearance?", "Yes, gives facial skin a healthy smooth protected look."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2109",
        "sku": "EK-2109",
        "gtin": "5281018006047",
        "brand": "Beesline",
        "ar": {
            "title": "واقي شمسي للوجه بعامل حماية من الشمس بدرجة 50+من بيزلين 60مل",
            "meta_title": "واقي شمس بيزلين للوجه SPF 50+ 60مل | إكليل أبها",
            "meta_description": "اشتري واقي شمسي للوجه بعامل حماية 50+ من بيزلين (60 مل). كريم واقي شمس واسع الطيف بشمع العسل لمنع التصبغات والحروق. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["بيزلين", "واقي_شمس_بيزلين", "واقي_شمس_للوجه", "بيزلين_spf50", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Facial Sunscreen SPF 50+ - 60ml",
            "meta_title": "Beesline Facial Sunscreen SPF 50+ 60ml | Ekleel Abha",
            "meta_description": "Buy original Beesline Facial Sunscreen SPF 50+ (60ml). Broad-spectrum beeswax facial sun protection cream with zero white cast. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["beesline", "beesline_sunscreen", "facial_sunscreen_spf50", "sun_protection", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 77 builders complete")
