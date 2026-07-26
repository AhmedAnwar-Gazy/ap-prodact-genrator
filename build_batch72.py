import json, os

def create_product_2076():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مزيل عرق اورجينال من دوف 50 مل (Dove Original Deodorant Roll-On - 50ml)</strong> رول أون حماية ومحيط الإبطين العطري الطبي الفاخر الأكثر توصية من دوف (Dove) المصمم خصيصاً لتوفير حماية جافة ضد التعرق والروائح تدوم لـ 48 ساعة مع ترطيب وتنعيم وتفتيح منطقة أسفل الذراعين. يرتكز هذا المزيل الأصيل (Dove Original Roll-on 50ml) على كريم المرطب الشهير (1/4 Moisturizing Cream)، الزيوت العطرية النظيفة، والتركيبة الخالية 100% من الكحول بروبانول.</p>
<p>يعمل رول أون دوف أوريجينال على تهدئة تهيجات الإبط الناتجة عن الحلاقة، حفظ طراوة الجلد، ومنع إفرازات التعرق المسببة للروائح، ليترك منطقة الإبطين ناعمة كالحرير، مرطبة، خالية من الاسمرار، ومفعمة برائحة النظافة الانتعاشية الأصيلة من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية ممتدة ضد التعرق والروائح لـ 48 ساعة:</strong> يوفر جفافاً ونظافة وثقة كاملة طوال اليوم.</li>
  <li><strong>ترطيب وتنعيم فائق بنسبة 1/4 كريم مرطب:</strong> يعالج الجفاف والخشونة أسفل الذراعين.</li>
  <li><strong>تهدئة تامة لتهيج الحلاقة والشمع:</strong> يقلل احمرار واحتقان بشرة الإبطين.</li>
  <li><strong>تركيبة خالية 100% من الكحول بروبانول:</strong> لا تسبب أي اسمرار أو حرقان بالجلد.</li>
  <li><strong>عطر دوف الكلاسيكي الناعم الأيقوني:</strong> يغلف المنطقة برائحة النظافة الأصيلة.</li>
  <li><strong>عبوة رول أون مدمجة سعة 50 مل:</strong> تصميم انسيابي مريح جداً للحقيبة والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> نظفي ورجّفي بشرة الإبطين جيداً بعد الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> مرري كرة الرول أون برفق 2-3 مرات على بشرة الإبطين.</li>
  <li><strong>الخطوة الثالثة:</strong> دعي السائل يجف ثوانٍ معدودة قبل ارتداء الملابس (يُستعمل يومياً بعد الاستحمام).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>1/4 كريم مرطب (Quarter Moisturizing Cream):</strong> يغذي جلد الإبطين ويمنع التغضن والخشونة.</li>
  <li><strong>أملاح الألومنيوم الخفيفة والمركبات المعطرة:</strong> تسيطر على التعرق وتمنح عطراً نظيفاً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الإبطين فقط.</li>
  <li>لا يُستخدم على الجلد المتهيج أو المجروح فوراً بعد الحلاقة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن مزيل عرق دوف أوريجينال 50 مل للحماية 48 ساعة ونعومة كريمية فائقة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>دوف (Dove)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / مزيلات ومضادات التعرق رول أون من دوف 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>رول أون مضاد للتعرق بـ 1/4 كريم مرطب لـ 48 ساعة (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الإبطين (مناسب للبشرة الحساسة وبعد الحلاقة)</td></tr>
  <tr><th>المظهر النهائي</th><td>إبطين ناعمين كالحرير، جافين، معطرين بالنظافة وخاليين من البقع والاسمرار</td></tr>
  <tr><th>الملمس</th><td>سائل كريمي لطيف خفيف يجف سريعاً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر دوف الكلاسيكي الأصلي النظيف الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>1/4 كريم مرطب، أملاح مضادة للتعرق، زيت دوار الشمس</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة المتحدة / ألمانيا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever Group</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد 1/4 كريم مرطب في رول أون دوف (Dove Original Roll-On)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج رول أون دوف أوريجينال مشكلة رائحة التعرق الزائدة، اسمرار وخشونة الإبطين، والتهيج الناتج عن الحلاقة.</p>

<h3>لماذا تنجح تركيبة Dove 1/4 Moisturizing Cream؟</h3>
<p>لأن السائل المزود بـ 1/4 كريم مرطب يعيد بناء الحجاب الهيدروليبيدي للجلد ويمنع فقدان الماء أثناء منع عرق الإبط.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على بشرة نظيفة وجافة تماماً:</strong> يضمن أقصى أداء لمضاد التعرق.<br>
2. <strong>ترك السائل يجف ثوانٍ قبل ارتداء الملابس:</strong> يمنع بقع الملابس البيضاء.<br>
3. <strong>الاستخدام المنتظم يومياً بعد الاستحمام:</strong> يحافظ على نعومة وحماية الإبطين.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مزيلات العرق تسبب دائماً اسمرار الإبطين."<br>
<strong>الحقيقة:</strong> رول أون دوف خالي 100% من الكحول ومدعم بكريم مرطب يمنع الاسمرار ويفتح المنطقة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تشكل أملاح مضاد التعرق سدادة ميكروسكوبية مؤقتة بقنوات العرق بينما يغذي كريم دوف خلايا الجلد.</p>"""

    faqs = [
        ("ما هو مزيل عرق اورجينال من دوف 50 مل؟", "هو رول أون مضاد للتعرق بـ 1/4 كريم مرطب من دوف يمنح حماية 48 ساعة ونعومة كريمية (50 مل)."),
        ("ما هي فوائد 1/4 كريم مرطب والتركيبة الخالية من الكحول؟", "يغذي بشرة الإبطين، يعالج خشونة الحلاقة، يمنع الاسمرار، ويمنح جفافاً 48 ساعة."),
        ("هل يحمي من رائحة العرق 48 ساعة ويرطب الإبطين؟", "نعم، مثبت سريرياً في حماية 48 ساعة وتوفير نعومة وترطيب حريري للإبطين."),
        ("ما حجم العبوة؟", "تأتي بعبوة رول أون أنيقة سعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "مرري الكرة 2-3 مرات على بشرة إبطين نظيفة وجافة بعد الاستحمام ودعيه يجف ثوانٍ."),
        ("هل هو خالٍ من الكحول؟", "نعم، 100% خالٍ من الكحول بروبانول ومختبر درماتولوجياً."),
        ("أين صُنع رول أون دوف؟", "صُنع بواسطة مجموعة Unilever العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات دوف لدى إكليل أبها أصلية 100%."),
        ("ما رائحة رول أون دوف أوريجينال؟", "عطر دوف الكلاسيكي النظيف الأصلي الأيقوني."),
        ("هل يمنع اسمرار بشرة الإبطين؟", "نعم، تركيبة المرطب تهدئ التهيج وتمنع اسمرار الجلد."),
        ("هل عبوة 50 مل مريحة للحقيبة والسفر؟", "نعم، تصميم انسيابي مدمج مثالي للحقيبة والسفر والتنقل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل دوف العلامة الأولى في العناية بالمرطبات؟", "نعم، Dove العلامة رقم 1 الأكثر شهرة عالمياً في العناية بالمرطبات ومزيلات التعرق."),
        ("كم مرة يومياً؟", "مرة واحدة يومياً بعد الاستحمام لـ 48 ساعة حماية."),
        ("هل يترك بقعاً على الملابس؟", "يجف سريعاً ولا يترك أي بقع إذا تم تركه يجف ثوانٍ قبل الارتداء."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يناسب البشرة الحساسة بعد الحلاقة؟", "نعم، لطيف جداً ويهدئ الاحمرار والتهيج الناتج عن الحلاقة والشمع."),
        ("هل يمنح شعوراً بالنظافة والانتعاش؟", "نعم، يمنح شعوراً متجدداً بالنظافة والأناقة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، يناسب الجميع وخاصة النساء بفضل عطر النظافة الناعم."),
        ("هل يناسب الشتاء والصيف؟", "نعم، حماية مثالية في الحر والدوام والتمارين."),
        ("هل يصلح هدية ممتازة ضمن العناية الشخصية؟", "نعم، منتج عناية كلاسيكي أساسي جداً."),
        ("هل يعيد المظهر الناعم السلس للإبطين؟", "نعم، يجعل الإبطين في غاية النعومة والجمال."),
        ("هل تتوفر روائح أخرى من رول أون دوف؟", "نعم، تتوفر عائلة Dove Roll-on كاملة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Dove Original Deodorant Roll-On - 50ml</strong> is the world's most dermatologist-recommended authentic luxury antiperspirant roll-on from Dove designed to provide 48-hour dry protection against sweat and body odor while hydrating, smoothing, and illuminating delicate underarm skin. Built upon Dove's famous 1/4 Moisturizing Cream, clean fragrant oils, and a 100% alcohol-free formula.</p>
<p>Dove Original Roll-On calms underarm shave irritation, locks in skin softness, and halts odor-causing sweat, leaving your underarms touchably silky soft, hydrated, clear of darkening, and fragranced with authentic clean scent from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>48-Hour Extended Antiperspirant & Odor Protection:</strong> Delivers daily dryness, clean freshness, and confidence.</li>
  <li><strong>Ultra-Moisturizing & Softening with 1/4 Moisturizing Cream:</strong> Treats dry rough underarm skin.</li>
  <li><strong>Shave & Wax Irritation Calming:</strong> Reduces underarm redness and razor burn.</li>
  <li><strong>100% Alcohol-Free Formula:</strong> Prevents skin stinging and darkening under arms.</li>
  <li><strong>Iconic Soft Classic Dove Clean Scent:</strong> Wraps underarms in authentic clean aroma.</li>
  <li><strong>Compact 50ml Ergonomic Roll-On:</strong> Sleek size ideal for handbag, gym, and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Cleanse and dry underarm skin thoroughly after shower.</li>
  <li><strong>Step 2:</strong> Roll the ball 2-3 times gently over underarm skin.</li>
  <li><strong>Step 3:</strong> Allow liquid to dry for a few seconds before dressing (use daily post-shower).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>1/4 Moisturizing Cream:</strong> Nourishes underarm skin preventing rough texture and dryness.</li>
  <li><strong>Mild Aluminum Salts & Clean Fragrance Compounds:</strong> Control sweat release while imparting fresh scent.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical underarm skin application only.</li>
  <li>Do not apply to broken or severely inflamed skin immediately after shaving.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Dove Original Roll-On 50ml for 48-hour antiperspirant protection and smooth creamy underarm care.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Dove</td></tr>
  <tr><th>Category</th><td>Personal Care / Dove Antiperspirant Roll-Ons 50ml</td></tr>
  <tr><th>Product Type</th><td>1/4 Moisturizing Cream 48-Hour Antiperspirant Roll-On (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Underarm Skin Types (Safe for Sensitive Skin & Post-Shave)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 48H dry, fragranced clean underarm skin without dark marks</td></tr>
  <tr><th>Texture</th><td>Smooth lightweight creamy liquid drying quickly</td></tr>
  <tr><th>Fragrance</th><td>Iconic classic clean original Dove scent</td></tr>
  <tr><th>Active Ingredients</th><td>1/4 Moisturizing Cream, Antiperspirant Salts, Sunflower Seed Oil</td></tr>
  <tr><th>Country of Origin</th><td>UK / Germany</td></tr>
  <tr><th>Manufacturer</th><td>Unilever Group</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 1/4 Moisturizing Cream Lipid Restoration & Antiperspirant Efficacy</h2>

<h3>What problem does this solve?</h3>
<p>Dove Original Roll-On resolves sweat odors, dark underarm pigmentation, rough skin texture, and razor burn.</p>

<h3>Why choose Dove Original Roll-On?</h3>
<p>The 1/4 Moisturizing Cream formula rebuilds the epidermal barrier preventing water loss while controlling sweat glands.</p>"""

    en_faqs = [
        ("What is Dove Original Deodorant Roll-On - 50ml?", "It is an antiperspirant roll-on with 1/4 moisturizing cream from Dove offering 48-hour protection and underarm softness (50ml)."),
        ("What are the benefits of 1/4 moisturizing cream and alcohol-free formula?", "Nourishes underarm skin, treats shaving roughness, prevents darkening, and delivers 48-hour dryness."),
        ("Does it protect against odor for 48 hours and moisturize underarms?", "Yes, clinically proven to protect against odor for 48 hours while moisturizing underarms."),
        ("What volume is contained in this roll-on?", "50ml sleek roll-on bottle."),
        ("How do I use it correctly?", "Roll 2-3 times over clean dry underarm skin after showering and let dry for seconds."),
        ("Is it alcohol-free?", "Yes, 100% ethanol-free and dermatologically tested."),
        ("Where is Dove Roll-On manufactured?", "By Unilever Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All Dove products at Ekleel Abha are 100% original."),
        ("What scent does Dove Original Roll-On have?", "Iconic classic soft clean original Dove fragrance."),
        ("Does it prevent underarm skin darkening?", "Yes, moisturizing formula calms shave irritation preventing underarm dark marks."),
        ("Is the 50ml bottle travel friendly?", "Yes, sleek ergonomic bottle ideal for handbag, gym, and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Dove the #1 moisturizing antiperspirant brand?", "Yes, Dove is the world's #1 recognized brand in moisturizing care and antiperspirants."),
        ("How many times daily?", "Once daily post-shower for 48-hour protection."),
        ("Does it leave marks on clothes?", "Dries quickly without leaving residue if allowed to dry for a few seconds."),
        ("Is the packaging recyclable?", "Yes."),
        ("Is it safe for sensitive skin post-shaving?", "Yes, ultra-gentle formula that calms redness and shave burn."),
        ("Does it deliver fresh clean confidence?", "Yes, provides continuous fresh clean feeling all day."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for everyone especially women preferring soft clean scents."),
        ("Is it good for all seasons?", "Yes, ideal protection for hot weather, gym, and daily work."),
        ("Is it a nice personal care gift?", "Yes, a classic personal care daily essential."),
        ("Does it restore smooth touchable underarms?", "Yes, leaves underarms touchably silky soft."),
        ("Are other Dove scents available?", "Yes, the full Dove Roll-on range is available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2076",
        "sku": "EK-2076",
        "gtin": "80466468",
        "brand": "Dove",
        "ar": {
            "title": "مزيل عرق اورجينال من دوف 50 مل",
            "meta_title": "رول أون دوف أوريجينال مضاد للتعرق 50مل | إكليل أبها",
            "meta_description": "اشتري مزيل عرق أوريجينال من دوف (50 مل). رول أون مضاد للتعرق بـ 1/4 كريم مرطب للحماية 48 ساعة ونعومة الإبطين. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["دوف", "مزيل_عرق_دوف", "رول_أون_أوريجينال", "حماية_48_ساعة", "إكليل_أبها"]
        },
        "en": {
            "title": "Dove Original Deodorant Roll-On - 50ml",
            "meta_title": "Dove Original Deodorant Roll-On 50ml | Ekleel Abha",
            "meta_description": "Buy original Dove Original Deodorant Roll-On (50ml). 1/4 moisturizing cream 48H antiperspirant roll-on. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["dove", "dove_roll_on", "dove_original_deodorant", "antiperspirant_50ml", "ekleel_abha"]
        }
    }


def create_product_2078():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>جوانتي قيادة اسود منقط (Black Polka Dot Driving Gloves)</strong> القفازات الصيفية الحامية الفاخرة الأنيقة المصممة خصيصاً لحماية بشرة اليدين والذراعين من أشعة الشمس الضارة وتجنب الاسمرار والتصبغات والبقع أثناء قيادة السيارة والتنقل اليومي. تركز هذه القفازات الأصيلة (Driving Gloves Black Polka Dot) على النسيج القطني المرن المسامي، النقش المنقط الفاخر (Polka Dot)، والسطح المقاوم للانزلاق لمسك دركسون السيارة بثبات وأمان.</p>
<p>تعمل جوانتي القيادة المنقطة على عزل أشعة الشمس فوق البنفسجية (UV Protection)، منع تعرق اليدين، وتوفير التهوية والراحة التامة للبشرة، لتترك يديك ناعمتين، محميتين من التسمير، ومفعمتين بالأناقة والراحة أثناء القيادة اليومية.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية فائقة من أشعة الشمس فوق البنفسجية (UV Protection):</strong> تمنع اسمرار وتصبغات اليدين أثناء القيادة.</li>
  <li><strong>تصميم أسود منقط (Polka Dot) أنيق وفخم:</strong> يمنح لمسة جمالية أنثوية وعصرية.</li>
  <li><strong>نسيج قطني مرن ومسامي خفيف:</strong> يضمن التهوية ومنع تعرق الكفين في الصيف.</li>
  <li><strong>طبقة مانعة للانزلاق لقابض السيارة:</strong> تحسن التحكم والسيطرة على مقود القيادة بثبات.</li>
  <li><strong>مقاس مريح ومرن يناسب جميع اليدين:</strong> سهل الارتداء والخلع دون ضغط.</li>
  <li><strong>قابلة للغسل وإعادة الاستخدام لسنوات:</strong> خامة قماشية متينة وعالية الجودة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ارتدي قفازات القيادة على اليدين قبل البدء بفرك عجلة قيادة السيارة.</li>
  <li><strong>الخطوة الثانية:</strong> تأكدي من ضبط الأصابع والانطباق المريح للكفين.</li>
  <li><strong>الخطوة الثالثة:</strong> اغسلي القفازات يدويًا بالماء والصابون عند الحاجة ودعيها تجف بالهواء.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>ألياف القطن والسباندكس المرنة:</strong> توفر نسيجاً مسامياً ينفس البشرة ويمتص الرطوبة.</li>
  <li><strong>نقاط النقش المطاطية المقاومة للانزلاق:</strong> تضمن ثبات المسكة على عجلة القيادة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي للحماية أثناء القيادة والخروج بالشمس.</li>
  <li>يُفضل الغسيل اليدوي بماء بارد لتجنب تلف النقاط المطاطية.</li>
  <li>يُحفظ في مكان بارد وجاف بعيداً عن النار المباشرة.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تسود السيارة وتبحث عن جوانتي قيادة أسود منقط لحماية اليدين من الشمس والاسمرار.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>قفازات القيادة الأنيقة (Driving Accessories)</td></tr>
  <tr><th>الفئة</th><td>إكسسوارات القيادة / قفازات حماية اليدين من الشمس للقيادة</td></tr>
  <tr><th>نوع المنتج</th><td>قفازات قطنية مسامية للحماية من الشمس ومقاومة للانزلاق (زوج واحد)</td></tr>
  <tr><th>الحجم/الوزن</th><td>مقاس موحد مرن (Free Size)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (النساء والفتيات)</td></tr>
  <tr><th>المظهر النهائي</th><td>يدين محميتين من أشعة الشمس والتسمير بمظهر أنيق أسود منقط</td></tr>
  <tr><th>الملمس</th><td>قماش قطني ناعم مرن ومطاطي مسامي</td></tr>
  <tr><th>العطر</th><td>خالٍ من العطور (منتج قماشي)</td></tr>
  <tr><th>المكونات النشطة</th><td>ألياف قطن 80%، سباندكس 20%، نقاط سيليكون مانعة للانزلاق</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين (China)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Sun Protection Products Ltd.</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغات والمراهقات (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد ألياف القطن والحماية من الأشعة فوق البنفسجية في جوانتي القيادة</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج قفازات القيادة مشكلة اسمرار اليدين والتصبغات وخشونة الجلد الناجمة عن تعرض اليدين المستمر لأشعة الشمس أثناء القيادة.</p>

<h3>لماذا تنجح تركيبة UV Protection Driving Gloves؟</h3>
<p>لأن الألياف القطنية الكثيفة تعكس 98% من الأشعة فوق البنفسجية (UVA/UVB) بينما تضمن النقاط السيليكونية التحكم المقود.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الارتداء الفوري قبل القيادة بالنهار:</strong> يمنح حماية كاملة من ضربات الشمس والتصبغات.<br>
2. <strong>الغسيل اليدوي المنتظم بماء بارد:</strong> يحافظ على مرونة القماش ونقاط السيليكون.<br>
3. <strong>التكميل بكريم واقي شمس لليدين:</strong> يضاعف وقاية وتغذية الجلد.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "قفازات القيادة تسبب تعرق وحرارة الكفين."<br>
<strong>الحقيقة:</strong> هذا الجوانتي مصمم بنسيج قطني مسامي ينفس البشرة ويمتص الرطوبة الانتعاشية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تحجب ألياف القطن المنسوجة بكثافة الإشعاع الشمسي فوق البنفسجي وتمنع أكسدة صبغة الميلانين بالجلد.</p>"""

    faqs = [
        ("ما هو جوانتي قيادة اسود منقط؟", "هو قفاز قيادة قطني فاخر ومسامي باللون الأسود المنقط لحماية اليدين من أشعة الشمس والتسمير أثناء القيادة."),
        ("ما هي فوائد قفازات القيادة القطنية لحماية اليدين؟", "تحمي اليدين من أشعة الشمس (UV)، تمنع الاسمرار والتصبغات، وتوفر مسكة مانعة للانزلاق على مقود السيارة."),
        ("هل تحمي اليدين من اسمرار الشمس أثناء القيادة؟", "نعم، مثبتة في حجب الأشعة فوق البنفسجية ومنع اسمرار وتصبغات الكفين."),
        ("ما مقاس القفازات؟", "تأتي بمقاس موحد مرن (Free Size) يناسب جميع أيدي النساء."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ارتدي القفازات قبل البدء بالقيادة بالنهار، واغسليها يدويًا بماء بارد عند الحاجة."),
        ("هل هي مسامية ولا تسبب تعرق الكفين؟", "نعم، 100% قطنية مسامية توفر تهوية تامة وتمنع تعرق اليدين في الصيف."),
        ("أين صُنع جوانتي القيادة؟", "صُنع وفق أعلى معايير الحماية والتصاميم العصرية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع إكسسوارات العناية لدى إكليل أبها جودة عالية وأصلية 100%."),
        ("ما شكل ولون القفازات؟", "لون أسود منقط بنقاط بيضاء أو رمادية أنيقة وفاخرة."),
        ("هل النقاط المطاطية تمنع الانزلاق على الدركسون؟", "نعم، توفر مسكة ثبات ممتازة على عجلة قيادة السيارة."),
        ("هل القفازات قابلة للغسل بالماء؟", "نعم، قابلة للغسل اليدوي وإعادة الاستخدام لسنوات."),
        ("كيف أحتفظ بالقفازات؟", "في مكان بارد وجاف أو بداخل دراج السيارة."),
        ("هل جوانتي القيادة ضروري لكل من تقود السيارة؟", "نعم، إكسسوار أساسي وضروري جداً لحماية جمال ونعومة اليدين."),
        ("كم مرة يُستخدم؟", "يومياً أثناء القيادة نهاراً وخارج المنزل."),
        ("هل يسهل ارتداء القفازات وخلعها؟", "نعم، مرنة جداً وسهلة الارتداء والخلع."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل تناسب القيادة في جميع الفصول؟", "نعم، ممتازة خاصة للصيف ولجميع الأوقات المشموسة."),
        ("هل تمنح شكلاً أنيقاً أثناء القيادة؟", "نعم، تمنح مظهراً أنثوياً أنيقاً ومتميزاً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الفتيات والنساء؟", "نعم، مقاس وتصميم مخصص للفتيات والنساء."),
        ("هل يصلح هدية ممتازة لمن تمتلك سيارة؟", "نعم، هدية أنيقة ومفيدة وعملية جداً."),
        ("هل يحمي أطراف الأصابع أيضاً؟", "نعم، يغطي اليدين والكبس وأطراف الأصابع لحماية شاملة."),
        ("هل يعيد الثقة بجمال ونعومة الكفين؟", "نعم، يحافظ على شباب ونعومة بشرة اليدين."),
        ("هل تتوفر ألوان أخرى؟", "نعم، تتوفر خيارات إكسسوارات متعددة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Black Polka Dot Driving Gloves</strong> are authentic luxury stylish summer sun-protection driving gloves designed to shield your hands and wrist skin against harmful UV sun rays and prevent tanning, hyperpigmentation, and dark spots during daily car driving. Built upon flexible breathable cotton fabric, an elegant polka dot pattern, and a non-slip grip surface for steering wheel control.</p>
<p>Black Polka Dot Driving Gloves insulate against ultraviolet rays (UV Protection), stop hand palm sweating, and provide ventilation and total comfort, leaving your hands touchably soft, protected from tanning, and stylishly comfortable during daily drives.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Superior UV Sun Protection:</strong> Prevents hand tanning, dark spots, and sun damage while driving.</li>
  <li><strong>Elegant & Stylish Black Polka Dot Design:</strong> Adds a feminine modern aesthetic touch.</li>
  <li><strong>Lightweight Breathable Cotton Fabric:</strong> Ensures ventilation and prevents palm sweating in summer.</li>
  <li><strong>Anti-Slip Palm Grip Texture:</strong> Enhances steering wheel control and handling stability.</li>
  <li><strong>Flexible Universal One-Size Fit:</strong> Easy to put on and take off without tightness.</li>
  <li><strong>Washable & Reusable for Years:</strong> Durable high-quality textile construction.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Put on driving gloves before starting car driving during daylight hours.</li>
  <li><strong>Step 2:</strong> Ensure proper finger positioning and comfortable palm fit over steering wheel.</li>
  <li><strong>Step 3:</strong> Hand-wash gloves with mild soap and water when needed and air dry.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Cotton & Spandex Elastic Fibers:</strong> Provide a breathable texture ventilating skin and absorbing sweat.</li>
  <li><strong>Silicone Anti-Slip Grip Dots:</strong> Ensure firm non-slip traction on the steering wheel.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical use for sun protection while driving and outdoors.</li>
  <li>Hand-wash with cold water to protect rubber grip dots.</li>
  <li>Keep in a cool, dry place away from direct flames.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Any female driver seeking Black Polka Dot Driving Gloves to protect hand skin from sun tanning and dark spots.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Driving Accessories</td></tr>
  <tr><th>Category</th><td>Driving Accessories / Sun Protection Driving Gloves</td></tr>
  <tr><th>Product Type</th><td>Breathable Anti-Slip Sun Protection Driving Gloves (1 Pair)</td></tr>
  <tr><th>Volume/Weight</th><td>Universal Flexible Fit (Free Size)</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Women & Girls)</td></tr>
  <tr><th>Finish</th><td>Sun-protected, untanned hand skin with an elegant polka dot look</td></tr>
  <tr><th>Texture</th><td>Soft elastic stretchable breathable cotton fabric</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (Textile Product)</td></tr>
  <tr><th>Active Ingredients</th><td>80% Cotton Fibers, 20% Spandex, Silicone Grip Dots</td></tr>
  <tr><th>Country of Origin</th><td>China</td></tr>
  <tr><th>Manufacturer</th><td>Sun Protection Products Ltd.</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Cotton UV Blocking & Steering Traction Control</h2>

<h3>What problem does this solve?</h3>
<p>Black Polka Dot Driving Gloves resolve hand sun tanning, dark spots, skin roughness, and steering wheel slip from sweat.</p>

<h3>Why choose Polka Dot Driving Gloves?</h3>
<p>Densely woven cotton blocks 98% of UVA/UVB rays while silicone grip dots maintain secure wheel handling.</p>"""

    en_faqs = [
        ("What are Black Polka Dot Driving Gloves?", "They are stylish breathable cotton sun protection driving gloves in black polka dot design (1 pair)."),
        ("What are the benefits of cotton driving gloves for hand protection?", "Shield hands from UV sun rays, prevent tanning and dark spots, and provide a non-slip steering wheel grip."),
        ("Do they protect hands from sun tanning while driving?", "Yes, proven to block UV rays and prevent hand palm tanning and dark spots."),
        ("What size are these gloves?", "Universal flexible fit (Free Size) fitting all women's hands."),
        ("How do I use them correctly?", "Slip on gloves before driving during daytime and hand-wash with cold water when needed."),
        ("Are they breathable and sweat-proof?", "Yes, 100% breathable cotton providing ventilation and stopping palm sweating in summer."),
        ("Where are Driving Gloves manufactured?", "Manufactured to international sun protection quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All driving accessories at Ekleel Abha are 100% original."),
        ("What pattern do these gloves have?", "Classic black background with elegant polka dots."),
        ("Do rubber dots prevent steering wheel slipping?", "Yes, provide excellent firm traction on the car steering wheel."),
        ("Are these gloves washable?", "Yes, hand-washable and reusable for years."),
        ("How should I store them?", "In a cool, dry place or in the car glove compartment."),
        ("Are driving gloves necessary for female drivers?", "Yes, a practical essential accessory for preserving hand skin beauty and softness."),
        ("How many times used?", "Daily during daytime driving and sunny outdoor errands."),
        ("Are they easy to put on and remove?", "Yes, flexible stretchable fit easy to put on and remove."),
        ("Is the packaging recyclable?", "Yes."),
        ("Are they good for all seasons?", "Yes, especially ideal for hot sunny summer driving."),
        ("Do they look elegant while driving?", "Yes, impart an elegant feminine stylish driving look."),
        ("Are they available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Are they suitable for women and girls?", "Yes, tailored fit for women and girls."),
        ("Are they a nice gift for car owners?", "Yes, an elegant practical gift for any female driver."),
        ("Do they protect fingers and wrists?", "Yes, cover hands, wrists, and fingertips for complete protection."),
        ("Do they restore confidence in hand skin softness?", "Yes, preserve hand skin youthfulness and touchable softness."),
        ("Are other colors available?", "Yes, various driving accessory options are available at Ekleel Abha."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q} Bios</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2078",
        "sku": "EK-2078",
        "gtin": "014117",
        "brand": "Driving Accessories",
        "ar": {
            "title": "جوانتي قيادة اسود منقط",
            "meta_title": "قفازات قيادة سوداء منقطة للحماية من الشمس | إكليل أبها",
            "meta_description": "اشتري جوانتي قيادة أسود منقط. قفازات قطنية مسامية حامية من أشعة الشمس والتسمير ومقاومة للانزلاق أثناء القيادة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["جوانتي_قيادة", "قفازات_الشمس", "حماية_اليدين_من_التسمير", "قفازات_أسود_منقط", "إكليل_أبها"]
        },
        "en": {
            "title": "Black Polka Dot Driving Gloves",
            "meta_title": "Black Polka Dot Sun Driving Gloves | Ekleel Abha",
            "meta_description": "Buy original Black Polka Dot Driving Gloves. Breathable anti-slip cotton UV protection sun driving gloves. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["driving_gloves", "black_polka_dot_gloves", "sun_protection_gloves", "uv_gloves", "ekleel_abha"]
        }
    }


def create_product_2080():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مرطب شفاه للبشرة شديدة الجفاف من كيوفي 15جم (QV Lip Balm for Very Dry Skin - 15g)</strong> بلسم المرطب والعلاجي الطبي الفاخر الأكثر توصية من كيوفي (QV) المصمم خصيصاً لترطيب، ترميم، وتنعيم الشفاه شديدة الجفاف، المتشققة، والمتقشرة مع توفير حماية حمائية ضد أشعة الشمس SPF 30. يرتكز هذا المرطب الأصيل (QV Lip Balm 15g) على مجمع البارافين الأبيض والزيوت الطبية (Liquid & Soft Paraffin)، فيتامين E المغذي، والواقيات الشمسية الواقية.</p>
<p>يعمل مرطب شفاه كيوفي الطبي على غلاف الشفاه بحجاب وقائي غني يمنع تبخر الماء، حبس الترطيب لـ 24 ساعة، وإخفاء التشققات والخشونة المؤلمة، ليترك شفاهك ناعمة كالحرير، مرطبة عمقاً، ممتلئة بالنضارة، ومحمية من الحساسية والجفاف من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتغذية مكثفة للشفاه شديدة الجفاف والمتشققة:</strong> يعالج التقشر والتشقق المؤلم.</li>
  <li><strong>حماية فائقة من أشعة الشمس بفلتر SPF 30:</strong> يقي الشفاه من الاسمرار وضرر الشمس.</li>
  <li><strong>ترميم حاجز الشفاه بفيتامين E والبارافين الطبي:</strong> يعيد بناء الأنسجة الرقيقة.</li>
  <li><strong>تركيبة خالية 100% من العطور، النكهات، واللانولين:</strong> يناسب الشفاه المفرطة الحساسية.</li>
  <li><strong>شكل أنبوب انسيابي بمطباق مريح:</strong> يسهل تطبيقه بسلاسة في أي وقت.</li>
  <li><strong>موصى به طبياً من أطباء الجلدية:</strong> منتج العناية الشاملة بالشفاه.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> اضغطي كمية صغيرة من مرطب كيوفي على المطباق أو الأصبع.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي البلسم برفق على الشفاه الجافة أو المتشققة.</li>
  <li><strong>الخطوة الثالثة:</strong> كوري التطبيق قبل التعرض للشمس بـ 20 دقيقة وعند الحاجة (يُستعمل عدة مرات يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>فيتامين E والبارافين الطبي:</strong> يرممان التشققات ويحبسان الرطوبة الداخلية.</li>
  <li><strong>فلاتر الحماية من الشمس SPF 30:</strong> تحمي الشفاه من أشعة UVA/UVB الضارة.</li>
</ul>

<h2>تحذيرات وااحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على الشفاه فقط.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من تشقق وجفاف الشفاه الشديد ويبحث عن مرطب كيوفي للشفاه 15 جم بحماية SPF 30.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كيوفي (QV Ego)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشفاه / مرطبات وبلسم الشفاه الطبية من كيوفي 15g</td></tr>
  <tr><th>نوع المنتج</th><td>بلسم مرطب طبي مصلح للشفاه شديدة الجفاف بـ SPF 30 وفيتامين E (15g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>15 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>الشفاه شديدة الجفاف، المتشققة والمفرطة الحساسية</td></tr>
  <tr><th>المظهر النهائي</th><td>شفاه ناعمة كالحرير، مرطبة 24 ساعة، ممتلئة ومحمية من التشققات والشمس</td></tr>
  <tr><th>الملمس</th><td>بلسم كريمي غني يمتص بسلاسة دون لزوجة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور والنكهات (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>بارافين طبي، فيتامين E، فلاتر واقية من الشمس SPF 30</td></tr>
  <tr><th>بلد المنشأ</th><td>أستراليا (Australia)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد البارافين الطبي وفيتامين E في مرطب شفاه كيوفي (QV Lip Balm)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مرطب شفاه كيوفي مشكلة التشققات الشديدة، الجنزرة المؤلمة، الجفاف الناجم عن الجو الشتوي أو الأدوية، وحروق الشمس بالشفاه.</p>

<h3>لماذا تنجح تركيبة QV Intensive Lip Balm؟</h3>
<p>لأن البارافين الطبي يشكل عازلاً يمنع تبخر الماء بينما يسرع فيتامين E التئام الجروح والشقوق.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق قبل الخروج للشمس بـ 20 دقيقة:</strong> يضمن أقصى وقاية بـ SPF 30.<br>
2. <strong>التطبيق قبل النوم بطبقة سخية:</strong> يعمل كقناع ترميم ليلي للشفاه.<br>
3. <strong>تجنب لعق الشفاه عند الجفاف:</strong> يمنع زيادة الجفاف والتفتت.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مرطبات الشفاه تسبب الإدمان والاعتماد الجلدي."<br>
<strong>الحقيقة:</strong> مرطب كيوفي خالي من المواد المهيجة والنكهات ويعيد البناء البيولوجي الطبيعي لأنسجة الشفاه.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>ترمم الدهون الطبية الغشاء المخاطي للشفاه وتمنع نفاذ الأشعة فوق البنفسجية المحللة للكولاجين.</p>"""

    faqs = [
        ("ما هو مرطب شفاه للبشرة شديدة الجفاف من كيوفي 15جم؟", "هو بلسم مرطب طبي خالي من العطور بـ SPF 30 وفيتامين E لترميم الشفاه شديدة الجفاف والمتشققة (15 جم)."),
        ("ما هي فوائد فيتامين E والبارافين الطبي وفلتر SPF 30؟", "يرممان تشققات الشفاه، يحبسان الترطيب لـ 24 ساعة، ويحميان الشفاه من أشعة الشمس والاسمرار."),
        ("هل يرمم الشفاه المتشققة ويحمي من الشمس فورياً؟", "نعم، مثبت سريرياً في ترميم تشققات الشفاه الشديدة وتوفير ترطيب وحماية SPF 30."),
        ("ما حجم العبوة؟", "تأتي بأنبوب مريح بمطباق بسعة 15 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اضغطي كمية ووزعيها على الشفاه قبل الشمس بـ 20 دقيقة وعند الحاجة عدة مرات يومياً."),
        ("هل هو خالٍ من العطور والنكهات واللانولين؟", "نعم، 100% خالٍ من العطور والنكهات واللانولين ومختبر درماتولوجياً."),
        ("أين صُنع مرطب شفاه كيوفي؟", "صُنع في أستراليا بواسطة Ego Pharmaceuticals."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كيوفي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب مستخدمي أدوية الروكوتان والشفاه شديدة التضرر؟", "نعم، ممتاز جداً للشفاه شديدة التضرر والمتشققة بفعل العلاجات الشديدة."),
        ("هل يترك الشفاه ناعمة وغير لزجة؟", "نعم، ينفذ بسلاسة ليترك الشفاه ناعمة كالحرير دون لزوجة."),
        ("هل أنبوب 15 جم مناسب للجيب والحقيبة؟", "نعم، أنبوب أنيق مدمج مثالي للجيب والحقيبة والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كيوفي الماركة الأولى طبياً في العناية الجلدية الأسترالية؟", "نعم، QV الماركة رقم 1 الموصى بها طبياً في أستراليا."),
        ("كم مرة يومياً؟", "عند الحاجة عدة مرات يومياً وقبل النوم وقبل الخروج للشمس."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في الوقاية من اسمرار الشفاه؟", "نعم، تحمي فلاتر SPF 30 الشفاه من الاسمرار الناجم عن الشمس."),
        ("هل يناسب الأطفال والبالغين؟", "نعم، آمن وممتاز للجميع من سن 3 سنوات."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، بلسم محايد ممتاز للنساء والرجال."),
        ("هل يناسب الشتاء والصيف؟", "نعم، حماية وترميم طبي مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن العناية؟", "نعم، منتج طبي فاخر وأساسي جداً."),
        ("هل يعيد المظهر الناعم السلس للشفاه؟", "نعم، يجعل الشفاه في غاية النعومة والامتلاء."),
        ("هل يناسب كبار السن وجميع الأعمار؟", "نعم، آمن وممتع ومناسب جداً للجميع من سن 3 سنوات لكبار السن."),
        ("هل تتوفر منتجات QV الأخرى؟", "نعم، تتوفر عائلة QV للعناية الجلدية كاملة لدى إكليل أبها."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>QV Lip Balm for Very Dry Skin - 15g</strong> is the world's most dermatologist-recommended authentic luxury medical hydrating lip balm from QV designed to moisturize, repair, and soften severely dry, cracked, and chapped lips while providing SPF 30 sun protection. Built upon liquid and soft medical paraffins, nourishing Vitamin E, and sun protective filters.</p>
<p>QV Medical Lip Balm seals lips in a rich protective shield preventing water evaporation, locking in hydration for 24 hours, and repairing painful cracks and roughness, leaving your lips touchably silky soft, deeply hydrated, plump, and protected against sensitivity from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intensive Hydration & Repair for Severely Dry & Chapped Lips:</strong> Treats painful flaking and cracking.</li>
  <li><strong>SPF 30 Broad Spectrum Sun Protection:</strong> Shields lips against dark discoloration and sun damage.</li>
  <li><strong>Lip Barrier Restoration with Vitamin E & Medical Paraffin:</strong> Rebuilds thin delicate mucosal skin.</li>
  <li><strong>100% Fragrance-Free, Flavor-Free & Lanolin-Free:</strong> Ideal for ultra-sensitive lips.</li>
  <li><strong>Ergonomic Tube with Smooth Applicator:</strong> Allows seamless application anytime, anywhere.</li>
  <li><strong>Dermatologist Recommended Medical Brand:</strong> Comprehensive medical lip care essential.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Squeeze a small amount of QV Lip Balm onto the applicator tip or fingertip.</li>
  <li><strong>Step 2:</strong> Gently smooth the balm over dry or chapped lips.</li>
  <li><strong>Step 3:</strong> Reapply 20 minutes before sun exposure and as needed throughout the day (use multiple times daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Vitamin E & Medical Grade Paraffin:</strong> Repair cracks and seal in internal skin moisture.</li>
  <li><strong>SPF 30 Sun Protective Filters:</strong> Shield delicate lips against harmful UVA/UVB sun rays.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical lip application only.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from severely dry chapped lips seeking QV Lip Balm 15g with SPF 30 protection and intensive repair.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>QV (Ego)</td></tr>
  <tr><th>Category</th><td>Lip Care / QV Medical Hydrating Lip Balms 15g</td></tr>
  <tr><th>Product Type</th><td>Medical Repairing Lip Balm for Severely Dry Lips with SPF 30 & Vitamin E (15g)</td></tr>
  <tr><th>Volume/Weight</th><td>15 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Severely Dry, Chapped & Ultra-Sensitive Lips</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, crack-healed & sun-protected smooth lips</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-sticky creamy balm</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free & Flavor-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>Medical Paraffin, Vitamin E, Sun Protection Filters (SPF 30)</td></tr>
  <tr><th>Country of Origin</th><td>Australia</td></tr>
  <tr><th>Manufacturer</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 3+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Medical Paraffin Occlusion & Vitamin E Mucosal Repair</h2>

<h3>What problem does this solve?</h3>
<p>QV Lip Balm resolves severe lip chapping, painful cracks, weather-induced dryness, and sun damage.</p>

<h3>Why choose QV Intensive Lip Balm?</h3>
<p>Medical paraffin forms an occlusive barrier preventing transepidermal water loss while Vitamin E accelerates wound healing.</p>"""

    en_faqs = [
        ("What is QV Lip Balm for Very Dry Skin - 15g?", "It is a medical fragrance-free lip balm with SPF 30 and Vitamin E from QV for repairing severely dry and chapped lips (15g)."),
        ("What are the benefits of Vitamin E, medical paraffin, and SPF 30?", "Repair lip cracks, lock in 24-hour hydration, and shield lips from sun damage and dark discoloration."),
        ("Does it repair chapped lips and protect from sun instantly?", "Yes, clinically proven to repair severe lip chapping and deliver 24-hour hydration with SPF 30."),
        ("What volume is contained in this tube?", "15g sleek tube with applicator tip."),
        ("How do I use it correctly?", "Squeeze gel, smooth over lips 20 minutes before sun exposure, and reapply as needed."),
        ("Is it fragrance-free, flavor-free, and lanolin-free?", "Yes, 100% free from fragrances, flavors, and lanolin, and dermatologically tested."),
        ("Where is QV Lip Balm manufactured?", "In Australia by Ego Pharmaceuticals."),
        ("How do I verify authenticity at Ekleel Abha?", "All QV products at Ekleel Abha are 100% original."),
        ("Is it suitable for acne-medication users and severely damaged lips?", "Yes, excellent for severely dry chapped lips caused by Roaccutane or harsh weather."),
        ("Does it leave lips soft and non-sticky?", "Yes, glides smoothly leaving lips touchably soft without stickiness."),
        ("Is the 15g tube pocket and travel friendly?", "Yes, sleek compact tube ideal for pocket, handbag, and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is QV the #1 medical skincare brand in Australia?", "Yes, QV is the #1 dermatologist recommended brand in Australia."),
        ("How many times daily?", "Multiple times daily as needed and bedtime."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it help prevent lip darkening?", "Yes, SPF 30 filters protect lips against sun-induced darkening."),
        ("Is it suitable for adults and children?", "Yes, safe and suitable for everyone aged 3+."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, neutral balm suitable for both men and women."),
        ("Is it good for all seasons?", "Yes, ideal medical lip repair for summer and winter."),
        ("Is it a nice skincare gift?", "Yes, a premier medical essential for daily lip care."),
        ("Does it restore smooth plump lips?", "Yes, leaves lips touchably soft and healthy."),
        ("Are other QV products available?", "Yes, the full QV medical skincare range is available at Ekleel Abha."),
        ("Is it suitable for elderly skin and all ages?", "Yes, safe, gentle, and highly suitable for all ages from 3+ to seniors."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2080",
        "sku": "EK-2080",
        "gtin": "9314839018633",
        "brand": "QV",
        "ar": {
            "title": "مرطب شفاه للبشرة شديدة الجفاف من كيوفي 15جم",
            "meta_title": "مرطب شفاه كيوفي شديد الجفاف SPF 30 15جم | إكليل أبها",
            "meta_description": "اشتري مرطب شفاه للبشرة شديدة الجفاف من كيوفي (15 جم). بلسم طبي مصلح بـ SPF 30 وفيتامين E لترميم الشفاه المتشققة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كيوفي", "مرطب_شفاه_كيوفي", "ترميم_الشفاه_المتشققة", "واقي_شمس_شفاه_SPF30", "إكليل_أبها"]
        },
        "en": {
            "title": "QV Lip Balm for Very Dry Skin - 15g",
            "meta_title": "QV Lip Balm for Very Dry Skin SPF 30 15g | Ekleel Abha",
            "meta_description": "Buy original QV Lip Balm for Very Dry Skin (15g). Medical repairing lip balm with SPF 30 and Vitamin E. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["qv", "qv_lip_balm", "chapped_lip_balm", "spf30_lip_balm", "ekleel_abha"]
        }
    }


def _make_lux_wash_b72(pid, gtin, ar_name, en_name, scent_ar, scent_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> سائل الاستحمام العطري الفاخر الأيقوني من لوكس (Lux) المصمم لمنح جسمك نظافة عميقة ورغوة مخملية غنية وعطراً فواحاً يدوم لـ 24 ساعة. يرتكز هذا الغسول الأصيل ({en_name}) على زيوت Everscent العطرية الأساسية، خلاصات {scent_ar} الفاخرة، والمركبات المرطبة لبشرة الجسم.</p>
<p>يعمل غسول لوكس العطري على تنظيف مسام الجسم وإزالة الشوائب، حماية الجلد من الجفاف وحفظ طراوته، وتغليف جسمك بنفحات {scent_ar} الفواحة، ليترك بشرتك ناعمة كالحرير، مرطبة، ومعطرة بالنظافة والجاذبية طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عطر فواح يدوم لـ 24 ساعة بتقنية Everscent Oil:</strong> يغلف الجسد بعبير {scent_ar} الفاخر.</li>
  <li><strong>تنظيف عميق ورغوة كريمية غنية:</strong> ينظف الجسم بلطف دون انتزاع الزيوت الطبيعية.</li>
  <li><strong>ترطيب وتنعيم لبشرة الجسم:</strong> يحفظ حاجز الترطيب الطبيعي للجلد.</li>
  <li><strong>تركيبة خفيفة متوازنة الحموضة (pH Balanced):</strong> مناسبة للاستخدام اليومي لجميع أنواع البشرة.</li>
  <li><strong>جودة لوكس (Lux) العالمية الشهيرة:</strong> العلامة الأولى في عطور وجمال الاستحمام.</li>
  <li><strong>عبوة اقتصادية ضخمة سعة 700 مل مزودة بضاغط:</strong> حجم ممتاز للاستخدام العائلي اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الجسم بالماء الدافئ أثناء الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> اضغطي كمية مناسبة من سائل لوكس على ليفة الاستحمام أو الكفين وكوّني رغوة غنية.</li>
  <li><strong>الخطوة الثالثة:</strong> دلكي الجسم برفق بحركات دائرية ثم اشطفي جيداً بالماء (يُستعمل يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت Everscent العطري وخلاصة {scent_ar}:</strong> يثبتان جزيئات العطر الفواح على البشرة.</li>
  <li><strong>المنظفات اللطيفة والمركبات المرطبة:</strong> تنظف الجسم وتحفظ نعومته الحريرية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} للانتعاش العطري والنظافة الحريرية.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لوكس (Lux)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / غسولات ومجموعات الاستحمام المعطرة من لوكس 700ml</td></tr>
  <tr><th>نوع المنتج</th><td>غسول جسم عطري مرطب بنفحات {scent_ar} وزيت Everscent (700ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>700 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (العادية، الجافة والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، مرطب، ناصع النظافة ومفعم بعطر {scent_ar} لـ 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>سائل جل عطري رغوي غني</td></tr>
  <tr><th>العطر</th><td>عطر {scent_ar} الفواح لـ 24 ساعة</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت Everscent Essential Oil، خلاصة {scent_ar}، منظفات لطيفة</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الإمارات</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever Group</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد زيت Everscent وخلاصة {scent_ar} في غسول لوكس (Lux Body Wash)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول لوكس مشكلة جفاف البشرة بعد الاستحمام بالصابون القاسي وتلاشي عطر النظافة سريعاً.</p>

<h3>لماذا تنجح تركيبة Lux Perfumed Body Wash؟</h3>
<p>لأن تقنية زيوت Everscent العطرية تفرز جزيئات العطر التي ترتبط بالجلد لتمنح ثباتاً لـ 24 ساعة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام اليومي بالماء الدافئ:</strong> ينظف المسام وينشط الدورة الدموية.<br>
2. <strong>استخدام ليفة ناعمة:</strong> يزيد تكوين الرغوة الغنية ويزيل الشوائب.<br>
3. <strong>الشطف الجيد بالماء:</strong> يضمن عدم بقاء أي ترسبات صابونية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "غسولات الجسم المعطرة تجفف البشرة."<br>
<strong>الحقيقة:</strong> غسول لوكس مدعم بمركبات مرطبة تحفظ التوازن المائي للجلد أثناء التنظيف.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخفض السورفاكتانتات اللطيفة التوتر السطحي للماء وتأطر الزيوت والأوساخ لينشطف بها الماء بسلاسة.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو سائل استحمام عطري فاخر من لوكس بنفحات {scent_ar} وزيت Everscent لثبات 24 ساعة (700 مل)."),
        (f"ما هي فوائد خلاصة {scent_ar} وزيت Everscent؟", "تنظف المنظفات اللطيفة البشرة دون جفاف، بينما يثبت زيت Everscent العطر لـ 24 ساعة."),
        ("هل يمنح رغوة غنية وعطراً يدوم لـ 24 ساعة؟", "نعم، مثبت سريرياً في توفير رغوة غنية وثبات عطري يدوم 24 ساعة."),
        ("ما حجم العبوة؟", "تأتي بعبوة ضخمة مزودة بضاغط بسعة 700 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الجسم، اضغطي كمية على الليفة وكوّني رغوة، دلكي برفق واشطفي بالماء يومياً."),
        ("هل هو آمن لجميع أنواع البشرة؟", "نعم، تركيبة متوازنة الحموضة آمنة لجميع أنواع بشرة الجسم."),
        ("أين صُنع غسول لوكس؟", "صُنع بواسطة مجموعة Unilever العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لوكس لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {scent_ar} الساحر الفواح الأنيق."),
        ("هل يترك البشرة ناعمة ومرطبة؟", "نعم، يحافظ على رطوبة الجلد ونعومته الحريرية."),
        ("هل 700 مل تكفي للاستخدام العائلي؟", "نعم، عبوة ضخمة بضاغط تكفي لعدة أشهر من الاستخدام العائلي اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب النساء والرجال؟", "مناسب لجميع أفراد الأسرة وخاصة محبي العطور الفاخرة."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً أثناء الاستحمام."),
        ("هل ينشطف بالماء بسهولة؟", "نعم، ينشطف بالماء الدافئ بسهولة دون ترك أثر لزج."),
        ("هل لوكس علامة عالمية شهيرة؟", "نعم، Lux علامة رائدة ومشهورة جداً عالمياً لمنتجات الاستحمام العطرية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في إزالة رائحة العرق؟", "نعم، ينظف بفاعلية ويعطر الجسم بنفحات عاطرة."),
        ("هل يناسب الاستخدام بعد الرياضة؟", "نعم، ممتاز للانتعاش والنظافة بعد التمارين والرياضة."),
        ("هل يترك أثراً دهنياً؟", "لا، ينظف وينشطف بالكامل دون دهنية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل العبوة مزودة بضاغط مريح؟", "نعم، ضاغط مريح جداً يسهل استخدام الجل أثناء الاستحمام."),
        ("هل يناسب الشتاء والصيف؟", "نعم، ممتاز لجميع فصول السنة."),
        ("هل يصلح هدية ضمن مجموعة الاستحمام؟", "نعم، خيار ممتاز جداً في مجموعات العناية الشخصية."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an iconic luxury fragranced body wash from Lux designed to deliver deep cleansing, a rich velvety lather, and a 24-hour long-lasting scent. Built upon Everscent Essential Oil technology, seductive {scent_en} extracts, and body-moisturizing compounds.</p>
<p>Lux Body Wash cleanses body pores of dirt and excess sebum, guards skin against dryness, and wraps your body in captivating {scent_en} notes, leaving your skin touchably silky soft, hydrated, and fragranced with elegance all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>24-Hour Long-Lasting Fragrance with Everscent Oil:</strong> Coats body in a captivating {scent_en} scent all day.</li>
  <li><strong>Deep Cleansing & Rich Creamy Lather:</strong> Cleanses body gently without stripping natural skin oils.</li>
  <li><strong>Body Skin Softening & Hydration:</strong> Preserves the skin's natural moisture barrier.</li>
  <li><strong>pH-Balanced Mild Formula:</strong> Suitable for daily use on all skin types.</li>
  <li><strong>Famous Quality of Lux Global:</strong> #1 recognized brand in perfumed bath care.</li>
  <li><strong>Generous 700ml Jumbo Pump Bottle:</strong> Excellent value lasting months of continuous daily family use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet body skin with warm water during shower.</li>
  <li><strong>Step 2:</strong> Pump a suitable amount of Lux gel onto a shower loofah or hands and work into a rich lather.</li>
  <li><strong>Step 3:</strong> Massage body gently in circular motions, then rinse thoroughly with water (use daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Everscent Essential Oil & {scent_en} Extract:</strong> Bind fragrance molecules to skin layers delivering 24-hour freshness.</li>
  <li><strong>Gentle Cleansers & Hydrating Agents:</strong> Cleanse body while maintaining touchable silky softness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application only.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for 24-hour fragrance and silky clean skin.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lux</td></tr>
  <tr><th>Category</th><td>Body Care / Lux Perfumed Hydrating Body Washes 700ml</td></tr>
  <tr><th>Product Type</th><td>24H Perfumed Body Wash with {scent_en} & Everscent Essential Oil (700ml)</td></tr>
  <tr><th>Volume/Weight</th><td>700 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Normal, Dry & Oily Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, hydrated, spotlessly clean body skin fragranced with {scent_en} for 24H</td></tr>
  <tr><th>Texture</th><td>Rich foaming fragranced clear gel fluid</td></tr>
  <tr><th>Fragrance</th><td>Captivating long-lasting {scent_en} scent for 24 hours</td></tr>
  <tr><th>Active Ingredients</th><td>Everscent Essential Oil, {scent_en} Extract, Gentle Cleansers</td></tr>
  <tr><th>Country of Origin</th><td>KSA / UAE</td></tr>
  <tr><th>Manufacturer</th><td>Unilever Group</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Everscent Essential Oil Binding & 24-Hour Fragrance Retention</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves skin dryness caused by harsh soaps, daily sweat accumulation, and fading body fragrance.</p>

<h3>Why choose Lux Body Wash?</h3>
<p>Everscent Essential Oil technology binds perfume micro-droplets to skin keratin providing sustained 24-hour fragrance release.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a luxury perfumed body wash from Lux with {scent_en} and Everscent Oil for 24-hour fragrance (700ml)."),
        (f"What are the benefits of {scent_en} extract and Everscent Oil?", "Gentle cleansers cleanse skin without dryness, while Everscent Oil binds fragrance for 24 hours."),
        ("Does it yield a rich lather and 24-hour fragrance?", "Yes, clinically proven to produce a rich lather and deliver 24-hour fragrance retention."),
        ("What volume is contained in this bottle?", "700ml jumbo pump bottle."),
        ("How do I use it correctly?", "Wet body, pump gel onto loofah, lather, massage gently and rinse with water daily."),
        ("Is it safe for all skin types?", "Yes, pH-balanced formula safe for all body skin types."),
        ("Where is Lux Body Wash manufactured?", "By Unilever Group."),
        ("How do I verify authenticity at Ekleel Abha?", "All Lux products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", f"Captivating elegant {scent_en} fragrance."),
        ("Does it leave skin soft and hydrated?", "Yes, preserves skin moisture and silky softness."),
        ("Does 700ml last long for family use?", "Yes, jumbo pump bottle lasts months of regular family use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for men and women?", "Yes, suitable for the entire family."),
        ("How many times daily?", "Once or twice daily during showers."),
        ("Does it rinse off easily?", "Yes, rinses off smoothly with warm water without sticky residue."),
        ("Is Lux a world-famous brand?", "Yes, Lux is a globally leading brand in perfumed bath care."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help remove sweat odor?", "Yes, effectively cleanses and perfumes body skin."),
        ("Is it good post-workout?", "Yes, excellent for post-workout refreshing shower routines."),
        ("Does it leave a greasy film?", "No, cleanses completely clean without greasiness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is the pump bottle convenient?", "Yes, convenient pump dispenser for easy showering."),
        ("Is it good for summer and winter?", "Yes, excellent for all seasons."),
        ("Is it a nice shower gift?", "Yes, excellent addition to personal care gift sets."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Lux",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. سائل استحمام بعطر {scent_ar} الفواح لـ 24 ساعة وترطيب البشرة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. 24H perfumed {scent_en} body wash. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2081():
    return _make_lux_wash_b72(
        pid=2081, gtin="6281006570009",
        ar_name="غسول جسم سحر زهرة الاوركيد من لوكس 700مل",
        en_name="Lux Magical Orchid Body Wash - 700ml",
        scent_ar="زهرة الأوركيد الساحرة", scent_en="Magical Orchid",
        feature_ar="سائل استحمام عطري بنفحات زهرة الأوركيد الفاخرة لـ 24 ساعة 700 مل", feature_en="magical orchid 24H perfumed body wash 700ml",
        tags_ar=["لوكس", "غسول_لوكس_الأوركيد", "زهرة_الأوركيد_الساحرة", "سائل_استحمام_لوكس", "إكليل_أبها"],
        tags_en=["lux", "lux_magical_orchid", "orchid_body_wash", "lux_body_wash_700ml", "ekleel_abha"]
    )


def create_product_2082():
    return _make_lux_wash_b72(
        pid=2082, gtin="6281006569775",
        ar_name="غسول جسم الورد الناعم من لوكس 700مل",
        en_name="Lux Soft Rose Body Wash 700ml",
        scent_ar="الورد الناعم والرقيق", scent_en="Soft Rose",
        feature_ar="سائل استحمام عطري بنفحات الورد الناعم الترطيبية لـ 24 ساعة 700 مل", feature_en="soft rose 24H perfumed moisturizing body wash 700ml",
        tags_ar=["لوكس", "غسول_لوكس_الورد_الناعم", "الورد_الناعم_لوكس", "سائل_استحمام_معطر", "إكليل_أبها"],
        tags_en=["lux", "lux_soft_rose", "rose_body_wash", "lux_rose_700ml", "ekleel_abha"]
    )


print("Loaded all 5 Batch 72 builders complete")
