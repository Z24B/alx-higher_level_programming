#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movie = JSON.parse(body);

    // Print the characters' names in the same order as in the /films/ response
    movie.characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
        } else if (response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        } else {
          console.log(`Error: ${response.statusCode}`);
        }
      });
    });
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
