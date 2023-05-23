#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const todo = JSON.parse(body);

    const completedTask = {};

    todo.forEach((todo) => {
      if (todo.completed) {
        if (completedTask[todo.userId]) {
          completedTask[todo.userId]++;
        } else {
          completedTask[todo.userId] = 1;
        }
      }
    });
    console.log(completedTask);
  }
});
