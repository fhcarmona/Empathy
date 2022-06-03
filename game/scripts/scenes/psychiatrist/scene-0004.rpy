# AUTHOR: PERALTA GAMES
# SCOPE: VISITA DOS INVESTIGADORES AO CONSULTORIO DA PSIQUIATRA

label scene_0004:
    scene black

    tln "18/04/2022 - 09:03h | CONSULTÓRIO RECEPÇÃO"

    # LIMPA A TELA E MOSTRA O AMBIENTE CONSULTORIO
    scene clinic-reception
    with dissolve

    $ narrative_image("i01", right, None, i01, "Bom dia [psi_nome], somos os [i02_nome] e este é o [i01_nome], somos responsáveis pelo caso de um de seus pacientes")
    $ narrative_image("i01", right, None, i01, "Poderia nos ajudar com algumas questões?")
    $ narrative_image("psi", left, None, psi, "Claro, mas só posso entrar em certos detalhes com ordem judicial, o senhores a possuem?")
    $ narrative_image("i02", right, None, i02, "Sim, aqui está doutora")
    $ narrative_image("psi", left, None, psi, "Hum...")
    $ narrative_image("psi", left, None, psi, "Vejo que é sobre o paciente [p01_nome], aconteceu algo com ele?")
    $ narrative_image("i01", right, None, i01, "Não se preocupe quanto a isso, podemos começar?")
    $ narrative_image("psi", left, None, psi, "Ah, desculpe, claro")
    $ narrative_image("psi", left, None, psi, "Entre comigo, vamos ao consultório")

    return
