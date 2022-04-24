"""
    GIL - Global Interpreter Locker
    É um mutex(lock) que permite apenas uam thread use o interpretador
    python,

    sys.getrefcount(a) -> metodo que apresenta a quantidade de referencias
    da variavel

    -> Este tipo de gerenciamento causa um problema chamado race conditions
    -> Podemos evitar este tipo de problema atravez de locks, que seguram o uso
    apenas para o objeto apontando.
    -> Porem este tipo de solução acarreta em outro problema que são
    os deadlocks, vulgo locks que nunca finalizam e que não são liberados
    -> Isso causa decaimento da performance em abrir e fechar locks
    -> GIl aplica o single lock, evitando o dead lock, porem transformando
    python em uma linguagem single tread.
    -> Para todo processo teremos um ambiente python proprio.
    -> Multi-processing sao mais pesados que multi-threading

"""
import time
from threading import Thread

CONTADOR = 5000

def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')