# AUTHOR: PERALTA GAMES
# SCOPE: DESENVOLVER A PRIMEIRA SESSAO DA INVESTIGADOR

label scene_0100:
    scene black

    tln "17/04/2022 - 10:22h | DELEGACIA"

    # LIMPA A TELA E MOSTRA A DELEGACIA
    scene police-station

    show screen cluesUI

    play music "audio/musics/investigator.mp3"

    #
    $ narrative_image("i02", left, None, i02, "O que você está lendo [i01_nome]?") # i02 "O que você está lendo [i01_nome]?"
    $ narrative_image("i01", left, None, i01, "Sobre o caso de ontem... apareceu no jornal") # i01 "Sobre o caso de ontem... apareceu no jornal"
    $ narrative_image("i02", left, None, i02, "Sério? Deixe-me ver") # i02 "Sério? Deixe-me ver"
    $ narrative_image("dlg", right, None, dlg, "[i01_nome], [i02_nome]. Na minha sala agora...") # del "[i01_nome], [i02_nome]. Na minha sala agora..."
    $ narrative_image("i01", left, None, i01, "Sim senhor") # i01 "Sim senhor"

    hide screen cluesUI

    scene black

    tln "17/04/2022 - 10:37h | GABINETE DO CHEFE DE POLÍCIA"

    # LIMPA A TELA E MOSTRA A SALA DO CHEFE DE POLICIA
    scene chiefs-room

    show screen cluesUI

    #
    $ narrative_image("dlg", right, None, dlg, "Vocês estão vendo isso?") # del "Vocês estão vendo isso?"
    $ narrative_image("i02", left, None, i02, "O jornal? É sobre o caso de ontem?") # i02 "O jornal? É sobre o caso de ontem?"
    $ narrative_image("dlg", right, None, dlg, "Exatamente...") # del "Exatamente..."
    $ narrative_image("dlg", right, None, dlg, "Os jornalistas estão cada vez mais em cima depois dos acontecimentos, não podemos deixar passar nada") # del "Os jornalistas estão cada vez mais em cima depois dos acontecimentos, não podemos deixar passar nada"
    $ narrative_image("dlg", right, None, dlg, "Quero que continuem investigando o caso") # del "Quero que continuem investigando o caso"
    $ narrative_image("i02", left, None, i02, "O sujeito já se encontra preso, não podemos considerar o caso como resolvido?") # i02 "O sujeito já se encontra preso, não podemos considerar o caso como resolvido?"
    $ narrative_image("dlg", right, None, dlg, "Não. O caso está nos jornais, isso indica que eles poderão investigar mais") # del "Não. O caso está nos jornais, isso indica que eles poderão investigar mais"
    $ narrative_image("dlg", right, None, dlg, "Vamos investigar antes deles") # del "Vamos investigar antes deles"
    $ narrative_image("i01", left, None, i01, "Entendido senhor") # i01 "Entendido senhor"
    $ narrative_image("dlg", right, None, dlg, "Alguma dúvida?") # del "Alguma dúvida?"
    $ narrative_image("i01", left, None, i01, "Não senhor") # i01 "Não senhor"

    hide screen cluesUI

    scene black

    tln "17/04/2022 - 10:43h | DELEGACIA"

    # LIMPA A TELA E MOSTRA A DELEGACIA
    scene police-station

    show screen cluesUI

    $ narrative_image("i02", left, None, i02, "Por onde devemos começar a investigação?") # i02 "Por onde devemos começar a investigação?"
    $ narrative_image("i01", left, None, i01, "Deixe-me ver...") # i01 "Deixe-me ver..."
    $ narrative_image("i01", left, None, i01, "A ficha do suspeito indicava que ele estava em uma liminar que o obrigava a participar de consultas com uma psiquiatra") # i01 "A ficha do suspeito indicava que ele estava em uma liminar que o obrigava a participar de consultas com uma psiquiatra"
    $ narrative_image("i02", left, None, i02, "Entendo, podemos interrogar o suspeito, talvez ele tenha algo a nos dizer") # i02 "Entendo, podemos interrogar o suspeito, talvez ele tenha algo a nos dizer"

    menu:
        "Investigar"

        "Suspeito":
            $ narrative_image("i01", left, None, i01, "Concordo, vamos ver o que o suspeito tem a dizer") # i01 "Concordo, vamos ver o que o suspeito tem a dizer"
            return 0

        "Psiquiatra":
            $ narrative_image("i02", left, None, i02, "A psiquiatra pode ter informações valiosas, vamos fazer uma visita") # i02 "A psiquiatra pode ter informações valiosas, vamos fazer uma visita"
            return 1
            
    return -1
