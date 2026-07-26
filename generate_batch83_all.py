import json, os
from build_batch83 import create_product_2137, create_product_2138, create_product_2139, create_product_2140, create_product_2141

products = [
    create_product_2137(),
    create_product_2138(),
    create_product_2139(),
    create_product_2140(),
    create_product_2141()
]

for pdata in products:
    pid = pdata["product_id"]
    out_dir = "temp/generated_products"
    os.makedirs(out_dir, exist_ok=True)
    with open(f"{out_dir}/{pid}.json", "w", encoding="utf-8") as f:
        json.dump(pdata, f, ensure_ascii=False, indent=2)
    ar_h2 = pdata["ar"]["description"].count("<h2>")
    ar_tr = pdata["ar"]["specifications"].count("<tr>")
    ar_kb = pdata["ar"]["knowledge_base"].count("<h3>")
    ar_faqs = pdata["ar"]["faqs"].count("<h3>")
    en_faqs = pdata["en"]["faqs"].count("<h3>")
    print(f"Product {pid}: H2={ar_h2}, SpecsTr={ar_tr}, KB_H3={ar_kb}, AR_FAQs={ar_faqs}, EN_FAQs={en_faqs}")

print("\nBatch 83 all products generated!")
