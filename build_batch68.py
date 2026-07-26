import json, os

def create_product_2055():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>شامبو بالبروتين للشعر الجاف والتالف 500مل (Protein Shampoo for Dry and Damaged Hair - 500ml)</strong> الشامبو العلاجي المغذي والمجدد الفاخر المصمم خصيصاً لإعادة بناء وترميم وترطيب الشعر الجاف والتالف والمتقصف بفعل الصبغات والحرارة والتقلبات الجوية. يرتكز هذا الشامبو الأصيل (Protein Shampoo 500ml) على بروتينات الكيراتين والقمح السائلة (Hydrolyzed Proteins)، الزيوت النباتية المغذية، والمركبات المرطبة لبصيلات الشعر.</p>
<p>يعمل شامبو البروتين للشعر الجاف على اختراق قشرة الكيراتين عمقاً، تغذية الشعر بالبروتينات والأحماض الأمينية الأساسية، وتنظيف فروة الرأس بلطف دون انتزاع الزيوت الطبيعية، ليترك شعرك ناعماً كالحرير، مرناً، قريباً من التجدد الكامل، ومحمياً من الهيشان والتقصف من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترميم وإعادة بناء الكيراتين بالبروتينات السائلة:</strong> يصلح الشعر التالف والمجهد من الصبغة والحرارة.</li>
  <li><strong>تنظيف لطيف وترطيب عميق للشعر الجاف:</strong> ينظف الفروة دون تسبيب أي جفاف أو حكة.</li>
  <li><strong>منع التكسر والتقصف والهيشان:</strong> يعزز مرونة الخصلات ويغلف ألياف الشعر بحجاب حمائي.</li>
  <li><strong>إعادة اللمعان والنعومة الحريرية:</strong> يمنح الشعر مظهراً صحياً ناصع الحيوية.</li>
  <li><strong>تركيبة خالية من الكبريتات والبارابين القاسية:</strong> آمنة ومخصصة للشعر المجهد والمعالج.</li>
  <li><strong>عبوة ضخمة اقتصادية سعة 500 مل:</strong> حجم ممتاز للاستخدام العائلي اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> بللي الشعر وفروة الرأس بالماء الدافئ.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة من شامبو البروتين ودلكي الفروة والشعر برفق برغوة غنية لكريمية.</li>
  <li><strong>الخطوة الثالثة:</strong> اشطفي جيداً بالماء الدافئ وكرري العملية عند الحاجة (يُستعمل 2-3 مرات أسبوعياً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>البروتينات السائلة (Hydrolyzed Protein):</strong> تتغلغل داخل ثقوب الكيراتين وترمم ألياف الشعر المكسورة.</li>
  <li><strong>المكونات المنظفة اللطيفة والزيوت المغذية:</strong> تنظف الفروة وتحفظ الرطوبة الداخلية للشعر.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على الشعر وفروة الرأس.</li>
  <li>تجنبي التلامس المباشر مع العينين واشطفي بالماء في حال التلامس.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يعاني من الشعر الجاف والتالف ويبحث عن شامبو البروتين 500 مل للتغذية والترميم.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>شامبو البروتين (Protein Care)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / شامبوهات البروتين للشعر الجاف والتالف 500ml</td></tr>
  <tr><th>نوع المنتج</th><td>شامبو علاجي مغذي بالبروتين السائل للشعر الجاف والتالف (500ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>500 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>الشعر الجاف، التالف، المجهد بالصبغة والحرارة، والمتقصف</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم كالحرير، مرمم من التقصف، مرطب ومفعم بالحيوية</td></tr>
  <tr><th>الملمس</th><td>سائل شامبو غني ينقلب لرغوة ناعمة كريمية</td></tr>
  <tr><th>العطر</th><td>عطر صالونات التجميل الفاخر المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>بروتينات سائلة (Hydrolyzed Protein)، كيراتين، زيوت مغذية</td></tr>
  <tr><th>بلد المنشأ</th><td>إيطاليا (Italy)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Professional Hair Care Italy</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد البروتينات السائلة في شامبو البروتين للشعر الجاف (Protein Shampoo)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج شامبو البروتين مشكلة تكسر وتقصف الشعر الجاف والتالف، فقدان المرونة، والتلف الناتج عن الصبغات والحرارة.</p>

<h3>لماذا تنجح تركيبة Hydrolyzed Protein؟</h3>
<p>لأن جزيئات البروتين الهيدروليزية الصغيرة تخترق ثقوب قشرة الشعر الكيراتينية وتملأ الفراغات المكسورة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التدليك اللطيف بماء دافئ:</strong> ينشط الدورة الدموية بفروة الرأس.<br>
2. <strong>التكميل ببلسم أو ماسك مرطب:</strong> يحفظ الترطيب الداخلي للشعر.<br>
3. <strong>تجنب استخدام الحرارة العالية فور الغسل:</strong> يمنح الشعر فرصة لاستعادة مرونته.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "شامبوهات البروتين تسبب تيبس الشعر."<br>
<strong>الحقيقة:</strong> هذا الشامبو مدعم بمركبات مرطبة توازن نسبة البروتين والماء لمنح النعومة وال مرونة.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>ترتبط الأحماض الأمينية بساق الشعر مشكلة خيوط ببتيدية تدعم هيكل الكيراتين المجهد.</p>"""

    faqs = [
        ("ما هو شامبو بالبروتين للشعر الجاف والتالف 500مل؟", "هو شامبو علاجي إيطالي فاخر ببروتينات الكيراتين السائلة لترميم وتغذية الشعر الجاف والتالف (500 مل)."),
        ("ما هي فوائد البروتينات السائلة للشعر الجاف والتالف؟", "ترمم ألياف الشعر المكسورة، تقوي ساق الشعر، وتمنع التقصف والتكسر."),
        ("هل يرمم التلف ويمنح نعومة من الاستخدام الأول؟", "نعم، مثبت سريرياً في ترميم تلف الكيراتين وتغذية الشعر الجاف وتنعيمه."),
        ("ما حجم العبوة؟", "تأتي بعبوة ضخمة بسعة 500 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي على شعر مبلل، دلكي الفروة برغوة كريمية واشطفي بالماء الدافئ 2-3 مرات أسبوعياً."),
        ("هل هو خالٍ من الكبريتات والبارابين القاسية؟", "نعم، تركيبة متوازنة آمنة للشعر المعالج بالصبغة والبروتين."),
        ("أين صُنع شامبو البروتين؟", "صُنع في إيطاليا وفق معايير جودة العناية بالشعر العالمية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع المنتجات لدى إكليل أبها أصلية 100%."),
        ("ما رائحة شامبو البروتين؟", "عطر صالونات التجميل الفاخر المنعش."),
        ("هل يناسب الشعر المصبوغ والمعالج كيميائياً؟", "نعم، ممتاز للشعر المصبوغ والمعالج بالبروتين والكيراتين."),
        ("هل عبوة 500 مل تكفي للاستخدام العائلي؟", "نعم، عبوة ضخمة تكفي لعدة أشهر من الاستخدام العائلي."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل هو ماركة موثوقة في علاج الشعر التالف؟", "نعم، علامة احترافية موثوقة في مستحضرات البروتين."),
        ("كم مرة أسبوعياً؟", "2 إلى 3 مرات أسبوعياً."),
        ("هل يمنح الشعر لمعاناً وطراوة حريرية؟", "نعم، يمنح الشعر بريقاً ناعماً وطراوة حريرية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في تقليل هيشان الشعر؟", "نعم، يسيطر على الهيشان والتطاير الناتجة عن الجفاف."),
        ("هل يمنع تكسر الأطراف؟", "نعم، يغلف أطراف الشعر ويحميها من التكسر."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل ينظف الفروة بلطف دون جفاف؟", "نعم، ينظف الفروة بفاعلية دون انتزاع الزيوت الطبيعية."),
        ("هل يفضل اتباع بلسم مرطب بعده؟", "نعم، يُفضل استخدام بلسم مرطب لدعم نتائج الترميم."),
        ("هل يصلح هدية ممتازة ضمن روتين العناية بالشعر؟", "نعم، منتج فاخر وأساسي لكل روتين عناية."),
        ("هل يعيد المرونة والحيوية للشعر؟", "نعم، يعيد الحيوية والقوة للشعر المجهد."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Protein Shampoo for Dry and Damaged Hair - 500ml</strong> is an authentic luxury Italian medical repairing and nourishing shampoo engineered to rebuild, restore, and deeply hydrate dry, damaged, and brittle hair stressed by dyes, heat styling, and environmental factors. Built upon liquid hydrolyzed wheat and keratin proteins, nourishing plant oils, and hair follicle hydrators.</p>
<p>Protein Shampoo for dry hair deeply penetrates the keratin cortex, infusing hair strands with essential amino acids and proteins while gently cleansing the scalp without stripping natural oils, leaving your hair touchably silky soft, flexible, deeply renewed, and protected against breakage and frizz from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Keratin Repair & Structural Rebuilding with Hydrolyzed Proteins:</strong> Restores hair damaged by dye and heat.</li>
  <li><strong>Gentle Cleansing & Deep Hydration for Dry Hair:</strong> Cleanses scalp without drying or causing itchiness.</li>
  <li><strong>Breakage, Split-End & Frizz Control:</strong> Boosts hair strand elasticity wrapping fibers in a protective shield.</li>
  <li><strong>Luminous Shine & Silky Softness Restoration:</strong> Delivers a healthy vibrant hair finish.</li>
  <li><strong>Sulfate-Free & Paraben-Free Formula:</strong> Safe clean formula for chemically processed hair.</li>
  <li><strong>Generous 500ml Family Value Bottle:</strong> Excellent size for daily continuous family use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wet hair and scalp with warm water.</li>
  <li><strong>Step 2:</strong> Apply a suitable amount of Protein Shampoo and massage scalp gently into a rich creamy lather.</li>
  <li><strong>Step 3:</strong> Rinse thoroughly with warm water and repeat if desired (use 2-3 times weekly).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Hydrolyzed Proteins:</strong> Penetrate deep keratin pores rebuilding broken hair fibers.</li>
  <li><strong>Gentle Cleansers & Plant Oils:</strong> Cleanse scalp while locking in internal hair moisture.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical hair and scalp application.</li>
  <li>Avoid direct contact with eyes; rinse with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone suffering from dry damaged hair seeking Protein Shampoo 500ml for nutrition and repair.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Protein Care</td></tr>
  <tr><th>Category</th><td>Hair Care / Protein Repairing Shampoos for Dry Hair 500ml</td></tr>
  <tr><th>Product Type</th><td>Hydrolyzed Protein Repairing & Nourishing Shampoo for Dry Hair (500ml)</td></tr>
  <tr><th>Volume/Weight</th><td>500 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Dry, Damaged, Heat-Stressed & Color-Treated Hair</td></tr>
  <tr><th>Finish</th><td>Silky soft, repaired, deeply hydrated & vibrant hair</td></tr>
  <tr><th>Texture</th><td>Rich smooth liquid shampoo forming a creamy lather</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh salon-grade fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>Hydrolyzed Protein, Keratin, Nourishing Oils</td></tr>
  <tr><th>Country of Origin</th><td>Italy</td></tr>
  <tr><th>Manufacturer</th><td>Professional Hair Care Italy</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Hydrolyzed Protein Cuticle Impregnation & Keratin Restoration</h2>

<h3>What problem does this solve?</h3>
<p>Protein Shampoo resolves hair breakage, split ends, loss of elasticity, and chemical/heat damage in dry hair.</p>

<h3>Why choose Hydrolyzed Protein Shampoo?</h3>
<p>Small hydrolyzed protein micro-molecules penetrate keratin cortex pores filling structural gaps and reinforcing strength.</p>"""

    en_faqs = [
        ("What is Protein Shampoo for Dry and Damaged Hair - 500ml?", "It is a luxury Italian medical repairing shampoo with liquid proteins for dry and damaged hair (500ml)."),
        ("What are the benefits of hydrolyzed proteins for dry hair?", "Rebuild broken hair fibers, reinforce hair shafts, and prevent split ends and breakage."),
        ("Does it repair damage and deliver softness from first use?", "Yes, clinically proven to repair keratin damage, nourish dry hair, and soften strands."),
        ("What volume is contained in this bottle?", "500ml family size bottle."),
        ("How do I use it correctly?", "Apply to wet hair, massage into a creamy lather, and rinse with warm water 2-3 times weekly."),
        ("Is it safe for color-treated and chemically processed hair?", "Yes, safe and gentle formula for color-treated and chemically processed hair."),
        ("Where is Protein Shampoo manufactured?", "In Italy according to international hair care standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% original."),
        ("What scent does Protein Shampoo have?", "Luxurious fresh salon-grade fragrance."),
        ("Is it suitable for color-treated hair?", "Yes, excellent for color-treated, protein-treated, and damaged hair."),
        ("Does the 500ml bottle last long for family use?", "Yes, generous size lasting months of regular family use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is it a trusted brand in hair repair?", "Yes, a trusted professional brand in hair protein treatments."),
        ("How many times weekly?", "2 to 3 times weekly."),
        ("Does it impart shine and silky softness?", "Yes, coats hair in natural luster and touchable softness."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help control hair frizz?", "Yes, controls frizz and flyaways caused by dryness."),
        ("Does it prevent split ends?", "Yes, coats hair ends protecting them from splitting."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Does it cleanse scalp gently without dryness?", "Yes, cleanses scalp effectively without stripping natural oils."),
        ("Is following with a conditioner recommended?", "Yes, follow with a hydrating conditioner for optimal repair."),
        ("Is it a nice hair care gift?", "Yes, a premier treatment essential for hair care routines."),
        ("Does it restore elasticity and vitality?", "Yes, restores strength and life to stressed hair."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "2055",
        "sku": "EK-2055",
        "gtin": "8022297067391",
        "brand": "Protein Care",
        "ar": {
            "title": "شامبو بالبروتين للشعر الجاف والتالف 500مل",
            "meta_title": "شامبو البروتين للشعر الجاف والتالف 500مل | إكليل أبها",
            "meta_description": "اشتري شامبو بالبروتين للشعر الجاف والتالف (500 مل). شامبو إيطالي طبي بالبروتينات السائلة لترميم وتغذية الشعر المتقصف والجاف. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": ["شامبو_البروتين", "شامبو_الشعر_الجاف", "ترميم_الشعر_التالف", "شامبو_إيطالي", "إكليل_أبها"]
        },
        "en": {
            "title": "Protein Shampoo for Dry and Damaged Hair - 500ml",
            "meta_title": "Protein Shampoo Dry & Damaged Hair 500ml | Ekleel Abha",
            "meta_description": "Buy original Protein Shampoo for Dry and Damaged Hair (500ml). Italian hydrolyzed protein repairing shampoo. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": ["protein_shampoo", "dry_hair_shampoo", "damaged_hair_shampoo", "italian_hair_care", "ekleel_abha"]
        }
    }


def _make_cofix_product_b68(pid, gtin, ar_name, en_name, key_ing_ar, key_ing_en, feature_ar, feature_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{ar_name}</strong> مستحضر الترطيب والتغذية الفاخر غير الدهني الأصيل من كوفيكس المصمم خصيصاً لتنظيف، ترطيب، وتنعيم بشرة الجسم والوجه والتخلص من الخشونة والجفاف. يرتكز هذا المستحضر الأصيل ({en_name}) على خلاصات {key_ing_ar}، الجليسرين المرطب، والمركبات المغذية لبشرة الجسم.</p>
<p>يعمل مستحضر كوفيكس على تغذية بشرة الجسم عمقاً، حفظ الرطوبة الداخلية لـ 24 ساعة دون أي أثر دهني، وإضفاء بريق ونعومة حريرية على الجلد، ليترك جسمك مرطباً بجمال، مرناً، ومعطراً بالنظافة والانتعاش من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب وتغذية مكثفة غير دهنية لـ 24 ساعة بـ {key_ing_ar}:</strong> يمنح الجلد ليونة ونعومة حريرية.</li>
  <li><strong>امتصاص فوري وسريع دون ترك أي طبقة دهنية ثقيلة:</strong> مناسب للاستخدام اليومي والارتداء السريع للملابس.</li>
  <li><strong>حماية البشرة من الخشونة والجفاف والتشققات:</strong> يعزز حاجز الترطيب الطبيعي للجلد.</li>
  <li><strong>عطر منعش فواح يدوم طوال اليوم:</strong> يغلف الجسم بعبير زكي وأنيق.</li>
  <li><strong>تركيبة آمنة ومختبرة جلدياً لجميع أنواع البشرة:</strong> خالية من البارابين والمواد القاسية.</li>
  <li><strong>عبوة ضخمة مزودة بضاغط سعة 400 مل:</strong> حجم ممتاز للاستخدام العائلي اليومي المستمر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> ضعي كمية مناسبة من مستحضر كوفيكس على بشرة الجسم النظيفة بعد الاستحمام.</li>
  <li><strong>الخطوة الثانية:</strong> دلكي برفق بحركات دائرية ناعمة حتى الامتصاص الكامل (يُستعمل يومياً صباحاً ومساءً).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصات {key_ing_ar} والجليسرين:</strong> تحفظان التوازن المائي للجلد وتمنحان نعومة فائقة.</li>
  <li><strong>المكونات المنعشة غير الدهنية:</strong> تنفذ لعمق المسام دون تسبيب لزوجة أو انسداد.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على بشرة الجسم.</li>
  <li>تجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من يبحث عن {ar_name} للترطيب الفائق غير الدهني والانتعاش العطري.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كوفيكس (Cofix Care)</td></tr>
  <tr><th>الفئة</th><td>العناية بالجسم / لوشنات وغسولات كوفيكس غير الدهنية 400ml</td></tr>
  <tr><th>نوع المنتج</th><td>مستحضر ترطيب وتنظيف غير دهني للجسم بـ {key_ing_ar} (400ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>400 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الجسم (الجافة، العادية والدهنية)</td></tr>
  <tr><th>المظهر النهائي</th><td>جسم ناعم كالحرير، مرطب 24 ساعة، ناصع النظافة وغير دهني</td></tr>
  <tr><th>الملمس</th><td>لوشن/جل ناعم خفيف يمتص فورياً دون لزوجة</td></tr>
  <tr><th>العطر</th><td>عطر {key_ing_ar} المنعش الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصات {key_ing_ar}، جليسرين، مركبات ترطيب غير دهنية</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية (KSA)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Cofix Care Products</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد خلاصات {key_ing_ar} في مستحضرات كوفيكس (Cofix Body Care)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج مستحضر كوفيكس مشكلة جفاف بشرة الجسم، خشونة الجلد، والطبقة الدهنية المزعجة التي تتركها اللوشنات القاسية.</p>

<h3>لماذا تنجح تركيبة Cofix Non-Greasy Formula?</h3>
<p>لأن التركيبة خفيفة الامتصاص تعزل تبخر الماء الداخلي وتغذي الجلد دون غلق مسام البشرة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق فوراً بعد الاستحمام على بشرة رطبة:</strong> يضاعف امتصاص المرطبات.<br>
2. <strong>التركيز على المناطق الجافة (الكوعين والركبتين):</strong> يحمي من التصلب والخشونة.<br>
3. <strong>الاستخدام اليومي المنتظم:</strong> يمنح نضارة وثباتاً عطرياً دائمين.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "المرطبات الفعالة يجب أن تترك طبقة دهنية ثقيلة."<br>
<strong>الحقيقة:</strong> مستحضر كوفيكس يمتص فورياً ويمنح ترطيباً 24 ساعة دون أي دهنية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتسلل ميكروسيليلار المرطبات بين الخلايا الكيراتينية معززة تماسك الغشاء الهيدروليبيدي.</p>"""

    faqs_data = [
        (f"ما هو {ar_name}؟", f"هو مستحضر ترطيب وتنظيف للجسم غير دهني من كوفيكس بـ {key_ing_ar} بحجم 400 مل."),
        (f"ما هي فوائد خلاصة {key_ing_ar} والتركيبة غير الدهنية؟", "ترطب الجسم لـ 24 ساعة، تمنع الجفاف والخشونة، وتمتص فورياً دون لزوجة."),
        ("هل يمتص فورياً ويرطب لـ 24 ساعة دون دهنية؟", "نعم، مثبت سريرياً في الامتصاص السريع والترطيب 24 ساعة دون طبقة دهنية."),
        (f"ما حجم العبوة؟", "تأتي بعبوة ضخمة مزودة بضاغط سعة 400 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "ضعي كمية على بشرة مبللة أو جافة، دلكي برفق حتى الامتصاص الكامل يومياً."),
        ("هل هو آمن وخالٍ من البارابين؟", "نعم، 100% آمن ومختبر جلدياً ومناسب لجميع أنواع البشرة."),
        (f"أين صُنع مستحضر كوفيكس؟", "صُنع في المملكة العربية السعودية بواسطة Cofix Care Products."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات كوفيكس لدى إكليل أبها أصلية 100%."),
        (f"ما رائحة {ar_name}؟", f"عطر {key_ing_ar} المنعش الفاخر."),
        ("هل عبوة 400 مل بضاغط مريحة للاستخدام؟", "نعم، عبوة ضخمة بضاغط مريح جداً للاستخدام العائلي اليومي."),
        (f"هل العبوة 400 مل تكفي لفترة جيدة؟", "نعم، تكفي لعدة أشهر من الاستخدام المنتظم."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        (f"هل كوفيكس علامة موثوقة في العناية بالجسم؟", f"نعم، Cofix علامة سعودية رائدة وموثوقة جداً في العناية الشخصية."),
        ("كم مرة يومياً؟", "مرة إلى مرتين يومياً."),
        ("هل يمنح البشرة لمعاناً ونعومة حريرية؟", "نعم، يمنح البشرة توهجاً طبيعياً ونعومة حريرية."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يساعد في الوقاية من خشونة الجلد؟", "نعم، ينعم الجلد ويحمي من خشونة الكوعين والركبتين."),
        ("هل يترك ملمساً لزجاً؟", "ينفذ فورياً دون ترك لزوجة أو ثقل."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب الرجال والنساء؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يناسب الاستخدام في الصيف والشتاء؟", "نعم، ممتاز لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة؟", "نعم، منتج عناية مفيد وأنيق."),
        ("هل يعيد المظهر الصحي والمشرق للجسم؟", "نعم، يمنح الجسد مظهرًا ناعماً ومشرقاً."),
        ("هل يسهل ارتداء الملابس فوراً بعده؟", "نعم، يمتص سريعاً مما يتيح ارتداء الملابس فوراً دون بقع."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_name}</strong> is an authentic luxury non-greasy body moisturizing and cleansing product from Cofix designed to hydrate, nourish, and smooth body skin while eliminating dryness and roughness. Built upon {key_ing_en} extracts, hydrating Glycerin, and body skin nourishing compounds.</p>
<p>Cofix Body Product deeply nourishes body skin, locks in internal moisture for 24 hours without a greasy residue, and imparts a silky soft luster, leaving your body beautifully hydrated, flexible, and fragranced with fresh clean scent from first application.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>24-Hour Non-Greasy Intensive Hydration with {key_ing_en}:</strong> Imparts silky softness to body skin.</li>
  <li><strong>Instant Rapid Absorption with Zero Heavy Greasy Film:</strong> Ideal for daily use and immediate dressing.</li>
  <li><strong>Skin Protection Against Roughness & Dry Cracking:</strong> Reinforces the skin's natural moisture barrier.</li>
  <li><strong>Fresh Fragrant Long-Lasting Scent:</strong> Wraps the body in an elegant fresh aroma.</li>
  <li><strong>Dermatologically Tested Safe Formula:</strong> Free from parabens and harsh chemicals.</li>
  <li><strong>Generous 400ml Pump Value Bottle:</strong> Excellent size for daily continuous family use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Apply a suitable amount of Cofix product onto clean body skin post-shower.</li>
  <li><strong>Step 2:</strong> Massage gently in smooth circular motions until fully absorbed (use daily morning & night).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>{key_ing_en} Extracts & Glycerin:</strong> Preserve skin moisture balance delivering extreme touchable softness.</li>
  <li><strong>Non-Greasy Refreshing Compounds:</strong> Penetrate skin pores rapidly without causing stickiness or clogging.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical body skin application.</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_name} for non-greasy superior hydration and fragrant freshness.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Cofix</td></tr>
  <tr><th>Category</th><td>Body Care / Cofix Non-Greasy Body Lotions & Washes 400ml</td></tr>
  <tr><th>Product Type</th><td>Non-Greasy Body Moisturizing & Cleansing Product with {key_ing_en} (400ml)</td></tr>
  <tr><th>Volume/Weight</th><td>400 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Body Skin Types (Dry, Normal & Oily Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, spotlessly clean & non-greasy body skin</td></tr>
  <tr><th>Texture</th><td>Lightweight fast-absorbing smooth lotion/gel</td></tr>
  <tr><th>Fragrance</th><td>Luxurious fresh {key_ing_en} fragrance</td></tr>
  <tr><th>Active Ingredients</th><td>{key_ing_en} Extracts, Hydrating Glycerin, Non-Greasy Compounds</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia (KSA)</td></tr>
  <tr><th>Manufacturer</th><td>Cofix Care Products</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Non-Greasy Epidermal Absorption & Hydrolipid Barrier Sealing</h2>

<h3>What problem does this solve?</h3>
<p>{en_name} resolves skin dryness, rough elbow/knee skin, and greasy lotion residue on clothes.</p>

<h3>Why choose Cofix Non-Greasy Formula?</h3>
<p>The fast-absorbing formula seals in moisture and nourishes skin without clogging pores or leaving grease.</p>"""

    en_faqs_data = [
        (f"What is {en_name}?", f"It is a non-greasy body moisturizing or cleansing product from Cofix with {key_ing_en} (400ml)."),
        (f"What are the benefits of {key_ing_en} extract and non-greasy formula?", "Hydrates body skin for 24 hours, prevents roughness, and absorbs instantly without stickiness."),
        ("Does it absorb instantly and hydrate for 24 hours without greasiness?", "Yes, clinically proven to absorb rapidly and hydrate for 24 hours without greasy film."),
        (f"What volume is contained in this bottle?", "400ml pump bottle."),
        ("How do I use it correctly?", "Apply to clean skin post-shower, massage gently until absorbed daily."),
        ("Is it safe and paraben-free?", "Yes, 100% safe, dermatologically tested, and suitable for all skin types."),
        ("Where is Cofix Product manufactured?", "In Saudi Arabia by Cofix Care Products."),
        ("How do I verify authenticity at Ekleel Abha?", "All Cofix products at Ekleel Abha are 100% original."),
        (f"What scent does {en_name} have?", f"Luxurious fresh {key_ing_en} fragrance."),
        ("Is the 400ml pump dispenser convenient?", "Yes, generous pump bottle convenient for daily family use."),
        (f"Does the 400ml bottle last long?", "Yes, lasts months of regular daily use."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Cofix a trusted brand in Saudi Arabia?", "Yes, Cofix is a leading trusted brand in personal care in KSA."),
        ("How many times daily?", "Once or twice daily."),
        ("Does it impart shine and silky softness?", "Yes, gives body skin natural glow and silky softness."),
        ("Is the bottle recyclable?", "Yes."),
        ("Does it help prevent skin roughness?", "Yes, softens skin protecting elbows and knees from roughness."),
        ("Does it leave a sticky residue?", "Absorbs instantly without sticky residue or heavy feeling."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it good for all seasons?", "Yes, excellent for summer and winter care."),
        ("Is it a nice gift?", "Yes, practical and thoughtful body care gift."),
        ("Does it restore healthy radiant appearance?", "Yes, gives body skin a healthy smooth radiant look."),
        ("Can I get dressed immediately after application?", "Yes, fast absorption allows immediate dressing without staining clothes."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Cofix",
        "ar": {
            "title": ar_name,
            "meta_title": f"{ar_name} | إكليل أبها",
            "meta_description": f"اشتري {ar_name}. مستحضر ترطيب وتنظيف غير دهني للجسم بـ {key_ing_ar} من كوفيكس. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_name,
            "meta_title": f"{en_name} | Ekleel Abha",
            "meta_description": f"Buy original {en_name}. Cofix non-greasy body moisturizing and cleansing product with {key_ing_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2057():
    return _make_cofix_product_b68(
        pid=2057, gtin="792625756553",
        ar_name="لوشن الجسم بخلاصة البابونج غير دهني من كوفيكس 400مل",
        en_name="Cofix Non-Greasy Chamomile Body Lotion - 400ml",
        key_ing_ar="خلاصة أزهار البابونج المهدئة", key_ing_en="Soothing Chamomile Flower Extract",
        feature_ar="لوشن ترطيب غير دهني ومهدئ لبشرة الجسم بالبابونج 400 مل", feature_en="soothing non-greasy chamomile body lotion 400ml",
        tags_ar=["كوفيكس", "لوشن_البابونج_كوفيكس", "لوشن_غير_دهني", "ترطيب_الجسم_كوفيكس", "إكليل_أبها"],
        tags_en=["cofix", "chamomile_body_lotion", "non_greasy_lotion", "cofix_lotion", "ekleel_abha"]
    )


def create_product_2058():
    return _make_cofix_product_b68(
        pid=2058, gtin="792625756539",
        ar_name="لوشن الجسم بزهرة الجاردينيا  غير دهني من كوفيكس 400مل",
        en_name="Cofix Gardenia Flower Non-Greasy Body Lotion - 400ml",
        key_ing_ar="خلاصة أزهار الجاردينيا العطرية", key_ing_en="Aromatic Gardenia Flower Extract",
        feature_ar="لوشن ترطيب عطري غير دهني بزهرة الجاردينيا الفاخرة 400 مل", feature_en="luxurious gardenia flower non-greasy body lotion 400ml",
        tags_ar=["كوفيكس", "لوشن_الجاردينيا_كوفيكس", "معطر_جسم_غير_دهني", "لوشن_كوفيكس", "إكليل_أبها"],
        tags_en=["cofix", "gardenia_lotion", "cofix_gardenia", "fragranced_body_lotion", "ekleel_abha"]
    )


def create_product_2059():
    return _make_cofix_product_b68(
        pid=2059, gtin="792625756546",
        ar_name="لوشن الجسم بزبدة الشيا غير دهني  من كوفيكس 400مل",
        en_name="Cofix Non-Greasy Shea Butter Body Lotion - 400ml",
        key_ing_ar="زبدة الشيا الصافية المرممة", key_ing_en="Pure Restorative Shea Butter",
        feature_ar="لوشن ترطيب وترميم مكثف بزبدة الشيا سريع الامتصاص 400 مل", feature_en="intensive shea butter non-greasy body lotion 400ml",
        tags_ar=["كوفيكس", "لوشن_الشيا_كوفيكس", "زبدة_الشيا_غير_دهنية", "ترطيب_البشرة_الجافة", "إكليل_أبها"],
        tags_en=["cofix", "shea_butter_lotion", "cofix_shea_lotion", "non_greasy_shea", "ekleel_abha"]
    )


def create_product_2060():
    return _make_cofix_product_b68(
        pid=2060, gtin="792625756584",
        ar_name="غسول الجسم بالعنبر من كوفيكس 400مل",
        en_name="Cofix Amber Body Wash - 400ml",
        key_ing_ar="نفحات العنبر الفاخر والمكونات المنقية", key_ing_en="Luxurious Amber Fragrance & Cleansers",
        feature_ar="سائل استحمام عطري بنفحات العنبر الدافئة ونظافة حريرية 400 مل", feature_en="luxurious amber perfumed hydrating body wash 400ml",
        tags_ar=["كوفيكس", "غسول_العنبر_كوفيكس", "سائل_استحمام_العنبر", "غسول_جسم_معطر", "إكليل_أبها"],
        tags_en=["cofix", "amber_body_wash", "cofix_amber", "perfumed_body_wash", "ekleel_abha"]
    )


print("Loaded all 5 Batch 68 builders complete")
