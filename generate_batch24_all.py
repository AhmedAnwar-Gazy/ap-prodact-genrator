import json, os
from build_batch24 import build_garnier_hair_food, create_product_1825, create_product_1826

products = []

# 1825: Johnson's Micellar Wipes 25s
products.append(create_product_1825())

# 1826: Feminine Wipes Musk 20s
products.append(create_product_1826())

# 1827: Garnier Hair Food Papaya 390ml
products.append(build_garnier_hair_food(
    1827,
    "غارنييه الترا دوكس غذاء الشعر المرمم 3 في 1 بالبابايا - 390 مل",
    "Ultra Doux 3-in-1 Repairing Hair Food - 390ml",
    "البابايا المرممة (Papaya)",
    "Repairing Papaya",
    "ترميماً عميقاً للأطراف المتقصفة",
    "deep hair fiber repair and split end sealing",
    "3600542370271",
    "ultra-doux-3-in-1-repairing-hair-food-390ml"
))

# 1828: Garnier Hair Food Banana 390ml
products.append(build_garnier_hair_food(
    1828,
    "غذاء الشعر المغذي 3 في 1 بالموز للشعر الجاف من غارنييه الترا دوكس - 390 مل",
    "Ultra Doux Nourishing 3-in-1 Hair Food 390ml",
    "الموز المغذي (Nourishing Banana)",
    "Nourishing Banana",
    "تغذية فائقة ونعومة حريرية للشعر الجاف",
    "intense nourishment and silky softness for dry hair",
    "3600542370110",
    "ultra-doux-nourishing-3-in-1-hair-food-390ml"
))

# 1829: Garnier Hair Food Coconut & Macadamia 390ml
products.append(build_garnier_hair_food(
    1829,
    "غارنييه الترا دوكس غذاء الشعر المنعم 3 في 1 بجوز الهند والمكاديميا للشعر الجاف 390 مل",
    "Ultra Doux 3-in-1 Smoothing Hair Food with Coconut and Macadamia for Dry Hair - 390ml",
    "جوز الهند والمكاديميا (Coconut & Macadamia)",
    "Coconut & Macadamia",
    "تنعيم فائق وضبط هيشان الشعر الجاف",
    "intense smoothing and frizz control for dry hair",
    "3600542370196",
    "ultra-doux-3-in-1-smoothing-hair-food-with-coconut-and-macadamia-for-dry-hair-390ml"
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

print("\nBatch 24 all products generated!")
