# GraphPrepKit
GraphPrepKit is a powerful and versatile graph preprocessing library designed to simplify and streamline the data preparation phase for graph-based applications. It provides a comprehensive set of tools and utilities to efficiently preprocess graphs, allowing users to transform, clean, and manipulate graph data with ease.

# Installation
```python
pip install -q git+'https://github.com/p4zaa/GraphPrepKit.git'
```
```python
from GraphPrepKit import construct, homo, hetero
```

# Graph Dataset Construction
  ### Construct connection dataframe
  **Note** `target` column **must** contain list of connected elements. Example
  |source|target|
  |------|------|
  |'t0001'|['u0001', 'u0005', 'u0010']|
  |'t0002'|['u0001', 'u0008', 'u0012']|
  
  ```python
  >>> dfConn = construct.get_connection_table(df, target='retweeter_ids')
  >>> dfConn
  ```
|source|target|
|------|------|
|'t0001'|'u0001'|
|'t0001'|'u0005'|
|'t0001'|'u0010'|
|'t0002'|'u0001'|
|'t0002'|'u0008'|
|'t0002'|'u0012'|
