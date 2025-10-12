from dataclasses import dataclass
from typing import Dict

from src.core.estoque.domain.exceptions.estoque_exceptions import EstoqueException
from src.core.estoque.domain.value_objects.quantidade import Quantidade

@dataclass
class Estoque:
    """
    Entidade de domínio representando um estoque no sistema.

    Um Estoque gerencia um mapeamento de produtos (por ID) para suas quantidades.
    Suporta operações mutáveis como adição e remoção, com validações embutidas.

    Attributes:
        id (int): Identificador único do estoque.
        produtos (Dict[int, Quantidade]): Mapeamento de ID de produto para quantidade.
        nome (str): Nome descritivo do estoque (ex.: "Estoque Principal").
    """

    id: int
    produtos: Dict[int, Quantidade]
    nome: str

    def __post_init__(self) -> None:
        """Inicializa o mapeamento de produtos se vazio."""
        if self.produtos is None:
            object.__setattr__(self, 'produtos', {})

    def adicionar_produto(self, produto_id: int, quantidade: Quantidade) -> None:   
        """
        Adiciona ou incrementa a quantidade de um produto no estoque.

        Args:
            produto_id (int): ID do produto a adicionar.
            quantidade (Quantidade): Quantidade a somar.

        Raises:
            EstoqueException: Se o produto_id for inválido (negativo).
        """
        if produto_id < 1:
            raise EstoqueException("ID de produto deve ser positivo.")
        if produto_id in self.produtos:
            self.produtos[produto_id] = self.produtos[produto_id] + quantidade
        else:
            self.produtos[produto_id] = quantidade

    def remover_produto(self, produto_id: int) -> None:
        """
        Remove um produto do estoque.

        Args:
            produto_id (int): ID do produto a remover.

        Raises:
            EstoqueException: Se o produto não existir no estoque ou ID inválido.
        """
        if produto_id < 1:
            raise EstoqueException("ID de produto deve ser positivo.")
        if produto_id not in self.produtos:
            raise EstoqueException(f"Produto {produto_id} não está no estoque.")
        del self.produtos[produto_id]

    def atualizar_quantidade_produto(self, produto_id: int, nova_quantidade: Quantidade) -> None:
        """
        Atualiza a quantidade de um produto específico.

        Args:
            produto_id (int): ID do produto.
            nova_quantidade (Quantidade): Nova quantidade a definir.

        Raises:
            EstoqueException: Se o produto não existir ou ID inválido.
        """
        if produto_id < 1:
            raise EstoqueException("ID de produto deve ser positivo.")
        if produto_id not in self.produtos:
            raise EstoqueException(f"Produto {produto_id} não está no estoque.")
        self.produtos[produto_id] = nova_quantidade

    def aplicar_delta_produto(self, produto_id: int, delta: int) -> None:
        """
        Aplica uma variação (delta) na quantidade de um produto.

        Args:
            produto_id (int): ID do produto.
            delta (int): Variação positiva ou negativa.

        Raises:
            EstoqueException: Se o produto não existir, ID inválido ou resultante negativo.
        """
        if produto_id < 1:
            raise EstoqueException("ID de produto deve ser positivo.")
        if produto_id not in self.produtos:
            raise EstoqueException(f"Produto {produto_id} não está no estoque.")
        nova_qtd = self.produtos[produto_id] + Quantidade(delta)
        if nova_qtd.valor < 0:
            raise EstoqueException("Quantidade não pode ser negativa.")
        self.produtos[produto_id] = nova_qtd

    def total_itens(self) -> int:
        """
        Calcula o total de itens no estoque (soma de quantidades).

        Returns:
            int: Soma total de quantidades.
        """
        return sum(q.valor for q in self.produtos.values())
    
    def listar_produtos(self) -> Dict[int, int]:
        """
        Retorna um dicionário simples de produtos e suas quantidades.

        Returns:
            Dict[int, int]: Mapeamento de ID de produto para quantidade inteira.
        """
        return {pid: qtd.valor for pid, qtd in self.produtos.items()}
    