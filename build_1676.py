import json, os

ar_description = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد عطر <strong>كارلوتا سكانداله او دي تواليت للنساء (100 مل)</strong> تحفةً عطريةً نسائيةً تأسر الحواس وتترك أثراً لا يُنسى. تنتمي هذه التركيبة الرائعة إلى عائلة عطور الشيبر الزهري (Chypre Floral)، وتفتح بانطلاقة حيوية منعشة ثم تنكشف تدريجياً لتُظهر قلباً أنثوياً دافئاً ومعقداً، لتستقر أخيراً على قاعدة بالغة الإغراء. العطر مستوحى من روح الأنوثة الجريئة والمتمردة، يُعبّر عن المرأة الواثقة بنفسها المتجردة عن التقاليد.</p>
<p>تتجلى في هذا العطر براعة دار كارلوتا في صياغة تجارب عطرية استثنائية، حيث يُقدّم مزيجاً متناغماً يبدأ بنضارة الحمضيات المتوهجة، ويمر عبر أسرار أزهار الفردوس وعذوبة العسل والخوخ، لينتهي بعمق الشمع والكراميل الذي يُضفي على العطر سحراً حسياً يدوم طوال النهار والليل.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>مثابرة عطرية استثنائية:</strong> يتمتع العطر بثبات ملحوظ على الجلد، يُرافق صاحبته لساعات طويلة ويترك أثراً عطرياً (سيلاج) فاتناً في كل مكان تمر منه.</li>
  <li><strong>تجربة عطرية متعددة الأبعاد:</strong> تطور رائحته التدريجي من النضارة الحمضية في البداية إلى الدفء الزهري ثم القاعدة الحسية يجعله عطراً حياً متجدداً على مدار اليوم.</li>
  <li><strong>توقيع نسائي فريد:</strong> يجمع ببراعة بين الأنثوية الحديثة والجرأة المتمردة، مما يجعله مناسباً لكل امرأة تريد أن تُعبّر عن شخصيتها بلا حدود.</li>
  <li><strong>تركيبة شيبر زهرية مميزة:</strong> تمزج الشيبر الكلاسيكية مع نعومة الزهور الفاخرة لخلق هوية عطرية راسخة تحمل بصمة التطور والأناقة.</li>
  <li><strong>ملائم للمناسبات المسائية والرسمية:</strong> يبرز تأثير العطر الساحر خاصةً مع الحرارة مما يجعله الرفيق الأمثل للسهرات والمناسبات الراقية.</li>
  <li><strong>تغليف أنيق فاخر:</strong> يأتي بتصميم عبوة عصري يعكس هوية العطر ويجعله هديةً مثاليةً للمرأة التي تقدر التميز.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التحضير):</strong> تأكدي من أن بشرتك نظيفة وجافة قبل التطبيق لضمان التصاق أفضل للعطر.</li>
  <li><strong>الخطوة الثانية (البخ على نقاط النبض):</strong> بخّي العطر على نقاط النبض الدافئة: باطن المعصمين، أسفل العنق، خلف الأذنين، وداخل الكوعين لتعزيز انتشار الرائحة.</li>
  <li><strong>الخطوة الثالثة (المسافة المثالية):</strong> احرصي على مسافة 15-20 سم بين البخاخ والجلد لتوزيع بخاخ العطر بشكل متساوٍ ومناسب.</li>
  <li><strong>الخطوة الرابعة (لا تفركي):</strong> لا تفركي مناطق البخ ببعضها البعض لأن ذلك يُفكك الجزيئات العطرية ويُضعف الأثر ويغير المسار العطري.</li>
  <li><strong>الخطوة الخامسة (حفظ العطر):</strong> احفظي الزجاجة بعيداً عن الضوء المباشر والحرارة والرطوبة للحفاظ على جودة العطر وإطالة عمره.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>النوتات الرأسية (البرتقال الدموي والماندرين):</strong> تفتح العطر بانطلاقة حمضية زاهية تمنح شعوراً فورياً بالانتعاش والحيوية والأناقة.</li>
  <li><strong>نوتات القلب (العسل، الغاردينيا، زهر البرتقال، الياسمين، الخوخ):</strong> تُشكّل قلب العطر الرومانسي والحسي، حيث يمزج العسل الدافئ مع الزهور الناصعة والخوخ المثمر لخلق مزيج أنثوي استثنائي.</li>
  <li><strong>نوتات القاعدة (شمع النحل، الكراميل، الباتشولي، العرق السوس):</strong> تُرسّخ العطر بقاعدة عميقة وحسية تبقى على الجلد لساعات طويلة وتترك أثراً خاطفاً.</li>
  <li><strong>عائلة عطرية: الشيبر الزهري (Chypre Floral):</strong> هذه العائلة العطرية العريقة تجمع بين الحيوية والعمق والأنثوية في تناغم نادر يناسب المرأة العصرية الواثقة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي فقط على الجلد؛ يُمنع تناوله أو استنشاقه بشكل مباشر ومركّز.</li>
  <li>تجنبي ملامسة العطر للعينين أو الأغشية المخاطية؛ وفي حالة التلامس العرضي اشطفي فوراً بالماء.</li>
  <li>يُنصح بعدم رشّ العطر مباشرةً على الملابس الحريرية أو المصنوعة من الألياف الحساسة لأنه قد يُخلّف بقعاً.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد بعيداً عن أشعة الشمس المباشرة والحرارة الشديدة.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>للمرأة الجريئة الواثقة بنفسها التي تبحث عن عطر يُعبّر عن شخصيتها الاستثنائية وجاذبيتها الأنثوية.</li>
  <li>لمحبات عطور الشيبر الزهرية التي تمتاز بالعمق والتطور والثبات الطويل على الجلد.</li>
  <li>مثالي للإرتداء في المناسبات المسائية والحفلات والأوساط الاجتماعية الراقية والسهرات الخاصة.</li>
  <li>هدية مثالية لكل امرأة تستحق الفخامة وتقدّر فن صناعة العطور.</li>
