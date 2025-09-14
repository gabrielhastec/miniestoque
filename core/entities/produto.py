class Produto:
    def __init__(self, nome: str, quantidade: int, preco: float):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __repr__(self):
        return f"<Produto {self.nome} | Qtde: {self.quantidade} | Preço: R$ {self.preco:.2f}>"
