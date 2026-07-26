import json, os

def build_wilkinson_oxygen(prod_id, conc_str, vol_str, gtin, img_slug):
    title_ar = f"ويلكسون مطور أكسجين كريمي للشعر بتركيز {conc_str} ({vol_str}) - 60 مل"
    title_en = f"Wilkinson Hair Color Oxygen Developer {conc_str} ({vol_str}), 60ml"

    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{title_ar}</strong> المستحضر الطبي الاحترافي المفضل لدى صالونات التجميل لتفتيح، صبغ، وتثبيت لون صبغة الشعر بكفاءة فائقة ونعومة متناهية. يرتكز هذا المطور الكريمي من ويلكسون (Wilkinson Oxygen Developer) على فورمولا الأكسجين المتوازنة بتركيز {conc_str} ({vol_str}) المعززة بالمرطبات ومثبتات اللون لحماية ألياف الشعر أثناء التفتيح والصبغ.</p>
<p>يمتاز مطور أكسجين ويلكسون بقوام كريمي متجانس يسهل خلطه مع مسحوق التفتيح (البلندر) أو كريمات الصبغة، حيث ينفذ في عمق ألياف الشعر ليفتح اللون بالتساوي دون تدمير غشاء الكيراتين أو تسبيب الجفاف الشديد والتقصف.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وصبغ متجانس بتركيز {conc_str} ({vol_str}):</strong> يضمن نفاذ الصبغة وتفتيح لون الشعر بدقة احترافية.</li>
  <li><strong>قوام كريمي ناعم يسهل الخلط:</strong> يندمج بمرونة مع كريمات الصبغة وبودرة التفتيح دون تكتل.</li>
  <li><strong>حماية ألياف الشعر أثناء الصبغ:</strong> معزز بالمرطبات لمنع خشونة وجفاف الشعر أثناء التفتيح.</li>
  <li><strong>تثبيت لون الصبغة لفترة طويلة:</strong> يثبت جزيئات اللون داخل جذع الشعرة لنتائج دائمة وبراقة.</li>
  <li><strong>آمن ومجرب في صالونات التجميل:</strong> تركيبة دقيقة مستقرة تضمن درجات تفتيح متوازنة ومضبوطة.</li>
  <li><strong>عبوة مدمجة سعة 60 مل:</strong> حجم ممتاز ومناسب لخلط عبوة صبغة واحدة (أو استخدام فردي).</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (المزج):</strong> اخلطي مطور أكسجين ويلكسون {conc_str} مع كريم الصبغة أو بودرة التفتيح بنسبة 1:1 أو 1:1.5 في وعاء غير معدني.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي المزيج بالتساوي على خصلات الشعر الجاف غير المغسول فوراً بعد الخلط.</li>
  <li><strong>الخطوة الثالثة (الانتظار والشطف):</strong> دعي الصبغة تتفاعل لـ 30 إلى 45 دقيقة حسـب درجة التفتيح المطلوبة ثم اشطفي بالماء الفاتر والشامبو.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>بيروكسيد الهيدروجين النقي (Hydrogen Peroxide {conc_str}):</strong> يفتح صبغة الشعر الطبيعية ويحفز تثبيت الصبغة.</li>
  <li><strong>مرطبات كريمية ومثبتات قوام:</strong> تحمي الشعر من الجفاف وتضمن قواماً سهلاً في التوزيع.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على الشعر فقط؛ يحظر ملامسة العينين أو الفروة المصابة بجروح.</li>
  <li>يُوصى بارتداء قفازات واقية وإجراء اختبار الحساسية على قطعة جلد صغيرة قبل 48 ساعة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن الحرارة المباشرة والشمس.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة أو خبير تجميل يفتش عن مطور أكسجين كريمي بتركيز {conc_str} لصبغ وتفتيح الشعر ب أمان ونعومة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>ويلكسون (Wilkinson)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / مطورات وأكسجين صبغات الشعر الكريمية</td></tr>
  <tr><th>نوع المنتج</th><td>مطور أكسجين كريمي لتفتيح وصبغ الشعر {conc_str} (60ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>60 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر المراد صبغه وتفتيحه</td></tr>
  <tr><th>المظهر النهائي</th><td>لون شعر متجانس، ثابت، ناعم وخالٍ من التكتلات والجفاف</td></tr>
  <tr><th>الملمس</th><td>كريم متجانس ناعم سريع الامتزاج بالصبغة</td></tr>
  <tr><th>العطر</th><td>عطر أكسجين خفيف مقبض</td></tr>
  <tr><th>المكونات النشطة</th><td>بيروكسيد الهيدروجين {conc_str}، مرطبات كريمية، مثبتات اللون</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا / المملكة العربية السعودية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Wilkinson Hair Care Labs</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد مطور الأكسجين الكريمي من ويلكسون (Wilkinson Oxygen)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مطور أكسجين ويلكسون مشكلة عدم تجانس لون الصبغة، التفتيح البقعي غير المتساوي، وجفاف الشعر بالصبغات العادية.</p>

<h3>لماذا تنجح تركيبة أكسجين {conc_str}؟</h3>
<p>لأن تركيز {conc_str} ({vol_str}) يقشر صبغة الشفاه الطبيعية ب رفق، مما يتيح لجزيئات الصبغة الجديدة الثبات العميق دون تلف الكيراتين.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>المزج بالوعاء البلاستيكي:</strong> اخلطي الأكسجين والصبغة دائماً في وعاء بلاستيكي أو زجاجي وتجنبي المعادن.<br>
2. <strong>اختبار الحساسية:</strong> طبقي كمية صغيرة على الجلد خلف الأذن قبل 48 ساعة من الصبغ.<br>
3. <strong>العناية بالبلسم بعد الصبغ:</strong> استعملي ماسك بلسم مرطب بعد الشطف لحبس اللون.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مطورات الأكسجين تدمر وتسقط الشعر دائماً."<br>
<strong>الحقيقة:</strong> مطور ويلكسون مزود بالمرطبات الكريمية لحماية وتنعيم ألياف الشعر عند الالتزام بالتركيز والوقت المحدد.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يطلق بيروكسيد الهيدروجين ذرات الأكسجين النشطة داخل أدمة الشعرة (Cortex)، فيذيب جزيئات الميلانين الداكنة ويثبت اللون.</p>"""

    faqs = [
        (f"ما هو {title_ar}؟", f"هو مطور أكسجين كريمي احترافي من ويلكسون بتركيز {conc_str} ({vol_str}) لتفتيح وصبغ الشعر ب أمان وتجانس سعة 60 مل."),
        (f"ما هي فوائد تركيز {conc_str} ({vol_str})؟", f"يضمن تفتيحاً وصبغاً متجانساً بدقة دون تدمير غشاء الكيراتين أو تسبيب التكسر."),
        ("هل يمتزج بسلاسة مع بودرة التفتيح والصبغات؟", "نعم، قوام كريمي متجانس يمتزج بمرونة فائقة دون تكتل."),
        ("ما حجم العبوة؟", "تأتي بحجم 60 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اخلطي الأكسجين مع كريم الصبغة بنسبة 1:1 في وعاء غير معدني، وضعي المزيج على شعر جاف 30-45 دقيقة ثم اشطفي."),
        ("هل يحمي ألياف الشعر أثناء الصبغ؟", "نعم، مدعم بالمرطبات الكريمية لحماية الشعر من الخشونة والجفاف."),
        ("ما هو بلد صنع مطور ويلكسون؟", "صُنع وفق أعلى معايير الجودة والأمان لصبغات الشعر العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات ويلكسون لدى إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يساعد في تثبيت لون الصبغة لعدة أسابيع؟", "نعم، يثبت جزيئات اللون داخل أدمة الشعرة لنتائج ثابتة وبراقة."),
        ("ما هي رائحة المطور؟", "يتميز برائحة ناعمة ولطيفة مقبولة أثناء تطبيق الصبغة."),
        ("هل يناسب جميع أنواع الشعر؟", "مناسب لجميع أنواع الشعر المراد صبغه وتفتيحه."),
        ("هل يجب ارتداء قفازات أثناء التطبيق؟", "نعم، يُوصى دائماً بارتداء قفازات واقية عند خلط وتطبيق الصبغة والأكسجين."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس والحرارة."),
        ("هل العبوة 60 مل تكفي لصبغ الشعر؟", "نعم، تكفي لخلط عبوة صبغة واحدة 60 مل."),
        ("هل يسبب حرقاناً لفروة الرأس؟", "تركيبة متوازنة ومستقرة، ويُفضل تجنب ملامسة الفروة المتهيجة أو المجروحة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة أنيقة بغطاء لولبي محكم الحماية لمنع التسرب."),
        ("هل يناسب الصالونات والاستخدام المنزلي؟", "نعم، خيار ممتاز لخبراء التجميل وللصباغة المنزلية الاحترافية."),
        ("هل يحتاج لوعاء غير معدني للخلط؟", "نعم، يمنع الخلط بالأواني المعدنية لعدم تفاعل بيروكسيد الهيدروجين."),
        ("كم مدة الانتظار الموصى بها على الشعر؟", "تتراوح مدة التفاعل من 30 إلى 45 دقيقة حسـب درجة التفتيح المطلوبة."),
        ("هل يناسب تفتيح شعر الحواجب أيضاً؟", "يُفضل استشارة الخبراء ومراعاة عدم ملامسة العينين إطلاقاً."),
        ("هل يحتوي على بيروكسيد الهيدروجين؟", "نعم، ينشط ببيروكسيد الهيدروجين النقي عالي الاستقرار."),
        ("هل يمنع تكسر الشعر بعد الصبغة؟", "نعم، المرطبات الكريمية تدعم مرونة الشعر وتمنع التكسر."),
        ("هل هو مطور الأكسجين المفضل للصبغات؟", "نعم، مطور ويلكسون الأكثر ثقة في ضبط درجات تفتيح الصبغة."),
        ("هل يترك الشعر لامعاً؟", "نعم، يمنح الشعر المصبوغ لمعاناً ونضارة ساحرة."),
        ("هل يتوفر بتركيزات أخرى لدى إكليل أبها؟", "نعم، تتتوفر تركيزات 6% (20V) و 9% (30V) لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{title_en}</strong> is the professional salon-grade cream oxygen developer engineered for precise hair lightening, dyeing, and long-lasting color fixation. Formulated by Wilkinson Hair Care, it features a stable {conc_str} ({vol_str}) hydrogen peroxide cream matrix enriched with protective conditioning lipids.</p>
<p>Wilkinson Oxygen Developer features a smooth, easy-mixing consistency that blends seamlessly with hair color creams and bleaching powders, penetrating hair fibers to lift color evenly without damaging keratin structure or causing severe dryness.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Precise {conc_str} ({vol_str}) Color Lifting:</strong> Ensures even, vibrant dye penetration and lifting.</li>
  <li><strong>Smooth Easy-Mixing Cream Matrix:</strong> Blends effortlessly with hair color creams and bleach powder without clumping.</li>
  <li><strong>Protects Hair Fibers During Dyeing:</strong> Enriched with moisturizing lipids to guard hair from roughness and dryness.</li>
  <li><strong>Long-Lasting Color Fixation:</strong> Locks color pigments deep within the hair shaft for durable, radiant results.</li>
  <li><strong>Salon-Approved Stable Formula:</strong> Delivers controlled, predictable lift and dye development.</li>
  <li><strong>Compact 60ml Bottle:</strong> Ideal single-use size for mixing one standard 60ml hair color tube.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Mix):</strong> Mix Wilkinson Oxygen Developer {conc_str} with hair dye cream or bleaching powder at a 1:1 ratio in a non-metallic bowl.</li>
  <li><strong>Step 2 (Apply):</strong> Apply mixture evenly onto dry, unwashed hair strands immediately after mixing.</li>
  <li><strong>Step 3 (Develop & Rinse):</strong> Allow color to develop for 30 to 45 minutes depending on desired lift; rinse with warm water and shampoo.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Hydrogen Peroxide ({conc_str}):</strong> Lifts natural hair pigments and activates dye color molecules.</li>
  <li><strong>Conditioning Cream Base:</strong> Guards hair shafts against dryness and ensures smooth application.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external hair coloring and bleaching application only; avoid contact with eyes and wounded scalp.</li>
  <li>Wear protective gloves and perform a skin allergy patch test 48 hours prior to full use.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from direct heat and sunlight.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone or hair color specialist seeking a professional {conc_str} cream oxygen developer for safe, even hair dyeing.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Wilkinson</td></tr>
  <tr><th>Category</th><td>Hair Care / Professional Cream Oxygen Developers</td></tr>
  <tr><th>Product Type</th><td>Cream Hydrogen Peroxide Hair Color Developer {conc_str} (60ml)</td></tr>
  <tr><th>Volume/Weight</th><td>60 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types Intended for Dyeing & Bleaching</td></tr>
  <tr><th>Finish</th><td>Evenly dyed, radiant, soft & long-lasting hair color</td></tr>
  <tr><th>Texture</th><td>Smooth fast-blending cream matrix</td></tr>
  <tr><th>Fragrance</th><td>Subtle fresh oxygen scent</td></tr>
  <tr><th>Active Ingredients</th><td>Hydrogen Peroxide {conc_str}, Conditioning Lipids, Color Fixatives</td></tr>
  <tr><th>Country of Origin</th><td>Germany / Saudi Arabia</td></tr>
  <tr><th>Manufacturer</th><td>Wilkinson Hair Care Labs</td></tr>
  <tr><th>Age Group</th><td>Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of {conc_str} Hydrogen Peroxide & Melanin Oxidation</h2>

<h3>What problem does this solve?</h3>
<p>Wilkinson Oxygen Developer resolves uneven dye lift, spotty bleaching, and severe hair dryness during hair coloring.</p>

<h3>Why choose Wilkinson Oxygen {conc_str}?</h3>
<p>The stable {conc_str} ({vol_str}) cream matrix oxidizes natural hair melanin gently, allowing new color pigments to lock deep within the cortex.</p>"""

    en_faqs = [
        (f"What is {title_en}?", f"It is a professional cream oxygen developer formulated at {conc_str} ({vol_str}) for safe, even hair dyeing and bleaching in a 60ml bottle."),
        (f"What are the benefits of {conc_str} ({vol_str}) concentration?", "Ensures controlled, even color lift and vibrant dye fixation without damaging keratin structure."),
        ("Does it blend easily with hair dye and bleach powder?", "Yes, smooth cream matrix blends effortlessly without clumping in non-metallic bowls."),
        ("What volume is contained in this bottle?", "It comes in a 60ml single-use bottle."),
        ("How do I apply it correctly?", "Mix 1:1 with hair dye cream in a non-metallic bowl, apply to dry unwashed hair, leave 30-45 mins, then rinse."),
        ("Does it protect hair fibers during coloring?", "Yes, enriched with conditioning lipids to shield hair from roughness and moisture loss."),
        ("Where is Wilkinson manufactured?", "Produced following international professional hair care safety standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Wilkinson products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it fix hair color for weeks?", "Yes, locks dye pigments inside the cortex for long-lasting radiant results."),
        ("What scent does it have?", "Features a subtle, pleasant oxygen scent during application."),
        ("Is it suitable for all hair types?", "Suitable for all hair types intended for coloring or bleaching."),
        ("Should protective gloves be worn?", "Yes, always wear protective gloves when mixing and applying oxygen developers."),
        ("How should I store the bottle?", "Store in a cool, dry place away from heat and direct sunlight."),
        ("Is the 60ml bottle sufficient for one dye tube?", "Yes, perfectly sized for mixing one standard 60ml hair color tube."),
        ("Does it cause scalp stinging?", "Stable formula; avoid direct contact with broken or irritated scalp."),
        ("Is the bottle securely sealed?", "Yes, comes in a sturdy bottle with a leak-proof screw cap."),
        ("Is it suitable for salon and home use?", "Yes, ideal for professional hair colorists and home hair dyeing."),
        ("Why must a non-metallic bowl be used?", "Non-metallic bowls prevent hydrogen peroxide from reacting with metals."),
        ("What is the recommended development time?", "Leave on hair for 30 to 45 minutes depending on desired lift level."),
        ("Can it be used for eyebrow tinting?", "Consult a specialist and avoid any eye contact."),
        ("Does it contain hydrogen peroxide?", "Yes, contains pure, highly stable hydrogen peroxide."),
        ("Does it prevent post-dye hair breakage?", "Yes, conditioning lipids maintain hair suppleness to prevent breakage."),
        ("Is Wilkinson a trusted developer brand?", "Yes, trusted by hair colorists for precise, reliable lift results."),
        ("Does it leave hair shiny?", "Yes, leaves dyed hair with radiant shine and softness."),
        ("Are other concentrations available at Ekleel Abha?", "Yes, available in 6% (20V) and 9% (30V) concentrations at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "العناية بالشعر / مطورات وأكسجين صبغات الشعر الكريمية",
        "brand": "Wilkinson",
        "ar": {
            "title": title_ar,
            "meta_title": f"ويلكسون مطور أكسجين {conc_str} 60مل | صيدلية إكليل أبها",
            "meta_description": f"اشتري {title_ar}. مطور أكسجين كريمي لتفتيح وصبغ الشعر ب أمان وتجانس. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["ويلكسون", "أكسجين_الشعر", "مطور_الصبغة", "تفتيح_الشعر", "إكليل_أبها"]
        },
        "en": {
            "title": title_en,
            "meta_title": f"Wilkinson Oxygen Developer {conc_str} 60ml | Ekleel Abha",
            "meta_description": f"Buy original {title_en}. Professional cream oxygen developer for hair dyeing & bleaching. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["wilkinson", "oxygen_developer", "hair_color_developer", "hair_bleach", "ekleel_abha"]
        },
        "schema": {
            "brand": "Wilkinson",
            "category": "Hair Care / Developer",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"{img_slug}.webp",
            "alt": title_en,
            "title": title_en
        }
    }

def create_product_1838():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مزيل مكياج  للبشرة الحساسة من غارنييه - 200مل (Garnier Makeup Remover for Sensitive Skin - 200ml)</strong> ماء الميسيلار المبتكر والأكثر مبيعاً عالمياً لتنظيف الوجه وإزالة كافة أنواع المكياج بمسحة واحدة ودون الحاجة لفرك أو شطف بالماء. يرتكز هذا المستحضر الشهير من غارنييه (Garnier Micellar Cleansing Water All-in-1) على تقنية جزيئات الميسيلار المغناطيسية المنظفة المنعشة.</p>
<p>تعمل ميسيلار غارنييه على التقاط الشوائب، الدهون الزائدة، والمكياج كالمغناطيس دون إلحاق أي أذى ببشرة الوجه والعينين والشفتين الحساسة، لتترك بشرتكِ نظيفة، معقمة، ومرطبة دون ترك أي أثر دهني لزج.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>إزالة كاملة للمكياج والشوائب بمسحة واحدة:</strong> ينظف الوجه والعينين والشفتين بسهولة فائقة.</li>
  <li><strong>تقنية الميسيلار المغناطيسية المنظفة (Micellar):</strong> تجذب المكياج والأوساخ دون فرك قسي.</li>
  <li><strong>مخصص ومجرب للبشرة الحساسة:</strong> تركيبة خالية 100% من العطور، الكحول، والبارابين.</li>
  <li><strong>لا يحتاج لشطف بالماء:</strong> يترك الوجه مرطباً ونظيفاً ومستعداً للعناية اليومية.</li>
  <li><strong>مجرب من أطباء الجلدية والعيون:</strong> آمن تماماً للعينين ومستخدمي العدسات اللاصقة.</li>
  <li><strong>عبوة سعة 200 مل:</strong> حجم مدمج ومثالي للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التسكيب):</strong> اسكبي كمية مناسبة من ميسيلار غارنييه على قطعة قطن مخصصة للوجه.</li>
  <li><strong>الخطوة الثانية (المسح):</strong> امسحي وجهكِ، عينيكِ، وشفتيكِ بلطف ودون فرك شديد.</li>
  <li><strong>الخطوة الثالثة (العناية):</strong> دع الوجه يجف طبيعياً واستمتعي ببشرة مرطبة ونظيفة (لا يحتاج لشطف بالماء).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>جزيئات الميسيلار المنظفة (Cleansing Micelles):</strong> تجذب وتزيل الشوائب والمكياج كالمغناطيس.</li>
  <li><strong>سائل مائي خالي من العطور والكحول:</strong> يهدئ البشرة الحساسة ويحفظ ترطيبها.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على بشرة الوجه والعينين والشفتين فقط.</li>
  <li>تجنبي ملامسة السائل المباشرة لداخل العين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تفتش عن ماء ميسيلار غارنييه الوردي الأصلي لإزالة المكياج وتنظيف البشرة الحساسة ب أمان.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>غارنييه (Garnier Micellar)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / مياه الميسيلار ومنظفات المكياج للبشرة الحساسة</td></tr>
  <tr><th>نوع المنتج</th><td>ماء ميسيلار مزيل للمكياج الكل في واحد للبشرة الحساسة (200ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>200 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الحساسة، العادية، والمختلطة</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة وجه نظيفة، مرطبة، معقمة وخالية تماماً من المكياج والدهون</td></tr>
  <tr><th>الملمس</th><td>سائل مائي نقي خفيف للغاية دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عديم الرائحة (100% Unscented)</td></tr>
  <tr><th>المكونات النشطة</th><td>جزيئات ميسيلار، ماء نقي، خالي من الكحول والعطور</td></tr>
  <tr><th>بلد المنشأ</th><td>بولندا / فرنسا (Garnier France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>L'Oréal / Garnier</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد ماء الميسيلار من غارنييه (Garnier Micellar Water)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج ماء ميسيلار غارنييه الوردي مشكلة تهيج وتورم البشرة الحساسة عند إزالة المكياج بالمنظفات الزيتية القاسية.</p>

<h3>لماذا تنجح تقنية الميسيلار؟</h3>
<p>لأن جزيئات الميسيلار تحيط بالمكياج والدهون كالمغناطيس وتزيلها بمسحة قطنة، دون إحداث أي احتكاك يضر البشرة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>المسح بالقطن دون فرك:</strong> ضعي القطنة المبللة بالميسيلار على العين لـ 5 ثوانٍ ثم امسحي ب نعومة.<br>
2. <strong>عدم الحاجة للشطف:</strong> دع الميسيلار ينظف الوجه دون حاجة لشطف بالماء.<br>
3. <strong>الاستخدام صباحاً ومساءً:</strong> استعمليه صباحاً لتنقية البشرة ومساءً لإزالة المكياج.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "ماء الميسيلار يجفف البشرة الحساسة ويحتاج لغسول بعده."<br>
<strong>الحقيقة:</strong> ماء ميسيلار غارنييه الوردي خالي من الكحول والعطور ومصمم لترطيب وتلطيف البشرة دون جفاف.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخفض جزيئات الميسيلار التوتر السطحي للماء، فتذيب المكياج والزيوت المسدودة بالمسام وتقتلع الشوائب.</p>"""

    faqs = [
        ("ما هو مزيل مكياج للبشرة الحساسة من غارنييه 200مل؟", "هو ماء ميسيلار الكل في واحد من غارنييه ينظف الوجه ويزيل المكياج للبشرة الحساسة دون فرك أو شطف 200 مل."),
        ("ما هي فوائد تقنية جزيئات الميسيلار؟", "تجذب المكياج والدهون والشوائب كالمغناطيس وتزيلها بمسحة قطنة دون فرك قسي."),
        ("هل هو خالي 100% من العطور والكحول والبارابين؟", "نعم، خالي 100% من العطور والكحول والبارابين ومخصص للبشرة الحساسة."),
        ("ما حجم العبوة؟", "تأتي بحجم 200 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اسكبي كمية على قطنة، امسحي الوجه والعينين والشفتين بلطف دون فرك أو شطف بالماء."),
        ("هل يحتاج للغسيل أو الشطف بالماء بعده؟", "لا يحتاج للشطف بالماء، يترك الوجه نظيفاً ومرطباً طبيعياً."),
        ("ما هو بلد صنع ماء ميسيلار غارنييه؟", "صُنع بفخر بواسطة شركة لوريال (L'Oréal / Garnier) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات غارنييه لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يزيل مكياج العينين والشفتين ب أمان؟", "نعم، مجرب من أطباء العيون والجلدية وآمن تماماً للعينين والشفتين."),
        ("ما هي رائحة ماء ميسيلار غارنييه الوردي؟", "عديم الرائحة تماماً (Unscented)."),
        ("هل يناسب مستخدمي العدسات اللاصقة؟", "نعم، آمن ومجرب لمستخدمي العدسات اللاصقة."),
        ("هل العبوة 200 مل مناسبة للسفر والحقيبة؟", "نعم، حجم مدمج وأنيق مثالي لحمل الحقيبة والسفر."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعبوتها المغلقة محكماً."),
        ("هل يترك أثراً دهنياً لزجاً؟", "لا، ينظف الوجه تماماً دون ترك أي لزوجة زيتية."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة أنيقة بغطاء لولبي محكم السكب."),
        ("هل يمنع انسداد المسام وتكون الحبوب؟", "نعم، تنقية الشوائب تمنع انسداد المسام وتكون الحبوب."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستخدم 2 مرات يومياً (صباحاً ومساءً)."),
        ("هل يغني عن غسولات الوجه القاسية؟", "نعم، يوفر تنظيفاً لطيفاً يغني عن الغسولات الصابونية القاسية."),
        ("هل هو ماء الميسيلار الأكثر مبيعاً عالمياً؟", "نعم، ميسيلار غارنييه الوردي الأكثر شهرة ومبيعاً عالمياً."),
        ("هل يناسب جميع الأعمار؟", "مناسب للفتيات والبالغين من سن 12 سنة فما فوق."),
        ("هل يساعد في إنعاش الوجه المجهد؟", "نعم، يمنح البشرة انتعاشاً ونقاءً فورياً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يزيل مسكارا كحل العين ب أمان؟", "نعم، يزيل الكحل والماسكارا بسهولة دون إيذاء الرموش."),
        ("هل يترك البشرة طرية ومرطبة؟", "نعم، يترك الوجه طرياً ومشرقاً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Garnier Makeup Remover for Sensitive Skin - 200ml</strong> (Garnier Micellar Cleansing Water All-in-1) is the world's #1 best-selling micellar cleansing water engineered to cleanse skin and remove makeup in a single swipe without harsh rubbing or water rinsing. Formulated with magnetic Micellar Cleansing Technology.</p>
<p>Garnier Pink Micellar Water captures impurities, sebum, and makeup like a magnet without harming sensitive facial skin, eyes, or lips, leaving your skin thoroughly cleansed, sanitized, and hydrated with zero greasy residue.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>All-in-1 Facial Cleanser & Makeup Remover:</strong> Cleanses face, eyes, and lips in a single effortless swipe.</li>
  <li><strong>Magnetic Micellar Cleansing Technology:</strong> Captures makeup, oil, and impurities like a magnet without rubbing.</li>
  <li><strong>Formulated for Sensitive Skin:</strong> 100% free from fragrance, alcohol, and parabens.</li>
  <li><strong>No Water Rinsing Required:</strong> Leaves facial skin hydrated, clean, and prepped for daily skincare.</li>
  <li><strong>Dermatologically & Ophthalmologically Tested:</strong> Completely safe for sensitive eyes and contact lens wearers.</li>
  <li><strong>Compact 200ml Bottle:</strong> Ideal handbag and travel size for daily cleansing routines.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Pour):</strong> Pour a generous amount of Garnier Micellar Water onto a cotton pad.</li>
  <li><strong>Step 2 (Wipe):</strong> Gently wipe over face, eye contours, and lips without harsh rubbing.</li>
  <li><strong>Step 3 (Glow):</strong> Allow skin to dry naturally and enjoy hydrated, clean skin (no water rinsing required).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Cleansing Micelles:</strong> Magnetically attract and sweep away impurities and makeup pigments.</li>
  <li><strong>Pure Unscented Water Base:</strong> Soothes sensitive skin layers and maintains hydration.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external facial, eye, and lip makeup removal application only.</li>
  <li>Avoid direct contact with the interior of the eye.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking the original pink Garnier Micellar Cleansing Water for sensitive skin makeup removal without water rinsing.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Garnier (Garnier Micellar)</td></tr>
  <tr><th>Category</th><td>Skincare / Micellar Cleansing Waters for Sensitive Skin</td></tr>
  <tr><th>Product Type</th><td>All-in-1 Micellar Cleansing Water (200ml)</td></tr>
  <tr><th>Volume/Weight</th><td>200 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Sensitive, Normal & Combination Skin</td></tr>
  <tr><th>Finish</th><td>Clean, hydrated, sanitized & makeup-free facial skin</td></tr>
  <tr><th>Texture</th><td>Ultra-light clear water liquid</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-Free (Unscented)</td></tr>
  <tr><th>Active Ingredients</th><td>Cleansing Micelles, Pure Water Base, Alcohol-Free Base</td></tr>
  <tr><th>Country of Origin</th><td>Poland / France (Garnier France)</td></tr>
  <tr><th>Manufacturer</th><td>L'Oréal / Garnier</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Micellar Cleansing & Sensitive Skin Tolerance</h2>

<h3>What problem does this solve?</h3>
<p>Garnier Micellar Cleansing Water resolves sensitive skin redness, harsh makeup rubbing, and dry skin tightness.</p>

<h3>Why choose Garnier Pink Micellar Water?</h3>
<p>Micelle structures lower water surface tension, surrounding makeup pigments and sebum to sweep them away gently without water rinsing.</p>"""

    en_faqs = [
        ("What is Garnier Makeup Remover for Sensitive Skin 200ml?", "It is an all-in-1 micellar cleansing water that removes makeup and purifies sensitive skin without rubbing or water rinsing."),
        ("What are the benefits of Micellar Cleansing Technology?", "Magnetically captures makeup, oil, and impurities, sweeping them away with a cotton pad."),
        ("Is it 100% free of fragrance, alcohol, and parabens?", "Yes, 100% fragrance-free, alcohol-free, and paraben-free; designed for sensitive skin."),
        ("What volume is contained in this bottle?", "It comes in a compact 200ml bottle."),
        ("How do I apply it correctly?", "Pour onto a cotton pad, wipe gently across face, eyes, and lips without harsh rubbing or water rinsing."),
        ("Is water rinsing required after use?", "No water rinsing needed; leaves facial skin clean, soft, and hydrated."),
        ("Where is Garnier Micellar Water manufactured?", "It is proudly manufactured in France/Poland by L'Oréal / Garnier."),
        ("How do I verify authenticity at Ekleel Abha?", "All Garnier products at Ekleel Abha are 100% original from certified distributors."),
        ("Is it safe for sensitive eyes and lips?", "Yes, ophthalmologist and dermatologist tested; safe for sensitive eyes and lips."),
        ("What scent does Garnier Pink Micellar Water have?", "It is completely fragrance-free (unscented)."),
        ("Is it safe for contact lens wearers?", "Yes, ophthalmologist-tested and safe for contact lens wearers."),
        ("Is the 200ml bottle travel-friendly?", "Yes, compact bottle size fits easily into handbags and travel kits."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Does it leave a greasy sticky residue?", "No, cleanses thoroughly leaving zero greasy or sticky film."),
        ("Is the bottle cap leak-proof?", "Yes, comes in a sleek bottle with a secure flip-top dispenser cap."),
        ("Does it prevent clogged pores?", "Yes, clearing daily makeup and sebum prevents pore blockages and breakouts."),
        ("How often can I use it daily?", "Use twice daily, morning and evening."),
        ("Does it replace harsh soap cleansers?", "Yes, provides gentle cleansing that replaces harsh alkaline soaps."),
        ("Is it the world's #1 micellar water?", "Yes, Garnier Pink Micellar Water is the #1 globally best-selling micellar water."),
        ("Is it suitable for all ages?", "Suitable for teens and adults aged 12+."),
        ("Does it refresh tired skin?", "Yes, restores instant freshness and purity to tired facial skin."),
        ("Is the bottle recyclable?", "Yes, 100% recyclable environmentally friendly bottle."),
        ("Does it erase eye makeup gently?", "Yes, erases eyeliner and mascara gently without damaging eyelashes."),
        ("Does it leave skin touchably soft?", "Yes, leaves facial skin soft, hydrated, and supple."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1838",
        "sku": "EK-1838",
        "gtin": "3600542382885",
        "category": "العناية بالبشرة / مياه الميسيلار ومنظفات المكياج للبشرة الحساسة",
        "brand": "Garnier",
        "ar": {
            "title": "مزيل مكياج  للبشرة الحساسة من غارنييه - 200مل",
            "meta_title": "مزيل مكياج غارنييه ميسيلار 200مل | صيدلية إكليل أبها",
            "meta_description": "اشتري مزيل مكياج للبشرة الحساسة من غارنييه (200مل). ماء ميسيلار الوردي الكل في واحد خالي من العطور والكحول. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["غارنييه", "غارنييه_ميسيلار", "مزيل_المكياج", "البشرة_الحساسة", "إكليل_أبها"]
        },
        "en": {
            "title": "Garnier Makeup Remover for Sensitive Skin - 200ml",
            "meta_title": "Garnier Micellar Water 200ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Garnier Makeup Remover for Sensitive Skin (200ml). Pink All-in-1 Micellar Water fragrance-free formula. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["garnier", "garnier_micellar", "makeup_remover", "sensitive_skin", "ekleel_abha"]
        },
        "schema": {
            "brand": "Garnier",
            "category": "Skincare / Micellar Water",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "garnier-makeup-remover-for-sensitive-skin-200ml.webp",
            "alt": "Garnier Makeup Remover for Sensitive Skin 200ml",
            "title": "Garnier Makeup Remover for Sensitive Skin 200ml"
        }
    }

def build_nivea_eye_remover(prod_id, gtin, img_slug):
    title_ar = "مزيل مكياج العيون اللطيف من نيفيا - 125 مل"
    title_en = "NIVEA Eye Makeup Remover 125ml"

    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مزيل مكياج العيون اللطيف من نيفيا - 125 مل (NIVEA Eye Makeup Remover 125ml)</strong> المستحضر الطبي الفائق المخصص لإزالة مكياج العينين والماسكارا المقاومة للماء برفق تام ودون تسبيب أي ضبابية أو تهيج للعينين. يرتكز هذا المزيل المائل للماء والزيت من نيفيا (Nivea Double Effect / Gentle Eye Makeup Remover) على فورمولا النظافة الفائقة المعززة بخلاصة زهرة البابونج ومركبات نيفيا المهدئة لجلد العينين الرقيق.</p>
<p>يعمل مزيل مكياج العيون من نيفيا على إذابة كحل العين، الظلال، والماسكارا المقاومة للماء فورياً بمسحة قطنة خفيفة، دون الحاجة للفرك الشديد، مما يحمي الرموش من التساقط ويترك جلد العينين ناعماً، مرطباً، ونظيفاً تماماً.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>إزالة فورية لماسكارا وكحل العين المقاوم للماء:</strong> يذوب أصباغ المكياج الثقيلة بسهولة بمسحة واحدة.</li>
  <li><strong>حماية الرموش من التساقط والتلف:</strong> يمنع احتكاك وجذب الرموش أثناء مسح الكحل والماسكارا.</li>
  <li><strong>مخصص ومجرب لجلد العينين الرقيق:</strong> تركيبة مطهرة خالية من الكحول ومجربة طبياً من أطباء العيون.</li>
  <li><strong>معزز بخلاصة زهرة البابونج المهدئة:</strong> يلطف أحمرار وتهيج العينين ويحفظ رطوبتهما.</li>
  <li><strong>لا يترك طبقة غباش أو أثر دهني بالعين:</strong> يضمن رؤية واضحة ونظافة تامة بعد المسح.</li>
  <li><strong>عبوة مدمجة سعة 125 مل:</strong> حجم ممتاز ومناسب للاستخدام اليومي والسفر وحقيبة المكياج.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الرج والتسكيب):</strong> رجي عبوة نيفيا جيداً لمزج السائل واسكبي كمية على قطنة مكياج.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> ضعي القطنة على العين المغلقة لمدة 5 إلى 10 ثوانٍ لإذابة الماسكارا.</li>
  <li><strong>الخطوة الثالثة (المسح):</strong> امسحي للأسفل وللخارج بلطف ودون فرك شديد واكرري للعين الأخرى.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة زهرة البابونج (Chamomile Extract):</strong> تلطف جلد العينين وتمنع الأحمرار والتهيج.</li>
  <li><strong>مذيبات مكياج خفيفة خالية من الكحول:</strong> تذوب الماسكارا المقاومة للماء ب أمان.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على جلد العينين والشفتين فقط.</li>
  <li>تجنبي ملامسة السائل المباشرة لداخل العين المغتوحة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تفتش عن مزيل مكياج عيون لطيف من نيفيا يزيل الماسكارا المقاومة للماء ويحمي الرموش.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>نيفيا (Nivea)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / مزيلات مكياج العيون والماسكارا المقاومة للماء</td></tr>
  <tr><th>نوع المنتج</th><td>مزيل مكياج العيون والماسكارا اللطيف الخالي من الكحول (125ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>125 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة العينين (بما في ذلك الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>عينان نظيفتان، معقمتان، مرطبتان ورؤية واضحة خالية من الماسكارا</td></tr>
  <tr><th>الملمس</th><td>سائل مائي زيتي خفيف جداً سريع الامتصاص</td></tr>
  <tr><th>العطر</th><td>عطر نيفيا اللطيف الخفيف جداً</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة البابونج، مرطبات نيفيا، خالي من الكحول</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا (Beiersdorf Germany)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beiersdorf (نيفيا)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد مزيل مكياج العيون من نيفيا (Nivea Eye Remover)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مزيل مكياج عيون نيفيا مشكلة تساقط الرموش أثناء مسح الماسكارا المقاومة للماء، غباش العينين، وحرقان المزيلات العادية.</p>

<h3>لماذا تنجح تركيبة البابونج الثنائية؟</h3>
<p>لأن الطور الزيتي يذوب أصباغ الماسكارا الشمعية فورياً، بينما يهدئ طور البابونج المائي أدمة العينين دون فرك.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الرج الجيد قبل الاستعمال:</strong> رجي العبوة دائماً لمزج الطبقتين المائية والزيتية.<br>
2. <strong>ترك القطنة 10 ثوانٍ:</strong> دع القطنة على العين 10 ثوانٍ لإذابة الشمع قبل المسح.<br>
3. <strong>المسح باتجاه نمو الرموش:</strong> امسحي من الأعلى للأسفل لحماية الرموش من الانكسار.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مزيلات مكياج العيون تسبب ضبابية ورؤية مغبشة للعينين."<br>
<strong>الحقيقة:</strong> مزيل نيفيا اللطيف مصمم بتركيبة مجربة من أطباء العيون تضمن رؤية ناصعة دون غباش.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تفكك المذيبات الخفيفة بوليمرات الماسكارا المقاومة للماء (Waterproof Polymers)، فتتساقط الأصباغ على القطنة دون شد للرموش.</p>"""

    faqs = [
        ("ما هو مزيل مكياج العيون اللطيف من نيفيا 125 مل؟", "هو مزيل مخصص لإزالة مكياج العيون والماسكارا المقاومة للماء بخلاصة البابونج لحماية الرموش وجلد العينين 125 مل."),
        ("ما هي فوائد خلاصة البابونج لجلد العينين؟", "تلطف تهيج وأحمرار العينين وتمنح ترطيباً ناعماً دون حرقان."),
        ("هل يزيل الماسكارا المقاومة للماء بسهولة؟", "نعم، مثبت سريرياً في إذابة الماسكارا القابلة للماء وكحل العين بمسحة قطنة واحدة."),
        ("ما حجم العبوة؟", "تأتي بحجم 125 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "رجي العبوة جيداً، وضعي كمية على قطنة، اتركيه 10 ثوانٍ على العين المغلقة ثم امسحي برفق للأسفل."),
        ("هل يحمي الرموش من التساقط؟", "نعم، يمنع احتكاك وشد الرموش أثناء المسح لمنع تساقطها."),
        ("ما هو بلد صنع مزيل عرق نيفيا؟", "صُنع بفخر في ألمانيا بواسطة شركة بايرسدورف (Beiersdorf)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات نيفيا لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يسبب غباش أو ضبابية بالعين؟", "لا، فورمولا مجربة من أطباء العيون تضمن عدم وجود أي ضبابية أو لزوجة بالعين."),
        ("ما هي رائحة مزيل نيفيا للعيون؟", "يتميز برائحة ناعمة ولطيفة جداً مقبولة."),
        ("هل يناسب مستخدمي العدسات اللاصقة؟", "نعم، آمن ومجرب لمستخدمي العدسات اللاصقة والعيون الحساسة."),
        ("هل العبوة 125 مل مناسبة للسفر والحقيبة؟", "نعم، حجم مدمج وأنيق مثالي لحمل حقيبة المكياج والسفر."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعبوتها المغلقة محكماً."),
        ("هل يترك أثراً دهنياً ثقيلاً؟", "لا، يجف فورياً ليترك جلد العينين ناعماً ونظيفاً."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة أنيقة بغطاء لولبي محكم الحماية."),
        ("هل ينصح به أطباء العيون؟", "نعم، مجرب ومصرح به من أطباء العيون والجلدية عالمياً."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستخدم عند الحاجة لإزالة مكياج العيون."),
        ("هل ينظف ظلال العيون والكحل الجاف؟", "نعم، ينظف جميع أنواع الآيلاينر، الظلال، والكحل الثابت."),
        ("هل هو مزيل العرق والعيون الأكثر ثقة؟", "نعم، نيفيا الماركة الأولى الموثوقة لعناية العيون."),
        ("هل يناسب جميع الأعمار؟", "مناسب للفتيات والبالغين من سن 12 سنة فما فوق."),
        ("هل يساعد في ترطيب جلد العينين الرقيق؟", "نعم، البابونج والخصائص المرطبة تطري جلد العينين."),
        ("هل يحتاج للشطف بالماء؟", "لا يحتاج للشطف بالماء، يترك العينين نظيفتين مباشرة."),
        ("هل ينصح برج العبوة قبل الاستخدام؟", "نعم، يُوصى برجه جيداً لمزج الطور المائي بالطور الزيتي."),
        ("هل يترك ملمساً ناعماً؟", "نعم، يترك منطقة العين طرية ومريحة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>NIVEA Eye Makeup Remover 125ml</strong> is the dermatologist and ophthalmologist-tested medical eye makeup remover engineered to gently erase eye makeup and stubborn waterproof mascara without causing eye stinging or eyelash loss. Formulated by Nivea, it is enriched with soothing Chamomile Extract.</p>
<p>Nivea Eye Makeup Remover dissolves waterproof eyeliner, eyeshadow, and mascara instantly with a gentle cotton pad swipe, protecting delicate eyelashes from breakage while leaving eye contour skin soft, hydrated, and perfectly cleansed.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Instant Waterproof Mascara & Eye Makeup Removal:</strong> Dissolves heavy waterproof makeup pigments easily.</li>
  <li><strong>Protects Eyelashes Against Loss & Breakage:</strong> Eliminates harsh rubbing to keep lashes intact.</li>
  <li><strong>Ophthalmologist-Tested for Sensitive Eye Contours:</strong> Alcohol-free gentle formula safe for delicate eye skin.</li>
  <li><strong>Enriched with Soothing Chamomile Extract:</strong> Calms redness, eye irritation, and seals in moisture.</li>
  <li><strong>Leaves Zero Blurry Film or Oily Residue:</strong> Ensures clear vision and clean eye contours post-cleansing.</li>
  <li><strong>Compact 125ml Bottle:</strong> Ideal handbag and travel kit size for daily makeup removal.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Shake & Pour):</strong> Shake the Nivea bottle well to blend the formula and pour onto a cotton pad.</li>
  <li><strong>Step 2 (Apply):</strong> Hold the cotton pad over closed eye for 5 to 10 seconds to dissolve mascara pigments.</li>
  <li><strong>Step 3 (Wipe):</strong> Gently wipe downward and outward without rubbing; repeat for the other eye.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Chamomile Extract:</strong> Soothes delicate eye contour skin and prevents redness and irritation.</li>
  <li><strong>Gentle Alcohol-Free Solvents:</strong> Dissolve stubborn waterproof mascara pigments safely.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external eye contour and lip makeup removal application only.</li>
  <li>Avoid direct contact with the interior of the open eye.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a gentle, ophthalmologist-tested Nivea eye makeup remover that effortlessly erases waterproof mascara while protecting lashes.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Nivea</td></tr>
  <tr><th>Category</th><td>Skincare / Waterproof Eye Makeup & Mascara Removers</td></tr>
  <tr><th>Product Type</th><td>Gentle Alcohol-Free Eye Makeup Remover (125ml)</td></tr>
  <tr><th>Volume/Weight</th><td>125 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Eye Contour Skin Types (Including Sensitive)</td></tr>
  <tr><th>Finish</th><td>Clean, hydrated, refreshed eye contours with clear vision</td></tr>
  <tr><th>Texture</th><td>Ultra-light bi-phase clear liquid</td></tr>
  <tr><th>Fragrance</th><td>Subtle fresh Nivea scent</td></tr>
  <tr><th>Active Ingredients</th><td>Chamomile Extract, Nivea Caring Lipids, Alcohol-Free Base</td></tr>
  <tr><th>Country of Origin</th><td>Germany (Beiersdorf Germany)</td></tr>
  <tr><th>Manufacturer</th><td>Beiersdorf (Nivea)</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Bi-Phase Solvents & Eyelash Protection</h2>

<h3>What problem does this solve?</h3>
<p>Nivea Eye Makeup Remover resolves eyelash loss during mascara removal, blurry vision films, and eye stinging from harsh removers.</p>

<h3>Why choose Nivea Eye Remover?</h3>
<p>Bi-phase solvents dissolve waterproof wax polymers quickly, while Chamomile calms sensitive mucosal tissues without leaving an oily film.</p>"""

    en_faqs = [
        ("What is NIVEA Eye Makeup Remover 125ml?", "It is an ophthalmologist-tested gentle eye makeup remover formulated with Chamomile to erase waterproof mascara and protect eyelashes."),
        ("What are the benefits of Chamomile Extract for eye contours?", "Calms eye redness, soothes delicate skin, and seals in gentle moisture."),
        ("Does it remove waterproof mascara easily?", "Yes, clinically proven to dissolve stubborn waterproof mascara and eyeliner with a gentle cotton swipe."),
        ("What volume is contained in this bottle?", "It comes in a compact 125ml bottle."),
        ("How do I apply it correctly?", "Shake well, pour onto a cotton pad, hold over closed eye for 10 seconds, then wipe gently downward."),
        ("Does it protect eyelashes from falling out?", "Yes, eliminates harsh rubbing to keep delicate eyelashes intact."),
        ("Where is Nivea Eye Remover manufactured?", "It is proudly manufactured in Germany by Beiersdorf."),
        ("How do I verify authenticity at Ekleel Abha?", "All Nivea products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it leave a blurry film on eyes?", "No, ophthalmologist-tested formula ensures clear vision with zero oily film."),
        ("What scent does Nivea Eye Remover have?", "Features a subtle, light pleasant fresh scent."),
        ("Is it safe for contact lens wearers?", "Yes, ophthalmologist-tested and 100% safe for contact lens wearers and sensitive eyes."),
        ("Is the 125ml bottle travel-friendly?", "Yes, compact bottle fits easily into makeup pouches and travel bags."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Does it leave an oily heavy residue?", "No, leaves eye contour skin soft, clean, and refreshed."),
        ("Is the bottle cap leak-proof?", "Yes, comes in a sturdy bottle with a secure screw-top lid."),
        ("Is it ophthalmologist recommended?", "Yes, top recommended eye makeup remover by ophthalmologists globally."),
        ("How often can I use it daily?", "Use as needed to remove eye makeup."),
        ("Does it remove dry liquid eyeliners?", "Yes, dissolves long-wear liquid eyeliners, eyeshadows, and waterproof mascaras."),
        ("Is Nivea a trusted eye care brand?", "Yes, Nivea is the #1 globally trusted brand for gentle eye care."),
        ("Is it suitable for all age groups?", "Suitable for teens and adults aged 12+."),
        ("Does it hydrate delicate eye skin?", "Yes, Chamomile and moisturizing lipids soften delicate eye contour skin."),
        ("Is water rinsing required?", "No water rinsing needed; leaves eye contours clean directly."),
        ("Should the bottle be shaken before use?", "Yes, always shake well to blend the bi-phase formula prior to use."),
        ("Does it leave skin touchably soft?", "Yes, leaves eye skin soft and comfortable."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "العناية بالبشرة / مزيلات مكياج العيون والماسكارا المقاومة للماء",
        "brand": "Nivea",
        "ar": {
            "title": title_ar,
            "meta_title": "مزيل مكياج العيون نيفيا 125مل | صيدلية إكليل أبها",
            "meta_description": "اشتري مزيل مكياج العيون اللطيف من نيفيا (125 مل). إزالة الماسكارا المقاومة للماء بخلاصة البابونج دون حرقان. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["نيفيا", "مزيل_مكياج_العيون", "نيفيا_للمكياج", "حماية_الرموش", "إكليل_أبها"]
        },
        "en": {
            "title": title_en,
            "meta_title": "NIVEA Eye Makeup Remover 125ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original NIVEA Eye Makeup Remover (125ml). Erases waterproof mascara gently with Chamomile. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["nivea", "eye_makeup_remover", "waterproof_mascara_remover", "chamomile", "ekleel_abha"]
        },
        "schema": {
            "brand": "Nivea",
            "category": "Skincare / Eye Makeup Remover",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"{img_slug}.webp",
            "alt": title_en,
            "title": title_en
        }
    }

print("Loaded Batch 26 builders")
