import json, os

def create_product_1685():
    ar_desc = """<h2>نظرة عامة على المنتج</h2>
<p>يُعتبر <strong>قناع الجيلي الموازن للحموضة pH 5.5 من إيم سوري فور ماي سكن (I'm Sorry For My Skin pH 5.5 Jelly Mask - Soothing / Moisture)</strong> حلاً كورياً متطوراً للعناية بالبشرة المجهدة والحساسة. يعيد هذا القناع التوازن الطبيعي لدرجة حموضة البشرة (pH 5.5) التي قد تتأثر باستخدام المنظفات القاسية أو العوامل البيئية الضارة. بفضل خلاصة الجيلي الغنية بحجم 33 مل ورقعة القناع المصنوعة من ألياف الإيوسيل (I-CELL) المستخلصة من شجر الأوكالبتوس، يمنح البشرة تهدئة فورية وترطيباً عميقاً يستمر لعدة ساعات دون أي ملمس لزج.</p>
<p>تم تصميم القناع ليناسب جميع أنواع البشرة وخاصة البشرة المعرضة للتهيج والاحمرار. يحتوي على مركب مهدئ فريد يضم خلاصة سنتيلا أسياتيكا (Centella Asiatica) والبانثينول والبابونج، مما يقلل من التهيج، يعزز حاجز البشرة الواقي، ويعيد إليها النضارة والحيوية والنعومة الفائقة بعد يوم طويل من الإجهاد.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>موازنة درجة الحموضة المثالية (pH 5.5):</strong> يحافظ على استقرار حموضة البشرة الطبيعية مما يدعم صحة حاجز البشرة ويمنع فقدان الرطوبة.</li>
  <li><strong>ترطيب عميق ومكثف:</strong> مشبع بـ 33 مل من السيروم الجيلي الغني الذي يغذي طبقات الجلد العميقة ويمنحها انتعاشاً يدوم طويلاً.</li>
  <li><strong>تهدئة فورية للتهيج والاحمرار:</strong> يهدئ البشرة المتهيجة نتيجة أشعة الشمس أو التلوث أو التقشير بفضل مركب سنتيلا أسياتيكا والبانثينول.</li>
  <li><strong>نسيج ألياف إيوسيل (I-CELL) المستدام:</strong> رقعة قناع نباتية صديقة للبيئة تلتصق بالوجه بكفاءة عالية لتضمن امتصاصاً مثالياً للمكونات المغذية.</li>
  <li><strong>تعزيز حاجز الحماية الطبيعي:</strong> يساعد على تقوية طبقة الليبيد الواقية للجلد لحمايته من البكتيريا والجفاف والتأثيرات البيئية الضارة.</li>
  <li><strong>خالي من المواد القاسية:</strong> تركيبته لطيفة وآمنة تماماً للبشرة الحساسة خالية من البارابين والمواد الكيميائية الضارة.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التنظيف والتأهيل):</strong> اغسلي وجهك جيداً بالمنظف المناسب واستخدمي التونر لتجهيز البشرة لامتصاص السيروم.</li>
  <li><strong>الخطوة الثانية (توزيع الجيلي):</strong> دلكي العبوة مغلقة برفق لتوزيع السيروم الجيلي بالتساوي داخل رقعة القناع.</li>
  <li><strong>الخطوة الثالثة (تطبيق القناع):</strong> افتحي العبوة وضعي القناع بدقة على الوجه مع ضبط فتحات العينين والأنف والفم.</li>
  <li><strong>الخطوة الرابعة (الانتظار):</strong> اتركي القناع على البشرة لمدة 10 إلى 20 دقيقة حتى تمتص البشرة المكونات الفعالة.</li>
  <li><strong>الخطوة الخامسة (الربت والامتصاص):</strong> أزيلي القناع وربتي برفق بأطراف أصابعك على ما تبقى من السيروم حتى يتم امتصاصه كاملاً (يمكن استخدام باقي الجيلي على الرقبة واليدين).</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<ul>
  <li><strong>خلاصة سنتيلا أسياتيكا (Centella Asiatica):</strong> مكون كوري شهير يمتاز بخصائصه المهدئة والمضادة لالتهابات الجلد والمحفزة لإنتاج الكولاجين.</li>
  <li><strong>البانثينول (Panthenol - Pro-Vitamin B5):</strong> يمتص الرطوبة ويحتفظ بها داخل طبقات الجلد ويساعد في تسريع ترميم الخلايا المتضررة.</li>
  <li><strong>خلاصة البابونج والألوفيرا:</strong> تمنح البشرة انتعاشاً وتهدئة سريعة للتهيج والحكة الناتجة عن الجفاف.</li>
  <li><strong>الألانتوين والتريهالوز (Allantoin & Trehalose):</strong> مرطبات طبيعية تحمي غشاء الخلايا وتمنح الجلد ملمساً ناعماً ومخملياً.</li>
  <li><strong>حمض الهيالورونيك:</strong> يجذب جزيئات الماء لترطيب البشرة من الداخل ومنحها مظهر ممتلئ وصحي.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>للاستخدام الخارجي فقط؛ تجنبي ملامسة المنتج للمحيط المباشر للعينين.</li>
  <li>توقفي عن الاستخدام فوراً في حال ظهور أعراض حساسية مثل احمرار شديد أو حكة غير طبيعية.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن أشعة الشمس المباشرة.</li>
  <li>يُستخدم القناع فور فتحه ولا يعاد استخدامه مرة أخرى لضمان النظافة والفعالية.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>لأصحاب البشرة الحساسة أو المتهيجة التي تحتاج إلى تهدئة فورية وترطيب عميق.</li>
  <li>لمن يعانون من اختلال حاجز البشرة بسبب الغسول القاسي أو المؤثرات البيئية الخارجية.</li>
  <li>لكل من يبحث عن قناع كوري ترطيبي غني بالسيروم الجيلي لإعادة النضارة للبشرة المجهدة.</li>
  <li>مناسب لجميع أنواع البشرة (الجافة، العادية، المختلطة، والدهنية الحساسة).</li>
</ul>"""

    ar_specs = """<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>إيم سوري فور ماي سكن (I'm Sorry For My Skin)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / أقنعة الوجه</td></tr>
  <tr><th>نوع المنتج</th><td>قناع ورقي سيروم جيلي موازن للحموضة (pH 5.5)</td></tr>
  <tr><th>الحجم/الوزن</th><td>33 مل (سيروم القناع)</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة وخاصة الحساسة والمتهيجة</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة هادئة، مشدودة، ومشرقة برطوبة طبيعية</td></tr>
  <tr><th>الملمس</th><td>سيروم جيلي مرطب وخفيف</td></tr>
  <tr><th>العطر</th><td>عشب طبيعي خفيف ومريح</td></tr>
  <tr><th>المكونات النشطة</th><td>سنتيلا أسياتيكا، بانثينول، بابونج، ألانتوين، حمض الهيالورونيك</td></tr>
  <tr><th>بلد المنشأ</th><td>كوريا الجنوبية</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ultru / I'm Sorry For My Skin</td></tr>
  <tr><th>الفئة العمرية</th><td>جميع الفئات العمرية (ابتداءً من 15 سنة)</td></tr>
</tbody>
</table>"""

    ar_kb = """<h2>الدليل المعرفي لتوازن حموضة البشرة (pH 5.5) وأقنعة الجيلي</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج قناع إيم سوري فور ماي سكن مشكلة اضطراب حاجز البشرة والتهيج الناتج عن اختلال درجة الحموضة الطبيعية للجلد (Skin Acid Mantle). يؤدي اختلال حموضة البشرة إلى الجفاف، الاحمرار، زاوية المسام الواسعة، وحساسية مفرطة للملوثات البيئية.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تتمتع البشرة الصحيه بغلاف حمضي طبيعي يبلغ مسعر حموضته 5.5 للحد من نمو البكتيريا الضارة. عند استخدام منظفات قاسية أو غسل الوجه بماء كلسي أو التعرض المستمر لأشعة الشمس والتلوث، ترتفع درجة حموضة الجلد نحو القلوية، مما يضعف الغلاف الواقي ويسبب الجفاف والتهيج السريع.</p>

<h3>نصائح وقائية للروتين اليومي</h3>
<p>1. <strong>استخدام غسول متوازن الحموضة:</strong> اختاري منظفات برقم pH 5.5 لحماية الغلاف الطبيعي للبشرة.<br>
2. <strong>تجنب التقشير المفرط:</strong> لا تفرطي في استخدام الأحماض أو المقشرات الفيزيائية لتجنب تلف حاجز البشرة.<br>
3. <strong>الترطيب بمنتجات الجيلي:</strong> أقنعة الجيلي توفر ترطيباً مائياً عميقاً دون إغلاق المسام.<br>
4. <strong>استخدام الأقنعة بانتظام:</strong> تطبييق أقنعة التهدئة مرتين أسبوعياً يعيد للبشرة حيويتها ومظهرها الشاب.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "أقنعة الجيلي تترك طبقة لزجة وثقيلة على البشرة."<br>
<strong>الحقيقة:</strong> قناع الجيلي الكوري يتميز بسيروم خفيف يمتصه الجلد بسرعة كاملة ليمنح ترطيباً مائياً ناعماً دون ملمس دهني.</p>
<p><strong>خرافة:</strong> "البشرة الدهنية لا تحتاج إلى أقنعة ترطيب."<br>
<strong>الحقيقة:</strong> البشرة الدهنية قد تعاني من الجفاف الداخلي واختلال الحموضة، وترطيبها بقناع موازن يحميهم من الإفراز الزائد للدهون.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يعمل القناع بآلية الامتصاص الذاتي بواسطة ألياف I-CELL المستخلصة من الأوكالبتوس التي تنقل 33 مل من السيروم المتوازن كيميائياً بدرجة pH 5.5 مباشرةً إلى خلايا البشرة. تعمل مركبات البانثينول وسنتيلا أسياتيكا على تقليل إنزيمات التهيج الجلدية وتحفيز بناء الأحماض الدهنية الأساسية، مما يعيد ترميم الغشاء الليبيدي ويضمن ثبات جزيئات الماء داخل البشرة لفترة طويلة.</p>"""

    faqs = [
        ("ما هو قناع الجيلي pH 5.5 من إيم سوري فور ماي سكن؟", "هو قناع ورقي كوري مشبع بـ 33 مل من السيروم الجيلي المغذي، مصمم بدرجة حموضة متوازنة (pH 5.5) لتهدئة البشرة المتهيجة وترطيبها بعمق وترميم حاجز الجلد الطبيعي."),
        ("ما أهمية درجة الحموضة pH 5.5 للبشرة؟", "درجة pH 5.5 هي الحموضة المثالية للجلد الصحي، حيث تمنع نمو البكتيريا الضارة وتحافظ على توازن غلاف الليبيد الواقي لمنع جفاف البشرة وتهيجها."),
        ("هل يترك السيروم الجيلي ملمساً لزجاً على الوجه؟", "لا، يتميز السيروم الجيلي بتركيبة سريعة الامتصاص تنفذ إلى طبقات البشرة وتتركها ناعمة ومنعشة دون أي بقايا زيتيّة أو لزجة."),
        ("ما هي مادة ألياف I-CELL المصنوع منها القناع؟", "ألياف I-CELL هي نسيج كوري نباتي مستخلص من ألياف الأوكالبتوس، صديق للبيئة ويتكيف تماماً مع انحناءات الوجه لضمان توصيل المكونات الفعالة بفعالية عالية."),
        ("هل القناع مناسب للبشرة الحساسة؟", "نعم، القناع خالي من المواد الكيميائية القاسية والبارابين، ومصمم خصيصاً لتهدئة البشرة الحساسة والمعرضة للاحمرار والتهيج."),
        ("كم مرة يُنصح باستخدام القناع في الأسبوع؟", "يُنصح باستخدامه من مرتين إلى ثلاث مرات أسبوعياً، أو كلما شعرتِ بجهد وجفاف في البشرة يحتاج للتهدئة والترطيب."),
        ("كم من الوقت يجب ترك القناع على الوجه؟", "يُترك القناع لمدة 10 إلى 20 دقيقة فقط لضمان امتصاص السيروم دون أن يجف الورق على الوجه."),
        ("هل يلزم غسل الوجه بالماء بعد إزالة القناع؟", "لا، لا ينبغي غسل الوجه بالماء. يُفضل الربت بلطف بأطراف الأصابع على البشرة حتى يمتص السيروم المتبقي بالكامل."),
        ("ماذا أفعل بالسيروم الجيلي المتبقي في العبوة؟", "السيروم المتبقي غني جداً ويمكن وضعه على منطقة الرقبة، الصدر، اليدين أو الكوعين لترطيبها واستغلال كافة فوائد القناع."),
        ("هل يساعد هذا القناع في تخفيف احمرار الشمس؟", "نعم، يحتوي على خلاصة سنتيلا أسياتيكا والبابونج والبانثينول التي تهدئ الاحمرار وتخفف الحرارة الناتجة عن التعرض للشمس."),
        ("هل يناسب القناع البشرة الدهنية والمعرضة لحب الشباب؟", "نعم، تركيبته الخفيفة الموازنة للحموضة تحافظ على رطوبة البشرة دون إغلاق المسام وتساعد في موازنة إفراز الدهون."),
        ("هل يمكن استخدام القناع قبل تطبيق المكياج؟", "نعم، استخدامه قبل المكياج يمنح البشرة ترطيباً رائعاً ومظهراً ممتلئاً وناعماً، مما يساعد المكياج على الثبات بشكل أفضل بدون تكتل."),
        ("هل يمكن حفظ القناع في الثلاجة قبل الاستخدام؟", "نعم، وضع العبوة في الثلاجة لمدة 10 دقائق قبل التطبيق يمنح البشرة انتعاشاً مضاعفاً ويسهم في تقليل انتفاخ الوجه."),
        ("ما هي المكونات الرئيسية المهدئة في القناع؟", "المكونات الأساسية هي خلاصة سنتيلا أسياتيكا الكورية، والبانثينول (فيتامين B5)، والألانتوين، وخلاصة البابونج والألوفيرا."),
        ("هل يحتوي القناع على عطور صناعية قوية؟", "لا، يتمتع برائحة عشبية طبيعية خفيفة جداً ولطيفة لا تسبب تهيجاً للبشرة الحساسة."),
        ("هل يحمي القناع من التجاعيد المبكرة؟", "الترطيب العميق وموازنة الحموضة يمنعان الجفاف الذي يُعد السبب الرئيسي لظهور الخطوط الدقيقة والتجاعيد المبكرة."),
        ("ما حجم كمية السيروم داخل العبوة؟", "تحتوي العبوة على كمية سخية تبلغ 33 مل من السيروم الجيلي الفاخر، وهي من أعلى الكميات في الأقنعة الكورية الورقية."),
        ("هل يناسب القناع الرجال أيضاً؟", "بالتأكيد، القناع مناسب لجميع الأجناس ويوفر تهدئة ممتازة للبشرة بعد الحلاقة أو التعرض للشمس."),
        ("ما هو بلد صنع هذا المنتج؟", "صُنع هذا القناع بفخر في كوريا الجنوبية بواسطة العلامة التجارية الشهيرة I'm Sorry For My Skin."),
        ("هل المنتج آمن للاستخدام أثناء الحمل؟", "نعم، مكونات القناع موضعية ومرطبة وآمنة عموماً، ولكن يُنصح دائماً بمراجعة قائمة المكونات واستشارة الطبيب المتابع."),
        ("هل يحتاج القناع لاستخدام كريم مرطب بعده؟", "صاحبات البشرة الدهنية والمختلطة قد لا يحتجن مرطب إضافي، أما البشرة الشديدة الجفاف فيفضل وضع طبقية خفيفة من المرطب لإغلاق الرطوبة."),
        ("كيف أعرف أن المنتج أصلي من إكليل أبها؟", "يتم استيراد كافة منتجات إكليل أبها من الوكلاء المعتمدين وتتميز بوجود الباركود الكوري الأصلي والتغليف المحكم."),
        ("هل يسبب القناع تهيج العينين؟", "القناع مصمم بفتحات دقيقة للعينين، ولكن ينبغي تجنب ملامسة السيروم المباشرة لداخل العين."),
        ("ما الفرق بين إصدار Soothing وإصدارات القناع الأخرى؟", "إصدار Soothing يركز بشكل أساسي على تهدئة الاحمرار والتهيج وموازنة الحموضة، بينما تركز الإصدارات الأخرى على التفتيح أو التقشير اللطيف."),
        ("هل يعاد استخدام رقعة القناع؟", "لا، القناع الورقي مصمم للاستخدام المرة الواحدة فقط لضمان أقصى درجات النظافة والفعالية الطبية.")
    ]

    ar_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in faqs])

    en_desc = """<h2>Product Overview</h2>
<p>The <strong>I'm Sorry For My Skin pH 5.5 Jelly Mask (Soothing / Moisture)</strong> is an innovative Korean skincare solution designed to restore optimal balance to stressed, sensitive skin. Formulated at a skin-ideal pH of 5.5, this sheet mask normalizes the natural acid mantle disrupted by harsh cleansers or environmental stressors. Infused with a generous 33ml of lightweight jelly essence and supported by an eco-friendly eucalyptus-derived I-CELL sheet, it delivers immediate calming relief and long-lasting hydration without a sticky residue.</p>
<p>Tailored for skin prone to redness, irritation, or dryness, this mask harnesses the power of Centella Asiatica, Panthenol, Chamomile, and Allantoin. It strengthens the natural moisture barrier, reduces inflammation, and leaves the complexion refreshed, supple, and radiant after a demanding day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Optimal pH 5.5 Balance:</strong> Restores natural skin acidity, fortifying the barrier against bacteria and moisture loss.</li>
  <li><strong>Intensive 33ml Jelly Hydration:</strong> Drenches the skin in a generous reservoir of soothing serum for deep, lasting moisture.</li>
  <li><strong>Immediate Calming Effect:</strong> Soothes redness, heat, and irritation caused by sun exposure, pollution, or exfoliants.</li>
  <li><strong>Eco-Friendly I-CELL Sheet:</strong> Breathable eucalyptus fiber sheet clings seamlessly to facial contours for maximum nutrient absorption.</li>
  <li><strong>Barrier Fortification:</strong> Enhances the skin's protective lipid layer to ward off environmental aggressors and dryness.</li>
  <li><strong>Clean & Gentle Formula:</strong> Free from harsh chemicals, parabens, and artificial irritants, making it ideal for sensitive skin.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Cleanse & Prep):</strong> Cleanse your face thoroughly and apply toner to prepare the skin.</li>
  <li><strong>Step 2 (Distribute Jelly):</strong> Gently rub the closed pouch to evenly spread the jelly essence across the sheet mask.</li>
  <li><strong>Step 3 (Apply Mask):</strong> Unfold and place the mask evenly onto the face, aligning eye, nose, and mouth cutouts.</li>
  <li><strong>Step 4 (Relax):</strong> Leave the mask on for 10 to 20 minutes to allow deep essence absorption.</li>
  <li><strong>Step 5 (Pat & Absorb):</strong> Remove the mask and gently pat remaining essence into the skin until fully absorbed (apply excess jelly to neck and hands).</li>
</ul>

<h2>Ingredients Overview</h2>
<ul>
  <li><strong>Centella Asiatica Extract:</strong> Iconic Korean botanical ingredient renowned for healing, anti-inflammatory, and soothing properties.</li>
  <li><strong>Panthenol (Pro-Vitamin B5):</strong> Attracts and binds moisture to skin cells, promoting rapid barrier repair and softness.</li>
  <li><strong>Chamomile & Aloe Extracts:</strong> Provide instant cooling relief to irritated or dehydrated skin.</li>
  <li><strong>Allantoin & Trehalose:</strong> Natural conditioning agents that protect cell membranes and smooth skin texture.</li>
  <li><strong>Hyaluronic Acid:</strong> Pulls water molecules deep into epidermal layers for a plumped, healthy complexion.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external use only; avoid direct contact with the inner eye area.</li>
  <li>Discontinue use immediately if irritation, swelling, or severe redness occurs.</li>
  <li>Keep out of reach of children and store in a cool, dry place away from direct sunlight.</li>
  <li>Single-use product; do not reuse the sheet mask to ensure safety and hygiene.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Individuals with sensitive, irritated, or redness-prone skin needing instant relief.</li>
  <li>Anyone with a compromised skin barrier caused by harsh cleansers or environmental exposure.</li>
  <li>Skincare enthusiasts seeking deep hydration through an enriched Korean jelly serum mask.</li>
  <li>Suitable for all skin types including oily, dry, combination, and sensitive skin.</li>
</ul>"""

    en_specs = """<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>I'm Sorry For My Skin</td></tr>
  <tr><th>Category</th><td>Skincare / Facial Sheet Masks</td></tr>
  <tr><th>Product Type</th><td>pH 5.5 Balancing Jelly Sheet Mask</td></tr>
  <tr><th>Volume/Weight</th><td>33 ml (Essence Volume)</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Ideal for Sensitive & Irritated Skin)</td></tr>
  <tr><th>Finish</th><td>Calmed, Plump, Hydrated & Radiant Skin</td></tr>
  <tr><th>Texture</th><td>Non-sticky, cooling jelly serum</td></tr>
  <tr><th>Fragrance</th><td>Light natural herbal aroma</td></tr>
  <tr><th>Active Ingredients</th><td>Centella Asiatica, Panthenol, Chamomile, Allantoin, Hyaluronic Acid</td></tr>
  <tr><th>Country of Origin</th><td>South Korea</td></tr>
  <tr><th>Manufacturer</th><td>Ultru / I'm Sorry For My Skin</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens (15+)</td></tr>
</tbody>
</table>"""

    en_kb = """<h2>Clinical Insights on Skin pH Balance & Jelly Mask Technology</h2>

<h3>What problem does this solve?</h3>
<p>The I'm Sorry For My Skin pH 5.5 Jelly Mask addresses skin barrier damage, redness, and dehydration caused by acid mantle imbalance. When skin pH strays from its natural acidic state, the lipid barrier weakens, leaving skin vulnerable to inflammation, bacterial breakouts, and accelerated moisture loss.</p>

<h3>Why does this condition happen?</h3>
<p>Healthy skin maintains a naturally acidic pH of approximately 5.5 to suppress harmful microbes. Everyday exposure to alkaline cleansers, hard tap water, pollution, and UV radiation raises skin pH toward alkalinity. This destabilizes the natural protective mantle, causing tight, sensitized skin that reacts easily to external irritants.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Use pH-Balanced Cleansers:</strong> Select cleansers formulated near pH 5.5 to preserve the acid mantle.<br>
2. <strong>Avoid Over-Exfoliation:</strong> Limit physical scrubs and strong chemical acids to prevent barrier stripping.<br>
3. <strong>Hydrate with Jelly Serums:</strong> Jelly essences deliver intense water hydration without clogging pores.<br>
4. <strong>Incorporate Sheet Masks Regularly:</strong> Applying soothing sheet masks twice weekly maintains barrier resilience.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Jelly mask essences leave a heavy, sticky film on the skin."<br>
<strong>Fact:</strong> High-quality Korean jelly serums feature lightweight water-binding polymers that absorb completely, leaving skin soft and velvety without greasy residue.</p>
<p><strong>Myth:</strong> "Oily skin types do not need hydrating sheet masks."<br>
<strong>Fact:</strong> Oily skin often suffers from internal dehydration and pH imbalance; balancing hydration prevents overproduction of compensatory sebum.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>This mask operates via capillary delivery through eucalyptus-derived I-CELL fibers that transport 33ml of pH 5.5 buffered serum directly to the epidermis. Active Centella Asiatica terpenes downregulate pro-inflammatory cytokines, while Panthenol accelerates lipid synthesis. Together, they repair corneal cohesion, suppress transepidermal water loss (TEWL), and stabilize skin homeostasis.</p>"""

    en_faqs = [
        ("What is the I'm Sorry For My Skin pH 5.5 Jelly Mask?", "It is a premium Korean sheet mask saturated with 33ml of jelly essence, specifically formulated at pH 5.5 to balance, soothe, and deeply hydrate sensitive or stressed skin."),
        ("Why is pH 5.5 balance important for the skin?", "pH 5.5 represents the skin's ideal natural acidity, which maintains a healthy acid mantle, protects against harmful bacteria, and prevents transepidermal moisture loss."),
        ("Does the jelly serum leave a sticky residue?", "No, the jelly serum is formulated to absorb rapidly into the skin, delivering intense moisture without leaving any greasy or uncomfortable stickiness."),
        ("What is the I-CELL sheet material made of?", "The I-CELL sheet is an eco-friendly, biodegradable fabric made from eucalyptus fibers that adheres smoothly to the face for optimal essence delivery."),
        ("Is this mask suitable for sensitive skin?", "Yes, it is dermatologist-tested, free from harsh chemicals and parabens, and specially designed to soothe redness and sensitive skin."),
        ("How often should I use this sheet mask?", "It is recommended to use 2 to 3 times per week or whenever your skin feels dehydrated, irritated, or stressed."),
        ("How long should I leave the mask on?", "Leave the mask on for 10 to 20 minutes to allow full essence absorption without letting the sheet dry out on your face."),
        ("Should I rinse my face after removing the mask?", "No, do not rinse. Gently pat the remaining jelly essence into your face and neck until fully absorbed to retain all beneficial nutrients."),
        ("What should I do with excess jelly in the pouch?", "The pouch contains a generous 33ml of essence; apply any leftover jelly to your neck, chest, arms, or elbows for extra hydration."),
        ("Does this mask help relieve sun exposure redness?", "Yes, enriched with Centella Asiatica, Chamomile, and Panthenol, it provides instant cooling relief to sun-exposed or overheated skin."),
        ("Is this mask suitable for acne-prone skin?", "Yes, its non-comedogenic jelly formula balances skin pH without clogging pores, helping calm active irritation."),
        ("Can I use this sheet mask before makeup application?", "Yes, using it before makeup plumps the skin and creates a smooth, hydrated canvas that helps makeup apply smoothly."),
        ("Can I chill the mask in the refrigerator before use?", "Yes, keeping the sealed mask in the fridge for 10 minutes prior to use provides an extra cooling sensation that reduces facial puffiness."),
        ("What are the primary active ingredients?", "The key ingredients include Centella Asiatica Extract, Panthenol (Pro-Vitamin B5), Chamomile, Allantoin, and Hyaluronic Acid."),
        ("Does the mask contain strong artificial fragrances?", "No, it features a subtle, natural herbal scent derived from botanical ingredients that will not irritate sensitive skin."),
        ("Does this mask help prevent premature skin aging?", "Yes, maintaining deep hydration and restoring pH 5.5 prevents dryness, which is a major factor in premature fine line formation."),
        ("How much essence is included in each pouch?", "Each pouch contains a generous 33ml of rich jelly serum, significantly higher than standard sheet masks."),
        ("Is this mask suitable for men?", "Yes, it is a unisex product that works exceptionally well to soothe skin after shaving or outdoor activities."),
        ("Where is this product manufactured?", "It is manufactured in South Korea by the renowned skincare brand I'm Sorry For My Skin (Ultru)."),
        ("Is this product safe during pregnancy?", "Yes, its topical hydrating ingredients are generally safe, though reviewing the ingredient list with your physician is always advised."),
        ("Do I need to apply moisturizer after using the mask?", "Oily and combination skin types may not need extra moisturizer, while dry skin types can layer a light moisturizer to seal in the hydration."),
        ("How can I verify product authenticity at Ekleel Abha?", "All products at Ekleel Abha are 100% authentic, imported directly from certified South Korean distributors with verifiable barcodes."),
        ("Can the serum irritate the eyes?", "The sheet mask is contoured away from the eyes, but direct contact of the liquid essence with the eyes should be avoided."),
        ("How does the Soothing mask differ from other variants?", "The Soothing variant specifically targets redness, irritation, and pH recovery, whereas other variants focus on brightening or pore care."),
        ("Is the sheet mask reusable?", "No, sheet masks are designed for single-use only to maintain medical hygiene and prevent bacterial contamination.")
    ]

    en_faqs_html = "".join([f"<h3>{q}</h3>\n<p>{a}</p>\n" for q, a in en_faqs])

    return {
        "product_id": "1685",
        "sku": "EK-1685",
        "gtin": "8809511985583",
        "category": "العناية بالبشرة / أقنعة الوجه",
        "brand": "I'm Sorry For My Skin",
        "ar": {
            "title": "قناع الجيلي PH5.5 الموازن والمهدئ للبشرة من ايم سوري فور ماي سكن",
            "meta_title": "قناع الجيلي الموازن للحموضة pH 5.5 ايم سوري فور ماي سكن | إكليل أبها",
            "meta_description": "اشتري قناع الجيلي الكوري الموازن للحموضة pH 5.5 من ايم سوري فور ماي سكن (33مل) لتهدئة وترطيب البشرة الحساسة. منتج أصلي 100% من صيدلية إكليل أبها.",
            "description": ar_desc,
            "specifications": ar_specs,
            "knowledge_base": ar_kb,
            "faqs": ar_faqs_html,
            "tags": ["ايم_سوري_فور_ماي_سكن", "قناع_جيلي", "pH5.5", "عناية_كورية", "إكليل_أبها"]
        },
        "en": {
            "title": "I'm Sorry For My Skin pH5.5 Jelly Mask - Soothing",
            "meta_title": "I'm Sorry For My Skin pH5.5 Jelly Mask 33ml | Ekleel Abha",
            "meta_description": "Buy I'm Sorry For My Skin pH5.5 Soothing Jelly Sheet Mask (33ml). Restores skin balance with Centella & Panthenol. 100% authentic at Ekleel Abha Pharmacy.",
            "description": en_desc,
            "specifications": en_specs,
            "knowledge_base": en_kb,
            "faqs": en_faqs_html,
            "tags": ["im_sorry_for_my_skin", "jelly_mask", "ph5_5", "korean_skincare", "ekleel_abha"]
        },
        "schema": {
            "brand": "I'm Sorry For My Skin",
            "category": "Skincare / Sheet Masks",
            "availability": "InStock"
        },
        "image_seo": {
            "image_filename": "im-sorry-for-my-skin-ph5-5-jelly-mask-soothing.webp",
            "alt": "I'm Sorry For My Skin pH5.5 Soothing Jelly Mask 33ml",
            "title": "I'm Sorry For My Skin pH5.5 Soothing Jelly Mask 33ml"
        }
    }

print("Loaded 1685 builder")
