# AUTHOR: PERALTA GAMES
# SCOPE:

label scene_0700:
    scene black

    tln "12/05/2022 - 15:12h | DELEGACIA DE POLICIA"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene police-station
    with dissolve

    #
    i02 "Bingo!"
    i01 "Encontrou?"
    i02 "Sim, [p03_nome] é o nome dela, mora próximo do bar"
    i01 "Perfeito! Pegue as coisas e vamos"

    scene black
    with Pause(2)

    play sound phone_ring
    with Pause(2)

    scene police-station
    with dissolve

    i01 "Alô, pois não?"
    i01 "Entendido..."
    i01 "Sem problemas, já estamos descendo, um momento, muito obrigado"

    i02 "Aconteceu algo?"
    i01 "Sim, saiu o relatório final da autópsia"
    i02 "Bom, vamos conversar com o legista, depois vamos para a casa da prima da vítima"

    scene morgue
    with dissolve

    leg "Boa tarde senhores"
    i01 "Boa tarde [leg_nome], então, quais são as novidades"
    leg "Como podem ver as imagens da autópsia, encontramos e analisamos esse líquido verde que se encontrava no pulmão da vítima"
    leg "Após a análise concluida verificamos que basicamente a constituição dessa água possuia uma grande quantidade de algas e micro-organismos"
    i01 "Algas?"
    leg "Isso, a coloração verde é devido a isso"
    i01 "Como a água pode chegar a esse estado?"
    leg "Depende de muitas coisas, mas dessa forma? PH alto, temperatura e pouco cloro"
    i02 "Isso indica que o assassino possui uma piscina ou algo que faça essa água"
    leg "Exato, não foi possível identificar se a água foi criada artificialmente ou é pega do exterior de uma piscina aberta"
    i01 "Muito obrigado, isso ajudará a diminuir o range de localidades"

    return
