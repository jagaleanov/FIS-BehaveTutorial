# Tutorial Behave (Virtual Studio Code)

Behave es un framework para realizar pruebas de aceptación para Python basado en el estandar de Gherkin que permite definir el comportamiento de aplicaciones en lenguaje de programación utilizando el lenguaje natural.

En este tutorial desarrollaremos un programa basado en el juego de cartas llamado 21 o Black Jack a partir de las siguientes historias de usuario:

## Historias de usuario juego 21
**Estructura:**

Como **ROL** quiero **ACCIÓN** para **FUNCIONALIDAD**

- Como repartidor quiero barajar las cartas para iniciar el juego. (iniciar)
- Como repartidor quiero entregar 2 cartas para iniciar el juego. (iniciar)
- Como jugador quiero determinar el valor de una carta para determinar el valor de la mano. (carta)
- Como jugador quiero determinar el valor de la mano para seguir jugando. (mano)
- Como jugador quiero solicitar una carta adicional para seguir jugando. (pedir)
- Como jugador quiero plantarme para finalizar el turno. (plantarse)
- Como repartidor quiero saber el valor de las manos para determinar quién gana. (ganador)


## Instalación
Para la instalación de Behave abriremos Virtual Studio Code e iniciaremos una nueva terminal (Ctrl + Shift + ñ)y en ella ejecutaremos el comando:

`pip install behave`

## Para empezar
La implementación se lleva a cabo por medio de la descripción de comportamientos (features) y la secuencia de pasos (steps) para cumplir con cada historia de usuario.

La idea es desarrollar cada historia de usuario una por una, por lo cual realizaremos un feature y lo daremos por terminado cuando sus pasos esten completos y su funcionamiento sea correcto.

### Anatomía de los features
En la carpeta raiz del proyecto crearemos un directorio llamado features en el cual almacenaremos los archivos que contienen una historia de usuario a evaluar en uno o más escenarios y las descripciones de cada prueba. Estos archivos deben tener la extension **.feature**.

Cada archivo o feature contiene un nombre, una historia de usuario y un texto en formato natural que describe un comportamiento o parte de él por medio de un escenario inicial **(Scenario)** con unas condiciones especificas dadas **(Given)**, un evento desencadenador **(When)** y un resultado esperado **(Then)**.

Las partes Given, When y Then identifican los pasos para ejecutar la prueba.

**Scenario**: un nombre que identifica la prueba y su entorno inicial.

**Given**: describe el estado inicial del sistema.

**When**: describe un evento que produce un cambio de estado.

**Then**: describe el estado final que se espera del sistema.

También es posible utilizar las palabras reservadas **And** y **But** como pasos las cuales seran renombradas por behave con el nombre del paso anterior.

### Anatomía de los Steps
Los pasos utilizados en los escenarios se implementan en archivos de Python y para almacenarlos se crea un nuevo directorio **steps** dentro de la carpeta features. Behave ejecutara todos los archivos incluidos en esta carpeta. 

Un archivo de Steps se relaciona con un archivo de Features.


### Construcción de un feature
Para la primera historia crearemos un feature segun el cual, al iniciar el juego, las cartas deben ser barajadas aleatoriamente. Comprobaremos esto comparando 2 cartas del mazo y el número total de cartas.

<pre>
Feature: iniciar juego
    
    Como repartidor quiero barajar las cartas para iniciar el juego.

Scenario: iniciar juego
Given el inicio de un juego de 21
Then las cartas 5 y 10 no son iguales
And la catidad de cartas es 52
</pre> 




### Construcción de los steps para un feature
Primero importaremos los archivos necesarios para ejecutar behave:

`from behave import *`

Luego, por cada paso en el archivo de características (Given, When, Then, And, But) crearemos un decorador que será utilizado por behave para relacionar el paso al escenario que corresponde. 

No olvide que las palabras reservadas **And** y **But** se sobreescriben a sus pasos anteriores, en esta caso, como **And** esta siguiente a **Then** sera analizado como otra linea de **Then**

<pre>
@given('un mazo para jugar 21')

@when('el repartidor baraja el mazo')

@then('las cartas 5 y 10 no son iguales')

@then('la catidad de cartas es 52')
</pre>

Ahora, cada uno de estos decoradores va asociado a una funcion de implementación que recibe como parametro un contexto y que se encargara de realizar proceso a llevar a cabo en cada paso:

<pre>
@given('un mazo para jugar 21')
def implementacion(context):

@when('el repartidor baraja el mazo')
def implementacion(context):

@then('las cartas 5 y 10 no son iguales')
def implementacion(context):

@then('la catidad de cartas es 52')
def implementacion(context):
</pre>

Consecuentemente con lo anterior se debe realizar una comprobacion con la palabra reservada **assert** y la variable de **context** servira como una extencion de la prueva n el momento de ejecucion creando un banco de informacion mutable en el momento de trabajo

**Implementacion de *context* para el manejo de informacion**
<pre>
@given('un mazo para jugar 21')
def implementacion(context):
    context.mazo = Mazo()

@when('el repartidor baraja el mazo')
def implementacion(context):
    context.mazo.barajar()
