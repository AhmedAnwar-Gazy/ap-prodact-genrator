import json, os

def create_product_2033():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>مناديل ازالة المكياج للوجه والعين والشفاه من كيوفي 25 منديل (QV Face Cleansing Wipes for Face, Eyes, and Lips - 25 Wipes)</strong> مناديل التنظيف وإزالة المكياج الطبية الفاخرة اللطيفة للغاية من كيو في الأسترالية المصممة خصيصاً لإزالة جميع أنواع المكياج (بما فيه المسكرة المقاومة للماء) والشوائب من الوجه والعينين والشفاه دون أي تهيج أو جفاف. ترتكز هذه المناديل الأصيلة (QV Face Wipes 25 Pack) على الجليسرين المرطب، مادة السكوالان الحمائية، والتركيبة المائية الخالية 100% من العطور، الكحول، والصابون.</p>
<p>تعمل مناديل كيوفي على تنظيف مسام البشرة بلطف، إذابة أحمر الشفاه ومكياج العيون دون الحاجة للفرك القاسي، وتغذية الجلد وحفظ رطوبته الطبيعية، لتترك بشرتك ناعمة كالحرير، ناصعة النظافة، مهدأة، ومحمية من الحساسية والجفاف من استخدام المنديل الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>إزالة سريعة ولطيفة للمكياج المقاوم للماء:</strong> تنظف الوجه والعينين والشفاه بسلاسة.</li>
  <li><strong>خالية 100% من العطور، الكحول، الصابون، واللانولين:</strong> آمنة ولطيفة جداً على البشرة شديدة الحساسية.</li>
  <li><strong>ترطيب وتغذية بمركب السكوالان والجليسرين:</strong> تمنع شد البشرة وجفافها بعد المسح.</li>
  <li><strong>مختبرة أوفثالمولوجياً ودرماتولوجياً:</strong> آمنة لمحيط العينين ولمستخدمي العدسات اللاصقة.</li>
  <li><strong>عبوة مدمجة معاد إغلاقها تحتوي على 25 منديل ناعم:</strong> تضمن بقاء المناديل رطبة وطازجة.</li>
  <li><strong>مثالية للتنظيف السريع أثناء السفر والتنقل:</strong> لا تتطلب الشطف بالماء.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> افتحي الغطاء اللاصق واسحبي منديل واحد من عبوة كيوفي.</li>
  <li><strong>الخطوة الثانية:</strong> امسحي برفق على الوجه والعينين والشفاه لإزالة المكياج والشوائب دون فرك شديد.</li>
  <li><strong>الخطوة الثالثة:</strong> أعيدي إغلاق العبوة جيداً لمنع جفاف المناديل (يُستعمل عند الحاجة ولإزالة المكياج المسائي).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مادة السكوالان الطبيعية (Squalene) والجليسرين:</strong> تحافظان على ترطيب الجلد وتقويان غلافه الوقائي.</li>
  <li><strong>نسيج المناديل الفائق النعومة والمحاليل اللطيفة:</strong> يلتقط الشوائب والزيوت دون تسبيب احمرار للبشرة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والعينين والشفاه.</li>
  <li>تجنبي إدخال المنديل داخل مقلة العين المباشرة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف وتأكدي من إغلاق العبوة.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تبحث عن مناديل كيوفي لإزالة المكياج 25 منديل لتنظيف الوجه والعينين والشفاه بأعلى لطف طبي.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كيو في (QV Face)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / مناديل إزالة المكياج وتنظيف الوجه من كيو في 25 Wipes</td></tr>
  <tr><th>نوع المنتج</th><td>مناديل طبية مرطبة لإزالة مكياج الوجه والعين والشفاه خالية من العطور والكحول (25 منديل)</td></tr>
  <tr><th>الحجم/الوزن</th><td>25 منديل رطب</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (خصيصاً البشرة شديدة الحساسية ومحيط العينين)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناصع النظافة، خالي من المكياج، مرطب ومهدأ بدون احمرار</td></tr>
  <tr><th>الملمس</th><td>مناديل قماشية فائقة النعومة مرطبة بسائل شفاف</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>سكوالان طبيعي، جليسرين مرطب، محاليل خالية من الصابون والكحول</td></tr>
  <tr><th>بلد المنشأ</th><td>أستراليا (Australia)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون والمراهقون (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد السكوالان والتركيبة الخالية من الكحول في مناديل كيوفي (QV Face Wipes)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج مناديل كيوفي مشكلة جفاف البشرة واحمرار العينين والشفاه الناتج عن مناديل إزالة المكياج المعطرة بالحك والكحول.</p>

<h3>لماذا تنجح تركيبة QV Face Cleansing Wipes؟</h3>
<p>لأن دمج نسيج المناديل الفائق النعومة مع السكوالان الطبيعي يذيب صبغات المكياج المقاوم للماء دون تجريد الزيوت الطبيعية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>المسح بالضغط الخفيف على مكياج العينين لثوانٍ:</strong> يسهل إذابة المسكرة دون شد الجفن.<br>
2. <strong>إحكام إغلاق العبوة بعد كل استخدام:</strong> يحفظ رطوبة المناديل حتى المنديل الأخير.<br>
3. <strong>التكميل بغسول أو كريم كيو في الوجه:</strong> يدعم النضارة والترطيب الداخلي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مناديل إزالة المكياج تسبب دائماً تجاعيد حول العينين."<br>
<strong>الحقيقة:</strong> مناديل كيوفي مدعمة بالسكوالان ونموذج مائي ينزلق بسلاسة مانعاً شد وقسوة الجلد.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تستقطب المنظفات غير الأيونية جزيئات المكياج الزيتية داخل ميكروسفيرات مائية ينظف بها الوجه بلمسة ناعمة.</p>"""

    faqs = [
        ("ما هي مناديل ازالة المكياج للوجه والعين والشفاه من كيوفي 25 منديل؟", "هي مناديل طبية فاخرة خالية من العطور والكحول من كيو في الأسترالية لإزالة المكياج المقاوم للماء وتنظيف الوجه والعين والشفاه (25 منديل)."),
        ("ما هي فوائد السكوالان والتركيبة الخالية من الكحول والصابون؟", "تزيل المكياج بسلاسة دون فرك، تحافظ على ترطيب الجلد، وتمنع الاحمرار والتهيج."),
        ("هل تزيل المسكرة المقاومة للماء ومكياج الشفاه دون جفاف؟", "نعم، مثبت سريرياً في إزالة المكياج المقاوم للماء ولطفها على الشفاه والعينين."),
        ("ما عدد المناديل بالعبوة؟", "تأتي بعبوة أنيقة معاد إغلاقها تحتوي على 25 منديل رطب."),
        ("كيف تُستخدم بالشكل الصحيح؟", "اسحبي منديل، امسحي الوجه والعينين والشفاه برفق وأغلقي الشريط اللاصق جيداً بعد الاستخدام."),
        ("هل هي خالية من العطور والكحول والصابون؟", "نعم، 100% خالية من العطور، الكحول، الصابون واللانولين ومختبرة أوفثالمولوجياً."),
        ("أين صُنعت مناديل كيوفي؟", "صُنع في أستراليا بواسطة Ego Pharmaceuticals Australia."),
        ("كيف أتأكد من أصالتها لدى إكليل أبها؟", "جميع منتجات كيوفي لدى إكليل أبها أصلية 100%."),
        ("هل هي آمنة لمستخدمي العدسات اللاصقة؟", "نعم، آمنة ومختبرة لمحيط العينين ولمستخدمي العدسات اللاصقة."),
        ("هل تترك البشرة ناعمة ومرطبة دون شد؟", "نعم، تترك البشرة ناعمة ومرطبة ومستقرة بدون أي شد أو جفاف."),
        ("هل عبوة 25 منديل مناسبة للحقيبة والسفر؟", "نعم، عبوة أنيقة مدمجة مثالية لحقيبة اليد والسفر والتنقل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف وتأكدي من إحكام إغلاق الشريط اللاصق."),
        ("هل كيوفي العلامة الأولى أسترالياً في العناية بالوجه؟", "نعم، QV Face العلامة رقم 1 الموصى بها طبياً في أستراليا."),
        ("كم مرة يومياً؟", "عند الحاجة لإزالة المكياج وتنظيف الوجه."),
        ("هل تتطلب الشطف بالماء بعد المسح؟", "لا تتطلب الشطف بالماء، لكن يمكن غسل الوجه بالغسول عند الرغبة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل تناسب البشرة الحساسة جداً؟", "نعم، مصممة خصيصاً للبشرة شديدة الحساسية والمتهيجة."),
        ("هل تحمي من ظهور خطوط التجفيف حول العين؟", "نعم، تمنع الجفاف والشد المحيط بالعينين بفضل السكوالان."),
        ("هل تتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، تتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل تناسب النساء والرجال للتنظيف السريع؟", "نعم، ممتازة لإزالة المكياج وللتنظيف السريع اليومي للجميع."),
        ("هل تجف المناديل داخل العبوة؟", "لا تجف إذا تم إعادة إغلاق العبوة باللاصق بشكل محكم بعد كل استخدام."),
        ("هل تصلح هدية ممتازة لحقيبة التجميل؟", "نعم، إضافة راقية وأساسية لكل حقيبة مكياج."),
        ("هل تمنح إزالة سريعة دون بقايا زهمية؟", "نعم، تزيل المكياج بالكامل دون ترك طبقة دهنية ثقيلة."),
        ("هل تتوفر منتجات QV Face الأخرى؟", "نعم، تتوفر عائلة QV Face كاملة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>QV Face Cleansing Wipes for Face, Eyes, and Lips - 25 Wipes</strong> are authentic luxury medical cleansing and makeup removal wipes from QV Australia designed to gently remove all makeup types (including waterproof mascara) and impurities from face, eyes, and lips without irritation or dryness. Built upon hydrating Glycerin, protective Squalene, and a 100% fragrance-free, alcohol-free, soap-free aqueous solution.</p>
<p>QV Face Wipes gently cleanse skin pores, dissolve lip lipstick and eye makeup without harsh rubbing, and nourish skin while preserving natural moisture, leaving your skin touchably silky soft, spotlessly clean, soothed, and protected from sensitivity from the very first wipe.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Fast & Gentle Waterproof Makeup Removal:</strong> Cleanses face, eye contours, and lips smoothly.</li>
  <li><strong>100% Free from Fragrance, Alcohol, Soap & Lanolin:</strong> Extremely safe and gentle on sensitive skin.</li>
  <li><strong>Hydration & Nourishment with Squalene & Glycerin:</strong> Prevents post-wipe tightness and dryness.</li>
  <li><strong>Ophthalmologically & Dermatologically Tested:</strong> Safe for eye contours and contact lens wearers.</li>
  <li><strong>Resealable Pack of 25 Soft Wipes:</strong> Ensures wipes remain moist and fresh.</li>
  <li><strong>Ideal for On-the-Go & Travel Cleansing:</strong> Requires no water rinsing.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Peel back resealable sticker and remove one wipe from the QV pack.</li>
  <li><strong>Step 2:</strong> Gently wipe across face, eye area, and lips to dissolve makeup and impurities without harsh rubbing.</li>
  <li><strong>Step 3:</strong> Reseal pack firmly to keep remaining wipes moist (use as needed & evening makeup removal).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Squalene & Hydrating Glycerin:</strong> Preserve skin moisture while reinforcing the natural lipid barrier.</li>
  <li><strong>Ultra-Soft Cloth Fabric & Mild Solution:</strong> Capture impurities and sebum without triggering skin redness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial, eye contour, and lip application.</li>
  <li>Avoid wiping directly inside the eyeball.</li>
  <li>Keep out of reach of children and store in a cool, dry place ensuring pack is sealed.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking QV Face Cleansing Wipes 25 Pack for gentle medical makeup removal on face, eyes, and lips.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>QV Face</td></tr>
  <tr><th>Category</th><td>Skincare / QV Medical Makeup Remover & Facial Wipes 25 Pack</td></tr>
  <tr><th>Product Type</th><td>Medical Fragrance-Free Alcohol-Free Face, Eye & Lip Cleansing Wipes (25 Wipes)</td></tr>
  <tr><th>Volume/Weight</th><td>25 Moist Wipes</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Specifically Sensitive Skin & Eye Contours)</td></tr>
  <tr><th>Finish</th><td>Spotlessly clean, makeup-free, hydrated & soothed skin without redness</td></tr>
  <tr><th>Texture</th><td>Ultra-soft cloth wipe moistened with clear solution</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Squalene, Hydrating Glycerin, Soap-Free Cleansers</td></tr>
  <tr><th>Country of Origin</th><td>Australia</td></tr>
  <tr><th>Manufacturer</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Squalene Solubilization & Alcohol-Free Ophthalmic Safety</h2>

<h3>What problem does this solve?</h3>
<p>QV Face Wipes resolve skin dryness, eye redness, and lip irritation caused by alcohol-laden perfumed cleansing wipes.</p>

<h3>Why choose QV Face Cleansing Wipes?</h3>
<p>Combining ultra-soft cloth fibers with natural Squalene dissolves waterproof pigments without stripping natural hydrolipids.</p>"""

    en_faqs = [
        ("What are QV Face Cleansing Wipes for Face, Eyes, and Lips - 25 Wipes?", "They are medical fragrance-free alcohol-free cleansing wipes from QV Australia for waterproof makeup removal on face, eyes, and lips (25 wipes)."),
        ("What are the benefits of Squalene and alcohol-free formula?", "They remove makeup smoothly without rubbing, maintain skin hydration, and prevent redness."),
        ("Do they remove waterproof mascara and lip makeup without dryness?", "Yes, clinically proven to remove waterproof makeup while remaining gentle on eyes and lips."),
        ("How many wipes are in this pack?", "Resealable pack of 25 moist wipes."),
        ("How do I use them correctly?", "Remove wipe, sweep gently over face, eyes, and lips, and seal sticker firmly after use."),
        ("Are they fragrance-free, alcohol-free, and soap-free?", "Yes, 100% free from fragrance, alcohol, soap, and lanolin."),
        ("Where are QV Face Wipes manufactured?", "In Australia by Ego Pharmaceuticals Australia."),
        ("How do I verify authenticity at Ekleel Abha?", "All QV products at Ekleel Abha are 100% original."),
        ("Are they safe for contact lens wearers?", "Yes, ophthalmologically tested safe for sensitive eye contours and contact lens wearers."),
        ("Do they leave skin soft and hydrated without tightness?", "Yes, leave skin soft, hydrated, and calm without tightness or dryness."),
        ("Is the 25 wipe pack handbag and travel friendly?", "Yes, sleek compact pack ideal for handbag and travel."),
        ("How should I store them?", "In a cool, dry place ensuring the adhesive seal is closed."),
        ("Is QV Face Australia's #1 medical facial brand?", "Yes, QV Face is the #1 medically recommended facial brand in Australia."),
        ("How many times daily?", "Whenever makeup removal or quick facial cleansing is needed."),
        ("Do they require water rinsing afterwards?", "No water rinsing required, though face can be washed if desired."),
        ("Is the packaging recyclable?", "Yes."),
        ("Are they suitable for ultra-sensitive skin?", "Yes, specifically formulated for sensitive and reactive skin."),
        ("Do they protect against fine dryness lines around eyes?", "Yes, prevent eye contour dryness and tightness thanks to Squalene."),
        ("Are they available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Are they suitable for men and women?", "Yes, great for makeup removal and quick cleansing for everyone."),
        ("Do wipes dry out inside the pack?", "Will not dry out if resealable sticker is pressed firmly closed after each use."),
        ("Are they a nice addition to beauty bags?", "Yes, an elegant essential addition to every cosmetics bag."),
        ("Do they provide quick cleansing without greasy residue?", "Yes, remove makeup completely without leaving a heavy greasy residue."),
        ("Are other QV Face products available?", "Yes, the full QV Face product line is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2033",
        "sku": "EK-2033",
        "gtin": "9314839015397",
        "brand": "QV",
        "ar": {
            "title": "مناديل ازالة المكياج للوجه والعين والشفاه  من كيوفي 25 منديل",
            "meta_title": "مناديل كيوفي لإزالة المكياج 25 منديل | إكليل أبها",
            "meta_description": "اشتري مناديل إزالة المكياج للوجه والعين والشفاه من كيو في (25 منديل). مناديل طبية خالية من العطور والكحول بالسكوالان والجليسرين. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كيوفي", "مناديل_إزالة_المكياج_كيوفي", "مناديل_الوجه_كيوفي", "تنظيف_الوجه", "إكليل_أبها"]
        },
        "en": {
            "title": "QV Face Cleansing Wipes for Face, Eyes, and Lips - 25 Wipes",
            "meta_title": "QV Face Cleansing Wipes 25 Wipes | Ekleel Abha",
            "meta_description": "Buy original QV Face Cleansing Wipes for Face, Eyes, and Lips (25 Wipes). Australian fragrance-free alcohol-free makeup remover wipes. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["qv", "qv_face_wipes", "makeup_remover_wipes", "cleansing_wipes", "ekleel_abha"]
        }
    }


def _make_cantu_b64(pid, gtin, ar_name, en_name, type_ar, type_en, weight_g, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> مستحضر العناية وتصفيف وترميم الشعر الفاخر الأصيل من كانتو العالمية المصمم خصيصاً لتغذية، تنعيم، وتقوية الخصلات والتجعدات الكيرلي الجافة والتالفة. يرتكز هذا المستحضر الأصيل ({en_name}) على زبدة الشيا الصافية 100%، الزيوت النباتية المغذية، والمركبات المرممة لألياف الشعر.</p>
<p>يعمل مستحضر كانتو للشعر على ترويض الهيشات، إصلاح التلف والتقصف، وتغذية الشعر من الجذور حتى الأطراف، ليترك شعرك أو شعر طفلك مصففاً بأناقة، ناعماً كالحرير، ومفعماً بالصحة واللمعان البراق طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترميم وتغذية مكثفة بزبدة الشيا الصافية 100%:</strong> يعالج الجفاف والتلف ويصلح ألياف الشعر.</li>
  <li><strong>تحديد وتثبيت مرن للشعر والتسريحات:</strong> يبرز الكيرلي دون تيبس أو قشور بيضاء.</li>
  <li><strong>السيطرة الكاملة على الهيشات والتطاير:</strong> يحمي الشعر من الرطوبة والطقس.</li>
  <li><strong>تركيبة خالية من الكبريتات، السيليكون والبارابين:</strong> آمنة ونظيفة للاستخدام اليومي.</li>
  <li><strong>يمنح الشعر لمعاناً طبيعياً براقاً:</strong> يغلف الخصلات ببريق ناعم صحي.</li>
  <li><strong>عبوة سعة {weight_g} جم/مل:</strong> حجم ممتاز للاستخدام العائلي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> وزعي كمية مناسبة من مستحضر كانتو على شعر رطب أو جاف.</li>
  <li><strong>الخطوة الثانية:</strong> صففي الشعر بالأصابع أو المشط وتدليك الأطراف والفروة لتقوية وتصفيف الشعر (يُستعمل عند التصفيف).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زبدة الشيا الصافية 100% والزيوت الطبيعية:</strong> تغذيان ساق الشعر وتمنحان القوة والنعومة الفائقة.</li>
  <li><strong>المركبات النباتية المرطبة:</strong> تحفظ رطوبة الشعر الداخلية وتمنع الجفاف والتقصف.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على الشعر فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لترميم، تنعيم، وتصفيف الشعر والتسريحة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كانتو (Cantu)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / مستحضرات تصفيف وترميم الشعر من كانتو {weight_g}g</td></tr>
  <tr><th>نوع المنتج</th><td>مستحضر تصفيف وترميم وتنعيم الشعر بـ زبدة الشيا ({type_ar}) {weight_g}g</td></tr>
  <tr><th>الحجم/الوزن</th><td>{weight_g} جم/مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (الكيرلي، المجعد، التالف، والأطفال)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر قوي، ناعم كالحرير، محدد وخالٍ من التكسر والهيشان</td></tr>
  <tr><th>الملمس</th><td>كريم/زيت/شامبو ناعم غني ذو ثبات مرن</td></tr>
  <tr><th>العطر</th><td>عطر جوز الهند وجوز الشيا الاستوائي الفواح</td></tr>
  <tr><th>المكونات النشطة</th><td>زبدة الشيا الصافية، الأفوكادو، بذور الكتان، الزيوت المغذية</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>PDC Brands USA</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (الأطفال، النساء والرجال)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد زبدة الشيا والزيوت المغذية في كانتو (Cantu Repair)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مستحضر كانتو مشكلة تكسر الشعر، هيشان الخصلات، التلف الناتج عن الصبغات والحرارة، والجفاف الشديد.</p>

<h3>لماذا تنجح تركيبة Cantu Repair?</h3>
<p>لأن دمج زبدة الشيا الصافية مع الزيوت الطبيعية يعزز مرونة الكيراتين ويحمي ألياف الشعر من الإجهاد اليومي.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق المباشر على الأطراف والجذور:</strong> يمنح القوة والتغذية المتكاملة.<br>
2. <strong>التصفيف اللطيف بالأصابع:</strong> يحافظ على استقامة وجمال الخصلات.<br>
3. <strong>الاستمرار في الروتين اليومي:</strong> يعيد بناء الشعر التالف بفاعلية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مستحضرات ترميم الشعر تجعل الخصلات قاسية."<br>
<strong>الحقيقة:</strong> مستحضرات كانتو تمنح القوة المرنة والنعومة دون تيبس أو قسوة في الشعر.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تغلف الليبيدات ساق الشعر مانعة تكسر الروابط الهيدروجينية أثناء التمشيط والتصفيف.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو مستحضر ترميم وتنعيم وتصفيف الشعر من كانتو بحجم {weight_g} جم/مل."),
        ("ما هي فوائد زبدة الشيا والزيوت للشعر؟", "تقويان ساق الشعر، تمنعان التكسر والتقصف، وتمنحان نعومة ولمعاناً براقاً."),
        ("هل يرمم الشعر ويمنع التكسر والهيشان؟", "نعم، مثبت سريرياً في تقوية ألياف الشعر والسيطرة على الهيشان والتكسر."),
        (f"ما وزن العبوة؟", f"{weight_g} جم/مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي على شعر رطب أو جاف، دلكي الأطراف وصففي بالأصابع أو المشط."),
        ("هل هو خالٍ من الكبريتات والسيليكون والبارابين؟", "نعم، 100% خالٍ من الكبريتات، السيليكون، والبارابين."),
        (f"أين صُنع مستحضر كانتو؟", "صُنع في الولايات المتحدة بواسطة PDC Brands USA."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كانتو لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", "عطر جوز الهند وجوز الشيا الاستوائي الفواح."),
        ("هل يناسب جميع أنواع الشعر؟", "نعم، ممتاز للشعر الكيرلي، المجعد، التالف والجاف."),
        (f"هل العبوة {weight_g} جم/مل تكفي لفترة جيدة؟", "نعم، تكفي لعدة أسابيع من الاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كانتو العلامة الأولى عالمياً في تصفيف وترميم الشعر؟", "نعم، Cantu العلامة العالمية الأكثر شهرة ومبيعا."),
        ("كم مرة يومياً؟", "عند تصفيف الشعر."),
        ("هل يمنح الشعر لمعاناً ونعومة حريرية؟", "نعم، يمنح الشعر لمعاناً طبيعياً ونعومة حريرية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في تحفيز نمو الشعر القوي؟", "نعم، يقوي البصيلات والأطراف لتحفيز النمو الصحي."),
        ("هل يترك ملمساً لزجاً؟", "ينفذ بمرونة دون ترك لزوجة أو تراكمات ثقيلة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء والأطفال؟", "نعم، ممتاز للنساء والرجال والأطفال."),
        ("هل يحمي الشعر من الحرارة والطقس؟", "نعم، يغلف الشعر ويحميه من المؤثرات الخارجية."),
        ("هل يصلح هدية ممتازة لمحب العناية بالشعر؟", "نعم، منتج أنيق وعملي جداً."),
        ("هل يعيد المظهر الصحي للشعر التالف؟", "نعم، يعيد الحيوية والقوة للشعر المجهد."),
        ("هل يسهل التصفيف اليومي؟", "نعم، يجعل التمشيط والتصفيف سهلاً وسلساً."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic luxury hair repair, moisturizing, and styling product from Cantu designed to nourish, smooth, and strengthen dry damaged hair strands and curls. Built upon 100% Pure Shea Butter, nourishing plant oils, and hair fiber repairing agents.</p>
<p>Cantu Hair Product tames hair flyaways, repairs damage and split ends, and nourishes hair from root to tip, leaving your hair or your child's hair beautifully styled, silky soft, and radiant all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intensive Hair Repair with 100% Pure Shea Butter:</strong> Treats dryness and damage while repairing hair fibers.</li>
  <li><strong>Flexible Hold & Styling Definition:</strong> Highlights curls without stiffness or white flakes.</li>
  <li><strong>Complete Frizz & Flyaway Control:</strong> Shields hair against humidity and adverse weather.</li>
  <li><strong>Sulfate-Free, Silicone-Free & Paraben-Free Formula:</strong> Safe clean formula for daily hair care routines.</li>
  <li><strong>Imparts Natural Luminous Shine:</strong> Coats hair strands in a healthy soft luster.</li>
  <li><strong>Generous {weight_g}g/ml Size:</strong> Excellent volume for daily styling and continuous family care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of Cantu product onto damp or dry hair.</li>
  <li><strong>Step 2:</strong> Style with fingers or comb, massaging roots and ends for reinforcement (use whenever styling).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>100% Pure Shea Butter & Natural Oils:</strong> Nourish the hair shaft imparting structural strength and extreme softness.</li>
  <li><strong>Moisturizing Botanical Agents:</strong> Lock in internal hair moisture preventing dryness and split ends.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hair application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for repairing, moisturizing, and styling hair.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Cantu</td></tr>
  <tr><th>Category</th><td>Hair Care / Cantu Hair Repair & Moisturizing Products {weight_g}g</td></tr>
  <tr><th>Product Type</th><td>Hair Repair & Moisturizing Product with Shea Butter ({type_en}) {weight_g}g</td></tr>
  <tr><th>Volume/Weight</th><td>{weight_g} g/ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Curly, Coily, Damaged, Dry & Kids Hair)</td></tr>
  <tr><th>Finish</th><td>Strong hair, silky smooth, defined & breakage-free styled hair</td></tr>
  <tr><th>Texture</th><td>Rich smooth cream/oil/shampoo with flexible hold</td></tr>
  <tr><th>Fragrance</th><td>Invigorating tropical coconut and shea butter scent</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Shea Butter, Avocado, Flaxseed, Nourishing Oils</td></tr>
  <tr><th>Country of Origin</th><td>USA</td></tr>
  <tr><th>Manufacturer</th><td>PDC Brands USA</td></tr>
  <tr><th>Age Group</th><td>All Ages (Kids, Men & Women)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Shea Butter & Plant Oil Cuticle Reinforcement</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves hair breakage, frizz, chemical damage, and severe hair dryness.</p>

<h3>Why choose Cantu Repair Formula?</h3>
<p>Combining 100% Pure Shea Butter with natural plant oils enhances keratin bond elasticity protecting fibers against friction.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a hair repairing, moisturizing, and styling product from Cantu ({weight_g}g/ml)."),
        ("What are the benefits of shea butter and oils for hair?", "Reinforce the hair shaft, prevent breakage, and deliver silky softness and shine."),
        ("Does it repair hair and control breakage and frizz?", "Yes, clinically proven to reinforce hair fibers and control breakage and frizz."),
        (f"What weight/volume is contained in this container?", f"{weight_g}g/ml."),
        ("How do I use it correctly?", "Apply to damp or dry hair, massage ends, and style with fingers or comb."),
        ("Is it sulfate-free, silicone-free, and paraben-free?", "Yes, 100% free from sulfates, silicones, and parabens."),
        ("Where is Cantu Hair Product manufactured?", "In the USA by PDC Brands USA."),
        ("How do I verify authenticity at Ekleel Abha?", "All Cantu products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", "Invigorating tropical coconut and shea butter fragrance."),
        ("Is it suitable for all hair types?", "Yes, excellent for curly, coily, damaged, and dry hair."),
        (f"Does the {weight_g}g/ml container last long?", "Yes, lasts weeks of regular daily styling."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Cantu a globally leading hair brand?", "Yes, Cantu is a world-famous brand in hair care."),
        ("How many times daily?", "Whenever styling hair."),
        ("Does it impart shine and silky softness?", "Yes, gives hair natural shine and silky softness."),
        ("Is the container recyclable?", "Yes."),
        ("Does it help promote strong hair growth?", "Yes, reinforces roots and ends promoting healthy growth."),
        ("Does it leave a sticky residue?", "Penetrates flexibly without sticky residue or heavy buildup."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men, women, and kids?", "Yes, suitable for the whole family."),
        ("Does it shield hair from weather and heat?", "Yes, coats hair guarding against environmental factors."),
        ("Is it a great gift for hair care lovers?", "Yes, elegant and practical gift for hair care."),
        ("Does it restore healthy appearance to damaged hair?", "Yes, restores vitality and strength to stressed hair."),
        ("Does it make daily styling easy?", "Yes, makes combing and styling smooth and effortless."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Cantu",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. مستحضر تصفيف وترميم وتنعيم الشعر بزبدة الشيا من كانتو. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Cantu shea butter hair repair and moisturizing product. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2034():
    return _make_cantu_b64(
        pid=2034, gtin="817513019890",
        ar_name="كريم إصلاح مرطب بالافوكادو من كانتو 340جم",
        en_name="Cantu moisturizing repair cream with avocado 340g",
        type_ar="كريم إلاح مرطب بالأفوكادو وزبدة الشيا", type_en="Avocado Moisturizing Repair Cream", weight_g=340,
        feature_ar="كريم ترميم وإصلاح مركز بالأفوكادو وزبدة الشيا للشعر التالف 340 جم", feature_en="intensive avocado and shea butter moisturizing repair cream 340g",
        tags_ar=["كانتو", "كريم_إصلاح_كانتو", "أفوكادو_كانتو", "ترميم_الشعر", "إكليل_أبها"],
        tags_en=["cantu", "cantu_avocado", "moisturizing_repair_cream", "avocado_repair_cream", "ekleel_abha"]
    )


def create_product_2035():
    return _make_cantu_b64(
        pid=2035, gtin="856017000126",
        ar_name="كريم مصفف وملمع الشعر بربدة الشيا من كانتو 453جم",
        en_name="Cantu Shea Butter Hair Polishing Cream 453 Gm",
        type_ar="كريم مصفف وملمع للشعر (Hair Polishing Cream)", type_en="Hair Polishing Cream", weight_g=453,
        feature_ar="كريم تلميع وتصفيف الشعر ضخم بزبدة الشيا الصافية 453 جم", feature_en="jumbo hair polishing and styling cream with pure shea butter 453g",
        tags_ar=["كانتو", "تلميع_الشعر_كانتو", "كريم_مصفف_453جم", "زبدة_الشيا_كانتو", "إكليل_أبها"],
        tags_en=["cantu", "hair_polishing_cream", "cantu_polishing_cream", "cantu_453g", "ekleel_abha"]
    )


def create_product_2036():
    return _make_cantu_b64(
        pid=2036, gtin="817513015465",
        ar_name="شامبو لشعر الاطفال من كانتو 237مل",
        en_name="Cantu Kids Shampoo 237ml",
        type_ar="شامبو لطيف خالي من الدموع لشعر الأطفال", type_en="Tear-Free Kids Shampoo", weight_g=237,
        feature_ar="شامبو لطيف برغوة ناعمة بزبدة الشيا والعسل لشعر الأطفال 237 مل", feature_en="gentle tear-free kids shampoo with shea butter and honey 237ml",
        tags_ar=["كانتو", "شامبو_كانتو_اطفال", "شامبو_شعر_الاطفال", "كانتو_كيدز", "إكليل_أبها"],
        tags_en=["cantu", "cantu_kids_shampoo", "kids_shampoo", "cantu_kids", "ekleel_abha"]
    )


def create_product_2037():
    return _make_cantu_b64(
        pid=2037, gtin="810006940749",
        ar_name="زبت بذور الكتان والزيتون واللوز والافوكادو والخروع للشعر من كانتو 118مل",
        en_name="Cantu Flaxseed, Olive, Almond, Avocado & Castor Hair Oil - 118ml",
        type_ar="زيت التغذية الخماسي للشعر (الكتان، الزيتون، اللوز، الأفوكادو، الخروع)", type_en="5-in-1 Nourishing Multi-Oil Blend", weight_g=118,
        feature_ar="خليط الزيوت الطبيعية الخماسية لتغذية وتكثيف وتنعيم الشعر 118 مل", feature_en="5-in-1 natural botanical multi-oil blend for hair growth and shine 118ml",
        tags_ar=["كانتو", "زيت_كانتو_الخماسي", "زيت_بذور_الكتان", "تكثيف_وتغذية_الشعر", "إكليل_أبها"],
        tags_en=["cantu", "cantu_hair_oil", "flaxseed_castor_oil", "botanical_hair_oil", "ekleel_abha"]
    )


print("Loaded all 5 Batch 64 builders complete")
