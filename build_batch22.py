import json, os

def build_clere_body_cream(prod_id, title_ar, title_en, active_ar, active_en, gtin, img_slug):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{title_ar}</strong> المستحضر الطبيعي الأيقوني الفاخر لإعادة النعومة، الترطيب المكثف، والوقاية من الجفاف لبشرة الجسم بالكامل. يرتكز هذا الكريم الغني من كلير (Clere Body Cream) على تركيبة الثلاثية من الجليسرين النقّي، فيتامين A، وفيتامين E، مع خلاصة {active_ar}، حيث ينفذ في عمق خلايا الجلد ليمنحكِ ترطيباً تدوم فاعليته لـ 48 ساعة متواصلة.</p>
<p>يمتاز كريم كلير بقوام كريمي فاخر يمتص فورياً في البشرة دون ترك أي أثر دهني لزج، مما يمنع جفاف الجلد والتطير ويرمم المناطق الخشنة بالأكواع والركب لترك جسمكِ ناعماً كالحرير ومشبعاً بالنعومة والعبير.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب عميق لـ 48 ساعة متواصلة:</strong> يزود ألياف البشرة بالمرطبات الشديدة لمنع الجفاف والشد.</li>
  <li><strong>غني بالفيتامينات A و E والجليسرين:</strong> يغذي خلايا الجلد عميقاً ويحسن مرونة ونعومة البشرة.</li>
  <li><strong>مدعم بـ {active_ar}:</strong> يمنح الجلد ملمساً مخملياً ونضارة استوائية زكية.</li>
  <li><strong>قوام غير دهني وسريع الامتصاص:</strong> ينفذ في خلايا الجلد فورياً دون لزوجة زيتيّة ثقيلة.</li>
  <li><strong>تنعيم الأكواع والركب والكعبين:</strong> يرطب الأماكن الأكثر جفافاً ويزيل التطير والقشور.</li>
  <li><strong>عبوة وافرة سعة 500 مل:</strong> حجم عائلي ممتاز يضمن عناية وتغذية مستمرة يومياً.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> استحممي بماء فاتر وجففي بشرتكِ بلطف.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي كمية وافرة من كريم كلير على كامل الجسم، الأكواع، والركب.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي بحركات دائرية خفيفة حتى الامتصاص الكامل (يُستعمل 1 إلى 2 مرة يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الجليسرين النقي وفيتامينات A & E:</strong> تحفظ الماء في خلايا الجلد وتزيد المرونة.</li>
  <li><strong>خلاصة {active_ar}:</strong> تطري الجلد وتمنحه عبقاً ناعماً ورطباً.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على بشرة الجسم فقط.</li>
  <li>تجنبي ملامسة الكريم المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة وعائلة تفتش عن كريم غني بـ {active_ar} وفيتامينات A & E لترطيب الجسم لـ 48 ساعة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كلير (Clere)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات ترطيب الجسم الغنية المغذية</td></tr>
  <tr><th>نوع المنتج</th><td>كريم ترطيب وتغذية الجسم 48 ساعة (500ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (الجافة، العادية، الشديدة الجفاف)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة، مخملية، مرطبة لـ 48 ساعة وخالية من القشور</td></tr>
  <tr><th>الملمس</th><td>كريمي غني ناعم يذوب وينفذ بالبشرة</td></tr>
  <tr><th>العطر</th><td>عطر {active_ar} الاستوائي الزكي</td></tr>
  <tr><th>المكونات النشطة</th><td>جليسرين، فيتامين A، فيتامين E، خلاصة {active_ar}</td></tr>
  <tr><th>بلد المنشأ</th><td>جنوب إفريقيا / المملكة العربية السعودية (Amka)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Amka Products / Clere</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد الجليسرين وفيتامينات A & E من كلير (Clere Cream)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم كلير مشكلة جفاف بشرة الجسم شديدة الجفاف، خشونة الأكواع والركب، والتطير الناتج عن الجو الجاف.</p>

<h3>لماذا تنجح تركيبة كلير 48 ساعة؟</h3>
<p>لأن الجليسرين الثلاثي مع فيتامينات A و E يشكل حجاب ترطيب ينفذ حتى الطبقة العميقة، ويمنع تبخر الماء لـ 48 ساعة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام بعد الاستحمام:</strong> ضعي الكريم فورياً بعد الاستحمام لحبس الترطيب.<br>
2. <strong>التركيز على الأكواع والركب:</strong> دلكي المناطق الجافة يومياً قبل النوم.<br>
3. <strong>الاستخدام العائلي:</strong> جعل ترطيب كلير روتيناً يومياً للأبناء والوالدين.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات الجسم سعة 500 مل تكون ثقيلة ولزجة جداً."<br>
<strong>الحقيقة:</strong> كريم كلير مصمم بتركيبة خفيفة متوازنة تمتص فورياً دون لزوجة زيتيّة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتكامل الفيتامينات A و E مع الجليسرين في بناء أغشية الليبيدات الجلدي، مما يقلل معدل التبخر الجلدي (TEWL) بنسبة 99%.</p>"""

    faqs = [
        (f"ما هو {title_ar}؟", f"هو كريم ترطيب عائلي فاخر سعة 500 مل غني بـ {active_ar} والجليسرين وفيتامينات A & E لترطيب 48 ساعة."),
        (f"ما هي فوائد {active_ar} وفيتامينات A & E؟", "تغذي خلايا البشرة عميقاً، تمنح ملمساً مخملياً، وتزيد مرونة الجلد 48 ساعة."),
        ("هل يوفر ترطيباً 48 ساعة متواصلة؟", "نعم، مثبت سريرياً في حفظ رطوبة بشرة الجسم لـ 48 ساعة متواصلة."),
        ("ما حجم العبوة؟", "تأتي بحجم وافر سعة 500 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي كمية وافرة على الجسم والأكواع والركب ودلكي بحركات دائرية حتى الامتصاص."),
        ("هل يترك أثراً دهنياً لزجاً؟", "لا، يمتص بسرعة ليعطي ملمساً ناعماً دون لزوجة ثقيلة."),
        ("ما هو بلد صنع كريم كلير؟", "صُنع بواسطة شركة Amka Products العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات كلير لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        (f"ما هي رائحة الكريم؟", f"يتميز برائحة {active_ar} الزكية الفواحة التي تدوم على الجسم طوال اليوم."),
        ("هل يرطب الأكواع والركب شديدة الجفاف؟", "نعم، ممتاز جداً لتنعيم وترطيب الأكواع والركب والكعبين الجافة."),
        ("هل يناسب جميع أنواع البشرة؟", "نعم، مناسب للبشرة العادية، الجافة، والشديدة الجفاف."),
        ("هل يناسب جميع أفراد العائلة؟", "نعم، غسول وكريم عائلي آمن للأطفال والبالغين من سن 3 سنوات."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل العبوة 500 مل اقتصادية؟", "نعم، عبوة عائلية وافرة تكفي لاستخدام مستمر لأشهر طويلة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة دائرية متينة بغطاء محكم الحماية."),
        ("هل يساعد في حماية البشرة في الشتاء؟", "نعم، يوفر حماية فائقة ضد برودة وجفاف الشتاء."),
        ("هل يناسب الاستخدام اليومي؟", "نعم، آمن وممتاز للاستخدام اليومي المتكرر."),
        ("هل يمنع القشور والتطير؟", "نعم، يقضي تماماً على قشور الجلد والتطير."),
        ("هل يمتص بسهولة على الجلد؟", "نعم، ينفذ بسهولة داخل خلايا البشرة."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب لكلا الجنسين."),
        ("هل يمكن استخدامه بعد الحلاقة؟", "نعم، ممتاز لتهدئة وترطيب جلد الجسم بعد الحلاقة."),
        ("هل يترك ملمساً حريرياً؟", "نعم، يترك جسمكِ أملس ونظيفاً طوال اليوم."),
        ("هل يعزز إشراقة نضارة البشرة؟", "نعم، التغذية بالفيتامينات تعيد الإشراقة والحيويّة للجسم."),
        ("هل هو الكريم الأفخر والجود لشركة كلير؟", "نعم، كريم كلير المفضل والموثوق لعقود طويلة."),
        ("هل يتوفر بنوعيات أخرى لدى إكليل أبها؟", "نعم، تتوفر نكهات متعددة من كريمات كلير 500مل.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{title_en}</strong> is the iconic luxury body moisturizing cream engineered to deliver 48-hour continuous hydration, deep skin feeding, and complete dryness protection. Formulated by Clere, it combines Triple Glycerin, Vitamin A, and Vitamin E with {active_en}.</p>
<p>Featuring a rich, fast-absorbing texture, Clere Body Cream penetrates deep into skin layers without leaving a greasy or sticky residue, smoothing rough elbows and knees and leaving your body touchably silky soft.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>48-Hour Continuous Deep Hydration:</strong> Feeds dermal layers with intense moisturizers to stop dry skin tightness.</li>
  <li><strong>Enriched with Vitamins A & E & Glycerin:</strong> Deeply nourishes skin cells and improves skin elasticity.</li>
  <li><strong>Infused with {active_en}:</strong> Delivers velvet softness, skin feeding, and a subtle fresh fragrance.</li>
  <li><strong>Fast-Absorbing & Non-Greasy:</strong> Absorbs in seconds without leaving an oily or sticky film.</li>
  <li><strong>Smooths Rough Elbows & Knees:</strong> Softens dry flaking elbows, knees, heels, and body skin.</li>
  <li><strong>Generous 500ml Tub:</strong> High-value family tub providing months of continuous daily body care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Shower with warm water and gently pat skin dry.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a generous amount of Clere Body Cream over full body, elbows, and knees.</li>
  <li><strong>Step 3 (Massage):</strong> Massage in gentle circular motions until fully absorbed (use 1 to 2 times daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Triple Glycerin & Vitamins A & E:</strong> Seal moisture in skin layers and boost elasticity.</li>
  <li><strong>{active_en} Extract:</strong> Softens skin and leaves a pleasant tropical fragrance.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external body moisturizing application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a generous 500ml 48-hour body moisturizing cream enriched with {active_en} and Vitamins A & E.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Clere</td></tr>
  <tr><th>Category</th><td>Skincare / Nourishing 48-Hour Body Creams</td></tr>
  <tr><th>Product Type</th><td>48-Hour Hydrating Rich Body Cream (500ml)</td></tr>
  <tr><th>Volume/Weight</th><td>500 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Dry, Normal, Extremely Dry)</td></tr>
  <tr><th>Finish</th><td>Soft, silky, 48h hydrated & smooth body skin</td></tr>
  <tr><th>Texture</th><td>Rich fast-absorbing smooth cream</td></tr>
  <tr><th>Fragrance</th><td>Captivating {active_en} botanical aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Glycerin, Vitamin A, Vitamin E, {active_en} Extract</td></tr>
  <tr><th>Country of Origin</th><td>South Africa / Saudi Arabia (Amka)</td></tr>
  <tr><th>Manufacturer</th><td>Amka Products / Clere</td></tr>
  <tr><th>Age Group</th><td>All Ages (3+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Triple Glycerin & 48-Hour Dermal Moisture</h2>

<h3>What problem does this solve?</h3>
<p>Clere Body Cream resolves extreme body skin dryness, flaking, rough elbows, and tightness.</p>

<h3>Why choose Clere?</h3>
<p>Triple Glycerin humectants combined with Vitamins A & E form an occlusive 48-hour moisture seal that restores skin suppleness.</p>"""

    en_faqs = [
        (f"What is {title_en}?", f"It is a rich 500ml 48-hour moisturizing body cream enriched with {active_en}, Glycerin, and Vitamins A & E."),
        (f"What are the benefits of {active_en} and Vitamins A & E?", "Deeply feeds skin cells, improves elasticity, and locks in internal moisture for 48 hours."),
        ("Does it provide 48-hour continuous hydration?", "Yes, clinically proven to lock in skin moisture for 48 continuous hours."),
        ("What volume is contained in this tub?", "It comes in a generous 500ml tub."),
        ("How do I apply it correctly?", "Massage a generous amount over body, elbows, and knees until fully absorbed."),
        ("Does it leave a greasy residue?", "No, absorbs quickly leaving skin touchably silky without greasy film."),
        ("Where is Clere manufactured?", "It is produced by Amka Products following global beauty standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Clere products at Ekleel Abha are 100% original from certified distributors."),
        (f"What scent does this cream have?", f"Features a captivating {active_en} scent that lingers all day."),
        ("Does it soften dry elbows and knees?", "Yes, highly effective at softening dry elbows, knees, heels, and hands."),
        ("Is it suitable for all skin types?", "Ideal for normal, dry, and extremely dry skin types."),
        ("Is it safe for family daily use?", "Yes, safe for adults and children aged 3+."),
        ("How should I store the tub?", "Store in a cool, dry place away from direct heat."),
        ("Is the 500ml tub economical?", "Yes, generous volume provides months of daily family body care."),
        ("Is it great for winter cold dryness?", "Yes, shields skin against winter cold dryness and flaking."),
        ("Can it be used daily?", "Yes, safe and recommended for daily body moisturizing."),
        ("Does it stop skin flaking?", "Yes, completely clears dry skin flaking and tightness."),
        ("Does it absorb quickly?", "Yes, glides smoothly and absorbs into skin cells instantly."),
        ("Can both men and women use it?", "Yes, suitable for both men and women."),
        ("Is it great post-shaving?", "Yes, calms and hydrates body skin after shaving."),
        ("Does it restore skin radiance?", "Yes, 48-hour hydration restores natural radiance to dry skin."),
        ("Is Clere a trusted brand?", "Yes, Clere is a globally beloved body care brand for decades."),
        ("Are other variants available at Ekleel Abha?", "Yes, Ekleel Abha offers various Clere 500ml body cream variants."),
        ("Is it paraben-free?", "Dermatologically tested and safety-certified."),
        ("Is it the best value 500ml body cream?", "Yes, the #1 best value 48-hour body moisturizer tub.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "العناية بالبشرة / كريمات ترطيب الجسم الغنية المغذية",
        "brand": "Clere",
        "ar": {
            "title": title_ar,
            "meta_title": f"كريم كلير مرطب للجسم 500مل | صيدلية إكليل أبها",
            "meta_description": f"اشتري {title_ar}. ترطيب 48 ساعة بالجليسرين وفيتامينات A و E بـ {active_ar}. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["كلير", "كريم_كلير", "ترطيب_48_ساعة", "فيتامين_A_E", "إكليل_أبها"]
        },
        "en": {
            "title": title_en,
            "meta_title": f"Clere Body Cream 500ml | Ekleel Abha Pharmacy",
            "meta_description": f"Buy original {title_en}. 48-hour hydrating body cream with Glycerin & Vitamins A & E. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["clere", "body_cream", "48h_hydration", "glycerin_vitamins", "ekleel_abha"]
        },
        "schema": {
            "brand": "Clere",
            "category": "Skincare / Body Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"{img_slug}.webp",
            "alt": title_en,
            "title": title_en
        }
    }

def create_product_1816():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مزيل عرق من نيفيا- 40مل (Nivea Deodorant - 40ml)</strong> مستحضر الحماية والانتعاش الأساسي الموثوق عالمياً لمنع رائحة العرق وتأمين حماية مضادة للتعرق تدوم حتى 48 ساعة متواصلة. يرتكز هذا المزيل الرولي من نيفيا (Nivea Roll-On) على تركيبة خالية تماماً من الكحول والملونات الصناعية، المعززة بمركبات نيفيا المغذية للعبة ولطف البشرة.</p>
<p>يمتاز رول اون نيفيا بقوام ناعم ينزلق بسلاسة تحت الإبطين، ليمنحكِ جفافاً منعشاً، حماية فائقة ضد التعرق المفرط، وعطراً زكياً يمنحكِ ثقة مطلق في كافة الأوقات والأنشطة اليومية.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية 48 ساعة ضد التعرق والرائحة الكريهة:</strong> يقضي على البكتيريا المسببة لرائحة العرق ويضمن جفافاً تاماً.</li>
  <li><strong>خالي تماماً من الكحول والملونات:</strong> تركيبة لطيفة ومجربة جلدياً لحماية منطقة الإبطين الرقيقة.</li>
  <li><strong>رول اون ينزلق بسلاسة:</strong> يوزع السائل بالتساوي دون ترك أثراً لزجاً أو تقعسياً.</li>
  <li><strong>حماية من التصبغات والبقع على الملابس:</strong> ينشف فورياً ولا يترك أثراً أبيض أو أصفر على الأقمشة.</li>
  <li><strong>عطر نيفيا الانتعاشي الزكي:</strong> يغلفكِ برائحة النظافة المميزة لنيفيا طوال اليوم.</li>
  <li><strong>عبوة مدمجة سعة 40 مل:</strong> تصميم أنيق ومثالي لحقيبة اليد، الرياضة، والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> استحممي وجففي منطقة الإبطين جيداً.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> مرري رول اون نيفيا 2 إلى 3 مرات تحت كل إبط بالتساوي.</li>
  <li><strong>الخطوة الثالثة (التجفيف):</strong> دعي السائل يجف لـ 30 ثانية قبل ارتداء الملابس (يُستعمل يومياً بعد الشاور).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركبات حماية ضد التعرق (Aluminum Chlorohydrate):</strong> تنظم التعرق وتضمن الجفاف.</li>
  <li><strong>خلاصة مرطبات نيفيا الخالية من الكحول:</strong> تلطف جلد الإبط وتمنع التهيج.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي تحت الإبطين فقط.</li>
  <li>تجنبي استخدامه على البشرة المتهيجة أو المصابة بجروح الحلاقة الحديثة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة وعائلة تفتش عن مزيل عرق رولي بحماية 48 ساعة ولطف خالي من الكحول.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>نيفيا (Nivea)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / مزيلات ومضادات عرق الإبطين (Roll-On)</td></tr>
  <tr><th>نوع المنتج</th><td>مزيل ومضاد عرق رول اون بحماية 48 ساعة (40ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>40 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الإبطين (بما في ذلك الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>إبطان جافان، معطران، محميان لـ 48 ساعة وخاليان من الرائحة</td></tr>
  <tr><th>الملمس</th><td>سائل رول اون خفيف سريع الجفاف غير لزج</td></tr>
  <tr><th>العطر</th><td>عطر نيفيا الانتعاشي الطبيعي الكلاسيكي</td></tr>
  <tr><th>المكونات النشطة</th><td>مركبات الحماية ضد التعرق، مرطبات نيفيا، خالي من الكحول</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا / المملكة العربية السعودية (Beiersdorf)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beiersdorf (نيفيا)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد مزيلات العرق من نيفيا (Nivea Roll-On)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مزيل عرق نيفيا مشكلة رائحة العرق المزعجة، التعرق المفرط، والتصبغات والتهيج الناجم عن مزيلات الكحول القاسية.</p>

<h3>لماذا تنجح تركيبة نيفيا 48 ساعة؟</h3>
<p>لأن مركب الألومنيوم المنظم يقلل إفراز الغدد العرقية، بينما تقتل المركبات المطهرة البكتيريا المسببة للرائحة لـ 48 ساعة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على بشرة جافة:</strong> استعملي الرول اون على بشرة جافة ونظيفة فورياً بعد الاستحمام.<br>
2. <strong>الانتظار حتى يجف:</strong> انتظري 30 ثانية ليجف السائل قبل ارتداء الملابس.<br>
3. <strong>تجنب الاستعمال بعد الحلاقة المباشرة:</strong> انتظري 20 دقيقة بعد الحلاقة لمنع التهيج.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مزيلات العرق تسبب اسمرار وسواد منطقة الإبطين."<br>
<strong>الحقيقة:</strong> مزيل نيفيا خالي من الكحول والملونات الصناعية ومجرب لحماية وتنعيم منطقة الإبطين دون اسمرار.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تكون جزيئات مضاد التعرق سداداً مؤقتاً بالطبقة السطحية لقنوات العرق، مما يقلل الرطوبة دون التأثير على التنفس الطبيعي للجلد.</p>"""

    faqs = [
        ("ما هو مزيل عرق من نيفيا- 40مل؟", "هو رول اون مضاد للتعرق من نيفيا خالي من الكحول يضمن حماية 48 ساعة وجفاف وانتعاش تام سعة 40 مل."),
        ("ما هي فوائد خلوه من الكحول والملونات؟", "يحمي منطقة الإبطين الرقيقة من التهيج والاسمرار ويمنح لطفاً فائقاً."),
        ("هل يوفر حماية 48 ساعة ضد التعرق والرائحة؟", "نعم، مثبت سريرياً في منع رائحة العرق وتأمين جفاف لـ 48 ساعة."),
        ("ما حجم العبوة؟", "تأتي بحجم 40 مل مدمج."),
        ("كيف يُستخدم بالشكل الصحيح؟", "مرري الرول اون 2 إلى 3 مرات تحت إبطين نظيفين وجافين ودعيه يجف لـ 30 ثانية قبل ارتداء الملابس."),
        ("هل يترك بقعاً بيضاء أو صفراء على الملابس؟", "لا، فورمولا متطورة تنشف فورياً ولا تترك أي أثر على الملابس."),
        ("ما هو بلد صنع مزيل عرق نيفيا؟", "صُنع بواسطة شركة بايرسدورف (Beiersdorf) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات نيفيا لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يناسب البشرة الحساسة؟", "نعم، تركيبة مجربة جلدياً وخالية من الكحول ومناسبة للبشرة الحساسة."),
        ("ما هي رائحة مزيل نيفيا؟", "يتميز برائحة النظافة والانتعاش الكلاسيكية المميزة لنيفيا."),
        ("هل أنبوب 40 مل مناسب للحقيبة والسفر؟", "نعم، حجم رول اون مدمج ومثالي لحقيبة اليد والرياضة والسفر."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب لكلا الجنسين."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل ينزلق السائل بسلاسة؟", "نعم، كرة الرول اون تضمن توزيعاً متساوياً وسلساً."),
        ("هل يناسب الصيف والحر الشديد؟", "ممتاز جداً لتأمين حماية وجفاف تام في حر الصيف."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة دائرية بغطاء لولبي محكم يمنع الجفاف والتسرب."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستخدم مرة واحدة يومياً بعد الاستحمام."),
        ("هل يساعد في تقليل التهيج بعد الحلاقة؟", "خلوه من الكحول يمنع أي حرقان أو تهيج بعد الحلاقة."),
        ("هل هو مزيل العرق الأكثر مبيعاً عالمياً؟", "نعم، نيفيا الماركة الأولى الموثوقة عالمياً لمزيلات العرق."),
        ("هل يترك ملمساً لزجاً؟", "لا، يجف فورياً ليترك الإبطين ناعمين وجافين."),
        ("هل يناسب المراهقين والبالغين؟", "مناسب للمراهقين والبالغين من سن 12 سنة فما فوق."),
        ("هل يحتوي على بارابين؟", "تركيبة مجربة ومصرح بها طبقاً لأعلى معايير السلامة."),
        ("هل يمنع تكاثر البكتيريا المسببة للرائحة؟", "نعم، يقضي على البكتيريا المسببة لرائحة العرق."),
        ("هل يمنح حس ثقة طوال اليوم؟", "نعم، يضمن انتعاشاً وجفافاً وثقة مطلقة."),
        ("هل يتوفر بأنواع أخرى لدى إكليل أبها؟", "نعم، تتوفر التشكيلة الكاملة من مزيلات نيفيا رول اون وسبراي.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Nivea Deodorant - 40ml</strong> is the world's #1 trusted daily antiperspirant roll-on engineered to deliver continuous 48-hour protection against body odor and sweat. Formulated alcohol-free and colorant-free by Nivea, it combines reliable antiperspirant performance with gentle skin care.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>48-Hour Reliable Sweat & Odor Shield:</strong> Clinically proven to block body odor and provide dryness.</li>
  <li><strong>100% Alcohol & Colorant Free:</strong> Ultra-gentle formula safe for sensitive underarm skin.</li>
  <li><strong>Smooth Glide Roll-On:</strong> Evenly dispenses formula without leaving sticky residue.</li>
  <li><strong>Stain Prevention:</strong> Dries rapidly with zero white marks or yellow stains on clothing.</li>
  <li><strong>Signature Clean Nivea Fragrance:</strong> Envelops you in a fresh, clean scent all day long.</li>
  <li><strong>Compact 40ml Bottle:</strong> Sleek glass roll-on size ideal for handbags, gym kits, and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Shower and dry underarm skin thoroughly.</li>
  <li><strong>Step 2 (Apply):</strong> Roll Nivea Deodorant 2 to 3 times evenly under each arm.</li>
  <li><strong>Step 3 (Dry):</strong> Allow 30 seconds to air dry before dressing.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Aluminum Chlorohydrate:</strong> Regulates underarm sweat production for 48h dryness.</li>
  <li><strong>Nivea Caring Lipids:</strong> Soften delicate underarm skin and prevent irritation.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external underarm application only.</li>
  <li>Do not apply to broken, inflamed, or freshly shaved irritated skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking 48-hour reliable antiperspirant protection in an alcohol-free roll-on.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Nivea</td></tr>
  <tr><th>Category</th><td>Personal Care / Antiperspirant Roll-On Deodorants</td></tr>
  <tr><th>Product Type</th><td>48-Hour Alcohol-Free Antiperspirant Roll-On (40ml)</td></tr>
  <tr><th>Volume/Weight</th><td>40 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Underarm Skin Types (Including Sensitive)</td></tr>
  <tr><th>Finish</th><td>Dry, fresh, 48h protected & clean-scented underarms</td></tr>
  <tr><th>Texture</th><td>Smooth fast-drying non-sticky roll-on fluid</td></tr>
  <tr><th>Fragrance</th><td>Classic fresh Nivea signature scent</td></tr>
  <tr><th>Active Ingredients</th><td>Aluminum Chlorohydrate, Nivea Caring Lipids, Alcohol-Free Base</td></tr>
  <tr><th>Country of Origin</th><td>Germany / Saudi Arabia (Beiersdorf)</td></tr>
  <tr><th>Manufacturer</th><td>Beiersdorf (Nivea)</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Aluminum Antiperspirants & 48-Hour Protection</h2>

<h3>What problem does this solve?</h3>
<p>Nivea Deodorant Roll-On resolves body odor, excess underarm sweating, clothing stains, and alcohol irritation.</p>

<h3>Why choose Nivea?</h3>
<p>Alcohol-free antiperspirant lipids form a temporary seal over sweat ducts, providing 48-hour dryness while soothing underarm skin.</p>"""

    en_faqs = [
        ("What is Nivea Deodorant - 40ml?", "It is an alcohol-free antiperspirant roll-on providing 48-hour protection against sweat and body odor."),
        ("What are the benefits of an alcohol-free formula?", "Protects delicate underarm skin from irritation, burning, and dark discoloration."),
        ("Does it provide 48-hour protection?", "Yes, clinically proven to block body odor and maintain dryness for 48 continuous hours."),
        ("What volume is contained in this bottle?", "It comes in a 40ml roll-on bottle."),
        ("How do I apply it correctly?", "Roll 2 to 3 times under clean dry underarms and allow 30 seconds to dry before dressing."),
        ("Does it stain clothing?", "No, dries rapidly without leaving white marks or yellow stains on clothes."),
        ("Where is Nivea manufactured?", "It is produced by Beiersdorf following global quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Nivea products at Ekleel Abha are 100% original from certified distributors."),
        ("Is it safe for sensitive skin?", "Dermatologically tested and 100% safe for sensitive underarms."),
        ("What scent does it have?", "Features the fresh, clean signature Nivea fragrance."),
        ("Is the 40ml bottle travel-friendly?", "Yes, compact roll-on size fits easily into handbags and gym kits."),
        ("Can both men and women use it?", "Yes, suitable for both men and women."),
        ("How should I store the bottle?", "Store in a cool, dry place away from heat."),
        ("Does the roll-on glide smoothly?", "Yes, smooth ball dispenser distributes fluid evenly without tugging."),
        ("Is it great for summer heat?", "Yes, essential for maintaining dryness during hot summer weather."),
        ("Is the bottle securely sealed?", "Yes, comes in a sturdy glass bottle with a screw lid."),
        ("How often should I use it?", "Apply once daily after showering."),
        ("Does it cause burning post-shaving?", "Alcohol-free formula prevents stinging or burning post-shaving."),
        ("Is Nivea a #1 trusted brand?", "Yes, Nivea is the #1 globally trusted deodorant brand."),
        ("Does it leave a sticky residue?", "No, absorbs quickly leaving underarms dry and soft."),
        ("Is it suitable for teenagers?", "Safe for adults and teens aged 12+."),
        ("Does it eliminate odor-causing bacteria?", "Yes, kills odor-causing bacteria for long-lasting freshness."),
        ("Does it provide confidence all day?", "Yes, guarantees fresh, dry confidence all day long."),
        ("Is it alcohol-free?", "Yes, 100% free of ethyl alcohol."),
        ("Are other Nivea deodorants available at Ekleel Abha?", "Yes, Ekleel Abha offers various Nivea roll-ons and spray deodorants.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1816",
        "sku": "EK-1816",
        "gtin": "42217572",
        "category": "العناية الشخصية / مزيلات ومضادات عرق الإبطين",
        "brand": "Nivea",
        "ar": {
            "title": "مزيل عرق من  نيفيا- 40مل",
            "meta_title": "مزيل عرق نيفيا رول اون 40مل | صيدلية إكليل أبها",
            "meta_description": "اشتري مزيل عرق من نيفيا (40مل). حماية 48 ساعة ضد التعرق خالي من الكحول. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["نيفيا", "مزيل_عرق_نيفيا", "رول_اون_نيفيا", "حماية_48_ساعة", "إكليل_أبها"]
        },
        "en": {
            "title": "Nivea Deodorant - 40ml",
            "meta_title": "Nivea Deodorant Roll-On 40ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Nivea Deodorant Roll-On (40ml). 48-hour antiperspirant protection alcohol-free formula. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["nivea", "deodorant", "roll_on", "48h_protection", "ekleel_abha"]
        },
        "schema": {
            "brand": "Nivea",
            "category": "Personal Care / Deodorant Roll-On",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "nivea-deodorant-40ml.webp",
            "alt": "Nivea Deodorant 40ml",
            "title": "Nivea Deodorant 40ml"
        }
    }

def create_product_1817():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>جهاز خيط تنظيف الاسنان (Water Dental Flosser)</strong> الجهاز الطبي التكنولوجي الأكثر فاعلية وتطوراً لتنظيف وتقليح الفم والأسنان بالماء الضغاط (Water Jet Flosser) بديل الخيط القطني التقليدي. يرتكز هذا الجهاز الحديث على تقنية النبضات المائية عالية التردد (Water Flossing Technology)، حيث يطلق ضغط ماء دقيقاً ينظف المسافات الضيقة بين الأسنان وتحت خط اللثة بفاعلية تفوق الخيط التقليدي بـ 5 أضعاف.</p>
<p>يعمل خيط الأسنان المائي على إزالة 99.9% من طفيليات البلاك وبقايا الطعام العالقة، يمنع تكون الجير، يهدئ التهابات ونزيف اللثة، ويُعد الجهاز الأهم والموصى به طبيًا لمن يملكون تقويم أسنان، زرعات، أو جسور طبية.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف الفم بالماء الضغاط 5 أضعاف:</strong> يزيل 99.9% من البلاك وبقايا الطعام بين فتحات الأسنان.</li>
  <li><strong>مثالي لتقويم الأسنان والزرعات والجسور:</strong> ينظف حول أسلاك التقويم والتركيبات بسهولة دون جرح.</li>
  <li><strong>تدليك وتحفيز صحة اللثة:</strong> نبضات الماء تنشط الدورة الدموية باللثة وتمنع النزيف والتهاب الأنسجة.</li>
  <li><strong>مستويات ضغط مائية متعددة:</strong> يمنحكِ خيارات ضغط تتدرج من اللطيف للحساس وحتى القوي للتنظيف العميق.</li>
  <li><strong>رؤوس تنظيف متعددة قابلة للاستبدال:</strong> يأتي بملحقات مخصصة لتقويم الأسنان وتنظيف اللسان.</li>
  <li><strong>تصميم لاسلكي قابلة للشحن ومقاوم للماء:</strong> بطارية تدوم طويلاً وسهلة الاستخدام داخل الحمام.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التعبئة):</strong> املئي خزان الماء الخاص بالجهاز بالماء الفاتر (يمكن إضافة قطرات غسول فم).</li>
  <li><strong>الخطوة الثانية (التحديد):</strong> اختاري الرأس المناسب ومستوى الضغط المرغوب فيه ووجهي الفوهة نحو خط اللثة بزاوية 90 درجة.</li>
  <li><strong>الخطوة الثالثة (التنظيف):</strong> شغلي الجهاز ومرري نبضات الماء بين الفتحات والأسنان لمدة 1 إلى 2 دقيقة ثم افرغي الخزان.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مضخة مائية نبضية عالية التردد:</strong> تطلق من 1400 إلى 1800 نبضة ماء بالدقيقة للتنظيف الفائق.</li>
  <li><strong>خزان ماء مقاوم للتسرب وسهل التنظيف:</strong> سعة مناسبة للتنظيف الشامل دون الحاجة لإعادة التعبئة.</li>
</ul>

<h2>تحذيرات وااحتياطات</h2>
<ul>
  <li>للاستخدام الفموي لتنظيف الأسنان واللثة فقط بالماء.</li>
  <li>تجنبي توجيه الضغط المائي الشديد مباشرة للعينين أو الأذنين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال الصغار وفي مكان جاف بعد تفريغ الخزان.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يملكون تقويم أسنان، تركيبات، أو يعانون من نزيف اللثة وتراكم البلاك ويرغبون في تنظيف مائي احترافي.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>عام / صيدلية إكليل أبها (Water Flosser)</td></tr>
  <tr><th>الفئة</th><td>أجهزة ومستلزمات الفم / أجهزة خيط الأسنان المائي اللاسلكي</td></tr>
  <tr><th>نوع المنتج</th><td>جهاز خيط تنظيف الأسنان المائي اللاسلكي القابل للشحن</td></tr>
  <tr><th>الحجم/الوزن</th><td>جهاز يدوياً مع خزان ماء ورؤوس متعددة</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بالفم والأسنان والتقويم)</td></tr>
  <tr><th>المظهر النهائي</th><td>أسنان منقاة، لثة صحية خالية من البلاك وخالية من بقايا الطعام</td></tr>
  <tr><th>الملمس</th><td>نبضات مائية دقيقة منعشة ومريحة</td></tr>
  <tr><th>العطر</th><td>عديم الرائحة</td></tr>
  <tr><th>المكونات النشطة</th><td>مضخة نبضية، خزان ماء مضاد للبكتيريا، رؤوس تنظيف متعددة</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين / كوريا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Oral Care Technologies</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والأطفال (من 8 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد خيط الأسنان المائي (Water Dental Flosser)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج جهاز خيط الأسنان المائي مشكلة انحشار بقايا الطعام حول تقويم الأسنان والزرعات، نزيف اللثة بالخيط القطني، وتراكم البلاك.</p>

<h3>لماذا تنجح تقنية النبضات المائية؟</h3>
<p>لأن ضغط نبضات الماء يزيل 99.9% من البلاك من الجيب اللثوي العميق ب رفق، دون إحداث جروح أو نزيف باللثة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنظيف اليومي بعد الأكل:</strong> استعملي الجهاز مرة إلى مرتين يومياً بعد الوجبات الرئيسية.<br>
2. <strong>تفريغ الخزان بعد الاستخدام:</strong> افرغي خزان الماء دائماً بعد الانتهاء للحفاظ على نظافة الجهاز.<br>
3. <strong>البدء بالمستوى اللطيف:</strong> ابدئي دائماً بالمستوى المنخفض لتعتاد اللثة ثم ارفعي الضغط تدريجياً.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الخيط المائي يسبب تراجع اللثة وتوسع الفتحات."<br>
<strong>الحقيقة:</strong> النبضات المائية تدلك اللثة وتزيد التروية الدموية، مما يثبت اللثة ويحميها من التراجع.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تولّد المضخة النبضية ضغطاً ديناميكياً يفتت البيوفلم البكتيري (Bacterial Biofilm) من الجيوب اللثوية والمسافات الفاصلة بدقة عالية.</p>"""

    faqs = [
        ("ما هو جهاز خيط تنظيف الاسنان المائي؟", "هو جهاز طبي لاسلكي ينظف الأسنان واللثة بالماء الضغاط لإزالة 99.9% من البلاك وبقايا الطعام بفاعلية فائقة."),
        ("هل هو أفضل من الخيط القطني التقليدي؟", "نعم، ينظف المسافات والجيوب اللثوية بفاعلية تفوق الخيط القطني بـ 5 أضعاف ودون إحداث نزيف."),
        ("هل يناسب أصحاب تقويم الأسنان والزرعات؟", "ممتاز جداً لأصحاب التقويم والتركيبات والجسور لتنظيف ما حول الأسلاك ب أمان."),
        ("هل يساعد في الوقاية من نزيف والتهاب اللثة؟", "نعم، نبضات الماء تدلك اللثة وتزيد الدورة الدموية وتمنع النزيف والالتهاب."),
        ("هل يدعم مستويات ضغط متعددة؟", "نعم، يحتوي على مستويات ضغط متدرجة تناسب اللثة الحساسة والتنظيف العميق."),
        ("ما هو بلد صنع الجهاز؟", "صُنع وفق أعلى معايير الجودة الطبية لأجهزة العناية بالفم."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع أجهزة العناية بالفم لدى إكليل أبها أصلية 100% ومصنوعة من خامات آمنة."),
        ("هل الجهاز قابل للشحن ولاسلكي؟", "نعم، يحتوي على بطارية قابلة للشحن تدوم لأيام طويلة ومقاوم للماء IPX7."),
        ("كيف ينظف الجهاز بعد الاستخدام؟", "يُفرغ خزان الماء ويشطف وتترك الفوهة لتجف."),
        ("هل يمكن إضافة غسول الفم في خزان الماء؟", "نعم، يمكن إضافة قطرات من غسول الفم المعقم مع الماء الفاتر."),
        ("هل يناسب جميع الأعمار؟", "مناسب للأطفال والبالغين من سن 8 سنوات فما فوق."),
        ("هل العبوة تحتوي على رؤوس متعددة؟", "نعم، تأتي مع ملحقات ورؤوس تنظيف متعددة قابلة للاستبدال."),
        ("كيف أحتفظ بالجهاز؟", "يُحفظ في مكان جاف بعد تفريغ خزان الماء."),
        ("هل يزيل رائحة الفم الكريهة؟", "نعم، تنظيف البلاك وبقايا الأكل يقضي على البكتيريا المسببة للرائحة الكريهة."),
        ("هل يقلل ترسبات الجير التكلسي؟", "نعم، منع تراكم البلاك يحد من تكون الجير التكلسي الصعب."),
        ("هل الجهاز سهل الاستخدام للسفر؟", "نعم، تصميم مدمج وخفيف الوزن ومثالي للسفر وتسهيل التنقل."),
        ("كم مدة الاستخدام الموصى بها في المرة؟", "يُستخدم لمدة 1 إلى 2 دقيقة كاملة لتنظيف كامل الفم."),
        ("هل يسبب آلاماً للثة الحساسة؟", "التدرج في مستويات الضغط يضمن تنظيفاً لطيفاً دون أي ألم."),
        ("هل العبوة محكمة التغليف؟", "تأتي في عبوة مغلفة طبقاً لأعلى المعايير الصحية والكهربائية."),
        ("هل يغني عن تفريش الأسنان بالفرشاة؟", "يُستخدم كأداة مكملة لفرشاة الأسنان للحصول على نظافة فموية 100%."),
        ("هل بطارية الجهاز تدوم طويلاً؟", "نعم، شحنة واحدة تكفي لعدة أسابيع من الاستخدام اليومي."),
        ("هل الجهاز مقاوم للماء؟", "نعم، تصنيف مقاومة الماء يسمح باستخدامه داخل الدش والحمام ب أمان."),
        ("هل ينصح به أطباء الأسنان والتقويم؟", "نعم، الجهاز رقم 1 الموصى به طبياً من أطباء التقويم واللثة."),
        ("هل الضغط المائي آمن؟", "نعم، ضغط مائي آمن ومجرب فسيولوجياً."),
        ("هل يتوفر بقيمة ممتازة لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Water Dental Flosser</strong> is the advanced medical water jet flossing device designed to revolutionize daily oral hygiene and interdental cleaning. Utilizing high-frequency water pulsation technology, it fires targeted water micro-jets between teeth and under the gumline 5x more effectively than traditional string floss.</p>
<p>Removing up to 99.9% of plaque bio-film and trapped food debris, the Cordless Water Flosser prevents tartar formation, massages bleeding gums, and stands as the essential dentist-recommended tool for those with braces, dental implants, crowns, or bridges.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>5x Deeper Water Jet Interdental Cleansing:</strong> Sweeps away 99.9% of plaque and food debris between teeth.</li>
  <li><strong>Essential for Braces, Implants & Bridges:</strong> Cleans around orthodontic wires and crowns effortlessly without bleeding.</li>
  <li><strong>Massages & Improves Gum Health:</strong> Water pulsations stimulate micro-circulation to halt gingival bleeding.</li>
  <li><strong>Multiple Water Pressure Modes:</strong> Features adjustable pressure settings from gentle sensitive to deep pulse.</li>
  <li><strong>Multiple Replaceable Nozzle Tips:</strong> Includes specialized orthodontic, plaque, and tongue cleaning tips.</li>
  <li><strong>Cordless Waterproof & Rechargeable Design:</strong> IPX7 waterproof rating with long-lasting battery life.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Fill Tank):</strong> Fill the water reservoir with warm water (or add a few drops of alcohol-free mouthwash).</li>
  <li><strong>Step 2 (Select Tip & Mode):</strong> Attach desired nozzle tip, select pressure mode, and aim tip at 90-degree angle to gumline.</li>
  <li><strong>Step 3 (Floss & Empty):</strong> Turn on device and guide water jet along teeth and gaps for 1 to 2 minutes; empty remaining water.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>High-Frequency Water Pulse Pump:</strong> Generates 1400 to 1800 water pulses per minute for deep cleaning.</li>
  <li><strong>Antibacterial Leak-Proof Water Reservoir:</strong> Easy-fill tank providing complete oral cleansing per session.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For oral water jet teeth and gum cleaning application only.</li>
  <li>Do not direct high-pressure water jets directly into eyes, ears, or open wounds.</li>
  <li>Keep out of reach of young children and store dry after emptying tank.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with braces, dental implants, crowns, or bleeding gums seeking a 5x more effective cordless water flosser.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Generic / Ekleel Abha Pharmacy</td></tr>
  <tr><th>Category</th><td>Oral Care Devices / Cordless Water Dental Flossers</td></tr>
  <tr><th>Product Type</th><td>Rechargeable Cordless Water Jet Oral Irrigator</td></tr>
  <tr><th>Volume/Weight</th><td>Single Handheld Device with Reservoir & Tips</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Oral, Dental & Orthodontic Care)</td></tr>
  <tr><th>Finish</th><td>Clean teeth, plaque-free gaps, healthy gums & fresh breath</td></tr>
  <tr><th>Texture</th><td>Refreshing high-frequency water pulsations</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-Free</td></tr>
  <tr><th>Active Ingredients</th><td>Water Pulse Pump, IPX7 Waterproof Body, Replaceable Tips</td></tr>
  <tr><th>Country of Origin</th><td>China / Korea</td></tr>
  <tr><th>Manufacturer</th><td>Oral Care Technologies</td></tr>
  <tr><th>Age Group</th><td>Adults & Kids (8+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Pulsating Water Jets & Plaque Biofilm Removal</h2>

<h3>What problem does this solve?</h3>
<p>Water Dental Flosser resolves food trapping around braces, gum bleeding caused by string floss, and deep plaque accumulation.</p>

<h3>Why choose a Water Flosser?</h3>
<p>High-frequency water jets dislodge 99.9% of plaque biofilm from deep periodontal pockets gently without tearing fragile gingival tissue.</p>"""

    en_faqs = [
        ("What is the Water Dental Flosser?", "It is a rechargeable cordless oral irrigator that uses targeted water jets to clear 99.9% of plaque and food debris."),
        ("Is it better than traditional string floss?", "Yes, cleans interdental gaps and gum pockets 5x more effectively than string floss without causing bleeding."),
        ("Is it suitable for braces, implants, and bridges?", "Yes, essential for cleaning around orthodontic wires, implants, and dental bridges safely."),
        ("Does it help prevent gum bleeding and inflammation?", "Yes, water pulsations massage gums, boost blood circulation, and stop bleeding."),
        ("Does it offer multiple pressure modes?", "Yes, features adjustable pressure settings ranging from soft sensitive to deep clean pulse."),
        ("Where is it manufactured?", "Produced under strict medical oral device quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All oral care devices at Ekleel Abha are 100% original and crafted from safe materials."),
        ("Is it cordless and rechargeable?", "Yes, features a long-lasting rechargeable battery and IPX7 waterproof body."),
        ("How do I clean the flosser after use?", "Empty remaining tank water, rinse reservoir, and let nozzle air dry."),
        ("Can mouthwash be added to the water tank?", "Yes, a few drops of alcohol-free mouthwash can be mixed with warm water in the reservoir."),
        ("Is it suitable for all ages?", "Safe for adults and children aged 8+."),
        ("Does it include multiple nozzle tips?", "Yes, comes with multiple interchangeable specialized nozzle tips."),
        ("How should I store the device?", "Store in a dry place after emptying the water reservoir."),
        ("Does it eliminate bad breath?", "Yes, removing trapped food and plaque eliminates odor-causing oral bacteria."),
        ("Does it reduce hard tartar buildup?", "Yes, clearing plaque daily prevents tartar calcification."),
        ("Is it travel-friendly?", "Yes, compact, lightweight cordless design ideal for travel."),
        ("What is the recommended flossing time?", "Use for 1 to 2 full minutes to cleanse all mouth quadrants."),
        ("Does it hurt sensitive gums?", "Multiple pressure settings ensure gentle, pain-free flossing for sensitive gums."),
        ("Is the packaging hygienic?", "Yes, packaged securely adhering to medical and electrical safety standards."),
        ("Does it replace manual toothbrushing?", "Used as a complementary tool alongside toothbrushing for 100% oral hygiene."),
        ("Does the battery last long?", "Yes, a single charge lasts for weeks of daily use."),
        ("Is the device waterproof?", "Yes, IPX7 waterproof rating allows safe use inside the shower."),
        ("Is it orthodontist recommended?", "Yes, the #1 recommended device by orthodontists and periodontists."),
        ("Is water pressure safe?", "Yes, physiologically tested safe water jet pressure."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1817",
        "sku": "EK-1817",
        "gtin": "121212",
        "category": "أجهزة ومستلزمات الفم / أجهزة خيط الأسنان المائي اللاسلكي",
        "brand": "Generic Water Flosser",
        "ar": {
            "title": "جهاز خيط تنظيف الاسنان",
            "meta_title": "جهاز خيط تنظيف الاسنان المائي | صيدلية إكليل أبها",
            "meta_description": "اشتري جهاز خيط تنظيف الاسنان المائي اللاسلكي. تنظيف مائي 5 أضعاف للتقويم واللثة وإزالة البلاك. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["خيط_الأسنان_المائي", "جهاز_الخيط_المائي", "تنظيف_التقويم", "إزالة_البلاك", "إكليل_أبها"]
        },
        "en": {
            "title": "Water Dental Flosser",
            "meta_title": "Water Dental Flosser Cordless | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Water Dental Flosser. Rechargeable cordless water jet flosser for braces, plaque & gum care. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["water_flosser", "dental_irrigator", "braces_cleaning", "plaque_remover", "ekleel_abha"]
        },
        "schema": {
            "brand": "Generic Water Flosser",
            "category": "Oral Care / Water Flosser",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "water-dental-flosser.webp",
            "alt": "Water Dental Flosser",
            "title": "Water Dental Flosser"
        }
    }

def create_product_1818():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>روج احمر شفاة من هيري (Hery Lipstick)</strong> أحمر الشفاه الكلاسيكي الفاخر المصمم لإضفاء لون أحمر مخملي غني وثابت يمنح شفتيكِ جاذبية وسحراً استثنائياً. يعتمد هذا الروج الأنيق من هيري (Hery) على تركيبة مخملية مرطبة مدعمة بفيتامين E والزيوت المطربة، حيث ينزلق بسلاسة على الشفتين ليمنحهما تغطية كاملة ولوناً حيوياً دون التسبب في الجفاف أو التكتل.</p>
<p>يمتاز روج هيري الأحمر بثبات يدوم لعدة ساعات متواصلة، ومظهر مخملي جذاب يبرز جمال شفتيكِ في كافة المناسبات، مع ترطيب عميق يحافظ على ليونة ونعومة الشفتين طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>لون أحمر كلاسيكي غني ومخملي:</strong> يمنح الشفتين تغطية كاملة ولوناً حيوياً جذاباً من أول مسحة.</li>
  <li><strong>ترطيب عميق بفيتامين E والزيوت:</strong> يمنع جفاف وتطير الشفتين ويحافظ على ليونتهما.</li>
  <li><strong>ثبات ممتاز يدوم لعدة ساعات:</strong> يقاوم التلطخ والتلطيخ ليضمن إطلالة متألقة طوال اليوم.</li>
  <li><strong>قوام ناعم ينزلق بسلاسة:</strong> ينساب على الشفتين بمرونة دون إحداث خطوط أو تكتلات.</li>
  <li><strong>لمسة نهائية ساتانية مخملية:</strong> تمنح الشفتين مظهراً ممتلئاً ومشرقاً في كافة المناسبات.</li>
  <li><strong>أنبوب أنيق ومدمج:</strong> تصميم راقٍ يسهل حمله في حقيبة المكياج والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التهيئة):</strong> قشري الشفتين بلطف وضعي مرطب خفيف إذا لزم الأمر.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> مرري روج هيري الأحمر من منتصف الشفة العليا باتجاه الزوايا الخارجية.</li>
  <li><strong>الخطوة الثالثة (التحديد):</strong> استكملي طلاء الشفة السفلى وكرري المسحة للحصول على كثافة ولون غني.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>صباغات أحمر مخملية غنية (Red Velvet Pigments):</strong> تمنح لوناً حيوياً وتغطية تامة.</li>
  <li><strong>فيتامين E وزيوت الترطيب الطبيعية:</strong> تغذي الشفتين وتمنع الجفاف والتطير.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي التجميلي على الشفتين فقط.</li>
  <li>يُحفظ بعيداً عن الحرارة الشديدة والشمس المباشرة لمنع ذوبان الروج.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تفتش عن أحمر شفاه أحمر كلاسيكي فاخر، مرطب، وثابت لمختلف المناسبات.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>هيري (Hery)</td></tr>
  <tr><th>الفئة</th><td>المكياج / أحمر الشفاه المخملي والمرطب (Lipsticks)</td></tr>
  <tr><th>نوع المنتج</th><td>أحمر شفاه كلاسيكي مرطب ومخملي (Red Lipstick)</td></tr>
  <tr><th>الحجم/الوزن</th><td>أحمر شفاه أنبوب واحد</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (مكياج الشفتين)</td></tr>
  <tr><th>المظهر النهائي</th><td>شفاه حمراء مخملية، ممتلئة، مرطبة، وخالية من الجفاف</td></tr>
  <tr><th>الملمس</th><td>قوام كريمي مخملي ينزلق بسلاسة</td></tr>
  <tr><th>العطر</th><td>عطر ناعم خفيف ممتع</td></tr>
  <tr><th>المكونات النشطة</th><td>صباغات أحمر ناصعة، فيتامين E، زيوت ترطيب مخملية</td></tr>
  <tr><th>بلد المنشأ</th><td>الصين / كوريا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Hery Cosmetics</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 15 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد روج هيري الأحمر (Hery Lipstick)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج روج هيري أحمر الشفاه مشكلة جفاف الشفتين عند وضع الروج المطفي، التكتل، وزوال اللون السريع.</p>

<h3>لماذا تنجح تركيبته المخملية؟</h3>
<p>لأن فيتامين E والزيوت المرطبة تغلف الشفتين بحجاب واقٍ، مما يمنح لوناً أحمر غنياً وثباتاً دون تشقق.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التقشير الخفيف:</strong> قشري الشفتين قبل وضع الروج لإبراز اللون المخملي.<br>
2. <strong>استخدام محدد الشفاه:</strong> استعملي محدد شفاه أحمر لتثبيت حدود الروج.<br>
3. <strong>الحفظ بعيداً عن الحرارة:</strong> احفظي الروج في مكان بارد لمنع ذوبان القوام.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "أحمر الشفاه الأحمر الثابت يسبب جفاف واسمرار الشفتين."<br>
<strong>الحقيقة:</strong> روج هيري مدعم بفيتامين E والمرطبات لحماية وتغذية الشفتين أثناء الارتداء.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>ترتبط الصباغات المخملية بدقة مع طبقة الشفتين السطحية، بينما توفر الزيوت المرطبة مرونة تمنع تشقق اللون أثناء الابتسام.</p>"""

    faqs = [
        ("ما هو روج احمر شفاة من هيري؟", "هو أحمر شفاه كلاسيكي مخملي باللون الأحمر الغني غني بفيتامين E لترطيب وتجميل الشفتين وثبات يدوم طويلاً."),
        ("ما هي فوائد فيتامين E في الروج؟", "يرطب الشفتين، يمنع الجفاف والتشقق، ويضمن تغطية مخملية ناعمة."),
        ("هل يمنح لوناً أحمر غنياً وثباتاً ممتازاً؟", "نعم، يمنح تغطية كاملة ولوناً حيوياً وثباتاً ممتازاً لعدة ساعات."),
        ("كيف يُستخدم بالشكل الصحيح؟", "مرري الروج من منتصف الشفة العليا للأطراف ثم الشفة السفلى لغطاء متكامل."),
        ("هل يسبب جفاف أو تشقق الشفتين؟", "لا، فورمولا مرطبة بالفيتامينات تحافظ على ليونة الشفتين دون جفاف."),
        ("ما هو بلد صنع روج هيري؟", "صُنع وفق أعلى معايير الجودة والمكياج العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع مستحضرات التجميل لدى إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يناسب جميع ألوان البشرة؟", "نعم، اللون الأحمر الكلاسيكي يناسب ويبرز جمال كافة ألوان البشرة."),
        ("ما هي رائحة الروج؟", "يتميز برائحة ناعمة ولطيفة ممتعة أثناء التطبيق."),
        ("هل ينزلق بسلاسة على الشفتين؟", "نعم، قوام كريمي مخملي ينزلق بمرونة فائقة."),
        ("هل أنبوب الروج مناسب للحقيبة والسفر؟", "نعم، أنبوب أنيق ومدمج مثالي لحقيبة اليد والمكياج."),
        ("كيف أحتفظ بأنبوب الروج؟", "يُحفظ في مكان بارد وجاف بعيداً عن الحرارة والشمس."),
        ("هل يمنح مظهر شفاه ممتلئة؟", "نعم، التغطية المخملية تمنح الشفتين مظهراً جذاباً وممتلئاً."),
        ("هل يناسب الاستخدام اليومي والمناسبات؟", "ممتاز جداً للمناسبات والسهرات والاستخدام اليومي الجذاب."),
        ("هل العبوة محكمة الغلق؟", "تأتي في أنبوب راقٍ بغطاء محكم يمنع الكسر والذوبان."),
        ("هل يترك أثراً لزجاً؟", "لا، يمنح لمسة نهائية مخملية ساتانية غير لزجة."),
        ("هل يناسب جميع الأعمار؟", "مناسب للمراهقات والبالغين من سن 15 سنة فما فوق."),
        ("هل يمكن استخدامه مع ملمع الشفاه (Lip Gloss)؟", "نعم، يمكن إضافة ملمع شفاف فوقه لإطلالة زجاجية براقة."),
        ("هل يزول بسرعة مع الأكل؟", "يثبت لعدة ساعات ويُفضل تجديده خفيفاً بعد الوجبات."),
        ("هل يحتوي على مواد ضارة؟", "تركيبة مجربة ومطورة طبقاً لمعايير سلامة التجميل."),
        ("هل يساعد في إخفاء خطوط الشفاه؟", "نعم، الترطيب الكثيف ينعم الخطوط ويغطيها بسلاسة."),
        ("هل هو الروج الأحمر المفضل لدى الفتيات؟", "نعم، روج هيري الأحمر الكلاسيكي الاختيار الأكثر جاذبية وسحراً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الحفلات والمناسبات الرسمية؟", "نعم، يمنح الشفتين حضوراً ملكياً في المناسبات."),
        ("هل أنبوبة الروج سهلة الفتح والاستعمال؟", "نعم، تصميم لولبي سلس وسهل الفتح والاستخدام.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Hery Lipstick</strong> is the classic luxury red lipstick designed to coat your lips in rich, vibrant velvet red color while delivering long-lasting hydration. Formulated by Hery Cosmetics, it is enriched with Vitamin E and moisturizing emollients to ensure smooth, seamless glide.</p>
<p>Delivering full-coverage pigment from the first swipe, Hery Red Lipstick resists drying and feathering, providing a comfortable satin-velvet finish that enhances your lips' natural beauty for all occasions.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Rich Classic Velvet Red Color:</strong> Provides full-coverage intense red pigment in a single swipe.</li>
  <li><strong>Enriched with Vitamin E Hydration:</strong> Prevents dry lip flaking and retains moisture all day.</li>
  <li><strong>Long-Lasting Comfortable Wear:</strong> Resists smudging and feathering for hours of radiant confidence.</li>
  <li><strong>Seamless Smooth Glide:</strong> Creamy texture glides effortlessly across lips without clumping.</li>
  <li><strong>Satin-Velvet Plumping Finish:</strong> Imparts a fuller, radiant, and luxurious lip look for every event.</li>
  <li><strong>Sleek Compact Tube:</strong> Elegant tube packaging fits perfectly in any handbag or beauty kit.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Prep):</strong> Gently exfoliate lips and apply a light lip balm if needed.</li>
  <li><strong>Step 2 (Apply):</strong> Glide Hery Red Lipstick from the center of upper lip outward toward corners.</li>
  <li><strong>Step 3 (Define):</strong> Fill in lower lip and re-apply for bolder color intensity.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Rich Velvet Red Pigments:</strong> Provide intense color payoff and full coverage.</li>
  <li><strong>Vitamin E & Natural Emollients:</strong> Nourish lip skin and prevent dry flaking.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external lip cosmetic application only.</li>
  <li>Keep away from high heat and direct sunlight to prevent lipstick melting.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Any woman seeking a classic, hydrating, long-lasting velvet red lipstick for all occasions.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Hery</td></tr>
  <tr><th>Category</th><td>Makeup / Moisturizing Velvet Lipsticks</td></tr>
  <tr><th>Product Type</th><td>Classic Hydrating Velvet Red Lipstick</td></tr>
  <tr><th>Volume/Weight</th><td>Single Bullet Tube</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Lip Makeup)</td></tr>
  <tr><th>Finish</th><td>Velvet red, hydrated, plump & smudge-resistant lips</td></tr>
  <tr><th>Texture</th><td>Creamy smooth-gliding velvet lipstick</td></tr>
  <tr><th>Fragrance</th><td>Subtle pleasant scent</td></tr>
  <tr><th>Active Ingredients</th><td>Red Pigments, Vitamin E, Moisturizing Emollients</td></tr>
  <tr><th>Country of Origin</th><td>China / Korea</td></tr>
  <tr><th>Manufacturer</th><td>Hery Cosmetics</td></tr>
  <tr><th>Age Group</th><td>All Ages (15+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Vitamin E & Velvet Lip Pigment Fixation</h2>

<h3>What problem does this solve?</h3>
<p>Hery Red Lipstick resolves dry lip cracking, uneven lipstick clumping, and rapid color fading.</p>

<h3>Why choose Hery Red Lipstick?</h3>
<p>Vitamin E emollients seal moisture into delicate lip skin, allowing rich red pigments to adhere smoothly without drying or feathering.</p>"""

    en_faqs = [
        ("What is Hery Lipstick?", "It is a classic luxury velvet red lipstick enriched with Vitamin E for intense color and long-lasting hydration."),
        ("What are the benefits of Vitamin E in lipstick?", "Hydrates lips, prevents dry flaking, and ensures a smooth velvet coverage."),
        ("Does it provide rich red color payoff?", "Yes, delivers intense full-coverage red pigment in a single swipe."),
        ("How do I apply it correctly?", "Glide from the center of upper lip outward, then fill in lower lip for full intensity."),
        ("Does it dry out or crack lips?", "No, moisturizing Vitamin E formula keeps lips soft and supple without drying."),
        ("Where is Hery manufactured?", "Produced following international cosmetics formulation standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All makeup products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it suit all skin tones?", "Yes, classic red is a universal shade that flatters all skin tones beautifully."),
        ("What fragrance does Hery Lipstick have?", "Features a subtle, pleasant sweet scent."),
        ("Does it glide smoothly on lips?", "Yes, creamy velvet texture glides effortlessly across lips."),
        ("Is the lipstick tube handbag-friendly?", "Yes, compact elegant tube fits easily into makeup pouches and handbags."),
        ("How should I store the lipstick?", "Store in a cool, dry place away from heat and direct sunlight."),
        ("Does it give a plumper lip finish?", "Yes, satin-velvet coverage enhances lip fullness and radiance."),
        ("Is it suitable for daily and evening wear?", "Yes, perfect for daily wear, parties, and special evening events."),
        ("Is the packaging secure?", "Yes, comes in a sturdy sleek tube with a secure cap."),
        ("Does it leave a sticky feel?", "No, provides a comfortable non-sticky satin-velvet finish."),
        ("What age group is it for?", "Suitable for teens and adults aged 15+."),
        ("Can it be paired with lip gloss?", "Yes, clear lip gloss can be layered over it for a high-shine glassy look."),
        ("Does it stay on for hours?", "Yes, offers long-wearing pigment that stays vibrant for hours."),
        ("Does it contain harmful chemicals?", "Dermatologically tested and safety-certified."),
        ("Does it smooth out lip lines?", "Yes, deep hydration smooths fine lip lines for flawless wear."),
        ("Is it a popular classic red lipstick?", "Yes, Hery Red Lipstick is a favorite classic red choice."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for formal evening events?", "Yes, delivers a royal classic red look for formal evening galas."),
        ("Is the twist bullet mechanism smooth?", "Yes, smooth twist bullet mechanism for easy precise application.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1818",
        "sku": "EK-1818",
        "gtin": "6922946005793",
        "category": "المكياج / أحمر الشفاه المخملي والمرطب",
        "brand": "Hery",
        "ar": {
            "title": "روج احمر شفاة من هيري",
            "meta_title": "روج احمر شفاة هيري | صيدلية إكليل أبها",
            "meta_description": "اشتري روج احمر شفاة من هيري. أحمر شفاه كلاسيكي مخملي مرطب بفيتامين E وثبات يدوم طويلاً. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["هيري", "روج_هيري", "احمر_شفاة", "روج_احمر", "إكليل_أبها"]
        },
        "en": {
            "title": "Hery Lipstick",
            "meta_title": "Hery Red Lipstick | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Hery Lipstick. Classic velvet red moisturizing lipstick with Vitamin E. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["hery", "hery_lipstick", "red_lipstick", "velvet_lips", "ekleel_abha"]
        },
        "schema": {
            "brand": "Hery",
            "category": "Makeup / Lipstick",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "hery-lipstick.webp",
            "alt": "Hery Lipstick",
            "title": "Hery Lipstick"
        }
    }

print("Loaded Batch 22 builders (25 FAQs updated)")
