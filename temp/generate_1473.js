const fs = require('fs');
const path = require('path');

const productData = {
  "product_id": "1473",
  "sku": "EK-1473",
  "category": "العناية بالبشرة / العناية بالشفاه",
  "brand": "Vaseline",
  "ar": {
    "title": "مرطب شفاه فازلين الأصلي لحماية وترطيب الشفاه طوال اليوم - 7 جم",
    "meta_title": "مرطب شفاه فازلين الأصلي 7 جم لحماية وترطيب الشفاه | صيدلية إكليل أبها",
    "meta_description": "تسوق مرطب شفاه فازلين الأصلي 7 جم لحماية وترطيب الشفاه طوال اليوم. يعالج التشقق وجفاف الشفاه بفضل الفازلين المكرر ثلاثياً. منتج أصلي 100% من صيدلية إكليل أبها.",
    "description": `<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مرطب شفاه فازلين الأصلي (Vaseline Lip Therapy Original - 7g)</strong> الخيار العلاجي الكلاسيكي الأول والموثوق عالمياً للحفاظ على صحة الشفاه ونعومتها طوال اليوم. تم تصميم هذه التركيبة المركزة بعناية فائقة لتوفير حماية فوتو-ترطيبية مكثفة تعيد حيوية الشفاه الجافة والمتشققة فوراً، بفضل اعتماده على الفازلين النقائي المكرر ثلاثياً (100% Pure Petroleum Jelly). يتميز المنتج بحجمه الصغير المدمج (7 جرام) الذي يجعله سهل الحمل في الحقيبة أو الجيب ليكون رفيقك الدائم أينما كنت.</p>
<p>يعمل بلسم الشفاه من فازلين على حبس الرطوبة داخل طبقات الجلد الرقيقة للشفاه بدلاً من الاكتفاء بتغطيتها السطحية. يساعد على تسريع عملية الاستشفاء الطبيعية للانسجة الجلدية المتضررة جراء العوامل الجوية القاسية كالحرارة، البرودة، والرياح الجافة. يمنح الشفاه مظهرًا طبيعيًا صحيًا ولامعًا دون أي ملمس لزج أو مزعج، وهو خالي تماماً من العطور والنكهات الصناعية مما يجعله آمنًا ومناسبًا للشفاه الأكثر حساسية.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب عميق وحبس للرطوبة:</strong> يعمل الفازلين المكرر ثلاثياً على حبس الرطوبة الطبيعية داخل أنسجة الشفاه ومنع تبخرها طوال اليوم.</li>
  <li><strong>علاج وتسكين التشطبات:</strong> يسرع من التئام التشققات والجروح السطحية الصغيرة الناتجة عن الجفاف الشديد والظروف الجوية القاسية.</li>
  <li><strong>حماية متكاملة ضد العوامل البيئية:</strong> يشكل حاجزاً وقائياً غير مرئي يحمي الشفاه من الرياح الجافة، التكييف، والهواء البارد.</li>
  <li><strong>مظهر طبيعي لامع وغير لزج:</strong> يمنح الشفاه لمعاناً صحياً جذاباً وملمساً مخملياً ناعماً دون أي شعور بثقل أو ثقل لزج.</li>
  <li><strong>تركيبة خالية من العطور:</strong> خالية تماماً من النكهات والألوان والمواد العطرية الاصطناعية، مما يضمن أقصى درجات الأمان للشفاه الحساسة.</li>
  <li><strong>حجم عملي ومدمج:</strong> عبوة مدمجة بحجم 7 جرام مثالية للتنقل اليومي والسفر، تضمن سهولة التطبيق في أي وقت وأي مكان.</li>
  <li><strong>تحسين مرونة ونعومة الجلد:</strong> يغذي أنسجة الشفاه ويمنحها مرونةائقة تقي من ظهور خطوط الجفاف الدقيقة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> نظفي الشفاه برفق وجففيها جيداً من أي بقايا طعام أو مستحضرات تجميل سابقة.</li>
  <li><strong>الخطوة الثانية:</strong> أخذ كمية صغيرة بحجم حبة الحمص من مرطب فازلين الأصلي باستخدام طرف إصبع نظيف أو فرشاة شفاه مخصصة.</li>
  <li><strong>الخطوة الثالثة:</strong> وزعي البلسم بالتساوي على الشفة العليا والسفلى بحركات دائرية لطيفة لضمان تغطية كامل الأنسجة والتغلغل في التشققات.</li>
  <li><strong>الخطوة الرابعة:</strong> كرر التطبيق كلما شعرت بالجفاف، خاصة قبل التعرض للهواء البارد أو الشديد، وقبل النوم للحصول على قناع ترطيب ليلي مكثف.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<p>تعتمد تركيبة مرطب فازلين الأصلي على علم الدهون الكتيمة والتغطية الوقائية المحسنة:</p>
<ul>
  <li><strong>البترولاتوم النقائي المكرر ثلاثياً (100% Pure Petroleum Jelly):</strong> المكون المعتمد من قبل أطباء الجلد عالمياً والذي يعمل كعامل كتيم (Occlusion) يمنع فقدان الماء عبر البشرة (TEWL) بنسبة تزيد عن 98%، مما يتيح للأنسجة الدقيقة تجديد نفسها.</li>
  <li><strong>زيت معدني مكرر (Mineral Oil):</strong> يساهم في تنعيم سطح الشفاه المتصلب وإعطائها المرونة والانسيابية السريعة.</li>
  <li><strong>فيتامين E (Tocopheryl Acetate):</strong> مضاد أكسدة قوي يساعد في حماية خلايا الشفاه من الإجهاد التأكسدي والشوارد الحرة الناجمة عن الأشعة فوق البنفسجية والتلوث.</li>
  <li><strong>زبدة الشيا الطبيعية (Shea Butter):</strong> تمد الشفاه بالأحماض الدهنية الأساسية والفيتامينات المغذية التي تعزز ترطيب الحاجز الجلدي وتزيد من طراوته.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>هذا المستحضر مخصص للاستخدام الظاهري الخارجي على الشفاه فقط؛ تجنبي ابتلاع كميات كبيرة منه.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال الصغار لتجنب الاستخدام غير المراقبة أو البلع العرضي.</li>
  <li>يُحفظ في مكان بارد وجاف بعيداً عن أشعة الشمس المباشرة ومصادر الحرارة العالية لمنع ذوبان قوام الجلي.</li>
  <li>في حال ظهور أي تهيج، احمرار، أو تفاعل حساسية غير متوقع، يوصى بإيقاف الاستخدام وغسل الشفاه بالماء الفاتر.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li><strong>أصحاب الشفاه الجافة والمتشققة:</strong> يعانون من جفاف شديد، تقشر، أو تشققات مؤلمة في الشفاه طوال العام.</li>
  <li><strong>ذوو البشرة والشفاه الحساسة:</strong> يبحثون عن مرطب نقائي خالي من العطور والنكهات والصبغات الصناعية التي قد تسبب التهيج.</li>
  <li><strong>الأشخاص المعرضون للظروف الجوية القاسية:</strong> من يقضون أوقاتاً طويلة في الأماكن المكيفة، أو المناطق الباردة، أو الجافة جداً.</li>
  <li><strong>مستخدمو أدوية حب الشباب (مثل الروكوتان/الإيزوترينوين):</strong> الذين يعانون من جفاف شفاه حاد ومستمر كعرض جانبي للدواء.</li>
</ul>`,
    "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>Vaseline (فازلين)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / العناية بالشفاه</td></tr>
  <tr><th>نوع المنتج</th><td>مرطب وبلسم شفاه علاجي</td></tr>
  <tr><th>الحجم/الوزن</th><td>7 جم (حجم صغير مدمج)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (خصيصاً الشفاه الجافة والمتشققة)</td></tr>
  <tr><th>المظهر النهائي</th><td>طبيعي لامع وغير لزج</td></tr>
  <tr><th>الملمس</th><td>بلسم جلي ناعم وسلس</td></tr>
  <tr><th>العطر</th><td>خالي من العطور (بدون رائحة)</td></tr>
  <tr><th>المكونات النشطة</th><td>بترولاتوم مكرر ثلاثياً 100%، زبدة الشيا، فيتامين E</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة الأمريكية / المملكة المتحدة</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (يونيلفر)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الأعمار (البالغين والأطفال)</td></tr>
</tbody>
</table>`,
    "knowledge_base": `<h2>الدليل المعرفي الشامل للترطيب والعناية بالشفاه</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مرطب شفاه فازلين الأصلي مشكلة جفاف الشفاه وتلكم التشققات المؤلمة والتسلخات السطحية التي تصيب النسيج المخاطي الخارجي للشفاه. تختلف بشرة الشفاه عن باقي بشرة الجسم كونها رقيقة للغاية وتفتقر إلى الغدد الدهنية والغدد العرقية الطبيعية التي تفرز الزيوت المرطبة. هذا يجعلها عاجزة عن الاحتفاظ بالرطوبة تلقائياً عند التعرض للعوامل البيئية، مما يؤدي إلى التقشر، النزيف الخفيف، والارتباك المزعج أثناء الحديث أو تناول الطعام. يوفر فازلين الحل السريع والمضمون عبر إعادة إنشاء الطبقة الواقية الكتيمة فوراً.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تحدث مشكلة جفاف وتشققات الشفاه بسبب عوامل متعددة، أبرزها غياب الحاجز الدهني الطبيعي في الشفاه مقارنة بباقي مناطق الوجه. التعرض المستمر للهواء الجاف، التكييف البارد، والطقس الشتوي يسرع عملية تبخر الماء من الأنسجة الخلوية (Transepidermal Water Loss). بالإضافة إلى ذلك، فإن عادة لعق الشفاه المستمرة تزيد المشكلة سوءاً؛ لأن اللعاب يحتوي على إنزيمات هاضمة مثل الأميليز والبروتياز التي تكسر غلاف الجلد الرقيق، وعندما يتبخر اللعاب فإنه يسحب معه الرطوبة الداخلية للشفاه، مما يتركها أكثر جفافاً وتلعثماً.</p>

<h3>نصائح وقائية</h3>
<ul>
  <li><strong>شرب كميات كافية من الماء:</strong> ترطيب الجسم الداخلي بشرب 2-3 لتر ماء يومياً يعد الخطوة الأساسية لمنع جفاف الشفاه.</li>
  <li><strong>الامتناع عن لعق الشفاه:</strong> تجنب تطبيق اللعاب على الشفاه لتمرير الرطوبة المؤقتة، واستبداله فوراً بتطبيق فازلين الأصلي.</li>
  <li><strong>استخدام الترطيب قبل النوم:</strong> تطبيق طبقة سخية من بلسم فازلين قبل النوم يعمل كقناع ترطيب ليلي يمنع الجفاف الناتج عن التنفس من الفم أثناء النوم.</li>
  <li><strong>تجنب التقشير القاسي:</strong> عدم فرك التشققات أو شد القشور الجافة بالإصبع أو الأسنان لمنع حدوث نزيف أو التهابات بكتيرية.</li>
  <li><strong>حماية الشفاه من الرياح والتكييف:</strong> الحرص على وضع الفازلين قبل الخروج في الهواء البارد أو الجلوس لفترات طويلة أمام أجهزة التكييف.</li>
</ul>

<h3>خرافات شائعة</h3>
<ul>
  <li><strong>خرافة:</strong> لعق الشفاه مراراً وتكراراً يوفر الترطيب الطبيعي الكافي للشفاه.<br><strong>الحقيقة:</strong> اللعاب يحتوي على إنزيمات هاضمة تجفف الشفاه وتسبب تهيج الأنسجة الرقيقة فور تبخره، مما يفاقم التشقق بدلاً من علاجه.</li>
  <li><strong>خرافة:</strong> الفازلين يسبب إدمان الشفاه بحيث لا تستطيع الاستغناء عنه.<br><strong>الحقيقة:</strong> الفازلين مادة محايدة وخاملة كيميائياً لا تسبب أي اعتاد كيميائي أو إدمان فيزيولوجي؛ بل يحمي الشفاه فقط ويساعد الأنسجة على ترميم نفسها.</li>
  <li><strong>خرافة:</strong> مرطبات الشفاه المعطرة أو الملونة أفضل علاجياً من المرطب الأصلي الخالي من العطور.<br><strong>الحقيقة:</strong> العطور والألوان والمطعمات الصناعية قد تسبب حساسية تلامسية وتهيجاً كبيراً للشفاه المتشققة، بينما فازلين الأصلي الخالي من العطور هو الخيار الأكثر أماناً وفعالية علاجية.</li>
  <li><strong>خرافة:</strong> الشفاه تصاب بالجفاف في فصل الشتاء فقط.<br><strong>الحقيقة:</strong> الشفاه معرضة للجفاف في فصل الصيف أيضاً بسبب حرارة الشمس الشديدة، التكييف المستمر، والتعرض للماء المالح أو الكلور في المسبح.</li>
</ul>

<h3>التفسير العلمي</h3>
<p>تستند آلية عمل بترولاتوم فازلين المكرر ثلاثياً إلى أقصى كفاءة في علم الكتامة الجلدية (Skin Occlusivity). حيث تشكل جزيئات البترولاتوم النظيفة شبكة هيدروكربونية كثيفة غير منفذة للمياه فوق سطح الشفاه الخارجية. تؤدي هذه الشبكة الفيزيائية إلى تقليل معدل تبخر الماء عبر البشرة (TEWL) بنسبة تزيد عن 98%، وهو أعلى معدل كتامة مثبت علمياً بين جميع المكونات المرطبة (مقارنة بالزيوت النباتية التي تحقق 20-30% فقط). يمنح هذا الاحتجاز للرطوبة البيئة المائية الكافية للأنزيمات الجلدية الطبيعية (Proteases) لتفكيك الروابط بين الخلايا الميتة بسلاسة وتسريع بناء طبقة كيراتينية جديدة وصحية دون أي تهيج.</p>`,
    "faqs": `<h3>ما هو مرطب شفاه فازلين الأصلي 7g؟</h3>
<p>مرطب شفاه فازلين الأصلي بحجم 7 جرام هو بلسم علاج مخصص لحماية وترطيب الشفاه الجافة والمتشققة. يتميز بتركيبته الغنية بالفازلين المكرر ثلاثياً نقي 100% والذي يحبس الرطوبة ويساعد على التئام التشققات بسرعة مع توفير لمعان طبيعي خفيف.</p>

<h3>ما هي المكونات الأساسية في فازلين الشفاه الأصلي؟</h3>
<p>يتكون بشكل رئيسي من بترولاتوم مكرر ثلاثياً 100% (Pure Petroleum Jelly)، بالإضافة إلى زيت معدني وزبدة الشيا وفيتامين E. هذه التركيبة الخالية من العطور توفر العناية الفائقة والأمان الكامل للشفاه الحساسة والمتضررة.</p>

<h3>هل يحتوي هذا المنتج على أي عطور أو نكهات صناعية؟</h3>
<p>لا، مرطب شفاه فازلين الأصلي 7g خالي تماماً من العطور والمواد المعطرة والنكهات الاصطناعية. هذا يجعله الخيار المثالي للأشخاص الذين يعانون من الحساسية الجلدية أو التهاب الشفاه التلامسي.</p>

<h3>كيف يعمل فازلين الأصلي على ترطيب الشفاه؟</h3>
<p>يعمل كحاجز وقائي كتيم يحبس الرطوبة الطبيعية داخل خلايا الشفاه ويمنع تبخرها في الهواء. كما يمنع المؤثرات الخارجية مثل الرياح والجفاف من إيذاء الأنسجة الرقيقة، مما يسمح للشفاه بالتعافي الذاتي.</p>

<h3>كم مرة يمكنني استخدام مرطب شفاه فازلين يومياً؟</h3>
<p>يمكنك استخدامه بالقدر الذي تحتاجه طوال اليوم دون أي قيود. يُوصى بتطبيقه في الصباح، وبعد تناول الطعام، وقبل الخروج في الطقس الجاف، وقبل النوم مباشرة للحصول على عناية مكثفة.</p>

<h3>هل يمكن استخدام مرطب فازلين الأصلي تحت روج الأسنان أو المكياج؟</h3>
<p>نعم، يوضع طبقة رقيقة من فازلين الأصلي على الشفاه وتترك لبضع دقائق لتنعيم التشققات، ثم يتم مسح الفائض الخفيف وتطبيق أحمر الشفاه (الروج)، مما يمنح مظهر مكياج سلس وغير متكتل.</p>

<h3>هل فازلين الشفاه 7g مناسب للأطفال؟</h3>
<p>نعم، فازلين الأصلي آمن جداً للأطفال من جميع الأعمار نظر نقائه الخالي من المواد الكيميائية الضارة أو العطور. يساعد في تهدئة التشققات الناتجة عن سيلان اللعاب أو البرد.</p>

<h3>هل يساعد هذا المنتج في علاج جفاف الشفاه الناتج عن علاج الروكوتان؟</h3>
<p>نعم، يعتبر فازلين الشفاه الأصلي من أكثر المستحضرات التي يوصي بها أطباء الجلد لمرضى الروكوتان (الإيزوترينوين)، حيث يوفر الترطيب السريع والحماية الكتيمة المطلوبة للجفاف الشديد.</p>

<h3>ما الفرق بين عبوة فازلين الشفاه 7g وعلبة الفازلين العادي الكبير؟</h3>
<p>عبوة 7g مخصصة ومصممة خصيصاً للشفاه بحجم صغير ومريح مخصص للحمل والمسح المباشر. كما أن قوام مرطب الشفاه تم ضبطه ليكون أكثر سلاسة وخفة على الشفاه مقارنة بالفازلين العادي.</p>

<h3>هل يترك الفازلين ملمساً لزجاً أو ثقيلاً على الشفاه؟</h3>
<p>تركيبة بلسم فازلين 7g مصممة لتتوزع بسلاسة على الشفاه دون أن تترك شعوراً باللزوجة المزعجة. يمنح الشفاه ملمساً مخملياً ناعماً ولمعاناً طبيعياً خفيفاً.</p>

<h3>هل يساعد فازلين الأصلي في تفتيح الشفاه الداكنة؟</h3>
<p>فازلين لا يحتوي على مواد تفتيح كيميائية، ولكنه يعالج الجفاف والتصطبغات الناتجة عن التشققات المستمرة والتسلخات. بإعادة الترطيب والحماية، يستعيد اللون الطبيعي الصحي للشفاه.</p>

<h3>هل يمكن استخدام مرطب الشفاه خلال فصل الصيف؟</h3>
<p>نعم بالتأكيد، الشفاه تتعرض للجفاف في الصيف نتيجة الحرارة وأجهزة التكييف والتعرض للماء المالح ومياه المسبح. فازلين يوفر الحماية الشاملة للشفاه في جميع الفصول.</p>

<h3>هل فازلين الشفاه الأصلي يسبب انسداد المسام حول الفم؟</h3>
<p>الفازلين النقي مكرر ثلاثياً وهو غير مسبب لانسداد المسام (Non-comedogenic). مع ذلك يُفضل تطبيقه بدقة على النسيج المخاطي للشفاه وتجنب إحاطة الجلد الخارجي الكبير بكثافة.</p>

<h3>ما هي المدة التي تدوم فيها عبوة 7 جرام من فازلين؟</h3>
<p>على الرغم من صغر حجم العبوة (7g)، إلا أنها مركزة جداً والكمية المطلوبة في كل مسحة تكون صغيرة جداً (بحجم حبة حمص). لذلك تدوم العبوة عادة من 1 إلى 2 شهر من الاستخدام اليومي المنتظم.</p>

<h3>هل الفازلين آمن إذا تم ابتلاع كمية بسيطة منه بالخطأ أثناء الأكل؟</h3>
<p>نعم، الكميات الميكروسكوبية الضئيلة التي قد تُبتلع عرضياً أثناء الكلام أو تناول الطعام آمنة كلياً وخاملة كيميائياً وتخرج من الجسم دون أن تسبب أي أذى أو امتصاص سيء.</p>

<h3>هل يحمي هذا المرطب الشفاه من أشعة الشمس؟</h3>
<p>يوفر فازلين الأصلي حماية فيزيائية رطبة من الهواء والجفاف، ولكنه لا يحتوي على فلتر شمس كيميائي (SPF). في حالات التعرض المباشر للشمس القوية لفترات طويلة يفضل استخدام واقي شمس مخصص للشفاه.</p>

<h3>ما هي الطريقة الأفضل لتطبيق فازلين الشفاه قبل النوم؟</h3>
<p>يُنصح بتنظيف الشفاه بالماء، ثم وضع طبقة أكثر سمكاً من المعتاد من فازلين الأصلي كقناع ليلي (Lip Mask). ستستيقظ في الصباح بشرة شفاه ناعمة، مرنة، وممتلئة بالرطوبة.</p>

<h3>هل يمكن استخدام فازلين 7g لأماكن أخرى جافة في الوجه؟</h3>
<p>نعم، بحكم نقاء تركيبته وحجمه المدمج، يمكن استخدامه بشكل طارئ لترطيب حول الأنف المتهيج أثناء الزكام، أو على الجلد الجاف حول الأظافر.</p>

<h3>هل يتعارض فازلين الشفاه مع منتجات تقشير الشفاه (Scrub)؟</h3>
<p>بالعكس، يفضل استخدامه فوراً بعد إجراء تقشير لطيف للشفاه لحبس الرطوبة وحماية الخلايا الجلدية الجديدة المكشوفة من الجفاف والتهيج.</p>

<h3>كيف أعرف أن فازلين الأصلي الذي بحوزتي منتج أصلي؟</h3>
<p>المنتج الأصلي يتوفر في عبوة مدمجة 7g عالية الجودة تحمل شعار Vaseline الواضح وتفاصيل الشركة المصنعة (Unilever)، ويكون قوام الجلي نقياً، شفافاً إلى أبيض ناعم وبدون رائحة عطشية.</p>

<h3>هل يناسب مرطب فازلين الرجال أيضاً أم للنساء فقط؟</h3>
<p>مرطب شفاه فازلين الأصلي مصمم للجنسين (رجال ونساء). مظهر خالي من الألوان والعطور ومظهره الطبيعي يجعله الخيار الأنسب للرجال الذين يبحثون عن ترطيب فعال دون لمعان صارخ أو رائحة زهرية.</p>

<h3>هل يمكن أن يتغير قوام المنتج في الطقس الحار؟</h3>
<p>نظراً لخصائص البترولاتوم الطبيعية، قد يلين القوام قليلاً في درجات الحرارة المرتفعة جداً. يُنصح بحفظه في درجة حرارة الغرفة (دون 25 درجة مئوية) للحفاظ على القوام متماسكاً وسلساً.</p>

<h3>ما هي الصلاحية النموذجية لمرطب شفاه فازلين الأصلي؟</h3>
<p>تصل فترة صلاحية فازلين الشفاه الأصلي عادة إلى 3 سنوات من تاريخ الإنتاج، ويفضل استخدامه خلال 12 شهراً من فتح العبوة لأول مرة لضمان أعلى مستويات النظافة والفعالية.</p>

<h3>هل يمكن استخدامه لعلاج التسلخات الزاوية في فم (Angular Cheilitis)؟</h3>
<p>يساعد الفازلين الأصلي في تخفيف الجفاف والتهيج في زوايا الفم عبر منع وصول اللعاب المتهيج، ولكن في حالات التهاب الزوايا الفطرية أو البكتيرية الشديدة يُفضل مراجعة الطبيب لوصف كريم علاج متخصص.</p>

<h3>أين يتم تصنيع فازلين Lip Therapy Original 7g؟</h3>
<p>يُصنع هذا المنتج في مصانع شركة يونيلفر (Unilever) المعتمدة عالمياً في الولايات المتحدة الأمريكية والمملكة المتحدة، وفق أعلى معايير السلامة والجودة الدوائية والتجميلية.</p>`,
    "tags": ["فازلين", "مرطب_شفاه", "ترطيب_الشفاه", "فازلين_اورجينال", "إكليل_أبها"]
  },
  "en": {
    "title": "Vaseline Lip Therapy Original for All-Day Protection and Hydration - 7g",
    "meta_title": "Vaseline Lip Therapy Original 7g All-Day Hydration | Ekleel Abha",
    "meta_description": "Buy Vaseline Lip Therapy Original 7g for all-day lip protection and deep hydration. Formulated with 100% pure triple-purified petroleum jelly. Order online from Ekleel Abha.",
    "description": `<h2>Product Overview</h2>
<p><strong>Vaseline Lip Therapy Original (7g)</strong> is the world-renowned, clinically proven therapeutic lip balm designed to lock in moisture for instantly soft, healthy-looking lips. Crafted with 100% pure, triple-purified Vaseline Petroleum Jelly, this concentrated formula acts as a resilient shield against environmental stress, dry winds, cold weather, and indoor air conditioning. Its compact 7g mini-jar packaging makes it an indispensable daily companion that easily fits into any pocket, purse, or travel kit.</p>
<p>Unlike superficial cosmetic lip products that provide temporary surface sheen, Vaseline Lip Therapy Original works at a cellular physical level by physically sealing in the skin's natural moisture. It accelerates the lip's natural recovery process from severe dryness, flaking, and painful cracking. Unscented, non-greasy, and hypoallergenic, it provides a natural glossy shine while being gentle enough for even the most sensitive lips.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Deep Moisture Locking:</strong> Formulated with 100% triple-purified Petroleum Jelly to lock in essential skin moisture and prevent dehydration all day long.</li>
  <li><strong>Heals & Soothes Chapped Lips:</strong> Clinically proven to soothe and rapidly accelerate the healing of dry, cracked, and irritated lip tissue.</li>
  <li><strong>Environmental Shield:</strong> Creates an invisible, non-sticky protective barrier that defends lips against harsh windburn, dry heat, and cold weather.</li>
  <li><strong>Natural Glossy Finish:</strong> Delivers a soft, supple texture with a healthy, subtle shine without any uncomfortable sticky or tacky residue.</li>
  <li><strong>Fragrance-Free & Hypoallergenic:</strong> Completely free from synthetic fragrances, flavors, dyes, and irritating additives, making it exceptionally safe for sensitive skin.</li>
  <li><strong>Convenient Compact Packaging:</strong> The portable 7g mini jar ensures easy application anytime and anywhere, perfect for daily commuting and travel.</li>
  <li><strong>Enhances Lip Elasticity:</strong> Deeply conditions lip skin to prevent fine dry lines and maintain long-term softness.</li>
</ul>

<h2>How to Use</h2>
<ul>
  <li><strong>Step 1:</strong> Gently clean and pat dry your lips, removing any leftover food particles or prior lip cosmetics.</li>
  <li><strong>Step 2:</strong> Dip a clean fingertip or lip applicator into the jar to scoop out a small pea-sized amount of Vaseline Lip Therapy Original.</li>
  <li><strong>Step 3:</strong> Smooth evenly over your upper and lower lips, massaging in gentle circular motions to allow the balm to penetrate micro-cracks.</li>
  <li><strong>Step 4:</strong> Reapply as needed throughout the day, especially before stepping into cold air, dry air-conditioned rooms, or right before bedtime for an overnight lip recovery mask.</li>
</ul>

<h2>Ingredients Overview</h2>
<p>Vaseline Lip Therapy Original relies on proven dermatological occlusive science and skin barrier nourishment:</p>
<ul>
  <li><strong>100% Pure Triple-Purified Petrolatum:</strong> The gold standard occlusive agent recommended by dermatologists worldwide. It reduces Transepidermal Water Loss (TEWL) by over 98%, creating an optimal hydrated environment for tissue healing.</li>
  <li><strong>Refined Mineral Oil:</strong> Works synergistically to smooth rough skin surfaces and impart immediate flexibility to dry, stiff skin layers.</li>
  <li><strong>Vitamin E (Tocopheryl Acetate):</strong> A powerful antioxidant that protects delicate lip cells against free radical damage caused by environmental pollution and UV exposure.</li>
  <li><strong>Natural Shea Butter (Butyrospermum Parkii):</strong> Rich in essential fatty acids and nutrients that nourish the skin lipid barrier, enhancing long-lasting lip softness.</li>
</ul>

<h2>Warnings and Precautions</h2>
<ul>
  <li>For external topical application on the lips only. Avoid swallowing large quantities.</li>
  <li>Keep out of reach of young children to prevent accidental ingestion or unsupervised usage.</li>
  <li>Store in a cool, dry place away from direct sunlight and extreme heat to maintain proper jelly consistency.</li>
  <li>If unusual irritation, redness, or allergic discomfort occurs, discontinue use and rinse with tepid water.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li><strong>Individuals with Dry & Chapped Lips:</strong> Anyone suffering from chronic lip dryness, peeling, tightness, or painful winter cracks.</li>
  <li><strong>Sensitive Skin Users:</strong> People who require a clean, fragrance-free, dye-free lip moisturizer that won't trigger contact dermatitis.</li>
  <li><strong>People Exposed to Extreme Environments:</strong> Those frequently in air-conditioned offices, cold climates, dry weather, or outdoor windy environments.</li>
  <li><strong>Patients on Acne Treatments (Isotretinoin / Roaccutane):</strong> Individuals experiencing severe systemic dry lip side effects looking for intense, dermatologist-approved relief.</li>
</ul>`,
    "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Vaseline</td></tr>
  <tr><th>Category</th><td>Skin Care / Lip Care</td></tr>
  <tr><th>Product Type</th><td>Therapeutic Lip Balm & Moisturizer</td></tr>
  <tr><th>Volume/Weight</th><td>7g (Compact Mini Jar)</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Specifically Dry & Chapped Lips)</td></tr>
  <tr><th>Finish</th><td>Natural Glossy & Non-Sticky</td></tr>
  <tr><th>Texture</th><td>Smooth & Soft Jelly Balm</td></tr>
  <tr><th>Fragrance</th><td>Unscented / Fragrance-Free</td></tr>
  <tr><th>Active Ingredients</th><td>100% Triple-Purified Petrolatum, Shea Butter, Vitamin E</td></tr>
  <tr><th>Country of Origin</th><td>USA / UK</td></tr>
  <tr><th>Manufacturer</th><td>Unilever</td></tr>
  <tr><th>Age Group</th><td>All Ages (Adults & Children)</td></tr>
</tbody>
</table>`,
    "knowledge_base": `<h2>Clinical & Educational Insights on Lip Barrier Protection</h2>

<h3>What problem does this solve?</h3>
<p>Vaseline Lip Therapy Original solves the problem of chronic lip dryness, flaking, chapping, and painful mucosal cracking. Lip skin is structurally unique compared to the rest of facial skin; it is extremely thin (only 3 to 5 cell layers deep) and lacks sebaceous (oil) glands and sweat glands. Consequently, the lips are incapable of producing their own protective lipid mantle. When exposed to dry air or cold environments, moisture evaporates rapidly, leading to painful splits, bleeding, and discomfort during speaking or eating. Vaseline instantly reconstructs an artificial moisture barrier to protect and repair this vulnerable tissue.</p>

<h3>Why does this condition happen?</h3>
<p>Lip dryness occurs due to a combination of environmental factors and physiological vulnerability. The absence of a natural lipid layer makes lips susceptible to rapid Transepidermal Water Loss (TEWL). Environmental triggers like dry winter air, continuous indoor air conditioning, solar radiation, and wind pull water out of the lip's outer stratum corneum. Furthermore, the common habit of frequently licking the lips worsens dryness dramatically. Saliva contains digestive enzymes like amylase and proteases that break down delicate skin cells. As saliva evaporates, it strips away the lip's intrinsic moisture, leaving lips significantly drier and more inflamed than before.</p>

<h3>Prevention Tips</h3>
<ul>
  <li><strong>Maintain Adequate Hydration:</strong> Drink at least 2-3 liters of water daily to maintain system-wide hydration, which directly supports lip softness.</li>
  <li><strong>Avoid Licking Your Lips:</strong> Refrain from licking dry lips for temporary moisture; replace this habit immediately with a sweep of Vaseline Lip Therapy.</li>
  <li><strong>Apply Overnight Treatment:</strong> Smooth a thick coat of Vaseline Original onto lips before sleeping to counteract moisture loss caused by mouth breathing during sleep.</li>
  <li><strong>Never Pick or Peel Dry Flakes:</strong> Avoid pulling off dry skin flakes with fingers or teeth, as this causes bleeding, scarring, and potential bacterial infection.</li>
  <li><strong>Shield Lips in Harsh Weather:</strong> Always apply an occlusive layer before entering cold, windy, or heavily air-conditioned environments.</li>
</ul>

<h3>Common Myths</h3>
<ul>
  <li><strong>Myth:</strong> Licking your lips provides quick, natural hydration.<br><strong>Fact:</strong> Saliva contains digestive enzymes that irritate and dry out the lips as the liquid evaporates, severely exacerbating chapping and inflammation.</li>
  <li><strong>Myth:</strong> Vaseline is addictive and makes your lips unable to hydrate themselves.<br><strong>Fact:</strong> Petrolatum is chemically inert and non-addictive; it does not alter physiological skin mechanics but physically seals moisture to allow natural healing.</li>
  <li><strong>Myth:</strong> Heavily scented or flavored lip balms are more effective than plain Vaseline.<br><strong>Fact:</strong> Artificial fragrances, flavorings, and cooling agents like menthol often cause contact dermatitis and stinging on cracked skin, whereas unscented Vaseline Original is the safest therapeutic option.</li>
  <li><strong>Myth:</strong> Lips only get dry during the winter season.<br><strong>Fact:</strong> Summer heat, intense sun exposure, air conditioning, and swimming pool chlorine dry out lip tissues just as severely as winter cold.</li>
</ul>

<h3>Scientific Explanation</h3>
<p>The therapeutic mechanism of 100% triple-purified Petrolatum is rooted in occlusive dermatological physics. Petrolatum molecules form a hydrophobic, continuous hydrocarbon matrix across the stratum corneum of the lips. This dense matrix reduces Transepidermal Water Loss (TEWL) by over 98%—the highest efficacy rating among all known cosmetic occlusives (compared to plant oils which achieve 20-30%). By trapping water inside the delicate epidermal layers, it maintains an optimal humid microenvironment. This hydration allows endogenous proteolytic enzymes to naturally desquamate dead corneocytes smoothly, accelerating tissue re-epithelialization without triggering an inflammatory response.</p>`,
    "faqs": `<h3>What is Vaseline Lip Therapy Original 7g?</h3>
<p>Vaseline Lip Therapy Original 7g is a concentrated lip balm specially formulated to hydrate, protect, and heal dry, chapped lips. It uses 100% pure, triple-purified Petroleum Jelly to lock in moisture and deliver long-lasting relief with a natural shine.</p>

<h3>What are the primary active ingredients in Vaseline Lip Therapy Original?</h3>
<p>The core ingredient is 100% pure triple-purified Petrolatum, enriched with mineral oil, natural Shea Butter, and Vitamin E. This clean, unscented formulation provides intense nourishment and physical barrier protection.</p>

<h3>Does Vaseline Lip Therapy Original contain any added fragrance or flavor?</h3>
<p>No, the Original variant is completely unscented, unflavored, and dye-free. This makes it ideal for individuals with sensitive skin, allergies, or skin conditions like eczema and lip dermatitis.</p>

<h3>How does Vaseline Lip Therapy hydrate dry lips?</h3>
<p>It acts as a physical occlusive barrier on top of lip tissue, trapping the skin's natural moisture inside while blocking external dry air, cold wind, and environmental pollutants from pulling water out.</p>

<h3>How often can I apply Vaseline Lip Therapy during the day?</h3>
<p>You can reapply Vaseline Lip Therapy as often as needed throughout the day. It is especially beneficial to apply in the morning, after meals, before outdoor exposure, and right before going to sleep.</p>

<h3>Can I wear Vaseline Lip Therapy under lipstick or lip gloss?</h3>
<p>Yes, applying a thin layer of Vaseline Lip Therapy a few minutes before lipstick application smoothes out dry flakes and fine lines, allowing your lipstick to glide on smoothly without clumping.</p>

<h3>Is Vaseline Lip Therapy Original safe for children and toddlers?</h3>
<p>Yes, because of its pure, hypoallergenic, and chemical-free formulation, Vaseline Original is completely safe for children and toddlers suffering from chapped lips due to cold weather or drooling.</p>

<h3>Does this product help with lip dryness caused by Isotretinoin (Accutane)?</h3>
<p>Yes, dermatologists frequently recommend Vaseline Lip Therapy to patients undergoing oral isotretinoin treatment, as it provides the intense, continuous occlusive moisture needed for severe medication-induced cheilitis.</p>

<h3>What is the difference between the 7g mini jar and standard Vaseline jelly?</h3>
<p>The 7g mini jar is specifically formulated and packaged for lip application, featuring a smoother, non-sticky texture tailored for comfortable, non-greasy wear on sensitive lip skin.</p>

<h3>Does Vaseline Lip Therapy feel sticky or heavy on the lips?</h3>
<p>No, the 7g formulation is optimized to glide on smoothly, leaving a soft, velvety feel and a subtle natural gloss without any heavy or uncomfortable stickiness.</p>

<h3>Can Vaseline Lip Therapy lighten dark or discolored lips?</h3>
<p>While Vaseline does not contain chemical bleaching agents, it heals chronic inflammation, flaking, and dryness that cause post-inflammatory hyperpigmentation, helping lips regain their natural healthy tone over time.</p>

<h3>Is Vaseline Lip Therapy effective during hot summer months?</h3>
<p>Absolutely. Lips lose moisture rapidly in summer due to scorching heat, air conditioning, and exposure to pool chlorine or saltwater. Vaseline provides year-round moisture defense.</p>

<h3>Will Vaseline Lip Therapy clog pores around the mouth?</h3>
<p>Pure petroleum jelly is non-comedogenic (it does not clog pores). However, it is best applied directly onto the vermilion border of the lips rather than spreading heavily onto surrounding facial skin.</p>

<h3>How long does a single 7g jar of Vaseline Lip Therapy last?</h3>
<p>Despite its compact 7g size, a little goes a very long way. Because each application requires only a tiny pea-sized dab, one mini jar typically lasts between 1 to 2 months of regular daily use.</p>

<h3>What happens if I accidentally swallow a small amount of Vaseline Lip Therapy?</h3>
<p>Small microscopic amounts swallowed incidentally while talking or eating are non-toxic, chemically inert, and pass through the digestive tract safely without causing harm.</p>

<h3>Does Vaseline Lip Therapy provide sun protection (SPF)?</h3>
<p>The Original 7g variant provides physical moisture protection but does not contain chemical UV filters (SPF). For prolonged direct sunlight, using a dedicated SPF lip product during the day is recommended.</p>

<h3>What is the best way to use Vaseline Lip Therapy as an overnight lip mask?</h3>
<p>Gently clean your lips before bed and apply a slightly thicker layer than usual. Over night, it locks in water, allowing you to wake up to deeply hydrated, smooth, and plump lips.</p>

<h3>Can I use Vaseline Lip Therapy on other dry skin spots?</h3>
<p>Yes, due to its high purity and compact size, it works wonderfully in emergency situations for dry cuticles, irritated skin around the nose during a cold, or small dry elbow patches.</p>

<h3>Can I use Vaseline Lip Therapy after using a lip scrub?</h3>
<p>Yes, applying Vaseline immediately after a gentle lip scrub is highly recommended to seal in moisture and protect newly exposed, tender skin cells from drying out.</p>

<h3>How can I verify that my Vaseline Lip Therapy 7g is authentic?</h3>
<p>Authentic Vaseline products come in high-quality 7g jars featuring clear Vaseline branding and Unilever manufacturer markings, with a pure, smooth, translucent to white unscented jelly consistency.</p>

<h3>Is Vaseline Lip Therapy Original suitable for men?</h3>
<p>Yes, Vaseline Lip Therapy Original is completely gender-neutral. Its unscented, unflavored, and clear formula makes it a favorite for men looking for effective lip hydration without shine or perfume.</p>

<h3>Does temperature affect the texture of Vaseline Lip Therapy?</h3>
<p>Yes, petroleum jelly naturally softens slightly in high heat. Storing the mini jar at room temperature (below 25°C) keeps the texture firm, smooth, and easy to apply.</p>

<h3>What is the shelf life of Vaseline Lip Therapy Original?</h3>
<p>The product typically has a shelf life of 3 years from the date of manufacture. For best hygienic practices, it is recommended to use within 12 months after opening.</p>

<h3>Does Vaseline help with Angular Cheilitis (cracks at the corners of the mouth)?</h3>
<p>Vaseline protects the corners of the mouth from saliva irritation and severe drying. However, if angular cheilitis is caused by a fungal or bacterial infection, consult a doctor for target antimicrobial treatment.</p>

<h3>Where is Vaseline Lip Therapy Original 7g manufactured?</h3>
<p>Vaseline Lip Therapy Original is manufactured by Unilever in certified facilities in the USA and UK, strictly adhering to global pharmaceutical and cosmetic quality standards.</p>`,
    "tags": ["vaseline", "lip_therapy", "lip_balm", "petroleum_jelly", "ekleel_abha"]
  }
};

const outputDir = path.join(__dirname, 'generated_products');
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

const targetPath = path.join(outputDir, '1473.json');
fs.writeFileSync(targetPath, JSON.stringify(productData, null, 2), 'utf8');

console.log(`✅ Successfully generated 1473.json at ${targetPath}`);
