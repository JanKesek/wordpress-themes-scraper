const fs = require('fs');

let rawdata = fs.readFileSync('rezultat.json');
let rawdata2 = fs.readFileSync('rezultat2.json');
let student = JSON.parse(rawdata);
let student2 = JSON.parse(rawdata2);
console.log(Object.keys(student).length)
console.log(Object.keys(student2).length)
