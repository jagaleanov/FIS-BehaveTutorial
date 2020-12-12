# Tutorial Behave

Behave es un frameworks de pruebas basado en el estandar de Gherkin a través del cual se puede definir el comportamiento aplicaciones en python en texto plano.

## Instalación
Para la instalación se ejecuta desde la consola de comandos:

`pip install behave`

## Implementación
La implementación se lleva a cabo por medio de la descripción de comportamientos (features) y la secuencia de pasos (steps) para llevar a cabo determinado comportamiento dentro del programa.

Como ejemplo se realizará la implementación para un juego de naipes (Veintiuna) paso a paso.

### Descripción de comportamientos (features)
En la carpeta raiz del proyecto es necesario crear una carpeta llamada features en la cual se almacenan los archivos que contienen las descripciones. Un archivo pro cada comportamiento a evaluar. Estos archivos pueden tener cualquier nombre y deben tener la extension .feature.

Cada archivo o feature, contiene texto en formato natural que describe un comportamiento o parte de él a través de un escenario inicial **(Scenario)** con unas condiciones especificas dadas **(Given)**, un evento desencadenador **(When)** y un resultado esperado **(Then)**. Adicionalmente cada feature tiene un nombre y una breve descripción.

Las partes Given When y Then conforman los pasos que seran tomados en cuenta para realizar la prueba.

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
And la catidad de cartas es 52
</pre>

### Secuencia de pasos (steps)

