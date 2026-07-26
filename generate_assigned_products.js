const fs = require('fs');
const path = require('path');

const targetDir = path.join(__dirname, 'temp/generated_products');
if (!fs.existsSync(targetDir)) {
  fs.mkdirSync(targetDir, { recursive: true });
}

// Product 1411: Stridex Acne Treatment Cotton Pads - 90 Pads (Red Box - Maximum 2% Salicylic Acid)
const prod1411 = {
  "product_id": "1411",
  "sku": "EK-1411",
  "category": "العناية بالبشرة / علاجات حب الشباب والمسحات",
  "brand": "Stridex",
  "ar": {
    "title": "مسحات علاج حب الشباب القطنية من ستريديكس 90 قطعة - التركيز الأقصى 2% حمض الساليسليك",
    "meta_title": "مسحات ستريديكس لعلاج حب الشباب 90 قطعة (ماكسيموم 2%) | إكليل أبها",
    "meta_description": "تسوقي مسحات ستريديكس القطنية ماكسيموم 2% حمض ساليسليك (90 مسحة) لعلاج حب الشباب وتنظيف المسام بعمق. خالية من الكحول. أصلي 100% من صيدلية إكليل أبها.",
    "description": `<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>مسحات ستريديكس القطنية لعلاج حب الشباب بالتركيز الأقصى (Stridex Maximum Strength Acne Control Pads 90 Count)</strong> العلاج الموضعي الأكثر شهرة واعتماداً عالمياً للتخلص من حب الشباب والبثور والرؤوس السوداء. تحتوي هذه العبوة الاقتصادية على 90 مسحة قطنية ناعمة مشبعة بتركيز 2% من حمض الساليسليك (BHA)، وهو التركيز الأقصى المسموح به طبياً دون وصفة طبية. تم تصنيف هذا المنتج خصيصاً ليمنح نتائج علاجية سريعة وملموسة للبشرة الدهنية والمعرضة للحبوب دون التسبب في التهيج الشديد الذي تسببه العلاجات الكيميائية القاسية.</p>
<p>تتميز مسحات ستريديكس بتركيبة <strong>خالية تماماً من الكحول (100% Alcohol-Free)</strong>، مما يعالج حب الشباب بفعالية دون تجريد البشرة من رطوبتها الطبيعية أو التسبب في جفاف قاسي أو حرق كيميائي. تقوم المسحات الثلاثية الفعالية بتنظيف الجلد، فتح المسام المسدودة، وإذابة الدهون الزائدة وتفكيك الخلايا الميتة المتراكمة داخل المسام، مما يضمن منع تكون بثور جديدة وحماية البشرة واستعادة نضارتها ونقائها.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>مفعول ثلاثي متكامل (Clean, Treat, Prevent):</strong> تنظف البشرة، تعالج الحبوب القائمة، وتمنع تفشي البثور والرؤوس السوداء مستقبلاً.</li>
  <li><strong>أقصى تركيز طبي بدون وصفة (2% Salicylic Acid):</strong> يتغلغل حمض الساليسليك الذائب في الدهون إلى عمق المسام لإذابة الزهم الملتصق وجدران الخلايا الميتة.</li>
  <li><strong>تركيبة خالية تماماً من الكحول:</strong> تمنع الجفاف الشديد والحرقة والتهيج الذي تسببه المسحات التقليدية المعبأة بالكحول.</li>
  <li><strong>تنظيف ميكانيكي وكيميائي مزدوج:</strong> الملمس القطني المصمم بعناية يساعد في إزالة الشوائب والدهون السطحية أثناء المسح، بينما يعمل الحمض كيميائياً داخل المسام.</li>
  <li><strong>عبوة توفيرية ممتازة (90 قطعة):</strong> تكفي لاستخدام يومي منتظم لفترة طويلة لتغطية الوجه ومناطق الجسم المعرضة للحبوب مثل الظهر والصدر.</li>
</ul>

<h2>طريقة الاستخدام الطبية</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> اغسلي الوجه جيداً باستخدام غسول لطيف مناسب ونشفي البشرة تماماً قبل التطبيق.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> خذي مسحة قطنية واحدة وامسحي بها المنطقة المصابة بحب الشباب أو الوجه بالكامل بلطف، مع تجنب منطقة العينين والشفتين.</li>
  <li><strong>الخطوة الثالثة (التدرج في الاستخدام):</strong> ابدئي باستعمال مسحة واحدة يومياً في البداية للتقييم، ثم زيدي الاستخدام إلى مرتين أو ثلاث مرات يومياً إذا لزم الأمر أو حسب توجيهات الطبيب/الصيدلي.</li>
  <li><strong>الخطوة الرابعة (الترطيب بعد الجفاف):</strong> اتركي السائل يجف طبيعياً على البشرة دون غسله بالماء، ثم اتبعيه بمرطب خفيف خالٍ من الزيوت (Oil-Free Moisturizer).</li>
  <li><strong>الخطوة الخامسة (الوقاية من الجفاف):</strong> في حال حدوث تقشر خفيف أو جفاف، يقلل الاستخدام إلى مرة واحدة يومياً أو يوم بعد يوم.</li>
</ul>

<h2>نظرة عامة على المكونات الفعالة</h2>
<p>المكون النشط الرئيسي هو <strong>حمض الساليسليك (Salicylic Acid 2.0% w/w)</strong>، وهو أحمض بيتا هيدروكسي (BHA) محب للدهون (Lipophilic) يستطيع اختراق الزهم الإفرازي داخل المسام وتفكيك الروابط بين الخلايا الميتة. كما تحتوي التركيبة على منظفات لطيفة خالية من الصابون ومواد مرطبة وموازنة لدرجة حموضة الجلد لضمان أقصى درجات التحمل دون إحداث تهيج.</p>

<h2>تحذيرات واحتياطات طبية</h2>
<ul>
  <li>للاستخدام الظاهري الموضعي فقط على الجلد. تجنبي ملامسة العينين والغشاء المخاطي للشفتين والأنف.</li>
  <li>قد يحدث تهيج خفيف أو تقشر للبشرة عند بدء الاستخدام، وهذا أمر طبيعي متوقع؛ وفي حال التهيج الشديد يجب تقليل التردد أو التوقف مؤقتاً.</li>
  <li>استخدام علاجات موضعية أخرى لحب الشباب بالتزامن مع هذا المنتج قد يسبب زيادة الجفاف أو التهيج. في هذه الحالة، استخدمي منتجاً واحداً فقط ما لم يوجهك الطبيب بخلاف ذلك.</li>
  <li>يحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعبوة مغلقة جيداً لمنع جفاف المسحات القطنية.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<p>مصمم خصيصاً للبالغين والمراهقين من أصحاب البشرة الدهنية والمختلطة والمعرضة لحب الشباب الشديد أو المتوسط، والرؤوس السوداء والبيضاء والمسام الواسعة. كما يناسب الأشخاص الذين يعانون من حب الشباب في الجسم (ظهر وأكتاف) ويبحثون عن مسحات سهلة وسريعة الاستخدام.</p>`,
    "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>Stridex (ستريديكس)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / علاجات حب الشباب والمسحات</td></tr>
  <tr><th>نوع المنتج</th><td>مسحات قطنية علاجيّة لحب الشباب خالية من الكحول</td></tr>
  <tr><th>الحجم/الوزن</th><td>90 مسحة قطنية (90 Soft-Touch Pads)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الدهنية والمختلطة والمعرضة لحب الشباب</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة صافية، مطفأة، وخالية من اللمعان والدهون</td></tr>
  <tr><th>الملمس</th><td>مسحات قطنية مبللة بسائل رقيق</td></tr>
  <tr><th>العطر</th><td>عطر نظيف خفيف (Clean Fragrance)</td></tr>
  <tr><th>المكونات النشطة</th><td>حمض الساليسليك 2.0% (Salicylic Acid 2% BHA)</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة الأمريكية (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Blistex Inc.</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (12 سنة فما فوق)</td></tr>
</tbody>
</table>`,
    "knowledge_base": `<h2>الدليل المعرفي الطبي لعلاج حب الشباب وتقشير المسام بحمض الساليسليك</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج مسحات ستريديكس ماكسيموم مشكلة حب الشباب الشائع (Acne Vulgaris)،انسداد المسام، التكيسات الدهنية الصغيرة، والرؤوس السوداء والبيضاء (Comedones). كما تقلل من التجمع الدهني واللمعان الزائد في مناطق الجبهة والأنف والذقن (T-Zone).</p>

<h3>لماذا تحدث مشكلة انسداد المسام وحب الشباب؟</h3>
<p>تنشأ البثور عندما تتحد الإفرازات الدهنية الزائدة (الزهم) التي تفرزها الغدد الدهنية مع خلايا الجلد الميتة التي لا تتساقط بشكل طبيعي. يؤدي هذا المزيج اللزج إلى سد فوهة المسام، مما يحبس الدهون بالداخل ويخلق بيئة لاهوائية مثالية لتكاثر بكتيريا حب الشباب (Cutibacterium acnes). تتغذى هذه البكتيريا على الدهون وتفرز مواد تهيجية تؤدي إلى احمرار المسام وانتفاخها وتكون البثور الصديدية.</p>

<h3>نصائح وقائية لروتين البشرة المعرضة للحبوب</h3>
<p>1. <strong>المواظبة على التقشير بـ BHA:</strong> حمض الساليسليك يذوب في الدهون مما يجعله المقشر الوحيد القادر على دخول المسام وإذابة سدادات الزهم.<br>2. <strong>اختيار منتجات خالية من الكحول:</strong> الكحول يسبب جفافاً مؤقتاً متبوعاً بإفراز دهني عكسي مضاعف، لذا يفضل استخدام تركيبات ستريديكس الخالية من الكحول.<br>3. <strong>استخدام مرطب خفيف خالٍ من الزيوت:</strong> التقشير يتطلب ترطيباً موازناً بحمض الهيالورونيك أو النياسيناميد لحماية حاجز البشرة.<br>4. <strong>استخدام واقي الشمس صباحاً:</strong> الأحماض المقشرة تجعل الجلد أكثر حساسية لأشعة الشمس، لذا يلزم تطبيق واقي شمس SPF 50 daily.</p>

<h3>توصيات الخبراء والصيادلة</h3>
<p>يوصي أطباء الجلدية باستخدام مسحات ستريديكس 2% كخطوة أساسية في خطة علاج حب الشباب المتكاملة. إذا كنت تبدأ استخدام حمض الساليسليك لأول مرة، يُنصح بتطبيق المسحة مرة واحدة كل يومين خلال الأسبوع الأول لبناء تحمل الجلد، ثم زيادة التردد تدريجياً. كما يمكن استعمال هذه المسحات بفعالية على منطقة أعلى الصدر والظهر والأكتاف لعلاج حب الشباب الجلدي بالكامل.</p>

<h3>خرافات شائعة حول تقشير البشرة وحب الشباب</h3>
<p><strong>خرافة:</strong> "مسح الوجه بشدة وقسوة بالمسحات القطنية يزيل حب الشباب بسرعة أكبر."<br><strong>الحقيقة:</strong> الاحتكاك القوي والفرك الشديد يسبب تمزقات ميكروية في جدار البشرة ويفاقم التهاب الحبوب. المضمون هو التأثير الكيميائي لـ Salicylic Acid، لذا يكفي مسح البشرة بلطف شديد دون ضغط.</p>

<h3>التفسير العلمي لآلية العمل (Salicylic Acid 2% BHA)</h3>
<p>ينتمي حمض الساليسليك إلى عائلة أحماض البيتا هيدروكسي (BHA). تمتاز هذه العائلة بخصائصها المحبة للدهون (Lipophilic)، مما يمنحها القدرة الفريدة على اختراق الغشاء الزيتي الذي يسد المسام. بمجرد دخوله، يكسر حمض الساليسليك الروابط الديسكوسومية (Desmosomes) التي تربط خلايا الجلد الميتة ببعضها، مما يسمح بتساقطها بسهولة وإذابة الرؤوس السوداء وخفض مستويات التهاب الأنسجة بفضل تركيبته الشبيهة بالأسبيرين.</p>`,
    "faqs": `<h3>ما هي مسحات ستريديكس ماكسيموم 90 قطعة؟</h3>
<p>هي مسحات قطنية علاجية مشبعة بتركيز 2% من حمض الساليسليك الخالي من الكحول، تصمم لتنظيف المسام بعمق وعلاج حب الشباب والرؤوس السوداء للوجه والجسم.</p>
<h3>ما نسبة حمض الساليسليك في العبوة الحمراء؟</h3>
<p>تحتوي العبوة الحمراء (Maximum Strength) على نسبة 2% من حمض الساليسليك، وهي أعلى نسبة طبية مسموح بها بدون وصفة طبية للحصول على أقصى فعالية.</p>
<h3>هل تحتوي مسحات ستريديكس الحمراء على الكحول؟</h3>
<p>لا، جميع مسحات ستريديكس خالية تماماً من الكحول (100% Alcohol-Free)، مما يمنع الشعور بالحرقان والجفاف الشديد المزعج.</p>
<h3>كم مرة يجب استخدام المسحات في اليوم؟</h3>
<p>يُنصح بالبدء بمرة واحدة يومياً، ويمكن زيادة التردد إلى مرتين أو ثلاث مرات يومياً حسب تحمل البشرة وحاجة الحبوب، أو وفق توجيهات الصيدلي.</p>
<h3>هل يجب غسل الوجه بالماء بعد استخدام المسحة؟</h3>
<p>لا، لا يُغسل الوجه بعد المسح. يترك سائل حمض الساليسليك ليمتص ويجف على البشرة طبيعياً ليمارس مفعوله العلاجي داخل المسام.</p>
<h3>هل يوضع المرطب بعد استخدام مسحات ستريديكس؟</h3>
<p>نعم، بعد أن يجف السائل تماماً على الوجه، يجب وضع مرطب خفيف خالٍ من الزيوت لحماية حاجز البشرة ومنع حدوث أي تقشر أو جفاف.</p>
<h3>هل تصلح مسحات ستريديكس لعلاج الرؤوس السوداء والبيضاء؟</h3>
<p>نعم بامتياز، حمض الساليسليك ذائب في الدهون ويدخل المسام مباشرة ليذوب سدادات الزهم والخلايا الميتة المسببة للرؤوس السوداء والبيضاء.</p>
<h3>هل يمكن استخدام مسحات ستريديكس لحب الشباب في الظهر والصدر؟</h3>
<p>نعم، العبوة تحتوي على 90 مسحة قطنية وتعتبر مثالية ومريحة جداً لمسح المناطق الواسعة في الجسم مثل الظهر والكتفين والصدر لعلاج حب الشباب.</p>
<h3>ما الفرق بين العبوة الحمراء والعبوة الزرقاء من ستريديكس؟</h3>
<p>العبوة الحمراء تحتوي على 2% حمض ساليسليك (أقصى تركيز للحالات المتوسطة والشديدة)، بينما العبوة الزرقاء تحتوي على 1% حمض ساليسليك مع فيتامينات مهدئة للبشرة الحساسة.</p>
<h3>هل تناسب مسحات ستريديكس الحمراء البشرة الحساسة؟</h3>
<p>البشرة شديدة الحساسية قد تجد تركيز 2% قوياً في البداية. يُفضل أصحاب البشرة الحساسة البدء بالعبوة الزرقاء (1%) أو استخدام العبوة الحمراء يوم بعد يوم.</p>
<h3>متى تظهر نتائج استخدام ستريديكس؟</h3>
<p>تبدأ التحسنات الأوليّة في ملمس البشرة وقلة اللمعان خلال 3 إلى 7 أيام، بينما تنظيف المسام وتراجع حب الشباب الشديد يظهر بشكل ملحوظ خلال 2 إلى 4 أسابيع من الاستخدام المنتظم.</p>
<h3>هل تسبب مسحات ستريديكس خروج حبوب جديدة في البداية (Purging)؟</h3>
<p>نعم، قد يحدث تقشير وتسريع لظهور الحبوب الكامنة تحت الجلد خلال أول أسبوعين (مرحلة التطهير Purging)، وهو أمر طبيعي يعقبه صفاء تام للبشرة.</p>
<h3>هل يمكن استخدام مسحات ستريديكس أثناء الحمل أو الرضاعة؟</h3>
<p>حمض الساليسليك الموضعي بتركيز 2% على مساحات صغيرة يُعتبر آمناً عموماً، ولكن يُنصح دائماً باستشارة الطبيب المتابع للحمل قبل استخدام أي حمض مقشر.</p>
<h3>هل تسبب مسحات ستريديكس زيادة الحساسية للشمس؟</h3>
<p>نعم، الأحماض المقشرة تجعل البشرة أكثر تأثراً بأشعة الشمس، لذا يجب تطبيق واقي شمس واسع الطيف SPF 50 نهاراً أثناء فترة العلاج.</p>
<h3>هل يمكن استخدام ستريديكس مع غسول يحتوي على أحماض أخرى؟</h3>
<p>يُفضل استخدام غسول لطيف خالٍ من الأحماض المقشرة القوية عند استخدام ستريديكس 2% لتجنب إجهاد البشرة وتدمير حاجز الجلد الطبيعي.</p>
<h3>هل يمكن استخدام المسحات لعلاج الشعر المنغرز تحت الجلد (Ingrown Hair)؟</h3>
<p>نعم، مسح مناطق الحلاقة أو خط البكيني بمسحات ستريديكس يمنع انسداد المسام ويقلل تكون الحبوب والشعر المنغرز بفعالية عالية.</p>
<h3>هل يجب مسح الوجه بقوة وإصرار بالقطنة؟</h3>
<p>لا، يجب مسح البشرة برفق ولطف شديد دون فرك حاد تجنباً لتهيج الأنسجة أو خدش الجلد.</p>
<h3>كيف يتم تخزين عبوة ستريديكس 90 مسحة؟</h3>
<p>يجب إغلاق الغطاء البلاستيكي بإحكام فور أخذ المسحة، وتخزين العبوة في مكان بارد وجاف بعيداً عن حرارة الشمس المباشرة لضمان عدم جفاف القطن.</p>
<h3>هل العبوة تحتوي على 90 قطعة تكفي لفترة طويلة؟</h3>
<p>نعم، 90 مسحة قطنية تكفي لمدة 3 أشهر عند الاستخدام مرة واحدة يومياً، مما يجعلها خياراً اقتصادياً وعلاجياً ممتازاً.</p>
<h3>هل يناسب هذا المنتج الرجال أيضاً؟</h3>
<p>نعم، مناسب جداً للرجال والنساء على حد سواء، وخاصة بعد الحلاقة لمنع التهاب البصيلات والحبوب.</p>
<h3>هل منتج ستريديكس أصلي لدى صيدلية إكليل أبها؟</h3>
<p>نعم، منتج ستريديكس أصلي 100% مستورد من أمريكا ومضمون الجودة لدى صيدلية إكليل أبها السعودية.</p>
<h3>هل يمكن استخدام المسحة الواحدة أكثر من مرة؟</h3>
<p>لا، كل مسحة قطنية مخصصة للاستخدام الفردي لمرة واحدة فقط ثم تُرمى في النفايات لمنع نقل البكتيريا.</p>
<h3>ما العمل إذا شعرت بجفاف أو تقشر خفيف بالوجه؟</h3>
<p>هذا رد فعل طبيعي، يمكنك تقليل الاستخدام إلى مرة كل يومين وزيادة ترطيب البشرة بمرطب لطيف مدعم بالسيراميد.</p>
<h3>هل يساعد ستريديكس في تضييق المسام الواسعة؟</h3>
<p>نعم، عندما ينظف المسام من الدهون المترسبة ويمنع تمددها، تستعيد المسام حجمها الطبيعي وتبدو أصغر وأكثر نضارة.</p>
<h3>هل يحتوي المنتج على عطور قوية؟</h3>
<p>يحتوي على معطر طبي خفيف جداً يمنح شعوراً بالنظافة والانتعاش دون التسبب في تحسس الجلد.</p>`,
    "tags": ["stridex", "salicylic_acid", "acne_pads", "maximum_strength", "ekleel_abha"]
  },
  "en": {
    "title": "Stridex Acne Treatment Cotton Pads Maximum Strength 2% Salicylic Acid - 90 Pads",
    "meta_title": "Stridex Acne Control Pads Maximum 2% Salicylic Acid 90 Pads | Ekleel",
    "meta_description": "Buy Stridex Maximum Strength 2% Salicylic Acid Pads (90 Count). Alcohol-free formula unclogs pores, clears acne & blackheads. 100% authentic at Ekleel Abha Pharmacy.",
    "description": `<h2>Product Overview</h2>
<p><strong>Stridex Maximum Strength Acne Control Cotton Pads (90 Count)</strong> represent the gold standard in over-the-counter topical acne treatment. Formulated with <strong>2% Salicylic Acid (BHA)</strong>—the highest allowable concentration without a prescription—these soft-textured pads offer an unbeatable solution for clearing active breakouts, removing stubborn blackheads, and preventing future comedones. Each container comes equipped with 90 pre-soaked cotton discs designed for maximum convenience and targeted dermatological performance.</p>
<p>Unlike traditional acne wipes that rely heavily on drying ethyl alcohol, Stridex pads are <strong>100% alcohol-free</strong>. This critical formulation choice ensures that skin receives deep pore exfoliation without suffering from painful burning, stripping of natural moisture, or rebound hyper-seborrhea. The triple-action pads clean the skin surface, treat underlying inflammation, and prevent new blemishes from taking root, making them an essential staple for oily and acne-prone skin types.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Triple-Action System (Clean, Treat, Prevent):</strong> Cleans skin surfaces, actively dissolves existing acne, and shields against future breakouts.</li>
  <li><strong>Maximum OTC BHA Strength (2.0% Salicylic Acid):</strong> Lipid-soluble acid penetrates deep into follicular pores to dissolve sebum plugs and keratinized skin debris.</li>
  <li><strong>100% Alcohol-Free Formula:</strong> Delivers high-potency acne care without the redness, severe dryness, or burning sensation associated with alcohol base.</li>
  <li><strong>Dual Mechanical & Chemical Exfoliation:</strong> Soft textured cotton pads mechanically lift surface grime while the active BHA chemically purifies pores.</li>
  <li><strong>Exceptional 90-Pad Value Size:</strong> Provides an extended supply for daily facial care as well as body acne treatment on the back, shoulders, and chest.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleansing):</strong> Wash face thoroughly with a mild, non-drying cleanser and pat completely dry before application.</li>
  <li><strong>Step 2 (Application):</strong> Take one cotton pad and gently wipe the entire affected area or face, strictly avoiding the eye contour and lips.</li>
  <li><strong>Step 3 (Gradual Frequency):</strong> Begin with one application daily to allow skin acclimatization. Gradually increase to 2 or 3 times daily if needed or directed by a physician.</li>
  <li><strong>Step 4 (Leave-On Treatment):</strong> Allow the liquid to absorb and dry naturally on the skin. Do not rinse off with water. Follow with an oil-free moisturizer.</li>
  <li><strong>Step 5 (Dryness Control):</strong> If bothersome dryness or peeling occurs, reduce application to once daily or every other day.</li>
</ul>

<h2>Active Ingredients Overview</h2>
<p>The core active ingredient is <strong>Salicylic Acid 2.0% w/w</strong>, a beta hydroxy acid renowned for its lipophilic properties, allowing it to mix seamlessly with cutaneous sebum and flush out pores from within. The liquid vehicle is balanced with soothing conditioning agents and pH adjusters to maximize efficacy while maintaining cutaneous tolerance.</p>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external dermatological use only. Avoid contact with eyes, nostrils, and lips.</li>
  <li>Mild skin peeling or redness may occur during the first few days of use; if severe irritation develops, discontinue use and consult a doctor.</li>
  <li>Using other topical acne medications simultaneously may increase dryness or irritation. If this occurs, use only one medication at a time unless advised by a physician.</li>
  <li>Keep out of reach of children. Store container tightly closed at room temperature to prevent pads from drying out.</li>
</ul>

<h2>Who Is This For?</h2>
<p>Ideal for teens and adults dealing with moderate to severe acne, stubborn blackheads, clogged pores, and excessive facial oiliness. Highly recommended for treating facial acne as well as body acne (bacne, chest, and shoulder breakouts).</p>`,
    "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Stridex</td></tr>
  <tr><th>Category</th><td>Skin Care / Acne Treatments & Pads</td></tr>
  <tr><th>Product Type</th><td>Alcohol-Free Medicated Acne Control Pads</td></tr>
  <tr><th>Volume/Weight</th><td>90 Soft-Touch Cotton Pads</td></tr>
  <tr><th>Skin/Hair Type</th><td>Oily, Combination & Acne-Prone Skin</td></tr>
  <tr><th>Finish</th><td>Clear, Matte & Oil-Free Finish</td></tr>
  <tr><th>Texture</th><td>Soft Cotton Pads Soaked in Liquid Solution</td></tr>
  <tr><th>Fragrance</th><td>Light Clean Fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Salicylic Acid 2.0% w/w (BHA)</td></tr>
  <tr><th>Country of Origin</th><td>USA</td></tr>
  <tr><th>Manufacturer</th><td>Blistex Inc.</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (12+ Years)</td></tr>
</tbody>
</table>`,
    "knowledge_base": `<h2>Clinical Insights on BHA Pore Exfoliation & Acne Management</h2>

<h3>What Problem Does This Product Solve?</h3>
<p>Stridex Maximum Strength Pads address acne vulgaris, comedonal acne (blackheads and whiteheads), enlarged pores, and hyper-seborrhea. They dissolve stubborn oil plugs trapped inside hair follicles without causing chemical burn or excessive dehydration.</p>

<h3>Why Do Clogged Pores & Acne Breakouts Form?</h3>
<p>Acne occurs when sebaceous glands produce an excess of sebum (skin oil), which mixes with shed keratinocytes (dead skin cells). This sticky mixture forms a comedonal plug within the follicular infundibulum, creating an anaerobic, oxygen-deprived space where <em>Cutibacterium acnes</em> bacteria flourish. Bacterial metabolic byproducts trigger localized tissue inflammation, resulting in papules, pustules, and cystic lesions.</p>

<h3>Prevention Tips for Clear Skin</h3>
<p>1. <strong>Incorporate Daily BHA Exfoliation:</strong> Salicylic acid is oil-soluble, making it uniquely capable of penetrating sebum to exfoliate deep inside pores.<br>2. <strong>Avoid Alcohol-Laden Toners:</strong> Alcohol strips essential skin lipids, triggering a rebound spike in sebum production. Opt for alcohol-free BHA formulations like Stridex.<br>3. <strong>Hydrate with Oil-Free Moisturizers:</strong> Maintain skin barrier integrity by pairing exfoliating acids with light, non-comedogenic moisturizers.<br>4. <strong>Apply Broad-Spectrum Sunscreen:</strong> Chemical exfoliants increase photosensitivity. Always apply SPF 50 daily.</p>

<h3>Professional Recommendations</h3>
<p>Dermatologists frequently recommend Stridex 2% pads as an accessible, high-performance maintenance tool. When initiating BHA therapy, start with alternate-day applications to build epidermal tolerance before advancing to daily use. Stridex pads are also exceptionally effective for managing post-workout body acne on the chest, back, and shoulders.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Scrubbing your face hard with acne pads removes pimples faster."<br><strong>Fact:</strong> Aggressive mechanical scrubbing causes micro-tears in the epidermal barrier, exacerbating inflammation and spreading acne bacteria. Gentle wiping allows the chemical action of Salicylic Acid to work effectively without damaging the skin.</p>

<h3>Scientific Explanation of Mechanism (Salicylic Acid 2% BHA)</h3>
<p>Salicylic acid is a aromatic beta hydroxy acid derived from salicin. Its lipophilic chemical structure enables it to bypass epidermal lipids and enter the sebaceous gland unit. Once inside the pore, it desolvates intercellular desmosomes, loosening dead skin cells and liquefying dense sebum plugs. Furthermore, its chemical similarity to acetylsalicylic acid (aspirin) imparts inherent anti-inflammatory properties, rapidly soothing acne-related erythema.</p>`,
    "faqs": `<h3>What are Stridex Maximum Strength Pads 90 Count?</h3>
<p>They are alcohol-free medicated cotton pads pre-soaked in 2% Salicylic Acid solution, designed to clean pores, treat active acne, and prevent future breakouts on the face and body.</p>
<h3>What is the active ingredient concentration in the Red tub?</h3>
<p>The Red tub (Maximum Strength) contains 2.0% Salicylic Acid (BHA), which is the highest non-prescription strength available for maximum clinical efficacy.</p>
<h3>Do Stridex Red Pads contain alcohol?</h3>
<p>No, all Stridex pads are 100% alcohol-free, eliminating the stinging, burning, and severe dehydration associated with traditional alcohol wipes.</p>
<h3>How often should I use Stridex Maximum Pads?</h3>
<p>Start with once daily. You may gradually increase to 2 or 3 times daily as tolerated by your skin or as directed by a healthcare professional.</p>
<h3>Do I need to wash my face after wiping with the pad?</h3>
<p>No, do not rinse your face after application. Leave the Salicylic Acid liquid on your skin to allow it to absorb and continuously dissolve pore impactions.</p>
<h3>Should I apply a moisturizer after using Stridex?</h3>
<p>Yes, once the liquid has dried completely on your face, apply a light, oil-free non-comedogenic moisturizer to protect your skin barrier.</p>
<h3>Are Stridex pads effective for blackheads and whiteheads?</h3>
<p>Yes, Salicylic Acid is oil-soluble and excels at penetrating pores to dissolve oxidized sebum plugs, effectively eliminating blackheads and whiteheads.</p>
<h3>Can I use Stridex pads on body acne (back and chest)?</h3>
<p>Absolutely. The 90-pad container provides ample supply for treating large body areas like the back, shoulders, and chest prone to sweat-induced breakouts.</p>
<h3>What is the difference between Stridex Red and Blue tubs?</h3>
<p>Stridex Red contains 2% Salicylic Acid for maximum acne control, while Stridex Blue contains 1% Salicylic Acid plus soothing vitamins A, C, and E for sensitive skin.</p>
<h3>Is Stridex 2% suitable for sensitive skin?</h3>
<p>Sensitive skin types may find 2% strong initially. It is recommended to start with the 1% Blue tub or use the Red tub every other day until tolerance develops.</p>
<h3>How long does it take to see visible results?</h3>
<p>Initial improvements in skin smoothness and oil reduction appear within 3-7 days. Significant acne clearance and pore refinement typically occur in 2-4 weeks.</p>
<h3>Will Stridex cause skin purging initially?</h3>
<p>Yes, temporary skin purging (microcomedones rising to the surface) can occur during the first 1-2 weeks. Continued use reveals clearer, smoother skin.</p>
<h3>Is Stridex safe during pregnancy or breastfeeding?</h3>
<p>Topical 2% BHA over limited areas is generally considered low-risk, but pregnant or nursing women should consult their obstetrician prior to use.</p>
<h3>Does Salicylic Acid increase sun sensitivity?</h3>
<p>Yes, chemical exfoliation renders skin more susceptible to UV rays. Always apply a broad-spectrum sunscreen with SPF 30 or higher during the day.</p>
<h3>Can I pair Stridex with acid-based face washes?</h3>
<p>It is best to pair Stridex with a gentle, non-acidic cleanser to prevent over-exfoliation and compromised skin barrier function.</p>
<h3>Can Stridex pads help with ingrown hairs and razor bumps?</h3>
<p>Yes, wiping shaved areas (face, neck, bikini line) with Stridex prevents clogged follicles and significantly reduces ingrown hairs and razor bumps.</p>
<h3>Should I scrub my face firmly with the cotton pad?</h3>
<p>No, wipe gently across your skin without aggressive rubbing. The chemical action of the BHA works effectively without mechanical pressure.</p>
<h3>How should I store the Stridex 90-pad tub?</h3>
<p>Close the flip-top lid tightly immediately after extracting a pad, and store in a cool, dry place away from direct sunlight to keep pads moist.</p>
<h3>Does the 90-pad count last a long time?</h3>
<p>Yes, a 90-pad container provides a 3-month supply when used once daily, offering exceptional value for continuous clinical acne control.</p>
<h3>Is Stridex suitable for men?</h3>
<p>Yes, Stridex is ideal for both men and women, especially for male skin which tends to produce more sebum and experience post-shave breakouts.</p>
<h3>Is this product authentic at Ekleel Abha Pharmacy?</h3>
<p>Yes, this product is 100% authentic, imported directly from the USA, and guaranteed by Ekleel Abha Pharmacy in Saudi Arabia.</p>
<h3>Can a single pad be reused?</h3>
<p>No, each cotton pad is designed for single-use application only and should be discarded after use to prevent cross-contamination.</p>
<h3>What should I do if I experience mild peeling?</h3>
<p>Mild peeling is normal. Reduce application frequency to once every two days and increase hydration with a ceramide-rich moisturizer.</p>
<h3>Does Stridex help reduce enlarged pores?</h3>
<p>Yes, by keeping pores free of sebum and cellular buildup, Stridex prevents pores from stretching, making them appear noticeably smaller.</p>
<h3>Does Stridex have a strong scent?</h3>
<p>It contains a subtle, fresh scent that leaves skin feeling clean and refreshed without causing cutaneous sensitization.</p>`
  },
  "schema": {
    "brand": "Stridex",
    "category": "Skin Care / Acne Treatments",
    "availability": "InStock"
  },
  "image_seo": {
    "image_filename": "stridex-acne-treatment-cotton-pads-90-pads.webp",
    "alt": "Stridex Acne Control Cotton Pads Maximum Strength 2% Salicylic Acid 90 Pads",
    "title": "Stridex Acne Control Cotton Pads Maximum Strength 2% Salicylic Acid 90 Pads"
  }
};

