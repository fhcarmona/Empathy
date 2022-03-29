# AUTHOR: PERALTA GAMES
# SCOPE: DEFINIR O FLUXO DA GAMEPLAY

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
