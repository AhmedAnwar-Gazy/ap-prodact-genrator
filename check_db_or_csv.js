const mysql = require('mysql2/promise');
const fs = require('fs');
const path = require('path');

const dbConfig = {
  host: '168.231.126.10',
  port: 3307,
  user: 'root',
  password: 'root',
  database: 'ekleel_new'
};

async function check() {
  console.log('Connecting to MySQL DB...');
  const conn = await mysql.createConnection(dbConfig);
  console.log('Connected!');

  // Query product_id, language_id, name from oc_product_description
  const [rows] = await conn.execute(`
    SELECT product_id, language_id, name 
    FROM oc_product_description 
    ORDER BY CAST(product_id AS UNSIGNED) ASC
  `);
  
  console.log(`Total rows in DB oc_product_description: ${rows.length}`);
  
  const productsMap = new Map();
  for (const r of rows) {
    const pid = String(r.product_id);
    if (!productsMap.has(pid)) {
      productsMap.set(pid, { product_id: pid, en_name: '', ar_name: '' });
    }
    const item = productsMap.get(pid);
    if (r.language_id === 1) item.en_name = r.name;
    else if (r.language_id === 2) item.ar_name = r.name;
  }
  
  console.log(`Total Unique Product IDs in DB: ${productsMap.size}`);
  
  // Check which products are already generated in temp/generated_products
  const genDir = path.join(__dirname, 'temp/generated_products');
  let existingFiles = new Set();
  if (fs.existsSync(genDir)) {
    existingFiles = new Set(fs.readdirSync(genDir).filter(f => f.endsWith('.json')).map(f => f.replace('.json', '')));
  }
  console.log(`Existing generated JSON files count: ${existingFiles.size}`);
  
  const allProductIds = Array.from(productsMap.keys());
  const unprocessed = allProductIds.filter(id => !existingFiles.has(id));
  console.log(`Unprocessed product count: ${unprocessed.length}`);
  
  const next20 = unprocessed.slice(0, 20).map(id => productsMap.get(id));
  console.log('\n--- NEXT 20 UNPROCESSED PRODUCTS ---');
  next20.forEach((p, idx) => {
    console.log(`${idx + 1}. ID: ${p.product_id} | EN: "${p.en_name}" | AR: "${p.ar_name}"`);
  });
  
  fs.writeFileSync(path.join(__dirname, 'next_20_products_from_db.json'), JSON.stringify(next20, null, 2));
  
  await conn.end();
}

check().catch(err => {
  console.error('Error:', err);
});
