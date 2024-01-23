#!/usr/bin/node

const arr = process.argv;
const maxArr = []; // stores all the biggest integer found and replaced
let ind = -1; // stores the index of the biggest integer
let maxVal = 0; // stores the biggest integer

// we start i at 2 because that is where command line input start
for (let i = 2; i < arr.length; i++) {
  if (arr[i] > maxVal) {
    ind++;
    maxVal = arr[i];
    maxArr.push(arr[i]);
  }
}

if (maxArr.length === 0 || maxArr.length === 1) {
  console.log(0);
} else {
  console.log(maxArr[ind - 1]); // we want the second biggest integer
}
