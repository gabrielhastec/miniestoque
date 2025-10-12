from datetime import date

from src.core.produto.domain.entities.produto import Produto
from src.core.produto.domain.exceptions.produto_exceptions import ProdutoNaoEncontradoError
from src.core.produto.domain.repositories.produto_repository_interface import ProdutoRepositoryInterface
from src.core.produto.domain.value_objects.nome import Nome
from src.core.produto.domain.value_objects.preco import Preco

class AtualizarProduto:
    """
    Use case para atualizar um Produto existente.

    Orquestra a atualização: valida inputs, recupera entidade, aplica mudanças e persiste via repositório.
    Mantém a camada de aplicação isolada do domínio e infraestrutura.

    Attributes:
        repository (ProdutoRepositoryInterface): Repositório para persistência.
    """

    def __init__(self, repository) -> None:
        self.repository = repository

    def execute(self, produto_id: int, nome: str = None, preco: float = None) -> Produto:
        """
        Executa a atualização do produto.

        Args:
            produto_id (int): ID do produto a ser atualizado.
            nome (str, optional): Novo nome do produto.
            preco (float, optional): Novo preço unitário.

        Returns:
            Produto: O produto atualizado e persistido.

        Raises:
            ProdutoNaoEncontradoError: Se o produto não for encontrado.
            ValueError: Para validações de domínio (ex.: nome inválido).
        """
        produto = self.repository.obter_por_id(produto_id)
        if not produto:
            raise ProdutoNaoEncontradoError(f"Produto com ID {produto_id} não encontrado.")

        # Aplica atualizações se fornecidas
        if nome:
            produto.nome = Nome(nome)
        if preco is not None:
            produto.preco = Preco(preco)

        self.repository.atualizar(produto)
        return produto
    
__all__ = ["AtualizarProduto"]
