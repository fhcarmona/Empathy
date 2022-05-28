# AUTHOR: PERALTA GAMES
# SCOPE: DEFINIR QUAL JORNAL SERA EXIBIDO

label newspaper(artigo=-1):
    # LIMPA A TELA E MOSTRA O AMBIENTE DO JORNAL
    scene newspaper
    with dissolve

    # DEFINE QUAL JORNAL SERA MOSTRADO
    if artigo==1:
        # DEFINE COMO JORNAL VISTO
        $jornal[0]=1

        $ narrative_image("", default, None, jor, "Recessão Continua e Crise Chega a [pais]") # jor "Recessão Continua e Crise Chega a [pais]"
        $ narrative_image("", default, None, jor, "Criminalidade Aumenta em Regiões de Baixa Renda") # jor "Criminalidade Aumenta em Regiões de Baixa Renda"
        $ narrative_image("", default, None, jor, "Veja Fotos da Viagem do Diretor de \"Delírio\"") # jor "Veja Fotos da Viagem do Diretor de \"Delírio\""
        $ narrative_image("", default, None, jor, "Homem Foge Depois de Atropelamento") # jor "Homem Foge Depois de Atropelamento"

        # ESCOLHA DA PSIQUIATRA DEFINE O QUE OCORRE NO JORNAL
        if psi_001==1:
            $ narrative_image("", default, None, jor, "Visite o Parque Aquático. Desconto Familiar.") # jor "Visite o Parque Aquático. Desconto Familiar."
        else:
            $ narrative_image("", default, None, jor, "Defensor ou Agressor? Pai Hospitaliza Homem em Festa Infantil") # jor "Defensor ou Agressor? Pai Hospitaliza Homem em Festa Infantil"
    elif artigo==2:
        # DEFINE COMO JORNAL VISTO
        $jornal[1]=1

        $ narrative_image("", default, None, jor, "Serial Killer Causa Terror em [estado], Terceira Vítima Encontrada") # jor "Serial Killer Causa Terror em [estado], Terceira Vítima Encontrada"
        $ narrative_image("", default, None, jor, "Crise Continua Aumentando") # jor "Crise Continua Aumentando"
        $ narrative_image("", default, None, jor, "Moradores de [cidade], Relatam Apagões") # jor "Moradores de [cidade], Relatam Apagões"
    elif artigo==3:
        # DEFINE COMO JORNAL VISTO
        $jornal[2]=1

        $ narrative_image("", default, None, jor, "Precarização das Forças de Seguranças") # jor "Precarização das Forças de Seguranças"
        $ narrative_image("", default, None, jor, "Ministro Indica \"Estar Preparado\" Para Crise da Guerra") # jor "Ministro Indica \"Estar Preparado\" Para Crise da Guerra"
        $ narrative_image("", default, None, jor, "Mulher é Encontrada com Sinais de Afogamento") # jor "Mulher é Encontrada com Sinais de Afogamento"

    return