</ul>"""

ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كارلوتا (Carlotta)</td></tr>
  <tr><th>الفئة</th><td>عطور نسائية</td></tr>
  <tr><th>نوع المنتج</th><td>او دي تواليت (Eau de Toilette) - بخاخ</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (عطر للجسم)</td></tr>
  <tr><th>المظهر النهائي</th><td>أثر عطري فاتن وراسخ يدوم ساعات</td></tr>
  <tr><th>الملمس</th><td>رذاذ سائل خفيف</td></tr>
  <tr><th>العطر</th><td>شيبر زهري - برتقال دموي، عسل، غاردينيا، ياسمين، كراميل، باتشولي</td></tr>
  <tr><th>المكونات النشطة</th><td>برتقال دموي، ماندرين، عسل، غاردينيا، زهر البرتقال، ياسمين، خوخ، شمع النحل، كراميل، باتشولي، عرق السوس</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين</td></tr>
  <tr><th>الشركة المصنعة</th><td>Carlotta / Giuseppe Fragrances</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغات (18+)</td></tr>
</tbody>
</table>"""

ar_kb = """<h2>الدليل المعرفي لفن اختيار العطور النسائية</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يحل عطر كارلوتا سكانداله مشكلة البحث عن عطر نسائي يجمع بين الشخصية الجريئة والأنوثة الراقية بسعر في المتناول. كثير من النساء يجدن صعوبة في العثور على عطر يُعبّر فعلاً عن استقلاليتهن ويمنحهن ثقة إضافية في المناسبات الاجتماعية.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تتباين أذواق النساء في العطور بشكل كبير، وكثيراً ما تسعى المرأة لعطر يُلائم تغيرات شخصيتها خلال اليوم؛ من نضارة الصباح إلى الجاذبية المسائية. عطور الشيبر الزهرية تُعالج هذا التحدي بمسارها العطري المتطور الذي يتكيف مع حرارة الجسم ويُقدّم تجربة متغيرة وغنية على مدار ساعات الارتداء.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الترطيب قبل العطر:</strong> ضعي مرطباً بدون رائحة قبل بخ العطر لأن الجلد المرطب يحتجز العطر أطول.<br>
2. <strong>التوقيت الصحيح:</strong> ضعي العطر مباشرةً بعد الاستحمام عندما تكون مسام الجلد مفتوحة لامتصاص أفضل.<br>
3. <strong>التنسيق مع الطقس:</strong> العطور الشيبرية تبرز أكثر في الطقس الدافئ والمساءات، لذا خصصي سكانداله لهذه الأوقات.<br>
4. <strong>عدم الإكثار:</strong> بخّتان إلى ثلاث كافية تماماً لأن العطر غني وله حضور قوي بطبيعته.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "او دي تواليت ثباته أقل من او دي بارفان دائماً."<br>
<strong>الحقيقة:</strong> يعتمد الثبات على تركيبة العطر ونوعية المكونات أكثر من نسبة الكحول. عطر سكانداله يمتاز بقاعدة شمع النحل والباتشولي الثقيلة التي تمنحه ثباتاً استثنائياً.</p>
<p><strong>خرافة:</strong> "العطور الزهرية مناسبة للنهار فقط."<br>
<strong>الحقيقة:</strong> العطور الشيبر الزهرية كسكانداله تحمل عمق القاعدة الكافي لتكون جميلة جداً في المساء بفضل الكراميل والباتشولي.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يتفاعل العطر مع الجلد عبر ثلاث مراحل كيميائية: المسار الأعلى (Top Notes) وهي أكثر المركبات تطايراً تُدرك فورياً عند البخ، يليها نوتات القلب (Heart Notes) الأقل تطايراً والتي تظهر بعد 10-30 دقيقة، وأخيراً نوتات القاعدة (Base Notes) الأثقل جزيئياً التي ترتبط بالبروتينات الجلدية وتبقى لساعات. في سكانداله، يتفاعل شمع النحل والكراميل مع دفء الجلد ليُصدرا تدريجياً رائحة حسية عميقة تُعرف بـ "البصمة العطرية" الفريدة لكل فرد.</p>"""

