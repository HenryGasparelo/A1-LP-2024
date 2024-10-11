import unittest
import os
import sys
import pandas as pd
import numpy as np

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import preparacao_visualizacao as pv

class TestAplicarDicionario(unittest.TestCase):

    def setUp(self):
        # Preparação de um dicionário de exemplo para os testes
        self.dicionario = {
            'a': 1,
            'b': 2,
            'c': 3,
        }

    def test_chave_existente(self):
        # Teste para chave existente
        resultado = pv.aplicar_dicionario('a', self.dicionario)
        self.assertEqual(resultado, 1, "O valor retornado para a chave 'a' deve ser 1")

    def test_chave_inexistente(self):
        # Teste para chave inexistente
        with self.assertRaises(KeyError):
            pv.aplicar_dicionario('z', self.dicionario)

    def test_dicionario_vazio(self):
        # Teste para dicionário vazio
        dicionario_vazio = {}
        with self.assertRaises(KeyError):
            pv.aplicar_dicionario('a', dicionario_vazio)

    def test_chave_valor_nulo(self):
        # Teste para chave com valor nulo no dicionário
        self.dicionario['d'] = None
        resultado = pv.aplicar_dicionario('d', self.dicionario)
        self.assertIsNone(resultado, "O valor retornado para a chave 'd' deve ser None")

    def test_dicionario_com_multiplos_tipos(self):
        # Teste para dicionário com múltiplos tipos de valores
        dicionario_misto = {
            'int': 1,
            'str': 'valor',
            'list': [1, 2, 3],
            'dict': {'chave': 'valor'},
        }
        self.assertEqual(pv.aplicar_dicionario('str', dicionario_misto), 'valor', "O valor retornado para 'str' deve ser 'valor'")
        self.assertEqual(pv.aplicar_dicionario('list', dicionario_misto), [1, 2, 3], "O valor retornado para 'list' deve ser [1, 2, 3]")
        self.assertEqual(pv.aplicar_dicionario('dict', dicionario_misto), {'chave': 'valor'}, "O valor retornado para 'dict' deve ser {'chave': 'valor'}")

class TestModificarDadosUsandoDicionario(unittest.TestCase):

    def setUp(self):
        # DataFrame de exemplo para os testes
        self.dataframe = pd.DataFrame({
            'col1': ['a', 'b', 'c'],
            'col2': [1, 2, 3]
        })
        # Dicionário de mapeamento para os testes
        self.dicionario = {
            'a': 'A',
            'b': 'B',
            'c': 'C'
        }

    def test_modificar_dados_coluna_existente(self):
        # Teste com coluna existente e mapeamento válido
        resultado = pv.modificar_dados_usando_dicionario(self.dataframe, 'col1', self.dicionario)
        esperado = pd.DataFrame({
            'col1': ['A', 'B', 'C'],
            'col2': [1, 2, 3]
        })
        pd.testing.assert_frame_equal(resultado, esperado, check_dtype=True)

    def test_modificar_dados_coluna_nao_existente(self):
        # Teste para coluna inexistente no DataFrame
        with self.assertRaises(KeyError):
            pv.modificar_dados_usando_dicionario(self.dataframe, 'coluna_invalida', self.dicionario)

    def test_modificar_dados_sem_chave_correspondente(self):
        # Teste para casos onde o dicionário não possui chaves para todos os elementos
        dicionario_incompleto = {
            'a': 'A',
            'b': 'B'
        }
        with self.assertRaises(KeyError):
            pv.modificar_dados_usando_dicionario(self.dataframe, 'col1', dicionario_incompleto)

    def test_modificar_dados_com_chave_nao_existente_no_dicionario(self):
        # Teste para chave não encontrada no dicionário
        dataframe_com_elemento_extra = pd.DataFrame({
            'col1': ['a', 'b', 'x'],  # 'x' não está no dicionário
            'col2': [1, 2, 3]
        })
        with self.assertRaises(KeyError):
            pv.modificar_dados_usando_dicionario(dataframe_com_elemento_extra, 'col1', self.dicionario)

    def test_modificar_dados_dicionario_vazio(self):
        # Teste para um dicionário vazio
        dicionario_vazio = {}
        with self.assertRaises(KeyError):
            pv.modificar_dados_usando_dicionario(self.dataframe, 'col1', dicionario_vazio)

    def test_modificar_dados_multiplos_tipos_no_dicionario(self):
        # Teste com valores de diferentes tipos no dicionário
        dicionario_misto = {
            'a': 'String',
            'b': 123,
            'c': [1, 2, 3]
        }
        resultado = pv.modificar_dados_usando_dicionario(self.dataframe, 'col1', dicionario_misto)
        esperado = pd.DataFrame({
            'col1': ['String', 123, [1, 2, 3]],
            'col2': [1, 2, 3]
        })
        pd.testing.assert_frame_equal(resultado, esperado, check_dtype=True)
        
