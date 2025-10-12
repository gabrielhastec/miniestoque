"""
Pacote core para o domínio de Produto.

Contém entidades, value objects, exceções, serviços de domínio, use cases de aplicação,
e factories relacionados a Produtos. Segue Clean Architecture, com domínio puro isolado.

Exemplos de uso:
    from src.core.produto import Produto, ApplicationProdutoService
"""

from .domain.entities.produto import Produto
from .domain.value_objects.nome import Nome
from .domain.value_objects.preco import Preco
from .domain.exceptions.produto_exceptions import (
    ProdutoException,
    ProdutoNaoEncontradoError,
    ProdutoPrecoInvalidoError,
)
from .domain.repositories.produto_repository_interface import ProdutoRepositoryInterface
from .domain.services.domain_produto_service import DomainProdutoService
from .application.services.application_produto_service import ApplicationProdutoService
from .application.usecases.criar_produto import CriarProduto
from .application.usecases.atualizar_produto import AtualizarProduto
from .application.factories.produto_factory import ProdutoFactory

__all__ = [
    "Produto",
    "Nome",
    "Preco",
    "ProdutoException",
    "ProdutoNaoEncontradoError",
    "ProdutoPrecoInvalidoError",
    "ProdutoRepositoryInterface",
    "DomainProdutoService",
    "ApplicationProdutoService",
    "CriarProduto",
    "AtualizarProduto",
    "ProdutoFactory",
]
