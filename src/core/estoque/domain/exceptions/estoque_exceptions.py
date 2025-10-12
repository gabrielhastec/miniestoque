from typing import Optional

class EstoqueException(Exception):
    """Exceção base para erros no domínio de Estoque."""

class EstoqueNaoEncontradoError(EstoqueException):
    """
    Exceção levantada quando um Estoque não é encontrado.

    Útil para cenários de consulta por ID.

    Attributes:
        mensagem (str): Mensagem de erro detalhada.
        id_estoque (Optional[int]): ID do estoque não encontrado (opcional).
    """

    def __init__(self, mensagem: str = "Estoque não encontrado.", id_estoque: Optional[int] = None) -> None:
        super().__init__(mensagem)
        self.id_estoque = id_estoque

class QuantidadeInvalidaError(EstoqueException):
    """
    Exceção para quantidades inválidas em Estoque.

    Levantada durante criações, atualizações ou operações com valores negativos.
    """
    pass

class ProdutoNaoNoEstoqueError(EstoqueException):
    """
    Exceção quando um produto não está presente no estoque.

    Útil para remoções ou atualizações inválidas.
    """
    pass
