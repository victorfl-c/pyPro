pessoas = []

for i in range(1, 6):
    print(f"{i}ª Pessoa: ")
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    calcado = int(input("Informe o tamanho do calçado: "))
    print("---------------------------------------------")
    pessoa = [nome, idade, calcado]
    pessoas.append(pessoa)

nova_lista = sorted(pessoas)
total_idades = 0
total_calcados = 0

for i in range(0, 5):
    total_idades += nova_lista[i][1]
    total_calcados += nova_lista[i][2]
    print(f"Nome:{nova_lista[i][0]}|idade:{nova_lista[i][1]}|calçado:{nova_lista[i][2]}")

print("------------------------------------------")
print(f"A média de idade é {total_idades/5} anos.")
print(f"A média de tamanho dos calçados é {int(total_calcados/5)}")