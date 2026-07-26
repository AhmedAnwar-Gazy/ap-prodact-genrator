import json
import os

ar_description = """<h2>نظرة عامة على المنتج</h2>
<p>تُعتبر <strong>شفرات فلامنجو للتحديد وإزالة شعر الوجه والحواجب (Feather Flamingo Eyebrow & Facial Touch-up Razors)</strong> المستوردة من اليابان الأداة الاحترافية الأولى والأكثر شهرة عالمياً لإزالة الشعر الوبري الدقيق (Peach Fuzz) وتقشير الوجه الفيزيائي اللطيف (Dermaplaning). صُممت هذه الشفرات بعناية فائقة من قِبل شركة "فيذر" اليابانية الرائدة في صناعة الأدوات الطبية والجراحية الدقيقة، حيث تجمع بين الحدة الاستثنائية والأمان التام، مما يتيح لك الحصول على بشرة ملساء ناعمة ومشرقة كالحرير في راحة منزلك دون التسبب في أي تهيج أو جروح.</p>
<p>تتميز كل شفرة في هذا الطقم المكون من 3 قطع بتكنولوجيا التغليف البلاتيني المزدوج للفولاذ المقاوم للصدأ (Platinum-Coated Stainless Steel)، المجهزة بشبكة واقي أمان ميكرو (Micro Safety Guard) مبتكرة. تمنع هذه الشبكة الدقيقة الاحتكاك المباشر الحاد مع الجلد وتمنع الانزلاق الجانبي المسبب للجروح، مما يجعلها مثالية لتشكيل ورسم الحواجب بدقة متناهية، والتخلص من شعر الشفة العليا والخدين والذقن، بالإضافة إلى إزالة خلايا الجلد الميتة المتراكمة على السطح. بفضل المقبض المريح المصمم بانحناءة انسيابية، تضمن لك شفرات فلامنجو حلاقة آمنة ومتحكم بها تماماً لتجديد نضارة البشرة وتعزيز امتصاص مستحضرات العناية بنسبة مضاعفة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تقشير ديرمابلاننج (Dermaplaning) احترافي:</strong> تفرك وتقشر الطبقة السطحية من الخلايا الميتة والشوائب، مما يمنح البشرة ملمساً حريرياً ونضارة فورية.</li>
  <li><strong>إزالة دقيقة للشعر الوبري الناعم:</strong> تتخلص من شعر الوجه الخفيف بفاعلية وسلاسة دون ترك جذور حادة أو التسبب في نمو الشعر تحت الجلد.</li>
  <li><strong>شبكة واقي أمان ميكرو لحماية البشرة:</strong> مزودة بأغطية أمان دقيقة تحمي البشرة الحساسة من النكش والجروح والخدوش أثناء الحركة.</li>
  <li><strong>فولاذ ياباني مغلف بالبلاتين المقاوم للصدأ:</strong> تضمن حوافاً فائقة الحدة والتعقيم تقطع الشعرة بنظافة تامّة مع الحفاظ على متانة الشفرة لعدة استخدامات.</li>
  <li><strong>تحسين الامتصاص وتطبيق المكياج:</strong> تزيل العوائق السطحية لتمكين السيرومات والمقشرات من التغلغل العميق، وتضمن توزيع كريم الأساس بدون تكتل.</li>
  <li><strong>تصميم انسيابي دقيق ومريح:</strong> يوفر مقبضاً مموجاً يمنع الانزلاق ويضمن تحكماً كاملاً لضبط زوايا رسم الحواجب والمناطق الضيقة.</li>
  <li><strong>طقم اقتصادي وعملي من 3 قطع:</strong> يأتي بألوان جذابة ومتنوعة مع غطاء حماية شفاف لكل شفرة لسهولة التنقل والحفظ الآمن داخل حقيبة المكياج.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>تجهيز وتنظيف البشرة:</strong> اغسلي وجهك جيداً بغسول لطيف لإزالة جميع التراكمات والمكياج، ثم جففي البشرة تماماً. يمكن استخدام الشفرة على بشرة جافة كلياً أو تطبيق قطرة من زيت الوجه الخفيف لسهولة الانزلاق.</li>
  <li><strong>شد الجلد وتحديد الزاوية:</strong> استخدمي يدك غير الممسكة بالشفرة لشد الجلد المراد حلاقته برفق، وامسكي شفرة فلامنجو بزاوية مائلة تتراوح بين 30 إلى 45 درجة بالنسبة لسطح الجلد.</li>
  <li><strong>الحركات القصيرة واللطيفة:</strong> مرري الشفرة لأسفل باتجاه نمو الشعر باستخدام ضربات قصيرة ولطيفة جداً دون الضغط بقوة على البشرة.</li>
  <li><strong>العناية بالحواجب والمناطق الدقيقة:</strong> استخدمي طرف الشفرة الدقيق لتحديد قوس الحاجب وإزالة الشعر الزائد بين العينين وفوق الشفة العليا ببطء وحذر.</li>
  <li><strong>التنظيف والتطبييب بعد الحلاقة:</strong> امسحي الشفرة بقطعة قطن مبللة بالكحول المطهر وأعيدي غطاء الأمان الشفاف. اغسلي وجهك بماء فاتر ثم طبقي مرطباً مهدئاً (مثل البانثينول أو الصبار) وزيت البشرة المغذي، وتجنبي مقشرات المقشر الكيميائي (AHA/BHA) لمدة 24 ساعة.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>فولاذ ياباني مقاوم للصدأ (Japanese Stainless Steel):</strong> معدن طبي وعالي الجودة يوفر حافة قطع فائقة الحدة، مقاومة للتآكل والأكسدة لضمان أقصى درجات النظافة والسلامة.</li>
  <li><strong>طبقة البلاتين الواقية (Platinum Coating):</strong> تقنية تغليف ميكروية تزيد من نعومة انزلاق المعدن على الجلد وتمنع الاحتكاك القاسي المسبب للاحمرار.</li>
  <li><strong>شبكة واقي الأمان (Micro Safety Guard Mesh):</strong> حواجز معدنية دقيقة جداً موزعة على طول الشفرة لمنع الشفرة من الانغراس العميق أو جرح طبقات الجلد الحية.</li>
  <li><strong>بوليمر عالي الكثافة (Medical-Grade Resin Polymer):</strong> بلاستيك مقاوم للبكتيريا ومصمم بشكل مريح ليمنح المقبض خفة الوزن والملمس الثابت لمنع الانزلاق أثناء الاستخدام.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>الشفرات مخصصة للاستخدام الشخصي الفردي فقط؛ يمنع مشاركتها بتاتاً لمنع نقل العدوى البكتيرية أو الفيروسية.</li>
  <li>لا تُستخدم الشفرة على مناطق الحبوب النشطة، البثور، الجروح المفتوحة، حروق الشمس، أو مناطق التهاب الأكزيما والصدفية.</li>
  <li>يجب الحذر الشديد عند التعامل مع الشفرات الحادة وحفظها دائماً بالغطاء الواقي بعيداً عن متناول الأطفال.</li>
  <li>تجنبي استخدام المقشرات القوية أو الأحماض المنشطة (الريتينول، حامض الجليكوليك) قبل أو بعد الحلاقة مباشرة لتجنب التخريش الشديد.</li>
  <li>يُوصى بالتخلص من الشفرة واستبدالها بعد 3 إلى 5 استخدامات أو بمجرد الشعور بعدم حدتها لمنع شد الشعر أو جرح الجلد.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>السيدات والفتيات اللاتي يبحثن عن وسيلة سريعة، غير مؤلمة، وآمنة تماماً لإزالة شعر الوجه وتشكيل الحواجب في المنزل.</li>
  <li>الراغبات في الحصول على جلسات تقشير الديرمابلاننج (Dermaplaning) المنزلية لإزالة الجلد الميت وتحسين ملمس البشرة.</li>
  <li>من يعانين من تكتل المكياج أو كريم الأساس بسبب الشعر الوبري وترغبن في مظاهر مكياج صافية ومخملية.</li>
  <li>أصحاب البشرة الحساسة التي تتأثر بالوسائل التقليدية كالشمع أو الخيط وتعاني من التورم والاحمرار الشديد.</li>
</ul>"""

