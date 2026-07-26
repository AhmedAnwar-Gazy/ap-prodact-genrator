import json
import os

ar_description = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد شامبو وبلسم <strong>بانتين برو-في ضد القشرة 2 في 1 (Pantene Pro-V Anti-Dandruff 2-in-1 Shampoo & Conditioner - 390 ml)</strong> حلاً متكاملاً وفعالاً للأشخاص الذين يعانون من القشرة ويرغبون في الحصول على شعر نظيف، ناعم، وقوي في خطوة واحدة عملية. تجمع هذه التركيبة المتطورة بين الفعالية الطبية المثبتة لمركب بيريثيون الزنك المضاد للفطريات والتغذية العميقة التي توفرها تقنية برو-فيتامين (Pro-V) الشهيرة من بانتين، مما يضمن التخلص من القشرة وحماية الفروة دون التضحية برطوبة الشعر ونعومته.</p>

<p>تم تصميم هذا المنتَج بعناية فائقة ليعمل كغسول مزدوج الفعالية؛ حيث ينظف فروة الرأس بعمق من الزيوت الزائدة، الإفرازات الدهنية، والتراكمات البكتيرية، وفي الوقت نفسه يغذي ألياف الشعر بلزوجة البلسم المرطب. يساعد ذلك على تقليل التقصف والتكسر الناتج عن التصفيف اليومي، ويترك الشعر سهلاً في التمشيط ومفعماً باللمعان والحيوية، مما يجعله الخيار المثالي للعناية اليومية بجميع أنواع الشعر.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>إزالة القشرة بنسبة تصل إلى 100%:</strong> يقضي على القشور البيضاء الظاهرة ويمنع إعادة ظهورها عند الاستخدام المنتظم.</li>
  <li><strong>عناية مزدوجة 2 في 1:</strong> يجمع بين قوة تنظيف الشامبو والترطيب المكثف للبلسم لتوفير الوقت والحفاظ على نعومة الشعر.</li>
  <li><strong>تقوية الشعر بتقنية Pro-V:</strong> يتغلغل برو-فيتامين B5 في ألياف الشعر لتعزيز القوة والارتقاء بمرونة الشعرة ضد التكسر.</li>
  <li><strong>تهدئة الفروة والحكة:</strong> يقلل فورياً من الحكة والتهيج المصاحب لانتشار القشرة ويمنح إحساساً بالنظافة والانتعاش.</li>
  <li><strong>تسهيل التصفيف والتمشيط:</strong> يمنع تشابك الخصلات ويترك الشعر ناعماً، حيوياً، وسهل التحكم فيه طوال اليوم.</li>
  <li><strong>تركيبة متوازنة للرعاية اليومية:</strong> مناسبة لجميع أنواع الشعر وللاستخدام المنتظم دون التسبب في جفاف الجلد أو إجهاد فروة الرأس.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل):</strong> بلي شعركِ وفروة رأسكِ جيداً بالماء الفاتر لتفتيح مسام الفروة وتسهيل تكوين الرغوة.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية مناسبة من شامبو بانتين 2 في 1 على كف اليد ووزعيها بالتساوي على فروة الرأس والشعر.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي فروة الرأس بلطف بأطراف الأصابع بحركات دائرية لمدة 2 إلى 3 دقائق لضمان وصول المادة الفعالة للجذور.</li>
  <li><strong>الخطوة الرابعة (الشطف):</strong> اشطفي الشعر جيداً بالماء الفاتر حتى إزالة الرغوة بالكامل والتأكد من عدم وجود أي بقايا شامبو.</li>
  <li><strong>الخطوة الخامسة (التكرار والمتابعة):</strong> كرري العملية إذا لزم الأمر، وللحصول على أفضل النتائج يُنصح باستخدامه 3 إلى 4 مرات أسبوعياً.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>بيريثيون الزنك (Zinc Pyrithione):</strong> مركب مضاد للفطريات والميكروبات يعمل بفعالية على كبح نمو فطريات الملاسيستية المسببة للقشرة.</li>
  <li><strong>برو-فيتامين B5 (Panthenol):</strong> يمتص داخل القشرة الداخلية للشعرة ليرطبها ويحافظ على توازن الرطوبة لمنع الجفاف والتقصف.</li>
  <li><strong>الهيستيدين (Histidine):</strong> حمض أميني مضاد للأكسدة ينفذ إلى عمق الشعرة لحمايتها من التلف الناتجة عن المعادن الموجودة بالماء.</li>
  <li><strong>الدايميثيكون (Dimethicone):</strong> عامل تكييف سيليكوني يخلق طبقة واقية خفيفة تحمي الشعر من الجفاف وتزيد من اللمعان والنعومة.</li>
  <li><strong>عوامل التنظيف اللطيفة (Sodium Laureth Sulfate):</strong> توفر رغوة غنية تنظف الأوساخ والدهون العالقة بالفروة بكفاءة عالية دون تهييج.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>هذا المنتج مخصص للاستخدام الخارجي على الشعر وفروة الرأس فقط؛ يُمنع ابتلاعه.</li>
  <li>تجنبي ملامسة الشامبو للعينين؛ وفي حالة ملامستهما اشطفيهما فوراً بكمية وفيرة من الماء النظيف.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن أشعة الشمس المباشرة.</li>
  <li>في حال ظهور أي علامات تحسس شديد أو تهيج غير عادي على فروة الرأس، توقفي عن الاستخدام واستشيري طبيب الجلدية.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>للأشخاص الذين يعانون من قشرة الرأس الظاهرة والحكة المزعجة المصاحبة لها بشكل مستمر.</li>
  <li>لمن يبحثون عن حل سرييع وعملي يجمع بين الشامبو والبلسم في منتج واحد للروتين اليومي.</li>
  <li>لأصحاب الشعر الذي يميل للجفاف عند استخدام شامبوهات القشرة التقليدية ويحتاج ترطيباً مضاعفاً.</li>
  <li>مناسب للرجال والنساء ولجميع أنواع الشعر العادي والدهني والمصبوغ.</li>
