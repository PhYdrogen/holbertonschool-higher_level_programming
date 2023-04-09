#!/usr/bin/node
import { exit } from 'node:process';

let count = 0;
process.argv.forEach(element => {
  if (count === 2) {
    console.log(element);
    exit(0);
  }
  count += 1;
});
console.log('No argument');
