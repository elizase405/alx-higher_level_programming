#!/usr/bin/node
//  a script that prints the title of a Star Wars movie where the episode number matches a given integer.
//  ./3-starwars_title.js 1

const req = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req(url, (err, res, data) => {
  if (err) console.log(err);

  data = JSON.parse(data);
  console.log(data.title);
});
