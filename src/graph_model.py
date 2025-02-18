import networkx as nx

G = nx.Graph()
G.add_edge("User_1", "Movie_101", weight=5)

pagerank = nx.pagerank(G)
