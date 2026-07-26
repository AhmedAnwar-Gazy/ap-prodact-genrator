import json, os
from build_batch6 import create_product_1711, create_product_1714, create_product_1726
from build_dove import build_dove_product

def create_product_1713():
    # Sunsilk Strength & Shine 400ml
    data = create_product_1711()
    data["product_id"] = "1713"
    data["sku"] = "EK-1713"
    data["gtin"] = "6281006424388"
    data["ar"]["title"] = "شامبو صانسيلك قوة ولمعان لتقوية وتغذية الشعر الباهت - 400 مل"
    data["ar"]["meta_title"] = "شامبو صانسيلك قوة ولمعان 400مل | صيدلية إكليل أبها"
    data["en"]["title"] = "Sunsilk Strength & Shine Shampoo, 400ml"
    data["en"]["meta_title"] = "Sunsilk Strength & Shine Shampoo 400ml | Ekleel Abha"
    data["image_seo"]["image_filename"] = "sunsilk-strength-and-shine-shampoo-400ml.webp"
    return data

def create_product_1717():
    # TRESemme Botanix 400ml
    data = build_dove_product(1717, "Botanix Nourish & Replenish Shampoo", "بوتانيكس تغذية وترميم مع جوز الهند والألوفيرا", "Botanix Botanical Complex", "مركب جوز الهند والألوفيرا النباتي", "400 مل", "6281006564169", "botanix-shampoo")
    data["brand"] = "TRESemmé"
    data["schema"]["brand"] = "TRESemmé"
    return data

products = []
products.append(create_product_1711())
products.append(create_product_1713())
products.append(create_product_1714())
products.append(create_product_1717())
products.append(create_product_1726())

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

print("\nBatch 6 all products generated!")
