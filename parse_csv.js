const fs = require('fs');
const path = require('path');

console.log('Files in directory:', fs.readdirSync(__dirname));

let csvFile = fs.readdirSync(__dirname).find(f => f.toLowerCase() === 'raw_products.csv');
if (!csvFile) {
  console.error('raw_products.csv not found!');
  process.exit(1);
}

const csvPath = path.join(__dirname, csvFile);
const content = fs.readFileSync(csvPath, 'utf8');
const lines = content.split(/\r?\n/).filter(l => l.trim());

console.log('Total CSV lines:', lines.length);
console.log('Header:', lines[0]);

function parseCSVLine(line) {
  const result = [];
  let current = '';
  let inQuotes = false;
  for (let i = 0; i < line.length; i++) {
    const char = line[i];
    if (char === '"') {
      if (inQuotes && line[i + 1] === '"') {
        current += '"';
        i++;
      } else {
        inQuotes = !inQuotes;
      }
    } else if (char === ',' && !inQuotes) {
      result.push(current.trim());
      current = '';
    } else {
      current += char;
    }
  }
  result.push(current.trim());
  return result;
}

const header = parseCSVLine(lines[0]);
console.log('Parsed Header:', header);

const productsMap = new Map();
for (let i = 1; i < lines.length; i++) {
  const cols = parseCSVLine(lines[i]);
  const product_id = cols[0];
  const language_id = cols[1];
  const name = cols[2];
  
  if (!product_id) continue;

  if (!productsMap.has(product_id)) {
    productsMap.set(product_id, { product_id, en_name: '', ar_name: '', row_indices: [] });
  }
  const item = productsMap.get(product_id);
  item.row_indices.push(i);
  if (language_id === '1') item.en_name = name;
  else if (language_id === '2') item.ar_name = name;
}

console.log('Total Unique Product IDs:', productsMap.size);

const genDir = path.join(__dirname, 'temp/generated_products');
let existingFiles = [];
if (fs.existsSync(genDir)) {
  existingFiles = fs.readdirSync(genDir).filter(f => f.endsWith('.json')).map(f => f.replace('.json', ''));
}
console.log('Existing JSON files count in temp/generated_products:', existingFiles.length);

const progressPath = path.join(__dirname, 'progress.json');
let progressData = {};
if (fs.existsSync(progressPath)) {
  progressData = JSON.parse(fs.readFileSync(progressPath, 'utf8'));
}
console.log('Progress data:', progressData);

const allProductIds = Array.from(productsMap.keys());
const existingSet = new Set(existingFiles);

const unprocessed = allProductIds.filter(id => !existingSet.has(id));
console.log('Unprocessed count (not in temp/generated_products):', unprocessed.length);
console.log('Next 20 unprocessed product IDs:', unprocessed.slice(0, 20));

const next20 = unprocessed.slice(0, 20).map(id => productsMap.get(id));
console.log('\n--- NEXT 20 PRODUCTS TO PROCESS ---');
next20.forEach((p, idx) => {
  console.log(`${idx + 1}. ID: ${p.product_id} | EN: "${p.en_name}" | AR: "${p.ar_name}"`);
});

// Write next 20 products to a JSON file for easy reading
fs.writeFileSync(path.join(__dirname, 'next_20_products.json'), JSON.stringify(next20, null, 2));
