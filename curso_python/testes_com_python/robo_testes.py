import unittest
from robo import Robo

class RoboTestes(unittest.TestCase):

    def setUp(self):
        #Cria o objeto e deixa disponivel, porem precisamos acessar com
        #self.nomeDaVar
        print('setUp() sendo executado...')
        self.megaman = Robo('Mega Man', bateria=50)

    def test_carregar(self):
        #megaman = Robo('Mega Man', bateria=50) - CODIGO REPETIDO - ARRUMAR NO SETUP()
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        #megaman = Robo('Mega Man', bateria=50) - CODIGO REPETIDO - ARRUMAR NO SETUP()
        self.assertEqual(self.megaman.dizer_nome(),
        'BEEP BOOP BEE BOOP, EU SOU MEGAMAN')
        self.assertEqual(self.megaman.bateria, 49,
        'A bateria deveria estar em 49%')

    def tearDown(self):
        print('tearDown() sendo executado...')


#Condição caso este arquivo seja executado,
#Rodara somente ele, executando a rotina de testes
if __name__ == '__main__':
    unittest.main()