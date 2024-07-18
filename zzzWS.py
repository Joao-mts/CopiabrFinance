import pandas as pd
import ast

# Leitura dos dataframes
df = pd.read_csv('cad_cia_aberta.csv', sep=';', encoding='latin1')
df_ibov = pd.read_csv('IBXX.csv', sep=';')
print(df_ibov['Acao'].nunique())

df = df[df['ticker'].notna()]

df['ticker'] = df['ticker'].apply(ast.literal_eval)

lista_tickers = df_ibov['Codigo'].tolist()


df['ibov'] = df['ticker'].apply(lambda x: any(ticker in lista_tickers for ticker in x))

# df = df[df['ibov']==True]

df.to_csv('Cad_Cia.csv', sep=';', encoding='latin1')
