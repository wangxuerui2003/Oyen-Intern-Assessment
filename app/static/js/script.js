function showError(message) {
	const errorMessage = document.getElementById('error-message');
	errorMessage.textContent = message;
	errorMessage.classList.remove('hidden'); // Show the element
	setTimeout(() => {
			errorMessage.classList.add('hidden'); // Hide the element after a delay
	}, 3000); // Adjust the delay (in milliseconds) as needed
}