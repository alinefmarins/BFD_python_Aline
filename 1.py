# 1 - Construa uma classe para armazenar informações de carros, cada objeto instanciado por essa classe deve ter os seguintes atributos:

class Carro:

#  A - Modelo, marca, ano de lançamento, potência (1.0,1.6,etc), tipo de câmbio (manual ou automático), preço no lançamento.   

    def __init__(self, modelo, marca, ano_de_lancamento, potencia, tipo_de_cambio, preco_no_lancamento):
        self.modelo = modelo
        self.marca = marca
        self.ano_de_lancamento = ano_de_lancamento
        self.potencia = potencia
        self.tipo_de_cambio = tipo_de_cambio
        self.preco_no_lancamento = preco_no_lancamento


# B - Crie um método para retornar cada atributo.

    def exibir_modelo(self):
        return self.modelo

    def exibir_marca(self):
        return self.marca

    def exibir_ano_de_lancamento(self):
        return self.ano_de_lancamento

    def exibir_potencia(self):
        return self.potencia

    def exibir_tipo_de_cambio(self):
        return self.tipo_de_cambio

    def exibir_preco_no_lancamento(self):
        return self.preco_no_lancamento

# Crie ao menos 3 instâncias de objeto, 

carro1 = Carro("Civic", "Honda", 2020, 2.0, "Automático", 45000.00)
carro2 = Carro("Gol", "Volkswagen", 2009, 1.6, "Manual", 20000.00)
carro3 = Carro("Corolla", "Toyota", 2022, 2.0, "Automático", 50000.00)

# e execute todos os métodos para teste. 

print("Informações do carro:")
print("Modelo:", carro1.exibir_modelo())
print("Marca:", carro1.exibir_marca())
print("Ano:", carro1.exibir_ano_de_lancamento())
print("Potência:", carro1.exibir_potencia())
print("Câmbio:", carro1.exibir_tipo_de_cambio())
print("Preço:", carro1.exibir_preco_no_lancamento())