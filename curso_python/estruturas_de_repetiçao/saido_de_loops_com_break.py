"""
Saindo de loops com break


"""

#Exemplo
for numero in range(1,11):
    if numero == 6:
        break
    else:
        print(numero)


while True:
    comando = input("Digite 'sair' para saor: ")
    if comando == 'sair':
        break
