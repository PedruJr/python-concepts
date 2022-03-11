"""
    Dunder main e Dunder Name

    Dunder = Double under __ __ __

    Dunder Main = __main__

    Dunder Name = __name__

    Convenção para nao gerar problemas com nomes de variaveis,
    usados para criar funçoes e atributos com __ double under,
    assim nao conflitando com outros elementos.

    ##Ao executar um arquivo python individual, internamente o python
    atribuira o __name__ o valor de __main__, indicando que o modulo é a exec
    principal.

    Podemos condicionar de forma a terem funções que só executam caso o modulo for
    o principal Ex:


"""

## __main__ significa modulo principal
if __name__ == '__main__':
    print('Executa codigo se o arquivo for main, sem isso executa ao ser importado')
else:
    print('Modulo importado - executa se for importado')
