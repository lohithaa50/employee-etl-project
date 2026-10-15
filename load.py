import sqlite3
def load_data(df):
    conn = sqlite3.connect("data/employee.db")
    df.to_sql("employees", conn, if_exists="replace", index=False)
    conn.close()