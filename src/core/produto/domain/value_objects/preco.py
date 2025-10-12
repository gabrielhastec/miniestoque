from dataclasses import dataclass
from typing import NewType

PrecoFloat = NewType('PrecoFloat', float)

@dataclass(frozen=True)
class Preco:
    """
    Value Object representando o preço de um produto.
    Garante que o preço seja um valor positivo, encapsulando validação e normalização.
    
    Attributes:
        valor (float): O valor do preço como número de ponto flutuante.
    """
    valor: float

    def __post_init__(self) -> None:
        """Valida o preço após inicialização."""
        if self.valor <= 0:
            raise ValueError("Preço deve ser um valor positivo.")

    def __str__(self) -> str:
        """Retorna o valor como string formatada."""
        return f"{self.valor:.2f}"   
