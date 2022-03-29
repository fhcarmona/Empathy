# AUTHOR: PERALTA GAMES
# SCOPE: VISITA DOS INVESTIGADORES AO CONSULTORIO DA PSIQUIATRA

label scene_0004:
    # LIMPA A TELA E MOSTRA O AMBIENTE CONSULTORIO
    scene clinic
    with dissolve

    $doutora="Rosana"
    $paciente="Douglas"
    $agente_a="Vinicius"
    $agente_b="Welligton"

    i01 "Bom dia Doutora [doutora], somos os agentes [agente_b] e este é o agente [agente_a], somos responsáveis pelo caso de um de seus pacientes"
    i01 "Poderia nos ajudar com algumas questões?"
    psi "Claro, mas só posso entrar em certos detalhes com ordem judicial, o senhores a possuem?"
    i02 "Sim, aqui está doutora"
    psi "Hum..."
    psi "Vejo que é sobre o paciente [paciente], aconteceu algo com ele?"
    i01 "Não aconteceu nada com ele, podemos começar?"
    psi "Ah, desculpe, claro"
    psi "Entre comigo, vamos ao consultório"

    return
