#!/usr/bin/node
const fs = require('fs');
const url = process.argv[2];

fs.readFile(url, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
