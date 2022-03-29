# AUTHOR: PERALTA GAMES
# SCOPE: DEFINIR O SPLASHSCREEN ANTERIOR AO MENU PRINCIPAL

# AVISO DE CONTEUDO EXPLICITO ANTES DO MENU
label splashscreen:
    scene black
    with Pause(1)

    show warning_explicit_content with dissolve
    with Pause(2)

    hide warning_explicit_content with dissolve
    with Pause(1)
