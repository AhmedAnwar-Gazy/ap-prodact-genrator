import json, os
from build_batch12 import create_product_1755, create_product_1757, create_product_1758, create_product_1761, create_product_1762

products = []
products.append(create_product_1755())
products.append(create_product_1757())
products.append(create_product_1758())
products.append(create_product_1761())
products.append(create_product_1762())

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

print("\nBatch 12 all products generated!")