ar_specifications = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>Feather Flamingo</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / أدوات إزالة الشعر</td></tr>
  <tr><th>نوع المنتج</th><td>شفرات تحديد وتقشير الوجه (Dermaplaning)</td></tr>
  <tr><th>الحجم/الوزن</th><td>طقم 3 شفرات</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ملساء خالية من الشعر الوبري والخلايا الميتة</td></tr>
  <tr><th>الملمس</th><td>شفرات فائقة الحدة بنمط ميكرو مع مقبض مريح وقابل للطي</td></tr>
  <tr><th>العطر</th><td>خالي من العطور</td></tr>
  <tr><th>المكونات النشطة</th><td>فولاذ مقاوم للصدأ مغلف بالبلاتين، واقي أمان ميكرو</td></tr>
  <tr><th>بلد المنشأ</th><td>اليابان</td></tr>
  <tr><th>الشركة المصنعة</th><td>Feather Safety Razor Co., Ltd.</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين</td></tr>
</tbody>
</table>"""

ar_knowledge_base = """<h2>الدليل المعرفي الطبي والعلمي لشفرات فلامنجو للتحديد وتقشير الوجه</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج شفرات فلامنجو مشكلة تراكم الشعر الوبري الخفيف (Peach Fuzz) وخلايا الجلد الميتة الجافة على سطح البشرة، وهي المشكلة التي تجعل مظهر الوجه باهتاً وتمنع الالتصاق المتجانس لكريم الأساس وتعيق نفاذ المواد المغذية في مستحضرات العناية. كما تمنح حلاً آمناً وسريعاً للفتيات والسيدات اللاتي يعانين من الألم والاحمرار الشديد الناجم عن وسائل إزالة الشعر التقليدية مثل الشمع والخيط، وتوفر بديلاً دقيقاً لتشكيل الحواجب وتحديدها دون التأثير على مرونة الجلد.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تحدث هذه المشكلة فسيولوجياً نتيجة للتجدد الخلوي الطبيعي حيث تتراكم خلايا الطبقة القرنية (Stratum Corneum) الميتة على السطح بشكل مستمر، متحدة مع الزيوت الطبيعية وبصيلات الشعر الوبري المتواجدة بكثرة في منطقة الوجه والرقبة. هذا التراكم يخلق حاجزاً غير منتظم يعكس الضوء بشكل غير متناسق فيظهر الوجه بشعور ناعم مفقود ومظهر غير متجانس، كما يمتص السيرومات والكريمات ويمنعها من الوصول إلى طبقات الجلد العميقة.</p>

