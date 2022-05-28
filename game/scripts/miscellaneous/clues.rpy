screen cluesUI():
    imagebutton:
        anchor(1.0, 0.0)
        pos(0.995, 0.0)
        idle "gui/clues/clues-icon-idle.png"
        hover "gui/clues/clues-icon-hover.png"
        action ShowMenu('cluesMenu')

screen cluesMenu():
    default item_description = 0

    tag clues
    add "gui/clues/folder-paperwork.png"

    # SE INVESTIGADOR TIVER PEGO O LIQUIDO VERDE
    if inventario[0] == 1:
        # IMAGEM
        imagebutton pos (75, 30):
            auto "images/inventory/algae_plate_%s.png"

            # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
            if item_description == 1:
                action SetLocalVariable("item_description", 0)
            else:
                action SetLocalVariable("item_description", 1)

        # DESCRICAO DO ITEM
        if item_description == 1:
            vbox:
                style_prefix "paperwork_item_description"

                text "Líquido verde\n\nMaterial encontrado nos pulmões das vítimas, composto por microorganismos e outros materiais orgânicos"

    # SE INVESTIGADOR TIVER PEGO A DROGA
    if inventario[1] == 1:
        # IMAGEM
        imagebutton pos (200, 30):
            auto "images/inventory/drug_%s.png"

            # DEFINE SE TEXTO DE DESCRICAO SERA MOSTRADO OU NAO
            if item_description == 2:
                action SetLocalVariable("item_description", 0)
            else:
                action SetLocalVariable("item_description", 2)

        # DESCRICAO DO ITEM
        if item_description == 2:
            vbox:
                style_prefix "paperwork_item_description"

                text "Droga\n\nEncontrado no chão do porão da quarta vítima, não foi possível indentificar a origem, pode causar mal estar e em grandes quantidades causar tontura e ou morte."

    # BOTAO PARA FECHAR O INVENTARIO
    textbutton _("Voltar"):
        style "clues_menu_voltar"

        action Return()

# ESTILOS
style paperwork_item_description_vbox:
    xsize 500
    ysize 600
    pos (600, 50)

style paperwork_item_description_text:
    color "#000"
    font "fonts/pincel_handwrite.ttf"

style clues_menu_voltar is button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -20
    xoffset 30
