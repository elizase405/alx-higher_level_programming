#!/usr/bin/node
// a script that reads and prints the content of a file.
// ./0-readme.js cisfun

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, { encoding: 'utf-8' }, (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