</ul>"""

ar_specifications = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بانتين (Pantene)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / شامبو ضد القشرة</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو وبلسم 2 في 1 مضاد للقشرة</td></tr>
  <tr><th>الحجم/الوزن</th><td>390 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر / الفروة المعرضة للقشرة</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر نظيف، خالي من القشرة، ناعم وقوي</td></tr>
  <tr><th>الملمس</th><td>كريمي سائل</td></tr>
  <tr><th>العطر</th><td>منعش (رائحة بانتين المميزة)</td></tr>
  <tr><th>المكونات النشطة</th><td>بيريثيون الزنك (Zinc Pyrithione)، برو-فيتامين B5</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / السويد</td></tr>
  <tr><th>الشركة المصنعة</th><td>بروكتر آند جامبل (Procter & Gamble)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين فوق 12 سنة</td></tr>
</tbody>
</table>"""

ar_knowledge_base = """<h2>الدليل المعرفي لعلاج قشرة الرأس والعناية بالفروة</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج شامبو بانتين 2 في 1 ضد القشرة مشكلة القشرة الجلدية (Dandruff) وما يرافقها من حكة ومظهر غير مرغوب فيه للقشور البيضاء المتساقطة على الملابس. كما أنه يقدم حلاً مشكلة الجفاف والخشونة التي تسببها غسولات القشرة العادية، حيث يعيد توازن الرطوبة للشعر والفروة في آن واحد.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تنشأ القشرة بشكل رئيسي بسبب النمو المفرط لفطر مجهري طبيعي يعيش على فروة الرأس يُعرف باسم <strong>الملاسيستية (Malassezia)</strong>. يغذي هذا الفطر على الزيوت الدهنية (الزهم) التي تفرزها الغدد الدهنية في الفروة، ويحللها إلى أحماض دهنية متهيجة تؤدي إلى تسارع تجدد خلايا الجلد وتساقطها على شكل قشور بيضاء. تزداد هذه الحالة عند تراكم الزيوت، التوتر العصبي، والتقلبات المناخية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام المنتظم:</strong> استعملي شامبو مضاد للقشرة من 3 إلى 4 مرات أسبوعياً للحد من تكاثر الفطريات.<br>2. <strong>تجنب الماء الساخن:</strong> اغسلي شعرك بالماء الفاتر لتجنب تحفيز الغدد الدهنية وإثارة التهيج.<br>3. <strong>تدليك لطيف:</strong> استخدمي وسائد الأصابع بدلاً من الأظافر لتجنب إحداث جروح ميكروبية بالفروة.<br>4. <strong>تقليل منتجات التصفيف الثقيلة:</strong> قللي من استخدام الجيل والشمع التي تراكم الدهون وتخلق بيئة خصبة للفطريات.</p>

<h3>خرافات شائعة حول القشرة والعناية بالشعر</h3>
<p><strong>خرافة:</strong> "القشرة تنتج عن قلة النظافة الشخصية فقط."<br><strong>الحقيقة:</strong> القشرة حالة استجابة بيولوجية لتكاثر فطريات الملاسيستية وتفاعل الجلد مع الأحماض الدهنية، وتحدث حتى مع الأشخاص الذين يغسلون شعرهم يومياً.</p>
<p><strong>خرافة:</strong> "استخدام شامبو القشرة يسبب تساقط الشعر ويجففه."<br><strong>الحقيقة:</strong> شامبوهات القشرة الحديثة المدعمة بالبلسم مثل بانتين 2 في 1 تحتوي على برو-فيتامين B5 ومواد تكييف تحمي الشعر من الجفاف وتقويه ضد التساقط الناتج عن التكسر.</p>

<h3>التفسير العلمي لآلية العمل (بيريثيون الزنك وبرو-فيتامين B5)</h3>
<p>يعتمد المنتج على مركب <strong>بيريثيون الزنك (Zinc Pyrithione)</strong> الذي يعمل كعامل مضاد للفطريات ميكروبي واسع الطيف، حيث يثبط امتصاص المغذيات داخل خلايا فطر الملاسيستية مما يؤدي لتقليل إعدادها وإعادة فروة الرأس إلى حالتها الطبيعية الصحيه. وفي نفس الوقت، يخترق مركب <strong>برو-فيتامين B5 (البارثينول)</strong> طبقة القشرة في ساق الشعرة، محولاً إياه إلى حمض البانتوثينيك الذي يزيد من قدرة الشعر على احتجاز الماء وتعزيز مرونته ضد المؤثرات الخارجية.</p>"""

