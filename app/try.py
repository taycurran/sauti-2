import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

labs_conn = psycopg2.connect(os.getenv("DATABASE_URL"))
labs_curs = labs_conn.cursor()

Q_select_all = """SELECT product_name, market_id,
                source_id, currency_code, date_price,
                        observed_price, observed_class
                        FROM product_clean_retail_info;"""
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

df['price_category'] = "retail"
df['market'] = df['market_id'].str.split().str[0:-2].str.join(" ")
df['country'] = df['market_id'].str.split().str[-1]
cols = ['country', 'market', 'product_name', 'observed_price', 'observed_class',
        'market_id', 'source_id', 'price_category']
df = df[cols]

print(df.head())