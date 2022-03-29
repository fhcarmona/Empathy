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

        rev "EDIÇÃO ESPECIAL: PSICOPATAS"
        rev "Reveja o Caso da Quarta Vítima Encontrada no Porão"
        rev "Na Pele de um Investigador: Como funciona uma investigação"
        rev "Psicopatia: Um enigma a ser explorado"
    elif artigo==2:
        # DEFINE COMO REVISTA VISTA
        $revista[1]=1

        rev "Mente Humana: Como é o funcionamento da mente humana?"
        rev "Doutora [doutora] Explica um Pouco Sobre Psiquiatria"
        rev "Situação dos Presídios: Uma situação de saúde mental?"

    return
