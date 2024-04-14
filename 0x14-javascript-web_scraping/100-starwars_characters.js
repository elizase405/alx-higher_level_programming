#!/usr/bin/node
// prints all characters of a Star Wars movie
// ./100-starwars_characters.js 3

const req = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

req(url, (err, res, data) => {
  if (err) console.log(err);

  data = JSON.parse(data);
  data.characters.forEach(link =>
    req(link, (err, res, data) => {
      if (err) console.log(err);

      data = JSON.parse(data);
      console.log(data.name);
    })
  );
});
