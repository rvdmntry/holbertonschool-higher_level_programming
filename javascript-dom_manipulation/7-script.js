// Fetch the movie data from the provided URL
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json()) // Parse the JSON from the response
  .then(data => {
    // Get the ul element with the ID 'list_movies'
    const list = document.querySelector('#list_movies');
    
    // Iterate over the list of movies and create an li element for each title
    data.results.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      list.appendChild(listItem);
    });
  })
  .catch(error => console.error('Error:', error)); // Handle any errors
