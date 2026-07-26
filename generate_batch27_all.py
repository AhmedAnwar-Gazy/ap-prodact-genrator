import json, os
from build_batch27 import build_beesline_deo, create_product_1843

products = []

# 1841: Beesline Rose Fragrance Deodorant (2 Pieces)
products.append(build_beesline_deo(
    1841,
    "مزيل عرق بعطر الورد من بيزلين(قطعتين)",
    "Beesline Rose Fragrance Deodorant (2 Pieces)",
    "الورد الجوري الفاخر (Rose)",
    "Rose",
    "تفتيحاً طبيعياً وعطراً ورود فواحاً",
    "natural underarm whitening and fresh rose aroma",
    "قطعتين (2 x 50ml)",
    "2 Pieces (2 x 50ml)",
    "5281018567968",
    "beesline-rose-fragrance-deodorant-2-pieces"
))

# 1842: Beesline Fragrance-Free Deodorant - 50 ml
products.append(build_beesline_deo(
    1842,
    "مزيل عرق خالي من العطور من بيزلين 50 مل",
    "Beesline Fragrance-Free Deodorant - 50 ml",
    "عديم الرائحة (Fragrance-Free)",
    "Fragrance-Free",
    "تفتيحاً طبيعياً ناعماً دون أي عطور",
    "gentle underarm whitening with zero fragrance",
    "50 مل",
    "50 ml",
    "5281018003039",
    "beesline-fragrance-free-deodorant-50ml"
))

# 1843: Beesline Whitening Cream 150g
products.append(create_product_1843())

# 1844: Beesline Invisible Touch Deodorant - 50ml
products.append(build_beesline_deo(
    1844,
    "مزيل عرق لمسة خفية من بيزلين 50 مل",
    "Beesline Invisible Touch Deodorant - 50ml",
    "اللمسة الخفية النظيفة (Invisible Touch)",
    "Invisible Touch",
    "حماية شفافة 100% دون ترك بقع بيضاء على الملابس",
    "100% transparent defense leaving zero white marks on clothes",
    "50 مل",
    "50 ml",
    "5281018003862",
    "beesline-invisible-touch-deodorant-50ml"
))

# 1845: Beesline Indian Incense Deodorant - 50 ml
products.append(build_beesline_deo(
    1845,
    "مزيل عرق بخور هندي من بيزلين 50 مل",
    "Beesline Indian Incense Deodorant - 50 ml",
    "البخور الهندي والمسك الفاخر (Indian Incense)",
    "Indian Incense",
    "تفتيحاً ناعماً وعبيراً شرقياً ملكياً بالبخور الهندي",
    "gentle underarm whitening and royal oriental Indian Incense scent",
    "50 مل",
    "50 ml",
    "5281018003886",
    "beesline-indian-incense-deodorant-50ml"
))

for pdata in products:
    pid = pdata["product_id"]
    paths = [
        f"temp/generated_products/{pid}.json",
        f"../temp/generated_products/{pid}.json"
    ]
    for p in paths:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as f:
            json.dump(pdata, f, ensure_ascii=False, indent=2)

    ar_faqs_cnt = pdata["ar"]["faqs"].count("<h3>")
    en_faqs_cnt = pdata["en"]["faqs"].count("<h3>")
    print(f"Product {pid} generated: AR FAQs={ar_faqs_cnt}, EN FAQs={en_faqs_cnt}")

print("\nBatch 27 all products generated!")
