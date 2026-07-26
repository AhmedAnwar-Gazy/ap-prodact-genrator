import json, os

def create_product_1696():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعتبر <strong>شامبو تلوين الشعر الأبيض بزيت الزيتون من كاترينا - أسود (Katerina Olive Oil Extract Hair Color Shampoo - Black 20 ml)</strong> حلاً عملياً وسريعاً لمشكلة الشيب والشعر الأبيض لدى الرجال والنساء. تجمع هذه التركيبة الكورية المتقدمة بين سهولة غسيل الشعر بالشامبو وفاعلية صبغة الشعر الطبيعية، مما يتيح لكِ التخلص من الشيب وتغطية الشعر الأبيض بلون أسود طبيعي لامع في غضون 5 إلى 10 دقائق فقط في المنزل.</p>
<p>تم تعزيز الفرمولة بخلاصة زيت الزيتون الطبيعي والأعشاب المغذية، وهي خالية تماماً من الأمونيا القاسية، مما يحمي الفروة وألياف الشعر من الجفاف والتلف المصاحب للصبغات التقليدية. تمنح العبوة المدمجة بحجم 20 مل كمية مثالية للاستخدام الفوري والسريع للرحلات أو للاستعمال الشخصي المتكرر دون عناء.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تغطية كاملة للشعر الأبيض في 8 دقائق:</strong> صبغة سريعة تخفي الشيب وتمنح لوناً أسوداً غنياً وطبيعياً في دقائق معدودة.</li>
  <li><strong>مدعم بخلاصة زيت الزيتون:</strong> يرطب ألياف الشعر وينعمها ويمنع الجفاف والتقصف أثناء عملية التلوين.</li>
  <li><strong>تركيبة خالية من الأمونيا:</strong> لطيفة على فروة الرأس ولا تسبب روائح قاسية أو تحسس مفرط كالصبغات التقليدية.</li>
  <li><strong>سهولة الاستخدام 2 في 1:</strong> يُطبق تماماً كالشامبو العادي دون الحاجة لأدوات صبغ معقدة أو زيارة الصالونات.</li>
  <li><strong>عبوة كيس مدمجة 20 مل:</strong> حجم عملي ومناسب للسفر والاستخدام الفوري أثناء التنقل.</li>
  <li><strong>مناسب للرجال والنساء:</strong> مثالي لتغطية الشيب في شعر الرأس أو اللحية والشارب للرجال بسهولة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التحضير والارتداء):</strong> ارتدي القفازات الواقية المرفقة وبلي شعركِ بالماء الفاتر ثم جففيه خفيفاً بالمنشفة ليكون رطباً.</li>
  <li><strong>الخطوة الثانية (فريغ الشامبو):</strong> افتاحي العبوة وافرغي كامل محتوى الشامبو 20 مل على كف اليد المرتدي للقفاز واخلطيه قليلاً.</li>
  <li><strong>الخطوة الثالثة (التوزيع والتدليك):</strong> ضعي الشامبو على الشعر ودلكي الفروة والشعر بلطف حتى تتكون رغوة غنية تغطي كافة المناطق البيضاء.</li>
  <li><strong>الخطوة الرابعة (الانتظار):</strong> اتركي الرغوة على الشعر لمدة 5 إلى 10 دقائق (يمكن إبقاؤها حتى 15 دقيقة للشعر الكثيف أو الأبيض الشديد).</li>
  <li><strong>الخطوة الخامسة (الشطف):</strong> اشطفي الشعر جيداً بالماء الفاتر فقط حتى يزول الرغوة تماماً ويظهر اللون الأسود الطبيعي.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة زيت الزيتون البكر (Olive Oil Extract):</strong> تمد الشعر بالأحماض الدهنية المرطبة لمنع الجفاف والخشونة.</li>
  <li><strong>مركب الأعشاب الطبيعية:</strong> يغذي بصلات الشعر ويمنح الخصلات لمعاناً وحيوية طبيعية.</li>
  <li><strong>صبغات التلوين السريعة الآمنة:</strong> تتغلغل في الطبقة الخارجية للشعرة لترسيب اللون الأسود الطبيعي بدقة.</li>
  <li><strong>عوامل الرغوة اللطيفة:</strong> توفر رغوة كثيفة تساعد على توزيع اللون بالتساوي دون تكتل.</li>
  <li><strong>تركيبة متوازنة خالية من الأمونيا:</strong> تحافظ على سلامة جلد الفروة وتمنع التهيج.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الشعر وفروة الرأس فقط.</li>
  <li>يُوصى بإجراء اختبار تحسس جلدي بسيط على منطقة صغيرة خلف الأذن قبل 48 ساعة من الاستخدام الكامل.</li>
  <li>تجنبي ملامسة المنتج للعينين؛ وفي حال ملامستهما اشطفي فوراً بكمية وفيرة من الماء.</li>
  <li>يجب ارتداء القفازات أثناء التطبيق لتجنب تصبغ صبغة اليدين والأظافر.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>للرجال والنساء الذين يعانون من ظهور الشعر الأبيض أو الشيب ويرغبون في تغطيته بسرعة في المنزل.</li>
  <li>لمن يبحثون عن صبغة شعر سوداء خالية من الأمونيا وغير مجهدة للشعر.</li>
  <li>لأصحاب الجداول المزدحمة الذين يحتاجون لحل تغطية الشيب في 8 دقائق دون زيارة صالون التجميل.</li>
  <li>مثالي للمسافرين بفضل عبوة الكيس 20 مل المدمجة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كاترينا (Katerina)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / شامبو وصبغات الشعر</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو صبغة لتغطية الشيب (أسود)</td></tr>
  <tr><th>الحجم/الوزن</th><td>20 مل (عبوة كيس مدمجة)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (الشعر الأبيض والشائب)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر أسود طبيعي، لامع، وخالٍ من الشيب</td></tr>
  <tr><th>الملمس</th><td>شامبو كريمي يرغي بسهولة</td></tr>
  <tr><th>العطر</th><td>عطر عشب زيت الزيتون الناعم</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة زيت الزيتون، صبغات طبيعية سريعة، مستخلصات عشبية كورية</td></tr>
  <tr><th>بلد المنشأ</th><td>كوريا الجنوبية / الصين</td></tr>
  <tr><th>الشركة المصنعة</th><td>Katerina Hair Care</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين (الرجال والنساء)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لتقنية شامبو صبغ الشعر وتغطية الشيب (Katerina)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج شامبو صبغة كاترينا بزيت الزيتون مشكلة ظهور الشيب والشعر الأبيض المبكر، ويغني عن جلسات الصبغ الطويلة والمكلفة في الصالونات، كما يحل مشكلة تلف الشعر الناتج عن الصبغات الكيميائية المحتوية على الأمونيا.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>يحدث الشيب نتيجة توقف خلايا الميلانوسيت في بصلات الشعر عن إنتاج صبغة الميلانين الطبيعية بفعل التقدم في السن، الجينات، أو التوتر. الصبغات التقليدية تستخدم الأمونيا لفتح حراشف الشعر بالقوة مما يسبب جفاف وتقصف الشعر.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>اختبار التحسس:</strong> جربي قطرة صغيرة خلف الأذن قبل 48 ساعة للتأكد من عدم وجود حساسية.<br>
