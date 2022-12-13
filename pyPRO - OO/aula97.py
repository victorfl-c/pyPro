# Herança Múltipla
class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def cumprimentar(self):
        return f'Olá, me chamo {self.__nome}!'


class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{super().get_nome()} Andando...'

    def cumprimentar(self):
        return f'Olá, sou {super().get_nome()}! (=_=)'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{super().get_nome()} Nadando...'

    def cumprimentar(self):
        return f'Olá, sou {super().get_nome()}!(-_-)'


class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)


pinguim1 = Pinguim('Ignácio')
print(pinguim1.nadar())
print(pinguim1.andar())
print(pinguim1.cumprimentar())

jabuti = Terrestre('Jabutizinho')
print(jabuti.andar())
print(jabuti.cumprimentar())

golfinho = Aquatico('Willy')
print(golfinho.nadar())
print(golfinho.cumprimentar())
