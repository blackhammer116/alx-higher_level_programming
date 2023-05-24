#!/usr/bin/node
const request = require('request');
const url1 = (process.argv[2].slice(0, -5)) + 'people/18';

request(url1, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(`${(JSON.parse(body).films).length}`);
  }
});
