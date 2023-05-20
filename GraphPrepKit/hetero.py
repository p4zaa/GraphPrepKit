def edge_index(dfConn, source: str, source: str):
    # Construct `edge_index` of non-self-loop and directed graph
    edge_index = torch.tensor(np.transpose(dfConn[[source, source]].to_numpy()),dtype=torch.long)
    return edge_index
