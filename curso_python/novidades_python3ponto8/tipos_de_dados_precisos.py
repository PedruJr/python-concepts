"""
    Tipos de Dados mais precisos

    Padrão -> int, str, float, List, Set, Dict, etc

"""
#Tipo Literal
from typing import Literal

#Podemos informar que ira retornar uma string e tambem o valor a ser
#retornado.
def pegar_status(usuario: str) -> Literal['conectado','desconectado']:
    pass

#RETORNANDO ERRO DESTACANDO O PARAMETRO UTILIZADO ERRADO:
    #else:
       # raise ValueError(f'Operação inválida {operacao!r}')