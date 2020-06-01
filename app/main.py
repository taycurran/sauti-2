from flask import Flask
from flask import jsonify 
import pandas as pd
from data.connection import db_session
from data.models import QC_Wholesale
  
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
        return QC_Wholesale.query.all()

@app.teardown_appcontext
def shutdown_session(exception=None):
        db_session.remove()

 
