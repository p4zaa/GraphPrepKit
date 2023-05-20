import numpy as np

def edge_index_numpy(dfConn, source: str, target: str):
    # Construct `edge_index` of self-loop and undirected graph
    edge_index = np.transpose(dfConn[[source, target]].to_numpy())
    return edge_index

def edge_index_torch(dfConn, source: str, target: str):
    # Construct `edge_index` of non-self-loop and directed graph
    edge_index = torch.tensor(np.transpose(dfConn[[source, target]].to_numpy()),dtype=torch.long)
    return edge_index
