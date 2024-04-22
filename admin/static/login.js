/*
document.addEventListener('DOMContentLoaded', function() {
    // Get the switch element
    var switchElement = document.getElementById('shutdownSwitch');
    
    // Add an event listener to detect when the switch state changes
    switchElement.addEventListener('change', function(event) {
        // Get the new state of the switch (checked or unchecked)
        var newState = event.target.checked ? 1 : 0;
        
        // Make an AJAX request to the Flask backend to update the switch state
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/settings', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    // Request was successful, handle response if needed
                    console.log(xhr.responseText);
                } else {
                    // Request failed, handle error if needed
                    console.error('Error:', xhr.statusText);
                }
            }
        };
        xhr.send(JSON.stringify({ state: newState }));
    });
  });
*/