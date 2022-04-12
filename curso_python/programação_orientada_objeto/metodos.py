"""
    POO - Metodos

    -> Metodos/Funções: processamento/rotinas/ações da classe/objeto,
    que podem receber ou não parametros de entrada e pode ter ou não um retorno final

    Metodos de instancia: Acesso aos atributos da classe

    metodos de classe: Conhecidos como metodos estaticos

    -> __init__: dunder init é o metodo construtor
    ->Metodos dunder sao metodos magicos


"""

class Usuario:

    contador = 0

    #Decorator de metodo em classes
    @classmethod
    def conta_usuarios(cls):#CLS é a compensão que manda a propria classe como parametro para o metodo
        print(f'Temos {cls.contador} usuarios no sistema')

    #Decorator de metodo estatico classes
    @staticmethod # sem acesso a classe
    def definicao():#CLS é a compensão que manda a propria classe como parametro para o metodo
        return 'UXR344 URRO SHEREK'

    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    #Metodo privado com double under mangling name
    #Metodo de instancia
    @classmethod
    def __gera_usuarios(self):#CLS é a compensão que manda a propria classe como parametro para o metodo
        return self.__email.split('@')[0]

user = Usuario('Rocardo', 'Circo@votstok.com')

#formas de usar o metodo
Usuario.conta_usuarios() #Forma correta
user.conta_usuarios() # Possivel mas incorreta