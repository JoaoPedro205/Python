class Veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    def descrever(self):
        return f"Veículo {self.marca} {self.modelo} e {self.ano} de {self.cor}"
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, num_portas):
        super().__init__(marca, modelo, ano, cor)
        self.num_portas = num_portas
    def descrever(self):
        return f"Carro de {self.marca} {self.modelo} {self.ano} de cor {self.cor} com {self.num_portas} portas"
    
carro = Carro('Ford', 'Fiesta', 2015, 'Azul', 4)
print(carro.descrever())

class Bicicleta(Veiculo):
    def __init__(self, marca, cor, num_marchas):
        super().__init__(marca, None, None, cor) 
        self.num_marchas = num_marchas
    
    def descrever(self):
        return f"Bicicleta {self.marca} de cor {self.cor} com {self.num_marchas} marchas"
    
bicicleta = Bicicleta('Caloi', 'Preta', 8)

print(bicicleta.descrever())