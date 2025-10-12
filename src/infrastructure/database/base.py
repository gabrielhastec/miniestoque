"""
Modelo base para entidades ORM no banco de dados.

Fornece configurações comuns como tabela, timestamps e representação string.
Usado como herança para todos os models SQLAlchemy.
"""

from datetime import datetime
from typing import Any

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel(Base):
    """
    Classe base para models SQLAlchemy.

    Inclui colunas padrão: id, created_at, updated_at.

    Attributes:
        id (int): Chave primária auto-incremental.
        created_at (datetime): Timestamp de criação.
        updated_at (datetime): Timestamp de atualização.
    """

    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        """
        Representação string do modelo para depuração.

        Returns:
            str: String com ID e nome da classe.
        """
        return f"<{self.__class__.__name__}(id={self.id})>"

    def to_dict(self) -> dict[str, Any]:
        """
        Converte o modelo para dicionário.

        Returns:
            dict[str, Any]: Dados do modelo como dict (exclui colunas sensíveis).
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name != 'updated_at'}
        
    