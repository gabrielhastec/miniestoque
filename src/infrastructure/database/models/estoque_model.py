"""
Modelo ORM para entidade Estoque.

Mapeia a tabela 'estoques' no banco, com mapeamento de produtos via tabela de associação.
A quantidade é armazenada na tabela associativa.
"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import BaseModel

class EstoqueModel(BaseModel):
    """
    Modelo SQLAlchemy para Estoque.

    Tabela: estoques. Relaciona com Produto via associação.

    Attributes:
        nome (str): Nome do estoque.
        produtos (list[ProdutoModel]): Produtos no estoque, com quantidades na associação.
    """

    __tablename__ = "estoques"

    nome = Column(String(100), nullable=False, index=True)

    # Relacionamento: um estoque tem múltiplos produtos
    produtos = relationship("ProdutoModel", secondary="estoque_produtos", back_populates="estoques")


class EstoqueProdutoAssociation(BaseModel):
    """
    Tabela de associação para Estoque-Produto.

    Armazena a quantidade de cada produto em cada estoque.

    Attributes:
        estoque_id (int): FK para Estoque.
        produto_id (int): FK para Produto.
        quantidade (int): Quantidade do produto no estoque.
    """

    __tablename__ = "estoque_produtos"

    estoque_id = Column(Integer, ForeignKey("estoques.id"), primary_key=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"), primary_key=True)
    quantidade = Column(Integer, nullable=False, default=0)
