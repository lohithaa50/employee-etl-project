def transform(df):
    df=df.drop_duplicates()
    df["monthly_salary"]=df["monthly_salary"].fillna(0)
    df["annual_salary"] = df["monthly_salary"] * 12
    return df;