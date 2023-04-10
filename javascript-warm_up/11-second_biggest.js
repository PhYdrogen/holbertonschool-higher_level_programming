#!/usr/bin/node
const argv = process.argv;
const numbersList = argv.slice(2);
numbersList.sort(function(a, b){return a - b})
console.log(numbersList[numbersList.length - 2]);
