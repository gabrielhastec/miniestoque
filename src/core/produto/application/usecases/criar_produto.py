from datetime import date

from src.core.produto.domain.entities.produto import Produto
from src.core.produto.domain.exceptions.produto_exceptions import ProdutoPrecoInvalidoError
from src.core.produto.domain.repositories.produto_repository_interface import ProdutoRepositoryInterface
from src.core.produto.domain.value_objects.nome import Nome
from src.core.produto.domain.value_objects.preco import Preco

class CriarProduto:
    """
    Use case para criar um novo Produto.

    Orquestra a criação: valida inputs, instancia entidade e persiste via repositório.
    Mantém a camada de aplicação isolada do domínio e infraestrutura.

    Attributes:
        repository (ProdutoRepositoryInterface): Repositório para persistência.
    """

    def __init__(self, repository: ProdutoRepositoryInterface) -> None:
        self.repository = repository

    def execute(self, nome: str, preco: float, descricao: str = None) -> Produto:
        """
        Executa a criação do produto.

        Args:
            nome (str): Nome do produto.
            preco (float): Preço unitário.
            descricao (str, optional): Descrição adicional.

        Returns:
            Produto: O produto criado e persistido.

        Raises:
            ValueError: Para validações de domínio (ex.: nome inválido).
            ProdutoPrecoInvalidoError: Se o preço for inválido.
        """
        try:
            nome_vo = Nome(nome)
            preco_vo = Preco(preco)
        except ValueError as e:
            raise ValueError(f"Input inválido: {e}")

        if preco_vo.valor <= 0:
            raise ProdutoPrecoInvalidoError("Preço deve ser positivo.")

        # Cria a entidade Produto
        produto = Produto(
            nome=nome_vo,
            preco=preco_vo,
            descricao=descricao,
            data_criacao=date.today()
        )
        # Persiste o produto via repositório
        self.repository.adicionar(produto)
        return produto
    
__all__ = ["CriarProduto"]
