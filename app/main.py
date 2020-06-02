from flask import Flask
from flask import jsonify 
import pandas as pd
# from app.data.connection import db_session
# from app.data.models import QC_Wholesale
from app.data.connection import DF_QC_WHOLESALE
  
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
        result = {}
        for index, row in DF_QC_WHOLESALE.iterrows():
                result[index] = dict(row)
        return jsonify(result)
        

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#         db_session.remove()

 
