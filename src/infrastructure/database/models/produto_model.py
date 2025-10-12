"""
Modelo ORM para entidade Produto.

Mapeia a tabela 'produtos' no banco, com campos correspondentes à entidade de domínio.
Integra com value objects via validações opcionais (adicione em factories para mapeamento).
"""

from sqlalchemy import Column, Float, String
from sqlalchemy.orm import relationship

from ..base import BaseModel

class ProdutoModel(BaseModel):
    """
    Modelo SQLAlchemy para Produto.

    Tabela: produtos. Relaciona com Estoque via associação (muitos-para-muitos).

    Attributes:
        nome (str): Nome do produto (máx. 100 chars).
        preco (float): Preço unitário.
        descricao (str, optional): Descrição do produto.
        estoques (list[EstoqueModel]): Produtos em estoques (relacionamento).
    """

    __tablename__ = "produtos"

    nome = Column(String(100), nullable=False, index=True)
    preco = Column(Float, nullable=False)
    descricao = Column(String(500))

    # Relacionamento: um produto pode estar em múltiplos estoques
    estoques = relationship("EstoqueModel", secondary="estoque_produtos", back_populates="produtos")
