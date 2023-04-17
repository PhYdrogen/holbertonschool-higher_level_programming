#!/usr/bin/node
const fs = require('fs');

function readFile (file) {
  fs.readFile(file, 'utf8', (err, data) => {
    if (err) console.log(err);
    console.log(data);
  });
}

readFile(process.argv[2]);
