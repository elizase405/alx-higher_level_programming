#!/usr/bin/node
// a script that display the status code of a GET request.
// ./2-statuscode.js https://alx-intranet.hbtn.io/status

const req = require('request');
const url = process.argv[2];

req(url, (err, res, data) => {
  if (err) console.log(err);
  console.log(`code: ${res.statusCode}`);
});
