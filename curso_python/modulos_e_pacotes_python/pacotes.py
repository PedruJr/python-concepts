"""
    Pacotes Python

    Modulo - Qualquer arquivo .py com funçoes e atributos
    Pacote - Diretorio contendo uma coleção de modulos

    OBS: nas versões 2.x do python é necessario ter um arquivo
    __init__.py

    nas versões 3.x não precisa, porem são colocados por compatibilidade

"""
from pacote_python import geek1, geek2
#pacote dentro de pacote
from pacote_python.pacote_python2 import geek3, geek4
#Metodo dentro do pacote dentro de pacote
from pacote_python.pacote_python2.geek3 import funcao3

print(geek1.pi)
print(geek1.funcao1(2, 3))
print(geek2.funcao2)
print(geek2.curso)
print(geek3.funcao3())
print(geek4.funcao4())

