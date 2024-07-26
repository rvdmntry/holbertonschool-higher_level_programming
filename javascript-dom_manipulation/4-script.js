// Add a click event listener to the element with the ID 'add_item'
document.querySelector('#add_item').addEventListener('click', function() {
  // Create a new li element
  const newItem = document.createElement('li');
  // Set the text content of the new li element
  newItem.textContent = 'Item';
  // Append the new li element to the ul element with the class 'my_list'
  document.querySelector('ul.my_list').appendChild(newItem);
});
