num = int(input("Informe um número: "))
fatorial = 1

if num < 0:
    print("Não é possível fatorar o número zero!")
elif num == 0:
    print("O fatorial de 0 é igual a 1")
else:
    for i in range(1, num+1):
        fatorial = fatorial*i
    print("O fatorial de", num,"é: ", fatorial)