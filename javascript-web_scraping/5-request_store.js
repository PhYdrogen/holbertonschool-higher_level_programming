#!/usr/bin/node
const req = require('request');
const fs = require('fs');

req(process.argv[2], (err, res) => {
  if (err) console.log(err);
  const data = res.body;
  fs.writeFile(process.argv[3], data, 'utf8', (err, result) => {
    if (err) console.log(err);
  });
});
