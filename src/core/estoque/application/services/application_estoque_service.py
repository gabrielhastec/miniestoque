from typing import Optional

from src.core.estoque.application.usecases.adicionar_produto_ao_estoque import AdicionarProdutoAoEstoque
from src.core.estoque.application.usecases.atualizar_estoque import AtualizarEstoque
from src.core.estoque.application.usecases.consultar_estoque import ConsultarEstoque
from src.core.estoque.application.usecases.remover_produto_do_estoque import RemoverProdutoDoEstoque
from src.core.estoque.domain.entities.estoque import Estoque
from src.core.estoque.domain.repositories.estoque_repository_interface import EstoqueRepositoryInterface
from src.core.produto.domain.repositories.produto_repository_interface import ProdutoRepositoryInterface

class ApplicationEstoqueService:
    """
    Serviço de aplicação para orquestrar use cases de Estoque.

    Coordena operações como adição, atualização e consulta, injetando repositórios.
    Não contém lógica de negócio; delega para use cases.

    Attributes:
        estoque_repository (EstoqueRepositoryInterface): Repositório principal.
        produto_repository (ProdutoRepositoryInterface): Para validações cruzadas.
    """

    def __init__(
        self,
        estoque_repository: EstoqueRepositoryInterface,
        produto_repository: ProdutoRepositoryInterface,
    ) -> None:
        self.estoque_repository = estoque_repository
        self.produto_repository = produto_repository
        self._adicionar_use_case = AdicionarProdutoAoEstoque(self.estoque_repository, self.produto_repository)
        self._atualizar_use_case = AtualizarEstoque(self.estoque_repository)
        self._consultar_use_case = ConsultarEstoque(self.estoque_repository)
        self._remover_use_case = RemoverProdutoDoEstoque(self.estoque_repository)

    def adicionar_produto(self, estoque_id: int, produto_id: int, quantidade: int) -> Estoque:
        """
        Adiciona um produto ao estoque via use case.

        Args:
            estoque_id (int): ID do estoque.
            produto_id (int): ID do produto.
            quantidade (int): Quantidade a adicionar.

        Returns:
            Estoque: Estoque atualizado.

        Raises:
            EstoqueNaoEncontradoError: Se estoque não existir.
            ValueError: Para produto inválido.
            QuantidadeInvalidaError: Para quantidade inválida.
        """
        return self._adicionar_use_case.execute(estoque_id, produto_id, quantidade)

    def atualizar_quantidade(self, estoque_id: int, produto_id: int, nova_quantidade: Optional[int] = None, delta: Optional[int] = None) -> Estoque:
        """
        Atualiza quantidade de produto no estoque.

        Args:
            estoque_id (int): ID do estoque.
            produto_id (int): ID do produto.
            nova_quantidade (Optional[int]): Nova quantidade absoluta.
            delta (Optional[int]): Variação.

        Returns:
            Estoque: Estoque atualizado.

        Raises:
            ValueError: Para parâmetros inválidos.
        """
        return self._atualizar_use_case.execute(estoque_id, produto_id, nova_quantidade, delta)

    def consultar(self, estoque_id: Optional[int] = None) -> Estoque | list[Estoque]:
        """
        Consulta estoque(s).

        Args:
            estoque_id (Optional[int]): ID específico.

        Returns:
            Estoque | list[Estoque]: Resultado da consulta.
        """
        return self._consultar_use_case.execute(estoque_id)

    def remover_produto(self, estoque_id: int, produto_id: int) -> Estoque:
        """
        Remove produto do estoque.

        Args:
            estoque_id (int): ID do estoque.
            produto_id (int): ID do produto.

        Returns:
            Estoque: Estoque atualizado.

        Raises:
            ProdutoNaoNoEstoqueError: Se produto não estiver presente.
        """
        return self._remover_use_case.execute(estoque_id, produto_id)
    