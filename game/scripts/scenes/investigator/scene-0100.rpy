# AUTHOR: PERALTA GAMES
# SCOPE: INTRODUCAO AOS POLICIAIS

label scene_0100:
    scene black

    tln "17/04/2022 - 10:22h | DELEGACIA"

    # LIMPA A TELA E MOSTRA A DELEGACIA
    scene police-station

    show screen cluesUI

    play music "audio/musics/investigator.mp3"

    #
    $ narrative_image("i02", left, None, i02, "O que você está lendo [i01_nome]?")
    $ narrative_image("i01", left, None, i01, "Sobre o caso de ontem... apareceu no jornal")
    $ narrative_image("i02", left, None, i02, "Sério? Deixe-me ver")
    $ narrative_image("dlg", right, None, dlg, "[i01_nome], [i02_nome]. Na minha sala agora...")
    $ narrative_image("i01", left, None, i01, "Sim senhor")

    $ locais(0)

    hide screen cluesUI

    scene black

    tln "17/04/2022 - 10:37h | GABINETE DO CHEFE DE POLÍCIA"    

    # LIMPA A TELA E MOSTRA A SALA DO CHEFE DE POLICIA
    scene chiefs-room

    show screen cluesUI

    #
    $ narrative_image("dlg", right, None, dlg, "Vocês estão vendo isso?")
    $ narrative_image("i02", left, None, i02, "O jornal? É sobre o caso de ontem?")
    $ narrative_image("dlg", right, None, dlg, "Exatamente...")
    $ narrative_image("dlg", right, None, dlg, "Os jornalistas estão cada vez mais em cima depois dos acontecimentos, não podemos deixar passar nada")
    $ narrative_image("dlg", right, None, dlg, "Quero que continuem investigando o caso")
    $ narrative_image("i02", left, None, i02, "O sujeito já se encontra preso, não podemos considerar o caso como resolvido?")
    $ narrative_image("dlg", right, None, dlg, "Não. O caso está nos jornais, isso indica que eles poderão investigar mais")
    $ narrative_image("dlg", right, None, dlg, "Vamos investigar antes deles")
    $ narrative_image("i01", left, None, i01, "Entendido senhor")
    $ narrative_image("dlg", right, None, dlg, "Alguma dúvida?")
    $ narrative_image("i01", left, None, i01, "Não senhor")

    hide screen cluesUI

    scene black

    tln "17/04/2022 - 10:43h | DELEGACIA"

    # LIMPA A TELA E MOSTRA A DELEGACIA
    scene police-station

    show screen cluesUI

    $ narrative_image("i02", left, None, i02, "Por onde devemos começar a investigação?")
    $ narrative_image("i01", left, None, i01, "Deixe-me ver...")
    $ narrative_image("i01", left, None, i01, "A ficha do suspeito indicava que ele estava em uma liminar que o obrigava a participar de consultas com uma psiquiatra")
    $ narrative_image("i02", left, None, i02, "Entendo, podemos interrogar o suspeito, talvez ele tenha algo a nos dizer")

    menu:
        "Investigar"

        "Suspeito":
            $ narrative_image("i01", left, None, i01, "Concordo, vamos ver o que o suspeito tem a dizer")
            return 0

        "Psiquiatra":
            $ narrative_image("i02", left, None, i02, "A psiquiatra pode ter informações valiosas, vamos fazer uma visita")
            return 1

    return -1
