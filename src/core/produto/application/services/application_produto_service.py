from typing import Optional

from src.core.produto.application.usecases.criar_produto import CriarProduto
from src.core.produto.application.usecases.atualizar_produto import AtualizarProduto
from src.core.produto.domain.repositories.produto_repository_interface import ProdutoRepositoryInterface
from src.core.produto.domain.entities.produto import Produto

class ApplicationProdutoService:
    """
    Serviço de aplicação para orquestrar use cases de Produto.

    Coordena fluxos como criação e atualização, injetando dependências.
    Não contém lógica de negócio; delega para use cases e domínio.

    Attributes:
        repository (ProdutoRepositoryInterface): Repositório injetado.
    """

    def __init__(self, repository: ProdutoRepositoryInterface) -> None:
        self.repository = repository
        self._criar_use_case = CriarProduto(self.repository)
        self._atualizar_use_case = AtualizarProduto(self.repository)

    def criar_produto(self, nome: str, preco: float, descricao: Optional[str] = None) -> Produto:
        """
        Cria um novo produto via use case.

        Args:
            nome (str): Nome do produto.
            preco (float): Preço unitário.
            descricao (Optional[str]): Descrição.

        Returns:
            Produto: Produto criado.

        Raises:
            ValueError: Para inputs inválidos.
            ProdutoPrecoInvalidoError: Para preço inválido.
        """
        return self._criar_use_case.execute(nome, preco, descricao)

    def atualizar_produto(self, produto_id: int, nome: Optional[str] = None, preco: Optional[float] = None) -> Produto:
        """
        Atualiza um produto existente via use case.

        Args:
            produto_id (int): ID do produto a atualizar.
            nome (Optional[str]): Novo nome (se fornecido).
            preco (Optional[float]): Novo preço (se fornecido).

        Returns:
            Produto: Produto atualizado.

        Raises:
            ProdutoNaoEncontradoError: Se o produto não existir.
        """
        return self._atualizar_use_case.execute(produto_id, nome, preco)
    
    # Métodos adicionais para outros use cases podem ser adicionados aqui.

    