from abc import ABC, abstractmethod
from typing import List, Optional

from src.core.estoque.domain.entities.estoque import Estoque

class EstoqueRepositoryInterface(ABC):
    """
    Interface para repositório de Estoque no domínio.

    Define o contrato para operações CRUD de Estoques, permitindo inversão de dependências.
    Implementações concretas ficam na infraestrutura (ex.: SQLAlchemy, in-memory).

    Methods:
        save: Persiste ou atualiza um Estoque.
        get_by_id: Busca um Estoque por ID.
        get_all: Lista todos os Estoques.
        delete: Remove um Estoque por ID.
    """

    @abstractmethod
    def save(self, estoque: Estoque) -> Estoque:
        """
        Salva ou atualiza um Estoque no repositório.

        Args:
            estoque (Estoque): A entidade Estoque a ser persistida.

        Returns:
            Estoque: A entidade salva, com ID atualizado se novo.

        Raises:
            Exception: Para erros de persistência (implementação específica).
        """

    @abstractmethod
    def get_by_id(self, estoque_id: int) -> Optional[Estoque]:
        """
        Busca um Estoque pelo seu ID.

        Args:
            estoque_id (int): O ID do Estoque a buscar.

        Returns:
            Optional[Estoque]: O Estoque encontrado ou None se não existir.
        """

    @abstractmethod
    def get_all(self) -> List[Estoque]:
        """
        Retorna a lista de todos os Estoques.

        Returns:
            List[Estoque]: Lista de entidades Estoque.
        """

    @abstractmethod
    def delete(self, estoque_id: int) -> bool:
        """
        Remove um Estoque pelo seu ID.

        Args:
            estoque_id (int): O ID do Estoque a remover.

        Returns:
            bool: True se removido com sucesso, False caso não encontrado.
        """
    