// Fetch the character data from the provided URL
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json()) // Parse the JSON from the response
  .then(data => {
    // Update the text content of the element with the ID 'character'
    document.querySelector('#character').textContent = data.name;
  })
  .catch(error => console.error('Error:', error)); // Handle any errors
