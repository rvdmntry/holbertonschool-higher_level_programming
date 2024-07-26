// Add a click event listener to the element with the ID 'toggle_header'
document.querySelector('#toggle_header').addEventListener('click', function() {
  // Select the header element
  const header = document.querySelector('header');
  
  // Check the current class of the header and toggle between 'red' and 'green'
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else {
    header.classList.remove('green');
    header.classList.add('red');
  }
});
