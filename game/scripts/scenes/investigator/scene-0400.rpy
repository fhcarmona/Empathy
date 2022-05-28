# AUTHOR: PERALTA GAMES
# SCOPE:

label scene_0400:
    hide screen cluesUI
    
    scene black

    tln "06/05/2022 - 22:48h | BAR"

    # LIMPA A TELA E MOSTRA O AMBIENTE
    scene bar
    with dissolve

    show screen cluesUI

    #
    $ narrative_image("bmn", right, None, bmn, "Boa noite, o que desejam beber?") # bmn "Boa noite, o que desejam beber?"
    $ narrative_image("i01", left, None, i01, "Duas cervejas, por favor") # i01 "Duas cervejas, por favor"
    $ narrative_image("bmn", right, None, bmn, "Claro, aqui está") # bmn "Claro, aqui está"
    $ narrative_image("i01", left, None, i01, "Conhece o homem desta imagem?") # i01 "Conhece o homem desta imagem?"
    $ narrative_image("bmn", right, None, bmn, "Quem gostaria de saber?") # bmn "Quem gostaria de saber?"
    $ narrative_image("i01", left, None, i01, "Somos policiais, estamos investigando o caso que envolve ele") # i01 "Somos policiais, estamos investigando o caso que envolve ele"
    $ narrative_image("bmn", right, None, bmn, "Aconteceu algo? Ele faz algum tempo que não aparece") # bmn "Aconteceu algo? Ele faz algum tempo que não aparece"
    $ narrative_image("i02", left, None, i02, "Ele foi encontrado morto em um parque a alguns kilometros daqui") # i02 "Ele foi encontrado morto em um parque a alguns kilometros daqui"
    $ narrative_image("bmn", right, None, bmn, "Já entraram em contato com a família dele?") # bmn "Já entraram em contato com a família dele?"
    $ narrative_image("i02", left, None, i02, "Ele não possui família em nossos registros") # i02 "Ele não possui família em nossos registros"
    $ narrative_image("bmn", right, None, bmn, "Certeza? Ele possui uma irmã, talvez vocês não tenham registro dela, pois ela é filha de outra relação") # bmn "Certeza? Ele possui uma irmã, talvez vocês não tenham registro dela, pois ela é filha de outra relação"
    $ narrative_image("i01", left, None, i01, "Sabe onde ela mora?") # i01 "Sabe onde ela mora?"
    $ narrative_image("bmn", right, None, bmn, "Não, mas sei que ela frequentava uma psiquiatra") # bmn "Não, mas sei que ela frequentava uma psiquiatra"
    $ narrative_image("bmn", right, None, bmn, "Lembro que um dia ele viu ela no programa do Jimmy e pediu para mudar de canal") # bmn "Lembro que um dia ele viu ela no programa do Jimmy e pediu para mudar de canal"
    $ narrative_image("i02", left, None, i02, "Se recorda da última vez que ele estava no bar?") # i02 "Se recorda da última vez que ele estava no bar?"
    $ narrative_image("bmn", right, None, bmn, "Sim, como ele era uma pessoa bem alegre, fica difícil não lembrar quando vem") # bmn "Sim, como ele era uma pessoa bem alegre, fica difícil não lembrar quando vem"
    $ narrative_image("bmn", right, None, bmn, "Na última noite ele estava alegre dançando com uma pessoa ruiva") # bmn "Na última noite ele estava alegre dançando com uma pessoa ruiva"
    $ narrative_image("bmn", right, None, bmn, "Depois de beber algumas eles sairam") # bmn "Depois de beber algumas eles sairam"
    $ narrative_image("i01", left, None, i01, "Sabe a onde foram?") # i01 "Sabe a onde foram?"
    $ narrative_image("bmn", right, None, bmn, "Não, ele pagou e sai fora") # bmn "Não, ele pagou e sai fora"
    $ narrative_image("bmn", right, None, bmn, "Não cheguei a notar nada diferente, ele tem o costume de sair acompanhado") # bmn "Não cheguei a notar nada diferente, ele tem o costume de sair acompanhado"
    $ narrative_image("bmn", right, None, bmn, "Ele vem no bar quase sempre, pois considera aqui um lugar de sorte") # bmn "Ele vem no bar quase sempre, pois considera aqui um lugar de sorte"
    $ narrative_image("i02", left, None, i02, "Muito obrigado, tenha uma boa noite, aqui está nosso cartão, pode ficar com o troco") # i02 "Muito obrigado, tenha uma boa noite, aqui está nosso cartão, pode ficar com o troco"
    $ narrative_image("bmn", right, None, bmn, "A disposição, se caso ela apareça aqui novamente, entro em contato com vocês") # bmn "A disposição, se caso ela apareça aqui novamente, entro em contato com vocês"
    $ narrative_image("i01", left, None, i01, "Agradecemos") # i01 "Agradecemos"

    return
