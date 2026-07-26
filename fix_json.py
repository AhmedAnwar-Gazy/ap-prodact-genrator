import json, os

def fix_json(pid):
    p1 = f"temp/generated_products/{pid}.json"
    p2 = f"../temp/generated_products/{pid}.json"
    for p in [p1, p2]:
        if os.path.exists(p):
            with open(p, "r", encoding="utf-8") as f:
                content = f.read()
            # load with strict=False to handle any raw unescaped control chars
            data = json.loads(content, strict=False)
            with open(p, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

for i in [1690, 1691]:
    fix_json(i)
    print(f"Fixed JSON formatting for product {i}")
