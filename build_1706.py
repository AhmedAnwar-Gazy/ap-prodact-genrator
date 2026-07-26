import json, os

def create_product_1706():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعتبر <strong>شامبو باستيل بزيت الأرجان المغذي والمرطب للشعر (Pastel Argan Oil Shampoo - 400ml)</strong> مستحضراً فاخراً يمنح شعركِ حيوية ونعومة استثنائية من الاستخدام الأول. صُمم هذا الشامبو ليعتمد على الخواص الطبيعية المذهلة لزيت الأرجان المغربي الثمين (الذهب السائل)، حيث يغذي الفروة بلطف، يعيد بناء الألياف المتضررة، ويمنح الشعر جدار حماية ضد التلف الحراري والجفاف.</p>
<p>يمتاز الشامبو بتركيبة غنية ومتوازنة الحموضة تنظف الشعر من الدهون الزائدة والأوساخ دون تجريده من مرطباته الطبيعية. بفضل بوليمرات التكييف المتقدمة وفيتامين E، يترك الشعر سهلاً في التمشيط، خالياً من التشابك والهيشان، ومفعماً باللمعان والنعومة الملموسة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتغذية بزيت الأرجان:</strong> يعوض الشعر عن الرطوبة المفقودة وينعم الخصلات الجافة والمجهدة.</li>
  <li><strong>موازنة حموضة الفروة:</strong> يحافظ على استقرار حموضة الجلد لحماية حاجز الفروة وتقليل التهيج.</li>
  <li><strong>معالجة التلف والتقصف:</strong> يغلف ألياف الشعر بطبقة واقية تحد من تكسر الأطراف وتطاير الشعر.</li>
  <li><strong>فك التشابك وتسهيل التصفيف:</strong> يحتوي على البوليكواتيرنيوم-10 الذي يسلس الحركة الميكانيكية للمشط.</li>
  <li><strong>لمعان ونظافة فائقة:</strong> ينظف الرواسب الزهمية بفاعلية ليترك الشعر متألقاً بحيوية طبيعية.</li>
  <li><strong>تركيبة آمنة للاستخدام المنتظم:</strong> خالية من المواد الضارة القاسية وتناسب جميع أنواع الشعر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل):</strong> بلي شعركِ وفروة رأسكِ بالماء الفاتر جيداً.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي كمية مناسبة من شامبو باستيل بالأرجان على كف اليد ووزعيها على الشعر.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي الفروة بأطراف الأصابع بحركات دائرية لمدة 2 إلى 3 دقائق لتكوين رغوة غنية.</li>
  <li><strong>الخطوة الرابعة (الشطف):</strong> اشطفي الشعر جيداً بالماء الفاتر حتى زوال الرغوة تماماً.</li>
  <li><strong>الخطوة الخامسة (التكرار):</strong> كرري العملية إذا لزم الأمر للحصول على نظافة وتغذية مضاعفة.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الأرجان الطبيعي (Argania Spinosa Kernel Oil):</strong> غني بالأحماض الدهنية والأوميغا 6 و 9 وفيتامين E لترميم الشعر.</li>
  <li><strong>بوليكواتيرنيوم-10 (Polyquaternium-10):</strong> عامل تكييف بوليمري يقلل الشحنات الكهروسكونية ويفك تشابك الشعر.</li>
  <li><strong>حمض الستريك (Citric Acid):</strong> يضبط درجة حموضة الشامبو لتناسب الفروة وتغلق حراشف الشعر.</li>
  <li><strong>كوكاميدوبروبيل بيتين:</strong> منظف رغوي لطيف مشتق من الكوكوت ينظف الدهون دون إجهاد.</li>
  <li><strong>مركبات الدايميثيكون:</strong> تنعم السطح الخارجي للشعر وتزيد من اللمعان والسهولة في التحكم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الشعر وفروة الرأس فقط.</li>
  <li>تجنبي ملامسة الشامبو المباشرة للعينين؛ وفي حال ملامستهما اشطفي بالماء الفاتر.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
  <li>في حال ظهور حكة شديدة أو احمرار توقفي عن الاستخدام.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من الشعر الجاف، التالف، أو الهائش الراغبة في ترطيب عميق بزيت الأرجان.</li>
  <li>لمن يبحثون عن شامبو موازن للحموضة يمنح لمس ناعم وسهولة في التمشيط.</li>
  <li>مناسب لجميع أنواع الشعر (العادي، الجاف، المصبوغ).</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>باستيل (Pastel)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / شامبو وزيوت الشعر</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو مرطب ومغذٍ بزيت الأرجان</td></tr>
  <tr><th>الحجم/الوزن</th><td>400 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (خاصة الجاف والتالف)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم، حريري، ومشرق ببريق طبيعي</td></tr>
  <tr><th>الملمس</th><td>سائل غني يرغي بسهولة</td></tr>
  <tr><th>العطر</th><td>عطر الأرجان الطبيعي الناعم</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت الأرجان، بوليكواتيرنيوم-10، حمض الستريك، مرطبات سلكية</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين / المملكة العربية السعودية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Pastel Beauty</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت الأرجان وموازنة حموضة الشعر</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج شامبو باستيل بأرجان مشكلة جفاف خشونة ألياف الشعر وتقصف الأطراف الناجم عن نقص الزيوت المرطبة وزيادة قلوية الفروة بفعل الشامبوهات القاسية.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تتأثر غدد الفروة بالحرارة والكيماويات، مما يقلل إفراز الدهون المغذية، فتفتح حراشف الشعرة وتفقد الماء الداخلي، وتتراكم الشحنات الكهربائية الساكنة التي تسبب الهيشان.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام المنتظم:</strong> استعملي الشامبو 2-3 مرات أسبوعياً.<br>
