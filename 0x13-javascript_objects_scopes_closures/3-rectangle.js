#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return new Rectangle();
    }
    this.width = w;
    this.height = h;
  }
  print(){
    for (let i = 0; i < this.height; i++){
      for (let j = 0; j < this.width; j++){
        document.write('X');
      }
      console.log('');
    }
  }
}
module.exports = Rectangle;
