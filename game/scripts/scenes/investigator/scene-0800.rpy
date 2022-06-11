# AUTHOR: PERALTA GAMES
# SCOPE:

label scene_0800:
    hide screen cluesUI

    scene black

    tln "12/05/2022 - 19:01h | RESIDÊNCIA DE CAMILA"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene pri-house-entrance
    with dissolve

    show screen cluesUI

    #
    $ narrative_image("p03", right, None, p03, "Querem um café? Água?")
    $ narrative_image("i01", left, None, i01, "Não será necessário")
    $ narrative_image("i02", left, None, i02, "Podemos fazer algumas perguntas?")
    $ narrative_image("p03", right, None, p03, "Claro, sem problemas")
    $ narrative_image("i01", left, None, i01, "Recentemente você entrou em contato com o seu irmão? Poderia nos informar como foi a última interação com ele?")
    $ narrative_image("p03", right, None, p03, "Eu liguei para ele durante a noite, para ele vir me ajudar, eu estava entrando em uma crise")
    $ narrative_image("i02", left, None, i02, "Que tipo de crise?")
    $ narrative_image("p03", right, None, p03, "Entre em contato com a minha psiquiatra, eu ainda não consigo falar abertamente sobre o assunto")
    $ narrative_image("i01", left, None, i01, "Entendo, poderia nos passar o número da sua psiquiatra?")
    $ narrative_image("p03", right, None, p03, "Claro, ela se chama [psi_nome], aqui está o contato dela")
    $ narrative_image("i02", left, None, i02, "A senhorita [psi_nome] é a sua psiquiatra?")
    $ narrative_image("p03", right, None, p03, "Sim, ela está me ajudando bastante a lidar com essas situações")
    $ narrative_image("i01", left, None, i01, "Que coincidência em [i02_nome]?")
    $ narrative_image("i02", left, None, i02, "Pois é, vamos fazer uma novo visita a ela")
    $ narrative_image("i02", left, None, i02, "Iremos retornar assim que possível, muito obrigado pelos esclarecimentos")

    # ADICIONA INFORMACA DO PERSONAGEM NO INVENTARIO
    $ personagens(5)

    return
