#!/usr/bin/node

const arr = process.argv.slice(2);

if (arr.length <= 1) {
  console.log(0);
} else {
  const max = Math.max(...arr);
  const secondMax = Math.max(...arr.filter(x => x < max));
  console.log(secondMax);
}
