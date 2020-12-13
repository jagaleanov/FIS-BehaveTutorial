from carta import Carta
from mano import Mano

class Main:
    def __init__(self):
        self.cartas = [Carta(x, y) for x in [str(z) for z in range(2,11)]+['A','J','Q','K'] for y in ['picas', 'treboles', 'diamantes', 'corazones']] 


    def dar_carta(self, posicion = 0):
        return self.cartas[posicion]