faqs = [
    ("ما هو عطر كارلوتا سكانداله وما الذي يميزه؟", "عطر كارلوتا سكانداله هو او دي تواليت نسائي من عائلة الشيبر الزهري، يمتاز بمسار عطري متطور يبدأ بالحمضيات المنعشة ويمر بقلب زهري دافئ ويختتم بقاعدة حسية عميقة من الكراميل والباتشولي. يُجسّد هذا العطر الأنوثة الجريئة والمتمردة في زجاجة أنيقة تدوم على الجلد لساعات."),
    ("ما هي نوتات العطر الرئيسية في سكانداله؟", "يفتح سكانداله بنوتات رأسية من البرتقال الدموي والماندرين المنعشة، ثم ينكشف قلبه عبر العسل والغاردينيا وزهر البرتقال والياسمين والخوخ، ليستقر على قاعدة فاخرة من شمع النحل والكراميل والباتشولي وعرق السوس التي تمنحه عمقاً وديمومة استثنائية."),
    ("هل عطر سكانداله مناسب للاستخدام اليومي أم للمناسبات فقط؟", "يمكن ارتداؤه يومياً في الأوقات المسائية أو لمناسبات خاصة. تركيبته الشيبرية الزهرية الغنية تجعله أكثر توهجاً في الأجواء الدافئة والمسائية، وقد يكون شخصياً جداً للبيئات المغلقة إذا أُسرف في استخدامه."),
    ("كم يدوم عطر سكانداله على الجلد؟", "بفضل قاعدة الباتشولي وشمع النحل والكراميل، يتميز سكانداله بثبات جيد يتراوح بين 6-8 ساعات على الجلد عند وضعه على نقاط النبض الدافئة، كما يترك أثراً عطرياً لطيفاً على الملابس لفترة أطول."),
    ("ما هي أفضل مناطق الجسم لوضع العطر عليها؟", "يُوصى بوضع عطر سكانداله على نقاط النبض الدافئة مثل باطن المعصمين، منطقة الرقبة والترقوة، خلف الأذنين، وداخل الكوعين. هذه المناطق تُولّد حرارة تُساعد على تطاير وانتشار العطر طوال اليوم."),
    ("هل يمكن وضع سكانداله على الملابس؟", "يمكن بخ كمية خفيفة على حواف الملابس المقاومة للبقع، ولكن يُنصح بتجنب الأقمشة الحريرية والفاتحة لأن الزيوت العطرية قد تترك أثراً. التطبيق المباشر على الجلد دائماً هو الأفضل للتجربة العطرية الكاملة."),
    ("هل سكانداله مناسب لفصل الصيف؟", "يمكن ارتداؤه صيفاً مع الأخذ بعين الاعتبار أن الحرارة تُعزز انتشار النوتات المكثفة كالكراميل والباتشولي، مما يجعله أكثر قوة. يُنصح بخفة الكمية صيفاً (بخة أو بخّتان كافيتان)."),
    ("ما هي الفئة العمرية الأنسب لعطر سكانداله؟", "يُناسب المرأة البالغة من 20 سنة فأكثر وبالتحديد المرأة التي تميل لعطور الشخصية الجريئة والحضور القوي. قد يكون مكثفاً للفتيات الصغيرات التي تُفضّل العطور الخفيفة."),
    ("كيف أحافظ على عطر سكانداله من التلف؟", "احتفظي بالزجاجة في مكان بارد وجاف بعيداً عن التعرض للضوء المباشر وتقلبات الحرارة، وأغلقي الغطاء جيداً بعد كل استخدام. تجنبي تخزينه في الحمام لأن الرطوبة والحرارة تُفسد التركيبة العطرية."),
    ("هل يمكن خلط سكانداله مع عطور أخرى؟", "نعم، هذه تقنية 'التطبيق الطبقي' (Layering). يمكن تطبيق عطر خفيف ومحايد كقاعدة أولاً ثم وضع سكانداله فوقه لتعزيز ثباته. ومع ذلك، يُنصح بتجربة التوافق أولاً بكميات صغيرة."),
    ("هل عطر سكانداله مستوحى من عطر آخر؟", "نعم، عطر سكانداله مستوحى من عطر سكاندال الشهير لجان بول غوتييه (Jean Paul Gaultier Scandal). يُقدّم كارلوتا تفسيرهم الخاص لهذا المزيج الزهري الحسي بجودة عالية وبسعر أكثر سهولة."),
    ("هل سكانداله مناسب كهدية؟", "بالتأكيد، يُعد عطر سكانداله خياراً راقياً وفكرة هدية مميزة لأي مناسبة سواء أعياد الميلاد أو الأعياد أو التقدير. تغليفه الأنيق وعطره الفاخر يجعله هدية ذات قيمة وانطباع أول رائع."),
    ("ما حجم زجاجة عطر سكانداله؟", "تأتي الزجاجة بسعة 100 مل، وهو حجم مثالي للاستخدام اليومي ولفترة طويلة. يكفي هذا الحجم عادةً من 6-12 شهراً تبعاً لكثافة الاستخدام."),
    ("ما الذي يعنيه مصطلح او دي تواليت (Eau de Toilette)؟", "او دي تواليت هو تصنيف للعطور يدل على نسبة تركيز الزيوت العطرية التي تتراوح عادةً بين 5-15%. يمنح ثباتاً لائقاً مع خفة نسبية مقارنةً بالبارفان، وهو الأنسب للاستخدام اليومي والمناسبات غير الرسمية."),
    ("لماذا تختلف رائحة العطر من شخص لآخر؟", "لأن العطر يتفاعل مع الكيمياء الحيوية الفردية لكل شخص، وتشمل: الحموضة الطبيعية للجلد، الهرمونات، النظام الغذائي، ودرجة حرارة الجلد. لذا يكون لكل شخص 'بصمة عطرية' خاصة عند ارتداء نفس العطر."),
    ("هل عطر سكانداله آمن للحساسية؟", "يُنصح الأشخاص ذوو الحساسية الشديدة للعطور باختبار العطر على منطقة صغيرة من الجلد وانتظار 24 ساعة قبل الاستخدام الكامل. إذا ظهرت أي أعراض تهيج، يجب إيقاف الاستخدام واستشارة الطبيب."),
    ("هل يختلف أداء العطر في الشتاء عن الصيف؟", "نعم، الحرارة تُعزز تطاير وانتشار العطر. في الشتاء، يكون العطر أكثر هدوءاً وداخلياً، بينما في الصيف يكون أكثر انتشاراً وحضوراً. يُنصح في الشتاء بزيادة كمية البخ طفيفاً وفي الصيف التقليل."),
    ("كيف يختلف شمع النحل في القاعدة عن مكونات أخرى؟", "شمع النحل (Beeswax) يمنح العطر دفئاً حسياً طبيعياً وملمساً كريمياً في الأثر العطري. يتفاعل مع حرارة الجلد ليُصدر رائحة ناعمة وعميقة تذكر بالعطور الشرقية الكلاسيكية ويُعزز ثبات التركيبة."),
    ("ما الباتشولي وما دوره في عطر سكانداله؟", "الباتشولي هو نبات من جنوب شرق آسيا يُعطي عطره الترابي العميق المميز. في سكانداله، يُشكّل الباتشولي جسر الوصل بين نضارة الزهور ودفء الكراميل، مانحاً التركيبة عمقاً ورجاحةً وقوة ثبات على الجلد."),
    ("هل عطر سكانداله مناسب للمرأة العربية؟", "نعم، تركيبته الزهرية الدافئة ذات القاعدة الكراميلية تناسب ذوق المرأة العربية التي تُقدّر العطور العميقة الغنية. القاعدة الشرقية اللطيفة تُذكّر بالعطور العربية الكلاسيكية مع لمسة غربية أنيقة."),
    ("هل يمكن للنساء الحوامل استخدام سكانداله؟", "يُفضّل استشارة الطبيب المتابع للحمل قبل استخدام أي عطر. بوجه عام، يُوصى بتجنب استخدام العطور القوية خاصةً في الثلث الأول من الحمل، والإبقاء على التهوية الجيدة عند الاستخدام."),
    ("أين يُصنع عطر كارلوتا سكانداله؟", "يُصنع عطر كارلوتا سكانداله في الصين وفق معايير عطرية دولية مضمونة الجودة. دار كارلوتا تُركّز على تقديم عطور استثنائية من حيث جودة المكونات وتطور التركيبة."),
    ("هل زجاجة 100 مل مناسبة للسفر؟", "الزجاجة بحجم 100 مل تتجاوز الحد المسموح به في أمتعة المقصورة للطائرات (75 مل)، لذا يُنصح بوضعها في الأمتعة المسجّلة أو شراء حجم تجريبي أصغر للسفر."),
    ("كيف أعرف أن العطر أصلي وليس مقلداً؟", "اشتري دائماً من صيادل ومتاجر معتمدة مثل إكليل أبها. العطر الأصلي يتمتع بثبات أعلى ورائحة متوازنة، وتأتي العبوة مع تغليف محكم وبخاخ سلس."),
    ("ما الفرق بين الشيبر والعطور الزهرية العادية؟", "عطور الشيبر الزهرية تجمع بين الزهور الطبيعية والمواد الأرضية الخشبية (كالباتشولي والأوك موس) والحمضيات، مما يُعطيها عمقاً وتعقيداً يفتقر إليه العطر الزهري البسيط الذي يُركّز على الزهور وحدها.")
]

ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

