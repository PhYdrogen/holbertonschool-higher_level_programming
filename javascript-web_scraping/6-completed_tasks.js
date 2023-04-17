#!/usr/bin/node
const req = require('request');

req(process.argv[2], (err, result, body) => {
  if (err) console.log(err.message);
  const stats = {};
  const data = JSON.parse(body);
  data.forEach(obj => {
    if (obj.completed === true) {
      if (isNaN(stats[obj.userId])) {
        stats[obj.userId] = 1;
      } else {
        stats[obj.userId] = stats[obj.userId] + 1;
      }
    }
  });
  console.log(stats);
});
