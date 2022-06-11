# AUTHOR: PERALTA GAMES
# SCOPE: CONVERSA COM O GARI SOBRE A TERCEIRA VITIMA

label scene_0300:
    hide screen cluesUI

    scene black

    tln "06/05/2022 - 09:23h | PARQUE"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene park-body-location
    with dissolve

    show screen cluesUI

    $ narrative_image("gar", right, None, gar, "Era aproximadamente seis horas da manhã, no dia que encontrei o corpo eu estava rotacionando o local de limpeza")
    $ narrative_image("gar", right, None, gar, "Limpando o local mais distante da praça, notei que havia uma roupa em um arbusto")
    $ narrative_image("gar", right, None, gar, "Descendo um pequeno declínio, vi uma pessoa desacordada")
    $ narrative_image("gar", right, None, gar, "A primeiro momento contatei meu colega e pedi para ele contactar a ambulância")
    $ narrative_image("gar", right, None, gar, "Enquanto ele ligava desci para tentar acordar a pessoa, mas só depois de um tempo notei que estava morto")
    $ narrative_image("i02", left, None, i02, "O que fez você imaginar que ele estava desacordado?")
    $ narrative_image("gar", right, None, gar, "Normalmente este rapaz sempre estava perto da região, em alguns bares")
    $ narrative_image("gar", right, None, gar, "Não é incomum encontrar ele jogado")
    $ narrative_image("i02", left, None, i02, "Conhece algum familiar?")
    $ narrative_image("gar", right, None, gar, "Acredito que não, mesmo eu cuidando da região a algum tempo, nunca vi nenhum parente dele")
    $ narrative_image("i02", left, None, i02, "Sabe se ele tinha alguma inimizade?")
    $ narrative_image("gar", right, None, gar, "Não, nenhuma que conheça")
    $ narrative_image("i02", left, None, i02, "Poderia nos informar qual o bar que ele frequentava?")
    $ narrative_image("gar", right, None, gar, "Claro...")

    # ADICIONA INFORMACA DO PERSONAGEM NO INVENTARIO
    $ personagens(3)

    return
