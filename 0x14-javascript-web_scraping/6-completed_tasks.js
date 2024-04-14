#!/usr/bin/node
// computes the number of tasks completed by user id.
// ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos

const req = require('request');
const url = process.argv[2];

req(url, (err, res, data) => {
  if (err) console.log(err);

  const numberOfTasks = {};
  data = JSON.parse(data);
  const completed = data.filter(obj => obj.completed === true);

  for (let i = 0; i < completed.length; i++) {
    if (numberOfTasks[completed[i].userId]) {
      numberOfTasks[completed[i].userId]++;
    } else {
      numberOfTasks[completed[i].userId] = 1;
    }
  }
  console.log(numberOfTasks);
});
