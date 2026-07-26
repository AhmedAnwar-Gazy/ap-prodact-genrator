import json, os
from build_1692 import create_product_1692
from build_1694 import create_product_1694
from build_1696 import create_product_1696
from build_lakme import build_lakme_product

products = []
products.append(create_product_1692())
products.append(create_product_1694())
products.append(create_product_1696())
products.append(build_lakme_product(1698, "Blue", "ازرق", "0/70", "8429421207010", "blue-0-70"))
products.append(build_lakme_product(1699, "Green", "اخضر", "0/10", "8429421211116", "green-0-10"))

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

print("\nBatch 3 all products generated!")
