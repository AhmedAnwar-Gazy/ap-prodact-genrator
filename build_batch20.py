import json, os

def build_vaseline_hand_cream(prod_id, title_ar, title_en, benefit_ar, benefit_en, gtin, img_slug):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{title_ar}</strong> المستحضر الطبي المتقدم والأجود عالمياً لإعادة النعومة، الترطيب المكثف، والوقاية الكاملة لبشرة اليدين الجافة والمجهدة. يرتكز هذا المستحضر من فازلين (Vaseline Intensive Care) على قطرات دقيقة من جل فازلين الأصلي (Vaseline Jelly Micro-Droplets) والزيوت المرطبة المغذية، حيث ينفذ في عمق خلايا الجلد ليمنحكِ ترطيباً 24 ساعة يمنع الجفاف والتطير.</p>
<p>يمتاز كريم فازلين لليدين بقوام ناعم غير دهني سريع الامتصاص يغلف اليدين والأظافر بحجاب حماية مغذٍ، مما يمنع جفاف الجلد والتحسس الناجم عن غسيل الأيدي والمنظفات ويترك يديكِ ملساء كالحرير.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب عميق 24 ساعة:</strong> يزود بشرة اليدين بالمرطبات الطبيعية ليمنع الجفاف والتطير.</li>
  <li><strong>قطرات جل فازلين الدقيقة (Vaseline Jelly):</strong> يحبس الرطوبة في الجلد ويدعم ترميم الحاجز الدهني.</li>
  <li><strong>{benefit_ar}:</strong> يغذي الجلد المحيط بالأظافر والأيدي شديدة الجفاف.</li>
  <li><strong>امتصاص سريع وغير دهني:</strong> ينفذ في الجلد فورياً دون إبقاء أثر دهني لزج على الأيدي.</li>
  <li><strong>نعومة حريرية طوال اليوم:</strong> يترك يديكِ ملساء، رطبة، ومفعمة بالمرونة.</li>
  <li><strong>أنبوب مدمج سعة 75 مل:</strong> حجم ممتاز ومثالي لحمله في حقيبة اليد أو السفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق):</strong> وضعي كمية بحجم حبة البازلاء من كريم فازلين على كف اليدين والأصابع.</li>
  <li><strong>الخطوة الثانية (التدليك):</strong> دلكي اليدين والجلد المحيط بالأظافر بعناية حتى يتم الامتصاص الكامل.</li>
  <li><strong>الخطوة الثالثة (التكرار):</strong> استخدميه بعد كل غسيل لليدين وقبل النوم لنتائج ممتازة.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>قطرات جل فازلين الدقيقة (Vaseline Jelly Micro-Droplets):</strong> تحفظ الرطوبة وتدعم ترميم الحاجز الدهني.</li>
  <li><strong>جليسرين وعوامل تنظيف لطيفة:</strong> يمنحان اليدين ملمساً حريرياً دون لزوجة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على اليدين فقط.</li>
  <li>تجنبي ملامسة الكريم المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تعاني من جفاف اليدين، ترهل الجلد، والتحسس الناجم عن غسيل الأيدي والمنظفات.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>فازلين (Vaseline)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات ترطيب وحماية اليدين</td></tr>
  <tr><th>نوع المنتج</th><td>كريم العناية المكثفة باليدين لترطيب البشرة الجافة (75ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>75 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة اليدين (الجافة، المجهدة، والحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>يدان ناعمتان كالحرير، مرطبتان لـ 24 ساعة وخاليتان من الجفاف</td></tr>
  <tr><th>الملمس</th><td>كريمي ناعم سريع الامتصاص غير دهني</td></tr>
  <tr><th>العطر</th><td>عطر الزهور الخفيف والزكي</td></tr>
  <tr><th>المكونات النشطة</th><td>قطرات فازلين الجل، جليسرين مرطب، زيوت مغذية</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة المتحدة / بولندا (Unilever)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Unilever (فازلين)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 10 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد كريمات فازلين لليدين الجافة (Vaseline Intensive Care)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم فازلين لليدين مشكلة جفاف وتخشن اليدين، تشقق الجلد، والتحسس الناجم عن غسيل الصابون المتكرر.</p>

<h3>لماذا تنجح تركيبة فازلين؟</h3>
<p>لأن قطرات جل فازلين الدقيقة تحفظ الرطوبة داخل خلايا الجلد، مما يمنع تبخر ماء البشرة لـ 24 ساعة دون لزوجة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام بعد غسل اليدين:</strong> ضعي الكريم فورياً بعد غسيل اليدين بالصابون.<br>
2. <strong>الحجم المناسب للحقيبة:</strong> احتفظي بالأنبوب 75 مل في حقيبتكِ للترطيب المستمر.<br>
3. <strong>الاستخدام قبل النوم:</strong> وضعي كمية سخية قبل النوم ونامي بجلد ناعم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات فازلين لليدين تترك أثراً دهنياً ثقيلاً."<br>
<strong>الحقيقة:</strong> كريم فازلين مصمم بتركيبة غير دهنية سريعة الامتصاص تنفذ فورياً دون لزوجة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتكامل قطرات الفازلين الجل مع طبقة الليبيدات السطحية بالجلد، مما يمنع تسرب المياه ويرمم تشققات الأيدي الجافة.</p>"""

    faqs = [
        (f"ما هو {title_ar}؟", f"هو كريم طبي مخصص للعناية باليدين الجافة وترطيبها لـ 24 ساعة بقطرات جل فازلين الدقيقة سعة 75 مل."),
        (f"ما هي فوائد قطرات جل فازلين لليدين؟", "تحفظ الرطوبة داخل خلايا الجلد، تمنع الت شقق والجفاف، وتمنح ملمساً حريرياً."),
        ("هل يوفر ترطيباً 24 ساعة؟", "نعم، مثبت سريرياً في حفظ رطوبة بشرة اليدين لـ 24 ساعة متواصلة."),
        ("ما حجم أنبوب الكريم؟", "يأتي بحجم 75 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي كمية على اليدين ودلكي بعناية بعد غسل اليدين وقبل النوم."),
        ("هل يترك أثراً دهنياً لزجاً؟", "لا، فورمولا سريعة الامتصاص وغير دهنية تنفذ فورياً دون لزوجة."),
        ("ما هو بلد صنع كريم فازلين؟", "صُنع بواسطة شركة يونيلفر (Unilever) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات فازلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يهدئ تهيج اليدين من المنظفات الصابونية؟", "نعم، يرمم ويهدئ البشرة المتهيجة من الغسيل المتكرر والمنظفات."),
        ("ما هي رائحة كريم فازلين؟", "يتميز برائحة ناعمة زكية تمنح إحساساً بالنظافة."),
        ("هل يناسب الأيدي شديدة الجفاف؟", "نعم، صُمم خصيصاً لعلاج وترطيب الأيدي شديدة الجفاف والتطير."),
        ("هل يناسب النساء والرجال؟", "نعم، مناسب لتنعيم أيدي النساء والرجال."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف."),
        ("هل حجم 75 مل مناسب للحقيبة والسفر؟", "نعم، حجم أنبوب أنيق ومدمج مثالي لحمل الحقيبة والسفر."),
        ("هل يناسب الاستخدام اليومي المتكرر؟", "نعم، يُوصى باستخدامه بعد كل غسيل لليدين."),
        ("هل العبوة محكمة الغلق؟", "تأتي في أنبوب محكم بغطاء لولبي يمنع التسرب."),
        ("هل يناسب جميع أنواع البشرة؟", "مناسب جداً للبشرة العادية، الجافة، والحساسة."),
        ("هل يمتص فورياً على الجلد؟", "نعم، يمتص في ثوانٍ معدودة."),
        ("هل يمنع تشقق اليدين في الشتاء؟", "نعم، يوفر درع حماية يقي الأيدي من برودة وجفاف الشتاء."),
        ("هل هو الكريم رقم 1 الموصى به لليدين؟", "نعم، فازلين الماركة رقم 1 عالمياً للعناية باليدين."),
        ("هل يساعد في ترطيب الأكواع أيضاً؟", "يمكن استخدامه لترطيب الأكواع والمناطق الجافة المدمجة."),
        ("هل يترك ملمساً حريرياً؟", "نعم، يترك يديكِ ملساء ونظيفة طوال اليوم."),
        ("هل يمكن استخدامه قبل ارتداء القفازات؟", "نعم، ممتاز لحماية اليدين قبل ارتداء قفازات التنظيف."),
        ("هل يعيد النضارة للأيدي المجهدة؟", "نعم، ترطيب 24 ساعة يعيد النضارة والنعومة للأيدي المجهدة."),
        ("هل يتوفر بنوعيات أخرى لدى إكليل أبها؟", "نعم، تتوفر كريمات فازلين المتعددة لليدين والجسم.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{title_en}</strong> is the world's #1 clinical hand conditioning lotion formulated to deeply hydrate and repair dry, overworked hand skin. Engineered by Vaseline Intensive Care, it fuses micro-droplets of original Vaseline Jelly with rich moisturizing lipids to deliver continuous 24-hour hydration.</p>
<p>Featuring a lightweight, fast-absorbing non-greasy texture, Vaseline Hand Lotion shields hand skin against soap stripping, environmental dryness, and flaking, leaving your hands touchably silky smooth all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>24-Hour Continuous Hand Hydration:</strong> Feeds dermal layers to stop dry hand tightness and flaking.</li>
  <li><strong>Vaseline Jelly Micro-Droplets:</strong> Seals moisture into skin and rebuilds the protective lipid barrier.</li>
  <li><strong>{benefit_en}:</strong> Deeply restores rough hand texture and protects cuticles.</li>
  <li><strong>Fast-Absorbing & Non-Greasy:</strong> Absorbs in seconds without leaving oily film on hands or devices.</li>
  <li><strong>All-Day Silky Smoothness:</strong> Keeps hands touchably soft, smooth, and supple.</li>
  <li><strong>Compact 75ml Tube:</strong> Perfect handbag and travel size for daily on-the-go hand care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply):</strong> Dispense a pea-sized amount of Vaseline hand cream onto palms and fingers.</li>
  <li><strong>Step 2 (Massage):</strong> Massage gently into hands and cuticles until fully absorbed.</li>
  <li><strong>Step 3 (Repeat):</strong> Reapply after handwashing and before bedtime for best hydration results.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Vaseline Jelly Micro-Droplets:</strong> Seal moisture into skin layers and heal dry flaking.</li>
  <li><strong>Hydrating Glycerin:</strong> Softens rough hand texture without greasy heaviness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external hand moisturizing application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dry, rough, or soap-stripped hands seeking 24-hour non-greasy hand moisturizing care.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Vaseline</td></tr>
  <tr><th>Category</th><td>Skincare / Hand Conditioning Creams & Lotions</td></tr>
  <tr><th>Product Type</th><td>24-Hour Hydrating Hand Lotion ({gtin[-4:]}) (75ml)</td></tr>
  <tr><th>Volume/Weight</th><td>75 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hand Skin Types (Dry, Soap-Stripped, Rough)</td></tr>
  <tr><th>Finish</th><td>Silky soft hands, 24h hydrated & protected skin</td></tr>
  <tr><th>Texture</th><td>Creamy fast-absorbing non-greasy lotion</td></tr>
  <tr><th>Fragrance</th><td>Subtle clean fresh fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Vaseline Jelly Micro-Droplets, Hydrating Glycerin</td></tr>
  <tr><th>Country of Origin</th><td>United Kingdom / Poland (Unilever)</td></tr>
  <tr><th>Manufacturer</th><td>Unilever (Vaseline)</td></tr>
  <tr><th>Age Group</th><td>All Ages (10+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Vaseline Jelly Micro-Droplets & Dermal Hand Moisture</h2>

<h3>What problem does this solve?</h3>
<p>Vaseline Hand Lotion resolves dry hand tightness, soap stripping, flaking, and rough skin texture.</p>

<h3>Why choose Vaseline?</h3>
<p>Micro-droplets of Vaseline Jelly seal in skin moisture, providing a 24-hour hydration shield that restores softness without greasy heaviness.</p>"""

    en_faqs = [
        (f"What is {title_en}?", f"It is an intensive hand lotion formulated with Vaseline Jelly micro-droplets to hydrate and repair dry hands for 24 hours."),
        ("What are the benefits of Vaseline Jelly micro-droplets?", "Seals moisture into skin layers, prevents dry flaking, and repairs protective lipid barriers."),
        ("Does it provide 24-hour hand hydration?", "Yes, clinically proven to lock in hand moisture for 24 continuous hours."),
        ("What volume is contained in this tube?", "It comes in a compact 75ml tube."),
        ("How do I apply it correctly?", "Massage a small amount into hands and cuticles after washing hands."),
        ("Does it leave a greasy residue on hands?", "No, fast-absorbing non-greasy formula absorbs in seconds without leaving oily film."),
        ("Where is Vaseline manufactured?", "It is produced by Unilever following global quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Vaseline products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it soothe soap-stripped hands?", "Yes, deeply restores and soothes skin irritated by frequent handwashing."),
        ("What scent does it have?", "Features a subtle, pleasant clean fresh fragrance."),
        ("Is it suitable for extremely dry hands?", "Yes, specially formulated for extremely dry, rough, and flaking hands."),
        ("Can both men and women use it?", "Yes, suitable for both men and women."),
        ("How should I store the tube?", "Store in a cool, dry place away from direct heat."),
        ("Is the 75ml tube handbag-friendly?", "Yes, compact tube fits easily into handbags and travel kits."),
        ("Is it safe for daily repeated use?", "Yes, recommended for use after every handwash."),
        ("Is the tube cap leak-proof?", "Yes, comes in a sturdy squeeze tube with a flip-top cap."),
        ("Is it suitable for all skin types?", "Ideal for normal, dry, and sensitive hand skin types."),
        ("Does it absorb quickly?", "Yes, absorbs completely into skin within seconds."),
        ("Does it prevent winter hand cracking?", "Yes, provides a protective barrier guarding hands against winter cold dryness."),
        ("Is it the #1 recommended hand brand?", "Yes, Vaseline is the #1 globally recommended hand care brand."),
        ("Can it be used on dry elbows?", "Yes, can be used for dry elbows and dry skin patches."),
        ("Does it leave hands silky soft?", "Yes, leaves hands touchably soft and smooth all day."),
        ("Can it be applied before household cleaning?", "Yes, excellent for protecting hands before wearing cleaning gloves."),
        ("Does it restore dry hand radiance?", "Yes, 24-hour hydration restores natural smoothness to dry hands."),
        ("Are other Vaseline hand creams available at Ekleel Abha?", "Yes, Ekleel Abha offers various Vaseline hand and body lotions.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "العناية بالبشرة / كريمات ترطيب وحماية اليدين",
        "brand": "Vaseline",
        "ar": {
            "title": title_ar,
            "meta_title": f"كريم فازلين لليدين 75مل | صيدلية إكليل أبها",
            "meta_description": f"اشتري {title_ar}. لترطيب وحماية اليدين بقطرات جل فازلين 24 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["فازلين", "كريم_فازلين_للبشرة", "ترطيب_اليدين", "إكليل_أبها"]
        },
        "en": {
            "title": title_en,
            "meta_title": f"Vaseline Hand Lotion 75ml | Ekleel Abha Pharmacy",
            "meta_description": f"Buy original {title_en}. 24-hour hydrating hand lotion with Vaseline Jelly micro-droplets. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["vaseline", "hand_lotion", "dry_skin_care", "24h_hydration", "ekleel_abha"]
        },
        "schema": {
            "brand": "Vaseline",
            "category": "Skincare / Hand Lotion",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"{img_slug}.webp",
            "alt": title_en,
            "title": title_en
        }
    }

def create_product_1808():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>صابون سيباميد الطبي لتنظيف البشرة الحساسة والمستعصية pH 5.5 (Sebamed Cleansing Bar for Sensitive and Problematic Skin)</strong> الصابون الخالي من الصابون والقلويات (100% Soap & Alkali-Free) والأول طبيًا عالمياً لتنظيف البشرة الحساسة، الدهنية، والمصابة بحب الشباب. يرتكز هذا القالب الطبي من سيباميد (Sebamed) على الرقم الهيدروجيني الفسيولوجي الموازن pH 5.5 المعزز بالفيتامينات والأحماض الأمينية الشافية والأنيولين الطبيعي (Inulin).</p>
<p>يعمل صابون سيباميد الطبي على تنظيف المسام بعمق، إزالة الدهون الزائدة والرؤوس السوداء، ودعم الغلاف الحمضي الطبيعي الواقي للبشرة (Acid Mantle)، مما يمنع تكاثر البكتيريا المسببة لحب الشباب والتهابات الجلد ويترك بشرتكِ معقمة، هادئة، ونظيفة تماماً.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>خالي 100% من الصابون والقلويات (100% Soap & Alkali-Free):</strong> ينظف المسام دون تجريف الغلاف الحمضي الواقي.</li>
  <li><strong>موازن للحموضة الطبيعية pH 5.5:</strong> يحافظ على بيئة الجلد الفسيولوجية ويمنع تكاثر البكتيريا.</li>
  <li><strong>ينقي البشرة الحساسة والمستعصية:</strong> يزيل الرؤوس السوداء، الدهون الزائدة، والشوائب بفاعلية طبية.</li>
  <li><strong>مدعم بالفيتامينات والأحماض الأمينية:</strong> يغذي الجلد ويسرع التئام حب الشباب والالتهابات.</li>
  <li><strong>يمنع تكون الحبوب والبثور:</strong> يطهر المسام ويمنع انسداد الجريبات الشعرية.</li>
  <li><strong>قالب طبي متين وزن 100 جم:</strong> يصمد طويلاً ويضمن نظافة طبية مستمرة للوجه والجسم.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبيل):</strong> بلي وجهك أو جسمك بالماء الفاتر وقالب صابون سيباميد.</li>
  <li><strong>الخطوة الثانية (الفرك):</strong> افركي الصابون بين الكفين لتوليد رغوة طبية خفيفة ودلكي البشرة برفق لمدة 1 دقيقة.</li>
  <li><strong>الخطوة الثالثة (الشطف):</strong> اشطفي بالماء الفاتر جيداً واستمتعي بنظافة معقمة دون جفاف.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركب الفيتامينات والأحماض الأمينية (Vitamins & Amino Acids):</strong> يرمم خلايا البشرة ويسرع الاندمال.</li>
  <li><strong>تركيبة pH 5.5 خالية من الصابون والقلويات:</strong> تحمي الغلاف الحمضي وتمنع نمو البكتيريا.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على بشرة الوجه والجسم فقط.</li>
  <li>تجنبي ملامسة الصابون المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي صحن صابون مصفى للماء ليجف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من البشرة الحساسة، الدهنية، المصابة بحب الشباب أو المشاكل الجلدية المستعصية.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>سيباميد (Sebamed)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / الصابون الطبي الخالي من الصابون للبشرة الحساسة</td></tr>
  <tr><th>نوع المنتج</th><td>قالب تنظيف طبي موازن للحموضة pH 5.5 (Cleansing Bar)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الحساسة، الدهنية، والمصابة بحب الشباب</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة نظيفة، معقمة، مطهرة، وخالية من الحبوب والدهون الزائدة</td></tr>
  <tr><th>الملمس</th><td>قالب تنظيف طبي يرغي برغوة خفيفة ناعمة</td></tr>
  <tr><th>العطر</th><td>عطر طبي خفيف جداً لطيف</td></tr>
  <tr><th>المكونات النشطة</th><td>تركيبة pH 5.5 خالية من الصابون، فيتامينات، أحماض أمينية، أنيولين</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا (Germany)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Sebapharma GmbH & Co. KG (سيباميد)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 10 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد التوازن الحمضي pH 5.5 وصابون سيباميد (Sebamed)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج صابون سيباميد الطبي مشكلة تكاثر بكتيريا حب الشباب (Propionibacterium acnes)، تهيج الصابون القلي، وانسداد المسام بالدهون.</p>

<h3>لماذا تنجح تركيبة pH 5.5؟</h3>
<p>لأن الرقم الهيدروجيني 5.5 يدعم الغلاف الحمضي الطبيعي (Acid Mantle)، مما يقتل البكتيريا الضارة دون تدمير حاجز البشرة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الغسيل مرتين يومياً:</strong> اغسلي الوجه بـ سيباميد صباحاً ومساءً.<br>
2. <strong>الحفظ على صحن مصفى:</strong> احفظي القالب على صحن مصفى للماء ليجف بسرعة.<br>
3. <strong>المرطب المهدئ:</strong> وضعي لوشن سيباميد المهدئ بعد الغسيل لنتائج مضاعفة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الصابون القلي العادي يطهر حب الشباب أفضل من الصابون الطبي."<br>
<strong>الحقيقة:</strong> الصابون القلي يدمر غشاء البشرة ويزيد إفراز الدهون، بينما سيباميد pH 5.5 يطهر المسام ب أمان.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط درجة الحموضة pH 5.5 نمو البكتيريا اللاهوائية في المسام، بينما تزيل المنظفات الخالية من الصابون الشوائب والزهم دون إحداث جفاف.</p>"""

    faqs = [
        ("ما هو صابون سيباميد الطبي لتنظيف البشرة الحساسة pH 5.5؟", "هو قالب تنظيف طبي ألماني خالي 100% من الصابون والقلويات بمستوى حموضة pH 5.5 لتنقية البشرة الحساسة والمعرضة لحب الشباب."),
        ("ما هي فوائد درجة الحموضة pH 5.5 للبشرة؟", "تدعم الغلاف الحمضي الطبيعي للبشرة وتمنع تكاثر بكتيريا حب الشباب والالتهابات."),
        ("هل هو خالي 100% من الصابون والقلويات؟", "نعم، خالي تماماً من الصابون التقليدي والقلويات القاسية (100% Soap & Alkali-Free)."),
        ("ما حجم قالب الصابون؟", "يأتي بحجم 100 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بلي الوجه والقالب، افركي لتوليد رغوة خفيفة، دلكي البشرة برفق ثم اشطفي بالماء الفاتر."),
        ("هل يزيل الرؤوس السوداء والدهون الزائدة؟", "نعم، ينظف المسام بعمق ويزيل الزهم والرؤوس السوداء دون تجفيف."),
        ("ما هو بلد صنع صابون سيباميد؟", "صُنع بفخر في ألمانيا بواسطة شركة سيبافارما (Sebapharma)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات سيباميد لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يناسب البشرة الدهنية والمصابة بحب الشباب؟", "ممتاز جداً للبشرة الدهنية والمصابة بحب الشباب والمشاكل المستعصية."),
        ("ما هي رائحة صابون سيباميد؟", "يتميز برائحة طبية ناعمة ولطيفة جداً."),
        ("هل يسبب جفاف البشرة أو حرقان؟", "لا، يحتوي على مرطبات وأحماض أمينية تحمي البشرة من الجفاف والحرقان."),
        ("هل يناسب غسيل الوجه والجسم معاً؟", "نعم، ممتاز لتنظيف بشرة الوجه والظهر والجسم المصاب بالحبوب."),
        ("كيف أحتفظ بقالب الصابون؟", "يُحفظ في صحن صابون مصفى للماء ليجف بعد كل استخدام."),
        ("هل يناسب المراهقين والبالغين؟", "نعم، مناسب للمراهقين والبالغين من سن 10 سنوات فما فوق."),
        ("هل هو خيار أطباء الجلدية الأول؟", "نعم، سيباميد الماركة الأولى الموصى بها طبياً من أطباء الجلدية عالمياً."),
        ("هل يساعد في تسريع اندمال البثور؟", "نعم، الفيتامينات والأحماض الأمينية تسرع التئام البثور والتهابات الجلد."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة كرتونية مغلفة طبقاً للمعايير الطبية الألمانيّة."),
        ("هل يناسب البشرة شديدة الحساسية والأكزيما؟", "نعم، تركيبة لطيفة مخصصة للبشرة شديدة الحساسية."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستخدم 2 مرات يومياً (صباحاً ومساءً)."),
        ("هل يساعد في تقليل مظهر المسام؟", "نعم، تنظيف الدهون يمنع تمدد وتوسع المسام."),
        ("هل يترك ملمساً معقماً ونظيفاً؟", "نعم، يمنح إحساساً بالنظافة والتعقيم الفائق دون لزوجة."),
        ("هل العبوة 100 جم اقتصادية؟", "نعم، قالب متين يصمد لعدة أسابيع من الاستخدام اليومي."),
        ("هل يحتوي على ملونات قاسية؟", "خالي من الصبغات والكيماويات الضارة."),
        ("هل يمكن استخدامه للحلاقة؟", "يمكن استخدامه لتنظيف الفروة والوجه قبل الحلاقة."),
        ("هل هو خيار ممتاز لجميع الفصول؟", "نعم، يحافظ على توازن البشرة في الصيف والشتاء.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Sebamed Cleansing Bar for Sensitive and Problematic Skin</strong> is the world's #1 dermatologist-recommended 100% Soap and Alkali-Free medicated cleansing bar tailored for sensitive, oily, and acne-prone skin types. Formulated in Germany by Sebapharma, it matches the natural physiological pH value of 5.5, enriched with healing vitamins, amino acids, and natural Inulin.</p>
<p>Sebamed Cleansing Bar deeply purifies pores, dislodges excess sebum and blackheads, and fortifies the skin's natural protective Acid Mantle, curbing acne-causing bacteria and leaving your skin thoroughly sanitized, calmed, and clear.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Soap & Alkali-Free Formula:</strong> Cleanses pores deeply without destroying the natural Acid Mantle.</li>
  <li><strong>Physiological pH 5.5 Balance:</strong> Preserves skin's natural barrier to prevent acne bacterial growth.</li>
  <li><strong>Purifies Sensitive & Problematic Skin:</strong> Clears blackheads, excess sebum, and impurities gently.</li>
  <li><strong>Enriched with Vitamins & Amino Acids:</strong> Feeds dermal cells and accelerates healing of acne pimples.</li>
  <li><strong>Prevents New Blemish Formation:</strong> Dislodges pore blockages before blackheads and pimples form.</li>
  <li><strong>Durable 100g Medicated Bar:</strong> Long-lasting bar ensuring continuous medical cleansing for face and body.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet face or body skin with warm water along with the Sebamed Cleansing Bar.</li>
  <li><strong>Step 2 (Lather):</strong> Rub bar between hands to create a light medicated lather and massage skin gently for 1 minute.</li>
  <li><strong>Step 3 (Rinse):</strong> Rinse thoroughly with warm water and enjoy sanitized, clean skin without dryness.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Vitamins & Amino Acids Complex:</strong> Restructures skin cells and accelerates acne healing.</li>
  <li><strong>100% Soap-Free pH 5.5 Base:</strong> Protects the Acid Mantle and inhibits bacterial proliferation.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external facial and body cleansing application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store on a draining soap dish to air dry.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with sensitive, oily, acne-prone, or problematic skin seeking a 100% soap-free pH 5.5 medical cleansing bar.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Sebamed</td></tr>
  <tr><th>Category</th><td>Skincare / 100% Soap-Free Medicated Cleansing Bars</td></tr>
  <tr><th>Product Type</th><td>pH 5.5 Medicated Cleansing Bar for Sensitive Skin (100g)</td></tr>
  <tr><th>Volume/Weight</th><td>100 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Sensitive, Oily, Acne-Prone & Problematic Skin</td></tr>
  <tr><th>Finish</th><td>Purified, sanitized, oil-free & acne-cleared facial skin</td></tr>
  <tr><th>Texture</th><td>Solid medicated bar producing light lather</td></tr>
  <tr><th>Fragrance</th><td>Subtle medical fresh scent</td></tr>
  <tr><th>Active Ingredients</th><td>100% Soap-Free Base, pH 5.5 Formula, Vitamins, Amino Acids</td></tr>
  <tr><th>Country of Origin</th><td>Germany</td></tr>
  <tr><th>Manufacturer</th><td>Sebapharma GmbH & Co. KG (Sebamed)</td></tr>
  <tr><th>Age Group</th><td>All Ages (10+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Biological pH 5.5 & Acid Mantle Protection</h2>

<h3>What problem does this solve?</h3>
<p>Sebamed Cleansing Bar resolves acne bacterial proliferation (P. acnes), alkaline soap irritation, and pore sebum clogging.</p>

<h3>Why choose Sebamed pH 5.5?</h3>
<p>Biological pH 5.5 supports the protective Acid Mantle, inhibiting acne bacteria growth without stripping skin moisture.</p>"""

    en_faqs = [
        ("What is Sebamed Cleansing Bar for Sensitive and Problematic Skin?", "It is a German 100% soap and alkali-free medicated cleansing bar matching biological pH 5.5 for sensitive and acne-prone skin."),
        ("What are the benefits of pH 5.5 for skin?", "Fortifies the natural Acid Mantle and inhibits acne-causing bacteria growth."),
        ("Is it 100% soap and alkali-free?", "Yes, completely free of traditional soaps and harsh alkalis (100% Soap & Alkali-Free)."),
        ("What volume is contained in this bar?", "It comes as a 100g medicated cleansing bar."),
        ("How do I use it correctly?", "Lather bar between wet hands, massage skin gently, and rinse with warm water."),
        ("Does it dislodge blackheads and excess oil?", "Yes, purifies pores deeply, clearing excess sebum and blackheads without dryness."),
        ("Where is Sebamed manufactured?", "It is proudly manufactured in Germany by Sebapharma."),
        ("How do I verify authenticity at Ekleel Abha?", "All Sebamed products at Ekleel Abha are 100% original from certified distributors."),
        ("Is it suitable for oily and acne-prone skin?", "Yes, highly recommended by dermatologists for oily, acne-prone, and problematic skin."),
        ("What scent does Sebamed have?", "Features a subtle, gentle fresh medical scent."),
        ("Does it cause skin tightness or burning?", "No, enriched with vitamins and amino acids to prevent skin dryness or stinging."),
        ("Can it be used for both face and body?", "Yes, excellent for facial cleansing and body acne care (back and chest)."),
        ("How should I store the bar?", "Store on a draining soap dish so it dries quickly between uses."),
        ("Is it suitable for teens and adults?", "Yes, suitable for teens and adults aged 10+."),
        ("Is Sebamed #1 dermatologist-recommended?", "Yes, Sebamed is the #1 globally recommended medical skin brand."),
        ("Does it accelerate acne healing?", "Yes, vitamins and amino acids nourish skin and accelerate blemish healing."),
        ("Is the packaging hygienic?", "Yes, packaged in a sterile medical carton box."),
        ("Is it suitable for sensitive skin and eczema?", "Yes, ultra-gentle formula safe for sensitive and eczema-prone skin."),
        ("How many times daily should I use it?", "Use twice daily, morning and evening."),
        ("Does it help minimize enlarged pores?", "Yes, dislodging trapped sebum prevents pore stretching."),
        ("Does it leave a clean sanitized feel?", "Yes, imparts an instant feeling of clean, sanitized protection."),
        ("Is the 100g bar long-lasting?", "Yes, solid durable bar lasts through weeks of daily use."),
        ("Does it contain harsh dyes?", "Free of harsh colorants and banned chemicals."),
        ("Can it be used prior to shaving?", "Yes, cleanses facial skin gently prior to shaving."),
        ("Is it ideal year-round?", "Yes, preserves skin barrier balance in all seasons.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1808",
        "sku": "EK-1808",
        "gtin": "4103040111784",
        "category": "العناية بالبشرة / الصابون الطبي الخالي من الصابون للبشرة الحساسة",
        "brand": "Sebamed",
        "ar": {
            "title": "صابون سيباميد الطبي لتنظيف البشرة الحساسة والمستعصية pH 5.5",
            "meta_title": "صابون سيباميد الطبي pH 5.5 100جم | صيدلية إكليل أبها",
            "meta_description": "اشتري صابون سيباميد الطبي لتنظيف البشرة الحساسة والمستعصية (pH 5.5). خالي 100% من الصابون والقلويات لحب الشباب. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["سيباميد", "صابون_سيباميد", "حب_الشباب", "pH_5.5", "إكليل_أبها"]
        },
        "en": {
            "title": "Sebamed Cleansing Bar for Sensitive and Problematic Skin",
            "meta_title": "Sebamed Cleansing Bar pH 5.5 100g | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Sebamed Cleansing Bar for Sensitive and Problematic Skin (pH 5.5). 100% Soap & Alkali-Free for acne skin. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["sebamed", "cleansing_bar", "ph_5_5", "acne_care", "ekleel_abha"]
        },
        "schema": {
            "brand": "Sebamed",
            "category": "Skincare / Cleansing Bar",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "sebamed-cleansing-bar-for-sensitive-and-problematic-skin.webp",
            "alt": "Sebamed Cleansing Bar for Sensitive and Problematic Skin",
            "title": "Sebamed Cleansing Bar for Sensitive and Problematic Skin"
        }
    }

def create_product_1809():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>بخاخ مجفف طلاء الأظافر السريع من مافالا - 150 مل (Mavala Nail Polish Dryer 150ml)</strong> المستحضر المبتكر والأساسي في روتين البديكير والمانيكير لتجفيف وتثبيت طلاء الأظافر (مناكير) في ثوانٍ معدودة. يعتمد هذا البخاخ الاحترافي على فورمولا منشطة سريعة التبخر مغذاة بزيوت التلميع اللطيفة، حيث يرش على طلاء الأظافر المبلل فيجففه فورياً، ويمنعه من التلطخ أو التخدش.</p>
<p>يمتاز بخاخ مافالا لتجفيف المناكير بإكفاء الأظافر بريقاً كريستالياً لافتاً، وتغذية حواف الجلد المحيط بالأظافر بالمرطبات، ليمنحكِ مانيكير صالونات احترافياً ومثالياً في المنزل بدقيقة واحدة فقط.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تجفيف الفوري لطلاء الأظافر في ثوانٍ:</strong> يسرع جفاف المناكير ويمنع التلطخ أو البصمات.</li>
  <li><strong>إعطاء بريق كريستالي لامع:</strong> يزيد من لمعان وبريق طلاء الأظافر لإطلالة صالونات فاخرة.</li>
  <li><strong>تغذية وترطيب الجلد المحيط بالأظافر:</strong> يزود حواف الأظافر بزيوت التهدئة ومنع الجفاف.</li>
  <li><strong>رذاذ ميكرو دقيق غير متكتل:</strong> يتوزع بسلاسة على الأظافر دون إحداث فقاعات أو عيوب.</li>
  <li><strong>سهل وسريع الاستخدام:</strong> رشة واحدة على الأظافر المبللة تضمن تثبيت المناكير فورياً.</li>
  <li><strong>عبوة وافرة سعة 150 مل:</strong> حجم ممتازة تكفي ل عشرات جلسات المانيكير والبديكير.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (طلاء الأظافر):</strong> وضعي طلاء الأظافر المفضّل واطلعي بالطبقة النهائية (Top Coat).</li>
  <li><strong>الخطوة الثانية (الرش):</strong> بعد انتهاء الطلاء بـ 60 ثانية، رشي بخاخ مافالا على الأظافر من مسافة 15 سم.</li>
  <li><strong>الخطوة الثالثة (التجفيف):</strong> دعي الرذاذ يجف لـ 10 ثوانٍ واستمتعي بطلاء أظافر ناعم، ثابت، ولامع فورياً.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركبات التجفيف السريع (Fast-Drying Agents):</strong> تسرع تبخر مذيبات طلاء الأظافر وتثبته.</li>
  <li><strong>زيوت تلميع وترطيب الأظافر:</strong> تعزز بريق المناكير وتغذي الـ Cuticles.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الأظافر فقط.</li>
  <li>عبوة مضغوطة قابلة للاشتعال؛ تُحفظ بعيداً عن الحرارة الشديدة والشمس ومصادر النيران.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة وعاشقة للمناكير ترغب في تجفيف طلاء الأظافر فورياً وإعطائه بريق صالونات كريستالياً.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>مافالا / عام (Mavala)</td></tr>
  <tr><th>الفئة</th><td>العناية بالأظافر / بخاخات ومستحضرات تجفيف المناكير السريع</td></tr>
  <tr><th>نوع المنتج</th><td>بخاخ تجفيف وتثبيت طلاء الأظافر السريع (Nail Polish Dryer 150ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>150 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (العناية بالأظافر والمانيكير)</td></tr>
  <tr><th>المظهر النهائي</th><td>طلاء أظافر جاف فورياً، لامع كالكراستال وخالٍ من التلطخ</td></tr>
  <tr><th>الملمس</th><td>رذاذ شفاف سريع التبخر واللمعان</td></tr>
  <tr><th>العطر</th><td>عطر خفيف لطيف</td></tr>
  <tr><th>المكونات النشطة</th><td>مركبات التجفيف السريع، زيوت تلميع الأظافر، مرطبات الجلد</td></tr>
  <tr><th>بلد المنشأ</th><td>سويسرا / فرنسا (Mavala Switzerland)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Mavala Switzerland Labs</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد بخاخات تجفيف طلاء الأظافر السريع (Mavala)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج بخاخ تجفيف الأظافر مشكلة الانتظار الطويل لجفاف المناكير، تلطخ البصمات، وتلف المانيكير بعد التطبيق مباشرة.</p>

<h3>لماذا تنجح تركيبة التجفيف السريع؟</h3>
<p>لأن الرذاذ المنشط يمتص المذيبات المتطايرة بطلاء الأظافر ويثبت الرابطة الكيميائية في ثوانٍ، مع تكوين طبقة حماية برّاقة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الانتظار 60 ثانية قبل الرش:</strong> انتظري دقيقة بعد وضع المناكير قبل الرش.<br>
2. <strong>الرش بمسافة 15 سم:</strong> رشي بالتساوي على كافة الأظافر من مسافة مناسبة.<br>
3. <strong>ترطيب الجلد المحيط:</strong> دلكي الزيوت المتبقية على الجلد المحيط بالأظافر لترطيبه.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "بخاخات تجفيف المناكير تقشر طلاء الأظافر وتفقده بريقه."<br>
<strong>الحقيقة:</strong> بخاخ مافالا يحتوي على زيوت تلميع تعزز بريق المناكير الكريستالي وتزيد ثباته.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تسرع المذيبات الطيارة بالرذاذ عملية التبلور السطحي لطلاء الأظافر (Polymerization)، مما يحول الجل المبلل إلى طبقة صلبة لامعة فورياً.</p>"""

    faqs = [
        ("ما هو بخاخ مجفف طلاء الأظافر السريع 150 مل؟", "هو بخاخ احترافي يسرع تجفيف طلاء الأظافر (المناكير) في ثوانٍ ويمنع التلطخ ويمنح بريقاً كريستالياً."),
        ("هل يجفف طلاء الأظافر في ثوانٍ؟", "نعم، مثبت في تسريع تجفيف المناكير فورياً ومنع بصمات وتخدش الأظافر."),
        ("ما هي فوائد زيوت التلميع في البخاخ؟", "تعزز لمعان وبريق طلاء الأظافر وتغذي الجلد المحيط بالأظافر (Cuticles)."),
        ("ما حجم العبوة؟", "تأتي بحجم 150 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي المناكير، انتظري 60 ثانية، ثم رشي البخاخ من مسافة 15 سم على الأظافر واتركيه يجف."),
        ("هل يمنع تلطخ وتخدش المناكير؟", "نعم، يثبت طبقة المناكير فورياً ويحميها من التلطخ والخدوش."),
        ("ما هو بلد صنع المنتج؟", "صُنع وفق أعلى معايير العناية بالأظافر السويسرية والأوروبية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع مستحضرات العناية بالأظافر لدى إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يترك أثراً لزجاً؟", "لا، رذاذ يتطاير ويجف فورياً ليترك الأظافر جافة ولامعة."),
        ("هل يناسب جميع أنواع طلاء الأظافر؟", "نعم، يعمل بكفاءة مع كافة أنواع المناكير والـ Top Coat."),
        ("هل العبوة 150 مل تكفي لعدة جلسات؟", "نعم، عبوة وافرة تكفي لعشرات جلسات المانيكير والبديكير."),
        ("هل يناسب الاستخدام المنزلي والصالونات؟", "نعم، ممتازة جداً للاستخدام المنزلي السريع ولصالونات التجميل."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الحرارة المباشرة والشمس."),
        ("هل البخاخ دقيق في التوزيع؟", "نعم، بخاخ ميكرو يوزع الرذاذ بالتساوي على الأصابع."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة معدنية أنيقة بغطاء محكم الحماية."),
        ("هل يمنع تفقيد بريق المناكير؟", "بالعكس، يزيد من لمعان وبريق طلاء الأظافر الكريستالي."),
        ("هل يناسب جميع الأعمار؟", "مناسب للمراهقات والبالغين من سن 12 سنة فما فوق."),
        ("هل يترك رائحة زكية؟", "يتميز برائحة خفيفة لطيفة مقبولة."),
        ("هل يسهل تنظيف الزيوت المتبقية؟", "دلكي الزيوت المتبقية على الجلد المحيط لزيادة الترطيب."),
        ("هل يحمي الأظافر من التثلم؟", "نعم، التثبيت السريع يمنع انكسار وتثلم الطلاء."),
        ("هل يساعد في توفير الوقت؟", "نعم، يغنيكِ عن الانتظار الطويل لجفاف الأظافر."),
        ("هل العبوة مضغوطة؟", "نعم، عبوة أيروسول مضغوطة سهلة الرش بضغطة واحدة."),
        ("هل هو خيار خبيرات المانيكير؟", "نعم، المستحضر رقم 1 الأساسي في جلسات المانيكير السريعة."),
        ("هل يترك أثراً على الأيدي؟", "لا، يرطب الجلد المحيط دون ترك أي لزوجة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Nail Polish Dryer 150ml</strong> is the professional manicurist essential spray designed to dry and set nail polish (lacquer) in seconds. Formulated with fast-evaporating setting agents infused with nourishing shine oils, it sprays onto freshly painted nails to dry them instantly, preventing smudges, fingerprints, and scratches.</p>
<p>Delivering salon-quality results at home in under a minute, this quick nail polish dryer enhances lacquer gloss with a crystal finish while conditioning cuticles with lightweight hydrating oils.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Instant Seconds Nail Polish Drying:</strong> Accelerates nail polish drying time to stop smudges and marks.</li>
  <li><strong>Crystal Gloss Enhancement:</strong> Enhances nail lacquer shine for a high-gloss salon-finish result.</li>
  <li><strong>Conditions Cuticles & Skin:</strong> Infuses cuticle borders with lightweight nourishing conditioning oils.</li>
  <li><strong>Micro-Fine Smooth Mist:</strong> Dispenses evenly without creating air bubbles or polish streaks.</li>
  <li><strong>Quick & Effortless Application:</strong> A single mist spray over freshly painted nails locks polish instantly.</li>
  <li><strong>Generous 150ml Can:</strong> High-value spray bottle lasting through dozens of manicure sessions.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply Polish):</strong> Apply your favorite nail polish and top coat.</li>
  <li><strong>Step 2 (Mist):</strong> Wait 60 seconds after painting, then spray Nail Polish Dryer 15 cm away from nails.</li>
  <li><strong>Step 3 (Dry & Shine):</strong> Let mist settle for 10 seconds and enjoy touch-dry, high-gloss nails instantly.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Fast-Drying Solvents:</strong> Accelerate nail lacquer solvent evaporation for instant fixation.</li>
  <li><strong>Nail Gloss & Cuticle Oils:</strong> Enhance polish gloss and condition cuticle borders.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external nail application only.</li>
  <li>Pressurized flammable container; keep away from high heat, sparks, open flames, and direct sunlight.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone wanting to dry freshly painted nail polish instantly with a high-gloss salon finish.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Mavala / Generic</td></tr>
  <tr><th>Category</th><td>Nail Care / Quick Nail Polish Dryers & Fixatives</td></tr>
  <tr><th>Product Type</th><td>Quick Fast-Drying Nail Polish Spray (150ml)</td></tr>
  <tr><th>Volume/Weight</th><td>150 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Nail & Manicure Care)</td></tr>
  <tr><th>Finish</th><td>Touch-dry, high-gloss crystal & smudge-proof nails</td></tr>
  <tr><th>Texture</th><td>Micro-fine fast-evaporating clear mist spray</td></tr>
  <tr><th>Fragrance</th><td>Subtle fresh fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Fast-Drying Solvents, Nail Gloss & Cuticle Oils</td></tr>
  <tr><th>Country of Origin</th><td>Switzerland / France</td></tr>
  <tr><th>Manufacturer</th><td>Mavala Switzerland Labs</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Fast Solvent Evaporation & Lacquer Polymerization</h2>

<h3>What problem does this solve?</h3>
<p>Nail Polish Dryer 150ml resolves long nail drying wait times, fingerprint smudges, and ruined manicures.</p>

<h3>Why choose Nail Polish Dryer?</h3>
<p>Fast-evaporating setting agents absorb volatile nail polish solvents, accelerating surface polymerization into a hard, glossy shield in seconds.</p>"""

    en_faqs = [
        ("What is Nail Polish Dryer 150ml?", "It is a professional spray formulated to dry nail polish instantly, prevent smudges, and add crystal shine."),
        ("Does it dry nail polish in seconds?", "Yes, clinically proven to accelerate nail lacquer drying and prevent fingerprints."),
        ("What are the benefits of gloss oils in the spray?", "Enhances nail polish crystal shine and conditions cuticle borders."),
        ("What volume is contained in this can?", "It comes in a generous 150ml aerosol spray can."),
        ("How do I apply it correctly?", "Apply nail polish, wait 60 seconds, then spray mist 15 cm away from nails."),
        ("Does it stop smudges and scratches?", "Yes, sets nail lacquer instantly protecting it from smudges and scratches."),
        ("Where is it manufactured?", "Produced following Swiss and European precision nail care standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All nail care products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it leave a sticky residue?", "No, clear fine mist evaporates quickly leaving touch-dry, glossy nails."),
        ("Is it compatible with all nail polishes?", "Yes, works effectively with all brands of nail lacquers and top coats."),
        ("Is the 150ml can long-lasting?", "Yes, generous volume lasts through dozens of manicure sessions."),
        ("Is it suitable for home and professional salon use?", "Yes, ideal for quick home manicures and professional nail salons."),
        ("How should I store the spray can?", "Store in a cool, dry place away from heat, sparks, and direct sunlight."),
        ("Does the nozzle spray evenly?", "Yes, micro-fine nozzle distributes mist evenly across fingernails."),
        ("Is the container pressurized?", "Yes, comes in a sturdy pressurized spray can."),
        ("Does it dull nail polish shine?", "No, on the contrary, it enhances nail polish crystal gloss."),
        ("What age group is it for?", "Suitable for teens and adults aged 12+."),
        ("Does it have a heavy odor?", "Features a subtle, light pleasant scent."),
        ("What should I do with leftover oil on cuticles?", "Massage leftover oils into cuticles for added skin hydration."),
        ("Does it prevent nail chipping?", "Yes, rapid setting guards nail lacquer against early chipping."),
        ("Does it save manicure time?", "Yes, eliminates long drying wait times completely."),
        ("Is it a single-press aerosol spray?", "Yes, easy one-press spray application."),
        ("Is it recommended by manicurists?", "Yes, a staple tool among professional nail technicians."),
        ("Does it leave hands feeling soft?", "Yes, conditions cuticles without greasy heaviness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1809",
        "sku": "EK-1809",
        "gtin": "7618900916609",
        "category": "العناية بالأظافر / بخاخات ومستحضرات تجفيف المناكير السريع",
        "brand": "Mavala",
        "ar": {
            "title": "بخاخ مجفف طلاء الأظافر السريع من مافالا - 150 مل",
            "meta_title": "بخاخ مجفف طلاء الاظافر مافالا 150مل | صيدلية إكليل أبها",
            "meta_description": "اشتري بخاخ مجفف طلاء الأظافر السريع من مافالا (150 مل). تجفيف المناكير في ثوانٍ مع بريق كريستالي. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["مافالا", "مجفف_المناكير", "طلاء_الأظافر", "تجفيف_الأظافر", "إكليل_أبها"]
        },
        "en": {
            "title": "Nail Polish Dryer 150ml",
            "meta_title": "Nail Polish Dryer Spray 150ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Nail Polish Dryer 150ml (Mavala). Dries nail polish in seconds with high-gloss crystal finish. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["mavala", "nail_polish_dryer", "quick_dry_spray", "manicure_care", "ekleel_abha"]
        },
        "schema": {
            "brand": "Mavala",
            "category": "Nail Care / Nail Polish Dryer",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "nail-polish-dryer-150ml.webp",
            "alt": "Nail Polish Dryer 150ml",
            "title": "Nail Polish Dryer 150ml"
        }
    }

print("Loaded Batch 20 builders")