// Product 1412: Stridex Essential Acne Treatment Pads - Blue (1% Salicylic Acid + Vitamins A, C, E)
const prod1412 = {
  "product_id": "1412",
  "sku": "EK-1412",
  "category": "العناية بالبشرة / علاجات حب الشباب والمسحات",
  "brand": "Stridex",
  "ar": {
    "title": "مسحات علاج حب الشباب الأساسية من ستريديكس - علبة زرقاء 1% حمض الساليسليك مع فيتامينات A, C, E",
    "meta_title": "مسحات ستريديكس زرقاء لعلاج حب الشباب 1% ساليسليك | صيدلية إكليل أبها",
    "meta_description": "اشتري مسحات ستريديكس الأساسية الزرقاء 1% حمض الساليسليك المدعمة بفيتامينات A, C, E. تركيبة خالية من الكحول للبشرة الحساسة. أصلي من صيدلية إكليل أبها.",
    "description": `<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>مسحات ستريديكس الأساسية لعلاج حب الشباب - العلبة الزرقاء (Stridex Essential Acne Treatment Pads - Blue)</strong> الخيار المفضل والأكثر أماناً للأشخاص ذوي البشرة الحساسة أو الذين يبدؤون علاج حب الشباب لأول مرة. تحتوي هذه المسحات على تركيز 1.0% من حمض الساليسليك (BHA)، وهو التركيز الأساسي المتوازن الذي يعالج حب الشباب الخفيف والرؤوس السوداء بفعالية مع الحفاظ على نعومة الجلد وراحتك دون التسبب في احمرار أو تهيج مفرط.</p>
<p>تم تمييز هذه التركيبة بكونها <strong>خالية تماماً من الكحول (100% Alcohol-Free)</strong> ومدعمة بمزيج غني من الفيتامينات المغذية والمضادة للأكسدة مثل <strong>فيتامين أ (Vitamin A)، فيتامين ج (Vitamin C)، وفيتامين هـ (Vitamin E)</strong>. تعمل هذه الفيتامينات الثلاثية على دعم تجدد خلايا البشرة، تفتيح الآثار، وتهدئة الالتهابات أثناء عمل حمض الساليسليك على تنظيف المسام بعمق وإذابة الدهون الزائدة، مما يمنحك بشرة صافية، ملساء، ومشرقة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تركيز أساسي متوازن (1% Salicylic Acid):</strong> مثالي للبشرة الحساسة وللمبتدئين لعلاج الحبوب الخفيفة وتنظيف المسام دون شد أو تهيج.</li>
  <li><strong>مدعم بـ 3 فيتامينات مغذية (Vitamins A, C, E):</strong> تعزز صحة البشرة وتعمل كمضادات أكسدة لحماية الجلد وتفتيح الآثار وتنعيم الملمس.</li>
  <li><strong>تركيبة خالية تماماً من الكحول:</strong> تضمن العناية بحب الشباب دون حرقان أو جفاف قاسي يضر بحاجز البشرة الطبيعي.</li>
  <li><strong>تنظيف وإذابة للدهون المسدودة:</strong> يخترق الزهم داخل المسام ويزيل الرؤوس السوداء والبيضاء والشوائب اليومية.</li>
  <li><strong>مسحات قطنية ناعمة جداً:</strong> مصممة بلطف لتناسب البشرة المعرضة للتحسس والتهيج بسهولة.</li>
</ul>

<h2>طريقة الاستخدام الطبية</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> اغسلي الوجه جيداً بغسول لطيف وجففي البشرة بلطف باستخدام منشفة ناعمة.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> خذي مسحة قطنية واحدة من العلبة الزرقاء وامسحي بها الوجه والرقبة بلطف شديد، مع تجنب منطقتي العينين والشفتين.</li>
  <li><strong>الخطوة الثالثة (التكرار):</strong> استخدمي المسحة من مرة إلى مرتين يومياً (صباحاً ومساءً) حسب حاجة بشرتك ومدى تحملها.</li>
  <li><strong>الخطوة الرابعة (امتصاص السائل):</strong> اتركي السائل المترسب يجف تلقائياً على البشرة دون شطفه بالماء.</li>
  <li><strong>الخطوة الخامسة (الترطيب):</strong> اتبعي المسحات بمرطب خفيف مناسب لنوع بشرتك لحمايتها من الجفاف.</li>
</ul>

<h2>نظرة عامة على المكونات الفعالة</h2>
<p>تحتوي العلبة الزرقاء على <strong>حمض الساليسليك بتركيز 1.0% w/w</strong> المقشر للمسام، بالإضافة إلى <strong>Retinyl Palmitate (فيتامين أ)</strong> الذي يدعم تجدد الخلايا، و<strong>Ascorbyl Palmitate (فيتامين ج)</strong> المضاد للأكسدة والمفتح للآثار، و<strong>Tocopheryl Acetate (فيتامين هـ)</strong> المرطب والمهدئ للأنسجة الجلدية.</p>

<h2>تحذيرات واحتياطات طبية</h2>
<ul>
  <li>للاستخدام الظاهري الموضعي على الجلد فقط. تجنبي ملامسة العينين وأغشية الفم والأنف.</li>
  <li>في حال حدوث جفاف خفيف أو تقشر، يقلل الاستخدام إلى مرة واحدة يومياً أو يوم بعد يوم.</li>
  <li>إذا كنت تستخدمين منتجات مقشرة أخرى، يُفضل عدم الدمج المباشر في نفس الوقت لتجنب تحسس الجلد.</li>
  <li>تحفظ العلبة في مكان بارد وجاف وتغلق بإحكام للحفاظ على رطوبة القطن.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<p>ممتاز جداً لأصحاب البشرة الحساسة، المختلطة، والجافة المعرضة للحبوب الخفيفة، وللمراهقين الجدد في عالم العناية بالبشرة، ولكل من يبحث عن مقشر أحماض فواكه لطيف يومي مدعم بالفيتامينات.</p>`,
    "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>Stridex (ستريديكس)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / علاجات حب الشباب والمسحات</td></tr>
  <tr><th>نوع المنتج</th><td>مسحات قطنية مغذية ومقشرة لحب الشباب 1% BHA</td></tr>
  <tr><th>الحجم/الوزن</th><td>55 مسحة قطنية (55 Essential Pads)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الحساسة، المختلطة، والمعرضة لحب الشباب الخفيف</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة متوازنة، صافية، ومشرقة</td></tr>
  <tr><th>الملمس</th><td>مسحات قطنية مشبعة بسائل مهدئ</td></tr>
  <tr><th>العطر</th><td>عطر منعش ولطيف (Fresh Scent)</td></tr>
  <tr><th>المكونات النشطة</th><td>حمض الساليسليك 1.0% + فيتامينات A, C, E</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة الأمريكية (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Blistex Inc.</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (12 سنة فما فوق)</td></tr>
</tbody>
</table>`,
    "knowledge_base": `<h2>الدليل المعرفي الطبي لتقشير البشرة الحساسة وتغذيتها بالفيتامينات</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج مسحات ستريديكس الزرقاء (Essential Strength) مشكلة حب الشباب الخفيف إلى المتوسط، الرؤوس السوداء الناشئة، الملمس الخشن، والتهيج الناتج عن انسداد المسام لدى أصحاب البشرة الحساسة الذين لا يتحملون الأحماض القوية.</p>

<h3>لماذا تظهر الحبوب لدى البشرة الحساسة؟</h3>
<p>تتعرض البشرة الحساسة لانسداد المسام تماماً مثل البشرة الدهنية، ولكن حاجزها الجلدي (Skin Barrier) يكون أكثر عرضة للتهيجات والاحمرار. عند استخدام مقشرات قوية أو منتجات تحتوي على الكحول، يلتهب حاجز البشرة وتتدهور صحة الجلد، مما يزيد من صعوبة علاج الحبوب. لذا تبرز الحاجة لمقشر بتركيز متوازن (1% BHA) مدعم بمضادات الأكسدة.</p>

<h3>نصائح وقائية للبشرة الحساسة المعرضة للحبوب</h3>
<p>1. <strong>التقشير التدريجي اللطيف:</strong> البدء بتركيز 1% ساليسليك لتنظيف المسام دون إجهاد حاجز الجلد.<br>2. <strong>تغذية الجلد بالفيتامينات:</strong> فيتامينات C و E تحمي الخلايا من الأكسدة وتساعد في التئام آثار الحبوب سريعا.<br>3. <strong>تجنب الكحول والمواد المهيجة:</strong> اختيار تركيبات ستريديكس الخالية من الكحول لضمان ترطيب الأنسجة.<br>4. <strong>الالتزام بالحماية من الشمس:</strong> تطبيق واقي شمس SPF 30-50 يومياً لحماية البشرة المقشرة.</p>

<h3>توصيات الخبراء والصيادلة</h3>
<p>ينصح الصيادلة بمسحات ستريديكس الزرقاء كخطوة مدخلية مثالية للأشخاص الجدد على استخدام حمض الساليسليك (BHA Beginners)، أو لأولئك الذين يمتلكون بشرة مختلطة وحساسة تتهيج من التركيزات العالية (2%). كما يمكن استخدام العلبة الزرقاء صيفاً كمقشر ومطهر يومي خفيف بعد الرياضة أو التعرق لغسل المسام ومنع تراكم الدهون.</p>

<h3>خرافات شائعة حول مقشرات حب الشباب للبشرة الحساسة</h3>
<p><strong>خرافة:</strong> "البشرة الحساسة لا يمكنها استخدام حمض الساليسليك إطلاقاً."<br><strong>الحقيقة:</strong> حمض الساليسليك بتركيز 1% وفي تركيبة خالية من الكحول ومطعمة بالفيتامينات المهدئة يمنح البشرة الحساسة تنظيفاً آمناً جداً دون التسبب في احمرار أو تحسس.</p>

<h3>التفسير العلمي لآلية العمل (1% Salicylic Acid + Vitamins A, C, E)</h3>
<p>يقوم حمض الساليسليك بتركيز 1% بتفكيك الروابط بين خلايا الجلد الميتة والتغلغل في المسام لإذابة الدهون الزائدة بطريقة لطيفة وغير مجهدة. بالتزامن مع ذلك، يعمل **فيتامين أ** على تحفيز الانقسام الخليوي الصحي، بينما يقوم **فيتامين ج** بتحييد الشوارد الحرة وتقليل تصبغ الآثار، ويوفر **فيتامين هـ** حماية زيتية مهدئة لغشاء الخلايا.</p>`,
    "faqs": `<h3>ما هي مسحات ستريديكس الأساسية الزرقاء؟</h3>
<p>هي مسحات قطنية خالية من الكحول تحتوي على 1% حمض الساليسليك ومدعمة بالفيتامينات (A, C, E) لعلاج حب الشباب الخفيف وتنظيف مسام البشرة الحساسة.</p>
<h3>ما نسبة حمض الساليسليك في ستريديكس الأزرق؟</h3>
<p>تحتوي العلبة الزرقاء على نسبة 1.0% حمض الساليسليك، وهي النسبة الأساسية اللطيفة المخصصة للبشرة الحساسة أو الحبوب الخفيفة.</p>
<h3>هل تحتوي المسحات الزرقاء على الكحول؟</h3>
<p>لا، المسحات خالية تماماً من الكحول (100% Alcohol-Free)، مما يحمي البشرة من الجفاف واللسع والاحمرار.</p>
<h3>ما فائدة إضافة فيتامينات A, C, E للمسحات؟</h3>
<p>تعمل هذه الفيتامينات كمضادات أكسدة مغذية تحمي خلايا الجلد، تهدئ التهيج، تدعم مرونة البشرة، وتساعد في تفتيح آثار الحبوب الداكنة.</p>
<h3>كم مرة يُستخدم ستريديكس الأزرق في اليوم؟</h3>
<p>يمكن استخدامه من مرة إلى مرتين يومياً صباحاً ومساءً على بشرة نظيفة وجافة.</p>
<h3>هل يجب غسل الوجه بالماء بعد استخدام المسحة الزرقاء؟</h3>
<p>لا يُغسل الوجه بالماء. يترك سائل المسحة ليجف طبيعياً على البشرة لتمتص المكونات الفعالة والفيتامينات.</p>
<h3>هل يناسب ستريديكس الأزرق البشرة الحساسة جداً؟</h3>
<p>نعم، تم تصميم العلبة الزرقاء بتركيز 1% خصيصاً ليلائم البشرة الحساسة والبشرة المبتدئة في استعمال الأحماض المقشرة.</p>
<h3>ما الفرق بين ستريديكس الأحادي 2% (الأحمر) و ستريديكس 1% (الأزرق)؟</h3>
<p>الأحمر يحتوي 2% حمض ساليسليك لحب الشباب الشديد والبشرة الدهنية، بينما الأزرق يحتوي 1% حمض ساليسليك مع فيتامينات مهدئة للحالات الخفيفة والحساسة.</p>
<h3>هل يزيل ستريديكس الأزرق الرؤوس السوداء؟</h3>
<p>نعم، يذيب سدادات الزهم والدهون المتراكمة داخل المسام ويمنع تكون الرؤوس السوداء والبيضاء.</p>
<h3>هل يمكن استخدامه للمراهقين بعمر 12-15 سنة؟</h3>
<p>نعم، آمن وممتاز جداً كبداية لعناية المراهقين ببشرتهم لمنع تفاقم حب الشباب الهرموني الخفيف.</p>
<h3>هل يجب استخدام مرطب بعد مسحات ستريديكس الزرقاء؟</h3>
<p>نعم، يُفضل دائماً تطبيق مرطب خفيف خالٍ من الزيوت بعد جفاف السائل للحفاظ على رطوبة البشرة وملمسها الناعم.</p>
<h3>متى تظهر نتائج ستريديكس الأزرق؟</h3>
<p>تلاحظ النظافة ونعومة الملمس فوراً، وتتراجع الحبوب الخفيفة والرؤوس السوداء خلال أسبوعين من الاستخدام المنتظم.</p>
<h3>هل تسبب المسحات الزرقاء تقشيراً شديداً للبشرة؟</h3>
<p>لا، تركيز 1% الخالي من الكحول نادر جداً ما يسبب تقشيراً ملحوظاً، بل يمنح تقشيراً ميكروبياً ناعماً وغير مرئي.</p>
<h3>هل يمكن استخدام ستريديكس الأزرق يومياً في الصيف؟</h3>
<p>نعم، ممتاز جداً في فصل الصيف لتنظيف العرق والزيوت المتراكمة بعد الخروج أو ممارسة الرياضة.</p>
<h3>هل يساعد على تفتيح بقايا الحبوب؟</h3>
<p>نعم، بفضل وجود فيتامين C وحمض الساليسليك اللذين يعملان معاً على تقشير وتفتيح تصبغات الآثار.</p>
<h3>هل يمكن استخدام المسحة على منطقة الصدر والأكتاف؟</h3>
<p>نعم، المسحات مناسبة تماماً لمسح مناطق الجسم الرقيقة مثل أعلى الصدر والأكتاف لعلاج الحبوب الخفيفة.</p>
<h3>هل يوضع واقي شمس بعد الاستخدام نهاراً؟</h3>
<p>نعم، يجب استخدام واقي شمس SPF 30 أو أعلى نهاراً للحماية من التصبغات الشمسية أثناء استخدام الأحماض.</p>
<h3>هل يمكن استخدام المسحات الزرقاء قبل المكياج؟</h3>
<p>نعم، مسح الوجه بها قبل الترطيب والمكياج يمنح البشرة ملمساً أملساً ومطفأً يسهل توزيع كريم الأساس.</p>
<h3>كم عدد المسحات داخل العلبة الزرقاء؟</h3>
<p>تحتوي العلبة على 55 مسحة قطنية مشبعة عالية الجودة.</p>
<h3>كيف يُحفظ المنتج؟</h3>
<p>يُحفظ في مكان بارد وجاف مع غلق الغطاء بإحكام لمنع تبخر السائل وجفاف المسحات.</p>
<h3>هل المنتج أصلي لدى صيدلية إكليل أبها؟</h3>
<p>نعم، جميع منتجات ستريديكس لدينا أصلية 100% ومستوردة ومضمونة الجودة لدى صيدلية إكليل أبها.</p>
<h3>هل يناسب الرجال بعد الحلاقة؟</h3>
<p>نعم، ممتاز لتهدئة البشرة بعد الحلاقة ومنع ظهور بثور الحلاقة والشعر تحت الجلد بفضل فيتامين E و 1% BHA.</p>
<h3>هل يمكن استخدامه مرتين في اليوم؟</h3>
<p>نعم، يمكن استخدامه صباحاً ومساءً إذا كانت البشرة تتحمله بشكل جيد وتتطلب ذلك.</p>
<h3>هل يُسبب حرقان للبشرة؟</h3>
<p>بسبب خلوه التام من الكحول وانخفاض تركيز الحمض، فإنه لا يسبب الحرقان الذي تسببه المسحات الأخرى.</p>
<h3>هل العلبة الزرقاء خالية من البارابين؟</h3>
<p>نعم، تركيبة آمنة وخالية من البارابين والمواد الكيميائية القاسية.</p>`,
    "tags": ["stridex", "salicylic_acid", "essential_pads", "blue_box", "ekleel_abha"]
  },
  "en": {
    "title": "Stridex Essential Acne Treatment Pads Blue - 1% Salicylic Acid with Vitamins A, C & E (55 Pads)",
    "meta_title": "Stridex Essential Blue Acne Pads 1% Salicylic Acid 55 Pads | Ekleel",
    "meta_description": "Buy Stridex Essential Blue Pads 1% Salicylic Acid with Vitamins A, C & E (55 Pads). Alcohol-free formula for sensitive skin. Fast shipping in Saudi Arabia.",
    "description": `<h2>Product Overview</h2>
<p><strong>Stridex Essential Acne Treatment Pads - Blue Container (55 Count)</strong> offer the perfect entry-level formula for individuals with sensitive skin, mild acne, or those introducing Beta Hydroxy Acids (BHAs) to their regimen for the first time. Formulated with a balanced <strong>1.0% Salicylic Acid concentration</strong>, these soft-textured pads effectively unclog pores, clear mild breakouts, and dissolve surface oil without triggering dryness, redness, or cutaneous irritation.</p>
<p>What sets the Stridex Blue formula apart is its <strong>100% alcohol-free delivery system</strong> enriched with a powerful trio of essential skin vitamins: <strong>Vitamin A (Retinyl Palmitate), Vitamin C (Ascorbyl Palmitate), and Vitamin E (Tocopheryl Acetate)</strong>. While Salicylic Acid penetrates deeply to clear pore impactions, these antioxidant vitamins nourish the skin barrier, promote cellular renewal, calm inflammation, and fade post-acne marks, leaving your complexion exceptionally smooth, clear, and radiant.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Gentle 1.0% BHA Strength:</strong> Specially tuned for sensitive skin, teenagers, and mild acne to exfoliate without burning or discomfort.</li>
  <li><strong>Enriched with Vitamins A, C & E:</strong> Triple-vitamin complex provides essential antioxidant defense, barrier support, and brightening properties.</li>
  <li><strong>100% Alcohol-Free Formulation:</strong> Clears acne effectively without stripping natural skin moisture or disrupting the acid mantle.</li>
  <li><strong>Dissolves Sebum & Blackheads:</strong> Penetrates lipid-filled pores to dissolve micro-comedones and keep skin smooth and clear.</li>
  <li><strong>Ultra-Soft Cotton Pads:</strong> Designed for delicate wiping that minimizes mechanical friction on sensitive or reactive skin.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleansing):</strong> Wash your face with a mild, hydrating cleanser and pat dry thoroughly with a soft towel.</li>
  <li><strong>Step 2 (Application):</strong> Take one blue pad and gently wipe across the entire face and neck, avoiding the delicate eye area and lips.</li>
  <li><strong>Step 3 (Frequency):</strong> Use 1 to 2 times daily (morning and/or evening) depending on your skin's tolerance and needs.</li>
  <li><strong>Step 4 (Absorption):</strong> Allow the liquid solution to absorb and dry naturally on the skin. Do not rinse off.</li>
  <li><strong>Step 5 (Moisturizing):</strong> Follow with your favorite light, non-comedogenic moisturizer to lock in hydration.</li>
</ul>

<h2>Active Ingredients Overview</h2>
<p>Formulated with <strong>Salicylic Acid 1.0% w/w</strong> to gently exfoliate inside pores, alongside <strong>Retinyl Palmitate (Vitamin A)</strong> for cell renewal, <strong>Ascorbyl Palmitate (Vitamin C)</strong> for antioxidant brightening, and <strong>Tocopheryl Acetate (Vitamin E)</strong> to soothe and condition the epidermis.</p>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external dermatological use only. Avoid contact with eyes, lips, and mucous membranes.</li>
  <li>If mild dryness or flaking occurs, reduce usage frequency to once daily or every other day.</li>
  <li>Avoid combining with other strong chemical exfoliants simultaneously to prevent skin barrier distress.</li>
  <li>Keep container tightly closed in a cool, dry place to prevent pads from drying out.</li>
</ul>

<h2>Who Is This For?</h2>
<p>Perfect for individuals with sensitive, dry, or combination skin experiencing mild acne, blackheads, or rough skin texture. Ideal for teenagers starting their acne care routine and anyone seeking a gentle daily BHA exfoliant enriched with vitamins.</p>`,
    "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Stridex</td></tr>
  <tr><th>Category</th><td>Skin Care / Acne Treatments & Pads</td></tr>
  <tr><th>Product Type</th><td>Alcohol-Free Vitamin-Enriched Acne Control Pads</td></tr>
  <tr><th>Volume/Weight</th><td>55 Soft-Touch Cotton Pads</td></tr>
  <tr><th>Skin/Hair Type</th><td>Sensitive, Combination & Mild Acne-Prone Skin</td></tr>
  <tr><th>Finish</th><td>Balanced, Smooth & Radiant Finish</td></tr>
  <tr><th>Texture</th><td>Soft Cotton Pads Soaked in Soothing Liquid</td></tr>
  <tr><th>Fragrance</th><td>Fresh Mild Fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Salicylic Acid 1.0% + Vitamins A, C, E</td></tr>
  <tr><th>Country of Origin</th><td>USA</td></tr>
  <tr><th>Manufacturer</th><td>Blistex Inc.</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (12+ Years)</td></tr>
</tbody>
</table>`,
    "knowledge_base": `<h2>Clinical Insights on Sensitive Skin Exfoliation & Vitamin Support</h2>

<h3>What Problem Does This Product Solve?</h3>
<p>Stridex Essential Blue Pads target mild acne breakouts, early-stage blackheads, rough texture, and clogged pores in individuals with sensitive skin who cannot tolerate high-potency acid treatments or alcohol-based wipes.</p>

<h3>Why Does Sensitive Skin Suffer from Breakouts?</h3>
<p>Sensitive skin experiences pore congestion just like oily skin, but its epidermal barrier is inherently more delicate and reactive. Harsh acne treatments containing ethyl alcohol or high acid percentages break down inter-cellular lipids, causing redness, burning, and compromised barrier function. A gentler 1% Salicylic Acid formula buffered with antioxidant vitamins provides effective pore purification while respecting barrier integrity.</p>

<h3>Prevention Tips for Sensitive Acne-Prone Skin</h3>
<p>1. <strong>Opt for Low-Concentration BHA:</strong> 1% Salicylic Acid provides effective comedolytic action without triggering cutaneous distress.<br>2. <strong>Prioritize Alcohol-Free Formulas:</strong> Avoid drying alcohols that strip barrier lipids and cause reactive redness.<br>3. <strong>Nourish with Antioxidants:</strong> Vitamins C and E protect skin lipids from environmental oxidation, preventing comedone darkening.<br>4. <strong>Daily Sun Protection:</strong> Protect exfoliated skin daily with a broad-spectrum SPF 30+ mineral or lightweight sunscreen.</p>

<h3>Professional Recommendations</h3>
<p>Dermatologists and pharmacists frequently recommend Stridex Blue pads for adolescents, BHA beginners, and individuals with reactive combination skin. Using these pads after workouts or outdoor activities effectively removes sweat and trapped lipids before they harden into blackheads. The addition of Vitamin E ensures the skin remains soft and pliable post-cleansing.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "People with sensitive skin should never use Salicylic Acid exfoliants."<br><strong>Fact:</strong> Salicylic Acid at 1% concentration in an alcohol-free, vitamin-buffered vehicle is extremely well tolerated by sensitive skin, offering gentle anti-inflammatory and pore-clearing benefits without irritation.</p>

<h3>Scientific Explanation of Mechanism (1.0% Salicylic Acid + Vitamins A, C, E)</h3>
<p>Salicylic Acid at 1.0% w/w desolvates desmosomal bonds between dead keratinocytes within the upper follicular infundibulum, allowing trapped sebum to flow freely. Concurrently, <strong>Vitamin A</strong> aids cellular differentiation, <strong>Vitamin C</strong> neutralizes reactive oxygen species to reduce post-inflammatory hyperpigmentation, and <strong>Vitamin E</strong> reinforces membrane lipid stability, preventing transepidermal water loss.</p>`,
    "faqs": `<h3>What are Stridex Essential Blue Pads 55 Count?</h3>
<p>They are gentle, alcohol-free medicated pads containing 1.0% Salicylic Acid enriched with Vitamins A, C, and E, designed for sensitive skin acne care.</p>
<h3>What is the Salicylic Acid percentage in the Blue tub?</h3>
<p>The Blue tub contains 1.0% Salicylic Acid, offering an essential, mild strength formulation suitable for sensitive skin and gentle daily exfoliation.</p>
<h3>Are Stridex Blue Pads alcohol-free?</h3>
<p>Yes, all Stridex pads are 100% alcohol-free, eliminating burning, stinging, and severe cutaneous dehydration.</p>

<h3>Why are Vitamins A, C, and E added to Stridex Blue?</h3>
<p>These antioxidant vitamins nourish and soothe the skin, promote cellular renewal, protect against environmental damage, and help fade post-acne marks.</p>
<h3>How often should I use Stridex Blue Pads?</h3>
<p>You can use them 1 to 2 times daily (morning and night) after cleansing your face thoroughly.</p>
<h3>Do I need to wash off the liquid after wiping?</h3>
<p>No, do not rinse. Leave the solution on your skin so the active ingredients and vitamins can absorb and work inside the pores.</p>
<h3>Is Stridex Blue suitable for very sensitive skin?</h3>
<p>Yes, the 1% alcohol-free vitamin formula is specifically formulated to be safe and gentle on sensitive and reactive skin types.</p>
<h3>What is the difference between Stridex Red (2%) and Blue (1%)?</h3>
<p>Stridex Red contains 2% Salicylic Acid for maximum acne control, while Stridex Blue contains 1% Salicylic Acid plus vitamins for mild acne and sensitive skin.</p>
<h3>Does Stridex Blue clear blackheads?</h3>
<p>Yes, 1% Salicylic Acid effectively penetrates lipid-filled pores to dissolve trapped sebum and clear blackheads and whiteheads.</p>
<h3>Is Stridex Blue good for teenagers?</h3>
<p>Yes, it is an ideal starter product for teens aged 12 and above experiencing mild adolescent acne and clogged pores.</p>
<h3>Should I use a moisturizer after applying Stridex Blue?</h3>
<p>Yes, applying a lightweight oil-free moisturizer after the solution dries helps lock in hydration and maintain barrier health.</p>
<h3>When can I expect visible improvements?</h3>
<p>Skin texture feels smoother almost immediately. Reduction in mild breakouts and blackheads is visible within 1 to 2 weeks of regular use.</p>
<h3>Does Stridex Blue cause peeling?</h3>
<p>Peeling is very rare with the gentle 1% alcohol-free formula, providing subtle, non-visible micro-exfoliation.</p>
<h3>Can I use Stridex Blue daily during summer?</h3>
<p>Yes, it is excellent in summer for removing sweat, excess oil, and impurities after outdoor activities or sports.</p>
<h3>Does it help fade post-acne marks?</h3>
<p>Yes, the synergistic combination of Salicylic Acid and Vitamin C helps exfoliate surface pigmented cells and brighten post-blemish spots.</p>
<h3>Can I use Stridex Blue on my chest and shoulders?</h3>
<p>Yes, it can be applied to delicate body areas like the neck, chest, and upper arms for mild body breakout control.</p>
<h3>Is sunscreen required when using Stridex Blue?</h3>
<p>Yes, always apply a broad-spectrum SPF 30 or higher sunscreen during daytime use, as acid exfoliants increase solar sensitivity.</p>
<h3>Can I use Stridex Blue before applying makeup?</h3>
<p>Yes, wiping skin prior to moisturizing creates a smooth, clear canvas for flawless makeup application.</p>
<h3>How many pads are in the Blue container?</h3>
<p>The Stridex Essential Blue container includes 55 pre-soaked cotton pads.</p>
<h3>How should I store this product?</h3>
<p>Keep the tub tightly closed in a cool, dry place away from direct sunlight to preserve pad moisture and vitamin potency.</p>
<h3>Is this product authentic at Ekleel Abha Pharmacy?</h3>
<p>Yes, it is 100% authentic, imported directly from the USA, and quality-guaranteed at Ekleel Abha Pharmacy in Saudi Arabia.</p>
<h3>Is Stridex Blue beneficial after shaving for men?</h3>
<p>Yes, its alcohol-free formula with Vitamin E and 1% BHA calms post-shave skin while preventing razor bumps and clogged follicles.</p>
<h3>Can I use it twice daily?</h3>
<p>Yes, if well tolerated by your skin, using it morning and night provides optimal pore-clearing benefits.</p>
<h3>Does it cause stinging upon application?</h3>
<p>No, because it is completely alcohol-free and has a mild 1% concentration, it does not cause uncomfortable stinging.</p>
<h3>Is the formula paraben-free?</h3>
<p>Yes, it is formulated without parabens or harsh irritating preservatives.</p>`
  },
  "schema": {
    "brand": "Stridex",
    "category": "Skin Care / Acne Treatments",
    "availability": "InStock"
  },
  "image_seo": {
    "image_filename": "stridex-essential-acne-treatment-pads-blue-55-pads.webp",
    "alt": "Stridex Essential Blue Acne Pads 1% Salicylic Acid 55 Pads",
    "title": "Stridex Essential Blue Acne Pads 1% Salicylic Acid 55 Pads"
  }
};

