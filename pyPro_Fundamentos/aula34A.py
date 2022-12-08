#ler um numero inteiro maior que zero, e verificar se é par ou impar

#ler o valor do numero
num = int(input("Informe um número: "))
#verificar se valor é maior que zero
if num > 0:
    #verificar se o valor é par
    if num % 2 == 0:
        print("O numero", num, "é par!")
    #verificar se o valor é impar
    else:
        print("O numero", num, "é impar!")
else:
    print("Informe um valor maior que zero!")
