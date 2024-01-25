document.getElementById('logout-form').addEventListener('submit', (e) => {
  e.preventDefault();


  fetch('/logout', {
    method: 'POST',
    credentials: 'include'
  })
  .then(response => {
    return response.json();
  })
  .then(data => {
    window.location = "/login";
  })
  .catch(error => {
    console.error('There has been a problem with your fetch operation:', error);
    window.location = "/login";
  });
})