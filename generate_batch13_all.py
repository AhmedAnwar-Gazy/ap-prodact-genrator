import json, os
from build_batch13 import create_product_1763, create_product_1764, build_disposable_towel_product

products = []
products.append(create_product_1763())
products.append(create_product_1764())
products.append(build_disposable_towel_product(1766, "25*40", "50", "6287022500525", "world-care-disposable-towels-25x40-50pcs"))
products.append(build_disposable_towel_product(1767, "70*140", "25", "6287022500495", "world-care-disposable-towels-70x140-25pcs"))
products.append(build_disposable_towel_product(1768, "50*100", "50", "6287022500501", "world-care-disposable-towels-50x100-50pcs"))

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

print("\nBatch 13 all products generated!")
