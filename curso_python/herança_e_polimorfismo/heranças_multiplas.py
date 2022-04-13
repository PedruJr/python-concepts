"""
    Heranças multiplas - Multiderivação

    Acontece de duas formas:
        -> Multiderivação Direta
        -> Multiderivação Indireta

        obs: Geram os mesmos resultados

        obs: Caso seja feita herança multiplas as classes
        possuirem metodos com mesmo nome sera executado o
        Method Resolution Order - MRO -> quer dizer que a ordem
        de ordenação dos parametros na hora de herdar o primeiro a
        ser herdado sobrescreve os metodos

        obs: Podemos utilizar o metodo isistance() para saber do que
        esta variavel é instancia, ele retorna true para todos os tipos
        de classe herdada e tambem true para objeto
"""
#Multiderivação Direta
class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass


#Multiderivação Indireta
class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3):
    pass


