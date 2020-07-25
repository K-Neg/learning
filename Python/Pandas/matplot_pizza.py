# importar bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# preparar dados para o pie chart
labels = ['Maria','Joao','Lucas']
tamanho = np.random.random(3)
#explode = (0.1, 0.1, 0.1)
explode = (0,0,0)

# plotar o gráfico de pizza
fig, ax = plt.subplots(figsize=(6,6))

ax.pie(tamanho, labels=labels, explode=explode, shadow=True)
ax.set_title("Classificação das nomes")

plt.tight_layout()
plt.show()