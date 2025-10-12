from typing import Optional

from src.core.estoque.domain.entities.estoque import Estoque
from src.core.estoque.domain.exceptions.estoque_exceptions import (
    EstoqueNaoEncontradoError,
    QuantidadeInvalidaError,
)
from src.core.estoque.domain.repositories.estoque_repository_interface import EstoqueRepositoryInterface
from src.core.estoque.domain.value_objects.quantidade import Quantidade
from src.core.produto.domain.repositories.produto_repository_interface import ProdutoRepositoryInterface


class AdicionarProdutoAoEstoque:
    """
    Use case para adicionar um produto a um estoque existente.

    Orquestra a validação, adição via lógica de domínio e persistência.
    Dependências: repositórios de Estoque e Produto para verificações cruzadas.

    Attributes:
        estoque_repository (EstoqueRepositoryInterface): Repositório para estoque.
        produto_repository (ProdutoRepositoryInterface): Repositório para validar produto.
    """

    def __init__(
        self,
        estoque_repository: EstoqueRepositoryInterface,
        produto_repository: ProdutoRepositoryInterface,
    ) -> None:
        self.estoque_repository = estoque_repository
        self.produto_repository = produto_repository

    def execute(self, estoque_id: int, produto_id: int, quantidade: int) -> Estoque:
        """
        Executa a adição de um produto ao estoque.

        Valida existência de estoque e produto, cria value object de quantidade,
        e chama método de domínio para adicionar.

        Args:
            estoque_id (int): ID do estoque alvo.
            produto_id (int): ID do produto a adicionar.
            quantidade (int): Quantidade a adicionar (deve ser positiva).

        Returns:
            Estoque: O estoque atualizado e persistido.

        Raises:
            EstoqueNaoEncontradoError: Se o estoque não existir.
            ValueError: Se o produto não existir ou quantidade inválida.
            QuantidadeInvalidaError: Para quantidade negativa ou zero.
        """
        estoque = self.estoque_repository.get_by_id(estoque_id)
        if not estoque:
            raise EstoqueNaoEncontradoError(f"Estoque com ID {estoque_id} não encontrado.")

        # Verifica se o produto existe
        produto = self.produto_repository.get_by_id(produto_id)
        if not produto:
            raise ValueError(f"Produto com ID {produto_id} não encontrado.")

        # Cria Value Object de Quantidade com validação
        try:
            qtd_vo = Quantidade(quantidade)
        except ValueError as e:
            raise QuantidadeInvalidaError(str(e))

        # Chama método de domínio para adicionar o produto
        estoque.adicionar_produto(produto_id, qtd_vo)
        return self.estoque_repository.save(estoque)