2. <strong>الشطف بالماء الفاتر:</strong> تجنبي الماء الساخن للحفاظ على زيت الأرجان داخل الخصلات.<br>
3. <strong>التدليك اللطيف:</strong> دلكي بأطراف الأصابع دون حك مفرط.<br>
4. <strong>العناية بالأطراف:</strong> ركزي على غسل أطراف الشعر وتغذيتها بالمرطبات.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "شامبوهات الزيوت تترك الشعر دهنياً ومسترخياً."<br>
<strong>الحقيقة:</strong> زيت الأرجان يخترق الشعرة بسرعة وتركيبة الشامبو تنظف الدهون الزائدة وتترك الخصلات خفيفة ومفعمة بالحجم.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يتغلغل زيت الأرجان الغني بحمض الأوليك واللينوليك داخل الطبقة القشرية للشعر، بينما يقوم البوليكواتيرنيوم-10 بمواجهة الشحنات السالبة على جدار الشعرة، وتعمل جزيئات حمض الستريك على خفض pH الفروة لإغلاق الحراشف وحبس الترطيب.</p>"""

    faqs = [
        ("ما هو شامبو باستيل بزيت الأرجان؟", "هو شامبو مخصص لترطيب وتغذية الشعر الجاف والتالف بفاعلية زيت الأرجان الطبيعي مع موازنة حموضة الفروة."),
        ("ما فائدة زيت الأرجان للشعر؟", "زيت الأرجان غني بالأحماض الدهنية وفيتامين E، يغذي البصيلات ويرمم الألياف المتضررة ويمنح الشعر بريقاً ناعماً."),
        ("هل يترك الشامبو ملمساً زيتيّاً على الشعر؟", "لا، ينظف الفروة بكفاءة ويتغلغل داخل ألياف الشعر دون أي ثقل زيتي."),
        ("ما حجم هذه العبوة؟", "تأتي بحجم 400 مل، وهي كمية وافرة تكفي للاستخدام الأسري المنتظم."),
        ("هل يساعد في فك تشابك الشعر؟", "نعم، يحتوي على مركب البوليكواتيرنيوم-10 الذي يقلل الشحنات الساكنة ويسهل التمشيط."),
        ("هل يناسب الشعر المسبوغ؟", "نعم، تركيبة لطيفة موازنة للحموضة تناسب الشعر المعالج بالألوان."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب لكلا الجنسين ولكافة أنواع الشعر."),
        ("كم مرة يجب استخدامه أسبوعياً؟", "يُنصح باستخدامه من 2 إلى 3 مرات أسبوعياً للحصول على أفضل رطوبة ونظافة."),
        ("هل يمنع تقصف أطراف الشعر؟", "نعم، تغليف ألياف الشعر بمرطبات الأرجان يقلل تكسر الأطراف الهشة."),
        ("ما هي رائحة الشامبو؟", "يتميز برائحة ناعمة ومنعشة تعكس عبير الأرجان الطبيعي."),
        ("هل يساعد الشامبو في تنعيم الشعر الهيش؟", "نعم، يقلل الهيشان ويمنح الخصلات ملمساً حريرياً."),
        ("هل يحتوي على حمض الستريك لموازنة الفروة؟", "نعم، يحتوي على حمض الستريك لضبط درجة الحموضة لحماية الفروة."),
        ("هل يلزم استخدام بلسم بعده؟", "يُفضل استخدام بلسم مرطب لزيادة التغذية وحبس الرطوبة."),
        ("ما هو بلد صنع شامبو باستيل؟", "تم تصنيعه وفق أعلى معايير العناية بالشعر العالمية."),
        ("هل يناسب البشرة والفروة الجافة؟", "نعم، ممتاز جداً للفروة التي تعاني من الجفاف والحكة الخفيفة."),
        ("هل يترك أي بقايا بعد الشطف؟", "لا، يشطف بسهولة وسرعة بالماء الفاتر."),
        ("هل يناسب الأطفال؟", "مناسب من سن 12 سنة فما فوق."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "كافة منتجات إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يساعد في حماية الشعر من حرارة السيشوار؟", "نعم، تغليف ألياف الشعر يخفف تأثر الخصلات بالحرارة."),
        ("هل يمنح الشعر لمعاناً طبيعياً؟", "نعم، ينظف الرواسب ويكسب الشعر بريقاً كراستالياً."),
        ("هل عبوة 400 مل سهلة الاستخدام؟", "تأتي بتصميم عصري يسهل التعامل معه داخل الاستحمام."),
        ("هل يسبب تساقط الشعر؟", "لا، بل يغذي البصلات ويحمي الخصلات من التكسر."),
        ("هل يناسب الشعر الدهني؟", "ينظف الدهون بفاعلية ويرطب الأطراف بمرونة."),
        ("هل يحتوي على بروتينات مغذية؟", "يحتوي على زيوت وأحماض مرطبة ترمم بروتينات الشعرة."),
        ("هل يلزم رج العبوة؟", "لا يلزم، القوام متجانس وجاهز للاستخدام.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Pastel Argan Oil Shampoo (400ml)</strong> is a premium moisturizing hair wash designed to restore softness, shine, and vitality to dry or damaged hair. Harnessing the legendary nourishing properties of natural Moroccan Argan Oil (Liquid Gold), this shampoo purifies the scalp while conditioning the hair shaft to defend against heat damage and environmental drying.</p>
<p>Featuring a pH-balanced, protective formula, it removes excess sebum and styling buildup without stripping hair cuticles. Enriched with Polyquaternium-10 conditioning polymers and essential fatty acids, it eases detangling, tames stubborn frizz, and leaves hair soft, silky, and naturally luminous.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Argan Oil Hydration:</strong> Infuses moisture into dry, stressed strands for renewed elasticity.</li>
  <li><strong>Scalp pH Balance:</strong> Maintains optimal scalp acidity to protect the skin barrier and prevent irritation.</li>
  <li><strong>Damage & Breakage Defense:</strong> Coats hair cuticles to diminish split ends and flyaway frizz.</li>
  <li><strong>Enhanced Detangling:</strong> Polyquaternium-10 smooths mechanical friction for effortless combing.</li>
  <li><strong>Luminous Cleanliness:</strong> Clears oil and residue, revealing brilliant natural hair shine.</li>
  <li><strong>Safe Daily Care:</strong> Free of harsh irritating agents, suitable for regular family use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Thoroughly wet hair and scalp with warm water.</li>
  <li><strong>Step 2 (Apply):</strong> Dispense an adequate amount of shampoo onto palms and spread over hair.</li>
  <li><strong>Step 3 (Massage):</strong> Massage scalp gently with fingertips for 2-3 minutes into a rich lather.</li>
  <li><strong>Step 4 (Rinse):</strong> Rinse completely with warm water until all foam is removed.</li>
  <li><strong>Step 5 (Repeat):</strong> Repeat if needed for extra deep cleansing and nourishment.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Argan Oil:</strong> Rich in omega fatty acids and Vitamin E to repair damaged hair structures.</li>
  <li><strong>Polyquaternium-10:</strong> Conditioning polymer neutralizing static charges for smooth detangling.</li>
  <li><strong>Citric Acid:</strong> Balances product pH to align and seal cuticles, enhancing natural shine.</li>
  <li><strong>Cocamidopropyl Betaine:</strong> Gentle coconut-derived surfactant clearing oils without harshness.</li>
  <li><strong>Dimethicone:</strong> Smooths the hair surface, sealing in moisture and adding weightless shine.</li>
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
  <li>Anyone with dry, damaged, or frizzy hair seeking deep Argan oil hydration.</li>
  <li>Individuals looking for a pH-balanced detangling shampoo for easy daily combing.</li>
  <li>Suitable for all hair types (normal, dry, color-treated).</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Pastel</td></tr>
  <tr><th>Category</th><td>Hair Care / Shampoos & Oils</td></tr>
  <tr><th>Product Type</th><td>Moisturizing Argan Oil Shampoo</td></tr>
  <tr><th>Volume/Weight</th><td>400 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Ideal for Dry & Damaged Hair)</td></tr>
  <tr><th>Finish</th><td>Soft, silky, radiant & manageable hair</td></tr>
  <tr><th>Texture</th><td>Rich fluid lathering easily</td></tr>
  <tr><th>Fragrance</th><td>Subtle fresh natural Argan aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Argan Oil, Polyquaternium-10, Citric Acid, Silky Conditioners</td></tr>
  <tr><th>Country of Origin</th><td>China / Saudi Arabia</td></tr>
  <tr><th>Manufacturer</th><td>Pastel Beauty</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Argan Oil & Scalp pH Homeostasis</h2>

<h3>What problem does this solve?</h3>
<p>Pastel Argan Oil Shampoo resolves hair shaft roughness, brittleness, and split ends caused by lipid depletion and elevated scalp alkalinity from harsh cleansers.</p>

<h3>Why does this condition happen?</h3>
<p>Frequent heat styling and environmental exposure strip lipid reserves from the cuticle layer. Elevated pH opens cuticles, causing water loss, static buildup, and persistent frizz.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Regular Cleansing:</strong> Wash 2-3 times weekly with Pastel Argan Shampoo.<br>
2. <strong>Lukewarm Water:</strong> Rinse with lukewarm water to preserve essential lipids.<br>
3. <strong>Gentle Massage:</strong> Massage softly with fingertips without aggressive friction.<br>
4. <strong>Condition Ends:</strong> Focus on conditioning ends to seal moisture.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Oil shampoos leave hair heavy and greasy."<br>
<strong>Fact:</strong> Argan oil absorbs rapidly while the shampoo formula cleanses excess sebum, maintaining light volume.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Argan oil oleic and linoleic acids penetrate the cortex, while Polyquaternium-10 neutralizes negative charges on the hair shaft. Citric acid lowers formula pH to seal cuticles, trapping moisture and boosting shine.</p>"""

    en_faqs = [
        ("What is Pastel Argan Oil Shampoo?", "It is a moisturizing hair shampoo enriched with natural Argan Oil designed to restore softness, shine, and pH balance to dry or damaged hair."),
        ("What are the benefits of Argan Oil for hair?", "Argan Oil is rich in essential fatty acids and Vitamin E, repairing damaged fibers and adding natural shine."),
        ("Does it leave hair greasy?", "No, it cleanses scalp oils effectively while providing internal hydration without weight."),
        ("What volume is contained in this bottle?", "It comes in a 400ml bottle suitable for regular family use."),
        ("Does it assist with hair detangling?", "Yes, Polyquaternium-10 reduces static and smooths hair for easy combing."),
        ("Is it safe for color-treated hair?", "Yes, its gentle pH-balanced formula protects colored hair."),
        ("Can men and women use it?", "Yes, it is a unisex shampoo suitable for all hair types."),
        ("How often should I use it?", "It is recommended to use 2 to 3 times weekly for optimal hydration."),
        ("Does it prevent split ends?", "Yes, coating hair fibers with Argan lipids minimizes split end breakage."),
        ("What scent does the shampoo have?", "It features a subtle, fresh natural Argan fragrance."),
        ("Does it reduce frizzy hair?", "Yes, it smooths cuticles, significantly reducing frizz."),
        ("Does it contain Citric Acid for pH balance?", "Yes, Citric Acid aligns product pH to protect the scalp barrier."),
        ("Should I use conditioner afterward?", "Pairing with a hydrating conditioner maximizes moisture retention."),
        ("Where is Pastel Shampoo manufactured?", "It is produced according to international hair care quality standards."),
        ("Is it suitable for dry scalps?", "Yes, it soothes and moisturizes dry scalps effectively."),
        ("Does it rinse out easily?", "Yes, it rinses out completely with warm water."),
        ("Is it suitable for teenagers?", "Yes, safe for adults and teens aged 12+."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it protect against styling heat?", "Yes, Argan oil lipids shield strands from thermal stress."),
        ("Does it restore natural hair shine?", "Yes, clearing buildup reveals brilliant natural hair shine."),
        ("Is the 400ml bottle convenient to use?", "It features an ergonomic shower bottle design."),
        ("Does it cause hair fall?", "No, it fortifies fibers against breakage-induced hair fall."),
        ("Is it suitable for oily hair?", "It cleanses sebum effectively while keeping ends flexible."),
        ("Does it contain nourishing proteins?", "It contains hydrating lipids that repair structural proteins."),
        ("Does it require shaking before use?", "No, its homogeneous formula is ready for direct use.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1706",
        "sku": "EK-1706",
        "gtin": "6924833411137",
        "category": "العناية بالشعر / شامبو وزيوت الشعر",
        "brand": "Pastel",
        "ar": {
            "title": "شامبو باستيل بزيت الارجان المغذي والمرطب للشعر - 400 مل",
            "meta_title": "شامبو باستيل بزيت الارجان 400مل | صيدلية إكليل أبها",
            "meta_description": "اشتري شامبو باستيل بزيت الأرجان المرطب والمغذي للشعر (400مل). ترميم التلف وموازنة الحموضة لجميع أنواع الشعر. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["باستيل", "شامبو_الارجان", "زيت_الارجان", "العناية_بالشعر", "إكليل_أبها"]
        },
        "en": {
            "title": "Pastel Argan Oil Shampoo 400ml",
            "meta_title": "Pastel Argan Oil Shampoo 400ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy Pastel Argan Oil Shampoo (400ml). Deeply hydrates and balances pH for dry, damaged hair. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["pastel", "argan_shampoo", "argan_oil", "hair_care", "ekleel_abha"]
        },
        "schema": {
            "brand": "Pastel",
            "category": "Hair Care / Shampoo",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "pastel-argan-oil-shampoo-400ml.webp",
            "alt": "Pastel Argan Oil Shampoo 400ml",
            "title": "Pastel Argan Oil Shampoo 400ml"
        }
    }

print("Loaded 1706 builder")
