from typing import Dict

from src.core.produto.domain.entities.produto import Produto
from src.core.produto.domain.value_objects.nome import Nome
from src.core.produto.domain.value_objects.preco import Preco
from src.core.produto.domain.repositories.produto_repository_interface import ProdutoRepositoryInterface
from src.core.produto.application.services.application_produto_service import ApplicationProdutoService

class ProdutoFactory:
    """
    Factory para criação de objetos relacionados a Produto.

    Facilita a instanciação com dados de dicionários ou defaults,
    útil para testes ou mapeamento de dados externos.

    Methods:
        criar_entidade: Cria uma entidade Produto a partir de dados.
        criar_service: Cria o application service com repositório.
    """

    @staticmethod
    def criar_entidade(data: Dict[str, any]) -> Produto:
        """
        Cria uma instância de Produto a partir de um dicionário.

        Args:
            data (Dict[str, any]): Dados com chaves 'id', 'nome', 'preco', etc.

        Returns:
            Produto: Entidade instanciada.

        Raises:
            KeyError: Se chaves obrigatórias faltarem.
            ValueError: Para valores inválidos.
        """
        return Produto(
            id=data['id'],
            nome=Nome(data['nome']),
            preco=Preco(data['preco']),
            data_criacao=data.get('data_criacao', date.today()),
            descricao=data.get('descricao')
        )

    @staticmethod
    def criar_service(repository: ProdutoRepositoryInterface) -> ApplicationProdutoService:
        """
        Cria o ApplicationProdutoService com repositório injetado.

        Args:
            repository (ProdutoRepositoryInterface): Repositório para injeção.

        Returns:
            ApplicationProdutoService: Serviço pronto para uso.
        """
        return ApplicationProdutoService(repository)
    
__all__ = ["ProdutoFactory"]