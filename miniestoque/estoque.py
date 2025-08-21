
from .database import get_connection, create_tables

# Inicializa o banco na primeira vez
create_tables()

def cadastrar_produto(nome, quantidade, preco):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
                   (nome, quantidade, preco))
    conn.commit()
    conn.close()

def listar_produtos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, quantidade, preco FROM produtos")
    produtos = cursor.fetchall()
    conn.close()
    return produtos
