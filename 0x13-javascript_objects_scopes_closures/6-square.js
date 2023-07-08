#!/usr/bin/node

const square = require('./5-square.js');
class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < super.size; i++) {
        let row = '';
        for (let j = 0; j < super.size; j++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
}
module.exports = Square;
