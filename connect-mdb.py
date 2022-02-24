# Module Imports
import mariadb
import sys
import pandas as pd
from sqlalchemy import create_engine
import json
import requests

from config.credentials import user
from config.credentials import nix

#read xls data into dataframe
df = pd.read_excel('./data/zip_code_database.xls')

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user=user.username, #change to your username
        password=user.password, #change 
        host=user.hostname,
        port=3306,
        database="classicmodels"
    )

#error message
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

#Convert DF into mariaDB format
engine_string = f"mysql+mysqlconnector://{user.username}:{user.password}@{user.hostname}/classicmodels"
engine = create_engine(engine_string) #change root:pass to your username:password
df.to_sql(name='zip', con=engine, if_exists='replace', index=False)


#display table
all_tables = pd.read_sql("SHOW tables", engine)
print(all_tables.to_string())
print()
print("zip table looks like: ")
zip_table = pd.read_sql("DESCRIBE zip", engine)
print(zip_table.to_string)
print()

# Get Cursor
cur = conn.cursor()

#Query, can change if need to
query = """
SELECT * FROM zip
ORDER BY RAND()
LIMIT 1
"""
cur.execute(query)
rows = cur.fetchall()
  
for row in rows :
    print(row)
    
#set lat and long
latitude = row[12]
longitude = row[13]

conn.close()

# Nutrition API call
PARAMS = {
    'll': f"{latitude},{longitude}",
    'distance': '5km',
    'limit': 1
}
URL = 'https://trackapi.nutritionix.com/v2/locations'
CREDENTIALS = {
    'x-app-id': nix.app_id,
    'x-app-key': nix.api_key
}

response = requests.get(url=URL,headers=CREDENTIALS, params=PARAMS)
data = response.json()

print(data)