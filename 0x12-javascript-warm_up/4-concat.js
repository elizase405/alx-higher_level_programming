#!/usr/bin/node

let arg1 = 'undefined';
let arg2 = 'undefined';

if (process.argv.length < 3) {
  console.log(arg1 + ' is ' + arg2);
} else if (process.argv.length === 3) {
  arg1 = process.argv[2];
  console.log(arg1 + ' is ' + arg2);
} else {
  arg1 = process.argv[2];
  arg2 = process.argv[3];
  console.log(arg1 + ' is ' + arg2);
}
