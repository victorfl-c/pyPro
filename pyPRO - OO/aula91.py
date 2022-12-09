from random import randint as rd
class Automovel:
    def __init__(self, placa, velocidade_max,):
        self.placa = placa
        self.velocidade_max = velocidade_max
        self.velocidade_atual = 0

    def __str__(self):
        return f'Velocidade atual: {self.velocidade_atual} Km/h'

    def get_placa(self):
        return self.placa

    def dirigir(self):
        return f"Estou dirigindo a {self.velocidade_atual} Km/h"

    def acelerar(self):
        velocidade = rd(0, rd(10, 20))
        maxima = self.velocidade_max
        nova = self.velocidade_atual + velocidade
        self.velocidade_atual = nova if nova <= maxima else maxima

    def frear(self):
        velocidade = rd(0, rd(10, 20))
        nova = self.velocidade_atual - velocidade
        self.velocidade_atual = nova if nova >= 0 else 0


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

main()
