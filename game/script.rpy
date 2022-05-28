# AUTHOR: PERALTA GAMES
# SCOPE: DEFINIR O FLUXO DA GAMEPLAY

# FUNCOES
init python:
    def narrative_image (*args):
        # IDENTIFICADORES
        nome = args[0]      # NOME DO PERSONAGEM DA LISTA DE CHARACTERS
        lado = args[1]      # LADO QUE O PERSONAGEM ESTARA (LEFT, RIGHT E VAZIO)
        humor = args[2]     # VARIACAO DE ROSTO
        char_obj = args[3]  # OBJETO DO PERSONAGEM (PUXA NOME, COR, ETC)
        fala = args[4]      # TEXTO ATUAL DO PERSONAGEM

        # MOSTRA A IMAGEM DE FUNDO DO PERSONAGEM E A FALA, DEPOIS ESCONDE
        if nome != "":
            renpy.show(nome, at_list=[lado], layer='master', what=humor, zorder=0, tag="atual", behind=[])
        renpy.say(char_obj, fala)
        renpy.hide("atual")

# INICIO DO JOGO
label start:
    # DECLARA AS VARIAVEIS
    call game_variables from _call_game_variables

    # PARA A MUSICA DO MENU PRINCIPAL
    stop music fadeout 1.0

    # CHAMA A CENA - INTRODUCAO
    call screen intro

    # ARMAZENA O VALOR DA ESCOLHA DEFINIDO PELO JOGADOR
    $narrativa=_return

    # PAUSA DRAMATICA DA ESCOLHA FEITA
    pause 2

    # PLOT INVESTIGADOS
    if narrativa==0:
        # SCENE-0100 -
        call investigator from _call_investigator

    # PLOT PSIQUIATRA
    elif narrativa==1:
        # SCENE-0001 - CONSULTORIO, PACIENTE 01
        call medic from _call_medic

    # FINALIZA O JOGO
    return
