# AUTHOR: PERALTA GAMES
# SCOPE: BAR, PSIQUIATRA PERSEGUI O SERIAL KILLER

label scene_0008:
    scene black

    tln "13/05/2022 - 19:02h | BAR"

    # LIMPA A TELA E MOSTRA O AMBIENTE CONSULTORIO
    scene bar
    with dissolve

    $ narrative_image("bmn", right, None, bmn, "Aqui está sua [bebida]") # bmn "Aqui está sua [bebida]"
    $ narrative_image("psi", left, None, psi, "Muito obrigada, pode ficar com o troco.") # psi "Muito obrigada, pode ficar com o troco."

    pause 2

    scene street
    with dissolve

    pause 2

    scene street-corner
    with dissolve
    with Pause(2)

    scene black
    with Pause(3)

    return
