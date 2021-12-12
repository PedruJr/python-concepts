"""

Operadores unários:
    not, is
Operadores binarios:
    and, or

    and = ambos precisam ser validos
    or = um ou outro pode estar valido
    not = ! diferente se não for true
    is = comparado a outro valor

"""
ativo = True
logado = False

if ativo and logado:
    print('Bem vindo usuario!')
else:
    print('Favor confirmar o email')

if not ativo:
    print('Você precisa ativar sua conta')
else:
    print('Bem vindo')

