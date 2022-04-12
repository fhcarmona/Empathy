# AUTHOR: PERALTA GAMES
# SCOPE:

label scene_0800:
    scene black

    tln "12/05/2022 - 19:01h | CASA DA PRIMA DA VITIMA"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene pri-house-entrance
    with dissolve

    #
    p03 "Querem um café? Água?"
    i01 "Não será necessário"
    i02 "Podemos fazer algumas perguntas?"
    p03 "Claro, sem problemas"
    i01 "Recentemente você entrou em contato com o seu primo? Poderia nos informar como foi a última interação com ele?"
    p03 "Eu liguei para ele durante a noite, para ele vir me ajudar, eu estava entrando em uma crise"
    i02 "Que tipo de crise?"
    p03 "Entre em contato com a minha psiquiatra, eu ainda não consigo falar abertamente sobre o assunto"
    i01 "Entendo, poderia nos passar o número da sua psiquiatra?"
    p03 "Claro, ela se chama [psi_nome], aqui está o contato dela"
    i02 "A senhorita [psi_nome] é a sua psiquiatra?"
    p03 "Sim, ela está me ajudando bastante a lidar com essas situações"
    i01 "Que coincidência em [i02_nome]?"
    i02 "Pois é, vamos fazer uma novo visita a ela"
    i02 "Iremos retornar assim que possível, muito obrigado pelos esclarecimentos"

    return
