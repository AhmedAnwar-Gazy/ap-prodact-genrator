import json, os

def create_product_1968():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مزيل عرق دراي كومفورت من نيفيا - 40مل (Nivea Dry Comfort Deodorant Stick - 40ml)</strong> مزيل ومضاد التعرق الجاف الأصيل من نيفيا الألمانية المصمم لتوفير حماية جافة ومريحة للغاية لـ 48 ساعة ضد البلل والتعرق ورائحة العرق. يرتكز هذا المزيل الطبي (Nivea Dry Comfort Stick 40ml) على التركيبة الثنائية المضادة للتعرق (Dual Active Formula) المعززة بالمعادن الجافة وخلاصة نيفيا للعناية بالبشرة.</p>
<p>يعمل مزيل عرق نيفيا دراي كومفورت على حماية الإبطين من بلل العرق الشديد، القضاء التام على البكتيريا المسببة للرائحة، والحفاظ على نعومة وجفاف جلد الإبطين دون تكتل، ليترك بشرتك ناصعة النظافة، جافة تماماً، ومعطرة بالنظافة الأيقونية لنيفيا طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية جافة ومريحة للغاية لـ 48 ساعة:</strong> تمنع البلل والتعرق المزعج تحت الإبطين.</li>
  <li><strong>التركيبة الثنائية النشطة بالمعادن الجافة (Dual Active System):</strong> تضمن أعلى كفاءة جفاف.</li>
  <li><strong>عطر النظافة الأيقوني الناعم من نيفيا:</strong> يمنح الإبطين رائحة النظافة والأناقة طوال اليوم.</li>
  <li><strong>خالٍ تماماً من الكحول والصبغات الصناعية:</strong> آمن ولطيف على البشرة الحساسة.</li>
  <li><strong>اختبر جلدياً لحماية البشرة من التهيج:</strong> لا يسبب احمراراً أو حساسية.</li>
  <li><strong>قلم اصبع ستيك مدمج سعة 40 مل:</strong> تطبيق سهل ومريح في الحقيبة والجيب.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> مرري اصبع ستيك نيفيا دراي كومفورت برفق على بشرة إبطين جافة ونظيفة بعد الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> دعي المنتج يجف طبيعياً لبضع ثوان قبل ارتداء الملابس (يُستعمل كل صباح).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>التركيبة الثنائية بالمعادن الجافة وأملاح الألومنيوم:</strong> تنظم عملية التعرق وتمنح الإبطين جفافاً مستمراً.</li>
  <li><strong>مركبات العناية بالبشرة من نيفيا:</strong> تهدئ جلد الإبطين وتحفظ ملمسه الناعم الحريري.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة تحت الإبطين فقط.</li>
  <li>تجنبي التطبيق على البشرة الملتهبة أو المصابة بجروح بعيد الحلاقة مباشرة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن مزيل عرق نيفيا دراي كومفورت 40 مل للحماية الجافة المريحة لـ 48 ساعة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>نيفيا (NIVEA)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / مزيلات ومضادات التعرق من نيفيا 40ml</td></tr>
  <tr><th>نوع المنتج</th><td>مزيل ومضاد تعرق ستيك بالمعادن الجافة لـ 48 ساعة (40ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>40 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة تحت الإبطين (العادية والحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>إبطان جافان تماماً، ناعمان، خاليان من الرائحة ومعطران برائحة نيفيا الناعمة</td></tr>
  <tr><th>الملمس</th><td>ستيك صلب كريمي ينزلق بنعومة دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر نيفيا الكلاسيكي الناعم النظيف</td></tr>
  <tr><th>المكونات النشطة</th><td>التركيبة الثنائية بالمعادن الجافة، أملاح ألومنيوم مضادة للتعرق، مركبات عناية</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا (Germany)</td></tr>
  <tr><th>الشركة المصنعة</th><td>NIVEA (Beiersdorf Germany)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد التركيبة الثنائية بالمعادن الجافة في نيفيا دراي كومفورت (Nivea Dry Comfort)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مزيل نيفيا دراي كومفورت مشكلة بلل العرق المزعج، الرطوبة العالية، ورائحة العرق تحت الإبطين.</p>

<h3>لماذا تنجح تقنية المعادن الجافة Dual Active؟</h3>
<p>لأن دمج اثنين من المكونات النشطة المضادة للتعرق مع المعادن الامتصاصية يضمن تنظيم إفراز العرق بفاعلية مضاعفة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على بشرة جافة ونظيفة تماماً:</strong> بعد الاستحمام صباحاً.<br>
2. <strong>الانتظار ثوانٍ قبل ارتداء الملابس:</strong> يمنح أفضل حماية للملابس.<br>
3. <strong>الاستخدام المنتظم:</strong> يحافظ على أقصى درجات الجفاف والراحة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مزيلات العرق الستيك تترك تكتلات بيضاء على الملابس."<br>
<strong>الحقيقة:</strong> نيفيا دراي كومفورت مصمم بتقنية انزلاق ناعمة تمنع التكتل أو ترك آثار على الأقمشة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتفاعل هيدروكسي كلوريد الألومنيوم مع المعادن لتقليل القطر القنواتي للغدد العرقية المفترزية بنسبة تصل إلى 95%.</p>"""

    faqs = [
        ("ما هو مزيل عرق دراي كومفورت من نيفيا - 40مل؟", "هو مزيل ومضاد تعرق ستيك من نيفيا الألمانية بالمعادن الجافة لحماية 48 ساعة من بلل العرق والرائحة (40 مل)."),
        ("ما هي فوائد التركيبة الثنائية بالمعادن الجافة؟", "تضمن المعادن الجافة أعلى كفاءة جفاف مريحة دون بلل، وتمنح عطر النظافة الأيقوني من نيفيا."),
        ("هل يحمي من البلل والتعرق لـ 48 ساعة؟", "نعم، مثبت سريرياً في توفير جفاف تام وحماية من الرائحة حتى 48 ساعة."),
        ("ما حجم العبوة؟", "تأتي بعبوة ستيك سعة 40 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "مرري الاصبع على بشرة إبطين جافة ونظيفة كل صباح ودعيه يجف ثوانٍ قبل ارتداء الملابس."),
        ("هل هو خالي من الكحول؟", "نعم، 100% خالٍ من الكحول وآمن للبشرة الحساسة."),
        ("أين صُنع مزيل عرق نيفيا؟", "صُنع في ألمانيا بواسطة Beiersdorf Germany."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات نيفيا لدى إكليل أبها أصلية 100%."),
        ("ما رائحة نيفيا دراي كومفورت؟", "عطر نيفيا الكلاسيكي الناعم النظيف الأنيق."),
        ("هل يترك أثراً على الملابس؟", "لا، ينزلق بنعومة دون ترك آثار أو تكتلات على الملابس."),
        ("هل العبوة 40 مل مناسبة للحقيبة؟", "نعم، حجم ستيك مدمج أنيق مثالي للحقيبة والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب ممارسة الرياضة والأنشطة اليومية؟", "نعم، ممتاز للانتعاش والجفاف في العمل والرياضة."),
        ("كم مرة يومياً؟", "مرة واحدة كل صباح."),
        ("هل نيفيا الماركة الأولى عالمياً في العناية بالبشرة؟", "نعم، NIVEA علامة عالمية رائدة وأسطورية في العناية بالبشرة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع الفئات ذوي البشرة العادية والحساسة."),
        ("هل يمنع تكاثر بكتيريا العرق؟", "نعم، يقضي على البكتيريا المسببة لرائحة العرق."),
        ("هل يترك الإبطين ناعمين؟", "نعم، يمنح الإبطين ملمساً ناعماً حريرياً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يجف سريعاً على الجلد؟", "نعم، ينزلق ويجف في ثوانٍ معدودة دون لزوجة."),
        ("هل يسبب احمراراً بعد الحلاقة؟", "يُفضل الانتظار قليلاً بعد الحلاقة قبل التطبيق لتجنب أي تهيج."),
        ("هل يصلح هدية ضمن مجموعة العناية؟", "نعم، منتج أنيق وعملي جداً في العناية الشخصية."),
        ("هل يحمي في الصيف الحار؟", "نعم، حماية ممتازة جداً من البلل في أشد أيام الصيف حرارة."),
        ("هل يتوفر بصيغ رول أون وبخاخ أيضاً؟", "نعم، تتوفر عائلة Nivea Dry بأشكال متعددة.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Nivea Dry Comfort Deodorant Stick - 40ml</strong> is an authentic dry antiperspirant deodorant stick from Nivea Germany designed to deliver 48-hour comfortable dry protection against wetness, sweat, and body odor. Built upon Nivea's Dual Active Formula enriched with dry minerals and skin-caring ingredients.</p>
<p>Nivea Dry Comfort Deodorant Stick shields underarms against heavy sweat wetness, completely eliminates odor-causing bacteria, and preserves underarm skin softness without clumping, leaving your skin touchably dry, spotlessly clean, and fragranced with Nivea's iconic cleanliness scent all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>48-Hour Comfortable Dry Protection:</strong> Prevents wetness and heavy underarm sweating.</li>
  <li><strong>Dual Active System with Dry Minerals:</strong> Ensures maximum drying performance.</li>
  <li><strong>Iconic Soft Nivea Cleanliness Fragrance:</strong> Imparts an elegant scent of cleanliness all day.</li>
  <li><strong>100% Free from Alcohol & Artificial Colors:</strong> Safe and gentle on sensitive underarm skin.</li>
  <li><strong>Dermatologically Tested:</strong> Shields skin from irritation and redness.</li>
  <li><strong>Compact 40ml Stick Container:</strong> Convenient easy application perfect for handbag and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Glide Nivea Dry Comfort stick gently onto completely clean, dry underarm skin after shower.</li>
  <li><strong>Step 2:</strong> Allow product to dry naturally for a few seconds before dressing (use daily every morning).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Dual Active Formula with Dry Minerals & Aluminum Salts:</strong> Regulate sweat secretions delivering continuous underarm dryness.</li>
  <li><strong>Nivea Skincare Compounds:</strong> Soothe underarm skin maintaining its silky smooth touch.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical underarm application only.</li>
  <li>Avoid applying onto irritated, broken, or freshly shaved underarm skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Nivea Dry Comfort 40ml Deodorant Stick for reliable 48-hour dry protection.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>NIVEA</td></tr>
  <tr><th>Category</th><td>Personal Care / Nivea Antiperspirant Deodorants 40ml</td></tr>
  <tr><th>Product Type</th><td>48H Dual Active Dry Minerals Antiperspirant Deodorant Stick (40ml)</td></tr>
  <tr><th>Volume/Weight</th><td>40 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Underarm Skin Types (Normal & Sensitive)</td></tr>
  <tr><th>Finish</th><td>Completely dry, smooth underarms fragranced with soft Nivea cleanliness scent</td></tr>
  <tr><th>Texture</th><td>Smooth creamy solid stick gliding without stickiness</td></tr>
  <tr><th>Fragrance</th><td>Classic soft clean Nivea fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Dual Active Formula, Dry Minerals, Aluminum Chlorohydrate, Care Agents</td></tr>
  <tr><th>Country of Origin</th><td>Germany</td></tr>
  <tr><th>Manufacturer</th><td>NIVEA (Beiersdorf Germany)</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Dual Active Minerals Occlusion & Nivea Epidermal Conditioning</h2>

<h3>What problem does this solve?</h3>
<p>Nivea Dry Comfort Deodorant Stick resolves underarm wetness, heavy sweating, high humidity discomfort, and body odor.</p>

<h3>Why choose Nivea Dry Comfort Deodorant Stick?</h3>
<p>Combining two active antiperspirant compounds with absorbent minerals ensures optimal sweat duct regulation reducing sweat flow by up to 95%.</p>"""

    en_faqs = [
        ("What is Nivea Dry Comfort Deodorant Stick - 40ml?", "It is a dry antiperspirant deodorant stick from Nivea Germany with dry minerals for 48h dry protection (40ml)."),
        ("What are the benefits of the Dual Active formula with dry minerals?", "Dry minerals deliver maximum drying performance keeping underarms dry with iconic Nivea cleanliness fragrance."),
        ("Does it protect against wetness and sweat for 48 hours?", "Yes, clinically proven to deliver complete dryness and odor defense up to 48 hours."),
        ("What volume is contained in this stick?", "40ml stick container."),
        ("How do I use it correctly?", "Glide on clean dry underarm skin every morning, let dry for seconds before dressing."),
        ("Is it alcohol-free?", "Yes, 100% alcohol-free and safe for sensitive skin."),
        ("Where is Nivea Deodorant manufactured?", "In Germany by Beiersdorf Germany."),
        ("How do I verify authenticity at Ekleel Abha?", "All Nivea products at Ekleel Abha are 100% original."),
        ("What scent does Nivea Dry Comfort have?", "Classic soft clean elegant Nivea fragrance."),
        ("Does it leave marks on clothes?", "No, glides smoothly without leaving residue or clumps on fabrics."),
        ("Is the 40ml stick handbag friendly?", "Yes, sleek compact stick ideal for handbag and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for workouts and daily activities?", "Yes, excellent for daily work and sports routines."),
        ("How many times daily?", "Once every morning."),
        ("Is Nivea a global #1 skincare brand?", "Yes, NIVEA is a globally leading iconic skincare brand."),
        ("Is the container recyclable?", "Yes."),
        ("Is it suitable for men and women?", "Suitable for all user categories seeking comfortable dry underarms."),
        ("Does it eliminate odor-causing bacteria?", "Yes, eliminates bacteria responsible for body odor."),
        ("Does it leave underarms smooth?", "Yes, leaves underarms silky smooth and soft."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it dry quickly on skin?", "Yes, glides and dries in seconds without stickiness."),
        ("Does it cause redness post-shaving?", "Prefer waiting shortly post-shaving before application to avoid irritation."),
        ("Is it a practical care gift?", "Yes, practical sleek addition to personal care gift sets."),
        ("Does it protect in hot summer weather?", "Yes, superior protection against wetness on hot summer days."),
        ("Are roll-on and spray versions available?", "Yes, the Nivea Dry family offers multiple formats.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1968",
        "sku": "EK-1968",
        "gtin": "42096276",
        "brand": "NIVEA",
        "ar": {
            "title": "مزيل عرق دراي كومفورت من نيفيا - 40مل",
            "meta_title": "مزيل عرق نيفيا دراي كومفورت ستيك 40مل | إكليل أبها",
            "meta_description": "اشتري مزيل عرق نيفيا دراي كومفورت ستيك (40 مل). مزيل ومضاد تعرق بالمعادن الجافة لحماية 48 ساعة من البلل والرائحة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["نيفيا", "دراي_كومفورت", "ستيك_نيفيا", "مزيل_عرق_جاف", "إكليل_أبها"]
        },
        "en": {
            "title": "Nivea Dry Comfort Deodorant Stick - 40ml",
            "meta_title": "Nivea Dry Comfort Deodorant Stick 40ml | Ekleel Abha",
            "meta_description": "Buy original Nivea Dry Comfort Deodorant Stick (40ml). 48H Dual Active dry minerals antiperspirant stick. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["nivea", "dry_comfort", "nivea_stick", "antiperspirant_deodorant", "ekleel_abha"]
        }
    }


def create_product_1969():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مزيل عرق بروتيكت اند كير 40مل (Protect & Care Deodorant 40ml)</strong> مزيل ومضاد التعرق الطبي اللطيف الفاخر من نيفيا الألمانية المصمم خصيصاً لجمع الحماية الفائقة لـ 48 ساعة مع مكونات كريم نيفيا الأزرق الأصلي للرعاية المغذية تحت الإبطين. يرتكز هذا المزيل الأصيل (Nivea Protect & Care Stick 40ml) على مركب العناية الفريد لكريم نيفيا (Nivea Creme Ingredients)، أملاح مضاد التعرق، والزيوت المهدئة للجلد.</p>
<p>يعمل مزيل عرق بروتيكت أند كير على حماية الإبطين من التعرق ورائحة العرق لـ 48 ساعة، تغذية وتهدئة جلد الإبطين المجهد بعد الحلاقة، ومنح الإبطين ملمساً ناعماً حريرياً وعطراً أيقونياً دافئاً، ليترك بشرتك جافة، مرطبة، موحدة المظهر، ومحمية تماماً طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية فائقة لـ 48 ساعة مدعمة بمكونات كريم نيفيا الأصلي:</strong> تجمع بين حماية الجفاف وعناية الكريمة المغذية.</li>
  <li><strong>عطر كريم نيفيا الأزرق الأيقوني الدافئ:</strong> يمنح الإبطين رائحة النظافة والرعاية الكلاسيكية.</li>
  <li><strong>تهدئة وحماية جلد الإبطين بعد الحلاقة:</strong> تمنع الاحمرار والتهيج والحكة.</li>
  <li><strong>خالٍ 100% من الكحول والصبغات الصناعية:</strong> آمن ولطيف للغاية على البشرة شديدة الحساسية.</li>
  <li><strong>مختبر جلدياً لحماية حاجز البشرة:</strong> يحافظ على نعومة الجلد وتوازنه المائي.</li>
  <li><strong>عبوة ستيك مدمجة سعة 40 مل:</strong> حجم ممتاز للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> مرري الاصبع برفق على بشرة إبطين جافة ونظيفة بعد الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> دعي المنتج يجف طبيعياً لثوانٍ قبل ارتداء الملابس (يُستعمل كل صباح).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مكونات كريم نيفيا الأزرق الأيقوني (Nivea Creme Ingredients):</strong> تغذي وترمم جلد الإبطين وتمنحه نعومة فائقة.</li>
  <li><strong>أملاح مضاد التعرق النشطة:</strong> تنظم إفراز التعرق وتقضي على البكتيريا المسببة للروائح الكريهة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة تحت الإبطين فقط.</li>
  <li>تجنبي التطبيق على الجروح المفتوحة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن مزيل عرق بروتيكت أند كير 40 مل للحماية لـ 48 ساعة وعناية كريم نيفيا الأصلي.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>نيفيا (NIVEA)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / مزيلات ومضادات التعرق من نيفيا بروتيكت أند كير 40ml</td></tr>
  <tr><th>نوع المنتج</th><td>مزيل ومضاد تعرق بمكونات كريم نيفيا لعناية 48 ساعة (40ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>40 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة تحت الإبطين (بما في ذلك الحساسة للغاية)</td></tr>
  <tr><th>المظهر النهائي</th><td>إبطان جافان، ناعمان جداً كالكريم، خاليان من الرائحة ومحميان بعناية نيفيا</td></tr>
  <tr><th>الملمس</th><td>ستيك صلب مغذٍ ينزلق بنعومة دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر كريم نيفيا الأزرق الأصلي الناعم الدافئ</td></tr>
  <tr><th>المكونات النشطة</th><td>مكونات كريم نيفيا، أملاح ألومنيوم مضادة للتعرق، زيوت ملطفة</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا (Germany)</td></tr>
  <tr><th>الشركة المصنعة</th><td>NIVEA (Beiersdorf Germany)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد مكونات كريم نيفيا في مزيل بروتيكت أند كير (Protect & Care)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مزيل بروتيكت أند كير مشكلة تهيج واحمرار الإبطين بعد الحلاقة، الجفاف، ورائحة التعرق.</p>

<h3>لماذا تنجح تركيبة Protect & Care؟</h3>
<p>لأنها تدمج حماية مضاد التعرق مع اللبيدات المرطبة لكريم نيفيا الأصلي لتنعيم وتغذية حواجز الجلد أثناء تنظيم العرق.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على بشرة جافة:</strong> بعد الاستحمام صباحاً.<br>
2. <strong>الاستخدام بعد الحلاقة:</strong> يهدئ البشرة ويمنع التهيج بفضل المكونات الملطفة.<br>
3. <strong>الترك لبضع ثوان حتى يجف:</strong> يحمي الملابس ويضمن ثبات المكونات المغذية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مزيل العرق المحتوي على كريم يسبب لزوجة الإبطين."<br>
<strong>الحقيقة:</strong> بروتيكت أند كير مصمم بامتصاص سريع يمنح جفافاً تاماً مع ملمس مخملي ناعم دون لزوجة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخترق البانثينول والجليسرين الطبقة القرنية لترميم تلف البشرة الناتج عن الحلاقة، بينما تنظم أملاح مضاد التعرق الإفراز العرقي.</p>"""

    faqs = [
        ("ما هو مزيل عرق بروتيكت اند كير 40مل؟", "هو مزيل ومضاد تعرق من نيفيا بمكونات كريم نيفيا الأصلي لحماية 48 ساعة وعناية فائقة بالإبطين (40 مل)."),
        ("ما هي فوائد مكونات كريم نيفيا وأملاح مضاد التعرق؟", "تغذي مكونات كريم نيفيا الجلد وتهدئه بعد الحلاقة، بينما تضمن أملاح التعرق جفافاً لـ 48 ساعة."),
        ("هل يهدئ الإبطين ويحمي من التهيج بعد الحلاقة؟", "نعم، مثبت سريرياً في تهدئة الجلد ومنع الاحمرار والتهيج بعد الحلاقة."),
        ("ما حجم العبوة؟", "تأتي بعبوة ستيك سعة 40 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "مرري الاصبع على بشرة إبطين جافة ونظيفة كل صباح ودعيه يجف ثوانٍ قبل ارتداء الملابس."),
        ("هل هو خالي من الكحول؟", "نعم، 100% خالٍ من الكحول وآمن للبشرة شديدة الحساسية."),
        ("أين صُنع مزيل بروتيكت أند كير؟", "صُنع في ألمانيا بواسطة Beiersdorf Germany."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات نيفيا لدى إكليل أبها أصلية 100%."),
        ("ما رائحة مزيل بروتيكت أند كير؟", "عطر كريم نيفيا الأزرق الأصلي الدافئ الناعم."),
        ("هل يترك أثراً على الملابس؟", "لا، ينزلق بنعومة دون ترك بقع أو آثار على الملابس."),
        ("هل العبوة 40 مل مناسبة للحقيبة؟", "نعم، حجم ستيك مدمج أنيق مثالي للحقيبة والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب ممارسة الرياضة والأنشطة؟", "نعم، ممتاز للانتعاش والجفاف في العمل والرياضة."),
        ("كم مرة يومياً؟", "مرة واحدة كل صباح."),
        ("هل نيفيا الماركة الأولى عالمياً في العناية بالبشرة؟", "نعم، NIVEA علامة عالمية رائدة وأسطورية في العناية بالبشرة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب النساء والرجال؟", "مناسب للجميع وخاصة أصحاب البشرة الحساسة المعرضة للتهيج."),
        ("هل يمنع تكاثر بكتيريا العرق؟", "نعم، يقضي على البكتيريا المسببة لرائحة العرق."),
        ("هل يترك الإبطين ناعمين كالكريم؟", "نعم، يمنح الإبطين ملمساً ناعماً مخملياً جداً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يجف سريعاً على الجلد؟", "نعم، يجف في ثوانٍ معدودة دون لزوجة."),
        ("هل يناسب الشتاء والصيف؟", "نعم، ممتاز لجميع فصول السنة."),
        ("هل يصلح هدية ضمن مجموعة العناية؟", "نعم، منتج أنيق وعملي جداً في العناية الشخصية."),
        ("هل يحمي من الجفاف الشديد للإبطين؟", "نعم، يغذي البشرة ويحميها من الجفاف والتشقق."),
        ("هل يتوفر بصيغ رول أون وبخاخ؟", "نعم، تتوفر عائلة Protect & Care بأشكال متعددة.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Protect & Care Deodorant 40ml</strong> is a premium medical antiperspirant deodorant stick from Nivea Germany specifically designed to combine 48-hour antiperspirant protection with the nourishing care ingredients of original Nivea Creme. Built upon Nivea Creme Ingredients, active antiperspirant salts, and skin-soothing oils.</p>
<p>Nivea Protect & Care Deodorant shields underarms against sweat and odor for 48 hours, deeply nourishes and calms underarm skin stressed by shaving, and imparts a velvety soft touch and iconic warm fragrance, leaving your skin dry, hydrated, even-toned, and protected all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>48-Hour Superior Protection Enriched with Nivea Creme Ingredients:</strong> Combines dry protection with rich creme nourishment.</li>
  <li><strong>Iconic Warm Original Nivea Blue Creme Fragrance:</strong> Imparts a classic comforting scent of cleanliness.</li>
  <li><strong>Post-Shaving Underarm Soothing & Protection:</strong> Prevents redness, irritation, and itching after shaving.</li>
  <li><strong>100% Alcohol-Free & Colorant-Free:</strong> Extremely safe and gentle on ultra-sensitive skin.</li>
  <li><strong>Dermatologically Tested Barrier Care:</strong> Preserves skin softness and moisture balance.</li>
  <li><strong>Compact 40ml Stick Container:</strong> Excellent size for daily care and travel convenience.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Glide stick gently onto completely clean, dry underarm skin after shower.</li>
  <li><strong>Step 2:</strong> Allow product to dry naturally for a few seconds before dressing (use daily every morning).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Nivea Creme Ingredients:</strong> Nourish and restore underarm skin giving it touchable softness.</li>
  <li><strong>Active Antiperspirant Salts:</strong> Regulate sweat secretions and eliminate odor-causing bacteria.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical underarm application only.</li>
  <li>Avoid applying onto open wounds or heavily broken skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Protect & Care 40ml Deodorant Stick for 48-hour protection and original Nivea Creme care.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>NIVEA</td></tr>
  <tr><th>Category</th><td>Personal Care / Nivea Protect & Care Deodorants 40ml</td></tr>
  <tr><th>Product Type</th><td>48H Antiperspirant Deodorant Stick with Nivea Creme Ingredients (40ml)</td></tr>
  <tr><th>Volume/Weight</th><td>40 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Underarm Skin Types (Including Ultra-Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Dry, velvety soft, creme-hydrated underarms with classic Nivea fragrance</td></tr>
  <tr><th>Texture</th><td>Smooth nourishing solid stick gliding without stickiness</td></tr>
  <tr><th>Fragrance</th><td>Original warm soft iconic Nivea Blue Creme fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Nivea Creme Ingredients, Aluminum Chlorohydrate, Soothing Oils</td></tr>
  <tr><th>Country of Origin</th><td>Germany</td></tr>
  <tr><th>Manufacturer</th><td>NIVEA (Beiersdorf Germany)</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Nivea Creme Lipids Epidermal Repair & Antiperspirant Sweat Regulation</h2>

<h3>What problem does this solve?</h3>
<p>Protect & Care Deodorant Stick resolves post-shaving underarm irritation, redness, dryness, and body odor.</p>

<h3>Why choose Nivea Protect & Care Deodorant Stick?</h3>
<p>Nivea Creme lipids (panthenol, glycerin) penetrate damaged stratum corneum layers restoring post-shave barrier function while antiperspirant salts regulate sweat.</p>"""

    en_faqs = [
        ("What is Protect & Care Deodorant 40ml?", "It is a medical antiperspirant deodorant stick from Nivea with original Nivea Creme ingredients for 48h protection (40ml)."),
        ("What are the benefits of Nivea Creme ingredients and antiperspirant salts?", "Nivea Creme ingredients nourish and soothe skin post-shaving while antiperspirant salts ensure 48h dryness."),
        ("Does it soothe underarms and prevent post-shave irritation?", "Yes, clinically proven to soothe skin and prevent post-shaving redness and itching."),
        ("What volume is contained in this stick?", "40ml stick container."),
        ("How do I use it correctly?", "Glide on clean dry underarm skin every morning, let dry for seconds before dressing."),
        ("Is it alcohol-free?", "Yes, 100% alcohol-free and safe for ultra-sensitive skin."),
        ("Where is Protect & Care manufactured?", "In Germany by Beiersdorf Germany."),
        ("How do I verify authenticity at Ekleel Abha?", "All Nivea products at Ekleel Abha are 100% original."),
        ("What scent does Protect & Care have?", "Original warm soft iconic Nivea Blue Creme fragrance."),
        ("Does it leave marks on clothes?", "No, glides smoothly without leaving marks or stains on fabrics."),
        ("Is the 40ml stick handbag friendly?", "Yes, sleek compact stick ideal for handbag and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for workouts and daily activities?", "Yes, excellent for daily work and sports routines."),
        ("How many times daily?", "Once every morning."),
        ("Is Nivea a global #1 skincare brand?", "Yes, NIVEA is a globally leading iconic skincare brand."),
        ("Is the container recyclable?", "Yes."),
        ("Is it suitable for men and women?", "Suitable for anyone seeking gentle skin care and sweat protection."),
        ("Does it eliminate odor-causing bacteria?", "Yes, eliminates bacteria responsible for body odor."),
        ("Does it leave underarms velvety soft?", "Yes, leaves underarms touchably soft and velvety."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it dry quickly on skin?", "Yes, dries in seconds without stickiness."),
        ("Is it suitable for all seasons?", "Yes, excellent for summer and winter care."),
        ("Is it a practical care gift?", "Yes, practical sleek addition to personal care gift sets."),
        ("Does it protect against extreme underarm dryness?", "Yes, nourishes skin guarding against dryness and cracking."),
        ("Are roll-on and spray versions available?", "Yes, the Protect & Care family offers multiple formats.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1969",
        "sku": "EK-1969",
        "gtin": "4005900243850",
        "brand": "NIVEA",
        "ar": {
            "title": "مزيل عرق بروتيكت اند كير 40مل",
            "meta_title": "مزيل عرق نيفيا بروتيكت أند كير 40مل | إكليل أبها",
            "meta_description": "اشتري مزيل عرق بروتيكت أند كير من نيفيا (40 مل). مزيل عرق بمكونات كريم نيفيا لحماية 48 ساعة وتهدئة الجلد بعد الحلاقة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["نيفيا", "بروتيكت_اند_كير", "مزيل_عرق_كريم_نيفيا", "عناية_الإبطين", "إكليل_أبها"]
        },
        "en": {
            "title": "Protect & Care Deodorant 40ml",
            "meta_title": "Nivea Protect & Care Deodorant 40ml | Ekleel Abha",
            "meta_description": "Buy original Protect & Care Deodorant (40ml). Nivea Creme enriched 48H antiperspirant stick. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["nivea", "protect_and_care", "nivea_creme_deodorant", "antiperspirant", "ekleel_abha"]
        }
    }


def create_product_1970():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم جليسرين من جليسولد 100 مل (Glysolid Glycerin Cream - 100 ml)</strong> كريم الترطيب والعلاج المكثف الأسطوري الألماني من جليسولد المصمم خصيصاً لإصلاح البشرة شديدة الجفاف والتالفة والمتشققة. يرتكز هذا الكريم الطبي الأصيل (Glysolid Cream 100ml) على نسبة الجليسرين النقي الفائقة (50% Pure Glycerin)، مركبات الألانتوين (Allantoin) المرممة للبشرة، والزيوت الواقية.</p>
<p>يعمل كريم جليسولد بالجليسرين على اختراق الطبقات العميقة للجلد، حبس الرطوبة الداخلية بمقدار استثنائي، شفاء التشققات في الكعبين واليدين والمرفقين، وتشكيل طبقة واقية تمنع التأثر بالطقس البارد، ليترك بشرتك ناعمة كالحرير، مرطبة عمقاً، مشفية من الجفاف، ومحمية طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب مكثف وشفاء للتشققات بتركيز 50% جليسرين:</strong> يعالج الجفاف الشديد وتشققات القدمين واليدين.</li>
  <li><strong>ترميم وتجديد الخلايا بمركب الألانتوين (Allantoin):</strong> يسرّع التئام الجلد المتشقق والتالف.</li>
  <li><strong>تشكيل طبقة واقية لحبس الترطيب 24 ساعة:</strong> يحمي الجلد من الطقس البارد والماء.</li>
  <li><strong>تركيبة ألمانية أصلية خالية من العطور القاسية:</strong> لطيفة وآمنة على البشرة الأكثر حساسية.</li>
  <li><strong>مثالي لليدين، القدمين، المرفقين، والركبتين:</strong> ينعم الجلد الخشن المتصلب بفاعلية من الاستخدام الأول.</li>
  <li><strong>عبوة مدمجة سعة 100 مل:</strong> حجم ممتاز للحقيبة والتنقل والاستخدام المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> ضعي الكريم على بشرة جافة ونظيفة (يُفضل بعد الغسيل أو الاستحمام).</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> خذي كمية مناسبة ودلكي بها اليدين أو القدمين أو المناطق شديدة الجفاف.</li>
  <li><strong>الخطوة الثالثة (الامتصاص):</strong> دلكي بحركات دائرية ناعمة حتى امتصاص الكريم بالكامل (يُستعمل 2-3 مرات يومياً وقبل النوم).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الجليسرين النقي بتركيز 50%:</strong> يجذب جزيئات الماء ويحبسها داخل الخلايا القرنية العميقة.</li>
  <li><strong>مركب الألانتوين (Allantoin):</strong> يجدد الخلايا الميتة ويسرّع التئام الجلد المتشقق والمجهد.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم واليدين والقدمين فقط.</li>
  <li>تجنبي التلامس مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من الجفاف الشديد وتشققات اليدين والقدمين ويبحث عن كريم جليسولد 100 مل للشفاء والترطيب.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جليسولد (Glysolid)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات جليسولد للجليسرين والترطيب المكثف 100ml</td></tr>
  <tr><th>نوع المنتج</th><td>كريم جليسرين مكثف بـ 50% جليسرين وألانتوين لإصلاح التشققات (100ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة شديدة الجفاف، المتشققة والتالفة (اليدين والقدمين)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة كالحرير، مشفية من التشققات، مرطبة عمقاً ومحمية</td></tr>
  <tr><th>الملمس</th><td>كريم غني دسم ناعم يشكل طبقة مرطبة حمائية</td></tr>
  <tr><th>العطر</th><td>خالٍ من العطور الصناعية القاسية (عطر خفيف ناعم)</td></tr>
  <tr><th>المكونات النشطة</th><td>جليسرين نقي (50%)، ألانتوين (Allantoin)، زيوت واقية</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا (Germany)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Glysolid (Burnus GmbH Germany)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الجليسرين بتركيز 50% والألانتوين في كريم جليسولد (Glysolid)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم جليسولد مشكلة تشققات الكعبين المؤلمة، جفاف خشونة اليدين، وتصلب الجلد الناتجة عن نقص الترطيب المستمر والطقس البارد.</p>

<h3>لماذا تنجح تركيبة الـ 50% جليسرين والألانتوين؟</h3>
<p>لأن الجليسرين بتركيز 50% يرتبط كيميائياً بالماء في كيراتين الجلد بينما يحفز الألانتوين الانقسام الخلوي لالتئام التشققات.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق المسائي قبل النوم:</strong> ارتداء جوارب قطنية بعد وضع الكريم على القدمين يضاعف الامتصاص والشفاء.<br>
2. <strong>العناية باليدين بعد غسيل الصحون:</strong> يمنع تأثر اليدين بالمنظفات الكيميائية والماء.<br>
3. <strong>الاستخدام المنتظم 2-3 مرات يومياً:</strong> يحافظ على أقصى درجات المرونة والنعومة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريم جليسولد ثقيل ولا يمتصه الجلد."<br>
<strong>الحقيقة:</strong> كريم جليسولد ينفذ لطبقات الجلد مع التدليك ليترك حماية غير لزجة ناعمة جداً.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يرفع الجليسرين الضغط الأسموزي الداخلي للبشرة جادباً جزيئات H2O لـ 10 أضعاف وزنها، بينما الألانتوين يزيد المحتوى المائي في المصفوفة الخارجلية (ECM).</p>"""

    faqs = [
        ("ما هو كريم جليسرين من جليسولد - 100 مل؟", "هو كريم الترطيب والعلاج المكثف الألماني من جليسولد بتركيز 50% جليسرين وألانتوين لإصلاح التشققات والجفاف (100 مل)."),
        ("ما هي فوائد الجليسرين 50% والألانتوين؟", "يحبس الجليسرين الرطوبة بمقدار استثنائي، بينما يسرّع الألانتوين التئام تشققات الكعبين واليدين."),
        ("هل يشفي تشققات الكعبين واليدين بفاعلية؟", "نعم، مثبت سريرياً في شفاء تشققات القدمين واليدين الجافة من الاستخدامات الأولى."),
        ("ما حجم العبوة؟", "تأتي بعبوة علبة بسعة 100 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على اليدين والقدمين الجافين، دلكي حتى الامتصاص 2-3 مرات يومياً وقبل النوم."),
        ("هل هو ألماني أصلي؟", "نعم، صُنع في ألمانيا بواسطة Burnus GmbH Germany."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات جليسولد لدى إكليل أبها أصلية 100%."),
        ("ما رائحة كريم جليسولد؟", "خالٍ من العطور الصناعية القاسية عطر ناعم لطيف جداً."),
        ("هل يحمي الجلد من البرد والماء؟", "نعم، يشكل غلافاً واقياً يحمي الجلد من الطقس البارد والماء والمنظفات."),
        ("هل 100 مل تكفي لفترة جيدة؟", "نعم، تكفي لعدة أسابيع من الاستخدام اليومي المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب المرفقين والركبتين؟", "نعم، ينعم المرفقين والركبتين والجلد المتصلب بفاعلية."),
        ("كم مرة يومياً؟", "2-3 مرات يومياً وخاصة قبل النوم."),
        ("هل جليسولد علامة ألمانية عريقة؟", "نعم، Glysolid علامة ألمانية أسطورية في ترطيب الجليسرين منذ عقود."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للجميع وخاصة أصحاب الأعمال اليدوية والجفاف الشديد."),
        ("هل يسبب لزوجة على الجلد؟", "ينفذ بالتدليك ليترك طبقة ناعمة غير لزجة."),
        ("هل يفضل ارتداء جوارب قطنية بعده؟", "نعم، ارتداء الجوارب القطنية ليلاً يضاعف مفعول التفتيح والشفاء للقدمين."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يمنع تشقق اليدين في الشتاء؟", "نعم، الحماية المثالية ضد جفاف وتعدي البرد الشتوي."),
        ("هل يصلح هدية كلاسيكية مفيدة؟", "نعم، هدية منزلية كلاسيكية لا غنى عنها لكل أسرة."),
        ("هل يناسب بشرة الوجه؟", "مخصص للجسم واليدين والقدمين، وللوجه يُفضل كريمات أخص خفيفة."),
        ("هل ينعم الكعبين في وقت قصير؟", "نعم، تلاحظ النعومة وإعادة المرونة من التطبيق الأول."),
        ("هل يناسب الاستخدام اليومي المستمر؟", "نعم، يناسب الاستخدام اليومي المنتظم للوقاية والترطيب."),
        ("هل العبوة المعدنية/الحمراء مريحة؟", "نعم، علبة جليسولد الحمراء الأيقونية المشهورة.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Glysolid Glycerin Cream - 100 ml</strong> is the iconic German intensive care and crack repair cream from Glysolid specifically designed to repair severely dry, damaged, and cracked skin. Built upon a high concentration of pure glycerin (50% Pure Glycerin), skin-restorative Allantoin compounds, and protective oils.</p>
<p>Glysolid Glycerin Cream penetrates deep skin layers, locks in internal moisture to an extraordinary degree, heals cracks in heels, hands, and elbows, and forms a protective barrier guarding against cold weather, leaving your skin touchably silky soft, deeply hydrated, healed, and protected all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intensive 50% Glycerin Moisture & Crack Repair:</strong> Treats severe dryness and heel/hand cracks.</li>
  <li><strong>Cell Restoration & Regeneration with Allantoin:</strong> Accelerates healing of cracked damaged skin.</li>
  <li><strong>24-Hour Moisture-Lock Barrier:</strong> Shields skin against harsh cold weather and water.</li>
  <li><strong>Original German Formula Free of Harsh Fragrances:</strong> Safe and gentle on the most sensitive skin.</li>
  <li><strong>Ideal for Hands, Feet, Elbows & Knees:</strong> Effectively softens calloused rough skin from first use.</li>
  <li><strong>Compact 100ml Container:</strong> Excellent volume for handbag, travel, and continuous care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Apply cream onto clean dry skin (preferably post-wash or bath).</li>
  <li><strong>Step 2 (Apply):</strong> Take a suitable amount and massage into hands, feet, or extra dry areas.</li>
  <li><strong>Step 3 (Absorb):</strong> Massage in smooth circular motions until fully absorbed (use 2-3 times daily & before bed).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>50% Pure Glycerin:</strong> Draws moisture molecules locking them deep inside stratum corneum cells.</li>
  <li><strong>Allantoin Complex:</strong> Regenerates damaged cells and accelerates healing of cracked skin.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body, hand, and foot skin application only.</li>
  <li>Avoid contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from severe dryness and cracked hands/feet seeking Glysolid 100ml Cream for healing and moisture.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Glysolid</td></tr>
  <tr><th>Category</th><td>Skincare / Glysolid Glycerin Intensive Hydration Creams 100ml</td></tr>
  <tr><th>Product Type</th><td>50% Glycerin & Allantoin Intensive Crack Repair Cream (100ml)</td></tr>
  <tr><th>Volume/Weight</th><td>100 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Severely Dry, Cracked & Damaged Skin (Hands & Feet)</td></tr>
  <tr><th>Finish</th><td>Silky soft, crack-healed, deeply hydrated & protected skin</td></tr>
  <tr><th>Texture</th><td>Rich smooth dense cream forming a protective barrier</td></tr>
  <tr><th>Fragrance</th><td>Free from harsh artificial fragrances (mild soft scent)</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Glycerin (50%), Allantoin, Protective Oils</td></tr>
  <tr><th>Country of Origin</th><td>Germany</td></tr>
  <tr><th>Manufacturer</th><td>Glysolid (Burnus GmbH Germany)</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 50% Glycerin Osmotic Hydration & Allantoin Cellular Healing</h2>

<h3>What problem does this solve?</h3>
<p>Glysolid Glycerin Cream resolves painful heel fissures, rough cracked hands, and skin callousing caused by severe dehydration and cold weather.</p>

<h3>Why choose Glysolid Glycerin Cream?</h3>
<p>50% concentrated Glycerin chemically binds H2O molecules within skin keratin while Allantoin stimulates cell mitosis accelerating fissure closure.</p>"""

    en_faqs = [
        ("What is Glysolid Glycerin Cream - 100 ml?", "It is an intensive hydration and crack repair cream from Glysolid Germany with 50% Glycerin and Allantoin (100ml)."),
        ("What are the benefits of 50% Glycerin and Allantoin?", "50% Glycerin locks in extreme moisture, while Allantoin accelerates healing of heel and hand cracks."),
        ("Does it effectively heal cracked heels and hands?", "Yes, clinically proven to heal dry cracked heels and hands from initial applications."),
        ("What volume is contained in this container?", "100ml tub container."),
        ("How do I use it correctly?", "Apply on clean dry hands and feet, massage until absorbed 2-3 times daily and before bed."),
        ("Is it authentic German made?", "Yes, made in Germany by Burnus GmbH Germany."),
        ("How do I verify authenticity at Ekleel Abha?", "All Glysolid products at Ekleel Abha are 100% original."),
        ("What scent does Glysolid Cream have?", "Free of harsh artificial fragrances with a very mild soft scent."),
        ("Does it protect skin against cold and water?", "Yes, forms a protective barrier shielding skin against cold air, water, and detergents."),
        ("Does 100ml last long?", "Yes, lasts weeks of regular daily use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for elbows and knees?", "Yes, effectively softens elbows, knees, and calloused skin."),
        ("How many times daily?", "2-3 times daily especially bedtime."),
        ("Is Glysolid a historic German brand?", "Yes, Glysolid is a legendary German brand in glycerin moisturizing for decades."),
        ("Is the container recyclable?", "Yes."),
        ("Is it suitable for men and women?", "Yes, great for anyone especially manual workers with severe dryness."),
        ("Does it leave a sticky residue?", "Penetrates upon massage leaving a soft non-greasy protective feel."),
        ("Is it recommended to wear cotton socks afterwards?", "Yes, wearing cotton socks overnight doubles heel healing and softening results."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it prevent winter hand cracking?", "Yes, superior defense against winter cold dryness."),
        ("Is it a classic household gift?", "Yes, an indispensable classic household gift for every family."),
        ("Is it suitable for the face?", "Formulated for body, hands, and feet; prefer lighter creams for face."),
        ("Does it soften heels quickly?", "Yes, softness and elasticity restoration are noticeable from first application."),
        ("Is it suitable for daily continuous use?", "Yes, suitable for daily continuous use for hydration and protection."),
        ("Is the red tub iconic?", "Yes, the famous iconic red Glysolid tin/tub container.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1970",
        "sku": "EK-1970",
        "gtin": "4000196910356",
        "brand": "Glysolid",
        "ar": {
            "title": "كريم جليسرين من جليسولد  100 مل",
            "meta_title": "كريم جليسرين جليسولد 100مل | إكليل أبها",
            "meta_description": "اشتري كريم جليسرين من جليسولد (100 مل). كريم ألماني مكثف بـ 50% جليسرين وألانتوين لإصلاح تشققات اليدين والقدمين. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["جليسولد", "كريم_جليسرين", "علاج_التشققات", "ترطيب_اليدين_والقدمين", "إكليل_أبها"]
        },
        "en": {
            "title": "Glysolid Glycerin Cream - 100 ml",
            "meta_title": "Glysolid Glycerin Cream 100ml | Ekleel Abha",
            "meta_description": "Buy original Glysolid Glycerin Cream (100ml). German 50% Glycerin & Allantoin intensive crack repair cream. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["glysolid", "glycerin_cream", "crack_repair", "hand_foot_care", "ekleel_abha"]
        }
    }


def create_product_1971():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم الحليب لليدين من يوكو 50 مل (Yoko Milk Hand Cream - 50 ml)</strong> كريم اليدين الفاخر والمغذي ببروتينات الحليب الصافية من يوكو التايلاندية المصمم خصيصاً لتنعيم وترطيب وتفتيح بشرة اليدين والأظافر. يرتكز هذا الكريم الأصيل (Yoko Milk Hand Cream 50ml) على بروتينات الحليب الطبيعية (Pure Milk Protein)، الفيتامينات E و B3، والزيوت المرطبة الملطفة للبشرة.</p>
<p>يعمل كريم يوكو بالحليب لليدين على التخلص التام من خشونة وتجاعيد اليدين، تفتيح التصبغات والبقع الداكنة على ظهر اليدين، وتقوية الأظافر والجلد المحيط بها، ليترك يديك ناعمتين كالحرير، مرطبتين، ناصعتي التبييض، ومعطرتين بعطر الحليب الناعم الدافيء طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تغذية وتنعيم فائق ببروتينات الحليب الصافية:</strong> تعيد المرونة والنعومة الحريرية لليدين.</li>
  <li><strong>تفتيح وتوحيد لون اليدين بفيتامين B3:</strong> يقلل التصبغات والبقع الداكنة الناتجة عن الشمس والتنظيف.</li>
  <li><strong>تقوية الأظافر والعناية بالجلد المحيط:</strong> يقوي صحة الأظافر ويمنع التكسر والتقشر.</li>
  <li><strong>ترطيب عميق وسريع الامتصاص دون لزوجة:</strong> ينفذ للجلد دون ترك ملمس دهني ثقيل.</li>
  <li><strong>جودة يوكو (Yoko) التايلاندية الشهيرة:</strong> علامة ممتازة وخاصة في مستحضرات بروتينات الحليب.</li>
  <li><strong>أنبوب أنيق سعة 50 مل:</strong> حجم مدمج مثالي لحقيبة اليد والعناية المستمرة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسية من كريم يوكو بالحليب على اليدين والأظافر بعد غسل اليدين أو الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي اليدين والأظافر برفق بحركات دائرية حتى الامتصاص الكامل (يُستعمل عدة مرات يومياً وقبل النوم).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>بروتينات الحليب الصافية وفيتامين E:</strong> تغذيان طبقات جلد اليدين وتمنحان نعومة حريرية فائقة.</li>
  <li><strong>فيتامين B3 والزيوت المرطبة:</strong> يفتحان التصبغات ويحفظان الترطيب الداخلي للبشرة والأظافر.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة اليدين والأظافر فقط.</li>
  <li>تجنبي التلامس مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن كريم يوكو بالحليب 50 مل لتنعيم وتفتيح اليدين وتقوية الأظافر.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>يوكو (Yoko)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات اليدين والأظافر ببروتينات الحليب من يوكو 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>كريم مغذٍ ومفتّح لليدين والأظافر ببروتينات الحليب والفيتامينات (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة اليدين (الجافة، الخشنة والمتصبغة)</td></tr>
  <tr><th>المظهر النهائي</th><td>يدان ناعمتان كالحرير، ناصعتا التبييض، موحدتا اللون وأظافر قوية</td></tr>
  <tr><th>الملمس</th><td>كريم ناعم خفيف سريع الامتصاص دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر الحليب الناعم الأنيق دافئ</td></tr>
  <tr><th>المكونات النشطة</th><td>بروتينات حليب صافية، فيتامين B3، فيتامين E، زيوت مرطبة</td></tr>
  <tr><th>بلد المنشأ</th><td>تايلاند (Thailand)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Siam Yoko Co., Ltd. Thailand</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد بروتينات الحليب وفيتامين B3 في كريم يوكو لليدين (Yoko Milk)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم يوكو بالحليب مشكلة خشونة اليدين، التسمر والتصبغات الناتجة عن الشمس والمنظفات، وضعف وتكسر الأظافر.</p>

<h3>لماذا تنجح تركيبة بروتينات الحليب وB3؟</h3>
<p>لأن حمض اللاكتيك والببتيدات في بروتينات الحليب تجدد خلايا اليدين بينما يثبط النياسيناميد (B3) التصبغات الداكنة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق بعد كل غسل لليدين:</strong> يعوض الزيوت المفقودة بفعل الصابون فورياً.<br>
2. <strong>تدليك الأظافر والجلد المحيط بها:</strong> يقوي بنية الكيراتين ويمنع التقشر.<br>
3. <strong>التطبيق المسائي قبل النوم:</strong> يضمن أقصى امتصاص وتغذية حريرية طوال الليل.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات اليدين بالحليب تترك أثراً لزجاً على الأدوات والأجهزة."<br>
<strong>الحقيقة:</strong> كريم يوكو بالحليب مصمم بتقنية امتصاص متقدمة تنفذ للجلد دون ترك لزوجة أو أثر دهني على الشاشات.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تغذي الأحماض الأمينية الكازينية خلايا البشرة وتدعم تخليق الكولاجين، بينما يمنع فيتامين E أكسدة الليبيدات الجلدية.</p>"""

    faqs = [
        ("ما هو كريم الحليب لليدين من يوكو 50 مل؟", "هو كريم مغذٍ ومفتّح لليدين والأظافر من يوكو التايلاندية ببروتينات الحليب الصافية والفيتامينات (50 مل)."),
        ("ما هي فوائد بروتينات الحليب وفيتامين B3 و E؟", "تغذي بروتينات الحليب الجلد وتمنحه نعومة حريرية، يفتح فيتامين B3 التصبغات، ويقوي فيتامين E الأظافر."),
        ("هل ينعم اليدين الخشنة ويفتح التصبغات؟", "نعم، مثبت سريرياً في تنعيم اليدين وتفتيح البقع الداكنة على ظهر اليدين بفاعلية."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنبوب سعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على اليدين والأظافر بعد الغسل ودلكي بحركات دائرية حتى الامتصاص عدة مرات يومياً وقبل النوم."),
        ("هل هو خالٍ من اللزوجة والدهنية؟", "نعم، قوام ناعم سريع الامتصاص دون لزوجة دهنية ثقيلة."),
        ("أين صُنع كريم يوكو بالحليب؟", "صُنع في تايلاند بواسطة Siam Yoko Co., Ltd."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات يوكو لدى إكليل أبها أصلية 100%."),
        ("ما رائحة كريم يوكو بالحليب؟", "عطر الحليب الناعم الدافيء الأنيق المحبب."),
        ("هل يقوي الأظافر والعناية بالجلد المحيط؟", "نعم، يغذي الأظافر ويمنع تكسرها وتقشر الجلد حولها."),
        ("هل أنبوب 50 مل مناسب لحقيبة اليد؟", "نعم، حجم مدمج أنيق مثالي لحقيبة اليد والسفر والعمل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب جميع أنواع بشرة اليدين؟", "نعم، مناسب للبشرة العادية، الجافة، الخشنة والمتصبغة."),
        ("كم مرة يومياً؟", "عدة مرات يومياً وخاصة بعد غسل اليدين وقبل النوم."),
        ("هل يوكو علامة تايلاندية معتمدة؟", "نعم، Yoko علامة رائدة ومشهورة جداً في تايلاند وآسيا لمنتجات بروتينات الحليب."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يحمي اليدين من المنظفات والماء؟", "نعم، يعوض المرطبات المفقودة ويشكل حماية لطيفة."),
        ("هل يمنح اليدين ملمساً ناعماً كالحرير؟", "نعم، يمنح اليدين ملمساً حريرياً ناعماً جداً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يجف سريعاً دون ترك أثر على الشاشات؟", "نعم، يمتص بسلاسة دون أثر دهني على أجهزة اللمس."),
        ("هل يصلح هدية لطيفة؟", "نعم، هدية أنيقة وعملية ومفيدة جداً لكل امرأة."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يناسب الاستخدام اليومي المستمر؟", "نعم، مصمم للاستخدام اليومي المستمر لحماية اليدين."),
        ("هل يمنح اليدين مظهراً حيوياً ومشرقاً؟", "نعم، يعيد الحيوية والإشراقة لليدين الباهتتين."),
        ("هل يمتص بسهولة؟", "نعم، يمتص بسلاسة مدهشة.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Yoko Milk Hand Cream - 50 ml</strong> is a luxury nourishing hand and nail cream infused with pure milk proteins from Yoko Thailand designed to soften, hydrate, brighten, and care for hand skin and nails. Formulated with Pure Milk Protein, Vitamins E & B3, and soothing moisturizing oils.</p>
<p>Yoko Milk Hand Cream completely eliminates hand roughness and fine lines, lightens hyperpigmentation and dark spots on the backs of hands, and strengthens nails and cuticles, leaving your hands touchably silky soft, deeply hydrated, visibly brightened, and fragranced with a sweet soft milk scent all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Superior Nourishment & Softening with Pure Milk Protein:</strong> Restores elasticity and silky smoothness to hands.</li>
  <li><strong>Hand Skin Brightening & Tone Unification with Vitamin B3:</strong> Reduces dark spots and sun/detergent discoloration.</li>
  <li><strong>Nail Strengthening & Cuticle Care:</strong> Enhances nail health preventing breakage and peeling cuticles.</li>
  <li><strong>Deep Fast-Absorbing Hydration Without Greasiness:</strong> Penetrates skin layers without a heavy greasy feel.</li>
  <li><strong>Renowned Quality of Yoko Thailand:</strong> Premier Asian brand specialized in milk protein cosmetics.</li>
  <li><strong>Sleek 50ml Tube Container:</strong> Compact volume perfect for handbag, work desk, and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of Yoko Milk Hand Cream onto hands and nails post-wash or shower.</li>
  <li><strong>Step 2:</strong> Massage hands, fingers, and cuticles gently in circular motions until completely absorbed (use multiple times daily & bedtime).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Milk Protein & Vitamin E:</strong> Nourish hand skin layers and impart extreme silky softness.</li>
  <li><strong>Vitamin B3 & Moisturizing Oils:</strong> Brighten dark spots and preserve internal skin and nail hydration.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hand and nail skin application only.</li>
  <li>Avoid contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Every woman seeking Yoko Milk Hand Cream 50ml for hand softening, brightening, and nail strengthening.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Yoko</td></tr>
  <tr><th>Category</th><td>Skincare / Yoko Milk Protein Hand & Nail Creams 50ml</td></tr>
  <tr><th>Product Type</th><td>Milk Protein & Vitamin B3 Nourishing Hand & Nail Brightening Cream (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hand Skin Types (Dry, Rough & Hyperpigmented Hands)</td></tr>
  <tr><th>Finish</th><td>Silky soft, brightened, even-toned hands with strong healthy nails</td></tr>
  <tr><th>Texture</th><td>Lightweight smooth fast-absorbing cream without stickiness</td></tr>
  <tr><th>Fragrance</th><td>Gentle sweet elegant milk fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Pure Milk Protein, Vitamin B3 (Niacinamide), Vitamin E, Hydrating Oils</td></tr>
  <tr><th>Country of Origin</th><td>Thailand</td></tr>
  <tr><th>Manufacturer</th><td>Siam Yoko Co., Ltd. Thailand</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Milk Protein Lactic Acid Exfoliation & Niacinamide Hand Brightening</h2>

<h3>What problem does this solve?</h3>
<p>Yoko Milk Hand Cream resolves rough dry hands, dark spots on backs of hands, and brittle peeling nails/cuticles.</p>

<h3>Why choose Yoko Milk Hand Cream?</h3>
<p>Milk protein amino acids and natural lactic peptides gently renew hand skin while Niacinamide (B3) suppresses dark melanin transfer.</p>"""

    en_faqs = [
        ("What is Yoko Milk Hand Cream - 50 ml?", "It is a nourishing hand and nail brightening cream from Yoko Thailand with pure milk proteins and vitamins (50ml)."),
        ("What are the benefits of pure milk proteins and vitamins B3 & E?", "Milk proteins nourish and soften skin, Vitamin B3 brightens dark spots, and Vitamin E strengthens nails."),
        ("Does it soften rough hands and brighten dark spots?", "Yes, clinically proven to soften hands and lighten dark spots on backs of hands effectively."),
        ("What volume is contained in this tube?", "50ml tube."),
        ("How do I use it correctly?", "Apply on hands and nails post-wash, massage in circular motions until absorbed multiple times daily."),
        ("Is it non-greasy and non-sticky?", "Yes, smooth lightweight formula absorbs quickly without greasy residue."),
        ("Where is Yoko Milk Hand Cream manufactured?", "In Thailand by Siam Yoko Co., Ltd."),
        ("How do I verify authenticity at Ekleel Abha?", "All Yoko products at Ekleel Abha are 100% original."),
        ("What scent does Yoko Milk Hand Cream have?", "Gentle sweet elegant comforting milk aroma."),
        ("Does it strengthen nails and care for cuticles?", "Yes, nourishes nails preventing breakage and soothing cuticles."),
        ("Is the 50ml tube handbag friendly?", "Yes, compact sleek size perfect for handbag, work desk, and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for all hand skin types?", "Yes, suitable for normal, dry, rough, and hyperpigmented hand skin."),
        ("How many times daily?", "Multiple times daily especially post-wash and bedtime."),
        ("Is Yoko a trusted Thai brand?", "Yes, Yoko is a premier famous Asian brand in milk protein skincare."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it protect hands against detergents and water?", "Yes, replenishes lost moisture forming a gentle barrier."),
        ("Does it leave hands silky soft?", "Yes, imparts an extremely soft silky feel to hands."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it absorb without leaving fingerprints on screens?", "Yes, absorbs smoothly without greasy marks on touchscreens."),
        ("Is it a nice practical gift?", "Yes, elegant practical gift for any woman."),
        ("Is it suitable for men and women?", "Yes, great for both men and women."),
        ("Is it safe for daily continuous use?", "Yes, safe for continuous daily use to protect hands."),
        ("Does it impart vibrant youthful hand appearance?", "Yes, restores vibrant radiance to dull hands."),
        ("Does it absorb easily?", "Yes, absorbs remarkably fast.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1971",
        "sku": "EK-1971",
        "gtin": "8853976004617",
        "brand": "Yoko",
        "ar": {
            "title": "كريم الحليب لليدين من يوكو  50 مل",
            "meta_title": "كريم الحليب لليدين يوكو 50مل | إكليل أبها",
            "meta_description": "اشتري كريم الحليب لليدين والأظافر من يوكو (50 مل). كريم تايلاندي ببروتينات الحليب لتنعيم وتفتيح اليدين وتقوية الأظافر. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["يوكو", "كريم_الحليب_لليون", "تنعيم_اليدين", "تقوية_الأظافر", "إكليل_أبها"]
        },
        "en": {
            "title": "Yoko Milk Hand Cream - 50 ml",
            "meta_title": "Yoko Milk Hand Cream 50ml | Ekleel Abha",
            "meta_description": "Buy original Yoko Milk Hand Cream (50ml). Thai pure milk protein & vitamin B3 hand brightening & nail cream. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["yoko", "milk_hand_cream", "hand_brightening", "nail_care", "ekleel_abha"]
        }
    }


def create_product_1972():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم سوفت للترطيب والانتعاش من نيفيا 75 مل (Nivea Soft Moisturizing and Refreshing Cream - 75ml)</strong> كريم الترطيب الخفيف اليومي الأكثر شهرة عالمياً من نيفيا الألمانية المصمم لمنح بشرة الوجه والجسم واليدين ترطيباً وانتعاشاً فورياً دون أي دهنية. يرتكز هذا الكريم الأصيل (Nivea Soft Refreshing Cream 75ml) على زيت الجوجوبا المغذي (Jojoba Oil)، فيتامين E المضاد للأكسدة، والمركبات المائية المنعشة.</p>
<p>يعمل كريم نيفيا سوفت على اختراق طبقات الجلد بسرعة فائقة، إمداد البشرة بجرعة مكثفة من الانتعاش والترطيب 24 ساعة، تنعيم البشرة الجافة والباهتة، وتوفير العناية اليومية المتكاملة للوجه واليدين والجسم، ليترك بشرتك ناعمة كالحرير، منتعشة، خافقة بالحيوية، وغير لامعة بالدهون.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب عميق وانتعاش فوري 24 ساعة بزيت الجوجوبا وفيتامين E:</strong> يغذي البشرة ويمنع الجفاف.</li>
  <li><strong>تركيبة فائقة الخفة سريعة الامتصاص دون لزوجة:</strong> تنفذ للجلد فورياً دون ترك أثر دهني ثقيل.</li>
  <li><strong>مناسب للوجه واليدين والجسم 3 في 1:</strong> كريم العناية الشاملة لجميع أفراد الأسرة.</li>
  <li><strong>عطر نيفيا سوفت المنعش الأيقوني:</strong> يمنح البشرة رائحة النظافة والنضارة طوال اليوم.</li>
  <li><strong>اختبر جلدياً لحماية وسلامة البشرة:</strong> لطيف ومناسب لجميع أنواع البشرة.</li>
  <li><strong>عبوة أنيقة سعة 75 مل:</strong> حجم مدمج مثالي لحقيبة اليد والسفر والعناية اليومية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسبة من كريم نيفيا سوفت على بشرة الوجه أو اليدين أو الجسم النظيفة.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي برفق بحركات دائرية ناعمة حتى الامتصاص الكامل (يُستعمل يومياً صباحاً ومساءً وعند الحاجة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الجوجوبا الطبيعي:</strong> يطابق الشحوم الطبيعية للبشرة ويغذيها عمقاً.</li>
  <li><strong>فيتامين E والمركبات المائية:</strong> يحميان البشرة من الجذور الحرة ويمدانها بانتعاش مائي مستمر.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه واليدين والجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن كريم نيفيا سوفت 75 مل للترطيب اليومي الفائق والانتعاش الخفيف للوجه والجسم.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>نيفيا (NIVEA)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات نيفيا سوفت للترطيب والانتعاش 75ml</td></tr>
  <tr><th>نوع المنتج</th><td>كريم ترطيب خفيف للوجه واليدين والجسم بزيت الجوجوبا وفيتامين E (75ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>75 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (العادية، الجافة، الدهنية والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة كالحرير، مرطبة عمقاً، منتعشة وخالية من اللزوجة الدهنية</td></tr>
  <tr><th>الملمس</th><td>كريم خفيف جداً سريع الامتصاص يشبه اللوشن الناعم</td></tr>
  <tr><th>العطر</th><td>عطر نيفيا سوفت المنعش الأيقوني الناعم</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت الجوجوبا الطبيعي، فيتامين E، مركبات ترطيب مائية</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا (Germany)</td></tr>
  <tr><th>الشركة المصنعة</th><td>NIVEA (Beiersdorf Germany)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 6 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت الجوجوبا وفيتامين E في كريم نيفيا سوفت (Nivea Soft)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم نيفيا سوفت مشكلة جفاف البشرة اليومي، ثقل الكريمات التقليدية الدهنية، والحاجة لمرطب خفيف وشامل للوجه واليدين والجسم.</p>

<h3>لماذا تنجح تقنية نيفيا سوفت؟</h3>
<p>لأن جزيئات زيت الجوجوبا تطابق الشحوم البشرية في المستحلب المائي الخفيف، فيمتصها الجلد فورياً دون إغلاق المسام.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق اليومي بعد الاستحمام والغسل:</strong> يحفظ أقصى كمية من الماء الداخلي.<br>
2. <strong>الاستخدام كقاعدة قبل المكياج:</strong> يهيئ الوجه ويضمن ثبات المكياج بسلاسة.<br>
3. <strong>الاستخدام الشامل:</strong> حيد ممتاز لليدين والوجه والجسم في منتج واحد.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الكريمات الخفيفة مثل نيفيا سوفت لا تمنح ترطيباً عميقاً."<br>
<strong>الحقيقة:</strong> نيفيا سوفت يمنح ترطيباً عميقاً يستمر لـ 24 ساعة بفضل امتصاص الجوجوبا السريع لعمق الخلايا.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>ينتشر المستحلب المائي الزيتي (Oil-in-Water Emulsion) في البشرة محرراً جزيئات الماء الميكروية فورياً للتغلغل في الطبقة القرنبة.</p>"""

    faqs = [
        ("ما هو كريم سوفت للترطيب والانتعاش من نيفيا 75 مل؟", "هو كريم ترطيب خفيف يومي 3 في 1 للوجه واليدين والجسم من نيفيا الألمانية بزيت الجوجوبا وفيتامين E (75 مل)."),
        ("ما هي فوائد زيت الجوجوبا وفيتامين E؟", "يغذي زيت الجوجوبا البشرة عمقاً، ويحمي فيتامين E من الأكسدة، ويمنحان ترطيباً وانتعاشاً لـ 24 ساعة."),
        ("هل يمتص بسرعة دون ترك ملمس دهني؟", "نعم، تركيبة فائقة الخفة تنفذ للجلد فورياً دون ترك لزوجة أو أثر دهني."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنيقة بسعة 75 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على بشرة الوجه أو اليدين أو الجسم النظيفة ودلكي برفق حتى الامتصاص يومياً عند الحاجة."),
        ("هل يناسب الوجه واليدين والجسم معاً؟", "نعم، كريم العناية الشاملة 3 في 1 للوجه واليدين والجسم."),
        ("أين صُنع كريم نيفيا سوفت؟", "صُنع في ألمانيا بواسطة Beiersdorf Germany."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات نيفيا لدى إكليل أبها أصلية 100%."),
        ("ما رائحة كريم نيفيا سوفت؟", "عطر نيفيا سوفت المنعش الأيقوني الناعم."),
        ("هل يصلح كقاعدة ممتازة قبل المكياج؟", "نعم، قاعدة ممتازة جداً قبل المكياج بفضل امطصاطه السريع وخفته."),
        ("هل 75 مل مناسبة للحقيبة والسفر؟", "نعم، حجم مدمج أنيق مثالي لحقيبة اليد والسفر والتنقل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب البشرة الدهنية والمختلطة؟", "نعم، مناسب لجميع أنواع البشرة بفضل خفته وزيت الجوجوبا المتوازن."),
        ("كم مرة يومياً؟", "صباحاً ومساءً وعند الحاجة."),
        ("هل نيفيا سوفت الماركة الأولى عالمياً في الترطيب الخفيف؟", "نعم، Nivea Soft أكثر كريم ترطيب خفيف شهيرة ومحبوبة عالمياً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب جميع أفراد الأسرة؟", "نعم، مناسب للرجال والنساء والأطفال من 6 سنوات."),
        ("هل يحمي من جفاف الشتاء والصيف؟", "نعم، ممتاز للانتعاش والترطيب في جميع الفصول."),
        ("هل يمنح البشرة ملمساً ناعماً كالحرير؟", "نعم، يمنح البشرة ملمساً حريرياً ناعماً جداً من الاستخدام الأول."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يسبب انسداد المسام؟", "لا، تركيبة خفيفة غير مسببة للانسداد (Non-Comedogenic)."),
        ("هل يتوفر بأحجام أخرى لدى نيفيا؟", "نعم، يتوفر بأحجام متعددة لدى نيفيا."),
        ("هل يصلح هدية ممتازة؟", "نعم، هدية عملية ومحبوبة جداً في كل بيت."),
        ("هل يغني عن كريمات متعددة؟", "نعم، مرطب 3 في 1 يختصر الروتين اليومي."),
        ("هل تظهر نتائج الانتعاش فورية؟", "نعم، انطباع الانتعاش والترطيب فوري بمجرد التطبيق.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Nivea Soft Moisturizing and Refreshing Cream - 75ml</strong> is the world's most famous daily lightweight moisturizing cream from Nivea Germany designed to impart instant hydration and freshness to face, body, and hands without any greasiness. Formulated with nourishing Jojoba Oil, antioxidant Vitamin E, and refreshing hydrators.</p>
<p>Nivea Soft Cream penetrates skin layers rapidly, delivers a concentrated 24-hour dose of moisture and freshness, softens dry dull skin, and provides comprehensive 3-in-1 daily care for face, hands, and body, leaving your skin touchably silky soft, refreshed, vibrant, and non-greasy.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Deep 24-Hour Hydration & Instant Refreshment with Jojoba Oil & Vitamin E:</strong> Nourishes skin and guards against dryness.</li>
  <li><strong>Ultra-Lightweight Fast-Absorbing Non-Greasy Formula:</strong> Penetrates skin instantly without heavy residue.</li>
  <li><strong>3-in-1 Versatile Care for Face, Hands & Body:</strong> All-in-one daily care for the whole family.</li>
  <li><strong>Iconic Fresh Nivea Soft Fragrance:</strong> Coats skin in a soft clean refreshing aura all day.</li>
  <li><strong>Dermatologically Tested:</strong> Gentle and suitable for all skin types.</li>
  <li><strong>Sleek 75ml Tub Container:</strong> Compact volume ideal for handbag, travel, and daily care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of Nivea Soft Cream onto clean skin of face, hands, or body.</li>
  <li><strong>Step 2:</strong> Massage gently in smooth circular motions until completely absorbed (use daily morning, night, and as needed).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Jojoba Oil:</strong> Mimics natural skin lipids and deeply nourishes.</li>
  <li><strong>Vitamin E & Hydrating Agents:</strong> Protect skin from free radicals while supplying continuous aqua refreshment.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial, hand, and body skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Nivea Soft 75ml Cream for daily lightweight 3-in-1 facial, hand, and body hydration.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>NIVEA</td></tr>
  <tr><th>Category</th><td>Skincare / Nivea Soft Refreshing Creams 75ml</td></tr>
  <tr><th>Product Type</th><td>3-in-1 Lightweight Jojoba & Vitamin E Moisturizing & Refreshing Cream (75ml)</td></tr>
  <tr><th>Volume/Weight</th><td>75 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Normal, Dry, Oily & Combination)</td></tr>
  <tr><th>Finish</th><td>Silky soft, deeply hydrated, refreshed & non-greasy skin</td></tr>
  <tr><th>Texture</th><td>Ultra-lightweight fast-absorbing smooth cream fluid</td></tr>
  <tr><th>Fragrance</th><td>Iconic soft refreshing Nivea Soft fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Jojoba Oil, Vitamin E, Aqua Hydrating Compounds</td></tr>
  <tr><th>Country of Origin</th><td>Germany</td></tr>
  <tr><th>Manufacturer</th><td>NIVEA (Beiersdorf Germany)</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 6+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Oil-in-Water Emulsion Rapid Absorption & Jojoba Sebum Mimicry</h2>

<h3>What problem does this solve?</h3>
<p>Nivea Soft Cream resolves daily skin dryness, heavy greasy cream discomfort, and the need for a versatile 3-in-1 face, hand, and body moisturizer.</p>

<h3>Why choose Nivea Soft Cream?</h3>
<p>Jojoba Oil esters mimic natural skin sebum within a lightweight Oil-in-Water emulsion, penetrating skin instantly without clogging pores.</p>"""

    en_faqs = [
        ("What is Nivea Soft Moisturizing and Refreshing Cream - 75ml?", "It is a world-famous daily lightweight 3-in-1 moisturizing cream for face, hands, and body from Nivea Germany with Jojoba Oil and Vitamin E (75ml)."),
        ("What are the benefits of Jojoba Oil and Vitamin E?", "Jojoba Oil deeply nourishes skin, Vitamin E protects against oxidation, and together they deliver 24-hour hydration."),
        ("Does it absorb quickly without greasy residue?", "Yes, ultra-lightweight formula penetrates skin instantly without greasiness or stickiness."),
        ("What volume is contained in this tub?", "75ml tub container."),
        ("How do I use it correctly?", "Apply on clean face, hand, or body skin, massage gently until absorbed daily as needed."),
        ("Is it suitable for face, hands, and body together?", "Yes, versatile 3-in-1 daily moisturizer for face, hands, and body."),
        ("Where is Nivea Soft manufactured?", "In Germany by Beiersdorf Germany."),
        ("How do I verify authenticity at Ekleel Abha?", "All Nivea products at Ekleel Abha are 100% original."),
        ("What scent does Nivea Soft have?", "Iconic fresh soft Nivea Soft signature fragrance."),
        ("Does it serve as a good makeup base?", "Yes, excellent makeup base due to lightweight fast absorption."),
        ("Is the 75ml tub handbag friendly?", "Yes, sleek compact size ideal for handbag, travel, and on-the-go care."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for oily and combination skin?", "Yes, suitable for all skin types due to lightweight balanced Jojoba formula."),
        ("How many times daily?", "Morning, night, and whenever needed."),
        ("Is Nivea Soft a global #1 lightweight moisturizer?", "Yes, Nivea Soft is the world's most recognized lightweight moisturizer."),
        ("Is the container recyclable?", "Yes."),
        ("Is it suitable for the whole family?", "Yes, suitable for men, women, and children aged 6+."),
        ("Does it protect against summer and winter dryness?", "Yes, excellent for hydration and freshness in all seasons."),
        ("Does it leave skin silky soft?", "Yes, imparts an extremely soft silky feel from first application."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it clog pores?", "No, lightweight non-comedogenic formula."),
        ("Are other sizes available?", "Yes, Nivea Soft comes in multiple tub sizes."),
        ("Is it a great gift?", "Yes, practical and universally beloved gift."),
        ("Does it replace multiple creams?", "Yes, 3-in-1 moisturizer simplifies daily routines."),
        ("Are refreshing results instant?", "Yes, instant hydration and refreshing feel upon application.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1972",
        "sku": "EK-1972",
        "gtin": "4005900008985",
        "brand": "NIVEA",
        "ar": {
            "title": "كريم سوفت للترطيب والانتعاش من نيفيا 75 مل",
            "meta_title": "كريم نيفيا سوفت للترطيب 75مل | إكليل أبها",
            "meta_description": "اشتري كريم نيفيا سوفت للترطيب والانتعاش (75 مل). كريم ألماني خفيف 3 في 1 للوجه واليدين والجسم بزيت الجوجوبا وفيتامين E. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["نيفيا", "نيفيا_سوفت", "كريم_ترطيب_خفيف", "زيت_الجوجوبا", "إكليل_أبها"]
        },
        "en": {
            "title": "Nivea Soft Moisturizing and Refreshing Cream - 75ml",
            "meta_title": "Nivea Soft Moisturizing Cream 75ml | Ekleel Abha",
            "meta_description": "Buy original Nivea Soft Moisturizing and Refreshing Cream (75ml). 3-in-1 German lightweight Jojoba & Vitamin E cream. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["nivea", "nivea_soft", "moisturizing_cream", "jojoba_oil", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 51 builders complete")
