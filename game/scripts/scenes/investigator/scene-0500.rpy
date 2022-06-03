# AUTHOR: PERALTA GAMES
# SCOPE: INVESTIGADORES VAO ATE O MOTEL

label scene_0500:
    hide screen cluesUI

    scene black

    tln "09/05/2022 - 19:37h | MOTEL"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene motel-entrance
    with dissolve

    show screen cluesUI

    # CONTEXTO MOTEL
    $ narrative_image("i02", left, None, i02, "Bom, depois desse, vamos para o último")
    $ narrative_image("i01", left, None, i01, "Que bom que eram apenas quatro hoteis nas proximidades do parque")
    $ narrative_image("i02", left, None, i02, "Sim, bora entrar e conversar com a atendente")

    hide screen cluesUI

    scene black

    tln "09/05/2022 - 19:39h | RECEPCAO MOTEL"

    # RECEPCAO MOTEL
    scene motel-entrance
    with dissolve

    show screen cluesUI

    $ narrative_image("atm", right, None, atm, "Sim, ele esteve nesse dia com uma moça com essa mesma descrição")
    $ narrative_image("i02", left, None, i02, "Poderia mostrar os registros do dia?")
    $ narrative_image("atm", right, None, atm, "Claro")

    # CAMERA DE SEGURANCA - DEPRECATED
    # $renpy.movie_cutscene("video/security_camera.webm")

    $ narrative_image("i01", left, None, i01, "É ele... E a mulher que o acompanhou... Talvez ela tenha alguma resposta, vamos localizar ela")
    $ narrative_image("atm", right, None, atm, "Aqui está o pendrive com a gravação do dia")

    # ADICIONA O PENDRIVE AO INVENTARIO
    $ inventory(2)

    $ narrative_image("i02", left, None, i02, "Muito obrigado pela colaboração")

    # ADICIONA INFORMACA DO PERSONAGEM NO INVENTARIO
    $ personagens(1)

    $ locais(3)

    return
