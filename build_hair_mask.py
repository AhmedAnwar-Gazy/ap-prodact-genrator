import json, os

def build_hair_mask_product(prod_id, ingredient_en, ingredient_ar, gtin, img_slug):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعتبر <strong>كريم حمام الزيت بـ{ingredient_ar} بحجم 1000 مل (Hair Mask Cream - {ingredient_en} 1000ml)</strong> المستحضر المغذي الفاخر والاحترافي المخصص لإعادة الحيوية والنعومة الفائقة للشعر التالف والجاف. يعتمد هذا الحمام الكريمي على الخواص الطبيعية المذهلة لـ{ingredient_ar}، حيث يخترق عمق ألياف الشعر المجهدة ليمنحها ترطيباً مكثفاً وترميماً شاملاً غسلة بعد غسلة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترميم وتغذية عميقة بـ{ingredient_ar}:</strong> يعوض الشعر عن الرطوبة والبروتينات المفقودة ويرمم الأطراف التالفة.</li>
  <li><strong>نعومة وانسيابية كراستالية:</strong> يترك الشعر ناعماً كالحرير، سهلاً في التمشيط، وخالياً من التشابك والهيشان.</li>
  <li><strong>حماية ضد الجفاف والتكسر:</strong> يغلف ألياف الشعر بحجاب حماية ضد الإجهاد الحراري والتقلبات الجوية.</li>
  <li><strong>عبوة صالونات ضخمة 1000 مل:</strong> توفر حجماً وافراً واقتصادياً يضمن عناية مكثفة وممتدة لعدة أشهر.</li>
  <li><strong>تسهيل تصفيف الشعر:</strong> يلين الخصلات القاسية والمجعدة ويسهل التحكم بها بسلاسة.</li>
  <li><strong>مناسب لجميع أنواع الشعر:</strong> تركيبة غنية وآمنة تناسب الشعر المعالج كيميائياً والمصبوغ والجاف.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف):</strong> اغسلي شعركِ جيداً بالشامبو المناسب واشطفيه بالماء الفاتر ثم اعصريه خفيفاً.</li>
  <li><strong>الخطوة الثانية (التوزيع):</strong> وضعي كمية وافرة من كريم حمام الزيت بـ{ingredient_ar} من منتصف الشعر وحتى الأطراف.</li>
  <li><strong>الخطوة الثالثة (التدليك والتوزيع):</strong> دلكي الخصلات بلطف ومشطيها بأصابعكِ لضمان تغلغل الكريم في كافة الألياف.</li>
  <li><strong>الخطوة الرابعة (الانتظار):</strong> اتركي الكريم على الشعر لمدة 10 إلى 15 دقيقة (يمكن استخدام غطاء حراري أو فوطة دافئة).</li>
  <li><strong>الخطوة الخامسة (الشطف):</strong> اشطفي الشعر جيداً بالماء الفاتر حتى يزول أثر الكريم تماماً وتمتعي بالنعومة.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>مستخلص {ingredient_ar} الطبيعي:</strong> يزود ألياف الشعر بالمرطبات الطبيعية والفيتامينات المغذية.</li>
  <li><strong>سيتريل ألكوهول (Cetearyl Alcohol):</strong> مرطب دهني نباتي يطري الخصلات ويمنع جفافها.</li>
  <li><strong>سيتريمونيوم كلورايد (Cetrimonium Chloride):</strong> عامل تكييف يزيل الشحنات الساكنة ويمنع تشابك الشعر.</li>
  <li><strong>الدايميثيكون (Dimethicone):</strong> يغلف الطبقة الخارجية للشعرة ويمنحها بريقاً كريستالياً ونعومة فادحة.</li>
  <li><strong>البانثينول (Pro-Vitamin B5):</strong> يمتص الرطوبة ويحبسها داخل قشرة الشعرة لزيادة مرونتها.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الشعر فقط.</li>
  <li>تجنبي ملامسة المنتج المباشرة للعينين؛ وفي حال ملامستهما اشطفي فوراً بالماء.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
  <li>في حال ظهور حكة أو تهيج بالفروة توقفي عن الاستخدام.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من الشعر الجاف، المجهد، التالف، أو المتقصف وترغب في حمام زيت مغذٍ بحجم كبير.</li>
  <li>صاحبات الشعر المصبوغ أو المعالج بالحرارة الراغبات في ترطيب واستعادة ليونة الشعر.</li>
  <li>مناسب لجميع أنواع الشعر والعناية الاحترافية المنزلية.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>عام / كريم حمام الزيت</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / أقنعة وحمام الزيت للشعر</td></tr>
  <tr><th>نوع المنتج</th><td>كريم حمام زيت مرطب ومغذٍ بـ{ingredient_ar}</td></tr>
  <tr><th>الحجم/الوزن</th><td>1000 مل (1 لتر)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (خاصة الجاف والمجهد والتالف)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم، حريري، متماسك ومفعم بالحيوية واللمعان</td></tr>
  <tr><th>الملمس</th><td>كريمي كثيف يرغي ويغلف الخصلات بسهولة</td></tr>
  <tr><th>العطر</th><td>عطر {ingredient_ar} الغني والمنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>مستخلص {ingredient_ar}، سيتريل ألكوهول، سيتريمونيوم كلورايد، بانثينول</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / الإمارات</td></tr>
  <tr><th>الشركة المصنعة</th><td>Professional Hair Care Labs</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد حمام الزيت بـ{ingredient_ar} وترميم ألياف الشعر</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم حمام الزيت بـ{ingredient_ar} مشكلة جفاف الشعر الشديد والتقصف وخشونة الملمس الناتجة عن الصبغات، الفرد الكيميائي، واستخدام حرارة السيشوار والمكواة بدون حماية.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تتلف حراشف الشعر وتفتح عند التعرض للكيماويات والحرارة، مما يسبب تسرب البروتينات والماء الداخلي، فتظهر أطراف الشعر متكسرة وخشونة وتفقد مرونتها.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>الاستخدام المنتظم:</strong> استعملي حمام الزيت مرة إلى مرتين أسبوعياً.<br>
