# AUTHOR: PERALTA GAMES
# SCOPE:

label scene_1000:
    scene black

    tln "13/05/2022 - 23:13h | RESGATE QUARTA VÍTIMA"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene rescue-psy
    with dissolve

    #
    i01 "Porque fomos chamados aqui?"
    cop "Foi solicitado a presença dos responsáveis pelo caso do serial killer"
    i01 "Encontramos eles?"
    cop "Sim, porém, infelizmente ele não se encontra com vida"
    i02 "Maldito, ao menos não irá causar mais mal, o que aconteceu?"
    cop "Uma mulher foi sequestrada e mantida como refem no porão"
    cop "Ela conseguiu escapar e com um pedaço de ferro pontudo cortou a garganta do assassino"
    i02 "Onde ela está nesse momento? Queremos fazer algumas perguntas"
    cop "Ela está desacordada, durante a luta, ela foi atingida por um tiro perto da região abdominal"
    cop "Encontramos ela perto da saída do porão, a vizinha que nos chamou, devido ao barulho do tiro"
    i01 "Está certo, vamos aguardar a vítima acordar"

    scene black

    tln "26/05/2022 - 10:13h | HOSPITAL"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene hospital
    with dissolve

    #
    i02 "Bom dia doutora [psi_nome], soubemos que acordou"
    psi "Ver vocês me visitando não me passava pela cabeça"
    i01 "Estamos em trabalho, o médico autorizou alguns questionamentos, podemos fazê-lo?"
    i02 "Claro..."

    return
