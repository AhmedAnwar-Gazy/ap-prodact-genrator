import json, os

def build_garnier_hair_food(prod_id, title_ar, title_en, active_ar, active_en, benefit_ar, benefit_en, gtin, img_slug):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعد <strong>{title_ar}</strong> القناع النباتي المتكامل الابتكاري والأكثر مبيعاً عالمياً لتغذية وترميم الشعر بمكونات طبيعية بنسبة 98%. يرتكز هذا المستحضر الفريد من غارنييه الترا دوكس (Garnier Ultra Doux Hair Food 3-in-1) على قوة {active_ar} المغذية والزيوت النباتية النقية دون سيليكونات أو بارابين أو ألوان صناعية.</p>
<p>يمتاز ماسك غارنييه بقوام غني متعدد الاستخدامات 3 في 1: يمكن استخدامه كـ حمام زيت مرطب، بلسم لتسهيل التمشيط، أو كريم يترك على الشعر (Leave-In)، حيث ينفذ في ألياف الشعر ليمنحه {benefit_ar}، ليترك شعركِ ناعماً، خفيفاً، ومفعماً بالصحة واللمعان.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>مكونات طبيعية بنسبة 98%:</strong> تركيبة نباتية ناصعة تغذي الشعر دون تثقيل البصيلات.</li>
  <li><strong>استخدام متعدد 3 في 1:</strong> يُستعمل كبلسم، ماسك مغذٍ، أو كريم مرطب يترك على الشعر (Leave-In).</li>
  <li><strong>غني بـ {active_ar}:</strong> يمنح ألياف الشعر {benefit_ar} ويحميه من التقصف.</li>
  <li><strong>خالي 100% من السيليكون والبارابين والألوان:</strong> يترك الشعر بحركية طبيعية خفيفة دون لزوجة زيتيّة ثقيلة.</li>
  <li><strong>ترطيب عميق للشعر التالف والجاف:</strong> يرمم أطراف الشعر المجهدة ويعيد إليها المرونة والبريق.</li>
  <li><strong>عبوة ضخمة سعة 390 مل:</strong> حجم وافر جداً تكفي لعدة أشهر من العناية المنزلية المكثفة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الاستخدام الأول (كبلسم):</strong> وضعي كمية على الشعر المبلل بعد الشامبو لفك التشابك ثم اشطفي.</li>
  <li><strong>الاستخدام الثاني (كماسك حمام زيت):</strong> وضعي كمية وافرة على الشعر المبلل، اتركيها لـ 3 دقائق ثم اشطفي جيداً.</li>
  <li><strong>الاستخدام الثالث (ككريم Leave-In):</strong> وضعي كمية صغيرة على الشعر الرطب أو الجاف من المنتصف حتى الأطراف دون شطف.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة {active_ar} والزيوت المغذية:</strong> تغذي ألياف الشعر وترمم التقصف.</li>
  <li><strong>تركيبة نباتية 98% خالية من السيليكون:</strong> تحفظ رطوبة الشعر بطبيعية ناعمة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الشعر فقط؛ يمنع البلع أو الأكل برغم الرائحة الشهية!</li>
  <li>تجنبي ملامسة الماسك المباشرة للعينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل من تعاني من الشعر التالف، الجاف، المتقصف وتفتش عن غذاء الشعر 3 في 1 بـ {active_ar} من غارنييه الترا دوكس.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>غارنييه الترا دوكس (Garnier Ultra Doux)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / ماسكات وغذاء الشعر 3 في 1 النباتية</td></tr>
  <tr><th>نوع المنتج</th><td>ماسك وغذاء الشعر 3 في 1 بـ {active_ar} (390ml)</td></tr>
  <tr><th>الحجم/الوزن</th><td>390 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>الشعر الجاف، التالف، والمتقصف</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم، مرطب، خفيف، ومفعم بالحيوية واللمعان الطبيعي</td></tr>
  <tr><th>الملمس</th><td>قوام كريمي غني نباتي يذوب بالشعر</td></tr>
  <tr><th>العطر</th><td>عطر {active_ar} الاستوائي الشهي واللذيذ</td></tr>
  <tr><th>المكونات النشطة</th><td>خلاصة {active_ar}، زيوت نباتية 98%، خالي من السيليكون</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا (Garnier France)</td></tr>
  <tr><th>الشركة المصنعة</th><td>L'Oréal / Garnier</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 3 سنوات)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد غذاء الشعر 3 في 1 من غارنييه (Garnier Hair Food)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج ماسك غارنييه هير فود مشكلة تلف وتقصف ألياف الشعر، الجفاف الشديد، وثقل السيليكون بالماسك التقليدي.</p>

