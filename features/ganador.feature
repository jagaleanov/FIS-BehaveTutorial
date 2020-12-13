Feature: ganador del 21

    Como repartidor quiero saber el valor de las manos para determinar quién gana. 

Scenario Outline: valor de las mano
Given varias <manos> para sumar sus cartas
When el repartidor quiere saber el valor de las manos
Then el <ganador> es correcto

Examples:
    | manos | ganador |
    | (5, picas);(J, treboles)-(A, picas);(A, treboles);(A, diamantes);(Q, picas)-(A, diamantes);(J, treboles) | 3 | 
    | (5, picas);(J, treboles)-(A, picas);(A, treboles);(A, diamantes);(Q, picas)                              | 1 | 
    | (3, diamantes);(Q, picas)-(5, picas);(J, treboles);(3, treboles)                                         | 2 | 
    
