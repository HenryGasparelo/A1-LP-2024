import unittest
import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


import manipulacao_csv as cm

class TestGenerico(unittest.TestCase):
    def test_generico_1(self):
        self.assertEqual(cm.filtrar_colunas(["entradas"]), "saída")

unittest.main(verbosity=2)