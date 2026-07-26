const fs = require('fs');
const path = require('path');

const dirsToSearch = [
  'e:\\ai_agents\\prodacts genrator',
  'e:\\ai_agents',
  'C:\\Users\\ahmed\\.gemini\\antigravity'
];

dirsToSearch.forEach(d => {
  if (fs.existsSync(d)) {
    console.log(`--- Checking ${d} ---`);
    const files = fs.readdirSync(d);
    files.forEach(f => {
      if (f.toLowerCase().includes('raw') || f.toLowerCase().includes('product')) {
        console.log(' Matched file/dir:', f);
      }
    });
  }
});
