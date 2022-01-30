"""
Modulo Collections - Deque

Deque é lista de alta performance, todos os collections são, imagine
como uma lista.

"""

from collections import deque

#criando deque
#isto cria uma lista de letras
deque = deque('geek')

#adicionando elementos no deq atravez de append no final da lista
deque.append('y')

#adicionando um valor ao começo da lista
deque.appendleft('x')

#esta logica de appendleft se aplica ao descartar elementos com .pop
deque.pop('y')

#Exemplo
deque.popleft('x')
