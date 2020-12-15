# Tutorial Behave (Virtual Studio Code)

Behave es un frameworks de pruebas de aceptación basado en el estandar de Gherkin a través del cual se puede definir el comportamiento aplicacionesen lenguaje python utilizando el lenguaje natural.

En este tutorial desarrollaremos un juego de 21 basado en las siguientes historias de usuario:

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
Para la instalación abriremos Virtual Studio Code e iniciaremos una nueva terminal (Ctrl + Shift + ñ).
En ella ejecutaremos el comando:

`pip install behave`

## Implementación
La implementación se lleva a cabo por medio de la descripción de comportamientos (features) y la secuencia de pasos (steps) para llevar a cabo determinado comportamiento dentro del programa.

La idea es desarrollar cada requerimiento uno a la vez por lo cual realizaremos un feature y lo daremos por terminado cuando su funcionamiento este completo y correcto.

### Características de la prueba (features)
En la carpeta raiz del proyecto crearemos una carpeta llamada features en la cual se almacenan los archivos que contienen las descripciones de cada prueba. Un archivo por cada comportamiento a evaluar en uno o más escenarios. Estos archivos deben tener la extension **.feature**.

Cada archivo o feature, contiene texto en formato natural que describe un comportamiento o parte de él por medio de un escenario inicial **(Scenario)** con unas condiciones especificas dadas **(Given)**, un evento desencadenador **(When)** y un resultado esperado **(Then)**. Adicionalmente cada feature tiene un nombre y una descripción.

Las partes Given, When y Then conforman los pasos que seran tomados en cuenta para ejecutar la prueba.

**Scenario**: un nombre que identifica la prueba y su entorno inicial.

**Given**: describe el estado inicial del sistema.

**When**: describe un evento que produce un cambio de estado.

**Then**: describe el estado final que se espera del sistema.

También es posible utilizar las palabras reservadas **And** y **But** como pasos las cuales seran renombradas por behave con el nombre del paso anterior.

Para la primera historia crearemos un feature segun el cual, al iniciar el juego, las cartas deben ser barajadas aleatoriamente. Comprobaremos esto comparando 2 cartas del mazo y el número total de cartas.

<pre>
Feature: iniciar juego
    
    Como repartidor quiero barajar las cartas para iniciar el juego.

Scenario: iniciar juego
Given el inicio de un juego de 21
Then las cartas 5 y 10 no son iguales
And la catidad de cartas es 52
</pre> 

### Secuencia de pasos (steps)
Los pasos utilizados en los escenarios se implementan en archivos de python y para almacenarlos se crea una nueva carpeta **steps** dentro de la carpeta features. Behave ejecutara todos los archivos incluidos en esta carpeta. 

Un archivo de pasos se relaciona con un archivo de características.

Primero importaremos los archivos necesarios para ejecutar behave y para ejecutar la prueba:
<pre>
from behave import *
from mazo import Mazo
</pre> 

Luego, por cada paso en el archivo de características (Given,When,Then,And,But) crearemos un decorador que será utilizado por behave para relacionar el paso al escenario que corresponde. 

No olvide que las palabras reservadas AND y BUT se sobreescriben a sus pasos anteriores, en esta caso como AND esta siguiente a THEN sera analizado como otra linea de THEN

<pre>
@given('un mazo para jugar 21')

@when('el repartidor baraja el mazo')

@then('las cartas 5 y 10 no son iguales')

@then('la catidad de cartas es 52')
</pre>




