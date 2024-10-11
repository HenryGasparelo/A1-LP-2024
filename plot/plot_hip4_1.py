#Hipotese 4.1
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys
import numpy as np

# Para poder importar o módulo a partir do diretório '../src'
sys.path.append('../src')

import dataframes_hipoteses as dh
import main as mn

#tema de fundo
sns.set_theme(style="whitegrid")

#dataframe
df = pd.DataFrame(dh.gerar_dataframe_hipotese1_original(mn.dados))

#paleta
paleta_linda_hex = ['#DCD301', '#DC0701', '#001EDB']

#grafo de linhas  empilhadas com marcadores
sns.lineplot(
    data=df,
    x="AnosCodando", y="SalarioMedio", hue="Satisfacao", style="Satisfacao",
    markers=True, dashes=False, palette= paleta_linda_hex
)
plt.show()
