"""
Script de configuração do pacote MiniEstoque.

Utiliza setuptools para empacotar e instalar o framework.
"""

from setuptools import setup, find_packages

setup(
    name="miniestoque",
    version="0.1.0",
    description="Mini framework de controle de estoque em Python com SQLite",
    author="Gabriel Rodrigues",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.7",
)
