import sys

# Adiciona o caminho para a pasta plot
sys.path.append('../plot')

# Importa todos os arquivos de plotagem
import plot_geral_hipoteses as pgh

# Plota todos os graficos
pgh.plotar_h1(pgh.dados_filtrados)
pgh.plotar_h2(pgh.dados_filtrados)
pgh.plotar_h3(pgh.dados_filtrados)
pgh.plotar_h4(pgh.dados_filtrados)