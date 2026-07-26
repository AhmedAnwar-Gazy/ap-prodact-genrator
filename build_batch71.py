import json, os

def create_product_2071():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول الوجه للبشرة الدهنية من لاروش بوزيه 400مل (La Roche-Posay Effaclar Gel Facial Wash for Oily Skin - 400ml)</strong> الجل المنظف الطبي الفاخر الأكثر توصية عالمياً من لاروش بوزيه المصمم خصيصاً لتنظيف، تنقية، وتصفية المسام للبشرة الدهنية والحساسة والمعرضة للحبوب والبثور. يرتكز هذا الغسول الأصيل (Effaclar Gel 400ml) على مياه لاروش بوزيه الحرارية المهدئة (Thermal Spring Water)، زنك PCA المنظم للدهون، والمنظفات اللطيفة متوازنة الحموضة (pH 5.5).</p>
<p>يعمل غسول إيفاكلار من لاروش بوزيه على تنظيف مسام الوجه عمقاً من الدهون المتراكمة والشوائب، تقليل اللمعان الزائد، وتهدئة التهيجات ومنع تكون البثور، ليترك بشرة وجهك ناعمة كالحرير، ناصعة النظافة، منتعشة، ومحمية من التضرر من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف وتصفية فائقة للدهون والشوائب:</strong> ينظف المسام بفاعلية دون تجريد البشرة أو تسبيب جفاف.</li>
  <li><strong>تنظيم إفراز الدهون وتقليل اللمعان بالزنك PCA:</strong> يقلل الزيوت الزائدة واللمعان الدهني طوال اليوم.</li>
  <li><strong>تهدئة الاحمرار والتهيج بمياه لاروش الحرارية:</strong> تلطف البشرة الحساسة المعرضة لحب الشباب.</li>
  <li><strong>تركيبة خالية من الصابون، الكحول، والعطور القاسية (pH 5.5):</strong> تحافظ على التوازن البيولوجي للجلد.</li>
  <li><strong>مختبر على البشرة المعرضة للحبوب وغير مسبب للانسداد:</strong> Non-Comedogenic.</li>
  <li><strong>عبوة ضخمة اقتصادية سعة 400 مل مزودة بضاغط:</strong> حجم ممتاز للاستخدام العائلي اليومي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الوجه بالماء الدافئ.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسية من جل إيفاكلار وكوّني رغوة ناعمة ودلكي الوجه برفق بحركات دائرية.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء الدافئ وجففي الوجه برفق (يُستعمل مرتين يومياً صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زنك PCA (Zinc PCA):</strong> ينظم إفراز الدهون وله خواص مطهرة تقضي على بكتيريا الحبوب.</li>
  <li><strong>مياه لاروش بوزيه الحرارية والمنظفات اللطيفة:</strong> تهدي التهيجات وتحفظ الرطوبة الداخلية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يملك بشرة دهنية أو حساسة أو معرضة للحبوب ويبحث عن غسول إيفاكلار 400 مل لتنظيف وتصفية الوجه.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لاروش بوزيه (La Roche-Posay Effaclar)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / غسولات إيفاكلار الطبية للبشرة الدهنية 400ml</td></tr>
  <tr><th>نوع المنتج</th><td>جل غسول طبي مصفٍ للدهون بالزنك PCA ومياه لاروش الحرارية (400ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>400 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الدهنية، الحساسة، المختلطة والمعرضة لحب الشباب</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، مرطب، مطهر، ناصع النظافة وغير لامع بالدهون</td></tr>
  <tr><th>الملمس</th><td>جل سائل شفاف رغوي ناعم ينشطف بالماء بسهولة</td></tr>
  <tr><th>العطر</th><td>عطر طبي خفيف جداً ناعم</td></tr>
  <tr><th>المكونات النشطة</th><td>زنك PCA، مياه لاروش بوزيه الحرارية، منظفات متوازنة pH 5.5</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>La Roche-Posay Laboratoire Dermatologique (L'Oréal)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الزنك PCA ومياه لاروش الحرارية في غسول إيفاكلار (Effaclar Gel)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول إيفاكلار مشكلة الإفرازات الدهنية الزائدة، لمعان الوجه، انسداد المسام، وتكون البثور والحبوب.</p>

<h3>لماذا تنجح تركيبة Effaclar Foaming Gel؟</h3>
<p>لأن الزنك PCA ينظم نشاط الغدد الدهنية بينما تمنع مياه لاروش الحرارية تهيج الحواجز الجسدية بالجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنظيف مرتين يومياً بالماء الدافئ:</strong> ينظف المسام من الأكسدة الدهنية.<br>
2. <strong>التكميل بمرطب إيفاكلار أو مرطب طبي خالي من الزيوت:</strong> يحفظ الترطيب الداخلي.<br>
3. <strong>تجنب الصابون القاسي:</strong> يمنع نكسات زيادة إفراز الدهون.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "غسولات البشرة الدهنية يجب أن تسبب شد وجفاف الوجه."<br>
<strong>الحقيقة:</strong> غسول إيفاكلار مصمم بدرجة حموضة pH 5.5 ليمنح تنظيفاً ناصعاً دون تجفيف البشرة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يخلّب الزنك PCA الأحماض الدهنية الحرة على الجلد بينما تطهر ميكروسيليلار المنظفات المسام بفعالية.</p>"""

    faqs = [
        ("ما هو غسول الوجه للبشرة الدهنية من لاروش بوزيه 400مل؟", "هو جل غسول طبي مصفٍ للدهون من لاروش بوزيه بالزنك PCA والمياه الحرارية للبشرة الدهنية والحساسة (400 مل)."),
        ("ما هي فوائد الزنك PCA ومياه لاروش الحرارية للبشرة الدهنية؟", "ينظم الزنك إفراز الدهون ويهدئ البثور، بينما تطهر المياه الحرارية وتلطف البشرة الحساسة."),
        ("هل ينظف المسام ويقلل الدهون بدون جفاف؟", "نعم، مثبت سريرياً في تنظيف المسام وتقليل الدهون دون تسبيب شد أو جفاف بالوجه."),
        ("ما حجم العبوة؟", "تأتي بعبوة ضخمة مزودة بضاغط مريح سعة 400 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الوجه، ضعي كمية وكوّني رغوة، دلكي برفق واشطفي بالماء مرتين يومياً."),
        ("هل هو خالٍ من الصابون والكحول والبارابين؟", "نعم، 100% خالٍ من الصابون والكحول والبارابين ومختبر درماتولوجياً."),
        ("أين صُنع غسول لاروش بوزيه إيفاكلار؟", "صُنع في فرنسا بواسطة La Roche-Posay Laboratoire Dermatologique."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات لاروش بوزيه لدى إكليل أبها أصلية 100%."),
        ("هل يناسب البشرة الدهنية والحساسة والمكونة للبثور؟", "نعم، ممتاز للبشرة الدهنية، الحساسة، المختلطة والمعرضة للحبوب."),
        ("هل يترك الوجه غير لامع بالدهون ومشرقاً؟", "نعم، يترك الوجه غير لامع بالدهون ونظيراً وناعماً كالحرير."),
        ("هل عبوة 400 مل بضاغط مريحة؟", "نعم، عبوة ضخمة بضاغط مريح جداً للاستخدام اليومي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل لاروش بوزيه الماركة الأولى الموصى بها من أطباء الجلدية؟", "نعم، La Roche-Posay الماركة رقم 1 الموصى بها طبياً في أوروبا والعالم."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل يزيل الدهون والمكياج والأوساخ؟", "نعم، يزيل الزيوت الزائدة والمكياج اليومي والشوائب بفاعلية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في تقليل الحبوب والبثور؟", "نعم، ينظف المسام ويقلل تكون الحبوب والبثور الدهنية."),
        ("هل يسبب انسداد المسام؟", "لا، تركيبة خالية من الزيوت وغير مسببة للانسداد (Non-Comedogenic)."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يفضل اتباع مرطب خفيف بعده؟", "نعم، يُفضل استخدام مرطب خفيف خالي من الزيوت بعد الغسل."),
        ("هل يناسب الصيف والشتاء؟", "نعم، ممتاز لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج طبي فاخر وأساسي لكل روتين عناية."),
        ("هل يعيد المظهر الصافي النقي للوجه؟", "نعم، يمنح الوجه مظهراً ناصع النقاء."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>La Roche-Posay Effaclar Gel Facial Wash for Oily Skin - 400ml</strong> is the world's most dermatologist-recommended authentic luxury medical purifying gel cleanser from La Roche-Posay designed to clean, clarify, and clear pores for oily, sensitive, and acne-prone facial skin without dryness, irritation, or barrier damage. Built upon soothing La Roche-Posay Thermal Spring Water, sebum-regulating Zinc PCA, and pH-balanced mild cleansing agents (pH 5.5).</p>
<p>La Roche-Posay Effaclar Gel deeply purifies facial pores of excess sebum and impurities, reduces oily shine, and calms redness preventing breakouts, leaving your facial skin touchably silky soft, spotlessly clean, refreshed, and protected from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Superior Purifying Cleansing for Oil & Sebum Control:</strong> Cleanses pores effectively without drying skin.</li>
  <li><strong>Sebum Production Regulation & Shine Reduction with Zinc PCA:</strong> Controls excess oil throughout the day.</li>
  <li><strong>Soothing Care for Sensitive Skin with Thermal Spring Water:</strong> Calms redness and irritation in acne-prone skin.</li>
  <li><strong>Soap-Free, Alcohol-Free & Paraben-Free Formula (pH 5.5):</strong> Maintains the natural biological balance of skin.</li>
  <li><strong>Dermatologically Tested Non-Comedogenic Formula:</strong> Will not clog pores or cause breakouts.</li>
  <li><strong>Generous 400ml Family Value Pump Bottle:</strong> Excellent size for daily continuous family use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet facial skin with warm water.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of Effaclar gel, work into a gentle lather, and massage face in circular motions.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and pat face dry (use twice daily morning & night).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Zinc PCA:</strong> Regulates sebum production while offering antibacterial properties against acne bacteria.</li>
  <li><strong>La Roche-Posay Thermal Spring Water & Mild Cleansers:</strong> Calm irritation while preserving internal hydration.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial skin application.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with oily, sensitive, or acne-prone skin seeking La Roche-Posay Effaclar Gel 400ml for pore purifying and oil control.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>La Roche-Posay (Effaclar)</td></tr>
  <tr><th>Category</th><td>Skincare / La Roche-Posay Effaclar Medical Cleansers 400ml</td></tr>
  <tr><th>Product Type</th><td>Zinc PCA & Thermal Water Purifying Medical Gel Cleanser (400ml)</td></tr>
  <tr><th>Volume/Weight</th><td>400 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Oily, Sensitive, Combination & Acne-Prone Skin</td></tr>
  <tr><th>Finish</th><td>Spotlessly clean, 24H hydrated, purified & matte silky soft face</td></tr>
  <tr><th>Texture</th><td>Clear liquid gel transforming into a gentle smooth lather</td></tr>
  <tr><th>Fragrance</th><td>Ultra-light mild pleasant scent</td></tr>
  <tr><th>Active Ingredients</th><td>Zinc PCA, La Roche-Posay Thermal Spring Water, Mild Cleansers (pH 5.5)</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>La Roche-Posay Laboratoire Dermatologique (L'Oréal)</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Zinc PCA Sebum Regulation & Thermal Water Anti-Inflammatory Action</h2>

<h3>What problem does this solve?</h3>
<p>Effaclar Gel resolves excess sebum secretion, facial oil shine, clogged pores, comedones, and acne breakouts.</p>

<h3>Why choose Effaclar Gel?</h3>
<p>Zinc PCA regulates sebaceous gland activity while La Roche-Posay Thermal Spring Water protects sensitive skin against irritation.</p>"""

    en_faqs = [
        ("What is La Roche-Posay Effaclar Gel Facial Wash for Oily Skin - 400ml?", "It is a medical purifying gel cleanser from La Roche-Posay with Zinc PCA and Thermal Water for oily and sensitive skin (400ml)."),
        ("What are the benefits of Zinc PCA and Thermal Spring Water?", "Zinc PCA regulates oil and prevents breakouts, while Thermal Spring Water soothes sensitive skin."),
        ("Does it clean pores and control oil shine without dryness?", "Yes, clinically proven to clean pores and reduce excess shine without tightness or dryness."),
        ("What volume is contained in this bottle?", "400ml pump dispenser bottle."),
        ("How do I use it correctly?", "Wet face, apply gel, lather, massage gently and rinse with warm water twice daily."),
        ("Is it soap-free, alcohol-free, and paraben-free?", "Yes, 100% free from soap, alcohol, and parabens, and dermatologically tested."),
        ("Where is La Roche-Posay Effaclar Gel manufactured?", "In France by La Roche-Posay Laboratoire Dermatologique."),
        ("How do I verify authenticity at Ekleel Abha?", "All La Roche-Posay products at Ekleel Abha are 100% original."),
        ("Is it suitable for oily, sensitive, and acne-prone skin?", "Yes, excellent for oily, sensitive, combination, and acne-prone skin."),
        ("Does it leave face matte and clean?", "Yes, leaves face matte, oil-free, spotlessly clean, and silky soft."),
        ("Is the 400ml pump bottle convenient?", "Yes, generous pump dispenser bottle ideal for daily family use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is La Roche-Posay the #1 dermatologist recommended brand?", "Yes, La Roche-Posay is the #1 dermatologist recommended skincare brand globally."),
        ("How many times daily?", "Twice daily (morning and night)."),
        ("Does it remove excess oil and makeup?", "Yes, effectively cleanses excess oil, light makeup, and daily impurities."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help reduce acne and pimples?", "Yes, cleanses pores reducing acne formation and pimples."),
        ("Does it clog pores?", "No, oil-free non-comedogenic formula."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is following with an oil-free moisturizer recommended?", "Yes, follow with a lightweight oil-free moisturizer after cleansing."),
        ("Is it good for all seasons?", "Yes, ideal oil-control cleansing for summer and winter."),
        ("Is it a nice skincare gift?", "Yes, a premier medical essential for facial care routines."),
        ("Does it restore clean radiant skin appearance?", "Yes, gives facial skin a clear healthy radiant look."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2071",
        "sku": "EK-2071",
        "gtin": "3337872411991",
        "brand": "La Roche-Posay",
        "ar": {
            "title": "غسول الوجه للبشرة الدهنية من لاروش بوزيه 400مل",
            "meta_title": "غسول لاروش بوزيه إيفاكلار للبشرة الدهنية 400مل | إكليل أبها",
            "meta_description": "اشتري غسول الوجه للبشرة الدهنية إيفاكلار من لاروش بوزيه (400 مل). جل طبي مصفٍ بالزنك PCA والمياه الحرارية لتنظيف المسام وتقليل الدهون. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["لاروش_بوزيه", "إيفاكلار_جل", "غسول_البشرة_الدهنية", "زنك_PCA", "إكليل_أبها"]
        },
        "en": {
            "title": "La Roche-Posay Effaclar Gel Facial Wash for Oily Skin - 400ml",
            "meta_title": "La Roche-Posay Effaclar Gel Cleanser 400ml | Ekleel Abha",
            "meta_description": "Buy original La Roche-Posay Effaclar Gel Facial Wash for Oily Skin (400ml). Zinc PCA medical purifying gel cleanser. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["la_roche_posay", "effaclar_gel", "oily_skin_cleanser", "zinc_pca_wash", "ekleel_abha"]
        }
    }


def _make_jayjun_eye_patches_b71(pid, gtin, ar_name, en_name, ing_ar, ing_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>{ar_name}</strong> لصقات هيدروجيل العناية بالعين الفاخرة الكورية الأيقونية الأصيلة من جيجون (Jayjun) المصممة خصيصاً لتفتيح الهالات السوداء، تقليل الانتفاخات والخطوط الدقيقة، وترطيب وتنعيم محيط العين الحساس. تركز هذه اللصقات الأصيلة ({en_name}) على خلاصات {ing_ar}، حمض الهيالورونيك، النياسيناميد المفتّح، وأدينوسين محاربة التجاعيد.</p>
<p>تعمل لصقات جل جيجون على تبريد وتلطيف منطقة أسفل العين، تزويد الجلد بتغذية مائية مكثفة، وتصفية الهالات الداكنة، لتترك محيط عينيك ناعماً كالحرير، ناضراً، مشرقاً، ومفعماً بالشباب والحيوية من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح الهالات السوداء وتوحيد لون محيط العين بـ {ing_ar}:</strong> يقلل التصبغات والإجهاد.</li>
  <li><strong>تقليل الانتفاخات والخطوط الدقيقة فورياً:</strong> يبرد ويرطب الجلد الرقيق بفعالية.</li>
  <li><strong>ترطيب وتغذية مائية مكثفة بتقنية الهيدروجيل:</strong> تنفذ المواد المغذية لعمق خلايا الجلد.</li>
  <li><strong>تحسين مرونة وملمس البشرة بالأدينوسين:</strong> يقاوم مظاهر الشيخوخة والتجعد.</li>
  <li><strong>عبوة تحتوي على 60 لاصقة مع ملعقة تطبيق مريحة:</strong> تكفي 30 استخداماً للعينين.</li>
  <li><strong>صناعة كورية فاخرة آمنة على العينين:</strong> مختبرة جلدياً ومناسبة للبشرة الحساسة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> نظفي بشرة الوجه ومحيط العينين ورطبيهما بالتونر.</li>
  <li><strong>الخطوة الثانية:</strong> استخدمي الملعقة المرفقة لرفع لصقتين وضعهما أسفل العينين برفق.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركيهما لمدة 20-30 دقيقة، ثم أزيلي اللصقات وطبطبي السيروم المتبقي حتى الامتصاص (يُستعمل 2-3 مرات أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصات {ing_ar} والنياسيناميد:</strong> تفتحان التصبغات وتصفيان الهالات السوداء.</li>
  <li><strong>حمض الهيالورونيك والأدينوسين:</strong> يشدان المنطقة ويحبسان الترطيب الداخلي.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على محيط العينين.</li>
  <li>تجنبي دخول السيروم المباشر داخل العين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لتفتيح الهالات السوداء وعلاج انتفاخات محيط العين.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جيجون (Jayjun Cosmetic)</td></tr>
  <tr><th>الفئة</th><td>العناية بالوجه / لصقات هيدروجيل العين الكورية من جيجون 60 Patches</td></tr>
  <tr><th>نوع المنتج</th><td>لصقات هيدروجيل مبردة ومفتحة ومضادة للتجاعيد بـ {ing_ar} (60 لاصقة)</td></tr>
  <tr><th>الحجم/الوزن</th><td>60 لاصقة (30 ثنائية للعينين)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة محيط العين (المتصبغة، المجهدة، والجافة)</td></tr>
  <tr><th>المظهر النهائي</th><td>محيط عين ناعم كالحرير، مشرق، موحد اللون وخالٍ من الهالات والانتفاخات</td></tr>
  <tr><th>الملمس</th><td>لصقات جل هيدروجيل مائية مرنة غنية بالسيروم</td></tr>
  <tr><th>العطر</th><td>عطر {ing_ar} المنعش الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصات {ing_ar}، نياسيناميد، أدينوسين، حمض الهيالورونيك</td></tr>
  <tr><th>بلد المنشأ</th><td>كوريا الجنوبية (South Korea)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Jayjun Cosmetic Co., Ltd.</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد خلاصات {ing_ar} وتقنية الهيدروجيل في لصقات جيجون (Jayjun Eye Patches)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج لصقات جيجون مشكلة الهالات السوداء، انتفاخات أسفل العين، جفاف محيط العين، والخطوط الدقيقة.</p>

<h3>لماذا تنجح تركيبة Hydrogel Eye Patches؟</h3>
<p>لأن الهيدروجيل المائي ينقل المغذيات والنياسيناميد لعمق الأدمة مع التبريد المباشر الذي يقلل احتقان الأوعية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>حفظ العبوة بالثلاجة قبل الاستخدام:</strong> يضاعف مفعول التبريد وتقليل الانتفاخات.<br>
2. <strong>الطبطبة اللطيفة بالسيروم المتبقي:</strong> ينشط الدورة الدموية بمحيط العين.<br>
3. <strong>الاستخدام المنتظم 2-3 مرات أسبوعياً:</strong> يحافظ على إشراقة ونضارة محيط العين.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "لصقات العين تسبب تهيج وحساسية لعينين."<br>
<strong>الحقيقة:</strong> لصقات جيجون الكورية مصممة بمكونات هيدروجيل مهدئة وآمنة تماماً على منطقة العين.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يقلل النياسيناميد تجمع صبغة الميلانين بينما يشد الأدينوسين ألياف الكولاجين المحيطة بأوعية العين.</p>"""

    faqs_data = [
        (f"ما هي {ar_name}؟", f"هي لصقات هيدروجيل كورية فاخرة بـ {ing_ar} لتفتيح الهالات وتقليل انتفاخات العين (60 لاصقة)."),
        (f"ما هي فوائد خلاصة {ing_ar} والنياسيناميد للعين؟", "تفتح الهالات السوداء، تقرر الانتفاخات، وترطب محيط العين وتنعمه."),
        ("هل تفتح الهالات وتقلل الانتفاخات فورياً؟", "نعم، مثبتة كوريين وسريرياً في التبريد المباشر وتفتيح الهالات وتقليل الانتفاخات."),
        ("ما عدد اللصقات بالعبوة؟", "تأتي بعبوة أنيقة تحتوي على 60 لاصقة (30 ثنائية)."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي اللصقتين أسفل العينين بعد التونر، اتركيهما 20-30 دقيقة وطبطبي السيروم 2-3 مرات أسبوعياً."),
        ("هل هي آمنة ومختبرة جلدياً؟", "نعم، 100% آمنة ومختبرة جلدياً ومناسبة للبشرة الحساسة."),
        ("أين صُنعت لصقات جيجون؟", "صُنع في كوريا الجنوبية بواسطة Jayjun Cosmetic."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات جيجون لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {ing_ar} المنعش الفاخر."),
        ("هل حفظها بالثلاجة ينصح به؟", "نعم، حفظها بالثلاجة يعزز التبريد الفوري وتقليل الانتفاخات الصباحية."),
        ("هل العبوة 60 لاصقة تكفي لفترة جيدة؟", "نعم، تكفي لـ 30 استخداماً (عدة أشهر من الاستخدام المنتظم)."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف أو في الثلاجة."),
        ("هل جيجون الماركة الكورية الأولى في لصقات العين؟", "نعم، Jayjun الماركة الكورية الشهيرة والموثوقة جداً في لصقات الهيدروجيل."),
        ("كم مرة أسبوعياً؟", "2 إلى 3 مرات أسبوعياً وعند الحاجة."),
        ("هل تترك محيط العين مشرقاً وناعماً؟", "نعم، تترك الجلد حول العينين مشرقاً، مرطباً، وناصع النضارة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل تساعد في تقليل الخطوط الدقيقة؟", "نعم، يشد الأدينوسين والهيالورونيك الخطوط الدقيقة بالعين."),
        ("هل تترك أثراً لزجاً؟", "يمتص السيروم بسلاسة دون لزوجة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للنساء والرجال."),
        ("هل تتضمن العبوة ملعقة تطبيق؟", "نعم، تتضمن ملعقة مريحة لرفع اللصقات بنظافة."),
        ("هل يناسب الصيف والشتاء؟", "نعم، ممتاز لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج كوري فاخر وأساسي لكل روتين عناية."),
        ("هل يعيد المظهر الشاب الناعم للعينين؟", "نعم، يمنح العينين مظهراً ناضراً ومشرقاً."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> are authentic luxury iconic Korean hydrogel eye patches from Jayjun designed to brighten dark circles, reduce under-eye puffiness and fine lines, and hydrate and smooth the delicate eye contour. Built upon {ing_en} extracts, Hyaluronic Acid, brightening Niacinamide, and anti-aging Adenosine.</p>
<p>Jayjun Hydrogel Eye Patches instantly cool and soothe the under-eye area, infusing skin with intensive moisture, leaving your eye contour touchably silky soft, radiant, even-toned, and youthful from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Dark Circle Brightening & Tone Evening with {ing_en}:</strong> Reduces pigmentation and fatigue.</li>
  <li><strong>Instant Puffiness & Fine Line Reduction:</strong> Cools and hydrates thin under-eye skin effectively.</li>
  <li><strong>Intensive Moisture Infusion with Hydrogel Technology:</strong> Delivers nutrients deep into skin cells.</li>
  <li><strong>Elasticity Improvement & Anti-Aging with Adenosine:</strong> Fights signs of aging and creasing.</li>
  <li><strong>Contains 60 Patches with Convenient Spatula:</strong> Provides 30 dual applications.</li>
  <li><strong>Authentic Korean Craftsmanship Safe for Sensitive Eyes:</strong> Dermatologically tested.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Cleanse facial skin and eye contour, and prep with toner.</li>
  <li><strong>Step 2:</strong> Use the included spatula to lift two patches and apply gently under eyes.</li>
  <li><strong>Step 3:</strong> Leave on for 20-30 minutes, remove patches, and pat remaining serum until absorbed (use 2-3 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>{ing_en} Extracts & Niacinamide:</strong> Lighten hyperpigmentation and clear dark circles.</li>
  <li><strong>Hyaluronic Acid & Adenosine:</strong> Firm skin and lock in internal hydration.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical eye contour application.</li>
  <li>Avoid direct serum contact inside the eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for dark circle brightening and under-eye puffiness treatment.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Jayjun Cosmetic</td></tr>
  <tr><th>Category</th><td>Skincare / Jayjun Korean Hydrogel Eye Patches 60 Patches</td></tr>
  <tr><th>Product Type</th><td>Hydrogel Cooling Brightening Anti-Aging Eye Patches with {ing_en} (60 Patches)</td></tr>
  <tr><th>Volume/Weight</th><td>60 Patches (30 Pairs)</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Eye Contour Skin Types (Pigmented, Stressed & Dry)</td></tr>
  <tr><th>Finish</th><td>Silky soft, radiant, even-toned & puff-free eye contour</td></tr>
  <tr><th>Texture</th><td>Flexible serum-rich cooling hydrogel gel patches</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh {ing_en} scent</td></tr>
  <tr><th>Active Ingredients</th><td>{ing_en} Extracts, Niacinamide, Adenosine, Hyaluronic Acid</td></tr>
  <tr><th>Country of Origin</th><td>South Korea</td></tr>
  <tr><th>Manufacturer</th><td>Jayjun Cosmetic Co., Ltd.</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Hydrogel Moisture Diffusion & Niacinamide Dark Circle Depigmentation</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves dark circles, under-eye puffiness, dryness, and fine lines.</p>

<h3>Why choose Jayjun Hydrogel Eye Patches?</h3>
<p>Water-rich hydrogel patches deliver Niacinamide and serum nutrients while direct cooling constricts dilated vessels.</p>"""

    en_faqs_data = [
        (f"What are {en_name}?", f"They are luxury Korean hydrogel eye patches with {ing_en} for brightening dark circles and reducing puffiness (60 patches)."),
        (f"What are the benefits of {ing_en} extract and Niacinamide for eyes?", "Brighten dark circles, reduce under-eye puffiness, and hydrate skin."),
        ("Do they brighten dark circles and reduce puffiness instantly?", "Yes, clinically proven to cool skin, reduce puffiness, and lighten dark circles."),
        ("How many patches are in this container?", "60 patches (30 pairs)."),
        ("How do I use them correctly?", "Apply patches under eyes post-toner, leave for 20-30 minutes, and pat serum 2-3 times weekly."),
        ("Are they safe and dermatologically tested?", "Yes, 100% safe, dermatologically tested, and suitable for sensitive eyes."),
        ("Where are Jayjun Eye Patches manufactured?", "In South Korea by Jayjun Cosmetic Co., Ltd."),
        ("How do I verify authenticity at Ekleel Abha?", "All Jayjun products at Ekleel Abha are 100% original."),
        (f"What scent do {en_name} have?", f"Luxurious fresh {ing_en} fragrance."),
        ("Is storing them in the fridge recommended?", "Yes, refrigeration enhances instant cooling and morning de-puffing."),
        ("Does the 60 patch container last long?", "Yes, lasts 30 applications (months of regular use)."),
        ("How should I store them?", "In a cool, dry place or in the refrigerator."),
        ("Is Jayjun a top Korean eye patch brand?", "Yes, Jayjun is a world-famous trusted brand in Korean cosmetics."),
        ("How many times weekly?", "2 to 3 times weekly or as needed."),
        ("Do they leave the eye contour bright and smooth?", "Yes, leave under-eye skin radiant, hydrated, and silky soft."),
        ("Is the container recyclable?", "Yes."),
        ("Do they help reduce fine lines?", "Yes, Adenosine and Hyaluronic acid firm fine lines around the eyes."),
        ("Do they leave a sticky residue?", "Serum absorbs smoothly without stickiness."),
        ("Are they available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Are they suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is a spatula included?", "Yes, includes a hygienic spatula for lifting patches."),
        ("Are they good for all seasons?", "Yes, excellent for summer and winter eye care."),
        ("Are they a nice skincare gift?", "Yes, a premier Korean skincare gift."),
        ("Do they restore youthful smooth eye appearance?", "Yes, give eyes a youthful smooth radiant look."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Jayjun",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. لصقات هيدروجيل كورية بـ {ing_ar} لتفتيح الهالات وتقليل انتفاخات العين. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Jayjun Korean hydrogel eye patches with {ing_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2072():
    return _make_jayjun_eye_patches_b71(
        pid=2072, gtin="8809495894963",
        ar_name="لصقات جل للعين بخلاصة شاي الكركديه من جيجون 60 لاصقة",
        en_name="Jayjun Hibiscus Tea Eye Gel Patches - 60 Patches",
        ing_ar="شاي الكركديه (Hibiscus Tea) المنشط", ing_en="Revitalizing Hibiscus Tea",
        feature_ar="لصقات هيدروجيل للعين بتأثير مبرد ومفتّح بخلاصة الكركديه 60 لاصقة", feature_en="hibiscus tea hydrogel cooling brightening eye patches 60 patches",
        tags_ar=["جيجون", "لصقات_الكركديه_جيجون", "لصقات_العين_الكورية", "تفتيح_الهالات", "إكليل_أبها"],
        tags_en=["jayjun", "hibiscus_eye_patches", "jayjun_eye_patches", "korean_eye_patches", "ekleel_abha"]
    )


def create_product_2073():
    return _make_jayjun_eye_patches_b71(
        pid=2073, gtin="8809495895106",
        ar_name="لصقات جل للعين بالافندر والشاي من جيجون 60 لاصقة",
        en_name="Jayjun Lavender & Tea Eye Gel Patches - 60 Patches",
        ing_ar="خلاصة اللافندر والشاي المهدئة", ing_en="Soothing Lavender & Tea Extract",
        feature_ar="لصقات هيدروجيل مهدئة ومفتحة بخلاصة اللافندر والشاي 60 لاصقة", feature_en="soothing lavender tea hydrogel eye patches 60 patches",
        tags_ar=["جيجون", "لصقات_اللافندر_جيجون", "لصقات_العين_باللافندر", "علاج_انتفاخات_العين", "إكليل_أبها"],
        tags_en=["jayjun", "lavender_eye_patches", "jayjun_lavender", "hydrogel_eye_mask", "ekleel_abha"]
    )


def create_product_2074():
    return _make_jayjun_eye_patches_b71(
        pid=2074, gtin="8809495894956",
        ar_name="لصقات جل للعين بخلاصة الشاي الاخضر من جيجون 60 لاصقة",
        en_name="Jayjun Green Tea Eye Gel Patches - 60 Patches",
        ing_ar="الشاي الأخضر (Green Tea) ومضادات الأكسدة", ing_en="Antioxidant Green Tea",
        feature_ar="لصقات هيدروجيل للعين بمضادات الأكسدة والشاي الأخضر 60 لاصقة", feature_en="antioxidant green tea hydrogel eye patches 60 patches",
        tags_ar=["جيجون", "لصقات_الشاي_الاخضر_جيجون", "لصقات_جيجون_للعيون", "تفتيح_محيط_العين", "إكليل_أبها"],
        tags_en=["jayjun", "green_tea_eye_patches", "jayjun_green_tea", "antioxidant_eye_patches", "ekleel_abha"]
    )


def create_product_2075():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>غسول الوجه ناتشورال وايت من اولاي 100جم (Olay Natural White Face Wash - 100g)</strong> غسول الوجه المفتّح والمنظف الفاخر الأكثر شهرة من أولاي (Olay) المصمم خصيصاً لتنظيف، تصفية، وتفتيح بشرة الوجه وإعادة النضارة الطبيعية وإزالة الخلايا الميتة والأوساخ اليومية. يرتكز هذا الغسول الأصيل (Olay Natural White 100g) على مجمع الفيتامينات الثلاثية (Triple Vitamin System: B3, Pro-B5, E)، خلاصة الأوراق الطبيعية، والمنظفات اللطيفة.</p>
<p>يعمل غسول أولاي ناتشورال وايت على تنظيف مسام الوجه عمقاً، تقليل التصبغات والبقع الداكنة، وتغذية الوجه وحفظ رطوبته الطبيعية، ليترك وجهك ناعماً كالحرير، ناصع البياض، مشرقاً، ومفعماً بالنضارة والحيوية من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح وتنقية الوجه بنظام الفيتامينات الثلاثية (B3, Pro-B5, E):</strong> يوحد لون البشرة ويقلل البقع.</li>
  <li><strong>تنظيف عميق وإزالة الشوائب والأوساخ اليومية:</strong> ينظف المسام بفاعلية ولطف.</li>
  <li><strong>ترطيب وتنعيم لبشرة الوجه:</strong> يمنع الجفاف وشعور الشد بعد الغسيل.</li>
  <li><strong>إعادة النضارة والإشراقة الطبيعية للوجه:</strong> يزيل الخلايا الميتة والبهتان.</li>
  <li><strong>تركيبة آمنة ومختبرة جلدياً للاستخدام اليومي:</strong> تناسب جميع أنواع البشرة.</li>
  <li><strong>أنبوب مدمج سعة 100 جم:</strong> حجم ممتاز للاستخدام اليومي والسفر والتنقل.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الوجه والرقبة بالماء الدافئ.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من غسول أولاي وكوّني رغوة كريمية غنية ودلكي الوجه برفق.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء الدافئ وجففي الوجه برفق (يُستعمل مرتين يومياً صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>فيتامين B3 (النياسيناميد) وفيتامين E وPro-B5:</strong> تفتح التصبغات، تغذي ألياف الجلد، وتحمي من الأكسدة.</li>
  <li><strong>المنظفات اللطيفة والمركبات المرطبة:</strong> تنظف المسام وتحفظ النعومة الحريرية للوجه.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن غسول أولاي ناتشورال وايت 100 جم لتفتيح الوجه وتنظيف المسام وإعادة الإشراقة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>أولاي (Olay Natural White)</td></tr>
  <tr><th>الفئة</th><td>العناية بالوجه / غسولات أولاي للتفتيح والنظافة 100g</td></tr>
  <tr><th>نوع المنتج</th><td>غسول وجه مفتّح ومنظف بمجمع الفيتامينات الثلاثية B3, Pro-B5, E (100g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (العادية، الجافة، والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجه ناعم كالحرير، مشرق، موحد اللون وناصع البياض والنظافة</td></tr>
  <tr><th>الملمس</th><td>رغوة كريمية غنية ينشطف بالماء بسهولة</td></tr>
  <tr><th>العطر</th><td>عطر ناتشورال وايت المنعش الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>فيتامين B3، فيتامين E، بروفيتامين B5، منظفات لطيفة</td></tr>
  <tr><th>بلد المنشأ</th><td>تايلاند / الهند</td></tr>
  <tr><th>الشركة المصنعة</th><td>Procter & Gamble (P&G)</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد الفيتامينات الثلاثية B3, Pro-B5, E في غسول أولاي (Olay Natural White)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول أولاي ناتشورال وايت مشكلة بهتان الوجه، عدم توحد اللون، البقع الداكنة، وتراكم الأوساخ بالمسام.</p>

<h3>لماذا تنجح تركيبة Olay Triple Vitamin System؟</h3>
<p>لأن فيتامين B3 يثبط نقل صبغة الميلانين بينما يجدد Pro-B5 وفيتامين E مرونة وخلايا الجلد.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنظيف مرتين يومياً صباحاً ومساءً:</strong> ينظف التلوث ويحفز تفتيح الوجه.<br>
2. <strong>التكميل بكريم أولاي ناتشورال وايت المرطب:</strong> يضاعف نضارة وتفتيح البشرة.<br>
3. <strong>الشطف الجيد بالماء الدافئ:</strong> ينعش الوجه ويمنع أي بقايا صابونية.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "غسولات التفتيح تجفف الوجه وتسبب التقشير."<br>
<strong>الحقيقة:</strong> غسول أولاي مدعم بـ Pro-B5 وفيتامين E لمنح ترطيب ونعومة حريرية أثناء الغسيل.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يقلل النياسيناميد (B3) فرط التصبغ بينما تقضي المنظفات على الرواسب والدهون المؤكسدة بالمسام.</p>"""

    faqs = [
        ("ما هو غسول الوجه ناتشورال وايت من اولاي 100جم؟", "هو غسول وجه مفتّح ومنظف فاخر من أولاي بنظام الفيتامينات الثلاثية B3 وE وPro-B5 لتفتيح البشرة (100 جم)."),
        ("ما هي فوائد نظام الفيتامينات الثلاثية (B3, Pro-B5, E)؟", "يفتح البقع الداكنة، يوحد لون الوجه، ويغذي الجلد ويحفظ رطوبته."),
        ("هل ينظف المسام ويفتح الوجه من الاستخدام الأول؟", "نعم، مثبت سريرياً في تنظيف المسام وتفتيح وإشراق بشرة الوجه."),
        ("ما حجم العبوة؟", "تأتي بأنبوب أنيق سعة 100 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي الوجه، ضعي كمية وكوّني رغوة كريمية، دلكي برفق واشطفي بالماء مرتين يومياً."),
        ("هل هو آمن لجميع أنواع البشرة؟", "نعم، 100% آمن ومختبر جلدياً ومناسب لجميع أنواع البشرة."),
        ("أين صُنع غسول أولاي ناتشورال وايت؟", "صُنع بواسطة Procter & Gamble (P&G) العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات أولاي لدى إكليل أبها أصلية 100%."),
        ("ما رائحة غسول أولاي ناتشورال وايت؟", "عطر أولاي ناتشورال وايت المنعش الأنيق."),
        ("هل يترك الوجه ناعماً ومشرقاً؟", "نعم، يترك الوجه ناعماً كالحرير ونظيراً ومشرقاً."),
        ("هل أنبوب 100 جم مناسب للحقيبة والسفر؟", "نعم، أنبوب أنيق مدمج مثالي للحقيبة والسفر والتنقل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل أولاي ماركة عالمية شهيرة في التفتيح؟", "نعم، Olay علامة عالمية رائدة ومشهورة جداً في العناية بالتفتيح والجمال."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل يزيل المكياج الخفيف والأوساخ؟", "نعم، يزيل المكياج الخفيف والأوساخ والدهون بفاعلية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في تقليل البقع الداكنة؟", "نعم، يقلل النياسيناميد البقع الداكنة ويوحد لون الوجه."),
        ("هل يترك أثراً دهنياً؟", "لا، ينظف وينشطف بالكامل دون دهنية."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يناسب الصيف والشتاء؟", "نعم، ممتاز لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج عناية وتفتيح أنيق ومفيد."),
        ("هل يعيد المظهر الناصع المشرق للبشرة؟", "نعم، يمنح الوجه مظهراً ناصع البياض والنقاء."),
        ("هل يفضل استخدام كريم أولاي المرطب بعده؟", "نعم، يُفضل اتباع كريم أولاي ناتشورال وايت لنتائج مضاعفة."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Olay Natural White Face Wash - 100g</strong> is an authentic luxury skin-brightening and purifying facial cleanser from Olay designed to clean, clarify, and illuminate facial skin while restoring natural radiance and sweeping away dead cells and daily dirt. Built upon the Triple Vitamin System (B3, Pro-B5, E), natural leaf extracts, and mild cleansing agents.</p>
<p>Olay Natural White Cleanser deeply purifies facial pores, reduces hyperpigmentation and dark spots, and nourishes skin while preserving natural moisture, leaving your face touchably silky soft, visibly brightened, glowing, and refreshed from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Facial Brightening & Purification with Triple Vitamin System (B3, Pro-B5, E):</strong> Evens skin tone and fades spots.</li>
  <li><strong>Deep Cleansing & Daily Dirt Removal:</strong> Cleanses pores effectively and gently.</li>
  <li><strong>Facial Softening & Hydration:</strong> Prevents post-wash dryness and tightness.</li>
  <li><strong>Natural Radiance & Glow Restoration:</strong> Removes dullness and dead skin cells.</li>
  <li><strong>Dermatologically Tested Safe Formula:</strong> Suitable for all skin types.</li>
  <li><strong>Compact 100g Tube:</strong> Ideal size for daily care, handbag, and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet face and neck skin with warm water.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of Olay cleanser, work into a rich creamy lather, and massage face gently.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and pat face dry (use twice daily morning & night).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Vitamin B3 (Niacinamide), Vitamin E & Pro-B5:</strong> Brighten dark spots, nourish skin fibers, and protect against oxidation.</li>
  <li><strong>Mild Cleansers & Hydrating Agents:</strong> Cleanse pores while locking in silky facial softness.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Olay Natural White Face Wash 100g for facial brightening, pore cleansing, and radiance restoration.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Olay (Natural White)</td></tr>
  <tr><th>Category</th><td>Skincare / Olay Brightening Cleansers 100g</td></tr>
  <tr><th>Product Type</th><td>Triple Vitamin System (B3, Pro-B5, E) Brightening Cleanser (100g)</td></tr>
  <tr><th>Volume/Weight</th><td>100 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Normal, Dry & Oily)</td></tr>
  <tr><th>Finish</th><td>Silky soft, brightened, radiant & spotlessly clean face</td></tr>
  <tr><th>Texture</th><td>Rich smooth foaming cream lather</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh Olay Natural White scent</td></tr>
  <tr><th>Active Ingredients</th><td>Vitamin B3 (Niacinamide), Vitamin E, Pro-Vitamin B5, Gentle Cleansers</td></tr>
  <tr><th>Country of Origin</th><td>Thailand / India</td></tr>
  <tr><th>Manufacturer</th><td>Procter & Gamble (P&G)</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Triple Vitamin System (B3, Pro-B5, E) Melanin Inhibition</h2>

<h3>What problem does this solve?</h3>
<p>Olay Natural White Face Wash resolves facial dullness, uneven skin tone, dark spots, and pore dirt accumulation.</p>

<h3>Why choose Olay Triple Vitamin System?</h3>
<p>Vitamin B3 inhibits melanosome transfer while Pro-B5 and Vitamin E regenerate skin cells and protect against environmental stress.</p>"""

    en_faqs = [
        ("What is Olay Natural White Face Wash - 100g?", "It is a luxury brightening facial cleanser from Olay with a Triple Vitamin System (B3, Pro-B5, E) for skin illumination (100g)."),
        ("What are the benefits of the Triple Vitamin System (B3, Pro-B5, E)?", "Brightens dark spots, evens skin tone, and nourishes and hydrates facial skin."),
        ("Does it clean pores and brighten skin from first use?", "Yes, clinically proven to purify pores and deliver visible facial brightening and radiance."),
        ("What volume is contained in this tube?", "100g compact tube."),
        ("How do I use it correctly?", "Wet face, apply cleanser, lather into a cream, massage gently and rinse twice daily."),
        ("Is it safe for all skin types?", "Yes, 100% safe, dermatologically tested, and suitable for all skin types."),
        ("Where is Olay Face Wash manufactured?", "By Procter & Gamble (P&G)."),
        ("How do I verify authenticity at Ekleel Abha?", "All Olay products at Ekleel Abha are 100% original."),
        ("What scent does Olay Natural White have?", "Luxurious fresh Olay Natural White fragrance."),
        ("Does it leave face soft and radiant?", "Yes, leaves face touchably silky soft, clear, and radiant."),
        ("Is the 100g tube travel friendly?", "Yes, sleek compact tube ideal for handbag and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Olay a world-famous brightening brand?", "Yes, Olay is a globally leading famous brand in skin brightening beauty care."),
        ("How many times daily?", "Twice daily (morning and night)."),
        ("Does it remove light makeup and dirt?", "Yes, effectively cleanses light makeup, excess sebum, and daily dirt."),
        ("Is the tube recyclable?", "Yes."),
        ("Does it help fade dark spots?", "Yes, Niacinamide fades dark spots and evens facial tone."),
        ("Does it leave a greasy film?", "No, cleanses completely clean without greasiness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it good for all seasons?", "Yes, excellent for summer and winter care."),
        ("Is it a nice skincare gift?", "Yes, an elegant practical brightening gift."),
        ("Does it restore bright glowing skin appearance?", "Yes, gives facial skin a bright spotlessly clean look."),
        ("Is following with Olay Moisturizer recommended?", "Yes, follow with Olay Natural White Moisturizer for enhanced results."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2075",
        "sku": "EK-2075",
        "gtin": "4902430987622",
        "brand": "Olay",
        "ar": {
            "title": "غسول الوجه ناتشورال وايت من اولاي 100جم",
            "meta_title": "غسول الوجه أولاي ناتشورال وايت 100جم | إكليل أبها",
            "meta_description": "اشتري غسول الوجه ناتشورال وايت من أولاي (100 جم). غسول مفتّح بنظام الفيتامينات الثلاثية B3, Pro-B5, E لإشراقة وتغطية الوجه. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["أولاي", "غسول_أولاي_ناتشورال_وايت", "غسول_تفتيح_الوجه", "فيتامينات_أولاي", "إكليل_أبها"]
        },
        "en": {
            "title": "Olay Natural White Face Wash - 100g",
            "meta_title": "Olay Natural White Face Wash 100g | Ekleel Abha",
            "meta_description": "Buy original Olay Natural White Face Wash (100g). Triple Vitamin System (B3, Pro-B5, E) skin brightening facial cleanser. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["olay", "olay_natural_white", "brightening_face_wash", "olay_cleanser", "ekleel_abha"]
        }
    }


print("Loaded all 5 Batch 71 builders complete")
