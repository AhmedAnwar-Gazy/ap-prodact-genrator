import json, os
from build_batch24 import build_garnier_hair_food
from build_batch25 import create_product_1831, create_product_1833, create_product_1834, create_product_1835

products = []

# 1830: Garnier Hair Food Aloe Vera 390ml
products.append(build_garnier_hair_food(
    1830,
    "غارنييه الترا دوكس غذاء الشعر المرطب 3 في 1 بالصبار وجوز الهند - 390 مل",
    "Ultra Doux 3 in 1 moisturizing hair food 390 ml",
    "الصبار وجوز الهند (Aloe Vera & Coconut)",
    "Aloe Vera & Coconut",
    "ترطيباً مكثفاً ونعومة فائقة للشعر الجاف",
    "intense hydration and softness for dry hair",
    "3600542371063",
    "ultra-doux-3-in-1-moisturizing-hair-food-390ml"
))

# 1831: Natural Glycerin Oil 185ml
products.append(create_product_1831())

# 1833: Lux Magical Beauty Body Wash with Loofah 250ml
products.append(create_product_1833())

# 1834: Colgate Plax Mouthwash 500ml
products.append(create_product_1834())

# 1835: Active Mouthwash 300ml
products.append(create_product_1835())

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

print("\nBatch 25 all products generated!")
