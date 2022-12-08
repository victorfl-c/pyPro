#Utilizando Dict comprehension
dicio = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
quadrado = {chave: valor**2 for chave, valor in dicio.items()}
print(dicio)
print(quadrado)
