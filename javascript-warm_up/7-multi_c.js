#!/usr/bin/node
const userNb = Number(process.argv[2]);
if (isNaN(userNb)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < userNb; i++) {
    console.log('C is fun');
  }
}
