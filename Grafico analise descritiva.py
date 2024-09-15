import matplotlib.pyplot as plt

# Dados fornecidos
linhas = ['004', '008', '032', '045', '098', '113', '112', '127', '179', '173', '076', '096', '108', '122', '140', '152', '168', '173_2', '191', '175', '165', '132', '118', '092', '037']
paradas = [62, 37, 32, 92, 37, 95, 109, 73, 63, 60, 49, 74, 54, 61, 53, 36, 22, 60, 29, 51, 38, 55, 33, 38, 18]
duracao = [59, 36, 28, 92, 35, 99, 124, 72, 68, 85, 67, 53, 50, 47, 46, 35, 15, 85, 31, 58, 46, 55, 41, 28, 11]

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(linhas, paradas, label="Número de Paradas", marker='o')
plt.plot(linhas, duracao, label="Duração da Viagem (min)", marker='o')

# Adicionando título e legendas
plt.title("Análise de Paradas e Duração de Viagens das Linhas de Transporte")
plt.xlabel("Linhas de Transporte")
plt.ylabel("Quantidade")
plt.xticks(rotation=90)
plt.legend()

# Mostrando o gráfico
plt.tight_layout()
plt.show()