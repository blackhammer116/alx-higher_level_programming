#!/usr/bin/node

function recur(a) {
  if (!a) {
    return 1;
  } else {
    return a * recur(a - 1);
  }
}

const process = require('process');
const args = process.argv;

console.log(recur(parseInt(args[2])));
