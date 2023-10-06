function findInfluencingAuthors() {
    const keyword = document.getElementById('influencingInput').value;
    
    // Send a POST request to the backend API for finding influential authors
    fetch('/influencing_authors', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ keyword: keyword }),
    })
    .then(response => response.json())
    .then(data => {
        // Display the list of influential authors on the page
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';

        for (const result of data) {
            resultsDiv.innerHTML += `<p>Author: ${result['Author']} - Page Rank: ${result['Page Rank']}</p>`;
        }
    });
}
