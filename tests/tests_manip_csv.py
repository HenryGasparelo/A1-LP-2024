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
    def test_csv_inexistente(self): 
        with self.assertRaises(FileNotFoundError):
            mc.ler_csv("inexistente.csv")
    def test_abrir_csv_vazio(self): 
        with self.assertRaises(pd.errors.EmptyDataError):
            mc.ler_csv("../tests/arquivos_testes/test_csv_vazio.csv")
    def test_abrir_csv_apenas_cabecalho(self): 
        pdt.assert_frame_equal(mc.ler_csv("../tests/arquivos_testes/test_apenas_cabecalho.csv"), pd.DataFrame(columns=["col1", "col2"]))
    def test_abrir_csv_mal_formatado(self): 
        with self.assertRaises(pd.errors.EmptyDataError):
            mc.ler_csv("../tests/arquivos_testes/test_csv_mal_formatado.csv")
    def test_abrir_arquivo_txt(self): 
        with self.assertRaises(pd.errors.EmptyDataError):
            mc.ler_csv("../tests/arquivos_testes/test_arquivo_texto.txt")
    def test_dados_mistos(self):
        pdt.assert_frame_equal(mc.ler_csv("../tests/arquivos_testes/test_dados_mistos.csv"), pd.DataFrame({"col1": [1, "dois"], "col2": [3.0, "quatro"]}))


if __name__ == "__main__":    
    unittest.main(verbosity=2)
