import sqlite3
import pandas as pd
conn = sqlite3.connect("data/employee.db")
   

df=pd.read_sql_query("SELECT * FROM employees", conn)
print(df)
conn.close()