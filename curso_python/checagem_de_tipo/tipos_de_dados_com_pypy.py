"""
    mypy -> Biblioteca que se rodada no terminal sua instancia
    passando oarquivo a ser analisado ele retorna os erros de tipo
    em um log no console
    Ex: mypy duck_typing.py -> Funf apenas com Duck Typing
    -> aponta os bugs para remover

"""

#Type Hinting:   #tipo de dado -> tipo de dado de retorno
def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'

def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f"{texto.title()}".center(50, '#')


print(cabecalho('Geek University'))
print(cabecalho('Geek University', alinhamento=False))

