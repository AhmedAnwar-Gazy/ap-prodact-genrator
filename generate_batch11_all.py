import json, os
from build_batch11 import create_product_1749, build_sponge_product, create_product_1753

products = []
products.append(create_product_1749())
products.append(build_sponge_product(1750, "اسفنجة استحمام من موروكان اويل لتنظيف وتقشير الجسم بلطف", "Moroccanoil Bath Sponge", "6291100270187", "moroccanoil-bath-sponge-cleansing"))
products.append(build_sponge_product(1751, "اسفنجة استحمام من موروكان اويل", "Moroccanoil Bath Sponge", "6291100270248", "moroccanoil-bath-sponge"))
products.append(build_sponge_product(1752, "اسفنجة استحمام ناعمة ولطيفة للجسم من موروكان اويل", "Moroccanoil Bath Sponge", "6291100278664", "moroccanoil-bath-sponge-soft"))
products.append(create_product_1753())

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

print("\nBatch 11 all products generated!")
