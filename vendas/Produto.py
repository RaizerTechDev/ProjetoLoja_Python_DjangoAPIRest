class Produto:

 def __init__(self, name, preco=30):
    self.name = name
    if preco > 30:
        self.preco = preco
    else:
        raise ValueError(
            " O Preço maior que trinta reais"
        )