# English version
en_description = """<h2>Product Overview</h2>
<p>The <strong>Carlotta Scandal Eau de Toilette Spray for Women (100ml)</strong> is an audacious, captivating fragrance that embodies the spirit of the modern, fearless woman. Belonging to the prestigious Chypre Floral fragrance family, this sophisticated scent opens with vibrant citrus notes that unfold into a lush, romantic floral heart before settling into a deeply sensual, lasting base. It draws inspiration from iconic femininity—bold, self-assured, and unapologetically glamorous.</p>
<p>Carlotta has masterfully crafted a multi-layered olfactory experience that transitions beautifully throughout the day. The brightness of blood orange and mandarin makes a confident first impression, while honey, gardenia, jasmine, and peach create an irresistibly feminine middle chapter. The lingering warmth of beeswax, caramel, patchouli, and licorice ensures the fragrance stays close to the skin for hours—leaving a trail that is impossible to ignore.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Exceptional Longevity:</strong> The rich base of beeswax, caramel, and patchouli ensures the fragrance lingers on the skin for up to 8 hours, making it ideal for long evenings and special occasions.</li>
  <li><strong>Multi-Dimensional Scent Journey:</strong> The evolution from sparkling citrus top notes to a warm floral heart and deep, sensual base creates a living, changing fragrance experience throughout the day.</li>
  <li><strong>Distinctly Feminine Signature:</strong> Blends modern feminine boldness with classic depth, projecting a confident aura that makes a lasting impression wherever you go.</li>
  <li><strong>Chypre Floral Sophistication:</strong> The Chypre Floral category represents one of perfumery's most complex and coveted fragrance families, combining earthiness with florals for a truly distinguished scent.</li>
  <li><strong>Ideal for Evening & Special Occasions:</strong> The fragrance intensifies and blooms beautifully in warm temperatures, making it the perfect companion for sophisticated evenings and social events.</li>
  <li><strong>Elegant Presentation:</strong> The chic bottle design mirrors the daring personality of the scent within, making it an exquisite gift for any woman who appreciates luxury.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Prepare the Skin):</strong> Apply to clean, dry skin immediately after bathing when pores are open and skin is most receptive to fragrance molecules.</li>
  <li><strong>Step 2 (Target Pulse Points):</strong> Spray on warm pulse points such as the inner wrists, base of the neck, décolleté, behind the ears, and the inside of the elbows to maximize diffusion.</li>
  <li><strong>Step 3 (Optimal Distance):</strong> Hold the bottle 15-20 cm from the skin for an even, light distribution of the fragrance mist.</li>
  <li><strong>Step 4 (Do Not Rub):</strong> Never rub the wrists together after application—this breaks down the delicate top notes and alters the fragrance's intended evolution on your skin.</li>
  <li><strong>Step 5 (Proper Storage):</strong> Store the bottle away from direct light, heat, and humidity to preserve the integrity and longevity of the fragrance.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Top Notes (Blood Orange & Mandarin):</strong> These volatile citrus molecules create an immediate burst of zesty, luminous freshness that makes a vivid and energetic first statement.</li>
  <li><strong>Heart Notes (Honey, Gardenia, Orange Blossom, Jasmine & Peach):</strong> The warm honey and white florals create an opulent, sensual feminine heart, softened by the succulent sweetness of peach for a romantic and captivating core.</li>
  <li><strong>Base Notes (Beeswax, Caramel, Patchouli & Licorice):</strong> These heavy, slow-evaporating molecules anchor the fragrance to the skin for hours, providing a deeply warm, gourmand, and earthy signature that is intensely memorable.</li>
  <li><strong>Chypre Floral Family:</strong> This prestigious fragrance family balances sharpness, florals, and earthiness for a sophisticated, complex, and enduring scent profile that transcends trends.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external use only on skin; do not ingest or inhale at close range.</li>
  <li>Avoid contact with eyes and mucous membranes; rinse immediately with plenty of water if contact occurs.</li>
  <li>Do not spray directly onto delicate silk fabrics as it may cause staining.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from direct sunlight and heat sources.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>The bold, self-confident woman seeking a fragrance that reflects her extraordinary personality and magnetic femininity.</li>
  <li>Enthusiasts of sophisticated Chypre Floral fragrances who appreciate depth, complexity, and lasting projection.</li>
  <li>Perfect for evening events, cocktail parties, romantic dinners, and any occasion that calls for a glamorous, memorable presence.</li>
  <li>An exceptional gift for the woman who deserves nothing less than luxury and who appreciates the art of fine perfumery.</li>
</ul>"""

