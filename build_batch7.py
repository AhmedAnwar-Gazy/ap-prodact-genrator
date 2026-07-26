import json, os

def create_product_1728():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>المسحات القطنية الدائرية 80 قطعة (Round Cotton Pads - 80 Pieces)</strong> الخيار الأساسي واليومي الأكمل للعناية بالبشرة وإزالة المكياج بكل رفق وفاعلية. صُنعت هذه الأقراص من قطن طبيعي نقي 100% عالي الجودة بحواف مخيطة بدقة لمنع تفتت الألياف أو ترك أي وبر على الوجه أثناء الاستخدام.</p>
<p>تمتاز الأقراص بتركيبة ثنائية الجوانب؛ حيث يمتلك الجانب الأول ملمساً مبطناً ناعماً جداً ومثالياً لتطبيق التونر واللوشنات وإعادة ترطيب الوجه، بينما يمتلك الجانب الثاني ملمساً محككاً لطيفاً يسهل إزالة المكياج وطلاء الأظافر بمسحة واحدة دون تهييج البشرة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>قطن طبيعي 100%:</strong> أقراص قطنية ناعمة ونقية خالية من المواد الكيميائية والعطور والمبيضات القاسية.</li>
  <li><strong>تصميم ثنائي الجوانب مضلع:</strong> جانب ناعم للترطيب واللوشن، وجانب مضلع لإزالة المكياج وطلاء الأظافر.</li>
  <li><strong>حواف مضغوطة ومخيطة (Stitched Edges):</strong> تمنع تفتت القطن أو ترك وبر وألياف على الوجه أو الأنسجة.</li>
  <li><strong>امتصاص فائق واقتصادي:</strong> تمتص التونر ومزيل المكياج وتوزعه بكفاءة دون إهدار المستحضرات.</li>
  <li><strong>لطيفة على البشرة الحساسة:</strong> تناسب الاستخدام اليومي لجميع أنواع البشرة ومحيط العينين الحساس.</li>
  <li><strong>عبوة اقتصادية 80 قطعة:</strong> عبوة عملية مزودة برباط غلق حفظاً من الغبار والتلوث.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (لإزالة المكياج):</strong> ضعي كمية مناسبة من مزيل المكياج أو ماء الميسيلار على القرص القطني.</li>
  <li><strong>الخطوة الثانية (المسح اللطيف):</strong> امسحي الوجه والعينين والشفاه برفق بالجانب المضلع لإزالة المكياج والرواسب.</li>
  <li><strong>الخطوة الثالثة (لتطبيق التونر):</strong> ضعي التونر على الجانب الأملس وربتي بلطف على الوجه لترطيب وتضييق المسام.</li>
  <li><strong>الخطوة الرابعة (لإزالة طلاء الأظافر):</strong> بلي القرص بمزيل طلاء الأظافر وامسحي الأظافر بسهولة.</li>
  <li><strong>الخطوة الخامسة (التخلص الآمن):</strong> تخلصي من القرص المستعمل في سلة المهملات ولا تكرري استخدامه.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>ألياف قطنية طبيعية 100% (Pure Natural Cotton Fibers):</strong> فائقة الامتصاص والنعومة على ألياف البشرة.</li>
  <li><strong>خالية من المواد الكيميائية المبيضة:</strong> نسيج نقي وآمن خالٍ من الكلور والعطور.</li>
  <li><strong>حواف مخيطة بتقنية الحرارة (Thermal Stitched Edges):</strong> تحفظ تماسك القرص أثناء البلل والمسح.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على البشرة والأظافر فقط.</li>
  <li>يُحفظ في مكان جاف ونظيف بعيداً عن الرطوبة وأشعة الشمس.</li>
  <li>تخلصي من القرص بعد كل استخدام وضعي العبوة مغلقة برباط الحفظ.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال لتجنب الابتلاع.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن أقراص قطنية ناعمة وعالية الجودة لإزالة المكياج وتطبيق التونر.</li>
  <li>لصاحبات البشرة الحساسة الباحثات عن نسيج خالي من الوبر والمواد الكيميائية.</li>
  <li>مناسب للاستخدام اليومي ولجميع العائله.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>عام / صيدلية إكليل أبها</td></tr>
  <tr><th>الفئة</th><td>مستلزمات التجميل / الأقراص والمسحات القطنية</td></tr>
  <tr><th>نوع المنتج</th><td>أقراص قطنية دائرية ثنائية الجوانب (80 قطعة)</td></tr>
  <tr><th>الحجم/الوزن</th><td>80 قطعة قطنية</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (الوجه، العينين، الأظافر)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة نظيفة، جافة، وخالية من بقايا المكياج والوبر</td></tr>
  <tr><th>الملمس</th><td>قطني ناعم ومضلع بحواف مضغوطة</td></tr>
  <tr><th>العطر</th><td>خالي من العطور (عديم الرائحة)</td></tr>
  <tr><th>المكونات النشطة</th><td>قطن طبيعي نقي 100%</td></tr>
  <tr><th>بلد المنشأ</th><td>تركيا / الصين</td></tr>
  <tr><th>الشركة المصنعة</th><td>Cotton Products Care</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لاستخدام الأقراص القطنية والعناية اليومية بالبشرة</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تحل المسحات القطنية الدائرية مشكلة تفتت القطن التقليدي وترك الوبر على الوجه أو رموش العينين أثناء إزالة المكياج، وتوفر أداة تطبيق متجانسة للمستحضرات السائلة تمنع إهدار التونر والميسيلار.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>القطن العادي غير المضغوط يفتقر للحواف المخيطة، مما يجعله يتفكك فور التلامس مع السوائل، ويترك أليافاً قطنية تعوق التنظيف وتسبب تهيج محيط العينين والمسام.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام الجانب المضلع للمكياج:</strong> الجانب المضلع يمسك بالرسوب والمكياج بسهولة دون مسح تكراري مجهد.<br>
