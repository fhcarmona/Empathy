# AUTHOR: PERALTA GAMES
# SCOPE: SURTO DO PACIENTE 02 CONTRA A PSIQUIATRA

label scene_0003:
    scene black

    tln "03/08/2016 - 10:08h | CONSULTÓRIO PSIQUIATRA"

    # LIMPA A TELA E MOSTRA O AMBIENTE CONSULTORIO
    scene clinic
    with dissolve

    psi "Agora irei preescrever alguns exames para você fazer, me informe assim que receber os resultados"
    psi "Após o resultado, retorne a mim e irei prescrever os remédios necessários para o tratamento adequado"
    p02 "Sem remédios doutora, não preciso deles"
    psi "Após os exames verificarei se precisará ou não"
    p02 "NÃO!"
    p02 "VOCÊ NÃO ENTENDE!"
    psi "[p02_nome], se acalme..."
    seg "SAI DE PERTO DELA!"

    return
