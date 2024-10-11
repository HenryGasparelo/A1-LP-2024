#Plot1 com Heatmap, a saude e a media
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys

# Para poder importar o módulo a partir do diretório '../src'
sys.path.append('../src')

import dataframes_hipoteses as dh
import main as mn


sns.set_theme()

df = pd.DataFrame(dh.gerar_dataframe_hipotese1(mn.dados))

# Usar pivot_table para agregar valores duplicados (por exemplo, usando a média)
df_p = df.pivot_table(index="AnosCodando", columns="LinguagemProgramacao", values="HabitosSaudaveis", aggfunc="mean")

#inverter os anos
df_p = df_p.sort_index(ascending=False)

# Criar o heatmap
f, ax = plt.subplots(figsize=(9, 6))

sns.heatmap(df_p, annot=True, fmt=".2f",cmap="magma" , ax=ax)

plt.xlabel("Anos Codando", labelpad=15)  # Espaçamento do rótulo do eixo X
plt.ylabel("Linguagem Programacao", labelpad=15)  # Espaçamento do rótulo do eixo Y


"""
plt.legend(title="Níveis Educacionais", title_fontsize=14, fontsize=12, loc="lower right",  bbox_to_anchor=(1.15, 1))
plt.tight_layout()
"""
# Adicionar uma caixa de texto explicando o índice
plt.text(1.0, 1.05, "Índice de Hábitos Saudáveis",
         transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', alpha=0.6))


plt.show()