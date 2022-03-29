# AUTHOR: PERALTA GAMES
# SCOPE: VISITA DOS INVESTIGADORES AO CONSULTORIO DA PSIQUIATRA

label scene_0006:
    # LIMPA A TELA E MOSTRA O AMBIENTE CONSULTORIO
    scene clinic
    with dissolve

    $secretaria="Judite"

    i01 "Acredito que sejam estes os questionamentos, muito obrigado pela colaboração"
    i02 "Caso lembre de alguma informação adicional, nos contate..."
    i01 "Aqui está meu cartão"
    psi "Está certo, [secretaria], acompanhe os agentes, por favor"

    return
