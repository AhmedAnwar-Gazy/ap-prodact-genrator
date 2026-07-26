import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
    try {
        const body = await req.json();
        
        // Destructure all possible fields from the incoming product object
        const { 
            name, 
            brand = '', 
            category = '', 
            description = '', 
            attributes = {}, 
            ingredients = [], 
            size = '', 
            sku = '', 
            language = 'ar' 
        } = body;

        console.log('[API] AI Content generation requested for:', { name, language });

        if (!name) {
            return NextResponse.json({ error: "Product name is required" }, { status: 400 });
        }

        const apiKey = process.env.NEXT_PUBLIC_OPEN_ROUTER_KEY;
        if (!apiKey) {
            console.error('[API] No API key found in environment variables (OPEN_ROUTER_KEY)');
            return NextResponse.json(
                { error: "API key not configured." },
                { status: 500 }
            );
        }

        const isEnglish = language === 'en';

        // 1. System Prompt (Brand Identity, Compliance, Language Rules)
        const systemPrompt = `You are the AI SEO Content Specialist for Ekleel Abha.

Ekleel Abha is a Saudi Arabian pharmacy and beauty e-commerce platform specializing in:
- Skincare
- Haircare
- Cosmetics
- Personal care
- Medical supplies
- Wellness products

Brand values:
- Authentic products
- Quality
- Customer trust
- Professional pharmacy standards
- Saudi market relevance

Your writing style:
- Professional, clinical yet approachable
- Informative and educational — not just marketing fluff
- Trustworthy and authoritative (pharmacy-grade tone)
- Clear, structured, and easy to scan
- Suitable for customers who want to understand what they are buying

${isEnglish 
  ? `IMPORTANT: Generate ALL output in English.` 
  : `For Arabic SEO:
Use Saudi e-commerce terminology.
Prefer: شراء, اطلب الآن, متوفر, أصلي, توصيل سريع.
Avoid: generic MSA only. Use natural Saudi shopping language.`}

Medical Compliance Rules:
Never claim: يعالج, يشفي, يقضي على المرض, نتيجة مضمونة (or English equivalents: cures, heals, guarantees).
Use: يساعد على, يدعم, يساهم في, مناسب لـ (or English equivalents: helps with, supports, contributes to, suitable for).
For medical products, require: usage, warnings, instructions, target users.

CONTENT DEPTH RULES:
The "description" field must be a comprehensive, informative product page — NOT just marketing copy.
Structure the HTML description using <h2> and <h3> sections in this order:

${isEnglish ? `
1. Product Overview — A concise 2-3 sentence summary of what the product is, who it's for, and its key benefit.
2. Key Benefits — Bullet list of the main benefits (3-6 items).
3. How to Use / Instructions for Use — Step-by-step usage instructions. Be specific: amount, frequency, method, timing (morning/night), body area. If the product has dosage info, include it.
4. Ingredients Overview — Highlight key active ingredients and their roles. Use the provided ingredients list if available.
5. Warnings & Precautions — Patch test advice, storage instructions, contraindications, "consult a doctor if..." statements.
6. Who Is This For? — Target audience section: skin type, age range, specific concerns it addresses.
` : `
1. نظرة عامة على المنتج — A concise 2-3 sentence summary of what the product is, who it's for, and its key benefit.
2. الفوائد الرئيسية — Bullet list of the main benefits (3-6 items).
3. طريقة الاستخدام — Step-by-step usage instructions. Be specific: amount, frequency, method, timing (morning/night), body area. If the product has dosage info, include it.
4. نظرة عامة على المكونات — Highlight key active ingredients and their roles. Use the provided ingredients list if available.
5. تحذيرات واحتياطات — Patch test advice, storage instructions, contraindications, "consult a doctor if..." statements.
6. لمن هذا المنتج — Target audience section: skin type, age range, specific concerns it addresses.
`}

For each section, write factual, helpful content. Avoid empty superlatives. Use data and specifics wherever possible.

You MUST respond strictly with a JSON object. Do not output any markdown formatting outside of the JSON.`;

        // 2. Dynamic Category Template
        let categoryTemplate = '';
        let faqTemplate = 'When generating the "faqs" field, include 20-40 questions relevant to the product. Answer them thoroughly.';
        const catLower = category.toLowerCase();
        if (catLower.includes('skin') || catLower.includes('بشرة')) {
            categoryTemplate = `For this skincare product, the description MUST include:
- Skin type suitability (oily, dry, combination, sensitive)
- Texture and absorption feel
- Key active ingredients and their dermatological roles
- Step-by-step usage within a skincare routine ( cleanser → toner → THIS → moisturizer → SPF)
- Frequency of use (daily, twice daily, weekly)
- Expected timeline for visible results (if applicable)
- Patch test and sensitivity warnings`;
        } else if (catLower.includes('hair') || catLower.includes('شامبو') || catLower.includes('شعر')) {
            categoryTemplate = `For this haircare product, the description MUST include:
- Hair type suitability (curly, straight, fine, thick, color-treated)
- Hair concerns addressed (damage, frizz, thinning, dandruff, dryness)
- Formula benefits and key ingredients
- Application method: amount, massage technique, rinse instructions
- Frequency of use and leave-in vs rinse-out instructions
- Compatibility with other hair treatments`;
        } else if (catLower.includes('supplement') || catLower.includes('فيتامين') || catLower.includes('مكمل')) {
            categoryTemplate = `For this supplement/health product, the description MUST include:
- Health benefits supported (with specific nutrient roles)
- Recommended dosage and timing (with or without food)
- Key ingredients with amounts per serving
- Who should use it and who should avoid it
- Drug interactions or contraindications warnings
- Storage and shelf life information
- "Consult your doctor" disclaimers where appropriate`;
        } else if (catLower.includes('cosmetic') || catLower.includes('makeup') || catLower.includes('مكياج')) {
            categoryTemplate = `For this cosmetic product, the description MUST include:
- Finish type (matte, dewy, satin, glossy)
- Coverage level if applicable (sheer, medium, full)
- Shade range or color description
- Application method and tools recommended
- Longevity and wear time
- Skin type compatibility
- Removal instructions`;
            faqTemplate = `When generating the "faqs" field, include 20-40 questions. Answer them thoroughly. Include questions like: What is it? Benefits? Shade? Skin type? Finish? Coverage? Longevity? Waterproof? Transfer-proof? Blending? Tools needed? Fragrance? Comedogenic? Sensitive skin? Vegan? Removal?`;
        } else if (catLower.includes('medical') || catLower.includes('طبي') || catLower.includes('devices') || catLower.includes('pharma') || catLower.includes('أدوية')) {
            categoryTemplate = `For this medical/health product, the description MUST include:
- Intended medical use and target condition
- How it works (mechanism of action in simple terms)
- Step-by-step usage instructions
- Precautions and warnings (prominent section)
- Storage conditions
- When to consult a healthcare professional
- Certifications or regulatory notes if applicable`;
            faqTemplate = `When generating the "faqs" field, include 20-40 questions. Answer them thoroughly. Include questions like: What is it and indications? Benefits? Mechanism of action? Onset? Duration? Dosage? Daily use? With food? Side effects? When to stop? Contraindications? Interactions? Pregnancy/Breastfeeding? Elderly/Children? Driving? Drowsiness? Weight gain? Kidneys/Liver/Blood pressure/Diabetes impact? Alternatives? Missed dose? Overdose? Storage? When to see a doctor?`;
        }

        // 3. User Prompt (The Product Data + Keyword Analysis + Output format)
        const userPrompt = `Generate a complete, informative SEO content package for the following product. This is NOT just marketing copy — it must be a comprehensive, pharmacy-grade product page that educates the customer.

Product Data:
{
  "name": "${name}",
  "brand": "${brand}",
  "category": "${category}",
  "current_description": "${description}",
  "attributes": ${JSON.stringify(attributes)},
  "ingredients": ${JSON.stringify(ingredients)},
  "size": "${size}",
  "sku": "${sku}"
}

${categoryTemplate}
${faqTemplate}

Please perform the following workflow internally:
1. Keyword Analysis: Determine primary, secondary, long-tail keywords, and search intent.
2. Content Generation: Write a thorough, informative, and professional product description.
3. SEO Validation: Ensure meta titles are <60 chars, descriptions <160 chars, and no prohibited medical claims are made.

CRITICAL RULES FOR THE FIELDS:
- "description": Write as a complete HTML product page. Structure with <h2> sections using the exact section names provided in the rules above. Use <ul>/<li> for lists.
- "specifications": Create an HTML structured table. Use <table>, <tbody>, <tr>, <th> for labels, and <td> for values. ${isEnglish ? "Include Brand, Category, Product Type, Volume/Weight, Skin/Hair Type, Finish, Texture, Fragrance, Active Ingredients, Country of Origin, Manufacturer, Age Group." : "The <th> labels MUST be in Arabic: العلامة التجارية, الفئة, نوع المنتج, الحجم/الوزن, نوع البشرة/الشعر, المظهر النهائي, الملمس, العطر, المكونات النشطة, بلد المنشأ, الشركة المصنعة, الفئة العمرية."}
- "knowledge_base": Write educational HTML content targeting AI search (GEO). Answer: What problem does this solve? Why does this condition happen? Prevention tips, Professional recommendations, Common myths, Scientific explanation. Use H2/H3 structure.
- "faqs": Generate a robust FAQ section formatted in HTML (using <h3> for questions and <p> for answers). You must aim for 20-40 questions if the product warrants it. Provide detailed answers.

Output the result strictly in this JSON format:
{
  "title": "Optimized H1 product title (accurate, not clickbait)",
  "meta_title": "SEO title under 60 chars",
  "meta_description": "SEO description under 160 chars, informative and high CTR",
  "description": "Full HTML product description without specifications or faqs. Use <h2> and <h3> tags for structuring.",
  "specifications": "HTML formatted specifications strictly as an HTML table using <table>, <tr>, <th>, <td> tags",
  "knowledge_base": "HTML formatted educational knowledge base content",
  "faqs": "HTML formatted FAQ section with 20-40 Q&A pairs. Use <h3> for the question and <p> for the answer.",
  "keywords": {
    "primary_keyword": "",
    "secondary_keywords": [],
    "long_tail": [],
    "search_intent": ""
  },
  "tags": ["tag1", "tag2", "tag3"],
  "schema": {
    "brand": "${brand}",
    "category": "${category}",
    "availability": "InStock"
  },
  "internal_linking": {
    "related_category": "Name of the main category to link to",
    "related_products": ["Name of product 1", "Name of product 2"]
  },
  "image_seo": {
    "image_filename": "seo-friendly-filename.webp",
    "alt": "Optimized alt text describing the product",
    "title": "Image title attribute"
  }
}

Ensure the response is valid JSON.`;

        console.log('[API] Calling OpenRouter API in JSON mode...');

        const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${apiKey}`,
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:3001",
                "X-Title": "Ekleel Abha AI SEO Engine",
            },
            body: JSON.stringify({
                model: "google/gemini-3.5-flash",
                provider: {
                    order: ["google-ai-studio"],
                    allow_fallbacks: false
                },
                messages: [
                    {
                        role: "system",
                        content: systemPrompt,
                    },
                    {
                        role: "user",
                        content: userPrompt,
                    },
                ],
                temperature: 0.2, // Lower temperature for consistent SEO formatting
                response_format: { type: "json_object" }
            }),
        });

        if (!response.ok) {
            const errorData = await response.text();
            console.error("[API] OpenRouter API error:", errorData);
            return NextResponse.json(
                { error: "Failed to generate content from AI service", details: errorData },
                { status: response.status }
            );
        }

        const data = await response.json();
        const content = data.choices[0]?.message?.content;

        if (!content) {
            throw new Error("No content received from AI");
        }

        // Parse the JSON response
        let parsedContent;
        try {
            parsedContent = JSON.parse(content);
        } catch (e) {
            console.error("[API] Failed to parse AI JSON response:", content);
            return NextResponse.json({ error: "AI returned invalid JSON" }, { status: 500 });
        }

        console.log('[API] Successfully generated SEO content package');
        
        return NextResponse.json(parsedContent);

    } catch (error) {
        console.error("[API] Error generating content:", error);
        return NextResponse.json(
            { error: "Failed to generate content", message: error instanceof Error ? error.message : "Unknown error" },
            { status: 500 }
        );
    }
}
