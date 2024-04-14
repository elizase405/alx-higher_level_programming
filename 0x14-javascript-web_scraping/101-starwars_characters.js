#!/usr/bin/node
// prints all characters of a Star Wars movie.
// displays each character's name in the same order as the list “characters” in the /films/ response
// ./100-starwars_characters.js 3

const req = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

req(url, (err, res, data) => {
  if (err) console.log(err);

  const characters = JSON.parse(data).characters;

  const charactersPromises = characters.map(link =>
    new Promise((resolve, reject) => {
      req(link, (err, res, data) => {
        if (err) reject(err);

        data = JSON.parse(data);
        resolve(data.name);
      });
    })
  );

  Promise.all(charactersPromises)
    .then(name => console.log(name.join('\n')))
    .catch(err => console.log(err));
});
