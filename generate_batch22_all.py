import json, os
from build_batch22 import build_clere_body_cream, create_product_1816, create_product_1817, create_product_1818

products = []

# 1815: Clere Coconut Body Cream 500ml
products.append(build_clere_body_cream(
    1815,
    "كريم كلير مرطب للجسم بجوز الهند للبشرة الجافة - 500 مل",
    "Coconut Moisturizing Body Cream - 500 ml",
    "جوز الهند المرطب",
    "Coconut Oil",
    "616762141686",
    "coconut-moisturizing-body-cream-500ml"
))

# 1816: Nivea Deodorant 40ml
products.append(create_product_1816())

# 1817: Water Dental Flosser
products.append(create_product_1817())

# 1818: Hery Lipstick
products.append(create_product_1818())

# 1819: Clere Rich Body Moisturizing Cream Glycerin & Vitamins A & E 500ml
products.append(build_clere_body_cream(
    1819,
    "كريم كلير مرطب للجسم غني بالجلسرين وفيتامين A و E - 500 مل",
    "Rich Body Moisturizing Cream with Glycerin and Vitamins A & E - 500ml",
    "الجلسرين النقي وفيتامين A & E",
    "Pure Glycerin & Vitamins A & E",
    "6001374081026",
    "rich-body-moisturizing-cream-with-glycerin-and-vitamins-a-and-e-500ml"
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

print("\nBatch 22 all products generated!")
