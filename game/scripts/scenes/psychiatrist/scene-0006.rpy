# AUTHOR: PERALTA GAMES
# SCOPE: VISITA DOS INVESTIGADORES AO CONSULTORIO DA PSIQUIATRA

label scene_0006:
    scene black

    tln "18/04/2022 - 09:43h | CLINICA CONSULTÓRIO"

    # LIMPA A TELA E MOSTRA O AMBIENTE CONSULTORIO
    scene clinic
    with dissolve

    i01 "Acredito que sejam estes os questionamentos, muito obrigado pela colaboração"
    i02 "Caso lembre de alguma informação adicional, nos contate..."
    i01 "Aqui está meu cartão"
    psi "Está certo, [atm_nome], acompanhe os agentes, por favor"

    return
