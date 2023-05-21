import numpy as np
import pandas as pd
import torch

def get_connection_table(dfCorr, target: str):
    dfConn = dfCorr.explode(target)
    return dfConn

def node_indices(dfConn, source: str, target: str):
    # Construct node indices
    all_source_ids = dfConn[source].unique().tolist()
    all_target_ids = dfConn[target].unique().tolist()

    source_to_idx = dict(zip(all_source_ids, range(len(all_source_ids))))
    target_to_idx = dict(zip(all_target_ids, range(len(all_target_ids))))
    idx_to_source = {v: k for k, v in source_to_idx.items()}
    idx_to_target = {v: k for k, v in target_to_idx.items()}

    return source_to_idx, target_to_idx, idx_to_source, idx_to_target

def map_to_idx(dfConn: pd.core.frame.DataFrame, source: str, target: str, type='homo', inplace=False, dropna=True):
    assert type == 'hetero' or type == 'homo', "Invalid type parameter: only 'homo' or 'hetero'"

    if dropna:
      dfConn = dfConn.dropna(axis=0, how='any', subset=[source, target], inplace=False)

    if type == 'hetero':
        source_to_idx, target_to_idx, _, _ = node_indices(dfConn, source, target)
    elif type == 'homo':
        combined_nodes = list(set(dfConn[source].unique()).union(set(dfConn[target].unique())))
        combined_to_idx = {node: idx for idx, node in enumerate(combined_nodes)}
        source_to_idx = combined_to_idx
        target_to_idx = combined_to_idx

    if inplace:
        dfConn[source] = dfConn[source].map(source_to_idx)
        dfConn[target] = dfConn[target].map(target_to_idx)
        return dfConn[[source, target]]
    else:
        dfConn_copy = dfConn.copy()
        dfConn_copy[source] = dfConn_copy[source].map(source_to_idx)
        dfConn_copy[target] = dfConn_copy[target].map(target_to_idx)
        return dfConn_copy

def get_mutual_table(dfConn, on: str, by: str, self_loop=True):
    '''
    Construct homogenous graph (sigle node type) with undirected edge
    Parameters:
        on: str -> column that will apply mutual information
        by: str -> column that will use for retrieve mutual information
        self_loop: boolean -> True: apply self-loop
    Example:
        on='content_id', by='topic_id'
        this will generate mutual connection betweeen each content_id based on mutual topic_id
    '''
    contentGraph = dfConn[[by, on]].merge(dfConn[[by, on]], on=by)
    if not self_loop:
        contentGraph = contentGraph.loc[contentGraph[on + '_x'] != contentGraph[on + '_y']]
    return contentGraph

def edge_index(dfConn, source: str, target: str, output_type='numpy'):
    '''
    Construct `edge_index`
    self-loop and directed edge are depend on input graph dataframe (dfConn)
    undirected edge (node1)<--[UNDIRECTED]-->(node2)
    directed edge (node1)--[DIRECTED]-->(node2)
    '''
    edge_index = np.transpose(dfConn[[source, target]].to_numpy())
    
    if output_type == 'torch':
        edge_index = torch.tensor(edge_index, dtype=torch.long)
    
    return edge_index
