from .database import get_connection, create_tables

# Inicializa o banco na primeira vez
create_tables()

def cadastrar_produto(nome, quantidade, preco):
    if quantidade < 0 or preco < 0:
        raise ValueError("Quantidade e preço devem ser maiores ou iguais a zero.")
    
    conn = get_connection()
    cursor = conn.cursor()
    
    # Verifica se o produto já existe
    cursor.execute("SELECT id FROM produtos WHERE nome = ?", (nome,))
    if cursor.fetchone():
        conn.close()
        raise ValueError(f"Produto '{nome}' já cadastrado.")
    
    cursor.execute(
        "INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
        (nome, quantidade, preco)
    )
    conn.commit()
    conn.close()

def listar_produtos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, quantidade, preco FROM produtos")
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def registrar_entrada(produto_id, quantidade):
    if quantidade <= 0:
        raise ValueError("Quantidade deve ser maior que zero.")
    
    conn = get_connection()
    cursor = conn.cursor()
    
    # Atualiza estoque
    cursor.execute("UPDATE produtos SET quantidade = quantidade + ? WHERE id = ?", (quantidade, produto_id))
    
    # Registra movimentação
    cursor.execute(
        "INSERT INTO movimentacoes (produto_id, tipo, quantidade) VALUES (?, 'entrada', ?)",
        (produto_id, quantidade)
    )
    
    conn.commit()
    conn.close()

def registrar_saida(produto_id, quantidade):
    if quantidade <= 0:
        raise ValueError("Quantidade deve ser maior que zero.")
    
    conn = get_connection()
    cursor = conn.cursor()
    
    # Verifica estoque disponível
    cursor.execute("SELECT quantidade FROM produtos WHERE id = ?", (produto_id,))
    result = cursor.fetchone()
    if not result:
        conn.close()
        raise ValueError("Produto não encontrado.")
    
    estoque_atual = result[0]
    if quantidade > estoque_atual:
        conn.close()
        raise ValueError("Estoque insuficiente.")
    
    # Atualiza estoque
    cursor.execute("UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?", (quantidade, produto_id))
    
    # Registra movimentação
    cursor.execute(
        "INSERT INTO movimentacoes (produto_id, tipo, quantidade) VALUES (?, 'saida', ?)",
        (produto_id, quantidade)
    )
    
    conn.commit()
    conn.close()

def relatorio_estoque_baixo(limite=5):
    """
    Retorna produtos com quantidade menor ou igual ao limite.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, nome, quantidade, preco FROM produtos WHERE quantidade <= ?",
        (limite,)
    )
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def historico_movimentacoes(produto_id):
    """
    Retorna o histórico de movimentações de um produto.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT tipo, quantidade, data FROM movimentacoes WHERE produto_id = ? ORDER BY data",
        (produto_id,)
    )
    movimentacoes = cursor.fetchall()
    conn.close()
    return movimentacoes
