"""
    Herança e Polimorfismo - metodo super() no python

    -> Metodo super se refere a super classe que é classe pai


"""

class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} faz o som de: {som}')


class Gato(Animal):

    # é possivel usar o super com o proprio nome da classe, mas nao e recomendado:
    # Ex: Animal.__init__(self, nome, especie)
    # Recomendado de forma tradicional Ex:
    def __init__(self, nome, especie, raca):
        super().__init__(self, nome, especie)
        self.__raca = raca
