#!/usr/bin/node
const argv = process.argv;
let numbers_list = argv.slice(2);
numbers_list = numbers_list.sort();
console.log(numbers_list[numbers_list.length - 2]);
//console.log(numbers_list);