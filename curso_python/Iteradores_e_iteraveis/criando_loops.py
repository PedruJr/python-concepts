"""
    Criando seu proprio Loop


"""

for num in [1, 2, 3, 4 ,5]:
    print(num)

for letra in 'Geek University':
    print(letra)

#Por baixo dos panos it1 = iter([1, 2, 3 , 4, 5])
#iter1.next()

#Função loop manual
def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

