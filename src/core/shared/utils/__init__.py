"""
Subpacote para utilitários compartilhados.

Funções genéricas para validação, formatação e helpers comuns.
Expanda em sub-arquivos como validators.py se necessário.
"""

from .helpers import formatar_moeda, validar_id_positivo

__all__ = ["formatar_moeda", "validar_id_positivo"]
