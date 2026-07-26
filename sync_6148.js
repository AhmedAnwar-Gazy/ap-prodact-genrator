const fs = require('fs');
const mysql = require('mysql2/promise');

const dbConfig = {
  host: '168.231.126.10',
  port: 3307,
  user: 'root',
  password: 'root',
  database: 'ekleel_new'
};

async function sync6148() {
  const data = JSON.parse(fs.readFileSync('./temp/generated_products/6148.json', 'utf8'));
  const connection = await mysql.createConnection(dbConfig);

  const updateArQuery = `
    UPDATE oc_product_description 
    SET description = ?, meta_title = ?, meta_description = ?, tag = ?, specifications = ?, knowledge_base = ?, faqs = ?
    WHERE product_id = ? AND language_id = 2
  `;
  await connection.execute(updateArQuery, [
    data.ar.description,
    data.ar.meta_title || '',
    data.ar.meta_description || '',
    data.ar.tags ? data.ar.tags.join(',') : '',
    data.ar.specifications || '',
    data.ar.knowledge_base || '',
    data.ar.faqs || '',
    6148
  ]);

  const updateEnQuery = `
    UPDATE oc_product_description 
    SET description = ?, meta_title = ?, meta_description = ?, tag = ?, specifications = ?, knowledge_base = ?, faqs = ?
    WHERE product_id = ? AND language_id = 1
  `;
  await connection.execute(updateEnQuery, [
    data.en.description,
    data.en.meta_title || '',
    data.en.meta_description || '',
    data.en.tags ? data.en.tags.join(',') : '',
    data.en.specifications || '',
    data.en.knowledge_base || '',
    data.en.faqs || '',
    6148
  ]);

  console.log('✅ Product #6148 successfully updated in DB (AR & EN).');
  await connection.end();
}

sync6148().catch(err => {
  console.error('❌ Sync failed:', err);
  process.exit(1);
});
