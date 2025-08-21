import os
import pytest
from miniestoque.estoque import cadastrar_produto, listar_produtos

# Apaga o banco antes de cada teste
@pytest.fixture(autouse=True)
def limpar_banco():
    DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'miniestoque', 'data', 'estoque.db')
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    yield

def test_cadastrar_e_listar_produtos():
    cadastrar_produto("TesteProduto", 10, 5.0)
    produtos = listar_produtos()
    assert len(produtos) == 1
    assert produtos[0][1] == "TesteProduto"
