#!/usr/bin/node
const fs = require('fs');

function writeFile (file, text) {
  fs.writeFile(file, text, (err, result) => {
    if (err) console.log(err);
  });
}

writeFile(process.argv[2], process.argv[3]);
