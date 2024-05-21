#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const completedTasksByUser = {};
    tasks.forEach(task => {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });
    console.log(completedTasksByUser);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
