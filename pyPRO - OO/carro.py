class Carro:
    def __init__(self, modelo, ano):
        self.__modelo = modelo
        self.__ano = ano
        self.__odometro = 0

    def get_descricao(self):
        return self.__modelo + ' ' + str(self.__ano)

    def get_kilometragem(self):
        return f'Esse carro tem {self.__odometro} Km.'

    def set_odometro(self, km):
        self.__odometro = self.__odometro + km
