import numpy as np

def edge_index_numpy(dfConn, source: str, target: str):
    # Construct `edge_index` of self-loop and undirected graph
    edge_index = np.transpose(dfConn[[source, target]].to_numpy())
    return edge_index

def edge_index_torch(dfConn, source: str, target: str):
    # Construct `edge_index` of self-loop and undirected graph
    edge_index = torch.tensor(np.transpose(contentGraph[[source, target]].to_numpy()),dtype=torch.long)
    return edge_index

def get_mutual_table(dfConn, on: str, by: str, self_loop=True):
    # Construct homogenous graph (sigle node type) with undirected edge
    contentGraph = dfConn.merge(dfConn, on=by)
    if not self_loop:
        contentGraph = contentGraph.loc[contentGraph[on + '_x'] != contentGraph[on + '_y']]
    return contentGraph
