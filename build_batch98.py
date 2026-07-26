import json, os
from build_batch96 import _make_mufe_foundation_b96

def create_product_2212():
    return _make_mufe_foundation_b96(
        pid=2212, gtin="3548752165358",
        ar_title="كريم أساس ميك أب فور ايفر بني داكن (Y545)30مل",
        en_title="Make Up For Ever Foundation Dark Brown (Y545) 30ml",
        shade_code="Y545", shade_ar="بني داكن (Dark Brown)", shade_en="Dark Brown",
        tags_ar=["ميك_أب_فور_إيفر", "كريم_أساس_ميك_أب_فور_إيفر_Y545", "فاونديشن_بني_داكن", "كريم_أساس_احترافي", "إكليل_أبها"],
        tags_en=["make_up_for_ever", "mufe_foundation_y545", "dark_brown_foundation", "liquid_foundation", "ekleel_abha"]
    )


def _make_nyx_palette_b98(pid, gtin, ar_title, en_title, palette_type_ar, palette_type_en, tags_ar, tags_en):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>تُعد <strong>{ar_title}</strong> باليت مكياج الوجه الاحترافية الأسطورية لنحت وإبراز وتوريد ملامح الوجه من الماركة الأمريكية الشهيرة نيكس (NYX Professional Makeup Palette) المصممة خصيصاً لتمنحك تحكماً كاملاً في تحديد الخدين، نحت الأنف والفك، وتفتيح زوايا الوجه بلمسة بودرية مخملية ثنائية التغطية وسهلة الدمج لـ 24 ساعة. تركز هذه الباليت الأمريكية الأصيلة ({en_title}) على صبغات البودرة المخملية عالية النقاء، فيتامين E المغذي، والبودرة الناعمة المضادة للتكتل.</p>
<p>تعمل باليت المكياج الاحترافية من نيكس على نحت ملامح الوجه بدقة متناهية، تزويد الوجنتين بتورد ناصع وإشراقة طبيعية، ومنح بشرتك لمسة مخملية ناعمة تحافظ على ثبات المكياج ونقائه من اللمسة الأولى.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>نحت وتحديد وتوريد احترافي لملامح الوجه ({palette_type_ar}):</strong> صبغات فائقة النقاء.</li>
  <li><strong>قوام بودري مخملي ينساب ويندمج بسلاسة:</strong> لا يترك تكتلات أو خطوط قاسية.</li>
  <li><strong>ثبات عالي لـ 24 ساعة مقاوم للتلطخ والعرق:</strong> يحافظ على جمال ونضارة الملامح طوال اليوم.</li>
  <li><strong>تغذية وحماية للبشرة بفيتامين E:</strong> يمنع جفاف وجفاف البشرة أثناء المكياج.</li>
  <li><strong>تركيبة خالية من الكرولتي ومختبرة من أطباء الجلدية:</strong> 100% آمنة لجميع أنواع البشرة.</li>
  <li><strong>باليت احترافية أنيقة ومدمجة:</strong> الخيار الأول لخبراء المكياج والاستخدام اليومي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> استخدمي فرشاة الكونتور أو البلاشر المناسبة وأخذ كمية من درجات الباليت.</li>
  <li><strong>الخطوة الثانية:</strong> وزعي درجات النحت تحت عظمتي الخدين وعلى جانبي الأنف، ودرجات التوريد والهايلايت على أعلى الوجنتين.</li>
  <li><strong>الخطوة الثالثة:</strong> ادمجي الألوان برفق بحركات دائرية ناعمة للحصول على مظهر نحت طبيعي متجانس (يُستعمل daily وعند المكياج).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>صبغات البودرة المجهرية وفيتامين E:</strong> تضمن اندماج الألوان بسلاسة وتمنع خشونة الجلد.</li>
  <li><strong>البوليمرات المطرية:</strong> تحفظ طراوة المكياج وتمنع التجمع في المسام.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي التجميلي على بشرة الوجه والخدين.</li>
  <li>تجنبي التلامس المباشر لداخل العين واغلقي الباليت بإحكام.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن {ar_title} لنحت وتوريد ملامح الوجه بباليت احترافية متكاملة.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>نيكس بروفيشنال مكياج (NYX Professional Makeup USA)</td></tr>
  <tr><th>الفئة</th><td>مكياج الوجه / باليتات الكونتور والبلاشر والهايلايت من نيكس</td></tr>
  <tr><th>نوع المنتج</th><td>باليت مكياج احترافية لنحت وتوريد الوجه بفيتامين E ({palette_type_ar})</td></tr>
  <tr><th>الحجم/الوزن</th><td>باليت بودرة متعددة الدرجات</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع بشرة الوجه (العادية، الجافة، الدهنية والمختلطة)</td></tr>
  <tr><th>المظهر النهائي</th><td>وجنتين ناعمتين، ملامح منحوتة بدقة ومظهر مخملي ناصع طوال اليوم</td></tr>
  <tr><th>الملمس</th><td>بودرة ناعمة حريرية تنزلق وتندمج بسلاسة</td></tr>
  <tr><th>العطر</th><td>خالٍ 100% من العطور المهيجة</td></tr>
  <tr><th>المكونات النشطة</th><td>صبغات بودرية فائقة النقاء، فيتامين E المغذي، مركبات النعومة الحريرية</td></tr>
  <tr><th>بلد المنشأ</th><td>الولايات المتحدة الأمريكية (USA) / الصين</td></tr>
  <tr><th>الشركة المصنعة</th><td>NYX Professional Makeup L'Oréal USA</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (من 16 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لفوائد الصبغات المجهرية وفيتامين E في باليت نيكس (NYX Palette {palette_type_ar})</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>تعالج باليت نيكس الاحترافية مشكلة الملامح المسطحة، عدم وضوح عظمتي الخدين، تكتل البلاشر والكونتير، وتلاشي المكياج.</p>

