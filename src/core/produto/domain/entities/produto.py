from dataclasses import dataclass
from datetime import date
from typing import Optional

from src.core.produto.domain.value_objects.preco import Preco
from src.core.produto.domain.value_objects.nome import Nome

@dataclass(frozen=True)
class Produto:
    """
    Entidade de domínio representando um produto no sistema.

    Um Produto possui atributos imutáveis como ID, nome, preço e data de criação.
    Representa o conceito central de um item comercializável, com validações embutidas.

    Attributes:
        id (int): Identificador único do produto.
        nome (Nome): Nome descritivo do produto (value object).
        preco (Preco): Preço unitário do produto (value object).
        data_criacao (date): Data de criação do produto.
        descricao (Optional[str]): Descrição opcional do produto.
    """

    id: int
    nome: Nome
    preco: Preco
    data_criacao: date
    descricao: Optional[str] = None
    
    def atualizar_preco(self, novo_preco: Preco) -> None:
        """
        Atualiza o preço do produto.

        Esta operação é mutável e deve ser chamada apenas em contextos transacionais.

        Args:
            novo_preco (Preco): O novo preço a ser definido.

        Raises:
            ValueError: Se o novo preço for inválido (ex.: negativo).
        """
        if novo_preco.valor <= 0:
            raise ValueError("Preço deve ser positivo.")
        object.__setattr__(self, 'preco', novo_preco)  # Bypass frozen para mutação controlada
    
    def atualizar_nome(self, novo_nome: Nome) -> None:
        """
        Atualiza o nome do produto.

        Esta operação é mutável e deve ser chamada apenas em contextos transacionais.

        Args:
            novo_nome (Nome): O novo nome a ser definido.

        Raises:
            ValueError: Se o novo nome for inválido (ex.: vazio).
        """
        if not novo_nome.valor.strip():
            raise ValueError("Nome não pode ser vazio.")
        object.__setattr__(self, 'nome', novo_nome)  # Bypass frozen para
    
    def __str__(self) -> str:
        return f"Produto(id={self.id}, nome={self.nome.valor}, preco={self.preco.valor}, data_criacao={self.data_criacao}, descricao={self.descricao})"
    