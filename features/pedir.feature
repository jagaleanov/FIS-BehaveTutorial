Feature: pedir carta
    
    Como jugador quiero solicitar una carta adicional para seguir jugando.

Scenario: pedir
Given el turno de un jugador y una mano para jugar
When el jugador pide una carta
Then el repartidor le añade una carta a la mano

