import json, os
from build_batch27 import build_beesline_deo
from build_batch28 import create_product_1847, create_product_1848, create_product_1850

products = []

# 1846: Beesline Cotton Softness Deodorant (2 Pieces)
products.append(build_beesline_deo(
    1846,
    "مزيل عرق نعومة القطن من بيزلين(قطعتين)",
    "Beesline Cotton Softness Deodorant (2 Pieces)",
    "نعومة القطن النقي (Cotton Softness)",
    "Cotton Softness",
    "تفتيحاً طبيعياً وملمساً قطنياً ناعماً",
    "natural underarm whitening and cotton-soft feel",
    "قطعتين (2 x 50ml)",
    "2 Pieces (2 x 50ml)",
    "5281018086810",
    "beesline-cotton-softness-deodorant-2-pieces"
))

# 1847: Beesline Facial Wash Oily Skin 250ml
products.append(create_product_1847())

# 1848: Beesline Sensitive Zone Soap 110g
products.append(create_product_1848())

# 1849: Beesline Breeze Freshness Deodorant (2-Piece Set)
products.append(build_beesline_deo(
    1849,
    "مزيل عرق انتعاش النسيم من بيزلين(قطعتين)",
    "Beesline Breeze Freshness Deodorant (2-Piece Set)",
    "انتعاش النسيم النقي (Breeze Freshness)",
    "Breeze Freshness",
    "تفتيحاً طبيعياً وانتعاش نسيم فواح",
    "natural underarm whitening and fresh breeze aroma",
    "قطعتين (2 x 50ml)",
    "2 Pieces (2 x 50ml)",
    "5281018567999",
    "beesline-breeze-freshness-deodorant-2-piece-set"
))

# 1850: Nivea Soft Cream 100ml
products.append(create_product_1850())

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

print("\nBatch 28 all products generated!")
