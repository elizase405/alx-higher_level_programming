#!/usr/bin/node

function addMeMaybe (x, func) {
  x++;
  func(x);
}

exports.addMeMaybe = addMeMaybe;
