import json, os
from build_batch27 import build_beesline_deo

def create_product_1847():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول الوجه للبشرة الدهنية المعرضة لحب الشباب من بيزلين 250 مل (Beesline Facial Wash for Oily and Acne-Prone Skin - 250ml)</strong> منظف البشرة الطبي العلاجي الأكثر تميزاً لتنقية المسام، التحكم بإفرازات الدهون، والقضاء على حب الشباب دون تسبب في جفاف أو تهيج الجلد. يرتكز هذا الغسول الطبي من بيزلين (Beesline Acne-Prone Facial Wash) على خلاصة صمغ النحل المطهر (Propolis)، حمض الساليسليك (Salicylic Acid)، خلاصة الزعتر البري، ونبات الصبار (Aloe Vera).</p>
<p>يعمل غسول بيزلين على إزالة الشوائب، الدهون الزائدة، والزيوت المتراكمة بداخل المسام، حيث يقضي على البكتيريا المسببة لـ حب الشباب والرؤوس السوداء، ليترك بشرتكِ ناصعة، جافة برفق، ومفعمة بالصفاء والانتعاش دون أي تأثير صابوني قسي.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف عميق للمسام والتحكم بالدهون:</strong> يزيل الدهون الزائدة ويمنع لمعان البشرة الدهنية.</li>
  <li><strong>مكافحة حب الشباب والرؤوس السوداء:</strong> حمض الساليسليك وصمغ النحل يقتلان بكتيريا الأكنيه فورياً.</li>
  <li><strong>معزز بخلاصة الزعتر والألوفيرا المهدئة:</strong> يهدئ أحمرار البثور ويسرع التئام ندبات حب الشباب.</li>
  <li><strong>خالي 100% من الصابون، الكحول، والبارابين:</strong> تركيبة دقيقة موازنة لـ pH البشرة الدهنية.</li>
  <li><strong>منع انسداد المسام وتكون البثور الجديدة:</strong> يقشر الخلايا الميتة ويحفظ نقاء الوجه.</li>
  <li><strong>عبوة وافرة سعة 250 مل:</strong> حجم ممتازة ومناسبة للاستعمال اليومي مرتين.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التبليل):</strong> بلي بشرة وجهكِ بالماء الفاتر أثناء الغسيل.</li>
  <li><strong>الخطوة الثانية (الرغوة):</strong> اسكبي كمية مناسبة من غسول بيزلين وافركي بين اليدين لتوليد رغوة لطيفة.</li>
  <li><strong>الخطوة الثالثة (التدليك والشطف):</strong> دلكي الوجه بحركات دائرية خاصة على منطقة T-Zone ثم اشطفي بالماء الفاتر (مرتين يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>صمغ النحل وحمض الساليسليك (Propolis & Salicylic Acid):</strong> يطهران المسام ويقضيان على بكتيريا حب الشباب.</li>
  <li><strong>خلاصة الزعتر والألوفيرا المهدئة:</strong> تهدئان التهاب البثور وتحفظان التوازن المائي.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه فقط.</li>
  <li>تجنبي ملامسة السائل المباشرة لداخل العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من البشرة الدهنية المعرضة لحب الشباب والرؤوس السوداء وتفتش عن غسول طبي بصمغ النحل من بيزلين.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / غسولات بيزلين الطبية للبشرة الدهنية وحب الشباب</td></tr>
  <tr><th>نوع المنتج</th><td>غسول وجه طبي لتنقية البشرة الدهنية وعلاج حب الشباب (250ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>250 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الدهنية، المختلطة، والمعرضة لحب الشباب</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة وجه مطهرة، منقاة من الدهون، خالية من حب الشباب والرؤوس السوداء</td></tr>
  <tr><th>الملمس</th><td>جل رغوي نقي لطيف سريع الامتزاج بالماء</td></tr>
  <tr><th>العطر</th><td>عطر الزعتر والألوفيرا المنعش اللطيف</td></tr>
  <tr><th>المكونات النشطة</th><td>صمغ النحل، حمض الساليسليك، الزعتر البري، الألوفيرا، خالي من الصابون</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Beesline Laboratories)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد صمغ النحل وحمض الساليسليك (Beesline Facial Wash)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول بيزلين للبشرة الدهنية مشكلة حب الشباب النشط، الرؤوس السوداء، انسداد المسام بالدهون، ولمعان البشرة.</p>

<h3>لماذا تنجح تركيبة صمغ النحل والساليسليك؟</h3>
<p>لأن حمض الساليسليك يذيب الدهون داخل المسام، بينما يعقم صمغ النحل البكتيريا اللاهوائية المسببة للأكنيه.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الغسيل مرتين يومياً:</strong> استعمليه صباحاً ومساءً لتنقية الشوائب.<br>
2. <strong>التركيز على T-Zone:</strong> دلكي الجبهة والأنف والذقن جيداً بالرغوة.<br>
3. <strong>المرطب الخالي من الزيوت:</strong> استعملي لوشن مرطب خفيف خالي من الزيوت بعد الغسيل.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "غسولات حب الشباب يجب أن تجفف الوجه تماماً حتى يقف الإفراز الدهني."<br>
<strong>الحقيقة:</strong> التجفيف الشديد يحفز المسام على إفراز مزيد من الدهون، بينما بيزلين يوازن pH دون تجفيف.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخترق جزيئات حمض الساليسليك المحبة للدهون (BHA) الغدد الدهنية، فتفكك التجمعات الزهمية وتمنع تكون البثور.</p>"""

    faqs = [
        ("ما هو غسول الوجه للبشرة الدهنية المعرضة لحب الشباب من بيزلين 250 مل؟", "هو غسول طبي من بيزلين غني بصمغ النحل وحمض الساليسليك لتنقية المسام والتحكم ب إفراز الدهون وعلاج حب الشباب 250 مل."),
        ("ما هي فوائد صمغ النحل وحمض الساليسليك؟", "يطهر صمغ النحل البكتيريا المسببة للأكنيه، بينما يذيب حمض الساليسليك الدهون بالمسام وينقيها."),
        ("هل يمنع تكون حب الشباب والرؤوس السوداء؟", "نعم، مثبت سريرياً في تقشير المسام ومنع تكون البثور والرؤوس السوداء."),
        ("ما حجم العبوة؟", "تأتي بحجم وافر سعة 250 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "اسكبي كمية على الوجه المبلل، افركي لتوليد رغوة، دلكي الوجه واشطفي بالماء الفاتر مرتين يومياً."),
        ("هل هو خالي من الصابون والكحول والبارابين؟", "نعم، تركيبة طبية خالية 100% من الصابون والكحول والبارابين وموازنة للـ pH."),
        ("ما هو بلد صنع غسول بيزلين؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين العالمية (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يجفف الوجه أو يسبب حرقاناً؟", "لا، يحتوي على الألوفيرا المهدئة لحفظ توازن رطوبة الوجه دون حرقان."),
        ("ما هي رائحة غسول بيزلين؟", "يتميز برائحة ناعمة من خلاصة الزعتر والألوفيرا الطبيعية."),
        ("هل يناسب جميع درجات البشرة الدهنية والمختلطة؟", "نعم، ممتاز للبشرة الدهنية، المختلطة، والمعرضة لحب الشباب."),
        ("هل العبوة 250 مل مناسبة للاستخدام اليومي المستمر؟", "نعم، حجم وافر ممتاز للاستخدام اليومي لعدة أشهر."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل يترك ملمساً ناعماً؟", "نعم، ينظف الوجه ويتركه طرياً ونظيفاً دون لزوجة."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة أنيقة بضغاط محكم السكب."),
        ("هل يقلل لمعان البشرة الدهنية؟", "نعم، يضبط الإفرازات الزهمية ويمنح ملمساً مطفياً ناعماً."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُوصى باستخدامه 2 مرات يومياً (صباحاً ومساءً)."),
        ("هل يناسب المراهقين والبالغين؟", "مناسب جداً للمراهقين والبالغين من سن 12 سنة."),
        ("هل يساعد في التئام ندبات حب الشباب؟", "نعم، الزعتر وصمغ النحل يسرعان التئام البثور والندبات."),
        ("هل هو الغسول الأكثر طلباً للبشرة الدهنية من بيزلين؟", "نعم، الغسول الطبي الأول للبشرة الدهنية من بيزلين."),
        ("هل يمنح حس نضارة وصفاء؟", "نعم، يمنح وجهكِ نضارة وصفاءً ملحوظاً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يمنع التكسر والتجمع الزهمي؟", "نعم، ينظف الدهون أولاً بأول ليمنع تكتل الزهم."),
        ("هل يترك الجلد طرياً؟", "نعم، يترك الوجه طرياً ومسترخياً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Facial Wash for Oily and Acne-Prone Skin - 250ml</strong> is the clinical purifying face wash engineered to unclog pores, control sebum production, and halt acne breakouts without causing skin dryness or irritation. Formulated by Beesline, it combines antibacterial Propolis, Salicylic Acid (BHA), Wild Thyme extract, and Aloe Vera.</p>
<p>Beesline Acne-Prone Facial Wash sweeps away deep impurities, excess oil, and clogged sebum, destroying acne-causing bacteria and leaving your face visibly clear, purified, and refreshed without harsh soap stripping.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Deep Pore Cleansing & Sebum Control:</strong> Removes excess oil and eliminates oily shine throughout the day.</li>
  <li><strong>Combats Acne Breakouts & Blackheads:</strong> Salicylic Acid and Propolis destroy acne bacteria instantly.</li>
  <li><strong>Enriched with Wild Thyme & Aloe Vera:</strong> Soothes acne redness, inflammation, and speeds up blemish healing.</li>
  <li><strong>100% Soap, Alcohol & Paraben Free:</strong> Gentle pH-balanced formulation for oily and acne-prone skin.</li>
  <li><strong>Prevents Clogged Pores & Future Breakouts:</strong> Exfoliates dead skin cells to maintain skin clarity.</li>
  <li><strong>Generous 250ml Pump Bottle:</strong> High-value bottle size ideal for twice-daily continuous facial hygiene.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Wet):</strong> Wet your facial skin with warm water during cleansing.</li>
  <li><strong>Step 2 (Lather):</strong> Pump a small amount of Beesline facial wash onto hands and rub to create a soft lather.</li>
  <li><strong>Step 3 (Massage & Rinse):</strong> Gently massage over face, focusing on the T-Zone, then rinse with warm water (twice daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Propolis & Salicylic Acid (BHA):</strong> Sanitize pores and destroy acne-causing bacteria.</li>
  <li><strong>Wild Thyme & Aloe Vera Extracts:</strong> Calm acne inflammation and preserve essential skin moisture.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial cleansing application only.</li>
  <li>Avoid direct contact with the interior of the eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with oily, acne-prone skin or blackheads seeking a Propolis and Salicylic Acid purifying facial cleanser by Beesline.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Skincare / Clinical Oily & Acne-Prone Facial Cleansers</td></tr>
  <tr><th>Product Type</th><td>Purifying Acne-Prone Facial Cleansing Gel (250ml)</td></tr>
  <tr><th>Volume/Weight</th><td>250 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Oily, Combination & Acne-Prone Skin</td></tr>
  <tr><th>Finish</th><td>Purified, shine-free, acne-cleared & fresh facial skin</td></tr>
  <tr><th>Texture</th><td>Soft foaming purifying gel</td></tr>
  <tr><th>Fragrance</th><td>Subtle natural Thyme & Aloe Vera scent</td></tr>
  <tr><th>Active Ingredients</th><td>Propolis, Salicylic Acid, Wild Thyme, Aloe Vera, Soap-Free Base</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon (Beesline Laboratories)</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Salicylic Acid Pore Penetration & Propolis Sanitization</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Acne-Prone Facial Wash resolves active acne breakouts, blackheads, sebum cloging, and oily shine.</p>

<h3>Why choose Beesline Acne Wash?</h3>
<p>Salicylic Acid (BHA) is lipid-soluble, penetrating deep into sebaceous glands to dissolve clogged sebum while Propolis kills acne bacteria.</p>"""

    en_faqs = [
        ("What is Beesline Facial Wash for Oily and Acne-Prone Skin - 250ml?", "It is a clinical face wash formulated with Propolis and Salicylic Acid to purify pores, control oil, and treat acne breakouts."),
        ("What are the benefits of Propolis and Salicylic Acid?", "Propolis kills acne-causing bacteria, while Salicylic Acid dissolves clogged sebum inside pores."),
        ("Does it prevent acne breakouts and blackheads?", "Yes, clinically proven to exfoliate pores and prevent new acne blemishes and blackheads."),
        ("What volume is contained in this bottle?", "It comes in a 250ml pump bottle."),
        ("How do I apply it correctly?", "Apply to wet face, lather, massage gently over T-Zone, and rinse with warm water twice daily."),
        ("Is it 100% soap-free, alcohol-free, and paraben-free?", "Yes, gentle pH-balanced formula completely free of soap, alcohol, and parabens."),
        ("Where is Beesline Facial Wash manufactured?", "It is proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it dry out facial skin or sting?", "No, enriched with soothing Aloe Vera to maintain essential skin hydration without stinging."),
        ("What scent does Beesline Facial Wash have?", "Features a light natural Wild Thyme and Aloe Vera scent."),
        ("Is it suitable for oily and combination skin types?", "Ideal for oily, combination, and acne-prone skin types."),
        ("Is the 250ml bottle economical for daily use?", "Yes, generous size lasts through months of twice-daily cleansing."),
        ("How should I store the bottle?", "Store in a cool, dry place away from direct heat."),
        ("Does it leave skin touchably smooth?", "Yes, purifies skin leaving it fresh, smooth, and non-sticky."),
        ("Is the bottle pump convenient?", "Yes, comes with a convenient pump dispenser for easy dosing."),
        ("Does it reduce oily skin shine?", "Yes, controls sebum production for a fresh matte finish."),
        ("How many times daily should I use it?", "Recommended for use twice daily, morning and evening."),
        ("Is it safe for teens and adults?", "Ideal for teens and adults aged 12+ dealing with acne."),
        ("Does it help heal acne blemishes?", "Yes, Wild Thyme and Propolis accelerate acne blemish healing."),
        ("Is it Beesline's top face wash for oily skin?", "Yes, Beesline Propolis Face Wash is the #1 trusted choice for oily acne-prone skin."),
        ("Does it give facial skin a clear glow?", "Yes, leaves skin visibly purified, clear, and radiant."),
        ("Is the bottle recyclable?", "Yes, 100% recyclable environmentally friendly bottle."),
        ("Does it prevent pore clogging?", "Yes, sweeps away daily excess oil to prevent clogged pores."),
        ("Does it leave skin touchably soft?", "Yes, leaves facial skin soft, clean, and calm."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1847",
        "sku": "EK-1847",
        "gtin": "5281018004050",
        "category": "العناية بالبشرة / غسولات بيزلين الطبية للبشرة الدهنية وحب الشباب",
        "brand": "Beesline",
        "ar": {
            "title": "غسول الوجه للبشرة الدهنية المعرضة لحب الشباب  من بيزلين 250 مل",
            "meta_title": "غسول بيزلين للبشرة الدهنية وحب الشباب 250مل | إكليل أبها",
            "meta_description": "اشتري غسول الوجه للبشرة الدهنية المعرضة لحب الشباب من بيزلين (250 مل). غسول طبي بصمغ النحل وحمض الساليسليك خالي من الصابون. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بيزلين", "غسول_بيزلين", "البشرة_الدهنية", "علاج_حب_الشباب", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Facial Wash for Oily and Acne-Prone Skin - 250ml",
            "meta_title": "Beesline Acne-Prone Facial Wash 250ml | Ekleel Abha",
            "meta_description": "Buy original Beesline Facial Wash for Oily and Acne-Prone Skin (250ml). Propolis & Salicylic Acid soap-free cleanser. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["beesline", "beesline_face_wash", "oily_skin", "acne_treatment", "ekleel_abha"]
        },
        "schema": {
            "brand": "Beesline",
            "category": "Skincare / Face Wash",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "beesline-facial-wash-for-oily-and-acne-prone-skin-250ml.webp",
            "alt": "Beesline Facial Wash for Oily and Acne-Prone Skin 250ml",
            "title": "Beesline Facial Wash for Oily and Acne-Prone Skin 250ml"
        }
    }

def create_product_1848():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>صابونة لتفتيح المنطقة الحساسة من بيزلين 110 جم (Beesline Whitening Sensitive Zone Soap - 110g)</strong> الصابونة الطبية الطبيعية المبتكرة الأكثر شهرة وطلباً في الشرق الأوسط للنظافة وتفتيح المنطقة الحساسة ب أمان تام. ترتكز هذه الصابونة الفريدة من بيزلين (Beesline Whitening Sensitive Zone Soap) على توليفة صمغ النحل (Propolis)، حجر الشبة (Alum)، زيت الزيتون البكر، مركب اللوميسكين (Lumiskin)، وخلاصة البقدونس.</p>
<p>تعمل صابونة بيزلين للمنطقة الحساسة على موازنة الحموضة الفسيولوجية pH، تطهير أنسجة المنطقة الحساسة من البكتيريا والفطريات المسببة للرائحة والحكة، وتفتيح اسمرار التصبغات والجلد الداكن، لتوفر لكِ نظافة، تعقيماً، ونعومة كالحرير دون التسبب في أي جفاف أو حرقان.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح طبيعي وآمن للمنطقة الحساسة:</strong> يزيل الاسمرار والتصبغات الداكنة ويجمع لون الجلد.</li>
  <li><strong>موازنة الحموضة الفسيولوجية الطبيعية pH:</strong> تحافظ على بيئة المنطقة الحساسة وتمنع الالتهابات.</li>
  <li><strong>تطهير وتعقيم بصمغ النحل وحجر الشبة:</strong> تقضي على البكتيريا والفطريات المسببة للرائحة الكريهة والحكة.</li>
  <li><strong>ترطيب وتنعيم بأنسجة الزيتون والبقدونس:</strong> تطري جلد المنطقة الحساسة وتمنع الجفاف والاحتكاك.</li>
  <li><strong>خالية 100% من الكحول، الصابون القاسي، والبارابين:</strong> تركيبة دقيقة ومجربة جلدياً لأمان المرأة.</li>
  <li><strong>قطعة صابون وافرة وزن 110 جم:</strong> حجم ممتاز يدوم لعدة أسابيع من العناية اليومية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الرغوة):</strong> افركي صابونة بيزلين بين يدين مبللتين بالماء الفاتر لتوليد رغوة مطهرة غنية.</li>
  <li><strong>الخطوة الثانية (التطبيق):</strong> وضعي الرغوة بلطف على جلد المنطقة الحساسة ودلكي برفق دون فرك قسي.</li>
  <li><strong>الخطوة الثالثة (الشطف):</strong> اشطفي بالماء الفاتر جيداً وجففي بالمنشفة برفق (تُستعمل 1 إلى 2 مرة يومياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>صمغ النحل وحجر الشبة (Propolis & Alum):</strong> يطهران ويقعقان الأنسجة ويقضيان على الجراثيم.</li>
  <li><strong>اللوميسكين وخلاصة البقدونس وزيت الزيتون:</strong> تفتيح طبيعي وتغذية ناعمة لجلد المنطقة الحساسة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على جلد المنطقة الحساسة فقط.</li>
  <li>تجنبي إدخال رغوة الصابون داخل القناة الفرجية الداخلية.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بوعاء الصابون.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن صابونة بيزلين الطبية لتفتيح، تعقيم، وموازنة حموضة المنطقة الحساسة ب أمان.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيزلين (Beesline)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / صابون ومستحضرات تفتيح المنطقة الحساسة الطبيعية</td></tr>
  <tr><th>نوع المنتج</th><td>صابونة طبية طبيعية لتفتيح وتعقيم المنطقة الحساسة (110g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>110 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>بشرة المنطقة الحساسة الرقيقة</td></tr>
  <tr><th>المظهر النهائي</th><td>منطقة حساسة مطهرة، معقمة، مفتحة اللون، ناعمة ومحمية من الحكة</td></tr>
  <tr><th>الملمس</th><td>قالب صابوني ناعم يولد رغوة لطيفة بسلاسة</td></tr>
  <tr><th>العطر</th><td>عطر ناعم لطيف خالي من العطور القاسية</td></tr>
  <tr><th>المكونات النشطة</th><td>صمغ النحل، حجر الشبة، لوميسكين، خلاصة البقدونس، زيت الزيتون</td></tr>
  <tr><th>بلد المنشأ</th><td>لبنان (Beesline Laboratories)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beesline Laboratories</td></tr>
  <tr><th>الفئة العمرية</th><td>النساء والفتيات (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد صمغ النحل واللوميسكين للمنطقة الحساسة (Beesline Soap)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج صابونة بيزلين للمنطقة الحساسة مشكلة اسمرار وسواد المنطقة الحساسة، الرائحة الكريهة، الحكة، والجفاف بالصابون العادي.</p>

<h3>لماذا تنجح تركيبة صمغ النحل واللوميسكين؟</h3>
<p>لأن صمغ النحل يقضي على الفطريات والبكتيريا دون إيذاء التوازن الفسيولوجي، بينما يفتح اللوميسكين التصبغات.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام الرغوة فقط:</strong> وضعي رغوة الصابونة فقط على الجلد واشطفي فوراً بالماء.<br>
2. <strong>التجفيف بالمنشفة القطنية:</strong> جففي المنطقة الحساسة بالطبطبة لمنع رطوبة الفطريات.<br>
3. <strong>الاستمرار مرتين يومياً:</strong> الاستخدام المستمر يضمن نتائج تفتيح ناصعة ومستدامة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الصابون يسبب تهيج واسمرار المنطقة الحساسة دائماً."<br>
<strong>الحقيقة:</strong> صابونة بيزلين خالية من القلويات والبارابين ومصممة بمكونات طبية موازنة لـ pH أمان للمنطقة الحساسة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط الفلافونويدات بصمغ النحل نمو الكانديدا (Candida Albicans)، بينما ينظم البقدونس تجدد الخلايا.</p>"""

    faqs = [
        ("ما هي صابونة لتفتيح المنطقة الحساسة من بيزلين 110 جم؟", "هي صابونة طبية طبيعية من بيزلين غنية بصمغ النحل، حجر الشبة واللوميسكين لتفتيح وتعقيم المنطقة الحساسة وموازنة حموضتها 110 جم."),
        ("ما هي فوائد صمغ النحل وحجر الشبة واللوميسكين؟", "يطهر صمغ النحل الشائبات والفطريات، بينما يفتح اللوميسكين وحجر الشبة اسمرار المنطقة الحساسة ب أمان."),
        ("هل توازن الحموضة الفسيولوجية pH للمنطقة الحساسة؟", "نعم، مثبتة في الحفاظ على التوازن الفسيولوجي الطبيعي للمنطقة الحساسة."),
        ("ما حجم وزر قالب الصابونة؟", "تأتي بوزن وافر 110 جم."),
        ("كيف تُستخدم بالشكل الصحيح؟", "افركي الصابونة بين يدين مبللتين لتوليد رغوة، وضعي الرغوة على جلد المنطقة الحساسة واشطفي بالماء الفاتر."),
        ("هل تساعد في تفتيح اسمرار المنطقة الحساسة؟", "نعم، تزيل اسمرار وتصبغات المنطقة الحساسة وتمنحها لوناً موحداً وناصعاً."),
        ("ما هو بلد صنع صابونة بيزلين؟", "صُنع بفخر في لبنان بواسطة مختبرات بيزلين العالمية (Beesline Laboratories)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيزلين لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل تسبب حرقاناً أو تهيجاً؟", "لا، خالية من القلويات القاسية والكحول والبارابين ومناسبة للجلد الرقيق دون حرقان."),
        ("ما هي رائحة صابونة بيزلين للمنطقة الحساسة؟", "تتميز برائحة ناعمة ولطيفة جداً."),
        ("هل تساعد في منع الحكة والرائحة الكريهة؟", "نعم، صمغ النحل وحجر الشبة يقضيان على البكتيريا والفطريات المسببة للرائحة والحكة."),
        ("هل العبوة 110 جم مناسبة للاستخدام اليومي؟", "نعم، قالب وافر يكفي للاستخدام اليومي لعدة أسابيع."),
        ("كيف أحتفظ بالصابونة؟", "تُحفظ في وعاء صابون جاف بعيداً عن تجمع الماء."),
        ("هل تترك ملمساً ناعماً؟", "نعم، تترك جلد المنطقة الحساسة طرياً وناعماً كالحرير."),
        ("هل العبوة غلافها محكم؟", "تأتي في عبوة مغلفة محكمة الحماية."),
        ("هل تناسب الاستخدام أثناء الدورة الشهرية وبعدها؟", "ممتازة جداً للنظافة والتعقيم الفوري أثناء وبعد الدورة الشهرية."),
        ("كم مرة يُفضل استخدامها يومياً؟", "يُفضل استخدامها 1 إلى 2 مرة يومياً."),
        ("هل يناسب النساء والفتيات؟", "مناسبة للفتيات والنساء من سن 12 سنة فما فوق."),
        ("هل تحتوي على بارابين أو كحول؟", "خالية 100% من الكحول والبارابين والكيماويات الضارة."),
        ("هل هي صابونة المنطقة الحساسة الأكثر شهرة لبيزلين؟", "نعم، صابونة بيزلين لتفتيح المنطقة الحساسة الأكثر طلباً بالشرق الأوسط."),
        ("هل تمنح حس نظافة وثقة؟", "نعم، تمنحكِ ثقة ونظافة وانتعاشاً مطلقاً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة بيزلين صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل تمنع الاحتكاك وتسلخات المنطقة الحساسة؟", "نعم، التنعيم والتطهير يمنعان التسلخات والاحتكاك."),
        ("هل تترك الجلد طرياً؟", "نعم، تترك المنطقة الحساسة بطراوة ونعومة."),
        ("هل تتوفّر بسعر ممتاز لدى إكليل أبها؟", "نعم، تتوفّر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Beesline Whitening Sensitive Zone Soap - 110g</strong> is the Middle East's #1 renowned natural clinical intimate soap bar engineered for safe intimate hygiene and underarm/intimate skin whitening. Formulated by Beesline, it fuses antibacterial Propolis, Alum Rock, virgin Olive Oil, natural Lumiskin, and Parsley extract.</p>
<p>Beesline Sensitive Zone Soap maintains the natural physiological pH balance, purifies intimate tissues from odor and itch-causing fungi, and brightens dark hyperpigmentation, leaving your intimate area clean, disinfected, and touchably smooth without drying or burning.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Safe & Natural Intimate Area Whitening:</strong> Brightens dark intimate hyperpigmentation and unifies skin tone.</li>
  <li><strong>Maintains Natural Physiological pH Balance:</strong> Preserves protective intimate flora to prevent fungal infections.</li>
  <li><strong>Antibacterial Sanitization with Propolis & Alum:</strong> Destroys bacteria and yeasts causing odor and itching.</li>
  <li><strong>Nourishing Hydration with Olive Oil & Parsley:</strong> Softens delicate intimate skin and prevents friction.</li>
  <li><strong>100% Alcohol, Soap & Paraben Free:</strong> Gentle, dermatologically tested formulation for feminine safety.</li>
  <li><strong>Generous 110g Soap Bar:</strong> High-value soap bar providing weeks of daily intimate care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Lather):</strong> Rub the Beesline soap bar between wet hands with warm water to create a purifying lather.</li>
  <li><strong>Step 2 (Apply):</strong> Gently apply lather over external intimate skin without harsh scrubbing.</li>
  <li><strong>Step 3 (Rinse):</strong> Rinse thoroughly with warm water and pat dry gently with a towel (use 1 to 2 times daily).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Propolis & Alum Rock:</strong> Sanitize intimate skin tissues and eliminate odor-causing bacteria.</li>
  <li><strong>Lumiskin, Parsley & Olive Oil:</strong> Naturally brighten pigmentation and soften delicate skin.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical intimate skin application only.</li>
  <li>Do not introduce soap lather inside the internal vaginal canal.</li>
  <li>Keep out of reach of children and store in a cool, dry place in a soap dish.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Women seeking the original natural Beesline whitening soap bar for safe intimate area brightening, sanitization, and pH balance.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beesline</td></tr>
  <tr><th>Category</th><td>Personal Care / Natural Intimate Whitening Soap Bars</td></tr>
  <tr><th>Product Type</th><td>pH-Balanced Intimate Whitening Soap Bar (110g)</td></tr>
  <tr><th>Volume/Weight</th><td>110 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Sensitive Intimate Skin</td></tr>
  <tr><th>Finish</th><td>Purified, sanitized, brightened & soft intimate skin</td></tr>
  <tr><th>Texture</th><td>Smooth soap bar generating gentle foam</td></tr>
  <tr><th>Fragrance</th><td>Subtle light fresh natural aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Propolis, Alum Rock, Lumiskin, Parsley Extract, Olive Oil</td></tr>
  <tr><th>Country of Origin</th><td>Lebanon (Beesline Laboratories)</td></tr>
  <tr><th>Manufacturer</th><td>Beesline Laboratories</td></tr>
  <tr><th>Age Group</th><td>Teens & Adult Women (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Propolis Antifungal Shield & Intimate pH Balance</h2>

<h3>What problem does this solve?</h3>
<p>Beesline Sensitive Zone Soap resolves intimate skin hyperpigmentation, odor, itching, and soap drying.</p>

<h3>Why choose Beesline Intimate Soap?</h3>
<p>Propolis destroys Candida fungi naturally without altering protective lactobacilli flora, while Lumiskin brightens dark tissue.</p>"""

    en_faqs = [
        ("What is Beesline Whitening Sensitive Zone Soap - 110g?", "It is a natural clinical intimate soap bar enriched with Propolis, Alum Rock, and Lumiskin to brighten, sanitize, and balance intimate pH."),
        ("What are the benefits of Propolis, Alum Rock, and Lumiskin?", "Propolis sanitizes bacteria and fungi, while Lumiskin and Alum Rock naturally brighten intimate hyperpigmentation."),
        ("Does it maintain natural physiological pH balance?", "Yes, clinically proven to preserve the delicate protective intimate pH balance."),
        ("What weight is contained in this soap bar?", "It comes as a generous 110g soap bar."),
        ("How do I use it correctly?", "Lather between wet hands, apply lather gently over external intimate skin, and rinse thoroughly with warm water."),
        ("Does it brighten dark intimate skin?", "Yes, clears dark intimate hyperpigmentation and unifies skin tone visibly."),
        ("Where is Beesline Intimate Soap manufactured?", "It is proudly manufactured in Lebanon by Beesline Laboratories."),
        ("How do I verify authenticity at Ekleel Abha?", "All Beesline products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it cause burning or irritation?", "No, free of harsh alkalis, alcohol, and parabens; safe for delicate intimate skin."),
        ("What scent does Beesline Intimate Soap have?", "Features a light, pleasant subtle fresh scent."),
        ("Does it prevent intimate itching and odor?", "Yes, Propolis and Alum Rock destroy bacteria and yeasts causing odor and itching."),
        ("Is the 110g soap bar economical?", "Yes, generous soap bar lasts through weeks of daily intimate care."),
        ("How should I store the soap bar?", "Store in a dry soap dish away from standing water."),
        ("Does it leave intimate skin touchably soft?", "Yes, leaves intimate skin touchably soft, smooth, and clean."),
        ("Is the packaging securely sealed?", "Yes, comes in a securely wrapped protective box."),
        ("Is it great for period hygiene care?", "Yes, essential for instant hygiene and sanitization during and post-menstruation."),
        ("How many times daily should I use it?", "Recommended for use 1 to 2 times daily."),
        ("Is it safe for teens and women?", "Suitable for teens and adult women aged 12+."),
        ("Is it free of parabens and alcohol?", "Yes, 100% free of alcohol, parabens, and harsh chemicals."),
        ("Is it Beesline's top-selling intimate soap bar?", "Yes, Beesline Whitening Sensitive Zone Soap is the #1 trusted intimate soap in the Middle East."),
        ("Does it provide all-day intimate confidence?", "Yes, guarantees fresh, disinfected, and bright intimate confidence."),
        ("Is the packaging recyclable?", "Yes, 100% recyclable environmentally friendly box."),
        ("Does it prevent intimate friction?", "Yes, softening and sanitizing formula prevents skin chafing."),
        ("Does it leave skin touchably soft?", "Yes, leaves intimate skin supple and comfortable."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1848",
        "sku": "EK-1848",
        "gtin": "5281018003220",
        "category": "العناية الشخصية / صابون ومستحضرات تفتيح المنطقة الحساسة الطبيعية",
        "brand": "Beesline",
        "ar": {
            "title": "صابونة لتفتيح المنطقة الحساسة من بيزلين 110 جم",
            "meta_title": "صابونة بيزلين للمنطقة الحساسة 110جم | إكليل أبها",
            "meta_description": "اشتري صابونة لتفتيح المنطقة الحساسة من بيزلين (110 جم). صابونة طبية بصمغ النحل واللوميسكين لتفتيح وتطهير المنطقة الحساسة وموازنة الـ pH. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بيزلين", "صابونة_بيزلين", "المنطقة_الحساسة", "تفتيح_المنطقة_الحساسة", "إكليل_أبها"]
        },
        "en": {
            "title": "Beesline Whitening Sensitive Zone Soap - 110g",
            "meta_title": "Beesline Sensitive Zone Soap 110g | Ekleel Abha",
            "meta_description": "Buy original Beesline Whitening Sensitive Zone Soap (110g). Natural Propolis & Lumiskin intimate whitening soap bar. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["beesline", "beesline_soap", "sensitive_zone_soap", "intimate_whitening", "ekleel_abha"]
        },
        "schema": {
            "brand": "Beesline",
            "category": "Personal Care / Intimate Soap",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "beesline-whitening-sensitive-zone-soap-110g.webp",
            "alt": "Beesline Whitening Sensitive Zone Soap 110g",
            "title": "Beesline Whitening Sensitive Zone Soap 110g"
        }
    }

def create_product_1850():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم مرطب نيفيا سوفت - 100 مل (Nivea Soft Moisturizing Cream 100ml)</strong> المستحضر الأيقوني الأكثر انتعاشاً وشهرة عالمياً لترطيب الوجه، الجسم، واليدين بتركيبة فائقة الخفة سريعة الامتصاص. يرتكز هذا الكريم الفريد من نيفيا (Nivea Soft Refreshing Soft Cream) على زيت الجوجوبا الطبيعي (Jojoba Oil) وفيتامين E المقاوم للجفاف.</p>
<p>يمتاز كريم نيفيا سوفت بقوام جل مائي خفيف يذوب بالبشرة فورياً، حيث يمنحكِ ترطيباً مكثفاً لـ 24 ساعة دون إبقاء أي أثر دهني لزج، ليترك بشرة وجهكِ وجسمكِ طرية، منعشة، ومفعمة بالحيوية والحماية طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتنعيم فائق الخفة لـ 24 ساعة:</strong> ينفذ فورياً بالبشرة لمنح ترطيب مائي منعش.</li>
  <li><strong>غني بزيت الجوجوبا وفيتامين E:</strong> يغذي ألياف الجلد ويحميه من الجفاف والتأثيرات البيئية.</li>
  <li><strong>استخدام متعدد 3 في 1 (الوجه، الجسم، اليدين):</strong> فورمولا خفيفة ومثالية لكل أجزاء البشرة.</li>
  <li><strong>امتصاص سريع فور لمس البشرة:</strong> يذوب بالجلد دون ترك أي لزوجة أو بقايا زيتية ثقيلة.</li>
  <li><strong>مجرب جلدياً لجميع أنواع البشرة:</strong> تركيبة دقيقة وآمنة للبشرة العادية، الجافة، والحساسة.</li>
  <li><strong>عبوة مدمجة سعة 100 مل:</strong> حجم ممتاز ومناسب للاستخدام اليومي والسفر وحقيبة اليد.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> وضعي الكريم على بشرة الوجه، اليدين، أو الجسم بعد الغسيل أو الاستحمام.</li>
  <li><strong>الخطوة الثانية (التدليك):</strong> دلكي برفق بحركات دائرية حتى امتصاص الكريم بالكامل.</li>
  <li><strong>الخطوة الثالثة (التكرار):</strong> كرري التطبيق عند الحاجة للانتعاش والترطيب طوال اليوم.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زيت الجوجوبا الطبيعي (Jojoba Oil):</strong> يغذي ألياف البشرة ويحفظ ترطيبها الطبيعي.</li>
  <li><strong>فيتامين E والمرطبات المائية (Vitamin E):</strong> يحميان الجلد من الجفاف ويرممان الحيوية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على الوجه والجسم واليدين فقط.</li>
  <li>تجنبي ملامسة الكريم المباشرة لداخل العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن كريم نيفيا سوفت الأبيض الأيقوني لترطيب الوجه والجسم بسرعة وانتعاش دون لزوجة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>نيفيا (Nivea Soft)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات نيفيا المنعشة لترطيب الوجه والجسم واليدين</td></tr>
  <tr><th>نوع المنتج</th><td>كريم مرطب ناعم وفائق الخفة بزيت الجوجوبا وفيتامين E (100ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (العادية، الجافة، والحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة مرطبة عميقاً، ناعمة كالحرير، خفيفة ومفعمة بالانتعاش دون لزوجة</td></tr>
  <tr><th>الملمس</th><td>كريم مائي ناعم خفيف يمتص فورياً</td></tr>
  <tr><th>العطر</th><td>عطر نيفيا المنعش الخفيف الأيقوني</td></tr>
  <tr><th>المكونات النشطة</th><td>زيت الجوجوبا، فيتامين E، مرطبات نيفيا المائية</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا (Beiersdorf Germany)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beiersdorf (نيفيا)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد زيت الجوجوبا وفيتامين E في نيفيا سوفت (Nivea Soft)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم نيفيا سوفت مشكلة جفاف وشحوب الوجه واليدين، وثقل كريمات الترطيب الزيتية التقليدية.</p>

<h3>لماذا تنجح تركيبة نيفيا سوفت؟</h3>
<p>لأن زيت الجوجوبا يمتلك بنية شمعية تماثل دهون البشرة الطبيعية (Sebum)، فيمتص فورياً ويغذي دون سد المسام.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق اليومي بعد الاستحمام:</strong> استعمليه على بشرة الوجه والجسم فور الاستحمام لحبس المياه.<br>
2. <strong>ترطيب اليدين بعد الغسيل:</strong> ابقي العبوة 100 مل بحقيبتكِ لترطيب اليدين بعد الصابون.<br>
3. <strong>المرطب الخفيف قبل المكياج:</strong> ممتاز جداً ككريم مرطب ومهيئ سريع للوجه قبل الفاونديشن.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "كريمات الترطيب الخفيفة لا تحمي البشرة من الجفاف الشديد."<br>
<strong>الحقيقة:</strong> نيفيا سوفت يجمع بين الخفة والترطيب المكثف لـ 24 ساعة بفضل فيتامين E والجوجوبا.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتحد جزيئات الجوجوبا وفيتامين E مع خلايا الطبقة القرنية، فتصلح حاجز البشرة الواقي وتمنع التبخر الجلدي.</p>"""

    faqs = [
        ("ما هو كريم مرطب نيفيا سوفت 100 مل؟", "هو كريم مرطب أيقوني خفيف بزيت الجوجوبا وفيتامين E لترطيب الوجه والجسم واليدين بسرعة وانتعاش سعة 100 مل."),
        ("ما هي فوائد زيت الجوجوبا وفيتامين E؟", "يغذي زيت الجوجوبا البشرة ويطريها، بينما يحمي فيتامين E من الجفاف والتأثيرات البيئية."),
        ("هل يضمن ترطيباً لـ 24 ساعة دون لزوجة؟", "نعم، مثبت سريرياً في منح ترطيب وانتعاش يدوم لـ 24 ساعة دون أي أثر دهني لزج."),
        ("ما حجم العبوة؟", "تأتي بحجم 100 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وضعي كمية على بشرة الوجه، اليدين، أو الجسم، ودلكي برفق حتى الامتصاص الكامل عند الحاجة."),
        ("هل يناسب الوجه والجسم واليدين معاً؟", "نعم، كريم 3 في 1 فائق الخفة يناسب جميع أجزاء البشرة."),
        ("ما هو بلد صنع نيفيا سوفت؟", "صُنع بفخر في ألمانيا بواسطة شركة بايرسدورف (Beiersdorf)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات نيفيا لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل يمتص بسرعة فور لمس البشرة؟", "نعم، قوام مائي يذوب ويمتص بالبشرة فورياً."),
        ("ما هي رائحة كريم نيفيا سوفت؟", "يتميز برائحة نيفيا المنعشة والأيقونية الخفيفة."),
        ("هل يناسب جميع أنواع البشرة؟", "مناسب للبشرة العادية، الجافة، والمختلطة."),
        ("هل العبوة 100 مل مناسبة للحقيبة والسفر؟", "نعم، حجم مدمج وأنيق مثالي لحمل الحقيبة والسفر."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعيداً عن الشمس."),
        ("هل يمكن استخدامه كقاعدة للمكياج؟", "نعم، ممتاز ككريم مرطب ومهيئ سريع للوجه قبل الفاونديشن."),
        ("هل العبوة محكمة الغلق؟", "تأتي في عبوة دائرية بغطاء لولبي محكم الحماية."),
        ("هل يمنع جفاف الأيدي بالصيف والشتاء؟", "نعم، مرطب ممتاز لمنع جفاف وخشونة اليدين."),
        ("كم مرة يُفضل استخدامه يومياً؟", "يُستعمل عند الحاجة طوال اليوم."),
        ("هل يناسب جميع أفراد العائلة؟", "مناسب للأطفال والبالغين من سن 3 سنوات فما فوق."),
        ("هل يمنع انسداد المسام؟", "نعم، تركيبة خفيفة لا تسد مسام الوجه."),
        ("هل هو الكريم المرطب الأقوى والأشهر لنيفيا؟", "نعم، نيفيا سوفت الأبيض الأكثر مبيعاً وشهرة عالمياً."),
        ("هل يمنح حس نضارة وانتعاش؟", "نعم، يمنح بشرتكِ نضارة وانتعاشاً فورياً."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير."),
        ("هل يترك ملمساً حريرياً؟", "نعم، يترك البشرة طرية ومخملية كالحرير."),
        ("هل يمنع القشور والتطير؟", "نعم، يقضي على القشور والتطير الجلدي."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Nivea Soft Moisturizing Cream 100ml</strong> (Nivea Soft Refreshing Soft Cream) is the world's iconic, most refreshing all-in-one moisturizing cream engineered to hydrate face, body, and hands with an ultra-light, fast-absorbing matrix. Formulated by Nivea, it blends natural Jojoba Oil with Vitamin E.</p>
<p>Nivea Soft features a feather-light hydra-gel texture that melts instantly into skin, providing deep 24-hour hydration without leaving any greasy film, leaving face, hands, and body touchably soft, refreshed, and vibrant all day long.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>24-Hour Ultra-Light Hydration & Softness:</strong> Absorbs instantly into skin for a refreshing burst of moisture.</li>
  <li><strong>Enriched with Jojoba Oil & Vitamin E:</strong> Nourishes skin fibers and guards against environmental drying.</li>
  <li><strong>Versatile 3-in-1 Application (Face, Body, Hands):</strong> Light formula suitable for all skin areas.</li>
  <li><strong>Fast Absorbing Upon Skin Contact:</strong> Melts into skin with zero sticky or heavy greasy residue.</li>
  <li><strong>Dermatologically Tested for All Skin Types:</strong> Safe formulation for normal, dry, and sensitive skin.</li>
  <li><strong>Compact 100ml Tub:</strong> Ideal handbag, travel kit, and daily grooming size.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Apply Nivea Soft cream onto clean face, hands, or body skin after showering or washing.</li>
  <li><strong>Step 2 (Massage):</strong> Massage gently in circular motions until completely absorbed.</li>
  <li><strong>Step 3 (Repeat):</strong> Reapply throughout the day as needed for instant refreshing hydration.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Jojoba Oil:</strong> Nourishes skin fibers and preserves essential skin lipids.</li>
  <li><strong>Vitamin E & Hydra-Moisturisers:</strong> Shield skin from drying out and restore suppleness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial, body, and hand moisturizing application only.</li>
  <li>Avoid direct contact with the interior of the eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking the iconic white Nivea Soft refreshing moisturizing cream for face, hands, and body without greasy weight.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Nivea (Nivea Soft)</td></tr>
  <tr><th>Category</th><td>Skincare / Refreshing All-in-One Face, Body & Hand Creams</td></tr>
  <tr><th>Product Type</th><td>Ultra-Light Refreshing Soft Cream (100ml)</td></tr>
  <tr><th>Volume/Weight</th><td>100 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Normal, Dry & Sensitive)</td></tr>
  <tr><th>Finish</th><td>Deeply hydrated, touchably soft, refreshed & non-greasy skin</td></tr>
  <tr><th>Texture</th><td>Ultra-light fast-absorbing hydra-cream</td></tr>
  <tr><th>Fragrance</th><td>Iconic fresh Nivea scent</td></tr>
  <tr><th>Active Ingredients</th><td>Jojoba Oil, Vitamin E, Hydra-Moisturisers</td></tr>
  <tr><th>Country of Origin</th><td>Germany (Beiersdorf Germany)</td></tr>
  <tr><th>Manufacturer</th><td>Beiersdorf (Nivea)</td></tr>
  <tr><th>Age Group</th><td>All Ages (3+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Jojoba Lipid Affinity & Vitamin E Hydration</h2>

<h3>What problem does this solve?</h3>
<p>Nivea Soft Moisturizing Cream resolves facial and hand dryness, dullness, and heavy cream lamination.</p>

<h3>Why choose Nivea Soft?</h3>
<p>Jojoba Oil closely mirrors natural skin sebum, allowing rapid absorption while Vitamin E locks in 24-hour hydration.</p>"""

    en_faqs = [
        ("What is Nivea Soft Moisturizing Cream 100ml?", "It is an iconic ultra-light moisturizing cream enriched with Jojoba Oil and Vitamin E for fast face, body, and hand hydration."),
        ("What are the benefits of Jojoba Oil and Vitamin E?", "Jojoba Oil nourishes and softens skin, while Vitamin E protects against dryness and environmental stress."),
        ("Does it provide 24-hour hydration without grease?", "Yes, clinically proven to deliver 24-hour refreshing hydration with zero greasy film."),
        ("What volume is contained in this tub?", "It comes in a compact 100ml tub."),
        ("How do I apply it correctly?", "Apply to clean face, hands, or body skin and massage gently until absorbed whenever needed."),
        ("Is it suitable for face, body, and hands?", "Yes, versatile 3-in-1 ultra-light cream suitable for face, hands, and body."),
        ("Where is Nivea Soft manufactured?", "It is proudly manufactured in Germany by Beiersdorf."),
        ("How do I verify authenticity at Ekleel Abha?", "All Nivea products at Ekleel Abha are 100% original from certified distributors."),
        ("Does it absorb quickly upon contact?", "Yes, hydra-cream matrix melts and absorbs into skin instantly."),
        ("What scent does Nivea Soft have?", "Features the iconic, light, fresh Nivea fragrance."),
        ("Is it suitable for all skin types?", "Ideal for normal, dry, and combination skin types."),
        ("Is the 100ml tub travel-friendly?", "Yes, compact tub size fits easily into handbags and travel kits."),
        ("How should I store the tub?", "Store in a cool, dry place away from direct heat."),
        ("Can it be used as a makeup primer?", "Yes, functions as a fast-absorbing lightweight primer before foundation."),
        ("Is the tub securely sealed?", "Yes, comes in a sleek tub with a tight screw-top lid."),
        ("Does it prevent dry hands year-round?", "Yes, excellent for preventing hand dryness in summer and winter."),
        ("How often can I use it daily?", "Use throughout the day as needed for refreshing moisture."),
        ("Is it safe for family use?", "Safe for adults and children aged 3+."),
        ("Does it prevent clogged pores?", "Yes, lightweight non-comedogenic formula will not clog pores."),
        ("Is Nivea Soft Nivea's best-selling cream?", "Yes, iconic white Nivea Soft is globally celebrated #1 soft cream."),
        ("Does it give skin an instant fresh glow?", "Yes, bestows instant hydration and fresh skin suppleness."),
        ("Is the tub recyclable?", "Yes, 100% recyclable environmentally friendly tub."),
        ("Does it leave skin touchably silky?", "Yes, leaves skin touchably soft, smooth, and supple."),
        ("Does it eliminate skin flaking?", "Yes, completely clears dry flaking patches and skin tightness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1850",
        "sku": "EK-1850",
        "gtin": "4005808890590",
        "category": "العناية بالبشرة / كريمات نيفيا المنعشة لترطيب الوجه والجسم واليدين",
        "brand": "Nivea",
        "ar": {
            "title": "كريم مرطب نيفيا سوفت 100 مل",
            "meta_title": "كريم نيفيا سوفت 100مل | صيدلية إكليل أبها",
            "meta_description": "اشتري كريم مرطب نيفيا سوفت (100 مل). كريم مرطب أيقوني بزيت الجوجوبا وفيتامين E للوجه والجسم. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["نيفيا", "نيفيا_سوفت", "كريم_نيفيا", "ترطيب_الوجه", "إكليل_أبها"]
        },
        "en": {
            "title": "Nivea Soft Moisturizing Cream 100ml",
            "meta_title": "Nivea Soft Moisturizing Cream 100ml | Ekleel Abha",
            "meta_description": "Buy original Nivea Soft Moisturizing Cream (100ml). Iconic Jojoba Oil & Vitamin E face, body & hand moisturizer. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["nivea", "nivea_soft", "moisturizing_cream", "jojoba_oil", "ekleel_abha"]
        },
        "schema": {
            "brand": "Nivea",
            "category": "Skincare / Body Cream",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "nivea-soft-moisturizing-cream-100ml.webp",
            "alt": "Nivea Soft Moisturizing Cream 100ml",
            "title": "Nivea Soft Moisturizing Cream 100ml"
        }
    }

print("Loaded Batch 28 builders")
