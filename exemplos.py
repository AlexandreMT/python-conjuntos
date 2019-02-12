#declarando um conjunto na linguagem Python
co = {1, 2, 3, 4, 5}
print('Conjunto 1: ', co)

# trabalhando a teoria dos conjuntos, união, interseção, diferença
co1 = {1, 2, 3, 4, 5}
co2 = {4, 5, 6, 7}

# pertinência
print('Pertinência: ', 3 in co1)

# união entre os conjuntos co1 e co2 na linguagem python
print('União de co1 e co2: ', co1.union(co2))

# interseção entre os conjuntos co1 e co2
print('Interseção de co1 e co2: ', co1.intersection(co2))

# diferença simétrica
print('Diferença simétrica: ', co1.symmetric_difference(co2))

# diferença entre o conjunto co1 e co2
print('Diferença de co1 e co2', co1.difference(co2))

# verificando se um conjunto é um subconjunto de outro de outro conjunto
co3 = {1, 2}

# Verificando se o conjunto co3 é subconjunto do conjunto co1
print('Verificando se co3 é subconjunto de co1: ', co3.issubset(co1))

# Verificando se um conjunto é superconjunto de outro conjunto
print('Verificando se um conjunto é superconjunto de outro: ', co1.issuperset(co3))

# verificando se dois conjuntos são disjuntos
a = {10, 11}
b = {12, 13}
print('Verificando se dois conjuntos são disjuntos: ', a.isdisjoint(b))

####
lista = [1, 2, 3, 4, 5, 6]
conjunto = set(lista) # a função set() seta um conjunto com determinados valores
