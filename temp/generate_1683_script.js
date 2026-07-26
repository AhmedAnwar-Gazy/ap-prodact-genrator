const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const productId = "1683";
const gtin = "8809511983077";
const sku = "EK-1683";

const productData = {
  "product_id": productId,
  "sku": sku,
  "gtin": gtin,
  "category": "العناية بالبشرة / أقنعة الوجه",
  "brand": "I'm Sorry For My Skin",
  "ar": {
    "title": "قناع الجيلي الموازن للحموضة pH 5.5 لإشراق وتفتيح البشرة من ايم سوري فور ماي سكن - 33 مل",
    "meta_title": "قناع الجيلي الموازن للحموضة pH 5.5 لتفتيح البشرة ايم سوري فور ماي سكن 33مل | إكليل أبها",
    "meta_description": "تسوقي قناع الجيلي الموازن للحموضة pH 5.5 لإشراق وتفتيح البشرة من ايم سوري فور ماي سكن بحجم 33 مل. تركيبة غنية بمستخلص الورد الدماكشي والبانثينول للنضارة الفورية لدى صيدلية إكليل أبها.",
    "description": `<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>قناع الجيلي الموازن للحموضة pH 5.5 لإشراق وتفتيح البشرة من ايم سوري فور ماي سكن (I'm Sorry For My Skin pH 5.5 Jelly Mask - Brightening)</strong> ابتكاراً كورية متطوراً موصى به من أطباء الجلدية لإعادة النضارة والحيوية الفورية للبشرة المجهدة والبهتة. يعاني الكثيرون من شحوب البشرة وفقدان البريق نتيجة التلوث البيئي، السهر، التعرض المستمر لأشعة الشمس، والضغوط اليومية. يأتي هذا القناع الفريد ليقدم حلاً علاجياً مكثفاً يجمع بين قوة التفتيح الطبيعي والعناية بالحاجز الحمضي الواقي للجلد برقم هيدروجيني متوازن تماماً عند pH 5.5.</p>
<p>يتميز هذا المنتج بتركيبته المبتكرة الغنية بـ 33 مل من الجوهر المكثف ذو القوام الجيلي (Jelly Essence)، والذي يمنح البشرة ترطيباً عميقاً يستمر لعدة أيام دون أن يتساقط أو يسبب إزعاجاً أثناء الاستخدام. ينغمس القناع الورقي المكون من ألياف الدقيقة النسيجية في مزيج فريد من المستخلصات النباتية الفعالة مثل الورد الدماكشي، بلسم الليمون، والبانثينول، مما يضمن تغلغل المكونات المغذية إلى أعمق طبقات البشرة وتفتيح لونها وإزالة مظاهر التعب والإرهاق بفعالية فائقة خلال 15 إلى 20 دقيقة فقط.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح البشرة واستعادة الإشراق:</strong> يعزز إشراقة الوجه الطبيعية ويقلل من مظاهر الشحوب والبهتان بفضل مستخلص الورد الدماكشي ومضادات الأكسدة.</li>
  <li><strong>موازنة الحموضة الطبيعية (pH 5.5):</strong> يحافظ على الغلاف الحمضي الطبيعي للبشرة، مما يحميها من البكتيريا المسببة للحبوب ويمنع الجفاف والتهيج.</li>
  <li><strong>ترطيب عميق طويل الأمد:</strong> يحتوي على 33 مل من جوهر الجيلي المكثف المزود بالتريحالوز وحمض الهيالورونيك لتثبيت الرطوبة داخل طبقات الجلد.</li>
  <li><strong>تهدئة البشرة المجهدة والمتعب:</strong> يلطف الاحمرار ويلطف الأنسجة الحساسة بفعل البانثينول (فيتامين B5) ومستخلصات الأعشاب المهدئة.</li>
  <li><strong>تحسين ملمس البشرة ومرونتها:</strong> يمنح الجلد ملمساً حريرياً ناعماً ويقلل من الخشونة ومظهر المسام الواسعة.</li>
  <li><strong>قناع نسيجي مريح وقوي الالتصاق:</strong> يتكيف بتناغم تام مع ملامح الوجه لضمان التوزيع المتساوي للجوهر دون انزلاق.</li>
  <li><strong>تركيبة آمنة وخالية من المكونات القاسية:</strong> خالية من البارابين والسلفات والألوان الصناعية الضارة، مما يجعله مناسباً للبشرة الأكثر حساسية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف والتجهيز):</strong> اغسلي وجهك جيداً باستخدام منظف لطيف مناسب لنوع بشرتك، ثم جففيه بلطف ووضعي التونر لتهيئة البشرة واستقبال الجوهر المغذي.</li>
  <li><strong>الخطوة الثانية (تطبيق القناع):</strong> افتحي العبوة واستخرجي القناع الورقي بحذر، ثم افرديه وضعي القناع بالتساوي على كامل الوجه مع محاذاة فتحات العينين والأنف والفم.</li>
  <li><strong>الخطوة الثالثة (الاسترخاء والتفعيل):</strong> اتركي القناع على وجهك لمدة 15 إلى 20 دقيقة للاسترخاء والسماح لجوهر الجيلي الكثيف بالتغلغل في عمق البشرة.</li>
  <li><strong>الخطوة الرابعة (التدليك والامتصاص):</strong> أزيلي القناع الورقي بلطف، ثم دلكي الجوهر المتبقي على الوجه والرقبة بحركات دائرية خفيفة وأطراف الأصابع حتى يتم امتصاصه بالكامل دون الحاجة لغسله بالماء.</li>
  <li><strong>الخطوة الخامسة (الاستفادة من الزوائد):</strong> يمكنك توزيع كمية الجيلي الكثيفة المتبقية داخل الكيس على اليدين، الكوعين، والرقبة للحصول على ترطيب وتفتيح شامل.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مستخلص الورد الدماكشي (Rosa Damascena Flower Extract):</strong> مكون طبيعي فاخر يعمل على تفتيح لون البشرة، توحيد لونها، ومنحها إشراقة وردية حيوية، بالإضافة إلى خصائصه المضادة للأكسدة.</li>
  <li><strong>مستخلص بلسم الليمون (Melissa Officinalis Leaf Extract):</strong> يساعد في تنقية البشرة، تهدئة التهابات الجلد، وموازنة إفراز الدهون والزيوت الطبيعية.</li>
  <li><strong>البانثينول (Pro-Vitamin B5):</strong> مادة مرطبة ومعالجة تخترق طبقات الجلد لتهدئة تهيج الأنسجة وتقوية حاجز الرطوبة الطبيعي.</li>
  <li><strong>التريحالوز والجليسرين (Trehalose & Glycerin):</strong> مركبات سكرية مرطبة تعمل كمصيدة للماء، حيث تجذب جزيئات الرطوبة وتحتفظ بها داخل الخلايا لمنع التجفاف.</li>
  <li><strong>مركب موازنة الحموضة (pH 5.5 Balancing Complex):</strong> تركيبة حمضية خفيفة تتماشى تماماً مع الرقم الهيدروجيني الطبيعي للبشرة لتعزيز ميكروبيوم الجلد النافع.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>المنتج مخصص للاستخدام الخارجي فقط على الوجه والجسم.</li>
  <li>تجنبي ملامسة الجوهر للعينين مباشرة؛ وفي حال حدوث ذلك، اغسلي العينين فوراً بماء فاتر نقي.</li>
  <li>لا يُستخدم القناع على الجروح المفتوحة، أو الجلد المصاب بحروق الشمس الشديدة، أو الأكزيما المتهيج.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال، وفي مكان بارد وجاف بعيداً عن الأشعة الشمسية المباشرة (يمكن حفظه في الثلاجة لانتعاش مضاعف).</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>أصحاب البشرة الباهتة والمجهدة التي فقدت نضارتها بسبب التلوث البيئي والسهر المستمر.</li>
  <li>الأفراد الذين يعانون من تفاوت لون البشرة وبقع التصبغ الخفيفة والراغبين في تفتيح طبيعي وآمن.</li>
  <li>جميع أنواع البشرة (الدهنية، الجافة، المختلطة، والحساسة) التي تحتاج إلى ترطيب مكثف وموازنة حموضة.</li>
  <li>السيدات والرجال الباحثون عن عناية سريعة ونتائج إشراق فورية قبل المناسبات والتجمعات.</li>
</ul>`,
    "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>I'm Sorry For My Skin (ايم سوري فور ماي سكن)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / أقنعة الوجه</td></tr>
  <tr><th>نوع المنتج</th><td>قناع ورقي بالجيلي لإشراق وتفتيح البشرة (pH 5.5 Brightening Jelly Mask)</td></tr>
  <tr><th>الحجم/الوزن</th><td>33 مل (عبوة قناع فردية)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (البشرة الباهتة، المجهدة، والحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة مشرفة، نضرة، ومفعمة بالحيوية والتألق</td></tr>
  <tr><th>الملمس</th><td>جيلي غني مكثف (Rich Jelly Essence)</td></tr>
  <tr><th>العطر</th><td>عطر زهري منعش خفيف ولطيف</td></tr>
  <tr><th>المكونات النشطة</th><td>مستخلص الورد الدماكشي، مستخلص بلسم الليمون، البانثينول (B5)، التريحالوز</td></tr>
  <tr><th>بلد المنشأ</th><td>كوريا الجنوبية (South Korea)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ultru Co., Ltd. / I'm Sorry For My Skin</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الأعمار (البالغين والمراهقين)</td></tr>
</tbody>
</table>`,
    "knowledge_base": `<h2>الدليل المعرفي الطبي لصحة البشرة، التفتيح، وموازنة الحموضة (pH 5.5)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج قناع الجيلي الموازن للحموضة pH 5.5 لإشراق البشرة مشكلة بهتان الجلد وشحوبه الناتج عن التلوث البيئي والإجهاد اليومي، بالإضافة إلى خلل الغلاف الحمضي الواقي (Acid Mantle Breakdown). عندما تفتقر البشرة إلى الرطوبة الكافية وتتعرض للعوامل المؤكسدة، تتباطأ عملية التجدد الخلوي وتتراكم الخلايا الميتة، مما يجعل البشرة تفقد بريقها وتبدو متعبة وجافة. يوفر هذا القناع تفتيحاً آمناً وترطيباً غزيراً مع استعادة التوازن الحمضي الفسيولوجي للجلد.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تحدث مشكلة شحوب البشرة وتغير رقمها الهيدروجيني بسبب الاستخدام المتكرر للمنظفات القلوية القاسية، والتعرض المستمر للأشعة فوق البنفسجية، والتلوث الجوي، وقلة النوم، وتراكم الشوارد الحرة. عندما يرتفع الرقم الهيدروجيني للجلد فوق المستوى الطبيعي (pH 5.5)، تضعف الإنزيمات المسؤولة عن بناء السيراميدات وتصبح البشرة عرضة لفقدان الماء عبر البشرة (TEWL) وتكاثر البكتيريا الضارة، مما يؤدي إلى فقدان الإشراق وجفاف الجلد وتهيجه.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<ul>
  <li><strong>الحفاظ على الرقم الهيدروجيني (pH 5.5):</strong> استخدمي منظفات ومنتجات عناية خالية من الصابون ومتوازنة الحموضة لحماية حاجز البشرة الحيوي.</li>
  <li><strong>الترطيب المكثف بأقنعة الجيلي:</strong> ادعمي روتينك الأسبوعي بأقنعة غنية بالجوهر الجيلي مثل "ايم سوري فور ماي سكن" لتعويض الرطوبة المفقودة.</li>
  <li><strong>مكافحة الأكسدة بالشاي والورد:</strong> ادخلي المنتجات الغنية بمضادات الأكسدة ومستخلصات الورد لحماية الخلايا من التلف البيئي.</li>
  <li><strong>الحماية اليومية من الشمس:</strong> طبقي واقي الشمس واسع الطيف يومياً لمنع ظهور التصبغات والحفاظ على نتائج التفتيح.</li>
  <li><strong>شرب الماء والحصول على نوم كافٍ:</strong> النوم لمدة 7-8 ساعات وشرب 2 لتر من الماء يسرعان من تجدد خلايا البشرة الطبيعي.</li>
</ul>

<h3>خرافات شائعة حول أقنعة البشرة والتفتيح</h3>
<ul>
  <li><strong>خرافة:</strong> "الأقنعة الورقية ذات الجوهر المائي أفضل من أقنعة الجيلي الكثيفة."<br><strong>الحقيقة:</strong> الجوهر الجيلي (Jelly Essence) يمتاز بلزوجة وكثافة أعلى تمنع تبخر المكونات الفعالة بسرعة، مما يضمن احتباس الرطوبة وتغلغل المواد المغذية والتفتيح لطبقات أعمق وبشكل ممتد مقارنة بالسائل المائي الخفيف.</li>
  <li><strong>خرافة:</strong> "تفتيح البشرة يتطلب استخدام أحماض تقشير قوية ومخرشة دائماً."<br><strong>الحقيقة:</strong> التفتيح الطبيعي السليم يمكن تحقيقه بمكونات نباتية مهدئة ومضادات أكسدة مثل مستخلص الورد الدماكشي وموازنة الحموضة، مما يمنح إشراقة وردية دون إحداث تهيج أو تقشر قاسي للجلد.</li>
  <li><strong>خرافة:</strong> "يجب ترك القناع الورقي على الوجه حتى يجف تماماً للحصول على أقصى فائدة."<br><strong>الحقيقة:</strong> ترك القناع النسيجي حتى يجف يسبب إعادة امتصاص الرطوبة من الجلد إلى القناع جافاً (الامتصاص العكسي). الوقت المثالي هو 15 إلى 20 دقيقة فقط بينما يظل القناع رطباً.</li>
</ul>

<h3>التفسير العلمي لآلية العمل (pH 5.5 & Damask Rose Complex)</h3>
<p>تعتمد الفعالية الطبية لقناع الجيلي ايم سوري فور ماي سكن على آليتين متكاملتين: الأولى هي <strong>موازنة الحموضة الفسيولوجية (pH 5.5)</strong>، حيث يساهم البيئة الحمضية الخفيفة في تحفيز إنزيمات السيراميد سينثاز وتحسين تماسك الخلايا القرنية في طبقة البشرة الخارجية. أما الآلية الثانية فتعتمد على <strong>مستخلص الورد الدماكشي (Rosa Damascena) الممزوج بالتريحالوز والبانثينول</strong>، حيث يعمل الورد على تثبيط إنزيم التايروسينيز المسكول عن إنتاج صبغة الميلانين وتثبيط الشوارد الحرة بفضل محتواه العالي من الفلافونويد وفيتامين C. في الوقت نفسه، يشكل مركب الجيلي شبكة ثلاثية الأبعاد تنحبس داخلها جزيئات الماء لتفرز بتدفق مستمر داخل الأنسجة، مما يمنح البشرة امتلاءً وتألقاً مشرقاً فورياً.</p>`,
    "faqs": `<h3>ما هو قناع الجيلي الموازن للحموضة pH 5.5 لإشراق البشرة من ايم سوري فور ماي سكن؟</h3>
<p>هو قناع ورقي كوري مبتكر مغمور بحجم كبير (33 مل) من الجوهر الكثيف بقوام الجيلي الموازن للحموضة (pH 5.5). يعمل خصيصاً على تفتيح البشرة الباهتة، استعادة النضارة الفورية، وتهدئة الآثار الناجمة عن التلوث والإجهاد اليومي.</p>

<h3>ما معنى الرقم الهيدروجيني pH 5.5 ولماذا هو مهم جداً للبشرة؟</h3>
<p>الرقم الهيدروجيني pH 5.5 يعبر عن مستوى الحموضة المثالي والطبيعي للطبقة الواقية للبشرة (Acid Mantle). الحفاظ على هذا المستوى يحمي الجلد من نمو البكتيريا الضارة، يقلل من الجفاف والتهيج، ويضمن عمل الإنزيمات الجلدية بكفاءة عالية للحفاظ على نضارة البشرة.</p>

<h3>كيف يساعد مستخلص الورد الدماكشي في تفتيح البشرة وإعادة نضارتها؟</h3>
<p>يحتوي مستخلص الورد الدماكشي على نسبة عالية من مركبات الفلافونويد وفيتامين C الطبيعي والمغذيات الدقيقة التي تساعد في تثبيط أكسدة الخلايا وتوحيد لون البشرة، مما يمنح الوجه إشراقة وردية مفعمة بالحيوية والتألق.</p>

<h3>ما الميزة الرئيسية لقوام "الجيلي" (Jelly Essence) مقارنة بالقناع الورقي العادي؟</h3>
<p>قوام الجيلي يمتاز بكثافته ولزوجته العالية التي تلتصق بالبشرة دون قطرات أو تساقط، كما أنه يمنع تبخر السوائل بسرعة، مما يسمح بتغلغل أعلى للمكونات المغذية والتفتيح إلى عمق الأنسجة وتوفير ترطيب طويل الأمد.</p>

<h3>هل يناسب قناع الجيلي pH 5.5 جميع أنواع البشرة بما فيها البشرة الحساسة؟</h3>
<p>نعم، تم اختبار القناع سريرياً ليتناسب مع جميع أنواع البشرة بما في ذلك البشرة الحساسة والدهنية والجافة والمختلطة، بفضل تركيبته المتوازنة خالية المواد الكيميائية القاسية كالبارابين والسلفات.</p>

<h3>كم تبلغ كمية الجوهر (الجيلي) داخل عبوة القناع الواحد وهل تكفي للوجه والجسم؟</h3>
<p>تحتوي العبوة الواحدة على كمية وفيرة جداً تبلغ 33 مل من الجوهر الجيلي، وهي كمية تتجاوز احتياج الوجه، مما يتيح لك تطبيق الزوائد الكثيفة على الرقبة، اليدين، الساعدين، والكوعين لترطيب وتفتيح كامل.</p>

<h3>ما هي الطريقة الصحيحة لاستخدام قناع الجيلي للحصول على أفضل نتائج؟</h3>
<p>يُوضع القناع على بشرة نظيفة ومجهزة بالتونر لمدة 15 إلى 20 دقيقة. بعد إزالة الورقة، تُدلك البقايا بحركات دائرية خفيفة على الوجه والرقبة حتى تمتصها البشرة تماماً دون غسيل.</p>

<h3>هل يجب غسل الوجه بالماء بعد إزالة قناع الجيلي؟</h3>
<p>لا، يوصى بعدم غسل الوجه بالماء بعد إزالة القناع لترك الجوهر المغذي يواصل تغلغله وعمله في ترطيب وتفتيح البشرة؛ فقط قومي بتدليك المتبقي بأطراف أصابعك حتى الامتصاص الكامل.</p>

<h3>كم مرة يُنصح باستخدام قناع الجيلي في الأسبوع؟</h3>
<p>يُنصح باستخدام القناع من 2 إلى 3 مرات أسبوعياً للحفاظ على نضارة وتفتيح البشرة باستمرار، أو قبل المناسبات الهامة للحصول على إشراقة فورية وسريعة.</p>

<h3>هل يساعد هذا القناع في تخفيف آثار التعب والإجهاد الناتج عن التلوث والسهر؟</h3>
<p>نعم بفعالية ممتازة، فالقناع مصمم خصيصاً كعلاج تعويضي (Skin Stress Relief) لإزالة شحوب الجلد وآثار السهر والتلوث البيئي وإعادة الحيوية المرئية للبشرة المجهدة.</p>

<h3>ما دور البانثينول (فيتامين B5) ومستخلص السينتيلا في تركيبة القناع؟</h3>
<p>يعمل البانثينول على ترطيب الأنسجة العميقة وتقوية حاجز الجلد الواقي، بينما يسهم مستخلص السينتيلا أسياتيكا في تهدئة الاحمرار والتهيج وتنشيط بناء الكولاجين لصحة الجلد.</p>

<h3>هل يسبب القناع انسداد المسام أو ظهور حب الشباب؟</h3>
<p>لا، تركيبة القناع خفيفة وغنية بالماء والمتوازنة حمضياً، ولا تحتوي على زيوت ثقيلة مسببة لانسداد المسام (Non-Comedogenic)، مما يجعله آمناً تماماً للبشرة المعرضة للشوائب.</p>

<h3>هل يمكن استخدام القناع قبل وضع المكياج في المناسبات؟</h3>
<p>بالتأكيد، يعتبر القناع مستحضراً رائعاً ممهداً للمكياج (Prep Mask)، حيث ينعم ملمس البشرة، يزيل القشور الجافة، ويمنح ترطيباً عميقاً تجعل الإبراء والمكياج يظهران بأسلوب ساحر دون تكتل.</p>

<h3>هل القناع آمن للاستخدام أثناء فترة الحمل والرضاعة؟</h3>
<p>نعم، القناع يتكون من مكونات موضعية وآمنة ونباتية خالية من الرتينويد أو المواد الضارة، ومع ذلك يُفضل دائماً مراجعة الطبيب المتابع في حال وجود حساسيات خاصة.</p>

<h3>ما هو الوقت المثالي لوضع القناع على البشرة؟</h3>
<p>يمكن استخدامه في أي وقت من اليوم، ولكن استخدامه مساءً قبل النوم يمنح البشرة فرصة امتصاص المستخلصات طوال الليل، كما أن استخدامه صباحاً يوفر نضارة ممتازة لبداية اليوم.</p>

<h3>هل يمكن وضع القناع في الثلاجة قبل الاستخدام؟</h3>
<p>نعم، يوصى بوضع كيس القناع في الثلاجة لمدة 10-15 دقيقة قبل الاستخدام للحصول على تأثير تبريد وانتعاش مضاعف، مما يساعد في تقليل الانتفاخات الصباحية وتهدئة البشرة.</p>

<h3>ما الفرق بين قناع التفتيح (Brightening) والإصدارات الأخرى من نفس المجموعة؟</h3>
<p>إصدار التفتيح (Brightening) يركز بشكل أساسي على توحيد اللون وإعادة الإشراق للبشرة الباهتة بفضل الورد الدماكشي، بينما تركز الإصدارات الأخرى على الترطيب الفائق (Moisturizing) أو التهدئة العميقة (Soothing).</p>

<h3>هل يقلل القناع من التصبغات والبقع الداكنة الناتجة عن أشعة الشمس؟</h3>
<p>يساعد الاستخدام المنتظم للقناع على تخفيف مظهر التصبغات السطحية والبقع الناتجة عن الشمس والتلوث بفضل مضادات الأكسدة ومكونات التفتيح الطبيعية التي تحد من الميلانين الزائد.</p>

<h3>ما العمل بالجوهر المتبقي داخل الكيس بعد أخذ ورقة القناع؟</h3>
<p>الجوهر المتبقي غني جداً بالمواد الفعالة؛ يمكنك وضعه على الرقبة، منطقة الصدر، اليدين، والقدمين، أو حفظ الكيس مغلقاً واستخدامه كجل مرطب مغذٍ في اليوم التالي.</p>

<h3>هل يحتوي القناع على مكونات قاسية أو بارابين أو كحول ضار؟</h3>
<p>لا، القناع خالٍ تماماً من البارابين، الفثالات، السلفات، والكحوليات الجافة القاسية، وتم اختباره من أطباء الجلدية لضمان أقصى درجات الأمان والسلامة.</p>

<h3>كيف يعمل مركب التريحالوز والجليسرين على حفظ الرطوبة طويلة الأمد؟</h3>
<p>التريحالوز والجليسرين هما مرطبات ماصة للماء (Humectants) تحاكي عامل الترطيب الطبيعي في البشرة، حيث تجذب جزيئات الماء وتحتفظ بها داخل الخلايا لمنع الجفاف حتى في أجواء الصيف الجافة.</p>

<h3>هل يمكن استخدام القناع بعد جلسات التقشير الكيميائي أو الليزر؟</h3>
<p>بعد جلسات التقشير والليزر بأيام قليلة وعند التئام البشرة، يوصى باستخدام أقنعة pH 5.5 لتهدئة الأنسجة وإعادة موازنة الحموضة، لكن يُفضل استشارة طبيب الجلدية المتابع أولاً.</p>

<h3>هل يناسب القناع البشرة الدهنية والمختلطة أم البشرة الجافة فقط؟</h3>
<p>يناسب جميع أنواع البشرة بدون استثناء؛ فالبشرة الدهنية تستفيد من موازنة الحموضة وتخفيف الإفرازات الزائدة، بينما تستفيد البشرة الجافة من الترطيب الجيلي العميق.</p>

<h3>كم تدوم نتائج الإشراق والنضارة بعد استخدام القناع؟</h3>
<p>تظهر النضارة والإشراق فور إزالة القناع وتستمر عادة من 24 إلى 48 ساعة، ومع الاستمرار في الاستخدام الأسبوعي تصبح البشرة أكثر إشراقاً وتماسكاً بشكل دائم.</p>

<h3>أين يتم تصنيع قناع ايم سوري فور ماي سكن وهل المنتج أصلي لدى إكليل أبها؟</h3>
<p>يتم تصنيع القناع بفخر في كوريا الجنوبية بواسطة شركة Ultru العالمية وفق أحدث المعايير الكورية للتجميل (K-Beauty)، وهو منتج أصلي 100% مضمون ومتوفر لدى صيدلية إكليل أبها السعودية.</p>`,
    "tags": [
      "ايم_سوري_فور_ماي_سكن",
      "قناع_الجيلي",
      "تفتيح_البشرة",
      "pH5.5",
      "ماسك_كوري",
      "إكليل_أبها",
      "نضارة_البشرة",
      "الورد_الدماكشي"
    ]
  },
  "en": {
    "title": "I'm Sorry For My Skin pH 5.5 Jelly Mask - Brightening (33 ml)",
    "meta_title": "I'm Sorry For My Skin pH 5.5 Brightening Jelly Mask 33ml | Ekleel",
    "meta_description": "Buy I'm Sorry For My Skin pH 5.5 Brightening Jelly Mask (33ml). Enriched with Damask Rose & Panthenol for instant radiance & skin balance. 100% Authentic from Ekleel Abha Pharmacy.",
    "description": `<h2>Product Overview</h2>
<p>The <strong>I'm Sorry For My Skin pH 5.5 Jelly Mask - Brightening (33 ml)</strong> is a cutting-edge South Korean skincare innovation designed by dermatological experts to instantly restore radiance and vitality to dull, fatigued, and environmentally stressed skin. Factors such as urban pollution, lack of sleep, prolonged sun exposure, and daily emotional stress deplete the skin's natural glow and disrupt its protective barrier. This clinical-grade sheet mask offers an intensive corrective treatment that combines powerful botanical brightening agents with pH 5.5 acid-mantle balancing technology.</p>
<p>What sets this product apart is its ultra-generous 33 ml bath of concentrated <strong>Jelly Essence</strong>. Unlike watery sheet masks that dry out quickly or drip, this thick, cushiony hydrogel jelly adheres seamlessly to facial contours, driving active nutrients deep into the dermal layers. Infused with Damask Rose extract, Lemon Balm, Centella Asiatica, and Pro-Vitamin B5 (Panthenol), it visibly brightens skin tone, smooths rough texture, and erases signs of exhaustion in just 15 to 20 minutes.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Instant Brightening & Radiance Boost:</strong> Revitalizes dull, tired complexions and restores natural luminous glow using Damask Rose extract and potent antioxidants.</li>  <li><strong>Optimal pH 5.5 Acid Mantle Balance:</strong> Maintains the skin's natural physiological pH level (~5.5), suppressing acne-causing bacteria and preventing moisture loss.</li>
  <li><strong>Deep & Sustained Jelly Hydration:</strong> Packed with 33 ml of rich Jelly Essence enriched with Trehalose and Glycerin to lock moisture deep within skin tissues.</li>
  <li><strong>Soothes Stress & Redness:</strong> Calms irritated skin, reduces micro-inflammation, and relieves environmental stress with Panthenol and botanical extracts.</li>
  <li><strong>Improves Skin Texture & Elasticity:</strong> Leaves skin feeling velvety smooth, plump, and refined, diminishing the appearance of enlarged pores.</li>
  <li><strong>High-Adhesion Microfiber Sheet:</strong> Soft microfiber matrix hugs facial curves snugly for maximum nutrient transfer without slipping or dripping.</li>
  <li><strong>Clean & Gentle Formula:</strong> Free from parabens, harsh sulfates, synthetic dyes, and drying alcohols, making it suitable for even hypersensitive skin.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse & Prep):</strong> Thoroughly wash your face with a mild cleanser suitable for your skin type, pat dry, and apply a hydrating toner to balance the skin canvas.</li>
  <li><strong>Step 2 (Apply Sheet Mask):</strong> Carefully unfold the sheet mask and align it over your face, fitting the openings for your eyes, nose, and mouth smoothly.</li>
  <li><strong>Step 3 (Relax & Activate):</strong> Leave the mask on for 15 to 20 minutes to allow the concentrated jelly essence to fully penetrate your skin.</li>
  <li><strong>Step 4 (Massage & Absorb):</strong> Remove the sheet mask gently and pat the remaining jelly essence into your face and neck using soft circular motions until absorbed. Do not rinse.</li>
  <li><strong>Step 5 (Utilize Extra Essence):</strong> Massage the excess jelly essence remaining inside the pouch onto your hands, elbows, and neck for extended hydration and brightening.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Rosa Damascena Flower Extract:</strong> A luxury botanical ingredient that brightens dark spots, unifies skin tone, and delivers a healthy rosy glow with rich antioxidant flavonoids.</li>
  <li><strong>Melissa Officinalis (Lemon Balm) Leaf Extract:</strong> Purifies the skin, calms cutaneous inflammation, and balances natural sebum secretion.</li>
  <li><strong>Panthenol (Pro-Vitamin B5):</strong> A renowned humectant and skin protectant that penetrates deep layers to soothe irritation and fortify the natural barrier.</li>
  <li><strong>Trehalose & Glycerin:</strong> Osmotic humectant sugars that bind water molecules tightly within skin cells, preventing trans-epidermal water loss.</li>
  <li><strong>pH 5.5 Balancing Complex:</strong> A mild acidic matrix that mimics physiological skin pH, nurturing beneficial cutaneous microflora.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external dermatological use only. Avoid direct contact with the inner eyes.</li>
  <li>If contact occurs with eyes, rinse immediately with clean lukewarm water.</li>
  <li>Do not apply on broken skin, open wounds, severe sunburns, or active eczema patches.</li>
  <li>Keep out of reach of children. Store in a cool, dry place away from direct sunlight (can be refrigerated for enhanced cooling).</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Individuals dealing with dull, tired, or sallow skin caused by environmental pollution and sleep deprivation.</li>
  <li>People seeking safe, non-irritating skin brightening and hyperpigmentation reduction.</li>
  <li>All skin types (oily, dry, combination, and sensitive) requiring barrier repair and pH normalization.</li>
  <li>Men and women looking for an immediate radiant skin prep before special events or makeup application.</li>
</ul>`,
    "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>I'm Sorry For My Skin</td></tr>
  <tr><th>Category</th><td>Skin Care / Face Masks</td></tr>
  <tr><th>Product Type</th><td>pH 5.5 Brightening Jelly Sheet Mask</td></tr>
  <tr><th>Volume/Weight</th><td>33 ml (Single Mask Packet)</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Dull, Stressed & Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Radiant, Glowing, & Hydrated Finish</td></tr>
  <tr><th>Texture</th><td>Rich Jelly Essence</td></tr>
  <tr><th>Fragrance</th><td>Light Refreshing Floral Scent</td></tr>
  <tr><th>Active Ingredients</th><td>Rosa Damascena Extract, Lemon Balm Extract, Panthenol, Trehalose</td></tr>
  <tr><th>Country of Origin</th><td>South Korea</td></tr>
  <tr><th>Manufacturer</th><td>Ultru Co., Ltd. / I'm Sorry For My Skin</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens</td></tr>
</tbody>
</table>`,
    "knowledge_base": `<h2>Clinical Knowledge Base: Skin Brightening, Barrier Balance & pH 5.5 Science</h2>

<h3>What problem does this solve?</h3>
<p>The I'm Sorry For My Skin pH 5.5 Jelly Mask (Brightening) directly addresses cutaneous dullness, uneven skin tone, and acid mantle breakdown caused by urban pollution and oxidative stress. When skin is exposed to free radicals and alkaline cleansers, cellular turnover slows down, leading to dead cell accumulation, moisture loss, and a sallow complexion. This clinical mask delivers targeted botanical brightening, deep hydration, and physiological pH normalization.</p>

<h3>Why does this condition happen?</h3>
<p>Skin dullness and barrier disruption occur when the skin's natural acidic mantle (normally around pH 5.5) becomes alkaline due to harsh soaps, UV radiation, and environmental toxins. An elevated pH degrades ceramide-synthesizing enzymes, increasing Trans-Epidermal Water Loss (TEWL) and allowing harmful microbes to proliferate. Consequently, the skin loses its natural luminosity, becomes prone to inflammation, and develops micro-roughness.</p>

<h3>Prevention Tips</h3>
<ul>
  <li><strong>Maintain Optimal pH (5.5):</strong> Use soap-free, pH-balanced cleansers and treatments to safeguard your protective acid mantle.</li>
  <li><strong>Weekly Jelly Mask Treatment:</strong> Integrate rich jelly essence sheet masks into your weekly routine to replenish deep hydration reservoirs.</li>
  <li><strong>Antioxidant Protection:</strong> Incorporate botanical antioxidants like Damask Rose and Green Tea to neutralize free radicals from UV and pollution.</li>
  <li><strong>Daily Broad-Spectrum Sunscreen:</strong> Apply SPF daily to prevent UV-induced melanogenesis and preserve brightening benefits.</li>
  <li><strong>Hydration & Sleep:</strong> Drink 2 liters of water daily and ensure 7-8 hours of restful sleep to optimize nocturnal cellular regeneration.</li>
</ul>

<h3>Common Myths</h3>
<ul>
  <li><strong>Myth:</strong> "Thin, watery sheet masks hydrate skin better than thick jelly essence masks."<br><strong>Fact:</strong> Watery essences evaporate quickly on the skin surface. Cushioning Jelly Essence has higher viscosity, locking in active ingredients and pushing nutrients deeper into the epidermal layers without premature evaporation.</li>
  <li><strong>Myth:</strong> "Skin brightening requires aggressive chemical exfoliants and acids."<br><strong>Fact:</strong> Gentle botanical extracts like Damask Rose combined with pH 5.5 balancing can achieve superior brightening without stripping the barrier or causing peeling and irritation.</li>
  <li><strong>Myth:</strong> "You should leave a sheet mask on until it dries completely."<br><strong>Fact:</strong> Leaving a mask until dry causes reverse osmosis, pulling moisture back out of the skin. The ideal wear time is strictly 15 to 20 minutes while the sheet remains damp.</li>
</ul>

<h3>Scientific Explanation of Mechanism (pH 5.5 & Damask Rose Complex)</h3>
<p>The therapeutic performance of the I'm Sorry For My Skin Jelly Mask relies on two scientific mechanisms: <strong>Physiological Acid Mantle Support (pH 5.5)</strong> and <strong>Phyto-Antioxidant Brightening</strong>. The pH 5.5 acidic environment optimizes beta-glucocerebrosidase enzyme activity, accelerating endogenous ceramide production and fortifying tight junctions between keratinocytes. Simultaneously, <strong>Rosa Damascena Extract</strong> rich in polyphenols and natural Ascorbic Acid inhibits Tyrosinase enzyme activity—the key rate-limiting step in melanin synthesis. Combined with <strong>Trehalose and Panthenol</strong>, the jelly matrix creates an osmotic moisture shield, continuously diffusing active compounds into the stratum corneum for immediate luminescence and plumpness.</p>`,
    "faqs": `<h3>What is the I'm Sorry For My Skin pH 5.5 Jelly Mask - Brightening?</h3>
<p>It is an innovative South Korean sheet mask soaked in a generous 33 ml bath of concentrated pH 5.5 Jelly Essence. It is specifically formulated to brighten dull skin, restore radiance, and soothe fatigue caused by pollution and daily stress.</p>

<h3>What does pH 5.5 mean and why is it important for skin?</h3>
<p>pH 5.5 represents the ideal, natural acidity level of the skin's protective barrier (Acid Mantle). Maintaining pH 5.5 protects against acne-causing bacteria, reduces irritation, and ensures optimal enzyme function for healthy, glowing skin.</p>

<h3>How does Damask Rose extract help in brightening the skin?</h3>
<p>Damask Rose extract is rich in natural Vitamin C, flavonoids, and essential antioxidants that inhibit melanin overproduction, unify skin tone, and impart a vibrant, healthy rosy glow to dull complexions.</p>

<h3>What is the key advantage of the "Jelly Essence" texture over standard sheet masks?</h3>
<p>The thick jelly texture clings snugly to the face without dripping or evaporating quickly. It creates a seal that drives hydrating and brightening nutrients deeper into the skin layers compared to thin watery essences.</p>

<h3>Is the pH 5.5 Jelly Mask suitable for all skin types, including sensitive skin?</h3>
<p>Yes, it is clinically tested and formulated to be safe for all skin types—including sensitive, dry, oily, and combination skin—thanks to its gentle, clean, hypoallergenic composition.</p>

<h3>How much essence is contained inside each packet and can it be used on the body?</h3>
<p>Each pouch contains an extra-large volume of 33 ml of jelly essence, which is more than enough for your face. The excess jelly can be applied generously to your neck, chest, hands, and arms.</p>

<h3>What is the correct step-by-step method to use this mask for optimal results?</h3>
<p>Apply the mask onto clean, toned skin for 15 to 20 minutes. After removing the sheet, gently massage the remaining jelly into your face and neck until fully absorbed. Do not wash off.</p>

<h3>Should I wash my face with water after removing the sheet mask?</h3>
<p>No, you should not rinse with water after removing the mask. Allow the rich nutrient jelly to remain on your skin to continue hydrating and brightening your complexion.</p>

<h3>How many times a week should I use this brightening jelly mask?</h3>
<p>It is recommended to use the mask 2 to 3 times a week for continuous radiance and hydration, or right before special events for an instant glowing boost.</p>

<h3>Does this mask help recover skin from environmental pollution and lack of sleep?</h3>
<p>Yes, it is specifically designed as an emergency skin recovery treatment (Skin Stress Relief) to erase signs of fatigue, dullness, and urban environmental stress.</p>

<h3>What is the role of Panthenol (Pro-Vitamin B5) and Centella Asiatica in the formula?</h3>
<p>Panthenol deeply hydrates and reinforces the skin barrier, while Centella Asiatica soothes redness, calms cutaneous irritation, and promotes collagen synthesis.</p>

<h3>Will this jelly mask clog pores or trigger acne breakouts?</h3>
<p>No, the formula is lightweight, water-rich, pH-balanced, and free from heavy comedogenic oils, making it completely safe for acne-prone and combination skin.</p>

<h3>Can I use this mask right before applying makeup for special events?</h3>
<p>Yes, it acts as an outstanding prep mask. It smooths rough skin, eliminates dry patches, and deeply hydrates, ensuring flawless, seamless makeup application.</p>

<h3>Is the mask safe to use during pregnancy and breastfeeding?</h3>
<p>Yes, the mask contains safe, topical, plant-based ingredients free from retinoids or harmful chemicals. However, consulting your physician is always good practice.</p>

<h3>What is the ideal time of day to apply the sheet mask?</h3>
<p>It can be used anytime. Using it in the evening allows nighttime absorption of nutrients, while morning application provides an instant refreshing glow for the day ahead.</p>

<h3>Can I chill the mask packet in the refrigerator before application?</h3>
<p>Yes! Placing the unopened pouch in the fridge for 10-15 minutes prior to use delivers an invigorating cooling effect that reduces morning facial puffiness and calms skin.</p>

<h3>What is the difference between the Brightening edition and other variants?</h3>
<p>The Brightening edition focuses on boosting skin radiance and evening out dull tone with Damask Rose, whereas other variants target intense moisture (Moisturizing) or deep calming (Soothing).</p>

<h3>Does this mask help reduce hyperpigmentation and sun spots over time?</h3>
<p>Regular use helps fade superficial dark spots and sun-induced discoloration over time due to its rich antioxidant complex and melanin-inhibiting botanical ingredients.</p>

<h3>How should I use the remaining jelly essence left inside the pouch?</h3>
<p>You can massage the extra jelly onto your neck, decollete, hands, and feet, or store the sealed packet to use as a hydrating serum gel the following day.</p>

<h3>Does the mask contain harsh parabens, sulfates, or drying alcohols?</h3>
<p>No, the formula is 100% free from parabens, sulfates, harsh phthalates, and drying alcohols, ensuring gentle care verified by dermatological standards.</p>

<h3>How do Trehalose and Glycerin work to provide long-lasting deep hydration?</h3>
<p>Trehalose and Glycerin are clinical humectants that bind water molecules tightly within skin cells, mimicking natural moisturizing factors to prevent dryness all day long.</p>

<h3>Can I use this mask after dermatological treatments such as chemical peels or lasers?</h3>
<p>Once your skin has healed post-procedure, pH 5.5 masks help rebalance and soothe the skin barrier. Always consult your dermatologist prior to post-treatment use.</p>

<h3>Is the mask suitable for oily skin, or only dry skin?</h3>
<p>It is excellent for oily skin because the pH 5.5 balance helps regulate sebum production without leaving greasy residue, while dry skin benefits from deep hydrogel hydration.</p>

<h3>How long do the brightening and radiance results last after single application?</h3>
<p>Visible skin luminescence and plumpness are immediate upon removal and last 24 to 48 hours. Consistent weekly application yields long-term skin clarity and resilience.</p>

<h3>Where is I'm Sorry For My Skin manufactured and is it authentic at Ekleel Abha?</h3>
<p>It is proudly manufactured in South Korea by Ultru Co., Ltd. under strict K-Beauty quality standards. It is 100% authentic and available at Ekleel Abha Pharmacy in Saudi Arabia.</p>`,
    "tags": [
      "im_sorry_for_my_skin",
      "jelly_mask",
      "brightening_mask",
      "ph5.5",
      "korean_sheet_mask",
      "ekleel_abha",
      "radiance",
      "damask_rose"
    ]
  },
  "schema": {
    "brand": "I'm Sorry For My Skin",
    "category": "Skin Care / Face Masks",
    "availability": "InStock"
  },
  "image_seo": {
    "image_filename": "im-sorry-for-my-skin-ph55-jelly-mask-brightening-33ml.webp",
    "alt": "I'm Sorry For My Skin pH 5.5 Jelly Mask Brightening 33ml",
    "title": "I'm Sorry For My Skin pH 5.5 Jelly Mask Brightening 33ml"
  }
};

// Target directory paths
const primaryDir = path.join(__dirname, '../temp/generated_products');
const secondaryDir = path.join(__dirname, 'temp/generated_products');

[primaryDir, secondaryDir].forEach(dir => {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
});

const primaryFile = path.join(primaryDir, `${productId}.json`);
const secondaryFile = path.join(secondaryDir, `${productId}.json`);

fs.writeFileSync(primaryFile, JSON.stringify(productData, null, 2), 'utf8');
fs.writeFileSync(secondaryFile, JSON.stringify(productData, null, 2), 'utf8');

console.log(`✅ Saved Product ${productId} JSON to:\n  - ${primaryFile}\n  - ${secondaryFile}`);

// Execute db_sync.js
try {
  console.log("⚡ Executing db_sync.js...");
  const output = execSync('node db_sync.js', { encoding: 'utf8' });
  console.log(output);
} catch (err) {
  console.error("❌ Error executing db_sync.js:", err.stdout || err.message);
  process.exit(1);
}
