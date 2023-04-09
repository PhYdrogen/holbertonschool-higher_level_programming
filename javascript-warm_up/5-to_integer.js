#!/usr/bin/node
let userNum = process.argv[2];
userNum = Number(userNum);
if (isNaN(userNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + userNum);
}
