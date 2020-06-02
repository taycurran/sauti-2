import psycopg2
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()

labs_conn = psycopg2.connect(os.getenv(""))
labs_curs = labs_conn.cursor()

Q_select_all = """SELECT * FROM qc_wholesale LIMIT 200;"""
labs_curs.execute(Q_select_all)
print("\nSELECT Query Excecuted")

DF_QC_WHOLESALE = pd.DataFrame(labs_curs.fetchmany(200))
print(DF_QC_WHOLESALE.head())

labs_curs.close()
labs_conn.close()
print("Cursor and Connection Closed.")