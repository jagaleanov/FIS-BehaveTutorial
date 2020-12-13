from behave import *
from mazo import Mazo
from mano import Mano


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

        self.contador_cartas = 4

        self.mano_jugador = Mano(self.cartas_jugador)
        self.mano_repartidor = Mano(self.cartas_repartidor)
        self.turno = 1

    def pedir(self):
        self.mano_jugador.ingresar_carta(self.mazo.dar_carta(self.contador_cartas))
        self.contador_cartas = self.contador_cartas +1

    def plantarse(self):
        self.turno = 2
    