en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Carlotta</td></tr>
  <tr><th>Category</th><td>Women's Fragrances</td></tr>
  <tr><th>Product Type</th><td>Eau de Toilette - Spray</td></tr>
  <tr><th>Volume/Weight</th><td>100 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Body Fragrance)</td></tr>
  <tr><th>Finish</th><td>Captivating, lasting fragrance trail</td></tr>
  <tr><th>Texture</th><td>Fine liquid mist spray</td></tr>
  <tr><th>Fragrance</th><td>Chypre Floral - Blood Orange, Honey, Gardenia, Jasmine, Caramel, Patchouli</td></tr>
  <tr><th>Active Ingredients</th><td>Blood Orange, Mandarin, Honey, Gardenia, Orange Blossom, Jasmine, Peach, Beeswax, Caramel, Patchouli, Licorice</td></tr>
  <tr><th>Country of Origin</th><td>China</td></tr>
  <tr><th>Manufacturer</th><td>Carlotta / Giuseppe Fragrances</td></tr>
  <tr><th>Age Group</th><td>Adults 18+</td></tr>
</tbody>
</table>"""

en_kb = """<h2>The Science & Art of Women's Chypre Floral Fragrances</h2>

<h3>What problem does this solve?</h3>
<p>Carlotta Scandal addresses the challenge of finding a women's fragrance that harmonizes audacious personality with refined femininity at an accessible price point. Many women struggle to find a scent that genuinely reflects their independence and empowers their confidence in social settings while offering respectable longevity throughout the day.</p>

