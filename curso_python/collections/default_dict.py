"""
Default Dict

Default Dict ao criar o dicionario, informamos um valor default, caso chamamos uma
chave que não exista vai retornar o valor de default e a chave sera criada.

Lambdas são funçoes sem nome que podem receber ou não parametros de entrada,
retornando um valor: FUNCAO SIMBOLICA
"""

from collections import defaultdict

dicionario = defaultdict(lambda : 0)