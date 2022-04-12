# AUTHOR: PERALTA GAMES
# SCOPE:

label scene_0600:
    scene black

    tln "12/05/2022 - 10:57h | RUA"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene street
    with dissolve

    #
    acp "O que dois investigadores estariam fazendo aqui?"
    i01 "Você foi a última pessoa a estar em contato com a vítima"
    acp "Ele está morto!?" # SURPRESA
    i02 "Sim, ele está morto, poderia nos contar como foi a última vez que o viu?"
    acp "Oh meu deus!" # CHOCADA
    acp "Nós iriamos ficar durante a noite, mas ele foi repentinamente embora"
    i02 "O que aconteceu?"
    acp "Ele recebeu uma ligação, ficou um pouco desesperado e saiu"
    i02 "Lembra de algo que ele tenha dito ou escutado desse telefonema?"
    acp "Não deu para entender muito bem... Parecia que era uma mulher gritando no telefone"
    acp "Ele me disse que teria que ajudar a prima dele, pediu desculpas e saiu"
    acp "Foi tudo bem repentino, não consegui nem me despedir direito"
    i01 "Saberia dizer qual o horário do ocorrido? E o que fez depois disso?"
    acp "Deve ter sido por volta das 02:00h"
    acp "Depois que ele saiu eu fiquei no motel até amanhacer e voltei para casa"
    i02 "Está certo, muito obrigado pela colaboração"
    i01 "Por questões de segurança, peço que caso vá sair da cidade nos contacte, aqui está nosso cartão"
    acp "Eu estou sobre algum risco?"
    i01 "De forma nenhuma, pode ficar tranquila, caso algo aconteça não tenha receio de ligar"
    acp "Está certo..."

    return
