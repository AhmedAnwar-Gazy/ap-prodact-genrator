import json, os
from build_batch18 import create_product_1795, build_rembrandt_body_mist

products = []
products.append(create_product_1795())

# 1796: Rembrandt Roses Vanilla Body Mist 200ml
products.append(build_rembrandt_body_mist(
    1796,
    "روزس فانيلا",
    "Roses Vanilla",
    "الورد والجوري مع دفقات الفانيلا الدافئة",
    "romantic rose petals and warm vanilla sweetness",
    "6281056589204",
    "rembrandt-roses-vanilla-body-mist-200ml"
))

# 1797: Rembrandt Supreme Floral Body Mist 200ml
products.append(build_rembrandt_body_mist(
    1797,
    "سوبريم فلورل",
    "Supreme Floral",
    "الزهور الملكية والياسمين الناعم",
    "royal floral bouquet and soft jasmine",
    "6281056589211",
    "rembrandt-supreme-floral-body-mist-200ml"
))

# 1798: Rembrandt Shake the Night Body Mist 200ml
products.append(build_rembrandt_body_mist(
    1798,
    "شاك ذا نايت",
    "Shake the Night",
    "العنبر الليلي والزهور الشرقية الساحرة",
    "night amber and mysterious oriental florals",
    "6281056589235",
    "rembrandt-shake-the-night-body-mist-200ml"
))

# 1799: Rembrandt Life Beige Body Mist 200ml
products.append(build_rembrandt_body_mist(
    1799,
    "لايف بيج",
    "Life Beige",
    "المسك الأبيض وخشب الصندل الدافئ",
    "white musk and soothing sandalwood",
    "6281056589228",
    "rembrandt-life-beige-body-mist-200ml"
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

print("\nBatch 18 all products generated!")
