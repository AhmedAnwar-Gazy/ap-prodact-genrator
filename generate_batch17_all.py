import json, os
from build_batch17 import build_johnson_body_wash

products = []

# 1789: Skin-Renewing Oils 400ml
products.append(build_johnson_body_wash(
    1789,
    "بالزيوت المجددة للبشرة",
    "Skin-Renewing Oils",
    "تجديد الحيوية ومرونة الجلد",
    "skin renewal and silky suppleness",
    "3574661543888",
    "johnsons-body-wash-with-skin-renewing-oils-400ml"
))

# 1790: Papaya Extract 400ml
products.append(build_johnson_body_wash(
    1790,
    "بخلاصة البابايا",
    "Papaya Extract",
    "تفتيح ونعومة ونضارة استوائية",
    "brightening, smooth radiance and tropical softness",
    "3574661093666",
    "johnsons-body-wash-with-papaya-extract-400ml"
))

# 1791: Pomegranate Flower Extract 400ml
products.append(build_johnson_body_wash(
    1791,
    "بخلاصة زهرة الرمان",
    "Pomegranate Flower Extract",
    "مضادات الأكسدة وإشراقة وردية مذهلة",
    "antioxidants and vibrant rosy skin glow",
    "3574661093956",
    "johnsons-body-wash-with-pomegranate-flower-extract-400ml"
))

# 1792: Milk, Honey & Oats Extract 400ml
products.append(build_johnson_body_wash(
    1792,
    "بخلاصة اللبن والعسل والشوفان",
    "Milk, Honey & Oats Extract",
    "تهدئة وتغذية مكثفة للبشرة الجافة والحساسة",
    "soothing hydration for dry sensitive skin",
    "3574661385730",
    "johnsons-body-wash-liquid-soap-with-milk-honey-and-oats-extract-400ml"
))

# 1794: Yogurt, Peach, and Coconut Extracts 400ml
products.append(build_johnson_body_wash(
    1794,
    "بخلاصة اللبن والخوخ وجوز الهند",
    "Yogurt, Peach, and Coconut Extracts",
    "انتعاش فاكهي ونعومة مخمليةائقة",
    "fruity freshness and velvet smoothness",
    "3574661385716",
    "johnsons-body-wash-with-yogurt-peach-and-coconut-extracts-400ml"
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

print("\nBatch 17 all products generated!")
