lista_idades = []
qtd = 0
soma = 0

while True:
    idade = int(input(f"Digite a {qtd+1}ª idade: "))
    if idade != -1:
        lista_idades.append(idade)
    else:
        break

tupla_idades = tuple(lista_idades)
qtd = len(tupla_idades)
soma = sum(tupla_idades)
media = (soma / qtd)

print(f"Foram informadas {qtd} idades.")
print(f"A média das idades é de {media} anos.")
