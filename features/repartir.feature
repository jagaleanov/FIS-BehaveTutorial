Feature: repartir al inicio
    
    Como repartidor quiero entregar 2 cartas a cada jugador para iniciar el juego.

Scenario: repartir
Given el inicio del juego
Then la mano del jugador se inicia con 2 cartas
And la mano del repartidor se inicia con 2 cartas

