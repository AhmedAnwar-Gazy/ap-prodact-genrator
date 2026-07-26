import json, os
from build_batch26 import build_wilkinson_oxygen, create_product_1838, build_nivea_eye_remover

products = []

# 1836: Wilkinson Oxygen 6% (20V) 60ml
products.append(build_wilkinson_oxygen(
    1836,
    "6%",
    "20 فاليوم / 20 Volume",
    "40568201",
    "wilkinson-hair-dye-with-6-percent-oxygen-20-volume-60ml"
))

# 1837: Wilkinson Oxygen 9% (30V) 60ml
products.append(build_wilkinson_oxygen(
    1837,
    "9%",
    "30 فاليوم / 30 Volume",
    "4056800031191",
    "wilkson-hair-color-oxygen-developer-blonde-9-percent-30-volume-60ml"
))

# 1838: Garnier Micellar Sensitive Skin 200ml
products.append(create_product_1838())

# 1839: Nivea Eye Makeup Remover 125ml
products.append(build_nivea_eye_remover(
    1839,
    "4005808571512",
    "nivea-eye-makeup-remover-125ml"
))

# 1840: Nivea Eye Makeup Remover 125ml (Original)
products.append(build_nivea_eye_remover(
    1840,
    "4005900250445",
    "nivea-eye-makeup-remover-125ml-original"
))

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

print("\nBatch 26 all products generated!")
