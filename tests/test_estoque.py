"""
Testes automatizados para o módulo MiniEstoque.

Valida cadastro, movimentações, duplicidade, valores inválidos, relatórios e histórico de produtos.
"""

import os
import pytest
from miniestoque.estoque import (
    cadastrar_produto,
    listar_produtos,
    registrar_entrada,
    registrar_saida,
    relatorio_estoque_baixo,
    historico_movimentacoes
)

@pytest.fixture(autouse=True)
def limpar_banco():
    """
    Remove o banco de dados antes de cada teste para garantir ambiente limpo.
    """
    DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'miniestoque', 'data', 'estoque.db')
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    yield

def test_cadastrar_e_listar_produtos():
    """
    Testa o cadastro e a listagem de produtos no estoque.
    """
    cadastrar_produto("TesteProduto", 10, 5.0)
    produtos = listar_produtos()
    assert len(produtos) == 1
    assert produtos[0][1] == "TesteProduto"

def test_entrada_saida():
    """
    Testa a entrada e saída de produtos no estoque.
    """
    cadastrar_produto("Produto1", 10, 5.0)
    produtos = listar_produtos()
    produto_id = produtos[0][0]

    registrar_entrada(produto_id, 5)
    produtos = listar_produtos()
    assert produtos[0][2] == 15  # quantidade após entrada

    registrar_saida(produto_id, 3)
    produtos = listar_produtos()
    assert produtos[0][2] == 12  # quantidade após saída

def test_saida_insuficiente():
    """
    Testa tentativa de saída com quantidade maior que o estoque disponível.
    """
    cadastrar_produto("Produto2", 5, 2.0)
    produtos = listar_produtos()
    produto_id = produtos[0][0]

    with pytest.raises(ValueError):
        registrar_saida(produto_id, 10)

def test_duplicidade_produto():
    """
    Testa cadastro de produto duplicado.
    """
    cadastrar_produto("Produto3", 5, 2.0)
    with pytest.raises(ValueError):
        cadastrar_produto("Produto3", 10, 3.0)

def test_valores_invalidos():
    """
    Testa cadastro e movimentação com valores inválidos.
    """
    with pytest.raises(ValueError):
        cadastrar_produto("Produto4", -1, 2.0)
    with pytest.raises(ValueError):
        cadastrar_produto("Produto5", 1, -5.0)
    cadastrar_produto("Produto6", 5, 2.0)
    produtos = listar_produtos()
    produto_id = produtos[-1][0]
    with pytest.raises(ValueError):
        registrar_entrada(produto_id, -3)
    with pytest.raises(ValueError):
        registrar_saida(produto_id, -2)

def test_relatorio_estoque_baixo():
    """
    Testa o relatório de produtos com estoque baixo.
    """
    cadastrar_produto("ProdutoBaixo1", 3, 2.0)
    cadastrar_produto("ProdutoAlto", 10, 5.0)
    produtos_baixo = relatorio_estoque_baixo(limite=5)
    nomes = [p[1] for p in produtos_baixo]
    assert "ProdutoBaixo1" in nomes
    assert "ProdutoAlto" not in nomes

def test_historico_movimentacoes():
    """
    Testa o histórico de movimentações de um produto.
    """
    cadastrar_produto("ProdutoHist", 5, 2.0)
    produtos = listar_produtos()
    produto_id = produtos[0][0]

    registrar_entrada(produto_id, 5)
    registrar_saida(produto_id, 3)

    historico = historico_movimentacoes(produto_id)
    assert historico[0][0] == "entrada"
    assert historico[0][1] == 5
    assert historico[1][0] == "saida"
    assert historico[1][1] == 3
    