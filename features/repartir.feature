Feature: repartir al inicio
    
    Como repartidor quiero entregar 2 cartas a cada jugador para iniciar el juego.

Scenario: repartir
Given un mazo para jugar 21 y un numero de jugadores
When el repartidor inicia la partida
Then cada jugador recibe 2 cartas

