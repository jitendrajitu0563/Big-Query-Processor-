from flask import Flask, request, jsonify
from py2neo import Graph

app = Flask(__name__)

# Initialize a connection to your Neo4j database
graph = Graph("bolt://localhost:7687", auth=("neo4j", "your_password"))

@app.route('/search', methods=['POST'])
def search():
    keyword = request.json.get('keyword')

    # Write Cypher query to retrieve relevant data based on the keyword
    query = """
    MATCH (p:Publication)-[:AUTHORED_BY]->(a:Author)
    WHERE toLower(p.title) CONTAINS toLower($keyword)
    RETURN a.name, p.title
    """

    results = graph.run(query, keyword=keyword).data()

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
