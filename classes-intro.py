class Cliente:
    def __init__(self, nome, altura, peso, vip=False):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.vip = vip
    
    def imc(self):
        return self.peso / (self.altura * self.altura)

