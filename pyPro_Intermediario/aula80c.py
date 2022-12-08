import os
#Ler todos os diretorios no ambiemte para o variavel diretorio
diretorio = os.listdir()
#Imprimir todos os diretorios, linha por linha
for i in range(0, len(diretorio)):
    print(diretorio[i])

#Imprimir todas as informações de todos os diretórios
diretorio = list(os.scandir())
for i in range(0, len(diretorio)):
    print('---------------------')
    print('>', diretorio[i].name)
    print(diretorio[i].inode())
    print(diretorio[i].is_dir())
    print(diretorio[i].is_file())
    print(diretorio[i].is_symlink())
    print(diretorio[i].path)
    print(diretorio[i].stat)
    print(diretorio[i].stat().st_size)
