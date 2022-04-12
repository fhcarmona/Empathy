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

        jor "Recessão Continua e Crise Chega a [pais]"
        jor "Criminalidade Aumenta em Regiões de Baixa Renda"
        jor "Veja Fotos da Viagem do Diretor de \"Delírio\""
        jor "Homem Foge Depois de Atropelamento"

        # ESCOLHA DA PSIQUIATRA DEFINE O QUE OCORRE NO JORNAL
        if psi_001==1:
            jor "Visite o Parque Aquático. Desconto Familiar."
        else:
            jor "Defensor ou Agressor? Pai Hospitaliza Homem em Festa Infantil"
    elif artigo==2:
        # DEFINE COMO JORNAL VISTO
        $jornal[1]=1

        jor "Serial Killer Causa Terror em [estado], Terceira Vítima Encontrada"
        jor "Crise Continua Aumentando"
        jor "Moradores de [cidade], Relatam Apagões"
    elif artigo==3:
        # DEFINE COMO JORNAL VISTO
        $jornal[2]=1

        jor "Precarização das Forças de Seguranças"
        jor "Ministro Indica \"Estar Preparado\" Para Crise da Guerra"
        jor "Mulher é Encontrada com Sinais de Afogamento"

    return
