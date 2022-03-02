"""
Erros Comuns em Python

Prestar atenção e ler as saidas de erros - Traceback

1 - SyntaxError -> Python nao reconhece sua escrita da linguagem
Ex: def funcao: << Falta o () do def
Ex: None = 1 palavra reservada resulta em Syntax erro

2 - NameError -> Ocorre quando variavel ou função não foi definida
Ex: print(geek) -> e geek nao foi definido, resultara em NameError
Ex: Quando criamos a definição de uma variavel por condição e ao não executala
uma variavel fica sem dados resultado em NameError ou seja variavel nao definida

3 - TypeError -> Quando uma função/alteração/ação a um tipo nao compativel
Ex: Usar length em um numero = len(5) = TypeError

4 - IndexError -> ao tentar acessar um elemento da lista com um indice invalido
Ex: tentar acessar um indice que nao existe em uma lista, como acessar a posiçao 5 de uma lista
de 4 itens

5 - ValueError -> Quando uma função, recebe um argumento com tipo correto, mas valor invalido.
Ex: int('42') -> transforma em 42 num, mas se jogar letras da erro.

6- KeyError -> Ao tentar achar uma posiçao no dicionarios com uma key que nao existe
Ex: dict['ChaveQueNaoEstaNoDict']

7 - AtributeError -> Quando uma variavel não tem atributo ou função
Ex: Quando tentamos usar um metodo nativo de um tipo de atributo em outro, ccomo o .sort() que funciona
somente paras as listas para o outro elementos é sorted

8 - IdentationError -> Ocorre quando nao respeitamos a identação do python de 4 espaços
Ex: Identação de bloco, 4 espaços

OBS: Exceptions e Erros sao sinonimos na programação.

OBS: Importante ler e entender a saida de erros
"""