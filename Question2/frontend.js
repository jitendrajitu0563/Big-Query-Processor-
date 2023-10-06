function profileResearcher() {
    const researcherName = document.getElementById('researcherInput').value;
    
    // Send a POST request to the backend API for researcher profiling
    fetch('/researcher_profiling', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ researcher_name: researcherName }),
    })
    .then(response => response.json())
    .then(data => {
        // Display researcher profiling results on the page
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';

        for (const result of data) {
            const topic = result['keyword'];
            const relevance = result['similarity_count'];
            const similarResearchers = result['similar_researchers'];
            const similarResearchersString = similarResearchers.map(r => `${r.name} (${r.similarity})`).join(', ');

            resultsDiv.innerHTML += `<p>Topic: ${topic}<br>Author Relevance: ${relevance}<br>Other researchers: ${similarResearchersString}</p>`;
        }
    });
}
