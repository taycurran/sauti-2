import pandas as pd
from flask import jsonify

def dummy_qcwholesale():
        df = pd.read_csv("app/qc_wholesale.csv")
        return jsonify(df)

print(dummy_qcwholesale())