<h3>لماذا تنجح تركيبة الـ 98% المكونات الطبيعية؟</h3>
<p>لأن خلاصة {active_ar} والزيوت تخترق جذع الشعرة لترميم أغشية البروتين، بينما تمنع التركيبة الخالية من السيليكون التثقيل.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التنويع بين الطرق الـ 3:</strong> استعمليه كبلسم يومي أو ماسك أسبوعي أو كريم يترك على الشعر.<br>
2. <strong>التركيز على الأطراف المتقصفة:</strong> دلكي أطراف الشعر المجهدة بـ Leave-In قبل التصفيف.<br>
3. <strong>التسريح بفرشاة واسعة:</strong> سرحي الشعر بالفرشاة أثناء وجود الماسك للتوزيع المثالي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الماسكات الطبيعية الخالية من السيليكون لا تنعم الشعر بفاعلية."<br>
<strong>الحقيقة:</strong> ماسك غارنييه 98% ينعم الشعر ويمنحه ملمساً حريرياً بطبيعية ناصعة دون رواسب سيليكونية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تتحد الأحماض الدهنية في {active_ar} مع كيراتين الشعر، مما يعوض نقص الليبيدات ويمنع تكسر الشعرة أثناء التمشيط.</p>"""

    faqs = [
        (f"ما هو {title_ar}؟", f"هو ماسك وغذاء للشعر 3 في 1 نباتي بنسبة 98% مكونات طبيعية بـ {active_ar} لترميم وتنعيم الشعر سعة 390 مل."),
        (f"ما هي فوائد الاستخدام الـ 3 في 1؟", "يمكن استخدامه كبلسم لفك التشابك، حمام زيت ماسك مكثف، أو كريم مرطب يترك على الشعر (Leave-In)."),
        ("هل هو خالي 100% من السيليكون والبارابين؟", "نعم، تركيبة نباتية ناصعة 98% خالية تماماً من السيليكون والبارابين والألوان الصناعية."),
        ("ما حجم العبوة؟", "تأتي بحجم وافر سعة 390 مل."),
        ("كيف يُستخدم بالشكل الصحيح؟", "يُستخدم كبلسم يشطف فوراً، كحمام زيت يترك لـ 3 دقائق ويشطف، أو ككريم يترك على الشعر الرطب دون شطف."),
        ("هل يثقل الشعر أو يتركه دهنياً؟", "لا، ينفذ في ألياف الشعر فورياً ويمنحه حركة ونعومة خفيفة دون لزوجة."),
        ("ما هو بلد صنع غارنييه الترا دوكس؟", "صُنع بفخر في فرنسا بواسطة شركة لوريال (L'Oréal / Garnier)."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات غارنييه لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        (f"ما هي رائحة الماسك؟", f"يتميز برائحة {active_ar} الشهية واللذيذة التي تدوم بالنسيم."),
        ("هل يناسب الشعر المصبوغ والمعالج؟", "نعم، خلوه من السيليكون والبارابين يجعله آمناً تماماً للشعر المصبوغ والمعالج."),
        ("هل يساعد في ترميم الأطراف المتقصفة؟", "نعم، يرمم تقصف الأطراف ويمنع تكسر الشعر عند التمشيط."),
        ("هل يناسب جميع أنواع الشعر الجاف؟", "مناسب للشعر الجاف، التالف، والمجهد حرارياً."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف بعبوتها المغلقة محكماً."),
        ("هل العبوة 390 مل اقتصادية؟", "نعم، عبوة ضخمة تكفي لعدة أشهر من العناية المنزلية الفاخرة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم، عبوة صديقة للبيئة وقابلة لإعادة التدوير 100%."),
        ("هل يناسب الأطفال؟", "آمن للأطفال والبالغين من سن 3 سنوات فما فوق."),
        ("هل يسهل تسريح الشعر الكيرلي؟", "ممتاز جداً لترطيب وتصفيف الشعر الكيرلي والمتموج."),
        ("كم مرة يُفضل استخدامه أسبوعياً؟", "يمكن استخدامه يومياً كبلسم أو 2 إلى 3 مرات أسبوعياً كـ ماسك."),
        ("هل يغني عن كريمات التصفيف العادية؟", "نعم، طريقة الـ Leave-In تغني عن كريمات التصفيف الزيتية الثقيلة."),
        ("هل يترك ملمساً ناعماً حريرياً؟", "نعم، يترك الشعر ناعماً، مشرقاً ومفعماً بالحيوية."),
        ("هل ينصح به خبراء التصفيف؟", "نعم، ماسك هير فود الأكثر مبيعاً وتقييماً عالمياً."),
        ("هل يحتوي على زيوت جوز الهند أو دوار الشمس؟", "نعم، مدعم بزيوت نباتية مغذية كجوز الهند ودوار الشمس."),
        ("هل يمنع تطاير وهيشان الشعر؟", "نعم، يضبط هيشان وتطاير الشعر ويمنحه ثباتاً ناعماً."),
        ("هل هو الماسك الأفخر لغارنييه؟", "نعم، السلسلة النباتية الفاخرة رقم 1 من غارنييه الترا دوكس."),
        ("هل يتوفر بنكهات أخرى لدى إكليل أبها؟", "نعم، تتوفر نكهات البابايا، الموز، وجوز الهند والمكاديميا لدى إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{title_en}</strong> is the globally #1 best-selling 98% natural origin 3-in-1 hair mask treatment formulated to repair and nourish dry, damaged hair. Engineered by Garnier Ultra Doux (Hair Food 3-in-1), it blends the power of {active_en} with pure botanical oils, completely free from silicones, parabens, and artificial colorants.</p>
<p>Featuring a versatile 3-in-1 rich texture, Garnier Hair Food functions as a rinse-out conditioner, a deep conditioning hair mask, or a leave-in treatment, penetrating hair fibers to provide {benefit_en} without leaving hair heavy or greasy.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>98% Natural Origin Ingredients:</strong> Vegan natural formula nourishing hair without silicone buildup.</li>
  <li><strong>Versatile 3-in-1 Application:</strong> Use as a conditioner, deep treatment mask, or leave-in conditioning cream.</li>
  <li><strong>Enriched with {active_en}:</strong> Provides hair fibers with {benefit_en} and repairs split ends.</li>
  <li><strong>100% Silicone, Paraben & Colorant Free:</strong> Leaves hair with natural bounce and zero oily heaviness.</li>
  <li><strong>Intense Repair for Damaged Hair:</strong> Smooths rough cuticles, restoring shine and suppleness.</li>
  <li><strong>Generous 390ml Tub:</strong> High-value tub providing months of deep home hair care.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (As a Conditioner):</strong> Apply to wet hair after shampooing to detangle, then rinse.</li>
  <li><strong>Step 2 (As a Hair Mask):</strong> Apply generously to wet hair, leave for 3 minutes, then rinse thoroughly.</li>
  <li><strong>Step 3 (As a Leave-In):</strong> Apply a small amount to damp or dry hair lengths without rinsing.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>{active_en} Extract & Plant Oils:</strong> Deeply nourish hair fibers and seal split ends.</li>
  <li><strong>98% Vegan Silicone-Free Base:</strong> Locks in hair moisture naturally.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external hair application only; do not eat despite the irresistible fragrance!</li>
  <li>Avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone with dry, damaged, or frizzy hair seeking the original Garnier 98% natural 3-in-1 {active_en} hair food mask.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Garnier Ultra Doux</td></tr>
  <tr><th>Category</th><td>Hair Care / 3-in-1 Vegan Hair Food Masks</td></tr>
  <tr><th>Product Type</th><td>98% Natural 3-in-1 {active_en} Hair Mask (390ml)</td></tr>
  <tr><th>Volume/Weight</th><td>390 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Dry, Damaged & Frizzy Hair</td></tr>
  <tr><th>Finish</th><td>Soft, smooth, hydrated, bouncy & shiny hair</td></tr>
  <tr><th>Texture</th><td>Rich melting vegan cream matrix</td></tr>
  <tr><th>Fragrance</th><td>Delicious tropical {active_en} scent</td></tr>
  <tr><th>Active Ingredients</th><td>{active_en} Extract, Coconut Oil, Sunflower Seed Oil</td></tr>
  <tr><th>Country of Origin</th><td>France (Garnier France)</td></tr>
  <tr><th>Manufacturer</th><td>L'Oréal / Garnier</td></tr>
  <tr><th>Age Group</th><td>All Ages (3+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of 98% Natural Origin & Silicone-Free Hair Nutrition</h2>

<h3>What problem does this solve?</h3>
<p>Garnier Hair Food 3-in-1 resolves hair fiber damage, split ends, severe dryness, and heavy silicone buildup.</p>

<h3>Why choose Garnier Hair Food?</h3>
<p>{active_en} lipids penetrate the hair cuticle to restructure damaged keratin without leaving silicone residues.</p>"""

    en_faqs = [
        (f"What is {title_en}?", f"It is a 98% natural origin 3-in-1 vegan hair mask treatment enriched with {active_en} to repair and nourish dry hair."),
        ("What are the benefits of 3-in-1 application?", "Functions as a detangling conditioner, 3-minute hair mask, or leave-in conditioning cream."),
        ("Is it 100% silicone, paraben, and colorant free?", "Yes, 98% vegan natural formula free of silicones, parabens, and artificial dyes."),
        ("What volume is contained in this tub?", "It comes in a generous 390ml tub."),
        ("How do I apply it correctly?", "Rinse out immediately as a conditioner, leave on 3 minutes as a mask, or apply to damp hair lengths as a leave-in."),
        ("Does it weigh down hair or leave it greasy?", "No, absorbs quickly into hair fibers leaving natural bounce without oily weight."),
        ("Where is Garnier Ultra Doux manufactured?", "It is proudly manufactured in France by L'Oréal / Garnier."),
        ("How do I verify authenticity at Ekleel Abha?", "All Garnier products at Ekleel Abha are 100% original from certified distributors."),
        (f"What scent does this hair food have?", f"Features a delicious, long-lasting tropical {active_en} fragrance."),
        ("Is it safe for color-treated hair?", "Yes, silicone-free and paraben-free formula is completely safe for color-treated hair."),
        ("Does it repair split ends?", "Yes, smooths hair cuticles and repairs dry split ends."),
        ("Is it suitable for dry and damaged hair?", "Ideal for dry, damaged, frizzy, and heat-styled hair."),
        ("How should I store the tub?", "Store in a cool, dry place with lid tightly closed."),
        ("Is the 390ml tub economical?", "Yes, generous volume provides months of deep home hair care."),
        ("Is the tub recyclable?", "Yes, 100% recyclable environmentally friendly tub packaging."),
        ("Is it safe for family use?", "Yes, safe for adults and children aged 3+."),
        ("Does it help style curly hair?", "Yes, excellent for moisturizing and defining curly and wavy hair."),
        ("How often can I use it weekly?", "Use daily as a conditioner or 2 to 3 times weekly as an intensive mask."),
        ("Does it replace traditional leave-in creams?", "Yes, the leave-in method replaces heavy styling creams."),
        ("Does it leave hair silky smooth?", "Yes, leaves hair touchably soft, shiny, and supple."),
        ("Is it hairdresser recommended?", "Yes, globally celebrated #1 hair food mask range."),
        ("Does it contain Coconut or Sunflower oil?", "Yes, enriched with nourishing Coconut and Sunflower seed oils."),
        ("Does it stop hair frizz?", "Yes, tames frizzy hair and controls flyaways."),
        ("Is it Garnier's premier hair mask line?", "Yes, the flagship 98% natural vegan line by Garnier Ultra Doux."),
        ("Are other variants available at Ekleel Abha?", "Yes, Ekleel Abha offers Papaya, Banana, and Coconut & Macadamia variants.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "العناية بالشعر / ماسكات وغذاء الشعر 3 في 1 النباتية",
        "brand": "Garnier",
        "ar": {
            "title": title_ar,
            "meta_title": f"ماسك غارنييه غذاء الشعر 390مل | صيدلية إكليل أبها",
            "meta_description": f"اشتري {title_ar}. ماسك وغذاء الشعر 3 في 1 بنسبة 98% مكونات طبيعية بـ {active_ar}. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["غارنييه", "الترا_دوكس", "غذاء_الشعر", "ماسك_الشعر_3في1", "إكليل_أبها"]
        },
        "en": {
            "title": title_en,
            "meta_title": f"Garnier Ultra Doux Hair Food 390ml | Ekleel Abha",
            "meta_description": f"Buy original {title_en}. 98% natural origin 3-in-1 hair mask with {active_en}. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["garnier", "ultra_doux", "hair_food", "3in1_mask", "ekleel_abha"]
        },
        "schema": {
            "brand": "Garnier",
            "category": "Hair Care / Hair Mask",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"{img_slug}.webp",
            "alt": title_en,
            "title": title_en
        }
    }

def create_product_1825():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>مناديل ميسيلار جونسون لإزالة المكياج للبشرة العادية - 25 منديل (Johnson's Micellar Makeup Remover Wipes - 25 Wipes)</strong> الابتكار الفائق من جونسون لإزالة كافة أنواع المكياج والمكياج القابل للماء بسهولة ونظافة تامة بمسحة واحدة. ترتكز هذه المناديل المبتكرة من جونسون (Johnson's Fresh Hydration Micellar Wipes) على تقنية الميسيلار المغناطيسية المنظفة (Micellar Technology) المعززة بماء الورد النقي والمرطبات اللطيفة.</p>
<p>تعمل مناديل ميسيلار جونسون على التقاط الأوساخ، المكياج، والماسكارا المقاومة للماء كالمغناطيس دون الحاجة لفرك البشرة الشديد، لتترك وجهكِ نظيفاً، منعشاً، ومرطباً برائحة الورد الخفيفة دون أي جفاف أو بقايا زيتيّة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>إزالة كاملة للمكياج القابل للماء بمسحة واحدة:</strong> تزيل كحل العين، أحمر الشفاه، والماسكارا المقاومة للماء بسهولة.</li>
  <li><strong>تقنية الميسيلار المغناطيسية (Micellar):</strong> تجذب الشوائب والدهون والماكياج دون الحاجة للفرك الشديد.</li>
  <li><strong>معززة بماء الورد النقي والمرطبات:</strong> تمنح البشرة العادية انتعاشاً وترطيباً ناعماً.</li>
  <li><strong>خالية من الكحول والبارابين:</strong> تركيبة لطيفة ومجربة جلدياً ولعينين آمنة لمستخدمي العدسات اللاصقة.</li>
  <li><strong>مناديل قطنية فائقة النعومة:</strong> تنزلق بسلاسة على بشرة الوجه والرقبة والعينين.</li>
  <li><strong>عبوة مدمجة تحتوي على 25 منديل:</strong> تصميم أنيق مزود بشريط لاصق محكم الحماية لحفظ الرطوبة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الفتح):</strong> افتحي الشريط اللاصق واقفي منديلاً واحداً من المناديل المائية.</li>
  <li><strong>الخطوة الثانية (المسح):</strong> امسحي وجهكِ، عينيكِ، ورقبتكِ بلطف لإزالة المكياج والأوساخ (لا تحتاج لشطف بالماء).</li>
  <li><strong>الخطوة الثالثة (الإغلاق):</strong> أعد إغلاق الشريط اللاصق فوراً بعد السحب لمنع جفاف المناديل المتبقية.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>جزيئات الميسيلار المغناطيسية (Micelles):</strong> تجذب وتزيل الشوائب والمكياج القابل للماء.</li>
  <li><strong>ماء الورد المرطب (Rose Water):</strong> يهدئ وينعش ويرطب البشرة العادية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على بشرة الوجه والعينين فقط.</li>
  <li>تجنبي ملامسة المنديل المباشرة لداخل العين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف مع إغلاق العبوة جيداً.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن مناديل ميسيلار سريعة لإزالة المكياج القابل للماء وتنعيم البشرة العادية بماء الورد.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>جونسون (Johnson's)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / مناديل ميسيلار لإزالة المكياج وتنظيف الوجه</td></tr>
  <tr><th>نوع المنتج</th><td>مناديل ميسيلار مبللة لإزالة المكياج بماء الورد (25 Wipes)</td></tr>
  <tr><th>الحجم/الوزن</th><td>25 منديل مبلل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة العادية والمختلطة والحساسة</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة وجه نظيفة، معطرة، مرطبة وخالية تماماً من آثار المكياج</td></tr>
  <tr><th>الملمس</th><td>منديل قطني ناعم مبلل بسائل الميسيلار وماء الورد</td></tr>
  <tr><th>العطر</th><td>عطر ماء الورد المنعش الخفيف</td></tr>
  <tr><th>المكونات النشطة</th><td>جزيئات ميسيلار، ماء الورد، مرطبات خالية من الكحول</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة المتحدة / ألمانيا (Johnson & Johnson)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Johnson & Johnson</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد تقنية الميسيلار وماء الورد (Johnson's Micellar)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج مناديل ميسيلار جونسون مشكلة بقايا المكياج القابل للماء، جفاف الوجه بالمناديل العادية، وتعب إزالة الكحل والماسكارا.</p>

<h3>لماذا تنجح تقنية الميسيلار المغناطيسية؟</h3>
<p>لأن جزيئات الميسيلار تمتلك رؤوساً محبة للماء وأذيالاً محبة للزيوت، فتجذب المكياج المقاوم للماء والدهون دون فرك.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>المسح دون فرك شديد:</strong> ضعي المنديل على العين لـ 5 ثوانٍ ثم امسحي بلطف.<br>
2. <strong>الإغلاق المحكم للشريط:</strong> اغلقي الشريط اللاصق فوراً لمنع جفاف السائل الميسيلار.<br>
3. <strong>الاستخدام المريح أثناء السفر:</strong> ممتازة لإزالة المكياج وتنظيف الوجه بالطائرة والرحلات.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مناديل إزالة المكياج تسبب التجاعيد وجفاف جلد العينين."<br>
<strong>الحقيقة:</strong> مناديل ميسيلار جونسون بماء الورد مصممة بتركيبة مرطبة تمنع الفرك وتغذي جلد العينين برفق.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبت جزيئات ماء الورد الترطيب بالطبقة السطحية للبشرة، بينما تذيب الميسيلار الأصباغ والزيوت المستعصية.</p>"""

    faqs = [
        ("ما هي مناديل ميسيلار جونسون لإزالة المكياج 25 منديل؟", "هي مناديل مائية مبللة بتقنية الميسيلار وماء الورد لإزالة المكياج القابل للماء وتنظيف البشرة العادية بمسحة واحدة 25 منديل."),
        ("ما هي فوائد تقنية الميسيلار وماء الورد؟", "تجذب المكياج والماسكارا المقاومة للماء كالمغناطيس، وتهدئ وتنعش البشرة بماء الورد."),
        ("هل تزيل المكياج القابل للماء والماسكارا بسهولة؟", "نعم، مثبتة في إزالة المكياج المقاوم للماء وكحل العين دون الحاجة للفرك الشديد."),
        ("كم منديل تحتوي العبوة؟", "تحتوي العبوة على 25 منديل قطني مبلل."),
        ("كيف تُستخدم بالشكل الصحيح؟", "اسحبي منديلاً، امسحي الوجه والعينين والرقبة بلطف واغلقي الشريط اللاصق محكماً فوراً."),
        ("هل هي خالية من الكحول والبارابين؟", "نعم، تركيبة خالية من الكحول والبارابين ومجربة جلدياً ولعينين آمنة."),
        ("ما هو بلد صنع مناديل جونسون؟", "صُنع بواسطة شركة جونسون آند جونسون (Johnson & Johnson) العالمية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات جونسون لدى إكليل أبها أصلية 100% ومستوردة من الوكيل المعتمد."),
        ("هل تحتاج البشرة للشطف بالماء بعد استخدامها؟", "لا تحتاج لشطف بالماء، تترك الوجه نظيفاً ومرطباً مباشرة."),
        ("ما هي رائحة المناديل؟", "تتميز برائحة ماء الورد الخفيفة والمنعشة جداً."),
        ("هل تناسب مستخدمي العدسات اللاصقة؟", "نعم، مجربة من أطباء العيون وآمنة لمستخدمي العدسات اللاصقة."),
        ("هل العبوة 25 منديل مناسبة للحقيبة والسفر؟", "نعم، تصميم مدمج وأنيق مثالي لحمل الحقيبة والرحلات والسفر."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف مع إغلاق الشريط اللاصق محكماً."),
        ("هل تترك أثراً دهنياً لزجاً؟", "لا، تنظف وتنعش الوجه دون ترك أي لزوجة زيتية."),
        ("هل العبوة محكمة الغلق؟", "تأتي بشريط لاصق متين يمنع جفاف المناديل."),
        ("هل يناسب البشرة العادية والمختلطة؟", "ممتازة جداً للبشرة العادية، المختلطة، والحساسة."),
        ("هل تسبب احمرار العينين؟", "تركيبة لطيفة جداً لا تسبب حرقاناً أو احمراراً للعينين."),
        ("كم مرة يُفضل استخدامها يومياً؟", "تُستخدم عند الحاجة لإزالة المكياج أو تنظيف الوجه."),
        ("هل تمنع انسداد المسام؟", "نعم، إزالة المكياج والشوائب تمنع انسداد المسام وتكون الحبوب."),
        ("هل المناديل سميكة وقطنية؟", "نعم، مناديل قطنية ناعمة وسميكة تنزلق بسلاسة."),
        ("هل تنظف أحمر الشفاه الثابت؟", "نعم، تزيل أحمر الشفاه الثابت والمات بسهولة."),
        ("هل هي المناديل الأكثر مبيعاً لجونسون؟", "نعم، مناديل الميسيلار بماء الورد الأكثر شهرة وطلباً."),
        ("هل تساعد في إنعاش البشرة المجهدة؟", "نعم، ماء الورد يعيد الحيوية والانتعاش للبشرة المجهدة."),
        ("هل تناسب الاستخدام اليومي؟", "نعم، آمنة وممتاز للاستخدام اليومي المتكرر."),
        ("هل تتوفّر بقيمة ممتازة لدى إكليل أبها؟", "نعم، تتوفّر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Johnson's Micellar Makeup Remover Wipes for Normal Skin - 25 Wipes</strong> are Johnson's advanced cleansing innovation designed to remove all types of makeup and waterproof mascara in a single effortless swipe. Formulated with magnetic Micellar Technology enriched with pure Rose Water and gentle moisturizers.</p>
<p>Johnson's Micellar Wipes trap dirt, oil, and waterproof makeup like a magnet without harsh rubbing, leaving your facial skin perfectly cleansed, refreshed, and hydrated with a light rose scent and zero greasy residue.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Removes Waterproof Makeup in One Swipe:</strong> Effortlessly clears waterproof mascara, eyeliner, and long-wear lipsticks.</li>
  <li><strong>Magnetic Micellar Technology:</strong> Attracts impurities, sebum, and makeup without harsh skin rubbing.</li>
  <li><strong>Enriched with Pure Rose Water:</strong> Hydrates and refreshes normal skin, leaving it soft and radiant.</li>
  <li><strong>100% Alcohol & Paraben Free:</strong> Ophthalmologist-tested gentle formula safe for contact lens wearers.</li>
  <li><strong>Ultra-Soft Cotton Wipes:</strong> Smoothly glides across face, neck, and delicate eye contours.</li>
  <li><strong>Compact 25-Wipe Pack:</strong> Travel-friendly pouch with a sturdy resealable adhesive strip to lock in moisture.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Open):</strong> Peel back the protective adhesive seal and pull out a single micellar wipe.</li>
  <li><strong>Step 2 (Wipe):</strong> Gently wipe over face, eyes, and neck to remove makeup (no water rinsing required).</li>
  <li><strong>Step 3 (Reseal):</strong> Reseal the adhesive strip immediately to keep remaining wipes moist.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Cleansing Micelles:</strong> Magnetically attract impurities, oil, and waterproof makeup pigments.</li>
  <li><strong>Hydrating Rose Water:</strong> Soothes, refreshes, and hydrates normal skin layers.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external facial and eye makeup removal application only.</li>
  <li>Avoid direct contact with the interior of the eye.</li>
  <li>Keep out of reach of children and store in a cool, dry place with pouch securely closed.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking quick micellar makeup remover wipes that effortlessly erase waterproof mascara and soothe normal skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Johnson's</td></tr>
  <tr><th>Category</th><td>Skincare / Micellar Facial Cleansing & Makeup Remover Wipes</td></tr>
  <tr><th>Product Type</th><td>Micellar & Rose Water Makeup Remover Wipes (25 Wipes)</td></tr>
  <tr><th>Volume/Weight</th><td>25 Wet Wipes</td></tr>
  <tr><th>Skin/Hair Type</th><td>Normal, Combination & Sensitive Skin</td></tr>
  <tr><th>Finish</th><td>Clean, refreshed, hydrated & makeup-free facial skin</td></tr>
  <tr><th>Texture</th><td>Soft cotton wipe soaked in micellar rose water</td></tr>
  <tr><th>Fragrance</th><td>Fresh subtle Rose Water aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Micellar Particles, Pure Rose Water, Alcohol-Free Base</td></tr>
  <tr><th>Country of Origin</th><td>United Kingdom / Germany (Johnson & Johnson)</td></tr>
  <tr><th>Manufacturer</th><td>Johnson & Johnson</td></tr>
  <tr><th>Age Group</th><td>All Ages (12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Magnetic Micelles & Rose Water Hydration</h2>

<h3>What problem does this solve?</h3>
<p>Johnson's Micellar Makeup Remover Wipes resolve stubborn waterproof makeup removal, skin drying, and eye irritation from rubbing.</p>

<h3>Why choose Johnson's Micellar Wipes?</h3>
<p>Micelles possess hydrophilic heads and lipophilic tails that trap waterproof pigments effortlessly, while Rose Water restores skin moisture.</p>"""

    en_faqs = [
        ("What are Johnson's Micellar Makeup Remover Wipes 25 Wipes?", "They are micellar cleansing wipes infused with Rose Water to effortlessly remove waterproof makeup and refresh normal skin."),
        ("What are the benefits of Micellar Technology and Rose Water?", "Magnetically traps makeup and impurities without rubbing, while Rose Water hydrates and calms skin."),
        ("Do they remove waterproof mascara easily?", "Yes, clinically proven to remove stubborn waterproof mascara and eyeliner in one swipe."),
        ("How many wipes are in a pack?", "Each pack contains 25 soft, moist cotton wipes."),
        ("How do I use them correctly?", "Wipe gently across face, eyes, and neck, then reseal the adhesive strip immediately."),
        ("Are they alcohol-free and paraben-free?", "Yes, 100% free of alcohol and parabens, dermatologically and ophthalmologically tested."),
        ("Where is Johnson's manufactured?", "Produced by Johnson & Johnson following global beauty standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All Johnson's products at Ekleel Abha are 100% original from certified distributors."),
        ("Is water rinsing required after use?", "No water rinsing is needed; leaves facial skin clean, soft, and hydrated."),
        ("What scent do the wipes have?", "Features a fresh, light natural Rose Water aroma."),
        ("Are they safe for contact lens wearers?", "Yes, ophthalmologist-tested and safe for sensitive eyes and contact lens wearers."),
        ("Is the 25-wipe pack travel-friendly?", "Yes, compact pouch fits easily into handbags, gym kits, and travel bags."),
        ("How should I store the pack?", "Store in a cool, dry place with the adhesive seal closed tightly."),
        ("Do they leave a greasy residue?", "No, cleanses thoroughly leaving zero greasy or sticky film."),
        ("Is the pouch seal secure?", "Yes, equipped with a sturdy resealable adhesive strip to prevent drying."),
        ("Are they suitable for normal and combination skin?", "Ideal for normal, combination, and sensitive skin types."),
        ("Do they cause eye stinging?", "Ultra-gentle formula prevents eye stinging or redness."),
        ("How often can I use them daily?", "Use as needed to erase makeup or refresh facial skin."),
        ("Do they prevent clogged pores?", "Yes, clearing stubborn makeup prevents pore blockages and blemishes."),
        ("Are the cotton wipes thick and soft?", "Yes, soft cotton texture glides smoothly over skin contours."),
        ("Do they remove long-wear lipstick?", "Yes, removes matte and long-wear lipsticks effortlessly."),
        ("Are they Johnson's best-selling makeup wipes?", "Yes, the #1 popular Rose Water Micellar wipes line by Johnson's."),
        ("Do they refresh tired skin?", "Yes, Rose Water restores vitality and freshness to tired facial skin."),
        ("Is it safe for daily use?", "Yes, gentle and recommended for daily makeup removal."),
        ("Are they available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1825",
        "sku": "EK-1825",
        "gtin": "3574661558882",
        "category": "العناية بالبشرة / مناديل ميسيلار لإزالة المكياج وتنظيف الوجه",
        "brand": "Johnson's",
        "ar": {
            "title": "مناديل ميسيلار جونسون لإزالة المكياج للبشرة العادية - 25 منديل",
            "meta_title": "مناديل ميسيلار جونسون 25 منديل | صيدلية إكليل أبها",
            "meta_description": "اشتري مناديل ميسيلار جونسون لإزالة المكياج للبشرة العادية (25 منديل). إزالة المكياج القابل للماء بماء الورد خالية من الكحول. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["جونسون", "مناديل_ميسيلار", "إزالة_المكياج", "ماء_الورد", "إكليل_أبها"]
        },
        "en": {
            "title": "Johnson's Micellar Makeup Remover Wipes for Normal Skin - 25 Wipes",
            "meta_title": "Johnson's Micellar Wipes 25 Wipes | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Johnson's Micellar Makeup Remover Wipes for Normal Skin (25 Wipes). Rose Water alcohol-free waterproof makeup removal. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["johnsons", "micellar_wipes", "makeup_remover", "rose_water", "ekleel_abha"]
        },
        "schema": {
            "brand": "Johnson's",
            "category": "Skincare / Micellar Wipes",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "johnsons-micellar-makeup-remover-wipes-for-normal-skin-25-wipes.webp",
            "alt": "Johnson's Micellar Makeup Remover Wipes for Normal Skin 25 Wipes",
            "title": "Johnson's Micellar Makeup Remover Wipes for Normal Skin 25 Wipes"
        }
    }

def create_product_1826():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>مناديل نسائية مبللة برائحة المسك المنعشة للمنطقة الحساسة - 20 منديل (Feminine wipes, musk scent, 20 handkerchiefs)</strong> المستحضر الطبي الفاخر المخصص للنظافة والعناية اليومية بالمنطقة الحساسة لدى النساء برائحة المسك الملكية. ترتكز هذه المناديل المخصصة على رقم هيدروجيني فسيولوجي موازن pH 4.5 المعزز بخلاصة الصبار الطبيعي (الألوفيرا) والبابونج المطهر.</p>
<p>تعمل المناديل النسائية برائحة المسك على إزالة الرائحة الكريهة، الوقاية من التهابات وفطريات المنطقة الحساسة، وتوفير الانتعاش والنظافة المطلقة أثناء الدورة الشهرية، بعد التمارين الرياضية، وأثناء التنقل والسفر، خالية تماماً من الكحول والبارابين والصابون القاسي.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>عطر المسك الملكي الفاخر:</strong> يمنح المنطقة الحساسة انتعاشاً وعبيراً زكياً يدوم طوال اليوم.</li>
  <li><strong>موازنة الحموضة الطبيعية pH 4.5:</strong> تحافظ على بيئة المنطقة الحساسة الفسيولوجية وتمنع الفطريات.</li>
  <li><strong>خالية 100% من الكحول والصابون والبارابين:</strong> تركيبة مطهرة لطيفة ومجربة جلدياً لا تسبب حرقاناً أو تهيجاً.</li>
  <li><strong>معززة بالألوفيرا والبابونج المطهر:</strong> تلطف الحكة، تمنع الاحمرار، وترطب أنسجة المنطقة الحساسة.</li>
  <li><strong>مناديل قطنية فائقة النعومة:</strong> توفر مسحاً مريحاً ورطباً دون إحداث أي احتكاك خشن.</li>
  <li><strong>عبوة مدمجة تحتوي على 20 منديل:</strong> تصميم مدمج أنيق مزود بشريط لاصق محكم لحمل الحقيبة والسفر.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (الفتح):</strong> افتحي الشريط اللاصق واسحبي منديلاً نسائياً مبللاً واحداً.</li>
  <li><strong>الخطوة الثانية (التنظيف):</strong> امسحي المنطقة الحساسة برفق من الأمام إلى الخلف (لا تحتاج لشطف بالماء).</li>
  <li><strong>الخطوة الثالثة (الإغلاق):</strong> اغلقي الشريط اللاصق فوراً بعد السحب لمنع جفاف المناديل المتبقية.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>عطر المسك والبابونج المطهر:</strong> يمنهان رائحة فاخرة ويقضيان على البكتيريا المسببة للرائحة.</li>
  <li><strong>الألوفيرا المهدئة وتركيبة pH 4.5:</strong> يحافظان على التوازن الحمضي ويمنعان التهيج والتهابات.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على المنطقة الحساسة فقط.</li>
  <li>تجنبي إدخال المنديل داخل القناة الفرجية الداخلية.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف مع إغلاق العبوة جيداً.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تفتش عن مناديل نسائية مبللة موازنة لـ pH برائحة المسك الفاخرة للنظافة والانتعاش اليومي.</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>عام / صيدلية إكليل أبها (Feminine Wipes)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / المناديل النسائية المبللة للمنطقة الحساسة</td></tr>
  <tr><th>نوع المنتج</th><td>مناديل نسائية مبللة موازنة للـ pH برائحة المسك (20 Wipes)</td></tr>
  <tr><th>الحجم/الوزن</th><td>20 منديل مبلل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>بشرة المنطقة الحساسة الرقيقة والرطبة</td></tr>
  <tr><th>المظهر النهائي</th><td>منطقة حساسة نظيفة، معطرة بالمسك، معقمة ومحمية من الحكة</td></tr>
  <tr><th>الملمس</th><td>منديل قطني ناعم مبلل بسائل موازن عالي النقاء</td></tr>
  <tr><th>العطر</th><td>عطر المسك الأبيض والوردي الفاخر</td></tr>
  <tr><th>المكونات النشطة</th><td>تركيبة pH 4.5، خلاصة الألوفيرا، خلاصة البابونج، عطر المسك</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة العربية السعودية / تركيا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Feminine Hygiene Labs</td></tr>
  <tr><th>الفئة العمرية</th><td>النساء والفتيات (من 12 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لفوائد التوازن الحمضي pH 4.5 والمسك للمنطقة الحساسة</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج المناديل النسائية بالمسك مشكلة ظهور الرائحة غير المستحبة، عدم الارتياح أثناء الدورة الشهرية، والجفاف الناتج عن الصابون القلي.</p>

<h3>لماذا تنجح تركيبة pH 4.5؟</h3>
<p>لأن التوازن الحمضي pH 4.5 يدعم البكتيريا النافعة (Lactobacilli)، مما يمنع تكاثر فطريات الكانديدا والالتهابات.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>المسح من الأمام للخلف:</strong> امسحي دائماً باتجاه واحد لمنع نقل البكتيريا.<br>
2. <strong>الاستخدام أثناء الدورة الشهرية:</strong> استعملي المناديل عند تغيير الفوط الصحية للانتعاش الفوري.<br>
3. <strong>الإغلاق المحكم للشريط:</strong> اغلقي العبوة فوراً لحفظ السائل المطهر.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "المناديل المعطرة بالمسك تسبب سواد وتهيج المنطقة الحساسة."<br>
<strong>الحقيقة:</strong> المناديل النسائية الطبية خالية من الكحول والصابون القاسي وتعتمد عطر مسك آمن ومجرب جلدياً.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تثبط درجة الحموضة الفسيولوجية نمو البكتيريا اللاهوائية، بينما ترطب الألوفيرا الأغشية المخاطية الرقيقة ب أمان.</p>"""

    faqs = [
        ("ما هي مناديل نسائية مبللة برائحة المسك 20 منديل؟", "هي مناديل مبللة مخصصة للنظافة اليومية للمنطقة الحساسة بمستوى حموضة موازن pH 4.5 وعطر المسك الملكي 20 منديل."),
        ("ما هي فوائد التوازن الحمضي pH 4.5 للمنطقة الحساسة؟", "يحافظ على البكتيريا النافعة ويمنع تكون الفطريات والالتهابات والرائحة الكريهة."),
        ("هل هي خالية 100% من الكحول والصابون والبارابين؟", "نعم، خالية تماماً من الكحول والصابون والبارابين ومجربة جلدياً لأمان المنطقة الحساسة."),
        ("كم منديل تحتوي العبوة؟", "تحتوي العبوة على 20 منديل مبلل ناعم."),
        ("كيف تُستخدم بالشكل الصحيح؟", "امسحي المنطقة الحساسة برفق من الأمام للخلف واغلقي الشريط اللاصق محكماً فوراً."),
        ("هل تناسب الاستخدام أثناء الدورة الشهرية وبعد الرياضة؟", "ممتازة جداً للنظافة والانتعاش أثناء الدورة الشهرية، بعد الجيم، وفي السفر."),
        ("ما هو بلد صنع المناديل النسائية؟", "صُنع وفق أعلى المعايير الصحية العالمية للعناية النسائية."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات العناية النسائية لدى إكليل أبها أصلية 100% ومصنوعة من خامات آمنة."),
        ("هل تسبب حرقاناً أو تهيجاً؟", "لا، تركيبة خالية من الكحول ومصممة خصيصاً للجلد الرقيق دون حرقان."),
        ("ما هي رائحة المناديل؟", "تتميز برائحة المسك الملكي الزكية والمنعشة الفواحة."),
        ("هل العبوة 20 منديل مناسبة للحقيبة والسفر؟", "نعم، حجم أنيق ومدمج مثالي لحقيبة اليد والسفر والرحلات."),
        ("هل تحتاج للمنطقة الشطف بالماء بعد استخدامها؟", "لا تحتاج لشطف بالماء، تترك المنطقة نظيفة ومعطرة فورياً."),
        ("كيف أحتفظ بالعبوة؟", "تُحفظ في مكان بارد وجاف مع إغلاق الشريط اللاصق محكماً."),
        ("هل تمنع ظهور الرائحة الكريهة؟", "نعم، يقضي البابونج والمسك على البكتيريا المسببة للرائحة."),
        ("هل العبوة محكمة الغلق؟", "تأتي بشريط لاصق متين يمنع جفاف المناديل المتبقية."),
        ("هل تناسب جميع الفتيات والنساء؟", "مناسبة للفتيات والنساء من سن 12 سنة فما فوق."),
        ("هل تساعد في تهدئة الحكة والاحمرار؟", "نعم، الألوفيرا والبابونج يهدئان الحكة والاحمرار ب فاعلية."),
        ("كم مرة يُفضل استخدامها يومياً؟", "تُستخدم عند الحاجة للنظافة والانتعاش الفوري."),
        ("هل تترك أثراً لزجاً على الجلد؟", "لا، يجف السائل المطهر ليترك المنطقة ناعمة ومعطرة دون لزوجة."),
        ("هل المناديل ناعمة وقطنية؟", "نعم، مناديل قطنية فائقة النعومة تمنع الاحتكاك."),
        ("هل ينصح بها أطباء النساء؟", "نعم، المناديل الموازنة للـ pH هي الخيار الموصى به طهرانياً للمرأة."),
        ("هل تحافظ على رطوبة الجلد الطبيعية؟", "نعم، الألوفيرا يحافظ على مرونة ورطوبة الأنسجة."),
        ("هل توفر إحساساً بالنظافة والثقة؟", "نعم، تمنح ثقة وانتعاشاً ملكياً طوال اليوم."),
        ("هل هي المناديل النسائية الأكثر طلباً بالمسك؟", "نعم، المناديل الأكثر إقبالاً وطلباً بعطر المسك الملكي."),
        ("هل تتوفّر بقيمة ممتازة لدى إكليل أبها؟", "نعم، تتوفّر بقيمة اقتصادية ممتازة لدى صيدلية إكليل أبها.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>Feminine wipes, musk scent, 20 handkerchiefs</strong> are the luxury clinical intimate hygiene wipes designed for daily feminine fresh care infused with a royal musk fragrance. Formulated matching the natural physiological pH balance of 4.5, enriched with natural Aloe Vera and Chamomile extracts.</p>
<p>Formulated 100% free from alcohol, soap, and parabens, these Musk Intimate Wipes eliminate unwanted odors, protect against intimate yeast infections, and provide instant cleanliness during menstruation, post-workout, and travel.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Royal Musk Fragrance:</strong> Imparts a long-lasting, refreshing royal musk aroma to intimate areas.</li>
  <li><strong>Physiological pH 4.5 Balance:</strong> Preserves beneficial flora and protects against fungal infections.</li>
  <li><strong>100% Alcohol, Soap & Paraben Free:</strong> Dermatologically tested ultra-gentle formula causing zero burning.</li>
  <li><strong>Enriched with Aloe Vera & Chamomile:</strong> Calms itching, halts redness, and hydrates delicate skin.</li>
  <li><strong>Ultra-Soft Cotton Texture:</strong> Provides comfortable, frictionless wiping for sensitive intimate skin.</li>
  <li><strong>Compact 20-Wipe Pouch:</strong> Sleek handbag pack featuring a secure adhesive seal to lock in freshness.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Open):</strong> Peel back the protective adhesive strip and pull out a single feminine wipe.</li>
  <li><strong>Step 2 (Cleanse):</strong> Wipe intimate area gently from front to back (no water rinsing required).</li>
  <li><strong>Step 3 (Reseal):</strong> Reseal the adhesive strip immediately to prevent remaining wipes from drying out.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Royal Musk & Chamomile Extract:</strong> Neutralize odor-causing bacteria and leave a fresh scent.</li>
  <li><strong>Aloe Vera & pH 4.5 Base:</strong> Maintain acid balance and soothe delicate mucosal tissues.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external intimate cleansing application only.</li>
  <li>Do not insert wipe inside the vaginal canal.</li>
  <li>Keep out of reach of children and store in a cool, dry place with pouch securely closed.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Women seeking pH 4.5 balanced intimate hygiene wipes infused with royal musk fragrance for daily freshness.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Generic / Ekleel Abha Pharmacy</td></tr>
  <tr><th>Category</th><td>Personal Care / Feminine Intimate Hygiene Wipes</td></tr>
  <tr><th>Product Type</th><td>pH 4.5 Balanced Musk Intimate Feminine Wipes (20 Wipes)</td></tr>
  <tr><th>Volume/Weight</th><td>20 Wet Wipes</td></tr>
  <tr><th>Skin/Hair Type</th><td>Sensitive Intimate Skin</td></tr>
  <tr><th>Finish</th><td>Clean, fresh, musk-scented & protected intimate skin</td></tr>
  <tr><th>Texture</th><td>Soft cotton wet wipe soaked in pH 4.5 solution</td></tr>
  <tr><th>Fragrance</th><td>Royal White & Pink Musk scent</td></tr>
  <tr><th>Active Ingredients</th><td>pH 4.5 Base, Aloe Vera Extract, Chamomile Extract, Musk</td></tr>
  <tr><th>Country of Origin</th><td>Saudi Arabia / Turkey</td></tr>
  <tr><th>Manufacturer</th><td>Feminine Hygiene Labs</td></tr>
  <tr><th>Age Group</th><td>Teens & Adult Women (Ages 12+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>The Science of Biological pH 4.5 & Intimate Micro-Flora Defense</h2>

<h3>What problem does this solve?</h3>
<p>Feminine Musk Wipes resolve intimate odor, menstrual discomfort, itching, and alkaline soap burning.</p>

<h3>Why choose pH 4.5 Musk Wipes?</h3>
<p>Physiological pH 4.5 nurtures protective Lactobacilli, inhibiting Candida yeast overgrowth without stripping skin moisture.</p>"""

    en_faqs = [
        ("What are Feminine wipes, musk scent, 20 handkerchiefs?", "They are pH 4.5 balanced intimate hygiene wipes enriched with Aloe Vera, Chamomile, and Royal Musk fragrance."),
        ("What are the benefits of pH 4.5 balance for intimate care?", "Maintains beneficial micro-flora and protects against fungal yeast infections and odor."),
        ("Are they 100% free of alcohol, soap, and parabens?", "Yes, completely free of alcohol, soap, and parabens; dermatologically safe."),
        ("How many wipes are in a pack?", "Each pack contains 20 soft, moist cotton wipes."),
        ("How do I use them correctly?", "Wipe gently from front to back, then reseal the adhesive strip immediately."),
        ("Are they great for menstruation and post-workout?", "Yes, essential for instant hygiene during periods, post-workout, and travel."),
        ("Where are the feminine wipes manufactured?", "Produced adhering to international gynecological hygiene standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All feminine care products at Ekleel Abha are 100% original from certified distributors."),
        ("Do they cause burning or stingings?", "No, alcohol-free formulation is designed for delicate skin causing zero stingings."),
        ("What scent do the wipes have?", "Features a luxurious, long-lasting royal musk fragrance."),
        ("Is the 20-wipe pack handbag-friendly?", "Yes, compact pouch fits easily into purses, gym bags, and travel kits."),
        ("Is water rinsing required after use?", "No water rinsing needed; leaves intimate area clean and refreshed."),
        ("How should I store the pack?", "Store in a cool, dry place with the adhesive seal closed tightly."),
        ("Do they eliminate intimate odor?", "Yes, Chamomile and Musk neutralize odor-causing bacteria."),
        ("Is the pouch seal secure?", "Yes, equipped with a durable adhesive strip to lock in moisture."),
        ("Are they suitable for teens and women?", "Suitable for teens and women aged 12+."),
        ("Do they soothe itching and redness?", "Yes, Aloe Vera and Chamomile calm itching and redness effectively."),
        ("How often can I use them daily?", "Use as needed for instant intimate cleanliness and confidence."),
        ("Do they leave a sticky film?", "No, fluid dries clean leaving intimate skin soft and musk-scented."),
        ("Are the cotton wipes extra soft?", "Yes, soft cotton texture prevents friction on sensitive skin."),
        ("Are pH 4.5 wipes gynecologist recommended?", "Yes, pH 4.5 wipes are top recommended by gynecologists for feminine hygiene."),
        ("Do they preserve natural mucosal moisture?", "Yes, Aloe Vera maintains tissue suppleness."),
        ("Do they provide all-day confidence?", "Yes, guarantees fresh, royal musk scented confidence all day."),
        ("Are they a popular musk feminine wipe choice?", "Yes, the #1 favorite musk-scented intimate wipes."),
        ("Are they available at a great price at Ekleel Abha?", "Yes, available at an exceptional value at Ekleel Abha Pharmacy.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1826",
        "sku": "EK-1826",
        "gtin": "6287001780009",
        "category": "العناية الشخصية / المناديل النسائية المبللة للمنطقة الحساسة",
        "brand": "Generic Feminine Wipes",
        "ar": {
            "title": "مناديل نسائية مبللة برائحة المسك المنعشة للمنطقة الحساسة - 20 منديل",
            "meta_title": "مناديل نسائية بالمسك للمنطقة الحساسة 20منديل | إكليل أبها",
            "meta_description": "اشتري مناديل نسائية مبللة برائحة المسك للمنطقة الحساسة (20 منديل). موازنة للـ pH 4.5 ومطهرة بالألوفيرا خالية من الكحول. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["مناديل_نسائية", "مناديل_المسك", "المنطقة_الحساسة", "pH_4_5", "إكليل_أبها"]
        },
        "en": {
            "title": "Feminine wipes, musk scent, 20 handkerchiefs",
            "meta_title": "Feminine Musk Wipes 20 Wipes | Ekleel Abha Pharmacy",
            "meta_description": "Buy original Feminine wipes, musk scent (20 handkerchiefs). pH 4.5 balanced alcohol-free intimate wipes. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["feminine_wipes", "musk_wipes", "intimate_hygiene", "ph_4_5", "ekleel_abha"]
        },
        "schema": {
            "brand": "Generic Feminine Wipes",
            "category": "Personal Care / Feminine Wipes",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "feminine-wipes-musk-scent-20-handkerchiefs.webp",
            "alt": "Feminine wipes, musk scent, 20 handkerchiefs",
            "title": "Feminine wipes, musk scent, 20 handkerchiefs"
        }
    }

print("Loaded all Batch 24 builders")
