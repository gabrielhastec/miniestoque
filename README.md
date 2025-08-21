
# 🗃️ MiniEstoque (WIP)

> **Status:** Em desenvolvimento (Versão 0.2)
> **Autor:** Gabriel Rodrigues
> **Data de Início:** 21/08/2025
> **Licença:** MIT (a ser adicionada)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![Licença](https://img.shields.io/badge/Licença-MIT-green)
![Versão](https://img.shields.io/badge/Versão-0.2-orange)

---

## 📑 Sumário

* [Descrição](#-descrição)
* [Objetivos](#-objetivos)
* [Funcionalidades](#-funcionalidades)

  * [Implementadas](#-implementadas)
  * [Planejadas](#-planejadas)
* [Estrutura do Projeto](#-estrutura-do-projeto)

  * [Estrutura de Dados](#-estrutura-de-dados)
  * [Funções Principais](#-funções-principais)
* [Como Executar](#-como-executar)
* [Como Usar](#-como-usar)
* [Limitações Atuais](#-limitações-atuais)
* [Contribuição](#-contribuição)
* [Licença](#-licença)
* [Contato](#-contato)

---

## 📖 Descrição

O **MiniEstoque** é um **mini framework em Python para controle de estoque** desenvolvido para ser integrado em sistemas maiores, como **sistemas de caixa**.

O projeto tem foco em **modularidade, simplicidade e boas práticas** (PEP 8 e PEP 257), permitindo fácil reutilização e expansão. Atualmente, funciona no console e possui roadmap para relatórios e integração com interfaces gráficas.

---

## 🎯 Objetivos

* Criar uma base modular para controle de estoque.
* Separar **lógica de estoque** da **lógica de negócio** do sistema principal.
* Permitir expansão para relatórios, consultas avançadas e integração com outros sistemas.
* Servir como projeto de portfólio, demonstrando boas práticas em Python.

---

## ✨ Funcionalidades

### ✅ Implementadas

* 🗂️ **Cadastro de produtos** — com validação de duplicidade, quantidade e preço.
* 🔄 **Movimentações de estoque** — entradas e saídas de produtos.
* 📊 **Relatórios simples** — produtos com estoque baixo e histórico de movimentações.
* 🧩 **Estrutura modular** — pode ser integrado em outros sistemas Python.
* 🧪 **Testes automatizados** — utilizando `pytest`.

### 🔜 Planejadas

* 💾 **Persistência avançada** — integração futura com banco de dados completo.
* 🖼️ **Interface gráfica** — integração com Tkinter ou web interface.
* 📈 **Relatórios avançados** — filtros e gráficos de estoque.
* 👥 **Gestão de usuários e permissões** — para acesso controlado.

---

## 🗂️ Estrutura do Projeto

```
miniestoque/
│
├── miniestoque/      # Código principal do framework
│   ├── __init__.py
│   ├── database.py
│   └── estoque.py
│
├── examples/         # Exemplos de uso
│   └── main.py
│
├── tests/            # Testes automatizados
│   └── test_estoque.py
│
├── setup.py          # Configuração do pacote
├── requirements.txt  # Dependências
└── README.md         # Documentação
```

### Estrutura de Dados

Produtos são armazenados no **SQLite**, dentro de `miniestoque/data/estoque.db`.

Tabela `produtos`:

| id | nome   | quantidade | preco |
| -- | ------ | ---------- | ----- |
| 1  | Arroz  | 10         | 25.90 |
| 2  | Feijão | 5          | 9.80  |

Tabela `movimentacoes`:

| id | produto\_id | tipo    | quantidade | data             |
| -- | ----------- | ------- | ---------- | ---------------- |
| 1  | 1           | entrada | 5          | 2025-08-21 11:00 |
| 2  | 2           | saida   | 2          | 2025-08-21 11:15 |

### Funções Principais

* **`cadastrar_produto(nome, quantidade, preco)`** → cadastra um produto no estoque.
* **`listar_produtos()`** → retorna a lista de produtos cadastrados.
* **`registrar_entrada(produto_id, quantidade)`** → adiciona unidades ao estoque.
* **`registrar_saida(produto_id, quantidade)`** → remove unidades do estoque, validando estoque suficiente.
* **`relatorio_estoque_baixo(limite)`** → retorna produtos com quantidade menor ou igual ao limite.
* **`historico_movimentacoes(produto_id)`** → retorna todas as movimentações de um produto.

---

## 🚀 Como Executar

### Pré-requisitos

* Python **3.8+**
* Dependências listadas em `requirements.txt`

### Passos

```bash
# 1. Clone o repositório
git clone https://github.com/gabrielhastec/miniestoque.git

# 2. Entre no diretório
cd miniestoque

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute o exemplo
python examples/main.py
```

---

## 📌 Como Usar

Exemplo básico:

```python
from miniestoque.estoque import cadastrar_produto, listar_produtos, registrar_entrada, registrar_saida
from miniestoque.estoque import relatorio_estoque_baixo, historico_movimentacoes

# Cadastro
cadastrar_produto("Arroz", 10, 25.90)
cadastrar_produto("Feijão", 5, 9.80)

# Movimentações
registrar_entrada(1, 5)
registrar_saida(2, 2)

# Consultas
print(listar_produtos())
print(relatorio_estoque_baixo(limite=5))
print(historico_movimentacoes(1))
```

---

## ⚠️ Limitações Atuais

* Banco em SQLite simples (sem usuários ou permissões).
* Apenas interface via console.
* Relatórios básicos (sem filtros avançados).
* Funcionalidades futuras de integração e interface gráfica ainda não implementadas.

---

## 🤝 Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature:

```bash
git checkout -b feature/nova-funcionalidade
```

3. Faça commits pequenos e descritivos:

```bash
git commit -m "Adiciona relatório de estoque baixo"
```

4. Envie sua branch:

```bash
git push origin feature/nova-funcionalidade
```

5. Abra um Pull Request.

---

## 📜 Licença

Distribuído sob a licença **MIT**.
Arquivo `LICENSE` será adicionado futuramente.

---

## 📧 Contato

* **Autor:** Gabriel Rodrigues
* **E-mail:** [gabrielhastec.dev@gmail.com](mailto:gabrielhastec.dev@gmail.com)
* **GitHub:** [gabrielhastec](https://github.com/gabrielhastec)
* **Localização:** Parnamirim - RN

⭐ Obrigado por conferir o **MiniEstoque**!
