import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys

#100 quantis em relação ao salário

# Para poder importar o módulo a partir do diretório '../src'
sys.path.append('../src')

import dataframes_hipoteses as dh
import main as mn

# Load the penguins dataset
df =  pd.DataFrame(dh.gerar_dataframe_hipotese2(mn.dados))

# Plot sepal width as a function of sepal_length across days
g = sns.lmplot(
    data=df,
    x="YearsCoding", y="ConvertedSalary", hue="LinguagemProgramacao",
    height=5
)

# Use more informative axis labels than are provided by default
g.set_axis_labels("AnosCodando", "SalarioAnual(convertido)")
plt.show()