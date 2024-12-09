# I want to display the graph of the knowledge graph, given a path to a graph.ml file
import networkx as nx
import matplotlib.pyplot as plt

def display_graph(graphml_path):
    # Read the GraphML file
    G = nx.read_graphml(graphml_path)
    
    # Create a new figure with a larger size
    plt.figure(figsize=(12, 8))
    
    # Create layout for the graph
    pos = nx.spring_layout(G)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=500, alpha=0.6)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos)
    
    # Add title
    plt.title("Knowledge Graph Visualization")
    
    # Remove axes
    plt.axis('off')
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python displayGraph.py <path_to_graphml>")
        sys.exit(1)
    
    graphml_path = sys.argv[1]
    display_graph(graphml_path)