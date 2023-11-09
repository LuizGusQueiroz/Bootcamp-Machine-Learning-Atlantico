import pandas as pd


def trata_nulos(df):
    return df.dropna(axis=1)


df = pd.read_csv('df_ex.csv')
df = trata_nulos(df)
print(df)
