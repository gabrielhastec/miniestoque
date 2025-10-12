"""
Pacote shared para elementos comuns no core.

Contém configurações (settings) e utilitários (utils) compartilhados entre bounded contexts.
Não contém lógica de domínio ou aplicação específica.

Exemplos de uso:
    from src.core.shared.config.settings import Settings
    from src.core.shared.utils.helpers import formatar_moeda
"""

from .config.settings import Settings
from .utils.helpers import formatar_moeda, validar_id_positivo

__all__ = [
    "Settings",
    "formatar_moeda",
    "validar_id_positivo",
]
