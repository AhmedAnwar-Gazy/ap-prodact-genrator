import json, os
from build_batch22 import build_clere_body_cream
from build_batch23 import create_product_1822, create_product_1823, create_product_1824

products = []

# 1820: Clere Rich Musk Body Moisturizing Cream 500ml
products.append(build_clere_body_cream(
    1820,
    "كريم مرطب للجسم ريتش مسك من كلير - 500 مل",
    "Rich Musk Body Moisturizing Cream - 500 ml",
    "المسك الفاخر (Rich Musk)",
    "Rich Musk",
    "6001374081064",
    "rich-musk-body-moisturizing-cream-500ml"
))

# 1821: Clere Cocoa Butter Smoothing Cream 500ml
products.append(build_clere_body_cream(
    1821,
    "كريم كلير للتنعيم بزبدة الكاكاو لترطيب وتغذية الجسم - 500 مل",
    "Cocoa Butter Smoothing Cream - 500ml",
    "زبدة الكاكاو النادرة",
    "Cocoa Butter",
    "6001374081033",
    "cocoa-butter-smoothing-cream-500ml"
))

# 1822: Beauty Vitamins for Hair & Nails 60 Gummies
products.append(create_product_1822())

# 1823: Watermans Hair Growth Conditioner 250ml
products.append(create_product_1823())

# 1824: Wellzed Baby Water Wipes 100 Wipes
products.append(create_product_1824())

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

print("\nBatch 23 all products generated!")
