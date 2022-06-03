# AUTHOR: PERALTA GAMES
# SCOPE: VISITA DOS INVESTIGADORES AO CONSULTORIO DA PSIQUIATRA

label scene_0005:
    scene black

    tln "18/04/2022 - 09:11h | CLINICA CONSULTÓRIO"

    # LIMPA A TELA E MOSTRA O AMBIENTE CONSULTORIO
    scene clinic
    with dissolve

    $ narrative_image("i01", right, None, i01, "Seu paciente [psi_nome], a quanto tempo o tratava?")
    $ narrative_image("psi", left, None, psi, "Faz pouco tempo, um momento, vou pegar o caso dele")
    $ narrative_image("psi", left, None, psi, "Três meses para ser mais exata")
    $ narrative_image("psi", left, None, psi, "Foi definido por uma decisão juridica que ele deveria buscar uma psiquiatra")
    $ narrative_image("psi", left, None, psi, "Desde então, tenho consulta uma vez por semana")
    $ narrative_image("i01", right, None, i01, "Conseguiria descrever a última sessão do [p01_nome]?")
    $ narrative_image("psi", left, None, psi, "Última sessão? Claro, conversávamos sobre os sonhos que estavam ocorrendo")
    $ narrative_image("i02", right, None, i02, "Sonhos? Que tipo de sonhos?")
    $ narrative_image("psi", left, None, psi, "Ele descrevia a dor de imaginar sua filha sofrendo, se sentindo impotente")
    $ narrative_image("i01", right, None, i01, "Como imaginavamos [i02_nome]...")
    $ narrative_image("i02", right, None, i02, "Sim, doutora [psi_nome], recentemente o [p01_nome] teve um surto e ele está atualmente preso")
    $ narrative_image("psi", left, None, psi, "Surto? O que aconteceu?")

    if psi_001==0:
        $ narrative_image("i01", right, None, i01, "Ele começou a ficar agressivo e agrediu um homem na festa de uma amiga da filha")
        $ narrative_image("i01", right, None, i01, "Só conseguiram conter a agressão depois de algum tempo")
        $ narrative_image("i02", right, None, i02, "Infelizmente foi determinado a prisão do [p01_nome]")
    else:
        $ narrative_image("i01", right, None, i01, "Ele começou a ficar agressivo e quase agrediu um homem na festa de uma amiga da filha")
        $ narrative_image("i01", right, None, i01, "Começou a ficar agressivo após ver a filha no colo do pai da aniversariante")
        $ narrative_image("i02", right, None, i02, "Por sorte o surto dele foi controlado, mas isso infligiu a determinação jurídica e ele voltará a prisão")

    $ narrative_image("psi", left, None, psi, "Nossa...")
    $ narrative_image("i01", right, None, i01, "E por determinação do delegado estamos aqui para entender melhor sobre o caso dele")
    $ narrative_image("i02", right, None, i02, "Esse surto é incomum para quem está em tratamento, certo?")
    $ narrative_image("psi", left, None, psi, "Certo...")
    $ narrative_image("i02", right, None, i02, "Algum medicamento poderia ter causado o surto?")
    $ narrative_image("psi", left, None, psi, "O que está querendo sugerir com isso? Que indiquei tratamento errado de propósito?")
    $ narrative_image("i02", right, None, i02, "Não se ofenda doutora, estamos apenas investigando. Poderia causar um surto?")
    $ narrative_image("psi", left, None, psi, "Não, de forma nenhuma.")
    $ narrative_image("psi", left, None, psi, "A prescrição era para controlar os surtos")

    return
