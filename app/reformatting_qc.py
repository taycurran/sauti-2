from flask import Flask
from flask import jsonify 
import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd

labs_conn = psycopg2.connect(os.getenv("DATABASE_URL"))
labs_curs = labs_conn.cursor()

Q_select_all = """SELECT * FROM qc_wholesale;"""
labs_curs.execute(Q_select_all)
print("\nSELECT * Query Excecuted.")

rows = labs_curs.fetchall()

df = pd.DataFrame(rows, columns=[
        "id", "market", "product", "source",
        "start", "end", "timeliness", "data_length",
        "completeness", "duplicates", "mode_D", "data_points",
        "DQI", "DQI_cat"
])

Q_select_all = """SELECT * FROM markets;"""
labs_curs.execute(Q_select_all)
print("\nSELECT * Query Excecuted.")

rowsM = labs_curs.fetchall()
dfM = pd.DataFrame(rowsM, columns=["id", "market_id", "market_name", "country_code"])


labs_curs.close()
labs_conn.close()
print("Cursor and Connection Closed.")

print(df.head())
print(dfM.head())

merged = df.merge(dfM, left_on='market', right_on='market_name')
merged["id"] = merged["id_x"]
merged = merged.drop(["id_x", "id_y", "market_id", "market_name"], axis=1)
cols = ['id', 'market','country_code', 'product', 'source', 'start', 'end', 'timeliness',
       'data_length', 'completeness', 'duplicates', 'mode_D', 'data_points',
       'DQI', 'DQI_cat']
merged = merged[cols]
print(merged.head())



        