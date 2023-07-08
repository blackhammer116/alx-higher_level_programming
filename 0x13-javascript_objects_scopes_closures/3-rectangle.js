#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {}
    }
    this.width = w;
    this.height = h;
  }
  print(){
    for (let i = 0; i < height; i++){
      for (let j = 0; j < width; j++){
        console.log('X');
      }
    }
  }
}
module.exports = Rectangle;
