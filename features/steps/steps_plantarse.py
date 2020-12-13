from behave import *
from turno import Turno 

@given('el turno de jugador')
def implementacion(context):
    context.turno = Turno()

@when('el jugador se planta')
def implementacion(context):
    context.turno.plantarse()

@then('el turno avanza')
def implementacion(context):
    assert context.turno.turno_de_jugador == False