from behave import *
from mazo import Mazo
from mano import Mano
from turno import Turno

class Juego:

    def __init__(self):
        self.mazo = Mazo()
        self.mazo.barajar()

        self.cartas_jugador = []
        self.cartas_repartidor = []

        self.cartas_jugador.append(self.mazo.dar_carta(0))
        self.cartas_jugador.append(self.mazo.dar_carta(1))
        self.cartas_repartidor.append(self.mazo.dar_carta(2))
        self.cartas_repartidor.append(self.mazo.dar_carta(3))
        print(self.cartas_jugador)
        print(self.cartas_repartidor)

        self.mano_jugador = Mano(self.cartas_jugador)
        self.mano_repartidor = Mano(self.cartas_repartidor)
        self.turno = Turno()


juego = Juego()