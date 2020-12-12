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

Cada archivo o feature, contiene texto en formato natural que describe un comportamiento o parte de él a través de un escenario inicial con unas condiciones especificas dadas (Given), un evento desencadenador (When) y una consecuencia esperada (Then). Adicionalmente cada feature tiene un titulo y una breve descripción.

#### Ejemplo
<pre>
Feature: Carta del 21

Como jugador quiero determinar el valor de una carta para determinar el valor de la mano.
Scenario Outline: determinar valor carta
Given una <carta> para saber su valor
When el jugador quiere saber su valor
Then el <valor> de la carta es correcto

Examples:
    | carta | valor | 
    | 2, picas  | 2  |
    | A, corazones  | 1  |
    | 8, treboles  | 8  |
    | J, picas  | 10  |
    | Q, picas  | 10  |
    | K, picas  | 10  |
</pre>   

### Secuencia de pasos (steps)