<h3>نصائح وقائية</h3>
<ul>
  <li><strong>التقشير الفيزيائي المنتظم:</strong> اعتمدي جلسة تقشير لطيفة بشفرات فلامنجو مرة كل 2 إلى 3 أسابيع للتخلص من التراكمات دون إرهاق حاجز البشرة.</li>
  <li><strong>التنظيف والتعقيم الدائم:</strong> نظفي الشفرة بكحول إيزوبروبيل 70% قبل وبعد كل استخدام لمنع انتقال البكتيريا وتكون البثور.</li>
  <li><strong>استخدام زاوية آمنة (30-45 درجة):</strong> لا تجعلي الشفرة عمودية أبداً على الجلد أثناء الحلاقة لتجنب الجروح والتخريش الميكانيكي.</li>
  <li><strong>الترطيب الفوري ومنع الكيماويات:</strong> طبقي مرطباً خافضاً للتهيج يحتوي على السيراميد أو البانثينول وتجنبي الأحماض القوية لمدة 24 ساعة بعد التقشير.</li>
  <li><strong>توفير الحماية الشمسية المطلقة:</strong> استخدمي واقي شمس واسع الطيف (SPF 50+) يومياً لأن البشرة المقشرة تكون أكثر حساسية للأشعة فوق البنفسجية.</li>
</ul>

<h3>خرافات شائعة</h3>
<ul>
  <li><strong>خرافة:</strong> "حلاقة شعر الوجه بالشفرة تجعل الشعر ينمو بكثافة أكبر ولون أغمق وسُمك أكثر."<br><strong>الحقيقة:</strong> هذا المفهوم خاطئ تماماً علمياً؛ الشفرة تقطع الجزء الخارجي من الشعرة فقط دون التأثير على البصيلة أو الجينات المسؤولة عن لون وسُمك الشعر. يظهر الشعر فقط بملمس مدبب مؤقتاً عند بداية نموه.</li>
  <li><strong>خرافة:</strong> "شفرات الوجه تسبب ترهل الجلد وتمدده على المدى الطويل."<br><strong>الحقيقة:</strong> تقنية الديرمابلاننج بشفرات فلامنجو اللطيفة لا تسحب الجلد أو تُمطه بعكس الشمع والخيط، بل تحفز الدورة الدموية السطحية وتنشط تجدد الخلايا.</li>
  <li><strong>خرافة:</strong> "يمكن استخدام أي شفرة حلاقة عادية مخصصة للجسم لإزالة شعر الوجه."<br><strong>الحقيقة:</strong> شفرات الجسم تفتقر إلى واقي الأمان الميكروي وتتميز بزوايا حادة لا تتناسب مع رقة وبشرة الوجه الحساسة، مما يسبب الجروح والالتهابات.</li>
</ul>