# Generate 25 FAQs in AR
ar_faqs_list = [
    ("ما هو شامبو بانتين برو-في ضد القشرة 2 في 1؟", "هو شامبو وبلسم مدمج مصمم طبياً وعناية يومية للتخلص من القشرة وتنظيف فروة الرأس مع ترطيب ألياف الشعر وتقويتها بتقنية برو-فيتامين B5."),
    ("هل يحتوي الشامبو على مركب مضاد للقشرة مثبت علمياً؟", "نعم، يحتوي الشامبو على مركب بيريثيون الزنك (Zinc Pyrithione) الفعال والذي يقضي على الفطريات المسببة للقشرة ويمنع تكاثرها."),
    ("ما الميزة في كون المنتج 2 في 1 (شامبو وبلسم)؟", "تتيح لك تركيبة 2 في 1 تنظيف الفروة من القشرة والدهون وفي الوقت نفسه ترطيب الشعر وتنعيمه، مما يغنيك عن استخدام بلسم مستقل ويختصر وقت الاستحمام."),
    ("هل هذا الشامبو يناسب جميع أنواع الشعر؟", "نعم، تم تطوير التركيبة لتناسب كافة أنواع الشعر سواء العادي، الدهني، الجاف، أو المصبوغ."),
    ("كم مرة ينبغي استخدام الشامبو في الأسبوع للحصول على نتائج ملحوظة؟", "يُنصح باستخدامه من 3 إلى 4 مرات أسبوعياً للحصول على أفضل نتائج في القضاء على القشرة والحفاظ على فروة رأس صحية."),
    ("هل يسبب شامبو بانتين ضد القشرة جفافاً للشعر؟", "لا، بفضل احتوائه على بلسم مدعم ببرو-فيتامين B5 والمرطبات، فإنه يحافظ على رطوبة الشعر ويحميه من الجفاف بعكس الشامبوهات التقليدية."),
    ("هل يساعد المنتج في تقليل حكة فروة الرأس؟", "نعم، يهدئ المنتج الفروة فورياً ويقلل الحكة والتهيج الناجم عن نشاط الفطريات القشرية."),
    ("هل هذا الشامبو آمن للشعر المصبوغ؟", "نعم، التركيبة متوازنة الحموضة ولطيفة، وهي آمنة للاستخدام على الشعر المعالج بالألوان دون أن تسبب بهتان الصبغة."),
    ("هل يمكن للرجال والنساء استخدام بانتين 2 في 1؟", "بالتأكيد، المنتج مناسب لكلا الجنسين ولكل من يعاني من مشكلة قشرة الرأس وترقق الشعر أو جفافه."),
    ("كيف يعمل مركب برو-فيتامين B5 في الشامبو؟", "يتغلغل برو-فيتامين B5 داخل ساق الشعرة ليحبس الرطوبة ويعزز مرونة الخصلات وقوتها ضد التكسر والتقصف."),
    ("هل يقضي بانتين 2 في 1 على القشرة بشكل نهائي؟", "يقضي على القشرة الظاهرة بنسبة 100% مع الاستخدام المنتظم، ويحافظ على الفروة صحية وخالية من القشرة طالما واصلت استخدامه ضمن روتينك."),
    ("ما حجم هذه العبوة؟", "تأتي هذه العبوة بحجم 390 مل، وهو حجم عائلي واقتصادي يكفي للاستخدام المنتظم لفترة طويلة."),
    ("هل يمكن استخدام المنتج يومياً؟", "نعم، شامبو بانتين 2 في 1 يتميز بتركيبة لطيفة ومتوازنة تسمح بالاستخدام اليومي دون إلحاق الضرر بفروة الرأس."),
    ("هل يترك الشامبو رائحة طيبة في الشعر؟", "نعم، يتميز برائحة بانتين الانتعاشية الكلاسيكية الممتعة التي تدوم طوال اليوم وتمنحك شعوراً بالنظافة."),
    ("ما هي الطريقة المثالية لتطبيق الشامبو؟", "ضعي الشامبو على شعر مبلل ودلكي فروة الرأس بأطراف الأصابع لمدة 2-3 دقائق ثم اشطفيه جيداً بالماء الفاتر."),
    ("هل يلزم استخدام بلسم إضافي بعد هذا الشامبو؟", "لا حاجة لاستخدام بلسم إضافي لأن التركيبة تحتوي بالفعل على البلسم المغذي، ولكن يمكن لأصحاب الشعر الشديد الجفاف استخدام بلسم لا يُشطف إن رغبوا."),
    ("هل يسبب هذا الشامبو تساقط الشعر؟", "على العكس، القضاء على القشرة والتهابات الفروة يقلل من تساقط الشعر الناجم عن الحكة، وتقنية برو-فيتامين تقوي الشعر ضد التكسر."),
    ("ما الفرق بين بانتين 2 في 1 وشامبوهات القشرة الأخرى؟", "بانتين 2 في 1 يجمع بين العلاج الفعال للقشرة والنعومة الفائقة للبلسم، فلا يترك الشعر خشناً أو متشابكاً بعد الاستحمام."),
    ("هل يمكن استخدام المنتج للأطفال؟", "يُوصى باستخدامه للأطفال والمراهقين فوق سن 12 سنة. للأطفال الأصغر سناً، يُفضل استخدام منتجات مخصصة للأطفال."),
    ("ما المكونات النشطة المسؤولة عن تنظيف الفروة؟", "يحتوي على عوامل تنظيف متوازنة مثل الصوديوم لوريث سلفات وكوكاميدوبروبيل بيتين التي تكتنف الدهون والأوساخ وتزيلها بفاعلية."),
    ("ما هو الهيستيدين وما فائدته بالشامبو؟", "الهيستيدين هو حمض أميني مضاد للأكسدة يخترق الشعرة ويحميها من التلف والأكسدة الناتجة عن المعادن الضارة بالماء."),
    ("ماذا أفعل إذا دخل الشامبو في عيني؟", "يجب غسل العينين فوراً بكمية وفيرة من الماء النظيف البارد حتى يزول شعور الحرقة."),
    ("هل يساعد الشامبو في التحكم بالزيوت الزائدة بالفروة؟", "نعم، ينظف الدهون الزائدة ويعيد توازن الإفرازات الزهمية بالفروة دون أن يجردها من مرطباتها الطبيعية."),
    ("أين يتم تصنيع هذا المنتج؟", "تم تصنيع المنتج بواسطة شركة بروكتر آند جامبل العالمية (P&G) وفق أعلى معايير الجودة والمواصفات المعتمدة."),
    ("هل المنتج أصلي ومضمون في صيدلية إكليل أبها؟", "نعم، جميع المنتجات المتوفرة في صيدلية إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين بالمملكة العربية السعودية.")
]

ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in ar_faqs_list])

