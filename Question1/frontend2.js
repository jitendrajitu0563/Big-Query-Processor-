function discoverAuthors() {
    const keyword = document.getElementById('keywordInput').value;
    
    // Send a POST request to the backend API for keyword discovery
    fetch('/keyword_discovery', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ keyword: keyword }),
    })
    .then(response => response.json())
    .then(data => {
        // Display keyword discovery results on the page
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';

        for (const result of data) {
            resultsDiv.innerHTML += `<p>${result['a.name']} - Relevance: ${result['relevance']}, Score: ${result['score']}</p>`;
        }
    });
}
