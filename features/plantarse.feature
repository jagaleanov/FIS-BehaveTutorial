Feature: plantarse
    
    Como jugador quiero plantarme para finalizar el turno.

Scenario: plantarse
Given el turno de un jugador
When el jugador se planta
Then el turno avanza

