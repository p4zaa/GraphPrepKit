import networkx as nx
import matplotlib.pyplot as plt

def nx_edges(dfConn, source: str, target: str, dropna=True):
    if dropna:
        dfConn = dfConn[[source, target]].dropna(axis=0, how='any', subset='retweeter_ids')
    edges = dfConn.values.tolist()
    return edges

def draw_graph(G, with_labels=False, node_color='lightblue', node_size=10, font_size=12, edge_color='gray'):
    nx.draw(G, with_labels=with_labels, node_color=node_color, node_size=node_size, font_size=font_size, edge_color=edge_color)
    plt.show()
