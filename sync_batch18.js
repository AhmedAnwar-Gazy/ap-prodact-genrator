const fs = require('fs');
const mysql = require('mysql2/promise');
const path = require('path');

const dbConfig = {
  host: '168.231.126.10',
  port: 3307,
  user: 'root',
  password: 'root',
  database: 'ekleel_new'
};

const ids = [1795, 1796, 1797, 1798, 1799];

async function syncBatch18() {
  const connection = await mysql.createConnection(dbConfig);
  let count = 0;
  for (const id of ids) {
    let filePath = path.join(__dirname, `temp/generated_products/${id}.json`);
    if (!fs.existsSync(filePath)) {
      filePath = path.join(__dirname, `../temp/generated_products/${id}.json`);
    }
    if (!fs.existsSync(filePath)) {
      console.log(`⚠️  Skipping ${id} - file not found`);
      continue;
    }
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
  console.log(`\n🎉 Batch 18 sync complete! ${count} products updated in MySQL database.`);
}

syncBatch18().catch(err => { console.error('❌ Error:', err); process.exit(1); });
