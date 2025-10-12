"""
Utilitários genéricos para o core.

Contém funções para formatação de dados (ex.: moeda) e validações comuns.
Não depende de domínio específico; use em services ou use cases.

Exemplos:
    preco_formatado = formatar_moeda(10.5)  # 'R$ 10,50'
    validar_id_positivo(1)  # OK
"""

from decimal import Decimal
from typing import Union

from src.core.shared.config.settings import Settings

def formatar_moeda(valor: Union[float, Decimal], locale: str = "pt_BR") -> str:
    """
    Formata um valor numérico como moeda brasileira (R$).

    Args:
        valor (Union[float, Decimal]): Valor a formatar.
        locale (str): Locale para formatação (default: pt_BR).

    Returns:
        str: Valor formatado (ex.: 'R$ 10,50').

    Raises:
        ValueError: Se valor for negativo ou inválido.
    """
    if valor < 0:
        raise ValueError("Valor não pode ser negativo para formatação de moeda.")
    from locale import setlocale, LC_ALL, format_string, currency
    
    # Configura locale para formatação
    try:
        setlocale(LC_ALL, (locale, 'UTF-8'))
        return currency(valor, grouping=True, symbol=True)
    except locale.Error:
        # Fallback simples se locale falhar
        return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def validar_id_positivo(id_valor: int) -> int:
    """
    Valida se um ID é positivo e inteiro.

    Args:
        id_valor (int): ID a validar.

    Returns:
        int: O ID validado.

    Raises:
        ValueError: Se ID <= 0.
    """
    if id_valor <= 0:
        raise ValueError("ID deve ser um inteiro positivo.")
    return id_valor

def get_settings() -> Settings:
    """
    Retorna instância de Settings singleton-like.

    Returns:
        Settings: Configurações carregadas.
    """
    return Settings()
