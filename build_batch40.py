import json, os

def create_product_1912():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم الجسم المكثف من دوف 75 مل (Dove Intensive Body Cream 75ml)</strong> كريم العناية المكثفة والترطيب العميق الأصيل من دوف المصمم طبياً لإعادة المرونة والنعومة للبشرة شديدة الجفاف والمناطق المجهدة. يرتكز هذا الكريم الفاخر (Dove Intensive Nourishing Body Cream 75ml) على مركب النوترا ديو الحصري (NutriDUO Complex)، الجليسرين المرطب، والزيوت المغذية الطبيعية للبشرة.</p>
<p>يعمل كريم دوف المكثف على اختراق طبقات الجلد العميقة لترطيب وإعادة بناء حاجز الترطيب الطبيعي لـ 24 ساعة، التخلص التام من الجفاف والحكة والخشونة، وتنعيم المناطق الجافة كالمرفقين والركبتين، ليترك بشرتك ناعمة كالحرير، ناضرة، ومعطرة بالنظافة الأيقونية لدوف.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب عميق ومكثف لـ 24 ساعة بمركب NutriDUO:</strong> يغذي طبقات الجلد العميقة ويمنع تبخر الرطوبة.</li>
  <li><strong>إصلاح الجفاف الشديد والخشونة بالمرفقين والركبتين:</strong> يعيد المرونة والنعومة للجلد المتصلب.</li>
  <li><strong>تركيبة خفيفة غير دهنية سريعة الامتصاص:</strong> تغذي البشرة عمقاً دون ترك أثر دهني ثقيل.</li>
  <li><strong>عطر دوف الأيقوني الناعم:</strong> يمنح الجسم رائحة النظافة والأناقة طوال اليوم.</li>
  <li><strong>مختبر جلدياً وآمن للبشرة الحساسة:</strong> لطيف ومناسب لجميع أنواع البشرة الجافة وشديدة الجفاف.</li>
  <li><strong>عبوة مدمجة سعة 75 مل:</strong> حجم أنيق مثالي لحقيبة اليد والسفر والعناية السريعة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> ضعي الكريم على بشرة جافة ونظيفة (يُفضل بعد الاستحمام).</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> خذي كمية مناسبة ودلكي بها الجسم أو المناطق شديدة الجفاف كالكعبين والمرفقين.</li>
  <li><strong>الخطوة الثالثة (الامتصاص):</strong> دلكي بحركات دائرية ناعمة حتى امتصاص الكريم بالكامل (يُستعمل يومياً صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركب NutriDUO وزيوت العناية الطبيعية:</strong> يجمع بين المكونات المرطبة والمغذيات الطبيعية للبشرة.</li>
  <li><strong>الجليسرين النقي:</strong> يجذب الرطوبة من الجو ويحبسها داخل طبقات البشرة العميقة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم واليدين فقط.</li>
  <li>تجنبي التلامس مع العينين وفي حال التلامس اشطفي بالماء.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من الجفاف الشديد والخشونة ويبحث عن كريم دوف المكثف 75 مل للترطيب والنعومة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>دوف (Dove)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / كريمات دوف المكثفة لترطيب البشرة شديدة الجفاف 75ml</td></tr>
  <tr><th>نوع المنتج</th><td>كريم جسم مغذٍ ومكثف بمركب NutriDUO والجليسرين للترطيب العميق (75ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>75 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الجافة وشديدة الجفاف والمناطق الخشنة (كالمرفقين والركبتين)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة كالحرير، مرطبة عمقاً لـ 24 ساعة ومحمية من الجفاف</td></tr>
  <tr><th>الملمس</th><td>كريم غني ناعم سريع الامتصاص دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر دوف الكلاسيكي الناعم الأيقوني</td></tr>
  <tr><th>المكونات النشطة</th><td>مركب NutriDUO، جليسرين نقي، زيوت مغذية طبيعية</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا / الإمارات العربية المتحدة</td></tr>
  <tr><th>الشركة المصنعة</th><td>Dove (Unilever Group)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد مركب NutriDUO والجليسرين في كريم دوف المكثف (Dove Intensive)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم دوف المكثف مشكلة الجفاف الشديد للبشرة، تشقق المرفقين والركبتين، والحكة وتصلب الجلد الناتجة عن نقص الترطيب.</p>

<h3>لماذا تنجح تقنية مركب NutriDUO؟</h3>
<p>لأن مركب NutriDUO يدمج بين مغذيات الجلد الطبيعية والزيوت المرطبة الغنية لترطيب سطح الجلد وتغذية أعماقه بشكل متزامن.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق فور الاستحمام:</strong> حبس الرطوبة المتبقية على الجلد يضاعف مفعول الكريم.<br>
2. <strong>العناية بالمناطق الخشنة:</strong> التركيز على المرفقين والركبتين مرتين يومياً.<br>
3. <strong>الشرب الكافي للماء:</strong> يدعم مرونة البشرة الداخلية بجانب الترطيب الخارجي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الكريمات المكثفة تترك طبقة دهنية مزعجة على البشرة."<br>
<strong>الحقيقة:</strong> كريم دوف المكثف مصمم بتركيبة سريعة الامتصاص تنفذ للجلد دون لزوجة أو ثقل.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعمل الجليسرين كمرطب جاذب للماء (Humectant) يربط جزيئات الماء بكيراتين الطبقة القرنية، بينما تشكل الزيوت طبقة عازلة (Occlusion) تمنع التبخر.</p>"""

    faqs = [
        ("ما هو كريم الجسم المكثف من دوف 75 مل؟", "هو كريم مغذٍ ومكثف من دوف بمركب NutriDUO والجليسرين لترطيب وإصلاح البشرة شديدة الجفاف 75 مل."),
        ("ما هي فوائد مركب NutriDUO والجليسرين؟", "يغذي NutriDUO الطبقات العميقة للجلد، بينما يجذب الجليسرين الرطوبة ويحبسها لـ 24 ساعة."),
        ("هل يصلح للمرفقين والركبتين والمناطق الخشنة؟", "نعم، ممتاز لإعادة المرونة والنعومة للمرفقين والركبتين والكعبين."),
        ("ما حجم العبوة؟", "تأتي بعبوة سعة 75 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية مناسبة ودلكي بحركات دائرية على بشرة جافة ونظيفة حتى الامتصاص الكامل مرتين يومياً."),
        ("هل يترك أثراً دهنياً لزجاً؟", "لا، قوام غني سريع الامتصاص دون لزوجة."),
        ("أين صُنع كريم دوف المكثف؟", "صُنع في ألمانيا/الإمارات بواسطة مجموعة Unilever."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات دوف لدى إكليل أبها أصلية 100%."),
        ("ما رائحة كريم دوف المكثف؟", "عطر دوف الكلاسيكي الناعم الأيقوني."),
        ("هل يمنح ترطيباً يدوم 24 ساعة؟", "نعم، ينفذ للجلد ويمنح ترطيباً مستمراً طوال اليوم."),
        ("هل 75 مل مناسبة للسفر والتنقل؟", "نعم، حجم مدمج أنيق مثالي لحقيبة اليد والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب البشرة الحساسة؟", "نعم، مختبر جلدياً وآمن للبشرة الحساسة الجافة."),
        ("كم مرة يومياً؟", "مرتين يومياً: صباحاً ومساءً."),
        ("هل يناسب اليدين والقدمين أيضاً؟", "نعم، ممتاز لليدين والقدمين وكامل الجسم."),
        ("هل دوف هي العلامة الأولى في ترطيب البشرة؟", "نعم، Dove من أشهر وأعرق علامات العناية بالبشرة عالمياً."),
        ("هل يساعد في تهيج الجفاف والحكة؟", "نعم، يهدئ الحكة ويمنح راحة فورية للبشرة المتهيجة بالجفاف."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب لجميع الفئات من 12 سنة."),
        ("هل قوامه ثقيل أم كريمي ناعم؟", "كريمي ناعم يمتص بسلاسة دون ثقل."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل ينعم الجلد المتصلب بسرعة؟", "نعم، تلاحظ النعومة والاطمئنان من الاستخدام الأول."),
        ("هل يصلح كهدية لطيفة؟", "نعم، حجم مدمج أنيق مفيد كهدية."),
        ("هل يحمي من تقلبات الطقس والجفاف الشتوي؟", "نعم، يحمي البشرة تماماً من جفاف الشتاء والطقس البارد."),
        ("هل يمكن استخدامه على الوجه؟", "مخصص للجسم واليدين، ويُفضل استخدام كريمات دوف المخصصة للوجه.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Dove Intensive Body Cream, 75 ml</strong> is the iconic intensive care and deep hydration cream from Dove formulated to restore elasticity and softness to extra dry skin and rough areas. Powered by exclusive NutriDUO Complex, hydrating Glycerin, and natural skin-nourishing oils.</p>
<p>Dove Intensive Cream penetrates deep skin layers to hydrate and rebuild the natural moisture barrier for 24 hours, eliminating dryness, itching, and calloused skin on elbows and knees, leaving your skin touchably soft, radiant, and fragranced with Dove's signature cleanliness.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intensive 24-Hour Hydration with NutriDUO Complex:</strong> Nourishes deep skin layers and prevents moisture loss.</li>
  <li><strong>Extra Dry Skin & Rough Elbow/Knee Repair:</strong> Restores elasticity and softness to hardened skin.</li>
  <li><strong>Lightweight Fast-Absorbing Formula:</strong> Deeply nourishes skin without leaving a heavy greasy layer.</li>
  <li><strong>Signature Soft Dove Fragrance:</strong> Gives the body an iconic scent of cleanliness and elegance.</li>
  <li><strong>Dermatologically Tested & Sensitive Skin Safe:</strong> Gentle and suitable for all dry and extra dry skin types.</li>
  <li><strong>Compact 75ml Tub:</strong> Elegant compact size ideal for handbag, travel, and on-the-go care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Apply cream on clean dry skin (preferably post-shower).</li>
  <li><strong>Step 2 (Apply):</strong> Take a suitable amount and massage over body or extra dry areas like heels and elbows.</li>
  <li><strong>Step 3 (Absorb):</strong> Massage in gentle circular motions until fully absorbed (use daily morning and night).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>NutriDUO Complex & Natural Oils:</strong> Combine skin-natural nutrients with rich moisturizing oils.</li>
  <li><strong>Pure Glycerin:</strong> Draws moisture from the air locking it into deep skin layers.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body and hand skin application only.</li>
  <li>Avoid contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from extra dry skin and roughness seeking Dove Intensive 75ml Cream for deep hydration and softness.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Dove</td></tr>
  <tr><th>Category</th><td>Body Care / Dove Intensive Hydration Body Creams for Extra Dry Skin 75ml</td></tr>
  <tr><th>Product Type</th><td>NutriDUO & Glycerin Intensive Nourishing Body Cream for Extra Dry Skin (75ml)</td></tr>
  <tr><th>Volume/Weight</th><td>75 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Dry to Extra Dry Skin & Rough Areas (Elbows, Knees & Heels)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24-hour deeply hydrated & protected skin</td></tr>
  <tr><th>Texture</th><td>Rich smooth fast-absorbing cream without greasiness</td></tr>
  <tr><th>Fragrance</th><td>Classic soft iconic Dove fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>NutriDUO Complex, Pure Glycerin, Natural Oils</td></tr>
  <tr><th>Country of Origin</th><td>Germany / UAE</td></tr>
  <tr><th>Manufacturer</th><td>Dove (Unilever Group)</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of NutriDUO Dual-Action Nourishment & Glycerin Humectant Action</h2>

<h3>What problem does this solve?</h3>
<p>Dove Intensive Body Cream resolves extra skin dryness, cracked elbows and knees, and itching and tightness caused by severe dehydration.</p>

<h3>Why choose Dove Intensive Body Cream?</h3>
<p>NutriDUO combines skin-natural nutrients and rich moisturizing oils to hydrate skin surfaces while feeding deep epidermal layers simultaneously.</p>"""

    en_faqs = [
        ("What is Dove Intensive Body Cream, 75 ml?", "It is an intensive nourishing body cream from Dove with NutriDUO Complex and Glycerin for repairing extra dry skin (75ml)."),
        ("What are the benefits of NutriDUO Complex and Glycerin?", "NutriDUO nourishes deep skin layers while Glycerin draws and locks in moisture for 24 hours."),
        ("Is it suitable for elbows, knees, and rough areas?", "Yes, excellent for restoring softness and elasticity to elbows, knees, and heels."),
        ("What volume is contained in this tub?", "75ml."),
        ("How do I use it correctly?", "Apply suitable amount on clean dry skin, massage in circular motions until absorbed twice daily."),
        ("Does it leave a greasy sticky residue?", "No, rich formula absorbs quickly without stickiness."),
        ("Where is Dove Intensive Cream manufactured?", "In Germany/UAE by Unilever Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All Dove products at Ekleel Abha are 100% original."),
        ("What does Dove Intensive Cream smell like?", "Classic soft iconic Dove cleanliness scent."),
        ("Does it deliver 24-hour hydration?", "Yes, penetrates deeply providing 24-hour continuous moisture."),
        ("Is 75ml compact for travel?", "Yes, compact tub perfect for handbag and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for sensitive dry skin?", "Yes, dermatologically tested safe for sensitive dry skin."),
        ("How many times daily?", "Twice daily: morning and night."),
        ("Is it suitable for hands and feet too?", "Yes, great for hands, feet, and full body."),
        ("Is Dove a globally trusted brand?", "Yes, Dove is one of the world's most trusted skincare brands."),
        ("Does it help soothe dry skin itching?", "Yes, soothes dryness itching providing immediate comfort."),
        ("Is the tub recyclable?", "Yes."),
        ("Is it suitable for men and women?", "Yes, suitable for all ages 12+."),
        ("Is the texture heavy or smooth?", "Smooth cream that absorbs easily without heaviness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it soften hardened skin quickly?", "Yes, softness and comfort are noticeable from first use."),
        ("Is it a nice compact gift?", "Yes, elegant compact tub ideal as a gift."),
        ("Does it protect against winter dryness?", "Yes, shields skin against harsh winter cold dryness."),
        ("Can it be used on the face?", "Designed for body/hands; prefer Dove facial creams for face.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1912",
        "sku": "EK-1912",
        "gtin": "6281006409545",
        "brand": "Dove",
        "ar": {
            "title": "كريم الجسم المكثف من دوف، 75 مل",
            "meta_title": "كريم الجسم المكثف دوف 75مل | إكليل أبها",
            "meta_description": "اشتري كريم الجسم المكثف من دوف (75 مل). كريم مغذٍ بمركب NutriDUO للجليسرين لترطيب وإصلاح البشرة شديدة الجفاف. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["دوف", "كريم_جسم_مكثف", "ترطيب_البشرة_الجافة", "نوترا_ديو", "إكليل_أبها"]
        },
        "en": {
            "title": "Dove Intensive Body Cream, 75 ml",
            "meta_title": "Dove Intensive Body Cream 75ml | Ekleel Abha",
            "meta_description": "Buy original Dove Intensive Body Cream (75ml). NutriDUO & Glycerin intensive cream for extra dry skin hydration. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["dove", "intensive_body_cream", "extra_dry_skin", "nutriduo", "ekleel_abha"]
        }
    }


def create_product_1913():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>شامبو للأطفال من نونو 200 مل (Nunu Baby Shampoo - 200 ml)</strong> شامبو الأطفال الأصيل الخالي من الدموع من نونو المصمَّم خصيصاً لتنظيف شعر وفروة رأس الرضع والأطفال الرقيقة بجمال وأمان تدمع له القلوب حنواً لا ألم. يرتكز هذا الشامبو الطبي (Nunu Baby Shampoo 200ml) على تركيبة لا دموع بعد اليوم (No More Tears)، خلاصة البابونج المهدئة، والمواد المنظفة النباتية اللطيفة للغاية.</p>
<p>يعمل شامبو نونو للأطفال على تنظيف شعر الطفل وفروة رأسه بفاعلية دون إحداث أي حرقان بالعينين، حفظ الترطيب الطبيعي لشعر الطفل، وتسهيل التمشيط وإعطاء الشعر لمعاناً ونعومة فائقتين، ليترك شعر طفلك ناعماً كالحرير، سهلاً في التمشيط، ومعطراً بعطر نونو الخالي من الحساسية.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تركيبة خالية تماماً من الدموع (No Tears Formula):</strong> لا تسبب حرقان بالعينين أثناء الغسيل.</li>
  <li><strong>تنظيف لطيف لشعر وفروة رأس الرضع:</strong> ينظف دون انتزاع الزيوت الطبيعية الواقية.</li>
  <li><strong>تهدئة وعناية بالفروة بخلاصة البابونج:</strong> يقي فروة رأس الطفل من الجفاف والتهيج.</li>
  <li><strong>تنعيم وتسهيل تمشيط الشعر:</strong> يمنح الشعر لمعاناً ونعومة ويسهل التسريح.</li>
  <li><strong>خالٍ 100% من الصابون، البارابين والكحول:</strong> آمن تماماً للرضع من الولادة.</li>
  <li><strong>عبوة اقتصادية 200 مل:</strong> سعة مناسبة تكفي لاستخدام يومي مستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (البلل):</strong> بللي شعر الطفل وفروة رأسه بالماء الدافئ.</li>
  <li><strong>الخطوة الثانية (التغسيل):</strong> ضعي كمية مناسبة من شامبو نونو في كف اليد وكوّني رغوة ناعمة.</li>
  <li><strong>الخطوة الثالثة (التدليك والشطف):</strong> دلكي شعر وفروة رأس الطفل برفق ثم اشطفي بالماء الدافئ جيداً (يُستعمل عند كل استحمام).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>منظفات نباتية فائقة اللطف:</strong> تنظف الشعر والجلد دون إحداث تهيج للعينين أو البشرة.</li>
  <li><strong>خلاصة البابونج النقي:</strong> تهدئ فروة رأس الطفل وتمنحه لمسية نعومة ورائحة عطرة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على شعر وفروة رأس الأطفال فقط.</li>
  <li>على الرغم من أنه لا يسبب الدموع يُنصح بتجنب السكب المباشر في عين الطفل.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل أم تبحث عن شامبو نونو للأطفال 200 مل لتنظيف شعر طفلها برفق وبدون دموع.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>نونو (Nunu)</td></tr>
  <tr><th>الفئة</th><td>العناية بالأطفال / شامبوهات نونو الخالية من الدموع للأطفال 200ml</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو أطفال لطيف بخالي من الدموع والبارابين بخلاصة البابونج (200ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>200 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>شعر وفروة رأس الأطفال الرضع والصغار (من الولادة)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر طفل ناعم، لامع، سهل التمشيط وفروة رأس مهدأة ونظيفة</td></tr>
  <tr><th>الملمس</th><td>سائل شامبو الذهبي الناعم الرغوي</td></tr>
  <tr><th>العطر</th><td>عطر نونو اللطيف الخاص بالأطفال</td></tr>
  <tr><th>المكونات النشطة</th><td>تركيبة لا دموع (No Tears)، خلاصة البابونج، منظفات نباتية لطيفة</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Nunu Baby Care Products</td></tr>
  <tr><th>الفئة العمرية</th><td>الرضع والأطفال (من الولادة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد تركيبة لا دموع وخلاصة البابونج في شامبو نونو للأطفال</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج شامبو نونو للأطفال مشكلة حرقان عين الطفل عند الغسيل بشامبوهات الكبار، جفاف فروة رأس الطفل، وصعوبة تمشيط شعر الرضع.</p>

<h3>لماذا تنجح تركيبة لا دموع (No Tears)؟</h3>
<p>لأن تركيبة الشامبو تمتلك قيمة أس هيدروجيني (pH) ومتطلبات ضغط أسموزي مطابقة تماماً لدموع العين الطبيعية، مما يمنع الوخز والحرقان.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستحمام بماء دافئ:</strong> يساعد في راحة الطفل وسهولة التنظيف.<br>
2. <strong>التدليك اللطيف برؤوس الأصابع:</strong> دون حك فروة رأس الرضيع الرقيقة.<br>
3. <strong>التجفيف بفوطة ناعمة:</strong> لمنع تشابك الشعر بعد الغسيل.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "شامبو الأطفال يسبب جفاف الشعر لأنه لا يحتوي على بلسم."<br>
<strong>الحقيقة:</strong> شامبو نونو يحتوي على خلاصات مرطبة تترك شعر الطفل ناعماً وسهل التمشيط دون الحاجة لبلسم ثقيل.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تستخدم الخواص السطحية المنخفضة التوتر (Low-Tension Surfactants) لجزيئات غسل نونو لإزالة الأوساخ دون اختراق الغشاء المخاطي للعين.</p>"""

    faqs = [
        ("ما هو شامبو للأطفال من نونو 200 مل؟", "هو شامبو لطيف للأطفال من نونو بتركيبة لا دموع وخلاصة البابونج لتنظيف شعر وفروة رأس الرضع والأطفال (200 مل)."),
        ("ما هي فوائد تركيبة لا دموع وخلاصة البابونج؟", "تمنع تركيبة لا دموع حرقان العينين، بينما تهدئ خلاصة البابونج فروة الرأس وتمنح الشعر نعومة."),
        ("هل يسبب حرقان بالعينين أثناء الاستحمام؟", "لا، تركيبة خالية من الدموع ومطابقة للpH الدمعي الطبيعي."),
        ("ما حجم العبوة؟", "تأتي بسعة 200 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي شعر الطفل بالماء الدافئ، ضعي الشامبو وكوّني رغوة، دلكي برفق ثم اشطفي بالماء."),
        ("هل هو آمن للرضع من الولادة؟", "نعم، آمن ولطيف 100% للرضع والأطفال من الولادة."),
        ("أين صُنع شامبو نونو للأطفال؟", "صُنع في المملكة العربية السعودية بواسطة Nunu Baby Care."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات نونو لدى إكليل أبها أصلية 100%."),
        ("هل يجعل شعر الطفل سهلاً في التمشيط؟", "نعم، ينعم الشعر ويمنع تشابكه."),
        ("ما رائحة شامبو نونو للأطفال؟", "عطر نونو اللطيف الخاص بالأطفال."),
        ("هل يترك الشعر لامعاً ونظيفاً؟", "نعم، يمنح الشعر لمعاناً ونظافة فائقة."),
        ("هل 200 مل تكفي للاستخدام المستمر؟", "نعم، تكفي لعدة أشهر من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل هو خالي من الصابون والبارابين والكحول؟", "نعم، خالي 100% من الصابون والبارابين والكحول."),
        ("هل يهدئ فروة رأس الطفل؟", "نعم، خلاصة البابونج تهدئ فروة الرأس من التهيج والجفاف."),
        ("كم مرة يُفضل استخدامه؟", "عند كل استحمام للطفل."),
        ("هل يزيل قشرة الرأس لدى الرضع؟", "ينظف الفروة بلطف ويساعد في الحفاظ على سلامتها ونظافتها."),
        ("هل شامبو نونو من أشهر شامبوهات الأطفال في السعودية؟", "نعم، Nunu Baby Shampoo من أعرق وأشهر شامبوهات الأطفال في السعودية."),
        ("هل يناسب جميع أنواع شعر الأطفال؟", "نعم، مناسب للشعر الناعم والكثيف والمجعد للأطفال."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمكن للكبار ذوي الفروة الحساسة استخدامه؟", "نعم، الكبار ذوو الفروة الحساسة جداً يفضلون استخدامه أحياناً."),
        ("هل ينتج رغوة ناعمة وفيرة؟", "نعم، ينتج رغوة ناعمة تنظف بسهولة."),
        ("هل ينشطف بالماء سريعاً؟", "نعم، ينشطف بالماء بسهولة ودون ترك أثر لزج."),
        ("هل يصلح هدية لمولود جديد؟", "نعم، هدية عملية وممتازة ضمن مجموعة العناية بالمولود."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Nunu Baby Shampoo - 200 ml</strong> is the iconic tear-free baby shampoo from Nunu formulated to clean infant and child hair and scalp safely and lovingly. Engineered with No More Tears technology, soothing Chamomile extract, and ultra-gentle plant-derived cleansing agents.</p>
<p>Nunu Baby Shampoo cleanses baby hair and scalp effectively without causing any eye sting or burning, preserves natural moisture balance, and makes hair smooth, shiny, and easy to comb, leaving your baby's hair touchably soft and fragranced with Nunu's hypoallergenic baby scent.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Tear-Free Formula (No Tears):</strong> Does not cause eye burning or irritation during bath time.</li>
  <li><strong>Gentle Infant Hair & Scalp Cleansing:</strong> Cleanses without stripping natural protective oils.</li>
  <li><strong>Chamomile Scalp Care & Soothing:</strong> Shields baby's scalp from dryness and irritation.</li>
  <li><strong>Softening & Easy Hair Combing:</strong> Imparts hair shine and softness making combing effortless.</li>
  <li><strong>100% Soap-Free, Paraben-Free & Alcohol-Free:</strong> Completely safe for infants from birth.</li>
  <li><strong>Generous 200ml Bottle:</strong> Suitable volume for continuous daily baby care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet baby's hair and scalp with warm water.</li>
  <li><strong>Step 2 (Lather):</strong> Apply a suitable amount of Nunu shampoo into palms and work into a soft lather.</li>
  <li><strong>Step 3 (Massage & Rinse):</strong> Gently massage hair and scalp, then rinse thoroughly with warm water (use during every bath).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Ultra-Gentle Plant Cleansers:</strong> Cleanse hair and scalp skin without causing eye or skin irritation.</li>
  <li><strong>Pure Chamomile Extract:</strong> Soothes baby's scalp giving soft touch and pleasant scent.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external child hair and scalp application only.</li>
  <li>Although tear-free, avoid pouring directly into baby's eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every mother seeking Nunu Baby Shampoo 200ml for tear-free, gentle baby hair cleansing.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Nunu</td></tr>
  <tr><th>Category</th><td>Baby Care / Nunu Tear-Free Hydrating Baby Shampoos 200ml</td></tr>
  <tr><th>Product Type</th><td>Tear-Free Soap-Free Chamomile Infant & Child Shampoo (200ml)</td></tr>
  <tr><th>Volume/Weight</th><td>200 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Infant & Child Hair & Delicate Scalp (From Birth)</td></tr>
  <tr><th>Finish</th><td>Soft, shiny, easy-to-comb baby hair with clean soothed scalp</td></tr>
  <tr><th>Texture</th><td>Smooth golden gentle foaming liquid shampoo</td></tr>
  <tr><th>Fragrance</th><td>Gentle signature Nunu baby fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>No Tears Formula, Chamomile Extract, Gentle Plant Cleansers</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia</td></tr>
  <tr><th>Manufacturer</th><td>Nunu Baby Care Products</td></tr>
  <tr><th>Age Group</th><td>Infants & Children (From Birth)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Isotonic Osmolality Tear-Free Formulation & Chamomile Scalp Protection</h2>

<h3>What problem does this solve?</h3>
<p>Nunu Baby Shampoo resolves eye sting during baby bathing, infant scalp dryness, and hair tangling difficulty.</p>

<h3>Why choose Nunu Baby Shampoo?</h3>
<p>Its pH and osmotic pressure match human lacrimal fluid (tears) perfectly, preventing mucosal cell swelling or shrinkage that causes burning sensations.</p>"""

    en_faqs = [
        ("What is Nunu Baby Shampoo - 200 ml?", "It is a gentle tear-free baby shampoo from Nunu with Chamomile extract for cleansing infant hair and scalp (200ml)."),
        ("What are the benefits of the No Tears formula and Chamomile?", "No Tears prevents eye sting while Chamomile soothes scalp and softens hair."),
        ("Does it cause eye burning during bath time?", "No, 100% tear-free formula matched to natural tear pH."),
        ("What volume is contained in this bottle?", "200ml."),
        ("How do I use it correctly?", "Wet baby's hair with warm water, apply shampoo, lather gently, massage scalp and rinse thoroughly."),
        ("Is it safe for infants from birth?", "Yes, 100% safe and gentle formula for infants from birth."),
        ("Where is Nunu Baby Shampoo manufactured?", "In Saudi Arabia by Nunu Baby Care Products."),
        ("How do I verify authenticity at Ekleel Abha?", "All Nunu products at Ekleel Abha are 100% original."),
        ("Does it make hair easy to comb?", "Yes, softens hair and prevents tangles."),
        ("What does Nunu Baby Shampoo smell like?", "Gentle signature Nunu baby fragrance."),
        ("Does it leave hair shiny and clean?", "Yes, imparts exceptional hair shine and cleanliness."),
        ("Does the 200ml bottle last long?", "Yes, lasts months of regular bath use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it soap-free, paraben-free, and alcohol-free?", "Yes, 100% free of soap, parabens, and alcohol."),
        ("Does it soothe baby scalp?", "Yes, Chamomile extract soothes scalp from dryness and irritation."),
        ("How often should I use it?", "During every baby bath."),
        ("Does it help with cradle cap care?", "Cleanses scalp gently maintaining scalp health."),
        ("Is Nunu a popular shampoo in Saudi Arabia?", "Yes, Nunu Baby Shampoo is a leading trusted brand in Saudi Arabia."),
        ("Is it suitable for all child hair types?", "Yes, suitable for fine, thick, and curly child hair."),
        ("Is the bottle recyclable?", "Yes."),
        ("Can adults with sensitive scalps use it?", "Yes, adults with ultra-sensitive scalps often prefer it."),
        ("Does it produce a soft rich lather?", "Yes, produces a gentle soft lather that cleans easily."),
        ("Does it rinse off quickly?", "Yes, rinses easily with water without sticky residue."),
        ("Is it a good newborn gift?", "Yes, practical and great newborn baby care gift."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1913",
        "sku": "EK-1913",
        "gtin": "6281053211900",
        "brand": "Nunu",
        "ar": {
            "title": "شامبو للاطفال من نونو 200 مل",
            "meta_title": "شامبو الأطفال نونو 200مل | إكليل أبها",
            "meta_description": "اشتري شامبو الأطفال من نونو (200 مل). شامبو لطيف خالي من الدموع والبارابين بخلاصة البابونج لتنظيف شعر الرضع. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["نونو", "شامبو_أطفال", "خالي_من_الدموع", "عناية_شعر_الرضيع", "إكليل_أبها"]
        },
        "en": {
            "title": "Nunu Baby Shampoo - 200 ml",
            "meta_title": "Nunu Baby Shampoo 200ml | Ekleel Abha",
            "meta_description": "Buy original Nunu Baby Shampoo (200ml). Tear-free & paraben-free Chamomile infant shampoo for gentle hair cleansing. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["nunu", "baby_shampoo", "tear_free", "infant_hair_care", "ekleel_abha"]
        }
    }


def create_product_1914():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>كبسولة بالنعناع الورقي 18 كبسولة من بيبرمينتس (Papermints Leaf Mint Capsules - 18 Capsules)</strong> كبسولات معطر الفم والبطن المبتكرة ذات الفعالية المزدوجة من بيبرمينتس البلجيكية المصممة للقضاء الفوري على رائحة الفم الكريهة من المصدر. ترتكز هذه الكبسولات الفريدة (Papermints Cool Capsule 18s) على تقنية الكبسولة الثنائية المزدوجة (Dual-Action Capsule) بنكهة النعناع الورقي المركّز وزيت زيتون النعناع الجاستري.</p>
<p>تعمل كبسولات بيبرمينتس بالنعناع الورقي بآلية مرحليتين: تذوب الطبقة الخارجية فورياً في الفم لتمنح نفساً منعشاً فواراً، بينما تنزل الكبسولة الداخلية إلى المعدة لتقضي على الروائح الصادرة من الهضم، لتترك فمك ومعدتك منعشين تماماً ونفسك فواحاً بالنعناع الصافي طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>فعالية مزدوجة الفم والمعدة (Dual-Action Mouth & Belly Freshness):</strong> تقضي على رائحة الفم والمعدة من المصدر.</li>
  <li><strong>انتعاش فورياً ومستمر لساعات طويلة:</strong> كبسولة خارجية تذوب بالفم وأخرى تذوب بالمعدة.</li>
  <li><strong>نكهة النعناع الورقي الطبيعي المركّز:</strong> تمنح نفساً فواحاً ناصع النقاء.</li>
  <li><strong>خالية 100% من السكر والسعرات الحرارية:</strong> مناسبة لمتبعي الحمية الغذائية ومرضى السكري.</li>
  <li><strong>ابتكار بلجيكي فاخر وموثوق:</strong> تصنيع بلجيكي عالي الجودة والدقة.</li>
  <li><strong>عبوة صغيرة أنيقة 18 كبسولة:</strong> حجم مدمج في الجيب مثالي للاستخدام بعد الوجبات وفي أي وقت.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كبسولة واحدة من بيبرمينتس في الفم.</li>
  <li><strong>الخطوة الثانية:</strong> دعي الكبسولة الخارجية تذوب في الفم لتمنح الانتعاش الفوري.</li>
  <li><strong>الخطوة الثالثة:</strong> ابتلعي الكبسولة الداخلية الصغيرة مع اللعاب لتنزل المعدة وتنعش الهضم (تُستعمل عند الحاجة وبعد الوجبات).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت النعناع الورقي المركّز (Peppermint Oil):</strong> يقضي على البكتيريا الفموية والمعوية المسببة للروائح.</li>
  <li><strong>غلاف الجيلاتين النباتي الصغير:</strong> يتفكك في الفم والمعدة بالتوالي لإطلاق الانتعاش المزدوج.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>مخصصة للبالغين والمراهقين (من 12 سنة فما فوق).</li>
  <li>يُحظر ابتلاع كميات كبيرة دفعة واحدة.</li>
  <li>تُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن كبسولات بيبرمينتس بالنعناع الورقي 18 كبسولة لإنعاش الفم والمعدة والقضاء على الرائحة الكريهة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيبرمينتس (Papermints)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / كبسولات بيبرمينتس المعطرة للفم والمعدة 18 كبسولة</td></tr>
  <tr><th>نوع المنتج</th><td>كبسولات مزدوجة الفعالية بالنعناع الورقي لإنعاش الفم والمعدة وقضاء الروائح (18 كبسولة)</td></tr>
  <tr><th>الحجم/الوزن</th><td>18 كبسولة</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>لا ينطبق (منتج إنعاش الفم والمعدة)</td></tr>
  <tr><th>المظهر النهائي</th><td>فم ومعدة منتعشان ونفس فواح بنقاء النعناع الورقي</td></tr>
  <tr><th>الملمس</th><td>كبسولة صلبة صغيرة تذوب في الفم وتنزل إلى المعدة</td></tr>
  <tr><th>العطر</th><td>نكهة النعناع الورقي المركّز الفواح (Leaf Mint)</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت النعناع الورقي المركّز، جيلاتين نباتي، منثول</td></tr>
  <tr><th>بلد المنشأ</th><td>بلجيكا (Belgium)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Papermints Europe</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون والمراهقون (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد تقنية الكبسولة المزدوجة بالنعناع الورقي في بيبرمينتس (Papermints)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج كبسولات بيبرمينتس مشكلة رائحة الفم الكريهة الصادرة عن الوجبات القوية (كالطعام الغني بالثوم أو البصل) أو غازات المعدة الهضمية.</p>

<h3>لماذا تنجح تقنية الكبسولة المزدوجة (Dual-Action Capsule)؟</h3>
<p>لأن العلك والمعاطرات العادية تعالج الفم فقط، بينما تنزل كبسولة بيبرمينتس للمعدة لتعادل الروائح الهضمية من المصدر.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التناول بعد الوجبات الدسمة:</strong> كبسولة واحدة بعد الأكل تحيد روائح الطعام فورياً.<br>
2. <strong>الحفظ في الجيب:</strong> العبوة المدمجة تتيح الاستخدام في أي وقت ومكان.<br>
3. <strong>الشرب الكافي للماء:</strong> يساعد في إذابة الكبسولة الداخلية بالمعدة بسرعة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كبسولات بيبرمينتس تحتوي على سكر وتضر الأسنان."<br>
<strong>الحقيقة:</strong> كبسولات بيبرمينتس خالية 100% من السكر والسعرات ومناسبة لمتبعي الحمية وصحة الأسنان.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تذوب المحفظة الخارجية السريعة Dissolvable Capsule في اللعاب الفموي، بينما تنتقل المحفظة المعوية Enteric-Coated Capsule إلى البيئة الحمضية بالمعدة لتطلق زيت النعناع المحايد للروائح.</p>"""

    faqs = [
        ("ما هي كبسولة بالنعناع الورقي 18 كبسولة من بيبرمينتس؟", "هي كبسولات مزدوجة الفعالية البلجيكية من بيبرمينتس بالنعناع الورقي لإنعاش الفم والمعدة والقضاء على الروائح (18 كبسولة)."),
        ("ما هي فوائد تقنية الكبسولة المزدوجة والنعناع الورقي؟", "تذوب الكبسولة الأولى بالفم لانتعاش فوري، وتنزل الثانية للمعدة لتحييد روائح الهضم."),
        ("هل تقضي على رائحة الفم والمعدة من المصدر؟", "نعم، مثبت سريرياً في القضاء على الروائح الصادرة من الفم والمعدة."),
        ("كم كبسولة في العبوة؟", "تحتوي العبوة على 18 كبسولة."),
        ("كيف تُستخدم بالشكل الصحيح؟", "ضعي كبسولة في الفم، دعي الطبقة الخارجية تذوب لإنعاش الفم، وايلعي الداخلية لتنعش المعدة."),
        ("هل هي خالية من السكر والسعرات الحرارية؟", "نعم، 100% خالية من السكر والسعرات الحرارية."),
        ("أين صُنعت كبسولات بيبرمينتس؟", "صُنعت في بلجيكا بواسطة Papermints Europe."),
        ("كيف أتأكد من أصالتها لدى إكليل أبها؟", "جميع منتجات بيبرمينتس لدى إكليل أبها أصلية 100%."),
        ("ما نكهة كبسولات بيبرمينتس؟", "نكهة النعناع الورقي المركّز الفواح (Leaf Mint)."),
        ("هل مناسبة لمتبعي الحمية ومرضى السكري؟", "نعم، خالية من السكر ومناسبة لمرضى السكري والحمية."),
        ("هل العبوة مناسبة للجيب والسفر؟", "نعم، عبوة أنيقة صغيرة مدمجة للجيب والتنقل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل تناسب من هم فوق 12 سنة؟", "نعم، مناسبة للبالغين والمراهقين من 12 سنة فما فوق."),
        ("كم كبسولة يمكن تناولها يومياً؟", "تُستعمل عند الحاجة بعد الوجبات (1-3 كبسولات يومياً)."),
        ("هل مفعولها سريع؟", "نعم، الانتعاش الفموي فورياً والمعدي خلال دقائق."),
        ("هل تقضي على رائحة الثوم والبصل؟", "نعم، تحيد الروائح القوية الناتجة عن الأطعمة كالثوم والبصل."),
        ("هل بيبرمينتس ماركة عالمية شهيرة؟", "نعم، Papermints علامة بلجيكية عالمية رائدة في معطرات الفم."),
        ("هل تترك الفم منعشاً طوال اليوم؟", "نعم، تمنح نفساً فواحاً ناصع النقاء."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يضر ابتلاع الكبسولة الداخلية؟", "لا، الكبسولة الداخلية مصنوعة من جيلاتين نباتي آمن ومخصص للابتلاع."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل تترك أثراً لزجاً بالفم؟", "لا، تذوب بالكامل دون لزوجة."),
        ("هل تصلح هدية عملية؟", "نعم، منتج أنيق وعملي جداً في الحقيبة والجيب."),
        ("هل يمنح ثقة كاملة أثناء التحدث؟", "نعم، يمنح ثقة تامة ونفساً معطراً ناصع النقاء."),
        ("هل لها طعم قوي جداً؟", "نكهة نعناع ورقي مركّز منعشة ولذيذة.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Papermints Leaf Mint Capsules - 18 Capsules</strong> are innovative dual-action mouth and belly breath refreshing capsules from Papermints Belgium designed to immediately eliminate bad breath from its root source. Engineered with Dual-Action Capsule technology infused with concentrated Leaf Mint oil.</p>
<p>Papermints Leaf Mint Capsules work in a two-stage mechanism: the outer shell dissolves instantly in the mouth providing immediate bursting fresh breath, while the inner micro-capsule swallows into the stomach neutralizing digestive odors, leaving your mouth and stomach thoroughly refreshed all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Dual-Action Mouth & Belly Freshness:</strong> Eliminates mouth and digestive stomach odors at the source.</li>
  <li><strong>Instant & Continuous Long-Lasting Freshness:</strong> Outer shell dissolves in mouth, inner micro-capsule in stomach.</li>
  <li><strong>Concentrated Natural Leaf Mint Flavor:</strong> Imparts a pure bursting fresh mint breath.</li>
  <li><strong>100% Sugar-Free & Calorie-Free:</strong> Suitable for dieters and diabetics.</li>
  <li><strong>Premium Trusted Belgian Innovation:</strong> Manufactured in Belgium to highest quality standards.</li>
  <li><strong>Compact Elegant 18-Capsule Pack:</strong> Pocket-sized design ideal post-meals and on-the-go.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Place one Papermints capsule into your mouth.</li>
  <li><strong>Step 2:</strong> Allow the outer shell to dissolve in the mouth for instant fresh breath.</li>
  <li><strong>Step 3:</strong> Swallow the small inner capsule with saliva into the stomach (use as needed post-meals).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Concentrated Peppermint Oil:</strong> Eliminates oral and digestive odor-causing bacteria.</li>
  <li><strong>Micro-Vegetable Gelatin Shell:</strong> Dissolves sequentially in mouth and stomach releasing dual freshness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>Designed for adults and teens (ages 12+).</li>
  <li>Do not swallow large quantities at once.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Papermints Leaf Mint 18 Capsules for dual mouth and stomach breath refreshment and odor elimination.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Papermints</td></tr>
  <tr><th>Category</th><td>Personal Care / Papermints Dual Action Mouth & Stomach Capsules 18s</td></tr>
  <tr><th>Product Type</th><td>Dual-Action Leaf Mint Mouth & Stomach Odor Neutralizing Capsules (18 capsules)</td></tr>
  <tr><th>Volume/Weight</th><td>18 capsules</td></tr>
  <tr><th>Skin/Hair Type</th><td>N/A (Oral & Stomach Breath Freshness Product)</td></tr>
  <tr><th>Finish</th><td>Refreshed mouth & stomach with pure bursting Leaf Mint breath</td></tr>
  <tr><th>Texture</th><td>Small firm dual capsule dissolving in mouth and stomach</td></tr>
  <tr><th>Fragrance</th><td>Bursting concentrated Leaf Mint flavor</td></tr>
  <tr><th>Active Ingredients</th><td>Concentrated Peppermint Oil, Vegetable Gelatin, Menthol</td></tr>
  <tr><th>Country of Origin</th><td>Belgium</td></tr>
  <tr><th>Manufacturer</th><td>Papermints Europe</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Dual-Action Dissolvable & Enteric-Coated Capsule Technology</h2>

<h3>What problem does this solve?</h3>
<p>Papermints Leaf Mint Capsules resolve bad breath caused by pungent foods (garlic, onion) and stomach digestive gases.</p>

<h3>Why choose Papermints Leaf Mint Capsules?</h3>
<p>Ordinary breath mints only treat the mouth, whereas Papermints dual capsule mechanism dissolves the outer layer in oral saliva and delivers the enteric inner capsule to the stomach to neutralize digestive volatile sulfur compounds (VSCs) at the source.</p>"""

    en_faqs = [
        ("What are Papermints Leaf Mint Capsules - 18 Capsules?", "They are Belgian dual-action mouth and stomach breath refreshing capsules with Leaf Mint oil for instant odor elimination (18 capsules)."),
        ("What are the benefits of dual-action capsule technology?", "The outer capsule dissolves in the mouth for instant freshness, while the inner capsule swallows into the stomach to neutralize digestive odors."),
        ("Do they eliminate mouth and stomach odors at the source?", "Yes, clinically proven to eliminate oral and stomach digestive odors."),
        ("How many capsules are in the pack?", "18 capsules per pocket pack."),
        ("How do I use them correctly?", "Place one capsule in mouth, let outer shell dissolve, swallow inner capsule with saliva."),
        ("Are they sugar-free and calorie-free?", "Yes, 100% sugar-free and calorie-free."),
        ("Where are Papermints manufactured?", "In Belgium by Papermints Europe."),
        ("How do I verify authenticity at Ekleel Abha?", "All Papermints products at Ekleel Abha are 100% original."),
        ("What flavor do Papermints Leaf Mint Capsules have?", "Concentrated bursting Leaf Mint flavor."),
        ("Are they safe for diabetics and dieters?", "Yes, sugar-free and safe for diabetics and keto dieters."),
        ("Is the pack pocket-friendly?", "Yes, compact sleek pack ideal for pocket and travel."),
        ("How should I store them?", "In a cool, dry place."),
        ("Are they suitable for ages 12+?", "Yes, suitable for adults and teens aged 12+."),
        ("How many capsules daily?", "Use as needed post-meals (1-3 capsules daily)."),
        ("Are the results instant?", "Yes, oral freshness is instant and stomach neutralization within minutes."),
        ("Do they neutralize garlic and onion odors?", "Yes, neutralizes strong food odors like garlic and onion effectively."),
        ("Is Papermints a famous brand?", "Yes, Papermints is a leading global Belgian brand in breath care."),
        ("Do they leave fresh breath all day?", "Yes, leaves pure bursting fresh mint breath."),
        ("Is the pack recyclable?", "Yes."),
        ("Is swallowing the inner capsule safe?", "Yes, inner micro-capsule is made of safe plant-derived gelatin designed for swallowing."),
        ("Are they available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Do they leave a sticky feel in mouth?", "No, dissolves completely clean without stickiness."),
        ("Are they a practical gift?", "Yes, sleek practical gift for handbag and pocket."),
        ("Do they give confidence during speaking?", "Yes, provides total confidence and pure fresh breath."),
        ("Do they have a pleasant taste?", "Refreshing delicious concentrated Leaf Mint taste.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1914",
        "sku": "EK-1914",
        "gtin": "5425010092251",
        "brand": "Papermints",
        "ar": {
            "title": "كبسولةبالنعناع الورقي 18 كبسوله من بيبرمينتس",
            "meta_title": "كبسولات بيبرمينتس بالنعناع الورقي 18s | إكليل أبها",
            "meta_description": "اشتري كبسولات النعناع الورقي من بيبرمينتس (18 كبسولة). كبسولات بلجيكية مزدوجة لإنعاش الفم والمعدة خالية من السكر. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["بيبرمينتس", "كبسولات_نعناع", "إنعاش_الفم_والمعدة", "خالي_من_السكر", "إكليل_أبها"]
        },
        "en": {
            "title": "Papermints Leaf Mint Capsules - 18 Capsules",
            "meta_title": "Papermints Leaf Mint Capsules 18s | Ekleel Abha",
            "meta_description": "Buy original Papermints Leaf Mint Capsules (18 capsules). Belgian dual-action mouth & belly sugar-free breath capsules. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["papermints", "leaf_mint_capsules", "dual_action_breath", "sugar_free", "ekleel_abha"]
        }
    }


def create_product_1915():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم واقي شمس بدرجة حماية 50+ من سيباميد 75 مل (Sebamed Sun Care Cream SPF 50+ - 75 ml)</strong> كريم الوقاية الطبية الفائقة من الشمس من سيباميد الألمانية المصمم لحماية وتغذية بشرة الوجه الحساسة من أضرار الأشعة فوق البنفسجية UVA و UVB. يرتكز هذا الكريم الطبي الأصيل (Sebamed Sun Care Cream SPF 50+ 75ml) على مرشحات الشمس الطبية المتقدمة (Broad-Spectrum UVA/UVB Filters)، فيتامين E المغذي، والـ pH 5.5 الحامي لحاجز البشرة الطبيعي.</p>
<p>يعمل كريم سيباميد واقي الشمس على توفير حماية فائقة بنسبة 98% ضد حروق الشمس، منع الشيخوخة المبكرة والتصبغات الناتجة عن الأشعة، وترطيب البشرة وتغذيتها دون انسداد المسام، ليترك وجهك محمياً تماماً، ناعماً، خافقاً بالصحة، وغير لامع بالدهون.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية فائقة عريضة الطيف SPF 50+ ضد UVA و UVB:</strong> تقي 98% من حروق الشمس والتلف الخلوي.</li>
  <li><strong>موازن لحموضة البشرة بـ pH 5.5 الطبيعي:</strong> يعزز حاجز الحماية الطبيعي للبشرة ضد البكتيريا والجفاف.</li>
  <li><strong>مقاوم للماء والعرق (Water & Sweat Resistant):</strong> حماية مثالية أثناء السباحة والأنشطة الخارجية.</li>
  <li><strong>مغَذٍ بفيتامين E والبروفيتامين B5:</strong> يحمي من الجذور الحرة والشيخوخة الشمسيّة المبكرة.</li>
  <li><strong>تركيبة غير دهنية وخالية من الزيوت الثقيلة (Oil-Free):</strong> لا تسد المسام ولا تسبب البثور.</li>
  <li><strong>عبوة مدمجة سعة 75 مل:</strong> حجم ممتاز للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسبة من كريم سيباميد واقي الشمس على الوجه والرقبة قبل التعرض للشمس بـ 20 دقيقة.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي الكريم بلطف بحركات دائرية حتى الامتصاص الكامل.</li>
  <li><strong>الخطوة الثالثة:</strong> كددي التطبيق كل ساعتين أو بعد السباحة والتجفيف بالفوطة (يُستعمل يومياً صباحاً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مرشحات UVA/UVB الطبية وفيتامين E:</strong> تحمي من الحروق والشيخوخة الضوئية والجذور الحرة.</li>
  <li><strong>تركيبة pH 5.5 والبروفيتامين B5:</strong> تدعم حاجز البشرة الطبيعي وتحفظ رطوبتها.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والرقبة فقط.</li>
  <li>تجنبي التلامس مع العينين.</li>
  <li>تجنبي التعرض المباشر لشمس الظهيرة الحارقة حتى مع استخدام واقي الشمس.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن كريم سيباميد واقي الشمس SPF 50+ بحجم 75 مل لحماية طبية فائقة لبشرة الوجه الحساسة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سيباميد (Sebamed)</td></tr>
  <tr><th>الفئة</th><td>العناية الطبية بالبشرة / واقيات الشمس الطبية من سيباميد بـ pH 5.5 و SPF 50+ (75ml)</td></tr>
  <tr><th>نوع المنتج</th><td>كريم واقي شمس طبي عريض الطيف SPF 50+ ومقاوم للماء بـ pH 5.5 (75ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>75 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الحساسة والشديدة الحساسية للشمس (جميع الأنواع)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه محمي تماماً من حروق الشمس والتصبغات، غير لامع بالدهون، وناعم</td></tr>
  <tr><th>الملمس</th><td>كريم خفيف سريع الامتصاص دون أثر أبيض أو دهنية</td></tr>
  <tr><th>العطر</th><td>عطر سيباميد الطبي اللطيف الناعم</td></tr>
  <tr><th>المكونات النشطة</th><td>مرشحات UVA/UVB الطبية، فيتامين E، بروفيتامين B5، تركيبة pH 5.5</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا (Germany)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Sebamed (Sebapharma Germany)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون والمراهقون (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد pH 5.5 ومرشحات UVA/UVB في سيباميد واقي الشمس (Sebamed Sun Care)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم سيباميد واقي الشمس حروق الشمس، الشيخوخة الضوئية المبكرة، التصبغات والبقع الداكنة، والتهيج الشمسي للبشرة الحساسة.</p>

<h3>لماذا تنجح تركيبة pH 5.5 الحامية؟</h3>
<p>لأن قيمة pH 5.5 تحافظ على الحموضة الطبيعية للغلاف الهيدروليبيدي للبشرة، مما يمنع جفاف البشرة وضياع رطوبتها تحت أشعة الشمس.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق قبل 20 دقيقة من التعرض للشمس:</strong> يتيح للمرشحات امتصاص الأشعة بفاعلية.<br>
2. <strong>التجديد كل ساعتين:</strong> يضمن استمرار الحماية الفائقة SPF 50+.<br>
3. <strong>ارتداء النظارات وقبعة الشمس:</strong> يكمل الحماية الكاملة من الأشعة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "واقيات الشمس SPF 50+ تترك طبقة بيضاء سميكة على الوجه."<br>
<strong>الحقيقة:</strong> كريم سيباميد مصمم بتقنية امتصاص متقدمة لا تترك طبقة بيضاء سميكة أو ملمساً لزجاً.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تمتص وتشتت المرشحات عريضة الطيف طاقة الفوتونات الضوئية بين 290-400 نانومتر، محولة الأشعة الضارة إلى طاقة حرارية غير ضارة بالجلد.</p>"""

    faqs = [
        ("ما هو كريم واقي شمس بدرجة حماية 50+ من سيباميد 75 مل؟", "هو كريم واقي شمس طبي عريض الطيف من سيباميد الألمانية بـ SPF 50+ و pH 5.5 لحماية وتغذية بشرة الوجه الحساسة (75 مل)."),
        ("ما هي فوائد SPF 50+ والـ pH 5.5 وفيتامين E؟", "يحمي SPF 50+ بنسبة 98% من حروق الشمس، يعزز pH 5.5 حاجز البشرة، ويحمي فيتامين E من الشيخوخة."),
        ("هل هو مقاوم للماء والعرق؟", "نعم، مثبت سريرياً في المقاومة للماء والعرق أثناء السباحة والرياضة."),
        ("ما حجم العبوة؟", "تأتي بعبوة سعة 75 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي الكمية قبل 20 دقيقة من الشمس، وزعي حتى الامتصاص، وجددي كل ساعتين."),
        ("هل يترك أثراً أبيض على الوجه؟", "لا، تركيبة خفيفة تمتص بسلاسة دون أثر أبيض سميك."),
        ("أين صُنع كريم سيباميد واقي الشمس؟", "صُنع في ألمانيا بواسطة Sebapharma Germany."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات سيباميد لدى إكليل أبها أصلية 100%."),
        ("هل هو خالٍ من الزيوت والبارابين؟", "نعم، تركيبة خالية من الزيوت الثقيلة والبارابين ولا تسد المسام."),
        ("ما رائحة كريم سيباميد واقي الشمس؟", "عطر سيباميد الطبي اللطيف الناعم."),
        ("هل يحمي من الشيخوخة الضوئية والتصبغات؟", "نعم، يحمي من الأشعة UVA المسببة للتجاعيد والتصبغات."),
        ("هل 75 مل تكفي لفترة جيدة؟", "نعم، تكفي لعدة أسابيع من الاستخدام الصباحي اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف بعيداً عن الحرارة المباشرة."),
        ("هل يناسب البشرة الحساسة جداً؟", "نعم، خيار أطباء الجلدية الأول للبشرة الحساسة للشمس."),
        ("كم مرة يُجدد خلال اليوم؟", "يُجدد كل ساعتين أو بعد السباحة والتجفيف."),
        ("هل يناسب الاستخدام تحت المكياج؟", "نعم، قاعدة ممتازة للحماية تحت المكياج."),
        ("هل سيباميد علامة ألمانية معتمدة؟", "نعم، Sebamed علامة ألمانية رائدة في العناية الطبية بالبشرة بـ pH 5.5."),
        ("هل يحمي من أشعة UVA و UVB معاً؟", "نعم، حماية عريضة الطيف ضوئية ضد UVA و UVB."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب المراهقين والبالغين؟", "نعم، مناسب من سن 12 سنة فما فوق."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يسبب لمعاناً دهنياً؟", "لا، يمنح مظهر غير دهني بدون لمعان زهمي."),
        ("هل يمنع احمرار البشرة بعد الشمس؟", "نعم، يهدئ البشرة ويمنع الاحمرار بحماية فائقة."),
        ("هل يصلح للسفر والبحر؟", "نعم، حجم مدمج مثالي للرحلات والبحر."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب للجميع لحماية اليومية.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Sebamed Sun Care Cream SPF 50+ - 75 ml</strong> is a premium medical sun protection cream from Sebamed Germany designed to shield and nourish sensitive facial skin against harmful UVA and UVB radiation. Formulated with Broad-Spectrum UVA/UVB Medical Filters, nourishing Vitamin E, and protective pH 5.5 formula.</p>
<p>Sebamed Sun Care Cream provides 98% superior protection against sunburn, prevents premature photo-aging and sun-induced hyperpigmentation, and hydrates skin without clogging pores, leaving your face fully protected, smooth, healthy, and shine-free.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Broad-Spectrum UVA & UVB SPF 50+ Protection:</strong> Shields 98% against sunburn and cellular UV damage.</li>
  <li><strong>pH 5.5 Skin Barrier Protection:</strong> Enhances the skin's natural hydro-lipid barrier against dryness.</li>
  <li><strong>Water & Sweat Resistant:</strong> Ideal protection during swimming and outdoor sports activities.</li>
  <li><strong>Enriched with Vitamin E & Provitamin B5:</strong> Protects from free radicals and premature photo-aging.</li>
  <li><strong>100% Oil-Free Non-Comedogenic Formula:</strong> Does not clog pores or trigger breakouts.</li>
  <li><strong>Compact 75ml Tube:</strong> Excellent volume for daily morning sun care and travel convenience.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a generous amount onto clean face and neck 20 minutes before sun exposure.</li>
  <li><strong>Step 2:</strong> Spread cream gently in circular motions until completely absorbed.</li>
  <li><strong>Step 3:</strong> Reapply every 2 hours or after swimming, sweating, and towel drying (use daily morning).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Broad-Spectrum UVA/UVB Filters & Vitamin E:</strong> Shield against burns, photo-aging, and free radicals.</li>
  <li><strong>pH 5.5 Formula & Provitamin B5:</strong> Support skin's natural barrier locking in hydration.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and neck skin application only.</li>
  <li>Avoid contact with eyes.</li>
  <li>Avoid direct intense midday sun exposure even while using sunscreen.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Sebamed Sun Care Cream SPF 50+ 75ml for superior medical facial sun protection.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Sebamed</td></tr>
  <tr><th>Category</th><td>Medical Skincare / Sebamed Medical Sunscreens pH 5.5 SPF 50+ 75ml</td></tr>
  <tr><th>Product Type</th><td>Medical Broad-Spectrum Water-Resistant SPF 50+ Sun Care Cream (75ml)</td></tr>
  <tr><th>Volume/Weight</th><td>75 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Sensitive & Sun-Sensitive Facial Skin (All Types)</td></tr>
  <tr><th>Finish</th><td>Fully sun-protected, smooth, hydrated, non-greasy & shine-free facial skin</td></tr>
  <tr><th>Texture</th><td>Lightweight fast-absorbing cream without white cast or greasiness</td></tr>
  <tr><th>Fragrance</th><td>Gentle soft medical Sebamed fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>UVA/UVB Filters, Vitamin E, Provitamin B5, pH 5.5 Formula</td></tr>
  <tr><th>Country of Origin</th><td>Germany</td></tr>
  <tr><th>Manufacturer</th><td>Sebamed (Sebapharma Germany)</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of pH 5.5 Hydro-Lipid Barrier Preservation & Broad-Spectrum Photon Absorption</h2>

<h3>What problem does this solve?</h3>
<p>Sebamed Sun Care Cream SPF 50+ resolves sunburn, premature photo-aging, hyperpigmentation, and sun irritation on sensitive skin.</p>

<h3>Why choose Sebamed Sun Care Cream?</h3>
<p>Its pH 5.5 formula preserves the acid mantle's natural protective barrier while broad-spectrum medical filters absorb UVA/UVB photon energy (290-400nm) converting harmful radiation into harmless heat.</p>"""

    en_faqs = [
        ("What is Sebamed Sun Care Cream SPF 50+ - 75 ml?", "It is a medical broad-spectrum sun cream from Sebamed Germany with SPF 50+ and pH 5.5 for sensitive facial skin protection (75ml)."),
        ("What are the benefits of SPF 50+, pH 5.5, and Vitamin E?", "SPF 50+ shields 98% against sunburn, pH 5.5 supports natural barrier, and Vitamin E prevents photo-aging."),
        ("Is it water and sweat resistant?", "Yes, clinically proven water and sweat resistant during swimming and sports."),
        ("What volume is contained in this tube?", "75ml."),
        ("How do I use it correctly?", "Apply 20 minutes before sun exposure, spread until absorbed, reapply every 2 hours."),
        ("Does it leave a white cast?", "No, lightweight formula absorbs smoothly without a thick white cast."),
        ("Where is Sebamed Sun Care manufactured?", "In Germany by Sebapharma Germany."),
        ("How do I verify authenticity at Ekleel Abha?", "All Sebamed products at Ekleel Abha are 100% original."),
        ("Is it oil-free and non-comedogenic?", "Yes, oil-free formula that does not clog pores."),
        ("What does Sebamed Sun Care smell like?", "Gentle soft medical Sebamed fragrance."),
        ("Does it protect against photo-aging and dark spots?", "Yes, broad-spectrum UVA protection prevents dark spots and wrinkles."),
        ("Does 75ml last long?", "Yes, lasts weeks of daily morning use."),
        ("How should I store it?", "In a cool, dry place away from direct heat."),
        ("Is it suitable for ultra-sensitive skin?", "Yes, dermatologist #1 choice for sun-sensitive skin."),
        ("How often should I reapply?", "Reapply every 2 hours or after swimming and towel drying."),
        ("Is it good under makeup?", "Yes, excellent protective base under makeup."),
        ("Is Sebamed a leading German brand?", "Yes, Sebamed is Germany's premier medical skincare brand with pH 5.5."),
        ("Does it protect against UVA and UVB rays?", "Yes, broad-spectrum protection against UVA and UVB rays."),
        ("Is the tube recyclable?", "Yes."),
        ("Is it suitable for teens and adults?", "Yes, ages 12+."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it cause greasy shine?", "No, gives a smooth non-greasy shine-free finish."),
        ("Does it prevent sun redness?", "Yes, calms skin and prevents sun-induced redness."),
        ("Is it travel and beach friendly?", "Yes, compact tub ideal for trips and beach days."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1915",
        "sku": "EK-1915",
        "gtin": "4103040899958",
        "brand": "Sebamed",
        "ar": {
            "title": "كريم واقي شمس بدرجة حماية 50+  من سيباميد 75 مل",
            "meta_title": "واقي شمس سيباميد SPF 50+ 75مل | إكليل أبها",
            "meta_description": "اشتري كريم واقي شمس سيباميد SPF 50+ (75 مل). كريم طبي مقاوم للماء بـ pH 5.5 وحماية عريضة الطيف للوجه. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["سيباميد", "واقي_شمس_سيباميد", "SPF50", "مقاوم_للماء", "إكليل_أبها"]
        },
        "en": {
            "title": "Sebamed Sun Care Cream SPF 50+ - 75 ml",
            "meta_title": "Sebamed Sun Care Cream SPF 50+ 75ml | Ekleel Abha",
            "meta_description": "Buy original Sebamed Sun Care Cream SPF 50+ (75ml). Medical water-resistant pH 5.5 broad-spectrum sunscreen. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["sebamed", "sun_care_cream", "spf50_sunscreen", "water_resistant", "ekleel_abha"]
        }
    }


def create_product_1916():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مرطب شفاه الطفل من سيباميد (Sebamed Baby Lip Balm)</strong> مرطب الشفاه الطبي الفاخر للأطفال والرضع من سيباميد الألمانية المصمم خصيصاً لحماية وترطيب شفاه الرضع والأطفال الحساسة والرقيقة. يرتكز هذا المرطب الطبي (Sebamed Baby Lip Balm) على الزيوت النباتية الطبيعية كزيت الجوجوبا (Jojoba Oil)، شمع النحل النقي (Beeswax)، خلاصة البابونج، وفيتامين E.</p>
<p>يعمل مرطب شفاه سيباميد للأطفال على منع تشقق وجفاف الشفاه الناتج عن اللعاب والطقس البارد، توفير ترطيب وحماية مستمرة لـ 24 ساعة، وتهدئة الشفاه المتهيجة والجافة، ليترك شفاه طفلك ناعمة، مرطبة، محمية، وخالية تماماً من التشقق والالتهاب.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وقائي فائق لشفاه الأطفال والرضع:</strong> يمنع الجفاف والتشقق الناتج عن اللعاب والبرد.</li>
  <li><strong>مدعم بزيوت الجوجوبا وشمع النحل وفيتامين E:</strong> يغذي الشفاه ويشكل طبقة حماية طبيعية.</li>
  <li><strong>تهدئة الشفاه المتهيجة بخلاصة البابونج:</strong> يهدئ الاحمرار والالتهاب الجلدي في الشفاه.</li>
  <li><strong>تركيبة آمنة 100% خالية من البارابين والروائح والصبغات:</strong> آمنة للرضع من الولادة حتى عند اللعق.</li>
  <li><strong>قلم اصبع سهل الاستخدام (Stick):</strong> تطبيق مريح وسريع لشفاه الطفل.</li>
  <li><strong>عبوة مدمجة للاستخدام اليومي:</strong> حجم صغير أنيق ومريح في الحقيبة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> مرري اصبع مرطب شفاه سيباميد برفق على شفاه الطفل.</li>
  <li><strong>الخطوة الثانية:</strong> كرري التطبيق 2-3 مرات يومياً أو عند الحاجة (خاصة قبل الخروج في الهواء البارد وبعد الوجبات).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الجوجوبا وشمع النحل:</strong> يغذيان الشفاه ويشكلان عازلاً واقياً يمنع تبخر الرطوبة.</li>
  <li><strong>خلاصة البابونج وفيتامين E:</strong> يهدئان التهيجات الجلدية ويحميان من الأكسدة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على الشفاه فقط.</li>
  <li>يُحفظ بعيداً عن الحرارة المباشرة والشمس لمنع الذوبان.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال دون إشراف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل أم تبحث عن مرطب شفاه سيباميد للأطفال لحماية وترطيب شفاه طفلها الرقيقة بكل أمان.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سيباميد (Sebamed)</td></tr>
  <tr><th>الفئة</th><td>العناية بالأطفال / مرطبات شفاه سيباميد الطبية للأطفال والرضع</td></tr>
  <tr><th>نوع المنتج</th><td>مرطب شفاه طبي للأطفال بالجوجوبا وشمع النحل والبابونج (قلم اصبع)</td></tr>
  <tr><th>الحجم/الوزن</th><td>قلم اصبع سعة القياسية (حوالي 4.8 جم)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>شفاه الأطفال والرضع الحساسة والجافة (من الولادة)</td></tr>
  <tr><th>المظهر النهائي</th><td>شفاه طفل ناعمة، مرطبة، محمية وخالية من التشقق والالتهاب</td></tr>
  <tr><th>الملمس</th><td>بلسم بلسمي ناعم ينزلق برفق دون لزوجة</td></tr>
  <tr><th>العطر</th><td>خالٍ من العطور والروائح (Fragrance-Free)</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت الجوجوبا، شمع النحل، خلاصة البابونج، فيتامين E</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا (Germany)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Sebamed (Sebapharma Germany)</td></tr>
  <tr><th>الفئة العمرية</th><td>الرضع والأطفال (من الولادة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت الجوجوبا وشمع النحل في مرطب شفاه سيباميد للأطفال</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مرطب شفاه سيباميد للأطفال مشكلة تشقق الشفاه، احمرار وتصلب جلد الشفتين الناتج عن اللعاب الدائم والطقس البارد.</p>

<h3>لماذا تنجح تركيبة الجوجوبا وشمع النحل؟</h3>
<p>لأن زيت الجوجوبا يطابق الشحوم الجلدية الطبيعية (Sebum Mimetics) فيغذي الشفاه عمقاً، بينما يشكل شمع النحل عازلاً يمنع تلامس اللعاب مع الجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق قبل الخروج في البرد:</strong> يحمي شفاه الطفل من جفاف الهواء الشتوي.<br>
2. <strong>التطبيق بعد تنظيف الفم بعد الوجبات:</strong> يمنع تهيج اللعاب وبقايا الطعام.<br>
3. <strong>الاستخدام المنتظم 2-3 مرات يومياً:</strong> يضمن حماية مستمرة طوال اليوم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مرطبات الشفاه غير آمنة للرضع إذا لعقها الطفل."<br>
<strong>الحقيقة:</strong> مرطب سيباميد مصنع بمكونات طبيعية طعامية آمنة 100% للرضع والأطفال حتى عند اللعق.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تمنع الإسترات الشمعية (Wax Esters) لشمع النحل نفاذ الإنزيمات الهاضمة في اللعاب (كالأميليز) لخلايا الشفاه الرقيقة.</p>"""

    faqs = [
        ("ما هو مرطب شفاه الطفل من سيباميد؟", "هو مرطب شفاه طبي للأطفال من سيباميد الألمانية بالجوجوبا وشمع النحل والبابونج لحماية وترطيب شفاه الرضع (اصبع)."),
        ("ما هي فوائد الجوجوبا وشمع النحل والبابونج؟", "يغذي زيت الجوجوبا الشفاه، يشكل شمع النحل عازلاً واقياً، ويهدئ البابونج الاحمرار والتهيج."),
        ("هل يمنع تشقق الشفاه الناتج عن اللعاب والبرد؟", "نعم، يشكل عازلاً طبيعياً يمنع تأثير اللعاب والطقس البارد على الشفاه."),
        ("ما نوع العبوة؟", "تأتي بعبوة قلم اصبع سهلة الاستخدام (Stick)."),
        ("كيف يُستخدم بالشكل الصحيح؟", "مرري الاصبع برفق على شفاه الطفل 2-3 مرات يومياً أو عند الحاجة."),
        ("هل هو آمن للرضع من الولادة حتى عند اللعق؟", "نعم، تركيبة طبيعية 100% خالية من البارابين والصبغات وآمنة للرضع عند اللعق."),
        ("أين صُنع مرطب شفاه سيباميد للأطفال؟", "صُنع في ألمانيا بواسطة Sebapharma Germany."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات سيباميد لدى إكليل أبها أصلية 100%."),
        ("هل هو خالٍ من العطور والصبغات؟", "نعم، 100% خالٍ من العطور والروائح والصبغات."),
        ("ما رائحة مرطب شفاه سيباميد؟", "خالٍ من العطور والروائح (Fragrance-Free)."),
        ("هل يمنح ترطيباً يمتد 24 ساعة؟", "نعم، يحافظ على ترطيب الشفاه وحمايتها طوال اليوم."),
        ("هل العبوة مدمجة ومناسبة للحقيبة؟", "نعم، حجم قلم أنيق ومريح في الحقيبة والجيب."),
        ("كيف أحتفظ به؟", "في مكان بارد بعيداً عن الشمس المباشرة لمنع الذوبان."),
        ("هل يناسب الأطفال والبالغين ذوي الشفاه الحساسة؟", "نعم، ممتاز للأطفال والبالغين ذوي الشفاه شديدة الحساسية."),
        ("كم مرة يومياً؟", "2-3 مرات يومياً أو عند الحاجة."),
        ("هل يترك أثراً لزجاً على شفاه الطفل؟", "لا، ينزلق بنعومة دون لزوجة زهمية."),
        ("هل سيباميد علامة ألمانية معتمدة لمنتجات الأطفال؟", "نعم، Sebamed Baby علامة ألمانية رائدة وموصى بها من أطباء الأطفال عالمياً."),
        ("هل يحمي من جفاف الشتاء؟", "نعم، حماية ممتازة ضد جفاف الهواء البارد في الشتاء."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل ينعم الشفاه المتصلبة؟", "نعم، تلاحظ النعومة والراحة من الاستخدام الأول."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الأطفال الذين يمارسون الأنشطة الخارجية؟", "نعم، يقي الشفاه من الهواء والشمس أثناء اللعب الخارجي."),
        ("هل يصلح هدية لطيفة لمولود جديد؟", "نعم، هدية عملية جداً ومفيدة في العناية بالمولود."),
        ("هل يمنع تهيج اللعاب أثناء التسنين؟", "نعم، يحمي الشفاه والمنطقة المحيطة من تهيج اللعاب خلال التسنين."),
        ("هل يمتص بسلاسة دون طعم مزعج؟", "نعم، خالٍ من الطعم المزعج ويمتص بسلاسة.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Sebamed Baby Lip Balm</strong> is a premium medical lip balm for infants and children from Sebamed Germany designed to protect and hydrate delicate baby lips. Formulated with natural botanical oils like Jojoba Oil, pure Beeswax, soothing Chamomile extract, and Vitamin E.</p>
<p>Sebamed Baby Lip Balm prevents lip chapping and dryness caused by continuous drooling and cold weather, provides continuous 24-hour hydration and protection, and calms dry irritated lips, leaving your baby's lips soft, hydrated, protected, and free of chapping.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Superior Protective Hydration for Baby Lips:</strong> Prevents dryness and chapping from drooling and cold weather.</li>
  <li><strong>Enriched with Jojoba Oil, Beeswax & Vitamin E:</strong> Nourishes lips and forms a natural protective layer.</li>
  <li><strong>Soothing Irritated Lips with Chamomile:</strong> Calms redness and skin inflammation on lips.</li>
  <li><strong>100% Safe Formula Free of Parabens, Fragrance & Dyes:</strong> Safe for infants from birth even if licked.</li>
  <li><strong>Easy-to-Use Stick Format:</strong> Convenient and quick application onto baby lips.</li>
  <li><strong>Compact Pack for Daily Care:</strong> Small sleek size convenient for handbag and pocket.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Gently glide the Sebamed Baby Lip Balm stick over baby's lips.</li>
  <li><strong>Step 2:</strong> Reapply 2-3 times daily or as needed (especially before outdoor cold air exposure and post-meals).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Jojoba Oil & Beeswax:</strong> Nourish lips and form a protective barrier preventing moisture evaporation.</li>
  <li><strong>Chamomile Extract & Vitamin E:</strong> Soothe skin irritation and protect against oxidation.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical lip application only.</li>
  <li>Store away from direct heat and sunlight to prevent melting.</li>
  <li>Keep out of reach of children without adult supervision.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every mother seeking Sebamed Baby Lip Balm for safe protection and hydration of their baby's delicate lips.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Sebamed</td></tr>
  <tr><th>Category</th><td>Baby Care / Sebamed Medical Baby Lip Balms & Protection Sticks</td></tr>
  <tr><th>Product Type</th><td>Medical Jojoba & Beeswax Chamomile Infant & Child Lip Balm Stick</td></tr>
  <tr><th>Volume/Weight</th><td>Standard Stick Size (approx 4.8g)</td></tr>
  <tr><th>Skin/Hair Type</th><td>Sensitive Dry Infant & Child Lips (From Birth)</td></tr>
  <tr><th>Finish</th><td>Soft, hydrated, protected, chap-free baby lips</td></tr>
  <tr><th>Texture</th><td>Smooth gentle balm stick gliding without stickiness</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-Free</td></tr>
  <tr><th>Active Ingredients</th><td>Jojoba Oil, Beeswax, Chamomile Extract, Vitamin E</td></tr>
  <tr><th>Country of Origin</th><td>Germany</td></tr>
  <tr><th>Manufacturer</th><td>Sebamed (Sebapharma Germany)</td></tr>
  <tr><th>Age Group</th><td>Infants & Children (From Birth)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Beeswax Esters Drool Barrier & Jojoba Sebum-Mimetics</h2>

<h3>What problem does this solve?</h3>
<p>Sebamed Baby Lip Balm resolves lip chapping, redness, and inflammation caused by continuous infant drooling and winter cold.</p>

<h3>Why choose Sebamed Baby Lip Balm?</h3>
<p>Jojoba Oil mimics natural skin sebum esters feeding deep lip layers while Beeswax forms an impermeable barrier preventing salivary digestive enzymes (amylase) from penetrating delicate lip keratin layers.</p>"""

    en_faqs = [
        ("What is Sebamed Baby Lip Balm?", "It is a medical baby lip balm from Sebamed Germany with Jojoba Oil, Beeswax, and Chamomile for protecting infant lips (stick)."),
        ("What are the benefits of Jojoba Oil, Beeswax, and Chamomile?", "Jojoba Oil nourishes, Beeswax forms a protective barrier, and Chamomile soothes redness."),
        ("Does it prevent lip chapping from drooling and cold weather?", "Yes, forms a natural barrier preventing saliva and cold air from chapping lips."),
        ("What format is this balm?", "Easy-to-use twist stick format."),
        ("How do I use it correctly?", "Glide gently over baby's lips 2-3 times daily or as needed."),
        ("Is it safe for infants from birth even if licked?", "Yes, 100% safe natural food-grade formula safe for infants when licked."),
        ("Where is Sebamed Baby Lip Balm manufactured?", "In Germany by Sebapharma Germany."),
        ("How do I verify authenticity at Ekleel Abha?", "All Sebamed products at Ekleel Abha are 100% original."),
        ("Is it fragrance-free and dye-free?", "Yes, 100% fragrance-free and dye-free."),
        ("What does Sebamed Baby Lip Balm smell like?", "Completely fragrance-free."),
        ("Does it provide 24-hour lip hydration?", "Yes, keeps lips hydrated and protected all day long."),
        ("Is the stick compact for handbag?", "Yes, sleek compact stick perfect for handbag and pocket."),
        ("How should I store it?", "Store in a cool place away from direct sunlight to prevent melting."),
        ("Is it suitable for adults with sensitive lips?", "Yes, excellent for adults with ultra-sensitive chapped lips."),
        ("How many times daily?", "2-3 times daily or as needed."),
        ("Does it leave a sticky feel on baby lips?", "No, glides smoothly without sticky residue."),
        ("Is Sebamed a trusted German baby brand?", "Yes, Sebamed Baby is a globally trusted pediatrician-recommended German brand."),
        ("Does it protect against winter cold dryness?", "Yes, superior barrier protection against harsh winter cold air."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it soften dry hardened lips?", "Yes, softness and comfort are noticeable from first application."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for outdoor active kids?", "Yes, shields lips from wind and sun during outdoor play."),
        ("Is it a nice newborn baby gift?", "Yes, practical and thoughtful newborn care gift."),
        ("Does it prevent teething drool lip irritation?", "Yes, protects lips from drool irritation during teething."),
        ("Does it absorb smoothly without unpleasant taste?", "Yes, completely free of unpleasant taste and absorbs smoothly.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1916",
        "sku": "EK-1916",
        "gtin": "4103040901811",
        "brand": "Sebamed",
        "ar": {
            "title": "مرطب شفاه الطفل من سيباميد",
            "meta_title": "مرطب شفاه الأطفال سيباميد | إكليل أبها",
            "meta_description": "اشتري مرطب شفاه الطفل من سيباميد. مرطب طبي بالجوجوبا وشمع النحل والبابونج لحماية شفاه الرضع من التشقق. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["سيباميد", "مرطب_شفاه_أطفال", "حماية_شفاه_الرضيع", "شمع_النحل", "إكليل_أبها"]
        },
        "en": {
            "title": "Sebamed Baby Lip Balm",
            "meta_title": "Sebamed Baby Lip Balm | Ekleel Abha",
            "meta_description": "Buy original Sebamed Baby Lip Balm. Medical Jojoba & Beeswax infant lip stick for preventing chapping. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["sebamed", "baby_lip_balm", "infant_lip_stick", "beeswax_lip_care", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 40 builders complete")
