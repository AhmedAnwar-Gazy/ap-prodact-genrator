import json, os
from build_hair_mask import build_hair_mask_product
from build_batch9 import create_product_1739, create_product_1741, create_product_1742

def create_product_1740():
    # Waxed Mint Dental Floss - 50 Meters
    data = create_product_1739()
    data["product_id"] = "1740"
    data["sku"] = "EK-1740"
    data["gtin"] = "1005160028108"
    data["ar"]["title"] = "خيط اسنان شمعي بالنعناع 50 متر لتنظيف عميق وحماية اللثة"
    data["ar"]["meta_title"] = "خيط اسنان شمعي بالنعناع 50 متر | صيدلية إكليل أبها"
    data["en"]["title"] = "Waxed Mint Dental Floss - 50 Meters"
    data["en"]["meta_title"] = "Waxed Mint Dental Floss 50 Meters | Ekleel Abha Pharmacy"
    data["image_seo"]["image_filename"] = "waxed-mint-dental-floss-50-meters.webp"
    return data

products = []
products.append(build_hair_mask_product(1738, "Argan Oil", "زيت الارغان", "6297938826725", "argan-oil"))
products.append(create_product_1739())
products.append(create_product_1740())
products.append(create_product_1741())
products.append(create_product_1742())

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

print("\nBatch 9 all products generated!")
