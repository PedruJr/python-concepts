"""
    Doctests - Complemento do Docstrings

    Para executar doctests no terminal:
        -> python -m docstest -v doctests.py.
        -> Ok o teste passou.
        -> Cuidado com os espaços e a IDE utilizada pois interferem no
        resultado dos testes.

"""
#Ex: Doctest
def soma(a, b):
    """soma os números a e b

    #Isto é um doctest, simulamos um console python
    >>> soma(1, 2)
    3
    #Podemos ter dois testes hehe
    >>> soma(2, 2)
    4
    """
    return a + b


#Ex: Doctest com TDD - Test Driven Development
def duplicar(valores):
    """Duplica valores em uma lista

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []

    >>> duplicar(['a', 'b', 'c', 'd'])
    ['aa', 'bb', 'cc', 'dd']

    >>> duplicar([True, None])# ... representa um conteudo no meio
    TracebacK (most recent call last):
        ...
    TypeError: unsupported operand types(s) for *: 'int' and 'NoneType'
     """
    return [2 * elemento for elemento in valores]

#Ex: Erro Inesperado...
def fala_oi():#Lembrar que entre aspas duplas as prox aspas sao simples
    """Fala oi

    >>> fala_oi() #caso aqui seja "oi" o teste reprova pois espera '' de aspas
    'oi'
    """
    return "oi"