<h3>لماذا تنجح تركيبة NYX Professional Makeup Palette؟</h3>
<p>لأن الصبغات البودرية المجهرية تندمج بانسجام مع كريم الأساس دون أن تترك خطوطاً قاسية أو بقعاً داكنة.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام فرشاة دمج ناعمة:</strong> يضمن توزيع الدرجات وتدرجها الطبيعي.<br>
2. <strong>النفخ الخفيف على الفرشاة لإزالة البودرة الزائدة:</strong> يمنع التلطخ.<br>
3. <strong>إغلاق الباليت بإحكام:</strong> يحافظ على سلامة ونقاء درجات البودرة.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "باليتات الكونتور والهايلايت تجعل الوجه يبدو متصنعاً ومثقلاً بالبودرة."<br>
<strong>الحقيقة:</strong> باليت نيكس مصممة بتركيبة ناعمة حريرية تندمج مع الجلد لتمنح مظهراً منحوتاً طبيعياً كالحرير.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>تخلق الدرجات الفاتحة والداكنة تضاداً ضوئياً ينعكس على الملامح مبرزاً عظمتي الخدين والأنف بنعومة.</p>"""

    faqs_data = [
        (f"ما هي {ar_title}؟", f"هي باليت مكياج احترافية لنحت وتوريد ملامح الوجه بالفيتامين E وصبغات ناعمة من نيكس ({palette_type_ar})."),
        (f"ما هي فوائد الصبغات النضرة وفيتامين E في الباليت؟", "تنحت الملامح، تورد الخدين، تضيء الزوايا، وتغذي البشرة دون تكتل أو جفاف لـ 24 ساعة."),
        ("هل تنحت وتورد الوجه وتثبت لـ 24 ساعة بدون تكتل؟", "نعم، مثبتة سريرياً في نحت الملامح وتوريد الوجه وتوفير ثبات بودري خالي من التكتل."),
        ("ما هي محتويات العبوة؟", "تأتي بباليت أنيقة احترافية متعددة درجات النحت والإضاءة."),
        ("كيف يُستخدم بالشكل الصحيح؟", "خذي كمية بالفرشاة، وزعي الدرجات الداكنة للنحت على الخدين والأنف، والدرجات الفاتحة والتوريد أعلى الوجنتين وادمجيهم."),
        ("هل هي خالية من العطور وآمنة للبشرة؟", "نعم، 100% خالية من العطور ومختبرة جلدياً وآمنة لجميع أنواع البشرة."),
        ("أين صُنعت باليت نيكس؟", "صُنت بواسطة NYX Professional Makeup L'Oréal USA."),
        ("كيف أتأكد من أصالته لدى إكليل أبها؟", "جميع منتجات نيكس لدى إكليل أبها أصلية 100%."),
        (f"ما هو نوع باليت نيكس؟", f"باليت احترافية ({palette_type_ar})."),
        ("هل تناسب جميع أنواع البشرة والمكياج؟", "نعم، ممتازة لجميع أنواع البشرة والنحت اليومي والاحترافي."),
        ("هل الباليت مريحة وموفرة بالشنطة؟", "نعم، باليت مدمجة أنيقة ومريحة بالحقيبة ولأخصائيي المكياج."),
        ("كيف أحتفظ بالعبوة؟", "في مكان بارد وجاف."),
        ("هل نيكس الماركة الأمريكية الأولى في الكونتور والتوريد؟", "نعم، NYX Professional Makeup الماركة الأمريكية رقم 1 الأكثر شهرة بتحديد ونحت الوجه."),
        ("كم يدوم ثباتها طوال اليوم؟", "تدوم لـ 24 ساعة متواصلة دون تلطخ أو تلاشي."),
        ("هل ينشطف بمزيل المكياج بسهولة؟", "نعم، ينشطف بسلاسة بمزيل المكياج دون شد البشرة."),
        ("هل العبوة قابلة لإعادة التدوير؟", "نعم."),
        ("هل تنزلق وتندمج دون ترك خطوط قاسية؟", "نعم، قوام بودري حريري ينزلق ويندمج بمرونة كاملة."),
        ("هل يتوفر بسعر ممتاز لدى إكليل أبها؟", "نعم، يتوفر بقيمة ممتازة لدى صيدلية إكليل أبها."),
        ("هل يناسب النساء والفتيات؟", "نعم، ممتاز للنساء والفتيات."),
        ("هل يناسب المناسبات والمكياج اليومي؟", "نعم، ممتاز للمكياج اليومي والمناسبات والتصوير."),
        ("هل يصلح هدية ممتازة ضمن مكياج الوجه؟", "نعم، منتج مكياج أمريكي فاخر وأساسي لكل امرأة راقية."),
        (f"هل يعيد المظهر المنحوت الناعم للوجنتين؟", f"نعم، يمنح الوجه مظهراً منحوتاً ومورداً بجمال ناصع."),
        ("هل تتوفر باليتات نيكس الأخرى؟", "نعم، تتوفر عائلة NYX Contour & Blush Palettes كاملة لدى إكليل أبها."),
        ("هل هي خالية من الكرولتي ولم تُجرب على الحيوانات؟", "نعم، نيكس علامة معتمدة خالية من التجريب على الحيوانات (Cruelty-Free)."),
        ("هل يتوفر المنتج الأصلي دائماً لدى إكليل أبها؟", "نعم، يتوفر المنتج الأصلي 100% دائماً لدى صيدلية إكليل أبها.")
    ]
    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs_data])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>{en_title}</strong> is an authentic luxury professional face contouring, highlighting, and blush palette from iconic US brand NYX Professional Makeup (NYX Professional Makeup Palette) designed to give you complete sculpting control over cheeks, nose, and jawlines with silky, blendable powder formulas for 24 hours. Built upon ultra-pure micro-powders, nourishing Vitamin E, and a non-caking texture.</p>
<p>NYX Professional Face Palette sculpts facial contours precisely, infuses cheeks with a healthy flush and glow, and provides a silky velvet finish that locks makeup in place from first sweep.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Professional Sculpting, Highlighting & Blush ({palette_type_en}):</strong> Ultra-pure rich pigments.</li>
  <li><strong>Silky Smooth Powder Texture Blends Seamlessly:</strong> Leaves no harsh lines or chalky patches.</li>
  <li><strong>24-Hour Long-Wear Smudge-Proof Hold:</strong> Preserves defined facial features all day long.</li>
  <li><strong>Vitamin E Skin Nourishment & Protection:</strong> Prevents skin dryness during makeup wear.</li>
  <li><strong>Cruelty-Free & Dermatologically Tested Formula:</strong> 100% safe for all skin types.</li>
  <li><strong>Sleek Compact Professional Palette:</strong> The #1 choice for makeup artists and daily users.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Swirl a contour, blush, or highlight brush into desired shade pan.</li>
  <li><strong>Step 2:</strong> Sweep contour shades below cheekbones and jawlines, and blush/highlighter onto tops of cheekbones.</li>
  <li><strong>Step 3:</strong> Blend gently in circular motions for a seamless natural sculpted finish (use daily with makeup).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Micro-Powder Pigments & Vitamin E:</strong> Ensure smooth color blending and protect skin texture.</li>
  <li><strong>Emollient Polymers:</strong> Preserve makeup freshness preventing settlement into pores.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external cosmetic application on facial and cheek skin.</li>
  <li>Avoid direct contact inside eyes and keep palette closed tightly.</li>
  <li>Keep out of reach of children and store in a cool, dry place.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking {en_title} for complete professional facial sculpting, highlighting, and cheek flushing.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>NYX Professional Makeup (USA)</td></tr>
  <tr><th>Category</th><td>Face Makeup / NYX Contour, Blush & Highlight Palettes</td></tr>
  <tr><th>Product Type</th><td>Professional Multi-Shade Face Sculpting & Blush Powder Palette ({palette_type_en})</td></tr>
  <tr><th>Volume/Weight</th><td>Multi-Shade Powder Palette</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Facial Skin Types (Normal, Dry, Oily & Combination Skin)</td></tr>
  <tr><th>Finish</th><td>Silky soft, 24H hydrated, sculpted & flushed face finish</td></tr>
  <tr><th>Texture</th><td>Rich smooth non-chalky silky powder gliding easily</td></tr>
  <tr><th>Fragrance</th><td>100% Fragrance-free (irritant-free)</td></tr>
  <tr><th>Active Ingredients</th><td>Micro-Powder Pigments, Vitamin E, Silky Binding Agents</td></tr>
  <tr><th>Country of Origin</th><td>USA / China</td></tr>
  <tr><th>Manufacturer</th><td>NYX Professional Makeup L'Oréal USA</td></tr>
  <tr><th>Age Group</th><td>Teens & Adults (Ages 16+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The Science of Micro-Powder Light Shadowing & Vitamin E Skin Protection</h2>

<h3>What problem does this solve?</h3>
<p>{en_title} resolves flat facial features, un-defined cheekbones, chalky contour patches, and makeup fading.</p>

<h3>Why choose NYX Professional Makeup Palette?</h3>
<p>Micro-powder pigments layer smoothly over foundation creating subtle optical shadows and light highlights without harsh edges.</p>"""

    en_faqs_data = [
        (f"What is {en_title}?", f"It is a professional face sculpting, blush, and highlighting palette with Vitamin E from NYX Professional Makeup ({palette_type_en})."),
        (f"What are the benefits of pure pigments and Vitamin E in this palette?", "Sculpt facial features, flush cheeks, highlight contours, and nourish skin for 24 hours without chalkiness."),
        ("Does it sculpt features and hold for 24 hours without caking?", "Yes, clinically proven to sculpt facial features and hold for 24 hours without caking."),
        ("What items are included in this palette?", "Sleek professional palette with multi-shade pans."),
        ("How do I use it correctly?", "Dip brush into shade, sweep contour below cheekbones/jawline, apply blush to apples of cheeks, and blend."),
        ("Is it cruelty-free and dermatologically safe?", "Yes, 100% cruelty-free, dermatologically tested, and safe for all skin types."),
        ("Where is NYX Palette manufactured?", "By NYX Professional Makeup L'Oréal USA."),
        ("How do I verify authenticity at Ekleel Abha?", "All NYX products at Ekleel Abha are 100% original."),
        (f"What type of NYX palette is this?", f"Professional face palette ({palette_type_en})."),
        ("Is it suitable for dry, oily, and combination skin?", "Yes, excellent for all skin types and daily or MUA sculpting."),
        ("Is the compact palette travel friendly?", "Yes, sleek compact palette ideal for makeup kits, handbags, and travel."),
        ("How should I store it?", "In a cool, dry place."),
        ("Is NYX a #1 US professional makeup brand?", "Yes, NYX Professional Makeup is a premier US brand in contouring and face palettes."),
        ("How long does it hold during the day?", "Holds for 24 continuous hours without smudging or fading."),
        ("Does it remove easily with makeup remover?", "Yes, removes smoothly with face makeup remover without tugging skin."),
        ("Is the palette recyclable?", "Yes."),
        ("Does it blend without leaving harsh lines?", "Yes, silky powder texture glides and blends effortlessly."),
        ("Is it available at a great price at Ekleel Abha?", "Yes, exceptional value at Ekleel Abha Pharmacy."),
        ("Is it suitable for women and teens?", "Yes, suitable for both women and teens."),
        ("Is it good for photoshoots and daily wear?", "Yes, ideal for daily makeup, photoshoots, and special events."),
        ("Is it a nice makeup gift?", "Yes, an essential premier US professional makeup gift."),
        (f"Does it restore beautifully sculpted cheeks in {palette_type_en}?", "Yes, gives facial features a defined contoured radiant look."),
        ("Are other NYX palettes available?", "Yes, the full NYX palette range is available at Ekleel Abha."),
        ("Is it 100% cruelty-free?", "Yes, NYX is PETA certified 100% cruelty-free."),
        ("Is the authentic product always available at Ekleel Abha?", "Yes, 100% authentic product is always available at Ekleel Abha Pharmacy.")
    ]
    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs_data])

    return {
        "product_id": str(pid),
        "sku": f"EK-{pid}",
        "gtin": gtin,
        "brand": "NYX",
        "ar": {
            "title": ar_title,
            "meta_title": f"{ar_title} | إكليل أبها",
            "meta_description": f"اشتري {ar_title}. باليت كونتور وتوريد احترافية أمريكية بنعومة مخملية وثبات 24 ساعة. أصلي لدى صيدلية إكليل أبها.",
            "description": ar_desc, "specifications": ar_specs, "knowledge_base": ar_kb, "faqs": ar_faqs_html,
            "tags": tags_ar
        },
        "en": {
            "title": en_title,
            "meta_title": f"{en_title} | Ekleel Abha",
            "meta_description": f"Buy original {en_title}. US professional 24-hour long-wear face contour, blush & highlight palette. 100% authentic at Ekleel Abha.",
            "description": en_desc, "specifications": en_specs, "knowledge_base": en_kb, "faqs": en_faqs_html,
            "tags": tags_en
        }
    }


