from typing import List

from src.core.produto.domain.entities.produto import Produto
from src.core.produto.domain.value_objects.preco import Preco

class DomainProdutoService:
    """
    Serviço de domínio para lógica de negócio pura relacionada a Produtos.

    Contém operações que não dependem de repositórios ou infraestrutura,
    como cálculos de descontos ou validações entre múltiplos produtos.

    Methods:
        calcular_desconto_total: Calcula desconto agregado para uma lista de produtos.
    """

    @staticmethod
    def calcular_desconto_total(produtos: List[Produto], taxa_desconto: float) -> Preco:
        """
        Calcula o desconto total aplicado a uma lista de produtos.

        Aplica uma taxa percentual uniforme a todos os produtos e soma os valores.

        Args:
            produtos (List[Produto]): Lista de produtos a serem descontados.
            taxa_desconto (float): Taxa de desconto em decimal (ex.: 0.1 para 10%).

        Returns:
            Preco: O valor total do desconto calculado.

        Raises:
            ValueError: Se a taxa de desconto for maior que 1.0 ou negativa.
        """
        if taxa_desconto < 0 or taxa_desconto > 1.0:
            raise ValueError("Taxa de desconto deve estar entre 0 e 1.0.")

        desconto_total = sum(p.preco.valor * taxa_desconto for p in produtos)
        return Preco(desconto_total)
    
    @staticmethod
    def validar_produtos_unicos(produtos: List[Produto]) -> bool:
        """
        Valida se todos os produtos na lista são únicos com base no ID.

        Args:
            produtos (List[Produto]): Lista de produtos a serem validados.

        Returns:
            bool: True se todos os produtos forem únicos, False caso contrário.
        """
        ids = [p.id for p in produtos]
        return len(ids) == len(set(ids))
