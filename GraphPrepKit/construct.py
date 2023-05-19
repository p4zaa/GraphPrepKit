def node_indice(dfConn, source: str, target: str):
    # Construct nodes indices
    all_topic_ids = dfConn[source].unique().tolist()
    all_content_ids = dfConn[target].unique().tolist()

    topic_to_idx = dict(zip(all_topic_ids, range(len(all_topic_ids))))
    content_to_idx = dict(zip(all_content_ids, range(len(all_content_ids))))

    idx_to_topic = {v: k for k, v in topic_to_idx.items()}
    idx_to_content = {v: k for k, v in content_to_idx.items()}
