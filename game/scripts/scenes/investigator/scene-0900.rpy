# AUTHOR: PERALTA GAMES
# SCOPE:

label scene_0900:
    hide screen cluesUI

    scene black

    tln "13/05/2022 - 08:57h | CONSULTÓRIO PSIQUIATRA"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene clinic
    with dissolve

    show screen cluesUI

    #
    $ narrative_image("i01", right, None, i01, "Então é essas crises que a [p03_nome] teve no dia?")
    $ narrative_image("psi", right, None, psi, "Eu imagino que sim, terei que conversar pessoalmente com ela, mas existe esse trauma de infância")
    $ narrative_image("i02", left, None, i02, "Seria ótimo [psi_nome] ter essa conversa, a senhorita [p03_nome] chegou a contar algo sobre esse primo?")
    $ narrative_image("psi", right, None, psi, "Eles eram bem próximos, mas ela me disse ter parado de conversar com ele a algum tempo")
    $ narrative_image("psi", right, None, psi, "Eu não saberia dizer qual o momento que os dois voltaram a conversar, nem para mim ela chegou a conversar sobre")
    $ narrative_image("i01", left, None, i01, "Acha que ela pode estar escondendo algo?")
    $ narrative_image("psi", right, None, psi, "Não acredito que ela esteja escondendo algo, mas talvez não consiga falar sobre")
    $ narrative_image("psi", right, None, psi, "Alguns pacientes que passam por um trauma, sofrem de amnésia seletiva")
    $ narrative_image("psi", right, None, psi, "Eu imagino que agora ela só queira se isolar")

    if locais_visitados[1] == 0:
        $ locais(1)

    hide screen cluesUI

    scene black

    tln "13/05/2022 - 11:13h | LANCHONETE"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene cafeteria
    with dissolve

    show screen cluesUI

    $ narrative_image("i02", left, None, i02, "Nossa!")
    $ narrative_image("i01", left, None, i01, "O que foi?")
    $ narrative_image("i02", left, None, i02, "Acho que entendi! A água no pulmão das vítimas")
    $ narrative_image("i01", left, None, i01, "Pode parar... Estamos no momento de pausa")
    $ narrative_image("i02", left, None, i02, "Se eu esperar perco o raciocínio")
    $ narrative_image("i02", left, None, i02, "Qual era a composição incomum na água do pulmão das vítimas?")
    $ narrative_image("i01", left, None, i01, "A cor verde?")
    $ narrative_image("i02", left, None, i02, "Não, mais que isso, a presença de organismos e alga")
    $ narrative_image("i01", left, None, i01, "O que tem isso?")
    $ narrative_image("i02", left, None, i02, "Acredito que haja uma relação entre o caso da [p03_nome] e os assassinatos")

    hide screen cluesUI

    scene black

    tln "13/05/2022 - 11:37h | DELEGACIA DE POLÍCIA"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene police-station
    with dissolve

    show screen cluesUI

    $ narrative_image("i02", left, None, i02, "Baseado na localidade das vítimas, elas estão em uma proximidade menor que vinte e cinco quilômetros")
    $ narrative_image("i01", left, None, i01, "Isso é um busca bem grande, mas já sabíamos disso, onde quer chegar?")
    $ narrative_image("i02", left, None, i02, "Agora, se você ver onde a [p03_nome] mora e onde ocorreu o trauma dela")
    $ narrative_image("i02", left, None, i02, "E depois filtra por consultórios de psiquiatria")
    $ narrative_image("i02", left, None, i02, "Voilà!")
    $ narrative_image("i01", left, None, i01, "Coincidência nossa psiquiatra ser o único consultório nesse filtro?")
    $ narrative_image("i02", left, None, i02, "Deveria saber que coincidência nesse ramo não existe")
    $ narrative_image("i01", left, None, i01, "Sinto que estamos mais perto!")
    $ narrative_image("i02", left, None, i02, "Vamos!")

    if personagens_vistos[6]==0:
        # ADICIONA INFORMACAO DO PERSONAGEM NO INVENTARIO
        $ personagens(6)

    return
