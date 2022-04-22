"""
    Alocação e Gerenciamento de Memoria

    Variavel declarada -> valor armazenado na memoria
    -> Caso declarado que variavel x = y, a variavel x ira
    apontar para o mesmo lugar na memoria, referenciando o
    mesmo objeto.
    -> caso seja de x = x+1 aponta para outro espaço na mem
    -> caso duas variaveis tenham o mesmo valor elas apontam
     para o mesmo espaço em memoria -> economiza espaço em memoria

    Memoria -> dividida em STACK que abriga o nome das variaveis/funções
    em frames. E memoria HEAP que guarda o valor, incluindo instancias e
    objetos

    Esta alocação se define por uma tabela com numero de referencias,
    cada valor/instancia/objeto possui uma quantidade de referencias.
    -> Caso o valor nao possua nenhuma referencia ele consta como
      DEAD OBJECT (0 referencias)
    -> Que são removidos pelo Garbage Collector, utilizando o algoritmo
    de Reference Couting.

"""