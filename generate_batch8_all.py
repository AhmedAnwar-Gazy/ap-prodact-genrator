import json, os
from build_hair_mask import build_hair_mask_product
from build_batch8 import create_product_1736, create_product_1737

products = []
products.append(build_hair_mask_product(1733, "Coffee Oil Replacement", "بديل الزيت بالقهوة", "6297938832627", "coffee-oil"))
products.append(build_hair_mask_product(1734, "Coconut Oil", "جوز الهند", "6297938832528", "coconut-oil"))
products.append(build_hair_mask_product(1735, "Avocado Oil", "الأفوكادو", "6297938832320", "avocado-oil"))
products.append(create_product_1736())
products.append(create_product_1737())

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

print("\nBatch 8 all products generated!")
