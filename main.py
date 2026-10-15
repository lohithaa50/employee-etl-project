from extract import extract_data
from transform import transform
from load import load_data

df = extract_data()
clean_df = transform(df)
load_data(clean_df)