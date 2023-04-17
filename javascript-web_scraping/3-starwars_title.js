#!/usr/bin/node
const req = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';
req(url + process.argv[2], (err, res, body) => {
  if (err) console.log(err);
  console.log(JSON.parse(body).title);
});
