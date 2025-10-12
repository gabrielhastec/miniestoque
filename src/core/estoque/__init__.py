"""
Pacote core para o domínio de Estoque.

Contém entidades, value objects, exceções, serviços de domínio, use cases de aplicação,
e factories relacionados a Estoques. Segue Clean Architecture, com domínio puro isolado.

Exemplos de uso:
    from src.core.estoque import Estoque, ApplicationEstoqueService
"""

from .domain.entities.estoque import Estoque
from .domain.value_objects.quantidade import Quantidade
from .domain.exceptions.estoque_exceptions import (
    EstoqueException,
    EstoqueNaoEncontradoError,
    QuantidadeInvalidaError,
    ProdutoNaoNoEstoqueError,
)
from .domain.repositories.estoque_repository_interface import EstoqueRepositoryInterface
from .domain.services.domain_estoque_service import DomainEstoqueService
from .application.services.application_estoque_service import ApplicationEstoqueService
from .application.usecases.adicionar_produto_ao_estoque import AdicionarProdutoAoEstoque
from .application.usecases.atualizar_estoque import AtualizarEstoque
from .application.usecases.consultar_estoque import ConsultarEstoque
from .application.usecases.remover_produto_do_estoque import RemoverProdutoDoEstoque
from .application.factories.estoque_factory import EstoqueFactory

__all__ = [
    "Estoque",
    "Quantidade",
    "EstoqueException",
    "EstoqueNaoEncontradoError",
    "QuantidadeInvalidaError",
    "ProdutoNaoNoEstoqueError",
    "EstoqueRepositoryInterface",
    "DomainEstoqueService",
    "ApplicationEstoqueService",
    "AdicionarProdutoAoEstoque",
    "AtualizarEstoque",
    "ConsultarEstoque",
    "RemoverProdutoDoEstoque",
    "EstoqueFactory",
]
