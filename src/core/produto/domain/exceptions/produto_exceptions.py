from typing import Optional

class ProdutoException(Exception):
    """Exceção base para erros no domínio de Produto."""

class ProdutoNaoEncontradoError(ProdutoException):
    """
    Exceção levantada quando um Produto não é encontrado.

    Útil para cenários de consulta por ID ou nome.

    Attributes:
        mensagem (str): Mensagem de erro detalhada.
        id_produto (Optional[int]): ID do produto não encontrado (opcional).
    """

    def __init__(self, mensagem: str = "Produto não encontrado.", id_produto: Optional[int] = None) -> None:
        super().__init__(mensagem)
        self.id_produto = id_produto

class ProdutoPrecoInvalidoError(ProdutoException):
    """
    Exceção para preços inválidos em Produtos.

    Levantada durante atualizações ou criações com valores negativos ou zero.
    """
    def __init__(self, mensagem: str = "Preço do produto é inválido.") -> None:
        super().__init__(mensagem)
    
class ProdutoNomeInvalidoError(ProdutoException):
    """
    Exceção para nomes inválidos em Produtos.

    Levantada quando o nome é vazio ou não atende aos critérios de validação.
    """
    def __init__(self, mensagem: str = "Nome do produto é inválido.") -> None:
        super().__init__(mensagem)
