from behave import *
from mano import Mano
from carta import Carta

@given('una {mano} para sumar sus cartas')
def step(context, mano):
    context.cartas = []
    for t in mano.split(";"):
        valor, pinta = t[1:-1].split(",")
        context.cartas.append(Carta(valor, pinta))

    context.mano = Mano(context.cartas)

@when('el jugador suma la mano')
def step(context):
    context.valor = context.mano.evaluar()

@then('el {valor:d} es correcto')
def step(context, valor):
    assert context.valor == valor
