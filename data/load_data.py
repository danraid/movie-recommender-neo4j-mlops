from py2neo import Graph

graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

query = """
CREATE (:User {id: 1, name: "Alice"})
CREATE (:User {id: 2, name: "Bob"})
CREATE (:Movie {id: 101, title: "Inception", genre: "Sci-Fi"})
"""
graph.run(query)
