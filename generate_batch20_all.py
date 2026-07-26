import json, os
from build_batch20 import build_vaseline_hand_cream, create_product_1808, create_product_1809

products = []

# 1805: Vaseline Lotion Extremely Dry Skin 75ml
products.append(build_vaseline_hand_cream(
    1805,
    "لوشن فازلين العناية بالبشرة شديدة الجفاف- 75 مل",
    "Vaseline Intensive Care Lotion for Extremely Dry Skin - 75 ml",
    "ترطيب مكثف وعلاج تشققات الأيدي الجافة جداً",
    "intensive hydration for extremely dry and cracked hands",
    "8720181101267",
    "vaseline-intensive-care-lotion-for-extremely-dry-skin-75ml"
))

# 1806: Vaseline Intensive Care Cream 75ml
products.append(build_vaseline_hand_cream(
    1806,
    "كريم فازلين للعناية المكثفة لليدين والأظافر - 75 مل",
    "Vaseline Intensive Care Cream - 75 ml",
    "تغذية الأظافر وتنعيم بشرة اليدين الجافة",
    "nail nutrition and dry hand skin softening",
    "8712561480307",
    "vaseline-intensive-care-cream-75ml"
))

# 1807: Vaseline 2-in-1 Dry Hands Cream 75ml
products.append(build_vaseline_hand_cream(
    1807,
    "كريم اليدين الجاف 2 في 1 من فازلين لترطيب وحماية البشرة - 75 مل",
    "Vaseline 2-in-1 Dry Hands Cream - 75 ml",
    "ترطيب وحماية اليدين 2 في 1 ضد الجفاف والجراثيم",
    "2-in-1 moisture and antibacterial hand protection",
    "8720181053702",
    "vaseline-2-in-1-dry-hands-cream-75ml"
))

# 1808: Sebamed Cleansing Bar pH 5.5
products.append(create_product_1808())

# 1809: Nail Polish Dryer 150ml
products.append(create_product_1809())

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

print("\nBatch 20 all products generated!")
