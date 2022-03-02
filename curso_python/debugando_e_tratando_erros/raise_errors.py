"""
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma função, é uma palavra reservada, como def em python.

Rise é util para criar error exceptions e mensagens de erros.

Utilizando:

raise TipoDoErro('Mensagem do erro')

Raise assim como return finaliza a função!!
"""
#Exemplo
cores = {'verde', 'amarelo', 'azul', 'roxo'}

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser string')
    if cor not in cores:
        return ValueError(f'A cor precisa ser uma entre{cores}')
    print(f'O texto {texto} sera impresso na cor {cor}')
