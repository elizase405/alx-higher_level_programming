#!/usr/bin/node

const num = parseInt(process.argv[2]);

function factorial (num) {
  if (num === 1) {
    return num;
  }
  return num * factorial(num - 1);
}

if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
