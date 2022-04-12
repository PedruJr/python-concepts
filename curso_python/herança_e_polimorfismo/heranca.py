"""
    Poo - Herança - Reaproveitamento de codigo por classes genericas
    utilizando extensões e derivados.

    Com herança com uma classe existente, extendemos outra classe que passa
    a herdar os atributos e metodos da classe herdada.

    Pergunta a se fazer, existe alguma entidade generica para encapsular os atributos
    e metodos comuns a outras entidades?



"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


#Ao extendermos passando a outra classe como parametro,  podemos
#utilizar os atributos e metodos iguais a classe extendida/herdada
# e apagar as repetiçoes na classe que herdou.
class Cliente(Pessoa):
    """Cliente herda de pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        #metodo para inicializar o construtor da classe herdada: super classe, classe pai
        #classe que herda outra classe: sub classe, classe filha
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

    #Podemos sobrepor metodos
    def nome_completo(self):
        #utilizando super para acessar atributos e metodos
        super().nome_completo()
        #acessando atributo
        print(self._Pessoa__cpf)
        return f' Funcionario Name:{self.__nome} {self.__sobrenome}'

#utilizando metodo herdado
cliente1 = Cliente('Jack', 'Johnson', '100.100.100.63', 5000)
print(cliente1.nome_completo())

