#FORMA PYTHONICA DE TRABALHAR COM ARQUIVOS

with open("texto.txt", 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())

print(arquivo.closed)
