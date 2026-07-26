import json, os

def build_vicks_vaporub(prod_id, weight_str, gtin, img_slug):
    title_ar = f"مرهم فابورب الموضعي من فيكس لتخفيف أعراض البرد والاحتقان - {weight_str}"
    title_en = f"Vicks VapoRub Topical Ointment {weight_str}"

    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مرهم فابورب الموضعي من فيكس لتخفيف أعراض البرد والاحتقان - {weight_str} (Vicks VapoRub Topical Ointment {weight_str})</strong> البلسم الطبيعي المهدئ والأكثر موثوقية عالمياً لتخفيف احتقان الصدر والانف، تهدئة السعال، وتسكين آلام العضلات المصاحبة لنزلات البرد والإنفلونزا. يرتكز هذا المرهم الأسطوري من فيكس (Vicks) على فورمولا منشنية تجمع بين الزيوت العطرية الطيارة: المنثول (Menthol)، الكافور (Camphor)، وزيت الكافور/الإيكاليبتوس (Eucalyptus Oil).</p>
<p>يمتاز مرهم فيكس بفاعلية مزدوجة: حيث ينبعث منه بخار منشط يفتح الممرات التنفسية المسدودة عند استنشاقه، بينما يوفر تدليكه الموضعي دفئاً مهدئاً يريح العضلات المشدودة والصدر ليضمن لكِ ولعائلتكِ نوماً هادئاً ومريحاً طوال الليل.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تخفيف فورية لاحتقان الأنف والصدر:</strong> الأبخرة الطيارة تفتح الممرات التنفسية وتسهل التنفس.</li>
  <li><strong>تهدئة السعال وآلام البرد:</strong> يخفف السعال المزعج المرتبط بنزلات الفلو والبرد.</li>
  <li><strong>تركيبة المنثول والكافور والإيكاليبتوس:</strong> زيوت طبيعية طيارة تمنح إحساساً مهدئاً بالدفء والانتعاش.</li>
  <li><strong>تسكين آلام العضلات والمفاصل:</strong> تدليكه على الرقبة والصدر والظهر يريح الآلام العضلية الخفيفة.</li>
  <li><strong>تسهيل النوم الهادئ لجميع العائلة:</strong> يوفر راحة تنفسية تدوم حتى 8 ساعات لليلة نوم مريحة.</li>
  <li><strong>عبوة مدمجة {weight_str}:</strong> حجم مرطب طبي ممتاز ومناسب لجميع أفراد الأسرة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق الموضعي):</strong> وضعي طبقة مناسبة من مرهم فيكس فابورب على الصدر، الرقبة، والظهر دلكي برفق لعدة دقائق.</li>
  <li><strong>الخطوة الثانية (الاستنشاق البخاري):</strong> يمكن إضافة ملعقتين صغار من المرهم في وعاء ماء ساخن (غير مغلي) واستنشاق الأبخرة المنبعثة ببطء.</li>
  <li><strong>الخطوة الثالثة (التغطية):</strong> ارتدي ملابس دافئة فضفاضة للسماح للأبخرة بالتصاعد نحو الأنف والفم.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>المنثول الطبيعي (Menthol 2.82%):</strong> يمنح شعوراً بالانتعاش ويفك انسداد الأنف.</li>
  <li><strong>الكافور (Camphor 5.26%):</strong> يسكن آلام الصدر والعضلات ويهدئ السعال.</li>
  <li><strong>زيت الإيكاليبتوس (Eucalyptus Oil 1.33%):</strong> يطهر الممرات التنفسية ويسهل التنفس.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي أو الاستنشاق البخاري فقط؛ لا يبتلع المرهم ولا يوضع داخل فتحات الأنف.</li>
  <li>تجنبي وضعه على الجروح المفتوحة أو البشرة التالفة أو بالقرب من العينين.</li>
  <li>غير مناسب للأطفال دون سن سنتين (2 سنة).</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من احتقان الأنف، انسداد الصدر، السعال، وآلام البرد العضلية لجميع العائلة (فوق سنتين).</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>فيكس (Vicks)</td></tr>
  <tr><th>الفئة</th><td>الأدوية والمستلزمات الطبية / مراهم تخفيف البرد والاحتقان</td></tr>
  <tr><th>نوع المنتج</th><td>مرهم موضي واستنشاقي لتهدئة أعراض البرد ({weight_str})</td></tr>
  <tr><th>الحجم/الوزن</th><td>{weight_str}</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (تطبيب موضي على الصدر والظهر)</td></tr>
  <tr><th>المظهر النهائي</th><td>راحة تنفسية، تخفيف الاحتقان، ونوم هادئ خالي من السعال</td></tr>
  <tr><th>الملمس</th><td>مرهم زيتي ناعم ينبعث منه أبخرة منعشة</td></tr>
  <tr><th>العطر</th><td>عطر المنثول والإيكاليبتوس الطبي والمنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>منثول، كافور، زيت الإيكاليبتوس، زيت جوزة الطيب، فازلين</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا / المملكة المتحدة (Procter & Gamble)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Procter & Gamble (P&G / Vicks)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والأطفال (من سنتين فما فوق)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد مرهم فيكس فابورب (Vicks VapoRub)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مرهم فيكس فابورب مشكلة انسداد الأنف، احتقان الصدر، السعال المزعج، وآلام العضلات الناتجة عن نزلات البرد.</p>

