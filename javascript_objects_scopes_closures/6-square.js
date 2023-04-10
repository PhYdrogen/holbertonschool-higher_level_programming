#!/usr/bin/node
const S1 = require('./5-square');

class Square extends S1 {
  charPrint (c) {
    let char = '';
    if (c === undefined) {
      char = 'X';
    } else {
      char = c;
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(char);
      }
      console.log();
    }
  }
}

module.exports = Square;
