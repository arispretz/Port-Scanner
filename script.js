window.onload = function() {
    fetch('/results')
        .then(response => response.text())
        .then(data => {
            document.getElementById('results').innerText = data;
        })
        .catch(error => {
            document.getElementById('results').innerText = `Error: ${error.message}`;
        });
};
