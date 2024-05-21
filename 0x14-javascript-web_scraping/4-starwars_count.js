#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const wedgeAntillesId = '18';
    let count = 0;

    // Loop through each film and check if Wedge Antilles is present
    for (const film of films) {
      for (const character of film.characters) {
        if (character.includes(`/api/people/${wedgeAntillesId}/`)) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  } else {
    console.log(`Error: ${response.statusCode}`);
  }
});
