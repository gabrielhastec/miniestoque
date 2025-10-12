from typing import List, Optional

from src.core.estoque.domain.entities.estoque import Estoque
from src.core.estoque.domain.repositories.estoque_repository_interface import EstoqueRepositoryInterface

class ConsultarEstoque:
    """
    Use case para consultar estoques, com filtros opcionais.

    Orquestra buscas no repositório, retornando entidades ou listas.

    Attributes:
        repository (EstoqueRepositoryInterface): Repositório para consultas.
    """

    def __init__(self, repository: EstoqueRepositoryInterface) -> None:
        self.repository = repository

    def execute(self, estoque_id: Optional[int] = None) -> Estoque | List[Estoque]:
        """
        Executa a consulta de estoque(s).

        Se ID fornecido, retorna um único; caso contrário, todos.

        Args:
            estoque_id (Optional[int]): ID específico para busca única.

        Returns:
            Estoque | List[Estoque]: Entidade única ou lista de estoques.

        Raises:
            EstoqueNaoEncontradoError: Se ID fornecido e estoque não existir.
        """
        if estoque_id is not None:
            estoque = self.repository.get_by_id(estoque_id)
            if not estoque:
                from src.core.estoque.domain.exceptions.estoque_exceptions import EstoqueNaoEncontradoError
                raise EstoqueNaoEncontradoError(f"Estoque com ID {estoque_id} não encontrado.")
            return estoque
        return self.repository.get_all()
    