2. <strong>ارتداء القفازات:</strong> ارتدي القفازات دائماً لمنع تصبغ الأظافر أو الجلد.<br>
3. <strong>التدليك بالتساوي:</strong> دلكي الشامبو لضمان تغطية كاملة لجذور الشعر والشيب.<br>
4. <strong>عدم تجاوز الوقت:</strong> التزمي بـ 8 إلى 10 دقائق للحصول على اللون الأسود الطبيعي المثالي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "شامبو الصبغة يسبب تساقط الشعر ويجففه."<br>
<strong>الحقيقة:</strong> شامبو كاترينا خالٍ من الأمونيا ومدعم بزيت الزيتون الذي يرطب الشعرة ويحمي الفروة بعكس الصبغات القاسية.</p>
<p><strong>خرافة:</strong> "اللون الأسود يزول فور الغسلة الأولى."<br>
<strong>الحقيقة:</strong> تتغلغل صبغات الشامبو المتقدمة في طبقات الشعرة لتمنح لوناً ثابتاً يدوم لعدة أسابيع.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعتمد المنتج على تقنية الترسيب الدقيق للصبغة (Micro-Pigment Deposition). عند تدليك الشامبو مع الماء الفاتر، تقوم العوامل اللطيفة بتنظيف السطح الخارجي للشعرة، بينما تنفذ الصبغات الدقيقة المدعومة بزيت الزيتون إلى المسام السطحية لطبقة القشرة دون الحاجة لفتح حراشف الشعر بالأمونيا، مما يثبت اللون الأسود ويرطب ألياف الشعر في آن واحد.</p>"""

    faqs = [
        ("ما هو شامبو صبغة الشعر كاترينا بزيت الزيتون؟", "هو شامبو مخصص لتغطية الشعر الأبيض والشيب بلون أسود طبيعي في 5 إلى 10 دقائق فقط، مدعم بزيت الزيتون وخالٍ من الأمونيا."),
        ("كم من الوقت يحتاج الشامبو لتغطية الشيب؟", "يحتاج من 5 إلى 10 دقائق فقط على الشعر الرطب للحصول على تغطية كاملة للشعر الأبيض."),
        ("هل يسبب الشامبو جفافاً أو تلفاً للشعر؟", "لا، لأنه خالٍ من الأمونيا ومدعم بخلاصة زيت الزيتون التي ترطب وتغذي ألياف الشعر أثناء التلوين."),
        ("هل يناسب شامبو صبغة كاترينا الرجال والنساء؟", "نعم، هو مناسب جداً لكلا الجنسين ويمكن استخدامه لشعر الرأس أو اللحية والشارب للرجال."),
        ("ما هي كيفية تطبيق الشامبو بشكل صحيح؟", "بلي شعركِ بالماء وجففيه خفيفاً، ارتدي القفازات وضعي الشامبو ودلكيه حتى تتكون رغوة غنية، اتركيها 8-10 دقائق ثم اشطفي بالماء."),
        ("هل يلزم ارتداء القفازات أثناء التطبيق؟", "نعم، يلزم ارتداء القفازات لتجنب تصبغ اليدين والأظافر باللون الأسود."),
        ("كم تدوم النتيجة واللون الأسود على الشعر؟", "يدوم اللون الأسود الطبيعي لعدة أسابيع تبعاً لمعدل غسيل الشعر ونموه."),
        ("ما حجم عبوة شامبو كاترينا؟", "تأتي العبوة بحجم كيس مدمج 20 مل، وهي مثالية للاستخدام المرة الواحدة أو السفر."),
        ("هل يحتوي المنتج على أمونيا؟", "لا، التركيبة خالية تماماً من الأمونيا لحماية الفروة والشعر من التلف والروائح النافذة."),
        ("هل يمكن استخدام الشامبو على اللحية والشارب للرجال؟", "نعم، ممتاز لتغطية شيب اللحية والشارب بسرعة ودون تحسس."),
        ("هل يجب غسل الشعر بشامبو عادي بعد الصبغة؟", "لا، يكفي شطف الشعر بالماء الفاتر جيداً حتى زوال الرغوة تماماً."),
        ("ماذا أفعل إذا لامس الشامبو الجلد أو الجبين؟", "امسحيه فوراً بمنديل مبلل قبل أن يجف لتجنب ترك أي بقع على الجلد."),
        ("هل يناسب جميع أنواع الشعر؟", "نعم، مناسب للشعر الجاف، العادي، والدهني ويمتاز بفاعلية عالية على كافة الأنسجة."),
        ("هل يحتاج لأي محسن أو هيدروجين مخلوط معه؟", "لا، هو جاهز للاستخدام المباشر دون الحاجة لمزجه مع أي بروكسيد أو هيدروجين."),
        ("ما هو بلد صنع شامبو كاترينا؟", "صُنع في كوريا الجنوبية وفق أعلى معايير الجودة للعناية بالشعر."),
        ("هل يسبب الشامبو تساقط الشعر؟", "لا، تركيبته المغذية بزيت الزيتون تحافظ على صحة البصلات ولا تسبب تساقط الشعر."),
        ("كم مرة يُنصح باستخدام الشامبو؟", "يُستخدم كلما ظهر الشيب مجدداً أو كل 2 إلى 3 أسابيع حسب الحاجة."),
        ("هل يمكن استخدامه للشعر المصبوغ سابقاً؟", "نعم، يوحد لون الشعر ويغطي الشيب والدرجات المتفاوتة باللون الأسود الطبيعي."),
        ("هل يعاد استخدام الكيس بعد الفتح؟", "الكيس بحجم 20 مل مخصص للاستخدام الفوري الكامل لضمان الفاعلية."),
        ("هل يحتاج اختبار تحسس قبل الاستخدام؟", "نعم، يُنصح دائماً بإجراء اختبار تحسس على جلد ساعد اليد أو خلف الأذن قبل 48 ساعة."),
        ("ما هي رائحة الشامبو؟", "يتميز برائحة ناعمة ولطيفة بزيت الزيتون دون روائح نفاذة كالصبغات التقليدية."),
        ("هل يصبغ فروة الرأس؟", "إذا دُلك جيداً وتكونت رغوة وافيرة، يُغسل بالماء دون تصبغ دائم للفروة."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات كاترينا لدى صيدلية إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يغطي الشيب الشديد جداً؟", "نعم، للشعر الأبيض الشديد يُفضل إبقاء الرغوة لمدة 12-15 دقيقة للحصول على تغطية قاتمة ومكتملة."),
        ("هل يناسب الشعر المعالج بالكيراتين أو البروتين؟", "نعم، لخلوه من الأمونيا والمواد الكيميائية القاسية التي تبطل علاجات البروتين.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Katerina Olive Oil Extract Hair Color Shampoo - Black (20 ml)</strong> offers a revolutionary, fast, and effortless solution for covering gray and white hair for both men and women. Combining the convenience of a daily hair wash with the coverage of a rich permanent hair dye, this Korean formulation turns gray hair into a glossy, natural black shade in just 5 to 10 minutes from the comfort of your home.</p>
<p>Enriched with pure Olive Oil extract and natural botanical herbs, this hair color shampoo is 100% ammonia-free. It protects the scalp and hair fibers against dryness, brittleness, and damage associated with harsh chemical dyes. Packed in a compact 20ml pouch, it is an ideal portable single-use solution for travel or quick root touch-ups on the go.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Full Gray Coverage in 8 Minutes:</strong> Quickly covers white hair and imparts a rich, natural black shade in minutes.</li>
  <li><strong>Enriched with Olive Oil Extract:</strong> Deeply conditions hair fibers, retaining moisture and preventing post-color dryness.</li>
  <li><strong>100% Ammonia-Free Formula:</strong> Gentle on the scalp, free of harsh chemical fumes and aggressive irritants.</li>
  <li><strong>2-in-1 Shampoo Convenience:</strong> Applies easily like regular shampoo without complex mixing bowls or salon visits.</li>
  <li><strong>Compact 20ml Travel Pouch:</strong> Ultra-portable format perfect for business trips, travel, and immediate root touch-ups.</li>
  <li><strong>Unisex Application:</strong> Ideal for men and women; excellent for scalp hair, beards, and mustaches.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Prep & Glove):</strong> Put on the included protective gloves; dampen hair with warm water and lightly towel-dry.</li>
  <li><strong>Step 2 (Dispense):</strong> Open the 20ml pouch and pour the entire shampoo content onto gloved palms; mix slightly.</li>
  <li><strong>Step 3 (Massage):</strong> Apply to hair and massage thoroughly into a rich lather covering all gray strands completely.</li>
  <li><strong>Step 4 (Wait):</strong> Allow lather to process for 5 to 10 minutes (up to 15 minutes for dense or resistant white hair).</li>
  <li><strong>Step 5 (Rinse):</strong> Rinse hair thoroughly with warm water until the water runs clear and natural black color is revealed.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Virgin Olive Oil Extract:</strong> Supplies essential fatty acids to condition cuticles and prevent post-dye dryness.</li>
  <li><strong>Natural Botanical Herb Complex:</strong> Nourishes hair roots and imparts a healthy, natural shine to strands.</li>
  <li><strong>Safe Quick Color Pigments:</strong> Deposit rich black color into the outer hair shaft safely and evenly.</li>
  <li><strong>Gentle Surfactants:</strong> Produce a luxurious foam that ensures uniform color distribution across every strand.</li>
  <li><strong>Ammonia-Free Base:</strong> Preserves scalp health and prevents aggressive skin irritation or redness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external use on hair and scalp only.</li>
  <li>Perform a skin patch test behind the ear 48 hours prior to full application.</li>
  <li>Avoid direct contact with eyes; rinse immediately with plenty of water if contact occurs.</li>
  <li>Always wear protective gloves during application to prevent temporary staining of hands and nails.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Men and women looking to cover gray or white hair quickly and conveniently at home.</li>
  <li>Anyone seeking an ammonia-free, non-damaging black hair color solution.</li>
  <li>Busy individuals needing full gray coverage in 8 minutes without visiting a hair salon.</li>
  <li>Travelers wanting a compact 20ml portable hair coloring sachet.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Katerina</td></tr>
  <tr><th>Category</th><td>Hair Care / Hair Color & Shampoo</td></tr>
  <tr><th>Product Type</th><td>Ammonia-Free Gray Coverage Hair Color Shampoo</td></tr>
  <tr><th>Volume/Weight</th><td>20 ml (Compact Pouch)</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Gray & White Hair)</td></tr>
  <tr><th>Finish</th><td>Natural black, shiny, gray-free hair</td></tr>
  <tr><th>Texture</th><td>Creamy lathering shampoo</td></tr>
  <tr><th>Fragrance</th><td>Subtle fresh olive herbal aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Olive Oil Extract, Fast Natural Pigments, Herbal Extracts</td></tr>
  <tr><th>Country of Origin</th><td>South Korea</td></tr>
  <tr><th>Manufacturer</th><td>Katerina Hair Care</td></tr>
  <tr><th>Age Group</th><td>Adults (Men & Women)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Ammonia-Free Hair Darkening Shampoos</h2>

<h3>What problem does this solve?</h3>
<p>Katerina Olive Oil Hair Color Shampoo resolves graying hair and white root growth quickly without requiring long salon sessions or subjecting hair cuticles to harsh ammonia dyes.</p>

<h3>Why does this condition happen?</h3>
<p>Graying occurs when hair follicle melanocytes reduce melanin synthesis due to aging, genetics, or oxidative stress. Conventional permanent hair dyes use high levels of ammonia to swell and open cuticles aggressively, leading to severe moisture loss and brittleness.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Perform a Patch Test:</strong> Test a small dab behind the ear 48 hours before full use.<br>
2. <strong>Wear Gloves:</strong> Always wear gloves to prevent temporary hand skin and nail staining.<br>
3. <strong>Massage Evenly:</strong> Work into a rich foam to ensure uniform coverage across all roots.<br>
4. <strong>Timer Accuracy:</strong> Maintain a 8-10 minute development time for a natural black result.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Hair color shampoos cause severe hair loss and dryness."<br>
<strong>Fact:</strong> Katerina shampoo is 100% ammonia-free and infused with Olive Oil, which hydrates and protects hair fibers during coloring.</p>
<p><strong>Myth:</strong> "Shampoo color washes out after a single shower."<br>
<strong>Fact:</strong> Micro-pigment technology deposits deep within outer cuticle layers, maintaining rich black color for several weeks.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>This formulation utilizes Micro-Pigment Deposition technology. As the gentle shampoo surfactants cleanse surface oils, micro-pigments suspended with Olive Oil lipids adhere onto outer cortex micro-crevices. Because no ammonia is present to strip internal structural proteins, the Olive Oil seals the cuticle layer smoothly, locking in rich black color while preserving hair elasticity.</p>"""

    en_faqs = [
        ("What is Katerina Olive Oil Hair Color Shampoo?", "It is an ammonia-free hair darkening shampoo enriched with Olive Oil that covers gray hair in a natural black shade in 5 to 10 minutes."),
        ("How long does it take to cover gray hair?", "It requires only 5 to 10 minutes of processing time on damp hair to achieve full natural black gray coverage."),
        ("Does it damage or dry out hair?", "No, it is 100% ammonia-free and infused with Olive Oil to condition and hydrate hair strands during coloring."),
        ("Is Katerina Hair Color Shampoo suitable for both men and women?", "Yes, it is a unisex formula perfect for scalp hair, beards, and mustaches."),
        ("How do I apply the shampoo correctly?", "Dampen hair, wear gloves, lather the shampoo thoroughly into hair for 8-10 minutes, then rinse completely with warm water."),
        ("Are gloves required during application?", "Yes, protective gloves prevent temporary black staining of palms and nails."),
        ("How long does the black color last?", "The natural black color stays vibrant for several weeks depending on wash frequency and new hair growth."),
        ("What size is the product packaging?", "It comes in a compact, travel-friendly 20ml single-use sachet pouch."),
        ("Is the formula free of ammonia?", "Yes, it is 100% ammonia-free, eliminating harsh fumes and scalp irritation."),
        ("Can men use it on beards and mustaches?", "Yes, it provides fast, gentle gray coverage for facial hair without skin irritation."),
        ("Do I need to wash with regular shampoo afterward?", "No, simply rinse thoroughly with warm water until the water runs clear."),
        ("What if the product touches skin or forehead?", "Wipe off immediately with a damp tissue before it dries to prevent temporary skin staining."),
        ("Is it suitable for all hair types?", "Yes, it works effectively on dry, normal, oily, or coarse hair textures."),
        ("Does it require developer or peroxide mixing?", "No, it is ready for immediate application straight from the sachet without developers."),
        ("Where is Katerina Hair Color Shampoo manufactured?", "It is manufactured in South Korea following premium hair care standards."),
        ("Does it cause hair fall?", "No, the ammonia-free formula with nourishing Olive Oil protects hair follicles and shaft health."),
        ("How often should I use this shampoo?", "Use whenever gray roots reappear or every 2 to 3 weeks as needed."),
        ("Can it be used on previously dyed hair?", "Yes, it unifies uneven tones and covers gray roots with a uniform natural black shade."),
        ("Is the sachet reusable after opening?", "The 20ml sachet is designed for single full-application to ensure peak pigment efficacy."),
        ("Is a patch test recommended?", "Yes, always perform a patch test behind the ear 48 hours prior to full use."),
        ("What fragrance does the shampoo have?", "It features a mild, pleasant olive herbal aroma without chemical fumes."),
        ("Does it stain the scalp permanently?", "No, thorough massaging into a lather allows clean rinsing off the scalp with water."),
        ("How do I verify product authenticity at Ekleel Abha?", "All Katerina products at Ekleel Abha are 100% original, imported from certified distributors."),
        ("Will it cover very resistant white hair?", "Yes, for resistant white hair, leave the lather on for 12 to 15 minutes before rinsing."),
        ("Is it safe for keratin or protein-treated hair?", "Yes, its ammonia-free composition preserves keratin and protein treatments.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1696",
        "sku": "EK-1696",
        "gtin": "6959222300099",
        "category": "العناية بالشعر / شامبو وصبغات الشعر",
        "brand": "Katerina",
        "ar": {
            "title": "شامبو تلوين الشعر الأبيض بزيت الزيتون من كاترينا - أسود (20 مل)",
            "meta_title": "شامبو صبغة كاترينا اسود بزيت الزيتون 20مل | صيدلية إكليل أبها",
            "meta_description": "اشتري شامبو تلوين الشعر الأبيض بزيت الزيتون من كاترينا أسود (20مل). تغطية كاملة للشيب في 8 دقائق خالي من الأمونيا. منتج أصلي من صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["كاترينا", "شامبو_صبغة", "تغطية_الشيب", "زيت_الزيتون", "إكليل_أبها"]
        },
        "en": {
            "title": "Katerina Olive Oil Extract Hair Color Shampoo - Black, 20 ml",
            "meta_title": "Katerina Olive Oil Hair Color Shampoo Black 20ml | Ekleel Abha",
            "meta_description": "Buy Katerina Olive Oil Extract Hair Color Shampoo Black (20ml). Ammonia-free full gray coverage in 8 minutes. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["katerina", "hair_color_shampoo", "gray_coverage", "olive_oil", "ekleel_abha"]
        },
        "schema": {
            "brand": "Katerina",
            "category": "Hair Care / Hair Color Shampoo",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "katerina-olive-oil-extract-hair-color-shampoo-black-20ml.webp",
            "alt": "Katerina Olive Oil Extract Hair Color Shampoo Black 20ml",
            "title": "Katerina Olive Oil Extract Hair Color Shampoo Black 20ml"
        }
    }

print("Loaded 1696 builder")
