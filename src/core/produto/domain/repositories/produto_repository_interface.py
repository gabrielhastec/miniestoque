from abc import ABC, abstractmethod
from typing import List, Optional

from src.core.produto.domain.entities.produto import Produto

class ProdutoRepositoryInterface(ABC):
    """
    Interface para repositório de Produto no domínio.

    Define o contrato para operações CRUD de Produtos, permitindo inversão de dependências.
    Implementações concretas ficam na infraestrutura (ex.: SQLAlchemy, in-memory).

    Methods:
        save: Persiste ou atualiza um Produto.
        get_by_id: Busca um Produto por ID.
        get_all: Lista todos os Produtos.
        delete: Remove um Produto por ID.
    """

    @abstractmethod
    def save(self, produto: Produto) -> Produto:
        """
        Salva ou atualiza um Produto no repositório.

        Args:
            produto (Produto): A entidade Produto a ser persistida.

        Returns:
            Produto: A entidade salva, com ID atualizado se novo.

        Raises:
            Exception: Para erros de persistência (implementação específica).
        """

    @abstractmethod
    def get_by_id(self, produto_id: int) -> Optional[Produto]:
        """
        Busca um Produto pelo seu ID.

        Args:
            produto_id (int): O ID do Produto a buscar.

        Returns:
            Optional[Produto]: O Produto encontrado ou None se não existir.
        """

    @abstractmethod
    def get_all(self) -> List[Produto]:
        """
        Retorna a lista de todos os Produtos.

        Returns:
            List[Produto]: Lista de entidades Produto.
        """

    @abstractmethod
    def delete(self, produto_id: int) -> bool:
        """
        Remove um Produto pelo seu ID.

        Args:
            produto_id (int): O ID do Produto a remover.

        Returns:
            bool: True se removido com sucesso, False caso não encontrado.
        """
