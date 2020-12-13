from behave import *

class Turno:

    def __init__(self):
        self.turno_de_jugador = True

    def plantarse(self):
        self.turno_de_jugador = False
        