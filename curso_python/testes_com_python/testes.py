"""
    Complemento do Modulo UnitTest

"""
import unittest
#importar metodos a serem testados
from atividades import comer, dormir, eh_engracada
#Providencia varios metos de assert herdar de 'unittest.TestCase'
class AtividadeTestes(unittest.TestCase):

    def test_comer(self):
        """Testando retorno com comida saudavel"""
        self.assertEqual(
            comer('Quiabo', True),
            'Estou comendo Quiabo porque quero manter a forma.'
        )

    def test_comer_gostosa(self):
        """Testando retorno com comida não saudavel"""
        self.assertEqual(
            comer(comida='Pizza', e_saudavel=False),
            'Hmmm... Jessiquinha.'
        )

    def test_dormir_pouco(self):
        """Testando com pouco descanço"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado apos dormir por 4 horas.'
        )

    def test_dormir_muito(self):
        """Testando com muito descanço"""
        self.assertEqual(
            dormir(8),
            'Ptz! Dormi muito! Estou atrasado para o trabalho!'
        )

    def test_eh_engracada(self):
        """Testando se é uma pessoa engraçada"""
        self.assertFalse(eh_engracada('Sergio Malandro'))
        self.assertTrue(eh_engracada('Jim Carrey'),'Jim deveria ser engraçado')


#Ao executar este arquivo como main, executara os testes do contrario
#não executara
if __name__ == '__main__':
    unittest.main()