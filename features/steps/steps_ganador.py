from behave import *
from mano import Mano

@given('varias {manos} para sumar sus cartas')
def step(context, manos):
    context.manos = Mano(mano.split("-"))

@when('el repartidor quiere saber el valor de las manos')
def step(context):
    #por cada elemento evaluar

@then('el {ganador:d} es correcto')
def step(context, ganador):
    assert context.ganador == ganador
