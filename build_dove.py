import json, os

def build_dove_product(prod_id, variant_en, variant_ar, technology_en, technology_ar, size_str, gtin, img_slug):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعتبر <strong>شامبو دوڤ {variant_ar} ({size_str})</strong> حلاً مثالياً متطوراً للعناية اليومية بالشعر. يعتمد هذا الشامبو من علامة دوڤ (Dove) الشهيرة على تركيبات المغذيات الدقيقة المتقدمة (Nutritive Solutions) المعززة بـ {technology_ar}، حيث ينظف فروة الرأس بلطف من الدهون والأوساخ، وفي نفس الوقت يتغلغل في عمق ألياف الشعر لتوفير الترطيب والتغذية المستمرة غسلة بعد غسلة.</p>
<p>صُممت الفرمولة ليمنح شعركِ حماية فائقة ضد التلف اليومي والإجهاد الميكانيكي الحراري. بفضل السيروم المرطب ومكونات السلسلة المغذية، يترك الشامبو الشعر ناعماً كالحرير، سهلاً في التمشيط، ومفعماً بالحيوية واللمعان دون تثقيل الخصلات، مما يجعله الخيار الأمثل للعناية اليومية بجميع أنواع الشعر.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تغذية تدريجية متطورة (Nutritive Solutions):</strong> يغذي ألياف الشعر من الداخل إلى الخارج ويعزز قوتها غسلة بعد غسلة.</li>
  <li><strong>تقنية {technology_ar}:</strong> تعمل على حماية الشعر وإصلاح أليافه واستعادة توازن رطوبته الطبيعية.</li>
  <li><strong>حماية ضد التكسر والجفاف:</strong> يقلل تقصف الأطراف والتلف الناتجة عن التصفيف والحرارة اليومية.</li>
  <li><strong>ترطيب وتنعيم فائق:</strong> يجعل الشعر سهلاً في التفكيك والتمشيط، ويتركه ناعماً ومخملي الملمس.</li>
  <li><strong>تركيبة خفيفة لا تثقل الشعر:</strong> تنظف الفروة بكفاءة وتمنح الشعر حجماً وحيوية طبيعية.</li>
  <li><strong>مناسب للاستخدام اليومي:</strong> تركيبة متوازنة الحموضة ولطيفة وآمنة لجميع أنواع الشعر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل):</strong> بلي شعركِ وفروة رأسكِ جيداً بالماء الفاتر لفتح المسام وتجهيز البصيلات.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية مناسبة من شامبو دوڤ على كف اليد ووزعيها بالتساوي على فروة الرأس والشعر.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي فروة الرأس بلطف بأطراف الأصابع بحركات دائرية لمدة 2 إلى 3 دقائق لتكوين رغوة غنية.</li>
  <li><strong>الخطوة الرابعة (الشطف):</strong> اشطفي الشعر جيداً بالماء الفاتر حتى إزالة الرغوة بالكامل.</li>
  <li><strong>الخطوة الخامسة (الترتيب):</strong> للحصول على أقصى درجات النعومة، يُفضل استخدام بلسم دوڤ المطابق بعد الشامبو.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركب {technology_ar}:</strong> جزيئات مغذية متطورة تتغلغل داخل القشرة الشعرية لترميم التلف وتثبيت الرطوبة.</li>
  <li><strong>الجليسرين (Glycerine):</strong> مرطب فعال يجذب الرطوبة ويحافظ على ليونة الشعرة ويمنع جفافها.</li>
  <li><strong>مركبات الدايميثيكونول (Dimethiconol):</strong> تغلف السطح الخارجي للشعرة بطبقة واقية ناعمة تحمي من الحرارة والتشابك.</li>
  <li><strong>غوار هيدروكسي بروبيل تريمونيوم كلورايد:</strong> عامل تكييف طبيعي يمنع التشابك ويسهل التمشيط.</li>
  <li><strong>عوامل تنظيف لطيفة (Sodium Laureth Sulfate):</strong> تضمن رغوة غنية تنظف الأوساخ دون تجريد الفروة من زيوتها المفيدة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الشعر وفروة الرأس فقط.</li>
  <li>تجنبي ملامسة الشامبو المباشرة للعينين؛ وفي حال ملامستهما اشطفي فوراً بكمية وفيرة من الماء النظيف.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن أشعة الشمس المباشرة.</li>
  <li>في حال حدوث حكة شديدة أو طفح جلدي غير عادي، توقفي عن الاستخدام واستشيري الطبيب.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من مشاكل الشعر المجهد أو التالف أو المعرض للتقصف والتساقط.</li>
  <li>لمن يبحثون عن شامبو يومي مغذٍ يمنح نعومة وحماية دائمة.</li>
  <li>مناسب للرجال والنساء ولجميع أنواع الشعر العادي والجاف والمختلط.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>دوڤ (Dove)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / شامبو ومغذيات الشعر</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو مغذٍ يومي ({variant_ar})</td></tr>
  <tr><th>الحجم/الوزن</th><td>{size_str}</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (خاصة العادي، الجاف والتالف)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم، حيوياً، مفعم بالنضارة والقوة</td></tr>
  <tr><th>الملمس</th><td>كريمي لؤلؤي سائل يرغي بسهولة</td></tr>
  <tr><th>العطر</th><td>عطر دوڤ الكلاسيكي المنعش واللطيف</td></tr>
  <tr><th>المكونات النشطة</th><td>{technology_ar}، جليسرين، دايميثيكونول، صوديوم لوريث سلفات</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / مصر (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (يونيليفر)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لتقنية المغذيات الدقيقة وحماية الشعر (Dove Nutritive Solutions)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج شامبو دوڤ {variant_ar} مشكلة جفاف وتلف ألياف الشعر الناجم عن الغسيل التكراري، الحرارة، والتقلبات الجوية، حيث يوفر تنظيفاً لطيفاً يحافظ على زيوت الفروة الطبيعية ويرمم الشعر المتضرر.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>يتعرض الشعر للتلف بسبب فقدان الليبيدات والبروتينات في الطبقة الخارجية (Cuticle) بفعل التصفيف الحراري والغسيل بشامبوهات قاسية. يؤدي ذلك لفتح الحراشف وزيادة التسامح والتقصف وفقدان الرطوبة الداخلية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام المنتظم:</strong> اغسلي شعرك 2 إلى 3 مرات أسبوعياً بشامبو دوڤ المغذي.<br>
2. <strong>تجنب الماء الساخن جداً:</strong> استخدمي الماء الفاتر لمنع جفاف الفروة وزيادة التقصف.<br>
3. <strong>التدليك اللطيف:</strong> دلكي الفروة بأطراف الأصابع بحركات دائرية دون فرك الشعر بشدة.<br>
4. <strong>استخدام البلسم المطابق:</strong> اتبعي الشامبو ببلسم دوڤ لإغلاق حراشف الشعر وحبس الترطيب.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الغسيل اليومي بالشامبو يسبب دائماً تساقط الشعر."<br>
<strong>الحقيقة:</strong> شامبو دوڤ بتركيبة Nutritive Solutions مصمم بدرجة حموضة متوازنة ومغذيات دقيقة تسمح بالاستخدام اليومي الآمن دون تجفيف.</p>
<p><strong>خرافة:</strong> "الشامبو المغذي يجعل الشعر دهنياً وثقيلاً."<br>
<strong>الحقيقة:</strong> تركيبة دوڤ الذكية تمنح الترطيب الداخلي مع الحفاظ على خفة الخصلات وحجمها الطبيعي.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعتمد المنتج على تقنية <strong>{technology_ar}</strong> الشاملة التي تتألف من جزيئات ماكرو وميكرو مغذية. تتغلغل المركبات الدقيقة داخل طبقة القشرة لتثبيت الروابط البروتينية، بينما تشكل البوليمرات السيليكونية المرطبة غشاءً رقيقاً على سطح الشعرة يعكس الضوء ويسهل التمشيط ويمنع تقصف الأطراف.</p>"""

    faqs = [
        (f"ما هو شامبو دوڤ {variant_ar} وما الذي يميزه؟", f"هو شامبو مغذٍ يومي مصمم بتركيبة Nutritive Solutions وتقنية {technology_ar} لتنظيف الشعر بلطف وترميمه وتغذية أليافه دون تثقيل."),
        (f"ما هي فوائد تقنية {technology_ar} في الشامبو؟", f"تعمل تقنية {technology_ar} على اختراق القشرة الشعرية وتغذية ألياف الشعر وترميم التلف وتأمين ترطيب عميق يدوم طوال اليوم."),
        ("هل يناسب هذا الشامبو الاستخدام اليومي؟", "نعم، يتميز بتركيبة لطيفة ومتوازنة الحموضة تسمح بالاستخدام اليومي الآمن دون إلحاق الضرر بالفروة."),
        ("هل يسبب شامبو دوڤ ثقلاً أو ملمساً دهنياً للشعر؟", "لا، تنظف تركيبته الفروة بكفاءة عالية وتمنح الشعر حيوية وحجماً طبيعياً خفيفاً."),
        ("ما حجم العبوة؟", f"تأتي العبوة بحجم {size_str}، وهي كمية وافرة واقتصادية تناسب الاستخدام اليومي المنتظم."),
        ("هل يساعد الشامبو في تقليل تقصف الأطراف؟", "نعم، المواد المرطبة والسيروم المدمج يقللان من تقصف الأطراف والتكسر الناجم عن التصفيف."),
        ("هل يناسب الشامبو الشعر المسبوغ؟", "نعم، تركيبته لطيفة وخالية من الكيمياويات القاسية وهي آمنة للشعر المعالج بالألوان."),
        ("هل يمكن استخدامه للرجال والنساء؟", "نعم، هو منتج مناسب لكلا الجنسين ولكافة أنواع الشعر."),
        ("كيف أتحصل على أفضل نتائج من الشامبو؟", "دلكي الشامبو على شعر مبلل لمدة 2-3 دقائق ثم اشطفيه جيداً واستخدمي بلسم دوڤ المطابق بعده."),
        ("ما هي الرائحة الخاصة بشامبو دوڤ؟", "يتميز برائحة دوڤ المنعشة والناعمة الشهيرة التي تدوم في الشعر طوال اليوم."),
        ("هل يساعد في فك تشابك الشعر؟", "نعم، يحتوي على عوامل تكييف مثل غوار كلورايد التي تسهل مشط الشعر وتمنع التشابك."),
        ("هل يناسب البشرة والفروة الحساسة؟", "نعم، تم اختباره جلدياً بتركيبة متوازنة الحموضة تناسب الفروة الحساسة."),
        ("هل يحتوي على مركبات البارابين؟", "تركيبات دوڤ الحديثة خالية من البارابين ومصممة بأعلى معايير الأمان."),
        ("ما هو بلد صنع شامبو دوڤ؟", "يُصنع بواسطة شركة يونيليفر (Unilever) العالمية في مصانعها المعتمدة."),
        ("هل يمنع تساقط الشعر الناجم عن التكسر؟", "نعم، تقوية ألياف الشعر وتقليل التقصف يحدان بشكل ملحوظ من تساقط الشعر الناجم عن التكسر."),
        ("هل يمكن استخدامه للأطفال؟", "مناسب للمراهقين والأطفال من سن 12 سنة. للأطفال الأصغر يُفضل شامبو مخصص للأطفال."),
        ("ما الفرق بين إصدارات شامبو دوڤ المختلفة؟", "تتشارك جميعها في قاعدة الترطيب اللطيفة، ولكن يختص كل إصدار بتقنية معينة مثل كبح التساقط، الترطيب اليومي، أو إصلاح الأطراف."),
        ("هل يلزم استخدام بلسم بعد الشامبو؟", "يُفضل دائماً استخدام بلسم دوڤ المطابق لإغلاق حراشف الشعر وتأمين أقصى حماية."),
        ("هل يتأثر الشامبو بالحرارة في الاستحمام؟", "يُفضل استخدام الماء الفاتر للحصول على أفضل رغوة وحماية الفروة من الجفاف."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات دوڤ لدى صيدلية إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين بشركة يونيليفر."),
        ("هل يترك الشامبو أي بقايا على الفروة؟", "لا، يشطف بسهولة بالماء ولا يترك أي بقايا أو تراكمات على فروة الرأس."),
        ("هل يساعد الشامبو في تنعيم الشعر الهيش؟", "نعم، السيروم المرطّب يقلل الهيشان ويمنح الشعر ملمساً ناعماً ومخملياً."),
        ("هل يحتاج الشامبو للرج قبل الاستخدام؟", "لا يحتاج للرج، فقوامه المتجانس جاهز للاستخدام المباشر."),
        ("هل العبوة بحجم 600 مل سهلة الاستخدام؟", "تأتي العبوات الكبيرة مضغوطة بتصميم مريح وعصري يسهل سكب الشامبو منها بمرونة."),
        ("هل يساعد في استعادة لمعان الشعر الباهت؟", "نعم، تنظيف التراكمات وتغليف الشعرة بالمرطبات يعيد إليها اللمعان والبريق الطبيعي.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>Dove {variant_en} ({size_str})</strong> offers an advanced daily haircare treatment designed to restore healthy smoothness and strength to your hair. Powered by Unilever's renowned Nutritive Solutions and enriched with {technology_en}, this shampoo gently purifies the scalp of sebum and impurities while penetrating deep into the hair cortex to nourish strands wash after wash.</p>
<p>Formulated to protect hair against daily mechanical, thermal, and environmental damage, it combines lightweight conditioning silicones and hydration humectants. It leaves your hair feeling silky soft, effortlessly detangled, and naturally radiant without weighing down your style—making it the essential daily wash for all hair types.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Progressive Nutritive Solutions:</strong> Nourishes hair fibers progressively from root to tip for lasting resilience.</li>
  <li><strong>Advanced {technology_en}:</strong> Repairs damaged cuticles, restores moisture equilibrium, and seals in essential hydration.</li>
  <li><strong>Breakage & Dryness Shield:</strong> Reduces split ends and protects strands against heat styling and mechanical stress.</li>
  <li><strong>Silky Smoothness & Detangling:</strong> Eases combability, minimizes frizz, and imparts a velvety touch.</li>
  <li><strong>Weightless Cleansing:</strong> Cleanses the scalp effectively while preserving natural volume and movement.</li>
  <li><strong>Safe Daily Wash:</strong> pH-balanced formula safe and gentle enough for everyday family application.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet Hair):</strong> Thoroughly wet hair and scalp with lukewarm water to open cuticles.</li>
  <li><strong>Step 2 (Apply):</strong> Dispense a suitable amount of Dove shampoo onto palms and distribute evenly across scalp and strands.</li>
  <li><strong>Step 3 (Massage):</strong> Gently massage into a rich lather using circular fingertip motions for 2 to 3 minutes.</li>
  <li><strong>Step 4 (Rinse):</strong> Rinse thoroughly with lukewarm water until all lather is completely removed.</li>
  <li><strong>Step 5 (Condition):</strong> For optimal smoothness, follow with the matching Dove conditioner.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>{technology_en}:</strong> Micro-nourishing complex that penetrates deep within hair layers to repair structural bonds.</li>
  <li><strong>Glycerin:</strong> Effective humectant that attracts and locks water into hair cells to prevent dryness.</li>
  <li><strong>Dimethiconol:</strong> Smooths outer cuticle layers, providing thermal protection and easy detangling.</li>
  <li><strong>Guar Hydroxypropyltrimonium Chloride:</strong> Natural conditioning agent ensuring snag-free combability.</li>
  <li><strong>Gentle Surfactants (Sodium Laureth Sulfate):</strong> Creates a luxurious lather clearing oil and buildup without stripping.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external use on hair and scalp only.</li>
  <li>Avoid direct contact with eyes; rinse immediately with plenty of clean water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from direct sunlight.</li>
  <li>Discontinue use if severe scalp irritation or itching develops.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone experiencing damaged, dry, split, or breakage-prone hair needing everyday repair.</li>
  <li>Individuals looking for a trusted, nourishing shampoo for daily hair protection.</li>
  <li>Suitable for men and women across all hair types (normal, dry, or combination).</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Dove</td></tr>
  <tr><th>Category</th><td>Hair Care / Nourishing Shampoo</td></tr>
  <tr><th>Product Type</th><td>Daily Nourishing Shampoo ({variant_en})</td></tr>
  <tr><th>Volume/Weight</th><td>{size_str}</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Ideal for Normal, Dry & Damaged Hair)</td></tr>
  <tr><th>Finish</th><td>Smooth, shiny, manageable & healthy hair</td></tr>
  <tr><th>Texture</th><td>Pearlescent creamy fluid lathering easily</td></tr>
  <tr><th>Fragrance</th><td>Fresh classic Dove signature aroma</td></tr>
  <tr><th>Active Ingredients</th><td>{technology_en}, Glycerin, Dimethiconol, Gentle Surfactants</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / Egypt (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens (12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Dove Nutritive Solutions & Fiber Repair</h2>

<h3>What problem does this solve?</h3>
<p>Dove {variant_en} addresses hair dryness, cuticle damage, and mechanical breakage caused by frequent washing, thermal styling, and weather exposure, delivering gentle cleansing without stripping lipid protection.</p>

<h3>Why does this condition happen?</h3>
<p>Daily styling and harsh environmental factors strip natural lipids and proteins from the protective cuticle layer. Open, rough cuticles cause moisture evaporation, frizz, split ends, and increased breakage during combing.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Regular Washing:</strong> Wash 2 to 3 times weekly with Dove Nutritive Solutions shampoo.<br>
2. <strong>Avoid Excessive Heat:</strong> Use lukewarm water to wash hair, protecting the scalp barrier.<br>
3. <strong>Gentle Scalp Massage:</strong> Massage scalp gently with fingertips without harsh rubbing.<br>
4. <strong>Pair with Conditioner:</strong> Follow with matching Dove conditioner to seal cuticles and lock in moisture.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Daily shampooing always damages and thins hair."<br>
<strong>Fact:</strong> Dove Nutritive Solutions features a pH-balanced, micro-nourishing formula safe for daily cleansing without drying.</p>
<p><strong>Myth:</strong> "Nourishing shampoos make hair feel heavy and oily."<br>
<strong>Fact:</strong> Dove's formula delivers targeted internal hydration while preserving natural volume and movement.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>This product operates through <strong>{technology_en}</strong>. Micro-nourishing actives penetrate deep into the hair cortex to fortify structural amino acid chains. Concurrently, lightweight conditioning polymers align surface cuticles, reducing friction, locking in moisture, and preventing split end formation.</p>"""

    en_faqs = [
        (f"What is Dove {variant_en} and what does it do?", f"It is a nourishing daily shampoo formulated with Nutritive Solutions and {technology_en} to clean, repair, and hydrate hair wash after wash."),
        (f"How does {technology_en} benefit hair?", f"It penetrates the hair cortex to nourish fibers, repair damage, and maintain optimal hydration."),
        ("Is this shampoo safe for daily use?", "Yes, its pH-balanced, gentle formula is designed for safe daily application."),
        ("Will it leave my hair feeling greasy or heavy?", "No, it cleanses thoroughly while maintaining natural volume and movement."),
        ("What size is this bottle?", f"This bottle contains {size_str}, offering an economical volume for regular family use."),
        ("Does it help reduce split ends and breakage?", "Yes, conditioning agents smooth cuticles and reinforce strands to minimize split ends and styling breakage."),
        ("Is it safe for color-treated hair?", "Yes, its gentle formula is free from harsh chemicals and safe for colored hair."),
        ("Can both men and women use it?", "Yes, it is a unisex formula suitable for all hair types."),
        ("How do I get the best results?", "Massage into wet hair for 2-3 minutes, rinse thoroughly, and follow with matching Dove conditioner."),
        ("What scent does Dove shampoo have?", "It features Dove's iconic, clean, fresh signature fragrance."),
        ("Does it help detangle knotty hair?", "Yes, conditioning agents like Guar Chloride ease combability and reduce tangles."),
        ("Is it safe for sensitive scalps?", "Yes, it is dermatologically tested and pH-balanced for scalp comfort."),
        ("Is the formula paraben-free?", "Yes, modern Dove formulas are paraben-free."),
        ("Where is Dove shampoo manufactured?", "It is manufactured by Unilever under strict international quality standards."),
        ("Does it reduce hair fall from breakage?", "Yes, reinforcing hair fiber strength significantly reduces hair fall caused by breakage."),
        ("Is it suitable for children?", "It is suitable for teens and adults aged 12+; child-specific products are recommended for younger children."),
        ("How do different Dove variants differ?", "All share gentle hydration bases, but each variant incorporates specific technologies targeting breakage, daily care, or split end rescue."),
        ("Should I use a conditioner after shampooing?", "Using matching Dove conditioner is recommended to seal cuticles and maximize protection."),
        ("Does water temperature affect shampoo performance?", "Lukewarm water provides optimal lather while preserving scalp moisture."),
        ("How do I verify product authenticity at Ekleel Abha?", "All Dove products at Ekleel Abha are 100% original, sourced from certified Unilever Saudi distributors."),
        ("Does it wash out cleanly without buildup?", "Yes, it rinses out completely with water without leaving heavy residue."),
        ("Does it help tame frizzy hair?", "Yes, moisture-locking silicones smooth cuticles, reducing frizz and flyaways."),
        ("Does it require shaking before use?", "No, its homogeneous creamy formula is ready for immediate use."),
        ("Is the 600ml bottle easy to handle?", "The 600ml bottle features an ergonomic grip design for convenient shower dispensing."),
        ("Does it restore shine to dull hair?", "Yes, clearing buildup and smoothing cuticles restores natural glossy shine.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "العناية بالشعر / شامبو ومغذيات الشعر",
        "brand": "Dove",
        "ar": {
            "title": f"شامبو دوڤ {variant_ar}، {size_str}",
            "meta_title": f"شامبو دوڤ {variant_ar} {size_str} | صيدلية إكليل أبها",
            "meta_description": f"اشتري شامبو دوڤ {variant_ar} ({size_str}). تغذية فائقة وحماية من التلف بتقنية {technology_ar}. منتج أصلي 100% لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["دوف", "شامبو_دوف", f"دوف_{variant_ar}", "العناية_بالشعر", "إكليل_أبها"]
        },
        "en": {
            "title": f"Dove {variant_en}, {size_str}",
            "meta_title": f"Dove {variant_en} {size_str} | Ekleel Abha Pharmacy",
            "meta_description": f"Buy Dove {variant_en} ({size_str}). Progressive nourishment with {technology_en}. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["dove", f"dove_{variant_en.lower()}", "shampoo", "hair_care", "ekleel_abha"]
        },
        "schema": {
            "brand": "Dove",
            "category": "Hair Care / Shampoo",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"dove-{img_slug}-{size_str.lower().replace(' ', '')}.webp",
            "alt": f"Dove {variant_en} {size_str}",
            "title": f"Dove {variant_en} {size_str}"
        }
    }

print("Dove builder ready")
