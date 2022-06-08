# CamelCase
class Carro:
    """Representa um carro."""

    # método construtor
    def __init__(self, modelo, motor, cor):
        self.modelo = modelo
        self.motor = motor
        self.cor = cor
        self.velocidade = 0
        self.ligado = False

    # o método __repr__ sempre tem que retornar uma string
    def __repr__(self):
        print("Exibindo informações do carro:")
        return " ".join([self.modelo, self.motor, self.cor])

    def ligar(self):
        """Liga o carro."""
        print(f"O carro {self} está ligado.")
        self.ligado = True

    def desligar(self):
        """Desliga o carro."""
        print(f"O carro {self.modelo} está desligado.")
        self.ligado = False

    def acelerar(self, velocidade_atingida):
        """Acelera o carro até uma velocidade."""
        if self.ligado:
            self.velocidade = velocidade_atingida
            print(f"Acelerou o carro {self.modelo} até {velocidade_atingida}km/h.")
        else:
            print(f"Carro {self.modelo} está desligado!")

carro_novo = Carro("monza", "v6", "azul")

print(carro_novo.modelo)
print(carro_novo.cor)
print(carro_novo.ligado)
carro_novo.acelerar(50)
carro_novo.ligar()
print(carro_novo.velocidade)
carro_novo.acelerar(90)
print(carro_novo.ligado)
print(carro_novo.velocidade)
carro_novo.desligar()
print(carro_novo.ligado)

outro_carro = Carro("gol", "v8", "preto")

print(outro_carro.modelo)
print(outro_carro)

print(carro_novo)
