# AUTHOR: PERALTA GAMES
# SCOPE:

label scene_1000:
    hide screen cluesUI

    scene black

    tln "13/05/2022 - 23:13h | RESGATE QUARTA VÍTIMA"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene rescue-psy
    with dissolve

    show screen cluesUI

    #
    $ narrative_image("i01", left, None, i01, "Porque fomos chamados aqui?")
    $ narrative_image("cop", right, None, cop, "Foi solicitado a presença dos responsáveis pelo caso do serial killer")
    $ narrative_image("i01", left, None, i01, "Encontramos eles?")
    $ narrative_image("cop", right, None, cop, "Sim, porém, infelizmente ele não se encontra com vida")
    $ narrative_image("i02", left, None, i02, "Maldito, ao menos não irá causar mais mal, o que aconteceu?")
    $ narrative_image("cop", right, None, cop, "Uma mulher foi sequestrada e mantida como refem no porão")
    $ narrative_image("cop", right, None, cop, "Ela conseguiu escapar e com isso cortou a garganta do assassino")
    $ narrative_image("i02", left, None, i02, "Onde ela está nesse momento? Queremos fazer algumas perguntas")
    $ narrative_image("cop", right, None, cop, "Ela está desacordada, durante a luta, ela foi atingida por um tiro perto da região abdominal")
    $ narrative_image("cop", right, None, cop, "Encontramos ela perto da saída do porão, a vizinha que nos chamou, devido ao barulho do tiro")
    $ narrative_image("cop", right, None, cop, "No local do crime foi encontrado algumas drogas controladas, pedi para separarem até vocês chegarem")

    # DROGA - INVENTARIO
    $ narrative_image("cop", right, None, cop, "Aqui está os itens encontrado na cena do crime")

    $ inventory(1)

    $ narrative_image("i01", left, None, i01, "Está certo, vamos aguardar a vítima acordar")

    # ADICIONA INFORMACA DO PERSONAGEM NO INVENTARIO
    $ personagens(7)

    $ locais(4)

    hide screen cluesUI

    scene black

    tln "26/05/2022 - 10:13h | HOSPITAL"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene hospital
    with dissolve

    show screen cluesUI

    #
    $ narrative_image("i02", left, None, i02, "Bom dia doutora [psi_nome], soubemos que acordou. Como você está se sentindo?")
    $ narrative_image("psi", right, None, psi, "bom dia, investigadores, nem imaginaria que vocês viriam me visitar.")
    $ narrative_image("i01", left, None, i01, "Desculpe chegarmos assim, mas estamos a trabalho o médico autorizou a nossa entrada e informou que podemos fazer alguns questionamentos sobre o ocorrido. Tudo bem fazê-lo agora?")
    $ narrative_image("psi", right, None, psi, "Claro, fiquem à vontade")
    $ narrative_image("i02", left, None, i02, "Poderia nos contar o que aconteceu?")
    $ narrative_image("psi", right, None, psi, "Eu tinha saído um pouco, para beber no bar próximo daqui, até que este homem chegou e se sentou ao meu lado.")
    $ narrative_image("psi", right, None, psi, "Ele pediu uma bebida e depois de 30 minutos observando o movimento se levantou e saiu do bar")
    $ narrative_image("psi", right, None, psi, "Só que ele esqueceu a sua carteira em cima do balcão.")
    $ narrative_image("psi", right, None, psi, "Peguei a carteira e sai para devolver, lembro de levar uma pancada na cabeça e depois disso só acordei amarrada.")
    $ narrative_image("i02", left, None, i02, "E como você fugiu de lá?")
    $ narrative_image("psi", right, None, psi, "Alguém tocou a campainha da casa e aproveitei esse momento para tentar me soltar. ")
    $ narrative_image("psi", right, None, psi, "Agarrei a primeira coisa que vi pela frente e quando tive a oportunidade bati nele e sai correndo")
    $ narrative_image("psi", right, None, psi, "Então ouvi um disparo e depois uma dor depois disso acordei aqui no hospital.")
    $ narrative_image("psi", right, None, psi, "O que aconteceu com aquele cara?")
    $ narrative_image("i02", left, None, i02, "O homem morreu no local, o corte acabou acertando uma parte sensível do pescoço. Agradecemos o seu depoimento, iremos averiguar as evidências.")

    return
