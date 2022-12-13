# Métodos Mágicos

class Livro:
    def __init__(self, titulo, autor, editora, ano, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__editora = editora
        self.__ano = ano
        self.__paginas = paginas

    def __repr__(self):
        return f'{self.__titulo} - {self.__autor}'


livro1 = Livro(
    'Algorítimos e Programação de computadores',
    'Piva Jr, et al',
    'Elsevier',
    2019,
    588
)

livro2 = Livro(
    'Estrutura de Dados e Técnicas de Programação',
    'Piva Jr, et al',
    'Elsevier',
    2014,
    399
)

print(livro1)
print(livro2)
