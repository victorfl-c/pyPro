# DESAFIO!
from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=1000, salt_size=10)

    def __str__(self):
        return f'Nome completo: {self.__nome} {self.__sobrenome}\nE-mail: {self.__email}'


    def checar_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


while True:
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    conf_senha = input("Confirme a senha: ")
    if senha == conf_senha:
        aluno = Usuario(nome, sobrenome, email, senha)
        break
    else:
        print("As senhas não conferem!")

print("Usuário criado com sucesso!")
print("---------------------------\n")
senha = input("Informe a senha de acesso: ")
if aluno.checar_senha(senha):
    print("Acesso Permitido!")
    print(aluno)
else:
    print("Acesso Negado!")


