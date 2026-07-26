const fs = require('fs');
const mysql = require('mysql2/promise');
const path = require('path');

const dbConfig = { host: '168.231.126.10', port: 3307, user: 'root', password: 'root', database: 'ekleel_new' };
const ids = [2061, 2062, 2063, 2064, 2065];

async function syncBatch69() {
  const connection = await mysql.createConnection(dbConfig);
  let count = 0;
  for (const id of ids) {
    const filePath = path.join(__dirname, `temp/generated_products/${id}.json`);
    if (!fs.existsSync(filePath)) { console.log(`⚠️  Skipping ${id}`); continue; }
    const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    await connection.execute(
      `UPDATE oc_product_description SET description=?, meta_title=?, meta_description=?, tag=?, specifications=?, knowledge_base=?, faqs=? WHERE product_id=? AND language_id=2`,
      [data.ar.description, data.ar.meta_title||'', data.ar.meta_description||'', data.ar.tags?data.ar.tags.join(','):'', data.ar.specifications||'', data.ar.knowledge_base||'', data.ar.faqs||'', id]
    );
    await connection.execute(
      `UPDATE oc_product_description SET description=?, meta_title=?, meta_description=?, tag=?, specifications=?, knowledge_base=?, faqs=? WHERE product_id=? AND language_id=1`,
      [data.en.description, data.en.meta_title||'', data.en.meta_description||'', data.en.tags?data.en.tags.join(','):'', data.en.specifications||'', data.en.knowledge_base||'', data.en.faqs||'', id]
    );
    count++;
    console.log(`✅ [${count}/${ids.length}] Product #${id} synced to DB (AR & EN).`);
  }
  await connection.end();
  console.log(`\n🎉 Batch 69 sync complete! ${count} products updated in MySQL database.`);
}

syncBatch69().catch(err => { console.error('❌ Error:', err); process.exit(1); });
