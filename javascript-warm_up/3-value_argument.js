#!/usr/bin/node
const { argv, exit } = require('node:process');

let count = 0;
argv.forEach(element => {
    if (count === 2) {
        console.log(element);
        exit(0);
    }
    count += 1;
});
console.log('No argument');