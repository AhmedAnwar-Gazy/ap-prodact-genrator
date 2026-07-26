const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const productData = {
  "product_id": "1675",
  "sku": "EK-1675",
  "gtin": "6936711831876",
  "category": "العطور والتجميل / عطور نسائية",
  "brand": "Carlotta",
  "ar": {
    "title": "عطر ماي دير للنساء من كارلوتا، او دي تواليت بسعة 100 مل",
    "meta_title": "عطر ماي دير للنساء من كارلوتا او دي تواليت 100 مل | صيدلية إكليل أبها",
    "meta_description": "اشتري عطر ماي دير للنساء من كارلوتا (Carlotta My Dear) سعة 100 مل او دي تواليت. عطر زهري عنبري أنيق يمنحك حضوراً ساحراً وانتعاشاً يدوم طويلاً. تسوقي الآن من إكليل أبها.",
    "description": `<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>عطر ماي دير (My Dear) من كارلوتا (Carlotta) للنساء</strong> بسعة 100 مل تركيبة عطرية ساحرة تجمع بين الأناقة الكلاسيكية واللمسات العصرية المنعشة. تم تصميم هذا العطر بنمط أو دي تواليت (Eau de Toilette) ليكون الخيار المثالي للمرأة الباحثة عن إطلالة مفعمة بالأنوثة والجاذبية في مختلف الأوقات. يفتتح العطر بنفحات حمضية منعشة توقظ الحواس، ثم يتدرج بسلاسة نحو قلب زهري فاخر غني بأجود أنواع الورود والياسمين، ليستقر أخيراً على قاعدة دافئة من الباتشولي وأخشاب الورد التي تمنح العطر ثباتاً وعمقاً لا يُنسى.</p>
<p>يتميز عطر كارلوتا ماي دير بكونه مستوحى من خطوط العطور العالمية الشهيرة (مثل ميس ديور)، حيث يقدم تجربة عطرية فاخرة وبجودة عالية تضاهي العطور الفخمة، مع الحفاظ على ملاءمته للاستخدام اليومي والمناسبات الخاصة. تأتي العبوة بحجم 100 مل وبزجاجة أنيقة تعكس الرقة والرقي، مما يجعله خياراً رائعاً للإهداء أو لإضافته إلى مجموعتك العطرية الشخصية للتمتع برائحة فواحة تحيطك بالدفء والبهجة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>توليفة عطرية أنثوية متناغمة:</strong> يمزج ببراعة بين الانتعاش الحمضي في البداية والعمق الزهري والخشبي في القاعدة ليعزز جاذبيتك وثقتك بالنفس.</li>
  <li><strong>ثبات وانتشار ممتازين:</strong> تم تطوير تركيبة أو دي تواليت بعناية لتدوم على البشرة والملابس لعدة ساعات مع انتشار عطري متوازن وغير مزعج.</li>
  <li><strong>ملاءمة لجميع المناسبات:</strong> عطر متعدد الاستخدامات يناسب أوقات العمل اليومية، اللقاءات الصباحية، والسهريات الرومانسية الخفيفة.</li>
  <li><strong>تصميم زجاجة راقي:</strong> تأتي العبوة في زجاجة عصرية جميلة تعكس أنوثة المنتج وتضفي لمسة من الفخامة على منصة التجميل الخاصة بك.</li>
  <li><strong>بديل ممتاز للعطور العالمية:</strong> يمنحك تجربة عطرية فاخرة مشابهة للروائح العالمية الشهيرة بقيمة ممتازة وجودة ثابته.</li>
  <li><strong>آمن ولطيف على البشرة:</strong> مصنع بمكونات عطرية نقية خاضعة لمعايير السلامة والجودة لتجنب تهيج البشرة عند الاستخدام المباشر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الرش على نقاط النبض:</strong> قمي برش العطر من مسافة 15-20 سم على مناطق النبض مثل معصمي اليدين، جانبي الرقبة، خلف الأذنين، ودواخل الكوعين حيث تولد هذه المناطق حرارة تساعد على انتشار الرائحة.</li>
  <li><strong>تجنب فرك العطر:</strong> بعد الرش على المعصمين، تجنبي فركهما معاً لأن ذلك يفكك الجزيئات العطرية العليا ويقلل من فترة ثبات العطر.</li>
  <li><strong>الرش على الملابس والشعر:</strong> للحصول على ثبات أطول، يمكن رش رذاذ خفيف من العطر على الملابس القطنية أو رش السحابة العطرية في الهواء المرور من خلالها.</li>
  <li><strong>الاستخدام بعد الاستحمام:</strong> يُفضل تطبيق العطر مباشرة بعد الاستحمام وترطيب البشرة بمرطب غير معطر، حيث تمتص البشرة الرطبة العطر بشكل أفضل وتزيد من مدة بقائه.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<p>تتألف البنية العطرية لعطر كارلوتا ماي دير من ثلاث طبقات عطرية متناغمة تضمن تحولاً سلسلاً وتجربة شذية فريدة:</p>
<ul>
  <li><strong>المكونات العليا (Top Notes):</strong> مزيج منعش ومشرق من البرتقال الدموي، البرتقال الحلو، برغموت كالابريا، الليمون، اليوسفي، مع لمسة حارة خفيفة من الفلفل الوردي لتنشيط الحواس.</li>
  <li><strong>المكونات الوسطى / قلب العطر (Heart Notes):</strong> باقة زهرية مفعمة بالأنوثة تتكون من ورد جراس الفاخر (Grasse Rose)، الورد الدمشقي، وأوراق الياسمين الناعمة التي تمنح العطر طابعاً رومانسياً أخاذاً.</li>
  <li><strong>المكونات القاعدية (Base Notes):</strong> قاعدة دافئة وغنية تثبت العطر وتمنحه العمق، تتألف من الباتشولي النقي وأخشاب الورد (Palisander Rosewood) التي تضفي لمسة شرقية خشبية ساحرة.</li>
</ul>

<h2>تحذيرات وااحتياطات</h2>
<ul>
  <li>المنتج مخصص للاستخدام الخارجي فقط؛ تجنبي ملامسة العطر للعينين أو الأغشية المخاطية.</li>
  <li>يُحظر رش العطر على البشرة الملتهبة، المتخرشة، أو الجروح المفتوحة لتجنب حدوث تهيج أو حرقان.</li>
  <li>يُحفظ العطر بعيداً عن مصادر الحرارة المباشرة، اللهب، وأشعة الشمس الساطعة لمنع تغير التركيبة العطرية أو اللون.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال لضمان السلامة ومنع الابتلاع أو الرش العرضي.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<p>هذا العطر صُمم خصيصاً للمرأة العصرية الشغوفة بالعطور الزهرية الفاخرة والتي تبحث عن رائحة أنثوية مفعمة بالحيوية والنعومة. يناسب الفتيات والنساء من مختلف الأعمار، سواء كعطر روتيني يومي للجامعة والعمل أو كخيار أنيق للمناسبات واللقاءات الاجتماعية.</p>`,
    "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>Carlotta (كارلوتا)</td></tr>
  <tr><th>الفئة</th><td>العطور والتجميل / عطور نسائية</td></tr>
  <tr><th>نوع المنتج</th><td>او دي تواليت (Eau de Toilette - EDT)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>مناسب لجميع أنواع البشرة</td></tr>
  <tr><th>المظهر النهائي</th><td>لمسة عطرية زهري عنبري أنيقة</td></tr>
  <tr><th>الملمس</th><td>سائل رذاذ عطري (Spray)</td></tr>
  <tr><th>العطر</th><td>زهري - عنبري - حمضي منعش</td></tr>
  <tr><th>المكونات النشطة</th><td>برتقال دمي، ورد جراس، ياسمين، باتشولي، خشب الورد</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين</td></tr>
  <tr><th>الشركة المصنعة</th><td>Zuofun Cosmetics / Carlotta Perfumes</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين (النساء)</td></tr>
</tbody>
</table>`,
    "knowledge_base": `<h2>الدليل المعرفي لثقافة العطور والعناية بالرائحة الشخصية</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج عطر ماي دير من كارلوتا مشكلة عدم ثبات الرائحة الشخصية والبحث عن عطر أنثوي راقٍ يمنح شعوراً بالنظافة والجاذبية طوال اليوم دون الحاجة لإنفاق مبالغ طائلة على العطور العالمية الباهظة. كما يقضي على الروائح غير المستحبة التي قد تنتج عن التعب اليومي أو العوامل الجوية، مما يعزز حضور المرأة وثقتها بنفسها في مختلف الأوساط.</p>

<h3>لماذا تحدث مشكلة تلاشي العطر بسرعة؟</h3>
<p>يعود تلاشي الرائحة العطرية بسرعة إلى عدة عوامل فيزيولوجية وبيئية؛ أبرزها جفاف البشرة، حيث تفتقر البشرة الجافة إلى الزيوت الطبيعية التي تحتفظ بجزيئات العطر وتمنع تبخرها السريع. كما أن التغيرات في مستوى حموضة البشرة (pH) وارتفاع درجات الحرارة والرطوبة يؤديان إلى تسريع تبخر المكونات العليا الخفيفة. بالإضافة إلى ذلك، يخطئ الكثيرون برش العطر على الملابس الصناعية أو فرك المعصمين مما يؤدي إلى تكسير الروابط الكيميائية للجزيئات العطرية وتلاشيها بوقت قياسي.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>ترطيب البشرة قبل رش العطر:</strong> استخدمي لوشن غير معطر أو فازلين خفيف على نقاط النبض قبل رش العطر لتشكيل قاعدة زيتية تحتفظ بالرائحة لفترة أطول.<br>2. <strong>تطبيق العطر طبقات (Perfume Layering):</strong> استخدمي شاور جل ومرطب برائحة زهري حمضية متناغمة مع العطر لتعزيز الثبات والعمق.<br>3. <strong>التخزين الصحيح للعطور:</strong> احتفظي بزجاجة العطر في مكان بارد ومظلم بعيداً عن رطوبة الحمام وأشعة الشمس للحفاظ على ثبات التركيبة.<br>4. <strong>الرش على الأنسجة الطبيعية:</strong> يثبت العطر لفترة أطول عند رشه على الملابس المصنوعة من القطن والصوف مقارنة بالأنسجة البوليسترية.</p>

<h3>خرافات شائعة حول العطور</h3>
<p><strong>خرافة:</strong> "فرك المعصمين معاً بعد رش العطر يساعد في تثبيت الرائحة وتنشيطها."<br><strong>الحقيقة:</strong> الاحتكاك الناتج عن فرك المعصمين يولد حرارة تتسبب في تدمير الجزيئات العطرية العليا الخفيفة (مثل الحمضيات) ويغير من التسلسل الطبيعي لتفتح نوتات العطر، مما يقلل من ثباته وجودته.</p>

<h3>التفسير العلمي لآلية العمل وتطور النوتات العطرية</h3>
<p>تعتمد آلية عمل العطور على معدل تطاير (Volatility Rate) الجزيئات العطرية المختلفة. يتكون عطر كارلوتا ماي دير من هرم عطري مدروس؛ تتبخر المكونات العليا ذات الوزن الجزيئي الخفيف (مثل المكونات الحمضية والفلفل الوردي) خلال أول 15 إلى 30 دقيقة لتمنحك الانطباع الأول المنعش. تليها المكونات الوسطى (ورد جراس والياسمين) ذات الوزن الجزيئي المتوسط والتي تظهر بعد نصف ساعة وتستمر لعدة ساعات ليشكل قلب العطر. أخيراً، تتبقى المكونات القاعدية ذات الجزيئات الثقيلة والمعقدة (الباتشولي وأخشاب الورد) التي تلتصق بالبشرة وتتبخر ببطء شديد على مدار اليوم، مما يضمن استمرار عبير العطر وثباته العميق.</p>`,
    "faqs": `<h3>ما هو عطر ماي دير من كارلوتا وما هي نوتاته الرئيسية؟</h3>
<p>عطر ماي دير من كارلوتا هو عطر نسائي أنيق بتركيز او دي تواليت وسعة 100 مل. يتكون هرمه العطري من افتتاحية حمضية منعشة تضم البرتقال الدموي والبرغموت واليوسفي، وقلب زهر غني بورد جراس والورد الدمشقي والياسمين، وقاعدة دافئة وثابتة من الباتشولي وأخشاب الورد.</p>

<h3>ما الفرق بين تركيز او دي تواليت (EDT) واو دي بارفان (EDP)؟</h3>
<p>يتميز او دي تواليت بتركيز زيوت عطرية يتراوح بين 5% إلى 15%، مما يجعله خفيفاً، منعشاً، ومثالي الاستخدام اليومي والأجواء الصباحية. بينما يحتوي او دي بارفان على تركيز أعلى يتراوح بين 15% إلى 20% ليكون أكثر كثافة وملاءمة للسهرات الطويلة.</p>

<h3>كم تبلغ مدة ثبات عطر كارلوتا ماي دير على البشرة والملابس؟</h3>
<p>يدوم عطر ماي دير على البشرة عادةً من 4 إلى 6 ساعات، بينما يمكن أن يستمر ثباته على الملابس والأقمشة لمدة تتجاوز 12 ساعة، وذلك بفضل وجود قاعدة الباتشولي وأخشاب الورد الثابتة التي تحتفظ بالرائحة.</p>

<h3>هل يناسب عطر ماي دير الاستخدام اليومي وأوقات العمل؟</h3>
<p>نعم، العطر مصمم ببراعة ليكون متوازناً وغير مزعج، حيث تمنحه الافتتاحية الحمضية انتعاشاً صباحياً رائعاً يجعله مناسباً جداً للذهاب إلى العمل، الجامعة، أو اللقاءات اليومية الخفيفة.</p>

<h3>هل يعتبر عطر ماي دير بديلاً لعطور عالمية شهيرة؟</h3>
<p>نعم، يُصنف عطر كارلوتا ماي دير كبديل عطري مميز (Dupe) مستوحى من خطوط العطور الزهرية الفاخرة مثل عطر ميس ديور الشهير، حيث يقدم تجربة عطرية قريبة جداً وبجودة عالية وبسعر اقتصادي مناسب.</p>

<h3>ما هي أفضل طريقة لتطبيق العطر لضمان أطول فترة ثبات؟</h3>
<p>أفضل طريقة هي رش العطر على مناطق النبض في الجسم مثل المعصمين، الرقبة، وخلف الأذنين بعد ترطيب البشرة بمرطب غير معطر، مع مراعاة عدم فرك المعصمين بعد الرش نهائياً.</p>

<h3>هل العطر مناسب لفصل الصيف أم الشتاء؟</h3>
<p>بفضل التوازن الفريد بين الحمضيات المنعشة والزهور والباتشولي الدافيء، يعتبر العطر مناسباً للاستخدام في جميع فصول السنة، وخاصة في فصلي الربيع والصيف بفضل طابعه الزهري المشرق.</p>

<h3>هل يسبب عطر كارلوتا ماي دير بقعاً على الملابس البيضاء؟</h3>
<p>تركيبة العطر شفافة ومصممة بعناية عالية لتجنب ترك أي تصبغات أو بقع على الأقمشة. ومع ذلك، يُنصح دائماً برش العطر من مسافة 20 سم للحصول على انتشار متجانس.</p>

<h3>ما هو حجم العبوة وهل هي مناسبة للسفر؟</h3>
<p>تأتي العبوة بحجم قياسي يبلغ 100 مل، وهي سعة ممتازة للاستخدام اليومي المستمر وتدوم لفترة طويلة. بالنسبة للشحن الجوي في الحقائب اليدوية قد تتطلب أحجاماً أصغر، ولكنها مثالية لحقائب السفر الكبيرة.</p>

<h3>هل يسبب هذا العطر أي تحسس للبشرة؟</h3>
<p>العطر مصنع وفق معايير الجودة ومناسب لمعظم أنواع البشرة. ومع ذلك، إذا كانت بشرتك شديدة الحساسية للعطور، يُفضل رش العطر على الملابس بدلاً من تطبيقه المباشر على الجلد.</p>

<h3>ما هي المكونات التي تمنح العطر ثباته في القاعدة؟</h3>
<p>يعود الثبات العالي لقاعدة العطر إلى جزيئات الباتشولي النقي وأخشاب الورد (Palisander Rosewood)، وهي مكونات خشبية ثقيلة تتبخر ببطء شديد وتعمل كمثبت طبيعي للرائحة.</p>

<h3>كيف يمكنني التمييز بين المنتج الأصلي والمقلد؟</h3>
<p>تأتي العبوة الأصلية من كارلوتا بتغليف محكم وعليها رمز الباركود الدولي (GTIN: 6936711831876)، مع طباعة واضحة لاسم العلامة التجارية وتفاصيل المنتج على العلبة والزجاجة.</p>

<h3>هل العطر مناسب لجميع الفئات العمرية من النساء؟</h3>
<p>نعم، يتسم العطر بطابع أنثوي عالمي يناسب الشابات والسيدات من مختلف الأعمار، حيث يجمع بين الحيوية والشبابية في بدايته والأناقة والوقار في نهايته.</p>

<h3>هل يمكن رش عطر ماي دير على الشعر؟</h3>
<p>يمكن رش العطر على الفرشاة ثم تمشيط الشعر بها لتوزيع الرائحة بلطف، ولكن يُفضل تجنب الرش المباشر والمركز على فروة الرأس لتجنب جفاف الشعر بسبب الكحول العطري.</p>

<h3>كيف يجب تخزين زجاجة العطر للحفاظ على جودتها؟</h3>
<p>يجب حفظ العطر في مكان جاف وبارد بعيداً عن الضوء المباشر ورطوبة الحمام، ويفضل إبقاؤه داخل علبته الكرتونية الأصلية أو في خزانة مغلقة عند عدم الاستخدام.</p>

<h3>هل يختلف طعم أو رائحة العطر من شخص لآخر؟</h3>
<p>نعم، قد تتفاعل المكونات العطرية بشكل طفيف مع درجة حموضة الجلد (pH) والزيوت الطبيعية ونوعية الغذاء لكل شخص، مما يمنح العطر بصمة عطرية فريدة خاصة بكل امرأة.</p>

<h3>هل يمكن استخدام العطر للمناسبات المسائية؟</h3>
<p>بالتأكيد، على الرغم من كونه او دي تواليت، إلا أن وجود الورد والباتشولي يمنحه حضوراً دافئاً وجذاباً يجعله مناسباً جداً للسهرات واللقاءات المسائية غير الرسمية.</p>

<h3>ما هي الشركة المصنعة لعطور كارلوتا؟</h3>
<p>تُصنع عطور كارلوتا بواسطة شركة Zuofun Cosmetics المتخصصة في إنتاج العطور ومستحضرات التجميل ذات المعايير العالمية والتصاميم الراقية.</p>

<h3>هل تحتوي زجاجة العطر على بخاخ (Spray)؟</h3>
<p>نعم، العبوة مزودة بمرش رذاذ عالي الدقة (Atomizer Spray) يضمن توزيع العطر بشكل متجانس وناعم على البشرة والملابس بضغطة واحدة.</p>

<h3>ما الذي يبرز في رائحة العطر بعد مضي ساعتين من الرش؟</h3>
<p>بعد ساعتين من التطبيق، تتلاشى المكونات الحمضية وتتفتح قلب الرائحة المكونة من باقة الورد الجوري والياسمين مع ظهور تدريجي لنفحات الباتشولي الخشبية الدافئة.</p>

<h3>هل العطر مناسب كهدية؟</h3>
<p>نعم، يُعد عطر كارلوتا ماي دير خياراً رائعاً ومثالياً للهدايا في المناسبات والأعياد وأعياد الميلاد بفضل تصميمه الأنيق ورائحته الأنثوية المفضلة لدى الكثيرات.</p>

<h3>هل يتفاعل العطر مع حرارة الصيف بشكل سلب؟</h3>
<p>لا، الافتتاحية الحمضية المكونة من البرتقال والبرغموت تجعل العطر منعشاً للغاية في الحرارة دون أن يسبب شعوراً بالثقل أو الكتمة.</p>

<h3>كم عدد الرشات الموصى بها في المرة الواحدة؟</h3>
<p>يُوصى برش من 3 إلى 5 رشات وزعة على نقاط النبض والملابس للحصول على انتشار عطري مثالي ومتوازن يدوم لعدة ساعات.</p>

<h3>هل يمكن مزج هذا العطر مع عطور أخرى (Layering)؟</h3>
<p>نعم، يمتزج العطر بشكل ممتاز مع العطور التي تحتوي على نوتات الفانيليا أو المسك الأبيض لإضافة طابع أكثر دفئاً وحلاوة حسب رغبتك.</p>

<h3>لماذا تختار شراء هذا المنتج من صيدلية إكليل أبها؟</h3>
<p>صيدلية إكليل أبها تضمن لك الحصول على منتجات أصصلية 100% مباشرة من الموردين المعتمدين، مع توفير خدمة توصيل سريعة وحفظ آمن للمنتجات وضمان أعلى مستويات الجودة.</p>`,
    "tags": ["carlotta", "عطر_ماي_دير", "عطور_نسائية", "او_دي_تواليت", "كارلوتا", "إكليل_أبها"]
  },
  "en": {
    "title": "My Dear Perfume by Carlotta for Women, Eau de Toilette Single Pack - 100ml",
    "meta_title": "Carlotta My Dear Perfume for Women Eau de Toilette 100ml | Ekleel Abha",
    "meta_description": "Buy Carlotta My Dear Eau de Toilette for Women (100ml). Elegant amber floral perfume featuring vibrant citrus, Grasse rose, and warm patchouli. 100% authentic product at Ekleel Abha Pharmacy.",
    "description": `<h2>Product Overview</h2>
<p>The <strong>My Dear Perfume by Carlotta for Women (100ml Eau de Toilette)</strong> is a captivating fragrance created to embody feminine elegance, romance, and vibrant charm. Formulated as a sophisticated Eau de Toilette, it strikes the perfect balance between uplifting freshness and lasting warmth. The scent opens with a luminous burst of sunny citrus fruits and a touch of spicy pink pepper, gracefully transitioning into a lush floral heart of precious Grasse rose and jasmine, before settling onto a velvety base of patchouli and rich rosewood.</p>
<p>Inspired by iconic luxury scents (such as Miss Dior), Carlotta My Dear delivers a high-end olfactory experience at an accessible price point, making luxury everyday fragrance an attainable reality. Housed in a charming 100ml glass bottle that adorns any vanity, this scent creates an enchanting aura around the wearer, ensuring you leave a memorable impression wherever you go.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Harmonious Amber Floral Blend:</strong> Masterfully balances zesty citrus top notes with a romantic floral heart and deep woody base.</li>
  <li><strong>Long-Lasting Projection:</strong> Engineered to provide several hours of continuous, elegant sillage on skin and fabrics without feeling overpowering.</li>
  <li><strong>Versatile Daily Wear:</strong> Perfect for morning office hours, casual daytime outings, as well as romantic evening gatherings.</li>
  <li><strong>Elegant Bottle Presentation:</strong> Housed in a beautifully crafted 100ml bottle with a fine atomizing spray for effortless application.</li>
  <li><strong>Affordable Luxury Alternative:</strong> Offers a premium scent profile inspired by famous high-end designer fragrances at an excellent value.</li>
  <li><strong>Dermatologically Gentle:</strong> Crafted with high-purity fragrance oils tested for safety and skin tolerance.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Apply to Pulse Points:</strong> Spray from a distance of 6-8 inches (15-20 cm) onto warm pulse points such as your wrists, neck sides, behind ears, and inner elbows.</li>
  <li><strong>Avoid Rubbing Wrists:</strong> After spraying, allow the perfume to dry naturally. Rubbing your wrists together breaks down fragile top notes and reduces fragrance longevity.</li>
  <li><strong>Mist Clothing and Hairbrush:</strong> Lightly spray your cotton clothing or spritz onto a hairbrush before styling to create an extended scent trail.</li>
  <li><strong>Apply After Showering:</strong> For maximum longevity, apply immediately after showering and applying an unscented body lotion, as hydrated skin locks in perfume molecules far better.</li>
</ul>

<h2>Ingredients Overview</h2>
<p>Carlotta My Dear Eau de Toilette features a carefully structured scent pyramid built from top-quality fragrance accords:</p>
<ul>
  <li><strong>Top Notes:</strong> An invigorating cocktail of Blood Orange, Sweet Orange, Calabrian Bergamot, Lemon, Mandarin, enriched with a subtle spicy kiss of Pink Pepper.</li>
  <li><strong>Heart / Middle Notes:</strong> A deeply romantic floral core featuring exquisite Grasse Rose, Damask Rose, and delicate Jasmine leaves.</li>
  <li><strong>Base Notes:</strong> A warm, grounding foundation of pure Patchouli and Palisander Rosewood that fixes the fragrance and ensures lasting depth.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external use only; avoid direct contact with eyes, inner ears, and mucous membranes.</li>
  <li>Do not apply to broken, irritated, or freshly shaved skin to prevent burning sensations or redness.</li>
  <li>Store away from direct sunlight, extreme heat sources, and open flames to preserve scent integrity.</li>
  <li>Keep out of reach of children to avoid accidental ingestion or spraying into eyes.</li>
</ul>

<h2>Who Is This For?</h2>
<p>This fragrance is designed for modern women who love elegant, romantic floral scents with a fresh citrus sparkle. It caters to women of all ages seeking a signature daily perfume for work, university, social gatherings, or romantic dates.</p>`,
    "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Carlotta</td></tr>
  <tr><th>Category</th><td>Perfumes & Cosmetics / Women's Perfumes</td></tr>
  <tr><th>Product Type</th><td>Eau de Toilette (EDT)</td></tr>
  <tr><th>Volume/Weight</th><td>100 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Suitable for all skin types</td></tr>
  <tr><th>Finish</th><td>Elegant Amber Floral Scent</td></tr>
  <tr><th>Texture</th><td>Liquid Atomizer Spray</td></tr>
  <tr><th>Fragrance</th><td>Amber Floral / Citrus Rose</td></tr>
  <tr><th>Active Ingredients</th><td>Blood Orange, Grasse Rose, Jasmine, Patchouli, Rosewood</td></tr>
  <tr><th>Country of Origin</th><td>China</td></tr>
  <tr><th>Manufacturer</th><td>Zuofun Cosmetics / Carlotta Perfumes</td></tr>
  <tr><th>Age Group</th><td>Adults (Women)</td></tr>
</tbody>
</table>`,
    "knowledge_base": `<h2>Clinical & Olfactory Insights on Fragrance Wear & Longevity</h2>

<h3>What problem does this solve?</h3>
<p>Carlotta My Dear Eau de Toilette solves the common challenge of finding a charming, romantic, and long-lasting feminine fragrance that fits daily budgets without compromising on quality or elegance. It neutralizes unwanted body odors caused by daily hustle and environmental exposure, surrounding the user with a fresh, captivating scent shield that boosts confidence and personal aura.</p>

<h3>Why does fragrance fade quickly on some individuals?</h3>
<p>Rapid fragrance evaporation is primarily caused by dry skin conditions, high body heat, and environmental factors. Dry skin lacks natural lipid oils needed to bind volatile fragrance molecules, causing them to evaporate into the air rapidly. Furthermore, skin pH imbalance, sweating, and incorrect application methods—such as rubbing wrists together or spraying onto synthetic fabrics—accelerate the breakdown of delicate aromatic bonds.</p>

<h3>Prevention & Maintenance Tips</h3>
<p>1. <strong>Pre-Moisturize Pulse Points:</strong> Apply a thin layer of unscented body moisturizer or petroleum jelly to pulse points prior to spraying fragrance to create an anchor for scent molecules.<br>2. <strong>Practice Scent Layering:</strong> Combine with matching floral or citrus shower gels and body lotions to build a multi-layered scent profile.<br>3. <strong>Proper Storage:</strong> Keep perfume bottles in a cool, dark place away from bathroom humidity and sunlight to maintain chemical stability.<br>4. <strong>Apply to Natural Fabrics:</strong> Spraying perfume on natural fibers like cotton or wool retains fragrance much longer than synthetic polyester.</p>

<h3>Common Fragrance Myths</h3>
<p><strong>Myth:</strong> "Rubbing your wrists together right after spraying helps set the perfume faster."<br><strong>Fact:</strong> Friction generated by rubbing wrists increases surface heat, which destroys fragile top notes (such as citrus and pink pepper) and alters the fragrance sequence, significantly reducing performance and longevity.</p>

<h3>Scientific Explanation of Fragrance Volatility & Pyramid Evolution</h3>
<p>The performance of a fragrance relies on the molecular weight and evaporation rates (volatility) of its constituent aromatic compounds. Carlotta My Dear is constructed around a classic three-tier scent pyramid. The light top notes (citrus oils and pink pepper) have low molecular weight and evaporate within the first 15-30 minutes, providing an instant burst of uplifting freshness. As top notes dissipate, the medium-weight heart notes (Grasse rose and jasmine) unfurl over the next 2 to 4 hours, establishing the romantic floral character. Finally, heavy, complex base molecules (patchouli and palisander rosewood) anchor to skin lipids, evaporating very slowly over 6+ hours to deliver a warm, memorable trail.</p>`,
    "faqs": `<h3>What is Carlotta My Dear Perfume and what are its key fragrance notes?</h3>
<p>Carlotta My Dear is an elegant Eau de Toilette for women in a 100ml spray bottle. Its scent pyramid features top notes of blood orange, bergamot, and pink pepper; heart notes of Grasse rose and jasmine; and a warm base of patchouli and palisander rosewood.</p>

<h3>What is the difference between Eau de Toilette (EDT) and Eau de Parfum (EDP)?</h3>
<p>Eau de Toilette typically contains a 5% to 15% concentration of aromatic oils, giving it a lighter, fresh profile perfect for daily daytime wear. Eau de Parfum contains 15% to 20% oil concentration, offering a denser scent suitable for evening events.</p>

<h3>How long does Carlotta My Dear EDT last on the skin and clothing?</h3>
<p>On hydrated skin, Carlotta My Dear typically lasts between 4 to 6 hours. On fabrics and clothing, the warm patchouli base notes can remain noticeable for over 12 hours.</p>

<h3>Is this fragrance suitable for daily office and university wear?</h3>
<p>Yes, the balanced citrus-floral composition is fresh, uplifting, and unobtrusive, making it ideal for daily work, school, and daytime activities.</p>

<h3>Is Carlotta My Dear a dupe for a high-end designer perfume?</h3>
<p>Yes, Carlotta My Dear is inspired by famous luxury amber floral fragrances such as Miss Dior, offering a remarkably similar scent profile and elegant vibe at an accessible price.</p>

<h3>What is the best way to apply perfume for maximum longevity?</h3>
<p>Apply to warm pulse points (wrists, neck, behind ears) after moisturizing your skin with an unscented lotion. Never rub your wrists together after spraying.</p>

<h3>Is Carlotta My Dear best suited for summer or winter?</h3>
<p>Thanks to its harmonious blend of bright citrus top notes and warm woody base notes, it is versatile enough for year-round wear, excelling particularly in spring and summer.</p>

<h3>Will this perfume stain white clothes or light fabrics?</h3>
<p>The fragrance liquid is clear and formulated to avoid staining fabrics. For best results, spray from a distance of 15-20 cm to ensure fine, even atomization.</p>

<h3>What is the volume of the bottle and is it travel-friendly?</h3>
<p>The bottle contains 100ml (3.4 fl. oz.), providing a generous volume for daily use. While standard carry-on liquid limits apply for flights, it fits easily into main luggage.</p>

<h3>Is this perfume safe for sensitive skin?</h3>
<p>The perfume is formulated with high-quality ingredients suitable for most skin types. If you have extreme skin sensitivities, spraying onto clothing is recommended.</p>

<h3>Which ingredients provide the lingering base notes in this perfume?</h3>
<p>The long-lasting foundation is created by pure Patchouli and Palisander Rosewood, which act as natural fixatives that evaporate slowly on skin.</p>

<h3>How can I verify the authenticity of Carlotta My Dear?</h3>
<p>Authentic Carlotta products feature clear brand packaging, sharp printing, and a valid international barcode (GTIN: 6936711831876) printed on the outer box.</p>

<h3>Is this scent suitable for women of all age groups?</h3>
<p>Yes, its romantic floral character combined with fresh citrus appeal makes it universally flattering for young women, professionals, and mature ladies alike.</p>

<h3>Can I spray this perfume directly on my hair?</h3>
<p>It is better to spritz perfume onto a hairbrush and run it through your hair. Direct spraying on hair can cause dryness due to the alcohol content in fragrance sprays.</p>

<h3>How should I store my perfume bottle to preserve its quality?</h3>
<p>Store your perfume bottle in a cool, dry place away from direct sunlight, heat vents, and bathroom humidity to prevent degradation of essential oils.</p>

<h3>Why does fragrance smell slightly different on different people?</h3>
<p>Perfume interacts with individual skin chemistry, natural body oils, pH levels, and temperature, creating a subtly unique scent signature for every individual.</p>

<h3>Can Carlotta My Dear be worn for evening events and dates?</h3>
<p>Absolutely. While fresh enough for daytime, the romantic rose heart and warm patchouli base give it an alluring depth perfect for evening dates and dinners.</p>

<h3>Who manufactures Carlotta perfumes?</h3>
<p>Carlotta perfumes are manufactured by Zuofun Cosmetics, a reputable fragrance house specializing in high-quality feminine perfumes and cosmetics.</p>

<h3>Does the bottle come with a spray atomizer?</h3>
<p>Yes, the 100ml glass bottle features a high-precision fine spray nozzle (atomizer) for smooth, even distribution with every spritz.</p>

<h3>What scent notes become most prominent after 2 hours of wearing?</h3>
<p>After 2 hours, the initial citrus burst settles, allowing the lush Grasse rose and jasmine heart to blossom fully alongside soft woody undertones of patchouli.</p>

<h3>Is Carlotta My Dear a good choice for a gift?</h3>
<p>Yes, with its attractive packaging, classic bottle design, and universally loved floral scent profile, it makes a thoughtful and elegant gift for birthdays and special occasions.</p>

<h3>Does summer heat affect the performance of this fragrance?</h3>
<p>Summer heat enhances the projection of citrus and rose notes, keeping you feeling fresh and scented without feeling heavy or oppressive.</p>

<h3>How many spritzes should I apply per use?</h3>
<p>3 to 5 spritzes distributed across pulse points and clothing provide an optimal scent cloud that lasts throughout the day.</p>

<h3>Can I layer this perfume with other scents?</h3>
<p>Yes, it layers exceptionally well with vanilla or white musk perfumes if you wish to add extra sweetness or warmth to your fragrance signature.</p>

<h3>Why buy Carlotta My Dear from Ekleel Abha Pharmacy?</h3>
<p>Ekleel Abha Pharmacy guarantees 100% authentic products sourced directly from authorized distributors, with fast shipping across Saudi Arabia and reliable customer care.</p>`
  },
  "schema": {
    "brand": "Carlotta",
    "category": "Perfumes & Cosmetics / Women's Perfumes",
    "availability": "InStock"
  },
  "image_seo": {
    "image_filename": "carlotta-my-dear-perfume-women-edt-100ml.webp",
    "alt": "Carlotta My Dear Perfume for Women Eau de Toilette 100ml",
    "title": "Carlotta My Dear Perfume for Women Eau de Toilette 100ml"
  }
};

const dir1 = path.join(__dirname, 'temp/generated_products');
const dir2 = path.join(__dirname, '../temp/generated_products');

[dir1, dir2].forEach(dir => {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
  const filePath = path.join(dir, '1675.json');
  fs.writeFileSync(filePath, JSON.stringify(productData, null, 2), 'utf8');
  console.log(`Saved JSON to ${filePath}`);
});

console.log("JSON generated successfully.");
