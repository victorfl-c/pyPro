class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def idenfificacao(self):
        return self.__cpf

    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, codigo):
        super().__init__(nome, sobrenome, cpf)
        self.__codigo = codigo

    def idenfificacao(self):
        return self.__codigo


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def identificacao(self):
        return self.__matricula


funcionario1 = Funcionario('Victor', 'Costa', '074.897.014-22', '01535662')
cliente1 = Cliente('Kennio', 'Herbert', '089.554.489-28', 3235556439)

print("-------------------------------")
print(f'Funcionário: {funcionario1.nome_completo()}')
print(f'Matrícula: {funcionario1.identificacao()}')
print("-------------------------------")
print(f'Cliente: {cliente1.nome_completo()}')
print(f'Código: R$: {cliente1.idenfificacao()}')
print("-------------------------------")
