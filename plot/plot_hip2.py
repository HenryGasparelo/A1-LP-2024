#Plot2 Disperção
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys

# Para poder importar o módulo a partir do diretório '../src'
sys.path.append('../src')

import dataframes_hipoteses as dh
import main as mn

# Carregar o dataset
df = pd.DataFrame(dh.gerar_dataframe_hipotese2(mn.dados))

# Criar o gráfico
g = sns.lmplot(
    data=df,
    x="PeriodoCodando", y="Salario", hue="LinguagemProgramacao",
    height=5, palette="tab10"
)

# Alterar o título da legenda (índice do hue)
g._legend.set_title("Linguagens")

# Ajustar os rótulos dos eixos
plt.xlabel("Período Codando", labelpad=17)
plt.ylabel("Salário", labelpad=17)

# Exibir o gráfico
plt.show()
