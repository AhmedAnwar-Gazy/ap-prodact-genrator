import json, os
from build_batch24 import build_garnier_hair_food

def create_product_1831():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>زيت الجليسرين الطبيعي النقي لترطيب البشرة والجسم - 185 مل (Natural Glycerin Oil, 185 ml)</strong> المستحضر الطبيعي النقي الأقوى عالمياً لعلاج الجفاف شديد الخشونة، تنعيم الأكواع والركب، وتوحيد ملمس الجلد. يرتكز هذا الزيت النقي على الجليسرين النباتي 100% (Pure Plant-Derived Glycerin)، الخالي تماماً من المواد الكيميائية والعطور الاصطناعية والبارابين.</p>
<p>يمتاز زيت الجليسرين الطبيعي بخصائص جاذبة للرطوبة (Humectant)، حيث يحبس الماء داخل خلايا الجلد، يرمم التشققات، ويمنحكِ بشرة ملساء طرية ومفعمة بالنضارة والصحة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>جليسرين نباتي نقي 100%:</strong> ترطيب وتغذية مكثفة لعلاج الجفاف والخشونة.</li>
  <li><strong>ترميم تشققات الجلد والأكواع والركب:</strong> يرطب الأماكن شديدة الجفاف وينعم الكعبين المجهدة.</li>
  <li><strong>جاذب فعال لرطوبة الهواء والجلد:</strong> يمنع التبخر الجلدي (TEWL) ويحفظ نضارة البشرة.</li>
  <li><strong>خالي من الكحول والعطور والبارابين:</strong> مستحضر نقي ومجرب يناسب الوجه والجسم واليدين.</li>
  <li><strong>تخليط ممتاز مع الزيوت الطبيعية:</strong> يمكن مزجه مع زيت اللوز أو اللافندر لروتين عناية فاخر.</li>
  <li><strong>عبوة وافرة سعة 185 مل:</strong> حجم ممتاز ومناسب للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> وضعي الزيت فورياً بعد الاستحمام على بشرة رطبة لحبس الماء.</li>
  <li><strong>الخطوة الثانية (التدليك):</strong> دلكي بحركات دائرية خفيفة على الأكواع، الركب، اليدين، أو كامل الجسم.</li>
  <li><strong>الخطوة الثالثة (المزج):</strong> يمكن إضافة قطرات من الزيت لكريم الجسم المفضل لترطيب مضاعف.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>جليسرين نباتي طبيعي نقي 100% (Pure Plant Glycerin):</strong> يحبس الماء ويطري الجلد الخشن.</li>
</ul>

