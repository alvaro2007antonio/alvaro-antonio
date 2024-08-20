class Carro:
    def __init__(self):
        self.modelo = ""
        self.marca = ""
        self.ano = ""


carro1 = Carro()
carro1.modelo = "Voyage"
carro1.marca = "Volkswagen"
carro1.ano = "2015"


carro2 = Carro()
carro2.modelo = "Ford Ka"
carro2.marca = "Ford"
carro2.ano = "2018"


print(f'O carro 1 é da marca {carro1.marca} e o carro 2 é um modelo {carro2.modelo}')
print(f'Agora o modelo do carro 1 é um {carro1.modelo}')