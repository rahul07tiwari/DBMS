document.addEventListener('DOMContentLoaded', function()  {
    // AJAX registration form submission
    document.getElementById("registrationForm").addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent the default form submission behavior
        
        var formData = new FormData(this); // Get the form data
        
        fetch('/', { // Send a POST request to the root route
            method: 'POST',
            body: formData // Send form data in the request body
        })
        .then(() => {
            clearForm(); // Function to clear the form fields
            closeModal(); // Function to close the modal
        })
        .catch(error => console.error('Error:', error)); // Handle any errors
   // Function to clear the form fields
                function clearForm() {
                    document.getElementById("registrationForm").reset();
                }

                // Function to close the Bootstrap modal
                function closeModal() {
                    var modal = new bootstrap.Modal(document.getElementById('Registermodal'));
                    modal.close();
                }
    });

});

// Assuming you have jQuery included in your project

$(document).ready(function() {
    $('#loginForm').submit(function(event) {
        event.preventDefault(); // Prevent the form from submitting normally
        
        // Get the email and password from the form
        var email = $('#email').val();
        var password = $('#password').val();
        
        // Send the login request to the server
        $.ajax({
            type: 'POST',
            url: '/login',
            data: {
                email: email,
                password: password
            },
            success: function(response) {
                if (response.status === 'success') {
                    // Login successful
                    $('#loginModal').modal('hide'); // Hide the login modal
                    $('#loginButton').hide(); // Hide the login button
                    $('#registerButton').hide(); // Hide the register button
                    $('#profileButton').show(); // Show the profile button
                    // You can also perform any other actions you need here, like updating the UI
                } else {
                    // Login failed
                    alert('Login failed. ' + response.message);
                }
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
                // Handle the error, e.g., show an error message to the user
            }
        });
    });
});

