from miniestoque.core.entities.produto import Produto
from miniestoque.infrastructure.repositories.produto_repository import ProdutoRepository

class EstoqueService:
    def __init__(self):
        ProdutoRepository.criar_tabela()

    def cadastrar_produto(self, nome: str, quantidade: int, preco: float):
        produto = Produto(nome, quantidade, preco)
        ProdutoRepository.salvar(produto)

    def listar_produtos(self):
        return ProdutoRepository.listar()
