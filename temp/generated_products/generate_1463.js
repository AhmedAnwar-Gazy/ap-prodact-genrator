const fs = require('fs');
const path = require('path');

const productData = {
  "product_id": "1463",
  "sku": "EK-1463",
  "category": "العناية بالجسم / إزالة الشعر",
  "brand": "Nair",
  "ar": {
    "title": "بخاخ مزيل شعر من نير بخلاصة الكيوي 200مل لإزالة سريعة وبشرة ناعمة",
    "meta_title": "بخاخ مزيل شعر من نير بخلاصة الكيوي 200مل | صيدلية إكليل أبها",
    "meta_description": "تسوق بخاخ مزيل شعر من نير بخلاصة الكيوي 200مل لإزالة سريعة وسهلة وبشرة ناعمة بدون ألم. إزالة سريعة للشعر وترطيب يدوم طويلاً من صيدلية إكليل أبها السعودية.",
    "description": `<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>بخاخ مزيل الشعر من نير بخلاصة الكيوي بحجم 200 مل (Nair Hair Removal Spray with Kiwi Extract)</strong> الابتكار الفعال والعصري الذي يمنحك تجربة إزالة شعر للجسم سريعة، مريحة، وخالية تماماً من الألم. تم تطوير هذا البخاخ المبتكر ليوفر سهولة فائقة في الاستخدام والتغطية المتساوية دون الحاجة لملامسة الكريم باليدين أو فركه على الجلد، مما يجعله الخيار الأول لتغطية المساحات الكبيرة في الجسم مثل الساقين والذراعين وكذلك الأماكن التي يصعب الوصول إليها. تجمع تركيبته المتقدمة بين القوة الكيميائية اللطيفة لإذابة الشعر تحت سطح الجلد مباشرة وبين التغذية المكثفة والترطيب الفائق المستمد من خلاصة فاكهة الكيوي الطبيعية الغنية بالفيتامينات ومضادات الأكسدة.</p>
<p>يمتاز بخاخ نير برغوة خفيفة ورقيقة تنتشر بسرعة وتعمل في غضون 3 إلى 10 دقائق فقط لتفكيك كيراتين الشعر وتليينه تماماً، مما يتيح إزالته بمسحة واحدة باستخدام ملعقة التطبيق المرفقة أو المنشفة الرطبة. بفضل تضمين خلاصة الكيوي المغذية والزيوت المرطبة، يحافظ البخاخ على توازن رطوبة الجلد ويمنع التهيج والجفاف، لتستمتعي ببشرة ملساء حريرية، مشعة بالنضارة، ومضمخة برائحة الكيوي والفواكه المنعشة التي تدوم طويلاً بعد كل استخدام.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تغطية سريعة وسهلة بدون ملامسة اليدين:</strong> تصميم البخاخ الرغوي يتيح لك رش المنتج وتغطيته للأجزاء الواسعة من الجسم مثل الساقين والذراعين في ثوانٍ معدودة ودون الحاجة لفرد الكريم بأصابعك.</li>
  <li><strong>إزالة سريعة بدون ألم:</strong> يذيب الشعر القصير والعنيد بالقرب من الجذور في غضون 3 إلى 10 دقائق فقط دون أي ألم أو شعور بالانزعاج.</li>
  <li><strong>غني بخلاصة الكيوي الطبيعية:</strong> يزود البشرة بمضادات الأكسدة وفيتامين C التي تعزز نضارة الجلد وتمنع الأكسدة وتساعد في توحيد المظهر العام للبشرة.</li>
  <li><strong>نمو أنعم للشعر بدون شعر تحت الجلد:</strong> يذيب أطراف الشعر ويجعلها مستديرة ونظيفة، مما يلغي تماماً مشكلة نهايات الشعر الحادة، الحكة، وظاهرة جلد الدجاجة (Keratosis Pilaris).</li>
  <li><strong>حماية كاملة من الجروح والندوب:</strong> بديل آمن 100% لشفرات الحلاقة، حيث يقضي على خطورة الاصابة بالجروح، الخدوش السطحية، أو التهيج الناتج عن الاحتكاك الميكانيكي.</li>
  <li><strong>ترطيب عميق ونعومة تدوم أياماً:</strong> تحتوي التركيبة على زيوت مرطبة تمنع فقدان الماء من الطبقة القرنية، لتبقى البشرة ناعمة ومشرقة لعدة أيام أطول من الحلاقة بالموس.</li>
  <li><strong>رائحة الكيوي الزكية والمنعشة:</strong> يتضمن تقنية تقليل الروائح الكيميائية وإحلال عطر فاكهي منعش يترك شعوراً بالانتعاش والنظافة المطلقة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التجهيز والرج):</strong> تأكدي من أن بشرتك جافة ونظيفة تماماً. رجي عبوة البخاخ جيداً لعدة ثوانٍ قبل الاستخدام لضمان امتزاج المكونات وتكون رغوة متجانسة.</li>
  <li><strong>الخطوة الثانية (الرش والتغطية):</strong> امسكي العبوة على مسافة 5 إلى 10 سم من المنطقة المراد إزالة الشعر منها، ورشي رغوة البخاخ بالتساوي ليغطي الشعر بالكامل. لا داعي لدلك الرغوة أو مسحها باليدين.</li>
  <li><strong>الخطوة الثالثة (الانتظار وااختبار المنطقة):</strong> اتركي الرغوة على الجلد لمدة 3 إلى 5 دقائق. قومي باختبار منطقة صغيرة جداً باستخدام الملعقة المرفقة أو قطعة قماش رطبة؛ إذا كان الشعر يزول بسهولة، قمي بإزالة باقي الرغوة.</li>
  <li><strong>الخطوة الرابعة (الحد الأقصى للوقت):</strong> إذا كان الشعر سميكاً، يمكنك ترك الرغوة لدقائق إضافية، ولكن <strong>يُحظر تماماً ترك البخاخ على البشرة لمدة تتجاوز 10 دقائق إجمالاً</strong> لتجنب التهيج.</li>
  <li><strong>الخطوة الخامسة (الإزالة والشطف):</strong> امسحي الرغوة والشعر المذاب بلطف باستخدام ملعقة التطبيق أو منشفة دافئة رطبة عكس اتجاه نمو الشعر، ثم اشطفي البشرة جيداً بالماء الفاتر دون استخدام الصابون، وجففيها بلطف.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<p>تم تركيب بخاخ نير بمزيج متناغم من المواد الكيميائية لإذابة الشعر والمكونات النباتية المرطبة لحماية البشرة والعناية بها:</p>
<ul>
  <li><strong>ثيوغليكولات البوتاسيوم (Potassium Thioglycolate):</strong> المادة الفعالة الأساسية المسؤولة عن الاختزال الكيميائي لروابط الديسولفيد (Disulfide bonds) في بروتين الكيراتين المكون للشعر، مما يؤدي إلى تليين بناء الشعرة واختفائها.</li>
  <li><strong>هيدروكسيد الكالسيوم (Calcium Hydroxide):</strong> مركب قلوي يعمل على رفع الرقم الهيدروجيني (pH) لتوفير بيئة قلوية ملائمة تساعد المادة الفعالة على تفتيح مسام كيراتين الشعر واختراقه بسرعة وسلاسة.</li>
  <li><strong>مستخلص فاكهة الكيوي (Actinidia Chinensis / Kiwi Fruit Extract):</strong> مستخلص طبيعي فائق الغنى بفيتامين C، والأحماض الفعالة، ومضادات الأكسدة التي تهدئ البشرة أثناء العملية الكيميائية، وتدعم تجدد الخلايا وتمنح الجلد إشراقة ونعومة حريرية.</li>
  <li><strong>الزيت المعدني والجلسرين (Mineral Oil & Glycerin):</strong> مرطبات ومطريات تعمل على تشكيل غشاء واقٍ على سطح الجلد يمنع تبخر الرطوبة، ويقلل الجفاف، ويضمن ليونة البشرة ومرونتها بعد الإزالة.</li>
  <li><strong>ستيريل الكحول ومطريات القوام (Cetearyl Alcohol & Emulsifiers):</strong> تمنح الرغوة قوامها المتماسك الخفيف الذي يتشبث بالشعر دون أن يسيل، مما يضمن ثبات المنتج أثناء فترة الانتظار.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li><strong>ضرورة إجراء اختبار الحساسية (Patch Test):</strong> يجب دائماً رش كمية صغيرة على مساحة صغيرة من الجلد قبل 24 ساعة من الاستخدام الكامل، لمراقبة التفاعلات والتأكد من عدم وجود حساسية.</li>
  <li><strong>المناطق الحظورة:</strong> البخاخ مخصص لشعر الجسم فقط؛ يُمنع تماماً رش المنتج على الوجه، العينين، الأنف، الأذنين، الحلمات، أو المناطق التناسلية والشرجية.</li>
  <li><strong>البشرة المتضررة:</strong> يُمنع استخدام البخاخ على البشرة المتهيجة، المجروحة، المحترقة من أشعة الشمس، أو البشرة التي تعاني من إكزيما أو حب الشباب المفتوح.</li>
  <li><strong>الالتزام بالوقت وسالمة التخزين:</strong> لا تتجاوزي مدة 10 دقائق كحد أقصى على الجلد. العبوة مضغوطة تحت الضغط؛ تُحفظ بعيداً عن الحرارة، النار، أشعة الشمس المباشرة، ومتناول الأطفال.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<p>تم تصميم <strong>بخاخ نير لإزالة الشعر بخلاصة الكيوي</strong> لجميع النساء والرجال الراغبين في وسيلة سريعة، حديثة، وبدون ألم لإزالة شعر الجسم بكفاءة. وهو مثالي للأفراد الذين يبحثون عن تغطية واسعة للساقين والذراعين والمناطق الصعبة دون تلطيخ اليدين، والذين يفضلون الحصول على بشرة ملساء ومعطرة برائحة فاكهية مع حماية ممتازة ضد الجفاف والشعر تحت الجلد.</p>`,
    "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>Nair (نير)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / إزالة الشعر</td></tr>
  <tr><th>نوع المنتج</th><td>بخاخ رغوي لإزالة الشعر (Depilatory Spray)</td></tr>
  <tr><th>الحجم/الوزن</th><td>200 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (بما فيها البشرة العادية والجافة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة فائقة النعومة ومشرقة بدون شعر</td></tr>
  <tr><th>الملمس</th><td>رغوة بخاخ خفيفة ورقيقة</td></tr>
  <tr><th>العطر</th><td>عطر الكيوي المنعش للفواكه</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة الكيوي (Kiwi Extract)، ثيوغليكولات البوتاسيوم (Potassium Thioglycolate)، هيدروكسيد الكالسيوم (Calcium Hydroxide)</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة المتحدة / الولايات المتحدة الأمريكية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Church & Dwight Co., Inc.</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (فوق 16 سنة)</td></tr>
</tbody>
</table>`,
    "knowledge_base": `<h2>الدليل المعرفي الطبي لإزالة الشعر بالبخاخ الكيميائي والعناية بالبشرة</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج بخاخ نير بالكيوي مشكلة نمو الشعر غير المرغوب فيه في المناطق المختلفة للجسم بكفاءة وسرعة فائقتين. كما يحل بشكل جذري المتاعب والمشكلات الصحية المرتبطة بالطرق التقليدية كالشفرات، مثل الجروح القطعية، تهيج البشرة، الشعور بالحرقة، التفتق الجلدي، وظاهرة نمو الشعر داخل الجلد (Ingrown Hairs) المسؤولة عن ظهور الحبوب المسدودة وشكل جلد الدجاجة على الساقين والذراعين.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تنشأ مشكلة الشعر غير المرغوب فيه نتيجة النشاط المستمر لبصيلات الشعر في طبقة الأدمة، حيث تقوم بتخليق بروتين الكيراتين المترابط بروابط كيميائية قوية ثنائية الكبريتيد. عند التخلص من الشعر بواسطة شفرات الحلاقة، يتم قطع ساق الشعرة بزاوية حادة مباشرة عند سطح الجلد. هذا المقطع العرضي الحاد يؤدي إلى بروز الشعر الجديد بعد وقت قصير بملمس خشن وقمم حادة تنغرس بسهولة في أنسجة الجلد المحيطة أثناء نموها، مسببة التهاب البصيلات (Folliculitis). بالإضافة إلى ذلك، فإن الحلاقة الميكانيكية تزيل الدهون الطبيعية المرطبة للبشرة، مما يحفز الجفاف واحمرار. البخاخ الكيميائي يحل ذلك بعمق من خلال تذويب مادة الشعرة داخل فتحة البصيلة السطحية، مما يترك نهاية الشعر مستديرة ولطيفة على الأنسجة.</p>

<h3>نصائح وقائية</h3>
<p>1. <strong>إجراء اختبار الحساسية مسبقاً:</strong> قومي دائماً باختبار البخاخ على مساحة صغيرة من الساق والانتظار 24 ساعة للتحقق من سلامة الاستجابة الجلدية.<br>2. <strong>التقشير الأسبوعي اللطيف:</strong> قمي بتقشير الجلد بانتظام مرة أو مرتين أسبوعياً بمقشر خفيف لإزالة خلايا الجلد الميتة وتسهيل خروج الشعر بشكل سلس.<br>3. <strong>الترطيب اليومي المكثف:</strong> استخدمي مرطباً يومياً غنياً لتعزيز حاجز الرطوبة الطبيعي للبشرة والحفاظ على مرونة الجلد بعد كل عملية إزالة.<br>4. <strong>تجنب التعرض المباشر للشمس فوراً:</strong> امتنعي عن التسمير أو التعرض لأشعة الشمس القوية والماء المكلور لمدة 24 ساعة بعد الرش لحماية المسام المفتوحة حديثاً.<br>5. <strong>الالتزام التام بالوقت المحدد:</strong> لا تتركي البخاخ على الجلد مطلقاً لأكثر من 10 دقائق لضمان عدم حدوث أي حروق كيميائية سطحيّة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "بخاخات إزالة الشعر تسبب زيادة سمك الشعر المرتد وغمق لونه."<br><strong>الحقيقة:</strong> هذا الاعتقاد خاطئ تماماً من الناحية الفسيولوجية. البخاخ يعمل على الجزء الخارجي من ساق الشعرة ولا يصل إلى البصيلات العميقة أو الجينات المسؤولة عن نمو الشعر وسمكه أو تصبغه. ينبت الشعر الجديد بنهايات ملساء ومستديرة، مما يمنح شعوراً بالنعومة وتأخراً في الصلابة مقارنة بالحلاقة بالشفرة.</p>

<h3>التفسير العلمي</h3>
<p>يعتمد المبدأ العلمي لإزالة الشعر بواسطة بخاخ نير على عملية التحلل الكيراتيني (Keratolysis). يتألف الكيراتين في شعر الإنسان من سلاسل ببتيدية بروتينية مرتبطة ببعضها بواسطة <strong>روابط ثنائية الكبريتيد (Disulfide Bonds - S-S)</strong> القوية المشتقة من حمض السيستين الأميني. يعمل مركب <strong>ثيوغليكولات البوتاسيوم (Potassium Thioglycolate)</strong> كمادة اختزال تقوم بمنح جزيئات الهيدروجين لتفكيك هذه الروابط وتحويلها إلى مجموعات سلفهيدريل (-SH). بالتوازي، يوفر <strong>هيدروكسيد الكالسيوم (Calcium Hydroxide)</strong> الوسط القلوي المناسب (pH مرتفع) الذي يساعد على انتفاخ الشعرة وسرعة اختراق المادة الفعالة لأنسجة الكيراتين. خلال 3 إلى 10 دقائق، تنحل البنية الهيكلية للشعرة وتتحول إلى كتلة هلامية طرية يمكن مسحها بسهولة دون المساس بالأنسجة السليمة للجلد.</p>`,
    "faqs": `<h3>ما هو بخاخ نير مزيل الشعر بخلاصة الكيوي وكيف يعمل؟</h3>
<p>بخاخ نير بخلاصة الكيوي 200مل هو مستحضر تجميلي ذكي ورغوي مخصص لإزالة شعر الجسم بدون ألم. يعمل عن طريق إطلاق رغوة خفيفة تغطي الشعر وتتغلغل الكيميائيات اللطيفة فيها لإذابة كيراتين الشعر بالقرب من الجذور خلال 3 إلى 10 دقائق، ليترك البشرة ملساء، ورطبة، ومعطرة برائحة الكيوي.</p>
<h3>ما الميزة الرئيسية لبخاخ إزالة الشعر مقارنة بكريمات إزالة الشعر التقليدية؟</h3>
<p>الميزة الأساسية هي السهولة والسرعة في التطبيق وتغطية المساحات الكبيرة كالساقين والذراعين دون الحاجة لملامسة الكريم باليدين أو فركه، بالإضافة إلى الوصول للأماكن الصعبة بفضل البخاخ المتساوي الذي يوزع الرغوة بكفاءة عالية.</p>
<h3>ما هي المكونات الفعالة الرئيسية في بخاخ نير بالكيوي؟</h3>
<p>يحتوي على ثيوغليكولات البوتاسيوم كمادة فعالة لإذابة كيراتين الشعر، وهيدروكسيد الكالسيوم لتأمين البيئة القلوية المناسبة، وخلاصة فاكهة الكيوي الطبيعية الغنية بمضادات الأكسدة وفيتامين C لحماية البشرة وترطيبها.</p>
<h3>كيف تدعم خلاصة الكيوي ترطيب ونضارة البشرة أثناء إزالة الشعر؟</h3>
<p>خلاصة الكيوي مادة غنية بالفيتامينات والمعادن والإنزيمات الطبيعية التي تلطف الجلد، وتقلل التهيج الكيميائي، وتساعد في تغذية الطبقات السطحية للبشرة وتنشيط نضارتها أثناء عملية إزالة الشعر.</p>
<h3>كم من الوقت يجب ترك بخاخ نير على البشرة قبل إزالته؟</h3>
<p>يُترك البخاخ عادة لمدة 3 إلى 5 دقائق كافية للشعر العادي. وفي حال كان الشعر سميكاً، يمكن تركه لفترة أطول قليلاً، ولكن يُمنع منعاً باتاً ترك البخاخ لأكثر من 10 دقائق إجمالاً على البشرة.</p>
<h3>هل يمكن استخدام بخاخ نير بالكيوي على البشرة الحساسة؟</h3>
<p>يمكن استخدامه لمعظم أنواع البشرة، ولكن إذا كانت بشرتك شديدة الحساسية أو سريعة التهيج، نوصي دائماً بإجراء اختبار الحساسية على مساحة صغيرة أولاً، أو اختيار الإصدارات المخصصة للبشرة الحساسة من نير.</p>
<h3>ما هي المناطق الجسدية المسموح باستخدام بخاخ نير عليها؟</h3>
<p>البخاخ مخصص ومناسب جداً للاستخدام على الساقين، الذراعين، منطقة تحت الإبطين، وخط البكيني. ويضمن الحصول على نتائج ملساء وموحدة في هذه المناطق.</p>
<h3>هل يصح استخدام بخاخ نير على بشرة الوجه أو المناطق التناسلية؟</h3>
<p>لا، يُحظر تماماً رش البخاخ على بشرة الوجه، الحواجب، الأنف، الأذنين، الحلمات، أو المناطق التناسلية والشرجية الداخلية، نظراً لرقة وحساسية الأنسجة في تلك المناطق.</p>
<h3>كيف أضمن عدم حدوث تهيج أو حساسية من البخاخ؟</h3>
<p>تضمن ذلك من خلال إجراء اختبار الحساسية الموصى به برش كمية صغيرة على جزء صغير من الساق والانتظار 24 ساعة. إذا لم يظهر احمرار أو حكة، يمكنك استخدام البخاخ بأمان كامل.</p>
<h3>ما هي طريقة الاستخدام الصحيحة والخطوات الموصى بها؟</h3>
<p>رجي العبوة جيداً، رشي الرغوة على بعد 5-10 سم لتغطية الشعر دون دلك، انتظري من 3 إلى 5 دقائق، اختبري منطقة صغيرة بالملعقة، ثم امسحي الرغوة والشعر المذاب بقطعة قماش رطبة واشطفي بالماء الفاتر.</p>
<h3>هل يجب رش البخاخ بالقرب من الجلد ودلكه باليدين؟</h3>
<p>لا يجب دلك البخاخ باليدين إطلاقاً. رشي العبوة على مسافة مناسبة (5-10 سم) لضمان انتشار طبقة رغوية متساوية تغطي الشعر بالكامل وتترك لتقوم بعملها دون حاجة للفرك.</p>
<h3>كيف يمنع بخاخ نير ظهور الشعر تحت الجلد (جلد الدجاجة)؟</h3>
<p>من خلال تذويب ساق الشعرة كيميائياً وتنعيم حوافها لتصبح مستديرة بدلاً من قصها بزاوية حادة كما تفعل الشفرات. هذا يمنع انغراس طرف الشعرة الحاد في الجلد عند نموها مجدداً.</p>
<h3>هل يسبب بخاخ نير اسمرار البشرة أو تصبغها؟</h3>
<p>لا يسبب البخاخ أي اسمرار إذا تم التزام بالتعليمات وعدم تجاوز مدة 10 دقائق على الجلد. التصبغات تحدث فقط نتيجة الحروق الكيميائية عند الإفراط الشديد في زمن ترك المنتج.</p>
<h3>هل ينمو الشعر بشكل أسمك أو أقسى بعد استخدام بخاخ نير؟</h3>
<p>لا، المنتجات الكيميائية الموضعية لا تؤثر إطلاقاً على جذور الشعر أو طبيعة نموه الجينية والهرمونية. الشعر المرتد ينمو بأطراف دائرية ناعمة توحي بقلة القسوة والسمك.</p>
<h3>ما هي الاحتياطات الواجب اتخاذها قبل وبعد استخدام البخاخ؟</h3>
<p>قبل الاستخدام: تأكدي من جفاف ونظافة البشرة وعدم وجود جروح. بعد الاستخدام: تجنبي مضادات التعرق والعطور والصابون المعقد والتعرض للشمس أو السباحة لمدة 24 ساعة.</p>
<h3>هل يمكن الاستحمام بماء ساخن أو استخدام الصابون فوراً بعد الإزالة؟</h3>
<p>يُنصح بشطف البشرة بماء فاتر أو بارد فقط، وتجنب الماء الساخن والصابون القوي فوراً لمنع تهيج المسام التي تم تنظيفها حديثاً.</p>
<h3>هل بخاخ نير بالكيوي آمن للاستخدام أثناء فترة الحمل والمرضعة؟</h3>
<p>نعم، منتجات إزالة الشعر الموضعية آمنة عموماً للحوامل والمرضعات لأن امتصاصها عبر الجلد شبه معدوم. ومع ذلك، يُفضل إجراء اختبار الحساسية لاحتمال تغير حساسيتها الهرمونية.</p>
<h3>كم تدوم النعومة الناتجة عن استخدام بخاخ نير بالكيوي؟</h3>
<p>تدوم النعومة عادة لعدة أيام وتصل إلى أسبوع كامل، وهي فترة أطول مرتين مقارنة بالحلاقة بالموس لأن البخاخ يذيب الشعر تحت السطح السطحي للجلد مباشرة.</p>
<h3>ما العمل إذا شعرت بحرارة أو وخز أثناء رش المنتَج؟</h3>
<p>إذا شعرت بتهييج أو وخز شديد، امسحي الرغوة فوراً بمنشفة رطبة واشطفي المنطقة بماء بارد وفير. إذا استمر الاحمرار، يُنصح باستشارة الطبيب أو الصيدلي.</p>
<h3>هل يحتاج بخاخ نير بالكيوي إلى رج العبوة قبل الاستخدام؟</h3>
<p>نعم، يجب رج عبوة البخاخ جيداً لعدة ثوانٍ قبل كل رش لضمان خروج الرغوة بقوام متجانس ودمج المكونات المرطبة والفعالة بشكل مثالي.</p>
<h3>ما الفرق بين تأثير الشفرة الموس وتأثير بخاخ نير؟</h3>
<p>الشفرة تقص الشعر بزاوية حادة مسببة ملمساً خشناً وجروحاً محتملة، بينما يذيب بخاخ نير الشعر بحواف دائرية ناعمة ويوفر تغطية سريعة بدون لمس اليدين وترطيباً مغذياً بخلاصة الكيوي.</p>
<h3>هل يترك بخاخ نير رائحة كيميائية قوية على الجلد؟</h3>
<p>تم تطوير بخاخ نير بتقنيات حديثة لتحييد الروائح الكيميائية وإضافة عطر الكيوي الفاكهي المنعش الذي يطغى على المكونات الكيميائية ويترك البشرة برائحة زكية.</p>
<h3>كم مرة يمكن استخدام بخاخ نير بالكيوي في الشهر؟</h3>
<p>يمكن استخدامه كلما نما الشعر مجدداً (عادة مرة كل 7 إلى 10 أيام)، مع مراعاة عدم استخدامه على نفس المنطقة مرتين خلال 48 ساعة.</p>
<h3>كيف يتم تخزين عبوة البخاخ 200مل بشكل آمن؟</h3>
<p>تُحفظ العبوة في مكان بارد وجاف بعيداً عن أشعة الشمس المباشرة، ومصادر الحرارة أو اللهب، وبدرجة حرارة أقل من 30 مئوية، وبعيداً عن متناول الأطفال.</p>
<h3>أين يُصنع بخاخ نير وما هي الشركة المالكة للعلامة؟</h3>
<p>تنتج علامة نير (Nair) بواسطة شركة Church & Dwight Co., Inc. العالمية الرائدة في منتجات العناية الشخصية، وتُصنع المنتجات في مصانع الشركة بالمملكة المتحدة والولايات المتحدة الأمريكية.</p>`,
    "tags": ["نير", "nair", "بخاخ_إزالة_الشعر", "خلاصة_الكيوي", "إزالة_الشعر", "إكليل_أبها"]
  },
  "en": {
    "title": "Nair Hair Removal Spray with Kiwi Extract 200ml for Fast Removal and Smooth Skin",
    "meta_title": "Nair Hair Removal Spray with Kiwi Extract 200ml | Ekleel Abha",
    "meta_description": "Shop Nair Hair Removal Spray with Kiwi Extract 200ml for fast, easy, and painless hair removal. Enjoy silky smooth skin with long-lasting hydration at Ekleel Abha Pharmacy.",
    "description": `<h2>Product Overview</h2>
<p><strong>Nair Hair Removal Spray with Kiwi Extract (200 ml)</strong> represents a modern, fast, and completely painless solution for achieving touchably smooth, hair-free skin. Engineered for ultimate convenience and touchless application, this innovative depilatory spray delivers an even aerated foam coverage without needing to rub the product into your skin with your hands. It is the premier choice for rapidly treating larger body surfaces like legs, arms, and hard-to-reach areas. The advanced formula combines gentle chemical depilatory power to dissolve hair just below the skin line with the rich botanical nourishment of natural Kiwi Extract, famous for its antioxidant vitamins and skin-clarifying benefits.</p>
<p>The lightweight foam dissolves stubble and body hair efficiently in just 3 to 10 minutes, allowing you to wipe away unwanted hair seamlessly using a damp cloth or the included spatula. Enhanced with hydrating mineral oils and soothing botanical agents, Nair Hair Removal Spray guards the skin barrier against moisture loss and dryness, leaving your skin noticeably silky, visibly radiant, and delicately perfumed with a refreshing fruity kiwi scent that lingers long after treatment.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Rapid Touchless Spray Application:</strong> The continuous aerated foam spray allows effortless, hands-free coverage of large body areas like legs and arms within seconds.</li>
  <li><strong>Painless & Fast Hair Removal:</strong> Dissolves short and stubborn hair near the root in just 3 to 10 minutes without pain or physical discomfort.</li>
  <li><strong>Enriched with Natural Kiwi Extract:</strong> Delivers essential vitamin C and antioxidant benefits to clarify, soothe, and boost skin radiance during depilation.</li>
  <li><strong>Softer Regrowth & No Ingrown Hairs:</strong> Dissolves hair tips into smooth, rounded ends, effectively eliminating sharp stubble, itching, and strawberry legs (Keratosis Pilaris).</li>
  <li><strong>100% Protection from Nicks & Razor Cuts:</strong> A safe alternative to razor blades that completely eliminates the risk of cuts, scratches, and mechanical friction burn.</li>
  <li><strong>Deep Hydration & Long-Lasting Smoothness:</strong> Moisture-locking formulation prevents transepidermal water loss, maintaining smooth, glowing skin days longer than shaving.</li>
  <li><strong>Refreshing Fruity Kiwi Fragrance:</strong> Features advanced odor-neutralizing technology that masks chemical smells, replacing them with a crisp, invigorating kiwi fragrance.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Preparation & Shake):</strong> Ensure your skin is clean and completely dry. Shake the aerosol canister vigorously for several seconds before use to blend the ingredients into a uniform foam.</li>
  <li><strong>Step 2 (Spray Coverage):</strong> Hold the canister approximately 5 to 10 cm away from the target skin area. Spray evenly to create a continuous foam layer that fully coats the hair. Do not rub in with hands.</li>
  <li><strong>Step 3 (Wait & Patch Check):</strong> Leave the foam on your skin for 3 to 5 minutes. Test a very small patch using a damp cloth or the spatula; if the hair wipes away easily, proceed to remove the rest.</li>
  <li><strong>Step 4 (Maximum Application Limit):</strong> For thicker or coarse hair, you may leave the foam on for a few additional minutes, but <strong>NEVER exceed 10 minutes of total application time</strong> to prevent irritation.</li>
  <li><strong>Step 5 (Removal & Rinse):</strong> Gently wipe away the foam and dissolved hair with a warm damp cloth or spatula against the direction of hair growth. Rinse the skin thoroughly with lukewarm water without soap, and pat dry.</li>
</ul>

<h2>Ingredients Overview</h2>
<p>Nair Hair Removal Spray with Kiwi Extract relies on a carefully balanced formulation of active depilatory agents and protective conditioning botanicals:</p>
<ul>
  <li><strong>Potassium Thioglycolate:</strong> The core active depilatory agent that chemically reduces the disulfide bonds in hair keratin, weakening the hair shaft matrix so it turns into a wipeable gel.</li>
  <li><strong>Calcium Hydroxide:</strong> An alkaline builder that elevates formula pH to create an optimal basic environment, causing the hair shaft to swell for rapid thioglycolate penetration.</li>
  <li><strong>Kiwi Fruit Extract (Actinidia Chinensis Extract):</strong> A potent botanical extract rich in natural vitamin C, fruit acids, and antioxidants that soothe skin, fight oxidative stress, and revitalize skin tone.</li>
  <li><strong>Mineral Oil & Glycerin:</strong> Essential emollient and humectant agents that form a protective moisture barrier on the skin, preventing dryness and ensuring silky softness post-removal.</li>
  <li><strong>Cetearyl Alcohol & Emulsifiers:</strong> Stabilize the aerated foam texture, ensuring it clings evenly to body hair without dripping during the application wait time.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li><strong>Mandatory Patch Test:</strong> Always spray a small test patch on your leg 24 hours prior to full application to monitor for potential skin sensitivity or allergic reaction.</li>
  <li><strong>Prohibited Body Areas:</strong> Formulated for body hair only; DO NOT spray on the face, eyes, nose, ears, nipples, or genital/perianal regions.</li>
  <li><strong>Unsuitable Skin Conditions:</strong> Never apply to broken, inflamed, sunburned, irritated, eczema-prone skin, or open cuts.</li>
  <li><strong>Strict Timer & Storage Safety:</strong> Never exceed 10 minutes total contact time on skin. Pressurized container; store away from heat, open flames, direct sunlight, and out of reach of children.</li>
</ul>

<h2>Who Is This For?</h2>
<p><strong>Nair Hair Removal Spray with Kiwi Extract</strong> is formulated for women and men seeking a fast, touchless, and painless method to remove unwanted body hair. It is ideal for individuals looking for effortless coverage over large areas like legs and arms without messy hands, providing touchably smooth, hydrated skin with a fresh fruity kiwi fragrance.</p>`,
    "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Nair</td></tr>
  <tr><th>Category</th><td>Body Care / Hair Removal</td></tr>
  <tr><th>Product Type</th><td>Depilatory Hair Removal Spray</td></tr>
  <tr><th>Volume/Weight</th><td>200 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (including normal & dry skin)</td></tr>
  <tr><th>Finish</th><td>Silky Smooth & Radiant Hair-Free Skin</td></tr>
  <tr><th>Texture</th><td>Light Aerated Foam Spray</td></tr>
  <tr><th>Fragrance</th><td>Fresh Kiwi & Fruity Fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Kiwi Extract, Potassium Thioglycolate, Calcium Hydroxide</td></tr>
  <tr><th>Country of Origin</th><td>United Kingdom / USA</td></tr>
  <tr><th>Manufacturer</th><td>Church & Dwight Co., Inc.</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens (16+)</td></tr>
</tbody>
</table>`,
    "knowledge_base": `<h2>Clinical & Science Guide to Depilatory Sprays and Skin Hydration</h2>

<h3>What problem does this solve?</h3>
<p>Nair Hair Removal Spray with Kiwi Extract solves the challenge of removing unwanted body hair over large surface areas rapidly and painlessly. It effectively eliminates the common drawbacks of mechanical shaving—such as razor cuts, painful nicks, skin burns, ingrown hairs, and strawberry legs—by dissolving hair below the surface while delivering botanical hydration.</p>

<h3>Why does this condition happen?</h3>
<p>Body hair originates in hair follicles in the dermis layer, where keratin proteins are synthesized and bonded by strong covalent disulfide bridges. Shaving severs the hair shaft horizontally at the skin surface, producing a flat, razor-sharp edge. As this sharp tip grows out over the next 24 to 48 hours, it creates a rough prickly stubble and frequently curls back into the follicle wall, inducing localized folliculitis and ingrown hairs. Shaving also scrapes off surface lipids, drying out the skin. A chemical depilatory spray solves this by dissolving the hair shaft into a soft, rounded tip within the upper follicular pore, preventing ingrown hairs while preserving skin moisture.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Perform a Patch Test:</strong> Always spray a small test patch on your lower leg and wait 24 hours to confirm skin compatibility.<br>2. <strong>Weekly Gentle Exfoliation:</strong> Exfoliate your skin once or twice weekly with a gentle body scrub to clear dead skin cells and allow smooth hair growth.<br>3. <strong>Daily Skin Moisturizing:</strong> Apply a hydrating body lotion daily to maintain healthy skin barrier function and skin elasticity post-removal.<br>4. <strong>Avoid Direct Sun Exposure:</strong> Refrain from sunbathing, tanning beds, and swimming in chlorinated water for 24 hours following hair removal to protect open pores.<br>5. <strong>Respect Application Timers:</strong> Use a timer to ensure application time stays between 3 and 10 minutes maximum to safeguard the stratum corneum.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Depilatory sprays make hair grow back thicker, darker, and faster."<br><strong>Fact:</strong> Depilatory sprays operate exclusively on the surface hair shaft and do not penetrate deep hair roots or alter genetic/hormonal growth patterns. Regrowing hair emerges with soft, rounded tips, giving a noticeably smoother feel compared to sharp razor stubble.</p>

<h3>Scientific Explanation</h3>
<p>Chemical depilation operates through the biochemical process of keratolysis. Hair keratin consists of long polypeptide chains held together by strong covalent <strong>disulfide bonds (-S-S-)</strong>. The active ingredient, <strong>Potassium Thioglycolate</strong>, acts as a reducing agent that donates hydrogen atoms to cleave these disulfide bonds into sulfhydryl (-SH) groups. Simultaneously, <strong>Calcium Hydroxide</strong> provides an alkaline environment (elevated pH) that causes the hair structure to swell, facilitating rapid penetration of the depilatory ions. Within 3 to 10 minutes, the structural integrity of the hair collapses into a soft gel that wipes away easily without harming normal skin tissue.</p>`,
    "faqs": `<h3>What is Nair Hair Removal Spray with Kiwi Extract and how does it work?</h3>
<p>Nair Hair Removal Spray with Kiwi Extract 200ml is an innovative aerated foam spray designed for painless body hair removal. It sprays evenly over skin, using gentle depilatory actives to dissolve hair keratin close to the root in 3 to 10 minutes while hydrating skin with natural Kiwi Extract.</p>
<h3>What is the key advantage of a hair removal spray compared to traditional depilatory creams?</h3>
<p>The primary advantage is hands-free, touchless application. The spray provides fast, continuous foam coverage over large areas like legs and arms without getting cream on your hands or needing manual rubbing.</p>
<h3>What are the main active ingredients in Nair Spray with Kiwi Extract?</h3>
<p>Key active ingredients include Potassium Thioglycolate (hair dissolving agent), Calcium Hydroxide (alkaline builder), and natural Kiwi Fruit Extract rich in antioxidants and vitamin C for skin conditioning.</p>
<h3>How does Kiwi Extract support skin hydration and radiance during hair removal?</h3>
<p>Kiwi Extract is abundant in vitamin C, fruit acids, and antioxidants that soothe the skin, minimize chemical irritation, and boost natural radiance and smoothness during treatment.</p>
<h3>How long should Nair Spray be left on the skin before removing it?</h3>
<p>Leave the spray on for 3 to 5 minutes as a starting point. For thicker or coarser hair, application can be extended slightly, but NEVER exceed 10 minutes total application time.</p>
<h3>Can Nair Spray with Kiwi Extract be used on sensitive skin?</h3>
<p>It is formulated for all skin types. However, if your skin is extremely sensitive, always conduct a 24-hour patch test first or select Nair formulas specially labeled for sensitive skin.</p>
<h3>Which body areas are safe for using Nair Hair Removal Spray?</h3>
<p>It is ideal for legs, arms, underarms, and the bikini line. It allows smooth, uniform coverage across all these body areas.</p>
<h3>Is it safe to use Nair Spray on facial skin or genital areas?</h3>
<p>No, the spray should NEVER be applied to the face, eyebrows, nose, ears, nipples, or genital/perianal areas, as mucosal tissues in these regions are too sensitive.</p>
<h3>How can I ensure no irritation or allergic reaction occurs from the spray?</h3>
<p>Perform the recommended 24-hour patch test by spraying a small patch on your leg and observing for redness or itching before full body application.</p>
<h3>What are the correct application steps and recommended procedures?</h3>
<p>Shake can well, spray 5-10 cm from clean dry skin to coat hair without rubbing, wait 3-5 minutes, test a small area with a damp cloth, then wipe away foam and hair, and rinse thoroughly with lukewarm water.</p>
<h3>Should the spray be applied close to the skin and rubbed in with hands?</h3>
<p>No, do not rub the foam in with your hands. Spray from a distance of 5 to 10 cm to allow the aerated foam to form a uniform coating over hair automatically.</p>
<h3>How does Nair Spray prevent ingrown hairs and strawberry legs?</h3>
<p>It dissolves hair chemically below skin level, creating rounded, smooth hair ends rather than blunt sharp tips, preventing regrowing hair from trapping beneath pores.</p>
<h3>Does Nair Spray cause skin hyperpigmentation or darkening?</h3>
<p>No, when used according to instructions without exceeding 10 minutes, it will not darken skin. Hyperpigmentation only occurs if skin experiences chemical burns from severe timer overuse.</p>
<h3>Does hair grow back thicker or coarser after using Nair Spray?</h3>
<p>No, depilatory sprays do not affect internal hair follicles or genetic growth patterns. Regrowing hair features smooth rounded tips that feel noticeably softer than razor stubble.</p>
<h3>What precautions should be taken before and after using the spray?</h3>
<p>Before: Ensure skin is clean, dry, and free of cuts. After: Avoid antiperspirants, perfumed products, hot water, swimming, or sun exposure for 24 hours.</p>
<h3>Can I take a hot shower or use soap immediately after removal?</h3>
<p>Rinse with cool or lukewarm water only. Avoid hot showers and harsh soaps immediately after treatment to prevent irritating newly exposed pores.</p>
<h3>Is Nair Kiwi Spray safe for use during pregnancy and breastfeeding?</h3>
<p>Yes, topical depilatories are generally safe during pregnancy and nursing as systemic absorption is negligible. Perform a patch test first due to potential hormonal skin sensitivity changes.</p>
<h3>How long does the smoothness last after using Nair Kiwi Spray?</h3>
<p>Smoothness typically lasts several days up to a full week—up to twice as long as shaving—because hair is dissolved slightly below the skin surface level.</p>
<h3>What should I do if I feel burning or tingling during application?</h3>
<p>Immediately wipe off the foam with a damp cloth and rinse thoroughly with cold water. If skin irritation persists, consult a healthcare provider.</p>
<h3>Does Nair Kiwi Spray require shaking the canister before use?</h3>
<p>Yes, always shake the aerosol canister vigorously for several seconds before spraying to ensure proper propellant and formula mixing for a rich foam.</p>
<h3>What is the difference between razor shaving and Nair Spray hair removal?</h3>
<p>Shaving cuts hair at sharp angles causing prickly stubble and cuts. Nair Spray dissolves hair into smooth rounded ends with touchless spray coverage and kiwi-enriched hydration.</p>
<h3>Does Nair Spray leave a harsh chemical smell on the skin?</h3>
<p>No, Nair utilizes fragrance technology that neutralizes depilatory chemical odors, replacing them with a crisp, refreshing fruity kiwi scent.</p>
<h3>How often can Nair Kiwi Spray be used in a month?</h3>
<p>It can be used whenever hair regrows (typically every 7 to 10 days), allowing at least 48 hours between applications on the exact same skin area.</p>
<h3>How should the 200ml spray canister be stored safely?</h3>
<p>Store the pressurized canister in a cool, dry place below 30°C, away from direct heat, naked flames, direct sunlight, and out of reach of children.</p>
<h3>Where is Nair Spray manufactured and who owns the brand?</h3>
<p>Nair is owned and manufactured by Church & Dwight Co., Inc., a global leader in personal care, with production facilities in the UK and USA.</p>`,
    "tags": ["nair", "hair_removal_spray", "kiwi_extract", "depilatory_spray", "ekleel_abha"]
  }
};

const outputFilePath = path.join(__dirname, '1463.json');

fs.writeFileSync(outputFilePath, JSON.stringify(productData, null, 2), 'utf-8');
console.log('Successfully generated 1463.json at:', outputFilePath);
