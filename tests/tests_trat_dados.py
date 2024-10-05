import unittest
import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

import tratamento_dados as dt


class TestGenerico(unittest.TestCase):
    def test_generico_1(self):
        self.assertEqual(dt.funcao_split("Barcelona,Real Madrid,PSG,Vasco",","), ["Barcelona", "Real Madrid", "PSG","Vasco"])

unittest.main(verbosity=2)
