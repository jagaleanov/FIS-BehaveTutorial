Feature: ganador

    se debe escoger entre dos manos de cartas la mano ganadora

    Scenario Outline: ganador
        Given 2 manos de <jugador> y <repartidor>
        When se evalua las manos
        Then se obtiene un <ganador>



            | jugador                                  | repartidor                                              | ganador    |
            | (5, treboles);(K, diamantes);(4 , picas) | (K, treboles);(A, diamantes);(A , picas);(k, corazones) | jugador    |
            | (9, treboles);(J, diamantes);(4 , picas) | (10, diamantes);(A , picas)                             | repartidor |
            | (K,diamantes);(Q, corazones);(A , picas) | (8, treboles);(K, corazones)                            | jugador    |
            | (K, treboles);(K, diamantes)             | (10, treboles);(5, picas);(6, diamantes)                | repartidor |