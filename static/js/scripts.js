document.getElementById('scraper-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const urls = document.getElementById('urls').value.split(',');
    const searchTerm = document.getElementById('search_term').value;

    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ urls, search_term: searchTerm })
    })
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';

        if (data.error) {
            resultsDiv.innerHTML = `<p style="color: red;">${data.error}</p>`;
        } else {
            data.forEach(result => {
                const p = document.createElement('p');
                p.textContent = result;
                resultsDiv.appendChild(p);
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
