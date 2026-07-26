import json, os

def create_product_1707():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>شامبو كيراتين سموث لتنعيم الشعر الجاف والمتطاير من تريسمي (TRESemmé Keratin Smooth Shampoo - 400ml)</strong> المستحضر الاحترافي الأول للحصول على شعر أنسيابي وخالٍ من الهيشان حتى 72 ساعة. يدمج هذا الشامبو المتطور بين قوة الكيراتين المحلل (Hydrolyzed Keratin) المرمم لألياف الشعر وغنى زيت الأرجان (Argan Oil) المغذي ليمنحكِ تجربة عناية بالصالونات في منزلكِ.</p>
<p>صُمم هذا الشامبو خصيصاً للتحكم بالشعر الجاف، المجعد، والمتطاير، حيث ينظف فروة الرأس بلطف من الزيوت والأوساخ بينما يتغلغل في عمق القشرة الشعرية ليملأ الفراغات الناتجة عن التلف الحراري والكيميائي. يترك الشعر ناعماً كالحرير، سهلاً في التحكم، ومفعماً باللمعان والحيوية دون تثقيل الخصلات.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تحكم بالهيشان حتى 72 ساعة:</strong> نظام متطور يمنح الشعر انسيابية ونعومة فائقة تقاوم الرطوبة والهيشان.</li>
  <li><strong>معزز بالكيراتين المحلل:</strong> يرطب ألياف الشعر ويعيد بناء الروابط المتضررة لمنع التكسر والتقصف.</li>
  <li><strong>تغذية بزيوت الأرجان:</strong> يعوض الشعر عن الرطوبة المفقودة ويمنحه لمعاناً كريستالياً وملمساً مخملياً.</li>
  <li><strong>تنظيف لطيف وفعال:</strong> ينظف الفروة من الدهون دون تجريد الزيوت الطبيعية الحامية.</li>
  <li><strong>تسهيل التصفيف والتمشيط:</strong> يمنع التشابك ويسلس حركة المشط للحماية من الإجهاد الميكانيكي.</li>
  <li><strong>جودة الصالونات الاحترافية:</strong> تركيبة مجربة من خبراء التجميل مناسبة للاستخدام اليومي والمنتظم.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل):</strong> بلي شعركِ وفروة رأسكِ بالماء الفاتر جيداً.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية مناسبة من شامبو كيراتين سموث على كف اليد ووزعيها على الشعر.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي الفروة بأطراف الأصابع بحركات دائرية لمدة 2 إلى 3 دقائق لتكوين رغوة غنية.</li>
  <li><strong>الخطوة الرابعة (الشطف):</strong> اشطفي الشعر جيداً بالماء الفاتر حتى إزالة الرغوة بالكامل.</li>
  <li><strong>الخطوة الخامسة (الترتيب):</strong> للحصول على نتائج مثالية تدوم 72 ساعة، اتبعي الشامبو ببلسم تريسمي كيراتين سموث.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الكيراتين المحلل (Hydrolyzed Keratin):</strong> بروتين صلب يخترق الشقوق السطحية للشعرة لترميمها وزيادة مرونتها.</li>
  <li><strong>زيت الأرجان (Argania Spinosa Kernel Oil):</strong> يغذي طبقات الشعر بالأحماض الدهنية وفيتامين E لمنع الجفاف.</li>
  <li><strong>الدايميثيكونول (Dimethiconol):</strong> سيليكون مرطب يعكس الضوء ويغلف ألياف الشعر لمنع التأثر بالرطوبة.</li>
  <li><strong>غوار كلورايد (Guar Hydroxypropyltrimonium Chloride):</strong> يمنع التشابك ويسلس حركة الشعر أثناء التمشيط.</li>
  <li><strong>عوامل تنظيف لطيفة (Sodium Laureth Sulfate & Cocamidopropyl Betaine):</strong> تضمن رغوة غنية وتنظيفاً كفؤاً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الشعر وفروة الرأس فقط.</li>
  <li>تجنبي ملامسة الشامبو المباشرة للعينين؛ وفي حال ملامستهما اشطفي فوراً بالماء الفاتر.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
  <li>توقفي عن الاستخدام في حال حدوث تهيج أو طفح جلدي.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من الشعر الجاف، المجعد، الهائش، أو الصعب التحكم به.</li>
  <li>لمن تبحث عن عناية احترافية تضمن انسيابية الشعر لمدة 72 ساعة.</li>
  <li>مناسب لجميع أنواع الشعر وخاصة المعالج كيميائياً أو الحراري.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>تريسمي (TRESemmé)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / شامبو الكيراتين والنعومة</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو تنعيم ومكافحة الهيشان (Keratin Smooth)</td></tr>
  <tr><th>الحجم/الوزن</th><td>400 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (خاصة الجاف والمجعد والمتطاير)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم، انسيابي، مفعم باللمعان وخالٍ من الهيشان</td></tr>
  <tr><th>الملمس</th><td>كريمي لؤلؤي يرغي بسهولة</td></tr>
  <tr><th>العطر</th><td>عطر الصالونات الاحترافي الناعم والمنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>كيراتين محلل، زيت الأرجان، دايميثيكونول، غوار كلورايد</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / المملكة المتحدة (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (يونيليفر)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لتقنية الكيراتين والأرجان ومكافحة الهيشان (TRESemmé)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج شامبو تريسمي كيراتين سموث مشكلة تطاير الشعر وهيشانه والجفاف الناتج عن نقص بروتين الكيراتين والزيوت المغذية في طبقات الشعرة الخارجية.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>ينشأ الهيشان عند تعرض الشعر للرطوبة الجوية في ظل وجود مسامات مفتوحة وتلف في غشاء الشعرة (Cuticle). تمتص ألياف الشعر الرطوبة بشكل غير متساوٍ، مما يسبب انتفاخ الخصلات وتجعدها.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام نظام كيراتين سموث الكامل:</strong> استخدمي الشامبو والبلسم معاً للحصول على ثبات 72 ساعة.<br>
2. <strong>الشطف بالماء الفاتر:</strong> تجنبي الماء الساخن لحماية الكيراتين من الجفاف.<br>
3. <strong>التجفيف بالمنشفة الميكروفايبر:</strong> جففي الشعر بربت لطيف لمنع الاحتكاك.<br>
4. <strong>استخدام حماية الحرارة:</strong> وضعي واقي الحرارة قبل استخدام أدوات التصفيف.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "شامبو الكيراتين يلغي الحاجة للبلسم."<br>
<strong>الحقيقة:</strong> الشامبو ينظف ويغذي القشرة الداخلية، بينما يقوم البلسم بإغلاق الحراشف الخارجية وحبس المكونات.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يتغلغل الكيراتين المحلل بوزنه الجزيئي المنخفض داخل شقوق القشرة ليملأ الفراغات البروتينية المكسورة، بينما يشكل زيت الأرجان والدايميثيكونول غشاءً مائياً عازلاً يمنع تسرب الرطوبة الخارجية إلى داخل ألياف الشعر، مما يقضي على الهيشان ويضمن النعومة لمدة 72 ساعة.</p>"""

    faqs = [
        ("ما هو شامبو تريسمي كيراتين سموث وما هي مميزاته؟", "هو شامبو احترافي معزز بالكيراتين المحلل وزيت الأرجان يمنح الشعر انسيابية ونعومة فائقة ويتحكم بالهيشان حتى 72 ساعة."),
        ("ما هي فائدة الكيراتين المحلل في الشامبو؟", "يرمم الشقوق السطحية والتلف البروتيني في ألياف الشعر، مما يزيد مرونة الخصلات ويمنع التكسر."),
        ("ما دور زيت الأرجان في الفرمولة؟", "يغذي طبقات الشعر بالأحماض الدهنية وفيتامين E ويمنحه لمعاناً كراستالياً وملمساً مخملياً."),
        ("هل يدوم مفعول التحكم بالهيشان حتى 72 ساعة؟", "نعم، عند استخدام نظام تريسمي كيراتين سموث الكامل (الشامبو والبلسم) بانتظام."),
        ("ما حجم عبوة الشامبو؟", "تأتي العبوة بحجم 400 مل، وهي كمية مناسبة للاستخدام المنتظم."),
        ("هل يناسب الشامبو الشعر المسبوغ؟", "نعم، تركيبة لطيفة وآمنة للشعر المصبوغ والمعالج كيميائياً."),
        ("هل يناسب الرجال والنساء؟", "نعم، هو مناسب لكلا الجنسين ولكافة أنواع الشعر المجعد أو الهائش."),
        ("كم مرة يُنصح باستخدامه أسبوعياً؟", "يُنصح باستخدامه من 2 إلى 3 مرات أسبوعياً لحماية مستمرة من الهيشان."),
        ("هل يساعد في فك تشابك الشعر؟", "نعم، يحتوي على غوار كلورايد وسيليكونات مرطبة تسلس حركة المشط وتمنع التشابك."),
        ("ما هي رائحة شامبو تريسمي كيراتين سموث؟", "يتميز برائحة الصالونات الاحترافية الناعمة والمنعشة التي تدوم في الشعر."),
        ("هل يترك الشامبو ملمساً دهنياً على الشعر؟", "لا، ينظف الفروة بكفاءة ويمنح الخصلات انسيابية دون أي ثقل زيتي."),
        ("هل يمكن استخدامه للشعر المعالج بالكيراتين أو البروتين؟", "نعم، يساعد في الحفاظ على النعومة وعلاج الكيراتين لفترة أطول."),
        ("ما هو بلد صنع الشامبو؟", "يُصنع بواسطة شركة يونيليفر (Unilever) العالمية في مصانعها المعتمدة."),
        ("هل يحتوي على مركبات البارابين؟", "التركيبة مطورة وخالية من البارابين ومجربة جلدياً."),
        ("هل يناسب الشعر الشديد الجفاف؟", "نعم، ممتاز جداً للشعر الجاف والمجهد بفعل الحرارة والصبغات."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات تريسمي لدى صيدلية إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يلزم استخدام بلسم بعد الشامبو؟", "يُفضل استخدام بلسم تريسمي كيراتين سموث للحصول على أقصى درجات النعومة والحماية."),
        ("هل يقلل الشامبو تساقط الشعر؟", "تقوية ألياف الشعر بالكيراتين تمنع التساقط الناجم عن تكسر الخصلات."),
        ("هل يناسب الأطفال؟", "مناسب للمراهقين والأطفال من سن 12 سنة فما فوق."),
        ("هل الشامبو آمن للاستخدام اليومي؟", "نعم، تركيبة لطيفة تناسب الاستخدام المنتظم."),
        ("هل يترك أي بقايا بعد الشطف؟", "لا، يشطف بسهولة وسرعة بالماء الفاتر."),
        ("كيف أحتفظ بالشامبو بالشكل الصحيح؟", "يُحفظ في مكان بارد وجاف بعيداً عن أشعة الشمس المباشرة."),
        ("هل يساعد في حماية الشعر من حرارة أجهزة التصفيف؟", "نعم، تغليف ألياف الشعر بالكيراتين والأرجان يخفف الإجهاد الحراري."),
        ("هل العبوة بحجم 400 مل سهلة الاستخدام؟", "تأتي بتصميم عصري بضغط سهل للسكب بمرونة."),
        ("هل يساعد في إضافة لمعان للشعر الباهت؟", "نعم، تنظيف الفروة وتغليف الخصلات يعيد للشعر بريقه الكريستالي.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>TRESemmé Keratin Smooth Shampoo (400ml)</strong> is a professional salon-quality hair wash engineered to transform dry, frizzy, and unruly hair into sleek, manageable strands for up to 72 hours. Combining the structural repairing power of Hydrolyzed Keratin with the deep moisture of pure Argan Oil, this advanced formula delivers salon-fresh smoothness at home.</p>
<p>Specially crafted to tame stubborn frizz and flyaways, it gently cleanses the scalp of oil and impurities while penetrating the hair cortex to fill micro-gaps caused by thermal and chemical stress. It leaves hair touchably soft, effortlessly detangled, and radiant without weighing down your style.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Up to 72-Hour Frizz Control:</strong> Advanced system delivering sleek smoothness that resists humidity and frizz.</li>
  <li><strong>Enriched with Hydrolyzed Keratin:</strong> Fills structural protein micro-gaps to fortify strands against breakage.</li>
  <li><strong>Argan Oil Nourishment:</strong> Infuses essential moisture and fatty acids for luminous shine and silky softness.</li>
  <li><strong>Gentle & Effective Cleansing:</strong> Purifies scalp oils while preserving natural protective barrier lipids.</li>
  <li><strong>Enhanced Detangling:</strong> Smooths cuticle friction for effortless combing and reduced mechanical stress.</li>
  <li><strong>Professional Salon Quality:</strong> Dermatologically tested formula suitable for regular daily use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Thoroughly wet hair and scalp with warm water.</li>
  <li><strong>Step 2 (Apply):</strong> Dispense a generous amount of Keratin Smooth shampoo onto palms and spread through hair.</li>
  <li><strong>Step 3 (Massage):</strong> Massage scalp gently with fingertips into a rich lather for 2-3 minutes.</li>
  <li><strong>Step 4 (Rinse):</strong> Rinse completely with warm water until all foam is cleared.</li>
  <li><strong>Step 5 (Condition):</strong> For optimal 72-hour results, follow with TRESemmé Keratin Smooth Conditioner.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Hydrolyzed Keratin:</strong> Low-molecular-weight protein penetrating outer shaft crevices to rebuild damaged bonds.</li>
  <li><strong>Argan Oil (Argania Spinosa Kernel Oil):</strong> Nourishes hair layers with fatty acids and Vitamin E to prevent dryness.</li>
  <li><strong>Dimethiconol:</strong> Protective silicone reflecting ambient light and sealing cuticles against environmental humidity.</li>
  <li><strong>Guar Hydroxypropyltrimonium Chloride:</strong> Anti-static conditioning agent easing combability.</li>
  <li><strong>Gentle Surfactants:</strong> Provide a rich, luxurious foam clearing oil and environmental buildup efficiently.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external use on hair and scalp only.</li>
  <li>Avoid direct contact with eyes; rinse immediately with warm water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
  <li>Discontinue use if severe irritation develops.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dry, frizzy, unmanageable, or coarse hair seeking long-lasting smoothness.</li>
  <li>Individuals looking for professional 72-hour salon-quality frizz control at home.</li>
  <li>Suitable for all hair types, including color-treated and heat-styled hair.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>TRESemmé</td></tr>
  <tr><th>Category</th><td>Hair Care / Keratin & Smooth Shampoos</td></tr>
  <tr><th>Product Type</th><td>Frizz Control & Smoothing Keratin Shampoo</td></tr>
  <tr><th>Volume/Weight</th><td>400 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Ideal for Dry, Frizzy & Unruly Hair)</td></tr>
  <tr><th>Finish</th><td>Sleek, smooth, shiny & frizz-free hair</td></tr>
  <tr><th>Texture</th><td>Pearlescent rich fluid lathering easily</td></tr>
  <tr><th>Fragrance</th><td>Fresh professional salon fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Hydrolyzed Keratin, Argan Oil, Dimethiconol, Guar Chloride</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / UK (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Keratin Repair & 72-Hour Frizz Control</h2>

<h3>What problem does this solve?</h3>
<p>TRESemmé Keratin Smooth Shampoo resolves hair flyaways, frizzy texture, and brittleness caused by protein loss and humidity penetration.</p>

<h3>Why does this condition happen?</h3>
<p>Frizz occurs when damaged cuticles expose the porous cortex to atmospheric humidity. Hair fibers absorb moisture unevenly, swelling and twisting into frizzy strands.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Use Full System:</strong> Pair shampoo with Keratin Smooth conditioner for 72-hour results.<br>
2. <strong>Lukewarm Water:</strong> Wash with lukewarm water to protect cuticle alignment.<br>
3. <strong>Microfiber Towel:</strong> Gently pat dry to avoid mechanical friction.<br>
4. <strong>Heat Protection:</strong> Apply heat spray prior to flat-ironing or blow-drying.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Keratin shampoos replace the need for conditioners."<br>
<strong>Fact:</strong> Shampoos deliver internal protein repair, while conditioners seal external cuticles for maximum smoothness.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Hydrolyzed Keratin micro-proteins penetrate broken cortex micro-gaps to restore structural strength. Argan oil and Dimethiconol form a hydrophobic shield over cuticles, preventing humidity penetration and maintaining sleek alignment for up to 72 hours.</p>"""

    en_faqs = [
        ("What is TRESemmé Keratin Smooth Shampoo?", "It is a professional shampoo enriched with Hydrolyzed Keratin and Argan Oil providing up to 72 hours of frizz control and sleek smoothness."),
        ("What is the benefit of Hydrolyzed Keratin?", "It fills structural protein gaps within damaged hair fibers, fortifying strands against breakage."),
        ("How does Argan Oil enhance the formula?", "It nourishes hair with essential fatty acids and Vitamin E, imparting silky softness and shine."),
        ("Does frizz control really last 72 hours?", "Yes, when used regularly as part of the full TRESemmé Keratin Smooth system."),
        ("What volume is contained in this bottle?", "It comes in a generous 400ml bottle suitable for regular use."),
        ("Is it safe for color-treated hair?", "Yes, its gentle formula is safe for color-treated and chemically styled hair."),
        ("Can men and women use it?", "Yes, it is a unisex formula ideal for anyone with frizzy or unruly hair."),
        ("How often should I use it?", "Use 2 to 3 times weekly for persistent frizz defense."),
        ("Does it help detangle hair?", "Yes, conditioning polymers ease combability and reduce friction tangles."),
        ("What fragrance does it have?", "It features a fresh, professional salon-quality fragrance."),
        ("Does it leave hair greasy?", "No, it cleanses scalp oils effectively while leaving hair lightweight."),
        ("Can it be used on keratin-treated hair?", "Yes, it helps maintain keratin treatment smoothness longer."),
        ("Where is TRESemmé manufactured?", "It is manufactured by Unilever under strict international quality standards."),
        ("Is the formula paraben-free?", "Yes, modern formulations are paraben-free."),
        ("Is it suitable for severely dry hair?", "Yes, it deeply nourishes heat-stressed and dry hair textures."),
        ("How do I verify authenticity at Ekleel Abha?", "All TRESemmé products at Ekleel Abha are 100% genuine from certified Unilever Saudi distributors."),
        ("Should I use conditioner afterward?", "Using matching TRESemmé Keratin Smooth conditioner maximizes smoothness."),
        ("Does it reduce hair fall?", "Fortifying fibers against breakage significantly reduces breakage-induced hair fall."),
        ("Is it suitable for teenagers?", "Yes, safe for adults and teens aged 12+."),
        ("Is it safe for daily use?", "Yes, its gentle formulation supports regular daily washing."),
        ("Does it rinse out cleanly?", "Yes, it rinses out completely with warm water."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Does it protect against heat styling damage?", "Yes, coating fibers reduces thermal friction damage."),
        ("Is the 400ml bottle easy to handle?", "It features an ergonomic shower bottle design."),
        ("Does it add shine to dull hair?", "Yes, clearing buildup and smoothing cuticles restores brilliant shine.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1707",
        "sku": "EK-1707",
        "gtin": "6281006535046",
        "category": "العناية بالشعر / شامبو الكيراتين والنعومة",
        "brand": "TRESemmé",
        "ar": {
            "title": "شامبو كيراتين سموث لتنعيم الشعر الجاف والمتطاير - 400 مل",
            "meta_title": "شامبو تريسمي كيراتين سموث 400مل | صيدلية إكليل أبها",
            "meta_description": "اشتري شامبو تريسمي كيراتين سموث لتنعيم الشعر الجاف والمتطاير (400مل). تحكم بالهيشان حتى 72 ساعة بالكيراتين وزيت الأرجان. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["تريسمي", "كيراتين_سموث", "شامبو_كيراتين", "مكافحة_الهيشان", "إكليل_أبها"]
        },
        "en": {
            "title": "Keratin Smooth Shampoo for Dry and Frizzy Hair - 400ml",
            "meta_title": "TRESemmé Keratin Smooth Shampoo 400ml | Ekleel Abha",
            "meta_description": "Buy TRESemmé Keratin Smooth Shampoo (400ml). 72-hour frizz control with Hydrolyzed Keratin & Argan Oil. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["tresemme", "keratin_smooth", "frizz_control", "hair_care", "ekleel_abha"]
        },
        "schema": {
            "brand": "TRESemmé",
            "category": "Hair Care / Keratin Shampoo",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "tresemme-keratin-smooth-shampoo-400ml.webp",
            "alt": "TRESemmé Keratin Smooth Shampoo 400ml",
            "title": "TRESemmé Keratin Smooth Shampoo 400ml"
        }
    }

print("Loaded 1707 builder")
