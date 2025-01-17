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
    
    url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_{}.csv.gz'
    months = ['2020-10', '2020-11', '2020-12']
    
#    df = pd.read_csv(url, sep=",", compression="gzip", low_memory=False)
#    print(df.columns)

    taxi_dtypes = {
                'VendorID': pd.Int64Dtype(),
                'passenger_count': pd.Int64Dtype(),
                'trip_distance': float,
                'RatecodeID': pd.Int64Dtype(),
                'store_and_fwd_flag': str,
                'PULocationID': pd.Int64Dtype(),
                'DOLocationID': pd.Int64Dtype(),
                'payment_type': pd.Int64Dtype(),
                'fare_amount': float,
                'extra': float,
                'mta_tax': float,
                'tip_amount': float,
                'tolls_amount': float,
                'improvement_surcharge': float,
                'total_amount': float,
                'congestion_surcharge': float 
            }
   
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    dfs = pd.DataFrame()
    
    for month in months:
        df = pd.read_csv(url.format(month), sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)
        dfs = pd.concat([dfs, df], ignore_index=True)
    
    #dfs['lpep_pickup_YM'] = dfs['lpep_pickup_datetime'].dt.strftime('%Y-%m')
    #print(dfs['lpep_pickup_YM'].unique())
    #print(dfs.dtypes)

    return dfs
