You are a single Subagent. Your job is to generate the JSON file for Product ID 6148.

1. **Read Instructions**: You MUST read `AGENT_INSTRUCTIONS.md` and `example_high_quality.js` to understand the exact structure, 12-row table, and 20-40 FAQs requirement.
2. **Product Details**: 
   - Product ID: 6148
   - English Name: Pantene Pro-V Anti-Dandruff 2-in-1 Shampoo - 390 ml
   - Arabic Name: بانتين شامبو برو-في ضد القشرة 2 في 1 - 390 مل
   - GTIN (Model): 8700216392785
3. **Research**: Search the web for barcode "8700216392785" and the product name to find accurate ingredients and medical facts.
4. **Generate & Save**: Generate the JSON and save it exactly to `temp/generated_products/6148.json`.
5. **Sync**: Run `node db_sync.js` to push it to the database.