# English Content
en_description = """<h2>Product Overview</h2>
<p>The <strong>Pantene Pro-V Anti-Dandruff 2-in-1 Shampoo & Conditioner (390 ml)</strong> offers a complete, clinically validated solution for individuals experiencing dandruff who refuse to compromise on hair softness and strength. Formulated with the dual power of proven anti-fungal Zinc Pyrithione and Pantene's signature Pro-Vitamin B5 complex, this 2-in-1 formula eliminates up to 100% of visible flakes while restoring optimal moisture balance to both the scalp and hair strands.</p>

<p>Engineered for effortless daily application, this multi-action wash deeply cleanses the scalp of excess sebum, dirt, and environmental pollutants, while simultaneously depositing weightless conditioning agents. It smooths the hair cuticle, prevents styling damage, and detangles tresses instantly. The result is flake-free, vibrant, and resilient hair that feels soft to the touch and smells fresh all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Up to 100% Flake Elimination:</strong> Effectively removes visible dandruff flakes and prevents their recurrence with regular use.</li>
  <li><strong>Dual 2-in-1 Convenience:</strong> Combines a deep-cleansing shampoo with a rich conditioner in one simple step to save time while preserving hair moisture.</li>
  <li><strong>Pro-V Hair Fortification:</strong> Infuses strands with Pro-Vitamin B5, reinforcing hair structural integrity against mechanical breakage.</li>
  <li><strong>Instant Scalp Soothing:</strong> Relieves scalp itching, irritation, and tightness from the very first wash, delivering lasting freshness.</li>
  <li><strong>Silky Smoothness & Detangling:</strong> Prevents knots and tangles, leaving hair manageable, soft, and naturally shiny.</li>
  <li><strong>Gentle Daily Formula:</strong> pH-balanced and formulated to be gentle enough for daily use on all hair types, including color-treated hair.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet Hair):</strong> Thoroughly wet your hair and scalp with lukewarm water to open hair cuticles and prepare for cleansing.</li>
  <li><strong>Step 2 (Apply Shampoo):</strong> Dispense an adequate amount of Pantene 2-in-1 shampoo into your palms and distribute evenly across scalp and hair.</li>
  <li><strong>Step 3 (Massage Scalp):</strong> Gently massage the scalp with your fingertips (avoiding fingernails) in circular motions for 2 to 3 minutes to activate ingredients.</li>
  <li><strong>Step 4 (Rinse Thoroughly):</strong> Rinse hair completely with lukewarm water until all lather is removed and hair feels clean.</li>
  <li><strong>Step 5 (Repeat & Maintain):</strong> Repeat if necessary. For best results, use consistently 3 to 4 times a week as part of your regular hair care regimen.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Zinc Pyrithione:</strong> A potent, clinically proven anti-fungal active ingredient that inhibits Malassezia yeast proliferation on the scalp.</li>
  <li><strong>Pro-Vitamin B5 (Panthenol):</strong> Penetrates deep into the hair shaft cortex to seal in essential moisture and improve elasticity.</li>
  <li><strong>Histidine:</strong> An antioxidant amino acid that penetrates the hair core to protect against mineral-induced oxidative stress.</li>
  <li><strong>Dimethicone:</strong> A premium conditioning polymer that coats hair fibers with a featherlight protective film for enhanced shine and detangling.</li>
  <li><strong>Gentle Cleansing Surfactants:</strong> Formulated with Sodium Laureth Sulfate to create a luxurious lather that removes dirt and oil without harsh stripping.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external use on hair and scalp only; do not swallow.</li>
  <li>Avoid direct contact with eyes. If contact occurs, rinse immediately and thoroughly with clean water.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from direct sunlight.</li>
  <li>If severe skin irritation or allergic reactions develop on the scalp, discontinue use immediately and consult a dermatologist.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Individuals dealing with stubborn dandruff, visible white flakes, and persistent scalp itchiness.</li>
  <li>People seeking a convenient, time-saving 2-in-1 shampoo and conditioner for their daily hair care routine.</li>
  <li>Those whose hair gets dry or frizzy when using traditional anti-dandruff shampoos and need extra moisturizing care.</li>
  <li>Suitable for men and women with all hair types, including normal, oily, dry, and color-treated hair.</li>
</ul>"""

