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
    });
});

// Function to clear the form fields
function clearForm() {
    document.getElementById("registrationForm").reset();
}

// Function to close the Bootstrap modal
function closeModal() {
    var modal = new bootstrap.Modal(document.getElementById('Registermodal'));
    modal.hide();
}
