"""
    Argumentos Sómente Posicionais - Recurso antigo
    -> Quando temos um argumento posicional quer dizer que não podemos
    passar o nome da variavel junto com o valor do parametro, pois é somente
    posicional o nome da variavel que enviamos como parametro.
    EX: funcao(x, /) -> chama.funcao(x=10) -< devemos passar somente o 10
    pois o parametro é apenas posicional, não recebe keyword.

    -> Adicionado na 3.8 -> podemos criar nossos proprios metodos, desta
    maneira, com argumentos posicionais.

    -> Assim como temos somente os posicionais, temos os oposto
    que obriga a usar os argumentos com nome
        EX: def cumprimenta(*, nome)

"""
#Lembrando que tudo antes da , / como parametro final se torna argumento
#posicional.
def cumprimenta_v1(nome, /):# Argumento posicional definido por /
    return f'Olá {nome}'

