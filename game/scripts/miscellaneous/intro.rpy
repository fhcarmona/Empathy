# AUTHOR: PERALTA GAMES
# SCOPE: DEFINIR O ACONTECIMENTO DA INTRODUCAO DO JOGO

# INICIO DA INTRODUCAO
screen intro:
    imagemap:
        ground "images/scenes/intro.png"
        hover "images/scenes/intro_hover.png"

        # AO JOGADOR CLICAR CLICAR
        hotspot(112, 8, 423, 700) action [Play("sound", "audio/sfx/character-selected.mp3", "None"), Return(0)] # INVESTIGADOR
        hotspot(777, 2, 357, 715) action [Play("sound", "audio/sfx/character-selected.mp3", "None"), Return(1)] # MEDICA
