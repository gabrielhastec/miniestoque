import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from miniestoque.estoque import cadastrar_produto, listar_produtos

# Limpar o banco de dados de teste (opcional)
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'miniestoque', 'data', 'estoque.db')
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

# Cadastro de exemplo
cadastrar_produto("Arroz", 10, 25.90)
cadastrar_produto("Feijão", 5, 9.80)

# Listagem
for p in listar_produtos():
    print(p)
