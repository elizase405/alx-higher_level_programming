#!/usr/bin/node
// a script that writes a string to a file.
// ./1-writeme.js my_file.txt "Python is cool"


const fs = require('fs');
const filePath = process.argv[2];
const data = process.argv[3];

fs.writeFile(filePath, data, (err) => {
  if (err) {
    console.log(err);
  }
});
