from behave import *
from juego import Juego


@given('el inicio del juego')
def implementacion(context):
    context.juego = Juego()

@then('la mano del jugador se inicia con 2 cartas')
def implementacion(context):
    assert  len(context.juego.mano_jugador.cartas) == 2
    

@then('la mano del repartidor se inicia con 2 cartas')
def implementacion(context):
    assert  len(context.juego.mano_repartidor.cartas) == 2