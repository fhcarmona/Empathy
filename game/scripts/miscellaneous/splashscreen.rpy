# AUTHOR: PERALTA GAMES
# SCOPE: DEFINIR O SPLASHSCREEN ANTERIOR AO MENU PRINCIPAL

# AVISO DE CONTEUDO EXPLICITO ANTES DO MENU
label splashscreen:
    scene black
    with Pause(1)

    show warning_explicit_content with dissolve

    centered "{color=#FFF}{size=+10}O conteúdo a seguir pode conter elementos que não são adequados para alguns públicos, recomenda-se prudência do espectador{/size}{/color}"

    hide warning_explicit_content with dissolve
    with Pause(1)
