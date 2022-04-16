"""

    Metodos Magicos - Todos os metodos que utilizam dunder. __init__ double under

    dunder init -> double underscore __init__

    -> Verificar os dunders possiveis em uma classe dir(__builtin__)

"""
class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__title = titulo
        self.__autor = autor
        self.__paginas = paginas

    #melhorar apresentação no print, muda a representação do objeto
    def __repr__(self):
        return f'{self.__title} escrito por {self.__autor}'

    #representação para os usuarios finais, tem preferencia no lugar de repr
    def __str__(self):#retorna mesma coisa que o repr, porem este é para o user final
        return self.__title

    #podemos adicionar um atributo para leitura do len no objeto
    def __len__(self):#Metodo dunder len __len__
        return self.__paginas

    #podemos utilizar o delete no objeto, porem sobrescrever o retorno do del
    #Isso ate quando o programa acaba ele retorna esta mensagem
    def __del__(self):
        print(f'Um livro foi deletado da memoria')

    #Podemos utilizar o dunder add para organizar um processo de adição caso o bojeto
    #seja utilizada em uma operação matematica de soma
    def __add__(self, other):
        return f'{self} - {other}'

    #Mesma coisa so que ao multiplicar
    def __mul__(self, other):
        #checar se other é istring
       if isinstance(other, str):
            return f'{self} * {other}'









livro1 = Livro('Python Records', 'Geeker Autor', 100)
livro2 = Livro('Python Metrics', 'Geeker Autor', 200)
