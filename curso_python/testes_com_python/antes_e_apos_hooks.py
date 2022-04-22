"""
    UnitTest - Antes e apos dos hooks
    -> hooks sao a execução dos testes(Os testes em si)

    Metodos preparatorios para aplicar antes e depois nos
    testes(hook processamento do teste) ->

    setup() -> executado antes de cada metodo de teste,
    -> util para criar instâncias de objetos e outros dados;

    tearDown() -> é executado ao final de cada Método de teste.
    -> util para excluir dados ou fechar conexões com banco de dados.

"""

import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self):#configuramos este primeiro
        #Configuração do setUp
        pass

    def test_primeiro(self):
        #setUp vai rodar antes do teste
        #tearDown() vai rodar após o teste
        pass

    def test_segundo(self):
        #setUp vai rodar antes do teste
        #tearDown() vai rodar após o teste
        pass

    def tearDown(self):#este por ultimo
        #setUp vai rodar antes do teste
        #tearDown() vai rodar após o teste
        pass