<h2>تحذيرات وااحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على البشرة فقط.</li>
  <li>تجنبي ملامسة الزيت المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن الشمس.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من تشققات الجلد، خشونة الأكواع والركب، وتفتش عن زيت جليسرين طبيعي نقي 100%.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>عام / صيدلية إكليل أبها (Natural Glycerin)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / زيوت الجليسرين الطبيعية النقية لترطيب الجسم</td></tr>
  <tr><th>نوع المنتج</th><td>زيت جليسرين نباتي طبيعي نقي 100% لترطيب الجلد (185ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>185 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة شديدة الجفاف، المتقشرة، والخشونة</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة كالحرير، مرطبة عميقاً، خالية من التشققات والقشور</td></tr>
  <tr><th>الملمس</th><td>زيت سائل شفاف عالي الكثافة ينفذ بالتدليك</td></tr>
  <tr><th>العطر</th><td>عديم الرائحة (Unscented)</td></tr>
  <tr><th>المكونات النشطة</th><td>100% جليسرين نباتي نقي (Pure Vegetable Glycerin)</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الهند</td></tr>
  <tr><th>الشركة المصنعة</th><td>Natural Oils Labs</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الجليسرين النباتي النقي (Natural Glycerin Oil)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج زيت الجليسرين الطبيعي مشكلة تشققات الكعبين والأكواع، الجفاف الشديد، وفقدان مرونة الجلد.</p>

<h3>لماذا تنجح خاصية الجليسرين النقي؟</h3>
<p>لأن الجليسرين يمتلك قدرة هيدروفيليّة عالية تجذب جزيئات الماء من الجو والطبقات العميقة لتغليف البشرة لـ 24 ساعة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على جلد رطب:</strong> استعملي الجليسرين بعد الاستحمام مباشرة وقبل تجفيف البشرة تماماً.<br>
2. <strong>ارتداء جوارب قطنية:</strong> دلكي الكعبين بالجليسرين وارتدي جوارب قطنية قبل النوم.<br>
3. <strong>المزج مع الزيوت العطرية:</strong> امزجي قطرات منه مع زيت اللوز الحلو لمعالجة التصبغات.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "زيت الجليسرين النقي يسبب اسمرار البشرة عند التعرض للشمس."<br>
<strong>الحقيقة:</strong> الجليسرين مرطب نقي لا يسبب اسمراراً عند استخدامه بشكل صحيح وتجنب الشمس المباشرة الحارقة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتخلل جزيئات الجليسرين بين الخلايا القرنية، مما يملأ الفراغات الناتجة عن الجفاف ويمنع تكسر الألياف المرنة.</p>"""

    faqs = [
        ("ما هو زيت الجليسرين الطبيعي النقي 185 مل؟", "هو زيت جليسرين نباتي طبيعي نقي 100% مخصص لترطيب وتنعيم البشرة شديدة الجفاف وعلاج التشققات سعة 185 مل."),
        ("ما هي فوائد الجليسرين النباتي النقي 100%؟", "يجذب الرطوبة، يحبس الماء بالجلد، يرمم التشققات، وينعم الأكواع والركب المجهدة."),
        ("هل هو خالي من العطور والكيماويات والبارابين؟", "نعم، زيت طبيعي نقي 100% خالي من العطور والملونات والبارابين."),
        ("ما حجم العبوة؟", "تأتي بحجم 185 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي قطرات على البشرة الرطبة بعد الاستحمام ودلكي برفق حتى الامتصاص أو امزجيه مع كريمكِ المفضّل."),
        ("هل يرمم تشققات الكعبين والأكواع؟", "نعم، ممتاز جداً لتنعيم وترطيب الكعبين والأكواع والركب شديدة الخشونة."),
        ("ما هو بلد صنع زيت الجليسرين؟", "صُنع بفخر وفق أعلى معايير نقاء الزيوت النباتية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع الزيوت لدى إكليل أبها أصلية 100% ومستوردة من الموردين المعتمدين."),
        ("هل يترك أثراً دهنياً ثقيلاً؟", "ينفذ بالبشرة بالتدليك على جلد رطب ليعطي ملمساً حريرياً طرياً."),
        ("ما هي رائحة زيت الجليسرين؟", "عديم الرائحة تماماً (Unscented)."),
        ("هل يناسب جميع أنواع البشرة؟", "مناسب للبشرة الجافة، شديدة الجفاف، والحساسة."),
        ("هل يمكن مزجه مع زيوت أخرى؟", "نعم، ممتاز لمزجه مع زيت اللوز الحلو، اللافندر، أو زبدة الشيا."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل العبوة 185 مل اقتصادية؟", "نعم، عبوة وافرة تكفي لاستخدامات متعددة لأشهر طويلة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة أنيقة بقطارة أو غطاء محكم يمنع التسرب."),
        ("هل يناسب حماية البشرة في الشتاء؟", "نعم، الحماية الأولى الفعالة ضد برودة وجفاف الشتاء."),
        ("هل يناسب جميع أفراد العائلة؟", "نعم، آمن وممتاز للأطفال والبالغين من سن 3 سنوات."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُفضل استخدامه 1 إلى 2 مرة يومياً بعد الغسيل."),
        ("هل يمنع القشور والتطير؟", "نعم، يقضي على القشور والتطير ويرمم الجلد."),
        ("هل يساعد في ترطيب الأيدي الجافة؟", "نعم، ممتاز جداً لتنعيم الأيدي شديدة الجفاف."),
        ("هل يمكن وضعه على الوجه؟", "يمكن وضع قطرات خفيفة جداً لترطيب شفتين أو وجنتين جافتين."),
        ("هل يناسب الكبار والأطفال؟", "نعم، يناسب جميع الفئات العمرية."),
        ("هل يمنح ملمساً مخملياً؟", "نعم، يترك الجلد طرياً ومخملياً طوال اليوم."),
        ("هل هو الزيت الأكثر طلباً للترطيب النقي؟", "نعم، زيت الجليسرين النقي الخيار الأكثر ثقة للترطيب المكثف."),
        ("هل يتوفر بقيمة ممتازة لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Natural Glycerin Oil, 185 ml</strong> is the world's #1 100% pure vegetable-derived glycerin oil engineered to treat severe skin dryness, smooth rough heels, elbows, and knees, and restore skin suppleness. Free from artificial perfumes, parabens, and chemicals.</p>
<p>Natural Glycerin Oil features powerful humectant properties, drawing atmospheric moisture into dermal cells, repairing cracked skin, and leaving your body touchably soft, smooth, and healthy all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Pure Plant Glycerin:</strong> Delivers intensive moisture to treat skin dryness and roughness.</li>
  <li><strong>Repairs Cracked Heels, Elbows & Knees:</strong> Softens extremely dry patches and cracked heels effectively.</li>
  <li><strong>Powerful Atmospheric Moisture Magnet:</strong> Prevents transepidermal water loss (TEWL), sealing in hydration.</li>
  <li><strong>100% Unscented, Alcohol & Paraben Free:</strong> Pure gentle formula suitable for face, hands, and body.</li>
  <li><strong>Ideal for DIY Skincare Blends:</strong> Blends seamlessly with almond oil, lavender oil, or body lotions.</li>
  <li><strong>Generous 185ml Bottle:</strong> High-value bottle size for daily continuous body hydration routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Apply immediately after showering onto damp skin to lock in water.</li>
  <li><strong>Step 2 (Massage):</strong> Massage in gentle circular motions onto elbows, knees, heels, or full body.</li>
  <li><strong>Step 3 (Blend):</strong> Alternatively, mix a few drops with your favorite body lotion for double hydration.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>100% Pure Vegetable Glycerin:</strong> Draws moisture into skin layers and heals rough cracked skin.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical skin moisturizing application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from direct heat.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with extremely dry, cracked heels, rough elbows, or flaking skin seeking 100% pure natural plant glycerin oil.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Generic / Ekleel Abha Pharmacy</td></tr>
  <tr><th>Category</th><td>Skincare / Pure Natural Glycerin Body Oils</td></tr>
  <tr><th>Product Type</th><td>100% Pure Plant Glycerin Oil (185ml)</td></tr>
  <tr><th>Volume/Weight</th><td>185 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Extremely Dry, Cracked & Rough Skin</td></tr>
  <tr><th>Finish</th><td>Touchably soft, supple, 24h hydrated & flake-free skin</td></tr>
  <tr><th>Texture</th><td>Viscous clear liquid absorbing during massage</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-Free (Unscented)</td></tr>
  <tr><th>Active Ingredients</th><td>100% Pure Vegetable Glycerin</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / India</td></tr>
  <tr><th>Manufacturer</th><td>Natural Oils Labs</td></tr>
  <tr><th>Age Group</th><td>All Ages (3+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Pure Vegetable Glycerin & Atmospheric Moisture Attraction</h2>

<h3>What problem does this solve?</h3>
<p>Natural Glycerin Oil resolves cracked heels, rough elbows, severe skin flaking, and lost dermal elasticity.</p>

<h3>Why choose Pure Glycerin Oil?</h3>
<p>Pure vegetable glycerin is a powerful humectant that attracts and binds water molecules into intercellular dermal matrix layers.</p>"""

    en_faqs = [
        ("What is Natural Glycerin Oil 185 ml?", "It is a 100% pure vegetable-derived glycerin oil formulated to hydrate extremely dry skin and heal cracked heels."),
        ("What are the benefits of 100% pure plant glycerin?", "Attracts atmospheric moisture, heals skin cracks, and softens rough heels and knees."),
        ("Is it fragrance-free, alcohol-free, and paraben-free?", "Yes, 100% pure plant oil completely free of synthetic perfumes, dyes, and parabens."),
        ("What volume is contained in this bottle?", "It comes in a 185ml bottle."),
        ("How do I apply it correctly?", "Apply to damp skin immediately after showering and massage gently until absorbed, or mix with body cream."),
        ("Does it heal cracked heels and rough elbows?", "Yes, highly effective at repairing cracked heels, dry elbows, and rough knees."),
        ("Where is Natural Glycerin Oil manufactured?", "Produced following strict plant-oil purity and safety standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All natural oils at Ekleel Abha are 100% original from certified suppliers."),
        ("Does it leave a heavy greasy film?", "Absorbs into damp skin during massage, leaving a silky soft finish."),
        ("What scent does it have?", "It is completely fragrance-free (unscented)."),
        ("Is it suitable for all skin types?", "Ideal for dry, extremely dry, cracked, and sensitive skin types."),
        ("Can it be blended with other natural oils?", "Yes, blends excellently with sweet almond oil, lavender oil, or Shea butter."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat and sunlight."),
        ("Is the 185ml bottle economical?", "Yes, generous volume lasts through months of daily body hydration."),
        ("Is the bottle securely sealed?", "Yes, comes in a sleek bottle with a secure leak-proof cap."),
        ("Is it great for winter cold dryness?", "Yes, the #1 effective natural shield against harsh winter cold dryness."),
        ("Is it safe for family use?", "Yes, safe for adults and children aged 3+."),
        ("How many times daily should I use it?", "Use 1 to 2 times daily after showering or washing."),
        ("Does it stop skin flaking?", "Yes, completely clears dry flaking patches and rough skin tightness."),
        ("Is it effective for dry cracked hands?", "Yes, highly effective at softening dry cracked hands."),
        ("Can a light drop be applied on facial skin?", "A very light drop can be applied on dry lips or dry cheeks."),
        ("Is it suitable for all age groups?", "Yes, suitable for all age groups."),
        ("Does it leave skin touchably soft?", "Yes, leaves skin supple and soft all day long."),
        ("Is it a top-selling pure moisturizer?", "Yes, the most trusted choice for 100% pure deep skin hydration."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1831",
        "sku": "EK-1831",
        "gtin": "6287016070096",
        "category": "العناية بالبشرة / زيوت الجليسرين الطبيعية النقية لترطيب الجسم",
        "brand": "Generic Natural Glycerin",
        "ar": {
            "title": "زيت الجليسرين الطبيعي النقي لترطيب البشرة والجسم - 185 مل",
            "meta_title": "زيت الجليسرين الطبيعي 185مل | صيدلية إكليل أبها",
            "meta_description": "اشتري زيت الجليسرين الطبيعي النقي لترطيب البشرة والجسم (185 مل). جليسرين نباتي نقي 100% للتنعيم والتشققات. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["جليسرين", "زيت_الجليسرين", "ترطيب_البشرة", "علاج_التشققات", "إكليل_أبها"]
        },
        "en": {
            "title": "Natural Glycerin Oil, 185 ml",
            "meta_title": "Natural Glycerin Oil 185ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Natural Glycerin Oil (185 ml). 100% pure vegetable glycerin for deep body moisturizing & cracked skin. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["glycerin_oil", "natural_glycerin", "body_moisturizer", "cracked_skin", "ekleel_abha"]
        },
        "schema": {
            "brand": "Generic Natural Glycerin",
            "category": "Skincare / Body Oil",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "natural-glycerin-oil-185ml.webp",
            "alt": "Natural Glycerin Oil 185 ml",
            "title": "Natural Glycerin Oil 185 ml"
        }
    }

def create_product_1833():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول الجسم سحر الجمال مع لوفة من لوكس - 250 مل (Lux Magical Beauty Body Wash with Loofah - 250ml)</strong> غسول الجسم الاستحمام الفاخر الأكثر سحراً وعطراً عالمياً لإضفاء نعومة حريرية وعطر مسك الفانيليا والزهور النادرة الذي يدوم على جسمكِ لـ 24 ساعة متواصلة. يرتكز هذا الغسول الفاخر من لوكس (Lux Magical Beauty) على فورمولا الزيوت العطرية النقية وزهرة الأوركيد السوداء (Black Orchid Oil) مع لوفة استحمام مهداة مرفقة بالعبوة.</p>
<p>يمتاز غسول لوكس برغوة غنية مخملية تطهر بشرة الجسم برفق، تمنع جفاف الجلد، وتغلفكِ بنفحات عطريّة ساحرة تعزز إحساسكِ بالأنوثة، الفخامة، والنظافة المطلقة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عطر زهرة الأوركيد المسكي الساحر لـ 24 ساعة:</strong> يترك عبقاً عطرياً زكياً يثبت على جسمكِ طوال اليوم.</li>
  <li><strong>مرفق بـ لوفة استحمام فاخرة:</strong> تساعد في تقشير ورغوة الجسم بسلاسة وتوليد رغوة كثيفة.</li>
  <li><strong>رغوة غنية مخملية تطهر برفق:</strong> تنظف المسام دون تجريف الرطوبة الطبيعية بالجلد.</li>
  <li><strong>مدعم بـ زيوت عطرية مغذية:</strong> يطري بشرة الجسم ويمنحها ملمساً ناعماً كالحرير.</li>
  <li><strong>عطر من تصميم أكبر خبراء العطور عالمياً:</strong> مزيج نفيح الأوركيد السوداء والمسك الفاخر.</li>
  <li><strong>عبوة سعة 250 مل:</strong> حجم ممتازة ومناسبة للاستحمام اليومي الممتع.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل):</strong> بلي جسمكِ واللوفة المرفقة بالماء الفاتر أثناء الشاور.</li>
  <li><strong>الخطوة الثانية (الرغوة):</strong> اسكبي كمية مناسبة من غسول لوكس سحر الجمال على اللوفة وافركي لتوليد رغوة عطرية غنية.</li>
  <li><strong>الخطوة الثالثة (التدليك والشطف):</strong> دلكي كامل الجسم بحركات دائرية خفيفة ثم اشطفي بالماء الفاتر واستمتعي بالعبير.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت زهرة الأوركيد السوداء (Black Orchid Oil):</strong> يمنح العطر الفاخر والنعومة الحريرية.</li>
  <li><strong>مركبات ترطيب وتنظيف لطيفة خالية من البارابين:</strong> تحفظ رطوبة الجلد وتنعش الجسم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم فقط أثناء الاستحمام.</li>
  <li>تجنبي ملامسة السائل المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تفتش عن غسول جسم فاخر بعطر سحر الجمال وثبات 24 ساعة مع لوفة استحمام مهداة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لوكس (Lux)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / غسولات ومستحضرات الاستحمام المعطرة مع لوفة</td></tr>
  <tr><th>نوع المنتج</th><td>غسول جسم معطر بعطر الأوركيد والمسك مع لوفة (250ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>250 مل + لوفة استحمام مهداة</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة جسم نظيفة، حريرية، مرطبة ومعطرة بعطر ساحر يدوم 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>سائل زيتي رغوي غني مخملي</td></tr>
  <tr><th>العطر</th><td>عطر زهرة الأوركيد السوداء والمسك الساحر</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت الأوركيد الأسود، زيوت عطرية، مرطبات لوكس</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / مصر (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (لوكس)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 10 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد غسول لوكس سحر الجمال والزيوت العطرية (Lux Magical Beauty)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول لوكس سحر الجمال مشكلة زوال عطر الاستحمام السريع، جفاف الجلد بالصابون العادي، وتراكم الشوائب.</p>

<h3>لماذا تنجح تركيبة الزيوت العطرية؟</h3>
<p>لأن جزيئات زيت الأوركيد تثبت ب مسام البشرة السطحية، فتطلق عبقاً عطرياً فواحاً مع حركية الجسم لـ 24 ساعة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام اللوفة المرفقة:</strong> دلكي الجسم باللوفة المرفقة لتقشير الخلايا الميتة ورغوة مضاعفة.<br>
2. <strong>الماء الفاتر:</strong> اشطفي بماء فاتر لعدم تجريف الزيوت العطرية الثابتة.<br>
3. <strong>المرطب المكمل:</strong> وضعي لوشن لوكس المعطر بعد الاستحمام لثبات عطري مضاعف.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "غسولات الجسم المعطرة تسبب جفاف وحكة بالبشرة."<br>
<strong>الحقيقة:</strong> غسول لوكس مدعم بزيوت المرطبات لمنع الجفاف وتنعيم الجلد مع العطر الساحر.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تلتصق ميكرو كبسولات العطر الفاخر بالطبقة القرنية (Stratum Corneum)، فتتحرر نوتات المسك والأوركيد تدريجياً.</p>"""

    faqs = [
        ("ما هو غسول الجسم سحر الجمال مع لوفة من لوكس 250 مل؟", "هو غسول استحمام فاخر بعطر زهرة الأوركيد والمسك يضمن عبيراً وثباتاً لـ 24 ساعة مرفق ب لوفة استحمام مهداة سعة 250 مل."),
        ("ما هي فوائد زيت الأوركيد واللوفة المرفقة؟", "يمنح زيت الأوركيد عطراً ساحراً ونعومة حريرية، بينما تساعد اللوفة في التقشير وتكثيف الرغوة."),
        ("هل يدوم العطر لـ 24 ساعة؟", "نعم، مثبت سريرياً في تثبيت نوتات العطر الساحر على بشرة الجسم لـ 24 ساعة."),
        ("ما حجم العبوة؟", "تأتي بحجم 250 مل مع لوفة استحمام مجانية."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اسكبي كمية على اللوفة المبللة، افركي لتوليد رغوة غنية، دلكي الجسم واشطفي بالماء الفاتر."),
        ("هل يترك أثراً جافاً على الجلد؟", "لا، فورمولا مزودة بزيوت مرطبة تنظف وتطري الجلد دون تجفيف."),
        ("ما هو بلد صنع غسول لوكس؟", "صُنع بواسطة شركة يونيلفر (Unilever) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات لوكس لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("ما هي رائحة غسول لوكس سحر الجمال؟", "يتميز برائحة زهرة الأوركيد السوداء والمسك الفاخر الساحر."),
        ("هل يناسب جميع أنواع البشرة؟", "نعم، مناسب للبشرة العادية، الجافة، والحساسة."),
        ("هل أنبوب العبوة 250 مل مناسب للاستخدام اليومي؟", "نعم، حجم ممتاز ومناسب للاستحمام اليومي المنعش."),
        ("هل يناسب النساء والفتيات؟", "نعم، الخيار الأحب للنساء والفتيات لإطلالة معطرة ساحرة."),
        ("كيف أحتفظ بالعبوة واللوفة؟", "تُحفظ العبوة في الشاور وتجفف اللوفة بعد الاستخدام."),
        ("هل الرغوة كثيفة وممتعة؟", "نعم، يولد رغوة مخملية غنية وعطرة جداً."),
        ("هل يغني عن رش المعطرات اليومية؟", "نعم، ثبات العطر 24 ساعة يمنحكِ عبيراً ناعماً طوال اليوم."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة دائرية بغطاء لولبي محكم السكب."),
        ("هل يناسب جميع الفصول؟", "نعم، يمنح انتعاشاً وعطراً ساحراً في الصيف والشتاء."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستخدم يومياً أثناء الاستحمام."),
        ("هل يحتوي على بارابين؟", "تركيبة مجربة ومصرح بها طبقاً لأعلى معايير السلامة."),
        ("هل اللوفة المرفقة ناعمة على الجلد؟", "نعم، لوفة ناعمة تقشر الجلد برفق دون أي خياشة."),
        ("هل يترك الجسم ناعماً كالحرير؟", "نعم، يترك البشرة ملساء ونظيفة ومفعمة بالعبير."),
        ("هل هو غسول لوكس الأكثر شهرة؟", "نعم، غسول سحر الجمال الأكثر مبيعاً وإقبالاً بين غسولات لوكس."),
        ("هل يمنح حس أنوثة وفخامة؟", "نعم، العطر والمسك يمنحانكِ شعوراً مطلقاً بالأناقة."),
        ("هل يتوفر بأحجام ونكهات أخرى لدى إكليل أبها؟", "نعم، تتوفر نكهات متعددة من غسولات لوكس لدى إكليل أبها."),
        ("هل العبوة تصميمها راقٍ وجميل؟", "نعم، تصميم أنيق وجذاب يزين حمامكِ.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Lux Magical Beauty Body Wash with Loofah - 250ml</strong> is the world's #1 iconic, enchanting scented body wash engineered to infuse your body skin with 24-hour long-lasting fine fragrance and velvet softness. Formulated by Lux (Magical Beauty), it fuses Black Orchid Oil with fine fragrance pearls, accompanied by a complimentary shower loofah.</p>
<p>Lux Magical Beauty body wash creates a rich, velvety lather that gently cleanses impurities without stripping skin moisture, leaving you wrapped in a mesmerizing Black Orchid and Royal Musk scent all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>24-Hour Long-Lasting Black Orchid Fragrance:</strong> Imparts a captivating, fine fragrance that lingers on skin all day.</li>
  <li><strong>Includes Complimentary Shower Loofah:</strong> Helps gently exfoliate dead skin cells and create rich foaming lather.</li>
  <li><strong>Rich Velvety Cleansing Lather:</strong> Purifies pores thoroughly without stripping natural skin hydration.</li>
  <li><strong>Enriched with Nourishing Floral Oils:</strong> Softens body skin, leaving it touchably silky smooth.</li>
  <li><strong>Crafted by World-Class Perfumers:</strong> A sophisticated blend of Black Orchid and rich Musk notes.</li>
  <li><strong>Generous 250ml Bottle:</strong> High-value bottle size ideal for daily indulgent shower routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet your body and the complimentary shower loofah with warm water during your shower.</li>
  <li><strong>Step 2 (Lather):</strong> Pour a generous amount of Lux Magical Beauty body wash onto the loofah and rub to create a rich lather.</li>
  <li><strong>Step 3 (Massage & Rinse):</strong> Massage over full body in gentle circular motions, then rinse with warm water.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Black Orchid Oil:</strong> Delivers luxurious fine fragrance and velvet skin softness.</li>
  <li><strong>Nourishing Hydrating Cleansers:</strong> Purify skin while preserving natural lipid moisture.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external body shower cleansing application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a luxury fine-fragrance body wash with 24-hour Black Orchid scent and a free shower loofah.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lux</td></tr>
  <tr><th>Category</th><td>Personal Care / Fine Fragrance Body Washes with Loofah</td></tr>
  <tr><th>Product Type</th><td>24-Hour Fine Fragrance Black Orchid Body Wash (250ml)</td></tr>
  <tr><th>Volume/Weight</th><td>250 ml + Free Shower Loofah</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types</td></tr>
  <tr><th>Finish</th><td>Clean, silky soft, hydrated & 24h fine-fragranced body skin</td></tr>
  <tr><th>Texture</th><td>Rich foaming silky shower gel</td></tr>
  <tr><th>Fragrance</th><td>Captivating Black Orchid & Royal Musk scent</td></tr>
  <tr><th>Active Ingredients</th><td>Black Orchid Oil, Fragrance Pearls, Lux Moisturisers</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / Egypt (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever (Lux)</td></tr>
  <tr><th>Age Group</th><td>All Ages (10+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Fine Fragrance Oils & 24-Hour Aroma Retention</h2>

<h3>What problem does this solve?</h3>
<p>Lux Magical Beauty Body Wash resolves short-lived shower scents, soap drying, and skin dullness.</p>

<h3>Why choose Lux Magical Beauty?</h3>
<p>Black Orchid Oil fine fragrance micro-capsules adhere to epidermal layers, releasing subtle musk notes as your body moves for 24 hours.</p>"""

    en_faqs = [
        ("What is Lux Magical Beauty Body Wash with Loofah - 250ml?", "It is a luxury body wash infused with Black Orchid Oil that provides 24-hour fine fragrance, accompanied by a free shower loofah."),
        ("What are the benefits of Black Orchid Oil and the included loofah?", "Black Orchid Oil provides a long-lasting fine scent and velvet softness, while the loofah gently exfoliates and builds rich lather."),
        ("Does the scent last for 24 hours?", "Yes, clinically proven to retain fine Black Orchid fragrance notes on body skin for 24 continuous hours."),
        ("What volume is contained in this bottle?", "It comes as a 250ml bottle with a free shower loofah."),
        ("How do I use it correctly?", "Pour onto the wet loofah, rub to create rich lather, massage over body, and rinse with warm water."),
        ("Does it dry out skin?", "No, enriched with nourishing moisturizing oils that cleanse while softening skin."),
        ("Where is Lux manufactured?", "It is produced by Unilever following global beauty standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Lux products at Ekleel Abha are 100% original from certified distributors."),
        ("What scent does Lux Magical Beauty have?", "Features a luxurious, captivating Black Orchid and Royal Musk scent."),
        ("Is it suitable for all skin types?", "Ideal for normal, dry, and sensitive body skin types."),
        ("Is the 250ml bottle suitable for daily use?", "Yes, perfect size for daily refreshing shower routines."),
        ("Is it designed for women and girls?", "Yes, a favorite choice for women seeking an elegant fine-fragrance shower experience."),
        ("How should I store the bottle and loofah?", "Store the bottle in your shower and hang the loofah to air dry after use."),
        ("Does it create rich foaming lather?", "Yes, generates a thick, creamy, fragrant lather."),
        ("Does it replace daily body mists?", "Yes, 24-hour fragrance retention provides a subtle scent all day."),
        ("Is the bottle cap leak-proof?", "Yes, comes in a sturdy bottle with a secure flip-top cap."),
        ("Is it great for summer and winter?", "Yes, provides refreshing fine-fragrance shower care year-round."),
        ("How often can I use it daily?", "Use daily during your shower routine."),
        ("Is it paraben-free?", "Dermatologically tested and safety-certified."),
        ("Is the included loofah gentle on skin?", "Yes, soft shower loofah exfoliates skin smoothly without irritation."),
        ("Does it leave skin touchably silky?", "Yes, leaves skin touchably soft, smooth, and clean."),
        ("Is it Lux's best-selling body wash?", "Yes, Magical Beauty is the #1 most popular fine-fragrance Lux body wash."),
        ("Does it provide a feeling of luxury?", "Yes, fine fragrance and rich lather impart a luxurious spa-like feel."),
        ("Are other variants available at Ekleel Abha?", "Yes, Ekleel Abha offers various Lux body wash fragrances."),
        ("Is the bottle design elegant?", "Yes, sleek design that adds elegance to your bathroom shelf.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1833",
        "sku": "EK-1833",
        "gtin": "6281006570306",
        "category": "العناية الشخصية / غسولات ومستحضرات الاستحمام المعطرة مع لوفة",
        "brand": "Lux",
        "ar": {
            "title": "غسول الجسم سحر الجمال مع لوفة من لوكس - 250 مل",
            "meta_title": "غسول الجسم لوكس سحر الجمال مع لوفة 250مل | إكليل أبها",
            "meta_description": "اشتري غسول الجسم سحر الجمال مع لوفة من لوكس (250 مل). عطر الأوركيد والمسك 24 ساعة مع لوفة استحمام مهداة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["لوكس", "غسول_لوكس", "سحر_الجمال", "لوفة_استحمام", "إكليل_أبها"]
        },
        "en": {
            "title": "Lux Magical Beauty Body Wash with Loofah - 250ml",
            "meta_title": "Lux Magical Beauty Body Wash 250ml | Ekleel Abha",
            "meta_description": "Buy original Lux Magical Beauty Body Wash with Loofah (250ml). 24-hour Black Orchid fine fragrance shower gel. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["lux", "magical_beauty", "body_wash", "black_orchid", "ekleel_abha"]
        },
        "schema": {
            "brand": "Lux",
            "category": "Personal Care / Body Wash",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "lux-magical-beauty-body-wash-with-loofah-250ml.webp",
            "alt": "Lux Magical Beauty Body Wash with Loofah 250ml",
            "title": "Lux Magical Beauty Body Wash with Loofah 250ml"
        }
    }

def create_product_1834():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول الفم كولجيت بلاكس لحماية متكاملة ونفس منعش - 500 مل (Colgate Plax Mouthwash, 500ml)</strong> غسول الفم الطبي الأكثر تطوراً وحماية الموثوق عالمياً لمنع البلاك، حماية اللثة، وتأمين حماية مضادة للبكتيريا تدوم لـ 12 ساعة متواصلة. يرتكز هذا الغسول الطبي من كولجيت (Colgate Plax Fresh Mint) على فورمولا الحماية المتكاملة الخالية من الكحول المعززة بـ الفلورايد وتقنية السيلتيدينيم المقاوم للبكتيريا.</p>
<p>يعمل غسول كولجيت بلاكس على الوصول للأماكن الصعبة التي لا تصلها الفرشاة، إزالة 99.9% من البكتيريا المسببة لـ تسوس الأسنان ورائحة الفم الكريهة، وتأمين حماية 10 أضعاف ضد البلاك مقارنة بالتفريش وحده دون إحداث حرقان فمي.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية 12 ساعة مضادة للبكتيريا والبلاك:</strong> يقضي على 99.9% من الجراثيم المسببة للتسوس ورائحة الفم.</li>
  <li><strong>حماية 10 أضعاف ضد البلاك مقارنة بالتفريش:</strong> ينظف المسافات الضيقة التي تعجز عنها الفرشاة.</li>
  <li><strong>خالي 100% من الكحول (Zero Alcohol):</strong> تركيبة لطيفة لا تسبب حرقاناً أو جفافاً بالفم.</li>
  <li><strong>تقوية مينا الأسنان بالفلورايد:</strong> يحمي الأسنان من النخر والتسوس بفاعلية فائقة.</li>
  <li><strong>نفس نعناعي منعش يدوم طوال اليوم:</strong> يغلف الفم بنكهة النعناع الباردة التي تبث الثقة.</li>
  <li><strong>عبوة وافرة سعة 500 مل:</strong> حجم عائلي ممتاز يضمن مضمضة فموية مستمرة لعدة أسابيع.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (المكيال):</strong> اسكبي 20 مل من غسول كولجيت بلاكس في غطاء العبوة.</li>
  <li><strong>الخطوة الثانية (المضمضة):</strong> مضمضي الفم جيداً لمدة 30 ثانية مع التمرير بين فتحات الأسنان.</li>
  <li><strong>الخطوة الثالثة (البصق):</strong> ابصقي السائل دون شطف بالماء أو تناول الطعام لـ 30 دقيقة (يُستعمل مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركب سيلتيدينيم (Cetylpyridinium Chloride):</strong> يقضي على 99.9% من بكتيريا الفم والبلاك.</li>
  <li><strong>فلورايد الصوديوم (Sodium Fluoride 0.05%):</strong> يقوي المينا ويحمي من التسوس خالي من الكحول.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الفموي للمضمضة فقط؛ لا يبتلع الغسول.</li>
  <li>غير مناسب للأطفال دون سن 6 سنوات.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن غسول فم طبي خالي من الكحول بحماية 12 ساعة ضد البلاك ونفس نعناعي منعش من كولجيت.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كولجيت (Colgate Plax)</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم / غسولات الأسنان ومضادات البلاك الخالية من الكحول</td></tr>
  <tr><th>نوع المنتج</th><td>غسول فم طبي خالي من الكحول بحماية 12 ساعة (500ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بالفم والأسنان واللثة)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان منقاة، فم معقم، لثة محمية ونفس نعناعي بارد منعش</td></tr>
  <tr><th>الملمس</th><td>سائل شفاف نعناعي بارد عالي النقاء</td></tr>
  <tr><th>العطر</th><td>عطر النعناع البارد (Fresh Mint) المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>Cetylpyridinium Chloride، فلورايد الصوديوم، خالي من الكحول</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة المتحدة / تايلاند (Colgate-Palmolive)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Colgate-Palmolive</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والأطفال (من 6 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد كولجيت بلاكس الخالي من الكحول (Colgate Plax)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول كولجيت بلاكس مشكلة تراكم البلاك في الأماكن الصعبة، رائحة الفم الكريهة، تسوس الأسنان، وجفاف الفم بالكحول.</p>

<h3>لماذا تنجح تركيبة كولجيت بلاكس؟</h3>
<p>لأن مركب CPC المضاد للبكتيريا يقتل 99.9% من الجراثيم، بينما يحافظ خلوه من الكحول على رطوبة الفم الطبيعية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>المضمضة 30 ثانية:</strong> مضمضي مرتين يومياً بعد تفريش الأسنان.<br>
2. <strong>تجنب الشطف بالماء:</strong> لا تشطفي بالماء فوراً لتمكين الفلورايد من تقوية المينا.<br>
3. <strong>الاستخدام العائلي:</strong> جعل المضمضة روتيناً يومياً للأطفال والبالغين.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "غسولات الفم التي لا تسبب حرقاناً تكون ضعيفة في قتل البكتيريا."<br>
<strong>الحقيقة:</strong> كولجيت بلاكس الخالي من الكحول يقتل 99.9% من البكتيريا بكفاءة طبية فائقة دون الحاجة لكحول يحرق الفم.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط أيونات السيلتيدينيم جدار خلايا البكتيريا اللاهوائية، فتمنع تكتل البلاك وتفكك البيوفلم البكتيري.</p>"""

    faqs = [
        ("ما هو غسول الفم كولجيت بلاكس لحماية متكاملة 500 مل؟", "هو غسول فم طبي من كولجيت خالي من الكحول يقضي على 99.9% من البكتيريا ويمنح حماية 12 ساعة ونفساً منعشاً 500 مل."),
        ("ما هي فوائد خلوه 100% من الكحول؟", "يمنع أي حرقان أو جفاف بالفم ويضمن مضمونة مريحة ولطيفة."),
        ("هل يقتل 99.9% من البكتيريا والبلاك؟", "نعم، مثبت سريرياً في القضاء على 99.9% من بكتيريا الفم والبلاك لـ 12 ساعة."),
        ("ما حجم العبوة؟", "تأتي بحجم عائلي وافر سعة 500 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اسكبي 20 مل، مضمضي الفم 30 ثانية ثم ابصقي دون شطف بالماء مرتين يومياً."),
        ("هل يوفر حماية 10 أضعاف ضد البلاك؟", "نعم، ينظف المسافات التي لا تصلها الفرشاة بحماية 10 أضعاف."),
        ("ما هو بلد صنع كولجيت بلاكس؟", "صُنع بواسطة شركة كولجيت-بالموليف (Colgate-Palmolive) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات كولجيت لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يزيل رائحة الفم الكريهة؟", "نعم، يقضي على البكتيريا المسببة للرائحة ويضمن نفساً نعناعياً بارداً."),
        ("ما هي رائحة ونكهة كولجيت بلاكس؟", "يتميز بنكهة النعناع البارد المنعشة (Fresh Mint)."),
        ("هل يحتوي على الفلورايد لتقوية المينا؟", "نعم، يحتوي على فلورايد الصوديوم لحماية الأسنان من التسوس."),
        ("هل يناسب جميع أفراد العائلة؟", "مناسب للأطفال والبالغين من سن 6 سنوات فما فوق."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل العبوة 500 مل اقتصادية؟", "نعم، عبوة عائلية تكفي للاستخدام المستمر لعدة أسابيع."),
        ("هل يمنع التهاب ونزيف اللثة؟", "نعم، تقليل البلاك يحمي اللثة من التهابات والنزيف."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة شفافة بغطاء مكيالي محكم الحماية."),
        ("هل يغير طعم الطعام بعده؟", "لا يغير طعم الأطعمة بعد فترة قصيرة من المضمضة."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُوصى بالمضمضة مرتين يومياً (صباحاً ومساءً)."),
        ("هل يمنع تكلس الجير الصعب؟", "نعم، الحد من البلاك يمنع تكون الجير التكلسي."),
        ("هل يناسب الأسنان واللثة الحساسة؟", "نعم، خلوه من الكحول يجعله ممتازاً للثة الحساسة."),
        ("هل ينصح به أطباء الأسنان عالمياً؟", "نعم، كولجيت الماركة رقم 1 الموصى بها من أطباء الأسنان عالمياً."),
        ("هل يساعد في تنظيف التقويم والتركيبات؟", "نعم، ممتاز لتنظيف الأماكن الضيقة بالتقويم والتركيبات."),
        ("هل يمنح حس نضارة وثقة طوال اليوم؟", "نعم، النعناع البارد يضمن انتعاشاً وثقة مطلقة."),
        ("هل هو الغسول الأكثر شهرة لكولجيت؟", "نعم، كولجيت بلاكس الغسول الأول والأكثر مبيعاً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Colgate Plax Mouthwash, 500ml</strong> (Fresh Mint) is the world's #1 dentist-recommended 12-hour antibacterial mouthwash engineered to provide 10x better plaque protection and continuous fresh breath confidence. Formulated alcohol-free by Colgate, it combines Sodium Fluoride with Cetylpyridinium Chloride (CPC).</p>
<p>Colgate Plax reaches hard-to-access areas that brushing misses, destroying 99.9% of cavity-causing and bad-breath bacteria without causing any dry mouth burning.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>12-Hour Continuous Antibacterial & Plaque Shield:</strong> Kills 99.9% of germs causing cavities and bad breath.</li>
  <li><strong>10x Better Plaque Protection vs Brushing Alone:</strong> Cleans narrow interdental spaces missed by manual brushing.</li>
  <li><strong>100% Zero Alcohol Formula:</strong> Ultra-gentle formula causing zero burning or dry mouth discomfort.</li>
  <li><strong>Enamel Strengthening Sodium Fluoride:</strong> Fortifies tooth enamel against bacterial acid decay.</li>
  <li><strong>Long-Lasting Fresh Mint Breath:</strong> Envelops your mouth in an intense fresh mint cooling sensation.</li>
  <li><strong>Generous 500ml Family Bottle:</strong> High-value size providing weeks of continuous daily oral hygiene.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Measure):</strong> Pour 20ml of Colgate Plax mouthwash into the cap dispenser.</li>
  <li><strong>Step 2 (Rinse):</strong> Rinse mouth thoroughly for 30 seconds, swishing swishing between teeth.</li>
  <li><strong>Step 3 (Spit):</strong> Spit out solution without rinsing with water; refrain from eating for 30 minutes (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Cetylpyridinium Chloride (CPC):</strong> Kills 99.9% of oral bacteria and prevents plaque formation.</li>
  <li><strong>Sodium Fluoride (0.05%):</strong> Reinforces tooth enamel and defends against cavities.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For oral rinsing application only; do not swallow.</li>
  <li>Not suitable for children under 6 years old.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking an alcohol-free 12-hour antibacterial mouthwash for 10x plaque defense and fresh mint breath.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Colgate (Colgate Plax)</td></tr>
  <tr><th>Category</th><td>Oral Care / 12-Hour Alcohol-Free Antibacterial Mouthwashes</td></tr>
  <tr><th>Product Type</th><td>12-Hour Plaque Defense Zero Alcohol Mouthwash (500ml)</td></tr>
  <tr><th>Volume/Weight</th><td>500 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Oral & Dental Hygiene)</td></tr>
  <tr><th>Finish</th><td>Purified teeth, disinfected gums, 10x plaque defense & fresh mint breath</td></tr>
  <tr><th>Texture</th><td>Clear cooling fresh mint liquid</td></tr>
  <tr><th>Fragrance</th><td>Fresh Mint cooling aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Cetylpyridinium Chloride, Sodium Fluoride, Zero Alcohol Base</td></tr>
  <tr><th>Country of Origin</th><td>United Kingdom / Thailand (Colgate-Palmolive)</td></tr>
  <tr><th>Manufacturer</th><td>Colgate-Palmolive</td></tr>
  <tr><th>Age Group</th><td>Adults & Kids (6+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of CPC Antibacterial Defense & Zero Alcohol Moisture</h2>

<h3>What problem does this solve?</h3>
<p>Colgate Plax Mouthwash resolves interdental plaque buildup, bad breath, cavity decay, and alcohol burning.</p>

<h3>Why choose Colgate Plax?</h3>
<p>CPC (Cetylpyridinium Chloride) kills 99.9% of oral bacteria on contact, forming a 12-hour protective shield over enamel without alcohol dryness.</p>"""

    en_faqs = [
        ("What is Colgate Plax Mouthwash 500ml?", "It is an alcohol-free 12-hour antibacterial mouthwash formulated to kill 99.9% of germs and provide 10x better plaque protection."),
        ("What are the benefits of zero alcohol?", "Prevents burning sensations and dry mouth discomfort while providing gentle oral care."),
        ("Does it kill 99.9% of bacteria and plaque?", "Yes, clinically proven to destroy 99.9% of germs causing cavities and bad breath for 12 hours."),
        ("What volume is contained in this bottle?", "It comes in a generous 500ml family bottle."),
        ("How do I use it correctly?", "Pour 20ml, rinse for 30 seconds, and spit out twice daily without water rinsing."),
        ("Does it provide 10x better plaque protection than brushing alone?", "Yes, cleans narrow interdental spaces missed by manual toothbrushing."),
        ("Where is Colgate Plax manufactured?", "Produced by Colgate-Palmolive following global medical oral standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Colgate products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it eliminate bad breath?", "Yes, neutralizes odor-causing bacteria for long-lasting fresh mint breath."),
        ("What flavor does Colgate Plax have?", "Features a cooling, refreshing Fresh Mint flavor."),
        ("Does it contain Fluoride for enamel strength?", "Yes, enriched with Sodium Fluoride to fortify enamel against cavities."),
        ("Is it safe for family use?", "Safe for adults and children aged 6+."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Is the 500ml bottle economical?", "Yes, generous volume provides weeks of daily family rinsing."),
        ("Does it prevent gum inflammation?", "Yes, reducing plaque buildup protects gums against inflammation and bleeding."),
        ("Is the cap dispenser convenient?", "Yes, comes with a cap dispenser for easy measuring."),
        ("Does it alter food taste after rinsing?", "Does not alter food taste shortly after rinsing."),
        ("How many times daily should I use it?", "Recommended for use twice daily, morning and evening."),
        ("Does it prevent tartar calcification?", "Yes, controlling plaque prevents hard tartar accumulation."),
        ("Is it safe for sensitive teeth and gums?", "Yes, alcohol-free formulation makes it safe for sensitive gums."),
        ("Is Colgate the #1 dentist-recommended brand?", "Yes, Colgate is the #1 globally recommended dental brand."),
        ("Does it clean around braces and dental work?", "Yes, excellent for cleaning around braces, crowns, and implants."),
        ("Does it provide all-day fresh breath confidence?", "Yes, Fresh Mint cooling delivers long-lasting confidence."),
        ("Is Colgate Plax Colgate's best-selling mouthwash?", "Yes, the flagship #1 best-selling mouthwash line by Colgate."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1834",
        "sku": "EK-1834",
        "gtin": "8850006304884",
        "category": "العناية بالفم / غسولات الأسنان ومضادات البلاك الخالية من الكحول",
        "brand": "Colgate",
        "ar": {
            "title": "غسول الفم كولجيت بلاكس لحماية متكاملة ونفس منعش - 500 مل",
            "meta_title": "غسول الفم كولجيت بلاكس 500مل | صيدلية إكليل أبها",
            "meta_description": "اشتري غسول الفم كولجيت بلاكس لحماية متكاملة ونفس منعش (500 مل). خالي 100% من الكحول بحماية 12 ساعة ضد البلاك. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["كولجيت", "كولجيت_بلاكس", "غسول_الفم", "حماية_البلاك", "إكليل_أبها"]
        },
        "en": {
            "title": "Colgate Plax Mouthwash, 500ml",
            "meta_title": "Colgate Plax Mouthwash 500ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Colgate Plax Mouthwash (500ml). 12-hour antibacterial plaque defense alcohol-free formula. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["colgate", "colgate_plax", "mouthwash", "zero_alcohol", "ekleel_abha"]
        },
        "schema": {
            "brand": "Colgate",
            "category": "Oral Care / Mouthwash",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "colgate-plax-mouthwash-500ml.webp",
            "alt": "Colgate Plax Mouthwash 500ml",
            "title": "Colgate Plax Mouthwash 500ml"
        }
    }

def create_product_1835():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول الفم اكتيف للعناية المتكاملة ونظافة الأسنان - 300 مل (Active Mouthwash - 300 ml)</strong> غسول الفم الألماني الطبي المتقدم (Lacalut Active / Active Fresh) المصمم خصيصاً لحماية الفم، تقوية اللثة، ومكافحة نزيف والتهاب اللثة ب فاعلية فائقة. يرتكز هذا الغسول الطبي من اكتيف (Active Fresh) على فورمولا الألومنيوم لاكتات المقلحة، فلورايد الصوديوم، والزيوت العطرية المطهرة.</p>
<p>يعمل غسول أكتيف على شد أنسجة اللثة المتهالكة، القضاء على البكتيريا المسببة لـ نزيف اللثة ورائحة الفم الكريهة، وتأمين حماية متكاملة لمينا الأسنان دون التسبب في جفاف الفم، ليمنحكِ ابتسامة صحية ونفساً منعشاً يبث الثقة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>شد وتدعيم أنسجة اللثة المتهالكة:</strong> الألومنيوم لاكتات يقوي اللثة يمنع نزيفها فورياً.</li>
  <li><strong>حماية متكاملة لمينا الأسنان من التسوس:</strong> الفلورايد الطبي يقوي المينا ويحميها من النخر.</li>
  <li><strong>القضاء على البكتيريا ورائحة الفم الكريهة:</strong> يطهر الأماكن الضيقة والأنسجة الفموية بفاعلية طبية.</li>
  <li><strong>تركيبة خالية من الكحول والقساوة:</strong> لا تسبب حرقاناً أو جفافاً بالفم أثناء المضمضة.</li>
  <li><strong>مثالي لعلاج نزيف اللثة والتهاب الأنسجة:</strong> يهدئ أحمرار اللثة ويحميه من التراجع.</li>
  <li><strong>عبوة سعة 300 مل:</strong> حجم طبي ممتاز ومناسب للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (المكيال):</strong> اسكبي 10 إلى 15 مل من غسول أكتيف في غطاء العبوة.</li>
  <li><strong>الخطوة الثانية (المضمضة):</strong> مضمضي الفم جيداً لمدة 30 ثانية مع التمرير بين الأسنان واللثة.</li>
  <li><strong>الخطوة الثالثة (البصق):</strong> ابصقي السائل دون شطف بالماء لمدة 30 دقيقة (يُستعمل مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>ألومنيوم لاكتات (Aluminum Lactate):</strong> يشد اللثة ويمنع النزيف والالتهاب.</li>
  <li><strong>فلورايد الصوديوم وزيوت مطهرة:</strong> يقويان المينا ويطهران الفم ونفساً منعشاً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الفموي للمضمضة فقط؛ لا يبتلع الغسول.</li>
  <li>غير مناسب للأطفال دون سن 6 سنوات.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من نزيف اللثة، التهاب الأنسجة الفموية، ويرغب في غسول فم ألماني طبي شديد الفاعلية.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>أكتيف / لاكالوت (Lacalut / Active Fresh)</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم / غسولات الأسنان الطبية لعلاج اللثة</td></tr>
  <tr><th>نوع المنتج</th><td>غسول فم طبي لشد اللثة وحماية الأسنان (300ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>300 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بالفم والأسنان واللثة)</td></tr>
  <tr><th>المظهر النهائي</th><td>لثة مشدودة قوية خالية من النزيف، أسنان محمية ونفس منعش</td></tr>
  <tr><th>الملمس</th><td>سائل شفاف طبي عالي النقاء</td></tr>
  <tr><th>العطر</th><td>عطر النعناع والأعشاب الطبية المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>ألومنيوم لاكتات، فلورايد الصوديوم، الزيوت العطرية المطهرة</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا (Germany)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Dr. Theiss Naturwaren GmbH</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والأطفال (من 6 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد ألومنيوم لاكتات وغسول أكتيف (Active Mouthwash)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول أكتيف الطبي مشكلة نزيف اللثة عند التفريش، تراجع اللثة، تسوس الأسنان، ورائحة الفم الكريهة.</p>

<h3>لماذا تنجح تركيبة ألومنيوم لاكتات؟</h3>
<p>لأن الألومنيوم لاكتات يمتلك خاصية قابضة للأوعية (Astringent)، فيقبض الشعيرات الدموية المتهالكة باللثة ليوقف النزيف فورياً.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>المضمضة بعد تفريش الأسنان:</strong> مضمضي مرتين يومياً بعد الغسيل بالفرشاة.<br>
2. <strong>تجنب الشطف المباشر بالماء:</strong> دع المواد القابضة والفلورايد تتفاعل باللثة لـ 30 دقيقة.<br>
3. <strong>الاستخدام عند الحوامل:</strong> ممتاز جداً لعلاج نزيف لثة الحوامل بحذر تحت الإشراف.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "نزيف اللثة يزول تلقائياً دون حاجة لغسول طبي قابض."<br>
<strong>الحقيقة:</strong> إهمال نزيف اللثة يؤدي لتراجع العظم والأسنان، بينما غسول أكتيف يشد اللثة ويوقف النزيف.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يخثر ألومنيوم لاكتات البروتينات السطحية بأنسجة اللثة، مما يشكل غشائاً يوقف النزيف ويقلل نفاذية البكتيريا.</p>"""

    faqs = [
        ("ما هو غسول الفم اكتيف للعناية المتكاملة 300 مل؟", "هو غسول فم ألماني طبي من أكتيف غني بالألومنيوم لاكتات والفلورايد لشد اللثة ومنع النزيف وتأمين نفس منعش 300 مل."),
        ("ما هي فوائد ألومنيوم لاكتات والفلورايد؟", "يشد الألومنيوم لاكتات أنسجة اللثة المتهالكة ويمنع النزيف، بينما يقوي الفلورايد المينا ضد التسوس."),
        ("هل يوقف نزيف والتهاب اللثة فورياً؟", "نعم، مثبت سريرياً في قبض الشعيرات الدموية ووقف نزيف اللثة والتهاب الأنسجة."),
        ("ما حجم العبوة؟", "تأتي بحجم 300 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اسكبي 10-15 مل، مضمضي الفم 30 ثانية ثم ابصقي دون شطف بالماء مرتين يومياً."),
        ("هل هو خالي من الكحول والقساوة؟", "نعم، تركيبة طبية خالية من الكحول لا تسبب حرقاناً أو جفافاً بالفم."),
        ("ما هو بلد صنع غسول أكتيف؟", "صُنع بفخر في ألمانيا بواسطة شركة د. تايس (Dr. Theiss Naturwaren)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع المستحضرات الطبية لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يزيل رائحة الفم الكريهة؟", "نعم، يقضي على البكتيريا المسببة للرائحة ويضمن نفساً نعناعياً منعشاً."),
        ("ما هي رائحة ونكهة غسول أكتيف؟", "يتميز برائحة ونكهة النعناع والأعشاب الطبية المنعشة."),
        ("هل يناسب لثة الحوامل؟", "ممتاز جداً لعلاج نزيف وتضخم لثة الحوامل."),
        ("هل يناسب جميع أفراد العائلة؟", "مناسب للأطفال والبالغين من سن 6 سنوات فما فوق."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل العبوة 300 مل مناسبة للاستخدام المستمر؟", "نعم، حجم طبي تكفي للاستخدام المستمر لعدة أسابيع."),
        ("هل يمنع تكلس الجير والبلاك؟", "نعم، يمنع تراكم البلاك وتكلس الجير بالمسافات الفموية."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة دائرية بغطاء مكيالي محكم الحماية."),
        ("هل يغير طعم الطعام بعده؟", "لا يغير طعم الأطعمة بعد فترة قصيرة من المضمضة."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُوصى بالمضمضة 2 مرات يومياً (صباحاً ومساءً)."),
        ("هل يقلل حركة وتراجع الأسنان؟", "نعم، شد وتقوية أنسجة اللثة يحمي الأسنان من التراجع."),
        ("هل يناسب الأسنان واللثة الحساسة؟", "نعم، تركيبة طبية خفيفة ممتازة للثة الحساسة."),
        ("هل ينصح به أطباء الأسنان بألمانيا؟", "نعم، الغسول الألماني الطبي الأكثر ثقة لعلاج نزيف اللثة."),
        ("هل يساعد في تنظيف التقويم والتركيبات؟", "نعم، ينظف ما حول التركيبات والتقويم بحماية مضادة للبكتيريا."),
        ("هل يمنح حس نضارة وثقة طوال اليوم؟", "نعم، يضمن انتعاشاً ونظافة وثقة مطلقة."),
        ("هل هو الغسول الألماني الأكثر مبيعاً للثة؟", "نعم، غسول أكتيف الخيار الطبي الأول لعلاج اللثة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Active Mouthwash - 300 ml</strong> (Lacalut / Active Fresh) is the German medical clinical mouthwash formulated to firm gums, prevent gingival bleeding, and halt oral inflammation. Engineered by Dr. Theiss Naturwaren, it combines astringent Aluminum Lactate, Sodium Fluoride, and antiseptic mint oils.</p>
<p>Active Mouthwash tightens delicate gum tissues, destroys bad-breath and plaque-causing bacteria, and fortifies tooth enamel without causing dry mouth burning.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Firms & Tightens Bleeding Gum Tissue:</strong> Aluminum Lactate tightens gums and halts gingival bleeding instantly.</li>
  <li><strong>Complete Cavity & Enamel Protection:</strong> Medical Sodium Fluoride reinforces enamel against bacterial decay.</li>
  <li><strong>Destroys Plaque & Bad-Breath Bacteria:</strong> Cleans narrow interdental spaces missed by manual toothbrushing.</li>
  <li><strong>100% Alcohol-Free Gentle Formula:</strong> Causes zero burning or dry mouth discomfort during swishing.</li>
  <li><strong>Ideal for Gingivitis & Periodontitis:</strong> Calms gum redness and protects against recession.</li>
  <li><strong>Compact 300ml Medical Bottle:</strong> High-value medical size ideal for daily continuous oral hygiene.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Measure):</strong> Pour 10 to 15ml of Active mouthwash into the cap dispenser.</li>
  <li><strong>Step 2 (Rinse):</strong> Rinse mouth thoroughly for 30 seconds, swishing between teeth and gums.</li>
  <li><strong>Step 3 (Spit):</strong> Spit out solution without rinsing with water for 30 minutes (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Aluminum Lactate:</strong> Tightens gum tissue and halts bleeding and inflammation.</li>
  <li><strong>Sodium Fluoride & Antiseptic Oils:</strong> Fortify tooth enamel and deliver long-lasting fresh breath.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For oral rinsing application only; do not swallow.</li>
  <li>Not suitable for children under 6 years old.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from bleeding gums, gingivitis, or oral inflammation seeking a German clinical astringent mouthwash.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Active / Lacalut (Active Fresh)</td></tr>
  <tr><th>Category</th><td>Oral Care / German Clinical Gum Protection Mouthwashes</td></tr>
  <tr><th>Product Type</th><td>Astringent Gum-Tightening Medical Mouthwash (300ml)</td></tr>
  <tr><th>Volume/Weight</th><td>300 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Oral, Dental & Gum Hygiene)</td></tr>
  <tr><th>Finish</th><td>Tightened strong gums, bleeding stopped, enamel protected & fresh breath</td></tr>
  <tr><th>Texture</th><td>Clear medical cooling mint liquid</td></tr>
  <tr><th>Fragrance</th><td>Fresh Mint & herbal medical aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Aluminum Lactate, Sodium Fluoride, Antiseptic Oils</td></tr>
  <tr><th>Country of Origin</th><td>Germany</td></tr>
  <tr><th>Manufacturer</th><td>Dr. Theiss Naturwaren GmbH</td></tr>
  <tr><th>Age Group</th><td>Adults & Kids (6+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Aluminum Lactate Astringation & Gum Hemostasis</h2>

<h3>What problem does this solve?</h3>
<p>Active Mouthwash resolves gingival bleeding, swollen gums, periodontitis, and bad breath.</p>

<h3>Why choose Active Mouthwash?</h3>
<p>Aluminum Lactate acts as a potent tissue astringent, precipitating mucosal proteins to halt capillary bleeding instantly.</p>"""

    en_faqs = [
        ("What is Active Mouthwash - 300 ml?", "It is a German medical clinical mouthwash formulated with Aluminum Lactate and Fluoride to firm gums and stop bleeding."),
        ("What are the benefits of Aluminum Lactate and Fluoride?", "Aluminum Lactate tightens bleeding gum tissue, while Fluoride fortifies enamel against cavities."),
        ("Does it stop gum bleeding and inflammation?", "Yes, clinically proven to constrict mucosal capillaries and halt gingival bleeding."),
        ("What volume is contained in this bottle?", "It comes in a compact 300ml bottle."),
        ("How do I apply it correctly?", "Pour 10-15ml, rinse for 30 seconds, and spit out twice daily without water rinsing."),
        ("Is it alcohol-free?", "Yes, gentle clinical formula free of alcohol; causes zero burning or dry mouth."),
        ("Where is Active Mouthwash manufactured?", "It is proudly manufactured in Germany by Dr. Theiss Naturwaren."),
        ("How do I verify authenticity at Ekleel Abha?", "All medical oral care products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it eliminate bad breath?", "Yes, neutralizes odor-causing oral bacteria for long-lasting fresh mint breath."),
        ("What flavor does Active Mouthwash have?", "Features a clean medical Fresh Mint and herbal flavor."),
        ("Is it suitable for pregnant women with bleeding gums?", "Yes, highly recommended for soothing pregnancy gingivitis under supervision."),
        ("Is it safe for family use?", "Safe for adults and children aged 6+."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Is the 300ml bottle economical?", "Yes, provides weeks of continuous daily clinical oral hygiene."),
        ("Does it prevent plaque calcification?", "Yes, controlling plaque prevents hard tartar accumulation."),
        ("Is the cap dispenser convenient?", "Yes, comes with a cap dispenser for easy measuring."),
        ("Does it alter food taste after rinsing?", "Does not alter food taste shortly after rinsing."),
        ("How many times daily should I use it?", "Recommended for use twice daily, morning and evening."),
        ("Does it protect against gum recession?", "Yes, tightening gingival tissue guards teeth against recession."),
        ("Is it safe for sensitive gums?", "Yes, gentle medical formulation safe for sensitive gums."),
        ("Is it German dentist recommended?", "Yes, top trusted German medical mouthwash for gum bleeding."),
        ("Does it clean around braces and implants?", "Yes, excellent for sanitizing around braces, crowns, and implants."),
        ("Does it provide fresh breath confidence?", "Yes, delivers medical fresh breath confidence all day."),
        ("Is it a top German clinical mouthwash choice?", "Yes, the #1 medical choice for bleeding gum care."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1835",
        "sku": "EK-1835",
        "gtin": "4016369546123",
        "category": "العناية بالفم / غسولات الأسنان الطبية لعلاج اللثة",
        "brand": "Active",
        "ar": {
            "title": "غسول الفم اكتيف للعناية المتكاملة ونظافة الأسنان - 300 مل",
            "meta_title": "غسول الفم اكتيف 300مل | صيدلية إكليل أبها",
            "meta_description": "اشتري غسول الفم اكتيف للعناية المتكاملة ونظافة الأسنان (300 مل). غسول ألماني طبي بالألومنيوم لاكتات لشد اللثة ومنع النزيف. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["اكتيف", "غسول_اكتيف", "علاج_نزيف_اللثة", "غسول_ألماني", "إكليل_أبها"]
        },
        "en": {
            "title": "Active Mouthwash - 300 ml",
            "meta_title": "Active Mouthwash 300ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Active Mouthwash (300 ml). German clinical formula with Aluminum Lactate to firm gums & stop bleeding. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["active_mouthwash", "lacalut", "gum_protection", "bleeding_gums", "ekleel_abha"]
        },
        "schema": {
            "brand": "Active",
            "category": "Oral Care / Mouthwash",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "active-mouthwash-300ml.webp",
            "alt": "Active Mouthwash 300 ml",
            "title": "Active Mouthwash 300 ml"
        }
    }

print("Loaded all Batch 25 builders with 25 FAQs")
