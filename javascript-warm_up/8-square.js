#!/usr/bin/node
const userNb = Number(process.argv[2]);
if (isNaN(userNb)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < userNb; i++) {
    for (let j = 0; j < userNb; j++) {     
      process.stdout.write('X');
    }
  console.log();
  }
}
