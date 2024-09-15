import pandas as pd

# Criando um DataFrame com as informações fornecidas
data = {
    'Linha': ['004', '008', '032', '045', '098', '113', '112', '127', '179', '173', '076', '096', '108', '122', '140', '152', '168', '173', '191', '175', '165', '132', '118', '092', '037'],
    'Paradas': [62, 37, 32, 92, 37, 95, 109, 73, 63, 60, 49, 74, 54, 61, 53, 36, 22, 60, 29, 51, 38, 55, 33, 38, 18],
    'Duração (minutos)': [59, 36, 28, 92, 35, 99, 124, 72, 68, 85, 67, 53, 50, 47, 46, 35, 15, 85, 31, 58, 46, 55, 41, 28, 11]
}

df = pd.DataFrame(data)

# Analisando estatísticas descritivas
descriptive_stats = df.describe()

import ace_tools as tools; tools.display_dataframe_to_user(name="Estatísticas Descritivas", dataframe=descriptive_stats)
