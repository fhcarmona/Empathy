# AUTHOR: PERALTA GAMES
# SCOPE: BAR, PSIQUIATRA PERSEGUI O SERIAL KILLER

label scene_0008:
    scene black

    tln "13/05/2022 - 19:02h | BAR"

    # LIMPA A TELA E MOSTRA O AMBIENTE CONSULTORIO
    scene bar
    with dissolve

    $ narrative_image("bmn", right, None, bmn, "Aqui está sua [bebida]")
    $ narrative_image("psi", left, None, psi, "Muito obrigada, mas estou sem tempo, pode ficar com o troco.")
    $ narrative_image("bmn", right, None, bmn, "Agradecido, tenha uma boa noite")

    # PERSEGUE RUA
    scene street
    with dissolve

    play sound footsteps
    with Pause(2)

    stop sound

    # PERSEGUE BECO
    scene street-corner
    with dissolve

    play sound footsteps
    with Pause(2)

    stop sound

    # DESMAIA
    $ narrative_image("psi", left, None, psi, "Onde ele foi parar?")

    scene black

    play sound bonk
    with Pause(2)

    return
