#!/usr/bin/node
const req = require('request');
let count = 0;

req(process.argv[2], (err, res) => {
  if (err) console.log(err);
  const arr = JSON.parse(res.body).results;
  arr.forEach(item => {
    item.characters.forEach(itemofitem => {
      if (itemofitem.includes('api/people/18/')) {
        count = count + 1;
      }
    });
  });
  console.log(count);
});
