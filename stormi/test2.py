import pandas as pd
import sqlite3
from datetime import datetime

# Connect to the database
conn = sqlite3.connect('weather.sqlite')

# Read the CSV data into a DataFrame
df1 = pd.read_csv('stormi/Resources/chairtemps.csv').reset_index(drop=False, names="id")


df1.to_sql('weather', conn, index=False, if_exists='replace', dtype={'id': 'INTEGER PRIMARY KEY'})


df2 = pd.read_csv('stormi/Resources/sanibelairtemps.csv').reset_index(drop=False, names='id')

df2.to_sql('weather2', conn, index=False, if_exists='replace', dtype={'id': 'INTEGER PRIMARY KEY'})

conn.close()