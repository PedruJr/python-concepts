"""
    Pickle - Python
    -> Pickle transforma objeto python em binario e de bineario para objeto python
        Este processo se chama de serialização/deserialização
        OBS: Metodo não seguro contra dados maliciosos, desta forma
        não recomendamos trabalhar com arquivos pickle de outras pessoas que
        não conheça ou fonte desconhecidas.

        Não abrir pickles de fontas desconhecidas, podem ter codigos
        maliciosos que roubam dados ou destroem arquivos.

"""
import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome
    # Usamos property para acessar atributos privados
    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.nome} esta comendo')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} esta miando...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.__nome} esta latindo...')


felix = Gato('Felix')
pluto = Cachorro('Pluto')

#WB = W:write - B:binario
#Escrita de arquivos pickle/binarios
with open('animais.pickle', 'wb') as arquivo:
    #dump recebe dois parametros, neste caso uma tupla, e o arquivo que queremos escrever
    #Metodo para serializar em binario,
    pickle.dump((felix, pluto), arquivo)

#Leitura de dados em arquivos pickle
#RB de READ Binary
with open('animais.pickle', 'rb') as arquivo:
    #traduzimos atravez do metodo load() descompactando os dados e colocando nos objetos
    #Transformando nos objetos que foram codificados para binario
    gato, cachoro = pickle.load(arquivo)
