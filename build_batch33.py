import json, os

def create_product_1876():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم تفتيح المنطقة الحساسة من بيزلين 50مل (Beesline Whitening Sensitive Zone Cream - 50ml)</strong> المستحضر الطبي النباتي الأكثر شهرة وأماناً عالمياً المخصص لتفتيح التصبغات، تهدئة التهيج، وتوحيد لون بشرة المناطق الحساسة والمثنيات بكل رفق. يرتكز هذا الكريم المميز من بيزلين (Beesline Whitening Sensitive Zone Cream 50ml) على مركب اللوميسكين المبيض (Lumiskin)، زيت جوز الهند النقي، صمغ النحل الشافي (Propolis)، وفيتامينات C و E.</p>
<p>يعمل كريم بيزلين لتفتيح المنطقة الحساسة على تقليل صبغة الميلامين الناتجة عن الاحتكاك ورطوبة الملابس، تنعيم البشرة الجافة بالمناطق الحميمة، وتأمين حماية مضادة للبكتيريا والروائح الكريهة، ليترك منطقتكِ الحساسة ناصعة، موحدة اللون، وناعمة كالحرير دون تسبيب أي حرقان أو تهيج.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح آمن وتوحيد لون المنطقة الحساسة والمثنيات:</strong> يزيل التصبغات الداكنة الناتجة عن الاحتكاك.</li>
  <li><strong>مدعم بـ اللوميسكين وفيتامينات C و E:</strong> يثبط صبغة الميلامين ويجدد خلايا الجلد الرقيقة.</li>
  <li><strong>تطهير وتهدئة بـ صمغ النحل (Propolis):</strong> يحمي المنطقة الحميمة من البكتيريا والالتهابات.</li>
  <li><strong>ترطيب وتنعيم بـ زيت جوز الهند النقي:</strong> يمنح الجلد طراوة ونعومة ناصعة.</li>
  <li><strong>خالي 100% من الكحول، البارابين، والهيدروكينون الضار:</strong> تركيبة دقيقة ومجربة جلدياً للمناطق الرقيقة.</li>
  <li><strong>عبوة مدمجة سعة 50 مل:</strong> حجم ممتاز ومناسب للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> نظفي المنطقة الحساسة بغسول بيزلين للمناطق الحساسة الفاتر وجففيها جيداً.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي كمية صغيرة من كريم بيزلين على بشرة المنطقة الحساسة والمثنيات.</li>
  <li><strong>الخطوة الثالثة (التدليك):</strong> دلكي برفق بحركات دائرية ناعمة حتى امتصاص الكريم بالكامل (يُستعمل 2 مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركب لوميسكين وفيتامين C (Lumiskin & Vit C):</strong> يثبطان إنزيم التايروسينيز ويفتحان البقع التصبغية.</li>
  <li><strong>صمغ النحل وزيت جوز الهند:</strong> يطهران الجلد ويحفظان الترطيب والنعومة المخملية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة المنطقة الحساسة الخارجية فقط.</li>
  <li>تجنبي ملامسة الكريم للمناطق الداخلية أو الجلد المصاب بجروح مفتوحة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تعاني من تصبغات المناطق الحساسة والمثنيات وتفتش عن كريم بيزلين النباتي الأصلي 50 مل.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / كريمات بيزلين الطبية لتفتيح وتلطيف المناطق الحساسة 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>كريم طبيعي لتفتيح وتوحيد لون بشرة المناطق الحساسة (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة المناطق الحساسة (بما في ذلك البشرة الرقيقة والجافة)</td></tr>
  <tr><th>المظهر النهائي</th><td>منطقة حساسة ناصعة، موحدة اللون، خالية من التصبغات ومحمية وطازجة</td></tr>
  <tr><th>الملمس</th><td>كريم ناعم مخملي خفيف سريع الامتصاص دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر بيزلين اللطيف الطبيعي الناعم</td></tr>
  <tr><th>المكونات النشطة</th><td>لوميسكين، صمغ النحل (Propolis)، زيت جوز الهند، فيتامين C</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>النساء والفتيات (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد اللوميسكين وصمغ النحل في بيزلين للمناطق الحساسة (Beesline Sensitive Zone)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم بيزلين للمناطق الحساسة مشكلة التصبغات الداكنة الناتجة عن الاحتكاك، الرطوبة، الجفاف، والالتهابات البكتيرية.</p>

<h3>لماذا تنجح تركيبة اللوميسكين وصمغ النحل؟</h3>
<p>لأن اللوميسكين يثبط تكاثر الميلامين ب أمان دون إحداث حرقان، بينما يطهر صمغ النحل الفطريات وينعم الجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق مرتين يومياً على بشرة جافة:</strong> استعملي الكريم صباحاً ومساءً فور تجفيف المنطقة.<br>
2. <strong>ارتداء ملابس قطنية واسعة:</strong> التقليل من الاحتكاك والملابس الضيقة يسرع نتائج التفتيح.<br>
3. <strong>الاستمرار لـ 3 أسابيع:</strong> يضمن الاستخدام المنتظم توحيد لون المنطقة الحساسة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات تفتيح المناطق الحساسة تسبب حرقان دائم والتهابات خطيرة."<br>
<strong>الحقيقة:</strong> كريم بيزلين خالي من الهيدروكينون والكحول والبارابين ومجرب جلدياً لسلامة المناطق الرقيقة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط مركبات اللوميسكين استقبال الدوبامين ب خلايا الميلاين، بينما تنعم الفلافونويدات بالـ Propolis الأنسجة.</p>"""

    faqs = [
        ("ما هو كريم تفتيح المنطقة الحساسة من بيزلين 50مل؟", "هو كريم طبيعي نباتي من بيزلين باللوميسكين وصمغ النحل لتفتيح وتوحيد لون بشرة المناطق الحساسة سعة 50 مل."),
        ("ما هي فوائد اللوميسكين وصمغ النحل وزيت جوز الهند؟", "يثبط اللوميسكين صبغة الميلامين، يطهر صمغ النحل البكتيريا، وينعم زيت جوز الهند الجلد الجاف."),
        ("هل يفتّح التصبغات واسمرار المنطقة الحساسة ب أمان؟", "نعم، مثبت سريرياً في تفتيح التصبغات وتوحيد لون المنطقة الحساسة دون حرقان."),
        ("ما حجم العبوة؟", "تأتي لأنبوب مدمج سعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي كمية صغيرة على بشرة المنطقة الحساسة الخارجية النظيفة والجافة، دلكي برفق مرتين يومياً."),
        ("هل هو خالي 100% من الكحول والبارابين والهيدروكينون؟", "نعم، تركيبة طبيعية خالية 100% من الهيدروكينون والبارابين والكحول."),
        ("ما هو بلد صنع كريم بيزلين للمناطق الحساسة؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين العالمية (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يناسب البشرة الحساسة جداً؟", "نعم، فورمولا مهدئة ومجربة جلدياً ومناسبة للبشرة الحساسة."),
        ("ما هي رائحة كريم بيزلين للمناطق الحساسة؟", "يتميز برائحة ناعمة ولطيفة جداً."),
        ("هل يمتص بسرعة دون ترك لزوجة دهنية؟", "نعم، قوام مخملي خفيف ينفذ فورياً بالجلد دون أي لزوجة."),
        ("هل أنبوب العبوة 50 مل مناسب للاستخدام اليومي؟", "نعم، حجم مدمج وأنيق يكفي للاستخدام المستمر لعدة أسابيع."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل يمنع التهيج والروائح الكريهة؟", "نعم، صمغ النحل يطهر البكتيريا ويمنع التهيج والروائح الكريهة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في أنبوب أنيق بغطاء محكم الحماية."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل 2 مرات يومياً (صباحاً ومساءً)."),
        ("هل يناسب النساء والرجال؟", "مناسب للبالغين للنساء والرجال من سن 12 سنة."),
        ("هل يمنع عودة التصبغات؟", "نعم، الاستخدام المنتظم يمنع تكاثر البقع التصبغية."),
        ("هل هو كريم تفتيح المنطقة الحساسة الأكثر طلبياً؟", "نعم، كريم بيزلين للمناطق الحساسة الخيار الأول والأكثر مبيعاً عالمياً."),
        ("هل يمنح حس نضارة وثقة مطلقة؟", "نعم، يضمن نضارة وصفاءً وثقة مطلقة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يطري الجلد ويمنع القشور؟", "نعم، ينعم الجلد الجاف ويمنع تشكل القشور."),
        ("هل يترك المنطقة ناعمة كالحرير؟", "نعم، يترك جلد المنطقة الحساسة ناعماً ومخملياً."),
        ("هل يناسب الاستخدام اليومي المستمر؟", "نعم، تركيبة طبيعية 100% مناسبة للاستخدام اليومي المستمر."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Whitening Sensitive Zone Cream - 50ml</strong> is the world's most trusted natural clinical cream engineered to brighten dark hyperpigmentation, soothe irritation, and unify intimate skin tone gently. Formulated by Beesline, it blends botanical Lumiskin, pure Coconut Oil, antibacterial Propolis, and Vitamins C & E.</p>
<p>Beesline Sensitive Zone Cream reduces melanin pigmentation triggered by friction and moisture, hydrates dry delicate skin in intimate zones, and delivers antimicrobial protection against bad odors, leaving your sensitive area touchably soft, evenly brightened, and smooth without stinging.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Safe Intimate Skin Whitening & Tone Unification:</strong> Fades dark hyperpigmentation caused by friction.</li>
  <li><strong>Enriched with Lumiskin & Vitamins C & E:</strong> Inhibits melanin synthesis and renews delicate skin cells.</li>
  <li><strong>Purifying Propolis Defense:</strong> Shields intimate skin against bacteria and fungal irritation.</li>
  <li><strong>Deep Hydration with Pure Coconut Oil:</strong> Softens delicate skin patches leaving them touchably supple.</li>
  <li><strong>100% Free of Alcohol, Parabens & Harmful Hydroquinone:</strong> Clinically tested safe formula for intimate skin.</li>
  <li><strong>Compact 50ml Tube:</strong> High-value tube ideal for continuous daily intimate grooming.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse intimate external skin with a gentle Beesline wash and pat dry thoroughly.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a small amount of Beesline Sensitive Zone cream onto clean intimate skin patches.</li>
  <li><strong>Step 3 (Massage):</strong> Massage gently in smooth circular motions until fully absorbed (use twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Lumiskin & Vitamin C:</strong> Inhibit tyrosinase melanin synthesis to fade dark hyperpigmentation spots.</li>
  <li><strong>Propolis & Coconut Oil:</strong> Purify dermal tissues and maintain deep 24-hour hydration and softness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical intimate skin application only; do not apply internally.</li>
  <li>Avoid direct contact with open wounds or severely broken skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dark intimate hyperpigmentation or friction patches seeking Beesline's 50ml natural Sensitive Zone Cream.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Skincare / Beesline Natural Sensitive Zone Whitening Creams 50ml</td></tr>
  <tr><th>Product Type</th><td>Natural Lumiskin & Propolis Intimate Skin Whitening Cream (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Intimate Skin Types (Including Sensitive & Dry Skin)</td></tr>
  <tr><th>Finish</th><td>Touchably soft, brightened, even-toned & odor-protected intimate skin</td></tr>
  <tr><th>Texture</th><td>Smooth velvety fast-absorbing light cream</td></tr>
  <tr><th>Fragrance</th><td>Subtle light natural Beesline aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Lumiskin, Propolis, Coconut Oil, Vitamin C</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Lumiskin Tyrosinase Block & Propolis Antimicrobial Defense</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Whitening Sensitive Zone Cream resolves dark intimate hyperpigmentation, friction discoloration, and post-shaving irritation.</p>

<h3>Why choose Beesline Sensitive Zone Cream?</h3>
<p>Lumiskin inhibits diacylglycerol melanin pathways safely without cell toxicity, while Propolis provides antibacterial defense.</p>"""

    en_faqs = [
        ("What is Beesline Whitening Sensitive Zone Cream - 50ml?", "It is a natural botanical cream formulated with Lumiskin, Propolis, and Coconut Oil to brighten dark intimate skin safely."),
        ("What are the benefits of Lumiskin, Propolis, and Coconut Oil?", "Lumiskin inhibits melanin synthesis, Propolis protects against bacteria, and Coconut Oil hydrates delicate skin."),
        ("Does it brighten dark intimate skin hyperpigmentation safely?", "Yes, clinically proven to fade friction hyperpigmentation and unify sensitive zone skin tone without stinging."),
        ("What volume is contained in this tube?", "It comes in a compact 50ml tube."),
        ("How do I apply it correctly?", "Apply a small amount onto clean, dry external intimate skin, massaging gently twice daily."),
        ("Is it 100% free of hydroquinone, parabens, and alcohol?", "Yes, 100% natural formula free of hydroquinone, parabens, and alcohol."),
        ("Where is Beesline Sensitive Zone Cream manufactured?", "Proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Is it safe for extremely sensitive skin?", "Yes, dermatologically tested soothing formula safe for sensitive intimate skin."),
        ("What scent does Beesline Sensitive Zone Cream have?", "Features a light, pleasant natural subtle fragrance."),
        ("Does it absorb quickly without grease?", "Yes, weightless velvety matrix absorbs instantly leaving zero greasy residue."),
        ("Is the 50ml tube economical for daily use?", "Yes, compact tube lasts through weeks of continuous daily intimate care."),
        ("How should I store the tube?", "Store in a cool, dry place away from direct heat."),
        ("Does it prevent irritation and bad odors?", "Yes, Propolis purifies bacteria to prevent irritation and bad odors."),
        ("Is the tube cap leak-proof?", "Yes, comes with a secure screw-top cap."),
        ("How many times daily should I use it?", "Recommended for use twice daily, morning and evening."),
        ("Is it suitable for men and women?", "Suitable for adults, both men and women aged 12+."),
        ("Does it prevent dark spot recurrence?", "Yes, regular use inhibits melanin overproduction to prevent spot recurrence."),
        ("Is it Beesline's #1 sensitive zone whitening cream?", "Yes, Whitening Sensitive Zone Cream is the #1 iconic intimate cream by Beesline."),
        ("Does it deliver complete intimate confidence?", "Yes, guarantees complete skin clarity, softness, and intimate confidence."),
        ("Is the tube recyclable?", "Yes, 100% recyclable environmentally friendly tube."),
        ("Does it soften dry skin patches?", "Yes, deeply hydrates and smooths dry delicate intimate skin patches."),
        ("Does it leave skin touchably soft?", "Yes, leaves intimate skin touchably soft, smooth, and supple."),
        ("Is it safe for continuous daily use?", "Yes, 100% natural botanical formula completely safe for daily use."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1876",
        "sku": "EK-1876",
        "gtin": "5281018003145",
        "category": "العناية الشخصية / كريمات بيزلين الطبية لتفتيح وتلطيف المناطق الحساسة 50ml",
        "brand": "Beesline",
        "ar": {
            "title": "كريم تفتيح المنطقة الحساسة من بيزلين50مل",
            "meta_title": "كريم تفتيح المنطقة الحساسة بيزلين 50مل | إكليل أبها",
            "meta_description": "اشتري كريم تفتيح المنطقة الحساسة من بيزلين (50 مل). كريم طبيعي باللوميسكين وصمغ النحل لتفتيح وتلطيف المناطق الحساسة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بيزلين", "تفتيح_المنطقة_الحساسة", "كريم_بيزلين", "عناية_المناطق_الحساسة", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Whitening Sensitive Zone Cream - 50ml",
            "meta_title": "Beesline Whitening Sensitive Zone Cream 50ml | Ekleel Abha",
            "meta_description": "Buy original Beesline Whitening Sensitive Zone Cream (50ml). Natural Lumiskin & Propolis intimate skin whitening cream. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["beesline", "sensitive_zone_cream", "whitening_cream", "intimate_care", "ekleel_abha"]
        },
        "schema": {
            "brand": "Beesline",
            "category": "Personal Care / Sensitive Zone Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "beesline-whitening-sensitive-zone-cream-50ml.webp",
            "alt": "Beesline Whitening Sensitive Zone Cream 50ml",
            "title": "Beesline Whitening Sensitive Zone Cream 50ml"
        }
    }

def create_product_1877():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مزيل عرق مدعم بالفضة للرجال من بيزلين 50 مل (Beesline Silver-Infused Deodorant for Men - 50ml)</strong> مزيل العرق الطبيعي الرول اون المصمم خصيصاً للرجال لتوفير أقصى جفاف تام وحماية مضادة للبكتيريا والروائح الكريهة لـ 48 ساعة. يرتكز هذا الرول اون الفاخر من بيزلين للرجال (Beesline Silver-Infused Men Roll-On Deodorant 50ml) على تكنولوجيا الفضة النانوية المضادة للبكتيريا (Silver Ions)، صمغ النحل النقي (Propolis)، وحجر الشبة الطبيعي.</p>
<p>يعمل مزيل عرق بيزلين بالفضة للرجال على للقضاء على البكتيريا المسببة للروائح الحادة أثناء المجهود الرياضي، امتصاص العرق الزائد، وتفتيح اسمرار الإبطين الناتجة عن الاحتكاك، ليترك منطقة الإبطين لدى الرجل جافة، معطرة بنفحات رجالية فواحة، ومحمية طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية قصوى بالفضة المضادة للبكتيريا لـ 48 ساعة:</strong> تقضي أيونات الفضة على البكتيريا المسببة لرائحة العرق.</li>
  <li><strong>جفاف تام وتفتيح آمن لإبطين الرجل:</strong> يمتص الرطوبة الزائدة ويفتح الاسمرار الناتج عن الاحتكاك.</li>
  <li><strong>تطهير وتهدئة بـ صمغ النحل النقي (Propolis):</strong> يهدئ البشرة بعد الحلاقة ويحمي من الالتهابات.</li>
  <li><strong>خالي 100% من ألومنيوم كلوروهيدرات، الكحول، والبارابين:</strong> لا يسد المسام ولا يسبب حساسية البشرة.</li>
  <li><strong>عطر رجالي فواح يبث الثقة والنشاط:</strong> يمنح شعوراً بالحيوية والانتعاش الرياضي طوال اليوم.</li>
  <li><strong>عبوة مدمجة سعة 50 مل:</strong> حجم ممتازة ومناسب للحقيبة الرياضية والعمل والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> نظفي أو نظف منطقة الإبطين بالماء والصابون وجففها جيداً قبل الاستعمال.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> مرر البكرة الدوارة لمزيل عرق بيزلين بالفضة 1-2 مرة على بشرة الإبط الجافة.</li>
  <li><strong>الخطوة الثالثة (التجفيف):</strong> دع السائل يجف لثوانٍ معدودة قبل ارتداء الملابس (يُستعمل مرة يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>أيونات الفضة النانوية وصمغ النحل (Silver Ions & Propolis):</strong> يقضيان على البكتيريا ويهدئان الجلد.</li>
  <li><strong>حجر الشبة الطبيعي واللوميسكين:</strong> يمتصان العرق ويفتحان التصبغات الجلديّة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الإبطين للرجال فقط.</li>
  <li>لا يوضع على الجلد المصاب بجروح مفتوحة أو التهابات شديدة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل رجل يبحث عن مزيل عرق بيزلين المدعم بالفضة 50 مل لحماية قصوى من العرق والروائح وتفتيح الإبطين.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين للرجال (Beesline Men)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / مزيلات العرق الرول اون بالفضة المخصصة للرجال 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>مزيل عرق رول اون رجالي بالفضة النانوية وجفاف تام 48 ساعة (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الإبطين للرجال (بما في ذلك البشرة الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>إبطين جافين تماماً، معطرين بعطر رجالي فواح وخاليين من الروائح والتصبغات</td></tr>
  <tr><th>الملمس</th><td>سائل رول اون خفيف ينفذ فورياً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر رجالي فواح ومنشط (Men Fresh Scent)</td></tr>
  <tr><th>المكونات النشطة</th><td>أيونات الفضة، صمغ النحل (Propolis)، حجر الشبة، لوميسكين</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>الرجال والشباب (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد أيوّنات الفضة في بيزلين للرجال (Beesline Men Silver)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مزيل عرق بيزلين بالفضة للرجال مشكلة رائحة العرق الحادة أثناء التمارين، العرق المفرط، واسمرار الإبطين.</p>

<h3>لماذا تنجح تقنية أيونات الفضة (Silver Ions)؟</h3>
<p>لأن الفضة النانوية تمزق الجدار الخلوي لبكتيريا العرق، فتقضي على الروائح فورياً دون الحاجة لكيميائيات ضارة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على بشرة جافة فور الاستحمام:</strong> ضع الرول اون على إبطين جافين ونظيفين.<br>
2. <strong>الاستخدام قبل الجيم:</strong> استعمله قبل التمارين الرياضية لمنع تكون الروائح الحادة.<br>
3. <strong>الانتظار ثوانٍ قبل اللبس:</strong> دع السائل يجف لتفادي التلطخ بالملابس.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "أيونات الفضة بمزيلات العرق تضر الجلد وتسبب تسمماً."<br>
<strong>الحقيقة:</strong> الفضة النانوية بمزيل بيزلين آمنة ومجربة طبياً لتقييد البكتيريا السطحية فقط.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>ترتبط أيونات Ag+ ببروتينات إنزيم البكتيريا (Corynebacteria)، فتعطل أيض الكبريت المسبب للرائحة الحادة.</p>"""

    faqs = [
        ("ما هو مزيل عرق مدعم بالفضة للرجال من بيزلين 50 مل؟", "هو مزيل عرق رول اون طبيعي للرجال بالفضة النانوية وصمغ النحل لحماية 48 ساعة من العرق والروائح وتفتيح الإبط 50 مل."),
        ("ما هي فوائد أيونات الفضة وصمغ النحل وحجر الشبة؟", "تقضي الفضة على البكتيريا، يمتص حجر الشبة العرق، ويفتّح اللوميسكين تصبغات الإبط لدى الرجال."),
        ("هل يوفر حماية قصوى من العرق والروائح أثناء الرياضة؟", "نعم، مثبت سريرياً في القضاء على البكتيريا وتوفير جفاف تام لـ 48 ساعة أثناء المجهود البدني."),
        ("ما حجم العبوة؟", "تأتي لعلبة رول اون رجالية سعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "مرر البكرة 1-2 مرة على بشرة الإبط النظيفة والجافة، دع السائل يجف ثوانٍ قبل ارتداء الملابس يومياً."),
        ("هل هو خالي 100% من ألومنيوم كلوروهيدرات والبارابين والكحول؟", "نعم، خالي 100% من ألومنيوم كلوروهيدرات والكحول والبارابين ومناسب للبشرة الحساسة."),
        ("ما هو بلد صنع مزيل عرق بيزلين للرجال؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين العالمية (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يترك أثراً أو بقعاً على الملابس الرياضية؟", "لا، قوام شفاف ينفذ فورياً دون ترك أي أثر على الملابس."),
        ("ما هي رائحة مزيل عرق بيزلين بالفضة للرجال؟", "يتميز برائحة رجالية فواحة ومنشطة تبث الثقة."),
        ("هل يهدئ تهيج الإبطين لدى الرجال؟", "نعم، صمغ النحل والألوفيرا يهدئان التهابات البشرة بعد الحلاقة."),
        ("هل عبوة الرول اون 50 مل مناسبة للحقيبة الرياضية؟", "نعم، حجم مدمج وأنيق مثالي للحقيبة الرياضية والعمل والسفر."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعبوتها المغلقة محكماً."),
        ("هل يناسب جميع الرجال والشباب؟", "مناسب للبالغين والشباب من سن 12 سنة فما فوق."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة رول اون أنيقة بغطاء محكم الحماية."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل مرة واحدة يومياً صباحاً أو قبل التمارين."),
        ("هل يمنع تكاثر البكتيريا المسببة للرائحة؟", "نعم، أيونات الفضة تقضي على البكتيريا المحللة للعرق."),
        ("هل يناسب البشرة الحساسة؟", "نعم، فورمولا خالية من المواد القاسية وآمنة للبشرة الحساسة."),
        ("هل هو مزيل العرق الرجالي الأكثر طلباً لبيزلين؟", "نعم، Beesline Silver Men Roll-On المزيل الرجالي الأول والأكثر مبيعاً."),
        ("هل يمنح حس ثقة وجفاف طوال اليوم؟", "نعم، يضمن جفافاً وانتعاشاً ورائحة فواحة طوال اليوم."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يمنع اسمرار الإبطين لدى الرجال؟", "نعم، اللوميسكين يفتح التصبغات ويمنع الاسمرار المستقبلي."),
        ("هل يترك الجلد طرياً؟", "نعم، يترك جلد الإبطين طرياً ومسترخياً."),
        ("هل يجف سريعاً على البشرة؟", "نعم، يجف السائل خلال ثوانٍ معدودة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Silver-Infused Deodorant for Men - 50ml</strong> (Beesline Silver-Infused Men Roll-On Deodorant) is the clinical natural roll-on deodorant engineered specifically for men to provide maximum 48-hour total dryness, antibacterial defense, and safe underarm whitening. Formulated by Beesline, it blends Silver Ions, Propolis, and natural Alum Rock.</p>
<p>Beesline Silver Men Deodorant eliminates odor-causing bacteria during intense physical activity, absorbs excess sweat moisture, and lightens underarm hyperpigmentation caused by friction, leaving a man's underarms touchably dry, freshly fragranced with a masculine scent, and protected all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Maximum 48-Hour Silver Antibacterial Protection:</strong> Silver Ions eliminate odor-causing bacteria instantly.</li>
  <li><strong>Total Dryness & Safe Underarm Whitening for Men:</strong> Absorbs excess sweat moisture and fades dark friction spots.</li>
  <li><strong>Purifying Propolis Defense:</strong> Soothes post-shaving irritation and protects against inflammation.</li>
  <li><strong>100% Free of Aluminum Chlorohydrate, Alcohol & Parabens:</strong> Does not clog pores or cause skin irritation.</li>
  <li><strong>Invigorating Masculine Fresh Scent:</strong> Delivers long-lasting freshness and athletic energy.</li>
  <li><strong>Compact 50ml Roll-On Bottle:</strong> Ideal gym bag and travel size for daily continuous freshness.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse underarm skin thoroughly with soap and water and pat dry before application.</li>
  <li><strong>Step 2 (Apply):</strong> Roll the Beesline Silver applicator 1 to 2 times over clean, dry underarm skin.</li>
  <li><strong>Step 3 (Dry):</strong> Allow fluid to dry for a few seconds before dressing (use once daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Nano Silver Ions & Propolis:</strong> Eliminate odor-causing bacteria and soothe underarm dermal tissue.</li>
  <li><strong>Natural Alum Rock & Lumiskin:</strong> Absorb sweat moisture and fade dark underarm hyperpigmentation spots.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical dry male underarm skin application only.</li>
  <li>Do not apply onto open wounds or severely broken skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Men seeking Beesline's 50ml Silver-Infused Roll-On Deodorant for maximum sweat defense, fresh scent, and underarm whitening.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline Men (Beesline)</td></tr>
  <tr><th>Category</th><td>Personal Care / Beesline Silver-Infused Men Roll-On Deodorants 50ml</td></tr>
  <tr><th>Product Type</th><td>48-Hour Silver Antibacterial Total Dryness Men Roll-On Deodorant (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Male Underarm Skin Types (Including Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Touchably dry, brightened, odor-free & clean male armpits</td></tr>
  <tr><th>Texture</th><td>Smooth lightweight fast-drying roll-on fluid</td></tr>
  <tr><th>Fragrance</th><td>Invigorating fresh masculine scent</td></tr>
  <tr><th>Active Ingredients</th><td>Silver Ions, Propolis, Alum Rock, Lumiskin</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>Teens & Adult Men (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Nano Silver Ion Antibacterial Disruption & Alum Absorption</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Silver Men Deodorant resolves heavy workout perspiration, strong male body odor, and friction underarm dark spots.</p>

<h3>Why choose Beesline Silver-Infused Men Deodorant?</h3>
<p>Nano Silver Ions disrupt Corynebacteria cell walls to halt odor instantly, while Alum Rock absorbs sweat without aluminum chlorohydrate toxicity.</p>"""

    en_faqs = [
        ("What is Beesline Silver-Infused Deodorant for Men - 50ml?", "It is a natural men's roll-on deodorant formulated with Silver Ions, Propolis, and Alum Rock to deliver 48-hour total dryness and underarm whitening."),
        ("What are the benefits of Silver Ions, Propolis, and Alum Rock?", "Silver Ions eliminate bacteria, Alum Rock absorbs sweat moisture, and Lumiskin brightens dark male underarm spots."),
        ("Does it deliver maximum 48-hour sweat defense during workouts?", "Yes, clinically proven to eliminate odor-causing bacteria and provide total dryness during intense physical activity."),
        ("What volume is contained in this roll-on bottle?", "It comes in a compact 50ml men's roll-on bottle."),
        ("How do I apply it correctly?", "Roll 1-2 times onto clean, dry male underarm skin, allow to dry for a few seconds, and dress."),
        ("Is it 100% free of aluminum chlorohydrate, alcohol, and parabens?", "Yes, 100% free of aluminum chlorohydrate, alcohol, and parabens; safe for sensitive skin."),
        ("Where is Beesline Silver Men Deodorant manufactured?", "Proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it leave white marks or yellow stains on gym clothes?", "No, invisible fluid absorbs instantly without leaving marks on workout apparel."),
        ("What scent does Beesline Silver Men Deodorant have?", "Features an invigorating, fresh masculine fragrance."),
        ("Does it soothe post-shaving underarm irritation?", "Yes, enriched with Propolis and Aloe Vera to calm male skin irritation after shaving."),
        ("Is the 50ml roll-on gym-bag friendly?", "Yes, compact roll-on bottle fits easily into gym bags, work totes, and travel kits."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Is it suitable for men and teens?", "Suitable for teens and adult men aged 12+."),
        ("Is the roll-on bottle leak-proof?", "Yes, features a secure screw-top cap over the smooth roller ball."),
        ("How many times daily should I use it?", "Recommended for use once daily, morning or post-workout."),
        ("Does it stop odor-causing bacteria growth?", "Yes, Silver Ions destroy odor-causing bacteria on contact."),
        ("Is it safe for sensitive male underarm skin?", "Yes, gentle formula free of harsh chemicals; safe for sensitive skin."),
        ("Is it Beesline's #1 men's roll-on deodorant?", "Yes, Silver-Infused Men Roll-On is the #1 flagship male deodorant by Beesline."),
        ("Does it provide all-day masculine freshness confidence?", "Yes, guarantees complete dryness, fresh masculine scent, and brightened armpits."),
        ("Is the bottle recyclable?", "Yes, 100% recyclable environmentally friendly bottle."),
        ("Does it prevent underarm friction darkening in men?", "Yes, Lumiskin brightens existing dark spots and prevents future friction darkening."),
        ("Does it leave underarm skin touchably soft?", "Yes, leaves male underarm skin touchably soft, smooth, and dry."),
        ("Does it dry quickly on skin?", "Yes, fluid dries in seconds for immediate dressing."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1877",
        "sku": "EK-1877",
        "gtin": "5281018088234",
        "category": "العناية الشخصية / مزيلات العرق الرول اون بالفضة المخصصة للرجال 50ml",
        "brand": "Beesline Men",
        "ar": {
            "title": "مزيل عرق مدعم بالفضة للرجال من بيزلين 50 مل",
            "meta_title": "مزيل عرق بيزلين بالفضة للرجال 50مل | إكليل أبها",
            "meta_description": "اشتري مزيل عرق مدعم بالفضة للرجال من بيزلين (50 مل). رول اون رجالي بالفضة النانوية لجفاف تام وتفتيح وتطهير 48 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بيزلين_للرجال", "مزيل_عرق_رجالي", "مزيل_عرق_بالفضة", "جفاف_تام", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Silver-Infused Deodorant for Men - 50ml",
            "meta_title": "Beesline Silver Deodorant for Men 50ml | Ekleel Abha",
            "meta_description": "Buy original Beesline Silver-Infused Deodorant for Men (50ml). Nano Silver 48-hour total dry whitening men roll-on. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["beesline_men", "silver_deodorant", "men_deodorant", "total_dry", "ekleel_abha"]
        },
        "schema": {
            "brand": "Beesline Men",
            "category": "Personal Care / Men Deodorant",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "beesline-silver-infused-deodorant-for-men-50ml.webp",
            "alt": "Beesline Silver Infused Deodorant for Men 50ml",
            "title": "Beesline Silver Infused Deodorant for Men 50ml"
        }
    }

def create_product_1878():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مزيل عرق رول اون ديو برائحة سبورت بلس من بيزلين 50 مل (Beesline Deo Roll-On Sport Pulse - 50 ml)</strong> مزيل العرق المنشط الطبيعي الأحدث المخصص للرياضيين والأنشطة المكثفة لتأمين حماية مضادة للعرق والروائح لـ 48 ساعة وتفتيح آمن لإبطين. يرتكز هذا الرول اون الفاخر من بيزلين (Beesline Whitening Roll-On Sport Pulse 50ml) على تكنولوجيا الشبة الطبيعية (Alum Rock)، صمغ النحل النقي (Propolis)، واللوميسكين المبيض بنكهة سبورت بلس الرياضية المنعشة.</p>
<p>يعمل مزيل عرق بيزلين سبورت بلس على إعطاء دفقة حيوية منعشة أثناء الحركة، القضاء على البكتيريا المسببة للرائحة الحادة، وتفتيح اسمرار الإبطين الناتجة عن الحركة والرياضة، ليترك منطقة الإبط جافة، ناصعة، ومحمية بعطر رياضي فواح طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية رياضية فائقة وجفاف تام لـ 48 ساعة:</strong> يمتص العرق المفرط أثناء الحركة والتمارين.</li>
  <li><strong>تفتيح وتوحيد لون بشرة الإبطين باللوميسكين:</strong> يزيل التصبغات الداكنة الناتجة عن الاحتكاك الرياضي.</li>
  <li><strong>عطر سبورت بلس (Sport Pulse) المنشط:</strong> يمنح دفعة حيوية وإحساساً بالانتعاش الرياضي الدائم.</li>
  <li><strong>تطهير وتهدئة بـ صمغ النحل النقي (Propolis):</strong> يهدئ البشرة المتهيجة ويدعم دفاع الإبطين.</li>
  <li><strong>خالي 100% من ألومنيوم كلوروهيدرات، الكحول، والبارابين:</strong> لا يسد المسام ولا يسبب حساسية البشرة.</li>
  <li><strong>عبوة مدمجة سعة 50 مل:</strong> حجم ممتازة ومناسب للحقيبة الرياضية والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> نظفي أو نظف منطقة الإبطين بالماء والصابون وجففها جيداً.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> مرر البكرة الدوارة لمزيل عرق بيزلين سبورت بلس 1-2 مرة على بشرة الإبط الجافة.</li>
  <li><strong>الخطوة الثالثة (التجفيف):</strong> دع السائل يجف لثوانٍ معدودة قبل ارتداء الملابس (يُستعمل يومياً قبل أو بعد الرياضة).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مركب سبورت بلس وحجر الشبة (Sport Pulse & Alum Rock):</strong> يمتصان العرق ويعطيان انتعاشاً حيوياً.</li>
  <li><strong>صمغ النحل واللوميسكين المبيض:</strong> يهدئان أنسجة الجلد ويفتحان البقع التصبغية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الإبطين الجافة فقط.</li>
  <li>لا يوضع على الجلد المصاب بجروح مفتوحة أو التهابات شديدة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يمارس الرياضة ويبحث عن رول اون بيزلين سبورت بلس 50 مل للانتعاش التام وتفتيح الإبطين.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / مزيلات العرق الرول اون الرياضية المبيضة 50ml</td></tr>
  <tr><th>نوع المنتج</th><td>مزيل عرق رول اون رياضي مبيض ومؤمن للجفاف لـ 48 ساعة (50ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الإبطين (بما في ذلك البشرة الرياضية والحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>إبطين جافين تماماً، ناصعين، معطرين بعطر سبورت بلس الرياضي ومحميين</td></tr>
  <tr><th>الملمس</th><td>سائل رول اون خفيف ينفذ فورياً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر سبورت بلس (Sport Pulse) الرياضي المنشط</td></tr>
  <tr><th>المكونات النشطة</th><td>حجر الشبة، صمغ النحل، لوميسكين، معطر سبورت بلس</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية للرجال والنساء (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد سبورت بلس واللوميسكين في بيزلين ديو (Beesline Sport Pulse)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مزيل عرق بيزلين سبورت بلس مشكلة العرق الرياضي المفرط، رائحة العرق الناتجة عن الجيم، واسمرار الإبطين.</p>

<h3>لماذا تنجح تركيبة سبورت بلس المبيضة؟</h3>
<p>لأن المعطر الرياضي المنشط يحيّد جزيئات الرائحة فورياً، بينما يمتص حجر الشبة العرق ويفتّح اللوميسكين البقع.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق قبل التمارين الرياضية:</strong> ضعه فور الاستحمام وقبل الذهاب للجيم.<br>
2. <strong>تجفيف الإبطين جيداً:</strong> تأكد من جفاف الجلد قبل دحرجة البكرة الدوارة.<br>
3. <strong>ارتداء ملابس رياضية مسامية:</strong> يساعد على تجديد هواء الإبطين وحفظ الجفاف.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مزيلات العرق الرياضية تحتوي على مواد كيميائية حادة تسبب اسمرار الإبطين."<br>
<strong>الحقيقة:</strong> رول اون بيزلين سبورت بلس طبيعي 100% وخالي من الألومنيوم الضار ويفتّح الإبطين ب أمان.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبت أملاح حجر الشبة الطبيعية قطرات العرق بالطبقة السطحية، في حين تمنع الفلافونويدات تكون البكتيريا المسببة للرائحة.</p>"""

    faqs = [
        ("ما هو مزيل عرق رول اون ديو برائحة سبورت بلس من بيزلين 50 مل؟", "هو مزيل عرق رول اون رياضي من بيزلين بحماية 48 ساعة وعطر سبورت بلس المنشط لتفتيح الإبطين وجفاف تام 50 مل."),
        ("ما هي فوائد عطر سبورت بلس وحجر الشبة واللوميسكين؟", "يمنح عطر سبورت بلس نشاطاً وحيوية، يمتص حجر الشبة العرق، ويفتّح اللوميسكين تصبغات الإبطين."),
        ("هل يمنح جفافاً وتفتيحاً لـ 48 ساعة أثناء التمارين؟", "نعم، مثبت سريرياً في تأمين جفاف تام وتفتيح التصبغات لـ 48 ساعة أثناء الحركة والرياضة."),
        ("ما حجم العبوة؟", "تأتي لعلبة رول اون بكرة دوارة سعة 50 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "مرر البكرة 1-2 مرة على بشرة الإبط النظيفة والجافة، دع السائل يجف ثوانٍ قبل ارتداء الملابس يومياً."),
        ("هل هو خالي 100% من ألومنيوم كلوروهيدرات والبارابين والكحول؟", "نعم، خالي 100% من ألومنيوم كلوروهيدرات والكحول والبارابين وآمن للبشرة الحساسة."),
        ("ما هو بلد صنع مزيل عرق بيزلين سبورت بلس؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين العالمية (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يترك أثراً أو بقعاً على الملابس الرياضية؟", "لا، قوام شفاف ينفذ فورياً دون ترك أي أثر على الملابس."),
        ("ما هي رائحة مزيل عرق بيزلين سبورت بلس؟", "يتميز برائحة سبورت بلس الرياضية المنشطة والحيوية."),
        ("هل يهدئ تهيج الإبطين بعد الحلاقة والرياضة؟", "نعم، صمغ النحل والألوفيرا يهدئان التهابات البشرة بعد التمارين والحلاقة."),
        ("هل عبوة الرول اون 50 مل مناسبة لحقيبة الجيم؟", "نعم، حجم مدمج وأنيق مثالي لحقيبة الجيم والعمل والسفر."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعبوتها المغلقة محكماً."),
        ("هل يناسب الرجال والنساء؟", "مناسب لجميع الفئات العمرية للنساء والرجال من سن 12 سنة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة رول اون أنيقة بغطاء محكم الحماية."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل مرة واحدة يومياً صباحاً أو قبل التمارين."),
        ("هل يمنع تكاثر البكتيريا المسببة للرائحة الرياضية؟", "نعم، صمغ النحل وحجر الشبة يمنعان نمو البكتيريا المحللة للعرق."),
        ("هل يناسب البشرة الحساسة؟", "نعم، فورمولا خالية من المواد القاسية وآمنة للبشرة الحساسة."),
        ("هل هو رول اون بيزلين الرياضي الأكثر طلباً؟", "نعم، Whitening Deo Roll-On Sport Pulse المزيل الرياضي الأول لبيزلين."),
        ("هل يمنح حس نشاط وحيوية طوال اليوم؟", "نعم، يضمن جفافاً ونشاطاً وإبطين ناصعين طوال اليوم."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يمنع اسمرار الإبطين الناتج عن الاحتكاك الرياضي؟", "نعم، اللوميسكين يفتح التصبغات ويمنع الاسمرار المستقبلي."),
        ("هل يترك الجلد طرياً؟", "نعم، يترك جلد الإبطين طرياً ومسترخياً."),
        ("هل يجف سريعاً على البشرة؟", "نعم، يجف السائل خلال ثوانٍ معدودة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Deo Roll-On Sport Pulse - 50 ml</strong> (Beesline Whitening Roll-On Sport Pulse 50ml) is the clinical athletic roll-on deodorant engineered for active individuals to provide 48-hour total dryness, invigorated fresh scent, and safe underarm whitening. Formulated by Beesline, it features natural Alum Rock, antibacterial Propolis, and Lumiskin with a vibrant Sport Pulse aroma.</p>
<p>Beesline Sport Pulse Deodorant delivers an invigorating burst of energy during physical workouts, neutralizes athletic body odor, and lightens underarm hyperpigmentation caused by movement, leaving your armpits touchably dry, brightened, and protected all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>48-Hour Athletic Dryness & Anti-Odor Shield:</strong> Absorbs heavy sweat moisture during exercise.</li>
  <li><strong>Safe Underarm Whitening with Lumiskin:</strong> Fades dark friction hyperpigmentation spots.</li>
  <li><strong>Invigorating Sport Pulse Fresh Aroma:</strong> Delivers long-lasting athletic energy and freshness confidence.</li>
  <li><strong>Purifying Propolis Defense:</strong> Soothes post-workout skin irritation and protects against bacteria.</li>
  <li><strong>100% Free of Aluminum Chlorohydrate, Alcohol & Parabens:</strong> Does not clog pores or cause skin irritation.</li>
  <li><strong>Compact 50ml Roll-On Bottle:</strong> Ideal gym bag and travel size for continuous daily freshness.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Cleanse underarm skin thoroughly with soap and water and pat dry before application.</li>
  <li><strong>Step 2 (Apply):</strong> Roll the Beesline Sport Pulse applicator 1 to 2 times over clean, dry underarm skin.</li>
  <li><strong>Step 3 (Dry):</strong> Allow fluid to dry for a few seconds before dressing (use once daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Sport Pulse Actives & Alum Rock:</strong> Neutralize odor-causing bacteria and absorb sweat moisture during workouts.</li>
  <li><strong>Propolis & Lumiskin:</strong> Soothe underarm dermal tissue and fade dark hyperpigmentation spots.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical dry underarm skin application only.</li>
  <li>Do not apply onto open wounds or severely broken skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Active individuals seeking Beesline's 50ml Sport Pulse Whitening Roll-On Deodorant for total dryness and fresh scent.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Personal Care / Beesline Athletic Whitening Roll-On Deodorants 50ml</td></tr>
  <tr><th>Product Type</th><td>48-Hour Total Dryness & Whitening Sport Pulse Roll-On Deodorant (50ml)</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Underarm Skin Types (Including Athletic & Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Touchably dry, brightened, odor-free & clean armpits</td></tr>
  <tr><th>Texture</th><td>Smooth lightweight fast-drying roll-on fluid</td></tr>
  <tr><th>Fragrance</th><td>Invigorating fresh Sport Pulse aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Alum Rock, Propolis, Lumiskin, Sport Pulse Fragrance</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Sport Pulse Odor Neutralization & Lumiskin Whitening</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Deo Roll-On Sport Pulse resolves heavy exercise perspiration, gym body odor, and friction underarm dark spots.</p>

<h3>Why choose Beesline Sport Pulse Roll-On?</h3>
<p>Vibrant Sport Pulse actives neutralize volatile sulfur compounds, while Alum Rock absorbs sweat without aluminum toxicity.</p>"""

    en_faqs = [
        ("What is Beesline Deo Roll-On Sport Pulse - 50 ml?", "It is an athletic roll-on deodorant formulated with Alum Rock, Propolis, and Lumiskin to deliver 48-hour total dryness and underarm whitening."),
        ("What are the benefits of Sport Pulse aroma, Alum Rock, and Lumiskin?", "Sport Pulse aroma imparts athletic freshness, Alum Rock absorbs sweat moisture, and Lumiskin brightens dark underarm spots."),
        ("Does it deliver 48-hour athletic dryness and underarm whitening?", "Yes, clinically proven to provide 48-hour total dryness and visible underarm skin brightening during exercise."),
        ("What volume is contained in this roll-on bottle?", "It comes in a compact 50ml roll-on bottle."),
        ("How do I apply it correctly?", "Roll 1-2 times onto clean, dry underarm skin, allow to dry for a few seconds, and dress."),
        ("Is it 100% free of aluminum chlorohydrate, alcohol, and parabens?", "Yes, 100% free of aluminum chlorohydrate, alcohol, and parabens; safe for sensitive skin."),
        ("Where is Beesline Sport Pulse Deodorant manufactured?", "Proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it leave white marks or yellow stains on gym clothes?", "No, invisible fluid absorbs instantly without leaving marks on workout apparel."),
        ("What scent does Beesline Sport Pulse Deodorant have?", "Features an invigorating, fresh athletic Sport Pulse fragrance."),
        ("Does it soothe post-workout underarm irritation?", "Yes, enriched with Propolis and Aloe Vera to calm irritation after exercise."),
        ("Is the 50ml roll-on gym-bag friendly?", "Yes, compact roll-on bottle fits easily into gym bags, work totes, and travel kits."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Is it suitable for men and women?", "Suitable for all age groups, both men and women aged 12+."),
        ("Is the roll-on bottle leak-proof?", "Yes, features a secure screw-top cap over the smooth roller ball."),
        ("How many times daily should I use it?", "Recommended for use once daily, morning or post-workout."),
        ("Does it stop odor-causing bacteria growth?", "Yes, Propolis and Alum Rock destroy odor-causing bacteria on contact."),
        ("Is it safe for sensitive underarm skin?", "Yes, gentle formula free of harsh chemicals; safe for sensitive skin."),
        ("Is it Beesline's #1 athletic roll-on deodorant?", "Yes, Whitening Deo Roll-On Sport Pulse is the #1 athletic deodorant by Beesline."),
        ("Does it provide all-day athletic freshness confidence?", "Yes, guarantees complete dryness, fresh athletic scent, and brightened armpits."),
        ("Is the bottle recyclable?", "Yes, 100% recyclable environmentally friendly bottle."),
        ("Does it prevent underarm friction darkening during exercise?", "Yes, Lumiskin brightens existing dark spots and prevents future friction darkening."),
        ("Does it leave underarm skin touchably soft?", "Yes, leaves underarm skin touchably soft, smooth, and dry."),
        ("Does it dry quickly on skin?", "Yes, fluid dries in seconds for immediate dressing."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1878",
        "sku": "EK-1878",
        "gtin": "5281018003893",
        "category": "العناية الشخصية / مزيلات العرق الرول اون الرياضية المبيضة 50ml",
        "brand": "Beesline",
        "ar": {
            "title": "مزيل عرق  رول اون ديو برائحة سبورت بلس من بيزلين 50 مل",
            "meta_title": "مزيل عرق بيزلين سبورت بلس 50مل | إكليل أبها",
            "meta_description": "اشتري مزيل عرق رول اون ديو برائحة سبورت بلس من بيزلين (50 مل). رول اون رياضي بالشبة واللوميسكين لجفاف تام وتفتيح الإبطين 48 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بيزلين", "مزيل_عرق_بيزلين", "سبورت_بلس", "تفتيح_الإبط", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Deo Roll-On Sport Pulse - 50 ml",
            "meta_title": "Beesline Deo Roll-On Sport Pulse 50ml | Ekleel Abha",
            "meta_description": "Buy original Beesline Deo Roll-On Sport Pulse (50 ml). Athletic Alum Rock & Lumiskin 48-hour total dry whitening roll-on. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["beesline", "beesline_deodorant", "sport_pulse", "whitening_deodorant", "ekleel_abha"]
        },
        "schema": {
            "brand": "Beesline",
            "category": "Personal Care / Deodorant",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "beesline-deo-roll-on-sport-pulse-50ml.webp",
            "alt": "Beesline Deo Roll On Sport Pulse 50ml",
            "title": "Beesline Deo Roll On Sport Pulse 50ml"
        }
    }

def create_product_1879():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>زيت تسمير ذهبي من بيزلين، 200 مل (Beesline Gold Tanning Oil, 200 ml)</strong> زيت التسمير والبرونز الفاخر الأكثر شهـرة عالمياً لإكساب بشرة الجسم لوناً برونزياً ذهبياً ساحراً وغنياً أثناء التعرض للشمس أو بحر الصيف. يرتكز هذا الزيت الطبيعي من بيزلين (Beesline Gold Sun Tanning Oil 200ml) على خلاصة الجزر الطبيعي (Carrot Extract)، زيت الجوز، شمع النحل النقي (Beeswax)، وغبار الذهب اللامع.</p>
<p>يعمل زيت تسمير بيزلين الذهبي على تحفيز صبغة الميلانين الطبيعية بالجلد، حماية البشرة من التكسر والجفاف الناتج عن أشعة الشمس، وتأمين لمعان ذهبي مبهر برائحة جوز الهند الطبيعية، ليترك جسمكِ ناعماً كالحرير، مشرقاً ببرونز فاخر، ومحمياً من التقشير طوال الصيف.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>لون برونزي ذهبي غني وسريع (Deep Gold Tan):</strong> يسرع ويكسب الجسم لوناً برونزياً دافئاً وساحراً.</li>
  <li><strong>غني بخلاصة الجزر وشمع النحل وفيتامين E:</strong> يغذي خلايا البشرة ويحميها من الجفاف والتقشر.</li>
  <li><strong>لمعان ذهبي مبهر بغبار الذهب اللامع:</strong> يمنح الجلد بريقاً وتألقاً رائعاً تحت أشعة الشمس.</li>
  <li><strong>حماية طبيعية ضد الأكسدة والتجاعيد:</strong> يحفظ مرونة الجلد ويمنع التشيّخ المبكر من الشمس.</li>
  <li><strong>قوام زيتي غني برائحة جوز الهند الفواحة:</strong> ينفذ بالبشرة بسهولة دون ترك أثر لزج ثقيل.</li>
  <li><strong>عبوة بخاخ سعة 200 مل:</strong> حجم وافر يكفي لموسم الصيف والرحلات البحرية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق):</strong> رشّي كمية سخية من زيت بيزلين الذهبي على بشرة الجسم بالكامل قبل التعرض للشمس.</li>
  <li><strong>الخطوة الثانية (التوزيع):</strong> وزعي الزيت بحركات دائرية ناعمة لضمان تغطية متساوية لكافة أجزاء الجسم.</li>
  <li><strong>الخطوة الثالثة (التكرار):</strong> أعيدي الرش بعد السباحة أو التجفيف بالمنشفة أو عند الحاجة لتسريع التسمير.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة الجزر وشمع النحل (Carrot Extract & Beeswax):</strong> يغنيان صبغة التان ويحفظان الترطيب العميق.</li>
  <li><strong>زيت الجوز وفيتامين E وغبار الذهب:</strong> يمنحون بريقاً ذهبياً ويحمون البشرة من التقشر.</li>
</ul>

<h2>تحذيرات وااحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي لتسمير بشرة الجسم أثناء التعرض للشمس فقط.</li>
  <li>تجنبي ملامسة الزيت المباشرة للعينين ويُنصح باستخدام واقي شمس معتمد إذا كانت البشرة شديدة البياض.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن الحرارة الشديدة.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة ورجل يبحثان عن زيت بيزلين الذهبي للتسمير بـ الجزر وشمع النحل سعة 200 مل للحصول على تان برونزي غني.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / زيوت بيزلين الذهبية لتسمير وتان الجسم بالشمس 200ml</td></tr>
  <tr><th>نوع المنتج</th><td>زيت تسمير طبيعي بالجزر وشمع النحل والذهب للون برونزي غني (200ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>200 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (المستعدة لتسمير الشمس والتان)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم برونزي ذهبي ساحر، لامع، مرطب عميقاً وخالي من التقشر</td></tr>
  <tr><th>الملمس</th><td>زيت ذهبي ناعم ينفذ بالجلد ويعطي بريقاً لامعاً</td></tr>
  <tr><th>العطر</th><td>عطر جوز الهند والجزر الطبيعي الاستوائي</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة الجزر، شمع النحل، زيت الجوز، غبار الذهب، فيتامين E</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 15 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد خلاصة الجزر وشمع النحل في بيزلين للتسمير (Beesline Gold Tanning)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج زيت بيزلين الذهبي للتسمير مشكلة صعوبة الحصول على لون تان برونزي دافئ، تقشر البشرة بعد الشمس، والجفاف.</p>

<h3>لماذا تنجح تركيبة الجزر وشمع النحل للتان؟</h3>
<p>لأن البيتا-كاروتين بالجزر يحفز خلايا الميلاين لإفراز التان البرونزي، بينما يغلف شمع النحل البشرة لحفظ الترطيب.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الرش بشكل متجانس قبل الشمس بـ 15 دقيقة:</strong> وزعي الزيت بالتساوي على كامل الجسم.<br>
2. <strong>إعادة الرش بعد السباحة:</strong> رشي الزيت مجدداً فور الخروج من البحر أو المسبح.<br>
3. <strong>الترطيب بـ الألوفيرا بعد التان:</strong> استعملي لوشن مهدئ بعد التعرض للشمس لحفظ اللون البرونزي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "زيوت التسمير تسبب حرقان وتقشر البشرة دائماً."<br>
<strong>الحقيقة:</strong> زيت بيزلين غني بشمع النحل وفيتامين E لمنع التقشر وتغذية الجلد أثناء التسمير.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخترق الكاروتينويدات الطبقة السطحية لتعزيز الميلانو جينيسيس، بينما يحمي فيتامين E أغشية الخلايا من أكسدة الـ UV.</p>"""

    faqs = [
        ("ما هو زيت تسمير ذهبي من بيزلين، 200 مل؟", "هو زيت تسمير طبيعي من بيزلين بالجزر وشمع النحل والذهب لإكساب الجسم لوناً برونزياً ذهبياً غنياً أثناء التعرض للشمس 200 مل."),
        ("ما هي فوائد خلاصة الجزر وشمع النحل وغبار الذهب؟", "يحفز الجزر صبغة التان، يحفظ شمع النحل الترطيب لمنع التقشر، ويضفي الذهب بريقاً لامعاً."),
        ("هل يمنح لوناً برونزياً ذهبياً غنياً وسريعاً؟", "نعم، مثبت سريرياً في تسريع وتعميق لون التان الذهبي ومنح الجسم إشراقة برونزية."),
        ("ما حجم العبوة البخاخ؟", "تأتي بحجم وافر سعة 200 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "رشي كمية سخية على بشرة الجسم قبل التعرض للشمس، وزعي متساوياً وأعيدي الرش بعد السباحة والتجفيف."),
        ("هل هو مكون من مواد طبيعية ونباتية 100%؟", "نعم، مكونات طبيعية من الجزر وشمع النحل وزيت الجوز خالية من المواد الكيميائية الضارة."),
        ("ما هو بلد صنع زيت بيزلين الذهبي؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين العالمية (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يحمي البشرة من التقشير والجفاف بعد الشمس؟", "نعم، غني بشمع النحل وفيتامين E لمنع جفاف وتقشر البشرة بعد التان."),
        ("ما هي رائحة زيت بيزلين للتسمير؟", "يتميز برائحة جوز الهند والجزر الاستوائية المنعشة والمحببة."),
        ("هل يمنح بريقاً ولمعاناً ذهبياً تحت الشمس؟", "نعم، غبار الذهب اللامع يضفي بريقاً وتألقاً رائعاً للشمس."),
        ("هل العبوة 200 مل مناسبة لموسم الصيف والرحلات؟", "نعم، حجم وافر بمضخة بخاخ مثالي للرحلات البحرية والصيف."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الحرارة الشديدة."),
        ("هل يترك الجلد طرياً ومخملياً؟", "نعم، يترك بشرة الجسم طرية، مشعة، ومخملية."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة بخاخ أنيقة بغطاء محكم الحماية."),
        ("هل يناسب النساء والرجال للتان؟", "مناسب لجميع الفئات العمرية للنساء والرجال من سن 15 سنة."),
        ("كم مرة يُفضل استخدامه أثناء التان؟", "يُستعمل عند الحاجة ويُعاد رشه بعد السباحة والتجفيف."),
        ("هل يناسب جميع أنواع بشرة الجسم؟", "مناسب للبشرة المستعدة للتسمير والتان."),
        ("هل هو زيت التسمير الذهبي الأكثر شهرة لبيزلين؟", "نعم، Gold Tanning Oil الزيت الذهبي الأول والأكثر مبيعاً لبيزلين."),
        ("هل يمنح حس أنوثة وتألق استوائي؟", "نعم، يضمن تألقاً ولوناً برونزياً ساحراً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يساعد في تثبيت لون التان لفترة أطول؟", "نعم، الترطيب بشمع النحل يثبت لون البرونز لأشهر."),
        ("هل يترك ملمساً ناعماً؟", "نعم، يترك أسطح الجلد ناعمة ومشرقة."),
        ("هل يناسب المسبح والبحر؟", "نعم، ممتاز للاستخدام على شواطئ البحر والمسابح."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>- {a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Gold Tanning Oil, 200 ml</strong> (Beesline Gold Sun Tanning Oil 200ml) is the world's iconic natural sun tanning oil engineered to deliver a rich, glamorous golden bronze tan while nourishing body skin under the sun. Formulated by Beesline, it blends natural Carrot extract, Walnut oil, pure Beeswax, and shimmering Gold Dust.</p>
<p>Beesline Gold Tanning Oil accelerates natural melanin pigmentation, protects skin cells from sun-induced dryness and peeling, and imparts a shimmering golden radiance with a tropical coconut scent, leaving your body touchably soft, glowing, and velvety smooth all summer long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Deep Golden Bronze Tan Acceleration:</strong> Accelerates and deepens natural warm bronze skin tanning.</li>
  <li><strong>Enriched with Carrot Extract, Beeswax & Vitamin E:</strong> Nourishes dermal cells and prevents post-sun peeling.</li>
  <li><strong>Shimmering Gold Dust Radiance:</strong> Bestows a luminous golden shimmer under sunlight.</li>
  <li><strong>Natural Antioxidant & Anti-Aging Protection:</strong> Preserves skin elasticity and prevents solar photo-aging.</li>
  <li><strong>Rich Tropical Coconut-Scented Oil Matrix:</strong> Glides smoothly onto skin without heavy sticky weight.</li>
  <li><strong>Generous 200ml Spray Bottle:</strong> High-value spray bottle ideal for summer vacations and beach trips.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Apply):</strong> Spray a generous amount of Beesline Gold Tanning Oil all over body skin before sun exposure.</li>
  <li><strong>Step 2 (Distribute):</strong> Spread evenly in smooth circular motions for uniform full-body sun coverage.</li>
  <li><strong>Step 3 (Reapply):</strong> Reapply after swimming, towel drying, or prolonged sun exposure to accelerate tanning.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Carrot Extract & Pure Beeswax:</strong> Enhance natural bronze melanin pigmentation and seal in deep hydration.</li>
  <li><strong>Walnut Oil, Vitamin E & Gold Dust:</strong> Impart a glowing golden shimmer while shielding skin against peeling.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body sun tanning application only.</li>
  <li>Avoid direct contact with eyes; apply sunscreen if you have fair or sun-sensitive skin.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from extreme heat.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Beesline's 200ml Gold Tanning Oil with Carrot extract and Beeswax for a rich, glowing golden bronze tan.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Skincare / Beesline Gold Sun Tanning Oils 200ml</td></tr>
  <tr><th>Product Type</th><td>Natural Carrot, Beeswax & Gold Shimmer Sun Tanning Oil (200ml)</td></tr>
  <tr><th>Volume/Weight</th><td>200 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Sun-Tanning Ready Skin)</td></tr>
  <tr><th>Finish</th><td>Deeply bronzed, glowing golden, hydrated & peel-free body skin</td></tr>
  <tr><th>Texture</th><td>Smooth golden oil fluid imparting luminous shimmer</td></tr>
  <tr><th>Fragrance</th><td>Tropical Coconut & Carrot natural aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Carrot Extract, Beeswax, Walnut Oil, Gold Dust, Vitamin E</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 15+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Carrot Beta-Carotene Melanogenesis & Beeswax Moisture Barrier</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Gold Tanning Oil resolves pale skin tone, sun-induced dermal peeling, and post-tan skin dryness.</p>

<h3>Why choose Beesline Gold Tanning Oil?</h3>
<p>Beta-carotene accelerates melanocyte melanin production, while pure Beeswax forms a protective barrier preventing skin peeling.</p>"""

    en_faqs = [
        ("What is Beesline Gold Tanning Oil, 200 ml?", "It is a natural sun tanning oil formulated with Carrot extract, Beeswax, and Gold Dust to deliver a deep golden bronze tan."),
        ("What are the benefits of Carrot extract, Beeswax, and Gold Dust?", "Carrot extract accelerates natural tanning, Beeswax locks in deep moisture to prevent peeling, and Gold Dust imparts a shimmer."),
        ("Does it deliver a deep golden bronze tan quickly?", "Yes, clinically proven to accelerate natural melanin production for a rich golden bronze tan."),
        ("What volume is contained in this spray bottle?", "It comes in a generous 200ml spray bottle."),
        ("How do I apply it correctly?", "Spray generously all over body skin before sun exposure, spread evenly, and reapply after swimming or towel drying."),
        ("Is it 100% natural and cruelty-free?", "Yes, 100% natural formula with Carrot extract, Beeswax, and Walnut oil free of harsh chemicals."),
        ("Where is Beesline Gold Tanning Oil manufactured?", "Proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it protect skin from post-sun peeling and dryness?", "Yes, enriched with Beeswax and Vitamin E to nourish dermal cells and prevent peeling after tanning."),
        ("What scent does Beesline Gold Tanning Oil have?", "Features a fresh, tropical natural Coconut and Carrot fragrance."),
        ("Does it impart a luminous golden shimmer under sunlight?", "Yes, shimmering Gold Dust bestows a radiant golden glow under sun rays."),
        ("Is the 200ml bottle ideal for summer vacations?", "Yes, generous 200ml spray bottle lasts through summer beach trips and poolside vacations."),
        ("How should I store the bottle?", "Store in a cool, dry place away from extreme heat."),
        ("Does it leave body skin touchably soft?", "Yes, leaves body skin touchably soft, supple, and glowing."),
        ("Is the spray bottle leak-proof?", "Yes, comes in a sturdy spray bottle with a secure cap."),
        ("Is it suitable for men and women?", "Suitable for teens and adults, both men and women aged 15+."),
        ("How often should I reapply during tanning?", "Reapply as needed, especially after swimming, sweating, or towel drying."),
        ("Is it suitable for all skin types ready for tanning?", "Ideal for all body skin types ready for sun exposure."),
        ("Is it Beesline's #1 gold tanning oil?", "Yes, Gold Sun Tanning Oil is the #1 flagship tanning product by Beesline."),
        ("Does it deliver tropical beach bronze confidence?", "Yes, guarantees a rich golden tan, radiant shimmer, and soft skin confidence."),
        ("Is the bottle recyclable?", "Yes, 100% recyclable environmentally friendly bottle."),
        ("Does it help lock in bronze tan color longer?", "Yes, deep Beeswax hydration seals in bronze tan color for months."),
        ("Does it leave body skin feeling smooth?", "Yes, leaves body skin touchably smooth and glowing."),
        ("Is it great for beach and pool use?", "Yes, perfect for sunbathing at beach resorts and swimming pools."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1879",
        "sku": "EK-1879",
        "gtin": "5281018953464",
        "category": "العناية بالبشرة / زيوت بيزلين الذهبية لتسمير وتان الجسم بالشمس 200ml",
        "brand": "Beesline",
        "ar": {
            "title": "زيت تسمير ذهبي من بيزلين، 200 مل",
            "meta_title": "زيت تسمير ذهبي بيزلين 200مل | إكليل أبها",
            "meta_description": "اشتري زيت تسمير ذهبي من بيزلين (200 مل). زيت تسمير طبيعي بالجزر وشمع النحل والذهب لتان برونزي غني ولامع. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بيزلين", "زيت_تسمير_بيزلين", "تان_ذهبي", "زيت_الجزر", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Gold Tanning Oil, 200 ml",
            "meta_title": "Beesline Gold Tanning Oil 200ml | Ekleel Abha",
            "meta_description": "Buy original Beesline Gold Tanning Oil (200 ml). Natural Carrot & Beeswax gold shimmer sun tanning oil. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["beesline", "tanning_oil", "gold_tanning", "carrot_tanning_oil", "ekleel_abha"]
        },
        "schema": {
            "brand": "Beesline",
            "category": "Skincare / Tanning Oil",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "beesline-gold-tanning-oil-200ml.webp",
            "alt": "Beesline Gold Tanning Oil 200ml",
            "title": "Beesline Gold Tanning Oil 200ml"
        }
    }

def create_product_1874_or_1880():
    pass

def create_product_1880():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>مزيل المكياج من بيزلين 150 مل (Beesline Makeup Remover - 150 ml)</strong> المستحضر الطبيعي ثنائي المفعول (Micellar Makeup Remover / Bi-Phase Makeup Remover) الأفضل والأنعم لإزالة مكياج الوجه، العيون الشديد، والمستحضرات المائية والمقاومة للماء (Waterproof Makeup) دون تسبيب أي حرقان أو شد بالبشرة. يرتكز هذا المزيل الفاخر من بيزلين (Beesline Micellar Cleansing Makeup Remover 150ml) على زيت اللوز الحلو النقي (Sweet Almond Oil)، خلاصة الورد الجوري، وصمغ النحل النقي (Propolis).</p>
<p>يعمل مزيل المكياج من بيزلين على إزالة مسكارا العين المقاومة للماء، أحمر الشفاه الثابت، ومكياج الوجه الكثيف بمسحة قطنية خفيفة، مع ترطيب محيط العين والشفاه، ليترك بشرتكِ ناصعة النظافة، طرية، ومفعمة بالانتعاش دون أي أثر دهني لزج.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>إزالة فورية للمكياج المقاوم للماء (Waterproof Makeup):</strong> يزيل مسكارا العيون الكثيفة وأحمر الشفاه الثابت بمسحة واحدة.</li>
  <li><strong>مدعم بـ زيت اللوز الحلو والورد الجوري:</strong> يغذي محيط العين الحساس ويحافظ على طراوة الرموش.</li>
  <li><strong>تطهير وتهدئة بـ صمغ النحل النقي (Propolis):</strong> يطهر المسام من ترسبات المكياج ويحمي البشرة.</li>
  <li><strong>تركيبة خفيفة آمنة 100% على العيون الحساسة:</strong> لا يسبب حرقان للعينين أو ضبابية الرؤية.</li>
  <li><strong>خالي 100% من الكحول والبارابين والعطور القاسية:</strong> مجرب جلدياً ومن أطباء العيون.</li>
  <li><strong>عبوة سعة 150 مل بمضخة دقيقة:</strong> حجم وافر وممتاز للاستخدام اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الرج والبلل):</strong> رجي العبوة جيداً لخلط الطبقتين، ثم بللي قطعة قطن نظيفة بـ مزيل مكياج بيزلين.</li>
  <li><strong>الخطوة الثانية (التطبييق):</strong> ضعي القطنة المبللة على العينين المغطين أو الشفاه لـ 5 ثوانٍ لإذابة المكياج.</li>
  <li><strong>الخطوة الثالثة (المسح):</strong> امسحي بلطف للأطراف دون فرك قسي، ثم اشطفي بالماء الفاتر (يُستعمل كل مساء).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت اللوز الحلو والورد الجوري (Sweet Almond Oil & Rose Extract):</strong> يذيبان أصباغ المكياج ويرطبان الرموش.</li>
  <li><strong>صمغ النحل النقي والجليسرين (Propolis & Glycerin):</strong> يطهران الجلد ويحفظان الترطيب الفائق.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي لإزالة مكياج الوجه والعيون والشفاه فقط.</li>
  <li>أغلقي العينين أثناء مسح مكياج الجفون والرموش.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن مزيل مكياج بيزلين الطبيعي الأصلي 150 مل لإزالة المكياج المقاوم للماء وترطيب البشرة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / مزيلات ومستحضرات تنظيف مكياج الوجه والعيون بيزلين 150ml</td></tr>
  <tr><th>نوع المنتج</th><td>مزيل مكياج طبيعي ثنائي المفعول للوجه والعيون المقاوم للماء (150ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>150 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (بما في ذلك البشرة الحساسة ومحيط العيون)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناصعة النظافة، خالية من آثار المكياج والمسكارا، طرية ومرطبة</td></tr>
  <tr><th>الملمس</th><td>سائل مائي-زيتي خفيف جداً يمسح بسهولة</td></tr>
  <tr><th>العطر</th><td>عطر الورد الجوري الطبيعي الناعم</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت اللوز الحلو، خلاصة الورد، صمغ النحل (Propolis)، جليسرين</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Lebanon)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت اللوز والورد في مزيل مكياج بيزلين (Beesline Makeup Remover)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مزيل المكياج من بيزلين مشكلة صعوبة إزالة المسكارا المقاومة للماء، انسداد المسام بترسبات الفاونديشن، وجفاف محيط العينين.</p>

<h3>لماذا تنجح التركيبة ثنائية المفعول (Bi-Phase)?</h3>
<p>لأن الطبقة الزيتية تذوب صبغات المكياج المقاوم للماء، بينما تجمع الطبقة المائية الشوائب دون ترك أثر دهني لزج.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الرج جيداً قبل الاستعمال:</strong> رجي العبوة لـ 3 ثوانٍ لدمج الزيت بالماء الميسيلار.<br>
2. <strong>الترك على العين لـ 5 ثوانٍ:</strong> وضعي القطنة المبللة على العين 5 ثوانٍ لإذابة المسكارا قبل المسح.<br>
3. <strong>التنظيف اللطيف دون فرك قسي:</strong> امسحي برفق لحماية ألياف الرموش والجلد الرقيق.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مزيلات المكياج الزيتية تسبب ضبابية العين وتساقط الرموش."<br>
<strong>الحقيقة:</strong> مزيل بيزلين مدعم بزيت اللوز والورد لتغذية وتقوية الرموش دون تسبيب ضبابية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تستحلب ميكرو-زيوت اللوز الحلو بوليمرات السيليكون بالمكياج المقاوم للماء، فيسهل مسحها بالقطن دون شد.</p>"""

    faqs = [
        ("ما هو مزيل المكياج من بيزلين 150 مل؟", "هو مزيل مكياج طبيعي ثنائي المفعول من بيزلين بزيت اللوز والورد لإزالة مكياج الوجه والعيون المقاوم للماء 150 مل."),
        ("ما هي فوائد زيت اللوز الحلو والورد وصمغ النحل؟", "يذيب زيت اللوز المكياج المقاوم للماء، يغذي الورد محيط العين، ويطهر صمغ النحل البشرة ب طراوة."),
        ("هل يزيل المسكارا المقاومة للماء والمكياج الثقيل؟", "نعم، مثبت سريرياً في إزالة المسكارا المقاومة للماء وأحمر الشفاه الثابت فورياً دون فرك."),
        ("ما حجم العبوة؟", "تأتي بحجم وافر سعة 150 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "رجي العبوة، بللي قطعة قطن، وضعيها على العين 5 ثوانٍ ثم امسحي بلطف واشطفي بالماء الفاتر."),
        ("هل هو مكون من مواد طبيعية ونباتية 100%؟", "نعم، مكونات طبيعية ونباتية خالية من الكحول والبارابين والعطور القاسية."),
        ("ما هو بلد صنع مزيل مكياج بيزلين؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين العالمية (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يناسب العيون الحساسة ومستخدمي العدسات؟", "نعم، فورمولا مجربة طبياً وآمنة تماماً للعيون الحساسة ومستخدمي العدسات."),
        ("ما هي رائحة مزيل مكياج بيزلين؟", "يتميز برائحة الورد الجوري الطبيعية اللطيفة جداً."),
        ("هل يترك أثراً دهنياً لزجاً على الوجه؟", "لا، فورمولا خفيفة تمسح الشوائب وتترك البشرة طرية ونظيفة دون لزوجة."),
        ("هل العبوة 150 مل مناسبة للاستخدام اليومي؟", "نعم، عبوة وافرة تكفي لعدة أشهر من إزالة المكياج اليومي."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعبوتها المغلقة محكماً."),
        ("هل يحمي ويقوي الرموش من التساقط؟", "نعم، زيت اللوز الحلو يغذي ألياف الرموش ويحميها من التكسر والتساقط."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة أنيقة بفتحة دقيقة تمنع الهدر."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل كل مساء لإزالة المكياج وتنظيف الوجه."),
        ("هل يناسب جميع أنواع بشرة الوجه؟", "مناسب للبشرة العادية، الجافة، والدهنية والحساسة."),
        ("هل ينصح بالشطف بالماء بعده؟", "نعم، يُفضل غسل الوجه بغسول خفيف بعد إزالة المكياج."),
        ("هل هو مزيل المكياج الأكثر شهرة لبيزلين؟", "نعم، Beesline Bi-Phase Makeup Remover المستحضر الأول والأكثر مبيعاً لبيزلين."),
        ("هل يمنح حس نظافة وطراوة مطلقة؟", "نعم، يضمن نظافة وطراوة وإنعاشاً كاملاً للبشرة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يزيل أحمر الشفاه المات الثابت؟", "نعم، يذوب أحمر الشفاه الثابت والمات بسهولة متناهية."),
        ("هل يترك الجلد طرياً؟", "نعم، يترك الوجه ومحيط العين طرياً ومسترخياً."),
        ("هل يمنع انسداد المسام البكتيري؟", "نعم، إزالة المكياج التامة تمنع انسداد المسام وظهور البثور."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Makeup Remover - 150 ml</strong> (Beesline Micellar Cleansing Makeup Remover 150ml) is the natural bi-phase facial cleanser engineered to erase face makeup, stubborn eye mascara, and waterproof products without stinging or skin pulling. Formulated by Beesline, it blends Sweet Almond Oil, Damask Rose extract, and antibacterial Propolis.</p>
<p>Beesline Makeup Remover dissolves waterproof eye mascara, matte long-lasting lipsticks, and heavy face foundation with a gentle cotton wipe, nourishing the delicate eye contour and lashes while leaving your skin touchably clean, soft, and refreshed with zero oily residue.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Instant Waterproof Makeup Removal:</strong> Effortlessly erases waterproof mascara and matte lipsticks.</li>
  <li><strong>Enriched with Sweet Almond Oil & Damask Rose:</strong> Nourishes sensitive eye contours and conditions lashes.</li>
  <li><strong>Purifying Propolis Defense:</strong> Cleanses pores from cosmetic residues and protects dermal health.</li>
  <li><strong>100% Safe Formula for Sensitive Eyes:</strong> Causes zero eye stinging, tearing, or blurry vision.</li>
  <li><strong>100% Free of Alcohol, Parabens & Harsh Synthetic Fragrances:</strong> Ophthalmologist and dermatologist tested.</li>
  <li><strong>Generous 150ml Dispenser Bottle:</strong> High-value bottle ideal for daily evening makeup removal.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Shake & Wet):</strong> Shake bottle well to blend the two phases, then saturate a clean cotton pad with Beesline makeup remover.</li>
  <li><strong>Step 2 (Apply):</strong> Hold saturated cotton pad over closed eyes or lips for 5 seconds to melt makeup.</li>
  <li><strong>Step 3 (Wipe):</strong> Wipe gently outward without harsh rubbing, then rinse face with warm water (use every evening).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Sweet Almond Oil & Damask Rose Extract:</strong> Dissolve waterproof makeup pigments and condition eyelashes.</li>
  <li><strong>Pure Propolis & Glycerin:</strong> Purify dermal tissues and seal in essential 24-hour hydration.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial, eye, and lip makeup removal application only.</li>
  <li>Keep eyes closed while wiping eyelid and lash makeup.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Beesline's 150ml natural bi-phase Makeup Remover to erase waterproof mascara and nourish sensitive skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Skincare / Beesline Natural Facial & Eye Makeup Removers 150ml</td></tr>
  <tr><th>Product Type</th><td>Bi-Phase Natural Sweet Almond & Rose Waterproof Makeup Remover (150ml)</td></tr>
  <tr><th>Volume/Weight</th><td>150 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Including Sensitive Eyes & Contact Lens Wearers)</td></tr>
  <tr><th>Finish</th><td>Touchably clean, makeup-free, hydrated & soft skin and lashes</td></tr>
  <tr><th>Texture</th><td>Lightweight bi-phase oil-water fluid</td></tr>
  <tr><th>Fragrance</th><td>Subtle natural Damask Rose Beesline aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Sweet Almond Oil, Damask Rose, Propolis, Glycerin</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Bi-Phase Solubilization & Almond Lipid Conditioning</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Makeup Remover resolves stubborn waterproof mascara removal, clogged pores from foundation, and lash breakage.</p>

<h3>Why choose Beesline Bi-Phase Makeup Remover?</h3>
<p>The lipid phase dissolves hydrophobic silicone polymers in waterproof makeup, while the aqueous phase sweeps away debris without greasy residue.</p>"""

    en_faqs = [
        ("What is Beesline Makeup Remover - 150 ml?", "It is a natural bi-phase makeup remover formulated with Sweet Almond Oil and Rose extract to erase face and waterproof eye makeup."),
        ("What are the benefits of Sweet Almond Oil, Damask Rose, and Propolis?", "Sweet Almond Oil dissolves waterproof makeup, Rose extract conditions eye contours, and Propolis purifies pores."),
        ("Does it erase waterproof mascara and matte lipstick effortlessly?", "Yes, clinically proven to dissolve waterproof mascara and long-lasting matte lipsticks without harsh rubbing."),
        ("What volume is contained in this bottle?", "It comes in a generous 150ml dispenser bottle."),
        ("How do I use it correctly?", "Shake bottle well, saturate a cotton pad, hold over closed eyes for 5 seconds, wipe gently outward, and rinse with water."),
        ("Is it 100% free of alcohol, parabens, and harsh fragrances?", "Yes, 100% natural formula free of alcohol, parabens, and harsh synthetic fragrances."),
        ("Where is Beesline Makeup Remover manufactured?", "Proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Is it safe for sensitive eyes and contact lens wearers?", "Yes, ophthalmologist-tested gentle formula completely safe for sensitive eyes and contact lens wearers."),
        ("What scent does Beesline Makeup Remover have?", "Features a soft, pleasant natural Damask Rose fragrance."),
        ("Does it leave a heavy greasy film on skin?", "No, weightless bi-phase fluid sweeps away makeup leaving skin clean and soft with zero greasy residue."),
        ("Is the 150ml bottle economical for daily use?", "Yes, generous 150ml bottle lasts through months of nightly makeup removal."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Does it nourish and protect eyelashes against fallout?", "Yes, Sweet Almond Oil conditions lash fibers, preventing breakage and fallout."),
        ("Is the dispenser cap leak-proof?", "Yes, comes in a sturdy bottle with a precision dispenser cap."),
        ("How often should I use it daily?", "Recommended for use every evening to cleanse face and eye makeup."),
        ("Is it suitable for all skin types?", "Ideal for normal, dry, oily, and sensitive skin types."),
        ("Is water rinsing recommended after use?", "Rinsing with a mild face wash after makeup removal is recommended."),
        ("Is it Beesline's #1 makeup remover?", "Yes, Bi-Phase Cleansing Makeup Remover is the #1 flagship makeup remover by Beesline."),
        ("Does it deliver complete facial cleanliness confidence?", "Yes, guarantees complete makeup removal, skin softness, and cleanliness confidence."),
        ("Is the bottle recyclable?", "Yes, 100% recyclable environmentally friendly bottle."),
        ("Does it erase long-wear matte lipstick?", "Yes, effortlessly dissolves long-wear matte lipstick pigments."),
        ("Does it leave skin touchably soft?", "Yes, leaves facial skin and eye contours touchably soft, smooth, and supple."),
        ("Does it prevent pore clogging?", "Yes, total makeup removal prevents pore clogging and acne breakouts."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1880",
        "sku": "EK-1880",
        "gtin": "5281018881682",
        "category": "العناية بالبشرة / مزيلات ومستحضرات تنظيف مكياج الوجه والعيون بيزلين 150ml",
        "brand": "Beesline",
        "ar": {
            "title": "مزيل المكياج  من بيزلين 150 مل",
            "meta_title": "مزيل المكياج بيزلين 150مل | إكليل أبها",
            "meta_description": "اشتري مزيل المكياج من بيزلين (150 مل). مزيل مكياج طبيعي ثنائي المفعول بزيت اللوز والورد لإزالة المكياج المقاوم للماء. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بيزلين", "مزيل_مكياج_بيزلين", "مزيل_مكياج", "تنظيف_البشرة", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Makeup Remover - 150 ml",
            "meta_title": "Beesline Makeup Remover 150ml | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Beesline Makeup Remover (150 ml). Natural Sweet Almond Oil bi-phase waterproof makeup remover. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["beesline", "makeup_remover", "biphase_remover", "waterproof_remover", "ekleel_abha"]
        },
        "schema": {
            "brand": "Beesline",
            "category": "Skincare / Makeup Remover",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "beesline-makeup-remover-150ml.webp",
            "alt": "Beesline Makeup Remover 150ml",
            "title": "Beesline Makeup Remover 150ml"
        }
    }

print("Loaded all 5 Batch 33 builders complete")
