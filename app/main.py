from flask import Flask
from flask import jsonify 
import pandas as pd
  
app = Flask(__name__) 
  
@app.route("/") 
def home_view(): 
        return "<h1>Welcome to Sauti DS</h1>"

@app.route("/dummy_qcwholesale")
def dummy_qcwholesale():
        df = pd.read_csv("app/qc_wholesale.csv")
        return df.head()

