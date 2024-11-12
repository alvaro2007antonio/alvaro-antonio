import Venda

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        self.__preco = preco

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade

    def exibirProduto(self):
        print(f"Nome: {self.__nome}, Preço: {self.__preco}, Quantidade: {self.__quantidade}")

    def to_dict(self):
        return{
            "nome": self.__nome,
            "preco": self.__preco,
            "quantidade": self.__quantidade
            }

    @classmethod
    def from_dict(cls, dados):
        return cls(dados['nome'], Venda.from_dict(dados['preço']), dados['quantidade'])