import json, os
from build_hair_mask import build_hair_mask_product

def create_product_1736():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعتبر <strong>كريم كاب سنفرة ومبيض للوجه والجسم (Krem Kap Face and Body Scrub and Whitening Cream - 500g)</strong> أسطورة التقشير الإيطالي والحل الأكثر شهرة وثقة لدى النساء والمشاطات لإعادة النضارة والتفتيح الفوري لجلد الوجه والجسم. يجمع هذا المستحضر الفريد بين تقنية التقشير الفيزيائي المباشر بحبيبات الألومينا الخفيفة، والخصائص الممتصة للمظاهر الزهمية بفضل طين الكاولين النقي، مما يزيل خلايا الجلد الميتة والتصفيات السطحية بفاعلية مذهلة.</p>
<p>يمتاز كريم كاب بتركيبة كريمية فاخرة تعيد توازن رطوبة الوجه والجسم، حيث ينظف المسام العميقة من الترسبات والزيوت المتراكمة، ويساعد على تفتيح المناطق الداكنة (مثل الأكواع، الركبتين، والمناطق الحساسة) وإكساب الجلد ملمساً مخملياً ناعماً ولوناً متجانساً ومشرقاً في دقائق معدودة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>سنفرة وتقشير مزدوج للوجه والجسم:</strong> يزيل خلايا الجلد الميتة والشوائب السطحية بفاعلية وأمان.</li>
  <li><strong>تفتيح وتوحيد لون البشرة:</strong> يقلل التصبغات الداكنة في الأكواع والركبتين والجسم، ويمنح نضارة فورية.</li>
  <li><strong>مدعم بطين الكاولين (Kaolin):</strong> يمتص الزيوت والدهون الزائدة وينظف المسام العميقة من الرواسب.</li>
  <li><strong>حبيبات تقشير ناعمة (Alumina Micro-Beads):</strong> تقشر الجلد ببطء ولطف دون التسبب في خدوش أو تهيج.</li>
  <li><strong>ملمس مخملي ونعومة فائقة:</strong> ينعم البشرة الخشنة ويتركها طرية وسلسة ومفعمة بالحيوية.</li>
  <li><strong>عبوة اقتصادية 500 جم:</strong> حجم كبير يضمن عناية متكاملة ومستمرة للوجه والجسم لعدة أشهر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف والتبليل):</strong> بلي بشرة الوجه أو الجسم بالماء الفاتر لفتح المسام وتجهيز الجلد.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي كمية مناسبة من كريم كاب على المنطقة المطلوبة ووزعيها بالتساوي.</li>
  <li><strong>الخطوة الثالثة (السنفرة والتدليك):</strong> دلكي البشرة بلطف بحركات دائرية خفيفة لمدة 1 إلى 5 دقائق.</li>
  <li><strong>الخطوة الرابعة (الشطف):</strong> اشطفي البشرة جيداً بالماء الفاتر حتى إزالة كافة حبيبات السنفرة.</li>
  <li><strong>الخطوة الخامسة (الترطيب والتكرار):</strong> رطبي بشرتكِ بمرطبكِ المفضل بعد السنفرة؛ يُستخدم من 1 إلى 3 مرات أسبوعياً.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>طين الكاولين الطبيعي (Kaolin):</strong> يمتص الدهون والشوائب وينقي المسام دون تجفيف الجلد.</li>
  <li><strong>دقيق الألومينا (Alumina Micro-particles):</strong> حبيبات دقيقة تقشر طبقات الجلد الميتة وتصقل سطح البشرة.</li>
  <li><strong>شمع البارافين وحمض الستياريك:</strong> يمنحان كريم السنفرة قواماً ناعماً يرطب البشرة أثناء التقشير.</li>
  <li><strong>ستيارات الجليسرين (Glyceryl Stearate):</strong> مطرٍ طبيعي ينعم ألياف البشرة الخشنة.</li>
  <li><strong>عطر كريم كاب الكلاسيكي:</strong> يمنح الوجه والجسم عبيراً إيطالياً منعشاً وأنيقاً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الوجه والجسم فقط.</li>
  <li>تجنبي ملامسة كريم السنفرة المباشرة للعينين؛ وفي حال ملامستهما اشطفي بالماء الفاتر.</li>
  <li>لا تستخدمي السنفرة على حبوب الشباب الالتهابية المفتوحة أو الجروح الحديثة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من شحوب الوجه، التصبغات السطحية، أو خشونة جلد الجسم والأكواع والركبتين.</li>
  <li>لمن تبحث عن سنفرة إيطالية فاخرة تجمع بين التقشير والتفتيح والنظافة العميقة.</li>
  <li>مناسب لجميع أنواع البشرة (الوجه والجسم) ولجميع الأعمار.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كريم كاب (Krem Kap)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / مقشرات وسنفرة الوجه والجسم</td></tr>
  <tr><th>نوع المنتج</th><td>كريم سنفرة ومبيض للوجه والجسم (500g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (الوجه والجسم)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة، متجانسة، مشدودة ومفعمة بالنضارة</td></tr>
  <tr><th>الملمس</th><td>كريمي كثيف مع حبيبات سنفرة دقيقة</td></tr>
  <tr><th>العطر</th><td>عطر كاب الكلاسيكي المنعش واللطيف</td></tr>
  <tr><th>المكونات النشطة</th><td>طين الكاولين، ألومينا، ستيارات الجليسرين، بارافين</td></tr>
  <tr><th>بلد المنشأ</th><td>إيطاليا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Krem Kap Italy / Nazih Group</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (من 15 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لتقنية السنفرة والتفتيح بالتقشير الفيزيائي (Krem Kap)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم كاب سنفرة ومبيض مشكلة تراكم خلايا الجلد الميتة، اسمرار الأكواع والركبتين، انسداد المسام بالرواسب الزهمية، وشحوب الوجه الناتج عن بطء التجدد الخلوي.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تتجمع خلايا البشرة الميتة على السطح الخارجي بفعل التلوث والجفاف، مما يمنع امتصاص كريمات الترطيب ويشكل طبقة داكنة خشنة تمتص الضوء وتظهر البشرة بشكل باهت ومجهد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>السنفرة المنتظمة:</strong> استعملي سنفرة كاب 1 إلى 2 مرة أسبوعياً للوجه و 2-3 مرات للجسم.<br>
2. <strong>الترطيب المباشر بعد السنفرة:</strong> وضعي كريم الترطيب فوراً لحبس الماء في الخلايا النظيفة.<br>
3. <strong>التدليك ببطء:</strong> دلكي بحركات دائرية خفيفة دون ضغط مفرط على الوجه.<br>
4. <strong>استخدام واقي الشمس:</strong> وضعي واقي الشمس بعد التقشير لحماية الخلايا الجديدة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "السنفرة اليومية تفتّح البشرة أسرع."<br>
<strong>الحقيقة:</strong> التقشير اليومي المفرط يضعف حاجز البشرة الواقي؛ الاستخدام المعتدل 2-3 مرات أسبوعياً هو المفتاح لتفتيح آمن ومستمر.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعتمد المنتج على تقنية التقشير الدقيق (Micro-Dermabrasion). تقوم حبيبات الألومينا بفصل الخلايا الميتة في الطبقة القرنية، بينما ينجذب طين الكاولين للدهون الزائدة والشوائب في المسام لتطهيرها، مما يسارع تجدد خلايا البشرة ويكشف عن طبقة فتية ناعمة وأكثر تفتيحاً.</p>"""

    faqs = [
        ("ما هو كريم كاب سنفرة ومبيض للوجه والجسم؟", "هو كريم سنفرة إيطالي فاخر 500 جم يجمع بين حبيبات الألومينا وطين الكاولين لتقشير الخلايا الميتة وتفتيح الوجه والجسم."),
        ("ما فائدة طين الكاولين وحبيبات الألومينا في كريم كاب؟", "يمتص طين الكاولين الدهون والشوائب من المسام، بينما تقشر حبيبات الألومينا الخلايا الميتة وتصقل البشرة."),
        ("هل يمكن استخدام كريم كاب للوجه والجسم معاً؟", "نعم، هو مصمم خصيصاً ليناسب سنفرة وتقشير بشرة الوجه وكافة مناطق الجسم ب أمان."),
        ("ما حجم عبوة كريم كاب؟", "تأتي العبوة بحجم كبير يبلغ 500 جم، وهي كمية اقتصادية تكفي لأشهر من الاستخدام المنتظم."),
        ("هل يساعد كريم كاب في تفتيح الأكواع والركبتين؟", "نعم، ممتاز جداً لإزالة الجلد الميت الداكن في الأكواع، الركبتين، والأقدام وتوحيد لونها."),
        ("كم مرة يُنصح باستخدام كريم كاب أسبوعياً؟", "يُنصح باستخدامه من 1 إلى 2 مرة أسبوعياً للوجه، ومن 2 إلى 3 مرات للجسم."),
        ("كيف يتم تطبيق كريم كاب بالشكل الصحيح؟", "وضعي الكريم على بشرة مبللة بالماء الفاتر، دلكي بلطف بحركات دائرية من 1-5 دقائق ثم اشطفي بالماء."),
        ("هل يناسب كريم كاب البشرة الحساسة؟", "نعم، لكن يُفضل تدليكه برفق شديد ودون ضغط مفرط على الوجه للبشرة الحساسة."),
        ("ما هو بلد صنع كريم كاب الأصلي؟", "صُنع هذا المنتج بفخر في إيطاليا وفق أعلى معايير الجودة الأوربية."),
        ("هل يحتوي الكريم على عطر؟", "يتميز برائحة ناعمة وأنيقة تمنح شعوراً بالنظافة والانتعاش."),
        ("هل يجب ترطيب البشرة بعد كريم كاب؟", "نعم، يُفضل دائماً وضع كريمكِ المرطب المفضل بعد السنفرة لحبس الترطيب."),
        ("هل يزيل كريم كاب الرؤوس السوداء؟", "نعم، تنظيف المسام بطين الكاولين والتقشير يقلل مظهر الرؤوس السوداء بفاعلية."),
        ("هل يمكن استخدامه قبل إزالة الشعر بالواكس أو الشفرة؟", "نعم، السنفرة قبل إزالة الشعر تمنع نمو الشعر تحت الجلد (جلد الدجاجة) ويسهل العملية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع عبوات كريم كاب لدى صيدلية إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين بشركة نزيح."),
        ("هل يسبب كريم كاب حرقاناً للبشرة؟", "لا يسبب حرقاناً، ولكن ينبغي تجنب وضعه على الجروح المفتوحة أو الحبوب الملتهبة."),
        ("هل يناسب الرجال والنساء؟", "نعم، هو مناسب لكلا الجنسين ولجميع الأعمار."),
        ("هل يناسب الأطفال؟", "مناسب للمراهقين والبالغين من سن 15 سنة فما فوق."),
        ("هل يترك أي أثر دهني على الوجه؟", "لا، يشطف بسهولة وسرعة بالماء الفاتر ليترك البشرة ناعمة ونظيفة."),
        ("كيف أحتفظ بالكريم بالشكل الصحيح؟", "يُحفظ في مكان بارد وجاف بعيداً عن حرارة الاستحمام المباشرة."),
        ("هل يمنح تفتيحاً فورياً؟", "إزالة طبقة الجلد الميت يمنح إشراقة وتفتيحاً ملحوظاً من الاستخدام الأول."),
        ("هل يساعد في إزالة آثر التسمير (التان)؟", "نعم، يساعد في التخلص من التبقع والتسمير السطحي الناتج عن الشمس."),
        ("هل العبوة بحجم 500 جم سهلة الاستخدام؟", "تأتي في عبوة دائرية متينة بغطاء محكم يسهل غرف الكريم منها بمرونة."),
        ("هل يمكن خلطه مع زيوت طبيعية؟", "يمكن خلطه مع قطرات من زيت الأرجان أو اللوز لزيادة الترطيب أثناء سنفرة الجسم."),
        ("هل يسبب جفافاً للبشرة؟", "مكوناته المرطبة تمنع الجفاف، لكن الترطيب بعد السنفرة يعزز النتيجة."),
        ("هل يلزم غسل الوجه بغسول بعد السنفرة؟", "لا يلزم، ينظف كريم كاب البشرة بفاعلية ويشطف بالماء فقط.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Krem Kap Face and Body Scrub and Whitening Cream (500g)</strong> is an iconic Italian micro-dermabrasion scrub renowned worldwide for restoring immediate radiance, smoothness, and brightness to facial and body skin. Formulated with physical alumina micro-exfoliants and oil-absorbing Kaolin clay, it safely lifts away dead skin cells, impurities, and surface discoloration.</p>
<p>Boasting a rich, creamy Italian formula, Krem Kap purifies deep pores from accumulated sebum and pollutants. It effectively lightens stubborn dark patches on elbows, knees, and body areas while imparting a velvety soft texture and an even, glowing complexion within minutes.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Dual Face & Body Micro-Exfoliation:</strong> Removes dead skin cells, debris, and surface impurities safely.</li>
  <li><strong>Complexion Whitening & Tone Unification:</strong> Fades dark spots on knees, elbows, and body, revealing instant brightness.</li>
  <li><strong>Enriched with Pure Kaolin Clay:</strong> Absorbs excess oils and clarifies deep pores from trapped pollutants.</li>
  <li><strong>Gentle Alumina Micro-Beads:</strong> Exfoliates smoothly without causing micro-tears or skin irritation.</li>
  <li><strong>Velvety Soft Texture:</strong> Smooths rough skin patches, leaving skin touchably soft and supple.</li>
  <li><strong>Generous 500g Value Jar:</strong> Large capacity ensuring months of comprehensive face and body care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse & Dampen):</strong> Dampen face or body skin with warm water to prepare cuticles.</li>
  <li><strong>Step 2 (Apply):</strong> Apply an adequate amount of Krem Kap scrub onto target areas and spread evenly.</li>
  <li><strong>Step 3 (Exfoliate):</strong> Massage gently using light circular motions for 1 to 5 minutes.</li>
  <li><strong>Step 4 (Rinse):</strong> Rinse thoroughly with warm water until all micro-beads are washed off.</li>
  <li><strong>Step 5 (Moisturize):</strong> Apply your favorite moisturizer after scrubbing; use 1 to 3 times weekly.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Kaolin Clay:</strong> Absorbs sebum and detoxifies deep pores without stripping natural moisture.</li>
  <li><strong>Alumina Micro-Particles:</strong> Precision exfoliating beads that buff away dead skin cells smoothly.</li>
  <li><strong>Paraffin Wax & Stearic Acid:</strong> Provide a rich cream base that cushions and hydrates skin during exfoliation.</li>
  <li><strong>Glyceryl Stearate:</strong> Conditioning emollient that softens rough skin texture.</li>
  <li><strong>Italian Signature Fragrance:</strong> Imparts a fresh, luxurious, clean aroma.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on face and body only.</li>
  <li>Avoid direct contact with eyes; rinse immediately with warm water if contact occurs.</li>
  <li>Do not apply on open acne lesions or fresh skin wounds.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dull skin, surface discoloration, or rough skin patches on knees, elbows, and body.</li>
  <li>Individuals looking for a premium Italian dual whitening scrub and face mask treatment.</li>
  <li>Suitable for all skin types (face and body) across all ages.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Krem Kap</td></tr>
  <tr><th>Category</th><td>Skincare / Face & Body Scrubs</td></tr>
  <tr><th>Product Type</th><td>Dual Whitening Face & Body Scrub Cream</td></tr>
  <tr><th>Volume/Weight</th><td>500 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Face & Body)</td></tr>
  <tr><th>Finish</th><td>Soft, radiant, even-toned, smooth skin</td></tr>
  <tr><th>Texture</th><td>Rich cream with fine micro-exfoliating beads</td></tr>
  <tr><th>Fragrance</th><td>Fresh classic Italian aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Kaolin Clay, Alumina Micro-Beads, Glyceryl Stearate</td></tr>
  <tr><th>Country of Origin</th><td>Italy</td></tr>
  <tr><th>Manufacturer</th><td>Krem Kap Italy / Nazih Group</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens (15+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Micro-Dermabrasion & Kaolin Clay Exfoliation</h2>

<h3>What problem does this solve?</h3>
<p>Krem Kap Face & Body Scrub resolves dead skin cell accumulation, rough elbow/knee textures, dark spots, and dull complexion caused by slowed cellular turnover.</p>

<h3>Why does this condition happen?</h3>
<p>Environmental pollutants and natural cell desquamation leave a layer of dead keratinized cells on the skin surface. This layer traps oils, blocks moisture absorption, and scatters light unevenly, making skin appear dull and dark.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Regular Exfoliation:</strong> Use 1-2 times weekly for face, 2-3 times for body.<br>
2. <strong>Moisturize Immediately:</strong> Apply hydrating cream directly after scrubbing to seal moisture.<br>
3. <strong>Gentle Massage:</strong> Massage in light circular motions without excessive pressure.<br>
4. <strong>Sunscreen Application:</strong> Always wear sunscreen after exfoliating to protect fresh skin cells.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Scrubbing daily whitens skin faster."<br>
<strong>Fact:</strong> Over-exfoliating damages the skin barrier; moderate 2-3 times weekly use is key to safe, sustainable brightening.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Krem Kap utilizes physical micro-dermabrasion technology. Precision Alumina micro-beads dislodge dead stratum corneum cells, while porous Kaolin clay binds excess sebum and impurities inside pores. This accelerates epidermal cell renewal, revealing smooth, radiant, brightened skin underneath.</p>"""

    en_faqs = [
        ("What is Krem Kap Face and Body Scrub?", "It is an Italian 500g dual whitening scrub combining Alumina micro-beads and Kaolin clay to exfoliate dead cells and brighten skin."),
        ("How do Kaolin clay and Alumina beads work?", "Kaolin clay absorbs deep pore oil and impurities, while Alumina beads buff away dead skin cells for smooth radiance."),
        ("Can it be used on both face and body?", "Yes, it is specially formulated to safely exfoliate and brighten both facial skin and body areas."),
        ("What volume is contained in this tub?", "It comes in a large 500g tub providing exceptional value for extended usage."),
        ("Does Krem Kap help lighten knees and elbows?", "Yes, it is highly effective for buffing away dark, rough skin on knees, elbows, and feet."),
        ("How many times weekly should I use it?", "Use 1 to 2 times weekly for facial skin, and 2 to 3 times weekly for body care."),
        ("How do I apply Krem Kap correctly?", "Apply onto damp skin, massage gently in circular motions for 1-5 minutes, then rinse with warm water."),
        ("Is Krem Kap suitable for sensitive skin?", "Yes, but massage very gently without excessive pressure when applying to sensitive facial skin."),
        ("Where is original Krem Kap manufactured?", "It is proudly manufactured in Italy following strict European cosmetic standards."),
        ("Does it contain fragrance?", "It features a clean, fresh classic Italian aroma."),
        ("Should I moisturize after using Krem Kap?", "Yes, always apply your favorite moisturizer after scrubbing to lock in hydration."),
        ("Does it help reduce blackheads?", "Yes, clearing deep pore oils with Kaolin clay helps minimize blackheads."),
        ("Can I use it before waxing or shaving?", "Yes, scrubbing prior to hair removal prevents ingrown hairs and ensures smoother results."),
        ("How do I verify authenticity at Ekleel Abha?", "All Krem Kap tubs at Ekleel Abha are 100% genuine, imported directly from authorized Nazih distributors."),
        ("Does it burn or sting skin?", "No, but avoid applying onto open wounds or active acne breakouts."),
        ("Can both men and women use it?", "Yes, it is a unisex exfoliation and whitening treatment."),
        ("Is it suitable for teenagers?", "Suitable for adults and teens aged 15+."),
        ("Does it leave an oily residue?", "No, it rinses out completely with warm water, leaving skin soft and clean."),
        ("How should I store the tub?", "Store in a cool, dry place away from direct shower water."),
        ("Does it deliver immediate brightness?", "Yes, buffing away dead surface cells reveals noticeable brightness after the first use."),
        ("Does it help fade sun tans?", "Yes, it helps lift surface sun spots and uneven tan lines."),
        ("Is the 500g tub easy to use?", "It comes in a sturdy round tub with a secure screw lid."),
        ("Can it be mixed with natural oils?", "Yes, mixing a few drops of Argan or Almond oil enhances body moisturizing during scrubbing."),
        ("Does it dry out skin?", "Conditioning ingredients prevent drying, though applying moisturizer afterward maximizes results."),
        ("Do I need to wash with cleanser after scrubbing?", "No, Krem Kap cleanses skin thoroughly; simply rinse off with warm water.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1736",
        "sku": "EK-1736",
        "gtin": "8019622354004",
        "category": "العناية بالبشرة / مقشرات وسنفرة الوجه والجسم",
        "brand": "Krem Kap",
        "ar": {
            "title": "كريم كاب سنفرة ومبيض للوجه والجسم 500 جم الأصلي",
            "meta_title": "كريم كاب سنفرة ومبيض الاصلي 500جم | صيدلية إكليل أبها",
            "meta_description": "اشتري كريم كاب سنفرة ومبيض للوجه والجسم الإيطالي الأصلي (500جم). تقشير بطين الكاولين وتفتيح فوري للأكواع والركبتين. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["كريم_كاب", "سنفرة_كاب", "تفتيح_الوجه", "تقشير_الجسم", "إكليل_أبها"]
        },
        "en": {
            "title": "Krem Kap Face and Body Scrub and Whitening Cream 500g",
            "meta_title": "Krem Kap Face and Body Scrub 500g | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Krem Kap Face & Body Whitening Scrub (500g) from Italy. Exfoliates with Kaolin clay & Alumina micro-beads. 100% authentic at Ekleel Abha.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["krem_kap", "whitening_scrub", "body_scrub", "kaolin_clay", "ekleel_abha"]
        },
        "schema": {
            "brand": "Krem Kap",
            "category": "Skincare / Face & Body Scrub",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "krem-kap-face-and-body-scrub-and-whitening-cream-500g.webp",
            "alt": "Krem Kap Face and Body Scrub and Whitening Cream 500g",
            "title": "Krem Kap Face and Body Scrub and Whitening Cream 500g"
        }
    }

def create_product_1737():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم سنفرة مبيض للوجه والجسم من فيزو (Feyzo / Vizo Whitening Scrub Cream for Face and Body - 700g)</strong> المستحضر المغذي الفاخر المصمم لإعادة نضارة البشرة وتفتيحها بعناية فائقة. يعتمد هذا المقشر على حبيبات الجوز الطبيعية (Walnut Shell Powder) المعززة بفيتامين E وخلاصة الفواكه، حيث يزيل خلايا الجلد الميتة والشوائب السطحية بفعالية عالية ويكشف عن بشرة جديدة ناعمة ومتألقة.</p>
<p>تأتي العبوة بحجم كبير وافر يبلغ 700 جم، مما يضمن عناية مكثفة وممتدة للوجه والجسم والأكواع والركبتين. يمنح الكريم ترطيباً غنياً يحمي البشرة من الجفاف أثناء التقشير، ويساعد في توحيد لون الوجه وإعادة النضارة للجلد الباهت مع عطر منعش تدوم ذكراه طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تقشير طبيعي بحبيبات مسحوق الجوز:</strong> يزيل خلايا الجلد الميتة دون إحداث خدوش أو إجهاد للبشرة.</li>
  <li><strong>تفتيح وتوحيد لون الوجه والجسم:</strong> يقلل البقع الداكنة والتصبغات في الأكواع والركبتين والمناطق الجافة.</li>
  <li><strong>مدعم بفيتامين E ومضادات الأكسدة:</strong> يغذي ألياف البشرة ويعزز مرونتها ويحميها من الجفاف.</li>
  <li><strong>تنظيف المسام العميقة:</strong> ينظف الشوائب والترسبات الزهمية ويترك الجلد ناعماً كالحرير.</li>
  <li><strong>عبوة صالونات وافرة 700 جم:</strong> حجم كبير جداً يوفر قيمة اقتصادية ممتازة للاستخدام المستمر.</li>
  <li><strong>مناسب لجميع أنواع البشرة:</strong> تركيبة لطيفة ومجربة جلدياً تناسب سنفرة الوجه والجسم.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف والتبليل):</strong> بلي بشرة الوجه أو الجسم بالماء الفاتر لتجهيز المسام.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية مناسبة من كريم سنفرة فيزو على المنطقة المطلوبة.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي البشرة بحركات دائرية خفيفة ولطيفة لمدة 2 إلى 4 دقائق.</li>
  <li><strong>الخطوة الرابعة (الشطف):</strong> اشطفي بالماء الفاتر جيداً حتى زوال حبيبات السنفرة بالكامل.</li>
  <li><strong>الخطوة الخامسة (الترطيب):</strong> رطبي بشرتكِ بمرطبكِ المفضل؛ يُستخدم من 1 إلى 3 مرات أسبوعياً.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مسحوق قشور الجوز الطبيعي (Walnut Shell Powder):</strong> مقشر طبيعي لطيف يزيل الخلايا الميتة ويصقل البشرة.</li>
  <li><strong>فيتامين E (Tocopheryl Acetate):</strong> مضاد أكسدة يرطب ألياف الجلد ويحمي من التلف البيئي.</li>
  <li><strong>خلاصة الفواكه الطبيعية:</strong> تمنح البشرة نضارة وفيتامينات مغذية وتحسن مظهر التصبغات.</li>
  <li><strong>زبدة الشيا والمرطبات النباتية:</strong> تحمي البشرة من الجفاف وتمنحها ملمساً مخملياً.</li>
  <li><strong>عوامل تنظيف ناعمة:</strong> تضمن رغوة خفيفة تنظف المسام بفاعلية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الوجه والجسم فقط.</li>
  <li>تجنبي ملامسة الشامبو والسنفرة المباشرة للعينين؛ وفي حال ملامستهما اشطفي بالماء الفاتر.</li>
  <li>لا تستخدمي السنفرة على الجروح المفتوحة أو الحبوب الملتهبة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من شحوب الوجه وتصبغات الأكواع والركبتين وترغب في سنفرة طبيعية بحجم كبير.</li>
  <li>لمن تبحث عن مقشر بحبيبات الجوز الطبيعية وفيتامين E لتفتيح ونعومة البشرة.</li>
  <li>مناسب لجميع أنواع البشرة وللعناية المنزلية المتكاملة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>فيزو (Vizo / Feyzo)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / مقشرات وسنفرة الوجه والجسم</td></tr>
  <tr><th>نوع المنتج</th><td>كريم سنفرة ومبيض بحبيبات الجوز وفيتامين E (700g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>700 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (الوجه والجسم)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة، متجانسة، مشرقة ومفعمة بالحيوية</td></tr>
  <tr><th>الملمس</th><td>كريمي كثيف غني بحبيبات قشور الجوز الطبيعية</td></tr>
  <tr><th>العطر</th><td>عطر الفواكه المنعش واللطيف</td></tr>
  <tr><th>المكونات النشطة</th><td>مسحوق قشور الجوز، فيتامين E، خلاصة الفواكه، زبدة الشيا</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الإماراة</td></tr>
  <tr><th>الشركة المصنعة</th><td>Vizo International Cosmetics</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (من 15 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد حبيبات الجوز وفيتامين E وتجديد الجلد (Vizo)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم سنفرة فيزو 700 جم مشكلة انسداد مسام الوجه والجسم، خشونة الجلد في الأكواع والركبتين، والتصبغات السطحية الناتجة عن تراكم طبقات الكيراتين الميتة.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تتباطأ دورة تجدد خلايا البشرة بفعل الجفاف والتلوث، مما يؤدي لتراكم الخلايا الميتة على السطح الخارجي، فتظهر البشرة بمظهر خشن باهت ويمتنع امتصاص المرطبات.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>السنفرة بحبيبات طبيعية:</strong> استخدمي مقشر قشور الجوز الطبيعي لتفادي خدوش المقشرات الصناعية.<br>
2. <strong>الترطيب المباشر:</strong> رطبي بشرتكِ بمرطب فايتيرا أو كريم مرطب بعد السنفرة.<br>
3. <strong>التدليك اللطيف:</strong> لا تضغطي بقوة أثناء دلك الوجه لعدم تهييج الأنسجة.<br>
4. <strong>العناية بالمناطق الجافة:</strong> ركزي السنفرة على الكعبين، الركبتين، والأكواع.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "حبيبات الجوز الطبيعية تسبب خرقاً في جدار البشرة."<br>
<strong>الحقيقة:</strong> مسحوق قشور الجوز الدقيق في فيزو مصقول بدقة لتقشير الخلايا السطحية ببطء ودون إحداث خدوش مجهرية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تقوم حبيبات قشور الجوز الدقيقة بإزالة الروابط الفيزيائية للخلية الميتة في الطبقة القرنية، بينما يتغلغل فيتامين E وزبدة الشيا داخل الخلايا المكشوفة لمنع الأكسدة وحبس الرطوبة، مما يمنح الجلد ملمساً حريرياً وتفتحاً ملحوظاً.</p>"""

    faqs = [
        ("ما هو كريم سنفرة مبيض للوجه والجسم من فيزو 700جم؟", "هو مقشر كبر حجم غني بحبيبات قشور الجوز الطبيعية وفيتامين E مصمم لتقشير وتفتيح وتنعيم بشرة الوجه والجسم."),
        ("ما فائدة حبيبات قشور الجوز وفيتامين E في الكريم؟", "تقشر حبيبات الجوز الخلايا الميتة وتصقل البشرة، بينما يغذي فيتامين E الأنسجة ويحميها من الأكسدة للجفاف."),
        ("هل يمكن استخدامه للوجه والجسم معاً؟", "نعم، هو آمن ومصمم خصيصاً لتقشير وتفتيح الوجه وكافة مناطق الجسم بفعالية."),
        ("ما حجم عبوة سنفرة فيزو؟", "تأتي العبوة بحجم كبير جداً يبلغ 700 جم، وهي كمية وافرة تكفي لأشهر من العناية المنزلية."),
        ("هل يساعد الشامبو والسنفرة في تفتيح الأكواع والركبتين؟", "نعم، ممتاز جداً لإزالة طبقات الجلد الميتة الداكنة وتوحيد لون الأكواع والركبتين."),
        ("كم مرة يُنصح باستخدام السنفرة أسبوعياً؟", "يُنصح باستخدامه من 1 إلى 2 مرة أسبوعياً للوجه، ومن 2 إلى 3 مرات للجسم."),
        ("كيف يتم تطبيق سنفرة فيزو بشكل صحيح؟", "وضعي الكريم على بشرة مبللة، دلكي بحركات دائرية خفيفة لمدة 2-4 دقائق ثم اشطفي بالماء الفاتر."),
        ("هل يناسب البشرة الحساسة؟", "نعم، لكن يُفضل تدليكه برفق شديد على الوجه للبشرة الحساسة."),
        ("ما هو بلد صنع سنفرة فيزو؟", "تم تصنيعه وفق أعلى معايير الجودة للعناية بالبشرة."),
        ("هل يحتوي الكريم على عطر؟", "يتميز برائحة فواكه ناعمة ومنعشة تدوم في البشرة."),
        ("هل يجب ترطيب البشرة بعد السنفرة؟", "نعم، يُفضل دائماً وضع كريمكِ المرطب المفضل بعد السنفرة لحبس الترطيب."),
        ("هل يزيل السنفرة الشوائب والرؤوس السوداء؟", "نعم، ينظف المسام العميقة ويقلل تراكم الشوائب والرؤوس السوداء."),
        ("هل يمكن استخدامه قبل إزالة الشعر بالواكس؟", "نعم، السنفرة قبل إزالة الشعر تمنع نمو الشعر تحت الجلد وتسهل العملية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع المستحضرات لدى صيدلية إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يناسب الرجال والنساء؟", "نعم، هو مناسب لكلا الجنسين ولجميع الأعمار."),
        ("هل يناسب الأطفال؟", "مناسب للمراهقين والبالغين من سن 15 سنة فما فوق."),
        ("هل يترك أي أثر دهني على الوجه؟", "لا، يشطف بسهولة بالماء الفاتر ليترك البشرة ناعمة ونظيفة."),
        ("كيف أحتفظ بالكريم بالشكل الصحيح؟", "يُحفظ في مكان بارد وجاف بعيداً عن حرارة الشمس المباشرة."),
        ("هل يمنح تفتيحاً ملحوظاً؟", "إزالة طبقات الجلد الميت يمنح إشراقة وتفتيحاً ملحوظاً للبشرة الباهتة."),
        ("هل يساعد في إزالة التسمير السطحي؟", "نعم، يساعد في التخلص من التبقع والتسمير الناتجة عن الشمس."),
        ("هل العبوة بحجم 700 جم اقتصادية؟", "نعم، حجم 700 جم ممتاز جداً واقتصادي للاستخدام العائلي المستمر."),
        ("هل يمكن خلطه مع مرطبات أخرى؟", "يمكن استخدامه بمفرده أو دمج قطرات زيوت مرطبة أثناء سنفرة الجسم."),
        ("هل يسبب جفافاً للبشرة؟", "زبدة الشيا وفيتامين E يمنعان الجفاف، ولكن الترطيب بعدها يعزز النتيجة."),
        ("هل يلزم غسل الوجه بغسول بعد السنفرة؟", "لا يلزم، تنظف السنفرة البشرة بفاعلية وتغسل بالماء فقط."),
        ("هل العبوة محكمة الإغلاق؟", "نعم، تأتي في عبوة دائرية بغطاء لولبي يمنع التسرب.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Feyzo / Vizo Whitening Scrub Cream for Face and Body (700g)</strong> is a multi-action exfoliating treatment designed to illuminate, soften, and clarify facial and body skin. Formulated with natural Walnut Shell powder, antioxidant Vitamin E, and fruit botanical extracts, it gently buffs away dull, dead skin cells and surface impurities without irritation.</p>
<p>Boasting a generous 700g value jar, it provides extended home treatment for face, knees, elbows, and dry body areas. It deeply hydrates while smoothing rough skin, evening out skin tone, and imparting a fresh, long-lasting fruity aroma.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Natural Walnut Shell Exfoliation:</strong> Buffs away dead surface cells safely without skin micro-tears.</li>
  <li><strong>Face & Body Whitening:</strong> Fades dark spots on elbows, knees, and dry patches for a luminous complexion.</li>
  <li><strong>Enriched with Vitamin E & Fruit Extracts:</strong> Nourishes skin fibers, boosts elasticity, and fights oxidative stress.</li>
  <li><strong>Deep Pore Cleansing:</strong> Clears trapped sebum and impurities, leaving skin touchably smooth.</li>
  <li><strong>Generous 700g Value Jar:</strong> Large volume providing exceptional long-term value for face and body care.</li>
  <li><strong>Safe Daily Exfoliator:</strong> Gentle, dermatologist-tested formula suitable for all skin types.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Dampen):</strong> Dampen face or body skin with warm water to open pores.</li>
  <li><strong>Step 2 (Apply):</strong> Apply an adequate amount of Feyzo Whitening Scrub onto target areas.</li>
  <li><strong>Step 3 (Massage):</strong> Massage gently using circular motions for 2 to 4 minutes.</li>
  <li><strong>Step 4 (Rinse):</strong> Rinse thoroughly with warm water until all walnut beads are cleared.</li>
  <li><strong>Step 5 (Moisturize):</strong> Apply your favorite moisturizer; use 1 to 3 times weekly.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Walnut Shell Powder:</strong> Precision natural exfoliant that smooths skin texture and removes dead cells.</li>
  <li><strong>Vitamin E (Tocopheryl Acetate):</strong> Antioxidant nutrient that hydrates and guards skin against environmental stress.</li>
  <li><strong>Botanical Fruit Extracts:</strong> Provide essential vitamins to brighten complexion and unearth skin radiance.</li>
  <li><strong>Shea Butter:</strong> Deeply conditions and protects the skin barrier against moisture loss.</li>
  <li><strong>Soft Cleansing Agents:</strong> Create a mild lather clearing deep pore impurities efficiently.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on face and body only.</li>
  <li>Avoid direct contact with eyes; rinse immediately with warm water if contact occurs.</li>
  <li>Do not apply on open wounds or active acne breakouts.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dull skin, dark spots, or rough skin patches on knees, elbows, and body.</li>
  <li>Individuals seeking a natural Walnut shell powder whitening scrub enriched with Vitamin E.</li>
  <li>Suitable for all skin types across all ages.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Vizo / Feyzo</td></tr>
  <tr><th>Category</th><td>Skincare / Face & Body Scrubs</td></tr>
  <tr><th>Product Type</th><td>Natural Walnut & Vitamin E Whitening Scrub</td></tr>
  <tr><th>Volume/Weight</th><td>700 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Face & Body)</td></tr>
  <tr><th>Finish</th><td>Soft, luminous, even-toned, glowing skin</td></tr>
  <tr><th>Texture</th><td>Rich cream with natural walnut shell particles</td></tr>
  <tr><th>Fragrance</th><td>Delightful fresh fruit aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Walnut Shell Powder, Vitamin E, Fruit Extracts, Shea Butter</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / UAE</td></tr>
  <tr><th>Manufacturer</th><td>Vizo International Cosmetics</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens (15+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Walnut Powder & Vitamin E Exfoliation</h2>

<h3>What problem does this solve?</h3>
<p>Feyzo / Vizo Whitening Scrub resolves dead skin cell accumulation, rough elbow/knee skin, clogged pores, and surface dullness caused by environmental pollutants and slowed desquamation.</p>

<h3>Why does this condition happen?</h3>
<p>Accumulated dead stratum corneum cells prevent skin moisture absorption and scatter ambient light unevenly, making skin appear dark, rough, and fatigued.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Natural Exfoliation:</strong> Use natural walnut shell scrubs to avoid synthetic bead scratch marks.<br>
2. <strong>Immediate Moisture:</strong> Apply hydrating lotion directly after scrubbing.<br>
3. <strong>Gentle Motions:</strong> Massage gently without excessive pressure on facial skin.<br>
4. <strong>Target Dry Areas:</strong> Focus scrubbing on elbows, knees, and heels.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Natural walnut powders create skin micro-tears."<br>
<strong>Fact:</strong> Precision-milled walnut powder in Vizo scrub is rounded smooth to exfoliate dead cells safely without skin tears.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Precision walnut shell particles gently disrupt dead desmosome cell bonds in the stratum corneum. Simultaneously, Vitamin E and Shea Butter penetrate newly exposed skin cells to prevent oxidation and lock in moisture, yielding a noticeably smoother, brighter complexion.</p>"""

    en_faqs = [
        ("What is Feyzo Whitening Scrub Cream 700g?", "It is a large-volume 700g face and body scrub enriched with natural Walnut shell powder and Vitamin E to exfoliate and brighten skin."),
        ("What are the benefits of Walnut shell powder and Vitamin E?", "Walnut powder buffs away dead surface cells, while Vitamin E nourishes skin and protects against dryness."),
        ("Can it be used on both face and body?", "Yes, it is specially formulated to safely exfoliate both facial skin and body areas."),
        ("What size is this product jar?", "It comes in an extra-large 700g value jar suitable for extended family care."),
        ("Does it help lighten dark elbows and knees?", "Yes, it is highly effective for buffing away dark, rough skin on knees, elbows, and feet."),
        ("How many times weekly should I use it?", "Use 1 to 2 times weekly for facial skin, and 2 to 3 times weekly for body care."),
        ("How do I apply Feyzo scrub correctly?", "Apply onto damp skin, massage gently in circular motions for 2-4 minutes, then rinse with warm water."),
        ("Is it safe for sensitive skin?", "Yes, but massage gently without excessive pressure when applying to sensitive facial skin."),
        ("Where is Feyzo / Vizo manufactured?", "It is manufactured in certified cosmetic laboratories under international quality standards."),
        ("Does it contain fragrance?", "It features a delightful fresh fruit aroma."),
        ("Should I moisturize after scrubbing?", "Yes, always apply your favorite moisturizer after scrubbing to lock in hydration."),
        ("Does it clear deep pore impurities?", "Yes, it cleanses deep pores and minimizes blackhead accumulation."),
        ("Can I use it before waxing?", "Yes, scrubbing prior to hair removal prevents ingrown hairs."),
        ("How do I verify authenticity at Ekleel Abha?", "All Vizo / Feyzo tubs at Ekleel Abha are 100% genuine from certified distributors."),
        ("Can both men and women use it?", "Yes, it is a unisex exfoliation and whitening treatment."),
        ("Is it suitable for teenagers?", "Suitable for adults and teens aged 15+."),
        ("Does it leave an oily residue?", "No, it rinses out completely with warm water, leaving skin soft and clean."),
        ("How should I store the jar?", "Store in a cool, dry place away from direct heat."),
        ("Does it deliver noticeable brightness?", "Yes, buffing away dead surface cells reveals noticeable skin brightness."),
        ("Does it help fade sun tans?", "Yes, it helps lift surface sun spots and uneven tan lines."),
        ("Is the 700g jar economical?", "Yes, it provides exceptional long-term value for whole-family use."),
        ("Can it be mixed with body oils?", "Yes, mixing a few drops of Argan or Almond oil enhances body moisturizing during scrubbing."),
        ("Does it dry out skin?", "Shea Butter and Vitamin E prevent drying, though applying moisturizer afterward maximizes results."),
        ("Do I need to wash with cleanser after scrubbing?", "No, the scrub cleanses skin thoroughly; simply rinse off with warm water."),
        ("Is the tub securely sealable?", "Yes, it comes in a sturdy round tub with a secure screw lid.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1737",
        "sku": "EK-1737",
        "gtin": "5281111373350",
        "category": "العناية بالبشرة / مقشرات وسنفرة الوجه والجسم",
        "brand": "Vizo",
        "ar": {
            "title": "كريم سنفرة مبيض للوجه والجسم من فيزو 700جم",
            "meta_title": "كريم سنفرة مبيض فيزو 700جم | صيدلية إكليل أبها",
            "meta_description": "اشتري كريم سنفرة مبيض للوجه والجسم من فيزو بحبيبات الجوز وفيتامين E (700جم). تقشير وتفتيح للأكواع والركبتين. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["فيزو", "كريم_سنفرة", "تفتيح_البشرة", "حبيبات_الجوز", "إكليل_أبها"]
        },
        "en": {
            "title": "Feyzo Whitening Scrub Cream for Face and Body - 700g",
            "meta_title": "Feyzo Whitening Scrub Cream 700g | Ekleel Abha Pharmacy",
            "meta_description": "Buy Feyzo / Vizo Whitening Scrub Cream for Face & Body (700g). Natural Walnut powder & Vitamin E formula. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["vizo", "feyzo", "whitening_scrub", "walnut_scrub", "ekleel_abha"]
        },
        "schema": {
            "brand": "Vizo",
            "category": "Skincare / Face & Body Scrub",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "feyzo-whitening-scrub-cream-for-face-and-body-700g.webp",
            "alt": "Feyzo Whitening Scrub Cream for Face and Body 700g",
            "title": "Feyzo Whitening Scrub Cream for Face and Body 700g"
        }
    }

print("Loaded 1736 & 1737 builders")