<h3>التفسير العلمي</h3>
<p>تعتمد آلية عمل تقشير الديرمابلاننج بشفرات Feather Flamingo على الإزالة الميكانيكية الدقيقة للطبقة القرنية (Stratum Corneum) والشعر الوبري غير المتصبغ. يحتوي نسيج الشفرة المصنوع من الفولاذ البلاتيني على واقي ميكروي مقسم هندسياً يوزع الضغط بالتساوي على السطح، مما يقلل قوة القشط على الخلايا الحية أسفل الغشاء القاعدي. تحفز هذه العملية الإشارة الخلوية الطبيعية لإفراز الكولاجين والإيلاستين، وتزيل الميكروبات الضارة المحتبسة في زغبات الشعر، مما يرفع كفاءة النفاذية الجلدية (Transdermal Delivery) للمركبات النشطة بنسبة تصل إلى 40%.</p>"""

# Generate 25 Detailed FAQs for Arabic
ar_faqs_list = [
    ("س1: ما هي شفرات فلامنجو اليابانية للتحديد؟", "شفرات فلامنجو هي أدوات تجميلية يابانية احترافية مصممة خصيصاً لإزالة شعر الوجه والحواجب الدقيق وتقشير الخلايا الميتة. تتميز بشفرات فولاذية مقاومة للصدأ ومغلفة بالبلاتين مزودة بشبكة حماية ميكرو لضمان حلاقة آمنة وسلسة بدون جروح."),
    ("س2: هل تجعل شفرات فلامنجو شعر الوجه ينمو بكثافة أكبر أو بسُمك أكثر؟", "لا إطلاقاً، هذا المفهوم غير صحيح علمياً. الحلاقة السطحية بالشفرة تزيص الجزء الظاهر من الشعر دون التأثير على الجذر أو بصيلة الشعرة، وبالتالي يعود الشعر للنمو بنفس سمكه ولونه وطبيعته الأصلية دون أي زيادة في الكثافة."),
    ("س3: ما الفرق بين شفرات فلامنجو وشفرات الحلاقة العادية للجسم؟", "تمتلك شفرات فلامنجو تصميماً مخصصاً لبشرة الوجه الحساسة مع واقي أمان ميكروي يمنع انغراس الشفرة في الجلد. بينما تفتقر شفرات الجسم لهذه التكنولوجيا وتكون حادة جداً وتسبب الخدوش والجروح عند استخدامها على ملامح الوجه الدقيقة."),
    ("س4: ما هي فوائد تقشير الديرمابلاننج (Dermaplaning) باستخدام هذه الشفرات؟", "يقوم تقشير الديرمابلاننج بإزالة خلايا الجلد الميتة والشعر الوبري، مما يمنح البشرة ملمساً حريرياً ناعماً، ويقلل من شحوب الوجه، ويسمح لمستحضرات العناية بالسيروم والمرطب بالتغلغل الفعال، كما يجعل تطبيق كريم الأساس سهلاً ومتجانساً."),
    ("س5: ما هي الزاوية الصحيحة لاستخدام الشفرة على بشرة الوجه؟", "يجب إمالة الشفرة بزاوية 30 إلى 45 درجة تقريباً بالنسبة لسطح الجلد. تضمن هذه الزاوية قطع الشعر والجلد الميت بانسيابية كاملة وبأقل قدر من الاحتكاك، مع تجنب جعل الشفرة عمودية تماماً بزاوية 90 درجة لعدم جرح البشرة."),
    ("س6: هل يُفضل استخدام الشفرة على بشرة جافة أم مبللة؟", "يمكن استخدام شفرات فلامنجو على بشرة جافة تماماً ونظيفة للحصول على أفضل نتائج تقشير، أو تطبيق قطرة من زيت الوجه المغذي (مثل زيت الجوجوبا) لتوفير طبقة انزلاق إضافية للبشرة الجافة أو الحساسة للغاية."),
    ("س7: كم مرة يمكنني إعادة استخدام شفرة فلامنجو الواحدة؟", "يمكن استخدام الشفرة الواحدة من 3 إلى 5 مرات بحسب سمك الشعر ومساحة المنطقة، بشرط تنظيفها وتعقيمها جيداً بعد كل استخدام. ويُفضل استبدال الشفرة فور الشعور بقلة حدتها لضمان عدم شد الشعر."),
    ("س8: كيف أقوم بتعقيم وتنظيف الشفرة بعد الانتهاء من الاستخدام؟", "بعد كل حلاقة، امسحي الشفرة برفق بقطعة قطن مبللة بكحول إيزوبروبيل تركيز 70%، ثم اتركيها لتجف في الهواء تماماً قبل تغطيتها بالغطاء الواقي الشفاف. تجنبي مسح حد الشفرة بقوة بقماش خشن لعدم إتلاف شبكة الأمان."),
    ("س9: هل يمكن استخدام شفرات فلامنجو في حال وجود حب الشباب أو البثور؟", "يجب تجنب تمرير الشفرة إطلاقاً فوق البثور وحبوب الشباب النشطة أو الجروح، لأن ذلك قد يؤدي إلى فتح البثور وتفريغها ونقل البكتيريا إلى مناطق أخرى من الوجه. يمكن الحلاقة بعناية حول المناطق السليمة فقط."),
    ("س10: ما هي خطوات العناية بالبشرة الواجب اتباعها بعد استخدام الشفرة؟", "بعد إزالة الشعر، اغسلي وجهك بماء فاتر وطبقي سيروم أو كريم مهدئ يرتكز على الصبار، البانثينول، أو السيراميد لترطيب وتسكين الجلد. احرصي على تجنب المقشرات الكيميائية والأحماض القوية لمدة 24 ساعة."),
    ("س11: هل تسبب شفرات فلامنجو أي ألم أو احمرار؟", "العملية خالية تماماً من الألم مقارنة بالشمع أو الخيط. قد يظهر احمرار خفيف جداً ومؤقت لدى أصحاب البشرة الحساسة للغاية، لكنه يزول خلال دقائق معدودة عند وضع كريم مرطب ومهدئ."),
    ("س12: هل يمكن استخدام الشفرة لتحديد رسمة الحواجب؟", "نعم، تعتبر شفرات فلامنجو الأداة المثالية لتحديد وتنسيق الحواجب بدقة عالية بفضل رأسها النحيف، حيث تتيح لك إزالة الشعيرات الدقيقة بين العينين وفوق وتحت قوس الحاجب بكل سهولة وسيطرة."),
    ("س13: ما دور واقي الأمان الميكرو (Micro Safety Guard) المدمج بالشفرة؟", "واقي الأمان الميكرو عبارة عن بروزات وحواجز دقيقة جداً من الفولاذ تغطي حد الشفرة، وظيفتها منع التلامس القاسي المباشر مع الجلد وحمايته من الخدوش والانزلاقات الجانبية، مما يوفر حماية فائقة للبشرة الحساسة."),
    ("س14: هل تناسب شفرات فلامنجو جميع أنواع البشرة؟", "نعم، تناسب الشفرات جميع أنواع البشرة بما في ذلك البشرة العادية، الجافة، الدهنية، والمختلطة. لكن يجب على صاحبات البشرة الملتهبة شديدة الحساسية تجريبها بحذر على منطقة صغيرة أولاً."),
    ("س15: كم مرة يُنصح بعمل تقشير الديرمابلاننج للوجه بالشفرة أسبوعياً أو شهرياً؟", "يُنصح بإجراء تقشير شامل للوجه مرة كل 2 إلى 4 أسابيع، وهي الفترة الطبيعية التي تحتاجها خلايا البشرة للتجدد. بينما يمكن استخدام الشفرة لتحديد الحواجب والشعر الزائد كلما دعت الحاجة."),
    ("س16: هل تساعد الشفرات في التخلص من الرؤوس السوداء أو المسام المسدودة؟", "تساعد الشفرات بشكل غير مباشر عن طريق إزالة الطبقة السطحية من الخلايا الميتة والزيوت والشعر الذي يحبس الدهون داخل المسام، مما يسهل تنظيف المسام ويمنع انسدادها مستقبلاً."),
    ("س17: هل يمكن وضع المكياج فوراً بعد استخدام شفرات فلامنجو؟", "يُفضل الانتظار لمدة ساعة على الأقل أو إجراء الحلاقة ليلاً قبل النوم لإعطاء البشرة فرصة للاسترخاء. بعد ذلك ستلاحظين أن المكياج ينساب بنعومة فائقة وبدون أي تكتل على البشرة."),
    ("س18: ما هي المادة المصنوع منها حد الشفرة؟", "حد الشفرة مصنوع من الفولاذ الياباني المقاوم للصدأ المغلف بطبقة بلاتينية عالي الجودة والمعالج طعن الأكسدة، مما يضمن حدة مستمرة ونظافة طبية فائقة أثناء الاستخدام."),
    ("س19: هل يصح مشاركة الشفرة مع شخص آخر إذا تم تعقيمها؟", "لا يجوز مشاركة شفرات الوجه بتاتاً مع أي شخص آخر حتى بعد التعقيم، حيث تعتبر أدوات عناية شخصية فردية لتجنب مخاطر نقل العدوى والميكروبات الجلدية دقيقة الحجم."),
    ("س20: كيف تساهم شفرات فلامنجو في تحسين نضارة البشرة الشاحبة؟", "تزيل الشفرات الطبقة المتأكسدة والرمادية من الخلايا الميتة التي تحجب الضوء، مما يكشف عن طبقة جلد جديدة وصحية تحتها تعكس الضوء بوضوح وتظهر البشرة بمظهر نضر ومشرق."),
    ("س21: هل يمكن استخدام الشفرة لإزالة شعر المناطق الأخرى كالجسم أو اليدين؟", "شفرات فلامنجو مخصصة في الأصل للوجه والحواجب والرقبة، ولكن يمكن استخدامها للمناطق الدقيقة بالجسم. إلا أن مساحتها الصغرى تخدم الوجه بشكل أفضل وأسرع."),
    ("س22: كيف أحافظ على سلامة الشفرة ومنع صدئها عند الحفظ؟", "احفظي الشفرات دائماً في مكان جاف بعيداً عن رطوبة الحمام، وتأكدي من تجفيفها تماماً وتركيب الغطاء الواقي الشفاف عليها بعد التعقيم بالكحول لحمايتها من الغبار والتلف."),
    ("س23: هل تسبب الشفرات ظهور حبوب تحت الجلد؟", "على العكس تماماً، الحلاقة السطحية بشفرات فلامنجو تقطع الشعر عند مستوى سطح الجلد دون اقتلاعه من الجذور، مما يقلل فرص انغراس الشعر ونموه تحت الجلد مقارنة بالشمع والأجهزة الكهربائية."),
    ("س24: هل الشفرة قابلة للطي أم تأتي بغطاء ثابت؟", "تأتي شفرات فلامنجو الأصلية بتصميم مريح مزود بغطاء أمان شفاف يتم تركيبه على الرأس لحماية الشفرة وضمان السلامة التامة أثناء التخزين والتنقل."),
    ("س25: لماذا تُعتبر شفرات فلامنجو الخيار الأول الموصى به في صيدلية إكليل أبها؟", "توفر صيدلية إكليل أبها شفرات فلامنجو اليابانية الأصلية لضمان أعلى معايير الجودة والأمان لبشرتك، حيث تقدم حلاً طبياً وتجميلياً متكاملاً لإزالة شعر الوجه والتقشير بأسعار مناسبة ونتائج مضمونة.")
]

ar_faqs_html = '<div class="faqs-container">\n'
for q, a in ar_faqs_list:
    ar_faqs_html += f'  <div class="faq-item">\n    <h3>{q}</h3>\n    <p>{a}</p>\n  </div>\n'
ar_faqs_html += '</div>'


en_description = """<h2>Product Overview</h2>
<p>The <strong>Feather Flamingo Facial & Eyebrow Touch-up Razors (3-Piece Set)</strong> imported directly from Japan represents the gold standard in precise facial hair removal and home dermaplaning technology. Precision-engineered by Feather Safety Razor Co., Ltd.—a global leader in surgical-grade and medical cutlery—these high-performance razors combine exceptional sharpness with maximum skin safety. Designed specifically for delicate facial contours, they effortlessly remove fine vellus hair (peach fuzz) and gently exfoliate the outermost layer of dead skin cells, leaving your complexion instantly smooth, radiant, and silky.</p>
<p>Each razor within this convenient 3-pack features a Japanese platinum-coated stainless steel blade integrated with a specialized Micro Safety Guard mesh. This advanced guard structure creates a protective barrier between the razor's edge and your skin, preventing lateral slippage, minor nicks, and mechanical irritation. Ideal for defining eyebrows, shaping upper lip lines, clearing cheek fuzz, and rejuvenating dull skin, the ergonomic handle provides superior leverage and fingertip control. Incorporating Feather Flamingo razors into your routine enhances skin texture, promotes cellular turnover, and dramatically improves skincare product penetration and seamless makeup application.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Professional At-Home Dermaplaning:</strong> Gently sweeps away dead skin cells and environmental debris to uncover a luminous, ultra-smooth facial canvas.</li>
  <li><strong>Precise Vellus Hair Removal:</strong> Safely cuts fine facial peach fuzz without pulling, tugging, or causing painful ingrown hairs.</li>
  <li><strong>Micro Safety Guard System:</strong> Features fine protective stainless steel wire mesh along the blade edge to safeguard sensitive skin against cuts and scratches.</li>
  <li><strong>Platinum-Coated Japanese Stainless Steel:</strong> Crafted with surgical-grade metal that resists corrosion, maintains long-lasting sharpness, and ensures hygienic precision.</li>
  <li><strong>Enhanced Skincare Absorption & Makeup Prep:</strong> Eliminates surface barriers, allowing serums and moisturizers to absorb deeper while foundation glides on flawlessly.</li>
  <li><strong>Ergonomic Non-Slip Handle Design:</strong> Contoured handle offers optimum grip, stability, and maneuverability for detailing intricate areas like eyebrow arches.</li>
  <li><strong>Hygienic 3-Piece Pack with Caps:</strong> Includes 3 distinct pastel-colored razors, each equipped with a clear snap-on safety cover for safe storage and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Cleanse & Dry Facial Skin:</strong> Thoroughly wash your face with a mild cleanser to remove surface oils, sweat, and cosmetics. Gently pat skin completely dry. For extra slip, you may apply a few drops of lightweight facial oil.</li>
  <li><strong>Taut Skin & Angle Alignment:</strong> Use your non-dominant hand to pull the target skin area taut. Hold the Feather Flamingo razor handle at a 30 to 45-degree angle relative to the skin surface.</li>
  <li><strong>Light, Short Downward Strokes:</strong> Gliding gently with minimal pressure, employ short downward strokes in the direction of hair growth to shave fuzz and exfoliate dead cells.</li>
  <li><strong>Detailing Eyebrows & Fine Contours:</strong> Carefully maneuver the precision tip to line eyebrow arches, touch up between the brows, and clear hair around the upper lip and chin.</li>
  <li><strong>Post-Shave Care & Sanitization:</strong> Wipe the blade clean with a 70% isopropyl alcohol cotton pad and snap on the protective cover. Wash face with lukewarm water, apply a soothing moisturizer (containing panthenol or aloe vera), and refrain from using harsh chemical exfoliants (AHAs/BHAs) for 24 hours.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Japanese Medical-Grade Stainless Steel:</strong> High-purity alloy providing unmatched edge retention, corrosion resistance, and surgical-level cleanliness.</li>
  <li><strong>Micro Platinum Coating:</strong> Ultra-thin platinum protective film applied to the blade edge to reduce surface friction and prevent skin drag and redness.</li>
  <li><strong>Micro Safety Guard Mesh:</strong> Fine perpendicular steel safety wires spaced precisely across the blade to buffer sharp contact and eliminate nicking.</li>
  <li><strong>High-Density Polymer Resin:</strong> Lightweight, durable, antibacterial plastic forming the ergonomic handle for comfortable, slip-free control.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For individual personal care use only. Never share razors with others to avoid cross-contamination of bacteria or skin infections.</li>
  <li>Do not use on active acne breakouts, open wounds, inflamed pimples, sunburned skin, eczema patches, or cold sores.</li>
  <li>Exercise caution when handling sharp blades; keep protective safety covers secured and store out of reach of children.</li>
  <li>Avoid applying strong chemical exfoliants, retinoids, or alcohol-based astringents immediately before or after dermaplaning to prevent severe irritation.</li>
  <li>Replace the razor after 3 to 5 uses or as soon as the blade feels dull or drags against the skin to maintain optimal hygiene and safety.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Women and individuals seeking an effortless, painless, and safe method for facial hair touch-ups and eyebrow shaping at home.</li>
  <li>Anyone desiring smooth, bright skin through gentle physical dermaplaning exfoliation without salon costs.</li>
  <li>Makeup enthusiasts looking to prevent foundation caking, dry patches, and uneven texture caused by fine peach fuzz.</li>
  <li>Individuals with sensitive skin who experience irritation, swelling, or ingrown hairs from waxing, threading, or epilators.</li>
