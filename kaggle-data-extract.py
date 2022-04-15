#from kaggle.api.kaggle_api_extended import KaggleApi
##api.authenicate()
#api.dataset_download_files('colearninglounge/chronic-kidney-disease')

from sqlalchemy import create_engine
import json
import mariadb
import requests
import io
import sys
import pandas as pd

#API Token
bearer_token = '20c5175c33ad7781d3e2b37ffa16badb'

#Data Retrieval
url="https://www.kaggle.com/datasets/colearninglounge/chronic-kidney-disease/download"
headers = { 'authorization': 'Bearer {0}'.format(bearer_token),}
response = requests.request("GET", url, headers=headers)

print(response.text)

"""

#pip install fsspec (to get bottom extension to work)
df = pd.read_json(response.text)

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user=user.username, #change to your username
        password=user.password, #change 
        host=user.hostname,
        port=3306,
        database="kidney"
    )

#error message
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

#Convert DF into mariaDB format
engine_string = f"mysql+mysqlconnector://{user.username}:{user.password}@{user.hostname}/classicmodels"
engine = create_engine(engine_string) #change root:pass to your username:password
df.to_sql(name='kidney-data', con=engine, if_exists='replace', index=False)

"""







