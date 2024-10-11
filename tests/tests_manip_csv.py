import unittest
import os
import sys
import pandas as pd
import pandas.testing as pdt

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


import manipulacao_csv as mc

class TestLerCSV(unittest.TestCase):
    def test_abrir_csv(self): 
        pdt.assert_frame_equal(mc.ler_csv("../tests/arquivos_testes/test_abrir_csv.csv"), pd.DataFrame({"col1": [1, 2], "col2": [3, 4]}))
        # Testa abrir um csv normal
    def test_csv_inexistente(self): 
        # Testa abrir um arquivo inexistente ou com caminho errado
        with self.assertRaises(FileNotFoundError):
            mc.ler_csv("inexistente.csv")
    def test_abrir_csv_vazio(self): 
        # Testa abrir um csv vazio
        with self.assertRaises(pd.errors.EmptyDataError):
            mc.ler_csv("../tests/arquivos_testes/test_csv_vazio.csv")
    def test_abrir_csv_apenas_cabecalho(self): 
        # Testa abrir um CSV apenas com a primeira linha
        pdt.assert_frame_equal(mc.ler_csv("../tests/arquivos_testes/test_apenas_cabecalho.csv"), pd.DataFrame(columns=["col1", "col2"]))

        
class TesteFiltrarColunas(unittest.TestCase):
    def setUp(self):
        # DataFrame exemplo para os testes
        self.df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': [4, 5, 6],
            'col3': [7, 8, 9]
        })
    
    def test_filtrar_colunas_existentes(self):
        # Testa a filtragem de colunas existentes
        resultado = mc.filtrar_colunas(self.df, ['col1', 'col2'])
        esperado = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
        pd.testing.assert_frame_equal(resultado, esperado)
    
    def test_filtrar_coluna_unica(self):
        # Testa a filtragem de uma única coluna
        resultado =mc.filtrar_colunas(self.df, ['col3'])
        esperado = pd.DataFrame({'col3': [7, 8, 9]})
        pd.testing.assert_frame_equal(resultado, esperado)
    
    def test_coluna_inexistente(self):
        # Testa quando uma coluna não existe no DataFrame
        with self.assertRaises(KeyError):
            mc.filtrar_colunas(self.df, ['col4'])

    
    def test_colunas_na_ordem_errada(self):
        # Testa a filtragem de colunas com a ordem invertida
        resultado = mc.filtrar_colunas(self.df, ['col3', 'col1'])
        esperado = pd.DataFrame({'col3': [7, 8, 9], 'col1': [1, 2, 3]})
        pd.testing.assert_frame_equal(resultado, esperado)


    def test_coluna_vazia_no_data_frame(self):
        # Testa a filtragem quando o DataFrame tem colunas vazias
        df_vazio = pd.DataFrame({'col1': [], 'col2': []})
        resultado = mc.filtrar_colunas(df_vazio, ['col1'])
        esperado = pd.DataFrame({'col1': []})
        pd.testing.assert_frame_equal(resultado, esperado)


    def test_lista_colunas_com_tipo_errado(self):
        # Testa quando a lista de colunas tem tipos incorretos (exemplo, não uma lista de strings)
        with self.assertRaises(KeyError):
            mc.filtrar_colunas(self.df, [1, 2, 3])

    def test_data_frame_com_tipos_variados(self):
        # Testa a filtragem com DataFrame contendo múltiplos tipos de dados
        df_variado = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': ['a', 'b', 'c'],
            'col3': [True, False, True]
        })
        resultado = mc.filtrar_colunas(df_variado, ['col2', 'col3'])
        esperado = pd.DataFrame({'col2': ['a', 'b', 'c'], 'col3': [True, False, True]})
        pd.testing.assert_frame_equal(resultado, esperado)

