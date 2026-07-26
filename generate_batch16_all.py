import json, os
from build_batch16 import create_product_1783, create_product_ogx

products = []
products.append(create_product_1783())

# 1784: OGX Coconut Milk Shampoo 385ml
products.append(create_product_ogx(
    1784,
    "شامبو بحليب جوز الهند من او جي اكس – 385 مل",
    "OGX Coconut Milk Shampoo – 385 ml",
    "بحليب جوز الهند وبروتينات البياض لترطيب ونعومة الشعر الجاف",
    "with Coconut Milk & Egg White Proteins for dry hair hydration",
    "حليب جوز الهند وبروتينات بياض البيض",
    "Coconut Milk & Egg White Proteins",
    "حليب جوز الهند الطبيعي",
    "natural Coconut Milk",
    ["او_جي_اكس", "شامبو_جوز_الهند", "شامبو_خالي_سلفات", "ترطيب_الشعر", "إكليل_أبها"],
    ["ogx", "coconut_milk_shampoo", "sulfate_free", "hair_hydration", "ekleel_abha"],
    "022796970053",
    "ogx-coconut-milk-shampoo-385ml"
))

# 1785: OGX Biotin & Collagen Shampoo 385ml
products.append(create_product_ogx(
    1785,
    "شامبو بيوتين وكولاجين لتكثيف وتغذية الشعر من او جي اكس - 385 مل",
    "OGX Thick & Full + Biotin & Collagen Shampoo – 385ml",
    "بالبيوتين والكولاجين لتكثيف وتغذية الشعر الخفيف وتكثيف البصيلات",
    "with Biotin & Collagen for thick, full hair density",
    "فيتامين البيوتين والكولاجين المتحلل",
    "Biotin (Vitamin B7) & Hydrolyzed Collagen",
    "البيوتين والكولاجين",
    "Biotin & Collagen",
    ["او_جي_اكس", "شامبو_بيوتين_كولاجين", "تكثيف_الشعر", "شامبو_خالي_سلفات", "إكليل_أبها"],
    ["ogx", "biotin_collagen_shampoo", "hair_thickening", "sulfate_free", "ekleel_abha"],
    "0022796976703",
    "ogx-thick-and-full-biotin-and-collagen-shampoo-385ml"
))

# 1787: OGX Argan Oil of Morocco Shampoo 385ml
products.append(create_product_ogx(
    1787,
    "شامبو بزيت الأرغان المغربي لتجديد وترطيب الشعر من أو جي اكس (OGX) - 385 مل",
    "OGX Renewing + Argan Oil of Morocco Shampoo – 385ml",
    "بزيت الأرغان المغربي النقي لترطيب وتجديد ألياف الشعر التالف",
    "with Moroccan Argan Oil for dry hair renewal",
    "زيت الأرغان المغربي النقي (Argan Oil)",
    "Pure Moroccan Argan Oil",
    "زيت الأرغان المغربي",
    "Moroccan Argan Oil",
    ["او_جي_اكس", "شامبو_الأرغان", "زيت_الأرغان_المغربي", "تجديد_الشعر", "إكليل_أبها"],
    ["ogx", "argan_oil_shampoo", "moroccan_argan", "hair_renewal", "ekleel_abha"],
    "022796976116",
    "ogx-renewing-argan-oil-of-morocco-shampoo-385ml"
))

# 1788: OGX Argan Oil of Morocco Conditioner 385ml
products.append(create_product_ogx(
    1788,
    "أو جي إكس بلسم الأرغان لتغذية وتنعيم الشعر - 385 مل",
    "OGX Renewing + Argan Oil of Morocco Conditioner – 385 ml",
    "بزيت الأرغان المغربي لتغذية وتنعيم وتفكيك تشابك الشعر التالف",
    "with Moroccan Argan Oil to condition & soften dry hair",
    "زيت الأرغان المغربي النقي (Argan Oil)",
    "Pure Moroccan Argan Oil",
    "زيت الأرغان المغربي",
    "Moroccan Argan Oil",
    ["او_جي_اكس", "بلسم_الأرغان", "تنعيم_الشعر", "زيت_الأرغان_المغربي", "إكليل_أبها"],
    ["ogx", "argan_oil_conditioner", "hair_conditioner", "moroccan_argan", "ekleel_abha"],
    "022796971111",
    "ogx-renewing-argan-oil-of-morocco-conditioner-385ml"
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

print("\nBatch 16 all products generated!")
