import json, os
from build_1706 import create_product_1706
from build_1707 import create_product_1707
from build_1710 import create_product_1710
from build_dove import build_dove_product

products = []
products.append(create_product_1706())
products.append(create_product_1707())
products.append(build_dove_product(1708, "Intensive Repair Shampoo", "لإصلاح مكثّف", "Nutri-Keratin Repair Actives", "مركب نوتري كيراتين لإصلاح التلف العميق", "600 مل", "6281006423640", "intensive-repair-shampoo"))
products.append(build_dove_product(1709, "2-in-1 Shampoo and Conditioner", "٢ في ١ للشعر العادي والجاف", "Pro-Moisture Complex", "مركب برو-مويستشر المرطب المزدوج", "600 مل", "6281006423589", "2-in-1-shampoo-and-conditioner"))
products.append(create_product_1710())

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

print("\nBatch 5 all products generated!")
