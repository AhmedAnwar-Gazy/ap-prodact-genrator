import json, os

def create_product_1711():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>شامبو صانسيلك لمعان ساحر للشعر الأسود (Sunsilk Stunning Black Shine Shampoo - 400ml)</strong> المستحضر الأيقوني المصمم خصيصاً لإبراز الجمال الطبيعي واللمعان الساحر للشعر الداكن والأسود. يعتمد هذا الشامبو على تقنية مركب اللمعان اللؤلؤي وزيت الحبة السوداء المغذي، حيث يعيد للشعر الأسود ألقه وحيويته، ويحميه من التلاشي والبهتان الناتج عن التعرض للشمس والتلوث.</p>
<p>ينظف الشامبو فروة الرأس بفاعلية ولطف، بينما يتغلغل في ألياف الشعر ليمنحها مرونة عالية وترطيباً عميقاً يعكس الضوء كالكراستال. يترك الشعر الأسود كئيباً بلون غني، مفعماً برائحة عطرية منعشة تدوم طوال اليوم، مما يجعله خياركِ المثالي للمحافظة على ألق شعركِ الأسود وجاذبيته.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>لمعان ساحر للشعر الأسود:</strong> يعزز اللون الداكن ويمنح الخصلات بريقاً كراستالياً يتوهج تحت الضوء.</li>
  <li><strong>مدعم بخلاصة الحبة السوداء:</strong> تغذي بصلات الشعر وتقوي أليافه وتحميه من التكسر والتساقط.</li>
  <li><strong>حماية ضد التلاشي والبهتان:</strong> يقي الشعر من التأثيرات الضارة للشمس والحرارة والتلوث البيئي.</li>
  <li><strong>ترطيب وتنعيم فائق:</strong> يجعل الشعر ناعماً كالحرير وسهلاً في التمشيط والتصفيف.</li>
  <li><strong>تنظيف لطيف للفروة:</strong> ينظف الرواسب الزهمية دون تجريد الزيوت الطبيعية الحامية.</li>
  <li><strong>مناسب للاستخدام اليومي:</strong> تركيبة متوازنة الحموضة ومناسبة للاستخدام المنتظم على الشعر الداكن.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل):</strong> بلي شعركِ وفروة رأسكِ بالماء الفاتر جيداً.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية مناسبة من شامبو صانسيلك لمعان ساحر على كف اليد ووزعيها.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي الفروة والشعر بلطف بأطراف الأصابع حتى تتكون رغوة غنية تعطر وتغذي الشعر.</li>
  <li><strong>الخطوة الرابعة (الشطف):</strong> اشطفي الشعر جيداً بالماء الفاتر حتى زوال الرغوة بالكامل.</li>
  <li><strong>الخطوة الخامسة (المتابعة):</strong> للحصول على أفضل لمعان، اتبعي الشامبو ببلسم صانسيلك لمعان ساحر للشعر الأسود.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة الحبة السوداء (Nigella Sativa Seed Oil):</strong> تقوي ألياف الشعر وتمنح الخصلات سواداً غنياً ولمعاناً طبيعياً.</li>
  <li><strong>مركب اللمعان اللؤلؤي (Amla & Pearl Complex):</strong> يعكس الضوء ويحمي ألياف الشعر من التلف الحراري والشمس.</li>
  <li><strong>الدايميثيكونول (Dimethiconol):</strong> ينعم السطح الخارجي للشعر ويمنع التشابك والهيشان.</li>
  <li><strong>غوار كلورايد (Guar Hydroxypropyltrimonium Chloride):</strong> يسهل حركة المشط على الشعر.</li>
  <li><strong>عوامل تنظيف لطيفة (Sodium Laureth Sulfate):</strong> تنظف الدهون والأوساخ بفاعلية عالية.</li>
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
  <li>لكل من تملك شعراً أسود أو داكناً وترغب في تعزيز بريقه ولمعانه الطبيعي.</li>
  <li>لمن تعاني من بهتان لون الشعر الأسود بسبب الشمس والتلوث.</li>
  <li>مناسب للاستخدام اليومي لجميع أنواع الشعر الأسود والداكن.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>صانسيلك (Sunsilk)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / شامبو لمعان الشعر الأسود</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو لمعان وحماية الشعر الأسود (Stunning Black Shine)</td></tr>
  <tr><th>الحجم/الوزن</th><td>400 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>الشعر الأسود والداكن (جميع الأنواع)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر أسود غني، براق، ومفعم باللمعان الكريستالي</td></tr>
  <tr><th>الملمس</th><td>كريمي أسود لؤلؤي يرغي بسهولة</td></tr>
  <tr><th>العطر</th><td>عطر شرقي منعش وأنيق</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة الحبة السوداء، مركب اللؤلؤ، دايميثيكونول، غوار كلورايد</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / مصر (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (يونيليفر)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لحماية لمعان الشعر الأسود وخلاصة الحبة السوداء</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج شامبو صانسيلك لمعان ساحر للشعر الأسود مشكلة بهتان اللون الأسود وشحوب بريقه الناجم عن الأكسدة، التلوث، والأشعة فوق البنفسجية.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>يتأثر صباغ الميلانين الطبيعي في الشعر الداكن بالأشعة الشمسية والحرارة، مما يتسبب في تحلل الجزيئات الصبغية وظهور درجات باهتة ومجهدة على السطح الخارجي للشعر.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام الشامبو المخصص:</strong> استعملي شامبو الحبة السوداء للمحافظة على ألق السواد.<br>
2. <strong>الشطف بالماء الفاتر:</strong> تجنبي الماء الساخن لحماية الصبغات الطبيعية.<br>
3. <strong>حماية الشعر من الشمس:</strong> ارتدي غطاء للرأس عند التعرض الطويل للشمس.<br>
4. <strong>الترطيب ببلسم مكمل:</strong> استخدمي البلسم لإغلاق الحراشف وعكس الضوء.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "شامبوهات الشعر الأسود تصبغ الجلد واليدين."<br>
<strong>الحقيقة:</strong> شامبو صانسيلك يعتمد على مركب اللمعان والحبة السوداء المغذية التي تعزز انعكاس الضوء دون صبغ الجلد.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تعمل خلاصة الحبة السوداء الغنية بالثيموكينون ومضادات الأكسدة على تغذية خلايا الشعر، بينما يشكل مركب اللؤلؤ والسيليكون طبقة فائقة النعومة على سطح الشعرة (Cuticle Mirror Effect) تعكس الضوء وتمنح الشعر الأسود بريقاً كراستالياً ساحراً.</p>"""

    faqs = [
        ("ما هو شامبو صانسيلك لمعان ساحر للشعر الأسود؟", "هو شامبو مخصص للشعر الأسود والداكن، يعزز بريقه وسواده الطبيعي بفضل خلاصة الحبة السوداء ومركب اللمعان اللؤلؤي."),
        ("ما فائدة الحبة السوداء للشعر الأسود؟", "تغذي الحبة السوداء بصلات الشعر، تقوي أليافه، وتحمي اللون الداكن من البهتان والتأكسد."),
        ("هل يصبغ هذا الشامبو اليدين أو الفروة؟", "لا، هو شامبو مغذٍ يعزز بريق وانعكاس الضوء على الشعر ولا يحتوي على صبغات جلدية."),
        ("ما حجم عبوة الشامبو؟", "تأتي العبوة بحجم 400 مل، وهي كمية مناسبة للاستخدام المنتظم."),
        ("هل يناسب الشعر المسبوغ باللون الأسود؟", "نعم، يحافظ على ثبات صبغة الشعر السوداء ويمنع بهتانها."),
        ("هل يناسب الرجال والنساء؟", "نعم، يناسب كلا الجنسين ولكافة أنواع الشعر الأسود والداكن."),
        ("كم مرة يُنصح باستخدامه أسبوعياً؟", "يُنصح باستخدامه من 2 إلى 3 مرات أسبوعياً، وهو آمن للاستخدام اليومي."),
        ("ما هي رائحة شامبو صانسيلك للشعر الأسود؟", "يتميز برائحة عطرية شرقية ناعمة ومنعشة تدوم طوال اليوم."),
        ("هل يترك الشامبو ملمساً دهنياً؟", "لا، ينظف الفروة بكفاءة ويدعم الانسيابية الخفيفة دون أي ثقل."),
        ("هل يمنع تقصف الشعر الأسود؟", "نعم، المواد المغذية والسيروم المدمج يقللان تكسر وتقصف أطراف الشعر."),
        ("ما هو بلد صنع الشامبو؟", "يُصنع بواسطة شركة يونيليفر (Unilever) العالمية في مصانعها المعتمدة."),
        ("هل يحتوي على مركبات البارابين؟", "التركيبة مطورة وخالية من البارابين ومجربة جلدياً."),
        ("هل يساعد في تقليل الهيشان؟", "نعم، ينعم حراشف الشعر ويمنع التأثر بالرطوبة والهيشان."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات صانسيلك لدى صيدلية إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يلزم استخدام بلسم بعد الشامبو؟", "يُفضل استخدام بلسم صانسيلك للشعر الأسود للحصول على أقصى لمعان."),
        ("هل يقلل الشامبو تساقط الشعر؟", "تقوية ألياف الشعر بالحبة السوداء تمنع التساقط الناجم عن التكسر."),
        ("هل يناسب الأطفال؟", "مناسب للمراهقين والأطفال من سن 12 سنة فما فوق."),
        ("هل الشامبو آمن للاستخدام اليومي؟", "نعم، تركيبة لطيفة تناسب الاستخدام المنتظم."),
        ("هل يترك أي بقايا بعد الشطف؟", "لا، يشطف بسهولة وسرعة بالماء الفاتر."),
        ("كيف أحتفظ بالشامبو بالشكل الصحيح؟", "يُحفظ في مكان بارد وجاف بعيداً عن أشعة الشمس المباشرة."),
        ("هل العبوة بحجم 400 مل سهلة الاستخدام؟", "تأتي بتصميم عصري يسهل سكب الشامبو منها بمرونة."),
        ("هل يضيف لمعاناً للشعر الباهت؟", "نعم، ينظف الرواسب ويكسب الشعر الأسود بريقاً كراستالياً."),
        ("هل يحمي من أشعة الشمس؟", "مركب مضادات الأكسدة يقلل تلف الشعر الناجم عن الشمس."),
        ("هل يناسب الشعر الطبيعي والمسبوغ؟", "نعم، مناسب تماماً للشعر الأسود الطبيعي والمصبوغ."),
        ("هل يحتاج لرج العبوة؟", "لا يلزم، القوام متجانس وجاهز للاستخدام المباشر.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Sunsilk Stunning Black Shine Shampoo (400ml)</strong> is an iconic hair wash specially crafted to enhance the natural radiance, deep richness, and luminous shine of black and dark hair. Enriched with natural Black Nigella Seed extract and Pearl Shine Complex, it revives dark hair vitality and protects against fading caused by UV exposure and environmental pollution.</p>
<p>It gently purifies the scalp of sebum and residue while penetrating hair cuticles to deliver deep moisture and light reflection. It leaves black hair looking intensely glossy, touchably soft, and beautifully fragranced all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Stunning Black Shine:</strong> Enhances dark tones, imparting a mirror-like crystal shine under light.</li>
  <li><strong>Enriched with Black Seed Extract:</strong> Nourishes hair roots, fortifies fibers, and reduces breakage.</li>
  <li><strong>Fade & Dullness Protection:</strong> Shields dark hair against environmental damage and UV fading.</li>
  <li><strong>Silky Smoothness:</strong> Leaves hair touchably soft and effortlessly easy to style.</li>
  <li><strong>Gentle Scalp Cleansing:</strong> Removes oils efficiently without stripping protective moisture.</li>
  <li><strong>Safe Daily Wash:</strong> pH-balanced formulation ideal for regular daily application on dark hair.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet hair and scalp thoroughly with warm water.</li>
  <li><strong>Step 2 (Apply):</strong> Dispense an adequate amount of Sunsilk Stunning Black Shine shampoo onto palms.</li>
  <li><strong>Step 3 (Massage):</strong> Gently massage into scalp and hair into a rich lather for 2-3 minutes.</li>
  <li><strong>Step 4 (Rinse):</strong> Rinse completely with warm water until all foam is cleared.</li>
  <li><strong>Step 5 (Condition):</strong> For maximum shine, follow with matching Sunsilk Black Shine Conditioner.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Black Seed Extract (Nigella Sativa Oil):</strong> Fortifies hair fibers and enhances natural deep black radiance.</li>
  <li><strong>Pearl Shine Complex:</strong> Reflects ambient light and shields hair fibers from heat and sun damage.</li>
  <li><strong>Dimethiconol:</strong> Smooths cuticles to reduce friction knots and flyaway frizz.</li>
  <li><strong>Guar Hydroxypropyltrimonium Chloride:</strong> Eases combability across strands.</li>
  <li><strong>Gentle Surfactants:</strong> Clear scalp oils efficiently while keeping hair supple.</li>
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
  <li>Anyone with black or dark hair seeking to amplify natural shine and color richness.</li>
  <li>Individuals experiencing dullness in black hair due to sun exposure or pollution.</li>
  <li>Suitable for daily care across all dark hair types.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Sunsilk</td></tr>
  <tr><th>Category</th><td>Hair Care / Black Hair Shine Shampoos</td></tr>
  <tr><th>Product Type</th><td>Stunning Black Shine Shampoo</td></tr>
  <tr><th>Volume/Weight</th><td>400 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Black & Dark Hair (All Hair Types)</td></tr>
  <tr><th>Finish</th><td>Rich black, shiny, mirror-like crystal finish</td></tr>
  <tr><th>Texture</th><td>Pearlescent black rich fluid</td></tr>
  <tr><th>Fragrance</th><td>Fresh oriental elegant aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Black Seed Extract, Pearl Shine Complex, Dimethiconol</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / Egypt (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Black Seed Extract & Cuticle Light Reflection</h2>

<h3>What problem does this solve?</h3>
<p>Sunsilk Stunning Black Shine Shampoo resolves black hair oxidation, surface dullness, and loss of color vibrancy caused by sunlight, heat styling, and environmental pollutants.</p>

<h3>Why does this condition happen?</h3>
<p>Natural melanin pigments in dark hair oxidize under UV exposure, breaking down color clarity and causing cuticles to become rough, resulting in a dull, lifeless appearance.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Use Black Shine Shampoo:</strong> Use dedicated black hair formulas to preserve color richness.<br>
2. <strong>Lukewarm Water:</strong> Wash with lukewarm water to protect natural pigments.<br>
3. <strong>Sun Protection:</strong> Cover hair during prolonged intense sun exposure.<br>
4. <strong>Conditioning:</strong> Pair with conditioner to seal cuticles and maximize light reflection.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Black hair shampoos stain skin and hands."<br>
<strong>Fact:</strong> Sunsilk Black Shine relies on light-reflecting polymers and nourishing black seed oil without temporary skin dyes.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Black Seed extract (thymoquinone and antioxidants) nourishes follicle cells, while the Pearl Shine Complex forms a mirror-smooth layer over the hair cuticle (Cuticle Mirror Effect), reflecting ambient light to produce a vibrant, multi-dimensional black shine.</p>"""

    en_faqs = [
        ("What is Sunsilk Stunning Black Shine Shampoo?", "It is a specialized shampoo for black and dark hair enriched with Black Seed extract and Pearl Shine Complex to enhance natural shine and color depth."),
        ("What are the benefits of Black Seed extract?", "It nourishes hair roots, strengthens fibers, and protects dark hair color from fading."),
        ("Does this shampoo stain hands or scalp?", "No, it enhances light reflection through nourishing ingredients and does not contain skin dyes."),
        ("What volume is contained in this bottle?", "It comes in a 400ml bottle ideal for regular daily use."),
        ("Is it suitable for black color-treated hair?", "Yes, it protects black hair dye from premature fading."),
        ("Can both men and women use it?", "Yes, it is a unisex formula suitable for all dark hair types."),
        ("How often should I use it?", "Use 2 to 3 times weekly or daily as needed."),
        ("What fragrance does it have?", "It features a pleasing, fresh oriental fragrance."),
        ("Does it leave hair feeling greasy?", "No, it purifies scalp oils while keeping strands lightweight."),
        ("Does it help reduce split ends?", "Yes, conditioning agents reduce mechanical breakage and split ends."),
        ("Where is Sunsilk manufactured?", "It is manufactured by Unilever under strict international quality standards."),
        ("Is the formula paraben-free?", "Yes, modern Sunsilk formulations are paraben-free."),
        ("Does it help reduce frizz?", "Yes, it smooths cuticles to protect against humidity frizz."),
        ("How do I verify authenticity at Ekleel Abha?", "All Sunsilk products at Ekleel Abha are 100% original from certified Unilever Saudi distributors."),
        ("Should I use conditioner afterward?", "Using matching Sunsilk Black Shine conditioner yields maximum shine."),
        ("Does it reduce hair fall from breakage?", "Yes, strengthening hair fibers reduces breakage-induced hair fall."),
        ("Is it suitable for teenagers?", "Yes, safe for adults and teens aged 12+."),
        ("Is it safe for daily use?", "Yes, its gentle formulation supports regular daily washing."),
        ("Does it rinse out easily?", "Yes, it rinses out completely with warm water."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Is the 400ml bottle convenient to handle?", "It features an ergonomic shower bottle design."),
        ("Does it add shine to dull black hair?", "Yes, clearing buildup and smoothing cuticles restores brilliant shine."),
        ("Does it protect against sun damage?", "Antioxidants reduce UV-induced hair degradation."),
        ("Is it suitable for natural and dyed black hair?", "Yes, suitable for both natural and dyed black hair."),
        ("Does it require shaking before use?", "No, its homogeneous formula is ready for direct use.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1711",
        "sku": "EK-1711",
        "gtin": "6281006424562",
        "category": "العناية بالشعر / شامبو لمعان الشعر الأسود",
        "brand": "Sunsilk",
        "ar": {
            "title": "شامبو صانسيلك لمعان ساحر للشعر الأسود، 400 مل",
            "meta_title": "شامبو صانسيلك لمعان ساحر للشعر الأسود 400مل | صيدلية إكليل أبها",
            "meta_description": "اشتري شامبو صانسيلك لمعان ساحر للشعر الأسود (400مل). فرمولة بالحبة السوداء ومركب اللؤلؤ لبريق كراستالي ساحر. أصلي من صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["صانسيلك", "لمعان_ساحر", "الشعر_الاسود", "الحبة_السوداء", "إكليل_أبها"]
        },
        "en": {
            "title": "Sunsilk Stunning Black Shine Shampoo, 400 ml",
            "meta_title": "Sunsilk Stunning Black Shine Shampoo 400ml | Ekleel Abha",
            "meta_description": "Buy Sunsilk Stunning Black Shine Shampoo (400ml). Enhanced with Black Seed & Pearl Complex for deep shine. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["sunsilk", "stunning_black_shine", "black_seed", "shampoo", "ekleel_abha"]
        },
        "schema": {
            "brand": "Sunsilk",
            "category": "Hair Care / Shampoo",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "sunsilk-stunning-black-shine-shampoo-400ml.webp",
            "alt": "Sunsilk Stunning Black Shine Shampoo 400ml",
            "title": "Sunsilk Stunning Black Shine Shampoo 400ml"
        }
    }

def create_product_1714():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول الفم اوبتيك وايت لتبييض الأسنان من كولجيت (Colgate Optic White Mouthwash - 500ml)</strong> حلاً طبياً ورائعاً للحصول على ابتسامة أكثر بياضاً ونفَس خالي من الروائح في آن واحد. يمتاز هذا الغسول بفرمولته المتقدمة الخالية من الكحول التي توفر تبييضاً آامناً للأسنان وحماية من التصبغات دون التسبب في الحرقة المزعجة أو جفاف الفم.</p>
<p>يحتوي الغسول على مركب البيروفوسفات المزدوج والمركبات المنقية التي تمنع تراكم التصبغات السطحية الناتجة عن القهوة والشاي والتطبيب، مع إضافة الفلورايد المقوي لمينا الأسنان لمنع التسوس. يوفر غسول كولجيت اوبتيك وايت انتعاشاً يدوم طوال اليوم وحماية كاملة للفم واللثة عند استخدامه كجزء من روتين العناية اليومي مرتين يومياً.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تبييض آمن ومتقدم للأسنان:</strong> يساعد في إزالة التصبغات السطحية ويمنع تكون بقع جديدة لابتسامة ناصعة.</li>
  <li><strong>تركيبة خالية تماماً من الكحول:</strong> تمنح تنظيفاً وتبييضاً فعالاً دون حرقة أو جفاف لغشاء الفم المخاطي.</li>
  <li><strong>مدعم بالفلورايد لحماية المينا:</strong> يقوي المينا ويحمي الأسنان من النخر والتسوس والمخاطر البكتيرية.</li>
  <li><strong>مكافحة رائحة الفم الكريهة:</strong> يقضي على البكتيريا المسببة للروائح ويمنح نفساً منعشاً يرافقكِ لساعات.</li>
  <li><strong>الحد من تراكم الجير (Tartar):</strong> يحتوي على مركب البيروفوسفات الذي يمنع تكلس البلاك وتحوله لجير صلب.</li>
  <li><strong>مناسب للاستخدام اليومي:</strong> تركيبة لطيفة وآمنة تماماً للاستخدام المنتظم مرتين يومياً.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> نظفي أسنانكِ بالفرشاة والمعجون كالمعتاد.</li>
  <li><strong>الخطوة الثانية (الجرعة):</strong> املئي غطاء العبوة بحوالي 20 مل من غسول كولجيت اوبتيك وايت.</li>
  <li><strong>الخطوة الثالثة (المضمضة):</strong> مضمضي الفم جيداً لمدة 30 ثانية لضمان وصول السائل لكافة زوايا الأسنان واللثة.</li>
  <li><strong>الخطوة الرابعة (البصق):</strong> ابصقي الغسول. للحصول على أفضل النتائج امتنعي عن الأكل أو الشرب لمدة 30 دقيقة.</li>
  <li><strong>الخطوة الخامسة (التكرار):</strong> يُستخدم مرتين يومياً (صباحاً ومساءً) بعد تفريش الأسنان.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>فلوريد الصوديوم (Sodium Fluoride):</strong> يعزز إعادة تمعدن مينا الأسنان ويحمي من التسوس.</li>
  <li><strong>مركب البيروفوسفات (Tetrapotassium & Tetrasodium Pyrophosphate):</strong> يمنع تكلس البلاك ويزيل التصبغات السطحية.</li>
  <li><strong>ستريد الزنك (Zinc Citrate):</strong> مركب مضاد للبكتيريا يقلل التهابات اللثة ويحارب رائحة الفم.</li>
  <li><strong>الجليسرين والسوربيتول:</strong> يمنحان الفم ترطيباً وانتعاشاً ويمنعان جفاف الأغشية المخاطية.</li>
  <li><strong>فرمول خالي من الكحول (Ethanol-Free):</strong> ينظف بلطف دون حرق الأنسجة الفموية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي (مضمضة) فقط؛ يُمنع ابتلاعه.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال دون سن 6 سنوات.</li>
  <li>في حال ابتلاع كمية كبيرة عن طريق الخطأ استشيري الطبيب.</li>
  <li>إذا كنتِ تعانين من تقرحات فموية شديدة استشيري طبيب الأسنان.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحثون عن تبييض آمن للأسنان ونفس منعش دون حرقة الكحول.</li>
  <li>لمحبي القهوة والشاي الباحثين عن حماية أسنانهم من التصبغات اليومية.</li>
  <li>مناسب للبالغين والأطفال فوق سن 6 سنوات.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كولجيت (Colgate)</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم / غسول الفم والتبييض</td></tr>
  <tr><th>نوع المنتج</th><td>غسول فم مبيض ومقوي للمينا (خالٍ من الكحول)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بالفم والأسنان)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان أكثر بياضاً، نفس منعش، وحماية كاملة للمينا</td></tr>
  <tr><th>الملمس</th><td>سائل منعش خفيف</td></tr>
  <tr><th>العطر</th><td>عطر النعناع الثلجي المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>فلوريد الصوديوم، بيروفوسفات، سترات الزنك، جليسرين</td></tr>
  <tr><th>بلد المنشأ</th><td>البرازيل / المكسيك (Colgate-Palmolive)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Colgate-Palmolive</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والأطفال فوق 6 سنوات</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لتقنية تبييض الأسنان وحماية المينا (Colgate Optic White)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول كولجيت اوبتيك وايت مشكلة اصفرار وتصبغ الأسنان الناتجة عن المشروبات الملونة والتدخين، كما يعالج رائحة الفم الكريهة وجفاف الأنسجة الذي تسببه الغسولات المحتوية على الكحول.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تتراكم التصبغات الخارجية على طبقة المينا بفعل العفص والكروموجينات الموجودة بالقهوة والشاي. كما تتكاثر البكتيريا اللاهوائية في جيوب اللثة لتنتج غازات الكبريت المسببة للروائح الكريهة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>المضمضة بعد المشروبات:</strong> مضمضي بالماء أو الغسول فور تناول القهوة.<br>
2. <strong>الالتزام بـ 30 ثانية:</strong> مضمضي لمدة 30 ثانية كاملة لضمان التغطية.<br>
3. <strong>اختيار غسول خالٍ من الكحول:</strong> الكحول يجفف اللعاب مما يفاقم رائحة الفم.<br>
4. <strong>التفريش اليومي:</strong> استخدمي معجون اوبتيك وايت لتعزيز التبييض.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الغسول المبيض يضعف مينا الأسنان."<br>
<strong>الحقيقة:</strong> غسول كولجيت مدعم بالفلورايد الذي يعيد تمعدن المينا ويقويها ضد التسوس أثناء التبييض.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعتمد الغسول على جزيئات البيروفوسفات التي تمنع ارتباط التصبغات بمينا الأسنان وتفكك البلاك، بينما يقوم فلوريد الصوديوم بترسيب الفلوراباتيت على المينا لتقويتها، وتعمل سترات الزنك على القضاء كيميائياً على البكتيريا المسببة للروائح.</p>"""

    faqs = [
        ("ما هو غسول الفم كولجيت اوبتيك وايت؟", "هو غسول فم مبيض خالي من الكحول ومدعم بالفلورايد، مصمم لإزالة التصبغات السطحية وتقوية المينا وانعاش النفس."),
        ("هل يحتوي الغسول على الكحول؟", "لا، هو خالي تماماً من الإيثانول مما يمنح مضمضة مريحة دون أي حرقة أو جفاف للفم."),
        ("كيف يعمل الغسول على تبييض الأسنان؟", "يحتوي على مركبات البيروفوسفات التي تفكك التصبغات السطحية وتمنع تراكم بقع جديدة على المينا."),
        ("هل يحتوي على الفلورايد لحماية الأسنان؟", "نعم، يحتوي على فلوريد الصوديوم الذي يعزز قوة مينا الأسنان ويحميها من التسوس."),
        ("ما حجم عبوة الغسول؟", "تأتي العبوة بحجم 500 مل، وهي كمية وافرة تكفي للاستخدام اليومي لفترة طويلة."),
        ("كيف يتم استخدام الغسول بشكل صحيح؟", "املئي الغطاء بـ 20 مل ومضمضي لمدة 30 ثانية مرتين يومياً بعد تفريش الأسنان ثم ابصقيه."),
        ("هل يجوز ابتلاع الغسول؟", "لا، الغسول مخصص للمضمضة والبصق فقط ويجب عدم ابتلاعه."),
        ("هل يناسب الأطفال؟", "مناسب للأطفال فوق سن 6 سنوات ممن يستطيعون المضمضة والبصق دون ابتلاع."),
        ("هل يساعد في محاربة رائحة الفم الكريهة؟", "نعم، يقتل البكتيريا المسببة للروائح ويحتوي على سترات الزنك والنعناع لانتعاش يدوم."),
        ("هل يسبب الغسول حساسيات الأسنان؟", "لا، تركيبة خالية من الكحول ومدعمة بالمرطبات والفلورايد لحماية الأسنان الحساسة."),
        ("متى تظهر نتائج التبييض؟", "تلاحظين نضارة وانتعاشاً فورياً وتراجعاً للتصبغات مع الاستخدام المنتظم لعدة أسابيع."),
        ("ما هو بلد صنع غسول كولجيت اوبتيك وايت؟", "تم تصنيعه بواسطة شركة كولجيت-بالموليف (Colgate-Palmolive) العالمية."),
        ("هل يساعد في الحد من الجير؟", "نعم، مركبات البيروفوسفات تمنع تكلس البلاك وتحوله إلى جير صلب على الأسنان."),
        ("ما هي رائحة ونكهة الغسول؟", "يتميز بنكهة النعناع الثلجي المنعشة والممتعة."),
        ("هل يناسب مستخدمي تقويم الأسنان؟", "نعم، ممتاز لتنظيف الزوايا الصعبة حول أقواس التقويم وحمايتها من التصبغ."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات كولجيت لدى صيدلية إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يغني الغسول عن تفريش الأسنان؟", "لا، الغسول يكمل التفريش بالفرشاة والمعجون ولا يغني عنه."),
        ("هل يمكن استخدامه قبل النوم؟", "نعم، استخدامه قبل النوم يقلل نشاط البكتيريا ليلاً ويمنع رائحة الفم الصباحية."),
        ("هل يغير لون التركيبات أو التيجان؟", "لا، هو آمن تماماً ولا يؤثر على ألوان التيجان أو الحشوات التجميلية."),
        ("هل يناسب الحوامل؟", "نعم، استخدامه موضعياً وآمن عموماً، ويُفضل استشارة الطبيب المتابع."),
        ("هل يترك طعماً مرّاً في الفم؟", "لا، يترك طعم نعناع منعش ونظيف دون مرارة."),
        ("كم مرة يُنصح باستخدامه يومياً؟", "يُنصح باستخدامه مرتين يومياً (صباحاً ومساءً)."),
        ("ماذا أفعل إذا دخل الغسول في العين؟", "اشطفي العين فوراً بكمية وفيرة من الماء البارد."),
        ("هل العبوة بحجم 500 مل اقتصادية؟", "نعم، تكفي العبوة للاستخدام اليومي لأكثر من شهر."),
        ("هل يمنع التصبغات الناجمة عن القهوة؟", "نعم، يمنع التصاق تصبغات القهوة والشاي بمينا الأسنان.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Colgate Optic White Whitening Mouthwash (500ml)</strong> is an advanced alcohol-free oral care rinse engineered to deliver a visibly whiter smile and long-lasting fresh breath. Formulated without drying ethyl alcohol, it offers gentle yet powerful whitening protection without the uncomfortable burning sensation or oral dry mouth associated with traditional rinses.</p>
<p>Enriched with dual pyrophosphate stain-shield technology and Sodium Fluoride, it actively prevents new surface stains from coffee, tea, and dark foods while reinforcing enamel strength against cavity-causing acids. Used twice daily after brushing, it provides 24-hour freshness and comprehensive oral hygiene protection.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Advanced Stain-Prevention Whitening:</strong> Helps lift surface stains and prevents new dark spots from setting onto enamel.</li>
  <li><strong>100% Alcohol-Free Gentle Formula:</strong> Delivers effective cleansing and whitening without burning sensitive oral tissues.</li>
  <li><strong>Fluoride Enamel Protection:</strong> Strengthens tooth enamel and defends against acid decay and micro-cavities.</li>
  <li><strong>24-Hour Fresh Breath:</strong> Neutralizes odor-causing oral bacteria with a long-lasting icy mint burst.</li>
  <li><strong>Tartar Buildup Control:</strong> Pyrophosphates prevent plaque calcification into hard tartar deposits.</li>
  <li><strong>Safe Daily Oral Wash:</strong> Mild, dermatologist-tested formula safe for twice-daily routine use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Brush):</strong> Thoroughly brush teeth using toothpaste prior to rinsing.</li>
  <li><strong>Step 2 (Dosage):</strong> Fill bottle cap to the 20ml mark with Colgate Optic White mouthwash.</li>
  <li><strong>Step 3 (Swish):</strong> Swish vigorously around the mouth for 30 seconds to reach all tooth surfaces and gums.</li>
  <li><strong>Step 4 (Spit):</strong> Expel the rinse into the sink. Do not swallow. Refrain from eating or drinking for 30 minutes.</li>
  <li><strong>Step 5 (Routine):</strong> Repeat twice daily (morning and evening) for optimal whitening results.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Sodium Fluoride:</strong> Essential mineral active that remineralizes enamel and protects against cavities.</li>
  <li><strong>Tetrapotassium & Tetrasodium Pyrophosphate:</strong> Stain-shield agents preventing plaque calcification and surface discoloration.</li>
  <li><strong>Zinc Citrate:</strong> Antibacterial agent that reduces gum inflammation and neutralizes breath odor.</li>
  <li><strong>Glycerin & Sorbitol:</strong> Humectants retaining mucosal moisture to prevent dry mouth.</li>
  <li><strong>Alcohol-Free Solvent System:</strong> Cleanses thoroughly without burning or drying oral tissues.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external swishing and spitting only; do not swallow.</li>
  <li>Keep out of reach of children under 6 years of age.</li>
  <li>If a large quantity is accidentally swallowed, seek medical advice immediately.</li>
  <li>Discontinue use if severe mouth ulcers or continuous irritation develops.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking gentle, alcohol-free tooth whitening and long-lasting fresh breath.</li>
  <li>Coffee, tea, and soda drinkers looking to shield teeth from daily surface stains.</li>
  <li>Suitable for adults and children over 6 years old.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Colgate</td></tr>
  <tr><th>Category</th><td>Oral Care / Mouthwash & Whitening</td></tr>
  <tr><th>Product Type</th><td>Alcohol-Free Whitening Mouthwash</td></tr>
  <tr><th>Volume/Weight</th><td>500 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Oral Care)</td></tr>
  <tr><th>Finish</th><td>Whiter teeth, fresh breath & enamel protection</td></tr>
  <tr><th>Texture</th><td>Liquid fluid rinse</td></tr>
  <tr><th>Fragrance</th><td>Fresh Icy Mint flavor</td></tr>
  <tr><th>Active Ingredients</th><td>Sodium Fluoride, Pyrophosphates, Zinc Citrate, Glycerin</td></tr>
  <tr><th>Country of Origin</th><td>Brazil / Mexico (Colgate-Palmolive)</td></tr>
  <tr><th>Manufacturer</th><td>Colgate-Palmolive</td></tr>
  <tr><th>Age Group</th><td>Adults & Children 6+</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Alcohol-Free Teeth Whitening & Enamel Defense</h2>

<h3>What problem does this solve?</h3>
<p>Colgate Optic White Mouthwash resolves surface tooth discoloration caused by chromogenic beverages and smoking, while avoiding the oral dry mouth and burning pain caused by alcohol-based rinses.</p>

<h3>Why does this condition happen?</h3>
<p>Tannins and chromogens in coffee, tea, and red wine bond to enamel pellicle proteins, turning teeth yellow over time. Additionally, anaerobic bacteria produce volatile sulfur compounds (VSCs) that cause bad breath.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Rinse After Beverages:</strong> Swish with mouthwash or water after drinking coffee or tea.<br>
2. <strong>Swish for 30 Seconds:</strong> Maintain full 30-second contact time for maximum pyrophosphate action.<br>
3. <strong>Avoid Alcohol Rinses:</strong> Stick to alcohol-free formulas to preserve natural salivary protective enzymes.<br>
4. <strong>Pair with Optic White Paste:</strong> Combine with Optic White toothpaste for synergistic whitening.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Whitening mouthwashes erode tooth enamel."<br>
<strong>Fact:</strong> Colgate Optic White contains Sodium Fluoride, which actively remineralizes and hardens enamel while pyrophosphates lift surface stains safely.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Pyrophosphate ions bind to enamel hydroxyapatite sites, displacing surface chromogens and preventing new stain attachment. Concurrently, Fluoride ions convert hydroxyapatite into acid-resistant fluorapatite, while Zinc Citrate disrupts anaerobic bacterial cell membranes to stop bad breath VSC formation.</p>"""

    en_faqs = [
        ("What is Colgate Optic White Mouthwash?", "It is an alcohol-free whitening rinse enriched with Sodium Fluoride and Pyrophosphates to lift surface stains and freshen breath."),
        ("Does it contain alcohol?", "No, it is 100% ethanol-free, providing a gentle rinse without burning or dry mouth."),
        ("How does it whiten teeth?", "Dual pyrophosphates break down surface coffee and tea stains while preventing new stain attachment."),
        ("Does it contain Fluoride?", "Yes, it contains Sodium Fluoride to remineralize enamel and defend against cavities."),
        ("What size is this bottle?", "It comes in a 500ml bottle providing long-lasting daily usage."),
        ("How do I use it correctly?", "Rinse with 20ml for 30 seconds twice daily after brushing, then spit out without swallowing."),
        ("Is it safe to swallow?", "No, it is designed for rinsing and spitting only; do not swallow."),
        ("Can children use it?", "It is suitable for children over 6 years old who can rinse and spit reliably."),
        ("Does it control bad breath?", "Yes, antibacterial Zinc Citrate and mint flavors neutralize odor-causing bacteria."),
        ("Will it cause tooth sensitivity?", "No, its alcohol-free, fluoride-enriched formula protects sensitive teeth."),
        ("When will I see whitening results?", "Visible stain reduction and fresh breath are noticeable within weeks of consistent use."),
        ("Where is Colgate Optic White manufactured?", "It is manufactured by Colgate-Palmolive under global oral care quality standards."),
        ("Does it help prevent tartar buildup?", "Yes, pyrophosphates prevent plaque calcification into hard tartar."),
        ("What flavor does it have?", "It features an invigorating Icy Mint flavor."),
        ("Is it safe for orthodontic braces?", "Yes, it cleans hard-to-reach areas around brackets safely."),
        ("How do I verify product authenticity at Ekleel Abha?", "All Colgate products at Ekleel Abha are 100% original from certified distributors."),
        ("Does mouthwash replace tooth brushing?", "No, mouthwash complements brushing and flossing but does not replace them."),
        ("Can I use it before sleep?", "Yes, bedtime use reduces overnight bacterial growth and morning breath."),
        ("Does it discolor dental crowns or fillings?", "No, it is completely safe for crowns, veneers, and composite fillings."),
        ("Is it safe during pregnancy?", "Topical oral rinsing is generally safe; consulting your physician is always advised."),
        ("Does it leave a bitter taste?", "No, it leaves a pleasant, clean mint taste."),
        ("How many times daily should I use it?", "Use twice daily (morning and night) after brushing."),
        ("What if it gets into the eyes?", "Rinse eyes immediately with cold water."),
        ("Is the 500ml size economical?", "Yes, it provides over a month of twice-daily rinses."),
        ("Does it prevent coffee stains?", "Yes, pyrophosphates prevent coffee and tea pigments from attaching to enamel.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1714",
        "sku": "EK-1714",
        "gtin": "7891024179482",
        "category": "العناية بالفم / غسول الفم والتبييض",
        "brand": "Colgate",
        "ar": {
            "title": "غسول الفم اوبتيك وايت لتبييض الأسنان من كولجيت - 500 مل",
            "meta_title": "غسول الفم كولجيت اوبتيك وايت 500مل | صيدلية إكليل أبها",
            "meta_description": "اشتري غسول الفم كولجيت اوبتيك وايت للتبييض وحماية المينا (500مل). خالي من الكحول بالنعناع الثلجي. أصلي 100% لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["كولجيت", "اوبتيك_وايت", "غسول_فم", "تبييض_الاسنان", "إكليل_أبها"]
        },
        "en": {
            "title": "Colgate Optic White Mouthwash - 500ml",
            "meta_title": "Colgate Optic White Whitening Mouthwash 500ml | Ekleel Abha",
            "meta_description": "Buy Colgate Optic White Whitening Mouthwash (500ml). Alcohol-free formula with Fluoride & Stain-Shield Pyrophosphates. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["colgate", "optic_white", "mouthwash", "whitening", "ekleel_abha"]
        },
        "schema": {
            "brand": "Colgate",
            "category": "Oral Care / Mouthwash",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "colgate-optic-white-mouthwash-500ml.webp",
            "alt": "Colgate Optic White Mouthwash 500ml",
            "title": "Colgate Optic White Mouthwash 500ml"
        }
    }

def create_product_1726():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم القدم للعناية بالكعب الخشن والمتشقق من فايتيرا (Vatira Foot Cream for Rough and Cracked Heel Care - 100 ml)</strong> حلاً طبياً وتجميلياً متقدماً لعلاج جفاف وتشققات القدمين الشديدة. يدمج هذا الكريم بين الفاعلية المقشرة والمرطبة لمركب اليوريا (Urea) الطبيعي ورغوة زبدة الشيا الغنية وزيت اللوز الحلو، مما يوفر ترميماً مكثفاً لجلد الكعبين الصلب وإعادة النعومة والمرونة لأنسجة الأقدام في فترة قياسية.</p>
<p>تم تصميم الفرمولة بتركيبة متوازنة تتيح الامتصاص السريع دون ترك أي طبقة دهنية مزعجة. يعمل الكريم على إذابة الخلايا الميتة والطبقات المتصلبة، وفي نفس الوقت يتغلغل في عمق الشقوق الجلدية ليغذيها برطوبة مضاعفة ويسرع التئام الأنسجة الجافة، مما يضمن أقداماً ناعمة، صحية، وخالية من الآلام المصاحبة للتشققات.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترميم وتنعيم الكعبين المتشققين:</strong> يذيب طبقات الجلد الصلبة الخشنة ويرمم التشققات في وقت قياسي.</li>
  <li><strong>مدعم بمركب اليوريا (Urea):</strong> يقشر الخلايا الميتة بلطف ويحبس الماء في طبقات الأقدام العميقة.</li>
  <li><strong>تغذية بزبدة الشيا وزيت اللوز:</strong> يزود ألياف الجلد بالمرطبات الغنية والأحماض الدهنية لمنع إعادة الجفاف.</li>
  <li><strong>امتصاص سريع وغير دهني:</strong> يتغلغل فورياً داخل الأنسجة دون ترك أثر زيتي أو لزوجة على الأقدام.</li>
  <li><strong>تخفيف الآلام الناتجة عن التشققات:</strong> يهدئ التهابات الجلد المتهيجة ويمنح شعوراً فورياً بالراحة والنعومة.</li>
  <li><strong>مناسب للاستخدام اليومي:</strong> تركيبة آمنة ومجربة جلدياً تناسب جميع أنواع البشرة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف والتجفيف):</strong> اغسلي قدميكِ جيداً بالماء الفاتر وجففيهما تماماً بمنشفة ناعمة.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية مناسبة من كريم فايتيرا على المناطق الخشنة والمتشققة في الكعبين والقدمين.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي الكريم بلطف بأطراف الأصابع بحركات دائرية حتى يتم امتصاصه كاملاً.</li>
  <li><strong>الخطوة الرابعة (الارتداء):</strong> للحصول على نتائج مضاعفة، يُفضل ارتداء جوارب قطنية بعد وضع الكريم قبل النوم.</li>
  <li><strong>الخطوة الخامسة (الاستمرارية):</strong> يُستخدم مرتين يومياً (صباحاً ومساءً) للحفاظ على كعبين ناعمين دائماً.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>اليوريا (Urea):</strong> مرطب ومقشر قرني طبيعي يذيب الكيراتين المتصلب في الكعبين ويحتفظ بالماء.</li>
  <li><strong>زبدة الشيا (Shea Butter):</strong> تغذي وتطري طبقات الجلد الجافة وترمم حاجز البشرة الحامي.</li>
  <li><strong>زيت اللوز الحلو (Sweet Almond Oil):</strong> يزود الأنسجة بـ فيتامين E والأحماض الدهنية لمنع تشقق الجلد.</li>
  <li><strong>الجليسرين (Glycerine):</strong> يجذب جزيئات الماء لترطيب الكعبين ومنع الجفاف المكرر.</li>
  <li><strong>عوامل تنعيم متطورة:</strong> تمنح الأقدام ملمساً مخملياً وتسرع تجدد الخلايا.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على القدمين والكعبين فقط.</li>
  <li>تجنبي وضع الكريم على الجروح المفتوحة أو الحروق الحديثة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
  <li>في حال حدوث حكة شديدة أو طفح توقفي عن الاستخدام.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعانون من تشققات الكعبين والجفاف الشديد وقسوة جلد القدمين.</li>
  <li>لمن يبحثون عن كريم أقدام طبي غني باليوريا وزبدة الشيا سريع الامتصاص.</li>
  <li>مناسب للرجال والنساء ولجميع أنواع البشرة وخاصة الجافة جداً.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>فايتيرا (Vatira)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات القدمين والكعبين</td></tr>
  <tr><th>نوع المنتج</th><td>كريم علاج الكعب المتشقق والخشن (اليوريا وزبدة الشيا)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (خاصة الأقدام والكعوب الجافة والمتشققة)</td></tr>
  <tr><th>المظهر النهائي</th><td>أقدام ناعمة، كعوب مرممة، وخالية من الخشونة والتشققات</td></tr>
  <tr><th>الملمس</th><td>كريمي غني سريع الامتصاص غير دهني</td></tr>
  <tr><th>العطر</th><td>عطر ناعم ومنعش للقدمين</td></tr>
  <tr><th>المكونات النشطة</th><td>اليوريا، زبدة الشيا، زيت اللوز الحلو، جليسرين</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / تركيا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Vatira Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لتقنية اليوريا وعلاج تشققات القدمين (Vatira Heel Care)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم فايتيرا مشكلة سمك وجفاف وقسوة جلد الكعبين (Heel Calluses) والتراكمات القرنية المتشققة التي تسبب الآلام ومظهراً غير مرغوب فيه للأقدام.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تنشأ تشققات الكعبين نتيجة الضغط الميكانيكي المستمر أثناء المشي أو الوقوف، مع نقص الرطوبة واليوريا في طبقة الجلد السطحية، مما يجعل الجلد يفقد مرونته ويتشقق بفعل الوزن.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام المنتظم لليوريا:</strong> وضعي كريم اليوريا يومياً للحفاظ على ليونة الجلد.<br>
2. <strong>ارتداء الجوارب القطنية:</strong> ارتدي الجوارب ليلاً بعد وضع الكريم لحبس المرطبات.<br>
3. <strong>تجنب نعل الأحذية الصلب:</strong> اختاري أحذية مريحة ذات وسائد كعبية ناعمة.<br>
4. <strong>عدم استخدام الشفرات الحادة:</strong> تجنبي قص الجلد الجاف بالشفرات لتفادي الالتهابات.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الفازلين العادي يكفي لعلاج تشققات الكعبين العميق."<br>
<strong>الحقيقة:</strong> الفازلين يحبس الرطوبة فقط، بينما اليوريا في فايتيرا تفكك الروابط الكيراتينية الميتة وتقشرها وترطب الخلايا العميق.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تعمل اليوريا بتركيزها الطبي بآلية مزدوجة (Keratolytic & Humectant)، حيث تفكك الروابط الهيدروجينية لبروتين الكيراتين المتصلب في طبقة الجلد الميتة لتذويبها، وفي نفس الوقت تجذب الماء لطبقات الأنسجة العميقة، بينما تغلف زبدة الشيا وزيت اللوز الشقوق لتسريع التئام الجروح السطحية.</p>"""

    faqs = [
        ("ما هو كريم فايتيرا للعناية بالكعب الخشن والمتشقق؟", "هو كريم طبي متخصص يجمع بين اليوريا وزبدة الشيا وزيت اللوز لتقشير وترميم تشققات القدمين والكعبين الخشنة."),
        ("ما هي فائدة اليوريا في كريم القدمين؟", "تذيب اليوريا طبقات الجلد الميتة المتصلبة وتجذب الرطوبة لعمق التشققات لترميمها ونعومتها."),
        ("هل يترك الكريم ملمساً زيتيّاً أو لزجاً على القدمين؟", "لا، يتميز بتركيبة سريعة الامتصاص تنفذ داخل الأنسجة دون ترك لزوجة أو أثر زيتي."),
        ("ما حجم عبوة الكريم؟", "تأتي العبوة بحجم 100 مل، وهي كمية وافرة تكفي للاستخدام اليومي لعدة أسابيع."),
        ("متى تظهر نتائج التنعيم والترميم؟", "تلاحظين نعومة فورية من اليوم الأول وتراجعاً ملحوظاً للتشققات خلال 3 إلى 7 أيام من الاستخدام اليومي."),
        ("هل يفضل ارتداء جوارب بعد وضع الكريم؟", "نعم، ارتداء جوارب قطنية ليلاً بعد تطبيق الكريم يضاعف الامتصاص وسرعة التئام التشققات."),
        ("هل يناسب الكريم مرضى السكري؟", "نعم، يعتبر كريم اليوريا ممتازا ورائعا لترطيب أقدام مرضى السكري والوقاية من التشققات (مع تجنب التطبيق على الجروح المفتوحة)."),
        ("هل يناسب الرجال والنساء؟", "نعم، هو مناسب جداً لكلا الجنسين ولكافة حالات جفاف القدمين."),
        ("كم مرة يُنصح باستخدامه يومياً؟", "يُنصح باستخدامه مرتين يومياً (صباحاً ومساءً قبل النوم)."),
        ("ما هي رائحة كريم فايتيرا للقدمين؟", "يتميز برائحة لطيفة وناعمة تمنح شعوراً بالنظافة والانتعاش للقدمين."),
        ("هل يمكن استخدامه على الركبتين والأكواع الخشنة؟", "نعم، ممتاز جداً لتنعيم وتقشير خشونة الأكواع والركبتين والمناطق الجافة بالجسم."),
        ("ما هو بلد صنع كريم فايتيرا؟", "تم تصنيعه وفق أعلى المعايير الطبية والتجميلية للعناية بالبشرة."),
        ("هل يساعد في تخفيف آلام تشققات الكعبين؟", "نعم، ترطيب التشققات العميقة يقلل الشد والآلام المصاحبة للمشي."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات فايتيرا لدى صيدلية إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يمنع عودة التشققات مجدداً؟", "نعم، الاستخدام المنتظم يحافظ على مرونة الجلد ويمنع تكون طبقات قاسية جديدة."),
        ("هل يحتوي على زبدة الشيا وزيت اللوز؟", "نعم، مدعم بزبدة الشيا وزيت اللوز الحلو لترطيب وتغذية الأنسجة الجافة."),
        ("هل يناسب جميع أنواع البشرة؟", "نعم، مناسب للبشرة العادية والجافة والشديدة الجفاف."),
        ("هل يسبب تهيج الجلد؟", "تركيبته لطيفة ومجربة جلدياً، ولكن يُجنب وضعه على الجروح المفتوحة."),
        ("كيف أحتفظ بالكريم بالشكل الصحيح؟", "يُحفظ في مكان بارد وجاف بعيداً عن أشعة الشمس المباشرة."),
        ("هل العبوة بحجم 100 مل سهلة الاستخدام؟", "تأتي بتصميم أنبوب مريح يسهل ضغط الكريم منه بمرونة."),
        ("هل يلزم غسل القدمين قبل وضع الكريم؟", "نعم، يُفضل غسل القدمين بالماء وتجفيفهما لضمان أفضل امتصاص."),
        ("هل يساعد في التخلص من رائحة القدمين؟", "نعم، حماية الجلد من البكتيريا والجفاف يقلل الروائح المزعجة."),
        ("هل يناسب كبار السن؟", "نعم، ممتاز جداً لكبار السن الذين يعانون من جفاف جلد القدمين القاسي."),
        ("هل يمكن استخدامه صيفاً وشتاءً؟", "نعم، مناسب للاستخدام في كافة فصول السنة لحماية الكعبين."),
        ("هل يلزم حك الكعب بالحجر قبل وضعه؟", "يمكن استخدام حجر القدمين بلطف مرة أسبوعياً، ولكن الكريم يعمل تلقائياً على التقشير باليوريا.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Vatira Foot Cream for Rough and Cracked Heel Care (100 ml)</strong> is an advanced dermatological foot care treatment formulated to repair severe heel cracking, roughness, and thickened skin calluses. Combining the keratolytic exfoliation and deep moisture-binding power of natural Urea with rich Shea Butter and Sweet Almond Oil, this intensive balm transforms hard, painful heels into soft, supple skin in record time.</p>
<p>Boasting a non-greasy, fast-absorbing texture, it dissolves dead skin cells and tough keratin layers while penetrating deep into micro-fissures to repair damaged tissues. It relieves discomfort caused by deep cracking, locks in essential moisture, and leaves feet feeling smoothly restored and healthy.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intensive Cracked Heel Repair:</strong> Dissolves tough calluses and seals micro-cracks in heels rapidly.</li>
  <li><strong>Powered by Medical-Grade Urea:</strong> Gently exfoliates dead skin layers while pulling moisture deep into tissue cells.</li>
  <li><strong>Enriched with Shea Butter & Almond Oil:</strong> Delivers essential lipids and fatty acids to nourish dry skin.</li>
  <li><strong>Fast-Absorbing & Non-Greasy:</strong> Penetrates rapidly into tissues without leaving a tacky or oily foot residue.</li>
  <li><strong>Relieves Heel Fissure Discomfort:</strong> Calms irritated, sore cracked skin, delivering instant walking comfort.</li>
  <li><strong>Safe Daily Foot Care:</strong> Dermatologically safety-tested formula suitable for everyday routine use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse & Dry):</strong> Wash feet thoroughly with warm water and dry completely with a clean towel.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a generous amount of Vatira foot cream directly onto dry, cracked heel areas.</li>
  <li><strong>Step 3 (Massage):</strong> Gently massage in circular motions using fingertips until fully absorbed into skin.</li>
  <li><strong>Step 4 (Cotton Socks):</strong> For enhanced overnight repair, put on clean cotton socks after application before sleep.</li>
  <li><strong>Step 5 (Routine):</strong> Apply twice daily (morning and evening) to maintain smooth, healthy heels.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Urea:</strong> Natural keratolytic agent that breaks down hard keratin bonds and locks water inside deep skin layers.</li>
  <li><strong>Shea Butter (Butyrospermum Parkii):</strong> Nourishes and softens rigid epidermal layers, rebuilding the lipid barrier.</li>
  <li><strong>Sweet Almond Oil (Prunus Amygdalus Dulcis):</strong> Supplies essential Vitamin E and fatty acids to enhance skin elasticity.</li>
  <li><strong>Glycerin:</strong> Powerful humectant attracting water molecules to protect against recurring dryness.</li>
  <li><strong>Softening Emollients:</strong> Restore skin smoothness and accelerate healthy epidermal cell turnover.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external application on feet and heels only.</li>
  <li>Do not apply onto open bleeding wounds or fresh burns.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
  <li>Discontinue use if severe irritation develops.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from severe heel fissures, rough calluses, or extreme foot dryness.</li>
  <li>Individuals seeking a fast-absorbing medical Urea foot cream enriched with Shea Butter.</li>
  <li>Suitable for men and women across all skin types, especially very dry skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Vatira</td></tr>
  <tr><th>Category</th><td>Skincare / Foot & Heel Creams</td></tr>
  <tr><th>Product Type</th><td>Rough & Cracked Heel Repair Foot Cream</td></tr>
  <tr><th>Volume/Weight</th><td>100 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Dry, Rough & Cracked Heels)</td></tr>
  <tr><th>Finish</th><td>Soft, deeply hydrated, smooth & fissure-free feet</td></tr>
  <tr><th>Texture</th><td>Rich non-greasy fast-absorbing cream</td></tr>
  <tr><th>Fragrance</th><td>Subtle fresh clean foot aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Urea, Shea Butter, Sweet Almond Oil, Glycerin</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / Turkey</td></tr>
  <tr><th>Manufacturer</th><td>Vatira Laboratories</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Urea Keratolysis & Heel Fissure Repair</h2>

<h3>What problem does this solve?</h3>
<p>Vatira Foot Cream resolves hyperkeratosis, thick heel calluses, and painful fissures caused by excessive skin dryness and mechanical pressure.</p>

<h3>Why does this condition happen?</h3>
<p>Heel cracks form when standing weight exerts pressure on epidermal layers depleted of natural Urea and lipids. Rigid, inelastic skin splits under mechanical stress, forming deep, painful fissures.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Daily Urea Cream:</strong> Apply Urea cream daily to maintain elasticity.<br>
2. <strong>Wear Cotton Socks:</strong> Wear socks after applying cream at night to seal in moisture.<br>
3. <strong>Cushioned Footwear:</strong> Choose supportive footwear with soft heel cushioning.<br>
4. <strong>Avoid Sharp Blades:</strong> Do not shave calluses with razor blades to avoid infection.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Plain petroleum jelly heals deep cracked heels effectively."<br>
<strong>Fact:</strong> Petroleum jelly only traps surface moisture, whereas Urea in Vatira dissolves hard dead keratin bonds while hydrating deep tissues.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Urea functions via dual keratolytic and humectant pathways. It disrupts hydrogen bonds holding rigid keratin proteins together, gently dissolving dead skin layers while drawing water into deep dermal cells. Concurrently, Shea Butter and Almond Oil lipids seal fissures to accelerate tissue recovery.</p>"""

    en_faqs = [
        ("What is Vatira Foot Cream for Rough & Cracked Heels?", "It is a specialized foot cream enriched with Urea, Shea Butter, and Sweet Almond Oil to exfoliate calluses and repair cracked heels."),
        ("What is the role of Urea in foot care?", "Urea dissolves hard dead keratin calluses while pulling moisture deep into tissue fissures."),
        ("Does it leave feet feeling greasy or slippery?", "No, it features a fast-absorbing formula that penetrates deeply without leaving oily residue."),
        ("What volume is contained in this tube?", "It comes in a 100ml tube ideal for several weeks of daily care."),
        ("How fast will I see results?", "Softness is noticeable from day one, with visible fissure repair within 3 to 7 days of daily use."),
        ("Is wearing cotton socks recommended after application?", "Yes, wearing cotton socks overnight enhances cream absorption and speeds up fissure healing."),
        ("Is it safe for diabetic foot care?", "Yes, Urea cream is highly recommended for diabetic foot moisturization (avoid open bleeding wounds)."),
        ("Can both men and women use it?", "Yes, it is a unisex formula suitable for anyone with rough or cracked heels."),
        ("How many times daily should I apply it?", "Apply twice daily (morning and evening before sleep)."),
        ("What fragrance does Vatira foot cream have?", "It features a subtle, fresh, clean aroma."),
        ("Can it be used on rough knees and elbows?", "Yes, it works wonderfully to soften and exfoliate rough knees and elbows."),
        ("Where is Vatira manufactured?", "It is manufactured according to strict medical cosmetic quality standards."),
        ("Does it help relieve heel walking pain?", "Yes, hydrating deep fissures reduces skin tension and walking discomfort."),
        ("How do I verify authenticity at Ekleel Abha?", "All Vatira products at Ekleel Abha are 100% genuine from certified distributors."),
        ("Does regular use prevent recurring cracks?", "Yes, daily use maintains skin flexibility, preventing new calluses from forming."),
        ("Does it contain Shea Butter and Almond Oil?", "Yes, it incorporates Shea Butter and Sweet Almond Oil to nourish dry tissues."),
        ("Is it suitable for all skin types?", "Yes, ideal for dry, extremely dry, and rough skin types."),
        ("Does it cause skin irritation?", "It is dermatologically safety-tested; avoid applying onto open bleeding wounds."),
        ("How should I store the cream?", "Store in a cool, dry place away from direct sunlight."),
        ("Is the 100ml tube easy to use?", "It comes in a convenient squeeze tube for easy application."),
        ("Should I wash my feet before applying?", "Yes, washing and drying feet beforehand ensures maximum absorption."),
        ("Does it help reduce foot odor?", "Yes, keeping foot skin hydrated and barrier-protected reduces odor-causing bacteria."),
        ("Is it suitable for seniors?", "Yes, it is excellent for seniors suffering from dry, rigid foot skin."),
        ("Can it be used year-round?", "Yes, it is ideal for year-round foot protection in summer and winter."),
        ("Do I need to use a pumice stone before applying?", "Gentle pumice use weekly is optional, but Urea naturally exfoliates dead skin automatically.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1726",
        "sku": "EK-1726",
        "gtin": "6286030000164",
        "category": "العناية بالبشرة / كريمات القدمين والكعبين",
        "brand": "Vatira",
        "ar": {
            "title": "كريم القدم للعناية بالكعب الخشن والمتشقق 100 مل",
            "meta_title": "كريم القدم للعناية بالكعب الخشن والمتشقق فايتيرا 100مل | إكليل أبها",
            "meta_description": "اشتري كريم فايتيرا لعلاج الكعب المتشقق والخشن (100مل). فرمولة باليوريا وزبدة الشيا لترميم وتنعيم القدمين بسرعة. أصلي من صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["فايتيرا", "كريم_القدمين", "الكعب_المتشقق", "اليوريا", "إكليل_أبها"]
        },
        "en": {
            "title": "Foot Cream for Rough and Cracked Heel Care - 100 ml",
            "meta_title": "Vatira Foot Cream Rough Cracked Heel Care 100ml | Ekleel Abha",
            "meta_description": "Buy Vatira Foot Cream for Rough & Cracked Heel Care (100ml). Fast-absorbing formula with Urea & Shea Butter. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["vatira", "foot_cream", "cracked_heel", "urea", "ekleel_abha"]
        },
        "schema": {
            "brand": "Vatira",
            "category": "Skincare / Foot Care",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "vatira-foot-cream-for-rough-and-cracked-heel-care-100ml.webp",
            "alt": "Vatira Foot Cream for Rough and Cracked Heel Care 100ml",
            "title": "Vatira Foot Cream for Rough and Cracked Heel Care 100ml"
        }
    }

print("Loaded Batch 6 builders")
