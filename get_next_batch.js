const fs = require('fs');
const path = require('path');

const progressFile = path.join(__dirname, 'progress.json');
const batchesDir = path.join(__dirname, 'ai_prodacts');

// Initialize progress file if it doesn't exist
if (!fs.existsSync(progressFile)) {
  fs.writeFileSync(progressFile, JSON.stringify({
    current_batch_id: 1
  }, null, 2));
}

let progress = JSON.parse(fs.readFileSync(progressFile, 'utf8'));
const batchId = progress.current_batch_id || 1;

const currentBatchFile = path.join(batchesDir, `batch_${batchId}.csv`);

if (!fs.existsSync(currentBatchFile)) {
  console.log("ALL DONE! No more batch files to process.");
  process.exit(0);
}

// Read the specific batch file
const csvContent = fs.readFileSync(currentBatchFile, 'utf8');
const lines = csvContent.split(/\r?\n/).filter(l => l.trim());
// Skip header
const dataLines = lines.slice(1);

console.log(`=== BATCH ${batchId} (File: batch_${batchId}.csv) ===`);

let agentIndex = 1;
for (const line of dataLines) {
  // Simple CSV parser handling quotes
  let parts = [];
  let current = '';
  let inQuotes = false;
  for (let i = 0; i < line.length; i++) {
    if (line[i] === '"') {
      inQuotes = !inQuotes;
    } else if (line[i] === ',' && !inQuotes) {
      parts.push(current);
      current = '';
    } else {
      current += line[i];
    }
  }
  parts.push(current);

  // CSV format: product_id,model,name_en,name_ar
  const productId = parts[0];
  const model = parts[1];
  const nameEn = parts[2] || 'N/A';
  const nameAr = parts[3] || 'N/A';

  console.log(`\nSubagent ${agentIndex}:`);
  console.log(`- Product ID: ${productId}`);
  console.log(`- English Name: ${nameEn}`);
  console.log(`- Arabic Name: ${nameAr}`);
  console.log(`- GTIN (Model): ${model}`);
  
  agentIndex++;
}

console.log("\n=================================");

// Increment to next batch
progress.current_batch_id = batchId + 1;
fs.writeFileSync(progressFile, JSON.stringify(progress, null, 2));
console.log(`\nProgress updated. Next run will process batch_${progress.current_batch_id}.csv`);
