from io import StringIO

frutas = ""
arquivo = StringIO(frutas)

while True:
    fruta = input("Digite uma fruta: ")
    if fruta == 'sair':
        break
    else:
        arquivo.write(fruta)
        arquivo.write('\n')

