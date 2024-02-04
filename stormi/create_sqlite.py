import pandas as pd
import sqlite3
from datetime import datetime

# Connect to the database
conn = sqlite3.connect('Hurricane_Weather.sqlite')

# Read the CSV data into a DataFrame
df1 = pd.read_csv('stormi/Resources/dorian_abaco_airtemp.csv').reset_index(drop=False, names="id")

df1.to_sql('Dorain_Abaco', conn, index=False, if_exists='replace', dtype={'id': 'INTEGER PRIMARY KEY'})

df2 = pd.read_csv('stormi/Resources/dorian_mb_airtemp.csv').reset_index(drop=False, names='id')

df2.to_sql('Dorian_MB', conn, index=False, if_exists='replace', dtype={'id': 'INTEGER PRIMARY KEY'})

df3 = pd.read_csv('stormi/Resources/dorian_will_airtemp.csv').reset_index(drop=False, names='id')

df3.to_sql('Dorian_Will', conn, index=False, if_exists='replace', dtype={'id': 'INTEGER PRIMARY KEY'})

df4 = pd.read_csv('macahela/hurricanes.csv')

df4.to_sql('Hurricanes', conn, index=False, if_exists='replace', dtype={'Unnamed: 0': 'INTEGER PRIMARY KEY'})
conn.close()