// Product 1413: Acretin Acne Treatment Cream 0.025% / 30g - Jamjoom Pharma
const prod1413 = {
  "product_id": "1413",
  "sku": "EK-1413",
  "category": "العناية بالبشرة / علاجات حب الشباب والأدوية الجلدية",
  "brand": "Jamjoom Pharma",
  "ar": {
    "title": "أكريتين كريم لعلاج حب الشباب وتجديد البشرة 0.025% - 30جم جمجوم فارما",
    "meta_title": "أكريتين كريم 0.025% لعلاج حب الشباب 30جم | صيدلية إكليل أبها",
    "meta_description": "اشتري كريم أكريتين 0.025% (30جم) من جمجوم فارما لعلاج حب الشباب، تقشير المسام، وتوحيد لون البشرة. دواء جلدي طبي أصلي 100% من صيدلية إكليل أبها السعودية.",
    "description": `<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم أكريتين 0.025% (Acretin Cream 0.025% 30g Jamjoom Pharma)</strong> المستحضر الطبي الجلدي الرائد والأكثر شهرة واستخداماً في المملكة العربية السعودية والشرق الأوسط لعلاج حب الشباب وتجديد خلايا البشرة. يحتوي هذا الكريم العلاجي المصنع بفخر لدى شركة جمجوم فارما على مادة <strong>التريتينوين (Tretinoin 0.025%)</strong>، وهي الشكل الحمضي النشط لفيتامين أ (Retinoic Acid) والمصنفة طبياً كمعيار ذهبي لعلاج المشاكل الجلدية المستعصية.</p>
<p>يعمل أكريتين 0.025% بفعالية فائقة على تسريع معدل تجدد خلايا البشرة (Cell Turnover)، وتقشير الطبقات السطحية الميتة، ومنع تكون الزهم والكوميدونات داخل المسام. ويُعتبر تركيز <strong>0.025%</strong> التركيز الابتدائي المثالي الموصى به طبياً للبدء في العلاج لتقليل فترة التأقلم الجلدي (Retinization) وتفادي الاحمرار والجفاف الشديد، مما يمنحك بشرة صافية، خالية من البثور والتجاعيد السطحية والتصبغات الداكنة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>المعيار الذهبي لعلاج حب الشباب (Tretinoin 0.025%):</strong> يعالج حب الشباب الشائع، البثور الصديدية، والكوميدونات من خلال تنظيم نمو الخلايا الجلدية.</li>
  <li><strong>تقشير وتجديد خلايا البشرة:</strong> يسرع تساقط الخلايا الميتة ويحفز بناء طبقات جلدية جديدة ناعمة وصحية.</li>
  <li><strong>تنظيف وفتح المسام المسدودة:</strong> يمنع انحشار الدهون والكرات القرنية داخل فوهات المسام مما يقلل تشكل الرؤوس السوداء والبيضاء.</li>
  <li><strong>تحسين ملمس البشرة وتوحيد اللون:</strong> يقلل التصبغات الناجمة عن آثار حب الشباب (Post-Inflammatory Hyperpigmentation) ويحفز إنتاج الكولاجين.</li>
  <li><strong>تركيز ابتدائي آمن (0.025%):</strong> يضمن التأقلم التدريجي للبشرة مع تقليل احتمالية التهيج المقترن بالتركيزات العالية (مثل 0.05%).</li>
</ul>

<h2>طريقة الاستخدام الطبية</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف والتجفيف التام):</strong> اغسلي الوجه بغسول لطيف خالٍ من الأحماض، وانظري 20-30 دقيقة حتى تجف البشرة تماماً قبل التطبيق (التطبيق على بشرة مبللة يزيد التحسس).</li>
  <li><strong>الخطوة الثانية (كمية بحجم حبة البسلة):</strong> ضعي كمية صغيرة جداً بحجم حبة البسلة (Pea-sized amount) على أطراف أصابعك ووزعيها بنقاط على الجبهة والخدين والدقن.</li>
  <li><strong>الخطوة الثالثة (التوزيع وتجنب المناطق الحساسة):</strong> وزعي الكريم بلطف على الوجه مع تجنب زوايا العينين، جانبي الأنف، وحول الشفتين.</li>
  <li><strong>الخطوة الرابعة (التدرج في الاستخدام):</strong> استخدميه ليلاً فقط. ابدئي بمرتين أسبوعياً في أول أسبوعين، ثم يوم بعد يوم، حتى تصلي للاستخدام اليومي حسب تحمل البشرة.</li>
  <li><strong>الخطوة الخامسة (الترطيب والحماية من الشمس):</strong> ضعي مرطباً مهدئاً (مثل السيراميد أو البانثينول) بعد 20 دقيقة من الأكريتين ليلاً، ولا تستغني عن واقي الشمس SPF 50 نهاراً.</li>
</ul>

<h2>نظرة عامة على المكونات الفعالة</h2>
<p>المادة الفعالة الرئيسية هي <strong>تريتينوين (Tretinoin 0.025% w/w)</strong> في قاعدة كريمية طبية سهلة الامتصاص. التريتينوين يتصل مباشرة بمستقبلات حمض الريتينويك (RARs) في نواة الخلايا الجلدية، مما ينظم التعبير الجيني الخاص بتمايز الخلايا وتخليق الكولاجين وإفراز الدهون.</p>

<h2>تحذيرات واحتياطات طبية</h2>
<ul>
  <li><strong>ممنوع تماماً أثناء الحمل والرضاعة:</strong> يُمنع استخدام التريتينوين الموضعي منعاً باتاً للحوامل والمرضعات أو لمن تخطط للحمل لاحتمالية التأثير السمي على الجنين.</li>
  <li>للاستخدام الخارجي ليلاً فقط. يجب عدم التعرض لأشعة الشمس أو الضوء القوي أثناء وضع الكريم.</li>
  <li>يجب استخدام واقي شمس واسع الطيف SPF 50 كل صباح طوال فترة العلاج لتجنب التصبغات والحروق الشمسية.</li>
  <li>يمنع تطبيق الأكريتين على الجلد المصاب بالجروح، الحروق الشمسية، أو الأكزيما النشطة.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<p>مصمم طبياً للبالغين والمراهقين المعالجين تحت إشراف طبي لعلاج حب الشباب، التصبغات الجلدية، البثور تحت الجلد، تحسين ملمس البشرة الخشن، ومكافحة علامات التقدم في السن المبكرة.</p>`,
    "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>Jamjoom Pharma (جمجوم فارما) / Acretin</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / علاجات حب الشباب والأدوية الجلدية</td></tr>
  <tr><th>نوع المنتج</th><td>كريم علاجي مقشر ومجدد للبشرة (Topical Retinoid Cream)</td></tr>
  <tr><th>الحجم/الوزن</th><td>30 جرام (30g Aluminum Tube)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الدهنية والمختلطة والمعرضة لحب الشباب والتغيرات التصبغية</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة متجددة، ملساء، موحدة اللون ومشدودة</td></tr>
  <tr><th>الملمس</th><td>كريم أبيض خفيف سريع الامتصاص</td></tr>
  <tr><th>العطر</th><td>خالٍ تماماً من العطور (Unfragranced)</td></tr>
  <tr><th>المكونات النشطة</th><td>تريتينوين 0.025% (Tretinoin 0.025% / Retinoic Acid)</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية (KSA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Jamjoom Pharmaceuticals Co.</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (12 سنة فما فوق بتحفظ طبي)</td></tr>
</tbody>
</table>`,
    "knowledge_base": `<h2>الدليل المعرفي الطبي لعلاج التريتينوين وتقشير البشرة بالأكريتين</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم أكريتين 0.025% حب الشباب الشائع (Acne Vulgaris)، البثور التكيسية والعميقة تحت الجلد، انسداد المسام، الآثار والتصبغات الناتجة عن الحبوب، خطوط التعبير السطحية، والقرنية الجريبية (Rough Skin Texture).</p>

<h3>لماذا تحدث مشكلة حب الشباب والتصبغات؟</h3>
<p>تحدث البثور عندما تبطؤ عملية التساقط الطبيعي لخلايا الجلد، فتتراكم الخلايا الميتة داخل القناة الجريبية وتختلط بالزهم. يؤدي هذا الكتمان إلى انتفاخ المسام وتكاثر البكتيريا. وعند اندمال البثور التهابياً، تترك خلفها بقعاً تصبغية داكنة (Post-Inflammatory Hyperpigmentation) ناتجة عن تحفيز خلايا الميلانين. التريتينوين يحل المشكلة من جذورها بتسريع الدورة الحيوية لتجدد الخلايا.</p>

<h3>نصائح وقائية لروتين علاج الأكريتين (Tretinoin Care)</h3>
<p>1. <strong>قاعدة (Less is More):</strong> كمية بحجم حبة البسلة تكفي للوجه بالكامل، زيادة الكمية لا تسرع العلاج بل تسبب الحروق.<br>2. <strong>تطبيق طريقة الساندويتش (Sandwich Technique):</strong> للمبتدئين: مرطب ثم أكريتين ثم مرطب لتقليل التهيج والجفاف.<br>3. <strong>التوقف عن المقشرات الأخرى:</strong> يمنع استخدام الأحماض (AHA/BHA) أو غسولات التقشير القوية بالتزامن مع الأكريتين.<br>4. <strong>الالتزام بالحماية الشمسية الصارمة:</strong> استخدام واقي الشمس SPF 50 وتجديده كل ساعتين نهاراً لمنع التصبغات العكسية.</p>

<h3>توصيات الخبراء وأطباء الجلدية</h3>
<p>يؤكد أطباء الجلدية أن كريم أكريتين 0.025% هو العلاج الأكثر إثباتاً سريرياً في العالم. ينصح الأطباء بالصبر الكامل، حيث تمر البشرة بمرحلة التطهير والتأقلم (Purging & Retinization) في أول 4-6 أسابيع، حيث تخرج الحبوب الكامنة وتتقشر البشرة، قبل أن تبدأ النتائج المذهلة في الظهور من الشهر الثاني. يُنصح بدعم حاجز البشرة بمرطبات تحتوي على السيراميد والبانثينول والحمض الهيالورونيكي.</p>

<h3>خرافات شائعة حول كريم الأكريتين</h3>
<p><strong>خرافة:</strong> "الأكريتين يرقق الجلد ويجعله ضعيفاً للأبد."<br><strong>الحقيقة:</strong> الأكريتين يقشر طبقة الخلايا الميتة السطحية الكراتينية فقط، ولكنه على المستوى العميق (الأدمة) يزيد من سمك البشرة ويحفز إنتاج الكولاجين والإيلاستين، مما يجعل الجلد أكثر قوة ومرونة وشباباً.</p>

<h3>التفسير العلمي لآلية العمل (Tretinoin 0.025%)</h3>
<p>ينتمي التريتينوين إلى الجيل الأول من الريتينويدات. يرتبط مباشرة بمستقبلات حمض الريتينويك النووية (Nuclear Retinoic Acid Receptors - RARs). هذا الارتباط يقلل من التماسك بين الخلايا القرنية (Corneocytes)، مما يسهل تساقطها ويمنع تكون انسدادات المسام (Microcomedones). كما يحفز النشاط الانقسامي لخلايا الطبقة القاعدة (Basal Layer)، ويمنع إنزيمات MMPs التي تكسر الكولاجين، مما يعزز بناء ألياف كولاجين جديدة.</p>`,
    "faqs": `<h3>ما هو كريم أكريتين 0.025% وما هي استخداماته؟</h3>
<p>أكريتين 0.025% هو كريم طبي يحتوي على التريتينوين (فيتامين أ الحمضي)، يستخدم لعلاج حب الشباب، تقشير المسام، تجديد خلايا البشرة، وتوحيد التصبغات.</p>
<h3>ما الفرق بين أكريتين 0.025% وأكريتين 0.05%؟</h3>
<p>أكريتين 0.025% يحتوي على نصف التركيز الموجود في 0.05%، وهو التركيز الابتدائي الموصى به للمبتدئين لتقليل الجفاف والتهيج أثناء فترة التأقلم.</p>
<h3>متى يُوضع كريم الأكريتين على الوجه؟</h3>
<p>يُوضع ليلاً فقط في الظلام قبل النوم، ويُغسل جيداً بالماء والغسول في الصباح، لأن مادة التريتينوين تتفكك بالضوء وتزيد حساسية الشمس.</p>
<h3>كم الكمية المناسبة لوضعها على الوجه؟</h3>
<p>الكمية الطبية الموصى بها هي بحجم حبة البسلة الصغيرة فقط للوجه بالكامل. زيادة الكمية لا تسرع النتائج بل تسبب احمراراً وحروقاً جلديّة.</p>
<h3>هل يجب تجفيف الوجه قبل وضع الأكريتين؟</h3>
<p>نعم، يجب الانتظار 20-30 دقيقة بعد غسل الوجه حتى تجف البشرة تماماً. تطبيق الأكريتين على بشرة مبللة يزيد من امتصاصه السريع وتهيج الجلد.</p>
<h3>هل كريم أكريتين مناسب للحوامل والمرضعات؟</h3>
<p>لا، كريم الأكريتين ممنوع منعاً باتاً أثناء الحمل والرضاعة لاحتمالية تسببه في تشوهات للجنين.</p>
<h3>هل يسبب الأكريتين زيادة الحبوب في البداية (Purging)؟</h3>
<p>نعم، في أول 2-4 أسابيع قد تظهر حبوب جديدة وتتقشر البشرة (مرحلة التطهير)، وهو أمر طبيعي يعبر عن خروج الحبوب الكامنة تحت الجلد.</p>
<h3>كيف أتجنب الجفاف والتهيج الشديد من الأكريتين؟</h3>
<p>ابدأي بالتدريج (مرتين أسبوعياً)، واستخدمي طريقة الساندويتش (مرطب ثم أكريتين ثم مرطب)، واحرصي على استخدام مرطب غني بالسيراميد.</p>
<h3>هل يوضع واقي شمس عند استخدام الأكريتين؟</h3>
<p>نعم، استخدام واقي الشمس SPF 50 صباحاً ضروري إجباري يومياً، لأن التريتينوين يجعل البشرة شديدة الحساسية لأشعة الشمس.</p>
<h3>هل يساعد الأكريتين في علاج الآثار والتصبغات؟</h3>
<p>نعم، يسرع من تساقط الخلايا الملونة بالميلانين ويحفز بناء خلايا جديدة موحدة اللون، مما يزيل آثار الحبوب الداكنة تدريجياً.</p>
<h3>هل يمكن استخدام الأكريتين حول العينين والشفتين؟</h3>
<p>لا، يجب تجنب وضع الأكريتين بالقرب من زوايا العينين، حول الشفتين، وحواف الأنف، لأن الجلد في هذه المناطق رقيق جداً وعرضة للاحتراق.</p>
<h3>كم يستغرق الأكريتين لإظهار النتائج النهائية؟</h3>
<p>تبدأ النضارة وقلة الحبوب بالظهور خلال 4 إلى 8 أسابيع، بينما النتائج الكاملة لعلاج حب الشباب والتصبغات تظهر خلال 3 إلى 6 أشهر من الالتزام.</p>
<h3>هل يمكن استخدام حمض الساليسليك أو مقشرات أخرى مع الأكريتين؟</h3>
<p>يُفضل تجنب استخدام المقشرات الكيميائية والأحماض الأخرى في نفس وقت استخدام الأكريتين لتجنب تدمير حاجز البشرة.</p>
<h3>ما العمل إذا حدث حرقان أو احمرار شديد في البشرة؟</h3>
<p>توقفي عن استخدام الأكريتين لعدة أيام، وركزي على الترطيب المكثف بكريم مهدئ مثل البانثينول حتى تتعافى البشرة ثم عودي بتدرج أقل.</p>
<h3>هل يمكن استخدام كريم الأكريتين لعلاج حب الشباب في الجسم؟</h3>
<p>نعم، يمكن استخدامه بحذر على الحبوب والتصبغات في مناطق الظهر والصدر بعد استشارة الطبيب الصيدلي.</p>
<h3>هل يسبب الأكريتين ترقيق الجلد؟</h3>
<p>لا، الأكريتين يحفز إنتاج الكولاجين في الأدمة مما يزيد سمك وقوة طبقات الجلد الداخلية الحقيقية.</p>
<h3>ما هي طريقة الساندويتش لتطبيق الأكريتين؟</h3>
<p>هي وضع طبقة مرطب خفيف، ثم الانتظار 10 دقائق وتطبيق الأكريتين، ثم الانتظار 10 دقائق وتطبيق طبقة مرطب ثانية لتقليل التهيج.</p>
<h3>هل يسبب الأكريتين اسمرار البشرة؟</h3>
<p>الأكريتين لا يسبب الاسمرار بنفسه، ولكن عدم استخدام واقي الشمس نهاراً أثناء فترة العلاج هو ما يسبب التصبغ والاسمرار العكسي.</p>
<h3>هل يحتاج الأكريتين إلى غسول خاص؟</h3>
<p>يُفضل استخدامه مع غسول لطيف خالٍ من الصابون والعطور والأحماض، لحماية حاجز البشرة من التهيج.</p>
<h3>هل الأكريتين مناسب لعمر المراهقين؟</h3>
<p>نعم، يُصرح باستخدامه للمراهقين من عمر 12 سنة فما فوق لعلاج حب الشباب الهرموني تحت إشراف طبي.</p>
<h3>ما هو حجم عبوة كريم أكريتين 0.025%؟</h3>
<p>تأتي العبوة في أنبوب ألومنيوم بحجم 30 جرام تصنعه شركة جمجوم فارما.</p>
<h3>كيف يُحفظ كريم أكريتين؟</h3>
<p>يُحفظ في درجة حرارة أقل من 25 درجة مئوية بعيداً عن الحرارة المباشرة وأشعة الشمس، وبعيداً عن متناول الأطفال.</p>
<h3>هل كريم أكريتين جمجوم فارما أصلي لدى صيدلية إكليل أبها؟</h3>
<p>نعم، كريم أكريتين دوايات ومستحضر طبي أصلي 100% مسجل ومضمون لدى صيدلية إكليل أبها السعودية.</p>
<h3>هل يمكن استخدام المكياج أثناء فترة العلاج بالأكريتين؟</h3>
<p>نعم، يمكن وضع المكياج نهاراً، ولكن يُفضل استخدام منتجات غير سادة للمسام وإزالتها بلطف بغسول ميسيلار قبل وضع الأكريتين ليلاً.</p>
<h3>هل يساعد الأكريتين في تصغير المسام الواسعة؟</h3>
<p>نعم، من خلال تفريغ المسام من السدادات الدهنية وتحفيز الكولاجين حول جدران المسام، تبدو المسام أصغر حجماً وأكثر مرونة.</p>`,
    "tags": ["acretin", "tretinoin", "jamjoom_pharma", "acne_cream", "ekleel_abha"]
  },
  "en": {
    "title": "Acretin Acne Treatment & Skin Renewing Cream 0.025% - 30g Jamjoom Pharma",
    "meta_title": "Acretin Cream 0.025% Acne Treatment 30g | Ekleel Abha",
    "meta_description": "Buy Acretin Cream 0.025% (30g) by Jamjoom Pharma. Clinical tretinoin formula for acne, pore unclogging & skin renewal. 100% authentic at Ekleel Abha Pharmacy.",
    "description": `<h2>Product Overview</h2>
<p><strong>Acretin Cream 0.025% (30g Jamjoom Pharma)</strong> represents the gold-standard prescription dermatological treatment for acne vulgaris, hyperpigmentation, and cutaneous texture renewal across Saudi Arabia and the Middle East. Expertly manufactured by Jamjoom Pharmaceuticals, this clinical cream is powered by <strong>Tretinoin 0.025% (Retinoic Acid)</strong>—the most biologically active form of Vitamin A proven to transform skin cellular behavior.</p>
<p>Acretin 0.025% works at the cellular level by dramatically accelerating epidermal cell turnover, unclogging congested hair follicles, shedding hyperkeratinized dead skin cells, and suppressing microcomedone formation. The <strong>0.025% concentration</strong> is specifically recognized as the ideal starter strength for tretinoin therapy, allowing the skin to build tolerance during the retinization phase while minimizing erythema, severe dryness, and peeling, resulting in a refined, blemish-free, and youthful skin texture.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Dermatological Gold Standard (Tretinoin 0.025%):</strong> Effectively treats acne vulgaris, inflammatory pustules, and deep microcomedones by regulating cellular differentiation.</li>
  <li><strong>Accelerates Epidermal Turnover:</strong> Promotes rapid shedding of dead surface skin cells and stimulates the birth of fresh, healthy epidermal layers.</li>
  <li><strong>Unclogs & Refines Pores:</strong> Clears follicular keratin plugs and trapped sebum, drastically reducing blackheads and whiteheads.</li>
  <li><strong>Fades Post-Acne Marks & Hyperpigmentation:</strong> Disperses melanin clusters from post-inflammatory hyperpigmentation while boosting dermal collagen synthesis.</li>
  <li><strong>Ideal Starter Strength (0.025%):</strong> Enables gradual cutaneous adaptation with significantly reduced irritation compared to higher concentrations (0.05%).</li>
</ul>

<h2>Pharmacist Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleansing & Complete Drying):</strong> Wash face with a mild, non-acidic cleanser and wait 20-30 minutes until skin is completely dry before application (applying to damp skin increases irritation risk).</li>
  <li><strong>Step 2 (Pea-Sized Amount):</strong> Dispense a small pea-sized amount onto fingertip and dot evenly across forehead, cheeks, and chin.</li>
  <li><strong>Step 3 (Application & Delicate Area Avoidance):</strong> Smooth gently across the face, strictly avoiding the corners of the eyes, nostrils, and lips.</li>
  <li><strong>Step 4 (Gradual Retinization):</strong> Use strictly at night. Start 2 nights per week for the first 2 weeks, then alternate nights, advancing to nightly use as skin tolerance permits.</li>
  <li><strong>Step 5 (Moisturizing & Sun Protection):</strong> Apply a soothing ceramide/panthenol moisturizer 20 minutes after Acretin application at night. Always apply SPF 50 sunscreen during the day.</li>
</ul>

<h2>Active Ingredients Overview</h2>
<p>The active pharmaceutical ingredient is <strong>Tretinoin 0.025% w/w</strong> in an easily absorbed dermatological cream base. Tretinoin binds directly to nuclear Retinoic Acid Receptors (RARs), modulating gene expression related to cellular mitosis, lipid secretion, and extracellular matrix synthesis.</p>

<h2>Warnings & Precautions</h2>
<ul>
  <li><strong>Strictly Contraindicated During Pregnancy & Breastfeeding:</strong> Topical tretinoin must never be used during pregnancy, breastfeeding, or by women planning pregnancy due to potential teratogenic risks.</li>
  <li>For nighttime external dermatological use only. Avoid exposure to sun lamps, UV rays, or bright artificial light while wearing the cream.</li>
  <li>Broad-spectrum sunscreen (SPF 50) must be applied every morning throughout the treatment period to prevent photosensitivity burns and hyperpigmentation.</li>
  <li>Do not apply to sunburned, abraded, cut, or eczematous skin.</li>
</ul>

<h2>Who Is This For?</h2>
<p>Formulated for adults and adolescents managing acne vulgaris, post-acne dark marks, rough keratinized texture, congested pores, and premature signs of photoaging under professional medical guidance.</p>`,
    "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Jamjoom Pharma / Acretin</td></tr>
  <tr><th>Category</th><td>Skin Care / Acne Treatments & Retinoids</td></tr>
  <tr><th>Product Type</th><td>Prescription-Strength Retinoid Cream</td></tr>
  <tr><th>Volume/Weight</th><td>30g Aluminum Tube</td></tr>
  <tr><th>Skin/Hair Type</th><td>Oily, Combination, Acne-Prone & Hyperpigmented Skin</td></tr>
  <tr><th>Finish</th><td>Renewed, Smooth, Firm & Even-Toned Finish</td></tr>
  <tr><th>Texture</th><td>Smooth White Light Absorbing Cream</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-Free / Unfragranced</td></tr>
  <tr><th>Active Ingredients</th><td>Tretinoin 0.025% w/w (Retinoic Acid)</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia (KSA)</td></tr>
  <tr><th>Manufacturer</th><td>Jamjoom Pharmaceuticals Co.</td></tr>
  <tr><th>Age Group</th><td>Adults & Adolescents (12+ Years Under Guidance)</td></tr>
</tbody>
</table>`,
    "knowledge_base": `<h2>Clinical Insights on Tretinoin Therapy & Skin Renewal</h2>

<h3>What Problem Does This Product Solve?</h3>
<p>Acretin 0.025% Cream treats inflammatory and non-inflammatory acne vulgaris, deep subcutaneous bumps, blackheads, whiteheads, post-inflammatory hyperpigmentation (PIH), coarse skin texture, and early facial fine lines.</p>

<h3>Why Do Acne & Hyperpigmentation Occur?</h3>
<p>Acne manifests when follicular desquamation slows down, causing dead keratinocytes to adhere to one another and trap sebum. This blockage expands hair follicles and fosters an anaerobic environment for <em>Cutibacterium acnes</em> proliferation. When inflammatory lesions heal, abnormal melanin deposition leaves persistent dark spots (PIH). Tretinoin resolves these root causes by accelerating mitotic renewal and dispersing localized pigment.</p>

<h3>Prevention Tips for Tretinoin Therapy</h3>
<p>1. <strong>Strict Adherence to "Pea-Sized" Rule:</strong> A pea-sized amount is sufficient for the entire face. Excessive application causes chemical burns without speeding results.<br>2. <strong>Employ the Sandwich Method:</strong> Apply moisturizer, wait 10 minutes, apply Acretin, wait 10 minutes, and follow with another layer of moisturizer to mitigate dryness.<br>3. <strong>Pause Chemical Exfoliants:</strong> Cease using AHAs, BHAs, and exfoliating scrubs while undergoing tretinoin therapy to protect the skin barrier.<br>4. <strong>Daily Broad-Spectrum Sunscreen:</strong> Apply SPF 50 daily and reapply every 2 hours outdoors to prevent rebound hyperpigmentation.</p>

<h3>Professional Recommendations</h3>
<p>Dermatologists regard Tretinoin 0.025% as one of the most thoroughly validated topical agents in medicine. Patients are advised to anticipate the "Purging and Retinization" phase during weeks 2 to 6, characterized by temporary breakout surfacing and mild desquamation. Clinical improvements accelerate significantly by week 8. Supporting the skin barrier with ceramide-rich, non-comedogenic moisturizers is strongly recommended throughout treatment.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Tretinoin thins out your skin permanently."<br><strong>Fact:</strong> Tretinoin compacts only the outermost dead stratum corneum, while substantially increasing dermal thickness, collagen density, and elastic fiber organization over time, leading to stronger, healthier skin.</p>

<h3>Scientific Explanation of Mechanism (Tretinoin 0.025%)</h3>
<p>Tretinoin (all-trans retinoic acid) binds directly to nuclear Retinoic Acid Receptors (RAR-alpha, beta, and gamma). This interaction alters gene transcription, decreasing cell cohesion in the stratum corneum and accelerating desquamation of follicular comedones. Furthermore, tretinoin downregulates matrix metalloproteinase (MMP) enzymes that break down collagen, while simultaneously stimulating fibroblasts to synthesize fresh Type I and III collagen fibers.</p>`,
    "faqs": `<h3>What is Acretin 0.025% Cream and what is it used for?</h3>
<p>Acretin 0.025% is a clinical dermatological cream containing Tretinoin (retinoic acid), used for treating acne vulgaris, clearing clogged pores, accelerating cell turnover, and fading post-acne marks.</p>
<h3>What is the difference between Acretin 0.025% and 0.05%?</h3>
<p>Acretin 0.025% contains half the tretinoin concentration of 0.05%. It is the recommended starter strength for beginners to build skin tolerance with minimal irritation.</p>
<h3>When should Acretin Cream be applied?</h3>
<p>Apply strictly at night in the dark before bedtime. Wash off thoroughly in the morning with a gentle cleanser, as tretinoin degrades in sunlight and increases solar sensitivity.</p>
<h3>How much Acretin Cream should be used per application?</h3>
<p>A single pea-sized amount is sufficient for the entire face. Using more product will not speed up results and will cause unnecessary redness, peeling, and skin burns.</p>
<h3>Why must skin be completely dry before applying Acretin?</h3>
<p>Wait 20-30 minutes after washing your face before applying Acretin. Applying tretinoin to damp skin increases rapid absorption, leading to severe irritation and burning.</p>
<h3>Is Acretin safe during pregnancy or breastfeeding?</h3>
<p>No, Acretin (tretinoin) is strictly contraindicated during pregnancy, planning for pregnancy, and breastfeeding due to potential teratogenic risks.</p>
<h3>Does Acretin cause skin purging initially?</h3>
<p>Yes, temporary skin purging (surfacing of underlying microcomedones and mild peeling) often occurs during weeks 2 to 4. Continued use reveals clear, smooth skin.</p>
<h3>How can I prevent dryness and irritation while using Acretin?</h3>
<p>Introduce it gradually (twice a week initially), use the sandwich moisturizing method (moisturizer-acretin-moisturizer), and use ceramide-rich soothing creams.</p>
<h3>Is sunscreen mandatory when using Acretin?</h3>
<p>Yes, applying a broad-spectrum SPF 50 sunscreen every morning is mandatory, as tretinoin makes the skin extremely vulnerable to sun damage and dark spots.</p>
<h3>Does Acretin help fade acne scars and hyperpigmentation?</h3>
<p>Yes, tretinoin accelerates the shedding of melanin-pigmented surface cells while boosting collagen, effectively fading post-acne dark marks over time.</p>
<h3>Can Acretin be applied around the eyes and lips?</h3>
<p>No, avoid applying Acretin near the corners of the eyes, nostrils, and mouth, as the skin in these areas is extremely delicate and prone to cracking.</p>
<h3>How long does it take to see full results with Acretin?</h3>
<p>Initial texture refinement and acne reduction appear in 4 to 8 weeks. Maximum clearance of acne and hyperpigmentation is achieved after 3 to 6 months of consistent use.</p>
<h3>Can I use Salicylic Acid or AHA products while using Acretin?</h3>
<p>It is best to avoid using other chemical exfoliants and acids simultaneously with tretinoin to prevent severe skin barrier breakdown.</p>
<h3>What should I do if my skin develops severe redness or burning?</h3>
<p>Pause Acretin application for a few days, focus heavily on hydrating with panthenol/ceramide creams until skin barrier recovers, then resume at a lower frequency.</p>
<h3>Can Acretin be used for body acne?</h3>
<p>Yes, it can be used cautiously for back and chest acne after consulting a healthcare professional.</p>
<h3>Does tretinoin thin the skin over time?</h3>
<p>No, tretinoin only thins the outermost layer of dead cells while increasing dermal collagen synthesis, resulting in thicker, firmer, and stronger skin.</p>
<h3>What is the "Sandwich Technique" for applying tretinoin?</h3>
<p>It involves applying a layer of moisturizer, waiting 10 minutes, applying a pea-sized amount of Acretin, waiting another 10 minutes, and finishing with another layer of moisturizer.</p>
<h3>Can Acretin cause skin darkening?</h3>
<p>Acretin itself does not darken skin, but failing to wear SPF 50 sunscreen during daytime solar exposure can cause photosensitive hyperpigmentation.</p>
<h3>What kind of cleanser should be used with Acretin?</h3>
<p>Use a gentle, soap-free, unfragranced, and non-acidic cleanser to maintain skin barrier health during tretinoin therapy.</p>
<h3>Is Acretin suitable for teenagers?</h3>
<p>Yes, it is indicated for adolescents aged 12 and above experiencing moderate to severe acne under dermatological supervision.</p>
<h3>What size is the Acretin 0.025% tube?</h3>
<p>It comes in a 30g aluminum tube manufactured by Jamjoom Pharmaceuticals.</p>
<h3>How should Acretin Cream be stored?</h3>
<p>Store below 25°C in a dry place away from direct heat and sunlight, and keep out of reach of children.</p>
<h3>Is Jamjoom Pharma Acretin authentic at Ekleel Abha Pharmacy?</h3>
<p>Yes, it is 100% authentic pharmaceutical-grade product registered and guaranteed at Ekleel Abha Pharmacy in Saudi Arabia.</p>
<h3>Can I wear makeup while undergoing Acretin treatment?</h3>
<p>Yes, you can wear non-comedogenic makeup during the day. Ensure you remove it gently at night with micellar water before applying Acretin.</p>
<h3>Does Acretin reduce the appearance of enlarged pores?</h3>
<p>Yes, by clearing pore-clogging debris and stimulating surrounding collagen structure, Acretin makes enlarged pores appear significantly smaller and tighter.</p>`
  },
  "schema": {
    "brand": "Jamjoom Pharma",
    "category": "Skin Care / Acne Treatments & Retinoids",
    "availability": "InStock"
  },
  "image_seo": {
    "image_filename": "acretin-acne-treatment-cream-0025-30g-jamjoom-pharma.webp",
    "alt": "Acretin Acne Treatment Cream 0.025% 30g Jamjoom Pharma",
    "title": "Acretin Acne Treatment Cream 0.025% 30g Jamjoom Pharma"
  }
};

const products = [prod1411, prod1412, prod1413];

products.forEach(p => {
  const filePath = path.join(targetDir, `${p.product_id}.json`);
  fs.writeFileSync(filePath, JSON.stringify(p, null, 2), 'utf8');
  console.log(`✅ Saved ${filePath} (Size: ${fs.statSync(filePath).size} bytes)`);
});

console.log('✨ All assigned product JSON files generated successfully!');