<h3>Why does this condition happen?</h3>
<p>Women's fragrance preferences vary enormously, and finding a single scent that adapts to different moods and occasions is genuinely challenging. Chypre Floral fragrances like Scandal address this by offering a dynamic multi-stage scent journey: an energetic opening, a romantic development, and a sensual base—all within a single spray. The Chypre structure provides that sophisticated duality of brightness and depth that most single-note fragrances simply cannot achieve.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Moisturize Before Application:</strong> Apply an unscented moisturizer before spraying, as hydrated skin retains fragrance significantly longer than dry skin.<br>
2. <strong>Timing Matters:</strong> Apply right after showering when pores are open for maximum absorption and longevity.<br>
3. <strong>Layer Thoughtfully:</strong> Use a matching or neutral-scented body lotion first to extend the fragrance's lifespan on the skin.<br>
4. <strong>Moderate Usage:</strong> Two to three sprays are sufficient for Scandal—its rich composition means over-application can become overwhelming.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Eau de Toilette always lasts less than Eau de Parfum."<br>
<strong>Fact:</strong> Longevity depends on the specific ingredients, particularly the base notes, not just the concentration level. Scandal's heavy base of beeswax, caramel, and patchouli delivers exceptional longevity that rivals many Eau de Parfum formulations.</p>
<p><strong>Myth:</strong> "Floral fragrances are only suitable for daytime."<br>
<strong>Fact:</strong> Chypre Floral fragrances like Scandal carry deep, earthy base notes that make them perfectly sophisticated and powerful for evening occasions.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Fragrance perception occurs through a biochemical reaction between volatile organic compounds (VOCs) in the formula and the olfactory receptors in the nose. The three-tier structure of Top, Heart, and Base notes corresponds to different evaporation rates determined by molecular weight. Top note molecules (citrus: Blood Orange and Mandarin) are small and light, evaporating within 15-30 minutes. Heart note molecules (Honey, Gardenia, Jasmine) are heavier and emerge over the next 1-4 hours. Base note molecules (Beeswax, Patchouli, Caramel) are the heaviest and bond with skin proteins through a process of adsorption, creating the fragrance's unique skin signature that can persist for 6-10+ hours.</p>"""

