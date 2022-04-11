"""
   POO - Atributos

   Atributos -> Caracteristicas dos objetos de forma computacional
    -> Atributos de Instância: Atributos dentro do metodo construtor.
    -> Atributos de Classe:
        Atribuidos fora do construtor.
    -> Atributos de instância:
        ao declarar a classe ou objeto obrigatoriamente possuira este atributo/metodo

"""

class Lampada:

    #Metodo construtor python, onde declaramos os atributos publicos e privados
    def __init__(self, voltagem, cor):
        #atributos de instância
        #private em python é o __ underline
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False

    #metodos para facilitar o acesso aos atributos da classe

    @property
    def voltagem(self):
        return self.__voltagem

    @property
    def cor(self):
        return self.__cor

    @property
    def voltagem(self):
        return self.__ligada

#CLASSE
class ContaCorrente:
    #Metodo da classe, fora seria uma função.A
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos Publicos ou privados, visibilidade utilizando __ setamos o name mangling de privado
# em python nao utilizamos public ou private para setar a visibilidade

class Acesso:

    #Atributo de classe
    #Não precisa de metodo para ser acessado
    impost = 1.00

    # Atributos Publicos ou privados, visibilidade utilizando __ setamos o name mangling de privado
    def __init__(self, email, senha):
        self.__email = email # se torna nome da _classe_ + atributo para acesso = _Acesso_senha -> este é o name mangling
        self.__senha = senha #È apenas uma convenção, python nao te impede de usar

    #getters and setters / atributos de instancia
    def get_senha(self):
        print(self.__senha)

    def get_email(self):
        print(self.__email)

#Atributos dinamicos, podemos simplismente chamar a
# instancia do objeto.nomeDoNovoAtributo "em tempo de execução" e criar um novo atributo

## metodo objeto.__dict__ informa sobre o metodo
