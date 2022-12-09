from random import randint as rd


class Automovel:
    def __init__(self, placa, velocidade_max,):
        self.__placa = placa
        self.__velocidade_max = velocidade_max
        self.__velocidade_atual = 0

    def __str__(self):
        return f'Velocidade atual: {self.__velocidade_atual} Km/h'

    def get_placa(self):
        return self.__placa

    def get_velocidade_max(self):
        return self.__velocidade_max

    def set_velocidade_max(self, nova):
        self.__velocidade_max = nova
        print(f"A nova velocidade máxima é {nova} Km/h")

    def dirigir(self):
        return f"Estou dirigindo a {self.__velocidade_atual} Km/h"

    def acelerar(self):
        velocidade = rd(0, rd(10, 20))
        maxima = self.__velocidade_max
        nova = self.__velocidade_atual + velocidade
        self.__velocidade_atual = nova if nova <= maxima else maxima

    def frear(self):
        velocidade = rd(0, rd(10, 20))
        nova = self.__velocidade_atual - velocidade
        self.__velocidade_atual = nova if nova >= 0 else 0


def main():

    meu_carro = Automovel('XZX1234', 200)

    for _ in range(20):
        meu_carro.acelerar()
        print(meu_carro.dirigir())

    for _ in range(20):
        meu_carro.frear()
        print(meu_carro.dirigir())

    print(f'PLACA: {meu_carro.get_placa()}')
    print(meu_carro)


meu_carro = Automovel('XYZ0022', 300)

print(meu_carro)
print(meu_carro.get_placa())
print(meu_carro.get_velocidade_max())

# Com Encapsulamento adequado:
meu_carro.set_velocidade_max(250)

print(meu_carro)
print(meu_carro.get_placa())
print(meu_carro.get_velocidade_max())

