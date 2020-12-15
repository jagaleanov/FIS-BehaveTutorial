from behave import *
from mano import Mano


@given("2 manos de {jugador} y {repartidor}")
def step(context, jugador, repartidor):
    context.jugadorCar = []
    context.repartidorCar = []
    for t in jugador.split(";"):
        valor, pinta = t[1:-1].split(",")
        context.jugadorCar.append(Carta(valor, pinta))
    context.jugador = Mano(context.cartas)

    for t in repartidor.split(";"):
        valor, pinta = t[1:-1].split(",")
        context.repartidorCar.append(Carta(valor, pinta))
    context.repartidor = Mano(context.cartas)


@when("se evalua las manos")
def step(context):
    context.valorJugador = context.jugador.evaluar()
    context.valorRepartidor = context.repartidor.evaluar()


@then("se obtiene un {ganador}")
def step(context, ganador):
    if context.valorJugador > context.valorRepartidor:
        context.ganador = "jugador"
    else:
        context.ganador = "repartidor"
    assert context.ganador == ganador
