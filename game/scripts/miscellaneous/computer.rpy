# AUTHOR: PERALTA GAMES
# SCOPE: DEFINIR QUAL TELA DO COMPUTADOR SERA EXIBIDA

label computador(artigo=-1):
    # LIMPA A TELA E MOSTRA O AMBIENTE DO COMPUTADOR
    scene psy-house
    with dissolve

    # DEFINE QUAL TELA DO COMPUTADOR SERA MOSTRADO
    if artigo==1:
        $ narrative_image("", default, None, com, "Encontrada terceira vítima afogada") # com "Encontrada terceira vítima afogada"

        menu:
            "Ler mais?"

            "Sim, ler mais sobre a notícia":
                $ narrative_image("", default, None, com, "...Não foram constatados sinais de luta, indicação é que vítima estava desacordada...") # com "...Não foram constatados sinais de luta, indicação é que vítima estava desacordada..."
                $ narrative_image("", default, None, com, "... vítima foi encontrada atrás de um arbusto, perto da lagoa em uma praça na região de [bairro]...") # com "... vítima foi encontrada atrás de um arbusto, perto da lagoa em uma praça na região de [bairro]..."
                $ narrative_image("", default, None, com, "O gari que encontrou a vítima, admite choque e relata problemas na iluminação da região") # com "O gari que encontrou a vítima, admite choque e relata problemas na iluminação da região"

            "Não":
                $ narrative_image("psi", left, None, psi, "Já li bastante sobre esses casos") # psi "Já li bastante sobre esses casos"

        $ narrative_image("", default, None, com, "Falsas Pistas da População Ofusca Investigação, Indica Delegado.") # com "Falsas Pistas da População Ofusca Investigação, Indica Delegado."

        menu:
            "Ler mais?"

            "Sim, ler mais sobre a notícia":
                $ narrative_image("", default, None, com, "...\"Estamos advertindo algumas pessoas, devido a informações não condizentes com fatos.") # com "...\"Estamos advertindo algumas pessoas, devido a informações não condizentes com fatos."
                $ narrative_image("", default, None, com, "Agracedemos a população pelo auxílio, pedimos que aguardem o rumo da investigação, temos uma força exclusiva para o caso.\" Relata o delegado responsável") # com "Agracedemos a população pelo auxílio, pedimos que aguardem o rumo da investigação, temos uma força exclusiva para o caso.\" Relata o delegado responsável"
                $ narrative_image("", default, None, a01, "Esse delegado é igual ao anterior, sentado em cima da investigação!") # a01 "Esse delegado é igual ao anterior, sentado em cima da investigação!"
                $ narrative_image("", default, None, a02, "Meu vizinho não sai de casa, fico pensando o que ele faz com tantos gatos, talvez não goste de pessoas. Estou de olho, nunca se sabe...") # a02 "Meu vizinho não sai de casa, fico pensando o que ele faz com tantos gatos, talvez não goste de pessoas. Estou de olho, nunca se sabe..."
                $ narrative_image("", default, None, a03, "Juro que na rua Leopoldo, perto da bar, vi uma movimentação esquisita durante a noite, quando sai tinha uma trilha de água, mas não me toquei o que poderia ter sido") # a03 "Juro que na rua Leopoldo, perto da bar, vi uma movimentação esquisita durante a noite, quando sai tinha uma trilha de água, mas não me toquei o que poderia ter sido"
                $ narrative_image("psi", left, None, psi, "Estou cansada, vou dar um pulo no bar.") # psi "Estou cansada, vou dar um pulo no bar."

            "Não, ir para o bar":
                $ narrative_image("psi", left, None, psi, "Estou cansada, vou dar um pulo no bar.") # psi "Estou cansada, vou dar um pulo no bar."

    return
