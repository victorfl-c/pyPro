nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#Retorna o valor quando a condição não é inteira (x % 2 == 1)
lista = [x**2 for x in nums if x % 2]
print(nums)
print(lista)
#Retorna os números pares divididos por 2
lista = [x/2 for x in nums if not x % 2]
print(nums)
print(lista)

#Retorna uma lista com a primeira letra em maiúscula
amigos = ['ana', 'marcela', 'fernando', 'pedro', 'roberto']
lista = [amigo.title() for amigo in amigos]
print(amigos)
print(lista)
