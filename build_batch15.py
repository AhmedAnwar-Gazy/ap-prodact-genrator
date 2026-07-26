import json, os

def create_product_1777():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>عطر افلون بيش للأطفال من سن سيت كافيه - 22 مل (Avalon Peach Perfume by Sunset Cafe - 22 ml)</strong> العطر الفاكهي اللطيف والأنعش المخصص للأطفال والبنات لإضفاء لمسة من السعادة والانتعاش طوال اليوم. يمزج هذا العطر الفرنسي الرقيق من علامة سن سيت كافيه بين نغمات الدراق الخوخي الطبيعي (Sweet Peach)، عبير الفواكه الاستوائية الناعمة، والنفحات الزهرية الخفيفة التي تناسب بشرة وملابس الأطفال الرقيقة.</p>
<p>يمتاز العطر بتركيبة آمنة وخالية من الكحول القاسي لتجنب تهيج بشرة الأطفال، وتأتي في زجاجة أنيقة سعة 22 مل مدمجة وسهلة الحمل في حقيبة المدرسة أو السفر ليرافق طفلتكِ في كل أوقاتها.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عبير الخوخ الاستوائي الطبيعي:</strong> يمنح طفلتكِ انتعاشاً فاكهياً رقيقاً ومحبباً طوال اليوم.</li>
  <li><strong>تركيبة رقيقة وآمنة للأطفال:</strong> خالية من الكحول القاسي والمواد الضارة لحماية بشرة الأطفال الحساسة.</li>
  <li><strong>ثبات ممتاز ورائحة لطيفة:</strong> يدوم لعدة ساعات على الملابس دون أن يكون نفاذاً أو ثقيلاً.</li>
  <li><strong>زجاجة مدمجة سعة 22 مل:</strong> تصميم أنيق ومثالي لحقيبة المدرسة، الرحلات، والسفر.</li>
  <li><strong>يعزز الشعور بالنظافة والانتعاش:</strong> يمنح الطفل شعوراً مبهجاً بالنظافة والأنشطة اليومية.</li>
  <li><strong>عطر فرنسي مخصص للأطفال:</strong> مصمم وفق أعلى معايير السلامة والجودة الفرنسية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الرش):</strong> رشي قطرات من عطر افلون بيش على ملابس الطفل أو خلف الأذنين وعلى المعصمين من مسافة 15 سم.</li>
  <li><strong>الخطوة الثانية (الاستمتاع):</strong> اتركي العطر ليجف طبيعياً واستمتعي بالعبير الفاكهي المنعش.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>نغمات الدراق الخوخي (Sweet Peach Notes):</strong> يمنح حلاوة فاكهية مبهجة.</li>
  <li><strong>عبق الفواكه والزهور الناعمة:</strong> يضيف انتعاشاً خفيفاً وناعماً.</li>
  <li><strong>قاعدة عطرية آمنة خالية من الكحول القاسي:</strong> لطيفة على بشرة وملابس الأطفال.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي فقط تحت إشراف الوالدين.</li>
  <li>تجنبي رش العطر مباشرة على العينين أو البشرة المتهيجة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال الصغار وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>للأطفال والبنات والوالدين الراغبين في عطر فاكهي آمن برائحة الخوخ الطبيعي.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سن سيت كافيه (Sunset Cafe)</td></tr>
  <tr><th>الفئة</th><td>عطور الأطفال / عطور الفواكه الرقيقة للأطفال</td></tr>
  <tr><th>نوع المنتج</th><td>عطر للأطفال برائحة الخوخ (Avalon Peach Eau de Parfum)</td></tr>
  <tr><th>الحجم/الوزن</th><td>22 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة وملابس الأطفال الحساسة</td></tr>
  <tr><th>المظهر النهائي</th><td>انتعاش فاكهي مبهج ورائحة خوخ زكية طوال اليوم</td></tr>
  <tr><th>الملمس</th><td>رذاذ عطري خفيف ورقيق</td></tr>
  <tr><th>العطر</th><td>عطر الخوخ الفاكهي الحلو والانتعاش الزهري</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة الخوخ الطبيعي، نفحات فاكهية، قاعدة خالية من الكحول القاسي</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Sunset Cafe Perfumes France</td></tr>
  <tr><th>الفئة العمرية</th><td>الأطفال والمراهقين (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لعطور الأطفال برائحة الخوخ (Sunset Cafe)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يحلم عطر افلون بيش مشكلة الرغبة في تعطير الأطفال بعطور آمنة خالية من الكحول القاسي والمواد المسببة للحساسية.</p>

<h3>لماذا تنجح تركيبة سن سيت كافيه؟</h3>
<p>لأن نغمات الخوخ الطبيعية مصممة على قاعدة خالية من الكحول القاسي، مما يمنح انتعاشاً فاكهياً زكياً ودون تهيج البشرة الرقيقة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الرش على الملابس:</strong> يُفضل الرش على ملابس الطفل لثبات أطول.<br>
2. <strong>الحفظ بعيداً عن الشمس:</strong> احفظي الزجاجة في مكان بارد للحفاظ على العبير.<br>
3. <strong>الحجم المناسب للسفر:</strong> ضعي زجاجة 22 مل في حقيبة المدرسة أو السفر.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "عطور الأطفال تسبب الحساسية بالضرورة."<br>
<strong>الحقيقة:</strong> عطور سن سيت كافيه الفرنسية خالية من الكحول القاسي ومجربة لسلامة الأطفال.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتطاير الجزيئات العطرية الفاكهية اللطيفة في الهواء دون نفاذية قاسية، لتمنح إحساساً بالنظافة والبهجة دون التأثير على جهاز الطفل التنفسي.</p>"""

    faqs = [
        ("ما هو عطر افلون بيش للأطفال من سن سيت كافيه 22 مل؟", "هو عطر فرنسي آمن برائحة الخوخ الفاكهية اللطيفة مخصص للأطفال بحجم مدمج 22 مل."),
        ("ما هي مميزات رائحة الخوخ (Avalon Peach)؟", "تمنح رائحة الخوخ الطبيعية انتعاشاً فاكهياً مبهجاً ومحبباً للأطفال."),
        ("هل هو خالي من الكحول القاسي وآمن للبشرة؟", "نعم، تركيبته مخصصة لحماية بشرة وملابس الأطفال الحساسة."),
        ("ما حجم الزجاجة؟", "تأتي بحجم 22 مل مدمج وسهل الحمل."),
        ("هل يناسب حمل العطر في حقيبة المدرسة أو السفر؟", "نعم، تصميم أنيق وحجم صغير مثالي لحقيبة المدرسة والسفر."),
        ("ما هو بلد صنع العطر؟", "صُنع بفخر في فرنسا بواسطة سن سيت كافيه (Sunset Cafe)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع عطور سن سيت كافيه لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يثبت على الملابس؟", "نعم، يثبت لعدة ساعات برائحة ناعمة وغير نفاذة."),
        ("ما هي الفئة العمرية المناسبة؟", "مناسب للأطفال والمراهقين من سن 3 سنوات فما فوق."),
        ("هل يسبب بقعاً على ملابس الأطفال؟", "لا، رذاذ شفاف لا يترك أثراً على الأقمشة."),
        ("هل يناسب الأولاد والبنات؟", "محبوب جداً للبنات والأطفال الراغبين في عطر فاكهي."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل هو خيار ممتاز كهدية للأطفال؟", "نعم، زجاجة أنيقة وعطر مبهج يمثل هدية رائعة للأطفال."),
        ("هل العطر نفاذ أم رقيق؟", "رقيق وناعم جداً يناسب حساسية الأطفال."),
        ("هل يمكن رشه خلف الأذنين والمعصمين؟", "نعم، رشي على نقاط النبض والملابس ب أمان."),
        ("هل يحتوي على زيوت طبيعية؟", "مدعم بخلاصات فاكهية فرنسية ناعمة."),
        ("هل يترك شعوراً بالنظافة؟", "نعم، يمنح الطفل إحساساً فورياً بالنظافة والبهجة."),
        ("هل الزجاجة متينة؟", "تأتي في زجاجة غليظة بغطاء محكم الحماية."),
        ("كم رشّة تكفي في المرة؟", "رشّتان إلى 3 رشّات تكفي لتعطير كامل."),
        ("هل يلزم ترجيج العبوة قبل الرش؟", "يُفضل ترجيعها خفيفاً قبل الاستعمال."),
        ("هل العبوة 22 مل اقتصادية؟", "نعم، تمنح مئات الرشات بفضل بخاخها الدقيق."),
        ("هل يناسب فصل الصيف والحر؟", "ممتاز جداً لإنعاش الأطفال في حر الصيف."),
        ("هل يحتوي على بارابين؟", "خالي من المواد الكيميائية الضارة للأطفال."),
        ("هل ينصح به للأطفال ذوي البشرة الحساسة؟", "نعم، تركيبة لطيفة مخصصة للبشرة الحساسة."),
        ("هل يتوفر بنكهات أخرى في إكليل أبها؟", "نعم، تتوفر نكهات فاكهية متعددة من سن سيت كافيه.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Avalon Peach Perfume by Sunset Cafe - 22 ml</strong> is a delightful, safe fruity fragrance designed to bring everyday joy and sweetness to kids and teens. Crafted in France by renowned perfumers Sunset Cafe, it blends natural sweet peach notes with soft tropical fruits and gentle florals suitable for delicate child skin and clothes.</p>
<p>Formulated without harsh alcohol to protect sensitive skin from irritation, this compact 22 ml bottle easily fits into school backpacks or travel pouches, offering your child an instant boost of refreshing sweetness wherever they go.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Natural Sweet Peach Aroma:</strong> Provides a pleasant, sweet fruity freshness all day long.</li>
  <li><strong>Child-Safe Hypoallergenic Formula:</strong> Free from harsh alcohol and aggressive chemicals to protect child skin.</li>
  <li><strong>Long-Lasting Gentle Sillage:</strong> Stays on clothes for hours without being overwhelming.</li>
  <li><strong>Compact 22 ml Travel Size:</strong> Elegant bottle perfect for school bags, trips, and daily outings.</li>
  <li><strong>Enhances Freshness & Happiness:</strong> Gives children an uplifting feel of cleanliness and joy.</li>
  <li><strong>French Crafted Quality:</strong> Manufactured adhering to strict European safety standards for kids.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Spray):</strong> Hold Avalon Peach Perfume bottle 15 cm away and spray onto child's clothes or wrist points.</li>
  <li><strong>Step 2 (Enjoy):</strong> Allow to dry naturally and enjoy the long-lasting sweet peach aroma.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Sweet Peach Notes:</strong> Delivers vibrant, sweet fruity sweetness.</li>
  <li><strong>Soft Tropical Fruit & Floral Accords:</strong> Adds a light, soothing floral-fruity fresh sillage.</li>
  <li><strong>Harsh-Alcohol-Free Base:</strong> Gentle on young skin and clothing fibers.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external use under adult supervision.</li>
  <li>Avoid spraying directly into eyes or onto broken skin.</li>
  <li>Keep out of reach of very young children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Kids, teens, and parents seeking a French-crafted, child-safe sweet peach fragrance.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Sunset Cafe</td></tr>
  <tr><th>Category</th><td>Kids Perfumes / Fruity Children Fine Fragrances</td></tr>
  <tr><th>Product Type</th><td>Avalon Peach Eau de Parfum for Kids</td></tr>
  <tr><th>Volume/Weight</th><td>22 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Child Skin & Clothes Types</td></tr>
  <tr><th>Finish</th><td>Uplifting sweet peach aroma & fresh sillage</td></tr>
  <tr><th>Texture</th><td>Ultra-fine clear fragrance mist</td></tr>
  <tr><th>Fragrance</th><td>Sweet Peach & Tropical Fruit accords</td></tr>
  <tr><th>Active Ingredients</th><td>Peach extract, Fruity Accords, Gentle Alcohol-Free Base</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>Sunset Cafe Perfumes France</td></tr>
  <tr><th>Age Group</th><td>Kids & Teens (3+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Child-Safe Fragrances & Peach Accords</h2>

<h3>What problem does this solve?</h3>
<p>Sunset Cafe Avalon Peach Perfume resolves the need for safe, harsh-alcohol-free fragrances for children.</p>

<h3>Why choose Sunset Cafe?</h3>
<p>Sweet peach notes are formulated on a gentle base free from harsh alcohol, imparting sweet freshness without irritating sensitive skin.</p>"""

    en_faqs = [
        ("What is Avalon Peach Perfume by Sunset Cafe 22 ml?", "It is a French-crafted sweet peach fragrance designed for kids in a compact 22 ml bottle."),
        ("What does Avalon Peach smell like?", "It features a sweet natural peach fragrance blended with light fruity accords."),
        ("Is it harsh-alcohol-free and safe for children?", "Yes, formulated to protect sensitive child skin and clothing."),
        ("What bottle volume is provided?", "It comes in a compact 22 ml spray bottle."),
        ("Is it travel and school bag friendly?", "Yes, compact 22 ml size fits easily into school bags and travel kits."),
        ("Where is Sunset Cafe manufactured?", "It is proudly manufactured in France."),
        ("How do I verify authenticity at Ekleel Abha?", "All Sunset Cafe perfumes at Ekleel Abha are 100% original from certified distributors."),
        ("Does it stay on clothes?", "Yes, lingers gently on clothing for hours without heavy overpowering notes."),
        ("What age group is it suitable for?", "Ideal for children and teens aged 3+."),
        ("Does it stain child clothing?", "No, clear fine mist leaves zero residue on fabrics."),
        ("Is it loved by girls?", "Yes, highly popular among young girls and kids who love sweet fruity scents."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct sunlight."),
        ("Is it a great gift for children?", "Yes, an adorable bottle and sweet scent make it a perfect gift."),
        ("Is the scent overpowering?", "No, ultra-gentle sillage tailored for young senses."),
        ("Can it be sprayed on pulse points?", "Yes, spray safely on pulse points and clothing."),
        ("Does it contain natural fruity extracts?", "Yes, enriched with fine French fruity essences."),
        ("Does it leave a clean refreshed feel?", "Yes, gives children an instant fresh and cheerful feel."),
        ("Is the bottle sturdy?", "Yes, packaged in a durable glass bottle with a secure cap."),
        ("How many sprays are needed per use?", "2 to 3 sprays provide complete, delightful scenting."),
        ("Should I shake before spraying?", "A gentle shake before spraying is recommended."),
        ("Is the 22 ml bottle economical?", "Yes, delivers hundreds of fine mist sprays."),
        ("Is it great for summer heat?", "Yes, perfect for refreshing kids during warm summer days."),
        ("Is it paraben-free?", "Yes, free from harsh chemicals."),
        ("Is it recommended for sensitive skin?", "Yes, ultra-gentle formula safe for sensitive skin."),
        ("Are other flavors available at Ekleel Abha?", "Yes, Ekleel Abha offers various Sunset Cafe child fragrances.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1777",
        "sku": "EK-1777",
        "gtin": "788119003081",
        "category": "عطور الأطفال / عطور الفواكه الرقيقة للأطفال",
        "brand": "Sunset Cafe",
        "ar": {
            "title": "عطر افلون بيش للأطفال من سن سيت كافيه - 22 مل",
            "meta_title": "عطر سن سيت كافيه افلون بيش 22مل للأطفال | صيدلية إكليل أبها",
            "meta_description": "اشتري عطر افلون بيش للأطفال من سن سيت كافيه (22 مل). عطر خوخ فرنسي آمن ورقيق خالي من الكحول القاسي. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["سن_سيت_كافيه", "عطر_افلون_بيش", "عطور_الأطفال", "عطر_الخوخ", "إكليل_أبها"]
        },
        "en": {
            "title": "Avalon Peach Perfume by Sunset Cafe - 22 ml",
            "meta_title": "Avalon Peach Perfume by Sunset Cafe 22ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Avalon Peach Perfume by Sunset Cafe (22 ml). French child-safe sweet peach fragrance. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["sunset_cafe", "avalon_peach", "kids_perfume", "peach_fragrance", "ekleel_abha"]
        },
        "schema": {
            "brand": "Sunset Cafe",
            "category": "Kids Fragrance / Eau de Parfum",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "avalon-peach-perfume-by-sunset-cafe-22ml.webp",
            "alt": "Avalon Peach Perfume by Sunset Cafe 22 ml",
            "title": "Avalon Peach Perfume by Sunset Cafe 22 ml"
        }
    }

def create_product_1778():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>صابون لايفبوي المتكامل 10 للحماية من الجراثيم - 125 جم (Lifebuoy Complete Soap 10, 125g)</strong> الصابون الطبي الأول والموثوق عالمياً لتوفير حماية متكاملة بنسبة 99.9% ضد الجراثيم والبكتيريا الضارة. يرتكز هذا الصابون المتطور من لايفبوي على تقنية الفضة النشطة المتقدمة (Activ Silver Formula)، حيث ينظف البشرة بعمق ويقضي على الجراثيم والميكروبات المسببة للأمراض والعدوى في 10 ثوانٍ فقط.</p>
<p>يمتاز صابون لايفبوي المتكامل 10 برغوة غنية وناعمة تترك بشرتكِ وبشرة عائلتكِ نظيفة، منتعشة، ومحمية من البكتيريا طوال اليوم دون تسبب في جفاف أو تهيج الجلد.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية 99.9% من الجراثيم والبكتيريا:</strong> يقضي على مسببات الأمراض والعدوى في 10 ثوانٍ فقط.</li>
  <li><strong>تقنية الفضة النشطة (Activ Silver Formula):</strong> توفر درع حماية متطور مستمر ضد البكتيريا طوال اليوم.</li>
  <li><strong>تنظيف عميق وانتعاش تام:</strong> يزيل الأوساخ، الدهون، العرق، والجراثيم من المسام بفاعلية.</li>
  <li><strong>رغوة غنية ولطيفة على الجلد:</strong> تنظف وتنعش البشرة دون تجريد الزيوت الطبيعية.</li>
  <li><strong>مناسب لجميع أفراد العائلة:</strong> صابون طبي عائلي آمن للاستخدام اليومي المتكرر.</li>
  <li><strong>قالب مدمج وزن 125 جم:</strong> يدوم طويلاً ويضمن نظافة وحماية متواصلة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل):</strong> بلي الصابون والجسم أو اليدين بالماء الفاتر.</li>
  <li><strong>الخطوة الثانية (الفرك):</strong> افركي صابون لايفبوي بين اليدين لتوليد رغوة غنية ودلكي الجلد لمدة 10 ثوانٍ على الأقل.</li>
  <li><strong>الخطوة الثالثة (الشطف):</strong> اشطفي بالماء الفاتر جيداً واستمتعي بحماية وانتعاش تام.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>جزيئات الفضة النشطة (Activ Silver):</strong> تخترق جدار البكتيريا وتقتلها بفاعلية.</li>
  <li><strong>عوامل تنظيف ناعمة مرطبة:</strong> تنظف الجلد وتمنع الجفاف.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على اليدين والجسم فقط.</li>
  <li>تجنبي ملامسة الصابون المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل العائلات والأفراد الراغبين في صابون طبي يوفر حماية 99.9% ضد البكتيريا والجراثيم.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لايفبوي (Lifebuoy)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / صابون غسيل اليدين والجسم المضاد للجراثيم</td></tr>
  <tr><th>نوع المنتج</th><td>صابون طبي مضاد للجراثيم وتقنية الفضة النشطة (125g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>125 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (اليدين والجسم)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة نظيفة، معقمة، محمية بنسبة 99.9% ومنتعشة</td></tr>
  <tr><th>الملمس</th><td>قالب صابون صلب يرغي بكثافة ناعمة</td></tr>
  <tr><th>العطر</th><td>عطر النظافة والتعقيم الطبيعي من لايفبوي</td></tr>
  <tr><th>المكونات النشطة</th><td>تقنية الفضة النشطة (Activ Silver)، عوامل مطهرة</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الإمارات (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (لايفبوي)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لتقنية الفضة النشطة والحماية من الجراثيم (Lifebuoy)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يحلم صابون لايفبوي المتكامل مشكلة تراكم البكتيريا والميكروبات الضارة على اليدين والجسم وانتقال العدوى بالأمراض.</p>

<h3>لماذا تنجح تقنية الفضة النشطة؟</h3>
<p>لأن جزيئات الفضة النشطة تخترق جدار الخلايا البكتيرية وتوقف تكاثرها في 10 ثوانٍ فقط، مما يمنح حماية 99.9% مستمرة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>غسل اليدين 20 ثانية:</strong> افركي اليدين بالصابون والماء 20 ثانية قبل الأكل وبعد استخدام التواليت.<br>
2. <strong>الحفظ على صحن صابون جاف:</strong> احفظي قالب الصابون في صحن صابون مصفى للماء لمنع ذوبانه.<br>
3. <strong>الاستخدام العائلي اليومي:</strong> اجعلي غسيل اليدين بلايفبوي روتيناً يومياً للأطفال.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الصابون المضاد للجراثيم يسبب جفاف البشرة."<br>
<strong>الحقيقة:</strong> صابون لايفبوي يحتوي على مرطبات تحافظ على نعومة الجلد وتمنع الجفاف أثناء التعقيم.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتفاعل أيونات الفضة النشطة (Activ Silver Ions) مع إنزيمات البكتيريا الحيوية، مما يعطل غشاء الجدار الخلوي للبكتيريا ويقضي عليها بنسبة 99.9%.</p>"""

    faqs = [
        ("ما هو صابون لايفبوي المتكامل 10 للحماية من الجراثيم 125 جم؟", "هو قالب صابون طبي مضاد للجراثيم يقتل 99.9% من البكتيريا والميكروبات في 10 ثوانٍ بتقنية الفضة النشطة."),
        ("ما هي تقنية الفضة النشطة (Activ Silver)؟", "هي تقنية متطورة تخترق البكتيريا وتوفر درع حماية مستمر ضد الأمراض والعدوى."),
        ("هل يقتل 99.9% من الجراثيم؟", "نعم، مثبت سريرياً في القضاء على 99.9% من البكتيريا والجراثيم في 10 ثوانٍ فقط."),
        ("ما حجم قالب الصابون؟", "يأتي بحجم 125 جم."),
        ("هل يناسب غسل اليدين والجسم معاً؟", "نعم، ممتاز لتعقيم اليدين واستحمام الجسم اليومي."),
        ("هل يناسب جميع أفراد العائلة؟", "نعم، صابون عائلي آمن للأطفال والبالغين من سن 3 سنوات."),
        ("ما هو بلد صنع صابون لايفبوي؟", "صُنع بواسطة شركة يونيلفر (Unilever) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات لايفبوي لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يسبب جفاف الجلد؟", "يحتوي على مرطبات تحمي البشرة من الجفاف أثناء التعقيم."),
        ("ما هي رائحة صابون لايفبوي المتكامل؟", "يتميز برائحة النظافة والانتعاش الطبيعية المميزة للايفبوي."),
        ("هل يرغي بشكل ممتاز؟", "نعم، يولد رغوة كثيفة تنظف وتطهر البشرة بسرعة."),
        ("كيف أحتفظ بقالب الصابون؟", "يُحفظ في صحن صابون مصفى للماء ليجف بعد كل استخدام."),
        ("هل يساعد في الوقاية من نزلات البرد والعدوى؟", "نعم، غسل اليدين المنتظم بلايفبوي يحد من انتشار الجراثيم والعدوى."),
        ("هل يناسب الاستخدام المتكرر يومياً؟", "نعم، آمن وممتاز للاستخدام المتكرر طوال اليوم."),
        ("هل يزيل روائح العرق والطبخ من اليدين؟", "نعم، يقضي على البكتيريا المسببة للرائحة يترك اليدين منتعشتين."),
        ("هل القالب صلب ولا يذوب بسرعة؟", "قالب متين يصمد مع الاستخدام التكراري."),
        ("هل العبوة غلافها محكم؟", "تأتي في عبوة مغلفة طبقاً لأعلى المعايير الصحية."),
        ("هل يناسب البشرة الحساسة؟", "تركيبة مجربة جلدياً ومناسبة لغالبية أنواع البشرة."),
        ("كم مدة الفرك الموصى بها؟", "يُوصى بفرك اليدين لمدة 10 إلى 20 ثانية بالرغوة."),
        ("هل يناسب المدارس والمكاتب؟", "ممتاز للاستخدام بالمنزل، المدارس، والمكاتب للحماية."),
        ("هل يساعد في تنظيف الدهون والأوساخ؟", "نعم، يزيل الزيوت والأوساخ فورياً."),
        ("هل يحتوي على مواد ضارة؟", "خالي من المواد الكيميائية المحظورة ومصرح به صحياً."),
        ("هل يتوفر بأحجام أخرى لدى إكليل أبها؟", "نعم، تتوفر عبوات ومقاسات صابون وغسول لايفبوي متعددة."),
        ("هل يترك ملمساً معقماً ونظيفاً؟", "نعم، يمنح إحساساً بالنظافة والتعقيم الفائق."),
        ("هل هو خيار اقتصادي للعائلة؟", "نعم، يوفر حماية مضاعفة بسعر ممتاز.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Lifebuoy Complete Soap 10, 125g</strong> is the world's #1 trusted germ protection soap bar engineered to deliver 99.9% protection against harmful bacteria and illness-causing germs. Powered by advanced Activ Silver Formula, it cleanses deeply and kills germs in just 10 seconds.</p>
<p>Lifebuoy Complete 10 features a rich, soothing lather that leaves your family's hands and skin thoroughly sanitized, refreshed, and protected against bacterial recontamination without causing skin dryness or tightness.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>99.9% Germ & Bacteria Protection:</strong> Clinically proven to destroy illness-causing germs in just 10 seconds.</li>
  <li><strong>Activ Silver Formula Technology:</strong> Delivers an advanced protective shield for hours after washing.</li>
  <li><strong>Deep Cleansing & Instant Refreshment:</strong> Sweeps away dirt, excess oil, sweat, and microbes from pores.</li>
  <li><strong>Rich Creamy Lather:</strong> Cleanses skin thoroughly while preserving natural dermal moisture.</li>
  <li><strong>Ideal Family Hygiene Choice:</strong> Safe antibacterial bar soap for daily handwashing and bathing.</li>
  <li><strong>Durable 125g Bar:</strong> Long-lasting bar ensuring continuous germ protection for your home.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet bar soap and hands/body with warm water.</li>
  <li><strong>Step 2 (Lather):</strong> Rub Lifebuoy soap bar between hands to create a rich lather and massage skin for at least 10 seconds.</li>
  <li><strong>Step 3 (Rinse):</strong> Rinse thoroughly with warm water for complete germ protection.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Activ Silver Particles:</strong> Penetrate bacterial cell walls to eliminate microbes rapidly.</li>
  <li><strong>Gentle Moisturizing Cleansers:</strong> Cleanse skin while preventing dry tightness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external hand and body cleansing only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Families and individuals seeking 99.9% trusted antibacterial germ protection for hands and body.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lifebuoy</td></tr>
  <tr><th>Category</th><td>Personal Care / Antibacterial Soap Bars</td></tr>
  <tr><th>Product Type</th><td>Antibacterial Soap Bar with Activ Silver Tech (125g)</td></tr>
  <tr><th>Volume/Weight</th><td>125 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Hands & Body)</td></tr>
  <tr><th>Finish</th><td>Clean, sanitized, 99.9% protected & refreshed skin</td></tr>
  <tr><th>Texture</th><td>Solid bar soap producing rich lather</td></tr>
  <tr><th>Fragrance</th><td>Clean, refreshing natural Lifebuoy hygienic scent</td></tr>
  <tr><th>Active Ingredients</th><td>Activ Silver Formula, Antibacterial Agents</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / UAE (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever (Lifebuoy)</td></tr>
  <tr><th>Age Group</th><td>All Ages (3+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Activ Silver Technology & 10-Second Germ Protection</h2>

<h3>What problem does this solve?</h3>
<p>Lifebuoy Complete 10 Soap Bar resolves bacterial accumulation, disease transmission, and inadequate hand sanitization.</p>

<h3>Why choose Lifebuoy Activ Silver?</h3>
<p>Activ Silver particles breach bacterial cell membranes within 10 seconds, eliminating 99.9% of microbes and offering long-lasting protection.</p>"""

    en_faqs = [
        ("What is Lifebuoy Complete Soap 10, 125g?", "It is an antibacterial soap bar formulated with Activ Silver technology to kill 99.9% of germs in 10 seconds."),
        ("What is Activ Silver technology?", "It is an advanced silver particle formula that breaches bacterial membranes for fast germ elimination."),
        ("Does it kill 99.9% of germs?", "Yes, clinically proven to eliminate 99.9% of bacteria and germs in 10 seconds."),
        ("What volume is contained in this soap bar?", "It comes as a 125g soap bar."),
        ("Is it safe for both handwashing and body bathing?", "Yes, excellent for daily hand sanitization and body bathing."),
        ("Is it suitable for the entire family?", "Yes, safe for adults and children aged 3+."),
        ("Where is Lifebuoy manufactured?", "It is produced by Unilever following global hygiene standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Lifebuoy products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it dry out skin?", "It contains gentle moisturizers to prevent skin dryness."),
        ("What fragrance does it have?", "Features a clean, refreshing hygienic signature scent."),
        ("Does it produce a rich lather?", "Yes, lathers easily into a rich creamy foam."),
        ("How should I store the soap bar?", "Store on a draining soap dish so it dries between uses."),
        ("Does it help prevent cold and flu transmission?", "Yes, regular handwashing with Lifebuoy reduces germ spread."),
        ("Is it safe for multiple daily uses?", "Yes, safe for frequent daily handwashing."),
        ("Does it eliminate kitchen and sweat odors?", "Yes, eliminates odor-causing bacteria leaving hands fresh."),
        ("Is the soap bar durable?", "Yes, solid formulation holds up well during frequent use."),
        ("Is the packaging hygienic?", "Yes, sealed in hygienic protective wrapping."),
        ("Is it suitable for sensitive skin?", "Dermatologically tested for general skin compatibility."),
        ("What is the recommended lather time?", "Rub hands with lather for 10 to 20 seconds."),
        ("Is it great for schools and offices?", "Yes, ideal for home, school, and workplace hand hygiene."),
        ("Does it strip oil and dirt effectively?", "Yes, removes grease, dirt, and microbes instantly."),
        ("Does it contain harmful additives?", "Free from banned chemicals and health-certified."),
        ("Are other sizes available at Ekleel Abha?", "Yes, Ekleel Abha offers various Lifebuoy soap and body wash sizes."),
        ("Does it leave a sterile clean feeling?", "Yes, imparts an instant feeling of clean, sanitized protection."),
        ("Is it economical for family budgets?", "Yes, offers reliable 99.9% protection at an affordable price.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1778",
        "sku": "EK-1778",
        "gtin": "6281006483644",
        "category": "العناية الشخصية / صابون غسيل اليدين والجسم المضاد للجراثيم",
        "brand": "Lifebuoy",
        "ar": {
            "title": "صابون لايفبوي المتكامل 10 للحماية من الجراثيم - 125 جم",
            "meta_title": "صابون لايفبوي المتكامل 10 125جم | صيدلية إكليل أبها",
            "meta_description": "اشتري صابون لايفبوي المتكامل 10 للحماية من الجراثيم (125 جم). تقنية الفضة النشطة لقضاء على 99.9% من البكتيريا في 10 ثوانٍ. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["لايفبوي", "صابون_لايفبوي", "حماية_الجراثيم", "الفضة_النشطة", "إكليل_أبها"]
        },
        "en": {
            "title": "Lifebuoy Complete Soap 10, 125g",
            "meta_title": "Lifebuoy Complete Soap 10 125g | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Lifebuoy Complete Soap 10 (125g). Kills 99.9% of germs in 10 seconds with Activ Silver Tech. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["lifebuoy", "antibacterial_soap", "activ_silver", "germ_protection", "ekleel_abha"]
        },
        "schema": {
            "brand": "Lifebuoy",
            "category": "Personal Care / Soap Bar",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "lifebuoy-complete-soap-10-125g.webp",
            "alt": "Lifebuoy Complete Soap 10 125g",
            "title": "Lifebuoy Complete Soap 10 125g"
        }
    }

def create_product_1780():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم تصفيف الشعر صنسيلك شاين اند سترينث لقوة ولمعان الشعر - 275 مل (Sunsilk Shine & Strength Hair Styling Cream 275ml)</strong> كريم التصفيف الأساسي والأرقى لإعادة القوة واللمعان وتسهيل تسريح الشعر المجهد والمتطاير. صُمم هذا المستحضر الغني من صنسيلك بالتعاون مع خبراء الشعر العالمييين، حيث يرتكز على تركيبة السيروم المغذي والحماية من الحرارة لمنح خصلات الشعر حيوية فائقة وبريقاً كريستالياً يرفع من جمال التسريحة طوال اليوم.</p>
<p>يمتاز كريم صنسيلك بقوام كريمي ناعم يتغلغل في ألياف الشعر ليمنع الهيشان، يفك التشابك فورياً، ويغلف الخصلات بحجاب واقٍ يعزز قوة الشعر ضد التكسر والإجهاد الحراري دون ترك ملمس دهني ثقيل.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>قوة ولمعان كريستالي للشعر:</strong> يعيد القوة والحيوية للشعر الضعيف ويمنحه بريقاً لافتاً.</li>
  <li><strong>السيطرة التامة على الهيشان:</strong> يلين خصلات الشعر المتطايرة ويمنع تأثير الرطوبة طوال اليوم.</li>
  <li><strong>سهولة الفك والتصفيف:</strong> ينزلق المشط بسلاسة دون تسبب في تقصف أو تكسر الخصلات.</li>
  <li><strong>حماية ضد الحرارة والإجهاد:</strong> يغلف الشعر بحجاب واقٍ من حرارة السيشوار والطقس الجاف.</li>
  <li><strong>قوام كريمي غير دهني:</strong> يمتص فورياً في الشعر دون إثقال الرأس أو ترك لزوجة.</li>
  <li><strong>عبوة وافرة سعة 275 مل:</strong> حجم ممتاز يضمن تصفيفاً وتغذية مستمرة يومياً.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق):</strong> وضعي كمية بحجم حبة الجوز من كريم صنسيلك على كف اليد بعد غسل الشعر وترطيبه خفيفاً.</li>
  <li><strong>الخطوة الثانية (التوزيع):</strong> وزعي الكريم بالتساوي على طول الشعر وحتى الأطراف (تجنبي الجذور المباشرة).</li>
  <li><strong>الخطوة الثالثة (التصفيف):</strong> صففي شعركِ بالمشط أو الاستشوار واستمتعي بقوة ولمعان مذهل.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>سيروم دوڤ وصنسيلك المغذي:</strong> يعيد توازن الترطيب ويمنح بريقاً لافتاً.</li>
  <li><strong>زيوت تنعيم طبيعية:</strong> تغلف خصلات الشعر وتمنع الهيشان والتكسر.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الشعر فقط.</li>
  <li>تجنبي ملامسة كريم الشعر المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من الشعر الضعيف، الباهت، المتطاير، والمجهد وتفتش عن كريم تصفيف بقوة ولمعان صنسيلك.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>صنسيلك (Sunsilk)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / كريمات تصفيف وقوة الشعر</td></tr>
  <tr><th>نوع المنتج</th><td>كريم تصفيف لقوة ولمعان الشعر (Shine & Strength Cream)</td></tr>
  <tr><th>الحجم/الوزن</th><td>275 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>الشعر الضعيف، الباهت، والمتطاير</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر قوي، لامع، مصفف بعناية، وخالٍ من الهيشان</td></tr>
  <tr><th>الملمس</th><td>كريمي ناعم سريع الامتصاص غير دهني</td></tr>
  <tr><th>العطر</th><td>عطر صنسيلك الزهري المنعش الفواح</td></tr>
  <tr><th>المكونات النشطة</th><td>سيروم التغذية واللمعان، مرطبات ألياف الشعر</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الإمارات (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (صنسيلك)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 10 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد السيروم وقوة الشعر (Sunsilk Shine & Strength)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم صنسيلك قوة ولمعان مشكلة هيشان الشعر الباهت، التكتل والتكسر أثناء التمشيط، وفقدان البريق الطبيعي.</p>

<h3>لماذا تنجح تركيبته؟</h3>
<p>لأن السيروم المغذي يكسو الألياف القشرية للشعرة بغلاف مرن يمنع الهيشان ويعكس الضوء لبريق كريستالي.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التوزيع بالتساوي:</strong> وزعي الكريم من المنتصف إلى الأطراف على شعر رطب خفيفاً.<br>
2. <strong>الحماية من الاستشوار:</strong> وضعي الكريم قبل التجفيف بالحرارة لحماية الأطراف.<br>
3. <strong>استخدام كمية مناسبة:</strong> كمية بحجم حبة الجوز تكفي لتصفيف الشعر بالكامل.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات التصفيف تسبب تساقط الشعر وثقله."<br>
<strong>الحقيقة:</strong> كريم صنسيلك خفيف جداً ويمتص دون ترك أثر زيتي أو سد لمسام الفروة عند تجنب الجذور.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تقوم البوليمرات المرنة والمرطبات بتنعيم طبقة حراشف الشعرة (Cuticles)، مما يقلل الاحتكاك الميكانيكي ويزيد انعكاس الضوء للبريق.</p>"""

    faqs = [
        ("ما هو كريم تصفيف الشعر صنسيلك شاين اند سترينث 275 مل؟", "هو كريم تصفيف غني يمنح الشعر القوة واللمعان الكريستالي، يمنع الهيشان ويسهل التمشيط دون أثر دهني."),
        ("ما هي فوائد سيروم اللمعان والقوة من صنسيلك؟", "يعيد الحيوية والبريق للشعر الضعيف والباهت ويغلف الألياف لحمايتها من التكسر."),
        ("هل يساعد في السيطرة على هيشان الشعر؟", "نعم، يلين الخصلات المتطايرة ويحميها من الهيشان بفعل الرطوبة."),
        ("ما حجم العبوة؟", "تأتي العبوة بحجم وافر يبلغ 275 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي كمية مناسبة على شعر رطب أو جاف من المنتصف حتى الأطراف ثم صففي بالمشط."),
        ("هل يترك ملمساً زيتيّاً ثقيلاً؟", "لا، كريم ناعم يمتص فورياً دون إثقال الشعر أو لزوجة."),
        ("ما هو بلد صنع كريم صنسيلك؟", "صُنع بواسطة شركة يونيلفر (Unilever) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات صنسيلك لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يساعد في حماية الشعر من الحرارة؟", "نعم، يشكل حجاب ترطيب يقي الشعر من حرارة الاستشوار."),
        ("ما هي رائحة الكريم؟", "يتميز برائحة صنسيلك الزهرية المنعشة التي تدوم طوال اليوم."),
        ("هل يناسب جميع أنواع الشعر؟", "مناسب جداً للشعر الضعيف، الجاف، الباهت، والمتطاير."),
        ("هل يمكن استخدامه يومياً؟", "نعم، آمن وممتاز للاستخدام والتصفيف اليومي."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب لتصفيف شعر الرجال والنساء."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل يسهل فك تشابك الشعر المجهد؟", "نعم، يجعل المشط ينزلق بسلاسة ويمنع التكسر."),
        ("هل العبوة 275 مل اقتصادية؟", "نعم، توفر استمالاً مستمراً لأشهر طويلة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة أنيقة بضغط يدوي محكم يسهل الاستخدام."),
        ("هل يناسب الشعر الكيرلي؟", "نعم، يحدد تموجات الكيرلي ويمنع هيشانه."),
        ("هل يحتوي على بارابين؟", "تركيبة مجربة ومطورة طبقاً لأعلى معايير الأمان."),
        ("هل يمنح بريقاً كريستالياً؟", "نعم، يمنح الشعر لمعاناً صحياً لافتاً."),
        ("هل يناسب المراهقين والأطفال؟", "مناسب للأطفال والبالغين من سن 10 سنوات فما فوق."),
        ("هل يلزم غسله فوراً؟", "لا، كريم تصفيف يُترك على الشعر (Leave-in)."),
        ("هل ينشط حيوية الشعر المصبوغ؟", "نعم، يعيد البريق والنعومة للشعر المسبوغ."),
        ("هل يمنع تقصف الأطراف؟", "نعم، تغليف الأطراف يمنع تقصفها أثناء التمشيط."),
        ("هل هو خيار ممتاز للروتين اليومي؟", "نعم، كريم التصفيف الأول لثبات ونعومة الشعر يومياً.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Sunsilk Shine & Strength Hair Styling Cream 275ml</strong> is the premier leave-in conditioning styling cream engineered to restore strength, brilliant crystal shine, and effortless combability to weak or frizzy hair. Developed in collaboration with international hair experts, it combines a nutritive shine serum with heat-protective conditioners.</p>
<p>Sunsilk Shine & Strength absorbs instantly into hair cuticles, taming unruly frizz, untangling stubborn knots, and forming a lightweight shield that protects strands against friction breakage and thermal styling damage without feeling greasy.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Crystal Shine & Hair Strength:</strong> Restores vitality to dull, weak hair while imparting brilliant shine.</li>
  <li><strong>Complete Frizz Control:</strong> Smooths flyaways and shields hair strands against humidity all day.</li>
  <li><strong>Effortless Detangling & Styling:</strong> Enables combs to glide snag-free to reduce friction breakage.</li>
  <li><strong>Heat & Weather Protection:</strong> Shields hair from blow-drying heat and dry ambient weather.</li>
  <li><strong>Lightweight Non-Greasy Formula:</strong> Absorbs instantly without weighing down styles or leaving sticky residue.</li>
  <li><strong>Generous 275ml Bottle:</strong> Excellent value bottle ensuring daily styling and nourishment.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply):</strong> Rub a walnut-sized amount of Sunsilk Shine & Strength cream between palms after washing hair.</li>
  <li><strong>Step 2 (Distribute):</strong> Smooth evenly through damp or dry hair from mid-lengths to ends (avoid roots directly).</li>
  <li><strong>Step 3 (Style):</strong> Style hair with a comb or blow-dryer to achieve brilliant, strong results.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Nutritive Shine Serum:</strong> Rebalances hair moisture and imparts high crystal gloss.</li>
  <li><strong>Natural Smoothing Emollients:</strong> Coat hair strands to stop friction breakage and humidity frizz.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external hair application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with weak, dull, or frizzy hair seeking a leave-in hair styling cream for strength and shine.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Sunsilk</td></tr>
  <tr><th>Category</th><td>Hair Care / Hair Styling & Leave-in Creams</td></tr>
  <tr><th>Product Type</th><td>Leave-in Shine & Strength Hair Styling Cream</td></tr>
  <tr><th>Volume/Weight</th><td>275 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Weak, Dull, Frizzy & Unruly Hair</td></tr>
  <tr><th>Finish</th><td>Strong, shiny, manageable & frizz-free hair</td></tr>
  <tr><th>Texture</th><td>Lightweight fast-absorbing smooth cream</td></tr>
  <tr><th>Fragrance</th><td>Fresh Sunsilk floral fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Nutritive Shine Serum, Smoothing Emollients</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / UAE (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever (Sunsilk)</td></tr>
  <tr><th>Age Group</th><td>All Ages (10+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Cuticle Smoothing & Nutritive Shine Serums</h2>

<h3>What problem does this solve?</h3>
<p>Sunsilk Shine & Strength Cream resolves dull hair frizz, comb snagging, and thermal styling breakage.</p>

<h3>Why choose Sunsilk?</h3>
<p>Nutritive shine serum coats the outer cuticles, reducing mechanical friction during combing and reflecting light for crystal gloss.</p>"""

    en_faqs = [
        ("What is Sunsilk Shine & Strength Hair Styling Cream 275ml?", "It is a leave-in hair styling cream enriched with shine serum to impart strength, crystal gloss, and frizz control."),
        ("What are the benefits of Sunsilk Shine Serum?", "It restores vitality and gloss to dull hair while fortifying strands against breakage."),
        ("Does it control frizz effectively?", "Yes, smooths unruly flyaways and protects against humidity all day."),
        ("What volume is contained in this bottle?", "It comes in a generous 275ml bottle."),
        ("How do I use it correctly?", "Smooth a small amount through damp or dry hair from mid-lengths to ends and style."),
        ("Does it leave a heavy greasy residue?", "No, it absorbs quickly leaving hair light and non-sticky."),
        ("Where is Sunsilk manufactured?", "It is produced by Unilever following global quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Sunsilk products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it protect hair against heat styling?", "Yes, forms a moisture shield protecting strands against blow-drying heat."),
        ("What fragrance does it have?", "Features a fresh, uplifting Sunsilk floral scent."),
        ("Is it suitable for all hair types?", "Ideal for weak, dull, dry, and frizzy hair types."),
        ("Is it safe for daily styling?", "Yes, safe and recommended for daily leave-in styling."),
        ("Can both men and women use it?", "Yes, suitable for both men and women."),
        ("How should I store the bottle?", "Store in a cool, dry place away from heat."),
        ("Does it ease hair detangling?", "Yes, allows combs to glide smoothly without pulling or snapping strands."),
        ("Is the 275ml bottle economical?", "Yes, provides months of daily leave-in styling."),
        ("Is the bottle easy to dispense?", "Yes, comes in a squeeze bottle with a secure cap."),
        ("Is it suitable for curly hair?", "Yes, defines natural curls and tames frizz."),
        ("Is it paraben-free?", "Dermatologically tested under high European standards."),
        ("Does it impart crystal shine?", "Yes, leaves hair with a healthy, vibrant crystal gloss."),
        ("Is it safe for teenagers?", "Safe for adults and teens aged 10+."),
        ("Does it require rinsing?", "No, it is a leave-in hair cream."),
        ("Does it revive color-treated hair?", "Yes, restores shine and softness to color-treated hair."),
        ("Does it prevent split ends?", "Yes, strand coating guards ends against friction splitting."),
        ("Is it a reliable daily styling choice?", "Yes, the #1 choice for daily smooth, shiny hair styling.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1780",
        "sku": "EK-1780",
        "gtin": "6281006547322",
        "category": "العناية بالشعر / كريمات تصفيف وقوة الشعر",
        "brand": "Sunsilk",
        "ar": {
            "title": "كريم تصفيف الشعر صنسيلك شاين اند سترينث لقوة ولمعان الشعر - 275 مل",
            "meta_title": "كريم صنسيلك قوة ولمعان 275مل | صيدلية إكليل أبها",
            "meta_description": "اشتري كريم تصفيف الشعر صنسيلك شاين اند سترينث (275 مل). لقوة ولمعان الشعر ومنع الهيشان. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["صنسيلك", "كريم_صنسيلك", "قوة_ولمعان", "تصفيف_الشعر", "إكليل_أبها"]
        },
        "en": {
            "title": "Sunsilk Shine & Strength Hair Styling Cream 275ml",
            "meta_title": "Sunsilk Shine & Strength Hair Styling Cream 275ml | Ekleel Abha",
            "meta_description": "Buy original Sunsilk Shine & Strength Hair Styling Cream (275ml). Leave-in shine serum for strong, frizz-free hair. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["sunsilk", "shine_strength", "hair_styling_cream", "frizz_control", "ekleel_abha"]
        },
        "schema": {
            "brand": "Sunsilk",
            "category": "Hair Care / Hair Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "sunsilk-shine-and-strength-hair-styling-cream-275ml.webp",
            "alt": "Sunsilk Shine and Strength Hair Styling Cream 275ml",
            "title": "Sunsilk Shine and Strength Hair Styling Cream 275ml"
        }
    }

def create_product_1781():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم تصفيف الشعر صنسيلك بزيت جوز الهند 275 مل لترطيب ونعومة فائقة (Sunsilk Hair Styling Cream with Coconut Oil - 275ml)</strong> الحل التجميلي الأمثل والأرغد لترطيب وتنعيم الشعر الجاف والمجعد والخشن. يعتمد هذا المستحضر الفاخر من صنسيلك على خلطة زيت جوز الهند الطبيعي (Natural Coconut Oil) المتطورة، حيث ينفذ إلى ألياف الشعرة الداخلية ليمنحها مرونة ونعومة حريرية تمنع الهيشان وتسهل تصفيف الشعر طوال اليوم.</p>
<p>يمتاز كريم صنسيلك بجوز الهند بقوام خفيف سريع الامتصاص يغلف خصلات الشعر بغشاء ترطيب واقٍ، مما يمنح شعركِ مظهراً متألقاً، ناعماً كالحرير، برائحة استوائية فواحة تدوم طويلاً دون ترك لزوجة أو ثقل.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب ونعومة فائقة بزيت جوز الهند:</strong> يغذي خصلات الشعر الجاف والمجهد بالمرطبات الطبيعية.</li>
  <li><strong>السيطرة التامة على الهيشان والتجعد:</strong> يلين الخصلات القاسية والمجعدة ويمنع تأثير الرطوبة.</li>
  <li><strong>تسهيل التمشيط وتفكيك التشابك:</strong> يجعل المشط ينزلق بسلاسة ويحمي الشعر من التقصف والتكسر.</li>
  <li><strong>حماية ضد الجفاف والإجهاد البيئي:</strong> يكسو ألياف الشعر بحجاب واقٍ يعيد إليها البريق واللمعان.</li>
  <li><strong>قوام كريمي خفيف وسريع الامتصاص:</strong> يغذي الشعر دون إثقال الرأس أو ترك طبقة دهنية لزجة.</li>
  <li><strong>عبوة وافرة سعة 275 مل:</strong> حجم ممتاز يدوم طويلاً للعناية والتصفيف اليومي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق):</strong> افركي كمية مناسبة من كريم صنسيلك بجوز الهند بين الكفين على شعر نظيف ورطب خفيفاً أو جاف.</li>
  <li><strong>الخطوة الثانية (التوزيع):</strong> وزعي الكريم بالتساوي على طول الشعر وحتى الأطراف.</li>
  <li><strong>الخطوة الثالثة (التصفيف):</strong> صففي شعركِ بالأسلوب المفضل واستمتعي بنعومة وترطيب استثنائي.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت جوز الهند الطبيعي (Natural Coconut Oil):</strong> يمتص بسرعة ليغذي ويرطب ألياف الشعر الجاف.</li>
  <li><strong>مرطبات ناعمة لحماية الكيراتين:</strong> تغلف الخصلات وتمنع جفاف الأطراف.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الشعر فقط.</li>
  <li>تجنبي ملامسة كريم الشعر المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من الشعر الجاف، الخشن، والمجعد وتفتش عن كريم تصفيف مغذٍ بزيت جوز الهند لترطيب فائق.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>صنسيلك (Sunsilk)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / كريمات تصفيف وترطيب الشعر الجاف</td></tr>
  <tr><th>نوع المنتج</th><td>كريم تصفيف الشعر بزيت جوز الهند (Coconut Oil Cream)</td></tr>
  <tr><th>الحجم/الوزن</th><td>275 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>الشعر الجاف، المجعد، الخشن، والمجهد</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم، حريري، مرطب، مصفف بعناية وبدون هيشان</td></tr>
  <tr><th>الملمس</th><td>كريمي غني سريع الامتصاص غير دهني</td></tr>
  <tr><th>العطر</th><td>عطر جوز الهند الاستوائي المنعش والزكي</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت جوز الهند الطبيعي، مرطبات ألياف الشعر</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الإمارات (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (صنسيلك)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 6 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت جوز الهند لتصفيف الشعر (Sunsilk Coconut)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم صنسيلك بجوز الهند مشكلة خشونة وجفاف الشعر، الهيشان عند الرطوبة، وتشابك الخصلات أثناء التصفيف.</p>

<h3>لماذا ينجح زيت جوز الهند في التصفيف؟</h3>
<p>لأن جزيئات زيت جوز الهند تنفذ داخل قشرة الشعرة لترطيبها، بينما تشكل طبقة حماية سطحية تمنع تبخر الماء وتمنع الهيشان.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التوزيع على شعر رطب:</strong> يُفضل توزيع الكريم على شعر رطب بعد الغسيل لامتصاص أسرع.<br>
2. <strong>التركيز على الأطراف:</strong> ركزي الكريم على الأطراف الجافة لمنع التكسر.<br>
3. <strong>التصفيف اليومي:</strong> استخدميه يومياً لتسهيل التمشيط وتثبيت النعومة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريم جوز الهند يجعل الشعر زيتياً وجاذباً للغبار."<br>
<strong>الحقيقة:</strong> كريم صنسيلك صُمم بتركيبة متوازنة سريعة الامتصاص تمنح النعومة دون لزوجة دهنية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتكامل حمض اللوريك الموجود بزيت جوز الهند مع بروتينات ألياف الشعر، مما يرطب الداخلية ويعيد مرونة الخصلات لمنع التقصف.</p>"""

    faqs = [
        ("ما هو كريم تصفيف الشعر صنسيلك بزيت جوز الهند 275 مل؟", "هو كريم تصفيف مغذٍ غني بزيت جوز الهند الطبيعي يمنح الشعر الجاف والمجعد ترطيباً ونعومة فائقة ويمنع الهيشان."),
        ("ما هي فوائد زيت جوز الهند لتصفيف الشعر؟", "يغذي ألياف الشعر بالمرطبات الطبيعية، يلين الخصلات القاسية، ويمنح لمعاناً حريرياً."),
        ("هل يسيطر على هيشان وتجعد الشعر؟", "نعم، يحمي الشعر من التأثر برطوبة الجو ويقضي على الهيشان طوال اليوم."),
        ("ما حجم العبوة؟", "تأتي العبوة بحجم وافر سعة 275 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي كمية منا سبة على شعر رطب أو جاف من المنتصف وحتى الأطراف ثم صففي بمرونة."),
        ("هل يترك أثراً دهنياً ثقيلاً؟", "لا، يمتص بسرعة ليعطي ملمساً ناعماً وحريرياً دون ثقل زيتي."),
        ("ما هو بلد صنع كريم صنسيلك؟", "صُنع بواسطة شركة يونيلفر (Unilever) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات صنسيلك لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يسهل فك تشابك الشعر الجاف؟", "نعم، ينعم الشعر ويسهل مرور المشط دون شد أو تقصف."),
        ("ما هي رائحة كريم صنسيلك بجوز الهند؟", "يتميز برائحة جوز الهند الاستوائية الفواحة والمنعشة."),
        ("هل يناسب الشعر الكيرلي والمجعد؟", "ممتاز جداً لتحديد تموجات الشعر الكيرلي وتليين خصلاته."),
        ("هل يمكن استخدامه يومياً؟", "نعم، آمن وممتاز للاستخدام والتصفيف اليومي."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب لتصفيف شعر الرجال والنساء."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل يناسب الأطفال؟", "مناسب للأطفال والبالغين من سن 6 سنوات فما فوق."),
        ("هل العبوة 275 مل اقتصادية؟", "نعم، تكفي للاستخدام اليومي المستمر لأشهر طويلة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة أنيقة بضغط يدوي محكم يمنع التسرب."),
        ("هل يحمي الشعر من الجفاف في الصيف؟", "نعم، يغلف الخصلات ويحميها من الجفاف والتأثيرات البيئية."),
        ("هل يحتوي على بارابين؟", "تركيبة مجربة ومطورة طبقاً لأعلى معايير السلامة."),
        ("هل يعالج الأطراف المتقصفة؟", "نعم، يغذي وينعم الأطراف الجافة المتقصفة."),
        ("هل ينصح به للشعر المصبوغ؟", "نعم، يعوض الشعر المصبوغ عن الرطوبة والزيوت المفقودة."),
        ("هل يلزم غسله بالماء؟", "لا، كريم تصفيف يُترك على الشعر (Leave-in)."),
        ("هل يمنح بريقاً كريستالياً؟", "نعم، يمنح الشعر لمعاناً طبيعياً ومظهراً صحياً."),
        ("هل يساعد في حماية الشعر أثناء التمشيط؟", "نعم، يمنع التكسر الناجم عن احتكاك المشط."),
        ("هل هو خيار ممتاز للروتين اليومي؟", "نعم، كريم التصفيف الأول لترطيب ونعومة الشعر يومياً.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Sunsilk Hair Styling Cream with Coconut Oil - 275ml</strong> is an intensive leave-in moisturising hair cream formulated to bring extreme softness, deep hydration, and smooth manageability to dry, frizzy, or coarse hair textures. Enriched with natural Virgin Coconut Oil, it penetrates hair fibers to replenish essential lipids.</p>
<p>Featuring a lightweight, fast-absorbing texture, Sunsilk Coconut Oil Cream coats hair strands with a protective humidity barrier, leaving your hair touchably silky, smooth, and beautifully scented with tropical coconut all day long without feeling greasy.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Extreme Softness & Coconut Moisture:</strong> Deeply nourishes dry, coarse hair strands with natural lipids.</li>
  <li><strong>Total Frizz & Humidity Control:</strong> Smooths unruly flyaways and resists environmental humidity all day.</li>
  <li><strong>Effortless Detangling & Combing:</strong> Enables wide-tooth combs to glide snag-free to prevent breakage.</li>
  <li><strong>Dryness & Weather Shield:</strong> Protects hair fibers against environmental drying and thermal stress.</li>
  <li><strong>Lightweight Fast-Absorbing Texture:</strong> Feeds hair without weighing down styles or leaving greasy residue.</li>
  <li><strong>Generous 275ml Tub:</strong> High-value tub providing long-lasting daily conditioning and styling.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply):</strong> Rub a suitable amount of Sunsilk Coconut Oil cream between palms after washing hair.</li>
  <li><strong>Step 2 (Distribute):</strong> Smooth evenly through damp or dry hair from mid-lengths to ends.</li>
  <li><strong>Step 3 (Style):</strong> Style hair as desired and enjoy touchable, silky soft hair.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Coconut Oil:</strong> Absorbs rapidly into the hair cortex to condition and restore moisture.</li>
  <li><strong>Softening Emollients:</strong> Coat cuticles to stop friction splitting and environmental dryness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external hair application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dry, coarse, frizzy, or curly hair seeking an intensive Coconut Oil leave-in styling cream.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Sunsilk</td></tr>
  <tr><th>Category</th><td>Hair Care / Hair Moisturizing & Styling Creams</td></tr>
  <tr><th>Product Type</th><td>Leave-in Coconut Oil Hair Moisturizing & Styling Cream</td></tr>
  <tr><th>Volume/Weight</th><td>275 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Dry, Coarse, Frizzy & Curly Hair</td></tr>
  <tr><th>Finish</th><td>Soft, silky, hydrated, manageable & frizz-free hair</td></tr>
  <tr><th>Texture</th><td>Rich fast-absorbing smooth cream</td></tr>
  <tr><th>Fragrance</th><td>Tropical Coconut fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Coconut Oil, Softening Emollients</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / UAE (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever (Sunsilk)</td></tr>
  <tr><th>Age Group</th><td>All Ages (6+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Coconut Oil Lipids & Hair Softening</h2>

<h3>What problem does this solve?</h3>
<p>Sunsilk Coconut Oil Hair Cream resolves severe hair dryness, coarse frizz, knotting, and splitting.</p>

<h3>Why choose Sunsilk Coconut?</h3>
<p>Coconut oil lipids penetrate deep into hair cortex gaps, restoring natural flexibility and forming a moisture barrier against humidity.</p>"""

    en_faqs = [
        ("What is Sunsilk Hair Styling Cream with Coconut Oil 275ml?", "It is an intensive leave-in moisturizing styling cream enriched with natural Coconut Oil to soften dry, frizzy hair."),
        ("What are the benefits of Coconut Oil for hair styling?", "It feeds hair fibers with natural lipids, softens coarse texture, and adds a silky gloss."),
        ("Does it control frizz and humidity?", "Yes, forms a protective shield resisting environmental humidity and stopping frizz."),
        ("What volume is contained in this tub?", "It comes in a generous 275ml tub."),
        ("How do I use it correctly?", "Smooth a small amount through damp or dry hair from mid-lengths to ends and style."),
        ("Does it leave a heavy greasy residue?", "No, it absorbs quickly leaving hair light, soft, and non-sticky."),
        ("Where is Sunsilk manufactured?", "It is produced by Unilever following global quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Sunsilk products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it ease detangling of dry hair?", "Yes, softens strands so combs glide smoothly without pulling."),
        ("What fragrance does it have?", "Features a delightful tropical Coconut scent."),
        ("Is it suitable for curly hair?", "Yes, defines natural curls and tames coarse frizz."),
        ("Is it safe for daily use?", "Yes, safe and recommended for daily leave-in styling."),
        ("Can both men and women use it?", "Yes, suitable for both men and women."),
        ("How should I store the tub?", "Store in a cool, dry place away from heat."),
        ("Is it safe for children?", "Safe for adults and kids aged 6+."),
        ("Is the 275ml tub economical?", "Yes, provides months of daily conditioning."),
        ("Is the bottle easy to dispense?", "Yes, comes in an easy-squeeze bottle with a secure cap."),
        ("Does it protect against summer dryness?", "Yes, coats strands to guard against sun and environmental dryness."),
        ("Is it paraben-free?", "Dermatologically tested under high safety standards."),
        ("Does it smooth split ends?", "Yes, nourishes and smooths dry split ends."),
        ("Is it suitable for color-treated hair?", "Yes, restores moisture lost during hair coloring."),
        ("Does it require rinsing?", "No, it is a leave-in hair cream."),
        ("Does it add natural shine?", "Yes, leaves hair touchably soft with natural radiance."),
        ("Does it prevent comb breakage?", "Yes, lubricates strands to prevent friction breakage during combing."),
        ("Is it a reliable daily moisturizing choice?", "Yes, the #1 choice for daily soft, hydrated hair styling.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1781",
        "sku": "EK-1781",
        "gtin": "6281006547407",
        "category": "العناية بالشعر / كريمات تصفيف وترطيب الشعر الجاف",
        "brand": "Sunsilk",
        "ar": {
            "title": "كريم تصفيف الشعر صنسيلك بزيت جوز الهند 275 مل لترطيب ونعومة فائقة",
            "meta_title": "كريم صنسيلك بجوز الهند 275مل | صيدلية إكليل أبها",
            "meta_description": "اشتري كريم تصفيف الشعر صنسيلك بزيت جوز الهند (275 مل). لترطيب ونعومة فائقة ومنع هيشان الشعر الجاف. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["صنسيلك", "كريم_جوز_الهند", "ترطيب_الشعر", "نعومة_فائقة", "إكليل_أبها"]
        },
        "en": {
            "title": "Sunsilk Hair Styling Cream with Coconut Oil - 275ml",
            "meta_title": "Sunsilk Hair Styling Cream with Coconut Oil 275ml | Ekleel Abha",
            "meta_description": "Buy original Sunsilk Hair Styling Cream with Coconut Oil (275ml). Extreme softness & hydration for dry frizzy hair. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["sunsilk", "coconut_oil_cream", "hair_hydration", "extreme_softness", "ekleel_abha"]
        },
        "schema": {
            "brand": "Sunsilk",
            "category": "Hair Care / Hair Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "sunsilk-hair-styling-cream-with-coconut-oil-275ml.webp",
            "alt": "Sunsilk Hair Styling Cream with Coconut Oil 275ml",
            "title": "Sunsilk Hair Styling Cream with Coconut Oil 275ml"
        }
    }

def create_product_1782():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>معجون أسنان كلوس أب احمر - 120مل (Closeup Red Hot Toothpaste - 120ml)</strong> معجون الأسنان الأيقوني المفضل عالمياً لإضفاء انتعاش حراري ناري يدوم حتى 12 ساعة متواصلة وحماية فموية فائقة. يعتمد هذا الجل العطري الناري من كلوس أب على تقنية الزنك النشط (Active Zinc Formula) والمعززة بمحلول الفلورايد المطهر ونكهة القرفة الحارة الشديدة للانتعاش (Red Hot Cinnamon flavor).</p>
<p>يقضي معجون كلوس أب الأحمر على 99% من البكتيريا المسببة لرائحة الفم الكريهة، يزيل طبقات البلاك الجيرية، ويحمي مينا الأسنان من التسوس، ليمنحكِ ابتسامة مشرفة، ناصعة البياض، ونفساً منعشاً يبث الثقة في كل لحظة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>انتعاش حار يدوم حتى 12 ساعة:</strong> نكهة القرفة النارية الشديدة تضمن نفساً منعشاً طوال اليوم.</li>
  <li><strong>تقنية الزنك النشط المضادة للبكتيريا:</strong> تقضي على 99% من بكتيريا الفم المسببة لرائحة الفم الكريهة.</li>
  <li><strong>حماية فائقة ضد التسوس والفلورايد:</strong> يدعم مينا الأسنان ويحميها من النخر وحمض البكتيريا.</li>
  <li><strong>تنظيف وإزالة طبقات البلاك:</strong> حبيبات التلميع تنظف أسطح الأسنان وتمنع تراكم التكلسات الجيرية.</li>
  <li><strong>جل أحمر ناري جذاب:</strong> قوام جل كريستالي يمنح تجربة تفريش ممتعة ومبهجة.</li>
  <li><strong>أنبوب سعة 120 مل:</strong> حجم ممتاز ومناسب للاستخدام العائلي اليومي المتكرر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق):</strong> وضعي كمية بحجم حبة البازلاء من معجون كلوس أب الأحمر على شعيرات فرشاة الأسنان.</li>
  <li><strong>الخطوة الثانية (التفريش):</strong> فرشي أسنانكِ وفروة اللسان بحركات دائرية خفيفة لمدة 2 دقيقة على الأقل.</li>
  <li><strong>الخطوة الثالثة (الشطف):</strong> ابصقي الجل واشطفي الفم بالماء الفاتر جيداً (يُستعمل 2 إلى 3 مرات يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الزنك النشط (Active Zinc Sulfate):</strong> يقضي على البكتيريا المسببة للرائحة الكريهة والبلاك.</li>
  <li><strong>فلورايد الصوديوم (Sodium Fluoride):</strong> يقوي المينا ويحمي من تسوس الأسنان.</li>
  <li><strong>نكهة القرفة الحارة الشديدة (Red Hot Cinnamon Aroma):</strong> تضمن انتعاشاً نارياً مستمراً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الفموي لتفريش الأسنان فقط؛ لا يبتلع المعجون.</li>
  <li>للأطفال دون 6 سنوات يُفضل استخدام كمية بحجم حبة البازلاء تحت إشراف الوالدين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن انتعاش ناري يدوم 12 ساعة، حماية من بكتيريا الفم، وابتسامة بيضاء ناصعة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كلوس أب (Closeup)</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم / معاجين الأسنان المنعشة</td></tr>
  <tr><th>نوع المنتج</th><td>معجون أسنان جل أحمر بنكهة القرفة والزنك (Red Hot 120ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>120 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بالفم والأسنان)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان نظيفة بيضاء، نفس حراري منعش لـ 12 ساعة ولثة صحية</td></tr>
  <tr><th>الملمس</th><td>جل أحمر ناري كريستالي يرغي بفاعلية</td></tr>
  <tr><th>العطر</th><td>نكهة القرفة الحارة والانتعاش الشديد</td></tr>
  <tr><th>المكونات النشطة</th><td>الزنك النشط (Active Zinc)، فلورايد الصوديوم، حبيبات تلميع السيليكا</td></tr>
  <tr><th>بلد المنشأ</th><td>جمهورية مصر العربية / المملكة العربية السعودية (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (كلوس أب)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والأطفال (من 6 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لتقنية الزنك النشط وانتعاش كلوس أب (Closeup Red Hot)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج معجون كلوس أب الأحمر مشكلة رائحة الفم الكريهة، تراكم البكتيريا والبلاك بين الأسنان، وشحوب بياض المينا.</p>

<h3>لماذا تنجح تقنية الزنك النشط؟</h3>
<p>لأن الزنك النشط يستهدف البكتيريا المسببة للرائحة الكريهة ويقضي عليها بنسبة 99%، بينما يمنح عبير القرفة انتعاشاً يدوم 12 ساعة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التفريش دقيقتين كاملتين:</strong> فرشي الأسنان مرتين يومياً صباحاً ومساءً.<br>
2. <strong>تنظيف اللسان:</strong> مرري الفرشاة بلطف على اللسان لإزالة البكتيريا.<br>
3. <strong>استخدام الخيط الطبي:</strong> استعملي الخيط الطبي لإزالة بقايا الطعام بين الفتحات.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "معاجين الجل المنعشة لا تحمي من التسوس."<br>
<strong>الحقيقة:</strong> يحتوي كلوس أب على فلورايد الصوديوم بتركيز طبي يقوي المينا ويحمي من التسوس بفاعلية مثبتة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط أيونات الزنك النشطة (Active Zinc Ions) عملية التمثيل الغذائي للبكتيريا الفموية وتمنع إفراز المركبات الكبريتية الطيارة المسببة للرائحة.</p>"""

    faqs = [
        ("ما هو معجون أسنان كلوس أب احمر 120مل؟", "هو معجون أسنان جل أحمر بنكهة القرفة الحارة الشديدة وتقنية الزنك النشط لمنح انتعاش يدوم 12 ساعة وحماية من البكتيريا والتسوس."),
        ("ما هي تقنية الزنك النشط (Active Zinc)؟", "تقنية مضادة للبكتيريا تقضي على 99% من بكتيريا الفم المسببة لرائحة الفم الكريهة والبلاك."),
        ("كم مدة الانتعاش التي يمنحها المعجون؟", "يمنح انتعاشاً حرارياً متواصلاً يدوم حتى 12 ساعة."),
        ("ما حجم أنبوب المعجون؟", "يأتي بحجم 120 مل."),
        ("هل يقي من تسوس الأسنان؟", "نعم، يحتوي على فلورايد الصوديوم الذي يقوي مينا الأسنان ويحميها من التسوس."),
        ("ما هي نكهة معجون كلوس أب الأحمر؟", "يتميز بنكهة القرفة الحارة الشديدة (Red Hot Cinnamon) المبهجة والمنعشة."),
        ("ما هو بلد صنع معجون كلوس أب؟", "صُنع بواسطة شركة يونيلفر (Unilever) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات كلوس أب لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يساعد في تلميع وإزالة بقع الأسنان؟", "نعم، يحتوي على حبيبات السيليكا للتلميع وإزالة طبقات البلاك والجير."),
        ("هل يزيل البكتيريا عن اللسان أيضاً؟", "نعم، تفريش اللسان بالجل يقضي على البكتيريا المتراكمة عليه."),
        ("هل المعجون آمن للأطفال؟", "آمن للأطفال من سن 6 سنوات فما فوق مع استخدام كمية بحجم حبة البازلاء تحت الإشراف."),
        ("هل يترك شعوراً بالحرقان الشديد؟", "يمنح شعوراً حرارياً مشوقاً ومحبباً يزول بالماء ليترك انتعاشاً ثابتاً."),
        ("كيف أحتفظ بأنبوب المعجون؟", "يُحفظ في مكان بارد وجاف بغطاء محكم."),
        ("كم مرة يُفضل تفريش الأسنان يومياً؟", "يُوصى بالتفريش مرتين إلى 3 مرات يومياً بعد الوجبات."),
        ("هل يمنع نزيف اللثة الناجم عن البلاك؟", "نعم، إزالة البلاك والزنك المضاد للبكتيريا يحافظان على صحة اللثة."),
        ("هل أنبوب 120 مل مناسب للعائلة؟", "نعم، حجم ممتاز للاستخدام اليومي العائلي."),
        ("هل يساعد في تحسين بياض الأسنان؟", "نعم، إزالة التكلسات والبقع الاستهلاكية تعيد البياض الطبيعي."),
        ("هل الجل برغوة غنية؟", "نعم، يولد رغوة كثيفة تنظف كامل أنحاء الفم."),
        ("هل يحتوي على فلورايد؟", "نعم، مدعم بفلورايد الصوديوم للحماية الطبيبة."),
        ("هل يناسب المدخنين ومحتشي القهوة؟", "ممتاز جداً للمدخنين ومحتشي القهوة لإزالة الروائح والبقع."),
        ("هل أنبوب المعجون يسهل الضغط؟", "نعم، أنبوب مرن بغطاء لولبي محكم يسهل الاستخدام."),
        ("هل يمنع تكلس الجير؟", "نعم، يقلل تراكم طبقات الجير والبلاك على الأسنان."),
        ("هل يناسب تفريش الأسنان قبل النوم؟", "نعم، ممتاز لتنظيف الفم وتأمين حماية طوال الليل."),
        ("هل يترك طعماً لذيذاً بالفم؟", "نعم، طعم القرفة النارية يترك نفساً منعشاً وطيباً."),
        ("هل هو خيار معجون الأسنان المنعش الأول عالمياً؟", "نعم، العلامة الأولى المحبوبة عالمياً للانتعاش الحراري 12 ساعة.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Closeup Red Hot Toothpaste - 120ml</strong> is the world's iconic gel toothpaste designed to deliver up to 12 hours of intense spicy fresh breath and complete oral cavity protection. Powered by Active Zinc Formula and Sodium Fluoride, it features the legendary intense Red Hot Cinnamon flavor.</p>
<p>Closeup Red Hot eliminates up to 99% of bad-breath-causing bacteria, sweeps away sticky dental plaque, and fortifies enamel against tooth decay, leaving you with a confident, brilliant white smile and intense fresh breath that lasts all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Up to 12 Hours Intense Fresh Breath:</strong> Spicy Red Hot Cinnamon flavor guarantees fresh breath confidence.</li>
  <li><strong>Active Zinc Antibacterial Formula:</strong> Destroys 99% of odor-causing oral bacteria and dental plaque.</li>
  <li><strong>Advanced Cavity & Fluoride Protection:</strong> Fortifies primary and permanent enamel against acid decay.</li>
  <li><strong>Plaque Removal & Whitening Polish:</strong> Silica polishing micro-particles clean tooth surfaces smoothly.</li>
  <li><strong>Vibrant Red Crystal Gel:</strong> Eye-catching gel texture that makes daily brushing fun and invigorating.</li>
  <li><strong>Convenient 120ml Tube:</strong> Excellent value tube ideal for family daily oral hygiene.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply):</strong> Apply a pea-sized amount of Closeup Red Hot gel toothpaste onto toothbrush bristles.</li>
  <li><strong>Step 2 (Brush):</strong> Brush teeth and tongue surface gently in circular motions for at least 2 minutes.</li>
  <li><strong>Step 3 (Rinse):</strong> Spit out gel and rinse mouth thoroughly with water (use 2 to 3 times daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Active Zinc Sulfate:</strong> Antibacterial agent that eliminates bad-breath germs and plaque.</li>
  <li><strong>Sodium Fluoride:</strong> Strengthens tooth enamel and defends against cavities.</li>
  <li><strong>Red Hot Cinnamon Flavor:</strong> Delivers signature intense spicy fresh breath.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For oral brushing application only; do not swallow.</li>
  <li>For children under 6 years, use a pea-sized amount under adult supervision.</li>
  <li>Keep out of reach of young children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking 12-hour intense fresh breath, 99% antibacterial protection, and a bright white smile.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Closeup</td></tr>
  <tr><th>Category</th><td>Oral Care / Refreshing Gel Toothpastes</td></tr>
  <tr><th>Product Type</th><td>Active Zinc Red Hot Cinnamon Gel Toothpaste (120ml)</td></tr>
  <tr><th>Volume/Weight</th><td>120 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Oral & Dental Care)</td></tr>
  <tr><th>Finish</th><td>Clean white teeth, 12-hour intense fresh breath & healthy gums</td></tr>
  <tr><th>Texture</th><td>Spicy red crystal foaming gel</td></tr>
  <tr><th>Fragrance</th><td>Intense Red Hot Cinnamon flavor</td></tr>
  <tr><th>Active Ingredients</th><td>Active Zinc Sulfate, Sodium Fluoride, Silica Polishers</td></tr>
  <tr><th>Country of Origin</th><td>Egypt / Saudi Arabia (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever (Closeup)</td></tr>
  <tr><th>Age Group</th><td>Adults & Kids (6+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Active Zinc & 12-Hour Fresh Breath</h2>

<h3>What problem does this solve?</h3>
<p>Closeup Red Hot Toothpaste resolves bad breath (halitosis), oral bacterial accumulation, plaque buildup, and dull teeth.</p>

<h3>Why choose Closeup Red Hot?</h3>
<p>Active Zinc ions breach bacterial membranes to destroy 99% of odor-causing microbes, while Red Hot Cinnamon oil provides 12-hour fresh breath.</p>"""

    en_faqs = [
        ("What is Closeup Red Hot Toothpaste 120ml?", "It is a red gel toothpaste featuring Active Zinc and intense Red Hot Cinnamon flavor to deliver 12 hours of fresh breath."),
        ("What is Active Zinc technology?", "An antibacterial formula that eliminates 99% of bad-breath-causing bacteria and plaque."),
        ("How long does the fresh breath last?", "Provides continuous spicy fresh breath confidence for up to 12 hours."),
        ("What volume is contained in this tube?", "It comes in a convenient 120ml tube."),
        ("Does it protect against cavities?", "Yes, contains Sodium Fluoride to strengthen enamel and guard against cavities."),
        ("What flavor does Closeup Red Hot have?", "Features an intense, spicy Red Hot Cinnamon flavor."),
        ("Where is Closeup manufactured?", "It is produced by Unilever following global oral care standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Closeup products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it help polish teeth stains?", "Yes, silica micro-polishers gently clean teeth and remove surface stains."),
        ("Does it clean bacteria from the tongue?", "Yes, brushing the tongue surface with gel removes lingering bacteria."),
        ("Is it safe for children?", "Safe for children aged 6+ using a pea-sized amount under supervision."),
        ("Does it cause intense tingling?", "Imparts a pleasant spicy warm sensation that settles into long-lasting fresh breath."),
        ("How should I store the tube?", "Store in a cool, dry place with cap tightly closed."),
        ("How many times daily should I brush?", "Brush 2 to 3 times daily after meals."),
        ("Does it prevent plaque-induced gum bleeding?", "Yes, clearing plaque and bacteria maintains healthy gums."),
        ("Is the 120ml tube family-friendly?", "Yes, ideal size for daily family oral care."),
        ("Does it boost natural teeth whiteness?", "Yes, polishing off stains restores natural enamel whiteness."),
        ("Does the gel foam well?", "Yes, produces a rich cleansing foam throughout the mouth."),
        ("Does it contain fluoride?", "Yes, enriched with Sodium Fluoride for medical enamel protection."),
        ("Is it great for coffee drinkers and smokers?", "Yes, excellent for neutralizing coffee and tobacco breath and stains."),
        ("Is the tube easy to squeeze?", "Yes, flexible tube with a secure cap."),
        ("Does it prevent tartar formation?", "Yes, reduces plaque buildup before it calcifies into tartar."),
        ("Is it good for nighttime brushing?", "Yes, cleanses oral cavity for overnight protection."),
        ("Does it leave a pleasant aftertaste?", "Yes, spicy cinnamon flavor leaves mouth feeling fresh."),
        ("Is it the world's #1 fresh breath gel toothpaste?", "Yes, globally famous for 12-hour intense fresh breath confidence.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1782",
        "sku": "EK-1782",
        "gtin": "6221155039774",
        "category": "العناية بالفم / معاجين الأسنان المنعشة",
        "brand": "Closeup",
        "ar": {
            "title": "معجون أسنان كلوس أب احمر - 120مل",
            "meta_title": "معجون اسنان كلوس اب احمر 120مل | صيدلية إكليل أبها",
            "meta_description": "اشتري معجون أسنان كلوس أب احمر (120مل). نكهة القرفة والزنك النشط لانتعاش يدوم 12 ساعة وحماية 99% من البكتيريا. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["كلوس_أب", "معجون_كلوس_أب", "كلوس_اب_احمر", "الزنك_النشط", "إكليل_أبها"]
        },
        "en": {
            "title": "Closeup Red Hot Toothpaste - 120ml",
            "meta_title": "Closeup Red Hot Toothpaste 120ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Closeup Red Hot Toothpaste (120ml). 12-hour fresh breath with Active Zinc & Cinnamon flavor. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["closeup", "red_hot_toothpaste", "active_zinc", "cinnamon_flavor", "ekleel_abha"]
        },
        "schema": {
            "brand": "Closeup",
            "category": "Oral Care / Toothpaste",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "closeup-red-hot-toothpaste-120ml.webp",
            "alt": "Closeup Red Hot Toothpaste 120ml",
            "title": "Closeup Red Hot Toothpaste 120ml"
        }
    }

print("Loaded Batch 15 builders")
