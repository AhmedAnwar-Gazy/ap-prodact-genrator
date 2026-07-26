import json, os

def create_product_1692():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم الوجه مضاد للبقع من جلو اند لوفلي (Glow & Lovely Anti-Marks Face Cream - 100g)</strong> الحليفة المتطورة للتخلص من التصبغات والبقع الداكنة وآثار حب الشباب. يعتمد هذا الكريم في تركيبته على مركب فايتا-ألو (Vita-Aloe Complex) المزود بمركب النياسيناميد (فيتامين B3) وبخلاصة الصبار الطبيعية وفيتامين E، حيث يعمل بتناغم فائق لتفتيح البشرة وتوحيد لونها واستعادة إشراقتها الطبيعية في فترة وجيزة.</p>
<p>صُمم هذا الكريم بتركيبة خفيفة غير دهنية تتغلغل بسهولة في طبقات الجلد السطحية، وتحتوي على واقيات شمسية ثلاثية لحماية البشرة من الأشعة فوق البنفسجية (UVA/UVB) الضارة التي تسبب تفاقم البقع والاسمرار. يمنح الاستخدام اليومي المنتظم بشرة أملس، أكثر نضارة، وخالية من علامات الإجهاد والبقع المزعجة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>إخفاء وتقليل البقع الداكنة:</strong> يستهدف التصبغات وآثار الحبوب والبقع الناتجة عن الشمس بفعالية مثبتة.</li>
  <li><strong>مركب النياسيناميد (فيتامين B3):</strong> يعزز تفتيح البشرة وتوحيد لونها ويمنح إشراقة وردية صحية.</li>
  <li><strong>حماية ثلاثية من أشعة الشمس:</strong> يقي الجلد من الأشعة فوق البنفسجية ويمنع ظهور بقع جديدة أو اسمرار مكرر.</li>
  <li><strong>ترطيب وتغذية بمركب الصبار وفيتامين E:</strong> يهدئ البشرة المتهيجة ويرطبها بعمق مع تقوية حاجز حمايتها الطبيعي.</li>
  <li><strong>قوام خفيف ومات (Matte):</strong> يمتص بسرعة دون ترك أثر زيتي أو لزوجة، مما يجعله مثالي لاستخدام النهار.</li>
  <li><strong>مناسب للاستخدام اليومي:</strong> تركيبة آمنة ومجربة جلدياً تناسب جميع أنواع البشرة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> اغسلي وجهك جيداً بالغسول المناسب وجففيه بلطف بمنديل ناعم.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية مناسبة من الكريم على نقاط الوجه (الجبين، الخدود، الأنف، والذقن) والرقبة.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> وزعي الكريم بأطراف الأصابع بحركات دائرية خفيفة حتى يمتصه الجلد تماماً.</li>
  <li><strong>الخطوة الرابعة (التكرار):</strong> يُفضل استخدامه مرتين يومياً (صباحاً ومساءً) للحصول على أفضل نتائج التفتيح.</li>
  <li><strong>الخطوة الخامسة (الوقاية):</strong> يمكنك وضعه كقاعدة خفيفة قبل المكياج أو الخروج في الشمس.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>النياسيناميد (Niacinamide - Vitamin B3):</strong> يحد من انتقال الميلانين لخلايا البشرة السطحية ويقلل التصبغات والبقع.</li>
  <li><strong>خلاصة الصبار (Aloe Vera Extract):</strong> تلطف البشرة وتمنحها ترطيباً مائياً مهدئاً يقلل الاحمرار والتهيج.</li>
  <li><strong>فيتامين E (Tocopheryl Acetate):</strong> مضاد أكسدة يحمي خلايا الجلد من التلف والجذور الحرة.</li>
  <li><strong>مرشحات الشمس الثلاثية (Triple Sunscreens):</strong> تمتص وتشتت الأشعة فوق البنفسجية الضارة للوقاية من الاسمرار.</li>
  <li><strong>الجليسرين (Glycerine):</strong> يرطب البشرة ويمنع فقدان رطوبتها الداخلية خلال اليوم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الوجه والرقبة فقط.</li>
  <li>تجنبي ملامسة المنتج المباشرة للعينين؛ وفي حال ملامستها اشطفي بالماء النظيف.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن أشعة الشمس.</li>
  <li>في حال ظهور أعراض حساسية توقفي عن الاستخدام واستشيري طبيب الجلدية.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لمن يعانون من البقع الداكنة وآثار حب الشباب والتصبغات الناتجة عن الشمس.</li>
  <li>لكل من تبحث عن كريم يومي يجمع بين التفتيح، الترطيب، والحماية من الشمس.</li>
  <li>مناسب لجميع أنواع البشرة وخاصة البشرة العادية والدهنية والمختلطة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جلو اند لوفلي (Glow & Lovely)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات الوجه والتفتيح</td></tr>
  <tr><th>نوع المنتج</th><td>كريم مضاد للبقع وموحد للون البشرة</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (الوجه والرقبة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة مشرقة، متجانسة، وخالية من اللمعان الزيتي</td></tr>
  <tr><th>الملمس</th><td>كريمي خفيف سريع الامتصاص</td></tr>
  <tr><th>العطر</th><td>عطر منعش وأنيق</td></tr>
  <tr><th>المكونات النشطة</th><td>النياسيناميد (فيتامين B3)، خلاصة الصبار، فيتامين E، واقيات شمسية ثلاثية</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الهند (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (يونيليفر)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (من 15 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لآلية علاج التصبغات وعناية النياسيناميد (Glow & Lovely)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم جلو اند لوفلي مضاد البقع مشكلة فرط التصبغ الجلدي (Hyperpigmentation) والتفاوت في لون البشرة الناتج عن آثار الحبوب، الندبات القديمة، والتعرض المستمر لأشعة الشمس دون حماية.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>عند تعرض البشرة لأشعة الشمس أو التهابات الحبوب، تفرز خلايا الميلانوسيت كميات مفرطة من صبغة الميلانين كآلية دفاعية. تتجمع هذه الصبغات في نقاط محددة لتكون البقع الداكنة والتصبغات التي تأخذ وقتاً طويلاً للتلاشي تلقائياً.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الالتزام بالحماية من الشمس:</strong> استخدمي واقي الشمس يومياً لتجنب تحفيز صبغة الميلانين.<br>
2. <strong>تجنب عبث الحبوب:</strong> لا تلمسي الحبوب أو تعصريها لتجنب ترك ندبات داكنة permanent.<br>
3. <strong>الاستخدام المنتظم للنياسيناميد:</strong> المواظبة مرتين يومياً تسارع من تفتيح البقع.<br>
4. <strong>التقشير الأسبوعي:</strong> قشري البشرة بحمض لطيف لإزالة الخلايا السطحية الداكنة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات التفتيح تقشر الجلد وتجعله رقيقاً."<br>
<strong>الحقيقة:</strong> كريم جلو اند لوفلي يعتمد على النياسيناميد والصبار، وهما مكونان يغذيان حاجز البشرة ويرممان الخلايا دون إحداث تقشير كيميائي قاسي.</p>
<p><strong>خرافة:</strong> "النتائج تظهر في يوم واحد."<br>
<strong>الحقيقة:</strong> يتطلب التفتيح الآمن والفعال استخداماً منتظماً لمدة 2 إلى 4 أسابيع لتظهر نتائج واضحة مع دورة تجدد الخلايا.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعمل النياسيناميد (فيتامين B3) عن طريق تثبيط نقل جسيمات الميلانوسومات المحملة بالصبغة من خلايا التخزين إلى خلايا الكيراتين السطحية بنسبة تصل إلى 68%. وفي الوقت نفسه، تقوم واقيات الشمس الثلاثية بامتصاص الأشعة فوق البنفسجية لمنع تكون خلايا صبغية جديدة، بينما يعيد الصبار وفيتامين E رطوبة الجلد ويحفزان التجدد الخلوي الطبيعي.</p>"""

    faqs = [
        ("ما هو كريم جلو اند لوفلي مضاد للبقع وما هي فوائده؟", "هو كريم مخصص لتفتيح وتقليل البقع الداكنة وتوحيد لون البشرة بفضل تركيبة مركب فايتا-ألو الغني بالنياسيناميد وفيتامين E وخلاصة الصبار."),
        ("هل يزيل كريم جلو اند لوفلي آثار حب الشباب؟", "نعم، يساعد الاستخدام المنتظم على تقليل التصبغات وآثار الحبوب الداكنة بفضل قدرة النياسيناميد على تثبيط صبغة الميلانين."),
        ("هل يحتوي الكريم على واقي من أشعة الشمس؟", "نعم، يحتوي على واقيات شمسية ثلاثية لحماية البشرة من الأشعة فوق البنفسجية (UVA/UVB) ومنع اسمرار البقع."),
        ("كم مرة يجب تطبيق الكريم في اليوم؟", "يُنصح باستخدامه مرتين يومياً، صباحاً ومساءً على بشرة نظيفة للحصول على أفضل النتائج."),
        ("هل الكريم آمن للبشرة الدهنية؟", "نعم، يتميز بتركيبة خفيفة غير دهنية تمتص بسرعة وتمنح لمسة مطفأة خالية من اللمعان الزيتي."),
        ("متى تظهر نتائج التفتيح الملحوظة؟", "تظهر النتائج الأولية في تقليل التصبغات وتوحيد لون البشرة خلال 2 إلى 4 أسابيع من الاستخدام المنتظم."),
        ("هل يحتوي المنتج على مركبات تفتيح قاسية أو هيدروكينون؟", "لا، المنتج خالي تماماً من الهيدروكينون والمواد القاسية، ويعتمد على مكونات تفتيح آمنة مثل النياسيناميد."),
        ("هل يناسب هذا الكريم جميع أنواع البشرة؟", "نعم، هو مناسب للبشرة العادية، الدهنية، والمختلطة."),
        ("هل يمكن استخدام الكريم قبل وضع المكياج؟", "نعم، يعمل الكريم كقاعدة خفيفة ومطفيّة وممتازة قبل تطبيق المكياج."),
        ("ما حجم هذه العبوة؟", "تأتي العبوة بحجم 100 جم، وهي كمية كافية للاستخدام اليومي لفترة طويلة."),
        ("هل يسبب الكريم جفافاً للبشرة؟", "لا، يحتوي على خلاصة الصبار والجليسرين لترطيب البشرة والحفاظ على نعومتها."),
        ("ما الفرق بين Glow & Lovely و Fair & Lovely؟", "Glow & Lovely هو الاسم الجديد المطور المعتمد عالمياً لعلامة Fair & Lovely بنفس الجودة والفاعلية الكبيرة."),
        ("هل يناسب كريم جلو اند لوفلي الرجال أيضاً؟", "نعم، هو مناسب لكلا الجنسين ويساعد في توحيد لون البشرة وتقليل التصبغات الشمسية."),
        ("هل يمكن استخدامه على منطقة الرقبة؟", "نعم، يُفضّل وضعه على الوجه والرقبة معاً لضمان توحيد لون الجلد كاملاً."),
        ("هل يمنع ظهور بقع جديدة؟", "نعم، الحماية الثلاثية من الشمس تمنع تكون بقع جديدة ناتجة عن التعرض للشمس."),
        ("هل المنتج خالي من البارابين؟", "نعم، الفرمولة مطورة وآمنة للاستخدام اليومي."),
        ("كيف أحتفظ بالكريم بالشكل الصحيح؟", "يُحفظ في مكان بارد وجاف بعيداً عن حرارة الشباك أو أشعة الشمس المباشرة."),
        ("هل يسبب الكريم تهيج العينين؟", "يجب توخي الحذر عند وضعه وتجنب ملامسة المحيط المباشر للعينين."),
        ("ما هي الشركة المصنعة لهذا المنتج؟", "تم تصنيعه بواسطة شركة يونيليفر (Unilever) العالمية الشهيرة بمنتجات العناية بالبشرة."),
        ("هل يمكن استخدامه أثناء الحمل؟", "النياسيناميد والصبار مكونان آمنان موضعياً، ولكن يُفضل استشارة الطبيب المتابع أثناء الحمل."),
        ("هل يفتح اللون الطبيعي للبشرة عن حدها؟", "لا، هو يزيل التصبغات الزائدة ويستعيد لون البشرة الطبيعي وإشراقتها الأصلي."),
        ("ما هو ملمس الكريم على الوجه؟", "ملمس كريمي ناعم يخترق البشرة بسرعة دون ثقل."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "كافة منتجات إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين لشركة يونيليفر بالسعودية."),
        ("هل يلزم غسل الوجه بعد وضع الكريم؟", "لا، الكريم مخصص للبقاء على البشرة لامتصاص كافة فوائده."),
        ("هل يحتوي على فيتامينات مغذية؟", "نعم، يحتوي على فيتامين B3 (النياسيناميد) وفيتامين E المغذيان للياقة وخلايا الجلد.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Glow & Lovely Anti-Marks Face Cream (100g)</strong> is an advanced skincare solution specially formulated to reduce dark spots, acne marks, and sun-induced hyperpigmentation. Featuring Unilever's Vita-Aloe Complex powered by Niacinamide (Vitamin B3), Aloe Vera extract, and Vitamin E, this targeted daily face cream restores an even tone, vivid radiance, and healthy smoothness to your complexion.</p>
<p>Boasting a lightweight, non-greasy texture, it absorbs rapidly into skin cells while delivering broad-spectrum Triple Sunscreen protection against harmful UVA/UVB rays. Regular daily application minimizes persistent spots, prevents future tanning, and safeguards your skin against daily environmental stressors.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Targeted Dark Spot Reduction:</strong> Fades persistent acne scars, sun spots, and dark patches effectively.</li>
  <li><strong>Powered by Niacinamide (Vitamin B3):</strong> Brightens skin tone, unifies complexion, and enhances natural glow.</li>
  <li><strong>Triple Sunscreen Shield:</strong> Protects against harmful UVA and UVB rays to prevent future spot formation and tanning.</li>
  <li><strong>Hydrating Vita-Aloe Blend:</strong> Soothes and deeply moisturizes skin with Aloe Vera and antioxidant Vitamin E.</li>
  <li><strong>Non-Greasy Matte Finish:</strong> Absorbs effortlessly without leaving a sticky or oily residue.</li>
  <li><strong>Safe Daily Formula:</strong> Dermatologically tested and suitable for routine daily application.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Wash your face thoroughly with a mild cleanser and pat dry.</li>
  <li><strong>Step 2 (Apply):</strong> Dot a generous amount of cream onto your forehead, cheeks, nose, chin, and neck.</li>
  <li><strong>Step 3 (Massage):</strong> Massage gently using circular upward strokes until fully absorbed into the skin.</li>
  <li><strong>Step 4 (Repeat):</strong> Use twice daily (morning and evening) for optimal spot reduction results.</li>
  <li><strong>Step 5 (Protect):</strong> Can be applied as a lightweight hydrating base before makeup or sun exposure.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Niacinamide (Vitamin B3):</strong> Key brightening active that downregulates melanin transfer, reducing spots and unifying tone.</li>
  <li><strong>Aloe Vera Extract:</strong> Delivers calming, cooling moisture to soothe skin and diminish irritation.</li>
  <li><strong>Vitamin E (Tocopheryl Acetate):</strong> Essential antioxidant defending skin cells from environmental damage and free radicals.</li>
  <li><strong>Triple UV Filters:</strong> Absorbs and reflects solar rays to prevent UV-induced pigmentation and tanning.</li>
  <li><strong>Glycerin:</strong> Humectant that locks in skin moisture for lasting softness throughout the day.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external use on face and neck only.</li>
  <li>Avoid direct contact with eyes; rinse immediately with clean water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from direct sunlight.</li>
  <li>Discontinue use if signs of severe irritation or allergic rash develop.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Individuals dealing with dark spots, acne scars, hyperpigmentation, or uneven skin tone.</li>
  <li>Anyone seeking an everyday face cream combining spot reduction, hydration, and UV protection.</li>
  <li>Suitable for all skin types, including normal, oily, and combination skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Glow & Lovely</td></tr>
  <tr><th>Category</th><td>Skincare / Face Creams & Brightening</td></tr>
  <tr><th>Product Type</th><td>Anti-Marks Spot Reduction Face Cream</td></tr>
  <tr><th>Volume/Weight</th><td>100 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Face & Neck)</td></tr>
  <tr><th>Finish</th><td>Even-toned, radiant, non-greasy matte finish</td></tr>
  <tr><th>Texture</th><td>Lightweight fast-absorbing cream</td></tr>
  <tr><th>Fragrance</th><td>Fresh elegant floral scent</td></tr>
  <tr><th>Active Ingredients</th><td>Niacinamide (Vitamin B3), Aloe Vera, Vitamin E, Triple Sunscreens</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / India (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens (15+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Niacinamide & Spot Reduction Technology</h2>

<h3>What problem does this solve?</h3>
<p>Glow & Lovely Anti-Marks Face Cream resolves localized hyperpigmentation, post-acne dark marks, and uneven skin tone caused by sun exposure, hormonal surges, or skin inflammation.</p>

<h3>Why does this condition happen?</h3>
<p>Skin trauma, UV radiation, and acne trigger melanocytes to overproduce melanin pigment. These excess melanin deposits accumulate in the upper epidermal layers, forming stubborn dark marks that take months to fade without targeted topical intervention.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Daily Sun Protection:</strong> Apply sunscreens daily to prevent UV rays from stimulating melanin synthesis.<br>
2. <strong>Avoid Picking Blemishes:</strong> Never squeeze or pick acne to minimize post-inflammatory scarring.<br>
3. <strong>Consistent Niacinamide Application:</strong> Applying Niacinamide twice daily steadily inhibits spot darkening.<br>
4. <strong>Gentle Exfoliation:</strong> Weekly exfoliation accelerates dead skin cell shedding, fading surface marks faster.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Brightening creams bleach or thin the skin."<br>
<strong>Fact:</strong> Glow & Lovely relies on safe Niacinamide and Aloe Vera, which nourish and repair the skin barrier without chemical bleaching or thinning.</p>
<p><strong>Myth:</strong> "Dark spots vanish overnight."<br>
<strong>Fact:</strong> Safe, sustainable spot reduction requires consistent application over 2-4 weeks to align with natural epidermal cell renewal cycles.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Niacinamide (Vitamin B3) inhibits melanosome transfer from melanocytes to surrounding keratinocyte cells by up to 68%. Simultaneously, Triple Sunscreens absorb and scatter UVA/UVB rays, preventing new melanin production, while Aloe Vera and Vitamin E deliver antioxidant hydration that restores epidermal health.</p>"""

    en_faqs = [
        ("What is Glow & Lovely Anti-Marks Face Cream?", "It is a targeted facial cream formulated with Niacinamide, Aloe Vera, and Triple Sunscreens to fade dark spots and unify skin tone."),
        ("Does it help fade post-acne scars?", "Yes, daily use significantly reduces dark post-acne marks by inhibiting excess melanin accumulation."),
        ("Does this cream include sunscreen protection?", "Yes, it contains Triple Sunscreens protecting against UVA/UVB rays to prevent sun spots and tanning."),
        ("How often should I apply it?", "Apply twice daily (morning and night) onto clean skin for best spot reduction results."),
        ("Is it suitable for oily skin?", "Yes, its lightweight, non-greasy formula absorbs quickly, leaving a smooth matte finish."),
        ("How long before I see visible results?", "Visible reduction in dark marks and improved radiance typically appear within 2 to 4 weeks of regular use."),
        ("Does it contain hydroquinone or harsh chemicals?", "No, it is 100% hydroquinone-free, using safe active ingredients like Niacinamide and Aloe Vera."),
        ("Is this cream suitable for all skin types?", "Yes, it is formulated to suit normal, oily, combination, and dry skin types."),
        ("Can I apply it under makeup?", "Yes, it serves as an excellent lightweight, hydrating, non-shiny makeup base."),
        ("What size is this product packaging?", "This product comes in a generous 100g tube ideal for daily extended application."),
        ("Will it dry out my skin?", "No, Glycerin and Aloe Vera extract maintain skin hydration and softness throughout the day."),
        ("What is the relation between Glow & Lovely and Fair & Lovely?", "Glow & Lovely is the officially rebranded global name of Fair & Lovely, maintaining the same trusted quality."),
        ("Can men use Glow & Lovely Anti-Marks Cream?", "Yes, it is a unisex product that works effectively to reduce sun spots and even skin tone for men."),
        ("Should I apply it to my neck area as well?", "Yes, applying to both face and neck ensures even color distribution across all visible skin."),
        ("Does it prevent new spots from forming?", "Yes, the Triple Sunscreen system blocks UV rays, preventing new sun-induced dark marks."),
        ("Is the formula paraben-free?", "Yes, the updated formula is dermatologically safety-tested for daily use."),
        ("How should I store this cream?", "Store in a cool, dry place away from direct sunlight and heat."),
        ("Can it cause eye irritation?", "Avoid direct contact with the inner eye area during application."),
        ("Who manufactures this product?", "It is manufactured by Unilever, a trusted global leader in personal care products."),
        ("Is it safe during pregnancy?", "Topical Niacinamide and Aloe Vera are generally safe, though consulting your doctor is always recommended."),
        ("Does it bleach natural skin tone?", "No, it does not bleach skin; it removes excess spot pigmentation to restore your natural radiant skin tone."),
        ("What texture does the cream have?", "It features a soft, smooth cream texture that absorbs quickly without heaviness."),
        ("How can I ensure product authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original, sourced directly from authorized Unilever Saudi distributors."),
        ("Do I need to wash off the cream after application?", "No, the cream is designed to remain on the skin to deliver its full hydrating and spot-fading benefits."),
        ("Does it contain skin-nourishing vitamins?", "Yes, it contains Niacinamide (Vitamin B3) and Vitamin E to nourish and protect skin cells.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1692",
        "sku": "EK-1692",
        "gtin": "6281006567474",
        "category": "العناية بالبشرة / كريمات الوجه والتفتيح",
        "brand": "Glow & Lovely",
        "ar": {
            "title": "كريم الوجه مضاد للبقع من جلو اند لوفلي 100جم لتوحيد لون البشرة",
            "meta_title": "كريم جلو اند لوفلي مضاد للبقع 100جم | صيدلية إكليل أبها",
            "meta_description": "تسوقي كريم جلو اند لوفلي مضاد البقع لتفتيح البشرة وتوحيد لونها 100جم. غني بالنياسيناميد وواقيات الشمس الثلاثية. منتج أصلي من صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["جلو_اند_لوفلي", "كريم_تفتيح", "مضاد_البقع", "نياسيناميد", "إكليل_أبها"]
        },
        "en": {
            "title": "Glow & Lovely Anti-Marks Face Cream - 100g",
            "meta_title": "Glow & Lovely Anti-Marks Face Cream 100g | Ekleel Abha",
            "meta_description": "Buy Glow & Lovely Anti-Marks Face Cream (100g). Fades dark spots with Niacinamide & Triple Sunscreen. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["glow_and_lovely", "anti_marks", "niacinamide", "face_cream", "ekleel_abha"]
        },
        "schema": {
            "brand": "Glow & Lovely",
            "category": "Skincare / Face Creams",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "glow-and-lovely-anti-marks-face-cream-100g.webp",
            "alt": "Glow & Lovely Anti-Marks Face Cream 100g",
            "title": "Glow & Lovely Anti-Marks Face Cream 100g"
        }
    }

print("Loaded 1692 builder")
