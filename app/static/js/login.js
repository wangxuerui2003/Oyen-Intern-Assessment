document.getElementById('login-form').addEventListener('submit', (e) => {
  e.preventDefault();

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  fetch('/token', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: new URLSearchParams({
      'username': username,
      'password': password
    }),
    credentials: 'include'
  })
  .then(response => {
    return response.json();
  })
  .then(data => {
    window.location = "/";
  })
  .catch(error => {
    console.error('There has been a problem with your fetch operation:', error);
    window.location = "/";
  });
})