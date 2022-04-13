"""
    POO - Propriedades - Properties

    Atributos privados nas classes são alterados por getters e setters
    que apresentam e alteram os valores

    -> Em python podemos utilizar propriedades

"""

class Conta:

    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property #Getter do python
    def numero(self):
        return self.__numero

    @property #Getter do python, pois pega valor
    def titular(self):
        return self.__numero

    @numero.setter##Seter, passando como parametro o valor do set
    def numero(self, novo_limite):
        self.__limite = novo_limite

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'
