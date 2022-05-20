# AUTHOR: PERALTA GAMES
# SCOPE: VISITA DOS INVESTIGADORES AO CONSULTORIO DA PSIQUIATRA

label scene_0004:
    scene black

    tln "18/04/2022 - 09:03h | CONSULTÓRIO RECEPÇÃO"

    # LIMPA A TELA E MOSTRA O AMBIENTE CONSULTORIO
    scene clinic-reception
    with dissolve

    i01 "Bom dia [psi_nome], somos os [i02_nome] e este é o [i01_nome], somos responsáveis pelo caso de um de seus pacientes"
    i01 "Poderia nos ajudar com algumas questões?"
    psi "Claro, mas só posso entrar em certos detalhes com ordem judicial, o senhores a possuem?"
    i02 "Sim, aqui está doutora"
    psi "Hum..."
    psi "Vejo que é sobre o paciente [p01_nome], aconteceu algo com ele?"
    i01 "Não aconteceu nada com ele, podemos começar?"
    psi "Ah, desculpe, claro"
    psi "Entre comigo, vamos ao consultório"

    return
