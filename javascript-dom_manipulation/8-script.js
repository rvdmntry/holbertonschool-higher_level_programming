document.addEventListener('DOMContentLoaded', function() {
  // Fetch the hello translation from the provided URL
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json()) // Parse the JSON from the response
    .then(data => {
      // Update the text content of the element with the ID 'hello'
      document.querySelector('#hello').textContent = data.hello;
    })
    .catch(error => console.error('Error:', error)); // Handle any errors
});
