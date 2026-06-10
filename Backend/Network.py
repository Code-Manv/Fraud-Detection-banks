import networkx as nx

def build_relationship_network(df):
    relationship_graph = nx.Graph()

    source_nodes = df["name"].values
    target_nodes = df["location"].values

    edges = [(source_nodes[i], target_nodes[i]) for i in range(len(df))]

    relationship_graph.add_edges_from(edges)

    return relationship_graph