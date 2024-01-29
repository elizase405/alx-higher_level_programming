#!/usr/bin/node

const Square_5 = require("./5-square");

class Square extends Square_5 {
  charPrint(c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let str = "";
        for (let j = 0; j < this.width; j++) {
          str += c;
	}
        console.log(str);
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
