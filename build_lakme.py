import json, os

def build_lakme_product(prod_id, color_en, color_ar, shade_code, gtin, img_slug):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعتبر <strong>كريم صبغة الشعر كولاج ميكس من لاكمي (Lakme Collage Mix Cream Hair Color - {shade_code} {color_ar} 60ml)</strong> الخيار الاحترافي الأول لمصففي الشعر والراغبات في تصحيح ألوان الصبغة وتخصيص درجاتها بدقة عالية. تم تصميم هذه الصبغة الإسبانية الدائمة المصححة (Mixtone) لتحييد النغمات الدافئة غير المرغوب فيها (مثل النغمات البرتقالية أو الصفراء) أو لإضافة لمسة لونية فنية بدرجة {color_ar} مذهلة ومكثفة.</p>
<p>تتميز الفرمولة بكونها نباتية 100% (Vegan) ومنخفضة الأمونيا وخالية من PPD، مدعمة بمركب جزيء OF5 المبتكر المتوافق كلياً مع ألياف الشعر، إضافة إلى مركب AQ-Save الاستثنائي المستخلص من الكستناء العضوية الذي يحافظ على توازن رطوبة ألياف الشعرة. كما يغذي بروتين الصويا والأرجينين هيكل الشعر لمنحه مرونة، حماية، ولمعاناً زجاجياً مبهراً بعد التلوين.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تجميل وتصحيح احترافي للون:</strong> درجة {color_ar} مصححة تفيد في تصحيح النغمات غير المرغوب فيها أو الابتكار في الألوان الفنية.</li>
  <li><strong>جزيء OF5 المبتكر:</strong> جزيء نباتي 100% يحسن كثافة اللون وثباته وتوافقه التام مع ألياف الشعر.</li>
  <li><strong>مركب AQ-Save الهيدراتي:</strong> مستخلص كستناء عضوي يحبس الرطوبة داخل طبقات الشعرة أثناء عملية الصبغ.</li>
  <li><strong>تركيبة نباتية وخالية من PPD:</strong> تركيبة إسبانية لطيفة منخفضة الأمونيا تحمي فروة الرأس وأنسجة الشعر من التلف.</li>
  <li><strong>تعزيز القوة ببروتين الصويا والأرجينين:</strong> حمض أميني وبروتينات طبيعية تعيد بناء هيكل الشعرة وتزيد مرونتها.</li>
  <li><strong>لمعان يدوم طويلاً وتغطية فائقة:</strong> تمنح الشعر بريقاً كراستالياً ولوناً غنياً ومتجانساً من الجذور حتى الأطراف.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التحضير والخلط):</strong> اخلطي صبغة لاكمي كولاج ميكس {shade_code} مع كريم الأكسجين (Developer) بالنسبة الموصى بها في وعاء غير معدني.</li>
  <li><strong>الخطوة الثانية (الدمج كـ Mixtone):</strong> في حال استخدامها كمصحح لون، اخلطي كمية معينة (بالغرامات) مع لون الصبغة الأساسي والمطوّر.</li>
  <li><strong>الخطوة الثالثة (التطبيق):</strong> وزعي المزيج بالتساوي على الشعر الجاف غير المغسول باستخدام فرشاة الصبغة من الجذور وحتى الأطراف.</li>
  <li><strong>الخطوة الرابعة (وقت المعالجة):</strong> اتركي الصبغة على الشعر لمدة 30 إلى 45 دقيقة وفقاً لدرجة التفتيح أو التصحيح المطلوبة.</li>
  <li><strong>الخطوة الخامسة (الشطف والعناية):</strong> اشطفي الشعر جيداً بالماء الفاتر حتى يزول أثر الصبغة، ثم استخدمي الشامبو والبلسم المخصص للشعر المصبوغ.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>جزيء OF5 (Botanical OF5 Molecule):</strong> مركب نباتي ينقل الصبغة لعمق القشرة ويعزز ثبات اللون وإشراقه.</li>
  <li><strong>مركب AQ-Save (Organic Chestnut Extract):</strong> يحافظ على الترطيب المائي للشعر لمنع الجفاف والتقصف أثناء التلوين.</li>
  <li><strong>الأرجينين (Arginine):</strong> حمض أميني طبيعي يوازن حموضة الصبغة بطلف ويعزز قوة الروابط الهيكلية للشعر.</li>
  <li><strong>بروتين الصويا (Soy Protein Complex):</strong> يتغلغل داخل ألياف الشعر ليمنحها نعومة ومرونة ولمعاناً فائقاً.</li>
  <li><strong>تركيبة منخفضة الأمونيا وخالية من PPD:</strong> تحافظ على سلامة جلد الفروة وتمنع التحسس.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي المبتكر على الشعر فقط.</li>
  <li>يجب إجراء اختبار تحسس جلدي بسيط قبل 48 ساعة من التطبيق.</li>
  <li>تجنبي ملامسة المنتج للعينين؛ وفي حال ملامستها اشطفي فوراً بكمية وفيرة من الماء.</li>
  <li>احرصي على ارتداء القفازات المناسبة أثناء التحضير والتطبيق.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لمصففي الشعر والمحترفين الراغبين في تصحيح ألوان الصبغة وتخصيص درجاتها بدقة.</li>
  <li>لكل من تعاني من ظهور نغمات برتقالية أو دافئة غير مرغوبة بعد صبغ الشعر وتريد تحييدها.</li>
  <li>لمحبات الألوان الفنية الجريئة بدرجة {color_ar} الفاخرة.</li>
  <li>مناسب لجميع أنواع الشعر والراغبات في صبغة نباتية آمنة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>لاكمي (Lakme)</td></tr>
  <tr><th>الفئة</th><td>العناية بالشعر / صبغات الشعر الاحترافية</td></tr>
  <tr><th>نوع المنتج</th><td>صبغة شعر كريم دائمة مصححة (Collage Mix / Mixtone)</td></tr>
  <tr><th>الحجم/الوزن</th><td>60 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع الشعر (للتصحيح والتلوين)</td></tr>
  <tr><th>المظهر النهائي</th><td>لون {color_ar} صافٍ، خالي من النغمات غير المرغوبة، ولمعان كريستالي</td></tr>
  <tr><th>الملمس</th><td>كريم متجانس ناعم الخلط</td></tr>
  <tr><th>العطر</th><td>عطر ناعم جداً منخفض الرائحة</td></tr>
  <tr><th>المكونات النشطة</th><td>جزيء OF5، مركب AQ-Save (كستناء عضوي)، أرجينين، بروتين الصويا</td></tr>
  <tr><th>بلد المنشأ</th><td>إسبانيا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Lakme Cosmetics (إسبانيا)</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين (18 سنة فما فوق)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لتقنية تصحيح الألوان وجزيء OF5 (Lakme Collage Mix)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج صبغة لاكمي كولاج ميكس مصحح {color_ar} ({shade_code}) مشكلة انكسار وتغير لون الصبغات وظهور نغمات دافئة مزعجة (مثل اللون البرتقالي أو الأصفر النحاسي) بعد التفتيح، كما توفر حلاً احترافياً لإنشاء درجات ألوان فنية ومخصصة برعاية نباتية عالية.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>عند صبغ الشعر وتفتيحه، تظهر الصبغات الضمنية الطبيعية للشعر (Underlying Pigments) والتي غالباً ما تكون دافئة برتقالية أو حمراء. الصبغات العادية لا تستطيع تحييد هذه الدرجات دون استخدام مصححات متخصصة (Mixtones) تعتمد على دائرة الألوان الفنية.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام دائرة الألوان:</strong> استخدمي اللون {color_ar} لتحييد النغمات المقابلة لها في عجلة ألوان الصبغة.<br>
