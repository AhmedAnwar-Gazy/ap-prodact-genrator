# Product Generator Agent Instructions (ULTIMATE MEDICAL QUALITY)

Welcome, Antigravity Agent! Your task is to generate extremely high-quality, medical-grade SEO content for products using your own advanced LLM capabilities (no external API keys).

You are generating content for a premium medical supplies and pharmacy e-commerce store in Saudi Arabia (Ekleel Abha). 

## CRITICAL DIRECTIVE: RESEARCH FIRST USING GTIN
You will receive the product `name`, `gtin` (barcode), and `sku` from the enriched CSV. **Before you write anything**, you MUST:
1. **Search the web using the GTIN barcode number** (e.g., search "6295120040348" or "barcode 6295120040348"). This gives you the EXACT product identity — no guessing.
2. Also search by product name to find: active ingredients, size, medical benefits, official usage instructions, and manufacturer details.
3. Cross-reference both searches to ensure 100% accuracy. DO NOT HALLUCINATE MEDICAL DATA.

## LENGTH AND DEPTH RULE (NO SHORTCUTS)
You MUST generate massive, deep, exhaustive content. Do NOT write 1-sentence answers. If you write short, lazy content, you have failed your mission.

## EXACT PROMPT & STRUCTURE
You must internally run the following prompt for EVERY product. Match the exact structure and extreme length:

---

### 1. `description` (Rich HTML - Minimum 500 words)
You MUST include these EXACT headers in `<h2>`:
1. **نظرة عامة على المنتج** (Product Overview - 2 paragraphs)
2. **الفوائد الرئيسية** (Key Benefits - 5 to 7 detailed bullet points)
3. **طريقة الاستخدام** (How to use - 4 to 5 step-by-step bullet points)
4. **نظرة عامة على المكونات** (Ingredients Overview - 4 to 5 bullet points explaining the science of the active ingredients)
5. **تحذيرات واحتياطات** (Warnings and Precautions - 3 to 4 bullet points)
6. **لمن هذا المنتج** (Who is this for - 3 to 4 bullet points)

*(Adapt the content based on the Category: Skin, Hair, Supplement, or Medical as appropriate).*

### 2. `specifications` (HTML Table - STRICTLY 12 ROWS)
Create an HTML structured table (`<table>`, `<tbody>`, `<tr>`, `<th>` for labels, `<td>` for values). 
**CRITICAL RULE: YOU MUST INCLUDE EXACTLY THESE 12 ROWS IN THIS EXACT ORDER. DO NOT OMIT ANY ROW.**
If you do not have the exact data for a row, you MUST infer it logically based on the product (e.g., if it is a gel cleanser, the Texture is "Gel", the Age Group is "Adults/Teens"). Do NOT leave it out.

**The Arabic `<th>` labels MUST be:**
1. العلامة التجارية
2. الفئة
3. نوع المنتج
4. الحجم/الوزن
5. نوع البشرة/الشعر
6. المظهر النهائي
7. الملمس
8. العطر
9. المكونات النشطة
10. بلد المنشأ
11. الفئة العمرية

### 3. `knowledge_base` (Rich HTML - Minimum 5 Sections)
Write deep, educational HTML content targeting AI search (GEO). You MUST include these EXACT 5 headers (using `<h3>`):
1. **ما هي المشكلة التي يحلها هذا المنتج؟** (What problem does this solve? - Detailed paragraph)
2. **لماذا تحدث هذه المشكلة؟** (Why does this condition happen? - Detailed paragraph)
3. **نصائح وقائية** (Prevention tips - Bullet points)
4. **خرافات شائعة** (Common myths - Bullet points of Myth vs Fact)
5. **التفسير العلمي** (Scientific explanation of the mechanism - Detailed paragraph)

### 4. `faqs` (Rich HTML - 20 to 40 Questions)
Generate a robust FAQ section (`<h3>` for questions, `<p>` for answers). 
**CRITICAL RULES FOR FAQS:**
- You MUST generate EXACTLY 20 TO 40 QUESTIONS. 
- **NO SHORT ANSWERS.** Every single answer MUST be a detailed paragraph (at least 2-3 sentences). One-line answers are strictly forbidden.
- Cover indications, benefits, mechanism, onset, duration, side effects, contraindications, pregnancy safety, interactions, storage, alternatives.

### 5. Bilingual Requirement
You must output a single JSON object containing two main keys: `ar` and `en`.
The Arabic MUST be native, professional medical Arabic (do not use literal machine translation). The English must be native. Both must have the exact same depth.

---

## Workflow for the Subagent
1. You will be assigned EXACTLY ONE `product_id` by the Orchestrator, along with its English and/or Arabic name.
2. **Search the web** to get the real ingredients and facts for this specific product.
3. Generate the full JSON object exactly matching the extreme depth and rules above.
4. Save the file to the `temp/generated_products` directory named `{product_id}.json`.
5. Run `node db_sync.js` to push your single generated file directly into the MySQL database.
6. Report back to the Orchestrator that your product is successfully synced.
