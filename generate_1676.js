const fs = require('fs');
const path = require('path');

const productData = {
  "product_id": "1676",
  "sku": "EK-1676",
  "gtin": "6936711835560",
  "category": "العطور / عطور نسائية",
  "brand": "Carlotta",
  "ar": {
    "title": "بخاخ او دي تواليت سكاندرال للنساء من كارلوتا، 100 مل",
    "meta_title": "بخاخ او دي تواليت سكاندرال للنساء من كارلوتا 100 مل | إكليل أبها",
    "meta_description": "تسوق بخاخ او دي تواليت سكاندرال للنساء من كارلوتا بحجم 100 مل. عطر زهري دافئ يجمع بين العسل والبرتقال والباتشولي لثبات وجاذبية لا تُقاوم من صيدلية إكليل أبها.",
    "description": `<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>بخاخ أو دي تواليت سكاندرال للنساء من كارلوتا (Carlotta Scandal Eau de Toilette Spray for Women 100ml)</strong> تجسيداً راقياً للأنوثة الجذابة والجريئة، حيث يجمع بين سحر النفحات الزهرية الفواحة ودفء المكونات الشرقية الغورماند العميقة. صُمم هذا العطر بعناية فائقة ليعكس أسلوب المرأة الحديثة الواثقة من نفسها والتي تبحث عن توقيع عطري فريد يترك أثراً انطباعياً ساحراً يدوم طويلاً في كافة المناسبات والأوقات.</p>
<p>يتميز هذا العطر بتركيبته المتوازنة بتركيز "أو دي تواليت" (Eau de Toilette) بحجم 100 مل، مما يوفر توازناً مثالياً بين الانتشار العطري الفواح والثبات المريح على البشرة والملابس دون أن يكون ثقيلاً أو مزعجاً. يفتتح العطر بنفحات منعشة وحيوية من الحمضيات المشرقة، ثم يتدرج ببراعة نحو قلب زهري مفعم بالأنوثة، مستقراً على قاعدة غنية وشديدة الدفء من العسل والكراميل والباتشولي، مما يمنحه شخصية حسية لا تُنسى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>توليفة عطرية فاخرة ومتوازنة:</strong> تمزج بين انتعاش الحمضيات وسحر الزهور البيضاء ودفء العسل والكراميل لتجربة حسية غنية ومميزة.</li>
  <li><strong>ثبات ممتاز وفوحان ملموس:</strong> تضمن الزيوت العطرية النقية في تركيبته ثباتاً يدوم لساعات طويلة على الجلد والأقمشة مع هالة عطرية جذابة تتبع خطواتك.</li>
  <li><strong>تصميم أنيق وزجاجة راقية:</strong> تأتي العبوة بحجم 100 مل في زجاجة مصممة بأناقة تضفي لمسة من الفخامة على منصة التجميل الخاصة بكِ.</li>
  <li><strong>مناسب لكافة المناسبات:</strong> يمكن ارتداؤه في اللقاءات اليومية، أوقات العمل، والأمسيات الخاصة حيث يضفي حضوراً لافتاً ودافئاً.</li>
  <li><strong>لطيف على البشرة:</strong> تركيبة معتمدة صُممت بزيوت عطرية ناعمة تقلل من تهيج البشرة وتمنح انطباعاً منعشاً ومريحاً.</li>
  <li><strong>سعر اقتصادي بجودة فاخرة:</strong> يقدم بديل عطري مذهل وأنيق يضاهي العطور العالمية الباهظة بثبات وجودة ممتازة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (تجهيز البشرة):</strong> يُفضل رش العطر بعد الاستحمام مباشرة عندما تكون مسام البشرة نظيفة ومترطبة، مما يساهم في حبس جزيئات العطر لثبات أطول.</li>
  <li><strong>الخطوة الثانية (الرش على نقاط النبض):</strong> قمي برش العطر من مسافة 15-20 سم على نقاط النبض مثل المعصمين، الرقبة، خلف الأذنين، ودواخل الكوعين.</li>
  <li><strong>الخطوة الثالثة (تجنب فرك المعصمين):</strong> تجنبي فرك المعصمين ببعضهما بعد الرش حتى لا تتفكك جزيئات النوتات العطرية العليا وتتغير رائحة العطر.</li>
  <li><strong>الخطوة الرابعة (الرش على الملابس والشعر):</strong> يمكنك رش رذاذ خفيف في الهواء والمرور من خلاله أو رشه على أطراف الملابس لتعزيز الفوحان والانتشار العطري.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<p>يعتمد عطر سكاندرال من كارلوتا على هرم عطري متناغم بدقة من أحدث المكونات والزيوت العطرية العالية الجودة:</p>
<ul>
  <li><strong>المقدمة (Top Notes):</strong> تتألق بلمسات حيوية منعشة من <em>البرتقال الأحمر (Blood Orange)</em> و<em>اليوسفي (Mandarin Orange)</em> لتوفير دفعة أولية من الانتعاش والحيوية المشرقة.</li>
  <li><strong>القلب العطري (Heart Notes):</strong> ينبض بعبير أنثوي ساحر يمزج بين <em>العسل الطبيعي (Honey)</em>، <em>أزهار الجاردينيا (Gardenia)</em>، <em>زهر البرتقال (Orange Blossom)</em>، <em>الياسمين (Jasmine)</em>، و<em>الخوخ (Peach)</em>.</li>
  <li><strong>القاعدة العطرية (Base Notes):</strong> ترتكز على عمق دافئ ومغرٍ من <em>شمع العسل (Beeswax)</em>، <em>الكراميل اللذيذ (Caramel)</em>، <em>الباتشولي (Patchouli)</em>، و<em>العرقسوس (Licorice)</em> لضمان الثبات والانتشار العميق.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>هذا المنتج مخصص للاستخدام الخارجي فقط؛ تجنبي الرش المباشر في العينين أو الأغشية المخاطية.</li>
  <li>يُحفظ المنتج في مكان بارد وجاف بعيداً عن أشعة الشمس المباشرة ومصادر الحرارة لضمان عدم تلف الزيوت العطرية.</li>
  <li>في حال ظهور أي علامات تهيج أو احمرار على البشرة، يُنصح بإيقاف الاستخدام وغسل المنطقة بالماء الفاتر.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال الصغار لتجنب الاستخدام الخاطئ أو الابتلاع العرضي.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>النساء اللاتي يبحثن عن عطر أنثوي دافئ وجذاب يعبر عن الجرأة والأناقة في وقت واحد.</li>
  <li>عاشقات العطور الشرقية الزهرية ذات لمسات العسل والكراميل التي تمنح إحساساً بالفخامة والراحة.</li>
  <li>من يرغبن في عطر يومي أو مخصص للمناسبات الخاصة بثبات ممتاز وحجم كبير (100 مل) يدوم لفترة طويلة.</li>
  <li>كهدية فاخرة ومثالية للصديقات والمقربات في المناسبات السعيدة وأعياد الميلاد.</li>
</ul>`,
    "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>Carlotta (كارلوتا)</td></tr>
  <tr><th>الفئة</th><td>العطور / عطور نسائية</td></tr>
  <tr><th>نوع المنتج</th><td>بخاخ أو دي تواليت (Eau de Toilette Spray)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة</td></tr>
  <tr><th>المظهر النهائي</th><td>ثبات عالي ورائحة دافئة جذابة</td></tr>
  <tr><th>الملمس</th><td>رذاذ عطري سائل (Liquid Spray)</td></tr>
  <tr><th>العطر</th><td>زهري دافئ مع العسل والكراميل والباتشولي</td></tr>
  <tr><th>المكونات النشطة</th><td>البرتقال الأحمر، العسل، الجاردينيا، الكراميل، الباتشولي</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين</td></tr>
  <tr><th>الشركة المصنعة</th><td>Carlotta Perfumes & Cosmetics Ltd.</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين (النساء)</td></tr>
</tbody>
</table>`,
    "knowledge_base": `<h2>الدليل العطري والمعرفي الشامل لثبات العطور والزيوت العطرية</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يحل هذا المنتج مشكلة زوال العطور السريع وبحث المرأة عن عطر يجمع بين الانتعاش النهاري والفوحان الدافئ الجذاب للأمسيات دون الحاجة لشراء عدة عطور باهظة الثمن. يقدم عطر سكاندرال من كارلوتا هبّة عطرية متوازنة وثابتة تدوم طويلاً وتمنح انطباعاً بالفخامة وحضوراً مميزاً طوال اليوم.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تتلاشى العطور العادية بسرعة على البشرة نتيجة انخفاض نسبة الزيوت العطرية أو استخدام زيوت تطير سريعاً عند التعرض للهواء والجفاف، أو نتيجة تطبيق العطر على بشرة جافة تفقد الرطوبة بسرعة. تعمل العطور المصممة بهرم عطري متكامل (مقدمة حمضية وقلب زهري وقاعدة غنية بالباتشولي والعسل) على الالتصاق بزيوت البشرة والتصاعد الدائم بحرارة الجسم الطبيعية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>ترطيب البشرة قبل الرش:</strong> استخدمي لوشن غير معطر أو فازلين خفيف على نقاط النبض قبل تطبيق العطر لزيادة ثبات الجزيئات العطرية لعدة ساعات إضافية.<br>2. <strong>تجنب فرك العطر:</strong> اترك قطرات العطر تجف تلقائياً على الجلد دون فرك لمنع تكسير الروابط الكيميائية للجزيئات العطرية العليا.<br>3. <strong>التخزين الصحيح:</strong> احتفظي بزجاجة العطر في علبتها الأصلية أو داخل خزانة بعيدة عن الضوء والرطوبة والحرارة العالية لتجنب تغير رائحتها مع الوقت.<br>4. <strong>الرش على الأنسجة الطبيعية:</strong> رش العطر على الملابس المصنوعة من القطن أو الصوف يمنحك ثباتاً مضاعفاً يمتد لأيام.</p>

<h3>خرافات شائعة حول العناية بالعطور</h3>
<p><strong>خرافة:</strong> "حفظ العطر في الثلاجة يزيد من ثباته وقوته."<br><strong>الحقيقة:</strong> التغيرات المفاجئة والتقلبات الشديدة في درجات الحرارة بين داخل الثلاجة وخارجها قد تفسد التركيب الكيميائي للزيوت العطرية الدقيقة وتغير رائحتها الأنيقة. الحفظ في مكان مظلم ومعتدل الحرارة هو الخيار الأمثل.<br><strong>خرافة:</strong> "العطور ذات تركيز أو دي تواليت لا تدوم لأكثر من ساعة واحدة."<br><strong>الحقيقة:</strong> ثبات العطر يعتمد بشكل أساسي على المكونات الثقيلة في القاعدة العطرية مثل الباتشولي والعسل والكراميل وليس فقط على اسم التركيز. عطر سكاندرال يوفر ثباتاً ممتازاً لساعات طويلة بفضل قاعدته الغنية.</p>

<h3>التفسير العلمي لآلية العمل والانتشار العطري</h3>
<p>يعتمد الانتشار العطري لعطر سكاندرال على تباين الأوزان الجزيئية ومعدلات تطاير (Volatility Rates) الزيوت العطرية المكونة للهرم العطري. تبدأ الجزيئات الخفيفة مثل البرتقال الأحمر واليوسفي بالتطاير أولاً لتوفير انطباع حسي منعش، تليها الجزيئات متوسطة الوزن من أزهار الجاردينيا والياسمين وزهر البرتقال التي تنتشر بحرارة الجلد. أخيراً، تظل الجزيئات الثقيلة عالية الوزن الجزيئي مثل شمع العسل والكراميل والباتشولي مثبتة على سطح الجلد، حيث تفرز أريجاً دافئاً ومستمراً يتفاعل مع الكيمياء الطبيعية لجسمكِ.</p>`,
    "faqs": `<h3>ما هو عطر سكاندرال للنساء من كارلوتا؟</h3>
<p>عطر سكاندرال من كارلوتا هو بخاخ أو دي تواليت بحجم 100 مل مخصص للنساء، يمتاز بتوليفة عطرية زهريّة شرقية تدمج بين انتعاش الحمضيات وسحر الزهور البيضاء ودفء العسل والكراميل والباتشولي.</p>

<h3>ما هي سعة زجاجة العطر وهل تكفي لفترة طويلة؟</h3>
<p>تأتي زجاجة العطر بسعة 100 مل، وهي كمية وفيرة ومناسبة للاستخدام اليومي المستمر لعدة أشهر دون الحاجة لشراء عبوة جديدة في وقت قريب.</p>

<h3>هل العطر مناسب للاستخدام اليومي أم للمناسبات؟</h3>
<p>يمتاز العطر بتركيبة متوازنة تجعله مثالياً لكلا الأغراض؛ فهو خفيف بما يكفي للاستخدام اليومي في العمل واللقاءات النهارية، ودافئ وجذاب بما يكفي للسهرات والمناسبات الخاصة.</p>

<h3>ما هي النوتات العطرية العلوية (المقدمة) في العطر؟</h3>
<p>تتكون افتتاحية العطر المنعشة من البرتقال الأحمر المشرق واليوسفي، مما يمنحكِ شعوراً فورياً بالنشاط والحيوية فور الرش.</p>

<h3>ما هي مكونات قلب العطر (Heart Notes)؟</h3>
<p>يتكون قلب العطر من باقة زهرية ساحرة من أزهار الجاردينيا، زهر البرتقال، الياسمين، مع نفحات حلوة من العسل الطبيعي والخوخ الناضج.</p>

<h3>ما هي مكونات قاعدة العطر (Base Notes) التي تضمن ثباته؟</h3>
<p>ترتكز قاعدة العطر على مزيج دافئ وغني من شمع العسل، الكراميل اللذيذ، الباتشولي الدافئ، ولمسات من العرقسوس، وهي المكونات المسؤولة عن ثبات العطر لساعات طويلة.</p>

<h3>كم تدوم رائحة العطر على الجلد والملابس؟</h3>
<p>يدوم العطر عادة من 6 إلى 8 ساعات على البشرة، ويمكن أن يمتد ثباته لأكثر من 24 ساعة عند رشه على الملابس والأقمشة القطنية.</p>

<h3>هل تسبب زيوت العطر تهيجاً للبشرة الحساسة؟</h3>
<p>تم تصنيع العطر بزيوت عطرية معتمدة وآمنة للاستخدام الظاهري. إذا كانت بشرتكِ شديدة الحساسية، يُفضل اختبار رش كمية صغيرة على الكوع قبل الاستخدام الكامل.</p>

<h3>ما هي أفضل طريقة لرش العطر لضمان أقصى ثبات؟</h3>
<p>أفضل طريقة هي رش العطر على نقاط النبض في الجسم مثل المعصمين، جانبي الرقبة، خلف الأذنين، ودواخل المرفقين من مسافة 15 سم.</p>

<h3>هل يمكن فرك المعصمين ببعضهما بعد رش العطر؟</h3>
<p>لا يُنصح بفرك المعصمين مطلقاً، لأن الفرك يولد حرارة تفكك الجزيئات العطرية الخفيفة في المقدمة وتسرع تلاشي الرائحة بدلاً من تثبيتها.</p>

<h3>هل العطر زيتي أم سائل بخاخ؟</h3>
<p>العطر عبارة عن بخاخ سائل بتركيز أو دي تواليت (Eau de Toilette Spray) يمنح رذاذاً ناعماً ومتساوياً يسهل توزيعه على الجسم والملابس.</p>

<h3>ما هي عائلة العطور التي ينتمي إليها هذا العطر؟</h3>
<p>ينتمي العطر إلى عائلة العطور الزهرية الشرقية الغورماند (Floral Oriental Gourmand)، والتي تشتهر برائحتها الجذابة التي تجمع بين الزهور والعسل والكراميل.</p>

<h3>هل يترك العطر بقعاً على الملابس البيضاء؟</h3>
<p>عند رشه من مسافة مناسبة (15-20 سم)، يتبخر السائل شفافاً دون ترك بقع. يُفضل تجنب الرش المباشر على الأقمشة الرقيقة جداً مثل الحرير عن قرب شديد.</p>

<h3>كيف يمكن حفظ زجاجة العطر للحفاظ على رائحتها الأصلية؟</h3>
<p>يُحفظ العطر في مكان بارد وجاف بعيداً عن أشعة الشمس المباشرة، الحرارة، والرطوبة العالية في الحمام حتى لا تتأكسد زيوت العطر.</p>

<h3>هل العطر مناسب لإهدائه في المناسبات السعيدة؟</h3>
<p>نعم، يُعد عطر سكاندرال من كارلوتا هدية فاخرة ومثالية للنساء في أعياد الميلاد، المناسبات السعيدة، والأعياد بفضل تصميم زجاجته الأنيق ورائحته الممتازة.</p>

<h3>ما الفرق بين أو دي تواليت (EDT) وأو دي بارفان (EDP)؟</h3>
<p>تركيز أو دي تواليت يحتوي على نسبة زيوت عطرية تتراوح بين 5% و15%، مما يجعله أكثر انتعاشاً وأخف وزناً للاستخدام اليومي مقارنة بالأو دي بارفان الأكثر كثافة.</p>

<h3>هل يمكن استخدام العطر على الشعر؟</h3>
<p>يُفضل عدم الرش المباشر على فروة الرأس لتجنب جفاف الشعر بفعل الكحول العطري. يمكنكِ رش الرذاذ في الهواء ثم السير تحته ليعلق العطر بالشعر بلطف.</p>

<h3>هل العطر آمن للاستخدام أثناء الحمل؟</h3>
<p>العطور الخارجية آمنة بشكل عام أثناء الحمل. ولكن نظراً لحساسية بعض النساء للروائح خلال هذه الفترة، يُفضل تجربة الرائحة أولاً أو استشارة الطبيب.</p>

<h3>ما الذي يجعل عطر سكاندرال من كارلوتا مميزاً في إكليل أبها؟</h3>
<p>يوفر العطر توازناً استثنائياً بين الجودة العالية والرائحة الجذابة والسعر المناسب، مع ضمان الحصول على منتج أصلي ومفحوص من صيدلية إكليل أبها.</p>

<h3>هل يتغير العطر بعد رشه بعدة ساعات؟</h3>
<p>نعم، العطر يتطور بمرور الوقت من الافتتاحية الحمضية المنعشة إلى القلب الزهري العسلي، ثم يستقر في النهاية على القاعدة الدافئة المكونة من الباتشولي والكراميل.</p>

<h3>هل يناسب العطر فصل الصيف أم الشتاء؟</h3>
<p>بفضل تركيبته الغنية بالعسل والباتشولي والانتعاش الحمضي، فهو مناسب للاستخدام طوال العام؛ حيث تبرز نوتاته المنعشة صيفاً ونوتاته الدافئة شتاءً.</p>

<h3>ما هي بلد المنشأ لعطر كارلوتا سكاندرال؟</h3>
<p>تم تصنيع العطر في جمهورية الصين الشعبية وفق معايير التصنيع العطري والتجميلي الدولية لضمان الجودة والسلامة.</p>

<h3>هل العطر مختبر طبياً ومصرح به؟</h3>
<p>نعم، العطر مصنع من مكونات تجميلية آمنة ومعتمدة ومطابقة للمواصفات القياسية الخاصة بمنتجات العناية الشخصية والعطور.</p>

<h3>هل يحتوي العطر على مكونات حيوانية؟</h3>
<p>المكون العطري لشمع العسل والعسل في العطر عبارة عن مركبات عطرية مصنعة ومحاكاة لنوتات العسل الطبيعي، العطر آمن ومناسب لجميع المستخدمات.</p>

<h3>كيف أحصل على عطر كارلوتا سكاندرال الأصلي؟</h3>
<p>يمكنك طلب العطر فوراً وبكل سهولة عبر متجر صيدلية إكليل أبها الإلكتروني مع التوصيل السريع لجميع مناطق المملكة العربية السعودية.</p>`,
    "tags": ["carlotta", "scandal", "عطور_نسائية", "بخاخ_عطر", "إكليل_أبها", "عطر_سكاندرال", "eau_de_toilette"]
  },
  "en": {
    "title": "Carlotta Scandal Eau de Toilette Spray for Women, 100ml",
    "meta_title": "Carlotta Scandal Eau de Toilette Spray for Women 100ml | Ekleel Abha",
    "meta_description": "Shop Carlotta Scandal Eau de Toilette Spray for Women (100ml). Elegant warm floral fragrance blending honey, blood orange, and patchouli. Authentic from Ekleel Abha Pharmacy.",
    "description": `<h2>Product Overview</h2>
<p>The <strong>Carlotta Scandal Eau de Toilette Spray for Women (100ml)</strong> is a sophisticated expression of bold, alluring femininity. Seamlessly blending vibrant floral blossoms with the rich warmth of oriental gourmand accords, this fragrance is meticulously crafted for the modern, confident woman who seeks a signature scent that leaves an indelible impression wherever she goes.</p>
<p>Housed in a generous 100ml bottle with an Eau de Toilette concentration, this scent offers an optimal balance between radiating sillage and comfortable, long-lasting wear on skin and fabrics. The fragrance opens with an invigorating burst of radiant citrus, gracefully transitions into a romantic white floral heart drizzled with natural honey, and anchors itself on a deeply sensual base of rich caramel, beeswax, and earthy patchouli.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Luxurious Olfactory Harmony:</strong> Combines fresh citrus top notes, captivating white flowers, and warm honey-caramel accords for a multi-layered sensory experience.</li>
  <li><strong>Long-Lasting Performance & Sillage:</strong> Formulated with premium aromatic oils that ensure enduring longevity and a mesmerizing trail throughout the day.</li>
  <li><strong>Elegant Bottle Design:</strong> Packaged in a stunningly designed 100ml glass bottle that adds a touch of glamour to any vanity setup.</li>
  <li><strong>Versatile Wearability:</strong> Perfectly tailored for daily daytime wear, professional settings, or intimate evening gatherings.</li>
  <li><strong>Skin-Friendly Formulation:</strong> Crafted using safe cosmetic-grade aromatic ingredients that minimize skin irritation while providing continuous freshness.</li>
  <li><strong>Exceptional Value:</strong> Delivers high-end luxury fragrance vibes and superior longevity at an accessible, affordable price point.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Skin Preparation):</strong> Apply fragrance immediately following a shower when skin pores are clean and hydrated to lock in scent molecules.</li>
  <li><strong>Step 2 (Pulse Point Application):</strong> Hold the bottle 15-20 cm away and spray directly onto key pulse points including wrists, sides of the neck, behind ears, and inner elbows.</li>
  <li><strong>Step 3 (Avoid Rubbing):</strong> Allow the perfume spray to dry naturally on the skin. Never rub wrists together, as friction crushes top-note molecules.</li>
  <li><strong>Step 4 (Fabric misting):</strong> Lightly mist the air and step through, or spray onto fabric hems and scarves to amplify sillage and projection.</li>
</ul>

<h2>Ingredients Overview</h2>
<p>Carlotta Scandal features a carefully balanced olfactory pyramid composed of high-grade essential oils and aromatic notes:</p>
<ul>
  <li><strong>Top Notes:</strong> Crisp, invigorating burst of <em>Blood Orange</em> and <em>Mandarin Orange</em> for an instantly uplifting citrus opening.</li>
  <li><strong>Heart Notes:</strong> Romantic floral center blending <em>Natural Honey</em>, <em>Gardenia</em>, <em>Orange Blossom</em>, <em>Jasmine</em>, and luscious <em>Peach</em>.</li>
  <li><strong>Base Notes:</strong> Rich, grounding base of <em>Beeswax</em>, <em>Decadent Caramel</em>, <em>Warm Patchouli</em>, and subtle <em>Licorice</em> for maximum longevity.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic use only; avoid direct contact with eyes and mucous membranes.</li>
  <li>Store in a cool, dry place away from direct sunlight and extreme thermal fluctuations to protect essential oils.</li>
  <li>Discontinue use if any unexpected redness or skin irritation occurs, and rinse affected areas with tepid water.</li>
  <li>Keep out of reach of children to prevent accidental ingestion or improper use.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Women seeking an alluring, warm floral perfume that exudes confidence, elegance, and charm.</li>
  <li>Fragrance lovers who appreciate gourmand scent profiles featuring notes of honey, gardenia, and caramel.</li>
  <li>Individuals looking for a high-volume (100ml) signature fragrance suitable for both daily wear and special occasions.</li>
  <li>Anyone looking for an elegant, beautifully packaged perfume gift for birthdays, anniversaries, and holidays.</li>
</ul>`,
    "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Carlotta</td></tr>
  <tr><th>Category</th><td>Perfumes / Women's Fragrances</td></tr>
  <tr><th>Product Type</th><td>Eau de Toilette Spray</td></tr>
  <tr><th>Volume/Weight</th><td>100ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types</td></tr>
  <tr><th>Finish</th><td>Long-Lasting Warm Floral Scent</td></tr>
  <tr><th>Texture</th><td>Liquid Fragrance Spray</td></tr>
  <tr><th>Fragrance</th><td>Warm Floral Gourmand (Honey, Caramel, Patchouli, Gardenia)</td></tr>
  <tr><th>Active Ingredients</th><td>Blood Orange, Honey, Gardenia, Caramel, Patchouli</td></tr>
  <tr><th>Country of Origin</th><td>China</td></tr>
  <tr><th>Manufacturer</th><td>Carlotta Perfumes & Cosmetics Ltd.</td></tr>
  <tr><th>Age Group</th><td>Adults (Women)</td></tr>
</tbody>
</table>`,
    "knowledge_base": `<h2>Comprehensive Clinical & Olfactory Knowledge Base</h2>

<h3>What problem does this solve?</h3>
<p>Carlotta Scandal solves the common issue of short-lived fragrances and the hassle of switching between multiple perfumes throughout the day. It provides a versatile, long-lasting scent signature that smoothly transitions from energizing daytime citrus to a cozy, seductive evening gourmand trail.</p>

<h3>Why does this condition happen?</h3>
<p>Many standard perfumes fade prematurely because they lack heavy, binding base notes or because they are applied to dehydrated skin. Fragrances built around an intricate scent pyramid—combining volatile citrus top notes with viscous base notes like patchouli, honey, and caramel—anchor more effectively to skin lipids, releasing fragrance continuously in response to body heat.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Moisturize Before Spraying:</strong> Apply a neutral unscented lotion or light occlusive to pulse points prior to spraying perfume to trap aromatic molecules longer.<br>2. <strong>Avoid Friction:</strong> Let the perfume mist dry naturally on your skin rather than rubbing your wrists together, which shears top-note chemical bonds.<br>3. <strong>Proper Storage:</strong> Store fragrance bottles in a dark, temperature-controlled environment away from bathroom humidity and sunlight to preserve aromatic integrity.<br>4. <strong>Apply to Natural Fabrics:</strong> Spraying perfume onto natural cotton or wool garments provides extended scent retention over several days.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Storing perfume in the refrigerator makes it last longer and perform better."<br><strong>Fact:</strong> Drastic temperature variations between inside the fridge and ambient air can disrupt the delicate equilibrium of essential oils, potentially altering the fragrance profile. Storing at steady room temperature in a dark cabinet is optimal.<br><strong>Myth:</strong> "Eau de Toilette concentrations only last for one hour."<br><strong>Fact:</strong> Longevity is primarily determined by the molecular weight of the base ingredients—such as patchouli, honey, and beeswax—rather than the concentration label alone. Carlotta Scandal delivers impressive multi-hour wear.</p>

<h3>Scientific Explanation of Scent Volatility and Mechanism</h3>
<p>The evaporation dynamics of Carlotta Scandal depend on the molecular weights and vapor pressures of its constituent essential oils. Low-molecular-weight monoterpenes in blood orange evaporate first, delivering an instant olfactory burst. Mid-weight aromatic esters in gardenia and orange blossom follow as skin temperature rises. Finally, heavy sesquiterpenes and complex resins in patchouli, beeswax, and caramel remain bound to skin lipids, evaporating slowly to maintain a warm, continuous fragrance sillage for hours.</p>`,
    "faqs": `<h3>What is Carlotta Scandal Eau de Toilette for Women?</h3>
<p>Carlotta Scandal is a 100ml Eau de Toilette spray designed for women, featuring a floral oriental gourmand fragrance that harmoniously blends citrus, white florals, natural honey, caramel, and patchouli.</p>

<h3>What is the volume of the perfume bottle?</h3>
<p>The product comes in a full-sized 100ml (3.4 fl oz) glass spray bottle, providing ample volume for months of daily application.</p>

<h3>Is this fragrance suitable for daily wear or evening occasions?</h3>
<p>Its balanced formula makes it exceptionally versatile. The fresh citrus opening works wonderfully for daytime office use, while the warm honey-caramel base shines during evening gatherings and special events.</p>

<h3>What are the top notes of Carlotta Scandal?</h3>
<p>The top notes feature an invigorating blend of Blood Orange and Mandarin Orange, delivering an uplifting and vibrant citrus opening.</p>

<h3>What are the heart notes of the perfume?</h3>
<p>The heart reveals a romantic bouquet of Gardenia, Orange Blossom, Jasmine, and juicy Peach, infused with sweet Natural Honey.</p>

<h3>What base notes ensure the longevity of this scent?</h3>
<p>The base is grounded in Beeswax, Caramel, Patchouli, and Licorice, creating a warm, sensual foundation that anchors the fragrance for hours.</p>

<h3>How long does Carlotta Scandal last on skin and clothes?</h3>
<p>It typically lasts between 6 to 8 hours on skin and can remain detectable for over 24 hours when misted onto fabrics and clothing.</p>

<h3>Is the perfume safe for sensitive skin types?</h3>
<p>Carlotta Scandal is formulated with cosmetic-grade, safety-tested aromatic ingredients. If you have hypersensitive skin, perform a patch test on your inner elbow before full application.</p>

<h3>Where are the best pulse points to apply perfume?</h3>
<p>Spray the fragrance onto warm pulse points where blood vessels are close to the surface, such as wrists, sides of the neck, behind ears, and inside elbows.</p>

<h3>Should I rub my wrists together after spraying?</h3>
<p>No, you should never rub your wrists together after spraying perfume. Rubbing generates heat that breaks down top-note molecules, altering the intended scent evolution.</p>

<h3>Is Carlotta Scandal a liquid spray or an oil roll-on?</h3>
<p>It is a liquid spray with an Eau de Toilette concentration, equipped with a fine mist atomizer for smooth, even distribution over skin and garments.</p>

<h3>Which fragrance family does Carlotta Scandal belong to?</h3>
<p>It belongs to the Floral Oriental Gourmand fragrance family, renowned for combining rich florals with sweet, mouth-watering accords like honey and caramel.</p>

<h3>Will the perfume spray stain white clothing?</h3>
<p>When sprayed from a standard distance of 15-20 cm, the clear liquid mist evaporates without leaving residue. Avoid spraying at point-blank range on delicate silk fabrics.</p>

<h3>How should I store my Carlotta Scandal bottle?</h3>
<p>Keep the bottle in a cool, dry place away from direct sunlight, moisture, and extreme heat sources to maintain the freshness of its essential oils.</p>

<h3>Is Carlotta Scandal suitable as a gift item?</h3>
<p>Yes, its beautifully designed bottle and attractive packaging make Carlotta Scandal an ideal gift for birthdays, anniversaries, and holidays.</p>

<h3>What is the difference between Eau de Toilette (EDT) and Eau de Parfum (EDP)?</h3>
<p>Eau de Toilette contains a 5% to 15% fragrance oil concentration, making it lighter and ideal for daily refreshing wear, while Eau de Parfum features a higher concentration.</p>

<h3>Can I spray Carlotta Scandal directly onto my hair?</h3>
<p>Direct spraying on hair root areas is discouraged due to alcohol drying effects. Instead, spray a mist into the air and step through it to lightly scent your hair.</p>

<h3>Is this perfume safe to use during pregnancy?</h3>
<p>Topical perfume sprays are generally considered safe during pregnancy. However, due to heightened sensitivity to smells during pregnancy, test a small amount first.</p>

<h3>What makes buying Carlotta Scandal from Ekleel Abha Pharmacy special?</h3>
<p>Ekleel Abha guarantees 100% authentic products, strict quality controls, and fast delivery across Saudi Arabia for a seamless shopping experience.</p>

<h3>Does the scent change over time after application?</h3>
<p>Yes, the fragrance unfolds in three stages: starting with bright citrus, moving into honeyed white florals, and settling into a warm patchouli-caramel base.</p>

<h3>Is Carlotta Scandal better for summer or winter?</h3>
<p>Its versatile formulation makes it suitable for all seasons. The citrus and floral notes bloom beautifully in warm weather, while honey and patchouli provide cozy warmth in winter.</p>

<h3>Where is Carlotta Scandal manufactured?</h3>
<p>The perfume is manufactured in the PRC under strict international fragrance and cosmetic production standards.</p>

<h3>Is the product dermatologically compliant and registered?</h3>
<p>Yes, Carlotta Scandal is produced using approved cosmetic ingredients compliant with standard safety regulations for personal fragrances.</p>

<h3>Are the honey and beeswax notes natural or synthetic?</h3>
<p>The honey and beeswax accords are expertly crafted cruelty-free synthetic olfactory notes that perfectly mimic natural scents without harming animals.</p>

<h3>How can I purchase authentic Carlotta Scandal online?</h3>
<p>You can easily purchase authentic Carlotta Scandal Eau de Toilette 100ml directly from the Ekleel Abha online pharmacy store with nationwide shipping in KSA.</p>`,
    "tags": ["carlotta", "scandal", "women_perfume", "fragrance_spray", "ekleel_abha", "eau_de_toilette"]
  },
  "schema": {
    "brand": "Carlotta",
    "category": "Perfumes / Women's Fragrances",
    "availability": "InStock"
  },
  "image_seo": {
    "image_filename": "carlotta-scandal-eau-de-toilette-100ml.webp",
    "alt": "Carlotta Scandal Eau de Toilette Spray for Women 100ml",
    "title": "Carlotta Scandal Eau de Toilette Spray for Women 100ml"
  }
};

// Create target directories
const targetDirs = [
  path.join(__dirname, 'temp', 'generated_products'),
  path.join(__dirname, '..', 'temp', 'generated_products')
];

targetDirs.forEach(dir => {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
  const filePath = path.join(dir, '1676.json');
  fs.writeFileSync(filePath, JSON.stringify(productData, null, 2), 'utf8');
  console.log(`Saved product 1676 JSON to: ${filePath}`);
});

