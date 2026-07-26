const fs = require('fs');
const path = require('path');
const mysql = require('mysql2/promise');

const generatedDir = path.join(__dirname, '../temp/generated_products');

const dbConfig = {
  host: '168.231.126.10',
  port: 3307,
  user: 'root',
  password: 'root',
  database: 'ekleel_new'
};

async function forceSyncAll() {
  console.log('⚡ Force-syncing products directly to MySQL DB...');
  
  let targetDir = path.join(__dirname, '../temp/generated_products');
  if (!fs.existsSync(targetDir)) {
    const localDir = path.join(__dirname, 'temp/generated_products');
    if (fs.existsSync(localDir)) {
      targetDir = localDir;
    } else {
      fs.mkdirSync(targetDir, { recursive: true });
    }
  }

  const files = fs.readdirSync(targetDir).filter(f => {
    if (!f.endsWith('.json')) return false;
    const id = parseInt(f.replace('.json', ''), 10);
    return !isNaN(id);
  });

  if (files.length === 0) {
    // Check if the other folder has files
    const localDir = path.join(__dirname, 'temp/generated_products');
    if (fs.existsSync(localDir)) {
      const localFiles = fs.readdirSync(localDir).filter(f => f.endsWith('.json') && !isNaN(parseInt(f.replace('.json', ''), 10)));
      if (localFiles.length > 0) {
        targetDir = localDir;
        files.push(...localFiles);
      }
    }
  }

  if (files.length === 0) {
    console.log('⚠️  No generated product files found.');
    process.exit(0);
  }

  console.log(`🚀 Found ${files.length} product files in ${targetDir} to sync immediately.`);
  const connection = await mysql.createConnection(dbConfig);

  let count = 0;
  for (const file of files) {
    const filePath = path.join(targetDir, file);
    const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    
    const productId = data.product_id;
    count++;

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

    console.log(`[${count}/${files.length}] ✅ Product #${productId} updated in DB (AR & EN).`);
  }

  console.log(`🎉 Completed direct sync for all ${files.length} products in range 6400 - 6499!`);
  await connection.end();
}

forceSyncAll().catch(err => {
  console.error('❌ Sync failed:', err);
  process.exit(1);
});
