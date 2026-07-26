import json, os
from build_batch15 import create_product_1777, create_product_1778, create_product_1780, create_product_1781, create_product_1782

products = []
products.append(create_product_1777())
products.append(create_product_1778())
products.append(create_product_1780())
products.append(create_product_1781())
products.append(create_product_1782())

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

print("\nBatch 15 all products generated!")
