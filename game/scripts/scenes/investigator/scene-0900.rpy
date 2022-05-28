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
    $ narrative_image("p01", right, None, p01, "Então é essas crises que a [p03_nome] teve no dia?") # p01 "Então é essas crises que a [p03_nome] teve no dia?"
    $ narrative_image("psi", right, None, psi, "Eu imagino que sim, terei que conversar pessoalmente com ela, mas existe esse trauma de infância") # psi "Eu imagino que sim, terei que conversar pessoalmente com ela, mas existe esse trauma de infância"
    $ narrative_image("i02", left, None, i02, "Seria ótimo [psi_nome] ter essa conversa, a senhorita [p03_nome] chegou a contar algo sobre esse primo?") # i02 "Seria ótimo [psi_nome] ter essa conversa, a senhorita [p03_nome] chegou a contar algo sobre esse primo?"
    $ narrative_image("psi", right, None, psi, "Eles eram bem próximos, mas ela me disse ter parado de conversar com ele a algum tempo") # psi "Eles eram bem próximos, mas ela me disse ter parado de conversar com ele a algum tempo"
    $ narrative_image("psi", right, None, psi, "Eu não saberia dizer qual o momento que os dois voltaram a conversar, nem para mim ela chegou a conversar sobre") # psi "Eu não saberia dizer qual o momento que os dois voltaram a conversar, nem para mim ela chegou a conversar sobre"
    $ narrative_image("i01", left, None, i01, "Acha que ela pode estar escondendo algo?") # i01 "Acha que ela pode estar escondendo algo?"
    $ narrative_image("psi", right, None, psi, "Não acredito que ela esteja escondendo algo, mas talvez não consiga falar sobre") # psi "Não acredito que ela esteja escondendo algo, mas talvez não consiga falar sobre"
    $ narrative_image("psi", right, None, psi, "Alguns pacientes que passam por um trauma, sofrem de amnésia seletiva") # psi "Alguns pacientes que passam por um trauma, sofrem de amnésia seletiva"
    $ narrative_image("psi", right, None, psi, "Eu imagino que agora ela só queira se isolar") # psi "Eu imagino que agora ela só queira se isolar"

    hide screen cluesUI

    scene black

    tln "13/05/2022 - 11:13h | TRAILER DE HOTDOG"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene hot-dog-stand
    with dissolve

    show screen cluesUI

    $ narrative_image("i02", left, None, i02, "Nossa!") # i02 "Nossa!"
    $ narrative_image("i01", left, None, i01, "O que foi?") # i01 "O que foi?"
    $ narrative_image("i02", left, None, i02, "Acho que entendi! A água no pulmão das vítimas") # i02 "Acho que entendi! A água no pulmão das vítimas"
    $ narrative_image("i01", left, None, i01, "Pode parar... Estamos no momento de pausa") # i01 "Pode parar... Estamos no momento de pausa"
    $ narrative_image("i02", left, None, i02, "Se eu esperar perco o raciocínio") # i02 "Se eu esperar perco o raciocínio"
    $ narrative_image("i02", left, None, i02, "Qual era a composição incomum na água do pulmão das vítimas?") # i02 "Qual era a composição incomum na água do pulmão das vítimas?"
    $ narrative_image("i01", left, None, i01, "A cor verde?") # i01 "A cor verde?"
    $ narrative_image("i02", left, None, i02, "Não, mais que isso, a presença de organismos e alga") # i02 "Não, mais que isso, a presença de organismos e alga"
    $ narrative_image("i01", left, None, i01, "O que tem isso?") # i01 "O que tem isso?"
    $ narrative_image("i02", left, None, i02, "Acredito que haja uma relação entre as vítimas e esse trauma") # i02 "Acredito que haja uma relação entre as vítimas e esse trauma"
    $ narrative_image("i02", left, None, i02, "E na sala da psiquiatra muitos remédios") # i02 "E na sala da psiquiatra muitos remédios"
    $ narrative_image("i02", left, None, i02, "Vamos voltar para a delegacia") # i02 "Vamos voltar para a delegacia"

    hide screen cluesUI
    
    scene black

    tln "13/05/2022 - 11:37h | DELEGACIA DE POLÍCIA"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene police-station
    with dissolve

    show screen cluesUI

    $ narrative_image("i02", left, None, i02, "Baseado na localidade das vítimas, elas estão em um range menor que vinte e cinco quilômetros") # i02 "Baseado na localidade das vítimas, elas estão em um range menor que vinte e cinco quilômetros"
    $ narrative_image("i01", left, None, i01, "Isso é um busca bem grande, mas já sabiamos disso, onde quer chegar?") # i01 "Isso é um busca bem grande, mas já sabiamos disso, onde quer chegar?"
    $ narrative_image("i02", left, None, i02, "Agora, se você filtra por lagos") # i02 "Agora, se você filtra por lagos"
    $ narrative_image("i02", left, None, i02, "E depois filtra por consultórios de psiquiatrias") # i02 "E depois filtra por consultórios de psiquiatrias"
    $ narrative_image("i02", left, None, i02, "Voilà!") # i02 "Voilà!"
    $ narrative_image("i01", left, None, i01, "Coincidência nossa psiquiatra ser o único consultório nesse filtro?") # i01 "Coincidência nossa psiquiatra ser o único consultório nesse filtro?"
    $ narrative_image("i02", left, None, i02, "Deveria saber que coincidência nesse ramo não existe") # i02 "Deveria saber que coincidência nesse ramo não existe"

    return
