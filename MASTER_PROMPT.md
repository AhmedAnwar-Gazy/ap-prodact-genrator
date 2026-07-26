# Massive 5-Agent Orchestrator Prompt (1 PRODUCT PER AGENT + GTIN)

*Copy and paste the prompt below into a new Antigravity conversation inside the `E:\ai_agents\prodacts genrator` workspace. This will spawn 5 agents, assigning exactly ONE product to each agent with its GTIN barcode for precise research.*

***

**Copy the text below:**

```text
Please orchestrate the generation of our product catalog from `raw_products_enriched.csv` (which contains product_id, language_id, name, gtin, and sku columns).

Because we demand absolute masterpiece quality (20-40 FAQs, massive knowledge base), we are using a "1 Product Per Agent" strategy.

Here are your strict instructions as the Orchestrator:

1. **Get Next Batch**: Run the command `node get_next_batch.js`. This script will safely read the CSV, check the `progress.json`, and output EXACTLY the 5 `product_id`s, names, GTINs, and SKUs you need to process right now. Do not try to read the CSV yourself.
2. **Spawn 5 Subagents**: Use your subagent tools to spawn 5 concurrent subagents.
3. **Assign 1 Product**: Give each subagent ONE of the products outputted by `get_next_batch.js`. Give them the exact Product ID, English Name, Arabic Name, GTIN, and SKU provided by the script.
5. **Mandatory Subagent Context**: You MUST pass the full contents of `AGENT_INSTRUCTIONS.md` and `example_high_quality.js` to every single subagent so they understand the extreme depth, exact 12-row table structure, and the 20-40 FAQ requirement. If you don't give them this, they will fail.
6. **Execution & Sync**: Instruct each subagent to:
   a. Search the web using the GTIN barcode first (e.g., search "6295120040348") to identify the exact product.
   b. Then search by product name for detailed medical facts, ingredients, and usage.
   c. Generate the JSON file and save it to `temp/generated_products/{product_id}.json`.
   d. Run `node db_sync.js` to push it to the MySQL database.
7. **Wait and Verify**: Set a timer using your `schedule` tool to wait until all 5 subagents report back that their product is fully synced.
8. **Update Progress**: Once all 5 subagents finish, update the `progress.json` file with the newly completed `product_id`s.
9. **Loop**: Immediately start the next batch of 5 without asking. Keep going until I tell you to stop or all products are done.

IMPORTANT: Quality and medical accuracy are your absolute highest priorities! Each subagent must follow AGENT_INSTRUCTIONS.md to the letter.
```