en_faqs_list = [
    ("What is Carlotta Scandal Eau de Toilette?", "Carlotta Scandal Eau de Toilette is a Chypre Floral women's fragrance featuring a sophisticated multi-stage scent journey from sparkling blood orange top notes through a lush floral heart of honey and jasmine to a deeply sensual base of beeswax, caramel, and patchouli."),
    ("What are the key fragrance notes in Carlotta Scandal?", "The top notes are blood orange and mandarin; the heart notes include honey, gardenia, orange blossom, jasmine, and peach; and the base notes feature beeswax, caramel, patchouli, and licorice—creating a rich, layered, and unforgettable olfactory experience."),
    ("Is Carlotta Scandal suitable for everyday wear?", "While it can be worn daily, its rich Chypre Floral character makes it most compelling for evenings, special occasions, and cooler months. The warm, deep base notes perform beautifully in social settings where its long-lasting trail can be fully appreciated."),
    ("How long does the fragrance last on the skin?", "Thanks to its heavy base ingredients—beeswax, patchouli, and caramel—Carlotta Scandal offers excellent longevity of approximately 6-8 hours on the skin at pulse points, with a lingering scent trail on clothing that can last even longer."),
    ("Which are the best pulse points to apply Scandal?", "The ideal application points are the inner wrists, the base of the throat, the décolleté, behind the ears, and the inside of the elbows. These areas generate body heat that activates and diffuses the fragrance molecules most effectively."),
    ("Can I spray Scandal on my clothes?", "A light application on the hems of heavier, non-delicate fabrics is acceptable, but avoid direct spraying on silk or light-colored fabrics due to potential staining from the fragrance oils. Direct skin application always provides the best olfactory experience."),
    ("Is Scandal suitable for summer or better for winter?", "The fragrance can be enjoyed year-round but truly shines in cooler weather and evening settings. In summer heat, the rich base notes amplify significantly, so use sparingly—one to two sprays is sufficient."),
    ("What age group is Carlotta Scandal best suited for?", "It is best suited for adult women aged 20 and above who appreciate bold, sophisticated, and complex fragrances. Its confident, rich character may feel too intense for very young users who prefer light, delicate scents."),
    ("How do I store my Carlotta Scandal bottle properly?", "Store the bottle upright in a cool, dry place away from direct sunlight, extreme temperatures, and humidity. Avoid storing in the bathroom where steam and heat can degrade the fragrance composition over time."),
    ("Can I layer Scandal with other fragrances?", "Yes, fragrance layering can create a unique personal scent. Apply a neutral or light base scent first, then layer Scandal on top. However, always test compatibility in small amounts first to ensure the combination is harmonious rather than conflicting."),
    ("Is Carlotta Scandal inspired by Jean Paul Gaultier Scandal?", "Yes, Carlotta Scandal is a creative interpretation inspired by the iconic Jean Paul Gaultier Scandal fragrance. It captures the spirit of the original's bold Chypre Floral identity while offering its own character at a more accessible price point."),
    ("Is Carlotta Scandal a good gift?", "Absolutely. The combination of its elegant bottle design, sophisticated scent profile, and generous 100ml volume makes it an impressive and thoughtful gift for birthdays, anniversaries, or any celebration for a woman who loves fine fragrances."),
    ("What does 'Eau de Toilette' mean?", "Eau de Toilette (EDT) is a fragrance classification indicating a concentration of aromatic compounds typically between 5-15%. It offers a lighter, fresher experience than Eau de Parfum while still providing substantial fragrance presence and longevity suitable for everyday and evening use."),
    ("Why does the same fragrance smell different on different people?", "Each person's unique skin chemistry—including natural pH levels, hormones, body temperature, and diet—interacts differently with fragrance molecules. This biochemical interaction creates a personalized 'skin scent' that makes the same perfume smell subtly unique on each individual."),
    ("Is the Carlotta Scandal safe for sensitive skin?", "People with highly sensitive skin or known fragrance allergies should perform a patch test on a small area before full application and wait 24 hours. If redness, itching, or irritation occurs, discontinue use and consult a dermatologist."),
    ("Does the fragrance perform differently in winter versus summer?", "Yes. Warmth accelerates evaporation, making summer application more powerful and diffusive. In winter, the fragrance develops more slowly and stays closer to the skin. In winter, an additional spray may be warranted, while in summer, reduction is advised."),
    ("What role does beeswax play in the base notes?", "Beeswax contributes a naturally warm, smooth, and subtly sweet animalic quality to the fragrance base. It interacts with skin warmth to gradually release a cozy, velvety depth that prolongs the overall longevity and creates a uniquely intimate skin scent."),
    ("What is patchouli and why is it used in Scandal?", "Patchouli is an essential oil derived from the Pogostemon cablin plant, valued for its rich, earthy, and slightly sweet aroma. In Scandal, patchouli serves as a critical base ingredient that adds depth, complexity, and exceptional longevity—anchoring the floral heart notes beautifully."),
    ("Is the 100ml bottle allowed in carry-on airline luggage?", "The 100ml bottle exceeds the typical 100ml (or 3.4oz) TSA/IATA limit for carry-on liquids in many airlines. It should be packed in checked luggage. A smaller travel-size decant is recommended for carry-on travel."),
    ("How can I verify this product is authentic?", "Purchase only from authorized retailers and pharmacies like Ekleel Abha. An authentic bottle has a consistent spray mechanism, correctly printed packaging with barcode details, and the fragrance itself will exhibit a balanced, evolving scent journey rather than a flat or chemical off-note."),
    ("Can pregnant or nursing women use this fragrance?", "It is generally recommended that pregnant or nursing women minimize exposure to strong fragrances, particularly during the first trimester, and consult their physician. If use is desired, application to clothing at a distance rather than directly on skin is a more conservative approach."),
    ("What is the Chypre fragrance family?", "Chypre (French for Cyprus) fragrances are a classic category built on a foundation of bergamot citrus, labdanum resin, and oakmoss. They are known for their sophisticated complexity, combining freshness, florals, and earthy depth. Chypre Floral, as in Scandal, adds a rich floral dimension to this classic structure."),
    ("Where is Carlotta Scandal manufactured?", "Carlotta Scandal Eau de Toilette is manufactured in China according to international fragrance quality standards, formulated to deliver a premium olfactory experience."),
    ("How is Eau de Toilette different from Eau de Parfum?", "Eau de Toilette typically contains 5-15% fragrance concentration while Eau de Parfum contains 15-20%. EDTs are lighter and more suited to casual and daytime wear, while EDP formulations project more intensely and last longer. Both are valid depending on personal preference and occasion."),
    ("What makes Carlotta Scandal stand out from other affordable fragrances?", "Carlotta Scandal stands out through the sophistication of its Chypre Floral composition—using premium-quality aromatic ingredients like real gardenia, jasmine absolute, and caramel accords that create a genuinely complex, multi-layered scent that competes with far more expensive designer fragrances.")
]

