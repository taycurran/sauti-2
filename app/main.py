from flask import Flask
from flask import jsonify 
import pandas as pd
# from app.data.connection import db_session
# from app.data.models import QC_Wholesale
import psycopg2
import os
from dotenv import load_dotenv
# import pandas as pd
# load_dotenv()

# labs_conn = psycopg2.connect("")
# labs_curs = labs_conn.cursor()

# Q_select_all = """SELECT * FROM qc_wholesale LIMIT 200;"""
# labs_curs.execute(Q_select_all)
# print("\nSELECT Query Excecuted")

# DF_QC_WHOLESALE = pd.DataFrame(labs_curs.fetchmany(200))
# print(DF_QC_WHOLESALE.head())

# labs_curs.close()
# labs_conn.close()
# print("Cursor and Connection Closed.")
  
app = Flask(__name__) 
  
@app.route("/") 
def home_view(): 
        return "<h1>Welcome to Sauti DS</h1>"

@app.route("/dummy_qcwholesale/")
def dummy_qcwholesale():
        df = pd.read_csv("app/qc_wholesale.csv")
        return df.to_json()

@app.route("/qcwholesale/")
def get_table():
        labs_conn = psycopg2.connect("")
        labs_curs = labs_conn.cursor()

        Q_select_all = """SELECT * FROM qc_wholesale LIMIT 200;"""
        labs_curs.execute(Q_select_all)
        print("\nSELECT Query Excecuted")

        DF_QC_WHOLESALE = pd.DataFrame(labs_curs.fetchmany(200))
        print(DF_QC_WHOLESALE.head())

        labs_curs.close()
        labs_conn.close()
        print("Cursor and Connection Closed.")
        result = {}
        for index, row in DF_QC_WHOLESALE.iterrows():
                result[index] = dict(row)
        return jsonify(result)
        

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#         db_session.remove()

 
