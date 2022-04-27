import pytest

from vendas.Categoria import Categoria
from vendas.Produto import Produto

def soma_1(numero):
    return int ( numero ) + 1


def test_soma_1():
    assert soma_1 ( 41 ) == 42


def test_soma_1_numero_como_string():
    assert soma_1 ( "41" ) == 42


def test_soma_1_palavra():
    with pytest.raises ( ValueError ):
        soma_1 ( "rafael" )


def test_categoria_palavra():
         Categoria("Masculino")



def test_preco_maior_que_trinta():
   Produtos = Produto("Tasks Study", 31)
   assert Produtos.preco == 31

