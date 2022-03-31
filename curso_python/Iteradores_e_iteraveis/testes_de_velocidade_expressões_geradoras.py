"""
    Testes de velocidade com Expressões Geradoras


"""
#Realizar teste de velocidade
import time

#Generetor expression - 1 segundo mais rapido
gen_inicio = time.time()
print(sum(num for num in range(100000000))) #100 milhoes
gen_tempo = time.time() - gen_inicio


#List Comprehension
list_inicio = time.time()
print(sum(num for num in range(100000000))) #100 milhoes
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou {gen_tempo}')
print(f'List comprehension levou {list_tempo}')