#Exemplo de grafo de linhas
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys
import numpy as np

# Para poder importar o módulo a partir do diretório '../src'
sys.path.append('../src')

import dataframes_hipoteses as dh
import main as mn

# Definir o tema e estilo do gráfico
sns.set_theme(style="whitegrid")

# Criar um DataFrame a partir dos dados
df = pd.DataFrame(dh.gerar_dataframe_hipotese3(mn.dados))

# Definir uma paleta personalizada
paleta_linda_hex = ['#DCD301', '#DC0701', '#001EDB', '#C800DB', '#00DBA3', '#BD7200']

# Criar o gráfico de linhas
plt.figure(figsize=(10, 6))  # Definir o tamanho da figura
sns.lineplot(data=df, x="AnosCodando", y="Empregabilidade", hue="NiveisEducacionais", palette=paleta_linda_hex)


# Adicionar títulos e rótulos com espaçamento personalizado
plt.xlabel("Anos Codando", labelpad=15)  # Espaçamento do rótulo do eixo X
plt.ylabel("Empregabilidade", labelpad=15)  # Espaçamento do rótulo do eixo Y

# Ajustar o tamanho e a posição da legenda (hue)
plt.legend(title="Níveis Educacionais", title_fontsize=14, fontsize=12, loc="lower center")




# Mostrar o gráfico
plt.show()