2. <strong>استخدام البخار الحراري:</strong> غطي الشعر بفوطة دافئة لمدة 15 دقيقة لزيادة امتصاص الكريم.<br>
3. <strong>الشطف بالماء الفاتر:</strong> اشطفي بالماء الفاتر لإبقاء طبقة ترطيب خفيفة.<br>
4. <strong>تجنب وضع الكريم على الفروة مباشرة:</strong> ركزي على الأطراف والخصلات التالفة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "حمام الزيت يسبب تساقط الشعر."<br>
<strong>الحقيقة:</strong> حمام الزيت يغذي ألياف الشعر ويقويها، ولكن يجب تجنب حك الفروة بشدة به والغسل الجيد بالماء.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يتغلغل مستخلص {ingredient_ar} والبانثينول داخل الطبقة القشرية لترميم الروابط البيبتيدية، بينما تقوم مستحلبات السيتريل ألكوهول بتغليف السطح الخارجي بحجاب دهني يمنع تبخر الماء ويمنح ملمساً ناعماً متماسكاً.</p>"""

    faqs = [
        (f"ما هو كريم حمام الزيت بـ{ingredient_ar} 1000 مل؟", f"هو كريم مرطب ومغذٍ مكثف للشعر غني بـ{ingredient_ar} مصمم لترميم الشعر التالف والجاف ومنحه نعومة وانسيابية."),
        (f"ما هي فوائد {ingredient_ar} للشعر؟", f"يزود ألياف الشعر بالمرطبات الطبيعية، يقلل التقصف، ويعيد الليونة واللمعان للخصم المتضررة."),
        ("ما حجم عبوة حمام الزيت؟", "تأتي العبوة بحجم صالونات وافر يبلغ 1000 مل (1 لتر)، وهي كمية اقتصادية تكفي لأشهر من الاستخدام."),
        ("كم من الوقت يُترك الكريم على الشعر؟", "يُترك من 10 إلى 15 دقيقة على الشعر المبلل للحصول على أقصى درجات الترطيب."),
        ("هل يفضل استخدام حرارة أو فوطة دافئة؟", "نعم، غطاء الرأس الحراري أو الفوطة الدافئة تفتح حراشف الشعر وتضاعف امتصاص الفوائد."),
        ("هل يناسب الشعر المسبوغ والمعالج؟", "نعم، تركيبة مغذية وممتازة للشعر المسبوغ والمفرود بروتين أو كيراتين."),
        ("هل يترك الشامبو ملمساً زيتيّاً ثقيلاً؟", "لا، يشطف بسهولة بالماء ويترك الشعر ناعماً دون ثقل زيتي مفرط."),
        ("هل يناسب جميع أنواع الشعر؟", "نعم، يناسب جميع أنواع الشعر وخاصة الجاف، المجهد، والمتقصف."),
        ("كم مرة يُنصح باستخدامه أسبوعياً؟", "يُنصح باستخدامه من مرة إلى مرتين أسبوعياً لحماية ممتدة."),
        (f"ما هي رائحة كريم حمام الزيت بـ{ingredient_ar}؟", f"يتميز برائحة {ingredient_ar} الطبيعية الغنية والمنعشة."),
        ("هل يساعد في فك تشابك الشعر القاسي؟", "نعم، يلين الخصلات فورياً ويسهل مرور المشط دون تقصف."),
        ("ما هو بلد صنع المنتج؟", "تم تصنيعه وفق أعلى معايير العناية بالشعر الاحترافية."),
        ("هل يمنع تقصف أطراف الشعر؟", "نعم، تغليف ألياف الشعر بالمرطبات يحد بشكل ملحوظ من تكسر الأطراف."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع المستحضرات لدى صيدلية إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين."),
        ("هل يوضع الكريم على فروة الرأس؟", "يُفضل تركيز وضعه من منتصف الشعر وحتى الأطراف وتجنب الفروة المباشرة."),
        ("هل يناسب الرجال والنساء؟", "نعم، هو مناسب جداً لكلا الجنسين ولجميع الأعمار."),
        ("هل يمكن استخدامه للأطفال؟", "مناسب للأطفال من سن 12 سنة فما فوق."),
        ("هل يترك أي بقايا بعد الشطف الجيد؟", "لا، يشطف بسهولة بالماء الفاتر لترك شعر أملس ومشرق."),
        ("كيف أحتفظ بالعبوة بالشكل الصحيح؟", "تُحفظ العبوة سعة 1000 مل في مكان بارد وجاف بعيداً عن حرارة الشباك."),
        ("هل يساعد في إضافة لمعان للشعر الباهت؟", "نعم، تغليف الشعرة بالمرطبات يعيد إليها البريق واللمعان الكريستالي."),
        ("هل يناسب الشعر المجعد (الكيرلي)؟", "نعم، يمنح التماوج الكيرلي رطوبة ونعومة ومظهراً ممتلئاً بدون هيشان."),
        ("هل يحتاج لغسل بالشامبو بعده؟", "لا، يُغسل الشعر بالشامبو أولاً، ثم يوضع حمام الزيت ويشطف بالماء فقط."),
        ("هل العبوة بحجم 1000 مل اقتصادية للعائلة؟", "نعم، حجم 1 لتر ممتاز واقتصادي جداً للاستخدام العائلي المستمر."),
        ("هل يساعد في حماية الشعر من الحرارة؟", "نعم، الترطيب العميق يقلل التأثر بحرارة أدوات التصفيف."),
        ("هل العبوة قابلة للإغلاق بإحكام؟", "نعم، العبوة متينة وتأتي بغطاء محكم يمنع التسرب.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>Hair Mask Cream - {ingredient_en} (1000ml)</strong> is a professional salon-grade nourishing treatment engineered to revitalize dry, damaged, and over-processed hair. Harnessing the deep conditioning properties of natural {ingredient_en}, this intensive cream mask penetrates deep into damaged hair cuticles to deliver rich moisture, elasticity, and softness wash after wash.</p>
<p>Formulated for whole-family and salon usage, this 1000ml (1 Litre) tub provides an economical reservoir of deep hydration. It smooths rough cuticle scales, tames persistent frizz, and facilitates easy combability without weighing down your hair style.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Deep Restorative {ingredient_en} Care:</strong> Replenishes lost moisture and proteins to repair split ends and brittle fibers.</li>
  <li><strong>Silky Smoothness & Crystal Shine:</strong> Leaves hair touchably soft, glossy, and completely detangled.</li>
  <li><strong>Thermal & Dryness Shield:</strong> Coats hair shafts with a protective barrier against heat styling and weather stress.</li>
  <li><strong>Generous 1000ml Salon Tub:</strong> Offers exceptional value providing extended deep treatment for months.</li>
  <li><strong>Effortless Styling Control:</strong> Softens coarse, frizzy strands for smooth manageable styling.</li>
  <li><strong>Safe for All Hair Types:</strong> Gentle, rich composition suitable for color-treated, chemically relaxed, and dry hair.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse):</strong> Shampoo hair thoroughly with a mild cleanser, rinse with warm water, and gently squeeze out excess water.</li>
  <li><strong>Step 2 (Apply):</strong> Apply a generous amount of {ingredient_en} Hair Mask Cream from mid-lengths to ends.</li>
  <li><strong>Step 3 (Distribute):</strong> Massage strands softly and comb through with fingers to ensure uniform coverage.</li>
  <li><strong>Step 4 (Process):</strong> Leave on for 10 to 15 minutes (use a warm towel or steamer for enhanced penetration).</li>
  <li><strong>Step 5 (Rinse):</strong> Rinse thoroughly with lukewarm water until completely cleared.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Natural {ingredient_en} Extract:</strong> Supplies vital fatty acids, vitamins, and humectants to nourish dry hair layers.</li>
  <li><strong>Cetearyl Alcohol:</strong> Botanical emollient that softens rough cuticles and traps internal moisture.</li>
  <li><strong>Cetrimonium Chloride:</strong> Conditioning agent that eliminates static charges and prevents friction tangles.</li>
  <li><strong>Dimethicone:</strong> Forms a light-reflecting sheath over hair cuticles, boosting gloss and softness.</li>
  <li><strong>Panthenol (Pro-Vitamin B5):</strong> Draws water into the hair cortex to restore natural elasticity.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on hair only.</li>
  <li>Avoid direct contact with eyes; rinse immediately with water if contact occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
  <li>Discontinue use if scalp irritation develops.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dry, brittle, damaged, or split-end-prone hair seeking a large-volume deep conditioning mask.</li>
  <li>Individuals with color-treated or heat-styled hair wanting salon-grade hydration at home.</li>
  <li>Suitable for all hair types and regular family haircare routines.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Generic / Hair Care Professional</td></tr>
  <tr><th>Category</th><td>Hair Care / Hair Masks & Treatments</td></tr>
  <tr><th>Product Type</th><td>Nourishing {ingredient_en} Hair Mask Cream</td></tr>
  <tr><th>Volume/Weight</th><td>1000 ml (1 Litre)</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Ideal for Dry & Damaged Hair)</td></tr>
  <tr><th>Finish</th><td>Soft, silky, shiny, fissure-free & manageable hair</td></tr>
  <tr><th>Texture</th><td>Rich thick cream spreading easily</td></tr>
  <tr><th>Fragrance</th><td>Fresh natural {ingredient_en} aroma</td></tr>
  <tr><th>Active Ingredients</th><td>{ingredient_en} Extract, Cetearyl Alcohol, Cetrimonium Chloride, Panthenol</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / UAE</td></tr>
  <tr><th>Manufacturer</th><td>Professional Hair Care Labs</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of {ingredient_en} Extraction & Cortical Hair Repair</h2>

<h3>What problem does this solve?</h3>
<p>The {ingredient_en} Hair Mask Cream resolves hair brittleness, cuticle roughness, and split ends caused by thermal styling, chemical dyeing, and severe moisture depletion.</p>

<h3>Why does this condition happen?</h3>
<p>Chemical processing and heat styling strip essential lipids and proteins from the protective cuticle sheath, leaving exposed inner cortex layers prone to dehydration and mechanical breakage.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Weekly Mask Treatment:</strong> Apply deep mask treatments 1 to 2 times weekly.<br>
2. <strong>Thermal Steaming:</strong> Wrap hair in a warm damp towel for 15 minutes to maximize absorption.<br>
3. <strong>Lukewarm Rinse:</strong> Rinse with lukewarm water to lock in active conditioning lipids.<br>
4. <strong>Focus on Ends:</strong> Apply primarily onto mid-lengths and ends rather than directly on scalp skin.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Hair masks cause excessive hair fall."<br>
<strong>Fact:</strong> Deep conditioning masks fortify hair shafts and reduce breakage; ensuring complete water rinsing prevents scalp buildup.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Natural {ingredient_en} lipids and Panthenol penetrate cortical micro-fissures to rebuild broken hydrogen bonds, while Cetearyl Alcohol and Dimethicone align outer cuticle scales into a smooth, light-reflecting hydrophobic shield that seals in moisture.</p>"""

    en_faqs = [
        (f"What is {ingredient_en} Hair Mask Cream 1000ml?", f"It is a professional deep-conditioning hair treatment enriched with {ingredient_en} designed to repair damaged, dry hair and restore silky softness."),
        (f"What are the benefits of {ingredient_en} for hair?", f"It infuses essential moisture, reduces split ends, and restores natural elasticity and gloss to damaged strands."),
        ("What volume is contained in this tub?", "It comes in a 1000ml (1 Litre) salon-size tub offering economical extended usage."),
        ("How long should I leave the mask on?", "Leave on clean damp hair for 10 to 15 minutes before rinsing thoroughly."),
        ("Is applying heat recommended?", "Yes, wrapping hair in a warm towel or using a steamer opens cuticles for deeper nutrient absorption."),
        ("Is it safe for color-treated hair?", "Yes, its rich nourishing formula is safe for color-treated and chemically relaxed hair."),
        ("Does it leave a heavy greasy residue?", "No, it rinses out completely with warm water, leaving hair soft without heavy grease."),
        ("Is it suitable for all hair types?", "Yes, ideal for dry, brittle, coarse, or over-processed hair textures."),
        ("How often should I use this mask?", "Use 1 to 2 times weekly for ongoing hair restoration."),
        (f"What scent does the mask have?", f"It features a rich, pleasant natural {ingredient_en} fragrance."),
        ("Does it help detangle knotty hair?", "Yes, conditioning agents ease friction for snag-free combing."),
        ("Where is this product manufactured?", "It is manufactured in certified professional cosmetic hair care laboratories."),
        ("Does it help prevent split ends?", "Yes, coating strands with conditioning lipids significantly reduces split end formation."),
        ("How do I verify authenticity at Ekleel Abha?", "All hair treatments at Ekleel Abha are 100% genuine from certified distributors."),
        ("Should I apply it to my scalp?", "Focus application on mid-lengths and ends to avoid heavy scalp oils."),
        ("Can both men and women use it?", "Yes, it is a unisex deep conditioning treatment."),
        ("Is it suitable for teenagers?", "Yes, safe for adults and teens aged 12+."),
        ("Does it rinse out easily?", "Yes, it rinses out cleanly with warm water."),
        ("How should I store the 1000ml tub?", "Store in a cool, dry place away from direct heat."),
        ("Does it add shine to dull hair?", "Yes, smoothing cuticles restores brilliant light reflection."),
        ("Is it suitable for curly hair?", "Yes, it provides intense moisture to enhance curl definition without frizz."),
        ("Do I need to shampoo after using the mask?", "No, shampoo first, apply the mask, then rinse with water only."),
        ("Is the 1000ml tub economical for families?", "Yes, the 1 Litre tub provides exceptional long-term value for family use."),
        ("Does it protect hair against styling heat?", "Yes, deep conditioning reduces thermal stress damage."),
        ("Does the tub seal securely?", "Yes, it features a strong screw lid preventing leakage.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "العناية بالشعر / أقنعة وحمام الزيت للشعر",
        "brand": "Generic",
        "ar": {
            "title": f"كريم حمام الزيت بـ{ingredient_ar} 1000مل",
            "meta_title": f"كريم حمام الزيت {ingredient_ar} 1000مل | صيدلية إكليل أبها",
            "meta_description": f"اشتري كريم حمام الزيت المغذي والمقوي للشعر بـ{ingredient_ar} (1000مل / 1 لتر). ترطيب مكثف وترميم للشعر التالف. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["حمام_زيت", f"حمام_زيت_{ingredient_ar}", "ترميم_الشعر", "عناية_بالشعر", "إكليل_أبها"]
        },
        "en": {
            "title": f"{ingredient_en} Hair Mask Cream - 1000ml",
            "meta_title": f"{ingredient_en} Hair Mask Cream 1000ml | Ekleel Abha Pharmacy",
            "meta_description": f"Buy {ingredient_en} Hair Mask Cream (1000ml / 1 Litre). Deep conditioning treatment for dry, damaged hair. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["hair_mask", f"{ingredient_en.lower()}_hair_mask", "deep_conditioning", "hair_care", "ekleel_abha"]
        },
        "schema": {
            "brand": "Generic",
            "category": "Hair Care / Hair Mask",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"{img_slug}-hair-mask-cream-1000ml.webp",
            "alt": f"{ingredient_en} Hair Mask Cream 1000ml",
            "title": f"{ingredient_en} Hair Mask Cream 1000ml"
        }
    }

print("Hair Mask module ready")
