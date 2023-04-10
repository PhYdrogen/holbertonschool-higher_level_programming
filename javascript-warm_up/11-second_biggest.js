#!/usr/bin/node
const argv = process.argv;
const numbersList = argv.slice(2);
let big = 0;
let second = 0;
for (let i = 0; i < numbersList.length; i++) {
  if (i === 0) {
    big = numbersList[i];
  } else if (numbersList[i] > big) {
    second = big;
    big = numbersList[i];
  }
}
console.log(second);
