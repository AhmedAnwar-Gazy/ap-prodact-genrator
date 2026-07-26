import json, os

def create_product_1710():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعتبر <strong>شامبو صانسيلك لشعر ناعم وانسيابي (Sunsilk Smooth & Manageable Shampoo - 400ml)</strong> الحل اليومي المبهج للحصول على شعر ناعم، مرن، وسهل التحكم به طوال اليوم. يعتمد هذا الشامبو على تقنية الزيوت الخمسة الطبيعية المبتكرة (بما فيها زيت الكاميليا وزيت الأرجان)، والتي تم تطويرها بالتعاون مع خبراء الشعر العالميين لتغذية كل خصلة شعر من الجذور حتى الأطراف.</p>
<p>ينظف الشامبو فروة الرأس بفاعلية ولطف، بينما يتغلغل في ألياف الشعر ليمنحها مرونة عالية وانسيابية مذهلة تقاوم الجفاف والهيشان. يترك الشعر ناعماً بشكل ملحوظ، عطراً برائحة الزهور الناعمة، وسهل التصفيف بدون عناء، مما يجعله خياركِ اليومي المفضل لشعر متألق ورائع دائماً.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>شعر ناعم وانسيابي طوال اليوم:</strong> يغذي الخصلات ويمنحها مرونة وانسيابية فائقة تسهل تصفيفها.</li>
  <li><strong>مزيج الزيوت الطبيعية المغذية:</strong> مدعم بزيوت الكاميليا والأرجان وجوز الهند وزيت الزيتون واللوز لترطيب مضاعف.</li>
  <li><strong>مكافحة الجفاف والهيشان:</strong> يغلف ألياف الشعر بطبقة ناعمة تقاوم الرطوبة وتمنع التعرج والتطاير.</li>
  <li><strong>تنظيف لطيف للفروة:</strong> يزيل الدهون والأوساخ دون تجريد الترطيب الطبيعي للبشرة.</li>
  <li><strong>رائحة زهرية منعشة تدوم:</strong> يكسب الشعر عبقاً زهرياً جذاباً يرافقكِ طوال اليوم.</li>
  <li><strong>فرمول مخصصة للاستخدام اليومي:</strong> آمنة ولطيفة ومناسبة لجميع أنواع الشعر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل):</strong> بلي شعركِ وفروة رأسكِ بالماء الفاتر جيداً.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية مناسبة من شامبو صانسيلك ناعم وانسيابي على راحة اليد ووزعيها.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي الفروة والشعر بلطف بأطراف الأصابع حتى تتكون رغوة غنية تعطر وتغذي الشعر.</li>
  <li><strong>الخطوة الرابعة (الشطف):</strong> اشطفي الشعر جيداً بالماء الفاتر حتى زوال الرغوة بالكامل.</li>
  <li><strong>الخطوة الخامسة (المتابعة):</strong> للحصول على أقصى درجات الانسيابية، اتبعي الشامبو ببلسم صانسيلك ناعم وانسيابي.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت كاميليا أوليفيرا (Camellia Seed Oil):</strong> يمنح الشعر لمعاناً ونعومة فائقة ويعيد مرونة الألياف.</li>
  <li><strong>زيت الأرجان (Argania Spinosa Kernel Oil):</strong> يغذي طبقات الشعر بالأحماض الدهنية وفيتامين E لمنع الجفاف.</li>
  <li><strong>الدايميثيكونول (Dimethiconol):</strong> سيليكون ينعم سطح الشعرة ويمنع التشابك والهيشان.</li>
  <li><strong>غوار كلورايد (Guar Hydroxypropyltrimonium Chloride):</strong> يسهل حركة المشط على الخصلات.</li>
  <li><strong>عوامل تنظيف لطيفة (Sodium Laureth Sulfate & Cocamidopropyl Betaine):</strong> تنظف الفروة بكفاءة عالية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الشعر وفروة الرأس فقط.</li>
  <li>تجنبي ملامسة الشامبو المباشرة للعينين؛ وفي حال ملامستهما اشطفي فوراً بالماء الفاتر.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
  <li>في حال حدوث حكة أو تهيج توقفي عن الاستخدام.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من الشعر الجاف، المتشابك، أو الصعب التحكم به.</li>
  <li>لمن تبحث عن شامبو يومي يمنح نعومة وانسيابية ورائحة زهرية مذهلة.</li>
  <li>مناسب لجميع أنواع الشعر والعناية اليومية.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>صانسيلك (Sunsilk)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / شامبو النعومة والانسيابية</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو تنعيم وتسهيل تصفيف الشعر (Smooth & Manageable)</td></tr>
  <tr><th>الحجم/الوزن</th><td>400 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (خاصة العادي، الجاف والصعب التصفيف)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم، انسيابي، مفعم باللمعان والعبير الزهري</td></tr>
  <tr><th>الملمس</th><td>كريمي وردي يرغي بسهولة</td></tr>
  <tr><th>العطر</th><td>عطر الزهور الطبيعي الجذاب والمنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت الكاميليا، زيت الأرجان، دايميثيكونول، غوار كلورايد</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / مصر (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (يونيليفر)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لتقنية الزيوت الطبيعية وانسيابية الشعر (Sunsilk)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج شامبو صانسيلك لشعر ناعم وانسيابي مشكلة جفاف الشعر وصعوبة تصفيفه والتشابك المستمر الناجم عن نقص المرونة الزيتية في ألياف الشعرة.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>يتعرض الشعر للجفاف عندما تفقد أليافه الزيوت المغذية بفعل العوامل البيئية والغسيل، مما يجعل حراشف الشعر خشنة وتلتصق ببعضها مكونة العقد والتشابك.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام البلسم المطابق:</strong> استخدمي بلسم صانسيلك ناعم وانسيابي للحصول على ترطيب كامل.<br>
2. <strong>التمشيط بمشط واسع الأسنان:</strong> ابدئي بتمشيط الأطراف أولاً ثم اتجهي للأعلى.<br>
3. <strong>الشطف بالماء الفاتر:</strong> تجنبي الماء الساخن لحماية الزيوت الطبيعية.<br>
4. <strong>التجفيف بلطف:</strong> لا تفركي الشعر بالمنشفة لتجنب إحداث تشابك جديد.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "شامبو النعومة يسبب تساقط الشعر."<br>
<strong>الحقيقة:</strong> شامبو صانسيلك يحتوي على مغذيات مرطبة تسهل التمشيط، مما يقلل التساقط الناجم عن تكسر الشعر بالفرشاة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعتمد المنتج على دمج الزيوت المغذية الدقيقة (مثل زيت الكاميليا والأرجان) التي تنفذ إلى الشقوق المجهرية للألياف، بينما تقوم بوليمرات التكييف بتنعيم حراشف الشعرة الخارجية، مما يقلل الاحتكاك السطحي ويمنح انسيابية مذهلة ومرونة طوال اليوم.</p>"""

    faqs = [
        ("ما هو شامبو صانسيلك لشعر ناعم وانسيابي؟", "هو شامبو مغذٍ مخصص لمنح الشعر نعومة فائقة وانسيابية وسهولة في التصفيف بفضل الزيوت المغذية وزيت الكاميليا والأرجان."),
        ("ما فائدة زيت الكاميليا والأرجان في الشامبو؟", "يغذيان ألياف الشعر بالأحماض الدهنية، يعيدان ليونة الخصلات، ويمنحان لمعاناً ونعومة كراستالية."),
        ("هل يساعد الشامبو في تسهيل تمشيط الشعر؟", "نعم، ينعم السطح الخارجي للشعر ويقلل الاحتكاك، مما يسهل مرور المشط دون تشابك."),
        ("ما حجم عبوة الشامبو؟", "تأتي العبوة بحجم 400 مل، وهي كمية مناسبة للاستخدام اليومي والمنتظم."),
        ("هل يناسب الشامبو الشعر المسبوغ؟", "نعم، تركيبة لطيفة وآمنة للشعر المصبوغ والمعالج بالألوان."),
        ("هل يناسب الرجال والنساء؟", "نعم، يناسب كافة أنواع الشعر ولكلا الجنسين."),
        ("كم مرة يُنصح باستخدامه أسبوعياً؟", "يُنصح باستخدامه من 2 إلى 3 مرات أسبوعياً، وهو آمن للاستخدام اليومي."),
        ("ما هي رائحة شامبو صانسيلك ناعم وانسيابي؟", "يتميز برائحة زهرية ناعمة وجذابة تدوم طويلاً في الشعر."),
        ("هل يترك الشامبو ملمساً دهنياً؟", "لا، ينظف الفروة بكفاءة ويدعم الانسيابية الخفيفة دون أي ثقل زيتي."),
        ("هل يناسب الشعر المتشابك الشديد؟", "نعم، ينعم الخصلات ويسلس فك العقد والتشابك بسرعة."),
        ("ما هو بلد صنع الشامبو؟", "يُصنع بواسطة شركة يونيليفر (Unilever) العالمية في مصانعها المعتمدة."),
        ("هل يحتوي على مركبات البارابين؟", "التركيبة مطورة وخالية من البارابين ومجربة جلدياً."),
        ("هل يساعد في تقليل الهيشان؟", "نعم، يغلف ألياف الشعر بحماية تقاوم الرطوبة وتقي من الهيشان."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات صانسيلك لدى صيدلية إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يلزم استخدام بلسم بعد الشامبو؟", "يُفضل استخدام بلسم صانسيلك ناعم وانسيابي للحصول على أقصى درجات النعومة."),
        ("هل يقلل الشامبو تكسر الشعر أثناء التمشيط؟", "نعم، تقليل الاحتكاك يمنع تكسر الخصلات وتساقطها الناجم عن المشط."),
        ("هل يناسب الأطفال؟", "مناسب للمراهقين والأطفال من سن 12 سنة فما فوق."),
        ("هل الشامبو آمن للاستخدام اليومي؟", "نعم، تركيبة لطيفة تناسب الاستخدام المنتظم."),
        ("هل يترك أي بقايا بعد الشطف؟", "لا، يشطف بسهولة وسرعة بالماء الفاتر."),
        ("كيف أحتفظ بالشامبو بالشكل الصحيح؟", "يُحفظ في مكان بارد وجاف بعيداً عن أشعة الشمس المباشرة."),
        ("هل العبوة بحجم 400 مل سهلة الاستخدام؟", "تأتي بتصميم عصري يسهل سكب الشامبو منها بمرونة."),
        ("هل يضيف بريقاً للشعر الباهت؟", "نعم، تنظيف التراكمات وتنعيم الخصلات يعيد البريق واللمعان."),
        ("هل يحتوي على زيت جوز الهند وزيت الزيتون؟", "نعم، تركيبته مدعمة بمزيج من الزيوت الطبيعية المغذية."),
        ("هل يساعد في حماية الشعر من الجفاف الصيفي؟", "نعم، يحافظ على ترطيب الشعر ويحميه من الجفاف."),
        ("هل يحتاج لرج العبوة؟", "لا يلزم، القوام متجانس وجاهز للاستخدام المباشر.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Sunsilk Smooth & Manageable Shampoo (400ml)</strong> is your daily essential for touchably soft, flexible, and effortlessly manageable hair all day long. Co-created with hair experts, this advanced shampoo features a nourishing natural oil blend enriched with Camellia and Argan oils to replenish every hair strand from root to tip.</p>
<p>It gently purifies the scalp of excess oil and buildup while infusing hair fibers with essential lipids to resist dryness and daily frizz. It leaves your hair noticeably smoother, delicately scented with a long-lasting floral fragrance, and effortlessly easy to style.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>All-Day Smooth & Manageable Hair:</strong> Nourishes strands to deliver long-lasting flexibility and soft combability.</li>
  <li><strong>Nourishing Natural Oil Blend:</strong> Enriched with Camellia, Argan, Coconut, Olive, and Almond oils for multi-layer hydration.</li>
  <li><strong>Frizz & Dryness Defense:</strong> Smooths cuticles to shield hair against atmospheric humidity and flyaways.</li>
  <li><strong>Gentle Scalp Purification:</strong> Cleanses oils effectively without stripping protective natural scalp moisture.</li>
  <li><strong>Long-Lasting Floral Scent:</strong> Imparts a fresh, delightful floral fragrance that lasts throughout the day.</li>
  <li><strong>Safe Daily Wash:</strong> Balanced, gentle formulation suitable for routine daily application.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Thoroughly wet hair and scalp with warm water.</li>
  <li><strong>Step 2 (Apply):</strong> Dispense a suitable amount of Sunsilk shampoo onto palms and distribute over hair.</li>
  <li><strong>Step 3 (Massage):</strong> Massage scalp gently with fingertips for 2-3 minutes into a rich, fragrant lather.</li>
  <li><strong>Step 4 (Rinse):</strong> Rinse completely with warm water until all foam is cleared.</li>
  <li><strong>Step 5 (Condition):</strong> For maximum smoothness, follow with Sunsilk Smooth & Manageable Conditioner.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Camellia Seed Oil (Camellia Oleifera):</strong> Imparts brilliant shine, intense softness, and restores fiber elasticity.</li>
  <li><strong>Argan Oil (Argania Spinosa Kernel Oil):</strong> Rich in omega fatty acids and Vitamin E to deeply nourish hair layers.</li>
  <li><strong>Dimethiconol:</strong> Smooths hair cuticles to prevent friction knots and humidity frizz.</li>
  <li><strong>Guar Hydroxypropyltrimonium Chloride:</strong> Eases comb movement across strands for smooth detangling.</li>
  <li><strong>Gentle Surfactants:</strong> Clear scalp buildup efficiently while preserving hair soft texture.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external use on hair and scalp only.</li>
  <li>Avoid direct contact with eyes; rinse immediately with warm water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
  <li>Discontinue use if irritation develops.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dry, tangled, coarse, or unmanageable hair seeking daily smoothness.</li>
  <li>Individuals looking for an everyday shampoo providing soft, fragrant, manageable hair.</li>
  <li>Suitable for all hair types and regular daily routine.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Sunsilk</td></tr>
  <tr><th>Category</th><td>Hair Care / Smoothing Shampoos</td></tr>
  <tr><th>Product Type</th><td>Smooth & Manageable Hair Shampoo</td></tr>
  <tr><th>Volume/Weight</th><td>400 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Ideal for Normal, Dry & Tangled Hair)</td></tr>
  <tr><th>Finish</th><td>Soft, smooth, manageable & fragrant hair</td></tr>
  <tr><th>Texture</th><td>Pinkish pearlescent rich fluid</td></tr>
  <tr><th>Fragrance</th><td>Delightful long-lasting natural floral aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Camellia Oil, Argan Oil, Dimethiconol, Guar Chloride</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / Egypt (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Natural Oils & Hair Manageability</h2>

<h3>What problem does this solve?</h3>
<p>Sunsilk Smooth & Manageable Shampoo resolves stubborn hair knots, friction tangles, and dryness caused by lipid depletion in hair fibers.</p>

<h3>Why does this condition happen?</h3>
<p>Hair fibers become tangled and difficult to manage when cuticle scales are raised and dry. Rough cuticles interlock like Velcro, creating knots and increasing combing resistance.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Use Matching Conditioner:</strong> Pair with Sunsilk Smooth conditioner for full cuticle smoothing.<br>
2. <strong>Wide-Tooth Comb:</strong> Start combing at the ends and work upward gently.<br>
3. <strong>Lukewarm Water:</strong> Wash with lukewarm water to protect lipid balance.<br>
4. <strong>Pat Dry Gently:</strong> Towel-dampen without aggressive rubbing.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Smoothing shampoos cause hair breakage."<br>
<strong>Fact:</strong> Sunsilk reduces friction during combing, significantly lowering breakage caused by forced brushing.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>The micro-oil complex (Camellia & Argan oils) fills microscopic cuticle gaps, while surface conditioning polymers reduce inter-fiber friction coefficient. This creates a lubricated, smooth surface that allows hair strands to slide past each other smoothly, restoring 24-hour manageability.</p>"""

    en_faqs = [
        ("What is Sunsilk Smooth & Manageable Shampoo?", "It is a daily smoothing shampoo enriched with Camellia and Argan oils designed to make hair soft, silky, and easy to manage."),
        ("What are the benefits of Camellia and Argan Oils?", "They nourish hair fibers, restore elasticity, and impart a smooth, crystal-like shine."),
        ("Does it help ease combing and detangling?", "Yes, conditioning agents smooth cuticles to facilitate easy comb movement without snagging."),
        ("What volume is contained in this bottle?", "It comes in a 400ml bottle ideal for regular daily use."),
        ("Is it safe for color-treated hair?", "Yes, its gentle formula is safe for color-treated hair."),
        ("Can both men and women use it?", "Yes, it is a unisex formula suitable for all hair types."),
        ("How often should I use it?", "It is safe for daily use or 2 to 3 times weekly as needed."),
        ("What fragrance does Sunsilk Smooth & Manageable have?", "It features a long-lasting, fresh floral aroma."),
        ("Does it leave a greasy residue?", "No, it cleanses scalp oils thoroughly while leaving hair light and bouncy."),
        ("Is it suitable for severely tangled hair?", "Yes, it smooths strands to allow quick and easy knot detangling."),
        ("Where is Sunsilk manufactured?", "It is manufactured by Unilever under strict international quality standards."),
        ("Is the formula paraben-free?", "Yes, it features an updated, dermatologically safety-tested formula."),
        ("Does it reduce frizzy hair?", "Yes, it seals cuticles against atmospheric humidity to prevent frizz."),
        ("How do I verify authenticity at Ekleel Abha?", "All Sunsilk products at Ekleel Abha are 100% original from certified Unilever Saudi distributors."),
        ("Should I use conditioner afterward?", "Using matching Sunsilk Smooth conditioner yields maximum softness."),
        ("Does it reduce breakage during brushing?", "Yes, lowering friction prevents comb-induced hair breakage."),
        ("Is it suitable for teenagers?", "Yes, safe for adults and teens aged 12+."),
        ("Is it safe for daily use?", "Yes, its gentle formulation supports regular daily washing."),
        ("Does it rinse out easily?", "Yes, it rinses out completely with warm water."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Is the 400ml bottle convenient to handle?", "It features an ergonomic shower bottle design."),
        ("Does it add shine to dull hair?", "Yes, clearing buildup and smoothing cuticles restores brilliant shine."),
        ("Does it contain Coconut and Olive oils?", "Yes, it incorporates a blend of natural conditioning oils."),
        ("Does it protect hair from summer dryness?", "Yes, it locks in moisture to defend against dry weather."),
        ("Does it require shaking before use?", "No, its homogeneous formula is ready for immediate use.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1710",
        "sku": "EK-1710",
        "gtin": "6281006424449",
        "category": "العناية بالشعر / شامبو النعومة والانسيابية",
        "brand": "Sunsilk",
        "ar": {
            "title": "شامبو صانسيلك لشعر ناعم وانسيابي - 400 مل",
            "meta_title": "شامبو صانسيلك لشعر ناعم وانسيابي 400مل | صيدلية إكليل أبها",
            "meta_description": "اشتري شامبو صانسيلك لشعر ناعم وانسيابي (400مل). فرمولة غنية بزيوت الكاميليا والأرجان لتغذية وسهولة تصفيف الشعر. أصلي من إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["صانسيلك", "شامبو_صانسيلك", "ناعم_وانسيابي", "زيت_الكاميليا", "إكليل_أبها"]
        },
        "en": {
            "title": "Sunsilk Shampoo for Smooth & Manageable Hair - 400ml",
            "meta_title": "Sunsilk Smooth & Manageable Shampoo 400ml | Ekleel Abha",
            "meta_description": "Buy Sunsilk Smooth & Manageable Shampoo (400ml). Infused with Camellia & Argan oils for all-day soft hair. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["sunsilk", "smooth_and_manageable", "camellia_oil", "shampoo", "ekleel_abha"]
        },
        "schema": {
            "brand": "Sunsilk",
            "category": "Hair Care / Shampoo",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "sunsilk-shampoo-for-smooth-and-manageable-hair-400ml.webp",
            "alt": "Sunsilk Shampoo for Smooth & Manageable Hair 400ml",
            "title": "Sunsilk Shampoo for Smooth & Manageable Hair 400ml"
        }
    }

print("Loaded 1710 builder")
