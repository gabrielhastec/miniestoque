"""
Exemplo de uso avançado do MiniEstoque.

Inclui cadastro, consulta, vendas e relatórios financeiros do estoque.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from miniestoque.estoque import (
    cadastrar_produto,
    listar_produtos,
    registrar_venda,
    consultar_produto
)

# ---------- CADASTRO DE PRODUTOS ----------
print("=== Cadastro de produtos ===")
cadastrar_produto("Arroz", 10, 25.90)
cadastrar_produto("Feijão", 5, 9.80)
cadastrar_produto("Macarrão", 20, 7.50)
cadastrar_produto("Açúcar", 15, 4.20)
cadastrar_produto("Óleo", 12, 6.50)

# ---------- LISTAGEM DE TODOS OS PRODUTOS ----------
print("\n=== Produtos cadastrados ===")
produtos = listar_produtos()
for p in produtos:
    print(p)

# ---------- CONSULTA DE UM PRODUTO ESPECÍFICO ----------
produto_busca = "Feijão"
print(f"\n=== Consulta de produto: {produto_busca} ===")
resultado = consultar_produto(produto_busca)
print(resultado if resultado else f"Produto '{produto_busca}' não encontrado.")

# ---------- REGISTRO DE VENDAS ----------
print("\n=== Registrando vendas ===")
registrar_venda("Arroz", 2)
registrar_venda("Feijão", 1)
registrar_venda("Açúcar", 3)

# ---------- RELATÓRIO SIMPLES: ESTOQUE ATUALIZADO ----------
print("\n=== Estoque atualizado após vendas ===")
produtos = listar_produtos()
for p in produtos:
    print(p)

# ---------- RELATÓRIO: PRODUTOS COM ESTOQUE BAIXO (<=5) ----------
print("\n=== Produtos com estoque baixo (<=5) ===")
produtos_baixo_estoque = [p for p in produtos if p[1] <= 5]  # p[1] = quantidade
for p in produtos_baixo_estoque:
    print(p)

# ---------- RELATÓRIO: VALOR TOTAL DO ESTOQUE ----------
print("\n=== Valor total do estoque ===")
valor_total = sum(p[1] * p[2] for p in produtos)  # p[1] = quantidade, p[2] = preço
print(f"R$ {valor_total:.2f}")

# ---------- RELATÓRIO: VENDAS SIMULADAS POR PRODUTO (quantidade vendida * preço) ----------
print("\n=== Receita estimada de vendas registradas ===")
vendas = [
    ("Arroz", 2),
    ("Feijão", 1),
    ("Açúcar", 3)
]
for nome, qtd in vendas:
    produto = consultar_produto(nome)
    if produto:
        receita = qtd * produto[2]  # preço
        print(f"{nome}: {qtd} unidades vendidas → R$ {receita:.2f}")
