from src.core.estoque.domain.entities.estoque import Estoque
from src.core.estoque.domain.exceptions.estoque_exceptions import (
    EstoqueNaoEncontradoError,
    ProdutoNaoNoEstoqueError,
)
from src.core.estoque.domain.repositories.estoque_repository_interface import EstoqueRepositoryInterface

class RemoverProdutoDoEstoque:
    """
    Use case para remover um produto de um estoque.

    Valida presença e remove via lógica de domínio, persistindo mudanças.

    Attributes:
        repository (EstoqueRepositoryInterface): Repositório para persistência.
    """

    def __init__(self, repository: EstoqueRepositoryInterface) -> None:
        self.repository = repository

    def execute(self, estoque_id: int, produto_id: int) -> Estoque:
        """
        Executa a remoção de um produto do estoque.

        Args:
            estoque_id (int): ID do estoque.
            produto_id (int): ID do produto a remover.

        Returns:
            Estoque: O estoque atualizado sem o produto.

        Raises:
            EstoqueNaoEncontradoError: Se o estoque não existir.
            ProdutoNaoNoEstoqueError: Se o produto não estiver no estoque.
        """
        # Busca o estoque pelo ID
        estoque = self.repository.get_by_id(estoque_id)
        if not estoque:
            raise EstoqueNaoEncontradoError(f"Estoque com ID {estoque_id} não encontrado.")

        # Verifica se o produto está no estoque
        if produto_id not in estoque.produtos:
            raise ProdutoNaoNoEstoqueError(f"Produto {produto_id} não está no estoque {estoque_id}.")

        # Remove o produto e persiste a mudança
        estoque.remover_produto(produto_id)
        return self.repository.save(estoque)
    