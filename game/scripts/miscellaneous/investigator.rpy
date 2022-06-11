# AUTHOR: PERALTA GAMES
# SCOPE: DEFINIR FLUXO DE CENAS DO PLOT DO INVESTIGADOR
label investigator:
    # CHAMA O JORNAL 01 - PAI AGRIDE HOMEM EM FESTA INFANTIL
    call newspaper(1) from _call_newspaper_3

    # CHAMA A CENA 0100 - DELEGACIA, DEMANDA DO CASO DO PACIENTE 01 PARA OS INVESTIGADORES RESPONSÁVEIS
    call scene_0100 from _call_scene_0100

    # ARMAZENA O VALOR DA ESCOLHA DEFINIDO PELO JOGADOR
    $rumo_investigacao=_return

    # CHAMA A CENA 0200 - QUESTIONARIO PSIQUIATRA
    call scene_0200(rumo_investigacao) from _call_scene_0200

    # CHAMA O JORNAL 02 - TERCEIRA VITIMA LOCALIZADA
    call newspaper(2) from _call_newspaper_4

    # CHAMA A CENA 0300 - QUESTIONARIO GARI
    call scene_0300 from _call_scene_0300

    # CHAMA A CENA 0400 - QUESTIONARIO BARMAN
    call scene_0400 from _call_scene_0400

    # CHAMA A CENA 0500 - RECEPCAO MOTEL
    call scene_0500 from _call_scene_0500

    # CHAMA A CENA 0600 - ENCONTRO COM MULHER DO BAR
    call scene_0600 from _call_scene_0600

    # CHAMA A CENA 0700 - DELEGACIA, RESULTADO AUTOPSIA
    call scene_0700 from _call_scene_0700

    # CHAMA A CENA 0800 - CONVERSA COM A PACIENTE 03 (PRIMA DA VITIMA 03)
    call scene_0800 from _call_scene_0800

    # CHAMA A CENA 0900 - CONSULTORIO PSIQUIATRA
    call scene_0900 from _call_scene_0900

    # CHAMA A CENA 1000 - RESGATE PSIQUIATRA, HOSPITAL
    call scene_1000 from _call_scene_1000

    # CHAMA A CENA 1100 - FINAL
    call scene_1100 from _call_scene_1100

    return
