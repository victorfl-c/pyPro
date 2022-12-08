soma = 0
num = 0

num = int(input("Informe um número: "))

while num != 0:
    resto = num % 10
    soma += resto
    num = int(num/10)
print(f"A soma dos números é :{soma}")
