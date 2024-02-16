from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
engine.connect()

# df = pd.read_csv('https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz')
# print(df.head(10))
# print(df.info)

query = """
    SELECT *
      FROM mage.green_taxi
    LIMIT 100
"""

df = pd.read_sql(query, con=engine)
print(df)