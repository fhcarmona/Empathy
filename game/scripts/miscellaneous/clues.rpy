#default item_description = 0
#default layer_folder = 1
#default niveis_suspeitos=["Testemunha", "Suspeito", "Vítima", "Inocente", "Culpado"]    # NIVEIS DE SUSPEITA

#default personagens_sus=[0, 0, 0, 0, 0, 0, 0, 0, 0]    # NIVEL DE SUSPEITA DE CADA PERSONAGEM DA LISTA DE PERSONAGEM VISTAS [0- TESTEMUNHA, 1- SUSPEITO, 2- VITIMA, 3- INOCENTE, 4- CULPADO]
#default locais_visitados=[1, 1, 1, 1, 1]               # LOCAIS VISITADOS PELOS DETETIVES
#default personagens_vistos=[1, 1, 1, 1, 1, 1, 1, 1, 1] # PERSONAGENS RELEVANTES PARA O INVESTIGADOR

screen cluesUI():
    imagebutton:
        anchor(1.0, 0.0)
        pos(0.995, 0.0)
        idle "gui/clues/clues-icon-idle.png"
        hover "gui/clues/clues-icon-hover.png"
        action ShowMenu('cluesMenu')

screen cluesMenu():
    # TROCA DE PASTA DO INVENTARIO
    if layer_folder == 1:
        add "gui/clues/folder_center.png"
        add "gui/clues/folder_right.png"
        add "gui/clues/folder_left.png"
    elif layer_folder == 2:
        add "gui/clues/folder_left.png"
        add "gui/clues/folder_right.png"
        add "gui/clues/folder_center.png"
    elif layer_folder == 3:
        add "gui/clues/folder_left.png"
        add "gui/clues/folder_center.png"
        add "gui/clues/folder_right.png"

    textbutton _("Evidências"):
        style_prefix "clues_menu_evidencia"

        action SetLocalVariable("item_description", 0), SetLocalVariable("layer_folder", 1)

    textbutton _("Pessoas"):
        style_prefix "clues_menu_pessoas"

        action SetLocalVariable("item_description", 0), SetLocalVariable("layer_folder", 2)

    textbutton _("Locais"):
        style_prefix "clues_menu_locais"

        action SetLocalVariable("item_description", 0), SetLocalVariable("layer_folder", 3)

    # EVIDENCIAS
    if layer_folder == 1:
        # SE INVESTIGADOR TIVER PEGO O LIQUIDO VERDE
        if inventario[0] == 1:
            # IMAGEM
            imagebutton pos (75, 110):
                auto "images/inventory/algae_plate_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 1:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 1)

            # DESCRICAO DO ITEM
            if item_description == 1:
                frame:
                    style_prefix "paperwork_item_description"

                    text "Líquido verde\n\nMaterial encontrado nos pulmões das vítimas, composto por micro-organismos e outros materiais orgânicos"

        # SE INVESTIGADOR TIVER PEGO A DROGA
        if inventario[1] == 1:
            # IMAGEM
            imagebutton pos (200, 110):
                auto "images/inventory/drug_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 2:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 2)

            # DESCRICAO DO ITEM
            if item_description == 2:
                frame:
                    style_prefix "paperwork_item_description"

                    text "Droga\n\nEncontrado no chão do porão da quarta vítima, não foi possível identificar a origem, pode causar mal-estar e em grandes quantidades causar tontura ou morte."

        # SE INVESTIGADOR TIVER PEGO O PENDRIVE
        if inventario[2] == 1:
            # IMAGEM
            imagebutton pos (325, 110):
                auto "images/inventory/pendrive_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 3:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 3)

            # DESCRICAO DO ITEM
            if item_description == 3:
                frame:
                    style_prefix "paperwork_item_description"

                    text "Pendrive\n\nPossui um vídeo de uma mulher com a terceira vítima no elevador, nada fora do padrão é notado. Porém, conseguimos pegar algumas informações da possível última pessoa que estava com a terceira vítima."

    # PESSOAS
    if layer_folder == 2:
        # ACOMPANHANTE
        if personagens_vistos[0] == 1:
            # IMAGEM
            imagebutton pos (75, 110):
                auto "images/characters/miniature/acp_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 1:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 1)

            # DESCRICAO DO ITEM
            if item_description == 1:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text niveis_suspeitos[int(personagens_sus[0])]

                        if personagens_sus[0] == 4:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 0, 0)
                        else:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 0, int(personagens_sus[0]) + 1)

                    text "\n\nNome: Veronica \nProfissão: Modelo\nIdade: 21 anos\nHistórico Criminal: Estelionato, falsidade ideológica\n\nÚltima pessoa a ser vista em um vídeo com a terceira vítima, estava no bar e acompanhou a vítima na saída. Durante a noite no motel, a vítima atendeu o celular, que o fez ir embora."

        # ATENDENTE MOTEL
        if personagens_vistos[1] == 1:
            # IMAGEM
            imagebutton pos (200, 110):
                auto "images/characters/miniature/atm_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 2:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 2)

            # DESCRICAO DO ITEM
            if item_description == 2:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text niveis_suspeitos[int(personagens_sus[1])]

                        if personagens_sus[1] == 4:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 1, 0)
                        else:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 1, int(personagens_sus[1]) + 1)

                    text "\n\nNome: Jessica\nProfissão: Recepcionista\nIdade: 27 anos\nHistórico Criminal: Nenhuma ocorrência\n\nA atendente do motel onde a terceira vítima frequentou no dia de sua morte. Nos foi entregue um pendrive contendo imagens da acompanhante junto a terceira vítima que conheceu no bar da região."

        # BARMAN
        if personagens_vistos[2] == 1:
            # IMAGEM
            imagebutton pos (325, 110):
                auto "images/characters/miniature/bmn_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 3:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 3)

            # DESCRICAO DO ITEM
            if item_description == 3:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text niveis_suspeitos[int(personagens_sus[2])]

                        if personagens_sus[2] == 4:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 2, 0)
                        else:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 2, int(personagens_sus[2]) + 1)

                    text "\n\nNome: Carlos\nProfissão: Barman\nIdade: 31 anos\nHistórico Criminal: Desacato\n\nAtendente do bar onde a terceira vítima frequentava, nos informou que a vítima saiu com uma mulher na noite do acontecido e que a vítima possui uma irmã bastarda."

        # GARRY
        if personagens_vistos[3] == 1:
            # IMAGEM
            imagebutton pos (450, 110):
                auto "images/characters/miniature/gar_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 4:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 4)

            # DESCRICAO DO ITEM
            if item_description == 4:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text niveis_suspeitos[int(personagens_sus[3])]

                        if personagens_sus[3] == 4:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 3, 0)
                        else:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 3, int(personagens_sus[3]) + 1)

                    text "\n\nNome: Pedro\nProfissão: Gari\nIdade: 23 anos\nHistórico Criminal: Nenhuma ocorrência\n\nPedro trabalha na região onde a terceira vítima foi localizada. A vítima foi encontrada em um mato no parque com algumas roupas rasgadas devido aos arbustos. Pedro nos indicou a pista de um bar que a terceira vítima frequentava."

        # PACIENTE 01
        if personagens_vistos[4] == 1:
            # IMAGEM
            imagebutton pos (75, 275):
                auto "images/characters/miniature/p01_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 5:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 5)

            # DESCRICAO DO ITEM
            if item_description == 5:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text niveis_suspeitos[int(personagens_sus[4])]

                        if personagens_sus[4] == 4:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 4, 0)
                        else:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 4, int(personagens_sus[4]) + 1)

                    text "\n\nNome: Douglas\nProfissão: Operador de Piscina\nIdade: 33 anos\nHistórico Criminal: Agressão, stalking, tentativa de homícidio\n\nDouglas preso por agressão que ocorreu em uma festa infantil. Estava sobre o julgamento por stalking e estava obrigado a frequentar uma psiquiatra devido a explosões de agressividade."

        # PACIENTE 03
        if personagens_vistos[5] == 1:
            # IMAGEM
            imagebutton pos (200, 275):
                auto "images/characters/miniature/p03_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 6:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 6)

            # DESCRICAO DO ITEM
            if item_description == 6:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text niveis_suspeitos[int(personagens_sus[5])]

                        if personagens_sus[5] == 4:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 5, 0)
                        else:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 5, int(personagens_sus[5]) + 1)

                    text "\n\nNome: Camila\nProfissão: Escritora\nIdade: 26 anos\nHistórico Criminal: Nenhuma ocorrência\n\nIrmã bastarda da terceira vítima. Frequenta o consultório da psiquiatra Rosana, nos informou que ligou para o irmão quando o mesmo estava no motel com Veronica devido a uma crise de ansiedade que estava ocorrendo com ela."

        # PSIQUIATRA
        if personagens_vistos[6] == 1:
            # IMAGEM
            imagebutton pos (325, 275):
                auto "images/characters/miniature/psi_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 7:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 7)

            # DESCRICAO DO ITEM
            if item_description == 7:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text niveis_suspeitos[int(personagens_sus[6])]

                        if personagens_sus[6] == 4:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 6, 0)
                        else:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 6, int(personagens_sus[6]) + 1)

                    text "\n\nNome: Rosana\nProfissão: Psiquiatra\nIdade: 36 anos\nHistórico Criminal: Nenhuma ocorrência\n\nPsiquiatra que trabalha com foco em agressões e traumas. Já foi a diversos programas para conversar sobre psiquiatria e possui uma lista enorme de méritos em sua carreira. Responsável pelo tratamento de Douglas, indicado pela juíza do caso."

        # SERIAL KILLER
        if personagens_vistos[7] == 1:
            # IMAGEM
            imagebutton pos (450, 275):
                auto "images/characters/miniature/skr_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 8:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 8)

            # DESCRICAO DO ITEM
            if item_description == 8:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text niveis_suspeitos[int(personagens_sus[7])]

                        if personagens_sus[7] == 4:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 7, 0)
                        else:
                            textbutton "(Trocar)":
                                action SetDict(personagens_sus, 7, int(personagens_sus[7]) + 1)

                    text "\n\nNome: Lector\nProfissão: Desempregado\nIdade: 38 anos\nHistórico Criminal: Agressão, Desacato\n\nAssassino das três vítimas, encontrado sem vida no porão de sua casa devido a um corte em sua jugular feito pela doutora Rosana que estava sendo mantida em cativeiro. Foi encontrado um cultivo de algas e outros itens em sua residência."

    # LOCAIS
    if layer_folder == 3:
        # ESTACAO DE POLICIA
        if locais_visitados[0] == 1:
            # IMAGEM
            imagebutton pos (75, 110):
                auto "images/scenes/miniature/police-station_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 1:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 1)



            # DESCRICAO DO ITEM
            if item_description == 1:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text "Delegacia de Polícia"

                    text "\n\nLocalizada perto do centro da cidade a única delegacia da cidade normalmente é pouco movimentada, sem grandes detalhes."

        # CLINICA
        if locais_visitados[1] == 1:
            # IMAGEM
            imagebutton pos (200, 110):
                auto "images/scenes/miniature/clinic_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 2:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 2)

            # DESCRICAO DO ITEM
            if item_description == 2:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text "Clínica Psiquiatrica"

                    text "\n\nClínica de uma famosa psiquiatra Rosana."

        # BAR
        if locais_visitados[2] == 1:
            # IMAGEM
            imagebutton pos (325, 110):
                auto "images/scenes/miniature/bar_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 3:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 3)

            # DESCRICAO DO ITEM
            if item_description == 3:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text "Bar"

                    text "\n\nBar onde a terceira vítima frequentava."

        # MOTEL
        if locais_visitados[3] == 1:
            # IMAGEM
            imagebutton pos (75, 275):
                auto "images/scenes/miniature/motel_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 4:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 4)

            # DESCRICAO DO ITEM
            if item_description == 4:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text "Motel"

                    text "\n\nUm dos quatro motéis mais próximos ao bar onde a terceira vítima frequentava, foi possível identificar que a terceira vítima foi até o local no dia do seu assassinato. Obtivemos um vídeo do acontecimento e foi entregue em um pendrive."

        # PORAO
        if locais_visitados[4] == 1:
            # IMAGEM
            imagebutton pos (200, 275):
                auto "images/scenes/miniature/basement_%s.png"

                # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
                if item_description == 5:
                    action SetLocalVariable("item_description", 0)
                else:
                    action SetLocalVariable("item_description", 5)

            # DESCRICAO DO ITEM
            if item_description == 5:
                frame:
                    style_prefix "paperwork_item_description"

                    hbox:
                        text "Porão do Serial Killer"

                    text "\n\nLocal onde a doutora Rosana estava sendo mantida presa. O porão possui isolamento acústico, a polícia foi chamada ao local devido ao barulho de tiro na tentativa de fuga da doutora."

    # BOTAO PARA FECHAR O INVENTARIO
    textbutton _("X"):
        style_prefix "clues_menu_fechar"

        action Return()

# ESTILOS
style paperwork_item_description_frame:
    xsize 550
    ysize 550
    background "#FFFFFF55"
    pos (630, 110)
    padding (25, 25)

style paperwork_item_description_text:
    color "#000"
    font "fonts/pincel_handwrite.ttf"

style paperwork_item_description_button_text:
    color "#000"
    font "fonts/pincel_handwrite.ttf"
    bold True
    size 20
    hover_color "#683f31"

style clues_menu_evidencia_button:
    pos (200, 40)

style clues_menu_evidencia_button_text:
    color "#000"
    hover_color "#683f31"

style clues_menu_pessoas_button:
    pos (600, 40)

style clues_menu_pessoas_button_text:
    color "#000"
    hover_color "#683f31"

style clues_menu_locais_button:
    pos (1000, 40)

style clues_menu_locais_button_text:
    color "#000"
    hover_color "#683f31"

style clues_menu_fechar_button:
    pos (75, 640)

style clues_menu_fechar_button_text:
    color "#000"
    hover_color "#683f31"
