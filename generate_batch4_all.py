import json, os
from build_dove import build_dove_product

products = []
products.append(build_dove_product(1700, "Hair Fall Rescue Shampoo", "ضد تساقط الشعر", "Nutri-Lock Actives", "مركب نوتري لوك الفعال", "200 مل", "6281006423220", "hair-fall-rescue-shampoo"))
products.append(build_dove_product(1702, "Daily Care Shampoo", "عناية يومية لترطيب وحماية الشعر", "Pro-Moisture Complex", "مركب برو-مويستشر المرطب", "600 مل", "6281006423602", "daily-care-shampoo"))
products.append(build_dove_product(1703, "Daily Care Shampoo", "عناية يومية", "Pro-Moisture Complex", "مركب برو-مويستشر المرطب", "200 مل", "6281006423206", "daily-care-shampoo"))
products.append(build_dove_product(1704, "Split End Rescue Shampoo", "لإصلاح الأطراف المتقصفة وتغذية الشعر التالف", "Nutri-Keratin Repair Actives", "مركب نوتري كيراتين لإصلاح الأطراف", "600 مل", "6281006423701", "split-end-rescue-shampoo"))
products.append(build_dove_product(1705, "Nourishing Oil Care Shampoo", "بالزيوت المغذية للعناية بالشعر الجاف والتالف", "Nutri-Oils Complex", "مركب الزيوت المغذية الطبيعية", "600 مل", "6281006423688", "nourishing-oil-care-shampoo"))

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

print("\nBatch 4 all products generated!")
