import sqlite3
from miniestoque.core.entities.produto import Produto
from miniestoque.infrastructure.database.database import get_connection

class ProdutoRepository:
    @staticmethod
    def criar_tabela():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                preco REAL NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    @staticmethod
    def salvar(produto: Produto):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
            (produto.nome, produto.quantidade, produto.preco),
        )
        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT nome, quantidade, preco FROM produtos")
        rows = cursor.fetchall()
        conn.close()
        return [Produto(nome, qtd, preco) for nome, qtd, preco in rows]