</ul>"""

en_specifications = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Feather Flamingo</td></tr>
  <tr><th>Category</th><td>Personal Care / Shaving & Hair Removal</td></tr>
  <tr><th>Product Type</th><td>Facial Dermaplaning Razors</td></tr>
  <tr><th>Volume/Weight</th><td>3-Piece Pack</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types</td></tr>
  <tr><th>Finish</th><td>Smooth, clear skin free from peach fuzz and dead cells</td></tr>
  <tr><th>Texture</th><td>Ultra-sharp micro-guard steel blade with folding ergonomic handle</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-Free</td></tr>
  <tr><th>Active Ingredients</th><td>Platinum-Coated Stainless Steel, Micro Guard</td></tr>
  <tr><th>Country of Origin</th><td>Japan</td></tr>
  <tr><th>Manufacturer</th><td>Feather Safety Razor Co., Ltd.</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens</td></tr>
</tbody>
</table>"""

en_knowledge_base = """<h2>Medical & Scientific Knowledge Base for Feather Flamingo Facial Razors</h2>

<h3>What problem does this solve?</h3>
<p>Feather Flamingo Facial Razors address the accumulation of microscopic vellus hair (peach fuzz) and dead stratum corneum skin cells on the facial skin surface. This build-up creates a dull, uneven skin barrier that reflects light poorly, traps facial oils, prevents smooth makeup application, and restricts deep penetration of active skincare ingredients. Additionally, these razors offer a painless, non-invasive alternative to traditional hair removal methods like waxing or threading, which frequently induce skin trauma, erythema, and follicular damage.</p>

<h3>Why does this condition happen?</h3>
<p>Facial dullness and rough texture occur as part of natural cutaneous physiological processes. Desquamation—the shedding of dead skin cells—slows down due to aging, environmental pollution, and climate exposure. Simultaneously, fine vellus hair follicles continuously grow across the cheeks, jawline, upper lip, and forehead. When dead keratinocytes adhere to these fine hairs alongside sebum, they form an irregular surface layer that dims natural radiance and causes cosmetic products to cling unevenly.</p>

<h3>Prevention Tips</h3>
<ul>
  <li><strong>Perform Regular Dermaplaning:</strong> Integrate gentle facial dermaplaning once every 2 to 4 weeks to keep the skin barrier clear and facilitate cell renewal.</li>
  <li><strong>Sanitize Blade Before & After Use:</strong> Clean the stainless steel blade with 70% isopropyl alcohol to eliminate lingering bacteria and mitigate breakout risks.</li>
  <li><strong>Maintain a 30-45 Degree Shaving Angle:</strong> Never hold the razor perpendicular (90 degrees) to the skin to avoid accidental micro-cuts and scraping injuries.</li>
  <li><strong>Post-Exfoliation Barrier Support:</strong> Apply soothing, humectant-rich formulations containing ceramide, panthenol, or hyaluronic acid immediately post-shave.</li>
  <li><strong>Apply Broad-Spectrum Sunscreen Daily:</strong> Protect freshly exfoliated epidermal layers with SPF 50+ to guard against heightened UV sensitivity.</li>
</ul>

<h3>Common Myths</h3>
<ul>
  <li><strong>Myth:</strong> "Shaving facial hair with a razor causes hair to grow back thicker, darker, and faster."<br><strong>Fact:</strong> This is a persistent biological myth. Shaving shears the hair shaft at the skin's surface without modifying the hair follicle or genetic parameters controlling thickness, color, or growth rate. Hair grows back with its natural diameter.</li>
  <li><strong>Myth:</strong> "Facial dermaplaning razors cause skin sagging and premature loss of elasticity."<br><strong>Fact:</strong> Unlike waxing or threading which forcibly stretch and pull the skin, gentle dermaplaning glides smoothly over the surface without mechanical tension, actually supporting microcirculation.</li>
  <li><strong>Myth:</strong> "Standard body razors work just as well for facial dermaplaning."<br><strong>Fact:</strong> Body razors lack specialized micro-safety guards and feature aggressive blade angles that can severely nick, cut, and irritate delicate facial tissue.</li>
</ul>

<h3>Scientific Explanation</h3>
<p>The dermatological mechanism of Feather Flamingo razors relies on controlled micro-exfoliation of the stratum corneum alongside physical vellus hair removal. The Japanese stainless steel edge, enhanced with platinum coating and micro-guard wire meshing, distributes cutting force uniformly across the epidermal surface. This prevents mechanical trauma while removing non-pigmented vellus hair shafts and hyperkeratinized cellular debris. Consequently, epidermal cell signaling promotes healthy regeneration, clears trapped follicular debris, and enhances the transdermal absorption efficiency of active topical ingredients by up to 40%.</p>"""

