import pandas as pd

url = 'https://github.com/p4zaa/GraphPrepKit/tree/main/'
data_path = 'GraphPrepKit/dataset' #GitHub Path

def load(title: str):
    df = pd.read_csv(url + data_path + f'/{title}.csv')
    # Additional processing or modifications to the dataframe can be done here
    return df
