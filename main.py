import pandas as pd
from brfinance import CVMAsyncBackend
from brfinance.utils import get_enet_download_url
from datetime import datetime, date
import ast

cvm_httpclient = CVMAsyncBackend()

df = pd.read_csv('Cad_Cia.csv', sep=';', encoding='latin1')
df['ticker'] = df['ticker'].apply(ast.literal_eval)
codigos = df[df['ibov']==True]['cd_cvm'].tolist()

# Realizando busca por Empresa
start_date = date(2024, 7, 1)
end_date = date.today()
cvm_codes_list = codigos
category = ["IPE_4_-1_-1"] # EST_3 - itr  // IPE_4_-1_-1 - Fato Relevante
last_ref_date = False # Se "True" retorna apenas o último report no intervalo de datas
participant_type = [1] # Companhia aberta

search_result = cvm_httpclient.get_consulta_externa_cvm_results(
    start_date=start_date,
    end_date=end_date,
    cod_cvm=cvm_codes_list,
    participant_type=participant_type,
    category=category,
    last_ref_date=last_ref_date
    )

df = search_result.data()
df.to_csv('RELEVANTE.csv', sep=';')
print(df)


