import os

print(os.getcwd())
#sobe um nível no diretório
os.chdir('..')
print(os.getcwd())
os.chdir('/home/victorfl-c/PycharmProjects/pythonProject/intermediario')
print(os.getcwd())
print(os.path.isabs('/home/victorfl-c/PycharmProjects/pythonProject/intermediario'))
print(os.name)