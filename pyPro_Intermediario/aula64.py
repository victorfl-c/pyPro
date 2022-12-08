from random import (
    random,
    uniform,
    randint,
    choice,
    shuffle
)

'''Função random(Gera um número decimal
aleatório entre [0 e 1))'''
for i in range(1, 6):
    print(f"random([0, 1)): {random()}")
    if i == 5:
        print("\n")

'''Função uniform(Gera um número decimal
aleatório entre a e b)'''
for i in range(1, 6):
    print(f"uniform(a, b): {uniform(0, 100)}")
    if i == 5:
        print("\n")

'''Função randint(Gera um número inteiro
entre a e b)'''
for i in range(1, 6):
    print(f"randint(a, b): {randint(1, 61)}")
    if i == 5:
        print("\n")

'''Função Choice(Mostra um valor aleatório 
entre um interável)'''
escolha = ['pedra', 'papel', 'tesoura']
for i in range(1, 6):
    print(f"choice(i): {choice(escolha)}")
    if i == 5:
        print("\n")


'''Função shuffle(Embaralha a sequencia x)'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 6):
    print("lista[]: ", lista)
    shuffle(lista)
    print(f"shuffle(x [,random]): {lista}\n")
