import json, os
from build_1685 import create_product_1685
from build_1686 import create_product_1686
from build_beausta import build_beausta_product

products = []
products.append(create_product_1685())
products.append(create_product_1686())
products.append(build_beausta_product(1689, "Purple", "بنفسجي", "#2 Purple", "8809577460888", "purple"))
products.append(build_beausta_product(1690, "Red", "احمر", "#1 Red", "8809577460901", "red"))
products.append(build_beausta_product(1691, "Orange Peach", "برتقالي خوخ", "#3 Orange Peach", "8809577460895", "orange-peach"))

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
    print(f"✅ Product {pid} saved successfully! AR FAQs: {ar_faqs_cnt}, EN FAQs: {en_faqs_cnt}")

print("\nAll 5 Batch 2 products generated!")
