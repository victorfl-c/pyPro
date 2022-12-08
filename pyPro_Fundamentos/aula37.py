#Implemente um algoritmo que leia cinco idades e imprima a média delas

#Iniciar a variável soma
soma = 0
#Repetir de 1 até 5(n-1), cinco valores de idades
for i in range(1, 6):
    #Ler idade
    idade = int(input(f"Informe a {i}ª idade: "))
    #somar idades
    soma = soma + idade
#Dividir a soma pelo número de idades
media = soma/5
#Imprimir a média de idade
print("A média de idades é de", media, "Anos")