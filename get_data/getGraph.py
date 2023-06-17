import networkx as nx
import matplotlib.pyplot as plt


def make_graph_with_aerial_distance(getData) :
    # Create an empty graph
    G = nx.Graph()
    
    graph_edges_with_distance = getData.get_graph_edges_values_aerial_distance()
    for i in range(len(graph_edges_with_distance)):
        G.add_edge(graph_edges_with_distance[i][0], graph_edges_with_distance[i][1],distance="{:.2f}".format(graph_edges_with_distance[i][2]))

    # Draw the graph
    pos = nx.spring_layout(G)  # Position nodes using spring layout algorithm
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12, edge_color='gray')
    
    # Add edge labels
    edge_labels = nx.get_edge_attributes(G, 'distance')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8)


    # Display the graph
    plt.show()

def make_graph_with_road_distance(getData) :
    # Create an empty graph
    G = nx.Graph()
    
    graph_edges_with_distance = getData.get_graph_edges_values_road_distance()
    for i in range(len(graph_edges_with_distance)):
        G.add_edge(graph_edges_with_distance[i][0], graph_edges_with_distance[i][1],distance="{:.2f}".format(graph_edges_with_distance[i][2]))

    # Draw the graph
    pos = nx.spring_layout(G)  # Position nodes using spring layout algorithm
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12, edge_color='gray')
    
    # Add edge labels
    edge_labels = nx.get_edge_attributes(G, 'distance')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8)


    # Display the graph
    plt.show()


def get_edges_with_values(getData):
    # Create an empty graph
    G = nx.Graph()

    graph_edges_with_distance = getData.get_graph_edges_values_aerial_distance()
    for i in range(len(graph_edges_with_distance)):
        G.add_edge(graph_edges_with_distance[i][0], graph_edges_with_distance[i][1],distance="{:.2f}".format(graph_edges_with_distance[i][2]))
        
    
    return G.edges(data=True)