class TestFiltrarLinhas(unittest.TestCase):

    def setUp(self):
        # DataFrame exemplo para os testes
        self.df = pd.DataFrame({
            'col1': [1, 2, 3, 4, 5],
            'col2': ['A', 'B', 'C', 'D', 'E']
        })
    
    def test_filtrar_linhas_com_um_elemento(self):
        resultado = mc.filtrar_linhas(self.df, 'col1', 3)
        esperado = pd.DataFrame({'col1': [3], 'col2': ['C']})
        resultado.reset_index(drop=True, inplace=True)  # Reseta o índice para evitar diferenças
        pd.testing.assert_frame_equal(resultado, esperado)
    
    def test_filtrar_linhas_com_varios_elementos(self):
        # Testa filtragem de várias linhas com múltiplos elementos na coluna
        resultado = mc.filtrar_linhas(self.df, 'col1', 2, 4)
        esperado = pd.DataFrame({'col1': [2, 4], 'col2': ['B', 'D']})
        pd.testing.assert_frame_equal(resultado, esperado)
    
    def test_filtrar_linhas_com_elementos_na_coluna_string(self):
        # Testa filtragem de várias linhas com múltiplos elementos em uma coluna string
        resultado = mc.filtrar_linhas(self.df, 'col2', 'B', 'D')
        esperado = pd.DataFrame({'col1': [2, 4], 'col2': ['B', 'D']})
        pd.testing.assert_frame_equal(resultado, esperado)
    
    def test_filtro_com_coluna_inexistente(self):
        # Testa filtragem com coluna que não existe
        with self.assertRaises(KeyError):
            mc.filtrar_linhas(self.df, 'col3', 1)
    
    def test_filtro_sem_resultados(self):
        # Testa filtragem onde nenhum dos elementos está presente na coluna
        resultado = mc.filtrar_linhas(self.df, 'col1', 10)
        esperado = pd.DataFrame({'col1': pd.Series([], dtype='int64'), 'col2': pd.Series([], dtype='object')})
        resultado.reset_index(drop=True, inplace=True)  # Reseta o índice
        pd.testing.assert_frame_equal(resultado, esperado)
    
    def test_filtro_elementos_nao_existem(self):
        resultado = mc.filtrar_linhas(self.df, 'col2', 'X', 'Y')
        esperado = pd.DataFrame({'col1': pd.Series([], dtype='int64'), 'col2': pd.Series([], dtype='object')})
        resultado.reset_index(drop=True, inplace=True)  # Reseta o índice
        pd.testing.assert_frame_equal(resultado, esperado)
    
    def test_filtro_com_data_frame_vazio(self):
        # Testa quando o DataFrame está vazio
        df_vazio = pd.DataFrame(columns=['col1', 'col2'])
        resultado = mc.filtrar_linhas(df_vazio, 'col1', 1)
        esperado = pd.DataFrame(columns=['col1', 'col2'])
        pd.testing.assert_frame_equal(resultado, esperado)
    
    def test_filtro_com_coluna_vazia(self):
        df_coluna_vazia = pd.DataFrame({'col1': pd.Series([], dtype='int64'), 'col2': pd.Series([], dtype='object')})
        resultado = mc.filtrar_linhas(df_coluna_vazia, 'col1', 1)
        esperado = pd.DataFrame({'col1': pd.Series([], dtype='int64'), 'col2': pd.Series([], dtype='object')})
        pd.testing.assert_frame_equal(resultado, esperado)
    
    def test_filtro_com_tipo_incorreto_para_coluna(self):
        # Testa quando o tipo do argumento passado não é compatível com o tipo da coluna (ex: string em coluna numérica)
        resultado = mc.filtrar_linhas(self.df, 'col1', 'A')
        esperado = pd.DataFrame({'col1': pd.Series([], dtype='int64'), 'col2': pd.Series([], dtype='object')})
        resultado.reset_index(drop=True, inplace=True)  # Reseta o índice
        pd.testing.assert_frame_equal(resultado, esperado)
    
    def test_filtro_com_varios_elementos(self):
        # Testa a funcionalidade com múltiplos elementos
        resultado = mc.filtrar_linhas(self.df, 'col2', 'A', 'B', 'C')
        esperado = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['A', 'B', 'C']})
        pd.testing.assert_frame_equal(resultado, esperado)
        
        
class TestFiltrarLinhasPorElementoEmLista(unittest.TestCase):

    def setUp(self):
        # DataFrame de exemplo para os testes
        self.df = pd.DataFrame({
            'col1': [[1, 2, 3], [4, 5], [3, 6], [1, 7]],
            'col2': ['A', 'B', 'C', 'D']
        })

    def test_filtrar_elemento_existente(self):
        # Testa se a função filtra corretamente por um elemento existente na lista
        resultado = mc.filtrar_linhas_por_um_elemento_em_lista(self.df, 'col1', 3)
        esperado = pd.DataFrame({
            'col1': [[1, 2, 3], [3, 6]],
            'col2': ['A', 'C']
        }).reset_index(drop=True)  # Reset index para comparar corretamente
        
        pd.testing.assert_frame_equal(resultado.reset_index(drop=True), esperado)

    def test_filtrar_elemento_nao_existente(self):
        # Testa se a função retorna um DataFrame vazio quando o elemento não está presente
        resultado = mc.filtrar_linhas_por_um_elemento_em_lista(self.df, 'col1', 8)
        esperado = pd.DataFrame({
            'col1': pd.Series([], dtype='object'),
            'col2': pd.Series([], dtype='object')
        })
        
        pd.testing.assert_frame_equal(resultado, esperado)


    def test_filtrar_coluna_nao_lista(self):
        # Testa se a função lida com uma coluna que não contém listas (deve retornar um DataFrame vazio)
        with self.assertRaises(TypeError):
            df_nao_lista = pd.DataFrame({
                'col1': [1, 2, 3, 4],
                'col2': ['A', 'B', 'C', 'D']
            })
            mc.filtrar_linhas_por_um_elemento_em_lista(df_nao_lista, 'col1', 3)


if __name__ == "__main__":    
    unittest.main(verbosity=2)
