soma = 0
qtd = 0
num = 0

while num != -1:
    num = int(input(f"Informe o {qtd+1} número: "))
    if num != -1:
        soma += num
        qtd += 1

if qtd == 0:
    print("Não foi informado nenhum número!")
else:
    media = soma / qtd
    print(f"A média dos {qtd} numeros é: {media}")
