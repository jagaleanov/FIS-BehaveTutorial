Feature: iniciar juego
    
    Como repartidor quiero barajar las cartas para iniciar el juego.
    Como repartidor quiero entregar 2 cartas a cada jugador para iniciar el juego.

Scenario: iniciar juego
Given el inicio de un juego de 21
Then las cartas 5 y 10 no son iguales
And la catidad de cartas es 52
And la mano del jugador se inicia con 2 cartas
And la mano del repartidor se inicia con 2 cartas
And es el turno del jugador

