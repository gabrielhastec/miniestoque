"""
Módulo de acesso ao banco de dados SQLite para o MiniEstoque.

Responsável por criar as tabelas e fornecer conexão ao banco.
"""

import sqlite3
import os

# Caminho do banco dentro da pasta data
DB_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DB_DIR, exist_ok=True)  # Cria a pasta se não existir
DB_PATH = os.path.join(DB_DIR, "estoque.db")

def get_connection():
    """
    Retorna uma conexão SQLite para o banco de dados do estoque.

    Returns:
        sqlite3.Connection: Conexão ativa com o banco de dados.
    """
    return sqlite3.connect(DB_PATH)

def create_tables():
    """
    Cria as tabelas 'produtos' e 'movimentacoes' no banco de dados, caso não existam.

    Executa comandos SQL para garantir que as tabelas necessárias estejam presentes.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL DEFAULT 0,
        preco REAL NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movimentacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto_id INTEGER,
        tipo TEXT CHECK(tipo IN ('entrada','saida')),
        quantidade INTEGER NOT NULL,
        data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(produto_id) REFERENCES produtos(id)
    )
    """)

    conn.commit()
    conn.close()