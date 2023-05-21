import matplotlib.pyplot as plt
import networkx as nx
import community
from pyvis.network import Network

def get_community_graph(G: nx.classes.graph.Graph, interactive=False, notebook=True, cdn_resources='in_line'):
    # Apply the Louvain algorithm for community detection
    partition = community.community_louvain.best_partition(G)

    # Create a new graph with the communities as node attributes
    community_graph = nx.Graph()
    for node, community_id in partition.items():
        community_graph.add_node(node, community=community_id)

    # Add the edges to the community graph
    for edge in G.edges():
        u, v = edge
        community_u = partition[u]
        community_v = partition[v]
        if community_u == community_v:
            community_graph.add_edge(u, v)
            
    if interactive:
        # Assign different colors to nodes based on their communities
        node_colors = [partition[node] for node in community_graph.nodes()]

        # Create a mapping from node ID to index in node_colors list
        node_id_to_index = {node: index for index, node in enumerate(community_graph.nodes())}

        # Create a Network object for interactive visualization
        nt = Network(notebook=notebook, cdn_resources=cdn_resources)

        # Add nodes and edges to the Network object
        for node in community_graph.nodes():
            color = node_colors[node_id_to_index[node]]
            nt.add_node(node, color=color)

        for edge in community_graph.edges():
            u, v = edge
            nt.add_edge(u, v)

        # Display the interactive graph
        nt.show("community_graph.html")
        
    else:
        # Define the layout for community visualization
        layout = nx.spring_layout(community_graph)

        # Assign different colors to nodes based on their communities
        colors = [partition[node] for node in community_graph.nodes()]

        # Draw the community graph
        nx.draw_networkx(community_graph, pos=layout, node_color=colors, with_labels=False, node_size=10)

        # Show the plot
        plt.show()
        
def print_community(G: nx.classes.graph.Graph):
    # Apply the Louvain algorithm for community detection
    partition = community.community_louvain.best_partition(G)
    
    # Retrieve the communities
    communities = {}
    for node, community_id in partition.items():
        if community_id not in communities:
            communities[community_id] = []
        communities[community_id].append(node)
        
     # Print the communities
    for community_id, nodes in communities.items():
        print(f"Community {community_id}: {nodes}")
