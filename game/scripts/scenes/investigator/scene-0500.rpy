# AUTHOR: PERALTA GAMES
# SCOPE:

label scene_0500:
    scene black

    tln "09/05/2022 - 19:37h | MOTEL"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene motel-entrance
    with dissolve

    # CONTEXTO MOTEL
    i02 "Bom, depois desse, vamos para o último"
    i01 "Que bom que eram apenas quatro hoteis nas proximidades do parque"
    i02 "Sim, bora entrar e conversar com a atendente"

    # RECEPCAO MOTEL
    scene motel-entrance
    with dissolve

    atm "Sim, ele esteve nesse dia com uma moça com essa mesma descrição"
    i02 "Poderia mostrar os registros do dia?"
    atm "Claro"

    # CAMERA DE SEGURANCA
    $renpy.movie_cutscene("video/security_camera.webm")

    i01 "É ele... E a mulher que o acompanhou... Talvez ela tenha alguma resposta, vamos localizar ela"
    atm "Aqui está o pendrive com a gravação do dia"
    i02 "Muito obrigado pela colaboração"

    return
