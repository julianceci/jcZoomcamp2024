import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    
    url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{}.parquet'
    months = ['2022-01', '2022-02', '2022-03', '2022-04', '2022-05', '2022-06', '2022-07', '2022-08', '2022-09', '2022-10', '2022-11', '2022-12']
    
    dfs = pd.DataFrame()
    
    for month in months:
        df = pd.read_parquet(url.format(month))
        dfs = pd.concat([dfs, df], ignore_index=True)
    
    return dfs
