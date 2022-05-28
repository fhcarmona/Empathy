# AUTHOR: PERALTA GAMES
# SCOPE: PORAO, PSIQUIATRA PRESA NO PORAO

label scene_0009:
    scene black

    tln "13/05/2022 - 20:16h | LOCAL DESCONHECIDO"

    # LIMPA A TELA E MOSTRA O AMBIENTE DO PORAO
    scene basement
    with dissolve

    $ narrative_image("psi sad", left, None, psi, "Que dor de cabeça") # psi "Que dor de cabeça"
    $ narrative_image("psi sad", left, None, psi, "Onde estou?") # psi "Onde estou?"

    scene black
    with Pause(2)

    return
