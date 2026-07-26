import json, os

def create_product_1694():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مرطب البشرة المتعدد الاستخدامات من إيجيبشن ماجيك (Egyptian Magic All-Purpose Skin Cream - 118 ml)</strong> أسطورة عالمية في عالم العناية بالبشرة والجمال. يعتمد هذا الكريم الأيقوني على سر تركيب الفراعنة القدامى والمكون من 6 مكونات طبيعية 100% مستخلصة من الخلية ومنتجات النحل وزيت الزيتون دون أي إضافات كيميائية أو مواد حافظة، مما يجعله بلسم الترطيب السحري الأكثر شهرة بين مشاهير العالم وخبراء العناية بالبشرة.</p>
<p>يمتاز الكريم بقوام بلسم دافئ يتحول عند فركه بين اليدين إلى زيت مغذٍ يذوب داخل ألياف الجلد، ليمنح ترطيباً مكثفاً وتهدئة فورية للتشققات والجفاف والالتهابات. يُستخدم كريم إيجيبشن ماجيك كمرطب للوجه، كريم للعينين، بلسم للشفاه، معالج لتقصف أطراف الشعر، مرطب للجسم، ومهدئ لتهيج البشرة بعد الحلاقة أو التعرض للشمس.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تركيبة طبيعية 100%:</strong> خالية تماماً من الكيمياويات والبارابين والمواد الحافظة والعطور الصناعية.</li>
  <li><strong>6 مكونات سحرية فقط:</strong> زيت زيتون نقي، شمع العسل، العسل، غذاء ملكات النحل، صمغ النحل (بروبوليس)، وحبوب لقاح النحل.</li>
  <li><strong>مرطب شمول متعدد الاستخدامات:</strong> يصلح للوجه، الجسم، الشفاه، الشعر، الأظافر، والحروق والجروح البسيطة.</li>
  <li><strong>تهدئة سريعة للتشققات والجفاف:</strong> يرمم حاجز البشرة المجهد ويمنح ترطيباً عميقاً يستمر لعدة أيام.</li>
  <li><strong>إصلاح الشعر المتقصف:</strong> يمنح أطراف الشعر رطوبة ولمعاناً مذهلاً دون ثقل.</li>
  <li><strong>آمن ومجرب جلدياً:</strong> آمن تماماً للبشرة الأكثر حساسيات ومناسب للأطفال والنساء الحوامل.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (أخذ الكمية):</strong> خذي كمية صغيرة جداً من البلسم الصلب بأطراف أصابعك.</li>
  <li><strong>الخطوة الثانية (التدفئة والتذويب):</strong> افركي البلسم بين كفيكِ لعدة ثوانٍ حتى يتحول فورياً إلى زيت ناعم.</li>
  <li><strong>الخطوة الثالثة (التطبيق):</strong> وزعي الزيت بلطف على المنطقة المطلوبة (الوجه، الشفاه، الأكواع، أطراف الشعر).</li>
  <li><strong>الخطوة الرابعة (الامتصاص):</strong> اتركي الزيت يتغلغل داخل الجلد لترطيب وترميم الخلايا.</li>
  <li><strong>الخطوة الخامسة (الاستخدام المفتوح):</strong> يُستخدم في أي وقت خلال النهار أو كقناع ترطيبي عميق قبل النوم.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الزيتون البكر (Olive Oil):</strong> مرطب غني بمضادات الأكسدة والأحماض الدهنية الأساسية التي تغذي ألياف الجلد.</li>
  <li><strong>شمع العسل (Beeswax):</strong> يشكل طبقة واقية طبيعية تحبس الرطوبة داخل الجلد وتمنع الجفاف.</li>
  <li><strong>العسل الطبيعي (Honey):</strong> مرطب طبيعي ومضاد للبكتيريا يساعد في تسريع التئام وترميم الأنسجة.</li>
  <li><strong>غذاء ملكات النحل (Royal Jelly):</strong> غني بالفيتامينات والمعادن التي تحفز إنتاج الكولاجين وتجديد الشباب.</li>
  <li><strong>صمغ النحل (Propolis):</strong> مضاد حيوي طبيعي يطهر الجلد ويحميه من التلوث والالتهابات.</li>
  <li><strong>حبوب لقاح النحل (Bee Pollen):</strong> تعزز مرونة الجلد وتغذي خلاياه بمضادات الأكسدة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي فقط.</li>
  <li>يُفضل إجراء اختبار حساسية خفيف لمن لديهم حساسية مثبتة تجاه منتجات النحل (العسل/البروبوليس).</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان معتدل الحرارة بعيداً عن الأشعة الشمسية المباشرة.</li>
  <li>أغلقي العبوة جيداً بعد كل استخدام للحفاظ على نقاء البلسم الطبيعي.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن كريم طبيعي 100% خالي من المواد الكيميائية والعطور.</li>
  <li>صاحبات البشرة الشديدة الجفاف أو المتهيجة التي تحتاج إلى ترميم طبيعي مكثف.</li>
  <li>لمن يرغبون في مستحضر شمول يغني عن كريمات متعددة للوجه والجسم والشعر.</li>
  <li>مناسب لجميع الأعمار ولجميع أنواع البشرة وخاصة الحساسة والجافة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>إيجيبشن ماجيك (Egyptian Magic)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / المرطبات متعددة الاستخدامات</td></tr>
  <tr><th>نوع المنتج</th><td>بلسم مرطب طبيعي 100% للوجه والجسم والشعر</td></tr>
  <tr><th>الحجم/الوزن</th><td>118 مل (4 أونصة)</td></tr>
  <tr><th>نوع البشرة/ الشعر</th><td>جميع أنواع البشرة (الوجه، الجسم، الشفاه، الشعر)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة، مرطبة بعمق، ومحمية ببريق صحي</td></tr>
  <tr><th>الملمس</th><td>بلسم غني يذوب إلى زيت عند التدفئة</td></tr>
  <tr><th>العطر</th><td>عطر العسل وشمع العسل الطبيعي الخفيف جداً</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت زيتون، شمع العسل، عسل، غذاء ملكات النحل، بروبوليس، حبوب لقاح النحل</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة الأمريكية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Egyptian Magic Skin Cream LLC</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من الرضع حتى كبار السن)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لخصائص منتجات النحل وزيت الزيتون (Egyptian Magic)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم إيجيبشن ماجيك مشكلة الجفاف الشديد والتشققات الجلدية والتهيج الناتجة عن تضرر حاجز البشرة، إضافة إلى علاج جفاف الشفاه، تقصف أطراف الشعر، والندبات السطحية دون استخدام كيماويات صناعية.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تتعرض البشرة باستمرار للجفاف والتشقق نتيجة نقص الأحماض الدهنية في غشاء الليبيد الواقي بفعل الطقس الجاف، غسيل الماء الساخن، أو استخدام المستحضرات المليئة بالمواد الحافظة والعطور التي تهيج الجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التدفئة بين الكفين:</strong> دلكي البلسم دائماً بين يديكِ ليتحول لزيت قبل وضعه على البشرة.<br>
