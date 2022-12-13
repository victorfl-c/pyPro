# Métodos Mágicos

'''Métodos Mágicos são também conhecidos na documentação oficial
do Python como MÉTODOS ESPECIAIS(Special names, special sintax)'''

class Livro:
    def __init__(self, titulo, autor, editora, ano, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__editora = editora
        self.__ano = ano
        self.__paginas = paginas

    def __repr__(self):
        # Retorna a representação do elemento, caso o método __str__ não esteja definido
        return f'{self.__titulo} - {self.__autor}'

    def __str__(self):
        # Retorna os valores definidos no método, sobreescrevendo sua representação
        return f'{self.__ano} - {self.__titulo}'

    def __len__(self):
        # Redefine o método len() para receber um valor definido no objeto,
        # como por exemplo, o número de páginas de um livro'''
        return self.__paginas

    def __add__(self, other):
        # Realiza a operação de adição/concatenação entre dois elementos.
        return self.__paginas + other.get_paginas()

    def __del__(self):
        # Ação que é realizada quando deletamos um objeto da memória
        # Python faz o garbage collection automáticamente
        print("Um bojeto da classe Livro foi deletado! ")

    def get_paginas(self):
        return self.__paginas


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
print(f"Páginas: {len(livro1)}")
print(livro2)
print(f"Páginas: {len(livro2)}")
print(f'Soma das páginas: {livro1 + livro2}')
