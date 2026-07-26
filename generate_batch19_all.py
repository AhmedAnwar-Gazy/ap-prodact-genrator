import json, os
from build_batch19 import build_vicks_vaporub, create_product_1802, build_vaseline_hand_nail

products = []

# 1800: Vicks VapoRub Topical Ointment 50g
products.append(build_vicks_vaporub(1800, "50 جم", "4015600000547", "vicks-vaporub-topical-ointment-50g"))

# 1801: Vicks VapoRub Topical Ointment 100g
products.append(build_vicks_vaporub(1801, "100 جم", "4015600000530", "vicks-vaporub-topical-ointment-100g"))

# 1802: Dove Body Care Cream 150ml
products.append(create_product_1802())

# 1803: Vaseline Intensive Care Healthy Hands & Stronger Nails Cream 75ml
products.append(build_vaseline_hand_nail(
    1803,
    "كريم فازلين الوردي للعناية المتكاملة باليدين والأظافر - 75 مل",
    "Vaseline Intensive Care Healthy Hands & Stronger Nails Cream - 75ml",
    "8712561485524",
    "vaseline-intensive-care-healthy-hands-and-stronger-nails-cream-75ml"
))

# 1804: Vaseline Hand and Nail Cream 75ml
products.append(build_vaseline_hand_nail(
    1804,
    "كريم فازلين العناية الفائقة باليدين والأظافر - 75 مل",
    "Vaseline Hand and Nail Cream - 75 ml",
    "8710447391259",
    "vaseline-hand-and-nail-cream-75ml"
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

print("\nBatch 19 all products generated!")
