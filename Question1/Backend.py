# ... (previous code)

@app.route('/keyword_discovery', methods=['POST'])
def keyword_discovery():
    keyword = request.json.get('keyword')

    # Write a Cypher query to find authors working on the given keyword and calculate relevance and score
    query = """
    MATCH (a:Author)-[:AUTHORED]->(p:Publication)
    WHERE toLower(p.keywords) CONTAINS toLower($keyword)
    WITH a, COUNT(p) AS publication_count, COLLECT(p.keywords) AS keywords
    UNWIND keywords AS keyword
    WITH a, publication_count, COUNT(keyword) AS keyword_count
    RETURN a.name, (keyword_count * 1.0 / publication_count) AS relevance, (keyword_count * 100.0 / SIZE(keywords)) AS score
    ORDER BY relevance DESC
    """

    results = graph.run(query, keyword=keyword).data()

    return jsonify(results)

# ... (remaining code)
