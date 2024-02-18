import pandas as pd
from sqlalchemy import create_engine
import pyarrow.parquet as pq
from google.cloud import storage

#------------------------------------------------------------------------------------------------------------------


# engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
# engine.connect()

# # df = pd.read_csv('https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz')
# # print(df.head(10))
# # print(df.info)

# query = """
#     SELECT *
#       FROM mage.green_taxi
#     LIMIT 100
# """

# df = pd.read_sql(query, con=engine)
# print(df)

#------------------------------------------------------------------------------------------------------------------

# Ruta al archivo Parquet en Google Cloud Storage
bucket_name = 'mage-zoomcamp-jc'
blob_name = 'nyc_green_taxi_data_2022'
key_path = '02-workflow-orchestration/iconic-atrium-414416-2428e49b5922.json'

# Crea un cliente de Google Cloud Storage usando la clave de la cuenta de servicio
client = storage.Client.from_service_account_json(key_path)

# Obtén el blob del archivo Parquet
bucket = client.get_bucket(bucket_name)

#------------------------------------------------------------------------------------------------------------------

# # Lista los objetos en el bucket
# blobs = list(bucket.list_blobs())

# # Imprime los nombres de los objetos
# for blob in blobs:
#     print(blob.name)

#------------------------------------------------------------------------------------------------------------------
# Leo un parquet en particular

blob = bucket.blob(blob_name)

# Descarga el archivo Parquet localmente
local_filename = 'archivo.parquet'
blob.download_to_filename(local_filename)

# Lee el archivo Parquet usando pyarrow
table = pq.read_table(local_filename)

# Convierte la tabla de pyarrow a un DataFrame de pandas si es necesario
df = table.to_pandas()

#Imprimo el esquema
print(pq.read_schema(local_filename))
print(df.dtypes)

#Imprimo el contenido
#print(df.head())
