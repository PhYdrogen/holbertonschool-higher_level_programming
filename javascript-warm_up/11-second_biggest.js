#!/usr/bin/node
const argv = process.argv;
const numbers_list = [1, 10, 11, 3, 4, 5];
let big = 0;
let second = 0;
for (let i = 0; i < numbers_list.length; i++) {
    if (i == 0) {
        big = numbers_list[i];        
    } else if (numbers_list[i] > big) {
        second = big;
        big = numbers_list[i];
    }
}
console.log(second);