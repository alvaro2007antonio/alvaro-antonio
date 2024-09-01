class Produto:
    def __init__(self, nome: str, preço: float, quantidade: int):
        self.__nome = nome
        self.__preço = preço
        self.__quantidade = quantidade

    def getNome(self) -> str:
        return self.__nome
    
    def getPreço(self) -> float:
        return self.__preço
    
    def getQuantidade(self) -> int:
        return self.__quantidade
    
    def setNome(self, nome: str):
        self.__nome = nome

    def setPreço(self, preço: float):
        self.__preço = preço

    def setQuantidade(self, quantidade: int):
        self.__quantidade = quantidade

    def __str__(self):
        return f"Produto(nome={self._nome}, preco={self._preco}, quantidade={self._quantidade})"
