
// local storage can be used to store some data in the browser in the server side.
function saveInLocalStorage(event) {
	var name = document.getElementById('name').value;
	var ph = document.getElementById('ph').value;
	var email = document.getElementById('email').value;
	var gender = document.getElementById('gender').value;
	var country = document.getElementById('country').value;

	localStorage.setItem('name', name);
	localStorage.setItem('mobile_number', ph);
	localStorage.setItem('email', email);
	localStorage.setItem('gender', gender);
	localStorage.setItem('country', country);
}
