import networkx as nx
import matplotlib.pyplot as plt


def make_graph(getData) :
    # Create an empty graph
    G = nx.Graph()

    # Add cities as nodes
    cities = getData.get_cities_names()
    # print(cities)
    G.add_nodes_from(cities)

    # Add connections between cities as edges
    connections = getData.connet_cities()
    G.add_edges_from(connections)

    # Draw the graph
    pos = nx.spring_layout(G)  # Position nodes using spring layout algorithm
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12, edge_color='gray')

    # Display the graph
    plt.show()
