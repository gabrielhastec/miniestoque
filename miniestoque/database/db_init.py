import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "estoque.db")

class Database:
    _conn = None
    _cursor = None

    @classmethod
    def init_db(cls):
        """Inicializa o banco e cria todas as tabelas."""
        if cls._conn is None:
            cls._conn = sqlite3.connect(DB_PATH)
            cls._cursor = cls._conn.cursor()

        # Tabela produtos
        cls._cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
        """)

        # Tabela movimentações
        cls._cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimentacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            tipo TEXT NOT NULL CHECK(tipo IN ('entrada', 'saida')),
            quantidade INTEGER NOT NULL,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(produto_id) REFERENCES produtos(id)
        )
        """)

        cls._conn.commit()

    @classmethod
    def get_cursor(cls):
        if cls._conn is None or cls._cursor is None:
            cls.init_db()
        return cls._cursor

    @classmethod
    def commit(cls):
        if cls._conn:
            cls._conn.commit()

    @classmethod
    def close(cls):
        if cls._conn:
            cls._conn.close()
            cls._conn = None
            cls._cursor = None
