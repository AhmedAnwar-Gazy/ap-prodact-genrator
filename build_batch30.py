import json, os

def create_product_1856():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>سيروم للشعر شديد الجفاف والمجعد الفيف اكسترا اورديناري من لوريال 100مل (L'Oréal Elvive Extraordinary Oil Serum - 100ml)</strong> مستحضر التغذية والتصفيف الفاخر والأكثر شهرة عالمياً لعلاج هيشان الشعر، تنعيم الأطراف المتقصفة، ومنح الشعر جفافاً وحيوية ساحرة دون تثقيل. يرتكز هذا السيروم الغني من لوريال باريس (L'Oréal Elvive Extraordinary Oil) على تكنولوجيا خلط 6 زيوت زهرية نادرة (6 Precious Flower Oils) لغمر ألياف الشعر بالترطيب العميق.</p>
<p>يمتاز سيروم الفيف اكسترا اورديناري بقوام زيتي مخملي غير لزج ينفذ في عمق ألياف الشعر فورياً، حيث يغلف كل شعرة بغشاء واقٍ ضد الحرارة والتطاير، ليترك شعركِ ناعماً كالحرير، مشرقاً بلمعان ماسي، وسهل التسريح طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترميم وتغذية مكثفة للـ 6 زيوت الزهرية النادرة:</strong> يغذي ألياف الشعر شديد الجفاف من الجذور للأطراف.</li>
  <li><strong>ضبط الهيشان والتطاير لـ 48 ساعة:</strong> ينعم الأطراف المتقصفة ويمنع تطاير الشعر في الرطوبة.</li>
  <li><strong>حماية من الحرارة حتى 230 درجة مئوية:</strong> يحمي الشعر من أضرار الاستشوار والمكواة قبل التصفيف.</li>
  <li><strong>ملمس مخملي خفيف 100% غير لزج:</strong> ينفذ فورياً بالبشرة والشعر دون ترك أي لزوجة زيتية ثقيلة.</li>
  <li><strong>لمعان ماسي ونعومة حريرية ساحرة:</strong> يعيد البريق واللمعان للشعر المجهد والمصبوغ.</li>
  <li><strong>عبوة زجاجية فاخرة بمضخة سعة 100 مل:</strong> حجم ممتازة ومناسب للاستخدام اليومي وقبل التصفيف.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (المكيال):</strong> اضغطي 1 إلى 2 ضغطة من سيروم لوريال الفيف على كف اليد.</li>
  <li><strong>الخطوة الثانية (التوزيع):</strong> فركي السيروم بين اليدين ووزعيه بالتساوي على الشعر المبلل أو الجاف من المنتصف حتى الأطراف.</li>
  <li><strong>الخطوة الثالثة (التصفيف):</strong> استعمليه قبل السشوار للحماية الحرارية، أو بعده لإضافة لمعان وضبط الهيشان.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مزيج الـ 6 زيوت الزهرية الثمينة (Lotus, Camomile, Rose, Flax):</strong> تغذي وتطري جذع الشعرة.</li>
  <li><strong>سيليكونات خفيفة للحماية الحرارية:</strong> تغلف الشعرة وتمنع تقصف وتكسر الأطراف.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على ألياف الشعر فقط.</li>
  <li>تجنبي ملامسة السيروم المباشرة للعينين أو الفروة المصابة بجروح.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن النار.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تعاني من الشعر شديد الجفاف، الهيشان، والتقصف وتفتش عن سيروم لوريال الفيف اكسترا اورديناري بالزيوت الزهرية.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لوريال الفيف (L'Oréal Elvive)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / سيروم وزيوت تغذية وتصفيف الشعر الفاخرة</td></tr>
  <tr><th>نوع المنتج</th><td>سيروم زيوت زهرية مغذية للحماية والتنعيم (100ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>الشعر شديد الجفاف، المجعد، والمتقصف</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم كالحرير، مشرق بلمعان ماسي، مضبوط الهيشان ومحمي من الحرارة</td></tr>
  <tr><th>الملمس</th><td>سيروم زيتي مخملي خفيف للغاية سريع الامتصاص</td></tr>
  <tr><th>العطر</th><td>عطر لوريال الزهري الشاذ الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>6 زيوت زهرية نادرة، مركبات الحماية الحرارية</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا / مصر (L'Oréal Paris)</td></tr>
  <tr><th>الشركة المصنعة</th><td>L'Oréal Paris</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 10 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الـ 6 زيوت الزهرية في سيروم الفيف (L'Oréal Extraordinary Oil)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج سيروم لوريال الفيف مشكلة جفاف الشعر شديد الخشونة، هيشان وتطاير الأطراف، وتلف الشعر الناتج عن حرارة السشوار والمكواة.</p>

<h3>لماذا تنجح تقنية الزيوت الزهرية الثمينة؟</h3>
<p>لأن خلاصة زيوت اللوتس والورد والكتان تمتلك جزيئات متناهية الصغر تخترق جذع الشعرة، فتغذي البروتينات وتثبت الترطيب.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق قبل التصفيف الحراري:</strong> وضعي السيروم على الشعر الرطب لحمايته من حرارة المكواة 230C.<br>
2. <strong>التركيز على الأطراف:</strong> دلكي أطراف الشعر الجافة بالسيروم لمنع التقصف.<br>
3. <strong>اللمسة الأخيرة (Finishing Touch):</strong> استخدمي قطرة واحدة على الشعر الجاف لإعطاء لمعان ماسي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "زيوت السيراميد والسيروم تجعل الشعر دهنياً وثقيلاً."<br>
<strong>الحقيقة:</strong> سيروم الفيف اكسترا اورديناري مصمم بتركيبة زهرية ناصعة ينفذ فورياً بالبصيلة دون أي ثقل دهني.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبت الدهون الزهرية غشائاً هيدروفوبياً فوق الطبقة القرنية للشعرة (Cuticle)، فيمنع امتصاص رطوبة الجو المسببة للهيشان.</p>"""

    faqs = [
        ("ما هو سيروم للشعر شديد الجفاف والمجعد الفيف اكسترا اورديناري من لوريال 100مل؟", "هو سيروم تصفيف وتغذية فاخر من لوريال غني بـ 6 زيوت زهرية نادرة لترميم وضبط هيشان الشعر شديد الجفاف 100 مل."),
        ("ما هي فوائد الـ 6 زيوت الزهرية النادرة؟", "تغذي ألياف الشعر الجاف، تضبط الهيشان لـ 48 ساعة، وتحمي الشعر من الحرارة حتى 230 درجة."),
        ("هل يوفر حماية من حرارة المكواة والاستشوار؟", "نعم، مثبت سريرياً في حماية ألياف الشعر من أضرار الحرارة حتى 230C."),
        ("ما حجم ونوع العبوة؟", "تأتي في عبوة زجاجية فاخرة بمضخة سعة 100 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اضغطي 1-2 ضغطة، وزعي على الشعر المبلل أو الجاف من المنتصف للأطراف قبل أو بعد التصفيف."),
        ("هل يترك أثراً دهنياً ثقيلاً على الشعر؟", "لا، فورمولا مخملية خفيفة تنفذ فورياً وتترك الشعر ناعماً دون لزوجة."),
        ("ما هو بلد صنع سيروم لوريال الفيف؟", "صُنع بواسطة شركة لوريال باريس (L'Oréal Paris) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات لوريال لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يمنع تقصف وتطاير الأطراف؟", "نعم، يغلف الأطراف المتقصفة ويمنع تطاير الشعر في الرطوبة."),
        ("ما هي رائحة سيروم الفيف اكسترا اورديناري؟", "يتميز برائحة زهرية ساحرة وفخمة تدوم بالنسيم."),
        ("هل يناسب جميع أنواع الشعر الجاف والمصبوغ؟", "نعم، ممتاز للشعر الجاف، المجعد، المصبوغ، والمعالج بالبروتين."),
        ("هل العبوة 100 مل مناسبة للاستخدام اليومي؟", "نعم، حجم وافر بمضخة دقيقة تكفي لعدة أشهر من التصفيف."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ العبوة الزجاجية في مكان بارد وجاف بعيداً عن الحرارة."),
        ("هل يمنح لمعاناً ماسياً للشعر؟", "نعم، يعيد البريق واللمعان الماسي للشعر المجهد."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة زجاجية أنيقة بمضخة لولبية محكمة الإغلاق."),
        ("هل يمكن استخدامه على الشعر الجاف بعد التصفيف؟", "نعم، يُستخدم كـ لمسة أخير على الشعر الجاف لزيادة اللمعان."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل عند الحاجة للتصفيف أو الترطيب اليومي."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع الفئات العمرية للنساء والرجال."),
        ("هل يناسب تصفيف الشعر الكيرلي؟", "نعم، ممتاز لترطيب وتحديد خصلات الشعر الكيرلي والمتموج."),
        ("هل هو سيروم الزيوت الأكثر مبيعاً عالمياً؟", "نعم، سيروم لوريال الفيف اكسترا اورديناري الأكثر شهرة عالمياً."),
        ("هل يمنح حس أنوثة وفخامة؟", "نعم، النعومة والعطر الفاخر يمنحانكِ شعوراً مطلقاً بالأناقة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة زجاجية صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يسهل تسريح وفك تشابك الشعر؟", "نعم، يسهل تمشيط وفك تشابك الشعر المبلل والجاف."),
        ("هل يترك الشعر طرياً؟", "نعم، يترك ألياف الشعر ب طراوة ونعومة حريرية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>L'Oréal Elvive Extraordinary Oil Serum for Very Dry and Frizzy Hair - 100ml</strong> is the world's #1 best-selling luxury hair oil serum engineered to tame frizz, seal split ends, and deliver 24-hour weightless hair nourishment. Formulated by L'Oréal Paris (Elvive Extraordinary Oil), it blends 6 Precious Flower Oils.</p>
<p>L'Oréal Elvive Extraordinary Oil Serum features a non-greasy velvety fluid matrix that penetrates hair fibers instantly, enveloping each strand in a protective shield against heat up to 230°C and humidity, leaving your hair touchably soft, shiny, and easy to style.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intense 6 Precious Flower Oils Nutrition:</strong> Deeply nourishes very dry hair from roots to ends.</li>
  <li><strong>48-Hour Frizz Control & Humidity Shield:</strong> Smooths rough split ends and halts humidity flyaways.</li>
  <li><strong>Heat Protection Up to 230°C:</strong> Shields hair fibers from blow-dryers and flat irons prior to styling.</li>
  <li><strong>100% Weightless Non-Greasy Velvety Texture:</strong> Absorbs instantly into hair fibers without oily weight.</li>
  <li><strong>Diamond Shine & Silky Touch:</strong> Restores brilliant shine and suppleness to damaged, color-treated hair.</li>
  <li><strong>Luxury 100ml Glass Pump Bottle:</strong> High-value bottle ideal for daily grooming and pre-styling care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Pump):</strong> Dispense 1 to 2 pumps of L'Oréal Elvive serum onto the palm of your hand.</li>
  <li><strong>Step 2 (Distribute):</strong> Rub palms together and distribute evenly through damp or dry hair lengths to ends.</li>
  <li><strong>Step 3 (Style):</strong> Apply before blow-drying for heat defense, or post-styling for finishing shine and frizz control.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>6 Precious Flower Oils Blend (Lotus, Camomile, Rose, Flax):</strong> Nourish and soften dry hair strands.</li>
  <li><strong>Lightweight Protective Heat Polymers:</strong> Shield hair cuticles and prevent end breakage up to 230°C.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hair application only.</li>
  <li>Avoid direct contact with eyes or wounded scalp.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from heat.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with very dry, frizzy, or heat-styled hair seeking L'Oréal Elvive's 6 Flower Oils Extraordinary Oil Serum.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>L'Oréal Elvive</td></tr>
  <tr><th>Category</th><td>Hair Care / Luxury Nourishing Hair Oil Serums & Heat Protectants</td></tr>
  <tr><th>Product Type</th><td>6 Precious Flower Oils Hair Nourishing & Heat Serum (100ml)</td></tr>
  <tr><th>Volume/Weight</th><td>100 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Very Dry, Frizzy, Damaged & Color-Treated Hair</td></tr>
  <tr><th>Finish</th><td>Touchably soft, diamond shiny, frizz-controlled & heat-protected hair</td></tr>
  <tr><th>Texture</th><td>Lightweight velvety non-greasy hair oil fluid</td></tr>
  <tr><th>Fragrance</th><td>Luxurious floral L'Oréal fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>6 Precious Flower Oils, Heat-Protective Polymers</td></tr>
  <tr><th>Country of Origin</th><td>France / Egypt (L'Oréal Paris)</td></tr>
  <tr><th>Manufacturer</th><td>L'Oréal Paris</td></tr>
  <tr><th>Age Group</th><td>All Ages (10+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 6 Precious Flower Oils & 230°C Thermal Defense</h2>

<h3>What problem does this solve?</h3>
<p>L'Oréal Elvive Extraordinary Oil Serum resolves severe hair dryness, split end frizz, and heat damage from styling tools.</p>

<h3>Why choose L'Oréal Elvive Extraordinary Serum?</h3>
<p>Micro-flower oil lipids penetrate the cortex to restructure damaged keratin, while heat polymers form a 230°C thermal barrier.</p>"""

    en_faqs = [
        ("What is L'Oréal Elvive Extraordinary Oil Serum 100ml?", "It is a luxury hair oil serum infused with 6 Precious Flower Oils to nourish dry hair, tame frizz, and protect against heat up to 230°C."),
        ("What are the benefits of 6 Precious Flower Oils?", "Deeply nourish very dry hair strands, control frizz for 48 hours, and impart brilliant diamond shine."),
        ("Does it provide heat protection up to 230°C?", "Yes, clinically proven to shield hair fibers against heat damage from blow-dryers and flat irons up to 230°C."),
        ("What volume is contained in this bottle?", "It comes in a luxury 100ml glass pump bottle."),
        ("How do I apply it correctly?", "Rub 1-2 pumps between hands, distribute through damp or dry hair lengths to ends before or after styling."),
        ("Does it leave a greasy heavy film?", "No, weightless velvety matrix absorbs instantly leaving zero greasy residue."),
        ("Where is L'Oréal Elvive Serum manufactured?", "It is proudly manufactured by L'Oréal Paris following global hair care standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All L'Oréal products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it prevent split ends and frizz?", "Yes, seals split ends and blocks humidity flyaways for 48 hours."),
        ("What scent does L'Oréal Extraordinary Serum have?", "Features a luxurious, long-lasting floral L'Oréal fragrance."),
        ("Is it suitable for very dry and color-treated hair?", "Ideal for very dry, frizzy, damaged, and color-treated hair types."),
        ("Is the 100ml bottle suitable for daily use?", "Yes, high-value glass bottle with a pump lasts through months of daily grooming."),
        ("How should I store the bottle?", "Store the glass bottle in a cool, dry place away from heat."),
        ("Does it restore diamond shine?", "Yes, restores brilliant shine and softness to dull, heat-damaged hair."),
        ("Is the pump bottle leak-proof?", "Yes, comes in a sturdy glass bottle with a secure pump lock."),
        ("Can it be used on dry hair after styling?", "Yes, can be applied to dry hair as a finishing touch for added shine and smoothness."),
        ("How often can I use it daily?", "Use daily as needed for styling, heat defense, or hydration."),
        ("Is it suitable for men and women?", "Suitable for all age groups, both men and women."),
        ("Does it define curly hair strands?", "Yes, excellent for moisturizing and defining wavy and curly hair."),
        ("Is it L'Oréal's best-selling hair oil serum?", "Yes, Elvive Extraordinary Oil Serum is the #1 iconic best-selling hair oil by L'Oréal."),
        ("Does it deliver a feeling of salon luxury?", "Yes, fine floral scent and velvet softness impart a salon-like finish."),
        ("Is the glass bottle recyclable?", "Yes, 100% recyclable environmentally friendly glass bottle."),
        ("Does it detangle hair easily?", "Yes, smooths hair cuticles for effortless wet and dry combing."),
        ("Does it leave hair touchably soft?", "Yes, leaves hair touchably soft, smooth, and supple."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1856",
        "sku": "EK-1856",
        "gtin": "3600522680147",
        "category": "العناية بالشعر / سيروم وزيوت تغذية وتصفيف الشعر الفاخرة",
        "brand": "L'Oréal Elvive",
        "ar": {
            "title": "سيروم للشعر شديد الجفاف والمجعد الفيف اكسترا اورديناري من لوريال 100مل",
            "meta_title": "سيروم لوريال الفيف اكسترا اورديناري 100مل | إكليل أبها",
            "meta_description": "اشتري سيروم للشعر شديد الجفاف والمجعد الفيف اكسترا اورديناري من لوريال (100مل). سيروم غني بـ 6 زيوت زهرية وحماية حرارية 230C. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["لوريال", "لوريال_الفيف", "سيروم_الفيف", "اكسترا_اوريدناري", "إكليل_أبها"]
        },
        "en": {
            "title": "L'Oréal Elvive Extraordinary Oil Serum for Very Dry and Frizzy Hair - 100ml",
            "meta_title": "L'Oréal Elvive Extraordinary Oil Serum 100ml | Ekleel Abha",
            "meta_description": "Buy original L'Oréal Elvive Extraordinary Oil Serum (100ml). 6 Precious Flower Oils dry hair & 230°C heat serum. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["loreal", "elvive", "extraordinary_oil", "hair_serum", "ekleel_abha"]
        },
        "schema": {
            "brand": "L'Oréal Elvive",
            "category": "Hair Care / Hair Serum",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "loreal-elvive-extraordinary-oil-serum-for-very-dry-and-frizzy-hair-100ml.webp",
            "alt": "L'Oréal Elvive Extraordinary Oil Serum 100ml",
            "title": "L'Oréal Elvive Extraordinary Oil Serum 100ml"
        }
    }

def create_product_1857():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>معجون أسنان سيجنال، 120 مل (Signal Toothpaste, 120 ml)</strong> معجون الأسنان العائلي الأيقوني الأكثر ثقة وحماية لتأمين نظافة الأسنان، مكافحة تسوس المينا، وتقوية اللثة لدى جميع أفراد العائلة. يرتكز هذا المعجون الشهير من سيجنال (Signal Cavity Fighter Toothpaste) على تكنولوجيا الفلورايد الفعال والكالسيوم النشط (Active Calcium & Fluoride Complex).</p>
<p>يعمل معجون سيجنال على تنظيف البلاك والشوائب بين الأسنان، تقوية بنية المينا ضد التآكل الحمضي، وتأمين نفس نعناعي منعش يمتد لساعات، ليضمن لكِ ولعائلتكِ ابتسامة ناصعة وأسناناً قوية خالية من النخر والتسوس.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية متكاملة ضد تسوس الأسنان (Active Calcium):</strong> يقوي المينا ويعيد ترميم المعادن المفقودة بالأسنان.</li>
  <li><strong>الفلورايد الفعال لحماية 12 ساعة:</strong> يقلل تكون البلاك والأحماض المسببة للنخر والتسوس.</li>
  <li><strong>نكهة النعناع المنعشة:</strong> تمنح الفم نفساً منعشاً ونظيفاً يبث الثقة طوال اليوم.</li>
  <li><strong>تنظيف فعال للبكتيريا واللويحة الجرثومية:</strong> ينظف طبقات البلاك المسدودة بفتح الأسنان.</li>
  <li><strong>تركيبة آمنة ومجربة لجميع أفراد العائلة:</strong> مناسبة للبالغين والأطفال من سن 6 سنوات.</li>
  <li><strong>عبوة اقتصادية سعة 120 مل:</strong> حجم عائلي ممتاز يضمن استخداماً مستمراً لعدة أسابيع.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق):</strong> وضعي كمية بحجم حبة البازلاء من معجون سيجنال على فرشاة أسنان ناعمة.</li>
  <li><strong>الخطوة الثانية (التفريش):</strong> فرشي الأسنان جيداً لمدة دقيقتين بحركات دائرية من اللثة باتجاه قمة السن.</li>
  <li><strong>الخطوة الثالثة (البصق والشطف):</strong> ابصقي المعجون واشطفي الفم بالماء الفاتر (يُستعمل مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الكالسيوم النشط وفلورايد الصوديوم (Active Calcium & Sodium Fluoride):</strong> يقويان المينا ويحميان الأسنان من النخر.</li>
  <li><strong>منظفات طبيعية ونكهة النعناع:</strong> تنظف البلاك وتنعش أنفاس الفم.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الفموي لتفريش الأسنان فقط؛ لا يبتلع المعجون.</li>
  <li>للأطفال دون سن 6 سنوات: تُستخدم كمية صغيرة جداً تحت إشراف البالغين لمنع البلع.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل عائلة تبحث عن معجون أسنان سيجنال الأصلي بالكالسيوم والفلورايد لحماية متكاملة ضد التسوس.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سيجنال (Signal)</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم / معاجين الأسنان العائلية لمكافحة التسوس وتقوية المينا</td></tr>
  <tr><th>نوع المنتج</th><td>معجون أسنان عائلي بمكافحة التسوس والكالسيوم والفلورايد (120ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>120 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بالفم والأسنان واللثة)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان بيضاء قوية خالية من التسوس، لثة صحية ونفس نعناعي منعش</td></tr>
  <tr><th>الملمس</th><td>معجون ناعم متجانس يولد رغوة تنظيف غنية</td></tr>
  <tr><th>العطر</th><td>عطر النعناع المنعش (Fresh Mint) الأيقوني</td></tr>
  <tr><th>المكونات النشطة</th><td>الكالسيوم النشط، فلورايد الصوديوم، منظفات المينا</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / مصر (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (سيجنال)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والأطفال (من 6 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الكالسيوم والفلورايد في معجون سيجنال (Signal Toothpaste)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج معجون أسنان سيجنال مشكلة نخر وتسوس المينا، تراكم البلاك، ضعف الأسنان، ورائحة الفم الكريهة.</p>

<h3>لماذا تنجح تركيبة الكالسيوم النشط والفلورايد؟</h3>
<p>لأن الفلورايد والكالسيوم يعيدان التمعدن الطبيعي لمينا الأسنان الضعيفة (Remineralization)، مما يوقف التسوس في مراحله الأولى.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التفريش دقيقتين مرتين يومياً:</strong> فرشي الأسنان صباحاً ومساءً لـ 2 دقيقة كاملة.<br>
2. <strong>تغيير الفرشاة كل 3 أشهر:</strong> استبدلي فرشاة الأسنان دورياً لضمان تنظيف البلاك.<br>
3. <strong>تقليل السكريات:</strong> التقليل من الأطعمة السكرية يمنع إنتاج حمض البكتيريا.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "معاجين الأسنان العائلية العادية لا تحمي من التسوس كالمعاجين الطبية المكلفة."<br>
<strong>الحقيقة:</strong> معجون سيجنال يحتوي على الفلورايد والكالسيوم الموصى بهما من أطباء الأسنان لحماية أكيدة ب قيمة ممتازة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يتحد فلورايد الصوديوم مع هيدروكسي أباتيت المينا، فيشكل الفلور أباتيت الأكثر مقاومة للأحماض البكتيرية.</p>"""

    faqs = [
        ("ما هو معجون أسنان سيجنال 120 مل؟", "هو معجون أسنان عائلي أيقوني من سيجنال بالكالسيوم النشط والفلورايد لحماية الأسنان من التسوس وتأمين نفس نعناعي منعش 120 مل."),
        ("ما هي فوائد الكالسيوم النشط والفلورايد؟", "يقويان بنية المينا، يعيدان التمعدن، ويحميان الأسنان من التآكل الحمضي والتسوس."),
        ("هل يمنع تسوس ونخر الأسنان لـ 12 ساعة؟", "نعم، مثبت سريرياً في تقليل الأحماض البكتيرية ومنع التسوس لجميع أفراد العائلة."),
        ("ما حجم العبوة؟", "تأتي بحجم عائلي 120 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية بحجم حبة البازلاء على الفرشاة، فرشي دقيقتين مرتين يومياً ثم ابصقي واشطفي بالماء."),
        ("هل يناسب جميع أفراد العائلة والأطفال؟", "مناسب للبالغين والأطفال من سن 6 سنوات فما فوق."),
        ("ما هو بلد صنع معجون سيجنال؟", "صُنع بواسطة شركة يونيلفر (Unilever) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات سيجنال لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يزيل رائحة الفم الكريهة؟", "نعم، ينظف الشوائب والبكتيريا ويمنح الفم نفساً نعناعياً منعشاً طوال اليوم."),
        ("ما هي رائحة ونكهة معجون سيجنال؟", "يتميز بنكهة النعناع المنعشة والأيقونية."),
        ("هل يساعد في تبييض وتنظيف الأسنان؟", "نعم، يزيل البقع السطحية والبلاك ليكشف عن أسنان ناصعة وقوية."),
        ("هل العبوة 120 مل مناسبة للاستخدام العائلي المستمر؟", "نعم، حجم عائلي ممتاز يكفي للاستخدام اليومي لعدة أسابيع."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعبوتها المغلقة محكماً."),
        ("هل العبوة محكمة الغلق؟", "تأتي في أنبوب محكم الإغلاق بغطاء لولبي حامي."),
        ("هل يمنع تراكم الجير والبلاك؟", "نعم، التنظيف اليومي بالكالسيوم يمنع تراكم البلاك والتكلس."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُوصى بالتفريش 2 مرات يومياً (صباحاً ومساءً)."),
        ("هل يناسب الأسنان واللثة العادية؟", "نعم، ممتاز للعناية اليومية بالأسنان واللثة العادية."),
        ("هل ينصح به أطباء الأسنان؟", "نعم، سيجنال الماركة العائلية الأكثر توصية وشهرة لحماية المينا."),
        ("هل هو معجون الأسنان العائلي الأكثر شهرة؟", "نعم، سيجنال مكافحة التسوس المعجون الأول والأكثر مبيعاً."),
        ("هل يمنح حس نظافة وثقة؟", "نعم، يضمن نظافة وانتعاشاً فموياً مطلقاً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، أنبوب صديق للبيئة وقابل لإعادة التدوير."),
        ("هل يمنع نخر المينا المبكر؟", "نعم، يعيد تمعدن المينا ويمنع النخر المبكر."),
        ("هل يترك الفم معطراً؟", "نعم، يترك الفم معطراً بنكهة النعناع المنعشة."),
        ("هل يترك الأسنان ملساء؟", "نعم، يترك أسطح الأسنان ملساء ونظيفة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Signal Toothpaste, 120 ml</strong> (Signal Cavity Fighter Toothpaste) is the world's trusted iconic family toothpaste engineered to protect tooth enamel, combat cavity decay, and fortify gums for all family members. Formulated by Signal, it features an Active Calcium & Fluoride Complex.</p>
<p>Signal Toothpaste cleans interdental plaque and surface stains, reinforces enamel structure against bacterial acid erosion, and delivers long-lasting fresh mint breath, ensuring strong, healthy teeth and a confident smile.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Complete Cavity Defense (Active Calcium):</strong> Reinforces enamel structure and remineralizes weak spots.</li>
  <li><strong>12-Hour Fluoride Shield Against Decay:</strong> Inhibits bacterial acid production and enamel demineralization.</li>
  <li><strong>Refreshing Fresh Mint Flavor:</strong> Leaves mouth enveloped in fresh mint breath confidence all day long.</li>
  <li><strong>Cleans Bacterial Plaque & Film:</strong> Sweeps away daily food debris and sticky interdental plaque.</li>
  <li><strong>Safe & Tested for Whole Family:</strong> Suitable for adults and children aged 6+ for daily oral care.</li>
  <li><strong>Generous 120ml Family Tube:</strong> High-value tube providing weeks of continuous family brushing.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply):</strong> Apply a pea-sized amount of Signal toothpaste onto a soft toothbrush.</li>
  <li><strong>Step 2 (Brush):</strong> Brush teeth thoroughly for 2 minutes in circular motions from gums to tooth tips.</li>
  <li><strong>Step 3 (Rinse):</strong> Spit out toothpaste and rinse mouth with warm water (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Active Calcium & Sodium Fluoride:</strong> Fortify tooth enamel and protect against acid cavity decay.</li>
  <li><strong>Natural Cleansers & Mint Flavor:</strong> Clean interdental plaque and provide fresh mint breath.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For oral toothbrushing application only; do not swallow.</li>
  <li>For children under 6 years: use a pea-sized amount under adult supervision to minimize swallowing.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Families seeking original Signal Cavity Fighter Toothpaste with Active Calcium & Fluoride for complete cavity defense.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Signal</td></tr>
  <tr><th>Category</th><td>Oral Care / Family Cavity Protection Toothpastes</td></tr>
  <tr><th>Product Type</th><td>Active Calcium & Fluoride Cavity Fighter Toothpaste (120ml)</td></tr>
  <tr><th>Volume/Weight</th><td>120 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Oral, Dental & Gum Hygiene)</td></tr>
  <tr><th>Finish</th><td>Strong white teeth, cavity-free enamel, healthy gums & fresh mint breath</td></tr>
  <tr><th>Texture</th><td>Smooth foaming toothpaste paste</td></tr>
  <tr><th>Fragrance</th><td>Iconic Fresh Mint cooling aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Active Calcium, Sodium Fluoride, Enamel Cleansers</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / Egypt (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever (Signal)</td></tr>
  <tr><th>Age Group</th><td>Adults & Kids (6+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Active Calcium Remineralization & Fluoride Defense</h2>

<h3>What problem does this solve?</h3>
<p>Signal Toothpaste resolves enamel demineralization, cavity decay, bacterial plaque buildup, and bad breath.</p>

<h3>Why choose Signal Toothpaste?</h3>
<p>Active Calcium and Sodium Fluoride work synergistically to incorporate fluorapatite into weak enamel, stopping cavities in early stages.</p>"""

    en_faqs = [
        ("What is Signal Toothpaste, 120 ml?", "It is an iconic family cavity fighter toothpaste enriched with Active Calcium and Fluoride to fortify enamel and prevent decay."),
        ("What are the benefits of Active Calcium and Fluoride?", "Fortify enamel structure, restore lost minerals, and protect teeth against bacterial acid erosion."),
        ("Does it prevent cavity decay for 12 hours?", "Yes, clinically proven to reduce bacterial acid production and defend against cavities for all family members."),
        ("What volume is contained in this tube?", "It comes in a generous 120ml family tube."),
        ("How do I use it correctly?", "Apply a pea-sized amount, brush for 2 minutes twice daily, spit out, and rinse with warm water."),
        ("Is it safe for the whole family?", "Suitable for adults and children aged 6+."),
        ("Where is Signal Toothpaste manufactured?", "It is produced by Unilever following global dental care standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Signal products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it eliminate bad breath?", "Yes, cleans plaque and food debris leaving your mouth with long-lasting fresh mint breath."),
        ("What flavor does Signal Toothpaste have?", "Features the iconic, refreshing Fresh Mint flavor."),
        ("Does it help brighten teeth?", "Yes, sweeps away surface stains and plaque to reveal strong, clean, white teeth."),
        ("Is the 120ml tube economical for family use?", "Yes, generous size lasts through weeks of continuous family brushing."),
        ("How should I store the tube?", "Store in a cool, dry place away from direct heat."),
        ("Is the tube cap leak-proof?", "Yes, comes in a sturdy tube with a tight screw-top cap."),
        ("Does it prevent tartar buildup?", "Yes, daily brushing with Active Calcium prevents plaque calcification into hard tartar."),
        ("How many times daily should I use it?", "Recommended for use twice daily, morning and evening."),
        ("Is it suitable for normal teeth and gums?", "Ideal for daily hygiene care of normal teeth and gums."),
        ("Is Signal recommended by dentists?", "Yes, Signal is a top trusted family brand recommended for enamel protection."),
        ("Is Signal Colgate's peer #1 family toothpaste?", "Yes, Signal Cavity Fighter is one of the world's #1 best-selling family toothpastes."),
        ("Does it deliver fresh breath confidence?", "Yes, guarantees complete oral cleanliness and fresh breath confidence."),
        ("Is the tube recyclable?", "Yes, 100% recyclable environmentally friendly tube."),
        ("Does it stop early enamel demineralization?", "Yes, remineralizes weak enamel spots to halt early cavity decay."),
        ("Does it leave your mouth feeling fresh?", "Yes, leaves your mouth feeling clean and refreshed."),
        ("Does it leave tooth surfaces smooth?", "Yes, leaves tooth surfaces smooth and plaque-free."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1857",
        "sku": "EK-1857",
        "gtin": "6281006412521",
        "category": "العناية بالفم / معاجين الأسنان العائلية لمكافحة التسوس وتقوية المينا",
        "brand": "Signal",
        "ar": {
            "title": "معجون أسنان سيجنال، 120 مل",
            "meta_title": "معجون أسنان سيجنال 120مل | صيدلية إكليل أبها",
            "meta_description": "اشتري معجون أسنان سيجنال (120 مل). معجون أسنان عائلي بالكالسيوم والفلورايد لحماية الأسنان من التسوس. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["سيجنال", "معجون_سيجنال", "مكافحة_التسوس", "عناية_الأسنان", "إكليل_أبها"]
        },
        "en": {
            "title": "Signal Toothpaste, 120 ml",
            "meta_title": "Signal Toothpaste 120ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Signal Toothpaste (120 ml). Active Calcium & Fluoride family cavity fighter toothpaste. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["signal", "signal_toothpaste", "cavity_protection", "active_calcium", "ekleel_abha"]
        },
        "schema": {
            "brand": "Signal",
            "category": "Oral Care / Toothpaste",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "signal-toothpaste-120ml.webp",
            "alt": "Signal Toothpaste 120ml",
            "title": "Signal Toothpaste 120ml"
        }
    }

def create_product_1858():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم تبييض اليدين من ايفلين 100 مل (Eveline Hand Whitening Cream - 100 ml)</strong> المستحضر الطبي الأوروبي الفائق المخصص لتفتيح تصبغات اليدين، ترطيب البشرة شديدة الجفاف، وحماية اليدين من التجاعيد والبقع الداكنة. يرتكز هذا الكريم المميز من ايفلين (Eveline White Prestige 4D Hand Cream) على تكنولوجيا التبييض رباعية الأبعاد 4D المعززة بـ مركب اللوميسكين (Lumiskin)، حمض الهيالورونيك (Hyaluronic Acid)، وخلاصة زبدة الشيا والزيوت المرطبة.</p>
<p>يعمل كريم تبييض اليدين ايفلين 4D على تقليل التصبغات والبقع الناتجة عن التقدم بالسنتين أو الشمس، تأمين ترطيب عميق لـ 48 ساعة، وتقوية الأظافر، ليترك يديكِ ناعمتين كالحرير، ناصعتين، ومفعمتين بالشاب والانتعاش دون أي لزوجة دهنية.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح رباعي الأبعاد 4D للبقع الداكنة باليدين:</strong> يزيل التصبغات وتصحيح لون بشرة اليدين ب فاعلية.</li>
  <li><strong>ترطيب مكثف لـ 48 ساعة بحمض الهيالورونيك:</strong> يحبس الماء بالجلد ويقضي على خشونة وجفاف الأيدي.</li>
  <li><strong>معزز بزبدة الشيا واللوميسكين الطبيعي:</strong> يغذي أنسجة الجلد ويحمي الأظافر من التكسر.</li>
  <li><strong>حماية ضد التشيّخ المبكر للبشرة:</strong> يقلل التجاعيد الخفيفة ويحفظ مرونة جلد اليدين.</li>
  <li><strong>امتصاص فوري وقوام كريمي غير لزج:</strong> ينفذ بالبشرة فورياً دون ترك أثر دهني لزج على اليدين.</li>
  <li><strong>أنبوب سعة 100 مل:</strong> حجم ممتاز ومناسب لحمل حقيبة اليد والعناية اليومية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> اغسلي يديكِ جيداً بالماء الفاتر والصابون وجففيهما.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي كمية مناسبة من كريم ايفلين 4D على ظهر اليدين والأصابع والأظافر.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي بحركات دائرية خفيفة حتى امتصاص الكريم بالكامل (يُستعمل 2 إلى 3 مرات يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركب لوميسكين وحمض الهيالورونيك (Lumiskin & Hyaluronic Acid):</strong> يفتحان البقع ويحفظان الترطيب العميق.</li>
  <li><strong>زبدة الشيا وفيتامين E:</strong> يغذيان الأظافر والجلد الجاف ويرممان حماية البشرة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة اليدين والأظافر فقط.</li>
  <li>تجنبي ملامسة الكريم المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تعاني من تصبغات اليدين، الجفاف، وتفتش عن كريم ايفلين 4D الفلبيني/الأوروبي لتفتيح وترطيب اليدين.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ايفلين (Eveline Cosmetics)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات ايفلين الأوروبية لتفتيح وترطيب اليدين 4D</td></tr>
  <tr><th>نوع المنتج</th><td>كريم تفتيح وترطيب اليدين رباعي الأبعاد 4D (100ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة اليدين (بما في ذلك الحساسة والشديدة الجفاف)</td></tr>
  <tr><th>المظهر النهائي</th><td>يدين ناصعتين، مفتحتين، ناعمتين كالحرير، خاليتين من التصبغات والتجاعيد</td></tr>
  <tr><th>الملمس</th><td>كريمي مخملي خفيف سريع الامتصاص دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر ايفلين الفرنسي اللطيف الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>لوميسكين، حمض الهيالورونيك، زبدة الشيا، فيتامين E</td></tr>
  <tr><th>بلد المنشأ</th><td>بولندا (Eveline Cosmetics EU)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Eveline Cosmetics</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد التفتيح 4D وحمض الهيالورونيك في ايفلين (Eveline Hand Cream)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم تبييض اليدين من ايفلين مشكلة تصبغات اليدين الناتجة عن الشمس، خشونة المفاصل، التجاعيد، وضعف الأظافر.</p>

<h3>لماذا تنجح تقنية 4D واللوميسكين؟</h3>
<p>لأن مركب 4D يعمل على 4 أبعاد: يقلل التصبغات، ينقص حجم البقع، يمنع ظهور تصبغات جديدة، ويغذي الجلد بـ الهيالورونيك.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق بعد غسيل اليدين:</strong> استعملي الكريم فور غسيل اليدين لحبس الترطيب.<br>
2. <strong>العناية بالأظافر والجلد المحيط:</strong> دلكي الأظافر والجلد المحيط بالكريم لمنع تكسرها.<br>
3. <strong>التطبيق قبل النوم:</strong> وضعي طبقة سخية قبل النوم لترميم الأيدي أثناء الليل.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات تفتيح اليدين تترك لزوجة تمنع استخدام الهاتف أو العمل."<br>
<strong>الحقيقة:</strong> كريم ايفلين 4D مصمم بتركيبة مخملية تمتصها اليدين فورياً دون أي لزوجة دهنية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يمتص حمض الهيالورونيك 1000 ضعف وزنه ماء بالبشرة، بينما يثبط اللوميسكين إنزيم التايروسينيز باليدين.</p>"""

    faqs = [
        ("ما هو كريم تبييض اليدين من ايفلين 100 مل؟", "هو كريم طبي أوروبي من ايفلين بتكنولوجيا 4D واللوميسكين لتفتيح تصبغات اليدين وترطيب الجفاف الشديد 100 مل."),
        ("ما هي فوائد تقنية 4D واللوميسكين وحمض الهيالورونيك؟", "تفتح تصبغات اليدين والبقع، تحبس الرطوبة لـ 48 ساعة، وتحمي الجلد والأظافر من التشيّخ."),
        ("هل يفتّح بقع وتصبغات اليدين ب فاعلية؟", "نعم، مثبت سريرياً في تفتيح التصبغات والبقع الداكنة وتوحيد لون اليدين."),
        ("ما حجم العبوة؟", "تأتي بحجم 100 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي كمية على ظهر اليدين والأظافر، دلكي برفق 2 إلى 3 مرات يومياً بعد غسيل اليدين."),
        ("هل يمتص بسرعة دون ترك لزوجة؟", "نعم، فورمولا مخملية خفيفة تنفذ فورياً وتترك اليدين ناعمتين دون لزوجة."),
        ("ما هو بلد صنع كريم ايفلين؟", "صُنع بفخر في بولندا (الاتحاد الأوروبي) بواسطة مختبرات ايفلين (Eveline Cosmetics)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات ايفلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يناسب اليدين شديدة الجفاف والأظافر؟", "نعم، ممتاز لترطيب الأيدي الجافة وتقوية الأظافر ومنع تكسرها."),
        ("ما هي رائحة كريم ايفلين 4D؟", "يتميز برائحة فرنسية لطيفة وراقية جداً."),
        ("هل يحمي اليدين من التجاعيد والتقدم بالعمر؟", "نعم، الهيالورونيك وزبدة الشيا يحافظان على مرونة اليدين ويمنعان التجاعيد."),
        ("هل أنبوب العبوة 100 مل مناسب لحقيبة اليد؟", "نعم، حجم مدمج وأنيق مثالي لحمل حقيبة اليد والسفر."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل يترك اليدين ناعمتين كالحرير؟", "نعم، يمنح اليدين ملمساً حريرياً ناعماً جداً."),
        ("هل العبوة محكمة الغلق؟", "تأتي في أنبوب أنيق بغطاء محكم الحماية."),
        ("هل يلزم استخدام واقي شمس مع اليدين؟", "يُفضل تطبيق واقي شمس على اليدين عند الخروج لحماية التفتيح."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل من 2 إلى 3 مرات يومياً عند الحاجة."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع الفئات العمرية للنساء والرجال."),
        ("هل خالي من Paraben والكحول؟", "نعم، تركيبة أوروبية خالية من البارابين ومناسبة للبشرة الحساسة."),
        ("هل هو كريم اليدين المفتّح الأكثر شهرة لايفلين؟", "نعم، Eveline White Prestige 4D كريم اليدين الأول والأكثر مبيعاً."),
        ("هل يمنح حس أنوثة ونظافة؟", "نعم، النعومة والعطر يمنحانكِ شعوراً مطلقاً بالأناقة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يزيل خشونة المفاصل والأصابع؟", "نعم، يرطب وينعم مفاصل الأصابع الخشنة ب فاعلية."),
        ("هل يترك الجلد طرياً؟", "نعم، يترك جلد اليدين طرياً ومسترخياً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Eveline Hand Whitening Cream - 100 ml</strong> (Eveline White Prestige 4D Hand Whitening Cream) is the European clinical hand cream engineered to lighten dark hand hyperpigmentation, hydrate dry skin, and protect hands against aging wrinkles. Formulated by Eveline Cosmetics, it features 4D Whitening Technology with Lumiskin, Hyaluronic Acid, and Shea Butter.</p>
<p>Eveline 4D Hand Cream reduces sun spots, age spots, and discoloration, delivering deep 48-hour moisture while strengthening nails, leaving hands touchably soft, brightened, and youthfully smooth with zero greasy residue.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>4D Whitening Technology for Hand Spots:</strong> Fades dark spots and unifies hand skin tone effectively.</li>
  <li><strong>Intense 48-Hour Hyaluronic Acid Hydration:</strong> Seals in moisture to end hand roughness and dryness.</li>
  <li><strong>Enriched with Shea Butter & Lumiskin:</strong> Nourishes hand skin and protects nails against breakage.</li>
  <li><strong>Anti-Aging Hand Protection:</strong> Smooths fine wrinkles and maintains hand skin elasticity.</li>
  <li><strong>Fast Absorbing Non-Greasy Velvety Texture:</strong> Absorbs instantly without leaving greasy hand residues.</li>
  <li><strong>Compact 100ml Tube:</strong> Ideal handbag size for daily continuous hand hydration and brightening.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Wash hands thoroughly with warm water and soap and pat dry.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a small amount of Eveline 4D hand cream onto the back of hands, fingers, and nails.</li>
  <li><strong>Step 3 (Massage):</strong> Massage in gentle circular motions until fully absorbed (use 2 to 3 times daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Lumiskin & Hyaluronic Acid:</strong> Fade dark spots and lock in deep 48-hour moisture.</li>
  <li><strong>Shea Butter & Vitamin E:</strong> Nourish dry hand skin, cuticles, and strengthen brittle nails.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hand and nail moisturizing application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dark hand spots, dry skin, or brittle nails seeking Eveline's 4D Whitening Hand Cream.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Eveline Cosmetics</td></tr>
  <tr><th>Category</th><td>Skincare / European 4D Whitening & Moisturizing Hand Creams</td></tr>
  <tr><th>Product Type</th><td>4D Whitening & Hyaluronic Moisturizing Hand Cream (100ml)</td></tr>
  <tr><th>Volume/Weight</th><td>100 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hand Skin Types (Including Dry & Sensitive)</td></tr>
  <tr><th>Finish</th><td>Touchably soft, brightened, even-toned & youthfully smooth hands</td></tr>
  <tr><th>Texture</th><td>Lightweight velvety fast-absorbing hand cream</td></tr>
  <tr><th>Fragrance</th><td>Subtle French luxury Eveline fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Lumiskin, Hyaluronic Acid, Shea Butter, Vitamin E</td></tr>
  <tr><th>Country of Origin</th><td>Poland (Eveline Cosmetics EU)</td></tr>
  <tr><th>Manufacturer</th><td>Eveline Cosmetics</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 4D Whitening Technology & Hyaluronic Dermal Binding</h2>

<h3>What problem does this solve?</h3>
<p>Eveline 4D Hand Whitening Cream resolves dark hand spots, sun pigmentation, hand wrinkles, and brittle nails.</p>

<h3>Why choose Eveline 4D Hand Cream?</h3>
<p>4D technology reduces spot size, prevents new melanin formation, while Hyaluronic Acid binds 1000x its weight in water to plump hand skin.</p>"""

    en_faqs = [
        ("What is Eveline Hand Whitening Cream - 100 ml?", "It is a European clinical hand cream featuring 4D Whitening Technology and Hyaluronic Acid to lighten hand spots and hydrate dry skin."),
        ("What are the benefits of 4D Technology, Lumiskin, and Hyaluronic Acid?", "Fade dark hand spots, seal in 48-hour moisture, and protect hand skin against aging wrinkles."),
        ("Does it lighten dark spots on hands effectively?", "Yes, clinically proven to reduce sun spots and hyperpigmentation, unifying hand skin tone."),
        ("What volume is contained in this tube?", "It comes in a compact 100ml tube."),
        ("How do I apply it correctly?", "Apply onto back of hands, fingers, and nails 2 to 3 times daily after washing hands."),
        ("Does it absorb quickly without leaving a greasy film?", "Yes, weightless velvety matrix absorbs instantly leaving zero greasy residue."),
        ("Where is Eveline Hand Cream manufactured?", "It is proudly manufactured in Poland (EU) by Eveline Cosmetics."),
        ("How do I verify authenticity at Ekleel Abha?", "All Eveline products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it nourish dry cuticles and strengthen brittle nails?", "Yes, enriched with Shea Butter and Vitamin E to strengthen nails and soften cuticles."),
        ("What scent does Eveline 4D Hand Cream have?", "Features a subtle, refined French luxury fragrance."),
        ("Does it protect hands against premature aging?", "Yes, Hyaluronic Acid and Shea Butter preserve hand skin elasticity to smooth fine lines."),
        ("Is the 100ml tube handbag-friendly?", "Yes, compact tube fits easily into purses and travel bags."),
        ("How should I store the tube?", "Store in a cool, dry place away from direct heat."),
        ("Does it leave hands touchably silky soft?", "Yes, leaves hands touchably soft, smooth, and supple."),
        ("Is the tube cap leak-proof?", "Yes, comes with a secure flip-top lid."),
        ("Should sunscreen be used on hands?", "Applying sunscreen to hands when outdoors preserves whitening results."),
        ("How many times daily should I use it?", "Use 2 to 3 times daily as needed for hand hydration and whitening."),
        ("Is it suitable for men and women?", "Suitable for all age groups, both men and women."),
        ("Is it paraben-free?", "Yes, European clinical formula safe for sensitive skin."),
        ("Is it Eveline's best-selling hand cream?", "Yes, White Prestige 4D Hand Cream is the #1 flagship hand cream by Eveline."),
        ("Does it deliver elegant hand freshness?", "Yes, soft skin texture and refined scent deliver complete hand grooming elegance."),
        ("Is the tube recyclable?", "Yes, 100% recyclable environmentally friendly tube."),
        ("Does it soften rough finger knuckles?", "Yes, deeply hydrates and smooths rough finger knuckles effectively."),
        ("Does it leave hand skin feeling comfortable?", "Yes, leaves hand skin hydrated, smooth, and relaxed."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1858",
        "sku": "EK-1858",
        "gtin": "5907609356833",
        "category": "العناية بالبشرة / كريمات ايفلين الأوروبية لتفتيح وترطيب اليدين 4D",
        "brand": "Eveline",
        "ar": {
            "title": "كريم تبييض اليدين  من ايفلين 100 مل",
            "meta_title": "كريم تبييض اليدين ايفلين 4D 100مل | إكليل أبها",
            "meta_description": "اشتري كريم تبييض اليدين من ايفلين (100 مل). كريم تفتيح وترطيب اليدين رباعي الأبعاد 4D بحمض الهيالورونيك واللوميسكين. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["ايفلين", "كريم_ايفلين", "تفتيح_اليدين", "ايفلين_4D", "إكليل_أبها"]
        },
        "en": {
            "title": "Eveline Hand Whitening Cream - 100 ml",
            "meta_title": "Eveline White Prestige 4D Hand Cream 100ml | Ekleel Abha",
            "meta_description": "Buy original Eveline Hand Whitening Cream (100 ml). European 4D Whitening & Hyaluronic Acid hand and nail cream. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["eveline", "eveline_hand_cream", "hand_whitening", "white_prestige_4d", "ekleel_abha"]
        },
        "schema": {
            "brand": "Eveline",
            "category": "Skincare / Hand Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "eveline-hand-whitening-cream-100ml.webp",
            "alt": "Eveline Hand Whitening Cream 100ml",
            "title": "Eveline Hand Whitening Cream 100ml"
        }
    }

def create_product_1859():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>بخاخ الأرغان المهدئ والمرطب 150 مل (Argan Soothing and Moisturizing Spray 150ml)</strong> مستحضر الرش الطبيعي الكوري المتقدم المخصص لتغذية، تهدئة، وترطيب الوجه والجسم واليدين بلمسة بخاخ رذاذية منعشة. يرتكز هذا البخاخ المبتكر (Argan Soothing & Moisturizing Mist 99%) على زيت الأرغان المغربي النقي (Pure Moroccan Argan Oil) وزيت الألوفيرا المهدئ.</p>
<p>يعمل بخاخ الأرغان المهدئ على غمر البشرة برذاذ مرطب خفيف ينفذ فورياً بالجلد، يعيد بناء مرونة البشرة، ويهدئ الاحمرار والتطير الناتج عن الجفاف والشمس، ليترك وجهكِ وجسمكِ رطباً، مشرقاً، ومفعماً بالحيوية والانتعاش دون أي لزوجة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتغذية بزيت الأرغان المغربي الأصلي:</strong> يغذي خلايا الوجه والجسم بالبروتينات والأحماض الدهنية.</li>
  <li><strong>تهدئة أحمرار وتهيج البشرة المجهدة:</strong> يخفف حروق الشمس والجفاف الشديد برذاذ لطيف.</li>
  <li><strong>استخدام متعدد 3 في 1 (الوجه، الجسم، الشعر):</strong> يمنح رذاذاً مغذياً لكافة أجزاء البشرة والخصلات.</li>
  <li><strong>امتصاص مائي سريع 100% دون لزوجة:</strong> ينفذ فورياً بالجلد دون ترك أي أثر دهني لزج.</li>
  <li><strong>مثالي لتثبيت المكياج وإنعاش البشرة:</strong> يمنح المكياج مظهراً ناضجاً ومشرقاً طوال اليوم.</li>
  <li><strong>عبوة بخاخ رذاذية سعة 150 مل:</strong> تصميم أنيق وسهل الرش مناسب للاستخدام المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الرش):</strong> رشي بخاخ الأرغان على مسافة 15-20 سم من الوجه، الجسم، أو الشعر.</li>
  <li><strong>الخطوة الثانية (التوزيع):</strong> دع الرذاذ ينفذ طبيعياً أو اربتي بلطف بكف اليد لامتصاص أسرع.</li>
  <li><strong>الخطوة الثالثة (التكرار):</strong> استعمليه عند الحاجة للانتعاش طوال اليوم أو بعد الاستحمام وتثبيت المكياج.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الأرغان المغربي النقي (Moroccan Argan Oil):</strong> يغذي خلايا الجلد ويعيد المرونة والبريق.</li>
  <li><strong>خلاصة الألوفيرا والمرطبات المائية:</strong> تلطف الأحمرار والتهيج وتحفظ الترطيب.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على الوجه والجسم والشعر فقط.</li>
  <li>أغلقي العينين أثناء رش الوجه لمنع دخول الرذاذ مباشرة داخل العين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن بخاخ الأرغان الكوري المهدئ والمرطب 99% لتغذية الوجه والجسم بسرعة وانتعاش.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>عام / صيدلية إكليل أبها (Argan Mist)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / بخاخات ورذاذات زيت الأرغان المهدئة والمرطبة</td></tr>
  <tr><th>نوع المنتج</th><td>بخاخ رذاذي مهدئ ومرطب بزيت الأرغان 99% (150ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>150 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (بما في ذلك الجافة والحساسة) والشعر</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة، مرطبة، مشعة ومحمية ورذاذ منعش دون لزوجة</td></tr>
  <tr><th>الملمس</th><td>رذاذ مائي زيتي خفيف للغاية سريع الامتصاص</td></tr>
  <tr><th>العطر</th><td>عطر الأرغان والألوفيرا الطبيعي الناعم</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت الأرغان المغربي، الألوفيرا، مرطبات مائية ناصعة</td></tr>
  <tr><th>بلد المنشأ</th><td>كوريا الجنوبية (South Korea)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Korean Beauty Labs</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد بخاخ الأرغان الكوري المهدئ (Argan Soothing Spray)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج بخاخ الأرغان المهدئ مشكلة جفاف وشحوب بشرة الوجه والجسم، التهيج الناتج عن الشمس، وثقل كريمات الترطيب الزيتية.</p>

<h3>لماذا تنجح تكنولوجيا الرذاذ بالـ 99% أرغان؟</h3>
<p>لأن جزيئات رذاذ الأرغان تتشتت بشكل مجهري فوق البشرة، فيمتصها الجلد فورياً دون إغلاق المسام.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الرش بعد الاستحمام:</strong> رشي البخاخ على الجسم فور الاستحمام لحبس الرطوبة.<br>
2. <strong>مثبت ناعم للمكياج:</strong> رشي رذاذاً خفيفاً فوق المكياج لإضفاء مظهراً نضراً.<br>
3. <strong>إنعاش الشعر:</strong> رشي رذاذاً على خصلات الشعر الجافة لإعطاء بريق ونعومة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "بخاخات الزيوت تسبب لزوجة وتفسد المكياج."<br>
<strong>الحقيقة:</strong> بخاخ الأرغان الكوري مصمم برذاذ خفيف يجف فورياً ليزيد ثبات ونضارة المكياج دون لزوجة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبت الأحماض الدهنية بالـ Argan Oil الطبقة الزهمية الواقية، بينما تهدئ السكريات المتعددة بالألوفيرا الأنسجة.</p>"""

    faqs = [
        ("ما هو بخاخ الأرغان المهدئ والمرطب 150 مل؟", "هو بخاخ رذاذي كوري غني بزيت الأرغان المغربي والألوفيرا لتغذية وتهدئة وترطيب الوجه والجسم والشعر 150 مل."),
        ("ما هي فوائد زيت الأرغان المغربي والألوفيرا؟", "يغذي زيت الأرغان خلايا الجلد والمرونة، بينما يلطف الألوفيرا الأحمرار والجفاف الشديد."),
        ("هل يناسب الوجه والجسم والشعر معاً؟", "نعم، رذاذ متعدد الاستخدامات 3 في 1 يلائم بشرة الوجه، الجسم، وخصلات الشعر."),
        ("ما حجم العبوة البخاخ؟", "تأتي بحجم 150 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "رشي من مسافة 15-20 سم على الوجه (مع إغلاق العينين) أو الجسم أو الشعر، ودعيه ينفذ طبيعياً طوال اليوم."),
        ("هل يمتص بسرعة دون لزوجة دهنية؟", "نعم، رذاذ مائي خفيف يمتص بالجلد فورياً دون ترك أي لزوجة زيتية."),
        ("ما هو بلد صنع بخاخ الأرغان؟", "صُنع بفخر في كوريا الجنوبية وفق أعلى المعايير الكورية للجمال K-Beauty."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع المستحضرات الكورية لدى إكليل أبها أصلية 100% ومستوردة من الموردين المعتمدين."),
        ("هل يمكن استخدامه كمثبت ومجدد للمكياج؟", "نعم، ممتاز لرشه فوق المكياج لإضفاء مظهراً ناضجاً ومشرقاً."),
        ("ما هي رائحة بخاخ الأرغان؟", "يتميز برائحة ناعمة ولطيفة من زيت الأرغان والألوفيرا."),
        ("هل يهدئ أحمرار وحروق الشمس؟", "نعم، يلطف أحمرار وتهيج الجلد الناتج عن التعرض للشمس والجفاف."),
        ("هل العبوة 150 مل مناسبة للحقيبة والسفر؟", "نعم، تصميم بخاخ أنيق ومدمج مثالي لحمل الحقيبة والسفر."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل يمنح حس نضارة وإشراقة فورية؟", "نعم، يمنح بشرتكِ وشعركِ نضارة وإشراقة فورية."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة بخاخ بغطاء حامي يمنع التسرب."),
        ("هل يغذي خصلات الشعر الجافة؟", "نعم، رشه على الشعر يمنحه لمعاناً ونعومة خفيفة."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل عند الحاجة للانتعاش طوال اليوم."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع الفئات العمرية للنساء والرجال من سن 3 سنوات."),
        ("هل خالي من Paraben والكيماويات الضارة؟", "تركيبة كورية آمنة خالية من البارابين والكيماويات الضارة."),
        ("هل هو بخاخ الأرغان المهدئ الأكثر طلباً؟", "نعم، بخاخ الأرغان الكوري الخيار الأول للانتعاش المائي."),
        ("هل يترك البشرة طرية؟", "نعم، يترك الوجه والجسم ب طراوة ونعومة ملحوظة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يمنع التكسر والتطير؟", "نعم، يضبط تطاير الشعر وهيشان البشرة الجافة."),
        ("هل يترك ملمساً أملساً؟", "نعم، يترك الوجه طرياً ومسترخياً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Argan Soothing and Moisturizing Spray 150ml</strong> (Argan Soothing & Moisturizing Mist 99%) is the Korean hydration mist engineered to nourish, calm, and hydrate face, body, and hair with a fine refreshing spray. Formulated with 99% pure Moroccan Argan Oil and soothing Aloe Vera.</p>
<p>Argan Soothing Spray envelops skin in a fine moisturizing mist that absorbs instantly, restoring dermal elasticity, calming sun redness, and leaving your face, body, and hair shiny and hydrated with zero sticky residue.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Nourishment & Hydration with Moroccan Argan Oil:</strong> Enriches skin and hair cells with essential fatty acids.</li>
  <li><strong>Calms Redness & Sun Irritation:</strong> Relieves sun burn and severe dryness with a delicate cooling mist.</li>
  <li><strong>Versatile 3-in-1 Application (Face, Body, Hair):</strong> Provides a nourishing mist for facial skin, body, and hair strands.</li>
  <li><strong>Fast Absorbing Non-Sticky Hydra-Mist:</strong> Penetrates instantly without leaving greasy residues.</li>
  <li><strong>Ideal for Makeup Setting & Refreshing:</strong> Bestows a dewy, glowing finish to facial makeup all day long.</li>
  <li><strong>Sleek 150ml Fine Spray Bottle:</strong> Elegant spray bottle size for continuous hydration anywhere.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Spray):</strong> Spray Argan Mist from a distance of 15-20cm over face, body, or hair strands.</li>
  <li><strong>Step 2 (Absorb):</strong> Allow mist to absorb naturally or pat gently with palms for faster absorption.</li>
  <li><strong>Step 3 (Repeat):</strong> Reapply throughout the day whenever instant hydration or makeup refreshing is needed.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Moroccan Argan Oil:</strong> Nourishes skin cells and restores healthy elasticity and shine.</li>
  <li><strong>Aloe Vera & Hydra-Moisturisers:</strong> Soothe skin redness, sunburn, and preserve moisture levels.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial, body, and hair application only.</li>
  <li>Close eyes while spraying face to prevent direct mist entry into eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking the Korean 99% Argan soothing and moisturizing spray for quick face, body, and hair hydration.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Generic / Ekleel Abha Pharmacy</td></tr>
  <tr><th>Category</th><td>Skincare / Korean Argan Soothing & Moisturizing Mists</td></tr>
  <tr><th>Product Type</th><td>99% Argan Soothing & Hydrating Facial & Body Mist (150ml)</td></tr>
  <tr><th>Volume/Weight</th><td>150 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Including Dry & Sensitive) & Hair</td></tr>
  <tr><th>Finish</th><td>Deeply hydrated, dewy, radiant & calm skin and shiny hair</td></tr>
  <tr><th>Texture</th><td>Ultra-light fine hydra-mist spray</td></tr>
  <tr><th>Fragrance</th><td>Subtle natural Argan & Aloe Vera aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Moroccan Argan Oil, Aloe Vera, Hydra-Moisturisers</td></tr>
  <tr><th>Country of Origin</th><td>South Korea</td></tr>
  <tr><th>Manufacturer</th><td>Korean Beauty Labs</td></tr>
  <tr><th>Age Group</th><td>All Ages (3+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Argan Fatty Acid Nourishment & Fine Mist Micro-Dispersion</h2>

<h3>What problem does this solve?</h3>
<p>Argan Soothing Spray resolves skin dryness, sun redness, dull makeup, and frizzy hair strands.</p>

<h3>Why choose Korean Argan Spray?</h3>
<p>Micro-dispersion technology allows Argan fatty acids and Aloe polysaccharides to penetrate skin without clogging pores or melting makeup.</p>"""

    en_faqs = [
        ("What is Argan Soothing and Moisturizing Spray 150ml?", "It is a Korean 99% Argan oil soothing hydration mist designed to nourish and refresh face, body, and hair."),
        ("What are the benefits of Moroccan Argan Oil and Aloe Vera?", "Moroccan Argan Oil nourishes skin cells, while Aloe Vera soothes redness, sunburn, and dryness."),
        ("Is it suitable for face, body, and hair?", "Yes, versatile 3-in-1 fine mist suitable for facial skin, body, and hair strands."),
        ("What volume is contained in this spray bottle?", "It comes in a sleek 150ml spray bottle."),
        ("How do I apply it correctly?", "Spray from 15-20cm over face (with eyes closed), body, or hair strands and let absorb naturally."),
        ("Does it absorb quickly without grease?", "Yes, weightless hydra-mist absorbs instantly leaving zero greasy residue."),
        ("Where is Argan Soothing Spray manufactured?", "Proudly manufactured in South Korea following K-Beauty standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Korean skincare products at Ekleel Abha are 100% original from certified suppliers."),
        ("Can it be used to set and refresh makeup?", "Yes, functions as a dewy makeup setting mist for a radiant finish."),
        ("What scent does Argan Spray have?", "Features a light, pleasant natural Argan and Aloe Vera fragrance."),
        ("Does it soothe sunburn and redness?", "Yes, calms skin redness and irritation caused by sun exposure."),
        ("Is the 150ml bottle handbag-friendly?", "Yes, sleek spray bottle fits easily into handbags and travel kits."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Does it deliver instant skin radiance?", "Yes, bestows an instant dewy glow to facial skin and hair."),
        ("Is the spray cap leak-proof?", "Yes, comes with a secure protective cap."),
        ("Does it nourish dry hair strands?", "Yes, spraying on hair strands adds light shine and softness."),
        ("How often can I use it daily?", "Use throughout the day whenever instant hydration or refreshing is needed."),
        ("Is it safe for family use?", "Safe for adults and children aged 3+."),
        ("Is it free of parabens and harsh chemicals?", "Yes, 100% free of parabens and harsh chemicals."),
        ("Is it a popular Korean hydration mist?", "Yes, a top favorite K-Beauty Argan mist for instant hydration."),
        ("Does it leave skin touchably soft?", "Yes, leaves skin touchably soft, smooth, and supple."),
        ("Is the bottle recyclable?", "Yes, 100% recyclable environmentally friendly bottle."),
        ("Does it tame frizzy hair?", "Yes, tames flyaways and restores hair shine."),
        ("Does it leave facial skin feeling comfortable?", "Yes, leaves facial skin hydrated, smooth, and calm."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1859",
        "sku": "EK-1859",
        "gtin": "8809514486322",
        "category": "العناية بالبشرة / بخاخات ورذاذات زيت الأرغان المهدئة والمرطبة",
        "brand": "Generic K-Beauty",
        "ar": {
            "title": "بخاخ الأرغان المهدئ والمرطب 150 مل",
            "meta_title": "بخاخ الأرغان المهدئ والمرطب 150مل | إكليل أبها",
            "meta_description": "اشتري بخاخ الأرغان المهدئ والمرطب (150 مل). رذاذ كوري 99% أرغان مغذٍ ومسكن للوجه والجسم والشعر. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بخاخ_الأرغان", "أرغان_مرطب", "رذاذ_الوجه", "العناية_الكورية", "إكليل_أبها"]
        },
        "en": {
            "title": "Argan Soothing and Moisturizing Spray 150ml",
            "meta_title": "Argan Soothing & Moisturizing Spray 150ml | Ekleel Abha",
            "meta_description": "Buy original Argan Soothing and Moisturizing Spray (150ml). Korean 99% Argan Oil face, body & hair mist. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["argan_spray", "argan_mist", "soothing_spray", "k_beauty", "ekleel_abha"]
        },
        "schema": {
            "brand": "Generic K-Beauty",
            "category": "Skincare / Face Mist",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "argan-soothing-and-moisturizing-spray-150ml.webp",
            "alt": "Argan Soothing and Moisturizing Spray 150ml",
            "title": "Argan Soothing and Moisturizing Spray 150ml"
        }
    }

def create_product_1860():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>مناديل نورس منظفة للعباية 25 منديل (Nawras Abaya Cleaning Wipes - 25 Wipes)</strong> المناديل الذكية والحل السريع والأول لإزالة البقع المستعصية، الغبار، والأوساخ عن العباية السوداء والملابس الملونة فورياً دون الحاجة لغسيل كامل أو شطف بالماء. ترتكز هذه المناديل المبتكرة من نورس (Nawras Abaya Instant Cleaning Wipes) على فورمولا تنظيف الأنسجة الداكنة المعززة بمركبات حماية ثبات اللون الأسود برائحة العود والمسك الفاخرة.</p>
<p>تعمل مناديل نورس لمنظفة العباية على إذابة بقع الأطعمة، المكياج، والزيوت الطارئة بمسحة قطنية خفيفة، دون ترك أي أثر بقع بيضاء أو أثـار تبييض على القماش الأسود، لتضمن لكِ عباية ناصعة السواد، نظيفة، ومعطرة بعطر العود الفاخر طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>إزالة فورية لبقع الطعام والمكياج والغبار:</strong> تنظف البقع الطارئة عن العباية بمسحة واحدة.</li>
  <li><strong>حماية ثبات اللون الأسود الفاخر:</strong> لا تترك بقعاً بيضاء أو أثراً لتبييض القماش الأسود.</li>
  <li><strong>معززة بعطر العود والمسك الملكي:</strong> تترك العباية ناصعة السواد ومعطرة بعاطر زكي.</li>
  <li><strong>مناديل مبللة قطنية فائقة النعومة:</strong> تنزلق بسلاسة على قماش العباية دون تنسيل الخيوط.</li>
  <li><strong>لا تحتاج لشطف بالماء أو غسيل:</strong> الحل الفوري أثناء العمل، المناسبات، والتنقل.</li>
  <li><strong>عبوة مدمجة تحتوي على 25 منديل:</strong> تصميم مدمج مزود بشريط لاصق محكم لحمل الحقيبة والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الفتح):</strong> افتحي الشريط اللاصق واسحبي منديلاً واحداً من المناديل المنظفة للعباية.</li>
  <li><strong>الخطوة الثانية (المسح):</strong> امسحي البقعة أو المنطقة المتسخة بالعباية بلطف بحركات دائرية (لا تحتاج لشطف بالماء).</li>
  <li><strong>الخطوة الثالثة (الإغلاق):</strong> اغلقي الشريط اللاصق فوراً بعد السحب لمنع جفاف المناديل المتبقية.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>سائل تنظيف الأقمشة الداكنة (Fabric Cleaning Solution):</strong> يذوب بقع المكياج والزيوت دون أثر بيضائي.</li>
  <li><strong>عطر العود والمسك:</strong> يمنح العباية عبيراً ملكياً زكياً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي لتنظيف الأقمشة والعباءات والملابس فقط.</li>
  <li>تجنبي ملامسة المنديل للمباشرة للعينين أو البشرة المتهيجة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف مع إغلاق العبوة جيداً.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة ترتدي العباية وتفتش عن مناديل نورس المنظفة السريعة لإزالة البقع الطارئة وعطر العود بالعبوة 25 منديل.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>نورس (Nawras)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / مناديل تنظيف العباية والملابس السوداء الفورية</td></tr>
  <tr><th>نوع المنتج</th><td>مناديل مبللة فورية لتنظيف بقع العباية بعطر العود (25 Wipes)</td></tr>
  <tr><th>الحجم/الوزن</th><td>25 منديل مبلل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بالأقمشة والعباءات والملابس)</td></tr>
  <tr><th>المظهر النهائي</th><td>عباية سوداء ناصعة النظافة، خالية من البقع والغبار ومعطرة بالعود</td></tr>
  <tr><th>الملمس</th><td>منديل قطني ناعم مبلل بسائل تنظيف الأقمشة الداكنة</td></tr>
  <tr><th>العطر</th><td>عطر العود والمسك الملكي الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>منظفات أقمشة داكنة، عطر العود، مرطبات نسيجية</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الصين</td></tr>
  <tr><th>الشركة المصنعة</th><td>Nawras Hygiene Labs</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد مناديل تنظيف العباية الفورية من نورس (Nawras Abaya Wipes)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج مناديل نورس لتنظيف العباية مشكلة البقع الطارئة (كالمكياج، الأطعمة، والغبار) أثناء التواجد بالعمل أو المناسبات، وبقع الغسيل البيضاء.</p>

<h3>لماذا تنجح تركيبة تنظيف العباية الخاصة؟</h3>
<p>لأن السائل المخصص يذوب الأصباغ والزيوت المستعصية دون إحداث هالة بيضاء (White Ring) على القماش الأسود.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>المسح الفوري عند حدوث البقعة:</strong> امسحي البقعة فور حدوثها لمنع تغلغلها بأنسجة القماش.<br>
2. <strong>الإغلاق المحكم للشريط:</strong> اغلقي الشريط اللاصق فوراً لمنع جفاف المناديل المتبقية.<br>
3. <strong>الاحتفاظ بها في حقيبة اليد:</strong> اجعلي عبوة 25 منديل رفيقتكِ اليومية بالعمل والسفر.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مناديل تنظيف العباية تسبب بهتان اللون الأسود وإحداث بقع بيضاء."<br>
<strong>الحقيقة:</strong> مناديل نورس مصممة بحماية ثبات اللون الأسود وتضمن نظافة العباية دون أي آثار بيضاء.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تفكك المذيبات الخفيفة بوليمرات المكياج والزيوت، فتمتصها ألياف المنديل دون التأثير على صبغة القماش السوداء.</p>"""

    faqs = [
        ("ما هي مناديل نورس منظفة للعباية 25 منديل؟", "هي مناديل مبللة فورية مخصصة لإزالة البقع والغبار عن العباية والملابس السوداء بعطر العود دون غسيل 25 منديل."),
        ("ما هي فوائد سائل تنظيف العباية وعطر العود؟", "يزيل البقع الطارئة فورياً، يحمي اللون الأسود من البقع البيضاء، ويترك العباية معطرة بالعود."),
        ("هل تترك بقعاً بيضاء على القماش الأسود؟", "لا، مثبتة في الحفاظ على ثبات اللون الأسود الفاخر دون ترك أي أثر أبيض."),
        ("كم منديل تحتوي العبوة؟", "تحتوي العبوة على 25 منديل قطني مبلل."),
        ("كيف تُستخدم بالشكل الصحيح؟", "اسحبي منديلاً، امسحي البقعة بالعباية بلطف بحركات دائرية واغلقي الشريط اللاصق محكماً فوراً."),
        ("هل تحتاج العباية للغسيل أو الشطف بالماء بعد استخدامها؟", "لا تحتاج لشطف بالماء، تترك العباية نظيفة ومعطرة فورياً."),
        ("ما هو بلد صنع مناديل نورس؟", "صُنع وفق أعلى المعايير الصحية والعناية بالملابس."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات العناية لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل تزيل بقع المكياج والأطعمة والزيوت الطارئة؟", "نعم، تزيل بقع الفاونديشن، الأطعمة، والزيوت الطارئة بسهولة."),
        ("ما هي رائحة مناديل نورس للعباية؟", "تتميز برائحة العود والمسك الفاخرة التي تثبت بالعباية."),
        ("هل العبوة 25 منديل مناسبة للحقيبة والمناسبات؟", "نعم، حجم مدمج وأنيق مثالي لحمل الحقيبة والعمل والمناسبات."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف مع إغلاق الشريط اللاصق محكماً."),
        ("هل المناديل ناعمة على أقمشة العباية الحريرية؟", "نعم، مناديل قطنية فائقة النعومة تنزلق دون تنسيل ألياف القماش."),
        ("هل العبوة محكمة الغلق؟", "تأتي بشريط لاصق متين يمنع جفاف المناديل المتبقية."),
        ("هل تناسب جميع أنواع العباءات والملابس السوداء؟", "ممتازة لجميع أقمشة العباءات السوداء والملابس الداكنة والملونة."),
        ("كم مرة يُفضل استخدامها يومياً؟", "تُستخدم عند الحاجة لإزالة البقع الطارئة."),
        ("هل تمنح حس نظافة وثقة طوال اليوم؟", "نعم، تمنحكِ ثقة ونظافة فورية بعبايتكِ."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل تساعد في إنعاش العباية المعطرة؟", "نعم، عطر العود يجدد عبق وانتعاش العباية."),
        ("هل هي المناديل المنظفة للعباية الأكثر طلباً؟", "نعم، مناديل نورس الخيار الأول والعملي لتنظيف العباية."),
        ("هل تترك العباية جافة بسرعة؟", "نعم، يجف سائل التنظيف خلال ثوانٍ لتصبح العباية جاهزة."),
        ("هل تناسب العبايات المطرزة بالخرز؟", "نعم، تنظف الأقمشة المحيطة بالقماش المطرز ب أمان."),
        ("هل تناسب السفر والرحلات؟", "نعم، المنتج الأكثر أهمية وسهولة في السفر والرحلات."),
        ("هل تترك ملمساً نظيفاً؟", "نعم، تترك القماش ناصع السواد ومسترخياً."),
        ("هل تتوفّر بسعر ممتاز لدى إكليل أبها؟", "نعم، تتوفّر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Nawras Abaya Cleaning Wipes - 25 Wipes</strong> are the instant dark fabric cleaning wipes engineered to eliminate sudden stains, food spills, makeup, and dust from black abayas and dark garments without requiring a full wash or water rinsing. Formulated by Nawras with color-protection technology infused with Oud and Musk scent.</p>
<p>Nawras Abaya Wipes dissolve oils, foundation stains, and dust particles with a gentle swipe, leaving zero white rings or bleaching marks on black fabric, keeping your abaya deep black, clean, and fragranced with royal Oud fragrance all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Instant Emergency Stain & Dust Removal:</strong> Cleans food, makeup, and oil stains in a single swipe.</li>
  <li><strong>Protects Deep Black Fabric Color:</strong> Leaves zero white rings or bleaching residue on black abayas.</li>
  <li><strong>Enriched with Royal Oud & Musk Fragrance:</strong> Imparts a long-lasting royal Oud aroma to your abaya.</li>
  <li><strong>Ultra-Soft Cotton Wet Wipes:</strong> Glides smoothly across delicate abaya fabrics without snagging threads.</li>
  <li><strong>No Water Rinsing or Washing Required:</strong> Instant cleaning solution for work, events, and travel.</li>
  <li><strong>Compact 25-Wipe Pouch:</strong> Sleek handbag pack featuring a secure adhesive seal to lock in moisture.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Open):</strong> Peel back the protective adhesive seal and pull out a single abaya cleaning wipe.</li>
  <li><strong>Step 2 (Wipe):</strong> Wipe gently over the stained area on the abaya in circular motions (no water rinsing required).</li>
  <li><strong>Step 3 (Reseal):</strong> Reseal the adhesive strip immediately to prevent remaining wipes from drying out.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Dark Fabric Cleansing Fluid:</strong> Dissolves makeup and oil stains without leaving white rings.</li>
  <li><strong>Oud & Musk Fragrance:</strong> Bestows a rich, royal aroma to black garments.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical fabric and garment spot cleaning application only.</li>
  <li>Avoid direct contact with eyes or broken skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place with pouch securely closed.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone wearing black abayas or dark garments seeking instant emergency stain removal wipes with Oud fragrance.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Nawras</td></tr>
  <tr><th>Category</th><td>Personal Care / Instant Black Abaya & Dark Fabric Cleansing Wipes</td></tr>
  <tr><th>Product Type</th><td>Oud-Scented Emergency Abaya Stain Remover Wipes (25 Wipes)</td></tr>
  <tr><th>Volume/Weight</th><td>25 Wet Wipes</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Dark Abayas, Black & Colored Garments)</td></tr>
  <tr><th>Finish</th><td>Clean, stain-free, deep black abaya fabric fragranced with Oud</td></tr>
  <tr><th>Texture</th><td>Soft cotton wipe soaked in dark fabric cleanser</td></tr>
  <tr><th>Fragrance</th><td>Royal Oud & Musk scent</td></tr>
  <tr><th>Active Ingredients</th><td>Dark Fabric Cleansers, Oud Fragrance, Fabric Softeners</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / China</td></tr>
  <tr><th>Manufacturer</th><td>Nawras Hygiene Labs</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Solvent Emulsification & White Ring Prevention</h2>

<h3>What problem does this solve?</h3>
<p>Nawras Abaya Cleaning Wipes resolve emergency makeup spills, food stains, dust streaks, and white washing residue on black abayas.</p>

<h3>Why choose Nawras Abaya Wipes?</h3>
<p>Specialized dark fabric cleansers emulsify lipid stains rapidly, lifting pigments into the wipe without leaching black dyes or leaving a white halo.</p>"""

    en_faqs = [
        ("What are Nawras Abaya Cleaning Wipes - 25 Wipes?", "They are instant wet wipes designed to erase stains, food spills, and makeup from black abayas with an Oud fragrance."),
        ("What are the benefits of dark fabric cleansers and Oud scent?", "Erases stains instantly, protects black color without white rings, and leaves abayas fragranced with Oud."),
        ("Do they leave white marks on black fabric?", "No, clinically proven to preserve deep black fabric color with zero white rings."),
        ("How many wipes are in a pack?", "Each pack contains 25 soft, moist cotton wipes."),
        ("How do I use them correctly?", "Wipe gently over the stain on your abaya, then reseal the adhesive strip immediately."),
        ("Is water rinsing or washing required?", "No water rinsing is needed; fluid dries clean in seconds leaving abayas clean and fragranced."),
        ("Where are Nawras Abaya Wipes manufactured?", "Produced following international fabric care safety standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All fabric care products at Ekleel Abha are 100% original from certified distributors."),
        ("Do they remove makeup, oil, and food stains?", "Yes, effortlessly clears foundation, oil, and food spills from abaya fabrics."),
        ("What scent do Nawras Abaya Wipes have?", "Features a luxurious, long-lasting royal Oud and Musk fragrance."),
        ("Is the 25-wipe pack handbag-friendly?", "Yes, compact pouch fits easily into purses, work totes, and travel bags."),
        ("How should I store the pack?", "Store in a cool, dry place with the adhesive seal closed tightly."),
        ("Are the cotton wipes gentle on silk and chiffon abayas?", "Yes, soft cotton texture glides smoothly over silk and chiffon without pulling threads."),
        ("Is the pouch seal secure?", "Yes, equipped with a durable adhesive strip to lock in moisture."),
        ("Are they suitable for all black garments and colored clothes?", "Ideal for black abayas, dark suits, and colored garments."),
        ("How often can I use them daily?", "Use as needed whenever emergency stain removal is required."),
        ("Do they provide instant stain confidence?", "Yes, guarantees instant cleanliness and confidence in your abaya appearance."),
        ("Is the pouch recyclable?", "Yes, 100% recyclable environmentally friendly pouch."),
        ("Do they refresh abaya fragrance?", "Yes, Oud fragrance refreshes abaya scent instantly."),
        ("Are they the #1 choice for abaya stain removal?", "Yes, Nawras Abaya Wipes are the top favorite choice for emergency abaya care."),
        ("Do they dry quickly on fabric?", "Yes, fluid dries in seconds leaving abayas ready to wear."),
        ("Are they safe for beaded and embroidered abayas?", "Yes, cleans fabric around beads and embroidery safely."),
        ("Are they essential for travel and work?", "Yes, the #1 essential item for work, events, and travel."),
        ("Do they leave fabric feeling soft?", "Yes, leaves abaya fabric clean, soft, and relaxed."),
        ("Are they available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1860",
        "sku": "EK-1860",
        "gtin": "6928388520948",
        "category": "العناية الشخصية / مناديل تنظيف العباية والملابس السوداء الفورية",
        "brand": "Nawras",
        "ar": {
            "title": "مناديل نورس  منظفة للعباية 25 منديل",
            "meta_title": "مناديل نورس منظفة للعباية 25منديل | إكليل أبها",
            "meta_description": "اشتري مناديل نورس منظفة للعباية (25 منديل). مناديل فورية لإزالة بقع العباية بعطر العود دون ترك آثار بيضاء. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["نورس", "مناديل_نورس", "منظف_العباية", "مناديل_العباية", "إكليل_أبها"]
        },
        "en": {
            "title": "Nawras Abaya Cleaning Wipes - 25 Wipes",
            "meta_title": "Nawras Abaya Cleaning Wipes 25 Wipes | Ekleel Abha",
            "meta_description": "Buy original Nawras Abaya Cleaning Wipes (25 Wipes). Instant Oud-scented emergency black abaya stain remover wipes. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["nawras", "nawras_wipes", "abaya_wipes", "stain_remover_wipes", "ekleel_abha"]
        },
        "schema": {
            "brand": "Nawras",
            "category": "Personal Care / Abaya Wipes",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "nawras-abaya-cleaning-wipes-25-wipes.webp",
            "alt": "Nawras Abaya Cleaning Wipes 25 Wipes",
            "title": "Nawras Abaya Cleaning Wipes 25 Wipes"
        }
    }

print("Loaded all 5 Batch 30 builders cleanly")
