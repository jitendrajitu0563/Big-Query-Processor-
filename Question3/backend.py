from py2neo import Graph
from py2neo import Node
from py2neo import Relationship
from py2neo import Subgraph
from py2neo import walk
from py2neo.matching import RelationshipMatcher
from py2neo.ogm import GraphObject, Property
# ... (previous code)

@app.route('/influencing_authors', methods=['POST'])
def influencing_authors():
    keyword = request.json.get('keyword')

    # Define a function to calculate PageRank for authors working on the specified keyword
    def calculate_pagerank(graph, keyword):
        query = f"""
        MATCH (a:Author)-[:AUTHORED]->(p:Publication)
        WHERE toLower(p.keywords) CONTAINS toLower('{keyword}')
        RETURN a
        """
        authors = graph.run(query).data()
        
        # Create a subgraph with authors and their publications related to the keyword
        subgraph = Subgraph(authors)

        # Calculate PageRank for authors within the subgraph
        pagerank_scores = graph.page_rank(subgraph)
        
        return pagerank_scores

    pagerank_scores = calculate_pagerank(graph, keyword)

    # Sort authors by PageRank score in descending order
    sorted_authors = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)

    # Return the sorted list of influential authors
    results = [{'Author': author, 'Page Rank': pagerank} for author, pagerank in sorted_authors]

    return jsonify(results)

# ... (remaining code)
