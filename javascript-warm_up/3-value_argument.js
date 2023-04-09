#!/usr/bin/node

let count = 0;
let isFound = false;
process.argv.forEach(element => {
  if (count === 2) {
    console.log(element);
    isFound = true;
  }
  count += 1;
});
if (!isFound) {
  console.log('No argument');
}
