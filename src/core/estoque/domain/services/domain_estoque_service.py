from typing import List

from src.core.estoque.domain.entities.estoque import Estoque
from src.core.estoque.domain.value_objects.quantidade import Quantidade

class DomainEstoqueService:
    """
    Serviço de domínio para lógica de negócio pura relacionada a Estoques.

    Contém operações que não dependem de repositórios ou infraestrutura,
    como validações agregadas ou cálculos entre múltiplos estoques.

    Methods:
        validar_capacidade_total: Verifica se o total de itens excede um limite.
        calcular_quantidade_agregada: Soma quantidades de um produto across estoques.
    """

    @staticmethod
    def validar_capacidade_total(estoque: Estoque, limite_maximo: int) -> bool:
        """
        Valida se o total de itens no estoque não excede o limite.

        Args:
            estoque (Estoque): O estoque a validar.
            limite_maximo (int): Limite máximo de itens totais.

        Returns:
            bool: True se válido, False caso exceda.

        Raises:
            ValueError: Se o limite for negativo.
        """
        if limite_maximo < 0:
            raise ValueError("Limite máximo deve ser não-negativo.")
        total = estoque.total_itens()
        return total <= limite_maximo

    @staticmethod
    def calcular_quantidade_agregada(
        estoques: List[Estoque], produto_id: int
    ) -> Quantidade:
        """
        Calcula a quantidade total de um produto across múltiplos estoques.

        Args:
            estoques (List[Estoque]): Lista de estoques a agregar.
            produto_id (int): ID do produto a somar.

        Returns:
            Quantidade: Quantidade agregada.

        Raises:
            ValueError: Se produto_id inválido ou nenhum estoque tiver o produto.
        """
        if produto_id < 1:
            raise ValueError("ID de produto deve ser positivo.")
        total = sum(
            e.produtos.get(produto_id, Quantidade(0)).valor for e in estoques
        )
        if total == 0:
            raise ValueError(f"Nenhum estoque possui o produto {produto_id}.")
        return Quantidade(total)
    