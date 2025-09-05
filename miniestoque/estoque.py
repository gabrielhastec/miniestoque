from .database.db_init import Database

# Inicializa o banco na primeira vez
Database.init_db()

def cadastrar_produto(nome, quantidade, preco):
    if quantidade < 0 or preco < 0:
        raise ValueError("Quantidade e preço devem ser maiores ou iguais a zero.")

    cursor = Database.get_cursor()

    # Verifica se o produto já existe
    cursor.execute("SELECT id FROM produtos WHERE nome = ?", (nome,))
    if cursor.fetchone():
        raise ValueError(f"Produto '{nome}' já cadastrado.")

    # Insere produto
    cursor.execute(
        "INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)",
        (nome, quantidade, preco)
    )
    Database.commit()

def listar_produtos():
    cursor = Database.get_cursor()
    cursor.execute("SELECT id, nome, quantidade, preco FROM produtos")
    return cursor.fetchall()

def registrar_entrada(produto_id, quantidade):
    if quantidade <= 0:
        raise ValueError("Quantidade deve ser maior que zero.")

    cursor = Database.get_cursor()

    # Atualiza estoque
    cursor.execute("UPDATE produtos SET quantidade = quantidade + ? WHERE id = ?", (quantidade, produto_id))

    # Registra movimentação
    cursor.execute(
        "INSERT INTO movimentacoes (produto_id, tipo, quantidade) VALUES (?, 'entrada', ?)",
        (produto_id, quantidade)
    )

    Database.commit()

def registrar_saida(produto_id, quantidade):
    if quantidade <= 0:
        raise ValueError("Quantidade deve ser maior que zero.")

    cursor = Database.get_cursor()

    # Verifica estoque disponível
    cursor.execute("SELECT quantidade FROM produtos WHERE id = ?", (produto_id,))
    result = cursor.fetchone()
    if not result:
        raise ValueError("Produto não encontrado.")

    estoque_atual = result[0]
    if quantidade > estoque_atual:
        raise ValueError("Estoque insuficiente.")

    # Atualiza estoque
    cursor.execute("UPDATE produtos SET quantidade = quantidade - ? WHERE id = ?", (quantidade, produto_id))

    # Registra movimentação
    cursor.execute(
        "INSERT INTO movimentacoes (produto_id, tipo, quantidade) VALUES (?, 'saida', ?)",
        (produto_id, quantidade)
    )

    Database.commit()

def relatorio_estoque_baixo(limite=5):
    cursor = Database.get_cursor()
    cursor.execute(
        "SELECT id, nome, quantidade, preco FROM produtos WHERE quantidade <= ?",
        (limite,)
    )
    return cursor.fetchall()

def historico_movimentacoes(produto_id):
    cursor = Database.get_cursor()
    cursor.execute(
        "SELECT tipo, quantidade, data FROM movimentacoes WHERE produto_id = ? ORDER BY data",
        (produto_id,)
    )
    return cursor.fetchall()
