import json, os
from build_batch7 import create_product_1728, create_product_1730
from build_hair_mask import build_hair_mask_product

def create_product_1729():
    # Johnson Round Cotton Makeup Pads 80 Pads
    data = create_product_1728()
    data["product_id"] = "1729"
    data["sku"] = "EK-1729"
    data["gtin"] = "6291018100019"
    data["brand"] = "Johnson's"
    data["ar"]["title"] = "أقراص قطنية دائرية لإزالة المكياج من جونسون - 80 قرص"
    data["ar"]["meta_title"] = "أقراص قطنية دائرية جونسون 80 قرص | صيدلية إكليل أبها"
    data["en"]["title"] = "Johnson Cotton Makeup Pads, 80 Round Pads"
    data["en"]["meta_title"] = "Johnson Cotton Makeup Pads 80 Round Pads | Ekleel Abha"
    data["schema"]["brand"] = "Johnson's"
    data["image_seo"]["image_filename"] = "johnson-cotton-makeup-pads-80-round-pads.webp"
    return data

products = []
products.append(create_product_1728())
products.append(create_product_1729())
products.append(create_product_1730())
products.append(build_hair_mask_product(1731, "Olive Oil", "زيت الزيتون", "6297938832221", "olive-oil"))
products.append(build_hair_mask_product(1732, "Honey", "العسل", "6297938832726", "honey"))

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

print("\nBatch 7 all products generated!")