2. <strong>الترطيب بعد الاستحمام:</strong> ضعي البلسم والجلد ما زال رطباً لحبس الماء داخل الطبقات.<br>
3. <strong>العناية بالشفاه والأظافر:</strong> مرري طبقة خفيفة ليلاً على الشفاه والجلد حول الأظافر.<br>
4. <strong>علاج الشعر المتقصف:</strong> ضعي كمية ضئيلة جداً على أطراف الشعر الجاف لاستعادة اللمعان.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الزيوت الطبيعية دائماً تسد مسام البشرة."<br>
<strong>الحقيقة:</strong> زيت الزيتون وشمع العسل في إيجيبشن ماجيك يمتلكان خصائص غير نفاذة وضارة، ويعملان على موازنة زيوت الجلد الطبيعية وتطهير الفروة بفضل البروبوليس.</p>
<p><strong>خرافة:</strong> "الكريم الطبيعي صلاحيته تنتهي بسرعة."<br>
<strong>الحقيقة:</strong> العسل والبروبوليس وشمع العسل مواد حافظة طبيعية أسطورية قادرة على الحفاظ على نضارة البلسم لسنوات دون مواد حافظة صناعية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعتمد الكريم على الدمج الفيزيائي الحيوي بين الدهون الدهنية المستخلصة من زيت الزيتون وشمع العسل (Cera Alba) التي تشكل غشاءً عازلاً ينظم التبخر الجلدي (TEWL). وفي نفس الوقت، تنفذ المركبات الحيوية مثل حمض 10-هيدروكسي ديسينويك في غذاء الملكات والفلافونويدات في البروبوليس لتحفيز تكاثر خلايا الجلد وإصلاح الكولاجين، بينما يمنح العسل ترطيباً اسموزياً يجذب رطوبة الجو لخلايا الوجه.</p>"""

    faqs = [
        ("ما هو كريم إيجيبشن ماجيك وما هي مكوناته؟", "هو مرطب طبيعي 100% متعدد الاستخدامات يعتمد على 6 مكونات طبيعية فقط: زيت الزيتون، شمع العسل، العسل، غذاء ملكات النحل، صمغ النحل (بروبوليس)، وحبوب اللقاح."),
        ("ما هي الاستخدامات المختلفة لكريم إيجيبشن ماجيك؟", "يُستخدم كمرطب للوجه، بلسم للشفاه، كريم للعينين، معالج لتقصف الشعر، مرطب للجسم، مهدئ للحروق البسيطة وتهيج الحلاقة، ومرطب للأظافر."),
        ("كيف يتم استخدام البلسم بشكل صحيح؟", "خذي كمية صغيرة وافركيها بين كفيكِ لعدة ثوانٍ حتى تذوب إلى زيت ناعم، ثم وزعيها على المنطقة المطلوبة."),
        ("هل يحتوي إيجيبشن ماجيك على أي مواد كيميائية أو بارابين؟", "لا، هو خالي تماماً من أي مواد كيميائية، مواد حافظة، عطور، بارابين، أو مشتقات بترولية."),
        ("هل يناسب كريم إيجيبشن ماجيك البشرة الحساسة؟", "نعم، مكوناته الطبيعية اللطيفة تصنفه كأحد أفضل المرطبات للبشرة الأكثر حساسيات والجافة."),
        ("هل يمكن استخدام الكريم للأطفال والرضع؟", "نعم، هو آمن جداً للأطفال ويستخدم لتهدئة طفح الحفاض والتهابات الجلد والجفاف لدى الرضع."),
        ("هل يساعد الكريم في معالجة تقصف الشعر؟", "نعم، مسح كمية بسيطة جداً على أطراف الشعر المتقصف يعيد إليها الرطوبة واللمعان ويقلل التطاير."),
        ("هل يمكن استخدامه كمزيل للمكياج؟", "نعم، يذوب المكياج والمقاوِم للماء بفعالية كبيرة ويترك البشرة مرطبة وناعمة."),
        ("ما حجم هذه العبوة؟", "تأتي العبوة بحجم 118 مل (4 أونصة)، وهي عبوة اقتصادية تكفي لأشهر من الاستخدام المتعدد."),
        ("هل يترك الكريم ملمساً دهنياً على البشرة؟", "عند تدفئته واستخدام كمية مناسبة، يمتصه الجلد تدريجياً ويزوده برطوبة عميقة دون ثقل مزعج."),
        ("هل يناسب البشرة المعرضة لحب الشباب؟", "المكونات تحتوي على البروبوليس والعسل وهما مضادان طبيعيان للبكتيريا، لكن يُفضل استخدامه باعتدال للبشرة الشديدة الدهنية."),
        ("هل يفيد في تهدئة حروق الشمس؟", "نعم، يهدئ احمرار وحرارة الجلد بعد التعرض للشمس ويرمم الخلايا السطحية بسرعة."),
        ("ما هو بلد صنع كريم إيجيبشن ماجيك؟", "صُنع هذا الكريم بفخر في الولايات المتحدة الأمريكية بنفس الوصفة التاريخية الأصيلة."),
        ("هل يمكن استخدامه ككريم تحت العين؟", "نعم، كمية ضئيلة جداً تربت تحت العين تنعم المنطقة وتمنع التجاعيد الناجمة عن الجفاف."),
        ("هل يحتاج الكريم للحفظ في الثلاجة؟", "لا، يُحفظ في درجة حرارة الغرفة العادية بعيداً عن أشعة الشمس والحرارة العالية."),
        ("ما هي رائحة كريم إيجيبشن ماجيك؟", "يتميز برائحة طبيعية خفيفة جداً من العسل وشمع العسل دون إضافة أي عطور صناعية."),
        ("هل يساعد في تقليل مظهر الندبات والتشققات؟", "نعم، غني بغذاء الملكات والبروبوليس اللذين يساعدان في تحفيز التئام وتجدد الجلد المرن."),
        ("هل المنتج أصلي 100% في صيدلية إكليل أبها؟", "نعم، جميع عبوات إيجيبشن ماجيك لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يناسب النساء الحوامل؟", "نعم، هو ممتاز جداً وآمن للحوامل لترطيب بطن الحامل والوقاية من علامات التمدد (Stretch Marks)."),
        ("ما هو الفرق بين إيجيبشن ماجيك والمرطبات البترولية؟", "إيجيبشن ماجيك خالي من الفازلين والبترول، وتتكون تركيبته 100% من مكونات حيوية مغذية ومستدامة."),
        ("كم مدة صلاحية العبوة بعد الفتح؟", "تصل صلاحية العبوة إلى 36 شهراً بعد الفتح بفضل خصائص الحفظ الطبيعية للعسل والبروبوليس."),
        ("هل يمكن استخدامه كبلسم بعد الحلاقة للرجال؟", "نعم، يهدئ تهيج البشرة وجروح الحلاقة اللطيفة فورياً بفضل صمغ النحل."),
        ("هل يتغير قوام البلسم في البرد؟", "نعم، قد يصبح صلباً في الطقس البارد، ولكن تدفئته بين اليدين تذيبه فوراً إلى زيت سائل."),
        ("هل يسبب المنتج انسداد مسام الشفاه؟", "لا، هو ممتاز جداً للشفاه ويقضي على التشققات من الاستخدام الأول."),
        ("هل يُستخدم قبل النوم كقناع ترطيب؟", "نعم، وضع طبقة خفيفة قبل النوم يمنحك بشرة ممتلئة وشديدة النعومة في الصباح.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Egyptian Magic All-Purpose Skin Cream (118 ml / 4 oz)</strong> is a legendary global multi-purpose moisturizing balm crafted from a 100% natural, clean formula. Inspired by ancient Egyptian skincare secrets, this cult-favorite balm fuses six pure bee-derived ingredients and olive oil without any synthetic additives, preservatives, fragrances, or parabens—making it a staple among celebrities, makeup artists, and dermatologists worldwide.</p>
<p>Beginning as a rich, solid balm, Egyptian Magic quickly melts into a luxurious, nutrient-rich oil when rubbed between your palms. It delivers intensive moisture and rapid relief to dry, cracked, or irritated skin. Extremely versatile, it acts as a face moisturizer, eye cream, lip balm, hair split-end treatment, body balm, post-shave smoother, and soothing salve for minor skin irritations.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Natural Formula:</strong> Completely free from synthetic chemicals, parabens, preservatives, fragrances, and petroleum.</li>
  <li><strong>6 Pure Ingredients:</strong> Olive Oil, Beeswax, Honey, Royal Jelly, Bee Propolis, and Bee Pollen.</li>
  <li><strong>All-in-One Versatility:</strong> Suitable for face, lips, eyes, body, hair, nails, and minor burns or abrasions.</li>
  <li><strong>Deep Moisture Restoration:</strong> Intensely hydrates severely dry skin, repairing compromised skin barriers.</li>
  <li><strong>Hair & Scalp Conditioner:</strong> Softens split ends and tames flyaway hair while restoring natural shine.</li>
  <li><strong>Dermatologist-Approved & Safe:</strong> Extremely gentle on sensitive skin, safe for infants, children, and pregnant women.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Dispense):</strong> Scoop a small pea-sized portion of the solid balm with clean fingertips.</li>
  <li><strong>Step 2 (Warming):</strong> Rub the balm vigorously between your palms for a few seconds until it melts into a silky liquid oil.</li>
  <li><strong>Step 3 (Apply):</strong> Gently massage the warm oil onto the targeted area (face, lips, elbows, hair ends).</li>
  <li><strong>Step 4 (Absorption):</strong> Allow the natural oils to absorb deeply into skin cells for intense nourishment.</li>
  <li><strong>Step 5 (Day or Night):</strong> Use anytime throughout the day or apply as a deep overnight hydration mask.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Olive Oil (Olea Europaea Fruit Oil):</strong> Rich in essential fatty acids and antioxidants that nourish and soften skin cells.</li>
  <li><strong>Beeswax (Cera Alba):</strong> Creates a natural breathable protective barrier that seals in essential moisture.</li>
  <li><strong>Pure Honey (Mel):</strong> Natural humectant with antibacterial properties that accelerate tissue recovery.</li>
  <li><strong>Royal Jelly:</strong> Packed with vitamins and amino acids that boost collagen production and skin vitality.</li>
  <li><strong>Bee Propolis:</strong> Natural antiseptic defender that purifies and shields skin from environmental stressors.</li>
  <li><strong>Bee Pollen:</strong> Nutrient-dense antioxidant complex enhancing skin elasticity and cellular resilience.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external use only.</li>
  <li>Perform a patch test prior to use if you have known allergies to bee products (honey, pollen, propolis).</li>
  <li>Keep out of reach of children and store at moderate room temperature away from direct sunlight.</li>
  <li>Seal jar tightly after every application to preserve formula purity.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone looking for a 100% natural, multi-purpose skin balm free of synthetic additives.</li>
  <li>Individuals with severely dry, cracked, or sensitive skin needing intensive barrier repair.</li>
  <li>Minimalists seeking a single, versatile product replacing separate face, body, and hair moisturizers.</li>
  <li>Suitable for all ages, skin types, and whole-family application.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Egyptian Magic</td></tr>
  <tr><th>Category</th><td>Skincare / All-Purpose Moisturization</td></tr>
  <tr><th>Product Type</th><td>100% Natural All-Purpose Skin Balm</td></tr>
  <tr><th>Volume/Weight</th><td>118 ml (4 fl. oz.)</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Face, Body, Lips, Hair, Nails)</td></tr>
  <tr><th>Finish</th><td>Deeply hydrated, soft, radiant finish</td></tr>
  <tr><th>Texture</th><td>Rich solid balm that melts into silky oil</td></tr>
  <tr><th>Fragrance</th><td>Subtle natural honey aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Olive Oil, Beeswax, Honey, Royal Jelly, Propolis, Bee Pollen</td></tr>
  <tr><th>Country of Origin</th><td>USA</td></tr>
  <tr><th>Manufacturer</th><td>Egyptian Magic Skin Cream LLC</td></tr>
  <tr><th>Age Group</th><td>All Ages (Infants to Seniors)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Healing Science of Bee Products & Botanical Lipids</h2>

<h3>What problem does this solve?</h3>
<p>Egyptian Magic All-Purpose Skin Cream solves severe skin dryness, barrier damage, chapped lips, split ends, and minor skin irritation without relying on petroleum derivatives, synthetic preservatives, or artificial fragrances.</p>

<h3>Why does this condition happen?</h3>
<p>Environmental extremes, hot showers, harsh soaps, and synthetic chemicals strip essential lipids from the stratum corneum. This increases transepidermal water loss (TEWL), leading to cracking, flaking, redness, and heightened sensitivity.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Warm Before Application:</strong> Rub the balm between palms to melt it into oil for optimal absorption.<br>
2. <strong>Apply to Damp Skin:</strong> Apply after bathing while skin is damp to trap maximum water hydration.<br>
3. <strong>Overnight Lip Care:</strong> Apply a thick layer to lips before sleep to eliminate chapping overnight.<br>
4. <strong>Split End Treatment:</strong> Work a tiny dab into dry hair ends to seal split cuticles.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Natural oils always clog pores and cause breakouts."<br>
<strong>Fact:</strong> The non-comedogenic olive oil and antibacterial propolis in Egyptian Magic balance natural sebum while fighting skin surface bacteria.</p>
<p><strong>Myth:</strong> "Preservative-free products spoil rapidly."<br>
<strong>Fact:</strong> Honey, propolis, and beeswax are nature's legendary preservatives, providing long-term stability without synthetic additives.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Egyptian Magic operates through lipid occlusion and biochemical tissue repair. The combination of olive oil fatty acids and beeswax esters forms a biocompatible barrier over the stratum corneum, reducing TEWL. Concurrently, 10-hydroxy-2-decenoic acid from Royal Jelly and flavonoids from Propolis stimulate fibroblast proliferation and collagen synthesis, while raw honey exerts an osmotic humectant draw to rehydrate skin cells.</p>"""

    en_faqs = [
        ("What is Egyptian Magic All-Purpose Skin Cream?", "Egyptian Magic is a 100% natural, multi-purpose skin balm made from 6 pure ingredients: Olive Oil, Beeswax, Honey, Royal Jelly, Propolis, and Bee Pollen."),
        ("What are the different uses for Egyptian Magic?", "It can be used as a face moisturizer, eye cream, lip balm, hair split-end treatment, body balm, post-shave smoother, cuticle cream, and soothing salve for minor burns."),
        ("How do I apply Egyptian Magic correctly?", "Scoop a small pea-sized amount, rub it between your palms until it melts into a smooth oil, then gently massage onto desired areas."),
        ("Does it contain any parabens, chemicals, or synthetic fragrances?", "No, it is 100% free of parabens, synthetic chemicals, preservatives, artificial fragrances, and petroleum derivatives."),
        ("Is Egyptian Magic suitable for sensitive skin?", "Yes, its ultra-gentle, pure formula is ideal for sensitive, dry, or easily irritated skin types."),
        ("Can it be used on infants and young children?", "Yes, it is completely safe for babies and children, working wonderfully to soothe diaper rash and dry skin patches."),
        ("Does Egyptian Magic help repair split ends?", "Yes, smoothing a tiny amount onto dry hair ends restores moisture, reduces flyaways, and enhances shine."),
        ("Can it be used as a makeup remover?", "Yes, it effectively dissolves stubborn and waterproof makeup while leaving the skin hydrated and soft."),
        ("What size is this jar?", "This jar contains 118 ml (4 fl. oz.), offering an economical volume that lasts for months of versatile use."),
        ("Does it leave a greasy residue?", "When warmed properly between hands and applied in moderate amounts, it absorbs deeply, leaving a healthy radiant glow rather than heavy grease."),
        ("Is it suitable for acne-prone skin?", "Honey and Propolis provide natural antibacterial benefits; however, oily skin types should use it moderately."),
        ("Does it help soothe sun exposure irritation?", "Yes, it rapidly cools and soothes sun-exposed, overheated skin while promoting cellular recovery."),
        ("Where is Egyptian Magic manufactured?", "It is proudly manufactured in the USA using the original authentic formulation."),
        ("Can I use it as an eye cream?", "Yes, patting a tiny dab under the eyes deeply hydrates and smooths fine dehydration lines."),
        ("Does it need to be refrigerated?", "No, store at normal room temperature away from direct heat and sunlight."),
        ("What does Egyptian Magic smell like?", "It features a subtle, natural honey and beeswax aroma with zero artificial perfumes."),
        ("Does it help reduce the appearance of scars and stretch marks?", "Yes, rich in Royal Jelly and Propolis, it encourages skin regeneration and improves elasticity."),
        ("Is the product at Ekleel Abha 100% authentic?", "Yes, all Egyptian Magic jars at Ekleel Abha are 100% genuine and sourced directly from certified distributors."),
        ("Is it safe for pregnant women?", "Yes, it is 100% safe and highly recommended for pregnant women to moisturize their belly and prevent stretch marks."),
        ("How does Egyptian Magic differ from petroleum jelly?", "Unlike petroleum-based products, Egyptian Magic contains zero petroleum derivatives and is made entirely of 100% natural, nutrient-dense ingredients."),
        ("What is its shelf life after opening?", "It remains fresh for up to 36 months after opening due to the natural preservative properties of honey and propolis."),
        ("Can men use it as an aftershave balm?", "Yes, it calms razor burn and minor nicks instantly thanks to the natural antiseptic qualities of bee propolis."),
        ("Why does the balm's consistency change in cold weather?", "It naturally firms up in cold temperatures; simply warming a small amount between your palms instantly melts it into smooth oil."),
        ("Does it effectively relieve chapped lips?", "Yes, it heals severely dry, chapped lips often after a single overnight application."),
        ("Can it be applied as an overnight face mask?", "Yes, applying a thin layer before sleep leaves your skin plump, radiant, and deeply nourished by morning.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1694",
        "sku": "EK-1694",
        "gtin": "764936777770",
        "category": "العناية بالبشرة / المرطبات متعددة الاستخدامات",
        "brand": "Egyptian Magic",
        "ar": {
            "title": "مرطب البشرة من ايجيبشن ماجيك 118 مل",
            "meta_title": "كريم ايجيبشن ماجيك الاصلي 118مل | صيدلية إكليل أبها",
            "meta_description": "اشتري مرطب البشرة إيجيبشن ماجيك الأصلي متعدد الاستخدامات 118مل. مكونات طبيعية 100% من العسل وشمع العسل وزيت الزيتون. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["ايجيبشن_ماجيك", "مرطب_طبيعي", "منتجات_النحل", "عناية_بالبشرة", "إكليل_أبها"]
        },
        "en": {
            "title": "Egyptian Magic Skin Cream - 118 ml",
            "meta_title": "Egyptian Magic All-Purpose Skin Cream 118ml | Ekleel Abha",
            "meta_description": "Buy original Egyptian Magic All-Purpose Skin Cream (118ml / 4 oz). 100% natural balm with Honey, Royal Jelly & Olive Oil. 100% authentic at Ekleel Abha.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["egyptian_magic", "all_purpose_balm", "natural_skincare", "bee_products", "ekleel_abha"]
        },
        "schema": {
            "brand": "Egyptian Magic",
            "category": "Skincare / All-Purpose Balm",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "egyptian-magic-skin-cream-118ml.webp",
            "alt": "Egyptian Magic All-Purpose Skin Cream 118ml",
            "title": "Egyptian Magic All-Purpose Skin Cream 118ml"
        }
    }

print("Loaded 1694 builder")
