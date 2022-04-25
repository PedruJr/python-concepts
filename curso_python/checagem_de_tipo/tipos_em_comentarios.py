"""
    Tipos em Comentarios


"""
import math

# Estrutura de tipos em comentarios:
# (tipoParamEntrada) -> tipoParamSaida
def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio

#Ex: Com mais parametros
def cabecalho(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'
