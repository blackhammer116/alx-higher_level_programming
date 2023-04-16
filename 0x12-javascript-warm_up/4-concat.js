#!/usr/bin/node

const process = require('process');
const args1 = [process.argv[2], process.argv[3]];

if (!args1[0] && !args1[1]) {
  args1[0] = 'undefined';
  args1[1] = 'undefined';
} else if (!args1[1] && args1[0]) {
  args1[1] = 'undefined';
} else if (!args1[0] && args1[1]) {
  args1[0] = 'undefined';
}
console.log(args1.join(' is '));
