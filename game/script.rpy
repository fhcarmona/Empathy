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
            renpy.show(nome, at_list=[lado], layer='transient', what=humor, zorder=0, tag="atual", behind=[])
        renpy.say(char_obj, fala)
        renpy.hide("atual")

    def inventory (item):
        # DEFINE A DESCRICAO DO ITEM AO SER PEGO DURANTE O JOGO
        if item==0:
            renpy.say("", "Informações sobre o líquido verde foi adicionada ao seu inventário")    # LIQUIDO VERDE
        elif item==1:
            renpy.say("", "Informações sobre a droga foi adicionada ao seu inventário")            # DROGA
        elif item==2:
            renpy.say("", "Informações sobre o pendrive foi adicionada ao seu inventário")         # PENDRIVE

        # DEFINE COMO PEGO O ITEM
        inventario[item]=1

    def personagens (personagem):
        # DEFINE A DESCRICAO DOS PERSONAGENS ENCONTRADOS
        if personagem==0:
            renpy.say("", "Informações sobre o [acp_nome] foi adicionada ao seu inventário")   # ACOMPANHANTE
        elif personagem==1:
            renpy.say("", "Informações sobre o [atm_nome] foi adicionada ao seu inventário")   # ATENDENTE MOTEL
        elif personagem==2:
            renpy.say("", "Informações sobre o [bmn_nome] foi adicionada ao seu inventário")   # BARMAN
        elif personagem==3:
            renpy.say("", "Informações sobre o [gar_nome] foi adicionada ao seu inventário")   # GARI
        elif personagem==4:
            renpy.say("", "Informações sobre o [p01_nome] foi adicionada ao seu inventário")   # PACIENTE 01
        elif personagem==5:
            renpy.say("", "Informações sobre o [p03_nome] foi adicionada ao seu inventário")   # PACIENTE 03
        elif personagem==6:
            renpy.say("", "Informações sobre a [psi_nome] foi adicionada ao seu inventário")   # PSIQUIATRA
        elif personagem==7:
            renpy.say("", "Informações sobre o [skr_nome] foi adicionada ao seu inventário")   # SERIAL KILLER

        # DEFINE COMO PEGO O ITEM
        personagens_vistos[personagem]=1

    def locais (locais):
        # DEFINE A DESCRICAO DOS LOCAIS VISITADOS
        if locais==0:
            renpy.say("", "Informações sobre a delegacia de polícia foi adicionada ao seu inventário")    # DELEGACIA DE POLICIA
        elif locais==1:
            renpy.say("", "Informações sobre a clínica psiquiatrica foi adicionada ao seu inventário")    # CLINICA
        elif locais==2:
            renpy.say("", "Informações sobre o bar foi adicionada ao seu inventário")                     # BAR
        elif locais==3:
            renpy.say("", "Informações sobre o motel foi adicionada ao seu inventário")                   # MOTEL
        elif locais==4:
            renpy.say("", "Informações sobre o porão foi adicionada ao seu inventário")                   # PORAO

        # DEFINE COMO PEGO O ITEM
        locais_visitados[locais]=1

# INICIO DO JOGO
label start:
    # DECLARA AS VARIAVEIS
    call game_variables from _call_game_variables

    # PARA A MUSICA DO MENU PRINCIPAL
    stop music fadeout 1.0

    # SCENE-0001 - CONSULTORIO, PACIENTE 01
    call psychiatrist from _call_psychiatrist

    # FINALIZA O JOGO
    return