en_specifications = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Pantene</td></tr>
  <tr><th>Category</th><td>Hair Care / Anti-Dandruff Shampoo</td></tr>
  <tr><th>Product Type</th><td>Anti-Dandruff 2-in-1 Shampoo & Conditioner</td></tr>
  <tr><th>Volume/Weight</th><td>390 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types / Scalp Prone to Dandruff</td></tr>
  <tr><th>Finish</th><td>Clean, Flake-Free, Smooth & Strong Hair</td></tr>
  <tr><th>Texture</th><td>Liquid Cream</td></tr>
  <tr><th>Fragrance</th><td>Fresh Signature Pantene Scent</td></tr>
  <tr><th>Active Ingredients</th><td>Zinc Pyrithione, Pro-Vitamin B5 (Panthenol)</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / Sweden</td></tr>
  <tr><th>Manufacturer</th><td>Procter & Gamble</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens 12+</td></tr>
</tbody>
</table>"""

en_knowledge_base = """<h2>Clinical Insights on Dandruff Control & Hair Resilience</h2>

<h3>What problem does this solve?</h3>
<p>Pantene Pro-V Anti-Dandruff 2-in-1 Shampoo addresses persistent dandruff (seborrheic dermatitis flaking), scalp itchiness, and irritation. Additionally, it solves the common issue of hair dryness and stiffness caused by harsh medicated shampoos by integrating deep conditioning nutrients into the washing step.</p>

