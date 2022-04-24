"""
    Duck Typing:
    -> O tipo da variavel é menos importante que o conteudo dentro,
    que é o que realmente define.
    -> Objetos similares tem os mesmos comportamentos.

    Type Hinting:
    -> Solução formal de formatação para apontar o tipo de dado

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