#Listas aninhadas (matrizes)
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for lista in listas:
    for num in lista:
        print(num)

print('----------------------------------')
#List comprehension
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[print(num) for num in lista] for lista in listas]

print('----------------------------------')
#Gerando uma matriz com list comprehension
matriz = [[num for num in range(1, 4)] for lista in range(1, 4)]
print(matriz)
