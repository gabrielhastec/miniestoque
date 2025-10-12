"""
Configurações globais do aplicação.

Usa Pydantic para validação e carregamento de variáveis de ambiente.
Suporta modos debug, database_url e outros.

Exemplos:
    settings = Settings()
    db_url = settings.database_url
"""

from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Classe de configurações com validação Pydantic.

    Carrega de env vars (prefixo 'APP_') ou .env. Suporta campos como database_url e debug.

    Attributes:
        database_url (str): URL de conexão com o banco (default: SQLite para testes).
        debug (bool): Modo debug (logs verbosos).
        secret_key (Optional[str]): Chave secreta para auth (opcional).
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        case_sensitive=False,
    )

    # Configurações
    database_url: str = "sqlite:///./miniestoque.db"
    debug: bool = False
    secret_key: Optional[str] = None

    @property
    def is_production(self) -> bool:
        """
        Verifica se está em modo produção.

        Returns:
            bool: True se debug=False.
        """
        return not self.debug
    