from typing import Optional

from src.core.estoque.domain.entities.estoque import Estoque
from src.core.estoque.domain.exceptions.estoque_exceptions import EstoqueNaoEncontradoError
from src.core.estoque.domain.repositories.estoque_repository_interface import EstoqueRepositoryInterface
from src.core.estoque.domain.value_objects.quantidade import Quantidade

class AtualizarEstoque:
    """
    Use case para atualizar a quantidade de um produto em um estoque.

    Permite incrementos ou decrementos, orquestrando validações e persistência.

    Attributes:
        repository (EstoqueRepositoryInterface): Repositório para persistência.
    """

    def __init__(self, repository: EstoqueRepositoryInterface) -> None:
        self.repository = repository

    def execute(self, estoque_id: int, produto_id: int, nova_quantidade: Optional[int] = None, delta: Optional[int] = None) -> Estoque:
        """
        Executa a atualização do estoque para um produto específico.

        Suporta definição direta de quantidade ou aplicação de delta (positivo/negativo).

        Args:
            estoque_id (int): ID do estoque.
            produto_id (int): ID do produto no estoque.
            nova_quantidade (Optional[int]): Nova quantidade absoluta (se fornecida).
            delta (Optional[int]): Variação a aplicar (se fornecida).

        Returns:
            Estoque: O estoque atualizado.

        Raises:
            EstoqueNaoEncontradoError: Se o estoque não existir.
            ValueError: Se nem nova_quantidade nem delta forem fornecidos, ou produto não estiver no estoque.
        """
        estoque = self.repository.get_by_id(estoque_id)
        if not estoque:
            raise EstoqueNaoEncontradoError(f"Estoque com ID {estoque_id} não encontrado.")

        # Verifica se o produto está no estoque
        if produto_id not in estoque.produtos:
            raise ValueError(f"Produto {produto_id} não está no estoque {estoque_id}.")

        # Aplica atualização conforme parâmetros
        if nova_quantidade is not None:
            qtd_vo = Quantidade(nova_quantidade)
            estoque.atualizar_quantidade_produto(produto_id, qtd_vo)
        elif delta is not None:
            estoque.aplicar_delta_produto(produto_id, delta)
        else:
            raise ValueError("Deve fornecer nova_quantidade ou delta.")

        return self.repository.save(estoque)
    