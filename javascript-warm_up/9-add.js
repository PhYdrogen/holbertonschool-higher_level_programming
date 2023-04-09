#!/usr/bin/node
function add (a, b) {
  a = Number(a);
  b = Number(b);
  return (a + b);
}

const first = process.argv[2];
const second = process.argv[3];
console.log(add(first, second));
