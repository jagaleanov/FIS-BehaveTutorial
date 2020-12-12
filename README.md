# Tutorial Behave

Behave es un frameworks de pruebas de aceptación basado en el estandar de Gherkin a través del cual se puede definir el comportamiento aplicacionesen lenguaje python utilizando el lenguaje natural.

## Instalación
Para la instalación ejecutaremos desde la consola de comandos:

`pip install behave`

## Implementación
La implementación se lleva a cabo por medio de la descripción de comportamientos (features) y la secuencia de pasos (steps) para llevar a cabo determinado comportamiento dentro del programa.

Como ejemplo se realizará la implementación para un juego de naipes (Veintiuna) paso a paso.

### Características de la prueba (features)
En la carpeta raiz del proyecto crearemos una carpeta llamada features en la cual se almacenan los archivos que contienen las descripciones de cada prueba. Un archivo por cada comportamiento a evaluar en uno o más escenarios. Estos archivos deben tener la extension **.feature**.

Cada archivo o feature, contiene texto en formato natural que describe un comportamiento o parte de él por medio de un escenario inicial **(Scenario)** con unas condiciones especificas dadas **(Given)**, un evento desencadenador **(When)** y un resultado esperado **(Then)**. Adicionalmente cada feature tiene un nombre y una descripción.

Las partes Given, When y Then conforman los pasos que seran tomados en cuenta para ejecutar la prueba.

**Scenario**: un nombre que identifica la prueba y su entorno inicial.

**Given**: describe el estado inicial del sistema.

**When**: describe un evento que produce un cambio de estado.

**Then**: describe el estado final que se espera del sistema.

#### Ejemplo
<pre>
Feature: barajar al inicio
    
    Como repartidor quiero barajar las cartas para iniciar el juego.

Scenario: barajar
Given un mazo para jugar 21
When el repartidor baraja el mazo
Then las cartas 5 y 10 no son iguales
</pre> 

También es posible utilizar las palabras reservadas **And** y **But** como pasos las cuales seran renombradas por behave a su paso predecesor.

### Secuencia de pasos (steps)
Los pasos utilizados en los escenarios se implementan en archivos de python y para almacenarlos se crea una nueva carpeta **steps** dentro de la carpeta features. Behave ejecutara todos los archivos incluidos en esta carpeta. 

Un archivo se relaciona con un archivo de características.






