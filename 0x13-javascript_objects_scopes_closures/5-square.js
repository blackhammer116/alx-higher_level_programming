#!/usr/bin/node

import { Rectangle } from '4-rectangle.js';
class square extends Rectangle {
  constructor(size) {
    super(size,size);
  }
}
module.exports = square()