def create_product_2213():
    return _make_nyx_palette_b98(
        pid=2213, gtin="800897056247",
        ar_title="بالته احمر خدود بروفيشنال ميك اب سويت من نيكس",
        en_title="NYX Professional Makeup Sweet Blush",
        palette_type_ar="باليت احمر خدود سويت", palette_type_en="Sweet Blush Palette",
        tags_ar=["نيكس", "بلاشر_نيكس_سويت", "احمر_خدود_نيكس", "باليت_مكياج_نيكس", "إكليل_أبها"],
        tags_en=["nyx", "nyx_sweet_blush", "nyx_blush_palette", "nyx_makeup", "ekleel_abha"]
    )


def create_product_2214():
    return _make_nyx_palette_b98(
        pid=2214, gtin="800897846879",
        ar_title="كونتور متعددة الالوان داكن  من نكس  2.2غرام",
        en_title="NYX Multi-Color Dark Contour - 2.2g",
        palette_type_ar="كونتور متعدد الألوان داكن 2.2g", palette_type_en="Multi-Color Dark Contour 2.2g",
        tags_ar=["نيكس", "كونتور_نيكس_داكن", "كونتور_متعدد_الألوان", "نحت_الوجه_نيكس", "إكليل_أبها"],
        tags_en=["nyx", "nyx_dark_contour", "nyx_contour_palette", "nyx_makeup", "ekleel_abha"]
    )


