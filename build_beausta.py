import json, os

def build_beausta_product(prod_id, color_en, color_ar, shade_code, gtin, img_slug):
    ar_desc = f"""<h2>نظرة عامة على المنتج</h2>
<p>يُعتبر <strong>ملمع وملون الشفاه اللامع بيوستا (Beausta Shine Gloss Lip Tint - {color_ar} 4ml)</strong> ابتكاراً كورية رائعاً يجمع بين اللمعان الساطع للملمع (Gloss) والثبات الطويل لملون الشفاه (Tint) في منتج واحد أنيق وسهل الحمل. يمنح هذا التينت شفتيكِ لونا زاهياً جذابا بدرجة {color_ar} مفعمة بالحيوية مع مظهر زجاجي لامع دون أي ملمس لزج ثقيل.</p>
<p>يأتي المنتج بتغليف كيس كوري ذكي وصغير الحجم مزود بصمام محكم يسهل حمله في حقيبة اليد أو الجيب أثناء التنقل والسفر. تتميز فرمولته برطوبة فائقة تحمي الشفاه من الجفاف والتشقق، بفضل احتوائها على مركب ترطيبي غني بالزيوت المغذية والمكونات الكورية المتقدمة التي تثبت اللون وتمنح حواف الشفاه مظهراً ممتلئاً وجذاباً.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تأثير مزدوج 2 في 1:</strong> يدمج بين لون التينت الثابت واللمعان الزجاجي المشرق للملمع في تطبيق واحد.</li>
  <li><strong>درجة لون {color_ar} مميزة:</strong> يمنح الشفاه لوناً غنياً ومشرقاً يبرز جمال الابتسامة ويعزز نضارة الوجه.</li>
  <li><strong>ترطيب عميق وحماية من التشقق:</strong> يغذي الشفاه وينعم خطوطها بفضل مركب المرطبات الذي يمنع الجفاف.</li>
  <li><strong>تغليف كوري ذكي ومحمول:</strong> عبوة كيس خفيفة بحجم 4 مل مزودة بإغلاق محكم مثالية للسفر والتنقل اليومي.</li>
  <li><strong>ثبات طويل دون لزوجة:</strong> يثبت اللون على الشفاه لساعات طويلة دون ترك ملمس ثقيل أو لزج مزعج.</li>
  <li><strong>تطبيق سهل ودقيق:</strong> مزود بأداة تطبيق ناعمة توزع اللون واللمعان بالتساوي من المرة الأولى.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (تحضير الشفاه):</strong> تأكدي من نظافة وجفاف الشفاه (يمكن تقشيرها خفيفاً للحصول على أفضل نتيجة).</li>
  <li><strong>الخطوة الثانية (التطبيق من المنتصف):</strong> ضعي كمية مناسبة من التينت باستخدام الفرشاة المدمجة بدءاً من منتصف الشفة السفلى والعليا.</li>
  <li><strong>الخطوة الثالثة (التوزيع):</strong> وزعي التينت بلطف نحو الزوايا الخارجية للحصول على تغطية متجانسة أو مظهر شفاه متدرج (Gradation Lip).</li>
  <li><strong>الخطوة الرابعة (الانتظار للتثبيت):</strong> اتركي التينت لعدة ثوانٍ ليتثبت اللون وتظهر اللمعة الزجاجية الفائقة.</li>
  <li><strong>الخطوة الخامسة (إعادة التطبيق):</strong> يمكن إضافة طبقة ثانية إذا كنت ترغبين في زيادة كثافة اللون واللمعان.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>أوكتيلدوديكانول (Octyldodecanol):</strong> مرطب دهني يمنح الشفاه ملمساً ناعماً ويساعد على توزيع الصبغات بشكل متساوٍ.</li>
  <li><strong>البوتيلين جلايكول (Butylene Glycol):</strong> مرطب يجذب جزيئات الماء ليحافظ على ليونة الشفاه ورطوبتها.</li>
  <li><strong>مركبات الدايميثيكون (Dimethicone):</strong> تمنح الطبقة اللامعة الحماية وتغلف الشفاه بطبقة زجاجية ناعمة.</li>
  <li><strong>ايثيل سيليولوز (Ethylcellulose):</strong> يساعد على تثبيت اللون واللمعان طوال اليوم دون تكتل.</li>
  <li><strong>صبغات كورية عالية النقاء:</strong> تمنح درجة لون {color_ar} ثباتاً وإشراقاً دون التسبب في تصبغ ضار.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي على الشفاه فقط.</li>
  <li>تجنبي تخزين المنتج في أماكن ذات درجات حرارة عالية جداً أو تحت أشعة الشمس المباشرة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وأغلقي السدادة جيداً بعد كل استخدام.</li>
  <li>توقفي عن الاستخدام في حال ظهور أعراض حساسية أو احمرار غير طبيعي على حواف الشفاه.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لكل امرأة تبحث عن ملمع شفاه كوري بلون {color_ar} ثابت ولمعة زجاجية جذابة.</li>
  <li>لمن يفضلن المستحضرات العملية خفيفة الوزن ذات التغليف المحمول المناسب للسفر.</li>
  <li>لصاحبات الشفاه الجافة الراغبات في لون مشرق دون التضحية بالترطيب.</li>
  <li>مناسب لجميع الفئات العمرية ومثالي للاستخدام اليومي أو المناسبات.</li>
</ul>"""

    ar_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>بيوستا (Beausta)</td></tr>
  <tr><th>الفئة</th><td>المكياج / ملون وملمع الشفاه</td></tr>
  <tr><th>نوع المنتج</th><td>ملون وملمع شفاه لامع (Shine Gloss Lip Tint)</td></tr>
  <tr><th>الحجم/الوزن</th><td>4 مل (عبوة كيس مدمجة)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (الشفاه)</td></tr>
  <tr><th>المظهر النهائي</th><td>لمعة زجاجية ولون {color_ar} زاهي وثابت</td></tr>
  <tr><th>الملمس</th><td>سائل سلكي خفيف غير لزج</td></tr>
  <tr><th>العطر</th><td>رائحة فواكه خفيفة ومنعشة</td></tr>
  <tr><th>المكونات النشطة</th><td>أوكتيلدوديكانول، بوتيلين جلايكول، دايميثيكون، صبغيات ناعمة</td></tr>
  <tr><th>بلد المنشأ</th><td>كوريا الجنوبية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beausta International</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (ابتداءً من 13 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = f"""<h2>الدليل المعرفي لتقنية تينت الشفاه الكوري واللمعان الزجاجي (Beausta Gloss)</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج ملمع وتينت بيوستا الكوري مشكلة الجفاف والتشقق الذي تسببه أحمر الشفاه المات التقليدية، وفي نفس الوقت يحل مشكلة زوال ملمعات الشفاه (Gloss) العادية بسرعة وتلطخها.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>أحمر الشفاه الماث يحتوي على نسبة عالية من البودرة والصبغات الجافة التي تمتص الرطوبة من الشفاه وتبرز الخطوط الدقيقة. بينما ملمعات الشفاه العادية تتكون من زيوت ثقيلة لا تلتصق بالجلد فتزول فور شرب الماء أو تناول الطعام.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>التقشير الخفيف:</strong> قشري شفاهكِ مرة أسبوعياً بإسفنجة ناعمة لإزالة الخلايا الميتة.<br>
2. <strong>الترطيب قبل المكياج:</strong> ضعي بلسم شفاه خفيف قبل وضع التينت لدعم مرونة الجلد.<br>
3. <strong>التطبيق التدريجي:</strong> ضعي التينت في مركز الشفاه ودمجيه للخارج لمظهر شفاه كوري ناعم الطبيعي.<br>
4. <strong>عدم فرك الشفاه بقوة:</strong> اتركي التينت لثوانٍ على الشفاه ليتشكل غشاء اللمعان الزجاجي دون فرك.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "التينت الكوري يسبب تصبغاً دائماً للشفاه."<br>
<strong>الحقيقة:</strong> صبغات تينت بيوستا كورية آمنة معتمدة تتغلغل خفيفاً في الطبقة السطحية وتزول بسهولة مع مزيل المكياج دون تصبغ دائم.</p>
<p><strong>خرافة:</strong> "تغليف الأكياس الأصغر يقلل من جودة المنتج."<br>
<strong>الحقيقة:</strong> تغليف الأكياس الذكي من بيوستا يقلل من تكلفة التعبئة البلاستيكية الثقيلة مما يتيح تقديم تركيبة فاخرة بسعر ممتازا جداً مع حفظ المستحضر من التلوث.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعتمد المنتج على تقنية ثنائية الطبقات (Dual-Layer Phase Technology). تتكون الطبقة السفلى من صبغات التينت المائية التي تمتصها الأنسجة السطحية للشفاه لمنح لون ثابت يدوم ساعات. بينما تطفو الطبقة العلوية المكونة من بوليمرات الدايميثيكون وأوكتيلدوديكانول لتعكس الضوء وتمنح المظهر الزجاجي الفائق وترطب الشفاه وتمنع تبخر الماء.</p>"""

    faqs = [
        (f"ما هو تينت وملمع الشفاه بيوستا بدرجة {color_ar}؟", f"هو مستحضر تجميل كوري مدمج يجمع بين لون التينت الثابت واللمعان الزجاجي المشرق بدرجة {color_ar} في عبوة كيس عملي بحجم 4 مل."),
        ("هل يترك ملمع بيوستا شعوراً لزجاً على الشفاه؟", "لا، تم تطوير فرمولته خصيصاً لتمنح لمعاناً زجاجياً بلمس سلكي خفيف دون أي لزوجة مزعجة."),
        ("كم تدوم ثباتية اللون على الشفاه؟", "يتميز التينت بثباتية عالية تدوم لعدة ساعات حتى بعد زوال طبقة اللمعان السطحية بفعل تناول الطعام أو الشراب."),
        ("ما ميزة عبوة الكيس (Pouch) المبتكرة من بيوستا؟", "عبوة الكيس خفيفة الوزن، صلبة وغير قابلة للكسر، مزودة بصمام إغلاق محكم يمنع التسرب، وتتيح استخدام المستحضر حتى آخر قطرة بسهولة في الحقيبة."),
        ("هل يناسب هذا التينت الشفاه الجافة؟", "نعم، هو ممتاز جداً للشفاه الجافة لأنه يحتوي على مرطبات متقدمة مثل البوتيلين جلايكول والأوكتيلدوديكانول لترطيب الشفاه وينعم خطوطها."),
        ("كيف يمكن الحصول على مظهر الشفاه المتدرجة (Gradation Lips) الكورية؟", "ضعي نقطتين من التينت في مركز الشفة الداخلية فقط، ثم اندمجيه بأطراف أصابعك نحو الخارج لخلق مظهر كوري ناعم وطبيعي."),
        ("هل يمكن وضع طبقات متعددة لزيادة كثافة اللون؟", "نعم، يمكنكِ تطبيق طبقة واحدة للون طبيعي خفيف، أو وضع طبقتين للحصول على لون غني ولمعان زجاجي مضاعف."),
        ("هل المنتج أصلي ومصنوع في كوريا؟", "نعم، جميع منتجات بيوستا مصممة ومصنوعة 100% في كوريا الجنوبية وفق أعلى معايير الجودة العالمية."),
        ("هل يحتوي التينت على عطر؟", "يتميز بنكهة ورائحة فواكه ناعمة خفيفة جداً تمنح شعوراً بالإنتعاش فور التطبيق."),
        ("هل يناسب التينت جميع درجات ألوان البشرة؟", f"نعم، درجة لون {color_ar} صُممت لتناسب مختلف درجات البشرة من الفاتحة إلى الحنطية والداكنة."),
        ("كم مرة يمكن استخدام العبوة بحجم 4 مل؟", "على الرغم من حجمها الصغير، إلا أن كمية بسيطة جداً تكفي للتطبيق، وبالتالي تكفي العبوة لأسابيع من الاستخدام اليومي."),
        ("كيف يمكن إزالة التينت في نهاية اليوم؟", "يُزال بسهولة باستخدام مزيل مكياج الشفاه والعيون، أو ماء الميسيلار، أو زيت التنظيف."),
        ("هل المنتج آمن للاستخدام للمراهقات؟", "نعم، تركيبته لطيفة وآمنة وتناسب المراهقات والبالغات ابتداءً من سن 13 سنة."),
        ("هل يسبب التينت اسمرار الشفاه؟", "لا، مكوناته خالية من المواد الضارة والتصبعات الكيميائية القاسية وهو آمن تماماً للشفاه."),
        ("هل يمكن استخدام التينت كبلاش (أحمر خدود)؟", "نعم، تدميج قطرة صغيرة على الخدود يمنح الخدين إشراقة وردية ورطوبة طبيعية مذهلة."),
        ("ما هي الدرجات الأخرى المتاحة من تينت بيوستا؟", "يتوفر بيوستا بدرجات رائعة متعددة مثل البنفسجي، الأحمـر، والبرتقالي الخوخي لتناسب كافة أذواق المكياج."),
        ("هل يمكن وضع بلسم شفاه قبل التينت؟", "يمكن وضع بلسم الشفاه، ولكن يُفضل مسحه خفيفاً قبل تطبيق التينت لضمان التصاق الصبغة المائية بالشفاه بفعالية."),
        ("هل العبوة قابلة لإعادة الإغلاق بإحكام؟", "نعم، تحتوي على غطاء لولبي محكم يضمن عدم تسرب أي نقطة داخل الحقيبة."),
        ("هل المنتج نباتي وخالي من القسوة؟", "نعم، بيوستا تلتزم بمعايير عدم تجربة المنتجات على الحيوانات (Cruelty-Free)."),
        ("ما الذي يجعل بيوستا مميزة عن الماركات الكورية الأخرى؟", "تميزت بيوستا بابتكار مفهوم أكياس المكياج المحمولة عالية الجودة بأسعار اقتصادية وعملية جداً."),
        ("هل يتأثر المنتج بالحرارة في الصيف؟", "يُفضل حفظه في مكان بارد وتجنب تركه داخل السيارة تحت الشمس المباشرة للحفاظ على قوام السيروم."),
        ("هل يبرز التينت تشققات الشفاه؟", "على العكس، تركيبته المرطبة واللمعة الزجاجية تموه الخطوط والتجاعيد وتمنح الشفاه مظهر ممتلئ ومشدود."),
        ("كيف أتأكد أن المنتج أصلي من إكليل أبها؟", "جميع منتجات بيوستا لدى صيدلية إكليل أبها أصلية 100% ومستوردة من الوكلاء المعتمدين بالمملكة العربية السعودية."),
        ("هل يناسب المكياج اليومي الخفيف (No-Makeup Look)؟", "نعم، هو الخيار الأفضل لمكياج النهار والمدرسة والعمل لأنه يمنح حيوية ونضارة طبيعية للوجه دون مبالغة."),
        ("هل يمكن استخدام ملمع شفاف فوق التينت؟", "التينت يحتوي بالفعل على ملمع زجاجي غني، ولكن يمكن إضافة ملمع شفاف إضافي إذا رغبتِ في زيادة كثافة اللمعة.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = f"""<h2>Product Overview</h2>
<p>The <strong>Beausta Shine Gloss Lip Tint ({color_en} 4ml)</strong> is an innovative K-beauty lip cosmetic that expertly combines the high-shine luminosity of a lip gloss with the long-lasting color stain of a lip tint. Designed in a compact, travel-friendly pouch, this product coats your lips in a vivid {color_en} hue with a glass-like finish, without any sticky or heavy sensation.</p>
<p>Featuring Beausta's signature eco-conscious spout pouch packaging, this lip tint easily slips into your pocket or purse for effortless touch-ups on the go. Its formula is enriched with lightweight hydrating agents that lock in moisture, smooth fine lip lines, and prevent chapping, leaving your lips looking plump, radiant, and naturally defined.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>2-in-1 Dual Function:</strong> Combines vivid tint pigmentation with a sparkling glass-gloss finish in one easy application.</li>
  <li><strong>Vibrant {color_en} Shade:</strong> Enhances natural lip color with an invigorating, radiant hue suitable for any makeup look.</li>
  <li><strong>Intensive Moisture & Protection:</strong> Keeps lips hydrated and smooth, preventing dryness and chapping throughout the day.</li>
  <li><strong>Compact Spout Pouch Packaging:</strong> Lightweight 4ml pouch with a tight screw cap, perfect for travel and quick touch-ups.</li>
  <li><strong>Long-Wear Non-Sticky Formula:</strong> Stains the lips for hours without feeling tacky or heavy.</li>
  <li><strong>Precise Soft Applicator:</strong> Built-in wand enables smooth, even, and controlled application from the first stroke.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Prep Lips):</strong> Ensure lips are clean and dry (gently exfoliate beforehand for the smoothest finish).</li>
  <li><strong>Step 2 (Apply Center):</strong> Using the built-in wand applicator, apply a small amount onto the center of upper and lower lips.</li>
  <li><strong>Step 3 (Blend Outwards):</strong> Gently blend outward toward the corners for full coverage or create a Korean gradient lip effect.</li>
  <li><strong>Step 4 (Allow Setting):</strong> Wait a few seconds for the tint to stain the lips and reveal its glass-shine barrier.</li>
  <li><strong>Step 5 (Layer for Intensity):</strong> Reapply a second layer if a deeper color intensity and higher shine are desired.</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Octyldodecanol:</strong> Emollient conditioning agent providing a silky smooth feel and uniform pigment dispersion.</li>
  <li><strong>Butylene Glycol:</strong> Effective humectant that draws water into the lips to maintain hydration and elasticity.</li>
  <li><strong>Dimethicone Polymers:</strong> Create a protective glass-like sheen over the lips while locking in moisture.</li>
  <li><strong>Ethylcellulose:</strong> Helps fix color pigments and gloss reflection for extended wear without clumping.</li>
  <li><strong>Purified Korean Pigments:</strong> Deliver vivid, clear {color_en} color without causing harmful staining.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external application on lips only.</li>
  <li>Avoid storing in high temperatures or under direct, prolonged sunlight.</li>
  <li>Keep out of reach of children and seal the cap tightly after every use.</li>
  <li>Discontinue use if signs of irritation, excessive redness, or discomfort develop.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Anyone seeking a Korean {color_en} lip tint featuring long-lasting stain and a glassy high-shine finish.</li>
  <li>People looking for ultra-portable, travel-friendly lip makeup for effortless touch-ups.</li>
  <li>Those with dry lips who want vivid color without sacrificing hydration and softness.</li>
  <li>Suitable for all ages and skin tones, perfect for daily wear or evening outings.</li>
</ul>"""

    en_specs = f"""<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Beausta</td></tr>
  <tr><th>Category</th><td>Makeup / Lip Gloss & Tint</td></tr>
  <tr><th>Product Type</th><td>Shine Gloss Lip Tint</td></tr>
  <tr><th>Volume/Weight</th><td>4 ml (Compact Pouch)</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Lips)</td></tr>
  <tr><th>Finish</th><td>Glassy Shine with Vibrant {color_en} Stain</td></tr>
  <tr><th>Texture</th><td>Lightweight Non-sticky Silky Fluid</td></tr>
  <tr><th>Fragrance</th><td>Subtle fresh fruity scent</td></tr>
  <tr><th>Active Ingredients</th><td>Octyldodecanol, Butylene Glycol, Dimethicone, Purified Pigments</td></tr>
  <tr><th>Country of Origin</th><td>South Korea</td></tr>
  <tr><th>Manufacturer</th><td>Beausta International</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens (13+)</td></tr>
</tbody>
</table>"""

    en_kb = f"""<h2>The K-Beauty Science of Glassy Lip Tints & Moisture Phase Technology</h2>

<h3>What problem does this solve?</h3>
<p>Beausta Shine Gloss Lip Tint solves the drying, cracking issues associated with traditional matte lipsticks, while eliminating the sticky, short-lived nature of conventional lip glosses.</p>

<h3>Why does this condition happen?</h3>
<p>Matte lipsticks contain high ratios of dry powders and heavy pigments that absorb moisture from sensitive lip tissue. Conversely, standard glosses consist of heavy viscous oils that slide off easily during eating or drinking, offering no lasting color stain.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Gentle Exfoliation:</strong> Exfoliate lips weekly with a damp cloth to remove dead skin cells.<br>
2. <strong>Light Hydration:</strong> Apply a sheer lip balm prior to tinting for optimum smoothness.<br>
3. <strong>Gradient Technique:</strong> Apply tint to the inner lip center and blend outward for a natural Korean gradient.<br>
4. <strong>Allow Setting:</strong> Let the product set untouched for 30 seconds to allow the glass-shine layer to form fully.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Korean lip tints cause permanent dark lip discoloration."<br>
<strong>Fact:</strong> Beausta uses safety-tested, approved Korean cosmetic dyes that stain only the superficial epidermal layer, removing easily with standard makeup removers.</p>
<p><strong>Myth:</strong> "Pouch cosmetics packaging means lower formula quality."<br>
<strong>Fact:</strong> Beausta's innovative pouch format reduces heavy plastic packaging costs, allowing premium K-beauty formulas to be delivered at an accessible price point while protecting ingredients from contamination.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>This formula employs Dual-Layer Phase Technology. Upon application, the water-based tint phase absorbs into the lip surface cells to anchor long-lasting pigment. Simultaneously, the hydrophobic phase featuring Octyldodecanol and Dimethicone rises to the surface, creating an optical light-reflecting glass barrier that locks in moisture and prevents transepidermal water loss.</p>"""

    en_faqs = [
        (f"What is Beausta Shine Gloss Lip Tint in {color_en}?", f"It is a Korean 2-in-1 lip cosmetic offering long-wearing tint stain combined with a glassy high-shine finish in a vibrant {color_en} shade."),
        ("Does this lip gloss feel sticky on the lips?", "No, it is specifically formulated to provide a high-shine glass finish with a lightweight, silky feel free from tackiness."),
        ("How long does the lip stain last?", "The tint stain lasts for several hours on the lips, retaining its color even after the surface shine wears off during drinking or eating."),
        ("What are the benefits of Beausta's pouch packaging?", "The pouch packaging is lightweight, unbreakable, leak-proof, and portable, allowing easy touch-ups on the go while utilizing every drop."),
        ("Is this lip tint suitable for dry lips?", "Yes, it contains hydrating humectants such as Butylene Glycol and Octyldodecanol to soothe lines and prevent lip chapping."),
        ("How do I achieve a Korean gradient lip look?", "Apply a small dab of tint to the inner center of your lips and blend outward using fingertips for a soft, flushed effect."),
        ("Can I build up the color intensity?", "Yes, apply one sheer layer for a natural stain, or layer a second coat for richer color intensity and higher shine."),
        ("Is Beausta made in South Korea?", "Yes, all Beausta products are 100% designed and manufactured in South Korea under strict cosmetic standards."),
        ("Does the lip tint have a fragrance?", "It features a subtle, pleasing fruity aroma that adds a fresh touch upon application."),
        ("Does this {color_en} shade suit all skin tones?", f"Yes, the {color_en} shade is universally flattering across fair, medium, and deeper complexions."),
        ("How long does a 4ml pouch last?", "Because only a small amount is required per use, one 4ml pouch provides weeks of daily application."),
        ("How do I remove the tint at night?", "It removes easily using a dual-phase lip and eye makeup remover, micellar water, or cleansing oil."),
        ("Is it suitable for teenagers?", "Yes, its gentle, safe formula is suitable for teens and adults aged 13 and above."),
        ("Does it cause lip darkening or discoloration?", "No, it uses safety-tested cosmetic colorants that stain topically without darkening natural lip pigment."),
        ("Can this tint be used as a liquid blush?", "Yes, blending a tiny dot onto cheeks creates a fresh, natural dewy flush."),
        ("What other shades are available in Beausta Lip Tints?", "Beausta offers multiple shades including Purple, Red, and Orange Peach to match diverse makeup preferences."),
        ("Can I wear lip balm under the tint?", "Yes, though blotting off excess balm before applying the tint ensures optimal water-stain adhesion."),
        ("Is the pouch cap re-sealable securely?", "Yes, it features a tight screw cap that prevents leakage inside bags or pockets."),
        ("Is Beausta cruelty-free?", "Yes, Beausta is committed to cruelty-free standards without animal testing."),
        ("Why is Beausta popular in K-beauty?", "Beausta pioneered convenient, high-quality pouch cosmetics, offering premium formulas at accessible price points."),
        ("Does heat affect the pouch formula?", "Keep in a cool place and avoid leaving inside hot cars to maintain optimal serum consistency."),
        ("Does the gloss highlight lip lines?", "No, the hydrating glassy finish blurs fine lines and creates a smoother, plumper lip appearance."),
        ("How do I verify product authenticity at Ekleel Abha?", "All Beausta products at Ekleel Abha are 100% genuine, imported directly from authorized Saudi distributors."),
        ("Is it suitable for a subtle 'no-makeup' look?", "Yes, one light coat provides a natural, youthful flush ideal for daily school, work, or casual wear."),
        ("Can I apply clear gloss over the tint?", "The formula already features a high-shine finish, though adding clear gloss is possible for extra intensity.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": str(prod_id),
        "sku": f"EK-{prod_id}",
        "gtin": gtin,
        "category": "المكياج / ملون وملمع الشفاه",
        "brand": "Beausta",
        "ar": {
            "title": f"ملمع وملون شفاه لامع {color_ar} من بيوستا 4مل",
            "meta_title": f"ملمع وملون شفاه بيوستا {color_ar} 4مل | صيدلية إكليل أبها",
            "meta_description": f"اشتري ملمع وملون شفاه بيوستا الكوري اللامع بدرجة {color_ar} (4مل). لمعان زجاجي وثبات طويل بعبوة كيس مدمجة. منتج أصلي 100% من إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["بيوستا", "تينت_شفاه", "ملمع_شفاه", "مكياج_كوري", f"بيوستا_{color_ar}", "إكليل_أبها"]
        },
        "en": {
            "title": f"Beausta Glossy Lip Tint & Gloss - {color_en} 4ml",
            "meta_title": f"Beausta Glossy Lip Tint {color_en} 4ml | Ekleel Abha Pharmacy",
            "meta_description": f"Buy Beausta Shine Gloss Lip Tint {color_en} (4ml) from Korea. Glassy shine & long-wearing stain in a portable pouch. 100% authentic at Ekleel Abha.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["beausta", "lip_tint", "lip_gloss", "kbeauty", f"beausta_{color_en.lower()}", "ekleel_abha"]
        },
        "schema": {
            "brand": "Beausta",
            "category": "Makeup / Lip Tint",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": f"beausta-glossy-lip-tint-{img_slug}-4ml.webp",
            "alt": f"Beausta Glossy Lip Tint {color_en} 4ml",
            "title": f"Beausta Glossy Lip Tint {color_en} 4ml"
        }
    }

print("Beausta module ready")
