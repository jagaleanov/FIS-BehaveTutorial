Feature: iniciar juego
    
    Como repartidor quiero entregar 2 cartas a cada jugador para iniciar el juego.

Scenario: iniciar juego
Given el inicio de un juego de 21
Then la mano del jugador se inicia con 2 cartas
And la mano del repartidor se inicia con 2 cartas
And es el turno del jugador

