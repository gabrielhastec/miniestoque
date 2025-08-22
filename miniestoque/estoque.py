"""
Módulo principal do MiniEstoque.

Fornece funções para cadastro, listagem, movimentação e relatórios de produtos no estoque.
"""

from .database import get_connection, create_tables

# Inicializa o banco na primeira vez
create_tables()

def cadastrar_produto(nome, quantidade, preco):
    """
    Cadastra um novo produto no estoque.

    Args:
        nome (str): Nome do produto.
        quantidade (int): Quantidade inicial em estoque (>= 0).
        preco (float): Preço unitário do produto (>= 0).

    Raises:
        ValueError: Se quantidade ou preço forem negativos, ou se o produto já existir.
    """
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
    """
    Retorna a lista de produtos cadastrados no estoque.

    Returns:
        list: Lista de tuplas (id, nome, quantidade, preco) dos produtos.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, quantidade, preco FROM produtos")
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def registrar_entrada(produto_id, quantidade):
    """
    Adiciona unidades ao estoque de um produto e registra a movimentação.

    Args:
        produto_id (int): ID do produto.
        quantidade (int): Quantidade a adicionar (> 0).

    Raises:
        ValueError: Se quantidade for menor ou igual a zero.
    """
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
    """
    Remove unidades do estoque de um produto e registra a movimentação.

    Args:
        produto_id (int): ID do produto.
        quantidade (int): Quantidade a remover (> 0).

    Raises:
        ValueError: Se quantidade for menor ou igual a zero, produto não existir ou estoque insuficiente.
    """
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

    Args:
        limite (int): Quantidade máxima para considerar estoque baixo.

    Returns:
        list: Lista de tuplas (id, nome, quantidade, preco) dos produtos com estoque baixo.
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

    Args:
        produto_id (int): ID do produto.

    Returns:
        list: Lista de tuplas (tipo, quantidade, data) das movimentações do produto.
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
