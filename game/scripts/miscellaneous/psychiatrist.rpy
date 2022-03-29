# AUTHOR: PERALTA GAMES
# SCOPE: DEFINIR FLUXO DE CENAS DO PLOT DA PSIQUIATRA

label medic:
    # CHAMA A CENA 01 - CONSULTORIO, PACIENTE 01
    call scene_0001 from _call_scene_0001

    # JORNAL PRESENTE - RESOLUCAO DO CASO DO PACIENTE 01
    call newspaper(1) from _call_newspaper

    # CHAMA A CENA 02 - CONSULTORIO, PEGANDO ALGUNS REMEDIOS
    call scene_0002 from _call_scene_0002

    # CHAMA A CENA 03 - CONSULTORIO, PACIENTE 02
    call scene_0003 from _call_scene_0003

    # JORNAL PRESENTE - TERCEIRA VITIMA, SERIAL KILLER
    call newspaper(2) from _call_newspaper_1

    # CHAMA A CENA 04 - ENTRADA DO CONSULTORIO, VISITA DO INVESTIGADOR 01 E INVESTIGADOR 02
    call scene_0004 from _call_scene_0004

    # CHAMA A CENA 05 - CONSULTORIO, INTERROGATORIO PSIQUIATRA
    call scene_0005 from _call_scene_0005

    # CHAMA A CENA 06 - RECEPCAO DO CONSULTORIO, FINAL DO INTERROGATORIO
    call scene_0006 from _call_scene_0006

    # REVISTA FUTURO - ARTIGO ESPECIAL PSICOPATAS
    call revista(1) from _call_revista

    # COMPUTADOR - CASA PSIQUIATRA, VERIFICANDO AS NOTICIAS DO DIA
    call computador(1) from _call_computador

    # CHAMA A CENA 07 - CONSULTORIO, PACIENTE 03 RELATANDO UM ACONTECIMENTO DO PASSADO
    call scene_0007 from _call_scene_0007

    # JORNAL PASSADO - VITIMA 01, ANTES DO CONHECIMENTO DE SER UM SERIAL KILLER
    call newspaper(3) from _call_newspaper_2

    # CHAMA A CENA 08 - BAR EM BUSCA DO SERIAL KILLER
    call scene_0008 from _call_scene_0008

    # CHAMA A CENA 09 - PSIQUIATRA PRESA NO PORAO
    call scene_0009 from _call_scene_0009

    # JORNAL PASSADO - MENTE HUMANA
    call revista(2) from _call_revista_1

    # CHAMA A CENA 10 - MENTE HUMANA
    call scene_0010 from _call_scene_0010

    # VOLTA AO INICIO
    call screen intro

    return
