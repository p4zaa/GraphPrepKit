import pandas as pd
import requests

url = 'https://github.com/p4zaa/GraphPrepKit/tree/main/'
data_path = 'GraphPrepKit/dataset' #GitHub Path

def load(title: str):
    file_url = url + f'{data_path}/{title}.csv'
    response = requests.get(file_url)
    if response.status_code == 200:
        df = pd.read_csv(file_url)
        # Additional processing or modifications to the dataframe can be done here
        return df
    else:
        return None
