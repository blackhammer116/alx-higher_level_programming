#!/usr/bin/node

function add(a, b) {
  console.log(a + b);
}

const process = require('process');
const args = process.argv;

add(parseInt(args[2]), parseInt(args[3]));
