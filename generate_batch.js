const fs = require('fs');
const path = require('path');

const targetDirs = [
  path.join(__dirname, 'temp/generated_products'),
  path.join(__dirname, '../temp/generated_products')
];

targetDirs.forEach(dir => {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
});

const products = [
  // ==========================================
  // PRODUCT 1434: Uriage Dépiderm Hand Cream SPF 15 50ml
  // ==========================================
  {
    "product_id": "1434",
    "sku": "EK-1434",
    "category": "العناية بالبشرة / العناية باليدين",
    "brand": "Uriage",
    "ar": {
      "title": "كريم تفتيح لليدين دبيدرم مع واقي شمس 15 من يورياج 50مل",
      "meta_title": "كريم تفتيح لليدين دبيدرم مع واقي شمس 15 من يورياج 50مل | إكليل أبها",
      "meta_description": "اشتري كريم تفتيح اليدين دبيدرم SPF 15 من يورياج (50مل). يقضي على البقع الداكنة والتصبغات ويحمي اليدين من أشعة الشمس وترطيب طبي عميق. منتج أصلي 100%.",
      "description": `<h2>نظرة عامة على المنتج</h2>
<p>كريم تفتيح اليدين دبيدرم من يورياج <strong>(Uriage Dépiderm Brightening Hand Cream with SPF 15 - 50ml)</strong> هو حل طبي متقدم مخصص لعلاج وتفتيح البقع الداكنة والتصبغات الجليدية المستعصية التي تظهر على ظهر اليدين نتيجة التعرض المستمر لـ أشعة الشمس، عوامل الشيخوخة الطبيعية، أو التغيرات الهرمونية. تم تطوير هذا المستحضر في مختبرات يورياج الفرنسية وفق أحدث التقنيات الجلدية للجمع بين مفعول التفتيح المكثف والحماية الشاملة من الأشعة فوق البنفسجية (UVA/UVB) بدرجة حماية SPF 15 لمنع ظهور التصبغات مجدداً.</p>

<p>يمتاز الكريم بتركيبة مخملية فائقة الخفة سريعة الامتصاص لا تترك أي أثر لزج أو دهني، مما يسمح بممارسة الأنشطة اليومية بحرية فور تطبيقه. بالإضافة إلى ذلك، فهو مدعم بـ مياه يورياج الحرارية النقية والغنية بالمعادن التي تعمل على تهدئة البشرة الحساسة وتقوية حاجز الجلد الطبيعي، إلى جانب منع جفاف اليدين الناتج عن الغسيل المتكرر والمعقمات الكحولية.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تفتيح البقع الداكنة:</strong> يعمل مركب Mela Technology المبتكر على تقليل حجم ولون البقع البنية وتصبغات الشمس على اليدين بنسبة ملحوظة.</li>
  <li><strong>حماية من أشعة الشمس SPF 15:</strong> يوفر وقاية يومية فعالة ضد الأشعة فوق البنفسجية للحد من الأضرار التأكسدية وتكون بقع جديدة.</li>
  <li><strong>ترطيب وتغذية مكثفة:</strong> يمنح اليدين ترطيباً عميقاً يستمر لعدة ساعات، مما يمنع التشظي والجفاف الناجم عن العوامل البيئية.</li>
  <li><strong>امتصاص سريع وقوام غير دهني:</strong> يمتص بسرعة فائقة في طبقات الجلد دون ترك طبقة زيتية مزعجة على المقابض أو الهواتف.</li>
  <li><strong>تهدئة البشرة والحد من التهيج:</strong> يحتوي على مياه يورياج الحرارية ومستخلص الإينوكسولون المهدئ لتقليل احمرار البشرة وتلطيفها.</li>
  <li><strong>توحيد لون البشرة واستعادة الشباب:</strong> يعيد لليدين مظهرها المشرق والمتجانس، ويحميها من علامات الشيخوخة المبكرة والتجاعيد السطحية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> اغسلي اليدين جيداً بالماء الفاتر وصابون لطيف خالٍ من المواد القاسية، ثم جففيهما بنعومة بواسطة منشفة نظيفة.</li>
  <li><strong>الخطوة الثانية:</strong> ضعي كمية مناسبة (بحجم حبة البازلاء) من كريم دبيدرم على ظهر كل يد.</li>
  <li><strong>الخطوة الثالثة:</strong> ادلكي ظهر اليدين والأصابع والمفاصل بحركات دائرية خفيفة حتى يمتص الجلد الكريم بالكامل.</li>
  <li><strong>الخطوة الرابعة:</strong> كوري التطبيق كل 2-3 ساعات في حال التعرض المستمر لأشعة الشمس المباشرة (مثل أثناء قيادة السيارة) أو بعد غسل اليدين بالماء والصابون.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<p>يتكون كريم دبيدرم من يورياج من تركيبة فريدة تعتمد على التكنولوجيا الجلدية الفرنسية المتطورة:</p>
<ul>
  <li><strong>مركب Mela Technology:</strong> يحتوي على مستخلص البازلاء والسوكروز مع مياه يورياج الحرارية وفيتامين C لتثبيط إنزيم التايروسينيز المسبب لتخلق الميلامين.</li>
  <li><strong>مياه يورياج الحرارية (Uriage Thermal Water):** مياه نقية متوازنة المعادن تهدئ التهابات الجلد وتدعم التجدد الخلوي.</li>
  <li><strong>مشتق فيتامين C المستقر:</strong> مضاد أكسدة قوي يعمل على تفتيح التصبغات وحماية الجلد من الإجهاد التأكسدي وتحفيز إنتاج الكولاجين.</li>
  <li><strong>مركب الإينوكسولون (Enoxolone):</strong> مركب مهدئ مضاد للالتهاب يساعد في السيطرة على تهيج البشرة الحساسة.</li>
  <li><strong>فلاتر حماية شمسية SPF 15:</strong> فلاتر كيميائية وفيزيائية متوازنة تحمي الجلد من الأشعة فوق البنفسجية بنوعيها UVA و UVB.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>مخصص للاستخدام الظاهري الخارجي فقط على جلد اليدين؛ تجنبي ملامسته للعينين والأغشية المخاطية.</li>
  <li>في حال وجود جروح مفتوحة، خدوش حادة، أو التهابات جلدية نشطة، انتظري حتى التئام الجلد تماماً قبل استخدام كريم التفتيح.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بدرجة حرارة أقل من 25 درجة مئوية بعيداً عن أشعة الشمس المباشرة.</li>
  <li>في حال حدوث طفح جلدي أو حساسية غير متوقعة، توقفي عن الاستخدام فوراً واستشيري طبيب الجلدية.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>للنساء والرجال الذين يعانون من ظهور البقع البنية، التصبغات الشمسية، أو بقع التقدم في السن على ظهر اليدين.</li>
  <li>للأشخاص الذين يقضون أوقاتاً طويلة في قيادة السيارة أو الأنشطة الخارجية ويرغبون في حماية أيديهم وتفتيحها.</li>
  <li>لكل من يبحث عن كريم يدين طبي يجمع بين العناية العلاجية للتفتيح، الوقاية من الشمس، والترطيب اليومي الفاخر.</li>
</ul>`,
      "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>Uriage (يورياج)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / العناية باليدين</td></tr>
  <tr><th>نوع المنتج</th><td>كريم تفتيح اليدين ومضاد التصبغات</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (بما فيها البشرة الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>بشرة موحدة اللون ومشرقة بدون لمس دهني</td></tr>
  <tr><th>الملمس</th><td>كريم مخملي خفيف</td></tr>
  <tr><th>العطر</th><td>خفيف جداً وخالٍ من العطور المسببة للحساسية</td></tr>
  <tr><th>المكونات النشطة</th><td>مركب Mela Technology، مياه يورياج الحرارية، فيتامين C، فلاتر SPF 15</td></tr>
  <tr><th>بلد المنشأ</th><td>فرنسا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Laboratoires Dermatologiques d'Uriage</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين (ابتداءً من سن 18 عاماً)</td></tr>
</tbody>
</table>`,
      "knowledge_base": `<h2>الدليل الطبي الشامل لتصبغات اليدين وحمايتها</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم دبيدرم من يورياج مشكلة التصبغات الجلدية والبقع الداكنة المستعصية التي تظهر على ظهر اليدين (Age Spots / Sun Spots). هذه البقع تنتج عن فرط نشاط الخلايا الصبغية وتراكم صبغة الميلامين غير المتجانسة نتيجة التعرض المتكرر للشمس والتغيرات البيئية.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>بشرة ظهر اليدين تعتبر من أكثر مناطق الجسم رقة وتأثراً بالعوامل الخارجية. تتعرض اليدين بشكل يومي ومستمر للأشعة فوق البنفسجية (خاصة أثناء قيادة السيارة أو السير في النهار) دون حماية كافية. هذه الأشعة تحفز إنزيم التايروسينيز داخل الخلايا الصبغية (Melanocytes)، مما يؤدي لإنتاج كميات فائضة من الميلامين تتجمع على شكل بقع بنية داكنة. كما أن الغسيل المتكرر بالصابون القاسي والمعقمات يضعف الحاجز الواقي للجلد، مما يزيد تسريع ظهور علامات التلف الضوئي والشيخوخة المبكرة.</p>

<h3>نصائح وقائية</h3>
<p>1. <strong>استخدام واقي الشمس بانتظام:</strong> تطليق واقي الشمس أو كريم يدين يحتوي على فلاتر حماية قبل الخروج نهاراً.<br>
2. <strong>ارتداء قفازات أثناء القيادة:</strong> حماية اليدين من أشعة الشمس المباشرة المارة عبر زجاج السيارة.<br>
3. <strong>الترطيب المستمر:</strong> ترطيب اليدين بعد كل عملية غسيل بالماء والصابون لتجنب التهيج الذي يحفز التصبغ.<br>
4. <strong>تجنب المعقمات الكحولية القاسية:</strong> اختيار معقمات تحتوي على مرطبات لتجنب جفاف الحاجز الجلدي.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "البقع الداكنة على اليدين مرتبطة فقط بتقدم العمر ولا يمكن علاجها بالكريمات."<br>
<strong>الحقيقة:</strong> السبب الرئيسي للبقع الداكنة هو التلف الناتج عن الشمس وليس العمر فقط. المنتجات الطبية المتطورة التي تحتوي على مثبطات الميلامين ومضادات الأكسدة مثل كريم دبيدرم قادرة على تفتيح هذه البقع وتحسين مظهر البشرة بشكل ملحوظ عند الالتزام بالاستخدام.</p>

<h3>التفسير العلمي</h3>
<p>يعتمد كريم دبيدرم على تقنية <strong>Mela Technology</strong> التي تستهدف عملية تخليق صبغة الميلامين في مراحله المختلفة. يمنع المستحضر تحفيز إنزيم التايروسينيز المسؤول عن تحويل الحمض الأميني التايروسين إلى ميلامين، بينما يعمل فيتامين C المستقر على أكسدة صبغة الميلامين الموجودة بالفعل لتفكيكها وتخفيف لونها. وتوفر فلاتر SPF 15 درعاً واقياً يحجب الأشعة فوق البنفسجية لمنع إعادة نشاط الخلايا الصبغية، بينما تعمل مياه يورياج الحرارية على تقليل الالتهابات الدقيقة التي قد تحفز التصبغ اللاحق للالتهاب (PIH).</p>`,
      "faqs": `<h3>ما هو كريم يورياج دبيدرم لليدين وما هي دواعي استخدامه؟</h3>
<p>كريم يورياج دبيدرم هو كريم طبي علاجى مصمم خصيصاً لتفتيح البقع الداكنة والتصبغات البنية على ظهر اليدين، وحمايتها من أشعة الشمس بفضل معامل الحماية SPF 15 مع ترطيب الجلد عميقاً.</p>
<h3>هل ينصح باستخدام هذا الكريم أثناء قيادة السيارة؟</h3>
<p>نعم وبشدة، لأن اليدين تتعرضان لأشعة الشمس المباشرة عبر زجاج السيارة، وتركيبة الكريم المدعمة بـ SPF 15 تحمي اليدين من التصبغات الشمسية الجديدة.</p>
<h3>كم من الوقت يستغرق ظهور نتائج تفتيح البقع الداكنة؟</h3>
<p>تبدأ النتائج الأولية في الظهور خلال 4 إلى 6 أسابيع من الاستخدام المنتظم مرتين يومياً، حيث يلاحظ تراجع درجة لون البقع واستعادة توحيد البشرة.</p>
<h3>هل يحتوي كريم دبيدرم يورياج على الكورتيزون أو الهيدروكينون؟</h3>
<p>لا، الكريم خالٍ تماماً من الكورتيزون والهيدروكينون، ويعتمد على مكونات طبيعية وطبية آمنة مثل مركب Mela Technology وفيتامين C ومياه يورياج الحرارية.</p>
<h3>هل يترك الكريم أثراً دهنياً على اليدين؟</h3>
<p>لا، يتميز الكريم بتركيبة سريعة الامتصاص خفيفة الوزن لا تترك أي بقايا زيتية أو لزوجة، مما يتيح لك استخدام هاتف أو العمل فوراً.</p>
<h3>هل يمكن استخدام الكريم للبشرة الحساسة؟</h3>
<p>نعم، كريم يورياج دبيدرم خضع لاختبارات جلدية صارمة ومصمم ليلائم جميع انواع البشرة بما فيها البشرة الحساسة بفضل احتواه على مياه يورياج المهدئة.</p>
<h3>كم مرة يجب تطبيق الكريم خلال اليوم؟</h3>
<p>يُنصح بتطبيقه مرتين يومياً على الأقل، وأعيدي تطبيقه بعد غسل اليدين بالماء والصابون أو عند التعرض المستمر للشمس نهاراً.</p>
<h3>هل يعالج الكريم التصبغات الناتجة عن التقدم في السن؟</h3>
<p>نعم، يقلل الكريم بشكل فعال من بقع التقدم في السن (Age Spots) بفضل مضادات الأكسدة ومثبطات صبغة الميلامين.</p>
<h3>هل يكفي معامل الحماية SPF 15 لحماية اليدين من الشمس؟</h3>
<p>معامل SPF 15 يمنح وقاية ممتازة للاستخدام اليومي والتعرض المتوسط للشمس، ويُنصح بإعادة تطبيقه كل ساعتين عند التواجد تحت الشمس المباشرة لفترات طويلة.</p>
<h3>هل يمكن استخدام هذا الكريم لتفتيح مناطق أخرى مثل الوجه؟</h3>
<p>هذا المنتج مصمم بتركيبة وقوام يلائم بشرة اليدين، وتوفر يورياج سيروم وكريم دبيدرم المخصصين للوجه للحصول على أفضل النتائج.</p>
<h3>هل يساعد الكريم في الوقاية من جفاف اليدين الناتج عن المعقمات؟</h3>
<p>نعم، يحتوي على مواد مرطبة ومياه حرارية تعوض الرطوبة المفقودة وتصلح حاجز الجلد المتضرر من المعقمات الكحولية.</p>
<h3>ما هو الدور الذي تلعبه مياه يورياج الحرارية في هذا المنتج؟</h3>
<p>مياه يورياج الحرارية غنية بالمعادن وتوفر خصائص مهدئة ومضادة للالتهاب، مما يمنع التهيج الذي قد يؤدي إلى تصبغ الجلد.</p>
<h3>هل يناسب الكريم الرجال والنساء؟</h3>
<p>نعم، المستحضر مناسب لكلا الجنسين وله عطر خفيف جداً ومحايد يناسب الاستخدام اليومي للجميع.</p>
<h3>ما هي سعة العبوة وهل هي مناسبة للحمل في الحقيبة؟</h3>
<p>تأتي العبوة بحجم 50 مل، وهو حجم مثالي وعملي جداً للحمل في حقيبة اليد أو السيارة للاستخدام المستمر طوال اليوم.</p>
<h3>هل يؤثر الكريم على طلاء الأظافر؟</h3>
<p>لا، الكريم لا يؤثر إطلاقاً على طلاء الأظافر أو سلامتها، بل يعزز ترطيب الجلد المحيط بالأظافر.</p>
<h3>هل يمكن استخدام الكريم خلال فترة الحمل أو الرضاعة؟</h3>
<p>تركيبة المنتج آمنة ولطيفة، ولكن يُفضل دائماً استشارة الطبيب المتابع أثناء فترة الحمل والرضاعة قبل استخدام منتجات التفتيح.</p>
<h3>ما الفرق بين كريم دبيدرم لليدين وكريمات اليدين العادية؟</h3>
<p>كريمات اليدين العادية توفر ترطيباً سطحي فقط، بينما كريم دبيدرم يجمع بين الترطيب الطبي والعلاج الفعال لتفتيح البقع والوقاية من الشمس بـ SPF 15.</p>
<h3>هل يحمي الكريم من علامات التجاعيد المبكرة على اليدين؟</h3>
<p>نعم، حماية الجلد من الأشعة فوق البنفسجية واحتوائه على مضادات الأكسدة يقللان من تكسر الكولاجين وظهور التجاعيد المبكرة.</p>
<h3>كيف أقوم بتخزين العبوة للحفاظ على جودتها؟</h3>
<p>احفظي العبوة مغلقة جيداً في درجة حرارة الغرفة (دون 25 مئوية) بعيداً عن مصادر الحرارة المباشرة والشمس.</p>
<h3>هل يحتوي كريم دبيدرم على البارابين؟</h3>
<p>تم اختبار المستحضر جلدياً وتطويره وفق أعلى المعايير الفرنسية الخالية من البارابين الضار بالبشرة.</p>
<h3>ما العمل إذا لامس الكريم العينين بالخطأ؟</h3>
<p>في حال ملامسة العينين، قومي بغسلهما فوراً بكمية وفيرة من الماء الفاتر النظيف حتى يزول أي شعور بالانزعاج.</p>
<h3>هل يسبب الكريم انسداد مسام الجلد؟</h3>
<p>لا، تركيبة الكريم خفيفة وغير مسببة لانسداد المسام (Non-comedogenic).</p>
<h3>هل يمكن تطبيق كريم آخر فوق كريم دبيدرم؟</h3>
<p>لا داعي لتطبيق كريم آخر لليدين فوقه، حيث يوفر دبيدرم التفتيح والترطيب والوقاية الشاملة بنفس الوقت.</p>
<h3>هل يمكن استخدامه للأطفال؟</h3>
<p>هذا المنتج مخصص للبالغين ابتداءً من عمر 18 عاماً لعلاج تصبغات اليدين.</p>
<h3>أين يتم تصنيع كريم يورياج دبيدرم؟</h3>
<p>يُصنع المستحضر في فرنسا بواسطة مختبرات يورياج الجلدية الشهيرة وتستورده صيدلية إكليل أبها مع ضمان الأصالة 100%. </p>`,
      "tags": ["uriage", "depiderm", "كريم_يدين", "تفتيح_البقع", "واقي_شمس", "إكليل_أبها"]
    },
    "en": {
      "title": "Uriage Dépiderm Brightening Hand Cream with SPF 15 - 50ml",
      "meta_title": "Uriage Dépiderm Brightening Hand Cream SPF 15 50ml | Ekleel",
      "meta_description": "Shop Uriage Dépiderm Brightening Hand Cream SPF 15 (50ml). Corrects dark spots, protects from UV rays, and deeply hydrates hands. 100% authentic at Ekleel Pharmacy.",
      "description": `<h2>Product Overview</h2>
<p>The <strong>Uriage Dépiderm Brightening Hand Cream with SPF 15 (50ml)</strong> is an advanced dermatological formula designed to target, correct, and fade hyperpigmentation and stubborn dark spots on the hands. Developed in Uriage's renowned French laboratories, this hand cream combines intense depigmenting action with daily SPF 15 broad-spectrum UVA/UVB protection to prevent new sun-induced spots from forming.</p>

<p>Featuring a lightweight, velvety texture, the cream absorbs quickly into the skin without leaving a greasy or sticky residue, allowing you to resume daily activities immediately after application. Enriched with legendary Uriage Thermal Water, it soothes sensitive skin, reinforces the cutaneous moisture barrier, and combats dry hands caused by frequent handwashing and alcohol-based sanitizers.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Corrects Dark Spots:</strong> Powered by Mela Technology to visibly reduce the size, color, and intensity of dark spots on the hands.</li>
  <li><strong>SPF 15 Sun Protection:</strong> Provides essential daily broad-spectrum UVA/UVB defense to prevent photoaging and spot recurrence.</li>
  <li><strong>Deep Hydration & Nourishment:</strong> Delivers long-lasting moisture to prevent dryness, cracking, and roughness caused by environmental stress.</li>
  <li><strong>Fast Absorption & Non-Greasy:</strong> Absorbs effortlessly without leaving oily marks on keyboards, phones, or handles.</li>
  <li><strong>Soothes Skin Irritation:</strong> Infused with Uriage Thermal Water and Enoxolone to calm sensitive skin and reduce micro-inflammation.</li>
  <li><strong>Evens Skin Tone:</strong> Restores youthful radiance and uniform clarity to the skin on the back of the hands with regular use.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Wash hands thoroughly with a mild cleanser and warm water, then gently pat dry with a clean towel.</li>
  <li><strong>Step 2:</strong> Dispense a pea-sized amount of Uriage Dépiderm Hand Cream onto the back of each hand.</li>
  <li><strong>Step 3:</strong> Massage gently over the back of the hands, fingers, and cuticles using smooth circular motions until fully absorbed.</li>
  <li><strong>Step 4:</strong> Reapply every 2-3 hours during prolonged sun exposure (such as driving) or immediately after washing hands.</li>
</ul>

<h2>Ingredients Overview</h2>
<p>Uriage Dépiderm Hand Cream incorporates cutting-edge French skincare technology:</p>
<ul>
  <li><strong>Mela Technology:</strong> A synergistic complex of Pea Extract, Sucrose, Uriage Thermal Water, and Vitamin C to inhibit tyrosinase enzyme activity.</li>
  <li><strong>Uriage Thermal Water:</strong> Pure mineral-rich thermal water that soothes inflammation, calms irritation, and strengthens the skin barrier.</li>
  <li><strong>Stabilized Vitamin C:</strong> A potent antioxidant that neutralizes free radicals, brightens hyperpigmentation, and boosts collagen synthesis.</li>
  <li><strong>Enoxolone:</strong> Anti-inflammatory active derived from licorice root that calms hyper-reactive skin tissue.</li>
  <li><strong>SPF 15 UV Filters:</strong> Balanced chemical and physical filters defending against sun-induced melanin overproduction.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external dermatological use on hands only. Avoid contact with eyes and mucous membranes.</li>
  <li>Do not apply on open wounds, severe cuts, or actively inflamed skin conditions.</li>
  <li>Store in a cool, dry place below 25°C, away from direct sunlight and excessive heat.</li>
  <li>If unexpected irritation or redness occurs, discontinue use and consult a dermatologist.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Individuals noticing age spots, sun spots, or uneven pigmentation on the back of their hands.</li>
  <li>People frequently exposed to sun during daily activities or driving who require brightening combined with UV protection.</li>
  <li>Anyone seeking a clinical hand treatment that offers anti-spot efficacy, UV protection, and luxurious daily hydration.</li>
</ul>`,
      "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Uriage</td></tr>
  <tr><th>Category</th><td>Skin Care / Hand Care</td></tr>
  <tr><th>Product Type</th><td>Depigmenting & Brightening Hand Cream</td></tr>
  <tr><th>Volume/Weight</th><td>50 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Including Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Radiant, Even-Toned & Non-Greasy</td></tr>
  <tr><th>Texture</th><td>Lightweight Velvety Cream</td></tr>
  <tr><th>Fragrance</th><td>Hypoallergenic Light Scent</td></tr>
  <tr><th>Active Ingredients</th><td>Mela Technology, Uriage Thermal Water, Vitamin C, SPF 15 Filters</td></tr>
  <tr><th>Country of Origin</th><td>France</td></tr>
  <tr><th>Manufacturer</th><td>Laboratoires Dermatologiques d'Uriage</td></tr>
  <tr><th>Age Group</th><td>Adults (18+)</td></tr>
</tbody>
</table>`,
      "knowledge_base": `<h2>Clinical Insights on Hand Hyperpigmentation & Sun Defense</h2>

<h3>What problem does this solve?</h3>
<p>Uriage Dépiderm Hand Cream solves hyperpigmentation, dark spots, and premature photoaging on the back of the hands. It reduces melanin concentration and prevents sun damage responsible for dark spot formation.</p>

<h3>Why does this condition happen?</h3>
<p>The skin on the back of the hands is thin and constantly exposed to environmental aggressors, especially ultraviolet (UV) radiation. UV exposure stimulates melanocytes via the tyrosinase enzyme, causing overproduction and clustering of melanin pigments known as sun spots or age spots. Frequent hand washing with harsh soaps degrades the natural lipid barrier, rendering the skin more vulnerable to oxidative stress and post-inflammatory hyperpigmentation (PIH).</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Daily Sun Protection:</strong> Apply broad-spectrum sun defense to hands every morning before stepping outside or driving.<br>
2. <strong>Protective Driving Gloves:</strong> Wear UV-protective gloves during long drives to shield hands from direct sunlight.<br>
3. <strong>Immediate Post-Wash Hydration:</strong> Apply moisturizing hand cream immediately after washing hands to seal in hydration.<br>
4. <strong>Gentle Cleansing:</strong> Avoid harsh sulfate cleansers and sanitizers that strip natural lipids from hand skin.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Dark spots on hands are purely an inevitable sign of aging and cannot be reversed topically."<br>
<strong>Fact:</strong> Dark spots are primarily caused by accumulated UV damage (photoaging). Clinical depigmenting creams containing active tyrosinase inhibitors, stabilized antioxidants, and SPF protection can effectively lighten existing spots and prevent new ones.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Uriage Dépiderm utilizes <strong>Mela Technology</strong> to regulate melanogenesis. Pea extract and sucrose inhibit tyrosinase activity, suppressing melanin synthesis at the cellular level. Stabilized Vitamin C oxidizes existing melanin deposits, visibly lightening dark spots. Integrated SPF 15 filters shield melanocytes from UV triggering, while Uriage Thermal Water attenuates micro-inflammation that contributes to hyperpigmentation recurrence.</p>`,
      "faqs": `<h3>What is Uriage Dépiderm Hand Cream and what are its main uses?</h3>
<p>Uriage Dépiderm Hand Cream is a clinical treatment designed to lighten dark spots on the hands, protect skin from sun damage with SPF 15, and provide intense, long-lasting hydration.</p>
<h3>Is this hand cream recommended while driving?</h3>
<p>Yes, highly recommended. Hands receive significant UV exposure through car windows; SPF 15 protection shields skin against sun spots while driving.</p>
<h3>How long does it take to see visible results in spot reduction?</h3>
<p>Initial visible lightening can be observed within 4 to 6 weeks of consistent twice-daily application alongside sun protection.</p>
<h3>Does Uriage Dépiderm contain hydroquinone or corticosteroids?</h3>
<p>No, it is completely free from hydroquinone and steroids. It relies on safe dermatological actives like Mela Technology, Vitamin C, and Uriage Thermal Water.</p>
<h3>Does it leave a greasy or sticky residue on hands?</h3>
<p>No, the formula features a lightweight, velvety texture that absorbs quickly without greasy residue, allowing instant use of touchscreens.</p>
<h3>Is it suitable for sensitive skin?</h3>
<p>Yes, it has been dermatologically tested on sensitive skin and enriched with soothing Uriage Thermal Water to prevent irritation.</p>
<h3>How many times a day should I apply this cream?</h3>
<p>Apply at least twice daily, and reapply after handwashing or during extended sun exposure for continuous protection.</p>
<h3>Does it treat age spots (liver spots) on hands?</h3>
<p>Yes, it effectively reduces age spots caused by accumulated UV exposure through targeted melanogenesis inhibition.</p>
<h3>Is SPF 15 sufficient for daily hand protection?</h3>
<p>SPF 15 offers excellent baseline protection for daily activities. Reapplication every 2 hours is advised during prolonged direct sunlight.</p>
<h3>Can this hand cream be applied to the face?</h3>
<p>It is specifically formulated for hand skin texture. For facial pigmentation, Uriage Dépiderm Facial Serum and Cream are recommended.</p>
<h3>Does it help relieve hand dryness from alcohol sanitizers?</h3>
<p>Yes, its hydrating lipids and thermal water rebuild the skin barrier damaged by frequent sanitizing.</p>
<h3>What role does Uriage Thermal Water play in the cream?</h3>
<p>Uriage Thermal Water is rich in trace elements that soothe micro-inflammation and strengthen skin defense against environmental stress.</p>
<h3>Is this product suitable for both men and women?</h3>
<p>Yes, it is unisex with a neutral, light fragrance suitable for daily use by both men and women.</p>
<h3>What is the size of the tube and is it travel-friendly?</h3>
<p>The 50ml tube size is compact and travel-friendly, making it easy to carry in hand bags or keep in the car.</p>
<h3>Will it alter or damage nail polish?</h3>
<p>No, the cream has no negative effect on nail polish or nail integrity; it hydrates the surrounding cuticles.</p>
<h3>Is it safe for pregnant or breastfeeding women?</h3>
<p>The ingredients are safe and gentle, but consulting your physician before starting any brightening regimen during pregnancy is recommended.</p>
<h3>How does Uriage Dépiderm differ from regular hand creams?</h3>
<p>Regular hand creams only hydrate, whereas Uriage Dépiderm actively fades dark spots, prevents melanin synthesis, and provides SPF 15 sun defense.</p>
<h3>Does it help prevent premature hand wrinkles?</h3>
<p>Yes, by shielding skin against UV damage and supplying antioxidants, it preserves collagen and prevents premature wrinkle formation.</p>
<h3>How should I store this product?</h3>
<p>Store tightly closed at room temperature below 25°C away from heat sources and direct sunlight.</p>
<h3>Does Uriage Dépiderm contain parabens?</h3>
<p>No, it is formulated without parabens in strict accordance with French dermatological standards.</p>
<h3>What should I do if the cream accidentally gets into my eyes?</h3>
<p>Rinse thoroughly with clean lukewarm water immediately until any discomfort subsides.</p>
<h3>Is it non-comedogenic?</h3>
<p>Yes, the formula is lightweight and non-comedogenic.</p>
<h3>Can I layer another cream over it?</h3>
<p>Layering another hand cream is unnecessary, as Uriage Dépiderm provides complete hydration, sun protection, and treatment in one.</p>
<h3>Can children use this cream?</h3>
<p>This product is formulated for adults (18+) dealing with hand hyperpigmentation.</p>
<h3>Where is Uriage Dépiderm Hand Cream manufactured?</h3>
<p>It is manufactured in France by Laboratoires Dermatologiques d'Uriage and imported directly by Ekleel Abha Pharmacy (100% genuine).</p>`,
      "tags": ["uriage", "depiderm", "hand_cream", "dark_spots", "spf15", "ekleel_abha"]
    },
    "schema": {
      "brand": "Uriage",
      "category": "Skin Care / Hand Care",
      "availability": "InStock"
    },
    "image_seo": {
      "image_filename": "uriage-depiderm-brightening-hand-cream-spf15-50ml.webp",
      "alt": "Uriage Dépiderm Brightening Hand Cream with SPF 15 - 50ml",
      "title": "Uriage Dépiderm Brightening Hand Cream with SPF 15 - 50ml"
    }
  },

  // ==========================================
  // PRODUCT 1435: QV Hand Cream 50g
  // ==========================================
  {
    "product_id": "1435",
    "sku": "EK-1435",
    "category": "العناية بالبشرة / العناية باليدين",
    "brand": "QV",
    "ar": {
      "title": "كريم اليدين كيو في - 50جم",
      "meta_title": "كريم اليدين كيو في لحماية وترطيب اليدين 50جم | صيدلية إكليل أبها",
      "meta_description": "احصلي على كريم اليدين كيو في (50جم) الترطيب الطبي الفائق للبشرة الجافة والحساسة. خالي من العطور والبارابين. أصلي 100% من إكليل أبها.",
      "description": `<h2>نظرة عامة على المنتج</h2>
<p>كريم اليدين كيو في <strong>(QV Hand Cream - 50g)</strong> هو كريم طبي مرطب وعلاجي فاخر مصمم خصيصاً لتوفير ترطيب مكثف وحماية فائقة لبشرة اليدين الجافة، الشديدة الجفاف، والحساسة. طور بواسطة مختبرات إيغو (Ego Pharmaceuticals) الأسترالية الشهيرة ليكون الحل الأمثل لاستعادة حيوية اليدين وتغذيتها بدون ترك أي ملمس دهني مزعج. يعمل هذا الكريم على بناء درع واقٍ يحبس الرطوبة داخل خلايا الجلد ويمنع فقدان الماء عبر البشرة (TEWL).</p>

<p>يمتاز كريم كيو في بتركيبة خالية تماماً من العطور، الألوان، اللانولين، البارابين، والبروبيلين غليكول، مما يجعله آمناً ولطيفاً حتى على البشرة المصابة بالحساسية، الأكزيما، أو الصدفية. بفضل حجمه المناسب (50 جم)، يمكنك حمله معك في كل مكان لحماية يديك من آثر الغسيل المتكرر والمعقمات الكحولية وتقلبات الطقس.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>ترطيب مكثف وعميق:</strong> يعوض الرطوبة المفقودة في طبقات الجلد السطحية والعميقة لمنع جفاف وتطرق اليدين.</li>
  <li><strong>تركيبة غير دهنية سريعة الامتصاص:</strong> يمتص بسرعة فائقة دون أن يترك طبقة لزجة، مما يسمح باستكمال الأعمال فوراً.</li>
  <li><strong>حماية خالية من المهيجات:</strong> خالٍ من العطور والصباغ واللانولين، مما يقلل احتمالية تهيج الجلد الحساس.</li>
  <li><strong>تعزيز حاجز البشرة الطبيعي:</strong> يحتوي على السكوالين والجليسرين لإعادة ترميم حواجز الجلد المتضررة.</li>
  <li><strong>مناسب لحالات الأكزيما والصدفية:</strong> تركيبة متوازنة الحموضة (pH balanced) توفر راحة فورية للجلد الملتهب.</li>
  <li><strong>مقاومة الجفاف الناتجة عن المعقمات:</strong> يمنع التشظي والجفاف الملازم للاستعمال المستمر للمطهرات الكحولية.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> نظفي يديكِ بماء فاتر وباستخدام غسول لطيف خالٍ من الصابون مثل منظف كيو في.</li>
  <li><strong>الخطوة الثانية:</strong> جففي اليدين بلطف بترك نسبة ضئيلة من الرطوبة على الجلد.</li>
  <li><strong>الخطوة الثالثة:</strong> ضعي كمية صغيرة من كريم اليدين كيو في على ظهر اليدين وادلكيهما بحركات دائرية ناعمة.</li>
  <li><strong>الخطوة الرابعة:</strong> دلكي الأصابع والأظافر والجلد المحيط بها بعناية حتى امتصاص الكريم كلياً. كوري الاستخدام بعد غسل اليدين وقبل النوم.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<p>تعتمد تركيبة كريم كيو في لليدين على مركبات متطورة عالية النقاء:</p>
<ul>
  <li><strong>السكوالين (Squalane):</strong> مكون طبيعي يحاكي الزيوت الطبيعية للبشرة، يمنحها نعومة فائقة ويرمم غشاء الخلية.</li>
  <li><strong>الجليسرين (Glycerin):</strong> مرطب هيدروفيلي يسحب الرطوبة من الجو ويحبسها داخل طبقات الجلد.</li>
  <li><strong>البرافين السائل والأبيض (Liquid & Soft White Paraffin):</strong> مركبات واقية تشكل طبقة حماية تمنع تبخر الماء.</li>
  <li><strong>تركيبة متوازنة الحموضة (pH 6):</strong> تحافظ على الحموضة الطبيعية للجلد لحمايته من نمو البكتيريا الضارة.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>يُستخدم مظهرياً على الجلد فقط، تجنبي ملامسة العينين مباشرة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان جاف بدرجة حرارة أقل من 30 درجة مئوية.</li>
  <li>في حال حدوث تهيج نادر أو حساسية لأي من المكونات، يوصى بإيقاف الاستخدام واستشارة الصيدلي أو الطبيب.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>للأشخاص الذين يعانون من جفاف اليدين الشديد والتشققات الناتجة عن أعمال المنزل أو غسل الأطباق.</li>
  <li>لأصحاب البشرة الحساسة أو المصابين بالأكزيما والصدفية والذين يبحثون عن مرطب خالٍ من العطور.</li>
  <li>للكوادر الطبية والممارسين الصحيين الذين يستخدمون معقمات اليدين بشكل مكثف يومياً.</li>
</ul>`,
      "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>QV (كيو في / إيغو)</td></tr>
  <tr><th>الفئة</th><td>العناية بالبشرة / العناية باليدين</td></tr>
  <tr><th>نوع المنتج</th><td>كريم يدين مرطب طبي</td></tr>
  <tr><th>الحجم/الوزن</th><td>50 جم</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>البشرة الجافة، التالفة، والحساسة جداً</td></tr>
  <tr><th>المظهر النهائي</th><td>أيدٍ ناعمة ورطبة بلمس ناعم بدون زيتية</td></tr>
  <tr><th>الملمس</th><td>كريم غني وخفيف بنفس الوقت</td></tr>
  <tr><th>العطر</th><td>خالٍ تماماً من العطور (Unscented)</td></tr>
  <tr><th>المكونات النشطة</th><td>السكوالين، الجليسرين، البرافين السائل</td></tr>
  <tr><th>بلد المنشأ</th><td>أستراليا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Ego Pharmaceuticals Pty Ltd</td></tr>
  <tr><th>الفئة العمرية</th><td>مناسب لجميع الأعمار (الرضع، الأطفال، البالغين)</td></tr>
</tbody>
</table>`,
      "knowledge_base": `<h2>الدليل الطبي الشامل لعلاج جفاف اليدين والأكزيما</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج كريم كيو في لليدين جفاف الجلد الشديد، التشققات الجليدية، الحكة، والتهيج الناتج عن تلف الحاجز الواقي للبشرة. كما يمنح اليدين الوقاية المستمرة من الجفاف الناجم عن المنظفات والمواد الكيميائية.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تفتقر بشرة اليدين إلى الغدد الدهنية المقارنة بمناطق الجسم الأخرى، مما يجعلها سريعة التأثر بالعوامل الخارجية. يؤدي الغسيل المتكرر بالماء الساخن والصابون القاسي أو استعمال المعقمات الكحولية إلى تذويب الدهون الطبيعية (الليبيدات) في الطبقة القرنية. هذا يتسبب في تبخر الماء بسرعة وحدوث تشققات دقيقة تسمح بمرور المهيجات والبكتيريا إلى داخل الجلد، مما ينتج عنه التهاب وأكزيما اليدين.</p>

<h3>نصائح وقائية</h3>
<p>1. <strong>تجنب الماء الساخن:</strong> غسل اليدين بماء فاتر بدلاً من الماء الساخن لمنع سلب الدهون الطبيعية.<br>
2. <strong>ارتداء القفازات الواقية:</strong> استخدام قفازات مطاطية مبطنة بالقطن أثناء تنظيف الأطباق والتعامل مع المواد الكيميائية.<br>
3. <strong>الترطيب الفوري:</strong> إبقاء عبوة كريم كيو في قرب المغسلة وتطبيق الكريم فور التنشيف مباشرة.<br>
4. <strong>تجنب المعقمات المعطرة:</strong> اختيار منتجات تعقيم لطيفة وتتبعها بالمرطب دائماً.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الكريمات الخالية من العطور لا تقدم ترطيباً كافياً مثل الكريمات الفاخرة ذات الروائح الزكية."<br>
<strong>الحقيقة:</strong> العطور هي السبب الأول لتهيج البشرة والجفاف اللاحق. التركيبات الخالية من العطور مثل كيو في تركز على المكونات الفعالة حيوياً مثل السكوالين والجليسرين لتوفير ترطيب طبي أعمق وأكثر أماناً.</p>

<h3>التفسير العلمي</h3>
<p>يعمل كريم كيو في عبر آلية مزدوجة تجمع بين <strong>الجذب والاحتجاز (Humectant & Occlusive Effect)</strong>. يقوم الجليسرين بجذب جزيئات الماء نحو الطبقة القرنية (Stratum Corneum)، بينما يشكل البرافين والسكوالين طبقة حماية عازلة شبه نفاذة تمنع تبخر الماء عبر الجلد بنسبة عالية. كما يساعد السكوالين في تجديد الليبيدات السطحية وتنعيم قشور الجلد الجاف دون سد المسام.</p>`,
      "faqs": `<h3>ما هو كريم كيو في لليدين وما مميزاته؟</h3>
<p>كريم كيو في لليدين هو كريم مرطب طبي خالٍ من العطور والمهيجات، مصمم لترطيب بشرة اليدين الجافة والحساسة وتغذيتها دون ترك ملمس دهني.</p>
<h3>هل ينصح باستخدام كريم كيو في لمرضى الأكزيما؟</h3>
<p>نعم، كريم كيو في مخصص وموصى به من أطباء الجلدية للمصابين بأكزيما اليدين والصدفية لكونه خالياً من العطور واللانولين ومواد التهيج.</p>
<h3>هل يترك كريم كيو في طبقة لزجة أو دهنية؟</h3>
<p>لا، يمتاز بتركيبة سريعة الامتصاص تمنح ترطيباً عميقاً وملمساً ناعماً ومريحاً دون لزوجة.</p>
<h3>هل يحتوي كريم كيو في على البارابين؟</h3>
<p>لا، المنتج خالٍ تماماً من البارابين، الألوان، العطور، والبروبيلين غليكول.</p>
<h3>كم مرة في اليوم يمكنني استخدام الكريم؟</h3>
<p>يمكنك استخدامه كلما دعت الحاجة، ويُفضل تطبيقه بعد كل غسيل لليدين وقبل النوم مباشرة للحصول على أفضل النتائج.</p>
<h3>هل كريم كيو في مناسب للأطفال والرضع؟</h3>
<p>نعم، تركيبة كيو في الطبية اللطيفة آمنة تماماً للاستخدام على بشرة الأطفال والرضع.</p>
<h3>ما هو المكون الأساسي الذي يمنح الكريم قدرته على التهدئة؟</h3>
<p>يحتوي الكريم على السكوالين الطبيعي والجليسرين، وهما مكونان يعيدان مرونة الجلد ويرممان الحاجز الواقي.</p>
<h3>هل يساعد كريم كيو في تقوية الأظافر والجلد المحيط بها؟</h3>
<p>نعم، تدليك الأظافر والجلد المحيط بها بالكريم يمنع جفاف التشققات ويحافظ على مرونة الأظافر ورطوبتها.</p>
<h3>هل يعالج التشققات الشديدة في اليدين؟</h3>
<p>نعم، يوفر كريم كيو في ترطيباً علاجياً مكثفاً يسرع التئام التشققات الجلدية الناتجة عن الجفاف الشديد.</p>
<h3>هل يمكن استخدام هذا الكريم للوجه؟</h3>
<p>كريم اليدين مصمم خصيصاً لبشرة اليدين، بينما توفر كيو في كريم الوجه المخصص (QV Face Cream) المتلائم مع مسام الوجه.</p>
<h3>هل يناسب المستحضر أصحاب البشرة الدهنية؟</h3>
<p>المستحضر مخصص لليدين والجفاف، واليدين نادراً ما تكون دهنية، لذا فهو ممتاز للجميع.</p>
<h3>ما هو حجم العبوة وهل هي عملية للتنقل؟</h3>
<p>تأتي العبوة بحجم 50 جم، وهو حجم مثالي يسهل وضعه في حقيبة اليد أو الجيب أو السيارة.</p>
<h3>هل يمنع الكريم تأثير المعقمات الكحولية على اليدين؟</h3>
<p>نعم، استخدامه بعد المعقمات يعوض الزيوت الطبيعية التي أزالها الكحول ويعيد توازن الرطوبة.</p>
<h3>هل يحتوي الكريم على الكورتيزون؟</h3>
<p>لا، كريم كيو في مرطب طبي خالٍ تماماً من الكورتيزون والأدوية الهرمونية.</p>
<h3>هل تم اختبار كريم كيو في من قبل أطباء الجلدية؟</h3>
<p>نعم، جميع منتجات كيو في يتم تطويرها واختبارها سريرياً بواسطة مختبرات إيغو الأسترالية المتخصصة.</p>
<h3>هل المنتج نباتي ولم يختبر على الحيوانات؟</h3>
<p>نعم، منتجات كيو في لا تحتوي على مشتقات حيوانية خالية من العنف ضد الحيوانات.</p>
<h3>ما هي مدة صلاحية كريم كيو في بعد الفتح؟</h3>
<p>تكون الصلاحية عادة 12 إلى 24 شهراً من تاريخ الفتح الموضح على رمز العبوة.</p>
<h3>كيف يختلف كريم كيو في عن مرطبات اليدين التجارية؟</h3>
<p>المرطبات التجارية تحتوي غالباً على عطور وكحول تسبب التهيج، بينما كيو في تركيبة علاجية خالية من المهيجات تمنح ترطيباً حقيقياً.</p>
<h3>هل يمكن استخدامه أثناء فصل الشتاء لمنع جفاف البرد؟</h3>
<p>نعم، هو الخيار الأول للحماية من جفاف اليدين وتشققات البرد في فصل الشتاء.</p>
<h3>هل يمكن للمرأة الحامل استخدام كريم كيو في بأمان؟</h3>
<p>نعم، التركيبة آمنة تماماً ومناسبة للاستخدام خلال فترتي الحمل والرضاعة.</p>
<h3>هل يساعد كريم كيو في تخفيف حكة اليدين الجافة؟</h3>
<p>نعم، يهدئ الحكة فورياً عبر إعادة ترطيب الأنسجة المتهيجة وتلطيفها.</p>
<h3>كيف أقوم بتخزين العبوة بشكل صحيح؟</h3>
<p>احفظ العبوة مغلقة في مكان بارد وجاف بدرجة حرارة أقل من 30 درجة مئوية بعيداً عن الشمس.</p>
<h3>ماذا أفعل إذا لامس الكريم العينين؟</h3>
<p>اغسلي العينين جيداً بماء فاتر نظيف لمحي أي أثر بالكريم.</p>
<h3>هل يسبب كريم كيو في انسداد المسام؟</h3>
<p>لا، تركيبة الكريم خفيفة ومصممة لعدم سد المسام (Non-comedogenic).</p>
<h3>أين يُصنع كريم اليدين كيو في؟</h3>
<p>يُصنع بفخر في أستراليا بواسطة Ego Pharmaceuticals وتوفر صيدلية إكليل أبها المنتج الأصلي 100%. </p>`,
      "tags": ["qv", "كريم_يدين", "كيو_في", "ترطيب_البشرة", "أكزيما", "إكليل_أبها"]
    },
    "en": {
      "title": "QV Hand Cream - 50g",
      "meta_title": "QV Hand Cream 50g Intense Moisture for Dry Hands | Ekleel",
      "meta_description": "Buy QV Hand Cream (50g) for dry and sensitive hands. Fragrance-free, lanolin-free, non-greasy medical hydration formula. 100% genuine at Ekleel Pharmacy.",
      "description": `<h2>Product Overview</h2>
<p><strong>QV Hand Cream (50g)</strong> is a clinically formulated, rich moisturizing cream designed to deliver intense hydration and skin-barrier protection for dry, very dry, and sensitive hand skin. Developed by Australia's renowned Ego Pharmaceuticals, this luxurious yet non-greasy hand cream restores hand softness and combats rough, cracked skin without leaving an uncomfortable sticky feel.</p>

<p>Formulated without fragrance, color, lanolin, parabens, or propylene glycol, QV Hand Cream is exceptionally gentle and safe for skin prone to eczema, dermatitis, or psoriasis. Its handy 50g tube makes it convenient to carry anywhere, ensuring your hands stay nourished and shielded from frequent handwashing, harsh detergents, and sanitizers throughout the day.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Intense Deep Hydration:</strong> Replenishes lost moisture to heal dry, rough, and chafed hand skin.</li>
  <li><strong>Non-Greasy & Fast Absorbing:</strong> Absorbs quickly into skin without leaving oily residue on objects or screen surfaces.</li>
  <li><strong>Irritant-Free Defense:</strong> Free from perfume, color, and lanolin to minimize risk of allergic skin reactions.</li>
  <li><strong>Restores Natural Skin Barrier:</strong> Enriched with Squalane and Glycerin to rebuild weakened cutaneous lipids.</li>
  <li><strong>Eczema & Psoriasis Friendly:</strong> pH-balanced formula (pH 6) provides instant soothing relief to inflamed skin.</li>
  <li><strong>Protects Against Sanitizer Dryness:</strong> Counteracts the stripping effects of alcohol-based sanitizers and soap.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Cleanse hands gently with warm water and a soap-free wash like QV Wash.</li>
  <li><strong>Step 2:</strong> Gently pat hands dry, leaving a hint of dampness on the skin surface.</li>
  <li><strong>Step 3:</strong> Apply a small amount of QV Hand Cream to the back of your hands.</li>
  <li><strong>Step 4:</strong> Smooth over hands, fingers, and cuticles in gentle circular motions until fully absorbed. Reapply as needed after washing.</li>
</ul>

<h2>Ingredients Overview</h2>
<p>QV Hand Cream relies on high-purity dermatological actives:</p>
<ul>
  <li><strong>Squalane:</strong> A natural component of skin sebum that softens skin, repairs barrier lipids, and enhances elasticity.</li>
  <li><strong>Glycerin:</strong> A humectant that draws water into the stratum corneum, ensuring deep moisture retention.</li>
  <li><strong>Liquid & Soft White Paraffin:</strong> Protective emollients forming an occlusive layer that prevents transepidermal water loss (TEWL).</li>
  <li><strong>pH-Balanced Formula (pH 6):</strong> Matches natural skin acidity to maintain healthy microflora and skin defense.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For external dermatological use only. Avoid contact with eyes.</li>
  <li>Keep out of reach of children. Store below 30°C in a cool, dry place.</li>
  <li>If irritation occurs, discontinue use and consult your healthcare professional.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Individuals suffering from severe hand dryness, cracking, or irritation due to housework or chemical exposure.</li>
  <li>People with sensitive skin, eczema, or psoriasis seeking a fragrance-free clinical moisturizer.</li>
  <li>Healthcare workers and professionals who frequently wash and sanitize their hands daily.</li>
</ul>`,
      "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>QV (Ego)</td></tr>
  <tr><th>Category</th><td>Skin Care / Hand Care</td></tr>
  <tr><th>Product Type</th><td>Medical Moisturizing Hand Cream</td></tr>
  <tr><th>Volume/Weight</th><td>50 g</td></tr>
  <tr><th>Skin/Hair Type</th><td>Dry, Very Dry & Sensitive Skin</td></tr>
  <tr><th>Finish</th><td>Soft, Hydrated & Non-Sticky</td></tr>
  <tr><th>Texture</th><td>Rich Cream</td></tr>
  <tr><th>Fragrance</th><td>Fragrance-Free (Unscented)</td></tr>
  <tr><th>Active Ingredients</th><td>Squalane, Glycerin, Liquid Paraffin</td></tr>
  <tr><th>Country of Origin</th><td>Australia</td></tr>
  <tr><th>Manufacturer</th><td>Ego Pharmaceuticals Pty Ltd</td></tr>
  <tr><th>Age Group</th><td>All Ages (Infants, Children, Adults)</td></tr>
</tbody>
</table>`,
      "knowledge_base": `<h2>Clinical Insights on Hand Dermatitis & Skin Moisture Barrier</h2>

<h3>What problem does this solve?</h3>
<p>QV Hand Cream resolves severe hand dryness, cracked skin, itching, and irritant contact dermatitis. It repairs the damaged skin barrier and prevents moisture loss caused by harsh soap and alcohol sanitizers.</p>

<h3>Why does this condition happen?</h3>
<p>The skin on our hands contains fewer sebaceous glands than facial skin. Frequent handwashing, exposure to dishwashing detergents, cold weather, and alcohol sanitizers dissolve natural surface lipids (ceramides and squalene). This degrades the stratum corneum, allowing rapid water evaporation (TEWL) and entry of irritants, leading to redness, cracking, and eczema flare-ups.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Avoid Hot Water:</strong> Wash hands with lukewarm water rather than hot water to prevent lipid depletion.<br>
2. <strong>Wear Protective Gloves:</strong> Use cotton-lined rubber gloves when cleaning or doing dishes.<br>
3. <strong>Immediate Moisturization:</strong> Keep QV Hand Cream by every sink and apply immediately after drying hands.<br>
4. <strong>Use Soap-Free Cleansers:</strong> Switch from harsh alkaline soaps to pH-balanced soap-free washes.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Fragranced creams provide better nourishment than plain fragrance-free medical creams."<br>
<strong>Fact:</strong> Synthetic fragrances and essential oils are major causes of skin sensitization and contact dermatitis. Fragrance-free formulas like QV focus purely on bioactive emollients like squalane to repair skin safely.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>QV Hand Cream utilizes a synergistic <strong>Humectant-Occlusive Mechanism</strong>. Glycerin attracts water molecules into the stratum corneum, while paraffin and squalane form a flexible hydrophobic seal over the skin. This dual action traps moisture, restores inter-cellular lipid bilayers, and soothes cutaneous nerve endings to stop itching and scaling.</p>`,
      "faqs": `<h3>What is QV Hand Cream and what are its key features?</h3>
<p>QV Hand Cream is a fragrance-free, dermatologist-recommended moisturizer formulated to nourish dry, sensitive hands without leaving a greasy residue.</p>
<h3>Is QV Hand Cream safe for eczema sufferers?</h3>
<p>Yes, it is specially formulated and recommended by dermatologists for skin prone to eczema, psoriasis, and contact dermatitis due to its irritant-free formula.</p>
<h3>Does QV Hand Cream leave hands feeling greasy?</h3>
<p>No, it features a fast-absorbing cream texture that deeply hydrates while leaving hands soft and comfortable without greasy residue.</p>
<h3>Does it contain parabens or fragrances?</h3>
<p>No, QV Hand Cream is 100% free from fragrances, colors, parabens, lanolin, and propylene glycol.</p>
<h3>How often can I use QV Hand Cream during the day?</h3>
<p>You can use it as often as needed. Applying after every hand wash and before sleeping provides maximum therapeutic results.</p>
<h3>Is it suitable for infants and children?</h3>
<p>Yes, its clinical, gentle formulation is completely safe for infants, children, and adults of all ages.</p>
<h3>What active ingredients give QV its soothing effect?</h3>
<p>Squalane (a natural skin lipid derivative) and Glycerin work together to restore skin elasticity and reinforce barrier lipids.</p>
<h3>Does it help strengthen nails and cuticles?</h3>
<p>Yes, massaging QV Hand Cream into cuticles prevents dry hangnails and keeps nail plates hydrated and resilient.</p>
<h3>Can it heal deep cracks on hands?</h3>
<p>Yes, regular application delivers intense therapeutic moisture that accelerates healing of painful dry hand cracks.</p>
<h3>Can I use this cream on my face?</h3>
<p>While safe, QV offers specialized facial moisturizers (QV Face) formulated specifically for facial pore dynamics.</p>
<h3>Is this cream suitable for oily skin?</h3>
<p>It is designed for dry hands; hand skin rarely experiences oiliness, so it is ideal for universal hand care.</p>
<h3>What is the package size and is it portable?</h3>
<p>The 50g tube is compact, lightweight, and perfectly portable for purses, pockets, or car storage.</p>
<h3>Does it protect hands against alcohol sanitizer dryness?</h3>
<p>Yes, applying QV after sanitizing replaces lost natural oils and neutralizes alcohol dryness.</p>
<h3>Does QV Hand Cream contain cortisone or steroids?</h3>
<p>No, it is a non-medicated, steroid-free emollient moisturizer.</p>
<h3>Has QV Hand Cream been clinically tested?</h3>
<p>Yes, all QV products are clinically formulated and dermatologically tested by Ego Pharmaceuticals in Australia.</p>
<h3>Is QV Hand Cream vegan and cruelty-free?</h3>
<p>Yes, QV products do not contain animal-derived ingredients and are cruelty-free.</p>
<h3>What is the shelf life after opening?</h3>
<p>The shelf life is typically 12 to 24 months after opening, as indicated by the PAO symbol on the packaging.</p>
<h3>How does QV differ from cosmetic hand lotions?</h3>
<p>Cosmetic lotions often contain synthetic perfumes and alcohol that irritate skin, whereas QV is a clinical, irritant-free barrier treatment.</p>
<h3>Is it ideal for winter hand care?</h3>
<p>Yes, it is an essential winter skincare product to protect hands against cold weather chapping and dryness.</p>
<h3>Is it safe for use during pregnancy?</h3>
<p>Yes, it is completely safe for use during pregnancy and breastfeeding.</p>
<h3>Does it soothe itchy dry hands?</h3>
<p>Yes, it rapidly calms itchiness by rehydrating dried, irritated nerve endings in the skin barrier.</p>
<h3>How should I store QV Hand Cream?</h3>
<p>Store in a cool, dry place below 30°C, away from direct heat and sunlight.</p>
<h3>What if the cream accidentally contacts the eyes?</h3>
<p>Rinse thoroughly with clean lukewarm water until any mild irritation clears.</p>
<h3>Is QV Hand Cream non-comedogenic?</h3>
<p>Yes, it is light, gentle, and non-comedogenic.</p>
<h3>Where is QV Hand Cream manufactured?</h3>
<p>It is manufactured in Australia by Ego Pharmaceuticals and distributed authentically by Ekleel Abha Pharmacy.</p>`,
      "tags": ["qv", "hand_cream", "dry_skin", "moisturizer", "eczema", "ekleel_abha"]
    },
    "schema": {
      "brand": "QV",
      "category": "Skin Care / Hand Care",
      "availability": "InStock"
    },
    "image_seo": {
      "image_filename": "qv-hand-cream-50g.webp",
      "alt": "QV Hand Cream 50g",
      "title": "QV Hand Cream - 50g"
    }
  },

  // ==========================================
  // PRODUCT 1436: Green Tea Mouthwash 250ml
  // ==========================================
  {
    "product_id": "1436",
    "sku": "EK-1436",
    "category": "العناية بالفم / غسول الفم",
    "brand": "Listerine",
    "ar": {
      "title": "غسول الفم بالشاي الأخضر 250 مل",
      "meta_title": "غسول الفم بالشاي الأخضر 250 مل لحماية اللثة والأسنان | إكليل أبها",
      "meta_description": "تسوق غسول الفم بالشاي الأخضر 250 مل لحماية الأسنان من التسوس وتقوية اللثة والقضاء على رائحة الفم. خالي من الكحول. منتج أصلي 100% من صيدلية إكليل أبها.",
      "description": `<h2>نظرة عامة على المنتج</h2>
<p>غسول الفم بالشاي الأخضر سعة 250 مل <strong>(Green Tea Mouthwash 250ml)</strong> هو غسول طبيعي وطبي متطور مخصص للعناية اليومية المتكاملة بصحة الفم، الأسنان، واللثة. يجمع هذا الغسول الفريد بين قوة مستخلص الشاي الأخضر الطبيعي الغني بمضادات الأكسدة ومركب الفلورايد المقوي لمينا الأسنان، ليمنحك فماً نظيفاً وانتعاشاً طبيعياً يمتد لطوال اليوم دون الحرقة المزعجة الناتجة عن الغسولات التقليدية المعتمدة على الكحول.</p>

<p>تم تطوير هذا الغسول ليكون خاليًا من الكحول وطيف المواد الكيميائية القاسية، مما يجعله الخيار المثالي للأشخاص الذين يعانون من حساسية الفم أو جفاف الفم (Xerostomia). يعمل الغسول على اختراق الأماكن الدقيقة بين الأسنان وحافة اللثة التي لا تصل إليها الفرشاة التقليدية، متخلصاً من البكتيريا المسببة لطبقة البلاك (التراكمات الجيرية) ورائحة الفم الكريهة مع الحفاظ على التوازن البيولوجي الطبيعي لبيئة الفم.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>تعزيز صحة اللثة:</strong> يحتوي على مضادات الأكسدة (البوليفينول) في الشاي الأخضر التي تهدئ التهابات اللثة وتحد من النزيف.</li>
  <li><strong>مقاومة التسوس وتقوية المينا:</strong> مدعم بمركب الفلورايد الفعال لإعادة معدنة مينا الأسنان وحمايتها من حمض البكتيريا.</li>
  <li><strong>القضاء على البكتيريا ورائحة الفم:</strong> يقتل البكتيريا اللاهوائية المسببة للبخر الفموي ويمنح نفساً منعشاً بنكهة الشاي الأخضر.</li>
  <li><strong>تركيبة خالية من الكحول:</strong> ينظف الفم بعمق دون أن يسبب شعور الحرقة أو يسبب جفاف اللعاب.</li>
  <li><strong>الوصول للأماكن الصعبة:</strong> ينظف الفراغات بين الأسنان والجيوب اللثوية التي يتعذر على فرشاة الأسنان الوصول إليها.</li>
  <li><strong>تقليل تراكم طبقة البلاك:</strong> يمنع تشكل الطبقة الجرثومية اللزجة على الأسنان ويحافظ على بياضها الطبيعي.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى:</strong> قم بتنظيف أسنانك بالفرشاة والمعجون كالمعتاد قبل استخدام الغسول.</li>
  <li><strong>الخطوة الثانية:</strong> اسكب 20 مل (حوالي ملعقة كبيرة أو ملء غطاء العبوة) من غسول الشاي الأخضر دون تخفيفه بالماء.</li>
  <li><strong>الخطوة الثالثة:</strong> مضمض الفم جيداً بالسائل لمدة 30 إلى 60 ثانية لضمان وصوله إلى جميع زوايا الفم واللثة.</li>
  <li><strong>الخطوة الرابعة:</strong> ابصق السائل بالكامل. تجنب تناول الطعام أو الشراب أو غسل الفم بالماء لمدة 30 دقيقة للحصول على أفضل النتائج.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<p>يعتمد غسول الفم بالشاي الأخضر على تركيبة متوازنة ومتطورة:</p>
<ul>
  <li><strong>مستخلص الشاي الأخضر (Camellia Sinensis):** غني بكاتيشينات EGCG ذات الخصائص القوية المضادة للبكتيريا والالتهاب.</li>
  <li><strong>فلورايد الصوديوم (Sodium Fluoride):** يوفر حماية فائقة لمينا الأسنان ويعزز مقاومة الأحماض التآكلية.</li>
  <li><strong>المنثول الطبيعي (Menthol):** يمنح شعوراً ثلجياً بالانتعاش ونظافة الفم المستمرة.</li>
  <li><strong>زيوت مطهرة أساسية:</strong> تساعد في تفكيك غشاء البلاك الجرثومي بطريقة لطيفة على الأغشية المخاطية.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>هذا المنتج مخصص للمضمضة الفموية فقط، ويُمنع ابتلاعه كلياً.</li>
  <li>غير مناسب للأطفال دون سن 6 سنوات إلا تحت إشراف طبي أو إشراف البالغين.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد وجاف بعيداً عن أشعة الشمس المباشرة.</li>
  <li>إذا لاحظت تهيجاً في أغشية الفم أو ظهور تقرحات، توقف عن الاستخدام واستشر طبيب الأسنان.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>للأشخاص الذين يفضلون الغسولات الطبيعية الخالية من الكحول ولا يتحملون الحرقة المزعجة.</li>
  <li>لمن يعانون من التهابات اللثة الخفيفة، النزيف عند التفريش، أو تراكم البلاك السريع.</li>
  <li>لكل من يبحث عن نفس منعش ورعاية متكاملة للأسنان وحمايتها من التسوس يومياً.</li>
</ul>`,
      "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>Listerine / Green Tea Care</td></tr>
  <tr><th>الفئة</th><td>العناية بالفم / غسول الفم</td></tr>
  <tr><th>نوع المنتج</th><td>غسول فم طبيعي خالي من الكحول</td></tr>
  <tr><th>الحجم/الوزن</th><td>250 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>غير مطبق (مخصص للعناية بالفم)</td></tr>
  <tr><th>المظهر النهائي</th><td>نفس منعش ولثة صحية وأسنان محمية</td></tr>
  <tr><th>الملمس</th><td>سائل شفاف</td></tr>
  <tr><th>العطر</th><td>نكهة الشاي الأخضر والنعناع المنعش</td></tr>
  <tr><th>المكونات النشطة</th><td>مستخلص الشاي الأخضر، فلورايد الصوديوم، المنثول</td></tr>
  <tr><th>بلد المنشأ</th><td>المملكة المتحدة / إيطاليا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Johnson & Johnson / Kenvue</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والأطفال فوق 6 سنوات</td></tr>
</tbody>
</table>`,
      "knowledge_base": `<h2>الدليل المعرفي لصحة الفم وتقنيات الشاي الأخضر</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج غسول الفم بالشاي الأخضر تراكم البكتيريا المسببة لتسوس الأسنان، التهاب اللثة (Gingivitis)، ورائحة الفم الكريهة. كما يقضي على البيئة الحمضية التي تضعف مينا الأسنان وتؤدي لتآكلها.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>تتغذى البكتيريا الفموية على بقايا السكريات والنشويات المترسبة بين الأسنان، وتنتج أحماضاً تهاجم المينا وتسبب تسوس الأسنان. كما تؤدي غشاء البلاك الجرثومي المتراكم عند خط اللثة إلى تحفيز استجابة مناعية التهابية تظهر على شكل احمرار ونزيف في اللثة. استخدام الغسولات الكحولية القاسية قد يزيد الجفاف ويخل بتوازن الميكروبيوم الطبيعي للفم.</p>

<h3>نصائح وقائية</h3>
<p>1. <strong>المضمضة يومياً:</strong> المضمضة بغسول خالي من الكحول مرتين يومياً بعد تفريش الأسنان.<br>
2. <strong>استخدام خيط الأسنان:</strong> تنظيف الفواصل بين الأسنان بالخيط الطبي يومياً.<br>
3. <strong>تقليل السكريات:</strong> الحد من تناول الأطعمة والمشروبات السكرية التي تغذي البكتيريا.<br>
4. <strong>زيارة طبيب الأسنان:</strong> إجراء فحص وتنظيف دوري كل 6 أشهر.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "الغسولات الطبيعية مثل غسول الشاي الأخضر أقل فعالية في قتل البكتيريا مقارنة بالغسولات الكحولية."<br>
<strong>الحقيقة:</strong> أثبتت الدراسات العلمية أن بوليفينولات الشاي الأخضر توفر خصائص مضادة للبكتيريا توازي المواد الكيميائية القاسية دون أن تتسبب في جفاف الفم أو اضطراب بيئة الفم الطبيعية.</p>

<h3>التفسير العلمي</h3>
<p>تتميز كاتيشينات الشاي الأخضر (أبرزها EGCG) بقدرتها على التثبيط المباشر لإنزيم Glucosyltransferase الذي تستخدمه بكتيريا Streptococcus mutans للالتصاق بالأسنان وتكوين البلاك. كما يفرز فلورايد الصوديوم أيونات الفلورايد التي تتفاعل مع هيدروكسي أباتيت المينا لترميم أيونات الكالسيوم وإعادة بناء بلورات الفلوراباتيت الأكثر مقاومة للأحماض.</p>`,
      "faqs": `<h3>ما هي فوائد غسول الفم بالشاي الأخضر 250 مل؟</h3>
<p>يوفر غسول الشاي الأخضر حماية فائقة ضد التسوس بفضل الفلورايد، يهدئ اللثة بمضادات الأكسدة، ويقضي على رائحة الفم الكريهة دون حرقة الكحول.</p>
<h3>هل يحتوي هذا الغسول على الكحول؟</h3>
<p>لا، الغسول خالي تماماً من الكحول، مما يجعله لطيفاً على الفم ولا يسبب جفاف اللعاب أو شعور الحرقة.</p>
<h3>كم مرة يُنصح باستخدام غسول الفم الشاي الأخضر في اليوم؟</h3>
<p>يُنصح باستخدامه مرتين يومياً (صباحاً ومساءً) بعد التفريش بالفرشاة والمعجون.</p>
<h3>هل يمكن للأطفال استخدام هذا الغسول؟</h3>
<p>نعم، هو مناسب للأطفال ابتداءً من سن 6 سنوات شريطة قدرة الطفل على المضمضة والبصق دون ابتلاع السائل.</p>
<h3>كيف يختلف غسول الشاي الأخضر عن غسولات الفم العادية؟</h3>
<p>يحتوي على مضادات أكسدة طبيعية من الشاي الأخضر تعمل على تهادئة اللثة وتقليل البكتيريا بأسلوب لطيف وخالٍ من الكحول.</p>
<h3>هل يساعد الغسول في تقليل نزيف اللثة؟</h3>
<p>نعم، مضادات الأكسدة والالتهاب في الشاي الأخضر تساعد بشكل ملموس في تقليل احمرار ونزيف اللثة الملتهبة.</p>
<h3>ما هي السعة وحجم العبوة؟</h3>
<p>تأتي العبوة بسعة 250 مل، وهي سعة عملية تكفي للاستخدام اليومي المستمر لعدة أسابيع.</p>
<h3>هل يسبب الغسول تصبغ الأسنان؟</h3>
<p>لا، تركيبة الغسول مصممة طبياً لعدم ترك أي تصبغات على مينا الأسنان.</p>
<h3>ما هي الجرعة المناسبة للمضمضة في كل مرة؟</h3>
<p>الجرعة الموصى بها هي 20 مل (ما يعادل ملاءة غطاء العبوة) دون تخفيف بالماء.</p>
<h3>هل يجب غسل الفم بالماء بعد استخدام الغسول؟</h3>
<p>لا، ينبغي بصق السائل فقط وعدم المضمضة بالماء لمدة 30 دقيقة لضمان بقاء الفلورايد والمكونات الفعالة على الأسنان.</p>
<h3>هل يمنع الغسول تكون التكلسات والجير؟</h3>
<p>نعم، يعطل تشكل غشاء البلاك الجرثومي الأول، مما يقلل بشكل كبير من صلابة وتكون التكلسات الجيرية.</p>
<h3>هل يساعد الغسول في علاج رائحة الفم الصباحية؟</h3>
<p>نعم، استخدامه قبل النوم يقلل من نشاط البكتيريا اللاهوائية ليلاً ويضمن استيقاظك بنفَس منعش.</p>
<h3>هل يناسب أصحاب الفم الجاف؟</h3>
<p>نعم، تركيبته الخالية من الكحول تجعله مناسباً وآمناً لمصابي جفاف الفم.</p>
<h3>ماذا أفعل إذا ابتلعت كمية صغيرة من الغسول بالخطأ؟</h3>
<p>ابتلاع كمية بسيطة جداً لا يشكل خطورة، اشرب قليلاً من الماء، ولكن احرص على عدم الابتلاع مستقبلاً.</p>
<h3>هل يمكن استخدام الغسول أثناء ارتداء تقويم الأسنان؟</h3>
<p>نعم، هو ممتاز لمستخدمي تقويم الأسنان لتنظيف الزوايا الصعبة التي تعجز الفرشاة عن الوصول إليها.</p>
<h3>هل يتعارض الغسول مع حشوات الأسنان أو التلبيسات؟</h3>
<p>لا يتعارض إطلاقاً، بل يحمي حواف الحشوات والتلبيسات من التسوس الثانوي.</p>
<h3>هل المنتج نباتي؟</h3>
<p>نعم، تركيبة الغسول تعتمد على خلاصة نبات الشاي الأخضر ومكونات آمنة.</p>
<h3>ما هي نكهة الغسول وهل هي قوية؟</h3>
<p>يتميز بنكهة الشاي الأخضر المنعشة والممتزجة بالنعناع الخفيف دون أي طعم قاسي.</p>
<h3>هل يساعد الغسول في تقوية المينا الحساسة؟</h3>
<p>نعم، يحتوي على فلورايد الصوديوم الذي يعيد معدنة المينا ويخفف حساسية الأسنان.</p>
<h3>كيف يتم تخزين العبوة للحفاظ على جودتها؟</h3>
<p>احفظ العبوة مغلقة في درجة حرارة الغرفة دون 30 مئوية بعيداً عن ضوء الشمس المباشر.</p>
<h3>هل يناسب الحوامل والمرضعات؟</h3>
<p>نعم، يعتبر آمناً للاستخدام الظاهري الفموي للحوامل والمرضعات.</p>
<h3>هل الغسول يغني عن تفريش الأسنان بالفرشاة؟</h3>
<p>لا، الغسول مكمل للتفريش ولا يغني عن إزالة البلاك ميكانيكياً بواسطة الفرشاة.</p>
<h3>ما هي الصلاحية بعد فتح العبوة؟</h3>
<p>تستمر الصلاحية عادة حتى 12 شهراً من تاريخ الفتح.</p>
<h3>أين يتم تصنيع هذا الغسول؟</h3>
<p>يتم تصنيعه وفق أعلى معايير السلامة والأمان وتوفره صيدلية إكليل أبها مع ضمان الجودة 100%. </p>`,
      "tags": ["غسول_فم", "شاي_أخضر", "صحة_الفم", "خالي_كحول", "إكليل_أبها"]
    },
    "en": {
      "title": "Green Tea Mouthwash 250ml",
      "meta_title": "Green Tea Mouthwash 250ml Alcohol-Free Oral Care | Ekleel",
      "meta_description": "Buy Green Tea Mouthwash 250ml. Protects gums, strengthens enamel with fluoride, and eliminates bad breath naturally. Alcohol-free. Fast delivery at Ekleel Pharmacy.",
      "description": `<h2>Product Overview</h2>
<p><strong>Green Tea Mouthwash (250ml)</strong> is an advanced clinical oral rinse formulated with natural Green Tea extract and essential Sodium Fluoride for comprehensive daily dental and gum care. Combining the powerful botanical antioxidant properties of green tea with enamel-strengthening fluoride, this mouthwash cleanses deep within the oral cavity without the intense burn associated with traditional alcohol-containing rinses.</p>

<p>Specially developed to be 100% alcohol-free, it is exceptionally gentle and ideal for individuals with sensitive gums or dry mouth (Xerostomia). The rinse penetrates hard-to-reach interdental spaces and along the gumline where toothbrushes cannot reach, effectively neutralizing plaque-causing bacteria and bad breath while maintaining healthy oral microflora balance.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>Promotes Healthy Gums:</strong> Enriched with Green Tea polyphenols (EGCG) that soothe gum tissue and reduce inflammation.</li>
  <li><strong>Enamel Protection & Cavity Defense:</strong> Contains active Sodium Fluoride to remineralize tooth enamel and guard against acid erosion.</li>
  <li><strong>Eliminates Odor & Plaque Bacteria:</strong> Targets anaerobic bacteria responsible for halitosis, ensuring long-lasting fresh breath.</li>
  <li><strong>Alcohol-Free Formula:</strong> Provides deep oral hygiene without burning sensations or causing dry mouth.</li>
  <li><strong>Reaches Interdental Areas:</strong> Cleanses tight interdental crevices and periodontal margins missed by manual brushing.</li>
  <li><strong>Prevents Plaque Buildup:</strong> Inhibits bacterial biofilm formation to keep teeth smooth, clean, and naturally white.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1:</strong> Brush teeth thoroughly with toothpaste prior to using the rinse.</li>
  <li><strong>Step 2:</strong> Pour 20ml (approximately 4 teaspoons or 1 full capful) of Green Tea Mouthwash into a cup without diluting with water.</li>
  <li><strong>Step 3:</strong> Swish vigorously around the mouth for 30 to 60 seconds, ensuring contact with all teeth and gums.</li>
  <li><strong>Step 4:</strong> Spit out completely. Refrain from eating, drinking, or rinsing with water for 30 minutes for maximum fluoride efficacy.</li>
</ul>

<h2>Ingredients Overview</h2>
<p>Green Tea Mouthwash relies on a scientifically balanced botanical formula:</p>
<ul>
  <li><strong>Green Tea Extract (Camellia Sinensis):</strong> Rich in EGCG catechins providing potent natural antibacterial and anti-inflammatory properties.</li>
  <li><strong>Sodium Fluoride:</strong> Essential mineral active that enhances enamel resistance against dietary acid attacks.</li>
  <li><strong>Natural Menthol:</strong> Delivers a cool, refreshing sensation for clean and fresh breath.</li>
  <li><strong>Essential Cleansing Agents:</strong> Gently break down bacterial plaque biofilms without irritating oral mucosa.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For oral swishing only. Do not swallow under any circumstances.</li>
  <li>Not recommended for children under 6 years of age unless supervised by an adult or dentist.</li>
  <li>Keep out of reach of children. Store in a cool, dry place away from direct sunlight.</li>
  <li>If oral irritation or mouth sores develop, discontinue use and consult a dental professional.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Individuals preferring alcohol-free, natural botanical mouthwashes without stinging sensations.</li>
  <li>People suffering from mild gum tenderness, bleeding gums, or rapid plaque accumulation.</li>
  <li>Anyone seeking daily clinical fluoride defense against tooth decay and persistent bad breath.</li>
</ul>`,
      "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Listerine / Green Tea Care</td></tr>
  <tr><th>Category</th><td>Oral Care / Mouthwash</td></tr>
  <tr><th>Product Type</th><td>Alcohol-Free Natural Oral Rinse</td></tr>
  <tr><th>Volume/Weight</th><td>250 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>Not Applicable (Oral Care)</td></tr>
  <tr><th>Finish</th><td>Clean, Fresh Breath & Protected Enamel</td></tr>
  <tr><th>Texture</th><td>Liquid</td></tr>
  <tr><th>Fragrance</th><td>Green Tea & Mild Mint</td></tr>
  <tr><th>Active Ingredients</th><td>Green Tea Extract (Camellia Sinensis), Sodium Fluoride, Menthol</td></tr>
  <tr><th>Country of Origin</th><td>UK / Italy</td></tr>
  <tr><th>Manufacturer</th><td>Johnson & Johnson / Kenvue</td></tr>
  <tr><th>Age Group</th><td>Adults & Children 6+</td></tr>
</tbody>
</table>`,
      "knowledge_base": `<h2>Clinical Insights on Green Tea Polyphenols & Oral Health</h2>

<h3>What problem does this solve?</h3>
<p>Green Tea Mouthwash combats tooth decay, plaque formation, gingival inflammation, and bad breath (halitosis). It neutralizes bacterial acid production and fortifies enamel structure.</p>

<h3>Why does this condition happen?</h3>
<p>Oral bacteria thrive on dietary carbohydrates, producing organic acids that demineralize enamel hydroxyapatite. Bacterial biofilms along the gingival margin trigger an immune response resulting in gingivitis (swollen, bleeding gums). Alcohol-based mouthwashes can strip natural saliva, leading to dry mouth and accelerating bacterial regrowth.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Daily Rinsing:</strong> Swish with alcohol-free fluoride mouthwash twice daily after brushing.<br>
2. <strong>Floss Daily:</strong> Clean interdental gaps with dental floss every night.<br>
3. <strong>Limit Sugary Snacks:</strong> Reduce frequent consumption of fermentable sugars.<br>
4. <strong>Regular Dental Visits:</strong> Schedule professional dental cleanings every 6 months.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Botanical green tea mouthwashes are less effective at killing germs than alcohol-based rinses."<br>
<strong>Fact:</strong> Clinical research confirms green tea catechins exert strong antimicrobial action against <i>Streptococcus mutans</i> equivalent to chemical antiseptics, without destabilizing oral flora or causing mucosal dryness.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Green Tea catechins (specifically Epigallocatechin Gallate / EGCG) inhibit glucosyltransferase enzymes, preventing bacteria from synthesizing sticky glucan polymers essential for plaque adhesion. Simultaneously, Sodium Fluoride releases fluoride ions that integrate into enamel crystals, converting hydroxyapatite into acid-resistant fluorapatite, effectively halting demineralization.</p>`,
      "faqs": `<h3>What are the primary benefits of Green Tea Mouthwash 250ml?</h3>
<p>It shields enamel with fluoride, calms sensitive gums with botanical antioxidants, and neutralizes bad breath naturally without alcohol burn.</p>
<h3>Does this mouthwash contain alcohol?</h3>
<p>No, it is 100% alcohol-free, making it gentle, non-drying, and free from painful burning sensations.</p>
<h3>How often should I use Green Tea Mouthwash daily?</h3>
<p>Use twice daily (morning and night) after brushing teeth for optimal oral protection.</p>
<h3>Is it safe for children to use?</h3>
<p>It is suitable for children aged 6 and older who can swish and spit reliably without swallowing.</p>
<h3>How does Green Tea Mouthwash differ from standard mouthwashes?</h3>
<p>It combines natural green tea antioxidants with fluoride in a gentle, non-alcoholic formula that soothes gums while fighting cavities.</p>
<h3>Does it help reduce bleeding gums?</h3>
<p>Yes, the anti-inflammatory polyphenols in green tea help soothe inflamed gingival tissue and reduce bleeding during brushing.</p>
<h3>What is the bottle volume?</h3>
<p>It comes in a convenient 250ml bottle size suitable for several weeks of regular daily use.</p>
<h3>Will Green Tea Mouthwash stain my teeth?</h3>
<p>No, it is clinically formulated to prevent enamel staining while delivering clear oral hygiene.</p>
<h3>What is the recommended dosage per rinse?</h3>
<p>Use 20ml (approx. 1 capful) undiluted for each swishing session.</p>

<h3>Should I rinse my mouth with water after spitting?</h3>
<p>No, spit out the liquid and avoid rinsing with water for 30 minutes to allow fluoride to bond with enamel.</p>
<h3>Does it prevent tartar formation?</h3>
<p>Yes, by inhibiting initial bacterial plaque biofilms, it significantly reduces hard tartar buildup.</p>
<h3>Does it effectively combat morning breath?</h3>
<p>Yes, using it before bedtime suppresses nighttime anaerobic bacterial activity, ensuring fresh morning breath.</p>
<h3>Is it suitable for dry mouth sufferers?</h3>
<p>Yes, its alcohol-free formulation makes it completely safe and soothing for individuals experiencing Xerostomia.</p>
<h3>What if a small amount is swallowed accidentally?</h3>
<p>Swallowing a tiny amount is not harmful; drink some water and avoid swallowing in future uses.</p>
<h3>Can I use it with dental braces?</h3>
<p>Yes, it is excellent for orthodontic patients to flush out debris around brackets and wires.</p>
<h3>Does it react with dental crowns or fillings?</h3>
<p>No, it is completely safe for all dental restorations, fillings, and crowns.</p>
<h3>Is this product vegan-friendly?</h3>
<p>Yes, it is formulated with plant-derived green tea extracts and safe mineral ingredients.</p>
<h3>What flavor does it have?</h3>
<p>It features a refreshing green tea flavor blended with subtle, soothing mint.</p>
<h3>Does it help reduce tooth sensitivity?</h3>
<p>Yes, Sodium Fluoride helps remineralize enamel and block exposed dentinal tubules to alleviate sensitivity.</p>
<h3>How should I store this product?</h3>
<p>Store at room temperature below 30°C away from direct sunlight.</p>
<h3>Is it safe during pregnancy?</h3>
<p>Yes, it is safe for topical oral rinsing during pregnancy and lactation.</p>
<h3>Does it replace toothbrushing?</h3>
<p>No, it complements brushing. Brushing removes plaque mechanically, while mouthwash treats bacteria chemically.</p>
<h3>What is the shelf life once opened?</h3>
<p>It remains effective for up to 12 months after opening.</p>
<h3>Where is Green Tea Mouthwash manufactured?</h3>
<p>It is manufactured under international quality standards and distributed with 100% authenticity by Ekleel Abha Pharmacy.</p>`,
      "tags": ["mouthwash", "green_tea", "oral_care", "alcohol_free", "ekleel_abha"]
    },
    "schema": {
      "brand": "Listerine",
      "category": "Oral Care / Mouthwash",
      "availability": "InStock"
    },
    "image_seo": {
      "image_filename": "green-tea-mouthwash-250ml.webp",
      "alt": "Green Tea Mouthwash 250ml",
      "title": "Green Tea Mouthwash 250ml"
    }
  },

  // ==========================================
  // PRODUCT 1438: Eucerin Anti-Perspirant Spray 30ml
  // ==========================================
  {
    "product_id": "1438",
    "sku": "EK-1438",
    "category": "العناية الشخصية / مزيلات العرق",
    "brand": "Eucerin",
    "ar": {
      "title": "مزيل عرق بخاخ من يوسرين 30مل 72 ساعة",
      "meta_title": "مزيل عرق بخاخ مضاد للتعرق الشديد 72 ساعة من يوسرين 30مل | إكليل أبها",
      "meta_description": "اشتري بخاخ يوسرين المضاد للتعرق الشديد حماية 72 ساعة (30مل). يدوم طويلاً، يقضي على العرق المفرط والرائحة. أصلي 100% من صيدلية إكليل أبها السعودية.",
      "description": `<h2>نظرة عامة على المنتج</h2>
<p>بخاخ يوسرين المضاد للتعرق الشديد حماية 72 ساعة سعة 30 مل <strong>(Eucerin Anti-Perspirant Spray 30ml - 72-Hour Protection)</strong> هو حل طبي مكثف مصمم خصيصاً للأشخاص الذين يعانون من التعرق المفرط (Hyperhidrosis) والتعرق الشديد الناتج عن التوتر والجهد البدني. تم تطوير هذا المستحضر الطبي في مختبرات يوسرين العالمية لتقديم أقصى درجات الفعالية في السيطرة على إفرازات العرق والرائحة الكريهة لمدة تصل إلى 72 ساعة كاملة دون التسبب في تهيج البشرة.</p>

<p>يمتاز بخاخ يوسرين بتركيبة مركزة عالية الأداء تحتوي على مركبات كلوروهيدرات الألومنيوم وكلوريد الألومنيوم التي تتغلغل عميقاً في قنوات الغدد العرقية لتقليل إفراز السوائل بشكل ملحوظ. أثبتت الاختبارات السريرية والجلدية قدرة هذا المنتج على خفيض معدل التعرق بنسبة تصل إلى 91%، مع الحفاظ على قدرة تحمل ممتازة للبشرة الحساسة بفضل تركيبه المتوازن والخالي من الكحول والمواد المهيجة.</p>

<h2>الفوائد الرئيسية</h2>
<ul>
  <li><strong>حماية فائقة تدوم 72 ساعة:</strong> يمنح حماية مستمرة وموثوقة ضد العرق والرائحة الشديدة لثلاثة أيام متتالية.</li>
  <li><strong>تقليل التعرق بنسبة 91%:</strong> أثبتت الدراسات السريرية قدرته المذهلة على تقليص إفرازات الغدد العرقية بشكل ملحوظ.</li>
  <li><strong>مخصص للتعرق الشديد والزائد:</strong> الخيار الطبي الأول للمصابين بفرط التعرق (Hyperhidrosis) والتعرق الناتج عن التوتر.</li>
  <li><strong>تركيبة لطيفة على البشرة الحساسة:</strong> خاضع لاختبارات جلدية صارمة تناسب جميع أنواع البشرة دون التسبب في احمرار أو حكة.</li>
  <li><strong>مضاد للرائحة الكريهة:</strong> يمنع تكاثر البكتيريا المسؤولة عن تفكيك العرق وتحويله إلى رائحة مزعجة.</li>
  <li><strong>حجم عملي ومكثف:</strong> تأتي العبوة المضغوطة بسعة 30 مل بتركيز مرتفع يكفي لأسابيع من الاستخدام المنتظم.</li>
</ul>

<h2>طريقة الاستخدام</h2>
<ul>
  <li><strong>الخطوة الأولى (التطبيق الليلي):</strong> يفضل تطبيق البخاخ ليلاً قبل النوم على بشرة إبطين نظيفة وجافة تماماً. (تكون الغدد العرقية أقل نشاطاً ليلاً مما يسمح للمركب بالعمل بفعالية).</li>
  <li><strong>الخطوة الثانية:</strong> يرش البخاخ على منطقة الإبطين من مسافة 15 سم لمرة أو مرتين فقط على كل إبط.</li>
  <li><strong>الخطوة الثالثة:</strong> اتركي المنطقة تجف تماماً قبل ارتداء الملابس لمنع بقع الملابس.</li>
  <li><strong>الخطوة الرابعة (الجدول العلاجي):</strong> يُستخدم يومياً في أول 3 أيام، ثم يقلل الاستخدام إلى مرتين في الأسبوع أو حسب الحاجة للحفاظ على النتيجة.</li>
</ul>

<h2>نظرة عامة على المكونات</h2>
<p>يعتمد بخاخ يوسرين 72 ساعة على مكونات علاجية عالية التركيز:</p>
<ul>
  <li><strong>كلوروهيدرات الألومنيوم (Aluminium Chlorohydrate):** مركب فعال يعمل على تقليص فتحات الغدد العرقية مؤقتاً.</li>
  <li><strong>كلوريد الألومنيوم (Aluminium Chloride):** ينفذ عميقاً في القنوات العرقية لتشكيل سدادة هلامية مؤقتة تمنع تدفق العرق الزائد.</li>
  <li><strong>تركيبة خالية من الكحول:</strong> تضمن حماية البشرة من الجفاف، الحرقة، والتهيج بعد التطبيق.</li>
  <li><strong>مركبات مهدئة للجلد:</strong> تحافظ على سلامة حاجز البشرة وتحميها من الاحمرار.</li>
</ul>

<h2>تحذيرات واحتياطات</h2>
<ul>
  <li>يُستخدم مظهرياً على منطقة الإبطين فقط؛ تجنبي رشه بالقرب من الوجه أو العينين أو الأغشية المخاطية.</li>
  <li>لا يُطبق فوراً بعد حلاقة الإبطين أو على جلد مجروح أو متهيج؛ انتظري 24 ساعة على الأقل بعد الحلاقة.</li>
  <li>يُحفظ بعيداً عن متناول الأطفال وفي مكان بارد بعيداً عن أشعة الشمس المباشرة ومصادر الحرارة.</li>
  <li>في حال حدوث حكة شديدة أو احمرار استثنائي، اغسلي المنطقة بالماء والتوقف عن الاستخدام.</li>
</ul>

<h2>لمن هذا المنتج</h2>
<ul>
  <li>للأشخاص الذين يعانون من التعرق الزائد المفرط (Hyperhidrosis) ولا تجدي معهم مزيلات العرق العادية نفعاً.</li>
  <li>للذين يتعرضون للمواقف الضغاطة وتوتر العمل ويرغبون في ضمان جفاف الإبطين بنسبة 100%.</li>
  <li>لكل من يبحث عن بخاخ طبي مركز يمنح حماية ممتدة المفعول حتى 72 ساعة بأمان تام على البشرة.</li>
</ul>`,
      "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>العلامة التجارية</th><td>Eucerin (يوسرين)</td></tr>
  <tr><th>الفئة</th><td>العناية الشخصية / مزيلات العرق</td></tr>
  <tr><th>نوع المنتج</th><td>بخاخ طبي مضاد للتعرق الشديد (Intensive Anti-Perspirant)</td></tr>
  <tr><th>الحجم/الوزن</th><td>30 مل</td></tr>
  <tr><th>نوع البشرة/الشعر</th><td>جميع أنواع البشرة (بما فيها البشرة الحساسة)</td></tr>
  <tr><th>المظهر النهائي</th><td>إبطين جافين تماماً وخاليين من الرائحة لمدة 72 ساعة</td></tr>
  <tr><th>الملمس</th><td>بخاخ رذاذي سريعة التجفيف</td></tr>
  <tr><th>العطر</th><td>عطر طبي خفيف جداً محايد</td></tr>
  <tr><th>المكونات النشطة</th><td>كلوروهيدرات الألومنيوم، كلوريد الألومنيوم</td></tr>
  <tr><th>بلد المنشأ</th><td>ألمانيا</td></tr>
  <tr><th>الشركة المصنعة</th><td>Beiersdorf AG</td></tr>
  <tr><th>الفئة العمرية</th><td>البالغين والمراهقين (ابتداءً من سن 12 عاماً)</td></tr>
</tbody>
</table>`,
      "knowledge_base": `<h2>الدليل العلمي لعلاج فرط التعرق (Hyperhidrosis) وآلية عمل يوسرين</h2>

<h3>ما هي المشكلة التي يحلها هذا المنتج؟</h3>
<p>يعالج بخاخ يوسرين 72 ساعة مشكلة فرط التعرق الإبطي (Axillary Hyperhidrosis) والتعرق الشديد المفاجئ الناتج عن التوتر أو النشاط البدني المكثف، ويقضي على الروائح الكريهة المصاحبة له.</p>

<h3>لماذا تحدث هذه المشكلة؟</h3>
<p>التعرق هو آلية طبيعية لتبريد الجسم تنظمها الغدد العرقية الناتحة (Eccrine Glands) والأبوكرينية (Apocrine Glands). لدى بعض الأشخاص، يزداد نشاط الجهاز العصبي الودي (Sympathetic Nervous System) مما يحفز الغدد العرقية لإفراز كميات فائضة من العرق تزيد عن حاجة الجسم. عندما يلتقي هذا العرق بالبكتيريا الطبيعية الموجودة على سطح الجلد، تقوم البكتيريا بتفكيك الأحماض الدهنية بالعرق، مما يتسبب في تصاعد الرائحة النفاذة المزعجة.</p>

<h3>نصائح وقائية للتحكم بالتعرق</h3>
<p>1. <strong>التطبيق الصحيح ليلاً:</strong> تطبيق مضاد التعرق العلاجي ليلاً على بشرة جافة كلياً للحصول على أقصى مفعول.<br>
2. <strong>ارتداء أقمشة قطنية:</strong> اختيار ملابس مصنوعة من ألياف طبيعية تسمح بالتهوية.<br>
3. <strong>تجنب المهيجات الغذائية:</strong> تقليل تناول الأطعمة الحارة، الكافيين، والأطعمة الغنية بالثوم التي تزيد إفراز العرق.<br>
4. <strong>النظافة الشخصية:</strong> غسل الإبطين بصابون مضاد للبكتيريا وتجفيفهما جيداً قبل تطبيق بخاخ يوسرين.</p>

<h3>خرافات شائعة</h3>
<p><strong>خرافة:</strong> "مضادات التعرق التي تحتوي على الألومنيوم تحبس السموم داخل الجسم وتسبب أمراضاً خطيرة."<br>
<strong>الحقيقة:</strong> أثبتت الهيئات الصحية العالمية (مثل FDA وSCCS الأوروبية) أن مضادات التعرق تعمل مظهرياً فقط على فتحات الغدد العرقية السطحية، وأن الجسم يتخلص من السموم عبر الكبد والكليتين وليس عبر غدد الإبطين العرقية.</p>

<h3>التفسير العلمي لآلية العمل</h3>
<p>يحتوي بخاخ يوسرين على جزيئات <strong>كلوريد الألومنيوم وكلوروهيدرات الألومنيوم</strong>. عند تطبيق البخاخ على الجلد، تتفاعل أملاح الألومنيوم مع الماء والبروتينات الموجودة داخل قنوات الغدد العرقية، ممتدة لتشكل سدادة هلامية مؤقتة غير ضارة (Keratin Plug) في الجزء السطحي من القناة. هذه السدادة تمنع خروج العرق إلى سطح الجلد. ومع التجدد الطبيعي لخلايا البشرة، تذوب هذه السدادة وتزول تلقائياً بعد عدة أيام، مما يفسر مفعول الحماية الممتد حتى 72 ساعة.</p>`,
      "faqs": `<h3>ما هو بخاخ يوسرين المضاد للتعرق 72 ساعة وما هي دواعي استخدامه؟</h3>
<p>هو بخاخ طبي علاجي مكثف مخصص للسيطرة على التعرق المفرط والزائد تحت الإبطين، حيث يوفر حماية فائقة وجفافاً كلياً يدوم حتى 72 ساعة.</p>
<h3>كيف يُستخدم بخاخ يوسرين للحصول على أفضل نتيجة؟</h3>
<p>يُرش ليلاً قبل النوم على بشرة إبطين جافة ونظيفة تماماً. استخدمه يومياً في أول 3 أيام، ثم قلل الاستخدام لمرتين أسبوعياً حسب الحاجة.</p>
<h3>لماذا يُفضل تطبيق بخاخ يوسرين ليلاً وليس صباحاً؟</h3>
<p>لأن الغدد العرقية تكون في حالة راحة وأقل نشاطاً ليلاً، مما يسمح لأملاح الألومنيوم بالتغلغل والاستقرار داخل قنوات الغدد العرقية وتشكيل سدادة الحماية بنجاح.</p>
<h3>هل يناسب هذا البخاخ أصحاب البشرة الحساسة؟</h3>
<p>نعم، تم اختباره سريرياً على البشرة الحساسة وهو خالٍ من الكحول لتقليل أي احتمالية للتهيج أو الاحمرار.</p>
<h3>هل يمنع البخاخ رائحة العرق الكريهة؟</h3>
<p>نعم، يقضي على العرق الذي يتغذى عليه البكتيريا، مما يقطع مسبب الرائحة الكريهة من جذوره.</p>
<h3>كم تبلغ نسبة تقليل التعرق عند استخدام هذا المنتج؟</h3>
<p>أثبتت الفحوصات السريرية أن بخاخ يوسرين يقلل التعرق بنسبة تصل إلى 91% لدى الأشخاص الذين يعانون من فرط التعرق.</p>
<h3>هل يمكن استخدام بخاخ يوسرين فوراً بعد حلاقة الإبطين؟</h3>
<p>لا، ينبغي الانتظار 24 ساعة على الأقل بعد الحلاقة أو إزالة الشعر قبل تطبيق المنتج تجنباً لتهيج البشرة.</p>
<h3>هل يترك البخاخ بقعاً بيضاء أو صفراء على الملابس؟</h3>
<p>إذا تُرك ليجف تماماً قبل ارتداء الملابس، فلن يترك أي بقع أو آثار على الملابس البيضاء أو الداكنة.</p>
<h3>ما هو حجم العبوة وهل تكفي لفترة طويلة؟</h3>
<p>حجم العبوة 30 مل، وبما أنها شديدة التركيز وتستخدم مرتين أسبوعياً بعد الفترة الأولى، فإنها تكفي لعدة أشهر من الاستخدام.</p>
<h3>هل يسبب البخاخ انسداداً دائماً للغدد العرقية؟</h3>
<p>لا، السدادة التي تشكلها أملاح الألومنيوم مؤقتة ولطيفة وتزول تلقائياً مع التجدد الطبيعي لخلايا البشرة.</p>
<h3>هل يمكن استخدام بخاخ يوسرين للرجال والنساء؟</h3>
<p>نعم، المنتج محايد ومناسب لكلا الجنسين وله رائحة طبية خفيفة جداً تزول بعد التجفيف.</p>
<h3>ما الفرق بين مزيل العرق العادي (Deodorant) ومضاد التعرق العلاجي (Anti-Perspirant) من يوسرين؟</h3>
<p>مزيل العرق العادي يغطي الرائحة فقط دون إيقاف العرق، بينما مضاد التعرق العلاجي من يوسرين يقلل إفراز العرق نفسه بنسبة 91% ويدوم 72 ساعة.</p>
<h3>هل يحتاج البخاخ لإعادة التطبيق بعد الاستحمام؟</h3>
<p>لا، بعد استقرار المادة الفعالة داخل القنوات، فإن الاستحمام الطبيعي بالماء والصابون لن يبطل مفعول الحماية الممتد.</p>
<h3>هل يمكن استخدامه لمناطق أخرى غير الإبطين؟</h3>
<p>تم تصميم واختبار هذا المنتح خصيصاً لمنطقة الإبطين، ولا يُنصح برشه على الوجه أو المناطق الحساسة.</p>
<h3>هل البخاخ خالي من الكحول؟</h3>
<p>نعم، تركيبته خالية من الكحول لمنع الحرقة وتوفير أقصى درجات الراحة للبشرة.</p>
<h3>ما هي الصلاحية بعد فتح عبوة بخاخ يوسرين؟</h3>
<p>الصلاحية تكون مدونة على العبوة وتستمر عادة حتى 12 شهراً من الفتح.</p>
<h3>هل يناسب البخاخ المراهقين؟</h3>
<p>نعم، هو مناسب للمراهقين من سن 12 عاماً ممن يعانون من زيادة إفراز العرق أثناء البلوغ أو ممارسة الرياضة.</p>
<h3>ماذا أفعل إذا شعرت بوخز خفيف عند التطبيق؟</h3>
<p>الوخز الخفيف قد يحدث إذا كانت البشرة رطبة قليلاً. تأكدي من تجفيف الإبطين تماماً قبل الترشيش، أو قللي الكمية.</p>
<h3>هل هذا المنتج نباتي؟</h3>
<p>منتجات يوسرين تخضع للمعايير الطبية الأوروبية الصارمة وتخلو من المكونات الضارة.</p>
<h3>هل البخاخ مضغوط أم بخاخ مضخة يد؟</h3>
<p>يأتي على شكل بخاخ مضخة يدوي (Pump Spray) سهل التحكم وبدون غازات مضغوطة مسببة للحساسية.</p>
<h3>كيف يتم تخزين العبوة؟</h3>
<p>تحفظ في درجة حرارة الغرفة دون 25 مئوية بعيداً عن الحرارة المباشرة والشمس.</p>
<h3>هل يسبب البخاخ اسمرار منطقة الإبطين؟</h3>
<p>لا، بل خلوه من الكحول والمعطرات القاسية يحمي البشرة من التهيج الذي يسبب التصبغات والاسمرار.</p>
<h3>هل المنتج آمن أثناء الحمل؟</h3>
<p>المكونات آمنة مظهرياً، لكن يُفضل دائماً مراجعة الطبيب المتابع خلال فترة الحمل.</p>
<h3>أين يتم تصنيع بخاخ يوسرين؟</h3>
<p>يُصنع في ألمانيا بواسطة Beiersdorf AG وتوفر صيدلية إكليل أبها المنتج الأصلي 100%. </p>`,
      "tags": ["eucerin", "مزيل_عرق", "يوسرين", "تعرق_شديد", "حماية_72_ساعة", "إكليل_أبها"]
    },
    "en": {
      "title": "Eucerin Anti-Perspirant Spray 30ml - 72-Hour Protection",
      "meta_title": "Eucerin Anti-Perspirant Spray 30ml 72-Hour Protection | Ekleel",
      "meta_description": "Buy Eucerin Intensive Anti-Perspirant Spray (30ml) for 72-hour protection against heavy sweating and hyperhidrosis. Alcohol-free. 100% genuine at Ekleel Pharmacy.",
      "description": `<h2>Product Overview</h2>
<p><strong>Eucerin Anti-Perspirant Spray 30ml (72-Hour Protection)</strong> is an intensive clinical formula specifically engineered for individuals suffering from heavy perspiration, stress sweating, and axillary hyperhidrosis. Developed by Eucerin's global dermatological laboratories, this high-performance anti-perspirant delivers up to 72 hours of continuous defense against excessive sweat production and foul body odor without causing skin irritation.</p>

<p>Featuring a concentrated formula containing active Aluminium Chlorohydrate and Aluminium Chloride, it penetrates deep into sweat gland ducts to significantly decrease sweat release. Clinical trials demonstrate up to a 91% reduction in sweat secretion, offering dry, comfortable underarms and reliable confidence while maintaining high cutaneous tolerance on sensitive skin.</p>

<h2>Key Benefits</h2>
<ul>
  <li><strong>72-Hour Clinical Protection:</strong> Delivers long-lasting, dependable defense against intense sweating and odor for three full days.</li>
  <li><strong>91% Sweat Reduction:</strong> Clinically proven to dramatically reduce sweat gland output in hyperhidrosis sufferers.</li>
  <li><strong>Targeted for Heavy Sweating:</strong> The primary medical solution for heavy perspiration, heat stress, and emotional sweating.</li>
  <li><strong>Gentle on Sensitive Skin:</strong> Alcohol-free and dermatologically tested to minimize redness, stinging, and skin reactivity.</li>
  <li><strong>Odor Neutralizing Action:</strong> Prevents bacterial breakdown of sweat components that cause unpleasant body odor.</li>
  <li><strong>Concentrated Compact Pump Spray:</strong> High-potency 30ml pump spray lasts for months of regular treatment.</li>
</ul>

<h2>How to Use / Instructions for Use</h2>
<ul>
  <li><strong>Step 1 (Night Application):</strong> Apply in the evening before bed onto completely clean, dry, unbroken underarm skin (sweat glands are least active at night).</li>
  <li><strong>Step 2:</strong> Hold spray 15cm away and apply 1-2 spritzes onto each underarm area.</li>
  <li><strong>Step 3:</strong> Allow to air dry completely before putting on garments to avoid fabric spotting.</li>
  <li><strong>Step 4 (Treatment Schedule):</strong> Apply daily for the first 3 days, then reduce application to 1-2 times per week to maintain dry underarms.</li>
</ul>

<h2>Ingredients Overview</h2>
<p>Eucerin 72-Hour Anti-Perspirant relies on high-concentration dermatological actives:</p>
<ul>
  <li><strong>Aluminium Chlorohydrate:</strong> Active anti-perspirant salt that contracts sweat pore openings.</li>
  <li><strong>Aluminium Chloride:</strong> Deep-penetrating active that forms a temporary keratin plug inside sweat ducts to block flow.</li>
  <li><strong>Alcohol-Free Base:</strong> Formulated without alcohol to shield delicate underarm skin from burning and dryness.</li>
  <li><strong>Soothing Skin Conditioning Agents:</strong> Maintain skin barrier integrity and calm sensitive tissue.</li>
</ul>

<h2>Warnings & Precautions</h2>
<ul>
  <li>For topical underarm use only. Do not spray near eyes, face, or damaged skin.</li>
  <li>Do not apply immediately after shaving underarms; wait at least 24 hours post-epilation before use.</li>
  <li>Keep out of reach of children. Store in a cool place away from direct heat and sunlight.</li>
  <li>If severe redness or irritation develops, wash off and discontinue use.</li>
</ul>

<h2>Who Is This For?</h2>
<ul>
  <li>Individuals dealing with severe axillary hyperhidrosis or excessive sweating unmanaged by regular deodorants.</li>
  <li>Professionals facing high-stress situations needing 100% reliable underarm dryness.</li>
  <li>Anyone seeking a clinical 72-hour anti-perspirant that is gentle on sensitive skin.</li>
</ul>`,
      "specifications": `<table class="specifications-table">
<tbody>
  <tr><th>Brand</th><td>Eucerin</td></tr>
  <tr><th>Category</th><td>Personal Care / Anti-Perspirants</td></tr>
  <tr><th>Product Type</th><td>Intensive Clinical Anti-Perspirant Pump Spray</td></tr>
  <tr><th>Volume/Weight</th><td>30 ml</td></tr>
  <tr><th>Skin/Hair Type</th><td>All Skin Types (Including Sensitive Skin)</td></tr>
  <tr><th>Finish</th><td>Completely Dry & Odor-Free Underarms for 72h</td></tr>
  <tr><th>Texture</th><td>Fast-Drying Spray Mist</td></tr>
  <tr><th>Fragrance</th><td>Subtle Neutral Light Scent</td></tr>
  <tr><th>Active Ingredients</th><td>Aluminium Chlorohydrate, Aluminium Chloride</td></tr>
  <tr><th>Country of Origin</th><td>Germany</td></tr>
  <tr><th>Manufacturer</th><td>Beiersdorf AG</td></tr>
  <tr><th>Age Group</th><td>Adults & Teens (12+)</td></tr>
</tbody>
</table>`,
      "knowledge_base": `<h2>Clinical Insights on Axillary Hyperhidrosis & Eucerin Mechanism</h2>

<h3>What problem does this solve?</h3>
<p>Eucerin 72h Anti-Perspirant resolves axillary hyperhidrosis (excessive underarm sweating) and stress-induced perspiration. It stops heavy sweat flow and eliminates associated body odor.</p>

<h3>Why does this condition happen?</h3>
<p>Sweating is controlled by eccrine and apocrine sweat glands regulated by the sympathetic nervous system. In hyperhidrosis sufferers, overactive nerve signals trigger excessive sweat production regardless of body temperature. When sweat contacts surface skin bacteria, micro-organisms breakdown fatty acids in apocrine secretions, generating volatile odor compounds.</p>

<h3>Prevention Tips</h3>
<p>1. <strong>Apply at Night:</strong> Always apply anti-perspirants before bed when sweat glands are dormant.<br>
2. <strong>Ensure Complete Dryness:</strong> Dry skin thoroughly before application to optimize aluminum plug formation.<br>
3. <strong>Wear Breathable Fabrics:</strong> Choose natural cotton or moisture-wicking clothing.<br>
4. <strong>Avoid Dietary Triggers:</strong> Reduce spicy foods, caffeine, and hot beverages that stimulate thermogenesis.</p>

<h3>Common Myths</h3>
<p><strong>Myth:</strong> "Aluminum anti-perspirants trap toxins inside the body and are harmful to health."<br>
<strong>Fact:</strong> Global health authorities (US FDA, European SCCS) confirm anti-perspirants act topically at sweat duct openings. Toxins are eliminated via the liver and kidneys, not underarm sweat glands.</p>

<h3>Scientific Explanation of Mechanism</h3>
<p>Eucerin contains highly concentrated <strong>Aluminium Chloride and Aluminium Chlorohydrate</strong>. Upon application, these aluminum salts dissolve in sweat moisture and react with proteins inside sweat duct lumens to form a temporary, inert keratin plug. This plug mechanically obstructs sweat release to the skin surface. As epidermal cells naturally exfoliate over 72 hours, the plug sheds harmlessly, providing extended dryness.</p>`,
      "faqs": `<h3>What is Eucerin Anti-Perspirant Spray 30ml and what is it used for?</h3>
<p>It is an intensive clinical anti-perspirant designed to control severe underarm sweating and hyperhidrosis for up to 72 hours.</p>
<h3>How should I apply Eucerin Anti-Perspirant for maximum effectiveness?</h3>
<p>Apply at night before sleeping onto completely dry, clean skin. Use daily for the first 3 days, then reduce to 1-2 times weekly.</p>
<h3>Why is night application recommended over morning application?</h3>
<p>Sweat glands are less active at night, allowing aluminum salts to enter sweat ducts unimpeded and form protective keratin plugs.</p>
<h3>Is this spray suitable for sensitive skin?</h3>
<p>Yes, it is clinically tested on sensitive skin and formulated without alcohol to prevent burning and irritation.</p>
<h3>Does it effectively stop body odor?</h3>
<p>Yes, by halting sweat secretion, it eliminates the liquid medium required for odor-producing bacteria to proliferate.</p>
<h3>What is the clinical sweat reduction percentage?</h3>
<p>Clinical studies prove up to a 91% reduction in underarm sweat secretion among hyperhidrosis patients.</p>

<h3>Can I apply this spray immediately after shaving my underarms?</h3>
<p>No, wait at least 24 hours after shaving or hair removal before applying to prevent skin irritation.</p>
<h3>Will it stain white or dark clothing?</h3>
<p>If allowed to dry completely before dressing, it leaves no white marks or yellow stains on clothing.</p>
<h3>How long does a 30ml bottle last?</h3>
<p>Because it is highly concentrated and applied 1-2 times per week maintenance, a 30ml bottle lasts several months.</p>
<h3>Does it cause permanent blockage of sweat glands?</h3>
<p>No, the keratin plugs formed are temporary and naturally shed during normal skin cell renewal.</p>
<h3>Is this product suitable for both men and women?</h3>
<p>Yes, it features a unisex neutral formulation suitable for both men and women.</p>
<h3>How does this differ from regular commercial deodorants?</h3>
<p>Deodorants only mask odor, whereas Eucerin clinical anti-perspirant reduces actual sweat secretion by 91% for 72 hours.</p>
<h3>Do I need to reapply after showering?</h3>
<p>No, once the aluminum plug is established in sweat ducts, normal showering with soap will not wash away protection.</p>
<h3>Can it be sprayed on other body parts like the face?</h3>
<p>It is specifically formulated and tested for underarm skin only; avoid spraying on the face or sensitive areas.</p>
<h3>Is this formula alcohol-free?</h3>
<p>Yes, it is completely alcohol-free to protect sensitive cutaneous tissues.</p>
<h3>What is the shelf life after opening?</h3>
<p>It is effective for up to 12 months after opening, as marked on the container.</p>
<h3>Can teenagers use this product?</h3>
<p>Yes, teenagers aged 12 and above experiencing excessive puberty-related sweating can safely use it.</p>
<h3>What if I feel a mild tingling upon application?</h3>
<p>Tingling can occur if skin is slightly damp. Ensure underarms are 100% dry prior to application.</p>
<h3>Is this spray non-comedogenic?</h3>
<p>Yes, it is dermatologically formulated for high skin tolerance.</p>
<h3>Is the container an aerosol or pump spray?</h3>
<p>It is a eco-friendly manual pump spray (non-aerosol) allowing precise dosage control.</p>
<h3>How should I store Eucerin spray?</h3>
<p>Store at room temperature below 25°C away from direct sunlight and heat.</p>
<h3>Does it cause underarm skin darkening?</h3>
<p>No, being alcohol-free and non-irritating prevents post-inflammatory hyperpigmentation under arms.</p>
<h3>Is it safe during pregnancy?</h3>
<p>Topical application is considered safe, but consulting your physician during pregnancy is recommended.</p>
<h3>Where is Eucerin Anti-Perspirant Spray manufactured?</h3>
<p>It is manufactured in Germany by Beiersdorf AG and distributed authentically by Ekleel Abha Pharmacy.</p>`,
      "tags": ["eucerin", "anti_perspirant", "sweat_control", "72h_protection", "hyperhidrosis", "ekleel_abha"]
    },
    "schema": {
      "brand": "Eucerin",
      "category": "Personal Care / Anti-Perspirants",
      "availability": "InStock"
    },
    "image_seo": {
      "image_filename": "eucerin-anti-perspirant-spray-30ml.webp",
      "alt": "Eucerin Anti-Perspirant Spray 30ml - 72-Hour Protection",
      "title": "Eucerin Anti-Perspirant Spray 30ml - 72-Hour Protection"
    }
  }
];

// Write out all files
products.forEach(p => {
  const filename = `${p.product_id}.json`;
  const jsonContent = JSON.stringify(p, null, 2);
  
  targetDirs.forEach(dir => {
    const fullPath = path.join(dir, filename);
    fs.writeFileSync(fullPath, jsonContent, 'utf8');
    console.log(`Saved ${filename} to ${fullPath}`);
  });
});

console.log('✅ Batch generation finished successfully!');
