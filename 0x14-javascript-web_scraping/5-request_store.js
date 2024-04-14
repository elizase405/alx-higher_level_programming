#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.
// ./5-request_store.js http://loripsum.net/api loripsum

const fs = require('fs');
const req = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

req(url, 'utf-8', (err, res, data) => {
  if (err) console.log(err);

  fs.writeFile(filePath, data, err => {
    if (err) console.log(err);
  });
});
