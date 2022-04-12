# AUTHOR: PERALTA GAMES
# SCOPE:

label scene_0900:
    scene black

    tln "13/05/2022 - 08:57h | CONSULTÓRIO PSIQUIATRA"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene clinic
    with dissolve

    #
    p01 "Então é essas crises que a [p03_nome] teve no dia?"
    psi "Eu imagino que sim, terei que conversar pessoalmente com ela, mas existe esse trauma de infância"
    i02 "Seria ótimo [psi_nome] ter essa conversa, a senhorita [p03_nome] chegou a contar algo sobre esse primo?"
    psi "Eles eram bem próximos, mas ela me disse ter parado de conversar com ele a algum tempo"
    psi "Eu não saberia dizer qual o momento que os dois voltaram a conversar, nem para mim ela chegou a conversar sobre"
    i01 "Acha que ela pode estar escondendo algo?"
    psi "Não acredito que ela esteja escondendo algo, mas talvez não consiga falar sobre"
    psi "Alguns pacientes que passam por um trauma, sofrem de amnésia seletiva"
    psi "Eu imagino que agora ela só queira se isolar"

    scene black

    tln "13/05/2022 - 11:13h | TRAILER DE HOTDOG"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene hot-dog-stand
    with dissolve

    i02 "Nossa!"
    i01 "O que foi?"
    i02 "Acho que entendi! A água no pulmão das vítimas"
    i01 "Pode parar... Estamos no momento de pausa"
    i02 "Se eu esperar perco o raciocínio"
    i02 "Qual era a composição incomum na água do pulmão das vítimas?"
    i01 "A cor verde?"
    i02 "Não, mais que isso, a presença de organismos e alga"
    i01 "O que tem isso?"
    i02 "Acredito que haja uma relação entre as vítimas e esse trauma"
    i02 "E na sala da psiquiatra muitos remédios"
    i02 "Vamos voltar para a delegacia"

    scene black

    tln "13/05/2022 - 11:37h | DELEGACIA DE POLÍCIA"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene police-station
    with dissolve

    i02 "Baseado na localidade das vítimas, elas estão em um range menor que vinte e cinco quilômetros"
    i01 "Isso é um range bem grande, mas já sabiamos disso, onde quer chegar?"
    i02 "Agora, se você filtra por lagos"
    i02 "E depois filtra por consultórios de psiquiatrias"
    i02 "Voilà!"
    i01 "Coincidência nossa psiquiatra ser o único consultório nesse filtro?"
    i02 "Deveria saber que coincidência nesse ramo não existe"

    return
