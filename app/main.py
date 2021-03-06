from flask import Flask
from flask import jsonify 
import pandas as pd
# from app.data.connection import db_session
# from app.data.models import QC_Wholesale
import psycopg2
import os
from dotenv import load_dotenv

  
app = Flask(__name__) 
app.config['JSON_SORT_KEYS'] = False

@app.route("/") 
def home_view(): 
        return "<h1>Welcome to Sauti DS</h1>"

@app.route("/dummy_qcwholesale/")
def dummy_qcwholesale():
        df = pd.read_csv("app/qc_wholesale.csv")
        return df.to_json()

@app.route("/data-quality-ws/")
def get_table_dqws():
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


        merged = df.merge(dfM, left_on='market', right_on='market_name')
        merged["id"] = merged["id_x"]
        merged = merged.drop(["id_x", "id_y", "market_id", "market_name"], axis=1)
        cols = ['id', 'market','country_code', 'product', 'source', 'start', 'end', 'timeliness',
        'data_length', 'completeness', 'duplicates', 'mode_D', 'data_points',
        'DQI', 'DQI_cat']
        merged = merged[cols]
        merged['price_category'] = "wholesale"

        result = []
        for index, row in merged.iterrows():
                        result.append(dict(row))
        return jsonify(result)

@app.route("/data-quality-rt/")
def get_table_dqrt():
        labs_conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        labs_curs = labs_conn.cursor()

        Q_select_all = """SELECT * FROM qc_retail;"""
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


        merged = df.merge(dfM, left_on='market', right_on='market_name')
        merged["id"] = merged["id_x"]
        merged = merged.drop(["id_x", "id_y", "market_id", "market_name"], axis=1)
        cols = ['id', 'market','country_code', 'product', 'source', 'start', 'end', 'timeliness',
        'data_length', 'completeness', 'duplicates', 'mode_D', 'data_points',
        'DQI', 'DQI_cat']
        merged = merged[cols]
        merged['price_category'] = "retail"

        result = []
        for index, row in merged.iterrows():
                        result.append(dict(row))
        return jsonify(result)

@app.route("/price-status-ws/")
def get_table_psws():
        labs_conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        labs_curs = labs_conn.cursor()
        
        Q_select_all = """SELECT product_name, market_id,
                        source_id, currency_code, date_price,
                         observed_price, observed_class, stressness
                         FROM product_clean_wholesale_info;"""
        labs_curs.execute(Q_select_all)
        print("\nSELECT * Query Excecuted.")

        rows = labs_curs.fetchall()

        df = pd.DataFrame(rows, columns= [
                        "product_name", "market_id", "source_id",
                        "currency_code", "date_price", "observed_price",
                        "observed_class", "stressness"
                ])
        labs_curs.close()
        labs_conn.close()
        print("Cursor and Connection Closed.")

        df['market'] = df['market_id'].str.split().str[0:-2].str.join(" ")
        df['country'] = df['market_id'].str.split().str[-1]
        cols = ['country', 'market', 'product_name','date_price', 'observed_price', 'currency_code', 'observed_class', 'stressness',
                'market_id', 'source_id']
        df = df[cols]
        df['price_category'] = "wholesale"

        result = []
        for index, row in df.iterrows():
                result.append(dict(row))
        return jsonify(result)

@app.route("/price-status-rt/")
def get_table_psrt():
        labs_conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        labs_curs = labs_conn.cursor()
        
        Q_select_all = """SELECT product_name, market_id,
                        source_id, currency_code, date_price,
                         observed_price, observed_class, stressness
                         FROM product_clean_retail_info;"""
        labs_curs.execute(Q_select_all)
        print("\nSELECT * Query Excecuted.")

        rows = labs_curs.fetchall()

        df = pd.DataFrame(rows, columns= [
                        "product_name", "market_id", "source_id",
                        "currency_code", "date_price", "observed_price",
                        "observed_class", "stressness"
                ])
        labs_curs.close()
        labs_conn.close()
        print("Cursor and Connection Closed.")

        df['market'] = df['market_id'].str.split().str[0:-2].str.join(" ")
        df['country'] = df['market_id'].str.split().str[-1]
        cols = ['country', 'market', 'product_name','date_price', 'observed_price', 'currency_code', 'observed_class', 'stressness',
                'market_id', 'source_id']
        df = df[cols]
        df['price_category'] = "retail"

        result = []
        for index, row in df.iterrows():
                result.append(dict(row))
        return jsonify(result)

        


 
