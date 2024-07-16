import pandas as pd

from brfinance import CVMAsyncBackend
from brfinance.utils import get_enet_download_url

from datetime import datetime, date


cvm_httpclient = CVMAsyncBackend()


# Realizando busca por Empresa
start_date = date(2000, 1, 1)
end_date = date.today()
cvm_codes_list = [20613] # B3
category = ["IPE_4_-1_-1"] # Códigos de categoria para DFP, ITR e fatos relevantes # EST_3 - itr  // IPE_4_-1_-1 - Fato Relevante
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


