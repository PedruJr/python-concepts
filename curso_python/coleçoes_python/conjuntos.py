"""
Conjuntos

- Conjuntos nas linguagens de programação se refere a teoria dos conjuntos
em matematica.

- sets (conjuntos nao possuem valores duplicados)
- sets (não possuem valores ordenados)
- elementos nos sets não são indexados

Conjuntos são bons para quando precisamos armazenar elementos,
mas não nos importamos com a ordenação deles, ou com chavez, valores
e itens duplicados

os conjuntos sets são referenciados por {} como os dicionarios/mapa
- diferença entre dicionario e um set/conjunto
    - dicionario tem chave e valor
    - conjunto tem apenas valor
"""
#definindo um conjunto:

#forma 1 com metodo set
#valores repetidos são ignorados sem gerar erro

s = set({ 1, 2, 3, 4, 5, 6, 9, 9, 2, 3})

print(s)

