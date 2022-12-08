def ler_sobrenome():
    while True:
        sobrenome = input("Informe o sobrenome: ")
        if sobrenome:
            if sobrenome.isalpha():
                return sobrenome
            else:
                print("Informe um sobrenome válido!")
        else:
            return sobrenome


def ler_idade():
    while True:
        try:
            idade = int(input("Informe a idade: "))
        except:
            print("Informe uma idade válida!")
        else:
            if idade:
                return idade
            else:
                print("Informe uma idade válida!")


def ler_altura():
    while True:
        try:
            altura = int(input("Informe a altura(em centímetros): "))
        except:
            print("Informe uma idade válida!")
        else:
            if altura:
                return altura
            else:
                print("Informe uma altura válida!")


def ler_peso():
    while True:
        try:
            peso = float(input("Informe o peso: "))
        except:
            print("Informe um peso válido!")
        else:
            if peso:
                return peso

            else:
                print("Informe um peso válido!")


pessoas = []
n = 0

while True:
    sobrenome = ler_sobrenome()
    if sobrenome:
        n += 1
        idade = ler_idade()
        altura = ler_altura()
        peso = ler_peso()
        pessoa = [sobrenome, idade, altura, peso]
        pessoas.append(pessoa)
    else:
        break


soma_idade = 0
soma_altura = 0
soma_peso = 0
if n > 0:
    #Existe 1 ou mais pessoas cadastradas
    pessoas.sort()
    print("Relação de nomes cadastrados...")
    print("-------------------------------")
    for i in range(0, len(pessoas)):
        print(f"{pessoas[i][0]} - {pessoas[i][1]} - {pessoas[i][2]} - {pessoas[i][3]}")
        soma_idade += pessoas[i][1]
        soma_altura += pessoas[i][2]
        soma_peso += pessoas[i][3]
    print("-------------------------------")
    media_idade = soma_idade/n
    media_altura = soma_altura/n
    media_peso = soma_peso/n
    print(f"Idade média: {media_idade}")
    print(f"Altura média: {media_altura}")
    print(f"Peso médio: {media_peso}")
    print("-------------------------------")