def create_product_2215():
    return _make_nyx_palette_b98(
        pid=2215, gtin="800897846855",
        ar_title="كونتور متعددة الالوان فاتح من نكس  2.2غرام",
        en_title="NYX Multi-Color Contour Palette - Light, 2.2g",
        palette_type_ar="كونتور متعدد الألوان فاتح 2.2g", palette_type_en="Multi-Color Light Contour 2.2g",
        tags_ar=["نيكس", "كونتور_نيكس_فاتح", "كونتور_متعدد_الألوان", "نحت_الوجه_نيكس", "إكليل_أبها"],
        tags_en=["nyx", "nyx_light_contour", "nyx_contour_palette", "nyx_makeup", "ekleel_abha"]
    )


def create_product_2216():
    return _make_nyx_palette_b98(
        pid=2216, gtin="800897836245",
        ar_title="مجموعة تحديد الوجه هايلايت وكونتور برو - من نيكس",
        en_title="NYX Highlight & Contour Pro Palette",
        palette_type_ar="باليت هايلايت وكونتور برو الاحترافية", palette_type_en="Highlight & Contour Pro Palette",
        tags_ar=["نيكس", "كونتور_نيكس_برو", "هايلايت_وكونتور_نيكس", "باليت_نحت_الوجه", "إكليل_أبها"],
        tags_en=["nyx", "nyx_highlight_contour_pro", "nyx_pro_palette", "nyx_makeup", "ekleel_abha"]
    )


print("Loaded all 5 Batch 98 builders complete")
