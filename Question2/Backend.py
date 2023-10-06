# ... (previous code)

@app.route('/researcher_profiling', methods=['POST'])
def researcher_profiling():
    researcher_name = request.json.get('researcher_name')

    # Write a Cypher query to profile the researcher and find related topics and other researchers
    query = """
    MATCH (a:Author {name: $researcher_name})-[:AUTHORED]->(p:Publication)
    WITH a, p.keywords AS keywords
    UNWIND keywords AS keyword
    MATCH (a2:Author)-[:AUTHORED]->(p2:Publication)
    WHERE a <> a2 AND toLower(p2.keywords) CONTAINS toLower(keyword)
    WITH a, keyword, COUNT(DISTINCT a2) AS similarity_count
    RETURN keyword, similarity_count, COLLECT({name: a2.name, similarity: similarity_count}) AS similar_researchers
    ORDER BY similarity_count DESC
    """

    results = graph.run(query, researcher_name=researcher_name).data()

    return jsonify(results)

# ... (remaining code)
