"""
    Geradores são iterators

    - Iteratos não sao generators
    - Generetors podem ser criados com funçoes ou expressoes geradoras
    - Funçoes geradoras usam a palavra reservada yield
    - Função utiliza return(retorna uma vez), Generator function usa yield(Retorna multiplas vezes)

"""

#Exemplo de Generetor function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador ## Retorna o valor e continua o metodo, diferente de return que sai do metodo
        contador = + 1

    # OBS: Generetor function não é um generetor, ela gera o generetor.

gen = conta_ate(5)

print(type(gen))
print(next(gen)) #retorna o primeiro valor

