document.getElementById('register-form').addEventListener('submit', (e) => {
  e.preventDefault();

  const username = document.getElementById('username').value;
  const email = document.getElementById('email').value;
  const full_name = document.getElementById('full-name').value;
  const password = document.getElementById('password').value;
  const confirm_password = document.getElementById('confirm-password').value;

	if (password !== confirm_password) {
		showError("Password and Confirm Password are different!");
		throw new Error("Password and Confirm Password are different!");
	}

  fetch('/register', {
    method: 'POST',
		headers: {
      'Content-Type': 'application/json',
      'accept': 'application/json'
    },
		body: JSON.stringify({
			username: username,
			email: email,
			full_name: full_name,
			password: password
		})
  })
  .then(response => {
    return response.json();
  })
  .then(data => {
		if (data.detail) {
			showError(data.detail)
		} else {
    	window.location = "/login";
		}
  })
  .catch(error => {
    console.log(error)
    throw new Error(error);
  });
})