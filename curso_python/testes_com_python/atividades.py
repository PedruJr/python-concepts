"""
    Complemento do Modulo UnitTest

"""

def comer(comida,e_saudavel):
    if e_saudavel:
       final = 'quero manter a forma.'
    else:
        final = 'a gente so vive uma vez.'

    return f'Estou comendo {comida} porque {final}'


def dormir(horas):
    if horas >= 8:
        return f'Ptz! Dormi muito! Estou atrasado para o trabalho!'
    else:
        return f'Continuo cansado apos dormir por {horas} horas..'
