class Automovel:
    def __init__(self, placa):
        self.placa = placa

    def get_placa(self):
        return self.placa

    def set_placa(self, placa):
        self.placa = placa

    def dirigir(self, velocidade):
        print(f"Estou dirigindo a {velocidade} por Km/h")


meu_carro = Automovel('XXO0011')
outro_carro = Automovel('ZZZ0011')
print(meu_carro.get_placa())
meu_carro.dirigir(100)
print(outro_carro.get_placa())
outro_carro.dirigir(150)
