"""
    Operador Walrus - Presas de Leao Marinho :=
    -> Permite a atribuição e retorno de valor em uma única expressão.
        EX: variavel := expressão
"""
#Padrão
nome = "Peterson"
print(nome)

#Atribuindo o valor e retornando para a func
print(nome := 'Geek University')

#EX2 - Python 3.7
cesta = []
fruta = input('Informe a fruta: ')
while fruta != 'Jaca':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ')


#EX2 - Python 3.8 - repare nas linhas economizadas
cesta = []
while(fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)

