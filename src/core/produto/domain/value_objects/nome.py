from dataclasses import dataclass
from typing import NewType

NomeStr = NewType('NomeStr', str)

@dataclass(frozen=True)
class Nome:
    """
    Value Object representando o nome de um produto.

    Garante que o nome seja uma string válida (não vazia, máx. 100 chars),
    encapsulando validação e normalização.

    Attributes:
        valor (NomeStr): O valor do nome como string tipada.
    """

    valor: NomeStr

    def __post_init__(self) -> None:
        """Valida o nome após inicialização."""
        if not self.valor or len(self.valor) > 100:
            raise ValueError("Nome deve ter entre 1 e 100 caracteres.")

    def __str__(self) -> str:
        """Retorna o valor como string."""
        return self.valor
