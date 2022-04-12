# AUTHOR: PERALTA GAMES
# SCOPE: DESENVOLVER A PRIMEIRA SESSAO DA INVESTIGADOR

label scene_0100:
    scene black

    tln "17/04/2022 - 10:22h | DELEGACIA"

    # LIMPA A TELA E MOSTRA A DELEGACIA
    scene police-station

    play music "audio/musics/investigator.mp3"
    #
    i02 "O que você está lendo [i01_nome]?"
    i01 "Sobre o caso de ontem... apareceu no jornal"
    i02 "Sério? Deixe-me ver"
    del "[i01_nome], [i02_nome]. Na minha sala agora..."
    i01 "Sim senhor"

    # LIMPA A TELA E MOSTRA A SALA DO CHEFE DE POLICIA
    scene chiefs-room

    #
    del "Vocês estão vendo isso?"
    i02 "O jornal? É sobre o caso de ontem?"
    del "Exatamente..."
    del "Os jornalistas estão cada vez mais em cima depois dos acontecimentos, não podemos deixar passar nada"
    del "Quero que vocês investiguem mais o caso da agressão, não desejo outro escândalo"
    i02 "O sujeito já se encontra preso, não podemos só deixar o caso como resolvido?"
    del "Não. O caso está nos jornais, isso indica que eles poderão investigar mais"
    del "Vamos investigar antes deles"
    i01 "Entendido senhor"
    del "Alguma dúvida?"
    i01 "Não senhor"

    # LIMPA A TELA E MOSTRA A DELEGACIA
    scene police-station

    i02 "Por onde devemos começar a investigação?"
    i01 "Deixe-me ver..."
    i01 "A ficha do suspeito indicava que ele estava em uma liminar que o obrigava a participar de consultas com uma psiquiatra"
    i02 "Entendo, podemos interrogar o suspeito, talvez ele tenha algo a nos dizer"

    menu:
        "Investigar"

        "Suspeito":
            i01 "Concordo, vamos ver o que o suspeito tem a dizer"
            return 0

        "Psiquiatra":
            i02 "A psiquiatra pode ter informações valiosas, vamos fazer uma visita"
            return 1

    return -1
