with open("frutas.txt", 'w') as arquivo:
    while True:
        fruta = input("Digite um texto")
        if fruta == 'sair':
            break
        else:
            arquivo.write(fruta)
            arquivo.write('\n')