class TestAnaliseUnidimensional(unittest.TestCase):

    def setUp(self):
        # DataFrame de exemplo para os testes
        self.dataframe = pd.DataFrame({
            'col1': [1, 2, 3, 4, 5],
            'col2': [10, 20, 30, 40, 50],
            'col3': [100, 200, 300, 400, 500]
        })

    def test_analise_coluna_valores_normais(self):
        # Teste com uma coluna contendo valores normais
        resultado = pv.analise_unidimensional(self.dataframe, 'col1')
        esperado = {
            'quantidade_de_elementos': 5,
            'media': np.mean([1, 2, 3, 4, 5]),
            'desvio_padrao': np.std([1, 2, 3, 4, 5], ddof=0),
            'minimo': 1,
            'primeiro_quartil': np.quantile([1, 2, 3, 4, 5], 0.25),
            'mediana': np.quantile([1, 2, 3, 4, 5], 0.5),
            'terceiro_quartil': np.quantile([1, 2, 3, 4, 5], 0.75),
            'maximo': 5
        }
        self.assertDictEqual(resultado, esperado)

    def test_analise_coluna_valores_repetidos(self):
        # Teste com uma coluna contendo valores repetidos
        self.dataframe['col_repetida'] = [1, 1, 1, 1, 1]
        resultado = pv.analise_unidimensional(self.dataframe, 'col_repetida')
        esperado = {
            'quantidade_de_elementos': 5,
            'media': 1,
            'desvio_padrao': 0.0,
            'minimo': 1,
            'primeiro_quartil': 1,
            'mediana': 1,
            'terceiro_quartil': 1,
            'maximo': 1
        }
        self.assertDictEqual(resultado, esperado)

    def test_analise_coluna_com_valores_faltantes(self):
        # Teste com uma coluna contendo valores NaN
        self.dataframe['col_nan'] = [1, np.nan, 3, np.nan, 5]
        resultado = pv.analise_unidimensional(self.dataframe.dropna(), 'col_nan')
        esperado = {
            'quantidade_de_elementos': 3,
            'media': np.mean([1, 3, 5]),
            'desvio_padrao': np.std([1, 3, 5], ddof=0),
            'minimo': 1,
            'primeiro_quartil': np.quantile([1, 3, 5], 0.25),
            'mediana': np.quantile([1, 3, 5], 0.5),
            'terceiro_quartil': np.quantile([1, 3, 5], 0.75),
            'maximo': 5
        }
        self.assertDictEqual(resultado, esperado)


    def test_analise_coluna_nao_existente(self):
        # Teste para coluna que não existe no DataFrame
        with self.assertRaises(KeyError):
            pv.analise_unidimensional(self.dataframe, 'col_inexistente')
            
class TestAnaliseBidimensional(unittest.TestCase):

    def setUp(self):
        # DataFrame de exemplo para os testes
        self.dataframe = pd.DataFrame({
            'col1': [1, 2, 3, 4, 5],
            'col2': [2, 4, 6, 8, 10],  # Coluna com correlação perfeita com col1
            'col3': [5, 4, 3, 2, 1],   # Coluna inversamente correlacionada com col1
            'col4': [1, 1, 1, 1, 1]    # Coluna com valores constantes
        })

    def test_correlacao_perfeita(self):
        # Teste para correlação perfeita entre 'col1' e 'col2'
        resultado = pv.analise_bidimensional(self.dataframe, 'col1', 'col2')
        esperado = 1.0  # Correlação perfeita
        self.assertAlmostEqual(resultado, esperado, places=5)

    def test_correlacao_inversa(self):
        # Teste para correlação inversa entre 'col1' e 'col3'
        resultado = pv.analise_bidimensional(self.dataframe, 'col1', 'col3')
        esperado = -1.0  # Correlação inversa perfeita
        self.assertAlmostEqual(resultado, esperado, places=5)

    def test_correlacao_colunas_iguais(self):
        # Teste para correlação entre colunas idênticas ('col1' com 'col1')
        resultado = pv.analise_bidimensional(self.dataframe, 'col1', 'col1')
        esperado = 1.0  # Correlação perfeita, pois as colunas são as mesmas
        self.assertAlmostEqual(resultado, esperado, places=5)

    def test_correlacao_colunas_sem_correlacao(self):
        # Teste com colunas sem correlação direta
        self.dataframe['col5'] = [1, 0, 1, 0, 1]  # Coluna com valores sem relação direta com 'col1'
        resultado = pv.analise_bidimensional(self.dataframe, 'col1', 'col5')
        esperado = 0.0  # Aproximadamente 0, pois não há correlação entre 'col1' e 'col5'
        self.assertAlmostEqual(resultado, esperado, places=5)

    def test_coluna_nao_existente(self):
        # Teste para coluna que não existe no DataFrame
        with self.assertRaises(KeyError):
            pv.analise_bidimensional(self.dataframe, 'col1', 'col_inexistente')
            
