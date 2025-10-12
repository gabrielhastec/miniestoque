"""
Repositório concreto para Produto, implementando a interface do domínio.

Usa SQLAlchemy para persistência em banco de dados.
Mapeia entre ProdutoModel (infra) e Produto (domain) via factory.

Dependências: models de database e session.
"""

from typing import List, Optional

from sqlalchemy.orm import Session

from src.core.produto.domain.entities.produto import Produto
from src.core.produto.domain.repositories.produto_repository_interface import ProdutoRepositoryInterface
from src.core.produto.application.factories.produto_factory import ProdutoFactory
from src.infrastructure.database.models.produto_model import ProdutoModel
from src.infrastructure.database.session import get_session

class ProdutoRepository(ProdutoRepositoryInterface):
    """
    Implementação concreta do repositório de Produto.

    Gerencia operações CRUD usando SQLAlchemy e mapeamento para entidades de domínio.

    Attributes:
        session (Optional[Session]): Sessão DB (injetada ou gerenciada internamente).
    """

    def __init__(self, session: Optional[Session] = None) -> None:
        self.session = session or next(get_session())

    def save(self, produto: Produto) -> Produto:
        """
        Salva ou atualiza um Produto no banco.

        Converte entidade para model, persiste e mapeia de volta.

        Args:
            produto (Produto): Entidade a persistir.

        Returns:
            Produto: Entidade salva com ID atualizado.

        Raises:
            Exception: Para erros de banco (ex.: integridade).
        """
        model = ProdutoModel(
            id=produto.id,
            nome=str(produto.nome),
            preco=produto.preco.valor,
            descricao=produto.descricao
        )
        self.session.add(model)
        self.session.flush()  # Flush para gerar ID sem commit
        produto.id = model.id  # Atualiza ID na entidade
        return produto

    def get_by_id(self, produto_id: int) -> Optional[Produto]:
        """
        Busca um Produto pelo ID.

        Args:
            produto_id (int): ID do produto.

        Returns:
            Optional[Produto]: Entidade ou None.
        """
        model = self.session.query(ProdutoModel).filter(ProdutoModel.id == produto_id).first()
        if model:
            return ProdutoFactory.criar_entidade(model.to_dict())
        return None

    def get_all(self) -> List[Produto]:
        """
        Lista todos os Produtos.

        Returns:
            List[Produto]: Lista de entidades.
        """
        models = self.session.query(ProdutoModel).all()
        return [ProdutoFactory.criar_entidade(m.to_dict()) for m in models]

    def delete(self, produto_id: int) -> bool:
        """
        Remove um Produto pelo ID.

        Args:
            produto_id (int): ID a remover.

        Returns:
            bool: True se removido.
        """
        model = self.session.query(ProdutoModel).filter(ProdutoModel.id == produto_id).first()
        if model:
            self.session.delete(model)
            self.session.flush()
            return True
        return False
