# AUTHOR: PERALTA GAMES
# SCOPE: VISITA DOS INVESTIGADORES AO CONSULTORIO DA PSIQUIATRA

label scene_0005:
    scene black

    tln "18/04/2022 - 09:11h | CLINICA CONSULTÓRIO"

    # LIMPA A TELA E MOSTRA O AMBIENTE CONSULTORIO
    scene clinic
    with dissolve

    i01 "Seu paciente [psi_nome], a quanto tempo o tratava?"
    psi "Faz pouco tempo, um momento, vou pegar o caso dele"
    psi "Três meses para ser mais exata"
    psi "Foi definido por uma decisão juridica que ele deveria buscar uma psiquiatra"
    psi "Desde então, tenho consulta uma vez por semana"
    i01 "Conseguiria descrever a última sessão do [p01_nome]?"
    psi "Última sessão? Claro, conversávamos sobre os sonhos que estavam ocorrendo"
    i02 "Sonhos? Que tipo de sonhos?"
    psi "Ele descrevia a dor de imaginar sua filha sofrendo, se sentindo impotente"
    i01 "Como imaginavamos [i02_nome]..."
    i02 "Sim, doutora [psi_nome], recentemente o [p01_nome] teve um surto e ele está atualmente preso"
    psi "Surto? O que aconteceu?"

    if psi_001==0:
        i01 "Ele começou a ficar agressivo e agrediu um homem na festa de uma amiga da filha"
        i01 "Só conseguiram conter a agressão depois de algum tempo"
        i02 "Infelizmente foi determinado a prisão do [p01_nome]"
    else:
        i01 "Ele começou a ficar agressivo e quase agrediu um homem na festa de uma amiga da filha"
        i01 "Começou a ficar agressivo após ver a filha no colo do pai da aniversariante"
        i02 "Por sorte o surto dele foi controlado, mas isso infligiu a determinação jurídica e ele voltará a prisão"

    psi "Nossa..."
    i01 "E por determinação do delegado estamos aqui para entender melhor sobre o caso dele"
    i02 "Esse surto é incomum para quem está em tratamento, certo?"
    psi "Certo..."
    i02 "Algum medicamento poderia ter causado o surto?"
    psi "O que está querendo sugerir com isso? Que indiquei tratamento errado de propósito?"
    i02 "Não se ofenda doutora, estamos apenas investigando. Poderia causar um surto?"
    psi "Não, de forma nenhuma."
    psi "A prescrição era para controlar os surtos"

    return
