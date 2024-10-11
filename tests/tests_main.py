import unittest
import tests_manip_csv
import tests_prep_vizu
import tests_trat_dados

# Cria o TestLoader para carregar os testes de cada arquivo
loader = unittest.TestLoader()

# Cria um TestSuite e adiciona todos os testes dos módulos
suite = unittest.TestSuite()

# Carrega os testes dos arquivos
suite.addTests(loader.loadTestsFromModule(tests_trat_dados))
suite.addTests(loader.loadTestsFromModule(tests_prep_vizu))
suite.addTests(loader.loadTestsFromModule(tests_manip_csv))

# Cria um TestRunner para executar os testes e exibir os resultados
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)

