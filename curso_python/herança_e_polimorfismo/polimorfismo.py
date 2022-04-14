"""
    POO - Polimorfismo -> sobrescrita de metodo (Overriding)
    Overrinding -> representação de polimorfismo

    Poli -> Significa Muitos
    Morfis -> Siginifa Formas
    Se comportam de muitas maneiras

"""

class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):#apontar um metodo a ser sobrescrevido
        raise NotImplementedError('A classe filha precisa implementar o metodo')

    def comer(self):#apontar um metodo a ser sobrescrevido
        print(f'{self.__nome} está comendo...')