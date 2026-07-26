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

async function exportProductsWithGTIN() {
  const connection = await mysql.createConnection(dbConfig);
  console.log('Connected to DB');

  // Query DB for products that DO NOT have FAQs generated yet
  const [rows] = await connection.execute(`
    SELECT 
      p.product_id,
      p.model AS gtin,
      p.sku,
      pd.language_id,
      pd.name
    FROM oc_product p
    JOIN oc_product_description pd ON p.product_id = pd.product_id
    WHERE pd.faqs IS NULL OR pd.faqs = '' OR pd.faqs = '<p><br></p>'
    ORDER BY p.product_id, pd.language_id
  `);

  console.log(`Fetched ${rows.length} rows from DB that need generation`);

  // Write enriched CSV
  const outputPath = path.join(__dirname, 'raw_products_enriched.csv');
  let csv = 'product_id,language_id,name,gtin,sku\n';
  
  for (const row of rows) {
    const escapedName = `"${(row.name || '').replace(/"/g, '""')}"`;
    const gtin = `"${(row.gtin || '').replace(/"/g, '""')}"`;
    const sku = `"${(row.sku || '').replace(/"/g, '""')}"`;
    csv += `${row.product_id},${row.language_id},${escapedName},${gtin},${sku}\n`;
  }

  fs.writeFileSync(outputPath, csv, 'utf8');
  console.log(`Filtered Enriched CSV written to: ${outputPath}`);

  // Reset progress file
  const progressFile = path.join(__dirname, 'progress.json');
  fs.writeFileSync(progressFile, JSON.stringify({
    last_processed_index: 0,
    completed_product_ids: []
  }, null, 2));
  console.log('Reset progress.json to start from index 0.');

  await connection.end();
}

exportProductsWithGTIN().catch(console.error);
