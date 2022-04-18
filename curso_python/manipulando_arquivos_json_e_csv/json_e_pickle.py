"""
    Trabalhando com JSON com Pickle

    JSON -> Javascript Object Notation
    PIP INSTALL JSONPICKLE para interagir com pickle e json
"""
import json

#json.dump formata redondo para o formato json que utiliza aspas
ret = json.dump(['produto', {'Playstation 4': ('2TB', 'Novo', '220v', 2340)}])

print(type(ret))

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property #Geter @Property para acesso a atributos privados
    def nome(self):
        return self.__nome

    @property #Geter @Property para acesso a atributos privados
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')#Instanciando classe Gato

print(felix.__dict__)# Dicionario

ret = json.dump(felix.__dict__)

print(ret)

##PIP INSTALL JSONPICKLE para interagir com pickle e json
##EX:
## ret == jsonpicle.encode(feliix)
##print(ret)

##Objeto python para json e json para objeto python
import pickle

#Encode
with open('felix.json', 'w') as arquivo:
    #ret = jsonpickle.encode(felix)
    ret = pickle.encode(felix)
    arquivo.write(ret)

##Decode
with open('felix.json', 'w') as arquivo:
    # ret = jsonpickle.encode(felix)
    ret = pickle.decode(felix)
    arquivo.write(ret)