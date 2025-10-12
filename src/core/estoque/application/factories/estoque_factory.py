from typing import Dict, Any

from src.core.estoque.application.services.application_estoque_service import ApplicationEstoqueService
from src.core.estoque.domain.entities.estoque import Estoque
from src.core.estoque.domain.repositories.estoque_repository_interface import EstoqueRepositoryInterface
from src.core.estoque.domain.value_objects.quantidade import Quantidade
from src.core.produto.domain.entities.produto import Produto
from src.core.produto.domain.repositories.produto_repository_interface import ProdutoRepositoryInterface

class EstoqueFactory:
    """
    Factory para criação de objetos relacionados a Estoque.

    Suporta instanciação de entidades a partir de dados e criação de services com DI.

    Methods:
        criar_entidade: Cria Estoque de dicionário.
        criar_service: Cria ApplicationEstoqueService com repositórios.
    """

    @staticmethod
    def criar_entidade(data: Dict[str, Any]) -> Estoque:
        """
        Cria uma instância de Estoque a partir de dados.

        Args:
            data (Dict[str, Any]): Dados com 'id', 'produtos' (dict de {produto_id: quantidade}), etc.

        Returns:
            Estoque: Entidade instanciada.

        Raises:
            KeyError: Para chaves faltantes.
            ValueError: Para dados inválidos em value objects.
        """
        # Constrói o dicionário de produtos com Value Objects de Quantidade
        produtos_dict = data.get('produtos', {})
        produtos = {
            pid: Quantidade(qtd) for pid, qtd in produtos_dict.items()
        }
        # Retorna a entidade Estoque
        return Estoque(
            id=data['id'],
            produtos=produtos,
            # Adicione outros attrs como nome_estoque se aplicável
        )

    @staticmethod
    def criar_service(
        estoque_repo: EstoqueRepositoryInterface,
        produto_repo: ProdutoRepositoryInterface,
    ) -> ApplicationEstoqueService:
        """
        Cria o ApplicationEstoqueService com repositórios injetados.

        Args:
            estoque_repo (EstoqueRepositoryInterface): Repositório de estoque.
            produto_repo (ProdutoRepositoryInterface): Repositório de produto.

        Returns:
            ApplicationEstoqueService: Serviço configurado.
        """
        return ApplicationEstoqueService(estoque_repo, produto_repo)
    