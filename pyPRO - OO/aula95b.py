class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome

    def get_cpf(self):
        return self.__cpf


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

    def get_renda(self):
        return self.__renda


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def get_matricula(self):
        return self.__matricula


funcionario1 = Funcionario('Victor', 'Costa', '074.897.014-22', '01535662')
cliente1 = Cliente('Kennio', 'Herbert', '089.554.489-28', 3600)

print("-------------------------------")
print(f'Funcionário: {funcionario1.nome_completo()}')
print(f'Nome: {funcionario1.get_nome()}')
print(f'CPF: {funcionario1.get_cpf()}')
print(f'Matrícula: {funcionario1.get_matricula()}')
print("-------------------------------")
print(f'Cliente: {cliente1.nome_completo()}')
print(f'Nome: {cliente1.get_nome()}')
print(f'CPF: {cliente1.get_cpf()}')
print(f'Renda: R$: {float(cliente1.get_renda())}')
print("-------------------------------")


