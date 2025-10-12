"""
Gerenciador de sessão para o banco de dados.

Fornece factory para sessões SQLAlchemy, configurável via engine e settings.
Usado em repositórios para transações.
"""

from contextlib import contextmanager
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.core.shared.config.settings import Settings  # Assuma settings.py em shared

def get_engine(settings: Optional[Settings] = None) -> Any:
    """
    Cria o engine SQLAlchemy baseado em configurações.

    Args:
        settings (Optional[Settings]): Configurações do app (DB URL).

    Returns:
        Any: Engine SQLAlchemy (de sqlalchemy.engine).
    """
    if settings is None:
        settings = Settings()
    return create_engine(settings.database_url, echo=settings.debug)

@contextmanager
def get_session(engine: Optional[Any] = None, expire_on_commit: bool = False) -> Session:
    """
    Context manager para sessões DB.

    Args:
        engine (Optional[Any]): Engine SQLAlchemy (default: cria novo).
        expire_on_commit (bool): Expira objetos após commit.

    Yields:
        Session: Sessão ativa para uso em with-block.

    Raises:
        Exception: Para erros de conexão ou transação.
    """
    if engine is None:
        engine = get_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=expire_on_commit)
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def get_db() -> Any:
    """
    Dependency para FastAPI/CLI: retorna gerador de sessões.

    Returns:
        Any: Função geradora para sessões (yield Session).
    """
    def _get_db():
        with get_session() as session:
            yield session
    return _get_db