2. <strong>الالتزام بالنسب:</strong> اخلطي غرامات معدودة من مصحح الميكس مع لون الصبغة الأساسية لعدم إطغاء اللون.<br>
3. <strong>اختيار الأكسجين المناسب:</strong> استخدمي مطور لاكمي المخصص للحصول على أفضل دمج وتغطية.<br>
4. <strong>العناية بالشعر المصبوغ:</strong> اغسلي الشعر بشامبو خالٍ من السلفات للحفاظ على ثبات بريق اللون.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "صبغات المصحح (Mixtone) تُستخدم كصبغة كاملة فقط."<br>
<strong>الحقيقة:</strong> صُممت صبغات الميكس لتخلط بنسب غرامية دقيقة مع الألوان الأساسية لتحييد الألوان الدافئة أو تعزيز بريق الدرجة.</p>
<p><strong>خرافة:</strong> "الصبغات الاحترافية تلف شعر الفروة."<br>
<strong>الحقيقة:</strong> صبغة لاكمي خالية من PPD ومنخفضة الأمونيا ومدعمة بمركب AQ-Save من الكستناء العضوي الذي يحمي مرونة ونعومة ألياف الشعر.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعتمد المنتج على تقنية جزيء <strong>OF5 النباتي</strong> المتوافق بنسبة 100% مع ألياف الشعر، حيث يحسن نقل الصبغيات النانوية إلى عمق القشرة (Cortex). يقوم مركب <strong>AQ-Save</strong> المشتق من الكستناء العضوي بربط جزيئات الماء بالبروتينات الهيكلية، بينما يعيد <strong>الأرجينين وبروتين الصويا</strong> بناء روابط الببتيد المكسورة، مما يثبت اللون المصحح ويرمم غشاء الشعر الخارجي.</p>"""

    faqs = [
        (f"ما هي صبغة لاكمي كولاج ميكس درجة {shade_code} ({color_ar})؟", f"هي صبغة إسبانية احترافية دائمة مصححة (Mixtone) درجة {color_ar} تُستخدم لتحييد النغمات غير المرغوب فيها أو لمنح لون فني صافٍ ومشرق."),
        ("ما هي فائدة استخدام صبغات الميكس (Mixtones)؟", "تُستخدم صبغات الميكس لدمجها مع ألوان الصبغات الأساسية لتحييد الألوان الدافئة غير المرغوبة (مثل البرتقالي أو الأصفر) أو لإنشاء درجات ألوان مخصصة."),
        ("هل صبغة لاكمي كولاج ميكس خالية من PPD ونباتية؟", "نعم، هي صبغة نباتية 100% (Vegan) خالية من PPD ومصنوعة بمكونات إسبانية عالية الجودة."),
        ("ما هو جزيء OF5 الموجود في الصبغة؟", "هو جزيء نباتي مبتكر من لاكمي متوافق كلياً مع ألياف الشعر يحسن ثبات اللون وكثافته وإشراقه."),
        ("ما فائدة مركب AQ-Save المستخلص من الكستناء؟", "يحافظ على توازن الترطيب الداخلي لألياف الشعر ويحميه من الجفاف والتقصف أثناء عملية الصبغ."),
        ("كيف يتم خلط صبغة الميكس مع اللون الأساسي؟", "تُضاف غرامات بسيطة (تترواح من 2 إلى 10 غرامات) من صبغة الميكس إلى أنبوب الصبغة الأساسية مع مطور الأكسجين وتخلط جيداً."),
        ("هل يمكن استخدام الصبغة بمفردها على الشعر؟", "نعم، يمكن استخدامها بمفردها على شعر مفتح مسبقاً للحصول على لون فني جريء بدرجة {color_ar}."),
        ("ما نسبة الخلط الموصى بها مع الأكسجين؟", "نسبة الخلط القياسية لصبغة لاكمي كولاج هي 1 : 1.5 مع كريم الأكسجين (Developer)."),
        ("كم من الوقت تُترك الصبغة على الشعر؟", "تُترك من 30 إلى 45 دقيقة تبعاً لدرجة التغطية والتصحيح المطلوبة."),
        ("هل الصبغة تحتوي على أمونيا عالية؟", "لا، تمتاز بتركيبة منخفضة الأمونيا تحافظ على سلامة فروة الرأس وأنسجة الشعر."),
        ("ما دور بروتين الصويا والأرجينين في الصبغة؟", "يعيدان بناء البروتينات المكسورة في الشعر ويمنحان الخصلات مرونة ونعومة ولمعاناً كريستالياً."),
        ("هل يناسب هذا المنتج جميع أنواع الشعر؟", "نعم، مناسب لجميع أنواع الشعر وخاصة الشعر المفتح أو المصبوغ الذي يحتاج لتصحيح اللون."),
        ("ما حجم أنبوب صبغة لاكمي كولاج؟", "يأتي الأنبوب بحجم 60 مل، وهو حجم قياسي احترافي."),
        ("هل تحتاج الصبغة لاختبار تحسس قبل الاستخدام؟", "نعم، يُنصح دائماً بإجراء اختبار تحسس جلدي على منطقة صغيرة قبل 48 ساعة من الصبغ."),
        ("ما هو بلد صنع صبغة لاكمي كولاج؟", "صُنعت بفخر في إسبانيا بواسطة شركة Lakme Cosmetics العالمية."),
        ("هل تسبب الصبغة تقصف الشعر؟", "لا، مركب AQ-Save والأرجينين يحميان ألياف الشعر ويحافظان على ترطيبها أثناء الصبغ."),
        ("هل يمكن استخدامها للشعر الأبيض (الشيب)؟", "عند دمجها مع الألوان الأساسية، تضمن تغطية ممتازة للشعر الأبيض بنسبة 100%."),
        ("ما هي الرائحة الخاصة بصبغة لاكمي؟", "تتميز برائحة لطيفة جداً ومنخفضة النفاذية مقارنة بالصبغات التقليدية."),
        ("كيف أحافظ على ثبات اللون بعد الصبغ؟", "استخدمي مجموعة الشامبو والبلسم الخالية من السلفات والمخصصة للشعر المصبوغ من لاكمي."),
        ("هل الصبغة آمنة للشعر المعالج بالبروتين؟", "نعم، تركيبتها المنخفضة الأمونيا والنباتية تحافظ على سلامة الشعر المعالج."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع صبغات لاكمي لدى صيدلية إكليل أبها أصلية 100% ومستوردة مباشرة من الوكيل المعتمد."),
        ("هل يُفضل غسل الشعر قبل الصبغ مباشرة؟", "يُفضل تطبيق الصبغة على شعر جاف وغير مغسول حديثاً لحماية الفروة بزيوتها الطبيعية."),
        ("هل يمكن خلط أكثر من درجة ميكس معاً؟", "نعم، يمكن للمحترفين خلط درجات ميكس مختلفة لإبتكار ألوان مخصصة وفريدة."),
        ("ما هي الأدوات المناسبة لخلط الصبغة؟", "يُوصى باستخدام وعاء وفرشاة بلاستيكية أو زجاجية وتجنب الأدوات المعدنية."),
        ("هل تلزم القفازات عند تطبيق الصبغة؟", "نعم، ينبغي ارتداء قفازات حماية أثناء الخلط والتطبيق لتجنب تصبغ اليدين.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>Lakme Collage Mix Cream Hair Color ({shade_code} {color_en} 60ml)</strong> is the professional colorist's choice for precise tone neutralization, shade correction, and artistic color customization. Engineered in Spain, this permanent cream mixtone is designed to neutralize unwanted warm undertones (such as orange or brassy yellow) or intensify creative, vibrant {color_en} highlights.</p>
<p>Featuring a 100% vegan, PPD-free, low-ammonia formula, it is enriched with Lakme's breakthrough Botanical OF5 molecule—a plant-derived compound fully compatible with hair fibers. It also incorporates the organic chestnut-derived AQ-Save Complex to lock in hair fiber hydration, while Soy Protein and Arginine fortify hair structure, leaving strands extraordinarily soft, resilient, and crystal-shiny.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Professional Color Correction:</strong> Corrective {color_en} mixtone ideal for neutralizing unwanted warm tones or creating vivid artistic color effects.</li>
  <li><strong>Botanical OF5 Molecule:</strong> 100% plant-derived molecule enhancing color intensity, longevity, and fiber compatibility.</li>
  <li><strong>Hydrating AQ-Save Complex:</strong> Organic chestnut extract that binds moisture within hair layers during the coloring process.</li>
  <li><strong>100% Vegan & PPD-Free Formula:</strong> Gentle Spanish low-ammonia composition protecting scalp comfort and hair health.</li>
  <li><strong>Strengthened with Soy Protein & Arginine:</strong> Natural amino acids and proteins rebuild damaged hair bonds for enhanced elasticity.</li>
  <li><strong>Crystal Shine & Long-Lasting Results:</strong> Delivers vibrant, uniform color reflection with luminous, lasting shine from root to tip.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Mixing Preparation):</strong> Mix Lakme Collage Mix {shade_code} with Lakme Developer at the recommended ratio in a non-metallic bowl.</li>
  <li><strong>Step 2 (Mixtone Blending):</strong> When using as a color corrector, add calculated grams of mixtone to your base dye formula and developer.</li>
  <li><strong>Step 3 (Application):</strong> Apply the cream mixture evenly onto dry, unwashed hair using a tint brush from roots to ends.</li>
  <li><strong>Step 4 (Processing Time):</strong> Allow the color to process for 30 to 45 minutes depending on desired intensity or correction level.</li>
  <li><strong>Step 5 (Rinse & Care):</strong> Rinse thoroughly with warm water until clear, then cleanse with color-safe shampoo and conditioner.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Botanical OF5 Molecule:</strong> Plant-derived ingredient that delivers nano-pigments deep into the cortex for vibrant, lasting color.</li>
  <li><strong>AQ-Save Complex (Organic Chestnut Extract):</strong> Maintains intra-fiber hydration to prevent dryness and breakage during dyeing.</li>
  <li><strong>Arginine:</strong> Natural essential amino acid that gently balances formula pH and reinforces structural hair bonds.</li>
  <li><strong>Soy Protein Complex:</strong> Penetrates hair strands to restore softness, flexibility, and radiant shine.</li>
  <li><strong>PPD-Free & Low-Ammonia Base:</strong> Protects scalp integrity and eliminates aggressive allergic chemical reactions.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For professional and external application on hair only.</li>
  <li>Perform a skin patch test 48 hours prior to full application.</li>
  <li>Avoid direct contact with eyes; rinse immediately with plenty of water if contact occurs.</li>
  <li>Always wear appropriate protective gloves during preparation and application.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from heat.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Hair colorists and individuals seeking precise hair color correction and tone neutralization.</li>
  <li>Anyone wanting to eliminate unwanted brassy, orange, or yellow tones after hair bleaching.</li>
  <li>Vibrant color enthusiasts seeking bold, artistic {color_en} hair highlights.</li>
  <li>Suitable for all hair types needing a gentle, vegan, high-performance permanent hair dye.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Lakme</td></tr>
  <tr><th>Category</th><td>Hair Care / Professional Hair Color</td></tr>
  <tr><th>Product Type</th><td>Permanent Cream Hair Color Mixtone</td></tr>
  <tr><th>Volume/Weight</th><td>60 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Hair Types (Color Correction & Toning)</td></tr>
  <tr><th>Finish</th><td>Pure {color_en} tone, brass-free, crystal shine</td></tr>
  <tr><th>Texture</th><td>Smooth, easy-to-blend cream</td></tr>
  <tr><th>Fragrance</th><td>Subtle low-odor aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Botanical OF5 Molecule, AQ-Save (Organic Chestnut), Arginine, Soy Protein</td></tr>
  <tr><th>Country of Origin</th><td>Spain</td></tr>
  <tr><th>Manufacturer</th><td>Lakme Cosmetics (Spain)</td></tr>
  <tr><th>Age Group</th><td>Adults (18+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Color Correction & Botanical OF5 Technology</h2>

<h3>What problem does this solve?</h3>
<p>Lakme Collage Mix {shade_code} ({color_en}) resolves unwanted warm undertones (brassy orange or red tones) that emerge during hair lightening, while offering professional colorists the exact tool to customize artistic shades safely.</p>

<h3>Why does this condition happen?</h3>
<p>During hair bleaching, underlying natural warm pigments (melanin remnants) are exposed. Without corrective mixtones formulated according to color wheel principles, final dye results often appear overly brassy or uneven.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Follow Color Wheel Principles:</strong> Use {color_en} mixtone to neutralize opposing unwanted warm shades on the color spectrum.<br>
2. <strong>Precise Gram Measuring:</strong> Add exact gram amounts of mixtone to base color formulas to avoid overpowering final shades.<br>
3. <strong>Use Recommended Developers:</strong> Always mix with dedicated Lakme Collage developers for optimal emulsion.<br>
4. <strong>Color-Safe Haircare:</strong> Wash colored hair with sulfate-free shampoos to maintain tone brilliance.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Mixtones can only be used alone as standalone dyes."<br>
<strong>Fact:</strong> Mixtones are specifically engineered to be blended in precise gram amounts into base dye formulas for custom tone correction.</p>
<p><strong>Myth:</strong> "Professional permanent dyes severely ruin hair texture."<br>
<strong>Fact:</strong> Lakme Collage features a PPD-free, low-ammonia base infused with organic AQ-Save chestnut extract that preserves fiber hydration and softness.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>This formulation utilizes the <strong>Botanical OF5 Molecule</strong>, which exhibits 100% biocompatibility with human hair kerato-proteins. OF5 transports pure corrective nano-pigments into the inner cortex layer. Concurrently, the <strong>AQ-Save Complex</strong> binds moisture molecules within cellular membranes, while <strong>Arginine and Soy Protein</strong> repair broken peptide bonds, locking in neutralized color and restoring cuticle smoothness.</p>"""

    en_faqs = [
        (f"What is Lakme Collage Mix Cream Hair Color {shade_code} ({color_en})?", f"It is a professional Spanish permanent cream hair color mixtone in {color_en} designed to neutralize unwanted undertones or create vibrant artistic hair colors."),
        ("What is the purpose of using a Mixtone dye?", "Mixtones are concentrated corrective shades added to base hair colors to eliminate unwanted warm undertones (like brassy orange or yellow) or customize creative colors."),
        ("Is Lakme Collage Mix vegan and PPD-free?", "Yes, it features a 100% vegan, PPD-free formula produced according to strict European quality standards."),
        ("What is the Botanical OF5 Molecule?", "OF5 is a 100% plant-derived molecule developed by Lakme that improves color penetration, vibrancy, and fiber compatibility."),
        ("How does the AQ-Save Complex benefit colored hair?", "Derived from organic chestnut, AQ-Save locks in moisture within the hair shaft, preventing dryness during the coloring process."),
        ("How do I mix a Mixtone with a base hair color?", "Add calculated gram amounts (typically 2 to 10 grams) of mixtone into your main Collage dye tube and developer mixture."),
        ("Can this mixtone be used alone on hair?", "Yes, it can be applied alone on pre-lightened hair to achieve a vibrant, artistic {color_en} fashion color."),
        ("What is the standard mixing ratio with developer?", "The standard mixing ratio for Lakme Collage dyes is 1 : 1.5 with Lakme Collage developer."),
        ("How long should the hair color process?", "Processing time ranges between 30 to 45 minutes depending on desired tone correction or depth."),
        ("Is the formula low in ammonia?", "Yes, it features a low-ammonia formulation that respects scalp comfort and hair shaft integrity."),
        ("What role do Soy Protein and Arginine play?", "They rebuild damaged hair peptide bonds, restoring elasticity, softness, and crystal-like shine."),
        ("Is Lakme Collage Mix suitable for all hair types?", "Yes, it is suitable for all hair types, particularly bleached or color-treated hair requiring tone correction."),
        ("What volume is contained in one tube?", "Each tube contains 60 ml of professional permanent hair color cream."),
        ("Is a skin patch test required before application?", "Yes, always perform a skin allergy patch test 48 hours prior to coloring."),
        ("Where is Lakme Collage Hair Color manufactured?", "It is proudly manufactured in Spain by Lakme Cosmetics."),
        ("Will this hair dye cause breakage?", "No, AQ-Save and Arginine protect the hair fiber, locking in hydration to prevent post-color brittleness."),
        ("Does it effectively cover gray hair?", "When blended with base shades, it provides 100% full gray coverage."),
        ("Does the dye have a strong chemical smell?", "No, it features a low-ammonia, subtle aroma that is far more pleasant than traditional dyes."),
        ("How do I maintain color vibrancy after dyeing?", "Use sulfate-free, color-protecting shampoos and conditioners designed for color-treated hair."),
        ("Is it safe for keratin or protein-treated hair?", "Yes, its low-ammonia, PPD-free formula preserves keratin and protein hair treatments."),
        ("How do I verify product authenticity at Ekleel Abha?", "All Lakme hair colors at Ekleel Abha are 100% genuine, imported directly from certified Spanish distributors."),
        ("Should hair be freshly washed before coloring?", "It is best applied onto dry, unwashed hair so natural scalp oils provide a protective barrier."),
        ("Can multiple mixtone shades be combined?", "Yes, professional colorists can mix different mixtones together to create custom tones."),
        ("What tools should be used for mixing?", "Use non-metallic plastic or glass bowls and tint brushes to prevent chemical reaction with metallic tools."),
        ("Should gloves be worn during application?", "Yes, always wear protective gloves during mixing and application to prevent hand skin staining.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "العناية بالشعر / صبغات الشعر الاحترافية",
        "brand": "Lakme",
        "ar": {
            "title": f"صبغة كريم كولاجميكس {color_ar} من لاكمي {shade_code} - 60 مل",
            "meta_title": f"صبغة لاكمي كولاج ميكس {color_ar} {shade_code} 60مل | صيدلية إكليل أبها",
            "meta_description": f"اشتري صبغة كريم كولاجميكس الإسبانية النباتية {color_ar} من لاكمي {shade_code} (60مل). مصحح لون احترافي خالي من PPD بمركب OF5. أصلي من إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["لاكمي", "صبغة_لاكمي", "كولاج_ميكس", "مصحح_لون", f"لاكمي_{color_ar}", "إكليل_أبها"]
        },
        "en": {
            "title": f"Lakme Collage Mix Cream Hair Color {shade_code} {color_en}, 60 ml",
            "meta_title": f"Lakme Collage Mix Hair Color {shade_code} {color_en} 60ml | Ekleel Abha",
            "meta_description": f"Buy Lakme Collage Mix Cream Hair Color {shade_code} {color_en} (60ml). Vegan, PPD-free professional tone corrector with OF5 molecule. 100% authentic at Ekleel Abha.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["lakme", "collage_mix", "hair_color", "mixtone", f"lakme_{color_en.lower()}", "ekleel_abha"]
        },
        "schema": {
            "brand": "Lakme",
            "category": "Hair Care / Hair Color",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"lakme-collage-mix-cream-hair-color-{img_slug}-60ml.webp",
            "alt": f"Lakme Collage Mix Cream Hair Color {shade_code} {color_en} 60ml",
            "title": f"Lakme Collage Mix Cream Hair Color {shade_code} {color_en} 60ml"
        }
    }

print("Lakme module ready")
