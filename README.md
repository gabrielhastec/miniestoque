
# MiniEstoque 🗃️

[![Python](https://img.shields.io/badge/python-3.7+-blue)](https://www.python.org/)  
[![Status](https://img.shields.io/badge/status-prot%C3%B3tipo-yellowgreen)](https://github.com/SEU_USUARIO/miniestoque)

**Mini framework em Python para controle de estoque com SQLite**.  
Protótipo modular, ideal para integração em sistemas maiores como sistemas de caixa.

---

## 🚀 Funcionalidades (protótipo)
- Criação automática do banco SQLite
- Cadastro de produtos
- Listagem de produtos
- Estrutura modular e reutilizável
- Fácil integração com outros sistemas Python

---

## 🗂️ Estrutura do projeto
```

miniestoque/
│── miniestoque/      # Código principal do framework
│   │── **init**.py
│   │── database.py
│   │── estoque.py
│
│── examples/         # Exemplos de uso
│   │── main.py
│
│── tests/            # Testes automatizados
│   │── test\_estoque.py
│
│── setup.py          # Configuração do pacote
│── requirements.txt  # Dependências
│── README.md         # Documentação

````

---

## 💻 Instalação

1. Clone o repositório:
```bash
git clone <URL_DO_REPOSITORIO>
cd miniestoque
````

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
from miniestoque.estoque import cadastrar_produto, listar_produtos

# Cadastrar produtos
cadastrar_produto("Arroz", 10, 25.90)
cadastrar_produto("Feijão", 5, 9.80)

# Listar produtos cadastrados
for p in listar_produtos():
    print(p)
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

---

## 🔗 Próximos passos

* Movimentações de entrada e saída de estoque
* Relatórios de produtos com estoque baixo
* Histórico de movimentações e consultas avançadas

```

---
