from behave import *
from mano import Mano

@given('el turno de un jugador y una mano para jugar')
def implementacion(context):
    context.mano = Mano()

@when('el jugador pide una carta')
def implementacion(context):

@then('el repartidor le añade una carta a la mano')
def implementacion(context):