import unittest
import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import preparacao_visualizacao as pv

class TestGenerico(unittest.TestCase):
    def test_generico_1(self):
        self.assertEqual(pv.analise_bidimensional(["entradas"]), "saída")

unittest.main(verbosity=2)