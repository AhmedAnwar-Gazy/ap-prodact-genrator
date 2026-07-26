import json, os

def create_product_2094():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>خلطة صابونية العكر الفاسي 500جم (Aker Fassi Soap Mix - 500g)</strong> الصابونية المغربية التراثية الموردة والمفتحة الفاخرة المصممة خصيصاً لتنظيف، توريد، وتفتيح بشرة الجسم وإكسابها لوناً وردياً ناضراً والتخلص من التصبغات والبقع الداكنة والخلايا الميتة. تركز هذه الصابونية الأصيلة (Aker Fassi Soap 500g) على مسحوق العكر الفاسي الغزال الأصلي (Poppy Extract)، الزيوت المغربية المرطبة، وخلاصات التفتيح النباتية.</p>
<p>تعمل صابونية العكر الفاسي على تقشير مسام الجسم بلطف، منح الجلد لوناً محمراً ناعماً مفعماً بالأنوثة والنضارة، وحفظ رطوبة البشرة الداخلية، لتترك بشرتك ناعمة كالحرير، ناصعة النقاء، وردية التوهج، ومفعمة بالانتعاش والجاذبية من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وتوريد طبيعي لبشرة الجسم بالعكر الفاسي:</strong> يمنح الجلد لوناً وردياً ناعماً وتوهجاً ناصعاً.</li>
  <li><strong>تقشير وتصفية الخلايا الميتة والشوائب الداكنة:</strong> ينظف مسام الجسم بفاعلية ولطف.</li>
  <li><strong>ترطيب وتنعيم فائق لبشرة الجسم:</strong> يمنع الجفاف والخشونة بعد الاستحمام.</li>
  <li><strong>تحسين ملمس ومظهر الجلد المجهد:</strong> يزيل البهتان ويجدد نضارة الكفين والركبتين والجسم.</li>
  <li><strong>تركيبة مغربية تراثية خالية من المواد الضارة:</strong> مناسبة لجميع أنواع البشرة.</li>
  <li><strong>عبوة ضخمة سعة 500 جم:</strong> حجم ممتاز للاستخدام اليومي المستمر وحمامات البخار المغربية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الجسم بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي كمية سخية من صابونية العكر الفاسي على الجسم وافركي برفق بالليفة المغربية.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركي الرغوة 5-10 دقائق ثم اشطفي جيداً بالماء (يُستعمل 2-3 مرات أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مسحوق العكر الفاسي الأصلي (دم الغزال):</strong> يورد البشرة ويمنحها لوناً ناضراً ناعماً.</li>
  <li><strong>الزيوت النباتية والمنظفات الصابونية الطبيعية:</strong> تنظف الجسم وتحفظ نعومته الحريرية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين والوجه الحساس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن صابونية العكر الفاسي 500 جم لتوريد وتفتيح وتنظيف بشرة الجسم.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>العكر الفاسي (Aker Fassi Beauty)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / الصابونيات المغربية وخلطات التوريد 500g</td></tr>
  <tr><th>نوع المنتج</th><td>خلطة صابونية مغربية موردة ومفتحة ومقشرة للجسم بالعكر الفاسي (500g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (خصيصاً الباهتة، الداكنة، والجافة)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، وردي التوهج، موحد اللون وناصع النقاء والنظافة</td></tr>
  <tr><th>الملمس</th><td>معجون صابوني أحمر وردي غني ينقلب لرغوة تنظيف ناعمة</td></tr>
  <tr><th>العطر</th><td>عطر العكر الفاسي المغربي العشبي الأصيل</td></tr>
  <tr><th>المكونات النشطة</th><td>مسحوق العكر الفاسي الأصلي، زيت أرجان، خلاصات تفتيح مائية</td></tr>
  <tr><th>بلد المنشأ</th><td>المغرب / المملكة العربية السعودية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Moroccan Beauty Care Inc.</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد مسحوق العكر الفاسي التراثي في صابونية التوريد (Aker Fassi Soap)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج صابونية العكر الفاسي مشكلة بهتان واصفرار لون الجسم، التصبغات الداكنة، وجفاف الجلد بعد الغسيل.</p>

<h3>لماذا تنجح تركيبة Aker Fassi Natural Soap?</h3>
<p>لأن صبغة أوراق شقائق النعمان والرمان بالعكر الفاسي ترتبط ببروتين الجلد مانحة توريداً طبيعياً ممتداً.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على جسم دافئ بالبخار:</strong> يضاعف امتصاص خلاصات التوريد والتفتيح.<br>
2. <strong>استخدام الليفة المغربية برفق:</strong> يزيل القشور الميتة ويظهر اللمعان الوردي.<br>
3. <strong>الترطيب بـ لوشن مرطب بعد الشطف:</strong> يحفظ طراوة ونعومة البشرة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "العكر الفاسي يترك بقعاً حمراء غير مرغوبة بالجلد."<br>
<strong>الحقيقة:</strong> صابونية العكر الفاسي مصممة بتركيبة صابونية متوازنة تنشطف بالماء مخلِفة توريداً وردياً ناعماً دون تلطخ.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخترق الفلافونويدات ومضادات الأكسدة الطبيعية الطبقة القرنية مغذية البشرة ومحسنة ترويتها الدموية.</p>"""

    faqs = [
        ("ما هي خلطة صابونية العكر الفاسي 500جم؟", "هي خلطة صابونية مغربية موردة ومفتحة ومقشرة للجسم بمسحوق العكر الفاسي الأصلي والزيوت الطبيعية (500 جم)."),
        ("ما هي فوائد العكر الفاسي الأصلي (دم الغزال) للجسم؟", "يمنح البشرة لوناً وردياً ناطقاً بالنضارة، يفتح التصبغات، ويقشر الخلايا الميتة."),
        ("هل تورد وتفتح بشرة الجسم وتزيل التصبغات؟", "نعم، مثبتة في توريد وتفتيح ونظافة بشرة الجسم وإكسابها نضارة ورائعة."),
        ("ما حجم العبوة؟", "تأتي بعبوة ضخمة بسعة 500 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي على جسم مبلل دافئ، افركي بالليفة المغربية، اتركيه 5-10 دقائق واشطفي 2-3 مرات أسبوعياً."),
        ("هل هي آمنة ومصنوعة من مواد طبيعية؟", "نعم، 100% آمنة ومصنوعة من خلاصات عكر فاسي وزيوت مرطبة طبيعية."),
        ("أين صُنعت صابونية العكر الفاسي؟", "صُنع وفق أعلى معايير الصابونيات المغربية التراثية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        ("ما رائحة صابونية العكر الفاسي؟", "عطر العكر الفاسي المغربي العشبي الزكي المنعش."),
        ("هل تناسب جميع مناطق الجسم؟", "نعم، ممتازة لتفتيح وتوريد الجسم والرقبة والكوعين والركبتين."),
        ("هل عبوة 500 جم تكفي لفترة جيدة؟", "نعم، عبوة ضخمة تكفي لعدة أشهر من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل هي الصابونية الأكثر تفضيلاً للتوريد الطبيعي؟", "نعم، صابونية العكر الفاسي الخيار الأكثر شهرة وتفضصيلاً لتوريد وتفتيح الجسم."),
        ("كم مرة أسبوعياً؟", "2 إلى 3 مرات أسبوعياً أثناء الاستحمام."),
        ("هل تنشطف بالماء بسهولة؟", "نعم، تنشطف بالماء الدافئ بسهولة تاركة توهجاً وردياً دون تلطيخ."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يفضل استخدام لوشن مرطب بعدها؟", "نعم، يُفضل استخدام لوشن مرطب بعد الشطف لحفظ الطراوة."),
        ("هل تترك البشرة ناعمة كالحرير؟", "نعم، تترك بشرة الجسم في غاية النعومة والنظافة الحريرية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والفتيات؟", "نعم، ممتازة جداً للنساء والفتيات والعرائس."),
        ("هل يناسب جميع فصول السنة؟", "نعم، ممتاز للصيف والشتاء وحمامات البخار."),
        ("هل يصلح هدية ممتازة ضمن العناية؟", "نعم، منتج عناية وتوريد مغربي فاخر ومفيد جداً."),
        ("هل يعيد المظهر الوردي المشرق للبشرة؟", "نعم، يمنح الجسد مظهراً وردياً ناضراً."),
        ("هل يناسب العرائس قبل الزفاف؟", "نعم، خيار أسطوري للعرائس لتوريد وتفتيح الجسم بالكامل."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Aker Fassi Soap Mix - 500g</strong> is an authentic luxury traditional Moroccan rosifying, whitening, and clarifying body soap paste designed to cleanse, rosify, and brighten body skin while adding a natural rosy pink glow and sweeping away dark spots and dead cells. Built upon authentic Aker Fassi poppy powder, hydrating Moroccan oils, and botanical whitening extracts.</p>
<p>Aker Fassi Soap Mix gently exfoliates body pores, imparts a feminine rosy glow, and preserves internal skin moisture, leaving your body touchably silky soft, spotlessly clean, rosy-radiant, and attractive from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Natural Rosy Glow & Body Whitening with Aker Fassi:</strong> Gives skin a soft pink radiance.</li>
  <li><strong>Exfoliates Dead Cells & Sweeps Dark Impurities:</strong> Purifies body skin pores effectively and gently.</li>
  <li><strong>Superior Body Softening & Hydration:</strong> Prevents post-shower skin dryness and tightness.</li>
  <li><strong>Rejuvenates Stressed Dull Skin:</strong> Fades dullness restoring vitality to body skin.</li>
  <li><strong>Traditional Moroccan Natural Formula:</strong> Safe and tested for all skin types.</li>
  <li><strong>Generous 500g Value Tub Container:</strong> Excellent format for regular use and Moroccan steam bath rituals.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet body skin with warm water during shower or steam bath.</li>
  <li><strong>Step 2:</strong> Spread a generous layer of Aker Fassi soap paste over body and scrub gently with a loofah.</li>
  <li><strong>Step 3:</strong> Leave lather on for 5-10 minutes, then rinse thoroughly with water (use 2-3 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Authentic Aker Fassi Powder (Poppy & Pomegranate Extract):</strong> Rosifies skin giving a soft natural pink radiance.</li>
  <li><strong>Plant Oils & Natural Soap Cleansers:</strong> Cleanse body while maintaining internal moisture balance.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application.</li>
  <li>Avoid direct contact with eyes and sensitive facial skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Any woman seeking Aker Fassi Soap Mix 500g for body rosifying, whitening, and smooth skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Aker Fassi Beauty</td></tr>
  <tr><th>Category</th><td>Body Care / Moroccan Rosifying & Whitening Soaps 500g</td></tr>
  <tr><th>Product Type</th><td>Moroccan Rosifying, Whitening & Exfoliating Aker Fassi Body Soap (500g)</td></tr>
  <tr><th>Volume/Weight</th><td>500 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Specifically Dull, Dark & Dry Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, rosy-glowing, even-toned & spotlessly clean body skin</td></tr>
  <tr><th>Texture</th><td>Rich smooth foaming reddish-pink herbal soap paste</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh traditional Moroccan Aker Fassi scent</td></tr>
  <tr><th>Active Ingredients</th><td>Authentic Aker Fassi Powder, Argan Oil, Whitening Herbal Extracts</td></tr>
  <tr><th>Country of Origin</th><td>Morocco / KSA</td></tr>
  <tr><th>Manufacturer</th><td>Moroccan Beauty Care Inc.</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Aker Fassi Flavonoids & Cutaneous Micro-Vascular Rosification</h2>

<h3>What problem does this solve?</h3>
<p>Aker Fassi Soap resolves body skin dullness, yellowish skin tone, dark spots, and dead skin cell accumulation.</p>

<h3>Why choose Aker Fassi Soap Mix?</h3>
<p>Poppy and pomegranate flavonoids bind to surface skin proteins imparting a soft natural rosy pink glow without staining.</p>"""

    en_faqs = [
        ("What is Aker Fassi Soap Mix - 500g?", "It is a luxury traditional Moroccan rosifying, whitening, and exfoliating body soap paste with authentic Aker Fassi powder (500g)."),
        ("What are the benefits of authentic Aker Fassi (Poppy powder) for the body?", "Gives body skin a natural rosy pink radiance, brightens dark spots, and exfoliates dead cells."),
        ("Does it rosify and brighten body skin effectively?", "Yes, proven to rosify body skin tone, even discoloration, and sweep away dark surface impurities."),
        ("What volume is contained in this tub?", "500g jumbo tub."),
        ("How do I use it correctly?", "Apply to wet warm skin, scrub with a loofah, leave 5-10 minutes and rinse 2-3 times weekly."),
        ("Is it safe and made from natural ingredients?", "Yes, 100% safe, formulated with natural Aker Fassi powder and moisturizing oils."),
        ("Where is Aker Fassi Soap manufactured?", "Manufactured to international Moroccan bath quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Aker Fassi products at Ekleel Abha are 100% original."),
        ("What scent does Aker Fassi Soap have?", "Luxurious fresh traditional Moroccan herbal fragrance."),
        ("Is it suitable for dark body zones?", "Yes, excellent for rosifying and brightening body skin, neck, knees, and elbows."),
        ("Does the 500g tub last long?", "Yes, jumbo tub lasts months of regular use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it a famous rosifying soap paste?", "Yes, Aker Fassi is the world's most famous choice for natural body rosification."),
        ("How many times weekly?", "2 to 3 times weekly during showers or steam baths."),
        ("Does it rinse off easily without staining?", "Yes, rinses off smoothly with warm water leaving a soft rosy glow without staining."),
        ("Is the container recyclable?", "Yes."),
        ("Is applying a body lotion recommended afterwards?", "Yes, follow with a hydrating lotion after rinsing to seal in moisture."),
        ("Does it leave skin touchably silky soft?", "Yes, leaves body skin silky soft, clear, and spotlessly clean."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and brides?", "Yes, highly recommended for women and brides before weddings."),
        ("Is it good for all seasons?", "Yes, excellent for summer, winter, and steam bath routines."),
        ("Is it a nice skincare gift?", "Yes, an elegant practical Moroccan body rosifying gift."),
        ("Does it restore bright rosy skin appearance?", "Yes, gives body skin a bright rosy radiant look."),
        ("Is it ideal for brides before weddings?", "Yes, an essential legendary preparation choice for brides for body rosification."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2094",
        "sku": "EK-2094",
        "gtin": "8721214011881",
        "brand": "Aker Fassi Beauty",
        "ar": {
            "title": "خلطة صابونية العكر الفاسي  500جم",
            "meta_title": "صابونية العكر الفاسي لتوريد الجسم 500جم | إكليل أبها",
            "meta_description": "اشتري خلطة صابونية العكر الفاسي لتوريد وتفتيح الجسم (500 جم). صابونية مغربية تراثية بالعكر الفاسي لترك لون وردي ناضر للبشرة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["العكر_الفاسي", "صابونية_العكر_الفاسي", "توريد_الجسم", "تفتيح_البشرة_المغربي", "إكليل_أبها"]
        },
        "en": {
            "title": "Aker Fassi Soap Mix - 500g",
            "meta_title": "Aker Fassi Soap Mix Rosifying 500g | Ekleel Abha",
            "meta_description": "Buy original Aker Fassi Soap Mix (500g). Traditional Moroccan rosifying, whitening, and exfoliating body soap paste. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["aker_fassi", "aker_fassi_soap", "rosifying_body_soap", "moroccan_soap", "ekleel_abha"]
        }
    }


def create_product_2095():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>صابونية النيلة مغربية الصحراويه 500جم (Moroccan Saharan Blue Nila Soap - 500g)</strong> خلطة الصابونية الطبيعية المفتحة والمصفيّة الفاخرة الأسطورية الأصيلة من المغرب المصممة خصيصاً لتفتيح وتوحيد لون بشرة الجسم والتخلص من التصبغات المستعصية، البقع الداكنة، وأثر الشمس، ومنح الجلد صفاءً وإشراقة ناصعة. تركز هذه الصابونية الأصيلة (Blue Nila Soap 500g) على بودرة النيلة الزرقاء الصحراوية المغربية النقية (Pure Saharan Nila Powder)، زيوت العناية المغربية، وخلاصات الأعشاب المبيضة.</p>
<p>تعمل صابونية النيلة المغربية الصحراوية على تقشير مسام الجسم عمقاً، امتصاص التصبغات والسموم الجلدية، وتنعيم وحفظ رطوبة البشرة الداخلية، لتترك بشرتك ناعمة كالحرير، ناصعة البياض، موحدة اللون، ومفعمة بالنقاء والانتعاش من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وتصفية فائقة للتصبغات بالنيلة المغربية الصحراوية:</strong> يزيل البقع الداكنة وأثر الشمس.</li>
  <li><strong>تقشير وتوحيد لون بشرة الجسم والرقبة والكوعين:</strong> يمنح الجلد مظهراً صافياً موحداً.</li>
  <li><strong>ترطيب وتنعيم فائق لبشرة الجسم:</strong> يحفظ حاجز الترطيب الطبيعي للجلد دون جفاف.</li>
  <li><strong>امتصاص الشوائب والسموم من مسام البشرة:</strong> يجدد نضارة وشباب الجسم المجهد.</li>
  <li><strong>تركيبة مغربية صحراوية تراثية ناعمة:</strong> آمنة ومختبرة لجميع أنواع البشرة.</li>
  <li><strong>عبوة ضخمة سعة 500 جم:</strong> حجم ممتاز للاستخدام العائلي المستمر وحمامات البخار.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الجسم بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي كمية سخية من صابونية النيلة الزرقاء على الجسم وافركي برفق بالليفة المغربية.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركي الرغوة 5-10 دقائق ثم اشطفي جيداً بالماء (يُستعمل 2-3 مرات أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>بودرة النيلة الزرقاء الصحراوية المغربية النقية:</strong> تمتص التصبغات وتفتح المناطق الداكنة بفاعلية أسطورية.</li>
  <li><strong>الزيوت النباتية والمنظفات الصابونية الطبيعية:</strong> تنظف الجسم وتحفظ نعومته الحريرية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين والوجه الحساس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن صابونية النيلة المغربية الصحراوية 500 جم لتفتيح وتصفية وتوحيد لون بشرة الجسم.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>النيلة الصحراوية (Saharan Blue Nila)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / الصابونيات المغربية بالنيلة الصحراوية 500g</td></tr>
  <tr><th>نوع المنتج</th><td>خلطة صابونية مغربية صحراوية مفتحة ومصفية ومقشرة للجسم بالنيلة الزرقاء (500g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (خصيصاً المتصبغة، الداكنة، والجافة)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، موحد اللون، ناصع البياض ومفعم بالصفاء والنظافة</td></tr>
  <tr><th>الملمس</th><td>معجون صابوني أزرق نيلي غني ينقلب لرغوة تنظيف ناعمة</td></tr>
  <tr><th>العطر</th><td>عطر النيلة المغربية الصحراوية الأصيل</td></tr>
  <tr><th>المكونات النشطة</th><td>بودرة النيلة الزرقاء الصحراوية، زيت الأرجان، خلاصات مبيضة</td></tr>
  <tr><th>بلد المنشأ</th><td>المغرب / المملكة العربية السعودية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Saharan Beauty Care Inc.</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد بودرة النيلة الزرقاء الصحراوية في صابونية التفتيح (Moroccan Blue Nila Soap)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج صابونية النيلة المغربية مشكلة التصبغات المستعصية، اسمرار الشاطئ والشمس، عدم توحد اللون، والجلد الميت.</p>

<h3>لماذا تنجح تركيبة Saharan Blue Nila Soap?</h3>
<p>لأن بودرة النيلة المغربية مجهزة بجزيئات دقيقة تدمج وتكسر تجمعات الميلانين المترسبة بالطبقات الجلدية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على جسم دافئ بالبخار:</strong> يفتح المسام ويضاعف تغلغل النيلة الزرقاء.<br>
2. <strong>الفرك بالليفة المغربية برفق:</strong> يزيل التصبغات السطحية بفاعلية.<br>
3. <strong>الترطيب بـ لوشن مرطب بعد الشطف:</strong> يحفظ طراوة ونعومة البشرة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "النيلة الزرقاء تترك صبغة زرقاء دائمة بالجلد."<br>
<strong>الحقيقة:</strong> صابونية النيلة تنشطف بالماء بالكامل مخلِفة بشرة ناصعة البياض دون أي أثر أزرق.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تمتص بودرة النيلة الشوائب والتراكمات الصباغية مظهرة أدمة جلدية موحدة وصافية.</p>"""

    faqs = [
        ("ما هي صابونية النيلة مغربية الصحراويه 500جم؟", "هي خلطة صابونية مغربية تراثية مفتحة ومصفية ومقشرة للجسم ببودرة النيلة الزرقاء الصحراوية (500 جم)."),
        ("ما هي فوائد بودرة النيلة الزرقاء الصحراوية المغربية للجسم؟", "تزيل التصبغات والبقع الداكنة وأثر الشمس، تقشر الجلد الميت، وتوحد لون البشرة بصفاء ناصع."),
        ("هل تفتح وتصفية وتوحد لون الجسم؟", "نعم، مثبتة في تفتيح وتصفية وتوحيد لون بشرة الجسم كلياً."),
        ("ما حجم العبوة؟", "تأتي بعبوة ضخمة بسعة 500 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي على جسم مبلل دافئ، افركي بالليفة المغربية، اتركيه 5-10 دقائق واشطفي 2-3 مرات أسبوعياً."),
        ("هل هي آمنة ومصنوعة من نيلة صحراوية أصلية؟", "نعم، 100% آمنة ومصنوعة من خلاصات نيلة صحراوية وزيوت مرطبة أصلية."),
        ("أين صُنعت صابونية النيلة المغربية؟", "صُنع وفق أعلى معايير الصابونيات الصحراوية التراثية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        ("ما رائحة صابونية النيلة الصحراوية؟", "عطر النيلة المغربية الصحراوية العشبي المنعش الفاخر."),
        ("هل تناسب جميع مناطق الجسم الداكنة؟", "نعم، ممتازة لتفتيح وتصفية الجسم والرقبة والكوعين والركبتين."),
        ("هل عبوة 500 جم تكفي لفترة جيدة؟", "نعم، عبوة ضخمة تكفي لعدة أشهر من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل هي الصابونية الأكثر شهرة في تصفية التصبغات؟", "نعم، صابونية النيلة الزرقاء الخيار الأسطوري الأكثر تفضيلاً للتفتيح المغربي."),
        ("كم مرة أسبوعياً؟", "2 إلى 3 مرات أسبوعياً أثناء الاستحمام."),
        ("هل تنشطف بالماء بسهولة دون ترك أثر أزرق؟", "نعم، تنشطف بالماء الدافئ بسهولة مخلِفة بياضاً صافياً دون أي لقع زرقاء."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يفضل استخدام لوشن مرطب بعدها؟", "نعم، يُفضل استخدام لوشن مرطب بعد الشطف لحفظ الطراوة."),
        ("هل تترك البشرة ناعمة كالحرير؟", "نعم، تترك بشرة الجسم في غاية النعومة والنظافة الحريرية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتازة للنساء والرجال."),
        ("هل يناسب جميع فصول السنة؟", "نعم، ممتاز للصيف والشتاء وحمامات البخار."),
        ("هل يصلح هدية ممتازة ضمن العناية؟", "نعم، منتج عناية وتفتيح مغربي فاخر ومفيد جداً."),
        ("هل يعيد المظهر الصافي المشرق للبشرة؟", "نعم، يمنح الجسد مظهراً ناصع البياض والصفاء."),
        ("هل يناسب العرائس قبل الزفاف؟", "نعم، خيار أسطوري للعرائس لتفتيح وتصفية الجسم بالكامل."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Moroccan Saharan Blue Nila Soap - 500g</strong> is an authentic luxury legendary traditional Moroccan whitening, clarifying, and exfoliating body soap paste designed to brighten body skin, unify tone, and clear stubborn hyperpigmentation, dark spots, and sun damage. Built upon Pure Saharan Blue Nila Powder, hydrating Moroccan oils, and botanical whitening extracts.</p>
<p>Moroccan Saharan Blue Nila Soap deeply exfoliates body pores, absorbs skin impurities and pigmentation deposits, and seals in moisture, leaving your body touchably silky soft, spotlessly clean, clear, and brightened from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Superior Hyperpigmentation Clarifying with Saharan Blue Nila:</strong> Fades dark spots and sun damage.</li>
  <li><strong>Exfoliates & Evens Skin Tone on Body, Neck & Knees:</strong> Imparts a unified clear white skin finish.</li>
  <li><strong>Superior Body Softening & Hydration:</strong> Preserves skin natural moisture barrier without dryness.</li>
  <li><strong>Absorbs Impurities & Toxins from Skin Pores:</strong> Rejuvenates stressed dull body skin.</li>
  <li><strong>Gentle Traditional Saharan Moroccan Formula:</strong> Safe and tested for all skin types.</li>
  <li><strong>Generous 500g Value Tub Container:</strong> Excellent format for regular use and Moroccan steam baths.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet body skin with warm water during shower or steam bath.</li>
  <li><strong>Step 2:</strong> Spread a generous layer of Blue Nila soap paste over body and scrub gently with a loofah.</li>
  <li><strong>Step 3:</strong> Leave lather on for 5-10 minutes, then rinse thoroughly with water (use 2-3 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Saharan Blue Nila Powder:</strong> Absorbs pigmentation and brightens dark zones with legendary efficacy.</li>
  <li><strong>Plant Oils & Natural Soap Cleansers:</strong> Cleanse body while maintaining internal moisture balance.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application.</li>
  <li>Avoid direct contact with eyes and sensitive facial skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Any woman seeking Moroccan Saharan Blue Nila Soap 500g for body whitening, clarifying, and tone evening.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Saharan Blue Nila</td></tr>
  <tr><th>Category</th><td>Body Care / Moroccan Saharan Nila Soaps 500g</td></tr>
  <tr><th>Product Type</th><td>Moroccan Saharan Blue Nila Whitening & Clarifying Body Soap Paste (500g)</td></tr>
  <tr><th>Volume/Weight</th><td>500 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Specifically Hyperpigmented, Dark & Dry Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, even-toned, clear white & spotlessly clean body skin</td></tr>
  <tr><th>Texture</th><td>Rich smooth foaming indigo-blue herbal soap paste</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh authentic Saharan Moroccan scent</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Saharan Blue Nila Powder, Argan Oil, Whitening Extracts</td></tr>
  <tr><th>Country of Origin</th><td>Morocco / KSA</td></tr>
  <tr><th>Manufacturer</th><td>Saharan Beauty Care Inc.</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Saharan Blue Nila Pigment Adsorption & Epidermal Clarification</h2>

<h3>What problem does this solve?</h3>
<p>Moroccan Saharan Blue Nila Soap resolves stubborn hyperpigmentation, beach sun tanning, uneven skin tone, and dead skin cell buildup.</p>

<h3>Why choose Saharan Blue Nila Soap?</h3>
<p>Micro-fine Saharan Blue Nila particles adsorb dark melanin complexes clearing skin without leaving blue stains.</p>"""

    en_faqs = [
        ("What is Moroccan Saharan Blue Nila Soap - 500g?", "It is a legendary luxury traditional Moroccan whitening, clarifying, and exfoliating body soap paste with pure Saharan Blue Nila powder (500g)."),
        ("What are the benefits of pure Saharan Blue Nila powder for the body?", "Fades dark spots and hyperpigmentation, exfoliates dead skin, and evens body skin tone to a clear bright finish."),
        ("Does it brighten, clarify, and even body skin tone effectively?", "Yes, proven to brighten body skin tone, clarify discoloration, and sweep away dark surface impurities."),
        ("What volume is contained in this tub?", "500g jumbo tub."),
        ("How do I use it correctly?", "Apply to wet warm skin, scrub with a loofah, leave 5-10 minutes and rinse 2-3 times weekly."),
        ("Is it safe and made from authentic Saharan Blue Nila?", "Yes, 100% safe, formulated with authentic Saharan Blue Nila powder and moisturizing oils."),
        ("Where is Moroccan Blue Nila Soap manufactured?", "Manufactured to international Saharan bath quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Blue Nila products at Ekleel Abha are 100% original."),
        ("What scent does Saharan Blue Nila Soap have?", "Luxurious fresh traditional Saharan Moroccan herbal fragrance."),
        ("Is it suitable for dark body zones?", "Yes, excellent for clarifying and brightening body skin, neck, knees, and elbows."),
        ("Does the 500g tub last long?", "Yes, jumbo tub lasts months of regular use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it a famous whitening soap paste?", "Yes, Saharan Blue Nila is a world-famous legendary choice for Moroccan body skin clarification."),
        ("How many times weekly?", "2 to 3 times weekly during showers or steam baths."),
        ("Does it rinse off easily without leaving blue stains?", "Yes, rinses off smoothly with warm water leaving a clear white glow without blue stains."),
        ("Is the container recyclable?", "Yes."),
        ("Is applying a body lotion recommended afterwards?", "Yes, follow with a hydrating lotion after rinsing to seal in moisture."),
        ("Does it leave skin touchably silky soft?", "Yes, leaves body skin silky soft, clear, and spotlessly clean."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it good for all seasons?", "Yes, excellent for summer, winter, and steam bath routines."),
        ("Is it a nice skincare gift?", "Yes, an elegant practical Moroccan body whitening gift."),
        ("Does it restore bright clear skin appearance?", "Yes, gives body skin a bright clear radiant look."),
        ("Is it ideal for brides before weddings?", "Yes, an essential legendary preparation choice for brides for body skin whitening."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2095",
        "sku": "EK-2095",
        "gtin": "2781214012031",
        "brand": "Saharan Blue Nila",
        "ar": {
            "title": "صابونية النيلة مغربية الصحراويه 500جم",
            "meta_title": "صابونية النيلة المغربية الصحراوية 500جم | إكليل أبها",
            "meta_description": "اشتري صابونية النيلة المغربية الصحراوية (500 جم). صابونية معجونة بالنيلة الزرقاء الصحراوية لتفتيح وتصفية وتوحيد لون الجسم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["النيلة_المغربية", "صابونية_النيلة_الصحراوية", "النيلة_الزرقاء", "تفتيح_الجسم_المغربي", "إكليل_أبها"]
        },
        "en": {
            "title": "Moroccan Saharan Blue Nila Soap - 500g",
            "meta_title": "Moroccan Saharan Blue Nila Soap 500g | Ekleel Abha",
            "meta_description": "Buy original Moroccan Saharan Blue Nila Soap (500g). Pure Saharan Blue Nila whitening and clarifying body soap paste. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["blue_nila_soap", "saharan_nila_soap", "moroccan_blue_nila", "whitening_nila_soap", "ekleel_abha"]
        }
    }


def create_product_2096():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول منظف ​​لطيف للوجه للبشرة الحساسة من كيوفي- 250 جم (QV Gentle Facial Cleanser for Sensitive Skin - 250g)</strong> الكريم المنظف الطبي الفاخر الأكثر توصية من كيوفي (QV) المصمم خصيصاً لتنظيف، تصفية، وترطيب بشرة الوجه الحساسة والمفرطة الحساسية دون التسبب في أي حرقان، احمرار، أو تجريد للحجاب الدهني الطبيعي. يرتكز هذا الغسول الأصيل (QV Gentle Cleanser 250g) على الجليسرين المرطب المكثف، التركيبة الخالية 100% من الصابون والعطور، ودرجة الحموضة المتوازنة (pH 6.0).</p>
<p>يعمل غسول كيوفي اللطيف للوجه على إزالة الأوساخ والمكياج الخفيف والشوائب بسلاسة، حماية الوجه من الجفاف الشديد، وإعادة التوازن المائي للبشرة، ليترك وجهك ناعماً كالحرير، مرطباً، ناصع النظافة، ومحمياً من التهيجات من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف كريمي لطيف جداً للبشرة الحساسة والجافة:</strong> ينظف الوجه دون صابون أو تهيج.</li>
  <li><strong>ترطيب وتغذية ممتدة بالجليسرين الطبي:</strong> يمنع شعور الشد والجفاف بعد الغسيل.</li>
  <li><strong>حماية حاجز البشرة بدرجة حموضة متوازنة (pH 6.0):</strong> تحافظ على الفلورا الجلدية الطبيعية.</li>
  <li><strong>تركيبة خالية 100% من الصابون والعطور والزيوت والبارابين:</strong> لا تسبب انسداد المسام.</li>
  <li><strong>موصى به من أطباء الجلدية ومختبر طبياً:</strong> مناسب للوجه والشفايف والعيون الحساسة.</li>
  <li><strong>عبوة سعة 250 جم مزودة بضاغط مريح:</strong> حجم ممتاز للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الوجه بالماء الدافئ أثناء الغسيل.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسية من كريم كيوفي ودلكي الوجه برفق بحركات دائرية ناعمة.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء الدافئ وجففي الوجه برفق (يُستعمل مرتين يومياً صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الجليسرين الطبي المكثف (Glycerin 15%):</strong> يحبس جزيئات الماء داخل خلايا البشرة.</li>
  <li><strong>المنظفات الكريمية الخالية من الصابون:</strong> تنظف المسام وتحفظ النعومة الحريرية للوجه.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يملك بشرة وجه حساسة أو جافة ويبحث عن غسول كيوفي اللطيف 250 جم للتنظيف والترطيب الشامل.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كيوفي (QV Ego)</td></tr>
  <tr><th>الفئة</th><td>العناية بالوجه / غسولات كيوفي الطبية للبشرة الحساسة 250g</td></tr>
  <tr><th>نوع المنتج</th><td>كريم غسول طبي لطيف خالي من الصابون والعطور للبشرة الحساسة (250g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>250 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الحساسة، الجافة، المفرطة التحسس والمصابة بالوردية</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، مرطب 24 ساعة، ناصع النظافة وخالٍ من الاحمرار والشد</td></tr>
  <tr><th>الملمس</th><td>كريم سائل ناعم غير رغوي ينشطف بالماء بسلاسة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>جليسرين طبي، منظفات خالية من الصابون (pH 6.0)، بارافين مرطب</td></tr>
  <tr><th>بلد المنشأ</th><td>أستراليا (Australia)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الجليسرين الطبي ودرجة pH 6.0 في غسول كيوفي للوجه (QV Gentle Cleanser)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول كيوفي اللطيف للوجه مشكلة احمرار وتقشر البشرة الحساسة، حرقان الصابون التقليدي، وجفاف الوجه بعد الغسل.</p>

<h3>لماذا تنجح تركيبة QV Gentle Facial Cleanser؟</h3>
<p>لأن التركيبة الخالية من الصابون وبدرجة pH 6.0 تنظف المسام دون التأثير على الأغشية الدهنية الضعيفة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنظيف مرتين يومياً بماء فاتر:</strong> يمنع تراكم الشوائب دون تسبيب احمرار.<br>
2. <strong>التكميل بمرطب كيوفي للوجه:</strong> يحفظ الترطيب الداخلي طوال اليوم.<br>
3. <strong>التجفيف اللطيف بالمنشفة بالطبطبة:</strong> يحافظ على استقرار حواجز الجلد.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الغسولات غير الرغوية لا تنظف الوجه جيداً."<br>
<strong>الحقيقة:</strong> غسول كيوفي الكريمي ينظف المسام ويزيل الأوساخ بفاعلية كاملة دون الحاجة للرغوة القاسية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>ترتبط جزيئات الجليسرين بماء الخلايا بينما تزيل الميكروسيرفاكتانتات الشوائب بأمان بيولوجي.</p>"""

    faqs = [
        ("ما هو غسول منظف ​​لطيف للوجه للبشرة الحساسة من كيوفي- 250 جم؟", "هو كريم غسول طبي خالي من الصابون والعطور من كيوفي بالجليسرين للبشرة الحساسة والجافة (250 جم)."),
        ("ما هي فوائد الجليسرين والتركيبة الخالية من الصابون للوجه؟", "تنظف الوجه بلطف، تحبس الترطيب لـ 24 ساعة، وتمنع الاحمرار والشد والجفاف."),
        ("هل ينظف الوجه ويرطب بدون صابون أو تهيج؟", "نعم، مثبت سريرياً في تنظيف البشرة الحساسة وتوفير نعومة وترطيب خالي من التهيج."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة مزودة بضاغط مريح سعة 250 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الوجه، ضعي كمية وكريميها، دلكي برفق واشطفي بالماء مرتين يومياً."),
        ("هل هو خالٍ من العطور واللانولين والبارابين؟", "نعم، 100% خالٍ من العطور واللانولين والبارابين ومختبر درماتولوجياً."),
        ("أين صُنع غسول كيوفي اللطيف للوجه؟", "صُنع في أستراليا بواسطة Ego Pharmaceuticals."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كيوفي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب البشرة المفرطة الحساسية والمصابة بالوردية؟", "نعم، ممتاز للبشرة الحساسة، الجافة، المفرطة التحسس والمصابة بالوردية."),
        ("هل يترك الوجه ناعماً ومرطباً دون شد؟", "نعم، يترك الوجه ناعماً كالحرير ومرطباً دون أي شعور بالشد."),
        ("هل عبوة 250 جم بضاغط مريحة؟", "نعم، عبوة أنيقة بضاغط مريح جداً للاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كيوفي الماركة الأولى طبياً في أستراليا؟", "نعم، QV الماركة رقم 1 الموصى بها طبياً في أستراليا."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل يزيل المكياج والأوساخ؟", "نعم، يزيل المكياج اليومي والأوساخ بفاعلية كاملة ولطف."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يسبب انسداد المسام؟", "لا، تركيبة خالية من الزيوت وغير مسببة للانسداد (Non-Comedogenic)."),
        ("هل يناسب الأطفال والبالغين؟", "نعم، آمن وممتاز للجميع من سن 3 سنوات."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يفضل اتباع مرطب كيوفي بعده؟", "نعم، يُفضل استخدام مرطب كيوفي بعد الغسل للحفاظ على الطراوة."),
        ("هل يناسب الصيف والشتاء؟", "نعم، ترطيب وتنظيف طبي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن العناية؟", "نعم، منتج طبي فاخر وأساسي لكل روتين عناية."),
        ("هل يعيد المظهر الناعم السلس للوجه؟", "نعم، يجعل الوجه في غاية النعومة والنقاء."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>QV Gentle Facial Cleanser for Sensitive Skin - 250g</strong> is the world's most dermatologist-recommended authentic luxury medical hydrating facial cleanser cream from QV designed to clean, clarify, and moisturize sensitive and extra-sensitive facial skin without causing stinging, redness, or lipid barrier stripping. Built upon intensive hydrating Glycerin, a 100% soap-free fragrance-free formula, and balanced pH (pH 6.0).</p>
<p>QV Gentle Facial Cleanser smoothly cleanses facial dirt, light makeup, and impurities, shields the face against severe dryness, and restores skin moisture balance, leaving your facial skin touchably silky soft, hydrated, spotlessly clean, and protected from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Ultra-Gentle Soap-Free Cleansing Cream for Sensitive Skin:</strong> Cleanses face without soap or irritation.</li>
  <li><strong>Extended Hydration with Medical Glycerin (15%):</strong> Prevents post-wash tight dry feeling.</li>
  <li><strong>Skin Barrier Protection with Balanced pH (pH 6.0):</strong> Preserves the natural biological flora of skin.</li>
  <li><strong>100% Soap-Free, Fragrance-Free, Oil-Free & Paraben-Free:</strong> Non-comedogenic formula that will not clog pores.</li>
  <li><strong>Dermatologist Recommended & Clinically Tested:</strong> Safe for sensitive face, lips, and eye areas.</li>
  <li><strong>Convenient 250g Pump Dispenser Bottle:</strong> Ideal format for continuous daily family care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet facial skin with warm water during cleansing.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of QV cleanser cream and massage face gently in smooth circular motions.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and pat face dry (use twice daily morning & night).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Medical Grade Glycerin (15%):</strong> Locks water molecules deep inside skin cells.</li>
  <li><strong>Soap-Free Cleansing Cream:</strong> Cleanses pores while preserving touchable facial softness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with sensitive or dry facial skin seeking QV Gentle Facial Cleanser 250g for gentle cleansing and hydration.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>QV (Ego)</td></tr>
  <tr><th>Category</th><td>Skincare / QV Medical Sensitive Cleansers 250g</td></tr>
  <tr><th>Product Type</th><td>Soap-Free Fragrance-Free Medical Gentle Facial Cleanser Cream (250g)</td></tr>
  <tr><th>Volume/Weight</th><td>250 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Sensitive, Dry, Ultra-Sensitive & Rosacea-Prone Facial Skin</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, spotlessly clean & redness-free face</td></tr>
  <tr><th>Texture</th><td>Smooth non-foaming liquid cleanser cream rinsing easily</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>Medical Glycerin, Soap-Free Cleansers (pH 6.0), Hydrating Paraffin</td></tr>
  <tr><th>Country of Origin</th><td>Australia</td></tr>
  <tr><th>Manufacturer</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 3+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Medical Glycerin Hydration & Soap-Free pH 6.0 Lipid Protection</h2>

<h3>What problem does this solve?</h3>
<p>QV Gentle Facial Cleanser resolves sensitive skin redness, stinging from harsh soaps, and post-wash facial dryness.</p>

<h3>Why choose QV Gentle Facial Cleanser?</h3>
<p>The soap-free pH 6.0 formula cleanses pores without disrupting delicate epidermal lipids or causing irritation.</p>"""

    en_faqs = [
        ("What is QV Gentle Facial Cleanser for Sensitive Skin - 250g?", "It is a medical soap-free fragrance-free cleansing cream from QV with Glycerin for sensitive and dry skin (250g)."),
        ("What are the benefits of Glycerin and the soap-free formula for face?", "Cleanse face gently, lock in 24-hour hydration, and prevent redness, tightness, and dryness."),
        ("Does it clean face and hydrate without soap or irritation?", "Yes, clinically proven to clean sensitive skin and deliver hydration without irritation."),
        ("What volume is contained in this bottle?", "250g pump dispenser bottle."),
        ("How do I use it correctly?", "Wet face, apply cream, massage gently and rinse with warm water twice daily."),
        ("Is it fragrance-free, lanolin-free, and paraben-free?", "Yes, 100% free from fragrances, lanolin, and parabens, and dermatologically tested."),
        ("Where is QV Gentle Cleanser manufactured?", "In Australia by Ego Pharmaceuticals."),
        ("How do I verify authenticity at Ekleel Abha?", "All QV products at Ekleel Abha are 100% original."),
        ("Is it suitable for ultra-sensitive and rosacea-prone skin?", "Yes, excellent for sensitive, dry, ultra-sensitive, and rosacea-prone skin."),
        ("Does it leave face soft and hydrated without tightness?", "Yes, leaves face touchably silky soft and hydrated without tight feeling."),
        ("Is the 250g pump bottle convenient?", "Yes, sleek pump dispenser bottle ideal for daily care."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is QV the #1 medical skincare brand in Australia?", "Yes, QV is the #1 dermatologist recommended brand in Australia."),
        ("How many times daily?", "Twice daily (morning and night)."),
        ("Does it remove makeup and dirt?", "Yes, effectively cleanses daily makeup and impurities gently."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it clog pores?", "No, oil-free non-comedogenic formula."),
        ("Is it suitable for adults and children?", "Yes, safe and suitable for everyone aged 3+."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is following with a QV moisturizer recommended?", "Yes, follow with a QV facial moisturizer after cleansing."),
        ("Is it good for all seasons?", "Yes, ideal medical cleansing for summer and winter."),
        ("Is it a nice skincare gift?", "Yes, a premier medical essential for daily facial care."),
        ("Does it restore smooth touchable face skin?", "Yes, gives facial skin a healthy smooth clean look."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2096",
        "sku": "EK-2096",
        "gtin": "9314839012723",
        "brand": "QV",
        "ar": {
            "title": "غسول منظف ​​لطيف للوجه للبشرة الحساسة  من كيوفي- 250 جم",
            "meta_title": "غسول كيوفي اللطيف للوجه للبشرة الحساسة 250جم | إكليل أبها",
            "meta_description": "اشتري غسول منظف لطيف للوجه للبشرة الحساسة من كيوفي (250 جم). كريم طبي خالي من الصابون والعطور بالجليسرين لترطيب وتنظيف الوجه الحساس. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كيوفي", "غسول_كيوفي_للوجه", "غسول_البشرة_الحساسة", "غسول_بدون_صابون", "إكليل_أبها"]
        },
        "en": {
            "title": "QV Gentle Facial Cleanser for Sensitive Skin - 250g",
            "meta_title": "QV Gentle Facial Cleanser Sensitive Skin 250g | Ekleel Abha",
            "meta_description": "Buy original QV Gentle Facial Cleanser for Sensitive Skin (250g). Soap-free fragrance-free medical gentle cleanser cream. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["qv", "qv_gentle_cleanser", "sensitive_face_wash", "soap_free_cleanser", "ekleel_abha"]
        }
    }


def create_product_2097():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم للعناية بكعب القدم من كيوفي 50 جم (QV Heel Balm - 50g)</strong> كريم الترميم والتقشير الطبي الفاخر الأكثر توصية عالمياً من كيوفي (QV) المصمم خصيصاً لترميم، تقشير، وتنعيم كعوب الأقدام المتشققة والصلبة والجافة جداً وإزالة الجلد الميت الخشن والشقوق المؤلمة. يرتكز هذا الكريم الأصيل (QV Heel Balm 50g) على مجمع اليوريا بتركيز 10% (Urea 10%)، حمض التشيلي (Sodium Lactate)، البارافين الطبي، والمركبات المطرية لأنسجة القدمين.</p>
<p>يعمل كريم كيوفي لكعب القدمين على إذابة القشور القرنية السميكة، حبس الترطيب لـ 24 ساعة، وإعادة البناء البيولوجي لكعب القدم، ليترك أقدامك ناعمة كالحرير، ممتلئة بالنضارة، خالية من التشققات، ومحمية من التضرر والخشونة من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترميم وتقشير طبي لكعوب الأقدام المتشققة بتركيز 10% يوريا:</strong> يذيب الجلد الميت الصلب.</li>
  <li><strong>التئام سريع للشقوق والجنزرة المؤلمة بكعب القدم:</strong> يغذي الأنسجة المتضررة عمقاً.</li>
  <li><strong>ترطيب وتنعيم مكثف لـ 24 ساعة بالبارافين الطبي:</strong> يحفظ الترطيب الداخلي للأقدام الجافة.</li>
  <li><strong>تركيبة خالية 100% من العطور واللانولين والمواد المهيجة:</strong> تناسب الأقدام الحساسة والسكريين.</li>
  <li><strong>موصى به من أطباء الجلدية وأخصائيي العناية بالأقدام:</strong> كريم العلاج الشامل للكعبين.</li>
  <li><strong>أنبوب مدمج سعة 50 جم:</strong> حجم ممتاز للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> اغسلي وجففي بشرة القدمين وكعوب الأقدام جيداً بالماء الدافئ.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من كريم كيوفي هيل بالم على كعوب الأقدام والمناطق المتشققة.</li>
  <li><strong>الخطوة الثالثة:</strong> دلكي برفق حتى الامتصاص (يُستعمل مرتين يومياً صباحاً ومساءً وقبل النوم).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>اليوريا بتركيز 10% (Urea 10%):</strong> تقشر القشور الصلبة ميكانيكياً وتحبس رطوبة الجلد.</li>
  <li><strong>صوديوم لاكتات والبارافين الطبي:</strong> يلينان الجلد القاسي وينعمان الكعبين الحريريين.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة كعوب الأقدام والجلد الصلب.</li>
  <li>لا يُستخدم على الجروح المفتوحة والنزيف الشديد.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من تشقق وخشونة كعوب الأقدام ويبحث عن كريم كيوفي هيل بالم 50 جم للترميم والتقشير.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كيوفي (QV Ego)</td></tr>
  <tr><th>الفئة</th><td>العناية بالأقدام / كريمات ومستحضرات كيوفي لكعب القدمين 50g</td></tr>
  <tr><th>نوع المنتج</th><td>كريم طبي مقشر ومصلح لكعوب الأقدام المتشققة بـ 10% يوريا (50g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>كعوب الأقدام المتشققة، الصلبة، الجافة جداً ومصابي السكري</td></tr>
  <tr><th>المظهر النهائي</th><td>أقدام ناعمة كالحرير، مرطبة 24 ساعة، ممتلئة وخالية من التشققات والقشور الصلبة</td></tr>
  <tr><th>الملمس</th><td>كريم دسم غني يمتص بسلاسة دون لزوجة زلقة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>يوريا 10%، صوديوم لاكتات، بارافين طبي، مرطبات أقدام</td></tr>
  <tr><th>بلد المنشأ</th><td>أستراليا (Australia)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد اليوريا بتركيز 10% في كريم كعب القدم من كيوفي (QV Heel Balm)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم كيوفي لكعب القدم مشكلة الشقوق العميقة الكعبية، خشونة الجلد الصلب، التقشر، والألم أثناء المشي.</p>

<h3>لماذا تنجح تركيبة QV Heel Balm 10% Urea؟</h3>
<p>لأن اليوريا بتركيز 10% تعمل كمذيب قرني (Keratolytic) يفكك الروابط البروتينية بين القشور الصلبة محفزاً تجدد الجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق مرتين يومياً صباحاً ومساءً:</strong> يسرع التئام الشقوق الكعبية.<br>
2. <strong>ارتداء جوارب قطنية بعد التطبيق ليلاً:</strong> يضاعف امتصاص اليوريا والترميم.<br>
3. <strong>تجنب استخدام المبرد الحاد بقوة:</strong> يمنح الجلد فرصة للشفاء الطبيعي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات كعب القدم تسبب انزلاق القدم بداخل الحذاء."<br>
<strong>الحقيقة:</strong> كريم كيوفي ينفذ لعمق خلايا الجلد دون ترك طبقة لزجة زلقة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تذيب اليوريا وصوديوم لاكتات خلايا الكيراتين الصلبة مصلحة طبقة الأدمة الكعبية (Heel Dermis).</p>"""

    faqs = [
        ("ما هو كريم للعناية بكعب القدم من كيوفي 50 جم؟", "هو كريم طبي مقشر ومصلح لكعوب الأقدام المتشققة والصلبة بتركيز 10% يوريا من كيوفي (50 جم)."),
        ("ما هي فوائد اليوريا 10% والبارافين الطبي لكعب القدم؟", "تذيب اليوريا الجلد الميت الصلب، تلتئم الشقوق المؤلمة، ويحفظ البارافين الترطيب 24 ساعة."),
        ("هل يرمم الشقوق الكعبية الصلبة فورياً؟", "نعم، مثبت سريرياً في ترميم تشققات كعب القدم وتقشير الخشونة وتنعيم الأقدام."),
        ("ما حجم العبوة؟", "تأتي بأنبوب أنيق سعة 50 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اغسلي وجففي القدمين، ضعي كمية على الكعبين المتشققين ودلكي برفق مرتين يومياً وقبل النوم."),
        ("هل هو خالٍ من العطور واللانولين؟", "نعم، 100% خالٍ من العطور واللانولين ومختبر درماتولوجياً لمرضى السكري."),
        ("أين صُنع كريم كيوفي هيل بالم؟", "صُنع في أستراليا بواسطة Ego Pharmaceuticals."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كيوفي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب مريضي السكري والأقدام شديدة الجفاف؟", "نعم، آمن وممتاز جداً لمرضى السكري والأقدام شديدة الجفاف والشقوق."),
        ("هل يترك القدمين ناعمتين وغير زلقتين؟", "نعم، ينفذ بسلاسة ليترك الكعبين ناعمين دون لزوجة زلقة."),
        ("هل أنبوب 50 جم مناسب للجيب والحقيبة؟", "نعم، أنبوب أنيق مدمج مثالي للجيب والحقيبة والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كيوفي الماركة الأولى طبياً في العناية بالأقدام؟", "نعم، QV الماركة رقم 1 الموصى بها طبياً في أستراليا."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً وقبل النوم)."),
        ("هل ينصح بارتداء جوارب قطنية بعده ليلاً؟", "نعم، ارتداء جوارب قطنية يضاعف مفعول الترميم والتقشير."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في إزالة الجلد الميت الخشن؟", "نعم، يذيب اليوريا 10% الجلد الميت الخشن بسلاسة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يناسب الشتاء والصيف؟", "نعم، حماية وترميم طبي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن العناية؟", "نعم، منتج طبي فاخر وأساسي لكل روتين عناية بالأقدام."),
        ("هل يعيد المظهر الناعم السلس للأقدام؟", "نعم، يجعل الكعبين في غاية النعومة والنقاء."),
        ("هل تتوفر منتجات QV الأخرى؟", "نعم، تتوفر عائلة QV للعناية الجلدية كاملة لدى إكليل أبها."),
        ("هل يقلل الألم أثناء المشي؟", "نعم، التئام الشقوق يزيل الألم الناتج عن ضغط المشي."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>QV Heel Balm - 50g</strong> is the world's most dermatologist-recommended authentic luxury medical foot repairing and exfoliating cream from QV designed to repair, exfoliate, and smooth cracked, hard, and severely dry heels while eliminating painful flaking and thick dead skin. Built upon a 10% Urea complex (Urea 10%), Sodium Lactate, medical paraffin, and foot tissue emollient compounds.</p>
<p>QV Heel Balm dissolves thick hard calluses, locks in hydration for 24 hours, and biologically rebuilds heel skin tissue, leaving your feet touchably silky soft, plump, crack-free, and protected against roughness from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Medical Repair & Exfoliation for Cracked Heels with 10% Urea:</strong> Dissolves thick hard calluses.</li>
  <li><strong>Fast Healing for Painful Heel Cracks:</strong> Nourishes damaged deep skin tissue.</li>
  <li><strong>Intensive 24-Hour Hydration with Medical Paraffin:</strong> Locks in internal moisture for dry feet.</li>
  <li><strong>100% Fragrance-Free, Lanolin-Free & Irritant-Free:</strong> Safe for sensitive feet and diabetic skin care.</li>
  <li><strong>Dermatologist & Podiatrist Recommended Medical Brand:</strong> Comprehensive medical heel repair cream.</li>
  <li><strong>Compact 50g Tube:</strong> Ideal size for daily care and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wash and dry feet and heel skin thoroughly with warm water.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of QV Heel Balm onto cracked heels and callused zones.</li>
  <li><strong>Step 3:</strong> Massage gently until absorbed (use twice daily morning and night & before bedtime).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>10% Urea (Urea 10%):</strong> Mechanically dissolves hard calluses and seals in skin moisture.</li>
  <li><strong>Sodium Lactate & Medical Grade Paraffin:</strong> Soften tough skin leaving heels touchably smooth.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical foot and callus skin application only.</li>
  <li>Do not apply to open bleeding wounds.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from cracked, hard heels seeking QV Heel Balm 50g for medical repair and exfoliation.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>QV (Ego)</td></tr>
  <tr><th>Category</th><td>Foot Care / QV Medical Heel Repair Creams 50g</td></tr>
  <tr><th>Product Type</th><td>10% Urea Medical Repairing & Exfoliating Heel Balm (50g)</td></tr>
  <tr><th>Volume/Weight</th><td>50 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Cracked, Hard, Severely Dry Heels & Diabetic Feet</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, crack-healed & callus-free smooth feet</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-slippery creamy balm</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>10% Urea, Sodium Lactate, Medical Paraffin, Foot Hydrators</td></tr>
  <tr><th>Country of Origin</th><td>Australia</td></tr>
  <tr><th>Manufacturer</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 10% Urea Keratolysis & Heel Dermal Repair</h2>

<h3>What problem does this solve?</h3>
<p>QV Heel Balm resolves deep heel cracks, hard calluses, skin roughness, and walking pain.</p>

<h3>Why choose QV Heel Balm 10% Urea?</h3>
<p>Urea 10% acts as a keratolytic agent breaking down protein bonds between hardened scales accelerating healing.</p>"""

    en_faqs = [
        ("What is QV Heel Balm - 50g?", "It is a medical 10% Urea repairing and exfoliating heel balm from QV for cracked, hard, and dry heels (50g)."),
        ("What are the benefits of 10% Urea and medical paraffin for heels?", "Dissolve hard dead calluses, heal painful cracks, and lock in 24-hour hydration."),
        ("Does it repair cracked heels and dissolve hard skin instantly?", "Yes, clinically proven to repair cracked heels and exfoliate rough calluses."),
        ("What volume is contained in this tube?", "50g compact tube."),
        ("How do I use it correctly?", "Wash and dry feet, apply to cracked heels and massage gently twice daily."),
        ("Is it fragrance-free, lanolin-free, and safe for diabetics?", "Yes, 100% free from fragrances and lanolin, and dermatologically tested for diabetic foot care."),
        ("Where is QV Heel Balm manufactured?", "In Australia by Ego Pharmaceuticals."),
        ("How do I verify authenticity at Ekleel Abha?", "All QV products at Ekleel Abha are 100% original."),
        ("Is it suitable for diabetic feet and severely cracked heels?", "Yes, safe and excellent for diabetic foot care and severely cracked heels."),
        ("Does it leave feet soft and non-slippery?", "Yes, absorbs smoothly leaving heels touchably soft without slippery residue."),
        ("Is the 50g tube travel friendly?", "Yes, sleek compact tube ideal for handbag and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is QV the #1 podiatrist recommended brand in Australia?", "Yes, QV is the #1 dermatologist and podiatrist recommended brand in Australia."),
        ("How many times daily?", "Twice daily (morning, night & bedtime)."),
        ("Is wearing cotton socks overnight recommended?", "Yes, wearing cotton socks overnight doubles heel repair Efficacy."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it help dissolve hard dead calluses?", "Yes, 10% Urea smoothly dissolves thick dead calluses."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it good for all seasons?", "Yes, ideal medical heel repair for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, a premier medical essential for daily foot care."),
        ("Does it restore smooth touchable heel skin?", "Yes, gives heels a healthy smooth crack-free look."),
        ("Does it reduce walking pain?", "Yes, healing cracks eliminates pain caused by walking pressure."),
        ("Are other QV products available?", "Yes, the full QV medical skincare range is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2097",
        "sku": "EK-2097",
        "gtin": "9314839006876",
        "brand": "QV",
        "ar": {
            "title": "كريم  للعناية بكعب القدم  من كيوفي 50 جم",
            "meta_title": "كريم كيوفي هيل بالم لكعب القدم 50جم | إكليل أبها",
            "meta_description": "اشتري كريم للعناية بكعب القدم من كيوفي (50 جم). كريم طبي مصلح بـ 10% يوريا لترميم وتقشير الشقوق والكعوب الصلبة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كيوفي", "كريم_كعب_القدم_كيوفي", "كيوفي_هيل_بالم", "ترميم_تشققات_القدمين", "إكليل_أبها"]
        },
        "en": {
            "title": "QV Heel Balm - 50g",
            "meta_title": "QV Heel Balm 50g | Ekleel Abha",
            "meta_description": "Buy original QV Heel Balm (50g). 10% Urea medical repairing and exfoliating cracked heel balm. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["qv", "qv_heel_balm", "cracked_heel_cream", "urea_heel_balm", "ekleel_abha"]
        }
    }


def create_product_2098():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول للبشرة الجافة او الحساسة للغاية من كيوفي ، 250 مل (QV Wash for Dry or Sensitive Skin, 250 ml)</strong> سائل الاستحمام والتنظيف الطبي الفاخر الأكثر توصية عالمياً من كيوفي (QV) المصمم خصيصاً لتنظيف، تنقية، وترطيب بشرة الجسم والوجه الجافة للغاية والمفرطة الحساسية والمصابة بالأكزيما والصدفية دون تسبيب أي صابون حارق أو تجريد للحجاب الدهني. يرتكز هذا الغسول الأصيل (QV Wash 250ml) على الجليسرين المرطب المكثف (Glycerin 15%)، التركيبة الخالية 100% من الصابون والعطور، والمكونات متوازنة الحموضة (pH 6.0).</p>
<p>يعمل غسول كيوفي للبشرة الجافة أو الحساسة على تنظيف مسام الجسم والوجه بسلاسة، حماية الجلد من الحكة والتقشر والجفاف الشديد، وإعادة التوازن البيولوجي للبشرة، ليترك بشرتك ناعمة كالحرير، مرطبة، ناصعة النظافة، ومحمية من الحساسية من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف سائل لطيف جداً للبشرة الجافة للغاية والحساسة:</strong> ينظف دون صابون أو تهيج.</li>
  <li><strong>ترطيب وتغذية مكثفة لـ 24 ساعة بالجليسرين (15%):</strong> يمنع الشد والجفاف والحكة بعد الغسيل.</li>
  <li><strong>مناسب لبشرة الجسم والوجه والأكزيما والصدفية:</strong> تركيبة طبية شاملة آمنة.</li>
  <li><strong>تركيبة خالية 100% من الصابون والعطور والزيوت والبارابين:</strong> لا تسبب انسداد المسام.</li>
  <li><strong>موصى به من أطباء الجلدية ومناسب للأطفال والكبار:</strong> غسول العناية العائلية الشاملة.</li>
  <li><strong>عبوة سعة 250 مل مزودة بضاغط مريح:</strong> حجم ممتاز للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الوجه والجسم بالماء الدافئ أثناء الاستحمام أو الغسيل.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسية من سائل كيوفي ودلكي البشرة برفق برغوة ناعمة.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء وجففي البشرة برفق (يُستعمل مرتين يومياً صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الجليسرين الطبي المكثف (Glycerin 15%):</strong> يحبس جزيئات الماء داخل خلايا الجلد.</li>
  <li><strong>المنظفات السائلة الخالية من الصابون (pH 6.0):</strong> تنظف المسام وتحفظ النعومة الحريرية للبشرة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يملك بشرة جافة أو حساسة للغاية ويبحث عن غسول كيوفي الطبي 250 مل للتنظيف والترطيب الشامل.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كيوفي (QV Ego)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم والوجه / غسولات كيوفي الطبية للبشرة الجافة والحساسة 250ml</td></tr>
  <tr><th>نوع المنتج</th><td>سائل غسول طبي مرطب خالي من الصابون والعطور للبشرة الجافة والحساسة (250ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>250 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الجافة للغاية، الحساسة، المصابة بالأكزيما والصدفية (للوجه والجسم)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة كالحرير، مرطبة 24 ساعة، ناصعة النظافة وخالية من الحكة والشد</td></tr>
  <tr><th>الملمس</th><td>سائل جل شفاف لطيف رغوي ينشطف بالماء بسهولة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>جليسرين طبي (15%)، منظفات خالية من الصابون (pH 6.0)، بارافين مرطب</td></tr>
  <tr><th>بلد المنشأ</th><td>أستراليا (Australia)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من عمر يوم لحديثي الولادة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الجليسرين الطبي الخالي من الصابون في غسول كيوفي (QV Wash)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول كيوفي للبشرة الجافة والحساسة مشكلة الحكة الشديدة، الأكزيما، تقشر الجلد، وحرقان الصابون التقليدي.</p>

<h3>لماذا تنجح تركيبة QV Wash Soap-Free?</h3>
<p>لأن الجليسرين بتركيز 15% والتركيبة الخالية من الصابون تحفظ التوازن المائي دون تدمير الأغشية الدهنية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام اليومي بماء دافئ أثناء الاستحمام:</strong> ينظف الجلد دون تسبيب جفاف.<br>
2. <strong>التكميل بمرطب كيوفي كريم بعد الشطف:</strong> يحبس الترطيب طوال 24 ساعة.<br>
3. <strong>التجفيف اللطيف بالمنشفة بالطبطبة:</strong> يحافظ على استقرار حواجز البشرة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الغسولات الطبية الخالية من الصابون لا تنظف الجسم بفاعلية."<br>
<strong>الحقيقة:</strong> غسول كيوفي ينظف المسام بفاعلية كاملة مخلِفاً بشرة مطهرة ونقية دون أي صابون ضار.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تحتجز جزيئات الجليسرين الماء داخل الأدمة بينما تزيل السورفاكتانتات اللطيفة الشوائب بأمان بيولوجي.</p>"""

    faqs = [
        ("ما هو غسول للبشرة الجافة او الحساسة للغاية من كيوفي ، 250 مل؟", "هو سائل غسول طبي خالي من الصابون والعطور من كيوفي بالجليسرين للبشرة الجافة للغاية والحساسة (250 مل)."),
        ("ما هي فوائد الجليسرين 15% والتركيبة الخالية من الصابون؟", "تنظف الوجه والجسم بلطف، تحبس الترطيب لـ 24 ساعة، وتمنع الحكة والشد والجفاف بالأكزيما."),
        ("هل ينظف ويرطب دون صابون أو تهيج للبشرة الجافة والحساسة؟", "نعم، مثبت سريرياً في تنظيف البشرة الجافة والحساسة وتوفير نعومة وترطيب خالي من التهيج."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة مزودة بضاغط مريح سعة 250 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الوجه والجسم، ضعي كمية وكوّني رغوة ناعمة، دلكي برفق واشطفي بالماء يومياً."),
        ("هل هو خالٍ من العطور واللانولين والبارابين؟", "نعم، 100% خالٍ من العطور واللانولين والبارابين ومختبر درماتولوجياً."),
        ("أين صُنع غسول كيوفي للبشرة الجافة والحساسة؟", "صُنع في أستراليا بواسطة Ego Pharmaceuticals."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كيوفي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب البشرة المصابة بالأكزيما والصدفية وللأطفال؟", "نعم، ممتاز لبشرة الأطفال والبالغين المصابة بالأكزيما والصدفية والحساسية الشديدة."),
        ("هل يترك البشرة ناعمة ومرطبة دون حكة؟", "نعم، يترك البشرة ناعمة كالحرير ومرطبة دون أي شعور بالحكة."),
        ("هل عبوة 250 جم بضاغط مريحة؟", "نعم، عبوة أنيقة بضاغط مريح جداً للاستخدام اليومي في الشاور."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كيوفي الماركة الأولى طبياً في أستراليا؟", "نعم، QV الماركة رقم 1 الموصى بها طبياً في أستراليا."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً أثناء الاستحمام أو الغسيل."),
        ("هل يناسب الوجه والجسم معاً؟", "نعم، غسول طبي شامل مخصص لبشرة الوجه والجسم معا."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يسبب انسداد المسام؟", "لا، تركيبة خالية من الزيوت وغير مسببة للانسداد (Non-Comedogenic)."),
        ("هل يناسب حديثي الولادة والأطفال؟", "نعم، آمن وممتاز لحديثي الولادة والأطفال والبالغين."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يفضل اتباع مرطب كيوفي بعده؟", "نعم، يُفضل استخدام كريم مرطب كيوفي بعد الغسل للحفاظ على الطراوة."),
        ("هل يناسب الصيف والشتاء؟", "نعم، ترطيب وتنظيف طبي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن العناية؟", "نعم، منتج طبي فاخر وأساسي لكل روتين عناية."),
        ("هل يعيد المظهر الناعم السلس للبشرة؟", "نعم، يجعل البشرة في غاية النعومة والنقاء."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>QV Wash for Dry or Sensitive Skin, 250 ml</strong> is the world's most dermatologist-recommended authentic luxury medical hydrating body and facial wash liquid from QV designed to clean, purify, and moisturize severely dry, sensitive, and eczema-prone skin without harsh soap stinging or lipid stripping. Built upon intensive hydrating Glycerin (15%), a 100% soap-free fragrance-free formula, and balanced pH (pH 6.0).</p>
<p>QV Medical Wash smoothly cleanses facial and body pores, shields skin against itchiness, flaking, and severe dryness, and restores biological skin balance, leaving your skin touchably silky soft, hydrated, spotlessly clean, and protected against sensitivity from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Ultra-Gentle Soap-Free Liquid Wash for Very Dry & Sensitive Skin:</strong> Cleanses without soap or irritation.</li>
  <li><strong>Intensive 24-Hour Hydration with Glycerin (15%):</strong> Prevents post-wash tight dry itching feeling.</li>
  <li><strong>Suitable for Face, Body, Eczema & Psoriasis Skin Care:</strong> Comprehensive safe medical formulation.</li>
  <li><strong>100% Soap-Free, Fragrance-Free, Oil-Free & Paraben-Free:</strong> Non-comedogenic formula that will not clog pores.</li>
  <li><strong>Dermatologist Recommended for Babies & Adults:</strong> Universal medical family cleansing wash.</li>
  <li><strong>Convenient 250ml Pump Dispenser Bottle:</strong> Ideal format for daily continuous bath routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet facial and body skin with warm water during shower or washing.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of QV liquid wash, work into a gentle lather, and massage skin.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with water and pat skin dry (use twice daily morning & night).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Medical Grade Glycerin (15%):</strong> Locks water molecules deep inside skin cells.</li>
  <li><strong>Soap-Free Liquid Cleansers (pH 6.0):</strong> Cleanse pores while preserving touchable silky softness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and body skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with very dry or sensitive skin seeking QV Wash 250ml for medical cleansing and hydration.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>QV (Ego)</td></tr>
  <tr><th>Category</th><td>Skincare / QV Medical Dry & Sensitive Washes 250ml</td></tr>
  <tr><th>Product Type</th><td>Soap-Free Fragrance-Free Medical Hydrating Body & Face Liquid Wash (250ml)</td></tr>
  <tr><th>Volume/Weight</th><td>250 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Very Dry, Sensitive, Eczema & Psoriasis-Prone Skin (Face & Body)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, spotlessly clean & itch-free skin</td></tr>
  <tr><th>Texture</th><td>Clear fast-foaming lightweight gentle liquid gel</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>Medical Glycerin (15%), Soap-Free Cleansers (pH 6.0), Hydrating Paraffin</td></tr>
  <tr><th>Country of Origin</th><td>Australia</td></tr>
  <tr><th>Manufacturer</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 0+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Medical Glycerin 15% Hydration & Soap-Free pH 6.0 Barrier Preservation</h2>

<h3>What problem does this solve?</h3>
<p>QV Wash for Dry or Sensitive Skin resolves severe skin itchiness, eczema flaking, stinging from soap, and post-shower dryness.</p>

<h3>Why choose QV Wash?</h3>
<p>The soap-free pH 6.0 formula cleanses skin pores effectively without stripping natural protective skin lipids.</p>"""

    en_faqs = [
        ("What is QV Wash for Dry or Sensitive Skin, 250 ml?", "It is a medical soap-free fragrance-free liquid wash from QV with Glycerin for very dry and sensitive skin (250ml)."),
        ("What are the benefits of 15% Glycerin and the soap-free formula?", "Cleanse face and body gently, lock in 24-hour hydration, and prevent itchiness, tightness, and eczema dryness."),
        ("Does it clean and hydrate without soap or irritation for dry sensitive skin?", "Yes, clinically proven to clean dry sensitive skin and deliver hydration without irritation."),
        ("What volume is contained in this bottle?", "250ml pump dispenser bottle."),
        ("How do I use it correctly?", "Wet skin, apply liquid wash, lather gently, massage and rinse with water daily."),
        ("Is it fragrance-free, lanolin-free, and paraben-free?", "Yes, 100% free from fragrances, lanolin, and parabens, and dermatologically tested."),
        ("Where is QV Wash manufactured?", "In Australia by Ego Pharmaceuticals."),
        ("How do I verify authenticity at Ekleel Abha?", "All QV products at Ekleel Abha are 100% original."),
        ("Is it suitable for eczema, psoriasis, newborns, and adults?", "Yes, safe and excellent for newborns, babies, adults, eczema, and psoriasis skin care."),
        ("Does it leave skin soft and hydrated without itching?", "Yes, leaves skin touchably silky soft and hydrated without tight itching feeling."),
        ("Is the 250ml pump bottle convenient for showering?", "Yes, sleek pump dispenser bottle ideal for daily shower use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is QV the #1 medical skincare brand in Australia?", "Yes, QV is the #1 dermatologist recommended brand in Australia."),
        ("How many times daily?", "Once or twice daily during shower or bath."),
        ("Is it suitable for face and body together?", "Yes, versatile medical cleanser for facial and body skin."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it clog pores?", "No, oil-free non-comedogenic formula."),
        ("Is it suitable for newborns and babies?", "Yes, safe and mild for newborns, babies, and adults."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is following with a QV moisturizing cream recommended?", "Yes, follow with a QV moisturizing cream after washing to lock in hydration."),
        ("Is it good for all seasons?", "Yes, ideal medical hydration for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, a premier medical essential for daily family bath routines."),
        ("Does it restore smooth touchable skin?", "Yes, gives facial and body skin a healthy smooth clean look."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2098",
        "sku": "EK-2098",
        "gtin": "9314839008948",
        "brand": "QV",
        "ar": {
            "title": "غسول للبشرة الجافة او الحساسة للغاية من كيوفي ، 250 مل",
            "meta_title": "غسول كيوفي للبشرة الجافة والحساسة 250مل | إكليل أبها",
            "meta_description": "اشتري غسول للبشرة الجافة أو الحساسة للغاية من كيوفي (250 مل). سائل طبي خالي من الصابون والعطور بالجليسرين لترطيب الوجه والجسم والأكزيما. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كيوفي", "غسول_كيوفي_للبشرة_الجافة", "غسول_الأكزيما", "سائل_استحمام_كيوفي", "إكليل_أبها"]
        },
        "en": {
            "title": "QV Wash for Dry or Sensitive Skin, 250 ml",
            "meta_title": "QV Wash for Dry or Sensitive Skin 250ml | Ekleel Abha",
            "meta_description": "Buy original QV Wash for Dry or Sensitive Skin (250ml). Soap-free fragrance-free medical hydrating body and facial wash liquid. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["qv", "qv_wash", "dry_skin_wash", "eczema_wash", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 75 builders complete")
