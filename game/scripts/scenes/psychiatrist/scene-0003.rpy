# AUTHOR: PERALTA GAMES
# SCOPE: SURTO DO PACIENTE 02 CONTRA A PSIQUIATRA

label scene_0003:
    scene black

    tln "03/08/2016 - 10:08h | CONSULTÓRIO PSIQUIATRA"

    # LIMPA A TELA E MOSTRA O AMBIENTE CONSULTORIO
    scene clinic
    with dissolve

    $ narrative_image("psi", left, None, psi, "Agora irei preescrever alguns exames para você fazer, me informe assim que receber os resultados") # psi "Agora irei preescrever alguns exames para você fazer, me informe assim que receber os resultados"
    $ narrative_image("psi", left, None, psi, "Após o resultado, retorne a mim e irei prescrever os remédios necessários para o tratamento adequado") # psi "Após o resultado, retorne a mim e irei prescrever os remédios necessários para o tratamento adequado"
    $ narrative_image("p02", right, None, p02, "Sem remédios doutora, não preciso deles") # p02 "Sem remédios doutora, não preciso deles"
    $ narrative_image("psi", left, None, psi, "Após os exames verificarei se precisará ou não") # psi "Após os exames verificarei se precisará ou não"
    $ narrative_image("p02", right, None, p02, "NÃO!") # p02 "NÃO!"
    $ narrative_image("p02", right, None, p02, "VOCÊ NÃO ENTENDE!") # p02 "VOCÊ NÃO ENTENDE!"
    $ narrative_image("psi sad", left, None, psi, "[p02_nome], se acalme...") # psi "[p02_nome], se acalme..."
    $ narrative_image("psi sad", left, None, psi, "SEGURANÇA!") # psi "[p02_nome], se acalme..."
    $ narrative_image("seg", right, None, seg, "SAI DE PERTO DELA!") # seg "SAI DE PERTO DELA!"
    $ narrative_image("psi sad", left, None, seg, "Minha... garganta") # psi sad "Minha... garganta"

    return
