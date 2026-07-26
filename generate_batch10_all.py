import json, os
from build_batch10 import create_product_1743, build_powder_product, create_product_1746, create_product_1748

products = []
products.append(create_product_1743())
products.append(build_powder_product(1744, "Moroccan Nila Powder for Face and Body", "بودرة النيلة المغربية الزرقاء الأصلية للوجه والجسم", "Moroccan Blue Nila", "النيلة المغربية الزرقاء", "62870627280", "moroccan-nila-powder"))
products.append(build_powder_product(1745, "Turmeric Powder for Face and Body", "بودرة الكركم للوجه و الجسم", "Natural Turmeric", "الكركم الطبيعي", "6211860954127", "turmeric-powder-for-face-and-body"))
products.append(create_product_1746())
products.append(create_product_1748())

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

print("\nBatch 10 all products generated!")
