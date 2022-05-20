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
    cop "Ela conseguiu escapar e com isso cortou a garganta do assassino"
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
    i02 "Bom dia doutora [psi_nome], soubemos que acordou. Como você está se sentindo?"
    psi "bom dia, investigadores, nem imaginaria que vocês viriam me visitar."
    i01 "Desculpe chegarmos assim, mas estamos a trabalho o médico autorizou a nossa entrada e informou que podemos fazer alguns questionamentos sobre o ocorrido. Tudo bem fazê-lo agora?"
    psi "Claro, fiquem à vontade"
    i02 "Poderia nos contar o que aconteceu?"
    psi "Eu tinha saído um pouco, para beber no bar próximo daqui, até que este homem chegou e se sentou ao meu lado."
    psi "Ele pediu uma bebida e depois de 30 minutos observando o movimento se levantou e saiu do bar"
    psi "Só que ele esqueceu a sua carteira em cima do balcão."
    psi "Peguei a carteira e sai para devolver, lembro de levar uma pancada na cabeça e depois disso só acordei amarrada."
    i02 "E como você fugiu de lá?"
    psi "Alguém tocou a campainha da casa e aproveitei esse momento para tentar me soltar. "
    psi "Agarrei a primeira coisa que vi pela frente e quando tive a oportunidade bati nele e sai correndo"
    psi "Então ouvi um disparo e depois uma dor depois disso acordei aqui no hospital."
    psi "O que aconteceu com aquele cara?"
    i02 "O homem morreu no local, o corte acabou acertando uma parte sensível do pescoço. Agradecemos o seu depoimento, iremos averiguar as evidências."

    return
