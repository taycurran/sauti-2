from flask import Flask
from flask import jsonify 
import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd


labs_conn = psycopg2.connect(os.getenv("DATABASE_URL"))
labs_curs = labs_conn.cursor()

Q_select_all = """SELECT product_name, market_id,
                source_id, currency_code, date_price,
                        observed_price, observed_class
                        FROM product_clean_wholesale_info;"""
labs_curs.execute(Q_select_all)
print("\nSELECT * Query Excecuted.")

rows = labs_curs.fetchall()

df = pd.DataFrame(rows, columns= [
                "product_name", "market_id", "source_id",
                "currency_code", "date_price", "observed_price",
                "observed_class"
        ])
labs_curs.close()
labs_conn.close()
print("Cursor and Connection Closed.")

df['market'] = df['market_id'].str.split().str[0:-2].str.join(" ")
df['country'] = df['market_id'].str.split().str[-1]
cols = ['country', 'market', 'product_name','date_price', 'observed_price', 'currency_code', 'observed_class',
        'market_id', 'source_id']
df = df[cols]

print(df.head())
