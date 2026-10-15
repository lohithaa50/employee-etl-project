import pandas as pd

from transform import transform
def extract_data():
    df = pd.read_csv("data/employee.csv")
    return df;
df = extract_data()
clean_df = transform(df)

print(clean_df)



