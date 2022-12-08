import os

'''
Verificar se as pastas ou arquivos existem:

print(os.path.exists("frutas.txt"))
print(os.path.exists("teste.py"))
print(os.path.exists("existe"))
'''
# Criar arquivo:
os.mknod('arquivo4.txt')

with open("arquivo4.txt", 'w') as arquivo:
    pass  # existe o bloco, mas nada será executado

# Criar diretório:
'''os.mkdir('pypro')'''

# Criar arvore de diretórios:
'''os.makedirs('pypro/fundamentos')'''

# Renomear um arquivo existente:
'''os.rename('arquivo1.txt', 'arquivox.txt')'''

# Renomear um diretório existente:
'''os.rename('pypro', 'python')'''

# Deletar arquivo FISICAMENTE(Não vai para lixeira)
'''os.remove('arquivo1.txt')'''

# Deletar diretório FISICAMENTE(Não vai para lixeira)
'''os.rmdir('pypro')'''
