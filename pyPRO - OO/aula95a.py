# Herança
class Mamifero:
    def __init__(self, pelo, mamas, idade):
        self.__pelo = pelo
        self.__mamas = mamas
        self.__idade = idade

    def comuninar(self):
        pass

class Cachorro(Mamifero):
    def __init__(self, pelo, mamas, idade, rabo):
        super.__init__(pelo, mamas, idade)
        self.__rabo = rabo

    def latir(self):
        pass

class gato(Mamifero):
    def __init__(self, pelo ,mamas, idade, rabo):
        super.__init__(pelo, mamas, idade)

    def miar(self):
        pass
