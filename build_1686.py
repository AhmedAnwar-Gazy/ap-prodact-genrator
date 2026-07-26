import json, os

def create_product_1686():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم أساس وبديل المكياج ماجيك فينيش من إم أسام (M. Asam Magic Finish Makeup - 30ml)</strong> واحداً من أكثر منتجات التجميل الألمانية شهرة وحصولاً على جوائز عالمية. يتميز هذا المنتج بتركيبة ثورية 4 في 1 تجمع بين خصائص برايمر تجهيز البشرة، خافي العيوب (كونسيلر)، كريم الأساس، والبودرة المثبتة في منتج واحد ذو ملمس موس المخملي الناعم، مما يختصر وقت روتينك الجمالي ويمنحك بشرة مثالية خالية من العيوب في ثوانٍ معدودة.</p>
<p>يتكيف كريم ماجيك فينيش تلقائياً مع معظم درجات البشرة بفضل صبغاته الذكية المبتكرة، حيث يخفي الاحمرار، الهالات السوداء، البقع، والمسام الواسعة، مع توحيد لون البشرة وإعطائها مظهر مات (مطفأ) مخملي دون تكتل أو جفاف. كما تحتوي التركيبة على فيتامين E المغذي لتعزيز حماية الجلد من الأكسدة والعوامل البيئية الضارة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تركيبة ثورية 4 في 1:</strong> يغني تماماً عن استخدام البرايمر، الكونسيلر، كريم الأساس، والبودرة بشكل منفصل.</li>
  <li><strong>تكيّف ذكي مع لون البشرة:</strong> يندمج بمرونة مع مختلف ألوان البشرة من الفاتحة إلى المتوسطة لمنح مظهر طبيعي مئة بالمئة.</li>
  <li><strong>إخفاء كامل للعيوب والمسام:</strong> يغطي الاحمرار، التصبغات، الهالات السوداء، والخطوط الدقيقة ويموه المسام الواسعة بلمسة واحدة.</li>
  <li><strong>ملمس موس مخملي خفيف:</strong> يمنح شعوراً خفيفاً للغاية على البشرة دون الشعور بالثقل أو الانسداد.</li>
  <li><strong>لمسة نهائية مطفأة (Matte Finish):</strong> يسيطر على لمعان البشرة والزيوت الزائدة ويمنح مظهراً ناعماً يدوم طوال اليوم.</li>
  <li><strong>مدعم بفيتامين E:</strong> يغذي البشرة ويحمي الخلايا من الأكسدة والجذور الحرة والجفاف.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الترطيب):</strong> وضعي كريمك المرطب اليومي على بشرة نظيفة واتركيه لعدة دقائق ليتم امتصاصه بالكامل.</li>
  <li><strong>الخطوة الثانية (أخذ الكمية):</strong> خذي كمية صغيرة جداً من كريم ماجيك فينيش بأطراف الأصابع أو بفرشاة المكياج.</li>
  <li><strong>الخطوة الثالثة (التوزيع):</strong> وزعي الكريم على كامل الوجه ببطء ودلكيه بحركات دائرية خفيفة من المركز نحو الأطراف.</li>
  <li><strong>الخطوة الرابعة (التدميج والتغطية):</strong> لاحظي كيف يتكيف اللون فورياً مع بشرتك، ويمكنك إضافة كمية إضافية صغيرة على المناطق التي تحتاج تغطية أكبر مثل الهالات أو البقع.</li>
  <li><strong>الخطوة الخامسة (اللمسة النهائية):</strong> لا حاجة لوضع بودرة تثبيت فوقه؛ استمتعي بمظهر مخملي مثالي طوال اليوم.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركب السيليكون المتقدم (Dimethicone & Cyclopentasiloxane):</strong> يوفر الملمس المخملي الفريد ويساعد في ملء الخطوط الدقيقة وتنعيم المسام.</li>
  <li><strong>فيتامين E (Tocopheryl Acetate):</strong> مضاد أكسدة قوي يغذي طبقات الجلد ويحميها من التلف الناجم عن العوامل البيئية.</li>
  <li><strong>السيليكا (Silica):</strong> تمتص الدهون الزائدة والزيوت لمنح لمسة مطفأة (Matte) تدوم طويلاً.</li>
  <li><strong>أكاسيد الحديد وثاني أكسيد التيتانيوم (Iron Oxides & Titanium Dioxide):</strong> صبغات معدنية ذكية توفر التغطية وتتكيف مع درجة لون البشرة.</li>
  <li><strong>تركيبة خالية من الكحول والأمونيا:</strong> لطيفة وآمنة للبشرة اليومية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي فقط على الوجه والرقبة.</li>
  <li>تجنبي ملامسة المنتج المباشرة للعينين؛ وفي حال ملامستهما يُشطف جيداً بالماء.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن أشعة الشمس والحرارة.</li>
  <li>يُغلق الغطاء جيداً بعد كل استخدام للحفاظ على قوام الموس المخملي من الجفاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن مكياج سريع وعملي يمنح بشرة خالية من العيوب في ثوانٍ.</li>
  <li>صاحبات البشرة الدهنية والمختلطة الراغبات في التحكم باللمعان والزيوت الزائدة.</li>
  <li>لمن يعانون من المسام الواسعة أو الخطوط الدقيقة والتصبغات الجلديّة.</li>
  <li>مناسب لجميع أنواع البشرة ومثالي للاستخدام اليومي أو المناسبات.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>إم أسام (M. Asam)</td></tr>
  <tr><th>الفئة</th><td>المكياج / كريم الأساس وخافي العيوب</td></tr>
  <tr><th>نوع المنتج</th><td>كريم أساس وبديل مكياج 4 في 1 (موس)</td></tr>
  <tr><th>الحجم/الوزن</th><td>30 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (العادية، الدهنية، المختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>لمسة مخملية مطفأة (Matte Finish) وتغطية طبيعية</td></tr>
  <tr><th>الملمس</th><td>موس كريمي خفيف جداً</td></tr>
  <tr><th>العطر</th><td>عطر خفيف وأنيق</td></tr>
  <tr><th>المكونات النشطة</th><td>فيتامين E، سيليكا، صبغات معدنية تكيفية، مركبات السيليكون</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا</td></tr>
  <tr><th>الشركة المصنعة</th><td>M. Asam GmbH</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغات (18 سنة فما فوق)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لتقنية الميكروبرايمر والمكياج المتكيف (Magic Finish)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج ماجيك فينيش من إم أسام مشكلة استهلاك الوقت الطويل في وضع طبقات المكياج المتعددة (البرايمر، الكونسيلر، الأساس، البودرة) والتي غالباً ما تؤدي لتكتل المكياج وثقله على البشرة وسد المسام.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>وضع عدة طبقات من مستحضرات التجميل المختلفة يزيد من سمك الطبقة الجلدية المغطاة، مما يسبب عدم تجانس اللون، تراكم الزيوت في خطوط الوجه، وظهور المظهر الكعكي (Caky Look). كما أن اختيار درجة الأساس الخاطئة يسبب تبايناً ملحوظاً بين لون الوجه والرقبة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الترطيب الجيد:</strong> رطبي بشرتك دائماً قبل وضع أي مكياج لضمان توزيع متساوٍ.<br>
2. <strong>استخدام كمية صغيرة:</strong> تركيبة الموس غنية جداً، لذا فإن كمية بحجم حبة الحمص تكفي الوجه بالكامل.<br>
3. <strong>التدميج الخفيف:</strong> استخدمي أطراف الأصابع لدمج المنتجات ذات الصبغات التكيفية بفعل حرارة اليد.<br>
4. <strong>التنظيف اللطيف مساءً:</strong> أزيلي المكياج بمزيل زيت أو ماء ميسيلار للحفاظ على صحة المسام.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "منتج درجة لون واحدة لا يمكن أن يناسب مختلف ألوان البشرة."<br>
<strong>الحقيقة:</strong> صبغيات ماجيك فينيش صُممت بتقنية انعكاس الضوء الضوئي التي تتكيف مع لون الجلد الطبيعي من الدرجات الفاتحة وحتى المتوسطة الداكنة بمرونة فائقة.</p>
<p><strong>خرافة:</strong> "كريمات الموس تسبب جفاف الجلد."<br>
<strong>الحقيقة:</strong> ماجيك فينيش مدعم بفيتامين E والزيوت السيليكونية المرطبة التي تحافظ على مرونة البشرة دون جفاف.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تعتمد تقنية ماجيك فينيش على شبكة البوليمرات السيليكونية المتصالبة (Dimethicone Crosspolymer) التي تشكل غشاءً مرناً رقيقاً يملأ الانخفاضات المجهرية للمسام والخطوط دون اختراق طبقات الجلد العميق. تتوزع الجسيمات الدقيقة للسيليكا لامتصاص الدهون الزائدة، بينما تتشتت صبغات أكسيد الحديد لتتكيف مع درجة انعكاس الضوء الخاصة ببشرتك، مما يوفر تغطية متجانسة ومظهراً مخملياً طبيعياً.</p>"""

    faqs = [
        ("ما هو كريم ماجيك فينيش من إم أسام وما فائدته؟", "هو كريم مكياج ألماني ثوري 4 في 1 يعمل كبرايمر، كونسيلر، كريم أساس، وبودرة في آن واحد، ليمنح البشرة تغطية مخملية مطفأة وتوحيداً للون العيوب في ثوانٍ معدودة."),
        ("هل يتماشى لون ماجيك فينيش مع جميع ألوان البشرة؟", "نعم، يعتمد على صبغات ذكية تتكيف تلقائياً مع درجة لون البشرة من الدرجات الفاتحة جداً وحتى المتوسطة والقمحية، مانحةً مظهراً طبيعياً دون تباين."),
        ("هل يحتاج كريم ماجيك فينيش إلى وضع بودرة تثبيت فوقه؟", "لا، يحتوي المنتج في تركيبه على السيليكا الممتصة للزيوت والتي تمنح لمسة مطفأة (Matte) مخملية تُغني تماماً عن استخدام البودرة."),
        ("ما هو ملمس وقوام هذا الكريم؟", "يتميز بقوام موس كريمي خفيف جداً وهوائي ينزلق بسلاسة على البشرة دون أن يترك أي شعور بالثقل."),
        ("هل يخفي كريم ماجيك فينيش المسام الواسعة والخطوط الدقيقة؟", "نعم، تعمل مركبات السيليكون اللطيفة على ملء التعرجات الجلدية والمسام والخطوط الدقيقة بصرياً، مما يمنح البشرة مظهراً أملس ومشرقاً."),
        ("هل الكريم آمن للاستخدام اليومي؟", "نعم، تركيبته خالية من الكحول والأمونيا ومدعمة بفيتامين E المغذي، مما يجعله مناسباً وآمناً للاستخدام اليومي."),
        ("ما هي الكمية المناسبة للاستخدام على الوجه؟", "كمية صغيرة جداً بحجم حبة الحمص تكفي لتغطية الوجه بالكامل نظراً لكثافة وتغطية الموس العالية."),
        ("هل يناسب كريم ماجيك فينيش البشرة الدهنية؟", "نعم، هو ممتاز للبشرة الدهنية والمختلطة لأنه يسيطر على لمعان الزيوت الزائدة طوال اليوم بفضل مادة السيليكا."),
        ("هل يمكن استخدامه لإخفاء الهالات السوداء تحت العين؟", "نعم، يعمل ككونسيلر فعال لإخفاء الهالات السوداء والاحمرار والتصبغات الجلدية دون أن يتكتل في خطوط العين."),
        ("هل يحتاج استخدام برايمر قبل ماجيك فينيش؟", "لا، يحتوي ماجيك فينيش على برايمر مدمج في تركيبه يمهد البشرة ويسد المسام تلقائياً."),
        ("هل يحتوي المنتج على معالج أو فيتامينات مفيدة للبشرة؟", "نعم، مدعم بفيتامين E (Tocopheryl Acetate) المضاد للأكسدة والذي يغذي البشرة ويحميها من عوامل الشيخوخة البيئية."),
        ("هل يسبب ماجيك فينيش انسداد المسام أو ظهور حب الشباب؟", "لا، مركب السيليكون المستخدم ينشئ طبقة مسامية تسمح للبشرة بالتنفس دون سد المسام (Non-comedogenic)."),
        ("ما هو حجم العبوة وكم تكفي من الوقت؟", "تأتي العبوة بحجم 30 مل، ونظراً لأن الكمية المطلوبة يومياً صغيرة جداً، فإن العبوة تكفي من 3 إلى 6 أشهر من الاستخدام المنتظم."),
        ("هل المنتج نباتي وخالي من القسوة؟", "نعم، منتجات M. Asam الألمانية نباتية 100% ولم يتم اختبارها على الحيوانات."),
        ("كيف يمكن تطبيق ماجيك فينيش بشكل أفضل؟", "يمكن طبقه بسهولة بأطراف الأصابع بحركات دائرية، كما يمكن استخدام فرشاة المكياج أو الإسفنجة حسب التفضيل الشخصي."),
        ("هل يتأثر ماجيك فينيش بالماء أو العرق؟", "يمتاز بمقاومة ممتازة للرطوبة والعرق بفضل تركيبته السيليكونية المطفأة، مما يحافظ على ثباته لساعات طويلة."),
        ("هل يناسب البشرة الجافة؟", "نعم، ولكن يُنصح بوضع الكريم المرطب الخاص بكِ أولاً والانتظار حتى امتصاصه قبل تطبيق ماجيك فينيش لضمان أفضل نتيجة."),
        ("ما هو بلد المنشأ لمنتج ماجيك فينيش؟", "صُنع هذا المنتج بفخر في ألمانيا بواسطة شركة M. Asam العالمية الشهيرة للجودة والتجميل."),
        ("هل يمكن استخدام ماجيك فينيش على الرقبة؟", "نعم، يُفضل دمجه على الرقبة أيضاً لضمان تجانس واستمرارية التغطية المخملية الطبيعية."),
        ("هل يحتوي على حماية من أشعة الشمس (SPF)؟", "يحتوي على ثنائي أكسيد التيتانيوم الذي يوفر حماية فيزيائية خفيفة، ولكن يُفضل استخدام واقي الشمس الخاص بكِ تحته عند التعرض القوي للشمس."),
        ("ما هي رائحة كريم ماجيك فينيش؟", "يتميز برائحة ناعمة وأنيقة جداً تتلاشى بعد دقائق قصيرة من التطبيق."),
        ("هل يسبب الكريم تصبغ الملابس؟", "ينبغي ترك الكريم يجف لثوانٍ على البشرة لتجنب احتكاكه المباشر بالملابس الفاتحة."),
        ("كيف أزيل ماجيك فينيش في نهاية اليوم؟", "يُزال بسهولة باستخدام مزيل المكياج الزيتي، أو غسول الوجه اليومي المفضل لديكِ مع الماء الفاتر."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات إكليل أبها أصلية 100% ومستوردة مباشرة من الوكلاء المعتمدين بشركة M. Asam الألمانية."),
        ("هل يناسب السيدات فوق سن 40 سنة؟", "نعم، هو ممتاز جداً للبشرة الناضجة لأنه يملأ الخطوط التعبيرية ولا يستقر فيها بعكس كريمات الأساس الثقيلة.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>M. Asam Magic Finish Makeup (30ml)</strong> is an internationally acclaimed 4-in-1 beauty innovation from Germany. Designed to simplify your cosmetics routine, this velvety mousse product acts simultaneously as a primer, concealer, foundation, and setting powder. In just a few seconds, it transforms your complexion, blurring imperfections and conferring a smooth, flawless finish.</p>
<p>Featuring intelligent tone-adapting pigments, Magic Finish automatically blends with most skin tones, concealing redness, dark circles, spots, and enlarged pores. Its airy, featherlight mousse texture leaves skin with a soft, velvety matte finish without feel heavy or cakey, while added Vitamin E nourishes the skin and guards against environmental oxidative stress.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Revolutionary 4-in-1 Formula:</strong> Replaces separate primer, concealer, foundation, and powder applications.</li>
  <li><strong>Intelligent Color Adaptation:</strong> Blends self-adjusting pigments seamlessly across light to medium skin tones.</li>
  <li><strong>Flawless Imperfection Coverage:</strong> Blurs redness, dark spots, under-eye dark circles, fine lines, and enlarged pores instantly.</li>
  <li><strong>Featherlight Mousse Texture:</strong> Feels virtually weightless on the skin without clogging pores or caking.</li>
  <li><strong>Long-Lasting Matte Finish:</strong> Controls excess shine and oil for a silky, velvety complexion that lasts all day.</li>
  <li><strong>Enriched with Vitamin E:</strong> Delivers essential antioxidant nourishment to maintain skin suppleness and health.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Moisturize):</strong> Apply your daily moisturizer onto clean skin and allow it to absorb fully.</li>
  <li><strong>Step 2 (Dispense):</strong> Take a very small pea-sized amount of Magic Finish mousse onto your fingertips or makeup brush.</li>
  <li><strong>Step 3 (Distribute):</strong> Dot across your face and gently blend in circular motions outward from the center.</li>
  <li><strong>Step 4 (Build Coverage):</strong> Watch the shade adapt immediately to your skin tone; add a small extra dab over areas needing extra coverage.</li>
  <li><strong>Step 5 (Enjoy):</strong> No setting powder is needed; enjoy a flawless, velvety matte finish all day long.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Advanced Silicone Matrix (Dimethicone & Cyclopentasiloxane):</strong> Creates the silky mousse texture, smoothing fine lines and pores.</li>
  <li><strong>Vitamin E (Tocopheryl Acetate):</strong> Potent antioxidant that protects skin cells against free radicals and environmental stress.</li>
  <li><strong>Silica:</strong> Absorbs excess oils and controls shine for a persistent matte appearance.</li>
  <li><strong>Iron Oxides & Titanium Dioxide:</strong> Tone-matching mineral pigments providing natural coverage and SPF enhancement.</li>
  <li><strong>Alcohol-Free Formula:</strong> Gentle, non-drying composition safe for daily skin application.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external use on face and neck only.</li>
  <li>Avoid direct contact with eyes; rinse thoroughly with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from heat and light.</li>
  <li>Keep jar lid tightly sealed after use to prevent mousse texture from drying out.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a fast, effortless makeup routine yielding a flawless complexion in seconds.</li>
  <li>Oily and combination skin types needing effective shine control throughout the day.</li>
  <li>Individuals looking to minimize visible pores, redness, or fine lines effortlessly.</li>
  <li>Suitable for all skin types, ideal for daily wear or special events.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>M. Asam</td></tr>
  <tr><th>Category</th><td>Makeup / Foundation & Concealer</td></tr>
  <tr><th>Product Type</th><td>4-in-1 Mousse Foundation & Primer</td></tr>
  <tr><th>Volume/Weight</th><td>30 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Normal, Oily, Combination)</td></tr>
  <tr><th>Finish</th><td>Velvety Matte Finish</td></tr>
  <tr><th>Texture</th><td>Featherlight Creamy Mousse</td></tr>
  <tr><th>Fragrance</th><td>Subtle elegant aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Vitamin E, Silica, Adaptive Mineral Pigments, Dimethicone Matrix</td></tr>
  <tr><th>Country of Origin</th><td>Germany</td></tr>
  <tr><th>Manufacturer</th><td>M. Asam GmbH</td></tr>
  <tr><th>Age Group</th><td>Adults (18+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Adaptive Micro-Primer Mousse Technology</h2>

<h3>What problem does this solve?</h3>
<p>M. Asam Magic Finish eliminates the hassle, time, and caking associated with applying multiple separate cosmetics layers (primer, concealer, liquid foundation, setting powder). Layering multiple products often causes heavy buildup, clogged pores, and uneven texture.</p>

<h3>Why does this condition happen?</h3>
<p>Traditional cosmetics application involves stacking several formulas of varying oil and water ratios, which can separate, settle into facial creases, and accent fine lines. Furthermore, selecting incorrect foundation shades creates noticeable mismatches between the face and neck.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Moisturize First:</strong> Always hydrate skin prior to application to ensure effortless blending.<br>
2. <strong>Use Small Amounts:</strong> Mousse formulations are highly concentrated; a pea-sized amount covers the entire face.<br>
3. <strong>Blend with Fingertips:</strong> Body heat from fingers helps activate tone-adapting pigments for optimal blending.<br>
4. <strong>Cleanse Nightly:</strong> Remove makeup thoroughly with micellar water or oil cleanser to keep pores clear.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "A single universal shade cannot match different skin tones."<br>
<strong>Fact:</strong> Magic Finish uses light-diffusing optical pigments that adapt dynamically to skin tones ranging from fair to medium-tan.</p>
<p><strong>Myth:</strong> "Mousse foundations dry out the skin."<br>
<strong>Fact:</strong> Enriched with Vitamin E and hydrating silicone polymers, Magic Finish maintains skin flexibility without drying.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Magic Finish functions through a cross-linked Dimethicone polymer matrix that forms a breathable, flexible film over the epidermis, filling micro-crevices and pores without clogging. Spherical Silica micro-particles continuously absorb excess sebum, while suspended iron oxide pigments scatter ambient light to self-adjust to your skin tone's natural undertones, delivering a velvety matte appearance.</p>"""

    en_faqs = [
        ("What is M. Asam Magic Finish and what does it do?", "M. Asam Magic Finish is a German 4-in-1 mousse cosmetics product that acts as a primer, concealer, foundation, and setting powder, providing instant velvety coverage in seconds."),
        ("Does Magic Finish suit all skin tones?", "Yes, its self-adjusting mineral pigments automatically adapt to match fair, medium, and olive skin tones naturally."),
        ("Do I need to use setting powder with Magic Finish?", "No, the formula includes oil-absorbing silica that delivers a lasting velvety matte finish without requiring extra powder."),
        ("What is the texture of Magic Finish?", "It features an airy, featherlight mousse texture that glides smoothly across the skin without feeling heavy."),
        ("Does it effectively blur pores and fine lines?", "Yes, advanced silicone polymers fill skin micro-crevices and pores optically, creating a silky, smooth complexion."),
        ("Is Magic Finish safe for daily use?", "Yes, it is alcohol-free, non-comedogenic, and enriched with antioxidant Vitamin E for safe daily wear."),
        ("How much product should I apply?", "A tiny pea-sized amount is sufficient for full facial coverage due to its concentrated mousse formula."),
        ("Is it suitable for oily skin types?", "Yes, it is ideal for oily and combination skin because its silica content controls shine throughout the day."),
        ("Can it conceal under-eye dark circles?", "Yes, it functions as an effective concealer for dark circles, redness, and hyperpigmentation without settling into fine lines."),
        ("Do I need to apply primer before Magic Finish?", "No, Magic Finish incorporates built-in primer properties that smooth skin texture automatically."),
        ("What skin-nourishing ingredients does it contain?", "It is enriched with Tocopheryl Acetate (Vitamin E), a powerful antioxidant protecting skin against environmental oxidative damage."),
        ("Will Magic Finish clog pores or cause breakouts?", "No, its silicone matrix forms a breathable film that allows normal skin respiration without clogging pores."),
        ("How long does one 30ml jar last?", "Because very little product is required per application, one 30ml jar typically lasts 3 to 6 months of daily use."),
        ("Is M. Asam Magic Finish vegan and cruelty-free?", "Yes, M. Asam products are 100% vegan and cruelty-free, produced without animal testing."),
        ("How should I apply Magic Finish for best results?", "Blend easily using fingertips in gentle circular motions, or apply with a foundation brush or sponge."),
        ("Is Magic Finish water and sweat resistant?", "Yes, its matte silicone formulation resists humidity and sweat, keeping your makeup intact for hours."),
        ("Is it suitable for dry skin?", "Yes, though applying a light hydrating moisturizer beforehand is recommended for dry skin types."),
        ("Where is M. Asam Magic Finish manufactured?", "It is proudly manufactured in Germany by M. Asam GmbH under strict quality controls."),
        ("Can I apply Magic Finish to the neck area?", "Yes, blending down the neck ensures seamless, natural coverage continuity."),
        ("Does it provide sun protection (SPF)?", "It contains titanium dioxide for light physical reflection, though applying dedicated sunscreen underneath is recommended for prolonged sun exposure."),
        ("What scent does Magic Finish have?", "It features a subtle, pleasant aroma that dissipates shortly after application."),
        ("Will it stain clothing?", "Allow the product to set on the skin for a few seconds to prevent transfer onto clothing collar edges."),
        ("How do I remove Magic Finish at night?", "It removes easily using your favorite oil cleanser, micellar water, or daily facial wash with warm water."),
        ("How do I ensure product authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original, imported directly from authorized German M. Asam distributors."),
        ("Is it recommended for mature skin (40+)?", "Yes, it works exceptionally well on mature skin because it blurs fine lines rather than settling into wrinkles like heavy liquids.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1686",
        "sku": "EK-1686",
        "gtin": "4049639420335",
        "category": "المكياج / كريم الأساس وخافي العيوب",
        "brand": "M. Asam",
        "ar": {
            "title": "كريم اساس وبديل مكياج ماجيك فينيش من إم أسام 30مل",
            "meta_title": "كريم اساس ماجيك فينيش إم أسام 30مل | صيدلية إكليل أبها",
            "meta_description": "تسوقي كريم أساس ماجيك فينيش إم أسام الألماني 4 في 1 (30مل). تغطية مخملية مطفأة تتكيف مع لون البشرة فورياً. منتج أصلي 100% من صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["ام_اسام", "ماجيك_فينيش", "كريم_اساس", "مكياج_الماني", "إكليل_أبها"]
        },
        "en": {
            "title": "M. Asam Magic Finish Makeup - 30ml",
            "meta_title": "M. Asam Magic Finish Makeup 30ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original M. Asam Magic Finish 4-in-1 Mousse Makeup (30ml) from Germany. Self-adjusting coverage & velvety matte finish. 100% authentic at Ekleel Abha.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["m_asam", "magic_finish", "mousse_foundation", "german_makeup", "ekleel_abha"]
        },
        "schema": {
            "brand": "M. Asam",
            "category": "Makeup / Foundation",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "m-asam-magic-finish-makeup-30ml.webp",
            "alt": "M. Asam Magic Finish Makeup 30ml",
            "title": "M. Asam Magic Finish Makeup 30ml"
        }
    }

print("Loaded 1686 builder")
