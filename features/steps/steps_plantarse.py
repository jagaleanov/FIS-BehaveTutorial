from behave import *
from juego import Juego

@given('un juego de 21 y el turno de jugador')
def implementacion(context):
    context.juego = Juego()

@when('el jugador se planta')
def implementacion(context):
    context.juego.plantarse()

@then('el turno avanza')
def implementacion(context):
    assert context.juego.turno == 2