en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_list])

product_data = {
    "product_id": "1676",
    "sku": "EK-1676",
    "gtin": "6936711835560",
    "category": "عطور نسائية",
    "brand": "Carlotta",
    "ar": {
        "title": "بخاخ او دي تواليت سكانداله للنساء من كارلوتا، 100 مل",
        "meta_title": "عطر كارلوتا سكانداله او دي تواليت للنساء 100مل | صيدلية إكليل أبها",
        "meta_description": "اشتري عطر كارلوتا سكانداله او دي تواليت بخاخ للنساء 100 مل. رائحة شيبر زهرية فاخرة بنوتات البرتقال الدموي والعسل والكراميل. منتج أصلي من إكليل أبها.",
        "description": ar_description,
        "specifications": ar_specs,
        "knowledge_base": ar_kb,
        "faqs": ar_faqs_html,
        "tags": ["كارلوتا", "سكانداله", "عطر_نسائي", "او_دي_تواليت", "إكليل_أبها"]
    },
    "en": {
        "title": "Carlotta Scandal Eau de Toilette Spray for Women, 100ml",
        "meta_title": "Carlotta Scandal Eau de Toilette Women 100ml | Ekleel Abha",
        "meta_description": "Buy Carlotta Scandal Eau de Toilette for Women (100ml). Chypre Floral fragrance with Blood Orange, Honey, Gardenia & Caramel. 100% authentic at Ekleel Abha.",
        "description": en_description,
        "specifications": en_specs,
        "knowledge_base": en_kb,
        "faqs": en_faqs_html,
        "tags": ["carlotta", "scandal_edt", "women_fragrance", "eau_de_toilette", "ekleel_abha"]
    },
    "schema": {
        "brand": "Carlotta",
        "category": "Women's Fragrances",
        "availability": "InStock"
    },
    "image_seo": {
        "image_filename": "carlotta-scandal-eau-de-toilette-women-100ml.webp",
        "alt": "Carlotta Scandal Eau de Toilette Spray for Women 100ml",
        "title": "Carlotta Scandal Eau de Toilette Spray for Women 100ml"
    }
}

paths = [
    "e:/ai_agents/prodacts genrator/temp/generated_products/1676.json",
    "e:/ai_agents/temp/generated_products/1676.json"
]
for p in paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(product_data, f, ensure_ascii=False, indent=2)

print("Saved 1676 successfully!")
print(f"AR FAQs: {ar_faqs_html.count('<h3>')}")
print(f"EN FAQs: {en_faqs_html.count('<h3>')}")
