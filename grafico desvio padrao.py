import numpy as np
import matplotlib.pyplot as plt

# Dados dos tempos de espera
wait_times = [5.5, 36, 28, 62, 35, 27.32, 25, 13.57, 35, 25, 5.5, 62, 62, 25, 35, 13.57]
bus_lines = ['Line 037', 'Line 008', 'Line 032', 'Line 112', 'Line 098', 'Line 113', 'Line 045', 'Line 127',
             'Line 179', 'Line 173', 'Line 076', 'Line 096', 'Line 108', 'Line 122', 'Line 140', 'Line 168']

# Cálculos
mean_wait_time = np.mean(wait_times)
median_wait_time = np.median(wait_times)
std_wait_time = np.std(wait_times)

# Gráfico de Espera por Linha de Ônibus
plt.figure(figsize=(10, 6))
plt.bar(bus_lines, wait_times, color='lightblue', edgecolor='black')

# Adicionando título e rótulos
plt.title("Bus Lines Wait Times (Minutes)", fontsize=16)
plt.xlabel("Bus Lines", fontsize=12)
plt.ylabel("Wait Times (Minutes)", fontsize=12)
plt.xticks(rotation=90)

# Adicionando linhas de média, mediana e desvio padrão
plt.axhline(mean_wait_time, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_wait_time:.2f}')
plt.axhline(median_wait_time, color='green', linestyle='dashed', linewidth=2, label=f'Median: {median_wait_time:.2f}')
plt.axhline(mean_wait_time + std_wait_time, color='purple', linestyle='dashed', linewidth=2, label=f'Std (+): {mean_wait_time + std_wait_time:.2f}')
plt.axhline(mean_wait_time - std_wait_time, color='purple', linestyle='dashed', linewidth=2, label=f'Std (-): {mean_wait_time - std_wait_time:.2f}')

# Exibindo legenda
plt.legend()

# Exibir gráfico
plt.tight_layout()
plt.show()