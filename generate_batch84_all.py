import json, os
from build_batch84 import create_product_2142, create_product_2143, create_product_2144, create_product_2145, create_product_2146

products = [
    create_product_2142(),
    create_product_2143(),
    create_product_2144(),
    create_product_2145(),
    create_product_2146()
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

print("\nBatch 84 all products generated!")
