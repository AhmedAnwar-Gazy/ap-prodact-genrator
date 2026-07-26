import json, os

def create_product_2023():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>كريم للحالات المتهيجة للبشرة الجافه من كيوفي 100جم (QV Cream for Irritated and Dry Skin Conditions - 100g)</strong> كريم الترطيب والترميم المكثف الطبي الفاخر من كيو في الأسترالية المصمم خصيصاً لترطيب وتهدئة وإصلاح حالات البشرة شديدة الجفاف، المتهيجة، الحساسة، والمعرضة للاكزيما والصدفية. يرتكز هذا الكريم الأصيل (QV Cream 100g) على السكوالان الطبيعي (Squalene)، الجليسرين، الشحوم المرممة لبشرة الوجه والجسم.</p>
<p>يعمل كريم كيوفي الطبي على حبس رطوبة الجلد لـ 24 ساعة، إعادة بناء حاجز البشرة الدهني المتضرر، وتهدئة الحكة والاحمرار والتقشر الناتج عن الجفاف الشديد، ليترك بشرتك ناعمة كالحرير، مرطبة عمقاً، مشفية، ومحمية من التهيجات طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وترميم مكثف لـ 24 ساعة بمادة السكوالان الطبيعية:</strong> يغذي البشرة ويصلح الحواجز الجلدية التالفة.</li>
  <li><strong>تهدئة فورية للحكة والاحمرار والتهيجات الجلادية:</strong> ممتاز للبشرة المعرضة للاكزيما والصدفية والجفاف الشديد.</li>
  <li><strong>خالٍ 100% من العطور، الصبغات، الينولين، والبارابين:</strong> آمن ولطيف للغاية على البشرة الأكثر حساسية.</li>
  <li><strong>مناسب لجميع مناطق الجسم والوجه والرضع والأطفال:</strong> كريم العناية العائلية الشاملة.</li>
  <li><strong>اختبر درماتولوجياً لحماية الفئات الجلدية الحساسة:</strong> لا يسبب انسداد المسام (Non-Comedogenic).</li>
  <li><strong>أنبوب أنيق سعة 100 جم:</strong> حجم مدمج مثالي للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسية من كريم كيوفي على بشرة نظيفة بعد الغسيل أو الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي برفق بحركات دائرية ناعمة على الوجه أو الجسم أو المناطق المتهيجة حتى الامتصاص الكامل (يُستعمل عدة مرات يومياً وقبل النوم).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مادة السكوالان الطبيعية (Squalene) والشحوم المرطبة:</strong> تطابق الشحوم البشرية الطبيعية لترميم الجلد.</li>
  <li><strong>الجليسرين بتركيز غني:</strong> يجذب جزيئات الماء ويحبسها داخل الخلايا القرنية العميقة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من الجفاف الشديد والتهيجات بالاكزيما ويبحث عن كريم كيوفي 100 جم للترميم والتهدئة.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كيو في (QV)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / كريمات كيوفي الطبية للترطيب المكثف والاكزيما 100g</td></tr>
  <tr><th>نوع المنتج</th><td>كريم طبي مرطب ومصمم للبشرة شديدة الجفاف والمتهيجة والاكزيما (100g)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة شديدة الجفاف، المتهيجة، الحساسة والمعرضة للاكزيما</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة كالحرير، مشفية من التهيجات، مرطبة عمقاً ومحمية 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>كريم دسم غني ينفذ بنعومة دون لزوجة ثقيلة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور الصناعية (عطر طبي محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>سكوالان طبيعي (Squalene)، جليسرين غني، شحوم حمائية</td></tr>
  <tr><th>بلد المنشأ</th><td>أستراليا (Australia)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (بما في ذلك الرضع والأطفال والبالغون)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد السكوالان والترطيب الخالي من العطور في كريم كيوفي (QV Cream)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم كيوفي مشكلة الاكزيما، التهاب وتقشر الجلد، الحكة المؤلمة، والجفاف الشديد الناتج عن فقدان شحوم الحجاب البشري.</p>

<h3>لماذا تنجح تركيبة QV Cream؟</h3>
<p>لأن دمج السكوالان (Squalene) المطابق لزيوت البشرة مع الجليسرين يرمم الغلاف الهيدروليبيدي دون تسبيب تهيج ناتج عن العطور.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق فوراً بعد الاستحمام والماء:</strong> يضمن حبس أكبر كمية من الرطوبة الداخلية.<br>
2. <strong>التطبيق المنتظم 3-4 مرات يومياً:</strong> يعيد بناء الجلد المتضرر بسرعة.<br>
3. <strong>تجنب استخدام الصابون القاسي المعطر:</strong> يحمي البشرة من نكسات التهدئة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الكريمات العلاجية للاكزيما تحتوي على كورتيزون."<br>
<strong>الحقيقة:</strong> كريم كيوفي خالٍ 100% من الكورتيزون والبارابين ومصمم كترطيب طبيعي آمن يومياً مدى الحياة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعوض السكوالان النقص في السيراميدات والليبيدات بين الخلوية (Intercellular Lipids)، مصلحاً ثقوب الحاجز الوقائي (Stratum Corneum Barrier).</p>"""

    faqs = [
        ("ما هو كريم للحالات المتهيجة للبشرة الجافه من كيوفي 100جم؟", "هو كريم مرطب طبي مكثف من كيو في الأسترالية بالسكوالان للبشرة شديدة الجفاف والمتهيجة والاكزيما (100 جم)."),
        ("ما هي فوائد السكوالان والتركيبة الخالية من العطور؟", "يرمم السكوالان حاجز البشرة، بينما تمنع التركيبة الخالية من العطور التهيج وتضمن ترطيباً 24 ساعة."),
        ("هل يهدئ الاكزيما والحكة والجفاف الشديد؟", "نعم، مثبت سريرياً في تهدئة الاكزيما والحكة والجفاف الشديد وإصلاح الجلد."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنبوب سعة 100 جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي على بشرة نظيفة دلكي برفق حتى الامتصاص عدة مرات يومياً وقبل النوم."),
        ("هل هو خالٍ من العطور والبارابين والكورتيزون؟", "نعم، 100% خالٍ من العطور، الصبغات، اللانولين، البارابين والكورتيزون."),
        ("أين صُنع كريم كيوفي؟", "صُنع في أستراليا بواسطة Ego Pharmaceuticals Australia."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كيوفي لدى إكليل أبها أصلية 100%."),
        ("هل يناسب الرضع والأطفال والبالغين؟", "نعم، آمن ومناسب لجميع الفئات من الرضع حتى كبار السن."),
        ("هل يترك ملمساً دهنياً ثقيلاً؟", "ينفذ بنعومة ليترك البشرة مرطبة دون لزوجة مزعجة."),
        ("هل أنبوب 100 جم مناسب للحقيبة؟", "نعم، حجم أنيق مدمج مثالي للحقيبة والسفر والتنقل."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب الوجه والجسم معاً؟", "نعم، مرطب شامل ممتاز للوجه والجسم والمناطق المتهيجة."),
        ("كم مرة يومياً؟", "عدة مرات يومياً وخاصة بعد الاستحمام وقبل النوم."),
        ("هل كيوفي الماركة الأولى أسترالياً في الترطيب الطبي؟", "نعم، QV الماركة رقم 1 الموصى بها طبياً في أستراليا."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع تشقق الجلد في الشتاء؟", "نعم، الحماية الأسترالية المثالية ضد جفاف وبرد الشتاء."),
        ("هل يقلل القشور والاحمرار؟", "نعم، يزيل القشور ويهدئ احمرار الجلد المتهيج."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يسبب انسداد المسام؟", "لا، تركيبة غير مسببة للانسداد (Non-Comedogenic)."),
        ("هل يصلح هدية ممتازة للرعاية الصحية؟", "نعم، منتج طبي فاخر وأساسي لكل عائلة."),
        ("هل يمنح ترطيباً لـ 24 ساعة؟", "نعم، يحفظ الترطيب الداخلي لـ 24 ساعة متواصلة."),
        ("هل يناسب صدفية الجلد أيضاً؟", "نعم، يهدئ الصدفية والجفاف الحرشفي بفاعلية."),
        ("هل يتوفر الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها."),
        ("هل تتوفر منه أحجام متعددة؟", "نعم، تتوفر أحجام متعددة تناسب جميع الاحتياجات.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>QV Cream for Irritated and Dry Skin Conditions - 100g</strong> is an authentic luxury medical intensive hydrating and repairing cream from QV Australia formulated to hydrate, soothe, and repair severely dry, irritated, sensitive, and eczema-prone skin. Built upon natural Squalene, Glycerin, and skin-restorative lipids.</p>
<p>QV Medical Cream locks in internal skin hydration for 24 hours, rebuilds damaged epidermal skin barriers, and calms itching, redness, and flaking from extreme dryness, leaving your skin touchably silky soft, deeply hydrated, healed, and protected all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intensive 24-Hour Hydration & Repair with Natural Squalene:</strong> Nourishes skin and repairs damaged barriers.</li>
  <li><strong>Instant Soothing for Itching, Redness & Irritated Skin:</strong> Excellent for eczema, psoriasis, and severe dryness.</li>
  <li><strong>100% Free from Fragrance, Colors, Lanolin & Parabens:</strong> Extremely safe and gentle on sensitive skin.</li>
  <li><strong>Suitable for Whole Body, Face, Infants & Adults:</strong> Complete family medical hydration cream.</li>
  <li><strong>Dermatologically Tested Non-Comedogenic Formula:</strong> Will not clog pores or cause breakouts.</li>
  <li><strong>Compact 100g Tube Container:</strong> Ideal size for daily care, handbag, and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of QV Cream onto clean skin post-wash or shower.</li>
  <li><strong>Step 2:</strong> Massage gently in smooth circular motions onto face, body, or irritated areas until absorbed (use multiple times daily & bedtime).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Squalene & Hydrating Lipids:</strong> Mimic natural human sebum repairing damaged skin barriers.</li>
  <li><strong>Rich Concentrated Glycerin:</strong> Draws moisture locking it deep inside stratum corneum cells.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and body skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from severe skin dryness and eczema seeking QV 100g Cream for repair and soothing.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>QV</td></tr>
  <tr><th>Category</th><td>Skincare / QV Medical Intensive Hydrating & Eczema Creams 100g</td></tr>
  <tr><th>Product Type</th><td>Medical Dry & Irritated Skin Repairing Cream with Squalene (100g)</td></tr>
  <tr><th>Volume/Weight</th><td>100 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Severely Dry, Irritated, Sensitive & Eczema-Prone Skin</td></tr>
  <tr><th>Finish</th><td>Silky soft, healed, deeply hydrated & 24H protected skin</td></tr>
  <tr><th>Texture</th><td>Rich smooth dense cream penetrating without heavy stickiness</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (neutral medical scent)</td></tr>
  <tr><th>Active Ingredients</th><td>Natural Squalene, Rich Glycerin, Protective Lipids</td></tr>
  <tr><th>Country of Origin</th><td>Australia</td></tr>
  <tr><th>Manufacturer</th><td>Ego Pharmaceuticals Australia</td></tr>
  <tr><th>Age Group</th><td>All Ages (Infants, Children & Adults)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Squalene Lipid Layer Mimicry & Fragrance-Free Epidermal Repair</h2>

<h3>What problem does this solve?</h3>
<p>QV Cream resolves eczema flare-ups, skin inflammation and peeling, painful itching, and severe barrier loss.</p>

<h3>Why choose QV Cream?</h3>
<p>Combining skin-identical Squalene with rich Glycerin repairs damaged stratum corneum lipids without fragrance-induced flare-ups.</p>"""

    en_faqs = [
        ("What is QV Cream for Irritated and Dry Skin Conditions - 100g?", "It is an Australian medical intensive hydrating cream with Squalene for dry, irritated, and eczema-prone skin (100g)."),
        ("What are the benefits of Squalene and fragrance-free formula?", "Squalene repairs skin barriers, while the fragrance-free formula prevents irritation ensuring 24-hour hydration."),
        ("Does it soothe eczema, itching, and severe dryness?", "Yes, clinically proven to soothe eczema, itching, and severe skin dryness."),
        ("What volume is contained in this tube?", "100g tube."),
        ("How do I use it correctly?", "Apply on clean skin, massage gently until absorbed multiple times daily and before bed."),
        ("Is it free from fragrance, parabens, and cortisone?", "Yes, 100% free from fragrance, colors, lanolin, parabens, and cortisone."),
        ("Where is QV Cream manufactured?", "In Australia by Ego Pharmaceuticals Australia."),
        ("How do I verify authenticity at Ekleel Abha?", "All QV products at Ekleel Abha are 100% original."),
        ("Is it safe for infants, children, and adults?", "Yes, safe and suitable for all ages from infants to elderly."),
        ("Does it leave a heavy greasy residue?", "Penetrates smoothly leaving skin hydrated without sticky residue."),
        ("Is the 100g tube handbag friendly?", "Yes, sleek compact tube ideal for handbag and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for face and body together?", "Yes, versatile moisturizer excellent for face, body, and flare-up zones."),
        ("How many times daily?", "Multiple times daily especially post-shower and bedtime."),
        ("Is QV the #1 medical brand in Australia?", "Yes, QV is the #1 medically recommended brand in Australia."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it prevent winter skin cracking?", "Yes, superior defense against winter cold dryness."),
        ("Does it reduce flaking and redness?", "Yes, removes flakes and calms irritated skin redness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it clog pores?", "No, non-comedogenic formula."),
        ("Is it a practical medical gift?", "Yes, a premier medical essential for every family."),
        ("Does it deliver 24-hour hydration?", "Yes, locks in internal skin moisture for 24 continuous hours."),
        ("Is it suitable for psoriasis skin?", "Yes, effectively calms psoriasis and scaly dry skin."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy."),
        ("Are multiple sizes available?", "Yes, multiple sizes are available to suit all user needs.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2023",
        "sku": "EK-2023",
        "gtin": "9314839015427",
        "brand": "QV",
        "ar": {
            "title": "كريم للحالات المتهيجة للبشرة الجافه من كيوفي 100جم",
            "meta_title": "كريم كيوفي للبشرة الجافة والمتهيجة 100جم | إكليل أبها",
            "meta_description": "اشتري كريم كيوفي للحالات المتهيجة والبشرة الجافة (100 جم). كريم أسترالي طبي بالسكوالان لترميم البشرة وتهدئة الاكزيما. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كيوفي", "كريم_كيوفي", "علاج_الاكزيما", "ترطيب_البشرة_الجافة", "إكليل_أبها"]
        },
        "en": {
            "title": "QV Cream for Irritated and Dry Skin Conditions - 100g",
            "meta_title": "QV Cream Irritated & Dry Skin 100g | Ekleel Abha",
            "meta_description": "Buy original QV Cream for Irritated and Dry Skin Conditions (100g). Australian medical Squalene hydrating eczema cream. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["qv", "qv_cream", "eczema_cream", "dry_skin_repair", "ekleel_abha"]
        }
    }


def _make_cantu_product(pid, gtin, ar_name, en_name, type_ar, type_en, weight_g, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> مستحضر تصفيف وترطيب الشعر الكيرلي والمجعد الفاخر الأصيل من كانتو العالمية المصمم خصيصاً لمنح الخصلات والتجعدات ثباتاً ناعماً، ترطيباً عميقاً، ولمعاناً ساحراً دون أي قشور أو تيبس. يرتكز هذا المستحضر الأصيل ({en_name}) على زبدة الشيا الصافية 100% (Pure Shea Butter)، الزيوت المغذية للشعر، والمركبات الملطفة.</p>
<p>يعمل مستحضر كانتو للشعر على ترويض الهيشات وتطوير وتحديد التجعدات الطبيعية الكيرلي، تغذية ألياف الشعر الجافة وحفظ رطوبتها، وإضفاء بريق ونعومة حريرية على التصفيفة، ليترك شعرك أو شعر طفلك مصففاً بجمال، مرناً، ومحمياً من الجفاف طوال اليوم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتغذية مكثفة بزبدة الشيا الصافية 100%:</strong> تعيد اللين والنعومة للشعر الجاف والمجعد.</li>
  <li><strong>تحديد وتثبيت التموجات والكيرلي (Curl Definition):</strong> يبرز جمال الخصلات الطبيعية دون تيبس.</li>
  <li><strong>السيطرة على الهيشات والتطاير:</strong> يحمي الشعر من الرطوبة الجوية والتجعّد.</li>
  <li><strong>خالٍ من الكبريتات، السيليكون، البارابين، والزيوت المعدنية:</strong> تركيبة ناصعة النظافة وآمنة للشعر.</li>
  <li><strong>يمنح الشعر لمعاناً طبيعياً براقاً:</strong> يكسو الخصلات ببريق ناعم.</li>
  <li><strong>عبوة سعة {weight_g} جم:</strong> حجم ممتاز للاستخدام اليومي والتصفيف المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> وزعي كمية مناسية من مستحضر كانتو على شعر رطب أو جاف قسماً بقسم.</li>
  <li><strong>الخطوة الثانية:</strong> صففي الشعر بالأصابع أو المشط الواسع لتشغيل وتحديد الكيرلي والتسريحة (يُستعمل عند التصفيف).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>زبدة الشيا الطبيعية الصافية:</strong> تغذي ساق الشعر وتمنحه طراوة واستعادة للمرونة.</li>
  <li><strong>الزيوت النباتية المغذية:</strong> تحفظ الترطيب الداخلي وتمنع جفاف وتكسر أطراف الشعر.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على الشعر فقط.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} لتصفيف وترطيب وتحديد الشعر الكيرلي والمجعد.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كانتو (Cantu)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / مستحضرات تصفيف وتحديد الشعر الكيرلي من كانتو {weight_g}g</td></tr>
  <tr><th>نوع المنتج</th><td>مستحضر تصفيف وتحديد الكيرلي بزبدة الشيا ({type_ar}) {weight_g}g</td></tr>
  <tr><th>الحجم/الوزن</th><td>{weight_g} جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>الشعر الكيرلي، المجعد، الجاف، وشعر الأطفال</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر مصفف كيرلي محدد، مرن، مرطب عمقاً وخالٍ من الهيشات والقشور</td></tr>
  <tr><th>الملمس</th><td>كريم/بوماد/كاسترد ناعم غني ذو ثبات مرن</td></tr>
  <tr><th>العطر</th><td>عطر جوز الهند وجوز الشيا الاستوائي الفواح</td></tr>
  <tr><th>المكونات النشطة</th><td>زبدة الشيا الصافية 100%، زيوت مغذية، مركبات تنعيم</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة (USA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>PDC Brands USA</td></tr>
  <tr><th>الفئة العمرية</th><td>النساء، الرجال، والأطفال (حسب التخصص)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد زبدة الشيا الصافية وتحديد الكيرلي في كانتو (Cantu)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مستحضر كانتو مشكلة هيشان الشعر الكيرلي، فقدان تحديد التموجات، جفاف الخصلات، والتكسر أثناء التصفيف.</p>

<h3>لماذا تنجح تركيبة Cantu Pure Shea Butter؟</h3>
<p>لأن الأحماض الدهنية في زبدة الشيا النقية تتغلغل في مسام الكيراتين الجاف وتغلف الخصلة بغشاء يحفظ النسبة المائية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على شعر رطب مقسم لأجزاء:</strong> يضمن توزيع المنتج وتحديد الكيرلي بامتياز.<br>
2. <strong>تجنب استخدام الفرشاة الضيقة على الشعر الجاف:</strong> يحافظ على نمط التموجات الطبيعي.<br>
3. <strong>الاستخدام المنتظم:</strong> يمنح الشعر مرونة وكثافة صحية طوال اليوم.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "منتجات زبدة الشيا تسبب ثقل ولزوجة الشعر."<br>
<strong>الحقيقة:</strong> مستحضرات كانتو مصممة بامتصاص متوازن يغذي الكيرلي ويحدد الخصلات دون تراكم لزج.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تلتصق دهون زبدة الشيا بالطبقة الخارجية لساق الشعر (Cuticle Layer) محددة التموجات ومانعة نفاذ الرطوبة الجوية المسببة للهيشان.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو مستحضر تصفيف وتحديد الكيرلي من كانتو بزبدة الشيا الصافية بحجم {weight_g} جم."),
        ("ما هي فوائد زبدة الشيا الصافية للتصفيف؟", "تغذي وتنعيم الشعر الكيرلي والجاف، تروض الهيشات، وتحدد التموجات بمرونة طوال اليوم."),
        ("هل يحدد الكيرلي ويمنع الهيشان بدون قشور؟", "نعم، مثبت سريرياً في تحديد التموجات والسيطرة على الهيشان دون ترك قشور بيضاء."),
        (f"ما وزن العبوة؟", f"{weight_g} جم."),
        ("كيف يُستخدم بالشكل الصحيح؟", "وزعي على شعر رطب أو جاف قسماً بقسم، صففي بالأصابع أو المشط الواسع لتحديد الكيرلي."),
        ("هل هو خالٍ من الكبريتات والسيليكون والبارابين؟", "نعم، 100% خالٍ من الكبريتات، السيليكون، البارابين والزيوت المعدنية."),
        (f"أين صُنع مستحضر كانتو؟", "صُنع في الولايات المتحدة بواسطة PDC Brands USA."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كانتو لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", "عطر جوز الهند وجوز الشيا الاستوائي الفواح."),
        ("هل يناسب الشعر الكيرلي والمجعد والجاف؟", "نعم، مصمم خصيصاً للشعر الكيرلي والمجعد والجاف."),
        (f"هل العبوة {weight_g} جم تكفي لفترة جيدة؟", "نعم، تكفي لعدة أسابيع من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل كانتو العلامة الأولى عالمياً في الشعر الكيرلي؟", "نعم، Cantu العلامة العالمية الأكثر شهرة في العناية بالشعر الكيرلي."),
        ("كم مرة يومياً؟", "عند تصفيف الشعر."),
        ("هل يمنح الشعر لمعاناً وطراوة؟", "نعم، يمنح الشعر لمعاناً طبيعياً وطراوة حريرية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع تكسر أطراف الشعر؟", "نعم، يغذي الشعر ويحمي الأطراف من الجفاف والتكسر."),
        ("هل يترك ملمساً لزجاً؟", "ينفذ بمرونة دون ترك لزوجة أو تراكمات ثقيلة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الأطفال والنساء والرجال؟", "نعم، مناسب للجميع حسب التخصص."),
        ("هل يحمي الشعر من الرطوبة الجوية؟", "نعم، يغلف الشعر ويحميه من الهيشان الناتج عن الرطوبة."),
        ("هل يصلح هدية ممتازة لمحب الكيرلي؟", "نعم، خيار ممتاز جداً للهدايا في العناية بالشعر."),
        ("هل يعيد المظهر الصحي للشعر؟", "نعم، يعيد الحيوية والجمال الطبيعي للتسريحة."),
        ("هل يسهل التصفيف اليومي؟", "نعم، يسهل تمشيط وتصفيف الشعر الكيرلي والمجعد بسلاسة."),
        ("هل تتوفر منه خيارات أخرى لدى كانتو؟", "نعم، تتوفر عائلة Cantu كاملة لدى إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic luxury curly and wavy hair styling and moisturizing product from Cantu designed to provide soft hold, deep hydration, and defined curls without flakes or stiffness. Built upon 100% Pure Shea Butter, hair-nourishing oils, and conditioning agents.</p>
<p>Cantu Hair Product tames frizz, defines natural curl patterns, nourishes dry hair fibers, and locks in moisture while adding a brilliant natural shine, leaving your hair or your child's hair beautifully styled, flexible, and protected against dryness all day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intensive Hydration with 100% Pure Shea Butter:</strong> Restores softness and moisture to dry curly hair.</li>
  <li><strong>Curl & Wave Definition:</strong> Highlights natural curl patterns with flexible non-stiff hold.</li>
  <li><strong>Frizz & Flyaway Control:</strong> Shields hair against environmental humidity and frizz.</li>
  <li><strong>Free from Sulfates, Silicones, Parabens & Mineral Oil:</strong> Clean safe formula for hair health.</li>
  <li><strong>Imparts Natural Luminous Shine:</strong> Coats strands in a soft healthy luster.</li>
  <li><strong>Generous {weight_g}g Tub:</strong> Excellent volume for daily styling and hair care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Section damp or dry hair and apply a suitable amount of Cantu product section by section.</li>
  <li><strong>Step 2:</strong> Style with fingers or a wide-tooth comb to define curls and style (use whenever styling).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Pure Natural Shea Butter:</strong> Deeply nourishes the hair shaft restoring elasticity and softness.</li>
  <li><strong>Nourishing Plant Oils:</strong> Lock in internal moisture preventing dry split ends.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hair application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for styling, hydrating, and defining curly and textured hair.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Cantu</td></tr>
  <tr><th>Category</th><td>Hair Care / Cantu Pure Shea Butter Curly Hair Styling Products {weight_g}g</td></tr>
  <tr><th>Product Type</th><td>Pure Shea Butter Curly Hair Styling & Defining Product ({type_en}) {weight_g}g</td></tr>
  <tr><th>Volume/Weight</th><td>{weight_g} g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Curly, Wavy, Coily, Dry & Children's Hair</td></tr>
  <tr><th>Finish</th><td>Defined curls, deeply hydrated, flexible & frizz-free styled hair</td></tr>
  <tr><th>Texture</th><td>Smooth rich cream/pomade/custard with flexible hold</td></tr>
  <tr><th>Fragrance</th><td>Invigorating tropical coconut and shea butter scent</td></tr>
  <tr><th>Active Ingredients</th><td>100% Pure Shea Butter, Nourishing Plant Oils, Conditioning Agents</td></tr>
  <tr><th>Country of Origin</th><td>USA</td></tr>
  <tr><th>Manufacturer</th><td>PDC Brands USA</td></tr>
  <tr><th>Age Group</th><td>Men, Women & Children (per variant)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Pure Shea Butter Cuticle Occlusion & Natural Curl Pattern Definition</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves curly hair frizz, curl pattern collapse, dry hair strands, and styling breakage.</p>

<h3>Why choose Cantu Pure Shea Butter?</h3>
<p>Pure Shea Butter fatty acids penetrate dry keratin micro-pores coating hair strands in a protective shield that locks in moisture and defines curls.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a curly hair styling and defining product from Cantu with pure shea butter ({weight_g}g)."),
        ("What are the benefits of pure shea butter for hair styling?", "Nourishes dry curly hair, tames frizz, and defines natural curls with flexible hold."),
        ("Does it define curls and control frizz without flakes?", "Yes, clinically proven to define curls and control frizz without leaving white flakes."),
        (f"What weight is contained in this container?", f"{weight_g}g."),
        ("How do I use it correctly?", "Apply to damp or dry hair section by section, style with fingers or wide-tooth comb."),
        ("Is it sulfate-free, silicone-free, and paraben-free?", "Yes, 100% free from sulfates, silicones, parabens, and mineral oil."),
        ("Where is Cantu Hair Product manufactured?", "In the USA by PDC Brands USA."),
        ("How do I verify authenticity at Ekleel Abha?", "All Cantu products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", "Invigorating tropical coconut and shea butter fragrance."),
        ("Is it suitable for curly, wavy, and coily hair?", "Yes, specifically formulated for curly, wavy, and coily hair textures."),
        (f"Does the {weight_g}g tub last long?", "Yes, lasts weeks of regular daily styling."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Cantu a global #1 curly hair brand?", "Yes, Cantu is the world's most recognized brand in curly hair care."),
        ("How many times daily?", "Whenever styling hair."),
        ("Does it impart shine and softness?", "Yes, gives hair a natural shine and touchable softness."),
        ("Is the container recyclable?", "Yes."),
        ("Does it prevent hair breakage and split ends?", "Yes, nourishes hair protecting ends from dryness and breakage."),
        ("Does it leave a sticky residue?", "Penetrates flexibly without sticky residue or heavy buildup."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for kids, women, and men?", "Yes, suitable for all user categories based on variant."),
        ("Does it shield hair against humidity?", "Yes, coats hair guarding against humidity-induced frizz."),
        ("Is it a great gift for curly hair lovers?", "Yes, an excellent gift for curly hair care routines."),
        ("Does it restore healthy hair appearance?", "Yes, restores natural vitality and beauty to hair styles."),
        ("Does it make daily styling easy?", "Yes, makes combing and styling curly hair smooth and effortless."),
        ("Are other Cantu products available?", "Yes, the full Cantu product line is available at Ekleel Abha.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Cantu",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. مستحضر تصفيف وتحديد الشعر الكيرلي بزبدة الشيا الصافية من كانتو. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Cantu pure shea butter curly hair styling and defining product. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2024():
    return _make_cantu_product(
        pid=2024, gtin="874211002685",
        ar_name="كريم مصفف وملمع الشعر بربدة الشيا من كانتو 113جم",
        en_name="Cantu Shea Butter Hair Dressing Pomade 113g",
        type_ar="بوماد كريم مصفف وملمع", type_en="Hair Dressing Pomade", weight_g=113,
        feature_ar="بوماد كلاسيكي مصفف وملمع بزبدة الشيا 113 جم", feature_en="classic hair dressing pomade for shine and hold 113g",
        tags_ar=["كانتو", "بوماد_كانتو", "كريم_مصفف_وملمع", "زبدة_الشيا_كانتو", "إكليل_أبها"],
        tags_en=["cantu", "cantu_pomade", "hair_dressing_pomade", "shea_butter_cantu", "ekleel_abha"]
    )


def create_product_2025():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>جل منظف للبشرة من افين 100 مل (Avène Cleansing Gel for Skin - 100 ml)</strong> الجل المنظف والمطهر الطبي الفاخر من أفين الفرنسية المصمم خصيصاً لتنظيف، تصفية، وتنظيم الإفرازات الدهنية لبشرة الوجه والجسم الدهنية والمختلطة والمعرضة لحب الشباب دون أي جفاف. يرتكز هذا الجل الأصيل (Avène Cleanance Cleansing Gel 100ml) على مياه أفين الحرارية المهدئة (Avène Thermal Spring Water)، مركب Comedoclastin المنظم للسيبوم، والمركبات المنظفة الخالية من الصابون القاسي.</p>
<p>يعمل جل أفين كلينانس على تنظيف مسام الوجه والجسم عمقاً من الدهون الزائدة والمكياج والشوائب، تقليل اللمعان الزائد والبثور دون تدمير حاجز الجلد، وتهدئة الاحمرار والتهيج، ليترك بشرتك ناعمة كالحرير، مطهرة، ناصعة النقاء، ومفعمة بالانتعاش من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تنظيف وتصفية فائقة للبشرة الدهنية والمختلطة:</strong> ينظف المسام من الزيوت والشوائب دون جفاف.</li>
  <li><strong>تنظيم الإفرازات الدهنية وتقليل اللمعان بمركب Comedoclastin:</strong> يقلل تكون البثور والكوميدونات.</li>
  <li><strong>تهدئة ولطف بمياه أفين الحرارية المهدئة:</strong> تمنع التهيج والاحمرار وتحفظ طراوة البشرة.</li>
  <li><strong>تركيبة خالية 100% من الصابون والبارابين:</strong> آمنة ولطيفة جداً ومختبرة جلدياً.</li>
  <li><strong>مناسب للوجه والجسم (أعلى الظهر والكتفين):</strong> غسول يومي مطهر شامل.</li>
  <li><strong>عبوة سعة 100 مل:</strong> حجم مدمج ممتاز للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي بشرة الوجه أو الجسم بالماء الدافئ.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من جل أفين وكوّني رغوة ناعمة ثم دلكي برفق بحركات دائرية.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء وجففي البشرة برفق (يُستعمل مرتين يومياً صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مياه أفين الحرارية الطبيعية:</strong> تلطف البشرة الحساسة وتخفف التهيج والاحمرار.</li>
  <li><strong>مركب Comedoclastin النباتي المنظم:</strong> ينظم عمل غدد السيبوم ويمنع تراكم الدهون في المسام.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الوجه والجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يملك بشرة دهنية أو مختلطة ويبحث عن جل أفين المنظف 100 مل للتنظيف وتصفية البثور.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>أفين (Avène)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / منظفات أفين الطبية للبشرة الدهنية والاكزيما 100ml</td></tr>
  <tr><th>نوع المنتج</th><td>جل منظف ومطهر خالي من الصابون للبشرة الدهنية بمركب Comedoclastin (100ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الدهنية، المختلطة، والمعرضة لحب الشباب والبثور</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة مطهرة، ناصعة النقاء، غير لامعة، ناعمة كالحرير وخالية من الدهون</td></tr>
  <tr><th>الملمس</th><td>جل سائل شفاف ينقلب لرغوة لطيفة ناعمة</td></tr>
  <tr><th>العطر</th><td>عطر أفين الطبي الناعم المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>مياه أفين الحرارية، مركب Comedoclastin، منظفات خالية من الصابون</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Pierre Fabre Dermo-Cosmétique France</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون والمراهقون (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد مركب Comedoclastin ومياه أفين الحرارية في Avène Cleanance</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج جل أفين مشكلة الزيوت والدهون الزائدة، انسداد المسام بالرؤوس السوداء والبيضاء، وحب الشباب الملتهب.</p>

<h3>لماذا تنجح تركيبة Comedoclastin؟</h3>
<p>لأن Comedoclastin المستخلص من بذور شوك الحليب يثبط تحول البصيلات السليمة إلى كوميدونات مجهرية قبل ظهور البثرة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنظيف مرتين يومياً بالماء الدافئ:</strong> ينظف الإفرازات الدهنية قبل أكسدتها.<br>
2. <strong>عدم الفرك الشديد بالليف القاسية:</strong> يمنع تحفيز الغدد الدهنية لإفراز المزيد من السيبوم.<br>
3. <strong>التكميل بمرطب مخصص للبشرة الدهنية:</strong> يحفظ توازن الماء دون زيوت.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "البشرة الدهنية يجب غسلها بكثرة 5-6 مرات يومياً بالصابون القاسي."<br>
<strong>الحقيقة:</strong> الغسيل الزائد يمنح رد فعل عكسي بجفاف ومضاعفة الإفرازات الدهنية، والتنظيف المتوازن بجل أفين مرتين يكفي بامتياز.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يقلل Comedoclastin حجم الغدد الدهنية بنسبة 20% ويثبط إنزيم 5-alpha reductase المستهدف لإنتاج السيبوم.</p>"""

    faqs = [
        ("ما هو جل منظف للبشرة من افين 100 مل؟", "هو جل منظف ومطهر طبي خالي من الصابون من أفين الفرنسية بمياه الحرارية للبشرة الدهنية والمختلطة (100 مل)."),
        ("ما هي فوائد مركب Comedoclastin ومياه أفين الحرارية؟", "ينظم Comedoclastin الدهون ويمنع البثور، بينما تلطف مياه أفين الحرارية التهيج والاحمرار."),
        ("هل ينظف المسام ويقلل الدهون واللمعان دون جفاف؟", "نعم، مثبت سريرياً في تنظيف المسام وتقليل اللمعان الزائد دون جفاف البشرة."),
        ("ما حجم العبوة؟", "تأتي بعبوة سائل مدمجة بسعة 100 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "بللي البشرة، ضعي كمية وكوّني رغوة، دلكي برفق واشطفي بالماء مرتين يومياً."),
        ("هل هو خالٍ من الصابون والبارابين؟", "نعم، 100% خالٍ من الصابون، البارابين ومختبر درماتولوجياً."),
        ("أين صُنع جل أفين؟", "صُنع في فرنسا بواسطة Pierre Fabre Dermo-Cosmétique France."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات أفين لدى إكليل أبها أصلية 100%."),
        ("ما رائحة جل أفين المنظف؟", "عطر أفين الطبي الناعم المنعش الأنيق."),
        ("هل يترك البشرة مطهرة وغير لامعة؟", "نعم، يترك البشرة مطهرة، ناصعة النقاء وغير لامعة بالدهون."),
        ("هل 100 مل مناسبة للحقيبة والسفر؟", "نعم، حجم أنيق مدمج مثالي لحقيبة اليد والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب الوجه والجسم (الظهر والكتفين)؟", "نعم، ممتاز لبثور الوجه والظهر والكتفين."),
        ("كم مرة يومياً؟", "مرتين يومياً (صباحاً ومساءً)."),
        ("هل أفين علامة طبية فرنسية عالمية؟", "نعم، Avène علامة أسطورية رائدة عالمياً في العناية بالبشرة الحساسة والدهنية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في تقليل الرؤوس السوداء والبيضاء؟", "نعم، ينظف الكوميدونات والزيوت المسببة للرؤوس السوداء والبيضاء."),
        ("هل يسبب جفافاً أو شد بالوجه؟", "لا، ينظف بلطف متوازن دون ترك شعور بالشد أو الجفاف."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء والمراهقين؟", "نعم، ممتاز للبشرة الدهنية للمراهقين والبالغين."),
        ("هل يفضل اتباع مرطب خفيف بعده؟", "نعم، يُفضل استخدام مرطب خفيف خالي من الزيوت بعد الغسل."),
        ("هل يقلل تهيج واحمرار حب الشباب؟", "نعم، مياه أفين الحرارية تلطف تهيج واحمرار حب الشباب."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية؟", "نعم، منتج طبي فاخر وأساسي للبشرة الدهنية."),
        ("هل يمتص ويجف بسهولة بعد الشطف؟", "نعم، ينشطف بالماء بسلاسة فائقة دون أثر لزج."),
        ("هل تتوفر منه أحجام أكبر لدى أفين؟", "نعم، تتوفر أحجام متعددة لدى Avène.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Avène Cleansing Gel for Skin - 100 ml</strong> is an authentic luxury medical soap-free purifying cleansing gel from Avène France designed to cleanse, clarify, and regulate sebum for oily, combination, and acne-prone facial and body skin without drying. Built upon soothing Avène Thermal Spring Water, sebum-regulating Comedoclastin, and mild soap-free cleansers.</p>
<p>Avène Cleanance Cleansing Gel deeply cleanses face and body pores of excess sebum, makeup, and impurities, reduces oily shine and breakouts without stripping the skin barrier, and soothes redness and irritation, leaving your skin touchably silky soft, purified, spotlessly clear, and refreshed from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Superior Pore Cleansing for Oily & Combination Skin:</strong> Cleanses pores of oil and impurities without dryness.</li>
  <li><strong>Sebum Regulation & Shine Control with Comedoclastin:</strong> Reduces pimples and comedone formation.</li>
  <li><strong>Soothing Care with Avène Thermal Spring Water:</strong> Prevents irritation and redness maintaining skin softness.</li>
  <li><strong>100% Soap-Free & Paraben-Free Formula:</strong> Dermatologically tested safe and gentle.</li>
  <li><strong>Suitable for Face & Body (Upper Back & Shoulders):</strong> Comprehensive daily purifying wash.</li>
  <li><strong>Compact 100ml Bottle:</strong> Ideal size for daily care, handbag, and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet face or body skin with warm water.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of Avène gel, work into a gentle lather, and massage in circular motions.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with water and pat skin dry (use twice daily morning and night).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural Avène Thermal Spring Water:</strong> Soothes sensitive skin calming irritation and redness.</li>
  <li><strong>Plant-Derived Comedoclastin Complex:</strong> Regulates sebum production preventing pore oil buildup.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical facial and body skin application.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with oily or combination skin seeking Avène Cleansing Gel 100ml for pore cleansing and acne clarity.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Avène</td></tr>
  <tr><th>Category</th><td>Skincare / Avène Cleanance Medical Oily Skin Cleansers 100ml</td></tr>
  <tr><th>Product Type</th><td>Soap-Free Purifying Cleansing Gel with Comedoclastin (100ml)</td></tr>
  <tr><th>Volume/Weight</th><td>100 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Oily, Combination & Acne-Prone Skin</td></tr>
  <tr><th>Finish</th><td>Purified, spotlessly clear, matte & silky soft oil-free skin</td></tr>
  <tr><th>Texture</th><td>Clear liquid gel transforming into a mild gentle lather</td></tr>
  <tr><th>Fragrance</th><td>Gentle medical Avène signature scent</td></tr>
  <tr><th>Active Ingredients</th><td>Avène Thermal Spring Water, Comedoclastin, Soap-Free Cleansers</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>Pierre Fabre Dermo-Cosmétique France</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Comedoclastin Sebum Reducer & Avène Thermal Spring Water Anti-Irritation</h2>

<h3>What problem does this solve?</h3>
<p>Avène Cleansing Gel resolves excess oil shine, blackheads, whiteheads, clogged pores, and inflamed acne breakouts.</p>

<h3>Why choose Avène Cleanance Gel?</h3>
<p>Comedoclastin derived from Milk Thistle seeds inhibits micro-comedone formation while Avène Thermal Water calms irritation.</p>"""

    en_faqs = [
        ("What is Avène Cleansing Gel for Skin - 100 ml?", "It is a medical soap-free purifying cleansing gel from Avène France with Thermal Spring Water for oily and combination skin (100ml)."),
        ("What are the benefits of Comedoclastin and Avène Thermal Spring Water?", "Comedoclastin regulates sebum preventing pimples, while Avène Thermal Water calms irritation and redness."),
        ("Does it clean pores and control oil shine without dryness?", "Yes, clinically proven to clean pores and reduce excess shine without drying skin."),
        ("What volume is contained in this bottle?", "100ml bottle."),
        ("How do I use it correctly?", "Wet skin, apply gel, lather, massage gently and rinse with water twice daily."),
        ("Is it soap-free and paraben-free?", "Yes, 100% soap-free, paraben-free, and dermatologically tested."),
        ("Where is Avène Cleansing Gel manufactured?", "In France by Pierre Fabre Dermo-Cosmétique France."),
        ("How do I verify authenticity at Ekleel Abha?", "All Avène products at Ekleel Abha are 100% original."),
        ("What scent does Avène Cleansing Gel have?", "Gentle medical fresh Avène signature scent."),
        ("Does it leave skin purified and matte?", "Yes, leaves skin purified, spotlessly clear, and matte."),
        ("Is the 100ml bottle handbag friendly?", "Yes, sleek compact bottle ideal for handbag and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for face and body (back and shoulders)?", "Yes, excellent for facial, back, and shoulder acne."),
        ("How many times daily?", "Twice daily (morning and night)."),
        ("Is Avène a global leading French medical brand?", "Yes, Avène is a globally leading brand in sensitive and oily skincare."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it help reduce blackheads and whiteheads?", "Yes, cleanses comedones and sebum causing blackheads and whiteheads."),
        ("Does it cause skin tightness or dryness?", "No, cleanses gently without tight dry feeling."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for teens and adults?", "Yes, excellent for oily skin in teens and adults."),
        ("Is it recommended to follow with an oil-free moisturizer?", "Yes, follow with an oil-free moisturizer after cleansing."),
        ("Does it reduce acne irritation and redness?", "Yes, Avène Thermal Water calms acne irritation and redness."),
        ("Is it a practical medical skincare gift?", "Yes, a premier medical essential for oily skin care."),
        ("Does it rinse off easily?", "Yes, rinses off smoothly with water without sticky residue."),
        ("Are larger sizes available from Avène?", "Yes, multiple sizes are available from Avène.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2025",
        "sku": "EK-2025",
        "gtin": "3282770207712",
        "brand": "Avène",
        "ar": {
            "title": "جل منظف للبشرة من افين 100 مل",
            "meta_title": "جل أفين المنظف للبشرة الدهنية 100مل | إكليل أبها",
            "meta_description": "اشتري جل منظف للبشرة من أفين (100 مل). جل طبي خالي من الصابون بمياه أفين الحرارية للبشرة الدهنية والمختلطة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["افين", "جل_منظف_افين", "افين_كلينانس", "تنظيف_البشرة_الدهنية", "إكليل_أبها"]
        },
        "en": {
            "title": "Avène Cleansing Gel for Skin - 100 ml",
            "meta_title": "Avène Cleansing Gel 100ml | Ekleel Abha",
            "meta_description": "Buy original Avène Cleansing Gel for Skin (100ml). French soap-free medical purifying gel for oily skin. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["avene", "avene_cleansing_gel", "avene_cleanance", "oily_skin_cleanser", "ekleel_abha"]
        }
    }


def create_product_2026():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>جلي البشرة الطبي من كوفيكس 100مل (Cofix Medical Skin Jelly 100ml)</strong> الفازلين والجلي الطبي النقي الفائق من كوفيكس المصمم خصيصاً لحماية وترطيب وعزل بشرة الوجه والشفتين والجسم واليدين والقدمين من التشققات والجفاف الشديد. يرتكز هذا الجلي الطبي الاصيل (Cofix Skin Jelly 100ml) على البترولاتوم النقي المصفى 100% (100% Pure Petroleum Jelly) والشحوم الواقية لحاجز البشرة.</p>
<p>يعمل جلي كوفيكس الطبي على تشكيل غلاف عازل واقٍ يحبس الرطوبة الداخلية بنسبة 99%، شفاء تشققات الشفتين واليدين والكعبين، وحماية الجروح والحروق السطحية من المؤثرات الخارجية، ليترك بشرتك ناعمة كالحرير، محمية، وماطرة بالترطيب من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حبس الرطوبة وعزل البشرة بنسبة 99% بالبترولاتوم النقي:</strong> يعالج التشققات والجفاف الشديد.</li>
  <li><strong>شفاء وتنعيم تشققات الكعبين والشفتين واليدين:</strong> يسرّع التئام الجلد المتشقق والتالف.</li>
  <li><strong>حماية الجروح والحروق السطحية والتسلخات:</strong> يشكل حجاباً واقياً من الجراثيم والماء.</li>
  <li><strong>خالٍ 100% من العطور والصبغات والمواد الكيميائية:</strong> آمن ولطيف للغاية على البشرة الأكثر حساسية.</li>
  <li><strong>مناسب لجميع أفراد الأسرة ولعناية الأطفال بالاحتفاظ بالرطوبة:</strong> جلي العناية الوقائية الشاملة.</li>
  <li><strong>عبوة مدمجة سعة 100 مل:</strong> حجم ممتاز للاستخدام اليومي والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسبة من جلي كوفيكس على بشرة جافة ونظيفة.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي برفق على الشفتين أو اليدين أو الكعبين أو المناطق شديدة الجفاف والمتشققة حتى التغطية الكاملة (يُستعمل عند الحاجة وقبل النوم).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>البترولاتوم الطبي النقي 100%:</strong> يشكل غشاءً عازلاً يمنع تبخر الماء من كيراتين الجلد العميق.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي فقط.</li>
  <li>تجنبي التلامس مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن جلي كوفيكس الطبي 100 مل لعزل الترطيب وشفاء تشققات البشرة والشفتين.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كوفيكس (Cofix)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / الفازلين والجلي الطبي لحماية البشرة والتشققات 100ml</td></tr>
  <tr><th>نوع المنتج</th><td>جلي طبي عازل ومحمٍ من التشققات بـ 100% بترولاتوم نقي (100ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>100 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة شديدة الجفاف، المتشققة، والحساسة (الشفتين، اليدين والقدمين)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة ناعمة، مشفية من التشققات، معزولة الترطيب ومحمية 24 ساعة</td></tr>
  <tr><th>الملمس</th><td>جلي ناعم دسم يشكل غلافاً واقياً</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور (محايد)</td></tr>
  <tr><th>المكونات النشطة</th><td>بترولاتوم طبي نقي 100% (Pure Petroleum Jelly)</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الصين</td></tr>
  <tr><th>الشركة المصنعة</th><td>Cofix Care Products</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من الرضع حتى البالغين)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد البترولاتوم النقي في جلي كوفيكس الطبي (Cofix Jelly)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج جلي كوفيكس الطبي تشققات الشفتين المؤلمة، جفاف خشونة القدمين، تسلخات الجلد، والجفاف الشديد الناتجة عن البرد.</p>

<h3>لماذا تنجح تركيبة Pure Petroleum Jelly؟</h3>
<p>لأن البترولاتوم النقي 100% يعزل سطح الجلد المجهد تماماً مانعاً نفاذية الماء (Transepidermal Water Loss) بنسبة 99%.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على الشفتين والكعبين قبل النوم:</strong> يضاعف سرعة التئام التشققات.<br>
2. <strong>الحماية قبل التعرض للبرد الشديد والماء:</strong> يمنع تسلخ وجفاف الجلد المباشر.<br>
3. <strong>الاستخدام الآمن للأطفال والرضع:</strong> يقي منطقة الحفاض من التسلخات والتهيج.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الجلي الطبي يسبب اسمرار البشرة."<br>
<strong>الحقيقة:</strong> الجلي الطبي مادة ناتجة عن تنقية عالية لا تسبب التسمر بل تحمي البشرة من الاحتكاك المسبب للاسمرار.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يشكل البترولاتوم طبقة كارهة للماء (Hydrophobic Layer) تحتبس الرطوبة الطبيعية داخل الخلايا الكيراتينية.</p>"""

    faqs = [
        ("ما هو جلي البشرة الطبي من كوفيكس 100مل؟", "هو فازلين وجلي طبي نقي 100% من كوفيكس لعزل الترطيب وشفاء تشققات البشرة والشفتين (100 مل)."),
        ("ما هي فوائد البترولاتوم الطبي النقي 100%؟", "يحبس رطوبة البشرة بنسبة 99%، يشفي تشققات الشفتين والكعبين، ويحمي الجلد من الجفاف والبرد."),
        ("هل يشفي التشققات والجفاف الشديد بفاعلية؟", "نعم، مثبت سريرياً في شفاء تشققات الشفتين واليدين والقدمين وحماية الجلد."),
        ("ما حجم العبوة؟", "تأتي بعبوة أنبوب سعة 100 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية مناسبة على الشفتين أو الكعبين أو البشرة الجافة ودلكي عند الحاجة وقبل النوم."),
        ("هل هو خالٍ من العطور والصبغات؟", "نعم، 100% خالٍ من العطور والصبغات والمواد الكيميائية."),
        ("أين صُنع جلي كوفيكس؟", "صُنع بأعلى معايير جودة المستحضرات الطبية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كوفيكس لدى إكليل أبها أصلية 100%."),
        ("هل يناسب الرضع والأطفال والبالغين؟", "نعم، آمن وممتاز لجميع الفئات العمرية من الرضع حتى البالغين."),
        ("هل يمنع تسلخات منطقة الحفاض للأطفال؟", "نعم، يشكل حماية عازلة ممتازة لوقاية بشرة الرضع من التسلخات."),
        ("هل أنبوب 100 مل مناسب للحقيبة؟", "نعم، حجم أنيق مدمج مثالي لحقيبة اليد والسفر."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل يناسب الشفتين واليدين والقدمين؟", "نعم، جلي شامل ممتاز للشفتين واليدين والقدمين والركبتين."),
        ("كم مرة يومياً؟", "عند الحاجة وخاصة قبل النوم."),
        ("هل يحمي الحروق والجروح السطحية؟", "نعم، يشكل حجاباً واقياً يحمي الجروح السطحية من الماء والجراثيم."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع تشقق الشفتين واليدين في الشتاء؟", "نعم، الحماية العازلة المثالية ضد جفاف وبرد الشتاء."),
        ("هل يترك ملمساً حمائياً ناعماً؟", "نعم، يغلف الجلد بطبقة حمائية ناعمة جداً."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يسبب حساسية بالجلد؟", "لا، خامل طبيعي وآمن للغاية على البشرة الحساسة."),
        ("هل يصلح هدية مفيدة لكل منزل؟", "نعم، منتج طبي أساسي لا غنى عنه في كل بيت."),
        ("هل يمنح ترطيباً ممتداً؟", "نعم، يحبس الترطيب الداخلي طوال 24 ساعة."),
        ("هل ينعم الكعبين المتصلبين؟", "نعم، ينعم الكعبين والقدمين المتصلبتين بفاعلية."),
        ("هل يتوفر الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها."),
        ("هل يحمي من برد الجفاف الشتوي؟", "نعم، يمنح وقاية عازلة ممتازة ضد طقس الشتاء الشديد.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Cofix Medical Skin Jelly 100ml</strong> is an authentic pure medical petroleum skin jelly from Cofix formulated to protect, hydrate, isolate, and repair facial, lip, body, hand, and foot skin against severe dryness and cracking. Built upon 100% Pure Medical Grade Petroleum Jelly and protective skin barrier lipids.</p>
<p>Cofix Medical Skin Jelly forms a protective occlusive shield locking in 99% of internal skin moisture, accelerates healing of cracked lips, hands, and heels, and protects minor cuts and burns from external elements, leaving your skin touchably silky soft, protected, and hydrated from first application.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>99% Moisture Lock & Skin Shielding with Pure Petroleum Jelly:</strong> Treats severe dryness and cracking.</li>
  <li><strong>Healing & Softening for Cracked Heels, Lips & Hands:</strong> Accelerates healing of cracked damaged skin.</li>
  <li><strong>Protective Shield for Minor Cuts, Burns & Chafing:</strong> Forms a barrier guarding against water and germs.</li>
  <li><strong>100% Fragrance-Free, Dye-Free & Chemical-Free:</strong> Safe and gentle on ultra-sensitive skin.</li>
  <li><strong>Suitable for Whole Family & Diaper Rash Prevention:</strong> Comprehensive protective family care.</li>
  <li><strong>Compact 100ml Tube Container:</strong> Excellent volume for daily care, handbag, and travel.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of Cofix jelly onto clean dry skin.</li>
  <li><strong>Step 2:</strong> Spread gently over lips, hands, heels, or extra dry cracked areas until fully covered (use as needed & bedtime).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>100% Pure Medical Petroleum Jelly:</strong> Forms an occlusive hydrophobic layer preventing transepidermal water evaporation.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical skin application only.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking Cofix Medical Skin Jelly 100ml for moisture sealing and healing cracked skin and lips.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Cofix</td></tr>
  <tr><th>Category</th><td>Skincare / Cofix Medical Petroleum Skin Jellies 100ml</td></tr>
  <tr><th>Product Type</th><td>100% Pure Medical Petroleum Occlusive Skin Repair Jelly (100ml)</td></tr>
  <tr><th>Volume/Weight</th><td>100 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Severely Dry, Cracked & Sensitive Skin (Lips, Hands & Feet)</td></tr>
  <tr><th>Finish</th><td>Soft, crack-healed, moisture-sealed & 24H protected skin</td></tr>
  <tr><th>Texture</th><td>Rich smooth protective jelly fluid</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (neutral)</td></tr>
  <tr><th>Active Ingredients</th><td>100% Pure Medical Petroleum Jelly</td></tr>
  <tr><th>Country of Origin</th><td>KSA / China</td></tr>
  <tr><th>Manufacturer</th><td>Cofix Care Products</td></tr>
  <tr><th>Age Group</th><td>All Ages (Infants, Children & Adults)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of 100% Hydrophobic Petroleum Occlusion & Transepidermal Moisture Preservation</h2>

<h3>What problem does this solve?</h3>
<p>Cofix Medical Skin Jelly resolves painful cracked lips, rough cracked heels, diaper chafing, and severe cold dryness.</p>

<h3>Why choose Cofix Medical Skin Jelly?</h3>
<p>100% Pure Petroleum Jelly forms a hydrophobic barrier reducing transepidermal water loss (TEWL) by up to 99%.</p>"""

    en_faqs = [
        ("What is Cofix Medical Skin Jelly 100ml?", "It is a 100% pure medical petroleum jelly from Cofix for moisture sealing and healing cracked skin and lips (100ml)."),
        ("What are the benefits of 100% pure medical petroleum jelly?", "Locks in 99% skin moisture, heals cracked lips and heels, and protects skin against dryness and cold."),
        ("Does it effectively heal severe dryness and cracked skin?", "Yes, clinically proven to heal cracked lips, hands, and feet while shielding skin."),
        ("What volume is contained in this tube?", "100ml tube."),
        ("How do I use it correctly?", "Apply a suitable amount on lips, heels, or dry skin, massage as needed and bedtime."),
        ("Is it fragrance-free and chemical-free?", "Yes, 100% free from fragrances, dyes, and harsh chemicals."),
        ("Where is Cofix Medical Skin Jelly manufactured?", "Manufactured to medical care quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Cofix products at Ekleel Abha are 100% original."),
        ("Is it safe for infants, children, and adults?", "Yes, safe and excellent for all ages from infants to adults."),
        ("Does it help prevent diaper rash in babies?", "Yes, forms an excellent protective barrier guarding infant skin against diaper chafing."),
        ("Is the 100ml tube handbag friendly?", "Yes, sleek compact tube ideal for handbag and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it suitable for lips, hands, and feet?", "Yes, versatile jelly excellent for lips, hands, feet, and elbows."),
        ("How many times daily?", "As needed, especially bedtime."),
        ("Does it protect minor cuts and burns?", "Yes, forms a protective shield guarding minor cuts from water and germs."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it prevent winter skin cracking?", "Yes, superior occlusive defense against winter cold dryness."),
        ("Does it leave a soft protective coating?", "Yes, coats skin in a very soft protective layer."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Does it cause skin allergies?", "No, naturally inert and extremely safe for sensitive skin."),
        ("Is it a practical medical gift?", "Yes, an essential medical item for every household."),
        ("Does it deliver long-lasting hydration sealing?", "Yes, seals internal moisture for 24 continuous hours."),
        ("Does it soften calloused heels?", "Yes, effectively softens calloused heels and feet."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy."),
        ("Does it protect against winter cold dryness?", "Yes, provides superior occlusive protection against harsh winter cold weather.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2026",
        "sku": "EK-2026",
        "gtin": "697794487720",
        "brand": "Cofix",
        "ar": {
            "title": "جلي البشرة الطبي من كوفيكس 100مل",
            "meta_title": "جلي كوفيكس الطبي للبشرة 100مل | إكليل أبها",
            "meta_description": "اشتري جلي البشرة الطبي من كوفيكس (100 مل). فازلين طبي نقي 100% لعزل الترطيب وشفاء تشققات الشفتين واليدين والقدمين. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["كوفيكس", "جلي_كوفيكس_الطبي", "فازلين_طبي", "علاج_التشققات", "إكليل_أبها"]
        },
        "en": {
            "title": "Cofix Medical Skin Jelly 100ml",
            "meta_title": "Cofix Medical Skin Jelly 100ml | Ekleel Abha",
            "meta_description": "Buy original Cofix Medical Skin Jelly (100ml). 100% Pure medical petroleum occlusive skin repair jelly. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["cofix", "cofix_skin_jelly", "petroleum_jelly", "skin_repair_jelly", "ekleel_abha"]
        }
    }


def create_product_2027():
    return _make_cantu_product(
        pid=2027, gtin="817513015434",
        ar_name="كريم كير فور كيدز مصفف شعر الاطفال من كانتو 227جم",
        en_name="Cantu Care for Kids Styling Custard 227g",
        type_ar="كاسترد مصفف ومحدد لشعر الأطفال", type_en="Kids Styling Custard", weight_g=227,
        feature_ar="كاسترد مخصص لتصفيف وتحديد شعر الأطفال بزبدة الشيا والعسل 227 جم", feature_en="specially formulated kids styling custard with shea butter and honey 227g",
        tags_ar=["كانتو", "كانتو_اطفال", "مصفف_شعر_الاطفال", "كاسترد_كانتو", "إكليل_أبها"],
        tags_en=["cantu", "cantu_care_for_kids", "kids_styling_custard", "cantu_kids", "ekleel_abha"]
    )


print("Loaded all 5 Batch 62 builders complete")
