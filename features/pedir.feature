Feature: pedir carta
    
    Como jugador quiero solicitar una carta adicional para seguir jugando.

Scenario: pedir
Given el inicio de un juego de 21 y una mano de jugador con un número de cartas
When el usuario pide una carta
Then hay una nueva carta en la mano


