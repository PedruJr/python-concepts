"""
    Escrevendo Iterador Custom

"""

class Contador:
    #Função especial consultor, responsavel por criar os objetos
    #Funções dentro de classe inicial com self
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior
    ##Transformando classe em Iter
    def __iter__(self):
        return self

    ##Necessita o next tambem para virar iter
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

#Funções dentro de uma classe são chamados de metodos
con = Contador(1, 61)
## Agora a classe contador pode virar iterator
it = iter(con)

for n in Contador(1, 61):
    print(n)

