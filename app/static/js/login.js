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
    if (response.status !== 200) {
      showError("Invalid Username or Password!")
      throw new Error("Invalid Username or Password!");
    }
    return response.json();
  })
  .then(data => {
    window.location = "/";
  })
  .catch(error => {
    showError("Invalid Username or Password!")
    throw new Error("Invalid Username or Password!");
  });
})