</pre>


**Comprobacion de la informacion añadida al contexto de la iteracion presente**
<pre>

@then('las cartas 5 y 10 no son iguales')
def implementacion(context):
    assert not context.mazo.dar_carta(5).son_iguales(context.mazo.dar_carta(10))

@then('la catidad de cartas es 52')
def implementacion(context):
    assert  len(context.mazo.cartas) == 52
</pre>

### Traspaso de informacion desde un feature

De igual forma nos podemos encontrar con que debemos evaluar un caso de prueva especifico, y debemos transportar informacion desde el <strong> feature </strong>  en este caso existen dos opciones, un **scenario** y un **scenario outline**, en el primero de estos analizar funciones que no deban tener un constructor con recibimiento de parametros, y en el segundo, se dan multiples casos de prueva. 

####  Scenario

En este caso se optienen los datos de forma directa en la escritura del scenario y se espera la comprobacion de forma directa desde los propios metodos de respuesta y retorno logicos en el momento.


<b>Feature</b>
<pre>
Feature: iniciar juego
    
    Como repartidor quiero entregar 2 cartas a cada jugador para iniciar el juego.

Scenario: iniciar juego
Given el inicio de un juego de 21
Then la mano del jugador se inicia con 2 cartas
And la mano del repartidor se inicia con 2 cartas
And es el turno del jugador
</pre>

La informacion se espera optener directamente desde la ejecucion añadiendose al contexto.

<b>Steps</b>
<pre> 
from behave import *
from juego import Juego

@given('el inicio de un juego de 21')
def implementacion(context):
    context.juego = Juego()

@then('la mano del jugador se inicia con 2 cartas')
def implementacion(context):
    assert len(context.juego.mano_jugador.cartas) == 2

@then('la mano del repartidor se inicia con 2 cartas')
def implementacion(context):
    assert len(context.juego.mano_repartidor.cartas) == 2

@then('es el turno del jugador')
def implementacion(context):
    assert context.juego.turno == 1
</pre>

La informacion se corrobora con un **assert** evaluado directamente sobre la ejecucion igualado a condiciones particulares tales como un numero o un string


#### Scenario outline

En el **Scenario outline** se espera poder pasar parametros de ejecucion especificos de estados tambien especificos en un momento intermedio de la ejecucion, tal como en este caso seria la evaluacion de un ganador de una partida de 21, para esto es imposible generar toda la ejecucion desde el inicio para ejecutar pruevas que presenten granularidad entre ellas sin ningun tipo de interdependencia de las mismas, por lo tanto la informacion debe ser introducida solamente en el proceso de evaluacion sin tener en cuenta el proceso anterior de la ejecucion. Tomaremos como ejemplo el escenario planteado con los siguientes casos de prueva


***
| jugador                                  | repartidor                                              | ganador    |
| ---------------------------------------- | --------------------------------------------------------|------------|
| (5, treboles);(K, diamantes);(4 , picas) | (K, treboles);(A, diamantes);(A , picas);(k, corazones) | jugador    |
| (9, treboles);(J, diamantes);(4 , picas) | (10, diamantes);(A , picas)                             | repartidor |
| (K,diamantes);(Q, corazones);(A , picas) | (8, treboles);(K, corazones)                            | jugador    |
| (K, treboles);(K, diamantes)             | (10, treboles);(5, picas);(6, diamantes)                | repartidor |
***


En la tabla se puede ver la cantidad de casos de prueva que se ejecutara funcionando como un ciclo forEach para cada caso de prueva se ejecutara el *Step* correspondiente tantas veces como casos de prueva.

El feature debe contener una tabla descrita de manera rapida con la referencia a las variables planteadas en las lineas especificas, en este caso es **Given** y **Then** en donde se especifican las variables a travez de las etiquetas  < ganador >, < jugador > y < repartidor > y el valor de estas en cada iteracion en la tabla descrita posteriormente, es importante recordar que en el archivo ***Step*** correspondiente la variables se exportaran de manera particular como *String*.

<pre>
Feature: ganador

    se debe escoger entre dos manos de cartas la mano ganadora

    Scenario Outline: ganador
        Given 2 manos de < jugador > y < repartidor >
        When se evalua las manos
        Then se obtiene un < ganador >



        | jugador                                  | repartidor                                              | ganador    |
        | (5, treboles);(K, diamantes);(4 , picas) | (K, treboles);(A, diamantes);(A , picas);(k, corazones) | jugador    |
        | (9, treboles);(J, diamantes);(4 , picas) | (10, diamantes);(A , picas)                             | repartidor |
        | (K,diamantes);(Q, corazones);(A , picas) | (8, treboles);(K, corazones)                            | jugador    |
        | (K, treboles);(K, diamantes)             | (10, treboles);(5, picas);(6, diamantes)                | repartidor |
</pre>


Luego en el ***Step*** pertinente se obtendra la pomprobacion pertienente de cada caso.

<pre>
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

</pre>

En algunos casos concretos se debe utilizar logica para guiar el procedimiento en especifico para emular cierta parte de la ejecucion del programa con tal de asegurar que el modulo en especifico funciones de manera correcta.