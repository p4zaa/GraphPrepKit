def node_indice(dfConn, source: str, target: str):
    # Construct nodes indices
    all_source_ids = dfConn[source].unique().tolist()
    all_target_ids = dfConn[target].unique().tolist()

    source_to_idx = dict(zip(all_source_ids, range(len(all_source_ids))))
    target_to_idx = dict(zip(all_target_ids, range(len(all_target_ids))))

    idx_to_source = {v: k for k, v in source_to_idx.items()}
    idx_to_target = {v: k for k, v in target_to_idx.items()}
    return source_to_idx, target_to_idx, idx_to_source, idx_to_target

def source_to_idx(dfConn, source: str):
    all_source_ids = dfConn[source].unique().tolist()
    source_to_idx = dict(zip(all_source_ids, range(len(all_source_ids))))
    return source_to_idx

def target_to_idx(dfConn, target: str):
    all_target_ids = dfConn[target].unique().tolist()
    target_to_idx = dict(zip(all_target_ids, range(len(all_target_ids))))
    return target_to_idx

def idx_to_source(dfConn, source: str, target: str):
    all_source_ids = dfConn[source].unique().tolist()
    source_to_idx = dict(zip(all_source_ids, range(len(all_source_ids))))
    idx_to_source = {v: k for k, v in topic_to_idx.items()}
    return idx_to_source

def idx_to_target(dfConn, source: str, target: str):
    all_target_ids = dfConn[target].unique().tolist()
    target_to_idx = dict(zip(all_target_ids, range(len(all_target_ids))))
    idx_to_target = {v: k for k, v in target_to_idx.items()}
    
def map_to_idx(dfConn, source: str, target: str, inplace=False):
    source_to_idx = source_to_idx(dfConn, source=source)
    target_to_idx = target_to_idx(dfConn, target=target)
    
    # Map ID to index
    if inplace:
        dfConn[source] = dfConn[source].map(source_to_idx)
        dfConn[target] = dfConn[target].map(target_to_idx)
        return dfConn[[source, target]]
    else:
        dfConn_copy = dfConn.copy()
        dfConn_copy[source] = dfConn_copy[source].map(source_to_idx)
        dfConn_copy[target] = dfConn_copy[target].map(target_to_idx)
        return dfConn_copy
