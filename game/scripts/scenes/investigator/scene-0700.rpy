# AUTHOR: PERALTA GAMES
# SCOPE:

label scene_0700:
    hide screen cluesUI

    scene black

    tln "12/05/2022 - 15:12h | DELEGACIA DE POLICIA"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene police-station
    with dissolve

    show screen cluesUI

    #
    $ narrative_image("i02", left, None, i02, "Bingo!") # i02 "Bingo!"
    $ narrative_image("i01", left, None, i01, "Encontrou?") # i01 "Encontrou?"
    $ narrative_image("i02", left, None, i02, "Sim, [p03_nome] é o nome dela, mora próximo do bar") # i02 "Sim, [p03_nome] é o nome dela, mora próximo do bar"
    $ narrative_image("i01", left, None, i01, "Espere um momento, irei atender antes de sairmos") # i01 "Espere um momento, irei atender antes de sairmos"

    hide screen cluesUI

    scene black
    with Pause(2)

    play sound phone_ring
    with Pause(2)

    scene police-station
    with dissolve

    show screen cluesUI

    $ narrative_image("i01", left, None, i01, "Alô, pois não?") # i01 "Alô, pois não?"
    $ narrative_image("i01", left, None, i01, "Entendido...") # i01 "Entendido..."
    $ narrative_image("i01", left, None, i01, "Sem problemas, já estamos descendo, um momento, muito obrigado") # i01 "Sem problemas, já estamos descendo, um momento, muito obrigado"

    $ narrative_image("i02", left, None, i02, "Aconteceu algo?") # i02 "Aconteceu algo?"
    $ narrative_image("i01", left, None, i01, "Sim, saiu o relatório final da autópsia") # i01 "Sim, saiu o relatório final da autópsia"
    $ narrative_image("i02", left, None, i02, "Bom, vamos conversar com o legista, depois vamos para a casa da prima da vítima") # i02 "Bom, vamos conversar com o legista, depois vamos para a casa da prima da vítima"

    hide screen cluesUI

    scene black

    tln "12/05/2022 - 15:37h | NECROTÉRIO"

    scene morgue
    with dissolve

    show screen cluesUI

    $ narrative_image("leg", right, None, leg, "Boa tarde senhores") # leg "Boa tarde senhores"
    $ narrative_image("i01", left, None, i01, "Boa tarde [leg_nome], então, quais são as novidades") # i01 "Boa tarde [leg_nome], então, quais são as novidades"
    $ narrative_image("leg", right, None, leg, "Como podem ver as imagens da autópsia, encontramos e analisamos esse líquido verde que se encontrava no pulmão da vítima") # leg "Como podem ver as imagens da autópsia, encontramos e analisamos esse líquido verde que se encontrava no pulmão da vítima"
    $ narrative_image("leg", right, None, leg, "Após a análise concluida verificamos que basicamente a constituição dessa água possuia uma grande quantidade de algas e micro-organismos") # leg "Após a análise concluida verificamos que basicamente a constituição dessa água possuia uma grande quantidade de algas e micro-organismos"
    $ narrative_image("i01", left, None, i01, "Algas?") # i01 "Algas?"
    $ narrative_image("leg", right, None, leg, "Isso, a coloração verde é devido a isso") # leg "Isso, a coloração verde é devido a isso"
    $ narrative_image("i01", left, None, i01, "Como a água pode chegar a esse estado?") # i01 "Como a água pode chegar a esse estado?"
    $ narrative_image("leg", right, None, leg, "Depende de muitas coisas, mas dessa forma? PH alto, temperatura e pouco cloro") # leg "Depende de muitas coisas, mas dessa forma? PH alto, temperatura e pouco cloro"
    $ narrative_image("i02", left, None, i02, "Isso indica que o assassino possui uma piscina ou algo que faça essa água") # i02 "Isso indica que o assassino possui uma piscina ou algo que faça essa água"
    $ narrative_image("leg", right, None, leg, "Exato, não foi possível identificar se a água foi criada artificialmente ou é pega do exterior de uma piscina aberta") # leg "Exato, não foi possível identificar se a água foi criada artificialmente ou é pega do exterior de uma piscina aberta"

    # LIQUIDO VERDE - INVENTARIO
    $ narrative_image("leg", right, None, leg, "De qualquer forma, aqui está os dados que foram analisados") # leg "De qualquer forma, aqui está os dados que foram analisados"
    "Informações sobre o líquido verde foi adicionada ao seu inventário"
    $inventario[0]=1

    $ narrative_image("i01", left, None, i01, "Muito obrigado, isso ajudará a diminuir a busca de localidades") # i01 "Muito obrigado, isso ajudará a diminuir a busca de localidades"

    return
