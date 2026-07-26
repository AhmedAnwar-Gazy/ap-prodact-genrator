const fs = require('fs');
const path = require('path');
const mysql = require('mysql2/promise');

const dbConfig = {
  host: '168.231.126.10',
  port: 3307,
  user: 'root',
  password: 'root',
  database: 'ekleel_new'
};

async function syncSingleProduct() {
  console.log('⚡ Syncing Product 4220 directly to MySQL DB...');
  
  const filePath = path.join(__dirname, 'temp/generated_products/4220.json');
  if (!fs.existsSync(filePath)) {
    console.error('❌ File 4220.json not found in temp/generated_products!');
    process.exit(1);
  }

  const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
  const productId = data.product_id;

  const connection = await mysql.createConnection(dbConfig);

  // --- ARABIC (language_id = 2) ---
  const updateArQuery = `
    UPDATE oc_product_description 
    SET description = ?, meta_title = ?, meta_description = ?, tag = ?, specifications = ?, knowledge_base = ?, faqs = ?
    WHERE product_id = ? AND language_id = 2
  `;
  const arValues = [
    data.ar.description,
    data.ar.meta_title || '',
    data.ar.meta_description || '',
    data.ar.tags ? data.ar.tags.join(',') : '',
    data.ar.specifications || '',
    data.ar.knowledge_base || '',
    data.ar.faqs || '',
    productId
  ];
  await connection.execute(updateArQuery, arValues);

  // --- ENGLISH (language_id = 1) ---
  const updateEnQuery = `
    UPDATE oc_product_description 
    SET description = ?, meta_title = ?, meta_description = ?, tag = ?, specifications = ?, knowledge_base = ?, faqs = ?
    WHERE product_id = ? AND language_id = 1
  `;
  const enValues = [
    data.en.description,
    data.en.meta_title || '',
    data.en.meta_description || '',
    data.en.tags ? data.en.tags.join(',') : '',
    data.en.specifications || '',
    data.en.knowledge_base || '',
    data.en.faqs || '',
    productId
  ];
  await connection.execute(updateEnQuery, enValues);

  console.log(`✅ Product #${productId} updated successfully in DB (AR & EN).`);
  await connection.end();
}

syncSingleProduct().catch(err => {
  console.error('❌ Sync failed:', err);
  process.exit(1);
});
