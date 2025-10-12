"""
Subpacote para configurações compartilhadas.

Carrega settings via Pydantic, suportando env vars e arquivos .env.
"""

from .settings import Settings

__all__ = ["Settings"]
