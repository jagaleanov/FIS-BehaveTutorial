from behave import *
from juego import Juego

@given('el inicio de un juego de 21 y una mano de jugador con un número de cartas')
def implementacion(context):
    context.juego = Juego()
    context.numero_cartas = len(context.juego.mano_jugador.cartas)

@when('el usuario pide una carta')
def implementacion(context):
    context.juego.pedir()

@then('hay una nueva carta en la mano')
def implementacion(context):
    assert len(context.juego.mano_jugador.cartas) == context.numero_cartas + 1