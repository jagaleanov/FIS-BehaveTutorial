from carta import Carta

class Mano:

    def __init__(self, cartas):
        self.cartas = cartas

    def evaluar(self):
        valor = 0
        for c in self.cartas:
            valor += c.evaluar()
        if self.tiene_a() and valor <= 11:
            valor += 10
        return valor

    def tiene_a(self):
        for c in self.cartas:
            if c.evaluar() == 1:
                return True
        return False

    def ingresar_carta(self,valor,pinta):
        self.cartas.append(Carta(valor, pinta))
        