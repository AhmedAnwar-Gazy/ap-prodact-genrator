import json, os

def _make_collagen_hair_dye_b82(pid, gtin, ar_title, en_title, shade_num, shade_ar, shade_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>{ar_title}</strong> صبغة الشعر الطبية الفاخرة والغنية بالكولاجين الإيطالي الأسطورية المصممة خصيصاً لمنح شعرك لوناً {shade_ar} غنياً، ثابتاً، وناصع التغطية للشيب 100% مع ترميم ألياف كيراتين الشعر أثناء التلوين. ترتكز هذه الصبغة الأصيلة ({en_title}) على مركب الكولاجين البحري المغذي (Marine Collagen Complex)، زيت الأرغان، والتركيبة الخالية من الأمونيا النفاذة الضارة.</p>
<p>تعمل صبغة الشعر بالكولاجين بدرجة {shade_num} على تزويد خصلات الشعر بلون {shade_ar} ساحر، حماية الشعر من التقصف والجفاف، وإغلاق حراشف الشعر لتثبيت البريق، لتترك شعرك ناعماً كالحرير، مرطباً، ناصع اللون، ومحمياً لعدة أسابيع من الاستخدام الأول.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تغطية كاملة 100% للشيب باللون {shade_ar} (درجة {shade_num}):</strong> يمنح مظهراً غنياً وناصعاً.</li>
  <li><strong>ترميم وتكثيف ألياف الشعر بالكولاجين البحري:</strong> يحمي الشعر من الجفاف والتكسر أثناء الصبغ.</li>
  <li><strong>ثبات عالي وبريق زاهٍ يدوم لعدة أسابيع:</strong> يمنع بهتان اللون بفعل الغسيل والشمس.</li>
  <li><strong>تركيبة آمنة خالية من الأمونيا النفاذة:</strong> تناسب الفروة الحساسة والشعر المجهد.</li>
  <li><strong>تغذية وتنعيم بزيت الأرغان الطبيعي:</strong> يترك الشعر ناعماً كالحرير ومفعماً باللمعان.</li>
  <li><strong>طقم صباغة مدمج متكامل:</strong> يتضمن كريم الصبغة والمظهر والقفازات المخصصة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> اخلطي كريم الصبغة {shade_num} مع كريم الأكسجين المرفق في وعاء غير معدني بنسبة 1:1.5.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي المزيج الكريمي على الشعر الجاف النظيف من الجذور حتى الأطراف باستخدام فرشاة الصبغة.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركي الصبغة على الشعر لمدة 30-40 دقيقة ثم اشطفي جيداً بالماء الفاتر والشامبو المخصص.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>الكولاجين البحري وزيت الأرغان:</strong> يملآن الفراغات المجهدة بالبشرة والكيراتين ويمنعان خشونة الصبغة.</li>
  <li><strong>الصبغات الإيطالية الناصعة خالية الأمونيا:</strong> تمنح لون {shade_ar} ثابتاً ومغلفاً بالكامل للشيب.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي الموضعي على شعر الرأس؛ اختبري التحسس قبل 48 ساعة من الاستخدام.</li>
  <li>ارتدي القفازات المخصصة وتجنبي التلامس المباشر مع العينين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة ورجل يبحث عن {ar_title} للتغطية الكاملة للشيب وتلوين الشعر باللون {shade_ar} مع ترميم الكولاجين.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>كولاجين كولور (Collagen Hair Color Italy)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / صبغات الشعر بالكولاجين الإيطالية 100ml</td></tr>
  <tr><th>نوع المنتج</th><td>صبغة شعر طبية خالية من الأمونيا بالكولاجين البحري لتغطية الشيب (درجة {shade_num})</td></tr>
  <tr><th>الحجم/الوزن</th><td>أنبوب الصبغة 100 مل + كريم المظهر</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (خصيصاً الجاف، المجهد، والشعر المصاب بالشيب)</td></tr>
  <tr><th>المظهر النهائي</th><td>شعر ناعم كالحرير، مرطب 24 ساعة، بلون {shade_ar} ناصع وتغطية شيب 100%</td></tr>
  <tr><th>الملمس</th><td>كريم صبغة ناعم متماسك يسهل الخلت والفرك برغوة تغطية</td></tr>
  <tr><th>العطر</th><td>عطر الزهور الإيطالي الناعم الخالي من الأمونيا النفاذة</td></tr>
  <tr><th>المكونات النشطة</th><td>كولاجين بحري مصلح، زيت الأرغان، صبغات إيطالية ثابتة خالية من الأمونيا</td></tr>
  <tr><th>بلد المنشأ</th><td>إيطاليا (Italy)</td></tr>
  <tr><th>الشركة المصنعة</th><td>Professional Hair Color Italy</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغون (من 18 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد الكولاجين البحري وزيت الأرغان في صبغات الكولاجين (Collagen Hair Dye {shade_num})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج صبغة الشعر بالكولاجين بدرجة {shade_num} مشكلة الشيب، جفاف وخشونة الشعر المبوغ، وتلف الكيراتين من الصبغات القديمة.</p>

<h3>لماذا تنجح تركيبة Collagen Hair Dye {shade_num}?</h3>
<p>لأن جزيئات الكولاجين البحري تنفذ لعمق قشرة الشعر مصلحة الألياف أثناء تسلل صبغة {shade_ar} دون أمونيا.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التطبيق على شعر جاف ونظيف بالكامل:</strong> يضمن توزيع وتثبيت لون {shade_ar}.<br>
2. <strong>الالتزام بوقت الانتظار (30-40 دقيقة):</strong> يضمن تغطية 100% للشيب.<br>
3. <strong>الشطف بالماء الفاتر واستخدام بلسم مثبت:</strong> يغلق حراشف الشعر ويحفظ اللون.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "صبغات الشعر الخالية من الأمونيا لا تغطي الشيب جيداً."<br>
<strong>الحقيقة:</strong> صبغة الكولاجين الإيطالية مصممة بصبغات جزيئية متطورة تغطي الشيب 100% وتمنح لوناً غنياً ثابتاً.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يرتبط الكولاجين البحري بسلاسل الببتيدات بالكيراتين مغلفاً جدار الشعر بينما تتوزع صبغة {shade_ar} بنقاء.</p>"""

    faqs_data = [
        (f"ما هي {ar_title}؟", f"هي صبغة شعر طبية خالية من الأمونيا بالكولاجين البحري وزيت الأرغان لتغطية الشيب 100% باللون {shade_ar} (درجة {shade_num})."),
        (f"ما هي فوائد الكولاجين البحري وزيت الأرغان في صبغة {shade_num}؟", f"تغطي الشيب 100%، ترمم الكيراتين والألياف، وتمنح لون {shade_ar} غنياً دون جفاف."),
        (f"هل تغطي الشيب 100% وتمنح لون {shade_ar} بدون أمونيا؟", f"نعم، مثبتة سريرياً في تغطية 100% للشيب وتوفير لون {shade_ar} ناصع وثابت بالكولاجين."),
        ("ما هي محتويات العبوة؟", f"تأتي بأنبوب صبغة سعة 100 مل + كريم المظهر + القفازات."),
        ("كيف تُستخدم بالشكل الصحيح؟", "اخلطي كريم الصبغة والمظهر بنسبة 1:1.5، وزعي على الشعر الجاف، اتركي 30-40 دقيقة واشطفي بالماء الفاتر."),
        ("هل هي خالية من الأمونيا النفاذة؟", "نعم، 100% خالية من الأمونيا ومصممة بعطر إيطالي لطيف."),
        ("أين صُنت صبغة الكولاجين؟", "صُنت في إيطاليا وفق أعلى معايير الجودة الأوروبية."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات الصبغات لدى إكليل أبها أصلية 100%."),
        (f"ما لون صبغة الكولاجين {shade_num}؟", f"لون {shade_ar} ناصع وغني (درجة {shade_num})."),
        ("هل تناسب جميع أنواع الشعر والشيب؟", "نعم، ممتازة لجميع أنواع الشعر والتغطية الكاملة للشيب المزعج."),
        ("هل العبوة مريحة وكافية للشعر؟", "نعم، طقم مدمج أنيق يكفي لصبغة كاملة لشعر متوسط الطول."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل صبغة الكولاجين الإيطالية الماركة الأكثر تفضيلاً؟", "نعم، صبغات الكولاجين الإيطالية الخيار الأكثر شهرة وتفضيلاً لحماية الشعر أثناء الصبغ."),
        ("كم يدوم ثبات اللون؟", "يدوم لعدة أسابيع متواصلة بنفس الزهاء."),
        ("هل ينشطف بسهولة دون ترك لزوجة؟", "نعم، ينشطف بالماء الفاتر والشامبو بسلاسة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل يمنع تقصف وخشونة الشعر المصبوغ؟", "نعم، يعوض الكولاجين وزيت الأرغان رطوبة الشعر فيمنع الخشونة والتقصف."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والرجال؟", "نعم، ممتاز للنساء والرجال."),
        ("هل يناسب الشتاء والصيف؟", "نعم، صباغة وترميم مثالي لجميع فصول السنة."),
        ("هل يصلح هدية ممتازة للعناية بالشعر؟", "نعم، منتج صباغة وتنعيم فاخر وأساسي لكل روتين جمال."),
        (f"هل يعيد المظهر المشرق الناعم للون {shade_ar}؟", f"نعم، يمنح الشعر مظهراً ناصع اللون {shade_ar} ومفعماً باللمعان."),
        ("هل تتوفر درجات صبغة الكولاجين الأخرى؟", "نعم، تتوفر عائلة Collagen Hair Dyes كاملة لدى إكليل أبها."),
        ("هل يفضل إجراء اختبار تحسس قبل الاستخدام؟", "نعم، يُنصح دائماً باختبار التحسس الموضعي قبل 48 ساعة."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury medical Italian collagen-enriched hair dye designed to deliver 100% gray hair coverage, vibrant {shade_en} color (Shade {shade_num}), and deep keratin fiber restoration during chemical coloring. Built upon Marine Collagen Complex, pure Argan Oil, and a 100% ammonia-free formula.</p>
<p>Collagen Hair Dye Shade {shade_num} infuses hair strands with rich {shade_en} tones, shields hair against breakage and dryness, and seals hair cuticles for lasting shine, leaving your hair touchably silky soft, hydrated, brilliantly colored, and protected for weeks from first use.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>100% Gray Hair Coverage with Rich {shade_en} Color (Shade {shade_num}):</strong> Delivers an intense vibrant finish.</li>
  <li><strong>Keratin Fiber Repair & Densification with Marine Collagen:</strong> Protects hair against chemical dryness.</li>
  <li><strong>Long-Lasting Vibrancy & Color Lock for Weeks:</strong> Prevents color washing out or fading in sun.</li>
  <li><strong>100% Ammonia-Free Safe Formula:</strong> Suitable for sensitive scalp and stressed hair.</li>
  <li><strong>Softness & Nourishment with Natural Argan Oil:</strong> Leaves hair silky soft and glossy.</li>
  <li><strong>Complete Coloring Kit Included:</strong> Contains color cream tube, developer cream, and gloves.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Mix color cream Shade {shade_num} with developer cream in a non-metallic bowl at 1:1.5 ratio.</li>
  <li><strong>Step 2:</strong> Apply the smooth creamy mixture onto clean dry hair from roots to tips using a tint brush.</li>
  <li><strong>Step 3:</strong> Leave dye on hair for 30-40 minutes, then rinse thoroughly with warm water and color shampoo.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Marine Collagen & Argan Oil:</strong> Fill keratin cuticle gaps preventing post-dye roughness and breakage.</li>
  <li><strong>Ammonia-Free Italian Color Pigments:</strong> Provide 100% gray coverage and uniform {shade_en} color deposition.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external topical head hair application; perform an allergy test 48 hours prior to use.</li>
  <li>Wear gloves and avoid direct contact with eyes.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_title} for 100% gray hair coverage, {shade_en} hair coloring, and collagen fiber repair.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Collagen Hair Color (Italy)</td></tr>
  <tr><th>Category</th><td>Hair Care / Italian Collagen Hair Dyes 100ml</td></tr>
  <tr><th>Product Type</th><td>Ammonia-Free Marine Collagen 100% Gray Coverage Hair Dye (Shade {shade_num})</td></tr>
  <tr><th>Volume/Weight</th><td>100 ml Color Tube + Developer Cream</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Specifically Dry, Stressed & Gray-Plagued Hair)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, 100% gray-covered & vibrant {shade_en} hair</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-drip conditioning color cream</td></tr>
  <tr><th>Fragrance</th><td>100% Mild fresh Italian floral scent (ammonia-free)</td></tr>
  <tr><th>Active Ingredients</th><td>Marine Collagen Complex, Argan Oil, Ammonia-Free Color Pigments</td></tr>
  <tr><th>Country of Origin</th><td>Italy</td></tr>
  <tr><th>Manufacturer</th><td>Professional Hair Color Italy</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 18+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Marine Collagen Cuticle Repair & Ammonia-Free {shade_en} Color Binding</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves gray hair coverage, post-dye roughness, broken keratin fibers, and harsh ammonia smells.</p>

<h3>Why choose Collagen Hair Dye Shade {shade_num}?</h3>
<p>Marine collagen peptides penetrate the hair shaft repairing internal peptide bonds while ammonia-free pigments deposit rich {shade_en} color.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a medical ammonia-free hair dye with Marine Collagen and Argan Oil for 100% gray coverage in {shade_en} (Shade {shade_num})."),
        (f"What are the benefits of Marine Collagen and Argan Oil in Shade {shade_num}?", f"Provide 100% gray coverage, repair keratin fibers, and deliver vibrant {shade_en} color without dryness."),
        (f"Does it cover 100% gray hair in {shade_en} without ammonia?", f"Yes, clinically proven to deliver 100% gray coverage and vibrant {shade_en} color with Marine Collagen protection."),
        ("What items are included in this kit?", f"100ml color tube + developer cream + protective gloves."),
        ("How do I use it correctly?", "Mix color tube with developer, apply to dry hair, wait 30-40 minutes and rinse with warm water."),
        ("Is it 100% ammonia-free?", "Yes, 100% ammonia-free with a mild fresh Italian floral fragrance."),
        ("Where is Collagen Hair Dye manufactured?", "In Italy to European quality standards."),
        ("How do I verify authenticity at Ekleel Abha?", "All hair dye products at Ekleel Abha are 100% original."),
        (f"What color shade is Collagen Dye {shade_num}?", f"Vibrant rich {shade_en} (Shade {shade_num})."),
        ("Is it suitable for all hair types and gray coverage?", "Yes, excellent for all hair types and complete gray hair coverage."),
        ("Is the kit size convenient for full head dyeing?", "Yes, sleek kit sufficient for full head application on medium hair."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is Italian Collagen Hair Dye a top trusted brand?", "Yes, Italian Collagen Hair Dyes are the premier choice for healthy hair coloring."),
        ("How long does the color stay vibrant?", "Stays vibrant for continuous weeks."),
        ("Does it rinse out smoothly?", "Yes, rinses out smoothly with warm water and color shampoo."),
        ("Is the packaging recyclable?", "Yes."),
        ("Does it prevent post-dye hair roughness?", "Yes, Marine Collagen and Argan Oil restore hair lipids preventing post-dye roughness."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for men and women?", "Yes, suitable for both men and women."),
        ("Is it good for all seasons?", "Yes, ideal hair coloring and repair for summer and winter care."),
        ("Is it a nice hair care gift?", "Yes, a premier luxury hair dye for daily beauty routines."),
        (f"Does it restore smooth shiny {shade_en} hair?", f"Yes, gives hair a vibrant smooth shiny {shade_en} look."),
        ("Are other Collagen Hair Dye shades available?", "Yes, the full Collagen Hair Dye shade range is available at Ekleel Abha."),
        ("Is performing an allergy test recommended prior to use?", "Yes, an allergy patch test 48 hours prior to use is always recommended."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "Collagen Hair Color",
        "ar": {
            "title": ar_title,
            "meta_title": f"{ar_title} | إكليل أبها",
            "meta_description": f"اشتري {ar_title}. صبغة شعر إيطالية خالية من الأمونيا بالكولاجين لتغطية الشيب 100% باللون {shade_ar}. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. Ammonia-free Marine Collagen Italian hair dye for 100% gray coverage in {shade_en}. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2132():
    return _make_collagen_hair_dye_b82(
        pid=2132, gtin="8052742458849",
        ar_title="صبغة شعر  زيتوني كثيف 7.8 بالكولاجين",
        en_title="Intense Olive Hair Dye 7.8 with Collagen",
        shade_num="7.8", shade_ar="زيتوني كثيف", shade_en="Intense Olive",
        tags_ar=["صبغة_الكولاجين", "صبغة_زيتوني_كثيف", "صبغة_الكولاجين_7.8", "صبغة_إيطالية_خالية_من_الأمونيا", "إكليل_أبها"],
        tags_en=["collagen_dye", "intense_olive_dye", "collagen_dye_7.8", "italian_hair_dye", "ekleel_abha"]
    )


def create_product_2133():
    return _make_collagen_hair_dye_b82(
        pid=2133, gtin="8053323158264",
        ar_title="صبغة شعر  ماروني 4.5 بالكولاجين",
        en_title="Maroon Hair Dye 4.5 with Collagen",
        shade_num="4.5", shade_ar="ماروني", shade_en="Maroon",
        tags_ar=["صبغة_الكولاجين", "صبغة_ماروني", "صبغة_الكولاجين_4.5", "صبغة_إيطالية_خالية_من_الأمونيا", "إكليل_أبها"],
        tags_en=["collagen_dye", "maroon_hair_dye", "collagen_dye_4.5", "italian_hair_dye", "ekleel_abha"]
    )


def create_product_2134():
    return _make_collagen_hair_dye_b82(
        pid=2134, gtin="8053323158158",
        ar_title="صبغة شعر  اشقر رمادي غامق 6.01 بالكولاجين",
        en_title="Dark Ash Blonde Hair Dye 6.01 with Collagen",
        shade_num="6.01", shade_ar="أشقر رمادي غامق", shade_en="Dark Ash Blonde",
        tags_ar=["صبغة_الكولاجين", "صبغة_أشقر_رمادي_غامق", "صبغة_الكولاجين_6.01", "صبغة_إيطالية_خالية_من_الأمونيا", "إكليل_أبها"],
        tags_en=["collagen_dye", "dark_ash_blonde_dye", "collagen_dye_6.01", "italian_hair_dye", "ekleel_abha"]
    )


def create_product_2135():
    return _make_collagen_hair_dye_b82(
        pid=2135, gtin="8053323158127",
        ar_title="صبغة شعر كستنائي غامق 6.23 بالكولاجين",
        en_title="Dark Chestnut Hair Dye 6.23 with Collagen",
        shade_num="6.23", shade_ar="كستنائي غامق", shade_en="Dark Chestnut",
        tags_ar=["صبغة_الكولاجين", "صبغة_كستنائي_غامق", "صبغة_الكولاجين_6.23", "صبغة_إيطالية_خالية_من_الأمونيا", "إكليل_أبها"],
        tags_en=["collagen_dye", "dark_chestnut_dye", "collagen_dye_6.23", "italian_hair_dye", "ekleel_abha"]
    )


def create_product_2136():
    return _make_collagen_hair_dye_b82(
        pid=2136, gtin="8052742458825",
        ar_title="صبغة شعرازرق قاع المحيط 6,90 بالكولاجين",
        en_title="Ocean Blue Hair Dye 6.90 with Collagen",
        shade_num="6.90", shade_ar="أزرق قاع المحيط", shade_en="Ocean Blue",
        tags_ar=["صبغة_الكولاجين", "صبغة_أزرق_المحيط", "صبغة_الكولاجين_6.90", "صبغة_إيطالية_خالية_من_الأمونيا", "إكليل_أبها"],
        tags_en=["collagen_dye", "ocean_blue_dye", "collagen_dye_6.90", "italian_hair_dye", "ekleel_abha"]
    )


print("Loaded all 5 Batch 82 builders complete")
