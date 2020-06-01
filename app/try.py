import pandas as pd
from flask import jsonify

def dummy_qcwholesale():
        df = pd.read_csv("app/qc_wholesale.csv")
        return (df.to_json())

print(dummy_qcwholesale())