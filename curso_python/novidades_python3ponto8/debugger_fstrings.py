"""
    Debugar com Fstrings

    -> Conceito simples utilizando print e F string
    Ex:
"""
resultado = 'yes'
#Ex:
print(f' O resultado é {resultado}')

print(f' O resultado é {2*2:.2f}')

#Ex with Walrus operator
#O escopo do walrus precisa do parenteses entre a chaver
print(f'{(media := 8 * 2)} é a metade de {media*2} ')

#chamando o nome da var com = no final apresentados seu nome e
#conteudo
geek = 'geek'
print(f'{geek.upper()[::-1]=}')