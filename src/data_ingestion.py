from py2neo import Graph
import pandas as pd

graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

query = "MATCH (u:User)-[r:RATED]->(m:Movie) RETURN u.id, m.id, r.score"
data = graph.run(query).to_data_frame()