<h3>لماذا تنجح أبخرة فيكس؟</h3>
<p>لأن الحرارة الطبيعية للجسم تبخر مركبات المنثول والإيكاليبتوس، مما يرسل إشارات حسية للمخ بتحسين تدفق الهواء وتخفيف السعال.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التدليك قبل النوم:</strong> دلكي الصدر والظهر بالمرهم قبل النوم مباشرة لنوم هادئ.<br>
2. <strong>ارتداء ملابس فضفاضة:</strong> لا تغطي منطقة الصدر بضمادات محكمة لتصاعد الأبخرة.<br>
3. <strong>تجنب التسخين المباشر:</strong> لا تسخني المرهم بالميكروويف أو الماء المغلي على النار.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مرهم فيكس يوضع داخل فتحات الأنف لنتائج أسرع."<br>
<strong>الحقيقة:</strong> يمنع وضع فيكس داخل فتحات الأنف؛ يوضع فقط على الصدر والرقبة والظهر الخارجي.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تستهدف أبخرة المنثول والكافور مستقبلا Cold Receptors (TRPM8) في الممرات الأنفية والصدرية، مما يمنح إحساساً بالانتعاش ويفك الاحتقان فورياً.</p>"""

    faqs = [
        (f"ما هو مرهم فابورب الموضعي من فيكس - {weight_str}؟", f"هو مرهم طبي موضي غني بالمنثول والكافور والإيكاليبتوس لتخفيف احتقان الصدر والأنف والسعال الناجم عن البرد."),
        ("ما هي فوائد المنثول والكافور في مرهم فيكس؟", "تفتح الأبخرة الطيارة الممرات التنفسية المسدودة وتخفف السعال وآلام العضلات."),
        ("هل يساعد في تحسين النوم أثناء نزلات البرد؟", "نعم، يوفر راحة تنفسية مستمرة تدوم حتى 8 ساعات لليلة نوم هادئة."),
        (f"ما وزن العبوة؟", f"تأتي العبوة بحجم {weight_str}."),
        ("كيف يُستخدم بالشكل الصحيح؟", "دلكي كمية من المرهم على الصدر والرقبة والظهر، أو استنشقي أبخرته في وعاء ماء ساخن."),
        ("هل يوضع داخل فتحات الأنف؟", "لا، يوضع فقط موضعياً على الصدر والرقبة والظهر ولا يدخل فتحات الأنف."),
        ("ما هي الفئة العمرية المناسبة؟", "مناسب للبالغين والأطفال من عمر سنتين (2 سنة) فما فوق."),
        ("ما هو بلد صنع مرهم فيكس؟", "صُنع بواسطة شركة بروكتر آند جامبل (P&G / Vicks) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات فيكس لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يهدئ آلام العضلات المرافقة للإنفلونزا؟", "نعم، يوفر دفئاً موضعياً يسكن آلام العضلات والمفاصل الخفيفة."),
        ("هل يمكن استخدامه كاستنشاق بخاري؟", "نعم، يذاب ملعقتين صغار في وعاء ماء ساخن لاستنشاق البخار دون غلي قسري."),
        ("ما هي رائحة مرهم فيكس؟", "يتميز برائحة المنثول والإيكاليبتوس العطرية الطبية المنعشة."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعبوتها المغلقة محكماً."),
        ("هل يناسب جميع أفراد العائلة؟", "نعم، مرهم عائلي طبي أساسي لكل منزل."),
        ("هل يسبب حساسية بالجلد؟", "تركيبة مجربة طبياً وآمنة للاستخدام الموضعي."),
        ("هل العبوة {weight_str} اقتصادية؟", "نعم، عبوة متينة تدوم لعدة مواسم شتاء."),
        ("هل يحتاج إلى وصفة طبية؟", "مستحضر طبي آمن متاح بدون وصفة طبية."),
        ("هل يوضع على الجروح أو الحروق؟", "لا، يمنع وضعه على الجلد المصاب بجروح أو حروق."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة دائرية بغطاء لولبي محكم يمنع تطاير الزيوت."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستخدم 2 إلى 3 مرات يومياً وخاصة قبل النوم."),
        ("هل يساعد في فك انسداد الأنف في الشتاء؟", "نعم، استنشاق أبخرته يفك الانسداد الأنفي فورياً."),
        ("هل يناسب الحوامل؟", "يُفضل استشارة الطبيب قبل الاستخدام للحوامل والمرضعات."),
        ("هل يمكن وضعه على القدمين وارتداء الجوارب؟", "نعم، طريقة شائعة تمنح دفئاً وراحة للجسم قبل النوم."),
        ("هل هو المرهم الأول عالمياً لنزلات البرد؟", "نعم، فيكس الماركة رقم 1 عالمياً في تخفيف الاحتقان."),
        ("هل يتوفر بأحجام مختلفة لدى إكليل أبها؟", "نعم، يتوفر بحجمي 50جم و100جم لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>Vicks VapoRub Topical Ointment {weight_str}</strong> is the world's #1 trusted medicated decongestant ointment designed to relieve nasal congestion, soothe coughs, and ease minor muscle aches associated with colds and flu. Formulated by Vicks, it fuses active aromatic vapors: Menthol, Camphor, and Eucalyptus Oil.</p>
<p>Vicks VapoRub delivers dual-action relief: inhaling its medicated vapors instantly opens blocked airways, while massaging it topically onto chest and neck provides a warm soothing sensation to promote a restful night's sleep.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Instant Nasal & Chest Decongestion:</strong> Medicated vapors dislodge nasal blockage for easier breathing.</li>
  <li><strong>Soothes Cough & Cold Symptoms:</strong> Calms troublesome coughs associated with flu and common cold.</li>
  <li><strong>Menthol, Camphor & Eucalyptus Formula:</strong> Aromatic essential oils provide warm soothing relief.</li>
  <li><strong>Eases Minor Muscle Aches:</strong> Topically massaged on neck, chest, and back to relieve sore muscles.</li>
  <li><strong>Promotes Restful Sleep:</strong> Provides up to 8 hours of continuous breathing comfort for nocturnal rest.</li>
  <li><strong>Compact {weight_str} Tub:</strong> High-value family size ideal for every medicine cabinet.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Topical Application):</strong> Apply a thick layer of Vicks VapoRub onto chest, neck, and back; massage gently for a few minutes.</li>
  <li><strong>Step 2 (Steam Inhalation):</strong> Alternatively, melt 2 teaspoons into a bowl of hot (not boiling) water and inhale vapors slowly.</li>
  <li><strong>Step 3 (Cover):</strong> Wear loose warm clothing to allow vapors to rise toward nose and mouth.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Menthol (2.82%):</strong> Provides cooling sensation and clears nasal passages.</li>
  <li><strong>Camphor (5.26%):</strong> Relieves chest tightness, muscle aches, and calms coughs.</li>
  <li><strong>Eucalyptus Oil (1.33%):</strong> Clears respiratory pathways and eases breathing.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical application or steam inhalation only; do not swallow or place inside nostrils.</li>
  <li>Do not apply to open wounds, damaged skin, or near eyes.</li>
  <li>Not suitable for children under 2 years old.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from nasal congestion, chest tightness, coughs, or cold-related muscle aches (ages 2+).</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Vicks</td></tr>
  <tr><th>Category</th><td>Medicine & Healthcare / Medicated Decongestant Ointments</td></tr>
  <tr><th>Product Type</th><td>Topical & Inhalation Decongestant Ointment ({weight_str})</td></tr>
  <tr><th>Volume/Weight</th><td>{weight_str}</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Topical Chest & Back Application)</td></tr>
  <tr><th>Finish</th><td>Decongested airways, cough relief & restful night sleep</td></tr>
  <tr><th>Texture</th><td>Soothing medicated vaporising ointment</td></tr>
  <tr><th>Fragrance</th><td>Medicated Menthol & Eucalyptus aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Menthol, Camphor, Eucalyptus Oil, Nutmeg Oil, Petrolatum</td></tr>
  <tr><th>Country of Origin</th><td>Germany / UK (Procter & Gamble)</td></tr>
  <tr><th>Manufacturer</th><td>Procter & Gamble (P&G / Vicks)</td></tr>
  <tr><th>Age Group</th><td>Adults & Children (Ages 2+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Aromatic Vapors & TRPM8 Cold Receptors</h2>

<h3>What problem does this solve?</h3>
<p>Vicks VapoRub resolves nasal congestion, chest tightness, nocturnal coughs, and flu muscle aches.</p>

<h3>Why choose Vicks VapoRub?</h3>
<p>Body heat volatilizes Menthol and Camphor vapors, triggering TRPM8 cold receptors in nasal passages to simulate airflow and calm cough reflexes.</p>"""

    en_faqs = [
        (f"What is Vicks VapoRub Topical Ointment {weight_str}?", f"It is a medicated decongestant ointment formulated with Menthol, Camphor, and Eucalyptus Oil to relieve cold symptoms."),
        ("What are the benefits of Menthol and Camphor?", "Volatile vapors open blocked nasal passages, calm coughs, and ease sore muscle aches."),
        ("Does it promote better sleep during colds?", "Yes, provides up to 8 hours of continuous breathing comfort for restful sleep."),
        (f"What volume is contained in this tub?", f"It comes in a {weight_str} jar."),
        ("How do I apply it correctly?", "Massage onto chest, neck, and back, or melt in hot water for steam inhalation."),
        ("Can it be placed inside nostrils?", "No, apply topically to chest and back only; never place inside nostrils."),
        ("What age group is it suitable for?", "Suitable for adults and children aged 2 years and older."),
        ("Where is Vicks manufactured?", "It is produced by Procter & Gamble (P&G / Vicks) under strict global medical standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Vicks products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it soothe flu muscle aches?", "Yes, topically massaged heat calms sore chest and back muscles."),
        ("Can it be used for steam inhalation?", "Yes, melt 2 teaspoons into a bowl of hot water to inhale vapors."),
        ("What scent does Vicks have?", "Features a clean medicated Menthol and Eucalyptus aroma."),
        ("How should I store the jar?", "Store in a cool, dry place with lid tightly closed."),
        ("Is it a household essential?", "Yes, the #1 trusted medicine cabinet staple for winter colds."),
        ("Is it safe for skin?", "Dermatologically tested and safe for topical chest application."),
        (f"Is the {weight_str} jar long-lasting?", "Yes, a durable jar lasting through winter cold seasons."),
        ("Does it require a prescription?", "No, it is a safe over-the-counter medicated ointment."),
        ("Can it be applied on cuts or burns?", "No, do not apply to broken, wounded, or burned skin."),
        ("Is the jar securely sealed?", "Yes, comes in a sturdy round jar with a screw lid."),
        ("How often can it be applied daily?", "Apply 2 to 3 times daily, especially before bedtime."),
        ("Does it clear winter nasal blockages?", "Yes, inhaling vapors opens blocked nasal airways rapidly."),
        ("Is it safe during pregnancy?", "Consult a physician before use if pregnant or nursing."),
        ("Can it be applied on feet with socks?", "Yes, applying to feet before wearing socks is a popular soothing bedtime routine."),
        ("Is Vicks the world's #1 cold rub?", "Yes, Vicks is the #1 globally trusted decongestant rub."),
        ("Are different sizes available at Ekleel Abha?", "Yes, available in 50g and 100g sizes at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "الأدوية والمستلزمات الطبية / مراهم تخفيف البرد والاحتقان",
        "brand": "Vicks",
        "ar": {
            "title": title_ar,
            "meta_title": f"مرهم فيكس فابورب {weight_str} | صيدلية إكليل أبها",
            "meta_description": f"اشتري {title_ar}. لتخفيف احتقان الصدر والأنف والسعال بالمنثول والكافور. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["فيكس", "مرهم_فيكس", "فابورب", "تخفيف_البرد", "إكليل_أبها"]
        },
        "en": {
            "title": title_en,
            "meta_title": f"Vicks VapoRub Ointment {weight_str} | Ekleel Abha Pharmacy",
            "meta_description": f"Buy original {title_en}. Relieves nasal congestion, coughs, & chest tightness with Menthol & Camphor. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["vicks", "vaporub", "decongestant_ointment", "cold_relief", "ekleel_abha"]
        },
        "schema": {
            "brand": "Vicks",
            "category": "Medicine / Decongestant Ointment",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"{img_slug}.webp",
            "alt": title_en,
            "title": title_en
        }
    }

def create_product_1802():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم دوف الوردي المرطب للعناية بالبشرة والجسم - 150 مل (Dove Body Care Cream 150ml)</strong> المستحضر الوردي الأسطوري المفضل عالمياً لإعادة النعومة المخملية والترطيب العميق للبشرة. يرتكز هذا الكريم الكلاسيكي من دوف على فورمولا السيروم المغذي (Deep Care Complex) والزيوت المرطبة الخفيفة، حيث ينفذ في عمق خلايا الجلد ليمنحكِ ترطيباً مكثفاً يدوم حتى 24 ساعة دون ترك أي أثر دهني لزج.</p>
<p>يمتاز كريم دوف الوردي بقوام ناعم جداً يناسب بشرة الوجه، اليدين، والجسم بالكامل، ليترك جلدكِ مشرقاً، ناعماً كالحرير، وبرائحة دوف النظيفة الزكية التي تعزز إحساسكِ بالنظافة والأنوئة طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب عميق لـ 24 ساعة:</strong> يزود ألياف البشرة بالمرطبات الطبيعية ويمنع الجفاف والتكسر.</li>
  <li><strong>مركب Deep Care Complex المغذي:</strong> يغذي خلايا الجلد عميقاً ويحسن مرونة ونعومة البشرة.</li>
  <li><strong>مناسب للوجه، اليدين، والجسم:</strong> كريم شامل متعدد الاستخدامات يرطب كافة مناطق البشرة الجافة.</li>
  <li><strong>قوام ناعم غير دهني:</strong> يمتص فورياً في البشرة دون إبقاء لزوجة أو ثقل زيتي.</li>
  <li><strong>رائحة دوف النظيفة المميزة:</strong> يمنح جسمكِ عبيراً منعشاً وناعماً يرافقكِ طوال اليوم.</li>
  <li><strong>عبوة دائرية سعة 150 مل:</strong> حجم ممتازة ومريحة للحمل والاستخدام اليومي المتكرر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> استحممي أو اغسلي المنطقة المراد ترطيبها وجففيها بلطف.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي كمية مناسبة من كريم دوف الوردي على الوجه، اليدين، أو الجسم.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي بحركات دائرية خفيفة حتى يتم امتصاص الكريم بالكامل (يُستعمل صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>سيروم دوف المغذي (Deep Care Complex):</strong> يغذي خلايا البشرة ويحفظ ترطيبها الداخلي.</li>
  <li><strong>مرطبات جليسرينية خفيفة:</strong> تطري الجلد وتمنع جفاف الأكواع والركب واليدين.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على بشرة الوجه والجسم فقط.</li>
  <li>تجنبي ملامسة الكريم المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن كريم وردي كلاسيكي متعدد الاستخدامات لترطيب الوجه واليدين والجسم بنعومة 24 ساعة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>دوڤ (Dove)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات ترطيب الوجه والجسم الكلاسيكية</td></tr>
  <tr><th>نوع المنتج</th><td>كريم ترطيب مرطب شامل للوجه والجسم (150ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>150 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (الجافة، العادية، الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة، حريرية، مرطبة لـ 24 ساعة ومشرقة</td></tr>
  <tr><th>الملمس</th><td>كريم ناعم غني سريع الامتصاص غير دهني</td></tr>
  <tr><th>العطر</th><td>عطر دوف الوردي الكلاسيكي للنظافة</td></tr>
  <tr><th>المكونات النشطة</th><td>سيروم Deep Care Complex، جليسرين مرطب، زيوت مغذية</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الهند (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (دوڤ)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد كريم دوف الوردي المرطب (Dove Body Care)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم دوف الوردي مشكلة جفاف بشرة الوجه واليدين والجسم، خشونة الأكواع والركب، وفقدان النضارة الطبيعية.</p>

<h3>لماذا تنجح تركيبة دوف الكلاسيكية؟</h3>
<p>لأن مركب Deep Care Complex يندمج مع ليبيدات الجلد، مما يشكل حجاب ترطيب يمنع تبخر الماء لـ 24 ساعة دون لزوجة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق المباشر بعد الغسيل:</strong> وضعي الكريم فورياً بعد غسيل الوجه واليدين لحبس الترطيب.<br>
2. <strong>التركيز على المناطق الجافة:</strong> دلكي الأكواع والركب واليدين بالمرهم مرتين يومياً.<br>
3. <strong>الاستخدام كقاعدة مكياج:</strong> مرطب ممتاز كقاعدة مهدئة قبل وضع كريم الأساس.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات الجسم تثقل بشرة الوجه وتسبب انسداد المسام."<br>
<strong>الحقيقة:</strong> كريم دوف الوردي مصمم بتركيبة ناعمة خفيفة متوازنة تناسب بشرة الوجه والجسم دون سد المسام.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتكامل المغذيات الطبيعية مع حواجز البشرة الدهنية (Lipid Barrier)، مما يزيد مرونة الخلايا ويحافظ على الملمس الحريري.</p>"""

    faqs = [
        ("ما هو كريم دوف الوردي المرطب للعناية بالبشرة والجسم 150 مل؟", "هو كريم كلاسيكي وردي مرطب غني بـ Deep Care Complex لترطيب وتنعيم الوجه، اليدين، والجسم لـ 24 ساعة."),
        ("ما هي فوائد مركب Deep Care Complex؟", "يغذي خلايا البشرة عميقاً، يحسن المرونة، ويحفظ الرطوبة الداخلية لـ 24 ساعة."),
        ("هل يناسب الوجه واليدين والجسم معاً؟", "نعم، كريم شامل متعدد الاستخدامات يرطب الوجه، اليدين، وكامل الجسم ب أمان."),
        ("ما حجم العبوة؟", "تأتي بحجم 150 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي كمية على البشرة ودلكي بحركات دائرية خفيفة حتى الامتصاص الكامل مرتين يومياً."),
        ("هل يترك أثراً دهنياً لزجاً؟", "لا، يمتص بسرعة ليعطي ملمساً ناعماً كالحرير دون لزوجة دهنية."),
        ("ما هو بلد صنع كريم دوف؟", "صُنع بواسطة شركة يونيلفر (Unilever) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات دوف لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("ما هي رائحة كريم دوف الوردي؟", "يتميز برائحة دوف الوردي الكلاسيكية الزكية للنظافة والانتعاش."),
        ("هل يرطب الأكواع والركب الجافة؟", "نعم، ممتاز جداً لتنعيم وترطيب الأكواع والركب والكعبين الجافة."),
        ("هل يمكن استخدامه كمرطب قبل المكياج؟", "نعم، يمنح الوجه قاعدة ناعمة ومرطبة قبل وضع الفاونديشن."),
        ("هل يناسب جميع أنواع البشرة؟", "مناسب للبشرة العادية، الجافة، والحساسة."),
        ("هل يناسب جميع أفراد العائلة؟", "نعم، آمن وممتاز للأطفال والبالغين من سن 3 سنوات."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل العبوة 150 مل مناسبة للسفر والحقيبة؟", "نعم، حجم دائر مدمج ومثالي للحقيبة والسفر."),
        ("هل يساعد في تحسين إشراقة البشرة؟", "نعم، الترطيب 24 ساعة يعيد النضارة والإشراقة للجلد الجاف."),
        ("هل يناسب الصيف والشتاء؟", "نعم، يحمي البشرة من جفاف الشتاء وحر الصيف."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة دائرية أنيقة بغطاء محكم الحماية."),
        ("هل يحتوي على بارابين؟", "تركيبة مجربة ومطورة طبقاً لأعلى معايير السلامة."),
        ("هل يمنع تشقق اليدين؟", "نعم، ترطيبه المكثف يعالج وينعم تشققات اليدين."),
        ("هل يمتص بسهولة؟", "نعم، ينفذ بسهولة داخل خلايا البشرة."),
        ("هل يناسب الرجال والنساء؟", "نعم، مناسب لكلا الجنسين."),
        ("هل يمكن استخدامه بعد الحلاقة؟", "نعم، ممتاز لتهدئة وترطيب البشرة بعد الحلاقة."),
        ("هل هو الكريم الوردي الأسطوري الأكثر مبيعاً؟", "نعم، كريم دوف الوردي المفضل عالمياً لعقود طويلة."),
        ("هل يتوفر بأحجام أخرى لدى إكليل أبها؟", "نعم، تتوفر أحجام متعددة من كريمات دوف المرطبة.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Dove Body Care Cream 150ml</strong> is the world's legendary classic pink moisturizing cream designed to restore velvet softness and deep 24-hour hydration to your skin. Formulated with Dove's signature Deep Care Complex and lightweight moisturizing lipids, it penetrates deep into skin cells without leaving any greasy residue.</p>
<p>Featuring a smooth, fast-absorbing texture suitable for face, hands, and full body application, Dove Pink Cream leaves your skin touchably soft, radiant, and beautifully scented with Dove's clean signature aroma all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>24-Hour Deep Moisture:</strong> Feeds skin fibers with continuous hydration to prevent dry flaking.</li>
  <li><strong>Deep Care Complex Formula:</strong> Deeply nourishes skin cells and improves overall skin elasticity.</li>
  <li><strong>Multi-Purpose Face, Hand & Body Cream:</strong> Versatile all-in-one moisturizing cream for all dry areas.</li>
  <li><strong>Lightweight Non-Greasy Texture:</strong> Absorbs in seconds without leaving sticky or oily residue.</li>
  <li><strong>Classic Clean Dove Aroma:</strong> Envelops your body in a long-lasting fresh, clean fragrance.</li>
  <li><strong>Convenient 150ml Pink Tub:</strong> Iconic round tub size ideal for daily home and handbag use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Shower or wash the target area and gently pat dry.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a suitable amount of Dove Body Care Cream onto face, hands, or body.</li>
  <li><strong>Step 3 (Massage):</strong> Massage in gentle circular motions until fully absorbed; use twice daily (morning and evening).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Dove Deep Care Complex:</strong> Nourishes dermal cells and locks in internal moisture.</li>
  <li><strong>Hydrating Glycerin:</strong> Softens rough elbows, knees, and hands effectively.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external face, hand, and body moisturizing application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking the iconic classic pink moisturizing cream for 24-hour soft face, hand, and body skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Dove</td></tr>
  <tr><th>Category</th><td>Skincare / Classic Face & Body Moisturizing Creams</td></tr>
  <tr><th>Product Type</th><td>Multi-Purpose 24-Hour Hydrating Pink Cream (150ml)</td></tr>
  <tr><th>Volume/Weight</th><td>150 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Dry, Normal, Sensitive)</td></tr>
  <tr><th>Finish</th><td>Soft, silky, 24h hydrated & clean-scented skin</td></tr>
  <tr><th>Texture</th><td>Rich fast-absorbing smooth pink cream</td></tr>
  <tr><th>Fragrance</th><td>Classic clean Dove signature fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Deep Care Complex, Hydrating Glycerin</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / India (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever (Dove)</td></tr>
  <tr><th>Age Group</th><td>All Ages (3+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Deep Care Complex & All-Over Dermal Hydration</h2>

<h3>What problem does this solve?</h3>
<p>Dove Body Care Cream resolves skin dryness on face, hands, elbows, knees, and body flaking.</p>

<h3>Why choose Dove Pink Cream?</h3>
<p>Deep Care Complex integrates into intercellular lipids, providing a 24-hour hydration barrier that preserves skin softness without heaviness.</p>"""

    en_faqs = [
        ("What is Dove Body Care Cream 150ml?", "It is the iconic classic pink moisturizing cream enriched with Deep Care Complex to hydrate face, hands, and body for 24 hours."),
        ("What are the benefits of Deep Care Complex?", "Deeply nourishes skin cells, improves elasticity, and locks in internal moisture for 24 hours."),
        ("Is it safe for face, hands, and body?", "Yes, a versatile multi-purpose cream safe for facial skin, hands, and full body areas."),
        ("What volume is contained in this tub?", "It comes in a convenient 150ml round tub."),
        ("How do I apply it correctly?", "Massage gently into skin using circular motions until fully absorbed twice daily."),
        ("Does it leave a greasy residue?", "No, absorbs quickly leaving skin touchably silky without greasy film."),
        ("Where is Dove manufactured?", "It is produced by Unilever following global quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Dove products at Ekleel Abha are 100% original from certified distributors."),
        ("What scent does Dove Pink Cream have?", "Features the clean, refreshing classic signature Dove aroma."),
        ("Does it soften dry elbows and knees?", "Yes, highly effective at softening dry elbows, knees, heels, and hands."),
        ("Can it be used as a makeup primer?", "Yes, provides a smooth, hydrated base before foundation application."),
        ("Is it suitable for all skin types?", "Ideal for normal, dry, and sensitive skin types."),
        ("Is it safe for family use?", "Yes, safe for adults and children aged 3+."),
        ("How should I store the tub?", "Store in a cool, dry place away from direct heat."),
        ("Is the 150ml tub travel-friendly?", "Yes, compact round tub size fits easily into handbags and travel kits."),
        ("Does it improve dry skin radiance?", "Yes, 24-hour continuous moisture restores natural skin radiance."),
        ("Is it great for summer and winter?", "Yes, protects skin against winter cold dryness and summer heat."),
        ("Is the tub securely sealed?", "Yes, comes in an iconic round tub with a protective lid."),
        ("Is it paraben-free?", "Dermatologically tested and approved under global safety standards."),
        ("Does it heal cracked hands?", "Yes, deep hydration smooths and heals dry cracked hand skin."),
        ("Does it absorb easily?", "Yes, glides smoothly and absorbs into skin cells instantly."),
        ("Can both men and women use it?", "Yes, suitable for both men and women."),
        ("Can it be used post-shaving?", "Yes, excellent for calming and hydrating skin after shaving."),
        ("Is it the world's #1 favorite pink moisturizing cream?", "Yes, globally beloved for decades as the ultimate daily pink cream."),
        ("Are other sizes available at Ekleel Abha?", "Yes, Ekleel Abha offers various sizes of Dove moisturizing creams.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1802",
        "sku": "EK-1802",
        "gtin": "6281006409620",
        "category": "العناية بالبشرة / كريمات ترطيب الوجه والجسم الكلاسيكية",
        "brand": "Dove",
        "ar": {
            "title": "كريم دوف الوردي المرطب للعناية بالبشرة والجسم - 150 مل",
            "meta_title": "كريم دوف الوردي المرطب 150مل | صيدلية إكليل أبها",
            "meta_description": "اشتري كريم دوف الوردي المرطب للعناية بالبشرة والجسم (150 مل). ترطيب 24 ساعة بمجمع Deep Care Complex للوجه واليدين والجسم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["دوف", "كريم_دوف_الوردي", "ترطيب_البشرة", "كريم_الجسم", "إكليل_أبها"]
        },
        "en": {
            "title": "Dove Body Care Cream 150ml",
            "meta_title": "Dove Body Care Cream 150ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Dove Body Care Cream (150ml). Iconic pink moisturizing cream for face, hands & body with 24-hour hydration. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["dove", "pink_cream", "body_moisturizer", "24h_hydration", "ekleel_abha"]
        },
        "schema": {
            "brand": "Dove",
            "category": "Skincare / Body Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "dove-body-care-cream-150ml.webp",
            "alt": "Dove Body Care Cream 150ml",
            "title": "Dove Body Care Cream 150ml"
        }
    }

def build_vaseline_hand_nail(prod_id, title_ar, title_en, gtin, img_slug):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{title_ar}</strong> المستحضر الطبي المتقدم ورقم 1 عالمياً للعناية المركزة باليدين وتدعيم قوة الأظافر. يرتكز هذا الكريم المتطور من فازلين (Vaseline Intensive Care) على قطرات دقيقة من جل فازلين الأصلي (Vaseline Jelly Micro-Droplets) المعززة بالكيراتين الطبيعي (Keratin) وفيتامين E، حيث يتغلغل في عمق خلايا الجلد ليمنحكِ ترطيباً مكثفاً يمنع الجفاف ويعزز قوة الأظافر بـ 10 أضعاف في 2 أسابيع فقط.</p>
<p>يمتاز كريم فازلين الوردي بقوام كريمي غير دهني سريع الامتصاص يغلف اليدين والأظافر بحجاب حماية مغذٍ، مما يمنع جفاف الأظافر وتقصف الجلد المحيط بها ويترك يديكِ ناعمتين كالحرير طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>أظافر أقوى 10 أضعاف في أسبوعين:</strong> يقوي صحة الأظافر ويمنع تكسرها وتثلمها.</li>
  <li><strong>ترطيب عميق بقطرات فازلين الجل:</strong> يحبس الرطوبة في الجلد ويمنع الجفاف والتطير.</li>
  <li><strong>مدعم بالكيراتين وفيتامين E:</strong> يرمم الجلد المحيط بالأظافر (Cuticles) ويغذي الجذور.</li>
  <li><strong>امتصاص سريع وغير دهني:</strong> ينفذ في الجلد فورياً دون إبقاء أثر دهني لزج على الأيدي.</li>
  <li><strong>نعومة حريرية طوال اليوم:</strong> يترك يديكِ ملساء، رطبة، ومفعمة بالمرونة.</li>
  <li><strong>أنبوب مدمج سعة 75 مل:</strong> حجم ممتاز ومثالي لحمله في حقيبة اليد أو السفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق):</strong> وضعي كمية بحجم حبة البازلاء من كريم فازلين على كف اليدين والأظافر.</li>
  <li><strong>الخطوة الثانية (التدليك):</strong> دلكي اليدين، الأصابع، والجلد المحيط بالأظافر بعناية حتى يتم الامتصاص الكامل.</li>
  <li><strong>الخطوة الثالثة (التكرار):</strong> استخدميه بعد كل غسيل لليدين وقبل النوم لنتائج ممتازة.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>كيراتين طبيعي (Hydrolyzed Keratin):</strong> يقوي بنية صفائح الأظافر ويمنع تكسرها.</li>
  <li><strong>قطرات جل فازلين الدقيقة (Vaseline Jelly Micro-Droplets):</strong> تحفظ الرطوبة وتدعم ترميم الحاجز الدهني.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على اليدين والأظافر فقط.</li>
  <li>تجنبي ملامسة الكريم المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تعاني من جفاف اليدين، تقصف الأظافر، وتكسر الجلد المحيط بالأظافر.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>فازلين (Vaseline)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات ترطيب اليدين وتقوية الأظافر</td></tr>
  <tr><th>نوع المنتج</th><td>كريم العناية المركزة باليدين وتقوية الأظافر بالكيراتين (75ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>75 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة اليدين (الجافة، المجهدة، والهشة)</td></tr>
  <tr><th>المظهر النهائي</th><td>يدان ناعمتان كالحرير وأظافر أقوى بـ 10 أضعاف وخالية من التكسر</td></tr>
  <tr><th>الملمس</th><td>كريمي ناعم سريع الامتصاص غير دهني</td></tr>
  <tr><th>العطر</th><td>عطر الزهور الوردي الخفيف والزكي</td></tr>
  <tr><th>المكونات النشطة</th><td>كيراتين، قطرات فازلين الجل، فيتامين E، جليسرين</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة المتحدة / بولندا (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (فازلين)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 10 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الكيراتين وفازلين الجل للأظافر (Vaseline Healthy Hands)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم فازلين الوردي مشكلة جفاف وتخشن اليدين، تكسر وتثلم صفائح الأظافر، والجلد الميت حول الأظافر.</p>

<h3>لماذا تنجح تركيبة الكيراتين وفازلين؟</h3>
<p>لأن الكيراتين يقوي صفائح الأظافر، بينما تحفظ قطرات فازلين الجل الرطوبة لتجعل الأظافر أقوى 10 أضعاف في 2 أسابيع.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام بعد غسل اليدين:</strong> ضعي الكريم فورياً بعد غسيل اليدين بالصابون.<br>
2. <strong>تدليك الجلد المحيط بالأظافر:</strong> دلكي الـ Cuticles بالمرهم لتقوية أصول الأظافر.<br>
3. <strong>الاستخدام قبل النوم:</strong> وضعي كمية سخية قبل النوم ونامي بجلد ناعم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات اليدين تجعل الأيدي لزجة وتترك أثراً على الشاشات."<br>
<strong>الحقيقة:</strong> كريم فازلين الوردي مصمم بتركيبة غير دهنية سريعة الامتصاص تنفذ فورياً دون لزوجة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يتحد الكيراتين مع طبقات الأظافر الكيراتينية لزيادة صلابتها، بينما تشكل قطرات فازلين الجل غشائاً يمنع تبخر الماء من اليدين.</p>"""

    faqs = [
        (f"ما هو {title_ar}؟", f"هو كريم طبي مخصص للعناية باليدين وتقوية الأظافر بـ 10 أضعاف في أسبوعين بالكيراتين وقطرات فازلين الجل سعة 75 مل."),
        ("ما هي فوائد الكيراتين للأظافر؟", "يقوي بنية الأظافر، يمنع تكسرها وتثلمها، ويغذي الجلد المحيط بالأظافر."),
        ("هل يجعل الأظافر أقوى 10 أضعاف؟", "نعم، مثبت سريرياً في تقوية الأظافر بـ 10 أضعاف خلال أسبوعين من الاستخدام المنتظم."),
        ("ما حجم أنبوب الكريم؟", "يأتي بحجم 75 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي كمية على اليدين والأظافر ودلكي بعناية بعد غسل اليدين وقبل النوم."),
        ("هل يترك أثراً دهنياً لزجاً على اليدين؟", "لا، فورمولا سريعة الامتصاص وغير دهنية تنفذ فورياً دون لزوجة."),
        ("ما هو بلد صنع كريم فازلين؟", "صُنع بواسطة شركة يونيلفر (Unilever) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات فازلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يساعد في تنعيم الجلد المحيط بالأظافر (Cuticles)؟", "نعم، يرمم وينعم الجلد الميت والمحيط بالأظافر بفاعلية."),
        ("ما هي رائحة كريم فازلين الوردي؟", "يتميز برائحة ناعمة زكية وممتعة تمنح شعوراً بالنظافة."),
        ("هل يناسب الأيدي شديدة الجفاف؟", "نعم، قطرات فازلين الجل توفر ترطيباً عميقاً للأيدي شديدة الجفاف."),
        ("هل يناسب النساء والرجال؟", "نعم، مناسب لتنعيم وتقوية أظافر وأيدي النساء والرجال."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل حجم 75 مل مناسب للحقيبة والسفر؟", "نعم، حجم أنبوب أنيق ومدمج مثالي لحمل الحقيبة والسفر."),
        ("هل يساعد في منع تقصف الأظافر بالماء؟", "نعم، يحمي الأظافر من التأثر بالماء والمنظفات المنزلية."),
        ("هل يناسب الاستخدام اليومي المتكرر؟", "نعم، يُوصى باستخدامه بعد كل غسيل لليدين."),
        ("هل العبوة محكمة الغلق؟", "تأتي في أنبوب محكم بغطاء لولبي يمنع التسرب."),
        ("هل يحتوي على فيتامين E؟", "نعم، مدعم بفيتامين E لتغذية الجلد والأظافر."),
        ("هل يناسب جميع أنواع البشرة؟", "مناسب جداً للبشرة العادية، الجافة، والهشة."),
        ("هل يمتص فورياً على الجلد؟", "نعم، يمتص في ثوانٍ معدودة."),
        ("هل يعيد الشفافية والصحة للأظافر؟", "نعم، التغذية بالكيراتين تعيد اللمعان الطبيعي والصحي للأظافر."),
        ("هل ينصح به خبراء التجميل والعناية بالأظافر؟", "نعم، المنتج رقم 1 الموصى به للعناية باليدين والأظافر عالمياً."),
        ("هل يساعد في ترطيب الأكواع أيضاً؟", "يمكن استخدامه لترطيب الأكواع والمناطق الجافة المدمجة."),
        ("هل يترك ملمساً حريرياً؟", "نعم، يترك يديكِ ملساء ونظيفة طوال اليوم."),
        ("هل يتوفر بأحجام أخرى لدى إكليل أبها؟", "نعم، تتوفر كريمات فازلين المتعددة لليدين والجسم.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{title_en}</strong> is the world's #1 clinical hand and nail conditioning treatment engineered to deeply moisturize hands while making nails 10x stronger in just 2 weeks. Formulated by Vaseline Intensive Care, it fuses micro-droplets of original Vaseline Jelly with natural Keratin and Vitamin E.</p>
<p>Featuring a fast-absorbing, non-greasy texture, Vaseline Healthy Hands & Nails Cream coats hands and cuticles with a protective nutrient shield, stopping nail chipping, softening ragged cuticles, and leaving your hands touchably silky smooth all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>10x Stronger Nails in 2 Weeks:</strong> Clinically proven to fortify nail plates and stop chipping and breaking.</li>
  <li><strong>Vaseline Jelly Micro-Droplets Hydration:</strong> Seals moisture into dermal layers to heal dry hands.</li>
  <li><strong>Enriched with Keratin & Vitamin E:</strong> Restructures cuticles and feeds nail bed roots.</li>
  <li><strong>Fast-Absorbing & Non-Greasy:</strong> Absorbs in seconds without leaving oily residue on hands or screens.</li>
  <li><strong>All-Day Silky Smoothness:</strong> Keeps hands touchably soft, smooth, and supple throughout the day.</li>
  <li><strong>Compact 75ml Tube:</strong> Perfect handbag and travel size for on-the-go hand care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply):</strong> Dispense a pea-sized amount of Vaseline Hand and Nail cream onto palms and nails.</li>
  <li><strong>Step 2 (Massage):</strong> Massage gently into hands, fingers, and cuticles until fully absorbed.</li>
  <li><strong>Step 3 (Repeat):</strong> Reapply after handwashing and before bedtime for optimal nail strength.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Hydrolyzed Keratin:</strong> Fortifies structural nail plates preventing splitting and breaking.</li>
  <li><strong>Vaseline Jelly Micro-Droplets:</strong> Seal moisture and restore the skin's protective lipid barrier.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external hand and nail conditioning application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dry hands, weak brittle nails, or ragged cuticles wanting 10x stronger nails.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Vaseline</td></tr>
  <tr><th>Category</th><td>Skincare / Hand & Nail Conditioning Creams</td></tr>
  <tr><th>Product Type</th><td>10x Stronger Nails Intensive Hand & Nail Cream (75ml)</td></tr>
  <tr><th>Volume/Weight</th><td>75 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hand Skin Types (Dry, Damaged, Brittle Nails)</td></tr>
  <tr><th>Finish</th><td>Silky soft hands, 10x stronger nails & smooth cuticles</td></tr>
  <tr><th>Texture</th><td>Creamy fast-absorbing non-greasy hand lotion</td></tr>
  <tr><th>Fragrance</th><td>Subtle fresh pink floral scent</td></tr>
  <tr><th>Active Ingredients</th><td>Hydrolyzed Keratin, Vaseline Jelly Micro-Droplets, Vitamin E</td></tr>
  <tr><th>Country of Origin</th><td>United Kingdom / Poland (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever (Vaseline)</td></tr>
  <tr><th>Age Group</th><td>All Ages (10+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Hydrolyzed Keratin & Vaseline Jelly Micro-Droplets</h2>

<h3>What problem does this solve?</h3>
<p>Vaseline Healthy Hands & Nails Cream resolves dry hand roughness, nail splitting, and dry ragged cuticles.</p>

<h3>Why choose Vaseline Healthy Hands?</h3>
<p>Hydrolyzed Keratin fortifies nail keratin layers for 10x strength in 2 weeks, while Vaseline Jelly micro-droplets lock in moisture.</p>"""

    en_faqs = [
        (f"What is {title_en}?", f"It is an intensive hand and nail cream formulated with Keratin and Vaseline Jelly micro-droplets to make nails 10x stronger in 2 weeks."),
        ("What are the benefits of Keratin for nails?", "Fortifies nail plate structure, stops chipping, and nourishes cuticles."),
        ("Does it really make nails 10x stronger in 2 weeks?", "Yes, clinically proven to boost nail strength 10x in just 14 days of regular use."),
        ("What volume is contained in this tube?", "It comes in a compact 75ml tube."),
        ("How do I apply it correctly?", "Massage a small amount into hands, fingers, and cuticles after washing hands."),
        ("Does it leave a greasy residue on hands?", "No, fast-absorbing non-greasy formula absorbs in seconds without leaving oily film."),
        ("Where is Vaseline manufactured?", "It is produced by Unilever following global quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Vaseline products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it soften ragged cuticles?", "Yes, deeply repairs and smooths dry cuticles around nails."),
        ("What scent does it have?", "Features a subtle, pleasant fresh floral scent."),
        ("Is it suitable for very dry hands?", "Yes, Vaseline Jelly micro-droplets provide deep hydration for dry hands."),
        ("Can both men and women use it?", "Yes, suitable for both men and women."),
        ("How should I store the tube?", "Store in a cool, dry place away from direct heat."),
        ("Is the 75ml tube handbag-friendly?", "Yes, compact tube fits easily into handbags and travel kits."),
        ("Does it protect nails from water damage?", "Yes, guards nails against drying caused by water and household detergents."),
        ("Can it be used multiple times daily?", "Yes, recommended for use after every handwash."),
        ("Is the tube cap leak-proof?", "Yes, comes in a sturdy squeeze tube with a flip-top cap."),
        ("Does it contain Vitamin E?", "Yes, enriched with Vitamin E to nourish skin and nail beds."),
        ("Is it suitable for all skin types?", "Ideal for normal, dry, and brittle nail skin types."),
        ("Does it absorb quickly?", "Yes, absorbs completely into skin within seconds."),
        ("Does it restore natural nail shine?", "Yes, Keratin nourishment restores a healthy natural shine to nails."),
        ("Is it dermatologist and manicurist recommended?", "Yes, the #1 globally recommended hand and nail conditioning cream."),
        ("Can it be used on dry elbows?", "Yes, can be used for dry elbows and small dry patches."),
        ("Does it leave hands silky soft?", "Yes, leaves hands touchably soft and smooth all day."),
        ("Are other Vaseline hand creams available at Ekleel Abha?", "Yes, Ekleel Abha offers various Vaseline hand and body lotions.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "العناية بالبشرة / كريمات ترطيب اليدين وتقوية الأظافر",
        "brand": "Vaseline",
        "ar": {
            "title": title_ar,
            "meta_title": f"كريم فازلين لليدين والأظافر 75مل | صيدلية إكليل أبها",
            "meta_description": f"اشتري {title_ar}. تقوية الأظافر 10 أضعاف وترطيب كيراتين فازلين. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["فازلين", "كريم_فازلين_الوردي", "تقوية_الأظافر", "ترطيب_اليدين", "إكليل_أبها"]
        },
        "en": {
            "title": title_en,
            "meta_title": f"Vaseline Healthy Hands & Nails Cream 75ml | Ekleel Abha",
            "meta_description": f"Buy original {title_en}. 10x stronger nails in 2 weeks with Keratin & Vaseline Jelly. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["vaseline", "healthy_hands", "nail_cream", "keratin", "ekleel_abha"]
        },
        "schema": {
            "brand": "Vaseline",
            "category": "Skincare / Hand Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"{img_slug}.webp",
            "alt": title_en,
            "title": title_en
        }
    }

print("Loaded Batch 19 builders")
