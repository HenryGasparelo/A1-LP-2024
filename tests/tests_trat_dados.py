import unittest
import os
import sys
import pandas as pd
import numpy as np

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import tratamento_dados as td


class TestFuncaoSplit(unittest.TestCase):

    def test_split_simples(self):
        # Testa a separação de uma string simples
        resultado = td.funcao_split("a,b,c", ",")
        self.assertEqual(resultado, ["a", "b", "c"])

    def test_split_espacos(self):
        # Testa a separação de uma string com espaços
        resultado = td.funcao_split("a b c", " ")
        self.assertEqual(resultado, ["a", "b", "c"])

    def test_split_sem_separador(self):
        # Testa a separação de uma string sem o separador presente
        resultado = td.funcao_split("abc", ",")
        self.assertEqual(resultado, ["abc"])

    def test_split_separador_inicial(self):
        # Testa a separação de uma string que começa com o separador
        resultado = td.funcao_split(",a,b,c", ",")
        self.assertEqual(resultado, ["", "a", "b", "c"])

    def test_split_separador_final(self):
        # Testa a separação de uma string que termina com o separador
        resultado = td.funcao_split("a,b,c,", ",")
        self.assertEqual(resultado, ["a", "b", "c", ""])

    def test_separador_unico(self):
        # Testa a separação de uma string com um separador único
        resultado = td.funcao_split("abc", "a")
        self.assertEqual(resultado, ["", "bc"])

    def test_string_vazia(self):
        # Testa a separação de uma string vazia
        resultado = td.funcao_split("", ",")
        self.assertEqual(resultado, [""])

    def test_objeto_invalido(self):
        # Testa o comportamento quando o objeto não é uma string
        resultado = td.funcao_split(12345, ",")
        self.assertEqual(resultado, 12345)  # Retorna o objeto original

class TestTratamentoValoresFaltantes(unittest.TestCase):

    def setUp(self):
        # Cria um DataFrame de exemplo para os testes
        self.data = {
            "A": [1, 2, np.nan, 4],
            "B": [np.nan, 5, 6, 7],
            "C": [8, 9, 10, 11]
        }
        self.df = pd.DataFrame(self.data)

    def test_drop_faltantes(self):
        # Testa a remoção de valores faltantes
        resultado = td.tratamento_valores_faltantes(self.df, "A", drop_faltantes=True)
        esperado = self.df.dropna(subset=["A"])
        pd.testing.assert_frame_equal(resultado, esperado)


    def test_sem_tratamento(self):
        # Testa o caso sem tratamento
        resultado = td.tratamento_valores_faltantes(self.df, "A")
        pd.testing.assert_frame_equal(resultado, self.df)


    def test_combinar_drop_e_fill(self):
        # Testa a combinação de drop e fill, onde drop deve prevalecer
        resultado = td.tratamento_valores_faltantes(self.df, "A", drop_faltantes=True, fill_faltantes=True, valor_fill=0)
        esperado = self.df.dropna(subset=["A"])
        pd.testing.assert_frame_equal(resultado, esperado)
        
class TestTratamentoValoresAtipicos(unittest.TestCase):
    
    def setUp(self):
        # DataFrame de exemplo com valores típicos e atípicos
        self.df = pd.DataFrame({
            'Valores': [10, -5, 0, 20, 100, -100, 5]
        })
    
    def test_valores_dentro_limites(self):
        # Teste com limites definidos
        resultado = td.tratamento_valores_atipicos(self.df, 'Valores', limite_inferior_valores=0, limite_superior_valores=50)
        esperado = pd.DataFrame({'Valores': [10, 0, 20, 5]})
        pd.testing.assert_frame_equal(resultado, esperado)

    def test_remover_zero(self):
        # Teste com remoção de valores igual a 0
        resultado = td.tratamento_valores_atipicos(self.df, 'Valores', remover_zero=True)
        esperado = pd.DataFrame({'Valores': [10, -5, 20, 100, -100, 5]})
        pd.testing.assert_frame_equal(resultado, esperado)

    def test_sem_remocao_ou_limites(self):
        # Teste sem remoção ou definição de limites
        resultado = td.tratamento_valores_atipicos(self.df, 'Valores')
        esperado = self.df.reset_index(drop=True)  # Deve retornar o mesmo DataFrame, mas com índice resetado
        pd.testing.assert_frame_equal(resultado, esperado)

    def test_remover_zero_e_limites(self):
        # Teste com remoção de zero e limites definidos
        resultado = td.tratamento_valores_atipicos(self.df, 'Valores', remover_zero=True, limite_inferior_valores=0, limite_superior_valores=20)
        esperado = pd.DataFrame({'Valores': [10, 20, 5]})
        pd.testing.assert_frame_equal(resultado, esperado)

if __name__ == '__main__':
    unittest.main()