2. <strong>استخدام الجانب الأملس للتونر:</strong> الجانب الأملس يوزع السائل بالتساوي دون امتصاص زائد.<br>
3. <strong>الربت الخفيف:</strong> لا تفركي عينيكِ بقوة أثناء إزالة المسكارة.<br>
4. <strong>إغلاق العبوة:</strong> اسحبي رباط العبوة دائماً لحماية القطن من الغبار والجراثيم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "جميع الأقراص القطنية متشابهة ولا تختلف الجودة."<br>
<strong>الحقيقة:</strong> الأقراص ذات الحواف المخيطة والقطن الطبيعي 100% تحمي البشرة الحساسة وتمنع الوبر وإهدار السوائل بعكس القطن التجاري الرخيص.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتميز ألياف القطن الطبيعي بخصائص شعرية اسموزية تمتص السوائل وتحتفظ بها في فجوات النسيج المبطن، مما يتيح التحرير التدريجي للتونر أو الميسيلار عند ملامسة الجلد دون تسرب السائل بسرعة.</p>"""

    faqs = [
        ("ما هي المسحات القطنية الدائرية 80 قطعة؟", "هي أقراص قطنية طبيعية 100% ثنائية الجوانب بحواف مخيطة مصممة لإزالة المكياج وتطبيق التونر والأنسجة الفموية."),
        ("هل تترك الأقراص أي وبر أو ألياف على الوجه؟", "لا، بفضل تقنية الحواف المخيطة والمضغوطة حرارياً، تبقى الأقراص متماسكة ولا تترك أي وبر أثناء البلل."),
        ("ما الفرق بين جانبي القرص القطني؟", "يتميز القرص بجانب مضلع لإزالة المكياج وطلاء الأظافر بفاعلية، وجانب ناعم أملس لتطبيق التونر واللوشنات."),
        ("هل القطن مصنوع من مواد طبيعية 100%؟", "نعم، الأقراص مصنوعة من قطن طبيعي نقي 100% خالي من العطور والمواد الكيميائية المبيضة."),
        ("كم قطعة تحتوي هذه العبوة؟", "تحتوي العبوة الاقتصادية على 80 قرصاً قطنياً دائرياً."),
        ("هل تناسب البشرة الحساسة ومحيط العينين؟", "نعم، نسيجها الناعم والنقي يجعلها آمنة ولطيفة جداً على البشرة الحساسة ومحيط العينين."),
        ("هل يمكن استخدامها لإزالة طلاء الأظافر؟", "نعم، ممتازة لإزالة طلاء الأظافر بسهولة بفضل نسيجها المتماسك الذي يتحمل مزيلات الأسيتون."),
        ("هل تساعد في توفير استهلاك التونر والميسيلار؟", "نعم، امتصاصها المتوازن يوزع السائل بكفاءة دون امتصاصه بالكامل داخل القرص."),
        ("هل العبوة قابلة للإغلاق؟", "نعم، تحتوي العبوة على رباط علوي سريعة السحب لحماية الأقراص من الغبار والرطوبة."),
        ("هل يمكن إعادة استخدام القرص القطني؟", "لا، الأقراص القطنية مصممة للاستخدام المرة الواحدة لضمان أقصى درجات النظافة والوقاية."),
        ("ما هو بلد صنع هذه الأقراص؟", "صُنعت في مصانع معتمدة وفق أعلى معايير الجودة والنظافة العالمية."),
        ("هل تحتوي على كلور أو مواد مبيضة؟", "لا، هي خالية من الكلور والعطور والمواد الحافظة."),
        ("هل تناسب استخدام الأطفال؟", "نعم، نسيجها النقي الآمن ممتاز لتنظيف بشرة الأطفال والرضع بلطف."),
        ("كيف أحتفظ بالعبوة بالشكل الصحيح؟", "تُحفظ في مكان جاف ونظيف بعيداً عن رطوبة الحمام المباشرة."),
        ("هل تصمد الأقراص عند نقعها بالسائل؟", "نعم، الحواف المضغوطة تحافظ على تماسك القرص حتى عند نقعه بالكامل بماء الميسيلار."),
        ("هل تسبب حساسية للجلد؟", "لا، لأنها قطن نقي 100% خالية من أي صبغات أو مسببات حساسية."),
        ("هل يناسب استخدامها للرجال؟", "نعم، ممتازة لتطبيق المطهرات بعد الحلاقة وتغيير الضمادات."),
        ("ما هو قطر القرص القطني الدائري؟", "تأتي بقطر قياسي مريح يغطي مساحة الوجه والعيون بسهولة."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "كافة المستلزمات لدى صيدلية إكليل أبها مضمونة ومصنوعة من قطن نقي 100%."),
        ("هل يمكن استخدامها لتنظيف الجروح البسيطة؟", "نعم، نقاؤها يتيح استخدامها لتطهير الجروح البسيطة بمطهر الجلد."),
        ("هل تتكسر عند إزالة المسكارة المقاومة للماء؟", "لا، نسيجها المضلع القوي يتناول المسكارة المائية والثقيلة بسلاسة."),
        ("هل تناسب وضع ماء الورد على الوجه؟", "نعم، الجانب الناعم ممتاز لتوزيع ماء الورد والترطيب اليومي."),
        ("هل يترك القطن ملمساً جافاً؟", "يمتاز بمرونة ونعومة تمنع خمش أو جرح البشرة."),
        ("هل يمكن حمل العبوة في حقيبة السفر؟", "نعم، العبوة خفيفة ومحكمة الغلق ومناسبة جداً للسفر."),
        ("هل يختلف شكلها بعد البلل؟", "تحافظ على شكلها الدائري دون تمدد أو تفكك.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Round Cotton Pads - 80 Pieces</strong> are your essential daily skincare companion for gentle makeup removal and precise toner application. Crafted from 100% pure natural cotton, these premium round pads feature thermal-stitched edges that prevent linting, fraying, or leaving residual fibers on your skin during use.</p>
<p>Boasting a versatile dual-sided design, one side features a softly cushioned smooth texture ideal for applying toners, lotions, and hydration liquids, while the embossed textured side easily lifts stubborn makeup, impurities, and nail polish in a single gentle wipe without irritating the skin.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Pure Natural Cotton:</strong> Soft, pure cotton pads free from harsh chemicals, perfumes, and chlorine bleach.</li>
  <li><strong>Dual-Sided Embossed Design:</strong> Smooth side for toners and hydration; embossed side for effective makeup removal.</li>
  <li><strong>Stitched Lint-Free Edges:</strong> Premium stitched edges prevent pad separation and linting on skin or lashes.</li>
  <li><strong>High Absorbency Efficiency:</strong> Absorbs and distributes liquids economically without wasting skincare products.</li>
  <li><strong>Gentle on Sensitive Skin:</strong> Hypoallergenic and safe for everyday use around delicate eye contours.</li>
  <li><strong>Economical 80-Piece Pack:</strong> Convenient draw-string pouch preserves pads clean and dust-free.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Makeup Removal):</strong> Apply makeup remover or micellar water onto the textured side of the pad.</li>
  <li><strong>Step 2 (Gentle Wipe):</strong> Gently wipe across face, eyelids, and lips to remove makeup and impurities.</li>
  <li><strong>Step 3 (Toner Application):</strong> Pour toner onto the smooth side and gently pat onto face to hydrate and refine pores.</li>
  <li><strong>Step 4 (Nail Polish Removal):</strong> Moisten pad with nail polish remover and wipe nails clean.</li>
  <li><strong>Step 5 (Dispose):</strong> Discard single-use pad responsibly after use; do not reuse.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>100% Pure Natural Cotton Fibers:</strong> Ultra-soft, highly absorbent natural cotton fibers gentle on skin.</li>
  <li><strong>Bleach & Fragrance Free:</strong> Pure clean composition free from chlorine, synthetic fragrances, and preservatives.</li>
  <li><strong>Thermal Stitched Edges:</strong> Maintains pad integrity and prevents fraying when wet.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic use on skin and nails only.</li>
  <li>Store in a clean, dry place away from humidity and direct sunlight.</li>
  <li>Dispose of pad after single use and keep drawstring pouch closed.</li>
  <li>Keep out of reach of young children.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking ultra-soft, lint-free 100% pure cotton pads for makeup removal and toner application.</li>
  <li>Individuals with sensitive skin looking for hypoallergenic, chemical-free cosmetic cotton.</li>
  <li>Suitable for daily family skincare routines.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Generic / Ekleel Abha Pharmacy</td></tr>
  <tr><th>Category</th><td>Cosmetic Accessories / Cotton Pads & Rounds</td></tr>
  <tr><th>Product Type</th><td>Dual-Sided Stitched Round Cotton Pads (80 Pack)</td></tr>
  <tr><th>Volume/Weight</th><td>80 Cotton Pads</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Face, Eyes, Nails)</td></tr>
  <tr><th>Finish</th><td>Clean, dry skin free from makeup residue and lint</td></tr>
  <tr><th>Texture</th><td>Soft smooth & embossed dual cotton with stitched edges</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-Free (Unscented)</td></tr>
  <tr><th>Active Ingredients</th><td>100% Pure Natural Cotton</td></tr>
  <tr><th>Country of Origin</th><td>Turkey / China</td></tr>
  <tr><th>Manufacturer</th><td>Cotton Products Care</td></tr>
  <tr><th>Age Group</th><td>All Ages</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Pure Cotton Pads & Skincare Application</h2>

<h3>What problem does this solve?</h3>
<p>Round Cotton Pads solve pad fraying, lint shedding on eyelashes, and liquid product waste commonly experienced with cheap unstitched cotton wool balls.</p>

<h3>Why does this condition happen?</h3>
<p>Low-grade unstitched cotton lacks edge compression, causing loose fibers to detach when wetted with liquids, depositing lint across facial pores and eye contours.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Use Embossed Side for Makeup:</strong> The textured side grips makeup particles without harsh dragging.<br>
2. <strong>Use Smooth Side for Toners:</strong> The smooth side releases liquids evenly onto skin.<br>
3. <strong>Pat Gently:</strong> Avoid aggressive rubbing around delicate eye areas.<br>
4. <strong>Keep Pack Sealed:</strong> Pull the drawstring closed to protect pads from dust and moisture.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "All cosmetic cotton pads deliver identical quality."<br>
<strong>Fact:</strong> 100% natural cotton pads with stitched edges protect sensitive skin and prevent linting far better than cheap synthetic blends.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Pure cotton fibers possess natural capillary action, absorbing liquid into inner lumen spaces. The thermal-stitched perimeter prevents structural deformation under wet tension, releasing skincare liquids smoothly upon dermal contact.</p>"""

    en_faqs = [
        ("What are Round Cotton Pads 80 Pieces?", "They are 100% pure natural dual-sided round cotton pads with stitched edges for makeup removal and toner application."),
        ("Do these pads leave lint on the face?", "No, thermal-stitched edges maintain pad structure, preventing lint or fiber shedding."),
        ("What is the difference between the two sides?", "One side is embossed for removing makeup and nail polish; the smooth side is designed for applying toners."),
        ("Are these pads 100% pure natural cotton?", "Yes, they are made from 100% pure cotton free of chlorine bleach and synthetic fragrances."),
        ("How many pads are in this pack?", "This economical pack contains 80 round cotton pads."),
        ("Are they safe for sensitive skin and eyes?", "Yes, their soft hypoallergenic texture makes them completely safe for sensitive skin and eye contours."),
        ("Can they be used to remove nail polish?", "Yes, their durable stitched design holds up well against acetone nail polish removers."),
        ("Do they help prevent toner waste?", "Yes, balanced absorbency distributes liquids efficiently without oversaturating inner layers."),
        ("Is the packaging re-sealable?", "Yes, it features a convenient drawstring top to keep pads clean and dust-free."),
        ("Are these cotton pads reusable?", "No, they are single-use pads designed for hygienic disposable application."),
        ("Where are these cotton pads manufactured?", "They are produced in certified facilities following international quality standards."),
        ("Do they contain chlorine or chemical bleaches?", "No, they are 100% chlorine-free and fragrance-free."),
        ("Are they suitable for baby care?", "Yes, their pure natural texture is gentle enough for cleansing baby skin."),
        ("How should I store this pack?", "Store in a dry, clean place away from direct bathroom moisture."),
        ("Do the pads hold together when soaked?", "Yes, thermal-stitched edges prevent separation even when fully saturated with micellar water."),
        ("Do they cause skin allergies?", "No, made from 100% pure natural cotton, they are completely hypoallergenic."),
        ("Can men use these cotton pads?", "Yes, they are excellent for applying aftershave toners and antiseptic cleansers."),
        ("What is the diameter of each round pad?", "They feature a standard comfortable size covering face and eye areas easily."),
        ("How do I verify product authenticity at Ekleel Abha?", "All cosmetic cotton products at Ekleel Abha are 100% genuine and quality-assured."),
        ("Can they be used for minor wound cleaning?", "Yes, their pure lint-free texture makes them suitable for applying topical antiseptics."),
        ("Do they break apart when removing waterproof mascara?", "No, the durable embossed texture lifts heavy mascara smoothly without tearing."),
        ("Are they suitable for applying rose water?", "Yes, the smooth side is ideal for applying rose water and liquid hydration."),
        ("Do they feel scratchy on skin?", "No, 100% pure cotton fibers provide a soft, non-abrasive touch."),
        ("Is the pack travel-friendly?", "Yes, the lightweight drawstring bag is ideal for travel."),
        ("Do they retain their round shape when wet?", "Yes, stitched edges maintain round shape without stretching.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1728",
        "sku": "EK-1728",
        "gtin": "6286030000270",
        "category": "مستلزمات التجميل / الأقراص والمسحات القطنية",
        "brand": "Generic",
        "ar": {
            "title": "مسحات قطنية دائرية 80 قطعة",
            "meta_title": "مسحات قطنية دائرية 80 قطعة | صيدلية إكليل أبها",
            "meta_description": "اشتري مسحات قطنية دائرية لإزالة المكياج وتطبيق التونر 80 قطعة. قطن طبيعي 100% بحواف مخيطة بدون وبر. متاح لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["مسحات_قطنية", "قطن_دائري", "ازالة_المكياج", "قطن_طبيعي", "إكليل_أبها"]
        },
        "en": {
            "title": "Round Cotton Pads - 80 Pieces",
            "meta_title": "Round Cotton Pads 80 Pieces | Ekleel Abha Pharmacy",
            "meta_description": "Buy 100% Pure Round Cotton Pads (80 Pieces). Dual-sided stitched lint-free pads for makeup removal & toner. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["cotton_pads", "round_cotton", "makeup_remover", "pure_cotton", "ekleel_abha"]
        },
        "schema": {
            "brand": "Generic",
            "category": "Cosmetics / Cotton Pads",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "round-cotton-pads-80-pieces.webp",
            "alt": "Round Cotton Pads 80 Pieces",
            "title": "Round Cotton Pads 80 Pieces"
        }
    }

def create_product_1730():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>جل الورد الطبيعي لترطيب البشرة من ناتشر ريبورت (Nature Report Natural Rose Soothing & Moisturizing Gel - 300ml)</strong> مستحضراً كورية مذهلاً للعناية الشاملة بالوجه والجسم والشعر. يعتمد هذا الجل المرطب على تركيبة فائقة النقاء تحتوي على 99% من خلاصة ماء الورد الطبيعي، مما يوفر تهدئة فورية للاحمرار وترطيباً عميقاً يستمر طوال اليوم دون أي ملمس زيتي أو لزج.</p>
<p>يمتاز الجل بقوام مائي خفيف يمتصه الجلد بسرعة كورية فائقة، ويحتوي على مضادات أكسدة طبيعية تحمي البشرة من الإجهاد البيئي والجذور الحرة. يُستخدم جل ناتشر ريبورت بالورد كمرطب يومي للوجه، مهدئ لاحمرار الشمس، بلسم خفيف للشعر، مرطب للجسم، ومهدئ للبشرة بعد الحلاقة أو إزالة الشعر.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>غني بـ 99% خلاصة الورد الطبيعي:</strong> يمنح البشرة ترطيباً مائياً ناعماً ويقلل الاحمرار والتهيج فورياً.</li>
  <li><strong>تهدئة فورية للبشرة المتهدجة:</strong> يبرد الاحمرار والحرارة الناتجة عن الشمس أو التقشير وإزالة الشعر.</li>
  <li><strong>قوام جيلي مائي خفيف:</strong> يمتص بسرعة كاملة دون ترك أي طبقة دهنية أو لزوجة على الجلد.</li>
  <li><strong>مستحضر شمول متعدد الاستخدامات:</strong> يصلح للوجه، الجسم، الأظافر، وأطراف الشعر الجافة.</li>
  <li><strong>مكافحة الأكسدة وإضفاء النضارة:</strong> يعزز حيوية الوجه ويكسبه عبق الورد الطبيعي الفاخر.</li>
  <li><strong>مناسب لجميع أنواع البشرة:</strong> تركيبة كورية لطيفة وآمنة تماماً للبشرة الحساسة والجافة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> اغسلي المنطقة المطلوبة (الوجه أو الجسم) بالماء الفاتر وجففيها بلطف.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية مناسبة من جل الورد من ناتشر ريبورت على كف اليد.</li>
  <li><strong>الخطوة الثالثة (التوزيع):</strong> وزعي الجل بلطف ودلكيه حتى يتم امتصاصه كاملاً داخل البشرة.</li>
  <li><strong>الخطوة الرابعة (الاستخدام المفتوح):</strong> يُستخدم كمرطب يومي، أو كقناع ترطيبي مائي بوضع طبقة سميكة لمدة 15 دقيقة ثم مسحها.</li>
  <li><strong>الخطوة الخامسة (الترطيب بعد الشمس):</strong> وضعي الجل بارداً بعد التعرض للشمس لتهدئة الجلد فورياً.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة ماء الورد 99% (Rosa Centifolia Flower Water):</strong> تمنح ترطيباً مائياً مهدئاً وتوحد لون الوجه وتقي من الالتهابات.</li>
  <li><strong>الجليسرين والتريهالوز:</strong> يجذبان رطوبة الجو ويحبسان الماء داخل طبقات الجلد العميقة.</li>
  <li><strong>خلاصة البابونج والألوفيرا:</strong> تعززان تهدئة احمرار البشرة وتلطيف التسلخات.</li>
  <li><strong>مركبات مائية خفيفة:</strong> تضمن امتصاص الجل في ثوانٍ معدودة دون سد المسام.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الوجه والجسم والشعر فقط.</li>
  <li>تجنبي ملامسة الجل المباشرة للعينين؛ وفي حال ملامستهما اشطفي بالماء.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
  <li>في حال ظهور أعراض حساسية توقفي عن الاستخدام.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تبحث عن جل ترطيب مائي كوري 99% ورد خفيف وخالي من الدهون.</li>
  <li>صاحبات البشرة الحساسة أو المتهيجة التي تحتاج إلى تهدئة فورية بعد الشمس أو الحلاقة.</li>
  <li>مناسب لجميع أنواع البشرة وللاستخدام اليومي الشامل.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ناتشر ريبورت (Nature Report)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / أقنعة وجل المرطبات</td></tr>
  <tr><th>نوع المنتج</th><td>جل الورد الطبيعي المهدئ والمرطب (99% Rose Gel)</td></tr>
  <tr><th>الحجم/الوزن</th><td>300 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (الوجه، الجسم، الشعر)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة مشرقة، هادئة، خالية من اللمعان واللوزجة</td></tr>
  <tr><th>الملمس</th><td>جل مائي خفيف ينفذ بسرعة</td></tr>
  <tr><th>العطر</th><td>عطر الورد الطبيعي المنعش واللطيف</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة الورد 99%، جليسرين، تريهالوز، بابونج</td></tr>
  <tr><th>بلد المنشأ</th><td>كوريا الجنوبية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Nature Report Korea</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد ماء الورد وترطيب الجيلي المائي (Nature Report)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج جل الورد من ناتشر ريبورت مشكلة تهيج واحمرار البشرة الناتجة عن التعرض للشمس أو الحلاقة أو التقشير، ويحل مشكلة الجفاف الداخلي للبشرة الدهنية والمختلطة دون إثقالها بالزيوت.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تؤدي أشعة الشمس والتلوث والمنظفات إلى فقدان الماء السريع من طبقات الوجه السطحية، فتتهيج البشرة وتفقد نضارتها الطبيعية وترتفع حرارتها.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>حفظ الجل في الثلاجة:</strong> حفظ العبوة في الثلاجة يضاعف الانتعاش وتهدئة احمرار الوجه.<br>
2. <strong>استخدامه بعد إزالة الشعر:</strong> وضعي الجل فورياً بعد الحلاقة لمنع تكون الحبوب الاحمرار.<br>
3. <strong>قناع مائي ليلي:</strong> ضعي طبقة سميكة قبل النوم لترطيب عميق دون سد المسام.<br>
4. <strong>عناية بأطراف الشعر:</strong> مرري قطرة على أطراف الشعر لتهدئة التطاير.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "جل الورد يسبب جفاف البشرة الشديدة."<br>
<strong>الحقيقة:</strong> جل ناتشر ريبورت يحتوي على 99% خلاصة الورد والتريهالوز التي تحبس الترطيب المائي داخل الخلايا بعكس ماء الورد الصافي المتبخر.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتميز خلاصات الورد الطبيعي بمركبات الفلافونويد والأنثوسيانين المضادة لالتهابات الجلد، والتي تهدئ المستقبليات المتهيجة فورياً، بينما تشكل البوليمرات المائية شبكة ترطيب رقيقة تمنع تبخر الماء من البشرة (TEWL) وتنعش أنسجة الجلد.</p>"""

    faqs = [
        ("ما هو جل الورد الطبيعي من ناتشر ريبورت؟", "هو جل كوري مرطب ومهدئ يحتوي على 99% خلاصة الورد الطبيعي لترطيب الوجه والجسم والشعر دون لزوجة."),
        ("ما هي فوائد خلاصة الورد 99% للبشرة؟", "تهدئ الاحمرار، تبرد تهيج الشمس والتقشير، تمنح ترطيباً مائياً، وتكسب الوجه نضارة وعبيراً زكياً."),
        ("هل يترك الجل ملمساً دهنياً أو لزجاً؟", "لا، يمتاز بقوام مائي خفيف يمتصه الجلد في ثوانٍ معدودة دون أثر زيتي أو لزوجة."),
        ("ما حجم عبوة جل ناتشر ريبورت؟", "تأتي العبوة بحجم 300 مل، وهي كمية وافرة تكفي للاستخدام المتعدد على الوجه والجسم."),
        ("هل يمكن استخدام الجل بعد الحلاقة أو إزالة الشعر؟", "نعم، هو ممتاز جداً لتهدئة الفروة والبشرة بعد الحلاقة وتخفيف التهابات إزالة الشعر."),
        ("هل يناسب البشرة الدهنية والمختلطة؟", "نعم، يعتبر خياراً مثالياً للبشرة الدهنية لأنه يرطب بعمق دون سد المسام أو زيادة الدهون."),
        ("هل يمكن استخدامه كقناع ترطيبي للوجه؟", "نعم، يمكن وضع طبقة سميكة منه كقناع مائي لمدة 15 دقيقة ثم مسحه لترطيب مضاعف."),
        ("هل يناسب الجل الشعر والأظافر؟", "نعم، يمكن مسح كمية بسيطة منه على الأظافر لتقويتها وعلى أطراف الشعر لتهدئة الهيشان."),
        ("ما هو بلد صنع جل ناتشر ريبورت؟", "صُنع بفخر في كوريا الجنوبية وفق أعلى معايير الجودة الكورية."),
        ("هل يحتوي على معطرات قاسية؟", "يتميز برائحة ورد طبيعية ناعمة ولطيفة جداً."),
        ("هل يمكن حفظ الجل في الثلاجة؟", "نعم، حفظه في الثلاجة يمنح برودة وانتعاشاً مضاعفاً لتقليل انتفاخ الوجه والاحمرار."),
        ("هل يساعد في تهدئة حروق الشمس؟", "نعم، يبرد الجلد فورياً ويخفف احمرار وتسلخات التعرض للشمس."),
        ("هل يناسب جميع أنواع البشرة؟", "نعم، مناسب للبشرة العادية، الجافة، الدهنية، والمختلطة والحساسة."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات ناتشر ريبورت لدى صيدلية إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يلزم غسل الوجه بعد وضع الجل؟", "لا، ينفذ الجل بالكامل داخل البشرة ولا يلزم غسله بالماء."),
        ("هل يسبب الجل ظهور حب الشباب؟", "لا، هو خفيف وغير كوميدوجينيك (لا يسد المسام)."),
        ("كم مرة يُنصح باستخدامه يومياً؟", "يمكن استخدامه مرتين يومياً أو كلما شعرتِ بحاجة البشرة للتهدئة والترطيب."),
        ("هل يناسب الرجال والنساء؟", "نعم، يناسب كلا الجنسين ممتاز جداً للترطيب اليومي."),
        ("هل يناسب الأطفال؟", "مناسب للأطفال فوق سن 6 سنوات لتهدئة الاحمرار والجفاف."),
        ("هل يساعد في تضييق المسام الواسعة؟", "نعم، تبريد البشرة وتوازن رطوبتها يساعد في تقليل مظهر المسام."),
        ("هل يمكن استخدامه حول العينين؟", "يمكن وضعه بلطف حول العينين لتهدئة الانتفاخ والإجهاد."),
        ("كيف أحتفظ بالعبوة بالشكل الصحيح؟", "تُحفظ في مكان بارد وجاف بعيداً عن أشعة الشمس المباشرة."),
        ("هل يساعد في توحيد لون البشرة؟", "مضادات الأكسدة بالورد تمنح الوجه إشراقة ونضارة متجانسة."),
        ("هل يعاد إغلاق العبوة بإحكام؟", "نعم، تأتي في عبوة دائرية متينة بغطاء لولبي محكم للحفاظ على الجل."),
        ("هل يناسب الاستخدام في الصيف والشتاء؟", "نعم، يرطب في الصيف بعد الشمس ويحمي من جفاف الشتاء.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Nature Report Natural Rose Soothing & Moisturizing Gel (300ml)</strong> is an iconic Korean multi-purpose skincare gel formulated with 99% pure Rose Flower Water extract. Designed to deliver instant cooling relief and long-lasting water hydration, it calms redness, restores elasticity, and refreshes the skin without any oily or sticky residue.</p>
<p>Featuring a lightweight aqueous gel texture, it absorbs into skin cells within seconds. Rich in natural antioxidants, Nature Report Rose Gel serves as a daily face moisturizer, sun exposure soothing gel, post-shave balm, body hydrator, and light hair conditioning treatment suitable for the whole family.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Enriched with 99% Pure Rose Extract:</strong> Delivers instant soothing hydration to calm irritated or flushed skin.</li>
  <li><strong>Immediate Cooling & Calming Effect:</strong> Cools redness and heat caused by sun exposure, shaving, or exfoliation.</li>
  <li><strong>Fast-Absorbing Non-Greasy Texture:</strong> Penetrates fully within seconds without sticky or heavy residue.</li>
  <li><strong>Versatile All-in-One Application:</strong> Suitable for face, body, hands, nails, and dry hair tips.</li>
  <li><strong>Antioxidant Radiance Boost:</strong> Defends skin against environmental free radicals while imparting a fresh rose aroma.</li>
  <li><strong>Safe for Sensitive Skin:</strong> Hypoallergenic K-beauty formula safe for all skin types, including sensitive skin.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse targeted area (face or body) with warm water and gently dry.</li>
  <li><strong>Step 2 (Dispense):</strong> Take a suitable amount of Nature Report Rose Gel onto palms.</li>
  <li><strong>Step 3 (Apply):</strong> Smooth gently across skin until fully absorbed.</li>
  <li><strong>Step 4 (Hydrating Mask):</strong> Apply a thick layer as a 15-minute hydrating mask, then wipe off excess.</li>
  <li><strong>Step 5 (After-Sun Care):</strong> Apply chilled gel directly after sun exposure to cool skin redness.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Rosa Centifolia Flower Water (99%):</strong> Pure rose water providing calming, anti-inflammatory hydration.</li>
  <li><strong>Glycerin & Trehalose:</strong> Humectants retaining water deep within dermal layers.</li>
  <li><strong>Chamomile & Aloe Extracts:</strong> Soothe skin flaring and calm post-shave irritation.</li>
  <li><strong>Light Aqueous Base:</strong> Absorbs in seconds without clogging facial pores.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on face, body, and hair only.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
  <li>Discontinue use if irritation develops.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a 99% pure rose water Korean gel for lightweight, non-greasy hydration.</li>
  <li>Individuals needing instant soothing relief after sun exposure, shaving, or peeling.</li>
  <li>Suitable for all skin types and everyday multi-purpose application.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Nature Report</td></tr>
  <tr><th>Category</th><td>Skincare / Soothing & Moisturizing Gels</td></tr>
  <tr><th>Product Type</th><td>99% Natural Rose Soothing Gel</td></tr>
  <tr><th>Volume/Weight</th><td>300 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Face, Body, Hair, Nails)</td></tr>
  <tr><th>Finish</th><td>Calmed, hydrated, radiant, non-sticky finish</td></tr>
  <tr><th>Texture</th><td>Lightweight fast-absorbing water gel</td></tr>
  <tr><th>Fragrance</th><td>Fresh natural rose aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Rose Water Extract 99%, Glycerin, Trehalose, Chamomile</td></tr>
  <tr><th>Country of Origin</th><td>South Korea</td></tr>
  <tr><th>Manufacturer</th><td>Nature Report Korea</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 99% Rose Water & Aqueous Gel Hydration</h2>

<h3>What problem does this solve?</h3>
<p>Nature Report Rose Gel resolves skin redness, post-shave irritation, sun flare-ups, and internal dehydration without clogging pores or leaving oily film.</p>

<h3>Why does this condition happen?</h3>
<p>Solar radiation, exfoliation, and harsh soaps deplete epidermal moisture, causing skin flushing, tightness, and temperature elevation.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Refrigerate Gel:</strong> Store in the fridge to enhance cooling and puffiness reduction.<br>
2. <strong>Post-Shave Balm:</strong> Apply immediately after shaving to prevent bumps.<br>
3. <strong>Overnight Water Mask:</strong> Layer generously before sleep for deep hydration.<br>
4. <strong>Hair Tip Care:</strong> Smooth a dab onto dry hair ends to tame flyaways.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Rose water gels dry out skin quickly."<br>
<strong>Fact:</strong> Nature Report combines 99% rose water with humectant Trehalose that binds water inside skin cells.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Rose extracts contain anthocyanin and flavonoid antioxidants that downregulate pro-inflammatory skin pathways. Hydrophilic gel polymers create a breathable moisture matrix that prevents TEWL while lowering skin temperature upon evaporation.</p>"""

    en_faqs = [
        ("What is Nature Report Natural Rose Soothing Gel?", "It is a Korean 99% Rose Water gel delivering instant cooling hydration for face, body, and hair without stickiness."),
        ("What are the benefits of 99% Rose extract?", "It soothes redness, cools sun heat, delivers lightweight water moisture, and leaves a fresh rose fragrance."),
        ("Does it feel greasy or sticky?", "No, it absorbs fully within seconds, leaving skin soft and non-sticky."),
        ("What size is this product tub?", "It comes in a 300ml tub providing generous volume for face and body use."),
        ("Can it be used after shaving or hair removal?", "Yes, it is excellent for calming redness and post-shave irritation."),
        ("Is it suitable for oily and combination skin?", "Yes, it hydrates deeply without clogging pores or adding oil."),
        ("Can it be used as a face mask?", "Yes, apply a thick layer for 15 minutes as an intensive hydrating water mask."),
        ("Can it be applied to hair and nails?", "Yes, it conditions cuticles and tames flyaway hair tips."),
        ("Where is Nature Report manufactured?", "It is proudly manufactured in South Korea following K-beauty standards."),
        ("Does it contain harsh artificial perfumes?", "It features a subtle, fresh natural rose fragrance."),
        ("Can I keep it in the refrigerator?", "Yes, chilling it enhances cooling performance for reducing puffiness."),
        ("Does it help calm sunburns?", "Yes, it rapidly cools and soothes sun-exposed, overheated skin."),
        ("Is it suitable for all skin types?", "Yes, ideal for normal, dry, oily, combination, and sensitive skin."),
        ("How do I verify authenticity at Ekleel Abha?", "All Nature Report products at Ekleel Abha are 100% original from certified Korean distributors."),
        ("Do I need to wash my face after applying?", "No, it absorbs completely into the skin without rinsing."),
        ("Does it cause acne or clogged pores?", "No, it is lightweight and non-comedogenic."),
        ("How often should I use it?", "Use twice daily or whenever skin needs soothing hydration."),
        ("Can both men and women use it?", "Yes, it is a unisex multi-purpose hydration gel."),
        ("Is it safe for children?", "Safe for adults and children aged 6+ for cooling redness."),
        ("Does it help reduce visible pore appearance?", "Yes, cooling skin and balancing hydration refines pore appearance."),
        ("Can it be used around the eyes?", "Yes, apply gently around eye contours to soothe tiredness."),
        ("How should I store the tub?", "Store in a cool, dry place away from direct sunlight."),
        ("Does it help even out skin tone?", "Antioxidants in rose water enhance natural complexion radiance."),
        ("Is the tub securely sealable?", "Yes, it comes in a durable tub with a secure screw lid."),
        ("Can it be used year-round?", "Yes, it hydrates after summer sun and guards against winter dryness.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1730",
        "sku": "EK-1730",
        "gtin": "8809514485134",
        "category": "العناية بالبشرة / أقنعة وجل المرطبات",
        "brand": "Nature Report",
        "ar": {
            "title": "جل الورد الطبيعي لترطيب البشرة من ناتشر ريبورت - 300مل",
            "meta_title": "جل الورد ناتشر ريبورت 300مل | صيدلية إكليل أبها",
            "meta_description": "اشتري جل الورد الطبيعي الكوري 99% لترطيب وتهدئة البشرة من ناتشر ريبورت (300مل). خفيف وسريع الامتصاص للوجه والجسم. أصلي من إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["ناتشر_ريبورت", "جل_الورد", "ترطيب_كوري", "العناية_بالبشرة", "إكليل_أبها"]
        },
        "en": {
            "title": "Nature Report Natural Rose Soothing & Moisturizing Gel - 300ml",
            "meta_title": "Nature Report Natural Rose Soothing Gel 300ml | Ekleel Abha",
            "meta_description": "Buy Nature Report Natural Rose 99% Soothing Gel (300ml). Hydrates and calms face, body, & hair without stickiness. 100% authentic at Ekleel Abha.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["nature_report", "rose_gel", "soothing_gel", "korean_skincare", "ekleel_abha"]
        },
        "schema": {
            "brand": "Nature Report",
            "category": "Skincare / Soothing Gel",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "nature-report-natural-rose-soothing-and-moisturizing-gel-300ml.webp",
            "alt": "Nature Report Natural Rose Soothing & Moisturizing Gel 300ml",
            "title": "Nature Report Natural Rose Soothing & Moisturizing Gel 300ml"
        }
    }

print("Loaded 1728 & 1730 builders")
