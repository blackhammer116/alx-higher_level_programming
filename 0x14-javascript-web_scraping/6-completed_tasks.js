#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
      const todo = JSON.parse(body);
      
      const completed_task = {};

      todo.forEach((todo) => {
        if (todo.completed){
          if (completed_task[todo.userId]) {
            completed_task[todo.userId]++;
          } else {
              completed_task[todo.userId] = 1;
            }
        }
      });
/*
      Object.keys(completed_task).forEach((userId) => {
        if (!completed_task[userId - 1]) {
          console.log('{');
          console.log(`'${userId}': ${completed_task[userId]},`);
        } else if (completed_task[userId + 1]) {
          console.log(`'${userId}': ${completed_task[userId]},`);
        } else if (!completed_task[userId + 1]){
          console.log(`'${userId}': ${completed_task[userId]} \}`);
        }
        });*/
    console.log(completed_task);
  }
});