# Generate 25 Detailed FAQs for English
en_faqs_list = [
    ("Q1: What are Feather Flamingo Touch-up Razors?", "Feather Flamingo Razors are professional Japanese facial grooming tools specifically designed for gentle eyebrow shaping, vellus hair (peach fuzz) removal, and facial dermaplaning. Made with platinum-coated stainless steel and micro-safety guards, they offer safe and smooth hair removal at home."),
    ("Q2: Does shaving facial hair with Flamingo razors make hair grow back thicker or darker?", "No, absolutely not. Shaving cuts hair at the surface level without altering the internal hair root, follicle, or genetic composition. As the hair regrows, it retains its original texture, color, and density without becoming thicker or coarser."),
    ("Q3: How do Feather Flamingo razors differ from standard body razors?", "Feather Flamingo razors are engineered specifically for delicate facial skin. They feature fine micro-safety wire guards across the blade edge to prevent cuts, and a sleek, narrow head that provides precise control around facial contours unlike bulky body razors."),
    ("Q4: What are the benefits of home dermaplaning with these razors?", "Dermaplaning with Flamingo razors gently exfoliates dead surface skin cells and removes fine peach fuzz. This uncovers a smooth, glowing complexion, enhances the deep absorption of serums and moisturizers, and allows foundation makeup to glide on flawlessly."),
    ("Q5: What is the correct angle to hold the razor against the face?", "Hold the razor at approximately a 30 to 45-degree angle relative to your skin. This optimal angle allows the sharp platinum edge to glide smoothly over hair and dead skin cells without scraping or digging into the skin surface."),
    ("Q6: Should I use the razor on dry or wet skin?", "Feather Flamingo razors work exceptionally well on clean, completely dry skin for precise dermaplaning. Alternatively, if you have very dry or sensitive skin, applying a few drops of lightweight facial oil provides additional slip and comfort."),
    ("Q7: How many times can I reuse a single Flamingo razor?", "Each razor can typically be reused 3 to 5 times depending on hair density and facial area covered. Be sure to clean and sanitize the blade after each session, and replace it as soon as you feel any dullness or drag."),
    ("Q8: How should I sanitize and clean the razor after use?", "After shaving, gently wipe the blade with a cotton pad saturated in 70% isopropyl alcohol to eliminate surface microbes. Allow it to air-dry completely before snapping on the clear protective cover. Avoid wiping hard with towels to preserve the guard."),
    ("Q9: Can I use Flamingo razors if I have active acne or pimples?", "No, you should avoid shaving directly over active acne breakouts, inflamed pimples, or open wounds. Shaving over blemishes can pop them, spread bacteria across the face, and cause scarring. Carefully shave around clear skin areas only."),
    ("Q10: What post-shave skincare routine should I follow after dermaplaning?", "Rinse your face with cool or lukewarm water, pat dry, and apply a soothing, non-comedogenic moisturizer enriched with aloe vera, panthenol, or ceramides. Avoid potent chemical exfoliants (AHAs, BHAs) and retinol for at least 24 hours."),
    ("Q11: Do Feather Flamingo razors cause pain or severe skin redness?", "No, shaving with Flamingo razors is completely painless compared to waxing or threading. Minor temporary redness may occur in extremely sensitive skin types, but it subsides quickly upon applying a hydrating, soothing moisturizer."),
    ("Q12: Can these razors be used for shaping eyebrows accurately?", "Yes, Feather Flamingo razors are renowned for precision eyebrow styling. The slender blade head allows you to carefully trim stray hairs above, below, and between the brows to define sharp, elegant arches with complete control."),
    ("Q13: How does the Micro Safety Guard technology protect the skin?", "The Micro Safety Guard consists of ultra-fine perpendicular wire ridges integrated across the blade edge. This mesh buffers the sharp blade contact, preventing direct skin gouging and side slips, ensuring a safe experience even for beginners."),
    ("Q14: Are Feather Flamingo razors suitable for all skin types?", "Yes, they are suitable for normal, dry, oily, and combination skin types. However, individuals with severe inflammatory skin conditions like rosacea, active eczema, or severe cystic acne should refrain from shaving affected areas."),
    ("Q15: How often should I perform full facial dermaplaning?", "Full facial dermaplaning is recommended once every 2 to 4 weeks, coinciding with the natural cell turnover cycle of your skin. Spot touch-ups for eyebrow shaping can be done weekly as needed."),
    ("Q16: Do these razors help unclog pores and reduce blackheads?", "Yes, by removing dead skin cells and vellus hair that trap sebum and surface debris, dermaplaning prevents clogged pores and reduces the formation of blackheads and dull surface buildup over time."),
    ("Q17: Can I apply makeup immediately after dermaplaning?", "It is best to wait at least 1 hour or dermaplane in the evening before bed to let your skin rest. Afterwards, you will notice foundation and concealer blend effortlessly without caking on facial fuzz or dry flakes."),
    ("Q18: What materials are used to manufacture the blade?", "The blade is manufactured in Japan from high-grade surgical stainless steel, coated with a micro-thin layer of platinum to ensure anti-corrosion properties, hygiene, and lasting edge sharpness."),
    ("Q19: Is it safe to share my Flamingo razors with family or friends?", "No, facial razors are personal care tools and should never be shared, even if sanitized. Sharing razors poses a significant risk of transmitting microscopic skin bacteria and viral infections."),
    ("Q20: How do Flamingo razors enhance skin radiance and glow?", "By removing the oxidized layer of dead keratinized cells and fine hair that casts subtle shadows on the face, the razors reveal fresh, healthy skin underneath that reflects light evenly for a natural glow."),
    ("Q21: Can I use these razors for hair removal on other body parts?", "While designed specifically for facial contours, eyebrows, and neck area, they can be used for small, delicate body spots. However, dedicated body razors are better suited for larger areas like legs and arms."),
    ("Q22: How should I store the razors to ensure longevity and safety?", "Store your Flamingo razors in a dry area outside of moist bathroom environments. Ensure the blade is thoroughly sanitized, dried, and covered with its transparent safety cap after every use."),
    ("Q23: Will dermaplaning cause ingrown hairs on the face?", "Unlike waxing or epilating which pulls hair from below the surface, Flamingo razors shear hair cleanly at the skin level. This significantly reduces the likelihood of developing painful ingrown hairs."),
    ("Q24: Does the pack come with protective safety covers for each razor?", "Yes, the 3-piece pack includes individual clear snap-on safety covers for each razor head, ensuring total safety during storage in your makeup bag or while traveling."),
    ("Q25: Why choose Feather Flamingo razors from Ekleel Abha Pharmacy?", "Ekleel Abha Pharmacy guarantees 100% authentic Japanese Feather Flamingo razors, offering customer assurance of original medical-grade quality, competitive prices, and reliable delivery across KSA.")
]