<h3>Why does this condition happen?</h3>
<p>Dandruff is primarily triggered by the overgrowth of a naturally occurring scalp fungus called <strong>Malassezia</strong>. This yeast feeds on the natural sebum produced by scalp hair follicles, breaking it down into oleic acid. In sensitive individuals, this causes micro-inflammation, accelerating epidermal cell turnover and resulting in visible white dead skin flakes. Factors like excess oil, stress, and weather changes exacerbate this imbalance.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Regular Cleansing:</strong> Wash hair with an effective anti-dandruff formula 3-4 times a week to keep Malassezia yeast populations controlled.<br>2. <strong>Avoid Hot Water:</strong> Use lukewarm water to avoid stimulating hyper-sebum production and causing scalp dryness.<br>3. <strong>Gentle Scalp Massage:</strong> Always use fingertips instead of fingernails to prevent micro-abrasions on the scalp.<br>4. <strong>Minimize Heavy Styling Products:</strong> Limit heavy waxes and gels that trap sebum and foster fungal growth.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Dandruff is caused solely by poor hygiene."<br><strong>Fact:</strong> Dandruff is a biological response to fungal activity and individual sensitivity to sebum breakdown, occurring regardless of cleanliness.</p>
<p><strong>Myth:</strong> "Anti-dandruff shampoos always dry out and damage your hair."<br><strong>Fact:</strong> Advanced 2-in-1 formulations like Pantene incorporate Pro-Vitamin B5 and conditioning lipids that protect hair softness and fortify hair fibers against breakage while eradicating flakes.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>This formulation operates through a dual-action mechanism. <strong>Zinc Pyrithione (ZPT)</strong> serves as a broad-spectrum antifungal agent that disrupts nutrient transport across Malassezia fungal cell membranes, inhibiting yeast cell division and restoring scalp microbiome equilibrium. Simultaneously, <strong>Pro-Vitamin B5 (Panthenol)</strong> penetrates the hair cortex where it converts into pantothenic acid, increasing water retention within the hair shaft and reinforcing structural elasticity against environmental stress.</p>"""

en_faqs_list = [
    ("What is Pantene Pro-V Anti-Dandruff 2-in-1 Shampoo?", "It is a clinically tested 2-in-1 shampoo and conditioner engineered to eliminate dandruff, cleanse the scalp, and deeply hydrate hair strands with Pro-Vitamin B5 in a single step."),
    ("Does this shampoo contain a proven anti-dandruff active ingredient?", "Yes, it contains Zinc Pyrithione (ZPT), a clinically proven anti-fungal agent that targets and inhibits the yeast responsible for dandruff."),
    ("What are the main advantages of a 2-in-1 formula?", "A 2-in-1 formula combines the deep cleansing power of a shampoo with the smoothing benefits of a conditioner, saving shower time while keeping hair soft and manageable."),
    ("Is Pantene Anti-Dandruff 2-in-1 suitable for all hair types?", "Yes, it is designed to work effectively across all hair types, including straight, wavy, curly, fine, thick, oily, or dry hair."),
    ("How often should I use this shampoo for best results?", "It is recommended to use it 3 to 4 times per week to effectively manage dandruff and maintain a healthy, flake-free scalp."),
    ("Will this anti-dandruff shampoo make my hair dry?", "No. Unlike harsh medicated cleansers, Pantene 2-in-1 includes rich conditioning agents and Pro-Vitamin B5 that lock in moisture and preserve softness."),
    ("Does this product help relieve scalp itching?", "Yes, it provides immediate relief from scalp itching, irritation, and discomfort associated with dandruff from the very first wash."),
    ("Is this shampoo safe for color-treated hair?", "Yes, it features a pH-balanced, gentle formula that cleanses without prematurely stripping hair color or causing dullness."),
    ("Can both men and women use Pantene Anti-Dandruff 2-in-1?", "Absolutely. It is a unisex product formulated for anyone suffering from scalp flaking or looking for a nourishing anti-dandruff wash."),
    ("How does Pro-Vitamin B5 benefit the hair?", "Pro-Vitamin B5 penetrates into the hair cortex to bind moisture, smooth the cuticle, and increase tensile strength against styling breakage."),
    ("Does Pantene 2-in-1 permanently cure dandruff?", "It eliminates up to 100% of visible flakes with regular use. Continuous use keeps the scalp microbiome balanced and prevents flakes from returning."),
    ("What is the volume of this shampoo bottle?", "This bottle contains 390 ml of product, providing a generous amount suitable for extended regular family use."),
    ("Can I use this 2-in-1 shampoo daily?", "Yes, the formula is gentle and balanced enough for daily cleansing without drying out the scalp or weighting down hair."),
    ("Does it leave a pleasant scent on the hair?", "Yes, it features Pantene's signature fresh fragrance that leaves hair smelling clean and refreshed throughout the day."),
    ("What is the recommended application method?", "Apply to wet hair, gently massage into the scalp for 2-3 minutes to allow active ingredients to penetrate, then rinse thoroughly with lukewarm water."),
    ("Do I need to apply a separate conditioner afterwards?", "No separate conditioner is required since the 2-in-1 formula already incorporates conditioning agents. However, those with extremely dry ends may add a leave-in treatment if desired."),
    ("Can this shampoo cause hair loss?", "No. In fact, controlling scalp inflammation and itching reduces hair shed caused by scratching, while Pro-V nutrients strengthen hair against breakage."),
    ("How does Pantene 2-in-1 differ from standard anti-dandruff shampoos?", "Standard anti-dandruff shampoos can leave hair feeling coarse. Pantene 2-in-1 delivers dual anti-dandruff efficacy and salon-quality hair softness."),
    ("Is this product suitable for children?", "It is recommended for adults and teenagers aged 12 and above. For younger children, pediatric hair care products are recommended."),
    ("What cleansing agents are used in this shampoo?", "It uses balanced surfactants such as Sodium Laureth Sulfate and Cocamidopropyl Betaine to lift away excess oil, dirt, and dead skin cells effectively."),
    ("What role does Histidine play in the formula?", "Histidine is an antioxidant amino acid that penetrates the hair core to neutralize damaging copper minerals found in tap water."),
    ("What should I do if the shampoo gets into my eyes?", "Flush your eyes immediately with plenty of clean, cool water until any stinging sensation subsides."),
    ("Does this shampoo help control excess scalp oil?", "Yes, it thoroughly washes away excess sebum without over-drying, helping maintain optimal scalp sebum balance."),
    ("Where is this Pantene product manufactured?", "It is manufactured by Procter & Gamble (P&G) adhering to international quality and safety standards."),
    ("Is this product authentic at Ekleel Abha Pharmacy?", "Yes, all products offered at Ekleel Abha Pharmacy are 100% original and sourced directly from authorized distributors in Saudi Arabia.")
]

en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_list])

product_data = {
    "product_id": "6148",
    "sku": "EK-6148",
    "gtin": "8700216392785",
    "category": "العناية بالشعر / شامبو ضد القشرة",
    "brand": "Pantene",
    "ar": {
        "title": "بانتين شامبو برو-في ضد القشرة 2 في 1 - 390 مل",
        "meta_title": "بانتين شامبو وبلسم 2 في 1 ضد القشرة 390مل | صيدلية إكليل أبها",
        "meta_description": "تسوق بانتين شامبو برو-في ضد القشرة 2 في 1 (390 مل) للقضاء على القشرة والحصول على شعر ناعم ومغذي. منتج أصلي 100% متوفر لدى صيدلية إكليل أبها بالسعودية.",
        "description": ar_description,
        "specifications": ar_specifications,
        "knowledge_base": ar_knowledge_base,
        "faqs": ar_faqs_html,
        "tags": ["بانتين", "شامبو_ضد_القشرة", "2في1", "العناية_بالشعر", "إكليل_أبها", "pantene"]
    },
    "en": {
        "title": "Pantene Pro-V Anti-Dandruff 2-in-1 Shampoo - 390 ml",
        "meta_title": "Pantene Pro-V Anti-Dandruff 2-in-1 Shampoo 390ml | Ekleel Abha",
        "meta_description": "Buy Pantene Pro-V Anti-Dandruff 2-in-1 Shampoo & Conditioner (390 ml). Eliminates flakes & nourishes hair with Pro-V formula. 100% original at Ekleel Abha.",
        "description": en_description,
        "specifications": en_specifications,
        "knowledge_base": en_knowledge_base,
        "faqs": en_faqs_html,
        "tags": ["pantene", "anti_dandruff", "2in1_shampoo", "hair_care", "ekleel_abha", "pro_v"]
    },
    "schema": {
        "brand": "Pantene",
        "category": "Hair Care / Anti-Dandruff Shampoo",
        "availability": "InStock"
    },
    "image_seo": {
        "image_filename": "pantene-pro-v-anti-dandruff-2-in-1-shampoo-390ml.webp",
        "alt": "Pantene Pro-V Anti-Dandruff 2-in-1 Shampoo 390 ml",
        "title": "Pantene Pro-V Anti-Dandruff 2-in-1 Shampoo 390 ml"
    }
}

paths_to_save = [
    "e:/ai_agents/prodacts genrator/temp/generated_products/6148.json",
    "e:/ai_agents/temp/generated_products/6148.json"
]

for p in paths_to_save:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(product_data, f, ensure_ascii=False, indent=2)

print("Saved product 6148 successfully to both paths!")
