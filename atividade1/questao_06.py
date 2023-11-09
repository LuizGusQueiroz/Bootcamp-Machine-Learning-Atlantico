import pandas as pd


def primeiras_linhas_df(caminho):
    df = pd.read_csv(caminho)
    print(df.head())


primeiras_linhas_df('df_ex.csv')