en_faqs_html = '<div class="faqs-container">\n'
for q, a in en_faqs_list:
    en_faqs_html += f'  <div class="faq-item">\n    <h3>{q}</h3>\n    <p>{a}</p>\n  </div>\n'
en_faqs_html += '</div>'

data = {
  "product_id": "1867",
  "sku": "EK-1867",
  "category": "العناية الشخصية / أدوات إزالة الشعر",
  "brand": "Flamingo",
  "ar": {
    "title": "شفرات فلامنجو للتحديد وإزالة شعر الوجه والحواجب 3 قطع",
    "meta_title": "شفرات فلامنجو للتحديد 3 قطع | صيدلية إكليل أبها",
    "meta_description": "تسوقي شفرات فلامنجو الأصلية 3 قطع للتحديد الدقيق وإزالة شعر الوجه والحواجب بلطف. مزودة بواقي أمان لحماية البشرة. أطلبيها من إكليل أبها.",
    "description": ar_description,
    "specifications": ar_specifications,
    "knowledge_base": ar_knowledge_base,
    "faqs": ar_faqs_html,
    "tags": ["flamingo", "شفرات_فلامنجو", "تحديد_الحواجب", "ديرمابلاننج", "إكليل_أبها"]
  },
  "en": {
    "title": "Feather Flamingo Facial & Eyebrow Razors - 3 Pieces",
    "meta_title": "Feather Flamingo Touch-Up Razors 3-Pack | Ekleel Abha",
    "meta_description": "Buy original Feather Flamingo 3-pack facial razors for gentle dermaplaning and precise eyebrow shaping. Platinum coated with safety guard. Fast KSA shipping.",
    "description": en_description,
    "specifications": en_specifications,
    "knowledge_base": en_knowledge_base,
    "faqs": en_faqs_html,
    "tags": ["flamingo", "facial_razor", "dermaplaning", "ekleel_abha"]
  },
  "schema": {
    "brand": "Feather Flamingo",
    "Category": "Personal Care / Shaving & Hair Removal",
    "availability": "InStock"
  },
  "image_seo": {
    "image_filename": "feather-flamingo-facial-eyebrow-razors-3pcs.webp",
    "alt": "Feather Flamingo Facial & Eyebrow Razors 3 Pieces",
    "title": "Feather Flamingo Facial & Eyebrow Razors 3 Pieces"
  }
}

output_path = r"e:\ai_agents\prodacts genrator\temp\generated_products\1867.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved successfully to", output_path)
