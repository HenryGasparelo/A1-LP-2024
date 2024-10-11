#Hipotese 4.1 linhas empilhadas com marcadores
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys
import numpy as np

# Para poder importar o módulo a partir do diretório '../src'
sys.path.append('../src')

import dataframes_hipoteses as dh
import main as mn

sns.set_theme(style="whitegrid")

# Carregar o dataframe
df = pd.DataFrame(dh.gerar_dataframe_hipotese1_original(mn.dados))

# Paleta personalizada
paleta_linda_hex = ['#DCD301', '#DC0701', '#001EDB']

# Criar o gráfico de linhas empilhadas com marcadores
d = sns.lineplot(
    data=df,
    x="AnosCodando", y="SalarioMedio", hue="Satisfacao", style="Satisfacao",
    markers=True, dashes=False, palette=paleta_linda_hex
)

# Ajustar os rótulos dos eixos
plt.xlabel("Anos Codando", labelpad=17)
plt.ylabel("Salário Médio", labelpad=17)

# Personalizar o título da legenda
d.legend(title="Nível de Satisfação", title_fontsize='13', loc='best')

# Exibir o gráfico
plt.show()
