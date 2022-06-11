# AUTHOR: PERALTA GAMES
# SCOPE:

label scene_0600:
    hide screen cluesUI

    scene black

    tln "12/05/2022 - 10:57h | RUA"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene street
    with dissolve

    show screen cluesUI

    #
    $ narrative_image("acp", right, None, acp, "O que dois investigadores estariam fazendo aqui?")
    $ narrative_image("i01", left, None, i01, "Você foi a última pessoa a estar em contato com a vítima")
    $ narrative_image("acp", right, None, acp, "Ele está morto!?")
    $ narrative_image("i02", left, None, i02, "Sim, ele está morto, poderia nos contar como foi a última vez que o viu?")
    $ narrative_image("acp", right, None, acp, "Oh meu deus!")
    $ narrative_image("acp", right, None, acp, "Nós iriamos ficar durante a noite, mas ele foi repentinamente embora")
    $ narrative_image("i02", left, None, i02, "O que aconteceu?")
    $ narrative_image("acp", right, None, acp, "Ele recebeu uma ligação, ficou um pouco desesperado e saiu")
    $ narrative_image("i02", left, None, i02, "Lembra de algo que ele tenha dito ou escutado desse telefonema?")
    $ narrative_image("acp", right, None, acp, "Não deu para entender muito bem... Parecia que era uma mulher gritando no telefone")
    $ narrative_image("acp", right, None, acp, "Ele me disse que teria que ajudar uma parente dele, pediu desculpas e saiu")
    $ narrative_image("acp", right, None, acp, "Foi tudo bem repentino, não consegui nem me despedir direito")
    $ narrative_image("i01", left, None, i01, "Saberia dizer qual o horário do ocorrido? E o que fez depois disso?")
    $ narrative_image("acp", right, None, acp, "Deve ter sido por volta das 02:00h")
    $ narrative_image("acp", right, None, acp, "Depois que ele saiu eu fiquei no motel até amanhacer e voltei para casa")
    $ narrative_image("i02", left, None, i02, "Está certo, muito obrigado pela colaboração")
    $ narrative_image("i01", left, None, i01, "Por questões de segurança, peço que caso vá sair da cidade nos contacte, aqui está nosso cartão")
    $ narrative_image("acp", right, None, acp, "Eu estou sobre algum risco?")
    $ narrative_image("i01", left, None, i01, "De forma nenhuma, pode ficar tranquila, caso algo aconteça não tenha receio de ligar")
    $ narrative_image("acp", right, None, acp, "Está certo...")

    # ADICIONA INFORMACA DO PERSONAGEM NO INVENTARIO
    $ personagens(0)

    return
