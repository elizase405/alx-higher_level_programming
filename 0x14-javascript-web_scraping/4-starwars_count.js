#!/usr/bin/node
//  a script that prints the title of a Star Wars movie where the episode number matches a given integer.
//  ./3-starwars_title.js 1

const request = require('request');
const url = process.argv[2];
const actor = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (err, res, data) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(data).results;
    const match = films.filter((film) => film.characters.includes(actor));
    console.log(`${match.length}`);
  }
});
