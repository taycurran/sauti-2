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

df = pd.DataFrame(rows, columns= [
        "id", "market", "product", "source",
        "start", "end", "timeliness", "data_length",
        "completeness", "duplicates", "mode_D", "data_points",
        "DQI", "DQI_cat"
])

labs_curs.close()
labs_conn.close()
print("Cursor and Connection Closed.")
result = []
for index, row in df.iterrows():
                result.append(dict(row))
return jsonify(result)
        