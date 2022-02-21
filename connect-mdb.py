# Module Imports
import mariadb
import sys
import pandas as pd
from IPython.display import display
from sqlalchemy import create_engine

from config.credentials import user

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


# Get Cursor
cur = conn.cursor()

#Query, can change if need to
query = f"Select * From zip"

cur.execute(query)

rows = cur.fetchall()
conn.close()
  
for row in rows :
    print(row)