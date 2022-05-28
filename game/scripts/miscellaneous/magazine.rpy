# AUTHOR: PERALTA GAMES
# SCOPE: DEFINIR QUAL REVISTA SERA EXIBIDA

label revista(artigo=-1):
    # LIMPA A TELA E MOSTRA O AMBIENTE DA REVISTA
    scene magazine
    with dissolve

    $doutora="Rosana"

    # DEFINE QUAL REVISTA SERA MOSTRADO
    if artigo==1:
        # DEFINE COMO REVISTA VISTA
        $revista[0]=1

        $ narrative_image("", default, None, rev, "EDIÇÃO ESPECIAL: PSICOPATAS") # rev "EDIÇÃO ESPECIAL: PSICOPATAS"
        $ narrative_image("", default, None, rev, "Reveja o Caso da Quarta Vítima Encontrada no Porão") # rev "Reveja o Caso da Quarta Vítima Encontrada no Porão"
        $ narrative_image("", default, None, rev, "Na Pele de um Investigador: Como funciona uma investigação") # rev "Na Pele de um Investigador: Como funciona uma investigação"
        $ narrative_image("", default, None, rev, "Psicopatia: Um enigma a ser explorado") # rev "Psicopatia: Um enigma a ser explorado"
    elif artigo==2:
        # DEFINE COMO REVISTA VISTA
        $revista[1]=1

        $ narrative_image("", default, None, rev, "Mente Humana: Como é o funcionamento da mente humana?") # rev "Mente Humana: Como é o funcionamento da mente humana?"
        $ narrative_image("", default, None, rev, "Doutora [doutora] Explica um Pouco Sobre Psiquiatria") # rev "Doutora [doutora] Explica um Pouco Sobre Psiquiatria"
        $ narrative_image("", default, None, rev, "Situação dos Presídios: Uma situação de saúde mental?") # rev "Situação dos Presídios: Uma situação de saúde mental?"

    return
