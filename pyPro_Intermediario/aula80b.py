import os.path

#criando uma pasta dentro do diretorio
pasta = os.path.join(os.getcwd(), 'teste')
os.mkdir(pasta)
os.chdir(pasta)
print(pasta)