idade =0
soma = 0
qtd = 0

while idade != 100:
    idade = int(input(f"Informe a {qtd+1}ª idade: "))
    if idade != 100:
        soma += idade
        qtd += 1

if qtd == 0:
    print("Não foi digitada nenhuma idade!")
else:
    media = soma / qtd
    print(f"A média das {qtd} idades é de: ")