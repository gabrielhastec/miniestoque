
# MiniEstoque 🗃️

[![Python](https://img.shields.io/badge/python-3.7+-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-prot%C3%B3tipo-yellowgreen)](https://github.com/gabrielhastec/miniestoque)

**Mini framework em Python para controle de estoque com SQLite**.
Protótipo modular, ideal para integração em sistemas maiores, como sistemas de caixa.

---

## 🚀 Funcionalidades (Protótipo)

* Criação automática do banco SQLite
* Cadastro de produtos com validação de duplicidade, quantidade e preço
* Listagem de produtos
* Movimentações de entrada e saída de estoque
* Relatórios de produtos com estoque baixo
* Histórico de movimentações
* Estrutura modular e reutilizável
* Fácil integração com outros sistemas Python

---

## 🗂️ Estrutura do projeto

```
miniestoque/
│── miniestoque/      # Código principal do framework
│   │── __init__.py
│   │── database.py
│   │── estoque.py
│
│── examples/         # Exemplos de uso
│   │── main.py
│
│── tests/            # Testes automatizados
│   │── test_estoque.py
│
│── setup.py          # Configuração do pacote
│── requirements.txt  # Dependências
│── README.md         # Documentação
```

---

## 💻 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/gabrielhastec/miniestoque.git
cd miniestoque
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Instale o pacote localmente (opcional):

```bash
pip install -e .
```

---

## 🧪 Uso básico

```python
from miniestoque.estoque import cadastrar_produto, listar_produtos, registrar_entrada, registrar_saida

# Cadastrar produtos
cadastrar_produto("Arroz", 10, 25.90)
cadastrar_produto("Feijão", 5, 9.80)

# Registrar movimentações
registrar_entrada(1, 5)  # adiciona 5 unidades do produto com ID 1
registrar_saida(2, 2)    # remove 2 unidades do produto com ID 2

# Listar produtos cadastrados
for p in listar_produtos():
    print(p)

# Gerar relatórios
from miniestoque.estoque import relatorio_estoque_baixo, historico_movimentacoes

print(relatorio_estoque_baixo(limite=5))
print(historico_movimentacoes(1))
```

---

## 🧰 Testes

Para rodar os testes automatizados:

```bash
pytest tests/
```

---

## 📌 Observações

* Banco SQLite (`estoque.db`) é criado automaticamente dentro de `miniestoque/data/`.
* Pasta `data/` está ignorada no Git para evitar versionamento.
* Protótipo modular pronto para integração em sistemas maiores.
* Funcionalidades futuras: relatórios avançados, filtros, integração com interface gráfica ou sistemas de caixa.

---

## 🔗 Próximos passos

* Expandir movimentações e validações
* Relatórios detalhados de estoque baixo e histórico
* Integração como módulo reutilizável em sistemas de caixa
* Exemplos visuais e GIFs demonstrativos para README e LinkedIn
