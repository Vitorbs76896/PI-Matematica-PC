# Importar pandas novamente
import pandas as pd

# Repetindo o cálculo do tempo médio de espera se uma pessoa estiver esperando na metade das paradas de cada linha
tempo_espera = [(p / 2) * (d / p) for p, d in zip(paradas, duracao)]

# Criando um DataFrame para apresentar os tempos de espera por linha
df_espera = pd.DataFrame({
    'Linha': linhas,
    'Tempo de Espera (minutos)': tempo_espera
})

import ace_tools as tools; tools.display_dataframe_to_user(name="Tempos de Espera por Linha", dataframe=df_espera)

df_espera