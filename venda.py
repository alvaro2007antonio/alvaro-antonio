from produto import Produto
from typing import List

class Venda:
    def __init__(self, produtos: List[Produto], dataVenda: str):
        self._produtos = produtos
        self._dataVenda = dataVenda
        self._total = self.calcular_total()

    def get_produtos(self) -> List[Produto]:
        return self._produtos

    def get_dataVenda(self) -> str:
        return self._dataVenda

    def get_total(self) -> float:
        return self._total

    def set_produtos(self, produtos: List[Produto]):
        self._produtos = produtos
        self._total = self.calcular_total()

    def set_dataVenda(self, dataVenda: str):
        self._dataVenda = dataVenda

    def calcular_total(self) -> float:
        return sum(produto.get_preco() * produto.get_quantidade() for produto in self._produtos)

    def __str__(self):
        produtos_str = ', '.join(str(produto) for produto in self._produtos)
        return f"Venda(dataVenda={self._dataVenda}, total={self._total}, produtos=[{produtos_str}])"
