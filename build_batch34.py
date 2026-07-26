import json, os

def create_product_1881():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مزيل عرق الطبيعي من بيزلين 50 مل (Beesline Natural Deodorant 50ml)</strong> مزيل العرق الطبيعي الكلاسيكي الأصيل من بيزلين المصمم لتأمين جفاف لطيف وحماية مضادة للبكتيريا والروائح الكريهة دون مواد كيميائية ضارة. يرتكز هذا الرول اون الأصيل من بيزلين (Beesline Natural Deodorant Roll-On 50ml) على حجر الشبة الطبيعي (Alum Rock)، صمغ النحل النقي (Propolis)، وخلاصة الألوفيرا المهدئة.</p>
<p>يعمل مزيل عرق بيزلين الطبيعي 50 مل على الحد من نمو البكتيريا المسببة للرائحة، امتصاص رطوبة العرق الزائدة، وتهدئة بشرة الإبطين الحساسة، ليترك المنطقة جافة، منعشة برائحة ناعمة طبيعية، ومحمية طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية طبيعية من العرق والروائح بـ حجر الشبة الطبيعي:</strong> يمتص العرق ويوقف نمو البكتيريا دون سد المسام.</li>
  <li><strong>تطهير وتهدئة بـ صمغ النحل النقي (Propolis):</strong> يحمي ويطهر بشرة الإبطين الرقيقة.</li>
  <li><strong>ترطيب وتهدئة بـ خلاصة الألوفيرا:</strong> يهدئ البشرة المتهيجة بعد الحلاقة.</li>
  <li><strong>خالي 100% من ألومنيوم كلوروهيدرات، الكحول، والبارابين:</strong> لا يسد المسام ولا يسبب حساسية البشرة.</li>
  <li><strong>رائحة طبيعية ناعمة ومنعشة:</strong> عطر طبيعي خفيف مريح يوفر إحساساً بالنظافة.</li>
  <li><strong>عبوة مدمجة سعة 50 مل:</strong> حجم ممتاز ومناسب للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> نظف منطقة الإبطين بالماء والصابون وجففها جيداً قبل الاستعمال.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> مرر البكرة الدوارة لمزيل عرق بيزلين الطبيعي 1-2 مرة على بشرة الإبط الجافة.</li>
  <li><strong>الخطوة الثالثة (التجفيف):</strong> دع السائل يجف لثوانٍ معدودة قبل ارتداء الملابس (يُستعمل مرة يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>حجر الشبة الطبيعي (Alum Rock):</strong> يمتص العرق ويوقف تكاثر بكتيريا الرائحة طبيعياً.</li>
  <li><strong>صمغ النحل وخلاصة الألوفيرا:</strong> يطهران ويهدئان بشرة الإبطين دون تسبيب أي تهيج.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الإبطين الجافة فقط.</li>
  <li>لا يوضع على الجلد المصاب بجروح مفتوحة أو التهابات شديدة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن مزيل عرق بيزلين الطبيعي 50 مل الأصيل للحماية اليومية من العرق والروائح بمكونات طبيعية آمنة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / مزيلات العرق الطبيعية الرول اون من بيزلين 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>مزيل عرق رول اون طبيعي بحجر الشبة وصمغ النحل والألوفيرا (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الإبطين (بما في ذلك البشرة الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>إبطين جافين تماماً ومنعشين برائحة طبيعية ناعمة ومحميين</td></tr>
  <tr><th>الملمس</th><td>سائل رول اون خفيف ينفذ فورياً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر طبيعي ناعم ومنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>حجر الشبة (Alum Rock)، صمغ النحل (Propolis)، خلاصة الألوفيرا</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد حجر الشبة وصمغ النحل في بيزلين الطبيعي (Beesline Natural Deodorant)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مزيل عرق بيزلين الطبيعي مشكلة العرق اليومي المفرط، الروائح الكريهة، وتهيج الإبطين الحساسة لمن يفضل المكونات الطبيعية 100%.</p>

<h3>لماذا تنجح تركيبة حجر الشبة الطبيعي؟</h3>
<p>لأن بوتاسيوم ألوم في حجر الشبة يضيق مسام الغدد العرقية السطحية ويمنع تكاثر البكتيريا دون أي امتصاص جهازي.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق صباحاً على بشرة جافة نظيفة:</strong> ضع الرول اون فور الاستحمام وتجفيف الإبطين جيداً.<br>
2. <strong>تجنب الاستخدام على جلد مبلل:</strong> تأكد من جفاف الجلد لضمان فعالية قصوى.<br>
3. <strong>الاستخدام المنتظم يضمن حماية مستمرة:</strong> الانتظام اليومي يمنع تراكم البكتيريا والرائحة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "حجر الشبة الطبيعي مثل الألومنيوم الكيميائي ويضر بالصحة."<br>
<strong>الحقيقة:</strong> بوتاسيوم ألوم مادة طبيعية كبيرة الجزيئات لا تمتصها الجلد ومعتمدة علمياً للاستخدام الآمن.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتفاعل أيونات الألومنيوم الطبيعية من حجر الشبة مع بروتينات قنوات العرق السطحية لتضييق مؤقت للغدد دون سدها كيميائياً.</p>"""

    faqs = [
        ("ما هو مزيل العرق الطبيعي من بيزلين 50 مل؟", "هو مزيل عرق رول اون طبيعي 100% من بيزلين بحجر الشبة وصمغ النحل والألوفيرا للحماية اليومية من العرق والروائح سعة 50 مل."),
        ("ما هي فوائد حجر الشبة وصمغ النحل والألوفيرا؟", "يمتص حجر الشبة العرق ويوقف البكتيريا، يطهر صمغ النحل البشرة، وتهدئ الألوفيرا التهيج بعد الحلاقة."),
        ("هل يوفر حماية يومية كافية من العرق والروائح؟", "نعم، مثبت سريرياً في الحد من نمو بكتيريا الروائح وامتصاص رطوبة العرق اليومي."),
        ("ما حجم العبوة؟", "تأتي لعلبة رول اون سعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "مرر البكرة 1-2 مرة على بشرة الإبط النظيفة والجافة، دع السائل يجف ثوانٍ قبل ارتداء الملابس يومياً."),
        ("هل هو خالي 100% من ألومنيوم كلوروهيدرات والبارابين والكحول؟", "نعم، خالي 100% من ألومنيوم كلوروهيدرات والكحول والبارابين وآمن للبشرة الحساسة."),
        ("ما هو بلد صنع مزيل عرق بيزلين الطبيعي؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين العالمية (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يترك أثراً أو بقعاً على الملابس؟", "لا، قوام شفاف ينفذ فورياً دون ترك أي أثر على الملابس."),
        ("ما هي رائحة مزيل عرق بيزلين الطبيعي؟", "يتميز برائحة طبيعية خفيفة ناعمة ومنعشة."),
        ("هل يهدئ تهيج الإبطين بعد الحلاقة؟", "نعم، خلاصة الألوفيرا وصمغ النحل يهدئان البشرة المتهيجة بعد الحلاقة."),
        ("هل عبوة الرول اون 50 مل مناسبة للاستخدام اليومي؟", "نعم، حجم مدمج وأنيق يكفي لعدة أسابيع من الاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعبوتها المغلقة محكماً."),
        ("هل يناسب الرجال والنساء؟", "مناسب لجميع الفئات العمرية للنساء والرجال من سن 12 سنة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة رول اون أنيقة بغطاء محكم الحماية."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل مرة واحدة يومياً صباحاً أو بعد الاستحمام."),
        ("هل يمنع تكاثر البكتيريا المسببة للرائحة؟", "نعم، حجر الشبة وصمغ النحل يمنعان نمو البكتيريا المحللة للعرق."),
        ("هل يناسب البشرة الحساسة جداً؟", "نعم، فورمولا طبيعية 100% خالية من المواد القاسية وآمنة للبشرة الحساسة."),
        ("هل هو مزيل العرق الطبيعي الأكثر طلباً لبيزلين؟", "نعم، Natural Deodorant هو مزيل العرق الطبيعي الأول لبيزلين."),
        ("هل يمنح حس نظافة وانتعاش طوال اليوم؟", "نعم، يضمن جفافاً وانتعاشاً ورائحة طبيعية ناعمة طوال اليوم."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يجف سريعاً على البشرة؟", "نعم، يجف السائل خلال ثوانٍ معدودة."),
        ("هل يترك الجلد طرياً؟", "نعم، يترك جلد الإبطين طرياً ومريحاً."),
        ("هل يصلح للاستخدام في التنقل والسفر؟", "نعم، حجم مدمج مثالي للسفر والتنقل اليومي."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Natural Deodorant 50ml</strong> is the original classic natural roll-on deodorant from Beesline, engineered to provide gentle daily dryness, antibacterial defense, and odor protection without any harsh chemicals. Formulated with natural Alum Rock, pure Propolis, and soothing Aloe Vera extract.</p>
<p>Beesline Natural Deodorant 50ml limits odor-causing bacteria, absorbs excess sweat moisture, and soothes sensitive underarm skin, leaving armpits touchably dry, freshened with a soft natural scent, and protected throughout the day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Natural Alum Rock Sweat & Odor Protection:</strong> Absorbs sweat and stops bacteria without clogging pores.</li>
  <li><strong>Purifying Propolis Defense:</strong> Protects and cleanses delicate underarm skin naturally.</li>
  <li><strong>Soothing Aloe Vera Hydration:</strong> Calms post-shaving irritation and softens underarm skin.</li>
  <li><strong>100% Free of Aluminum Chlorohydrate, Alcohol & Parabens:</strong> Safe for daily sensitive skin use.</li>
  <li><strong>Soft Natural Fresh Fragrance:</strong> Light natural aroma providing clean all-day comfort.</li>
  <li><strong>Compact 50ml Roll-On Bottle:</strong> Ideal daily-use size for continuous freshness.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse underarms with soap and water, pat dry before use.</li>
  <li><strong>Step 2 (Apply):</strong> Roll the Beesline Natural applicator 1-2 times over clean dry underarm skin.</li>
  <li><strong>Step 3 (Dry):</strong> Allow fluid to dry for a few seconds before dressing (use once daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Alum Rock:</strong> Absorbs sweat and naturally prevents odor-causing bacteria multiplication.</li>
  <li><strong>Propolis & Aloe Vera Extract:</strong> Purify and soothe underarm skin without causing irritation.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical dry underarm skin application only.</li>
  <li>Do not apply onto open wounds or severely broken skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Beesline's 50ml Natural Deodorant with Alum Rock and Propolis for safe, daily natural odor protection.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Personal Care / Beesline Natural Roll-On Deodorants 50ml</td></tr>
  <tr><th>Product Type</th><td>Natural Alum Rock & Propolis Daily Roll-On Deodorant (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Underarm Skin Types (Including Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Touchably dry, fresh, natural scented & clean armpits</td></tr>
  <tr><th>Texture</th><td>Smooth lightweight fast-drying roll-on fluid</td></tr>
  <tr><th>Fragrance</th><td>Soft natural fresh aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Alum Rock, Propolis, Aloe Vera Extract</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Potassium Alum Astringency & Propolis Antibacterial Defense</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Natural Deodorant resolves daily perspiration, underarm body odor, and post-shaving irritation for those seeking 100% natural formulas.</p>

<h3>Why choose Beesline Natural Deodorant?</h3>
<p>Potassium alum ions from Alum Rock tighten sweat gland pores and inhibit bacteria without systemic absorption, while Propolis provides antibacterial defense.</p>"""

    en_faqs = [
        ("What is Beesline Natural Deodorant 50ml?", "It is a 100% natural roll-on deodorant from Beesline formulated with Alum Rock, Propolis, and Aloe Vera for daily odor protection."),
        ("What are the benefits of Alum Rock, Propolis, and Aloe Vera?", "Alum Rock absorbs sweat and stops bacteria, Propolis purifies skin, and Aloe Vera soothes post-shaving irritation."),
        ("Does it provide sufficient daily protection from sweat and odor?", "Yes, clinically proven to limit odor-causing bacteria and absorb daily sweat moisture."),
        ("What volume is contained in this bottle?", "It comes in a compact 50ml roll-on bottle."),
        ("How do I apply it correctly?", "Roll 1-2 times onto clean, dry underarm skin, allow to dry for a few seconds, and dress."),
        ("Is it 100% free of aluminum chlorohydrate, alcohol, and parabens?", "Yes, 100% free of aluminum chlorohydrate, alcohol, and parabens; safe for sensitive skin."),
        ("Where is Beesline Natural Deodorant manufactured?", "Proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it leave marks on clothes?", "No, invisible fluid absorbs instantly without leaving marks on clothing."),
        ("What scent does Beesline Natural Deodorant have?", "Features a light, soft, pleasant natural fresh fragrance."),
        ("Does it soothe post-shaving irritation?", "Yes, Aloe Vera extract and Propolis calm underarm skin irritation after shaving."),
        ("Is the 50ml bottle ideal for daily use?", "Yes, compact bottle lasts through weeks of daily continuous use."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Is it suitable for men and women?", "Suitable for all ages, both men and women aged 12+."),
        ("Is the bottle cap leak-proof?", "Yes, features a secure screw-top cap."),
        ("How many times daily should I use it?", "Recommended for use once daily, morning or after showering."),
        ("Does it prevent odor-causing bacteria?", "Yes, Alum Rock and Propolis prevent odor-causing bacterial multiplication."),
        ("Is it safe for very sensitive underarm skin?", "Yes, 100% natural formula free of harsh chemicals; safe for sensitive skin."),
        ("Is it Beesline's original natural deodorant?", "Yes, Natural Deodorant is the original flagship natural deodorant by Beesline."),
        ("Does it provide all-day freshness?", "Yes, guarantees daily dryness, freshness, and clean comfort."),
        ("Is the bottle recyclable?", "Yes, 100% recyclable environmentally friendly bottle."),
        ("Does it dry quickly on skin?", "Yes, fluid dries in seconds for immediate dressing."),
        ("Does it leave underarm skin soft?", "Yes, leaves underarm skin touchably soft and comfortable."),
        ("Is it good for travel?", "Yes, compact size ideal for travel and daily on-the-go use."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1881",
        "sku": "EK-1881",
        "gtin": "5281018019023",
        "brand": "Beesline",
        "ar": {
            "title": "مزيل عرق الطبيعي من بيزلين 50 مل",
            "meta_title": "مزيل عرق طبيعي بيزلين 50مل | إكليل أبها",
            "meta_description": "اشتري مزيل العرق الطبيعي من بيزلين (50 مل). رول اون طبيعي بحجر الشبة وصمغ النحل للحماية اليومية. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["بيزلين", "مزيل_عرق_طبيعي", "حجر_الشبة", "صمغ_النحل", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Natural Deodorant 50ml",
            "meta_title": "Beesline Natural Deodorant 50ml | Ekleel Abha",
            "meta_description": "Buy original Beesline Natural Deodorant (50ml). Alum Rock & Propolis natural roll-on for daily odor protection. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["beesline", "natural_deodorant", "alum_rock", "propolis_deodorant", "ekleel_abha"]
        }
    }


def create_product_1882():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مزيل عرق إنارة فورية للنساء من بيزلين 50 مل (Beesline Instant Brightening Roll-On Deodorant for Women - 50ml)</strong> مزيل العرق الرول اون النسائي الفاخر من بيزلين المصمم خصيصاً للمرأة لتأمين جفاف تام وحماية 48 ساعة وتفتيح فوري لبشرة الإبطين. يرتكز هذا الرول اون (Beesline Instant Brightening Women Roll-On 50ml) على مركب اللوميسكين المبيض (Lumiskin)، صمغ النحل النقي (Propolis)، وخلاصة الألوفيرا المهدئة.</p>
<p>يعمل مزيل بيزلين للنساء على تفتيح التصبغات الداكنة بالإبطين الناتجة عن الاحتكاك والحلاقة المستمرة، منح الجلد لوناً موحداً وناصعاً، وحمايته من العرق والروائح الكريهة، ليترك إبطي المرأة ناعمين كالحرير، ناصعي اللون، ومحميين برائحة نسائية فواحة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح فوري وتوحيد لون بشرة الإبطين للمرأة:</strong> يزيل التصبغات الداكنة بسرعة مذهلة.</li>
  <li><strong>مدعم بـ اللوميسكين وفيتامين C:</strong> يثبط صبغة الميلامين ويجدد خلايا الجلد الرقيقة.</li>
  <li><strong>حماية 48 ساعة من العرق والروائح:</strong> صمغ النحل يقضي على البكتيريا ويحمي الإبطين طوال اليوم.</li>
  <li><strong>تطهير وتهدئة بـ صمغ النحل والألوفيرا:</strong> يهدئ البشرة المتهيجة بعد الحلاقة النسائية.</li>
  <li><strong>خالي 100% من ألومنيوم كلوروهيدرات، الكحول، والبارابين:</strong> مجرب جلدياً وآمن للبشرة الحساسة.</li>
  <li><strong>عبوة مدمجة سعة 50 مل بعطر نسائي فواح:</strong> حجم ممتاز ومناسب لحقيبة السيدة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> نظفي منطقة الإبطين بالماء والصابون وجففيها جيداً قبل الاستعمال.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> مرري البكرة الدوارة لرول اون بيزلين للنساء 1-2 مرة على بشرة الإبط الجافة.</li>
  <li><strong>الخطوة الثالثة (التجفيف):</strong> دعي السائل يجف لثوانٍ معدودة قبل ارتداء الملابس (يُستعمل مرة يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركب لوميسكين وفيتامين C (Lumiskin & Vit C):</strong> يثبطان إنزيم التايروسينيز ويفتحان البقع التصبغية الداكنة.</li>
  <li><strong>صمغ النحل وخلاصة الألوفيرا:</strong> يطهران الجلد ويهدئان التهيج بعد الحلاقة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الإبطين الجافة للنساء فقط.</li>
  <li>لا يوضع على الجلد المصاب بجروح مفتوحة أو التهابات شديدة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن رول اون بيزلين للإنارة الفورية 50 مل لتفتيح إبطين ناصعين وجفاف تام.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين للنساء (Beesline Women)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / مزيلات العرق النسائية الرول اون المبيضة من بيزلين 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>مزيل عرق رول اون نسائي مبيض باللوميسكين وجفاف 48 ساعة (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الإبطين للنساء (بما في ذلك البشرة الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>إبطان ناصعتا اللون، جافتان تماماً، معطرتان بعطر نسائي فواح</td></tr>
  <tr><th>الملمس</th><td>سائل رول اون خفيف ينفذ فورياً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر نسائي فواح ومنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>لوميسكين، صمغ النحل (Propolis)، خلاصة الألوفيرا، فيتامين C</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>النساء والفتيات (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد اللوميسكين وصمغ النحل في بيزلين الإنارة الفورية للنساء</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج رول اون بيزلين للنساء مشكلة التصبغات الداكنة بالإبطين الناتجة عن الحلاقة المستمرة والعرق وضيق الملابس.</p>

<h3>لماذا تنجح تركيبة اللوميسكين للتفتيح الفوري؟</h3>
<p>لأن اللوميسكين يثبط مسار DAG-PKC لتقليل إفراز الميلانين بشكل آمن وتدريجي دون تهيج الجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق صباحاً على جلد جاف:</strong> ضعي الرول اون فور الاستحمام وتجفيف الإبطين.<br>
2. <strong>ارتداء ملابس قطنية واسعة:</strong> التقليل من الاحتكاك يسرع نتائج تفتيح الإبطين.<br>
3. <strong>الاستمرار لـ 3-4 أسابيع:</strong> يضمن الاستخدام المنتظم توحيد لون الإبطين تدريجياً.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مزيلات عرق التفتيح تحتوي على مواد ضارة تضر بصحة المرأة."<br>
<strong>الحقيقة:</strong> رول اون بيزلين للنساء خالي من الهيدروكينون والكحول والبارابين ومجرب جلدياً للبشرة الحساسة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يرتبط اللوميسكين بمستقبلات الدوبامين بخلايا الميلاين السطحية ليثبط إنزيم التايروسينيز ويقلل إنتاج الميلانين الزائد.</p>"""

    faqs = [
        ("ما هو مزيل عرق إنارة فورية للنساء من بيزلين 50 مل؟", "هو رول اون نسائي من بيزلين باللوميسكين وصمغ النحل لتفتيح فوري لإبطين ناصعين وجفاف 48 ساعة 50 مل."),
        ("ما هي فوائد اللوميسكين وصمغ النحل وفيتامين C؟", "يثبط اللوميسكين صبغة الميلامين للتفتيح الفوري، يقضي صمغ النحل على البكتيريا، ويجدد فيتامين C الخلايا."),
        ("هل يفتّح الإبطين بسرعة مذهلة؟", "نعم، مثبت سريرياً في التفتيح الفوري لتصبغات الإبطين الداكنة الناتجة عن الحلاقة."),
        ("ما حجم العبوة؟", "تأتي لعلبة رول اون نسائية سعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "مرري البكرة 1-2 مرة على بشرة الإبط النظيفة والجافة، دعي السائل يجف ثوانٍ قبل ارتداء الملابس يومياً."),
        ("هل هو خالي 100% من ألومنيوم كلوروهيدرات والبارابين والكحول؟", "نعم، خالي 100% من ألومنيوم كلوروهيدرات والكحول والبارابين ومجرب جلدياً للبشرة الحساسة."),
        ("ما هو بلد صنع مزيل عرق بيزلين للنساء؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين العالمية (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يترك أثراً أو بقعاً على الملابس؟", "لا، قوام شفاف ينفذ فورياً دون ترك أي أثر على الملابس."),
        ("ما هي رائحة رول اون بيزلين للنساء؟", "يتميز برائحة نسائية فواحة ومنعشة."),
        ("هل يهدئ تهيج الإبطين بعد الحلاقة النسائية؟", "نعم، صمغ النحل والألوفيرا يهدئان التهابات البشرة بعد الحلاقة."),
        ("هل عبوة الرول اون 50 مل مناسبة لحقيبة السيدة؟", "نعم، حجم مدمج وأنيق مثالي لحقيبة السيدة."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعبوتها المغلقة محكماً."),
        ("هل يناسب النساء والفتيات؟", "مناسب للنساء والفتيات من سن 12 سنة فما فوق."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة رول اون أنيقة بغطاء محكم الحماية."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل مرة واحدة يومياً صباحاً."),
        ("هل يمنع عودة التصبغات الداكنة؟", "نعم، الاستخدام المنتظم يمنع تكاثر البقع التصبغية باللوميسكين."),
        ("هل يناسب البشرة الحساسة؟", "نعم، فورمولا خالية من المواد القاسية وآمنة للبشرة الحساسة."),
        ("هل هو الرول اون النسائي الأكثر طلباً لبيزلين؟", "نعم، Instant Brightening Women Roll-On هو الرول اون النسائي الأول لبيزلين."),
        ("هل يمنح حس ثقة وجمال طوال اليوم؟", "نعم، يضمن إبطين ناصعين وجفافاً وثقة مطلقة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يجف سريعاً على البشرة؟", "نعم، يجف السائل خلال ثوانٍ معدودة."),
        ("هل يترك الجلد طرياً؟", "نعم، يترك جلد الإبطين طرياً ومخملياً."),
        ("هل يصلح للاستخدام في التنقل والسفر؟", "نعم، حجم مدمج مثالي للسفر والتنقل اليومي."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Instant Brightening Roll-On Deodorant for Women - 50ml</strong> is the premium women's natural roll-on deodorant engineered to provide instant underarm brightening, 48-hour total dryness, and antibacterial protection. Formulated with Lumiskin, pure Propolis, and soothing Aloe Vera.</p>
<p>Beesline Women's Roll-On brightens dark underarm hyperpigmentation caused by shaving and friction, unifies skin tone, and shields from sweat and odor, leaving armpits touchably soft, brightened, and protected with a feminine fragrance.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Instant Underarm Brightening & Tone Unification:</strong> Fades dark hyperpigmentation quickly.</li>
  <li><strong>Enriched with Lumiskin & Vitamin C:</strong> Inhibits melanin synthesis and renews delicate underarm cells.</li>
  <li><strong>48-Hour Sweat & Odor Protection:</strong> Propolis eliminates bacteria for all-day protection.</li>
  <li><strong>Soothing Propolis & Aloe Vera Defense:</strong> Calms post-shaving skin irritation for women.</li>
  <li><strong>100% Free of Aluminum Chlorohydrate, Alcohol & Parabens:</strong> Dermatologist tested for sensitive skin.</li>
  <li><strong>Compact 50ml Feminine Scented Bottle:</strong> Ideal size for a woman's handbag.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse underarms with soap and water, pat dry before use.</li>
  <li><strong>Step 2 (Apply):</strong> Roll Beesline Women's applicator 1-2 times over clean dry underarm skin.</li>
  <li><strong>Step 3 (Dry):</strong> Allow to dry for a few seconds before dressing (use once daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Lumiskin & Vitamin C:</strong> Inhibit tyrosinase melanin synthesis for instant brightening.</li>
  <li><strong>Propolis & Aloe Vera Extract:</strong> Purify and soothe underarm skin after shaving.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical dry women's underarm skin application only.</li>
  <li>Do not apply onto open wounds or severely broken skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Women seeking Beesline's 50ml Instant Brightening Roll-On for instant underarm brightening and 48-hour protection.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline Women (Beesline)</td></tr>
  <tr><th>Category</th><td>Personal Care / Beesline Brightening Women Roll-On Deodorants 50ml</td></tr>
  <tr><th>Product Type</th><td>Instant Brightening 48-Hour Women Roll-On Deodorant with Lumiskin (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Women's Underarm Skin Types (Including Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Brightened, touchably soft, dry, odor-free female armpits</td></tr>
  <tr><th>Texture</th><td>Smooth lightweight fast-drying roll-on fluid</td></tr>
  <tr><th>Fragrance</th><td>Fresh feminine fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Lumiskin, Propolis, Aloe Vera Extract, Vitamin C</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>Girls & Women (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Lumiskin Melanin Suppression & Propolis Antibacterial Defense in Women</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Instant Brightening Women Roll-On resolves dark underarm hyperpigmentation from shaving and friction, and odor in women.</p>

<h3>Why choose Beesline Instant Brightening Women Roll-On?</h3>
<p>Lumiskin inhibits DAG-PKC melanin pathways safely without skin toxicity, while Propolis provides antibacterial protection for women.</p>"""

    en_faqs = [
        ("What is Beesline Instant Brightening Roll-On Deodorant for Women - 50ml?", "It is a women's roll-on deodorant with Lumiskin and Propolis for instant underarm brightening and 48-hour total dryness."),
        ("What are the benefits of Lumiskin, Propolis, and Vitamin C?", "Lumiskin inhibits melanin for instant brightening, Propolis eliminates bacteria, and Vitamin C renews skin cells."),
        ("Does it brighten dark underarms instantly?", "Yes, clinically proven to instantly brighten dark underarm hyperpigmentation from shaving and friction."),
        ("What volume is contained in this roll-on bottle?", "It comes in a compact 50ml women's roll-on bottle."),
        ("How do I apply it correctly?", "Roll 1-2 times onto clean, dry underarm skin, allow to dry for a few seconds, and dress."),
        ("Is it 100% free of aluminum chlorohydrate, alcohol, and parabens?", "Yes, 100% free of aluminum chlorohydrate, alcohol, and parabens; dermatologically tested."),
        ("Where is Beesline Women's Roll-On manufactured?", "Proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it leave marks on clothes?", "No, invisible fluid absorbs instantly without leaving marks on clothing."),
        ("What scent does Beesline Women's Roll-On have?", "Features a pleasant, fresh feminine fragrance."),
        ("Does it soothe post-shaving underarm irritation in women?", "Yes, Propolis and Aloe Vera calm skin irritation after women's shaving or hair removal."),
        ("Is the 50ml bottle ideal for a woman's handbag?", "Yes, compact bottle fits perfectly in a handbag or travel kit."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Is it suitable for girls and women?", "Suitable for girls and women aged 12+."),
        ("Is the bottle cap leak-proof?", "Yes, features a secure screw-top cap."),
        ("How many times daily should I use it?", "Recommended for use once daily, in the morning."),
        ("Does it prevent dark spot recurrence?", "Yes, regular Lumiskin use prevents melanin overproduction and dark spot recurrence."),
        ("Is it safe for sensitive female underarm skin?", "Yes, gentle formula free of harsh chemicals; safe for sensitive skin."),
        ("Is it Beesline's #1 women's brightening roll-on?", "Yes, Instant Brightening Women Roll-On is Beesline's #1 women's deodorant."),
        ("Does it provide all-day feminine freshness?", "Yes, guarantees brightened armpits, dryness, and feminine freshness confidence."),
        ("Is the bottle recyclable?", "Yes, 100% recyclable environmentally friendly bottle."),
        ("Does it dry quickly on skin?", "Yes, fluid dries in seconds for immediate dressing."),
        ("Does it leave underarm skin touchably soft?", "Yes, leaves women's underarm skin touchably soft and supple."),
        ("Is it great for travel?", "Yes, compact size ideal for travel and daily on-the-go use."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1882",
        "sku": "EK-1882",
        "gtin": "5281018088142",
        "brand": "Beesline Women",
        "ar": {
            "title": "مزيل عرق انارة فورية للنساء من بيزلين 50 مل",
            "meta_title": "مزيل عرق بيزلين إنارة فورية للنساء 50مل | إكليل أبها",
            "meta_description": "اشتري مزيل عرق إنارة فورية للنساء من بيزلين (50 مل). رول اون نسائي باللوميسكين لتفتيح فوري وجفاف 48 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["بيزلين_للنساء", "تفتيح_الإبط", "رول_اون_نسائي", "لوميسكين", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Instant Brightening Roll-On Deodorant for Women - 50ml",
            "meta_title": "Beesline Instant Brightening Women Deodorant 50ml | Ekleel Abha",
            "meta_description": "Buy original Beesline Instant Brightening Roll-On for Women (50ml). Lumiskin & Propolis women's roll-on for instant brightening and 48-hour protection. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["beesline_women", "brightening_deodorant", "lumiskin_deodorant", "women_roll_on", "ekleel_abha"]
        }
    }


def create_product_1883():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مزيل عرق نسمة من الغابة من بيزلين 50 مل (Beesline Forest Breeze Roll-On Deodorant - 50 ml)</strong> مزيل العرق الرول اون ذو الرائحة الغابية الاستثنائية من بيزلين المصمم لتأمين جفاف تام وحماية مضادة للبكتيريا والروائح الكريهة 48 ساعة مع عطر انتعاشي يذكرك بنسيم الغابة المنعش. يرتكز هذا الرول اون (Beesline Forest Breeze Whitening Roll-On 50ml) على حجر الشبة الطبيعي (Alum Rock)، صمغ النحل (Propolis)، واللوميسكين مع معطر النسمة الغابية.</p>
<p>يعمل مزيل عرق بيزلين نسمة من الغابة على القضاء على البكتيريا المسببة للروائح الحادة، امتصاص العرق الزائد، وتفتيح تصبغات الإبطين، ليترك جسمك منتعشاً بعبير الغابة الخضراء، جافاً، وإبطيك ناصعي اللون طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية 48 ساعة بعطر نسمة الغابة المنعش:</strong> يمنح انتعاشاً طبيعياً وحماية قصوى من العرق والروائح.</li>
  <li><strong>تفتيح وتوحيد لون بشرة الإبطين باللوميسكين:</strong> يزيل التصبغات الداكنة الناتجة عن الاحتكاك.</li>
  <li><strong>تطهير وتهدئة بـ صمغ النحل النقي:</strong> يحمي البشرة من البكتيريا والالتهابات.</li>
  <li><strong>جفاف تام بـ حجر الشبة الطبيعي:</strong> يمتص العرق الزائد دون سد المسام.</li>
  <li><strong>خالي 100% من ألومنيوم كلوروهيدرات، الكحول، والبارابين:</strong> مجرب جلدياً وآمن للبشرة الحساسة.</li>
  <li><strong>عبوة مدمجة سعة 50 مل:</strong> حجم ممتاز ومناسب للاستخدام اليومي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> نظف منطقة الإبطين بالماء والصابون وجففها جيداً.</li>
  <li><strong>الخطوة الثانية:</strong> مرر البكرة 1-2 مرة على بشرة الإبط الجافة.</li>
  <li><strong>الخطوة الثالثة:</strong> دع السائل يجف ثوانٍ قبل ارتداء الملابس (يُستعمل مرة يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>معطر نسمة الغابة وحجر الشبة:</strong> ينعشان الحواس ويمتصان العرق طبيعياً.</li>
  <li><strong>صمغ النحل واللوميسكين:</strong> يطهران الجلد ويفتحان بقع التصبغات الداكنة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على بشرة الإبطين الجافة فقط.</li>
  <li>لا يوضع على الجلد المصاب بجروح مفتوحة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لمن يبحث عن رول اون بيزلين نسمة الغابة 50 مل بعطر انتعاشي مختلف وتفتيح الإبطين.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / مزيلات العرق الرول اون الانتعاشية المبيضة من بيزلين 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>مزيل عرق رول اون انتعاشي بعطر نسمة الغابة ومبيض للإبطين (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الإبطين (بما في ذلك البشرة الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>إبطان ناصعتا اللون، جافتان، منتعشتان بعبير الغابة ومحميتان</td></tr>
  <tr><th>الملمس</th><td>سائل رول اون خفيف ينفذ فورياً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر نسمة الغابة الخضراء المنعش (Forest Breeze)</td></tr>
  <tr><th>المكونات النشطة</th><td>حجر الشبة، صمغ النحل (Propolis)، لوميسكين، معطر نسمة الغابة</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد عطر نسمة الغابة واللوميسكين في بيزلين (Beesline Forest Breeze)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج رول اون بيزلين نسمة الغابة مشكلة رائحة العرق اليومية، اسمرار الإبطين، والحاجة إلى عطر انتعاشي مختلف ومميز.</p>

<h3>لماذا تنجح تركيبة نسمة الغابة واللوميسكين؟</h3>
<p>لأن المعطر الغابي يحيّد روائح العرق بجزيئات عطرية عميقة، بينما يفتّح اللوميسكين التصبغات بشكل آمن ومستمر.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق صباحاً على جلد جاف:</strong> ضع الرول اون فور الاستحمام وتجفيف الإبطين.<br>
2. <strong>تجنب الملابس الضيقة:</strong> التهوية الجيدة تمد فعالية المزيل لساعات أطول.<br>
3. <strong>الاستخدام المنتظم للتفتيح:</strong> استمرار الاستخدام 3-4 أسابيع يظهر نتائج التفتيح الواضحة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "العطور في مزيلات العرق تسبب حساسية دائمة."<br>
<strong>الحقيقة:</strong> معطر نسمة الغابة في بيزلين طبيعي خفيف ومجرب جلدياً وآمن لجميع أنواع البشرة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تلتقط جزيئات العطر الغابي الاستربين والمركبات الكبريتية المسببة للروائح في أقفاص جزيئية، فتحيّدها قبل تحررها.</p>"""

    faqs = [
        ("ما هو مزيل عرق نسمة من الغابة من بيزلين 50 مل؟", "هو رول اون من بيزلين بعطر نسمة الغابة الانتعاشي وصمغ النحل لحماية 48 ساعة وتفتيح الإبطين سعة 50 مل."),
        ("ما هي فوائد عطر نسمة الغابة وحجر الشبة واللوميسكين؟", "يمنح عطر الغابة انتعاشاً مميزاً، يمتص حجر الشبة العرق، ويفتّح اللوميسكين تصبغات الإبطين."),
        ("هل يوفر جفافاً وتفتيحاً لـ 48 ساعة؟", "نعم، مثبت سريرياً في تأمين جفاف تام وتفتيح التصبغات لـ 48 ساعة."),
        ("ما حجم العبوة؟", "تأتي لعلبة رول اون سعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "مرر البكرة 1-2 مرة على بشرة الإبط النظيفة والجافة، دع السائل يجف ثوانٍ قبل ارتداء الملابس يومياً."),
        ("هل هو خالي من ألومنيوم كلوروهيدرات والبارابين والكحول؟", "نعم، خالي 100% من ألومنيوم كلوروهيدرات والكحول والبارابين."),
        ("ما هو بلد صنع مزيل عرق بيزلين نسمة الغابة؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% من الوكيل المعتمد."),
        ("هل يترك أثراً على الملابس؟", "لا، قوام شفاف ينفذ فورياً دون ترك أي أثر."),
        ("ما هي رائحة مزيل عرق بيزلين نسمة الغابة؟", "يتميز برائحة الغابة الخضراء المنعشة والمميزة."),
        ("هل يهدئ تهيج الإبطين بعد الحلاقة؟", "نعم، صمغ النحل والألوفيرا يهدئان البشرة بعد الحلاقة."),
        ("هل العبوة 50 مل مناسبة للاستخدام اليومي؟", "نعم، حجم مدمج يكفي لعدة أسابيع من الاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل يناسب الرجال والنساء؟", "مناسب لجميع الفئات العمرية للنساء والرجال من سن 12 سنة."),
        ("هل العبوة محكمة الغلق؟", "نعم، تأتي بغطاء محكم الحماية."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل مرة يومياً صباحاً."),
        ("هل يمنع تكاثر البكتيريا المسببة للرائحة؟", "نعم، صمغ النحل وحجر الشبة يمنعان نمو البكتيريا."),
        ("هل يناسب البشرة الحساسة؟", "نعم، فورمولا طبيعية آمنة للبشرة الحساسة."),
        ("هل هو من أبرز منتجات بيزلين؟", "نعم، Forest Breeze Roll-On من أبرز منتجات مزيلات عرق بيزلين."),
        ("هل يمنح انتعاشاً وحيوية طوال اليوم؟", "نعم، يضمن انتعاشاً بعطر الغابة وجفافاً طوال اليوم."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة."),
        ("هل يجف سريعاً على البشرة؟", "نعم، يجف خلال ثوانٍ."),
        ("هل يترك الجلد طرياً؟", "نعم، يترك جلد الإبطين طرياً ومريحاً."),
        ("هل يصلح للسفر والتنقل؟", "نعم، حجم مدمج مثالي للسفر والتنقل."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Forest Breeze Roll-On Deodorant - 50 ml</strong> is a refreshing natural roll-on deodorant with an exceptional forest-inspired scent, providing 48-hour total dryness and antibacterial odor protection. Formulated with natural Alum Rock, Propolis, Lumiskin, and a Forest Breeze fragrance.</p>
<p>Beesline Forest Breeze Roll-On eliminates odor-causing bacteria, absorbs excess sweat, and brightens underarm hyperpigmentation, leaving you refreshed with a forest breeze scent, dry, and with brightened underarms all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>48-Hour Protection with Fresh Forest Breeze Scent:</strong> Natural freshness and maximum sweat and odor protection.</li>
  <li><strong>Underarm Brightening with Lumiskin:</strong> Fades dark hyperpigmentation from friction.</li>
  <li><strong>Purifying Propolis Defense:</strong> Protects skin from bacteria and inflammation.</li>
  <li><strong>Total Dryness with Natural Alum Rock:</strong> Absorbs excess sweat without clogging pores.</li>
  <li><strong>100% Free of Aluminum Chlorohydrate, Alcohol & Parabens:</strong> Dermatologically tested safe formula.</li>
  <li><strong>Compact 50ml Bottle:</strong> Ideal daily-use size.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Cleanse underarms with soap and water, pat dry.</li>
  <li><strong>Step 2:</strong> Roll applicator 1-2 times over dry underarm skin.</li>
  <li><strong>Step 3:</strong> Allow to dry for seconds before dressing (use once daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Forest Breeze Fragrance & Alum Rock:</strong> Neutralize odor and absorb sweat naturally.</li>
  <li><strong>Propolis & Lumiskin:</strong> Purify skin and fade dark underarm spots.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical dry underarm skin application only.</li>
  <li>Do not apply onto open wounds or broken skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Those seeking Beesline's 50ml Forest Breeze Roll-On with a unique refreshing scent and underarm brightening.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Personal Care / Beesline Refreshing Whitening Roll-On Deodorants 50ml</td></tr>
  <tr><th>Product Type</th><td>Forest Breeze Scented 48-Hour Brightening Roll-On Deodorant (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Underarm Skin Types (Including Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Brightened, dry, forest-fresh scented & protected armpits</td></tr>
  <tr><th>Texture</th><td>Smooth lightweight fast-drying roll-on fluid</td></tr>
  <tr><th>Fragrance</th><td>Refreshing Forest Breeze natural aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Alum Rock, Propolis, Lumiskin, Forest Breeze Fragrance</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Forest Breeze Terpene Odor Capture & Alum Rock Astringency</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Forest Breeze Roll-On resolves daily underarm odor, dark hyperpigmentation, and the need for a unique refreshing forest-inspired scent.</p>

<h3>Why choose Beesline Forest Breeze Roll-On?</h3>
<p>Forest-inspired terpene compounds in the fragrance capture sulfur odor molecules, while Alum Rock naturally tightens sweat gland pores.</p>"""

    en_faqs = [
        ("What is Beesline Forest Breeze Roll-On Deodorant - 50 ml?", "It is a Beesline roll-on with Forest Breeze scent, Propolis, and Lumiskin for 48-hour protection and underarm brightening."),
        ("What are the benefits of Forest Breeze fragrance, Alum Rock, and Lumiskin?", "Forest Breeze imparts unique freshness, Alum Rock absorbs sweat, and Lumiskin brightens underarm spots."),
        ("Does it provide 48-hour dryness and brightening?", "Yes, clinically proven for 48-hour total dryness and underarm brightening."),
        ("What volume is contained in this bottle?", "It comes in a compact 50ml roll-on bottle."),
        ("How do I apply it correctly?", "Roll 1-2 times onto clean, dry underarm skin, allow to dry, and dress."),
        ("Is it 100% free of aluminum chlorohydrate, alcohol, and parabens?", "Yes, 100% free of aluminum chlorohydrate, alcohol, and parabens."),
        ("Where is Beesline Forest Breeze manufactured?", "Proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it leave marks on clothes?", "No, invisible fluid absorbs instantly without leaving marks."),
        ("What scent does Beesline Forest Breeze have?", "Features a refreshing, unique forest-inspired natural aroma."),
        ("Does it soothe post-shaving irritation?", "Yes, Propolis and Aloe Vera calm skin irritation after shaving."),
        ("Is the 50ml bottle ideal for daily use?", "Yes, compact bottle lasts through weeks of daily use."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Is it suitable for men and women?", "Suitable for all ages, both men and women aged 12+."),
        ("Is the bottle cap leak-proof?", "Yes, features a secure screw-top cap."),
        ("How many times daily should I use it?", "Recommended for use once daily, in the morning."),
        ("Does it prevent odor-causing bacteria?", "Yes, Propolis and Alum Rock prevent odor-causing bacterial growth."),
        ("Is it safe for sensitive underarm skin?", "Yes, gentle natural formula safe for sensitive skin."),
        ("Is it one of Beesline's most popular roll-ons?", "Yes, Forest Breeze Roll-On is among Beesline's most popular deodorants."),
        ("Does it provide all-day freshness?", "Yes, guarantees all-day forest freshness, dryness, and brightened armpits."),
        ("Is the bottle recyclable?", "Yes, 100% recyclable bottle."),
        ("Does it dry quickly on skin?", "Yes, fluid dries in seconds."),
        ("Does it leave underarm skin soft?", "Yes, leaves underarm skin touchably soft."),
        ("Is it good for travel?", "Yes, compact size ideal for travel."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1883",
        "sku": "EK-1883",
        "gtin": "5281018003169",
        "brand": "Beesline",
        "ar": {
            "title": "مزيل عرق  نسمة من الغابة  من بيزلين 50 مل",
            "meta_title": "مزيل عرق بيزلين نسمة الغابة 50مل | إكليل أبها",
            "meta_description": "اشتري مزيل عرق نسمة من الغابة من بيزلين (50 مل). رول اون بعطر الغابة واللوميسكين لجفاف 48 ساعة وتفتيح الإبطين. أصلي لدى إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["بيزلين", "مزيل_عرق_بيزلين", "نسمة_الغابة", "تفتيح_الإبط", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Forest Breeze Roll-On Deodorant - 50 ml",
            "meta_title": "Beesline Forest Breeze Roll-On Deodorant 50ml | Ekleel Abha",
            "meta_description": "Buy original Beesline Forest Breeze Roll-On Deodorant (50 ml). Natural Alum Rock & Lumiskin brightening roll-on with forest scent. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["beesline", "forest_breeze_deodorant", "brightening_rollOn", "alum_rock", "ekleel_abha"]
        }
    }


def create_product_1884():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>صابونة نباتية لتنقية الوجه بصمغ النحل (Vegan Propolis Facial Purifying Soap)</strong> الصابونة النباتية الطبية الأصيلة من بيزلين المصممة لتنقية عميقة لمسام الوجه من الشوائب والمواد الدهنية الزائدة والبكتيريا المسببة لحب الشباب. يرتكز هذا الصابون الفاخر (Beesline Vegan Propolis Soap) على صمغ النحل النقي (Propolis) بنسبة عالية، وخلاصة زيت شجرة الشاي (Tea Tree Oil)، والنيم الطبيعي.</p>
<p>يعمل صابون بيزلين نباتي صمغ النحل على إزالة الزيوت الزائدة الدهنية، تطهير المسام من البكتيريا المسببة لحب الشباب والبثور، وتهدئة الاحمرار والالتهابات، ليترك بشرة الوجه ناعمة، صافية، مشرقة، ومحمية دون إزالة الترطيب الطبيعي.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنقية عميقة لمسام الوجه بصمغ النحل عالي التركيز:</strong> يزيل الدهون الزائدة والشوائب والبكتيريا بكفاءة.</li>
  <li><strong>مضاد قوي لحب الشباب والبثور بـ زيت شجرة الشاي:</strong> يقلص حجم البثور ويمنع ظهورها.</li>
  <li><strong>تهدئة وتلطيف الالتهابات والاحمرار:</strong> مركبات الفلافونويد بصمغ النحل تهدئ الجلد المتهيج.</li>
  <li><strong>صابونة نباتية 100% خالية من البارابين والكبريتات:</strong> آمنة للبشرة الحساسة والمختلطة.</li>
  <li><strong>توازن درجة حموضة بشرة الوجه:</strong> يحافظ على توازن pH الطبيعي للجلد.</li>
  <li><strong>مناسبة للاستخدام اليومي صباحاً ومساءً:</strong> تصنع جزءاً أساسياً من روتين العناية ببشرة الوجه.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (البلل):</strong> بللي وجهك بالماء الفاتر لفتح المسام قبل الاستعمال.</li>
  <li><strong>الخطوة الثانية (التغسيل):</strong> حركي صابونة بيزلين بين راحتي اليدين أو على قطعة إسفنج حتى تتكون رغوة كثيفة.</li>
  <li><strong>الخطوة الثالثة (المسح):</strong> دلكي الوجه بالرغوة بحركات دائرية خفيفة لـ 30-60 ثانية ثم اشطفي بالماء البارد (يُستعمل صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>صمغ النحل النقي (Propolis 15%):</strong> يطهر المسام ويقضي على الجراثيم والبكتيريا المسببة لحب الشباب.</li>
  <li><strong>زيت شجرة الشاي والنيم:</strong> يقلصان المسام ويمنعان تكاثر بكتيريا P. acnes.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي لتنظيف بشرة الوجه فقط.</li>
  <li>تجنبي التلامس مع العينين ويُستعمل الماء الفاتر للشطف الفوري.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لأصحاب البشرة الدهنية والمختلطة المعرضة لحب الشباب الباحثين عن صابونة بيزلين نباتية بصمغ النحل للتنظيف العميق.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / صابونات بيزلين النباتية الطبية لتنقية وتطهير مسام الوجه</td></tr>
  <tr><th>نوع المنتج</th><td>صابونة نباتية طبية لتنقية مسام الوجه بصمغ النحل عالي التركيز</td></tr>
  <tr><th>الحجم/الوزن</th><td>حسب مواصفات العبوة</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الدهنية والمختلطة والمعرضة لحب الشباب (مناسبة للبشرة الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه صافٍ، نقي، خالٍ من الدهون الزائدة والشوائب والبثور</td></tr>
  <tr><th>الملمس</th><td>صابونة نباتية صلبة تنتج رغوة لطيفة كثيفة</td></tr>
  <tr><th>العطر</th><td>عطر صمغ النحل وزيت الشاي الطبي اللطيف</td></tr>
  <tr><th>المكونات النشطة</th><td>صمغ النحل (Propolis)، زيت شجرة الشاي، النيم الطبيعي</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>المراهقون والبالغون (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد صمغ النحل وزيت شجرة الشاي في صابونة بيزلين (Beesline Propolis Soap)</h2>

<h3>ما هي المشكلة التي تحلها هذه الصابونة؟</h3>
<p>تعالج صابونة بيزلين نباتية صمغ النحل مشكلة انسداد المسام، تراكم الدهون والزيوت الزائدة، وحب الشباب والبثور لبشرة الوجه الدهنية والمختلطة.</p>

<h3>لماذا تنجح تركيبة صمغ النحل وزيت شجرة الشاي؟</h3>
<p>لأن الفلافونويدات والبيوفلافونويدات بصمغ النحل تثبط نمو P. acnes، في حين يقلص التيربينول في زيت شجرة الشاي المسام ويمنع تكاثر البكتيريا.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الغسل مرتين يومياً بماء فاتر:</strong> صباحاً ومساءً لمنع تراكم الدهون والبكتيريا.<br>
2. <strong>تجنب الماء الساخن جداً:</strong> يفتح المسام بشكل مبالغ ويزيد إنتاج الدهون.<br>
3. <strong>استخدام مرطب خفيف بعد الغسيل:</strong> يحافظ على توازن الترطيب بعد التنظيف العميق.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الصابون يزيل حب الشباب فوراً في يوم واحد."<br>
<strong>الحقيقة:</strong> صابونة بيزلين تمنع ظهور بثور جديدة تدريجياً مع الاستخدام المنتظم لـ 3-4 أسابيع.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يثبط الكايمبيرول والكيرسيتين في Propolis الـ Cyclooxygenase المسؤولة عن الالتهاب، بينما يعطل Terpinen-4-ol في Tea Tree بروتينات غشاء بكتيريا P. acnes.</p>"""

    faqs = [
        ("ما هي صابونة نباتية لتنقية الوجه بصمغ النحل من بيزلين؟", "هي صابونة نباتية طبية من بيزلين بصمغ النحل وزيت شجرة الشاي لتنقية عميقة لمسام الوجه ومكافحة حب الشباب."),
        ("ما هي فوائد صمغ النحل وزيت شجرة الشاي والنيم؟", "يطهر صمغ النحل المسام، يقلص زيت شجرة الشاي البثور ويمنعها، ويهدئ النيم الالتهابات والاحمرار."),
        ("هل تعالج حب الشباب والبثور بكفاءة؟", "نعم، مثبت سريرياً في التقليل من حب الشباب والبثور مع الاستخدام المنتظم."),
        ("هل تناسب البشرة الدهنية والمختلطة؟", "نعم، مصممة خصيصاً للبشرة الدهنية والمختلطة المعرضة لحب الشباب."),
        ("كيف تُستخدم الصابونة بالشكل الصحيح؟", "بللي الوجه، كوّني رغوة وادلكي الوجه 30-60 ثانية بحركات دائرية ثم اشطفي بالماء البارد صباحاً ومساءً."),
        ("هل هي نباتية 100% وخالية من البارابين والكبريتات؟", "نعم، صابونة نباتية 100% خالية من البارابين والكبريتات والإضافات الكيميائية الضارة."),
        ("ما هو بلد صنع صابونة بيزلين نباتية صمغ النحل؟", "صُنعت بفخر في لبنان بواسطة مختبرات بيزلين (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% من الوكيل المعتمد."),
        ("هل تناسب البشرة الحساسة أيضاً؟", "نعم، فورمولا نباتية لطيفة مناسبة للبشرة الحساسة."),
        ("ما هي رائحة صابونة بيزلين نباتية صمغ النحل؟", "تتميز برائحة صمغ النحل وزيت شجرة الشاي الطبية اللطيفة."),
        ("هل تنتج رغوة كثيفة وغنية؟", "نعم، تنتج رغوة لطيفة كثيفة تنظف المسام بعمق."),
        ("هل تتحكم في الدهون الزائدة لبشرة الوجه؟", "نعم، تزيل الزيوت الزائدة وتوازن إنتاجها."),
        ("كيف أحتفظ بالصابونة؟", "تُحفظ في مكان جاف بعيداً عن الرطوبة الزائدة."),
        ("هل يُفضل استخدامها صباحاً أو مساءً أو كلاهما؟", "يُستعمل مرتين يومياً صباحاً ومساءً لنتائج أفضل."),
        ("هل تهدئ احمرار الوجه والبثور الملتهبة؟", "نعم، الفلافونويدات بصمغ النحل تهدئ الالتهابات والاحمرار."),
        ("هل تمنع ظهور بثور جديدة مستقبلاً؟", "نعم، الاستخدام المنتظم يمنع تكاثر بكتيريا حب الشباب."),
        ("كم يستغرق الاستخدام لرؤية نتائج واضحة؟", "تظهر نتائج الصفاء والتنقية تدريجياً خلال 3-4 أسابيع من الاستخدام المنتظم."),
        ("هل تناسب المراهقين الذين يعانون من حب شباب الأكنى؟", "نعم، مناسبة للمراهقين والبالغين من سن 12 سنة."),
        ("هل هي الصابونة النباتية الأكثر طلباً لبيزلين؟", "نعم، Propolis Facial Purifying Soap من أبرز صابونات الوجه من بيزلين."),
        ("هل تترك الوجه مشرقاً وصافياً بعد الغسيل؟", "نعم، تترك الوجه صافياً ومشرقاً خالياً من الدهون والشوائب."),
        ("هل العبوة مناسبة للاستخدام الشهري؟", "نعم، صابونة صلبة تدوم فترة طويلة من الاستخدام اليومي."),
        ("هل تحافظ على الترطيب الطبيعي للجلد؟", "نعم، توازن pH يحافظ على الترطيب الطبيعي دون جفاف."),
        ("هل تناسب البشرة المعرضة للشمس؟", "يُفضل استخدام واقي شمس بعد التنظيف في النهار."),
        ("هل تزيل المكياج الخفيف؟", "تُستعمل بعد مزيل المكياج لتنظيف المسام بعمق."),
        ("هل تتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، تتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Vegan Propolis Facial Purifying Soap</strong> by Beesline is a medical-grade vegan facial bar soap engineered for deep pore purification, eliminating excess sebum, bacteria, and acne-causing impurities. Formulated with high-concentration Propolis, Tea Tree Oil, and natural Neem.</p>
<p>Beesline Vegan Propolis Soap removes excess sebaceous oils, purifies pores from acne-causing bacteria and blemishes, and soothes redness and inflammation, leaving facial skin soft, clear, radiant, and protected without stripping natural moisture.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Deep Pore Purification with High-Concentration Propolis:</strong> Removes excess sebum, impurities, and bacteria.</li>
  <li><strong>Powerful Anti-Acne with Tea Tree Oil:</strong> Shrinks blemishes and prevents future breakouts.</li>
  <li><strong>Soothes Inflammation & Redness:</strong> Propolis flavonoids calm irritated acne-prone skin.</li>
  <li><strong>100% Vegan, Paraben-Free & Sulfate-Free:</strong> Safe for sensitive and combination skin.</li>
  <li><strong>pH-Balancing Formula:</strong> Maintains skin's natural pH balance.</li>
  <li><strong>Suitable for Twice Daily Use:</strong> Essential part of daily facial skincare routine.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet face with warm water to open pores before use.</li>
  <li><strong>Step 2 (Lather):</strong> Work Beesline soap between palms or on a sponge to create a rich lather.</li>
  <li><strong>Step 3 (Cleanse):</strong> Massage face with lather in circular motions for 30-60 seconds, rinse with cold water (use morning and evening).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>High-Concentration Propolis (15%):</strong> Purifies pores and eliminates acne-causing bacteria.</li>
  <li><strong>Tea Tree Oil & Neem:</strong> Shrink pores and prevent P. acnes bacterial proliferation.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial skin cleansing only.</li>
  <li>Avoid eye contact; rinse immediately with warm water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Those with oily, combination, or acne-prone skin seeking Beesline's Vegan Propolis Facial Purifying Soap for deep pore cleansing.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Skincare / Beesline Vegan Medical Facial Purifying Soaps</td></tr>
  <tr><th>Product Type</th><td>Vegan High-Concentration Propolis & Tea Tree Deep Pore Facial Soap</td></tr>
  <tr><th>Volume/Weight</th><td>As per packaging specifications</td></tr>
  <tr><th>Skin/Hair Type</th><td>Oily, Combination & Acne-Prone Skin (Suitable for Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Clear, purified, oil-free, blemish-free, radiant facial skin</td></tr>
  <tr><th>Texture</th><td>Firm vegan bar soap producing gentle rich lather</td></tr>
  <tr><th>Fragrance</th><td>Subtle medical Propolis & Tea Tree natural scent</td></tr>
  <tr><th>Active Ingredients</th><td>Propolis, Tea Tree Oil, Natural Neem</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Propolis Kaempferol Anti-Inflammation & Tea Tree Terpinen Antibacterial Action</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Vegan Propolis Facial Soap resolves clogged pores, excess sebaceous oil, acne blemishes, and facial bacterial infections.</p>

<h3>Why choose Beesline Vegan Propolis Soap?</h3>
<p>Propolis Kaempferol inhibits Cyclooxygenase inflammation enzymes, while Tea Tree Terpinen-4-ol disrupts P. acnes bacterial cell membranes.</p>"""

    en_faqs = [
        ("What is the Vegan Propolis Facial Purifying Soap by Beesline?", "It is a medical-grade vegan bar soap with Propolis and Tea Tree Oil for deep pore purification and acne control."),
        ("What are the benefits of Propolis, Tea Tree Oil, and Neem?", "Propolis purifies pores, Tea Tree Oil shrinks blemishes, and Neem soothes inflammation and redness."),
        ("Does it effectively treat acne and blemishes?", "Yes, clinically proven to reduce acne and blemishes with regular use over 3-4 weeks."),
        ("Is it suitable for oily and combination skin?", "Yes, specifically designed for oily and combination acne-prone facial skin."),
        ("How do I use the soap correctly?", "Wet face, lather between hands, massage face in circles for 30-60 seconds, rinse with cold water morning and evening."),
        ("Is it 100% vegan, paraben-free, and sulfate-free?", "Yes, 100% vegan formula free of parabens, sulfates, and harmful chemical additives."),
        ("Where is Beesline Vegan Propolis Soap manufactured?", "Proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Is it suitable for sensitive skin too?", "Yes, gentle vegan formula suitable for sensitive skin."),
        ("What does Beesline Vegan Propolis Soap smell like?", "Features a subtle, pleasant medical Propolis and Tea Tree natural scent."),
        ("Does it produce a rich lather?", "Yes, produces a gentle rich lather that deep-cleanses pores."),
        ("Does it control excess facial oiliness?", "Yes, removes excess sebum and balances sebaceous production."),
        ("How should I store the soap?", "Store in a dry place away from excess moisture."),
        ("Should I use it morning, evening, or both?", "Use twice daily, morning and evening, for best results."),
        ("Does it calm red inflamed blemishes?", "Yes, Propolis flavonoids soothe inflammation and reduce redness."),
        ("Does it prevent future breakouts?", "Yes, regular use prevents acne-causing bacteria proliferation."),
        ("How long does it take to see visible results?", "Visible skin clarity appears gradually within 3-4 weeks of regular use."),
        ("Is it suitable for teens with acne?", "Yes, suitable for teens and adults aged 12+."),
        ("Is it Beesline's most popular facial soap?", "Yes, Propolis Facial Purifying Soap is among Beesline's most popular facial soaps."),
        ("Does it leave skin clear and radiant after washing?", "Yes, leaves facial skin clear, radiant, and free of oil and impurities."),
        ("Does a bar last a long time?", "Yes, a solid bar lasts through extended periods of daily use."),
        ("Does it maintain natural skin moisture?", "Yes, pH-balancing formula preserves natural hydration without causing dryness."),
        ("Is it suitable for sun-exposed skin?", "Apply sunscreen after daytime cleansing for sun protection."),
        ("Can it remove light makeup?", "Use after a makeup remover to deep-cleanse pores effectively."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1884",
        "sku": "EK-1884",
        "gtin": "5281018004036",
        "brand": "Beesline",
        "ar": {
            "title": "صابونة نباتية لتنقية الوجه بصمغ النحل",
            "meta_title": "صابونة بيزلين نباتية بصمغ النحل لتنقية الوجه | إكليل أبها",
            "meta_description": "اشتري صابونة بيزلين نباتية بصمغ النحل لتنقية الوجه. صابون طبي نباتي بصمغ النحل وزيت الشاي لتنقية مسام الوجه ومكافحة حب الشباب. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["بيزلين", "صابون_صمغ_النحل", "صابون_وجه_نباتي", "تنقية_المسام", "إكليل_أبها"]
        },
        "en": {
            "title": "Vegan Propolis Facial Purifying Soap",
            "meta_title": "Beesline Vegan Propolis Facial Purifying Soap | Ekleel Abha",
            "meta_description": "Buy original Beesline Vegan Propolis Facial Purifying Soap. Medical vegan Propolis & Tea Tree deep pore facial soap. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["beesline", "propolis_soap", "vegan_face_soap", "acne_soap", "ekleel_abha"]
        }
    }


def create_product_1886():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>صابون تفتيح الوجه بالتوت البري من بيزلين 85جم (Beesline Cranberry Facial Whitening Soap - 85g)</strong> الصابونة التفتيحية الطبية الأصيلة من بيزلين المصممة لتفتيح بشرة الوجه، إزالة التصبغات الداكنة وبقع الشمس، وتوحيد لون البشرة بتقنية التوت البري الفائقة في التجديد والتفتيح. يرتكز هذا الصابون الفاخر (Beesline Cranberry Whitening Soap 85g) على خلاصة التوت البري الغنية بمضادات الأكسدة (Cranberry Extract)، اللوميسكين المبيض (Lumiskin)، وصمغ النحل النقي (Propolis).</p>
<p>يعمل صابون بيزلين بالتوت البري على تفتيح بقع الشمس والتصبغات الداكنة، تقشير خلايا الجلد الميتة بلطف، وتغذية وتجديد بشرة الوجه بمضادات الأكسدة القوية، ليترك وجهك ناصعاً، موحد اللون، مشرقاً، وأكثر شباباً من اليوم الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح قوي وسريع لبقع الشمس والتصبغات الداكنة:</strong> خلاصة التوت البري واللوميسكين يفتحان البشرة ويوحدانها.</li>
  <li><strong>تقشير لطيف لخلايا الجلد الميتة:</strong> يجدد البشرة ويكشف طبقة مشرقة جديدة أسفلها.</li>
  <li><strong>غني بمضادات الأكسدة القوية:</strong> خلاصة التوت البري تحمي من التلف الجذري الحر وتبطئ التشيّخ.</li>
  <li><strong>تطهير وتهدئة بـ صمغ النحل النقي:</strong> يطهر المسام ويهدئ الجلد المتهيج.</li>
  <li><strong>صابونة طبية آمنة خالية من الهيدروكينون والبارابين:</strong> تفتيح آمن دون مواد كيميائية ضارة.</li>
  <li><strong>عبوة 85 جم:</strong> حجم اقتصادي مناسب لعدة أشهر من الاستخدام اليومي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (البلل):</strong> بللي وجهك بالماء الفاتر لفتح المسام قبل الاستعمال.</li>
  <li><strong>الخطوة الثانية (التغسيل):</strong> حركي صابونة بيزلين بالتوت البري بين راحتي اليدين حتى تتكون رغوة كثيفة.</li>
  <li><strong>الخطوة الثالثة (المسح):</strong> دلكي الوجه بالرغوة بحركات دائرية خفيفة لـ 30-60 ثانية ثم اشطفي بالماء البارد (يُستعمل صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة التوت البري ومضادات الأكسدة (Cranberry Extract & Antioxidants):</strong> يفتحان التصبغات ويحميان الجلد من التلف.</li>
  <li><strong>مركب اللوميسكين وصمغ النحل:</strong> يثبطان إنزيم التايروسينيز ويطهران المسام.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي لتنظيف وتفتيح بشرة الوجه فقط.</li>
  <li>تجنبي التلامس مع العينين ويُستعمل الماء الفاتر للشطف الفوري.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من تصبغات الوجه وبقع الشمس وتبحث عن صابون تفتيح بيزلين بالتوت البري 85جم لنتائج مشرقة سريعة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / صابونات بيزلين الطبية التفتيحية لوجه مشرق ومتوحد اللون 85جم</td></tr>
  <tr><th>نوع المنتج</th><td>صابونة طبية لتفتيح الوجه بالتوت البري واللوميسكين وصمغ النحل (85جم)</td></tr>
  <tr><th>الحجم/الوزن</th><td>85 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (بما في ذلك البشرة ذات التصبغات والبشرة الدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناصع، موحد اللون، خالٍ من بقع الشمس والتصبغات ومشرق</td></tr>
  <tr><th>الملمس</th><td>صابونة صلبة تنتج رغوة لطيفة كثيفة</td></tr>
  <tr><th>العطر</th><td>عطر التوت البري الفاكهي الناعم</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة التوت البري، لوميسكين، صمغ النحل (Propolis)، مضادات الأكسدة</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد التوت البري واللوميسكين في صابون بيزلين المبيض (Beesline Cranberry Whitening)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج صابون بيزلين بالتوت البري مشكلة تصبغات الوجه الداكنة، بقع الشمس، وعدم توحد لون البشرة.</p>

<h3>لماذا تنجح تركيبة التوت البري واللوميسكين للتفتيح؟</h3>
<p>لأن البروانثوسيانيدين بالتوت البري تثبط إنتاج الميلانين وتحمي الكولاجين، بينما يمنع اللوميسكين التايروسينيز بأمان.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الغسل مرتين يومياً بماء فاتر ثم بارد:</strong> يفتح الماء الفاتر المسام ويغلقها البارد بعد التنظيف.<br>
2. <strong>استخدام واقي شمس SPF 30+ بعد التنظيف:</strong> لمنع عودة التصبغات بعد التفتيح.<br>
3. <strong>الاستمرار لـ 4-6 أسابيع:</strong> يظهر توحيد اللون المستمر مع الاستخدام المنتظم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "صابون التفتيح يتلف الجلد ويجعله أكثر حساسية للشمس."<br>
<strong>الحقيقة:</strong> صابون بيزلين بالتوت البري غني بمضادات الأكسدة التي تحمي الجلد من أشعة الشمس وتبطئ التشيّخ.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط البروانثوسيانيدين بالتوت البري نشاط MMP-1 المسؤول عن تدمير الكولاجين، بينما يثبط اللوميسكين مسارات PKC للميلانين.</p>"""

    faqs = [
        ("ما هو صابون تفتيح الوجه بالتوت البري من بيزلين 85جم؟", "هو صابون طبي من بيزلين بخلاصة التوت البري واللوميسكين وصمغ النحل لتفتيح الوجه وإزالة بقع الشمس والتصبغات 85 جم."),
        ("ما هي فوائد التوت البري واللوميسكين وصمغ النحل؟", "يفتّح التوت البري التصبغات ويحمي الكولاجين، يثبط اللوميسكين الميلامين، ويطهر صمغ النحل المسام."),
        ("هل يفتّح بقع الشمس والتصبغات الداكنة بسرعة؟", "نعم، مثبت سريرياً في التفتيح التدريجي لبقع الشمس وتوحيد لون البشرة مع الاستخدام المنتظم."),
        ("ما حجم الصابونة؟", "تأتي بوزن 85 جم."),
        ("كيف تُستخدم الصابونة بالشكل الصحيح؟", "بللي الوجه بالماء الفاتر، كوّني رغوة وادلكي الوجه 30-60 ثانية بحركات دائرية ثم اشطفي بالماء البارد مرتين يومياً."),
        ("هل هي خالية من الهيدروكينون والبارابين؟", "نعم، تفتيح آمن خالٍ 100% من الهيدروكينون والبارابين والكيميائيات الضارة."),
        ("ما هو بلد صنع صابون بيزلين بالتوت البري؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% من الوكيل المعتمد."),
        ("هل تناسب جميع أنواع بشرة الوجه؟", "نعم، مناسبة لجميع أنواع البشرة بما في ذلك البشرة الدهنية والمختلطة."),
        ("ما هي رائحة صابون بيزلين بالتوت البري؟", "تتميز برائحة التوت البري الفاكهية الناعمة والمحببة."),
        ("هل تنتج رغوة كثيفة وغنية؟", "نعم، تنتج رغوة لطيفة كثيفة تنظف المسام وتفتّح البشرة."),
        ("هل تقشّر خلايا الجلد الميتة بلطف؟", "نعم، تقشير لطيف يكشف طبقة بشرة جديدة أكثر إشراقاً."),
        ("كيف أحتفظ بالصابونة؟", "تُحفظ في مكان جاف بعيداً عن الرطوبة الزائدة."),
        ("هل يُفضل استخدامها صباحاً أو مساءً أو كلاهما؟", "يُستعمل مرتين يومياً صباحاً ومساءً لنتائج تفتيح أسرع."),
        ("هل تهدئ التهيج والاحمرار؟", "نعم، صمغ النحل يهدئ الالتهابات والاحمرار."),
        ("كم يستغرق التفتيح لرؤية نتائج واضحة؟", "تظهر نتائج التفتيح التدريجي خلال 4-6 أسابيع من الاستخدام المنتظم."),
        ("هل تمنع ظهور تصبغات جديدة؟", "يُفضل استخدام واقي الشمس بعدها لمنع عودة التصبغات."),
        ("هل تناسب المراهقين والبالغين؟", "نعم، مناسبة للمراهقين والبالغين من سن 12 سنة."),
        ("هل هي الصابونة التفتيحية الأكثر طلباً لبيزلين؟", "نعم، Cranberry Whitening Soap من أبرز صابونات التفتيح من بيزلين."),
        ("هل تترك الوجه ناصعاً ومشرقاً بعد الغسيل؟", "نعم، تترك الوجه ناصعاً ومشرقاً وموحد اللون."),
        ("هل صابونة 85 جم تدوم طويلاً؟", "نعم، صابونة صلبة 85 جم تدوم عدة أشهر من الاستخدام اليومي."),
        ("هل تحمي من أكسدة الشمس؟", "نعم، مضادات الأكسدة بالتوت البري تحمي من التلف الشمسي."),
        ("هل تصلح كجزء من روتين العناية المتكامل؟", "نعم، تكمل صابونة بيزلين مراحل التنظيف والتفتيح في الروتين اليومي."),
        ("هل تغني عن الكريمات التفتيحية؟", "تعمل الصابونة بشكل مكمل مع كريمات ومصل التفتيح من بيزلين لنتائج أفضل."),
        ("هل تتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، تتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Cranberry Facial Whitening Soap - 85g</strong> is the medical whitening soap engineered to brighten facial skin, eliminate dark sun spots and hyperpigmentation, and unify skin tone using a powerful Cranberry Extract technology. Formulated with antioxidant-rich Cranberry extract, Lumiskin whitening compound, and pure Propolis.</p>
<p>Beesline Cranberry Soap lightens sun spots and dark hyperpigmentation, gently exfoliates dead skin cells, and nourishes facial skin with powerful antioxidants, leaving your face radiant, even-toned, glowing, and visibly younger from day one.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Powerful & Fast Whitening of Sun Spots & Dark Hyperpigmentation:</strong> Cranberry extract and Lumiskin brighten and unify skin.</li>
  <li><strong>Gentle Exfoliation of Dead Skin Cells:</strong> Renews skin and reveals a brighter, fresher layer beneath.</li>
  <li><strong>Rich in Powerful Antioxidants:</strong> Cranberry extract shields against free radical damage and slows aging.</li>
  <li><strong>Purifying Propolis Defense:</strong> Cleanses pores and soothes irritated skin.</li>
  <li><strong>Safe Medical Formula, Free of Hydroquinone & Parabens:</strong> Safe brightening without harmful chemicals.</li>
  <li><strong>85g Bar:</strong> Economical size lasting months of daily use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet face with warm water to open pores before use.</li>
  <li><strong>Step 2 (Lather):</strong> Work Beesline Cranberry soap between palms to create a rich lather.</li>
  <li><strong>Step 3 (Cleanse):</strong> Massage lather onto face in circular motions for 30-60 seconds, rinse with cold water (use morning and evening).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Cranberry Extract & Antioxidants:</strong> Brighten hyperpigmentation and protect collagen from damage.</li>
  <li><strong>Lumiskin & Propolis:</strong> Inhibit tyrosinase melanin synthesis and purify pores.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial skin cleansing and whitening only.</li>
  <li>Avoid eye contact; rinse immediately with warm water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with facial hyperpigmentation and sun spots seeking Beesline's 85g Cranberry Facial Whitening Soap for fast brightening results.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Skincare / Beesline Medical Facial Whitening Soaps 85g</td></tr>
  <tr><th>Product Type</th><td>Medical Cranberry Extract & Lumiskin Facial Whitening Bar Soap (85g)</td></tr>
  <tr><th>Volume/Weight</th><td>85 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Including Hyperpigmented & Oily Skin)</td></tr>
  <tr><th>Finish</th><td>Brightened, even-toned, sun-spot-free, radiant facial skin</td></tr>
  <tr><th>Texture</th><td>Firm bar soap producing gentle rich brightening lather</td></tr>
  <tr><th>Fragrance</th><td>Soft fruity Cranberry natural scent</td></tr>
  <tr><th>Active Ingredients</th><td>Cranberry Extract, Lumiskin, Propolis, Antioxidants</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>All Ages (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Cranberry Proanthocyanidins Melanin Suppression & Lumiskin PKC Inhibition</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Cranberry Facial Whitening Soap resolves dark facial hyperpigmentation, sun spots, and uneven skin tone.</p>

<h3>Why choose Beesline Cranberry Whitening Soap?</h3>
<p>Cranberry Proanthocyanidins inhibit melanin production and protect collagen from MMP-1 damage, while Lumiskin safely blocks PKC melanin pathways.</p>"""

    en_faqs = [
        ("What is Beesline Cranberry Facial Whitening Soap - 85g?", "It is a medical whitening bar soap with Cranberry extract, Lumiskin, and Propolis to brighten facial skin and fade sun spots."),
        ("What are the benefits of Cranberry extract, Lumiskin, and Propolis?", "Cranberry brightens spots and protects collagen, Lumiskin inhibits melanin, and Propolis purifies pores."),
        ("Does it brighten sun spots and dark hyperpigmentation quickly?", "Yes, clinically proven to progressively brighten sun spots and unify skin tone with regular use."),
        ("What size is this soap bar?", "It comes in an 85g bar."),
        ("How do I use the soap correctly?", "Wet face, create lather, massage in circles for 30-60 seconds, rinse with cold water morning and evening."),
        ("Is it free of hydroquinone and parabens?", "Yes, 100% safe brightening formula free of hydroquinone, parabens, and harmful chemicals."),
        ("Where is Beesline Cranberry Soap manufactured?", "Proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Is it suitable for all facial skin types?", "Yes, suitable for all skin types including oily and combination skin."),
        ("What does Beesline Cranberry Soap smell like?", "Features a soft, pleasant fruity Cranberry natural scent."),
        ("Does it produce a rich lather?", "Yes, produces a gentle rich brightening lather."),
        ("Does it gently exfoliate dead skin cells?", "Yes, gentle exfoliation reveals a brighter, fresher skin layer."),
        ("How should I store the soap?", "Store in a dry place away from excess moisture."),
        ("Should I use it morning, evening, or both?", "Use twice daily, morning and evening, for faster brightening results."),
        ("Does it calm irritation and redness?", "Yes, Propolis soothes inflammation and redness."),
        ("How long does brightening take?", "Visible brightening results appear gradually within 4-6 weeks of regular use."),
        ("Does it prevent new dark spots?", "Apply sunscreen after use to prevent sun-induced spot recurrence."),
        ("Is it suitable for teens and adults?", "Yes, suitable for teens and adults aged 12+."),
        ("Is it Beesline's most popular whitening soap?", "Yes, Cranberry Whitening Soap is among Beesline's most popular facial soaps."),
        ("Does it leave skin radiant after washing?", "Yes, leaves facial skin radiant, even-toned, and sun-spot-free."),
        ("Does an 85g bar last a long time?", "Yes, a solid 85g bar lasts months of daily use."),
        ("Does it protect skin from sun oxidation?", "Yes, Cranberry antioxidants shield from UV-induced free radical damage."),
        ("Is it part of a complete skincare routine?", "Yes, complements other Beesline whitening creams and serums in a full routine."),
        ("Does it replace whitening creams?", "Works complementarily with Beesline whitening creams for enhanced results."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1886",
        "sku": "EK-1886",
        "gtin": "5281018087008",
        "brand": "Beesline",
        "ar": {
            "title": "صابون تفتيح الوجه بالتوت البري من بيزلين 85جم",
            "meta_title": "صابون تفتيح الوجه بالتوت البري بيزلين 85جم | إكليل أبها",
            "meta_description": "اشتري صابون تفتيح الوجه بالتوت البري من بيزلين (85 جم). صابون طبي بالتوت البري واللوميسكين لتفتيح وتوحيد لون بشرة الوجه. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["بيزلين", "صابون_تفتيح_بيزلين", "صابون_التوت_البري", "تفتيح_الوجه", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Cranberry Facial Whitening Soap - 85g",
            "meta_title": "Beesline Cranberry Facial Whitening Soap 85g | Ekleel Abha",
            "meta_description": "Buy original Beesline Cranberry Facial Whitening Soap (85g). Cranberry & Lumiskin medical whitening bar for brightening and unifying facial skin. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["beesline", "cranberry_soap", "whitening_soap", "facial_soap", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 34 builders complete")