class TestCriarColunaHabitosSaudaveis(unittest.TestCase):

    def setUp(self):
        # DataFrame de exemplo para os testes
        self.dataframe = pd.DataFrame({
            'HoursComputer': [4, 6, 8, 10, 2],
            'HoursOutside': [2, 4, 1, 0, 5],
            'SkipMeals': [0, 1, 2, 3, 0],
            'Exercise': [1, 2, 0, 1, 3]
        })

    def test_coluna_criada(self):
        # Verifica se a coluna 'HabitosSaudaveis' foi criada corretamente
        resultado = pv.criar_coluna_habitos_saudaveis(self.dataframe)
        self.assertIn('HabitosSaudaveis', resultado.columns)

    def test_valores_habitos_saudaveis(self):
        # Verifica se os valores da coluna 'HabitosSaudaveis' foram calculados corretamente
        resultado = pv.criar_coluna_habitos_saudaveis(self.dataframe)
        esperado = [
            4 * 0.25 + 2 * 0.25 + 0 * 0.25 + 1 * 0.25,  # Para a primeira linha
            6 * 0.25 + 4 * 0.25 + 1 * 0.25 + 2 * 0.25,  # Para a segunda linha
            8 * 0.25 + 1 * 0.25 + 2 * 0.25 + 0 * 0.25,  # Para a terceira linha
            10 * 0.25 + 0 * 0.25 + 3 * 0.25 + 1 * 0.25, # Para a quarta linha
            2 * 0.25 + 5 * 0.25 + 0 * 0.25 + 3 * 0.25   # Para a quinta linha
        ]
        np.testing.assert_array_almost_equal(resultado['HabitosSaudaveis'].values, esperado, decimal=5)

    def test_data_completa(self):
        # Verifica se o DataFrame retornado contém todos os dados originais além da coluna 'HabitosSaudaveis'
        resultado = pv.criar_coluna_habitos_saudaveis(self.dataframe)
        for col in self.dataframe.columns:
            np.testing.assert_array_equal(resultado[col].values, self.dataframe[col].values)
            
    def test_valores_nulos(self):
        # Testa comportamento com valores nulos
        self.dataframe.iloc[0, 0] = np.nan  # Introduz um valor nulo na coluna 'HoursComputer'
        resultado = pv.criar_coluna_habitos_saudaveis(self.dataframe)
        self.assertTrue(pd.isnull(resultado['HabitosSaudaveis'].iloc[0]))  # O valor resultante também deve ser nulo

    def test_colunas_ausentes(self):
        # Testa se ocorre erro quando colunas necessárias estão ausentes
        dataframe_incompleto = pd.DataFrame({
            'HoursComputer': [4, 6, 8],
            'HoursOutside': [2, 4, 1]  # Falta 'SkipMeals' e 'Exercise'
        })
        with self.assertRaises(KeyError):
            pv.criar_coluna_habitos_saudaveis(dataframe_incompleto)
            
class TestCalcularEmpregabilidade(unittest.TestCase):

    def setUp(self):
        # DataFrame de exemplo para os testes
        self.dataframe = pd.DataFrame({
            'Employment': [
                'Employed part-time',
                'Unemployed',
                'Employed full-time',
                'Independent contractor, freelancer, or self-employed',
                'Unemployed'
            ]
        })

    def test_empregabilidade_calculada_corretamente(self):
        # Testa a taxa de empregabilidade com dados conhecidos
        resultado = pv.calcular_empregabilidade(self.dataframe)
        # Total de programadores: 5
        # Programadores empregados: 3
        # Empregabilidade esperada: 3 / 5 = 0.6
        self.assertAlmostEqual(resultado, 0.6, places=2)

    def test_todos_empregados(self):
        # Testa o caso em que todos os programadores estão empregados
        dataframe_empregados = pd.DataFrame({
            'Employment': [
                'Employed part-time',
                'Employed full-time',
                'Independent contractor, freelancer, or self-employed'
            ]
        })
        resultado = pv.calcular_empregabilidade(dataframe_empregados)
        self.assertAlmostEqual(resultado, 1.0, places=2)

    def test_nenhum_empregado(self):
        # Testa o caso em que nenhum programador está empregado
        dataframe_nenhum = pd.DataFrame({
            'Employment': [
                'Unemployed',
                'Unemployed',
                'Unemployed'
            ]
        })
        resultado = pv.calcular_empregabilidade(dataframe_nenhum)
        self.assertAlmostEqual(resultado, 0.0, places=2)

    def test_data_frame_vazio(self):
        # Testa o caso de um DataFrame vazio
        with self.assertRaises(ZeroDivisionError):
            pv.calcular_empregabilidade(pd.DataFrame(columns=['Employment']))


    def test_valores_invalido(self):
        # Testa a empregabilidade com valores inválidos na coluna 'Employment'
        dataframe_invalido = pd.DataFrame({
            'Employment': [
                'Unknown',
                'Unknown',
                'Unknown'
            ]
        })
        resultado = pv.calcular_empregabilidade(dataframe_invalido)
        # Total de programadores: 3, empregados: 0
        self.assertAlmostEqual(resultado, 0.0, places=2)

if __name__ == '__main__':
    unittest.main(verbosity=3)