from dataclasses import dataclass
from typing import NewType

from src.core.estoque.domain.exceptions.estoque_exceptions import QuantidadeInvalidaError

QuantidadeInt = NewType('QuantidadeInt', int)

@dataclass(frozen=True)
class Quantidade:
    """
    Value Object representando uma quantidade no estoque.

    Garante que a quantidade seja um inteiro não-negativo, encapsulando validação.

    Attributes:
        valor (QuantidadeInt): O valor da quantidade como inteiro tipado.
    """

    valor: QuantidadeInt

    def __post_init__(self) -> None:
        """Valida a quantidade após inicialização."""
        if self.valor < 0:
            raise QuantidadeInvalidaError("Quantidade não pode ser negativa.")

    def __str__(self) -> str:
        """Retorna o valor como string."""
        return str(self.valor)

    def __add__(self, other: 'Quantidade') -> 'Quantidade':
        """
        Sobrecarrega o operador + para somar quantidades.

        Args:
            other (Quantidade): Quantidade a somar.

        Returns:
            Quantidade: Nova quantidade resultante.
        """
        if not isinstance(other, Quantidade):
            raise TypeError("Pode somar apenas Quantidade com Quantidade.")
        return Quantidade(self.valor + other.valor)

    def __sub__(self, other: 'Quantidade') -> 'Quantidade':
        """
        Sobrecarrega o operador - para subtrair quantidades.

        Args:
            other (Quantidade): Quantidade a subtrair.

        Returns:
            Quantidade: Nova quantidade resultante (levanta erro se negativa).

        Raises:
            QuantidadeInvalidaError: Se o resultado for negativo.
        """
        if not isinstance(other, Quantidade):
            raise TypeError("Pode subtrair apenas Quantidade de Quantidade.")
        resultado = self.valor - other.valor
        if resultado < 0:
            raise QuantidadeInvalidaError("Resultado de subtração não pode ser negativo.")
        return Quantidade(resultado)
    